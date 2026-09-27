# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_mrp Module MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_MRP-MVQ48-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `project_mrp`
**Module Class:** 2-way bridge (project management + manufacturing) — seam-only per
`GMVQ_BRIDGE_MODULE_RULE_V1.00`
**Wave:** W3
**Author Cell:** P12-2 (GMVQ Question Factory — Production Cell P12-2)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the seam between project management and
manufacturing: what happens when a manufacturing/production activity is linked to a project task
for cost, quantity, schedule, and traceability purposes. Per the Bridge Module Rule and the Group
G12 brief, `project_mrp` is treated as a 2-way bridge — questions belonging to `project` alone or to
manufacturing alone were cut before authoring using the removal-of-capability test.

Duplicate-risk note: this bank deliberately does not re-ask the "project+X+account" cost-allocation
pattern already covered from a different angle in `project_mrp_account` / `project_stock_account` /
`sale_project_stock_account` (G08) once those exist; where a cost question appears here it is tied
specifically to what manufacturing itself contributes (production execution, component consumption,
scrap/rework), not to accounting valuation as such.

## Control

- Bridge seam test applied to every question: removal-of-capability test per
  `GMVQ_BRIDGE_MODULE_RULE_V1.00` section 2.
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because each tests a distinct material seam hypothesis, spread
  across ordering, partiality, ownership, timing, reversal, quantity/money, lifecycle mismatch,
  error asymmetry, authority, and concurrency.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G12-PROJECT_MRP-Q001

```yaml
QID: G12-PROJECT_MRP-Q001
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a manufacturing order linked to a project task is cancelled after component consumption has
  already been recorded against it, the cost already attributed to the project is reversed or
  clearly flagged, not left standing as if production had completed normally.
WHY_IT_MATTERS: >
  A cancelled production run that still leaves its cost sitting on the project overstates that
  project's true cost with no way to tell the figure is stale.
DISCONFIRMING_OBSERVATION: >
  After a linked manufacturing order is cancelled following partial component consumption, the
  project's cost still shows the consumption-based cost with no reversal or flag.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Link a manufacturing order to a project task, record partial component consumption, cancel the
  order, and inspect the project's cost record.
```

## G12-PROJECT_MRP-Q002

```yaml
QID: G12-PROJECT_MRP-Q002
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a linked manufacturing order's completion event arrives after the project task's own status
  was already independently advanced to done, the resulting state is an explicit, resolvable
  conflict rather than two silently disagreeing statuses.
WHY_IT_MATTERS: >
  A task marked done while production is still open, or vice versa, with nothing reconciling the two,
  leaves the true progress of the work unknowable from either side alone.
DISCONFIRMING_OBSERVATION: >
  A project task shows as complete while its linked manufacturing order is still open, with no
  indication anywhere that the two disagree.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Mark a project task done while its linked manufacturing order is still in progress, and inspect
  whether the disagreement is surfaced.
```

## G12-PROJECT_MRP-Q003

```yaml
QID: G12-PROJECT_MRP-Q003
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A partial production quantity against a manufacturing order linked to a project task is reflected
  as partial progress on that task, not rounded up to a false appearance of full completion.
WHY_IT_MATTERS: >
  Reporting a partially produced deliverable as fully done misleads whoever relies on the project
  view to judge real progress.
DISCONFIRMING_OBSERVATION: >
  A manufacturing order that produced less than its full planned quantity results in the linked
  project task appearing fully complete.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Complete a manufacturing order at less than its full planned quantity and inspect the linked
  project task's reported progress.
```

## G12-PROJECT_MRP-Q004

```yaml
QID: G12-PROJECT_MRP-Q004
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where both a manufacturing view and a project view report the cost of a production run tied to a
  project task, one of the two is documented as the authoritative source, so the two are not left as
  equally-valid figures that can silently disagree.
WHY_IT_MATTERS: >
  Two systems each claiming to be the true cost of the same activity, with no stated authority
  between them, means any disagreement can never be resolved by rule.
DISCONFIRMING_OBSERVATION: >
  The manufacturing-side cost and the project-side cost for the same production run disagree, and
  no documented rule identifies which one governs.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Produce against a manufacturing order linked to a project task and compare the cost as shown in
  the manufacturing view against the cost as shown in the project view.
```

## G12-PROJECT_MRP-Q005

```yaml
QID: G12-PROJECT_MRP-Q005
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the final cost of a production run is only settled after a customer has already been billed
  based on an earlier estimate, the difference triggers a defined reconciling action rather than
  silently vanishing.
WHY_IT_MATTERS: >
  A customer billed on an estimate that later proves wrong, with the gap never reconciled, is either
  an under-recovery the business absorbs unnoticed or an over-charge that damages trust.
DISCONFIRMING_OBSERVATION: >
  A production cost finalized after customer billing differs from the amount billed, with no
  reconciling entry, credit, or follow-up charge recorded.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Bill a customer for a project deliverable based on an estimated production cost, then finalize the
  actual production cost and inspect whether any reconciling action follows.
```

## G12-PROJECT_MRP-Q006

```yaml
QID: G12-PROJECT_MRP-Q006
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where manufacturing quantities and project cost reporting use different units of measure, the
  conversion applied is consistent and documented, not silently variable between two views of the
  same production run.
WHY_IT_MATTERS: >
  An undocumented unit conversion is a common, easy-to-miss source of a materially wrong cost figure.
DISCONFIRMING_OBSERVATION: >
  The same production quantity converts to different project-reported figures across two views with
  no documented reason for the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Produce a quantity under a unit of measure different from the project's own reporting unit and
  compare the converted figures across two views.
```

## G12-PROJECT_MRP-Q007

```yaml
QID: G12-PROJECT_MRP-Q007
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A project that is archived or closed while a linked manufacturing order remains open produces an
  explicit exception or warning, rather than each side proceeding as if the other did not exist.
WHY_IT_MATTERS: >
  A production run left running with no connection to a project that no longer considers itself
  active loses the very reason the link existed.
DISCONFIRMING_OBSERVATION: >
  A project is archived or closed while its linked manufacturing order remains open, with no warning
  or exception surfaced on either side.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Archive or close a project task while its linked manufacturing order is still open, and observe
  whether either side flags the mismatch.
```

## G12-PROJECT_MRP-Q008

```yaml
QID: G12-PROJECT_MRP-Q008
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting a project task that has an in-progress manufacturing order linked to it is prevented, or
  the manufacturing order is explicitly re-flagged as unlinked, rather than left silently pointing at
  a task that no longer exists.
WHY_IT_MATTERS: >
  An orphaned manufacturing order with no visible connection to any project loses its business
  justification and its cost destination at the same time.
DISCONFIRMING_OBSERVATION: >
  Deleting a project task with an in-progress linked manufacturing order succeeds with no warning
  and leaves the order referencing a task that no longer exists.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to delete a project task that has an in-progress linked manufacturing order.
```

## G12-PROJECT_MRP-Q009

```yaml
QID: G12-PROJECT_MRP-Q009
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the bill of components for an item changes between the time a project task requests
  production and the time production actually executes, which version was actually used is
  determinable afterward.
WHY_IT_MATTERS: >
  Not knowing which component list actually governed a production run tied to a project makes any
  later cost or quality investigation impossible to ground in fact.
DISCONFIRMING_OBSERVATION: >
  After a component-list revision between request and execution, there is no way to determine which
  version actually governed the production run linked to the project task.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Revise an item's component list after a project task requests production of it but before
  production executes, then attempt to determine which version was used.
```

## G12-PROJECT_MRP-Q010

```yaml
QID: G12-PROJECT_MRP-Q010
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Component prices that fluctuate between when a manufacturing order is created for a project task
  and when consumption actually happens are captured at a single, defined point (order time or
  consumption time), not an inconsistent mix.
WHY_IT_MATTERS: >
  An inconsistent pricing point for the same category of cost makes project cost comparisons across
  similar tasks unreliable.
DISCONFIRMING_OBSERVATION: >
  Two otherwise comparable production runs linked to project tasks capture component cost at
  different points in time with no documented rule for which point governs.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Vary a component's price between order creation and consumption for two comparable production
  runs linked to project tasks, and compare which price point each actually used.
```

## G12-PROJECT_MRP-Q011

```yaml
QID: G12-PROJECT_MRP-Q011
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The method used to allocate manufacturing overhead or labor cost onto a project's cost view is
  documented and consistent, not an unstated default that differs by project without explanation.
WHY_IT_MATTERS: >
  An unexplained overhead allocation method undermines the credibility of any project margin figure
  built on top of it.
DISCONFIRMING_OBSERVATION: >
  Two comparable projects with linked manufacturing show different overhead or labor allocation
  outcomes with no documented method explaining the difference.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Compare the overhead/labor cost allocated to two comparable projects that each have a linked
  manufacturing order.
```

## G12-PROJECT_MRP-Q012

```yaml
QID: G12-PROJECT_MRP-Q012
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Triggering a manufacturing order from within a project view is subject to a permission distinct
  from the general permission to edit a project task, rather than bundled into ordinary task-editing
  rights.
WHY_IT_MATTERS: >
  Bundling manufacturing-triggering rights into general project editing lets anyone who can update a
  task also commit real production cost and resources.
DISCONFIRMING_OBSERVATION: >
  An account with general project task edit rights, but no distinct manufacturing-trigger grant, is
  still able to create a manufacturing order from a project task.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  From an account with general task-edit rights but no distinct manufacturing-trigger grant, attempt
  to create a manufacturing order from a project task.
```

## G12-PROJECT_MRP-Q013

```yaml
QID: G12-PROJECT_MRP-Q013
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Multiple manufacturing orders linked to the same project task have their quantities and costs
  aggregated into that task's totals through a defined rule, not left as a set of disconnected
  figures the viewer must sum manually.
WHY_IT_MATTERS: >
  A task that requires manual reconstruction of its own true cost from several separate records
  invites both error and delay in every review.
DISCONFIRMING_OBSERVATION: >
  A project task with two or more linked manufacturing orders shows no combined quantity or cost
  figure, only separate, unaggregated records.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Link two manufacturing orders to the same project task and inspect whether their quantities and
  costs are aggregated on the task.
```

## G12-PROJECT_MRP-Q014

```yaml
QID: G12-PROJECT_MRP-Q014
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A manufacturing order for a produced item that ends up used across multiple, unrelated project
  tasks records that shared use explicitly, rather than each task claiming exclusive credit for the
  same production.
WHY_IT_MATTERS: >
  Two unrelated tasks each silently claiming the full cost or output of one production run overstates
  total project cost or output across the business.
DISCONFIRMING_OBSERVATION: >
  The full quantity or cost of a single manufacturing order appears attributed in full to more than
  one project task with no indication the source is shared.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Link the output of a single manufacturing order to more than one project task and inspect how
  quantity and cost are attributed to each.
```

## G12-PROJECT_MRP-Q015

```yaml
QID: G12-PROJECT_MRP-Q015
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Scrap or material loss recorded during a manufacturing order linked to a project task is reflected
  as an identifiable increase in that task's cost, not absorbed silently into an unexplained total.
WHY_IT_MATTERS: >
  Hidden scrap cost prevents a project manager from ever identifying that inefficiency is where their
  budget is actually going.
DISCONFIRMING_OBSERVATION: >
  Scrap recorded during a linked manufacturing order does not appear as a distinguishable component
  of the project task's reported cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record scrap during a manufacturing order linked to a project task and inspect whether it is
  identifiable in the task's cost breakdown.
```

## G12-PROJECT_MRP-Q016

```yaml
QID: G12-PROJECT_MRP-Q016
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rework loop following a failed quality check on a manufacturing order linked to a project task is
  visible on the project side as a distinct delay event, not hidden inside an eventual on-time
  completion.
WHY_IT_MATTERS: >
  A project view that hides rework makes recurring quality problems invisible to the people who plan
  around delivery timing.
DISCONFIRMING_OBSERVATION: >
  A production run that required rework after a failed quality check shows on the project task as if
  it completed without incident, with no visible delay or rework record.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Trigger a quality failure and rework cycle on a manufacturing order linked to a project task, then
  inspect the task's record for any indication of the rework.
```

## G12-PROJECT_MRP-Q017

```yaml
QID: G12-PROJECT_MRP-Q017
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Rescheduling a manufacturing order linked to a project task does not silently move the task's own
  due date without an explicit, visible action or notification.
WHY_IT_MATTERS: >
  A task deadline that moves on its own because production was rescheduled removes the project
  manager's ability to independently judge and communicate real delivery risk.
DISCONFIRMING_OBSERVATION: >
  Rescheduling a linked manufacturing order changes the project task's due date with no visible
  notification or explicit confirming action.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Reschedule a manufacturing order linked to a project task and observe whether the task's due date
  changes and whether that change is flagged.
```

## G12-PROJECT_MRP-Q018

```yaml
QID: G12-PROJECT_MRP-Q018
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A component shortage delaying a manufacturing order linked to a project task is surfaced as a
  visible risk on the project side, not confined to a manufacturing-only view the project team never
  sees.
WHY_IT_MATTERS: >
  A project team unaware of a shortage-driven delay cannot manage customer expectations or
  reprioritize until it is too late.
DISCONFIRMING_OBSERVATION: >
  A component shortage delaying a linked manufacturing order produces no visible risk indicator
  anywhere in the project task's own view.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a component shortage that delays a manufacturing order linked to a project task and inspect
  the project task's view for any risk indication.
```

## G12-PROJECT_MRP-Q019

```yaml
QID: G12-PROJECT_MRP-Q019
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where production for a project task occurs in a different company or facility than the project
  itself belongs to, cost and quantity data cross that boundary only through an explicit,
  authorized step, not implicitly.
WHY_IT_MATTERS: >
  An implicit cross-company data flow for cost and inventory information is exactly the kind of
  boundary failure multi-tenant and multi-company controls exist to prevent.
DISCONFIRMING_OBSERVATION: >
  Production data from a manufacturing order in one company context appears attributed to a project
  in a different company context with no explicit cross-company authorization recorded.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Link a project task in one company context to a manufacturing order executed in a different
  company context and inspect how the data crosses that boundary.
```

## G12-PROJECT_MRP-Q020

```yaml
QID: G12-PROJECT_MRP-Q020
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a project task is marked billable to a customer, manufacturing cost linked to it does not
  automatically flow onto a customer invoice without an explicit action confirming it should be
  billed.
WHY_IT_MATTERS: >
  Automatically billing raw production cost to a customer without a confirming step risks exposing
  internal cost detail or billing amounts nobody actually reviewed.
DISCONFIRMING_OBSERVATION: >
  Manufacturing cost linked to a billable project task appears on a customer invoice with no
  intervening confirmation step.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Mark a project task billable, link a manufacturing order to it, and observe whether its cost
  reaches a customer invoice without a separate confirming action.
```

## G12-PROJECT_MRP-Q021

```yaml
QID: G12-PROJECT_MRP-Q021
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Internal manufacturing detail (such as component-level cost or production scheduling) linked to a
  project task is not exposed to an external customer or portal view of that project by default.
WHY_IT_MATTERS: >
  Internal cost structure and production scheduling detail is commercially sensitive information
  that should not leak to a customer through a project view designed for status, not cost detail.
DISCONFIRMING_OBSERVATION: >
  A customer-facing or portal view of a project task exposes component-level manufacturing cost or
  detailed production scheduling information.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Link a manufacturing order to a project task and inspect exactly what manufacturing detail is
  visible through any external or portal-facing view of that task.
```

## G12-PROJECT_MRP-Q022

```yaml
QID: G12-PROJECT_MRP-Q022
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The complete chain from a project task's production request through the manufacturing order,
  component consumption, completion, and cost posting back to the project can be reconstructed end
  to end from stored records alone.
WHY_IT_MATTERS: >
  If this specific chain cannot be reconstructed, no dispute about where a project's manufacturing
  cost actually came from can ever be resolved from evidence.
DISCONFIRMING_OBSERVATION: >
  Attempting to reconstruct the full chain from project task to final cost posting for a completed
  production run leaves gaps that cannot be filled from stored records alone.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a manufacturing order linked to a project task end to end, then attempt to reconstruct
  the full chain using only stored records.
```

## G12-PROJECT_MRP-Q023

```yaml
QID: G12-PROJECT_MRP-Q023
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Manually unlinking a manufacturing order from a project task after its cost has already been
  recorded against that task does not remove the historical cost record from the project's history.
WHY_IT_MATTERS: >
  A historical cost record that can be made to disappear by simply unlinking its source afterward
  defeats the purpose of having recorded it in the first place.
DISCONFIRMING_OBSERVATION: >
  Unlinking a manufacturing order from a project task after cost was recorded removes that cost from
  the project's historical record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record cost against a project task from a linked manufacturing order, then unlink the order and
  inspect the project's historical cost record.
```

## G12-PROJECT_MRP-Q024

```yaml
QID: G12-PROJECT_MRP-Q024
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a quality failure requires full scrap and a complete re-manufacture, the project sees this as
  two distinguishable cost events, not one that quietly folds the wasted run into the final
  successful one.
WHY_IT_MATTERS: >
  Folding a scrapped run into the successful one hides the true cost of quality failure from anyone
  reviewing project margin.
DISCONFIRMING_OBSERVATION: >
  A scrapped production run followed by a full re-manufacture appears on the project as a single
  cost event with no distinguishable record of the scrapped attempt.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Force a full scrap and re-manufacture cycle on production linked to a project task and inspect
  whether the two events are distinguishable in the project's cost record.
```

## G12-PROJECT_MRP-Q025

```yaml
QID: G12-PROJECT_MRP-Q025
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A manufacturing order accidentally duplicated against the same project task is detectable, and its
  cost is not silently double-counted in the project's total.
WHY_IT_MATTERS: >
  A duplication error that silently doubles a project's reported cost can trigger a false budget
  overrun or margin alarm that has nothing to do with actual spend.
DISCONFIRMING_OBSERVATION: >
  A duplicated manufacturing order linked to the same project task results in its cost being counted
  twice in the project's total with no detection.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create a duplicate manufacturing order against the same project task and inspect whether the
  duplication is detected and how the project's cost total responds.
```

## G12-PROJECT_MRP-Q026

```yaml
QID: G12-PROJECT_MRP-Q026
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Time logged directly against manufacturing floor activity and time logged on the project's own
  timesheet for the same underlying work are reconcilable against each other, not two disconnected
  records with no way to compare them.
WHY_IT_MATTERS: >
  Disconnected labor records for the same work make it impossible to catch double-recorded or
  missing time on either side.
DISCONFIRMING_OBSERVATION: >
  Time recorded on the manufacturing floor for work linked to a project task cannot be compared or
  reconciled against the time recorded on that task's own timesheet.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record time on both the manufacturing side and the project timesheet for the same linked work and
  attempt to reconcile the two.
```

## G12-PROJECT_MRP-Q027

```yaml
QID: G12-PROJECT_MRP-Q027
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When production linked to a project task is split into subcontracted sub-orders, the aggregate
  quantity and cost still trace back to the originating project task without ambiguity.
WHY_IT_MATTERS: >
  A split into sub-orders that loses its trace back to the project defeats the purpose of the link
  the moment production gets even slightly more complex.
DISCONFIRMING_OBSERVATION: >
  A production run split into subcontracted sub-orders cannot be traced back in full to the
  originating project task.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Split production linked to a project task into subcontracted sub-orders and attempt to trace the
  combined result back to the originating task.
```

## G12-PROJECT_MRP-Q028

```yaml
QID: G12-PROJECT_MRP-Q028
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A manufacturing order created with no linked project task is never later silently attributed to an
  unrelated project task through an ambiguous automatic match.
WHY_IT_MATTERS: >
  A silent, unintended link between an unrelated production run and a project misstates that
  project's real cost and progress.
DISCONFIRMING_OBSERVATION: >
  A manufacturing order created with no project link becomes attributed to a project task with no
  explicit action having made that link.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a manufacturing order with no project link under conditions similar to an existing project
  task and observe whether it becomes attributed without an explicit linking action.
```

## G12-PROJECT_MRP-Q029

```yaml
QID: G12-PROJECT_MRP-Q029
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a manufacturing order linked to a project task yields more than one distinct output (a
  primary item plus a by-product), the project's cost and quantity reporting attributes value to each
  output rather than crediting everything to the primary output alone.
WHY_IT_MATTERS: >
  Crediting an entire multi-output run to a single output overstates that item's true cost while
  hiding the value of the by-product entirely.
DISCONFIRMING_OBSERVATION: >
  A production run linked to a project task yields a by-product that receives no distinguishable
  cost or quantity attribution anywhere on the project.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Produce a run linked to a project task that yields both a primary output and a by-product, and
  inspect how each is reflected on the project.
```

## G12-PROJECT_MRP-Q030

```yaml
QID: G12-PROJECT_MRP-Q030
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a project task requires a multi-stage sequence of manufacturing orders, the task's reported
  lead time reflects the true aggregate across all stages, not only the most recent stage in
  isolation.
WHY_IT_MATTERS: >
  A lead-time figure based only on the last stage hides delay accumulated earlier in the sequence
  from anyone planning around the task's completion.
DISCONFIRMING_OBSERVATION: >
  A project task fed by a multi-stage manufacturing sequence reports a lead time that reflects only
  the final stage, ignoring delay accumulated in earlier stages.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Run a multi-stage manufacturing sequence linked to a single project task with a deliberate delay in
  an early stage, then inspect the task's reported lead time.
```

## G12-PROJECT_MRP-Q031

```yaml
QID: G12-PROJECT_MRP-Q031
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a production scheduling mechanism gives weight to a linked project task's own deadline
  urgency is an explicit, documented configuration, not an undocumented and unpredictable behaviour.
WHY_IT_MATTERS: >
  An undocumented scheduling behaviour makes it impossible for a project manager to know whether
  raising a task's priority will actually influence when production happens.
DISCONFIRMING_OBSERVATION: >
  Raising a project task's deadline urgency produces an inconsistent, undocumented effect on the
  scheduling of its linked manufacturing order across comparable cases.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Raise the deadline urgency on two comparable project tasks with linked manufacturing orders and
  compare the resulting scheduling behaviour.
```

## G12-PROJECT_MRP-Q032

```yaml
QID: G12-PROJECT_MRP-Q032
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Viewing a detailed manufacturing cost breakdown from within a project view requires a permission
  distinct from general project view access, rather than being exposed to anyone who can simply open
  the project.
WHY_IT_MATTERS: >
  Detailed production cost is sensitive information that a general project viewer, such as a junior
  team member, has no inherent need to see.
DISCONFIRMING_OBSERVATION: >
  An account with only general project view access can see a detailed manufacturing cost breakdown
  with no distinct permission granted for it.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  From an account with general project view access only, attempt to view a detailed manufacturing
  cost breakdown for a linked production run.
```

## G12-PROJECT_MRP-Q033

```yaml
QID: G12-PROJECT_MRP-Q033
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A manufacturing order and a project task that happen to share a similar name but have no actual
  business relationship are never automatically linked based on that coincidental similarity alone.
WHY_IT_MATTERS: >
  An automatic link based on coincidental naming would silently attribute unrelated production cost
  and progress to the wrong project.
DISCONFIRMING_OBSERVATION: >
  A manufacturing order and an unrelated project task with a similar name become linked with no
  explicit linking action having occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a manufacturing order and an unrelated project task with deliberately similar names and
  observe whether any automatic link forms.
```

## G12-PROJECT_MRP-Q034

```yaml
QID: G12-PROJECT_MRP-Q034
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two people concurrently linking or unlinking the same project task and manufacturing order do not
  leave the pair in an inconsistent state, such as linked on one side and not the other.
WHY_IT_MATTERS: >
  An inconsistent link state between the two records means neither side can be trusted to reflect
  the other's true status.
DISCONFIRMING_OBSERVATION: >
  Concurrent linking and unlinking actions on the same project-task/manufacturing-order pair leave
  the two records disagreeing about whether they are linked.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  From two sessions, simultaneously attempt to link and unlink the same project task and
  manufacturing order and inspect the resulting state on both sides.
```

## G12-PROJECT_MRP-Q035

```yaml
QID: G12-PROJECT_MRP-Q035
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a manufacturing order's production location differs from the project's own registered
  location, the resulting regional cost or tax context is applied according to the actual production
  location, not silently assumed to match the project's location.
WHY_IT_MATTERS: >
  Assuming the project's own location for a cost or tax context that actually depends on where
  production happened produces a materially wrong figure.
DISCONFIRMING_OBSERVATION: >
  A production run at a location different from the project's registered location has its cost or
  tax context computed as though it occurred at the project's location instead.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Produce at a location different from a project's registered location and inspect which location's
  cost/tax context was actually applied.
```

## G12-PROJECT_MRP-Q036

```yaml
QID: G12-PROJECT_MRP-Q036
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a project task while its linked manufacturing order is still mid-run either propagates a
  defined action to that order (pause, flag, or cancel) or leaves it in an explicitly flagged
  orphaned state, rather than continuing silently as if nothing changed.
WHY_IT_MATTERS: >
  Production continuing unnoticed for a task the business has already cancelled wastes resources on
  work nobody wants any more.
DISCONFIRMING_OBSERVATION: >
  Cancelling a project task with a mid-run linked manufacturing order leaves that order continuing
  with no flag, pause, or cancellation propagated.
EXPECTED_SURFACE: S1,S5,S8
PRECONDITIONS: >
  Cancel a project task while its linked manufacturing order is still mid-run and observe what
  happens to that order.
```

## G12-PROJECT_MRP-Q037

```yaml
QID: G12-PROJECT_MRP-Q037
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A revision to a linked manufacturing order's own quantity or dates is reflected on the project
  task's history as a distinct update event, not as a silent overwrite that erases what was
  originally recorded.
WHY_IT_MATTERS: >
  A silent overwrite of a manufacturing order's original figures removes the ability to later see
  how the plan for a task actually changed over time.
DISCONFIRMING_OBSERVATION: >
  A revision to a linked manufacturing order's quantity or dates leaves no distinct update event on
  the project task's history, only the final revised value.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Revise the quantity or dates on a manufacturing order linked to a project task and inspect the
  task's history for a distinct update record.
```

## G12-PROJECT_MRP-Q038

```yaml
QID: G12-PROJECT_MRP-Q038
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where actual labor time on a production run differs from the standard or planned time assumed when
  the project task was costed, the variance is visible on the project side, not silently absorbed
  into the originally planned figure.
WHY_IT_MATTERS: >
  A hidden labor variance prevents a project manager from ever learning that a task consistently
  takes longer, or less, than what was planned.
DISCONFIRMING_OBSERVATION: >
  Actual labor time on a production run differs materially from the planned figure used at costing
  time, and the project task shows no visible variance.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record actual labor time that differs from the planned figure on a production run linked to a
  project task, then inspect the task for a visible variance.
```

## G12-PROJECT_MRP-Q039

```yaml
QID: G12-PROJECT_MRP-Q039
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A manufacturing order's reservation of inventory against a project-linked allocation does not
  silently compete with a reservation from an unrelated project without either side being made aware
  of the conflict.
WHY_IT_MATTERS: >
  Two projects silently drawing on the same reserved stock without either side knowing can leave one
  of them unable to complete as planned with no warning.
DISCONFIRMING_OBSERVATION: >
  Inventory reserved for one project's linked manufacturing order is also consumed by an unrelated
  project's reservation with neither side shown the conflict.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create competing inventory reservations from two unrelated projects' linked manufacturing orders
  against the same limited stock and observe whether the conflict is surfaced to either side.
```

## G12-PROJECT_MRP-Q040

```yaml
QID: G12-PROJECT_MRP-Q040
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a manufacturing order is placed on hold for a reason unrelated to the project itself (such as
  an equipment issue), the linked project task shows this as an explicit external dependency, rather
  than simply appearing as an ordinary in-progress state.
WHY_IT_MATTERS: >
  A project team that cannot distinguish normal progress from an external hold cannot correctly judge
  whether the delay is something they can influence.
DISCONFIRMING_OBSERVATION: >
  A manufacturing order placed on hold for a reason external to the project shows on the linked task
  identically to a normally progressing one.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Place a linked manufacturing order on hold for a reason unrelated to the project and inspect how
  the project task reflects that hold.
```

## G12-PROJECT_MRP-Q041

```yaml
QID: G12-PROJECT_MRP-Q041
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a project's own reporting currency differs from the currency used to cost production at the
  manufacturing facility, the conversion applied between the two is documented, not silently assumed
  to be identical.
WHY_IT_MATTERS: >
  Assuming two different currencies are the same produces a materially wrong project cost figure
  with no correction possible until someone notices.
DISCONFIRMING_OBSERVATION: >
  Production costed in a currency different from the project's reporting currency appears on the
  project with no documented conversion having been applied.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Cost a production run in a currency different from its linked project's reporting currency and
  inspect how the figure is converted for the project view.
```

## G12-PROJECT_MRP-Q042

```yaml
QID: G12-PROJECT_MRP-Q042
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reopening a project task after it was marked done, to correct an error, does not silently
  re-trigger or duplicate a manufacturing order that already completed under the earlier, mistaken
  done status.
WHY_IT_MATTERS: >
  An unintended re-triggered production run consumes real materials and labor for work that was
  never actually needed a second time.
DISCONFIRMING_OBSERVATION: >
  Reopening a completed project task causes its already-completed linked manufacturing order to be
  re-triggered or duplicated.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Complete a project task and its linked manufacturing order, then reopen the task to correct an
  error and observe whether the manufacturing order is affected.
```

## G12-PROJECT_MRP-Q043

```yaml
QID: G12-PROJECT_MRP-Q043
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A discrepancy between a manufacturing order's estimated and actual completion date is retained in
  the record even after the project task is later reported as on schedule for other purposes.
WHY_IT_MATTERS: >
  Losing the original schedule discrepancy once a task is later reported as on-time hides a pattern
  of estimation error that would otherwise inform future planning.
DISCONFIRMING_OBSERVATION: >
  A production run's estimated-versus-actual completion date discrepancy is no longer retrievable
  once the project task is reported as on schedule.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce a run that completes later than its estimate, then later report the project task as on
  schedule and check whether the original discrepancy is still retrievable.
```

## G12-PROJECT_MRP-Q044

```yaml
QID: G12-PROJECT_MRP-Q044
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an item produced through a project-linked manufacturing order later fails final acceptance by
  the customer or project owner after delivery, that rejection is traceable back to the specific
  production run without ambiguity.
WHY_IT_MATTERS: >
  An acceptance failure that cannot be traced to a specific production run prevents any investigation
  into what actually went wrong in that run.
DISCONFIRMING_OBSERVATION: >
  A delivered item's acceptance rejection cannot be traced back to the specific production run that
  produced it when more than one run contributed to the project.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have a delivered, project-linked item rejected on final acceptance, then attempt to trace that
  rejection back to the specific production run responsible.
```

## G12-PROJECT_MRP-Q045

```yaml
QID: G12-PROJECT_MRP-Q045
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A manufacturing order's consumption of raw materials reserved specifically for a project is
  validated against that project's own material budget or allocation, not merely against general
  stock availability regardless of project.
WHY_IT_MATTERS: >
  Checking only general stock availability lets a production run silently consume materials that
  were actually earmarked and budgeted for a different, specific project purpose.
DISCONFIRMING_OBSERVATION: >
  A manufacturing order consumes materials reserved for a specific project's allocation while general
  stock availability alone was the only check applied, exceeding that project's own allocation with
  no flag.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Set a project-specific material allocation smaller than general stock availability, then attempt
  production that would exceed the project's own allocation but not general availability.
```

## G12-PROJECT_MRP-Q046

```yaml
QID: G12-PROJECT_MRP-Q046
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Splitting a project task into two separate tasks after a manufacturing order was already linked to
  the original produces a defined, non-ambiguous attribution of that order to one or both resulting
  tasks, rather than an orphaned or duplicated link.
WHY_IT_MATTERS: >
  An ambiguous attribution after a routine task split makes it impossible to say afterward which of
  the resulting tasks the production cost actually belongs to.
DISCONFIRMING_OBSERVATION: >
  After splitting a project task with a linked manufacturing order into two tasks, the order's
  attribution to either resulting task is ambiguous, missing, or duplicated on both.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Split a project task that has a linked manufacturing order into two separate tasks and inspect the
  resulting attribution.
```

## G12-PROJECT_MRP-Q047

```yaml
QID: G12-PROJECT_MRP-Q047
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A manufacturing order's cancellation reason is captured and remains associated with the linked
  project task's history, distinguishing a cancelled-for-cause production attempt from one that
  simply never existed.
WHY_IT_MATTERS: >
  Without a retained cancellation reason, a reviewer cannot tell whether a missing production run was
  cancelled deliberately, for a documented cause, or never happened at all.
DISCONFIRMING_OBSERVATION: >
  A cancelled manufacturing order's reason for cancellation is not retrievable from the linked
  project task's history afterward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a manufacturing order linked to a project task with a specific cancellation reason, then
  inspect the task's history for that reason.
```

## G12-PROJECT_MRP-Q048

```yaml
QID: G12-PROJECT_MRP-Q048
MODULE: project_mrp
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a manufacturing order for a project task is created, then cancelled, then a second order is
  created for the same task, the combined evidentiary record distinguishes all three events (created,
  cancelled, re-created) rather than merging them into what looks like one continuous order.
WHY_IT_MATTERS: >
  Merging a cancel-and-recreate sequence into what looks like a single continuous order hides the
  fact that an earlier attempt failed or was abandoned.
DISCONFIRMING_OBSERVATION: >
  A create-cancel-recreate sequence for the same project task appears in the record as a single,
  continuous manufacturing order with no distinguishable trace of the cancelled first attempt.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a manufacturing order for a project task, cancel it, create a second order for the same
  task, then inspect whether all three events remain individually distinguishable.
```
