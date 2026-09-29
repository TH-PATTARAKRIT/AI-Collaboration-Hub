# Source Map (candidate) — `hr_org_chart`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_org_chart` |
| Display name | HR Org Chart |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `277fd1fe10617e24` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_org_chart/` |
| auto_install / application | ['hr'] / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr`, `web_hierarchy`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources / —
- Inventory of user-facing artifacts (counts): menu items 0, views 7, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 3
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `hr.employee`, `hr.employee.public`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.employee`, `hr.employee.public`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 35 of 36 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_org_chart (HR Org Chart)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_org_chart.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Presentation module that shows reporting lines: an in-form "Organization Chart" panel (managers above, direct reports below), a full-screen hierarchy view of employees, and a hierarchy view of departments. Manifest states the panel covers N+1, N+2 and direct subordinates (hr_org_chart/__manifest__.py:13-14). Depends on hr and the generic hierarchy view component (hr_org_chart/__manifest__.py:16).
- Conditional-on-install: auto_install is set on hr (hr_org_chart/__manifest__.py:17); appears automatically with HR. Not an application; no settings.
- Employee form: panel with a "Full Chart" link that opens the hierarchy screen focused on the employee (hr_org_chart/views/hr_views.xml:22-45). Hidden when the employee has neither subordinates nor a distinct manager (hr_org_chart/views/hr_views.xml:28).
- Full hierarchy screen for employees (path "org-chart"), listed with kanban/list/form/graph/pivot/activity alternatives (hr_org_chart/views/hr_views.xml:3-8) and drag-and-drop enabled (hr_org_chart/views/hr_views.xml:73); a public-profile equivalent (path "org-chart-public") with drag-and-drop disabled (hr_org_chart/views/hr_employee_public_views.xml:4-8, 24). Hierarchy is also added as a view type to the "my employees" action (hr_org_chart/views/hr_views.xml:99-103).
- Department hierarchy view (drag-and-drop enabled) added to the department kanban and list actions (hr_org_chart/views/hr_department_views.xml:8, 31-41).
- Computed helpers on the employee: direct-report count, all-descendant count, list of all subordinates, department colour, and a "is subordinate of me" flag with search support (hr_org_chart/models/hr_org_chart_mixin.py:11-20, 40-70; hr_org_chart/models/hr_employee.py:10-12). Public profile mirrors them (hr_org_chart/models/hr_org_chart_mixin.py:73-87; hr_org_chart/models/hr_employee.py:15-19).
- Three JSON endpoints for the chart widget: which model to open (employee vs public profile depending on read right), the manager chain plus children, and direct/indirect subordinate ids (hr_org_chart/controllers/hr_org_chart.py:38-42, 44-78, 80-99).

## B. Business objects, relationships, lifecycle
- Uses the employee "Manager" link (hr/models/hr_employee.py:195) and its inverse "Direct subordinates" (active only) (hr/models/hr_employee.py:197). Department parent/child is used for department chart (hr/models/hr_department.py:115-116 guards department parent).
- Subordinate calculation walks descendants and excludes anyone already seen higher in the chain, so a person who manages their own manager (loops, e.g. top executive) is not counted as their own subordinate (hr_org_chart/models/hr_org_chart_mixin.py:22-38).
- Manager chain length is capped: default five levels above, extended by one, with loop breaking when an ancestor is already collected (hr_org_chart/controllers/hr_org_chart.py:10, 57-65, 74).
- "Is subordinate" is relative to the acting user's own employee: true if the record is a direct or indirect report (hr_org_chart/models/hr_org_chart_mixin.py:46-60). (TEST) direct report true, no-manager false, chain of two levels both true, breaking the chain makes both false (hr_org_chart/tests/test_employee.py:19-61).
- No lifecycle/states of its own. Reassigning a manager by dragging in the hierarchy screen changes the employee's manager (front-end behaviour; the drag-enabled flag is hr_org_chart/views/hr_views.xml:73; the write path is in static assets not traced: UNKNOWN — EVIDENCE INSUFFICIENT).

## C. Validations, automation, security, multi-company
- No constraints, cron or ACL of its own (skeleton: constrains [], access [], rules []). Counts are computed with elevated rights so managers who cannot see a report's record still get consistent counts (hr_org_chart/models/hr_org_chart_mixin.py:14, 19; hr_org_chart/models/hr_employee.py:11).
- Controller reads data from the public employee profile (a reduced view of employee data), returns nothing if the user has no read access, honours the user's active companies, and uses elevated reads only to walk the manager chain (hr_org_chart/controllers/hr_org_chart.py:12-23, 47, 55). Job title is read with elevated rights (hr_org_chart/controllers/hr_org_chart.py:26).
- Company scoping: active-company list from the request context, defaulting to the current company (hr_org_chart/controllers/hr_org_chart.py:15-21). (TEST) a restricted user in one company can still open the org chart when the manager belongs to another company (hr_org_chart/tests/test_employee_ui.py:28-57).
- (TEST) Editing an employee whose manager and coach are themselves, with a department change, must not delete the record (hr_org_chart/tests/test_employee_deletion.py:10-39) - regression guard for the form.
- Which group can see the full employee hierarchy vs public hierarchy follows base hr access; the open-model endpoint picks the employee model only if the user has read access to it (hr_org_chart/controllers/hr_org_chart.py:40-42).

## D. Accounting / payroll / analytic handoffs
- None. Pure organisational display; no accounting, payroll or analytic use.

## E. Configuration / defaults that change outcomes
- Maximum manager levels default five (hr_org_chart/controllers/hr_org_chart.py:10); callers may override via context (hr_org_chart/controllers/hr_org_chart.py:57).
- Quality of the manager field drives everything; manager candidates are limited to employees of no company or in the user's allowed companies (hr/models/hr_employee.py:195-196).
- Inactive (archived) reports are not shown in the direct-report list (hr/models/hr_employee.py:197 domain).

## F. Effective extension path (module names only)
- Extends: hr (employee, public employee, department views/actions), web_hierarchy (view type). Manifest dependents on hr_org_chart: none found.

## G. Not verified
- Front-end drag/drop write permissions and effect on coach: UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether a manager change loop is prevented on the model: UNKNOWN — EVIDENCE INSUFFICIENT (no constraint found in this module; the controller and helper tolerate loops).
- Revision `19.0.post20260921`.

