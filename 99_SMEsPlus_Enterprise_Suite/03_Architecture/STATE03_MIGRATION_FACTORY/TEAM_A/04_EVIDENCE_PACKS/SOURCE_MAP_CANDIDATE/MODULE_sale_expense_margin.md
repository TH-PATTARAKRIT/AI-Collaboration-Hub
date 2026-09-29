# Source Map (candidate) — `sale_expense_margin`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_expense_margin` |
| Display name | Sales Expense Margin |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c1e93b51b8c95aa2` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_expense_margin/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_expense`, `sale_margin`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `account.move.line`, `sale.order.line`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.move.line`, `sale.order.line`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 12 of 12 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_expense_margin
Source revision: 19.0.post20260921 | Module: "Sales Expense Margin" (sale_expense_margin/__manifest__.py:5) | depends: sale_expense, sale_margin (:8) | auto_install true (:10) | LGPL-3 (:12)
Basis: static reading of both models; the single test read fully.

## A. Capabilities and optionality
- A1. When an employee expense is re-invoiced on a sales order, the resulting sales line's cost (for margin) is set to the expense's untaxed amount rather than the product's standard cost. sale_expense_margin/__manifest__.py:7; sale_expense_margin/models/sale_order_line.py:11-19
- A2. Automatic bridge: installs itself when Expenses-to-Sales and Sales Margin are present. sale_expense_margin/__manifest__.py:8,10

## B. Objects, relationships, lifecycle
- B1. Sales line gains a link to the originating expense record (owner hr_expense). sale_expense_margin/models/sale_order_line.py:9
- B2. Invoice-line-to-sales-line preparation copies the expense link onto the new sales line when the source journal line comes from an expense. sale_expense_margin/models/account_move_line.py:10-14
- B3. Cost per unit = expense untaxed amount (in expense currency) divided by expense quantity (1 if none), converted to the sales line currency. sale_expense_margin/models/sale_order_line.py:14-17
- B4. Lines without an expense link follow the normal margin cost rule (product standard cost, or delivery cost with sale_stock_margin). sale_expense_margin/models/sale_order_line.py:19
- B5. (TEST) Re-invoiceable expenses at "sales price": first order line (a normal sold product) keeps cost 1000 and is not flagged as expense; expense lines get costs 86.96 (100 with 15% purchase tax included), 100.0 (no tax), 869.57 (3 x 1000 product with tax, per unit), 1000.0 (no tax) and are flagged as expenses. sale_expense_margin/tests/test_so_expense_purchase_price.py:12-85
- B6. Lifecycle: expense submitted, approved, posted (accounting entry created); cost appears on the sales order only after posting via the expense flow. (TEST) test_so_expense_purchase_price.py:75-85

## C. Validations, security, multi-company
- C1. No constraints, groups or rules added. Cost visibility remains internal-user only via sale_margin. sale_margin/models/sale_order_line.py:18
- C2. Test runs the order creation as sudo (salesperson access to expense objects not shown). UNKNOWN — EVIDENCE INSUFFICIENT on user rights needed to trigger the link.
- C3. Multi-company: none explicit. UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. Expense creation/approval/posting: hr_expense; re-invoice to sales order and the created sales line: sale_expense (and sale). Margin arithmetic: sale_margin.
- D2. Accounting: expense entry belongs to account/hr_expense; this module does not create entries.

## E. Configuration that changes outcomes
- E1. Product expense policy (re-invoice at sales price or at cost) decided in sale_expense; test uses "sales price". test_so_expense_purchase_price.py:15,17
- E2. Taxes on the expense: untaxed amount drives cost. sale_expense_margin/models/sale_order_line.py:16
- E3. Recompute trigger is the expense flag on the line. sale_expense_margin/models/sale_order_line.py:11

## F. Effective extension path (modules)
- Depended on by: none (grep of manifests). Overrides cost logic of sale_margin (also overridden by sale_stock_margin, sale_timesheet_margin); extends sale_expense's line preparation.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour for expenses in a foreign currency beyond the conversion call, and after later expense correction/reversal.

