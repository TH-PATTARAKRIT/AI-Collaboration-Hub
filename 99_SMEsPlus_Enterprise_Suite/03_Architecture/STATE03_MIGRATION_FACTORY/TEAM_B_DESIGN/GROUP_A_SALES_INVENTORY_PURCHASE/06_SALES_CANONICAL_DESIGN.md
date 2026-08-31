> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 4 — Sales Canonical Design

# 06 — SALES CANONICAL DESIGN

## 01 — Commercial Lifecycle

**Independent decision**: one Sales Order concept spans quotation and committed order, distinguished by state —
TEAM B adopts this (evidence: `03` §02 SO-01) because splitting quotation and order into separate document types
would require re-establishing identity/traceability at the moment of commitment, solving a problem that state
alone already solves cleanly.

Canonical states: `Draft` → (`Sent`, optional, an engagement-tracking signal only — TEAM B confirms it carries no
behavioral difference from Draft and should not be over-engineered into a gate) → `Committed` → `Cancelled`, with
`Draft` reachable again from `Committed`-derived `Cancelled` or from `Sent`. `Committed` orders may additionally be
`Locked` — an **independent boolean**, not a lifecycle state, since evidence proves it is orthogonal (a
just-committed order defaults to unlocked; locking and unlocking do not themselves change lifecycle state).

**Confirmation gate — an independent design decision, not an inherited default**: evidence shows the reference
system's confirmation gate is minimal (state + product presence only), with credit exposure shown as an advisory
banner that never blocks. TEAM B does **not** treat "advisory-only, never blocking" as the correct target
behavior by default — it is one legitimate configuration among several a real business might need. TEAM B's
canonical requirement: confirmation gating (credit exposure, inventory availability, or neither) must be an
**explicit, configurable business policy**, not hardcoded to any one behavior. This is recorded as a genuine open
design decision requiring Boss/business validation before a default is fixed — see
[13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) and
[17](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md) (Fit-Gap candidate #14).

**Locking, precisely**: TEAM B requires Locking to freeze a named, explicit set of commercial fields (not a
blanket write-block) — adopted from evidence as a workable, low-friction pattern. The exact field set is an
implementation decision outside this design's scope, but the *mechanism shape* (named-field freeze, independent
of lifecycle state, explicitly reversible) is adopted.

## 02 — Order Line and the Quantity Quadruple

Canonical quantities: **Ordered** (commitment, plain input), **Delivered** (derived, dispatched by fulfillment
method — see [11](11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md)), **Invoiced** (derived, backward from
Financial Handoff), **Billable-Now** (derived, the one quantity that branches on billing policy: order-based vs.
delivery-based). Full register in [11](11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md).

**Independent decision — Ordered quantity editability after commitment**: evidence shows the reference system logs
but never blocks a post-commitment quantity edit (except a floor guard once fulfillment has begun). TEAM B adopts
the floor guard (never allow a commitment to be reduced below what has already been fulfilled — redirect to a
Reversal instead) as a hard rule, and treats "should any other post-commitment edit be blocked, warned, or freely
allowed" as a business-policy decision, not a hardcoded default — same posture as the confirmation gate above.

**Invoiced quantity — deliberate single-source requirement**: evidence shows two non-interchangeable variants
(any-non-cancelled vs. posted-only) coexisting with no single canonical answer. TEAM B requires a target design to
pick **one** as "the" Invoiced quantity for line-status purposes, while still allowing the other to exist as a
distinct, separately-named reporting view if a real need is confirmed. This is a decision this design package
flags for Boss/business input rather than resolves unilaterally, since it depends on AR policy the evidence
package does not settle.

## 03 — Sales Fulfillment Tracking

Delivered quantity is entirely Inventory-derived once physical fulfillment applies (see
[05](05_INVENTORY_CORE_CANONICAL_DESIGN.md)); for non-physical lines (services), it is a manually-maintained
derived value with no Inventory involvement. TEAM B requires this dispatch to be an explicit, named policy on the
line (not an implicit fallback), so "why is this line's delivered quantity computed this way" is always
answerable without inspecting code.

**Header delivery-progress status is durable; line-level remaining quantity is always a live computation, never
stored** — TEAM B adopts this pattern deliberately (evidence: `03` §07 synthesis). Storing a per-line "remaining"
value would create a second, driftable source of truth for something fully derivable from Ordered − Delivered.

## 04 — Sales Billing Eligibility (Financial Handoff Origination)

Billable-Now quantity is computed from Ordered/Delivered/Invoiced plus the line's billing policy (order-based vs.
delivery-based) and is the value written, verbatim, to the Financial Handoff when a billing event fires. This is
the **entire mechanism** distinguishing bill-on-commitment businesses from bill-on-fulfillment businesses — TEAM B
confirms no other fork is needed and none should be invented.

## 05 — Cancellation

- Pre-commitment: unrestricted except by Locking (which should not normally apply pre-commitment).
- Post-commitment: cancels only the **not-yet-executed** portion of any associated physical fulfillment; already-
  executed fulfillment is explicitly spared, never reconciled or force-matched against the cancellation. TEAM B
  adopts this as a hard rule — a cancelled commercial commitment coexisting indefinitely with completed physical
  fulfillment is an accepted, correct state, not a defect to "fix" by inventing an automatic reconciliation step
  (none is evidenced as needed, and inventing one would add unrequested complexity).
- Re-committing a previously-cancelled-then-drafted order **always produces new physical fulfillment demand**,
  never revives or reuses the cancelled instructions — adopted as a target-parity decision point, test-confirmed
  in evidence.

## 06 — Return / Reversal — No Sales-Owned Return Feature

**Independent decision, closing a governance-flagged open question**: Sales does **not** own a Return capability.
Evidence for this is exhaustively confirmed (full-file-grep negative, both structural mechanism and its absence
independently verified). TEAM B's canonical design gives Sales exactly one participation in a Reversal: (a) a
guard preventing an ordered-quantity reduction below already-delivered quantity, redirecting the user toward
Inventory's Reversal capability, and (b) preserved traceability linkage so a Reversal against this order's
fulfillment remains queryable from the order. **Whether SMEsPlus should additionally offer a Sales-initiated RMA
affordance is an open, evidence-flagged business question**, not resolved here — see
[17](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md), Decision on Fit-Gap candidate #15.

## 07 — Approval

A real, historically-used, sequential per-level approval control exists on Sales commitments in the evidence
(confirmed installed and used, though internal workflow logic is a Controlled Carry-Forward Unknown). TEAM B
designs the vendor-neutral shape only — see [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) — and does not
invent the missing internal logic.

## 08 — Cross-Domain Dependencies Summary

| Dependency | Direction | Mechanism |
|---|---|---|
| Shared Master (Party/Product/Price Rule/Tax/Payment Term/Currency/Sequence/Company-Branch/Dimension) | Read | Commitment-time resolution, snapshotted where noted in [04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md) |
| Inventory (physical fulfillment demand) | Write (indirect — emits a fulfillment request, does not write physical state) | On commitment, for physically-fulfilled lines only |
| Inventory (Delivered quantity, Reversal linkage) | Read | Derived quantities and traceability |
| Financial Handoff | Write | Billable-Now quantity, at each billing event |
| Financial Handoff | Read (backward) | Invoiced quantity |

## 09 — Stock-vs-Service Behavior

**Independent decision**: whether a line participates in physical fulfillment is derived from the Product's
type (§02 of [04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md)), evaluated through **one centralized gate**, not
scattered checks. Evidence shows the reference system repeats this check independently 5-7 times across files —
TEAM B treats this as an implementation defect (a maintenance/consistency risk, since each occurrence could in
principle drift) and requires a target design to centralize the gate. This is a deliberate strengthening over the
observed pattern, not a preservation of it.
