# U19 Website, Community and Public-Facing Channels - NEUTRAL KNOWLEDGE

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Clean-room layer: plain business and process language only (platform: Odoo 19 Community, named once here).
> Each statement carries an identifier in square brackets that links it to restricted technical claims. No file, module, field or code names appear below.

## CAP-U19-01 Public page serving, visibility levels and publishing control

### WHAT
- [N-U19-001] Website pages are resolved by web address after all dedicated application endpoints and stored files have had their chance; the page store is the last resort of the request router. A page belongs either to one specific website or to all websites, and the most specific match wins.
- [N-U19-002] A separate feature lets an administrator expose any concrete business record type as a public listing and detail pages, filtered by an optional record filter and, when the record type has a publication flag, only for published records.

### WHY
- [N-U19-003] Marketing content must be visible to anonymous visitors while editing, publishing and access restriction stay with a small set of trusted roles.

### BUSINESS RULE
- [N-U19-004] A page can be public, restricted to signed-in users, restricted to members of chosen groups, or protected by a shared password. Visibility is enforced when the page is rendered, and administrators with the design role bypass it.
- [N-U19-005] A page password is stored only as a salted hash. After a visitor supplies it, the page is unlocked for that visitor session only.
- [N-U19-006] A page is shown to visitors only if it is published and any scheduled publication date has passed; designers see unpublished pages.
- [N-U19-007] Changing the published state of a record is allowed only to users who may modify that record, or to the design role for pages; creating an already-published record without that right is refused.
- [N-U19-008] Site search returns only published, indexed pages, hides password-protected pages from everyone except designers, hides signed-in-only pages from anonymous visitors, and respects group restrictions.
- [N-U19-009] Redirections can be defined only by designers; a permanent or temporary redirect is served when no page matches.
- [N-U19-010] The listing feature refuses to expose record types that the anonymous user cannot read, and refuses abstract, temporary or non-table record types.

### STATE
- [N-U19-011] A page moves from draft (unpublished) to scheduled (published with a future date) to visible (published, date reached); it can be unlocked per visitor session when password protected.

### OPTIONALITY
- [N-U19-012] Visibility, publication date, group list, indexing flag, homepage selection and website assignment are per page settings. Anonymous responses can be served from a one-hour response cache.

### DEPENDENCY
- [N-U19-013] Page content is built from stored view templates; access to the content uses the same view store and its own read rules for anonymous and signed-in portal users.

### CONSTRAINT
- [N-U19-014] Only the design role may write pages; the restricted editing role may edit content but may not change page structure. Page addresses are slugged and must be unique per website.

### RISK
- [N-U19-015] The one-hour anonymous response cache is keyed by website, language, address, debug flag and consent state, not by whether the visitor session has unlocked a password-protected page. A page unlocked by one visitor session may therefore be cached and shown to later anonymous visitors. This needs runtime confirmation.
- [N-U19-016] The generic record listing passes the visitor supplied sort expression to the search without a field whitelist and renders any record type readable by the anonymous user, so it widens the public data surface when configured carelessly.
- [N-U19-017] Visibility is checked on the main page view only; other views and data endpoints that the page calls remain reachable.

### UNKNOWN
- [N-U19-018] Not confirmed: whether the ordering expression of the listing feature can order by fields the visitor cannot read, and whether the response cache honours unlocked pages under real traffic.

## CAP-U19-02 Website form submission creating business records

### WHAT
- [N-U19-019] Anonymous visitors can submit forms that create business records directly: sales opportunities, job applications, project tasks, newsletter contacts and outbound emails. The record is created with system rights.

### WHY
- [N-U19-020] The business wants lead capture and applications from the public site without giving visitors accounts or direct data access.

### BUSINESS RULE
- [N-U19-021] A record type can be the target of a public form only if an administrator has flagged it as form-enabled.
- [N-U19-022] Only fields explicitly whitelisted by a designer for a record type can be filled from a form; every field is blocked by default, read-only and technical fields are removed, and unknown extra inputs are appended as free text to a configured notes field or logged as a message.
- [N-U19-023] Uploaded files that do not correspond to a file field become attachments linked to the created record; no size or type limit is applied by the form handler itself.
- [N-U19-024] A public form that sends an email may only target the recipient the page designer configured: the recipient (and any copy recipient) must match a server-generated signature. The sender shown is the company, with the visitor address placed in the reply address and message body.
- [N-U19-025] Optionally, the visitor network address, browser identity, language and referring page are appended to the record.
- [N-U19-026] A lead created from a form takes its source, default team, default salesperson and company from the website, normalises phone numbers, links to the visitor contact when the email matches, and is attached to the visitor profile.
- [N-U19-027] A job application is refused when the target job is archived, and is placed in the first open stage valid for that job.
- [N-U19-028] A task created from a form is linked to an existing contact when the posted email matches one.
- [N-U19-029] A verification challenge is requested on the generic form endpoint, but it is a no-op unless a secret key is configured.

### STATE
- [N-U19-030] Form posted, then target and fields checked, then record created inside a savepoint, then attachments added; on a validation problem nothing is kept and an error list is returned; the last created record is remembered in the visitor session for the confirmation page.

### OPTIONALITY
- [N-U19-031] Which record types accept forms, which fields are open, and whether metadata is stored are all configuration. The challenge needs a configured key pair and a score threshold.

### DEPENDENCY
- [N-U19-032] Needs the visitor tracking feature for lead linking, the sales, recruitment, project and mailing features for their record types, and an external challenge service for bot checks.

### CONSTRAINT
- [N-U19-033] Required fields without defaults must be supplied; database integrity violations return a generic failure; posts from signed-in sessions must carry a valid request token while anonymous posts are exempt.

### RISK
- [N-U19-034] The sales opportunity form accepts the salesperson and sales team as visitor-supplied fields, so an anonymous visitor can route a lead to a chosen user or team instead of the website default.
- [N-U19-035] The public job application pre-check reveals, for a given name, email, phone or profile link, whether an earlier application exists and discloses the recruiter contact details.
- [N-U19-036] Task and registration forms can attach the new record to an existing contact simply by quoting that contact email or identifier, with no proof of ownership.
- [N-U19-037] In this database no challenge secret is configured, so public forms are not protected against automated submission by the challenge feature; no other rate limiting was found in the studied code.
- [N-U19-038] A job application can target any active job identifier, including jobs that are not published on the site, because only the active flag is checked.

### UNKNOWN
- [N-U19-039] Not confirmed: infrastructure level rate limiting, maximum upload size enforced elsewhere, and behaviour of the email form when only a copy recipient is posted.

## CAP-U19-03 Multi-website scoping, company binding, cookie consent and visitor tracking

### WHAT
- [N-U19-040] Several websites can run on one database. The current website is chosen from the session override, then the request context, then the host name, and finally falls back to the first website.
- [N-U19-041] Anonymous and signed-in visitors are tracked as visitor profiles, with tracked page visits, country, language, time zone and links to leads and contacts.

### WHY
- [N-U19-042] Each website needs its own content, user accounts and visibility, while the operator needs visitor insight for sales follow-up and must respect consent obligations.

### BUSINESS RULE
- [N-U19-043] Records carrying a website assignment are visible on that website or on all websites when unassigned; a record bound to another website returns not found when requested directly.
- [N-U19-044] Login names are unique per website, user lookup is restricted to the current website scope, and a new customer account is bound to the website company and optionally to the website itself.
- [N-U19-045] Free sign-up versus invitation-only is a per website setting that overrides the global sign-up setting.
- [N-U19-046] When the consent bar is off, all optional cookies are considered accepted. When it is on, optional cookies and third party embeds are blocked until the visitor accepts, except for editors.
- [N-U19-047] A visitor profile is keyed by the contact (signed-in) or by a hash of network address, browser identity and session; only pages flagged as tracked create visits, bots and requests with an opt-out header are skipped.
- [N-U19-048] On login the anonymous visitor is merged into the contact visitor so visits, leads and chat sessions follow the person.
- [N-U19-049] Anonymous visitors idle for the retention period (60 days by default) are deleted by a daily job unless they have a contact or a lead.

### STATE
- [N-U19-050] Anonymous visitor is created on first tracked page, becomes contact-bound on login (merged), and is deleted after inactivity unless tied to a contact or lead.

### OPTIONALITY
- [N-U19-051] Website domain, company, languages, cookie bar, third party blocking, user account scope, sign-up scope and retention days are configuration.

### DEPENDENCY
- [N-U19-052] Visitor data feeds leads, live chat, events and SMS or email follow-up; geolocation data comes from the request.

### CONSTRAINT
- [N-U19-053] A website domain is unique; a company with a linked website cannot be archived.

### RISK
- [N-U19-054] Visitor creation and page tracking are not gated by the cookie consent setting in the studied code; consent only controls optional cookies and third party embeds.
- [N-U19-055] The optional lead generation from visits feature stores the visitor network address of every matching public page view and sends batches of addresses to an external intelligence service on a daily job, again without a consent check.
- [N-U19-056] All 29 websites in this database have the consent bar disabled, which the code treats as full consent given.
- [N-U19-057] Several public endpoints do not apply website scoping (for example partner profile pages and booth listings), so content assigned to one website may be reachable through another.

### UNKNOWN
- [N-U19-058] Not confirmed: legal basis for tracking in the target jurisdiction, and runtime behaviour of the geolocation lookup.

## CAP-U19-04 Blog, partner showcase pages, and follow subscriptions

### WHAT
- [N-U19-059] The blog publishes articles in blogs with tags, authors, scheduled publication, comments and follower notifications. Partner and customer showcase pages list published organisations with grade, country and industry filters and a map.

### WHY
- [N-U19-060] Marketing content and reference showcases attract visitors, and followers should be told when new content appears.

### BUSINESS RULE
- [N-U19-061] Anonymous and portal users may read only published articles in active blogs; only the design role can edit them. An article scheduled in the future is hidden from non-designers by the page controller.
- [N-U19-062] Publishing an active article posts a notification to followers of its blog; archiving an article unpublishes it.
- [N-U19-063] Public comments on an article are limited to non-internal comment messages, and posting needs only read access to the article.
- [N-U19-064] Any visitor can follow or unfollow a readable record by giving an email address; when a challenge fails an existing contact is looked up but none is created.
- [N-U19-065] A partner page is shown to anyone once the partner is flagged published; it exposes the address, website, phone and email of the partner.
- [N-U19-066] A graded reseller partner can accept, decline or update leads assigned to its commercial entity from the portal; changes are executed with system rights after an ownership check.

### STATE
- [N-U19-067] Article: draft, then published with publication date, then archived (unpublished). Assigned lead: assigned to partner, then accepted (converted to opportunity) or declined (returned with a decline mark, optionally flagged as spam).

### OPTIONALITY
- [N-U19-068] Blog website assignment, article scheduling, comment moderation settings, partner grade publication and map key are configuration.

### DEPENDENCY
- [N-U19-069] Articles depend on the messaging and publishing foundations; showcase pages depend on the geolocation and sales team features.

### CONSTRAINT
- [N-U19-070] A portal user may modify only leads whose assigned partner belongs to their commercial entity; only reseller partners with a grade may create opportunities from the portal.

### RISK
- [N-U19-071] Unfollowing and following require no proof of email ownership, so anyone who knows an address can remove its owner from a notification list.
- [N-U19-072] Showcase pages and the map endpoint read partner records with system rights, so a partner published on one website is reachable from any website, and the map result size is chosen by the requester.
- [N-U19-073] The portal stage change accepts any stage identifier without checking it belongs to the lead pipeline.
- [N-U19-074] Article bodies are stored without HTML sanitising, so anyone allowed to edit articles can publish script content.

### UNKNOWN
- [N-U19-075] Not confirmed: comment moderation behaviour of the portal messaging layer and the content of the showcase templates beyond the address block.

## CAP-U19-05 Community forum and public profiles with reputation-gated actions

### WHAT
- [N-U19-076] A community forum lets signed-in users ask questions, answer, comment, vote, flag and moderate, with every action gated by a reputation score. Public profiles show reputation, badges and activity.

### WHY
- [N-U19-077] Self-moderating communities reduce staff effort: trust is earned by reputation rather than granted by role.

### BUSINESS RULE
- [N-U19-078] A forum is public, visible to signed-in users, or private to one chosen group; anonymous users can read only public forums and their content.
- [N-U19-079] Each action (ask, answer, comment, vote, edit, retag, close, delete, flag, moderate) has its own reputation threshold per forum, with separate thresholds for own and others posts. Defaults include 3 to ask or answer, 100 to post without validation and 1000 to moderate.
- [N-U19-080] A question from an author below the validation threshold stays pending until a moderator validates it.
- [N-U19-081] Links and images in posts require editor reputation; below the do-follow threshold links are marked non-followed.
- [N-U19-082] A profile is visible to others only if its owner published it and the viewer has the minimum reputation (150 by default); owners always see their own profile.
- [N-U19-083] An avatar is served to anonymous visitors only for published profiles with positive reputation.

### STATE
- [N-U19-084] Post: pending, then active, then flagged, closed or offensive, with reopen and delete paths; each transition has a reputation requirement and awards or removes reputation.

### OPTIONALITY
- [N-U19-085] Forum privacy, mode (single answer or discussion), every reputation threshold and the minimum profile reputation are settings.

### DEPENDENCY
- [N-U19-086] Reputation and badges come from the gamification feature; profile pages are shared with the online learning feature.

### CONSTRAINT
- [N-U19-087] Posting requires a signed-in user with a valid email address; replying to a closed or deleted question is refused.

### RISK
- [N-U19-088] Portal users hold full table level rights (read, create, change, delete) on posts; the real protection lies in the model checks, so any new write path must repeat them.
- [N-U19-089] A public endpoint redirects from a contact identifier to the forum page of the linked user, confirming whether a contact has a user account.
- [N-U19-090] The forum module sets the global sign-up scope to free sign-up, but in this database each website overrides it with invitation-only, so free public registration is currently closed.

### UNKNOWN
- [N-U19-091] Not confirmed: reputation gaming through vote rings and the full set of moderation queue routes.

## CAP-U19-06 Online courses: visibility, enrolment, invitations and completion

### WHAT
- [N-U19-092] Courses with lessons, categories, quizzes and certifications can be published to the website, with enrolment, progress tracking, reviews and reputation rewards.

### WHY
- [N-U19-093] Training content is delivered at scale while keeping paid or internal courses restricted.

### BUSINESS RULE
- [N-U19-094] A course is visible to everyone, to signed-in users, only to enrolled attendees, or to anyone holding the link; anonymous users may open only published public or link courses and only lesson previews and category headings.
- [N-U19-095] Enrolment is either open to any signed-in user or by invitation; invitation-only courses can be joined only after being invited, and attendee-only visibility forces invitation enrolment.
- [N-U19-096] An invitation link carries a recipient and a keyed hash; pending invitations expire after three months and a valid link lets an anonymous visitor preview the course and obtain a sign-up link for the invited contact.
- [N-U19-097] Publishing a course or lesson is allowed to the course responsible, or to the manager role for documentation courses and group uploads.
- [N-U19-098] Quiz completion requires one answer set covering all questions; completion awards reputation and may raise the user rank; attempts are counted.
- [N-U19-099] Lessons can be embedded in outside sites; embedded views from outside increment an embed counter and record the referring address.

### STATE
- [N-U19-100] Attendee: invited, then joined, then completed; lesson: not viewed, viewed, completed; progress recomputes course completion.

### OPTIONALITY
- [N-U19-101] Course visibility, enrolment type, auto-enrol groups, upload groups, reputation values, prerequisites and review thresholds are settings.

### DEPENDENCY
- [N-U19-102] Reputation, ratings, surveys for certifications, signed invitation emails and the sign-up flow.

### CONSTRAINT
- [N-U19-103] Officers manage only courses they are responsible for; managers manage all; attendees read downloadable resources only for courses they belong to.

### RISK
- [N-U19-104] The external embed route writes to the lesson (embed counter and referrer) before it checks that the visitor may read the lesson, so anonymous requests can inflate statistics for restricted lessons.
- [N-U19-105] The invitation hash for an enrolled member has no expiry and the link can be used to create a sign-up token for a contact that has no user yet.
- [N-U19-106] The quiz submission accepts any answer identifiers for the quiz questions; completeness is checked per question, not that each question has a single chosen answer.

### UNKNOWN
- [N-U19-107] Not confirmed: certification flows with surveys, payment for courses, and slide file download access tokens.

## CAP-U19-07 Live chat sessions, chat bots and visitor conversion

### WHAT
- [N-U19-108] Visitors can open a chat from the website with an available agent or an automated chat bot; sessions are stored as conversations, rated by the visitor, convertible to leads, and linked to the visitor profile.

### WHY
- [N-U19-109] Real-time support and qualification of website traffic with traceability of every conversation.

### BUSINESS RULE
- [N-U19-110] Starting a session needs no login: anonymous visitors receive a temporary guest identity and the conversation is created with system rights on a chosen chat channel.
- [N-U19-111] Agents are chosen by availability, language, country and expertise within the channel capacity; a bot can be chosen only if one of the channel rules lists it.
- [N-U19-112] Channel rules show, hide or auto-open the chat button by web address pattern and visitor country; they drive the button display, not the ability to start a session.
- [N-U19-113] Bot scripts guide the visitor through questions, collect email and phone, can create a contact from the typed email, and can forward the visitor to an agent or create a lead.
- [N-U19-114] One rating per conversation is allowed from the conversation participant; a repeat submission overwrites the earlier rating.
- [N-U19-115] Livechat users can read every live chat conversation; managers can configure channels, bots and view reports.

### STATE
- [N-U19-116] Conversation: in progress, then closed by visitor or agent, optionally pending as an operator-initiated chat request that is cancelled if the visitor starts their own chat.

### OPTIONALITY
- [N-U19-117] Agents, maximum concurrent sessions, rules, bot scripts, languages and review link.

### DEPENDENCY
- [N-U19-118] Visitor profiles for page history, contacts for visitor-to-partner mapping and the lead feature for conversions.

### CONSTRAINT
- [N-U19-119] Only internal users can email a transcript; the bot email step rejects invalid addresses.

### RISK
- [N-U19-120] The session start endpoint is anonymous and creates a conversation each call without a challenge or visible rate limit, so it can be used to flood agents or storage.
- [N-U19-121] A bot step that captures an email creates a new contact record from anonymous input.
- [N-U19-122] Because rules only control the button, a visitor can start a conversation on a channel whose rule hides the button.

### UNKNOWN
- [N-U19-123] Not confirmed: guest authentication cookie lifetime, operator presence calculation under load and the attachment upload limits of live chat.

## CAP-U19-08 Public event registration and booth booking

### WHAT
- [N-U19-124] Published events show tickets, optional time slots and registration forms; visitors can register attendees and book sponsor booths without an account.

### WHY
- [N-U19-125] Self-service registration reduces organiser workload and captures leads.

### BUSINESS RULE
- [N-U19-126] Anonymous and portal users read events, tickets, slots, questions and tags only for published events.
- [N-U19-127] Seat availability is checked per ticket and slot before creating registrations, and again by a constraint when registrations are saved; tickets must be launched and not expired.
- [N-U19-128] Registrations created from the site are made with system rights, linked to the visitor profile and to the visitor contact or the signed-in contact.
- [N-U19-129] Only name, phone, email, company, event, slot, ticket and contact fields are accepted from the registration form.
- [N-U19-130] A booth booking requires available booths of a single category; confirmation books them immediately for a contact found or created from the posted email; an anonymous request using the email of an existing contact is refused.
- [N-U19-131] Registrations can generate leads according to rules, enriched with the visitor and answers to event questions.

### STATE
- [N-U19-132] Registration: draft or confirmed according to event settings; booth: available, then booked on confirmation.

### OPTIONALITY
- [N-U19-133] Seats limit, slots, ticket windows, questions, booth categories, and lead rules.

### DEPENDENCY
- [N-U19-134] Visitor profile, event and booth features, optional lead rules and reCAPTCHA.

### CONSTRAINT
- [N-U19-135] Seat checks raise an error when capacity is exceeded; unknown tickets are refused.

### RISK
- [N-U19-136] The form accepts a contact identifier from the visitor, so a registration can be attached to any existing contact.
- [N-U19-137] The booth booking refusal for an existing email lets an anonymous party test whether an address belongs to a known contact.
- [N-U19-138] Booth listing endpoints read booths with system rights for any event identifier, including events that are not published.
- [N-U19-139] Seat checks happen before creation; whether concurrent submissions can exceed capacity depends on the saving constraint under load and needs runtime confirmation.

### UNKNOWN
- [N-U19-140] Not confirmed: payment for tickets (the shop feature is not installed), sponsor and track features that need other modules.

## CAP-U19-09 Newsletter subscription, public mailing groups and rating feedback links

### WHAT
- [N-U19-141] Visitors can subscribe to newsletters by email or phone, join or leave public discussion groups, and rate a service through a one-click email link.

### WHY
- [N-U19-142] Opt-in audience building and customer satisfaction measurement without requiring accounts.

### BUSINESS RULE
- [N-U19-143] A newsletter subscription form creates the contact if needed and subscribes it to the chosen list; if the address had opted out it is re-subscribed; no confirmation email is required.
- [N-U19-144] The newsletter endpoint takes a list identifier from the request; it does not check that the list is public.
- [N-U19-145] Unsubscribing from a mailing needs a keyed token for the recipient, mailing and address, except for logged-in internal users managing their own page.
- [N-U19-146] Joining or leaving a group as an anonymous visitor sends a confirmation email carrying a keyed token; signed-in users act directly. A group-level token allows access to a group otherwise not visible.
- [N-U19-147] Group archives are readable according to group access mode (public, members only, authorised group) and only for accepted, non-rejected messages.
- [N-U19-148] A rating link carries a random token; the rating can be submitted or changed through the token without login, and the result is posted on the rated record.
- [N-U19-149] Publishing a comment on a rating needs the website editing role or write access to the rated record.

### STATE
- [N-U19-150] Subscription: not subscribed, subscribed, opted out (re-subscribable by any visitor); group member: pending confirmation, member, removed; rating: requested, submitted, resubmittable.

### OPTIONALITY
- [N-U19-151] List public flag, group access mode, moderation and reCAPTCHA keys.

### DEPENDENCY
- [N-U19-152] Mass mailing, mail group, contact verification emails and the rating feature.

### CONSTRAINT
- [N-U19-153] Token checks use keyed hashes; rating values are limited to three levels.

### RISK
- [N-U19-154] Subscribing an address the visitor does not own, and re-subscribing an opted-out address, require no confirmation, which weakens consent evidence.
- [N-U19-155] Any list identifier can be targeted, including non-public lists.
- [N-U19-156] The group index and subscribe endpoints confirm whether an email address is a member of a public group.
- [N-U19-157] The group confirmation email can be triggered to arbitrary addresses by anonymous requests that know a group token.
- [N-U19-158] A rating token is reusable and has no expiry in the studied code.

### UNKNOWN
- [N-U19-159] Not confirmed: mail group moderation and posting by email, and the delivery behaviour of the outgoing mail server.

## CAP-U19-10 Donation payment hook and public integration endpoints

### WHAT
- [N-U19-160] The website payment bridge adds donations, website-specific payment providers and a payment method showcase. Other public endpoints fetch link previews, import stock photos, shorten links and serve map data.

### WHY
- [N-U19-161] Accept donations through the same payment engine as other payments and give editors convenient media tools.

### BUSINESS RULE
- [N-U19-162] A payment provider may be restricted to one website; the payment page shows only providers matching the current website.
- [N-U19-163] An anonymous donation uses a shared contact record; name, email and country are mandatory, and the transaction notes the donor details.
- [N-U19-164] A donation transaction sends an immediate notification email to the recipient address and comment given in the request, before payment completes, and later a confirmation to the donor when it succeeds.
- [N-U19-165] The minimum donation amount is taken from the request address.
- [N-U19-166] An anonymous endpoint fetches an outside web address and returns its title, description and image.
- [N-U19-167] Only signed-in users can import images, and only from approved stock image hosts; the application key is stored in settings.
- [N-U19-168] Short links are created and measured by signed-in users and redirect anonymously and permanently to the stored target.

### STATE
- [N-U19-169] Donation transaction: created, pending, done or failed, with the confirmation email only when done.

### OPTIONALITY
- [N-U19-170] Provider website assignment, donation snippet options and stock image keys.

### DEPENDENCY
- [N-U19-171] Needs the payment and invoicing payment modules; the online shop is not installed in this database.

### CONSTRAINT
- [N-U19-172] Currency and amount are signed by a keyed access token for anonymous donors.

### RISK
- [N-U19-173] The donation endpoint lets an anonymous caller choose the recipient and text of an email sent from the company address, which can be abused as a spam relay.
- [N-U19-174] Because the minimum amount comes from the request, the minimum can be bypassed by editing the address.
- [N-U19-175] The anonymous link preview endpoint performs server side requests to arbitrary web addresses following redirects, so it may reach internal network services unless blocked elsewhere.
- [N-U19-176] The payment provider callback base address is derived from the incoming request host, so a forged host header can influence callback addresses.
- [N-U19-177] Short link redirects are open redirects by design; the creation is restricted to signed-in users.

### UNKNOWN
- [N-U19-178] Not confirmed: network level protection against internal address fetching, real provider callbacks, and the stock image service behaviour (all need runtime).

