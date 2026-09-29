# Source Map (candidate) — `hr`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr` |
| Display name | Employees |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `bf7754f632dd6a72` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`, `digest`, `phone_validation`, `resource_mail`, `web`
- Direct dependents in 300-module list (17): `hr_attendance`, `hr_calendar`, `hr_expense`, `hr_fleet`, `hr_gamification`, `hr_holidays`, `hr_homeworking`, `hr_hourly_cost`, `hr_livechat`, `hr_maintenance`, `hr_org_chart`, `hr_presence` … (+5)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `pos_hr`
- Custom / third-party modules that declare a dependency (name — license only) (11): `purchase_request_level_approve` — LGPL-3, `product_brand_sale` — AGPL-3, `19_contact_reference_sequence` — OPL-1, `purchase_request_level_approve_po` — LGPL-3, `19_bhpro_master_data` — OPL-1, `multi_level_approval_hr` — OPL-1, `base_location` — AGPL-3, `sale_order_level_approve` — LGPL-3, `purchase_request` — LGPL-3, `product_stock_equipment` — no-license, `contact_reference_sequence` — OPL-1

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Employees / Centralize employee information
- Inventory of user-facing artifacts (counts): menu items 18, views 56, window actions 20, server actions 3, reports 1, mail templates 0, scheduled jobs 2, wizards 6, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (15): `hr.version.wizard` (Contract Template Wizard); `hr.departure.wizard` (Departure Wizard); `hr.bank.account.allocation.wizard.line` (Bank Account Allocation Line (Wizard)); `hr.bank.account.allocation.wizard` (Bank Account Allocation Wizard); `hr.departure.reason` (Departure Reason); `hr.contract.type` (Contract Type); `hr.version` (Version); `hr.employee.public` (Public Employee); `hr.work.location` (Work Location); `hr.employee.category` (Employee Category); `hr.department` (Department); `hr.job` (Job Position); `hr.payroll.structure.type` (Salary Structure Type); `hr.employee` (Employee); `hr.manager.department.report` (Hr Manager Department Report)
- Objects extended from other modules (20): `mail.activity.schedule`, `discuss.channel`, `mail.thread`, `mail.activity.mixin`, `mail.activity.plan`, `resource.calendar`, `base`, `mail.activity.plan.template`, `resource.calendar.leaves`, `resource.resource`, `ir.ui.menu`, `res.partner.bank`, `res.company`, `mail.thread.main.attachment`, `resource.mixin`, `avatar.mixin`, `mail.alias`, `res.users`, `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `hr.departure.wizard` ← Community: `hr_fleet`, `hr_holidays`, `hr_maintenance`; open-license custom/third-party scanned: —
- `hr.version` ← Community: `hr_attendance`, `hr_holidays`, `hr_work_entry`, `hr_work_entry_holidays`, `l10n_fr_hr_work_entry_holidays`; open-license custom/third-party scanned: —
- `hr.employee.public` ← Community: `hr_attendance`, `hr_expense`, `hr_fleet`, `hr_gamification`, `hr_holidays`, `hr_homeworking`, `hr_maintenance`, `hr_org_chart`, `hr_presence`, `hr_skills` … (+2); open-license custom/third-party scanned: `base_location`, `purchase_request`, `purchase_request_level_approve`
- `hr.work.location` ← Community: `hr_homeworking`; open-license custom/third-party scanned: —
- `hr.department` ← Community: `hr_expense`, `hr_holidays`, `hr_recruitment`, `website_hr_recruitment`; open-license custom/third-party scanned: —
- `hr.job` ← Community: `hr_recruitment`, `hr_recruitment_skills`, `hr_recruitment_survey`, `hr_skills`, `website_hr_recruitment`; open-license custom/third-party scanned: —
- `hr.employee` ← Community: `hr_attendance`, `hr_expense`, `hr_fleet`, `hr_gamification`, `hr_holidays`, `hr_holidays_attendance`, `hr_holidays_homeworking`, `hr_homeworking`, `hr_homeworking_calendar`, `hr_hourly_cost` … (+12); open-license custom/third-party scanned: `base_location`, `product_brand_sale`, `purchase_request`, `purchase_request_level_approve`, `scgl_advance_expense_request`, `scgl_timesheet_grid`, `smesplus_advance_expense_request`
- `hr.manager.department.report` ← Community: `hr_holidays`, `hr_timesheet`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.activity.schedule`, `discuss.channel`, `mail.thread`, `mail.activity.mixin`, `mail.activity.plan`, `resource.calendar`, `base`, `mail.activity.plan.template`, `resource.calendar.leaves`, `resource.resource`, `ir.ui.menu`, `res.partner.bank`, `res.company`, `mail.thread.main.attachment`, `resource.mixin`, `avatar.mixin`, `mail.alias`, `res.users`, `res.config.settings`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 9 declarative constraint method(s), 6 database-level uniqueness/check declaration(s) (declared in code)
- Automation: HR Employee: Notify Expiring Contract or Work Permit every 1 days; HR Employee: Update Current Version every 1 days
- Security: groups declared 3 (`group_hr_user`, `group_hr_manager`, `base.default_user_group`); record rules 13 (of which company-scoped by text 5); access rows 26

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

