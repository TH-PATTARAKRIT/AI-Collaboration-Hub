# SMEsPlus ENTERPRISE SUITE
## GMVQ — G05 INVENTORY / product_expiry Module MVQ Bank

**Document ID:** GMVQ-G05-PRODUCT_EXPIRY-MVQ48-V1.00
**Group:** G05 INVENTORY
**Module Metadata:** `product_expiry`
**Wave:** W2
**Author Cell:** TEAM P05 (GMVQ Production Team — Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies module-specific research questions (MVQ) for the shelf-life-tracked-lot capability within G05 INVENTORY: a lot carrying several distinct dates (a best-before date, a shelf-life limit date, a removal date and an alert date) and which one governs which decision; the checkpoints at which a limit is evaluated (reservation, picking and dispatch) and a lot that crosses the boundary between them; the removal strategy's interaction with a lot already past its limit and who may override that; a limit date changed after the lot has moved, or received already past its limit; a date derived at receipt from a rule that later changes; the carried value of stock past its limit and when a write-down occurs, including across a period close; partial consumption near the limit; an alert firing for stock already departed; and the traceability of a decision to move stock close to its limit. Coverage is spread across business capability, business rule, state transition, configuration dependency, role and permission, exception path, cancellation, reversal, negative case, cross-module dependency, optional behaviour, auditability, tenant/company boundary, concurrency and ordering, runtime reachability, configuration reachability, and source/runtime contradiction potential.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses; none was trimmed or stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table, field, method, XML ID, API path), and the module's own metadata name never appears outside the `MODULE:` field and the `QID` — the generic term "shelf-life limit date" stands in for it throughout, and "past its limit" stands in for the state it names.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/evidence from Lane A or Lane B.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank alone.
- This document is PREPARED ONLY / NOT APPROVED / NOT FROZEN. It is not Boss Final Approval.

## G05-PRODUCT_EXPIRY-Q001

```yaml
QID: G05-PRODUCT_EXPIRY-Q001
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Automatic removal-strategy selection is driven specifically by a lot's removal date, not by its best-before date or shelf-life limit date, when the three differ.
WHY_IT_MATTERS: >
  Conflating the dates would make the removal order unpredictable and defeat the purpose of carrying them separately.
DISCONFIRMING_OBSERVATION: >
  Two lots with identical removal dates but different best-before or shelf-life limit dates are picked in an order that only the best-before or limit date can explain.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create two lots of one product with matching removal dates but deliberately different best-before and shelf-life limit dates, then trigger an automatic removal-strategy pick and compare the order chosen.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q002

```yaml
QID: G05-PRODUCT_EXPIRY-Q002
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Blocking a lot from a new outbound reservation is governed by its shelf-life limit date (or an explicitly configured blocking date), independent of whether a separate alert date has been configured at all.
WHY_IT_MATTERS: >
  If blocking silently depended on an unrelated alert configuration, a site that never configured alerts would lose blocking protection without knowing it.
DISCONFIRMING_OBSERVATION: >
  A lot past its shelf-life limit is still offered to a new reservation when no alert date was ever configured for it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a lot with a shelf-life limit date but no alert date, let the limit pass, then attempt a new reservation against it.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q003

```yaml
QID: G05-PRODUCT_EXPIRY-Q003
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An alert date configured earlier than the shelf-life limit date is honoured as configured and is not silently clamped to, or replaced by, the limit date itself.
WHY_IT_MATTERS: >
  A clamped alert date would remove the early-warning window the business deliberately configured, defeating the purpose of setting it separately.
DISCONFIRMING_OBSERVATION: >
  An alert configured to fire several days before the shelf-life limit date instead fires only on or after that limit date.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Configure an alert date set well before a lot's shelf-life limit date and observe when the alert condition actually becomes true.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q004

```yaml
QID: G05-PRODUCT_EXPIRY-Q004
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A lot carrying a best-before date and a shelf-life limit date but no explicit removal date is still subject to a defined removal-order rule rather than being treated as having no removal preference at all.
WHY_IT_MATTERS: >
  A silent gap in removal-order logic for incompletely dated lots would make stock rotation unpredictable exactly where it matters most.
DISCONFIRMING_OBSERVATION: >
  A lot with no removal date set is picked in an order indistinguishable from random relative to otherwise-comparable dated lots, with no fallback rule observable.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a lot lacking a removal date alongside lots that have one, run the removal strategy repeatedly, and check whether a consistent fallback ordering rule is observed.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q005

```yaml
QID: G05-PRODUCT_EXPIRY-Q005
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A best-before date passing does not by itself block a lot from being picked or shipped, while the shelf-life limit date passing does — the two dates carry materially different operational consequences.
WHY_IT_MATTERS: >
  If the two were treated identically, either useful stock would be blocked too early or unsafe stock would ship too late.
DISCONFIRMING_OBSERVATION: >
  A lot whose best-before date has passed but whose shelf-life limit date has not is blocked from picking in exactly the same way as a lot past its actual limit.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a lot whose best-before date has passed but whose shelf-life limit date is still in the future, and attempt to pick it.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q006

```yaml
QID: G05-PRODUCT_EXPIRY-Q006
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An existing reservation against a lot whose shelf-life limit date is reached before the linked outbound document is picked is surfaced to the operator rather than being carried through the completion path unremarked.
WHY_IT_MATTERS: >
  A reservation made when a lot was still within limit does not update itself, so without a check the operator could complete a pick against stock that quietly became unusable.
DISCONFIRMING_OBSERVATION: >
  A reservation created while the lot was within limit reaches the picking step after the limit date has passed with no warning or difference in behaviour from an ordinary in-limit pick.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Reserve a lot against a customer demand while it is within limit, advance time past its shelf-life limit date without touching the reservation, then attempt to pick it.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q007

```yaml
QID: G05-PRODUCT_EXPIRY-Q007
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A reserved lot that passes its shelf-life limit date before dispatch is flagged rather than allowed to complete dispatch through the normal, unmodified completion path.
WHY_IT_MATTERS: >
  Dispatch is the last controllable point before stock leaves the business; a silent pass-through here removes the final safeguard.
DISCONFIRMING_OBSERVATION: >
  A shipment completes and confirms dispatch of a lot that is past its shelf-life limit date with no distinct warning, hold, or required acknowledgment compared to an in-limit dispatch.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Bring a reserved, picked lot to the point of dispatch after its shelf-life limit date has passed and observe whether dispatch completion behaves differently from the in-limit case.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q008

```yaml
QID: G05-PRODUCT_EXPIRY-Q008
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A lot already reserved for a specific demand that passes its shelf-life limit date is treated as unavailable for that reservation just as it would be for a brand-new demand — the existing reservation is not exempt from the limit check.
WHY_IT_MATTERS: >
  An exemption for already-reserved stock would create a loophole where reserving early is a way to bypass the limit check entirely.
DISCONFIRMING_OBSERVATION: >
  A new demand is correctly refused an over-limit lot, while an already-reserved demand against the identical lot proceeds without any equivalent check.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Compare the outcome of a new reservation attempt and an existing reservation's continuation against the same lot once it has passed its shelf-life limit date.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q009

```yaml
QID: G05-PRODUCT_EXPIRY-Q009
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A lot past its shelf-life limit date is excluded from the availability search a removal strategy uses at the moment a reservation is created, not only later at picking.
WHY_IT_MATTERS: >
  Filtering only at picking leaves a window where demand is committed against stock that should never have been offered.
DISCONFIRMING_OBSERVATION: >
  A lot already past its shelf-life limit date at the time of reservation is nevertheless selected and reserved by the automatic removal strategy.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  With only an over-limit lot available for a product, attempt to create a new reservation through the standard removal strategy.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q010

```yaml
QID: G05-PRODUCT_EXPIRY-Q010
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A lot that was within limit when reserved but crosses its shelf-life limit date before picking is actually performed is re-evaluated at the picking step rather than carried through on the original, now-stale availability check.
WHY_IT_MATTERS: >
  Trusting a point-in-time check indefinitely turns a routine delay between reservation and picking into a silent safety gap.
DISCONFIRMING_OBSERVATION: >
  Picking proceeds without any re-check for a lot that has crossed its shelf-life limit date in the interval between reservation and the picking action.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reserve a lot while in limit, allow its shelf-life limit date to pass before the pick step is performed, and observe whether picking re-evaluates the limit.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q011

```yaml
QID: G05-PRODUCT_EXPIRY-Q011
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A lot that remains within limit through picking but crosses its shelf-life limit date before the dispatch confirmation step is checked again at that final step, rather than the limit only ever being enforced once at the earliest checkpoint.
WHY_IT_MATTERS: >
  A single-checkpoint design would let normal handling delays between picking and dispatch turn into unnoticed shipments of over-limit stock.
DISCONFIRMING_OBSERVATION: >
  A lot that crosses its shelf-life limit date strictly between picking and dispatch is dispatched with no distinguishable check at the dispatch step.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Pick a lot while within limit, allow its shelf-life limit date to pass before dispatch confirmation, and observe whether dispatch re-evaluates the limit.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q012

```yaml
QID: G05-PRODUCT_EXPIRY-Q012
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The three checkpoints — reservation, picking and dispatch — can produce different outcomes for the same lot depending on when each runs, and passing the earliest checkpoint is never treated as proof that the later ones will also pass.
WHY_IT_MATTERS: >
  Assuming an early pass guarantees a later pass is exactly the assumption that produces silent over-limit shipments.
DISCONFIRMING_OBSERVATION: >
  Documentation or observed behaviour shows the system treating a pass at reservation as sufficient grounds to skip the limit check at picking or dispatch.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Trace one lot through all three checkpoints under a scenario engineered so its limit status differs at each one, and compare the checks actually performed at each stage.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q013

```yaml
QID: G05-PRODUCT_EXPIRY-Q013
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A configured automatic removal strategy does not select a lot past its shelf-life limit date when an in-limit alternative of the same product exists.
WHY_IT_MATTERS: >
  This is the core promise of an automatic removal strategy; failing it silently defeats the entire feature's purpose.
DISCONFIRMING_OBSERVATION: >
  With both an in-limit lot and an over-limit lot available for the same demand, the automatic strategy selects the over-limit lot.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Stock one in-limit and one over-limit lot of the same product and location, then trigger the automatic removal strategy for a demand that either could satisfy.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q014

```yaml
QID: G05-PRODUCT_EXPIRY-Q014
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When every available lot for a demand is past its shelf-life limit date, an explicit elevated action is required to proceed rather than the automatic removal strategy silently substituting an over-limit lot.
WHY_IT_MATTERS: >
  Silent substitution under scarcity is the exact moment the safeguard is needed most and most likely to be quietly bypassed.
DISCONFIRMING_OBSERVATION: >
  A demand is satisfied entirely from over-limit lots through the ordinary automatic removal strategy with no distinct elevated step required.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Reduce available stock for a product to only over-limit lots and attempt to satisfy a demand through the standard removal strategy.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q015

```yaml
QID: G05-PRODUCT_EXPIRY-Q015
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An override that allows an over-limit lot to be picked or shipped leaves a distinguishable trace from an ordinary automatic selection.
WHY_IT_MATTERS: >
  Without a distinguishable trace, no later review can tell a deliberate exception from a routine pick, which defeats accountability for the decision.
DISCONFIRMING_OBSERVATION: >
  The record of an overridden over-limit pick is indistinguishable from an ordinary in-limit pick once the transaction is complete.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Perform one ordinary in-limit pick and one overridden over-limit pick, then compare the resulting records for any distinguishing marker.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q016

```yaml
QID: G05-PRODUCT_EXPIRY-Q016
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The ability to override a shelf-life limit block is restricted to a defined role or permission, and a user lacking it cannot force an over-limit lot through the same path.
WHY_IT_MATTERS: >
  An unrestricted override turns a governance control into an option any user can quietly exercise, removing its value entirely.
DISCONFIRMING_OBSERVATION: >
  A user without the designated override permission is nevertheless able to push an over-limit lot through picking or dispatch.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Attempt the override path as a user explicitly not granted the override permission and compare the outcome to the same attempt by an authorised user.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q017

```yaml
QID: G05-PRODUCT_EXPIRY-Q017
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing a lot's shelf-life limit date after part of its quantity has already been picked and delivered does not retroactively alter the historical record of what was shipped relative to the limit that applied at that time.
WHY_IT_MATTERS: >
  Retroactive alteration of shipped history would let a later date correction erase evidence of what was actually shipped and under what condition.
DISCONFIRMING_OBSERVATION: >
  Editing a lot's shelf-life limit date changes what an already-completed shipment record shows the limit to have been at the time of shipment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Ship part of a lot's quantity, then change the lot's shelf-life limit date and inspect whether the historical shipment record's stated limit changes.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q018

```yaml
QID: G05-PRODUCT_EXPIRY-Q018
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to a lot's shelf-life limit date is recorded as a distinct, attributable event rather than being applied with no record of who made the change or when.
WHY_IT_MATTERS: >
  An unattributed date change is an unaudited path to making stock ship-able that should not be, with no way to later establish who did it.
DISCONFIRMING_OBSERVATION: >
  A lot's shelf-life limit date is changed and no record exists afterward showing that a change occurred, by whom, or from what value.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Change a lot's shelf-life limit date as an identifiable user and check for a corresponding change record.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q019

```yaml
QID: G05-PRODUCT_EXPIRY-Q019
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A shelf-life limit date change on a lot that has already been split across multiple locations or reservations is reflected consistently on every remaining unconsumed portion, not only on the specific portion that was edited.
WHY_IT_MATTERS: >
  A split lot with inconsistent dates across its portions would let the same nominal lot be simultaneously in-limit in one place and over-limit in another.
DISCONFIRMING_OBSERVATION: >
  After a lot is split across two locations, changing the shelf-life limit date through one portion leaves the other portion showing the old, unchanged date.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Split one lot's quantity across two locations, change the shelf-life limit date via one location's portion, and compare the date shown for the other portion.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q020

```yaml
QID: G05-PRODUCT_EXPIRY-Q020
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Receiving a lot whose shelf-life limit date is already in the past does not proceed as an ordinary, unremarked receipt — it is flagged or requires an explicit acknowledgment distinct from normal goods-in handling.
WHY_IT_MATTERS: >
  Silently accepting already-over-limit stock at the door removes the earliest and cheapest point to catch a supplier or handling problem.
DISCONFIRMING_OBSERVATION: >
  A lot received with a shelf-life limit date already in the past completes the goods-in process with no warning, flag, or required acknowledgment different from an ordinary receipt.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Receive a lot and record a shelf-life limit date already in the past, then observe whether the receipt process behaves any differently from an in-limit receipt.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q021

```yaml
QID: G05-PRODUCT_EXPIRY-Q021
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A lot received with its shelf-life limit date already past remains visible to a removal-strategy search (as a blocked, over-limit candidate) rather than being invisible with no record that it was ever received.
WHY_IT_MATTERS: >
  An invisible over-limit lot cannot be counted, written down, or disposed of through a controlled process because nothing shows it exists.
DISCONFIRMING_OBSERVATION: >
  A lot received already past its shelf-life limit date does not appear in on-hand quantity or stock listings at all after receipt.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Receive a lot already past its shelf-life limit date and check whether it appears in on-hand stock records as a blocked quantity.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q022

```yaml
QID: G05-PRODUCT_EXPIRY-Q022
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A lot's shelf-life limit date, once derived and stored at receipt from a configured shelf-life duration rule, does not automatically recalculate when that configuration rule is changed afterward.
WHY_IT_MATTERS: >
  Retroactive recalculation would silently rewrite the stated limit of stock already on hand and already communicated to customers or regulators.
DISCONFIRMING_OBSERVATION: >
  Changing the configured shelf-life duration rule changes the stored limit date of a lot that was already received under the previous rule.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Receive a lot under one shelf-life duration configuration, then change that configuration and check whether the already-stored lot date changes.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q023

```yaml
QID: G05-PRODUCT_EXPIRY-Q023
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A newly received lot of the same product, received after the shelf-life duration rule changes, is derived under the new rule, so lots derived under the old and new rules coexist with different limit dates for the same product.
WHY_IT_MATTERS: >
  If new receipts silently inherited the old rule instead, a configuration change would have no real effect until every existing lot cleared.
DISCONFIRMING_OBSERVATION: >
  A lot received after the shelf-life duration rule is changed is nonetheless derived using the prior rule's duration.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change the configured shelf-life duration rule, receive a new lot of the affected product, and check which duration was actually applied.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q024

```yaml
QID: G05-PRODUCT_EXPIRY-Q024
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A lot's on-hand quantity remains valued at its original cost after passing its shelf-life limit date until a distinct, deliberate write-down or scrap action occurs — the limit passing does not by itself reduce carried value.
WHY_IT_MATTERS: >
  If passing the limit silently changed valuation, financial results would move without any traceable transaction behind the change.
DISCONFIRMING_OBSERVATION: >
  A lot's recorded value changes at the moment its shelf-life limit date passes, with no distinct write-down or scrap transaction recorded.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Hold a valued lot through its shelf-life limit date without any write-down action and compare its recorded value immediately before and after the date passes.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q025

```yaml
QID: G05-PRODUCT_EXPIRY-Q025
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The event that reduces an over-limit lot's carried value is a distinct, identifiable action visible in the record as something that happened, not merely inferable by comparing a stored date to the current date at query time.
WHY_IT_MATTERS: >
  A value change that exists only as an inference from a date comparison cannot be reconciled, audited, or explained to a reviewer after the fact.
DISCONFIRMING_OBSERVATION: >
  No transaction record exists for a reduction in an over-limit lot's carried value; the only way to see the reduction is by recomputing it from the current date.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Trigger a write-down on an over-limit lot and check for a corresponding recorded transaction distinct from the underlying date comparison.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q026

```yaml
QID: G05-PRODUCT_EXPIRY-Q026
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A lot that passes its shelf-life limit date between one accounting period close and the next has any resulting value adjustment land in the period during which the adjusting action actually occurred, not silently restated into the already-closed prior period.
WHY_IT_MATTERS: >
  Restating a closed period without a controlled reopening breaks the integrity of financial statements already issued for that period.
DISCONFIRMING_OBSERVATION: >
  A write-down for a lot that passed its shelf-life limit date after a period closed appears recorded within the already-closed period rather than the current one.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  Close a period, then let a lot pass its shelf-life limit date and trigger a write-down afterward, and check which period the adjustment is recorded in.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q027

```yaml
QID: G05-PRODUCT_EXPIRY-Q027
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Stock that passed its shelf-life limit date before a period close but had not yet been written down carries into the next period at its prior value rather than the close process itself silently adjusting it.
WHY_IT_MATTERS: >
  A close process that quietly performs valuation adjustments would hide a write-down decision inside a routine, unrelated procedure.
DISCONFIRMING_OBSERVATION: >
  An un-written-down over-limit lot's carried value changes purely as a side effect of running the period close, with no distinct write-down action taken.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  Have an over-limit, not-yet-written-down lot on hand at the moment a period close is run, and compare its recorded value immediately before and after the close.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q028

```yaml
QID: G05-PRODUCT_EXPIRY-Q028
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Consuming only part of a lot's quantity close to its shelf-life limit date leaves the remaining quantity under the same lot identity and the same limit date rather than creating an ambiguous or untracked remainder.
WHY_IT_MATTERS: >
  An untracked remainder could sit on the shelf indefinitely with no identity to check it against.
DISCONFIRMING_OBSERVATION: >
  After partial consumption of a lot, the remaining quantity cannot be located under any identifiable lot, or shows no shelf-life limit date at all.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Consume part of a lot's quantity near its limit date and check the identity and stated limit date of what remains.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q029

```yaml
QID: G05-PRODUCT_EXPIRY-Q029
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The remaining quantity of a partially consumed lot near its shelf-life limit date is still subject to the same removal-strategy and blocking checks as a lot that has not been touched at all.
WHY_IT_MATTERS: >
  A remainder that quietly loses its checks would become an easy, unnoticed route to shipping over-limit stock.
DISCONFIRMING_OBSERVATION: >
  Once a lot has been partially consumed, its remaining quantity is offered to a new reservation past its shelf-life limit date when an untouched lot in the same state would have been blocked.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Partially consume a lot, allow its shelf-life limit date to pass, and attempt to reserve the remainder against a new demand.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q030

```yaml
QID: G05-PRODUCT_EXPIRY-Q030
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An alert configured for a lot does not fire, or is suppressed, once that lot's entire quantity has already left the warehouse through a completed outbound movement.
WHY_IT_MATTERS: >
  An alert about stock that is already gone gives the operator a warning they can no longer act on, wasting attention and eroding trust in the alert system.
DISCONFIRMING_OBSERVATION: >
  An alert fires for a lot whose entire recorded quantity has already been dispatched, with no indication that the underlying stock is gone.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Fully dispatch a lot before its configured alert date is reached, then observe whether the alert still fires on that date.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q031

```yaml
QID: G05-PRODUCT_EXPIRY-Q031
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A lot that has partially shipped and partially remains on hand generates an alert scoped to the remaining on-hand quantity, not to the original full quantity that included what already left.
WHY_IT_MATTERS: >
  An alert overstating the affected quantity misleads whoever has to act on it about the real scale of the exposure.
DISCONFIRMING_OBSERVATION: >
  A partially shipped lot's alert states the original received quantity rather than what is actually still on hand.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Partially ship a lot before its alert date, then check what quantity the resulting alert references.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q032

```yaml
QID: G05-PRODUCT_EXPIRY-Q032
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An alert that was scheduled before a lot was fully consumed but only fires afterward is distinguishable in the record as referring to already-departed stock, rather than being indistinguishable from a live warning.
WHY_IT_MATTERS: >
  An operator cannot tell a stale alert from an actionable one without some marker distinguishing the two, wasting response effort.
DISCONFIRMING_OBSERVATION: >
  A fired alert for a fully departed lot carries no marker distinguishing it from an alert about stock still physically present.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Let a lot fully depart after its alert was scheduled but before the alert date, then inspect the fired alert for any indication that the underlying stock is gone.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q033

```yaml
QID: G05-PRODUCT_EXPIRY-Q033
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A shipment record allows tracing, after the fact, which specific lot and shelf-life limit date applied to a shipment that included stock close to its limit.
WHY_IT_MATTERS: >
  Without after-the-fact traceability, a customer complaint or recall inquiry about a near-limit shipment cannot be resolved from the record alone.
DISCONFIRMING_OBSERVATION: >
  A completed shipment record cannot be traced back to the specific lot or the limit date that applied to the stock it contained.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Ship a lot close to its shelf-life limit date, then attempt to trace the completed shipment record back to that lot and its stated date.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q034

```yaml
QID: G05-PRODUCT_EXPIRY-Q034
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A shipment of a near-limit lot made through the ordinary automatic removal strategy remains distinguishable in the historical record from one made under an explicit override.
WHY_IT_MATTERS: >
  Collapsing the two into one indistinguishable outcome removes the ability to later separate routine near-limit shipments from deliberate exceptions when reviewing what happened.
DISCONFIRMING_OBSERVATION: >
  An automatic near-limit shipment and an overridden over-limit shipment leave identical records with no field or marker separating the two cases.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Perform one automatic near-limit shipment and one overridden over-limit shipment, then compare the two resulting records for a distinguishing marker.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q035

```yaml
QID: G05-PRODUCT_EXPIRY-Q035
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Shelf-life tracking can be enabled or disabled per product, and a product with tracking disabled is not subject to limit-based blocking or alerting even if a date happens to be present on one of its lot records.
WHY_IT_MATTERS: >
  If a stray date still triggered blocking on a product deliberately opted out, the configuration setting would not mean what it claims to mean.
DISCONFIRMING_OBSERVATION: >
  A product configured with tracking disabled is still blocked or alerted based on a date value present on one of its lots.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Disable shelf-life tracking on a product that nonetheless has a lot carrying a past limit date, and attempt to reserve or pick that lot.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q036

```yaml
QID: G05-PRODUCT_EXPIRY-Q036
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Shelf-life configuration set for one company's use of a shared product does not alter the limit-based blocking behaviour applied to a different company's stock of the same product.
WHY_IT_MATTERS: >
  A configuration leak across company boundaries would let one tenant's shelf-life policy silently govern another tenant's stock.
DISCONFIRMING_OBSERVATION: >
  Changing the shelf-life configuration under one company changes the blocking behaviour observed for the same product's stock recorded under a different company.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  With the same product shared across two companies, change the shelf-life configuration under one company and check whether the other company's blocking behaviour changes.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q037

```yaml
QID: G05-PRODUCT_EXPIRY-Q037
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two operators attempt at the same time to reserve the sole remaining in-limit lot of a product, only one succeeds — the other is refused or redirected rather than both proceeding on the same, now-stale availability check.
WHY_IT_MATTERS: >
  A double-reservation of the same physical stock produces a shortage that surfaces later at picking, when it is far more costly to resolve.
DISCONFIRMING_OBSERVATION: >
  Two concurrent reservation attempts against the sole remaining in-limit lot both report success.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  With exactly one in-limit lot available, issue two reservation attempts against it as close together in time as possible and compare both outcomes.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q038

```yaml
QID: G05-PRODUCT_EXPIRY-Q038
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Attempting to set a shelf-life limit date or removal date earlier than the lot's own receipt date is rejected or explicitly flagged rather than silently accepted as a valid configuration.
WHY_IT_MATTERS: >
  A date preceding receipt is never a meaningful business fact, and silently accepting it invites nonsensical downstream blocking or removal-order decisions.
DISCONFIRMING_OBSERVATION: >
  A lot is successfully saved with a shelf-life limit date or removal date earlier than its own recorded receipt date, with no rejection or flag raised.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to record a shelf-life limit date or removal date earlier than a lot's receipt date and observe whether the attempt is accepted, rejected, or flagged.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q039

```yaml
QID: G05-PRODUCT_EXPIRY-Q039
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A near-limit lot consumed as a component in a production or kitting operation carries its shelf-life visibility forward into the resulting output lot's traceability rather than the link being lost at consumption.
WHY_IT_MATTERS: >
  Losing the link at the point of transformation would make it impossible to trace a quality issue in a finished item back to a component that was already near its limit.
DISCONFIRMING_OBSERVATION: >
  A finished item produced from a near-limit component lot cannot be traced back to that component's identity or limit date.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consume a near-limit lot as a component in a production or kitting operation, then attempt to trace the resulting output back to that component lot.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q040

```yaml
QID: G05-PRODUCT_EXPIRY-Q040
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Limit-based blocking and the reason for it are visible to a warehouse role that has no access to cost or valuation data — the block itself is not gated behind a financial permission.
WHY_IT_MATTERS: >
  If warehouse staff could see that a lot is blocked but never why, they could not act on it correctly, and the safeguard would create confusion instead of preventing errors.
DISCONFIRMING_OBSERVATION: >
  A user with warehouse operational access but no financial or valuation permission cannot see that a lot is blocked, or cannot see the reason, while a user with financial access can.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user granted only warehouse operational permissions, attempt to view a blocked lot and the stated reason for the block.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q041

```yaml
QID: G05-PRODUCT_EXPIRY-Q041
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reversing a delivery that included a since-over-limit lot returns that lot to stock still marked with its original, over-limit status rather than resetting it to an unmarked, apparently fresh state.
WHY_IT_MATTERS: >
  A reversal that quietly clears the over-limit marker would reintroduce unsafe stock into normal circulation under the guise of a routine correction.
DISCONFIRMING_OBSERVATION: >
  After reversing a delivery, the returned lot shows no over-limit marker even though its shelf-life limit date has, in fact, passed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Deliver an over-limit lot under an override, reverse that delivery, and inspect the lot's status once it is back on hand.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q042

```yaml
QID: G05-PRODUCT_EXPIRY-Q042
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Limit-based blocking applies uniformly to a lot regardless of which removal strategy is configured for the product or location, rather than blocking only being effective under one particular strategy choice.
WHY_IT_MATTERS: >
  A safeguard that only works under one configuration choice would leave sites using a different valid configuration silently unprotected.
DISCONFIRMING_OBSERVATION: >
  An over-limit lot is blocked under one configured removal strategy but is picked without any block under a different, equally supported removal strategy.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Repeat the same over-limit pick attempt under two different supported removal-strategy configurations and compare whether blocking is applied in both.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q043

```yaml
QID: G05-PRODUCT_EXPIRY-Q043
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The record of a limit-based block or an override retains enough detail — which lot, which date, who acted — to reconstruct the decision independently of any live dashboard or current-state view.
WHY_IT_MATTERS: >
  A decision that can only be understood by looking at live, mutable state cannot be reviewed once that state has moved on, which defeats after-the-fact accountability.
DISCONFIRMING_OBSERVATION: >
  Weeks after a block or override occurred, the historical record no longer shows which lot, date, or user was involved, even though the underlying transaction still exists.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Record a block or override event, allow live state to move on (further receipts, further picks), then attempt to reconstruct the original decision from the historical record alone.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q044

```yaml
QID: G05-PRODUCT_EXPIRY-Q044
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A configuration setting that appears to permit shipping over-limit stock under defined conditions actually governs runtime behaviour consistently with what it states, rather than existing in configuration while being ignored in practice.
WHY_IT_MATTERS: >
  A configuration option that does not actually do what it says is worse than no option at all, because it gives false confidence to whoever set it.
DISCONFIRMING_OBSERVATION: >
  The configured condition for permitting an over-limit shipment is met, yet the shipment is blocked anyway, or the condition is not met and the shipment proceeds regardless.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Set the configuration to permit over-limit shipment under a specific condition, then test both the condition being met and not met, and compare actual outcomes to the stated configuration.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q045

```yaml
QID: G05-PRODUCT_EXPIRY-Q045
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A lot whose alert date has passed but whose shelf-life limit date has not is treated only as a warning, not as a block — a pre-limit alert and an actual limit block are two distinguishable behaviours.
WHY_IT_MATTERS: >
  Conflating an early warning with an actual block would either stop usable stock from moving or make the earlier warning meaningless.
DISCONFIRMING_OBSERVATION: >
  A lot whose alert date has passed but whose shelf-life limit date is still in the future is blocked from picking in the same way an over-limit lot would be.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Let a lot's alert date pass while its shelf-life limit date remains in the future, then attempt to pick it.
LAYER: PROCESS
```

## G05-PRODUCT_EXPIRY-Q046

```yaml
QID: G05-PRODUCT_EXPIRY-Q046
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Once a lot passes its shelf-life limit date, its over-limit condition is a distinct, directly queryable state rather than something only ever derivable by comparing a stored date to the current date at the moment of the query.
WHY_IT_MATTERS: >
  A condition that only exists as a live computation cannot be consistently reported, filtered, or reconciled across the many places stock status is used.
DISCONFIRMING_OBSERVATION: >
  No direct query or listing can show which lots are currently over-limit without externally recomputing the comparison against today's date for every lot.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Attempt to list all currently over-limit lots directly through a normal stock inquiry rather than recomputing the comparison externally.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q047

```yaml
QID: G05-PRODUCT_EXPIRY-Q047
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling an inbound receipt after a shelf-life limit date has already been derived and stored for the received lot removes or invalidates that limit record rather than leaving an orphaned limit entry with no corresponding stock.
WHY_IT_MATTERS: >
  An orphaned limit record could later be mistaken for real stock, or could pollute a report of upcoming limits with a lot that no longer exists.
DISCONFIRMING_OBSERVATION: >
  After a receipt is cancelled, the shelf-life limit record derived for that receipt still appears as an active, upcoming limit with no linked stock behind it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive a lot with a derived shelf-life limit date, cancel the receipt, and check whether the limit record still appears as active.
LAYER: BASE
```

## G05-PRODUCT_EXPIRY-Q048

```yaml
QID: G05-PRODUCT_EXPIRY-Q048
MODULE: product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Shelf-life rules configured at the product level apply consistently to every lot of that product across all of its stocking locations, rather than the same lot behaving under different rules depending on which location holds it.
WHY_IT_MATTERS: >
  Location-dependent inconsistency would mean the same physical product is safe in one warehouse and blocked in another under identical dates, with no business reason for the difference.
DISCONFIRMING_OBSERVATION: >
  The same lot, held partly in one location and partly in another, is blocked in one location but not the other despite carrying the identical shelf-life limit date in both.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Split a lot across two stocking locations, let its shelf-life limit date pass, and compare blocking behaviour for each location's portion.
LAYER: BASE
```
