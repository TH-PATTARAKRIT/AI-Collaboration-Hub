# Source Map (candidate) — `spreadsheet_dashboard_hr_timesheet`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `spreadsheet_dashboard_hr_timesheet` |
| Display name | Spreadsheet dashboard for time sheets |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `366e5b79bb805cbe` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/spreadsheet_dashboard_hr_timesheet/` |
| auto_install / application | ['hr_timesheet'] / None |

## 2. Dependencies
- Direct dependencies (manifest): `spreadsheet_dashboard`, `hr_timesheet`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Dashboard / Spreadsheet
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 8 of 9 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: spreadsheet_dashboard_hr_timesheet
Revision 19.0.post20260921 | Dashboard bridge: Spreadsheet Dashboards <-> Timesheets (hr_timesheet) | data-only module

## A. Capabilities (core / optional / conditional)
- Delivers one published dashboard named "Project" (task workload and logged hours) (spreadsheet_dashboard_hr_timesheet/data/dashboards.xml:3-9). Depends on spreadsheet_dashboard and hr_timesheet (spreadsheet_dashboard_hr_timesheet/__manifest__.py:8).
- Auto-install: when hr_timesheet is installed (spreadsheet_dashboard_hr_timesheet/__manifest__.py:13). Manifest name reads "Spreadsheet dashboard for time sheets" (:4) although the dashboard is titled Project.
- Placed in the Project dashboard group, sequence 100, restricted to timesheet approvers (spreadsheet_dashboard_hr_timesheet/data/dashboards.xml:6-7). No main data model and no sample dashboard file are declared (data file has neither entry: :3-9). No settings, models, rules or access CSV.

## B. Business objects and lifecycle
- Read-only reporting on the task analysis report (one row per task/assignee) (dashboard pivots use report.project.task.user: spreadsheet_dashboard_hr_timesheet/data/files/tasks_dashboard.json:632-800).
- Widgets: scorecards Tasks, Hours Logged, Time to Assign, Time to Close (KPI cells: tasks_dashboard.json:521-524); bar chart of task count by stage and state; pie of task count by state; leaderboards by assignee, tag, project, customer showing hours logged and task count (tasks_dashboard.json:632,666,700,734).
- No state changes; no lifecycle.

## C. Validations, automation, security
- Access: timesheet approver group only (spreadsheet_dashboard_hr_timesheet/data/dashboards.xml:7). Hours-related report field is itself restricted to the timesheet user group (hr_timesheet/report/project_report.py:10).
- Leaderboards drop rows with an empty grouping key (assignee, project, tag, customer) (tasks_dashboard.json pivots at :632-768, domains "not set" exclusion).
- Company scoping: UNKNOWN — EVIDENCE INSUFFICIENT (no explicit rule in this module).

## D. Handoffs
- project owns the task analysis report and tasks, stages, tags; hr_timesheet owns logged hours (effective hours) on tasks and timesheet approver group; spreadsheet_dashboard owns the container and the Project group.

## E. Measures and configuration
- Tasks = count of task rows; Hours logged = summed time spent on tasks; Days to assign / Days to close = averaged working days open / to close, rounded (tasks_dashboard.json:521-524, D4-D5 rounding in Data sheet). Working-day fields defined in project/report/project_report.py:25-30 (whether averaged or summed by the spreadsheet: pivot measure type UNKNOWN — EVIDENCE INSUFFICIENT).
- Hours are timesheet time, not cost or revenue; no cost/revenue basis is used by this dashboard.
- Period filter default: last 30 days (tasks_dashboard.json:818); additional filters Assignees, Project, Tags, Customer (json:~810-860). Previous period = matching prior range via "stats - previous" pivot (json:800).

## F. Effective extension path
- project, hr_timesheet, spreadsheet_dashboard (module names only). A billing-oriented timesheet dashboard is in spreadsheet_dashboard_sale_timesheet.

## G. Not verified
- Which date field the Period filter applies to (task creation vs other): UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether archived/template tasks are excluded by the report: the report exposes template flags (project/report/project_report.py:70-73) but filter in the dashboard is not confirmed: UNKNOWN — EVIDENCE INSUFFICIENT.

