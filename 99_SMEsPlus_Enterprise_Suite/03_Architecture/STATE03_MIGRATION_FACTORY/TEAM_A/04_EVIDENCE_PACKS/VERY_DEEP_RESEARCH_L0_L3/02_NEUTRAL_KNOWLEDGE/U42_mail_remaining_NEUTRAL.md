# U42 Messaging Remaining Features — NEUTRAL KNOWLEDGE

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Clean-room layer: plain business and process language only (platform: Odoo 19 Community, named once here).
> Each statement carries an identifier in square brackets that links it to restricted technical claims. No file, module, field or code names appear below.
> Scope: discussion spaces, guests and presence, message reactions and files, link previews, composition and bulk sending, template security, scheduled messages, outgoing channels and external data transfers, incoming mail gateway, opt-out list, activity plans and the messaging extensions of contacts and users. Statements describe the standard behaviour and are not legal conclusions.

## CAP-U42-01 Discussion channels, groups, chats and their members

### WHAT
- [N-U42-001] Staff can hold conversations in named discussion spaces that are separate from business documents. A space is a thread of messages; posting in a space needs only the right to read it.
- [N-U42-002] There are three kinds of space: a private chat between two persons, a group that is private to the persons invited, and an open channel that can be joined according to its configuration. The kind is fixed when the space is created.
- [N-U42-003] Participation is recorded as a membership linking one space to exactly one person, either a contact or an anonymous guest. A person can appear once per space, a membership cannot be moved to another space or person, and a contact that belongs to an anonymous public account cannot become a member.
- [N-U42-004] Any message can be turned into a sub-thread of a channel or group. The thread has the same kind as its parent, follows the parent's authorised group, and its members are always members of the parent as well; removing someone from a space removes them from its threads.
- [N-U42-005] A private chat is found or created for each pair of persons; a chat involving more than two persons is refused.
- [N-U42-006] On installation a space for all employees and a space restricted to administrators are created, and the persons of the matching groups are added automatically.

### WHY
- [N-U42-007] The spaces give staff a lightweight internal conversation tool, and give outside visitors a way to join a conversation by link without creating a user account or a business document. The point of studying them for a business system is the control of who can read, join, be added, or remain a member.

### BUSINESS RULE
- [N-U42-008] An open channel is visible to the group chosen when it is created. If none is chosen it defaults to all internal staff; clearing the group makes the channel visible to everyone, including anonymous visitors.
- [N-U42-009] A restriction by authorised group is possible only on open channels. Groups and private chats cannot carry one.
- [N-U42-010] A channel may name user groups whose members are added automatically, when the channel is created, when the list changes, and when a user is created or gains the group. Members may leave afterwards.
- [N-U42-011] Visibility follows membership for groups and chats, and the authorised group for open channels. System administrators can see and manage every space, including other people's private conversations. Anyone who can see an open channel can list its members, and a person can change or remove only their own membership.
- [N-U42-012] A person may add themselves only to an open channel they are authorised for. Staff may add others to open channels they are authorised for and to groups they belong to. A private chat can never gain members. Adding someone who is already a member has no effect.
- [N-U42-013] When people join or are invited into a group or chat, a visible notice is written into the conversation.
- [N-U42-014] Leaving removes the membership and, in groups and chats, writes a visible notice. A private chat can only be hidden, not left.
- [N-U42-015] Staff with access can invite outside people by email to a group or to an unrestricted channel. Addresses that already belong to a member are skipped, each invitation carries a signed token bound to the address, and the invitation is sent immediately; if sending fails the inviter sees an error.
- [N-U42-016] The invitation picker lists only active internal users who are not yet members and, for restricted channels, belong to the authorised group. For a typed outside address it offers an email invitation where allowed and shows whether an invitation to that address was already sent.
- [N-U42-017] Each space has a secret link. Anyone opening it, logged in or not, becomes a member without any approval.
- [N-U42-018] Members of a space are notified of new comments by browser push, not by email or inbox. The author, muted members, members marked do-not-disturb and inactive contacts are skipped. In open channels each member's own choice (all, mentions only, nothing) or their personal default decides; groups and chats notify every member who has not muted. People mentioned by name are reached through their normal notification preference.
- [N-U42-019] A mention in a space can name only people who may access it: for open channels the people of the authorised group, for groups and chats existing members. An everyone mention reaches all members.
- [N-U42-020] Spaces have members, not followers; posting never adds followers.
- [N-U42-021] Posting a comment records the time of last interest on the space and never subscribes the author.
- [N-U42-022] Only comments in a space can be edited.
- [N-U42-023] Renaming a space or changing its description is done with the caller's own rights, and a rename leaves a visible notice.
- [N-U42-024] Creating an open channel from the interface writes a creation notice, and the chosen authorised group is looked up with the creator's own rights.
- [N-U42-025] The person who creates a space is always its first member.
- [N-U42-026] The all-employees space cannot be deleted because other features depend on it.
- [N-U42-027] Read markers are kept per member and are shown to the other members only in groups and chats.
- [N-U42-028] The member list and the search of spaces are available to anyone who can read the space, including guests on open channels; private chats are left out of searches.
- [N-U42-029] From a notification link, staff are taken to the discussion application and outsiders to a public page.
- [N-U42-030] When a user is archived, deleted, or loses the group that grants access, the user's membership in group-restricted channels is removed so internal conversations no longer reach them. The messages they wrote remain.

### STATE
- [N-U42-031] Once a space exists its kind, parent and originating message can no longer be changed.
- [N-U42-032] A private chat holds at most two members, and a chat that already has members cannot be extended.

### OPTIONALITY
- [N-U42-033] A system setting, off by default, lets any secret token in a public address create an open channel with no group restriction on demand; with the setting off those addresses do not exist.
- [N-U42-034] Creation accepts only a fixed list of membership settings; any other command or setting is rejected.

### DEPENDENCY
- [N-U42-035] Visibility rules depend on a membership test computed for the current person (user or guest) at the moment of access.
- [N-U42-036] Setting the list of contact members creates the missing memberships and removes the ones no longer listed.
- [N-U42-037] Call infrastructure details of a channel are readable by administrators only.
- [N-U42-038] Creating a channel may create its first memberships without passing the join rules, but only through an internal marker that is removed afterwards.

### CONSTRAINT
- [N-U42-039] The invitation secret of a space is a ten-character random string, unique in the database, with no expiry or rotation in the behaviour read.

### RISK
- [N-U42-040] Because the rules limit rows and not fields, staff who can see a channel may also be able to change its settings, including its authorised group, directly in the data layer; whether the interface exposes this was not exercised.
- [N-U42-041] A group restriction on a channel overrides its link, but private groups cannot carry a restriction, so for them the link alone grants access to anyone who obtains it.
- [N-U42-042] A visitor who learns a space link can join it as a guest; the guest's name, country and time zone are recorded.

### UNKNOWN
- [N-U42-043] How spaces, messages and templates behave with two or more companies is not evidenced; the available database has one company.
- [N-U42-044] In the available database there are three spaces (an all-staff channel, an administrators channel, and one private chat), no guests, no call sessions and one presence record.

## CAP-U42-02 Guests, presence, real-time bus coupling, call infrastructure and retention of messaging data

### WHAT
- [N-U42-045] A guest is a lightweight anonymous participant with a name, country, language and time zone, and optionally an email address. Guests can be members of spaces and authors of messages without having a user account; the name must be between one and 512 characters, and a guest can rename only themselves while an administrator can rename any guest.
- [N-U42-046] Online status is kept in a separate record per user or guest: online while the client reports activity every minute, away after 30 minutes of inactivity, offline when the connection closes or after twelve hours without a signal. Users can set their own status (online, away, do not disturb, offline); do-not-disturb silences space notifications and call invitations. Watching another person's status needs either read access to that person or a scoped token.
- [N-U42-047] Every live connection is subscribed automatically to the live channels of all spaces the person belongs to, and a guest is recognised from a token carried in the subscription name. Short system messages such as help text are shown live only and are not stored.
- [N-U42-048] A visitor joining a space through its public page becomes a guest with a name, a country taken from the network address and the browser time zone, and a cookie that identifies the guest on later requests. A logged-in person who opens such a page is added as a normal member.
- [N-U42-049] Voice and video calls are signalled through the system: a participant can send signals and change media state only for their own session, calls are joined only after becoming a member, and invitations go to members who are neither busy nor already in a call, and to guests seen within twelve hours.

### WHY
- [N-U42-050] Guests and presence exist so that outside people can take part in a conversation with minimal friction, and so staff see who is reachable. The audit relevance is that anonymous personal data is created by unauthenticated visitors and that third parties receive call-related data.

### BUSINESS RULE
- [N-U42-051] A guest is recognised by a secret token stored in a cookie set for 365 days, hidden from page scripts and compared in constant time; an invalid or missing token means no guest. The token is visible to system administrators only. The cookie is not marked secure or restricted by origin in the behaviour read, and the identification step carries no separate request-forgery token.
- [N-U42-052] Contact data shown to non-staff viewers is limited to presence, name and whether the contact is external; email and phone are added only for staff viewers. Whether a contact is in a call is visible to administrators only. Staff can open a profile card for any user or contact within their allowed companies.
- [N-U42-053] From three simultaneous participants the system asks an external relay server for a call room using a short-lived signed token; if that request fails the call stays peer-to-peer and only a warning is logged. Participants receive a signed credential valid for eight hours.
- [N-U42-054] When a commercial relay provider is configured, every call join sends the provider account identifier and secret to the provider to obtain temporary relay servers; on failure the system falls back to locally configured servers.
- [N-U42-055] Each call leaves a history record with the space, start and end times and the announcing message; it is readable by anyone who can read the space and is deleted only with the space, because no cleanup job exists.
- [N-U42-056] Automatic deletion is limited: online records after twelve hours, call sessions after about seventy-five seconds of inactivity, stored message translations after two weeks, and inactive sub-thread memberships are only hidden after two days. Only the creator of a sub-thread can delete it, which removes its messages. Deleting a whole document type deletes all its messages, followers, activities and files directly in the data layer, and removing a tracked field first preserves the description of its history.

### STATE
- [N-U42-057] A call session is created on join, becomes inactive when it stops signalling, and is deleted automatically or by an administrator.

### OPTIONALITY
- [N-U42-058] Local relay servers for calls are optional; their username and credential are stored as plain text, are given to every participant who joins a call, and are manageable by administrators only.

### DEPENDENCY
- [N-U42-059] Live updates, presence and typing signals depend on the separate live-update component, which was not read here.

### CONSTRAINT
- [N-U42-060] Presence updates are written immediately and failures are ignored, because presence is not essential.

### RISK
- [N-U42-061] A per-participant volume preference for guests appears to point at the wrong kind of record, so guest volume settings may not work as intended; this was derived from the code and not exercised.
- [N-U42-062] Cancelling a call invitation appears to need only read access to the space, not membership, and acts on the listed members; this was derived from the code and not exercised.

### UNKNOWN
- [N-U42-063] No automatic removal of guest records, or of their messages and reactions, was found; how long anonymous visitor data stays is unknown.
- [N-U42-064] Real network behaviour of the relay servers, the commercial provider and the other external services cannot be observed here: nothing is configured in the available database.

## CAP-U42-03 Message reactions, favourites, attachments, link previews and posting access

### WHAT
- [N-U42-065] Anyone who may post on a thread can react to a message with an emoji; one reaction per person, message and emoji can exist and a second click removes it. The reaction author is always the acting person, and the emoji text itself is not checked against a list. Reactions are stored in a table that only administrators can read directly, while summaries are shown to everyone who can read the message.
- [N-U42-066] Each person can mark messages as favourites for themselves; the mark is private to that person and needs only read access to the message.
- [N-U42-067] Read state of notifications is kept per recipient: marking a message done, or marking everything read, affects only the acting person, and the inbox, history and favourites lists show only the person's own items.
- [N-U42-068] When a message contains web links, the server fetches each page (up to five per message, with a short time limit) and stores its title, description and image in a cache shared by all messages. Only the author or an administrator can trigger or hide a preview; hiding keeps the cached data.
- [N-U42-069] Files can be uploaded onto a thread by anyone with the right to post there. Before the message exists they are parked as pending and linked at posting. Ownership of a file is proved by write access or by a signed token, which bypasses normal access checks; a client can attach only files it owns, and file previews and thumbnails need read or write access or a token.
- [N-U42-070] A message whose text, attachments, subtype description and readable change entries are all empty is treated as removed, and removing a channel message's content also clears its reply link.
- [N-U42-071] Searching for people to mention uses the searcher's normal access to contacts, prefers internal users, and gives each result a scoped token that lets external users mention that contact.

### WHY
- [N-U42-072] These features make conversation on documents richer, but each one introduces a path by which data leaves or becomes reachable: link fetches go out from the server, token links reach files without a login, and posting parameters decide what kind of message is recorded.

### BUSINESS RULE
- [N-U42-073] Posting through the web routes forces ordinary comment type for external users and for users without the right to post; internal users with the right may choose the type and visibility. External users cannot choose the author or sender address. Mentioned people are kept only if the poster is staff who can read them or presents a mention token. The text is cleaned when stored, and a poster who cannot modify the document is not made a follower. Reading needs read access to the document, posting needs the document's posting right, editing and deleting need write access.
- [N-U42-074] Only four extra parameters (signature flag, message type, subject and subtype) are passed unchecked to the posting step from the web routes, so a user with the right to post can choose between a note and a comment.
- [N-U42-075] Editing a message needs the posting right plus being its author or an administrator.
- [N-U42-076] Searching a thread covers text, subject, subtype description, file names and readable change entries, and excludes personal notifications.
- [N-U42-077] Delivery-failure information is shown only to the author of the message and the current user, and only when they can read the document; orphaned failure records are deleted when found.
- [N-U42-078] Link previews are on unless a setting sets the per-domain limit to zero or less; by default more than 99 fetches to one domain within ten seconds are throttled.
- [N-U42-079] Pinning or unpinning a message does not change its modification date and leaves no record of who pinned except a visible notice in the space.

### STATE
- [N-U42-080] A file attached to a message is deleted with its owner's request; the deletion is announced live and updates the message's modification date.

### OPTIONALITY
- [N-U42-081] Message translation is offered only when a translation service key is configured.

### DEPENDENCY
- [N-U42-082] In the available database there are 357 messages, 355 of them automatic notifications, mostly about changes to server actions and scheduled jobs, and no reactions or link previews.

### CONSTRAINT
- [N-U42-083] A message keeps at most five link previews and ignores links back to the system itself.

### RISK
- [N-U42-084] The server fetches addresses supplied by message authors, following redirects, with a spoofed browser identity, and the code applies no filter on the target address; internal addresses could therefore be reached from the server unless the network blocks them.
- [N-U42-085] Pictures pasted into a message become stored files reachable by a link carrying a secret token; anyone holding the link, including recipients of an emailed copy, can open the file without logging in.
- [N-U42-086] The route that downloads several files as one archive is open to anonymous callers and does not check access itself; it appears to rely on the checks made when each file is read.
- [N-U42-087] Anyone who can read an open channel can list every file ever shared in it, not only the files of messages they were present for.

### UNKNOWN
- [N-U42-088] Whether the hosting network stops the server from fetching internal addresses is outside the behaviour read and unknown.

## CAP-U42-04 Mail composer and mass-send contract

### WHAT
- [N-U42-089] One composition screen serves both a single message on a record and a bulk send to many records. In bulk mode each recipient's subject and body are produced separately from a template; in single mode the user edits the finished text. Every internal user may use it; each user can read and change only the compositions they started.
- [N-U42-090] A bulk send creates the outgoing emails on the user's behalf with elevated rights, in batches of 50 by default; the design note says that anyone who can access the records may create many emails this way. No role beyond internal user is required by the composition screen itself.
- [N-U42-091] A template can publish a button on its target document type that opens the bulk composition with that template preselected.

### WHY
- [N-U42-092] The composition screen lets staff send many personalised emails from existing records without a separate marketing tool. For control purposes the question is which safeguards the base behaviour supplies and which depend on additional components.

### BUSINESS RULE
- [N-U42-093] Within a single bulk send, a recipient address that already received an identical subject and body (with the same number of attachments) is skipped as a duplicate; the check does not span separate sends.
- [N-U42-094] A single email is sent immediately; a bulk send to at most 100 recipients (by default) without a stored selection is also sent immediately, otherwise emails wait for the queue.
- [N-U42-095] A bulk send may target all records matching a stored search; the search runs with the user's own rights, is parsed without code execution, is validated against the document type, and has no size cap in the behaviour read.
- [N-U42-096] Bulk emails carry the record's technical headers, and a message identifier is created in advance and stored as a reference so replies can be traced even if the provider rewrites identifiers.
- [N-U42-097] The author of the message follows the sender address: with a template the author is looked up from the template's sender, otherwise it is the current user. A template cannot name an arbitrary author.
- [N-U42-098] Template attachments are copied for the composition so that sending does not change who owns the template's files.
- [N-U42-099] Pending composition attachments that were never used are deleted automatically after one day.

### STATE
- [N-U42-100] A bulk email is created as outgoing, or as cancelled when it falls under the exclusion list or the duplicate check, or as failed when the address is missing or invalid; a failed email is moved to cancelled instead when sending history is not being kept.

### OPTIONALITY
- [N-U42-101] The exclusion list is applied by default to bulk sends but is a plain option on the composition screen that any user can switch off; when off, blacklisted addresses are not checked at all.
- [N-U42-102] Batch size, the immediate-send limit, keeping the message copy after deletion, and scheduling are options; scheduling is allowed only for a single-record comment.

### DEPENDENCY
- [N-U42-103] In the base behaviour the opt-out list and the list of already served addresses are empty extension points; real opt-out handling exists only if an additional mailing component fills them.
- [N-U42-104] A composition can be saved as a personal template, as described in the template security section.

### CONSTRAINT
- [N-U42-105] A message can be scheduled only from a single-record comment composition and needs a scheduled date.

### RISK
- [N-U42-106] Because bulk emails are created with elevated rights and the exclusion option is user-editable, controls on who may send to whom depend on access to the records and on user discipline rather than on a dedicated sending role.

### UNKNOWN
- [N-U42-107] The behaviour of the optional mailing component that completes opt-out and tracking was not read.

## CAP-U42-05 Template rendering sandbox, who can edit templates, and signed action links

### WHAT
- [N-U42-108] Email templates and the composition screen can use placeholders and richer expressions in subject, body, sender, recipients and reply address. Three rendering styles exist: simple placeholders, a template language, and a template language based on stored views.
- [N-U42-109] Expressions can see the target record, the current user, the whole data environment and the request context, plus formatting helpers. A non-restricted expression can therefore read any data the rendering user can reach.
- [N-U42-110] A person who is not a template editor may use only seven plain field references (name, contact name, customer, customer name, responsible user, responsible name and the responsible's signature). Anything else counts as unsafe: with the restricted template language only output and attribute directives are allowed, and a template made only of safe references is rendered by simple substitution without evaluating code.
- [N-U42-111] In bulk or batch mode the subject, body, sender and reply address are produced separately for each record with the engine configured for the field, and comments are kept only in email mode so that conditional layout hints for some mail clients survive.
- [N-U42-112] A shipped template can be restored from its original source, blanking fields the source leaves out and reloading its translations for installed languages; the action is available to template editors.
- [N-U42-113] A preview shows every dynamic field rendered against a chosen record, with the previewer's own rights, and shows errors in the dialog.

### WHY
- [N-U42-114] Dynamic templates are powerful and are meant to be authored by trusted people. The design therefore checks authorship when a template is saved and trusts its content afterwards, which is the central security trade-off to understand.

### BUSINESS RULE
- [N-U42-115] Creating or changing a template, including a translation of it, with any unsafe expression is refused unless the user is a template editor or system process; the check is made after the change is written and the change is rolled back when it fails. Every save also test-renders the dynamic fields against the first record of the document type and blocks the save on failure.
- [N-U42-116] Rendering is restricted for non-trusted content such as an edited composition, unless the user is an administrator or template editor or an internal marker is present. Templates themselves are trusted at render time, so the restriction does not apply to them.
- [N-U42-117] A non-editor composing from a template is trusted only while the body is unchanged from the template, or the body cannot be edited and the template body is forced back; an edited body is rendered in restricted mode. In single-record mode the body is always editable because it has already been rendered once.
- [N-U42-118] Seeded groups are Template Editor, Canned Response Administrator and an inbox-notification group; the system administrator group includes the first two.
- [N-U42-119] Any user can create a template from a composition and become its owner; the template is created from the already rendered text and no template-editor check is made at that step.
- [N-U42-120] All employees can read every template; they can create templates, but change or delete only those they created or that are assigned to them, while template editors and administrators can change all of them.
- [N-U42-121] Sending from a template requires only read access to the target records; there is no separate right to send a given template.
- [N-U42-122] Email addresses in a template's recipient fields are turned into contacts, finding existing ones or creating new ones, so sending can create contact records.
- [N-U42-123] Templates are classed as shipped with description, shipped without description or archived (hidden), and user-created (custom).
- [N-U42-124] Links in emails (view, unfollow, assign) carry a signed token over the path and parameters; the unfollow link works without login and without a request-forgery token, so anyone holding it can unfollow that person from the record. The generic view link sends logged-in users with access to the record, others to the discussion application, and anonymous users to the login page. A legacy message parameter is resolved to its document with elevated rights before the access decision is made, and the tokens have no expiry in the behaviour read.
- [N-U42-125] When rendering fails the user sees an error that may include a snippet of the template source and the technical cause.

### STATE
- [N-U42-126] Turning the restriction setting on removes the template-editor role from every internal user except through administrator membership; turning it off grants it to all internal users.

### OPTIONALITY
- [N-U42-127] The restriction setting is a single switch; when it is off every employee becomes a template editor and can put arbitrary expressions in templates. The restored database has it on.
- [N-U42-128] The available database has the restriction on, no direct template editors, and 62 templates, all shipped with the product and none created by users.

### DEPENDENCY
- [N-U42-129] Emails produced from a template are created with elevated rights, so what is sent depends on the template content rather than on the sender's own rights.

### CONSTRAINT
- [N-U42-130] Templates cannot be defined on abstract document types, and the template's recipient list may name only existing contacts.

### RISK
- [N-U42-131] Because templates are trusted after saving, anyone who can edit a dynamic template (editors, administrators, or every employee while the restriction is off) can have expressions run with the rights of whichever user later sends it.
- [N-U42-132] A template's partner list can name any existing contact in the database, and existence is checked without access rules, so a template can address any contact.

### UNKNOWN
- [N-U42-133] The exact reach of the template language beyond this component, in the base template compiler, was not read.

## CAP-U42-06 Scheduled messages and delayed notifications

### WHAT
- [N-U42-134] A scheduled message holds everything needed to post a user's message later: text, subject, recipients, files, author, whether it is a note, stored sending settings and a copy of the sending context. It can only be attached to a thread-enabled record, its date must be in the future, and its target record cannot be changed afterwards.
- [N-U42-135] A separate delay mechanism stores only the moment at which an already posted message is to be notified. An hourly job, plus exact triggers, sends notifications that are due, skips records that no longer exist, ignores unreadable stored settings, and removes the delay record afterwards. Only system administrators can access these records directly.
- [N-U42-136] Scheduling is possible only for a single-record comment from the composition screen and requires a scheduled date; the post values are stored as text with a cleaned copy of the context.

### WHY
- [N-U42-137] Scheduled messages let staff prepare communication in advance, for instance a follow-up on a quotation. The audit question is whose authority is used when the message finally leaves.

### BUSINESS RULE
- [N-U42-138] Creating, changing or deleting a scheduled message requires the right to post on the target record. Manual immediate sending is allowed only to the creator or an administrator.
- [N-U42-139] When due, the message is posted as its creator after re-checking that the creator still has the right to post, with the stored author and only twelve whitelisted settings replayed. What counts is the creator's rights at sending time, not at scheduling time.
- [N-U42-140] A daily job, triggered at each scheduled moment, posts due messages in batches of fifty with immediate notification and re-triggers itself while more are due.

### STATE
- [N-U42-141] A scheduled message is pending until it is posted, then removed; a failed message in the job is also removed after the creator receives a notice quoting its text.

### OPTIONALITY
- [N-U42-142] Only messages of the types supported by the composition screen can be scheduled, and the delayed-notification mechanism is used only when a sender asks for a later notification date.

### DEPENDENCY
- [N-U42-143] The environment-cleaning script used when a database is copied for testing clears mail servers, incoming servers and push keys and devices, but does not clear scheduled messages or delayed notifications, so a test copy could still post or notify them if the jobs run.

### CONSTRAINT
- [N-U42-144] A failed scheduled message is never retried; its record is deleted in every case once the job has handled it.

### RISK
- [N-U42-145] Anyone with the right to post on a record can see other people's pending messages for that record, because only changing and creating are limited to the creator.

### UNKNOWN
- [N-U42-146] How exact-date triggers behave in the job framework, which belongs to the base platform, was not read.

## CAP-U42-07 Outgoing notification pipeline, web push, and what leaves the system

### WHAT
- [N-U42-147] When a message is posted the system notifies recipients in a fixed order: inbox, then email, then browser push; if a later date is requested it only stores a delay record. Email notifications contain the full message body wrapped in a layout, one outgoing email per recipient partner or address, created with elevated rights and sent immediately only when fewer than 100 emails are created, otherwise left for the queue; replies are traced through stored identifiers, and when a sent email that is not a mere notification is deleted, its parent message is deleted with it, whereas notification emails leave the message in place.
- [N-U42-148] Files that are links, or that would make an email too large, are replaced in the email by download links carrying a secret token, so anyone holding the emailed link can download the file without logging in.
- [N-U42-149] Browser push goes to all active recipients other than the author for comments, and only to inbox-preferring recipients for system notifications and incoming emails.
- [N-U42-150] A push message carries the author and record name as title, the plain-text message body or attachment names, tracking text, the author's picture path, and the document type and number. The body is cut to fit one 4096-byte encrypted record.
- [N-U42-151] The server calls a third-party GIF service for search, categories and favourites, sending the user's search text, language and country together with the service key and the database name; any logged-in user can trigger it.
- [N-U42-152] Translating a message sends its full text to a third-party translation service, with the service key in the web address; any logged-in user who can read the message can trigger it, and results are cached for two weeks.
- [N-U42-153] Every week the system sends the database identifier and name, creation date, version, language, base web address, numbers of active and external users, the list of installed applications, any subscription code, and the company's name, email and phone to the publisher's server. Errors are hidden in the job.

### WHY
- [N-U42-154] Listing every outbound path lets an operator decide which to disable and which to document in a privacy or data-transfer assessment. None of the facts here is a legal conclusion.

### BUSINESS RULE
- [N-U42-155] Call invitations are also sent as browser push messages, titled as an incoming call and naming the space, to the registered devices of the invited contacts.
- [N-U42-156] Fewer than five target devices are pushed immediately within the request; five or more are queued.
- [N-U42-157] A daily job sends up to fifty queued pushes with the stored keys, deletes the queue rows whether or not sending succeeded, removes devices reported gone, and re-triggers itself while rows remain.
- [N-U42-158] Each push is sent to the stored device address with a signed publisher credential valid twelve hours, a short time limit and a failure only logged as a warning.
- [N-U42-159] If no push key pair exists, the first request for the public key deletes all registered devices and generates a new pair stored as system settings.
- [N-U42-160] A device record holds its browser address, subscription keys and expiry for one contact; an address that already exists is re-assigned to the latest registrant.
- [N-U42-161] Messages returned by the publisher's server are posted as comments in the all-employees space, and subscription information can update stored expiry settings; this is inbound content controlled by an outside party.
- [N-U42-162] An unauthenticated image route accepts a font path parameter, resolved by the platform's file helper, and answers with cross-origin access allowed.

### STATE
- [N-U42-163] A push device is deleted when its address reports it is gone; push keys are regenerated only when absent.

### OPTIONALITY
- [N-U42-164] Service keys for relay, translation and GIF providers are stored as plain system settings readable by administrators and by anyone with database access.
- [N-U42-165] Browser push, translation, GIF and relay services work only when their keys or devices are configured; the publisher update works by default.

### DEPENDENCY
- [N-U42-166] In the available database nothing is configured for push, relay, translation, GIF, outgoing or incoming mail, and no email was ever queued.

### CONSTRAINT
- [N-U42-167] A device address is unique; a push payload must fit one encrypted record.

### RISK
- [N-U42-168] Only addresses ending in the reserved invalid domain are treated as unreachable; no list of allowed push service hosts is applied to a stored address, so the server posts to whatever address was registered.
- [N-U42-169] Registering a push device is a publicly callable method that acts with elevated rights and only requires the instance's public push key, which is not secret; a registrant could therefore store an arbitrary address; this was derived from the code and not exercised.

### UNKNOWN
- [N-U42-170] Actual delivery, certificate handling and the real address of the publisher service in this deployment cannot be observed from the source.

## CAP-U42-08 Mail gateway, fetchmail, bounce handling, loop protection and sender policies

### WHAT
- [N-U42-171] Incoming email is turned into business activity through one entry point: the message is parsed, ignored if its identifier was already processed (including by a parallel run) or if it answers one of the system's own rate-limit notices, routed to a document, checked against the sender loop limit, and then recorded as a message on a new or existing document.
- [N-U42-172] Routing first treats a message as a reply when its reference matches a stored message, unless it is addressed to an address of another document type, in which case it is a forward. New emails are matched to an address defined in the system by full address or by local part, with an optional restriction of accepted domains; if none matches the caller's fallback document type is used, otherwise an error is raised. Records created by mail are created with elevated rights and the message is posted as the system robot, so the sender's own permissions do not apply.
- [N-U42-173] Each company uses an address domain from which its bounce, catch-all and default sender addresses are built; these must be unique and must not clash with document addresses; the first domain created is attached to all companies and addresses, and system addresses are filtered out of recipient lists of incoming messages.
- [N-U42-174] Outgoing mail is grouped by mail server, address domain and sender, and the server is chosen from the sender address. Staff may have a personal outgoing server where the feature is enabled: it is limited to their own address, throttled per minute, cannot be forced on others, is deleted by cleanup when the owner stops using it, and cannot reuse an address that belongs to a company default sender.
- [N-U42-175] Models that keep carbon-copy addresses merge new Cc addresses from incoming mail with the old ones and offer them as suggested recipients.
- [N-U42-176] Incoming mail servers (mailbox protocols or a local pipe) are configured by system administrators with host, port, encryption flag and a plain password; up to 50 messages per server are processed per run, one transaction per message, and the job switches itself on or off with the servers.
- [N-U42-177] A shipped pipe script submits each mail to the system over a remote procedure call with a user number and password given on its command line, defaulting to plain http; errors exit silently so that returned bounces do not reveal the command.

### WHY
- [N-U42-178] The gateway lets customers and suppliers reply by email and lets new emails open business records. The control questions are who the system believes the sender is, what authority creates the record, and what happens to messages that cannot be processed.

### BUSINESS RULE
- [N-U42-179] An address can accept everyone, only senders matched to a known contact, or only followers of the target record; the sender is identified from the unauthenticated From header, matched to a contact by address, and an incoming message never creates a contact just to be its author.
- [N-U42-180] A detected bounce is never routed as a document message. It only raises the bounce counter on matching opt-out records, marks the original notification as bounced with the bounce text, and is logged. Emails sent only to the catch-all address, or to it together with unroutable addresses, are answered with an explanatory bounce and not stored.
- [N-U42-181] A contact whose bounce count has reached ten is removed from a discussion space before the usual bounce handling continues.
- [N-U42-182] Unless the sender is on the allow-list, the system drops an email and replies with a rate-limit notice when the same sender has created at least twenty records through addresses, or posted at least twenty emails on one record, within two hours (both numbers are settings). Replies to such notices are recognised by a tagged identifier and ignored.
- [N-U42-183] When a comment or incoming email notifies an internal user who is marked out of office, the system posts an automatic reply as that user with automatic-reply headers, at most once every four days per recipient, and the limit is recomputed from stored out-of-office messages.
- [N-U42-184] Reply-to addresses are chosen from the owning parent record's address, else the company catch-all, else a default, and a bare address is used when the formatted one would exceed 68 characters to protect signature checks; message identifiers encode the document so replies thread back.
- [N-U42-185] A user who may edit a document that owns an inbound address can change that address, its contact policy, defaults and bounce text without rights on the address table.

### STATE
- [N-U42-186] An incoming email ends as ignored, bounced, dropped by the loop limit, rejected by address policy, or accepted; accepted mail marks its address valid and a configuration failure marks it invalid.

### OPTIONALITY
- [N-U42-187] The incoming-server password is stored as plain text with no encryption or masking in the record, and only system administrators can read the records.

### DEPENDENCY
- [N-U42-188] Whether portal accounts can call the public methods that process incoming mail, through the generic call route, was not exercised.

### CONSTRAINT
- [N-U42-189] Address validation is strict only when an optional validation library is installed; otherwise a simple normalisation check is used.
- [N-U42-190] Addresses use unaccented letters only; defaults are a literal dictionary; the loop limit does not apply to allow-listed senders.

### RISK
- [N-U42-191] No check of sender authenticity (SPF, DKIM, authentication results) was found in the module, so address policies that rely on the sender's address trust whatever the mail server in front of the gateway lets through.
- [N-U42-192] Rejected mail is answered with a bounce that embeds original message data and goes to the return path or From header chosen by the sender, so the system can be used to send unwanted bounces to third parties.
- [N-U42-193] When a mailbox message fails processing it is still marked handled; with the mailbox protocol that deletes messages the message is removed from the mailbox and only a log entry remains, so a failed inbound mail can be lost.
- [N-U42-194] The method that processes incoming mail is publicly callable on the abstract thread model and has no role check in its body, so any account that can reach the remote call endpoint could inject a mail into routing; address policies still apply.

### UNKNOWN
- [N-U42-195] Extensions of these models by other installed components, such as mass mailing, livechat, calendar and customer-relationship modules, were not read, so effective behaviour may differ.

## CAP-U42-09 Blacklist, opt-out and sender policies

### WHAT
- [N-U42-196] A central list holds email addresses that must not receive bulk emails. Only system administrators can manage it. Each entry is unique, tracked in its own history (address and active state changes), and removal does not delete: it archives the entry with an optional written reason, and adding the address again re-activates the same entry. Deleting a portal account may also add the account's address, with a note naming who did it.
- [N-U42-197] Business records that carry an email can be marked as opt-out capable: they keep a normalised address, a flag showing whether the address is listed (visible to staff), and a counter of bounces. A bounce raises the counter; any later normal email from that address resets it. In the base behaviour nothing blacklists an address automatically after a number of bounces.

### WHY
- [N-U42-198] The list protects recipients who should not be mailed in bulk and protects the business from repeated sending to dead addresses. Whether this satisfies any consent or opt-out obligation is a separate legal question that is not decided here.

### BUSINESS RULE
- [N-U42-199] A bulk send checks the active list against the recipient address of each record and cancels listed ones, marking them as excluded and not writing them into the recipient's history.

### STATE
- [N-U42-200] An address is either listed or unlisted; listing is an active entry, unlisting an archived one, and relisting reactivates it.

### OPTIONALITY
- [N-U42-201] The bulk composition option that applies the list is user-editable and on by default.

### DEPENDENCY
- [N-U42-202] When the optional bulk-mailing component is installed, as in the available database, its opt-out and already-served lists fill those extension points for mailings; sends without a mailing still see empty lists, and a mailing whose target type defines no opt-out computation has no opt-out list.
- [N-U42-203] Real opt-out processing, such as unsubscribe links and recipient preferences, belongs to an optional mailing component whose hooks are empty in the base behaviour.

### CONSTRAINT
- [N-U42-204] An address must be valid to be listed; duplicate entries are merged.

### RISK
- [N-U42-205] Because the exclusion option can be switched off per send by any user, the list is a default safeguard and not an enforced barrier.

### UNKNOWN
- [N-U42-206] No statutory requirement on consent, opt-out or retention of email records is established by this unit; software behaviour does not prove a legal duty and the statutory register was not consulted.

## CAP-U42-10 Activity plans, contact and user extensions, server actions, scheduled jobs and settings

### WHAT
- [N-U42-207] An activity plan is a named list of follow-up steps for one document type, optionally limited to a company. Each step names an activity type, a delay before or after the plan date, and either a default person or an assignee chosen at launch. Launching a plan creates the activities on each selected record and writes a note on the record listing the steps, assignees and due dates. Plans can be changed only by administrators; all records must belong to one company; plans are filtered by company only inside the launch screen.
- [N-U42-208] An activity is a dated to-do on a record or personal. Assigning it to a user subscribes that user as a follower of the record and notifies them. Marking it done writes a message, optionally creates the next activity, and archives it as history; cancelling deletes it without any trace; activities left overdue for the configured number of years (three in the available database) are deleted automatically, while archived ones are not. Deleting any record deletes the activities attached to it, and master activity types cannot be deleted.
- [N-U42-209] Contacts become documents with a log, activities and opt-out information. Changes to name, email, phone, parent company, salesperson, tax identification number and address are tracked with who, when, old and new value. Merging contacts writes a note listing every merged contact. Matching of incoming addresses to contacts is by normalised email, oldest first, and unknown valid addresses create new contacts.
- [N-U42-210] Users can choose their own notification preference and vacation reply; they gain role tags that can be mentioned, and archiving a user permanently deletes the activities assigned to that user.  A systray summary shows the user's own activities, counting only records they can read.
- [N-U42-211] Automation actions are tracked documents: edits to their name, target model, value, update path, state and outgoing web address leave history. Mail adds four action types (create activity, send email or message, add followers, remove followers) that work only on thread-enabled records; emails from actions are always queued and not sent immediately.
- [N-U42-212] Scheduled jobs are tracked documents too: the running user, interval, unit and priority are tracked, and job failures such as mailbox deactivation are posted to the administrators space.
- [N-U42-213] Canned responses are shortcut texts shared by group; owners and Canned Response Administrators manage them.
- [N-U42-214] Bulk editing of followers uses the normal subscribe rules, requires the actor to have an email when adding, and may send a single invitation naming all documents.

### WHY
- [N-U42-215] These behaviours matter for governance because they define what is recorded when staff change role, when tax identification data changes, and when automation is edited, and what is silently deleted.

### BUSINESS RULE
- [N-U42-216] Granting or revoking portal access is logged as a note on the contact. Changing a user's login, password or email sends a security alert (for an email change, to the previous address) including the requester's network address, approximate location, browser and system; alert delivery failures are suppressed so they never block the change.
- [N-U42-217] Mail features can be switched on for custom models only and never switched off.
- [N-U42-218] Time spent in each stage of a record is computed from the stored change history and requires the stage field to be tracked; it reads history directly, so anyone who can read the duration can see aggregate stage timing.
- [N-U42-219] The robot partner authors system messages and does not email itself.

### STATE
- [N-U42-220] In the available database there are two plans (onboarding and offboarding) with six steps, 21 activity types and one shared canned response.

### OPTIONALITY
- [N-U42-221] In the available database the counts of access rows, record rules, jobs and groups equal those in the source; one menu entry is unaccounted for, and no automation rules exist.
- [N-U42-222] In the available database 569 fields are flagged for tracking, 136 document types are thread-enabled, 57 activity-enabled and 15 opt-out capable; the contact name field is tracked with a different order than the source states, probably through another component.

### DEPENDENCY
- [N-U42-223] Company scoping of plans, templates and messages depends on the document's own rules, because the messaging layer adds no company term of its own.

### CONSTRAINT
- [N-U42-224] A plan step must use an activity type that matches the plan's document type; an activity type either suggests or triggers its next step, not both.

### RISK
- [N-U42-225] Cancelling an activity and archiving a user delete follow-up records without a trace, which may matter where activities are used as evidence of tasks or approvals.

### UNKNOWN
- [N-U42-226] A chat-bot component installed in the available database also processes every message posted in a space; its behaviour was not read.
- [N-U42-227] Whether other installed components change the deletion and tracking behaviour described above was not read.

