# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_purchase Module Bridge MVQ Bank

**Document ID:** GMVQ-G08-SALE_PURCHASE-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_purchase`
**Wave:** W2
**Author Cell:** P-S6 (GMVQ Question Factory — Wave W2 Acceleration, 25-Team Programme)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `sale_purchase` — a BRIDGE per
GMVQ_BRIDGE_MODULE_RULE_V1.00, seam: a customer order line procured to order through a DIRECT
vendor order, with no stock movement in scope (that three-way seam belongs to the sibling
`sale_purchase_stock` bank and is deliberately not asked here) and no competitive tender or award
process in scope (that mechanism, and its own authority and margin-visibility questions, already
belongs to the existing `purchase_requisition_sale` bank on the procurement side of the group).
This bank's seam is narrower and more direct: one confirmed customer line generates one vendor
order (or shares one with other lines), with no requisition, tender, or vendor-selection contest
between them. Ground covered: the vendor price known only after the customer price was fixed, and
the margin that results; vendor lead time against the customer's committed date; a customer order
reduced or cancelled after the vendor order was already committed, and the resulting cancellation
cost; the vendor delivering a different quantity than the customer ordered; one vendor order
serving several customer orders; the direct link between the two documents surviving an edit to
either; who may change the vendor on a line already promised to a customer; the customer's
specification passed to the vendor and the commercial exposure that creates; and a vendor order
raised speculatively before the customer order is ever confirmed. Every question was tested
against the bridge removal test: if it would read equally well with no customer commitment in the
picture, it was cut as belonging to `purchase` alone; if it required a tender, bid, or award step
to make sense, it was cut as belonging to `purchase_requisition_sale` instead. Coverage spans
business capability, business rule, state transition, configuration dependency, role and
permission, exception path, cancellation, reversal, negative case, cross-module dependency,
optional behaviour, auditability, tenant/company boundary, concurrency and ordering, runtime
reachability, configuration reachability, and source/runtime contradiction potential.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material seam hypotheses; none was
  trimmed or stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table,
  field, method, XML ID, API path), and the module's own metadata name never appears outside the
  `MODULE:` field.
- No question requires a tender, bid, or formal award mechanism to make sense — that ground is
  reserved to `purchase_requisition_sale`; no question involves a physical stock receipt — that
  ground is reserved to `sale_purchase_stock`.
- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$G07_DIR"/*.md | sort`
  was run against the existing `purchase`, `purchase_requisition_sale` and `purchase_requisition_
  stock` banks before authoring. `purchase_requisition_sale` covers the tender/award seam in depth
  (award-versus-quote margin exposure, vendor lead time versus committed date, cancellation after
  award, customer-specific requirement constraining vendor selection, multi-order allocation and
  traceability, margin visibility as a permission, currency mismatch, multi-company); this bank
  keeps the same ground family but rebuilds every hypothesis and disconfirming observation around
  the DIRECT one-step order-to-vendor-order mechanism with no requisition, tender, or award entity
  anywhere in the observable event, so no question here restates one of theirs. `grep -h
  'HYPOTHESIS' "$G08_DIR"/*.md | sort` was run against the already-authored `sale_mrp` bank: its
  ground is production-triggered fulfilment (lead time from a production schedule, WIP ownership,
  yield shortfall, quality failure, item substitution) and none of it concerns a vendor order, a
  vendor price, or a vendor-side lead time, so no overlap exists.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_PURCHASE-Q001

```yaml
QID: G08-SALE_PURCHASE-Q001
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Because the vendor's price for a procure-to-order line is not known until after the customer
  price was already fixed, the resulting margin is computed and recorded once the vendor price is
  confirmed, not left implicitly assumed from the original estimate used at quotation.
WHY_IT_MATTERS: >
  Assuming the original estimate remains true hides a real margin change from whoever needs to
  know it actually happened.
DISCONFIRMING_OBSERVATION: >
  The vendor price used to source a procure-to-order line is confirmed at a different amount than
  the estimate used when the customer was quoted, and no updated margin figure results anywhere.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Quote a customer a price for a procure-to-order line, then confirm a vendor price different from
  the original estimate, and check for a resulting margin figure.
```

## G08-SALE_PURCHASE-Q002

```yaml
QID: G08-SALE_PURCHASE-Q002
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the confirmed vendor price causes the margin on a procure-to-order line to fall below an
  acceptable threshold, that condition is surfaced as a visible exception rather than the order
  proceeding unremarked.
WHY_IT_MATTERS: >
  An unremarked negative or thin margin removes the chance for someone accountable to decide
  whether to still proceed.
DISCONFIRMING_OBSERVATION: >
  A procure-to-order line's confirmed vendor price drives its margin below any reasonable
  threshold and the order proceeds with no flag, warning, or required acknowledgement.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Source a procure-to-order line at a vendor price that erodes margin below a normal threshold and
  observe whether any exception results.
```

## G08-SALE_PURCHASE-Q003

```yaml
QID: G08-SALE_PURCHASE-Q003
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The authority needed to proceed with a procure-to-order line once the vendor price is known to
  produce a reduced or negative margin is distinct from the authority needed to confirm an
  ordinary line whose cost was already known and acceptable at quotation.
WHY_IT_MATTERS: >
  Treating the two identically lets a low-authority action commit the business to a loss nobody
  with real authority ever agreed to.
DISCONFIRMING_OBSERVATION: >
  A user whose authority covers only ordinary line confirmation is able to proceed with a
  procure-to-order line despite its vendor price producing a negative margin, with no additional
  approval invoked.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with ordinary confirmation authority, attempt to proceed with a procure-to-order line
  whose confirmed vendor cost yields a negative margin.
```

## G08-SALE_PURCHASE-Q004

```yaml
QID: G08-SALE_PURCHASE-Q004
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The margin figure on a procure-to-order line, once the vendor price is known, is visible to a
  role with commercial oversight as a separately controllable permission, not bundled inseparably
  with an unrelated permission over the same order.
WHY_IT_MATTERS: >
  Bundling margin visibility with an unrelated permission means an organization cannot grant one
  without the other, even when its own controls call for separating them.
DISCONFIRMING_OBSERVATION: >
  There is no way to grant visibility of the margin figure without also granting an unrelated
  permission, or vice versa, on a procure-to-order line.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Attempt to configure a role with margin visibility on a procure-to-order line but without an
  unrelated permission it would ordinarily carry, and observe whether that separation is possible.
```

## G08-SALE_PURCHASE-Q005

```yaml
QID: G08-SALE_PURCHASE-Q005
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The vendor price attached to a procure-to-order line, once confirmed, is not silently revised
  later by an unrelated event without a recorded reason, since a customer price was already
  committed against it.
WHY_IT_MATTERS: >
  An unexplained cost revision after commitment breaks the traceability of why a margin figure
  changed.
DISCONFIRMING_OBSERVATION: >
  The vendor cost recorded against a procure-to-order line changes value at a later point with no
  recorded reason, actor, or triggering event.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm a vendor cost on a procure-to-order line, then trigger a later event that could
  plausibly change it, and inspect whether any change is recorded with a reason.
```

## G08-SALE_PURCHASE-Q006

```yaml
QID: G08-SALE_PURCHASE-Q006
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where the vendor price is still unknown at the moment the customer order is confirmed, the order
  does not proceed as though margin were already established and acceptable, but instead reflects
  that the figure is still provisional.
WHY_IT_MATTERS: >
  Presenting a provisional margin as settled misleads anyone reviewing the order's profitability
  before the real cost is known.
DISCONFIRMING_OBSERVATION: >
  A procure-to-order line whose vendor price has not yet been confirmed shows a margin figure
  indistinguishable from one whose cost is already settled.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm a customer order with a procure-to-order line before any vendor price is confirmed, and
  inspect how its margin is represented.
```

## G08-SALE_PURCHASE-Q007

```yaml
QID: G08-SALE_PURCHASE-Q007
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The date committed to the customer on a procure-to-order line reflects the vendor's actual
  stated lead time, not a generic estimate applied regardless of which vendor or item is actually
  sourcing it.
WHY_IT_MATTERS: >
  A generic estimate risks promising a date the specific vendor sourcing the order cannot actually
  meet.
DISCONFIRMING_OBSERVATION: >
  Two procure-to-order lines sourced from vendors with materially different stated lead times
  receive an identical committed customer date with no reference to either lead time.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Source two procure-to-order lines from vendors with different stated lead times and compare the
  committed customer dates offered.
```

## G08-SALE_PURCHASE-Q008

```yaml
QID: G08-SALE_PURCHASE-Q008
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the vendor's stated lead time already makes the customer's requested date unreachable at
  the moment of sourcing, that conflict is surfaced as a controllable exception before the order
  proceeds, not discovered only after commitment.
WHY_IT_MATTERS: >
  Discovering the conflict only after commitment leaves no opportunity to reset expectations or
  choose another vendor while there is still time.
DISCONFIRMING_OBSERVATION: >
  A vendor's stated lead time already makes the customer's requested date unreachable at the time
  of sourcing, and the order proceeds to commitment with no exception raised.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Source a procure-to-order line from a vendor whose stated lead time already exceeds the
  customer's requested date, and observe whether an exception results before commitment.
```

## G08-SALE_PURCHASE-Q009

```yaml
QID: G08-SALE_PURCHASE-Q009
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the vendor's lead time changes after the customer date was already committed, that change is
  reflected as an update or exception on the customer-facing commitment, not silently absorbed
  with the original date left standing.
WHY_IT_MATTERS: >
  An unremarked lead-time change leaves a commitment standing that the business already knows it
  cannot keep.
DISCONFIRMING_OBSERVATION: >
  The vendor's stated lead time changes after the customer date was committed, and the
  customer-facing commitment shows no resulting update or flag.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Commit a customer date based on an initial vendor lead time, then change that lead time, and
  inspect the customer-facing commitment for any resulting change.
```

## G08-SALE_PURCHASE-Q010

```yaml
QID: G08-SALE_PURCHASE-Q010
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Responsibility for deciding what to tell the customer when the vendor's lead time will not meet
  the committed date is assignable to a specific role, not left as an implicit expectation with no
  owner recorded.
WHY_IT_MATTERS: >
  An unowned conflict is one nobody is accountable for actually resolving before the customer
  feels the consequence.
DISCONFIRMING_OBSERVATION: >
  A detected conflict between vendor lead time and customer commitment produces no assignable
  owner, recipient, or task distinguishable from a routine status entry.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Create a lead-time conflict against a committed customer date and inspect whether any owner or
  actionable assignment results.
```

## G08-SALE_PURCHASE-Q011

```yaml
QID: G08-SALE_PURCHASE-Q011
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where more than one vendor could source the same procure-to-order line, the vendor's relative
  lead time is available as a visible factor at the point of choosing, not something apparent only
  after commitment.
WHY_IT_MATTERS: >
  A business unable to see lead time before choosing routinely commits to the slower option by
  accident rather than by decision.
DISCONFIRMING_OBSERVATION: >
  Choosing among vendors capable of sourcing the same line offers no visible comparison of their
  respective lead times before commitment.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Identify two vendors capable of sourcing the same procure-to-order line with different lead
  times, and inspect what is visible to whoever chooses between them.
```

## G08-SALE_PURCHASE-Q012

```yaml
QID: G08-SALE_PURCHASE-Q012
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a customer order after its procure-to-order line has already been committed to a
  vendor surfaces that conflict as a visible exception, not silently proceeding as though nothing
  downstream were affected.
WHY_IT_MATTERS: >
  An unremarked cancellation leaves a live vendor commitment nobody is tracking against a customer
  who no longer wants it.
DISCONFIRMING_OBSERVATION: >
  Cancelling a customer order whose line was already committed to a vendor produces no visible
  flag, exception, or required action referencing the still-live vendor commitment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Commit a procure-to-order line to a vendor, cancel the originating customer order, and inspect
  whether any exception results.
```

## G08-SALE_PURCHASE-Q013

```yaml
QID: G08-SALE_PURCHASE-Q013
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a customer order is cancelled after its vendor commitment was made, there is a defined path
  to cancel or reduce that vendor commitment, rather than the only available action being to let
  it proceed regardless.
WHY_IT_MATTERS: >
  With no cancellation path, the business is forced to accept and pay for goods or services a
  customer no longer wants.
DISCONFIRMING_OBSERVATION: >
  After a customer order is cancelled post-commitment, no action allows cancelling or reducing the
  corresponding vendor commitment — proceeding with it unchanged is the only available option.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Commit a procure-to-order line to a vendor, cancel the customer order, and examine what actions
  are available against the vendor commitment.
```

## G08-SALE_PURCHASE-Q014

```yaml
QID: G08-SALE_PURCHASE-Q014
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A cancellation charge imposed by a vendor as a result of a customer cancellation is recorded as
  attributable to that specific customer cancellation, not left as an unexplained cost with no
  link to what caused it.
WHY_IT_MATTERS: >
  An unlinked charge leaves nobody able to recover it from, or even explain it to, the customer
  whose cancellation actually caused it.
DISCONFIRMING_OBSERVATION: >
  A vendor cancellation charge exists in the records following a customer cancellation with no
  link back to the customer order that triggered it.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Cancel a customer order after vendor commitment such that a vendor cancellation charge results,
  and inspect whether that charge is linked back to the customer cancellation.
```

## G08-SALE_PURCHASE-Q015

```yaml
QID: G08-SALE_PURCHASE-Q015
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reducing, rather than fully cancelling, a customer order's quantity after vendor commitment
  surfaces the same kind of exception as a full cancellation would, proportional to the reduction,
  rather than only full cancellations being handled.
WHY_IT_MATTERS: >
  A partial reduction that goes unremarked leaves the business committed to more vendor supply
  than any remaining customer demand actually needs.
DISCONFIRMING_OBSERVATION: >
  Reducing a customer order's quantity after vendor commitment produces no exception or flag,
  while a full cancellation of the same order would have produced one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Commit a procure-to-order line to a vendor, reduce the customer order's quantity rather than
  cancelling it outright, and inspect whether an exception results.
```

## G08-SALE_PURCHASE-Q016

```yaml
QID: G08-SALE_PURCHASE-Q016
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The decision to accept a vendor cancellation charge and absorb it, rather than seeking recovery
  from the customer, requires authority distinct from ordinary order cancellation.
WHY_IT_MATTERS: >
  Treating the financial absorption of a vendor charge as an ordinary cancellation action lets a
  cost be accepted with nobody accountable for that specific decision.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary order-cancellation permission is able to finalize acceptance of a
  vendor cancellation charge with no additional approval invoked.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with only ordinary cancellation permission, attempt to finalize a customer order
  cancellation that results in a vendor charge.
```

## G08-SALE_PURCHASE-Q017

```yaml
QID: G08-SALE_PURCHASE-Q017
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where the vendor has already partially fulfilled a commitment by the time a customer
  cancellation is processed, the record distinguishes the already-fulfilled portion from the
  portion that can still be cancelled without cost.
WHY_IT_MATTERS: >
  Failing to distinguish the two portions risks either cancelling something already irreversibly
  committed or paying to cancel something that was never actually started.
DISCONFIRMING_OBSERVATION: >
  A customer cancellation is processed against a vendor commitment that was already partially
  fulfilled, with no indication of which portion was already fulfilled and which was not.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Partially fulfil a vendor commitment, then process a customer cancellation against it, and
  inspect whether the record distinguishes the fulfilled and unfulfilled portions.
```

## G08-SALE_PURCHASE-Q018

```yaml
QID: G08-SALE_PURCHASE-Q018
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a vendor delivers a quantity different from what the procure-to-order line requested, the
  resulting discrepancy against the customer order is surfaced as a visible exception, not
  silently treated as the order fully satisfied.
WHY_IT_MATTERS: >
  A silently accepted discrepancy leaves the customer commitment either overstated or understated
  with nobody deciding what to do about it.
DISCONFIRMING_OBSERVATION: >
  A vendor delivers a quantity different from what was ordered, and the customer order it was
  sourcing shows no discrepancy flag or resulting exception.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Source a procure-to-order line, receive a vendor delivery at a different quantity than ordered,
  and inspect the state of the customer order.
```

## G08-SALE_PURCHASE-Q019

```yaml
QID: G08-SALE_PURCHASE-Q019
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A vendor shortfall against a procure-to-order line does not cause the customer-facing order to
  be marked as fully satisfied at the originally promised quantity.
WHY_IT_MATTERS: >
  Marking the order fully satisfied when it was not misleads whoever next checks whether the
  customer commitment was actually met.
DISCONFIRMING_OBSERVATION: >
  A vendor delivers less than the ordered quantity, and the customer order is marked as fully
  satisfied at the original quantity regardless.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Source a procure-to-order line, receive a vendor shortfall, and check the resulting fulfilment
  state of the customer order.
```

## G08-SALE_PURCHASE-Q020

```yaml
QID: G08-SALE_PURCHASE-Q020
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A vendor delivering more than the procure-to-order line requested does not cause the customer to
  be committed to, billed for, or shipped the excess without a deliberate decision about what
  happens to it.
WHY_IT_MATTERS: >
  Passing an unrequested excess straight through to the customer or into unmanaged stock removes a
  decision that should belong to someone.
DISCONFIRMING_OBSERVATION: >
  A vendor delivers more than the procure-to-order line requested, and the excess quantity is
  passed to the customer commitment or elsewhere with no distinguishable decision point.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Source a procure-to-order line, receive a vendor over-delivery, and inspect how the excess
  quantity is handled.
```

## G08-SALE_PURCHASE-Q021

```yaml
QID: G08-SALE_PURCHASE-Q021
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the customer order allows only an exact quantity match, a vendor quantity discrepancy
  blocks progression to the customer-facing fulfilment step until resolved, rather than allowing
  the mismatched quantity straight through.
WHY_IT_MATTERS: >
  Letting a mismatched quantity through when an exact match was required breaks a commitment the
  business specifically made to the customer.
DISCONFIRMING_OBSERVATION: >
  A customer order requiring an exact quantity match proceeds to its fulfilment step despite a
  vendor delivery discrepancy, with no block or hold.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Configure a customer order requiring an exact quantity match, introduce a vendor delivery
  discrepancy, and observe whether fulfilment is blocked.
```

## G08-SALE_PURCHASE-Q022

```yaml
QID: G08-SALE_PURCHASE-Q022
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A vendor quantity discrepancy against a procure-to-order line that serves more than one customer
  order is attributed to those orders by a defined rule, not by whichever order happens to be
  processed first.
WHY_IT_MATTERS: >
  An undefined attribution rewards processing order over any real business priority when a vendor
  discrepancy has to be shared out.
DISCONFIRMING_OBSERVATION: >
  Repeating an identical vendor discrepancy scenario against the same set of customer orders
  sharing the sourcing produces a different attribution between them on separate occasions.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Source a vendor discrepancy against a procurement serving more than one customer order and
  repeat the scenario to compare attribution outcomes.
```

## G08-SALE_PURCHASE-Q023

```yaml
QID: G08-SALE_PURCHASE-Q023
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When one vendor order is raised to cover several customer orders' procure-to-order lines at
  once, each contributing customer order's share remains individually identifiable in the vendor
  order's own record.
WHY_IT_MATTERS: >
  Losing the individual breakdown makes it impossible to later verify each customer received what
  was actually sourced for them.
DISCONFIRMING_OBSERVATION: >
  A vendor order covering several customer orders' lines provides no way to determine which
  portion of it belongs to which customer order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Raise one vendor order to cover procure-to-order lines from more than one customer order and
  inspect whether each one's share is identifiable.
```

## G08-SALE_PURCHASE-Q024

```yaml
QID: G08-SALE_PURCHASE-Q024
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a vendor order consolidating several customer orders is edited to add further demand after
  being submitted to the vendor but before any vendor acknowledgement, the recorded committed
  quantity does not exceed what the vendor has actually confirmed accepting.
WHY_IT_MATTERS: >
  Treating an unacknowledged addition as already committed overstates what the business can
  actually promise customers depending on it.
DISCONFIRMING_OBSERVATION: >
  A vendor order's recorded committed quantity includes demand added after submission but before
  vendor acknowledgement, with no distinction from the quantity the vendor actually confirmed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit a consolidated vendor order, add further customer demand to it before the vendor
  acknowledges, and inspect the order's recorded committed quantity against the vendor's actual
  acknowledgement.
```

## G08-SALE_PURCHASE-Q025

```yaml
QID: G08-SALE_PURCHASE-Q025
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling one of several customer orders sharing a consolidated vendor order reduces or
  releases only that order's own share, leaving the vendor commitment for the remaining customer
  orders intact and unaffected.
WHY_IT_MATTERS: >
  A cancellation bleeding into other customers' shares would harm customers who did nothing to
  cause the cancellation.
DISCONFIRMING_OBSERVATION: >
  Cancelling one customer order sharing a consolidated vendor order changes the quantity or terms
  attributable to a different, still-active customer order sharing the same vendor order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel one customer order among several sharing a consolidated vendor order and inspect the
  effect on the other, still-active customer orders.
```

## G08-SALE_PURCHASE-Q026

```yaml
QID: G08-SALE_PURCHASE-Q026
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cost variance on a consolidated vendor order is distributed across the contributing customer
  orders by a defined, visible basis, rather than the full variance landing against whichever
  order happens to be recorded first.
WHY_IT_MATTERS: >
  An undistributed variance charged arbitrarily to one customer misstates that specific order's
  true margin while understating the others'.
DISCONFIRMING_OBSERVATION: >
  The full cost variance from one consolidated vendor order lands against a single contributing
  customer order with no rule explaining why that one absorbed it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a cost variance on a vendor order consolidating several customer orders' demand and
  inspect how that variance is distributed.
```

## G08-SALE_PURCHASE-Q027

```yaml
QID: G08-SALE_PURCHASE-Q027
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Adding a new customer order to an already-raised, not-yet-fulfilled consolidated vendor order is
  a distinguishable, deliberate action, not something that happens as a silent side effect of
  unrelated activity.
WHY_IT_MATTERS: >
  An unremarked addition to a live vendor commitment removes anyone's chance to check the vendor
  can actually absorb the increased quantity.
DISCONFIRMING_OBSERVATION: >
  A new customer order's demand attaches to an already-raised vendor order with no distinguishable
  action or record showing that the attachment occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Raise a consolidated vendor order for one customer order's demand, then introduce a second
  customer order whose demand could attach to it, and inspect whether attachment is a visible,
  deliberate action.
```

## G08-SALE_PURCHASE-Q028

```yaml
QID: G08-SALE_PURCHASE-Q028
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Consolidating several customer orders' demand into a single vendor order is a distinguishable,
  deliberate action attributable to a specific actor, not an incidental side effect with no record
  of who decided to combine them.
WHY_IT_MATTERS: >
  An unattributed consolidation decision means nobody can later explain why several customers'
  supply became dependent on one single vendor commitment.
DISCONFIRMING_OBSERVATION: >
  Several customer orders' demand ends up combined into a single vendor order with no record of
  who made that consolidation decision or when.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consolidate several customer orders' procure-to-order lines into a single vendor order and
  inspect the record for who made that consolidation decision.
```

## G08-SALE_PURCHASE-Q029

```yaml
QID: G08-SALE_PURCHASE-Q029
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The link between a procure-to-order customer line and the vendor order sourcing it survives an
  edit to the customer order's own unrelated fields, such as its terms or delivery address,
  without being cleared or broken.
WHY_IT_MATTERS: >
  A fragile link that breaks on unrelated edits means routine order maintenance can silently sever
  the very traceability the seam depends on.
DISCONFIRMING_OBSERVATION: >
  Editing an unrelated field on a customer order whose line is linked to a vendor order results in
  that link no longer resolving.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Link a customer order line to a vendor order, edit an unrelated field on the customer order, and
  check whether the link still resolves.
```

## G08-SALE_PURCHASE-Q030

```yaml
QID: G08-SALE_PURCHASE-Q030
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The link between a procure-to-order customer line and its vendor order similarly survives an
  edit to the vendor order's own unrelated fields.
WHY_IT_MATTERS: >
  The same fragility on the vendor side would sever traceability just as easily from routine
  vendor-side maintenance.
DISCONFIRMING_OBSERVATION: >
  Editing an unrelated field on a vendor order whose line is linked to a customer order results in
  that link no longer resolving.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Link a vendor order line to a customer order, edit an unrelated field on the vendor order, and
  check whether the link still resolves.
```

## G08-SALE_PURCHASE-Q031

```yaml
QID: G08-SALE_PURCHASE-Q031
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the quantity is edited independently on the customer order and on the vendor order line after
  the link between them was made, there is a defined rule for whether and how the two are
  reconciled, rather than the mismatch persisting unremarked.
WHY_IT_MATTERS: >
  An unreconciled mismatch leaves the business unable to tell which of the two quantities actually
  governs what happens next.
DISCONFIRMING_OBSERVATION: >
  The customer order quantity and the linked vendor order quantity are edited independently after
  the link is made, and neither is flagged as inconsistent with the other.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Link a customer order line to a vendor order line, edit the quantity independently on each side,
  and inspect whether any reconciliation or flag results.
```

## G08-SALE_PURCHASE-Q032

```yaml
QID: G08-SALE_PURCHASE-Q032
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling the vendor order side of the link, while the customer order remains open, leaves a
  visible signal on the customer order that its sourcing is no longer in place, rather than the
  customer order appearing unaffected.
WHY_IT_MATTERS: >
  An unaffected-looking customer order hides the fact that nothing is actually sourcing it any
  more.
DISCONFIRMING_OBSERVATION: >
  Cancelling the vendor order linked to an open customer order line leaves that customer order
  showing no change and no indication that its sourcing no longer exists.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a vendor order linked to an open customer order line and inspect the customer order for
  any resulting change.
```

## G08-SALE_PURCHASE-Q033

```yaml
QID: G08-SALE_PURCHASE-Q033
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The link between a procure-to-order line and its vendor order cannot be silently detached
  through an ordinary edit to either document, since the traceability it provides depends on the
  link surviving routine maintenance.
WHY_IT_MATTERS: >
  A link removable by an ordinary edit offers no real assurance that it will still be there when
  it is actually needed.
DISCONFIRMING_OBSERVATION: >
  An ordinary edit to either the customer order or the vendor order removes or overwrites the link
  between them with no special permission or warning required.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt an ordinary edit to a linked customer or vendor order that would remove the existing
  link, and observe whether any special step is required.
```

## G08-SALE_PURCHASE-Q034

```yaml
QID: G08-SALE_PURCHASE-Q034
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Changing the vendor sourcing a procure-to-order line after the customer has already been given a
  committed date requires an authority distinct from choosing the vendor before any customer
  commitment existed.
WHY_IT_MATTERS: >
  Treating both cases identically lets a low-authority action risk a customer-facing commitment
  nobody with real authority reviewed.
DISCONFIRMING_OBSERVATION: >
  A user whose authority covers only initial vendor selection is able to change the vendor on a
  line with an already-committed customer date, with no additional approval invoked.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with only initial vendor-selection authority, attempt to change the vendor on a line
  already carrying a committed customer date.
```

## G08-SALE_PURCHASE-Q035

```yaml
QID: G08-SALE_PURCHASE-Q035
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing the vendor on a line already promised to a customer is recorded as a distinguishable
  event, including who made the change and why, rather than looking identical to the line having
  been sourced from that vendor from the start.
WHY_IT_MATTERS: >
  An indistinguishable change removes any way to later investigate why a specific vendor ended up
  sourcing a customer's order.
DISCONFIRMING_OBSERVATION: >
  The vendor on a line already promised to a customer is changed, and the record shows no
  distinguishable trace of the change, its actor, or its reason.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change the vendor on a line already promised to a customer and inspect the order's history for a
  record of the change.
```

## G08-SALE_PURCHASE-Q036

```yaml
QID: G08-SALE_PURCHASE-Q036
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where changing the vendor on an already-promised line would also change the committed customer
  date or price, that consequence is surfaced before the change is finalized, not discovered only
  afterward.
WHY_IT_MATTERS: >
  Discovering the consequence after the fact removes the chance to reconsider or renegotiate with
  the customer before the change is locked in.
DISCONFIRMING_OBSERVATION: >
  Changing the vendor on an already-promised line silently changes the committed date or price
  with no warning shown before the change is finalized.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change the vendor on a line already promised to a customer to one with a different lead time or
  cost, and observe what is shown before the change is finalized.
```

## G08-SALE_PURCHASE-Q037

```yaml
QID: G08-SALE_PURCHASE-Q037
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reverting a vendor change on an already-promised line back to the original vendor is possible
  only while the original commitment has not itself been superseded, not silently allowed
  regardless of what has happened since.
WHY_IT_MATTERS: >
  Allowing an unconditional revert risks contradicting other actions that already assumed the
  changed vendor was final.
DISCONFIRMING_OBSERVATION: >
  A vendor change on an already-promised line is reverted after other actions already assumed the
  new vendor, with no warning or block reflecting that inconsistency.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change the vendor on a promised line, take a further action assuming the new vendor, then
  attempt to revert to the original vendor.
```

## G08-SALE_PURCHASE-Q038

```yaml
QID: G08-SALE_PURCHASE-Q038
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A vendor change on a line already promised to a customer in one company is not made by a user
  whose authority is scoped to a different company, even where the vendor pool happens to be
  shared.
WHY_IT_MATTERS: >
  Allowing a cross-company change lets someone with no accountability in the affected company
  alter a commitment that company actually made.
DISCONFIRMING_OBSERVATION: >
  A user whose authority is scoped to one company is able to change the vendor on a promised line
  belonging to a different company sharing the same vendor pool.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user scoped to one company, attempt to change the vendor on a promised line belonging to a
  different company in a multi-company setup with a shared vendor pool.
```

## G08-SALE_PURCHASE-Q039

```yaml
QID: G08-SALE_PURCHASE-Q039
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A customer-specific specification carried through to the vendor order constrains which vendor
  responses or deliveries are acceptable, rather than any vendor delivery being accepted
  regardless of whether it matches what the customer actually specified.
WHY_IT_MATTERS: >
  Accepting a non-matching delivery against a customer-specific specification risks passing the
  customer something they did not actually order.
DISCONFIRMING_OBSERVATION: >
  A vendor delivery that does not meet the customer-specific specification carried onto the vendor
  order is accepted and passed through to fulfil the customer commitment with no flag.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Carry a customer-specific specification onto a vendor order, receive a vendor delivery that does
  not meet it, and inspect whether it is accepted without flag.
```

## G08-SALE_PURCHASE-Q040

```yaml
QID: G08-SALE_PURCHASE-Q040
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Information from the customer's specification that is commercially sensitive, such as their own
  intended use or identity, is passed to the vendor only to the extent the sourcing actually
  requires, not exposed in full by default regardless of necessity.
WHY_IT_MATTERS: >
  Unnecessary exposure of a customer's commercial details to a third-party vendor creates a real
  exposure the customer never agreed to.
DISCONFIRMING_OBSERVATION: >
  The vendor order carries customer-identifying or commercially sensitive detail from the
  specification that the sourcing did not actually require.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create a procure-to-order line from a customer specification containing sensitive commercial
  detail and inspect what is actually carried onto the resulting vendor order.
```

## G08-SALE_PURCHASE-Q041

```yaml
QID: G08-SALE_PURCHASE-Q041
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the vendor cannot meet the customer's specification as passed, that failure is surfaced as an
  exception routed to a role able to decide how to proceed with the customer, not silently treated
  as an ordinary vendor delay.
WHY_IT_MATTERS: >
  Treating a specification failure as an ordinary delay hides a situation where the customer may
  need an entirely different resolution.
DISCONFIRMING_OBSERVATION: >
  A vendor's inability to meet the passed customer specification is recorded identically to an
  ordinary delivery delay, with no distinguishing exception or routed decision.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Source a procure-to-order line against a customer specification the vendor cannot meet, and
  inspect how that failure is recorded compared with an ordinary delay.
```

## G08-SALE_PURCHASE-Q042

```yaml
QID: G08-SALE_PURCHASE-Q042
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to the customer's specification after the vendor order has already been placed is
  propagated to the vendor order or raised as an exception, not left with the vendor sourcing
  against the original, now-superseded specification unremarked.
WHY_IT_MATTERS: >
  Leaving the vendor sourcing an outdated specification risks delivering something the customer no
  longer wants with nobody having caught the mismatch.
DISCONFIRMING_OBSERVATION: >
  The customer's specification changes after the vendor order is placed, and the vendor order
  proceeds against the original specification with no propagation or exception.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Place a vendor order against a customer specification, change that specification afterward, and
  inspect whether the vendor order is affected or flagged.
```

## G08-SALE_PURCHASE-Q043

```yaml
QID: G08-SALE_PURCHASE-Q043
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Commercial exposure arising from passing a customer's specification to a vendor, such as a
  resulting vendor claim or dispute over what was actually specified, is traceable back to the
  exact specification in effect when the vendor order was placed, not a specification that may
  have since changed.
WHY_IT_MATTERS: >
  Without that exact-version trace, a dispute over what was actually specified at the time cannot
  be resolved from the business's own records.
DISCONFIRMING_OBSERVATION: >
  A dispute over the specification passed to the vendor cannot be resolved against the exact
  version in effect at the time the vendor order was placed, because only the current, possibly
  since-changed specification is available.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Place a vendor order against a customer specification, change that specification afterward, and
  attempt to retrieve the exact specification version in effect at the time the vendor order was
  placed.
```

## G08-SALE_PURCHASE-Q044

```yaml
QID: G08-SALE_PURCHASE-Q044
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A vendor order raised in anticipation of a customer order that is never actually confirmed
  leaves a visible, distinguishable record that its originating customer commitment never
  materialized, rather than appearing identical to a vendor order backing a confirmed sale.
WHY_IT_MATTERS: >
  An indistinguishable record hides real, uncommitted vendor spend inside what looks like ordinary
  confirmed-order activity.
DISCONFIRMING_OBSERVATION: >
  A vendor order raised against a customer order that is never confirmed looks, in every visible
  respect, identical to one backing a confirmed customer order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Raise a vendor order from an unconfirmed customer order that is never subsequently confirmed,
  and inspect whether that fact is visible on the vendor order.
```

## G08-SALE_PURCHASE-Q045

```yaml
QID: G08-SALE_PURCHASE-Q045
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Raising a vendor order from a customer order that is not yet confirmed is a deliberate,
  discoverable configuration behaviour, not an unstated default that commits real vendor spend
  before the customer commitment is actually firm.
WHY_IT_MATTERS: >
  An unstated default risks the business routinely committing real money to unconfirmed,
  speculative demand with nobody having deliberately allowed that.
DISCONFIRMING_OBSERVATION: >
  Two comparably configured environments differ on whether an unconfirmed customer order is able
  to raise a vendor order, with no discoverable setting explaining the difference.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Attempt to raise a vendor order from an unconfirmed customer order in two separately configured
  environments and compare the outcome.
```

## G08-SALE_PURCHASE-Q046

```yaml
QID: G08-SALE_PURCHASE-Q046
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a vendor order was raised against a customer order that is later never confirmed and
  instead lapses or is withdrawn, there is a defined path to cancel that vendor order, rather than
  the only option being to let it proceed regardless.
WHY_IT_MATTERS: >
  With no cancellation path, speculative vendor spend against demand that never materialized
  cannot be stopped.
DISCONFIRMING_OBSERVATION: >
  A customer order that raised a vendor order lapses or is withdrawn without ever being confirmed,
  and no action allows cancelling the resulting vendor order.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Raise a vendor order from an unconfirmed customer order, let that customer order lapse or be
  withdrawn, and examine what actions are available against the vendor order.
```

## G08-SALE_PURCHASE-Q047

```yaml
QID: G08-SALE_PURCHASE-Q047
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Raising a vendor order from an unconfirmed customer order requires an authority distinct from
  raising one from an already-confirmed order, given the additional risk of committing to demand
  that may never materialize.
WHY_IT_MATTERS: >
  Treating both cases identically lets speculative vendor commitment happen with no one
  specifically accountable for that added risk.
DISCONFIRMING_OBSERVATION: >
  A user whose authority covers only vendor orders raised from confirmed customer orders is able
  to raise one from an unconfirmed customer order with no additional approval invoked.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with authority limited to confirmed-order sourcing, attempt to raise a vendor order
  from an unconfirmed customer order.
```

## G08-SALE_PURCHASE-Q048

```yaml
QID: G08-SALE_PURCHASE-Q048
MODULE: sale_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A customer order that never confirms after having already raised a vendor order remains linked
  to that vendor order for as long as the vendor order exists, so the vendor commitment's origin
  remains traceable even though the customer side never became firm.
WHY_IT_MATTERS: >
  Losing that trace once the customer order is abandoned leaves an unexplained vendor commitment
  with no way to establish why it exists.
DISCONFIRMING_OBSERVATION: >
  An unconfirmed customer order that raised a vendor order is deleted or archived, and the vendor
  order's link back to its originating customer order can no longer be resolved.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Raise a vendor order from an unconfirmed customer order, archive or delete that customer order,
  and attempt to trace the vendor order back to it.
```
