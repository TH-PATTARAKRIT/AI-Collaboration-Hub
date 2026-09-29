# Source Map (candidate) — `sale_project_stock`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_project_stock` |
| Display name | Sale Project - Sale Stock |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `35f0626a0db0baac` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_project_stock/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_project`, `sale_stock`, `project_stock_account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales / Adds a full traceability of inventory operations on the profitability report.
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (4): `sale.order.line`, `stock.move`, `stock.picking`, `project.project`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `sale.order.line`, `stock.move`, `stock.picking`, `project.project`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 26 of 26 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_project_stock
Source revision: 19.0.post20260921 | Module: "Sale Project - Sale Stock" (sale_project_stock/__manifest__.py:5) | depends: sale_project, sale_stock, project_stock_account (:12) | auto_install true (:16) | LGPL-3 (:10)
Basis: static reading of all four models, view and manifest; both test files read in part.

## A. Capabilities and optionality
- A1. Goods moved out on a transfer linked to a project can be automatically re-invoiced on that project's sales order (sales line created with the moved products), and inventory traceability is shown per sales line in the project's profitability panel. sale_project_stock/__manifest__.py:7-8; sale_project_stock/models/stock_picking.py:10-62; sale_project_stock/models/sale_order_line.py:10-25
- A2. Automatic bridge when the three parents are present. sale_project_stock/__manifest__.py:12,16
- A3. Conditional on operation type flag "analytic costs" (owner project_stock_account) and product "expense policy" = re-invoice at sales price or at cost. sale_project_stock/models/stock_picking.py:18,20

## B. Objects, relationships, lifecycle
- B1. Transfer creation inherits the project of the sales order tied to the move's sales line (picking header, move-to-picking assignment, and procurement values). sale_project_stock/models/stock_move.py:60-77
- B2. On validation of a transfer (only when validation completes without an intermediate wizard): if the project has a "re-invoiced sales order" and the picking type generates analytic costs, moves whose product is re-invoiceable produce new sales lines on that order (batch), placed after the last line. sale_project_stock/models/stock_picking.py:10-61
- B3. Guard on that order state: draft/quotation -> error "must be validated before validating the picking"; cancelled -> error; locked -> error asking for a new order linked to the project. sale_project_stock/models/stock_picking.py:24-45. No effect when there is no project order or no re-invoiceable product. sale_project_stock/models/stock_picking.py:16-22
- B4. New sales line values: description = move reference, product and tax from the order's fiscal position, quantity ordered = move demand, delivered = move done quantity, discount 0. sale_project_stock/models/stock_move.py:39-58
- B5. Unit price: "sales price" policy -> pricelist price of one unit on the order date; "cost" policy -> product standard cost (0 when done quantity is zero), converted to the order currency when currencies differ (rounded without conversion when equal). sale_project_stock/models/stock_move.py:10-37
- B6. The lines are created without launching procurement (no second delivery) and under elevated rights. sale_project_stock/models/stock_picking.py:61
- B7. (TEST) Picking of 3 units at-cost product and 5 units at-sales-price product validated by a stock user: order gains 2 lines with price = standard price (3 delivered) and list price (5 delivered), nothing invoiced yet, delivered-quantity method = stock move. sale_project_stock/tests/test_reinvoice.py:42-81
- B8. Project action "Transfers" pre-selects the user's default warehouse operation type (outgoing/incoming). sale_project_stock/models/project_project.py:9-18
- B9. Sales-line "action" in project profitability opens the stock moves of the line (list/form) for non-service lines when the user has stock rights. sale_project_stock/models/sale_order_line.py:15-24; sale_project_stock/views/stock_move_views.xml:4-9
- B10. (TEST) Anglo-Saxon automatic valuation: COGS invoice lines are classified under "Costs" in the project profitability report. sale_project_stock/tests/test_sale_project_stock_profitability.py:40-60

## C. Validations, security, multi-company
- C1. No new groups, ACLs, or rules. Stock-move list available only to stock users in the profitability panel. sale_project_stock/models/sale_order_line.py:18
- C2. Line creation runs with elevated rights and reads the order under sudo so a stock user need not have sales rights. sale_project_stock/models/stock_move.py:43; sale_project_stock/models/stock_picking.py:17,61
- C3. Company: uses the move's company currency versus the order's; order fiscal position and company taxes. sale_project_stock/models/stock_move.py:31-46. Other multi-company: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. Inventory (transfer validation, moves): stock. Sales lines/order lifecycle and invoicing to customer: sale. Project profitability and cost items: project/sale_project/project_stock_account (analytic costs on picking type). Accounting entries and COGS: stock_account/account.
- D2. Analytic: project analytic account distribution flows via sale_project; not created here.

## E. Configuration that changes outcomes
- E1. Operation type "analytic costs". sale_project_stock/models/stock_picking.py:18
- E2. Product expense policy (sales price / cost / none). sale_project_stock/models/stock_move.py:16,28
- E3. Project field "sales order to re-invoice" (reinvoiced_sale_order_id, owned by sale_project). sale_project/models/project_project.py:45-47
- E4. User's default warehouse (property_warehouse). sale_project_stock/models/project_project.py:12

## F. Effective extension path (modules)
- Depended on by: none (grep of manifests). Extends sale_project, sale_stock, project_stock_account; overrides _sale_prepare_sale_line_values pattern also in sale, sale_expense, sale_expense_margin.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: what happens on picking return/cancel after lines were created; duplicate-line risk when a picking is re-validated after backorder.

