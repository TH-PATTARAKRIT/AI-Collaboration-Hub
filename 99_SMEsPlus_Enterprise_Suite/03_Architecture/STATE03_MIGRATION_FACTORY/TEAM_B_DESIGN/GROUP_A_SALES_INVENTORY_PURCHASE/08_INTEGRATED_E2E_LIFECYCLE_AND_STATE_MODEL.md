> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 6 — Integrated Cross-Module E2E Design

# 08 — INTEGRATED E2E LIFECYCLE AND STATE MODEL

## 00 — Independent Framing: No Global State

Per governing prompt §13.3, TEAM B does not assume one global transaction state. Five lifecycles are independent
and correlate only through events, never through a shared state field:

1. **Commercial Lifecycle** (Sales) — [06](06_SALES_CANONICAL_DESIGN.md) §01
2. **Supply Lifecycle** (Purchase) — [07](07_PURCHASE_CANONICAL_DESIGN.md) §01
3. **Internal Demand Lifecycle** (Purchase Request equivalent) — [07](07_PURCHASE_CANONICAL_DESIGN.md) §04
4. **Physical Fulfillment Lifecycle** (Inventory Transfer Operation) — [05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §05
5. **Financial Lifecycle** — out of scope; only its entry point (the Financial Handoff) is modeled here

A Commercial or Supply commitment's own state (Draft/Committed/Cancelled/etc.) **never** implies a specific
Physical Fulfillment state. This is the single most important correction TEAM B makes relative to a naive reading
of the reference system: "confirmed" does not mean "moving," and "moving" does not mean "billed." Each of the
Never-Assume-Equivalence reminders evidence records (`07` §06) is adopted here as a hard modeling rule:

- A committed Sales order does not imply a Movement Instruction exists yet (it implies one has been *requested*).
- A committed Purchase order does not imply stock has arrived.
- A completed Movement Execution does not imply a Financial Handoff has occurred.
- An "approved" Internal Demand Request does not, by itself, prove which control approved it (see
  [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md)).

## 01 — Canonical E2E Scenario 1: Buy → Receive → Stock → Sell → Reserve → Deliver

```
Supply Commitment confirmed
  → emits a Movement Instruction directly/synchronously into the receiving Location, IMMEDIATELY, regardless of
    whether the commitment itself lands in Committed or Pending Approval (CORR-008 closure, FV006-STE-004 /
    FV006-EVT-003 — see [07](07_PURCHASE_CANONICAL_DESIGN.md) §01/§03 for the full rationale)
  → if Pending Approval: the created instruction is held BLOCKED (not-yet-executed, non-actionable) until the
    gate resolves
      → Approved: instruction unblocks, proceeds normally to execution
      → Rejected: instruction is stood down via the SAME not-yet-executed cascade used for Cancellation (§05
        below) — no separate stand-down mechanism, no orphaned fulfillment request
  → [if Committed directly, or once unblocked] Movement Execution recorded → Stock Position increments
  → Purchase's Received quantity re-derives from the now-executed instruction

Commercial Commitment confirmed
  → for physically-fulfilled lines, emits a fulfillment request (NOT a direct write) — Inventory resolves
    the actual Movement Instruction via its own routing rules, independent of how Sales asked
  → Movement Instruction created against the resolved source Location
  → Reservation claims Stock Position (partial claim is a valid outcome)
  → Movement Execution recorded → source decremented, destination incremented
  → Sales' Delivered quantity re-derives from the now-executed instruction
```

**Independent note**: TEAM B deliberately preserves the evidenced asymmetry that Purchase's demand-to-instruction
path is direct/synchronous while Sales' is indirect/event-driven — see §04 below for why this is not normalized.

## 02 — Scenario 2: Sales Demand → Shortage → Supply Need → Purchase → Receipt → Fulfillment

```
Stock Position forecast falls below policy threshold
  → Inventory emits a Supply Need Event (fulfillment-method-agnostic)
  → Purchase (registered as a fulfiller, see 05 §07) resolves the event into a new or reused draft
    Supply Commitment, OR
  → the product's policy instead routes the same signal into an Internal Demand Request (a distinct,
    per-product-configurable fork of the same trigger — not a competing mechanism)
  → either path converges back on Scenario 1's Supply half
```

## 03 — Scenario 3/4 — Partial Fulfillment (Symmetric Across Sales and Purchase)

```
Commitment confirmed, Movement Instruction created for full committed quantity
  → less than the full quantity is executed
  → Fulfillment Continuation splits the unexecuted remainder onto a new Transfer Operation,
    continuation-linked to the original
  → the commercial/supply Received-or-Delivered quantity reflects only the executed portion
  → remaining obligation is tracked independently on each side: the commercial/supply domain re-derives
    "remaining" live from its own quantity fields; it does NOT read the Inventory-side continuation link
    directly (an intentional non-coupling, adopted from evidence as a genuine architectural choice, not a gap)
```

## 04 — Scenario 5/6 — Reversal (Customer or Vendor Direction)

```
Transfer Operation already fully executed (a hard precondition — an in-progress operation cannot be reversed)
  → a Reversal is opened against it FROM Inventory (see 05 §05) — never from the Commercial or Supply
    document directly
  → Reversal swaps source/destination, links back to the specific Movement Execution(s) reversed
  → the originating commercial/supply document's ONLY participation is preserving traceability linkage;
    it never initiates or gates the Reversal
```

## 05 — Scenario 7/8 — Cancellation Before/After Confirmation, and After Reservation

```
Pre-commitment: cancellation is unrestricted except by an explicit Lock.
Post-commitment: cancellation cascades ONLY to not-yet-executed Movement Instructions/Reservations;
  already-executed work is spared, never force-reconciled.
A Reservation on a cancelled not-yet-executed instruction is released back to Available.
An executed Movement Execution can never be cancelled — only reversed (05 §05).
```

**TEAM B's independent correction, carried from [07](07_PURCHASE_CANONICAL_DESIGN.md) §07**: the target design
applies **one consistent return-to-draft rule** and **one consistent deletion-eligibility rule** across Sales and
Purchase — the reference system's asymmetries here are corrected, not preserved, since no functional rationale for
them was found in evidence.

## 06 — Scenario 9/10 — Correction During and After Physical Movement

```
During (not-yet-fully-executed): the physical layer's own "undo and redo in place" mechanic (05 §01) allows a
  still-open execution's detail to be corrected without a full Reversal — this is a physical-layer-only capability,
  invisible to Sales/Purchase, which continue to see only the net re-derived quantity.
After (fully executed): correction is possible ONLY via Reversal (05 §05). There is no "un-execute" action
  anywhere in this canonical design — TEAM B adopts this as a hard invariant, since evidence found it exhaustively
  confirmed absent across every phase of research and no business need for it was identified.
```

## 07 — Scenario 11 — Multi-Warehouse / Company Context

Every fact in this design scopes primarily by Company, with Warehouse as a secondary, often-derived dimension —
detailed in [14](14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md). Company/Branch (a legal hierarchy) is disjoint
from the Thai Tax-Branch concept (a Party attribute) — restated here because it is load-bearing for this scenario,
not merely a Shared Master footnote.

## 08 — Scenario 12 — Financial Handoff (Interface Only)

```
Sales/Purchase compute Billable-Now quantity → write it, verbatim, to the Financial Handoff on each billing event
  → Accounting posts and returns a durable record
  → Sales/Purchase read that record back to re-derive Invoiced quantity (a round-trip, not a one-way push)
Tax determination and fiscal substitution are invoked by Sales/Purchase but resolved entirely inside the
  Financial Handoff's far side — full detail in [15](15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md).
```

## 09 — The Scoped Sales→Purchase Direct Coupling (Subcontract/Dropship)

**Independent decision**: TEAM B does not treat the evidenced narrow exception (a specific product configuration
where a Commercial commitment line directly and automatically creates a draft Supply Commitment, bypassing the
general Supply-Need-Event path) as a violation of the domain boundary rules in
[02](02_CANONICAL_CAPABILITY_AND_DOMAIN_BOUNDARY_MODEL.md). It is modeled as a **distinct, explicitly product-
configuration-gated fulfillment method** — a line whose product is flagged "fulfilled by direct vendor
subcontract/dropship" — rather than a general capability of Sales to create Purchase commitments. This keeps the
general rule (Commercial and Supply communicate only through Inventory's Supply Need Event) intact while still
accounting for the real, evidenced scenario.

## 10 — Why Sales' and Purchase's Physical-Demand Mechanisms Are NOT Normalized to Match

TEAM B explicitly declines to force Sales' indirect/event-driven fulfillment-request mechanism and Purchase's
direct/synchronous one into a single shared mechanism, despite the apparent inconsistency. Reasoning: the two
represent genuinely different business timing needs — a Sales commitment's fulfillment routing may legitimately
depend on real-time inventory-policy decisions (which warehouse, which rule fires) that are Inventory's to make,
whereas a Purchase commitment's receipt is unconditional (whatever is received against a specific PO simply
arrives) and does not require a routing decision. Forcing symmetry here would either strip Sales' fulfillment
routing of meaningful complexity or add unneeded indirection to Purchase's receipt path. This is a considered
`ADAPT` of an architecture pattern (per [05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §07's reflective-dispatch
principle for the Sales side specifically), not an unexamined carry-over.

## 11 — Retry / Idempotency Contract for Confirm and Movement Execution (CORR-008 closure, `FV006-INT-001`)

Full detail and the general vendor-neutral invariant are recorded in
[12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §11; this section states only how it binds into the
E2E chains above. Every state-changing action named in §01–§09 above — `Commercial Commitment Confirmed`,
`Supply Commitment Confirmed`, `Supply Commitment Approved`/`Rejected`, and every `Movement Executed` trigger —
is a **business-identity-idempotent** action: a repeated invocation carrying the same business identity as an
already-applied action (the same commitment confirm, the same specific execution) produces no additional
Movement Instruction, no additional Reservation, and no additional Financial Handoff write. This closes the
double-click/network-retry/message-redelivery risk named in Formal IBPV FV-006 Deliverable 10 without
prescribing any implementation mechanism (no lock, queue, or framework choice is specified here — see
[12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §11 for the full business-invariant statement).

## 12 — Cross-Domain Handoff Failure / Compensation (CORR-008 closure, `FV006-INT-002`)

Full detail is recorded in [10](10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md) §02 (Handoff Resolution
column) and [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §13; this section states only how it
binds into the E2E chains above. Both Hard handoffs in §01 above (Commercial commitment → physical fulfillment
request; Supply commitment → physical receipt expectation) are business-observable, not silently assumed to
always succeed: if the receiving side (Inventory) does not emit its confirming event (`Movement Instruction
Confirmed`) within the transport-semantics window stated in
[09](09_CANONICAL_BUSINESS_EVENT_CATALOG.md) §07, the handoff surfaces as `Handoff Unresolved` on the initiating
Commitment rather than remaining silently pending forever. Resolution is always re-triggerable (safe, because
retry is idempotent per §11 above) and requires no invented compensating-reversal mechanism, since no physical
fact was yet created on the failed side. See
[10](10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md) §02 for the full owner/status/retry/convergence/audit
statement.
