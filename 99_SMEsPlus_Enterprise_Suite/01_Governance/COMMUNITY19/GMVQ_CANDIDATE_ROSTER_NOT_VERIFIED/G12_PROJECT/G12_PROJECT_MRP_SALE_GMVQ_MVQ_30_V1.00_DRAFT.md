# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_mrp_sale Module Bridge MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_MRP_SALE-MVQ30-V1.00
**Group:** G12 PROJECT
**Module Metadata:** `project_mrp_sale`
**Wave:** GMVQ 25-Team Acceleration (2026-09-27)
**Author Cell:** P12-3 (GMVQ Question Factory — Production Cell P12-3)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 30
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 30 = 85
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `project_mrp_sale`, the three-participant seam
where a project's own task and milestone tracking is the visible layer that must correctly reconcile
a customer order's commitments (quantity, delivery date, cancellation, customer visibility) with a
production order's own progress (schedule, yield, quality, priority). Per the GMVQ Bridge Module Rule
V1.00, every question here fails only where the order, the project's task/milestone view, AND
manufacturing progress all three have to be present at once.

Mandatory pre-authoring sibling check performed per GMVQ_BRIDGE_MODULE_RULE_V1.00 §5:
`grep -h 'HYPOTHESIS'` was run against `G08_SALES/G08_SALE_MRP_GMVQ_MVQ_48_V1.00_DRAFT.md` and
`G08_SALES/G08_SALE_PROJECT_GMVQ_MVQ_48_V1.00_DRAFT.md` in full before authoring. No question below
restates a pure `sale_mrp` hypothesis (order-versus-production behaviour with no project task in the
picture — delivery-date derivation, quantity change authority, cancellation-with-WIP handling, yield
shortfall and allocation, quality-failure counting) or a pure `sale_project` hypothesis (order-versus-
project behaviour with no manufacturing in the picture — project creation, budget derivation,
ownership, closure ordering, portal visibility of project detail). Where `sale_mrp` already asks the
general order-versus-production question, this bank asks the narrower question of whether the
project's own task or milestone view correctly and visibly carries that same fact, rather than
disagreeing with it or hiding it — a question that does not make sense at all where no project task
sits between the order and the production run.

## Control

**Arity owned: THREE-PARTICIPANT (customer order + project task/milestone view + manufacturing
progress) only.** A question answerable by order+manufacturing alone with no project task in the
picture, or by order+project alone with no manufacturing progress in the picture, does not belong
here.

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: these 30 questions test 30 distinct material seam hypotheses. An honest exhaustion
  statement follows the questions rather than stretched wording used to reach 48.
- Question text is source-neutral: no vendor or product name, no technical identifier, and the
  module's own metadata name never appears outside the `MODULE:` field.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## G12-PROJECT_MRP_SALE-Q001

```yaml
QID: G12-PROJECT_MRP_SALE-Q001
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A project milestone tied to a production order's completion is not marked complete while the production order it depends on still shows unfinished progress.
WHY_IT_MATTERS: >
  Marking the milestone complete ahead of the actual production would let a dependent customer-facing commitment, such as an invoice trigger, fire before the work is really done.
DISCONFIRMING_OBSERVATION: >
  A project milestone tied to production completion shows as complete while its underlying production order still reports unfinished progress.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Link a project milestone to a production order's completion, advance the production order only partway, and check whether the milestone shows complete.
```

## G12-PROJECT_MRP_SALE-Q002

```yaml
QID: G12-PROJECT_MRP_SALE-Q002
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Increasing an order's quantity after its linked production has already started results in the project task's own scope or budget structure being visibly extended to cover the added quantity, rather than the task's scope silently staying at its original definition.
WHY_IT_MATTERS: >
  A task whose scope silently understates the order would leave whoever manages the project unaware that more work is now committed than the task shows.
DISCONFIRMING_OBSERVATION: >
  Increasing the order's quantity after production has started leaves the linked project task's own scope or budget structure unchanged, with no visible extension for the added quantity.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Increase an order's quantity after its linked production order has started, and check whether the project task's own scope or budget structure reflects the increase.
```

## G12-PROJECT_MRP_SALE-Q003

```yaml
QID: G12-PROJECT_MRP_SALE-Q003
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reducing an order's quantity after its linked production has already started leaves the project task's own scope description distinguishing the portion still needed from the excess already committed to production, rather than presenting the two as one undifferentiated remaining scope.
WHY_IT_MATTERS: >
  An undifferentiated scope would hide from the project team that some already-committed production work is now excess relative to the reduced order.
DISCONFIRMING_OBSERVATION: >
  After an order's quantity is reduced mid-production, the linked project task's scope description shows one undifferentiated remaining amount with no distinction between still-needed and now-excess quantity.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Reduce an order's quantity after its linked production order has started, and check whether the project task's scope description distinguishes still-needed from excess quantity.
```

## G12-PROJECT_MRP_SALE-Q004

```yaml
QID: G12-PROJECT_MRP_SALE-Q004
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order whose linked project task is tracking a part-complete production run requires an authority distinct from ordinary task editing, and the decision to halt the underlying production is attributable to a specific recorded actor rather than happening as an automatic, unattributed side effect.
WHY_IT_MATTERS: >
  An unattributed automatic halt would leave no one accountable for a decision that discards partly-completed production work.
DISCONFIRMING_OBSERVATION: >
  Cancelling the order automatically halts the part-complete production run tracked by the project task with no distinct authorization step and no attributable actor recorded for the halt decision.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Cancel an order whose linked project task tracks a part-complete production run, and check what authorization the halt required and who it is attributed to.
```

## G12-PROJECT_MRP_SALE-Q005

```yaml
QID: G12-PROJECT_MRP_SALE-Q005
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A production yield shortfall against an order is reflected as a visible scope gap on the project task tracking that order's fulfilment, rather than the task's own progress figure showing full completion despite the shortfall.
WHY_IT_MATTERS: >
  A task showing full completion despite a real shortfall would hide from the project team that the order cannot actually be fully satisfied yet.
DISCONFIRMING_OBSERVATION: >
  A production yield shortfall against an order leaves the project task's own progress figure showing full completion, with no visible scope gap recorded.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Produce a yield shortfall against an order's linked production run, and check whether the project task tracking that order shows a visible scope gap.
```

## G12-PROJECT_MRP_SALE-Q006

```yaml
QID: G12-PROJECT_MRP_SALE-Q006
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order for a customer-specific configuration after its project task has already logged effort against part-complete production preserves that logged effort as a distinguishable record, rather than discarding it along with the cancelled order.
WHY_IT_MATTERS: >
  Discarding the logged effort would leave no record of work already performed that a business might still need to account for or bill separately.
DISCONFIRMING_OBSERVATION: >
  Cancelling the order removes or hides the project task's previously logged effort for the part-complete production, leaving no distinguishable record that the work was performed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Log effort on a project task for part-complete, customer-specific production, cancel the funding order, and check whether the logged effort remains as a distinguishable record.
```

## G12-PROJECT_MRP_SALE-Q007

```yaml
QID: G12-PROJECT_MRP_SALE-Q007
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A quality failure discovered in production output already counted toward a project task's progress for an order causes that task's progress figure to be corrected downward, rather than the task retaining credit for output that has since failed inspection.
WHY_IT_MATTERS: >
  Retaining credit for failed output would overstate the project's true progress toward fulfilling the order.
DISCONFIRMING_OBSERVATION: >
  A project task's progress figure remains unchanged after output it had already counted toward the order fails a subsequent quality inspection.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Count production output toward a project task's progress for an order, fail that output at a later inspection, and check whether the task's progress figure is corrected.
```

## G12-PROJECT_MRP_SALE-Q008

```yaml
QID: G12-PROJECT_MRP_SALE-Q008
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A customer viewing their own order through a self-service portal does not see internal project task detail or production schedule information generated to track that order's fulfilment internally.
WHY_IT_MATTERS: >
  Exposing internal task or production scheduling detail would leak operational information never meant for the customer's own view of their order.
DISCONFIRMING_OBSERVATION: >
  A customer's self-service portal view of their order exposes internal project task detail or production schedule information generated to track that order's fulfilment.
EXPECTED_SURFACE: S3,S4,S5
PRECONDITIONS: >
  Create an order tracked internally through a project task and a production schedule, then view that order as the customer would through the self-service portal.
```

## G12-PROJECT_MRP_SALE-Q009

```yaml
QID: G12-PROJECT_MRP_SALE-Q009
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where one order's fulfilment is tracked across several project task phases, each fed by its own separate production run, a later phase's task is prevented from, or clearly flagged when, starting ahead of an earlier phase's production actually completing.
WHY_IT_MATTERS: >
  An unflagged out-of-sequence start would let the project's own tracking present work as properly sequenced when it was not.
DISCONFIRMING_OBSERVATION: >
  A later phase's project task starts, with no block or flag, while an earlier phase's production run it depends on has not yet completed.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Configure one order's fulfilment across two dependent project task phases, each fed by its own production run, and attempt to start the later phase before the earlier phase's production completes.
```

## G12-PROJECT_MRP_SALE-Q010

```yaml
QID: G12-PROJECT_MRP_SALE-Q010
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Planned resource hours logged on a project task for order-driven work and operation time recorded on the production order fulfilling that same work are reconciled against one shared capacity view, rather than each being scheduled independently with no visibility into the other's commitment.
WHY_IT_MATTERS: >
  Independently scheduling the same work twice would risk double-booking the same resource against two different plans for the same order.
DISCONFIRMING_OBSERVATION: >
  A resource shows as available in the project task's own scheduling view while the same resource's time is already committed on the linked production order's operation schedule, with no cross-reference between the two.
EXPECTED_SURFACE: S1,S5,S8
PRECONDITIONS: >
  Schedule a resource on a project task for order-driven work already committed on the linked production order's own operation schedule, and check whether the two views cross-reference each other.
```

## G12-PROJECT_MRP_SALE-Q011

```yaml
QID: G12-PROJECT_MRP_SALE-Q011
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  The project task's own assigned owner and the production order's own responsible person can legitimately differ, and a decision to accept a production shortfall or delay against the order is attributable to a specific one of the two rather than left ambiguous between them.
WHY_IT_MATTERS: >
  An ambiguous attribution would leave no clear accountability for a decision that directly affects what the customer is told.
DISCONFIRMING_OBSERVATION: >
  A recorded decision to accept a shortfall or delay against the order cannot be attributed to either the project task's owner or the production order's responsible person specifically.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Assign different people as the project task's owner and the production order's responsible person, record a decision to accept a shortfall or delay, and check who it is attributed to.
```

## G12-PROJECT_MRP_SALE-Q012

```yaml
QID: G12-PROJECT_MRP_SALE-Q012
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project task marked complete while the order's manufacturing-based delivery has not yet actually been fulfilled is distinguishable, in the order's own fulfilment view, from a task completion that genuinely coincides with delivery.
WHY_IT_MATTERS: >
  An indistinguishable premature completion would let the order's own fulfilment view claim the customer's goods have shipped when they have not.
DISCONFIRMING_OBSERVATION: >
  The order's own fulfilment view treats a project task marked complete identically to an actual manufacturing-based delivery, with no way to tell the two apart.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Mark a project task complete ahead of its order's actual manufacturing-based delivery, and check whether the order's fulfilment view distinguishes the two.
```

## G12-PROJECT_MRP_SALE-Q013

```yaml
QID: G12-PROJECT_MRP_SALE-Q013
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where one order-funded project has several tasks, each tied to its own separate production order, cancelling one task does not silently cancel or orphan the production orders still tied to the project's other, still-active tasks.
WHY_IT_MATTERS: >
  A cascading cancellation across unrelated tasks would destroy production work that the order still legitimately needs.
DISCONFIRMING_OBSERVATION: >
  Cancelling one task among several under the same order-funded project causes the production orders linked to the project's other, still-active tasks to also become cancelled or orphaned.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create several tasks under one order-funded project, each tied to its own separate production order, cancel one task, and check the effect on the other tasks' production orders.
```

## G12-PROJECT_MRP_SALE-Q014

```yaml
QID: G12-PROJECT_MRP_SALE-Q014
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Duplicating an order whose fulfilment already triggered a completed production run, through a project template that includes a manufacturing-triggering task, generates a fresh production trigger for the new order rather than the duplicate's task silently referencing the original, already-completed run.
WHY_IT_MATTERS: >
  A stale reference to an already-completed run would leave the new order's own fulfilment tracking pointing at goods that do not belong to it.
DISCONFIRMING_OBSERVATION: >
  Duplicating the order produces a new project task that references the original order's already-completed production run rather than triggering a fresh one of its own.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Duplicate an order whose project template task already triggered and completed a production run, and check whether the duplicate's own task triggers a fresh run or references the original.
```

## G12-PROJECT_MRP_SALE-Q015

```yaml
QID: G12-PROJECT_MRP_SALE-Q015
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The customer-facing delivery date shown against the order and the project task's own schedule date, once derived from the same underlying production plan, are reconciled to one documented rule for which updates first when production actually slips.
WHY_IT_MATTERS: >
  Two views updating independently and inconsistently would let the customer-facing date and the internal task schedule silently disagree about the same commitment.
DISCONFIRMING_OBSERVATION: >
  After production slips, the order's customer-facing delivery date and the project task's own schedule date show two different values with no documented rule for which one governs or updates first.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Derive both the order's customer-facing delivery date and a project task's schedule date from the same production plan, cause production to slip, and compare the two dates afterward.
```

## G12-PROJECT_MRP_SALE-Q016

```yaml
QID: G12-PROJECT_MRP_SALE-Q016
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Responsibility for telling the customer about a slipped delivery commitment caused by a production delay is assignable to a specific recorded actor, distinguishing whether the responsibility sits with whoever manages the order or whoever manages the project task.
WHY_IT_MATTERS: >
  Unassigned responsibility risks a slipped commitment reaching neither owner's attention until the customer notices it first.
DISCONFIRMING_OBSERVATION: >
  A production delay that slips the customer-facing delivery date generates no assignable notification responsibility on either the order's or the project task's own owner.
EXPECTED_SURFACE: S1,S5,S8
PRECONDITIONS: >
  Cause a production delay that slips an order's committed delivery date, and check whether a specific, attributable notification responsibility is generated for either the order's or the task's owner.
```

## G12-PROJECT_MRP_SALE-Q017

```yaml
QID: G12-PROJECT_MRP_SALE-Q017
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where one shared production run serves several orders each tracked by its own project task, a shortfall in that run's output is reflected proportionately across each affected task's own progress view, rather than the shortfall's impact landing entirely on whichever task happens to be checked first.
WHY_IT_MATTERS: >
  An arbitrary, non-proportionate impact would misrepresent which orders are actually at risk from the shared shortfall.
DISCONFIRMING_OBSERVATION: >
  A shortfall on a shared production run appears fully reflected in one order's project task while another order drawing on the same shortfall run shows no impact at all, with no documented allocation rule explaining the split.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Have several orders, each tracked by its own project task, draw from one shared production run, produce a shortfall on that run, and compare the impact shown on each task.
```

## G12-PROJECT_MRP_SALE-Q018

```yaml
QID: G12-PROJECT_MRP_SALE-Q018
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Whether a priority order's project task receives preferential allocation from a shared production run that falls short is governed by one documented, visible rule rather than an outcome that cannot be explained after the fact.
WHY_IT_MATTERS: >
  An inexplicable allocation outcome would leave no way to confirm that priority customers were actually treated according to any stated policy.
DISCONFIRMING_OBSERVATION: >
  Two orders of declared different priority, both tracked by their own project task and drawing on the same shortfall-affected production run, receive an allocation outcome that no documented rule can explain.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Configure two orders of different declared priority, each tracked by its own project task, to draw from a production run that falls short, and check whether the resulting allocation is explainable by a documented rule.
```

## G12-PROJECT_MRP_SALE-Q019

```yaml
QID: G12-PROJECT_MRP_SALE-Q019
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Inventory left over from a cancelled, customer-specific order remains traceable, through the project task that tracked its production, back to the specific order it was originally produced for.
WHY_IT_MATTERS: >
  Losing that traceability would leave unsellable, customer-specific inventory with no record of why it exists or which cancellation produced it.
DISCONFIRMING_OBSERVATION: >
  Leftover inventory from a cancelled, customer-specific order's production cannot be traced back, through its project task, to the order it was originally produced for.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a customer-specific order after its project task's linked production run leaves leftover inventory, and check whether that inventory remains traceable back to the order through the task.
```

## G12-PROJECT_MRP_SALE-Q020

```yaml
QID: G12-PROJECT_MRP_SALE-Q020
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Output that has failed a quality inspection is not counted toward the project task's reported progress as available to satisfy the order it was intended for, even while the failed output has not yet been formally dispositioned.
WHY_IT_MATTERS: >
  Counting undispositioned failed output as available would overstate the task's true readiness to fulfil the order.
DISCONFIRMING_OBSERVATION: >
  A project task's reported progress counts output that has already failed quality inspection as available to satisfy the order, even though the failed output has not been dispositioned.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Fail a batch of production output at quality inspection before it is dispositioned, and check whether the project task tracking that order's fulfilment still counts it as available progress.
```

## G12-PROJECT_MRP_SALE-Q021

```yaml
QID: G12-PROJECT_MRP_SALE-Q021
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project task representing internal oversight of an order's production, closed before that production physically completes, is reopened or otherwise flagged if the production later reports a problem, rather than staying closed with no path back to visibility.
WHY_IT_MATTERS: >
  A task that stays closed despite a later production problem would leave that problem invisible to whoever was tracking the order's oversight.
DISCONFIRMING_OBSERVATION: >
  A project oversight task closed ahead of production completion stays closed with no flag or reopening even after the underlying production later reports a problem.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Close a project task that oversees an order's production before that production physically completes, then have the production later report a problem, and check whether the task is reopened or flagged.
```

## G12-PROJECT_MRP_SALE-Q022

```yaml
QID: G12-PROJECT_MRP_SALE-Q022
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where two separate orders feed manufacturing runs tracked under one shared, consolidated project, the project's own task view distinguishes which order's production is behind schedule rather than presenting one combined status that hides which order is actually at risk.
WHY_IT_MATTERS: >
  A combined status would prevent whoever manages the shared project from knowing which specific customer commitment is actually in danger.
DISCONFIRMING_OBSERVATION: >
  A shared project tracking two orders' separate production runs shows one combined status with no way to tell which of the two orders is behind schedule.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Feed two separate orders' production runs into one shared, consolidated project, delay one run, and check whether the project's task view distinguishes which order is affected.
```

## G12-PROJECT_MRP_SALE-Q023

```yaml
QID: G12-PROJECT_MRP_SALE-Q023
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An order's quantity changed by a sales user and its linked project task rescheduled by a project manager at nearly the same moment both take effect, rather than one change silently overwriting the other.
WHY_IT_MATTERS: >
  A silently discarded change would leave either the order's own quantity or the task's own schedule stale with no one aware which one actually won.
DISCONFIRMING_OBSERVATION: >
  Changing an order's quantity and rescheduling its linked project task at nearly the same moment results in one of the two changes being silently discarded.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Simultaneously change an order's quantity and reschedule its linked project task, then check whether both changes are present afterward.
```

## G12-PROJECT_MRP_SALE-Q024

```yaml
QID: G12-PROJECT_MRP_SALE-Q024
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project task closed or archived while its triggering order still awaits production-based fulfilment does not leave that order's own fulfilment tracking pointing at a task that no longer offers any visible status.
WHY_IT_MATTERS: >
  A stale reference to a closed task would leave the order's own fulfilment view unable to show current progress toward delivery.
DISCONFIRMING_OBSERVATION: >
  Closing or archiving a project task leaves its triggering order's fulfilment tracking still pointing at that task with no visible status, while the order itself still awaits delivery.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Close or archive a project task whose triggering order still awaits production-based fulfilment, and check the state of the order's own fulfilment tracking afterward.
```

## G12-PROJECT_MRP_SALE-Q025

```yaml
QID: G12-PROJECT_MRP_SALE-Q025
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Deleting a project task that originally triggered a production order for a still-active customer order either blocks the deletion or leaves the production order clearly flagged as no longer tracked by any task, rather than the production order continuing silently with no visible link back to the order it serves.
WHY_IT_MATTERS: >
  A silently orphaned production order would leave no visible way to trace which customer commitment it is actually fulfilling.
DISCONFIRMING_OBSERVATION: >
  Deleting the triggering project task leaves its production order running with no visible flag or block, and no remaining link back to the order it was fulfilling.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Where task deletion is permitted, delete a project task that triggered a production order for a still-active customer order, and check the resulting state of that production order.
```

## G12-PROJECT_MRP_SALE-Q026

```yaml
QID: G12-PROJECT_MRP_SALE-Q026
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The delivery commitment date shown by the order's own view and the delivery commitment date shown by the project task's own view, both sourced from the same production schedule, agree at any given moment rather than one lagging a schedule update the other has already picked up.
WHY_IT_MATTERS: >
  Two disagreeing views of the same commitment would make it unclear which date a reviewer, or the customer, should actually trust.
DISCONFIRMING_OBSERVATION: >
  At the same moment, the order's own view and the project task's own view show two different delivery commitment dates sourced from the same production schedule.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Update the production schedule underlying an order's delivery commitment, then immediately compare the date shown in the order's own view against the date shown in the project task's own view.
```

## G12-PROJECT_MRP_SALE-Q027

```yaml
QID: G12-PROJECT_MRP_SALE-Q027
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A project task's scope description, initially defined from a planned production route at task creation, is updated to reflect what was actually produced when the completed production followed a different route than planned.
WHY_IT_MATTERS: >
  A stale scope description would leave the task claiming work that does not match what the business actually delivered against the order.
DISCONFIRMING_OBSERVATION: >
  A project task's scope description still reflects the originally planned production route after the completed production actually followed a different route.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a project task whose scope is defined from a planned production route, complete the linked production order along a different actual route, and check whether the task's scope description updates.
```

## G12-PROJECT_MRP_SALE-Q028

```yaml
QID: G12-PROJECT_MRP_SALE-Q028
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where the order's company, the project's company, and the company actually operating the production run are three different entities, visibility of the shared project task is governed by one documented rule for which entity's users may see it, rather than an unresolved conflict between three separate scopes.
WHY_IT_MATTERS: >
  An unresolved three-way visibility conflict would either expose the task to an entity that should not see it or hide it from one that legitimately needs to.
DISCONFIRMING_OBSERVATION: >
  In a three-entity setup, users from at least one of the three companies involved get a visibility outcome for the shared project task that no documented rule can explain.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure an order, its project, and its production run under three different companies, and check which of the three companies' users can see the shared project task.
```

## G12-PROJECT_MRP_SALE-Q029

```yaml
QID: G12-PROJECT_MRP_SALE-Q029
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A rush or expedite request placed on an order after its production has already started results in the project task's own priority indicator and the production order's own priority queue position being updated consistently with each other, rather than one reflecting the rush and the other not.
WHY_IT_MATTERS: >
  An inconsistent priority signal would leave the project team believing an order is expedited while production still queues it normally, or vice versa.
DISCONFIRMING_OBSERVATION: >
  A rush request on an order updates the project task's own priority indicator but leaves the production order's own queue position unchanged, or vice versa.
EXPECTED_SURFACE: S1,S5,S8
PRECONDITIONS: >
  Place a rush or expedite request on an order after its linked production has started, and compare the resulting priority indicator on the project task against the priority queue position on the production order.
```

## G12-PROJECT_MRP_SALE-Q030

```yaml
QID: G12-PROJECT_MRP_SALE-Q030
MODULE: project_mrp_sale
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Splitting an order's line into two separate orders after production has already started under one shared project task results in a documented rule for which of the two resulting orders the ongoing production work is attributed to, rather than both orders' own tasks independently claiming the same in-progress work.
WHY_IT_MATTERS: >
  Both resulting orders independently claiming the same in-progress work would overstate progress on whichever order is checked and leave the other showing none of the actual work under way.
DISCONFIRMING_OBSERVATION: >
  After an order line is split into two orders, both resulting orders' own project tasks show the same in-progress production work as their own, with no documented rule for which one it actually belongs to.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Split an order line into two separate orders after production has already started under one shared project task, and check which resulting order's task claims the ongoing production work.
```

## ARITY EXHAUSTION STATEMENT — the 48 floor is NOT met by this bank

Actual count: 30. Shortfall: 18 short of the 48 floor. Reported honestly per
GMVQ_BRIDGE_MODULE_RULE_V1.00 §7 and GMVQ_AUTHORING_STANDARD_V1.00 §2 rather than closed with
manufactured questions.

Reasoning: this bank's 30 questions already work the seam dimensions in GMVQ_BRIDGE_MODULE_RULE_V1.00
§3 for this three-way combination — ORDERING and TIMING (milestone-versus-production completion,
date reconciliation, sequencing across dependent task phases), PARTIALITY (quantity increase/decrease
mid-production, shared-run shortfall allocation across several tasks), OWNERSHIP (task owner versus
production responsible person, three-company visibility), REVERSAL/LIFECYCLE MISMATCH (cancellation
with logged effort preserved, closed oversight task with a later problem, deleted triggering task,
order-line split), QUANTITY (yield shortfall, leftover customer-specific inventory), ERROR ASYMMETRY
(quality failure counted against progress, priority-queue inconsistency), and AUTHORITY (cancellation
authorization, notification responsibility, concurrent-edit preservation). Each dimension is
represented, several more than once from a distinct triggering event.

Candidate ground that was considered and REJECTED because it duplicates a HYPOTHESIS already on disk
in a sibling bank (checked per §5 against `grep -h 'HYPOTHESIS'` on
`G08_SALES/G08_SALE_MRP_GMVQ_MVQ_48_V1.00_DRAFT.md` and `G08_SALES/G08_SALE_PROJECT_GMVQ_MVQ_48_V1.00_DRAFT.md`
before authoring):
- "the delivery date committed to the customer is derived from production's own schedule" as a pure
  order-versus-production question with no project task involved — already `sale_mrp`'s own ground;
  this bank kept only the narrower question of whether a project task's own view of that same date
  agrees with the order's (Q015, Q026).
- "cancelling an order with production part-complete leaves the work distinguishable in the resulting
  record" as a pure order-versus-production question — already `sale_mrp`'s ground; kept here only
  where a project task specifically is the thing preserving or losing that record (Q006).
- "a project's budget derived from the order's value" and "ownership of the order and the project can
  differ" — pure order-versus-project questions requiring no manufacturing at all; these are
  `sale_project`'s own ground and were not re-asked with a production order silently attached but
  playing no real role in the failure.
- "ledger cost recognition timing for order-funded manufacturing work" — this requires an accounting
  posting as the third participant, not a project task's scope/schedule view; that ground belongs to
  `project_mrp_account` (already authored in this group) and was excluded here.

Candidate ground REJECTED as belonging to a different module or arity, not this bridge:
- Physical delivery classification (delivered-to-customer versus consumed-by-project) and material
  reservation reallocation require a stock movement as a fourth participant; that ground belongs to
  `sale_project_stock` and `project_stock` and was excluded here as this module has no stock leg.
- A generic "two people can have different roles on the same record" ownership question, with no
  production-driven decision actually turning on which role holds authority, survives the bridge
  removal test with manufacturing removed and was cut as `sale_project` ground rather than kept here
  as a noun-swapped restatement.
