# G01 PLATFORM_BASE — Lane A PASS-1 Source Evidence — module `mail`

| Field | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Governed group | G01 PLATFORM_BASE |
| Slot | T2 |
| Module (FREEZE_W1-STD roster) | `mail` |
| Source anchor | odoo/odoo branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, path `addons/mail/` |
| Retrieval | raw.githubusercontent.com at pinned commit; blob SHA-1 via `git hash-object` on fetched bytes |
| Date | 2026-09-27 |
| Scope | PASS-1 breadth: server-side Python models, security CSV/XML, crons, config params, controllers. JS/static, views, wizards, tests NOT studied. |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (breadth only; depth gaps listed in section 5) |

Clean-room note: all findings are neutral WHAT / WHY / RISK abstractions. No source code reproduced; identifiers appear only as evidence pointers. Source presence does not equal runtime reachability. No runtime proof, no Formal Coverage claim, no percentages. No GMVQ QID answered.

## 1. Evidence Pointer Table (62 blobs)

| Path | Git blob SHA-1 | Purpose |
|---|---|---|
| addons/mail/__manifest__.py | 2f88958b66791f6bfa3eb1b6f3861538edd10ff4 | Manifest: name Discuss, deps, data list, post_init_hook, LGPL-3 |
| addons/mail/__init__.py | 3fd366ff96e4ec945c716b9582e5c7d3ab870ff1 | Package init; post-init migrates ICP alias params to alias domain |
| addons/mail/models/__init__.py | 553bd76763256a3cdd19b1863da6d8983eef76f8 | Model import roster (mixins, mail, discuss, odoo overrides) |
| addons/mail/models/discuss/__init__.py | bcabd8eda0f1415d0c0f15ff543792f4be5bf554 | Discuss sub-package model roster |
| addons/mail/controllers/__init__.py | 528e42909456b47ca6a2da9daa464e246fae1bcb | Controller roster |
| addons/mail/controllers/discuss/__init__.py | 253cde0a7b5c1b1b07ac657a871d2fb14fa0ba13 | Discuss controller roster |
| addons/mail/security/ir.model.access.csv | 29275551e7ca156899fa03985765fb2828de0b06 | Model ACL (69 rows) |
| addons/mail/security/mail_security.xml | 0219605e445b1f0f545e78f15aa6bca9084a0b5b | Record rules (26 ir.rule records) |
| addons/mail/data/mail_groups.xml | 4b4125ed11ba10696bb321cf40f7573ec4387ec8 | Groups: template editor, canned response admin, inbox notification |
| addons/mail/data/ir_cron_data.xml | d72aacbe8f9e17e84d4dd62dfc3642a1ba4dc9fd | Scheduled jobs (8 crons) |
| addons/mail/data/ir_config_parameter_data.xml | 1f556c605ddc3dbd13dbf68554cabec78dc47906 | Seeded config params (activity GC years, restricted rendering) |
| addons/mail/models/mail_message.py | 4a70962dbcad8cab3d6de3bf1b112e5e753a062b | mail.message: types, internal flag, custom access check |
| addons/mail/models/discuss/mail_message.py | a3e72c0f94da11f0a93038552f2b43bbc044cbbe | mail.message discuss extension |
| addons/mail/models/mail_thread.py | c1f8a83bbd4d6667c1ee7cd38b78cef71ad8f374 | mail.thread mixin: gateway routing, post, notify, tracking, followers API |
| addons/mail/models/mail_followers.py | 915ebee70c212830edd820b67c7153f57dee445a | mail.followers: partner-document-subtype subscription |
| addons/mail/models/mail_activity.py | 66d9cd7994a49fc01d62d4992b64501cc26bfc48 | mail.activity: state, constraints, access, GC |
| addons/mail/models/mail_activity_type.py | 35594d2d9680e948af4767880f724c57e871fc30 | mail.activity.type: delay, chaining, category |
| addons/mail/models/mail_activity_mixin.py | b56d4d3de75f2f611eb8fb4407e815dccb9f014c | mail.activity.mixin: activity state on documents |
| addons/mail/models/mail_template.py | f95b8f53dd95166603eadd42013907b77a23870f | mail.template fields and write/create checks |
| addons/mail/models/mail_render_mixin.py | 25ef82e3615fec8f6c5bba7defe79d706368f8bc | Rendering engine, restricted/unsafe expression guard |
| addons/mail/models/mail_mail.py | 44c9e2d2066e5d0d01908e95298f3c7662e34b80 | mail.mail outgoing queue, states, send, retry |
| addons/mail/models/mail_alias.py | 3d5c8fb2b32e82bc9a20f6cde25f036675d02989 | mail.alias: contact policy, uniqueness, company checks |
| addons/mail/models/mail_alias_domain.py | f3f7fdae4c3134b0737368b140480d7e27546c42 | mail.alias.domain: bounce/catchall/default-from per company |
| addons/mail/models/mail_alias_mixin.py | 88cecd644378ce58ad57a5b2c199eeffa9eefc58 | Alias delegation mixin |
| addons/mail/models/mail_tracking_value.py | cc29178f0c4d59a1d1059f2a5e1a1bc424f40995 | Field-change tracking values; field-level visibility filter |
| addons/mail/models/mail_notification.py | f16b7b45618f3df9d97395e81d4df23dbb8cbc21 | Per-recipient notification status, uniqueness |
| addons/mail/models/fetchmail.py | 352a2b4f70ab83afb0f0feaecc149566957f4f3c | Incoming mail server (IMAP/POP/local) |
| addons/mail/models/mail_blacklist.py | 3be3953d22e5192279859b52d2f65ce78f34975c | Email blacklist, unique email |
| addons/mail/models/mail_thread_blacklist.py | 160ff244837c50441572d05028aa8a07f516dd57 | Blacklist-aware thread mixin |
| addons/mail/models/mail_message_subtype.py | 70399d6d8bd6bff5661f551f09b09df332cdfc7a | Subtypes incl. internal flag |
| addons/mail/models/mail_gateway_allowed.py | 17a6aa94cdfb17dd348a678d04bf1be8752d059b | Loop-detection allowlist |
| addons/mail/models/mail_scheduled_message.py | 9ddc7a4c5cae898dc634733981c00cba2b917c5c | User scheduled message (post later) |
| addons/mail/models/mail_message_schedule.py | cba5178ff99004345eb71f51c811529a23f8270f | Scheduled notification dispatch |
| addons/mail/models/ir_attachment.py | 56f7c3543f189d56bc42225fa7406980740d3751 | Attachment ownership/token, delete-and-notify |
| addons/mail/models/discuss/ir_attachment.py | 886ea7b01053f87b66e2511c03c627a910aecd14 | Attachment discuss extension |
| addons/mail/models/ir_mail_server.py | 52fa3b5b76fe9317aa2ffb193919fe33ee8875dd | Outgoing server extension: personal server owner uniqueness |
| addons/mail/models/res_users.py | 56c27c1113a2149e6d311f366b12cff6c8772e98 | User notification type, personal mail server GC, company filter |
| addons/mail/models/res_partner.py | 463b52d392251ab7e12bd78b6e491b069c43dec2 | Partner inherits activity + blacklist thread |
| addons/mail/models/res_company.py | e1a640e2781a02a5894e52340b6aca0a1d9ce5de | Company alias domain link |
| addons/mail/models/models.py | 1edb1f78d952f754d364ac7d6e7863f7ef58bbf5 | Base override: _mail_post_access semantics, company field hook |
| addons/mail/models/discuss/discuss_channel.py | 57e38f3446071bd42ef4b80583a4b16f31c97423 | discuss.channel: types, uuid, group restriction |
| addons/mail/models/discuss/discuss_channel_member.py | 504f70b880311220309d84ae78b4db0966e68a63 | Channel membership, partner/guest uniqueness, GC |
| addons/mail/models/discuss/mail_guest.py | 9c7c2192c6d5da4f8b334c967a094c381b6c2786 | Guest identity for public discuss |
| addons/mail/controllers/thread.py | 57ab2401542aff66eb0cf4b4329bcf92cbda0912 | Thread routes; thread-with-access resolution |
| addons/mail/controllers/attachment.py | 70db479c69e1ed277b56e2199b9c77d6ff63dc97 | Attachment upload/delete/zip routes |
| addons/mail/controllers/mail.py | fd62e06fc4c68764d82d396a54bf26aca550eff3 | Mail redirect/unfollow/message view routes |
| addons/mail/controllers/mailbox.py | 465f321b3cbff514bd31eca11765f8312748d195 | Inbox/history/starred routes |
| addons/mail/controllers/webclient.py | da5b8d5b7a7f6f98c1a18cb3a899edfd3050df42 | Client data/action routes |
| addons/mail/controllers/guest.py | 2513907f21e7c97051b9eacb535a7a2c57169df0 | Guest rename route |
| addons/mail/controllers/message_reaction.py | 3a56154660434804dd3dd4309312ecfdc4c66b71 | Reaction route |
| addons/mail/controllers/link_preview.py | 15ff3c9e77b96b0913ceb9f78b50106bb58b3689 | Link preview routes |
| addons/mail/controllers/im_status.py | 19cafc0298588f847021e4d44f653d6e0792e4cb | Manual presence route |
| addons/mail/controllers/google_translate.py | f2606b9bfd6c113e4bfeba7ea8510db82f2336c0 | Message translation route (external API) |
| addons/mail/controllers/websocket.py | e37a0f314f0eb47aa93ed214261b0952dfc7bf28 | Websocket/bus presence route |
| addons/mail/controllers/webmanifest.py | 6e0d72c811ee6dba349814aceaf08ac89a7aa319 | Extends web manifest controller |
| addons/mail/controllers/discuss/channel.py | 99a38151d219ed42fe631a4b1631554520929bb4 | Channel routes |
| addons/mail/controllers/discuss/public_page.py | d68ff9ffb817c07687eca96f7eba114676a44324 | Public channel/invitation pages |
| addons/mail/controllers/discuss/rtc.py | a959ac5dfd8cc6cd8faf5379585127826a02c69d | RTC call routes |
| addons/mail/controllers/discuss/search.py | f80b088b7755b1da59b49a189e21ce1d7c90f2b1 | Discuss search route |
| addons/mail/controllers/discuss/settings.py | 193af07fe186a60c4845eca546624976cd2710bc | Mute/notification settings routes |
| addons/mail/controllers/discuss/gif.py | f5eba191836f3ebc7ffd8177e13c41e489d3f31b | GIF search/favorites (external API) |
| addons/mail/controllers/discuss/voice.py | d1effcfcc3871e5eda5e56577caac0e2d57f5685 | Voice worklet route |

## 2. Findings by A1 completion-card section

### 2.1 Manifest / dependencies / purpose
1. Module's display name is "Discuss" (technical `mail`), category Productivity/Discuss, flagged as an application, LGPL-3. Purpose statement covers three capabilities: internal/guest chat (text/voice/video), outbound/inbound mail gateway, and document-attached conversation ("chatter") with followers, subtypes and activities; plus POP/IMAP inbound fetching. (`__manifest__.py`)
2. Declared dependencies: `base`, `base_setup`, `bus`, `web_tour`, `html_editor`. (`__manifest__.py`)
3. A post-install hook migrates legacy system-parameter alias settings into the per-domain alias record. WHY: alias configuration moved from global params to a domain entity; RISK: upgrade path depends on this one-time migration. (`__init__.py`)

### 2.2 Data — models, inheritance, key fields, identity/uniqueness
4. Core mixins other business modules inherit: a thread mixin (messaging/chatter), activity mixin, alias mixin (delegation to an alias record), blacklist-aware thread mixin, render mixin, tracking-duration and main-attachment mixins. (`models/__init__.py`, `models/mail_thread.py`, `models/mail_activity_mixin.py`, `models/mail_alias_mixin.py`, `models/mail_thread_blacklist.py`, `models/mail_render_mixin.py`)
5. Message entity: polymorphic link to any document via (model name, record id) with composite indexes on that pair; carries author, recipients, subtype, a per-message "employee only" flag, a stored company reference and alias-domain reference, and a message-type classification (incoming email, comment, outgoing email, system notification, automated targeted notification, out-of-office, user-specific notification). (`models/mail_message.py`)
6. Outgoing email entity delegates-inherits the message entity (one message may have many outgoing emails with different recipients). Lifecycle states: outgoing, sent, received, delivery failed, cancelled; plus a failure-type taxonomy and an auto-delete flag. Constraint couples message and mail server. (`models/mail_mail.py`)
7. Followers: unique on (document model, document id, partner); each follower carries a subtype subscription set. (`models/mail_followers.py`)
8. Notifications: per-recipient row with type (inbox/email), status (ready, processing, sent, delivered, bounced, exception, cancelled), read flag/date, failure type/reason; partial unique index on (message, partner) where partner set; check constraints requiring partner for inbox type and partner-or-email for email type. (`models/mail_notification.py`)
9. Tracking values: typed old/new value columns (integer, float, char, text, datetime), linked field definition, JSON field info for non-field tracking, optional currency, parent message. (`models/mail_tracking_value.py`)
10. Activities: linked polymorphically to a document or free-floating; DB checks enforce "document model implies non-zero record id" and "no document implies assignee required". Computed state: overdue, today, planned, done. Activity types define delay unit/origin, chaining (suggest vs trigger next), category, restricted model. (`models/mail_activity.py`, `models/mail_activity_type.py`)
11. Alias: unique on (alias local-part, alias domain, null-coalesced); contact policy selection (everyone / authenticated partners / followers only); computed validity status; custom bounce content. Alias domain: bounce and catchall local-parts with uniqueness constraints, default-from, linked companies. (`models/mail_alias.py`, `models/mail_alias_domain.py`)
12. Templates: render-model binding, dynamic address fields, HTML body, static attachments and report attachments, layout reference, mail server, scheduled date expression, auto-delete, owner user; category selection. (`models/mail_template.py`)
13. Discuss channel: types chat (unique 2-person private), group (private invited), channel (joinable); unique UUID; unique "created from message" link for sub-channels; DB check that group-restriction applies only to type channel. Members: partial unique on (channel, partner) and (channel, guest), check that one of partner/guest exists; index on seen-message. Guest is a separate non-user identity entity. (`models/discuss/discuss_channel.py`, `models/discuss/discuss_channel_member.py`, `models/discuss/mail_guest.py`)
14. Blacklist: unique normalized email; gateway allowlist entity exempting senders from loop detection. (`models/mail_blacklist.py`, `models/mail_gateway_allowed.py`)
15. Incoming server: states not-confirmed/confirmed, server types IMAP/POP/local, SSL flag, keep-attachments and keep-original flags, priority ordering, last-fetch date. (`models/fetchmail.py`)
16. Users extended with notification preference (inbox vs email, enforced by a constraint) and personal outgoing mail server with per-owner uniqueness on the mail-server extension. Partners inherit activity and blacklist-thread mixins (non-flat thread). (`models/res_users.py`, `models/ir_mail_server.py`, `models/res_partner.py`)

### 2.3 Business rules / states / lifecycle / exceptions
17. Posting access per document model is governed by a class-level "post access" operation (default: write; discuss channel: read); base override validates the value is a legal ORM operation. WHY: lets read-only viewers comment where allowed. RISK: per-model relaxation widens posting surface. (`models/models.py`, `models/mail_thread.py`, `models/discuss/discuss_channel.py`)
18. Message content may be edited only for user comments without tracking values; otherwise a user error is raised. (`models/mail_thread.py` `_check_can_update_message_content`)
19. Outgoing queue: failed mails can be retried (exception -> outgoing); cancel sets cancelled; send errors mark exception with a failure reason and propagate exception status to notifications; auto-delete mails are removed after successful processing. (`models/mail_mail.py`)
20. Inbound routing pipeline (source-visible): parse -> bounce detection (bounce alias addresses) -> loop detection (sender allowlist bypass; time window and threshold from config params; sender-domain and header checks) -> route resolution (reply thread, alias, fallback model) -> route validation (model exists, accepts creation/update, alias contact policy for followers/partners) -> create new record or update existing thread. Violations either warn/drop or send a bounce reply and may mark alias invalid. (`models/mail_thread.py` `message_route`, `_routing_check_route`, `_detect_loop_sender`, `_routing_handle_bounce`, `message_process`)
21. Field tracking: tracked field changes produce a log message with tracking values and optionally a subtype and template-triggered post. (`models/mail_thread.py` `_message_track*`, `_track_*`)
22. Notification fan-out: recipients computed from followers/subtypes and explicit partners, classified into groups, delivered by inbox, email, web push, plus out-of-office auto-reply handling. (`models/mail_thread.py` `_notify_thread*`, `_notify_get_recipients*`)
23. Activity garbage collection deletes overdue activities older than N years (seeded N=3; 0/missing disables; negative ignored; batch capped). RISK: silent data deletion governed by a param. (`models/mail_activity.py`, `data/ir_config_parameter_data.xml`)
24. Other autovacuum routines: unpin outdated sub-channels; purge personal mail servers. (`models/discuss/discuss_channel_member.py`, `models/res_users.py`)
25. Scheduled messages: a user can schedule a post for later; constraints on model and future date. (`models/mail_scheduled_message.py`)

### 2.4 Security
26. Groups defined: Mail Template Editor, Canned Response Administrator (under a privilege), "Receive notifications in Odoo" (inbox notification type); system administrators imply the first two. (`data/mail_groups.xml`)
27. ACL highlights: messages readable by public, full CRUD for portal and internal users (then narrowed by custom access logic); outgoing mail, tracking values, incoming servers, gateway allowlist, blacklist, reactions, presence, push, translation — system admin only (so user-facing flows necessarily operate with elevated privilege internally); followers read-only for internal users; aliases read-only for internal users, full for admin; alias domains full for ERP manager; templates full CRUD for internal users (narrowed by rules); channel members full CRUD for public/portal/internal (narrowed by rules). (`security/ir.model.access.csv`)
28. Message access logic (custom, beyond ACL/rules): non-internal users are denied internal messages (employee-only flag, missing subtype, or internal subtype). Read allowed if author/creator/recipient/notified or read access on the linked document; create allowed for private messages, followers, readers of parent, or holders of the document's post-access right; write for author/recipient or document write; unlink requires document write. (`models/mail_message.py` `_check_access`, `_get_forbidden_access`)
29. Activity access logic: read requires rule AND (assignee OR document read); create/write/unlink tied to document post-access/write. Record rule restricts write/unlink to creator or assignee. (`models/mail_activity.py`, `security/mail_security.xml`)
30. Follower subscription: subscribing self requires document read; subscribing others requires document write; unsubscribing others requires write; internal users may always unsubscribe themselves; partner list filtered to active partners with elevated privilege. (`models/mail_thread.py` `message_subscribe`, `message_unsubscribe`)
31. Tracking visibility: tracking values are shown only if the viewer has read access to the tracked field (field-group aware); tracking without a field is system-admin only. (`models/mail_tracking_value.py`)
32. Template injection guard: users outside the template-editor group cannot save templates containing unsafe dynamic expressions; restricted rendering mode seeded ON by config param. Record rules: internal users write only own/assigned templates; editors/admins all. (`models/mail_render_mixin.py`, `models/mail_template.py`, `data/ir_config_parameter_data.xml`, `security/mail_security.xml`)
33. Channel access rule: non-channel types visible only to members (or members of parent channel); type channel visible if no group restriction or user in the restricting group; admins bypass. Membership rules govern self-entries, reading members of accessible channels, joining group-restricted channels, and inviting. (`security/mail_security.xml`)
34. Notifications rule: users write own; portal reads own-as-recipient or as-author. Public/portal read only non-internal subtypes. Compose wizard, canned responses, scheduled messages, GIF favorites, volume settings restricted to owner/creator (with admin overrides). (`security/mail_security.xml`)
35. Attachments: ownership proven via write access or ownership tokens; controllers resolve the target thread with post/read access and accept guest context; thread-access helper accepts only whitelisted access params (token/hash-type portal params). (`models/ir_attachment.py`, `controllers/attachment.py`, `controllers/thread.py`, `models/mail_thread.py` `_get_thread_with_access`, `_get_allowed_access_params`)
36. Multi-company / tenant: messages store a record company; alias constraints validate alias domain vs record company; inbound catchall routing picks recipient company from domain companies; partner lookup from email prefers same-company or company-agnostic partners; some notification/inbox paths run with empty allowed-company context to bypass company filtering. No mail-specific company record rules found in `mail_security.xml`. A source comment flags an unresolved allowed-company check. RISK: cross-company visibility of message notifications. (`models/mail_message.py` ~L1361, `models/mail_alias.py`, `models/mail_thread.py`, `models/res_users.py`, `security/mail_security.xml`)

### 2.5 UI surfaces (controller route names only)
37. Thread/chatter: `/mail/thread/messages`, `/mail/thread/recipients[...]`, `/mail/partner/from_email`, `/mail/read_subscription_data`, `/mail/message/post` (public auth), `/mail/message/update_content` (public), `/mail/thread/subscribe|unsubscribe`. (`controllers/thread.py`)
38. Mailbox: `/mail/inbox|history|starred/messages`; client data `/mail/data`, `/mail/action`; redirects `/mail/view`, `/mail/unfollow` (public, CSRF disabled), `/mail/message/<id>`. (`controllers/mailbox.py`, `controllers/webclient.py`, `controllers/mail.py`)
39. Attachments `/mail/attachment/upload|delete|zip` (public); reactions, link preview, guest rename, manual presence, translation, bus presence. (`controllers/attachment.py`, `controllers/message_reaction.py`, `controllers/link_preview.py`, `controllers/guest.py`, `controllers/im_status.py`, `controllers/google_translate.py`, `controllers/websocket.py`)
40. Discuss: `/discuss/channel/*` (members, messages, pinned, mark_as_read, join, sub_channel create/fetch/delete, attachments, typing), public pages `/chat/<id>/<token>` and `/discuss/channel/<id>`, RTC `/mail/rtc/*`, `/discuss/search`, `/discuss/settings/*`, `/discuss/gif/*`, voice worklet. Most use public auth with guest context. (`controllers/discuss/*.py`)

### 2.6 Jobs / config / integrations
41. Crons: email queue manager (hourly, batch 1000, root user); notification GC older than 180 days (monthly); fetchmail service (5 min, inactive by default); post scheduled messages (daily); notify scheduled messages (hourly); web push delivery (daily); channel member unmute cleanup (daily); publisher update notification (weekly). (`data/ir_cron_data.xml`)
42. Config params read in code (names only): `mail.batch_size`, `mail.mail.queue.batch.size`, `mail.mail.force.send.limit`, `mail.session.batch.size`, `mail.gateway.loop.minutes`, `mail.gateway.loop.threshold`, `mail.bounce.alias`, `mail.catchall.alias`, `mail.catchall.domain`, `mail.catchall.domain.allowed`, `mail.default.from`, `mail.disable_personal_mail_servers`, `mail.server.personal.limit.minutes`, `mail.activity.gc.delete_overdue_years`, `mail.activity.systray.limit`, `mail.restrict.template.rendering`, `mail.chat_from_token`, `mail.web_push_vapid_public_key|private_key`, `mail.google_translate_api_key`, `discuss.klipy_api_key`, `web.base.url`, `database.secret`, `auth_signup.reset_password`. (grep over `models/`, `controllers/`)
43. External integrations visible: SMTP (outgoing, incl. personal servers), IMAP/POP (incoming), web push (VAPID), Google Translate API, GIF provider API (Klipy), WebRTC/ICE servers and SFU asset bundle. (`models/fetchmail.py`, `models/mail_mail.py`, `controllers/google_translate.py`, `controllers/discuss/gif.py`, `__manifest__.py`)

## 3. Cross-module edges
44. Depends on `base` (users, partners, companies, attachments, crons, mail servers, qweb), `base_setup` (settings), `bus` (bus listener mixin, websocket presence), `web_tour`, `html_editor`.
45. Extends `web` webmanifest controller (`controllers/webmanifest.py`) though `web` is not a direct declared dependency (transitive via deps — not verified).
46. Reads an `auth_signup` config param and defines a cron on a publisher-warranty model — soft coupling; ownership of that model inside `mail` not verified (see gap G4).
47. Provides mixins consumed by nearly all business modules (thread, activity, alias, blacklist); partner model gains messaging/activity behavior here. Status "processing"/"pending" notification values are documented as used by SMS (downstream module).

## 4. Evidence gaps / contradictions
- G1: `mail_thread.py` (5141 lines) and `discuss_channel.py` (1705) read only by targeted grep/sections; full rule inventory is PASS-2 work.
- G2: Wizards (`wizard/*`: composer, activity schedule, followers edit, template reset/preview, blacklist remove) not fetched; composer mass-mail rules unverified.
- G3: `tools/` (discuss Store, guest context decorator, link preview, parser) not studied; guest-context authorization semantics unverified.
- G4: `models/update.py` (publisher warranty) not fetched; purpose/data egress of weekly cron unverified.
- G5: Remaining models not read: canned response, ICE server, presence, push/push device, link preview, reactions, message translation, res_role, res_users_settings, call history, RTC session, voice metadata, gif favorite, plan/plan template, tracking-duration mixin, config settings, ir_* overrides (except attachment/mail_server).
- G6: Views/menus/data templates (layouts, chatter templates, subtype data, activity type data) not studied.
- G7: `webmanifest.py` shows no route decorator in grep; inherits parent routes — not verified.
- G8: Multi-company: the in-code FIXME on allowed-company check and absence of company record rules in `mail_security.xml` are source observations only; behaviour needs runtime proof.
- No contradictions detected between manifest, init rosters and fetched files. All 62 cited fetches returned HTTP 200.

## 5. Limitations
- PASS-1 breadth only; static source reading; no execution, no tests run, no runtime reachability.
- Line references (~Lnnn) are approximate pointers valid at the anchor commit only.
- Blob SHA-1 values are computed on fetched bytes and should equal the git tree blobs at the anchor; tree listing via API was not available to cross-check.
- Enterprise-only extensions and other modules' overrides of these models are out of scope.
