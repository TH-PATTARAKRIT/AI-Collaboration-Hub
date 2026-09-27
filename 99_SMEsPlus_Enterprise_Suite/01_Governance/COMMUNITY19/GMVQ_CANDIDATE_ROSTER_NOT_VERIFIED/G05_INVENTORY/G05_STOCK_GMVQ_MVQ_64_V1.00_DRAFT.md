# SMEsPlus ENTERPRISE SUITE
## GMVQ — G05 INVENTORY / stock Module Adversarial MVQ Bank

**Document ID:** GMVQ-G05-STOCK-MVQ64-V1.00
**Group:** G05 INVENTORY
**Module Metadata:** `stock`
**Wave:** W2
**Author Cell:** P01 (GMVQ Question Factory — Production Team P01)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 64

## Purpose

`stock` is the BASE module of Group G05 INVENTORY and one of the two or three most consequential modules
in the whole programme: locations, quantities, movements, reservations/claims, picking, lot and serial
tracking, valuation method, negative-quantity handling, direct quantity adjustment, multi-warehouse and
cross-company transfer, unit-of-measure conversion, and multi-step routes all sit inside it. Eleven bridge
modules in this group are authored against this bank, so this bank deliberately owns the group's core
invariants directly rather than leaving them to be rediscovered piecemeal in each bridge bank. It
supplements the 35 Standard Questions with module-specific, adversarial questions targeting: reservation/
claim fairness and visibility; partial and over-receipt; duplicate validation of the same movement;
backdated movement into a closed period; a valuation method changed while quantity exists; cost layers
consumed out of order; negative on-hand quantity and its valuation; lot/serial uniqueness, split and
merge; an expiring or archived batch that is still claimed; scrap; direct quantity adjustment as a
lightly-audited write path; cross-company warehouse transfer; unit conversion across purchase/stock/sale
units; multi-step routes partially completed; concurrency between two operators; and forced availability /
reservation override with its trace.

Per the Group Brief, a movement question that cannot ask what the accounting did is only half a question,
so a majority of the movement-touching questions in this bank carry an explicit ledger/valuation dimension
inside their `DISCONFIRMING_OBSERVATION`, not as a bolt-on afterthought.

Question text is source-neutral: no vendor or product name, no technical identifier (model, table, field,
method, XML ID, API path), and no reference to how any specific implementation is built. Language is
generic inventory/business behaviour throughout; the module's own metadata name appears only in the
`MODULE:` field of each record.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 64 questions exist because they test 64 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, cross-module dependency, auditability, tenant/company boundary,
  concurrency/ordering, and runtime/configuration reachability.
- `LAYER: BASE` marks a foundation/configuration question; `LAYER: PROCESS` marks a transactional/
  operational question, since this module carries both layers.
- 26 of the 64 questions carry `S2` (accounting/posting) in `EXPECTED_SURFACE`, giving the group's
  inventory-to-accounting bridge risk direct, explicit coverage from the base module, per the Group Brief's
  instruction that this bank should own the group's core invariants so the bridge banks do not have to.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a
  Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G05-STOCK-Q001

```yaml
QID: G05-STOCK-Q001
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When two independent outbound demands are created for the same product and only one unit is available,
  the system commits that unit to exactly one demand and leaves the other demand in an unfulfilled, clearly
  identifiable state rather than double-promising it.
WHY_IT_MATTERS: >
  If both demands are told the unit is theirs, one fulfillment will fail at the point of physical release,
  producing a customer-facing failure that traces back to a promise the system should never have made.
DISCONFIRMING_OBSERVATION: >
  Both outbound demands show the same unit as reserved and available for release at the same time, so that
  either could be picked and released against it.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Bring on-hand quantity of a product to exactly one unit, then create two independent outbound demands for
  that product in close succession and inspect what each demand reports as reserved.
```

## G05-STOCK-Q002

```yaml
QID: G05-STOCK-Q002
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The rule that decides which of two competing demands wins a scarce unit is deterministic and documented
  (for example, order of creation or a configured priority), not left to incidental processing order.
WHY_IT_MATTERS: >
  An undocumented or non-deterministic allocation rule makes the outcome unexplainable to the business user
  who did not get their unit, and unverifiable by anyone auditing the decision afterward.
DISCONFIRMING_OBSERVATION: >
  Repeating the same two-demand-one-unit scenario under identical conditions produces a different winner on
  different runs, with no configuration difference to explain it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create the same one-unit-two-demands scenario multiple times under identical configuration and compare
  which demand is satisfied each time.
```

## G05-STOCK-Q003

```yaml
QID: G05-STOCK-Q003
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling or releasing an outbound demand's claim on a unit makes that unit visible as available to a new
  competing demand without requiring an unrelated background pass to run first.
WHY_IT_MATTERS: >
  A unit that is physically free but not yet visible as available causes staff to believe there is a
  shortage that does not exist, or to over-order.
DISCONFIRMING_OBSERVATION: >
  After a claim is released, a new demand for the same product still reports the unit as unavailable until
  an unrelated scheduled process later runs.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reserve the last available unit against one demand, cancel that demand's claim, and immediately check
  whether a new demand for the same product sees the unit as available.
```

## G05-STOCK-Q004

```yaml
QID: G05-STOCK-Q004
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A person creating a new outbound demand can see, for the product in question, the difference between the
  total quantity physically present and the quantity already promised to other demands.
WHY_IT_MATTERS: >
  Without that distinction a user will promise a delivery date against quantity that is physically present
  but already spoken for, creating a broken promise to a customer.
DISCONFIRMING_OBSERVATION: >
  The quantity figure shown when creating a new demand is the same whether or not other demands have already
  claimed part of the physically present quantity.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Reserve part of a product's on-hand quantity against one demand, then start creating a second demand for
  the same product and inspect what quantity figure is presented.
```

## G05-STOCK-Q005

```yaml
QID: G05-STOCK-Q005
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A demand cannot claim more units than are physically present at the moment the claim is made, absent an
  explicit configured allowance to promise against incoming supply.
WHY_IT_MATTERS: >
  Unlimited claiming beyond what physically exists silently converts an inventory system into a wish list,
  and downstream fulfillment staff cannot trust what "reserved" means.
DISCONFIRMING_OBSERVATION: >
  A demand successfully claims a quantity greater than what is physically present, with no configuration in
  place that explicitly permits claiming against expected future supply.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  With a known small on-hand quantity and no forward-claiming configuration enabled, attempt to create a
  demand for a larger quantity and observe whether the claim succeeds.
```

## G05-STOCK-Q006

```yaml
QID: G05-STOCK-Q006
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Reducing the quantity requested on an outbound demand that already holds a claim releases the excess
  claimed quantity back to general availability rather than continuing to hold it against a demand that no
  longer needs it.
WHY_IT_MATTERS: >
  A claim left in place after the need shrank silently strands supply that the business believes is free to
  use elsewhere.
DISCONFIRMING_OBSERVATION: >
  After the requested quantity on a demand is reduced, the previously claimed excess remains held against
  that demand and is not visible to a new competing demand.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a demand that claims a multi-unit quantity, then reduce the requested quantity on that demand and
  check whether the released amount becomes available to another demand.
```

## G05-STOCK-Q007

```yaml
QID: G05-STOCK-Q007
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A claim that has been outstanding well past the point the demand should reasonably have been fulfilled
  does not hold the unit indefinitely without any visible flag distinguishing it from a normal, timely
  claim.
WHY_IT_MATTERS: >
  An indefinitely stale claim quietly removes real supply from the available pool with no mechanism
  prompting anyone to review or release it.
DISCONFIRMING_OBSERVATION: >
  A claim created long before the current date continues to hold a unit exactly like a freshly created
  claim, with nothing in the system distinguishing the aged claim or prompting review.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a claim on a unit, artificially age the underlying demand well past a normal fulfillment window,
  and check whether the system treats it any differently from a fresh claim.
```

## G05-STOCK-Q008

```yaml
QID: G05-STOCK-Q008
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Recording a partial receipt against an expected inbound quantity leaves the un-received remainder visible
  as still outstanding against the same originating expectation, and the recorded inventory value reflects
  only the quantity actually received, not the full expected amount.
WHY_IT_MATTERS: >
  If the remainder silently disappears, nobody follows up on the missing quantity and no one is accountable
  for chasing the supplier; if value is booked ahead of physical receipt, the books overstate what is
  actually on hand.
DISCONFIRMING_OBSERVATION: >
  After a partial receipt, the originating expectation shows a fully-received status even though less than
  the expected quantity has actually arrived, or the recorded inventory value reflects the full expected
  quantity rather than only what was received.
EXPECTED_SURFACE: S1,S2,S5
PRECONDITIONS: >
  Create an inbound expectation for a multi-unit quantity, record a receipt for less than the full quantity,
  and inspect the status, remaining quantity, and recorded value of the expectation.
```

## G05-STOCK-Q009

```yaml
QID: G05-STOCK-Q009
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Receiving more units than were expected against an inbound expectation is either blocked, requires an
  explicit confirmation, or is recorded in a way that visibly flags the excess quantity rather than silently
  absorbing it as if it had been expected.
WHY_IT_MATTERS: >
  Unflagged over-receipt hides a supplier discrepancy that has both a physical-space and a payable-amount
  consequence.
DISCONFIRMING_OBSERVATION: >
  A receipt for more than the expected quantity is recorded and the resulting record shows no difference in
  form or trace from a receipt that matched the expected quantity exactly.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an inbound expectation for a known quantity and attempt to record a receipt for a larger quantity,
  observing whether the system distinguishes the excess.
```

## G05-STOCK-Q010

```yaml
QID: G05-STOCK-Q010
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A series of partial receipts recorded against one inbound expectation, over several separate occasions,
  sums to the correct total received quantity and correctly closes the expectation once the sum reaches what
  was expected.
WHY_IT_MATTERS: >
  An arithmetic or state-tracking error across multiple partial events is far more likely than in a
  single-event receipt, and would misstate what has actually arrived.
DISCONFIRMING_OBSERVATION: >
  After several partial receipts whose quantities sum exactly to the expected quantity, the expectation
  still shows outstanding quantity, or shows a total different from the sum of the individual receipts.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Record three or more separate partial receipts against one inbound expectation on different occasions and
  verify the running total and final closure.
```

## G05-STOCK-Q011

```yaml
QID: G05-STOCK-Q011
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When an over-received quantity is accepted into on-hand, the extra quantity is assigned a cost and
  reflected in the value of on-hand inventory rather than being added to quantity records without a
  corresponding valuation entry.
WHY_IT_MATTERS: >
  Quantity and value must move together; quantity added without value creates a ledger position that
  understates what is actually held.
DISCONFIRMING_OBSERVATION: >
  On-hand quantity increases by the over-received amount but the recorded inventory value does not change,
  or changes by an amount inconsistent with the quantity accepted.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Accept an over-received quantity into on-hand and compare the resulting quantity and value figures against
  the amount actually accepted.
```

## G05-STOCK-Q012

```yaml
QID: G05-STOCK-Q012
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  If a receipt is recorded using a different unit of measure than the one the expectation was raised in, the
  recorded quantity is converted correctly so that the expectation's outstanding balance reflects the true
  physical amount received, and the value recorded for the receipt is computed on the correctly converted
  quantity.
WHY_IT_MATTERS: >
  A silent unit mismatch at receipt is one of the most common causes of a physical count disagreeing with
  the recorded quantity, and a value computed on the wrong quantity misstates the cost of the goods
  received.
DISCONFIRMING_OBSERVATION: >
  Recording a receipt in an alternate unit of measure leaves the expectation's outstanding balance
  calculated as if the receipt had been recorded in the original unit, or the recorded value is computed
  using the pre-conversion quantity figure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Raise an inbound expectation in one unit of measure, record the receipt using a different, convertible
  unit of measure, and check the resulting outstanding balance and recorded value.
```

## G05-STOCK-Q013

```yaml
QID: G05-STOCK-Q013
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Reversing or cancelling a previously recorded partial receipt restores the outstanding quantity on the
  originating expectation to what it was before that receipt, and any value already recorded for that
  receipt is reversed with it, rather than leaving the expectation permanently reduced, or value standing,
  against an event that no longer stands.
WHY_IT_MATTERS: >
  A receipt that is undone but still counted, in quantity or value, causes the business to believe less is
  outstanding or more is on hand than what is actually true.
DISCONFIRMING_OBSERVATION: >
  After a partial receipt is reversed, the expectation's outstanding quantity does not return to its
  pre-receipt value, or the previously recorded value remains in the accounts with no corresponding physical
  receipt behind it.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record a partial receipt, reverse or cancel it, and compare the expectation's outstanding quantity and
  recorded value before the receipt, after the receipt, and after the reversal.
```

## G05-STOCK-Q014

```yaml
QID: G05-STOCK-Q014
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Attempting to validate or confirm a movement that has already been completed has no further effect on
  quantity, and does not apply the movement's quantity change a second time.
WHY_IT_MATTERS: >
  A duplicate application of the same movement silently inflates or deflates on-hand quantity by an amount
  that never physically happened.
DISCONFIRMING_OBSERVATION: >
  Repeating the validation action on an already-completed movement changes on-hand quantity a second time in
  the same direction as the original validation.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Complete a movement, note the resulting on-hand quantity, then attempt to validate the same movement again
  through the normal interface or a repeat call and compare quantities.
```

## G05-STOCK-Q015

```yaml
QID: G05-STOCK-Q015
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two near-simultaneous attempts to validate the same movement, such as from a duplicated click or a
  repeated automated call, result in exactly one applied quantity change, not two.
WHY_IT_MATTERS: >
  Network retries and impatient double-clicks are common real-world events; a system that is not resilient
  to them will periodically double-post real transactions.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous validation attempts on the same movement both succeed and both apply a quantity
  change.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Fire two validation requests for the same movement in immediate succession, as close together as the
  available interface allows, and inspect whether one or both applied a quantity change.
```

## G05-STOCK-Q016

```yaml
QID: G05-STOCK-Q016
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If a duplicate validation attempt is rejected at the quantity level, the corresponding accounting entries
  are also not duplicated; quantity and value integrity move together on this exception path exactly as they
  must on the normal path.
WHY_IT_MATTERS: >
  A quantity-level safeguard that leaves a value-level gap would still result in a ledger that disagrees with
  physical quantity, defeating the purpose of the safeguard.
DISCONFIRMING_OBSERVATION: >
  A duplicate validation attempt that correctly has no further quantity effect nonetheless produces a second
  set of accounting entries for the same movement.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Attempt to validate an already-completed movement a second time and inspect both the quantity and the
  accounting entries for evidence of duplication in either.
```

## G05-STOCK-Q017

```yaml
QID: G05-STOCK-Q017
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A rejected or no-effect repeat validation attempt is still recorded somewhere in the trace of the
  movement, distinguishable from the original successful validation, rather than leaving no trace of the
  attempt at all.
WHY_IT_MATTERS: >
  An unrecorded repeat attempt hides a pattern (script error, user confusion, or a bypass attempt) that an
  auditor would otherwise be able to detect.
DISCONFIRMING_OBSERVATION: >
  After a repeat validation attempt that had no quantity or ledger effect, no trace of the attempt exists
  anywhere associated with the movement.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Attempt to validate an already-completed movement a second time and search the movement's history or log
  for any record of the attempt.
```

## G05-STOCK-Q018

```yaml
QID: G05-STOCK-Q018
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A movement dated on or before the last day of a period that has been formally closed for financial
  reporting is blocked from normal completion, or requires an explicit elevated action to proceed, rather
  than completing exactly as an ordinary current-dated movement would.
WHY_IT_MATTERS: >
  An unrestricted backdate into a closed period lets a transaction silently change results that have already
  been reported and relied upon.
DISCONFIRMING_OBSERVATION: >
  A movement dated into a closed period completes through the ordinary path with no additional step,
  warning, or permission check beyond a current-dated movement.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Close a period, then attempt to complete a movement dated within that closed period using the same steps
  as an ordinary movement.
```

## G05-STOCK-Q019

```yaml
QID: G05-STOCK-Q019
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a backdated movement into a closed period is permitted at all, its accounting effect lands in a
  period still open for adjustment, not silently restated into the already-closed period's reported figures.
WHY_IT_MATTERS: >
  Silently altering a closed period's figures after they were reported and relied upon breaks the guarantee
  that a closed period is actually closed.
DISCONFIRMING_OBSERVATION: >
  A permitted backdated movement changes the reported figures of the already-closed period rather than
  landing in a currently open period.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  With backdating into a closed period permitted through whatever elevated path exists, complete such a
  movement and compare the closed period's reported figures before and after.
```

## G05-STOCK-Q020

```yaml
QID: G05-STOCK-Q020
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Completing a movement dated into a closed period, where permitted at all, requires a level of permission
  distinct from the permission needed for an ordinary current-dated movement, and the action is traceable to
  the person who performed it.
WHY_IT_MATTERS: >
  Without a distinct permission and trace, any user who can move goods at all can also silently rewrite
  closed-period history.
DISCONFIRMING_OBSERVATION: >
  A user holding only ordinary movement permission is able to complete a backdated movement into a closed
  period with no additional check and no trace naming who did it.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  With a user who holds only ordinary movement permission, attempt a movement dated into a closed period and
  check both whether it succeeds and whether it is traced.
```

## G05-STOCK-Q021

```yaml
QID: G05-STOCK-Q021
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A movement backdated into a closed period, once permitted, changes the recorded on-hand quantity as of
  that historical date consistently, so that a report run for that historical date reflects the same
  quantity a report run at the time would show plus the effect of the backdated event.
WHY_IT_MATTERS: >
  An inconsistency between a rerun historical report and what was reported at the time makes any prior
  reconciliation or count unreliable.
DISCONFIRMING_OBSERVATION: >
  A report of on-hand quantity as of the closed historical date, rerun after the backdated movement, does
  not reflect the backdated movement's effect at all, or reflects an amount inconsistent with the movement.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a backdated movement into a closed period and rerun a quantity-as-of report for that historical
  date, comparing it against the movement's quantity effect.
```

## G05-STOCK-Q022

```yaml
QID: G05-STOCK-Q022
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Changing the valuation method for a product that already carries on-hand quantity applies the new method
  to movements going forward, and does not silently recalculate the value of quantity already on hand under
  the prior method without an explicit revaluation step.
WHY_IT_MATTERS: >
  An automatic, invisible retroactive recalculation changes reported inventory value with no distinct event
  a reviewer can point to as the cause.
DISCONFIRMING_OBSERVATION: >
  Immediately after changing the valuation method, the recorded value of unchanged on-hand quantity differs
  from its value immediately before the change, with no explicit revaluation action having been taken.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Record on-hand quantity for a product under one valuation method, change the method, and compare the
  product's recorded value immediately before and after the change with no other action taken.
```

## G05-STOCK-Q023

```yaml
QID: G05-STOCK-Q023
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Movements completed before a valuation method change keep the cost that was assigned to them at the time,
  rather than being recalculated under the new method after the fact.
WHY_IT_MATTERS: >
  If history rewrites itself every time a configuration changes, no historical cost figure can ever be
  trusted as a permanent record of what happened.
DISCONFIRMING_OBSERVATION: >
  The recorded cost of a movement completed before a valuation method change is different when inspected
  after the change than it was when inspected before the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Note the recorded cost of a completed movement, change the product's valuation method, and inspect the
  same movement's recorded cost again afterward.
```

## G05-STOCK-Q024

```yaml
QID: G05-STOCK-Q024
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If a valuation method change does trigger a revaluation of on-hand quantity, that revaluation produces an
  identifiable accounting entry rather than adjusting the recorded value with no corresponding trace in the
  ledger.
WHY_IT_MATTERS: >
  An unexplained jump in inventory value with no supporting entry is exactly the kind of discrepancy a
  financial reviewer cannot reconcile.
DISCONFIRMING_OBSERVATION: >
  A valuation method change measurably changes the recorded value of on-hand quantity but no corresponding
  accounting entry exists to explain the change.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Change a product's valuation method in a way expected to trigger revaluation and check whether a
  corresponding accounting entry was created.
```

## G05-STOCK-Q025

```yaml
QID: G05-STOCK-Q025
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Reverting a valuation method back to its original setting does not automatically restore on-hand quantity
  to its value from before the original change; the two changes are independent events, each of which may or
  may not trigger a revaluation.
WHY_IT_MATTERS: >
  An operator who assumes reverting the setting also reverts the value could be badly surprised, either by
  an unwanted revaluation or by a value that stays put when they expected it to return.
DISCONFIRMING_OBSERVATION: >
  Reverting a valuation method setting to its original value silently and automatically restores on-hand
  value to its pre-change figure without an explicit revaluation action, or conversely destroys traceable
  history of the intermediate value.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Change a valuation method, note the resulting value, revert the setting to its original value, and observe
  what happens to recorded value and its history.
```

## G05-STOCK-Q026

```yaml
QID: G05-STOCK-Q026
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When quantity is consumed from a product with distinct cost layers, the layer actually charged to the
  consuming movement matches the order the configured costing policy specifies, rather than an arbitrary or
  reversed order.
WHY_IT_MATTERS: >
  If the wrong layer is charged, the cost of goods recognized for a sale does not match the true economic
  cost of the units actually shipped.
DISCONFIRMING_OBSERVATION: >
  A consuming movement is charged a cost from a layer other than the one the configured costing policy
  specifies as next in line, while an eligible layer following that policy still exists.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Build up on-hand quantity for one product across at least two distinct cost layers with different unit
  costs, consume part of the quantity, and check which layer's cost was actually charged.
```

## G05-STOCK-Q027

```yaml
QID: G05-STOCK-Q027
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A manual quantity correction that changes on-hand quantity for a product does not leave the remaining cost
  layers in an inconsistent order that a later automatic consumption would then apply incorrectly.
WHY_IT_MATTERS: >
  A manual fix intended to correct one problem should not quietly create a second, harder-to-detect problem
  in future costing.
DISCONFIRMING_OBSERVATION: >
  After a manual quantity correction, a subsequent ordinary consuming movement is charged a cost inconsistent
  with the costing policy applied to the layers that remain.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Build multiple cost layers for a product, apply a manual quantity correction, then consume quantity through
  an ordinary movement and check the resulting charged cost against the policy.
```

## G05-STOCK-Q028

```yaml
QID: G05-STOCK-Q028
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a consuming movement takes more quantity than exists in the available cost layers, the cost assigned
  to the excess follows a documented, consistent rule rather than an arbitrary or zero value.
WHY_IT_MATTERS: >
  An arbitrary or zero cost for the excess understates cost of goods and overstates margin for exactly the
  units that are hardest to track.
DISCONFIRMING_OBSERVATION: >
  The excess quantity beyond available cost layers is charged a cost of zero or a cost that cannot be traced
  to any documented rule.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reduce available cost layers for a product to less than a planned consuming movement's quantity, complete
  the movement, and inspect the cost charged to the portion beyond the available layers.
```

## G05-STOCK-Q029

```yaml
QID: G05-STOCK-Q029
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A margin or cost-of-goods report for a period reflects the actual layer costs charged during that period,
  so that a layer-ordering error, if one occurred, is visible in the report rather than being masked by a
  report that recalculates cost independently.
WHY_IT_MATTERS: >
  A report that silently recalculates cost using a different method than what was actually charged would
  hide a real costing defect from the people relying on it.
DISCONFIRMING_OBSERVATION: >
  A margin or cost-of-goods report shows a cost for a consuming movement different from the cost actually
  charged and recorded at the time the movement completed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a consuming movement, note its recorded charged cost, then run a margin or cost-of-goods report
  covering that movement and compare the two figures.
```

## G05-STOCK-Q030

```yaml
QID: G05-STOCK-Q030
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether an outbound movement is allowed to bring on-hand quantity below zero is governed by an explicit,
  visible configuration setting rather than being an inherent, unconfigurable behaviour of every product.
WHY_IT_MATTERS: >
  A business that never wants negative quantity needs a control it can set and rely on, not an assumption
  about default behaviour that may vary by product or path.
DISCONFIRMING_OBSERVATION: >
  An outbound movement drives on-hand quantity below zero with no configuration setting found anywhere that
  governs whether this is permitted.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  With on-hand quantity at zero for a product, attempt an outbound movement and check both the result and
  whether a configuration setting exists to control it.
```

## G05-STOCK-Q031

```yaml
QID: G05-STOCK-Q031
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A movement that takes quantity below zero, when permitted, is assigned a cost using a documented rule
  (such as the most recent known cost) rather than a zero or undefined cost, and that assignment is corrected
  in a traceable way once a receipt later covers the shortfall.
WHY_IT_MATTERS: >
  An undefined cost during a negative period misstates cost of goods for exactly the transactions most likely
  to be scrutinized as unusual.
DISCONFIRMING_OBSERVATION: >
  A movement that takes on-hand quantity negative is recorded with a zero or blank cost, and no later
  correction ties that cost back to the receipt that eventually covers it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Permit a movement to take a product's quantity negative, inspect the cost it was assigned, then later
  record a covering receipt and check whether the earlier cost is reconciled.
```

## G05-STOCK-Q032

```yaml
QID: G05-STOCK-Q032
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Once a receipt arrives that covers a quantity that had gone negative, the valuation of the movements that
  consumed the negative quantity is corrected to reflect the actual received cost, through a visible
  correcting entry.
WHY_IT_MATTERS: >
  Without this correction, the period during which quantity was negative permanently carries an incorrect
  cost that is never reconciled to what the goods actually cost.
DISCONFIRMING_OBSERVATION: >
  A covering receipt arrives after a negative-quantity period and no correcting entry appears anywhere
  linking the receipt's actual cost back to the earlier movements that had consumed the shortfall.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Let a product's quantity go negative, then record a receipt that covers the shortfall, and search for a
  correcting entry tying the two together.
```

## G05-STOCK-Q033

```yaml
QID: G05-STOCK-Q033
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A product currently sitting at negative on-hand quantity is visibly flagged as such in ordinary quantity
  reporting, rather than being indistinguishable from a product simply at zero, and the corresponding
  negative position is reflected consistently in reported inventory value rather than shown as zero.
WHY_IT_MATTERS: >
  An unflagged negative position hides an operational problem (goods promised or shipped that were never
  actually received) that the business needs to actively chase, and a zeroed-out value hides the fact that a
  cost obligation already exists.
DISCONFIRMING_OBSERVATION: >
  A product at negative on-hand quantity appears in ordinary reporting with no visual or data distinction
  from a product legitimately at zero, or its reported value is shown as zero rather than a negative or
  otherwise flagged figure.
EXPECTED_SURFACE: S1,S2,S5,S6
PRECONDITIONS: >
  Bring a product's quantity to a negative value and inspect standard quantity and value reports and screens
  for any distinguishing indicator.
```

## G05-STOCK-Q034

```yaml
QID: G05-STOCK-Q034
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  An identifier for an individually tracked unit or batch is enforced as unique within its defined scope
  (such as per product, or per product and company), and the system rejects or flags an attempt to create a
  duplicate within that scope.
WHY_IT_MATTERS: >
  A duplicate identifier makes it impossible to know which physical unit or batch a later reference to that
  identifier actually means, defeating the purpose of individual tracking.
DISCONFIRMING_OBSERVATION: >
  Two distinct records are created carrying the identical identifier within the same defined scope, with no
  rejection or flag from the system.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Attempt to create a second individually tracked record using an identifier already in use within the same
  scope and observe whether it is accepted.
```

## G05-STOCK-Q035

```yaml
QID: G05-STOCK-Q035
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Splitting one tracked batch across two locations (or two documents) preserves the total quantity across the
  resulting parts and keeps both parts traceable back to the original batch identifier.
WHY_IT_MATTERS: >
  A split that loses the link to the origin makes any later recall or quality trace incomplete for part of
  the original batch.
DISCONFIRMING_OBSERVATION: >
  The sum of quantity across the split parts differs from the original batch quantity, or one of the
  resulting parts cannot be traced back to the original batch identifier.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Split a tracked batch of known quantity across two locations or documents, then check the resulting
  quantities and each part's traceability back to the original.
```

## G05-STOCK-Q036

```yaml
QID: G05-STOCK-Q036
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Merging two tracked batches into one preserves, in the resulting record's history, the fact that it
  originated from two distinct source batches rather than collapsing the history to show only one origin.
WHY_IT_MATTERS: >
  A collapsed history breaks a recall: if one of the two original batches is later found defective, the
  merged result should still be traceable to it.
DISCONFIRMING_OBSERVATION: >
  After merging two tracked batches, the resulting record's history shows only one of the two original
  batches as its origin.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Merge two distinct tracked batches into one and inspect the resulting record's origin history for both
  source batches.
```

## G05-STOCK-Q037

```yaml
QID: G05-STOCK-Q037
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  An individually tracked serial identifier that has been fully consumed, shipped out, or scrapped is not
  available for reassignment to a new, different physical unit while its history still needs to remain
  distinct.
WHY_IT_MATTERS: >
  Reusing a serial identifier for a second physical unit corrupts the history of both units under one
  identifier, defeating warranty and recall traceability.
DISCONFIRMING_OBSERVATION: >
  A new physical unit is successfully registered under a serial identifier that already has a complete prior
  history from a different physical unit.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Fully consume, ship, or scrap a serially tracked unit, then attempt to register a new unit under the same
  serial identifier.
```

## G05-STOCK-Q038

```yaml
QID: G05-STOCK-Q038
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  The uniqueness rule for a tracked identifier is enforced consistently regardless of whether the record is
  created through manual entry, a scanning input, or a bulk import, so that no one path can introduce a
  duplicate the other paths would reject.
WHY_IT_MATTERS: >
  A control enforced on only one entry path is not a real control once any other path exists to bypass it.
DISCONFIRMING_OBSERVATION: >
  An identifier already in use is successfully created a second time through a different entry path than the
  one that created the original, even though direct manual entry would have rejected it.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a tracked identifier through one entry path, then attempt to create the same identifier through a
  different entry path (such as a scan or an import) and compare the outcome.
```

## G05-STOCK-Q039

```yaml
QID: G05-STOCK-Q039
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A tracked batch reaching its expiry date while it is currently claimed against an outstanding demand either
  blocks that demand from proceeding against the expired batch or surfaces a clear warning, rather than
  silently allowing the expired batch to be picked and shipped as if unexpired.
WHY_IT_MATTERS: >
  Shipping an expired batch because a claim predated the expiry date is a product-safety and compliance
  failure hiding behind a timing coincidence.
DISCONFIRMING_OBSERVATION: >
  A batch that has passed its expiry date while claimed against a demand is picked and released for that
  demand with no block or warning distinguishing it from an unexpired batch.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Claim a batch against a demand before its expiry date, allow the expiry date to pass without fulfilling the
  demand, then attempt to complete the fulfillment.
```

## G05-STOCK-Q040

```yaml
QID: G05-STOCK-Q040
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Archiving or deactivating a tracked batch record that still carries on-hand quantity either is blocked or
  leaves that quantity still visible and accounted for elsewhere, rather than making the quantity disappear
  from ordinary quantity views.
WHY_IT_MATTERS: >
  Quantity that becomes invisible because its batch record was archived is physically still present but
  effectively lost to the business's own records.
DISCONFIRMING_OBSERVATION: >
  A batch carrying on-hand quantity is archived or deactivated and its quantity no longer appears in ordinary
  on-hand quantity totals for the product.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Archive or deactivate a tracked batch that still carries on-hand quantity and check whether that quantity
  still appears in the product's total on-hand figure.
```

## G05-STOCK-Q041

```yaml
QID: G05-STOCK-Q041
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  If picking an already-expired batch is possible at all, doing so requires an explicit override action
  distinguishable from an ordinary pick, and that override is traceable to the person who performed it.
WHY_IT_MATTERS: >
  Allowing an expired batch to be picked with no distinct override step and no trace means an expired-goods
  shipment could happen with nobody accountable for the decision.
DISCONFIRMING_OBSERVATION: >
  An already-expired batch is picked through the same steps as an unexpired batch, with no override step and
  no trace naming who picked it.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  With a batch already past its expiry date and still carrying quantity, attempt to pick it using the
  ordinary picking steps and observe whether any distinct override or trace appears.
```

## G05-STOCK-Q042

```yaml
QID: G05-STOCK-Q042
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Recording a quantity as scrapped produces an accounting entry that is distinguishable from an entry
  produced by ordinary outbound consumption (such as a sale), so that scrapped value is separately
  identifiable.
WHY_IT_MATTERS: >
  Scrap mixed indistinguishably into ordinary cost of goods overstates the apparent cost of normal sales and
  hides the true scale of loss.
DISCONFIRMING_OBSERVATION: >
  The accounting entry produced by a scrap action is indistinguishable in category from the entry produced by
  an ordinary sale consumption of the same product and quantity.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Record a scrap action for a known quantity and compare its accounting entry against the entry produced by
  an ordinary sale consumption of the same quantity.
```

## G05-STOCK-Q043

```yaml
QID: G05-STOCK-Q043
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Scrapping a quantity that is currently claimed against an outstanding demand but not yet physically picked
  also clears or clearly flags that demand's now-unfulfillable claim, rather than leaving the demand believing
  the quantity is still coming.
WHY_IT_MATTERS: >
  A demand left pointing at scrapped quantity will proceed as if fulfillment is still possible, creating a
  downstream failure with no upstream warning.
DISCONFIRMING_OBSERVATION: >
  After the claimed quantity behind a demand is scrapped, the demand still shows the quantity as reserved and
  available for future picking with no flag of the conflict.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Claim a quantity against a demand, scrap that same quantity before it is picked, and check the demand's
  resulting claim status.
```

## G05-STOCK-Q044

```yaml
QID: G05-STOCK-Q044
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A scrap action, once recorded, cannot be silently reversed by simply deleting the record; correcting a
  mistaken scrap requires a new, traceable compensating action that restores both quantity and value in a way
  visible in history.
WHY_IT_MATTERS: >
  A silently deleted scrap record erases the fact that a loss was ever recorded and reviewed, defeating the
  purpose of recording scrap at all.
DISCONFIRMING_OBSERVATION: >
  A recorded scrap action can be deleted outright, leaving no trace that it ever happened and no distinct
  compensating record of the correction.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record a scrap action, then attempt to undo it and observe whether the undo is a traceable compensating
  action or an outright deletion of the original record.
```

## G05-STOCK-Q045

```yaml
QID: G05-STOCK-Q045
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A direct quantity adjustment made outside the normal receive/ship/transfer flow is recorded with the same
  actor, timestamp, and reason traceability as an ordinary movement, not with lighter or optional
  traceability.
WHY_IT_MATTERS: >
  A quantity-changing path with weaker traceability than the normal flow becomes the path of least resistance
  for correcting (or hiding) discrepancies without accountability.
DISCONFIRMING_OBSERVATION: >
  A direct quantity adjustment is recorded with no actor, no timestamp, or no reason captured, while an
  ordinary movement always requires this information.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform a direct quantity adjustment and inspect what actor, timestamp, and reason information was
  captured, comparing it against what an ordinary movement requires.
```

## G05-STOCK-Q046

```yaml
QID: G05-STOCK-Q046
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A large or repeated direct quantity adjustment against the same product or location is surfaced in some way
  for review, rather than looking identical to a single, unremarkable correction with no distinguishing
  signal regardless of size or frequency.
WHY_IT_MATTERS: >
  A write path with no signal for unusual use is invisible to normal oversight and becomes an easy way to
  mask shrinkage, theft, or a recurring process failure.
DISCONFIRMING_OBSERVATION: >
  A series of repeated large direct adjustments against the same product or location produces no report,
  alert, or aggregate view different from a single ordinary correction.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Perform several direct quantity adjustments against the same product and location over a short period and
  check for any aggregate reporting or alerting distinct from viewing each adjustment individually.
```

## G05-STOCK-Q047

```yaml
QID: G05-STOCK-Q047
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Every direct quantity adjustment that changes recorded value produces a corresponding accounting entry,
  with no configuration or code path under which a value-changing adjustment can occur with no ledger trace
  at all.
WHY_IT_MATTERS: >
  A value change with no ledger entry breaks the fundamental link between physical quantity records and the
  financial books.
DISCONFIRMING_OBSERVATION: >
  A direct quantity adjustment that changes recorded value completes successfully with no corresponding
  accounting entry found anywhere.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Perform a direct quantity adjustment that changes recorded value and check for a corresponding accounting
  entry.
```

## G05-STOCK-Q048

```yaml
QID: G05-STOCK-Q048
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The permission required to perform a direct quantity adjustment is configured separately from the
  permission required to perform an ordinary movement, so that the two can be granted or withheld
  independently as a deliberate control decision.
WHY_IT_MATTERS: >
  If the two permissions are inseparable, the business cannot grant ordinary movement rights to warehouse
  staff while restricting the unaudited-adjustment path to a smaller group, which is exactly the control most
  businesses want.
DISCONFIRMING_OBSERVATION: >
  Granting a user the permission to perform ordinary movements automatically and unavoidably also grants the
  ability to perform direct quantity adjustments, with no separate setting to withhold the latter.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Configure a user with only ordinary movement permission and check whether a separate setting exists, and is
  enforced, to withhold direct adjustment permission from that same user.
```

## G05-STOCK-Q049

```yaml
QID: G05-STOCK-Q049
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A transfer of quantity from a location owned by one company to a location owned by a distinct company
  generates the intercompany accounting effect (such as a sale/purchase pair or an equivalent settlement
  record) appropriate to two separate legal entities exchanging goods, rather than being treated as an
  internal transfer with no financial boundary crossed.
WHY_IT_MATTERS: >
  Treating a cross-company movement as a costless internal transfer misstates both companies' books and can
  misstate intercompany balances relied on for statutory reporting.
DISCONFIRMING_OBSERVATION: >
  A transfer between locations belonging to two distinct companies completes with no accounting entry on
  either company's books reflecting a transaction between separate entities.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set up two locations each owned by a different company, transfer quantity between them, and inspect the
  accounting entries created on each company's books.
```

## G05-STOCK-Q050

```yaml
QID: G05-STOCK-Q050
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A user's ability to transfer quantity between two company-owned locations is subject to the same
  company-scope permission check as any other action that crosses a company boundary, not treated as an
  ordinary internal transfer exempt from that check.
WHY_IT_MATTERS: >
  An exemption here would let a user move value between two legally distinct entities without the
  authorization a cross-entity transaction should require.
DISCONFIRMING_OBSERVATION: >
  A user without permission scoped to one of the two companies involved is nonetheless able to complete a
  transfer between their two locations.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Configure a user with permission scoped to only one of two companies and attempt a transfer between a
  location owned by each company.
```

## G05-STOCK-Q051

```yaml
QID: G05-STOCK-Q051
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When the two companies in a cross-company transfer report in different currencies, the value recorded on
  each side of the transfer uses a documented, consistent exchange rate rather than each side independently
  deriving a different figure with no shared basis.
WHY_IT_MATTERS: >
  An unreconciled currency mismatch between two sides of the same physical transfer leaves an intercompany
  balance that can never be cleanly settled.
DISCONFIRMING_OBSERVATION: >
  The value recorded for the same transferred quantity differs between the two companies' books by more than
  the applicable exchange rate can explain, with no record of what rate was used.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Set the two companies involved in a transfer to report in different currencies, complete the transfer, and
  compare the recorded value and applied rate on each side.
```

## G05-STOCK-Q052

```yaml
QID: G05-STOCK-Q052
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A movement quantity that requires converting from a purchasing unit to a differently-scaled internal
  tracking unit is recorded with a defined, consistent rounding rule, and any resulting residue is visible
  rather than silently dropped or silently added.
WHY_IT_MATTERS: >
  A silently dropped or added fractional residue compounds over many movements into a discrepancy nobody can
  trace back to its cause.
DISCONFIRMING_OBSERVATION: >
  The recorded internal-unit quantity for a converted movement, multiplied back by the conversion factor,
  does not reconcile to the original unit's quantity, and no residue or rounding record explains the gap.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Record a movement whose quantity requires a non-whole conversion factor between two units and check whether
  the resulting quantity reconciles cleanly or leaves an unexplained residue.
```

## G05-STOCK-Q053

```yaml
QID: G05-STOCK-Q053
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The same conversion factor between an internal tracking unit and an external transaction unit is applied
  consistently whether that quantity is being received in one external unit or shipped out in a different
  external unit, so the same physical quantity converts back to the same internal amount either way, and the
  recorded value per internal unit stays consistent across both conversions.
WHY_IT_MATTERS: >
  An inconsistent factor between the receiving side and the shipping side of the same product silently
  creates or destroys quantity, or distorts value, on paper that never happened physically.
DISCONFIRMING_OBSERVATION: >
  Receiving and then fully shipping out the same physical quantity, using a different external unit on each
  side, leaves a nonzero remaining internal quantity with no physical counterpart, or the recorded per-unit
  value differs depending on which external unit was used.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Receive a quantity of a product using one external unit of measure, then ship out the equivalent physical
  quantity using a different external unit of measure, and check the resulting internal on-hand balance and
  its recorded value.
```

## G05-STOCK-Q054

```yaml
QID: G05-STOCK-Q054
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Changing the conversion factor between two units of measure for a product does not retroactively change the
  recorded internal quantity of movements that were already completed under the previous factor.
WHY_IT_MATTERS: >
  If historical movements silently reinterpret themselves under a new factor, any reconciliation performed
  before the change becomes invalid without anyone being told.
DISCONFIRMING_OBSERVATION: >
  The recorded internal quantity of a movement completed before a conversion factor change is different when
  inspected after the change than it was immediately after the movement completed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a movement under one conversion factor, note its recorded internal quantity, change the conversion
  factor, and inspect the same movement's recorded quantity again.
```

## G05-STOCK-Q055

```yaml
QID: G05-STOCK-Q055
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A quantity currently between two steps of a defined multi-step route (for example, arrived but not yet
  through an intermediate check) is queryable as being in that specific intermediate state, rather than
  appearing either fully at the origin step or fully at the final step with nothing in between.
WHY_IT_MATTERS: >
  Without visibility into the intermediate state, staff cannot answer where something is right now for goods
  that are legitimately mid-process, and cannot act on goods stuck partway through.
DISCONFIRMING_OBSERVATION: >
  A quantity known to be sitting at an intermediate step of a multi-step route cannot be distinguished, in any
  query or report, from quantity that has not yet started the route or has already completed it.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Move a quantity through the first step of a multi-step route without completing the remaining steps, then
  query the quantity's current state.
```

## G05-STOCK-Q056

```yaml
QID: G05-STOCK-Q056
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Quantity that has completed the first step of a multi-step route but not yet the second is counted exactly
  once in any total that spans both steps, not counted at both steps simultaneously, and the value associated
  with that quantity is likewise counted exactly once.
WHY_IT_MATTERS: >
  Double-counted in-transit quantity or value overstates total available or on-hand position, leading to
  promises or figures the business cannot back up.
DISCONFIRMING_OBSERVATION: >
  A total that is meant to span the whole multi-step route counts the same physical quantity twice because it
  currently sits between two of the route's steps, or the value associated with it is counted at both steps.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Move a quantity partway through a multi-step route and check whether a total spanning the whole route counts
  that quantity, and its value, once or more than once.
```

## G05-STOCK-Q057

```yaml
QID: G05-STOCK-Q057
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If a later step of a multi-step route is cancelled or fails after an earlier step already moved the
  quantity, the quantity's position and status are left in a defined, recoverable state, and no value already
  recognized for the cancelled step is left standing with no physical event to support it.
WHY_IT_MATTERS: >
  A quantity stranded in an undefined state after a partial route failure is effectively lost to normal
  operational visibility, and a dangling value entry misstates the books for an event that did not actually
  complete.
DISCONFIRMING_OBSERVATION: >
  After a later route step is cancelled following an earlier step's completion, the quantity's recorded
  location and status do not correspond to any location or status a person could act on, or a value entry
  tied to the cancelled step remains posted with nothing behind it.
EXPECTED_SURFACE: S1,S2,S5
PRECONDITIONS: >
  Complete the first step of a multi-step route, then cancel or fail the following step, and inspect the
  resulting recorded location, status, and any value entries tied to that quantity.
```

## G05-STOCK-Q058

```yaml
QID: G05-STOCK-Q058
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  The step of a multi-step route at which value or cost is recognized in the accounting entries is a fixed,
  documented point in the route, not one that varies depending on how many steps happen to be configured for
  a particular route.
WHY_IT_MATTERS: >
  If the recognition point silently shifts with route configuration, the same physical event (goods truly
  received or truly shipped) could be recognized at inconsistent times across different routes, corrupting
  period-to-period comparability.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical movements, routed through a different number of intermediate steps, recognize the
  accounting value of the goods at different physical points in the process.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Configure two routes for the same kind of movement with a different number of intermediate steps, complete
  both, and compare at which physical point each recognizes accounting value.
```

## G05-STOCK-Q059

```yaml
QID: G05-STOCK-Q059
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two operators attempting to validate the same single operation at effectively the same moment result in
  exactly one applied outcome; the second attempt is rejected or has no further effect, and only one
  corresponding accounting entry results, not two.
WHY_IT_MATTERS: >
  Two operators are a normal, expected real-world occurrence on a busy floor; a system not resilient to it
  will periodically apply one physical event, and its accounting effect, twice.
DISCONFIRMING_OBSERVATION: >
  Two operators validating the same operation at effectively the same moment both succeed and both apply
  their own quantity or status change, or two accounting entries are created for the two attempts even though
  only one physical operation occurred.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Have two sessions attempt to validate the same single operation as close together in time as the available
  interface allows and inspect whether one or both applied an effect, and how many accounting entries
  resulted.
```

## G05-STOCK-Q060

```yaml
QID: G05-STOCK-Q060
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Two operators picking from the same location for two different demands at effectively the same time cannot
  together remove more quantity than was actually present at that location at the start.
WHY_IT_MATTERS: >
  A race condition here creates a physical shortfall that traces back to two people each correctly following
  the system's instructions.
DISCONFIRMING_OBSERVATION: >
  The combined quantity picked by two operators from the same location for two different demands, occurring
  at effectively the same time, exceeds what was present at that location before either pick began.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Set a location's quantity to a known amount and have two operators attempt to pick against different
  demands from that location at effectively the same time, then compare the combined amount picked against
  what was present.
```

## G05-STOCK-Q061

```yaml
QID: G05-STOCK-Q061
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a concurrency conflict is detected between two operators acting on the same operation or location, at
  least one of them receives a clear indication that their action did not proceed as expected, rather than
  both operators seeing an ordinary success message while only one action actually took effect.
WHY_IT_MATTERS: >
  A silently failed action that reports success to the operator who performed it leaves that person believing
  they completed work that never actually happened.
DISCONFIRMING_OBSERVATION: >
  Following a detected concurrency conflict, the operator whose action did not take effect nonetheless
  receives the same success indication as the operator whose action did take effect.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Trigger a concurrency conflict between two operators on the same operation and observe what each operator's
  interface reports as the outcome.
```

## G05-STOCK-Q062

```yaml
QID: G05-STOCK-Q062
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Forcing a demand to show as available for fulfillment despite insufficient actual on-hand quantity requires
  a permission distinct from ordinary fulfillment permission, and the forced state is visibly flagged as such
  rather than looking identical to a demand that is genuinely available.
WHY_IT_MATTERS: >
  An unflagged forced availability lets a false promise travel downstream (to picking, shipping, even
  invoicing) looking exactly like a real one.
DISCONFIRMING_OBSERVATION: >
  A demand is forced to show as available despite insufficient on-hand quantity, using only ordinary
  fulfillment permission, and the resulting record is indistinguishable from a genuinely available demand.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  With insufficient on-hand quantity for a demand, attempt to force it into an available state using only
  ordinary fulfillment permission and inspect whether it succeeds and whether it is flagged.
```

## G05-STOCK-Q063

```yaml
QID: G05-STOCK-Q063
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Manually reassigning a unit's claim from one demand to another, overriding the original claimant, retains a
  record of which demand originally held the claim and who performed the reassignment.
WHY_IT_MATTERS: >
  Without this trace, the person whose demand lost its claim has no way to know the loss was a deliberate
  override rather than an ordinary allocation outcome, and no one is accountable for the decision.
DISCONFIRMING_OBSERVATION: >
  After a claim is manually reassigned from one demand to another, no record identifies the original
  claimant, the new claimant, or who performed the reassignment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Manually reassign a claimed unit from one demand to a different demand and inspect the resulting trace for
  the original claimant and the actor who made the change.
```

## G05-STOCK-Q064

```yaml
QID: G05-STOCK-Q064
MODULE: stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A demand that was forced into an available state ahead of actual on-hand quantity is reconciled once the
  real supply arrives, so that the forced state does not persist indefinitely once the underlying shortfall is
  resolved.
WHY_IT_MATTERS: >
  A forced state left unreconciled after the shortfall is resolved makes it impossible to tell, later, which
  fulfillments were ever actually backed by real quantity at the time they were promised.
DISCONFIRMING_OBSERVATION: >
  After the real supply that a forced availability was anticipating arrives and is recorded, the demand's
  forced-availability flag remains unresolved with no link drawn between the two events.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Force a demand into an available state ahead of actual quantity, then record the receipt that covers the
  shortfall, and check whether the forced flag is resolved and linked to that receipt.
```

---
## GMVQ Internal QA Checklist

- [x] 64 distinct MVQ records (exceeds the 48 floor; no padding — every record targets a distinct
      hypothesis).
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`.
- [x] Questions are behavioral and source-neutral; no vendor/product name, technical identifier, or module
      name appears in question text.
- [x] Reservation/claim fairness, determinism, visibility, and staleness represented (Q001-Q007).
- [x] Partial receipt, over-receipt, multi-partial summation, and receipt-time unit conversion represented
      (Q008-Q013).
- [x] Duplicate/repeat validation of an already-completed movement, including concurrency and audit trail,
      represented (Q014-Q017).
- [x] Backdated movement into a closed period, including ledger and historical-report consequence,
      represented (Q018-Q021).
- [x] Valuation method changed while quantity exists, including historical-cost preservation and rollback,
      represented (Q022-Q025).
- [x] Cost layers consumed out of order, including manual-correction disruption and margin-report
      consistency, represented (Q026-Q029).
- [x] Negative on-hand quantity, its costing, retroactive correction, and reporting visibility represented
      (Q030-Q033).
- [x] Lot/serial uniqueness, split, merge, and reuse after full consumption represented (Q034-Q038).
- [x] A batch expiring or archived while still claimed represented (Q039-Q041).
- [x] Scrap, its ledger distinction, and reversal represented (Q042-Q044).
- [x] Direct quantity adjustment as a lightly-audited write path represented (Q045-Q048).
- [x] Cross-company warehouse transfer, its accounting and currency consistency, represented (Q049-Q051).
- [x] Unit conversion across purchase/stock/sale units, including rounding residue, represented (Q052-Q054).
- [x] Multi-step route partial completion, double-counting, and ledger timing represented (Q055-Q058).
- [x] Concurrency between two operators on one operation or one location represented (Q059-Q061).
- [x] Forced availability and reservation override, with trace and later reconciliation, represented
      (Q062-Q064).
- [x] `LAYER: BASE` or `LAYER: PROCESS` tagged on every question.
- [x] 26 of 64 questions carry `S2` in `EXPECTED_SURFACE`, giving the group's ledger-bridge risk direct
      coverage from the base module.
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
