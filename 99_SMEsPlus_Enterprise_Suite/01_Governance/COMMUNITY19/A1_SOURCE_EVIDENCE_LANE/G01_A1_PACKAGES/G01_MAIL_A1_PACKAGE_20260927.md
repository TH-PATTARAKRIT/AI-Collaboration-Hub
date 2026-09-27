# G01 PLATFORM_BASE — RED TEAM A1 Package — `mail`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `mail` (display name "Discuss") |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_MAIL_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `8511f925843c54984cc4fb0edf589c8e3421640e38e996551d236b7958be22e6` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/mail/` |
| Question bank (lens only) | `GMVQ/G01_PLATFORM_BASE/G01_MAIL_GMVQ_MVQ_50_V1.00_DRAFT.md` (sha256 `0d6d7fcc…bf7d`, matches `FREEZE_W1-B01.json`) |
| Freeze | batch W1-B01, freeze hash `558ec88047aef5c8e7ea0e2675b1c43ef358ec29b172d6878068330f3fba7177`, ELIGIBLE |
| Lane B dependency | None. A1 does not wait for Lane B; no runtime evidence consumed |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Clean-room note: the claims are neutral WHAT / WHY / RISK statements. Identifiers are evidence pointers only. Nothing here recommends reusing vendor schema, ORM, workflow, UI or naming. No QIDs are answered. The bank was used only to pick topics: parent-record access inheritance, follower/recipient eligibility, internal-note leakage, inbound routing and spoofing, queue/retry context, cross-company boundaries, unsubscribe links, template authority, retention/GC and elevated-privilege paths.

Evidence key (blob SHA-1 from the Lane A packet; "SC" = re-fetched and hash-verified in this package, see section 10):
E1 `__manifest__.py` 2f88958b; E2 `__init__.py` 3fd366ff; E7 `security/ir.model.access.csv` 29275551 (SC); E8 `security/mail_security.xml` 0219605e (SC); E9 `data/mail_groups.xml` 4b4125ed; E10 `data/ir_cron_data.xml` d72aacbe; E11 `data/ir_config_parameter_data.xml` 1f556c60 (SC); E12 `models/mail_message.py` 4a70962d (SC); E14 `models/mail_thread.py` c1f8a83b (SC); E15 `models/mail_followers.py` 915ebee7 (SC); E16 `models/mail_activity.py` 66d9cd79 (SC); E17 `models/mail_activity_type.py` 35594d2d; E19 `models/mail_template.py` f95b8f53; E20 `models/mail_render_mixin.py` 25ef82e3; E21 `models/mail_mail.py` 44c9e2d2 (SC); E22 `models/mail_alias.py` 3d5c8fb2; E23 `models/mail_alias_domain.py` f3f7fdae; E25 `models/mail_tracking_value.py` cc29178f (SC); E26 `models/mail_notification.py` f16b7b45; E27 `models/fetchmail.py` 352a2b4f; E28 `models/mail_blacklist.py` 3be3953d; E31 `models/mail_gateway_allowed.py` 17a6aa94; E32 `models/mail_scheduled_message.py` 9ddc7a4c; E34 `models/ir_attachment.py` 56f7c354; E36 `models/ir_mail_server.py` 52fa3b5b; E37 `models/res_users.py` 56c27c11; E40 `models/models.py` 1edb1f78; E41 `models/discuss/discuss_channel.py` 57e38f34; E42 `models/discuss/discuss_channel_member.py` 504f70b8; E43 `models/discuss/mail_guest.py` 9c7c2192; E44 `controllers/thread.py` 57ab2401 (SC); E45 `controllers/attachment.py` 70db479c; E46 `controllers/mail.py` fd62e06f (SC); E53 `controllers/google_translate.py` f2606b9b; E57 `controllers/discuss/public_page.py` d68ff9ff (SC); E62 `controllers/discuss/gif.py` f5eba191.

## 1. Claims

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-MAIL-C01 | WHAT: The module bundles three capabilities: internal/guest chat (text, voice, video), an outbound/inbound email gateway, and conversations attached to business documents with followers, subtypes and activities. It declares dependencies on base, base_setup, bus, web_tour and html_editor. RISK: one module is a shared communication layer for every business domain. | E1 | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C02 | WHAT: Reusable behaviours (conversation thread, activities, alias delegation, blacklist-aware thread, rendering) are inherited by other business modules, and the partner entity gains messaging and activity behaviour here. RISK: an access flaw in this layer spreads to every module that inherits it. | E14, E40; packet items 4, 47 | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C03 | WHAT: A message links to any business record through a generic (model name, record id) pair. It stores a record-company reference, an "employee only" flag, a subtype, and one of several message-type classes. WHY: one message store serves all documents. RISK: access depends on how the linked record is resolved at runtime, not on a typed reference. | E12 (SC) | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C04 | WHAT: The access-control list grants read on messages to public users and full create/read/update/delete to portal and internal users. Custom access logic then narrows this, beyond the list and the record rules. WHY: messages inherit visibility from their parent document. RISK: the security boundary lives in code, not in declarative rules. | E7 (SC), E12 (SC) | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C05 | WHAT: The custom message check denies non-internal users any message that is flagged employee-only, has no subtype, or has an internal subtype. Other operations depend on the actor's relation to the message (author, recipient, notified, follower) or on access to the linked document. Deleting a message requires write access to the document. | E12 `_check_access` / `_get_forbidden_access` (SC) | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C06 | WHAT: A per-model "post access" setting controls posting. The default requires write access on the document, and the channel entity relaxes it to read. WHY: lets readers comment where the model allows it. RISK: relaxing it per model widens who can post. | E40, E14, E41 | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C07 | WHAT: Only system administrators have access-list rights on outgoing mail, tracking values, incoming servers, the gateway allowlist, the blacklist, reactions, presence, push and push devices, and message translation. Internal users get read-only access to followers and aliases. RISK: ordinary user flows that create or read these entities must run with elevated privilege in code, so authorization depends on the checks made before that elevation. | E7 (SC) | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C08 | WHAT: The public posting endpoint resolves the target thread with a post-access check and then posts with elevated privilege. Posters without write access are not auto-subscribed. The content-update endpoint allows edits by the author, the guest author or an admin, again with elevated privilege after the check. | E44 (SC) | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C09 | WHAT: The thread-access helper only logs a warning when it receives access parameters that are not on the allowlist; it does not reject them. It then checks access with the allowed-company context emptied. RISK: whether an empty company context narrows or widens the check is decided in the base layer and is not shown in this module. | E14 `_get_thread_with_access` (SC) | HIGH (behaviour in source) / LOW (effect) | SOURCE-STATIC |
| A1-G01-MAIL-C10 | WHAT: The file of 26 record rules contains no company-scoped rule for any mail entity. Company separation for messages depends on access to the parent record plus some company checks in code (aliases, catchall routing, partner lookup). | E8 (SC); E22, E14 | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C11 | WHAT: When a notification status update is pushed to the client, the message is included only if the parent record passes a read check. A source comment says the allowed-company check "if necessary" is still unresolved. The inbox push path builds each user's payload with the company context emptied. RISK: status updates or previews could cross company boundaries. | E12 ~L1356-1370 (SC); E14 ~L3381 (SC) | HIGH (source) / LOW (runtime effect) | SOURCE-STATIC |
| A1-G01-MAIL-C12 | WHAT: Follower rules: following a record yourself requires read access to it. Subscribing someone else, or unsubscribing someone else, requires write access. Follower rows are unique per (document, partner). RISK: a follower gets notifications but no rights on the record, so eligibility at delivery time rests on notification logic. | E14 `message_subscribe` (SC); E15 (SC) | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C13 | WHAT: The unsubscribe link endpoint is public, has CSRF protection disabled (the in-code comment says mail clients call it with an unpredictable session), and unsubscribes the partner named in the request, with elevated privilege. A keyed signature over the path and all request parameters authorizes the call, so the partner id is bound by the token. RISK: whoever holds a link can replay it, and no expiry is visible in this module. | E46 `/mail/unfollow`, `_check_token` (SC) | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C14 | WHAT: The generic "view from email" redirect and the message redirect are public. The message redirect reads the message itself and then decides where to send the caller. A legacy parameter resolves a message id to its record with elevated privilege before redirecting. RISK: redirect behaviour could reveal whether a record or message exists. | E46 `/mail/view`, `/mail/message/<id>` (SC) | MED | SOURCE-STATIC |
| A1-G01-MAIL-C15 | WHAT: Public Discuss pages attach a guest identity to the request. The invitation route checks a channel secret in constant time. The group restriction on a channel (or its parent) overrides the token. A token-based route, enabled by a configuration parameter, can create a channel with elevated privilege and no group restriction when none exists for the token. RISK: anonymous callers can create channels whenever that parameter is on. | E57 (SC); E41, E43 | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C16 | WHAT: Activity access: read needs the record rule AND (being the assignee OR read access to the document). Write and delete are allowed when the record rule passes (creator or assignee) OR when the user has post/write access to the document. Free-floating activities are limited to the assignee. RISK: people other than the creator or assignee can change activities on any document they can post to. | E16 `_check_access` (SC); E8 (SC) | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C17 | WHAT: A value change is shown only to viewers who have read access to the tracked field, taking field groups into account. Tracking entries without a linked field are visible only to system administrators. | E25 (SC) | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C18 | WHAT: Users outside the template-editor group cannot save templates that contain unsafe dynamic expressions. Restricted rendering is seeded ON by a configuration parameter. Internal users can write only templates they own or are assigned; editors and admins can write all. RISK: the guard is only as strong as that parameter and the group assignments. | E20, E19, E11 (SC), E8 (SC) | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C19 | WHAT: A message's content can be edited only if it is a user comment with no tracking values. Other message kinds raise a user error. WHY: protects system and audit messages. RISK: authors can still edit comments after sending, and whether previous versions are kept is not shown in the packet. | E14 `_check_can_update_message_content` | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C20 | WHAT: Outgoing mail has five states: outgoing, sent, received, delivery failed and cancelled. It defaults to outgoing and cannot be copied. Retry puts a mail back to outgoing; cancel sets cancelled. Mails flagged for auto-delete are removed after processing. One message can produce several outgoing mails. | E21 (SC) | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C21 | WHAT: The mail queue runs as a scheduled job under the root user, in batches with a commit after each one. Send failures move the mail to failed with a failure type and propagate an exception status to the per-recipient notifications. RISK: the job's identity and company context differ from the original sender's. | E10; E21 (SC) | MED | SOURCE-STATIC |
| A1-G01-MAIL-C22 | WHAT: Per-recipient notification rows have a type (inbox or email) and a status (ready, processing, sent, delivered, bounced, exception, cancelled). A partial uniqueness applies to (message, partner), and checks require a partner for inbox notifications and a partner or email for email notifications. | E26 | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C23 | WHAT: The inbound pipeline runs in this order: parse, bounce detection, loop detection (with an allowlist bypass and configurable time window and threshold), route resolution (reply thread, alias, fallback), then route validation (the model accepts the message and the alias contact policy allows the sender: everyone, authenticated partners, or followers). Failures either drop the mail with a warning or send a bounce, and may mark the alias invalid. RISK: the sender is matched to a contact by email address. | E14 `message_route` family; E22, E31 | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C24 | WHAT: A recurring cleanup deletes overdue activities older than N years. The seed value of N is 3. A value of 0 or a missing value disables the cleanup with a warning, and negative values are ignored. RISK: open business tasks are silently deleted according to one global parameter. | E16 `_gc_delete_old_overdue_activities` (SC); E11 (SC) | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C25 | WHAT: Other scheduled jobs: notification cleanup (rows older than 180 days, monthly), incoming mail fetch (every 5 minutes, inactive by default), posting and notifying scheduled messages, web push, member unmute cleanup, and a weekly publisher update notification. | E10 | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C26 | WHAT: Aliases are unique per (local part, domain). Alias domains hold unique bounce and catchall local parts, a default sender, and linked companies. Alias constraints compare the alias domain with the record's company. A post-install hook moves legacy global alias parameters into the domain entity. | E22, E23, E2 | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C27 | WHAT: Channel record rules: private and group channels are visible only to members (or to members of the parent channel). Open channels are visible when there is no group restriction or the user is in the restricting group. A database check allows a group restriction only on the open channel type. Members are unique per partner or guest. | E8 (SC); E41, E42 | HIGH | SOURCE-STATIC |
| A1-G01-MAIL-C28 | WHAT: Attachments uploaded through Discuss or chatter prove ownership by write access or by an ownership token. The upload, delete and zip routes are public and accept a guest context. | E34, E45; packet item 35 | MED | SOURCE-STATIC |
| A1-G01-MAIL-C29 | WHAT: Message content can go to outside services: a translation API, a GIF provider, web push (VAPID keys) and personal SMTP servers, each configured by a system parameter or a user setting. RISK: message data leaves the system. | E53, E62, E36, E37; packet items 42-43 | MED | SOURCE-STATIC |
| A1-G01-MAIL-C30 | WHAT: Users choose between inbox and email notifications (enforced by a constraint), and a group implies the inbox preference. Personal outgoing servers are unique per owner and are cleaned up by a scheduled job. | E37, E36, E9 | HIGH | SOURCE-STATIC |

## 2. Business rules (derived, neutral)

- BR1: Access to a message follows access to its parent document. The exceptions are the message author, the message's recipients and notified users, and the private-message and follower creation paths (C04, C05).
- BR2: External (portal/public) actors never see internal-class messages, whatever their document rights (C05).
- BR3: Posting needs the model's declared post operation. Write is the default, and a model can lower it (C06).
- BR4: Managing someone else's follower subscription needs write access to the document; following it yourself needs read access (C12).
- BR5: Only comment-type messages without tracking values can have their content edited (C19).
- BR6: Tracking visibility follows field-level group access (C17).
- BR7: Unsafe dynamic template content needs template-editor membership while restricted rendering is on (C18).
- BR8: Inbound mail must pass bounce, loop and contact-policy gates before it creates or updates a record (C23).
- BR9: Overdue activities past the configured age are purged; the purge is off when the parameter is zero or missing (C24).
- BR10: An open channel's group restriction overrides an invitation token (C15, C27).

## 3. States and transitions

| Entity | States / transitions (source-visible) | Evidence |
|---|---|---|
| Message | Not a state machine. Classified by type (incoming email, comment, outgoing email, system notification, automated targeted notification, out-of-office, user-specific notification) and by internal/external visibility. Only comments without tracking values can have content edited | E12, E14 |
| Outgoing mail | outgoing -> sent / received / failed (exception) / cancelled; failed -> outgoing (retry); any -> cancelled (cancel); auto-delete removes the mail after processing | E21 (SC) |
| Notification | ready -> processing -> sent / delivered / bounced / exception / cancelled (the pending/processing values are documented as used by the SMS module); read flag and date kept separately | E26 |
| Activity | Computed from due date: planned / today / overdue, then done. Activity types can suggest or trigger the next activity. Overdue activities past the age threshold are deleted by the cleanup job | E16 (SC), E17 |
| Follower subscription | none -> subscribed (self: read; others: write) -> per-subtype preferences -> unsubscribed (self: internal users always may; others: write; email link: signed token) | E14 (SC), E15 (SC), E46 (SC) |
| Incoming server | not confirmed -> confirmed; fetch job inactive by default | E27, E10 |
| Alias | computed validity status; the inbound bounce path can mark it invalid | E22, E14 |

## 4. Exceptions / failure modes

- X1: Send failure: the mail moves to failed with a reason, and its notifications move to exception. Retry is manual or by resetting to outgoing (C20, C21).
- X2: Inbound loop, bounce or policy failure: the mail is dropped with a warning or answered with a bounce, and the alias may be marked invalid (C23).
- X3: A notification status push skips records deleted without cascade instead of failing (E12 ~L1366, SC).
- X4: Disallowed thread-access parameters produce only a log warning; the request continues to the access check (C09).
- X5: An invalid or missing unsubscribe token raises an access error (C13).
- X6: The activity cleanup skips itself with a warning when the parameter is zero, missing or negative (C24).
- X7: An edit to a non-comment message, or to one with tracking values, raises a user error (C19).

## 5. Cross-module handoffs

- H1: base supplies users, partners, companies, attachments, scheduled jobs, the outgoing server and the rendering engine. The meaning of an empty allowed-company context belongs to base (C09, C11).
- H2: bus carries inbox and notification-status pushes and presence (C11).
- H3: Every business module that inherits the thread, activity or alias behaviours takes on these access rules and its own post-access setting (C02, C06).
- H4: The SMS module uses the pending/processing notification statuses (C22).
- H5: The web manifest controller is extended although `web` is not a declared dependency (packet item 45, unverified).
- H6: auth_signup (configuration parameter read) and a publisher-warranty model (weekly job) are soft couplings (packet item 46).

## 6. Evidence gaps (carried forward from Lane A, plus A1 additions)

- G1: `mail_thread.py` (5141 lines) and `discuss_channel.py` were read only in parts, and the full rule inventory is still open. A1 read the subscribe, thread-access and inbox-push sections.
- G2: The wizards (composer, activity scheduling, follower editing, template reset/preview, blacklist removal) were not studied, so the rules for mass mail and composing are unverified.
- G3: The `tools/` guest-context decorator and Store were not studied. How guests are authorized on public routes (C15, C28) is unverified.
- G4: `models/update.py` (publisher warranty) was not studied. Data leaving the system through the weekly job is unverified.
- G5: Canned responses, ICE servers, presence, push, link preview, reactions, translation, roles, settings, RTC and call history, GIF favourites, plans and the tracking-duration behaviour were not studied.
- G6: Views, menus and data templates (layouts, subtype and activity-type seed data) were not studied.
- G7: `webmanifest.py` route inheritance is unverified.
- G8: The allowed-company comment in the source and the missing company record rules are source observations only, and runtime proof is required.
- G9 (A1): Whether the empty allowed-company context (C09, C11) narrows or widens checks is decided in base and was not traced here.
- G10 (A1): No expiry or rotation of the unsubscribe and redirect signatures is visible in the files studied (C13).
- G11 (A1): Lane A's route list omits the token-based channel creation routes (`/chat/<token>`, `/meet/<token>`) and the legacy image routes in `controllers/mail.py`. The full route inventory needs a PASS-2 sweep.

## 7. CRQ candidates (for A2 / Proof)

| CRQ | Question to resolve | Links |
|---|---|---|
| CRQ-MAIL-01 | In a multi-company setup, can a user receive a notification-status or inbox push, with its preview, for a record in a company not in their active or allowed set? | C11, G8, G9 |
| CRQ-MAIL-02 | Does checking thread access with an empty company context let a user post or attach to a record in an inactive allowed company, or in a company they cannot access? | C09, C08, G9 |
| CRQ-MAIL-03 | Can a user who is neither creator nor assignee edit or delete another user's activity through document post/write rights, and is that change recorded in the audit trail? | C16 |
| CRQ-MAIL-04 | Can an unsubscribe link be replayed after the partner's access or email changes, and does it ever reveal the name of a record the caller cannot read? | C13, G10 |
| CRQ-MAIL-05 | With the chat-from-token parameter on, can an anonymous caller create any number of channels and guest identities? | C15, G3 |
| CRQ-MAIL-06 | Do follower-driven notifications keep reaching a partner who has lost read access to the record? | C12, C22 |
| CRQ-MAIL-07 | Does the root-user queue job ever re-render content or recompute recipients under a broader context than the sender's? | C21, G2 |
| CRQ-MAIL-08 | Can an inbound sender whose address matches a follower or partner get past the alias contact policy by spoofing? | C23 |
| CRQ-MAIL-09 | Can a guest or portal user use public attachment routes to delete or zip attachments on threads they can only read? | C28, G3 |
| CRQ-MAIL-10 | Is the overdue-activity cleanup applied across all companies and tenants with no per-company override or audit record? | C24 |
| CRQ-MAIL-11 | Can non-editors get unsafe template expressions through a composer or wizard path while restricted rendering is on? | C18, G2 |
| CRQ-MAIL-12 | Does the public message redirect behave differently for existing and non-existing messages in a way that reveals they exist? | C14 |

## 8. Contradictions

| ID | Observation | Status |
|---|---|---|
| K1 | Lane A item 29 says the record rule "restricts write/unlink to creator or assignee". The access logic in the source grants write and delete when the rule passes OR the user has post/write rights on the document. The rule is therefore not a restriction on its own (C16). | CONFIRMED-FROM-SOURCE (E16, E8 spot-checked) |
| K2 | Lane A item 40 lists only the invitation and channel-id public pages. The source also has the token-based create-or-join routes `/chat/<token>` and `/meet/<token>`, gated by a parameter. This is an omission, not a conflict (C15, G11). | CONFIRMED-FROM-SOURCE (E57 spot-checked) |
| K3 | Lane A item 36 says "some notification/inbox paths" empty the company context. The source also shows the generic thread-access helper (used for posting and attachments) doing the same, so the scope is wider than stated (C09). | CONFIRMED-FROM-SOURCE (E14 spot-checked) |
| K4 | Lane A item 35 implies disallowed access parameters are rejected. The source only logs a warning and continues (C09). | CONFIRMED-FROM-SOURCE (E14 spot-checked) |

## 9. Topic lens trace (no QIDs answered)

The bank topics on parent-record inheritance, follower coupling, internal-note leakage, unsubscribe links, retry context, cross-company counts, template authority and retention were used only to prioritize C04-C18, C21, C24 and CRQ-01 to CRQ-12.

## 10. Spot-check log

The files were re-fetched from `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/mail/<path>` on 2026-09-27, and `git hash-object` was run on the fetched bytes. The copies are kept in the session scratchpad and are not committed.

| # | Path | HTTP | Recorded blob | Computed blob | Result | Claims checked |
|---|---|---|---|---|---|---|
| S1 | models/mail_message.py | 200 | 4a70962dbcad8cab3d6de3bf1b112e5e753a062b | 4a70962dbcad8cab3d6de3bf1b112e5e753a062b | MATCH | C03, C05, C11 (company comment at L1361 confirmed) |
| S2 | security/mail_security.xml | 200 | 0219605e445b1f0f545e78f15aa6bca9084a0b5b | 0219605e445b1f0f545e78f15aa6bca9084a0b5b | MATCH | C10 (26 rules; no "company" token), C16, C27 |
| S3 | security/ir.model.access.csv | 200 | 29275551e7ca156899fa03985765fb2828de0b06 | 29275551e7ca156899fa03985765fb2828de0b06 | MATCH | C04, C07 (admin-only rows confirmed) |
| S4 | controllers/mail.py | 200 | fd62e06fc4c68764d82d396a54bf26aca550eff3 | fd62e06fc4c68764d82d396a54bf26aca550eff3 | MATCH | C13 (public, CSRF off, signed token over params), C14 |
| S5 | controllers/thread.py | 200 | 57ab2401542aff66eb0cf4b4329bcf92cbda0912 | 57ab2401542aff66eb0cf4b4329bcf92cbda0912 | MATCH | C08 (public post/update, guest context) |
| S6 | controllers/discuss/public_page.py | 200 | d68ff9ffb817c07687eca96f7eba114676a44324 | d68ff9ffb817c07687eca96f7eba114676a44324 | MATCH | C15, K2 |
| S7 | models/mail_thread.py | 200 | c1f8a83bbd4d6667c1ee7cd38b78cef71ad8f374 | c1f8a83bbd4d6667c1ee7cd38b78cef71ad8f374 | MATCH | C09, C11 (L3381, L5138), C12 |
| S8 | models/mail_activity.py | 200 | 66d9cd7994a49fc01d62d4992b64501cc26bfc48 | 66d9cd7994a49fc01d62d4992b64501cc26bfc48 | MATCH | C16, C24, K1 |
| S9 | models/mail_mail.py | 200 | 44c9e2d2066e5d0d01908e95298f3c7662e34b80 | 44c9e2d2066e5d0d01908e95298f3c7662e34b80 | MATCH | C20 (5 states, retry/cancel, auto-delete) |
| S10 | models/mail_followers.py | 200 | 915ebee70c212830edd820b67c7153f57dee445a | 915ebee70c212830edd820b67c7153f57dee445a | MATCH | C12 (uniqueness) |
| S11 | data/ir_config_parameter_data.xml | 200 | 1f556c605ddc3dbd13dbf68554cabec78dc47906 | 1f556c605ddc3dbd13dbf68554cabec78dc47906 | MATCH | C18, C24 (seeds 3 and 1) |
| S12 | models/mail_tracking_value.py | 200 | cc29178f0c4d59a1d1059f2a5e1a1bc424f40995 | cc29178f0c4d59a1d1059f2a5e1a1bc424f40995 | MATCH | C17 |

Result: 12 of 12 hashes match and no hash mismatch was found. The content checks support every claim listed. Four packet-level corrections came out of these checks (K1 to K4).

## 11. Provenance

- Input: the Lane A packet only (sha256 above). No Lane B, Evidence Pool, runtime or prior A1 material was consumed.
- Spot-check source: GitHub raw content at the pinned anchor commit. Hashing used the local `git hash-object` on fetched bytes only; no repository git operations were run.
- Bank: read only as a topic lens. Its hash matches the W1-B01 freeze record, and it was not edited.
- Claims without the (SC) tag rely on the Lane A packet as recorded and were not re-verified by A1.

## 12. Limitations

- Everything here is SOURCE-STATIC. Finding code in the source does not show that it is reachable at runtime, what it does under a given configuration, or which override from another module or the Enterprise edition applies.
- Line references are approximate and valid only at the anchor commit.
- No Formal Coverage claim is made and no percentages are used. The GMVQ floors are research depth, not a denominator.
- Confidence ratings reflect source clarity only. Any claim that depends on base-layer semantics (C09, C11) or on unstudied helpers (C15, C28) is limited by G3 and G9.
- Clean room: no code is reproduced and nothing recommends reusing schema, ORM or workflow.
