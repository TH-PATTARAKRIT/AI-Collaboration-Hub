# Source Map (candidate) — `sms`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

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
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

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
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

