# Source Map (candidate) — `project_timesheet_holidays`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_timesheet_holidays` |
| Display name | Timesheet when on Time Off |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `ba8c41d74eb92640` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_timesheet_holidays/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr_timesheet`, `hr_holidays`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources / Schedule timesheet when on time off
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (7): `hr.leave`, `resource.calendar.leaves`, `account.analytic.line`, `res.company`, `hr.employee`, `project.task`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.leave`, `resource.calendar.leaves`, `account.analytic.line`, `res.company`, `hr.employee`, `project.task`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 40 of 40 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: project_timesheet_holidays
Revision 19.0.post20260921 | Bridge: Timesheets (hr_timesheet) <-> Time Off (hr_holidays)

## A. Capabilities (core / optional / conditional)
- Automatically records timesheet lines for employees on approved time off and on company-wide (public) time off; project and task configured company-wide (project_timesheet_holidays/__manifest__.py:13-14). Depends on hr_timesheet and hr_holidays (:16).
- Auto-install: yes (project_timesheet_holidays/__manifest__.py:27). It is also switchable from the Timesheets settings "Time Off" option, described as generating timesheets for validated time off and public holidays (hr_timesheet/views/res_config_settings_views.xml:28-31); that option is forced off when the Timesheets module option is off (hr_timesheet/models/res_config_settings.py:42-46).
- Settings added (Internal Project, Time Off Task) shown only when the option is on (project_timesheet_holidays/views/res_config_settings_views.xml:9-21); project and task are per company (project_timesheet_holidays/models/res_company.py:10-12; models/res_config_settings.py:10-19). Project field is required in settings (models/res_config_settings.py:11).
- Conditional: nothing is generated for a company lacking both project and task (project_timesheet_holidays/models/hr_leave.py:30; models/resource_calendar_leaves.py:202), for inactive employees (models/hr_leave.py:24), or for leave types whose time type is "other" (models/hr_leave.py:30).
- Install hook: creates an "Internal" project (timesheets allowed) and a "Time Off" task for companies missing them (project_timesheet_holidays/__init__.py:7-45). New internal projects also get the task (models/res_company.py:14-29).

## B. Business objects and lifecycle
- Timesheet line (owner hr_timesheet/analytic) gains links to a time off request and to a public time off (project_timesheet_holidays/models/account_analytic.py:11-12). Time off request lists its timesheet lines (models/hr_leave.py:11); public time off lists its lines (models/resource_calendar_leaves.py:13).
- On time off validation: one timesheet line per working day, hours per the employee's schedule, name "Time Off (n/total)", assigned to company project/task/analytic account (project_timesheet_holidays/models/hr_leave.py:13-16,60-84). Flexible-hours schedules: single-day leave uses hours-per-day, half day uses half, hourly leave uses the requested span (models/hr_leave.py:40-48).
- Regeneration removes prior lines first (project_timesheet_holidays/models/hr_leave.py:63-67).
- Refusal, user cancel, forced cancel, deletion, or duration becoming zero deletes the lines; after refusal/cancel/deletion, missing public-holiday lines are re-created (project_timesheet_holidays/models/hr_leave.py:102-143).
- Public time off (no specific resource) creates lines for every employee on affected schedules, skipping days already covered by a validated personal leave and days with no work hours (project_timesheet_holidays/models/resource_calendar_leaves.py:118-184,254-258). Edit of dates/schedule deletes and regenerates, re-checking overlapping leaves; deleting a public time off regenerates overlapping personal leaves' lines (:260-288).
- New employee, re-activated employee, or schedule change: future public-holiday lines created/replaced; archiving deletes future ones (project_timesheet_holidays/models/hr_employee.py:11-45,47-73).

## C. Validations, automation, security
- Lines tied to public time off cannot be deleted or edited by normal users (project_timesheet_holidays/models/account_analytic.py:33-34,43-44).
- Lines tied to a time off request cannot be deleted or edited; users are redirected to Time Off; time off officers or the request's approver get a link to it (project_timesheet_holidays/models/account_analytic.py:35-40,45-46). Bypassed under elevated rights.
- Users cannot create timesheets on a time-off task (any task with time-off lines, or the company time-off task) (project_timesheet_holidays/models/account_analytic.py:49-52; models/project_task.py:24-27,29-42). Task timesheet list becomes read-only for such tasks (views/project_task_views.xml:12-14). Time-off tasks are excluded from the timesheet task picker and from "favorite project" suggestions (models/account_analytic.py:13,54-59).
- Access: time off managers get read-only access to analytic accounts (project_timesheet_holidays/security/ir.model.access.csv:2). Generation runs with elevated rights (models/hr_leave.py:64,69).
- Company scoping: generated line company comes from the task or project (models/hr_leave.py:83); public-time-off employees are filtered by company (models/resource_calendar_leaves.py:126); multi-company covered by tests (TEST) tests/test_timesheet_global_time_off.py:115,290.

## D. Handoffs
- hr_holidays owns time off, leave types, public holidays (resource calendar leaves); hr_timesheet/project own project, task, timesheet lines, Internal project; resource owns schedules; analytic owns the account link.
- Payroll/work entries not touched (see hr_work_entry_holidays).

## E. Configuration that changes outcomes
- Company Internal Project and Time Off Task (settings) decide where hours land; the settings help text says a project/task can also be set per time off type (project_timesheet_holidays/models/res_config_settings.py:13-19) but generation code reads only the company values (models/hr_leave.py:28): per-type override in this module: UNKNOWN — EVIDENCE INSUFFICIENT.
- Leave type "time type" other = no timesheets (models/hr_leave.py:30).
- Employee schedule (fixed vs flexible) controls hours (models/hr_leave.py:37-58).

## F. Effective extension path
- hr_timesheet, hr_holidays, project, resource (module names only).

## G. Not verified
- Demo data effect (project_timesheet_holidays/data/holiday_timesheets_demo.xml): UNKNOWN — EVIDENCE INSUFFICIENT (not opened).
- Half-day/hourly leave on fixed schedules beyond schedule-hours listing: UNKNOWN — EVIDENCE INSUFFICIENT; tests exist (TEST) tests/test_timesheet_holidays.py:459.

