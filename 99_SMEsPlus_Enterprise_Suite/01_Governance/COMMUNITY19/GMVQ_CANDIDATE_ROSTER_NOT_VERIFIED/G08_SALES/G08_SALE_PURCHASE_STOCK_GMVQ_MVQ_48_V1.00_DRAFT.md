# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_purchase_stock Module Bridge MVQ Bank

**Document ID:** GMVQ-G08-SALE_PURCHASE_STOCK-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_purchase_stock`
**Wave:** W2
**Author Cell:** P-S6 (GMVQ Question Factory — Wave W2 Acceleration, 25-Team Programme)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `sale_purchase_stock` — a BRIDGE per
GMVQ_BRIDGE_MODULE_RULE_V1.00, seam: procure-to-order that ALSO moves physical stock through the
selling business's own warehouse before delivery — three documents (customer order, vendor order,
physical receipt/delivery) governing one commitment. Only a genuinely three-way question belongs
here: if a question works with only two of the three documents in view, it belongs to the
already-authored `sale_purchase` bank (no stock) or to a production seam, not here. This bank is
also distinct from the drop-ship mechanism, where a vendor ships directly to the customer and the
selling business's own stock is never touched — that ground is out of scope here by definition,
since every question below assumes goods are physically received into the seller's own stock
first. Ground covered: goods received into stock and immediately owed to a specific customer —
whether reserved or pooled; a different order consuming units that arrived for this one; a
received quantity differing from both the vendor order and the customer order, and which one
absorbs the difference; goods arriving damaged against a promise already made; the chain's
traceability from customer line to vendor line to physical unit; a customer order cancelled after
receipt, leaving stock nobody ordered; a period straddle across vendor invoice, receipt, delivery
and customer invoice; and cross-company setups where the receiving and selling entities differ.
Every question passed the bridge removal test for a three-document seam: it must fail only where
the vendor side, the customer side, AND the physical stock movement all have to be considered
together. Coverage spans business capability, business rule, state transition, configuration
dependency, role and permission, exception path, cancellation, reversal, negative case,
cross-module dependency, optional behaviour, auditability, tenant/company boundary, concurrency
and ordering, runtime reachability, configuration reachability, and source/runtime contradiction
potential.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material three-way seam hypotheses;
  none was trimmed or stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table,
  field, method, XML ID, API path), and the module's own metadata name never appears outside the
  `MODULE:` field.
- Every question requires all three documents (customer order, vendor order, physical stock event)
  to make sense; a question answerable with only two was cut to the two-document `sale_purchase`
  bank instead.
- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$G07_DIR"/*.md | sort`
  was run against the existing `purchase`, `purchase_mrp`, `purchase_requisition_sale` and
  `purchase_requisition_stock` banks. `purchase_requisition_stock` covers an automatic
  general-replenishment rule raising a requisition with no waiting customer order in view — a
  different mechanism entirely from a specific customer order directly driving a specific vendor
  order and receipt — so no hypothesis here restates one of theirs. `grep -h 'HYPOTHESIS'
  "$G08_DIR"/*.md | sort` was run against the already-authored `sale_mrp` and `sale_purchase`
  banks: `sale_mrp`'s ground is production-triggered fulfilment with no vendor order in view at
  all, and `sale_purchase`'s ground is the same commercial seam as this bank but explicitly
  excludes any physical stock receipt — every question below that resembles one of theirs was
  rebuilt around the three-way physical receipt event that only exists in this module, and any
  question that would still make sense with the receipt removed was cut back to `sale_purchase`.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_PURCHASE_STOCK-Q001

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q001
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When goods received from a vendor order are known at receipt to be sourcing a specific customer
  order, the received units are reserved to that customer order rather than pooled as general,
  undifferentiated stock available to any demand.
WHY_IT_MATTERS: >
  Pooling units already owed to a specific customer risks another demand consuming them before the
  customer they were actually sourced for is served.
DISCONFIRMING_OBSERVATION: >
  Goods received against a vendor order known to be sourcing a specific customer order appear as
  general, unreserved stock available to any other demand.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive goods against a vendor order known to be sourcing a specific customer order and check
  whether the received units are reserved to it or left as general stock.
```

## G08-SALE_PURCHASE_STOCK-Q002

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q002
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether goods received against a customer-linked vendor order are automatically reserved to that
  customer order, or require a manual reservation step, is a deliberate, discoverable
  configuration behaviour, not an unstated default.
WHY_IT_MATTERS: >
  An unstated default risks either automatic reservation being silently assumed where it never
  actually runs, or an unnecessary manual step burying a link that should already exist.
DISCONFIRMING_OBSERVATION: >
  Two comparably configured environments differ on whether receipt against a customer-linked
  vendor order automatically reserves the goods, with no discoverable setting explaining the
  difference.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Receive goods against a customer-linked vendor order in two separately configured environments
  and compare whether reservation happens automatically.
```

## G08-SALE_PURCHASE_STOCK-Q003

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q003
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Units reserved to a specific customer order at receipt remain reserved to it through to
  delivery, not silently released back to general stock by an unrelated event in between.
WHY_IT_MATTERS: >
  An unexplained release breaks the very commitment the reservation was meant to protect, with
  nobody having decided to release it.
DISCONFIRMING_OBSERVATION: >
  Units reserved to a customer order at receipt are found available to other demand before that
  customer order was ever delivered, cancelled, or otherwise resolved.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve received units to a customer order, then check their availability to other demand before
  that order is delivered.
```

## G08-SALE_PURCHASE_STOCK-Q004

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q004
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Overriding a reservation that ties received goods to a specific customer order, to redirect them
  elsewhere, requires an authority distinct from ordinary stock allocation.
WHY_IT_MATTERS: >
  Treating the override as ordinary allocation lets a customer's already-secured supply be
  redirected with nobody accountable for that specific decision.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary stock-allocation permission is able to redirect units reserved to a
  specific customer order to a different demand with no additional approval invoked.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with only ordinary allocation permission, attempt to redirect units already reserved
  to a specific customer order.
```

## G08-SALE_PURCHASE_STOCK-Q005

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q005
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where goods received against a consolidated vendor order serve several customer orders, the
  received quantity is divided among them by a defined, repeatable rule, not by whichever order
  happens to be checked first.
WHY_IT_MATTERS: >
  An undefined division rewards checking order over any real business priority when receipt has to
  be shared out among several waiting customers.
DISCONFIRMING_OBSERVATION: >
  Repeating an identical receipt scenario against the same set of customer orders sharing a
  consolidated vendor order produces a different division between them on separate occasions with
  no rule explaining the difference.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive goods against a consolidated vendor order serving several customer orders more than once
  under identical conditions and compare the resulting division.
```

## G08-SALE_PURCHASE_STOCK-Q006

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q006
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Overriding the reservation that ties received goods to a specific customer order is recorded as
  a distinguishable event, including who made the change and why, not merged invisibly into
  ordinary stock movement history.
WHY_IT_MATTERS: >
  An invisible override removes any way to later investigate why a customer's secured supply ended
  up serving someone else.
DISCONFIRMING_OBSERVATION: >
  Received goods reserved to a specific customer order are redirected to different demand, and the
  stock movement history shows no distinguishable record of the redirection or its reason.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Redirect units already reserved to a specific customer order to different demand and inspect the
  stock movement history for a record of the change.
```

## G08-SALE_PURCHASE_STOCK-Q007

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q007
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When units received and reserved for one customer order are consumed by a different order's
  delivery, that consumption is blocked or, if allowed, surfaced as a visible exception, not
  silently permitted with no trace.
WHY_IT_MATTERS: >
  Silent cross-consumption leaves the originally intended customer short with nobody aware it
  happened.
DISCONFIRMING_OBSERVATION: >
  Units reserved for one customer order are delivered against a different order's demand with no
  block and no resulting exception or record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reserve received units to one customer order, attempt to deliver them against a different order,
  and observe whether this is blocked or flagged.
```

## G08-SALE_PURCHASE_STOCK-Q008

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q008
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where cross-consumption of reserved units does occur, the order that lost its reserved units is
  left with a visible, distinguishable shortage, not silently shown as still covered.
WHY_IT_MATTERS: >
  Showing an order as still covered after its reserved supply was actually taken elsewhere hides a
  shortfall the customer will eventually feel.
DISCONFIRMING_OBSERVATION: >
  An order whose reserved units were consumed by a different order's delivery still shows as fully
  covered, with no shortage indicator.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cause cross-consumption of reserved units between two customer orders and inspect the state of
  the order that lost its reservation.
```

## G08-SALE_PURCHASE_STOCK-Q009

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q009
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Cross-consumption of another order's reserved units requires an authority distinct from ordinary
  delivery processing, given that it takes supply away from a customer commitment that was not the
  one being fulfilled.
WHY_IT_MATTERS: >
  Treating cross-consumption as ordinary delivery processing lets it happen with nobody accountable
  for the customer it disadvantaged.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary delivery-processing permission is able to consume another order's
  reserved units with no additional approval invoked.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with only ordinary delivery-processing permission, attempt to deliver against units
  reserved for a different customer order.
```

## G08-SALE_PURCHASE_STOCK-Q010

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q010
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If two deliveries are processed at effectively the same time and both would draw on the same
  limited reserved units, only one delivery actually consumes them, and the other results in a
  visible shortage rather than both silently succeeding against the same physical units.
WHY_IT_MATTERS: >
  Allowing both to silently succeed overstates the physical stock actually available and
  guarantees a discrepancy discovered only later.
DISCONFIRMING_OBSERVATION: >
  Two deliveries processed at effectively the same time both consume the same limited reserved
  units, with both appearing to succeed in full.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Process two deliveries at effectively the same time that both draw on the same limited reserved
  units and inspect whether both succeed in full.
```

## G08-SALE_PURCHASE_STOCK-Q011

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q011
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A reservation tying received units to a customer order cannot be silently cleared by an
  unrelated stock adjustment or correction elsewhere in the warehouse.
WHY_IT_MATTERS: >
  An unrelated adjustment clearing a reservation would sever a customer commitment for a reason
  that has nothing to do with that customer.
DISCONFIRMING_OBSERVATION: >
  An unrelated stock adjustment elsewhere in the warehouse clears or reduces a reservation tying
  received units to a specific customer order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Perform an unrelated stock adjustment in the same warehouse as a reserved customer order's units
  and check whether the reservation is affected.
```

## G08-SALE_PURCHASE_STOCK-Q012

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q012
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where reserved units are legitimately reassigned away from the order they were reserved for, for
  instance because that order was cancelled, the units becoming available to another order is a
  distinguishable, deliberate event, not indistinguishable from an original reservation.
WHY_IT_MATTERS: >
  An indistinguishable reassignment makes it impossible to later tell whether a unit's current
  reservation was its first or a later reassignment.
DISCONFIRMING_OBSERVATION: >
  Units reassigned from a cancelled order's reservation to a different order show no
  distinguishable record that a reassignment, rather than an original reservation, occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a customer order holding a reservation, allow its units to be reassigned to a different
  order, and inspect the resulting record for a distinguishable reassignment event.
```

## G08-SALE_PURCHASE_STOCK-Q013

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q013
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the quantity actually received differs from both the quantity on the vendor order and the
  quantity on the customer order it was sourcing, the resulting three-way discrepancy is surfaced
  as a visible exception, not silently resolved by favoring one figure over the other with no
  record.
WHY_IT_MATTERS: >
  Silently favoring one figure hides which of the mismatched documents is actually now wrong, and
  by how much.
DISCONFIRMING_OBSERVATION: >
  A received quantity differing from both the vendor order and the customer order it sources
  produces no discrepancy exception, with one of the two documents simply overwritten to match
  receipt with no record of the mismatch.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive a quantity differing from both the linked vendor order and customer order quantities,
  and inspect whether a three-way discrepancy exception results.
```

## G08-SALE_PURCHASE_STOCK-Q014

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q014
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Resolving a three-way quantity discrepancy at receipt is an action available to a role with
  visibility of both the vendor side and the customer side, not something a purely
  warehouse-facing role can resolve unilaterally with no reference to the customer commitment.
WHY_IT_MATTERS: >
  A warehouse-only resolution risks a decision that ignores what the customer was actually
  promised.
DISCONFIRMING_OBSERVATION: >
  A user with warehouse-only visibility is able to finally resolve a three-way quantity
  discrepancy with no reference to, or visibility of, the customer order it affects.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with warehouse-only access, attempt to resolve a three-way quantity discrepancy at
  receipt.
```

## G08-SALE_PURCHASE_STOCK-Q015

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q015
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the received quantity is less than both the vendor order and the customer order
  quantities, the shortfall is attributed to the vendor rather than silently reducing the
  customer's own order quantity to match what arrived.
WHY_IT_MATTERS: >
  Silently reducing the customer's order to match a vendor shortfall hides a vendor performance
  problem behind what looks like a routine order adjustment.
DISCONFIRMING_OBSERVATION: >
  A shortfall received below both the vendor and customer order quantities results in the
  customer order's own quantity being reduced to match, with no attribution to the vendor
  shortfall.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive less than both the vendor order and customer order quantities, and inspect whether the
  customer order quantity is altered as a result.
```

## G08-SALE_PURCHASE_STOCK-Q016

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q016
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the received quantity exceeds both the vendor order and the customer order quantities, the
  excess is recorded as unattributed stock requiring a decision, not silently added to either
  document's quantity as though it had been ordered.
WHY_IT_MATTERS: >
  Silently absorbing an unordered excess into either document misstates what was actually agreed
  with either the vendor or the customer.
DISCONFIRMING_OBSERVATION: >
  A received quantity exceeding both the vendor and customer order quantities is silently added to
  one of those documents' recorded quantity with no distinct exception or decision point.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive more than both the vendor order and customer order quantities, and inspect how the
  excess is recorded.
```

## G08-SALE_PURCHASE_STOCK-Q017

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q017
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A three-way quantity discrepancy discovered at receipt is traceable, after resolution, back to
  which of the three figures — vendor order, customer order, or physical receipt — actually
  governed the final outcome.
WHY_IT_MATTERS: >
  Without that trace, nobody can later verify whether a discrepancy was resolved in the business's
  favor, the customer's, or arbitrarily.
DISCONFIRMING_OBSERVATION: >
  After a three-way discrepancy is resolved, there is no way to determine from the record which of
  the three original figures the final outcome actually followed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Resolve a three-way quantity discrepancy at receipt and attempt to trace which original figure
  the final outcome followed.
```

## G08-SALE_PURCHASE_STOCK-Q018

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q018
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A three-way discrepancy between vendor order, customer order, and physical receipt is handled by
  the same defined rule regardless of whether the mismatch favors or disadvantages the business
  financially.
WHY_IT_MATTERS: >
  A rule that only triggers scrutiny when the business is disadvantaged, and waves through
  mismatches in its favor, is not really a control at all.
DISCONFIRMING_OBSERVATION: >
  A three-way discrepancy that happens to favor the business financially receives no exception or
  scrutiny, while an equivalent discrepancy disadvantaging the business does.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create two comparable three-way discrepancies, one favoring the business and one disadvantaging
  it, and compare whether both trigger the same exception handling.
```

## G08-SALE_PURCHASE_STOCK-Q019

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q019
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When goods received against a customer-linked vendor order arrive damaged, the affected units
  are excluded from what can be delivered against the customer commitment, rather than remaining
  available to fulfil it.
WHY_IT_MATTERS: >
  Allowing damaged units to remain available risks them actually being shipped to a customer
  before anyone catches the problem.
DISCONFIRMING_OBSERVATION: >
  Goods recorded as arriving damaged remain available to fulfil the customer order they were
  received to source.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive goods against a customer-linked vendor order, record damage on arrival, and check
  whether the damaged units remain available to the customer order.
```

## G08-SALE_PURCHASE_STOCK-Q020

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q020
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a vendor order backing an already-communicated customer delivery commitment is cancelled by
  the vendor, that cancellation generates a discoverable exception routed to a role able to manage
  the customer relationship, not merely an internal procurement record with no onward consequence.
WHY_IT_MATTERS: >
  A vendor cancellation with no routed customer-facing exception leaves the customer relationship
  consequence entirely to chance.
DISCONFIRMING_OBSERVATION: >
  A vendor order backing an already-communicated delivery commitment is cancelled, and no
  exception, alert, or assigned action toward the customer-facing commitment results.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Communicate a delivery commitment to a customer, then cancel the backing vendor order, and
  inspect whether any customer-facing exception results.
```

## G08-SALE_PURCHASE_STOCK-Q021

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q021
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where only part of a received quantity arrives damaged, the undamaged portion remains available
  to at least partially fulfil the customer commitment, rather than the entire receipt being held
  back because part of it was damaged.
WHY_IT_MATTERS: >
  Holding back a good portion unnecessarily delays a customer who could otherwise have received at
  least part of what they were promised.
DISCONFIRMING_OBSERVATION: >
  A partially damaged receipt results in the entire received quantity, including the undamaged
  portion, being withheld from the customer order with no partial fulfilment offered.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive a quantity that is only partially damaged and check whether the undamaged portion
  remains available to the customer order.
```

## G08-SALE_PURCHASE_STOCK-Q022

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q022
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Replacing damaged goods with a fresh vendor order is traceable back to the original damaged
  receipt and the customer order it was meant to satisfy, not treated as an unrelated,
  freestanding new procurement.
WHY_IT_MATTERS: >
  An untraceable replacement makes it impossible to later verify the customer was actually made
  whole for the original damage.
DISCONFIRMING_OBSERVATION: >
  A replacement vendor order raised after damaged goods cannot be traced back to the original
  damaged receipt or the customer order it was meant to satisfy.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Raise a replacement vendor order following a damaged receipt and attempt to trace it back to the
  original damage event and customer order.
```

## G08-SALE_PURCHASE_STOCK-Q023

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q023
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A financial claim against the vendor for damaged goods is recorded as attributable to the
  specific receipt and customer order affected, not as an unattributed general dispute with no
  link to the underlying transaction.
WHY_IT_MATTERS: >
  An unattributed claim cannot be reconciled against the specific commitment it was meant to
  offset, and risks being lost or double-counted.
DISCONFIRMING_OBSERVATION: >
  A financial claim raised against a vendor for damaged goods carries no link back to the specific
  receipt or customer order the damage affected.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Raise a vendor claim for goods damaged on receipt and inspect whether it is linked back to the
  specific receipt and customer order.
```

## G08-SALE_PURCHASE_STOCK-Q024

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q024
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a vendor order covering a customer commitment is received in more than one partial
  shipment, the customer-facing commitment is fulfilled only as each partial receipt actually
  arrives, not marked satisfied in full upon the first partial receipt.
WHY_IT_MATTERS: >
  Marking the commitment satisfied on the first partial receipt would tell the customer their full
  order is ready when only part of it has actually arrived.
DISCONFIRMING_OBSERVATION: >
  After only a partial receipt against a split vendor order, the linked customer-facing commitment
  already shows as fully satisfied.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Place a vendor order covering a customer commitment, receive it in more than one partial
  shipment, and check the commitment's fulfilment status after only the first partial receipt.
```

## G08-SALE_PURCHASE_STOCK-Q025

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q025
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A specific physical unit delivered to a customer can be traced back through its receipt to the
  specific vendor order line that brought it in, and onward to the specific customer order line it
  was sourced for.
WHY_IT_MATTERS: >
  A broken link anywhere in that chain makes it impossible to investigate a later complaint or
  recall back to its actual commercial origin.
DISCONFIRMING_OBSERVATION: >
  A delivered unit's trace back through receipt to its vendor order line, or onward to its
  customer order line, breaks at some point even though the underlying transactions all exist.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deliver a unit sourced through a customer-linked vendor order and attempt to trace it back
  through receipt to the vendor order line and the customer order line.
```

## G08-SALE_PURCHASE_STOCK-Q026

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q026
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where the received units for one vendor order line are split across deliveries to more than one
  customer order, the trace correctly attributes each delivered unit to the specific customer
  order it actually went to.
WHY_IT_MATTERS: >
  A trace that cannot distinguish which of several customers actually received which unit makes it
  impossible to isolate who is affected by a problem found in part of the receipt.
DISCONFIRMING_OBSERVATION: >
  Units received against one vendor order line and delivered to more than one customer order
  cannot be individually traced to which customer order each specific unit actually went to.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Split the receipt from one vendor order line across deliveries to more than one customer order
  and attempt to trace individual units to their actual recipient order.
```

## G08-SALE_PURCHASE_STOCK-Q027

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q027
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If the physical location a unit was received into differs from the location it was ultimately
  delivered from, because of an internal transfer between the two, the three-way trace still
  connects the receipt to the eventual delivery across that internal transfer.
WHY_IT_MATTERS: >
  A trace that stops at an internal transfer would falsely suggest the delivered unit has no
  traceable link back to its original vendor receipt.
DISCONFIRMING_OBSERVATION: >
  A unit received at one location and internally transferred to another before delivery cannot be
  traced, as the same physical unit, back through the transfer to its original vendor receipt.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive a unit at one location, transfer it internally to another location, deliver it from
  there, and attempt to trace it back through the transfer to the original receipt.
```

## G08-SALE_PURCHASE_STOCK-Q028

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q028
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a vendor delivers a different item than the one actually ordered against a customer
  commitment, that substitution is recorded as a discoverable discrepancy, rather than the
  received item silently being treated as satisfying the original commitment unchanged.
WHY_IT_MATTERS: >
  Silently treating a substitute as satisfying the original commitment could deliver the wrong item
  to a customer with no record that a substitution ever occurred.
DISCONFIRMING_OBSERVATION: >
  A vendor's delivery of a different item than ordered is recorded as satisfying the original
  customer commitment with no discrepancy noted anywhere.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Have a vendor deliver a different item than what was ordered against a customer commitment, and
  check whether the substitution is recorded as a discrepancy.
```

## G08-SALE_PURCHASE_STOCK-Q029

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q029
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The three-way chain from customer order line to vendor order line to physical receipt remains
  traceable even where the receipt is split across more than one physical delivery from the
  vendor.
WHY_IT_MATTERS: >
  Losing the chain across split deliveries hides the true origin of units that arrived in more
  than one shipment.
DISCONFIRMING_OBSERVATION: >
  A vendor order line fulfilled through more than one physical delivery cannot be traced, as a
  whole, back to the single customer order line it was sourcing.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Fulfil one vendor order line through more than one physical delivery and attempt to trace the
  combined receipt back to the customer order line it sources.
```

## G08-SALE_PURCHASE_STOCK-Q030

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q030
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a vendor supplies goods under their own lot or batch identification, that vendor-assigned
  identification is retained and can be recovered from the received stock's own record, not
  silently replaced by an internal lot identity with no link back to the vendor's original one.
WHY_IT_MATTERS: >
  Losing the link to the vendor's own lot identification would prevent matching a vendor recall or
  quality notice, issued against the vendor's lot numbers, back to the specific stock affected.
DISCONFIRMING_OBSERVATION: >
  Received stock under vendor lot tracking shows no recoverable link to the vendor's own lot or
  batch identification for that shipment.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Receive goods from a vendor that supplies its own lot or batch identification, and check whether
  that vendor identification can be recovered from the received stock's own record.
```

## G08-SALE_PURCHASE_STOCK-Q031

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q031
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a customer order is cancelled after the goods sourced for it have already been received,
  those goods are flagged as no longer committed to any customer, rather than remaining shown as
  reserved to a cancelled order indefinitely.
WHY_IT_MATTERS: >
  Goods left reserved to a cancelled order are goods unavailable to any real, still-active demand
  for no reason.
DISCONFIRMING_OBSERVATION: >
  Cancelling a customer order after its sourced goods were already received leaves those goods
  still shown as reserved to the cancelled order with no resulting flag or release.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive goods sourced for a customer order, cancel that order after receipt, and inspect the
  state of the received goods.
```

## G08-SALE_PURCHASE_STOCK-Q032

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q032
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Goods left over from a customer order cancelled after receipt remain traceable back to the order
  and customer they were originally sourced for, even after being released to general stock.
WHY_IT_MATTERS: >
  Losing that trace removes any basis for later deciding whether to hold, discount, or return the
  goods, or investigate why the cancellation happened after receipt.
DISCONFIRMING_OBSERVATION: >
  Goods released to general stock after their originating customer order was cancelled
  post-receipt can no longer be traced back to that order or customer.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a customer order after its sourced goods were received, release the goods to general
  stock, and attempt to trace them back to the cancelled order.
```

## G08-SALE_PURCHASE_STOCK-Q033

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q033
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether goods orphaned by a post-receipt cancellation are automatically released to general
  stock or require a deliberate disposition decision is a discoverable configuration behaviour,
  not an unstated default.
WHY_IT_MATTERS: >
  An unstated default either strands goods in limbo indefinitely or releases custom or committed
  goods into general stock with nobody having decided that was appropriate.
DISCONFIRMING_OBSERVATION: >
  Two comparably configured environments handle an identical post-receipt cancellation differently
  regarding automatic release to general stock, with no discoverable setting explaining the
  difference.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Cancel a customer order after receipt in two separately configured environments and compare
  whether the goods are automatically released to general stock.
```

## G08-SALE_PURCHASE_STOCK-Q034

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q034
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A vendor return or credit process for goods orphaned by a post-receipt customer cancellation is
  traceable back to the original cancellation that caused it, not treated as an unrelated,
  freestanding stock reduction.
WHY_IT_MATTERS: >
  An untraceable return obscures the actual reason stock is leaving, and whether the vendor is
  honoring an obligation created by the original transaction.
DISCONFIRMING_OBSERVATION: >
  A vendor return processed for goods orphaned by a post-receipt cancellation carries no link back
  to the cancellation that caused the goods to become orphaned.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Cancel a customer order after receipt, initiate a vendor return for the resulting orphaned
  goods, and inspect whether the return is linked to the cancellation.
```

## G08-SALE_PURCHASE_STOCK-Q035

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q035
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where goods orphaned by one cancelled customer order are subsequently allocated to a different,
  unrelated customer order, that allocation is recorded as a distinguishable event, not appearing
  as though the second order had been the original source of the receipt.
WHY_IT_MATTERS: >
  An indistinguishable reallocation erases the actual history of where the goods came from and why
  they were available.
DISCONFIRMING_OBSERVATION: >
  Goods orphaned by a cancelled customer order and later allocated to a different order show no
  distinguishable record that they were originally sourced for, and orphaned by, the first order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a customer order after receipt, allocate the resulting orphaned goods to a different
  customer order, and inspect the record for a distinguishable reallocation trace.
```

## G08-SALE_PURCHASE_STOCK-Q036

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q036
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The financial consequence of goods orphaned by a post-receipt cancellation, such as a holding
  cost or valuation adjustment, is attributed to a specific recorded decision, not silently
  absorbed into general inventory valuation with no trace of why it changed.
WHY_IT_MATTERS: >
  An invisibly absorbed consequence hides a real cost from whoever is accountable for inventory or
  cancellation decisions.
DISCONFIRMING_OBSERVATION: >
  The valuation or holding cost of orphaned goods changes following a post-receipt cancellation
  with no recorded decision or reason for the change.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Cancel a customer order after receipt, allow the orphaned goods to sit in stock, and inspect
  whether any valuation change is recorded with a reason.
```

## G08-SALE_PURCHASE_STOCK-Q037

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q037
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the vendor's receipt and the customer's delivery for the same three-way chain fall in
  different accounting periods, each side's financial recognition is attributed to the period the
  physical event actually happened in, not both forced into whichever period is currently open.
WHY_IT_MATTERS: >
  Forcing both into the currently open period misstates the results of whichever period the
  physical event actually happened in.
DISCONFIRMING_OBSERVATION: >
  A receipt and its corresponding delivery falling in different accounting periods are both
  recognized in the same, currently open period regardless of when each physical event occurred.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a receipt and its corresponding delivery in different accounting periods and inspect
  which period each side's financial recognition is attributed to.
```

## G08-SALE_PURCHASE_STOCK-Q038

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q038
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the vendor invoice for a receipt arrives in a later period than the receipt itself, the
  cost is still attributable to the period of physical receipt through an accrual, rather than
  only appearing once the vendor invoice itself arrives.
WHY_IT_MATTERS: >
  Waiting for the vendor invoice to recognize a cost that physically occurred earlier misstates the
  period the goods actually arrived in.
DISCONFIRMING_OBSERVATION: >
  A vendor invoice arriving in a later period than its receipt results in no cost being
  attributable to the receipt's own period until the invoice itself arrives.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive goods in one period and receive the corresponding vendor invoice in a later period, then
  inspect whether any cost is attributed to the receipt's own period.
```

## G08-SALE_PURCHASE_STOCK-Q039

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q039
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where the customer invoice for a delivery is raised in a later period than the delivery itself,
  the revenue recognition rule applied is a deliberate, documented choice, not an unexplained
  inconsistency between comparable transactions.
WHY_IT_MATTERS: >
  An unexplained inconsistency between comparable transactions makes period-end results impossible
  to explain or defend.
DISCONFIRMING_OBSERVATION: >
  Two comparable deliveries with customer invoices raised in a later period are recognized in
  different periods from each other with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Create two comparable deliveries each invoiced in a later period and compare the period each
  one's revenue is recognized in.
```

## G08-SALE_PURCHASE_STOCK-Q040

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q040
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A three-way chain straddling a period boundary remains fully traceable across that boundary, so
  the vendor invoice, receipt, delivery, and customer invoice can all still be linked together
  regardless of which periods they individually fall in.
WHY_IT_MATTERS: >
  A chain that loses its links across a period boundary would defeat period-end reconciliation for
  exactly the transactions most likely to need it.
DISCONFIRMING_OBSERVATION: >
  A three-way chain whose four events fall across more than one accounting period can no longer be
  fully linked together once the periods involved have been closed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a three-way chain whose vendor invoice, receipt, delivery, and customer invoice fall
  across more than one period, close those periods, and attempt to trace the chain as a whole.
```

## G08-SALE_PURCHASE_STOCK-Q041

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q041
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Closing an accounting period does not prevent a chain still open in that period, such as goods
  received but not yet delivered, from being completed and correctly attributed once it does
  complete.
WHY_IT_MATTERS: >
  A closed period that blocks completion of a still-open chain would leave real inventory or
  commitments unable to be finished off correctly.
DISCONFIRMING_OBSERVATION: >
  Goods received in a now-closed period, but not yet delivered at the time it closed, cannot be
  correctly delivered and attributed once delivery actually happens afterward.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive goods in a period that is then closed before delivery, and attempt to complete and
  attribute the delivery afterward.
```

## G08-SALE_PURCHASE_STOCK-Q042

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q042
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Adjusting the cost or valuation basis of a receipt after its period has closed, because of a
  late vendor invoice or correction, requires an authority distinct from ordinary receipt entry,
  given that it revises an already-closed period's figures.
WHY_IT_MATTERS: >
  Treating a closed-period adjustment as ordinary entry lets prior results be revised with nobody
  accountable for that specific decision.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary receipt-entry permission is able to adjust the cost or valuation of a
  receipt in an already-closed period with no additional approval invoked.
EXPECTED_SURFACE: S2,S4
PRECONDITIONS: >
  As a user with only ordinary receipt-entry permission, attempt to adjust the valuation of a
  receipt whose accounting period has already closed.
```

## G08-SALE_PURCHASE_STOCK-Q043

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q043
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where the company physically receiving the goods differs from the company holding the customer
  order, the three-way chain records both companies' roles distinctly, rather than treating the
  transaction as though a single company had performed both parts.
WHY_IT_MATTERS: >
  Collapsing two distinct companies' roles into one hides an intercompany transaction that
  actually needs its own accounting and accountability.
DISCONFIRMING_OBSERVATION: >
  A three-way chain spanning a receiving company and a different selling company shows no
  distinction between which company performed which role, as though a single company had done
  both.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a three-way chain where the receiving company and the selling company differ, and inspect
  whether the record distinguishes each company's role.
```

## G08-SALE_PURCHASE_STOCK-Q044

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q044
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An intercompany transfer of goods from the receiving company to the selling company, arising
  from a cross-company three-way chain, generates its own recorded transaction between the two
  companies, not an invisible movement with no intercompany record at all.
WHY_IT_MATTERS: >
  An invisible intercompany movement leaves neither company's books able to show what was actually
  transferred and at what value.
DISCONFIRMING_OBSERVATION: >
  Goods move from the receiving company to the selling company in a cross-company chain with no
  intercompany transaction recorded between them.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a cross-company three-way chain and inspect whether an intercompany transaction is
  recorded for the movement between the two companies.
```

## G08-SALE_PURCHASE_STOCK-Q045

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q045
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user with access limited to one company in a cross-company chain cannot see or act on the full
  chain's detail belonging to the other company, only on the portion attributable to their own
  company.
WHY_IT_MATTERS: >
  Exposing one company's full detail to a user scoped to a different company breaches the access
  boundary the multi-company setup is meant to enforce.
DISCONFIRMING_OBSERVATION: >
  A user with access limited to one company in a cross-company chain is able to see or act on the
  portion of the chain belonging to the other company.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user scoped to one company in a cross-company three-way chain, attempt to view or act on
  the portion of the chain belonging to the other company.
```

## G08-SALE_PURCHASE_STOCK-Q046

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q046
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The price or transfer value used for the intercompany leg of a cross-company chain is a
  deliberate, recorded figure, not silently assumed equal to either the vendor's price or the
  customer's price with no basis stated.
WHY_IT_MATTERS: >
  An unstated intercompany price makes each company's own margin figure unverifiable and
  potentially wrong.
DISCONFIRMING_OBSERVATION: >
  The intercompany transfer value for a cross-company chain matches either the vendor price or the
  customer price with no recorded basis or rule explaining why that figure was used.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Create a cross-company three-way chain and inspect whether the intercompany transfer value has a
  recorded, deliberate basis.
```

## G08-SALE_PURCHASE_STOCK-Q047

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q047
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling the customer order in a cross-company chain after the receiving company has already
  received goods surfaces the resulting orphaned-goods condition to both companies, not only to
  the one holding the customer order.
WHY_IT_MATTERS: >
  Surfacing the condition to only one company leaves the other company, which is physically
  holding the goods, unaware that its stock is now uncommitted.
DISCONFIRMING_OBSERVATION: >
  Cancelling the customer order in a cross-company chain after receipt produces a visible
  exception in the selling company's records but no corresponding visibility in the receiving
  company's own records.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a customer order in a cross-company three-way chain after the receiving company has
  received goods, and inspect whether both companies show the resulting condition.
```

## G08-SALE_PURCHASE_STOCK-Q048

```yaml
QID: G08-SALE_PURCHASE_STOCK-Q048
MODULE: sale_purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The full three-way trace from customer order line to vendor order line to physical unit remains
  intact across the company boundary, so a unit's origin can be established starting from either
  company's own records.
WHY_IT_MATTERS: >
  A trace that breaks at the company boundary defeats the purpose of tracing at all in exactly the
  setup where it is hardest to reconstruct manually.
DISCONFIRMING_OBSERVATION: >
  Tracing a delivered unit's origin from the selling company's own records stops at the company
  boundary and cannot continue into the receiving company's records, or vice versa.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deliver a unit through a cross-company three-way chain and attempt to trace its origin starting
  from each company's own records in turn.
```
