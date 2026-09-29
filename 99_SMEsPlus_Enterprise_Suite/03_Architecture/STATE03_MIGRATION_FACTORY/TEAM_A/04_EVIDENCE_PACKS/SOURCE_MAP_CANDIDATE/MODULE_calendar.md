# Source Map (candidate) — `calendar`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `calendar` |
| Display name | Calendar |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `95e0c0f556661e6b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/calendar/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `mail`
- Direct dependents in 300-module list (8): `calendar_sms`, `crm`, `google_calendar`, `hr_calendar`, `hr_holidays`, `hr_homeworking_calendar`, `hr_recruitment`, `microsoft_calendar`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_discuss_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Calendar / Schedule employees' meetings
- Inventory of user-facing artifacts (counts): menu items 8, views 18, window actions 5, server actions 0, reports 0, mail templates 5, scheduled jobs 1, wizards 3, web routes 10
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (9): `calendar.provider.config` (Calendar Provider Configuration Wizard); `calendar.popover.delete.wizard` (Calendar Popover Delete Wizard); `calendar.alarm_manager` (Event Alarm Manager); `calendar.attendee` (Calendar Attendee Information); `calendar.event.type` (Event Meeting Type); `calendar.recurrence` (Event Recurrence Rule); `calendar.event` (Calendar Event); `calendar.filters` (Calendar Filters); `calendar.alarm` (Event Alarm)
- Objects extended from other modules (11): `mail.activity.schedule`, `mail.composer.mixin`, `discuss.channel`, `ir.http`, `mail.activity.type`, `res.users.settings`, `mail.activity`, `mail.thread`, `res.users`, `mail.activity.mixin`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `calendar.alarm_manager` ← Community: `calendar_sms`, `google_calendar`, `microsoft_calendar`; open-license custom/third-party scanned: —
- `calendar.attendee` ← Community: `google_calendar`, `microsoft_calendar`; open-license custom/third-party scanned: —
- `calendar.recurrence` ← Community: `google_calendar`, `microsoft_calendar`; open-license custom/third-party scanned: —
- `calendar.event` ← Community: `calendar_sms`, `crm`, `google_calendar`, `hr_calendar`, `hr_holidays`, `hr_recruitment`, `microsoft_calendar`; open-license custom/third-party scanned: —
- `calendar.alarm` ← Community: `calendar_sms`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.activity.schedule`, `mail.composer.mixin`, `discuss.channel`, `ir.http`, `mail.activity.type`, `res.users.settings`, `mail.activity`, `mail.thread`, `res.users`, `mail.activity.mixin`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 3 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Calendar: Event Reminder every 1 days
- Security: groups declared 0 (—); record rules 4 (of which company-scoped by text 0); access rows 15

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

