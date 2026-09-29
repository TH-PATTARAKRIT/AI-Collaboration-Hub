# Source Map (candidate) — `project_sale_expense`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_sale_expense` |
| Display name | Project - Sale - Expense |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `22dd24781802ae61` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_sale_expense/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_project`, `sale_expense`, `project_hr_expense`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `hr.expense`, `account.move.line`, `project.project`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.expense`, `account.move.line`, `project.project`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 20 of 20 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: project_sale_expense (Odoo 19 Community, revision 19.0.post20260921)
## A. Capabilities; core / optional / conditional
- Adds full traceability of re-invoiced expenses to the project profitability report. project_sale_expense/__manifest__.py:6
- Conditional bridge: auto-installs when sale_project, sale_expense and project_hr_expense are installed. project_sale_expense/__manifest__.py:11-12
## B. Business objects and lifecycle
- Objects touched: expense, journal item (move line), project. project_sale_expense/models/__init__.py:3-5
- Expense linked to a sale order: its cost distribution is merged with the order's project distribution when analytic plans differ; if both use the same plan, the project's one wins. project_sale_expense/models/hr_expense.py:9-37; (TEST) project_sale_expense/tests/test_project_sale_expense.py:35-106
- Not applied when the expense is created from the project overview (project in context). project_sale_expense/models/hr_expense.py:11
- On posting an expense without distribution whose order has a project, the project's analytic account is created if absent and used. project_sale_expense/models/hr_expense.py:39-50
- Posted / in-payment / paid expenses tied to project accounts are grouped by order, product, currency and reported as cost; the re-invoiced part (expense-type order lines on confirmed orders, same product) is reported as revenue (invoiced / to invoice). project_sale_expense/models/project_project.py:12-88
## C. Validations, automation, security, multi-company
- Expense-generated move lines find their sale order from the expense first, otherwise from the project's analytic accounts. project_sale_expense/models/account_move_line.py:9-17
- Expense drill-down action only for users in the expense team-approver group; order-line amounts read in elevated mode. project_sale_expense/models/project_project.py:23,34
- Amounts converted to the project currency using the project's company. project_sale_expense/models/project_project.py:32,57-58. Company scoping of expenses beyond this: UNKNOWN — EVIDENCE INSUFFICIENT
- (TEST) Company-paid expense: project distribution stays on the expense (P&L) line only, not on outstanding/tax lines. project_sale_expense/tests/test_expense_analytics.py:9-53
- (TEST) Order project without analytic account stays without one after confirmation of an ordinary sale. project_sale_expense/tests/test_project_sale_expense.py:11-33
## D. Accounting / inventory / analytic handoffs
- Expense posting and payment: hr_expense; re-invoice order line creation: sale_expense (expense mapping sale_expense/models/account_move_line.py:22-26, line values :36-49); project mapping of move lines to orders: sale_project (sale_project/models/account_move_line.py:35). Analytic accounts: analytic. This module only adjusts distribution and reporting.
- Expense invoice lines are excluded from other profitability sections to avoid double counting. project_sale_expense/models/project_project.py:90-101; base rule project_hr_expense/models/project_project.py:60-67
- Inventory: none.
## E. Configuration
- Product expense re-invoice policy (sales price / cost) on the expense product decides whether re-invoicing applies. sale_expense/models/account_move_line.py:13-20
- Expense sale order field and order's project/analytic account. project_sale_expense/models/hr_expense.py:14
## F. Extension path
- _inherit: account.move.line, hr.expense, project.project (project_sale_expense/models/*.py). Overrides the profitability expense section of project_hr_expense (project_hr_expense/models/project_project.py:70). Dependents: none in tree.
## G. Not verified
- Reimbursement/payment state effects on revenue side: UNKNOWN — EVIDENCE INSUFFICIENT
- Behaviour with multiple expenses per order and mixed currencies beyond code above: UNKNOWN — EVIDENCE INSUFFICIENT

