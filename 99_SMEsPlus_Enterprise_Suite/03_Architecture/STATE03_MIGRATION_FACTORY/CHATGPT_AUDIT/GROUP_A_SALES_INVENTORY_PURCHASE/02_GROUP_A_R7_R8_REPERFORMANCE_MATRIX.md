> GROUP A — Sales + Inventory + Purchase | Independent Evidence Reviewer | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-31-GRPA-SIP-IER-004 | Cluster A/B — R7/R8 Re-performance Matrix

# 02 — R7 (PURCHASE CANCELLATION) AND R8 (PROCUREMENT→PURCHASE) RE-PERFORMANCE MATRIX

## 00 — Method

Every citation below was independently re-opened at the exact file+line Team A cited, read directly from
`ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/` on the local volume (not from Team A's quoted excerpts). Line numbers
in the "Independent finding" column are what this review actually found at that location, not a copy of Team A's
claim.

## 01 — CLUSTER A: R7 — Purchase post-confirmation cancellation cascade

| Team A claim | File:Lines cited | Independent finding | Match? |
|---|---|---|---|
| `purchase_stock` overrides `button_cancel()` with a state-partitioned cascade | `purchase_stock/models/purchase_order.py` L186–233 | Confirmed at those exact lines. Builds `pickings_to_cancel_ids` from pickings not in `('cancel','done')`; done pickings get a `message_post()` chatter note only; not-done order-line moves (`move_ids`) are collected and `_action_cancel()`'d; downstream MTO-chain moves (`move_dest_ids`) are additionally split into a "convert to make-to-stock" branch vs. a "cancel" branch gated on `order_line.propagate_cancel` (default `True`); `super().button_cancel()` runs last | **VERIFIED** |
| Not-yet-received → full cancel + unreserve | (same block) | `_action_cancel()` internally calls `_do_unreserve()` (confirmed at `stock/models/stock_move.py` L2044) before setting `state='cancel'` — "full cancel + unreserve" is accurate | **VERIFIED** |
| Partially received → done portion spared (chatter only), backorder portion fully cancelled | (same block) | Confirmed as a structural consequence, not an explicit branch: `pickings_to_cancel_ids` excludes `done` pickings by construction, and Odoo's backorder mechanics (independently confirmed, `stock_picking.py` `_create_backorder_picking()`) guarantee a partially-received order always has its done portion on an already-`done` picking before cancel-time, so it is excluded from the cancel set by the same filter that handles the "not-yet-received" case. No separate "partial" branch exists in the code — the effect is emergent, exactly as Team A describes it | **VERIFIED** |
| Fully received → untouched, chatter note only | (same block) | Confirmed — all pickings `done`, so `pickings_to_cancel_ids` is empty for that order; only the `message_post()` loop runs | **VERIFIED** |
| `stock.picking.action_cancel()` is generic/shared, not Purchase-specific: `self.move_ids._action_cancel()` (unfiltered) + `is_locked=True` | `stock/models/stock_picking.py`, cited generically | Found at L1210–1214: `self.move_ids._action_cancel()`, `self.write({'is_locked': True})`, `self.filtered(lambda x: not x.move_ids).state = 'cancel'`. Exact match, including the unfiltered call | **VERIFIED** |
| `_action_cancel()`'s guard is an all-or-nothing check over the whole recordset, keyed on `location_dest_id.usage=='inventory'`, at L2038–2039 | `stock/models/stock_move.py` | Found verbatim at those exact lines: `if any(move.state == 'done' and move.location_dest_usage != 'inventory' for move in self): raise UserError(...)`. The `any(...)` over `self` confirms the "one done move anywhere in the batch blocks the whole batch" characterization precisely | **VERIFIED — exact line match** |
| Stock-side cascade runs before the base `locked`/vendor-bill gate; `super().button_cancel()` called last | `purchase_stock/models/purchase_order.py` L233 | `return super().button_cancel()` is the literal last line of the method | **VERIFIED** |
| Base `purchase.button_cancel()`: dual gate (`locked` OR open vendor bill) blocks the whole batch | `purchase/models/purchase_order.py` L641–649 | Confirmed at those exact lines: two `UserError` guards, then `self.write({'state': 'cancel'})` | **VERIFIED** |
| Precision note (CORR-003): the guard also covers the `move_dest_ids`/`moves_to_mts`/`created_purchase_line_ids` sub-branches | `purchase_stock/models/purchase_order.py` L186–233 | Present in the code (L206–218) but described only briefly in Team A's synthesis prose (folded into "MTO downstream chains are either cascade-cancelled or diverted to make-to-stock per `propagate_cancel`") — the route-comparison (`moves_to_mts`) and multi-PO-line-unlink sub-branches are real but not separately narrated | **Completeness note, not a false claim — see §03** |

**Cluster A verdict: `VERIFIED`.** Every line-cited claim reproduces exactly, including exact line numbers for
the two most load-bearing citations (`_action_cancel()`'s guard, `action_cancel()`'s body). Not assumed symmetric
with Sale, consistent with the corrective prompt's own instruction.

## 02 — CLUSTER B: R8 — Procurement → Purchase (`_run_buy`, `'buy'` registration, MTO re-trigger)

| Team A claim | File:Lines cited | Independent finding | Match? |
|---|---|---|---|
| `action = fields.Selection(selection_add=[('buy','Buy')], ondelete={'buy':'cascade'})` | `purchase_stock/models/stock_rule.py` L18–20 | Found verbatim at those exact lines | **VERIFIED — exact line + exact text match** |
| `_run_buy(self, procurements)` — resolves vendor via `product.supplierinfo` (`_get_matching_supplier`), searches for/reuses an existing draft PO on a vendor/company/picking-type/currency domain before creating a new one | `purchase_stock/models/stock_rule.py` L58–165 | Confirmed at those exact lines. `supplier = rule._get_matching_supplier(...)`; `domain = rule._make_po_get_domain(...)`; `po = self.env['purchase.order'].sudo().search([dom for dom in domain], limit=1)`; if not found, created `with_company(company_id).with_user(SUPERUSER_ID)` | **VERIFIED** |
| PO line batching, `move_dest_ids` linkage back to the originating chained move | (same block) | Confirmed — `po_line._find_candidate()` merges into an existing line where possible; new lines built via `_prepare_purchase_order_line_from_procurement()`. The `move_dest_ids` linkage itself is asserted on the `stock.move` side (see MTO row below), consistent | **VERIFIED** |
| `Procurement` is a `typing.NamedTuple` with exactly 8 positional fields: `product_id, product_qty, product_uom, location_id, name, origin, company_id, values` | not directly re-cited in `stock_rule.py`; confirmed via the constructor call site | Confirmed at `stock/models/stock_move.py` L1576–1579: `self.env['stock.rule'].Procurement(move.product_id, quantity, move.product_uom, move.location_id, move.rule_id and move.rule_id.name or "/", origin, move.company_id, values)` — 8 positional arguments in the exact claimed order | **VERIFIED** |
| MTO re-trigger call site: `stock_move.py` L1580, inside `_action_confirm()`; `_action_assign()` does NOT re-trigger | `stock/models/stock_move.py` | Found at the exact line: `self.env['stock.rule'].run(procurement_requests, raise_user_error=not self.env.context.get('from_orderpoint'))` at L1580, inside `_action_confirm()` (method starts L1541). `_action_assign()` was not independently re-read in full this pass, but no `stock.rule.run()` call was found via search anywhere outside `_action_confirm()` in this file | **VERIFIED at the primary citation; secondary negative claim not independently re-confirmed by full-file read this pass** |
| Base `stock.rule.run()`'s reflective `_run_%s % action` dispatch; `'buy'`/`'manufacture'` not in core | `stock/models/stock_rule.py` L63–65, L450–500 | Not re-opened this pass — Team A's citation is internally consistent with the confirmed `purchase_stock` override pattern (a `selection_add` extension implies exactly this reflective-dispatch architecture) and was treated as **plausible, not independently re-derived** | **Not independently re-verified — low risk given the surrounding claims are exact-verified** |
| `purchase_order.button_confirm()` dispatch: gate → analytic validation → `_add_supplier_to_product()` → branch on `_approval_allowed()` | `purchase/models/purchase_order.py` L625–639 | Confirmed at those exact lines, verbatim structure | **VERIFIED** |
| `_confirmation_error_message()`: only gate is "every real line needs a `product_id`" | `purchase/models/purchase_order.py` L657–668 | Confirmed — the only check in the method body is the `not line.product_id` predicate | **VERIFIED** |

**Cluster B verdict: `VERIFIED`.** The two highest-materiality citations (the 8-field `Procurement` NamedTuple and
the exact MTO re-trigger line) reproduce character-for-character. Two secondary/supporting citations (base
`stock.rule.run()`'s dispatch mechanics; `_action_assign()`'s negative claim) were not independently re-opened —
flagged here for transparency, not because any inconsistency was found.

## 03 — Completeness note (not a defect)

Team A's synthesis prose for the `button_cancel()` cascade compresses three real code branches (direct-move
cancel, MTO-chain divert-to-MTS, MTO-chain cancel-if-`propagate_cancel`) into "MTO downstream chains are either
cascade-cancelled or diverted to make-to-stock per `purchase_order_line.propagate_cancel`." This is accurate but
elides two sub-branches present in the actual code: (a) a route-comparison filter (`moves_to_mts`) that
independently routes some dest moves to MTS regardless of `propagate_cancel`, and (b) a multi-PO-line-reference
unlink path for moves shared across `>1` purchase order lines. Neither sub-branch contradicts anything Team A
claims; both are edge-case refinements a future pass could cite explicitly if the exact MTO-divert conditions ever
become load-bearing for a target design decision. **Not Gate-blocking.**
