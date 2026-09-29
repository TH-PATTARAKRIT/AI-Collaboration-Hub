# Source Map (candidate) — `sms`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sms` |
| Display name | SMS gateway |
| Manifest version | 3.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `952df6b919b024c7` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sms/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `iap_mail`, `mail`, `phone_validation`
- Direct dependents in 300-module list (11): `base_automation`, `calendar_sms`, `crm_sms`, `event_sms`, `hr_presence`, `hr_recruitment_sms`, `project_sms`, `sale_sms`, `sms_twilio`, `stock_sms`, `website_sms`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (6): `mass_mailing_event_sms`, `mass_mailing_event_track_sms`, `mass_mailing_sms`, `pos_sms`, `test_mail_full`, `test_mail_sms`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / SMS Text Messaging
- Inventory of user-facing artifacts (counts): menu items 2, views 18, window actions 7, server actions 1, reports 0, mail templates 0, scheduled jobs 1, wizards 6, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (9): `sms.account.sender` (SMS Account Sender Name Wizard); `sms.account.phone` (SMS Account Registration Phone Number Wizard); `sms.account.code` (SMS Account Verification Code Wizard); `sms.composer` (Send SMS Wizard); `sms.template.preview` (SMS Template Preview); `sms.template.reset` (SMS Template Reset); `sms.sms` (Outgoing SMS); `sms.tracker` (Link SMS to mailing/sms tracking models); `sms.template` (SMS Templates)
- Objects extended from other modules (11): `mail.followers`, `ir.model`, `mail.notification`, `base`, `mail.thread`, `res.company`, `mail.render.mixin`, `template.reset.mixin`, `ir.actions.server`, `mail.message`, `iap.account`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `sms.composer` ← Community: `mass_mailing_sms`, `sms_twilio`; open-license custom/third-party scanned: —
- `sms.sms` ← Community: `mass_mailing_sms`, `sms_twilio`; open-license custom/third-party scanned: —
- `sms.tracker` ← Community: `mass_mailing_sms`, `sms_twilio`; open-license custom/third-party scanned: —
- `sms.template` ← Community: `event_sms`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.followers`, `ir.model`, `mail.notification`, `base`, `mail.thread`, `res.company`, `mail.render.mixin`, `template.reset.mixin`, `ir.actions.server`, `mail.message`, `iap.account`

## 6. Actions / states / validation / automation / security
- State fields found: `sms.sms` → ['outgoing', 'process', 'pending', 'sent', 'error', 'canceled']
- Validation: 1 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: SMS: SMS Queue Manager every 24 hours
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 0); access rows 13

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 68 of 68 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: sms (Odoo 19.0.post20260921)
Scope: only pointers cited; anything else is UNKNOWN — EVIDENCE INSUFFICIENT.

## A. Capabilities
- SMS text-messaging framework via a paid external gateway (Odoo IAP service "SMS", credit-based). sms/__manifest__.py:8-14; sms/data/iap_service_data.xml:4-10; sms/tools/sms_api.py:59,106-110.
- Send an SMS to arbitrary numbers, to one record's contact (posted as a message on the record), or in batch to many records. sms/wizard/sms_composer.py:32-36,196-208.
- SMS templates with placeholders, per applicable document type; optional sidebar action to send from a record list/form. sms/models/sms_template.py:22-28,52-70.
- Server-action type "Send SMS" (with note / without note / note only) for automation. sms/models/ir_actions_server.py:11-25,88-105.
- Delivery tracking: status per message, later updated by provider delivery reports; failed messages can be resent. sms/controllers/main.py:15-41; sms/models/sms_sms.py:123-148.
- Account registration wizards: phone number -> verification code -> sender name. sms/wizard/sms_account_phone.py:15-27; sms_account_code.py:15-36; sms_account_sender.py:22-25.
- Core: outgoing queue, composer, tracking. Conditional: works only if IAP account has credits and registration. sms/models/sms_sms.py:216-222 (failure types incl. credit/unregistered). Manifest: auto_install True. sms/__manifest__.py:45. Depends base, iap_mail, mail, phone_validation. sms/__manifest__.py:15-20.

## B. Business objects, relationships, lifecycle
- Outgoing SMS: number, text, optional partner and originating message, unique reference (uuid), state In Queue -> Processing -> Sent -> Delivered, or Error / Cancelled; failure type list (missing number, bad format, unsupported country, no credit, server, unregistered, blacklisted, duplicate, opted out). sms/models/sms_sms.py:38-70.
- SMS Tracker: links an SMS reference to a chatter notification (or marketing trace) so status flows back even after the SMS row is deleted; reference unique. sms/models/sms_tracker.py:6-37.
- Chatter notification gains type "SMS", number, failure types; message gains type "SMS". sms/models/mail_notification.py:10-32; sms/models/mail_message.py:12-14.
- SMS template: name, applies-to model (only models with phone/partner fields), body; optional sidebar action. sms/models/sms_template.py:22-32; sms/models/ir_model.py:10-25.
- IAP account gains sender name (read-only, from provider). sms/models/iap_account.py:9,31-35.
- Lifecycle: created In Queue (cron triggered on create) -> sent to provider in batches -> success marks "Sent" and flags for deletion; failure marks Error; provider report later moves to Delivered or failure; flagged rows purged by autovacuum. sms/models/sms_sms.py:77-80,99-118,173-225,237-240; sms/controllers/main.py:34-40.
- Tracker states map to notification states and never move backwards (e.g. delivered not overwritten by pending). sms/models/sms_tracker.py:61-75.

## C. Validations, automation, security, session/audit
- Single recipient must have a valid number; multi-recipient comment mode blocks if any invalid; free-typed numbers must be well-formed else error. sms/wizard/sms_composer.py:145-153,155-167,182-189.
- Mass mode never blocks; instead each record is created Cancelled with a reason: blacklisted, opted out (hook, void by default), duplicate number, missing/malformed number. sms/wizard/sms_composer.py:317-352; opt-out void: 288-291.
- Blacklist check can be turned off by the sender (default on). sms/wizard/sms_composer.py:50-52,283-286.
- Options: keep a note on the document (default yes), send immediately (default no, else queue by cron). sms/wizard/sms_composer.py:48-49,255-265.
- Editing the recipient number in single mode writes it back to the record's number field. sms/wizard/sms_composer.py:229-233.
- Sender name rule: 3-11 letters/digits; cannot change once set (provider-side). sms/wizard/sms_account_sender.py:16-20; sms/tools/sms_api.py:11-13.
- Queue cron: every 24 hours as well as triggered on new SMS; batch size parameter default 500; rows locked while sending. sms/data/ir_cron_data.xml:3-10; sms/models/sms_sms.py:79,150-164.
- Sending failure to reach provider: recorded as server error, not raised unless requested; retries may cause duplicate sends (documented warning). sms/models/sms_sms.py:99-104,198-202.
- Company: SMS sent in the company of the originating message, else current company; provider class chosen per company (overridable). sms/models/sms_sms.py:166-167,177-179; sms/models/res_company.py:9-11.
- Delivery-report endpoint is public (no login) but validates format (32-hex references, word-char status) and only touches known references; no shared secret seen: authenticity check beyond format UNKNOWN — EVIDENCE INSUFFICIENT. sms/controllers/main.py:15,43-49.
- Access: SMS and tracker records - system administrators only; templates - internal users read only, administrators full; composer/preview wizards - internal users; template reset - template editors group; registration wizards - administrators. sms/security/ir.model.access.csv:2-14. Extra rule gives administrators all templates. sms/security/sms_security.xml:3-8.
- Users can send SMS though they cannot see SMS rows: sending runs with elevated rights internally. sms/wizard/sms_composer.py:219,356; sms/models/mail_thread.py:174,213,228.
- Template rendering restriction: when restricted-rendering setting is on, non-editors can use template as is but not type new dynamic code (TEST). sms/tests/test_sms_template.py:74-96; sms/models/sms_template.py:13.
- Provider call sends account token and database identifier to the endpoint (default vendor URL, overridable by parameter). sms/tools/sms_api.py:59,74-77.
- Audit: message with type SMS and per-recipient notification (number, status, failure) on the record; external delivery/credit data not stored beyond that. sms/models/mail_thread.py:215-228. No dedicated audit trail seen.
- Notification cancel by type deletes pending SMS. sms/models/mail_thread.py:240-246.
- Phone-number sanitising depends on phone_validation and country context: UNKNOWN — EVIDENCE INSUFFICIENT for exact rules (module phone_validation not read).

## D. Handoffs
- mail: SMS as a message/notification channel; followers can be set to be notified by SMS. sms/models/mail_thread.py:138-144,146-233; sms/models/mail_followers.py:10-29.
- phone_validation: number formatting, blacklist model, top menu (SMS and Templates menus under it). sms/models/models.py:8-109; sms/views/sms_sms_views.xml:69-72; sms/views/sms_template_views.xml:93-97.
- iap / iap_mail: account, credits, buy-credits link, registration state. sms/models/iap_account.py; sms/tools/sms_api.py:68,117.
- Partner form: blacklisted-number warning button; partner actions to send SMS single/multi. sms/views/res_partner_views.xml:12-24,25-50.
- Server actions / automation: "Send SMS" action type; base_automation depends on sms. sms/models/ir_actions_server.py; base_automation/__manifest__.py.
- Dependent Community modules: calendar_sms, crm_sms, event_sms, hr_recruitment_sms, mass_mailing_sms, pos_sms, project_sms, sale_sms, stock_sms, website_sms, sms_twilio (manifests).
- Alternative gateway hook: provider class per company and per-call. sms/models/res_company.py:9; sms/models/sms_sms.py:120-121; sms/tools/sms_api.py:36-56.
- Web client patches for buttons, phone field, failure display. sms/static/src/**.

## E. Configuration/defaults
- Batch size parameter default 500. sms/models/sms_sms.py:163-164.
- Gateway endpoint parameter, default vendor URL. sms/tools/sms_api.py:59,76.
- Cron interval 24 h (forcecreate, noupdate). sms/data/ir_cron_data.xml:2-3,9-10.
- Composer defaults: keep note on, send directly off, exclusion list on. sms/wizard/sms_composer.py:48-52.
- Composition mode guessed: >1 records -> mass, else comment; server action sets mass or comment by chosen method. sms/wizard/sms_composer.py:72-80; sms/models/ir_actions_server.py:97-103.
- Restricted template rendering system parameter changes who can author dynamic text (TEST). sms/tests/test_sms_template.py:75.
- Demo data present (not for production). sms/__manifest__.py:40-43.

## F. Effective extension path
- iap_mail, mail, phone_validation; sms_twilio (alternative provider); mass_mailing_sms; crm_sms, sale_sms, project_sms, calendar_sms, event_sms, hr_recruitment_sms, pos_sms, stock_sms, website_sms; base_automation.

## G. Not verified
- Provider-side pricing, registration legislation per country, delivery SLAs: UNKNOWN — EVIDENCE INSUFFICIENT.
- Webhook authenticity beyond format checks: UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether the composer respects record-level access rules on target records in mass mode: UNKNOWN — EVIDENCE INSUFFICIENT.
- Test coverage (TEST): composer posting vs notification body, template access, rendering restricted/unrestricted, reset. sms/tests/test_sms_composer.py:16,46; sms/tests/test_sms_template.py:39,56,74,98,119. Shared test helpers sms/tests/common.py.
- Universal rules: none stated.

