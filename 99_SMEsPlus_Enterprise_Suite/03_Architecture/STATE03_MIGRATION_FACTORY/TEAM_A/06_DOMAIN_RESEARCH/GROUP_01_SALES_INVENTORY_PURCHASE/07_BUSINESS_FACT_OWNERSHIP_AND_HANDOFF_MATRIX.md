> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 5-6 of 10 — Business Fact Ownership & Handoff Matrix
> Applies governance §13's mandatory rule: `Document state changed ≠ Physical stock changed ≠ Financial posting
> occurred` — each relationship below is proven independently, from evidence already established in Phases 1-4.

# 07 — BUSINESS FACT OWNERSHIP AND HANDOFF MATRIX

## 00 — Method

For each material business fact: Fact | Technical State/Field | Owning Model | Business Event that changes it |
Consumers | Evidence status. This is not a re-statement of the capability models — it is a cross-cutting index
answering "who owns this fact, and who else touches it."

## 01 — Commercial Intent facts (Sales)

| Fact | Field | Owner | Changing event | Consumers | Status |
|---|---|---|---|---|---|
| A quotation exists | `sale.order`, `state='draft'/'sent'` | Sale | `create()` / `action_quotation_sent()` | none cross-module | VERIFIED FACT |
| A sale is committed | `sale.order.state='sale'` | Sale | `action_confirm()` (SO-13..16) | Inventory (procurement launch), Accounting (eventual invoice) | VERIFIED FACT |
| Commercial terms are frozen | `sale.order.locked` | Sale | `action_lock()` (auto or manual, SO-17/21) | Sale itself (8 protected line fields, SO-26/27) — no cross-module consumer found | VERIFIED FACT |
| Ordered quantity | `sale.order.line.product_uom_qty` | Sale | user input / `write()` | Inventory (procurement demand), Accounting (order-policy billing) | VERIFIED FACT |

## 02 — Physical Reality facts (Inventory)

| Fact | Field | Owner | Changing event | Consumers | Status |
|---|---|---|---|---|---|
| On-hand quantity | `stock.quant.quantity` | Inventory | `_update_available_quantity()` (AVL-QNT-04), only from move-line completion | Sale/Purchase read only via `product.qty_available` (AVL-09), never the quant directly | VERIFIED FACT |
| Reserved quantity | `stock.quant.reserved_quantity` | Inventory | `_action_assign()`→`_update_reserved_quantity()` | No `product.reserved_qty` field exists — only the complement `free_qty` surfaces (Phase 2 synthesis) | VERIFIED FACT |
| A move is planned | `stock.move`, non-done states | Inventory | `_action_confirm()`/`_action_assign()` | Sale/Purchase read `state`/`quantity` to derive delivered/received | VERIFIED FACT |
| A move is physically executed | `stock.move.line._action_done()` | Inventory | validation (`button_validate()`) | Sale's `qty_delivered` (SOL-26), Purchase's `qty_received` (POL-22/23) — **both read-only, neither module writes physical-movement facts** | VERIFIED FACT |
| A transfer is fully/partially done | `stock.picking.state` (derived, PICK-10) | Inventory | child-move state aggregation | `sale_order.delivery_status` (PDEL-02) re-derives its own header status from picking states — a SEPARATE, independently-computed fact, not a passthrough | VERIFIED FACT |
| Remaining supply (backorder) | `stock.picking.backorder_id` (self-referential) | Inventory | `_create_backorder_picking()` (BO-08) | **Neither Sale nor Purchase read this field** (Purchase confirmed by full-grep, POL-31) — remaining supply is independently re-derived by each commercial side from move state, not from the backorder record | VERIFIED FACT — genuine non-consumption |

## 03 — Financial Consequence facts (handoff into Accounting, interface-only per governance §19)

| Fact | Field | Owner | Changing event | Consumers | Status |
|---|---|---|---|---|---|
| Sale line is billable now | `sale.order.line.qty_to_invoice` | Sale | `_compute_qty_to_invoice()`, branches on `product.invoice_policy` (SOL-12) | `_prepare_invoice_line()` writes this verbatim as the invoice line's `quantity` (SOL-17) | VERIFIED FACT |
| Sale line has been billed | `sale.order.line.qty_invoiced`/`qty_invoiced_posted` | Sale, but **backward-derived** from Accounting | `_compute_qty_invoiced()` reads `account.move.line` (SOL-09/10) | A round-trip: Accounting owns the source data, Sale owns the derived field | VERIFIED FACT — two non-interchangeable variants, must pick one deliberately |
| Purchase line is billable now | `purchase.order.line.qty_to_invoice` | Purchase | `_compute_qty_invoiced()`, branches on `product.purchase_method` (POL-07) | Same round-trip pattern as Sale, mirrored for AP | VERIFIED FACT |
| Tax amount | computed via `account.tax.compute_all()` | Accounting (shared engine) | Both Sale (`tax_ids`, TAX-13/14) and Purchase (`tax_ids`, TAX-16/17) feed into it | Neither Sale nor Purchase computes tax itself | VERIFIED FACT; fiscal-position substitution's own base model file EVIDENCE_MISSING |

## 04 — Approval facts (the open governance question)

| Fact | Field | Owner (claimed by schema) | Owner (actually implemented) | Status |
|---|---|---|---|---|
| Sale order is approved | `sale_order.level1_approved_by`/`level2_approved_by` | Unknown — no model declares these fields | **No implementation found anywhere** — Sale's only real gate is state+product-presence; credit is advisory | EVIDENCE_MISSING — critical (Phase 3 §08 item 1) |
| Purchase order is approved | `purchase_order.level1_approved_by`/`level2_approved_by` PLUS the separately-real `_approval_allowed()` amount-threshold gate | Two DIFFERENT mechanisms coexist on one model | Real: `po_double_validation` (single amount-threshold, PO-06/08). Orphaned: the level1/level2 columns, zero source | EVIDENCE_MISSING for the orphaned half; VERIFIED FACT for the real half (Phase 4 §03) |
| Purchase request is approved | `purchase_request.state='approved'` PLUS orphaned `level1_approved_by` etc. | `purchase.request` module (native buttons) OR `multi_level_approval_configuration` (if data-configured) | The wizard-gate (PREQ-13) reads `purchase_request.state`, which is set by whichever mechanism is actually live — **this cannot be determined from source alone** | EVIDENCE_MISSING — the PR→PO conversion gate's true upstream authority is unresolved (Phase 4 §03/§05) |

**This section is the fact-ownership answer to the single largest open question in GROUP A research**: three
models (`sale_order`, `purchase_order`, `purchase_request`) each have a *claimed* two-level-approval fact owner
(the orphaned columns) that does not match any *actual* owning code anywhere in the source tree. Downstream
consumers of "is this approved" (the PR→PO wizard, PREQ-13, being the one case where approval state is a real,
sourced, hard gate) read `state`, not the orphaned columns — so the practical fact-ownership chain is intact
even though the elaborate two-level schema sitting alongside it is unexplained.

## 05 — Handoff points where ownership crosses a module boundary (summary)

| Handoff | From → To | Mechanism | Is it a hard dependency or advisory? |
|---|---|---|---|
| Commercial commitment → physical demand | Sale → Inventory | `stock.rule.run()` via Procurement tuple (indirect) | Hard — this is the only way a confirmed SO line produces a move |
| Purchase commitment → physical expectation | Purchase → Inventory | `stock.move.create()` (direct/synchronous) | Hard |
| Physical execution → commercial fulfillment | Inventory → Sale/Purchase | Read-only compute (`qty_delivered`/`qty_received`) | Advisory in the sense that Sale/Purchase never block on it directly, but the QUANTITY becomes an input to the next hard gate (invoicing) |
| Fulfillment quantity → billing eligibility | Sale/Purchase → Accounting | `qty_to_invoice` written verbatim onto the invoice/bill line | Hard |
| Billing → re-derived invoiced quantity | Accounting → Sale/Purchase | Backward read of posted `account.move.line` | Hard (drives `invoice_status`, which drives whether more can be invoiced) |
| Demand signal → commercial commitment | Purchase Request → Purchase Order | Wizard, hard-gated on `state=='approved'` | Hard |
| Sale line → auto-generated Purchase commitment | Sale → Purchase (subcontract/dropship) | `sale_purchase`/`sale_purchase_stock` write path (`sale_line_id`) | Hard, but scoped to specific product configurations (`service_to_purchase`, dropship routes) — not the general case |

## 06 — Never-Assume-Equivalence reminders (governance §13 compliance)

- **A confirmed Sale order (`state='sale'`) does NOT mean a delivery move exists yet** — `_action_confirm()` is
  empty in base `sale`; the move is created by `sale_stock`'s override, and even then only for `consu`-type lines
  (Sales SO-16, SVS-06).
- **A confirmed Purchase order does NOT mean stock has arrived** — `qty_received` stays 0 until a move reaches
  `done`, regardless of `state='purchase'`.
- **A `done` stock move does NOT mean an invoice/bill has been posted** — `qty_to_invoice` is a separate compute
  that may fire immediately (order-based policy) or only after delivery/receipt (delivery/receive-based policy) —
  the two are never conflated in the source, and this research does not conflate them either.
- **An "approved" `purchase.request` does NOT prove which system actually approved it** — see §04 above.
