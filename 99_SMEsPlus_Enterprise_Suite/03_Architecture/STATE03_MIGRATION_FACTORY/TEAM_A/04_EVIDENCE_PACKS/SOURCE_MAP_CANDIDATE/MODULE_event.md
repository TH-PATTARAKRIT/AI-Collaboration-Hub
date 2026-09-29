# Source Map (candidate) — `event`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `event` |
| Display name | Events Organization |
| Manifest version | 1.9 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c5f4a2350dad4f4a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/event/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `barcodes`, `base_setup`, `mail`, `phone_validation`, `portal`, `utm`
- Direct dependents in 300-module list (5): `event_booth`, `event_crm`, `event_product`, `event_sms`, `hr_skills_event`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `mass_mailing_event`, `mass_mailing_event_sms`, `test_event_full`, `website_event`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Events / Trainings, Conferences, Meetings, Exhibitions, Registrations
- Inventory of user-facing artifacts (counts): menu items 12, views 49, window actions 15, server actions 0, reports 7, mail templates 3, scheduled jobs 1, wizards 1, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (16): `event.question` (Event Question); `event.mail` (Event Automated Mailing); `event.type` (Event Template); `event.stage` (Event Stage); `event.type.ticket` (Event Template Ticket); `event.slot` (Event Slot); `event.registration` (Event Registration); `event.registration.answer` (Event Registration Answer); `event.event` (Event); `event.type.mail` (Mail Scheduling on Event Category); `event.mail.slot` (Slot Mail Scheduler); `event.question.answer` (Event Question Answer); `event.tag.category` (Event Tag Category); `event.tag` (Event Tag); `event.event.ticket` (Event Ticket); `event.mail.registration` (Registration Mail Scheduler)
- Objects extended from other modules (5): `mail.thread`, `mail.activity.mixin`, `mail.template`, `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `event.question` ← Community: `pos_event`; open-license custom/third-party scanned: —
- `event.mail` ← Community: `event_sms`; open-license custom/third-party scanned: —
- `event.type` ← Community: `event_booth`, `website_event`, `website_event_booth`, `website_event_exhibitor`, `website_event_track`; open-license custom/third-party scanned: —
- `event.type.ticket` ← Community: `event_product`; open-license custom/third-party scanned: —
- `event.slot` ← Community: `pos_event`, `website_event`; open-license custom/third-party scanned: —
- `event.registration` ← Community: `event_crm`, `event_crm_sale`, `event_product`, `event_sale`, `mass_mailing_event`, `pos_event`, `pos_event_sale`, `website_event`, `website_event_crm`; open-license custom/third-party scanned: —
- `event.registration.answer` ← Community: `pos_event`; open-license custom/third-party scanned: —
- `event.event` ← Community: `event_booth`, `event_crm`, `event_product`, `event_sale`, `hr_skills_event`, `mass_mailing_event`, `mass_mailing_event_sms`, `mass_mailing_event_track`, `mass_mailing_event_track_sms`, `pos_event` … (+5); open-license custom/third-party scanned: —
- `event.type.mail` ← Community: `event_sms`; open-license custom/third-party scanned: —
- `event.question.answer` ← Community: `event_crm`, `pos_event`; open-license custom/third-party scanned: —
- `event.tag.category` ← Community: `website_event`; open-license custom/third-party scanned: —
- `event.tag` ← Community: `website_event`; open-license custom/third-party scanned: —
- `event.event.ticket` ← Community: `event_product`, `event_sale`, `pos_event`, `website_event_sale`; open-license custom/third-party scanned: —
- `event.mail.registration` ← Community: `event_sms`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.thread`, `mail.activity.mixin`, `mail.template`, `res.config.settings`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: `event.registration` → ['draft', 'open', 'done', 'cancel']
- Validation: 10 declarative constraint method(s), 3 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Event: Mail Scheduler every 24 hours
- Security: groups declared 4 (`group_event_registration_desk`, `group_event_user`, `group_event_manager`, `base.default_user_group`); record rules 3 (of which company-scoped by text 3); access rows 37

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

