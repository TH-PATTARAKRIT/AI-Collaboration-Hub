> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 3 — Inventory Core Canonical Design

# 05 — INVENTORY CORE CANONICAL DESIGN

## 00 — Independent Framing

Inventory is the sole owner of physical fact (domain boundary rule 2 in
[02](02_CANONICAL_CAPABILITY_AND_DOMAIN_BOUNDARY_MODEL.md)). Everything in this file answers: what must be true
physically, how is it recorded, and what may Sales/Purchase do with it (read only, never write).

## 01 — Movement Instruction and Movement Execution (the Planned/Actual Split)

**Independent decision**: TEAM B adopts the planned-instruction/actual-execution split as a canonical pattern,
generalized (not copied) from evidence — because the underlying business need is real and evidenced repeatedly:
demand and actual outcome are allowed to diverge (partial fulfillment, over-execution against a plan, multi-step
detail against one plan), and the split is what makes backorder/exception handling possible without losing the
original plan's identity.

- **Movement Instruction** (Commitment fact): what is planned to move — product, planned quantity, source,
  destination, and the document it is planned to fulfill. Mutable until execution begins.
- **Movement Execution** (Physical fact): what actually moved — may be recorded in multiple execution entries
  against one instruction (e.g., different lots, different exact sub-locations). **Immutable once recorded** —
  correctable only by a new, opposing execution (Reversal/Return, §05), never by editing.
- A Movement Instruction's "actual so far" quantity has **state-dependent meaning**, not fixed meaning: while the
  instruction is open, it means "reserved/claimed so far"; once the instruction is closed, the same aggregate
  means "what was actually moved." TEAM B adopts this explicitly as a documented state-dependent semantic, not an
  implicit one — a target implementation must make the distinction visible (e.g., via the instruction's own state)
  rather than relying on callers to infer meaning from context, which is the exact ambiguity evidence flags as a
  risk for any code reading the field without checking state first.
- A Movement Instruction may be **chained** to another (its destination feeds another instruction's source) —
  this is required to represent multi-step internal routing and demand-triggered replenishment chains.

## 02 — Stock Position (On-Hand Ledger)

- One ledger row per (Product, Location, [Traceability Unit], [Handling Unit], [Ownership context]) — a **bin**,
  not a transaction log. TEAM B requires this to be genuinely unique per that key combination as an enforced
  invariant, not merely an application convention reconciled after the fact — evidence shows the reference system
  leaves this to eventual-consistency cleanup, which TEAM B classifies as a defect worth correcting, not a pattern
  to preserve (see [17](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md)).
- Company/Warehouse scope is always *derived* from the ledger row's Location, never independently settable — TEAM
  B adopts this to prevent the exact "same product reports different on-hand numbers depending on caller's
  company context" ambiguity evidence describes; the resolution is that the derivation rule itself (which
  companies' warehouses are "in scope" for a given query) must be an explicit, documented default, not implicit.
- **Negative stock**: TEAM B requires an explicit, configurable policy (block / warn-and-allow / allow) rather
  than the reference system's silent allow-via-bypass-path. This is a deliberate strengthening, not a preservation
  of the observed behavior — see [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md).

## 03 — The Six Canonical Quantity Views

Full register in [11](11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md). Summary: On-Hand, Reserved, Available
(On-Hand − Reserved), Incoming (not-yet-executed instructions moving into scope), Outgoing (not-yet-executed
instructions moving out of scope), Forecasted (On-Hand + Incoming − Outgoing, legitimately negative). TEAM B
adopts all six as first-class, independently-named views — not because the reference system does, but because
each answers a genuinely distinct business question that both Sales and Purchase need to ask.

## 04 — Reservation

- A Reservation is a Commitment fact: a claim against Available stock made on behalf of a Movement Instruction,
  releasable without penalty until the instruction executes. Partial reservation (less than requested) is a valid
  outcome, not an error — the instruction's state must reflect "partially claimed" as a distinct condition from
  "fully claimed" or "nothing claimed yet."
- **Reservation is never directly visible to Sales or Purchase as a raw claim total** — both domains read only the
  *derived* Available/Forecasted views (§03), consistent with the domain-boundary rule that Inventory owns
  physical fact exclusively. TEAM B treats a future design exposing raw reservation totals to Sales/Purchase as a
  boundary violation, not a convenience.

## 05 — Transfer Operation, Fulfillment Continuation, and Reversal

- **Transfer Operation**: the operational document a warehouse worker executes — one Receipt, Delivery, or
  Internal Transfer, wrapping one or more Movement Instructions. Its state is **entirely derived** from
  constituent instruction states; it carries no independent state machine. A Transfer Operation Type (Receipt /
  Delivery / Internal) drives default source/destination and the fulfillment-continuation policy (§below).
- **Fulfillment Continuation (Backorder)**: TEAM B independently decides to keep this as a *link on the same
  Transfer Operation concept* (self-continuation) rather than inventing a separate document type — the underlying
  business need (unfinished lines split off, original document's identity preserved) is well served by a
  continuation link, and inventing a new document type would add a concept without a corresponding new business
  need. The **policy** for whether a continuation is offered, forced, or never created must be configurable per
  Transfer Operation Type (evidenced pattern, adopted).
- **Reversal (Return)**: only a **fully executed** Transfer Operation may be the source of a Reversal. A Reversal
  swaps source/destination relative to the original and carries a **mandatory, application-visible traceability
  link** back to the specific Movement Execution(s) it reverses — TEAM B elevates this from a database-level FK
  (as evidenced) to a first-class, queryable fact, per the traceability requirement in
  [03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md) §06.
- **Independent design decision — Reversal is Inventory-owned regardless of commercial origin.** Evidence for this
  is the single most exhaustively-confirmed finding in the whole Team A package (both a customer-initiated and a
  vendor-directed reversal are structurally identical, negative-confirmed on both commercial sides). TEAM B
  adopts "Reversal belongs to Inventory, full stop" as a hard rule. Whether Sales/Purchase should additionally
  offer a commercial-side *initiation* affordance (a button that opens a Reversal against a specific delivery/
  receipt) is a separate, genuinely open UX/process question — see
  [17](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md) Decision on Fit-Gap candidate #15, carried as
  `HYPOTHESIS / REQUIRES REAL USER VALIDATION` per Boss Gate §4.3.

## 06 — Traceability Unit (Lot/Serial) and Handling Unit (Package)

- **Traceability Unit**: exists only for products flagged trackable (a Product-master policy, not an Inventory
  decision made per-transaction). On-hand quantity for a given unit is always a derived view over contributing
  Movement Executions, never independently stored — avoids a second, driftable source of truth.
- **Handling Unit**: as established in
  [03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md) §03, TEAM B treats *current* handling-unit membership
  and the *historical snapshot* taken at Transfer Operation completion as two distinct fact instances. This is a
  deliberate elevation of an evidenced pattern into an explicit design requirement: a naive "just keep one live
  table" implementation would silently lose what a completed shipment actually contained if the live package
  record is later reused or emptied.

## 07 — Supply Need Signaling and Put-Away

- **Supply Need Signal**: a continuously-derived fact ("forecast has fallen below policy minimum for this
  product/location") that, when it fires, emits an abstract **Supply Need Event** — Inventory does not itself
  know or care who fulfills it.
- **Independent architecture decision, elevated to a target-design principle**: TEAM B adopts the reflective/
  pluggable dispatch pattern evidence found between core Inventory and Purchase (`stock` has zero compile-time
  knowledge of `purchase_stock`; the fulfiller registers itself into a generic dispatch contract) as a **worth-
  preserving architecture pattern**, independent of any specific technology. The generic shape: Inventory defines
  and emits the Supply Need Event; zero, one, or more fulfillment providers (Purchase being the only one in this
  domain's scope; a future Manufacturing domain would be another) may register to handle a given fulfillment
  method. This keeps Inventory's core free of a hard dependency on Purchase — TEAM B classifies this as the single
  cleanest module-boundary pattern found anywhere in the evidence and an explicit `ADAPT` (as a pattern, not a
  literal mechanism) — see [17](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md).
- **Put-Away**: resolves the exact destination sub-location for arriving stock, by specificity-ordered policy
  (handling-unit-type > product > exact-category > any-category). Purely Inventory-internal; never referenced by
  Sales or Purchase.

## 08 — Exception/Partial/Correction Semantics (Inventory-Layer Summary)

Full model in [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md). Inventory-owned invariants TEAM B
carries forward as hard rules:

1. A Movement Execution, once recorded, can never be deleted or silently edited — only reversed.
2. A Movement Instruction that has already executed cannot be cancelled; cancellation applies only to the
   not-yet-executed remainder.
3. A cancellation affecting a batch of Movement Instructions must evaluate each instruction independently for its
   own execution state — TEAM B explicitly requires **per-instruction** evaluation, correcting an evidenced defect
   where the reference system's guard was found to apply all-or-nothing across an entire batch (a single executed
   instruction anywhere in a batch blocked cancellation of the whole batch). This is a deliberate strengthening.
4. Only a fully-executed Transfer Operation may be the source of a Reversal.

## 09 — What Inventory Never Does

Per domain boundary rule 2: Inventory never reads Sales' or Purchase's commercial fields to make a physical
decision (e.g., it does not gate reservation on credit status or approval state — those are Commercial/Supply
Commitment concerns). Inventory never posts to Accounting directly — it only produces the physical facts that
Sales/Purchase read to compute their own billable-quantity handoff (see
[15](15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md)).
