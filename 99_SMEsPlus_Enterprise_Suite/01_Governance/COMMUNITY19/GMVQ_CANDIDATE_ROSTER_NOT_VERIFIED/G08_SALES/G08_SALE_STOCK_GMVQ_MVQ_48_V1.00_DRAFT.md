# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_stock Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-SALE_STOCK-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_stock`
**Wave:** W2
**Author Cell:** TEAM P-S5 (GMVQ Question Factory — Production Cell P-S5, Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This module is the seam by which a commercial order becomes an outbound stock movement, and the point
at which a promise is made to a customer that inventory must actually be able to keep. Available-to-promise
is the heart of this bank: what the order says it can deliver versus what is actually free to promise, and
what happens when two commercial commitments compete for the same physical unit. This bank supplements the
55 Standard Questions with module-specific, adversarial questions covering: two orders promising the same
unit; the promise made at quotation versus honoured or not at confirmation; reservation created at
confirmation versus at a later scheduling step, and what (if anything) holds goods in between; a committed
date derived from availability that then changes; a line quantity increased after part was already shipped;
an order cancelled after reservation but before dispatch, and what releases; partial delivery and the
remainder's promise; delivery from a different warehouse or company than the order's; the order's unit
versus the movement's unit; a return creating an inbound movement against a sold line; invoicing policy
keyed to delivered quantity and a movement later corrected; and an order shipped complete but invoiced
partially, or the reverse.

Per the Bridge Module Rule (V1.00), this module owns almost no behaviour of its own: every question below
targets a point where the commercial commitment and the physical movement could legitimately disagree, not
a restatement of the commercial order's own pricing/terms behaviour (which belongs to the base `sale`
module) or of stock reservation/valuation mechanics taken alone (which belong to G05 INVENTORY). The
removal test was applied to every question: if it would still make sense with the commercial order and the
stock movement used entirely apart from each other, it was cut. Question text is source-neutral: no vendor
or product name, no technical identifier (model, table, field, method, XML ID, API path), and no reference
to how any specific implementation is built. Language is generic business/behavioural language throughout.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, cross-module dependency, optional behaviour, auditability,
  tenant/company boundary, concurrency and ordering, and runtime/configuration reachability.
- This module carries both a configuration layer (whether confirmation ahead of availability is permitted,
  where in the lifecycle reservation occurs, how available-to-promise itself is defined, partial-delivery
  policy) and a runtime process layer (what happens at and after confirmation, delivery and invoicing);
  each question is tagged `LAYER: BASE` or `LAYER: PROCESS` accordingly.
- Pre-authoring sibling check (Bridge Module Rule §5): `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G05_INVENTORY/G05_STOCK_GMVQ*.md 01_QUESTION_BANKS/G05_INVENTORY/G05_PRODUCT_EXPIRY*.md 01_QUESTION_BANKS/G05_INVENTORY/G05_STOCK_DELIVERY*.md` and
  `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G08_SALES/*.md` were both run before authoring. G05_STOCK's 64
  hypotheses cover reservation/claim mechanics, valuation, cost layers, negative on-hand, batch/serial
  identity and multi-step routes entirely inside the warehouse — none of them require a commercial order to
  exist. G05_STOCK_DELIVERY's 48 cover the carrier/shipping-cost seam. G05_PRODUCT_EXPIRY's 48 cover
  shelf-life mechanics with no customer promise involved. No G08 SALES bank existed on disk at authoring
  time. This bank restates none of that ground: every hypothesis below requires BOTH a commercial commitment
  and a physical movement to exist together, which is why it belongs here and not in either sibling group.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a
  Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_STOCK-Q001

```yaml
QID: G08-SALE_STOCK-Q001
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When two separate orders are confirmed for the same product and their combined promised quantity
  exceeds what is actually free to promise, the second confirmation to complete surfaces the shortfall
  rather than both orders showing as fully covered.
WHY_IT_MATTERS: >
  Two orders both believing they are covered for a unit that exists once is the direct cause of a broken
  promise to a customer, discovered only when the shortage becomes physical.
DISCONFIRMING_OBSERVATION: >
  Both orders' outstanding quantity independently displays as fully available and covered when only one
  product unit actually exists to satisfy them.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Reduce a product's free stock to a small quantity, confirm two separate orders whose combined line
  quantity exceeds it in quick succession, then inspect what each order reports as its promise status.
```

## G08-SALE_STOCK-Q002

```yaml
QID: G08-SALE_STOCK-Q002
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The quantity presented as available to promise for a product subtracts quantity already committed to
  other confirmed orders from on-hand, rather than presenting raw on-hand quantity as if none of it were
  already spoken for.
WHY_IT_MATTERS: >
  Quoting from raw on-hand quantity manufactures a promise that cannot be kept at the exact moment a
  commitment is made to a customer.
DISCONFIRMING_OBSERVATION: >
  A product already fully committed to other confirmed orders still displays as available in the same
  quantity as its raw on-hand figure.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Confirm an order that reserves all of a product's on-hand quantity, then check what a second, unrelated
  order sees as available for the same product.
```

## G08-SALE_STOCK-Q003

```yaml
QID: G08-SALE_STOCK-Q003
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When an already-reserved order line is edited without changing its quantity, the availability check
  performed as part of the edit does not treat the line's own existing reservation as competing demand
  against itself.
WHY_IT_MATTERS: >
  Self-competition on edit would make an already-covered order intermittently appear short of stock for
  no operational reason, undermining trust in the figure shown.
DISCONFIRMING_OBSERVATION: >
  Making an unrelated edit to an order line that already holds a full reservation causes its
  available-to-promise figure to drop as though its own reserved quantity were now competing against
  itself.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm and fully reserve an order line, then make an edit to the line that does not change quantity,
  and re-check the availability figure shown for that line and product.
```

## G08-SALE_STOCK-Q004

```yaml
QID: G08-SALE_STOCK-Q004
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Producing a quotation for a product does not itself place a hold on stock; a different order can still
  take the same quantity before this quotation is confirmed.
WHY_IT_MATTERS: >
  If quoting silently held stock, unconfirmed exploratory quotations would starve real, confirmed demand
  of inventory that was never actually promised.
DISCONFIRMING_OBSERVATION: >
  A quotation, while still unconfirmed, prevents a separate confirmed order from being able to claim the
  same on-hand quantity.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a quotation for a product's full available quantity without confirming it, then attempt to
  confirm a separate order for the same quantity of the same product.
```

## G08-SALE_STOCK-Q005

```yaml
QID: G08-SALE_STOCK-Q005
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The commitment date carried on a quotation is re-evaluated against current availability at the moment
  the order is confirmed, rather than being carried unchanged from whatever was true when the quotation
  was drafted.
WHY_IT_MATTERS: >
  A stale commitment date confirmed unchanged after availability worsened is a promise to the customer
  that was already false the moment it was made.
DISCONFIRMING_OBSERVATION: >
  Availability materially worsens between quoting and confirming, yet the confirmed order's commitment
  date remains exactly what the quotation showed, with no recalculation or flag.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Quote an order with a given commitment date, deliberately consume the underlying stock through an
  unrelated order, then confirm the original order and inspect its commitment date.
```

## G08-SALE_STOCK-Q006

```yaml
QID: G08-SALE_STOCK-Q006
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An order confirmed while its promised quantity is not fully covered by available stock is recorded as
  confirmed-but-short, a state distinguishable from confirmed-and-fully-covered, rather than the two
  being indistinguishable once confirmation succeeds.
WHY_IT_MATTERS: >
  If a shortfall is invisible after confirmation, no one downstream knows to expedite, communicate a
  delay, or watch the order until the true state becomes apparent as a stockout.
DISCONFIRMING_OBSERVATION: >
  A short order and a fully-covered order are indistinguishable in their confirmed state once both have
  gone through confirmation.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Confirm one order fully covered by stock and one order exceeding available stock for the same product,
  then compare what each order's record shows.
```

## G08-SALE_STOCK-Q007

```yaml
QID: G08-SALE_STOCK-Q007
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A change to an order's commitment date, whether recalculated automatically or overridden manually,
  leaves a visible record distinguishing the new date from the one it replaced.
WHY_IT_MATTERS: >
  Without a visible before/after, a customer complaint about a broken delivery promise cannot be checked
  against what was actually committed and when it changed.
DISCONFIRMING_OBSERVATION: >
  An order's commitment date changes between two points in time with no trace of the earlier value or of
  what caused the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Force a recalculation of an order's commitment date by changing underlying availability, then inspect
  whether the prior date is still recoverable.
```

## G08-SALE_STOCK-Q008

```yaml
QID: G08-SALE_STOCK-Q008
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A commitment date manually overridden by a user is preserved through the next automatic availability
  re-evaluation rather than being silently recalculated back to a system-derived value.
WHY_IT_MATTERS: >
  A manual override exists specifically to reflect a business decision outside the automatic rule; losing
  it silently reintroduces the exact promise the override was meant to correct.
DISCONFIRMING_OBSERVATION: >
  A manually set commitment date reverts to a system-computed value the next time availability is
  re-evaluated, with no user action requesting that change.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Manually override an order's commitment date, then trigger a routine availability re-evaluation (such
  as an unrelated stock movement) and re-check the date.
```

## G08-SALE_STOCK-Q009

```yaml
QID: G08-SALE_STOCK-Q009
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether physical stock is reserved at order confirmation or at a later scheduling step is a single,
  consistently applied point for a given configuration, not a choice that varies unpredictably order to
  order under the same setup.
WHY_IT_MATTERS: >
  An unpredictable reservation point makes available-to-promise figures untrustworthy, since no one can
  say from the order alone whether its stock is actually held yet.
DISCONFIRMING_OBSERVATION: >
  Two orders confirmed under identical configuration and timing reserve stock at two different lifecycle
  points with no configuration difference explaining why.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm two comparable orders for the same product under one fixed reservation-timing configuration and
  compare the lifecycle point at which each one's reservation actually appears.
```

## G08-SALE_STOCK-Q010

```yaml
QID: G08-SALE_STOCK-Q010
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When reservation is a later step than confirmation, a second order confirmed in that gap can
  legitimately claim the same unit ahead of the first; the first order confirming earlier does not itself
  guarantee it the unit.
WHY_IT_MATTERS: >
  If confirmation order silently guaranteed a claim regardless of the reservation gap, a scheduling step
  would be running on stale assumptions about what stock is actually still free.
DISCONFIRMING_OBSERVATION: >
  The first-confirmed order is shown as covered throughout the gap even though a later reservation step
  actually assigns the unit to the second order instead.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure reservation to occur at scheduling rather than confirmation, confirm two competing orders for
  a scarce product before either is scheduled, then run scheduling and inspect which order actually holds
  the unit.
```

## G08-SALE_STOCK-Q011

```yaml
QID: G08-SALE_STOCK-Q011
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An order edited after confirmation but before its reservation is created is checked against current
  availability at the time reservation actually happens, not against availability as it stood at
  confirmation.
WHY_IT_MATTERS: >
  Reserving against stale availability data can silently assign stock that has since been claimed by
  something else, creating a hidden double-commitment.
DISCONFIRMING_OBSERVATION: >
  An order's reservation is created using an availability snapshot taken at confirmation time, ignoring
  stock movements that occurred in the meantime.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order without immediate reservation, deliberately change on-hand quantity for the product,
  then let reservation occur and inspect which availability figure it used.
```

## G08-SALE_STOCK-Q012

```yaml
QID: G08-SALE_STOCK-Q012
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Increasing a line's ordered quantity after part of it has already shipped creates an outstanding
  requirement only for the newly added amount, without re-running an availability check or reservation
  against the quantity that has already physically left.
WHY_IT_MATTERS: >
  Re-checking already-shipped quantity against current stock would produce a nonsensical shortfall
  against goods that are already gone, and could block or corrupt a legitimate order.
DISCONFIRMING_OBSERVATION: >
  Increasing quantity on a partially shipped line triggers an availability recheck that includes the
  portion already shipped, producing a shortfall against stock that has already left.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Partially deliver a line, then increase its ordered quantity and inspect what outstanding quantity and
  availability check result from the change.
```

## G08-SALE_STOCK-Q013

```yaml
QID: G08-SALE_STOCK-Q013
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Reducing a line's ordered quantity to below the quantity already delivered against it is rejected or
  produces an explicit exception, rather than silently leaving the line with a negative outstanding
  quantity.
WHY_IT_MATTERS: >
  A negative outstanding quantity is a state nothing downstream is built to interpret correctly, and it
  corrupts any report that sums outstanding quantity across orders.
DISCONFIRMING_OBSERVATION: >
  A line's ordered quantity is reduced below what has already been delivered, and the order accepts the
  change while showing a negative or nonsensical outstanding quantity with no warning.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Partially deliver a line, then attempt to reduce the line's ordered quantity to less than the delivered
  amount.
```

## G08-SALE_STOCK-Q014

```yaml
QID: G08-SALE_STOCK-Q014
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Increasing a line's quantity after partial delivery does not change the commitment date already
  associated with the portion that has already been delivered; only the newly added, undelivered quantity
  carries a date subject to fresh calculation.
WHY_IT_MATTERS: >
  Rewriting history for an already-fulfilled portion of a promise makes it impossible to tell afterward
  whether the original commitment was actually met on time.
DISCONFIRMING_OBSERVATION: >
  Increasing a line's quantity after partial delivery changes the commitment date attributed to the
  already-delivered portion of that same line.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Partially deliver a line against a recorded commitment date, increase the line's quantity, and check
  whether the original delivered portion's commitment date changed.
```

## G08-SALE_STOCK-Q015

```yaml
QID: G08-SALE_STOCK-Q015
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a confirmed order that already holds a reservation, before any physical picking has begun,
  releases the reserved quantity so that it becomes visible as available to a different demand.
WHY_IT_MATTERS: >
  A reservation that survives its own order's cancellation quietly locks up stock indefinitely,
  understating what is actually free without any order left to explain why.
DISCONFIRMING_OBSERVATION: >
  A cancelled order's reserved quantity remains unavailable to other demand even though no order still
  claims it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm and reserve an order line, cancel the order before picking starts, then check whether the
  quantity is now visible as available elsewhere.
```

## G08-SALE_STOCK-Q016

```yaml
QID: G08-SALE_STOCK-Q016
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling only some lines of a multi-line order releases the reservation held for those specific lines
  without disturbing the reservation still held for the lines that remain active.
WHY_IT_MATTERS: >
  An all-or-nothing release on partial cancellation would either strand active lines without stock or
  wrongly keep cancelled lines' stock locked up.
DISCONFIRMING_OBSERVATION: >
  Cancelling one line of a multi-line order releases or disturbs the reservation belonging to a different,
  still-active line on the same order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm and reserve a multi-line order, cancel one line only, and check the reservation state of both
  the cancelled and the remaining lines.
```

## G08-SALE_STOCK-Q017

```yaml
QID: G08-SALE_STOCK-Q017
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Attempting an ordinary cancellation on an order whose fulfilment has already begun physical picking is
  either blocked or routed through an explicit reversal path, rather than silently deleting the
  commercial order while the physical movement continues unattached.
WHY_IT_MATTERS: >
  An orphaned physical movement with no commercial order behind it cannot be invoiced, reconciled, or
  explained to a customer who asks what happened to their order.
DISCONFIRMING_OBSERVATION: >
  An order with picking already in progress can be ordinarily cancelled with no warning, leaving an active
  physical movement referencing an order that no longer exists.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Confirm an order, begin picking its fulfilment, then attempt an ordinary cancellation of the order and
  observe what happens to both the order and the in-progress movement.
```

## G08-SALE_STOCK-Q018

```yaml
QID: G08-SALE_STOCK-Q018
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Delivering only part of a line's quantity leaves the undelivered remainder tracked as a distinct
  outstanding promise against that same line, rather than the line being marked complete once any
  delivery occurs.
WHY_IT_MATTERS: >
  If a line is treated as fulfilled the moment any quantity moves, the still-owed remainder disappears
  from anyone's view of what is left to deliver.
DISCONFIRMING_OBSERVATION: >
  A line with a partial delivery recorded shows the same delivered state as a line that was delivered in
  full.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Deliver less than the full ordered quantity of a line, then inspect what the line reports as delivered
  versus outstanding.
```

## G08-SALE_STOCK-Q019

```yaml
QID: G08-SALE_STOCK-Q019
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The commitment date attached to the undelivered remainder of a partially delivered line is
  independently re-evaluated against current availability, rather than simply inherited unchanged from
  the date originally set for the full line quantity.
WHY_IT_MATTERS: >
  An unrevised date on the remainder can promise a delivery time that no longer reflects what is actually
  achievable for the outstanding quantity.
DISCONFIRMING_OBSERVATION: >
  The remainder of a partially delivered line keeps exactly the original full-line commitment date even
  though availability for the remaining quantity has since changed materially.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Partially deliver a line, change availability for the remaining quantity, and check whether the
  remainder's commitment date was re-evaluated.
```

## G08-SALE_STOCK-Q020

```yaml
QID: G08-SALE_STOCK-Q020
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling the undelivered remainder of a partially delivered line leaves the record of what was
  actually delivered intact and clearly distinguishable from the withdrawn, cancelled portion.
WHY_IT_MATTERS: >
  Losing the delivered-portion record on cancellation would make it impossible to reconcile what a
  customer actually received against what they were later told was cancelled.
DISCONFIRMING_OBSERVATION: >
  Cancelling the remainder of a partially delivered line also erases or obscures the record of the
  quantity that was already delivered.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Partially deliver a line, cancel the outstanding remainder, and inspect whether the already-delivered
  quantity is still visibly recorded.
```

## G08-SALE_STOCK-Q021

```yaml
QID: G08-SALE_STOCK-Q021
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  When an order is ultimately fulfilled from a warehouse different from the one its availability was
  originally assessed against, the movement record identifies the actual fulfilling warehouse
  distinguishably from the one referenced at confirmation.
WHY_IT_MATTERS: >
  If the two are conflated, no one can later tell whether the original promise was actually honoured from
  the location it claimed to be covered from.
DISCONFIRMING_OBSERVATION: >
  An order fulfilled from a different warehouse than the one used for its original availability check
  shows only the original warehouse on the resulting movement, with no trace of the actual source.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order against one warehouse's availability, then route its fulfilment through a different
  warehouse and inspect what the resulting movement records as its source.
```

## G08-SALE_STOCK-Q022

```yaml
QID: G08-SALE_STOCK-Q022
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  When a commercial order belonging to one company is fulfilled through a delivery routed via a different
  company's warehouse, the resulting movement and any accounting consequence remain traceable back to the
  original order and correctly attributed across the company boundary, rather than the movement appearing
  to belong solely to the fulfilling company with no link back.
WHY_IT_MATTERS: >
  An untraceable cross-company fulfilment breaks intercompany accounting and hides which entity is
  actually responsible for satisfying the customer's order.
DISCONFIRMING_OBSERVATION: >
  A delivery fulfilled through a different company's warehouse than the order's own company shows no
  reference back to the original order or its owning company.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Confirm an order under one company, fulfil it through a warehouse belonging to a different company in
  the same multi-company structure, and trace the resulting movement back to the order.
```

## G08-SALE_STOCK-Q023

```yaml
QID: G08-SALE_STOCK-Q023
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Changing the warehouse assigned to fulfil an order after confirmation triggers a fresh availability
  check at the newly assigned warehouse, rather than carrying forward the coverage conclusion reached for
  the original warehouse.
WHY_IT_MATTERS: >
  Assuming coverage transfers automatically to a new warehouse can promise stock that was never actually
  verified to exist there.
DISCONFIRMING_OBSERVATION: >
  Reassigning an order's fulfilling warehouse leaves the order marked fully covered with no fresh check
  performed against the new warehouse's own stock.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order covered at one warehouse, reassign its fulfilling warehouse to one with different stock
  levels, and check whether coverage was re-evaluated.
```

## G08-SALE_STOCK-Q024

```yaml
QID: G08-SALE_STOCK-Q024
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When an order line's commercial unit differs from the unit its outbound movement is recorded in, the
  conversion factor applied to compute delivered quantity is the same factor that invoicing policy
  subsequently reads, rather than the sales side and the delivery side maintaining two independently
  rounded conversions.
WHY_IT_MATTERS: >
  Two disagreeing conversions between the same two units can make delivered and invoiced quantity
  permanently unreconcilable for that line.
DISCONFIRMING_OBSERVATION: >
  The delivered quantity computed on the order's commercial unit and the quantity recorded on the
  movement, converted back, disagree by more than a rounding difference explainable by a single shared
  conversion factor.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set up an order line whose commercial unit differs from its movement's recording unit, deliver it, and
  compare the delivered quantity in each unit against a single conversion factor.
```

## G08-SALE_STOCK-Q025

```yaml
QID: G08-SALE_STOCK-Q025
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Repeated partial deliveries of a line recorded in a different unit than the order's commercial unit
  accumulate to the same total, within the same rounding tolerance, as a single delivery of the
  equivalent full quantity would.
WHY_IT_MATTERS: >
  Small rounding losses on every partial delivery compound silently across many transactions and
  eventually produce a delivered total that cannot match what was ordered.
DISCONFIRMING_OBSERVATION: >
  Several partial deliveries of a line converted through a differing unit sum to a materially different
  total than one delivery of the same overall quantity would produce.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Deliver the same total line quantity once as a single movement and once as several partial movements,
  both through a unit conversion, and compare the two resulting totals.
```

## G08-SALE_STOCK-Q026

```yaml
QID: G08-SALE_STOCK-Q026
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A return of previously delivered goods creates an inbound movement linked back to the specific order
  line it was originally sold on, so the line's net delivered quantity reflects the return.
WHY_IT_MATTERS: >
  An unlinked return leaves the original line permanently overstating what the customer actually kept,
  corrupting any later reconciliation or reorder decision.
DISCONFIRMING_OBSERVATION: >
  A processed return creates an inbound movement with no traceable link back to the order line the goods
  were originally sold against.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deliver a line in full, process a return of part of that quantity, and check whether the line's net
  delivered figure and the return movement reference each other.
```

## G08-SALE_STOCK-Q027

```yaml
QID: G08-SALE_STOCK-Q027
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a return reduces net delivered quantity below what has already been invoiced under a
  delivered-quantity invoicing policy, the resulting mismatch is surfaced as an identifiable adjustment
  requirement rather than being silently absorbed into the existing invoice with no record of the
  discrepancy.
WHY_IT_MATTERS: >
  A silently absorbed overinvoice leaves the business having billed for goods it no longer holds evidence
  of having delivered, with no trace of when or why.
DISCONFIRMING_OBSERVATION: >
  A return that drops net delivered quantity below the already-invoiced quantity produces no visible flag,
  credit requirement, or discrepancy record anywhere on the order.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Deliver and fully invoice a line under a delivered-quantity policy, then return part of the delivered
  quantity and inspect what the order shows about the resulting mismatch.
```

## G08-SALE_STOCK-Q028

```yaml
QID: G08-SALE_STOCK-Q028
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Processing a return against a line that has already been invoiced in full is handled through an
  identifiable exception path distinct from an ordinary new delivery, rather than being folded silently
  into whatever unrelated delivery happens to be recorded next.
WHY_IT_MATTERS: >
  A return hidden inside an unrelated delivery record makes it impossible to later separate what shipped
  for this order from what came back for a different reason.
DISCONFIRMING_OBSERVATION: >
  A return recorded against a fully invoiced line appears indistinguishable from an ordinary forward
  delivery on the same line, with no marker that it was a return.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Fully deliver and invoice a line, then process a return against it and inspect how the return is
  represented relative to ordinary deliveries.
```

## G08-SALE_STOCK-Q029

```yaml
QID: G08-SALE_STOCK-Q029
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Under an invoicing policy keyed to delivered quantity, a correction made to a recorded delivery before
  invoicing has occurred is reflected in the quantity that invoicing subsequently reads, so the invoice is
  based on the corrected, not the original, delivered figure.
WHY_IT_MATTERS: >
  Invoicing off a stale, pre-correction figure bills the customer for a quantity known at the time of
  invoicing to be wrong.
DISCONFIRMING_OBSERVATION: >
  A delivery correction made before invoicing has no effect on the delivered quantity that the subsequent
  invoice is actually generated against.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a delivery, correct its quantity before invoicing occurs, then generate the invoice and check
  which figure it used.
```

## G08-SALE_STOCK-Q030

```yaml
QID: G08-SALE_STOCK-Q030
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Correcting a previously recorded delivery after an invoice has already been issued based on the
  original, uncorrected figure produces a distinguishable adjustment record rather than silently altering
  the already-issued invoice.
WHY_IT_MATTERS: >
  Silently rewriting an issued invoice destroys the ability to know what the customer was actually billed
  and when, and can misstate a period already closed for reporting.
DISCONFIRMING_OBSERVATION: >
  Correcting a delivery after invoicing changes the content of the already-issued invoice directly, with
  no separate adjustment record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Deliver, invoice based on the delivered figure, then correct the underlying delivery record and inspect
  what happens to the existing invoice versus what new record, if any, is created.
```

## G08-SALE_STOCK-Q031

```yaml
QID: G08-SALE_STOCK-Q031
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An order line delivered in full but invoiced only in part retains a clear, traceable record of the
  still-uninvoiced delivered quantity, distinguishable from a line that has not been delivered at all.
WHY_IT_MATTERS: >
  If the two look the same, a billing sweep cannot tell already-shipped-still-owed apart from
  not-shipped-yet, and revenue that should be billed goes uncaptured.
DISCONFIRMING_OBSERVATION: >
  A fully delivered, partially invoiced line and an entirely undelivered line present the same
  outstanding-to-invoice figure with no way to tell delivered status apart.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Fully deliver a line, invoice only part of it, and compare its record against a comparable line that has
  not been delivered at all.
```

## G08-SALE_STOCK-Q032

```yaml
QID: G08-SALE_STOCK-Q032
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Under an ordered-quantity invoicing policy, invoicing the full ordered quantity before physical delivery
  is complete leaves a traceable, queryable gap between invoiced and delivered quantity, rather than the
  two figures being presented as if they were the same event.
WHY_IT_MATTERS: >
  Without a visible gap, no one can identify revenue billed ahead of fulfilment, which matters for both
  customer risk and revenue recognition timing.
DISCONFIRMING_OBSERVATION: >
  A line invoiced in full under an ordered-quantity policy, ahead of any delivery, shows delivered
  quantity as equal to invoiced quantity with no way to see the shortfall.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Invoice a line in full under an ordered-quantity policy before delivering any of it, and inspect what
  the line reports as delivered versus invoiced.
```

## G08-SALE_STOCK-Q033

```yaml
QID: G08-SALE_STOCK-Q033
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Changing the invoicing policy on an order line after partial delivery and partial invoicing already
  exist under the prior policy does not retroactively alter what has already been invoiced under that
  prior policy.
WHY_IT_MATTERS: >
  Retroactively rewriting settled invoicing history on a policy change can silently change amounts already
  billed to a customer or already reported for a closed period.
DISCONFIRMING_OBSERVATION: >
  Switching an order line's invoicing policy after partial invoicing already exists changes the previously
  invoiced amount or quantity without a new, separate transaction causing that change.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially deliver and invoice a line under one invoicing policy, then change the line's invoicing policy
  and inspect whether the existing invoiced record was altered.
```

## G08-SALE_STOCK-Q034

```yaml
QID: G08-SALE_STOCK-Q034
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A role without broad inventory visibility can still see enough of a product's available-to-promise
  figure to know whether a new order can be honoured, without necessarily being able to see the identity
  of the other orders competing for that same stock.
WHY_IT_MATTERS: >
  If promise visibility requires full inventory access, sales staff must either be over-permissioned or
  make promises blind to whether they can actually be kept.
DISCONFIRMING_OBSERVATION: >
  A role without inventory-module permission sees no usable available-to-promise figure at all when
  creating an order, or conversely can freely browse the competing orders' own details.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  As a role scoped to sales only, attempt to view a product's available-to-promise figure while creating
  an order, and separately attempt to view the specific competing orders behind that figure.
```

## G08-SALE_STOCK-Q035

```yaml
QID: G08-SALE_STOCK-Q035
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether an order is permitted to be confirmed when it is not fully covered by available stock is
  governed by an explicit, configurable business rule, and the order's actual behaviour follows whatever
  that configuration currently states rather than a fixed assumption built into confirmation regardless of
  setting.
WHY_IT_MATTERS: >
  If the real behaviour ignores the configured setting, whoever configured it believes they have a control
  that does not actually operate.
DISCONFIRMING_OBSERVATION: >
  An order confirms, or is blocked, the same way regardless of how the relevant configuration setting is
  set.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Set the configuration to disallow confirming uncovered orders, attempt to confirm one anyway, then
  reverse the setting and repeat.
```

## G08-SALE_STOCK-Q036

```yaml
QID: G08-SALE_STOCK-Q036
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a scarce unit's claim moves automatically from one order to another because the first order's hold
  was released or overridden, the record identifies both which order lost the unit and which order gained
  it.
WHY_IT_MATTERS: >
  Without both sides of the movement recorded, a customer complaint about a broken promise cannot be
  traced to the specific competing order that took the unit instead.
DISCONFIRMING_OBSERVATION: >
  A unit's claim moves from one order to another with only the gaining order's new reservation visible and
  no trace of which order previously held it.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Create a situation where one order's reservation is released and immediately claimed by a second,
  competing order, then inspect the audit trail for both orders.
```

## G08-SALE_STOCK-Q037

```yaml
QID: G08-SALE_STOCK-Q037
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  An order line for a product that is not tracked for on-hand quantity at all (a service or non-stocked
  item) does not generate an availability check or a reservation, and its presence on an order does not
  block confirmation because of an unrelated line's stock shortfall.
WHY_IT_MATTERS: >
  Forcing a non-stocked line through inventory logic it has no relationship to can incorrectly block or
  delay orders that have no real stock dependency at all.
DISCONFIRMING_OBSERVATION: >
  A non-stocked line generates a reservation or availability check, or a stock shortfall on an unrelated
  stocked line prevents a non-stocked line from proceeding on its own.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Place an order combining a non-stocked line with a separately shortfall-affected stocked line, and
  observe whether the non-stocked line is affected by the stocked line's shortage.
```

## G08-SALE_STOCK-Q038

```yaml
QID: G08-SALE_STOCK-Q038
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An order that was confirmed and fully reserved, then has that reservation forcibly released by an
  unrelated inventory action such as a manual stock correction, surfaces the resulting loss of coverage on
  the order rather than the order continuing to display as fully promised.
WHY_IT_MATTERS: >
  An order silently believed to be covered when it no longer is will not be flagged for expediting until a
  customer discovers the shortfall themselves.
DISCONFIRMING_OBSERVATION: >
  An order whose reservation was forcibly released by an unrelated action continues to display as fully
  covered with no visible change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm and reserve an order, then force a release of that reservation through an unrelated inventory
  correction, and check what the order now shows.
```

## G08-SALE_STOCK-Q039

```yaml
QID: G08-SALE_STOCK-Q039
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When an inbound receipt that would satisfy a backordered promise and a newly confirmed competing order
  for the same product arrive at effectively the same time, which one is served is decided by a defined,
  deterministic rule rather than by processing order that happens to occur first.
WHY_IT_MATTERS: >
  A race-determined outcome for who gets the next unit of stock is impossible to explain to whichever
  customer loses, and impossible to reproduce when investigated afterward.
DISCONFIRMING_OBSERVATION: >
  Repeating the same near-simultaneous receipt-and-confirmation scenario produces different winners with
  no identifiable rule explaining the difference.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Arrange a backordered order and a receipt that covers it to occur at effectively the same time as a new
  competing order confirmation, and inspect which is served and why.
```

## G08-SALE_STOCK-Q040

```yaml
QID: G08-SALE_STOCK-Q040
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Reopening or reactivating a previously cancelled order line, where the workflow permits it, re-runs the
  availability and reservation logic against current stock rather than restoring whatever reservation
  state the line held before it was cancelled.
WHY_IT_MATTERS: >
  Restoring a stale reservation state ignores everything that happened to stock while the line was
  cancelled, potentially reserving a unit that has since been committed elsewhere.
DISCONFIRMING_OBSERVATION: >
  Reactivating a cancelled line restores its old reservation outright without checking whether that stock
  is still actually free.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm and reserve a line, cancel it, allow the released stock to be claimed elsewhere, then reactivate
  the line and check what it does.
```

## G08-SALE_STOCK-Q041

```yaml
QID: G08-SALE_STOCK-Q041
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A backorder created for the undelivered remainder of a line is linked back to the original order and
  line it came from, rather than appearing as an unrelated new demand with no traceable origin.
WHY_IT_MATTERS: >
  An untraceable backorder cannot be matched back to the customer promise it exists to fulfil, defeating
  the reason it was created in the first place.
DISCONFIRMING_OBSERVATION: >
  A backorder created from a partial delivery shortfall shows no reference back to the order and line that
  generated it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Partially deliver a line so that a backorder is generated for the remainder, then check whether the
  backorder references its originating order and line.
```

## G08-SALE_STOCK-Q042

```yaml
QID: G08-SALE_STOCK-Q042
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A product whose on-hand quantity is already negative at the moment an order line for it is confirmed
  does not display that line as fully available to promise; the shortfall is surfaced in some observable
  way at confirmation rather than only becoming apparent later when reservation fails.
WHY_IT_MATTERS: >
  Discovering the shortfall only at the reservation stage, rather than at confirmation, delays the moment
  a business could have communicated a delay to the customer.
DISCONFIRMING_OBSERVATION: >
  An order line for a product already at negative on-hand confirms showing full availability, with the
  shortfall only surfacing at a later step.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Bring a product's on-hand quantity to negative through an allowed override elsewhere, then confirm a new
  order line for that product and inspect what it shows about availability.
```

## G08-SALE_STOCK-Q043

```yaml
QID: G08-SALE_STOCK-Q043
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether partial delivery is allowed on an order or line at all is a configurable choice, and when it is
  configured as disallowed, an attempt to deliver less than the full line quantity is refused rather than
  silently proceeding as a partial delivery anyway.
WHY_IT_MATTERS: >
  A configuration that is silently ignored at the point where it matters gives whoever set it a false
  sense that partial shipments cannot happen.
DISCONFIRMING_OBSERVATION: >
  An order configured to disallow partial delivery still allows a movement for less than the full line
  quantity to be completed.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Configure an order or line to disallow partial delivery, then attempt to deliver less than the full
  quantity and observe the result.
```

## G08-SALE_STOCK-Q044

```yaml
QID: G08-SALE_STOCK-Q044
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether the figure used to promise stock to a new order includes expected incoming receipts or only
  physical on-hand quantity is a configurable business rule, and orders are evaluated consistently against
  whichever definition is actually configured rather than against a fixed, undocumented assumption.
WHY_IT_MATTERS: >
  Two orders evaluated under two different, undocumented notions of what counts as available produce
  promises that cannot be compared or trusted against each other.
DISCONFIRMING_OBSERVATION: >
  Two orders for the same product, confirmed under the same configuration, are evaluated against visibly
  different notions of what counts as available.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Set the available-to-promise definition to a specific configured rule, confirm two comparable orders
  under it, and check that both were evaluated against the same definition.
```

## G08-SALE_STOCK-Q045

```yaml
QID: G08-SALE_STOCK-Q045
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The sum of everything ever delivered against a line across any number of partial movements and
  corrections never exceeds the quantity actually confirmed on that line at any point in time.
WHY_IT_MATTERS: >
  Overshipping beyond what was ever actually committed is a direct, avoidable cost with no commercial
  justification once it has physically happened.
DISCONFIRMING_OBSERVATION: >
  The cumulative delivered quantity recorded against a line, across all of its partial movements and
  corrections, exceeds the quantity that line was ever confirmed for.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Perform several partial deliveries and at least one correction against a single line, then sum
  everything delivered and compare it to the line's confirmed quantity.
```

## G08-SALE_STOCK-Q046

```yaml
QID: G08-SALE_STOCK-Q046
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  When fulfilment of an order is handed to a different warehouse team than the one that confirmed it, that
  fulfilling team's ability to alter the order's reservation or commitment date is bounded by a defined
  permission rather than being open to unilateral change by whichever side happens to act last.
WHY_IT_MATTERS: >
  An unbounded ability to quietly change a commercial commitment from the fulfilment side removes
  accountability for who actually decided to alter a promise made to the customer.
DISCONFIRMING_OBSERVATION: >
  A user acting purely in a fulfilment role, with no commercial authority granted, can change the order's
  commitment date or reservation with no permission check and no distinguishable record of having done so.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  As a fulfilment-only role, attempt to alter a confirmed order's commitment date or reservation and
  observe whether the action is permitted and recorded.
```

## G08-SALE_STOCK-Q047

```yaml
QID: G08-SALE_STOCK-Q047
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A line partially delivered once in one unit of measure and again in a different, but convertible, unit
  of measure still sums, in the order's own commercial unit, to a single consistent delivered total rather
  than the two partial figures being tracked as unreconciled quantities in their own separate units.
WHY_IT_MATTERS: >
  Unreconciled mixed-unit partials make it impossible to state confidently how much of the original
  commercial promise has actually been fulfilled.
DISCONFIRMING_OBSERVATION: >
  Two partial deliveries of the same line recorded in two different convertible units do not sum to a
  single, coherent total in the order's commercial unit.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Deliver a line partially in one unit of measure and partially in a different, convertible unit, then
  check the line's total delivered quantity in its own commercial unit.
```

## G08-SALE_STOCK-Q048

```yaml
QID: G08-SALE_STOCK-Q048
MODULE: sale_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a commercial edit to an order line (such as a quantity change) and a fulfilment-side event on the
  same line (such as a delivery being recorded) happen at effectively the same time, the two effects are
  both retained rather than one silently overwriting the other.
WHY_IT_MATTERS: >
  A silently lost fulfilment event or a silently lost commercial edit each produce a record that no longer
  matches what actually happened, in opposite but equally damaging ways.
DISCONFIRMING_OBSERVATION: >
  Making a commercial edit to a line at the same moment a delivery is being recorded against it causes one
  of the two changes to be lost with no trace.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Arrange a quantity edit on a line to occur at effectively the same time as a delivery is recorded against
  that line, then check that both changes are reflected.
```

---
## GMVQ Internal QA Checklist

- [x] 48 distinct MVQ records; no padding — every record targets a distinct hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`.
- [x] Questions are behavioral and source-neutral; no vendor/product name, technical identifier, or module
      name appears in question text.
- [x] Bridge Module Rule seam test applied to every question: removing either the commercial-order
      capability or the physical-movement capability would make each question meaningless.
- [x] Two orders promising the same unit represented (Q001-Q004).
- [x] Promise at quotation vs honoured at confirmation represented (Q005-Q008).
- [x] Reservation at confirmation vs at scheduling, and what holds goods between, represented
      (Q009-Q011).
- [x] Committed date derived from availability, later changing, represented (Q005, Q007, Q008, Q019).
- [x] Line quantity increased after partial shipment represented (Q012-Q014).
- [x] Order cancelled after reservation but before dispatch, and what releases, represented
      (Q015-Q017).
- [x] Partial delivery and the remainder's promise represented (Q018-Q020).
- [x] Delivery from a different warehouse or company than the order's represented (Q021-Q023).
- [x] Order's unit vs movement's unit represented (Q024-Q025).
- [x] Return creating an inbound movement against a sold line represented (Q026-Q028).
- [x] Invoicing policy keyed to delivered quantity and a movement later corrected represented
      (Q029-Q030).
- [x] Order shipped complete but invoiced partially, or the reverse, represented (Q031-Q033).
- [x] Role/permission and tenant/company boundary represented (Q022, Q034, Q046).
- [x] Configuration dependency and reachability represented (Q009, Q035, Q043, Q044).
- [x] Concurrency and ordering represented (Q003, Q010, Q039, Q048).
- [x] Auditability represented (Q007, Q036, Q041).
- [x] Cross-module dependency / negative case (non-stocked lines, negative on-hand) represented
      (Q037, Q042).
- [x] No specific Thai legal or tax requirement asserted anywhere in this bank.
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT

