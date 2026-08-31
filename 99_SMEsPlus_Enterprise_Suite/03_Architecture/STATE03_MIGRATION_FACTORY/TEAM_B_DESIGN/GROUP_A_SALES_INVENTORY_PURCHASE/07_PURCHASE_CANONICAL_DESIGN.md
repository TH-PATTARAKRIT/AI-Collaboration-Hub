> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 5 — Purchase Canonical Design

# 07 — PURCHASE CANONICAL DESIGN

## 01 — Supply Lifecycle

Canonical states: `Draft` → (`Sent`, engagement-tracking only, same non-behavioral status as Sales' `Sent`) →
[`Pending Approval`, conditional] → `Committed` → `Cancelled`; `Pending Approval` may also resolve to `Rejected`
instead of `Committed` (see the CORR-008 closure below) — with `Draft` reachable from any prior state, including
`Rejected` (TEAM B notes the reference system's unrestricted `button_draft()`-equivalent as a genuine, evidenced
**asymmetry** against Sales' more restricted return-to-draft — see §07 below for TEAM B's independent decision on
whether to preserve it). **CORR-010 precision fix (`FV006-STE-004`):** this enumeration previously omitted
`Rejected` even though it is a canonical state reachable from `Pending Approval` — Formal IBPV RV-009 found this
summary line was not updated when `Rejected` was introduced below, repeating a defect pattern the original
Formal IBPV FV-006 review had already caught once in this exact section (`FV006-STE-003`).

**`Pending Approval` is a genuine third phase Sales' lifecycle has no equivalent of** — TEAM B adopts this as a
real, evidenced business-semantic difference (not an accident), because Purchase's real approval gate
(§03) is a test-confirmed, working hard control, unlike Sales' advisory-only credit check. A Supply Commitment
that fails the approval-allowed check does not error — it transitions to `Pending Approval` and waits.

**CORR-008 closure (`FV006-STE-004` / `FV006-EVT-003`) — Approval-denial exit path.** `Pending Approval`
previously had no stated exit for a denied approval, leaving an open vendor-facing commitment with no closure
mechanism and, per Formal IBPV FV-006 Deliverables 04 and 05, a possible orphaned Inventory fulfillment request.
TEAM B independently designs the business-semantic closure below, without inventing the missing legacy modules'
internal trigger/permission logic — that internal logic remains `HOLD`, per §03 below and
[13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) §00/§03, and is unaffected by this closure:

- **Resulting state**: `Pending Approval` → `Rejected`, a new named state distinct from `Cancelled` — `Rejected`
  carries approval-denial semantics (one authorized approver's decision, with a mandatory reason) that a general
  `Cancelled` (withdrawal for any reason, by any authorized actor, at any stage) does not. `Rejected` is reachable
  only from `Pending Approval`.
- **Denial event**: `Supply Commitment Rejected` (added to [09](09_CANONICAL_BUSINESS_EVENT_CATALOG.md) §02) —
  reuses the generic Approval Control rejection-event shape already defined in
  [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) §03 (an approve/reject event with actor, timestamp, and a
  mandatory rejection reason), applied here specifically to the Supply Commitment document type.
- **Owner**: Purchase (the Supply Commitment document type), coordinated with the Approval Control concept
  ([13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) §02, APR-001 — the Amount-Threshold Approval control that
  actually produces the `Pending Approval`/`Rejected` transition; **not** §03's Sequential Level-Based Approval, a
  distinct control this document type does not use for this gate). **CORR-010 citation correction**: the
  pre-correction text named §03 here, which Formal IBPV RV-009 independently confirmed contains no reference
  anywhere to the `Rejected` state or the `Supply Commitment Rejected` event — the coordination is, and was always
  meant to be, with §02, which now carries the matching cross-reference (see
  [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) §02 Event Impact row).
- **Downstream demand withdrawal**: §03 below clarifies (also as part of this CORR-008 closure) that the
  Inventory-facing receipt fulfillment request is created directly/synchronously at Confirm time on **both**
  branches (`Committed` or `Pending Approval`), and held `Blocked` (not-yet-executed, non-actionable) for the
  `Pending Approval` branch specifically — see
  [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) §01. On denial, that already-created, not-yet-executed
  instruction is stood down using the **same** not-yet-executed-instruction cascade already defined for
  Cancellation ([08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) §05,
  [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §07) — no separate stand-down mechanism is
  invented; `Rejected` reuses the existing cascade rather than introducing a second one. This closes the
  orphaned-fulfillment-request risk both Deliverable 04 and Deliverable 05 of Formal IBPV FV-006 identified.
- **Audit history**: the rejection event's actor, timestamp, and reason are permanently retained on the Supply
  Commitment's history, consistent with every other rejection event in this design
  ([12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §14).
- **Resubmission / correction classification**: `Rejected` → `Draft` is permitted, consistent with the
  "`Draft` reachable from any prior state" rule stated above — a resubmitted commitment re-enters the lifecycle
  from `Draft` and, on re-confirmation, creates a fresh fulfillment request; it never resumes or reuses the
  rejected instance's withdrawn instruction. Whether a resubmitted commitment must restart at Approval Level 1 or
  may resume at the level it was rejected from is governed by the Approval Control's own internal transition
  logic, which remains `HOLD` — TEAM B does not invent an answer here, consistent with
  [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) §03.
- **Residual unknown, explicitly registered**: whether `Rejected` should auto-transition back to `Draft` or
  require an explicit manual resubmission action is a business-policy nuance, not a structural gap — the state,
  event, owner, downstream-withdrawal, and audit shape above are all structurally complete and do not depend on
  this nuance. TEAM B's default recommendation, absent a Boss ruling: require an explicit manual resubmission
  action (mirroring the manual-reset pattern already adopted for every other return-to-`Draft` transition in this
  design) rather than a silent auto-reset, since an unprompted state change immediately after a human rejection
  decision would itself be a control-integrity risk. Carried forward in
  [22_TEAM_B_CORR008_FINDING_CLOSURE_REGISTER.md](CORRECTIVE_CORR_008/22_TEAM_B_CORR008_FINDING_CLOSURE_REGISTER.md).

## 02 — Order Line and Quantities

Canonical quantities: **Ordered** (commitment), **Received** (derived, dispatched by fulfillment method, same
state-dependent-meaning pattern as Sales' Delivered — see [11](11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md)),
**Invoiced/Billable-Now** (derived, branches on a Purchase-specific billing policy field, structurally parallel
to but a **distinct field from** Sales' billing-policy — TEAM B keeps these as two independently-configurable
policies, since AP and AR billing bases can legitimately diverge per business, per
[03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md)).

**Independent decision — over-receipt policy**: evidence shows over-receipt is completely unguarded in the
reference system (no detection, no block). TEAM B does **not** carry this forward as the target default. TEAM B
requires an explicit, configurable over-fulfillment policy (block / warn-and-allow / allow-silently) applied
symmetrically to both Received (here) and Delivered ([06](06_SALES_CANONICAL_DESIGN.md)) — this closes Fit-Gap
candidate #10 with an actual decision rather than leaving it UNKNOWN, on the reasoning that "no system reaction to
a quantity mismatch" is a real operational risk regardless of which business ultimately configures it away. The
specific default (block vs. warn vs. allow) is left to Boss/business policy — TEAM B decides only that the policy
must exist and be explicit, not what its default value is.

## 03 — Purchase Approval — Two Genuinely Coexisting Mechanisms

TEAM B's independent classification, reasoned from evidence, not inherited from Team A's labels:

1. **Amount-threshold approval** — a real, working, test-confirmed hard gate: below a configured threshold, or
   for a user holding an approval-manager role, a commitment self-approves on confirmation; above it, or without
   the role, it lands in `Pending Approval` until an authorized user acts. TEAM B `ADAPT`s this pattern in full —
   it is simple, evidenced, and needs no correction. **CORR-008 clarification (`FV006-STE-004` /
   `FV006-EVT-003`, coordinated with §01 above):** the Inventory-facing receipt fulfillment request (§06 below)
   is created directly/synchronously at Confirm time regardless of which branch the commitment lands in; on the
   `Pending Approval` branch it is held `Blocked` until the gate resolves (unblocked on Approval, stood down via
   the standard not-yet-executed cascade on Rejection — see §01 above). This removes a prior internal ambiguity
   between this file and [09](09_CANONICAL_BUSINESS_EVENT_CATALOG.md) §02 about whether the fulfillment request
   exists before or only after approval; the answer is now stated once, here and in
   [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) §01, and both are kept consistent with it.
2. **Sequential per-level approval** — confirmed real, installed, and (on the internal-demand-request concept,
   §04) heavily used historically; on the Supply Commitment concept itself, data shows the "assign an approver"
   half is used far more than the "record the approval" half, leaving genuine doubt whether the full workflow was
   ever completed in practice for that specific document type. TEAM B's independent decision: design the
   **vendor-neutral shape** of a multi-level approval capability (N numbered levels — "numbered" for audit/
   display purposes only, not an enforced-sequence claim, per the CORR-008 wording clarification in
   [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) §03 — each with an assigned approver, an approval or
   rejection event, a timestamp, and a rejection reason) as a first-class Approval Control concept usable by both
   this and the internal-demand-request concept — but explicitly **HOLD** on any claim about its exact trigger
   conditions or transition rules, since the internal button/workflow logic is a Controlled Carry-Forward Unknown
   per Boss Gate §4.1. Full detail in [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md).

These two mechanisms are **not the same concept** and must not be merged into one approval model — TEAM B treats
conflating them as a design error the evidence specifically warns against (`04` §03 synthesis).

## 04 — Internal Demand Capture (Purchase Request equivalent)

A distinct, upstream Commitment fact: an internal actor's stated need, captured *before* any vendor is chosen.
Canonical states: `Draft` → `Pending Approval` → `Approved` / `Rejected`. Conversion to a Supply Commitment is
**hard-gated on `Approved`** — TEAM B adopts this gate without modification (clean, unambiguous, well-evidenced).
The approver-assignment mechanism (derived from the requester's own record) is adopted as a reasonable default,
with the explicit, evidence-flagged caveat that whether requesters can escalate to a different approver is an
open, real-user-validation question (see [12](12_PERSONA_USER_FITNESS_OBSERVATION_MATRIX.md)-equivalent content
folded into [16](16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md) where Thailand-specific, and
[17](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md) generally).

An Internal Demand Request's own state is a **read-model mirror** of whatever Supply Commitment it converts into
— it does not itself drive the commitment's lifecycle after conversion. Independently confirmed as the correct
shape: any design letting a converted, closed demand request continue to influence a live commitment would create
a confusing dual-authority situation.

## 05 — Standing Supply Agreement vs. Multi-Vendor Comparison — Explicit Non-Conflation

**Independent decision, correcting a manifest-vs-reality mismatch found in evidence**: TEAM B's canonical model
draws a hard line between two concepts the reference system's own documentation conflates:

- **Standing Supply Agreement**: a pre-negotiated blanket/template arrangement that confirms terms (price,
  vendor) reusable across many future commitments. Confirming an agreement does **not** itself create a Supply
  Commitment — it updates the Vendor Price Reference and/or provides a template a user explicitly applies to a new
  draft commitment.
- **Multi-Vendor Comparison (Tendering)**: a transient, commitment-level concept — competing draft commitments to
  different vendors for the same need, resolved by a human choosing a winner; losing commitments are cancelled
  (history-preserved), not deleted. This lives entirely on the Supply Commitment concept itself and requires **no**
  Standing Supply Agreement to exist.

TEAM B requires a target design to **name these two concepts distinctly** and never use one term to mean both —
this directly closes Fit-Gap candidate #17 (naming-trap REJECT).

## 06 — Receipt, Dropship, and Vendor Reversal

- **Receipt**: Purchase's demand converts directly and synchronously into a Movement Instruction (unlike Sales'
  indirect, event-driven path — see [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) for why TEAM B does not
  force these two paths into one mechanism).
- **Dropship**: a destination substitution on the same movement-creation step (ship-to-customer instead of
  ship-to-warehouse) — TEAM B adopts this as a routing variant, not a separate capability.
- **Vendor Reversal**: the exact structural mirror of Sales' non-ownership of Reversal (§06 of
  [06](06_SALES_CANONICAL_DESIGN.md)) — Purchase has no owned Reversal feature; Inventory owns it exclusively,
  triggered by a destination-location predicate, with Purchase only netting the effect into Received quantity
  after the fact.

## 07 — Cancellation

Mirrors Sales' rule (§05 of [06](06_SALES_CANONICAL_DESIGN.md)): cancels only not-yet-executed physical
fulfillment, state-partitioned by how much has already been received (nothing received → full cancel; partially
received → the completed portion is always already isolated onto its own operation by the fulfillment-
continuation mechanism, so it is spared while the remainder cancels; fully received → nothing physical touched).

**Independent decision on the evidenced asymmetries**: TEAM B's dispositions for
[13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md]-equivalent asymmetries §04 items:
- **Dual cancellation gate (locked OR an open vendor bill) vs. Sales' single gate (locked only)**: TEAM B judges
  this a **legitimate, preservable business asymmetry** — an outstanding vendor bill represents real financial
  exposure that an outstanding customer invoice on the Sales side does not symmetrically create at cancellation
  time (a Sales cancellation only touches draft invoices, never posted ones, by the same logic). `ADAPT` both
  sides' actual gates as-is; do not force symmetry.
- **Unrestricted return-to-draft (Purchase) vs. restricted (Sales)**: TEAM B finds no functional rationale for
  this difference in evidence and classifies it as an inconsistency, not a business rule — the target design
  should apply **one consistent rule** (return-to-draft permitted only from Cancelled/Sent-equivalent states) to
  both domains, correcting Purchase's unrestricted behavior rather than loosening Sales'.
- **Deletion allowed from Draft OR Cancelled (Sales) vs. Cancelled only (Purchase)**: same disposition — TEAM B
  requires one consistent rule (deletion permitted from Draft or Cancelled) across both domains.

## 08 — Cross-Domain Dependencies Summary

| Dependency | Direction | Mechanism |
|---|---|---|
| Shared Master (Party/Product/Vendor Price Reference/Tax/Payment Term/Currency/Sequence/Company-Branch/Dimension) | Read (+ opportunistic Vendor Price Reference write) | Commitment-time resolution, snapshotted where noted |
| Inventory (Supply Need Signal) | Read (as one of possibly several registered fulfillers) | Reflective/pluggable dispatch, see [05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §07 |
| Inventory (physical receipt demand) | Write (indirect — emits a fulfillment request) | On commitment, direct/synchronous per evidence |
| Inventory (Received quantity, Reversal linkage) | Read | Derived quantities and traceability |
| Financial Handoff | Write | Billable-Now quantity, at each billing event |
| Financial Handoff | Read (backward) | Invoiced quantity |
