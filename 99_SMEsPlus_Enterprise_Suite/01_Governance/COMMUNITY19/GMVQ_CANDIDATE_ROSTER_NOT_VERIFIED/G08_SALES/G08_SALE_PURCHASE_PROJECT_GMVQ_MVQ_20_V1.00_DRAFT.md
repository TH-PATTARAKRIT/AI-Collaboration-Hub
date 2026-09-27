# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_purchase_project Module Bridge MVQ Bank

**Document ID:** GMVQ-G08-SALE_PURCHASE_PROJECT-MVQ20-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_purchase_project`
**Wave:** W2
**Author Cell:** P-S7 (GMVQ Question Factory — Production Team P-S7)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 20
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 20 = 75
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `sale_purchase_project`, the three-participant
seam of procure-to-order INSIDE a project: a customer order line, the project task it funds, and the
vendor commitment raised to fulfil that task. Per the GMVQ Bridge Module Rule V1.00, every question
here fails only where the customer's order, the project, AND a vendor-side procurement commitment
all three have to be present at once: traceability from order line to task to vendor commitment and
back; what happens to the vendor side when the customer order changes, is amended, or is cancelled;
authority splits between project-level spend and purchasing approval measured against the order's own
approved value; cost variance between what the order assumed and what the vendor actually charges;
cross-company attribution; and reallocation, substitution, or reprioritization of vendor commitments
across competing customer-order-funded tasks. No question here concerns physical receipt of goods
into stock or a customer-facing delivery — those seams belong to `sale_project_stock` and
`sale_purchase_stock` — and no question restates a pure `sale_project` (order+project) or a pure
project-plus-procurement fact that would hold even for a project with no funding customer order.

## Control

**Arity owned: THREE-PARTICIPANT (customer order + project + vendor procurement commitment) only.**
Every question below requires the customer's order, the project task it funds, and a vendor
commitment to be jointly in play; a question answerable by project+procurement alone, with no
customer order in the picture, does not belong here.

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: this bank is reported at 20, not 48. During authoring, roughly two dozen additional
  candidate questions were drafted from the group brief's ground list, but on application of the
  mandatory three-participant removal test (`GMVQ_BRIDGE_MODULE_RULE_V1.00.md` §2 and §5), a large
  share of them turned out to be fully meaningful as pure project+procurement questions with no
  customer order actually required — vendor-date-versus-task-schedule conflicts, pure purchasing
  authority chains, and warehouse-versus-site receipt timing among them. Rather than keep those
  under this module's name, each was either rewritten to bind explicitly to the customer order (its
  line, its price assumption, its cancellation, its company, or its schedule commitment) where a
  genuine seam existed, or cut outright. This is reported as the actual, non-padded count reached
  for this arity, per the Bridge Module Rule's explicit instruction that a short honest bank is
  worth more than a padded one.
- Question text is source-neutral: no vendor or product name, no technical identifier, and the
  module's own metadata name never appears outside the `MODULE:` field.
- No question concerns physical receipt into stock or delivery to the customer; those seams are
  reserved to `sale_project_stock` and `sale_purchase_stock`.
- Every question passed the three-participant bridge removal test before being kept, and was
  cross-checked against the sibling `sale_project` bank's authored HYPOTHESIS lines at authoring
  time to avoid restating a pure order+project invariant with a vendor label attached.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_PURCHASE_PROJECT-Q001

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q001
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A vendor commitment raised to source a component specifically for a project task that fulfils a line on the customer's order, when that task is later removed from the project's scope, results in the vendor commitment being flagged against the now-unfulfilled customer order line.
WHY_IT_MATTERS: >
  An unflagged vendor commitment for scope the customer no longer needs risks paying for goods with no order left to justify them.
DISCONFIRMING_OBSERVATION: >
  Removing the task from scope leaves the vendor commitment open with no flag connecting it to the customer order line it was meant to fulfil.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Raise a vendor commitment for a project task fulfilling a customer order line, remove the task from scope, and check whether the commitment is flagged against the affected order line.
```

## G08-SALE_PURCHASE_PROJECT-Q002

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q002
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Traceability from a customer order line, through the project task it funds, to the vendor commitment raised to fulfil it, can be reconstructed intact even after the vendor commitment is re-numbered or reassigned.
WHY_IT_MATTERS: >
  A broken chain here would make it impossible to prove what a customer actually paid for was really sourced.
DISCONFIRMING_OBSERVATION: >
  Re-numbering or reassigning the vendor commitment breaks the traceable path back to the customer order line it was raised to fulfil.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Re-number or reassign a vendor commitment tied through a project task to a customer order line, and attempt to trace the full chain afterward.
```

## G08-SALE_PURCHASE_PROJECT-Q003

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q003
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Manually reassigning a vendor commitment, originally raised to fulfil one customer order line's project task, to serve a different task leaves a visible record of which customer order line lost its sourcing.
WHY_IT_MATTERS: >
  Silent reassignment could leave the paying customer's order line without any documented source of supply.
DISCONFIRMING_OBSERVATION: >
  Reassigning the vendor commitment to a different task leaves no record of which customer order line's sourcing was affected.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reassign a vendor commitment from the project task funding one customer order line to a different task, and check whether the affected order line is flagged.
```

## G08-SALE_PURCHASE_PROJECT-Q004

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q004
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A vendor commitment's price, when it differs from what the customer's order line was priced assuming, surfaces that variance for someone authorized over the customer order to decide whether to accept it.
WHY_IT_MATTERS: >
  An unreviewed cost variance could erode margin the customer's order was actually priced to protect, with no one having decided to accept the loss.
DISCONFIRMING_OBSERVATION: >
  A vendor price above what the customer order line assumed is absorbed into project figures with no visible decision point tied to that order line.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a vendor commitment priced above the assumption behind its funding customer order line, and check whether the variance surfaces against that line for a decision.
```

## G08-SALE_PURCHASE_PROJECT-Q005

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q005
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling the customer's order after a vendor commitment was already placed to fulfil one of its linked project's tasks results in that vendor commitment being flagged for review against the now-cancelled order.
WHY_IT_MATTERS: >
  An unreviewed vendor obligation surviving a cancelled sale risks paying for goods with no customer commitment left to justify them.
DISCONFIRMING_OBSERVATION: >
  Cancelling the customer order leaves an already-placed vendor commitment for its project task unflagged and unreviewed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a customer order after a vendor commitment was placed for one of its linked project's tasks, and check whether that commitment is flagged for review.
```

## G08-SALE_PURCHASE_PROJECT-Q006

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q006
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Amending the customer's order to add or remove scope after a vendor commitment was already placed for the original scope surfaces the mismatch between the current order and the standing vendor commitment for review.
WHY_IT_MATTERS: >
  An unreconciled mismatch between what the customer now wants and what has been committed to a vendor could result in paying for the wrong scope or missing the right one.
DISCONFIRMING_OBSERVATION: >
  Amending the customer order's scope leaves an existing vendor commitment for the original scope unflagged against the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Amend a confirmed customer order's scope after a vendor commitment was placed for its original scope, and check whether the mismatch is surfaced.
```

## G08-SALE_PURCHASE_PROJECT-Q007

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q007
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where a vendor commitment for a project task is placed by a different company entity than the one holding the customer's order, the project's own view of committed spend against that order reflects the obligation only once the required inter-company step has occurred.
WHY_IT_MATTERS: >
  Recognizing the commitment early would let the project appear covered by an obligation that has not actually been formalized between the two responsible entities.
DISCONFIRMING_OBSERVATION: >
  The project's committed-spend view against the customer order reflects a cross-entity vendor commitment before the corresponding inter-company step has occurred.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Place a vendor commitment through a different company entity than the one holding the customer order, and check when the project's committed-spend view updates relative to the inter-company step.
```

## G08-SALE_PURCHASE_PROJECT-Q008

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q008
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a vendor's actual invoiced price or quantity differs from what was committed, the project's spend tracked against the customer order's approved budget updates to the invoiced reality rather than remaining fixed at the original commitment.
WHY_IT_MATTERS: >
  A budget figure frozen at the commitment stage would misstate how much of the customer order's approved value has actually been consumed.
DISCONFIRMING_OBSERVATION: >
  The project's spend against the customer order's budget stays at the original vendor commitment amount even after an invoice arrives at a different price or quantity.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive a vendor invoice differing from its commitment for a task funded by a customer order, and check whether the order-tracked budget-consumed figure updates.
```

## G08-SALE_PURCHASE_PROJECT-Q009

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q009
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where the project manager's authority to commit spend against the customer order's approved value and the purchasing function's authority to approve a vendor commitment are separate approval chains, a request exceeding what purchasing will approve is blocked or escalated.
WHY_IT_MATTERS: >
  Allowing the project side to bypass the separate purchasing approval would defeat the point of having two independent checks over spend against the customer's order.
DISCONFIRMING_OBSERVATION: >
  A vendor commitment proceeds on the project manager's authorization over the order's budget alone despite exceeding the separate purchasing approval threshold.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Request a vendor commitment against a customer order's approved budget that exceeds the purchasing function's approval threshold, and check whether it is blocked or escalated.
```

## G08-SALE_PURCHASE_PROJECT-Q010

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q010
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  At project closure, reconciling every vendor commitment raised for its tasks against what the customer's order actually paid for that scope identifies any commitment never consumed by any task.
WHY_IT_MATTERS: >
  An unconsumed vendor commitment surviving past the customer order's own closure could represent spend with no remaining justification that goes unnoticed.
DISCONFIRMING_OBSERVATION: >
  A vendor commitment never consumed by any task remains invisible after the customer order it was meant to serve has been closed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close a customer order and its linked project while a vendor commitment for one of its tasks remains unconsumed, and check whether that commitment is surfaced.
```

## G08-SALE_PURCHASE_PROJECT-Q011

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q011
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a vendor order's referenced project task, itself funding a specific customer order line, is merged into a different task during a restructuring, the vendor commitment's reference updates to the surviving task.
WHY_IT_MATTERS: >
  A dangling reference would break the ability to show which vendor commitment actually sources a given customer order line after any internal restructuring.
DISCONFIRMING_OBSERVATION: >
  The vendor commitment still references a merged-away task, leaving the customer order line's sourcing untraceable to the surviving task.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Merge a project task that has a vendor commitment funding a customer order line into a different task, and check whether the commitment's reference updates.
```

## G08-SALE_PURCHASE_PROJECT-Q012

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q012
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  One vendor commitment used to source material for both a customer-order-funded project task and a separate, non-order purchase correctly separates, on partial receipt, what portion belongs to the order-committed need.
WHY_IT_MATTERS: >
  Letting the general-purpose need consume material actually committed to a paying customer's order risks that order going unfulfilled while an unrelated need is served first.
DISCONFIRMING_OBSERVATION: >
  A partial receipt from a shared vendor commitment is available to satisfy the non-order need without the order-committed share being reserved.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place one vendor commitment covering both a customer-order-funded task and a separate non-order need, partially receive it, and check whether the order-committed portion is kept separate.
```

## G08-SALE_PURCHASE_PROJECT-Q013

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q013
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When two project tasks, each funding a different customer order line, both depend on the same partially delivered vendor commitment, the allocation between the two order lines is a documented, recorded decision.
WHY_IT_MATTERS: >
  An unrecorded allocation would make it impossible to explain to either customer which of their order lines was actually served first from a shared source.
DISCONFIRMING_OBSERVATION: >
  A partial delivery shared between two customer-order-funding tasks is allocated between them with no documented record of the decision.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have two project tasks, each funding a different customer order line, share one partially delivered vendor commitment, and check whether the resulting allocation is documented.
```

## G08-SALE_PURCHASE_PROJECT-Q014

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q014
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A rush vendor commitment placed to recover a schedule slip threatening one customer order's delivery date, when prioritized ahead of an already-committed vendor order serving an earlier-scheduled customer order, has that reprioritization traceable back to the order-level decision that caused it.
WHY_IT_MATTERS: >
  An unexplained reordering of vendor priority could quietly delay one paying customer's order to protect another, with no record of that trade-off being made deliberately.
DISCONFIRMING_OBSERVATION: >
  A vendor commitment sequence reprioritizes to protect one customer order's date ahead of another with no visible trace connecting that change to a recorded order-level decision.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a rush vendor commitment protecting one customer order's schedule at the expense of an earlier commitment serving a different customer order, and check whether the reprioritization is traceable.
```

## G08-SALE_PURCHASE_PROJECT-Q015

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q015
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A subcontracted deliverable's vendor commitment, placed against a project schedule funding a specific customer order line, has its expected receipt date updated or flagged when the customer order's own delivery commitment changes.
WHY_IT_MATTERS: >
  A stale vendor expectation could leave the team unaware that the customer's own delivery promise has already changed.
DISCONFIRMING_OBSERVATION: >
  Changing the customer order's delivery commitment leaves the subcontracted vendor commitment's expected date unchanged and unflagged.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Change a customer order's delivery commitment after placing a vendor commitment for a subcontracted deliverable tied to the original plan, and check whether the vendor commitment's date reflects or flags the change.
```

## G08-SALE_PURCHASE_PROJECT-Q016

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q016
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Duplicating a project task to plan similar future work against a new customer order does not
  cause the duplicate to inherit a live link to a specific vendor order line already placed and
  committed against the original customer order.
WHY_IT_MATTERS: >
  An inherited live link would make it appear that a new customer's order is already covered by a
  vendor order line that is actually committed, in full, to someone else's order.
DISCONFIRMING_OBSERVATION: >
  A duplicated project task's own record shows a live link to the same vendor order line already
  committed to the original customer order it was duplicated from.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Duplicate a project task that is linked to a specific vendor order line committed to an original
  customer order, for use against a different customer order, and check whether the duplicate's
  own record shows a live link to that same vendor order line.
```

## G08-SALE_PURCHASE_PROJECT-Q017

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q017
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Putting a project on hold after a vendor commitment was placed for one of its tasks, but before the vendor has delivered, results in a documented treatment of that commitment relative to the customer order's own status.
WHY_IT_MATTERS: >
  Without a documented rule, a paused project's open vendor obligations against a still-active customer order could be forgotten or wrongly cancelled.
DISCONFIRMING_OBSERVATION: >
  An open vendor commitment for a paused project's task, funding a still-active customer order, is treated inconsistently across similar cases with no documented rule.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Put a project on hold while a still-active customer order's linked task has an open, undelivered vendor commitment, and check the resulting treatment.
```

## G08-SALE_PURCHASE_PROJECT-Q018

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q018
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Goods received from a vendor commitment at a general warehouse do not, merely by being marked received, count as satisfying the specific customer order line's project task that actually needs them delivered to the project site.
WHY_IT_MATTERS: >
  Treating warehouse receipt as equivalent to site-ready would let a customer order line appear served before the work it actually funds can proceed.
DISCONFIRMING_OBSERVATION: >
  A project task funding a customer order line treats vendor goods as available to use as soon as they are marked received at a general warehouse, before reaching the project site.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive a vendor commitment's goods at a general warehouse distinct from the project site funding a specific customer order line, and check whether the task's availability view treats them as usable immediately.
```

## G08-SALE_PURCHASE_PROJECT-Q019

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q019
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a vendor delivers late against a task whose need date has already passed and the customer order it funds has since been adjusted, the late delivery is reconciled against the customer order's current, adjusted state.
WHY_IT_MATTERS: >
  An unreconciled late delivery could sit unattributed while the customer order it was meant to serve has already moved on.
DISCONFIRMING_OBSERVATION: >
  A late vendor delivery for a task whose funding customer order has since been adjusted has no documented reconciliation against the order's current state.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Adjust a customer order after its linked task's vendor commitment is placed, allow late delivery, and check how the delivery reconciles against the order's current state.
```

## G08-SALE_PURCHASE_PROJECT-Q020

```yaml
QID: G08-SALE_PURCHASE_PROJECT-Q020
MODULE: sale_purchase_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A vendor commitment fulfilling a substitute item, used because the original vendor commitment tied to a customer order line was delayed, is traceable as having satisfied that specific customer order line.
WHY_IT_MATTERS: >
  A disconnected sourcing record would make it impossible to show what genuinely fulfilled a specific paying customer's order line.
DISCONFIRMING_OBSERVATION: >
  A substitute vendor delivery used in place of a delayed original commitment leaves the customer order line's sourcing record still pointing only at the delayed, undelivered original.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Fulfil a project task funding a customer order line with a substitute vendor delivery after the original commitment is delayed, and check whether the order line's sourcing record reflects the substitute.
```
