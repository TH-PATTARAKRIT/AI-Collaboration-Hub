> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 6 — Canonical Business Event Catalog

# 09 — CANONICAL BUSINESS EVENT CATALOG

## 00 — Method

Every event below is business-semantic and vendor-neutral, named for what happened, not for a reference-system
method. An event qualifies for this catalog only if at least one other domain observes or reacts to it (per
governing prompt §13.4) — purely internal recomputation is not catalogued as an event.

## 00A — Event Transport Semantics (CORR-008 closure, `FV006-EVT-002`)

No row below previously stated whether its emission/consumption is synchronous, asynchronous, ordered, or how a
failed consumer should behave — a systemic gap Formal IBPV FV-006 Deliverable 05 found underlying two separate
race-condition findings. TEAM B closes this once, catalog-wide, rather than per event:

- **Synchronous / transactional** — emission and consumption occur within the same commitment action's boundary;
  the emitting action does not complete until the consuming side has accepted or rejected the event. This is the
  classification for every event [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) §01/§10 already
  characterizes as "direct/synchronous" — concretely, `Supply Commitment Confirmed`'s Inventory-facing
  fulfillment-request effect (§02 below).
- **Asynchronous, at-least-once delivery** — emission completes independently of consumption; the consumer may
  process the event after a delay, and the same event may be redelivered. Ordering is guaranteed only within a
  single originating document line's own event sequence (e.g., a given Commercial Commitment line's own events
  are FIFO relative to each other); no ordering guarantee holds *across* different event types or different
  lines. This is the classification for every event characterized elsewhere in this package as
  "indirect/event-driven" — concretely, `Commercial Fulfillment Requested` and every other Sales-originated
  event in §01 below, and every cross-domain notification not explicitly marked synchronous above.
- **Consumer-failure behavior** — a consumer that fails to process a delivered event must not silently drop it:
  redelivery/retry must be safe (governed by the idempotency contract, `FV006-INT-001` —
  [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §11), and if the event remains unprocessed past a
  policy-configured window, the condition must surface as an observable `Handoff Unresolved` status rather than
  fail silently (`FV006-INT-002` — §04A below, cross-referenced from
  [10](10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md) §02).
- **Per-table default**: unless a row in §01–§04 below states otherwise, an event is Asynchronous / at-least-once
  by default; only the rows explicitly named "direct/synchronous" in this package (Supply Commitment's
  Inventory-facing effects) are Synchronous.

This section does not resolve the two named race-condition findings themselves
(`FV006-EVT-004`, `FV006-EVT-005`) — those remain outside CORR-008's nine-finding scope and stay open, tracked
in [18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md). It
closes only the systemic transport-semantics absence that was their stated contributing cause.

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
[12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §13; this table records only the event shape.

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
