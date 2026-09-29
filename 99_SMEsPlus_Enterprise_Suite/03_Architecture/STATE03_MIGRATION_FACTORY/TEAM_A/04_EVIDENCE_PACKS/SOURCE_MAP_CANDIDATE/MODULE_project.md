# Source Map (candidate) — `project`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project` |
| Display name | Project |
| Manifest version | 1.4 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `7d722c5109276ff8` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `analytic`, `base_setup`, `mail`, `portal`, `rating`, `resource`, `web`, `web_tour`, `digest`
- Direct dependents in 300-module list (9): `hr_timesheet`, `project_account`, `project_hr_skills`, `project_mail_plugin`, `project_mrp`, `project_sms`, `project_stock`, `project_todo`, `website_project`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (1): `purchase_request` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / Organize and plan your projects
- Inventory of user-facing artifacts (counts): menu items 19, views 112, window actions 39, server actions 5, reports 0, mail templates 3, scheduled jobs 1, wizards 9, web routes 9
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (20): `project.template.create.wizard` (Project Template create Wizard); `project.template.role.to.users.map` (Project role to users mapping); `project.share.collaborator.wizard` (Project Sharing Collaborator Wizard); `project.project.stage.delete.wizard` (Project Stage Delete Wizard); `project.share.wizard` (Project Sharing); `task.share.wizard` (Task Sharing); `project.task.type.delete.wizard` (Project Task Stage Delete Wizard); `project.update` (Project Update); `project.collaborator` (Collaborators in project shared); `project.project.stage` (Project Stage); `project.task.recurrence` (Task Recurrence); `project.task.stage.personal` (Personal Task Stage); `project.task.type` (Task Stage); `project.tags` (Project Tags); `project.task` (Task); `project.project` (Project); `project.role` (Project Role); `project.milestone` (Project Milestone); `project.task.burndown.chart.report` (Burndown Chart); `report.project.task.user` (Tasks Analysis)
- Objects extended from other modules (19): `portal.share`, `digest.digest`, `mail.thread.cc`, `mail.activity.mixin`, `account.analytic.account`, `res.users.settings`, `ir.ui.menu`, `res.users`, `portal.mixin`, `rating.mixin`, `mail.tracking.duration.mixin`, `html.field.history.mixin`, `res.config.settings`, `mail.alias.mixin`, `rating.parent.mixin`, `analytic.plan.fields.mixin`, `mail.message`, `res.partner`, `mail.thread`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `project.template.create.wizard` ← Community: `sale_project`; open-license custom/third-party scanned: —
- `project.update` ← Community: `hr_timesheet`, `sale_project`; open-license custom/third-party scanned: —
- `project.collaborator` ← Community: `hr_timesheet`; open-license custom/third-party scanned: —
- `project.project.stage` ← Community: `project_sms`; open-license custom/third-party scanned: —
- `project.task.recurrence` ← Community: `sale_project`; open-license custom/third-party scanned: —
- `project.task.type` ← Community: `project_sms`, `sale_project`; open-license custom/third-party scanned: —
- `project.task` ← Community: `hr_timesheet`, `project_hr_skills`, `project_sms`, `project_timesheet_holidays`, `project_todo`, `sale_project`, `sale_timesheet`, `website_project`; open-license custom/third-party scanned: —
- `project.project` ← Community: `hr_timesheet`, `project_account`, `project_hr_expense`, `project_mrp`, `project_mrp_account`, `project_purchase`, `project_sale_expense`, `project_sms`, `project_stock`, `project_stock_account` … (+3); open-license custom/third-party scanned: —
- `project.milestone` ← Community: `sale_project`; open-license custom/third-party scanned: —
- `report.project.task.user` ← Community: `hr_timesheet`, `project_hr_skills`, `sale_project`, `sale_timesheet`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `portal.share`, `digest.digest`, `mail.thread.cc`, `mail.activity.mixin`, `account.analytic.account`, `res.users.settings`, `ir.ui.menu`, `res.users`, `portal.mixin`, `rating.mixin`, `mail.tracking.duration.mixin`, `html.field.history.mixin`, `res.config.settings`, `mail.alias.mixin`, `rating.parent.mixin`, `analytic.plan.fields.mixin`, `mail.message`, `res.partner`, `mail.thread`

## 6. Actions / states / validation / automation / security
- State fields found: `project.update` → ['on_track', 'at_risk', 'off_track', 'on_hold', 'done']; `project.task.burndown.chart.report` → ['01_in_progress', '1_done', '04_waiting_normal', '03_approved', '1_canceled', '02_changes_requested']; `report.project.task.user` → ['01_in_progress', '1_done', '04_waiting_normal', '03_approved', '1_canceled', '02_changes_requested']
- Validation: 11 declarative constraint method(s), 6 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Project Stage: Send rating every ? days
- Security: groups declared 9 (`group_project_user`, `group_project_manager`, `group_project_stages`, `group_project_recurring_tasks`, `group_project_task_dependencies`, `group_project_milestone` … (+3)); record rules 31 (of which company-scoped by text 6); access rows 55

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

