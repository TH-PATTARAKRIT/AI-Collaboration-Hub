# SMEsPlus ENTERPRISE SUITE
## GMVQ — G05 INVENTORY / delivery_stock_picking_batch Module Adversarial MVQ Bank

**Document ID:** GMVQ-G05-DELIVERY_STOCK_PICKING_BATCH-MVQ48-V1.00
**Group:** G05 INVENTORY
**Module Metadata:** `delivery_stock_picking_batch`
**Wave:** W2
**Author Cell:** TEAM P03 (GMVQ Question Factory — Production Cell P03, Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This module is a seam of a seam: it applies carrier handling not to one outbound movement but to a batch
of them. This bank supplements the 55 Standard Questions with module-specific, adversarial questions
covering: one batch spanning several carriers or several destinations; cost allocated across the batch and
the residual on each movement; one movement in the batch failing or being removed after labels were
produced for all of them; the batch partially dispatched; a movement added to a batch after processing
began; two operators working the same batch; a batch cancelled after some of its movements completed; the
batch's carrier state versus each member movement's state; ordering within a batch when sequence matters;
and reporting a batch as delivered when only part of it was.

Per the Bridge Module Rule (V1.00), every question below fails only at the batch seam: if a question would
still make sense asked of a single movement handled on its own, it does not belong in this bank and was
excluded rather than authored and later cut. Question text is source-neutral: no vendor or product name,
no technical identifier (model, table, field, method, XML ID, API path), and no reference to how any
specific implementation is built. Language is generic business/behavioural language throughout.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, auditability, tenant/company boundary, concurrency and ordering,
  and runtime reachability — every one of them at the batch level specifically.
- This module carries one layer only (batch-level runtime behaviour); the `LAYER` field is omitted
  throughout, consistent with the Authoring Standard.
- Pre-authoring sibling check (Bridge Module Rule §5): `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G05_INVENTORY/*.md`
  was run before authoring, after the `stock_delivery` bank in this same group was written, and against
  every other G05 INVENTORY bank present on disk at authoring time (`stock`, `stock_account`,
  `stock_landed_costs`, `barcodes`, `barcodes_gs1_nomenclature`, `product_expiry`, `repair` — 402
  HYPOTHESIS lines in total). None concerned carrier handling of more than one movement at once, so none
  of this bank's questions duplicate a sibling's. Every candidate question that would have made equal sense
  asked of one movement alone was cut per the Bridge Module Rule's test rather than kept.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a
  Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G05-DELIVERY_STOCK_PICKING_BATCH-Q001

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q001
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A batch containing movements addressed to different carriers is either rejected from having a single
  batch-level carrier action, or is split at the point of carrier handling into carrier-specific groups,
  rather than one carrier silently being applied to every movement in the batch regardless of which
  carrier each one actually needs.
WHY_IT_MATTERS: >
  Silently applying one carrier to movements that need a different one either fails at the carrier's own
  intake or, worse, ships goods through the wrong carrier entirely.
DISCONFIRMING_OBSERVATION: >
  A batch containing movements destined for different carriers completes a single batch-level carrier
  booking that assigns one carrier to all of them regardless of what each movement actually required.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Build a batch from movements that individually require different carriers and attempt a single
  batch-level carrier booking action.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q002

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q002
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A batch containing movements addressed to several distinct delivery destinations produces carrier
  documentation (labels, manifests) that correctly reflects each movement's own destination, rather than
  one destination from the batch being applied to documentation covering all of them.
WHY_IT_MATTERS: >
  A shared destination on all documentation for a multi-destination batch would misdirect every movement
  but the one whose destination was actually used.
DISCONFIRMING_OBSERVATION: >
  Carrier documentation generated for the batch shows a single destination applied uniformly, even though
  the batch's individual movements have different destinations.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Build a batch of movements with distinct destinations, generate carrier documentation at the batch
  level, and check whether it reflects each movement's own destination.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q003

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q003
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a batch is allowed to mix several carriers or several destinations at all is a configurable or
  explicitly enforced rule, rather than an unstated behaviour that differs depending on how the batch
  happens to have been assembled.
WHY_IT_MATTERS: >
  An unstated, inconsistent rule about whether mixing is allowed means operators cannot predict, before
  building a batch, whether it will be usable for a combined carrier action.
DISCONFIRMING_OBSERVATION: >
  Whether a batch mixing several carriers or destinations can proceed to a batch-level carrier action
  varies inconsistently, with no discoverable rule or setting explaining when it is or is not allowed.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Attempt to run a batch-level carrier action on batches assembled with mixed carriers or mixed
  destinations several times, and look for a consistent, documented rule governing the outcome.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q004

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q004
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a batch spans several destinations, the shipment count and tracking identities produced correspond
  to the number of distinct end points actually being shipped to, rather than a single tracking identity
  trying to represent multiple physically distinct destinations at once.
WHY_IT_MATTERS: >
  One tracking identity covering shipments to several different addresses cannot meaningfully answer "did
  this specific destination receive its goods".
DISCONFIRMING_OBSERVATION: >
  A batch spanning several distinct destinations results in a single tracking identity that is expected to
  represent delivery to all of them.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Process a batch with movements to several distinct destinations through a batch-level carrier action and
  count the tracking identities produced against the number of destinations.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q005

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q005
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A batch is prevented from mixing movements that belong to different companies before any batch-level
  carrier action can be attempted, rather than allowing a cross-company batch to reach the carrier step
  and only then behaving unpredictably.
WHY_IT_MATTERS: >
  A cross-company batch reaching carrier booking risks charging one company's carrier account for another
  company's goods.
DISCONFIRMING_OBSERVATION: >
  A batch containing movements belonging to more than one company is allowed to proceed to a batch-level
  carrier action.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Attempt to build a batch from movements belonging to two different companies and proceed to a
  batch-level carrier action.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q006

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q006
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a single carrier charge is incurred for the batch as a whole, that charge is allocated across the
  batch's individual movements by a defined basis (such as weight or line count), so that the sum of what
  is allocated to each movement reconciles back to the one batch-level charge.
WHY_IT_MATTERS: >
  An allocation that doesn't reconcile back to the actual batch charge either overstates or understates the
  true shipping cost attributed to individual movements, corrupting per-movement cost reporting.
DISCONFIRMING_OBSERVATION: >
  The amounts allocated to the batch's individual movements do not sum back to the single carrier charge
  incurred for the batch.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Incur one carrier charge for a batch of several movements, allocate it across those movements, and sum
  the allocated amounts against the original charge.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q007

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q007
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A residual amount left over after allocating a batch-level cost across its movements by a chosen basis
  (a rounding remainder) is assigned somewhere identifiable, rather than silently vanishing or being
  absorbed without record into whichever movement happens to be processed last.
WHY_IT_MATTERS: >
  A vanishing rounding residual, repeated across many batches, becomes a real, unexplained gap between
  total shipping cost incurred and total shipping cost allocated.
DISCONFIRMING_OBSERVATION: >
  The sum of individually allocated amounts differs from the original batch charge by a residual that
  cannot be traced to where it went.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Allocate a batch-level cost across movements using a basis that does not divide evenly, and trace where
  any rounding residual ends up.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q008

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q008
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The basis used to allocate a batch-level carrier cost across its movements (by weight, by value, by line
  count, evenly) is a configurable choice, not a single fixed method applied regardless of what the
  business actually wants to reflect.
WHY_IT_MATTERS: >
  A business that wants cost allocated by weight cannot get accurate per-movement cost reporting if only an
  even split is available.
DISCONFIRMING_OBSERVATION: >
  There is only one fixed allocation basis available for batch-level carrier cost, with no way to
  configure or select a different one.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Look for a configuration option governing the basis used to allocate batch-level carrier cost, and
  attempt to select a different basis.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q009

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q009
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a movement is removed from a batch after a batch-level cost has already been allocated across it and
  its siblings, the allocation is recalculated across the movements that remain, rather than the removed
  movement's share being silently lost or permanently left on the remaining movements' totals without
  adjustment.
WHY_IT_MATTERS: >
  An unadjusted allocation after a movement leaves the batch either overcharges the remaining movements or
  understates the true cost attached to the one that was removed.
DISCONFIRMING_OBSERVATION: >
  Removing a movement from a batch after cost allocation leaves the remaining movements' allocated amounts
  unchanged, still summing to the original batch total as if the removed movement were still part of it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Allocate a batch-level cost across several movements, remove one movement from the batch, and check
  whether the allocation is recalculated.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q010

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q010
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The batch-level cost allocation is traceable back to the specific batch-level carrier charge it derived
  from, so that a later reconciliation against the carrier's own invoice can identify which movements
  shared which charge.
WHY_IT_MATTERS: >
  Without that traceability, reconciling the carrier's consolidated invoice against internal records
  requires manually reconstructing which movements were in which batch at the time.
DISCONFIRMING_OBSERVATION: >
  A movement's allocated shipping cost carries no reference back to the batch-level charge or the batch it
  was allocated from.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Allocate a batch-level charge across movements and check whether each movement's allocated amount
  references the source batch charge.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q011

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q011
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When carrier labels have already been produced for every movement in a batch and one of those movements
  subsequently fails or is removed, the remaining movements' labels and bookings stay valid and
  unaffected, rather than the whole batch-level carrier action being invalidated for all of them.
WHY_IT_MATTERS: >
  Invalidating every movement's label because one movement in the batch failed forces needless re-work on
  shipments that were never the problem.
DISCONFIRMING_OBSERVATION: >
  One movement failing or being removed from a batch after labels were produced causes the labels or
  bookings of the batch's other, unaffected movements to also become invalid.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Produce labels for every movement in a batch, then fail or remove one movement, and check the state of
  the others' labels and bookings.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q012

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q012
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A carrier tracking identity already issued to a movement that is then removed from its batch is voided
  or flagged for resolution, rather than remaining active and orphaned from a batch that no longer
  includes it.
WHY_IT_MATTERS: >
  An orphaned, still-active tracking identity for a movement no longer in any batch risks an uncontrolled
  carrier collection for a shipment nobody is now tracking.
DISCONFIRMING_OBSERVATION: >
  A movement removed from its batch after receiving a tracking identity keeps that identity active with no
  flag or link connecting it to anything still being tracked.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Issue tracking identities to every movement in a batch, remove one movement from the batch afterward,
  and check the state of that movement's tracking identity.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q013

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q013
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If a batch-level carrier cost was computed assuming every movement's label would be produced, and one
  movement is then removed after the fact, the batch-level cost is revisited rather than the batch
  continuing to reflect a cost basis that no longer matches what is actually being sent.
WHY_IT_MATTERS: >
  A stale batch-level cost basis after a movement is pulled out overstates the true shipping cost of what
  actually goes out with the batch.
DISCONFIRMING_OBSERVATION: >
  The batch-level shipping cost remains unchanged after a movement it was based on is removed following
  label production.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Compute a batch-level shipping cost with all movements' labels produced, remove one movement, and check
  whether the batch-level cost is revisited.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q014

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q014
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A movement that fails at the carrier's own intake after batch-level labels were already produced for the
  whole batch is distinguishable, in the batch's own record, from a movement that succeeded, rather than
  the batch showing a uniform outcome for all its members.
WHY_IT_MATTERS: >
  A uniform batch-level outcome hides exactly which one movement needs attention, forcing a manual check of
  every movement in the batch to find it.
DISCONFIRMING_OBSERVATION: >
  After one movement in a fully labelled batch fails at carrier intake, the batch's own record shows the
  same outcome for every movement, with no indication of which one failed.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Produce labels for a full batch, simulate one movement failing at carrier intake, and check whether the
  batch record distinguishes it from the movements that succeeded.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q015

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q015
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Re-attempting the carrier action for only the one movement that failed, after the rest of the batch
  already succeeded, is possible without repeating the batch-level action for the movements that already
  have valid labels.
WHY_IT_MATTERS: >
  Forcing the whole batch to be re-run to fix one failed movement risks producing duplicate labels or
  duplicate bookings for the movements that already succeeded.
DISCONFIRMING_OBSERVATION: >
  The only available way to resolve one failed movement in an otherwise successful batch is to re-run the
  batch-level carrier action for every movement in it.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Have one movement fail carrier intake within an otherwise successful batch, and attempt to resolve only
  that one movement.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q016

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q016
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A batch in which some movements have been physically dispatched and others have not yet left shows a
  state that reflects that partial reality, rather than the batch as a whole being represented as either
  fully dispatched or not dispatched at all.
WHY_IT_MATTERS: >
  A batch falsely shown as fully dispatched hides which specific movements are still sitting in the
  warehouse waiting to go.
DISCONFIRMING_OBSERVATION: >
  A batch with only some of its movements physically dispatched shows the same overall state as a batch
  where either all or none have been dispatched.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Dispatch only some of the movements in a batch and inspect the batch's own overall state against the
  states of its individual movements.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q017

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q017
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The movements remaining undispatched in a partially dispatched batch can still be acted on individually
  (dispatched later, cancelled, moved to another batch) without requiring the entire batch to be undone
  first.
WHY_IT_MATTERS: >
  Forcing the whole batch to be undone to handle its slower-moving remainder needlessly disturbs the
  movements that have already dispatched correctly.
DISCONFIRMING_OBSERVATION: >
  Acting on the undispatched remainder of a partially dispatched batch requires first undoing or unwinding
  the batch's already-dispatched movements.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Partially dispatch a batch, then attempt to act individually on one of the remaining, undispatched
  movements.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q018

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q018
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A batch-level carrier cost tied to the full, original batch is not treated as fully incurred the moment
  only part of the batch has actually dispatched; the portion attributable to the undispatched movements is
  distinguishable from cost that has actually been incurred.
WHY_IT_MATTERS: >
  Recognising the full batch cost against a partial dispatch overstates incurred shipping cost for goods
  that have not yet actually left.
DISCONFIRMING_OBSERVATION: >
  The full batch-level carrier cost is recorded as incurred as soon as any part of the batch dispatches,
  with no distinction for the portion still undispatched.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially dispatch a batch with a batch-level carrier cost already computed, and inspect how much of
  that cost is treated as incurred.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q019

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q019
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A batch can be closed out or marked complete only once every one of its movements has reached a terminal
  state (dispatched, cancelled, or otherwise resolved), rather than being closeable while movements are
  still pending.
WHY_IT_MATTERS: >
  Allowing a batch to be marked complete while movements are still pending buries those pending movements
  from further attention.
DISCONFIRMING_OBSERVATION: >
  A batch can be marked complete or closed while some of its movements are still pending, with no warning
  or block.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attempt to close or mark a batch complete while some of its movements remain undispatched or unresolved.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q020

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q020
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A movement added to a batch after the batch-level carrier action has already been performed for the
  movements originally in it is either processed through its own subsequent carrier action or clearly
  flagged as not yet covered, rather than being silently treated as if it already shared in the earlier
  action.
WHY_IT_MATTERS: >
  A movement silently assumed to be already labelled and booked, when it never went through the carrier
  action at all, ships without any label or tracking.
DISCONFIRMING_OBSERVATION: >
  A movement added to a batch after its batch-level carrier action already ran is shown with the same
  carrier status as the movements that were actually included in that action.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Run a batch-level carrier action for a batch, then add a new movement to the same batch, and compare its
  carrier status to the movements already processed.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q021

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q021
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Adding a movement to a batch after processing began does not retroactively alter the cost already
  allocated to the movements processed earlier in that batch.
WHY_IT_MATTERS: >
  Retroactively changing an already-communicated cost allocation for movements that already shipped
  creates figures that no longer match what was recorded or reported at the time.
DISCONFIRMING_OBSERVATION: >
  Adding a new movement to a batch after its earlier movements were already processed and cost-allocated
  changes the allocated amounts already recorded on those earlier movements.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Process and cost-allocate part of a batch, add a new movement afterward, and check whether the earlier
  movements' allocated costs change.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q022

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q022
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a batch remains open to new movements once its carrier action has started is a defined, enforced
  state, rather than an unstated behaviour where a batch sometimes accepts additions and sometimes does not
  with no discoverable rule.
WHY_IT_MATTERS: >
  An unpredictable rule about whether a batch can still receive movements means operators cannot know, when
  planning a batch, when it becomes safe to add one more.
DISCONFIRMING_OBSERVATION: >
  Whether a movement can be added to a batch after its carrier action has started differs unpredictably,
  with no discoverable rule or state governing it.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Attempt to add a movement to a batch at several points after its carrier action has started, and look
  for a consistent, discoverable rule.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q023

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q023
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A movement belonging to a different company than the batch it is being added to is prevented from being
  added, consistent with the boundary already enforced when a batch is first assembled.
WHY_IT_MATTERS: >
  Allowing a late addition to bypass a boundary enforced at batch creation would make the company boundary
  depend on timing rather than being a real, standing rule.
DISCONFIRMING_OBSERVATION: >
  A movement belonging to a different company than the batch's existing movements can be added to that
  batch after it was originally assembled.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to add a movement from a different company to an existing batch partway through its processing.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q024

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q024
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two operators trigger the batch-level carrier action for the same batch at effectively the same
  time, exactly one action takes effect for the batch as a whole, rather than both succeeding and
  producing duplicate labels or duplicate bookings across the batch's movements.
WHY_IT_MATTERS: >
  Duplicate batch-level bookings multiply carrier charges and produce conflicting tracking identities
  across every movement in the batch at once, not just one.
DISCONFIRMING_OBSERVATION: >
  Two concurrent batch-level carrier actions on the same batch both succeed, producing duplicate labels or
  bookings across the batch's movements.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger two near-simultaneous batch-level carrier actions on the same batch and observe how many
  complete.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q025

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q025
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  One operator removing a movement from a batch while a second operator is mid-way through running that
  batch's carrier action results in a consistent outcome for the removed movement (either it is excluded
  cleanly or the action is blocked), rather than an undefined, inconsistent state depending on exact
  timing.
WHY_IT_MATTERS: >
  An undefined outcome from this ordinary race leaves it a matter of luck whether a removed movement still
  ends up wrongly included in a live carrier action.
DISCONFIRMING_OBSERVATION: >
  A movement removed from a batch while its carrier action is mid-flight is sometimes included in the
  resulting bookings and sometimes not, with no consistent rule.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Remove a movement from a batch while its batch-level carrier action is in progress, repeated across
  attempts, and check for a consistent outcome.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q026

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q026
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two operators each individually working different movements within the same batch (one picking, one
  handling the carrier step) do not overwrite each other's progress on the batch's shared record.
WHY_IT_MATTERS: >
  One operator's carrier-step update silently overwriting another's picking progress on the same batch
  record loses real work and can misstate what has actually been done.
DISCONFIRMING_OBSERVATION: >
  One operator's update to the batch while working a movement overwrites a different, unrelated update
  another operator made to the same batch at nearly the same time.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have two operators update different aspects of the same batch at nearly the same time and check whether
  either update is lost.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q027

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q027
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Which operator is considered responsible for a batch's carrier-level outcome (for audit and
  accountability) is recorded per action taken, rather than the batch attributing every action uniformly
  to whichever operator originally created it.
WHY_IT_MATTERS: >
  Attributing every batch action to its creator regardless of who actually triggered the carrier step
  misrepresents who is accountable for what actually happened.
DISCONFIRMING_OBSERVATION: >
  A batch-level carrier action performed by an operator other than the batch's creator is recorded as if
  the creator performed it.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Have an operator other than the batch's creator perform its batch-level carrier action, and check who is
  recorded as responsible for that action.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q028

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q028
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a batch after some of its movements have already been dispatched and completed does not
  retroactively cancel or disturb those already-completed movements; only the movements still pending
  within the batch are affected.
WHY_IT_MATTERS: >
  Retroactively disturbing already-completed, physically-shipped movements when a batch is cancelled
  creates a record that contradicts what has actually, physically happened.
DISCONFIRMING_OBSERVATION: >
  Cancelling a batch changes the state of movements within it that had already been dispatched and
  completed before the cancellation.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Complete some movements within a batch, cancel the batch, and check whether the already-completed
  movements are affected.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q029

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q029
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Carrier tracking identities already issued to the still-pending movements of a batch that is then
  cancelled are voided or flagged, consistent with how a single cancelled movement's own tracking identity
  would be handled.
WHY_IT_MATTERS: >
  A batch-level cancellation that skips voiding pending movements' tracking identities leaves live
  shipments with a carrier that nothing internally still expects.
DISCONFIRMING_OBSERVATION: >
  Cancelling a batch leaves its still-pending movements' already-issued tracking identities active, with no
  voiding or flag raised.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Issue tracking identities to a batch's pending movements, cancel the batch, and check the state of those
  tracking identities.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q030

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q030
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cancelled batch retains a record of which of its movements had already completed at the moment of
  cancellation, so that the boundary between what happened before and after cancellation remains
  reconstructable later.
WHY_IT_MATTERS: >
  Losing that boundary makes it impossible to later explain which movements actually shipped under a batch
  that was ultimately cancelled.
DISCONFIRMING_OBSERVATION: >
  After a batch is cancelled, there is no way to determine which of its movements had already completed at
  the point of cancellation versus which were still pending.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete part of a batch, cancel the rest, and later attempt to reconstruct which movements were done at
  the time of cancellation.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q031

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q031
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A batch that is cancelled while it still has completed movements within it is represented as partially,
  not fully, cancelled, distinguishing it from a batch cancelled before any movement completed.
WHY_IT_MATTERS: >
  Treating a partially-completed cancellation identically to a clean, fully-uncompleted cancellation
  obscures that real shipments actually went out under that batch.
DISCONFIRMING_OBSERVATION: >
  A batch cancelled with some movements already completed shows the same cancelled state as a batch
  cancelled before anything in it was ever processed.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Cancel one batch before any movement completes and another after some movements completed, then compare
  the resulting states.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q032

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q032
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The batch's own carrier-facing state (booked, in transit, delivered) is derived consistently from the
  actual states of its member movements, rather than the batch showing a status that no combination of its
  members' individual states could actually produce.
WHY_IT_MATTERS: >
  A batch status detached from its members' real states misleads anyone who trusts the batch view instead
  of checking every movement individually.
DISCONFIRMING_OBSERVATION: >
  The batch shows a carrier state (for example, fully delivered) that does not correspond to any consistent
  combination of its member movements' own actual states.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Put the batch's member movements into a known mixture of states and compare the batch's own reported
  carrier state against that mixture.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q033

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q033
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a member movement's carrier status changes independently (through a carrier feed update to that one
  movement), the batch's own aggregate status reflects that change rather than remaining stuck at whatever
  it showed when the batch-level action last ran.
WHY_IT_MATTERS: >
  A batch status that never reflects a single member's later status change becomes stale and misleading the
  moment any one shipment's real-world progress diverges from the rest.
DISCONFIRMING_OBSERVATION: >
  A member movement's carrier status changes but the batch's own aggregate status does not reflect that
  change at all.
EXPECTED_SURFACE: S1,S5,S8
PRECONDITIONS: >
  Change one member movement's carrier status independently after the batch action ran, and check whether
  the batch's own aggregate status updates.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q034

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q034
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A contradiction between the batch's own recorded carrier state and what its individual member movements
  actually show is surfaced as something to resolve, rather than the batch view and the movement-level view
  being allowed to silently disagree indefinitely.
WHY_IT_MATTERS: >
  A silent, indefinite disagreement between the batch view and the movement-level view means whichever one
  a report happens to use gives a different answer to the same real-world question.
DISCONFIRMING_OBSERVATION: >
  The batch-level carrier state and the actual states of its member movements disagree, and nothing in the
  record flags the disagreement.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Force a mismatch between the batch's aggregate carrier state and its members' actual states, and check
  whether that mismatch is surfaced anywhere.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q035

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q035
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A batch is only shown as fully delivered when every one of its member movements has independently
  reached a delivered state, not merely when the batch-level carrier action itself completed without
  error.
WHY_IT_MATTERS: >
  Equating "the batch-level action ran without error" with "everything in the batch was delivered"
  confuses a booking-time success with an actual, later delivery outcome.
DISCONFIRMING_OBSERVATION: >
  The batch is shown as fully delivered immediately once its batch-level carrier action completes, even
  though its individual member movements have not yet independently reached a delivered state.
EXPECTED_SURFACE: S1,S5,S8
PRECONDITIONS: >
  Complete a batch-level carrier action and, before any member movement independently reaches delivered
  status, check what the batch itself reports.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q036

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q036
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where the sequence in which a batch's movements are handled to the carrier matters (for example, a
  required collection or drop order), that sequence is preserved through to the carrier-facing
  documentation, rather than being lost once the movements are grouped into one batch-level action.
WHY_IT_MATTERS: >
  Losing a required sequence at the batch step defeats the reason the sequence was needed in the first
  place, once the shipment is physically in the carrier's hands.
DISCONFIRMING_OBSERVATION: >
  A deliberate sequence assigned to a batch's movements is not reflected anywhere in the carrier-facing
  documentation produced for that batch.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Assign a deliberate handling sequence to a batch's movements and check whether that sequence appears in
  the resulting carrier documentation.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q037

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q037
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reordering the movements within a batch before its carrier action has run changes the sequence used for
  that action, rather than the original order being fixed and unresponsive to a later, deliberate
  reordering.
WHY_IT_MATTERS: >
  An unresponsive, fixed order despite a deliberate reordering means an operator's correction never
  actually takes effect where it matters.
DISCONFIRMING_OBSERVATION: >
  Reordering a batch's movements before running its carrier action has no effect on the sequence actually
  used by that action.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Reorder a batch's movements before its carrier action runs, then check whether the action's own sequence
  reflects the reordering.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q038

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q038
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Inserting a movement into the middle of an already-sequenced batch (rather than appending it at the end)
  either re-establishes a coherent overall sequence or is clearly flagged as unsequenced, rather than
  silently breaking the ordering of movements that were already placed correctly.
WHY_IT_MATTERS: >
  A silently broken sequence downstream of a mid-batch insertion defeats the ordering without anyone
  noticing until the carrier acts on the wrong order.
DISCONFIRMING_OBSERVATION: >
  Inserting a movement into the middle of an already-sequenced batch produces a sequence that no longer
  matches what was deliberately set for the movements around it, with no flag raised.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Insert a movement into the middle of a batch that already has a deliberate sequence, and check the
  resulting order.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q039

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q039
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two movements within a batch have genuinely conflicting sequence requirements (each needing to be
  handled before the other for a legitimate but different reason), that conflict is surfaced rather than
  one requirement being silently discarded in favour of the other.
WHY_IT_MATTERS: >
  Silently discarding one of two legitimate, conflicting sequence requirements satisfies one business need
  while unknowingly breaking the other.
DISCONFIRMING_OBSERVATION: >
  A batch containing two movements with genuinely conflicting sequence requirements proceeds with one
  requirement silently dropped and no indication that a conflict existed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Construct a batch with two movements carrying conflicting sequence requirements and observe how the
  conflict is handled.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q040

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q040
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A batch report or summary view distinguishes a batch where every movement has been confirmed delivered
  from one where only some of its movements have been, rather than presenting both as simply "delivered"
  once any threshold of the batch is reached.
WHY_IT_MATTERS: >
  Reporting a partially-delivered batch as delivered creates false confidence that a customer or downstream
  process received everything it was expecting from that batch.
DISCONFIRMING_OBSERVATION: >
  A batch report shows a batch as delivered while some of its member movements have not actually been
  confirmed delivered.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Confirm delivery for only some of a batch's movements and check what the batch-level report or summary
  shows.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q041

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q041
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A notification or downstream event fired on a batch being "delivered" only fires once every movement
  within it has actually reached that state, rather than firing on the first movement's delivery as if it
  applied to the whole batch.
WHY_IT_MATTERS: >
  A downstream action (a customer notification, an invoicing trigger) firing on partial delivery falsely
  tells the customer or the ledger that the full batch already arrived.
DISCONFIRMING_OBSERVATION: >
  A batch-level delivered notification or downstream event fires as soon as one member movement is
  delivered, without waiting for the rest of the batch.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Deliver only one movement in a multi-movement batch and check whether a batch-level delivered
  notification or downstream event fires.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q042

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q042
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The proportion of a batch actually delivered, at any point in time, can be determined from the batch's
  own record without having to open and check every member movement individually.
WHY_IT_MATTERS: >
  Forcing a manual check of every individual movement to know how much of a batch has actually arrived
  defeats the purpose of having a batch-level view at all.
DISCONFIRMING_OBSERVATION: >
  There is no way, from the batch's own record, to tell how many of its movements have been delivered
  without opening each movement individually.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Partially deliver a batch and attempt to determine, from the batch's own view alone, how much of it has
  arrived.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q043

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q043
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A batch permanently stuck with one movement that never reaches a resolved state (delivered, cancelled, or
  otherwise closed) is distinguishable, over time, from a batch that is simply still in normal progress,
  rather than the two looking identical indefinitely.
WHY_IT_MATTERS: >
  An indefinitely stuck batch that looks identical to one still progressing normally will never surface as
  something anyone needs to investigate.
DISCONFIRMING_OBSERVATION: >
  A batch with one movement stuck unresolved for an extended period shows no difference from a batch whose
  movements are all still normally in progress.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Leave one movement in a batch unresolved for an extended period and compare the batch's appearance to one
  still in ordinary progress.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q044

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q044
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Triggering a batch-level carrier action, which commits every movement in the batch at once, requires a
  permission distinct from the permission needed to trigger that same carrier action on one movement
  individually.
WHY_IT_MATTERS: >
  If the same permission covers both, a role intended only for small-scale, single-movement carrier actions
  can commit an entire batch's worth of shipments and cost at once.
DISCONFIRMING_OBSERVATION: >
  A role restricted to single-movement carrier actions is still able to trigger a batch-level carrier
  action affecting many movements at once.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Assign a role limited to single-movement carrier actions and attempt a batch-level carrier action under
  that role.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q045

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q045
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling an entire batch, with the consequences that has for every pending movement inside it, is
  logged as a batch-level action distinct from, and not indistinguishable from, cancelling one movement on
  its own.
WHY_IT_MATTERS: >
  An unlogged or indistinguishable batch-level cancellation makes it impossible to later tell whether many
  movements were cancelled together as one deliberate decision or individually for separate reasons.
DISCONFIRMING_OBSERVATION: >
  Cancelling a batch is recorded identically to cancelling each of its movements one at a time, with
  nothing indicating the cancellations happened together as one batch-level action.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Cancel a batch containing several pending movements and check how that action is recorded relative to
  cancelling one movement individually.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q046

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q046
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user without permission to act on one particular movement inside a batch cannot have that movement
  swept along and acted on anyway purely because a batch-level action was triggered by someone else who
  does have permission for the batch as a whole.
WHY_IT_MATTERS: >
  A batch-level action bypassing an individual movement's own permission boundary lets a broad batch
  permission quietly override a narrower, deliberate restriction on one specific movement.
DISCONFIRMING_OBSERVATION: >
  A movement that an operator individually has no permission to act on is still committed to a carrier
  action as part of a batch-level action that operator triggered.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Restrict a user's permission on one specific movement, include that movement in a batch, and have the
  user trigger the batch-level carrier action.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q047

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q047
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A batch whose movements individually reach the carrier weight or size limit only when considered
  together (none exceeds it alone, but the physical consolidation for carrier handling does) is checked
  against that combined limit rather than only ever checking each movement in isolation.
WHY_IT_MATTERS: >
  Only ever checking each movement alone lets a batch-level consolidation exceed a real carrier limit that
  no single movement ever revealed.
DISCONFIRMING_OBSERVATION: >
  A batch whose movements individually stay under a carrier limit, but whose consolidated handling for the
  batch would exceed it, proceeds with no warning at the batch level.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Construct a batch whose individual movements are each within a carrier limit but whose combined batch
  handling would exceed it, and attempt the batch-level carrier action.
```

## G05-DELIVERY_STOCK_PICKING_BATCH-Q048

```yaml
QID: G05-DELIVERY_STOCK_PICKING_BATCH-Q048
MODULE: delivery_stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A batch's own record retains, after the fact, which movements were included in it at the time its
  carrier action actually ran, even if movements are later added to or removed from the batch, so that the
  batch's own history is not silently rewritten by later membership changes.
WHY_IT_MATTERS: >
  A batch's membership at the moment of action is what the carrier actually acted on; if later membership
  changes rewrite that history, nobody can reconstruct what was truly shipped together.
DISCONFIRMING_OBSERVATION: >
  After movements are added to or removed from a batch following its carrier action, the batch's own
  history no longer shows which movements were actually included at the time that action ran.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Run a batch-level carrier action, then add or remove movements from the batch, and check whether the
  batch's history still shows the original membership at the time of the action.
```

---
## GMVQ Internal QA Checklist

- [x] 48 distinct MVQ records; no padding — every record targets a distinct hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`.
- [x] Questions are behavioral and source-neutral; no vendor/product name, technical identifier, or module
      name appears in question text.
- [x] Bridge Module Rule seam-of-a-seam test applied to every question: each one fails only at the
      batch level; any candidate that would still make sense for one movement handled on its own was cut.
- [x] Batch spanning several carriers or destinations represented (Q001-Q005).
- [x] Cost allocated across the batch and residual handling represented (Q006-Q010).
- [x] One movement failing or being removed after labels were produced for the whole batch represented
      (Q011-Q015).
- [x] Batch partially dispatched represented (Q016-Q019).
- [x] Movement added to a batch after processing began represented (Q020-Q023).
- [x] Two operators working the same batch represented (Q024-Q027).
- [x] Batch cancelled after some of its movements completed represented (Q028-Q031).
- [x] Batch carrier state versus member movement state represented (Q032-Q035).
- [x] Ordering within a batch when sequence matters represented (Q036-Q039).
- [x] Reporting a batch as delivered when only part of it was represented (Q040-Q043).
- [x] Role/permission boundary specific to batch-level carrier actions represented (Q044-Q046).
- [x] Combined-limit negative case and post-hoc membership history integrity represented (Q047-Q048).
- [x] Tenant/company boundary represented (Q005, Q023).
- [x] No specific Thai legal or tax requirement asserted anywhere in this bank.
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
