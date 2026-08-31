> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 10 of 10 — Fit-Gap Candidate Pack
> Per governance §21: Reference Observation → Generic Business Semantic → SMEsPlus Downstream Decision Candidate
> (ADAPT / EXTEND / REJECT / UNKNOWN). Team A does NOT make final target-design decisions — every "Candidate"
> column below is a classification proposal for Team B / Boss review, not a ruling.

# 16 — FIT-GAP CANDIDATE PACK

## 01 — Core capability candidates (things that work and are candidates to adapt)

| # | Reference Observation | Generic Business Semantic | Candidate | Rationale |
|---|---|---|---|---|
| 1 | One model serves both quotation and committed order, distinguished by `state` (Sales SO-01) | Quotation-to-order is a lifecycle, not a document-type change | **ADAPT** | Simple, evidenced, no material downside found |
| 2 | Purchase's amount-threshold approval gate (`po_double_validation`), real and test-confirmed | Self-approval limits by transaction value | **ADAPT** | Working, sourced, test-confirmed mechanism — a clean pattern to reuse |
| 3 | Quantity quadruple (ordered/delivered/invoiced/to-invoice) with a policy-driven billing fork | Fulfillment and billing must be trackable independently, with a configurable trigger | **ADAPT** | Core to any Sales/Purchase backbone; well-evidenced on both sides |
| 4 | Backorder as a self-referential document link rather than a separate model | Partial fulfillment splits remaining demand without losing the original document's identity | **ADAPT** | Simple, proven, avoids a proliferation of document types |
| 5 | Return as a single generic Inventory mechanism serving both customer and vendor directions | One return concept, reached from either commercial side by the same wizard/logic | **ADAPT** | The most cleanly evidenced pattern in this entire research effort — genuinely elegant |
| 6 | `stock.rule`'s reflective `_run_<action>` dispatch — core Inventory has zero compile-time knowledge of Purchase | Extensible fulfillment-source resolution without coupling the core engine to every possible source type | **ADAPT** (as an architecture pattern, not literally the Python mechanism) | Confirmed clean module-boundary discipline; worth preserving the SHAPE of this decoupling even if the target isn't Python/Odoo |
| 7 | Physical count workflow fused into the same ledger row as the on-hand quantity (`stock.quant`) | Inventory count-and-adjust is not a separate document type from the on-hand ledger itself | **UNKNOWN** | Works in source, but conflates two concerns (ledger + count-in-progress) in one row — a target design may reasonably prefer separation |

## 02 — Candidates requiring correction, not adoption

| # | Reference Observation | Generic Business Semantic | Candidate | Rationale |
|---|---|---|---|---|
| 8 | Two independent, uncoordinated Thai "branch" modules on the same field concept | A single business fact (tax-branch registration) should have one source of truth | **REJECT** (as observed) — do not replicate the duplication; **UNKNOWN** whether the underlying Thai tax-branch requirement itself should be adapted | The duplication is a defect pattern in the source, not a design worth preserving |
| 9 | Two independent modules both auto-generate `product.default_code` by different rules (Phase 1) | SKU auto-numbering | **REJECT** (the dual-writer collision) — the underlying "auto-generate SKU" need may still be **ADAPT**-worthy in isolation | Collision risk is a defect, not a feature |
| 10 | Over-receipt/over-delivery is completely unguarded on both Sale and Purchase lines | Whether exceeding ordered quantity should be blocked, warned, or silently allowed | **UNKNOWN** | A real design decision SMEsPlus must make deliberately — the source's silence here is not evidence that silence is correct |
| 11 | Sequence fallback sentinel differs between Sale (`"New"`) and Purchase (`"/"`) with no functional reason found | Placeholder-before-numbering convention | **REJECT** (as an inconsistency) — pick ONE sentinel for the target | A genuine inconsistency, not a business rule |
| 12 | Purchase's cancellation gate is dual (locked OR open vendor bill); Sale's is single (locked only) | Cancellation preconditions | **UNKNOWN** | Could be intentional (AP exposure is a harder blocker than AR) or accidental — not resolvable from source alone |

## 03 — The two-level approval schema — RECLASSIFIED (was the pack's highest-priority UNKNOWN)

| # | Reference Observation | Generic Business Semantic | Candidate | Rationale |
|---|---|---|---|---|
| 13 | ~~A complete two-level manager-approval DB schema exists on three models with zero implementing source anywhere~~ **UPDATED (CORR-003)**: identified as three real, actively-installed modules (`sale_order_level_approve` first-party; `purchase_request_level_approve_po`/`purchase_request_level_approve` third-party "BH Pro International"), with genuine historical usage confirmed on Purchase Request and partial usage (approver-assignment only) on Purchase Order | Sequential, per-person, auditable approval with a reject reason — **now known to be a real, working, historically-used feature**, not hypothetical schema | **EXTEND** (upgraded from UNKNOWN) — on top of Purchase's already-working single-threshold gate (`po_double_validation`), for Purchase Request specifically, where live data shows genuine use (1,945 approved, 96 rejected of 2,199 records). **UNKNOWN remains** for Purchase Order specifically, since `level1_approved_by` is populated on 0 of 27,874 rows there — it's unclear whether the "approval recording" half of that workflow was ever actually completed in practice vs. only the "assign an approver" half. Sale Order's version has only 2 historical records — sample too small to classify with confidence. | Source code for the three modules is still needed (action item raised in `04_PURCHASE_CAPABILITY_MODEL.md` §03) before Team B can design against this with full confidence — the DATA proves the feature is real and was used; it does not yet prove every workflow rule inside the modules. |

## 04 — Structural gaps found (things the source does NOT do, worth a deliberate SMEsPlus decision)

| # | Reference Observation | Generic Business Semantic | Candidate | Rationale |
|---|---|---|---|---|
| 14 | Sale confirmation is never gated by inventory availability | Whether promising a sale should require a stock check | **UNKNOWN** | A material customer-facing behavior choice; the source's choice (advisory-only) is not necessarily wrong, but must be a deliberate SMEsPlus decision, not an inherited default |
| 15 | Neither Sale nor Purchase has a dedicated Return object/button | Whether SMEsPlus wants a commercial-side "Return" UX (e.g., a Sales-initiated RMA flow) distinct from a pure warehouse action | **EXTEND** candidate | The source's Inventory-only model works but is warehouse-centric; many SME businesses expect a salesperson-initiated RMA — this is a plausible extension point, explicitly flagged as a candidate rather than a finding of a defect |
| 16 | No hard link between "approved" `purchase.request` state and a specific verifiable approval authority (native buttons vs. an unconfirmed external engine) | Demand-signal approval traceability | **UNKNOWN** | Depends entirely on resolving item #13 |
| 17 | `purchase.requisition`'s manifest promises tendering but the real mechanism lives elsewhere on `purchase.order` | Documentation/naming clarity | **REJECT** (as a naming trap) for target design — do not name a target concept "Requisition = Tender"; the semantics are genuinely different in this source and should not be conflated | Confirmed manifest-vs-code mismatch |

## 05 — Explicitly deferred (Accounting Core territory, interface-only per governance §19)

Tax computation, WHT, payment execution, and inventory valuation are NOT classified here — GROUP A's role is to
observe the HANDOFF POINTS (already documented in `07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md`), not to
propose Fit-Gap candidates for Accounting Core's own domain.

## 06 — Summary counts

- **ADAPT candidates**: 6 (items 1-6)
- **UNKNOWN candidates**: 6 (items 7, 10, 12, 14, 16, plus the underlying-requirement half of 8) — item 13 is
  reclassified below and no longer counted here
- **REJECT candidates**: 5 (items 8's duplication, 9's collision, 11, 17, plus the naming-trap noted in 17)
- **EXTEND candidates**: 2 confirmed (item 15; item 13's Purchase-Request half, upgraded from UNKNOWN by CORR-003
  dump forensics), 1 remaining UNKNOWN sub-item (item 13's Purchase-Order half, and Sale-Order's small-sample half)

**Updated (Session CORR-003)**: item 13 (the two-level approval schema) moved from a single "highest-priority
UNKNOWN" to a mixed classification — real and EXTEND-worthy on Purchase Request (confirmed active use), still
UNKNOWN on Purchase Order (assigned-but-never-approved pattern in the data) and Sale Order (sample too small).
See §03 above for the full breakdown.

No item above is a Team A decision. This pack is a classification PROPOSAL for Team B / Boss review, built
entirely from evidence already cited across Phases 1-9 of this research chain plus the CORR-003 corrective
follow-up.
