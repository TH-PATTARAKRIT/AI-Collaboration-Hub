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

## 14 — Approval Rejection

- **Evidence**: a native single-reason rejection exists on the Internal Demand Request; a second, more elaborate
  reject-with-audit-trail mechanism is evidenced as real (paired with the sequential level-based approval control)
  but with unconfirmed internal logic.
- **TEAM B decision**: design the vendor-neutral shape only — a rejection event with an actor, a reason, and a
  timestamp, attachable at any approval level — full detail in
  [13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md). Internal trigger
  logic remains `HOLD / EVIDENCE REQUIRED FOR THIS DECISION POINT`.

## 15 — Line Deletion After Commitment

- **Evidence**: a confirmed line with existing Financial Handoff activity cannot be deleted, only zeroed —
  symmetric on both sides.
- **TEAM B decision**: `ADOPT` unmodified — a clean, symmetric, audit-preserving pattern.

## 16 — Wrong Item / Wrong Quantity Received or Delivered

- **Evidence**: `NOT OBSERVED` as a distinct workflow — handled, if at all, via the general edit-in-place or
  Reversal mechanisms already catalogued.
- **TEAM B decision**: `NOT MATERIAL TO CURRENT DESIGN` as a separate mechanism — covered by §09/§05 above. No
  additional capability designed.
