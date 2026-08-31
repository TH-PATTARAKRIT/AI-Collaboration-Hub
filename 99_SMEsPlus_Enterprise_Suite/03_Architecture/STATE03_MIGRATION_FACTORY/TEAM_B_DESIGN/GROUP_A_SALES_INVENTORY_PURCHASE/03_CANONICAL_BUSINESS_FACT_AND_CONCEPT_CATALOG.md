> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 2 — Canonical Business Facts / Concepts

# 03 — CANONICAL BUSINESS FACT AND CONCEPT CATALOG

## 00 — Method and Fact-Type Taxonomy

Every business fact below is classified into exactly one of four types, per governing prompt §13.1:

- **Commitment fact** — a promise or authorization that something will happen (e.g., an order line's quantity).
  Mutable until the commitment is executed against; the commitment itself, once made, is history-preserving.
- **Physical fact** — a statement about the real world (stock on hand, a completed movement). Immutable once the
  underlying event has occurred; correctable only by a new, opposing physical fact (a Return), never by editing
  history.
- **Derived fact** — computed from other facts, never independently authored (e.g., delivered quantity, forecast
  availability). Recomputation on dependency change is expected; the fact itself carries no independent identity.
- **Control/Financial-handoff fact** — a fact whose purpose is to gate a downstream domain (approval status) or to
  hand a value to Accounting (billable quantity). Treated as history-preserving once acted upon.

## 01 — Shared Master Concepts

| Concept | Type | Immutable-after-occurrence? | Identity note |
|---|---|---|---|
| Party | Reference (not commitment/physical/derived) | N/A — a master identity, not an event | One actor concept for every external/internal role (customer, vendor, contact); role is usage-context, not a separate identity |
| Product/Service | Reference | N/A | One concept for goods/service/bundle; "stockable" is a derived property of type, not a separate model |
| Product Classification | Reference | N/A | Hierarchical; carries inventory-policy defaults as well as reporting grouping — two distinct jobs on one concept, kept distinct in this catalog (see §05) |
| Unit of Measure | Reference | Conversion ratio becomes immutable once any commitment or physical fact has referenced it (an evidenced invariant worth preserving, `13` §01 item 7) | Self-referential conversion family, not a separate category model |
| Sales Price Rule | Reference (Sales-only) | N/A | Rule-tree, not a literal list; resolves to a price at commitment time |
| Vendor Price Reference | Reference (Purchase-only) | N/A | Distinct concept from Sales Price Rule — not a symmetric pair, see [04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md) |
| Tax Rule | Reference (interface) | N/A | Direction-scoped (applies-to-sales vs. applies-to-purchase); substitution logic is an Accounting-interface Unknown |
| Payment Term | Reference | N/A | Installment schedule template; becomes historically bound to a specific commitment once applied |
| Currency / Exchange Rate | Reference / Physical (rate is a dated fact) | Rate, once used by a commitment, should be treated as historically frozen on that commitment (snapshot pattern, evidenced) | |
| Document Sequence | Control | N/A — a numbering service, not a business fact itself | |
| Warehouse / Stock Location | Reference | Warehouse's owning company is immutable after creation (evidenced invariant) | |
| Company / Branch | Reference | Hierarchy position immutable after creation (evidenced invariant); currency must match root (evidenced invariant) | |
| Cost Dimension (Analytic) | Reference | N/A | Definitions shareable; usage on a posted line is always company-attributed |

**CORR-008 addition (`FV006-DFO-005`)**: every concept in the table above, once referenced by at least one
historical Commitment, Physical, or Control/Financial-Handoff fact, is also subject to the general
Archival/Non-Deletion rule now stated in
[04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md) §08 — hard deletion is prohibited once referenced; the
concept is archived/retired instead. This generalizes what was previously stated only for UOM's conversion ratio
and Warehouse's owning-company assignment (both still individually noted above) to every row in this table.

## 02 — Commercial Demand (Sales) Facts

| Fact | Type | Immutable-after-occurrence? |
|---|---|---|
| Quotation exists | Commitment (pre-binding) | No — freely editable pre-commitment |
| Sale is committed | Commitment | The commitment event itself (state + timestamp) is permanent history; the order's mutable fields are not automatically frozen by commitment alone — freezing is a separate, explicit control (see below) |
| Commercial terms are locked | Control | Once set, blocks a named subset of line fields; itself reversible by explicit unlock |
| Ordered quantity | Commitment | Editable after commitment (evidenced: not blocked, only logged); a target design must decide deliberately whether this remains editable — see [11](11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md) |
| Delivered quantity | Derived | Derived from Physical facts (Inventory); never independently authored by Sales |
| Invoiced quantity | Derived (backward, from Financial Handoff) | Derived from Accounting's posted records; two variants must be deliberately chosen between (any-non-cancelled vs. posted-only) |
| Billable-now quantity | Control/Financial-handoff | Recomputed live from Ordered/Delivered/Invoiced + billing policy; the *value written to Accounting* at the moment of handoff is history-preserving |
| Delivery progress status | Derived | Header-level only; not a commitment on its own |

## 03 — Physical Fulfillment (Inventory) Facts

| Fact | Type | Immutable-after-occurrence? |
|---|---|---|
| Movement instruction (planned) | Commitment | Mutable pre-execution (quantity/route may change); becomes physical fact on execution |
| Movement execution (actual) | Physical | **Yes — immutable once executed.** Correctable only via a new opposing movement (Return), never by editing. This is TEAM B's strongest inherited invariant — evidenced as an ORM-enforced rule with no exception found anywhere in the source system. |
| Stock position (on-hand) | Physical | Each individual contributing movement is immutable; the aggregate position is a live derived view over all contributing movements |
| Reservation (claim on stock) | Commitment | Exists only pre-execution; released on cancellation or converted to a physical decrement on execution |
| Transfer operation (grouping document) | Commitment→Physical (state-derived) | State is entirely derived from constituent movement-instruction states, never authored independently |
| Fulfillment continuation (backorder) | Commitment | A new commitment carrying forward unexecuted quantity; the original transfer's completed portion remains immutable |
| Reversal (return) | Physical | Immutable once executed, same as any other movement execution; carries a mandatory traceability link to the movement it reverses |
| Traceability unit (lot/serial) | Reference/Physical hybrid | Existence is a reference fact; its location/quantity is always derived from contributing physical movements, never stored independently. **Owner, changing event, and lifecycle-end are recorded in [10](10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md) §01 (CORR-008 closure, `FV006-DFO-001`) — this catalog states its fact-type only.** |
| Handling unit (package) | Physical, with a live/historical split | **A first-class design decision, not a footnote**: the *current* handling-unit membership is a live, mutable fact; a *historical snapshot* is taken and frozen at the moment a transfer operation completes. TEAM B treats these as two distinct fact instances, not one fact with a "done" flag — collapsing them loses real information (evidenced: `02` §08 synthesis). **Owner, changing event, and lifecycle-end are recorded in [10](10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md) §01 (CORR-008 closure, `FV006-DFO-001`) — this catalog states its fact-type only.** |
| Supply need signal | Derived | Recomputed continuously from stock position vs. policy thresholds; not itself a persisted commitment |

## 04 — Supply Commitment (Purchase) Facts

| Fact | Type | Immutable-after-occurrence? |
|---|---|---|
| Internal demand request exists | Commitment (pre-approval) | No |
| Demand request is approved | Control | Yes, once acted upon — gates conversion to a supply commitment |
| RFQ exists | Commitment (pre-binding) | No |
| Supply is committed | Commitment | Same permanence pattern as Sales' "Sale is committed" |
| Supply commitment requires approval | Control | See [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) — two independently real mechanisms coexist in evidence and must both be modeled |
| Ordered quantity (supply) | Commitment | Same pattern as Sales' ordered quantity |
| Received quantity | Derived | Derived from Physical facts, same pattern as Delivered quantity |
| Invoiced/billable-now quantity | Derived / Control-Financial-handoff | Mirrors Sales' pattern, policy-gated by a distinct field (see [11](11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md)) |
| Standing agreement (blanket/template) | Reference/Commitment hybrid | Confirms vendor pricing terms; does not itself commit a specific delivery — a real, evidenced distinction from a live commitment |
| Multi-vendor comparison (tender) | Commitment (transient, pre-decision) | Resolved (winner/loser) at confirmation; losers are cancelled, not deleted — history-preserving |

## 05 — Cross-Cutting Notes (TEAM B independent reasoning, not restating evidence)

- **Product Classification does two structurally different jobs and TEAM B keeps them conceptually distinct even
  though the reference system fuses them on one record**: (a) *taxonomy* (reporting/grouping) and (b)
  *inventory-policy template* (removal strategy, routing, put-away defaults). A target design may still implement
  both on one underlying table for simplicity, but the **business concepts are catalogued separately here** so a
  future schema decision is made deliberately, not by inheriting the reference system's fusion unexamined.
- **Sales Price Rule and Vendor Price Reference are catalogued as two separate concepts, not a symmetric pair.**
  Evidence is unambiguous that Purchase has no rule-engine equivalent to Sales pricing (`01` §06 PRC-22). TEAM B
  independently confirms this should **not** be normalized away in a target design — the business reality (list
  pricing to many customers vs. negotiated/historical pricing with individual vendors) is asymmetric, and forcing
  a common "Pricelist" abstraction over both would misrepresent the Purchase side's actual need (a price
  *reference/history*, not a *rule engine*).
- **The six Inventory quantity concepts (On-Hand, Reserved, Available, Incoming, Outgoing, Forecasted) are
  canonical facts in their own right, not restatements of the commercial quadruple.** Full register in
  [11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md](11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md).
- **"Returned" and "Backordered" quantities are explicitly NOT catalogued as independent facts** at the
  commercial-line level, following strong evidence (both are netting effects folded into Delivered/Received,
  never stored as their own signed quantity at that layer — `09` §04). They *are* first-class physical facts at
  the Movement/Transfer layer (§03 above). TEAM B treats this as a genuine layering decision: the commercial line
  answers "how much, net" — the physical layer answers "what exactly happened, including reversals."

## 06 — Identity and Traceability Requirements

Every Commitment fact and every Physical fact must carry (a) a durable reference identity independent of internal
row identity, and (b) an explicit traceability link to (i) the master identities it references (Party, Product,
Warehouse/Company) and (ii) any fact it was derived from or reverses. This is not optional: evidence shows the
reference system's traceability breaks down exactly where such a link is missing or FK-only-at-the-database-level
(e.g., the PO-line↔SO-line FK that no application code surfaced — `08` §02) — TEAM B treats "traceability must be
a first-class, application-visible fact, not merely a database FK" as an independent design requirement.
