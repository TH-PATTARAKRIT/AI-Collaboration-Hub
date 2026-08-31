> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 6 — Canonical Business Event Catalog

# 09 — CANONICAL BUSINESS EVENT CATALOG

## 00 — Method

Every event below is business-semantic and vendor-neutral, named for what happened, not for a reference-system
method. An event qualifies for this catalog only if at least one other domain observes or reacts to it (per
governing prompt §13.4) — purely internal recomputation is not catalogued as an event.

## 00A — Event Transport Semantics (CORR-008 closure, `FV006-EVT-002`; ordering clause corrected by CORR-010, `FV006-EVT-004`)

No row below previously stated whether its emission/consumption is synchronous, asynchronous, ordered, or how a
failed consumer should behave — a systemic gap Formal IBPV FV-006 Deliverable 05 found underlying two separate
race-condition findings. TEAM B closes this once, catalog-wide, rather than per event:

- **Synchronous / transactional** — emission and consumption occur within the same commitment action's boundary;
  the emitting action does not complete until the consuming side has accepted or rejected the event. This is the
  classification for every event [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) §01/§10 already
  characterizes as "direct/synchronous" — concretely, `Supply Commitment Confirmed`'s Inventory-facing
  fulfillment-request effect (§02 below).
- **Asynchronous, at-least-once delivery** — emission completes independently of consumption; the consumer may
  process the event after a delay, and the same event may be redelivered. This is the classification for every
  event characterized elsewhere in this package as "indirect/event-driven" — concretely, `Commercial Fulfillment
  Requested` and every other Sales-originated event in §01 below, and every cross-domain notification not
  explicitly marked synchronous above.
- **Consumer-failure behavior** — a consumer that fails to process a delivered event must not silently drop it:
  redelivery/retry must be safe (governed by the idempotency contract, `FV006-INT-001` —
  [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §11), and if the event remains unprocessed past a
  policy-configured window, the condition must surface as an observable `Handoff Unresolved` status rather than
  fail silently (`FV006-INT-002` — §03A below, cross-referenced from
  [10](10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md) §02).
- **Per-table default**: unless a row in §01–§04 below states otherwise, an event is Asynchronous / at-least-once
  by default; only the rows explicitly named "direct/synchronous" in this package (Supply Commitment's
  Inventory-facing effects) are Synchronous.

**Ordering and value-currency rule (CORR-010 closure, `FV006-EVT-004`) — replaces the prior ordering clause.**
Formal IBPV RV-009 Deliverable 06 independently found the prior wording self-contradictory: it stated, in the
same breath, that "a given [Commercial Commitment] line's own events are FIFO relative to each other"
(line-scoped, type-agnostic) and that "no ordering guarantee holds *across* different event types or different
lines" (denies exactly that guarantee) — two opposite answers for the one case that matters most: two
different-typed events on the same line, precisely the scenario `FV006-EVT-004` describes. TEAM B replaces both
clauses with one rule that removes the contradiction by making same-line delivery order immaterial to
correctness, instead of asserting an ordering guarantee this transport model cannot enforce without prescribing
infrastructure:

- **No cross-line, no cross-document ordering guarantee** (unchanged): events originating from two different
  document lines, or two different documents, carry no relative-ordering guarantee of any kind.
- **Same-line events, any event type: ordering-independent-by-design.** For any event whose consuming effect
  depends on a value-bearing field of its originating document line (concretely: `Commercial Fulfillment
  Requested`, `Commercial Line Quantity Changed`, and `Supply Commitment Line Quantity Changed`), the event is a
  **trigger to reconcile**, not a **carrier of the value to apply**. On receipt of such an event, the consuming
  domain (Inventory) must read the line's then-current, authoritative field values directly from the originating
  Commitment — never a value captured in the event's own payload at emission time — before computing or updating
  the dependent physical fact (a Movement Instruction's planned quantity, in particular). Consuming the same event
  again, or consuming two same-line events of different types in either order, therefore converges on the
  identical outcome: whatever the line's current authoritative state is at the moment each reconciliation happens.
  This extends, to cross-domain event consumption specifically, the same "never trust a stored/carried value where
  a live, authoritative source exists" principle already adopted for Movement Instruction's actual-so-far quantity
  ([05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §01) and for line-level remaining quantity
  ([06](06_SALES_CANONICAL_DESIGN.md) §03).
  - This directly closes the scenario `FV006-EVT-004` named: confirming a commitment and then immediately editing
    the line's Ordered quantity fires `Commercial Fulfillment Requested` and `Commercial Line Quantity Changed` in
    quick succession; whichever is processed first, the Movement Instruction that results is created/adjusted by
    reading Ordered quantity as it stands at the moment of that processing — never a pre-edit value silently
    retained, because no step in this rule ever applies a payload-carried quantity independent of a fresh read.
  - If a reconciling event is processed before any Movement Instruction yet exists (e.g., `Quantity Changed`
    processed before the `Fulfillment Requested` event that will create the instruction), the reconciliation is a
    no-op with nothing yet to adjust — not a lost update, because the instruction, once created (by the
    possibly-later-processed `Fulfillment Requested` event), is itself created by reading the line's then-current
    quantity, which already reflects the change. No separate replay of the earlier event is required for
    correctness.
  - This rule composes with, and does not replace, the idempotency invariant (`FV006-INT-001` —
    [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §11) and `Handoff Unresolved` detection
    (`FV006-INT-002` — §03A below): if the *first* handoff (the fulfillment/receipt-instruction creation itself)
    never occurs at all, that is total non-delivery, caught by `Handoff Unresolved` — a distinct failure mode from
    mis-ordering, which this rule does not need to, and does not, address.
  - No lock, queue, compare-and-swap, or messaging-technology mechanism is prescribed here — only the business
    rule that value-bearing consumption must be re-derived from current authoritative state, never from an
    event's frozen payload.
- **Registration**: `FV006-EVT-004` is registered and closed in
  [18](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md) §07 (CORR-010). The prior claim in this section that it
  was "tracked in file 18" was independently found false by Formal IBPV RV-009 Deliverable 06 (zero occurrences on
  direct inspection); it is corrected here by actually registering the finding, not by restating the claim.

**`FV006-EVT-005` (Reservation-claim atomicity) is a separate, distinct concurrency concern** — not an
event-transport/ordering question, since it concerns a read-then-write race inside a single Inventory-internal
action rather than delivery order between two events. It is closed in
[05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §04 and registered in
[18](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md) §07 (CORR-010).

## 01 — Events Originating in Commercial Demand (Sales)

| Event | Preconditions | Fact/state change | Consumers |
|---|---|---|---|
| Commercial Commitment Confirmed | Draft/Sent, product presence on every real line | State → Committed | Inventory (fulfillment request for physical lines); (for gated-billing-policy lines, nothing further fires automatically) |
| Commercial Fulfillment Requested | Commitment confirmed, line is physically-fulfilled | Emits a fulfillment request | Inventory (creates a Movement Instruction) |
| Commercial Line Quantity Changed (post-commitment) | Commitment confirmed | Ordered quantity changes | Inventory (adjusts the fulfillment request, subject to the floor guard — see [06](06_SALES_CANONICAL_DESIGN.md) §02) |
| Commercial Commitment Locked | Manual or auto-policy | Locked = true | Sales itself (freezes named fields) |
| Commercial Commitment Cancelled (post-commitment) | Not fully executed elsewhere | Not-yet-executed fulfillment cancelled; executed work spared | Inventory (Reservation release / instruction cancellation) |
| Billable-Now Recomputed | Delivered or Invoiced quantity changes | Billable-Now recomputed | (internal to Sales; feeds the next Billing Event) |
| Billing Event Fired | Billable-Now > 0, user/policy action | Financial Handoff record created | Accounting (posts); Sales (re-derives Invoiced on the round-trip) |
| Subcontract/Dropship Fulfillment Line Confirmed | Commitment confirmed, product flagged for this fulfillment method | A draft Supply Commitment is created/reused | Purchase |

## 02 — Events Originating in Supply Commitment (Purchase)

| Event | Preconditions | Fact/state change | Consumers |
|---|---|---|---|
| Supply Commitment Confirmed | Draft/Sent, product presence on every real line | State → Committed or → Pending Approval, per the amount-threshold gate | Inventory (receipt fulfillment request created directly/synchronously in **both** cases; held `Blocked` if the state lands in Pending Approval — CORR-008 closure, `FV006-STE-004`/`FV006-EVT-003`, see [07](07_PURCHASE_CANONICAL_DESIGN.md) §01/§03); Shared Master (opportunistic Vendor Price Reference extension) |
| Supply Commitment Approved | Pending Approval, authorized actor | State → Committed | Inventory (unblocks the already-created, `Blocked` fulfillment request) |
| Supply Commitment Rejected | Pending Approval, authorized actor denies | State → Rejected | Inventory (stands down the already-created, not-yet-executed fulfillment request via the standard not-yet-executed cascade, [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) §05); Purchase (permanent audit history, actor+reason+timestamp) — **CORR-008 closure, `FV006-EVT-003`, cross-ref `FV006-STE-004`** |
| Supply Commitment Line Quantity Changed (post-commitment) | Commitment confirmed | Ordered quantity changes | Inventory (adjusts the receipt expectation) |
| Supply Commitment Cancelled | Not fully received, or received with the completed portion isolated | Not-yet-received fulfillment cancelled; received portion spared | Inventory |
| Internal Demand Request Approved | Pending Approval | State → Approved | Enables Internal-Demand-to-Supply-Commitment conversion |
| Internal Demand Converted | Approved | A Supply Commitment line is created/reused; an allocation link is written | Supply Commitment; Internal Demand Request's own state becomes a read-model mirror |
| Multi-Vendor Comparison Resolved | ≥2 competing draft commitments exist for the same need | Winner proceeds to confirmation; losers cancelled | Supply Commitment (losers) |
| Supply Need Fulfilled (Purchase's response) | A Supply Need Event was received | A new or reused draft Supply Commitment created | Inventory (eventually, on this commitment's own confirmation) |
| Billable-Now Recomputed / Billing Event Fired | Mirrors §01, AP-side | Financial Handoff record created | Accounting; Purchase (re-derives Invoiced) |

## 03 — Events Originating in Physical Fulfillment (Inventory)

| Event | Preconditions | Fact/state change | Consumers |
|---|---|---|---|
| Movement Instruction Confirmed | Fulfillment request received or internally triggered | Draft → Waiting/Confirmed; for chained demand, may itself emit a further fulfillment request upstream | Chained upstream instruction (replenishment) |
| Stock Reserved | Instruction confirmed, stock available (fully or partially) | Reservation created/updated against Stock Position | Sales/Purchase advisory Available-quantity reads (never a raw reservation read) |
| Movement Executed | Instruction (fully or partially) actioned | Stock Position changes at source and destination; Movement Execution recorded (immutable) | Sales' Delivered / Purchase's Received re-derivation |
| Fulfillment Continuation Created | A Transfer Operation is closed with an unexecuted remainder | New continuation-linked Transfer Operation created | (Inventory-internal; Sales/Purchase do not consume the link directly, per [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) §03) |
| Reversal Executed | Source Transfer Operation fully executed | New opposing Movement Execution recorded, linked to the original | Sales/Purchase (traceability only) |
| Supply Need Raised | Stock Position forecast crosses policy threshold | Supply Need Event emitted | Purchase (or another registered fulfiller) |
| Put-Away Resolved | Receipt-direction instruction executed | Destination sub-location assigned | (Inventory-internal) |

## 03A — Handoff Reconciliation Events (CORR-008 closure, `FV006-INT-002`)

Both Hard handoffs in [10](10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md) §02 (Commercial commitment →
physical fulfillment request; Supply commitment → physical receipt expectation) were previously documented only
for their success path. TEAM B adds the two events below so a failed or stalled handoff is business-observable
rather than silently assumed to never fail — full owner/status/retry/convergence detail is in
[10](10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md) §02 and
[12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §13A (**CORR-010 citation correction** — previously
misread as plain §13, the unrelated, unchanged SLA-lateness section); this table records only the event shape.

| Event | Preconditions | Fact/state change | Consumers |
|---|---|---|---|
| Handoff Unresolved Detected | A Hard handoff's confirming event (`Movement Instruction Confirmed`) has not been observed within the transport-semantics window (§00A) since the initiating commitment reached `Committed` | Initiating Commitment (Sales or Purchase) gains a visible `Handoff Unresolved` status | Sales/Purchase (surfaces to the user); Inventory (informational — the missing routing/creation condition is on its side) |
| Handoff Resolved | The confirming event (`Movement Instruction Confirmed`, or equivalent receipt-expectation acknowledgment) is subsequently observed for a Commitment previously in `Handoff Unresolved` | `Handoff Unresolved` status clears | Sales/Purchase (clears the visible status; no other state change — the underlying Movement Instruction proceeds through its own normal lifecycle) |

Re-triggering a stalled handoff (a retried Confirm or an explicit "retry handoff" action) is always safe to
attempt, since it is covered by the same idempotency contract as every other Confirm/Movement Execution action
(`FV006-INT-001` — [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §11). No compensating-reversal
event is introduced, since a `Handoff Unresolved` condition by definition means no physical fact was yet created
on the receiving side — there is nothing to compensate, only something to detect and re-trigger.

## 04 — Events Originating in the Financial Handoff Boundary (Interface Only)

| Event | Preconditions | Fact/state change | Consumers |
|---|---|---|---|
| Financial Record Posted | A Billing Event was received | Accounting-owned posted record exists | Sales/Purchase (backward Invoiced-quantity re-derivation) |
| Financial Record Reversed/Corrected | Accounting-side correction | Accounting-owned reversal exists | Sales/Purchase (backward re-derivation on next read) |

TEAM B does not further decompose these two — everything past the Financial Handoff boundary is Accounting
Core's own domain, per [15](15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md).

## 05 — Cross-Cutting Dependency Table (Who Reads Whose State)

| Reads | Reader | Access mode | Governing rule |
|---|---|---|---|
| Stock Position / Available / Forecasted views | Sales, Purchase | Read-only, advisory | [02](02_CANONICAL_CAPABILITY_AND_DOMAIN_BOUNDARY_MODEL.md) rule 2 |
| Movement/Instruction state | Sales (Delivered), Purchase (Received) | Read-only | Derived-quantity re-computation only |
| Financial Handoff posted record | Sales, Purchase | Read-only, backward | Round-trip for Invoiced quantity |
| Billing-policy fields (Product master) | Sales, Purchase | Read-only, per-product | Directional (distinct field per domain, [03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md)) |
| Company/Branch accessible-scope | Sales, Purchase | Read-only | [14](14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md) |
| Commercial Commitment line | Purchase (subcontract/dropship fulfillment method only) | Write, scoped | [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) §09 |
| Internal Demand Request state | Supply Commitment (via the conversion wizard-equivalent) | Read-only, hard gate | [07](07_PURCHASE_CANONICAL_DESIGN.md) §04 |
| Transfer Operation Type | Sales, Purchase | Read-only | Classification/default resolution |

## 06 — Confirmed Non-Crossings (Adopted as Hard Boundary Rules, Not Just Observations)

- Sales never reads or writes Stock Position directly — only Product-level derived views.
- Purchase never reads or writes Stock Position directly — same rule.
- Neither Sales nor Purchase references a Fulfillment Continuation link directly.
- Neither Sales nor Purchase owns a Reversal capability of its own.
- Standing Supply Agreement and Commercial Commitment have no direct relationship — any Sales-triggered
  make-to-order path beyond the scoped subcontract/dropship exception (§08 of
  [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md)) is out of this design's evidenced scope.
