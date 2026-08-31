> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 6 — Canonical Business Event Catalog

# 09 — CANONICAL BUSINESS EVENT CATALOG

## 00 — Method

Every event below is business-semantic and vendor-neutral, named for what happened, not for a reference-system
method. An event qualifies for this catalog only if at least one other domain observes or reacts to it (per
governing prompt §13.4) — purely internal recomputation is not catalogued as an event.

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
| Supply Commitment Confirmed | Draft/Sent, product presence on every real line | State → Committed or → Pending Approval, per the amount-threshold gate | Inventory (receipt fulfillment request, direct/synchronous); Shared Master (opportunistic Vendor Price Reference extension) |
| Supply Commitment Approved | Pending Approval, authorized actor | State → Committed | Inventory (unblocks the already-created fulfillment request) |
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
