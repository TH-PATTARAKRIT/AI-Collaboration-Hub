# Source Map (candidate) — `hr_timesheet`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_timesheet` |
| Display name | Task Logs |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `9983572e14932259` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_timesheet/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr`, `hr_hourly_cost`, `analytic`, `project`, `uom`
- Direct dependents in 300-module list (5): `hr_timesheet_attendance`, `project_timesheet_holidays`, `sale_timesheet`, `spreadsheet_dashboard_hr_timesheet`, `website_timesheet`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (1): `scgl_timesheet_grid` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Services/Timesheets / Track employee time on tasks
- Inventory of user-facing artifacts (counts): menu items 11, views 54, window actions 12, server actions 1, reports 4, mail templates 0, scheduled jobs 0, wizards 2, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `hr.employee.delete.wizard` (Employee Delete Wizard); `account.analytic.line.calendar.employee` (Personal Filters on Employees for the Calendar view); `timesheets.analysis.report` (Timesheets Analysis Report)
- Objects extended from other modules (15): `account.analytic.line`, `hr.employee.public`, `ir.http`, `project.update`, `project.collaborator`, `ir.ui.menu`, `res.company`, `hr.employee`, `uom.uom`, `project.task`, `res.config.settings`, `project.project`, `account.analytic.applicability`, `report.project.task.user`, `hr.manager.department.report`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `timesheets.analysis.report` ← Community: `sale_timesheet`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `account.analytic.line`, `hr.employee.public`, `ir.http`, `project.update`, `project.collaborator`, `ir.ui.menu`, `res.company`, `hr.employee`, `uom.uom`, `project.task`, `res.config.settings`, `project.project`, `account.analytic.applicability`, `report.project.task.user`, `hr.manager.department.report`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 3 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 5 (`group_hr_timesheet_user`, `group_hr_timesheet_approver`, `group_timesheet_manager`, `project.group_project_manager`, `base.default_user_group`); record rules 9 (of which company-scoped by text 1); access rows 7

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

