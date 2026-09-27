# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_hr_expense Module MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_HR_EXPENSE-MVQ50-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `project_hr_expense`
**Module Class:** 2-way bridge (project management + employee expense management) — seam-only per `GMVQ_BRIDGE_MODULE_RULE_V1.00`
**Wave:** W3
**Author Cell:** P12-2 (GMVQ Question Factory — Production Cell P12-2)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the seam between project management and
employee expense management: what happens when an expense claim is attributed to a project for
cost tracking, budget impact, and customer billing. Per the Bridge Module Rule, every question
below fails ONLY at that seam — if the capability were removed and expenses and projects were used
entirely apart, the question would no longer make sense, so it was cut before authoring.

Question text is source-neutral. It does not name the module, any vendor or product, or any
technical identifier (field, model, method, XML ID, API path).

## Control

- Bridge seam test applied to every question before inclusion: removal-of-capability test per
  `GMVQ_BRIDGE_MODULE_RULE_V1.00` section 2.
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 50 questions exist because each tests a distinct material seam hypothesis, spread
  across ordering, partiality, ownership, timing, reversal, quantity/money, lifecycle mismatch,
  error asymmetry, and authority.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G12-PROJECT_HR_EXPENSE-Q001

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q001
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The cost figure shown on a project for an approved expense agrees with the amount actually
  approved in the expense workflow, even when a foreign-currency conversion happened at a different
  point in each system's own timeline.
WHY_IT_MATTERS: >
  A project manager and a finance reviewer trusting two different numbers for the same underlying
  claim, with neither told there is a discrepancy, undermines every downstream decision built on
  project cost.
DISCONFIRMING_OBSERVATION: >
  The amount attributed to the project for a foreign-currency expense differs from the amount
  approved in the expense workflow, with no explanation surfaced for the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Submit and approve a foreign-currency expense claim attributed to a project, then compare the
  approved amount to the amount reflected in the project's cost view.
```

## G12-PROJECT_HR_EXPENSE-Q002

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q002
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Submitting an expense claim attributed to a project that has already been closed or archived is
  either blocked outright or produces an explicit exception state, not silently accepted as if the
  project were still active.
WHY_IT_MATTERS: >
  Cost silently added to a closed project distorts a figure that was supposed to already be final,
  after any review of it has already happened.
DISCONFIRMING_OBSERVATION: >
  An expense claim attributed to an already closed or archived project is accepted with no
  distinguishing exception or flag.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Close or archive a project, then submit an expense claim attributed to it.
```

## G12-PROJECT_HR_EXPENSE-Q003

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q003
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a multi-line expense report is only partially approved, the project's cost reflects only the
  approved lines, not the full submitted total.
WHY_IT_MATTERS: >
  A project cost figure inflated by rejected lines gives a false read on budget consumption before
  anyone has actually agreed the cost is legitimate.
DISCONFIRMING_OBSERVATION: >
  A project's cost total includes amounts from expense lines that were rejected, not only the lines
  that were approved.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Submit a multi-line expense report attributed to a project, approve some lines and reject others,
  then inspect the project's cost total.
```

## G12-PROJECT_HR_EXPENSE-Q004

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q004
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an expense is incurred in one accounting period but approved in a later one, the project cost
  report attributes it to a single, explicit, consistently applied period rather than an ambiguous
  or inconsistently chosen one.
WHY_IT_MATTERS: >
  A cost that can land in either period depending on unstated logic makes any period-over-period
  project cost comparison unreliable.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical late-approved expenses attributed to different projects are reported under
  different periods with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Log an expense in one period, approve it in a later period, and inspect which period the project
  cost report attributes it to; repeat for a second, comparable case.
```

## G12-PROJECT_HR_EXPENSE-Q005

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q005
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an expense already reflected in a project's cost is later reversed or rejected as a
  duplicate or an error, the project's cost figure is retroactively corrected rather than left to
  silently overstate cost indefinitely.
WHY_IT_MATTERS: >
  An overstated project cost that is never corrected after the underlying claim was withdrawn misleads
  every subsequent budget and margin decision on that project.
DISCONFIRMING_OBSERVATION: >
  A project's cost total continues to include an expense after that expense has been reversed or
  rejected, with no correction applied.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Approve an expense attributed to a project, confirm it is reflected in project cost, then reverse
  or reject the expense and re-check the project cost total.
```

## G12-PROJECT_HR_EXPENSE-Q006

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q006
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A foreign-currency expense attributed to a project is converted for cost display using one
  defined, documented point in time (such as the expense date or the approval date), not an
  inconsistent mix depending on when the report happens to run.
WHY_IT_MATTERS: >
  An undocumented, inconsistent conversion point means the same claim can appear to cost different
  amounts on different days with no underlying change to the claim itself.
DISCONFIRMING_OBSERVATION: >
  The project cost value for the identical foreign-currency expense changes across two separate
  views taken close together, with the conversion point used undocumented or inconsistent.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  View the project cost attributed to a foreign-currency expense at two different times and compare
  the converted amount and the rate basis used.
```

## G12-PROJECT_HR_EXPENSE-Q007

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q007
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Removing an employee from a project's staffed team after they have logged an expense against that
  project does not alter or hide the historical attribution of that expense to the project.
WHY_IT_MATTERS: >
  Historical cost accuracy must not depend on whether the person who incurred it is still on the
  team today.
DISCONFIRMING_OBSERVATION: >
  After an employee is removed from a project's team, an expense they previously logged against it
  is no longer shown attributed to that project, or its history is altered.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Log an expense against a project by a staffed employee, then remove that employee from the
  project's team and inspect the expense's historical attribution.
```

## G12-PROJECT_HR_EXPENSE-Q008

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q008
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An expense report that is successfully submitted and approved in the expense workflow, but whose
  linkage to the named project fails, is surfaced as a visible exception rather than silently leaving
  the cost invisible to the project.
WHY_IT_MATTERS: >
  A cost that exists in the expense system but never reaches the project view is invisible to the
  person responsible for that project's budget, with nothing prompting anyone to look for it.
DISCONFIRMING_OBSERVATION: >
  An approved expense intended for a named project is missing from that project's cost view with no
  error, warning, or exception recorded anywhere.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Submit and approve an expense naming a project under conditions likely to stress the linkage (for
  example, an unusual project state), then check both the expense record and the project cost view.
```

## G12-PROJECT_HR_EXPENSE-Q009

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q009
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Re-assigning an already-submitted expense from one project to another requires a permission
  distinct from the permission to approve the expense itself.
WHY_IT_MATTERS: >
  If approval rights alone are enough to silently redirect which project absorbs a cost, project
  budget figures can be manipulated without anyone exercising a dedicated re-attribution control.
DISCONFIRMING_OBSERVATION: >
  An account holding only expense-approval rights, with no distinct re-attribution grant, is able to
  change which project an already-submitted expense is attributed to.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  From an account with approval rights but no explicit re-attribution grant, attempt to change the
  project attributed to an already-submitted expense.
```

## G12-PROJECT_HR_EXPENSE-Q010

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q010
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two people concurrently changing which project the same expense line is attributed to do not
  result in one change being silently lost with neither notified of a conflict.
WHY_IT_MATTERS: >
  A silently lost re-attribution can leave a cost sitting against a project nobody actually chose in
  the end.
DISCONFIRMING_OBSERVATION: >
  Two concurrent attribution changes to the same expense line result in one disappearing with no
  conflict indication to either party.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Open the same expense line in two sessions and submit conflicting project re-attributions at
  nearly the same time.
```

## G12-PROJECT_HR_EXPENSE-Q011

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q011
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a billable expense already reflected on a draft customer invoice is subsequently rejected in
  the expense workflow, the invoice draft is flagged for reconciliation rather than left silently
  stale and overstated.
WHY_IT_MATTERS: >
  Billing a customer for a cost that has since been withdrawn is a direct financial and reputational
  exposure if nothing flags the mismatch before the invoice goes out.
DISCONFIRMING_OBSERVATION: >
  A rejected expense remains, unflagged, on a draft customer invoice that has not yet been sent.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Mark an expense billable and let it appear on a draft customer invoice, then reject the expense and
  inspect the state of the draft invoice.
```

## G12-PROJECT_HR_EXPENSE-Q012

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q012
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where both a project-level markup rate and a company-default markup rate exist for billable
  expense, an explicit, documented precedence decides which applies, rather than an unpredictable or
  undocumented pick.
WHY_IT_MATTERS: >
  An unpredictable markup outcome makes it impossible to explain a billed amount to a customer with
  confidence.
DISCONFIRMING_OBSERVATION: >
  A billable expense on a project with its own markup rate configured is billed using a different
  rate with no documented reason for which one won.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Configure a project-specific markup rate different from the company default, then bill an expense
  against that project and inspect which rate was applied.
```

## G12-PROJECT_HR_EXPENSE-Q013

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q013
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An expense category configured as excluded from project cost reporting is excluded consistently
  across every report and dashboard that surfaces project cost, not only the primary one.
WHY_IT_MATTERS: >
  A category exclusion that only holds in one place gives a false sense that sensitive or irrelevant
  cost has been filtered out everywhere, when it has not.
DISCONFIRMING_OBSERVATION: >
  An expense in a category configured as excluded from project cost appears in at least one project
  cost report or dashboard.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure an expense category as excluded from project cost, log a qualifying expense, and check
  every available project cost report and dashboard for it.
```

## G12-PROJECT_HR_EXPENSE-Q014

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q014
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An expense logged with task-level detail keeps that level of detail available even when the
  project's own reporting only aggregates cost at the whole-project level.
WHY_IT_MATTERS: >
  Losing task-level detail on aggregation removes the ability to later explain which specific piece
  of work actually drove a cost.
DISCONFIRMING_OBSERVATION: >
  An expense logged against a specific task can no longer be traced back to that task once the
  project's aggregate cost report is produced.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Log an expense against a specific project task, generate the project's aggregate cost report, and
  attempt to trace the expense back to its originating task.
```

## G12-PROJECT_HR_EXPENSE-Q015

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q015
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a billable expense's supporting receipt is exposed to a customer through a project-facing
  view, only what billing actually requires is shown, not the underlying personal payment method
  detail.
WHY_IT_MATTERS: >
  Over-exposing an employee's personal payment detail to a customer is a privacy failure with no
  business purpose behind it.
DISCONFIRMING_OBSERVATION: >
  A customer-facing view of a billable expense's receipt reveals personal payment method detail
  beyond what is needed to justify the billed amount.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Mark an expense with an attached receipt as billable and inspect what a customer-facing view of
  that expense actually exposes.
```

## G12-PROJECT_HR_EXPENSE-Q016

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q016
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a project's own reporting currency differs from the currency the expense was originally
  claimed in, the conversion is applied exactly once and is documented, not compounded across
  intermediate steps.
WHY_IT_MATTERS: >
  A compounded, undocumented double conversion produces a cost figure that does not correspond to
  any real exchange transaction.
DISCONFIRMING_OBSERVATION: >
  The project-reported cost of a foreign-currency expense reflects more than one conversion step, or
  the conversion basis used cannot be identified.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Claim an expense in a currency different from the project's reporting currency and trace the
  conversion path to the final reported figure.
```

## G12-PROJECT_HR_EXPENSE-Q017

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q017
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A project budget alert tied to expense totals fires at one consistent, defined point in the
  approval lifecycle (for example, on submission or on final approval), not inconsistently between
  comparable cases.
WHY_IT_MATTERS: >
  An alert that fires unpredictably relative to approval status is either a false alarm or a warning
  that arrives too late to act on.
DISCONFIRMING_OBSERVATION: >
  Two comparable expenses that would each cross a budget threshold trigger the alert at different
  points in their respective approval lifecycles.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Set a project budget threshold and submit two comparable expenses that would each cross it,
  observing at what lifecycle point the alert fires for each.
```

## G12-PROJECT_HR_EXPENSE-Q018

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q018
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An employee who is not staffed on a project is either prevented from logging an expense against it
  or such an entry is clearly flagged as an exception requiring explicit override.
WHY_IT_MATTERS: >
  An unstaffed employee freely charging cost to a project they have no assigned role on removes any
  meaningful gate on who can affect that project's budget.
DISCONFIRMING_OBSERVATION: >
  An employee with no staffed role on a project successfully logs an expense against it with no
  flag, warning, or override step.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  From an employee account not staffed on a given project, attempt to log an expense against it.
```

## G12-PROJECT_HR_EXPENSE-Q019

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q019
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An expense report split across multiple projects allocates its total using a defined, auditable
  method, and rounding differences from the split neither silently vanish nor get double-counted.
WHY_IT_MATTERS: >
  An unauditable or lossy split allocation across projects makes it impossible to confirm the sum of
  what each project was charged actually matches the original claim.
DISCONFIRMING_OBSERVATION: >
  The sum of a split expense's per-project allocations does not equal the original claimed total, or
  the split method cannot be identified after the fact.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Submit a single expense report allocated across at least two projects with an amount likely to
  produce a rounding remainder, then verify the allocations sum correctly and the method is
  identifiable.
```

## G12-PROJECT_HR_EXPENSE-Q020

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q020
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Resubmitting a corrected expense report after an earlier rejection does not cause the project's
  cost total to include figures from both the rejected original and the corrected resubmission.
WHY_IT_MATTERS: >
  A double-counted correction silently inflates project cost by exactly the amount that was supposed
  to have been fixed.
DISCONFIRMING_OBSERVATION: >
  After a rejected expense is corrected and resubmitted, the project's cost total reflects both the
  original rejected amount and the corrected amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Submit an expense attributed to a project, reject it, correct and resubmit it, then inspect the
  project's cost total.
```

## G12-PROJECT_HR_EXPENSE-Q021

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q021
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Expenses without a receipt, such as mileage or per-diem style claims, go through the same
  project-attribution and approval seam as receipted expenses, rather than a lighter, less-reviewed
  path.
WHY_IT_MATTERS: >
  A weaker path for unreceipted claims creates an easy, low-scrutiny way to inflate project cost.
DISCONFIRMING_OBSERVATION: >
  An unreceipted expense attributed to a project bypasses a review or approval step that an
  otherwise-comparable receipted expense would go through.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Submit a receipted and an unreceipted expense of comparable size against the same project and
  compare the approval paths each follows.
```

## G12-PROJECT_HR_EXPENSE-Q022

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q022
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a project defines its own approval hierarchy distinct from the general expense approval
  chain, an expense billed to that project actually routes through the project's hierarchy rather
  than bypassing it through the general chain.
WHY_IT_MATTERS: >
  A project-specific control that can be routed around by the general chain provides no real
  additional oversight, only the appearance of one.
DISCONFIRMING_OBSERVATION: >
  An expense billed to a project with its own defined approval hierarchy is approved entirely through
  the general expense chain with no step from the project's own hierarchy.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure a project-specific approval hierarchy for expenses, submit a qualifying expense against
  it, and trace which approvers actually acted.
```

## G12-PROJECT_HR_EXPENSE-Q023

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q023
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting a project that has linked expense history is either prevented or produces a defined,
  discoverable orphan-handling behaviour, rather than silently detaching the cost record from any
  project context.
WHY_IT_MATTERS: >
  A cost record silently cut loose from its project loses the context needed to ever explain why it
  was incurred.
DISCONFIRMING_OBSERVATION: >
  Deleting a project with linked expense history succeeds, and the expense records afterward show no
  trace of the project they were once attributed to.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to delete a project that has expense history linked to it and inspect the resulting state
  of that expense history.
```

## G12-PROJECT_HR_EXPENSE-Q024

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q024
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The tax treatment applied to a reimbursed expense (gross versus net of recoverable tax) is
  reflected consistently in what is shown as the project's cost, not silently mismatched between the
  reimbursement figure and the project cost figure.
WHY_IT_MATTERS: >
  A silent gross/net mismatch between what an employee is paid and what a project is charged makes
  project cost figures unreliable for margin analysis.
DISCONFIRMING_OBSERVATION: >
  The amount reimbursed to the employee and the amount attributed to the project's cost for the same
  expense differ by a tax-related amount that is nowhere explained.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Submit an expense subject to a recoverable tax component and compare the reimbursed amount to the
  amount shown as project cost.
```

## G12-PROJECT_HR_EXPENSE-Q025

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q025
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An expense originally logged as non-billable and later reclassified as billable does not
  retroactively become visible to the customer for the period before the reclassification without an
  explicit, deliberate action.
WHY_IT_MATTERS: >
  A retroactive, automatic exposure of a previously internal cost to a customer view is a disclosure
  the business never actually chose to make.
DISCONFIRMING_OBSERVATION: >
  Reclassifying a past expense as billable causes it to appear in the customer's view for the period
  before the reclassification, without a separate deliberate step to publish it.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Log an expense as non-billable, later reclassify it as billable, and inspect whether it appears in
  the customer-facing view retroactively.
```

## G12-PROJECT_HR_EXPENSE-Q026

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q026
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The audit trail can link a specific expense line to the specific project task that justified it,
  not only to a generic project-level bucket with no task-level distinction.
WHY_IT_MATTERS: >
  Without a task-level link, a reviewer cannot connect a cost to the actual piece of work that
  produced it, only to the project as a whole.
DISCONFIRMING_OBSERVATION: >
  An expense logged against a specific task shows in the audit trail only as attributed to the
  project generally, with no traceable link to the task.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Log an expense against a specific project task and inspect the audit trail for a task-level link.
```

## G12-PROJECT_HR_EXPENSE-Q027

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q027
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An expense claimed by an employee under one company context and attributed to a project belonging
  to a different company context does not combine into a single cost record without an explicit
  cross-company step.
WHY_IT_MATTERS: >
  Company-scoped cost data crossing a boundary without an explicit control is a direct violation of
  the tenant/company separation the whole cost model depends on.
DISCONFIRMING_OBSERVATION: >
  An expense claimed under one company is attributed to a project belonging to a different company
  with no explicit cross-company authorization step recorded.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Have an employee scoped to one company claim an expense against a project scoped to a different
  company and observe what step, if any, is required.
```

## G12-PROJECT_HR_EXPENSE-Q028

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q028
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An expense that fails a downstream accounting posting step, such as a locked accounting period, is
  still shown, distinctly flagged, in what a project manager sees as pending or unposted cost, rather
  than silently dropped from the total.
WHY_IT_MATTERS: >
  A posting failure that simply vanishes from the project's view understates true cost with no
  indication anything is wrong.
DISCONFIRMING_OBSERVATION: >
  An expense that fails to post due to a locked accounting period disappears entirely from the
  project's cost view with no pending or unposted indicator.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Lock the accounting period an expense would post into, submit and approve that expense against a
  project, and inspect the project's cost view.
```

## G12-PROJECT_HR_EXPENSE-Q029

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q029
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Duplicate submission of the same underlying receipt by an employee against the same project is
  detectable, and is not counted twice in the project's cost.
WHY_IT_MATTERS: >
  Undetected duplicate claims are one of the simplest and most common forms of expense cost
  inflation.
DISCONFIRMING_OBSERVATION: >
  The same receipt submitted twice against the same project is approved and counted twice in the
  project's cost total with no duplicate detection.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit the identical receipt twice against the same project and observe whether duplication is
  detected before both are counted.
```

## G12-PROJECT_HR_EXPENSE-Q030

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q030
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A manager's own expense, when billed to a project that manager also approves expenses for, is
  subject to a documented escalation to a different approver rather than a self-approval.
WHY_IT_MATTERS: >
  Self-approval on cost the approver personally benefits from removes the basic separation of duties
  the approval control exists to provide.
DISCONFIRMING_OBSERVATION: >
  A manager's own expense claim against a project they approve for is approved by that same manager
  with no escalation.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Submit an expense from a manager account against a project that manager is also the designated
  approver for, and observe whether approval escalates.
```

## G12-PROJECT_HR_EXPENSE-Q031

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q031
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The expense date shown to a customer on billing documentation is the date the cost was actually
  incurred, not the date it happened to be approved or posted.
WHY_IT_MATTERS: >
  A billing document that misstates when a cost was incurred can misrepresent the timeline of work
  to the customer.
DISCONFIRMING_OBSERVATION: >
  A customer-facing billing document shows an expense's approval or posting date rather than the
  date the cost was actually incurred.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Incur an expense on one date, approve it on a later date, bill it to the customer, and inspect
  which date the billing document displays.
```

## G12-PROJECT_HR_EXPENSE-Q032

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q032
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A retention policy that would purge an expense's supporting attachment is prevented, or requires an
  explicit hold, once that expense has already been billed to a customer.
WHY_IT_MATTERS: >
  Losing the ability to substantiate an already-billed cost leaves the business unable to defend that
  charge if the customer later disputes it.
DISCONFIRMING_OBSERVATION: >
  A billed expense's supporting attachment is purged under a general retention policy with no
  distinguishing hold for already-billed items.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Bill an expense with an attached receipt to a customer, then let the general retention policy's
  purge window elapse and check whether the attachment is protected.
```

## G12-PROJECT_HR_EXPENSE-Q033

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q033
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A currency-conversion discrepancy between the amount reimbursed to an employee and the amount
  recognized as project cost is visible and explained, not a silent, unexplained gap.
WHY_IT_MATTERS: >
  An unexplained gap between reimbursement and project cost invites suspicion of an error even when
  the underlying conversion logic was actually correct.
DISCONFIRMING_OBSERVATION: >
  The reimbursed amount and the project-recognized cost for the same foreign-currency expense differ,
  with no visible explanation for the gap.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reimburse a foreign-currency expense and compare the reimbursed amount to the project-recognized
  cost, checking for an accompanying explanation of any difference.
```

## G12-PROJECT_HR_EXPENSE-Q034

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q034
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A recurring or template-based expense automatically generated on a schedule is not attributed to a
  project without the same review step a manually entered expense would go through.
WHY_IT_MATTERS: >
  An automated expense that skips review is an unmonitored, recurring channel for cost to enter a
  project's budget.
DISCONFIRMING_OBSERVATION: >
  A recurring, automatically generated expense is attributed to a project and included in its cost
  with no review step applied.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Set up a recurring expense template attributed to a project, let it fire automatically, and inspect
  whether it went through the normal review step.
```

## G12-PROJECT_HR_EXPENSE-Q035

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q035
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An expense claimed against a project that is only placed on hold, rather than fully closed or
  archived, is handled by a defined behaviour that is distinct from either the fully active or the
  fully closed case.
WHY_IT_MATTERS: >
  An undefined middle state between active and closed leaves an on-hold project's expense handling
  unpredictable exactly when it most needs to be clear.
DISCONFIRMING_OBSERVATION: >
  An expense submitted against an on-hold project is treated identically to one submitted against a
  fully active project, with no distinguishing behaviour for the hold state.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place a project on hold, submit an expense against it, and compare the handling to both a fully
  active and a fully closed equivalent case.
```

## G12-PROJECT_HR_EXPENSE-Q036

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q036
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A negative expense entry, such as a credit, refund, or correction, reduces a project's cost through
  the same traceable, auditable path as a positive entry, not through an untracked manual adjustment.
WHY_IT_MATTERS: >
  A cost-reducing entry made outside the normal traceable path is just as capable of misstating
  project cost as an untracked cost-increasing one.
DISCONFIRMING_OBSERVATION: >
  A negative expense entry reduces a project's cost total with no corresponding traceable record
  comparable to a positive entry's.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Submit a negative (credit or correction) expense entry against a project and inspect its
  traceability compared to an ordinary positive entry.
```

## G12-PROJECT_HR_EXPENSE-Q037

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q037
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A project cost dashboard's reflection of a newly approved expense has a bounded, predictable
  refresh behaviour, with some indication of currency (how current the figure is), rather than
  indefinite staleness with no way to tell when it last updated.
WHY_IT_MATTERS: >
  A dashboard figure with no indication of staleness can be trusted or distrusted with equal, and
  equally unwarranted, confidence.
DISCONFIRMING_OBSERVATION: >
  A newly approved expense fails to appear on the project cost dashboard within any bounded,
  documented time, and the dashboard gives no indication of how current its figures are.
EXPECTED_SURFACE: S1,S5,S8
PRECONDITIONS: >
  Approve an expense against a project and monitor how and when the project cost dashboard reflects
  it, noting any staleness indicator.
```

## G12-PROJECT_HR_EXPENSE-Q038

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q038
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Once an expense line's project attribution is set, changing it afterward is itself an action
  captured in the audit trail, not a silent background correction with no trace.
WHY_IT_MATTERS: >
  A silently corrected attribution removes the ability to later tell whether a cost was always meant
  for its final project or was moved there after the fact.
DISCONFIRMING_OBSERVATION: >
  An expense line's project attribution changes with no corresponding entry in the audit trail
  showing the change occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change an already-set project attribution on an expense line and inspect the audit trail for a
  record of that specific change.
```

## G12-PROJECT_HR_EXPENSE-Q039

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q039
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An expense report submitted covering a period before the employee was staffed on the named project
  produces a flagged inconsistency, rather than being accepted silently as if the staffing had always
  existed.
WHY_IT_MATTERS: >
  A claim covering a period with no staffing basis is a plausible sign of a misattributed or
  fraudulent claim that deserves at least a flag.
DISCONFIRMING_OBSERVATION: >
  An expense dated before the employee's staffing start on a project is accepted and attributed with
  no flag or inconsistency noted.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Stage an employee's project staffing to begin on a known date, then submit an expense dated before
  that date against the same project.
```

## G12-PROJECT_HR_EXPENSE-Q040

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q040
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A bulk-approval action covering many expense lines across different projects produces per-project,
  per-line audit detail, not a single undifferentiated bulk log entry.
WHY_IT_MATTERS: >
  A single bulk log entry makes it impossible to review afterward which specific lines and projects
  were actually affected by that one action.
DISCONFIRMING_OBSERVATION: >
  A bulk approval spanning multiple projects produces one generic log entry with no way to see which
  specific lines and projects were included.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Perform a bulk approval covering expense lines attributed to several different projects and inspect
  the resulting audit detail.
```

## G12-PROJECT_HR_EXPENSE-Q041

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q041
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A currency loss or gain arising between the currency an expense was claimed in and the project's
  own cost currency is recorded as a distinct, visible figure, rather than absorbed silently into the
  base cost amount.
WHY_IT_MATTERS: >
  Hiding a currency gain or loss inside the base cost figure prevents anyone from distinguishing real
  spend from a currency-movement artifact.
DISCONFIRMING_OBSERVATION: >
  A currency gain or loss on a converted expense is not shown as a separate, identifiable figure
  anywhere in the project's cost record.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cause a currency movement between an expense's claim date and its recognition in project cost, and
  inspect whether the resulting gain or loss is separately visible.
```

## G12-PROJECT_HR_EXPENSE-Q042

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q042
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An expense explicitly marked as not to be billed to the customer cannot later be included on a
  customer invoice without an explicit override step distinct from ordinary invoicing.
WHY_IT_MATTERS: >
  A non-billable marking that can be silently ignored during invoicing provides no real assurance
  that internal cost stays internal.
DISCONFIRMING_OBSERVATION: >
  An expense marked not billable to the customer appears on a customer invoice with no explicit
  override step having occurred.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Mark an expense explicitly as not billable, then attempt to include it on a customer invoice.
```

## G12-PROJECT_HR_EXPENSE-Q043

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q043
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The set of employees permitted to log an expense against a given project is itself governed by a
  defined, auditable scope, not left open to anyone who happens to know the project's identifier.
WHY_IT_MATTERS: >
  An open scope for who can charge cost to a project means the project's own team roster provides no
  actual protection over its budget.
DISCONFIRMING_OBSERVATION: >
  An employee with no defined relationship to a project is able to log an expense against it purely
  by knowing or guessing its identifier.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  From an employee account with no assigned relationship to a project, attempt to log an expense
  against that project using only its identifier.
```

## G12-PROJECT_HR_EXPENSE-Q044

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q044
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an expense report requires a second-level approver once it exceeds a defined threshold, an
  expense attributed to a project cannot bypass that threshold check by being split into several
  smaller submissions.
WHY_IT_MATTERS: >
  A threshold that can be defeated by splitting a claim into pieces gives no real ceiling on
  unsupervised cost.
DISCONFIRMING_OBSERVATION: >
  Several smaller expense submissions that together exceed the second-level approval threshold, all
  attributed to the same project, are each approved without ever triggering the second-level step.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Submit several smaller expenses against the same project whose combined total exceeds the
  second-level approval threshold and observe whether the threshold check is triggered.
```

## G12-PROJECT_HR_EXPENSE-Q045

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q045
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A project archived mid-cycle while expense claims are still pending approval leaves those claims in
  a defined, discoverable state, rather than silently losing them from view.
WHY_IT_MATTERS: >
  A pending claim that disappears when its project is archived leaves an employee unreimbursed with
  no visible record of why.
DISCONFIRMING_OBSERVATION: >
  Archiving a project with pending expense claims makes those claims undiscoverable through any
  normal pending-approval view.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Archive a project that has expense claims still pending approval and check whether those claims
  remain discoverable.
```

## G12-PROJECT_HR_EXPENSE-Q046

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q046
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The complete lifecycle of a billable expense — logged, approved, attributed to a project, and
  invoiced to the customer — can be reconstructed end to end from stored records alone.
WHY_IT_MATTERS: >
  This is the exact chain a customer billing dispute would need reconstructed; a gap anywhere in it
  leaves the charge undefendable.
DISCONFIRMING_OBSERVATION: >
  Attempting to reconstruct the full lifecycle of a billed expense from logging through invoicing
  leaves a gap that stored records alone cannot fill.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Take a billable expense through logging, approval, project attribution, and customer invoicing,
  then attempt to reconstruct the full chain from stored records alone.
```

## G12-PROJECT_HR_EXPENSE-Q047

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q047
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An expense entry's association with a specific project task, rather than the project as a whole, is
  preserved through that task's own rename or re-parenting to a different phase or milestone.
WHY_IT_MATTERS: >
  A task-level cost link that breaks on a routine rename or reorganization loses exactly the
  granularity it was created to provide.
DISCONFIRMING_OBSERVATION: >
  An expense previously linked to a specific task loses that link, or shows an incorrect one, after
  the task is renamed or re-parented.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Link an expense to a specific project task, then rename or re-parent that task to a different phase
  and re-check the expense's task-level link.
```

## G12-PROJECT_HR_EXPENSE-Q048

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q048
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a project defines its own expense policy (allowed categories, spending caps) stricter than
  the general company expense policy, the project's stricter rule is what is actually enforced when
  an expense is attributed to it, not the more permissive general default silently winning.
WHY_IT_MATTERS: >
  A project-specific control that the general default can silently override provides no real
  protection, only the appearance of one.
DISCONFIRMING_OBSERVATION: >
  An expense that violates a project's own stricter policy is accepted because it satisfies the more
  permissive general company policy instead.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a project-specific expense policy stricter than the general company policy, then submit
  an expense that violates only the project-specific rule.
```

## G12-PROJECT_HR_EXPENSE-Q049

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q049
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An expense flagged for a compliance or travel-policy exception review is not billed to the customer
  until that review concludes.
WHY_IT_MATTERS: >
  Billing a customer for a cost still under a compliance exception review risks charging for
  something that review may ultimately disallow.
DISCONFIRMING_OBSERVATION: >
  An expense still flagged for an unresolved compliance or policy-exception review is billed to the
  customer before that review concludes.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Flag an expense for a compliance or policy-exception review, leave the review unresolved, and
  attempt to bill it to the customer.
```

## G12-PROJECT_HR_EXPENSE-Q050

```yaml
QID: G12-PROJECT_HR_EXPENSE-Q050
MODULE: project_hr_expense
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where an expense's original claim currency, the employee's home reimbursement currency, and the
  project's own reporting currency are all different, each conversion step used to arrive at the
  final project-reported figure is individually identifiable, not collapsed into one unexplained
  combined rate.
WHY_IT_MATTERS: >
  A three-currency chain collapsed into a single unexplained figure cannot be checked or defended if
  any one of the underlying rates is later questioned.
DISCONFIRMING_OBSERVATION: >
  For an expense involving three distinct currencies across claim, reimbursement, and project
  reporting, the individual conversion steps cannot be separately identified from the final reported
  figure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct a case where the claim currency, reimbursement currency, and project reporting currency
  are all different, then attempt to identify each individual conversion step behind the final
  reported cost.
```
