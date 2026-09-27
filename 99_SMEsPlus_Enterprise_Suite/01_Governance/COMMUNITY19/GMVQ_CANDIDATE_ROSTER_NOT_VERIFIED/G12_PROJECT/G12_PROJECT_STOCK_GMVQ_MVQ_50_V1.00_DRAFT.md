# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_stock Module MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_STOCK-MVQ50-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `project_stock`
**Wave:** W3
**Author Cell:** P12-4 (GMVQ Question Factory — Production Cell P12-4)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the seam between project management and
physical material/stock consumption. Per the Bridge Module Rule, `project_stock` is a 2-way bridge:
it owns no behaviour of its own beyond making a project's own cost, schedule, and readiness views
agree with what stock actually records as issued, reserved, or returned.

This bank is deliberately silent on any customer-facing sale or delivery, and does not restate the
purchase-side procurement questions (that seam belongs to `project_purchase` and
`project_purchase_stock`). Every question here is about internal material issue/consumption/return
against a project task, independent of how that material was originally acquired, and independent
of any customer order.

Question text is source-neutral: no vendor or product name, no technical identifier, and no
reference to the module's own metadata name.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 50 questions exist because each tests a distinct material hypothesis.
- Pre-authoring check performed: `grep -h HYPOTHESIS` across `G08_SALE_PROJECT_STOCK` (which is
  framed entirely around delivery to a *customer* via an order) and the base `G05_STOCK` bank (pure
  stock, no project) confirmed neither asks about project-task-level internal consumption with no
  customer order in the loop. No overlap found.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G12-PROJECT_STOCK-Q001

```yaml
QID: G12-PROJECT_STOCK-Q001
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Material issued from stock to a specific project task is attributed to that task at the moment of
  issue, not only inferred later from a broader project-level total.
WHY_IT_MATTERS: >
  A task-level attribution inferred only after the fact is unreliable whenever more than one task
  could plausibly have consumed the same material.
DISCONFIRMING_OBSERVATION: >
  Material issued from stock shows only a project-level total immediately after issue, with the
  specific task attribution appearing only later, if at all.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Issue material from stock to a specific project task and inspect the record immediately after
  issue.
```

## G12-PROJECT_STOCK-Q002

```yaml
QID: G12-PROJECT_STOCK-Q002
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The cost recorded against a project for consumed material reflects the stock's own valuation
  method (its costing basis) rather than an independently entered, potentially disagreeing figure.
WHY_IT_MATTERS: >
  An independently entered cost figure that disagrees with the stock's own valuation misstates the
  project's true cost and breaks reconciliation between the two views.
DISCONFIRMING_OBSERVATION: >
  The project's recorded material cost for an item differs from that item's own stock valuation at
  the time of issue, with no documented reason for the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue a valued stock item to a project task and compare the project's recorded cost against the
  item's own stock valuation.
```

## G12-PROJECT_STOCK-Q003

```yaml
QID: G12-PROJECT_STOCK-Q003
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Stock reserved specifically for a project task's planned consumption is visible to other, unrelated
  demands as already committed, not as freely available.
WHY_IT_MATTERS: >
  Stock shown as freely available when it is actually reserved invites an unrelated demand to
  consume material the project is depending on.
DISCONFIRMING_OBSERVATION: >
  Stock already reserved for a project task appears as freely available quantity when an unrelated
  demand checks availability.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve stock for a project task's planned consumption, then check that stock's availability from
  an unrelated demand.
```

## G12-PROJECT_STOCK-Q004

```yaml
QID: G12-PROJECT_STOCK-Q004
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A return of unused material from a project task back to general stock is recorded through one
  documented path, distinct from an ordinary, unrelated stock adjustment.
WHY_IT_MATTERS: >
  Conflating a project return with an ordinary adjustment loses the ability to see how much material
  a project actually consumed versus merely drew and returned.
DISCONFIRMING_OBSERVATION: >
  A return of unused project material is recorded identically to an unrelated stock adjustment, with
  no distinguishing record of it having come from a project task.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Return unused material from a project task to general stock and check whether the return is
  distinguishable from an ordinary adjustment.
```

## G12-PROJECT_STOCK-Q005

```yaml
QID: G12-PROJECT_STOCK-Q005
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where two different project tasks each draw material from the same shared stock location, one
  task's over-consumption does not silently reduce what the system shows as available to the other
  task without a visible flag.
WHY_IT_MATTERS: >
  A silent reduction leaves the second task's planner unaware that material they were counting on
  has already been consumed by a different task.
DISCONFIRMING_OBSERVATION: >
  One task's over-consumption from a shared location reduces the other task's own shown availability
  with no flag indicating why.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Have two project tasks draw from the same shared stock location, push one task's consumption
  beyond its planned share, and check the other task's availability view.
```

## G12-PROJECT_STOCK-Q006

```yaml
QID: G12-PROJECT_STOCK-Q006
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Putting a project on hold after material has already been issued to one of its tasks does not
  silently reclassify that issued material as available again for an unrelated purpose without an
  explicit release action.
WHY_IT_MATTERS: >
  An automatic, silent release of already-issued material lets it be consumed elsewhere while the
  project is merely paused, not cancelled.
DISCONFIRMING_OBSERVATION: >
  Placing the project on hold changes already-issued material's status to available with no explicit
  release action taken.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Put a project on hold after material has already been issued to one of its tasks, and check whether
  that material remains marked as issued.
```

## G12-PROJECT_STOCK-Q007

```yaml
QID: G12-PROJECT_STOCK-Q007
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project task marked complete does not, by itself, retroactively record consumption of material
  that was never actually issued from stock.
WHY_IT_MATTERS: >
  Fabricating consumption from a completion state would let a task appear to have used material it
  never physically received.
DISCONFIRMING_OBSERVATION: >
  Marking a project task complete creates a stock consumption record for material that was never
  actually issued to it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Mark a project task complete without any prior material issue and check whether a consumption
  record is created.
```

## G12-PROJECT_STOCK-Q008

```yaml
QID: G12-PROJECT_STOCK-Q008
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Closing a project while it still holds a stock reservation for a task that was never fulfilled
  either releases that reservation through a documented action or leaves it explicitly flagged rather
  than silently forgotten.
WHY_IT_MATTERS: >
  A forgotten reservation on a closed project permanently ties up stock that could otherwise be used
  elsewhere, with no one aware it is still held.
DISCONFIRMING_OBSERVATION: >
  A project closes with an unfulfilled stock reservation still active, and nothing about the closure
  releases it or flags it.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Close a project that has an unfulfilled stock reservation for one of its tasks, and observe the
  reservation's resulting state.
```

## G12-PROJECT_STOCK-Q009

```yaml
QID: G12-PROJECT_STOCK-Q009
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Duplicating a project to plan a similar future engagement does not cause the duplicate to inherit a
  live reference to material already issued and consumed under the original project.
WHY_IT_MATTERS: >
  A live reference in the duplicate would make a brand-new, unstarted project appear to already have
  consumed material it never actually used.
DISCONFIRMING_OBSERVATION: >
  The duplicated project shows the original project's already-issued and consumed material as its
  own current consumption.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Duplicate a project that already has issued and consumed material, and inspect the duplicate's own
  material state.
```

## G12-PROJECT_STOCK-Q010

```yaml
QID: G12-PROJECT_STOCK-Q010
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A serial- or lot-tracked item issued to a project task remains traceable back to that specific
  project and task even after the project is later restructured.
WHY_IT_MATTERS: >
  Losing traceability after restructuring defeats the purpose of tracked identity exactly when a
  defect or recall investigation would need it.
DISCONFIRMING_OBSERVATION: >
  After a project is restructured, a serial- or lot-tracked item issued before the restructuring can
  no longer be traced back to its original task.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Issue a tracked item to a project task, restructure the project, and check whether the item is
  still traceable to its original task.
```

## G12-PROJECT_STOCK-Q011

```yaml
QID: G12-PROJECT_STOCK-Q011
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two simultaneous issues of material from the same stock location to two different project tasks do
  not result in either task's recorded consumption being lost or overwritten.
WHY_IT_MATTERS: >
  A lost or overwritten consumption record understates one task's true material use and can make
  reported project cost inaccurate.
DISCONFIRMING_OBSERVATION: >
  After two near-simultaneous issues to two different tasks from the same location, one task's
  recorded consumption is missing.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Issue material to two different project tasks from the same stock location at nearly the same
  time, and verify both consumption records persisted.
```

## G12-PROJECT_STOCK-Q012

```yaml
QID: G12-PROJECT_STOCK-Q012
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a project spans more than one physical location, each location's own material issues
  correctly roll up into the project's single overall consumption total rather than one location's
  issues being silently dropped.
WHY_IT_MATTERS: >
  A dropped location's issues understate the project's true total material cost.
DISCONFIRMING_OBSERVATION: >
  Material issued at one of a multi-location project's sites is missing from the project's overall
  consumption total.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Issue material to a project at more than one physical location, and check whether the overall
  consumption total includes all locations.
```

## G12-PROJECT_STOCK-Q013

```yaml
QID: G12-PROJECT_STOCK-Q013
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A negative stock condition arising from issuing more material to a project task than is actually
  on hand is either blocked or produces a visibly exceptional record, not a silent pass-through.
WHY_IT_MATTERS: >
  A silent pass-through into negative stock hides a real shortage that the project's own schedule
  and cost tracking are relying on being accurate.
DISCONFIRMING_OBSERVATION: >
  Issuing more material than is on hand to a project task proceeds with no exceptional flag, leaving
  stock negative with no visible indication.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attempt to issue more material to a project task than is actually on hand, and observe the
  system's response.
```

## G12-PROJECT_STOCK-Q014

```yaml
QID: G12-PROJECT_STOCK-Q014
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Material transferred internally from one project's already-issued stock to a different, unrelated
  project leaves a visible record of that transfer on both projects' histories.
WHY_IT_MATTERS: >
  An untraceable transfer leaves one project's cost overstated for material it never actually kept,
  and the other project's cost understated for what it actually used.
DISCONFIRMING_OBSERVATION: >
  Material transferred between two projects shows no visible transfer record on either project's own
  history.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Transfer already-issued material from one project to a different project, and check both projects'
  histories for the transfer record.
```

## G12-PROJECT_STOCK-Q015

```yaml
QID: G12-PROJECT_STOCK-Q015
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reversing a project's over-issue of material returns that quantity to general available stock
  through a documented, traceable path rather than an unexplained disappearance and reappearance.
WHY_IT_MATTERS: >
  An unexplained reversal makes it impossible to later confirm that the corrected quantity actually
  matches the original over-issue.
DISCONFIRMING_OBSERVATION: >
  Reversing an over-issue changes the project's recorded consumption and the general stock level with
  no traceable link connecting the two changes.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Over-issue material to a project task, reverse the over-issue, and trace the path the reversal took
  back into general stock.
```

## G12-PROJECT_STOCK-Q016

```yaml
QID: G12-PROJECT_STOCK-Q016
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project task's estimated material requirement, once actual stock is issued against it, does not
  silently overwrite the original estimate, keeping estimate and actual separately visible.
WHY_IT_MATTERS: >
  Overwriting the estimate destroys the ability to later compare planned material use against what
  was actually consumed.
DISCONFIRMING_OBSERVATION: >
  After actual stock is issued against a task, its originally recorded material estimate can no
  longer be viewed separately from the actual issued quantity.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Record a task's material estimate, issue actual stock against it, and check whether the original
  estimate remains separately viewable.
```

## G12-PROJECT_STOCK-Q017

```yaml
QID: G12-PROJECT_STOCK-Q017
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a project's task depends on a stock location that is later archived or deactivated, any
  still-pending reservation against that location is flagged rather than silently lost.
WHY_IT_MATTERS: >
  A silently lost reservation leaves the task's planner unaware their planned material source no
  longer exists.
DISCONFIRMING_OBSERVATION: >
  A stock location holding a pending project reservation is archived, and the reservation
  disappears with no flag or notice.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Archive a stock location that holds a pending reservation for a project task, and check whether the
  reservation is flagged.
```

## G12-PROJECT_STOCK-Q018

```yaml
QID: G12-PROJECT_STOCK-Q018
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A project archived with an unresolved stock discrepancy (issued quantity disagreeing with what the
  task's records show as received) retains that discrepancy as visible, unresolved history rather
  than the archival implicitly closing it out.
WHY_IT_MATTERS: >
  Implicitly closing out an unresolved discrepancy through archival lets a genuine shortage or
  over-issue quietly disappear from view.
DISCONFIRMING_OBSERVATION: >
  A project is archived while an unresolved stock discrepancy exists on one of its tasks, and the
  discrepancy no longer appears as open, unresolved history.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Archive a project that has an unresolved stock discrepancy on one of its tasks, and check whether
  the discrepancy remains visible.
```

## G12-PROJECT_STOCK-Q019

```yaml
QID: G12-PROJECT_STOCK-Q019
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The valuation method used to cost material issued to a project (for example, whether cost reflects
  the specific batch consumed or an averaged figure) is applied consistently across every report
  showing the project's material cost, not one method in one report and a different one elsewhere.
WHY_IT_MATTERS: >
  An inconsistent valuation method across reports produces two different cost figures for the same
  physical consumption, undermining trust in either report.
DISCONFIRMING_OBSERVATION: >
  Two different reports of the same project's material cost apply two different valuation methods to
  the same consumed items.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Pull a project's material cost from two different reports for the same consumed items and compare
  the valuation method each applies.
```

## G12-PROJECT_STOCK-Q020

```yaml
QID: G12-PROJECT_STOCK-Q020
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project template applied to create a new project does not carry forward a live reference to
  material actually issued and consumed under the original project the template was derived from.
WHY_IT_MATTERS: >
  A live reference in a template-created project would make a brand-new engagement appear to already
  have consumed material from an entirely unrelated, earlier project.
DISCONFIRMING_OBSERVATION: >
  A project created from a template shows the template's source project's already-consumed material
  as its own current consumption.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a template from a project with already-consumed material, apply the template to create a
  new project, and inspect the new project's material references.
```

## G12-PROJECT_STOCK-Q021

```yaml
QID: G12-PROJECT_STOCK-Q021
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a stock item issued to a project task is tracked by expiry date, an item nearing or past its
  expiry is flagged at the point of issue to the project rather than issued indistinguishably from
  unexpired stock.
WHY_IT_MATTERS: >
  Issuing expired or near-expired material indistinguishably risks the project unknowingly using
  material that is no longer fit for its purpose.
DISCONFIRMING_OBSERVATION: >
  An expiry-tracked item past its expiry is issued to a project task with no flag distinguishing it
  from unexpired stock.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Issue an expiry-tracked item at or past its expiry date to a project task, and check whether the
  issue is flagged.
```

## G12-PROJECT_STOCK-Q022

```yaml
QID: G12-PROJECT_STOCK-Q022
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Someone with permission to view a project's overall cost report but no permission over stock
  valuation does not see the underlying per-unit stock cost through the project's material cost
  figure alone.
WHY_IT_MATTERS: >
  Per-unit stock cost is commercially sensitive; leaking it through a project view never meant to
  expose it undermines pricing confidentiality.
DISCONFIRMING_OBSERVATION: >
  A user with project-cost-only access can see a specific item's per-unit stock cost by navigating
  through the project's own material cost breakdown.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  As a user with project cost-view access only, attempt to see an item's per-unit stock cost through
  the project's own cost breakdown.
```

## G12-PROJECT_STOCK-Q023

```yaml
QID: G12-PROJECT_STOCK-Q023
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project task's material consumption, once logged, is distinguishable in reporting from material
  that has merely been reserved for the task but not yet actually issued.
WHY_IT_MATTERS: >
  Conflating reserved with consumed overstates the task's true progress and can trigger a premature
  completion or billing claim.
DISCONFIRMING_OBSERVATION: >
  Material merely reserved for a task, but not yet issued, appears identically to actually consumed
  material in the project's reporting.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve material for a task without issuing it, and compare its appearance in reporting against
  material that has actually been issued and consumed.
```

## G12-PROJECT_STOCK-Q024

```yaml
QID: G12-PROJECT_STOCK-Q024
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Merging two project tasks that each already have material issued against them combines the
  recorded consumption of both without silently losing either task's original figure.
WHY_IT_MATTERS: >
  Losing one task's original consumption figure during a merge understates the true combined
  material cost of the resulting task.
DISCONFIRMING_OBSERVATION: >
  After merging two tasks that each had material issued, the resulting task's consumption total is
  less than the sum of the two original figures.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Merge two project tasks that each already have recorded material consumption, and sum the
  resulting task's total against the two original figures.
```

## G12-PROJECT_STOCK-Q025

```yaml
QID: G12-PROJECT_STOCK-Q025
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A stock item issued to a project task under one company, in a multi-company setup where the
  project itself belongs to a different company, follows a documented inter-company step before that
  cost is attributed to the project.
WHY_IT_MATTERS: >
  Attributing cross-company cost without the required inter-company step misstates each company's own
  books and the boundary between them.
DISCONFIRMING_OBSERVATION: >
  Stock issued under one company entity appears as project cost on a different company's project
  with no intercompany step having occurred.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Issue stock under one company entity to a project owned by a different entity, and trace whether an
  intercompany step is required before cost is attributed.
```

## G12-PROJECT_STOCK-Q026

```yaml
QID: G12-PROJECT_STOCK-Q026
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a project's material need is fulfilled from more than one stock location due to a shortage at
  the primary location, the task's consumption record correctly reflects the combination rather than
  showing only the first location's contribution.
WHY_IT_MATTERS: >
  Showing only the first location's contribution understates the task's true total material
  consumption and cost.
DISCONFIRMING_OBSERVATION: >
  A task fulfilled from two stock locations shows a consumption record reflecting only the first
  location's issue.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Fulfil a task's material need from two different stock locations due to a shortage at the primary
  one, and check the task's overall consumption record.
```

## G12-PROJECT_STOCK-Q027

```yaml
QID: G12-PROJECT_STOCK-Q027
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A quality or inspection hold placed on stock earmarked for a project task blocks the project's own
  indication that the material is ready for use.
WHY_IT_MATTERS: >
  A project team unaware of a quality hold may proceed to use material that has not actually cleared
  inspection.
DISCONFIRMING_OBSERVATION: >
  Stock under an active quality hold is shown by the project's own readiness view as ready for use.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Place a quality hold on stock earmarked for a project task, and check the task's readiness
  indicator.
```

## G12-PROJECT_STOCK-Q028

```yaml
QID: G12-PROJECT_STOCK-Q028
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Damaged material discovered at a project site after issue but before being logged as consumed is
  attributed to a single documented cause path distinguishing it from material that was actually
  used.
WHY_IT_MATTERS: >
  Without a documented cause path, damaged-but-unused material can be indistinguishably counted as
  consumed, overstating the project's true material usage.
DISCONFIRMING_OBSERVATION: >
  Material damaged after issue but before use is recorded identically to material that was actually
  consumed, with no distinguishing cause path.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record material as damaged at a project site after issue but before being logged as consumed, and
  check how it is distinguished from actually-used material.
```

## G12-PROJECT_STOCK-Q029

```yaml
QID: G12-PROJECT_STOCK-Q029
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Confirming a project task's material consumption while another user simultaneously reverses that
  same task's earlier reservation resolves to one consistent, recorded outcome rather than an
  unrecorded race.
WHY_IT_MATTERS: >
  An unrecorded race between confirming consumption and reversing a reservation leaves the system in
  a state neither user actually intended.
DISCONFIRMING_OBSERVATION: >
  Simultaneously confirming consumption and reversing the same task's reservation produces an
  outcome neither action alone would predict, with no record of how it was resolved.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Simulate confirming a task's material consumption at the same moment another user reverses that
  task's earlier reservation, and observe the resulting state.
```

## G12-PROJECT_STOCK-Q030

```yaml
QID: G12-PROJECT_STOCK-Q030
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A project's reported material cost, calculated while some issued stock is still pending valuation
  (for example, awaiting a landed-cost adjustment), is distinguishable from the same figure once
  valuation is finalized.
WHY_IT_MATTERS: >
  An indistinguishable provisional figure can be mistaken for a confirmed, final cost, misleading
  anyone relying on it for a decision.
DISCONFIRMING_OBSERVATION: >
  The project's reported material cost looks identical whether or not pending valuation for some of
  its issued stock has actually finalized.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Compare a project's reported material cost while a valuation adjustment is still pending against
  the same figure once the adjustment finalizes.
```

## G12-PROJECT_STOCK-Q031

```yaml
QID: G12-PROJECT_STOCK-Q031
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reopening a closed project to record a late stock adjustment against one of its already-completed
  tasks is a recorded action — who reopened it and when — rather than an unaudited change.
WHY_IT_MATTERS: >
  An unaudited reopening of a closed project undermines closure as a control checkpoint and hides
  who decided to revisit it.
DISCONFIRMING_OBSERVATION: >
  A closed project is reopened to record a late stock adjustment, and no audit entry shows who
  reopened it or when.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Reopen a closed project to record a late stock adjustment against one of its tasks, and check the
  audit trail.
```

## G12-PROJECT_STOCK-Q032

```yaml
QID: G12-PROJECT_STOCK-Q032
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where one physical batch of material is issued across more than one project, each project's own
  consumption record attributes only its own portion, not the batch's full quantity.
WHY_IT_MATTERS: >
  Attributing the full batch quantity to more than one project overstates the true combined material
  cost across those projects.
DISCONFIRMING_OBSERVATION: >
  Two projects sharing one issued batch each show the batch's full quantity in their own consumption
  record.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Issue one physical batch of material split across two different projects, and check each
  project's own recorded consumption quantity.
```

## G12-PROJECT_STOCK-Q033

```yaml
QID: G12-PROJECT_STOCK-Q033
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A project's task-level material budget being exceeded by an issue produces one documented,
  consistent system behaviour (block, warn, or flag) rather than varying case to case.
WHY_IT_MATTERS: >
  An inconsistent response to breaching a task-level material budget makes the control's effect
  depend on unrelated factors rather than the actual breach.
DISCONFIRMING_OBSERVATION: >
  Two comparable material issues that each breach their task's own budget by a similar margin
  produce two different system responses with no documented reason for the difference.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Issue material breaching a task's own material budget in two comparable cases, and compare the
  resulting system behaviour.
```

## G12-PROJECT_STOCK-Q034

```yaml
QID: G12-PROJECT_STOCK-Q034
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An emergency reallocation that pulls stock already reserved for one project task to cover an
  unrelated urgent need elsewhere results in a visible change to that project task's own
  material-readiness indicator.
WHY_IT_MATTERS: >
  A reallocation with no visible change to the losing task's readiness leaves that task falsely
  believing it still has material it no longer holds.
DISCONFIRMING_OBSERVATION: >
  Stock reserved for a project task is reallocated elsewhere and the task's own readiness indicator
  shows no resulting change.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Reallocate stock already reserved for a project task to cover an unrelated urgent need, and check
  the task's readiness indicator afterward.
```

## G12-PROJECT_STOCK-Q035

```yaml
QID: G12-PROJECT_STOCK-Q035
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a project's task requires a specific stock location (such as a job site) rather than the
  general warehouse, material issued to the wrong location is either blocked or recorded as an
  explicit exception.
WHY_IT_MATTERS: >
  Material silently issued to the wrong location can leave a project site without material it
  actually needs while the system believes the need is met.
DISCONFIRMING_OBSERVATION: >
  Material issued to a location other than the task's own specified site proceeds with no block or
  exception record.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Issue material to a location different from a project task's own specified site, and observe
  whether the system blocks or flags it.
```

## G12-PROJECT_STOCK-Q036

```yaml
QID: G12-PROJECT_STOCK-Q036
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A stock item's unit of measure conversion, when the unit used for a project task's planned
  requirement differs from the unit used at actual issue, is applied identically at both points
  rather than two independently derived conversions producing different physical quantities.
WHY_IT_MATTERS: >
  Two independently derived conversions can make the task's plan and its actual issue disagree on
  the true physical quantity, even when both sides believe they match.
DISCONFIRMING_OBSERVATION: >
  The same nominal quantity converts to two different physical amounts depending on whether it is
  read from the task's planned requirement or from the actual issue record.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Plan a task's material requirement in one unit and issue the actual material in a different unit,
  then compare the converted physical quantities on both sides.
```

## G12-PROJECT_STOCK-Q037

```yaml
QID: G12-PROJECT_STOCK-Q037
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A project's total material cost report and a separate warehouse-level consumption report, both
  claiming to reflect the same project's actual usage, reconcile to a single documented source or
  their difference is explained.
WHY_IT_MATTERS: >
  Two disagreeing figures for the same actual usage, with no documented reason, leaves neither
  report trustworthy.
DISCONFIRMING_OBSERVATION: >
  The project's own material cost report and a warehouse-level consumption report show different
  totals for the same project with no documented explanation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Pull a project's material cost total from the project's own report and from a warehouse-level
  consumption report, and compare the two.
```

## G12-PROJECT_STOCK-Q038

```yaml
QID: G12-PROJECT_STOCK-Q038
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling a project task after material has already been issued to it results in that material
  being flagged for return or reallocation rather than remaining an unexplained, orphaned issue.
WHY_IT_MATTERS: >
  An unflagged, orphaned issue is material already taken out of stock that no longer serves any
  documented purpose.
DISCONFIRMING_OBSERVATION: >
  A project task is cancelled after material was already issued to it, and no flag or prompt appears
  against the now-unused material.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a project task after material has already been issued to it, and check whether the material
  is flagged.
```

## G12-PROJECT_STOCK-Q039

```yaml
QID: G12-PROJECT_STOCK-Q039
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project's currency-neutral, unit-based material record does not create a disagreeing cost figure
  when converted into the project's own reporting currency compared to how the same conversion is
  applied elsewhere in the project's cost report.
WHY_IT_MATTERS: >
  Two different currency conversions of the same unit-based record produce two different reported
  costs for what should be a single, fixed quantity.
DISCONFIRMING_OBSERVATION: >
  The same unit-based material record converts to two different currency figures in two different
  places within the project's own cost report.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Convert a project's unit-based material record into its reporting currency in two different report
  views and compare the figures.
```

## G12-PROJECT_STOCK-Q040

```yaml
QID: G12-PROJECT_STOCK-Q040
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Splitting a project task into two separate tasks after material has already been issued against the
  original correctly attributes the already-issued quantity to one, clearly documented, resulting
  task rather than leaving it ambiguous between the two.
WHY_IT_MATTERS: >
  An ambiguous attribution after a split makes it impossible to know which resulting task's cost
  actually includes the previously issued material.
DISCONFIRMING_OBSERVATION: >
  After a task is split, the previously issued material's attribution between the two resulting
  tasks is unclear or unresolved.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Issue material to a task, split the task into two, and check which resulting task the already-
  issued material is attributed to.
```

## G12-PROJECT_STOCK-Q041

```yaml
QID: G12-PROJECT_STOCK-Q041
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a project's task consumption is logged through an automated, no-human-review background
  process (such as a scheduled stock count reconciliation), it is subject to the same task-
  attribution rule as a manually logged issue.
WHY_IT_MATTERS: >
  An automated path exempted from the attribution rule becomes an unmonitored route for consumption
  to be misattributed or attributed to no task at all.
DISCONFIRMING_OBSERVATION: >
  Consumption logged through an automated background process lacks the task-level attribution that
  a manually logged issue would have required.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a background reconciliation process that logs project consumption, and compare its
  resulting attribution against a manually logged issue.
```

## G12-PROJECT_STOCK-Q042

```yaml
QID: G12-PROJECT_STOCK-Q042
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A stock item substituted for the one originally planned for a project task, due to a shortage of
  the original, is flagged on the project's material record as a substitution rather than silently
  treated as satisfying the original planned item.
WHY_IT_MATTERS: >
  An unflagged substitution can leave a project task proceeding with a different item than what its
  own plan or specification actually required.
DISCONFIRMING_OBSERVATION: >
  A substitute item issued to a project task is shown in the project's material record as if the
  originally planned item had been used, with no substitution flag.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Issue a substitute item in place of the originally planned one to a project task, and check the
  project's material record for a substitution flag.
```

## G12-PROJECT_STOCK-Q043

```yaml
QID: G12-PROJECT_STOCK-Q043
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An unrelated administrative action elsewhere in the system (merging stock locations, mass
  adjustments) does not silently change a project task's already-recorded consumption without a
  distinct, traceable action explaining the change.
WHY_IT_MATTERS: >
  An untraceable change from an unrelated administrative action makes it impossible to later explain
  why a project's material record no longer matches what was originally recorded.
DISCONFIRMING_OBSERVATION: >
  A mass adjustment or location merge unrelated to a specific project changes that project's already-
  recorded consumption with no distinct, traceable explanation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform an administrative mass adjustment or location merge affecting stock a project has already
  consumed, and check whether the project's consumption record changed and whether it is traceable.
```

## G12-PROJECT_STOCK-Q044

```yaml
QID: G12-PROJECT_STOCK-Q044
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a project is renamed or its reference renumbered after material has already been issued
  against it, the stock-side historical record updates its display reference rather than showing a
  stale label.
WHY_IT_MATTERS: >
  A stale label on a stock-side historical record confuses anyone trying to cross-reference it
  against the project's current identity.
DISCONFIRMING_OBSERVATION: >
  After the project is renamed, its stock-side historical consumption records still display the
  project's old name or number.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Rename a project that has already-issued material recorded against it, and check the reference
  shown on the stock-side historical record.
```

## G12-PROJECT_STOCK-Q045

```yaml
QID: G12-PROJECT_STOCK-Q045
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A project's task marked as no longer needing further material, after some has already been issued,
  still permits an explicit return of any unused portion rather than trapping it as consumed by
  default.
WHY_IT_MATTERS: >
  Trapping unused material as consumed by default overstates the task's true cost and loses reusable
  stock that could serve another need.
DISCONFIRMING_OBSERVATION: >
  Marking a task as needing no further material makes any already-issued but unused portion
  unreturnable, recorded as consumed by default.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Mark a task as no longer needing further material while some issued material remains unused, and
  attempt to return the unused portion.
```

## G12-PROJECT_STOCK-Q046

```yaml
QID: G12-PROJECT_STOCK-Q046
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two projects sharing one common, pooled stock allocation (rather than each having its own
  dedicated stock) have their respective consumption from that pool separately and correctly
  attributed rather than merged into one undifferentiated draw.
WHY_IT_MATTERS: >
  A merged, undifferentiated draw makes it impossible to know how much of a shared pool each project
  actually consumed.
DISCONFIRMING_OBSERVATION: >
  Two projects drawing from one shared pooled allocation show one combined consumption figure with
  no attribution split between them.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have two projects draw from one shared, pooled stock allocation, and check whether their
  respective consumption is separately attributed.
```

## G12-PROJECT_STOCK-Q047

```yaml
QID: G12-PROJECT_STOCK-Q047
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A backorder on material needed by a project task, where the shortfall is only discovered at the
  moment of attempted issue, produces a visible schedule-risk indicator on the project rather than
  only a silent stock-shortage note with no project-level visibility.
WHY_IT_MATTERS: >
  Confining the shortage signal to the stock side leaves the project team unaware their own schedule
  is now at risk.
DISCONFIRMING_OBSERVATION: >
  A material shortage discovered at the moment of attempted issue produces a stock-side note but no
  corresponding schedule-risk indicator on the project.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attempt to issue material to a project task where a shortage is only discovered at that moment,
  and check both the stock-side note and the project's own schedule view.
```

## G12-PROJECT_STOCK-Q048

```yaml
QID: G12-PROJECT_STOCK-Q048
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Deleting a project outright, where deletion is distinct from archiving, does not leave already-
  issued material's historical stock records pointing at a reference with no explanation that the
  originating project is gone.
WHY_IT_MATTERS: >
  A broken, unexplained reference in a stock-side historical record makes it impossible for a later
  reviewer to understand what the missing project originally was.
DISCONFIRMING_OBSERVATION: >
  A stock-side historical record references a project that has been outright deleted, with no
  indication of what happened to it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Where outright deletion of a project is permitted, delete one with already-issued material history,
  and inspect the stock-side record afterward.
```

## G12-PROJECT_STOCK-Q049

```yaml
QID: G12-PROJECT_STOCK-Q049
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project's material consumption recorded against a task that is later found to have been the
  wrong task (a data-entry mismatch) is correctable through a distinct, traceable adjustment rather
  than silently overwriting the original entry with no trace.
WHY_IT_MATTERS: >
  Silently overwriting a mismatched entry destroys the ability to later explain why a task's cost
  history changed.
DISCONFIRMING_OBSERVATION: >
  Correcting a consumption entry recorded against the wrong task overwrites the original entry with
  no trace of the correction having occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record consumption against the wrong task by mistake, correct the attribution, and check whether
  the original entry remains traceable.
```

## G12-PROJECT_STOCK-Q050

```yaml
QID: G12-PROJECT_STOCK-Q050
MODULE: project_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a project draws material through more than one sequential phase, stock reserved for a later
  phase is visible to an earlier phase's own consumption view as committed-but-not-available, not as
  freely usable ahead of schedule.
WHY_IT_MATTERS: >
  An earlier phase freely consuming a later phase's reserved stock can leave the later phase short of
  material it was specifically counting on.
DISCONFIRMING_OBSERVATION: >
  An earlier phase's consumption view shows a later phase's reserved stock as freely usable rather
  than committed-but-not-available.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve stock for a later project phase, and check whether an earlier phase's own consumption view
  treats that stock as freely usable.
```
