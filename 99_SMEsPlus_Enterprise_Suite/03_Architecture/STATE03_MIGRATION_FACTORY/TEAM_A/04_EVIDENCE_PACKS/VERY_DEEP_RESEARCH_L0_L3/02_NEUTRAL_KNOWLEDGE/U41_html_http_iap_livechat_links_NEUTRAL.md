# U41 html_http_iap_livechat_links — NEUTRAL KNOWLEDGE

> Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**
> Source system: Odoo 19 Community (named once in this header).
> Neutral layer: process and rule statements only; technical identifiers are kept in the restricted layer.

## CAP-U41-01 Paid external service accounts, credits and what leaves the system

**WHAT**
- [N-U41-001] A shared platform component lets the system buy and consume paid external services (for example lead enrichment, text messages, postal letters and company lookups) through service accounts held inside the system; it installs itself automatically with the web platform and holds no accounting data.
- [N-U41-002] Each service account links one external service to an optional list of companies and holds a secret token, a displayed balance, a low-balance alert threshold with its recipients and a registration state; an account created without a name takes the service name.
- [N-U41-003] A catalogue of services records the name, description, unit (credits, stamps, enrichments) and whether balances are whole numbers; only the lead generation service is seeded by the shared component itself, the others come from the modules that use them.
- [N-U41-004] Every request to the external provider is a single remote call carrying the account token and the request data, with a short default time limit.

**WHY**
- [N-U41-005] Features need to tell apart no account (zero credit), a failed lookup (minus one) and a real balance, so they can warn users before work is lost.
- [N-U41-006] Users must be able to top up credits from inside the application; the link carries the database identifier, the service name and a hash of the token, and a direct link to the account screen is offered only to technical users.

**BUSINESS RULE**
- [N-U41-007] When several accounts exist for one service an account tied to an active company is used before a company-less account, otherwise the newest; asking for a service that does not exist is an error; a missing account is created on first use.
- [N-U41-008] Opening an account screen refreshes the balance, threshold and registration state and locks the service choice by asking the provider; balances are rounded to four decimals unless the service counts whole units.
- [N-U41-009] The alert threshold may not be negative and every alert recipient must have an email address.
- [N-U41-010] An out-of-credit answer is raised as its own distinct error so that a feature can show a buy-credits message; every other provider problem (timeout, transport error, generic server error) becomes a general access error that names only the address contacted.
- [N-U41-011] Public mailbox providers are excluded when looking for company information; for those the whole address is treated as an individual, very short addresses can be skipped, and a fixed list of countries decides where state filtering is offered when mining leads.
- [N-U41-012] Success, error and out-of-credit notices are shown only to the user who triggered the action; the out-of-credit notice offers a buy-credits link; enrichment notes in the record history show provider-supplied logo and social links.

**STATE**
- [N-U41-013] In a neutralised copy of the database account tokens are rewritten with a disabled marker and new accounts are created disabled, so a test copy cannot spend real credits; the hash used for buy links ignores that marker.

**OPTIONALITY**
- [N-U41-014] The provider address defaults to the vendor host and can be overridden by a system parameter; the current database does not override it.
- [N-U41-015] Where the messaging component is installed, accounts become threaded records, changes to companies, threshold and recipients are tracked and a chatter is shown.
- [N-U41-016] A small bridge adds the provider reveal identifier to leads and keeps it when leads are merged; enrichment skips leads that already carry one and skips inactive leads, leads without a valid email and leads at full probability.

**DEPENDENCY**
- [N-U41-017] Text messages, postal letters, company lookups, lead enrichment, lead generation, the editor text helper and website features call the provider through the shared helper; the editor text helper sends no account token.
- [N-U41-018] Failures to reach the provider while refreshing information or updating alert settings are logged and ignored locally, so local settings can differ from the provider; enrichment commits batch by batch and stops at the first out-of-credit answer.

**CONSTRAINT**
- [N-U41-019] Every internal user can read and create service accounts and sees global accounts and accounts of the active companies; only administrators edit or delete them; services are read-only for users.
- [N-U41-020] The account token is a secret readable only by administrators and displayed only in technical mode, although accounts themselves are readable by every internal user.

**RISK**
- [N-U41-021] Calls to the provider send the account token, the database identifier, alert recipient emails with languages, lead identifiers with company web domains for enrichment and, through the consuming modules that send messages or letters, the content and recipient details of what is sent (payload fields not read in detail).

**UNKNOWN**
- [N-U41-022] What the provider keeps from tokens, database identifiers, recipients and payloads, how credits are priced and limited, and whether tokens rotate cannot be derived from the source and needs the provider terms and a captured runtime request.

## CAP-U41-02 Language-prefixed public addresses, language choice and redirects

**WHAT**
- [N-U41-023] A routing layer adds language handling to public website pages: when several languages are active the visitor language appears as a short prefix in the address, while back-office and data routes are left untouched.

**WHY**
- [N-U41-024] Addresses are redirected permanently to one canonical form (record name plus number, in the visitor language) so search engines see a single address per page.

**BUSINESS RULE**
- [N-U41-025] The visitor language is chosen in this order: the language in the address, the remembered language cookie, the user or context language, then the site default; each is mapped to the nearest installed language.
- [N-U41-026] Browsing pages are multilingual by default, data-style routes are not by default, a route can say otherwise, and submitted forms are never redirected.
- [N-U41-027] The browser is redirected to add a missing prefix for a non-default language, to remove the prefix of the default language, to replace a long alias by the short prefix, and to drop the trailing slash on a language home page; a valid prefix is removed internally before the page is served.
- [N-U41-028] Addresses containing a double slash are merged by a permanent redirect.
- [N-U41-029] Automated clients such as crawlers and link previewers are recognised by the descriptive text the client sends about itself and are not redirected for a missing prefix; they receive the default language.
- [N-U41-030] Routes not flagged as website routes skip all language processing and a request already rewritten is not processed twice.

**STATE**
- [N-U41-031] The chosen language is remembered in a cookie that is refreshed only when it differs from the language being served.
- [N-U41-032] An address that matches nothing is still treated as a website page so that the not-found page uses the site layout.

**OPTIONALITY**
- [N-U41-033] With a single active language, as in the current database, prefixes are neither added nor removed unless forced; the redirect behaviour becomes relevant only after a second language is activated.
- [N-U41-034] The default language is the stored default for the contact language, else the first active language; the current database has one such stored default and one active language.

**DEPENDENCY**
- [N-U41-035] Which languages are offered is the set of active languages, narrowed by the website component when installed; each language has a unique short code for addresses, and activating a language prefers the short code when it is free.
- [N-U41-036] Links in pages are rewritten to carry the right prefix; only relative addresses outside static and back-office areas are rewritten; if a page cannot be rebuilt in another language the original is kept; canonical addresses are absolute and carry no query string.

**CONSTRAINT**
- NOT APPLICABLE — the routing layer owns no stored data; its only data constraint (a unique short code per language) is described under dependency.

**RISK**
- [N-U41-037] Automated-client detection trusts the text a client sends about itself, so any client can claim to be a crawler to avoid language redirects.

**UNKNOWN**
- [N-U41-038] Behaviour with two or more active languages, with website language sets, behind a caching proxy and for automated clients was read but not executed and needs a runtime test after a second language is activated.

## CAP-U41-03 Readable address segments, public translations and frontend error pages

**WHAT**
- [N-U41-039] Public page addresses can contain a readable name followed by the record number; only the trailing number identifies the record, a name that cannot be made readable is replaced by the bare number, a negative number that does not exist falls back to its positive value, and templates receive helpers to build such addresses.

**WHY**
- [N-U41-040] Public pages load their interface translations from a public route that serves the base set plus extra modules the page asks for; the logout address is never language-prefixed.

**BUSINESS RULE**
- [N-U41-041] Failures on public pages are shown with the site layout: a user-facing error keeps its own status and message, not-found and forbidden first try attachments and pages, server errors show a generic page, an error raised inside a nested template is reported as a server error, the transaction is rolled back before display, and if the error page itself fails a minimal page is shown with a teapot status.

**STATE**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**OPTIONALITY**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**DEPENDENCY**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**CONSTRAINT**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**RISK**
- [N-U41-042] The full error trace is always passed to the page and shown whenever debug mode is on for the session; debug mode can be switched on through the address itself without any role check, so an anonymous visitor may be able to read an error trace on a failing public page.

**UNKNOWN**
- [N-U41-043] Whether another layer prevents an anonymous visitor from obtaining an error trace through the debug argument was not established and needs a runtime request to a failing public address.

## CAP-U41-04 Tracked short links, click counting and redirect, and link shortening in content

**WHAT**
- [N-U41-044] A tracked link wraps any web address into a short address on the system own domain, counts clicks and carries campaign, medium and source labels; deleting a campaign, medium or source leaves the link in place.

**WHY**
- [N-U41-045] Marketing content is rewritten so that every eligible link becomes a tracked short link whose label is the link text truncated to forty characters; mail, phone and message links, already-short links, unsubscribe links and excluded paths are left alone.

**BUSINESS RULE**
- [N-U41-046] The same address, campaign, medium, source and label combination exists only once; asking again returns the existing link.
- [N-U41-047] A link has one or more short codes made of letters and digits, at least three characters long and unique across the whole system; the displayed code can be edited; codes are created without needing special rights.
- [N-U41-048] An address may not point to the current page, and an address with an unusual scheme is prefixed so it cannot run as a script; this check happens at creation only.
- [N-U41-049] The destination receives the campaign, medium and source labels as query parameters; an optional system setting keeps labels off links to other websites; creating a link never takes labels from the creator browser cookies.
- [N-U41-050] Visiting a short address records a click (except for automated clients) and sends the visitor to the destination by a permanent redirect that may point to any host; an unknown code gives a not-found answer.

**STATE**
- [N-U41-051] A click stores the visitor network address and country; the click count of a link and of a campaign is derived from the stored clicks.

**OPTIONALITY**
- [N-U41-052] Short links are optional marketing functionality that depends only on campaign labels and messaging; it adds no accounting, stock or tax data.

**DEPENDENCY**
- [N-U41-053] Mass mailing marks a message opened and clicked when a click carries its trace and fills campaign and mailing from it; a website tool lets signed-in users create links and view statistics.

**CONSTRAINT**
- [N-U41-054] Internal users can read links, codes and clicks, only administrators change them, the public has no access, the menu appears only in technical mode, and no record rules exist; other roles create links through elevated rights or extension access.

**RISK**
- [N-U41-055] Any valid short code redirects with no confirmation step, the short code is the only protection and the smallest code space is small; for visitors in a non-default language the redirect may first be bounced through a prefixed address.
- [N-U41-056] Creating a link without a title makes the server fetch the destination page; the fetch follows redirects and has no destination filter, so whoever chooses the destination can make the server request it.

**UNKNOWN**
- [N-U41-057] Rate limits against code guessing, effects of browser caching of the permanent redirect on counts, and exactly what the server fetches at creation cannot be established from the source and need a runtime test.

## CAP-U41-05 Editor media, attachments, previews and outbound calls

**WHAT**
- [N-U41-058] A rich-text editing component provides media, image and attachment handling, video embedding, link previews, text generation, collaboration messages and decorative shapes for back-office and public pages; it holds no business data and only test records have access rules.

**WHY**
- [N-U41-059] Several people can edit the same document field; editing steps are announced on a private channel that requires read and write rights on the document and field, and anonymous users cannot subscribe.

**BUSINESS RULE**
- [N-U41-060] Editing, media, text generation and internal preview routes require a signed-in user; decorative shapes and external link previews are public.
- [N-U41-061] Uploaded and added images must be of a supported type (including vector images); content is checked, reprocessed and reused by checksum; an image used by a page cannot be deleted; attachments on pages are public and others private; modifying an image needs read access to the source and write access to the target; image rights are bypassed only by an extension, in which case an access token is generated; library images are stored with elevated rights.
- [N-U41-062] Only five video platforms are accepted; embed addresses are rebuilt from the extracted identifier; related tracking is limited where the platform supports it; thumbnails are fetched from the platform by the server.
- [N-U41-063] Decorative shape colours must be hexadecimal or colour-function values or one of five theme colour names; illustration shapes come only from public attachments; image shapes embed an image the requester can read.
- [N-U41-064] Internal previews read the record under the requester own rights and return error text instead of failing.

**STATE**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**OPTIONALITY**
- [N-U41-065] Text generation is available to every signed-in user, uses a default vendor address that a parameter can override, has no switch in the component, and maps vendor answers to too-long, limit-reached and failure messages.

**DEPENDENCY**
- [N-U41-066] The component contacts external hosts: media library search and download with the database identifier, the text service, link preview pages, video platform thumbnails and remote images referenced by saved markup.

**CONSTRAINT**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**RISK**
- [N-U41-067] Adding an image by address makes the server contact an address chosen by the user, library downloads have no time limit, and remote images in saved markup are downloaded by the server; no destination filtering is visible.
- [N-U41-068] The external link preview is open to anyone and returns the title, description and image of any address, so an anonymous caller can make the server request a chosen address.

**UNKNOWN**
- [N-U41-069] Server egress controls for previews, library, text and image downloads, and all editor plugins running in the browser were not read and need a network test and a front-end review.

## CAP-U41-06 In-place editing save-back, snippets, field converters and revision history

**WHAT**
- [N-U41-070] Pages edited in place are saved back: fields embedded in the markup are converted from displayed text to stored values by type and written to the record named in the markup under the editor own rights; conversion errors are reported as validation errors naming the field.
- [N-U41-071] Editable blocks become extension views of the page view, edited views are protected from being overwritten by module upgrades, only a few attributes of the section root can change, and unchanged edits are not written.

**WHY**
- [N-U41-072] Versioned fields keep up to three hundred revisions with the author and time, patches ignore collaboration step markers, history cannot be written directly, and a save whose collaboration history diverges from the stored one is refused so simultaneous editors do not overwrite each other; this is used by project task descriptions and by job description saves.

**BUSINESS RULE**
- [N-U41-073] Custom building blocks are saved as new views with unique keys and a registration view, names are made unique, translations are copied only where still untranslated, deleting removes both parts, install placeholders are shown to administrators only, and related-view lists are filtered by the requester groups.
- [N-U41-074] Dates and date-times use the user format and time zone (a conversion failure is logged and the plain value kept), selections are matched by displayed label, and relation edits write only when the target exists.
- [N-U41-075] Fields whose stored content would be altered by cleaning are made non-editable for editors who cannot override cleaning, field cleaning settings are exposed to the editor, and remote images are re-encoded to drop hidden data.

**STATE**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**OPTIONALITY**
- [N-U41-076] Query flags for editing, translation editing and translatable mode are accepted from any request and set editor context for the whole dispatch.

**DEPENDENCY**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**CONSTRAINT**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**RISK**
- [N-U41-077] The target record and field of a saved embedded value come from the submitted markup; only the editor normal access rights limit what can be written.

**UNKNOWN**
- [N-U41-078] The callers of the section save and the browser-side cleaning of submitted markup were not read and need a review of the website and editor front end.

## CAP-U41-07 Live chat channel set-up, operators, rules and operator selection

**WHAT**
- [N-U41-079] A live chat channel defines the button text and colours, welcome message, optional review link, agents, rules and capacity, and offers an external script and a public support page; a new channel starts with its creator as agent and joining as agent needs the live chat role.
- [N-U41-080] Live chat is an optional application that depends on discussion, ratings, digest and campaign modules; it has no accounting, stock or tax effect.

**WHY**
- [N-U41-081] Live chat results appear in the periodic digest (happiness, conversations handled, time to answer) together with a tip whose image is hosted externally.

**BUSINESS RULE**
- [N-U41-082] Capacity per operator is unlimited by default or limited to a positive number; a conversation counts as ongoing only if it is not ended and was active in the last fifteen minutes; remaining capacity excludes agents in a call when calls block assignment.
- [N-U41-083] A channel is offered when a chatbot rule exists or at least one agent is online, under capacity and not blocked by a call, so the button can appear with no human online.
- [N-U41-084] Operator choice prefers the previous operator, avoids giving two sessions to one operator within two minutes, then tries eight tiers of language, country and expertise matches, and picks the least recently busy operator at random among ties.
- [N-U41-085] Rules decide the button behaviour by page address pattern and visitor country; country rules are tried first; a bot rule can depend on agent availability; inactive or empty bots are skipped; actions are show, show with notification, open automatically and hide.

**STATE**
- [N-U41-086] Agent membership follows role membership: removing the live chat role removes the user from every channel; users may edit their own live chat name, languages and expertise, which colleagues can see.

**OPTIONALITY**
- [N-U41-087] In the current database one channel exists with one agent and no rules, there are no conversations, and the counts of access rows, record rules, groups, menus and views match the module definition.

**DEPENDENCY**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**CONSTRAINT**
- [N-U41-088] Live chat users read channels and every live chat conversation, member and call history; only administrators create, edit or delete channels, bots and reports; the administrator group implies the user group and canned-response administration; menus follow the same roles with technical menus hidden outside technical mode.

**RISK**
- [N-U41-089] Ordinary operators can create and edit display rules, so they can change which pages show the chat button.

**UNKNOWN**
- [N-U41-090] Presence and message-bus behaviour, behaviour of capacity counts under load, and geolocation availability need a runtime test.

## CAP-U41-08 Visitor session creation, public and cross-origin surface, feedback, transcripts and session end

**WHAT**
- [N-U41-091] A visitor starts a chat through a public route; the system picks a bot or agent, creates the conversation and an anonymous identity for visitors who are not signed in, adds visitor and operator as members, names the conversation, pushes it to the operator and returns a token for later calls; if nobody can answer nothing is created.

**WHY**
- [N-U41-092] The chat can be embedded on external websites: cross-origin routes accept the visitor token instead of cookies, run as the public user and serve scripts and fonts to any origin; one initialisation route appears to be unused.

**BUSINESS RULE**
- [N-U41-093] Public routes give not-found for an unknown channel; the loader and support page show only presentation data of a channel; visitors never see operator-only settings.
- [N-U41-094] Which pages show the button is decided from the page address the browser reports, which the client controls, so rules are display hints and not a security boundary.
- [N-U41-095] One rating exists per conversation and later feedback updates it; the rated person is the first partner of the conversation, which may not be the operator; the rating value is taken from the request.
- [N-U41-096] Visitors can send the operator the list of pages they visited; the route accepts any partner that is a member of the conversation; the list is shown as links that are escaped but not checked for scheme.
- [N-U41-097] Internal users can email a transcript to any address from the company mailbox, and visitors can download a document of their own conversation; an invalid address would fail without a friendly message.

**STATE**
- [N-U41-098] A conversation ends when the visitor leaves, the last operator leaves, a bot script finishes, or after a day of inactivity without an agent; empty conversations are deleted after an hour; a closed conversation refuses visitor attachments; visitors cannot start calls; a visitor can reopen a bot conversation by restarting it.

**OPTIONALITY**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**DEPENDENCY**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**CONSTRAINT**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**RISK**
- [N-U41-099] Public creation of conversations has no throttle, captcha or token check in the code, so volume control depends on the infrastructure.

**UNKNOWN**
- [N-U41-100] Throttling at the proxy, limits on anonymous identities, websocket behaviour for embedded use and whether guest access rules fully prevent misuse of history, restart and trigger routes need a runtime test.

## CAP-U41-09 Chatbot scripts, steps, visitor data capture and hand-over to a human

**WHAT**
- [N-U41-101] A chatbot script is an ordered list of steps (text, question with answers, email, phone, free input, forward to an operator; the sales bridge adds create-lead steps) with an archived partner acting as the bot author; question steps must have answers, step order is assigned automatically, copies remap conditional triggers, and the editor warns about unsuitable first steps.

**WHY**
- [N-U41-102] The leading text steps up to the first non-text step are shown to the visitor without being stored until the visitor interacts, to avoid filling conversations with bot lines for visitors who never answer.

**BUSINESS RULE**
- [N-U41-103] The next step is the first later step whose trigger answers are all satisfied (any one answer per earlier question, all earlier questions together); a non-question step with no next step ends the script and closes the conversation; an answer must belong to the step it answers; while a bot is active and no human has joined every message is tied to the current step.
- [N-U41-104] Email, phone and free-input answers are stored for later use; an invalid email is rejected without advancing; for anonymous visitors a partner is created from the typed contact data using the email as name; for signed-in visitors the contact data fills only empty partner fields; the create-lead step builds an unassigned lead with the whole conversation text in its description.
- [N-U41-105] A forward step hands the visitor to an available human: the step message is posted, the agent joins, the bot leaves silently, the conversation is renamed and pushed to the agent; if no one is available the failure state is set and the bot keeps talking so later steps still run; expertise on the step steers the choice.

**STATE**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**OPTIONALITY**
- [N-U41-106] In the current database two scripts exist and are active, a welcome bot seeded by the module and a lead generation bot from the sales bridge; no channel rule uses them yet.

**DEPENDENCY**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**CONSTRAINT**
- [N-U41-107] Only live chat administrators manage scripts, steps, answers and bot messages and see the chatbot menu; visitors act through elevated rights inside the controllers.

**RISK**
- [N-U41-108] The restart and step routes take the script identifier from the request and do not check it against the scripts attached to the channel, so a visitor can drive any existing script and post as its bot author.

**UNKNOWN**
- [N-U41-109] Whether the guest-scoped conversation search restricts restart, answer and trigger calls to the caller own conversation in every case needs a runtime test with two anonymous visitors.

## CAP-U41-10 Conversation handling after the first reply: status, escalation, history, tags, ratings and reporting

**WHAT**
- [N-U41-110] Conversations carry a status (in progress, waiting for customer, looking for help); an ended conversation must have no status; a help request is pushed to all live chat users and withdrawn when someone joins or the status changes; a visitor reply returns a waiting conversation to in progress.
- [N-U41-111] A history row is kept for each participant of a conversation (one per partner or anonymous visitor), only live chat conversations are allowed, a member added without a type is an agent unless the visitor signed in after chatting anonymously, and live chat users can read histories.

**WHY**
- [N-U41-112] The first agent reply clears the never-answered failure and records the response time once; message counts ignore notifications; a conversation with more than one agent is escalated, the first agent being the one who asked for help; the outcome calculation assigns to the whole set of conversations and so may give one value to several conversations recalculated together.

**BUSINESS RULE**
- [N-U41-113] Notes and statuses can be changed by any non-portal user who can read the conversation; tags need write access to tags and have unique names; expertise changes accept only link and unlink and need the live chat role; creating an expertise from a conversation relies on the access rows only.
- [N-U41-114] Satisfaction counts only ratings of the last fourteen days; ratings map to unhappy, neutral and happy; one rating per conversation is attached to the rated agent or bot history.
- [N-U41-115] A reporting view over live chat conversations shows duration, message count, time to answer (empty when the reply came after the end), outcome, bot or agent handling, call duration, chatbot answer path and expertise; it is read-only and limited to live chat administrators; the transcript layout uses the channel colours and the company logo.

**STATE**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**OPTIONALITY**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**DEPENDENCY**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**CONSTRAINT**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**RISK**
- NOT APPLICABLE — no statement of this kind was derived for this capability.

**UNKNOWN**
- [N-U41-116] No retention or anonymisation of conversations, visitor country, language or anonymous identities was found; only empty conversations are removed automatically; any retention rule is an operational policy to be decided outside the source.

