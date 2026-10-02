# U43 — mail family, maintenance, Microsoft (neutral knowledge)

Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

Source: Odoo 19 Community

Unit U43, date 2026-10-02.

## Capability 1 — OdooBot onboarding and bot replies

### WHAT

- A built-in assistant greets new internal users in chat and walks them through a short scripted tour. [N-U43-001]
### WHY

- It lowers the learning curve for first-time users without involving an administrator. [N-U43-002]
### BUSINESS RULE

- The assistant ignores its own messages and anything that is not an ordinary comment. [N-U43-003]
- Each step of the tour expects a specific input such as an emoji, a help word, a ping or an attachment before moving on. [N-U43-004]
- A user can restart the tour at any time by typing a trigger phrase. [N-U43-005]
### STATE

- The tour moves forward one step at a time and ends in an idle state. [N-U43-006]
### OPTIONALITY

- The assistant and its tour can be removed by uninstalling the feature; a companion piece only adjusts the user form when the human-resources feature is also present. [N-U43-007]
### DEPENDENCY

- It depends on the chat feature and on user records to remember progress. [N-U43-008]
### CONSTRAINT

- Progress is stored per user and the stored value is not editable by hand in the interface. [N-U43-009]
### RISK

- The assistant posts replies with elevated rights, so its replies appear even if the user could not post them. [N-U43-010]
- Progress updates are written under the user's own rights, so a low-privilege user might not keep progress. [N-U43-011]
### UNKNOWN

- It is not confirmed whether progress persists for every kind of internal user; this needs a runtime check. [N-U43-012]

## Capability 2 — Mailing group lifecycle and moderation

### WHAT

- A mailing group lets an organization run list-style email distribution with optional moderation of incoming posts. [N-U43-013]
### WHY

- It allows controlled broadcast and discussion by email while protecting members from unwanted messages. [N-U43-014]
### BUSINESS RULE

- In a moderated group every incoming post waits for a moderator decision unless a standing allow or ban rule already decides it. [N-U43-015]
- Moderated groups must have moderators with email addresses, and notification text is required where notification is enabled. [N-U43-016]
- Closed groups refuse new incoming mail and members-only groups refuse non-members. [N-U43-017]
### STATE

- A post is received, then held or accepted, then delivered to members in batches; rejected posts are never delivered. [N-U43-018]
### OPTIONALITY

- Moderation, notification of senders and guidelines are options per group. [N-U43-019]
### DEPENDENCY

- It depends on the outgoing mail queue, the incoming alias mechanism and a daily reminder job for moderators. [N-U43-020]
### CONSTRAINT

- Delivery batch size is a system setting and the sender is excluded from their own post. [N-U43-021]
### RISK

- Some quick moderation shortcuts do not run the same eligibility check as the normal accept and reject actions. [N-U43-022]
- Outgoing list mail carries unsubscribe headers; if mail clients mishandle them members may be unable to leave easily. [N-U43-023]
### UNKNOWN

- Behaviour of real mail delivery and bounce handling is not confirmed by source reading. [N-U43-024]

## Capability 3 — Mailing group membership, tokens and portal

### WHAT

- People can join and leave a mailing group through links in email and through a public group page. [N-U43-025]
### WHY

- It gives members do-it-yourself control over subscriptions without staff involvement. [N-U43-026]
### BUSINESS RULE

- A signed-in person joins immediately while an anonymous person must confirm through an emailed link. [N-U43-027]
- One-click unsubscribe is accepted from mail clients without a session using a signed token. [N-U43-028]
- Links are signed with secrets scoped to the specific purpose, so a token for one purpose does not serve another. [N-U43-029]
### STATE

- A subscription is pending until confirmed, then active until the member leaves. [N-U43-030]
### OPTIONALITY

- Public subscription and one-click unsubscribe can be offered or withdrawn by group settings. [N-U43-031]
### DEPENDENCY

- It depends on the portal feature and on the outgoing mail queue for confirmation messages. [N-U43-032]
### CONSTRAINT

- Confirmation links must match the stored signature to be accepted. [N-U43-033]
### RISK

- Some token comparisons are not constant-time, which is a minor timing-leak risk. [N-U43-034]
- One-click unsubscribe deliberately skips request-forgery protection, so the signature is the only safeguard. [N-U43-035]
### UNKNOWN

- Whether the confirm and unsubscribe pages behave correctly end to end is not confirmed. [N-U43-036]

## Capability 4 — Mail plugin authentication, enrichment and logging

### WHAT

- An email add-in can sign in to the system, look up or create contacts, enrich company data and log emails against records. [N-U43-037]
### WHY

- It lets users work from their mail client while keeping customer records current. [N-U43-038]
### BUSINESS RULE

- Sign-in issues a short-lived signed code that must be exchanged within three minutes for a long-lived access key. [N-U43-039]
- The access key has an expiry set by a system setting, defaulting to thirty days. [N-U43-040]
- Logging an email is limited to a fixed list of record types, and creating contacts needs create rights. [N-U43-041]
### STATE

- A code is issued, exchanged for a key, then the key expires. [N-U43-042]
### OPTIONALITY

- Company enrichment is optional and consumes credits of an external paid service. [N-U43-043]
### DEPENDENCY

- It depends on the contacts feature and on an external enrichment service. [N-U43-044]
### CONSTRAINT

- Codes are verified with a signature and expire; keys carry a dedicated scope for the add-in. [N-U43-045]
### RISK

- Company domain names are sent to an external service, so data leaves the system during enrichment. [N-U43-046]
- The email body is stored as formatted text supplied by the add-in, which trusts the add-in content. [N-U43-047]
### UNKNOWN

- How the sign-in redirect target is validated was not observed and needs a runtime check. [N-U43-048]

## Capability 5 — Maintenance request workflow

### WHAT

- A maintenance request records a repair or preventive task through stages from new to repaired or scrapped. [N-U43-049]
### WHY

- It gives maintenance teams a trackable queue with owners, dates and history. [N-U43-050]
### BUSINESS RULE

- A request that moves into a finished stage records a close date and completes its scheduled activity. [N-U43-051]
- Changing stage resets the progress indicator to normal. [N-U43-052]
- A recurring request spawns a fresh copy when it is finished, as long as the repeat window allows. [N-U43-053]
### STATE

- New, in progress, repaired and scrapped are the shipped stages; two of them count as finished. [N-U43-054]
### OPTIONALITY

- Recurrence and the extra stage set are optional configuration. [N-U43-055]
### DEPENDENCY

- It depends on the messaging and activity features for followers and reminders. [N-U43-056]
### CONSTRAINT

- Date and repeat settings are validated when saved. [N-U43-057]
### RISK

- A recurring request set to repeat until a date but missing that date may fail when finished. [N-U43-058]
- Recurring copies multiply records, so open workload can grow unnoticed. [N-U43-059]
### UNKNOWN

- Behaviour under real use was not run and is unconfirmed. [N-U43-060]

## Capability 6 — Equipment, categories, teams and alias intake

### WHAT

- Equipment is registered with a category and maintenance team, and reliability figures are derived from past requests. [N-U43-061]
### WHY

- It lets the business see which assets fail and who is responsible. [N-U43-062]
### BUSINESS RULE

- Serial numbers must be unique and an owner is automatically added as a follower. [N-U43-063]
- A category that is in use cannot be deleted. [N-U43-064]
- A team that belongs to a different company than the equipment is cleared. [N-U43-065]
### STATE

- An asset is active until archived. [N-U43-066]
### OPTIONALITY

- Teams may expose an email address so requests can be created by mail. [N-U43-067]
### DEPENDENCY

- It depends on the incoming mail mechanism for requests created by email. [N-U43-068]
### CONSTRAINT

- Mean time between failures and mean time to repair are computed from request history. [N-U43-069]
### RISK

- Anyone who knows the team address can create requests when the contact policy allows everyone. [N-U43-070]
- Incoming mail is copied into requests, including sender and cc addresses. [N-U43-071]
### UNKNOWN

- Calculated reliability figures were not verified with data. [N-U43-072]

## Capability 7 — Maintenance security and multi-company

### WHAT

- Maintenance access is controlled by a manager role and by record-level rules. [N-U43-073]
### WHY

- It limits maintenance data to people involved while letting managers see everything. [N-U43-074]
### BUSINESS RULE

- Ordinary users see requests they own, follow or are assigned to. [N-U43-075]
- Equipment visibility for ordinary users depends on following the asset. [N-U43-076]
- Records of other companies are hidden except where no company is set. [N-U43-077]
### STATE

- NOT APPLICABLE — no workflow states; access rules are static. [N-U43-078]
### OPTIONALITY

- The manager role is optional and implies ordinary internal access. [N-U43-079]
### DEPENDENCY

- It depends on the base user and company model. [N-U43-080]
### CONSTRAINT

- Access rights are listed per record type and rules narrow them further. [N-U43-081]
### RISK

- Managers bypass record rules by an always-true condition. [N-U43-082]
- Group membership grows by implication, which can widen access unintentionally. [N-U43-083]
### UNKNOWN

- Rule results per real user were not exercised. [N-U43-084]

## Capability 8 — Microsoft account OAuth and token lifecycle

### WHAT

- The Microsoft account feature handles sign-in consent and stores tokens used by other Microsoft features. [N-U43-085]
### WHY

- It lets features call Microsoft services on behalf of a user. [N-U43-086]
### BUSINESS RULE

- Requests to Microsoft use a short timeout and may only target the expected token and service hosts. [N-U43-087]
- The client secret is held as a system setting and used only when exchanging or refreshing tokens. [N-U43-088]
- Endpoints can be changed by settings for testing or special clouds. [N-U43-089]
### STATE

- A user is unlinked, authorized by consent, and refreshed until the refresh fails. [N-U43-090]
### OPTIONALITY

- The endpoints are optional settings with sensible defaults. [N-U43-091]
### DEPENDENCY

- It depends on user records and system settings. [N-U43-092]
### CONSTRAINT

- Token fields are restricted to administrators. [N-U43-093]
### RISK

- The sign-in state value is not signed, so its return address could be tampered with. [N-U43-094]
- Detailed request logs may expose tokens or secrets if debug logging is enabled. [N-U43-095]
### UNKNOWN

- Whether a non-administrator can complete consent was not confirmed. [N-U43-096]

## Capability 9 — Outlook calendar synchronization

### WHAT

- Calendar events are synchronized in both directions between the system and Microsoft Outlook calendars. [N-U43-097]
### WHY

- It keeps meetings consistent so users see the same events in both places. [N-U43-098]
### BUSINESS RULE

- The most recently changed copy wins when both sides changed. [N-U43-099]
- Recurring events must be created in Outlook when synchronization is active. [N-U43-100]
- Attendees need email addresses, and the organizer must be an attendee with a synchronized calendar. [N-U43-101]
### STATE

- Synchronization is not configured, then active, and may be paused, stopped or require re-authorization. [N-U43-102]
### OPTIONALITY

- Administrators can pause synchronization, set the range and timeout, and reset a user account. [N-U43-103]
### DEPENDENCY

- It depends on the Microsoft account feature and the calendar feature. [N-U43-104]
### CONSTRAINT

- Recurrence is capped at seven hundred and twenty occurrences. [N-U43-105]
### RISK

- Event titles, bodies, locations and attendee names and emails leave the system to Microsoft. [N-U43-106]
- Unknown attendees from Outlook can create new contact records in the system. [N-U43-107]
### UNKNOWN

- Behaviour under throttling, token rotation and failure was not confirmed. [N-U43-108]

## Capability 10 — Outlook mail server OAuth (SMTP and IMAP)

### WHAT

- Outlook can be linked as the outgoing and incoming mail account using token-based sign-in. [N-U43-109]
### WHY

- It allows mail to be sent and fetched without storing a mailbox password. [N-U43-110]
### BUSINESS RULE

- Only administrators may link an account and the email must match for personal servers. [N-U43-111]
- Tokens refresh automatically when close to expiry. [N-U43-112]
- Sign-in can run directly with Microsoft or through a vendor-hosted broker. [N-U43-113]
### STATE

- An account is unlinked, linked after consent, refreshed, or failed with an error. [N-U43-114]
### OPTIONALITY

- Using the broker is optional when the company has its own application credentials. [N-U43-115]
### DEPENDENCY

- It depends on the mail feature and, in one place, on a Google mail feature that is not declared. [N-U43-116]
### CONSTRAINT

- Secure transport is required for both sending and fetching. [N-U43-117]
### RISK

- With the broker the refresh token is sent in a request address to the vendor service. [N-U43-118]
- The email in the sign-in token is read without verifying its signature. [N-U43-119]
### UNKNOWN

- Broker behaviour, failures and real mail flow were not confirmed. [N-U43-120]
