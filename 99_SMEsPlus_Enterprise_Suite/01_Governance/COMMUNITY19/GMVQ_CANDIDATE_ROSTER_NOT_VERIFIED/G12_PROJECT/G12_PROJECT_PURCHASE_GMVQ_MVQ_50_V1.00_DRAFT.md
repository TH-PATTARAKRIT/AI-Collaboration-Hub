# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_purchase Module MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_PURCHASE-MVQ50-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `project_purchase`
**Wave:** W3
**Author Cell:** P12-4 (GMVQ Question Factory — Production Cell P12-4)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the seam between project management and
vendor procurement. Per the Bridge Module Rule, `project_purchase` is a 2-way bridge: it owns no
behaviour of its own beyond making project cost tracking and vendor procurement agree with each
other. Every question below fails the seam test — "if this capability were removed and project and
purchasing were used entirely apart, would the question still make sense?" — with a NO: each
question depends on a purchase actually being tied to a project's cost, budget, or task.

This bank is deliberately silent on any customer-facing sale or order. Where procurement is placed
to fulfil a *customer* order that in turn funds a project task, that three-way seam belongs to the
`sale_purchase_project` family (G08) and is out of scope here. This bank covers purchases made for
project cost/budget purposes generally, including non-billable and internal-cost-center projects.

Question text is source-neutral: no vendor or product name, no technical identifier (field, model,
method, XML ID, API path), and no reference to the module's own metadata name.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 50 questions exist because each tests a distinct material hypothesis, spread across
  business rule, state transition, configuration dependency, role and permission, exception path,
  cancellation, reversal, negative case, cross-module dependency, auditability, tenant/company
  boundary, and concurrency and ordering.
- Pre-authoring check performed: `grep -h HYPOTHESIS` across `G08_SALE_PURCHASE_PROJECT` (main +
  supplement) confirmed those questions are anchored on a *customer order* funding the purchase via
  a project task — a dimension this bank never uses. No overlap found.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G12-PROJECT_PURCHASE-Q001

```yaml
QID: G12-PROJECT_PURCHASE-Q001
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A purchase raised to source something for a specific project task records that linkage at the
  moment of creation, not only inferred later from matching cost postings.
WHY_IT_MATTERS: >
  A linkage inferred only after the fact from cost matching is unreliable whenever two candidate
  tasks could plausibly have generated the same cost, and disputes about attribution become
  unresolvable.
DISCONFIRMING_OBSERVATION: >
  The purchase's project-task reference exists only after a later cost-matching step runs; before
  that, no record shows which task the purchase was actually meant to serve.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a purchase explicitly against a project task and inspect the purchase record immediately,
  before any cost posting occurs.
```

## G12-PROJECT_PURCHASE-Q002

```yaml
QID: G12-PROJECT_PURCHASE-Q002
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cost committed by a purchase order is a separate, distinct amount in a project's budget view from
  cost that has actually been invoiced by the vendor.
WHY_IT_MATTERS: >
  Collapsing committed and invoiced cost into one figure overstates certainty about spend that has
  not actually been billed, and understates exposure that has been committed but not yet paid.
DISCONFIRMING_OBSERVATION: >
  The project's budget view shows only one combined spend figure, with no way to distinguish
  what is merely on order from what has actually been billed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place a purchase order against a project task, view the project's budget before any vendor bill
  exists, then again after the bill is recorded, and compare the two figures shown.
```

## G12-PROJECT_PURCHASE-Q003

```yaml
QID: G12-PROJECT_PURCHASE-Q003
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Two different project tasks cannot each silently claim ownership of the same single purchase
  line without one of them being flagged.
WHY_IT_MATTERS: >
  Dual attribution of one cost to two tasks double-counts spend in both tasks' own budget views.
DISCONFIRMING_OBSERVATION: >
  A single purchase line appears as an attributed cost inside two different tasks' budget totals at
  once, with neither view flagging the conflict.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to attribute one already-linked purchase line to a second, different project task and
  observe whether the system blocks, warns, or silently allows it.
```

## G12-PROJECT_PURCHASE-Q004

```yaml
QID: G12-PROJECT_PURCHASE-Q004
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling a purchase order after it has already been counted in a project's committed budget
  removes it from that committed figure, rather than leaving a ghost commitment.
WHY_IT_MATTERS: >
  A ghost commitment overstates remaining budget risk and can block or discourage legitimate new
  spend against a task that actually has room.
DISCONFIRMING_OBSERVATION: >
  The project's committed-spend figure still includes the cancelled purchase order's amount after
  cancellation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a project's committed budget with the purchase order open, cancel the order, and re-check
  the committed figure.
```

## G12-PROJECT_PURCHASE-Q005

```yaml
QID: G12-PROJECT_PURCHASE-Q005
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a project's task is deleted after a purchase order was linked to it, the purchase order's
  cost does not silently vanish from the project's overall cost view.
WHY_IT_MATTERS: >
  A cost that vanishes with its task understates the project's true spend and hides money already
  committed on the vendor's side.
DISCONFIRMING_OBSERVATION: >
  After the funding task is deleted, the project's overall cost total drops by the purchase order's
  amount with no flag or reassignment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Link a purchase order to a task, delete the task, and compare the project's overall cost total
  before and after.
```

## G12-PROJECT_PURCHASE-Q006

```yaml
QID: G12-PROJECT_PURCHASE-Q006
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A purchase order amended to a higher amount after the project's budget was already approved
  either re-triggers approval or is explicitly flagged for review.
WHY_IT_MATTERS: >
  An unflagged increase after approval defeats the point of approving a budget in the first place.
DISCONFIRMING_OBSERVATION: >
  The purchase order's amount is increased after approval and no approval step re-runs and no flag
  appears anywhere on the project or the order.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Approve a project budget, then increase the value of an already-linked purchase order, and
  observe whether any control activates.
```

## G12-PROJECT_PURCHASE-Q007

```yaml
QID: G12-PROJECT_PURCHASE-Q007
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The role authorized to approve a project's budget is not automatically the role authorized to
  approve a vendor's purchase order value, and each control operates independently.
WHY_IT_MATTERS: >
  Merging the two authorities lets one person single-handedly both set a spending ceiling and
  approve spend against it, defeating segregation of duties.
DISCONFIRMING_OBSERVATION: >
  A person who can approve a project's budget can also single-handedly approve a purchase order
  against it with no separate authorization required.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Identify the roles for project budget approval and purchase order approval, and test whether one
  role alone can complete both steps for the same spend.
```

## G12-PROJECT_PURCHASE-Q008

```yaml
QID: G12-PROJECT_PURCHASE-Q008
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Splitting one purchase order's cost across more than one project task allocates the total
  consistently to sum to the original amount.
WHY_IT_MATTERS: >
  A split that does not sum to the original either creates cost out of nothing or loses it, either
  way corrupting every task's own budget figure.
DISCONFIRMING_OBSERVATION: >
  The sum of the amounts allocated to each task from a split purchase order does not equal the
  order's original total.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split one purchase order's cost across two project tasks and sum the two allocated figures against
  the order's original amount.
```

## G12-PROJECT_PURCHASE-Q009

```yaml
QID: G12-PROJECT_PURCHASE-Q009
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A vendor invoice priced differently from its originating purchase order surfaces that variance to
  whoever manages the project's budget, not only to purchasing.
WHY_IT_MATTERS: >
  A project manager unaware of a price variance cannot judge whether the task's budget is still on
  track, and may report a margin that quietly erodes.
DISCONFIRMING_OBSERVATION: >
  A vendor invoice's price differs from the purchase order and the project's own budget or cost view
  shows no indication of the variance.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a vendor invoice at a different price than its purchase order and check whether the
  project's own cost view surfaces the difference.
```

## G12-PROJECT_PURCHASE-Q010

```yaml
QID: G12-PROJECT_PURCHASE-Q010
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a project spans more than one company in a multi-company setup, a purchase order raised by
  one company for another company's project attributes cost according to a documented rule.
WHY_IT_MATTERS: >
  An undocumented, inconsistent attribution across company boundaries misstates each company's own
  cost and can misstate intercompany balances.
DISCONFIRMING_OBSERVATION: >
  Cost attribution for a cross-company purchase against a project varies unexplained between similar
  cases with no documented rule governing which company records what.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Set up a project owned by one company and raise a purchase order under a different company
  entity for one of its tasks, then trace how cost is attributed.
```

## G12-PROJECT_PURCHASE-Q011

```yaml
QID: G12-PROJECT_PURCHASE-Q011
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reassigning a purchase order originally raised for one project to a different project leaves a
  traceable record of the change.
WHY_IT_MATTERS: >
  An untraceable reassignment makes it impossible to later explain why one project's historical cost
  report no longer matches what was originally reported.
DISCONFIRMING_OBSERVATION: >
  A purchase order's project link is changed and no record of the prior project, the new project, or
  who made the change, and when, is retained anywhere.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Reassign an already-linked purchase order to a different project and inspect the audit history for
  the change.
```

## G12-PROJECT_PURCHASE-Q012

```yaml
QID: G12-PROJECT_PURCHASE-Q012
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A project placed on hold does not, by itself, cancel or suspend an already-placed purchase order
  still awaiting delivery.
WHY_IT_MATTERS: >
  An automatic, undocumented suspension of an in-flight vendor commitment can breach a vendor
  agreement the business is contractually bound to honor.
DISCONFIRMING_OBSERVATION: >
  Placing the project on hold changes the state of an already-confirmed, still-open purchase order
  with no separate, explicit action taken on the order itself.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Place a project on hold while it has an open, unfulfilled purchase order and observe the order's
  own state.
```

## G12-PROJECT_PURCHASE-Q013

```yaml
QID: G12-PROJECT_PURCHASE-Q013
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Duplicating a project to plan a similar future engagement does not cause the duplicate to inherit
  a live reference to a purchase order already committed under the original.
WHY_IT_MATTERS: >
  A live reference in the duplicate would make a brand-new, unstarted project appear to already have
  vendor spend committed against it.
DISCONFIRMING_OBSERVATION: >
  The duplicated project shows the original project's purchase order as an active, current
  commitment of its own.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Duplicate a project that has an existing linked purchase order and inspect the duplicate's own
  purchase references.
```

## G12-PROJECT_PURCHASE-Q014

```yaml
QID: G12-PROJECT_PURCHASE-Q014
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a purchase requisition is raised directly from within a project task, it follows the same
  approval threshold rules as a requisition raised independently of any project.
WHY_IT_MATTERS: >
  An exemption for project-originated requisitions creates a known bypass of the ordinary spend
  control simply by routing the request through a project.
DISCONFIRMING_OBSERVATION: >
  A requisition raised from within a project task above the approval threshold proceeds without the
  approval that an identical, project-independent requisition would require.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Raise a requisition above the approval threshold from within a project task, and a matching one
  outside any project, and compare the approval behaviour.
```

## G12-PROJECT_PURCHASE-Q015

```yaml
QID: G12-PROJECT_PURCHASE-Q015
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A purchase order's currency, when different from the project's own reporting currency, is
  converted using one documented rate and moment consistently across every report.
WHY_IT_MATTERS: >
  Two different conversion moments for the same cost produce two different reported figures for
  what should be a single, fixed historical amount.
DISCONFIRMING_OBSERVATION: >
  The same foreign-currency purchase order's cost appears as two different converted amounts on two
  different project cost reports.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a purchase order in a currency different from the project's reporting currency and compare
  its converted cost across at least two different project reports.
```

## G12-PROJECT_PURCHASE-Q016

```yaml
QID: G12-PROJECT_PURCHASE-Q016
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Closing a project while a linked purchase order still has an outstanding, unfulfilled balance
  either blocks closure or leaves the balance explicitly flagged.
WHY_IT_MATTERS: >
  A closed project with a silently unresolved vendor balance can leave that spend permanently
  outside anyone's active attention.
DISCONFIRMING_OBSERVATION: >
  The project closes with an outstanding purchase order balance still open, and nothing on the
  closed project indicates the balance remains.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attempt to close a project that has a linked purchase order with an unfulfilled balance and
  observe the outcome.
```

## G12-PROJECT_PURCHASE-Q017

```yaml
QID: G12-PROJECT_PURCHASE-Q017
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A purchase order cancelled after its cost was already reported in a closed project's final cost
  figure results in that figure being explicitly corrected, not silently left stale.
WHY_IT_MATTERS: >
  A stale final figure misrepresents the project's true profitability to anyone relying on the
  closed record for future estimating.
DISCONFIRMING_OBSERVATION: >
  A closed project's final cost figure still includes a since-cancelled purchase order's amount with
  no correction recorded.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close a project, then cancel a purchase order that had already contributed to its reported final
  cost, and re-check the figure.
```

## G12-PROJECT_PURCHASE-Q018

```yaml
QID: G12-PROJECT_PURCHASE-Q018
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Someone with permission to view a project's overall budget but no permission over purchasing does
  not see individual vendor pricing through the project view.
WHY_IT_MATTERS: >
  Vendor-specific pricing is commercially sensitive; leaking it through a project view that was
  never meant to expose it undermines purchasing's negotiating position.
DISCONFIRMING_OBSERVATION: >
  A user with project-budget-only access can see a specific vendor's line-item price by navigating
  through the project's own cost breakdown.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  As a user with project-budget view access only, attempt to drill into a purchase order's own
  vendor pricing through the project's cost breakdown.
```

## G12-PROJECT_PURCHASE-Q019

```yaml
QID: G12-PROJECT_PURCHASE-Q019
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A purchase order deleted outright, where deletion is distinct from cancellation, does not leave a
  project's cost record pointing at a reference with no explanation.
WHY_IT_MATTERS: >
  A broken, unexplained reference in a cost record makes it impossible for a later reviewer to
  understand what the missing line originally represented.
DISCONFIRMING_OBSERVATION: >
  The project's cost record shows a line referencing a purchase order that no longer exists, with no
  indication of what happened to it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Where outright deletion of a purchase order is permitted, delete one linked to a project and
  inspect the project's cost record afterward.
```

## G12-PROJECT_PURCHASE-Q020

```yaml
QID: G12-PROJECT_PURCHASE-Q020
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two purchase orders placed for the same project task at nearly the same time, each within its own
  approval authority, do not silently combine into double the intended commitment without
  visibility.
WHY_IT_MATTERS: >
  A silent doubling of commitment through two independently-approved but overlapping orders defeats
  the purpose of an approval ceiling meant to cap total spend.
DISCONFIRMING_OBSERVATION: >
  Two concurrently placed purchase orders for the same task together exceed the task's approval
  ceiling and neither the placing users nor the project see any warning.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Simultaneously place two separate purchase orders against the same project task, each individually
  within the approval limit, and check whether their combined total is flagged.
```

## G12-PROJECT_PURCHASE-Q021

```yaml
QID: G12-PROJECT_PURCHASE-Q021
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A recurring or blanket purchase arrangement drawing repeatedly against one persistent project
  accumulates committed cost correctly across each release rather than resetting or double-counting.
WHY_IT_MATTERS: >
  A resetting or double-counting accumulation makes a long-running project's cumulative cost figure
  meaningless for tracking budget consumption over time.
DISCONFIRMING_OBSERVATION: >
  After several releases against a blanket arrangement, the project's cumulative committed figure
  does not equal the sum of the individual releases.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Draw several sequential releases against one blanket purchase arrangement tied to a persistent
  project and sum the project's own recorded cumulative commitment.
```

## G12-PROJECT_PURCHASE-Q022

```yaml
QID: G12-PROJECT_PURCHASE-Q022
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a project's approved budget cap would be exceeded by a new purchase order, the system's
  behaviour (block, warn, or allow with flag) is one documented, consistent rule rather than varying
  case to case.
WHY_IT_MATTERS: >
  An inconsistent response to breaching a budget cap means the control's effect depends on
  unrelated factors rather than the actual breach, making the cap unreliable.
DISCONFIRMING_OBSERVATION: >
  Two purchase orders that each breach their project's budget cap by a similar margin produce two
  different system responses with no documented reason for the difference.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Raise two comparable purchase orders that each breach a different project's approved budget cap
  and compare the resulting system behaviour.
```

## G12-PROJECT_PURCHASE-Q023

```yaml
QID: G12-PROJECT_PURCHASE-Q023
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A purchase order's expected delivery date and the project task's own planned dependency on that
  delivery are reconciled through one documented rule when they disagree, not left silently unequal.
WHY_IT_MATTERS: >
  An unreconciled disagreement between a vendor's promised date and the project's own schedule
  leaves the project team unaware their plan depends on a date that has already changed.
DISCONFIRMING_OBSERVATION: >
  The purchase order's delivery date changes and the dependent project task's own schedule shows no
  update or flag reflecting the new date.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Change a purchase order's expected delivery date after a dependent project task's schedule was
  set from the original date, and check the task's schedule view.
```

## G12-PROJECT_PURCHASE-Q024

```yaml
QID: G12-PROJECT_PURCHASE-Q024
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Renaming or re-numbering a project after a purchase order already references it updates the
  purchase order's own reference display rather than showing a stale label.
WHY_IT_MATTERS: >
  A stale label on a vendor-facing or purchasing-facing document confuses anyone trying to
  cross-reference it against the project's current identity.
DISCONFIRMING_OBSERVATION: >
  After the project is renamed, an already-linked purchase order still displays the project's old
  name or number.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Rename a project that has a linked purchase order and check the reference shown on the purchase
  order afterward.
```

## G12-PROJECT_PURCHASE-Q025

```yaml
QID: G12-PROJECT_PURCHASE-Q025
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A vendor credit note issued against a purchase order after the project has already closed and
  reported final cost either reopens the project's cost figure through a documented path or is
  recorded separately.
WHY_IT_MATTERS: >
  A credit note that is neither reflected nor separately tracked understates the true final cost
  correction and can misstate the project's own historical profitability.
DISCONFIRMING_OBSERVATION: >
  A vendor credit note against a closed project's purchase order is recorded with no visible effect
  on, or separate note against, that project's reported final cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Close a project, then apply a vendor credit note to one of its already-reported purchase orders,
  and check the project's cost record for any resulting change.
```

## G12-PROJECT_PURCHASE-Q026

```yaml
QID: G12-PROJECT_PURCHASE-Q026
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a purchase order references a project task that itself is later merged into a different task
  during restructuring, the purchase order's reference updates to the surviving task.
WHY_IT_MATTERS: >
  A reference left pointing at a now-absorbed task makes the merged task's true cost look
  incomplete and the old task's cost look like an unexplained orphan.
DISCONFIRMING_OBSERVATION: >
  After two tasks are merged, a purchase order originally linked to the absorbed task still shows
  that absorbed task as its reference, rather than the surviving one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Merge two project tasks where one already has a linked purchase order, and check the purchase
  order's task reference afterward.
```

## G12-PROJECT_PURCHASE-Q027

```yaml
QID: G12-PROJECT_PURCHASE-Q027
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Concurrent edits to a project's task budget and to a linked purchase order's amount at nearly the
  same moment do not result in one change being silently discarded.
WHY_IT_MATTERS: >
  A silently discarded concurrent edit leaves one of the two users believing their change took
  effect when it did not, with no error to alert them.
DISCONFIRMING_OBSERVATION: >
  After two near-simultaneous edits, one to the task budget and one to the linked purchase order
  amount, one of the two changes is missing with no conflict notice shown to either editor.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Simulate two users editing, at nearly the same time, a project task's budget and its linked
  purchase order's amount, then verify both changes persisted.
```

## G12-PROJECT_PURCHASE-Q028

```yaml
QID: G12-PROJECT_PURCHASE-Q028
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A purchase order's approval routed through an automated, no-human-review path is subject to the
  same project budget check as one manually approved.
WHY_IT_MATTERS: >
  An automated path exempted from the budget check becomes an unmonitored route for spend to bypass
  the project's own cost control.
DISCONFIRMING_OBSERVATION: >
  A purchase order approved through an automated path proceeds despite exceeding the project's
  budget check that a manually approved equivalent order would have been stopped by.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Route a purchase order that would breach a project's budget check through both the automated
  approval path and manual approval, and compare outcomes.
```

## G12-PROJECT_PURCHASE-Q029

```yaml
QID: G12-PROJECT_PURCHASE-Q029
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where purchasing operates under a different company entity than the one holding the project, the
  inter-company step required before the cost is visible on the project is a documented, enforced
  boundary.
WHY_IT_MATTERS: >
  An unenforced boundary lets cost cross company lines onto a project's books without the
  intercompany transaction that should govern and record that crossing.
DISCONFIRMING_OBSERVATION: >
  A purchase raised by one company entity appears as project cost on another company's project with
  no intercompany step having occurred.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Raise a purchase order under one company entity against a project owned by a different company
  entity, and trace whether an intercompany step is required before cost is visible.
```

## G12-PROJECT_PURCHASE-Q030

```yaml
QID: G12-PROJECT_PURCHASE-Q030
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A project manager's authority to request spend against the project's approved budget and
  purchasing's authority to actually approve the vendor commitment are two separate, independently
  enforced approval chains.
WHY_IT_MATTERS: >
  Collapsing the two chains lets a project manager commit the business to a vendor without the
  independent commercial check purchasing exists to provide.
DISCONFIRMING_OBSERVATION: >
  A project manager's own budget-approval action, by itself, finalizes a vendor commitment with no
  separate purchasing-side approval step occurring.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a project manager, approve spend against a project's budget and observe whether the linked
  purchase order still requires a separate purchasing approval before becoming a live commitment.
```

## G12-PROJECT_PURCHASE-Q031

```yaml
QID: G12-PROJECT_PURCHASE-Q031
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  At project closure, reconciling every purchase order raised against it identifies any commitment
  that was never actually invoiced.
WHY_IT_MATTERS: >
  An unreconciled, never-invoiced commitment left behind at closure is money the business may still
  owe or may have wrongly assumed it already paid.
DISCONFIRMING_OBSERVATION: >
  A project closes with a purchase order that was never invoiced, and no reconciliation step
  surfaces that outstanding commitment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close a project that has at least one purchase order never matched to a vendor invoice, and check
  whether closure surfaces that gap.
```

## G12-PROJECT_PURCHASE-Q032

```yaml
QID: G12-PROJECT_PURCHASE-Q032
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A purchase order originally raised with no project reference, later manually linked to a project
  after the fact, is recorded so that the link's creation date is distinguishable from the purchase
  order's original date.
WHY_IT_MATTERS: >
  Without distinguishing the two dates, a project's cost history can be made to appear as if it
  always included a cost that was only attributed to it much later.
DISCONFIRMING_OBSERVATION: >
  A purchase order manually linked to a project long after its original date shows the project's
  cost history as if the link had always existed, with no separate record of when the link was made.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Create a purchase order with no project reference, wait, then manually link it to a project, and
  inspect the audit trail for both dates.
```

## G12-PROJECT_PURCHASE-Q033

```yaml
QID: G12-PROJECT_PURCHASE-Q033
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Discontinuing use of a vendor mid-project does not silently remove or obscure the historical cost
  already attributed to the project from that vendor's earlier purchase orders.
WHY_IT_MATTERS: >
  Losing historical cost attribution when a vendor is discontinued would corrupt a project's own
  cumulative cost record for reasons unrelated to the project itself.
DISCONFIRMING_OBSERVATION: >
  After a vendor is discontinued, the project's cost report no longer shows the cost previously
  attributed to purchases from that vendor.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record project cost from a vendor's purchase orders, then discontinue that vendor, and re-check
  the project's cost report.
```

## G12-PROJECT_PURCHASE-Q034

```yaml
QID: G12-PROJECT_PURCHASE-Q034
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A negative-value correction line added to a purchase order after the project has already reported
  that cost is reflected in the project's cost view through a visible, traceable adjustment rather
  than a silent rewrite.
WHY_IT_MATTERS: >
  A silent rewrite of a previously reported cost figure destroys the ability to explain, later, why
  a historical report no longer matches what was originally shown.
DISCONFIRMING_OBSERVATION: >
  A negative correction line changes the project's already-reported cost figure with no visible
  adjustment entry marking that a correction occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Add a negative correction line to a purchase order after its cost was already reported on a
  project, and check for a visible adjustment record.
```

## G12-PROJECT_PURCHASE-Q035

```yaml
QID: G12-PROJECT_PURCHASE-Q035
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where several projects each draw from one shared blanket purchase arrangement, one project's task
  consuming more than its expected share is visibly flagged rather than silently reducing what
  remains for the others.
WHY_IT_MATTERS: >
  An unflagged over-consumption by one project silently starves the budget available to every other
  project sharing the same arrangement.
DISCONFIRMING_OBSERVATION: >
  One project's draw against a shared blanket arrangement exceeds its expected share and no flag
  appears on either that project or the other projects sharing the arrangement.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Have two projects draw against one shared blanket purchase arrangement, push one project's draw
  beyond its expected share, and check for a flag on either project.
```

## G12-PROJECT_PURCHASE-Q036

```yaml
QID: G12-PROJECT_PURCHASE-Q036
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A purchase order's responsible buyer changing after the order was raised does not disconnect the
  project's historical traceability to who originally committed the cost.
WHY_IT_MATTERS: >
  Losing the original committing buyer's identity when responsibility is reassigned removes
  accountability for the decision that actually created the cost.
DISCONFIRMING_OBSERVATION: >
  After the responsible buyer on a purchase order is changed, the project's historical cost record
  shows only the new buyer, with no trace of who originally committed the cost.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Reassign the responsible buyer on a purchase order already linked to a project's cost, and check
  the project's historical audit trail.
```

## G12-PROJECT_PURCHASE-Q037

```yaml
QID: G12-PROJECT_PURCHASE-Q037
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An emergency or rush purchase order raised outside the normal requisition path for an urgent
  project need is still subject to the same budget-limit control as an ordinary requisition, or its
  exemption is an explicit, recorded decision.
WHY_IT_MATTERS: >
  An unrecorded, informal exemption for urgent purchases becomes a routine way to bypass budget
  controls simply by labelling any purchase as urgent.
DISCONFIRMING_OBSERVATION: >
  An emergency purchase order that exceeds a project's budget-limit control proceeds with no
  applied control and no recorded exemption decision.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Raise a purchase order flagged as an emergency or rush order that exceeds a project's budget
  limit, and observe whether the control applies or an exemption is explicitly recorded.
```

## G12-PROJECT_PURCHASE-Q038

```yaml
QID: G12-PROJECT_PURCHASE-Q038
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A purchase order placed for a project task, where that task is later deemed no longer needed and
  removed from project scope, results in the purchase order being flagged for review rather than
  remaining an unnoticed, unrelated commitment.
WHY_IT_MATTERS: >
  An unnoticed commitment left behind after its funding scope is removed can go unpaid, unreviewed,
  or unexplained for the life of the vendor relationship.
DISCONFIRMING_OBSERVATION: >
  A project task is removed from scope while it has an open, linked purchase order, and the purchase
  order shows no flag connecting it to the now-removed scope.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Remove a project task from scope after a purchase order has already been placed against it, and
  check whether the purchase order is flagged.
```

## G12-PROJECT_PURCHASE-Q039

```yaml
QID: G12-PROJECT_PURCHASE-Q039
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a project's cost report and a purchasing department's own commitment report both claim to
  show total outstanding spend for the same project, the two figures reconcile to a single
  documented source of truth or their difference is explained.
WHY_IT_MATTERS: >
  Two disagreeing figures for the same outstanding spend, with no documented reason, leaves whoever
  relies on either report unable to trust it.
DISCONFIRMING_OBSERVATION: >
  The project's own cost report and purchasing's commitment report show different outstanding-spend
  totals for the same project with no documented explanation for the difference.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Pull a project's outstanding-spend figure from the project's own cost report and from purchasing's
  commitment report and compare the two.
```

## G12-PROJECT_PURCHASE-Q040

```yaml
QID: G12-PROJECT_PURCHASE-Q040
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A purchase order line marked as fully received and billed for accounting purposes still correctly
  reflects, on the project side, whichever of received-but-not-yet-used or actually-consumed status
  the project's own tracking distinguishes.
WHY_IT_MATTERS: >
  Conflating fully billed with actually used overstates the project's true progress and can trigger
  premature milestone or completion claims.
DISCONFIRMING_OBSERVATION: >
  A purchase line marked fully received and billed is shown by the project's own tracking as already
  consumed, even though it has not actually been used on the task.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Mark a purchase order line as fully received and billed while the goods remain unused on the
  project task, and check the project's own consumption status for that line.
```

## G12-PROJECT_PURCHASE-Q041

```yaml
QID: G12-PROJECT_PURCHASE-Q041
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Archiving a vendor record after a project's historical purchase orders reference that vendor does
  not remove the ability to see that vendor's name on the project's historical cost trail.
WHY_IT_MATTERS: >
  Losing the vendor's identity on a historical cost trail defeats later attempts to understand or
  audit where a project's money actually went.
DISCONFIRMING_OBSERVATION: >
  After the vendor record is archived, the project's historical cost trail no longer displays which
  vendor a given past purchase was made from.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Archive a vendor referenced by a project's historical purchase orders and check the project's cost
  trail afterward.
```

## G12-PROJECT_PURCHASE-Q042

```yaml
QID: G12-PROJECT_PURCHASE-Q042
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A purchase order's tax treatment, when the project itself spans a jurisdiction different from the
  purchasing entity's home jurisdiction, follows one documented and consistently applied rule.
WHY_IT_MATTERS: >
  An inconsistent tax treatment across jurisdictions on project-linked purchases risks misstated tax
  liability that surfaces only at audit.
DISCONFIRMING_OBSERVATION: >
  Two comparable purchases for projects in different jurisdictions from the purchasing entity's home
  jurisdiction are taxed under two different, undocumented treatments.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Raise comparable purchase orders for two projects in jurisdictions different from the purchasing
  entity's own, and compare the tax treatment applied to each.
```

## G12-PROJECT_PURCHASE-Q043

```yaml
QID: G12-PROJECT_PURCHASE-Q043
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Withdrawal of project budget approval after a purchase order has already been placed against it
  does not retroactively cancel the vendor commitment without an explicit, separate cancellation
  action.
WHY_IT_MATTERS: >
  An automatic, silent cancellation of a live vendor commitment when a budget approval is later
  withdrawn can breach the vendor agreement without anyone deliberately deciding to cancel it.
DISCONFIRMING_OBSERVATION: >
  Withdrawing a project's budget approval changes an already-placed purchase order's own state with
  no separate, explicit cancellation action having been taken.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Withdraw a project budget approval after a purchase order was already placed under it, and observe
  the purchase order's own resulting state.
```

## G12-PROJECT_PURCHASE-Q044

```yaml
QID: G12-PROJECT_PURCHASE-Q044
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project task's estimated cost, once a purchase order is placed against it, does not silently
  overwrite the original estimate figure, keeping both the estimate and the committed figure
  separately visible.
WHY_IT_MATTERS: >
  Overwriting the estimate destroys the ability to later compare what was planned against what was
  actually committed, defeating the point of estimating at all.
DISCONFIRMING_OBSERVATION: >
  After a purchase order is placed against a task, the task's originally recorded estimate can no
  longer be viewed separately from the purchase order's committed amount.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Record a project task's cost estimate, place a purchase order against it, and check whether the
  original estimate remains separately viewable.
```

## G12-PROJECT_PURCHASE-Q045

```yaml
QID: G12-PROJECT_PURCHASE-Q045
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where the same purchase order funds work spanning two sequential phases of one project, each
  phase's share of that order's cost is separately attributable rather than assigned wholesale to
  only the first phase.
WHY_IT_MATTERS: >
  Assigning all cost to the first phase misstates that phase's own profitability and understates the
  second phase's true cost.
DISCONFIRMING_OBSERVATION: >
  A purchase order funding two sequential project phases shows its entire cost attributed to only
  the first phase, with none allocated to the second.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Fund two sequential phases of one project from a single purchase order and check how the order's
  cost is allocated between the two phases.
```

## G12-PROJECT_PURCHASE-Q046

```yaml
QID: G12-PROJECT_PURCHASE-Q046
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A purchase order's delivery being delayed past a project task's need date produces a visible
  schedule-risk indicator on the project rather than only a silent late-delivery note on the
  purchase order itself.
WHY_IT_MATTERS: >
  Confining the late-delivery signal to the purchase order leaves the project team unaware their
  own schedule is now at risk.
DISCONFIRMING_OBSERVATION: >
  A purchase order's delivery passes a dependent project task's need date and only the purchase
  order shows a late-delivery indication; the project's own schedule view shows nothing.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Let a purchase order's delivery date pass a dependent project task's own need date without
  delivery occurring, and check both the order and the project's schedule view.
```

## G12-PROJECT_PURCHASE-Q047

```yaml
QID: G12-PROJECT_PURCHASE-Q047
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reopening a closed project to accommodate a late-arriving vendor invoice against an old purchase
  order is a recorded action — who reopened it and when — rather than an unaudited state change.
WHY_IT_MATTERS: >
  An unaudited reopening of a closed project undermines the meaning of closure as a control
  checkpoint and hides who decided to revisit it.
DISCONFIRMING_OBSERVATION: >
  A previously closed project is reopened to record a late vendor invoice, and no audit entry shows
  who reopened it or when.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Reopen a closed project to record a late-arriving vendor invoice against one of its old purchase
  orders, and check the audit trail for the reopening action.
```

## G12-PROJECT_PURCHASE-Q048

```yaml
QID: G12-PROJECT_PURCHASE-Q048
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A purchase order's quantity being received in a currency-neutral unit while its cost is booked in
  a different currency does not create two disagreeing figures for the same committed amount within
  the project's cost view.
WHY_IT_MATTERS: >
  Two disagreeing figures for what should be one committed amount undermines confidence in every
  other number the project's cost view reports.
DISCONFIRMING_OBSERVATION: >
  The project's cost view shows two different values for the same purchase order's committed amount,
  traceable to the unit-versus-currency split rather than to any real cost change.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a purchase order whose received quantity is unit-based and whose cost is booked in a
  currency, and check for consistency between the two figures in the project's cost view.
```

## G12-PROJECT_PURCHASE-Q049

```yaml
QID: G12-PROJECT_PURCHASE-Q049
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Full or partial refunds from a vendor for previously invoiced project-related purchases reduce the
  project's recorded cost through a visible, traceable adjustment rather than an unexplained figure
  change.
WHY_IT_MATTERS: >
  An unexplained figure change makes it impossible to later distinguish a legitimate refund
  adjustment from a data-entry error or an unauthorized alteration.
DISCONFIRMING_OBSERVATION: >
  A vendor refund against a previously invoiced project purchase changes the project's cost figure
  with no visible adjustment record explaining the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a vendor refund against a previously invoiced, project-attributed purchase, and check for a
  visible adjustment record on the project's cost history.
```

## G12-PROJECT_PURCHASE-Q050

```yaml
QID: G12-PROJECT_PURCHASE-Q050
MODULE: project_purchase
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a single purchase order is later split into two separate orders to serve two different
  projects, each resulting order retains a correct, independent link to its own project rather than
  both still pointing at the original combined reference.
WHY_IT_MATTERS: >
  Two split orders both still referencing the original combined project would misattribute cost to
  the wrong project on at least one side of the split.
DISCONFIRMING_OBSERVATION: >
  After a purchase order is split to serve two different projects, one or both resulting orders
  still reference the original, pre-split combined project rather than their own correct project.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Split one purchase order originally serving one combined need into two orders, each intended for
  a different project, and check each resulting order's project reference.
```
