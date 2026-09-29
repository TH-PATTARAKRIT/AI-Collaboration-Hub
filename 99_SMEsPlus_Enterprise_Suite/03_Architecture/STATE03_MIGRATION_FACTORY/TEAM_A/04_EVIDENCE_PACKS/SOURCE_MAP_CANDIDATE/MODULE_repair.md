# Source Map (candidate) — `repair`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `repair` |
| Display name | Repairs |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d3dc6292965a1ea5` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/repair/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `sale_stock`, `sale_management`
- Direct dependents in 300-module list (3): `mrp_repair`, `mrp_subcontracting_repair`, `purchase_repair`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `l10n_din5008_repair`, `pos_repair`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / Repair damaged products
- Inventory of user-facing artifacts (counts): menu items 8, views 18, window actions 7, server actions 1, reports 1, mail templates 0, scheduled jobs 0, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `stock.warn.insufficient.qty.repair` (Warn Insufficient Repair Quantity); `repair.order` (Repair Order); `repair.tags` (Repair Tags)
- Objects extended from other modules (17): `stock.warn.insufficient.qty`, `mail.thread`, `mail.activity.mixin`, `product.catalog.mixin`, `stock.warehouse`, `sale.order`, `sale.order.line`, `stock.move.line`, `account.move.line`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.traceability.report`, `product.product`, `product.template`, `stock.lot`, `stock.forecasted_product_product`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 1 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `repair.order` ← Community: `l10n_din5008_repair`, `mrp_repair`, `purchase_repair`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `stock.warn.insufficient.qty`, `mail.thread`, `mail.activity.mixin`, `product.catalog.mixin`, `stock.warehouse`, `sale.order`, `sale.order.line`, `stock.move.line`, `account.move.line`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.traceability.report`, `product.product`, `product.template`, `stock.lot`, `stock.forecasted_product_product`

## 6. Actions / states / validation / automation / security
- State fields found: `repair.order` → ['draft', 'confirmed', 'under_repair', 'done', 'cancel']
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 1); access rows 3

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 77 of 77 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: repair
Source revision: 19.0.post20260921 (Odoo 19 Community). Read-only trace; neutral business language; no code copied.

## A. Capabilities / activation
- Repair orders for customer or internal products: parts to add, remove or recycle, warranty flag, technician notes, quotation to customer, printable quotation report, availability of parts, traceability. repair/__manifest__.py:5-22
- Core when installed: it is a standalone app (application flag) requiring sale_stock and sale_management; not auto-installed. repair/__manifest__.py:23,42
- On install, every warehouse without one gets a "Repairs" operation type (sequence prefix warehouse-code/RO/, barcode, lot creation and existing-lot use enabled), and a make-to-order rule for the repair operation. repair/__init__.py:9-17; repair/models/stock_warehouse.py:15-25,27-52,78-98; repair/data/repair_data.xml:9-24
- Optional pieces: sale products with service tracking "Repair Order" auto-create a repair when the sale order is confirmed (conditional on that product setting); catalog picker for parts; kits, purchases, manufacturing links live in bridge modules (see F). repair/models/product.py:52-57; repair/models/sale_order.py:90-112
- Menus: Repairs app (inventory user), reporting and configuration (inventory manager), tags menu only in debug mode group. repair/views/repair_views.xml:381-398

## B. Business objects and relationships
- Repair order: reference (from operation-type sequence), company, status, priority, customer, responsible, tags, warranty, scheduled date, product to repair + quantity + unit + lot/serial, operation type, stock references, locations, parts (stock movements), sale order and line, source transfer (a return), availability indicators, custom properties from the operation type. repair/models/repair.py:22-200
- Parts are ordinary stock movements carrying a repair link and a line type: add (from stock to the production-type location), remove (from that location to the "removed parts" destination, default inventory-loss), recycle (to the recycle destination, default stock). repair/models/stock_move.py:6-10,16-21,40-62
- Product to repair must be a consumable-type product (storable or not); qty defaults from the linked return transfer (by lot for tracked goods), serial-tracked goods forced to quantity 1. repair/models/repair.py:84-87,205-216,403-404
- Source transfer: repair can be started from a return (customer, lot and quantities come from the transfer); warning if warehouses of return and repair locations differ. repair/models/repair.py:180-186,223-239,358-365; repair/models/stock_picking.py:154-170; repair/tests/test_repair.py:499-554 (TEST)
- Operation type ("repair_operation"): defaults for component source, product source/destination, added-parts destination (production location), removed-parts destination (inventory-loss location), recycle destination; counters (confirmed, under repair, ready, late). repair/models/stock_picking.py:14-64,65-114; repair/models/stock_warehouse.py:37-51
- Locations on the repair are computed from the operation type and pushed to part movements when changed. repair/models/repair.py:264-282,406-409; repair/models/stock_move.py:194-215
- Availability indicator: parts availability (Available / Not Available / expected date), late if forecast date after schedule date; remove/recycle parts always count as available. repair/models/repair.py:284-324; repair/models/stock_move.py:23-29
- Sale order link: repair belongs to at most one sale order; add-type parts become sale lines automatically (once the sale order exists); quantities on repair drive sale line quantities; sale-line changes do not flow back to parts. repair/models/repair.py:168-177,687-710; repair/models/stock_move.py:90-131,142-189; repair/tests/test_repair.py:317-422 (TEST)
- Sale confirmation with a "Repair Order" service line creates one confirmed repair per line (quantity above one does not create several); cancelling or zeroing that line cancels the repair; restoring quantity re-confirms a cancelled one. repair/models/sale_order.py:26-29,66-83,90-119; repair/tests/test_repair.py:317-422 (TEST)
- Warranty flag zeroes sales price of parts; toggling recomputes prices. repair/models/repair.py:64-66,412-413,669-675; repair/models/stock_move.py:153-156
- Lifecycle: New(draft) -> Confirmed -> Under Repair -> Repaired(done); Cancelled from any non-done; Cancelled -> back to draft. repair/models/repair.py:42-53
  - Confirm (action_validate): blocked by negative part quantities; if product to repair is storable and not enough is present in source location (owner-specific or no owner), a confirmation wizard warns and the user chooses to continue; then parts are confirmed, procure method adjusted (MTO if an MTO rule fits), scheduler triggered. repair/models/repair.py:570-608,621-633; repair/wizard/stock_warn_insufficient_qty.py:15-21
  - Start: confirms first if needed, then Under Repair. repair/models/repair.py:560-565
  - End: only from Under Repair; then done processing. repair/models/repair.py:545-558
  - Done processing: zero-quantity parts cancelled; parts marked picked if none was; sale service line marked delivered when applicable; tracked product to repair requires lot/serial (validation error); creates one movement for the repaired product (from product source to product destination, with owner = customer when the customer's own stock is available), consumption links between used parts and produced lines; all movements completed without backorders; state Repaired. repair/models/repair.py:468-543
  - Cancel: not allowed once Repaired; cancels parts, sets linked sale line quantities to zero. repair/models/repair.py:450-457
  - Set to draft: after cancel, restores parts draft and refreshes sale lines. repair/models/repair.py:459-466
  - Delete: any non-cancelled repair is cancelled first. repair/models/repair.py:424-427
- (TEST) Whole transition matrix incl. warnings and no split of partially done part movements. repair/tests/test_repair.py:170-316 (TEST)
- Parts are not moved via a stock picking; no transfer document is created for repair movements. repair/tests/test_repair.py:170-316 (TEST); repair/models/stock_move.py:217-220
- Partially processed parts are not split on completion. repair/models/stock_move.py:222-226

## C. Validations / constraints / security / multi-company
- Negative quantity blocked at confirm; serial required when finishing tracked products; cancel of done repair blocked; quotation requires a customer and only one quotation per repair; change of unit of measure of a product used in repairs is blocked when other units used. repair/models/repair.py:572-573,494-498,451-452,687-705; repair/models/product.py:34-47
- New lot/serial creation from a repair is refused unless the operation type allows creating lots. repair/models/stock_lot.py:75-80
- Missing production location or inventory-loss location raises a user error when creating warehouse repair types. repair/models/stock_warehouse.py:34-35,66-69; repair/tests/test_repair.py:891-923 (TEST)
- Tag names unique. repair/models/repair.py:791-794
- Company: repair carries company (required, read-only) with company-consistency checks on confirm; multi-company record rule limits to allowed companies. repair/models/repair.py:26,38-41,626-628; repair/security/repair_security.xml:5-9
- Access: inventory users (stock.group_stock_user) have full rights on repair orders, tags and the warning wizard (no delete on wizard). repair/security/ir.model.access.csv:2-4
- Sale-side elevated rights: repairs created from a sale order are created with elevated rights; repair fields on sale order restricted to inventory users. repair/models/sale_order.py:10-14,111-112

## D. Handoffs (owner in brackets)
- Inventory movements and reservation [stock]: parts confirmed/reserved/completed as stock movements; consumption forecast uses the "consuming" notion (add parts count as consuming). repair/models/stock_move.py:191-192; stock/models/stock_move.py:527-560,2441
- Invoicing [sale/account]: parts (add) and the service line appear on a sale order; delivered quantity on sale lines follows the repair-done quantity; lots of used components print on the invoice. repair/models/sale_order.py:53-64; repair/models/stock_move_line.py:9-10; repair/tests/test_repair.py:667-698 (TEST)
- Sales pickings: sale lines linked to repair movements do not generate deliveries. repair/models/sale_order.py:85-88
- Valuation [stock_account]: (TEST) with FIFO real-time parts and anglo-saxon accounting, invoice posts revenue/receivable and cost-of-goods lines (10); (TEST) when the repair destination location has a valuation account, the repair movement itself books stock valuation vs that account and the invoice does not book cost again. repair/tests/test_anglo_saxon_valuation.py:49-88,90-134 (TEST)
- Double-accounting guard: invoice lines are not eligible for stock accounting when a repair "add" movement is already accounted. repair/models/account_move_line.py:7-10
- A sale line whose moves belong to a repair is not treated as having valued stock moves (sale_stock hook). repair/models/sale_order.py:121-123; sale_stock/models/sale_order_line.py:464-468
- Procurement [purchase_stock, mrp via bridge modules]: MTO rule per warehouse; (TEST, by test title only; body not reviewed) reorder rules can be triggered from repair part demand. repair/models/stock_warehouse.py:78-98; repair/tests/test_repair.py:798-857 (TEST)
- Traceability report treats a repair as the source document and follows consumed/produced move lines. repair/models/stock_traceability.py:9-25
- Lot views: per-lot counters of repairs in progress / repaired and shortcuts. repair/models/stock_lot.py:11-53
- Forecast report avoids double-counting quantities bound to both a repair and a sale. repair/report/stock_forecasted.py:10-30
- Reports: repair quotation report. repair/report/repair_reports.xml; repair/report/repair_templates_repair_order.xml
- Point of sale exclusion for repair lines is done in [pos_repair]. pos_repair/models/stock_picking.py:8-9
- No approval workflow, no scheduled jobs, no external event/webhook found in this module.

## E. Configuration that changes outcomes
- Operation type: default locations (component source, product source/destination, removed/recycle destination), lot creation permission, sequence, properties definition. repair/models/stock_picking.py:14-114
- Warehouse default operation type and user's default warehouse select the repair type; if several exist, picker visible. repair/models/repair.py:197-203,638-667
- Product: service tracking "Repair Order" (sale side), storable flag (drives availability warning), tracking type. repair/models/product.py:52-57; repair/models/repair.py:574
- Warranty flag; owner (customer) stock preference on completion. repair/models/repair.py:64-66,500-505
- Accounting configuration of product category and location valuation account (see D). repair/tests/test_anglo_saxon_valuation.py:90-134 (TEST)
- MTO route activation and repair MTO rule procure method (TEST). purchase_repair/tests/test_repair_purchase_flow.py:23-25 (TEST)

## F. Effective extension path (Community modules extending repair objects; names only)
- repair.order: mrp_repair, purchase_repair, l10n_din5008_repair.
- stock.move/stock.move.line, sale.order.line, stock.picking.type, stock.warehouse, stock.lot, product: many modules; repair-aware ones seen: pos_repair (sale lines/pickings), mrp_repair (kits), purchase_repair.
- Bridge with no content: mrp_subcontracting_repair.

## G. Not verified
- Precisely how the repair movements are valued in every cost method (standard/average/FIFO) and account paths beyond the two tests: UNKNOWN — EVIDENCE INSUFFICIENT
- Handling of removed/recycled parts value and scrap accounting: UNKNOWN — EVIDENCE INSUFFICIENT
- Rights of users below inventory user (portal or sales-only) to view repair quotation: UNKNOWN — EVIDENCE INSUFFICIENT
- Multi-company behaviour when repairing a serial that belongs to another company (only a creation test exists): UNKNOWN — EVIDENCE INSUFFICIENT (repair/tests/test_repair.py:699-710)
- Any behaviour depending on the sale_project module's service policy field beyond the explicit code comment: UNKNOWN — EVIDENCE INSUFFICIENT (repair/models/repair.py:488-490)

