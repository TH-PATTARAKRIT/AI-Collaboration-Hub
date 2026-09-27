# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_sale_expense Module MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_SALE_EXPENSE-MVQ48-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `project_sale_expense`
**Wave:** W3
**Author Cell:** P12-4 (GMVQ Question Factory — Production Cell P12-4)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

Per the Group Brief, `project_sale_expense` is treated as a 2-way bridge: project on one side, and
the already-integrated capability of re-invoicing an incurred expense to a customer through a sale
document ("sale-driven expense") on the other, treated as a single unit. Every question below fails
the seam test with a NO — each depends on the re-invoicing process actually being tied to a
project's task, budget, or margin, not merely to an order in isolation.

This bank does not restate the pure sale+project seam (order confirmation, cancellation, budget
derivation — that belongs to `sale_project`, G08) or the pure sale+expense seam (approval,
re-invoicing basis, currency, tax on the re-invoiced line, with no project in the loop — that
belongs to `sale_expense`, G08). Every question here specifically needs the project's own task,
budget, or margin view to make sense.

Question text is source-neutral: no vendor or product name, no technical identifier, and no
reference to the module's own metadata name.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because each tests a distinct material hypothesis.
- Pre-authoring check performed: `grep -h HYPOTHESIS` across `G08_SALE_PROJECT` (order+project,
  no expense) and `G08_SALE_EXPENSE` / `G08_SALE_EXPENSE_MARGIN` (order+expense re-invoicing, no
  project) confirmed neither asks about a project's own task-level attribution, margin, or budget
  interacting with expense re-invoicing. No overlap found.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G12-PROJECT_SALE_EXPENSE-Q001

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q001
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An expense captured against a specific project task carries that task-level attribution through
  to the point it is re-invoiced to the customer, not only a project-level attribution with the task
  detail lost.
WHY_IT_MATTERS: >
  Losing task-level attribution at billing prevents the project from later understanding which task
  actually drove a given re-invoiced cost.
DISCONFIRMING_OBSERVATION: >
  A re-invoiced expense line traces back only to the project as a whole, with no way to identify
  which specific task it was originally attributed to.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attribute an expense to a specific project task, carry it through to re-invoicing, and check
  whether the task-level detail is still traceable from the resulting invoice line.
```

## G12-PROJECT_SALE_EXPENSE-Q002

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q002
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project's own profitability report reflects both a re-invoiced expense's cost and its billed
  revenue as two separately visible figures, not netted into a single number that hides the markup
  actually realized.
WHY_IT_MATTERS: >
  Netting cost and revenue into one figure hides whether the project is actually recovering its
  markup or merely breaking even on re-invoiced expenses.
DISCONFIRMING_OBSERVATION: >
  The project's profitability report shows only one combined figure for a re-invoiced expense, with
  no separate cost and revenue lines.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Re-invoice an expense at a markup through a project and check whether the project's profitability
  report shows cost and revenue separately.
```

## G12-PROJECT_SALE_EXPENSE-Q003

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q003
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a re-invoicing markup rate can be set at the level of the specific project rather than only
  at the level of the customer contract, the project-level rate takes precedence through one
  documented, consistent rule when the two would otherwise disagree.
WHY_IT_MATTERS: >
  An undocumented precedence between a project-level and contract-level markup makes the actually
  billed rate unpredictable and unauditable.
DISCONFIRMING_OBSERVATION: >
  Two comparable expenses under the same project and contract, both eligible for either markup rate,
  are billed at different rates with no documented reason.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set a project-level markup rate that differs from the customer contract's own rate, re-invoice an
  expense under the project, and observe which rate is applied.
```

## G12-PROJECT_SALE_EXPENSE-Q004

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q004
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An expense attributed to a project task that is later deemed out of scope and removed from the
  project results in the expense being flagged for review rather than silently invoiced against a
  task that no longer exists.
WHY_IT_MATTERS: >
  Silently invoicing against a removed task can bill the customer for work the project no longer
  actually recognizes as part of its own scope.
DISCONFIRMING_OBSERVATION: >
  A task is removed from project scope while it has an attributed, not-yet-billed expense, and the
  expense is re-invoiced with no flag connecting it to the removed task.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Remove a project task from scope after an expense has already been attributed to it, and observe
  whether the expense is flagged before re-invoicing.
```

## G12-PROJECT_SALE_EXPENSE-Q005

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q005
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Deleting a project task after an expense attributed to it has already been re-invoiced to the
  customer does not remove the historical record of which task the billed expense actually related
  to.
WHY_IT_MATTERS: >
  Losing that historical link makes a later billing dispute or margin review unable to explain what
  work the charge actually corresponded to.
DISCONFIRMING_OBSERVATION: >
  After the funding task is deleted, the already-issued invoice line for the expense no longer shows
  any trace of which task it originally related to.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Re-invoice an expense attributed to a task, delete the task, and check the invoice line's
  historical task reference.
```

## G12-PROJECT_SALE_EXPENSE-Q006

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q006
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where one expense is split for billing across two different tasks within the same project, the
  sum billed across both tasks equals the original expense amount.
WHY_IT_MATTERS: >
  A split that does not sum to the original either bills the customer for money never spent or
  writes off spend that was never actually recovered.
DISCONFIRMING_OBSERVATION: >
  The sum of the two task-level billed amounts from a split expense does not equal the original
  expense's total amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split one expense across two tasks within the same project for billing purposes, and sum the two
  resulting billed amounts against the original.
```

## G12-PROJECT_SALE_EXPENSE-Q007

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q007
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A project placed on hold does not, by itself, block an already-approved, already-attributed
  expense from completing its re-invoicing to the customer, unless a documented rule explicitly ties
  billing to project status.
WHY_IT_MATTERS: >
  An undocumented, automatic block on billing when a project pauses can delay legitimate revenue
  recovery for reasons unrelated to the expense's own approval status.
DISCONFIRMING_OBSERVATION: >
  Putting the project on hold blocks an already-approved expense's re-invoicing with no documented
  rule stating that project status governs billing eligibility.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Approve an expense for re-invoicing, then put its project on hold, and observe whether the
  re-invoicing still proceeds.
```

## G12-PROJECT_SALE_EXPENSE-Q008

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q008
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Closing a project while an approved expense attributed to one of its tasks has not yet been
  re-invoiced either blocks closure or leaves that pending re-invoicing explicitly flagged.
WHY_IT_MATTERS: >
  A closed project with a silently unresolved, billable expense is revenue the business may never
  actually collect.
DISCONFIRMING_OBSERVATION: >
  A project closes with an approved, not-yet-billed expense attached to one of its tasks, and the
  closed project shows no flag for the pending billing.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attempt to close a project that has an approved but not-yet-re-invoiced expense on one of its
  tasks, and observe the outcome.
```

## G12-PROJECT_SALE_EXPENSE-Q009

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q009
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project's completion percentage or margin figure, once an expense has been re-invoiced against
  it, is not silently recalculated backward if the underlying expense is later reclassified as
  non-billable.
WHY_IT_MATTERS: >
  Silently recalculating an already-reported historical margin figure misrepresents what was
  actually known and reported at the time.
DISCONFIRMING_OBSERVATION: >
  Reclassifying an already-billed expense as non-billable changes the project's previously reported
  margin figure for a period that has already closed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Re-invoice an expense against a project, record the resulting margin, then reclassify the expense
  as non-billable, and re-check the previously reported margin.
```

## G12-PROJECT_SALE_EXPENSE-Q010

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q010
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Someone permitted to view a project's overall cost and margin, but with no permission over the
  customer's own commercial pricing, does not see the customer-facing billed amount for a
  re-invoiced expense through the project view alone.
WHY_IT_MATTERS: >
  Commercial pricing exposed through an unrelated project-cost view leaks sensitive customer terms
  to people who were never granted that access.
DISCONFIRMING_OBSERVATION: >
  A user with project-cost-only access can see the customer-facing billed amount for a re-invoiced
  expense by navigating through the project's own cost view.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  As a user with project cost-view access only, attempt to see the customer-facing billed amount for
  a re-invoiced expense through the project's own view.
```

## G12-PROJECT_SALE_EXPENSE-Q011

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q011
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A currency mismatch between the expense's original currency, the project's own reporting currency,
  and the customer's billing currency is resolved through one documented rate and moment applied
  consistently to both the project's cost figure and the customer's billed figure.
WHY_IT_MATTERS: >
  Two different conversion moments for the same expense produce a project cost figure and a customer
  billed figure that disagree for reasons unrelated to the actual markup applied.
DISCONFIRMING_OBSERVATION: >
  The project's own reported cost for a re-invoiced expense and the customer's actual billed amount,
  once both converted to one reference currency, disagree by more than the intended markup.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Capture an expense in one currency, re-invoice it to a customer billed in a different currency
  under a project with a third reporting currency, and reconcile all three figures.
```

## G12-PROJECT_SALE_EXPENSE-Q012

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q012
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Duplicating a project to plan a similar future engagement does not cause the duplicate to inherit
  a live reference to an expense already re-invoiced under the original project.
WHY_IT_MATTERS: >
  A live reference in the duplicate would make a brand-new, unstarted project appear to already have
  billed revenue and recognized cost.
DISCONFIRMING_OBSERVATION: >
  The duplicated project shows the original project's already re-invoiced expense as its own current
  billing activity.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Duplicate a project that has an already re-invoiced expense, and inspect the duplicate's own
  billing references.
```

## G12-PROJECT_SALE_EXPENSE-Q013

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q013
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a project draws expenses toward billing under more than one linked customer arrangement, an
  expense attributed to the project alone (with no specific arrangement chosen) is resolved to
  exactly one billing destination, not silently duplicated across more than one.
WHY_IT_MATTERS: >
  Duplicated billing across more than one customer arrangement for the same expense overcharges the
  customer relationship and overstates recovered revenue.
DISCONFIRMING_OBSERVATION: >
  An expense attributed only to the project, with no chosen arrangement, is re-invoiced onto more
  than one of the project's linked customer arrangements.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attribute an expense to a project that has more than one linked customer arrangement, with no
  specific arrangement chosen, and observe where it is billed.
```

## G12-PROJECT_SALE_EXPENSE-Q014

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q014
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Rejecting an expense as fraudulent or policy-violating after it has already been re-invoiced to
  the customer through the project results in a documented correction path rather than leaving the
  project's reported margin based on a rejected expense.
WHY_IT_MATTERS: >
  A margin figure left standing on a rejected, fraudulent expense misstates the project's true
  performance and the correction owed to the customer.
DISCONFIRMING_OBSERVATION: >
  An expense is rejected as fraudulent after being re-invoiced, and the project's reported margin
  still reflects it with no correction recorded.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Re-invoice an expense through a project, then reject the underlying expense as fraudulent, and
  check the project's margin report for a correction.
```

## G12-PROJECT_SALE_EXPENSE-Q015

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q015
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A project's own billing milestones and an expense's own independent re-invoicing trigger are
  reconciled to one governing rule for which actually causes the customer invoice to be issued,
  rather than both silently attempting to trigger it.
WHY_IT_MATTERS: >
  Two independent triggers both attempting to cause billing risks issuing the customer two separate
  invoices for what should be one charge.
DISCONFIRMING_OBSERVATION: >
  Reaching a project billing milestone and an expense's own re-invoicing trigger both fire, and both
  produce separate invoice activity for the same underlying charge.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set up a project with a billing milestone and an independently billable expense reaching its
  trigger at the same time, and observe how many invoices result.
```

## G12-PROJECT_SALE_EXPENSE-Q016

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q016
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An expense re-invoiced through a project retains a traceable link back to both the specific
  project task and the specific customer invoice line, so the connection survives even if either the
  task or the invoice is later renumbered.
WHY_IT_MATTERS: >
  Losing the link when either side is renumbered makes it impossible to later reconstruct which
  invoice line paid for which piece of project work.
DISCONFIRMING_OBSERVATION: >
  After the task or the invoice is renumbered, the re-invoiced expense's link between the two can no
  longer be traced.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Re-invoice an expense through a project task, renumber either the task or the resulting invoice,
  and check whether the link between them still resolves.
```

## G12-PROJECT_SALE_EXPENSE-Q017

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q017
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a project spans more than one company entity in a multi-company setup, an expense captured
  under one company but attributed to a project owned by another company follows a documented
  inter-company step before it is billable to the end customer.
WHY_IT_MATTERS: >
  Billing the end customer before the inter-company step completes can charge the customer for a
  cost that has not yet actually been recognized between the two internal entities.
DISCONFIRMING_OBSERVATION: >
  An expense captured under one company, attributed to a project owned by a different company, is
  re-invoiced to the end customer with no inter-company step having occurred.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Capture an expense under one company entity and attribute it to a project owned by a different
  entity, then trace whether an inter-company step is required before customer billing.
```

## G12-PROJECT_SALE_EXPENSE-Q018

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q018
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A project archived after its expected active life, receiving a late-submitted expense report
  referencing one of its now-archived tasks, either reopens the project through a documented path or
  routes the expense for separate handling rather than silently failing to attribute it.
WHY_IT_MATTERS: >
  Silently failing to attribute a late expense loses both the cost record and the customer's
  chargeable revenue for legitimate, already-incurred work.
DISCONFIRMING_OBSERVATION: >
  A late expense report referencing an archived project's task is submitted and neither reopens the
  project nor is routed anywhere for handling.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Archive a project, then submit a late expense report referencing one of its tasks, and observe
  what happens to it.
```

## G12-PROJECT_SALE_EXPENSE-Q019

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q019
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two employees each submitting an expense against the same project task at nearly the same time do
  not result in one expense silently overwriting or being merged into the other before either
  reaches re-invoicing.
WHY_IT_MATTERS: >
  Silently merging or overwriting one of two genuinely distinct expenses loses a legitimate cost and
  understates what the project actually incurred.
DISCONFIRMING_OBSERVATION: >
  After two employees submit separate expenses against the same task at nearly the same time, only
  one expense is visible for re-invoicing.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Submit two separate expenses from two employees against the same project task at nearly the same
  time, and verify both remain distinctly recorded.
```

## G12-PROJECT_SALE_EXPENSE-Q020

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q020
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project's margin report, when it includes both timesheet-based billing and expense-based
  re-invoicing for the same task, attributes each billed amount to its own correct source rather
  than conflating the two into one undifferentiated revenue line.
WHY_IT_MATTERS: >
  Conflating the two sources hides whether the project's margin is actually driven by labor recovery
  or by expense markup, obscuring where true profitability comes from.
DISCONFIRMING_OBSERVATION: >
  A task billed through both timesheet time and a re-invoiced expense shows one combined revenue
  figure in the margin report with no breakdown by source.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Bill one project task through both timesheet time and a re-invoiced expense, and check whether the
  margin report distinguishes the two revenue sources.
```

## G12-PROJECT_SALE_EXPENSE-Q021

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q021
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reassigning an expense originally attributed to one project's task to a different project's task
  after the fact leaves a traceable record of the reassignment and its date.
WHY_IT_MATTERS: >
  Without a traceable reassignment record, neither project's historical cost report can later
  explain why its figures changed.
DISCONFIRMING_OBSERVATION: >
  An expense reassigned between two project tasks shows no record of when the reassignment occurred
  or what its original attribution had been.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Reassign an already-attributed expense from one project task to a task on a different project, and
  check for an audit record of the change.
```

## G12-PROJECT_SALE_EXPENSE-Q022

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q022
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A markup rate change applied at the project level after some of the project's expenses have
  already been re-invoiced under the previous rate does not retroactively alter the already-issued
  customer invoice lines.
WHY_IT_MATTERS: >
  Retroactively altering an already-issued invoice line changes a document the customer has already
  received and may have already acted on.
DISCONFIRMING_OBSERVATION: >
  Changing the project's markup rate alters the amount shown on an invoice line that was already
  issued under the previous rate.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Re-invoice an expense under one project-level markup rate, then change the rate, and check whether
  the already-issued invoice line's amount changes.
```

## G12-PROJECT_SALE_EXPENSE-Q023

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q023
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where the project's own assigned manager and the underlying expense's approver are two different
  people, the system does not require the project manager's approval to also serve as the expense's
  own policy approval, keeping the two checks independent.
WHY_IT_MATTERS: >
  Collapsing the two approvals lets a project manager single-handedly clear an expense that the
  expense policy itself requires a separate check on.
DISCONFIRMING_OBSERVATION: >
  A project manager's own approval of a project-level action also satisfies the expense's own
  required policy approval with no separate check occurring.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a project manager, approve a project-level action tied to an unapproved expense, and check
  whether the expense's own separate policy approval is still required.
```

## G12-PROJECT_SALE_EXPENSE-Q024

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q024
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A negative or corrective expense line recorded against a project task after the original expense
  was already re-invoiced results in a visible, traceable credit or adjustment rather than a silent
  rewrite of the original billed amount.
WHY_IT_MATTERS: >
  A silent rewrite of an already-billed amount destroys the ability to later explain why a
  historical invoice no longer matches what was originally issued.
DISCONFIRMING_OBSERVATION: >
  A corrective expense line changes the project's already re-invoiced figure with no visible credit
  or adjustment entry marking that a correction occurred.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Add a corrective expense line against a task after its original expense was already re-invoiced,
  and check for a visible adjustment record.
```

## G12-PROJECT_SALE_EXPENSE-Q025

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q025
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An expense attributed to a project task funded by more than one customer arrangement, where the
  arrangements have different markup rates, is billed at a documented, resolved rate rather than an
  ambiguous or arbitrarily chosen one.
WHY_IT_MATTERS: >
  An arbitrarily chosen rate among several possible arrangements makes the actually billed amount
  unpredictable and potentially inconsistent with what either arrangement specifies.
DISCONFIRMING_OBSERVATION: >
  An expense eligible for billing under two arrangements with different markup rates is billed at a
  rate that matches neither arrangement's own documented rate.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attribute an expense to a task funded by two customer arrangements with different markup rates,
  and check which rate is actually applied.
```

## G12-PROJECT_SALE_EXPENSE-Q026

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q026
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project's non-billable classification, applied at the project level to mark the whole engagement
  as internal, is honored by an expense attributed to one of its tasks, blocking that expense from
  ever reaching re-invoicing regardless of the expense's own billable flag.
WHY_IT_MATTERS: >
  An expense's own billable flag overriding the project's internal classification would bill an
  internal, non-chargeable engagement's customer by mistake.
DISCONFIRMING_OBSERVATION: >
  An expense flagged billable on its own is re-invoiced to a customer despite being attributed to a
  project classified as non-billable at the project level.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Classify a project as non-billable, then attribute a billable-flagged expense to one of its tasks,
  and observe whether re-invoicing proceeds.
```

## G12-PROJECT_SALE_EXPENSE-Q027

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q027
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling a customer arrangement linked to a project after some of the project's expenses have
  already been re-invoiced against it does not retroactively unbill or hide those already-issued
  charges from the project's own historical cost report.
WHY_IT_MATTERS: >
  Retroactively hiding already-issued charges when the underlying arrangement is cancelled
  misrepresents the project's actual historical billing activity.
DISCONFIRMING_OBSERVATION: >
  Cancelling the customer arrangement removes already-issued, re-invoiced expense charges from the
  project's historical cost report.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Re-invoice expenses against a project's customer arrangement, cancel the arrangement, and check the
  project's historical cost report for those charges.
```

## G12-PROJECT_SALE_EXPENSE-Q028

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q028
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An expense report submitted under an automated, no-human-review approval path is subject to the
  same project-task attribution and billing eligibility rules as one requiring manual approval.
WHY_IT_MATTERS: >
  An automated path exempted from attribution and eligibility rules becomes an unmonitored route for
  incorrect or premature customer billing.
DISCONFIRMING_OBSERVATION: >
  An expense approved through an automated path is re-invoiced despite failing an attribution or
  eligibility rule that a manually approved equivalent would have been stopped by.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Submit a comparable expense through both the automated approval path and manual approval, each
  failing the same attribution or eligibility rule, and compare outcomes.
```

## G12-PROJECT_SALE_EXPENSE-Q029

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q029
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a project task is merged into a different task after an expense was already attributed and
  re-invoiced against the original task, the expense's task reference updates to the surviving task.
WHY_IT_MATTERS: >
  A reference left pointing at an absorbed task makes the merged task's billed history look
  incomplete and the old task's history look like an unexplained orphan.
DISCONFIRMING_OBSERVATION: >
  After two tasks are merged, an expense originally attributed and re-invoiced against the absorbed
  task still references that absorbed task rather than the surviving one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Merge two project tasks where one already has a re-invoiced expense attributed to it, and check the
  expense's task reference afterward.
```

## G12-PROJECT_SALE_EXPENSE-Q030

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q030
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  At project closure, reconciling every expense attributed to its tasks against what was actually
  re-invoiced to the customer identifies any approved, billable expense that was never actually
  billed.
WHY_IT_MATTERS: >
  An unreconciled, never-billed but billable expense left behind at closure is revenue the business
  earned but will never actually collect.
DISCONFIRMING_OBSERVATION: >
  A project closes with an approved, billable expense that was never actually re-invoiced, and no
  reconciliation step surfaces that gap.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close a project that has at least one approved, billable expense never re-invoiced, and check
  whether closure surfaces that gap.
```

## G12-PROJECT_SALE_EXPENSE-Q031

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q031
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A receipt or supporting document attached to an expense that is later re-invoiced through a
  project is not itself exposed on the customer-facing invoice, only the commercially relevant
  description and amount.
WHY_IT_MATTERS: >
  Exposing the original receipt to the customer can leak internal pricing, unrelated personal
  details, or the identity of the employee who incurred the cost.
DISCONFIRMING_OBSERVATION: >
  The customer-facing invoice for a re-invoiced expense includes the original receipt or its
  underlying supporting document.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Re-invoice an expense that has an attached receipt through a project, and inspect what the
  customer-facing invoice actually exposes.
```

## G12-PROJECT_SALE_EXPENSE-Q032

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q032
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where several employees' expenses attributed to the same project task are consolidated onto one
  customer-facing invoice line, that consolidated line still preserves, in the underlying project
  record, which individual expenses it represents.
WHY_IT_MATTERS: >
  Losing the breakdown behind a consolidated line makes it impossible to later verify or dispute any
  one employee's contribution to the billed total.
DISCONFIRMING_OBSERVATION: >
  A consolidated invoice line for several employees' expenses cannot be traced back, in the project's
  own record, to the individual expenses it represents.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consolidate several employees' expenses attributed to the same task onto one invoice line, and
  check whether the project's own record still shows the individual breakdown.
```

## G12-PROJECT_SALE_EXPENSE-Q033

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q033
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A project's reported margin, calculated before an attributed expense's re-invoicing has actually
  completed, is distinguishable in reporting from margin calculated after the billing has actually
  occurred.
WHY_IT_MATTERS: >
  An indistinguishable figure lets a provisional, unbilled margin be mistaken for a confirmed,
  actually recovered one.
DISCONFIRMING_OBSERVATION: >
  The project's margin figure looks identical whether or not the attributed expense's re-invoicing
  has actually completed.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Compare a project's reported margin before an attributed expense is re-invoiced and again after
  billing actually completes.
```

## G12-PROJECT_SALE_EXPENSE-Q034

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q034
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An expense originally captured with no project reference, later manually attributed to a project's
  task after the fact, is recorded so that the attribution's creation date is distinguishable from
  the expense's original submission date.
WHY_IT_MATTERS: >
  Without distinguishing the two dates, a project's cost history can appear to have always included
  an expense that was only attributed to it much later.
DISCONFIRMING_OBSERVATION: >
  An expense manually attributed to a project long after submission shows the project's cost history
  as if the attribution had always existed, with no separate record of when it was made.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Capture an expense with no project reference, wait, then manually attribute it to a project task,
  and inspect the audit trail for both dates.
```

## G12-PROJECT_SALE_EXPENSE-Q035

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q035
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where the customer arrangement linked to a project changes its own re-invoicing basis (cost,
  markup, or fixed price) mid-project, already-attributed but not-yet-billed expenses follow one
  documented rule for whether they adopt the new basis or remain under the old one.
WHY_IT_MATTERS: >
  An undocumented, inconsistent transition leaves some pending expenses billed under one basis and
  others under a different one with no explainable reason.
DISCONFIRMING_OBSERVATION: >
  Two comparable, already-attributed but not-yet-billed expenses under the same mid-project basis
  change are billed under different bases with no documented rule explaining the split.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a project's linked customer arrangement's re-invoicing basis mid-project while expenses are
  already attributed but unbilled, and observe which basis applies to them.
```

## G12-PROJECT_SALE_EXPENSE-Q036

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q036
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project task's estimated cost, once an actual expense is attributed and re-invoiced against it,
  does not silently overwrite the original estimate, keeping the estimate and the actual separately
  visible.
WHY_IT_MATTERS: >
  Overwriting the estimate destroys the ability to later compare planned against actual, defeating
  the purpose of estimating.
DISCONFIRMING_OBSERVATION: >
  After an expense is attributed and re-invoiced against a task, the task's originally recorded
  estimate can no longer be viewed separately from the actual figure.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Record a task's cost estimate, attribute and re-invoice an actual expense against it, and check
  whether the original estimate remains separately viewable.
```

## G12-PROJECT_SALE_EXPENSE-Q037

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q037
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Withdrawal of a project's billing authorization after an expense has already been submitted and
  approved for that project's task does not retroactively re-invoice or automatically release the
  pending expense without an explicit, separate action.
WHY_IT_MATTERS: >
  An automatic, silent release or billing of a pending expense when authorization is withdrawn can
  bill a customer the business no longer intends to bill, or the reverse.
DISCONFIRMING_OBSERVATION: >
  Withdrawing the project's billing authorization changes the pending expense's own billing state
  with no separate, explicit action having been taken.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Withdraw a project's billing authorization after an expense was already approved for one of its
  tasks, and observe the expense's own resulting state.
```

## G12-PROJECT_SALE_EXPENSE-Q038

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q038
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where one project's task depends on an expense attributed but re-invoicing is deferred until a
  documented milestone, the deferred expense remains visible in the project's cost report as an
  incurred but not-yet-billed cost, not absent from the report entirely.
WHY_IT_MATTERS: >
  An absent, invisible deferred cost understates the project's true incurred spend until the
  milestone is finally reached.
DISCONFIRMING_OBSERVATION: >
  An expense attributed to a task but deferred for billing until a later milestone does not appear
  anywhere in the project's cost report until the milestone is reached.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Attribute an expense to a task with billing deferred to a documented milestone, and check whether
  the project's cost report shows it before the milestone is reached.
```

## G12-PROJECT_SALE_EXPENSE-Q039

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q039
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A project spanning a jurisdiction different from the expense's originating jurisdiction applies
  one documented, consistently applied tax treatment to the re-invoiced amount.
WHY_IT_MATTERS: >
  An inconsistent tax treatment across jurisdictions on project-linked, re-invoiced expenses risks
  misstated tax liability that surfaces only at audit.
DISCONFIRMING_OBSERVATION: >
  Two comparable, project-linked expenses re-invoiced across the same pair of jurisdictions are taxed
  under two different, undocumented treatments.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Re-invoice comparable expenses for two projects spanning jurisdictions different from the
  expense's own originating jurisdiction, and compare the tax treatment applied to each.
```

## G12-PROJECT_SALE_EXPENSE-Q040

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q040
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reopening a closed project to attribute and bill a late-arriving expense is a recorded action —
  who reopened it and when — rather than an unaudited change to a previously closed record.
WHY_IT_MATTERS: >
  An unaudited reopening of a closed project undermines closure as a control checkpoint and hides
  who decided to revisit it.
DISCONFIRMING_OBSERVATION: >
  A previously closed project is reopened to bill a late expense, and no audit entry shows who
  reopened it or when.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Reopen a closed project to attribute and bill a late-arriving expense, and check the audit trail
  for the reopening action.
```

## G12-PROJECT_SALE_EXPENSE-Q041

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q041
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A project's task-level expense budget being exceeded by a newly attributed expense produces one
  documented, consistent system behaviour (block, warn, or flag) rather than varying case to case.
WHY_IT_MATTERS: >
  An inconsistent response to breaching a task-level expense budget makes the control's effect
  depend on unrelated factors rather than the actual breach.
DISCONFIRMING_OBSERVATION: >
  Two comparable expenses that each breach their task's own expense budget by a similar margin
  produce two different system responses with no documented reason for the difference.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Attribute two comparable expenses that each breach a different task's own expense budget, and
  compare the resulting system behaviour.
```

## G12-PROJECT_SALE_EXPENSE-Q042

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q042
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Full or partial write-off of an expense that was never actually re-invoiced, recorded against a
  project task, is distinguishable in the project's cost report from an expense that was
  successfully billed.
WHY_IT_MATTERS: >
  Conflating a written-off, never-recovered cost with a successfully billed one misrepresents how
  much of the project's incurred cost was actually recovered from the customer.
DISCONFIRMING_OBSERVATION: >
  The project's cost report shows a written-off, never-billed expense identically to one that was
  actually billed and collected.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Write off an expense against a task that was never actually re-invoiced, and compare its
  appearance in the cost report against a successfully billed expense.
```

## G12-PROJECT_SALE_EXPENSE-Q043

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q043
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where two separate projects each attribute a portion of one shared, jointly-incurred expense, the
  sum attributed across both projects equals the original expense amount, with no portion silently
  duplicated or lost.
WHY_IT_MATTERS: >
  A duplicated or lost portion across two projects either overstates one project's cost or
  understates the true joint spend the business actually incurred.
DISCONFIRMING_OBSERVATION: >
  The sum of the amounts attributed to two projects sharing one jointly-incurred expense does not
  equal the original expense's total.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split one shared, jointly-incurred expense across two different projects, and sum the two
  resulting attributed amounts against the original.
```

## G12-PROJECT_SALE_EXPENSE-Q044

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q044
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project's own currency, distinct from the expense's original submission currency, does not cause
  the project's reported cost for that expense to disagree with the amount actually re-invoiced to
  the customer once both are converted to the same reference currency.
WHY_IT_MATTERS: >
  A currency-driven disagreement between reported cost and actual billed amount, once reconciled to
  one reference currency, would misstate the project's true recovered margin.
DISCONFIRMING_OBSERVATION: >
  The project's reported cost for an expense and the amount actually re-invoiced, once both converted
  to one common reference currency, disagree by more than the intended markup.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Capture an expense in a currency different from the project's own reporting currency, re-invoice
  it, and reconcile the project's reported cost against the actual billed amount in one common
  currency.
```

## G12-PROJECT_SALE_EXPENSE-Q045

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q045
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An expense attributed to a project task and flagged billable, but for which the linked customer
  arrangement has since been fully closed and locked, either blocks the billing with a clear reason
  or routes it through a documented exception path.
WHY_IT_MATTERS: >
  Proceeding to bill against a closed, locked arrangement with no explanation confuses whoever is
  trying to understand why a supposedly closed arrangement still shows activity.
DISCONFIRMING_OBSERVATION: >
  A billable expense proceeds to invoice against a customer arrangement that is already closed and
  locked, with no blocking reason or documented exception path shown.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to re-invoice a billable expense whose linked customer arrangement has already been closed
  and locked, and observe the outcome.
```

## G12-PROJECT_SALE_EXPENSE-Q046

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q046
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project template applied to create a new project does not carry forward a live reference to
  expenses that were actually re-invoiced under the original project the template was derived from.
WHY_IT_MATTERS: >
  A live reference in a template-created project would make a brand-new engagement appear to
  already have billed revenue from an entirely unrelated, earlier project.
DISCONFIRMING_OBSERVATION: >
  A project created from a template shows a previously re-invoiced expense from the template's
  source project as its own current billing activity.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a project template from a project with already re-invoiced expenses, apply the template to
  create a new project, and inspect the new project's billing references.
```

## G12-PROJECT_SALE_EXPENSE-Q047

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q047
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Concurrent edits to a project task's billable-expense budget and to an individual expense's own
  billable flag at nearly the same moment do not result in one change being silently discarded.
WHY_IT_MATTERS: >
  A silently discarded concurrent edit leaves one of the two editors believing their change took
  effect when it did not, with no error to alert them.
DISCONFIRMING_OBSERVATION: >
  After two near-simultaneous edits, one to a task's billable-expense budget and one to an expense's
  own billable flag, one of the two changes is missing with no conflict notice shown.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Simulate two users editing, at nearly the same time, a task's billable-expense budget and an
  attributed expense's own billable flag, then verify both changes persisted.
```

## G12-PROJECT_SALE_EXPENSE-Q048

```yaml
QID: G12-PROJECT_SALE_EXPENSE-Q048
MODULE: project_sale_expense
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a project's task requires multiple approval steps before an attributed expense becomes
  billable, a partial approval does not make that expense appear on a customer-facing invoice as
  though it were fully cleared.
WHY_IT_MATTERS: >
  Billing a customer for an only-partially-approved expense charges them before the business itself
  has actually finished clearing that cost internally.
DISCONFIRMING_OBSERVATION: >
  An expense that has completed only one of several required approval steps appears on a
  customer-facing invoice as though fully approved.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Advance an expense through only one of several required approval steps, and check whether it
  reaches the customer-facing invoice.
```
