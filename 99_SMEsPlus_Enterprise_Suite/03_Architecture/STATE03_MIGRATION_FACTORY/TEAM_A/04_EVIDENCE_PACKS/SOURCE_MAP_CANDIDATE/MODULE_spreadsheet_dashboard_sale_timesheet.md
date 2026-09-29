# Source Map (candidate) — `spreadsheet_dashboard_sale_timesheet`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `spreadsheet_dashboard_sale_timesheet` |
| Display name | Spreadsheet dashboard for time sheets |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `ddf4123cbf4ca129` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/spreadsheet_dashboard_sale_timesheet/` |
| auto_install / application | ['sale_timesheet'] / None |

## 2. Dependencies
- Direct dependencies (manifest): `spreadsheet_dashboard`, `sale_timesheet`
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 7 of 8 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: spreadsheet_dashboard_sale_timesheet
Revision 19.0.post20260921 | Dashboard bridge: Spreadsheet Dashboards <-> Billable Timesheets (sale_timesheet) | data-only module

## A. Capabilities (core / optional / conditional)
- Delivers one published dashboard "Timesheets" focused on billable versus non-billable hours (spreadsheet_dashboard_sale_timesheet/data/dashboards.xml:3-11). Depends on spreadsheet_dashboard and sale_timesheet (spreadsheet_dashboard_sale_timesheet/__manifest__.py:8). Manifest name duplicates that of the hr_timesheet dashboard module ("Spreadsheet dashboard for time sheets": :4).
- Auto-install: when sale_timesheet is installed (spreadsheet_dashboard_sale_timesheet/__manifest__.py:13). No settings, models, rules or access CSV.
- Project dashboard group, sequence 200, restricted to timesheet approvers (spreadsheet_dashboard_sale_timesheet/data/dashboards.xml:8-9). Main data models: analytic (timesheet) lines, projects, sales orders; sample dashboard registered (:6-7).

## B. Business objects and lifecycle
- Read-only. Sheets Dashboard and Data; pivots by project, task, department, employee on the timesheet analysis report, and two summary pivots by billable type on timesheet lines (spreadsheet_dashboard_sale_timesheet/data/files/timesheet_dashboard.json:523,574,623,672,700,724).
- Widgets: scorecards Billable Hours, Non-billable Hours, Billable Rate; weekly line chart of billable time; "Top Departments" carousel; leaderboards of project, task, department, employee (json:135-179 titles; KPI cells json:391-397).
- No state changes.

## C. Validations, automation, security
- Access: timesheet approver group only (spreadsheet_dashboard_sale_timesheet/data/dashboards.xml:9).
- Leaderboards include only timesheet lines that have a project, and drop rows without task / department / employee for their pivot (timesheet_dashboard.json:523-700, domains).
- Company scoping: UNKNOWN — EVIDENCE INSUFFICIENT (no explicit rule in this module).

## D. Handoffs
- sale_timesheet owns the billable type on timesheet lines and the analysis report with billable time; sale owns order lines that define billability; hr_timesheet/project own timesheets, projects, tasks; spreadsheet_dashboard owns the container.

## E. Measures and revenue basis (business level)
- Hours-based only: no cost or revenue amounts are shown. Billable hours = fixed-price billed hours + manually billed hours + billed-on-timesheets hours (KPI sum: timesheet_dashboard.json:391-394). Non-billable hours = hours with billable type "non-billable" (json:395). Grand total = all hours on timesheets with a project (json:396). Billable rate = Billable / Grand total (json:397).
- The billed-type categories come from sale_timesheet: a timesheet with no sales order item is non-billable (or "billed manually" when the project bills manually); one on a service product billed on order counts as fixed price; on delivery billed by timesheet counts as billed on timesheets; milestone-billed lines have their own type and are not in the dashboard sum (sale_timesheet/models/hr_timesheet.py:9-19, 54-69; dashboard sum omits milestones type: timesheet_dashboard.json:391-394).
- Weekly chart and carousels use the analysis report's "billable time": hours on lines linked to a sales order, whatever type (sale_timesheet/report/timesheets_analysis_report.py:46). This differs slightly from the KPI definition above (milestone and other order-linked types count in the chart); consequence: UNKNOWN — EVIDENCE INSUFFICIENT.
- Default period: last 30 days (timesheet_dashboard.json:740). Filters: Period, Project, Task, Department, Employee (json:~740-780). Fixed anchor date in the summary pivot context (2022-09-12) is a grid setting: effect UNKNOWN — EVIDENCE INSUFFICIENT (timesheet_dashboard.json:700-724).

## F. Effective extension path
- sale_timesheet, hr_timesheet, project, sale, spreadsheet_dashboard (module names only). Task-centric sibling: spreadsheet_dashboard_hr_timesheet.

## G. Not verified
- Unit of measure (hours vs days) when timesheets are encoded in days: UNKNOWN — EVIDENCE INSUFFICIENT.
- Inclusion of billed-on-milestone and "timesheet revenues" types in headline figures: UNKNOWN — EVIDENCE INSUFFICIENT.

