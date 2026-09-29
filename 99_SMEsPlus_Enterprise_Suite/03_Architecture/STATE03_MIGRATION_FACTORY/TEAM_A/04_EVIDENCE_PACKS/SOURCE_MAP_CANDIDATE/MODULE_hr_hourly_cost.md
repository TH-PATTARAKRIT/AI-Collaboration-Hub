# Source Map (candidate) — `hr_hourly_cost`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_hourly_cost` |
| Display name | Employee Hourly Wage |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c181cea682f731d5` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_hourly_cost/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr`
- Direct dependents in 300-module list (1): `hr_timesheet`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Employee Hourly Cost / Employee Hourly Wage
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `hr.employee`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.employee`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 30 of 31 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_hourly_cost (Employee Hourly Wage)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_hourly_cost.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests (tests of consuming modules are labelled as such).

## A. Capabilities / functions
- Tiny foundation module: gives every employee one "Hourly Cost" amount so that other modules can value time; the manifest describes it as a wage "to be used by other modules" (hr_hourly_cost/__manifest__.py:9). Depends only on the base HR module (hr_hourly_cost/__manifest__.py:13).
- Core (there is no settings toggle, no application flag, no auto_install): it is installed either explicitly or because a dependent module pulls it in. The Timesheets module lists it as a hard dependency (hr_timesheet/__manifest__.py:22), so anyone installing timesheets gets it.
- Adds a single money field on the employee, restricted to HR officers, default zero, change-tracked in chatter (hr_hourly_cost/models/hr_employee.py:9-10).
- Adds the field to the employee form in the "Application Settings" block; the module un-hides that otherwise hidden block (hr/views/hr_employee_views.xml:399 hides it; hr_hourly_cost/views/hr_employee_views.xml:9-18 reveals it and places the field).
- Demo data (demo mode only) assigns sample costs to demo employees (hr_hourly_cost/data/hr_hourly_cost_demo.xml:1-83, manifest demo entry hr_hourly_cost/__manifest__.py:17-19). Not present in production installs.

## B. Business objects, relationships, lifecycle
- One object touched: Employee. The cost is a property of the employee record itself, not of the versioned employment/contract record (field sits on the employee model: hr_hourly_cost/models/hr_employee.py:7). Consequence: there is one current value per employee; no built-in effective-dated history of the rate beyond chatter tracking (hr_hourly_cost/models/hr_employee.py:10). Whether some other module keeps rate history: UNKNOWN — EVIDENCE INSUFFICIENT.
- Amount is denominated in the employee's company currency, which is a read-only mirror of the company currency (hr/models/hr_employee.py:217; currency reference hr_hourly_cost/models/hr_employee.py:9).
- No states / workflow of its own.

## C. Validations, automation, security, multi-company
- No constraints, cron jobs, or automated actions in this module (skeleton: constrains [], crons []).
- Security: the field is visible/editable only to the HR Officer group ("Officer: Manage all employees") (hr_hourly_cost/models/hr_employee.py:10; group defined hr/security/hr_security.xml:10-11). Users without that group cannot read it through the model directly; consumers that read it with elevated rights are covered in D.
- Module ships no ACL file and no record rules; employee access and company scoping are owned by the hr module (hr_hourly_cost skeleton: access [], rules []). Company scoping of the currency follows the employee's company (hr/models/hr_employee.py:217).

## D. Accounting / payroll / analytic handoffs (owner of each)
- Timesheets (hr_timesheet) is the main consumer. When a timesheet line is created, or when its hours, employee or analytic account change, the line's analytic "amount" is set to minus hours x employee hourly cost, converted from the employee currency to the analytic account (or line) currency at the line date (hr_timesheet/models/hr_timesheet.py:459-478; cost source hr_timesheet/models/hr_timesheet.py:503-505). Cost lookup is done under elevated rights so ordinary timesheet users still get a costed line (hr_timesheet/models/hr_timesheet.py:443).
- (TEST, consumer module) A one-hour line at cost 10 gets amount -10; splitting the line 50/50 across two analytic accounts gives -5 each (hr_timesheet/tests/test_timesheet.py:1022-1034). Recompute on multi-line hour changes is also exercised (hr_timesheet/tests/test_timesheet.py:324-328).
- Timesheet posting does not create journal entries here; the cost lands only as an analytic line (accounting-side analytic ownership: analytic module; project profitability reads it).
- Sales-timesheet (sale_timesheet) refines it: for projects priced by employee rate, the cost on a line comes from the project's employee-to-sale-item mapping row instead of the raw employee cost (sale_timesheet/models/hr_timesheet.py:194-199). The mapping row copies the employee hourly cost by default and keeps a manual override flag when someone edits it (sale_timesheet/models/project_sale_line_employee_map.py:77-82, 125-126).
- (TEST, consumer module) Project profitability expectations are built from employee hourly cost, including a fractional rate for a foreign-company employee (sale_timesheet/tests/test_project_profitability.py:148, 189). Margin reporting on sale lines uses it too (TEST: sale_timesheet_margin/tests/test_sale_timesheet_margin.py:52).
- Attendance-vs-timesheet reporting (hr_timesheet_attendance) multiplies attendance and timesheet hours by the employee hourly cost to show cost and cost difference (hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:30-40).
- Payroll: this module has no link to payroll; payroll/salary rules are outside Community HR here. Any relation to real wages: UNKNOWN — EVIDENCE INSUFFICIENT (the cost is an independently maintained figure, not derived from a contract wage in this module).

## E. Configuration / defaults that change outcomes
- Default hourly cost is zero (hr_hourly_cost/models/hr_employee.py:10); a timesheet line for an employee with no cost, or with none set, is costed at zero (hr_timesheet/models/hr_timesheet.py:505).
- Cost is applied to a line only when the line is written or created with hours/employee/account values (hr_timesheet/models/hr_timesheet.py:460). I found no trigger that revalues existing lines when the employee's hourly cost later changes; existing amounts therefore keep the cost that applied when they were last written. Stated for hr_timesheet only; other modules' behaviour: UNKNOWN — EVIDENCE INSUFFICIENT.
- Company currency and the line date drive currency conversion (hr_timesheet/models/hr_timesheet.py:475-476).
- Project pricing mode "employee rate" swaps the cost source (see D).

## F. Effective extension path (module names only)
- Extends the employee model: hr_hourly_cost itself; employee form is further extended by hr_timesheet (its employee view inherits hr_hourly_cost's view: hr_timesheet/views/hr_employee_views.xml:13).
- Manifest dependents (grep of addons manifests): hr_timesheet only. Transitive consumers: sale_timesheet, sale_timesheet_margin, hr_timesheet_attendance (all read the field or the timesheet amount).

## G. Not verified
- Rate history / effective dating: UNKNOWN — EVIDENCE INSUFFICIENT.
- Relation to payroll wages: UNKNOWN — EVIDENCE INSUFFICIENT.
- Behaviour of project profitability views beyond the cited tests: UNKNOWN — EVIDENCE INSUFFICIENT.
- Revision `19.0.post20260921`; no rule above is asserted as universal beyond the cited lines.

