# Source Map (candidate) — `hr_work_entry`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_work_entry` |
| Display name | Work Entries |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `463195313e378a1f` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_work_entry/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr`
- Direct dependents in 300-module list (1): `hr_work_entry_holidays`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Employees / Manage work entries
- Inventory of user-facing artifacts (counts): menu items 0, views 19, window actions 4, server actions 1, reports 0, mail templates 0, scheduled jobs 1, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (4): `hr.work.entry.regeneration.wizard` (Regenerate Employee Work Entries); `hr.user.work.entry.employee` (Work Entries Employees); `hr.work.entry.type` (HR Work Entry Type); `hr.work.entry` (HR Work Entry)
- Objects extended from other modules (5): `hr.version`, `resource.calendar`, `resource.calendar.attendance`, `resource.calendar.leaves`, `hr.employee`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `hr.work.entry.type` ← Community: `hr_work_entry_holidays`; open-license custom/third-party scanned: —
- `hr.work.entry` ← Community: `hr_work_entry_holidays`, `l10n_fr_hr_work_entry_holidays`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `hr.version`, `resource.calendar`, `resource.calendar.attendance`, `resource.calendar.leaves`, `hr.employee`

## 6. Actions / states / validation / automation / security
- State fields found: `hr.work.entry` → ['draft', 'conflict', 'validated', 'cancelled']
- Validation: 3 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Generate Missing Work Entries every 1 days
- Security: groups declared 0 (—); record rules 3 (of which company-scoped by text 1); access rows 6

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

