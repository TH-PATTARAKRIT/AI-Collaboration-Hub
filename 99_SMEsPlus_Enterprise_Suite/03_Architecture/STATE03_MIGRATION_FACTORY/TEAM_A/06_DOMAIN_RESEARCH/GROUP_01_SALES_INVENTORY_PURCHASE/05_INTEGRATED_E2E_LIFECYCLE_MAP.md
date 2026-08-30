> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 5 of 10 — Cross-Module E2E Reconciliation
> Synthesizes Phases 1-4 (`01_SHARED_MASTER_DEPENDENCY_MAP.md` through `04_PURCHASE_CAPABILITY_MODEL.md`) plus the
> Phase 5 gap-closure research on `stock.rule` and `purchase_order_line.sale_line_id`
> (`group_a_phase5_mto_dropship_chain.md`, evidence IDs RULE-*/SLID-*). No new source claims are made here beyond
> what those documents already established — this document connects them into the 12 scenarios required by
> governance §12. Evidence status per scenario is stated explicitly; scenarios not directly evidenced are marked
> `NOT OBSERVED / EVIDENCE_MISSING` rather than assumed.

# 05 — INTEGRATED E2E LIFECYCLE MAP

## 00 — Method

Each scenario below is assembled strictly from already-cited evidence IDs. Where a step in the chain was not
independently verified (e.g., the exact `stock_move.py` re-trigger call site for `make_to_order`), it is marked
`EVIDENCE_MISSING` inline rather than assumed to work a particular way.

---

## Scenario 1 — Buy → Receipt → Stock → Sell → Reserve/Fulfill → Deliver

```
purchase.order confirmed (PO §02 PO-04/06/07)
  → state='purchase', product.supplierinfo updated (PO-04)
  → purchase_order_line._create_stock_moves() creates stock.move DIRECTLY/SYNCHRONOUSLY (Phase 2 GRPA-01/02)
      into WH/Stock (or via put-away rule, Phase 2 PA-04 if configured)
  → receipt validated: stock.move.line._action_done() → _synchronize_quant() → stock.quant.quantity++ (Phase 2 RES-15/17)
  → purchase_order_line._prepare_qty_received() sums the now-done move (Phase 4 POL-22/23)
  → product.qty_available reflects the new on-hand (Phase 2 AVL-09)

sale.order confirmed (Sales §02 SO-13..16)
  → state='sale'; _action_confirm() empty in base sale, delegated to sale_stock (SO-16/SO-25)
  → sale_order_line._action_launch_stock_rule() builds a Procurement and calls stock.rule.run() (Phase 2 GRPA-04/05)
  → stock.rule._get_rule() resolves the applicable rule by walking the customer-location hierarchy (Gap-closure RULE-15)
  → matched 'pull' rule (procure_method='make_to_stock') → _run_pull() creates ONE stock.move,
      WH/Stock → Customer, no chaining (Gap-closure RULE-09/10, "plain outgoing move" path)
  → reservation: stock.move._action_assign() claims quant via stock.quant._get_reserve_quantity() (Phase 2 RES-07/AVL-QNT-03)
  → delivery validated: stock.move.line._action_done() decrements source quant, increments Customer quant (Phase 2 RES-17)
  → sale_order_line._compute_qty_delivered() (method='stock_move') sums the done outgoing move (Sales §03 SOL-26)
```

**Evidence status: VERIFIED FACT** for every step except the exact `stock_move.py` call site that would re-trigger
`stock.rule.run()` if the matched rule were `make_to_order` instead of `make_to_stock` — that specific re-trigger
line is `EVIDENCE_MISSING` (Gap-closure synthesis, Gap 1 item 3). The chaining data model it would use
(`move_dest_ids`/`move_orig_ids`, DB-backed by `stock_move_move_rel`) is independently confirmed to exist (RULE-09/10,
DB cross-check).

## Scenario 2 — Sales Demand → Shortage/Supply Need → Purchase/Replenishment → Receipt → Fulfillment

```
Two independent trigger paths, both evidenced, neither dependent on the other:

(a) Reordering rule (stock.warehouse.orderpoint, Phase 2 REPL-01..15):
    forecast < min_qty → _procure_orderpoint_confirm() builds a Procurement, calls stock.rule.run()
    → _get_rule() may resolve a 'buy' rule (contributed by purchase_stock, Phase 2 REPL-10/11) at the
      warehouse's input/receiving location
    → run()'s dispatch treats 'buy' identically to 'pull'/'push' (Gap-closure RULE-13) — calls _run_buy()
      (not opened in any phase; purchase_stock's own body, EVIDENCE_MISSING on its exact implementation,
      but its EXISTENCE and dispatch contract are fully confirmed)
    → _run_buy() presumably creates a purchase.order (this exact creation code was never opened in this
      research effort — SUPPORTED INFERENCE from the dispatch contract, not a directly-read fact)

(b) Purchase Request path (Phase 4 PREQ-19/20/21): a product flagged product_template.purchase_request=True
    routes the same reordering signal into a purchase.request instead of a plain RFQ (stock_rule.py's
    create_purchase_request(), Phase 4 PREQ-19) — this is a DIFFERENT fork of the same orderpoint trigger,
    selected per-product, not per-warehouse or per-company.

Either path converges back on purchase.order confirmation (Scenario 1's PO half), receipt, and on-hand increase.
```

**Evidence status**: the trigger conditions (REPL-05, orderpoint forecast check) and the dispatch mechanism
(RULE-13) are VERIFIED FACT. The actual body of `_run_buy()` (what fields it sets on the new PO) was **never opened
in any phase of this research** — flagged as `EVIDENCE_MISSING`, a genuine gap for a future pass, not filled in
here. The Purchase Request fork is fully evidenced (Phase 4 §05).

## Scenario 3 — Partial PO Receipt / Remaining Supply

```
purchase.order confirmed, stock.move created for full product_qty (Scenario 1)
  → warehouse receives less than ordered → stock.move.line._action_done() only for the picked quantity
  → stock.picking._check_backorder() (Phase 2 BO-04, picking_type.create_backorder policy) flags the shortfall
  → _create_backorder_picking() splits unfinished moves onto a NEW stock.picking, backorder_id set (Phase 2 BO-08)
  → purchase_order_line.qty_received reflects only the done portion (Phase 4 POL-22/23, done-moves-only sum)
  → remaining demand stays open on the ORIGINAL PO line — Purchase tracks "remaining supply" implicitly via
    not-done stock.move records, NEVER via stock.picking.backorder_id itself (Phase 4 POL-31, confirmed
    by full-file grep — Purchase-side code never references backorder_id)
```

**Evidence status: VERIFIED FACT.** Notable finding carried forward: Purchase's own line-level "remaining supply"
bookkeeping is entirely independent of the Inventory-side backorder record that is simultaneously being created
for the same physical shortfall — two parallel, unlinked views of the same partial event.

## Scenario 4 — Partial SO Delivery / Remaining Obligation

```
sale.order confirmed, delivery move created (Scenario 1)
  → warehouse ships less than ordered → same backorder mechanism as Scenario 3 fires on the delivery picking
  → sale_order.delivery_status computed as 'partial' (Sales §07 PDEL-01/02: requires a done picking AND
    at least one line with qty_delivered > 0)
  → sale_order_line.qty_to_deliver = product_uom_qty - qty_delivered, live recompute, never stored (PDEL-03/04)
  → remaining obligation is NOT a persisted line-level status — only the header delivery_status is durable
    (Sales §07 synthesis: "partial delivery is a header-only persisted concept")
```

**Evidence status: VERIFIED FACT.**

## Scenario 5 — Customer Return

```
Delivery already state='done' (a precondition, Phase 2 RET-02: "only a fully Done picking is returnable")
  → user opens Inventory's generic return wizard (stock.return.picking, Phase 2 §06) FROM THE DELIVERY, not
    from the Sale order (Sales §05 SRET-02/08: confirmed, no dedicated Sale Return button exists at all)
  → wizard swaps source/dest locations, creates a new stock.picking + stock.move,
    stock.move.origin_returned_move_id links back to the original move (Phase 2 RET-07)
  → sale_stock's ONLY participation: two small wizard overrides re-stamp sale_id/sale_line_id onto the new
    picking/move so the FK trail survives (Sales §05 SRET-04/05/06) — Sale does not initiate or gate the return
  → sale_order_line._update_line_quantity() blocks reducing ordered qty below delivered qty, redirecting the
    user to "create a return in your inventory instead" (Sales §05 SRET-07) — the only Sale-side "return" text
    that exists anywhere in this source tree
```

**Evidence status: VERIFIED FACT.** This is the single cleanest, most fully-closed scenario in the entire
research effort — both the mechanism and its negative claim (no Sale-side return feature) are full-file-grep
confirmed.

## Scenario 6 — Vendor Return

```
Receipt already state='done' (implicit precondition, same underlying stock.picking mechanism as Scenario 5)
  → user opens the SAME generic Inventory return wizard, this time creating a move whose destination location's
    usage='supplier' (Phase 4 POL-29: stock.move._is_purchase_return() IS this exact predicate — a pure
    location-usage check, no dedicated model or button)
  → Purchase's ONLY participation: _prepare_qty_received()/_get_outgoing_incoming_moves() recognize such a
    move AFTER THE FACT and net it out of (or back into) qty_received/procurement demand (Phase 4 POL-23/27)
  → confirmed, full-file-grep: Purchase has NO dedicated return-to-vendor button/wizard/model anywhere
    (Phase 4 POL-30) — the exact structural mirror of Scenario 5, arguably even less Purchase-owned since
    Purchase doesn't even carry a "view return" smart button (dropship gets one, POL-35, returns don't)
```

**Evidence status: VERIFIED FACT.** Scenarios 5 and 6 are structurally identical: "Return" as a concept belongs
entirely to Inventory in this codebase, regardless of which commercial document originated the transaction.

## Scenario 7 — Cancellation Before/After Confirmation

```
BEFORE confirmation (state in draft/sent, both Sale and Purchase):
  → action_cancel()/button_cancel() only checks 'locked' (Sales SO-22/PO §04 PO-35) and, for Purchase,
    outstanding vendor bills (PO-10) — neither check is normally triggerable pre-confirmation since neither
    a draft/sent order nor a service typically HAS a bill or is locked yet
  → sets state='cancel'; no stock/move interaction in either base module (Sale SO — Purchase base has
    zero direct stock.picking touch either, PO §04 synthesis)

AFTER confirmation (state='sale'/'purchase'):
  → Sale: sale_stock._action_cancel() cancels picking_ids.filtered(state != 'done') — DONE pickings
    explicitly spared (Sales §04 CANC-13/14)
  → Purchase: base button_cancel() has NO direct stock interaction in files read; whether purchase_stock
    cascades into receipts the same way sale_stock does is EVIDENCE_MISSING (Phase 4 §04 synthesis,
    explicitly flagged as not opened)
  → Both: a cancelled order can be reset to draft (Sale via action_draft() restricted to cancel/sent origin,
    SO-18; Purchase via button_draft() with NO state precondition at all — PO-09, a genuine asymmetry) and
    re-confirmed; Sale's re-confirmation is TEST-CONFIRMED to create a brand-new picking, never reviving
    the cancelled one (Sales CANC-17)
```

**Evidence status: VERIFIED FACT for Sale's full cycle** (test-confirmed). **EVIDENCE_MISSING for Purchase's
post-confirmation stock cascade** — genuinely not resolved by this research effort; flagged for a future pass
before any Fit-Gap conclusion assumes symmetry with Sale.

## Scenario 8 — Cancellation After Reservation/Expected Receipt

```
A reserved (assigned) but not-yet-done delivery/receipt move, upon its picking's cancellation:
  → stock.move._do_unreserve() releases the reservation by deleting non-picked move lines (Phase 2 MOV-22)
  → stock.move._action_cancel() itself REFUSES to cancel a done move (raises UserError, instructing a return
    instead — Phase 2 MOV-31) — this only applies to NOT-YET-done moves, consistent with Scenarios 5/6's
    "return, not cancel" rule for completed movement
  → On the commercial side: Sale's cancellation reaches this state via sale_stock._action_cancel() (Scenario 7);
    Purchase's reach into this state is EVIDENCE_MISSING (same gap as Scenario 7)
```

**Evidence status: VERIFIED FACT for the Inventory-side mechanics.** The commercial-side trigger for Purchase
remains an open gap (see Scenario 7).

## Scenario 9 — Correction After Partial Physical Movement

```
A stock.move.line already partially done cannot itself be "corrected" by deleting — done/cancel lines are
IMMUTABLE, undeletable (Phase 2 MOVL-15: "That would be like going back in time..."). Editing a DONE line's
quantity/location instead UNDOES and REDOES the actual quant transfer in place (Phase 2 MOVL-14) — a genuine,
sourced "correction" mechanism, but one that operates by re-executing the physical transfer, not by adjusting
a status flag.

On the commercial side, both Sale and Purchase log (chatter) rather than block quantity edits after partial
movement: Sale's write() override posts a comparison note (Sales SOL-18); Purchase's write() override does the
same (Phase 4 POL-15) — NEITHER blocks the edit outright. The one hard guard found is sale_stock-specific:
reducing ordered qty below already-delivered qty raises UserError, redirecting to a return (Sales SVS-07/SRET-07)
— Purchase has NO equivalent guard found in files read (a real, sourced asymmetry, not verified as intentional).
```

**Evidence status: VERIFIED FACT.**

## Scenario 10 — Correction After Complete Physical Movement

```
Once a move/line is fully done, correction is ONLY possible via the Return mechanism (Scenarios 5/6) — there is
no "edit a done move" path other than the undo/redo-in-place behavior of MOVL-14 (Scenario 9), which is really
a form of "still touching an in-progress line," not a fully-closed one. A picking's state, once 'done', can
only be reversed by creating a Return (RET-02: "_can_return() = state=='done'"); there is no "un-confirm a done
picking" action anywhere in the source read across any phase of this research.
```

**Evidence status: VERIFIED FACT (as a negative claim — no such mechanism was found in any phase's full-file
reads/greps).**

## Scenario 11 — Multi-Warehouse / Location / Company Context

```
Every model in this domain scopes primarily by company_id, with warehouse_id as a secondary, often-derived
dimension:
  - stock.warehouse: required + IMMUTABLE company (Phase 1 WH-03/10)
  - stock.location: OPTIONAL company (nullable = shared across companies, WH-16)
  - stock.quant: company/warehouse both DERIVED from location_id, never independently set (Phase 2 QNT-02/03)
  - sale.order / purchase.order: company_id required, both call res.company._accessible_branches() to police
    cross-branch product usage on lines (Phase 1 CO-27/CO-29)
  - "Branch" in this codebase = a child res.company record (Phase 1 CO-04) — NOT a separate warehouse/location
    dimension. A completely SEPARATE, unrelated "Thai Tax Branch" concept (a flat Char field on res.partner)
    has ZERO connection to Warehouse/Location or to the Company/Branch hierarchy (Phase 1 CO-15..24)
  - product.qty_available/virtual_available default to ALL warehouses of the active company set when no
    context is given (Phase 2 AVL-14) — the same product can report different numbers under different
    company contexts on identical underlying quant rows
```

**Evidence status: VERIFIED FACT.** This is a heavily-evidenced area across Phases 1-2; no new claims made here.

## Scenario 12 — Downstream Financial/Tax Dependency (interface observation only, per governance §19)

```
Sale → Accounting: qty_to_invoice feeds account.move.line.quantity verbatim (Sales SOL-17); qty_invoiced/
  qty_invoiced_posted read back from posted account.move.line records (SOL-09/10) — a round-trip dependency.
  Tax computed via the shared account.tax.compute_all() engine (Phase 1 TAX-09), fiscal-position substitution
  via account.fiscal.position.map_tax() (Phase 1 TAX-14/17) — that model's OWN base file was never located in
  this source tree (Phase 1 TAX synthesis, EVIDENCE_MISSING).

Purchase → Accounting (AP): qty_invoiced/qty_to_invoice computed from posted vendor-bill lines, gated by
  product.purchase_method (Phase 4 POL-06/07/08) — the AP-side structural analogue of Sale's invoice_policy.

Neither Sale nor Purchase performs its own GL posting logic — both hand a quantity + tax set to the shared
account.move/account.tax engine and read status back. This research does NOT reopen Accounting Core's own
posting-lifecycle findings (already researched separately, DOMAIN_01_ACCOUNTING_CORE/) — it only confirms the
HANDOFF POINTS from Sales/Purchase into that engine.
```

**Evidence status: VERIFIED FACT for the handoff points.** Full posting-lifecycle mechanics are out of GROUP A's
scope by design (governance §19: interface/dependency observation only).

---

# Cross-scenario notes

- **Scenarios 5 and 6 are the strongest, most fully-closed findings in this entire phase** — both are confirmed by
  exhaustive negative greps, not just positive citations.
- **The weakest link across all 12 scenarios is the Purchase-side cancellation cascade into `stock.picking`**
  (Scenario 7/8) and the exact body of `_run_buy()` (Scenario 2) — both explicitly carried forward as
  `EVIDENCE_MISSING`, not filled in with plausible-sounding inference.
- **The orphaned two-level approval schema (Phase 3/4) sits upstream of every scenario that begins with
  "confirmed"** — none of the 12 scenarios above required or found evidence of that mechanism actually gating
  any of these flows; it remains a separate, unresolved governance question, not a blocking factor for this map.
