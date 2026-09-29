# Source Map (candidate) — `hr_holidays`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_holidays` |
| Display name | Time Off |
| Manifest version | 1.6 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e91f5a076d268b83` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_holidays/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `hr`, `calendar`, `resource`
- Direct dependents in 300-module list (5): `hr_holidays_attendance`, `hr_holidays_homeworking`, `hr_presence`, `hr_work_entry_holidays`, `project_timesheet_holidays`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (3): `l10n_fr_hr_holidays`, `l10n_in_hr_holidays`, `test_discuss_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Time Off / Allocate time off and follow leave requests
- Inventory of user-facing artifacts (counts): menu items 19, views 70, window actions 24, server actions 1, reports 1, mail templates 0, scheduled jobs 2, wizards 5, web routes 5
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (14): `hr.leave.generate.multi.wizard` (Generate time off for multiple employees); `hr.holidays.summary.employee` (HR Time Off Summary Report By Employee); `hr.leave.allocation.generate.multi.wizard` (Generate time off allocations for multiple employees); `hr.holidays.cancel.leave` (Cancel Time Off Wizard); `hr.leave` (Time Off); `hr.leave.accrual.plan` (Accrual Plan); `hr.leave.accrual.level` (Accrual Plan Level); `hr.leave.allocation` (Time Off Allocation); `hr.leave.type` (Time Off Type); `hr.leave.mandatory.day` (Mandatory Day); `hr.leave.report.calendar` (Time Off Calendar); `hr.leave.report` (Time Off Summary / Report); `hr.leave.employee.type.report` (Time Off Summary / Report); `report.hr_holidays.report_holidayssummary` (Holidays Summary Report)
- Objects extended from other modules (19): `hr.departure.wizard`, `hr.mixin`, `hr.version`, `mail.thread.main.attachment`, `mail.activity.mixin`, `hr.employee.public`, `mail.activity.type`, `mail.message.subtype`, `hr.department`, `resource.calendar.leaves`, `resource.calendar`, `resource.resource`, `res.company`, `hr.employee`, `mail.thread`, `calendar.event`, `res.users`, `res.partner`, `hr.manager.department.report`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `hr.leave` ← Community: `hr_holidays_attendance`, `hr_work_entry_holidays`, `l10n_fr_hr_holidays`, `l10n_in_hr_holidays`, `project_timesheet_holidays`; open-license custom/third-party scanned: —
- `hr.leave.accrual.level` ← Community: `hr_holidays_attendance`; open-license custom/third-party scanned: —
- `hr.leave.allocation` ← Community: `hr_holidays_attendance`; open-license custom/third-party scanned: —
- `hr.leave.type` ← Community: `hr_holidays_attendance`, `hr_work_entry_holidays`, `l10n_in_hr_holidays`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `hr.departure.wizard`, `hr.mixin`, `hr.version`, `mail.thread.main.attachment`, `mail.activity.mixin`, `hr.employee.public`, `mail.activity.type`, `mail.message.subtype`, `hr.department`, `resource.calendar.leaves`, `resource.calendar`, `resource.resource`, `res.company`, `hr.employee`, `mail.thread`, `calendar.event`, `res.users`, `res.partner`, `hr.manager.department.report`

## 6. Actions / states / validation / automation / security
- State fields found: `hr.leave` → ['confirm', 'refuse', 'validate1', 'validate', 'cancel']; `hr.leave.allocation` → ['confirm', 'refuse', 'validate1', 'validate']; `hr.leave.report.calendar` → ['cancel', 'confirm', 'refuse', 'validate1', 'validate']; `hr.leave.report` → ['cancel', 'confirm', 'refuse', 'validate1', 'validate']; `hr.leave.employee.type.report` → ['cancel', 'confirm', 'refuse', 'validate1', 'validate']
- Validation: 15 declarative constraint method(s), 11 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Accrual Time Off: Updates the number of time off every 1 days; Time Off: Cancel invalid leaves every 1 days
- Security: groups declared 4 (`group_hr_holidays_responsible`, `group_hr_holidays_user`, `group_hr_holidays_manager`, `base.default_user_group`); record rules 26 (of which company-scoped by text 7); access rows 27

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

