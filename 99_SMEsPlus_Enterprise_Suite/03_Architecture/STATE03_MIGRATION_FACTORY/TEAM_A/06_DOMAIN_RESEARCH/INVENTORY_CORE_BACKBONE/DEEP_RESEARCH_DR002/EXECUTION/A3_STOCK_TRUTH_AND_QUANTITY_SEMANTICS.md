# A3 — Stock Truth / Quantity Semantics

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Exhaustively research primary vs. derived quantity concepts, owners, and mutation triggers | Claude (Team A, DR-002) | This artifact; `stock/models/stock_quant.py`, `stock/models/stock_move.py`, `stock/models/product.py` | 2026-08-31 | Independent Evidence Review (pending) | VERIFIED (direct source citation) | Central input to A16 Cross-Proof pack |

## 1. What "Stock Truth" is — the canonical answer to DR-002 Mandatory Question #1

**Stock Truth is one row of `stock.quant`**, keyed on `(product_id, location_id, lot_id, package_id, owner_id)`. It is not a transaction log and not a running balance computed on read — it is a stored, mutable bin-level record. Everything else (on-hand totals, forecasts, availability) is derived by summing or computing over `stock.quant` and `stock.move`/`stock.move.line` records. This is GROUP A's own QNT-01 finding, independently re-confirmed this pass by direct reading of `stock/models/stock_quant.py`.

## 2. The six quantity concepts — owner / lifecycle / source of truth / derived-from / mutation trigger / correction path / cross-domain consumer

| Concept | Field(s) | Owner / Source of Truth | Derived From | Mutation Trigger | Correction Path | Cross-domain Consumer |
|---|---|---|---|---|---|---|
| **On-hand** | `stock.quant.quantity` (stored) | Inventory | Primary (not derived) | `stock.move.line._synchronize_quant(action="available")` at `_action_done()` | Physical count (`inventory_quantity` → applied) or manual `product.qty_available` inverse write | `product.product.qty_available` (compute, `@api.depends('stock_move_ids.product_qty','stock_move_ids.state','stock_move_ids.quantity')`) |
| **Reserved / Allocated** | `stock.quant.reserved_quantity` (stored) | Inventory | Primary (not derived) | `stock.quant._update_reserved_quantity()`, called from `stock.move._action_assign()` | Unreserve (`_do_unreserve`) on cancel or re-assign | Feeds `available_quantity` compute |
| **Available / Free-to-promise** | `stock.quant.available_quantity` (computed, not stored) | Inventory | `quantity - reserved_quantity` | Recomputed on read | N/A (pure compute) | `product.product.free_qty = qty_available - reserved_quantity - expired_unreserved_qty` |
| **Demand (planned)** | `stock.move.product_uom_qty` | Inventory (move-local) | Primary — user/rule-set at move creation | Direct write on move creation/edit while `state` allows | Edited while move is open; frozen once `done` | `sale.order.line`/`purchase.order.line` read this to compute their own delivered/received quantities |
| **Real quantity (base UoM)** | `stock.move.product_qty` | Inventory | Computed+stored, `@api.depends('product_id','product_uom','product_uom_qty','state')` — UoM conversion of `product_uom_qty` | Recomputed whenever demand/UoM changes | Inverse setter (`_set_product_qty`) **deliberately raises `UserError`** if written directly — a hard guard against bypassing the compute | Internal only |
| **Actual / Picked / Done quantity** | `stock.move.quantity` | Inventory | Computed+stored, `@api.depends('move_line_ids.quantity','move_line_ids.product_uom_id')` — sum of move-line-level actuals converted to move UoM | Recomputed whenever a `stock.move.line.quantity` changes | This is **the** field that drives backorder/extra-move logic in `_action_done` — its meaning is genuinely state-dependent (before `done`: "picked so far"; at `done`: "what actually moved"), confirming GROUP A's MOV-02/03/13/19 finding independently | `sale.order.line._prepare_qty_delivered()` and `purchase.order.line._compute_qty_received()` both sum this field, filtered to `state=='done'` moves only |
| **Incoming / Outgoing** | `product.product.incoming_qty` / `outgoing_qty` (computed, not stored) | Inventory | Sum of non-done moves into/out of the relevant location context | Recomputed on read, contextual on `warehouse_id`/`location` | N/A (pure compute) | `virtual_available = qty_available + incoming_qty - outgoing_qty` (Forecasted) |
| **Forecasted** | `product.product.virtual_available` (computed) | Inventory | `qty_available + incoming_qty - outgoing_qty`, minus expired-lot unreserved qty | Recomputed on read | N/A | Sales/Purchase replenishment logic (MTS/MTO decisions) |
| **Inventory-count / Physical** | `stock.quant.inventory_quantity`, `inventory_quantity_auto_apply`, `inventory_diff_quantity` | Inventory | User-entered counted value vs. system theoretical value | Manual entry during a physical count, applied via inverse setter | The **only** path to directly overwrite `quantity` outside normal move flow — see A7 | None (Inventory-internal correction mechanism) |

## 3. UOM conversions and precision (Mandatory Question #4/#6 partial)

- All UoM math funnels through `uom.uom._compute_quantity(qty, to_unit, round=True, rounding_method='UP', raise_if_failure=True)`: `qty * self.factor / to_unit.factor`.
- **Deviation from textbook Odoo, material finding**: this checkout has **no `uom.category` model**. `uom.uom` is self-referential via `relative_uom_id` (parent-store tree); a unit's absolute `factor` is computed recursively from its chain of `relative_factor` values up to a root reference unit. "Same category / convertible" is determined structurally (`_has_common_reference`, comparing `parent_path` prefixes), not by a stored category-membership field. Any Team B design that assumes a `uom.category` table exists in the reference data will be building against a model this source does not actually have.
- **Rounding precision is global, not per-UoM**: `uom.uom.rounding` is computed from one shared `decimal.precision` record named `'Product Unit'` — every UoM in the system shares the same rounding precision. This differs from versions where each UoM stores its own rounding independently.
- No explicit "UoM type" (reference/bigger/smaller) selection field exists — it is inferred from `relative_uom_id` presence and the magnitude of `relative_factor`.

## 4. Negative quantity / return semantics (Mandatory Question #5, quantity half)

- A `stock.move` with negative `product_uom_qty` is transformed during `_action_confirm()`: `location_id`/`location_dest_id` are swapped, `picking_type_id` switched to `picking_type_id.return_picking_type_id`, `procure_method` forced to `make_to_stock`. There is no separate "negative quantity" data type — the sign is resolved into a location-swap before the move proceeds.
- Distinct from this: `stock.picking.return_id`/`return_ids` and `stock.move.origin_returned_move_id` (the actual return-tracking primitive, populated by the `stock.picking.return` wizard, confirming GROUP A's RET-01–RET-10 findings).
- `stock.quant.quantity` itself can legitimately go negative in the **Forecasted** sense (virtual_available), and GROUP A's NEG-05/06 confirmed no DB CHECK constraint blocks negative `stock_quant.quantity` at the physical level either — see A2, A13.

## 5. Partials / backorders / over-under fulfillment (Mandatory Question #5, partial half)

- `stock.move._create_backorder()` splits a move when `quantity < product_uom_qty` (rounding-compared at "Product Unit" precision) — this is a **move-level**, not document-level, mechanism; `stock.picking._create_backorder()` operates on top of it to split the picking.
- `stock.picking.type.create_backorder` (Selection `ask`/`always`/`never`) controls whether the split is prompted, automatic, or suppressed — a per-operation-type policy, not a per-transaction choice.
- **Over-fulfillment is not guarded anywhere in this codebase** — confirmed independently by this pass's own reading of `purchase.order.line._compute_qty_received()` (reads `move.quantity` on done moves with no ceiling at `product_qty`) and by GROUP A's DB-forensics-corroborated Exception #4 finding. This is a genuine, evidence-supported invariant gap, not a guess — see A13.
- Sale-side over-delivery clamping on `qty_to_deliver` was flagged by GROUP A as not fully traced (their §05 item 1) — **this pass did not close that specific trace either**; it remains open in A14 (carried forward, not silently dropped).

## 6. Concurrency / race-sensitive facts

- `stock.quant._merge_quants()` exists specifically to reconcile duplicate rows created by concurrent transactions racing to create the same `(product, location, lot, package, owner)` bin — a cleanup mechanism, not a prevention mechanism (no unique DB index enforces the bin key, per A2).
- No DB-level optimistic/pessimistic locking evidence was found in the models read this pass; ORM-level row locking (`SELECT ... FOR UPDATE`) was not traced in the time available — registered as an open item in A14 (N-CONC-01).

## 7. Derived vs. stored — summary table

| Stored (primary) | Computed (derived, not stored) | Computed AND stored (hybrid) |
|---|---|---|
| `stock.quant.quantity`, `reserved_quantity`, `inventory_quantity` | `stock.quant.available_quantity`, `on_hand` (search-only) | — |
| `stock.move.product_uom_qty`, `picked` | `stock.move.availability`, `forecast_availability` | `stock.move.product_qty`, `quantity` |
| — | `product.product.qty_available`, `virtual_available`, `free_qty`, `incoming_qty`, `outgoing_qty` | — |

This confirms and refines GROUP A's own "quantity semantics are state-dependent, not merely field-dependent" synthesis finding with exact compute/store citations.

No Evidence = No Progress. DELTA-FIRST.
