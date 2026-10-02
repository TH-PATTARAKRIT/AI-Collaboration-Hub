# U188 — Repair Order: Lifecycle, Parts Consumption, Invoicing Integration
**Unit:** U188 | **Group:** G07 | **Priority:** P2 | **Level:** L3
**Source:** `odoo/addons/repair/` — Odoo Community 19.0.post20260921
**Date:** 2026-10-02 | **Status:** COMPLETE

---

## 1. Model Architecture — Key Change from Prior Versions

In Odoo 19 Community the repair module no longer has a separate `repair.line` model.
Parts and operations are represented as **`stock.move`** records linked to the repair order
via `repair_id` (Many2one on `stock.move`). The move classification is encoded in
`repair_line_type` (Selection: `add` / `remove` / `recycle`).

**Source:** `repair/models/stock_move.py` lines 16–21, `repair/models/repair.py` lines 150–152.

---

## 2. State Machine — `repair.order.state`

| # | State | Label | Trigger |
|---|-------|-------|---------|
| 1 | `draft` | New | Default on create |
| 2 | `confirmed` | Confirmed | `_action_repair_confirm()` |
| 3 | `under_repair` | Under Repair | `action_repair_start()` |
| 4 | `done` | Repaired | `action_repair_done()` |
| 5 | `cancel` | Cancelled | `action_repair_cancel()` |

**Transition logic:**
- `action_repair_start()` (line 560–565): if state != `confirmed`, first calls `_action_repair_confirm()`; then writes `{'state': 'under_repair'}`. This means start can be called directly from draft and will auto-confirm.
- `action_validate()` (line 570–608): checks available stock for storable products; if insufficient, opens a wizard; otherwise calls `_action_repair_confirm()`.
- `action_repair_end()` (line 545–558): validates state == `under_repair`, then delegates to `action_repair_done()`.
- `action_repair_cancel()` (line 450–457): blocked if any RO is in state `done`. Cancels all `move_ids` and sets state to `cancel`.
- `action_repair_cancel_draft()` (line 459–466): resets cancelled RO back to `draft`; also resets move states to `draft`.

**Source:** `repair/models/repair.py`.

---

## 3. Parts Lines — `stock.move` with `repair_line_type`

Each parts/operations line is a `stock.move` record with:

| Field | Purpose |
|-------|---------|
| `repair_id` | FK to `repair.order` |
| `repair_line_type` | `add` (consume part into repair), `remove` (extract part from product), `recycle` (return extracted part to stock) |
| `product_id` | Component/part product |
| `product_uom_qty` | Planned quantity |
| `quantity` | Done quantity (set at completion) |
| `price_unit` | Unit price for invoicing purposes |
| `picked` | Boolean — marks that quantity is confirmed picked |

Location routing per type (defined in `MAP_REPAIR_LINE_TYPE_TO_MOVE_LOCATIONS_FROM_REPAIR`):
- `add`: source = `repair.location_id` (component WH stock), dest = `repair.location_dest_id` (production virtual location)
- `remove`: source = `repair.location_dest_id` (production), dest = `repair.parts_location_id` (scrap/inventory-loss)
- `recycle`: source = `repair.location_dest_id` (production), dest = `repair.recycle_location_id` (WH stock)

**Source:** `repair/models/stock_move.py` lines 6–10, 41–62.

---

## 4. Parts Consumption — `action_repair_done()`

`action_repair_done()` (repair.py lines 468–543) performs the following sequence:

1. Cancels any moves with zero done quantity.
2. For moves not yet marked `picked`, sets `picked = True` on all.
3. For each RO with a `product_id` (storable product to repair):
   a. Checks available qty for the repaired product in `product_location_src_id`, considering partner ownership.
   b. Builds a `stock.move` dict for the repaired product: moves from `product_location_src_id` → `product_location_dest_id`.
   c. The move_line carries `consume_line_ids` linking to all `move_ids.move_line_ids` (traceability of consumed parts).
4. Creates the product moves via `self.env['stock.move'].create(product_move_vals)`.
5. Links each created move back via `repair.move_id`.
6. Calls `all_moves._action_done(cancel_backorder=True)` — validates all moves (parts + product) in one shot.
7. Sets `repair.state = 'done'`.

**Key traceability point:** the `consume_line_ids` field on the product's move_line links it to all consumed component move_lines, enabling lot/serial traceability in Odoo's traceability report.

**Source:** `repair/models/repair.py` lines 468–543; `repair/models/stock_traceability.py`.

---

## 5. Invoicing Integration — Sale Order Bridge

**Odoo 19 has removed `invoice_method` from `repair.order`.** Invoicing is driven entirely through a linked **Sale Order**.

Mechanism:
- `action_create_sale_order()` (repair.py line 446) calls `_create_sale_order()` which:
  - Creates a `sale.order` linked via `repair_order_ids`.
  - Calls `move_ids._create_repair_sale_order_line()` to create SO lines for all `add`-type moves.
- `_prepare_repair_so_line_vals()` (stock_move.py lines 142–157):
  - Sets `product_uom_qty` from move.
  - If `repair.under_warranty` is True, forces `price_unit = 0.0`.
  - Otherwise uses `move.price_unit`.
- Once the SO is confirmed and invoiced, the standard SO invoicing flow applies (account.move from SO lines).

**Reverse flow:** When a SO line with `service_tracking = 'repair'` is confirmed, `_create_repair_order()` auto-creates a confirmed repair order and links it back (sale_order.py lines 90–112).

**Source:** `repair/models/repair.py` lines 677–710; `repair/models/stock_move.py` lines 142–189; `repair/models/sale_order.py`.

---

## 6. Under Warranty (`under_warranty`)

`repair.order.under_warranty` (Boolean, repair.py line 64–66):
- Help text: "If ticked, the sales price will be set to 0 for all products transferred from the repair order."
- When toggled, `write()` calls `_update_sale_order_line_price()` (lines 669–675):
  - Finds all `add`-type moves with a linked SO line.
  - If `under_warranty`: sets `price_unit = 0.0, technical_price_unit = 0.0` on the SO line.
  - Else: recomputes `price_unit` via SO line compute method.
- Also enforced in `_prepare_repair_so_line_vals()` when creating SO lines.

**Source:** `repair/models/repair.py` lines 64–66, 413, 669–675; `repair/models/stock_move.py` line 153–154.

---

## 7. Product Lot/Serial Tracking

- `repair.order.lot_id` (Many2one `stock.lot`, lines 95–99): identifies the lot/serial number of the product being repaired.
- If product tracking != `none`, `lot_id` is **required** before `action_repair_done()` can complete — a `ValidationError` is raised otherwise (repair.py lines 494–498).
- `lot_id` is computed from `picking_id.move_ids.lot_ids` when there is exactly one lot (auto-populate on picking binding).
- `allowed_lot_ids` restricts the available lots to those on the linked return picking.
- `action_generate_serial()` (lines 429–441): generates a new serial number for the repaired product using the product's lot sequence.
- `stock.lot` inverse: `lot.in_repair_count` and `lot.repaired_count` are computed aggregates on `repair.order` filtered by state.

**Source:** `repair/models/repair.py` lines 95–99, 429–441, 494–498; `repair/models/stock_lot.py`.

---

## 8. Multi-Company

- `repair.order.company_id` (Many2one `res.company`, line 38–41): required, read-only, defaults to `self.env.company`.
- `_check_company_auto = True` ensures cross-model company checks propagate.
- `picking_type_id` domain restricted to `('company_id', '=', company_id)` (line 107).
- `_get_picking_type()` (lines 638–667): resolves default repair operation type per (company, user), using `user._get_default_warehouse_id()`.
- On `action_repair_cancel()`, multi-company checks are enforced via `_check_company()` in `_action_repair_confirm()`.

**Source:** `repair/models/repair.py` lines 26, 38–41, 103–108, 621–633, 638–667.

---

## 9. Return Parts — `remove` and `recycle` Types

- `remove` type moves: parts extracted from the repaired product travel from production virtual location → `parts_location_id`.
- Default `parts_location_id` from warehouse setup = **Inventory Loss** location (scrap-equivalent).
- `recycle` type moves: parts extracted but deemed reusable travel to `recycle_location_id`.
- Default `recycle_location_id` from warehouse setup = **WH/Stock** (internal storage), so recycled parts are returned to available inventory.
- `ProductProduct._count_returned_sn_products_domain()` includes `remove`/`recycle` moves to internal locations in serial number return counting.

**Source:** `repair/models/stock_warehouse.py` lines 27–52; `repair/models/stock_move.py` lines 6–10; `repair/models/product.py` lines 27–32.

---

## 10. Account Move / Inventory Valuation

- `account_move_line.py` overrides `_eligible_for_stock_account()` (lines 7–10):
  - For a journal entry line to be eligible for a follow-on stock account entry, it checks: if the underlying stock move is an `add`-type repair move **and** already has an `account_move_id`, the line is **not** eligible again.
  - This prevents double-posting of inventory cost for repair parts that are already accounted for via the SO/invoice path.
- `stock.move._is_consuming()` (stock_move.py lines 191–192): returns `True` for `add`-type repair moves, ensuring they trigger consumption valuation.
- No dedicated repair expense account; parts consumption flows through standard COGS/stock valuation accounts configured on the product.

**Source:** `repair/models/account_move_line.py`; `repair/models/stock_move.py` lines 191–192.

---

## 11. Analytic Integration

- No explicit analytic account (`account.analytic.line`) fields exist on `repair.order` or the underlying `stock.move` in the repair module.
- When a Sale Order is created from a repair order, standard SO line analytic distribution applies if `account_analytic` module is installed.
- No evidence of direct analytic posting on component consumption moves within the repair module itself.

**Source:** Full scan of `repair/models/repair.py`, `repair/models/stock_move.py` — no `analytic` fields found.

---

## 12. Additional Technical Claims

### C12 — Operation Type (`stock.picking.type` with code `repair_operation`)
- `picking_type_id` on `repair.order` is restricted to `code = 'repair_operation'`.
- Each warehouse gets a `repair_type_id` auto-created with specific location defaults.
- The picking type carries `repair_properties_definition` (PropertiesDefinition) for custom fields on repairs.

### C13 — MTO (Make-to-Order) Rule for Parts
- `stock.warehouse` creates a `repair_mto_pull_id` rule with `procure_method = 'make_to_order'`.
- Route: Replenish on Order (MTO), from `default_location_src_id` to `default_location_dest_id`.
- Move creation in confirmed/under_repair state auto-triggers `_adjust_procure_method` and `_trigger_scheduler`.

### C14 — Product Catalog Integration
- `repair.order` inherits `product.catalog.mixin`; allows adding parts via a product catalog UI.
- `_update_order_line_info()` creates or updates `stock.move` records of type `add`.

### C15 — Picking (Return) Binding
- `picking_id` on `repair.order` links the RO to a stock return picking.
- Partner, product, and lot are auto-populated from the linked picking.
- Warning shown if repair location warehouse differs from return picking warehouse.

### C16 — Sequence and Reference
- Repair reference auto-generated from `picking_type_id.sequence_id.next_by_id()` on create.
- A `stock.reference` record is also auto-created and linked via `reference_ids`.

### C17 — Partial Moves at Completion
- `action_repair_end()` does not block on partially-done moves; it calls `action_repair_done()` which passes `cancel_backorder=True` to `_action_done()`.
- Excess/deficit quantities are handled by cancelling backorders, not creating them.

### C18 — Parts Availability Computation
- `parts_availability` and `parts_availability_state` computed from `forecast_availability` on moves.
- States: `available` / `expected` (future date) / `late` (insufficient qty or past scheduled date).
- `remove` and `recycle` type moves are excluded from availability check (their forecast_availability equals product_qty unconditionally).

### C19 — Sale Order Qty Delivered
- `SaleOrderLine._prepare_qty_delivered()` overridden in `repair/models/sale_order.py` (lines 53–64).
- For SO lines with exactly one associated done repair move, `qty_delivered = move.quantity`.
- In `action_repair_done()`: if `service_policy == 'ordered_prepaid'`, `qty_delivered` is set to `sale_order_line.product_uom_qty`.

### C20 — Cancel Propagation to SO
- `action_repair_cancel()` writes `product_uom_qty = 0.0` on the linked SO line (line 455).
- `move_ids._action_cancel()` is called to cancel all part moves.
- `_clean_repair_sale_order_line()` also zeroes SO line qty when a move is unlinked.

### C21 — No Duplicate Stock Valuation
- `StockMoveLine._should_show_lot_in_invoice()` returns True for any repair line type, so lot details appear on invoices from the SO.
- `_eligible_for_stock_account()` guard prevents double-posting.

---

## Evidence Files Cross-Reference

| Claim | Source File | Lines |
|-------|-------------|-------|
| State machine | repair.py | 42–53, 450–633 |
| Parts as stock.move | stock_move.py | 13–21 |
| Location routing | stock_move.py | 6–10, 41–62 |
| action_repair_done | repair.py | 468–543 |
| Sale order invoicing | repair.py, stock_move.py, sale_order.py | 677–710, 142–189 |
| under_warranty | repair.py | 64–66, 669–675 |
| Lot tracking | repair.py | 95–99, 429–441, 494–498 |
| Multi-company | repair.py | 26, 38–41, 103–108 |
| Remove/recycle to stock | stock_warehouse.py | 27–52 |
| Account valuation guard | account_move_line.py | 7–10 |
| MTO rule | stock_warehouse.py | 78–100 |
