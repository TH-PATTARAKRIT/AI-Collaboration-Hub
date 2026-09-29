# Source Map (candidate) — `mail`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

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
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

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
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

