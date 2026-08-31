> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 6 (§13.5) — Quantity / Commitment / Fulfillment Semantics

# 11 — QUANTITY, COMMITMENT AND FULFILLMENT SEMANTICS

## 00 — Method

Per governing prompt §13.5, TEAM B does not collapse quantity concepts merely because a reference implementation
stores or computes several together. Each concept below is independently named and given a proof, not merely a
label.

## 01 — Inventory (Physical) Quantities — Canonical Six

| Concept | Definition | Stored or derived | Never conflate with |
|---|---|---|---|
| On-Hand | Physically present, raw sum across contributing bins, no reservation adjustment | Stored per bin; derived at aggregate | Available |
| Reserved | Portion of On-Hand already claimed by a not-yet-executed Movement Instruction | Stored, at the bin/claim level | On-Hand |
| Available | On-Hand − Reserved — the number safe to claim as a **new** reservation | Derived | On-Hand, Forecasted |
| Incoming | Sum of not-yet-executed instructions moving into scope | Derived, excludes executed instructions | Received/Delivered |
| Outgoing | Sum of not-yet-executed instructions moving out of scope | Derived, excludes executed instructions | Received/Delivered |
| Forecasted | On-Hand + Incoming − Outgoing | Derived; **may legitimately be negative** (a valid trigger condition for Supply Need, not an error state) | On-Hand (only On-Hand's negativity is an oversell condition requiring policy attention) |

## 02 — Commercial (Sales) Quantities

| Concept | Definition | Stored/derived | Branches on |
|---|---|---|---|
| Ordered | Plain committed-quantity input | Stored | — |
| Delivered | Fulfillment-method-dispatched: expense-driven, manually-maintained (services), or Movement-Execution-summed (physically-fulfilled) | Stored compute, per-line dispatch | The line's fulfillment method |
| Invoiced | Backward-derived from the Financial Handoff's posted records | Stored compute | Whether cancelled/reversed postings are included (a deliberate single-source decision required — §04) |
| Billable-Now | The only Sales quantity that branches on billing policy | Stored compute | `order-based` → Ordered − Invoiced; `fulfillment-based` → Delivered − Invoiced |
| Remaining-to-Deliver | Ordered − Delivered | **Always a live computation, never stored** | — |

## 03 — Supply (Purchase) Quantities

| Concept | Definition | Stored/derived | Branches on |
|---|---|---|---|
| Requested | The pre-commitment internal-demand quantity — a genuinely different concept from Ordered, existing only if an Internal Demand Request was used | Stored, on the Internal Demand Request | — |
| Ordered | Plain committed-quantity input on the Supply Commitment line | Stored | — |
| Received | Fulfillment-method-dispatched, mirrors Delivered's shape (manual vs. Movement-Execution-summed, with explicit reversal/dropship netting) | Stored compute, per-line dispatch | The line's fulfillment method |
| Invoiced | Backward-derived, mirrors Sales | Stored compute | Same single-source decision as Sales, §04 |
| Billable-Now | Mirrors Sales' shape, distinct policy field | Stored compute | `commitment-based` → Ordered − Invoiced; `fulfillment-based` → Received − Invoiced |
| Remaining-to-Receive | Ordered − Received | Always live, implicit via not-yet-executed instructions | — |

## 04 — Cross-Family Reconciliation (Independent TEAM B Decisions)

- **Delivered and Received are the same underlying mechanism from opposite directions.** TEAM B adopts one shared
  "Fulfillment Quantity Dispatch" pattern for both — a per-line, stored, computed method-selector, defaulting to
  manual for non-physical lines and switching to Movement-Execution-summed once the line is physically fulfilled.
  This symmetry is preserved deliberately as a canonical design pattern.
- **Billable-Now's billing-policy field is deliberately kept as two independently-configurable fields (one for
  Sales, one for Purchase), not unified into one shared policy concept.** AR and AP billing bases can legitimately
  diverge per business — forcing one shared field would remove a real degree of freedom the evidence shows the
  reference system correctly preserves (see [03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md) §05).
- **Invoiced quantity — the single-source decision TEAM B flags as requiring Boss/business input, not resolved
  unilaterally here**: a target design must pick exactly one canonical definition (any-non-cancelled postings vs.
  posted-only postings) for line-status purposes on **both** Sales and Purchase, consistently. TEAM B's
  recommendation, stated as a recommendation and not a ruling: use posted-only as the canonical "Invoiced" value
  (it more accurately answers "what has Accounting actually finalized"), while allowing the broader
  any-non-cancelled view to exist as a separately-named reporting concept if a real reporting need is later
  confirmed. This recommendation is not binding — it is recorded as TEAM B's reasoned position for Boss review.
- **Returned and Backordered are not independent commercial-line quantities** (§05 of
  [03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md)) — both are netting effects folded into
  Delivered/Received at the commercial layer, while remaining fully first-class, separately-tracked physical facts
  at the Movement/Transfer Operation layer. A target design exposing "Returned Quantity" as an independent field
  on a Commercial or Supply line would be inventing a concept this canonical design does not have at that layer.
- **No cross-field database-level relationship is assumed enforced anywhere in this register** (e.g., nothing in
  this canonical model assumes the database itself prevents Invoiced from exceeding Ordered) — TEAM B treats this
  as a genuine target-design decision, not a default: see
  [12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md)
  for the over-fulfillment/over-invoicing policy decision.

## 05 — Commitment vs. Fulfillment vs. Financial — The Three-Layer Rule

Restated as a standalone rule because it governs every quantity above: **a quantity belongs to exactly one of
three layers — Commitment (what was promised), Fulfillment (what physically happened), or Financial (what was
billed) — and no single stored field may serve two layers at once.** Every quantity in §§01–03 is tagged to
exactly one layer; where the reference system blurred this (e.g., letting a `quantity`-named field mean different
things pre- and post-execution), TEAM B's canonical model requires the *state* to disambiguate meaning explicitly,
never the field name alone (see [05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §01).
