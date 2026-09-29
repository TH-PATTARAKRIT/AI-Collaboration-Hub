# Source Map (candidate) — `mail`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mail` |
| Display name | Discuss |
| Manifest version | 1.19 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `aa251bd517b4cf25` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mail/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `base_setup`, `bus`, `web_tour`, `html_editor`
- Direct dependents in 300-module list (35): `analytic`, `auth_signup`, `auth_totp_mail`, `base_automation`, `base_install_request`, `calendar`, `cloud_storage`, `contacts`, `crm`, `digest`, `event`, `fleet` … (+23)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (8): `data_recycle`, `lunch`, `mass_mailing`, `test_discuss_full`, `test_http`, `test_mail`, `test_mail_full`, `test_mail_sms`
- Custom / third-party modules that declare a dependency (name — license only) (16): `nthub_binary_field_preview` — LGPL-3, `multi_level_approval` — OPL-1, `purchase_request_level_approve` — LGPL-3, `tracking_history` — LGPL-3, `purchase_request_level_approve_po` — LGPL-3, `agreement` — AGPL-3, `bh_parent_company` — LGPL-3, `deepseek_r1` — GPL-3, `auto_database_backup` — LGPL-3, `social_hub` — LGPL-3, `oi_jasper_report` — OPL-1, `web_chatter_resize` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Discuss / Chat, mail gateway and private channels
- Inventory of user-facing artifacts (counts): menu items 37, views 117, window actions 42, server actions 0, reports 0, mail templates 0, scheduled jobs 8, wizards 10, web routes 55
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (55): `mail.activity.schedule` (Activity schedule plan Wizard); `mail.followers.edit` (Followers edit wizard); `mail.compose.message` (Email composition wizard); `mail.blacklist.remove` (Remove email from blacklist wizard); `mail.template.reset` (Mail Template Reset); `mail.template.preview` (Email Template Preview); `mail.activity.schedule.line` (Mail Activity Schedule Line); `publisher_warranty.contract` (Publisher Warranty Contract); `mail.ice.server` (ICE Server); `mail.followers` (Document Followers); `mail.blacklist` (Mail Blacklist); `mail.activity.plan` (Activity Plan); `mail.notification` (Message Notifications); `mail.push` (Push Notifications); `mail.link.preview` (Store link preview data); `mail.activity.plan.template` (Activity plan template); `res.users.settings.volumes` (User Settings Volumes); `mail.alias.mixin.optional` (Email Aliases Mixin (light)); `mail.activity.type` (Activity Type); `mail.scheduled.message` (Scheduled Message); `mail.message.link.preview` (Link between link previews and messages); `mail.message.subtype` (Message subtypes); `fetchmail.server` (Incoming Mail Server); `mail.alias.domain` (Email Domain); `mail.template` (Email Templates) … (+30)
- Objects extended from other modules (24): `base.module.uninstall`, `base.partner.merge.automatic.wizard`, `ir.mail_server`, `ir.model`, `bus.listener.mixin`, `ir.http`, `base`, `ir.attachment`, `res.users.settings`, `ir.ui.menu`, `ir.ui.view`, `res.company`, `ir.qweb`, `ir.model.fields`, `ir.config_parameter`, `res.users`, `res.config.settings`, `ir.actions.act_window.view`, `ir.cron`, `ir.websocket`, `ir.actions.server`, `res.partner`, `avatar.mixin`, `res.groups`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `mail.activity.schedule` ← Community: `calendar`, `hr`, `hr_recruitment`; open-license custom/third-party scanned: —
- `mail.compose.message` ← Community: `marketing_card`, `mass_mailing`; open-license custom/third-party scanned: `account_credit_control`
- `publisher_warranty.contract` ← Community: `website_mail`; open-license custom/third-party scanned: —
- `mail.followers` ← Community: `sms`; open-license custom/third-party scanned: —
- `mail.blacklist` ← Community: `mass_mailing`; open-license custom/third-party scanned: —
- `mail.activity.plan` ← Community: `hr`, `hr_recruitment`; open-license custom/third-party scanned: —
- `mail.notification` ← Community: `sms`, `sms_twilio`, `snailmail`; open-license custom/third-party scanned: —
- `mail.activity.plan.template` ← Community: `hr`, `hr_fleet`; open-license custom/third-party scanned: —
- `mail.alias.mixin.optional` ← Community: `account`, `test_mail`; open-license custom/third-party scanned: —
- `mail.activity.type` ← Community: `calendar`, `fleet`, `hr_holidays`; open-license custom/third-party scanned: —
- `mail.message.subtype` ← Community: `hr_holidays`; open-license custom/third-party scanned: —
- `fetchmail.server` ← Community: `google_gmail`, `microsoft_outlook`; open-license custom/third-party scanned: —
- `mail.template` ← Community: `account`, `event`, `pos_self_order`; open-license custom/third-party scanned: —
- `mail.render.mixin` ← Community: `link_tracker`, `marketing_card`, `mass_mailing`, `sms`; open-license custom/third-party scanned: —
- `mail.thread.main.attachment` ← Community: `account`, `hr`, `hr_expense`, `hr_holidays`, `hr_recruitment`, `l10n_id_efaktur_coretax`, `l10n_it_edi_doi`, `test_mail`; open-license custom/third-party scanned: —
- `mail.alias.mixin` ← Community: `crm`, `hr_recruitment`, `mail_group`, `maintenance`, `project`, `test_mail`; open-license custom/third-party scanned: —
- `mail.thread` ← Community: `account`, `analytic`, `base_automation`, `calendar`, `event`, `event_booth`, `fleet`, `gamification`, `hr`, `hr_attendance` … (+43); open-license custom/third-party scanned: `account_asset_management`, `account_credit_control`, `agreement`, `auto_database_backup`, `base_account_budget`, `base_accounting_kit`, `bh_parent_company`, `l10n_th_withholding_tax_cert` … (+7)
- `mail.tracking.value` ← Community: `account`; open-license custom/third-party scanned: —
- `mail.activity` ← Community: `calendar`, `crm`, `website_slides`; open-license custom/third-party scanned: —
- `mail.alias` ← Community: `hr`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `base.module.uninstall`, `base.partner.merge.automatic.wizard`, `ir.mail_server`, `ir.model`, `bus.listener.mixin`, `ir.http`, `base`, `ir.attachment`, `res.users.settings`, `ir.ui.menu`, `ir.ui.view`, `res.company`, `ir.qweb`, `ir.model.fields`, `ir.config_parameter`, `res.users`, `res.config.settings`, `ir.actions.act_window.view`, `ir.cron`, `ir.websocket`, `ir.actions.server`, `res.partner`, `avatar.mixin`, `res.groups`

## 6. Actions / states / validation / automation / security
- State fields found: `fetchmail.server` → ['draft', 'done']; `mail.presence` → ['online', 'away', 'offline']; `mail.activity` → ['overdue', 'today', 'planned', 'done']; `mail.mail` → ['outgoing', 'sent', 'received', 'exception', 'cancel']
- Validation: 22 declarative constraint method(s), 23 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Mail: Email Queue Manager every 1 hours; Publisher: Update Notification every 1 weeks; Notification: Delete Notifications older than 6 Months every 1 months; Mail: Fetchmail Service every 5 minutes; Mail: Post scheduled messages every 1 days; Notification: Notify scheduled messages every 1 hours; Mail: send web push notification every 1 days; Discuss: channel member unmute every 1 days
- Security: groups declared 4 (`group_mail_canned_response_admin`, `group_mail_template_editor`, `base.group_system`, `group_mail_notification_type_inbox`); record rules 26 (of which company-scoped by text 0); access rows 69

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 131 of 133 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: `mail` (Odoo 19 Community, revision 19.0.post20260921)

Scope: neutral business reading of the messaging/chatter module. Pointers are `module/path:LINE` relative to the addons root. Items marked (TEST) come from test modules (`mail/tests`, `test_mail/tests`), not from production code. Skeleton used for orientation: sourcemap/mail.json. Nothing was executed.

## A. Capabilities (core / optional / conditional)

Identity and packaging
- Module is an installable application ("Discuss") depending only on base, base_setup, bus, web_tour, html_editor (mail/__manifest__.py:63,137,138). It is the foundation that most business modules attach to.

Core (present whenever the module is installed)
- Document conversation log ("chatter") that any business record can carry: posted messages, internal notes, system logs (mail/models/mail_thread.py:2199 `message_post`, :2913 `_message_log_batch`).
- Field-change audit trail: fields flagged for tracking generate a log message with old/new values (mail/models/mail_thread.py:527-700, mail/models/models.py:226, mail/models/mail_tracking_value.py:68).
- Followers and subscription preferences per record and per message subtype (mail/models/mail_followers.py:11, mail/models/mail_thread.py:4639-4850, mail/models/mail_message_subtype.py:7).
- Notification dispatch to recipients through inbox, email and web push (mail/models/mail_thread.py:3279 `_notify_thread`, :3340, :3394, :3895).
- Outgoing email queue with retry states and cron sender (mail/models/mail_mail.py:26, :194; mail/data/ir_cron_data.xml:4).
- Activities (to-dos with deadline, owner, type, chaining) and activity plans (mail/models/mail_activity.py:19, mail/models/mail_activity_plan.py:7).
- Email templates with placeholder rendering (mail/models/mail_template.py:17) and a compose wizard (mail/wizard/mail_compose_message.py:31).
- Attachments attached to messages and to the document (mail/models/mail_message.py:104-108 field; mail/models/mail_thread.py:2387 `_process_attachments_for_post`).

Optional / configuration-dependent
- Incoming mail routing through aliases, catch-all and bounce addresses: requires an alias domain and an incoming mail source (mail/models/mail_alias.py:19, mail/models/mail_alias_domain.py:9, mail/models/mail_thread.py:1122).
- Incoming mail server polling (POP/IMAP): the polling job is created inactive and is switched on by server records (mail/data/ir_cron_data.xml:40-49, mail/models/fetchmail.py:89 onward).
- Personal outgoing mail servers per user (mail/models/ir_mail_server.py:10-30, mail/models/mail_mail.py:349-355).
- Email address blacklist: a mixin a model must opt into; sending honours it only in composer mass mode (mail/models/mail_thread_blacklist.py:9, mail/wizard/mail_compose_message.py:1478-1499).
- Scheduled messages (post later) and delayed notifications (mail/models/mail_scheduled_message.py:17, mail/models/mail_message_schedule.py:14).
- Server-action extensions: send email, add/remove followers, create activity (mail/models/ir_actions_server.py:9-40).
- Out-of-office auto-notice for users (mail/models/res_users.py:39-42, :101-109; mail/models/mail_thread.py:4385).

Conditional / secondary (not ERP-critical)
- Discuss channels, chats, groups, calls, GIFs, voice, link previews, canned responses, push devices: separate model family under mail/models/discuss/ and the mail/models/mail_link_preview.py, mail_canned_response.py, mail_push*.py files. Channel type set: chat / channel / group (mail/models/discuss/discuss_channel.py:69-73).
- Outside the module on purpose: mass mailing, SMS, snailmail, mail groups, livechat, portal chatter are separate modules (see section F/D).

## B. Business objects, relationships, lifecycle

Objects (neutral names)
- Message (`mail.message`): one entry in a record's conversation. Carries author, recipients, document link (model + record id), type, subtype, internal flag, attachments, optional tracking lines (mail/models/mail_message.py:23-203). Types: incoming email, comment, outgoing email, system notification, automated comment, out-of-office, user notification (mail/models/mail_message.py:119-141).
- Tracking line (`mail.tracking.value`): one field change (old value, new value, currency) tied to a message; deleted with its message (mail/models/mail_tracking_value.py:12-45, field `mail_message_id` ondelete cascade at :43).
- Subtype (`mail.message.subtype`): category of message that decides who is notified; flags internal-only, default, hidden, parent link for cascading subscriptions (mail/models/mail_message_subtype.py:7-45). Seeded: Discussions, Note (internal, off by default), Activities (internal) (mail/data/mail_message_subtype_data.xml:4-21).
- Follower (`mail.followers`): partner subscribed to one record with a chosen set of subtypes; unique per (model, record, partner) (mail/models/mail_followers.py:69).
- Notification (`mail.notification`): per-recipient delivery record for a message: type inbox/email, status ready/sent/bounce/exception/canceled, read flag and read date, failure type/reason (mail/models/mail_notification.py:12-58).
- Outgoing email (`mail.mail`): queued email built on a message; states outgoing/sent/received/exception/cancel; failure type and reason; scheduled date; auto-delete flag (mail/models/mail_mail.py:26-100).
- Activity (`mail.activity`): task on a record or free-standing, with type, deadline, assignee, note, feedback, done date, `automated` flag (mail/models/mail_activity.py:19-108). Activity type (`mail.activity.type`): default delay, chaining "suggest" or "trigger", templates (mail/models/mail_activity_type.py:10-60). Plan (`mail.activity.plan`) with ordered templates (mail/models/mail_activity_plan.py:7, mail/models/mail_activity_plan_template.py:10).
- Template (`mail.template`): subject/body/recipients with placeholders, optional attachments, reports, preferred outgoing server, scheduled date, auto-delete (default true) (mail/models/mail_template.py:17-96).
- Alias (`mail.alias`) and alias domain (`mail.alias.domain`): map an inbound address to a model and default values; the domain carries bounce, catch-all and default-from local parts, and is linked to companies (mail/models/mail_alias.py:19-95, mail/models/mail_alias_domain.py:9-60).
- Fetch server (`fetchmail.server`), blacklist entry (`mail.blacklist`), scheduled message, message schedule, presence, guest, push device.

Relationships
- Message -> record: by model name plus record id (no database foreign key); index on the pair (mail/models/mail_message.py:110-112, :205). Followers, activities, scheduled messages are linked the same way and are removed by code when the record is deleted (mail/models/mail_thread.py:399-412, mail/models/models.py:41-55).
- Message -> notifications (one per recipient), -> tracking lines, -> attachments, -> outgoing emails (mail/models/mail_message.py:168-176, :203).
- Outgoing email inherits the message (delegation) so one email row = one message row plus email envelope data (mail/models/mail_mail.py:31, :62).

Lifecycle
- Record creation: creator auto-follows (unless suppressed), auto-subscription by parent/assignee runs, a "created" log is written (mail/models/mail_thread.py:313-380). Suppression switches: `mail_create_nosubscribe`, `mail_create_nolog`, `mail_notrack`, `tracking_disable` (mail/models/mail_thread.py:99-104, :324, :371).
- Record update: initial values of tracked fields are captured, and at transaction pre-commit one message with one tracking line per changed field is written (mail/models/mail_thread.py:527-575, :645-700). A change from empty to empty is not tracked (mail/models/models.py:257).
- Posting: message created, author auto-follow for discussion type, notifications computed and dispatched (mail/models/mail_thread.py:2199-2375).
- Email path: notification -> `mail.mail` (state outgoing) -> sent immediately after commit if fewer than the force-send limit (default 100), otherwise left for the queue cron -> state sent, or exception with a reason (mail/models/mail_thread.py:3506-3524, mail/models/mail_mail.py:194-249, :769-980).
- Activity: create -> optional notification to assignee -> "mark done" posts a message under the Activities subtype, then archives the activity (history kept) and can create the chained next activity (mail/models/mail_activity.py:274-300, :514-598).
- Record deletion: its messages, followers, scheduled messages and activities are deleted (mail/models/mail_thread.py:399-412, mail/models/models.py:41-55).

## C. Validations, automation, security, audit

Validations and constraints
- Follower uniqueness per record/partner (mail/models/mail_followers.py:69).
- Notification: inbox needs a partner; email needs a partner, an address or a failure type; unique per (message, partner) (mail/models/mail_notification.py:60-71).
- Activity: a document link needs a record id; an activity without document must have an assignee (mail/models/mail_activity.py:110-124). Plan template step: activity type model must match plan model; "default user" assignment needs a user (mail/models/mail_activity_plan_template.py:59-85).
- Alias: unique (name, domain); ASCII-only local part; default values must be a literal dictionary; must not equal bounce/catch-all alias; alias domain must match the owning record's company domain (mail/models/mail_alias.py:96, :179, :194, :204, :100-165).
- Alias domain: bounce and catch-all addresses unique (mail/models/mail_alias_domain.py:44-51).
- Personal mail server: one per owner (mail/models/ir_mail_server.py:29); an email cannot use another user's server (mail/models/mail_mail.py:101-105).
- Blacklist: unique normalised address; invalid address rejected (mail/models/mail_blacklist.py:19, :28-41).
- Template: cannot target an abstract model; rendering is test-run at save (mail/models/mail_template.py:200-232, :247-263).
- Scheduled message: cannot be set in the past and needs a threaded model (mail/models/mail_scheduled_message.py:59-68).
- Notification type "in Odoo" not allowed for portal/shared users (mail/models/res_users.py:70-73).
- Channel: a chat has at most two members; group-based access only on plain channels (mail/models/discuss/discuss_channel.py:129-181).

Automation (scheduled jobs, all in mail/data/ir_cron_data.xml)
- Email queue manager: hourly, up to 1000 emails per run, priority 6 (:4-13; batch size overridable by system parameter, mail/models/mail_mail.py:215).
- Notification purge: monthly; deletes read, delivered/cancelled notifications older than 180 days for internal recipients (:31-38; mail/models/mail_notification.py:93-102).
- Incoming mail polling: every 5 minutes, ships inactive and is toggled by server records; a server failing for 5 days is put back to draft and admins are alerted (:40-49; mail/models/fetchmail.py:21, :323-330).
- Scheduled message posting: daily plus on-demand trigger; sends up to 50 per run (:51-58; mail/models/mail_scheduled_message.py:278-288).
- Delayed notification sender: hourly, also triggered at each scheduled time (:60-67; mail/models/mail_message_schedule.py:45-52, :35-41).
- Web push sender daily; mute-expiry daily; publisher update notification weekly (:69-88, :15-25).
- Auto-vacuum: overdue activity cleanup, only if the year threshold is above 0 (mail/models/mail_activity.py:860-878); seeded threshold value is 3 years (mail/data/ir_config_parameter_data.xml:4-7).

Security: groups
- Template Editor group; Canned Response Admin group; "Receive notifications in Odoo" group that drives inbox vs email notification type; system administrators imply the first two (mail/data/mail_groups.xml:8-30; mail/models/res_users.py:76-95).

Security: model access (mail/security/ir.model.access.csv)
- Messages: public read only; portal and internal users read/write/create/delete at model level (:3-5), narrowed by document logic below.
- Outgoing emails, tracking lines, scheduled-message queue, fetch servers, blacklist, reactions: administrators only (:2, :6, :7, :37; blacklist row in same file).
- Followers: internal read-only; administrators full (:8-9). Notifications: portal read, internal read/write/create without delete, admin full (:10-12).
- Aliases and alias domains: internal read; alias write for admins, alias domain write for the ERP manager group (:26-29).
- Templates: all internal users have full model access, then record rules limit changes (:39-41).

Security: record rules (mail/security/mail_security.xml)
- Message access is NOT governed by a record rule; it is coded in `_check_access` (mail/models/mail_message.py:453-490, :493-640). Read: author, creator, recipient/notified partner, or read access to the target document. Write: author, recipient, or write access to the document. Create: document write access (or the model's `_mail_post_access`, default write, :132 in mail_thread.py), follower, or reader of the parent message. Delete: document write access. Non-employees never see messages without subtype, internal-flagged or internal-subtype messages, and only comment-type on read/create (:509-530).
- Activity: coded check plus a rule limiting change/delete to assignee or creator (mail/models/mail_activity.py:197-255; mail/security/mail_security.xml:240-249). Read is allowed for the assignee or with read access to the document.
- Template: employees may change only templates they created or own; template editors and admins change all (mail_security.xml:275-295).
- Notifications: internal/portal users may write only their own entries; portal users read own or authored (:216-232).
- Subtypes: portal/public see only non-internal subtypes (:233-239).
- Channels and members: membership/group-based rules (:3-200); canned responses: own or group-shared (:319-345); scheduled messages: creator only (:346-353).
- Company scoping: no company rule exists in this file for messages, followers, activities, templates or plans. Company enters through message field `record_company_id` and `record_alias_domain_id` set at post time (mail/models/mail_thread.py:2343-2347), the alias-domain-to-company link (mail/models/res_company.py:10-12) and alias/company consistency validation (mail/models/mail_alias.py:100-165). Plan has a company field (mail_activity_plan.py:23) but no rule references it. Document-level company rules of the target model apply indirectly because message access defers to the document (mail/models/mail_message.py:400-425).

Audit / tracking implications (what is stored, where, who sees or deletes)
- Tracked-field changes are stored as message + tracking lines: old/new value in typed columns; many2one keeps id and display text; many2many keeps text list; selection keeps label text; monetary keeps currency (mail/models/mail_tracking_value.py:68-150). Only fields explicitly flagged tracking on the model are captured (mail/models/mail_thread.py:616-631); examples of flagged ERP fields: sale order amounts and status (sale/models/sale_order.py:69,75,233,235), purchase order status/amount/buyer (purchase/models/purchase_order.py:111,137,158).
- Actor and time: taken from the message author and creation stamp. Author of an automatic tracking message is the acting user unless overridden (mail/models/mail_thread.py:583-589); (TEST) author check test_message_track_author (test_mail/tests/test_message_track.py:28).
- Untracked-value logging is disabled by context `mail_notrack` or `tracking_disable`; (TEST) no message produced (test_mail/tests/test_message_track.py:220-234). Copying a record also disables tracking (mail/models/mail_thread.py:416). Imports/tools using these keys leave no trail.
- Visibility: the tracking-line list on a message is administrator-group only at field level (mail/models/mail_message.py:180-185); the chatter shows lines only for fields the viewer may read (mail/models/mail_message.py:1256-1273, mail/models/mail_tracking_value.py:37-55). (TEST) field with restricted group hides its value from a normal employee (test_mail/tests/test_message_track.py:788-848).
- Removal: tracking lines vanish when their message is deleted (cascade). Message delete needs write access on the document (mail/models/mail_message.py:826-847). Editing message content is refused for messages with tracking lines and for any non-comment message (mail/models/mail_thread.py:511-521); UI edit route is limited to author or administrator (mail/controllers/thread.py:262-264). Moving a message to another record or changing its type is administrator-only for record link (mail/models/mail_message.py:812-817). There is no separate immutable audit store: log messages can be removed by anyone with document write access through direct data calls.
- Log-only messages (no subtype) are written as internal notes in bulk with elevated rights and no notification (mail/models/mail_thread.py:2913-2967).
- Outgoing email traces: with default auto-delete true (mail_template.py:94; notification flow default in mail_thread.py:3395), the email row is erased after successful send; the message and notification rows remain as the durable trace, and failed sends (except invalid/missing address) are kept (mail/models/mail_mail.py:250-290).
- Notification rows expire after 180 days once read (see cron above); failure reasons persist until then.
- Activity history: done activities are archived, not deleted; feedback text and done date kept (mail/models/mail_activity.py:590-598); a chatter message records completion (:545-560).
- Tracked config models: server actions and scheduled jobs are themselves threaded and track key fields (mail/models/ir_actions_server.py:9-20; mail/models/ir_cron.py:6); the blacklist tracks address and active flag (mail/models/mail_blacklist.py:12-17).

## D. Handoffs to other modules (owner in parentheses)

- Per-document tracked fields, subtypes and tracking templates are defined by the owning business module: sale (sale/models/sale_order.py:40 `_mail_post_access = "read"`, :69), purchase (purchase/models/purchase_order.py:111), account, stock, mrp, project, hr*, crm, maintenance, repair, fleet, etc.
- Assignee auto-follow and "assigned to you" notice fire when a tracked `user_id`-type field changes; the owning model may override (mail/models/mail_thread.py:4710-4732).
- Customer mail sending from documents: business modules call the template/compose services; the compose wizard is extended by mass_mailing and marketing_card (extension list F).
- Mass mailing, blacklist opt-out, bounce statistics: mass_mailing (extends mail.mail, mail.blacklist, compose). SMS notifications: sms (adds sms as notification type). Postal letters: snailmail. Alias-driven record creation (leads, applicants, maintenance requests, tasks): crm, hr_recruitment, maintenance, project.
- Portal access and customer-visible chatter: portal, portal_rating, rating, website_* modules extend `mail.message`.
- Outgoing server, bounce and default-from configuration reside in base + mail (company alias domain, mail/models/res_company.py:10-12).
- Attachment content lives in base `ir.attachment` (mail adds thumbnail, ownership checks and main-attachment logic, mail/models/ir_attachment.py:11-60); the main-attachment mixin is used by account, hr_expense, hr, hr_holidays (F).
- Server actions and automation rules run through base_automation, which is itself a threaded model (F).

## E. Configuration and defaults that change outcomes

System parameters (documented in mail/models/ir_config_parameter.py:8-60; read at the call sites shown)
- `mail.mail.queue.batch.size` (default 1000, mail_mail.py:215), `mail.mail.force.send.limit` (default 100; 0 forces everything through the queue, mail_thread.py:3514), `mail.batch_size` (50, mail_thread.py:3451, mail_template.py:714), `mail.session.batch.size` (1000, mail_mail.py:581).
- `mail.disable_personal_mail_servers`: removes personal servers from selection (mail_mail.py:352).
- `mail.gateway.loop.minutes` (120) and `mail.gateway.loop.threshold` (20): incoming loop protection; senders on the gateway-allowed list are exempt (mail_thread.py:1004-1030).
- `mail.catchall.domain.allowed`: restricts accepted recipient domains (mail_thread.py:1150-1162).
- `mail.activity.gc.delete_overdue_years`: seeded 3, code fallback 0 (= disabled) (data/ir_config_parameter_data.xml:4-7; mail_activity.py:868-877).
- `mail.restrict.template.rendering`: seeded 1, i.e. only template editors may create/modify templates using non-default placeholders (data/ir_config_parameter_data.xml:8-11; mail/models/mail_render_mixin.py:260-306; settings label mail/models/res_config_settings.py:20-25).

Behaviour switches (context keys) that skip audit or notification: `mail_notrack`, `tracking_disable`, `mail_create_nolog`, `mail_create_nosubscribe`, `mail_post_autofollow`, `mail_notify_force_send`, `mail_activity_automation_skip`, `mail_auto_subscribe_no_notify` (mail_thread.py:99-104, :125; mail_activity_mixin.py:34, :334; mail_thread.py:121, :4754).

Record-level defaults
- Model attributes: `_mail_post_access` (default write, some models read: sale_order.py:40, project_task.py:102, hr_expense.py:48, hr_holidays/models/hr_leave.py:73), `_mail_flat_thread` (default true, mail_thread.py:130), `_mail_thread_customer` (default false, mail_thread.py:131).
- Posting default subtype is Note when none is given (mail_thread.py:2303-2305); discussion-type posts auto-follow internal authors (mail_thread.py:2352-2362).
- Alias default contact policy is "everyone"; alternatives "authenticated partners" and "followers only" (mail_alias.py:73-82). Alias status becomes valid on first successful record creation and invalid on configuration error (mail_thread.py:1381-1382; mail_alias.py:88-93, :527).
- Notification type per user: email by default, inbox via group (res_users.py:29-37, :76-95). Company email colours default white/purple (res_company.py:28-33).
- Templates default auto-delete true and default recipients true (mail_template.py:53-57, :94).
- Activity type seed: Email, Call, Meeting, To-Do, Document (upload), Exception (inactive) with default delays (mail/data/mail_activity_type_data.xml:4-40).
- Activity chaining default is "suggest"; "trigger" auto-creates the next activity on completion (mail_activity_type.py:52-58; mail_activity.py:514-540).
- Bounce/catch-all/default-from local parts default `bounce`, `catchall`, `notifications` (mail_alias_domain.py:22-42).
- Incoming-mail settings: attachments kept only if the server flag is set; original email stored only if flagged (fetchmail.py:111-114); batch limit 50 per server per run (fetchmail.py:263).

Incoming routing order (mail_thread.py:1122-1341): bounce handling first; then reply-to-existing-thread by message references; then alias match; then fallback model; then catch-all bounce; else error. Duplicate Message-Id is ignored (mail_thread.py:1483-1494). Alias contact policy check `followers`/`partners` at mail/models/models.py:785-802. (TEST) bounce, followers-only and partners-only alias behaviour: test_mail/tests/test_mail_gateway.py:691-756, :1065-1300.

## F. Effective extension path (direct `_inherit` found by pattern scan of non-test files; module names only)

- mail.thread: account, analytic, base_automation, calendar, event, event_booth, fleet, gamification, hr, hr_attendance, hr_holidays, hr_recruitment, iap_mail, l10n_fr_pdp, l10n_in, l10n_in_ewaybill, l10n_latam_check, l10n_my_edi, loyalty, lunch, mail, maintenance, marketing_card, mass_mailing, mrp, phone_validation, point_of_sale, portal, product, project, purchase, purchase_requisition, rating, repair, sale, sales_team, sms, snailmail, stock, stock_landed_costs, stock_picking_batch, survey, website_blog, website_event_exhibitor, website_event_track, website_forum, website_sale, website_slides (test-only modules omitted).
- mail.message: account, im_livechat, mail (discuss), portal, portal_rating, project, rating, sms, snailmail, website_slides.
- mail.mail: mass_mailing.
- Related mixins: mail.activity.mixin used by account, base_automation, calendar, crm, event, fleet, hr, hr_expense, hr_holidays, hr_recruitment, l10n_* (in, my, latam_check, fr_pdp, id_efaktur_coretax, it_edi_doi), lunch, maintenance, marketing_card, mass_mailing, mrp, point_of_sale, product, project, purchase, purchase_requisition, repair, sale, stock, stock_landed_costs, stock_picking_batch, survey, website_event_*, website_slides. mail.thread.cc: crm, hr_recruitment, maintenance, project. mail.alias.mixin: crm, hr_recruitment, mail_group, maintenance, project. mail.thread.blacklist: mass_mailing (crm and hr_recruitment also reference it). mail.thread.main.attachment: account, hr, hr_expense, hr_holidays, hr_recruitment, l10n_id_efaktur_coretax, l10n_it_edi_doi.
- Other mail models extended: mail.template (account, event, pos_self_order), mail.activity (calendar, crm, website_slides), mail.compose.message (marketing_card, mass_mailing), mail.followers (sms), mail.notification (sms, sms_twilio, snailmail), mail.message.subtype (hr_holidays), mail.tracking.value (account), mail.alias (hr).
- Caveat: models that gain threading only through a mixin (for example crm leads via `mail.thread.cc`) are not listed under mail.thread above. Scan covers class-level `_inherit` text only.

## G. Not verified

- UNKNOWN — EVIDENCE INSUFFICIENT: whether any installed non-Community layer changes tracking retention, message deletion rights or audit immutability.
- UNKNOWN — EVIDENCE INSUFFICIENT: runtime behaviour of the email queue under real SMTP failures, concurrency and cron scheduling (no execution performed).
- UNKNOWN — EVIDENCE INSUFFICIENT: complete list of tracked fields per business model; only sale and purchase samples were pointed to, others were not enumerated.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether front-end views expose message deletion to users beyond editing (only server-side checks and the edit route were read).
- UNKNOWN — EVIDENCE INSUFFICIENT: multi-company outcomes for messages and followers when the target model has its own company rule (behaviour derived from code path only; test_mail/tests/test_mail_multicompany.py not reviewed).
- UNKNOWN — EVIDENCE INSUFFICIENT: contents of discuss controllers, websocket/bus behaviour, RTC/call handling, link-preview, translation and push internals (only located, not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: data-neutralisation script effects (mail/data/neutralize.sql not opened).
- Findings on message-level access apply to the paths read (`_check_access`, create/write/unlink); other direct-database or sudo callers in other modules were not audited.

