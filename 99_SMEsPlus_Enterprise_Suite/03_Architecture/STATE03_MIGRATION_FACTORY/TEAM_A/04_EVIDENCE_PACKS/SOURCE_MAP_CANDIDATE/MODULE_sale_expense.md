# Source Map (candidate) — `sale_expense`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_expense` |
| Display name | Sales Expense |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c049c501abb2239f` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_expense/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_management`, `hr_expense`
- Direct dependents in 300-module list (3): `project_sale_expense`, `sale_expense_margin`, `spreadsheet_dashboard_hr_expense`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Quotation, Sales Orders, Delivery & Invoicing Control
- Inventory of user-facing artifacts (counts): menu items 0, views 7, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (7): `account.move`, `hr.expense`, `sale.order`, `account.move.line`, `sale.order.line`, `product.template`, `hr.expense.split`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.move`, `hr.expense`, `sale.order`, `account.move.line`, `sale.order.line`, `product.template`, `hr.expense.split`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 40 of 40 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: sale_expense (revision 19.0.post20260921)
Scope: Odoo Community read-only study. Pointers `module/path:LINE`; (TEST) = test-derived. Reinvoice engine itself is owned by sale (account move line hooks).

## A. Capabilities and activation
- Lets an employee expense be re-billed to a customer by picking the customer sales order directly on the expense (sale_expense/__manifest__.py:9-15). Depends on sale_management and hr_expense (sale_expense/__manifest__.py:16); auto_install, so it activates when both are present (sale_expense/__manifest__.py:24).
- Conditional per product: only expense categories with re-invoice policy "at cost" or "sales price" can carry a sales order (sale_expense/models/hr_expense.py:29-40; sale/models/product_template.py:22-30). The customer field on the expense form is hidden otherwise (sale_expense/views/hr_expense_views.xml:24-25).
- Seed data flips the demo expense categories: meals and mileage to sales price, travel/accommodation and communication to cost; mileage and travel also set to invoice on delivery (sale_expense/data/sale_expense_data.xml:3-23, noupdate).

## B. Objects, relationships, lifecycle
- Expense gets "Customer to Reinvoice" (a confirmed sales order) and a link to the generated order line (sale_expense/models/hr_expense.py:9-28). Order gets a read-only list of expenses in posted/in payment/paid states and an expense count, with a smart button (sale_expense/models/sale_order.py:10-17,35-43; sale_expense/views/sale_order_views.xml:10-19). Order line gets its expenses list (sale_expense/models/sale_order_line.py:9-14).
- Posting the expense: if a customer order is set but the expense has no analytic distribution, a new analytic account is created from the order data and used at 100% (sale_expense/models/hr_expense.py:70-79). Reinvoicing works through analytic entries, so the standard flow then builds the order line when analytic lines are generated (sale/models/account_move_line.py:47-71).
- Order line creation for expenses: each expense goes on its own order line (forced split), copying description, expense link and analytic distribution; for "sales price" policy with a standard cost set, order quantity equals the expense quantity (sale_expense/models/account_move_line.py:35-58). Target order determination is overridden to use the expense's order (sale_expense/models/account_move_line.py:22-33). Reinvoice is allowed only for product-type move lines of expenses whose category has cost/sales price policy and an order is set (sale_expense/models/account_move_line.py:9-20).
- Standard checks in sale before creating the line: target order must be confirmed (not draft/sent), not cancelled, not locked (sale/models/account_move_line.py:103-119). Created lines are flagged as expense lines (sale/models/account_move_line.py:195). Expense lines are excluded from purchase generation in sale_purchase (sale_purchase/models/sale_order_line.py:45-48).
- Reversal path: resetting the expense's journal entry to draft, reversing it, or deleting it zeroes ordered and delivered quantities on the linked order line and detaches the expenses (sale_expense/models/account_move.py:9-22; sale_expense/models/hr_expense.py:48-61) (TEST: sale_expense/tests/test_reinvoice.py:202-225,262-337). Lines not created from expenses are untouched (TEST: sale_expense/tests/test_reinvoice.py:202-225). Duplicated identical lines are not both reset (TEST: sale_expense/tests/test_reinvoice.py:338-408).
- Splitting an expense carries the customer order to each split part; the split wizard limits choices to confirmed orders of the same company (sale_expense/models/hr_expense.py:63-68; sale_expense/models/hr_expense_split.py:9-26).
- Company-paid expenses are re-invoiced too (TEST: sale_expense/tests/test_reinvoice.py:542-563).

## C. Validations, security, multi-company
- Customer field: company-checked; changing it forces the analytic distribution to recompute; cleared automatically when the category cannot be reinvoiced (sale_expense/models/hr_expense.py:20,36-46).
- Order picker for expense users: salesmen without all-leads visibility can still find confirmed orders (name only) across their allowed companies via an elevated search, so the standard record rules do not hide them; other users use normal search (sale_expense/models/sale_order.py:19-33; view context sale_expense/views/hr_expense_views.xml:44).
- Resetting order-line quantities runs with elevated rights after a write-access check on the expense (sale_expense/models/hr_expense.py:55-57).
- Expense category policy is forced to "no" when the product cannot be expensed (sale_expense/models/product_template.py:40-43); policy visibility for expense products is shown to expense-officer group members (sale_expense/models/product_template.py:31-38).
- Expense button on the order is shown to salesmen only (sale_expense/views/hr_expense_views.xml:11); order-list amount columns are restricted to sales/invoice/accounting-readonly groups (sale_expense/views/sale_order_views.xml:30-40). No access or record-rule file in this module.

## D. Handoffs (owner)
- Expense posting, employee payable/reimbursement, journal entry: hr_expense / account. Order line creation, pricing at cost vs sales price, taxes by fiscal position: sale (sale/models/account_move_line.py:175-196). Customer invoice: sale/account from the order line. Analytic entries: analytic/account. Purchase: none. Inventory: none (a stock-tracked product would raise on reset, as noted in sale_expense/models/hr_expense.py:52-53).

## E. Configuration that changes outcomes
- Product "Re-Invoice Costs" (no / at cost / sales price) and invoicing policy of the expense category (sale_expense/data/sale_expense_data.xml:5-22). Sales order must already be confirmed and unlocked. Analytic account creation is automatic if absent (sale_expense/models/hr_expense.py:76-78).

## F. Extension path
- Extends hr.expense, hr.expense.split, account.move, account.move.line, product.template, sale.order, sale.order.line (sale_expense/models/*.py). Modules depending on it: project_sale_expense, sale_expense_margin, spreadsheet_dashboard_hr_expense (manifest grep). Other hr.expense extenders: project_hr_expense, project_sale_expense.

## G. Not verified
- Tax and multi-line behaviour beyond test title (TEST: sale_expense/tests/test_reinvoice.py:451): UNKNOWN — EVIDENCE INSUFFICIENT
- Effect on the employee reimbursement side: UNKNOWN — EVIDENCE INSUFFICIENT
- Company-level access rules on hr.expense across companies: UNKNOWN — EVIDENCE INSUFFICIENT

