# Source Map (candidate) — `sale_purchase_stock`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_purchase_stock` |
| Display name | MTO Sale <-> Purchase |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `6334b9837748e08b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_purchase_stock/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_stock`, `purchase_stock`, `sale_purchase`
- Direct dependents in 300-module list (1): `stock_dropshipping`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / SO/PO relation in case of MTO
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `sale.order`, `purchase.order`, `purchase.order.line`, `stock.move`, `stock.rule`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `sale.order`, `purchase.order`, `purchase.order.line`, `stock.move`, `stock.rule`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 19 of 19 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_purchase_stock
Source revision: 19.0.post20260921 | Module: "MTO Sale <-> Purchase" (sale_purchase_stock/__manifest__.py:5) | depends: sale_stock, purchase_stock, sale_purchase (:12) | auto_install true (:17) | LGPL-3 (:19)
Basis: static reading of all models/views; tests sampled by docstring and selected reads.

## A. Capabilities and optionality
- A1. Shows the relationship between sales orders and purchase orders created by make-to-order (MTO) replenishment or dropshipping. sale_purchase_stock/__manifest__.py:6-11
- A2. Bridge, automatic when sales-with-inventory, purchase-with-inventory and sales-purchase links are present. sale_purchase_stock/__manifest__.py:12,17
- A3. Dropship itself (route, delivery to customer) is NOT here; it is in stock_dropshipping, which depends on this module (manifest grep).

## B. Objects, relationships, lifecycle
- B1. Purchase order's linked sales orders now also include orders reachable through procurement references of the PO; count recomputed accordingly. sale_purchase_stock/models/purchase_order.py:10-15
- B2. Sales order's linked purchase orders also include those reachable through the order's stock references. sale_purchase_stock/models/sale_order.py:10-15
- B3. Purchase receipt moves: if the PO line is tied to a sales line and the final destination is a customer or transit location, the move is linked to that sales line (so delivered quantity flows back to the order); routes of the sales line are propagated to the move. sale_purchase_stock/models/purchase_order.py:21-29
- B4. Merging logic: for a procurement from a sales line with no downstream move (dropship-type), only PO lines already tied to that sales line are candidates for merging; otherwise standard merging. sale_purchase_stock/models/purchase_order.py:35-41. (TEST) RFQs are not grouped across orders for dropship even if the vendor is set to group all; sale_purchase_stock/tests/test_unwanted_replenish_flow.py:137-171
- B5. New PO line from a procurement carries the sales line link only when there is no downstream move (dropship), and copies the sales line analytic distribution when present. sale_purchase_stock/models/purchase_order.py:43-51. (TEST) MTO+Buy analytic distribution reaches the PO line: sale_purchase_stock/tests/test_sale_purchase_stock_flow.py:555-576
- B6. Product description on dropship receipts uses the customer's language and hides the vendor PO wording (when PO has a delivery address). sale_purchase_stock/models/stock_move.py:9-15
- B7. Lifecycle: confirming the sales order triggers MTO+Buy procurement that generates a draft PO. Cancelling the order posts an activity on the linked draft PO. (TEST) sale_purchase_stock/tests/test_sale_purchase_stock_flow.py:45-64; decreasing quantity by a user without PO rights also posts an activity/warning on the PO. (TEST) sale_purchase_stock/tests/test_access_rights.py:26-77
- B8. Procurement failure notification also reaches the salesperson of the originating orders in addition to the product's responsible user. sale_purchase_stock/models/stock_rule.py:9-14
- B9. (TEST) Cancelling a PO then re-reserving stock, partial cancellations and quantity changes on MTO orders are covered: test_sale_purchase_stock_flow.py:193-306,374-416,632-659.

## C. Validations, security, multi-company
- C1. No new groups, access rules or ACLs (no security folder). sale_purchase_stock/ (file list)
- C2. Purchase delivery address field on the PO is visible only to salespeople and read-only when locked or when the PO comes from a sales order. sale_purchase_stock/views/purchase_order_views.xml:9-12
- C3. (TEST) A pure salesperson (no PO rights) can decrease a sales line linked to a PO, forecast report accessible. sale_purchase_stock/tests/test_access_rights.py:26-163
- C4. Multi-company: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. Purchase order creation/merge and vendor choice: purchase_stock (procurement rule Buy) and purchase; this module edits merge/link behaviour. sale_purchase_stock/models/purchase_order.py:35-51
- D2. Inventory receipt/delivery moves: stock; delivered quantity of the sales line: sale_stock. sale_purchase_stock/models/purchase_order.py:21-29
- D3. Analytic distribution: sale line -> PO line. sale_purchase_stock/models/purchase_order.py:49-50
- D4. Vendor bill and customer invoice: purchase/account (not touched here).

## E. Configuration that changes outcomes
- E1. Product routes MTO + Buy (and vendor price list); dropship route with stock_dropshipping. (TEST) test_sale_purchase_stock_flow.py:45-49; test_unwanted_replenish_flow.py:137-160
- E2. Vendor "group RFQ" preference (per vendor / all) affects merging except for dropship. (TEST) test_unwanted_replenish_flow.py:161-171; test_sale_purchase_stock_flow.py:601-631
- E3. Warehouse delivery steps (multi-step delivery) affect linking. (TEST) test_sale_purchase_stock_flow.py:170,522,578-600

## F. Effective extension path (modules)
- Depended on by: stock_dropshipping. Counterparts: sale_purchase (sale-line link on purchase lines), purchase_stock, sale_stock.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: multi-company purchase/sales routing; behaviour of location_final_id when not customer/transit.

