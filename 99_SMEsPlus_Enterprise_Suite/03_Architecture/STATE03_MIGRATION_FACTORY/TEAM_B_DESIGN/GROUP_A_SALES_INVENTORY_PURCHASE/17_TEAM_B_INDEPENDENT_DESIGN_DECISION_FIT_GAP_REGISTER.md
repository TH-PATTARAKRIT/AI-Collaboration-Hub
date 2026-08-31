> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 11 — Independent Fit-Gap / Design Decision Consolidation

# 17 — TEAM B INDEPENDENT DESIGN DECISION / FIT-GAP REGISTER

## 00 — Method

Every Team A Fit-Gap candidate (`16_FIT_GAP_CANDIDATE_PACK.md`) is addressed below with TEAM B's own,
independently-reasoned decision. Per governing prompt §5, TEAM B does not write "Team A said X, therefore
SMEsPlus shall X" — each row states what the evidence supports and what TEAM B concludes, including every case of
agreement, disagreement, or reclassification.

## 01 — Core Capability Candidates (Team A items 1–7)

| # | Team A Candidate | TEAM B Independent Decision | Agree/Disagree | Where designed |
|---|---|---|---|---|
| 1 | Quotation/order as one lifecycle-distinguished document | `ADAPT` | Agree — independently confirmed the same reasoning: splitting would require re-establishing identity at commitment for no corresponding benefit | [06](06_SALES_CANONICAL_DESIGN.md) §01 |
| 2 | Amount-threshold approval gate | `ADAPT` | Agree | [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) §02 |
| 3 | Quantity quadruple with policy-driven billing fork | `ADAPT` | Agree, generalized to both Sales and Purchase symmetrically | [11](11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md) |
| 4 | Backorder as self-referential link, not a separate model | `ADAPT` | Agree | [05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §05 |
| 5 | Return as one generic Inventory mechanism for both directions | `ADAPT` | Agree — TEAM B independently confirms this is the strongest-evidenced pattern in the whole package | [05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §05 |
| 6 | Reflective/pluggable replenishment-to-fulfiller dispatch, as an architecture pattern | `ADAPT` (pattern only, not the literal mechanism) | Agree, with the explicit caveat Team A itself raised (pattern, not literal mechanism) — TEAM B additionally generalizes it to any future fulfillment domain (e.g., Manufacturing), not just Purchase | [05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §07 |
| 7 | Physical count fused into the same ledger row as on-hand quantity | Team A: `UNKNOWN`. **TEAM B independently resolves this to a decision**: keep count-in-progress conceptually distinct from the settled on-hand ledger fact, even if a future schema implementation stores them adjacently — a count-in-progress is a Commitment-type fact (a proposed correction awaiting reconciliation), not yet a Physical fact | **Disagree with leaving it UNKNOWN** — TEAM B resolves it using the Commitment/Physical/Derived fact-type taxonomy already established in [03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md), which Team A's evidence-only mandate did not have available to it | [03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md) §00 fact-type taxonomy |

## 02 — Candidates Requiring Correction (Team A items 8–12)

| # | Team A Candidate | TEAM B Independent Decision | Agree/Disagree | Where designed |
|---|---|---|---|---|
| 8 | Two uncoordinated Thai branch modules — `REJECT` the duplication, `UNKNOWN` on the underlying requirement | TEAM B agrees on rejecting the duplication (one Tax-Branch attribute, not two competing implementations). The underlying Thailand-requirement half remains genuinely `Unknown / Requires Real-User Validation` — TEAM B does not resolve it, consistent with TBRAC discipline | Agree | [16](16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md) §01 item 1; [18](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md) |
| 9 | Two uncoordinated `default_code` generators — `REJECT` the collision, underlying need may be `ADAPT`-worthy | `REJECT` the dual-writer pattern; `ADAPT` a single, canonical SKU-generation capability owned by Product/Service | Agree | [04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md) §02 |
| 10 | Over-receipt/over-delivery unguarded — Team A: `UNKNOWN` | TEAM B resolves this to a decision rather than leaving it open: `EXTEND` — introduce an explicit, configurable Over-Fulfillment Policy | **Disagree with leaving it UNKNOWN** — TEAM B judges "no system reaction to any quantity mismatch" as a real enough operational risk that the *existence* of a policy (not its default value) is decidable now | [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §02 |
| 11 | Inconsistent sequence-fallback sentinel — `REJECT` | `REJECT`, requiring one consistent fallback across both domains | Agree | [04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md) §04 |
| 12 | Dual vs. single cancellation gate — Team A: `UNKNOWN` | TEAM B resolves this: `ADAPT` both gates as evidenced (not a defect) — an outstanding vendor financial exposure is a materially different, legitimately-stricter blocking condition than a merely-drafted customer invoice | **Disagree with leaving it UNKNOWN** — TEAM B judges this resolvable from the business-semantic difference alone, without needing further evidence | [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §07 |

## 03 — Two-Level Approval Schema (Team A item 13)

| # | Team A Candidate | TEAM B Independent Decision | Agree/Disagree | Where designed |
|---|---|---|---|---|
| 13 | `EXTEND` on the Internal-Demand-Request half (confirmed active use); `UNKNOWN` remains on the Purchase-Commitment half and the Sales half (small sample) | TEAM B agrees with the mixed classification but designs **one shared, vendor-neutral Approval Control concept** usable by all three document types rather than three separately-shaped mechanisms — a generalization Team A's evidence-only mandate did not attempt. Internal workflow logic remains `HOLD` for all three, per governing prompt §11 | Agree on classification; extends the design further than Team A's evidence-gathering mandate allowed | [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) §03 |

## 04 — Structural Gaps (Team A items 14–17)

| # | Team A Candidate | TEAM B Independent Decision | Agree/Disagree | Where designed |
|---|---|---|---|---|
| 14 | Sale confirmation never gated by inventory availability — `UNKNOWN` | TEAM B resolves the **shape** of the decision (must be configurable) but explicitly defers the **default value** to Boss/business — a partial resolution, not a full one | Partial agree — TEAM B narrows the Unknown to "what default," not "whether a policy concept should exist" | [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) §04 |
| 15 | No dedicated commercial-side Return object — `EXTEND` candidate, resting partly on an unsourced "many SME businesses expect..." generalization | TEAM B accepts the underlying design question as genuinely open but explicitly **does not treat Team A's rationale as evidence** — per Boss Gate §4.3, that sentence is a `HYPOTHESIS / REQUIRES REAL USER VALIDATION`, not a finding. TEAM B's own position: the Inventory-owned Reversal mechanism (`ADAPT`ed in full) is sufficient as designed; whether to additionally add a Sales-initiated RMA *affordance* is left open, pending real-user validation, not pre-decided in either direction | Agree the question is open; disagrees with using the unsourced rationale to justify a direction | [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §05; [16](16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md) §04 |
| 16 | Demand-request approval traceability — Team A: depends on resolving #13 | Same disposition as #13 — traceability requirement (§05 SoD data-shape) is designed now; internal logic remains `HOLD` | Agree | [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) §05 |
| 17 | Requisition-vs-Tender naming trap — `REJECT` | `REJECT`, with two explicitly separate concepts named (Standing Supply Agreement vs. Multi-Vendor Comparison) | Agree | [07](07_PURCHASE_CANONICAL_DESIGN.md) §05 |

## 05 — Summary Counts

- **ADAPT**: 8 (items 1–6, 9's canonical-SKU half, 12)
- **EXTEND**: 4 (item 10, item 13's shared-concept design, item 14's policy-shape half, item 16's SoD-shape half)
- **REJECT**: 4 (item 8's duplication half, item 9's collision half, item 11, item 17)
- **Genuinely left OPEN** (not resolved by TEAM B, correctly so): item 8's underlying Thailand-requirement half,
  item 14's default value, item 15's RMA-affordance direction, item 13/16's internal workflow logic (`HOLD` per
  governing prompt §11).
- **TEAM B resolved beyond Team A's own classification** (items 7, 10, 12): three cases where TEAM B judged the
  evidence sufficient to make a decision Team A had left as `UNKNOWN`, using reasoning tools (the fact-type
  taxonomy, the risk-of-silent-mismatch argument, the business-semantic-asymmetry argument) that were available
  to TEAM B's design mandate but not to Team A's evidence-only mandate.

No item above was silently dropped; every Team A candidate (1–17) has an explicit TEAM B disposition.
