# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_stock_margin Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-SALE_STOCK_MARGIN-MVQ48-V1.00  
**Group:** G08 SALES  
**Module Metadata:** `sale_stock_margin`  
**Wave:** W2  
**Author Cell:** P-S3 (GMVQ Question Factory — Wave W2 Production)  
**Review Cell:** PENDING  
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN  
**actual_mvq_count:** 48  
**Standard bank reference:** 55 (shared, not reproduced here)  
**Research depth:** 55 + 48 = 103  
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded  

## Purpose

This bank authors the module-specific MVQ set for `sale_stock_margin` — the margin figure computed
on a commercial order line where the cost is a valuation layer, known only when the specific units
actually ship. Per the GMVQ Bridge Module Rule and the Five-Margin Problem in the G08 Group Brief,
this bank is built around the timing, revisability and authority of a cost that is PROVISIONAL until
fulfillment: the figure is an estimate at order time and becomes real only at delivery, drawn from
whichever specific valuation layer or layers the shipped units actually came from. Ground covered:
the provisional-versus-actual transition and whether anything restates; blended figures from
multiple valuation layers in one shipment; partial delivery leaving an order's margin partly actual
and partly still provisional; delivery reversal and redo from different units; a valuation method
changed between order and delivery; delivery from a location carrying a different valuation setting;
revaluation occurring after delivery but before invoicing; and margin built on an estimated cost
while stock is negative. This bank deliberately does not re-author the general cost-basis,
recompute-versus-restate, or reconciliation questions already covered for derived margin figures
elsewhere in the programme, nor the pre-sale standing-cost ground owned by the sibling `sale_margin`
bank; it targets only the ground specific to a cost that is knowable solely at the moment of
fulfillment.

The question text is source-neutral and does not expose vendor model names, field names, methods,
schema, XML IDs, API shapes, or implementation algorithms. `MODULE: sale_stock_margin` appears only
in the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 48 questions exist because they test 48 distinct material hypotheses.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
- Authored under the GMVQ Bridge Module Rule V1.00 Five-Margin Problem: this bank's ground is the
  delivery-valuation cost only; siblings own the pre-sale standing-cost, production-outcome,
  third-party-invoice and recorded-labour cost grounds.

## G08-SALE_STOCK_MARGIN-Q001

```yaml
QID: G08-SALE_STOCK_MARGIN-Q001
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A margin figure shown at order time, before the specific units to be shipped are known, is
  visibly and distinguishably marked as provisional rather than presented identically to a margin
  computed after actual delivery.
WHY_IT_MATTERS: >
  A provisional figure presented as final misleads anyone relying on it to judge the deal's real
  profitability before fulfillment has actually happened.
DISCONFIRMING_OBSERVATION: >
  The margin shown on an order before delivery is presented with no visible distinction from the
  margin shown on a fully delivered order.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Compare the margin display of an unfulfilled order to that of a fully delivered order for
  equivalent items.
```

## G08-SALE_STOCK_MARGIN-Q002

```yaml
QID: G08-SALE_STOCK_MARGIN-Q002
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Confirming delivery replaces the order's provisional margin with the actual figure computed from
  the units actually shipped, rather than leaving the provisional figure standing alongside or
  instead of the actual one with no clear resolution.
WHY_IT_MATTERS: >
  Two live figures with no indication of which now governs leaves every downstream reader guessing
  which number to trust.
DISCONFIRMING_OBSERVATION: >
  After delivery is confirmed, the order still displays the pre-delivery provisional margin, or
  displays both figures with no indication which is now authoritative.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Record the provisional margin before delivery, confirm delivery, and check what the order displays
  afterward.
```

## G08-SALE_STOCK_MARGIN-Q003

```yaml
QID: G08-SALE_STOCK_MARGIN-Q003
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The transition from provisional to actual margin at delivery is logged in a way that preserves
  both the provisional value that existed before and the actual value that replaced it.
WHY_IT_MATTERS: >
  Without both values preserved, nobody can later check whether the pre-delivery estimate the
  business relied on was any good.
DISCONFIRMING_OBSERVATION: >
  After delivery, no record exists anywhere of what the provisional margin had been before it was
  replaced by the actual figure.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Note the provisional margin before delivery, confirm delivery, and search for a record of the
  pre-delivery value afterward.
```

## G08-SALE_STOCK_MARGIN-Q004

```yaml
QID: G08-SALE_STOCK_MARGIN-Q004
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order whose delivery is delayed indefinitely does not have its still-provisional margin treated
  as final in any report that is meant to reflect only realized, delivered business.
WHY_IT_MATTERS: >
  An indefinitely stale estimate counted as realized profit overstates results for business that has
  not actually happened yet.
DISCONFIRMING_OBSERVATION: >
  A report scoped to realized, delivered margin includes the provisional figure of an order whose
  delivery has never occurred.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Leave an order undelivered for an extended period and check whether a realized-margin report
  includes its provisional figure.
```

## G08-SALE_STOCK_MARGIN-Q005

```yaml
QID: G08-SALE_STOCK_MARGIN-Q005
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When an order is invoiced ahead of delivery under an invoice-on-order policy, the margin shown at
  invoicing is explicit about whether it is the provisional or the actual figure.
WHY_IT_MATTERS: >
  Invoicing crystallizes a financial event; a reader of the invoice-time margin needs to know
  whether it rests on a real fulfillment cost or an estimate.
DISCONFIRMING_OBSERVATION: >
  A margin shown at the point of invoicing an order not yet delivered gives no indication of whether
  it is provisional or actual.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Invoice an order under an invoice-on-order policy before delivery occurs, and check whether the
  displayed margin is labeled as provisional.
```

## G08-SALE_STOCK_MARGIN-Q006

```yaml
QID: G08-SALE_STOCK_MARGIN-Q006
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The estimate used for the provisional margin at order time is drawn from a defined, disclosed
  source, such as the most recent known valuation, rather than an arbitrary or unstated figure.
WHY_IT_MATTERS: >
  An estimate with an unknown basis cannot be judged for reasonableness or compared meaningfully to
  the actual figure once it arrives.
DISCONFIRMING_OBSERVATION: >
  The provisional margin at order time cannot be traced to any disclosed cost source.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create an order and attempt to trace the cost basis behind the displayed provisional margin to a
  disclosed source.
```

## G08-SALE_STOCK_MARGIN-Q007

```yaml
QID: G08-SALE_STOCK_MARGIN-Q007
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a single delivery draws from more than one valuation layer at different costs, the line's
  actual margin reflects the true blended cost of the specific units shipped, not the cost of only
  one of the contributing layers.
WHY_IT_MATTERS: >
  Reporting only one layer's cost when several were actually consumed misstates the real cost of
  what was shipped.
DISCONFIRMING_OBSERVATION: >
  A delivery drawing from two valuation layers of different cost shows a margin matching only one
  layer's cost rather than the blend actually shipped.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Fulfill a delivery that draws from two valuation layers of different cost and compare the margin
  to an independently computed blended cost.
```

## G08-SALE_STOCK_MARGIN-Q008

```yaml
QID: G08-SALE_STOCK_MARGIN-Q008
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A blended margin figure drawn from multiple valuation layers is decomposable back to the specific
  layers and quantities that contributed to it.
WHY_IT_MATTERS: >
  A blend that cannot be decomposed cannot be checked, audited, or explained to a customer
  disputing a price.
DISCONFIRMING_OBSERVATION: >
  A blended margin figure exists with no way to identify the layers and quantities that produced it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce a blended-layer delivery and attempt to trace the resulting margin back to its component
  layers and quantities.
```

## G08-SALE_STOCK_MARGIN-Q009

```yaml
QID: G08-SALE_STOCK_MARGIN-Q009
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a delivery blends layers whose costs differ substantially, such as old low-cost stock mixed
  with new high-cost stock, the resulting figure discloses that a blend occurred rather than
  presenting a smooth single number indistinguishable from a single-layer cost.
WHY_IT_MATTERS: >
  A hidden blend across widely different costs can make a genuinely thin margin look comfortable, or
  vice versa, depending on which layer happened to dominate.
DISCONFIRMING_OBSERVATION: >
  A delivery blending layers of substantially different cost shows a margin with no indication that
  more than one cost layer was involved.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Fulfill a delivery from layers of substantially different cost and check whether the resulting
  figure discloses the blend.
```

## G08-SALE_STOCK_MARGIN-Q010

```yaml
QID: G08-SALE_STOCK_MARGIN-Q010
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two deliveries of the same item shipped moments apart from different remaining layers each show a
  margin reflecting their own actual layer mix, rather than both showing an identical average figure
  that matches neither shipment exactly.
WHY_IT_MATTERS: >
  Two different real events collapsing into one shared average erases the very difference the layer
  system exists to track.
DISCONFIRMING_OBSERVATION: >
  Two consecutive deliveries of the same item from different layers show identical margin figures
  despite drawing from different cost layers.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Ship the same item twice in quick succession from different remaining valuation layers and compare
  the two resulting margins.
```

## G08-SALE_STOCK_MARGIN-Q011

```yaml
QID: G08-SALE_STOCK_MARGIN-Q011
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The layer sequence actually used to cost a shipment corresponds to the configured valuation policy
  governing which layers are consumed first, rather than an arbitrary or most-recently-added layer.
WHY_IT_MATTERS: >
  A margin computed against the wrong layer sequence produces a cost figure the business's own
  configured policy would never have produced.
DISCONFIRMING_OBSERVATION: >
  A shipment's margin corresponds to a layer that the configured valuation policy would not have
  selected first for that shipment.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a specific layer-consumption policy, ship an item with multiple layers available, and
  check whether the margin matches the layer the policy would select.
```

## G08-SALE_STOCK_MARGIN-Q012

```yaml
QID: G08-SALE_STOCK_MARGIN-Q012
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a layer's recorded cost is corrected retroactively after it has already been consumed by a
  shipment, any resulting change to that shipment's already-computed margin is traceable to the
  specific correction that caused it.
WHY_IT_MATTERS: >
  An untraceable retroactive change to a previously delivered order's margin cannot be explained to
  anyone who asks why a settled figure moved.
DISCONFIRMING_OBSERVATION: >
  A previously delivered shipment's margin changes after a retroactive layer-cost correction, with
  no record linking the change to that correction.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Retroactively correct the recorded cost of an already-consumed valuation layer and check whether
  the affected shipment's margin change is traceable to the correction.
```

## G08-SALE_STOCK_MARGIN-Q013

```yaml
QID: G08-SALE_STOCK_MARGIN-Q013
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An order with partial delivery shows a margin composed of an actual portion for the delivered
  quantity and a provisional portion for the undelivered quantity, with the two visibly
  distinguished rather than merged into one undifferentiated figure.
WHY_IT_MATTERS: >
  A merged figure hides how much of a partially fulfilled order's profitability is fact and how much
  is still an estimate.
DISCONFIRMING_OBSERVATION: >
  A partially delivered order's margin is presented as one single figure with no distinction between
  the actual and provisional portions.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Partially deliver an order and inspect whether the displayed margin distinguishes the actual and
  provisional portions.
```

## G08-SALE_STOCK_MARGIN-Q014

```yaml
QID: G08-SALE_STOCK_MARGIN-Q014
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The order-level aggregate margin for a partially delivered order makes discoverable what fraction
  of the figure rests on actual delivered cost versus provisional undelivered cost.
WHY_IT_MATTERS: >
  Without a discoverable split, a reviewer cannot judge how much confidence to place in a partially
  fulfilled order's reported margin.
DISCONFIRMING_OBSERVATION: >
  No available view or field discloses what fraction of a partially delivered order's margin is
  actual versus provisional.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Partially deliver a multi-line order and search for a way to discover the actual-versus-provisional
  split of the order-level margin.
```

## G08-SALE_STOCK_MARGIN-Q015

```yaml
QID: G08-SALE_STOCK_MARGIN-Q015
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the provisional cost for a partially delivered order's remaining undelivered quantity changes
  before it ships, only the provisional portion of the order margin moves, leaving the already-actual
  portion for delivered quantity undisturbed.
WHY_IT_MATTERS: >
  A settled, already-fulfilled portion changing value because of a later estimate revision would
  misstate work that has already actually happened.
DISCONFIRMING_OBSERVATION: >
  A change to the estimated cost of undelivered quantity also changes the margin figure attributed
  to the already-delivered quantity of the same order.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Partially deliver an order, change the cost estimate for the remaining quantity, and check whether
  the already-delivered portion's margin is affected.
```

## G08-SALE_STOCK_MARGIN-Q016

```yaml
QID: G08-SALE_STOCK_MARGIN-Q016
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a partially delivered order is fully invoiced despite only partial delivery, the resulting
  margin figure is explicit about the undelivered portion's cost still being an estimate rather than
  presenting one number as if it were entirely settled.
WHY_IT_MATTERS: >
  A fully invoiced document that looks entirely final while resting partly on an estimate overstates
  the certainty of the reported outcome.
DISCONFIRMING_OBSERVATION: >
  A fully invoiced, partially delivered order shows a single margin figure with nothing indicating
  that part of its cost basis is still an estimate.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Fully invoice an order that has only been partially delivered and inspect the resulting margin
  figure for any indication of the estimated portion.
```

## G08-SALE_STOCK_MARGIN-Q017

```yaml
QID: G08-SALE_STOCK_MARGIN-Q017
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  For an order fulfilled through many small partial shipments over time, each new shipment's actual
  cost updates only its own portion of the order margin without disturbing the already-settled actual
  portions recorded from earlier shipments.
WHY_IT_MATTERS: >
  A later shipment retroactively changing an earlier, already-settled shipment's contribution
  destroys the ability to trust any interim figure along the way.
DISCONFIRMING_OBSERVATION: >
  A new partial shipment's delivery changes the margin previously attributed to an earlier,
  already-delivered partial shipment of the same order.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Fulfill an order across several partial shipments and check whether a later shipment changes the
  margin already attributed to an earlier one.
```

## G08-SALE_STOCK_MARGIN-Q018

```yaml
QID: G08-SALE_STOCK_MARGIN-Q018
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a partially delivered order is cancelled for its remaining undelivered quantity, the order's
  margin retains the actual portion for what was delivered and drops the provisional portion for the
  quantity that will now never ship.
WHY_IT_MATTERS: >
  Retaining a provisional estimate for quantity that will never actually ship overstates the margin
  of business that only partly happened.
DISCONFIRMING_OBSERVATION: >
  After cancelling the undelivered remainder of a partially delivered order, the order's margin still
  includes the provisional estimate for the cancelled quantity.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Partially deliver an order, cancel the remaining undelivered quantity, and check whether the
  provisional estimate for the cancelled portion still appears in the margin.
```

## G08-SALE_STOCK_MARGIN-Q019

```yaml
QID: G08-SALE_STOCK_MARGIN-Q019
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a delivery is reversed, its margin contribution, including any valuation-layer consumption
  it recorded, unwinds completely rather than leaving a residual figure attributed to the reversed
  event.
WHY_IT_MATTERS: >
  A residual figure surviving a full reversal misstates an event that, from the business's
  perspective, never actually happened.
DISCONFIRMING_OBSERVATION: >
  After a delivery is fully reversed, some margin or layer-consumption trace attributable to that
  delivery remains.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reverse a completed delivery and check for any remaining margin or layer-consumption trace
  attributed to the reversed event.
```

## G08-SALE_STOCK_MARGIN-Q020

```yaml
QID: G08-SALE_STOCK_MARGIN-Q020
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a reversed delivery is redone and fulfilled from valuation layers different from the ones the
  original delivery consumed, the new margin reflects the layers actually consumed on the redo, not
  the layers consumed by the reversed original.
WHY_IT_MATTERS: >
  A redo that still reflects the undone original's cost misrepresents which units and which cost
  actually left the business the second time.
DISCONFIRMING_OBSERVATION: >
  A redone delivery's margin matches the reversed original's layer cost rather than the layers
  actually consumed by the redo.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reverse a delivery, redo it so that it draws from different valuation layers than the original, and
  compare the new margin to both the original and the redo's actual layers.
```

## G08-SALE_STOCK_MARGIN-Q021

```yaml
QID: G08-SALE_STOCK_MARGIN-Q021
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reversing and redoing a delivery leaves an auditable record of both the original cost and the
  redone cost, so a reviewer can see that a change occurred and can identify why.
WHY_IT_MATTERS: >
  Without both values on record, a margin swing caused by a reversal and redo looks identical to an
  unexplained data error.
DISCONFIRMING_OBSERVATION: >
  After a delivery is reversed and redone, no record distinguishes the original cost from the
  redone cost.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reverse and redo a delivery and search for a record distinguishing the original and redone cost.
```

## G08-SALE_STOCK_MARGIN-Q022

```yaml
QID: G08-SALE_STOCK_MARGIN-Q022
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a delivery is reversed after it has already been invoiced, the resulting margin adjustment
  correctly separates the invoicing-period effect from the delivery-period effect rather than
  conflating the two into a single undated correction.
WHY_IT_MATTERS: >
  A conflated correction cannot be attributed to the right accounting period, undermining any
  period-based reconciliation.
DISCONFIRMING_OBSERVATION: >
  A margin adjustment following a post-invoice delivery reversal cannot be attributed to a specific
  period as either a delivery-period or invoicing-period effect.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Invoice a delivery, then reverse the delivery, and check whether the resulting margin adjustment
  identifies which period it belongs to.
```

## G08-SALE_STOCK_MARGIN-Q023

```yaml
QID: G08-SALE_STOCK_MARGIN-Q023
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a reversed delivery returns units to a valuation layer different from the one they were
  originally drawn from, a later, unrelated shipment that consumes those returned units reflects the
  layer they were actually returned to.
WHY_IT_MATTERS: >
  A later shipment costed against the wrong layer propagates the original reversal's bookkeeping
  error into an otherwise unrelated transaction.
DISCONFIRMING_OBSERVATION: >
  A later shipment consuming units returned by a reversal shows a margin implying a different layer
  than the one the reversal actually returned those units to.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reverse a delivery so units return to a different layer than their origin, then ship those units
  again and check which layer cost the new margin reflects.
```

## G08-SALE_STOCK_MARGIN-Q024

```yaml
QID: G08-SALE_STOCK_MARGIN-Q024
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Repeatedly reversing and redoing the same delivery multiple times does not introduce cumulative
  drift in the margin figure; each full reversal-and-redo cycle is completely undone rather than
  leaving a residual trace.
WHY_IT_MATTERS: >
  Cumulative drift from repeated correction cycles produces a figure with no relationship to the
  actual, final state of the transaction.
DISCONFIRMING_OBSERVATION: >
  After several cycles of reversing and redoing the same delivery back to its original quantity and
  layers, the final margin differs from the margin recorded before the first reversal.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reverse and redo the same delivery several times, returning each time to the same quantity and
  layers, and compare the final margin to the pre-reversal value.
```
## G08-SALE_STOCK_MARGIN-Q025

```yaml
QID: G08-SALE_STOCK_MARGIN-Q025
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the valuation method for an item changes between order confirmation and delivery, the
  delivered margin uses the valuation method actually in effect at the moment of delivery, and which
  method was used is disclosed.
WHY_IT_MATTERS: >
  A method mismatch between what was assumed at order and what was actually applied at delivery
  misstates which rule actually governed the transaction's cost.
DISCONFIRMING_OBSERVATION: >
  A delivered order's margin cannot be traced to the valuation method that was actually in effect at
  the moment of delivery.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change an item's valuation method between order confirmation and delivery, then check which method
  the delivered margin reflects.
```

## G08-SALE_STOCK_MARGIN-Q026

```yaml
QID: G08-SALE_STOCK_MARGIN-Q026
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When stock valued under a prior method and stock valued under a newly adopted method coexist after
  a valuation method change, a shipment's margin correctly reflects which of the two populations of
  stock was actually shipped.
WHY_IT_MATTERS: >
  Attributing the wrong method to a mixed-inventory shipment produces a cost figure that matches
  neither the old nor the new method correctly.
DISCONFIRMING_OBSERVATION: >
  A shipment drawing from stock valued under the prior method shows a margin computed as if it had
  been valued under the newly adopted method, or vice versa.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Change the valuation method with old-method and new-method stock coexisting, ship from the
  old-method stock, and check which method the margin reflects.
```

## G08-SALE_STOCK_MARGIN-Q027

```yaml
QID: G08-SALE_STOCK_MARGIN-Q027
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A valuation method change follows a defined, disclosed rule for whether margins on orders already
  delivered under the prior method are recomputed under the new method or left frozen, rather than
  the outcome depending on when a report happens to be run.
WHY_IT_MATTERS: >
  An undefined rule means the same historical order can show two different margins depending purely
  on the accident of report timing.
DISCONFIRMING_OBSERVATION: >
  The margin of an order delivered before a valuation method change differs depending solely on when,
  after the change, the figure is viewed.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change the valuation method and view the margin of an order delivered before the change at two
  different times afterward.
```

## G08-SALE_STOCK_MARGIN-Q028

```yaml
QID: G08-SALE_STOCK_MARGIN-Q028
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the valuation method changes mid-way through fulfilling a single order across multiple
  partial deliveries, each partial delivery's margin reflects the method actually in effect for that
  specific delivery, rather than one method being forced retroactively across the whole order.
WHY_IT_MATTERS: >
  Forcing a single method across a multi-method fulfillment history misrepresents deliveries that
  genuinely happened under different rules.
DISCONFIRMING_OBSERVATION: >
  A partial delivery made before a valuation method change shows a margin computed under the new
  method rather than the method in effect when it was actually delivered.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change the valuation method between two partial deliveries of the same order and check which method
  each delivery's margin reflects.
```

## G08-SALE_STOCK_MARGIN-Q029

```yaml
QID: G08-SALE_STOCK_MARGIN-Q029
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A margin figure computed under a since-superseded valuation method is flagged as having been
  computed under a method no longer in effect when it is reviewed after the method has changed.
WHY_IT_MATTERS: >
  An unflagged historical figure invites a reviewer to compare it directly against current-method
  figures as though they were computed the same way.
DISCONFIRMING_OBSERVATION: >
  A historical order's margin, computed under a valuation method later superseded, displays with no
  indication that the method has since changed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change the valuation method after an order has been delivered under the old method, then reopen the
  historical order and check for a superseded-method indication.
```

## G08-SALE_STOCK_MARGIN-Q030

```yaml
QID: G08-SALE_STOCK_MARGIN-Q030
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a valuation method change is reverted back to the original method shortly after being made,
  margins computed in the interim retain the values actually computed under the temporarily active
  method rather than silently reverting to what they would have been under the original method.
WHY_IT_MATTERS: >
  Silently rewriting a real interim event as though it never happened erases a true record of what
  was actually shipped and costed at that moment.
DISCONFIRMING_OBSERVATION: >
  A margin computed while a valuation method was temporarily active changes after that method is
  reverted, with no delivery or correction event to explain the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change and then revert a valuation method shortly after, and check whether margins computed during
  the interim window changed as a result of the revert alone.
```

## G08-SALE_STOCK_MARGIN-Q031

```yaml
QID: G08-SALE_STOCK_MARGIN-Q031
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When an order line is delivered from a stock location whose valuation setting differs from the
  item's default, the margin reflects the cost actually recorded at the location that fulfilled it,
  not the default location's cost.
WHY_IT_MATTERS: >
  Using the wrong location's cost misstates the profitability of a shipment that never actually
  passed through the default location.
DISCONFIRMING_OBSERVATION: >
  A delivery fulfilled from a non-default location shows a margin matching the default location's
  cost rather than the fulfilling location's own recorded cost.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Fulfill a delivery from a non-default location with a different valuation setting and compare the
  margin to each location's recorded cost.
```

## G08-SALE_STOCK_MARGIN-Q032

```yaml
QID: G08-SALE_STOCK_MARGIN-Q032
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a single order is fulfilled by splitting delivery across two locations with different
  valuation settings, the order-level margin correctly attributes each portion to its actual
  fulfilling location's cost.
WHY_IT_MATTERS: >
  Misattributing a split delivery's cost across locations produces an order-level figure that does
  not correspond to what actually happened at either location.
DISCONFIRMING_OBSERVATION: >
  An order split across two locations with different valuation settings shows an order-level margin
  that does not correctly combine each location's actual contribution.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Split a delivery across two locations with different valuation settings and independently verify
  the order-level margin against each location's actual cost.
```

## G08-SALE_STOCK_MARGIN-Q033

```yaml
QID: G08-SALE_STOCK_MARGIN-Q033
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The profitability consequence of choosing which location fulfills a specific delivery is visible
  to the person making that choice before the choice is finalized, rather than only becoming visible
  afterward.
WHY_IT_MATTERS: >
  A consequence only visible after the fact removes any ability to make an informed fulfillment
  decision when more than one location could serve the order.
DISCONFIRMING_OBSERVATION: >
  A person choosing between two eligible fulfilling locations with different valuation settings has
  no way to see the margin consequence of either choice before committing to one.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Present a delivery eligible for fulfillment from either of two locations with different valuation
  settings and check whether the margin consequence of each choice is visible beforehand.
```

## G08-SALE_STOCK_MARGIN-Q034

```yaml
QID: G08-SALE_STOCK_MARGIN-Q034
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When a location's valuation setting changes after stock has already been received there but
  before it is shipped, a delivery from that stock uses a consistently defined and disclosed choice
  between the setting in effect at receipt and the setting in effect at shipment.
WHY_IT_MATTERS: >
  An inconsistent or undisclosed choice between the two moments produces a cost figure that cannot
  be reproduced or explained after the fact.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical shipments from stock received before a location valuation-setting change
  use different rules for which setting applies, with neither documented.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a location's valuation setting after receiving stock there but before shipping it, then ship
  and check which setting governed the margin.
```

## G08-SALE_STOCK_MARGIN-Q035

```yaml
QID: G08-SALE_STOCK_MARGIN-Q035
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  In a multi-company setup where locations belonging to different companies use different valuation
  settings, a cross-location delivery applies the fulfilling location's own company's valuation
  setting rather than the ordering company's.
WHY_IT_MATTERS: >
  Applying the wrong company's valuation rule to a cross-company fulfillment misstates the cost
  actually borne by the company that physically shipped the goods.
DISCONFIRMING_OBSERVATION: >
  A cross-company delivery's margin reflects the ordering company's valuation setting rather than the
  fulfilling company's own setting.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Fulfill a cross-company delivery where the two companies have different valuation settings and
  check which company's setting the margin reflects.
```

## G08-SALE_STOCK_MARGIN-Q036

```yaml
QID: G08-SALE_STOCK_MARGIN-Q036
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a location is reclassified from one valuation setting to another with existing stock already
  on hand, which specific units of stock were reclassified is traceable, so a subsequent shipment's
  margin can be explained.
WHY_IT_MATTERS: >
  An untraceable reclassification of on-hand stock makes any subsequent margin change impossible to
  explain to someone reviewing it later.
DISCONFIRMING_OBSERVATION: >
  A shipment's margin reflects a reclassified valuation setting for on-hand stock, but no record
  shows which units were reclassified or when.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reclassify a location's valuation setting with existing stock on hand, then ship from that stock and
  search for a record of which units were reclassified.
```

## G08-SALE_STOCK_MARGIN-Q037

```yaml
QID: G08-SALE_STOCK_MARGIN-Q037
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a revaluation of already-delivered stock occurs after delivery but before the corresponding
  invoice is issued, the invoice-time margin reflects the revalued cost rather than the
  pre-revaluation cost that was current at the moment of delivery.
WHY_IT_MATTERS: >
  An invoice that ignores a revaluation that happened before it was issued books a margin the
  business already knew, at that point, to be wrong.
DISCONFIRMING_OBSERVATION: >
  An invoice issued after a revaluation shows a margin based on the pre-revaluation cost rather than
  the revalued figure that was current when the invoice was issued.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Deliver an order, revalue the shipped stock before invoicing, then invoice and check which cost the
  invoice-time margin used.
```

## G08-SALE_STOCK_MARGIN-Q038

```yaml
QID: G08-SALE_STOCK_MARGIN-Q038
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A revaluation occurring in the gap between delivery and invoicing leaves an auditable record
  distinguishing the delivery-time cost from the revalued cost that the invoice ultimately used.
WHY_IT_MATTERS: >
  Without both values on record, a margin figure that changed between delivery and invoicing cannot
  be explained to someone reconciling the two.
DISCONFIRMING_OBSERVATION: >
  After a delivery-to-invoice-gap revaluation, no record distinguishes the delivery-time cost from
  the revalued cost the invoice used.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Revalue stock between delivery and invoicing and search for a record showing both the delivery-time
  and revalued cost.
```

## G08-SALE_STOCK_MARGIN-Q039

```yaml
QID: G08-SALE_STOCK_MARGIN-Q039
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a revaluation occurs after some lines of a multi-line order have already been invoiced and
  others have not, the revaluation affects only the not-yet-invoiced lines' margin, leaving the
  already-invoiced lines undisturbed.
WHY_IT_MATTERS: >
  Disturbing an already-invoiced line's margin after the fact restates a financial event the business
  already closed out.
DISCONFIRMING_OBSERVATION: >
  A revaluation changes the margin of a line that was already invoiced before the revaluation
  occurred.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Invoice one line of a multi-line order, leave another uninvoiced, revalue the underlying stock, and
  check whether the already-invoiced line's margin changed.
```

## G08-SALE_STOCK_MARGIN-Q040

```yaml
QID: G08-SALE_STOCK_MARGIN-Q040
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an invoice is issued before any revaluation occurs and the revaluation happens afterward, the
  already-issued invoice's recorded margin remains frozen rather than silently reflecting the later
  revaluation.
WHY_IT_MATTERS: >
  A margin that moves after the invoice was already issued restates a document the customer and the
  ledger both already treated as final.
DISCONFIRMING_OBSERVATION: >
  An already-issued invoice's recorded margin changes after a revaluation that occurred after the
  invoice was issued.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue an invoice, then revalue the underlying stock afterward, and check whether the invoice's
  recorded margin changed.
```

## G08-SALE_STOCK_MARGIN-Q041

```yaml
QID: G08-SALE_STOCK_MARGIN-Q041
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a revaluation in the delivery-to-invoice gap changes the sign of a line's margin from
  positive to negative, that sign change is specifically flagged rather than blending unnoticed into
  an aggregate figure.
WHY_IT_MATTERS: >
  A line that quietly flips to a loss inside an aggregate is exactly the kind of change that most
  needs a reviewer's attention and is most likely to be missed without a flag.
DISCONFIRMING_OBSERVATION: >
  A line whose margin sign flips from positive to negative due to a delivery-to-invoice-gap
  revaluation shows no distinct flag anywhere a reviewer would see it.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Revalue stock in the delivery-to-invoice gap so that a line's margin sign flips, and check for a
  flag on that specific change.
```

## G08-SALE_STOCK_MARGIN-Q042

```yaml
QID: G08-SALE_STOCK_MARGIN-Q042
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A revaluation event occurring in the delivery-to-invoice gap applies consistently to every order
  awaiting invoicing for the affected item, rather than to some orders and not others depending on
  the order in which they happen to be processed.
WHY_IT_MATTERS: >
  Inconsistent application across otherwise identical waiting orders means the same revaluation event
  produces different, unexplainable outcomes for equivalent transactions.
DISCONFIRMING_OBSERVATION: >
  Two orders equally awaiting invoicing for the same revalued item show inconsistent treatment of
  the revaluation, with one reflecting it and the other not.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Revalue an item while two orders for it are both awaiting invoicing, then invoice both and compare
  how each reflects the revaluation.
```

## G08-SALE_STOCK_MARGIN-Q043

```yaml
QID: G08-SALE_STOCK_MARGIN-Q043
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a delivery is fulfilled from stock that has gone negative and is valued at an estimated cost
  pending replenishment, the resulting margin is marked as based on an estimate rather than presented
  identically to a margin based on a known, received cost.
WHY_IT_MATTERS: >
  A figure that looks final but rests on a guess can lead to decisions made with more confidence than
  the underlying data actually supports.
DISCONFIRMING_OBSERVATION: >
  A delivery fulfilled from negative, estimate-valued stock shows a margin with no indication that
  its cost basis is an estimate.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Fulfill a delivery from stock that has gone negative and is valued at an estimate, then inspect the
  resulting margin for an estimate indication.
```

## G08-SALE_STOCK_MARGIN-Q044

```yaml
QID: G08-SALE_STOCK_MARGIN-Q044
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the actual replenishment cost later becomes known for stock that was shipped at an estimated
  cost while negative, the previously estimated margin is corrected, and that correction is traceable
  to the specific delivery it affects.
WHY_IT_MATTERS: >
  An estimate that is never reconciled to the real cost once it becomes known leaves a permanently
  wrong figure on record with no path to fix it.
DISCONFIRMING_OBSERVATION: >
  The actual replenishment cost becomes known for previously negative stock, but the margin of the
  delivery that shipped at the estimated cost is never corrected or the correction cannot be traced
  to that delivery.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Ship from negative, estimate-valued stock, then replenish it with a known actual cost, and check
  whether the earlier delivery's margin is corrected and traceably so.
```

## G08-SALE_STOCK_MARGIN-Q045

```yaml
QID: G08-SALE_STOCK_MARGIN-Q045
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order margin based on an estimated negative-stock cost is excluded from, or specially flagged
  within, any approval threshold or report that assumes its inputs are known facts rather than
  estimates.
WHY_IT_MATTERS: >
  Treating an estimate exactly like a fact in a threshold or report lets a decision be made on
  confidence the data does not actually support.
DISCONFIRMING_OBSERVATION: >
  An order margin resting on an estimated negative-stock cost passes through an approval threshold or
  appears in a report identically to one based on a known cost, with no distinguishing indication.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Produce an order margin based on an estimated negative-stock cost and check how it is treated by an
  approval threshold or report compared to a known-cost margin.
```

## G08-SALE_STOCK_MARGIN-Q046

```yaml
QID: G08-SALE_STOCK_MARGIN-Q046
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When multiple deliveries are fulfilled from the same negative-stock position before it is
  replenished, each one carries its own individually traceable estimate rather than all of them
  silently sharing one blended assumption that may not match any of them once resolved.
WHY_IT_MATTERS: >
  A shared, untraceable assumption across several deliveries means correcting it later cannot be
  attributed fairly or accurately to each individual delivery.
DISCONFIRMING_OBSERVATION: >
  Several deliveries fulfilled from the same negative-stock position cannot be individually traced to
  their own estimate once the position is replenished and corrected.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Fulfill several deliveries from the same negative-stock position, then replenish it and attempt to
  trace each delivery's own estimate individually.
```

## G08-SALE_STOCK_MARGIN-Q047

```yaml
QID: G08-SALE_STOCK_MARGIN-Q047
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the negative-stock estimate mechanism activates due to a data or timing artifact rather than
  a genuine shortfall, that circumstance is distinguishable after the fact from a genuine
  negative-stock estimate.
WHY_IT_MATTERS: >
  Conflating an artifact with a genuine shortfall means a data-quality problem and a real supply
  problem get treated, and investigated, identically.
DISCONFIRMING_OBSERVATION: >
  A margin flagged as based on a negative-stock estimate provides no way to tell whether the
  underlying negative position was a genuine shortfall or a data or timing artifact.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce a negative-stock estimate situation arising from a timing artifact rather than a genuine
  shortfall, and check whether that distinction is discoverable afterward.
```

## G08-SALE_STOCK_MARGIN-Q048

```yaml
QID: G08-SALE_STOCK_MARGIN-Q048
MODULE: sale_stock_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When negative stock is finally replenished and its estimate is corrected, the correction to
  already-recognized margin lands in an identifiable accounting period rather than silently altering
  a period already considered closed.
WHY_IT_MATTERS: >
  A silent alteration to a closed period's figures undermines the finality that a period close is
  supposed to represent.
DISCONFIRMING_OBSERVATION: >
  A correction to a previously estimated negative-stock margin changes the reported figure for an
  already-closed accounting period with no new, identifiable entry marking the correction.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Correct a negative-stock estimate after the accounting period in which it was originally recognized
  has closed, and check whether the correction lands as an identifiable new entry.
```
