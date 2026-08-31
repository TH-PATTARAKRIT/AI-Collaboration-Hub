# A4 — Movement / State / Event Lifecycle Evidence

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Research full lifecycle of receipt, delivery, transfer, reservation, execution, cancel, return, scrap, adjustment, backorder | Claude (Team A, DR-002) | This artifact; `stock/models/stock_move.py`, `stock_picking.py`, `stock_scrap.py` | 2026-08-31 | Independent Evidence Review (pending) | VERIFIED (direct source citation) | Central to A16 Cross-Proof pack |

## 1. `stock.move` state machine

```
draft → waiting / confirmed → partially_available / assigned → done
                                                      ↓
                                                   cancel (from any non-done state)
```

Seven values total (`draft, waiting, confirmed, partially_available, assigned, done, cancel`) — one more than the classic 6-state Odoo machine (`partially_available` is used when only some of a move's demand could be reserved). Independently confirmed by this pass's own reading of `stock/models/stock_move.py`, consistent with GROUP A's MOV-07.

## 2. Key transition methods (exact citations)

| Method | Transition | Notable behavior |
|---|---|---|
| `_action_confirm(merge=True, merge_into=False, create_proc=True)` | draft → confirmed/waiting | Creates procurements for `make_to_order` moves via `stock.rule.run()`; contains the negative-demand → return transform (location swap, see A3 §4) |
| `_action_assign(force_qty=False)` | confirmed/waiting/partially_available → assigned/partially_available | Creates `stock.move.line` records, reserves quants |
| `_action_cancel()` | any non-done → cancel | Unreserves; propagates to `move_dest_ids` if `propagate_cancel` set; respects `stock.cancel_moves_origin` system parameter. GROUP A's MOV-31 finding (independently confirmed this pass): the guard checked before allowing cancellation is an **all-or-nothing check over the whole recordset** (`any(move.state=='done' and move.location_dest_usage != 'inventory' for move in self)`), not evaluated per-move — a real, source-confirmed batch-cancellation nuance |
| `_action_done(cancel_backorder=False)` | → done | Auto-confirms draft moves first; cancels moves with `quantity<=0` or not `picked` (unless `is_inventory`); calls `_create_backorder()` **before** marking `state='done'`; propagates to `move_dest_ids` |
| `_create_backorder()` | (internal, called from `_action_done`) | Splits the move (`_split(qty_split)`) when `quantity < product_uom_qty` |
| `_merge_moves()` | (internal) | Silently merges identical-characteristic moves — GROUP A's MOV-40 finding: **move cardinality is not stable relative to source document lines** (a `sale.order.line` with one demand line can end up backed by a merged/split set of `stock.move` records that doesn't 1:1 match the commercial line) |

## 3. `stock.picking` state — fully derived, not independently set

`stock.picking.state` is `compute='_compute_state', store=True`, `@api.depends('move_type','move_ids.state','move_ids.picking_id')` — six values (`draft, waiting, confirmed, assigned, done, cancel`), aggregated from per-picking move-state flags (`any_draft`, `all_cancel`, `all_cancel_done`, `all_done_are_scrapped`, `any_cancel_and_not_scrapped`). There is no independent picking-level state transition — the picking is always a read-out of its moves.

## 4. Receipt / Delivery / Internal Transfer

- Distinguished by `stock.picking.type.code` (`incoming` / `outgoing` / `internal`), a **string literal**, not a dedicated enum-backed model relationship — GROUP A's own External Dependency register flags `picking_type.code` string-literal comparisons as a migration technical-ID coupling risk (§10), independently corroborated by this pass's own reading of `sale_stock`/`purchase_stock` (both branch on `product.type` string literals, e.g. `!= 'consu'`, the same pattern).
- Receipt: `purchase.order.button_approve()` → `_create_picking()` → `_prepare_picking()` finds/creates a non-done/non-cancel `stock.picking`, then `order_line._create_stock_moves(picking)`, then `_action_confirm()`/`_action_assign()`.
- Delivery: `sale.order._action_confirm()` → `order_line._action_launch_stock_rule()` → `stock.rule.run()` (procurement-group dispatch, not a direct `create()` — this is the **Sale/Purchase asymmetry** GROUP A's GRPA-01/02 vs. GRPA-04/05 identified and this pass independently re-confirmed: Purchase creates `stock.move` directly/synchronously; Sale creates it indirectly through the rule engine).
- Internal Transfer: same `stock.move`/`stock.picking` machinery, `picking_type.code == 'internal'`, no commercial document driving it by default.

## 5. Reservation / Release / Movement Confirmation / Execution/Done

Covered in detail in A3 §2 (quantity mechanics). State-wise: reservation happens during `_action_assign` (confirmed/waiting → assigned/partially_available); release/unreserve happens during `_action_cancel` (`_do_unreserve`) or when a move is re-assigned; execution/done happens during `_action_done`, which is the single choke point that also triggers backorder-splitting and valuation (`_set_value()`, see A9).

## 6. Cancel / Return / Reversal / Scrap / Adjustment / Correction / Backorder

| Concept | Model / Mechanism | Persistent record? |
|---|---|---|
| Cancel | `stock.move._action_cancel()` / `stock.picking` (derived) | Yes — `state='cancel'` on existing records, not a new document |
| Return | `stock.picking.return` wizard (TransientModel) → creates new `stock.move` records with `origin_returned_move_id` set, `stock.picking.return_id` linking back | Yes — new `stock.move`/`stock.picking` records; the wizard itself is not persistent (GROUP A RET-01–10) |
| Reversal (financial) | Out of Inventory's ownership — see A9 boundary statement | Accounting-owned |
| Scrap | `stock.scrap` (`_name='stock.scrap'`) — dedicated model, source `usage='internal'`, destination `usage='inventory'` (the "Inventory Loss" virtual location) | Yes — `stock.scrap` record + generated `stock.move` (`stock.move.scrap_id` links back) |
| Adjustment | `stock.quant.inventory_quantity` → applied | See A7 |
| Correction (post-done) | **No "un-confirm a done picking" action exists anywhere in this source** (GROUP A finding, independently unrebutted by this pass) — the only path to correct a done movement is a new Return | N/A — corrections are always new records, never retroactive edits to done moves |
| Backorder | `stock.picking.backorder_id`/`backorder_ids` — self-referencing, **not a separate model** (GROUP A BO-01–11, confirmed) | Yes — a new `stock.picking` record chained via `backorder_id` |

## 7. Retry/duplicate implications

See A6 §5 (duplicate/retry safeguards are documented alongside route/procurement dispatch, since that is where this pass found the concrete evidence). Summary forward-reference: all observed guards are **quantity-remaining-based merges/no-ops**, not a unified idempotency-key mechanism; `_action_confirm()`'s own first-line guard (`if move.state != 'draft': continue`) makes re-confirming an already-processed move a safe no-op at the move level.

No vendor state machine is proposed here as SMEsPlus target design — this document records what the source evidences, per the DR-002 clean-room boundary.

No Evidence = No Progress. DELTA-FIRST.
