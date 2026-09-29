# Source Map (candidate) — `mrp_subcontracting_purchase`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mrp_subcontracting_purchase` |
| Display name | Purchase and Subcontracting Management |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G03 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `6f6d78ecddf48981` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_subcontracting_purchase/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mrp_subcontracting`, `purchase_mrp`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Purchase / —
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (7): `account.move.line`, `purchase.order`, `product.product`, `stock.move`, `stock.picking`, `stock.rule`, `report.mrp.report_bom_structure`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.move.line`, `purchase.order`, `product.product`, `stock.move`, `stock.picking`, `stock.rule`, `report.mrp.report_bom_structure`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 30 of 30 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: mrp_subcontracting_purchase

Source revision: 19.0.post20260921 (Odoo 19 Community). Pointers relative to the addons root. `(TEST)` = test-derived. Neutral business language; no code copied.

## 1. Capabilities
- Bridge between Purchase and Subcontracting: "adds some smart buttons" (`mrp_subcontracting_purchase/__manifest__.py:8-10`) but in practice also owns lead-time, notification, valuation-on-bill and reporting adjustments. Depends on `mrp_subcontracting` and `purchase_mrp` (`:11`); auto-installs (`:20`) - conditional bridge.
- Views: purchase order smart button for resupply pickings and picking smart button for the source purchase order (`views/purchase_order_views.xml`, `views/stock_picking_views.xml`; counts at `models/purchase_order.py:10-25`, `models/stock_picking.py:10-40`).
- Demo data present (`__manifest__.py:16-18`).

## 2. Business objects and lifecycle
- Purchase order to subcontract: a PO line for a product that has a subcontract BoM listing that vendor produces a receipt line flagged as subcontract (created by `mrp_subcontracting`), which in turn creates the production and component resupply pickings (see `mrp_subcontracting` note, section 2). This module links them back: PO -> resupply pickings via production pickings (`models/purchase_order.py:22-25`); picking -> source PO via receipt lines' purchase lines (`models/stock_picking.py:38-40`).
- At production creation the source PO's buyer and the product's responsible user are notified about procurement problems (`models/stock_picking.py:42-45`, `models/stock_rule.py:58-63`).
- PO production listing hides productions whose operation type is archived (`models/purchase_order.py:27-31`).

## 3. Actions, gating, security
- No new groups, ACLs or record rules in this module (manifest lists views only, `__manifest__.py:12-15`). It inherits standard purchase access.
- Returns: a return of subcontract goods to the subcontractor is treated as a purchase return for valuation purposes (`models/stock_move.py:10-12`).
- Company scoping: lead-time uses the company of the buy rule's operation type (`models/stock_rule.py:22-26`); "Days to Purchase" taken from the BoM's company in reports (`report/mrp_report_bom_structure.py:19`).

## 4. Accounting / inventory / purchase handoffs (cost of the subcontracted product)
Owner by step:
- PO price: entered on PO line; before billing it values the receipt (purchase_stock quotation-value routine `purchase_stock/models/stock_move.py:229-243`).
- Fee determination order (bill first, then PO for unbilled part, then receipt price) sits in `mrp_subcontracting_account/models/mrp_production.py:11-21` and the generic order in `stock_account/models/stock_move.py:401-424`.
- Revaluation when a vendor bill is posted: this module recomputes the finished production move's value as (existing unit cost minus old fee plus new fee from bill/PO) x quantity, where new fee = (bill value + PO value for unbilled qty) / quantity; it does nothing when both are zero (`mrp_subcontracting_purchase/models/stock_move.py:14-38`). The bill lookup on the subcontract receipt suppresses the extra so that fee is not counted twice (`:22`).
- Standard-cost products: price difference between bill and standard also carries the components' cost (value of raw moves of the production divided by produced quantity, currency-converted at the last component move date) (`models/account_move_line.py:9-22`) (TEST `tests/test_mrp_subcontracting_purchase.py:354,404` price-difference and multi-currency).
- Which moves a bill line relates to: includes the production's finished moves (`models/account_move_line.py:24-30`) so bills reach the production valuation (TEST `:268` bill flow, `:470` price change after bill produces a corrective valuation entry).
- Component cost: comes from components consumed at the subcontracting location (owned by `mrp_account`/`stock_account`); component value never comes from the PO.
- Landed costs: not handled in this module. `mrp_subcontracting_landed_costs` redirects landed cost targeting from the receipt line to the underlying production finished move (`mrp_subcontracting_landed_costs/models/stock_landed_cost.py:10-18`) (TEST `mrp_subcontracting_landed_costs/tests/test_subcontracting_landed_costs.py:11,141`).
- Dropship: owned by `mrp_subcontracting_dropshipping` (see its note).

## 5. Configuration that changes outcomes
- Lead time: subcontracted receipt date = larger of vendor lead time and BoM manufacturing lead time plus days-to-prepare-MO, plus days to purchase (`models/stock_rule.py:7-56`); vendor lead time wins when it is at least BoM lead time + prepare days (`:32`). Reports show the same (`report/mrp_report_bom_structure.py:15-24`).
- The Buy route is not offered for the reporting of a subcontract BoM (`report/mrp_report_bom_structure.py:10-12`).
- Product costing method (standard vs FIFO/average) determines whether component cost is added to the bill price difference (`models/account_move_line.py:11`).
- Demand forecasting: stock moves into subcontracting locations count as monthly demand, moves out of them do not (`models/product_product.py:10-19`).
- PO price, vendor bill price and currency (see section 4).

## 6. Effective extension path
Models extended: `purchase.order`, `stock.move`, `stock.picking`, `stock.rule`, `account.move.line`, `product.product`, report `report.mrp.report_bom_structure`. Related community modules: `mrp_subcontracting`, `mrp_subcontracting_account`, `mrp_subcontracting_dropshipping`, `mrp_subcontracting_landed_costs`, `purchase_mrp`, `purchase_stock`, `stock_account`.

## 7. By-products
Not applicable on the BoM path: subcontract BoMs reject by-product lines (`mrp_subcontracting/models/mrp_bom.py:24-27`). This module contains no by-product logic. Manual by-products on a subcontract production: UNKNOWN - EVIDENCE INSUFFICIENT.

## 8. UNKNOWN items
- Behaviour of bill quantity greater than received quantity for a subcontract line: UNKNOWN - EVIDENCE INSUFFICIENT.
- Interaction with blanket orders / purchase agreements: UNKNOWN - EVIDENCE INSUFFICIENT.
- Whether bill revaluation applies identically for every costing method beyond the tested standard, FIFO cases (`mrp_subcontracting_purchase/models/stock_move.py:14-38` is method-agnostic; account-line branch at `models/account_move_line.py:11` is standard-only): UNKNOWN - EVIDENCE INSUFFICIENT.

