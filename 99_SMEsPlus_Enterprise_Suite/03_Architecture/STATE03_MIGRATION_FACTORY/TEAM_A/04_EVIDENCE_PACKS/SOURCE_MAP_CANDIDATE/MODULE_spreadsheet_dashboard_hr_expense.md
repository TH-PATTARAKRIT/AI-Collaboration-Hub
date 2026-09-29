# Source Map (candidate) — `spreadsheet_dashboard_hr_expense`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `spreadsheet_dashboard_hr_expense` |
| Display name | Spreadsheet dashboard for expenses |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `538f8a951070edec` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/spreadsheet_dashboard_hr_expense/` |
| auto_install / application | ['sale_expense'] / None |

## 2. Dependencies
- Direct dependencies (manifest): `spreadsheet_dashboard`, `sale_expense`
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

# Source Map trace note: spreadsheet_dashboard_hr_expense
Revision 19.0.post20260921 | Dashboard bridge: Spreadsheet Dashboards <-> Expenses (via sale_expense) | data-only module

## A. Capabilities (core / optional / conditional)
- Delivers one published dashboard "Expenses" (spreadsheet_dashboard_hr_expense/data/dashboards.xml:3-11). Depends on spreadsheet_dashboard and sale_expense (not directly on hr_expense) (spreadsheet_dashboard_hr_expense/__manifest__.py:9).
- Auto-install: when sale_expense is installed (spreadsheet_dashboard_hr_expense/__manifest__.py:14). The dashboard therefore appears only where sales-linked expenses are available, not with hr_expense alone. sale_expense itself depends on sale_management and hr_expense and auto-installs (sale_expense/__manifest__.py:16,24).
- Finance dashboard group, sequence 40, visible to expense managers (spreadsheet_dashboard_hr_expense/data/dashboards.xml:8-9). Main data model: expenses; sample dashboard registered (:6-7). No settings, rules or access CSV.

## B. Business objects and lifecycle
- Read-only over expense records. Pivots: by category (product), by employee, by sales order, and four KPI pivots (spreadsheet_dashboard_hr_expense/data/files/expense_dashboard.json:528,566,593,615,642,669,713).
- Widgets: scorecards Expenses, To report, To validate, To reimburse (KPI cells json:430-433); monthly bar chart of total amount by product; "Top Categories" carousel; Top Expenses list sorted by amount descending (json:774-777).
- No state changes.

## C. Validations, automation, security
- Access: expense manager group only (spreadsheet_dashboard_hr_expense/data/dashboards.xml:9).
- KPI state filters: To report = draft; To validate = state "reported"; To reimburse = approved (expense_dashboard.json:608,635,662). Observation: the expense state list of this revision is draft / submitted / approved / posted / in payment / paid / refused (hr_expense/models/hr_expense.py:124-137), so the value "reported" used for To validate is not one of them; effect on the figure: UNKNOWN — EVIDENCE INSUFFICIENT (likely no match).
- Leaderboards exclude expenses without a category / employee / sales order for their respective pivot (expense_dashboard.json:528-566,713-733).
- Company scoping: UNKNOWN — EVIDENCE INSUFFICIENT (top-expenses list includes company column: json:777 columns; no explicit rule).

## D. Handoffs
- hr_expense owns expenses, states, employees, categories (products); sale_expense owns the sales-order link on expenses (basis of the "Order" pivot/filter); spreadsheet_dashboard owns the container and Finance group.

## E. Measures and configuration (cost basis)
- "Expenses" KPI = count of expense records (expense_dashboard.json:430). Amount KPIs and chart use "total amount" (Total), which is in company currency (not the expense's own currency) and includes taxes (hr_expense/models/hr_expense.py:168-182, 502-546). Basis is claimed expense amount by expense date, not posted/paid amounts.
- Default period: last 12 months (expense_dashboard.json:733). Filters: Period, Product, Order, Employee (json:~733-770).
- To reimburse = approved-state amount, i.e. approved but not yet posted/paid (expense_dashboard.json:662).

## F. Effective extension path
- hr_expense, sale_expense, spreadsheet_dashboard (module names only).

## G. Not verified
- Whether the period filter applies to expense date or creation date: UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether refused expenses are included in the count and monthly chart (no state filter present: expense_dashboard.json:593-614): inclusion by default record visibility: UNKNOWN — EVIDENCE INSUFFICIENT.

