> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 7 — Exception / Partial / Cancel / Return / Correction Design

# 12 — EXCEPTION / PARTIAL / CANCEL / RETURN / CORRECTION MODEL

## 00 — Method

First-class treatment per governing prompt §13.6 — every exception path below is a deliberate design decision,
not an afterthought. Each entry states what evidence showed, what TEAM B independently decided, and why.

## 01 — Partial Fulfillment (Delivery / Receipt)

- **Evidence**: header-level progress status is durable; line-level remaining quantity is always live.
- **TEAM B decision**: `ADOPT` unmodified. A stored per-line "remaining" value would be a second, driftable
  source of truth for something fully derivable. Header status remains the one durable partial-progress signal.

## 02 — Over-Fulfillment (Over-Delivery / Over-Receipt)

- **Evidence**: completely unguarded on both sides in the reference system — no detection, no block.
- **TEAM B decision**: `EXTEND` — introduce an explicit, configurable Over-Fulfillment Policy (block / warn-and-
  allow / allow-silently), applied symmetrically to Delivered and Received. TEAM B does not fix a default value;
  this is flagged for Boss/business policy input. Rationale: "no system reaction to a quantity mismatch" is a real
  operational risk (data quality, potential fraud/error masking) regardless of which specific default a business
  ultimately configures — the *existence* of a policy is the design requirement, not any specific setting.

## 03 — Over-Invoicing / Over-Billing

- **Evidence**: no cross-field database constraint anywhere ties Invoiced to Ordered/Delivered/Received on either
  side.
- **TEAM B decision**: same disposition as §02 — an explicit, configurable Over-Billing Policy is required at the
  Billable-Now computation, not left silently unguarded. Symmetric across Sales and Purchase.

## 04 — Backorder (Fulfillment Continuation)

- **Evidence**: not a separate document type — a self-continuation link on the Transfer Operation; policy
  (offer/force/never) lives on the Transfer Operation Type.
- **TEAM B decision**: `ADAPT`, adopted as the Fulfillment Continuation concept in
  [05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §05. Inventing a separate document type was considered and
  rejected — it would add a concept without a corresponding new business need.

## 05 — Customer Return / Vendor Return

- **Evidence**: neither Sales nor Purchase owns a dedicated Return feature; both defer entirely to one Inventory-
  owned, direction-agnostic Reversal mechanism, confirmed by exhaustive negative evidence on both sides.
- **TEAM B decision**: `ADAPT` in full — Reversal is Inventory-owned, full stop, per
  [05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §05. TEAM B additionally flags, as a genuinely open and separate
  question (not resolved here): should SMEsPlus offer a Sales-initiated RMA affordance beyond the current
  warehouse-only entry point? Carried as `HYPOTHESIS / REQUIRES REAL USER VALIDATION` per Boss Gate §4.3 — see
  [17](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md).
- **CORR-008 note (`FV006-DFO-001`)**: a Reversal preserves whatever Traceability Unit / Handling Unit identity
  was recorded on the Movement Execution(s) it reverses — this linkage is never dropped, consistent with
  Reversal's own mandatory traceability-link requirement
  ([03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md) §03) and with the ownership/lifecycle statement now
  recorded in [10](10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md) §01.

## 06 — Cancellation Before Confirmation

- **Evidence**: unrestricted except by Lock, on both sides.
- **TEAM B decision**: `ADOPT` unmodified.

## 07 — Cancellation After Confirmation

- **Evidence**: cascades only to not-yet-executed physical fulfillment; already-executed work is spared, never
  force-reconciled. Sales' cascade evidence is test-confirmed; Purchase's evidence (once opened via corrective
  research) is confirmed structurally equivalent, state-partitioned by receipt scenario.
- **TEAM B decision**: `ADOPT`, made symmetric by design (see [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md)
  §05). **Correction to an evidenced defect**: the reference system's cancellation guard was found to evaluate an
  entire batch of instructions all-or-nothing (one executed instruction anywhere in a batch blocks the whole
  batch's cancellation). TEAM B requires **per-instruction** evaluation instead — a deliberate strengthening, not
  a preserved behavior.
- **Gate asymmetry disposition** (locked-only vs. locked-OR-open-financial-exposure): `ADAPT` both as-is — TEAM B
  judges the Purchase-side dual gate a legitimate business asymmetry (outstanding vendor financial exposure is a
  real blocking condition that a merely-drafted customer invoice does not symmetrically represent), not an
  inconsistency to normalize away.

## 08 — Cancellation After Reservation

- **Evidence**: releases the reservation; a Reversal is required instead of cancellation for anything already
  executed.
- **TEAM B decision**: `ADOPT` unmodified — consistent with the immutable-execution invariant in
  [05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §01.

## 09 — Correction After Partial Physical Movement

- **Evidence**: an executed detail entry cannot be deleted; correcting it re-executes the physical transfer in
  place ("undo and redo"), not a status-flag flip. Neither commercial side blocks a post-partial-movement quantity
  edit outright, except a floor guard against reducing below what's already been fulfilled.
- **TEAM B decision**: `ADOPT` the immutable-execution/re-execute-in-place mechanic as an Inventory-internal
  capability (invisible to Sales/Purchase, which see only the re-derived net quantity). `ADOPT` the floor guard,
  made symmetric across Sales and Purchase (evidence found it Sales-only; TEAM B extends it to Purchase, since no
  functional rationale for the asymmetry was found — see [07](07_PURCHASE_CANONICAL_DESIGN.md) §07).

## 10 — Correction After Complete Physical Movement

- **Evidence**: no "un-execute" action exists anywhere; the only correction path is a Reversal.
- **TEAM B decision**: `ADOPT` as a hard invariant — see [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) §06.
  No business need for an "un-execute" capability was identified anywhere in the evidence, and inventing one would
  undermine the immutable-execution invariant that gives this design its audit integrity.

## 11 — Duplicate / Retry Behavior

- **Evidence**: one concrete, sourced instance — concurrent writers to the same logical Stock Position bin can
  each insert a competing row rather than update one, requiring after-the-fact reconciliation.
- **TEAM B decision**: `REJECT` the after-the-fact-reconciliation pattern as the target approach. TEAM B requires
  the Stock Position bin's uniqueness (per [05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §02) to be an **enforced**
  invariant a target implementation must guarantee at write time (e.g., via a concurrency-safe upsert or
  equivalent), not merely an application convention cleaned up later. This is a deliberate strengthening.
- **CORR-008 closure (`FV006-INT-001`) — general Confirm / Movement Execution idempotency contract.** The
  disposition above was scoped only to the Stock Position bin case; Formal IBPV FV-006 Deliverable 10 found no
  stated contract for the far more common case of a retried Confirm action or a redelivered fulfillment-request
  message (double-click, network retry, at-least-once redelivery per
  [09](09_CANONICAL_BUSINESS_EVENT_CATALOG.md) §00A). TEAM B closes this with one general, vendor-neutral
  business invariant, without prescribing any lock, queue, or framework mechanism:

  > **Idempotency invariant**: every action that transitions a Commitment (`Commercial Commitment Confirmed`,
  > `Supply Commitment Confirmed`, `Supply Commitment Approved`/`Rejected`) or triggers a `Movement Executed`
  > event carries a business identity — the specific commitment being confirmed, or the specific instruction
  > being executed. A repeated invocation carrying the **same** business identity as an action already applied
  > must produce **no additional business effect**: no second Movement Instruction, no second Reservation, and
  > no second Financial Handoff write. The repeat must be observably distinguishable from a genuine new action —
  > it must expose the original action's already-recorded outcome, never silently error and never silently
  > repeat the effect.

  This closes the gap named in `FV006-INT-001` (Critical) for exactly the categories the finding named: a
  retried Confirm and a redelivered fulfillment-request/Movement-Execution trigger. It generalizes, rather than
  replaces, the Stock Position bin strengthening above — that remains the one place this invariant is stated at
  the physical-write level specifically; this paragraph states it at the document/command layer generally.
  Cross-referenced from [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) §11 and
  [09](09_CANONICAL_BUSINESS_EVENT_CATALOG.md) §00A.

## 12 — Cross-Warehouse / Cross-Company Cases

- **Evidence**: both Sales and Purchase apply an identical accessible-branch check on lines; Stock Position scope
  is always derived from Location, never independently set.
- **TEAM B decision**: `ADOPT` unmodified; detailed further in
  [14](14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md).

## 13 — Missing/Late Documents, Late Supply, SLA Breach

- **Evidence**: `NOT OBSERVED` — no detection or grace-period handling found anywhere.
- **TEAM B decision**: `UNKNOWN` — not designed in this session. No evidence exists to reason from, and inventing
  an SLA/lateness mechanism without a stated business need would violate the no-invented-certainty principle.
  Registered as an open item in
  [18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md).
  **This item is unchanged by CORR-008** and must not be confused with §13A below, which is a distinct, now-closed
  question (a technical handoff-write failure, not business lateness).

## 13A — Downstream / Cross-Domain Handoff-Write Failure (CORR-008 closure, `FV006-INT-002`)

- **Distinguished from §13 above**: §13 is about a shipment or document being *late* (a business-timing
  condition); this section is about the *technical* handoff write itself failing or never occurring — e.g.,
  Inventory cannot resolve a routing rule and never creates the Movement Instruction a Commercial or Supply
  Commitment expects, or a "direct, synchronous" receipt-expectation write fails partway. Formal IBPV FV-006
  Deliverable 10 found neither case addressed anywhere in this design.
- **TEAM B decision**: both Hard handoffs named in
  [10](10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md) §02 (Commercial commitment → physical fulfillment
  request; Supply commitment → physical receipt expectation) are now business-observable rather than
  success-path-only:
  - **Owner of the unresolved handoff**: the initiating Commitment (Sales or Purchase) remains the owner of
    record of the handoff obligation until Inventory's confirming event is observed.
  - **Visible status**: a `Handoff Unresolved` status becomes visible on the initiating Commitment once the
    transport-semantics window ([09](09_CANONICAL_BUSINESS_EVENT_CATALOG.md) §00A) elapses without the
    confirming event — this is a new, explicit Control/Financial-handoff-adjacent fact, not a hidden internal
    state.
  - **Retry eligibility**: always eligible — safe by construction, because retry is covered by the idempotency
    invariant in §11 above (`FV006-INT-001`).
  - **Compensation/reconciliation responsibility**: no compensating-reversal mechanism is invented. A
    `Handoff Unresolved` condition means, by definition, that no physical fact was yet created on the receiving
    side — there is nothing to reverse, only something to detect and re-trigger. This deliberately avoids
    inventing an unevidenced compensation mechanism while still closing the completeness gap.
  - **Convergence criterion**: the handoff transitions back to `Handoff Resolved` the moment Inventory's
    confirming event (`Movement Instruction Confirmed`, or the equivalent receipt-expectation acknowledgment) is
    observed.
  - **Audit trail**: `Handoff Unresolved Detected` and `Handoff Resolved` are themselves catalogued, timestamped
    events ([09](09_CANONICAL_BUSINESS_EVENT_CATALOG.md) §03A).
  - **Duplicate-prevention interaction**: re-triggering a stalled handoff is the same action as a normal retry
    and is governed by the same idempotency contract (§11) — no separate duplicate-prevention rule is needed.
- **Residual scope note**: this closure does not extend to Cross-Warehouse/Cross-Company exception effects
  during a handoff failure (a separate, narrower, non-blocking item — `FV006-INT-003` — which remains outside
  CORR-008's nine-finding scope and is unchanged).

## 14 — Approval Rejection

- **Evidence**: a native single-reason rejection exists on the Internal Demand Request; a second, more elaborate
  reject-with-audit-trail mechanism is evidenced as real (paired with the sequential level-based approval control)
  but with unconfirmed internal logic.
- **TEAM B decision**: design the vendor-neutral shape only — a rejection event with an actor, a reason, and a
  timestamp, attachable at any approval level — full detail in
  [13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md). Internal trigger
  logic remains `HOLD / EVIDENCE REQUIRED FOR THIS DECISION POINT`.
- **CORR-008 closure (`FV006-STE-004` / `FV006-EVT-003`)**: this generic shape is now explicitly instantiated for
  the Supply Commitment document type's own `Pending Approval` → `Rejected` transition, including the resulting
  state, the downstream Inventory fulfillment-request stand-down, and the resubmission path — see
  [07](07_PURCHASE_CANONICAL_DESIGN.md) §01 and [09](09_CANONICAL_BUSINESS_EVENT_CATALOG.md) §02 for the full
  closure. This section's generic shape is unchanged; what was missing was its explicit application to the
  Supply Commitment's own state/event model, which is now supplied.

## 15 — Line Deletion After Commitment

- **Evidence**: a confirmed line with existing Financial Handoff activity cannot be deleted, only zeroed —
  symmetric on both sides.
- **TEAM B decision**: `ADOPT` unmodified — a clean, symmetric, audit-preserving pattern.

## 16 — Wrong Item / Wrong Quantity Received or Delivered

- **Evidence**: `NOT OBSERVED` as a distinct workflow — handled, if at all, via the general edit-in-place or
  Reversal mechanisms already catalogued.
- **TEAM B decision**: `NOT MATERIAL TO CURRENT DESIGN` as a separate mechanism — covered by §09/§05 above. No
  additional capability designed.
