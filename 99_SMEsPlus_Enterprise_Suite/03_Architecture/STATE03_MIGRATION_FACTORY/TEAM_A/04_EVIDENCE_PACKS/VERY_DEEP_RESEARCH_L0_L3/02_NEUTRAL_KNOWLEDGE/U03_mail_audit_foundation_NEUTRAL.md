# U03 Mail, Audit Log, Notification and Portal Foundation — NEUTRAL KNOWLEDGE

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Clean-room layer: plain business and process language only (platform: Odoo 19 Community, named once here).
> Each statement carries an identifier in square brackets that links it to restricted technical claims. No file, module, field or code names appear below.

## CAP-U03-01 Change tracking and the discussion log as an audit trail

### WHAT
- [N-U03-001] Business documents can carry a discussion log. Selected data fields of a document can be flagged for change tracking; when the value of a flagged field changes, the system writes a change entry (field, previous value, new value) into the document's log.
- [N-U03-002] Each log entry is a message that records its author (by default the contact record of the acting user, unless the process names another author) and a timestamp of when it was written.
- [N-U03-003] A creation line is written into the log when a document is created, unless the calling process suppresses it.

### WHY
- [N-U03-004] The log gives reviewers a who-changed-what-and-when trail on a document without a separate audit product. It is the generic basis on which document-specific audit practices (for example a backdating note on both a stock transfer and its journal entry) can be built; the generic layer alone does not prove backdating.

### BUSINESS RULE
- [N-U03-005] Change detection compares the value held before the first modification within a transaction with the value at the end of that transaction. Several edits of one field in one transaction collapse into one net change; an edit that returns the field to its original value, or a change from empty to empty, produces no entry.
- [N-U03-006] Values supplied when a document is created are not recorded as change entries; only the creation line (and an optional template-driven message) results.
- [N-U03-007] Previous and new values are stored by data type. Choice fields keep the displayed label rather than the internal key; single-link relational fields keep the linked record's reference and display name at the time of change; multi-link relational fields keep only a comma-separated list of display names; date fields keep date-only precision.
- [N-U03-008] Change entries are written at the end of the transaction with elevated rights, so users who may edit a field but not post messages still produce an entry. The recorded author remains the acting user unless the process names another author.
- [N-U03-009] A change entry is shown to a viewer only if the viewer may read the audited field. Entries whose field no longer exists are visible to system administrators only. Direct access to the change-entry store is limited to system administrators.
- [N-U03-010] By default a tracked change is logged as an internal note: it is invisible to portal and public users and triggers no notification. A document type may attach a notification category or an automatic template message to specific changes.
- [N-U03-011] A log message can be read by its author, its creator, a named or notified recipient, or any user who can read the underlying document. Portal and public users additionally see only messages that have a non-internal category.
- [N-U03-012] Posting on a document requires the document-level right named by the document type, which defaults to modify rights; a document type may lower it to read rights (journal entries do).
- [N-U03-013] The user interface lets only the author or an administrator edit a message, only for plain comments, and never for messages that carry change entries. An edited message gets a visible edited marker and its previous text is overwritten.
- [N-U03-014] Deleting a document also deletes its whole discussion log, including change entries, followers, scheduled messages and open tasks.
- [N-U03-015] Not captured by the log: initial values at creation, fields that are not flagged, changes made while tracking is disabled, writes made directly in the database outside the application layer, intermediate values inside one transaction, changes to follower lists, flips of a message's portal visibility, and the deletion of a message or of the whole document.

### STATE
- [N-U03-016] Life of a change entry: a tracked field is modified; a pre-change snapshot is held; at the end of the transaction values are compared; an entry is written as an internal note (or as a notified message if the document type defines a category for it); it then stays attached to the document until the message or the document is deleted.

### OPTIONALITY
- [N-U03-017] Tracking is skipped when a calling process disables it for creation or modification, and is switched off while duplicating a document. Stored computed fields are tracked only when they are recomputed through the normal application layer. Which fields are tracked is decided per document type by the module that defines that type; the generic layer ships none.
- [N-U03-018] Document types choose their own posting right, notification categories, automatic template messages and the list of tracked fields.

### DEPENDENCY
- [N-U03-019] Concrete audited fields come from other areas: a journal entry's accounting date and status are tracked, and a stock transfer's scheduled date, status, responsible user and operation type are tracked, whereas the actual processing date of a transfer carries no tracking flag.

### CONSTRAINT
- [N-U03-020] Message content is not write-protected at the data layer: a user who authored a message or may modify the document can change its text, timestamp or visibility, and users who may modify a document can delete its messages. Only the link from a message to its document is limited to administrators.
- [N-U03-021] Exporting messages is limited to administrators.

### RISK
- [N-U03-022] Because deleting a document deletes its log and because messages are editable at the data layer, the log alone is not a tamper-evident audit record. A defensible audit trail needs an additional control such as restricted roles, no deletion of posted documents, and external log retention.
- [N-U03-023] Only the first value held in a transaction is kept, so intermediate values inside a multi-step process are not evidenced.
- [N-U03-024] Staff who may modify a message can flip its portal visibility after the fact, and no entry records that flip.

### UNKNOWN
- [N-U03-025] Whether tracking flags present on journal-entry line fields have any effect, because line records are not discussion-enabled in the observed configuration. A runtime test is needed.
- [N-U03-026] Whether other installed modules block message edits or deletions at the data layer is not determined by this unit.
- [N-U03-027] End-to-end confirmation of a who-and-when record for a backdated transfer needs execution plus the inventory and accounting units; this unit documents only the generic mechanism.

## CAP-U03-02 Followers, subscriptions and notification routing

### WHAT
- [N-U03-028] A follower list per document decides who is notified about new messages; each follower holds the set of message categories they want to receive.
- [N-U03-029] Every new message produces delivery records per recipient: internal users with the in-application preference receive an inbox item, all other recipients receive an email.

### WHY
- [N-U03-030] Followers and categories let people stay informed about documents they care about without receiving every internal note, and keep external contacts away from staff-only content.

### BUSINESS RULE
- [N-U03-031] The creating user, if active and internal, is automatically made a follower of a new document unless the calling process suppresses it.
- [N-U03-032] When a tracked user-type responsible field is set, that user is subscribed and notified of the assignment unless they are the acting user; a document type may declare further automatic subscriptions.
- [N-U03-033] Following a parent record (for example a project) can propagate to child documents through category relationships; internal-only categories are removed for external contacts.
- [N-U03-034] An internal author who posts a discussion-type message is subscribed so replies reach them; system notices and automatic messages do not subscribe the author.
- [N-U03-035] A user may follow a document with read rights; adding someone else requires modify rights and inactive contacts are filtered out. Internal users may unfollow themselves without rights; removing others requires modify rights.
- [N-U03-036] New followers receive the default categories of the document type; external contacts receive only the non-internal ones.
- [N-U03-037] A recipient linked to an internal user is notified according to that user's preference (inbox or email). External contacts, contacts without a user, and portal users are always notified by email. The in-application preference is allowed only for internal users.
- [N-U03-038] Only active user accounts count when deciding the preference, and when a contact has several users the internal one is chosen first.
- [N-U03-039] Authors are not notified of their own messages unless asked (except when explicitly mentioned); archived contacts are never notified; an address already emailed by an incoming message is not emailed again.
- [N-U03-040] Messages in internal-only categories never reach external contacts even when those contacts follow the document.
- [N-U03-041] Notification emails are sent directly right after the transaction commits when fewer than a configured number are pending (default one hundred); larger batches go to the outgoing queue.
- [N-U03-042] A delivery record per recipient keeps a status (ready, sent, bounced, exception, cancelled). Read inbox items of internal users are purged after about six months by a scheduled job.
- [N-U03-043] Notification emails contain an unfollow link only for internal contacts or where the document type allows external unfollowing.

### STATE
- [N-U03-044] Delivery record status flow: ready, then sent or exception; set to bounced when a bounce email arrives; inbox items are created directly as sent; cancelled when a notification is cancelled.

### OPTIONALITY
- [N-U03-045] Calling processes can suppress follower subscription, author subscription and assignment notices; a document type can turn on automatic following of its customer; the direct-send limit, batch size and preference are configurable.

### DEPENDENCY
- [N-U03-046] Each application seeds its own notification categories and declares which fields trigger assignment subscription; in the observed configuration the core module seeds three categories and applications add many more.

### CONSTRAINT
- [N-U03-047] A contact can follow a given document only once. Follower and delivery records carry no creator or modification stamps, and ordinary users hold read-only rights on the follower table.
- [N-U03-048] Being a follower lets a user create a message on that document at the data layer even without modify rights.

### RISK
- [N-U03-049] Follower changes leave no who-and-when trail, so a subscription added or removed cannot later be attributed to a user.
- [N-U03-050] A read-only follower right on the table does not stop followers from posting messages on the document, which widens write-like behaviour beyond role design.

### UNKNOWN
- [N-U03-051] Runtime behaviour when a contact has several users, missing email, or mixed preferences was not executed.

## CAP-U03-03 Dated tasks as lightweight follow-up and approval hand-off

### WHAT
- [N-U03-052] Activities are dated to-do tasks attached to a document (or personal), with a type, summary, note, due date and assignee. Completing a task posts a log message and archives the task; tasks are lightweight follow-up and are not an enforced approval workflow.

### WHY
- [N-U03-053] They let business documents hand work to people (call, upload, approve, review) and keep a visible record of when it was done and by whom, without hard-coding a workflow.

### BUSINESS RULE
- [N-U03-054] Creating a task for someone else notifies the assignee and subscribes them to the document; changing the assignee does the same for the new assignee.
- [N-U03-055] Completing a task posts a message of the task's type on the document (with optional feedback and attachments, authored by the completing user), moves task attachments to that message, archives the task with a completion date and, for chained types, schedules the next task. An assignee may complete a task without having access to the document.
- [N-U03-056] Cancelling (deleting) a task posts no message, so a removed approval task leaves no trace.
- [N-U03-057] A task's state derives from its due date relative to today in the assignee's time zone: overdue, today or planned; archived tasks are done.
- [N-U03-058] Tasks created by business code are flagged as automated and can be found, rescheduled, completed or removed by code through their type; tasks created by people are not automated. A calling process can suppress automation entirely.
- [N-U03-059] A type defines default summary, delay (days, weeks or months, counted from today or from the previous task), icon, category (none, upload document, phone call), default assignee, email templates and chaining (suggest or trigger the next type); it can be limited to one document type. The generic call, meeting and to-do types cannot be deleted, the five generic types (those three plus upload and exception) cannot be retargeted to a specific document type, the to-do type cannot be archived, and deleting any other type moves its tasks to to-do.
- [N-U03-060] A plan bundles several task templates for a document type, each with a delay before or after a plan date and an assignee mode (fixed user or asked at launch). Launching a plan creates the tasks and posts a message listing them. A plan is offered only if it has no company or matches the document's company.
- [N-U03-061] Reading a task requires being its assignee or being able to read the document; changing or deleting requires being its creator or assignee, or being able to modify the document; creating requires the right to post on the document.
- [N-U03-062] A daily housekeeping run deletes open overdue tasks older than a configured number of years (three in this configuration). Archived (completed) tasks are not selected.
- [N-U03-063] Other areas use tasks as follow-up and approval hand-offs: a purchase date change creates a warning task for the buyer, a sale creates an upsell reminder, an expense submission creates an approval task for the manager, and leave requests create first and second approval tasks that are completed or removed when the request moves on. None of these tasks blocks the document.

### STATE
- [N-U03-064] Task life: scheduled and open; overdue, today or planned by deadline; completed (archived with a message) or deleted; a completed task of a chained type spawns the next one.

### OPTIONALITY
- [N-U03-065] Task support is optional per document type; plans, chaining, default assignees and templates are optional configuration. Six generic types are seeded in this configuration, one of them (exception) archived.

### DEPENDENCY
- [N-U03-066] Other applications seed their own task types (maintenance, fleet, expenses, time off, certification) and plans extend this model.

### CONSTRAINT
- [N-U03-067] A task linked to a document needs a valid document reference; a task without a document must have an assignee. The completion date is recorded when the task is archived.

### RISK
- [N-U03-068] Anyone who can modify a document can complete or delete another person's open task, and deletion leaves no trace, so tasks are follow-up aids and not a segregation-of-duties control.
- [N-U03-069] Completion posts the message under the completing user, but an automated completion by the system on a state change also posts as the acting user, so completion does not prove the assignee acted.

### UNKNOWN
- [N-U03-070] Runtime behaviour of chained types, plan launch and the assignee-without-access path was not executed.

## CAP-U03-04 Message templates and the outgoing email queue

### WHAT
- [N-U03-071] A mail template defines subject, body, sender, recipients, attachments, report attachments, preferred outgoing server, schedule and auto-delete for one document type; rendering fills it per record and sending places entries in an outgoing queue.
- [N-U03-072] The outgoing queue holds one entry per email with a state (waiting, sent, received, failed, cancelled), failure type, failure reason and optional scheduled time; a scheduled job sends waiting entries.

### WHY
- [N-U03-073] Templates standardise business correspondence; the queue decouples sending from the user's transaction, throttles volume and keeps failures visible for follow-up.

### BUSINESS RULE
- [N-U03-074] Templates containing dynamic expressions may be created or changed only by members of the template-editor group (system administrators always qualify); plain placeholders are open to all. This restriction is switched on in this configuration, and a template is test-rendered on one existing record when saved and refused if it fails.
- [N-U03-075] Every internal user can read all templates, but may modify or delete only those they created or own; template editors may modify all.
- [N-U03-076] Sending from a template requires read access to the target document, creates queue entries with elevated rights in batches (default fifty) and attaches rendered report files to the entry; entries wait for the queue unless immediate sending is requested.
- [N-U03-077] Templates and notification emails default to deleting the outgoing entry after successful sending; a mass mailing with auto-delete keeps the core message as a log, while a single comment keeps the message on the document.
- [N-U03-078] A scheduled job every hour processes waiting entries whose scheduled time has passed, up to a per-run maximum (default one thousand), grouped by sending server, sender and domain, committing after each entry.
- [N-U03-079] A failure records a type (unknown, spam, invalid address, missing address, invalid sender, missing sender, server connection) and a reason. An entry is marked failed before sending is attempted, so a crash cannot cause double sending; a connection failure marks the whole batch failed.
- [N-U03-080] Failed entries are not retried automatically; someone with queue access must requeue them by hand. Successfully sent entries marked for auto-delete are removed, and failed ones other than invalid or missing address are kept.
- [N-U03-081] An incoming bounce email marks the matching delivery record as bounced with the bounce text and raises a bounce counter on contact records that carry one; any later incoming email from that address resets the counter.
- [N-U03-082] Personal outgoing servers are throttled to a per-minute cap (default thirty), with excess entries re-scheduled minute by minute; personal servers can be disabled globally, and an entry cannot use another user's personal server.
- [N-U03-083] Large attachments owned by business records are replaced in the email by download links when the estimated message size exceeds the outgoing server limit.
- [N-U03-084] The mail module seeds eight scheduled jobs: email queue manager (hourly), publisher update notification (weekly), purge of read notifications older than six months (monthly), incoming-mail fetch (every five minutes, inactive unless a confirmed fetch server exists), posting of due scheduled messages (daily), notifying of scheduled messages (hourly), web push notification (daily), and unmuting of discussion channel members (daily).
- [N-U03-085] The weekly update-notification job sends the database identifier, user counts, names of installed applications, base address, version and the company's name, email and phone to an external publisher server, and posts any reply to the all-staff channel; deployments may want it disabled.

### STATE
- [N-U03-086] Queue entry flow: waiting, then sent or failed; failed returns to waiting only by manual requeue; waiting may be cancelled; successful entries marked auto-delete disappear.

### OPTIONALITY
- [N-U03-087] Batch sizes, direct-send limit, session size, personal-server limit and template restriction are configuration parameters; the fetch job switches itself on or off with the number of confirmed fetch servers; sending can be forced immediate or left to the queue.

### DEPENDENCY
- [N-U03-088] Sending needs an outgoing mail server and, for return addresses, an alias domain; neither is configured in the restored database, so sending behaviour could not be observed.

### CONSTRAINT
- [N-U03-089] Only system administrators have table-level access to the outgoing queue; ordinary users create entries only through business actions that use elevated rights.

### RISK
- [N-U03-090] Failed entries remain silently in the queue until someone looks; with no automatic retry, a transient outage can lose customer notifications unless monitored.
- [N-U03-091] Auto-delete removes the outgoing copy, so the system may retain only a message record and not the sent email itself; evidence of what was emailed depends on the message log.
- [N-U03-092] The weekly publisher update job sends environment and company details outside the organisation by default.

### UNKNOWN
- [N-U03-093] Real sending, failure classification against live servers and bounce handling need an outgoing server and runtime execution.

## CAP-U03-05 Incoming email, address aliases and the mail gateway

### WHAT
- [N-U03-094] An alias maps an email address to a document type (each incoming mail creates a new document) or to one fixed document (each incoming mail is appended), with default values, a sender policy and a status.

### WHY
- [N-U03-095] Aliases let customers and vendors start or continue business documents by email without logging in.

### BUSINESS RULE
- [N-U03-096] Incoming mail is routed in this order: bounces are handled and dropped; replies to an existing thread are attached to it; recipient addresses matching an alias are routed to it; a fallback document type is used if given; otherwise the mail is rejected. Direct writes to the catch-all address are bounced.
- [N-U03-097] The sender policy is everyone, only senders matching a known contact, or only followers of the target document; a violation bounces a notice to the sender, and a configuration error marks the alias invalid and bounces.
- [N-U03-098] Documents created by an alias are created with elevated rights on behalf of the internal user matching the sender if one exists, otherwise on behalf of the user account running the gateway; the incoming message itself is posted by the system user.
- [N-U03-099] Loop protection ignores mail from a sender who has created or replied more than a threshold (twenty) within a time window (two hours by default) and bounces a notice; a list of allowed senders is exempt.
- [N-U03-100] Alias names must be unique within a domain, plain ASCII, and different from the bounce and catch-all addresses; defaults must be a literal dictionary; an alias domain tied to a company must match the company of the owning or target document.
- [N-U03-101] Mail fetch servers (IMAP, POP or local) are polled every five minutes by a scheduled job that is enabled only when a confirmed remote server exists; messages are processed one by one with a commit each, at most fifty per run per server; after prolonged failure the server is returned to draft and administrators are notified.

### STATE
- [N-U03-102] Alias status flow: not tested, then valid after a successful creation from mail, or invalid after a configuration error; changing the policy, defaults or target resets it to not tested. Fetch server flow: draft, confirmed; prolonged failure returns it to draft.

### OPTIONALITY
- [N-U03-103] Local-part-only matching, the allowed catch-all domains, loop thresholds and the allow-list are optional configuration; keeping the original email and stripping attachments are per-server options.

### DEPENDENCY
- [N-U03-104] A document type must accept creation or update from incoming mail; aliases are normally created by the owning application (for example vendor bills, leads, tasks, expenses).

### CONSTRAINT
- [N-U03-105] Table-level rights on aliases are read-only for employees and full only for system administrators (alias domains for access-rights administrators); alias records created through a document's own fields are created with elevated rights.

### RISK
- [N-U03-106] The default sender policy is everyone, so anyone who knows an address can create documents; in the restored configuration eight aliases exist, all without a domain, and seven allow everyone.
- [N-U03-107] Incoming content is stored under an elevated user context and its text is not trusted; downstream document creation hooks must tolerate hostile content.

### UNKNOWN
- [N-U03-108] No alias domain, fetch server or outgoing server exists in the restored database; routing, bounce and loop behaviour were not executed.

## CAP-U03-06 Conversation and task capabilities inherited by business documents

### WHAT
- [N-U03-109] A document type that inherits the thread mixin gains a message list, a follower list, need-action and delivery-error counters, an attachment count, field tracking, posting and logging functions, notification functions, and hooks for creating or updating the document from incoming mail.
- [N-U03-110] A document type that also inherits the task mixin gains open tasks, the next deadline, the activity state and helper functions to schedule, reschedule, complete or remove automated tasks.

### WHY
- [N-U03-111] One shared mechanism gives every business document the same conversation, follow-up and audit behaviour, so policies can be reasoned about once.

### BUSINESS RULE
- [N-U03-112] A document's access rights govern its messages: reading the document allows reading its non-internal messages, the post right (modify by default) allows posting, and modify rights allow editing or deleting its messages.
- [N-U03-113] The follower list and the attachment count are visible only to internal users; messages of the notification type used for single-recipient notices are never part of the document's log.
- [N-U03-114] Posting is only possible on a saved business document; the default category is internal note, the real author is the acting user, and the document's company is recorded on the message.
- [N-U03-115] Replies without an explicit parent attach to the latest relevant message so the thread stays flat unless the document type opts for threaded replies.

### STATE
- [N-U03-116] A thread-enabled document carries unread and error counters derived from delivery records; messages move from posted to notified to read or failed according to recipients.

### OPTIONALITY
- [N-U03-117] Document types switch behaviour with type-level options (post right, customer auto-follow, flat threads) and per-call flags (no tracking, no creation log, no subscription, forced immediate sending).

### DEPENDENCY
- [N-U03-118] In the restored configuration 136 document types are thread-enabled, 57 are task-enabled and 15 carry the opt-out and bounce mixin.

### CONSTRAINT
- [N-U03-119] Deleting a thread-enabled record removes its messages, followers and scheduled messages; deleting any record removes its tasks.

### RISK
- [N-U03-120] Anything widened on a document is inherited by its log: widening read exposes its non-internal messages, and widening modify allows deleting or rewriting them.

### UNKNOWN
- [N-U03-121] Behaviour of every inheriting document type's overrides was not studied here; only the generic contract was traced.

## CAP-U03-07 Customer portal access, share links and invitation

### WHAT
- [N-U03-122] The customer portal lets external contacts see and act on documents through (1) a user account in the portal group, (2) a shareable link carrying a per-document secret, and (3) a per-recipient signed value that lets a recipient post as themselves.
- [N-U03-123] Granting access creates a portal user from a template user and emails an invitation; sharing a document posts an internal note naming the recipients and emails them the link.

### WHY
- [N-U03-124] Customers can read quotes, invoices or orders, communicate and, for signature or payment flows owned by the sales area, act without receiving internal rights.

### BUSINESS RULE
- [N-U03-125] A shareable document holds one random secret created on first use; anyone holding the link can view the document, bypassing normal rights. The secret has no expiry and persists until changed.
- [N-U03-126] A per-recipient signed value derived from a server secret, the database, the document secret and the contact lets that recipient post to the portal discussion; changing the document secret invalidates every signed value.
- [N-U03-127] Posting through the secret or signed value works without login; the author is set to the identified contact, and only that contact may edit their own message.
- [N-U03-128] The portal discussion shows only non-internal, non-empty messages of a limited set of message types; internal users see it as portal users do.
- [N-U03-129] Granting portal access requires a valid unique email, creates (or reactivates) a user in the company of the contact by copying the template user, adds the portal group and sends an invitation with a signup link; revoking archives the user and clears the pending signup; re-inviting is allowed only for existing portal users.
- [N-U03-130] Sharing by link posts an internal note for each recipient and sends the link; recipients without a user receive a signup link when free sign-up is enabled and the document type has no shareable secret.
- [N-U03-131] Portal users may edit their own contact and address data (name, phone, email, address, tax number for the commercial entity), archive other addresses but not their main one, change their password, and deactivate their account; customer API keys are allowed only by a setting that is not enabled here.
- [N-U03-132] Signup and password-reset links are signed, expire after one hundred and forty-four hours (invitation) or four hours (reset), and become invalid once the user logs in or the contact's user set changes. Free sign-up for uninvited visitors and password reset from the login page are both enabled in this configuration.
- [N-U03-133] Record-level portal rules are not defined by the portal module itself; each business document type declares its own. In the restored database twenty-seven modules (twenty-five excluding test modules) contribute eighty-three rules that mention the portal group, and the portal module itself contributes none.
- [N-U03-134] A daily job emails the inviting employees about invited internal users who have not logged in five days after creation.

### STATE
- [N-U03-135] Portal access flow: contact without user; invited (user created, signup pending); confirmed on first login; revoked (user archived, signup cleared); a revoked contact can be granted again.

### OPTIONALITY
- [N-U03-136] Free sign-up versus invitation-only, password reset, customer API keys, the template user and the signup validity periods are configuration; sharing is optional per document type.

### DEPENDENCY
- [N-U03-137] Signature and payment links reuse the document secret and access address; their business flows belong to the sales and payment areas and are not traced here.

### CONSTRAINT
- [N-U03-138] Contacts need a valid email not used by another user; the fields portal users may edit themselves are a fixed list; the invitation mechanism acts only on contacts and child contacts of the selected partner.

### RISK
- [N-U03-139] Secrets never expire and a forwarded link grants the same view to anyone, so a link is a bearer credential; revocation requires regenerating the secret.
- [N-U03-140] Free sign-up is enabled by default, so uninvited visitors can create accounts; this widens the public attack surface and should be a deliberate decision.

### UNKNOWN
- [N-U03-141] Signature and payment flows, portal rules of business modules and token behaviour at runtime were not executed.

## CAP-U03-08 Security and multi-company aspects of messaging data

### WHAT
- [N-U03-142] Security of the messaging models is split between table-level access rows, a small set of record rules, groups, and extensive code-level checks for messages and tasks.

### WHY
- [N-U03-143] Message and task visibility has to follow the business document rather than a flat list, so the protection lives mostly in code.

### BUSINESS RULE
- [N-U03-144] Employees may read, create, modify and delete messages at table level and the real limit is the document-based check; portal users may do the same under stricter checks; public users read only. The outgoing queue, change-entry store, fetch servers, blacklist and gateway allow-list are administrator-only.
- [N-U03-145] The messaging module declares twenty-six record rules; none is company-based. They govern channels, channel members, notifications, task and plan administration, template ownership, composer ownership, scheduled messages and canned responses. Messages themselves have no record rule.
- [N-U03-146] Three groups come from the module: template editor, canned-response administrator and the inbox-notification marker; the system administrator group implies the first two. No user holds the template-editor group directly in the restored database.
- [N-U03-147] Messages record the company of their document but nothing filters by it; templates, queue entries, tasks, followers, aliases and notifications have no company; task plans and digests carry a company that no rule enforces; alias domains are validated against the company of the owning document.
- [N-U03-148] Another application (recruitment) adds a rule that gives its user group unrestricted reading of messages; this is outside the messaging module and affects only that group.

### STATE
- Not applicable to this capability (no separate statement).

### OPTIONALITY
- [N-U03-149] The template-editor restriction can be switched on or off by a setting that adds or removes the group for all internal users.

### DEPENDENCY
- [N-U03-150] Document-level company rules in other areas indirectly scope messages and tasks, because their access follows the document.

### CONSTRAINT
- [N-U03-151] The restored database confirms sixty-nine access rows and twenty-six record rules from the messaging module, three access rows and no rules from the portal module, and four access rows and no rules from the digest module.

### RISK
- [N-U03-152] In a multi-company deployment templates, aliases, task plans and digests are shared across companies, and a template comment notes that recipient information can leak between companies when contacts are found or created by email.

### UNKNOWN
- [N-U03-153] The restored database has one company, so multi-company behaviour was not observable and needs a multi-company runtime test.

## CAP-U03-09 Periodic indicator digest emails

### WHAT
- [N-U03-154] A digest is a periodic email to internal subscribers showing key indicators for the last day, week and month compared with the previous period, plus an occasional tip.

### WHY
- [N-U03-155] It gives managers a regular business pulse without logging in.

### BUSINESS RULE
- [N-U03-156] A daily job sends every activated digest whose next mailing date has been reached, then moves the next date by the periodicity (daily, weekly, monthly, quarterly).
- [N-U03-157] Indicators are switched on per digest and computed per recipient with that recipient's rights; indicators a recipient cannot read are left out. The core indicators are connected users and messages sent; other applications add theirs.
- [N-U03-158] If none of the recipients has logged in during a window matching the periodicity, the digest is slowed to the next longer periodicity to avoid spam.
- [N-U03-159] New internal users are subscribed automatically to the default digest when that option is on; recipients can unsubscribe with a signed one-click link, and access-rights administrators manage digests.
- [N-U03-160] Each email carries one tip not yet shown to that recipient, restricted by authorised group; shown tips are recorded per recipient.

### STATE
- [N-U03-161] Digest flow: activated or deactivated; when sent the next mailing date advances and the periodicity may widen.

### OPTIONALITY
- [N-U03-162] Which indicators appear, the periodicity, recipients and activation are all configuration; the default digest and auto-subscription are settings.

### DEPENDENCY
- [N-U03-163] Indicators for sales, accounting, projects and others come from those applications; the restored database also carries indicator switches for live chat, recruitment and relationship management.

### CONSTRAINT
- [N-U03-164] Employees can read digests and tips; only access-rights administrators can change them; recipients must be internal users.

### RISK
- [N-U03-165] The messages-sent indicator counts messages of all companies, and a digest has a company but no rule restricts who reads or edits it.

### UNKNOWN
- [N-U03-166] The restored database has one activated daily digest with one recipient whose next mailing date is in the past with no recorded last run for the job; actual sending was not executed.
