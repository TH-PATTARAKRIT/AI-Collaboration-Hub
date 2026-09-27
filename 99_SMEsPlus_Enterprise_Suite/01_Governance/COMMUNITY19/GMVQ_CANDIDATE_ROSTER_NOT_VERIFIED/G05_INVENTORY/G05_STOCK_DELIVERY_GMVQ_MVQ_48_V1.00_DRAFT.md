# SMEsPlus ENTERPRISE SUITE
## GMVQ — G05 INVENTORY / stock_delivery Module Adversarial MVQ Bank

**Document ID:** GMVQ-G05-STOCK_DELIVERY-MVQ48-V1.00
**Group:** G05 INVENTORY
**Module Metadata:** `stock_delivery`
**Wave:** W2
**Author Cell:** TEAM P03 (GMVQ Question Factory — Production Cell P03, Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This module is the seam by which an outbound stock movement acquires a carrier, a shipping cost, and a
tracked shipment. This bank supplements the 55 Standard Questions with module-specific, adversarial
questions covering: the shipping cost quoted at order time versus charged at dispatch versus invoiced by
the carrier, and who absorbs the difference; weight and dimensions derived from the goods being wrong or
absent; a carrier rejecting the shipment after the movement was validated; a shipment split across several
packages while the underlying movement is not; a tracking identity issued and then the movement cancelled;
a delivery address changed after label generation; the carrier's own state and the internal state
disagreeing about whether goods left; per-company carrier configuration; cost booked to the correct period
when dispatch and invoice straddle a close; and returns travelling back through the same seam.

Per the Bridge Module Rule (V1.00), this module owns almost no behaviour of its own: every question below
targets a point where the seam itself could disagree with itself, not a restatement of stock movement
behaviour or of carrier behaviour taken alone. Question text is source-neutral: no vendor or product name,
no technical identifier (model, table, field, method, XML ID, API path), and no reference to how any
specific implementation is built. Language is generic business/behavioural language throughout.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, cross-module dependency, auditability, tenant/company boundary,
  concurrency and ordering, and runtime/configuration reachability.
- This module carries both a configuration layer (carrier setup, per-company scoping, pricing basis) and a
  runtime process layer (what happens at and after dispatch); each question is tagged `LAYER: BASE` or
  `LAYER: PROCESS` accordingly.
- Pre-authoring sibling check (Bridge Module Rule §5): `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G05_INVENTORY/*.md`
  was run before authoring. At the time this bank was authored, no other G05 INVENTORY bank existed on
  disk, so there were no sibling HYPOTHESIS lines to check against.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a
  Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G05-STOCK_DELIVERY-Q001

```yaml
QID: G05-STOCK_DELIVERY-Q001
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When the amount the carrier actually invoices for a shipment differs from the amount estimated and
  charged to the customer at booking time, the difference is recorded as an identifiable variance rather
  than silently absorbed into the original estimated figure.
WHY_IT_MATTERS: >
  If the variance is not identifiable, margin erosion on shipping recovery accumulates unnoticed across
  many shipments until a period review, by which point the cause cannot be traced to individual shipments.
DISCONFIRMING_OBSERVATION: >
  The carrier's actual invoiced amount for a shipment is recorded, but the original estimated/charged
  amount is overwritten with no trace of the two figures or their difference.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Book a shipment with an estimated cost, then supply a different actual carrier-invoiced amount for the
  same shipment and inspect what is retained.
```

## G05-STOCK_DELIVERY-Q002

```yaml
QID: G05-STOCK_DELIVERY-Q002
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The shipping cost estimate produced at order time and the cost actually applied at the moment of
  dispatch are two independently held figures, so a change in carrier pricing between order and dispatch
  does not silently rewrite what was already quoted to the customer.
WHY_IT_MATTERS: >
  If dispatch-time repricing silently overwrites the quoted figure, a customer-facing commitment changes
  without anyone deciding to change it.
DISCONFIRMING_OBSERVATION: >
  The figure originally quoted to the customer at order time is replaced by the dispatch-time price with
  no record that a different figure was once quoted.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change the applicable carrier rate between order placement and dispatch of the same order, then compare
  the quoted and dispatch-time figures retained on the record.
```

## G05-STOCK_DELIVERY-Q003

```yaml
QID: G05-STOCK_DELIVERY-Q003
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether the customer or the business absorbs a shortfall between the quoted shipping charge and the
  carrier's actual invoice is a configurable business rule, not a hard-coded behaviour that applies
  uniformly regardless of the situation.
WHY_IT_MATTERS: >
  A business that only sometimes wants to absorb the variance (for example, only above a threshold, or
  only for certain carriers) cannot express that policy if the behaviour is fixed.
DISCONFIRMING_OBSERVATION: >
  There is no configuration point governing who absorbs a shipping cost variance; the outcome is fixed in
  one direction regardless of any setting.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Search the available configuration for a setting governing shipping cost variance allocation and attempt
  to change its outcome.
```

## G05-STOCK_DELIVERY-Q004

```yaml
QID: G05-STOCK_DELIVERY-Q004
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A shipment for which the carrier's final invoice has still not arrived is distinguishable, on the
  record, from one where the invoiced amount has been confirmed, rather than both looking identical once
  the estimated charge was applied.
WHY_IT_MATTERS: >
  Without that distinction, nobody can tell which shipments still carry an unconfirmed cost exposure, and
  a systematic under-quote could go undetected indefinitely.
DISCONFIRMING_OBSERVATION: >
  A shipment awaiting carrier invoice confirmation and one with a confirmed invoice show the same status
  and cannot be told apart without manually checking each one externally.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create one shipment with only an estimated cost and another with a confirmed carrier invoice amount,
  then compare what each looks like on the record.
```

## G05-STOCK_DELIVERY-Q005

```yaml
QID: G05-STOCK_DELIVERY-Q005
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Multiple candidate rates from more than one carrier option can be compared before a shipment is booked,
  and the rate actually selected is the one recorded as charged, not silently substituted for a different
  candidate's rate.
WHY_IT_MATTERS: >
  If the recorded charge doesn't match the option that was actually chosen, cost reporting per carrier
  becomes unreliable.
DISCONFIRMING_OBSERVATION: >
  The amount recorded as charged for the shipment corresponds to a different carrier option than the one
  the operator actually selected.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Obtain rate options from more than one carrier for the same movement, select one deliberately, and
  verify which rate is recorded as charged.
```

## G05-STOCK_DELIVERY-Q006

```yaml
QID: G05-STOCK_DELIVERY-Q006
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The weight used to obtain a shipping cost estimate is derived from the actual goods on the movement, and
  a product carrying no weight information produces a visible gap or exception rather than a silent zero
  that understates the estimate.
WHY_IT_MATTERS: >
  A silent zero-weight assumption systematically underprices heavy shipments, and the underpricing is
  invisible until the carrier's own invoice arrives.
DISCONFIRMING_OBSERVATION: >
  A movement containing a product with no recorded weight produces a shipping cost estimate as if the item
  weighed nothing, with no warning or exception raised.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Include a product with no weight recorded on a movement being handed to a carrier and observe the
  resulting cost estimate and any warning.
```

## G05-STOCK_DELIVERY-Q007

```yaml
QID: G05-STOCK_DELIVERY-Q007
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When several distinct goods with different weights are combined on one movement, the weight passed to
  the carrier reflects the sum of what is actually being shipped on that movement, not a fixed
  per-movement assumption or only the first line.
WHY_IT_MATTERS: >
  An estimate based on only part of the shipment's contents misrepresents the shipment to the carrier and
  to the cost estimate alike.
DISCONFIRMING_OBSERVATION: >
  A movement with several product lines of differing weight produces a shipping weight equal to only one
  line's weight rather than the combined total.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Build a movement with several product lines of different, known weights and inspect the total weight
  passed toward the carrier interaction.
```

## G05-STOCK_DELIVERY-Q008

```yaml
QID: G05-STOCK_DELIVERY-Q008
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A change to the quantity actually picked, made after an initial weight-based estimate was produced but
  before the shipment is finally booked, is reflected in a refreshed weight and cost rather than the
  shipment going out priced against a quantity that no longer matches what left.
WHY_IT_MATTERS: >
  A picking shortage or substitution that isn't reflected in the shipping cost basis creates a mismatch
  that surfaces only when the carrier's invoice contradicts what was booked.
DISCONFIRMING_OBSERVATION: >
  The quantity actually picked differs from the quantity used for the shipping estimate, and the shipment
  is booked and dispatched without the estimate being refreshed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Reduce or change the picked quantity on a movement after its initial shipping estimate was produced,
  then proceed to booking and compare the two figures.
```

## G05-STOCK_DELIVERY-Q009

```yaml
QID: G05-STOCK_DELIVERY-Q009
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether dimensions (not only weight) are required and used in the shipping cost computation is a
  configurable expectation per carrier, since some carriers price by weight alone and others by volumetric
  measurement, rather than one fixed formula applied to every carrier.
WHY_IT_MATTERS: >
  Applying a single weight-only formula to a carrier that actually prices volumetrically produces
  systematically wrong estimates for that carrier's shipments.
DISCONFIRMING_OBSERVATION: >
  The same computation method is applied regardless of which carrier is selected, with no way to configure
  a carrier that prices on volume instead of weight.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Configure two different carriers with different stated pricing bases (weight versus volumetric) and
  compare the cost computation each produces for an identical movement.
```

## G05-STOCK_DELIVERY-Q010

```yaml
QID: G05-STOCK_DELIVERY-Q010
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a carrier rejects a shipment (for example, an undeliverable address or a prohibited item) after the
  underlying stock movement has already been validated and the goods logically left, the movement's own
  state is corrected or flagged rather than being left showing the goods as gone while the carrier
  confirms nothing was ever collected.
WHY_IT_MATTERS: >
  Stock that is neither in the warehouse nor genuinely in transit, yet recorded as shipped, is invisible
  to inventory and cannot be found, reordered around, or accounted for correctly.
DISCONFIRMING_OBSERVATION: >
  The movement remains recorded as validated and complete after the carrier has rejected the shipment,
  with no distinguishable state and no prompt to resolve the goods' actual location.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Simulate a carrier rejection after a movement was validated and observe whether the movement's state
  changes or a resolution path is offered.
```

## G05-STOCK_DELIVERY-Q011

```yaml
QID: G05-STOCK_DELIVERY-Q011
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A carrier rejection can be acted on without requiring the entire original movement to be undone and
  re-created from scratch; a path exists to correct the shipment (re-book, return to stock, or re-address)
  that preserves the movement's history.
WHY_IT_MATTERS: >
  Forcing a full undo-and-redo on every rejection discards the audit trail of what actually happened to
  that shipment and multiplies operator effort for a routine exception.
DISCONFIRMING_OBSERVATION: >
  The only available response to a carrier rejection is deleting or fully reversing the original movement
  with no record connecting the rejected attempt to what replaces it.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Trigger a carrier rejection on a validated movement and attempt to resolve it, observing whether the
  history of the rejected attempt is preserved.
```

## G05-STOCK_DELIVERY-Q012

```yaml
QID: G05-STOCK_DELIVERY-Q012
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If a shipping cost was already charged to the customer or booked internally before the carrier's
  rejection became known, that charge is reversed or held pending resolution rather than remaining posted
  as if the shipment succeeded.
WHY_IT_MATTERS: >
  A charge left standing for a shipment that never happened overstates recognised shipping revenue or cost
  recovery.
DISCONFIRMING_OBSERVATION: >
  The shipping charge tied to a rejected shipment remains posted unchanged with no linkage prompting its
  review after the rejection is recorded.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Book and charge a shipment, then simulate the carrier rejecting it, and inspect what happens to the
  already-recorded charge.
```

## G05-STOCK_DELIVERY-Q013

```yaml
QID: G05-STOCK_DELIVERY-Q013
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A shipment rejected for a reason outside the business's control (a prohibited item, an address the
  carrier cannot serve) is distinguishable, in what is recorded, from a shipment that failed because of an
  internal data problem (bad weight, missing reference), since the two call for different corrective
  action.
WHY_IT_MATTERS: >
  Treating carrier-side and internal-data-side failures identically means the wrong team resolves the
  wrong class of problem, or nobody resolves either.
DISCONFIRMING_OBSERVATION: >
  A carrier-side rejection and an internally-caused booking failure are recorded with the same generic
  failure indication, with nothing distinguishing which side caused it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce one rejection caused by a carrier-side reason and one caused by an internal data problem, then
  compare how each is recorded.
```

## G05-STOCK_DELIVERY-Q014

```yaml
QID: G05-STOCK_DELIVERY-Q014
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When one stock movement is packed into several physical parcels for a carrier, each parcel's own
  tracking identity is retained against that one movement, rather than only the last parcel's identity
  surviving or the movement holding a single tracking value that cannot represent more than one parcel.
WHY_IT_MATTERS: >
  Losing all but one tracking identity on a multi-parcel shipment makes it impossible to trace or resolve
  a claim for whichever parcel goes missing.
DISCONFIRMING_OBSERVATION: >
  A movement split into several parcels for shipping ends up associated with only one tracking identity,
  with the others unrecorded or overwritten.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Split one validated movement into several parcels for a single carrier shipment and inspect what
  tracking information is retained per parcel.
```

## G05-STOCK_DELIVERY-Q015

```yaml
QID: G05-STOCK_DELIVERY-Q015
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The total shipping cost for a movement split across several parcels is not silently duplicated per
  parcel nor silently divided without basis; the total charged corresponds to what the carrier actually
  charges for the combined shipment.
WHY_IT_MATTERS: >
  A naive per-parcel cost duplication would overstate the true shipping expense every time a shipment
  needs more than one box.
DISCONFIRMING_OBSERVATION: >
  Splitting a shipment into multiple parcels multiplies the recorded shipping cost by the parcel count
  rather than reflecting the carrier's actual combined charge.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split a shipment into multiple parcels with a known combined carrier charge and compare that charge to
  what is recorded on the movement.
```

## G05-STOCK_DELIVERY-Q016

```yaml
QID: G05-STOCK_DELIVERY-Q016
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If one parcel of a multi-parcel shipment is lost or damaged in transit, the movement supports recording
  that partial loss against the specific parcel affected, rather than forcing an all-or-nothing resolution
  across the entire movement.
WHY_IT_MATTERS: >
  Forcing an all-or-nothing resolution either overstates a loss that only affected part of the shipment,
  or leaves a genuine partial loss unrecorded because the tool cannot express it.
DISCONFIRMING_OBSERVATION: >
  The only way to record a lost parcel is to treat the entire multi-parcel movement as lost, or there is
  no way to record a partial-parcel loss at all.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to record that only one of several parcels belonging to one movement was lost or damaged, and
  observe what granularity is available.
```

## G05-STOCK_DELIVERY-Q017

```yaml
QID: G05-STOCK_DELIVERY-Q017
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  The decision to split a shipment into multiple parcels can be driven by a genuine physical limit (weight
  or size per parcel) rather than being an arbitrary operator choice with no relationship to what a
  carrier will actually accept in one parcel.
WHY_IT_MATTERS: >
  A parcel that exceeds what the carrier will actually accept is rejected at the carrier's own point of
  intake, after the business has already committed the movement.
DISCONFIRMING_OBSERVATION: >
  A single-parcel shipment can be booked and handed to the carrier even though its combined weight or size
  is far beyond any stated per-parcel limit for that carrier, with no warning.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Attempt to book a single parcel that clearly exceeds a configured carrier limit and observe whether any
  warning or block occurs.
```

## G05-STOCK_DELIVERY-Q018

```yaml
QID: G05-STOCK_DELIVERY-Q018
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a movement for which a carrier tracking identity has already been issued is subsequently
  cancelled, the shipment is also cancelled or voided with the carrier, rather than the internal
  cancellation leaving an active shipment label and tracking number the carrier still expects to see
  collected.
WHY_IT_MATTERS: >
  An uncancelled label left active with the carrier can result in a real collection or a charge for a
  shipment the business no longer intends to send.
DISCONFIRMING_OBSERVATION: >
  Cancelling a movement that already has a carrier tracking identity leaves that identity active, with no
  attempt or prompt to void it with the carrier.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Issue a tracking identity for a movement, then cancel the movement, and observe what happens to the
  carrier-side shipment.
```

## G05-STOCK_DELIVERY-Q019

```yaml
QID: G05-STOCK_DELIVERY-Q019
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A tracking identity, once issued, is retained on the movement's record even if the movement is later
  cancelled, so that the history of what was attempted is not lost along with the cancellation.
WHY_IT_MATTERS: >
  Losing the tracking identity on cancellation destroys the only link available to confirm with the
  carrier that a void actually took effect.
DISCONFIRMING_OBSERVATION: >
  Cancelling a movement clears or removes the tracking identity that had already been issued for it,
  leaving no record that a shipment attempt occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Issue a tracking identity, cancel the movement, and check whether the tracking identity is still visible
  on the movement's record.
```

## G05-STOCK_DELIVERY-Q020

```yaml
QID: G05-STOCK_DELIVERY-Q020
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Requesting a new tracking identity for a movement that already holds an active one produces a
  deliberate replacement or an explicit block, rather than silently issuing a second, parallel identity
  that leaves two labels claiming to represent the same physical movement.
WHY_IT_MATTERS: >
  Two live tracking identities for one movement can result in two collections, two charges, or confusion
  about which label the carrier actually honours.
DISCONFIRMING_OBSERVATION: >
  A second tracking identity is issued for a movement that already has one, with both remaining recorded
  as active with no resolution or warning.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Trigger a second carrier booking request for a movement that already has an active tracking identity,
  and observe the outcome.
```

## G05-STOCK_DELIVERY-Q021

```yaml
QID: G05-STOCK_DELIVERY-Q021
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Reprinting or re-fetching an existing shipping label for a movement returns the same tracking identity
  already on record, rather than silently generating a new carrier booking each time the label is
  reprinted.
WHY_IT_MATTERS: >
  A new booking created on every reprint could produce multiple chargeable shipments, or multiple tracking
  identities, for what the operator understood to be one reprint of one label.
DISCONFIRMING_OBSERVATION: >
  Reprinting the label for a movement that already has a tracking identity results in a new, different
  tracking identity being issued.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Print a shipping label for a booked movement, then request the label again, and compare the tracking
  identity each time.
```

## G05-STOCK_DELIVERY-Q022

```yaml
QID: G05-STOCK_DELIVERY-Q022
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Every carrier tracking identity ever issued against a movement remains traceable in the movement's own
  history, even after it has been superseded or voided, rather than only the current, most recent
  identity being visible.
WHY_IT_MATTERS: >
  Investigating a shipping dispute after the fact requires knowing every identity that was ever issued for
  that movement, not only the last one.
DISCONFIRMING_OBSERVATION: >
  A movement that has had more than one tracking identity issued over its life (through cancellation and
  rebooking) shows only the latest one, with earlier identities not retrievable from the record.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Cause a movement to go through more than one tracking identity (void and rebook), then check whether the
  full sequence remains visible.
```

## G05-STOCK_DELIVERY-Q023

```yaml
QID: G05-STOCK_DELIVERY-Q023
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Changing the delivery address on a movement after a shipping label carrying the original address has
  already been generated is either blocked, or triggers an explicit re-generation of the label and
  shipment, rather than silently updating the address on the record while the physical label the carrier
  will use still shows the old one.
WHY_IT_MATTERS: >
  A physical label mismatched to the address now recorded internally sends the shipment to the wrong place
  while every internal report shows the corrected address.
DISCONFIRMING_OBSERVATION: >
  The delivery address is changed on a movement after its label was generated, the label is not
  regenerated or flagged, and the record shows the new address as if it were what was actually shipped to.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Generate a shipping label for a movement, then change the delivery address on the same movement, and
  observe whether the label or shipment reacts.
```

## G05-STOCK_DELIVERY-Q024

```yaml
QID: G05-STOCK_DELIVERY-Q024
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An address change made before dispatch but after a carrier booking was already confirmed is
  communicated to the carrier (through a re-booking or an update request) rather than only being updated
  in the internal record with the carrier left unaware.
WHY_IT_MATTERS: >
  A carrier acting on stale address information delivers to a location the customer or business no longer
  intends.
DISCONFIRMING_OBSERVATION: >
  The internal record shows the corrected address while nothing indicates the carrier was ever informed of
  the change.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Confirm a carrier booking, then change the delivery address before dispatch, and check for any
  carrier-facing update.
```

## G05-STOCK_DELIVERY-Q025

```yaml
QID: G05-STOCK_DELIVERY-Q025
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If an address change after label generation results in an additional carrier charge (a redirection
  fee), that additional cost is captured against the shipment rather than being absent from the record
  entirely.
WHY_IT_MATTERS: >
  An unrecorded redirection charge understates the true cost of that shipment and cannot be reconciled
  against the carrier's own invoice later.
DISCONFIRMING_OBSERVATION: >
  A carrier-imposed redirection charge following an address change is never reflected anywhere on the
  shipment's own cost record.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Simulate an address change after label generation that would incur a carrier redirection fee, and check
  whether that fee is captured.
```

## G05-STOCK_DELIVERY-Q026

```yaml
QID: G05-STOCK_DELIVERY-Q026
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Whether an address change is still allowed depends on where the movement actually is in its lifecycle
  (before booking, after booking, after physical dispatch), rather than the system allowing or blocking
  address edits identically at every stage.
WHY_IT_MATTERS: >
  Allowing an unrestricted address edit after the goods have physically left cannot change where a truck
  has already gone, and gives a false impression that the correction took effect.
DISCONFIRMING_OBSERVATION: >
  The delivery address can be edited on a movement that has already been marked as physically dispatched,
  with no distinction from editing it before booking.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attempt to edit the delivery address at each of several lifecycle stages (before booking, after booking,
  after dispatch) and compare what is allowed.
```

## G05-STOCK_DELIVERY-Q027

```yaml
QID: G05-STOCK_DELIVERY-Q027
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When the carrier's own tracking status contradicts the internal movement's state (for example, the
  carrier shows the parcel delivered while the internal record still shows it awaiting dispatch, or the
  reverse), that contradiction is surfaced as something to resolve rather than one of the two states being
  blindly trusted and the other left stale and misleading.
WHY_IT_MATTERS: >
  A silent, unresolved contradiction between the two sources means neither can be trusted, and whichever
  one a downstream process reads (invoicing, customer notification) may be the wrong one.
DISCONFIRMING_OBSERVATION: >
  The internal movement state and the carrier's own reported status disagree about whether the goods have
  left, and nothing in the record indicates the disagreement exists.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Force a mismatch between the internal movement state and a carrier-reported status for the same
  shipment, then check whether the disagreement is visible anywhere.
```

## G05-STOCK_DELIVERY-Q028

```yaml
QID: G05-STOCK_DELIVERY-Q028
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The internal movement is not automatically flipped to a "delivered" or "shipped" state purely because
  the carrier's tracking feed reports that status; an internal act (or an explicit, auditable
  synchronisation rule) governs the movement's own state.
WHY_IT_MATTERS: >
  If the carrier's feed alone can silently close out an internal movement, an error or a compromised feed
  on the carrier's side can misstate the business's own inventory position.
DISCONFIRMING_OBSERVATION: >
  The internal movement's state changes to reflect a carrier feed status with no auditable event or
  configured rule explaining why it changed.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Have the carrier feed report a status change for a shipment and observe whether and how the internal
  movement's own state reacts.
```

## G05-STOCK_DELIVERY-Q029

```yaml
QID: G05-STOCK_DELIVERY-Q029
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a carrier's tracking status is unavailable or the carrier's system cannot be reached, the
  movement's own recorded state is unaffected and clearly distinguishable from a state that has been
  positively confirmed by the carrier.
WHY_IT_MATTERS: >
  Treating "carrier unreachable" the same as "carrier confirmed" hides a genuine unknown behind a false
  confirmation.
DISCONFIRMING_OBSERVATION: >
  A period where the carrier's tracking feed could not be reached results in the movement showing the same
  confirmed status it would show if the carrier had actually confirmed delivery.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Simulate the carrier's tracking feed being unreachable for a period and compare the movement's state to
  one where the carrier positively confirmed the same status.
```

## G05-STOCK_DELIVERY-Q030

```yaml
QID: G05-STOCK_DELIVERY-Q030
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A shipment that the carrier marks as an exception (delayed, held at a facility, returned to sender by
  the carrier's own decision) is reflected as a distinct state internally, rather than being folded into
  either "in transit" or "delivered" with no visibility of the exception.
WHY_IT_MATTERS: >
  A shipment silently sitting in an exception state looks, internally, exactly like one proceeding
  normally, delaying any response to a problem that is already known to the carrier.
DISCONFIRMING_OBSERVATION: >
  A carrier-reported exception status for a shipment produces no visible difference from a normal
  in-transit shipment on the internal record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Simulate a carrier exception status (delay, hold, carrier-initiated return) and compare the resulting
  internal record to a normal in-transit shipment.
```

## G05-STOCK_DELIVERY-Q031

```yaml
QID: G05-STOCK_DELIVERY-Q031
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Whichever side (internal record or carrier feed) is authoritative for a movement's delivery state is a
  documented, applied rule, not an unstated assumption that differs depending on which screen or report
  someone happens to look at.
WHY_IT_MATTERS: >
  Without a documented authority, two people investigating the same shipment can reach opposite, equally
  defensible conclusions about whether it was delivered.
DISCONFIRMING_OBSERVATION: >
  Two different views of the same shipment's delivery status (one sourced from the internal record, one
  from the carrier feed) disagree, and neither is marked as the authoritative one.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Locate two different places the delivery status of the same shipment can be viewed and compare them
  after forcing a disagreement between sources.
```

## G05-STOCK_DELIVERY-Q032

```yaml
QID: G05-STOCK_DELIVERY-Q032
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Carrier configuration (which carriers are available, their rates and credentials) can be set
  independently per company, so that one company's carrier setup is not visible to, or usable by,
  movements belonging to a different company.
WHY_IT_MATTERS: >
  A shared carrier configuration across companies could let one company's shipments be booked, charged, or
  credentialed under an unrelated company's carrier account.
DISCONFIRMING_OBSERVATION: >
  A movement belonging to one company can select or use a carrier configuration that was set up under a
  different company.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure distinct carrier setups for two different companies, then check whether a movement in one
  company can reach the other company's carrier configuration.
```

## G05-STOCK_DELIVERY-Q033

```yaml
QID: G05-STOCK_DELIVERY-Q033
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  When a carrier account's credentials are configured, they are scoped to the company that owns them and
  are not exposed, even indirectly, to users or processes operating under a different company in the same
  environment.
WHY_IT_MATTERS: >
  Credential leakage across companies would let one company's shipments be booked and billed against
  another company's real-world carrier account.
DISCONFIRMING_OBSERVATION: >
  A carrier credential configured under one company is usable, viewable, or selectable from a context
  belonging to a different company.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Configure a carrier credential under one company and attempt to view or use it from a session or context
  belonging to a different company.
```

## G05-STOCK_DELIVERY-Q034

```yaml
QID: G05-STOCK_DELIVERY-Q034
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A warehouse or movement that legitimately belongs to more than one company context (a shared facility,
  an intercompany transfer) has a defined rule for which company's carrier configuration governs the
  shipment, rather than an ambiguous or arbitrary pick between the two.
WHY_IT_MATTERS: >
  An arbitrary pick between two companies' carrier setups could charge the wrong company or use the wrong
  company's carrier account for a shipment that legitimately touches both.
DISCONFIRMING_OBSERVATION: >
  A movement spanning two companies produces a carrier booking without any determinable rule for which
  company's configuration was actually used.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Create a movement that spans two companies (an intercompany transfer using an external carrier) and
  identify which company's carrier configuration is applied.
```

## G05-STOCK_DELIVERY-Q035

```yaml
QID: G05-STOCK_DELIVERY-Q035
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Disabling or removing a carrier's configuration for a company does not silently orphan shipments already
  booked with that carrier; existing bookings remain traceable to the configuration that was in force when
  they were made.
WHY_IT_MATTERS: >
  Losing the link between a historical shipment and the carrier configuration used at the time makes it
  impossible to explain, later, why that shipment was priced or routed the way it was.
DISCONFIRMING_OBSERVATION: >
  Removing or disabling a carrier's configuration causes existing shipments already booked with it to lose
  their reference to that configuration.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Book a shipment against a specific carrier configuration, then disable or remove that configuration, and
  check whether the existing shipment's record still shows what it used.
```

## G05-STOCK_DELIVERY-Q036

```yaml
QID: G05-STOCK_DELIVERY-Q036
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a shipment is dispatched in one accounting period but the carrier's invoice for that shipment
  arrives in a later period, the cost is recognised in a way that reflects when the shipping obligation
  actually arose, rather than automatically landing in whichever period the invoice happens to be
  processed in.
WHY_IT_MATTERS: >
  Letting invoice timing alone dictate the period misstates the cost of goods actually shipped in the
  earlier, already-closed period.
DISCONFIRMING_OBSERVATION: >
  A shipping cost for goods dispatched in one period is recognised only in the period the carrier's
  invoice was later processed, with no mechanism to attribute it back to the dispatch period.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Dispatch a shipment in one period, supply the carrier's actual invoice in a following period, and
  observe which period the cost lands in.
```

## G05-STOCK_DELIVERY-Q037

```yaml
QID: G05-STOCK_DELIVERY-Q037
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An estimated shipping cost recognised at dispatch, ahead of the carrier's actual invoice, is reconciled
  against that invoice when it arrives, with the difference visible, rather than both the estimate and the
  actual invoice being posted independently and left to accumulate as an unexplained discrepancy.
WHY_IT_MATTERS: >
  Two independently posted figures for the same shipment, never reconciled, either double-count the cost
  or leave a growing, unexplained gap in shipping expense.
DISCONFIRMING_OBSERVATION: >
  Both an estimated shipping cost and the carrier's later actual invoice are posted for the same shipment
  with nothing tying the two together or showing the variance between them.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post an estimated shipping cost at dispatch, then supply a differing actual carrier invoice for the same
  shipment, and inspect how the two are reconciled.
```

## G05-STOCK_DELIVERY-Q038

```yaml
QID: G05-STOCK_DELIVERY-Q038
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A shipment dispatched just before a period closes, whose carrier invoice has not yet been recorded, is
  still identifiable at period-end as an outstanding shipping cost exposure, rather than disappearing from
  view until the invoice eventually shows up.
WHY_IT_MATTERS: >
  An invisible, unrecorded shipping cost exposure at period close means the close itself is based on an
  understated set of obligations.
DISCONFIRMING_OBSERVATION: >
  At period close, a shipment already dispatched but not yet carrier-invoiced cannot be found on any list
  of outstanding shipping cost exposure.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Dispatch a shipment just before a period boundary without yet recording a carrier invoice, then look for
  it on whatever represents outstanding shipping cost exposure at that close.
```

## G05-STOCK_DELIVERY-Q039

```yaml
QID: G05-STOCK_DELIVERY-Q039
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A shipping cost correction discovered after the period in which the shipment was dispatched has already
  been closed is handled through an explicit adjustment in a current, open period, rather than by silently
  rewriting the figure inside the already-closed period.
WHY_IT_MATTERS: >
  Silently rewriting a closed period's figures invalidates whatever was already reported and reconciled
  for that period.
DISCONFIRMING_OBSERVATION: >
  Correcting a shipping cost for a shipment dispatched in an already-closed period changes the figures
  recorded inside that closed period rather than posting the correction in an open one.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Close a period containing a dispatched shipment, then attempt to correct that shipment's cost, and
  observe where the correction lands.
```

## G05-STOCK_DELIVERY-Q040

```yaml
QID: G05-STOCK_DELIVERY-Q040
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A return shipment travelling back from the customer through the same carrier relationship is recorded as
  its own distinct movement and shipment, with its own cost, rather than being netted invisibly against
  the original outbound shipment's figures.
WHY_IT_MATTERS: >
  Netting a return invisibly into the original outbound record hides both the fact that a return occurred
  and its own separate cost from anyone looking at either record alone.
DISCONFIRMING_OBSERVATION: >
  Processing a return shipment changes the figures on the original outbound movement's record rather than
  producing its own separate, traceable movement and cost.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Process a return through the carrier for a previously delivered shipment and check whether it produces
  its own record or alters the original.
```

## G05-STOCK_DELIVERY-Q041

```yaml
QID: G05-STOCK_DELIVERY-Q041
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether the cost of a return shipment is borne by the business or by the customer is a configurable rule
  (for example, tied to the reason for the return), not a single fixed outcome applied to every return
  regardless of cause.
WHY_IT_MATTERS: >
  A business that only accepts return shipping cost for its own errors, and not for a change of mind,
  cannot express that distinction if the outcome is fixed.
DISCONFIRMING_OBSERVATION: >
  There is no configuration governing who bears a return shipment's carrier cost; the same party always
  bears it regardless of the return's stated reason.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Look for a configuration point governing who bears return shipping cost based on the reason for the
  return, and attempt to vary it.
```

## G05-STOCK_DELIVERY-Q042

```yaml
QID: G05-STOCK_DELIVERY-Q042
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A return shipment is linked back to the specific original outbound shipment it relates to, so that the
  pairing (and hence any cost or accounting resolution between the two) is traceable, rather than the
  return standing alone with no recorded relationship to what was originally sent.
WHY_IT_MATTERS: >
  An unlinked return cannot be reconciled against the original sale or shipment, leaving open which
  shipment a given return actually resolves.
DISCONFIRMING_OBSERVATION: >
  A processed return carries no reference back to the original outbound shipment it corresponds to.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Process a return for a known original shipment and check whether the return record references that
  original shipment.
```

## G05-STOCK_DELIVERY-Q043

```yaml
QID: G05-STOCK_DELIVERY-Q043
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A return travelling back through a different carrier than the one used for the original outbound
  shipment (a customer using their own preferred return method) is still recognised as a return against
  the original shipment, rather than the linkage only working when the same carrier is used both ways.
WHY_IT_MATTERS: >
  Requiring the same carrier for a return to be recognised would silently orphan every return sent back
  through a different carrier, which is a common real-world case.
DISCONFIRMING_OBSERVATION: >
  A return sent back through a carrier different from the one used outbound cannot be linked to or
  recognised against the original shipment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Process a return using a different carrier than the original outbound shipment used, and check whether
  the linkage to the original still holds.
```

## G05-STOCK_DELIVERY-Q044

```yaml
QID: G05-STOCK_DELIVERY-Q044
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Voiding an already-issued carrier tracking identity (with the potential cost and customer-facing
  consequences that carries) requires a distinct permission from the permission needed merely to validate
  the underlying stock movement.
WHY_IT_MATTERS: >
  If any user who can validate a movement can also void a live shipment with a carrier, an operational
  action and a decision with real financial and customer consequences share no separate control.
DISCONFIRMING_OBSERVATION: >
  A user role that can validate stock movements but has no shipment-specific permission is still able to
  void an issued carrier tracking identity.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Assign a role limited to movement validation only, and attempt to void an issued carrier tracking
  identity under that role.
```

## G05-STOCK_DELIVERY-Q045

```yaml
QID: G05-STOCK_DELIVERY-Q045
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Overriding a system-computed shipping cost with a manually entered figure is a distinct, logged action,
  not indistinguishable from the system's own computed figure once saved.
WHY_IT_MATTERS: >
  An unlogged manual override of a computed cost removes the ability to later tell whether an unusual
  shipping charge came from the carrier's own pricing or from a person's manual entry.
DISCONFIRMING_OBSERVATION: >
  A manually overridden shipping cost is stored identically to a system-computed one, with nothing
  indicating an override occurred or who made it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Override a computed shipping cost manually and check whether the override and its author are
  distinguishable from a system-computed figure.
```

## G05-STOCK_DELIVERY-Q046

```yaml
QID: G05-STOCK_DELIVERY-Q046
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A user without permission to view a particular company's shipments cannot reach that company's carrier
  tracking information or shipping cost figures through a cross-company report or lookup that was not
  itself scoped to company.
WHY_IT_MATTERS: >
  A report that forgets to scope by company can leak one company's shipping activity and cost exposure to
  users who have no business seeing it.
DISCONFIRMING_OBSERVATION: >
  A user restricted from one company's shipments can still see that company's carrier tracking or cost
  information through some other report or lookup path.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Restrict a user from one company's data, then attempt to reach that company's shipment or carrier
  information through every available report or lookup.
```

## G05-STOCK_DELIVERY-Q047

```yaml
QID: G05-STOCK_DELIVERY-Q047
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two operators attempting to book a carrier shipment for the same movement at effectively the same time
  result in exactly one booking taking effect, rather than both succeeding and producing two live tracking
  identities for one physical shipment.
WHY_IT_MATTERS: >
  Two live bookings for one physical shipment can mean two charges and two carrier collection attempts for
  goods that only exist once.
DISCONFIRMING_OBSERVATION: >
  Two concurrent booking attempts for the same movement both succeed, producing two separate active
  tracking identities for one movement.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger two near-simultaneous carrier booking attempts against the same movement and observe how many
  bookings result.
```

## G05-STOCK_DELIVERY-Q048

```yaml
QID: G05-STOCK_DELIVERY-Q048
MODULE: stock_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A carrier option that is configured but has since become unreachable or invalid (expired credentials,
  discontinued service) is prevented from being selected for a new shipment, rather than remaining
  selectable and only failing at the point of booking with no earlier warning.
WHY_IT_MATTERS: >
  Discovering an invalid carrier only at the moment of booking delays dispatch and can happen repeatedly if
  nothing flags the configuration as broken beforehand.
DISCONFIRMING_OBSERVATION: >
  A carrier configuration known to be invalid or unreachable remains selectable for a new shipment with no
  warning before the booking attempt itself fails.
EXPECTED_SURFACE: S3,S5,S7
PRECONDITIONS: >
  Invalidate a carrier's credentials or configuration, then attempt to select that carrier for a new
  shipment before actually booking it.
```

---
## GMVQ Internal QA Checklist

- [x] 48 distinct MVQ records; no padding — every record targets a distinct hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`.
- [x] Questions are behavioral and source-neutral; no vendor/product name, technical identifier, or module
      name appears in question text.
- [x] Bridge Module Rule seam test applied to every question: removing the carrier capability and using
      stock movement and carrier handling apart would make each question meaningless.
- [x] Shipping cost quote vs charge vs invoice and who absorbs the difference represented (Q001-Q005).
- [x] Weight/dimension derivation correctness represented (Q006-Q009).
- [x] Carrier rejection after validation represented (Q010-Q013).
- [x] Package splitting vs single movement represented (Q014-Q017).
- [x] Tracking identity lifecycle and cancellation represented (Q018-Q022).
- [x] Delivery address changed after label generation represented (Q023-Q026).
- [x] Carrier state vs internal state disagreement represented (Q027-Q031).
- [x] Per-company/tenant carrier configuration represented (Q032-Q035).
- [x] Period recognition for shipping cost at dispatch/invoice/close represented (Q036-Q039).
- [x] Returns travelling back through the same seam represented (Q040-Q043).
- [x] Role/permission boundary specific to carrier operations represented (Q044-Q046).
- [x] Concurrency and configuration-reachability represented (Q047-Q048).
- [x] Tenant/company boundary represented (Q032-Q035, Q046).
- [x] No specific Thai legal or tax requirement asserted anywhere in this bank.
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
