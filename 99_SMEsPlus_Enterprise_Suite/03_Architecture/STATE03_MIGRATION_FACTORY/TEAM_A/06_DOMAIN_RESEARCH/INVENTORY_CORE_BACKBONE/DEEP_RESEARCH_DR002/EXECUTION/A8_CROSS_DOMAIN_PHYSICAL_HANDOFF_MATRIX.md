# A8 — Sales / Purchase / Manufacturing Physical Handoff Matrix

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Research E2E handoffs Sale→Inventory, Purchase→Inventory, Manufacturing raw material→WIP→FG, returns/cancellation, partials, fact ownership at each boundary | Claude (Team A, DR-002) | This artifact; `sale_stock/models/`, `purchase_stock/models/`, `mrp/models/` | 2026-08-31 | Independent Evidence Review (pending) | VERIFIED (direct source citation) | Central input to A16 Cross-Proof pack |

## 1. Sale → Inventory

| Fact | Evidence |
|---|---|
| Link | `sale.order.line.move_ids` (One2many to `stock.move`) ⇄ `stock.move.sale_line_id` (Many2one) |
| Trigger | `SaleOrder._action_confirm()` → `order_line._action_launch_stock_rule()` → builds `Procurement` tuples → `stock.rule.run()` |
| Re-trigger on qty change | `SaleOrderLine.create()`/`.write()` (when `product_uom_qty` changes on a `state=='sale'` line) also call `_action_launch_stock_rule()` |
| Delivered-qty computation | `_prepare_qty_delivered()` sums `move.quantity` on outgoing/incoming moves, **only `state=='done'`** moves counted; `qty_delivered_method='stock_move'` for storable/consu products |
| Partial delivery representation | `sale.order.delivery_status` (Selection `pending`/`started`/`partial`/`full`, computed from `picking_ids` states + `order_line.qty_delivered`) — a **header-level**, not line-level, persisted concept |
| Policy control | `sale.order.picking_policy` (`direct` vs `one`) — release-partial-immediately vs. wait-for-all-lines-ready |
| Return handling | Generic core wizard (`stock/wizard/stock_picking_return.py`), not `sale_stock`-specific; `sale_stock` only asserts eligibility (`StockPicking._can_return()` — any picking tied to a confirmed sale order is returnable) |
| Return-qty exclusion | `to_refund` boolean on `stock.move` marks whether a returned qty subtracts from `qty_delivered` |

**Fact ownership at this boundary**: Sales owns commercial intent/commitment (`product_uom_qty` demand); Inventory owns whether/when physical fulfillment actually occurred (`quantity` on done moves). Sales reads Inventory's done-move quantities to compute its own delivered/returned figures — a one-directional read, not a shared-writable fact.

## 2. Purchase → Inventory

| Fact | Evidence |
|---|---|
| Link | `purchase.order.line.move_ids` (One2many, "Reservation") ⇄ `stock.move.purchase_line_id`; also `stock.move.created_purchase_line_ids` (M2M, used when a downstream MTO procurement auto-creates a PO line) |
| Trigger | `PurchaseOrder.button_approve()` → `_create_picking()` → finds/creates picking → `order_line._create_stock_moves(picking)` → `_action_confirm()`/`_action_assign()` |
| Re-trigger on qty change | `PurchaseOrderLine.create()`/`.write()` → `_create_or_update_picking()` (reuses existing open picking on the order, else creates one) |
| Received-qty computation | `_compute_qty_received()` reads `move.quantity` on **done** moves — **no ceiling at ordered qty** (over-receipt is simply a larger `move.quantity` on the same move, not specially detected or blocked); return moves (`move._is_purchase_return()`) subtracted |
| Demand-increase handling | `_prepare_stock_moves()` computes `qty_to_attach` (reuse `move_dest_ids`) and `qty_to_push` (extra beyond already-linked); appends a new "extra move" when `qty_to_push > 0` |
| Duplicate-move guard | `_get_qty_procurement()` sums existing move quantities to prevent re-creating moves for already-covered demand |

**Fact ownership at this boundary**: Purchase owns commercial commitment (`product_qty` ordered); Inventory owns physical receipt fact. Unlike Sales, Purchase creates the `stock.move` directly and synchronously (A6 §6 asymmetry) — a structurally different integration shape for what is conceptually the mirror-image handoff.

## 3. Manufacturing → Inventory (raw material → WIP → finished goods)

| Fact | Evidence |
|---|---|
| `mrp.production` state | Selection `draft`/`confirmed`/`progress`/`to_close`/`done`/`cancel` — a **distinct** state machine from `stock.move`'s own 7-state machine (A4 §1); the MO's state and its component/FG moves' states are related but not identical vocabularies |
| Raw-material consumption link | `stock.move.raw_material_production_id` (→ MO), `stock.move.bom_line_id` (→ specific BOM component line), `stock.move.workorder_id` (→ specific operation) |
| Consumption quantity assignment | `MrpProduction._set_qty_producing()` calls `move._set_quantity_done(new_qty)` and sets `move.picked=True` |
| Component move value-building | `_get_moves_raw_values()` explodes `bom_id` via `bom_id.explode(...)` → `_get_move_raw_values()` sets `raw_material_production_id`, `bom_line_id`, `manual_consumption` |
| FG receipt — the exact recording move | `MrpProduction._post_inventory()`: for each finished move matching `production.product_id` and not done/cancelled, `move.quantity = order.product_uom_id.round(order.qty_producing - order.qty_produced, ...)`, then `_action_done(...)` posts it — **this is the specific `stock.move` that records the FG receipt into `location_dest_id`** |
| Byproducts | `move_byproduct_ids` — computed subset of `move_finished_ids`, one move per non-skipped `bom_id.byproduct_ids`, tagged `byproduct_id` |
| Backorder / partial production | `_split_productions()` creates MO backorders (`_get_backorder_mo_vals()` clears `move_raw_ids`/`move_finished_ids` on the split copy), driven by `_get_quantity_produced_issues()`/`_get_quantity_to_backorder()` and a `mrp.action_mrp_production_backorder` wizard |
| Orchestration | `button_mark_done()`: `workorder_ids.button_finish()` → `_split_productions()` for flagged MOs → `_post_inventory(cancel_backorder=True)` for both halves → `state='done'` |

**Fact ownership at this boundary**: Manufacturing owns the BOM/routing/WIP concept; Inventory owns the actual component-consumption and FG-receipt stock facts, recorded as ordinary `stock.move` records tagged back to the MO — the same movement primitive used everywhere else in the codebase, not a parallel manufacturing-specific ledger.

## 4. Returns / cancellation interactions across all three boundaries

- Sale-side and vendor-side returns both funnel through the same generic core wizard/mechanism (A4 §6) — no domain-specific return logic exists in `sale_stock`/`purchase_stock` beyond eligibility checks.
- Manufacturing does not have its own "return" concept distinct from the generic Inventory return mechanism for its consumed/produced stock.
- Cancellation: Sale-side cancellation-after-confirmation is source-verified straightforward; GROUP A's frozen evidence records Purchase-side post-confirmation cancellation cascade as closed by their CORR-003 (traced to `purchase_stock/models/purchase_order.py` L186-233, "state-partitioned... provably symmetric-in-effect with Sale's") — reused DELTA-FIRST, not independently re-traced line-by-line this pass, no contrary evidence found.

## 5. Partials — cross-boundary summary

All three domains represent "partial" differently: Sale as a header-level `delivery_status` enum; Purchase as an unclamped `qty_received` that simply reflects whatever moves are done so far; Manufacturing as an explicit MO-split (`_split_productions()`) creating a genuinely separate backorder MO record. There is no single shared "partial fulfillment" primitive across the three domains — each integration module re-implements its own partial-representation logic on top of the shared `stock.move`/backorder mechanism.

No target design for Sale/Purchase/MRP is proposed here — this document captures neutral handoff facts and unknowns only, per DR-002 §7/A8's explicit instruction.

No Evidence = No Progress. DELTA-FIRST.
