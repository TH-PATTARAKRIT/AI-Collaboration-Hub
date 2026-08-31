> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 5-6 of 10 — Cross-Module Event & Dependency Map
> Synthesizes Phases 1-4 and the Phase 5 gap-closure research. Every row cites back to an evidence ID already
> established in those documents — no new source claims are introduced here.

# 06 — CROSS-MODULE EVENT AND DEPENDENCY MAP

## 00 — Method

A "business event" here means a state or quantity change that at least one OTHER module observes or reacts to
(as opposed to a purely internal recompute). Events are grouped by originating module.

## 01 — Events originating in Sales

| Event | Trigger | Source | What changes | Downstream consumers |
|---|---|---|---|---|
| Quotation confirmed | `action_confirm()` | sale_order.py SO-13..16 | `state→'sale'`, `date_order` stamped | `sale_stock._action_confirm()` creates delivery procurement (SO-25 → GRPA-04/05) |
| Delivery procurement launched | line confirmed, `state=='sale'`, `type=='consu'` | sale_order_line.py SVS-06 | `stock.rule.run()` called with a Procurement tuple | `stock.rule._get_rule()`/`_run_pull` creates a `stock.move` (RULE-09/10) |
| SO line quantity increased/decreased (confirmed order) | `write()` on `product_uom_qty` | sale_stock/sale_order_line.py SOL-29 | Re-invokes `_action_launch_stock_rule` for the delta | New/adjusted `stock.move` |
| SO line quantity reduced below delivered | `_update_line_quantity()` | sale_stock/sale_order_line.py SVS-07/SRET-07 | **Blocked** (UserError) for `consu` lines only | User redirected to Inventory's return wizard |
| Order cancelled (confirmed) | `action_cancel()`→`_action_cancel()` | sale_stock/sale_order.py CANC-13/14 | Cancels not-done pickings; done pickings spared | `stock.picking.action_cancel()` — **CLOSED (CORR-003)**: `self.move_ids._action_cancel()` (unfiltered) + `is_locked=True`; confirmed to be generic/shared code, not Sale- or Purchase-specific — see `04_PURCHASE_CAPABILITY_MODEL.md` §04 (traced via the Purchase-side investigation, applies equally here) |
| Order locked | `action_lock()` (auto or manual) | sale_order.py SO-17/21 | `locked=True` | Blocks 8 named line fields (SO-26/27); blocks new procurement runs on `consu` lines (CANC-15) |
| Delivery move done | `stock.move.line._action_done()` | (Inventory-owned, consumed by Sale) | quant on-hand/reserved change | `sale_order_line._compute_qty_delivered()` (`'stock_move'` method, SOL-26) recomputes; `sale_order.delivery_status` recomputes (PDEL-02) |
| Invoice created | `_create_invoices()` | sale_order.py SOL-39/40 | `account.move` created, `quantity=qty_to_invoice` | `account.move.line` read back for `qty_invoiced`/`qty_invoiced_posted` (SOL-09/10) — a round-trip |
| Subcontract-service line confirmed | `_action_confirm()` on an order with a `service_to_purchase` product | sale_purchase module, SLID-04/05/06 | Auto-creates/reuses a **draft** `purchase.order` + line, `sale_line_id` stamped | Purchase side gains a new draft PO with no human RFQ step |

## 02 — Events originating in Purchase

| Event | Trigger | Source | What changes | Downstream consumers |
|---|---|---|---|---|
| RFQ confirmed | `button_confirm()` | purchase_order.py PO-04..07 | Branches to `state='purchase'` or `'to approve'`; vendor written into `product.supplierinfo` | `_create_stock_moves()` creates receipt move(s) directly (GRPA-01/02) |
| Order approved (post "to approve") | `button_approve()` | purchase_order.py PO-07 | `state='purchase'`, `date_approve` stamped | Same as above, now unblocked |
| Receipt move done | `stock.move.line._action_done()` | (Inventory-owned) | quant on-hand increases | `purchase_order_line._prepare_qty_received()` (`'stock_moves'` method, POL-22/23) recomputes |
| PO line quantity reduced below already-invoiced | `write()` on `product_qty` | purchase_order_line.py POL-24 | **Not blocked** — only a chatter activity nudges toward a manual refund | No hard downstream effect found |
| Order cancelled | `button_cancel()` | purchase_order.py PO-10/35 | Blocked if `locked` or an open vendor bill exists; else `state='cancel'` | Stock cascade **CLOSED (CORR-003)**: `purchase_stock` overrides `button_cancel()`, state-partitioned by receipt scenario — see `04_PURCHASE_CAPABILITY_MODEL.md` §04 |
| Vendor bill posted | (Accounting-owned) | — | `account.move.line.purchase_line_id` set | `_prepare_qty_invoiced()` sums it (POL-09) |
| Purchase Request approved | `button_approved()` (native) or an unconfirmed external `multi.approval` flow | purchase_request module, PREQ-07/APPR-08/09 | `state='approved'` | Unblocks the PR→PO conversion wizard (PREQ-13, hard gate) |
| PR line converted to PO | `make_purchase_order()` wizard | PREQ-14/15/16 | Creates/reuses `purchase.order`+line; writes `purchase.request.allocation` | PR line's `purchase_state` becomes a read-model mirror of the PO line (PREQ-10) |
| Reordering rule fires | `_procure_orderpoint_confirm()` | stock_orderpoint.py (Phase 2 REPL-06), consumed by Purchase | `stock.rule.run()` → `'buy'` action dispatch | New `purchase.order` — **CLOSED (CORR-003)**: `_run_buy()` fully traced (`purchase_stock/models/stock_rule.py` L58-165), reuses/creates a draft PO per vendor/company/picking-type/currency domain — see `02_INVENTORY_CAPABILITY_MODEL.md` §09 |
| Tender confirmed | `button_confirm()` with open `alternative_po_ids` | purchase_requisition/models/purchase.py PREQS-10 | Intercepts with a warning wizard; losing alternative POs get `button_cancel()`-ed | The winning PO proceeds through the normal confirmation path above |

## 03 — Events originating in Inventory

| Event | Trigger | Source | What changes | Downstream consumers |
|---|---|---|---|---|
| Move confirmed | `_action_confirm()` | stock_move.py MOV-23 | `draft→waiting/confirmed`; for `make_to_order`, builds a Procurement and calls `stock.rule.run()` again | Chained upstream replenishment move — **CLOSED (CORR-003)**: exact re-trigger site is `stock_move.py` L1580; `_action_assign()` confirmed NOT to re-trigger |
| Move reserved | `_action_assign()` | stock_move.py MOV-30, stock_quant.py AVL-QNT-03 | `state→assigned`/`partially_available`; `stock.quant.reserved_quantity` increases | Sale's advisory availability widgets (GRPA-02/03/04); Purchase has no equivalent read path found |
| Move done | `_action_done()`→`move_line._action_done()` | stock_move.py MOV-32, stock_move_line.py RES-15/17 | quant on-hand/reserved both change; `_create_backorder()` runs first if under-picked | Sale's `qty_delivered` (SOL-26); Purchase's `qty_received` (POL-22/23); `product.qty_available`/`virtual_available` (AVL-09/12) |
| Picking validated with shortfall | `button_validate()`→`_check_backorder()` | stock_picking.py BO-04/05 | New backorder picking created, `backorder_id` set | Neither Sale nor Purchase reference `backorder_id` directly (Phase 4 POL-31 confirms this for Purchase; Sale not independently re-verified but no positive citation exists either) |
| Return created | `stock.return.picking` wizard | stock_picking.py RET-01..10 | New picking/move, `origin_returned_move_id` set, locations swapped | Sale (SRET-04/05/06) and would-be-symmetric Purchase behavior both re-stamp FKs onto the result but never initiate it |
| Replenishment procurement raised | `_procure_orderpoint_confirm()`/`_run_scheduler_tasks()` (daily cron) | stock_orderpoint.py REPL-06/12/13 | `stock.rule.run()` invoked | Routes to `'buy'` (Purchase) or a plain internal `'pull'`/`'push'` depending on the resolved rule |
| Put-away resolved | `_get_putaway_strategy()` on receipt | stock_location.py PA-04 | Move line's destination sub-location set | Purely Inventory-internal; not referenced by Sale/Purchase |

## 04 — Cross-cutting dependency table (which module reads which other module's state)

| Reads | Reader | Read-only or write-back? | Evidence |
|---|---|---|---|
| `stock.quant`/`product.qty_available` compute fields | Sale (availability widget) | Read-only, advisory | Sales GRPA-02/03/04 |
| `stock.quant`/`product.qty_available`/`virtual_available` | Purchase (`_compute_forecasted_issue`) | Read-only, advisory | Phase 2 GRPA-08 |
| `stock.move.state`/`quantity` | Sale (`qty_delivered`) | Read-only | Sales SOL-26 |
| `stock.move.state`/`quantity` | Purchase (`qty_received`) | Read-only | Purchase POL-22/23 |
| `account.move.line` (posted invoice) | Sale (`qty_invoiced`) | Read-only, backward-derived | Sales SOL-09/10 |
| `account.move.line` (posted bill) | Purchase (`qty_invoiced`) | Read-only, backward-derived | Purchase POL-09 |
| `product.template.invoice_policy`/`purchase_method` | Both (billing gate) | Read-only, per-product | Sales SOL-34/35, Purchase POL-08 |
| `res.company._accessible_branches()` | Both (line-level company check) | Read-only | Phase 1 CO-27/29 |
| `sale.order.line` | Purchase (`sale_purchase` subcontract/dropship) | **Write** — creates a PO line and stamps `sale_line_id` | Gap-closure SLID-01..12 |
| `purchase.request.state` | Purchase (PR→PO wizard gate) | Read-only, hard gate | Purchase PREQ-13 |
| `stock.picking.type.code` | Both (Sale reads for "Delivery" button; Purchase carries the FK directly) | Read-only | Phase 2 PICK, Sales/Purchase respective sections |

## 05 — What does NOT cross module boundaries (confirmed negatives, not just silence)

- **Sale never reads or writes `stock.quant` directly** — it only reads `product`-level compute fields (GRPA
  citations above). All physical mutation is Inventory-internal.
- **Purchase never reads or writes `stock.quant` directly either** — same pattern.
- **Neither Sale nor Purchase references `stock.picking.backorder_id`** as a field (Purchase: full-grep-confirmed,
  POL-31; Sale: no positive citation found in any phase).
- **Neither Sale nor Purchase has its own Return model, button, or wizard** — both are equally silent, deferring
  100% to Inventory's generic mechanism (Scenarios 5/6 of `05_INTEGRATED_E2E_LIFECYCLE_MAP.md`).
- **`purchase.requisition` and `sale.order` have no direct relationship anywhere found** — the demand-signal chain
  from Sales into Purchase (if any exists for make-to-order scenarios beyond `sale_purchase`'s subcontract-service
  case) was not independently evidenced in this research effort.
