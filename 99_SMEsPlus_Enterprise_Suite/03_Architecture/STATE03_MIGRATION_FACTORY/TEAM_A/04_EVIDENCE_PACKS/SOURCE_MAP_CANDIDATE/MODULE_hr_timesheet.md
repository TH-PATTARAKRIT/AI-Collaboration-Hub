# Source Map (candidate) — `hr_timesheet`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

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
- Core/optional/conditional behavior and business meaning of each capability: see section 10

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
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 89 of 89 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — hr_timesheet
Source revision: 19.0.post20260921 | Module: "Task Logs" (hr_timesheet/__manifest__.py:5), category Timesheets | depends: hr, hr_hourly_cost, analytic, project, uom (:22) | License LGPL-3 (:76)
Basis: static reading of all models (incl. 560-line analytic-line file), wizard, security, reports, portal controllers, seed data; 8 test files listed, ~20 tests read in detail. Not auto_install and not flagged as an application key; optional module installed explicitly. hr_timesheet/__manifest__.py:49-52

## A. Capabilities and optionality
- A1. Employees log time ("timesheets") against projects and tasks; each entry is an analytic line that also carries employee, department, manager, unit of measure and a cost amount. hr_timesheet/models/hr_timesheet.py:16-81,441-480
- A2. Projects can turn time tracking on/off ("Timesheets" flag, default on); tasks carry allocated hours, time spent, remaining time, progress and overtime; sub-task time rolls up. hr_timesheet/models/project_project.py:13-15,34-35; hr_timesheet/models/project_task.py:34-44,83-143
- A3. Time can be encoded in hours/minutes or in days/half-days, chosen per company; project time unit is a separate company setting (default hour for both). hr_timesheet/models/res_company.py:12-25; hr_timesheet/models/res_config_settings.py:20-35
- A4. Analysis: timesheet analysis report (one row per timesheet with project, department, manager, amount, hours), task analysis columns for planned/spent/remaining time, project panel button "Timesheets" with spent/allocated and an "Extra Time" alert. hr_timesheet/report/timesheets_analysis_report.py:8-74; hr_timesheet/report/project_report.py:6-31; hr_timesheet/models/project_project.py:218-284
- A5. Portal/customer view: customers see timesheets of their tasks/projects under "my timesheets" and on task pages; project-sharing collaborators can log time when rules are enabled. hr_timesheet/controllers/portal.py:69; hr_timesheet/controllers/project.py:37-46; hr_timesheet/models/project_collaborator.py:10-21; hr_timesheet/security/hr_timesheet_security.xml:33-48
- A6. Internal project: each company gets an "Internal" project with tasks "Training" and "Meeting", used as the default for entries without an explicit project and by the time-off bridge. hr_timesheet/models/res_company.py:26-30,37-66; hr_timesheet/models/hr_timesheet.py:29-36
- A7. Quick task creation syntax: "30h" in a new task title sets allocated hours. hr_timesheet/models/project_task.py:47-54,145-161 (TEST: tests/test_project_task_quick_create.py:14-39)
- A8. Settings for approver/employee reminder emails exist as fields and switches; implementing code not found in this module. hr_timesheet/models/res_config_settings.py:12-13; hr_timesheet/views/res_config_settings_views.xml:21-26 (both use upgrade-style widgets). UNKNOWN — EVIDENCE INSUFFICIENT for any reminder job.
- A9. Conditional: optional link to time off via module_project_timesheet_holidays setting (turned off automatically when timesheets module is off). hr_timesheet/models/res_config_settings.py:10-11,42-46; hr_timesheet/views/res_config_settings_views.xml:31

## B. Business objects, relationships, lifecycle
- B1. Timesheet = account.analytic.line (owner analytic) extended with task, parent task, project, employee, department, manager; a line is a timesheet when it has a project. hr_timesheet/models/hr_timesheet.py:62-79; hr_timesheet/report/timesheets_analysis_report.py:70
- B2. Project (owner project) links to one analytic account (mandatory if timesheets allowed) and lists its timesheets; task (owner project) lists its timesheets. hr_timesheet/models/project_project.py:16-25,98-106; hr_timesheet/models/project_task.py:45
- B3. Analytic account auto-creation: a project that allows timesheets and has no account gets one (name, company, partner from the project); also when timesheets are switched on later or a template is converted into a regular project. hr_timesheet/models/project_project.py:131-148,198-212,292-295; project/models/project_project.py:1179-1192 (TEST: tests/test_timesheet.py:200-244; tests/test_project_template.py:7-56 templates get none until converted/instantiated)
- B4. Creating a timesheet: project taken from task if missing; company taken from task, else project, else supplied; unit of measure defaults to company project time unit; empty description becomes "/"; project's analytic accounts (all plans) copied onto the line. hr_timesheet/models/hr_timesheet.py:245-268,423-439 (TEST: tests/test_timesheet.py:132-176,561-585,606-628 account, employee, partner and unit assertions)
- B5. Employee resolution: supplied employee is used if active in the selected companies; otherwise the user's employee in the entry's company, or the user's only employee; anything else is refused. hr_timesheet/models/hr_timesheet.py:278-337 (TEST: tests/test_timesheet.py:433-482,586-605,1039-1049)
- B6. Cost/amount: amount = minus (hours x employee hourly cost), converted from the employee's currency to the analytic account currency at the entry date; recomputed when hours, employee or account change. hr_timesheet/models/hr_timesheet.py:459-479,503-505 (TEST: tests/test_timesheet.py:324-359 hours 2 gave -10 and -12 with hourly costs 5 and 6)
- B7. Entry partner defaults to the task customer, else the project customer. hr_timesheet/models/hr_timesheet.py:131-136 (TEST: tests/test_timesheet.py:170-176)
- B8. Moving an entry to another project clears its task; changing a task's project moves entries along (project recomputed from task). hr_timesheet/models/hr_timesheet.py:138-160 (TEST: tests/test_timesheet.py:246-313,382-424,1091+)
- B9. Task progress = (own + sub-task hours) / allocated; overtime = excess; remaining = allocated - own - sub-task hours (0 if nothing allocated). hr_timesheet/models/project_task.py:94-133 (TEST: tests/test_timesheet.py:708-735)
- B10. Project time spent / remaining / overtime flag computed from all its entries; total displayed in the company encoding unit. hr_timesheet/models/project_project.py:68-79,108-129 (TEST: tests/test_project_project.py:66-93; tests/test_timesheet.py:638-678 unit switch hours to days)
- B11. Project updates snapshot allocated and spent time with the unit at that time. hr_timesheet/models/project_update.py:26-38 (TEST: tests/test_timesheet.py:825-866)
- B12. Favorite project default: last 5 entries of the employee decide the most frequent project; otherwise the company internal project. hr_timesheet/models/hr_timesheet.py:29-48 (TEST: tests/test_timesheet.py:314-323)
- B13. No approval or validation state on entries in this module; "readonly" hook exists for other modules to lock entries. hr_timesheet/models/hr_timesheet.py:112-125

## C. Validations, security, multi-company
- C1. Timesheets cannot be created on a private task (task without project); a task with entries cannot become private. hr_timesheet/models/hr_timesheet.py:250-252,370-371; hr_timesheet/models/project_task.py:60-64 (TEST: tests/test_timesheet.py:691-706)
- C2. Timesheet company checks: project, task and analytic accounts of a timesheet must all belong to one company; the analytic account must be active; a mandatory analytic plan (business domain "Timesheet") must be set on the project. hr_timesheet/models/hr_timesheet.py:428-435,462-471 (TEST: tests/test_timesheet.py:799-823)
- C3. Archived employees cannot be put on new or existing entries. hr_timesheet/models/hr_timesheet.py:380-383 (TEST: tests/test_timesheet.py:586-605)
- C4. Project with timesheets on needs an analytic account (templates exempt). hr_timesheet/models/project_project.py:98-106
- C5. Deletion guards: project or task holding entries cannot be deleted (redirects to the entries); users lacking read access on those entries get a plain refusal; employee deletion offers archive/termination when entries exist. hr_timesheet/models/project_project.py:165-181; hr_timesheet/models/project_task.py:242-274; hr_timesheet/models/hr_employee.py:52-68; hr_timesheet/wizard/hr_employee_delete_wizard.py:45-63 (TEST: tests/test_employee_delete_wizard.py:9-26; tests/test_timesheet.py:679-690)
- C6. Groups: "User: own timesheets only" (implies internal user), "User: all timesheets" (approver), "Administrator" (implies approver and HR officer); project managers imply approver. hr_timesheet/security/hr_timesheet_security.xml:10-31,84-86
- C7. Record rules on timesheets: own-only for basic users (project visible to employees/portal, or user is follower/customer), all visible-project entries for approvers, all for administrators/project managers; portal rule (inactive until project sharing is used) limited to collaborators. hr_timesheet/security/hr_timesheet_security.xml:33-82. Write/create check: non-approvers may only touch their own entries. hr_timesheet/models/hr_timesheet.py:207-213 (TEST: tests/test_timesheet.py:177-199)
- C8. Access lines: timesheet users full rights on analytic lines, read/write on analytic accounts, read on projects and units; all internal users read the analysis report (row-limited by rules); report rules add company filter. hr_timesheet/security/ir.model.access.csv:2-8; hr_timesheet/security/hr_timesheet_security.xml:88-131
- C9. Hourly cost field is visible only to HR officers, yet cost amounts are computed with elevated rights when entries are saved. hr_hourly_cost/models/hr_employee.py:9-10; hr_timesheet/models/hr_timesheet.py:443,458
- C10. Multi-company: entry company follows task/project; employee lookup respects selected companies; display names add company when several companies are selected; internal project must belong to its own company. hr_timesheet/models/hr_timesheet.py:256-257; hr_timesheet/models/hr_employee.py:32-50; hr_timesheet/models/res_company.py:32-35 (TEST: tests/test_timesheet.py:483-510 company on entry is current company not employee's; tests/test_project_sharing.py:10-40 portal access across companies)

## D. Handoffs (which module owns what)
- D1. Cost accounting/analytic ledger: analytic (analytic lines, plans, accounts, applicability). This module supplies employee cost as a negative analytic amount per project account. hr_timesheet/models/hr_timesheet.py:473-479
- D2. Hourly cost master data: hr_hourly_cost. Employees, departments, calendars (work-day check for calendar entry): hr / resource. hr_timesheet/models/hr_timesheet.py:238-244
- D3. Billing time to customers (revenue, sales order line, invoice policy): NOT here; sale_timesheet (F2). UNKNOWN — EVIDENCE INSUFFICIENT for invoicing rules (not read).
- D4. Project profitability panel: project_account and sale_project; this module only provides cost lines. Inventory handoff: none.
- D5. Time off becoming timesheets: project_timesheet_holidays; attendance-based checks: hr_timesheet_attendance; website portal: website_timesheet (F2).

## E. Configuration/defaults that change outcomes
- E1. Company encoding unit (hours vs days) changes displayed totals, widgets and project panels; stored entries keep the original unit and are converted for display (TEST: tests/test_timesheet.py:638-678). hr_timesheet/models/project_project.py:108-129
- E2. Employee hourly cost (default 0) decides cost amount; without it, entries carry amount 0. hr_hourly_cost/models/hr_employee.py:9-10; hr_timesheet/models/hr_timesheet.py:503-505
- E3. Project flag "Timesheets" default true; switching it on creates an account. hr_timesheet/models/project_project.py:13-15,142-148
- E4. Project privacy setting (employees/portal vs invited only) alters who sees timesheets (C7). hr_timesheet/security/hr_timesheet_security.xml:50-75
- E5. Analytic plan applicability for "Timesheet" (optional/mandatory). hr_timesheet/models/analytic_applicability.py:10-15
- E6. Hour-to-day conversions use the unit-of-measure table and round to 2 decimals. hr_timesheet/models/hr_timesheet.py:494-501

## F. Effective extension path (grep of _inherit)
- F1. This module extends: account.analytic.line, account.analytic.applicability, hr.employee, hr.employee.public, project.project, project.task, project.update, project.collaborator, res.company, res.config.settings, uom.uom, ir.http, ir.ui.menu, report.project.task.user; defines timesheets.analysis.report, hr.employee.delete.wizard, account.analytic.line.calendar.employee. hr_timesheet/models/*.py; hr_timesheet/report/*.py; hr_timesheet/wizard/hr_employee_delete_wizard.py:7
- F2. Modules depending on hr_timesheet: hr_timesheet_attendance, project_timesheet_holidays, sale_timesheet, spreadsheet_dashboard_hr_timesheet, website_timesheet. Additional modules extending account.analytic.line (grep): account, mrp_account, project_stock_account, project_timesheet_holidays, sale, sale_timesheet, website_timesheet.

## G. Not verified
- G1. UNKNOWN — EVIDENCE INSUFFICIENT: invoicing/revenue from timesheets (sale_timesheet, not read).
- G2. UNKNOWN — EVIDENCE INSUFFICIENT: reminder emails (A8) and the digest tip effect beyond the seed record (hr_timesheet/data/digest_data.xml:4-15).
- G3. UNKNOWN — EVIDENCE INSUFFICIENT: enforced rate for entries whose analytic account uses a different currency than the employee, beyond the conversion at B6 (single-currency tests only).
- G4. UNKNOWN — EVIDENCE INSUFFICIENT: front-end web behaviour (timer, hotkeys, calendar view) implemented in static scripts (not read).

