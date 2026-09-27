# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_stock_product_expiry Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-SALE_STOCK_PRODUCT_EXPIRY-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_stock_product_expiry`
**Wave:** W2
**Author Cell:** TEAM P-S5 (GMVQ Question Factory — Production Cell P-S5, Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This module is a seam of a seam: shelf life constraining what may be promised and shipped to a customer.
That, and only that, is this bank's ground. A question that would still make sense with no customer promise
in it belongs to shelf-life mechanics alone (G05 INVENTORY / `product_expiry`); a question that would still
make sense with no shelf-life fact in it belongs to the commercial-order-to-movement seam alone (this
group's `sale_stock` bank). This bank supplements the 55 Standard Questions with module-specific,
adversarial questions covering: a customer contract requiring a minimum remaining shelf life at delivery and
the order promising stock that will not meet it; availability counted including units that will expire
before the committed date; a long-dated order confirmed against short-dated stock; the removal strategy
picking the shortest-dated lot and the customer specifying otherwise; a delivery delayed until the reserved
lot is no longer acceptable; partial delivery from two lots with different dates and what the customer is
told; a return of stock whose remaining life is now too short to resell; the expiry date printed on the
customer document versus the one shipped; and who may override a shelf-life rule to complete a sale, and
what trace that leaves.

Per the Bridge Module Rule (V1.00), applied here at double strength (a bridge of a bridge): every question
below requires BOTH a customer-facing commercial promise AND a shelf-life fact to exist together. The
removal test was applied to every question: if it would still make sense with the shelf-life fact removed
and only the commercial seam left, or with the customer promise removed and only shelf-life mechanics left,
it was cut. Question text is source-neutral: no vendor or product name, no technical identifier (model,
table, field, method, XML ID, API path), and no reference to how any specific implementation is built.
Language is generic business/behavioural language throughout.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, cross-module dependency, auditability, tenant/company boundary,
  concurrency and ordering, and runtime/configuration reachability.
- This module carries both a configuration layer (per-customer shelf-life terms, hard-block vs
  soft-warning mode, per-company scoping) and a runtime process layer (what happens at confirmation,
  reservation, picking, dispatch, return and documentation); each question is tagged `LAYER: BASE` or
  `LAYER: PROCESS` accordingly.
- Pre-authoring sibling check (Bridge Module Rule §5): `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G05_INVENTORY/G05_PRODUCT_EXPIRY*.md`
  and `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G08_SALES/*.md` were both run before authoring.
  G05_PRODUCT_EXPIRY's 48 hypotheses cover shelf-life mechanics entirely inside the warehouse — removal
  strategy, blocking, alerting, valuation write-down, override permission for warehouse operations, and
  per-lot/per-location consistency — with no customer order or contractual term anywhere in them. This
  bank's own sibling, `sale_stock`, covers available-to-promise, reservation timing, delivery, returns and
  invoicing with no shelf-life fact anywhere in it. This bank restates neither: every hypothesis below is
  keyed to a customer-specific shelf-life term or a customer-facing consequence, which is why it belongs
  here and not in either sibling.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a
  Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q001

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q001
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A customer-specific minimum remaining shelf-life requirement, when configured, is checked against a
  lot's dates before that lot is allowed to be promised on that customer's order.
WHY_IT_MATTERS: >
  If the check happens after the promise is made rather than before, the business has already told the
  customer something it may not be able to honour.
DISCONFIRMING_OBSERVATION: >
  An order line for a customer with a configured minimum shelf-life requirement is promised against a lot
  that does not meet it, with no check having occurred before the promise was made.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure a customer minimum shelf-life requirement, then attempt to promise a lot that does not meet it
  on that customer's order.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q002

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q002
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An order line for a customer with a minimum-shelf-life requirement, confirmed against a lot that will
  not meet that requirement by the committed delivery date, is flagged or blocked rather than confirmed
  identically to an order with no such requirement.
WHY_IT_MATTERS: >
  Confirming identically to an unconstrained order hides the one fact that most matters for this customer:
  their stock will not meet the contract.
DISCONFIRMING_OBSERVATION: >
  An order confirmed against a lot failing the customer's requirement shows no different state than an
  order confirmed against a fully qualifying lot.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Confirm an order for a customer with a shelf-life requirement against a lot that will not meet it by the
  committed date, and compare its state to a normally confirmed order.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q003

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q003
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The customer's minimum shelf-life requirement, once configured, applies to every order for that customer
  without needing to be manually reasserted line by line.
WHY_IT_MATTERS: >
  A requirement that must be manually reapplied on every order will eventually be forgotten on one of them.
DISCONFIRMING_OBSERVATION: >
  A new order for a customer with a configured requirement is confirmed with no check performed unless
  someone manually re-enters the requirement on that order.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a customer's shelf-life requirement once, then create and confirm a fresh order for that
  customer without re-entering it.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q004

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q004
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A customer with no minimum-shelf-life requirement configured is not blocked by a shelf-life check meant
  for a different customer's stricter contract.
WHY_IT_MATTERS: >
  A check leaking across customers would block or delay orders for customers who never asked for any such
  guarantee.
DISCONFIRMING_OBSERVATION: >
  An order for a customer with no configured shelf-life requirement is blocked or flagged by a shelf-life
  check anyway.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Configure a strict requirement for one customer only, then confirm an order for a different customer
  against the same short-dated stock.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q005

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q005
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a customer's minimum-shelf-life requirement changes after an order is already confirmed against a
  previously-acceptable lot, the existing order is not silently re-evaluated and invalidated without any
  visible flag.
WHY_IT_MATTERS: >
  Retroactively invalidating an already-confirmed promise with no notice leaves fulfilment staff unaware
  the order needs attention.
DISCONFIRMING_OBSERVATION: >
  Tightening a customer's requirement after an order was already confirmed against a previously-acceptable
  lot causes that order to silently change state with no visible flag.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order against a qualifying lot, then tighten the customer's shelf-life requirement so that lot
  would no longer qualify, and check what happens to the existing order.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q006

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q006
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The available-to-promise figure shown for a customer order does not count a lot that will pass its
  shelf-life limit before the order's committed delivery date as though it were fully available for that
  promise.
WHY_IT_MATTERS: >
  Promising stock that will not exist in an acceptable state by the delivery date is a promise already
  known, at the moment it is made, to be false.
DISCONFIRMING_OBSERVATION: >
  A lot that will fall below a customer's shelf-life requirement before the order's committed delivery date
  is still shown as available to promise for that date.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Set a committed delivery date far enough out that a currently qualifying lot will no longer qualify by
  then, and check what availability is shown for a customer with that requirement.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q007

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q007
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Two customers with different configured shelf-life requirements querying the same product's availability
  at the same moment can see different available quantities, reflecting which lots actually qualify for
  each.
WHY_IT_MATTERS: >
  If every customer sees the same undifferentiated figure, the figure is meaningless for whichever customer
  has an actual contractual requirement.
DISCONFIRMING_OBSERVATION: >
  Two customers with different configured shelf-life requirements are shown identical available quantity
  for the same product at the same moment, despite different lots qualifying for each.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Configure two customers with different minimum shelf-life requirements, and compare the availability each
  sees for the same product.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q008

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q008
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A lot that qualifies as available to promise today, but will fall short of a customer's requirement by a
  delivery date several weeks out, is excluded from what can be promised for that specific future date,
  even while it remains promisable for a nearer date.
WHY_IT_MATTERS: >
  A single available-to-promise figure that ignores the requested date entirely cannot distinguish a
  promise that is safe from one that is not.
DISCONFIRMING_OBSERVATION: >
  The same lot is shown as available to promise for both a near and a far committed date to the same
  shelf-life-constrained customer, even though it will not qualify by the far date.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Check availability for a shelf-life-constrained customer against the same lot for two different committed
  dates, one within and one beyond its qualifying window.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q009

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q009
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Confirming a long-lead-time order against currently on-hand short-dated stock, when no longer-dated
  alternative or incoming replenishment can be identified, is blocked or explicitly flagged rather than
  silently accepted as covered.
WHY_IT_MATTERS: >
  Confirming such an order as covered, with nothing else in the pipeline able to satisfy it later, sets an
  expectation nothing currently justifies.
DISCONFIRMING_OBSERVATION: >
  A long-lead order is confirmed as fully covered by current short-dated stock alone, with no flag, when no
  replenishment or alternative can be identified.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Confirm a distant-dated order for a shelf-life-constrained customer when only short-dated stock exists
  and no replenishment is scheduled.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q010

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q010
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An order confirmed today against stock that currently satisfies the shelf-life requirement, where the
  requirement is instead evaluated against a distant committed date, is checked against the requirement as
  it will stand at that future date, not only as it stands at confirmation.
WHY_IT_MATTERS: >
  Checking only against today's date approves orders that are already known to fail by the time they
  actually need to ship.
DISCONFIRMING_OBSERVATION: >
  An order with a distant committed date is evaluated against the shelf-life requirement using today's
  date rather than the date the goods must actually still qualify by.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order with a distant committed date against a lot that qualifies today but will not qualify by
  that date, and check which date the evaluation used.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q011

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q011
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether an incoming, not-yet-received replenishment lot may be counted toward satisfying a future order's
  shelf-life requirement, ahead of its own receipt and date being known, is a defined rule, not an unstated
  assumption.
WHY_IT_MATTERS: >
  An unstated assumption about whether unreceived stock counts toward a shelf-life-sensitive promise means
  no one can be sure what a given order is actually covered by.
DISCONFIRMING_OBSERVATION: >
  An incoming, unreceived lot is silently counted, or silently excluded, toward satisfying a shelf-life
  requirement with no configured rule governing which behaviour applies.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a shelf-life-constrained order coverable only by an incoming, not-yet-received lot, and check
  whether and how it is counted.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q012

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q012
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The default removal strategy's shortest-dated-first selection is overridden by a customer's own minimum
  shelf-life requirement when the two would otherwise pick a lot the customer's contract does not accept.
WHY_IT_MATTERS: >
  Fulfilling from the strategy's usual choice regardless of the customer's contract ships stock the
  contract says should not be shipped.
DISCONFIRMING_OBSERVATION: >
  An order for a shelf-life-constrained customer is fulfilled from the shortest-dated lot even though that
  lot fails the customer's requirement and a qualifying alternative exists.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Stock a qualifying longer-dated lot and a shorter-dated lot the strategy would normally pick, then fulfil
  a shelf-life-constrained customer's order and see which lot is used.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q013

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q013
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a customer specifies a longer-dated preference than the default removal strategy would select, and
  a qualifying longer-dated lot exists, the order is fulfilled from that lot rather than the strategy's
  normal shortest-dated choice being forced through anyway.
WHY_IT_MATTERS: >
  A stated preference that is never actually acted on is not a real capability, only a field that is
  stored and ignored.
DISCONFIRMING_OBSERVATION: >
  A customer's stated preference for a longer-dated lot is on file, a qualifying longer-dated lot is in
  stock, yet the order still fulfils from a different, shorter-dated qualifying lot.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Configure a customer preference for longer-dated stock, stock both a preferred and a merely-qualifying
  lot, and fulfil an order to see which is chosen.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q014

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q014
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If no lot meets a customer's stated shelf-life preference at all, the order is flagged for an explicit
  decision rather than the removal strategy silently falling back to its ordinary shortest-dated pick
  regardless of the customer's requirement.
WHY_IT_MATTERS: >
  A silent fallback to a non-qualifying lot defeats the entire purpose of having configured the
  requirement.
DISCONFIRMING_OBSERVATION: >
  When no lot in stock meets a customer's requirement at all, the order still completes fulfilment from a
  non-qualifying lot with no flag or decision point raised.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Ensure no lot in stock meets a customer's requirement, then attempt to fulfil that customer's order and
  observe what happens.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q015

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q015
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reserved lot that still satisfies a customer's shelf-life requirement at the time of reservation, but
  would no longer satisfy it by the time an operational delay pushes back the actual delivery date, is
  re-evaluated against the requirement before dispatch rather than shipped on the strength of its original,
  now-stale qualification.
WHY_IT_MATTERS: >
  Shipping on the strength of a qualification check that is now known to be stale delivers exactly the
  outcome the requirement exists to prevent.
DISCONFIRMING_OBSERVATION: >
  A delayed order dispatches the originally reserved lot with no re-check, even though that lot no longer
  meets the customer's requirement by the actual, delayed delivery date.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve a lot that qualifies for the original delivery date, delay the order past the point that lot
  still qualifies, and check whether dispatch re-verifies it.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q016

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q016
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An operational delay long enough to make the originally reserved lot fall short of the customer's
  requirement surfaces that fact to whoever is responsible for the order, rather than the delay and the
  shelf-life consequence remaining two unconnected facts.
WHY_IT_MATTERS: >
  An unconnected delay and shelf-life consequence means no one is prompted to intervene before a
  non-qualifying shipment goes out.
DISCONFIRMING_OBSERVATION: >
  An operational delay that causes the reserved lot to fall out of qualification produces no visible flag
  connecting the delay to the shelf-life consequence.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Delay a shelf-life-constrained order past its reserved lot's qualifying window and check whether the
  order surfaces the connection.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q017

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q017
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a delayed delivery's original lot no longer qualifies, substituting a different, still-qualifying
  lot for the same order is a distinguishable, traceable substitution rather than an unremarked change to
  what will actually ship.
WHY_IT_MATTERS: >
  An unremarked substitution means no one can later explain why a different lot than originally reserved
  actually shipped.
DISCONFIRMING_OBSERVATION: >
  A lot substituted in place of an originally reserved, now-disqualified lot is not distinguishable in the
  order's record from the lot that was always going to ship.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Force a lot substitution due to a delay-driven disqualification, and check whether the substitution is
  recorded as such.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q018

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q018
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A single order line partially delivered from two lots with different remaining shelf life is recorded so
  that each portion's own date is traceable to the specific portion of the customer's order it was applied
  to.
WHY_IT_MATTERS: >
  Without a per-portion trace, no one can later say which physical goods, with which dates, actually
  reached the customer.
DISCONFIRMING_OBSERVATION: >
  A line delivered partly from two lots with different dates records only one date for the whole delivered
  quantity, with no way to tell which portion came from which lot.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deliver one line using two lots with different dates and inspect what the delivery record shows per
  portion.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q019

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q019
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a customer's minimum-shelf-life requirement applies and a partial delivery would have to draw from
  a lot that fails the requirement to complete the full quantity, the shortfall is handled as an explicit
  exception rather than being silently filled from the disqualified lot.
WHY_IT_MATTERS: >
  Silently filling the last portion of a promise from disqualified stock is precisely the failure a
  shelf-life requirement exists to prevent, made worse by its invisibility.
DISCONFIRMING_OBSERVATION: >
  A partial delivery completes its final portion from a lot that fails the customer's requirement, with no
  exception or flag raised, purely to reach the full ordered quantity.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Set up a delivery where only a non-qualifying lot remains to complete the quantity, and observe whether
  it is used silently or flagged.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q020

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q020
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  What the customer-facing delivery document communicates about shelf life, when an order is split across
  two lots with different dates, reflects both dates rather than presenting a single date that applies to
  only part of the shipped quantity.
WHY_IT_MATTERS: >
  A single date on a document covering two different actual dates misrepresents what the customer is
  receiving.
DISCONFIRMING_OBSERVATION: >
  A customer delivery document for an order split across two lots with different dates shows only one
  date, applied as if it covered the entire shipped quantity.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Deliver a line from two lots with different dates and inspect the resulting customer-facing document.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q021

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q021
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Returned stock that no longer meets any customer's minimum shelf-life requirement, or the business's own
  minimum for resale, is distinguishable in the returned-goods record from stock still fit to be promised
  to a new order.
WHY_IT_MATTERS: >
  Indistinguishable returned stock risks being promised again to a customer whose contract it can no longer
  satisfy.
DISCONFIRMING_OBSERVATION: >
  Returned stock that no longer meets any resale shelf-life threshold looks the same in the record as stock
  still fit to promise.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Return stock whose remaining shelf life is now too short to resell, and compare its record to ordinarily
  returned, still-fit stock.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q022

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q022
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Returned stock does not become available to be promised to a new customer order in the same
  removal-strategy pool as fresh stock without the same shelf-life check any other candidate lot would
  receive.
WHY_IT_MATTERS: >
  Skipping the check for returns specifically reopens exactly the failure mode the requirement exists to
  close, through a different door.
DISCONFIRMING_OBSERVATION: >
  Returned stock becomes available to a new shelf-life-constrained order without that order's requirement
  being checked against it, unlike any other candidate lot.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Return stock and attempt to fulfil a shelf-life-constrained order from the returned quantity, observing
  whether the same check applies.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q023

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q023
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Stock returned in a condition that fails the general resale shelf-life check is routed to an identifiable
  disposition path rather than sitting in ordinary on-hand quantity with no distinguishing marker.
WHY_IT_MATTERS: >
  Undifferentiated on-hand quantity that quietly includes unsellable returned stock overstates what is
  actually available to sell.
DISCONFIRMING_OBSERVATION: >
  Stock returned in a condition that fails the general resale shelf-life check sits in ordinary on-hand
  quantity with no distinguishing marker or routing.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Return stock that fails the general resale shelf-life check and inspect where it lands.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q024

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q024
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The shelf-life date shown on a customer-facing delivery or shipping document matches the actual date
  carried by the lot that physically fulfils that line, not a date computed independently at
  document-generation time.
WHY_IT_MATTERS: >
  A document date that does not match the physical goods misinforms the customer about exactly what a
  shelf-life-sensitive contract is meant to guarantee.
DISCONFIRMING_OBSERVATION: >
  A customer document states a shelf-life date that does not match the lot that actually physically
  fulfilled that line.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Fulfil a line from a specific lot and compare the date on the resulting customer document to that lot's
  actual date.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q025

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q025
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An order fulfilled from a substituted lot, different from the one originally planned, produces a
  customer document that reflects the lot that actually shipped, not the one originally planned.
WHY_IT_MATTERS: >
  A document describing a lot that was never actually shipped is a false record of what the customer
  received.
DISCONFIRMING_OBSERVATION: >
  An order fulfilled from a substituted lot still produces a customer document referencing the originally
  planned lot's date.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Substitute a different lot than originally planned at fulfilment, and check what date the resulting
  customer document shows.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q026

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q026
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A line originally documented against one lot, later partly fulfilled from a different lot for the
  remaining quantity, produces a document correction or supplement rather than leaving the original
  document silently wrong for the substituted portion.
WHY_IT_MATTERS: >
  A document silently wrong for part of what shipped misrepresents that portion to the customer with no
  way to catch the error.
DISCONFIRMING_OBSERVATION: >
  A line originally documented against one lot, later partly fulfilled from a different lot, leaves the
  original document unchanged and uncorrected for the substituted portion.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Generate a customer document against one lot, then fulfil part of the remaining quantity from a different
  lot, and check whether a correction or supplement results.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q027

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q027
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Overriding a shelf-life requirement to allow a sale to proceed against non-qualifying stock is restricted
  to a defined role or permission, and a user lacking it cannot force the same order through the identical
  path.
WHY_IT_MATTERS: >
  An override anyone can invoke defeats the purpose of having a customer-specific requirement at all.
DISCONFIRMING_OBSERVATION: >
  A user without a designated override permission can force a non-qualifying lot through to complete a
  shelf-life-constrained sale via the same path as an authorised user.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Attempt a shelf-life override as a user without the designated permission and as one with it, and compare
  the outcomes.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q028

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q028
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An order completed through a shelf-life override is distinguishable in its own record from an order that
  qualified under the ordinary rule, so a later question about why non-qualifying stock reached a customer
  can be answered from the order itself.
WHY_IT_MATTERS: >
  Without a distinguishing mark, no one reviewing the order later can tell that a non-qualifying shipment
  happened by deliberate exception rather than ordinary process.
DISCONFIRMING_OBSERVATION: >
  An order completed via a shelf-life override looks identical in its own record to one that qualified
  under the ordinary rule.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete one order via override and one via ordinary qualification, and compare their records.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q029

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q029
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  The override action itself, once taken, records who took it and does not merely change the order's
  downstream state with no attributable actor.
WHY_IT_MATTERS: >
  An override with no attributable actor cannot be followed up on or accounted for afterward.
DISCONFIRMING_OBSERVATION: >
  An override changes the order's state with no record of which user performed it or when.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Perform a shelf-life override and inspect whether the actor and time are recorded.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q030

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q030
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A customer-specific shelf-life requirement cannot be silently bypassed by a user simply picking a
  different, unqualified lot manually, without the same override authorization the formal override path
  requires.
WHY_IT_MATTERS: >
  A side door that reaches the same non-qualifying outcome without the formal authorization makes the
  entire override control meaningless.
DISCONFIRMING_OBSERVATION: >
  A user without override permission manually selects a non-qualifying lot for a shelf-life-constrained
  order and the selection is accepted without the same authorization the formal override requires.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user without override permission, attempt to manually select a non-qualifying lot on a
  shelf-life-constrained order.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q031

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q031
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a shelf-life requirement is enforced as a hard block or a soft warning for a given customer is a
  configurable choice, and orders behave consistently with whichever mode is actually configured for that
  customer.
WHY_IT_MATTERS: >
  If actual behaviour does not follow the configured mode, whoever set a hard block believes they have a
  control that is not actually operating as a block.
DISCONFIRMING_OBSERVATION: >
  A customer configured for a hard block still allows the order through with only a warning, or vice versa.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Configure hard-block mode for one customer and warning-only mode for another, and confirm a
  non-qualifying order for each.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q032

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q032
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A shelf-life requirement configured for one company's relationship with a customer does not apply to a
  different company's sales to what is nominally the same customer record in a multi-company structure,
  unless explicitly shared.
WHY_IT_MATTERS: >
  A requirement leaking across company boundaries in a multi-company structure applies a contract term to
  an entity that never agreed to it.
DISCONFIRMING_OBSERVATION: >
  A shelf-life requirement configured for one company's relationship with a customer also blocks or flags
  that customer's orders under a different company, with no explicit sharing configured.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a requirement under one company for a customer that also transacts with a second company in
  the same structure, and check whether the second company's orders are affected.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q033

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q033
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An order line for a product with no shelf-life tracking is never blocked or flagged by a customer's
  shelf-life requirement, regardless of how strict that requirement is configured.
WHY_IT_MATTERS: >
  Applying a shelf-life check to a product that carries no shelf-life data at all can only ever produce a
  meaningless or incorrect result.
DISCONFIRMING_OBSERVATION: >
  An order line for a product with no shelf-life tracking is blocked or flagged by a customer's shelf-life
  requirement.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Configure a strict customer requirement, then order a product for that customer that carries no
  shelf-life tracking at all.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q034

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q034
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An order's own record shows that it was blocked or substituted for shelf-life reasons in enough detail —
  which lot, which date, which requirement — that the decision can be reconstructed without needing a live
  inventory dashboard.
WHY_IT_MATTERS: >
  A decision only explainable by re-running a live query cannot be reconstructed once the underlying stock
  state has moved on.
DISCONFIRMING_OBSERVATION: >
  An order's own record shows that it was blocked or substituted for shelf-life reasons, but not which lot,
  which date, or which requirement was involved.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Trigger a shelf-life block or substitution, then inspect the order's own record after the underlying
  stock state has since changed.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q035

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q035
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A line blocked for lack of a qualifying lot can become fulfillable once a qualifying receipt arrives
  without the order needing to be cancelled and recreated from scratch.
WHY_IT_MATTERS: >
  Requiring an order to be recreated once a qualifying lot appears is unnecessary friction for a situation
  the system already has all the facts to resolve.
DISCONFIRMING_OBSERVATION: >
  A line blocked for lack of a qualifying lot cannot become fulfillable once a qualifying receipt arrives
  without the order being cancelled and recreated.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Block a line for lack of a qualifying lot, receive a new lot that would qualify, and check whether the
  existing line can proceed.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q036

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q036
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A stricter customer's order is not silently served from a lot that would fail that customer's own
  shelf-life requirement merely because the lot was still numerically available in stock.
WHY_IT_MATTERS: >
  Treating numeric availability as sufficient regardless of qualification directly breaks the one guarantee
  the requirement exists to provide.
DISCONFIRMING_OBSERVATION: >
  A stricter customer's order is fulfilled from a lot that numerically exists in enough quantity but fails
  that customer's own shelf-life requirement.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Stock only a lot that fails a strict customer's requirement but is numerically sufficient, and fulfil
  that customer's order.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q037

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q037
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A rush or expedited order for a shelf-life-constrained customer still has the applicable requirement
  checked before dispatch, not skipped because the order took an accelerated fulfilment path.
WHY_IT_MATTERS: >
  An accelerated path that skips the check delivers a faster route to exactly the outcome the requirement
  exists to prevent.
DISCONFIRMING_OBSERVATION: >
  A rush or expedited order for a shelf-life-constrained customer dispatches without the requirement being
  checked, because it took an accelerated fulfilment path.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Place a rush order for a shelf-life-constrained customer against a non-qualifying lot and observe whether
  the requirement is still checked before dispatch.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q038

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q038
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A lot released by a cancelled shelf-life-constrained order returns to the pool of stock eligible for
  other qualifying orders with its shelf-life qualification status preserved, not merely as general on-hand
  with that status lost.
WHY_IT_MATTERS: >
  Losing the lot's qualification status on release could let it be wrongly counted as fit for an order it
  does not actually qualify for.
DISCONFIRMING_OBSERVATION: >
  A lot released by a cancelled shelf-life-constrained order returns to general stock with its shelf-life
  qualification status no longer distinguishable from any other lot.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve a lot against a shelf-life-constrained order, cancel the order, and check whether the lot's
  qualification status is preserved in the pool of stock.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q039

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q039
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A lot that fails a customer's shelf-life requirement for a given committed date is never the lot recorded
  as having fulfilled that specific customer's line for that date.
WHY_IT_MATTERS: >
  A record showing a requirement was met when it was not is a false record precisely where the requirement
  is meant to give assurance.
DISCONFIRMING_OBSERVATION: >
  A shipment record shows a customer line as fulfilled for a committed date using a lot that did not
  actually meet that customer's requirement for that date.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Force a shipment using a non-qualifying lot (via override or otherwise) and inspect what the fulfilment
  record states about whether the requirement was met.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q040

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q040
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A customer's own, stricter shelf-life requirement takes precedence over a looser general company policy
  for the same product; the two do not silently collapse into just whichever one is checked last.
WHY_IT_MATTERS: >
  If the more general rule silently wins, the specific contract term the customer was promised is not the
  one actually enforced.
DISCONFIRMING_OBSERVATION: >
  A customer's own, stricter shelf-life requirement is overridden by a looser general company policy for
  the same product with no indication the specific term was considered.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Configure a stricter customer-specific requirement alongside a looser general policy for the same
  product, and confirm which one governs an order for that customer.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q041

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q041
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A customer's configured shelf-life requirement is actually read and applied at order confirmation, not
  merely stored as reference information with no effect on confirmation behaviour.
WHY_IT_MATTERS: >
  A stored-but-inert setting gives whoever configured it a false sense that the requirement is actually
  being enforced.
DISCONFIRMING_OBSERVATION: >
  A customer's configured shelf-life requirement has no observable effect on order confirmation behaviour
  for that customer.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a customer shelf-life requirement, then confirm an order against non-qualifying stock and check
  whether confirmation behaviour changes at all.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q042

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q042
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A lot verified as qualifying at reservation, but that crosses the requirement's limit before picking
  occurs, is re-verified against the customer's requirement at the picking step rather than being picked
  and shipped on the strength of the earlier check alone.
WHY_IT_MATTERS: >
  A lot that has crossed the limit between reservation and picking, if shipped anyway, delivers the exact
  non-qualifying outcome the check exists to prevent.
DISCONFIRMING_OBSERVATION: >
  A lot verified as qualifying at reservation, but that crosses the requirement's limit before picking, is
  picked and shipped without a second check at that point.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve a qualifying lot, let it cross the requirement's limit before picking occurs, then pick and check
  whether it is re-verified.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q043

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q043
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  The figure used to check a customer's shelf-life requirement at picking is the same figure used at
  reservation for the same order, with no silently different or default value governing the two
  checkpoints.
WHY_IT_MATTERS: >
  Two silently different figures governing the same requirement at two checkpoints means the requirement is
  not actually one consistent rule.
DISCONFIRMING_OBSERVATION: >
  The figure used to check shelf life at picking differs from the figure used at reservation for the same
  order, with no configuration explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enable a picking-stage shelf-life check alongside the reservation-stage check for the same order, and
  compare the requirement figure each one actually used.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q044

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q044
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Changing the general removal-strategy configuration for a product does not cause a stricter
  customer-specific shelf-life requirement to stop being applied to that customer's orders.
WHY_IT_MATTERS: >
  A general configuration change should not silently erase a specific customer's contractual protection.
DISCONFIRMING_OBSERVATION: >
  Changing the general removal-strategy configuration causes a stricter customer-specific requirement to no
  longer be applied to that customer's orders.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change the general removal-strategy configuration for a product, then confirm an order for a customer
  with a stricter specific requirement and check whether it is still applied.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q045

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q045
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When stock is split between a shelf-life-constrained customer's order and an unconstrained customer's
  order, the constrained customer's portion draws only from qualifying lots, while the unconstrained
  customer's portion is not also artificially limited to that same qualifying subset.
WHY_IT_MATTERS: >
  Either failure direction — the constrained customer getting non-qualifying stock, or the unconstrained
  customer being needlessly starved — is an incorrect allocation.
DISCONFIRMING_OBSERVATION: >
  The constrained customer's portion draws from a non-qualifying lot, or the unconstrained customer's
  portion is refused stock that only fails to qualify for the other customer.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Split available stock, some qualifying and some not, between orders for a constrained and an unconstrained
  customer, and check what each actually receives.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q046

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q046
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A compliance or month-end report covering a period's shipments provides a way to identify which of them
  went out under a shelf-life override, rather than an override shipment being indistinguishable from an
  ordinary one in that report.
WHY_IT_MATTERS: >
  An override indistinguishable in later reporting prevents anyone from tracking how often, and for whom,
  the shelf-life requirement was set aside.
DISCONFIRMING_OBSERVATION: >
  A compliance or month-end report covering shipments gives no way to identify which ones went out under a
  shelf-life override.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Ship at least one order under override and one under the ordinary rule, then inspect what a period-level
  report shows about each.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q047

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q047
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A user permitted to approve a shelf-life override for their own team's orders cannot also approve the
  same override on an order belonging to a different team or company without a separate grant.
WHY_IT_MATTERS: >
  Authority to override for one's own team should not silently extend to orders that authority was never
  granted over.
DISCONFIRMING_OBSERVATION: >
  A user permitted to approve a shelf-life override for their own team's orders can also approve the same
  override on an order belonging to a different team or company with no separate grant.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with override approval scoped to one team, attempt to approve an override on an order belonging
  to a different team or company.
```

## G08-SALE_STOCK_PRODUCT_EXPIRY-Q048

```yaml
QID: G08-SALE_STOCK_PRODUCT_EXPIRY-Q048
MODULE: sale_stock_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Whatever mechanism enforces a customer's shelf-life requirement at order time is the same mechanism whose
  outcome actually determines which lot ships — a requirement that is checked but has no bearing on the
  lot picked is not a real enforcement of the requirement.
WHY_IT_MATTERS: >
  A requirement that is checked but has no effect on which lot is actually picked is a check that exists on
  paper only.
DISCONFIRMING_OBSERVATION: >
  An order's record shows the shelf-life requirement was checked and passed or failed, but the lot actually
  picked and shipped was chosen independently of that outcome.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trace a shelf-life-constrained order from its confirmation-time check through to the lot actually picked
  and shipped, and verify the outcome of the check determined that choice.
```

---
## GMVQ Internal QA Checklist

- [x] 48 distinct MVQ records; no padding — every record targets a distinct hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`.
- [x] Questions are behavioral and source-neutral; no vendor/product name, technical identifier, or module
      name appears in question text.
- [x] Bridge-of-a-bridge seam test applied to every question: removing the customer promise leaves plain
      shelf-life mechanics (not this bank's ground); removing the shelf-life fact leaves the plain
      commercial-to-movement seam (not this bank's ground either). Every surviving question needs both.
- [x] Customer contract minimum remaining shelf life at delivery, and a promise not meeting it, represented
      (Q001-Q005).
- [x] Availability counted including units that will expire before the committed date represented
      (Q006-Q008).
- [x] Long-dated order confirmed against short-dated stock represented (Q009-Q011).
- [x] Removal strategy's shortest-dated default vs a customer-specified preference represented
      (Q012-Q014).
- [x] Delivery delayed until the reserved lot is no longer acceptable represented (Q015-Q017).
- [x] Partial delivery from two lots with different dates, and what the customer is told, represented
      (Q018-Q020).
- [x] Return of stock whose remaining life is now too short to resell represented (Q021-Q023).
- [x] Expiry date printed on the customer document vs the one shipped represented (Q024-Q026).
- [x] Who may override a shelf-life rule to complete a sale, and what trace it leaves, represented
      (Q027-Q030).
- [x] Configuration dependency and reachability represented (Q031, Q040, Q041, Q043, Q044).
- [x] Tenant/company boundary represented (Q032, Q047).
- [x] Cross-module dependency / negative case (non-tracked product) represented (Q033).
- [x] Auditability represented (Q034, Q046).
- [x] State transition (blocked line becoming fulfillable) represented (Q035).
- [x] Concurrency / allocation across competing customers represented (Q036, Q045).
- [x] Runtime reachability (re-check at picking, not only at reservation) represented (Q042).
- [x] Source/runtime contradiction potential represented (Q043, Q048).
- [x] No specific Thai legal or tax requirement asserted anywhere in this bank.
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT

