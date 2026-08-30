> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 6 of 10 — Exception / Partial / Return / Cancellation Catalogue
> Per governance §18: coverage follows material evidence and risk, not a fixed ratio. Synthesizes Phases 1-5.
> Every row cites an evidence ID already established elsewhere in this evidence chain.

# 10 — EXCEPTION / PARTIAL / RETURN / CANCELLATION MATRIX

| # | Exception | Observed in source? | Mechanism | Evidence | Status |
|---|---|---|---|---|---|
| 1 | Partial delivery (Sale) | Yes | `stock.picking._check_backorder()` splits unfinished moves; `sale_order.delivery_status='partial'` computed at header only | Phase 2 BO-04/08; Sales PDEL-01/02 | VERIFIED FACT |
| 2 | Partial receipt (Purchase) | Yes | Same backorder mechanism; Purchase tracks remaining supply implicitly via not-done moves, never via `backorder_id` | Phase 2 BO-08; Purchase POL-31 | VERIFIED FACT |
| 3 | Backorder (generic) | Yes | Backorder is not a separate model — `stock.picking` self-referencing itself via `backorder_id`; policy (`ask`/`always`/`never`) lives on `stock.picking.type` | Phase 2 BO-01..14 | VERIFIED FACT |
| 4 | Over/under receipt | Partially | No dedicated field/flag. Under-receipt handled via backorder (#2). Over-receipt is **never specially detected or blocked** — `_prepare_qty_received`'s stock-moves sum will happily exceed `product_qty` if more done moves exist | Purchase POL-24 | VERIFIED FACT (as a negative — genuinely unguarded) |
| 5 | Wrong item / wrong quantity | Not observed | No dedicated correction workflow found distinct from #9/#10 below (edit-in-place or return) | — | NOT OBSERVED / EVIDENCE_MISSING |
| 6 | Shortage (insufficient stock to fulfill) | Yes, but advisory only | Sale's availability widgets are read-only forecasts; confirmation is **not gated** by stock availability anywhere in the code read | Phase 2 GRPA-02/03/04; Sales synthesis | VERIFIED FACT |
| 7 | Late supply | Not directly observed | `stock.warehouse.orderpoint.get_horizon_days()`/deadline logic exists (Phase 2 REPL-05) but no "late" flag or SLA-breach handling was found on either PO or SO lines | Phase 2 REPL-05 (partial) | NOT OBSERVED beyond forecast/deadline computation / EVIDENCE_MISSING for any breach handling |
| 8 | Customer return | Yes — fully closed | Inventory-only generic wizard; Sale has **no dedicated Return feature at all** (full-grep confirmed); only participation is FK re-stamping + a redirect error message | Phase 2 RET-01..12; Sales SRET-01..08 | VERIFIED FACT — one of the two most fully-evidenced findings in this research effort |
| 9 | Vendor return | Yes — fully closed | Same generic wizard; detection is a pure `location_dest_id.usage=='supplier'` predicate on an ordinary move; Purchase has **no dedicated feature at all** (full-grep confirmed), arguably less than Sale (no smart button even) | Purchase POL-29/30 | VERIFIED FACT — structurally identical to #8 |
| 10 | Cancellation before confirmation | Yes | Both Sale and Purchase: state+product-presence gate only; `write({'state':'cancel'})`, no stock/invoice interaction needed since neither typically exists yet | Sales SO-22; Purchase PO-10 | VERIFIED FACT |
| 11 | Cancellation after confirmation | Yes, asymmetric between modules | Sale: `sale_stock` cancels not-done pickings, spares done ones (test-confirmed). Purchase: base has zero stock interaction; whether `purchase_stock` cascades is **EVIDENCE_MISSING** | Sales CANC-13/14/17; Purchase §04 synthesis | VERIFIED FACT for Sale; EVIDENCE_MISSING for Purchase |
| 12 | Cancellation after reservation | Yes | `stock.move._do_unreserve()` releases the reservation by deleting non-picked lines; a `done` move can never be cancelled (must be returned instead) | Phase 2 MOV-22/31 | VERIFIED FACT |
| 13 | Cancellation after partial movement | Yes | Same as #12 — the done PORTION of a move is immutable; only the not-done remainder can be cancelled/unreserved | Phase 2 MOV-22/31, MOVL-15 | VERIFIED FACT |
| 14 | Correction after completed movement | Yes | **Only** via the Return mechanism (#8/#9) — no "un-confirm a done picking" action exists anywhere in the source read across any phase | Phase 2 RET-02; cross-phase negative | VERIFIED FACT (negative claim, exhaustive across all phases) |
| 15 | Duplicate/retry behavior | Yes, one concrete instance | `stock.quant._merge_quants()` exists specifically because **concurrent transactions writing the same logical quant key can each insert a new row instead of updating one** — a real, sourced, expected-and-handled race condition | Phase 2 AVL-QNT-08 | VERIFIED FACT |
| 16 | Cross-warehouse/company cases | Yes | `_check_order_line_company_id()` (identical on Sale and Purchase) blocks order lines whose product's company is outside `_accessible_branches()`; quant/move company is always derived from location, never independently set | Phase 1 CO-27/29; Phase 2 QNT-02 | VERIFIED FACT |
| 17 | Missing/late documents | Not observed | No "missing document" detection or grace-period handling found in any phase | — | NOT OBSERVED / EVIDENCE_MISSING |
| 18 | Failure/recovery observations | Partial | `_ondelete_stock_moves` (Purchase) explicitly degrades gracefully via raw SQL if `purchase_stock` is ever uninstalled while lines reference it — a genuine, sourced recovery path, but narrow in scope (module-uninstall only, not transaction failure) | Purchase POL-19 | VERIFIED FACT for this one narrow case; broader transaction-failure recovery NOT OBSERVED |
| 19 | Line deletion after confirmation | Yes, both sides | Sale: line with invoice_lines cannot be deleted, must be zeroed instead (SOL-19). Purchase: identical pattern, cannot delete once `state=='purchase'` except display lines (POL-16) | Sales SOL-19; Purchase POL-16 | VERIFIED FACT — symmetric between the two modules |
| 20 | Approval rejection | Ambiguous | Purchase Request has a native `button_rejected()` wizard (single reason field); a **second**, orphaned `purchase_order_level_reject`/`purchase_request_level_reject` table pair exists with zero corresponding source, suggesting a more elaborate reject-with-audit-trail mechanism that cannot be confirmed as live | Purchase PREQ-08; PO-23/DBX-04 | VERIFIED FACT for the native wizard; EVIDENCE_MISSING for the orphaned mechanism |

## Cross-cutting observations

- **The two most exhaustively-verified exceptions in this entire GROUP A research effort are Customer Return (#8)
  and Vendor Return (#9)** — both closed by full-file greps proving a NEGATIVE (no dedicated commercial-side
  feature exists), not merely a positive citation. Any Fit-Gap candidate proposing a dedicated "Sales Return" or
  "Purchase Return" object should be evaluated against this evidence, not against assumption.
- **Over-receipt (#4) and late supply (#7) are the two clearest evidence gaps for a system that otherwise polices
  quantities carefully** — over-receipt is genuinely unguarded in source (not merely unresearched), which is
  itself a material finding, not an absence of research.
- **Cancellation-after-confirmation (#11) is the one exception where Sale and Purchase are NOT proven symmetric**
  — Sale's cascade into Inventory is test-confirmed; Purchase's equivalent was never opened. This is the single
  highest-value follow-up read for anyone continuing this research line, since every other cancellation-adjacent
  exception (#10, #12, #13) was confirmed symmetric or Inventory-owned regardless of commercial origin.
- **Approval rejection (#20) inherits the same orphaned-schema ambiguity documented at length in
  `04_PURCHASE_CAPABILITY_MODEL.md` §03** — not re-litigated here, only cross-referenced.
