# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_mrp_account Module Bridge MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_MRP_ACCOUNT-MVQ32-V1.00
**Group:** G12 PROJECT
**Module Metadata:** `project_mrp_account`
**Wave:** GMVQ 25-Team Acceleration (2026-09-27)
**Author Cell:** P12-3 (GMVQ Question Factory — Production Cell P12-3)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 32
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 32 = 87
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `project_mrp_account`, the three-participant seam
between a project's own cost and budget tracking, a manufacturing order's costing lifecycle
(work-in-progress, variance, by-product and scrap value, operation cost), and the accounting ledger
that records it — with NO customer order in scope. Per the GMVQ Bridge Module Rule V1.00, every
question here fails only where the project's own cost or budget view, a manufacturing order's
costing behaviour, AND a ledger posting all three have to be present at once.

Mandatory pre-authoring sibling check performed per GMVQ_BRIDGE_MODULE_RULE_V1.00 §5:
`grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G06_MANUFACTURING/G06_MRP_ACCOUNT_GMVQ_MVQ_48_V1.00_DRAFT.md`
and `01_QUESTION_BANKS/G08_SALES/G08_SALE_PROJECT_STOCK_ACCOUNT_GMVQ_MVQ_28_V1.00_DRAFT.md` (plus its
supplement) were read in full before authoring. No question below restates a pure `mrp_account`
hypothesis (production-order costing with no project in the picture) or a `sale_project_stock_account`
hypothesis (which requires a funding customer order and a physical stock/delivery leg — neither of
which this module has). Where `mrp_account` already asks the general production-costing question
(WIP separation, variance timing, by-product/scrap treatment, multi-company posting, rounding,
manual-adjustment authority), this bank asks the narrower question of whether that same behaviour is
correctly carried into, and stays consistent with, the PROJECT's own cost or budget view of the same
work — a question that would not make sense at all for a production order with no project task
attached, and is not answered by the order-funded, stock-moving `sale_project_stock_account` bank
because no customer order or physical delivery is involved here.

## Control

**Arity owned: THREE-PARTICIPANT (project cost/budget view + manufacturing order costing +
accounting ledger) only.** No customer order participates in this module; a question that requires a
funding order does not belong here — see `project_mrp_sale` and `sale_project_stock_account` instead.

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: these 32 questions test 32 distinct material seam hypotheses, spread across ordering,
  partiality, ownership, timing, reversal, quantity/money, lifecycle mismatch and authority per the
  Bridge Module Rule §3. An honest exhaustion statement follows the questions rather than stretched
  wording used to reach 48.
- Question text is source-neutral: no vendor or product name, no technical identifier, and the
  module's own metadata name never appears outside the `MODULE:` field.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## G12-PROJECT_MRP_ACCOUNT-Q001

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q001
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  While a production order feeding a project task is still open, the project's own recognized cost for that task and the manufacturing order's own work-in-progress balance do not both separately claim the same consumed value as their own final figure.
WHY_IT_MATTERS: >
  Both sides independently claiming the same interim value as settled would overstate the project's true cost the moment either side is read on its own.
DISCONFIRMING_OBSERVATION: >
  Reading the project's recognized cost for the task and the production order's own work-in-progress balance at the same moment shows the same consumed value counted as final in both places at once.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Link a production order to a project task, consume components without completing the order, and compare the project's recognized cost figure against the production order's own work-in-progress balance.
```

## G12-PROJECT_MRP_ACCOUNT-Q002

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q002
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A cost variance realized when a production order feeding a project task closes is reflected in the project's own cost view through one documented, consistently timed rule, rather than a rule that differs unexplained between similarly configured tasks.
WHY_IT_MATTERS: >
  An unexplained difference in when variance reaches the project's own figures would make two similar tasks' reported cost incomparable for no real reason.
DISCONFIRMING_OBSERVATION: >
  Two similarly configured project tasks, each fed by a production order that closes with a variance, show that variance landing in the project's own cost view at two different points with no configuration difference explaining why.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Close two similarly configured production orders, each feeding its own project task, each with a realized cost variance, and compare when that variance appears in each task's own cost view.
```

## G12-PROJECT_MRP_ACCOUNT-Q003

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q003
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A production order that consumed components for a project task and is then abandoned — neither completed nor explicitly cancelled — does not leave the project's own cost view silently omitting that consumed value while the ledger still carries it as an open balance.
WHY_IT_MATTERS: >
  A silent gap between what the project shows and what the ledger still holds would leave a real consumed cost invisible to whoever reviews the project's own figures.
DISCONFIRMING_OBSERVATION: >
  A production order left neither completed nor cancelled after consuming components for a project task shows no trace of that consumed value in the project's own cost view, while the ledger still carries the value as an open balance.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Consume components on a production order feeding a project task, leave the order neither completed nor cancelled, and compare the project's own cost view against the ledger's open balance for that order.
```

## G12-PROJECT_MRP_ACCOUNT-Q004

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q004
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When one production order's output is split to feed two separate project tasks, the recognized cost each task's own view shows is a documented share of that order's total cost rather than the full order cost independently claimed by each task.
WHY_IT_MATTERS: >
  Two tasks each independently claiming the full cost of a shared production order would overstate the combined project's total cost.
DISCONFIRMING_OBSERVATION: >
  Two project tasks each fed from a share of the same production order's output both show that order's full recognized cost in their own cost view, rather than a documented split.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split one production order's output to feed two separate project tasks, and compare the recognized cost each task's own view shows against the order's total cost.
```

## G12-PROJECT_MRP_ACCOUNT-Q005

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q005
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project archived or closed while a production order still feeding one of its tasks remains open does not leave that order's future cost postings with nowhere documented to land.
WHY_IT_MATTERS: >
  A future posting with no documented destination would either be silently dropped or land somewhere no one reviewing the closed project would ever see.
DISCONFIRMING_OBSERVATION: >
  Closing or archiving the project while its linked production order remains open leaves that order's later cost postings with no documented destination once they occur.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Archive or close a project whose task is fed by a still-open production order, let that order post further cost, and check where the posting lands.
```

## G12-PROJECT_MRP_ACCOUNT-Q006

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q006
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A manual adjustment posted to a completed production order's cost after the project's own cost report for that task was already generated is reflected the next time that report is regenerated, rather than the report staying frozen at its earlier figure with no indication a later adjustment exists.
WHY_IT_MATTERS: >
  A report that silently stays stale would let a reviewer rely on a project cost figure that a later correction has already superseded.
DISCONFIRMING_OBSERVATION: >
  Regenerating the project's cost report after a manual adjustment to the underlying production order's cost still shows the earlier, unadjusted figure with no indication that a later change exists.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Generate a project task's cost report, post a manual adjustment to its linked production order's already-completed cost, and regenerate the report to compare.
```

## G12-PROJECT_MRP_ACCOUNT-Q007

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q007
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where the project's own company and the company actually operating the production order feeding it differ, the manufacturing cost posts to one documented entity's ledger with any required inter-company transaction generated alongside it.
WHY_IT_MATTERS: >
  A missing inter-company step would leave one entity's books recognizing a manufacturing cost against a project it does not itself own, with no corresponding entry on the entity that actually produced the goods.
DISCONFIRMING_OBSERVATION: >
  Manufacturing cost is recognized against the project's company without the corresponding inter-company transaction that should accompany production performed by a different company.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  In a multi-company setup, link a project task to a production order operated by a different company than the project's own, and check whether cost recognition and any required inter-company entry both occur.
```

## G12-PROJECT_MRP_ACCOUNT-Q008

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q008
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A by-product value credited when a production order feeding a project task completes is reflected in that task's own recognized cost as a documented offset, rather than the offset landing only in general manufacturing accounts with no trace back to the project.
WHY_IT_MATTERS: >
  An offset that never reaches the project would overstate that task's true net cost relative to what the business actually incurred.
DISCONFIRMING_OBSERVATION: >
  A by-product credit generated by a production order feeding a project task is posted to a general manufacturing account with no documented offset appearing in that task's own recognized cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a production order that yields a by-product while feeding a project task, and check whether the by-product's credited value appears as an offset in the task's own recognized cost.
```

## G12-PROJECT_MRP_ACCOUNT-Q009

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q009
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Scrap value recorded during a production order feeding a project task is distinguishably represented in that task's own cost view, rather than blended invisibly into the same figure as good output cost.
WHY_IT_MATTERS: >
  A blended figure would prevent whoever reviews the task's cost from telling how much of it came from scrap rather than usable output.
DISCONFIRMING_OBSERVATION: >
  Scrap recorded on a production order feeding a project task shows up in the task's own cost view only as part of an undifferentiated total, with no way to isolate the scrap portion.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record scrap during a production order feeding a project task, and check whether the task's own cost view separately identifies the scrap portion.
```

## G12-PROJECT_MRP_ACCOUNT-Q010

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q010
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Retrieving a project task's recognized manufacturing cost when the production order's own costing currency differs from the project's own reporting currency uses one documented rate and moment consistently, not a different one depending on which screen or report is used.
WHY_IT_MATTERS: >
  Two views converting the same cost differently would make the task's own reported figure numerically unreliable.
DISCONFIRMING_OBSERVATION: >
  Two different reports of the same task's recognized manufacturing cost, across the two currencies involved, use different conversion rates or moments for the same underlying production order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Link a project task, tracked in one reporting currency, to a production order costed in a different currency, and compare the task's recognized cost as shown in two different reports.
```

## G12-PROJECT_MRP_ACCOUNT-Q011

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q011
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A project task's budget, once derived from a production order's planned or estimated cost at task creation, follows one documented rule for whether it later updates to the order's actual realized cost or stays fixed at the original estimate, applied consistently rather than drifting between the two for similar tasks.
WHY_IT_MATTERS: >
  An inconsistent rule would make budget-versus-actual comparisons meaningless across otherwise similar tasks.
DISCONFIRMING_OBSERVATION: >
  Two similarly configured project tasks, each fed by a production order whose actual cost differs from its original estimate, show one task's budget updating to the actual figure and the other staying fixed, with no configuration difference explaining why.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create two similarly configured project tasks each fed by a production order, let each order's actual cost diverge from its original estimate, and compare whether each task's budget figure updates.
```

## G12-PROJECT_MRP_ACCOUNT-Q012

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q012
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Labour time logged directly on a project task and operation time recorded on a production order feeding that same task are not both counted as separate cost components in the task's own total recognized cost when they represent the same work.
WHY_IT_MATTERS: >
  Counting the same labour twice would inflate the task's true cost and mislead any profitability comparison built on it.
DISCONFIRMING_OBSERVATION: >
  The same work is recorded once as logged time directly on the project task and again as operation time on its linked production order, and the task's total recognized cost sums both as if they were separate costs.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Log time directly on a project task for work also recorded as operation time on its linked production order, and check whether the task's total recognized cost counts it once or twice.
```

## G12-PROJECT_MRP_ACCOUNT-Q013

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q013
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Deleting a project task whose linked production order has already posted cost against it leaves that posted cost entry intact and correctly referenced, rather than orphaned or silently reversed as a side effect of deleting the task.
WHY_IT_MATTERS: >
  A silently reversed or orphaned posting would corrupt the manufacturing cost record with no one having decided to change it.
DISCONFIRMING_OBSERVATION: >
  Deleting the project task either leaves its linked production order's posted cost entry with a broken reference, or silently reverses that entry as an unintended side effect of the deletion.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Where task deletion is permitted, delete a project task whose linked production order already posted cost against it, and check the state of that posted entry afterward.
```

## G12-PROJECT_MRP_ACCOUNT-Q014

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q014
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing or unbuilding a completed production order after its cost was already reflected in a project task's own cost view produces a documented, visible correction in that task's cost view rather than leaving the task's figure unchanged while the underlying manufacturing record no longer supports it.
WHY_IT_MATTERS: >
  An unreversed task figure would keep showing a cost the manufacturing side no longer actually recognizes.
DISCONFIRMING_OBSERVATION: >
  Reversing or unbuilding a production order leaves the project task's own cost view unchanged, still reflecting the cost as if the reversal had not happened.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Reverse or unbuild a completed production order whose cost was already reflected in a project task's cost view, and check whether the task's view is correspondingly corrected.
```

## G12-PROJECT_MRP_ACCOUNT-Q015

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q015
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Small rounding differences accumulated across several production orders rolled up into one project task's total recognized cost remain bounded and traceable, rather than compounding into a materially wrong total with no way to see where the difference came from.
WHY_IT_MATTERS: >
  An untraceable compounding rounding difference would make a project task's total cost figure impossible to reconcile back to its component orders.
DISCONFIRMING_OBSERVATION: >
  A project task fed by several production orders shows a total recognized cost that differs from the sum of its component orders' own costs by more than a traceable rounding amount, with no way to identify the source.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Roll up several production orders' costs into one project task's total, and compare that total against the sum of each order's own recognized cost.
```

## G12-PROJECT_MRP_ACCOUNT-Q016

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q016
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where one project task is fed by two production orders whose components are costed under two different valuation methods, the task's combined recognized cost correctly separates each order's own true cost basis rather than blending the two into one indistinguishable figure.
WHY_IT_MATTERS: >
  A blended figure would make it impossible to tell which of the two production orders actually drove the task's cost.
DISCONFIRMING_OBSERVATION: >
  The project task's combined recognized cost blends two production orders' differently-valued costs into one figure that cannot be separated back into each order's true basis.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Feed one project task from two production orders costed under two different valuation methods, and check whether the task's combined cost figure can be separated back into each order's own basis.
```

## G12-PROJECT_MRP_ACCOUNT-Q017

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q017
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Manually adjusting a project task's manufacturing-derived cost figure after it has already posted requires a permission distinct from the permission needed merely to view the task's own cost report, and the adjustment is attributed to the user who made it.
WHY_IT_MATTERS: >
  Allowing anyone who can view a task's cost to also alter it would remove any real control over a figure that feeds project profitability reporting.
DISCONFIRMING_OBSERVATION: >
  A user with only view access to a project task's cost report is able to alter its already-posted manufacturing-derived cost figure, or the alteration carries no attributable actor.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  As a user with view-only access to a project task's cost report, attempt to manually adjust its already-posted manufacturing-derived cost figure.
```

## G12-PROJECT_MRP_ACCOUNT-Q018

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q018
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A near-simultaneous manual note edited on a project task's cost record and a production order's own cost posting landing at nearly the same moment are both preserved, rather than one silently overwriting the other.
WHY_IT_MATTERS: >
  A silently discarded update would leave either the manual note or the actual posted cost missing with no one aware it was lost.
DISCONFIRMING_OBSERVATION: >
  Editing a project task's cost-related note at nearly the same moment its linked production order posts a cost results in one of the two changes being silently discarded.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Simultaneously edit a project task's cost-related note and let its linked production order post a cost, then check whether both changes are present afterward.
```

## G12-PROJECT_MRP_ACCOUNT-Q019

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q019
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Whether a project task's recognized manufacturing cost is captured at the moment components are consumed on the production order or only once that order completes is one documented, consistently applied rule across similar tasks.
WHY_IT_MATTERS: >
  An unexplained difference in timing between similar tasks would make cost recognition unpredictable and hard to audit.
DISCONFIRMING_OBSERVATION: >
  Two similarly configured project tasks recognize manufacturing cost at different moments, one at component consumption and one at order completion, with no configuration difference explaining why.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Compare the cost-recognition timing of two similarly configured project tasks, one whose linked production order completes quickly and one whose order remains open for an extended period after consumption.
```

## G12-PROJECT_MRP_ACCOUNT-Q020

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q020
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A recognized manufacturing cost entry referencing a project task that is later merged into a different task has its reference updated to the surviving task, rather than being left pointing at a task that no longer exists.
WHY_IT_MATTERS: >
  A cost entry pointing at a task that no longer exists would become untraceable back to the work it was actually meant to represent.
DISCONFIRMING_OBSERVATION: >
  A recognized manufacturing cost entry still references a project task after that task has been merged into a different task, with no update to the surviving task's reference.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Recognize manufacturing cost against a project task, merge that task into a different task, and check whether the cost entry's reference is updated.
```

## G12-PROJECT_MRP_ACCOUNT-Q021

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q021
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project put on hold after manufacturing cost was already recognized against one of its tasks does not continue accruing further production-driven cost against that same task as though work were still actively progressing.
WHY_IT_MATTERS: >
  Continued accrual against a paused project would overstate cost incurred for work that is not actually progressing.
DISCONFIRMING_OBSERVATION: >
  A paused project's task continues to accrue further manufacturing-driven cost identical to an active task, with no distinction made for the hold.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Put a project on hold after manufacturing cost was recognized against one of its tasks, let its linked production order continue, and check whether cost keeps accruing against the task.
```

## G12-PROJECT_MRP_ACCOUNT-Q022

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q022
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A component substituted mid-production at a different cost than originally planned, for a production order feeding a project task, has the task's own recognized cost reflect the substituted component's actual cost rather than the originally planned component's cost.
WHY_IT_MATTERS: >
  Reporting a planned-but-never-used cost as the task's actual cost would misstate the true cost of what was actually consumed.
DISCONFIRMING_OBSERVATION: >
  A project task's recognized cost still reflects the originally planned component's cost after a mid-production substitution, rather than the substituted component's actual cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Substitute a component at a different cost mid-production on an order feeding a project task, and check which cost the task's own recognized figure reflects.
```

## G12-PROJECT_MRP_ACCOUNT-Q023

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q023
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When an operation or labour rate used by a production order feeding a project task changes partway through that order's progress, the portion of the task's recognized cost already posted before the change is not silently restated at the new rate.
WHY_IT_MATTERS: >
  A silent restatement would change a previously reported task cost with no one having decided to revalue it.
DISCONFIRMING_OBSERVATION: >
  A rate change partway through a production order causes the project task's already-posted cost for the portion completed before the change to be recalculated at the new rate.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Change an operation or labour rate partway through a production order feeding a project task, and check whether the task's already-posted cost for the earlier portion changes.
```

## G12-PROJECT_MRP_ACCOUNT-Q024

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q024
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A project task's total manufacturing-derived cost, when queried through the task's own detail view and through the project's overall cost summary view, shows the same figure in both.
WHY_IT_MATTERS: >
  Two disagreeing views of the same underlying cost would make it unclear which figure a reviewer should actually trust.
DISCONFIRMING_OBSERVATION: >
  The task's detail view and the project's overall cost summary view show two different figures for the same task's manufacturing-derived cost at the same moment.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Recognize manufacturing cost against a project task, then compare the figure shown in the task's own detail view against the figure shown in the project's overall cost summary view.
```

## G12-PROJECT_MRP_ACCOUNT-Q025

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q025
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A negative or credit-style cost posting from a production order — such as a return of components back to stock — reduces a project task's own recognized cost by that same amount rather than being ignored by the task's own view.
WHY_IT_MATTERS: >
  An ignored credit would leave a project task's cost permanently overstated relative to what was actually consumed.
DISCONFIRMING_OBSERVATION: >
  A production order's negative or credit-style cost posting has no effect at all on the project task's own recognized cost figure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a negative or credit-style cost adjustment on a production order feeding a project task, such as a component return, and check whether the task's recognized cost decreases accordingly.
```

## G12-PROJECT_MRP_ACCOUNT-Q026

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q026
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A project task's manufacturing-derived cost export, generated as evidence while its linked production order is still open, is marked as provisional rather than presented identically to an export generated after the order has fully settled.
WHY_IT_MATTERS: >
  An unmarked provisional figure could be mistaken for a final, settled cost by whoever later relies on that exported evidence.
DISCONFIRMING_OBSERVATION: >
  An exported cost report generated while the linked production order is still open is indistinguishable in its own content from one generated after the order has fully settled.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Export a project task's manufacturing-derived cost report while its linked production order is still open, and compare its content against an export taken after the order settles.
```

## G12-PROJECT_MRP_ACCOUNT-Q027

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q027
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where the entity actually operating a production order feeding a project task lacks a required valuation account of its own, the project task's cost view shows a documented blocking condition rather than silently carrying no cost for work that demonstrably happened.
WHY_IT_MATTERS: >
  A silently missing cost would understate the task's true cost with no visible indication that anything went wrong.
DISCONFIRMING_OBSERVATION: >
  A production order run by an entity lacking a required valuation account still completes, and the project task's cost view shows no cost at all for it with no blocking condition or flag recorded.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure an entity operating a production order to lack a required valuation account, run the order to completion under a project task, and check the task's resulting cost view.
```

## G12-PROJECT_MRP_ACCOUNT-Q028

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q028
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A manual adjustment made to a project task's manufacturing-derived cost leaves a retained trace identifying who made the change, when, and what the prior figure was.
WHY_IT_MATTERS: >
  An untraceable adjustment would make it impossible to later explain why a task's reported cost differs from what the linked production order itself shows.
DISCONFIRMING_OBSERVATION: >
  A manual adjustment to a project task's manufacturing-derived cost leaves no retained record of who made it, when, or what the prior figure was.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Manually adjust a project task's manufacturing-derived cost figure, and check whether a retained trace of the change, its actor, and the prior value exists afterward.
```

## G12-PROJECT_MRP_ACCOUNT-Q029

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q029
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project task's manufacturing-derived cost figure, once posted, does not silently change when the underlying component's standard cost is later revised, without a deliberate revaluation step having been taken.
WHY_IT_MATTERS: >
  An unintended retroactive change would alter a previously reported task cost with no one having decided to revalue it.
DISCONFIRMING_OBSERVATION: >
  A later standard-cost revision silently alters a project task's already-posted manufacturing-derived cost with no deliberate revaluation step having been taken.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Post manufacturing cost to a project task at a component's prior standard cost, revise that standard cost afterward, and check whether the task's already-posted figure changes.
```

## G12-PROJECT_MRP_ACCOUNT-Q030

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q030
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A project task spanning a fiscal year boundary, whose linked production order posts cost in one year while the task's own budget review happens in the next, shows that one-period timing gap visibly rather than smoothing it away.
WHY_IT_MATTERS: >
  A silently smoothed gap would hide a real timing difference that internal financial reporting is supposed to disclose.
DISCONFIRMING_OBSERVATION: >
  The cross-year timing gap between a project task's recognized manufacturing cost and its own budget review is smoothed away by an unexplained adjustment rather than shown as the actual timing difference it is.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a project task's manufacturing cost in one fiscal year and hold its budget review in the next, and check whether the resulting timing gap is visible or silently adjusted away.
```

## G12-PROJECT_MRP_ACCOUNT-Q031

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q031
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  At project closure, reconciling a task's own recognized manufacturing cost against the linked production order's own final cost uses one documented register as authoritative when a gap is found between the two.
WHY_IT_MATTERS: >
  Two reconciliation views producing two different closing figures would make it impossible to know the task's actual final cost.
DISCONFIRMING_OBSERVATION: >
  Two different closure reconciliation reports for the same project task produce different closing cost figures because they treat different registers as authoritative.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a reconciliation gap between a project task's own recognized cost and its linked production order's final cost, close the project, and compare the closing figure from two different reconciliation views.
```

## G12-PROJECT_MRP_ACCOUNT-Q032

```yaml
QID: G12-PROJECT_MRP_ACCOUNT-Q032
MODULE: project_mrp_account
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Correcting a misattributed cost posting that was wrongly assigned to a project task's production order corrects both the task's own cost view and the production order's own cost record together.
WHY_IT_MATTERS: >
  Fixing only one side would leave the task's own figure still reflecting an error that the production order's own record no longer shows, or vice versa.
DISCONFIRMING_OBSERVATION: >
  Correcting a misattributed posting updates the project task's own cost view but leaves the production order's own cost record still reflecting the original error, or vice versa.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Correct a cost posting that was wrongly attributed to a project task's linked production order, and check whether both the task's and the order's cost figures reflect the correction.
```

## ARITY EXHAUSTION STATEMENT — the 48 floor is NOT met by this bank

Actual count: 32. Shortfall: 16 short of the 48 floor. Reported honestly per
GMVQ_BRIDGE_MODULE_RULE_V1.00 §7 and GMVQ_AUTHORING_STANDARD_V1.00 §2 rather than closed with
manufactured questions.

Reasoning: this bank's 32 questions already work the seam dimensions in GMVQ_BRIDGE_MODULE_RULE_V1.00
§3 for this specific three-way combination — ORDERING and TIMING (WIP-versus-final double counting,
variance-timing consistency, consumption-versus-completion recognition point, rate changes mid-order,
fiscal-year-boundary gaps), PARTIALITY (one order split across two tasks, one task fed by two orders
under different valuation methods), OWNERSHIP (which register is authoritative at closure, task-merge
reference update), REVERSAL (unbuild/reversal propagation, component-return credit, standard-cost
retroactive restatement), QUANTITY AND MONEY (rounding roll-up across several orders, currency
conversion consistency, by-product and scrap distinguishability), LIFECYCLE MISMATCH (abandoned order,
archived project with an order still open, paused project still accruing), and AUTHORITY (adjustment
permission distinct from view, retained trace of manual adjustment, concurrent-edit preservation).
Each of these dimensions is represented, several more than once from a distinct triggering event,
which is the expected density for a ledger-facing three-way bridge — the Bridge Module Rule itself
anticipates this in §7: "a short honest bank is worth more than a padded one."

Candidate ground that was considered and REJECTED because it duplicates a HYPOTHESIS already on disk
in a sibling or base bank (checked per §5 against `grep -h 'HYPOTHESIS'` on
`G06_MANUFACTURING/G06_MRP_ACCOUNT_GMVQ_MVQ_48_V1.00_DRAFT.md` and
`G08_SALES/G08_SALE_PROJECT_STOCK_ACCOUNT_GMVQ_MVQ_28_V1.00_DRAFT.md` before authoring):
- "the total value of components consumed by a production order reconciles to the value assigned to
  output" — this is a pure two-participant production-costing invariant that holds with no project
  task involved at all; it belongs to `mrp_account` and was cut rather than re-asked with a task
  attached but no genuine project-side consequence.
- "whether variance is recognized only once at final closure or incrementally" as a pure production
  question — already covered by `mrp_account`; this bank kept only the narrower question of whether
  that recognition timing is consistently carried into the project's own view (Q002), not the
  underlying production-accounting mechanics themselves.
- "material issued to a project task is not double-counted as cost and as stock valuation" and
  "cancelling a funding order unwinds recognized revenue and cost together" — these require a
  customer order and a physical stock/delivery leg that this module does not have; that ground
  belongs to `sale_project_stock_account` (already authored) and was not re-asked here with the order
  or delivery role silently dropped.
- "a project's own delivery-status or scheduling reconciliation against manufacturing progress" —
  this is a scheduling and status question, not an accounting one; the bridge test applied here (does
  it fail only when project, manufacturing, AND accounting are all three present?) answers NO — it
  survives with the accounting leg removed, so it does not belong to this bank. It is left as
  candidate ground for `project_mrp` or `project_mrp_sale`.

Candidate ground REJECTED as belonging to a different module or arity, not this bridge:
- Timesheet cost double-counted against a production order's operation cost was kept once (Q012) as
  the one genuine occurrence of that seam; further variants (different task types, different rate
  structures) were found on re-check to restate the same underlying failure event with a noun
  swapped, and were cut per the Bridge Module Rule §4 prohibition on that pattern.
- A production order's own multi-company valuation-account requirement, absent any project task, is
  `mrp_account`'s own ground; only the narrower question of whether the project's own view reflects
  that blocking condition (Q027) was kept.
