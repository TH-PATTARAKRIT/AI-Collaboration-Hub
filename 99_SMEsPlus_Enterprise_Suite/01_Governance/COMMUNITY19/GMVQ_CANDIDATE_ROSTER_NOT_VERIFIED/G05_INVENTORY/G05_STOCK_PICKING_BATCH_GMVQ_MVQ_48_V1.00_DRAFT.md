# SMEsPlus ENTERPRISE SUITE
## GMVQ — G05 INVENTORY / stock_picking_batch Module MVQ Bank

**Document ID:** GMVQ-G05-STOCK_PICKING_BATCH-MVQ48-V1.00
**Group:** G05 INVENTORY
**Module Metadata:** `stock_picking_batch`
**Wave:** W2
**Author Cell:** GMVQ PRODUCTION TEAM P04
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This bank supplies the module-specific MVQ set for `stock_picking_batch`, the grouping of several
warehouse operations into one operational unit of work. Per the G05 INVENTORY group brief and the
GMVQ Bridge Module Rule, this bank is scoped to the OPERATIONAL view of a batch: how it behaves as a
unit that can be assigned, started, paused and completed while its members keep their own
independent states, regardless of any carrier or shipping concern. Carrier-facing handling of a
batch is out of scope here and belongs to the sibling bank for the module that layers carrier
handling onto a batch of pickings; this bank does not repeat that ground. Coverage is spread across
business capability, business rule, state transition, configuration dependency, role and
permission, exception path, cancellation, reversal, negative case, cross-module dependency,
optional behaviour, auditability, tenant/company boundary, concurrency and ordering, runtime
reachability, configuration reachability, and source/runtime contradiction potential. This bank
supplements the 55-question Standard bank; combined research depth for this module is
55 + 48 = 103.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses; none
  was trimmed or stretched to hit the count.
- Every question passes the bridge-module seam test: if batching were removed and each member
  operation were worked on its own, the question would no longer make sense. A question that would
  still make sense without batching belongs to the base module or another bank, not here, and was
  cut during authoring rather than included.
- Question text is source-neutral: no vendor or product name, no technical identifier (table,
  field, method, XML ID, API path), and the module's own metadata name never appears outside the
  `MODULE:` field — the generic term "batch" or "member operation" stands in for it throughout.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G05-STOCK_PICKING_BATCH-Q001

```yaml
QID: G05-STOCK_PICKING_BATCH-Q001
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A batch's overall status reports complete only once every member operation it contains has itself reached a terminal state; it cannot report complete while any member is still open.
WHY_IT_MATTERS: >
  If the batch-level status is trusted as a proxy for real completion, a false 'complete' hides unfinished work that nobody then goes back to finish.
DISCONFIRMING_OBSERVATION: >
  A batch shows a complete status while at least one of its member operations remains open or unprocessed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a batch with several members, complete all but one, and read the batch's own status field.
```

## G05-STOCK_PICKING_BATCH-Q002

```yaml
QID: G05-STOCK_PICKING_BATCH-Q002
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Removing a member operation from an in-progress batch does not itself change that operation's own state or release or alter its stock reservation; removal only detaches it from the group.
WHY_IT_MATTERS: >
  If detaching from a batch silently mutates the member's own state or reservation, an operator who only meant to regroup work has unintentionally changed what stock is committed to what demand.
DISCONFIRMING_OBSERVATION: >
  A member's state or its stock reservation changes at the moment it is removed from a batch, with no other action taken on the member itself.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Add a member with an active reservation to a batch, remove it from the batch without touching it otherwise, and compare its state and reservation before and after.
```

## G05-STOCK_PICKING_BATCH-Q003

```yaml
QID: G05-STOCK_PICKING_BATCH-Q003
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A member operation added to a batch after the batch was created keeps its own original creation and scheduling timestamps; joining a batch does not backdate or overwrite them to match the batch.
WHY_IT_MATTERS: >
  Backdated timestamps on a newly joined member would misrepresent when that work actually became known, corrupting lead-time and on-time analysis.
DISCONFIRMING_OBSERVATION: >
  A member's own creation or scheduled date changes to match the batch's dates purely as a side effect of being added to it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a batch on one date, then add a member operation created on a different date, and compare the member's own dates before and after joining.
```

## G05-STOCK_PICKING_BATCH-Q004

```yaml
QID: G05-STOCK_PICKING_BATCH-Q004
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A batch's own progress summary can never show a completion fraction that cannot be reconciled by independently counting how many of its members are actually in a done state.
WHY_IT_MATTERS: >
  An unreconcilable progress figure lets a batch look further along than it is, which delays someone noticing that a specific member is stuck.
DISCONFIRMING_OBSERVATION: >
  The batch's displayed completion fraction or count does not match a manual count of members in a done state, with no formula difference that explains the gap.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Bring a batch with a known number of members to a known number of completions, and compare the displayed progress figure against a manual tally.
```

## G05-STOCK_PICKING_BATCH-Q005

```yaml
QID: G05-STOCK_PICKING_BATCH-Q005
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Validating an entire batch at once enforces every business rule check that would apply to validating each of its members individually; no check is skipped because it was done as part of a bulk action.
WHY_IT_MATTERS: >
  A bulk shortcut that skips a per-item check would let stock move in ways that would have been blocked if attempted one at a time, defeating the purpose of the check entirely.
DISCONFIRMING_OBSERVATION: >
  A member carrying a condition that would block it from being validated on its own is validated successfully anyway when it rides inside a batch-wide validation.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct one member operation that on its own would fail a validation check, place it inside a batch with otherwise-valid members, and validate the batch as a whole.
```

## G05-STOCK_PICKING_BATCH-Q006

```yaml
QID: G05-STOCK_PICKING_BATCH-Q006
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Stock reserved for a batch's members is tracked in a way that never allows the same physical quantity to be counted as reserved for more than one member of that batch at once.
WHY_IT_MATTERS: >
  A shared reservation pool that can be double-claimed inside one batch would let two members believe they each hold stock that only exists once, discovered only when one of them tries to actually take it.
DISCONFIRMING_OBSERVATION: >
  Two different members of the same batch each show the same units of the same item as reserved to them at the same time.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a batch whose members compete for the same limited-quantity item, reserve stock for the batch, and inspect what each member's reservation actually points to.
```

## G05-STOCK_PICKING_BATCH-Q007

```yaml
QID: G05-STOCK_PICKING_BATCH-Q007
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When stock available to a batch is insufficient to satisfy every member, which member ends up short follows a consistent, defined allocation rule rather than depending on the arbitrary order an operator happened to work through them.
WHY_IT_MATTERS: >
  An outcome that depends on click order rather than a business rule is not repeatable, not explainable to a customer whose order came up short, and not something anyone can be held accountable for.
DISCONFIRMING_OBSERVATION: >
  Running the same batch, with the same starting stock and the same members, but processed in a different order, leaves a different member short of stock.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a batch with two members competing for a quantity that cannot satisfy both, and process the members in one order, then repeat with the same starting stock in reverse order.
```

## G05-STOCK_PICKING_BATCH-Q008

```yaml
QID: G05-STOCK_PICKING_BATCH-Q008
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two operators working different members of the same batch at the same time do not lose each other's progress; one operator's recorded completion of a member is never silently overwritten by the other operator's unrelated update to the batch.
WHY_IT_MATTERS: >
  A lost update on a warehouse floor with two people working the same batch means physical work that was actually done disappears from the record, and someone re-does it or ships short.
DISCONFIRMING_OBSERVATION: >
  One operator's completion of a member operation is reverted or disappears after a second operator, working a different member of the same batch, saves their own progress.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have two sessions open the same batch, complete different members concurrently, and verify both completions persist.
```

## G05-STOCK_PICKING_BATCH-Q009

```yaml
QID: G05-STOCK_PICKING_BATCH-Q009
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A member operation cannot be cancelled after the batch containing it has already been fully validated without an explicit action that also updates what the batch itself reports as done.
WHY_IT_MATTERS: >
  A cancellation that happens quietly behind an already-closed batch leaves the batch's own completion record overstating what actually still stands.
DISCONFIRMING_OBSERVATION: >
  A member inside an already-validated batch is cancelled, and the batch's own completion or summary record shows no trace of that cancellation having happened.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Validate a batch fully, then attempt to cancel one of its now-complete members, and check whether the batch's own record reflects the cancellation.
```

## G05-STOCK_PICKING_BATCH-Q010

```yaml
QID: G05-STOCK_PICKING_BATCH-Q010
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The audit trail for an action taken on a specific member operation inside a batch records the individual operator who actually performed it, not only the batch as an undifferentiated actor.
WHY_IT_MATTERS: >
  If every member action is logged only as 'the batch', nobody can later answer who actually picked, packed, or moved a specific item when it matters for a discrepancy or a claim.
DISCONFIRMING_OBSERVATION: >
  The log entry for an action on a specific member shows the batch as the actor, or no actor at all, with the individual operator who performed it not recoverable from the record.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Have a named operator complete one member inside a batch, and inspect the audit or log entry created for that specific action.
```

## G05-STOCK_PICKING_BATCH-Q011

```yaml
QID: G05-STOCK_PICKING_BATCH-Q011
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A batch's members are constrained to operations that could each independently execute inside the same operational and legal-company boundary; grouping them does not create a movement across a boundary that a single one of those operations would not otherwise be permitted to cross.
WHY_IT_MATTERS: >
  If batching quietly bypasses a boundary that individual operations respect, stock or obligations cross a legal or operational line with no one having explicitly authorized that crossing.
DISCONFIRMING_OBSERVATION: >
  A batch is built successfully from members that individually belong to different companies or operational boundaries, and no warning, restriction, or explicit handling of that mixture is presented.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Attempt to add a member belonging to a different company or operational unit than the batch's other members, and observe whether it is accepted, blocked, or flagged.
```

## G05-STOCK_PICKING_BATCH-Q012

```yaml
QID: G05-STOCK_PICKING_BATCH-Q012
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A batch that groups members already spanning more than one warehouse presents its own location or origin information honestly as spanning multiple locations, rather than displaying a single warehouse header that misrepresents where all the work actually sits.
WHY_IT_MATTERS: >
  An operator trusting a single displayed location for a batch that actually spans several would look in the wrong place, or assume coverage that is not real.
DISCONFIRMING_OBSERVATION: >
  A batch containing members from more than one warehouse displays a single warehouse as though it were the location for the whole batch.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Build a batch from members located in two different warehouses and inspect what location information the batch itself presents.
```

## G05-STOCK_PICKING_BATCH-Q013

```yaml
QID: G05-STOCK_PICKING_BATCH-Q013
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A batch left open with unstarted or paused members continues to hold their stock reservations only for as long as those reservations would independently be valid; the system provides a way to see, and does not indefinitely hide, reservations that a long-idle batch is still holding against other demand.
WHY_IT_MATTERS: >
  Stock quietly locked up by a batch nobody is working degrades service to every other order competing for the same item, and is invisible unless the batch itself is surfaced as the reason.
DISCONFIRMING_OBSERVATION: >
  A batch sits untouched well past any normal working window while its members' reservations remain in place, and nothing in the system surfaces that this batch is the reason a given quantity is unavailable elsewhere.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Create a batch, reserve stock for its members, leave it untouched, and check whether the held reservation and its cause are visible to someone investigating why stock is unavailable.
```

## G05-STOCK_PICKING_BATCH-Q014

```yaml
QID: G05-STOCK_PICKING_BATCH-Q014
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Assigning an operator to a batch as a whole does not silently overwrite an operator already explicitly assigned to one of its individual members; the two assignments are reconciled by a defined rule rather than one quietly erasing the other.
WHY_IT_MATTERS: >
  An operator who was deliberately assigned to a specific member for a reason (skill, certification, location) should not lose that assignment just because someone assigned the batch to a different person.
DISCONFIRMING_OBSERVATION: >
  A member's individually assigned operator is silently replaced with no record of the change, purely because the containing batch was assigned to someone else.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Assign a specific operator to one member of a batch, then assign a different operator to the batch as a whole, and check what the member's assignment becomes.
```

## G05-STOCK_PICKING_BATCH-Q015

```yaml
QID: G05-STOCK_PICKING_BATCH-Q015
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Pausing a batch is enforced against its members, not merely a cosmetic label; an attempt to complete a member while its batch is in a paused state is blocked or explicitly flagged as an exception rather than silently succeeding.
WHY_IT_MATTERS: >
  A pause that only changes a displayed word but does not stop work gives a false sense of control during whatever event caused the pause in the first place.
DISCONFIRMING_OBSERVATION: >
  A member operation inside a batch that has been paused is completed normally, with nothing in the system noting that this happened while the batch was supposed to be paused.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Pause a batch that has at least one member still open, then attempt to complete that member, and observe whether the pause has any enforced effect.
```

## G05-STOCK_PICKING_BATCH-Q016

```yaml
QID: G05-STOCK_PICKING_BATCH-Q016
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Starting a batch does not require every one of its members to already be fully reservable; a batch can be started with the understanding that some members may not yet be fulfillable, and that condition is visibly distinguished from a member that is genuinely ready.
WHY_IT_MATTERS: >
  If starting a batch implies every member is ready, an operator sent out to execute it will discover the gap physically instead of being told about it up front.
DISCONFIRMING_OBSERVATION: >
  A batch is presented as started with no indication that one of its members cannot actually be fulfilled from currently available stock.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a batch containing one member for an item with insufficient available stock, start the batch, and check what the member shows about its own fulfillability.
```

## G05-STOCK_PICKING_BATCH-Q017

```yaml
QID: G05-STOCK_PICKING_BATCH-Q017
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Deleting or discarding a batch does not discard or auto-cancel member operations that are still open; those operations survive as independent work outside the batch.
WHY_IT_MATTERS: >
  A batch is an organizational grouping, not the work itself; destroying the grouping should never destroy the underlying obligation to move the stock.
DISCONFIRMING_OBSERVATION: >
  Deleting a batch that still has open members causes those members' own records to disappear or be cancelled as a side effect.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a batch with at least one still-open member, delete or discard the batch, and check whether the member operation still exists in its own right.
```

## G05-STOCK_PICKING_BATCH-Q018

```yaml
QID: G05-STOCK_PICKING_BATCH-Q018
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reordering the sequence of members within a batch after some members have already been completed does not retroactively alter the recorded order in which those already-completed members were actually done.
WHY_IT_MATTERS: >
  If resequencing can rewrite history, any later analysis of what stock was allocated to whom, in what order, becomes unreliable exactly where it matters — under a stock shortage.
DISCONFIRMING_OBSERVATION: >
  Changing the display or working order of a batch's remaining members alters the recorded sequence number or timestamp of members that were already completed before the reordering happened.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete the first two members of a multi-member batch in order, then reorder the remaining members, and check whether the already-completed members' recorded sequence changed.
```

## G05-STOCK_PICKING_BATCH-Q019

```yaml
QID: G05-STOCK_PICKING_BATCH-Q019
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A batch created by an automatic, unattended grouping pass records enough about why those particular operations were grouped together that its membership is not indistinguishable from a batch an operator built by hand.
WHY_IT_MATTERS: >
  If an automatically formed batch looks identical to a manual one, nobody can later explain, question, or adjust the grouping logic that produced it when it produces an odd combination.
DISCONFIRMING_OBSERVATION: >
  A batch produced by an automatic grouping process carries no indication of having been formed automatically or of what criteria drove that grouping, and is presented exactly as a manually built one would be.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Trigger whatever automatic batch-grouping capability exists, then inspect the resulting batch's record for any trace of its automatic origin or grouping criteria.
```

## G05-STOCK_PICKING_BATCH-Q020

```yaml
QID: G05-STOCK_PICKING_BATCH-Q020
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An operator who is not the batch's assigned actor is either prevented from marking one of its member operations complete, or that action is visibly and explicitly recorded as an exception to normal assignment.
WHY_IT_MATTERS: >
  Without this, batch assignment is decorative: anyone can act on anyone else's assigned work with no trace that the assignment was bypassed.
DISCONFIRMING_OBSERVATION: >
  An operator with no assignment to a batch completes one of its members with no exception, warning, or distinguishing record of the mismatch between assignee and actor.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Assign a batch to one operator, then have a different, unassigned operator attempt to complete one of its members.
```

## G05-STOCK_PICKING_BATCH-Q021

```yaml
QID: G05-STOCK_PICKING_BATCH-Q021
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reserving stock for a batch's members does not give that reservation a standing priority claim that continues to starve a newly created, more urgent demand for the same item after the batch's own need could reasonably be re-evaluated.
WHY_IT_MATTERS: >
  A batch quietly outranking every new urgent order for the same scarce item, indefinitely, turns an organizational convenience into a de facto allocation policy nobody chose.
DISCONFIRMING_OBSERVATION: >
  A newly created, higher-priority demand for an item is unable to obtain stock that is sitting reserved inside an old, idle batch, with no mechanism to surface or reconsider that conflict.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve a scarce item inside an idle batch, then create a new higher-priority demand for the same item, and observe whether the conflict is surfaced.
```

## G05-STOCK_PICKING_BATCH-Q022

```yaml
QID: G05-STOCK_PICKING_BATCH-Q022
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A batch's own count of completed-versus-total members stays correct even when two members are completed by two different operators at effectively the same moment; no race between simultaneous completions produces a count that over- or under-states how many members are actually done.
WHY_IT_MATTERS: >
  A miscounted progress figure under exactly the concurrent conditions a real warehouse floor produces would fail precisely when it is most needed.
DISCONFIRMING_OBSERVATION: >
  Completing two members of the same batch at the same moment from two different sessions results in a progress count that does not equal the true number of completed members.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Trigger near-simultaneous completion of two different members of the same batch from two separate sessions, then check the batch's own completed-count.
```

## G05-STOCK_PICKING_BATCH-Q023

```yaml
QID: G05-STOCK_PICKING_BATCH-Q023
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A member added to a batch after a batch-wide validation action has already run is not silently treated as though it had already been included in that earlier action; it requires its own explicit handling.
WHY_IT_MATTERS: >
  If a late-added member is invisibly swept into an action that happened before it existed, either it gets falsely marked done or the batch's completion record becomes internally inconsistent about what the validation actually covered.
DISCONFIRMING_OBSERVATION: >
  A member added after a batch-wide validation shows as already validated, or the batch's record implies the earlier validation covered a member that did not yet exist at that time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Validate a batch, then add a new member to it afterward, and check the new member's own status and how the batch describes what its prior validation covered.
```

## G05-STOCK_PICKING_BATCH-Q024

```yaml
QID: G05-STOCK_PICKING_BATCH-Q024
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Any total quantity a batch displays or acts on at the batch level always equals the current sum of its members' own quantities; it is never a cached figure that can drift out of step after a member's quantity changes.
WHY_IT_MATTERS: >
  A stale rolled-up total gives false confidence that a batch-level figure used for planning or billing still matches what will actually move.
DISCONFIRMING_OBSERVATION: >
  A batch-level total quantity does not match the sum of its current members' quantities after one member's quantity was changed following the batch's creation.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a batch, note its displayed total quantity, change one member's quantity, and recheck the batch-level total against a manual sum.
```

## G05-STOCK_PICKING_BATCH-Q025

```yaml
QID: G05-STOCK_PICKING_BATCH-Q025
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling a batch that already has some members completed does not implicitly touch those already-completed members; the cancellation's scope and what it leaves standing is stated explicitly rather than left to be inferred.
WHY_IT_MATTERS: >
  An operator relying on 'the batch was cancelled' to mean nothing happened would be wrong and could fail to notice stock already moved under the completed members.
DISCONFIRMING_OBSERVATION: >
  Cancelling a batch with some members already completed leaves no clear statement of which members were affected and which were left standing as already done.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete some members of a batch, leave others open, cancel the batch, and inspect what the resulting record says happened to each member.
```

## G05-STOCK_PICKING_BATCH-Q026

```yaml
QID: G05-STOCK_PICKING_BATCH-Q026
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a batch-wide validation encounters one member that fails a check, the outcome (whether the whole batch stops, or the valid members commit while the failing one is called out) is a defined, consistent behavior rather than one that varies unpredictably by circumstance.
WHY_IT_MATTERS: >
  An operator needs to know, every time, whether a single bad line blocks everyone else's already-good work or lets it through, so they can plan around it rather than discover it by accident.
DISCONFIRMING_OBSERVATION: >
  Running the same batch-wide validation scenario twice, with one member set up to fail the same way both times, produces a different outcome for the passing members between the two runs.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct a batch with one member set to fail a validation check and the rest valid, run the batch-wide validation, then repeat with an equivalent setup and compare outcomes.
```

## G05-STOCK_PICKING_BATCH-Q027

```yaml
QID: G05-STOCK_PICKING_BATCH-Q027
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A batch that ends up with zero members after all of them were removed is not reported as complete purely because there is nothing left to be incomplete about; an empty batch is distinguished from a genuinely finished one.
WHY_IT_MATTERS: >
  A vacuously 'complete' empty batch would let a batch that never actually did anything look, in every report, identical to one that fulfilled real demand.
DISCONFIRMING_OBSERVATION: >
  A batch whose every member was removed reports the same completion status as a batch that actually finished all of its original members.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a batch with members, remove every member one by one, and check the batch's resulting status against a genuinely fully-completed batch.
```

## G05-STOCK_PICKING_BATCH-Q028

```yaml
QID: G05-STOCK_PICKING_BATCH-Q028
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Completing a member operation while it is part of a batch produces the same downstream effects that completing that same operation on its own, outside any batch, would produce; no step that would normally follow completion is skipped because the action arrived through a batch.
WHY_IT_MATTERS: >
  A batch-specific shortcut that skips a downstream step would make batching a way to accidentally bypass processing that every other completion path enforces.
DISCONFIRMING_OBSERVATION: >
  Completing a member inside a batch fails to trigger a downstream effect that completing the same kind of operation individually would have triggered.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Complete a member operation once individually and once as part of a batch, with otherwise equivalent setups, and compare the downstream effects each produces.
```

## G05-STOCK_PICKING_BATCH-Q029

```yaml
QID: G05-STOCK_PICKING_BATCH-Q029
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Grouping operations into a batch is optional at the level of an individual operation: an operation of the same kind can still be worked entirely on its own, one at a time, with an identical final outcome to working it inside a batch.
WHY_IT_MATTERS: >
  If batching secretly changes what an operation does rather than only how it is organized, the two paths stop being interchangeable and users lose a genuinely free choice.
DISCONFIRMING_OBSERVATION: >
  An operation worked individually, outside any batch, produces a different final state than an equivalent operation worked to completion inside a batch.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Take two equivalent operations, complete one on its own and the other inside a batch, and compare their final states.
```

## G05-STOCK_PICKING_BATCH-Q030

```yaml
QID: G05-STOCK_PICKING_BATCH-Q030
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Detaching the last remaining member from a batch, leaving it empty, is either consistently prevented or consistently allowed; the two ways of reaching an empty batch (removing the last member one at a time versus some other path) do not disagree about whether an empty batch is a valid state.
WHY_IT_MATTERS: >
  An inconsistency here means the system's own rules contradict themselves about what a valid batch looks like, which shows up as an unrepeatable, confusing error somewhere else.
DISCONFIRMING_OBSERVATION: >
  One path to an empty batch is blocked while a different path reaches the same empty state without being blocked.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to remove the last member of a batch directly, and separately attempt to reach an empty batch by a different available action, and compare whether each is permitted.
```

## G05-STOCK_PICKING_BATCH-Q031

```yaml
QID: G05-STOCK_PICKING_BATCH-Q031
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The same batching and completion-tracking rules that apply to a batch of outbound movements apply symmetrically to a batch built from inbound movements; the direction of the underlying movement does not change whether the batch honestly reports partial completion.
WHY_IT_MATTERS: >
  If the completion invariant only really holds for one direction of movement, work built assuming symmetric behavior will surface a defect only when someone happens to batch the other direction.
DISCONFIRMING_OBSERVATION: >
  A batch of inbound movements reports overall progress or completion in a way that a batch of outbound movements, in an otherwise equivalent state, would not.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Build one batch of outbound movements and one batch of inbound movements in equivalent partial-completion states, and compare what each reports.
```

## G05-STOCK_PICKING_BATCH-Q032

```yaml
QID: G05-STOCK_PICKING_BATCH-Q032
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a member's own scheduled date differs from the batch's overall scheduled date, which one governs whether the batch is presented as due or late is a defined, stated rule rather than an arbitrary pick between the two.
WHY_IT_MATTERS: >
  An operator deciding what to work on next needs to know reliably whether 'late' means the batch's date or an individual member's date, or a wrong priority call gets made.
DISCONFIRMING_OBSERVATION: >
  Two otherwise-identical batches, differing only in whether a member's own date or the batch's date is earlier, are shown with due/late status that cannot be explained by a single consistent rule.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create two batches whose member dates and batch dates differ in opposite directions, and compare how each is flagged as due or late.
```

## G05-STOCK_PICKING_BATCH-Q033

```yaml
QID: G05-STOCK_PICKING_BATCH-Q033
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A batch-wide instruction and a conflicting instruction attached to one specific member are both surfaced to the operator working that member, rather than one silently masking the other.
WHY_IT_MATTERS: >
  An operator who never sees the member-specific instruction because the batch-wide one displaced it may follow guidance that does not apply to the specific item in hand.
DISCONFIRMING_OBSERVATION: >
  An operator working a specific member only ever sees the batch-wide instruction, with no way to see or ever be told about a conflicting instruction attached to that individual member.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attach a batch-wide instruction and a differing member-specific instruction to the same batch, then check what an operator working that member is shown.
```

## G05-STOCK_PICKING_BATCH-Q034

```yaml
QID: G05-STOCK_PICKING_BATCH-Q034
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An operation that belongs to more than one batch at once is possible only if completing it in one batch is correctly reflected as done everywhere it appears, so no other batch continues to present that same completed operation as still outstanding.
WHY_IT_MATTERS: >
  An operation left showing as outstanding in a second batch after it was actually finished through the first would send an operator to redo work that is already done, or worse, to redo a physical movement that already happened.
DISCONFIRMING_OBSERVATION: >
  An operation completed through one batch still appears as an open, actionable member in a different batch that also references it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  If the same operation can be referenced by more than one batch, add it to two batches, complete it through one, and check its status in the other.
```

## G05-STOCK_PICKING_BATCH-Q035

```yaml
QID: G05-STOCK_PICKING_BATCH-Q035
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a batch's membership can be recalculated automatically after its initial creation, each such recalculation leaves a trace of what was added or removed, so the batch's composition at any past moment can be reconstructed rather than only ever known as whatever it currently is.
WHY_IT_MATTERS: >
  An audit or investigation into a discrepancy needs to know what a batch actually contained at the time in question, not only what it contains now if the membership has since changed.
DISCONFIRMING_OBSERVATION: >
  A batch's membership changes as a result of an automatic recalculation, and no record exists afterward of what the membership was immediately before that change.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Trigger an automatic recalculation of an existing batch's membership and check whether the prior membership state remains retrievable afterward.
```

## G05-STOCK_PICKING_BATCH-Q036

```yaml
QID: G05-STOCK_PICKING_BATCH-Q036
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a batch records a single completion timestamp for the whole batch, that figure does not stand in for or obscure the actual, individually staggered completion times of each member wherever those individual times matter (for example, in a dispute over when a specific item actually moved).
WHY_IT_MATTERS: >
  Collapsing several real, distinct completion moments into one timestamp erases information that may be exactly what is needed to resolve a later question about timing.
DISCONFIRMING_OBSERVATION: >
  The actual completion time recorded for an individual member cannot be recovered because only a single batch-level completion timestamp exists anywhere in the record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a batch's members at clearly different, spaced-out times, then check whether each member's own completion time is separately recoverable.
```

## G05-STOCK_PICKING_BATCH-Q037

```yaml
QID: G05-STOCK_PICKING_BATCH-Q037
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  If a technical or business limit exists on how many member operations a single batch may hold, attempting to exceed it produces a clear, explicit rejection rather than a silent truncation that drops members without saying so.
WHY_IT_MATTERS: >
  A silent drop at a size limit means someone believes a large batch fully captured a set of work when a portion of it quietly never made it in.
DISCONFIRMING_OBSERVATION: >
  Adding members past whatever limit exists results in fewer members present in the batch than were actually added, with no message explaining that some were rejected.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to add members to a batch well past any plausible size limit and compare the number added against the number attempted.
```

## G05-STOCK_PICKING_BATCH-Q038

```yaml
QID: G05-STOCK_PICKING_BATCH-Q038
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If batch functionality itself is gated by a setting at the operational-unit level, a batch that already exists remains viewable and completable after that setting is later turned off, rather than becoming stranded or inaccessible.
WHY_IT_MATTERS: >
  Turning off a feature for future use should not orphan work that is already committed and physically in progress under the old setting.
DISCONFIRMING_OBSERVATION: >
  Disabling the batching setting after a batch already exists makes that existing batch inaccessible, uncompleteable, or causes its members to lose their grouping without an explicit resolution.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a batch while the batching capability is enabled, then disable that capability at the operational-unit level, and check whether the existing batch remains usable.
```

## G05-STOCK_PICKING_BATCH-Q039

```yaml
QID: G05-STOCK_PICKING_BATCH-Q039
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A batch's displayed 'ready to start' or similar readiness signal reflects the true, current reservability of its members at the moment it is shown, rather than a cached signal that can go stale between when it was computed and when an operator actually acts on it.
WHY_IT_MATTERS: >
  An operator trusting a stale green light walks to the floor expecting stock that has since been claimed by something else, wasting the trip and delaying the real fix.
DISCONFIRMING_OBSERVATION: >
  A batch continues to display a ready state after the underlying stock that made it ready has since been consumed or reserved elsewhere, with the display not refreshed to reflect that.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Bring a batch to a displayed ready state, then consume or reserve the underlying stock through an unrelated action, and check whether the batch's readiness display updates.
```

## G05-STOCK_PICKING_BATCH-Q040

```yaml
QID: G05-STOCK_PICKING_BATCH-Q040
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reassigning a batch to a different operator mid-progress does not retroactively re-attribute work already recorded as done by the original operator; history stays attributed to whoever actually performed it at the time.
WHY_IT_MATTERS: >
  Rewriting who did what after the fact, just because a batch changed hands, corrupts the very accountability record the audit trail exists to preserve.
DISCONFIRMING_OBSERVATION: >
  Work already completed and attributed to the original operator shows as attributed to the new operator after the batch is reassigned.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Have one operator complete some members of a batch, reassign the batch to a second operator, and check the attribution recorded for the already-completed work.
```

## G05-STOCK_PICKING_BATCH-Q041

```yaml
QID: G05-STOCK_PICKING_BATCH-Q041
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the demand behind a specific member is cancelled elsewhere while that member still sits inside an in-progress batch, the member is either removed or clearly flagged as no longer actionable, rather than continuing to present as ordinary open work leading nowhere.
WHY_IT_MATTERS: >
  An operator who picks and moves stock for a member whose underlying demand was already cancelled elsewhere has wasted the movement and possibly created stock sitting in the wrong place with no order to justify it.
DISCONFIRMING_OBSERVATION: >
  A member whose originating demand was cancelled elsewhere continues to display as ordinary, unflagged open work inside its batch.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Cancel the source demand behind one member of an in-progress batch through an unrelated path, then check how that member is presented inside the batch afterward.
```

## G05-STOCK_PICKING_BATCH-Q042

```yaml
QID: G05-STOCK_PICKING_BATCH-Q042
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If batches can be formed automatically, two concurrent automatic grouping runs cannot both claim the same eligible operation into two different batches at once.
WHY_IT_MATTERS: >
  An operation claimed by two batches at once means two different pieces of work each believe they own the same physical movement, and completing one leaves the other's record wrong.
DISCONFIRMING_OBSERVATION: >
  The same eligible operation ends up present as a member in two different batches formed by concurrent automatic grouping.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Trigger two concurrent automatic batch-grouping runs against an overlapping pool of eligible operations and check whether any operation lands in more than one resulting batch.
```

## G05-STOCK_PICKING_BATCH-Q043

```yaml
QID: G05-STOCK_PICKING_BATCH-Q043
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether manually resequencing a batch's members changes the order operators are actually required to work them, versus merely changing a suggested display order, is a stated distinction rather than one the operator has to guess at.
WHY_IT_MATTERS: >
  An operator who assumes reordering is a hard sequence, when it is really just a suggestion, may wait unnecessarily; one who assumes the reverse may act out of an order that was meant to matter for stock allocation.
DISCONFIRMING_OBSERVATION: >
  Operators working the same resequenced batch reach different, equally accepted conclusions about whether the new order is enforced, because nothing in the batch states which it is.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Resequence a batch's members and attempt to complete them out of the new order, checking whether the system enforces, warns, or silently allows it.
```

## G05-STOCK_PICKING_BATCH-Q044

```yaml
QID: G05-STOCK_PICKING_BATCH-Q044
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A member operation that is itself partially fulfilled, neither fully open nor fully done, is counted toward a batch's progress consistently everywhere that progress is shown, not as 'done' in one place and 'not done' in another.
WHY_IT_MATTERS: >
  A partial state that is counted inconsistently across different views of the same batch would let two people looking at the same batch honestly disagree about how far along it is.
DISCONFIRMING_OBSERVATION: >
  A batch's member in a partially-fulfilled state is counted as complete in one place the batch's progress is shown, and as incomplete in another place the same progress is shown.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Bring one member of a batch to a partially-fulfilled state and compare how that member is counted across every place the batch's progress or summary is displayed.
```

## G05-STOCK_PICKING_BATCH-Q045

```yaml
QID: G05-STOCK_PICKING_BATCH-Q045
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a batch that has already reached a terminal done state can still be reopened to add or change a member, the record afterward honestly shows that the batch was reopened, rather than presenting a single, unbroken original completion.
WHY_IT_MATTERS: >
  A reopened batch that looks exactly like one that was never touched again would mislead anyone relying on 'completed on this date' as the final word.
DISCONFIRMING_OBSERVATION: >
  A batch that was reopened after reaching a done state, and modified, shows no trace afterward of having ever been reopened.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Bring a batch to a fully done state, reopen it if that is possible, add or change a member, and check whether the resulting record discloses the reopening.
```

## G05-STOCK_PICKING_BATCH-Q046

```yaml
QID: G05-STOCK_PICKING_BATCH-Q046
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A batch that groups member operations of genuinely different underlying operation types (for example, an ordinary outbound movement alongside a return or a correction) still applies the same completion and status rules uniformly across every member, rather than one member type quietly being exempt from the rule that governs the others.
WHY_IT_MATTERS: >
  A completion rule that silently treats one operation type differently inside a mixed batch produces a status that means something different depending on which kind of member you happen to be looking at.
DISCONFIRMING_OBSERVATION: >
  A batch containing a mix of operation types reports its overall completion in a way that ignores, or treats inconsistently, the state of members of one particular operation type.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Build a batch that mixes an ordinary movement member with a return or correction member, bring one to completion and leave the other open, and check what the batch reports.
```

## G05-STOCK_PICKING_BATCH-Q047

```yaml
QID: G05-STOCK_PICKING_BATCH-Q047
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a batch is credited to an operator for performance or workload purposes, that credit reflects who actually performed the work on each member, not solely whoever happened to start, validate, or close the batch as a whole.
WHY_IT_MATTERS: >
  Crediting only the person who closed the batch, when several operators actually did the physical work, produces a workload or performance record that does not match what really happened on the floor.
DISCONFIRMING_OBSERVATION: >
  A batch worked by more than one operator attributes its full workload or performance credit to a single operator, with the other contributors' actual work not reflected anywhere.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Have two different operators each complete different members of the same batch, then check how workload or performance credit for that batch is attributed.
```

## G05-STOCK_PICKING_BATCH-Q048

```yaml
QID: G05-STOCK_PICKING_BATCH-Q048
MODULE: stock_picking_batch
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A permission or role check applied to validating a batch as a whole is at least as strict as the check that would apply to validating each of its members individually; grouping members into a batch does not create a lower-privilege path to an action a member's own rules would otherwise require a higher privilege for.
WHY_IT_MATTERS: >
  A bulk action with a weaker permission check than its individual equivalent is a privilege-escalation path: a user without authority for one member gains it simply by wrapping the action in a batch.
DISCONFIRMING_OBSERVATION: >
  A user lacking the permission required to validate a specific member individually is able to validate it successfully by including it in a batch-wide validation instead.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Identify a member whose individual validation requires a specific permission, assign it to a user lacking that permission, and have that user attempt a batch-wide validation that includes it.
```
