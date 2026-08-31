# A6 — Route / Procurement / Replenishment Evidence

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Research routes/rules, reorder points, replenishment, MTS/MTO, dropship, chained movements, procurement dispatch, duplicate/retry controls | Claude (Team A, DR-002) | This artifact; `stock/models/stock_rule.py`, `purchase_stock/models/stock_rule.py`, `mrp/models/stock_rule.py` | 2026-08-31 | Independent Evidence Review (pending) | VERIFIED (direct source citation) | Central to A16 Cross-Proof pack |

## 1. `stock.rule` — the routing/procurement engine

- `stock.rule.action` (core `stock/models/stock_rule.py`) — Selection: `pull` / `push` / `pull_push`, default `pull`. Extended via `selection_add` in each dependent app: `purchase_stock` adds `'buy'`; `mrp` adds `'manufacture'`. This is independently confirmed by **both** this session's own source reading and GROUP A's frozen REPL-01–15 findings — full agreement, no discrepancy.
- Dispatch mechanism: `stock.rule.run()` groups procurements by `action` (collapsing `pull_push` → `pull`) and dynamically calls `_run_<action>()` via `getattr` — i.e. `_run_pull` (core), `_run_push` (core), `_run_buy` (`purchase_stock`), `_run_manufacture` (`mrp`). This is the single procurement-dispatch choke point for the entire Inventory-adjacent module family.
- `stock.rule.procure_method` (Selection `make_to_stock` / `make_to_order` / `mts_else_mto`) controls MTS/MTO behavior. Chained/multi-step routes are represented entirely through `stock.move.move_orig_ids`/`move_dest_ids` linkage (populated in `_get_stock_move_values()`), not a separate "route step" model — each rule's output move becomes the "orig" of the next rule's move.

## 2. `_run_buy()` — full trace (purchase_stock)

`purchase_stock/models/stock_rule.py — StockRule._run_buy()`: searches for an existing open PO matching the vendor/company/currency domain (`po = self.env['purchase.order'].sudo().search([...], limit=1)`); creates a new PO only `if not po` — otherwise merges the new procurement into the existing PO (updates `origin`, `reference_ids`). This closes GROUP A's own Critical#3 (`_run_buy()`'s exact implementation, originally EVIDENCE_MISSING, closed by their CORR-003) — this pass's independent re-read of the same method reaches the identical conclusion, corroborating rather than contradicting GROUP A's finding.

## 3. `_run_manufacture()` — full trace (mrp)

`mrp/models/stock_rule.py — StockRule._run_manufacture()`: builds a domain via `_make_mo_get_domain()` (matches `bom_id`, `product_id`, `state in ['draft','confirmed']`, `is_planned=False`, `picking_type_id`, `company_id`, `user_id=False`, `reference_ids`); if a matching draft/confirmed MO is found, it does **not** create a duplicate — it invokes the `change.production.qty` wizard to bump the existing MO's `product_qty` instead of creating a new one. This is a new finding this pass contributes (not in GROUP A's Sales+Purchase-focused register, since Manufacturing was outside GROUP A's scope) — a real, source-confirmed merge-not-duplicate safeguard at the manufacturing-procurement boundary.

## 4. Structural finding: no `procurement.group` model

**Material new discovery this pass**: there is no `procurement.group` model anywhere in this codebase (confirmed by exhaustive grep — zero hits for `_name = 'procurement.group'`), and `stock.move` has no `group_id` field. Grouping/origin-tracking across Sale/Purchase/Manufacture documents and their generated stock documents is instead done via a **`stock.reference`** model (`_name = 'stock.reference'`; fields `name`, `move_ids` M2M to `stock.move`, computed `picking_ids`) — `sale.order.stock_reference_ids`, `purchase.order.reference_ids`, and `mrp.production.reference_ids` each carry a M2M to `stock.reference`, threaded through the procurement `values` dicts. A stale docstring comment in `stock_rule.py`'s `run()` method still references the old `ProcurementGroup.Procurement` class name — a harmless leftover comment, not live code (the actual class is a `NamedTuple` named `Procurement`, assigned as `StockRule.Procurement`). This is a genuinely new, more precise structural fact for the evidence base — not previously registered by GROUP A, and materially relevant to any future migration/target-schema discussion since it means "procurement group" is not a concept SMEsPlus can assume exists in a familiar shape.

## 5. Duplicate/retry safeguards — full inventory (Mandatory Question, cross-cutting)

No single unified idempotency-key mechanism exists. Every guard found is a **quantity-remaining-based merge or no-op**, not a hard duplicate-prevention error:

| Layer | Guard | Citation |
|---|---|---|
| Move confirm | `if move.state != 'draft': continue` | `stock/models/stock_move.py — _action_confirm()`, first line of loop |
| Sale procurement | `qty = line._get_qty_procurement(...)`; skip if already fully procured | `sale_stock/models/sale_order_line.py — _action_launch_stock_rule()` |
| Purchase procurement | `qty = self._get_qty_procurement()`; only appends new move dicts for the remaining, unattached quantity | `purchase_stock/models/purchase_order_line.py — _prepare_stock_moves()` |
| Purchase picking reuse | Looks for an existing non-done/non-cancel picking on the order before creating a new one | `purchase_stock/models/purchase_order_line.py — _create_or_update_picking()` |
| PO dedup at rule level | Search-before-create (§2 above) | `purchase_stock/models/stock_rule.py — _run_buy()` |
| MO dedup at rule level | Search-before-create, merge via wizard (§3 above) | `mrp/models/stock_rule.py — _run_manufacture()` |
| Backorder split guard | Only splits when `quantity < product_uom_qty` — will not create a spurious backorder for a fully/over-processed move | `stock/models/stock_move.py — _create_backorder()` |

This deepens GROUP A's own Exception#15 finding ("duplicate/retry — `_merge_quants()` exists specifically because concurrent transactions can insert duplicate rows") with the additional rule-dispatch-layer evidence above. **No explicit "already processed, abort" exception/guard was found anywhere** — every mechanism is a remaining-quantity computation, which means a sufficiently unusual retry sequence (e.g. concurrent partial writes) could in principle still produce an inconsistent result; this is registered as a genuine open invariant question in A13, not asserted as proven-safe.

## 6. Source asymmetry between Sales and Purchase (Mandatory Question #8 supporting evidence)

Independently re-confirmed by this pass: Purchase creates `stock.move` **directly and synchronously** (`PurchaseOrderLine._create_stock_moves()` → `stock.move.create()`), while Sale creates it **indirectly through the rule engine** (`SaleOrderLine._action_launch_stock_rule()` → `stock.rule.run()` → `_run_pull`/`_run_push`). This is not a stylistic difference — it means Purchase's receipt-generation logic and Sale's delivery-generation logic are genuinely different code paths with different extension points, a real fact for any future target-design fit-gap analysis (GROUP A's own GRPA-01/02 vs. GRPA-04/05, independently corroborated).

No Evidence = No Progress. DELTA-FIRST.
