> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 7 of 10 — Quantity Semantics Register
> Consolidates every quantity concept documented across Phases 1-5 into one canonical register, per governance §14.
> `Field name alone is NOT semantic proof` — every row below cites the compute method or DB column that PROVES the
> meaning, not just the field's label. No new source claims are introduced; every entry cites an existing evidence ID.

# 09 — QUANTITY SEMANTICS REGISTER

## 00 — Method

Governance §14 requires, per quantity: source reference; proven business meaning; stored vs derived; relevant
state/event; database evidence; cross-module consumer; company/warehouse scope; evidence confidence; contradiction/
unknown. Grouped by domain family, in the order governance §14 lists them.

---

## 01 — SALES quantities

| Quantity | Field | Stored/Derived | Proven meaning (not just the label) | DB evidence | Cross-module consumer | Confidence |
|---|---|---|---|---|---|---|
| Requested | *(no distinct field found)* | n/a | No separate "requested" concept exists on `sale.order.line` prior to `product_uom_qty` — a line begins life already as "ordered" | — | — | NOT OBSERVED |
| Quoted | `sale.order.line.product_uom_qty` while `order.state in (draft,sent)` | Stored, plain user input | Same field as "ordered" below — state, not field name, distinguishes quote from commitment (Sales SO-01, SOL-01) | `product_uom_qty NOT NULL` | Inventory reads it only after confirmation | VERIFIED FACT |
| Ordered | `sale.order.line.product_uom_qty` | Stored, plain user input | Precomputed default, never derived from anything else in the cluster; user-editable pre- and post-confirmation (chatter-logged only, not blocked) (Sales SOL-01/02, SO-18) | `product_uom_qty NOT NULL` | Feeds procurement demand (Phase 2 GRPA-04/05); feeds `qty_to_invoice` under order-policy (SOL-12) | VERIFIED FACT |
| Reserved | `stock.quant.reserved_quantity` (there is NO `sale.order.line` field for this) | Stored (on the quant, not the SO line) | Portion of on-hand claimed by move lines of confirmed-but-not-done deliveries; Sale never reads this directly — only the advisory `free_qty` complement (Phase 2 QNT-05, synthesis) | `reserved_quantity NOT NULL` | Sale's availability widget reads the complement, not this field itself | VERIFIED FACT — genuine absence at the Sale layer, not a gap in research |
| Picked | `stock.move.line.picked` (Inventory-owned; no SO-line equivalent) | Stored | Line-level execution flag rolling up into `stock.move.picked`; distinct from `quantity` (Phase 2 MOV-08/MOVL-04) | `picked boolean` | Not read by Sale in any file examined | VERIFIED FACT |
| Delivered | `sale.order.line.qty_delivered` | Stored compute, directly user-editable (manual override) | A **dispatched** computation, not one formula: `'analytic'` (expense-driven, sums `account.analytic.line.unit_amount`), `'manual'` (services — stays whatever was last written), or `'stock_move'` (sums `done` outgoing moves minus done incoming/returns, once `sale_stock` installed and product is `consu`) (Sales SOL-05/06/07, SOL-26) | `qty_delivered numeric` (nullable) | Feeds `qty_to_invoice` under delivery-policy (SOL-12); feeds `invoice_status` (SOL-15/27) | VERIFIED FACT |
| Returned | *(no distinct field — netted directly into `qty_delivered` via `-SUM(done incoming moves)`)* | Derived, folded into `qty_delivered` | A customer return is a `done` incoming move against the same line; `sale_stock`'s `qty_delivered` computation subtracts it rather than tracking it as a separate signed quantity (Sales SOL-26) | — | — | VERIFIED FACT — returns are NOT a separate quantity concept in this codebase, they are a negative delivered-quantity input |
| Cancelled | *(no distinct field)* | n/a | Cancelling a confirmed order does not zero or track a "cancelled quantity" on the line — it cancels the underlying not-done `stock.move` and stops the invoicing chain via `state` (Sales CANC-05/13) | — | — | NOT OBSERVED as a quantity — it is a state transition, not a quantity |
| Remaining | `sale.order.line.qty_to_deliver` (compute-only, never stored) | Derived, live | `= product_uom_qty − qty_delivered`; no clamping to zero observed; over-delivery behavior on this field's sign was NOT traced | Absent from DDL (compute-only, confirmed) | Drives `display_qty_widget` only — a UI concern layered into the same compute (Sales PDEL-03/04) | VERIFIED FACT for the formula; EVIDENCE_MISSING for over-delivery clamping |
| Backordered | *(no SO-line field — lives entirely on the Inventory-side `stock.picking.backorder_id`)* | n/a at the Sale layer | Sale never reads `backorder_id`; "remaining obligation" is entirely re-derived from `qty_to_deliver` and header `delivery_status`, independent of whether a formal backorder picking exists | — | — | VERIFIED FACT — a genuine non-consumption, not a research gap |
| Invoiced | `sale.order.line.qty_invoiced` | Stored compute, NOT manually overridable | Derived **backward** from `account.move.line` via `invoice_lines`: `out_invoice`→add, `out_refund`→subtract, excludes cancelled moves (Sales SOL-08/09) | `qty_invoiced numeric` (nullable) | Round-trips into Accounting | VERIFIED FACT |
| Invoiced (posted-only) | `sale.order.line.qty_invoiced_posted` | Compute, **not stored** | Same aggregation restricted to `state=='posted'` — deliberately a SEPARATE, non-interchangeable computation from `qty_invoiced` (Sales SOL-10) | Absent from DDL (confirmed non-stored) | — | VERIFIED FACT — a migration must pick ONE of these two as canonical, they answer different questions |
| To-invoice | `sale.order.line.qty_to_invoice` | Stored compute | The **only** one of the Sales quantities that branches on `product.invoice_policy`: `order`→`ordered−invoiced`; `delivery`→`delivered−invoiced` (Sales SOL-11/12) | `qty_to_invoice numeric` (nullable) | Written verbatim as the invoice line's quantity (SOL-17) | VERIFIED FACT — the single mechanism separating bill-on-order from bill-on-delivery businesses |

## 02 — PURCHASE quantities

| Quantity | Field | Stored/Derived | Proven meaning | DB evidence | Cross-module consumer | Confidence |
|---|---|---|---|---|---|---|
| Requested | `purchase.request.line.product_qty` (a DIFFERENT model from the PO line) | Stored, plain input | The pre-RFQ internal demand signal — exists only if the `purchase_request` OCA module's flow is used; converted 1:1 into `purchase.order.line.product_qty` by the wizard (Purchase PREQ-09, PREQ-14/15) | `purchase_request_line.product_qty` | Feeds the PR→PO wizard | VERIFIED FACT |
| Quoted/RFQ | `purchase.order.line.product_qty` while `order.state in (draft,sent)` | Stored, plain input | Same field as "ordered" — state distinguishes RFQ from commitment, identical pattern to Sale (Purchase PO-01, POL-01) | `product_qty NOT NULL` | — | VERIFIED FACT |
| Ordered | `purchase.order.line.product_qty` | Stored, required, plain input | The root demand number — chatter-logged (not blocked) on post-confirmation edit (Purchase POL-01, POL-15) | `product_qty NOT NULL` — the **only** quantity column that IS `NOT NULL` at the DB level on this table | Feeds `qty_to_invoice` under order-based `purchase_method` | VERIFIED FACT |
| Expected | `stock.move` (not-done) records linked via `move_ids` | Derived, implicit | There is no dedicated "expected quantity" field on the PO line — expected supply is whatever not-done moves exist against it, read via `_get_qty_procurement` (Purchase POL-25) | — | — | VERIFIED FACT — expected supply is a computed VIEW over moves, not a stored fact |
| Received | `purchase.order.line.qty_received` | Stored compute + manual escape hatch (`qty_received_manual`) | Architecturally dispatched by `qty_received_method`: `'manual'` (typed) or `'stock_moves'` (sum of `done` moves, with explicit return/dropship netting — a purchase-return move subtracts, a dropship-origin move already counted elsewhere is deliberately ignored) (Purchase POL-04/05, POL-13/22/23) | `qty_received numeric` (nullable) | Feeds `qty_to_invoice` under receive-based `purchase_method` | VERIFIED FACT |
| Accepted | *(no distinct field — receipt-validation IS acceptance in this codebase; no separate QA/inspection-hold quantity found)* | n/a | Not observed as a separate concept from "received" | — | — | NOT OBSERVED / EVIDENCE_MISSING |
| Returned-to-vendor | *(no distinct field — netted directly into `qty_received` via the return-move predicate)* | Derived, folded into `qty_received` | Exact structural mirror of Sale's "returned" finding — a vendor return is a `done` move whose destination usage is `'supplier'`; Purchase nets it out of `qty_received` rather than tracking it separately (Purchase POL-23/29) | — | — | VERIFIED FACT — structurally identical non-separation to the Sales side |
| Cancelled | *(no distinct field — a state transition, not a quantity, same as Sales)* | n/a | — | — | — | NOT OBSERVED as a quantity |
| Remaining | *(no dedicated field — implicit via not-done moves)* | Derived, implicit | `_get_qty_procurement` nets outgoing against incoming moves to determine "how much of this line is already covered" (Purchase POL-25/26) | — | — | VERIFIED FACT |
| Backordered | *(no PO-line field — Purchase NEVER references `stock.picking.backorder_id`, confirmed by full-file grep)* | n/a | Identical non-consumption finding to Sales | — | — | VERIFIED FACT — confirmed negative, not silence |

## 03 — INVENTORY quantities (the canonical six, on `stock.quant`/`product.product`)

These are the foundational quantities both Sales and Purchase read (never write) via `product`-level compute
fields — established in full in Phase 2, restated here in register form per governance §14's required shape.

| Quantity | Field | Stored/Derived | Proven meaning | DB evidence | Cross-module consumer | Confidence |
|---|---|---|---|---|---|---|
| On-hand | `stock.quant.quantity` / `product.qty_available` | Quant: stored. Product: compute | Physically present, raw `SUM(quantity)` over quants in scope, **no adjustment for reservation** — what a warehouse count would show (Phase 2 QNT-04, AVL-09) | `stock_quant.quantity numeric` (nullable — an asymmetry vs. `reserved_quantity NOT NULL`, unexplained) | Sale/Purchase read `product.qty_available` only, never the quant | VERIFIED FACT |
| Available | `stock.quant.available_quantity` (per bin) / `product.free_qty` (product level) | Both compute | `On-Hand − Reserved` (Phase 2 QNT-06, AVL-10) — the number safe to hand out as a NEW reservation | Not a stored column (compute) | Sale's advisory widget (GRPA-02/03/04); Purchase's `_compute_forecasted_issue` (GRPA-08) | VERIFIED FACT |
| Reserved | `stock.quant.reserved_quantity` | Stored | Portion of on-hand already claimed by move lines of confirmed-but-not-done transfers; **no `product.reserved_qty` field exists** — only the complement (`free_qty`) surfaces at product level | `reserved_quantity numeric NOT NULL` | Neither Sale nor Purchase read this field directly | VERIFIED FACT |
| Incoming | `product.incoming_qty` | Compute | `SUM(product_qty)` of moves whose destination crosses into scope, **explicitly excluding `done` moves** — always "still in flight" | Not stored | Purchase's `_compute_forecasted_issue` implicitly (via `virtual_available`) | VERIFIED FACT |
| Outgoing | `product.outgoing_qty` | Compute | Mirror of incoming — not-yet-done moves whose source is in scope and destination leaves it | Not stored | Same as above | VERIFIED FACT |
| Forecasted | `product.virtual_available` | Compute | `On-Hand + Incoming − Outgoing` — can legitimately go **negative** (used by reordering rules as a normal trigger condition, Phase 2 NEG-06), unlike raw on-hand which is only negative in an oversell edge case | Not stored | Sale's advisory widget; Purchase's `_compute_forecasted_issue` (GRPA-08); `stock.warehouse.orderpoint` (REPL-05) | VERIFIED FACT |

## 04 — Cross-family reconciliation (the single most important register-level finding)

- **"Delivered" (Sale) and "Received" (Purchase) are the SAME underlying mechanism from opposite ends**: both are
  a `stock.move`-completion sum, both are dispatched by a per-line method-selector field
  (`qty_delivered_method`/`qty_received_method`) that is itself a stored, computed field, and both default to
  `'manual'` for services and switch to a stock-derived method only once the respective `_stock` bridge module is
  installed AND the product is `type=='consu'`. This symmetry is itself a register-level fact worth preserving.
- **"To-invoice" (Sale) and "To-invoice" (Purchase) are NOT symmetric in their gating field name, but ARE
  symmetric in structure**: Sale branches on `product.invoice_policy` (`order`/`delivery`); Purchase branches on
  `product.purchase_method` (`purchase`/`receive`). Same two-value fork, same role (order-based vs.
  fulfillment-based billing), different field. A migration target should decide whether these deserve one unified
  concept or should remain deliberately separate (AR vs. AP control policies can legitimately diverge per
  business).
- **Returns are not a distinct quantity family on either commercial side** — both Sale and Purchase fold returns
  into their respective delivered/received computation as a negative netting term, never as their own signed
  quantity. Any target Quantity Semantics model that tries to expose "returned quantity" as a first-class field on
  the SO/PO line would be inventing a concept this source system does not have at that layer (it DOES exist, fully
  tracked, at the `stock.move`/`stock.picking` layer via `origin_returned_move_id` and `return_id`).
- **Backorder is never a quantity either commercial side reads** — "remaining obligation/supply" is always
  independently re-derived by each side from its own quantity fields (`qty_to_deliver`, `_get_qty_procurement`),
  never by querying the Inventory-side backorder record. This is confirmed as a genuine architectural choice
  (full-grep negative on the Purchase side), not a coincidental gap.
- **No DB constraint anywhere in this entire register enforces a cross-field relationship** (e.g., nothing
  prevents `qty_invoiced > product_uom_qty` at the database level on either SO or PO lines) — every quantity rule
  documented above is application-layer only, consistent with the "no DB CHECK constraints" finding that recurs
  throughout Phases 2-4.

## 05 — Open items carried forward

1. Sale-side over-delivery clamping behavior on `qty_to_deliver` — not traced (Phase 3 finding, restated).
2. Purchase-side over-receipt is confirmed **unguarded** (not merely unresearched) — `_prepare_qty_received` will
   sum past `product_qty` with no block (Phase 4 finding, restated).
3. The exact `stock_move.py` call site that re-triggers `stock.rule.run()` for a `make_to_order` move (needed to
   fully close the "Incoming"/"Expected" chain from a Sales-triggered replenishment back to a new Purchase order)
   — EVIDENCE_MISSING per the Phase 5 gap-closure research.
4. `stock_move.is_in`/`is_out` DB columns — compute source never opened in any phase (Phase 2 finding, restated).
