# Source Map (candidate) — `sale_margin`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_margin` |
| Display name | Margins in Sales Orders |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `4ef067da76e70f60` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_margin/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_management`
- Direct dependents in 300-module list (3): `sale_expense_margin`, `sale_stock_margin`, `sale_timesheet_margin`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `pos_sale_margin`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / —
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `sale.order`, `sale.order.line`, `sale.report`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `sale.order`, `sale.order.line`, `sale.report`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 23 of 23 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_margin
Source revision: 19.0.post20260921 | Module: "Margins in Sales Orders" (sale_margin/__manifest__.py:5) | depends: sale_management (:15) | not auto_install; LGPL-3 (:23)
Basis: static reading of all models, report, view; test_sale_margin.py read fully.

## A. Capabilities and optionality
- A1. Adds cost, margin (amount) and margin % to each sales line, and margin/margin % totals to the order; optional module, installed explicitly. sale_margin/models/sale_order_line.py:10-18; sale_margin/models/sale_order.py:10-12
- A2. Order form shows margin total (with % only when untaxed total is non-zero); line list shows cost/margin/margin% as optional hidden columns; margin % added to order pivot/graph. sale_margin/views/sale_order_views.xml:10-31,35-55
- A3. Sales analysis report gains a margin measure, converted using the order currency rate and the company currency table. sale_margin/report/sale_report.py:10-18

## B. Objects, relationships, lifecycle
- B1. No new business object; three stored calculated fields on sales line (cost "purchase_price", margin, margin %) and two on order. sale_margin/models/sale_order_line.py:10-18; sale_margin/models/sale_order.py:10-12
- B2. Cost per line default = product's standard cost, converted to the line's unit of measure, then to the sales line currency (from the product's cost currency); zero when no product. sale_margin/models/sale_order_line.py:20-36
- B3. Cost is user-editable (readonly false), not copied on duplication, recomputed when product, company, currency or unit changes. sale_margin/models/sale_order_line.py:15-20. (TEST) copying an order re-reads the current product cost: sale_margin/tests/test_sale_margin.py:104-126
- B4. Line margin = line subtotal (excl. tax, after discount) minus cost x ordered quantity; margin % = margin / subtotal (0 if subtotal 0). sale_margin/models/sale_order_line.py:47-48. (TEST) test_sale_margin.py:10-26,75-102
- B5. Special case: a line with delivered quantity but zero ordered quantity (added from delivery) uses price x delivered quantity for the basis and cost x delivered quantity. sale_margin/models/sale_order_line.py:42-45
- B6. Order margin = sum of line margins; margin % = order margin / untaxed total (0 if untaxed 0). sale_margin/models/sale_order.py:14-32. (TEST) test_sale_margin.py:56-57 (150% on negative-margin mix)
- B7. Zero-cost lines show 100% margin; negative price lines produce negative margin. (TEST) test_sale_margin.py:28-73
- B8. No state gating: margin is computed on quotations as well as confirmed orders. sale_margin/models/sale_order_line.py:38-48 (no state test); (TEST) test_sale_margin.py:59-73 (no confirmation)

## C. Validations, security, multi-company
- C1. No constraints. UNKNOWN — EVIDENCE INSUFFICIENT for any rounding or currency rule beyond the conversion call.
- C2. All margin/cost fields readable only by internal users (base.group_user) - portal/public cannot read them. sale_margin/models/sale_order_line.py:12,14,18; sale_margin/models/sale_order.py:10,12
- C3. Cost is computed in the line's company context (with_company). sale_margin/models/sale_order_line.py:26. Multi-company: standard cost is company-dependent on the product; company handling otherwise inherited. (TEST for stock variant) sale_stock_margin/tests/test_sale_stock_margin.py:242-302
- C4. Batch recomputation of order margins uses a single grouped read instead of per-record loop when records are saved. sale_margin/models/sale_order.py:20-32

## D. Handoffs
- D1. Cost source: product standard cost (owner product/stock_account). No accounting entry, no inventory move, no purchase or analytic posting from this module.
- D2. Actual-cost refinement after delivery is delegated to sale_stock_margin; expense re-invoice cost to sale_expense_margin; timesheet cost to sale_timesheet_margin; point-of-sale to pos_sale_margin (see F).

## E. Configuration that changes outcomes
- E1. Product cost (standard price) and its currency; product unit vs line unit; pricelist currency vs cost currency. sale_margin/models/sale_order_line.py:29-36
- E2. Manual override of the line cost. sale_margin/models/sale_order_line.py:15-18
- E3. Discount and price on the line drive subtotal used in margin. sale_margin/models/sale_order_line.py:47

## F. Effective extension path (modules)
- Depended on by (manifests): pos_sale_margin, sale_expense_margin, sale_stock_margin, sale_timesheet_margin.
- Overriding the cost computation (grep _compute_purchase_price): sale_stock_margin, sale_expense_margin, sale_timesheet_margin.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: demo data intent (sale_margin/data/sale_margin_demo.xml not analysed); effect of taxes-included prices on margin beyond subtotal being tax-excluded.

