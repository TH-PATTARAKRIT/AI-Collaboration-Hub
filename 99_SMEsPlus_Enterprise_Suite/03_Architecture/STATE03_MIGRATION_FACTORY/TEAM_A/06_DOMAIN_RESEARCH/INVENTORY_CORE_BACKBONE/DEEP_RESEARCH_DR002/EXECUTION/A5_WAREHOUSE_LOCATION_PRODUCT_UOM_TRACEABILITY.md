# A5 — Warehouse / Location / Product / UOM / Traceability

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Research warehouse, location, product classification, UOM, lot/serial, package, put-away evidence | Claude (Team A, DR-002) | This artifact; `stock/models/stock_location.py`, `stock_warehouse.py`, `product.py`, `product_strategy.py`; `product/models/product_template.py`, `product_category.py`, `product_uom.py`; `uom/models/uom_uom.py` | 2026-08-31 | Independent Evidence Review (pending) | VERIFIED (direct source citation) | Central to A16 Cross-Proof pack, A10 SaaS boundary |

## 1. Warehouse semantics

`stock.warehouse` fields (exact citations): `reception_steps` (Selection `one_step`/`two_steps`/`three_steps`, default `one_step`), `delivery_steps` (Selection `ship_only`/`pick_ship`/`pick_pack_ship`, default `ship_only`), plus the location fields tied to those steps (`lot_stock_id`, `wh_input_stock_loc_id`, `wh_qc_stock_loc_id`, `wh_output_stock_loc_id`, `wh_pack_stock_loc_id`, `view_location_id`), and generated picking-type fields (`pick_type_id`, `pack_type_id`, `out_type_id`, `in_type_id`, `int_type_id`, `qc_type_id`, `store_type_id`, `xdock_type_id`). Writing `reception_steps`/`delivery_steps` triggers `_update_location_reception`/`_update_location_delivery`, which **rebuild** the warehouse's `stock.rule`/`stock.route` graph — warehouse configuration is not static data, it is a code generator for routing rules.

**No aggregate-quantity fields exist on `stock.warehouse` itself** — all incoming/outgoing/forecast quantities live on `product.product`, context-filtered by `warehouse_id`. A warehouse is a routing/configuration record, not a quantity ledger.

## 2. Physical vs. logical/virtual locations

`stock.location.usage` — Selection, exactly 7 values: `supplier, view, internal, customer, inventory, production, transit` (default `internal`). Per the field's own help text: `supplier`/`customer` are virtual counterpart locations for external parties; `view` is a non-stock-holding hierarchical aggregator; `internal` is physical warehouse space; `inventory` is the "Inventory Loss" counterpart used by adjustments and scrap; `production` is the BOM-consumption/production counterpart; `transit` is the inter-company/inter-warehouse counterpart. This is the authoritative answer to DR-002 §5's "transit/loss/scrap/customer/vendor/production locations where evidenced" question — all five are evidenced, exactly as named above (scrap uses the `inventory` usage value, not a separate `scrap` value).

## 3. Multi-warehouse / company

- `stock.warehouse.company_id` scopes a warehouse to one company.
- GROUP A's Scenario 11 finding (E2E Lifecycle Map, independently unrebutted): "Branch" in this codebase's Thai-localization layer is a **child `res.company` record**, not a warehouse/location dimension — and a completely separate "Thai Tax Branch" `Char` field exists on `res.partner` with **zero structural connection** to the company hierarchy. This is a material SaaS/multi-entity finding, carried into A10.
- No branch-level field or logic exists anywhere in the core `stock` movement models — `company_id` is the only organizational scope on `stock.move` itself (GROUP A MOV-46, unrebutted).

## 4. Product inventory-management behavior — stockable / consumable / service (Mandatory Question #7)

This pass's own fresh source reading materially deepens GROUP A's register here:

- `product.template.type` (base `product` module) — Selection, **exactly 3 values**: `consu` ("Goods"), `service` ("Service"), `combo` ("Combo"). There is **no** `'product'` (storable) value coexisting with `'consu'` in this codebase's current field definition.
- The actual storable/non-storable flag is a **separate boolean added by the `stock` module**: `product.template.is_storable` (`compute='_compute_is_storable'`, `readonly=False`, `precompute=True`) — `@api.depends('type')` forces `is_storable = False` whenever `type != 'consu'`. Only `type=='consu'` products can ever be storable; `service` and `combo` never can.
- Gating chain confirmed at three points: (a) `sale_stock`'s `_action_launch_stock_rule()` only launches a stock move when `product.type == 'consu'`; (b) `stock.move._should_bypass_reservation()` returns true (skips quant reservation) when `not product.is_storable`; (c) `stock_account`'s `_should_create_account_move()` requires `is_storable == True` **and** `product.valuation == 'real_time'` before any valuation journal entry is created.
- **Reconciliation of GROUP A's Medium#14** ("product.type literal 'product' alongside 'consu'" — an open unknown in the frozen register): this pass's direct reading of the **current** `product.template.type` field definition finds no `'product'` value in the live Selection. This narrows, but does not fully close, GROUP A's item: the current source-code field definition is confirmed 3-way (`consu`/`service`/`combo`); whether `'product'` ever appears as **legacy data** in the dump (not as a field option) is a distinct question this pass could not test (DB restore blocked, see A2). Recorded in A14 as **PARTIALLY VERIFIED**, not fully resolved.

## 5. Product Category relationship

- Base `product.category` (in `product` module) has **zero** inventory/costing fields — confirmed by full-file read (70 lines: only `name`, `complete_name`, `parent_id`, `child_id`, `product_count`, `product_properties_definition`).
- All Inventory-relevant category fields are added by `stock` (`route_ids`, `removal_strategy_id` → `product.removal` model with FIFO/LIFO/Closest-location/FEFO/Least-Packages methods, `putaway_rule_ids`, `packaging_reserve_method`) and `stock_account` (`property_valuation`, `property_cost_method`, `property_stock_journal`, `property_stock_valuation_account_id`, `property_price_difference_account_id`, `anglo_saxon_accounting` — see A9 for full valuation detail).

## 6. UOM and conversion — see A3 §3 for full detail

Summary cross-reference: no `uom.category` model; self-referential `uom.uom.relative_uom_id` tree; global (not per-UoM) rounding precision. This is a structural deviation from textbook Odoo that must be flagged to any future Team B design work — assuming a `uom.category` table exists in reference data would be incorrect for this codebase.

## 7. Lot/serial

`product.template.tracking` — Selection, exactly 3 values: `serial` ("By Unique Serial Number"), `lot` ("By Lots"), `none` ("By Quantity") — required, default `none`. Added by `stock` (not present in base `product`). `_compute_tracking()` forces `tracking='none'` whenever `not is_storable` — a non-storable product can never carry lot/serial tracking, consistent with the storable-gating chain in §4. `stock_account.product.template.lot_valuated` is forced `False` when `tracking=='none'` — per-lot valuation is only possible for tracked products (see A9).

## 8. Expiration

Not directly inspected this pass (out of the 6-topic scope assigned to the product/UOM research agent); `product_expiry` module exists in the source tree (confirmed in A1's landscape scan) but its fields were not read. Registered `EVIDENCE_MISSING — NOT YET RESEARCHED` in A14, not silently assumed.

## 9. Package / handling unit

- **No `product.packaging` model exists in this codebase** (confirmed by exhaustive grep — zero hits for `_name = 'product.packaging'` anywhere in the source tree). This differs from GROUP A's own §08 Package findings, which described `stock.package`/`stock.package.history` (the *physical container* concept) — that model set is confirmed still present and unaffected by this finding; what is **absent** is the older *product-level packaging definition* concept (e.g. "this product ships in boxes of 12").
- Instead: (a) `product.template.uom_ids` (Many2many to `uom.uom`, "Additional packagings for this product") — a pack quantity is now literally represented as an extra `uom.uom` record (e.g., "Pack of 6") linked to the product, with the pack size carried by the UoM's own `relative_factor`; (b) `product.uom` (`_name='product.uom'`, distinct from `uom.uom`) — a barcode-per-packaging link model (`uom_id`, `product_id`, `barcode`, unique-barcode constraint whose own error message calls it "packaging").
- `product.category.packaging_reserve_method` (Selection `full`/`partial`, default `partial`) governs whether partial packagings can be reserved.
- This is a genuinely new structural finding for the DR-002 package (GROUP A's own research did not reach this specific product-level packaging model question) — registered as a positive deepening, not a contradiction of GROUP A's `stock.package` findings.

## 10. Owner/consignment

Not directly inspected this pass beyond confirming `owner_id` is part of the `stock.quant` bin key (§A3) — full consignment-workflow evidence (e.g., a dedicated consignment model or wizard) was not traced. Registered `EVIDENCE_MISSING — NOT YET RESEARCHED` in A14.

## 11. Put-away

Lives in `stock/models/product_strategy.py` (`product.removal` for removal strategy; put-away rules via `stock.putaway.rule`, linked from `product.category.putaway_rule_ids`). GROUP A's PA-01/02/04/06 findings (specificity-ordering: package-type > product > exact-category > any-category, expressed as a sort-lambda, not a stored priority field) are reused DELTA-FIRST — not independently re-verified this pass, no contrary evidence found.

No Evidence = No Progress. DELTA-FIRST.
