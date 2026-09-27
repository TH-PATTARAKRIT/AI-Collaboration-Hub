# SMEsPlus ENTERPRISE SUITE
## GMVQ — G15 PRODUCTIVITY / spreadsheet_dashboard_hr_expense Module Bridge MVQ Bank

**Document ID:** GMVQ-G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-MVQ50-V1.00
**Group:** G15 PRODUCTIVITY (Wave W4)
**Module Metadata:** `spreadsheet_dashboard_hr_expense`
**Wave:** W4
**Author Cell:** P15-2 (GMVQ Question Factory — Wave W4 Acceleration, Cell P15-2)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 50 = 105
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `spreadsheet_dashboard_hr_expense` — a 2-way
BRIDGE per GMVQ_BRIDGE_MODULE_RULE_V1.00 and GROUP_BRIEF_G15_PRODUCTIVITY.md, seam: a live
collaborative dashboard drawing rollups and tiles from expense-report data it does not itself own.
The underlying expense report's own submission, approval-chain mechanics, and reimbursement
lifecycle belong to the expense-tracking base family and are deliberately NOT re-asked here.
This bank asks only what becomes true or uncertain **because a dashboard layer sits on top of**
that data: staleness of cached or scheduled rollups against a live source; aggregation that
exposes individual-level detail through small-group rollups, rankings, or drill-down; real-time
versus batch-refresh mismatch; cross-record and cross-boundary summation that should not have
happened at the reporting layer; and whether dashboard access itself is mistaken for, or grants,
an action the source module gates behind its own permission model. Every question was tested
against the bridge rule: if it would read equally well with no dashboard in the picture at all —
i.e. it is really a question about expense approval, reimbursement, or categorization on its own —
it was cut.

The question text is source-neutral and does not expose vendor or product names, field names,
methods, schema, XML IDs, API shapes, or implementation algorithms. `MODULE:
spreadsheet_dashboard_hr_expense` appears only in the structured metadata field, never inside
question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` stating a concrete failure state,
  never a restatement of its own hypothesis.
- No padding: 50 questions exist because they test 50 distinct material hypotheses at the seam
  between a reporting/dashboard layer and expense-report data; none was trimmed or stretched to
  hit count.
- BRIDGE MODULE per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question fails only at the seam. None
  restates an expense submission, approval-workflow, or reimbursement invariant that holds with no
  dashboard layer present.
- Mandatory pre-authoring sibling check performed: `01_QUESTION_BANKS/G15_PRODUCTIVITY/` held no
  sibling files on disk at authoring time (checked directly). Overlap against this cell's own
  `spreadsheet_dashboard_hr_timesheet`, `spreadsheet_dashboard_im_livechat`, and
  `spreadsheet_dashboard_sale` drafts was checked directly against their HYPOTHESIS text at
  authoring time; no overlap found.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/evidence.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q001

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q001
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rollup total shown by department does not become an effective disclosure of one individual's
  spending when that department has few enough members that the total identifies a single person.
WHY_IT_MATTERS: >
  Aggregation is supposed to protect individual detail; a small-group total that identifies one
  person defeats that protection while still looking like a safe, aggregate figure.
DISCONFIRMING_OBSERVATION: >
  A department or grouping with a single member (or an otherwise identifying membership) is shown
  the same unmasked total as a large department, effectively revealing that individual's amount.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure or locate a department/cost-center grouping with one or very few members and compare
  its rollup presentation against a large department's rollup on the same dashboard.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q002

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q002
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A tile counting expenses awaiting approval reflects the current state of the source records, not
  a count computed before a recent approval or rejection took effect.
WHY_IT_MATTERS: >
  A stale pending count causes an approver to under- or over-estimate their actual workload and can
  leave a viewer believing an item is still open when it has already been resolved.
DISCONFIRMING_OBSERVATION: >
  A pending-approval tile continues to show a count including an expense that was approved or
  rejected moments earlier, past any refresh window the dashboard claims to honor.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Note the pending-approval tile's value, approve or reject one qualifying expense, then reload the
  tile within its stated refresh interval and compare.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q003

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q003
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Drilling from an aggregate expense tile into the underlying record list enforces the same
  "own records or direct reports only" restriction that the source list view enforces, not a
  broader default scope introduced by the reporting layer.
WHY_IT_MATTERS: >
  A reporting layer that is more permissive than the record it reports on turns an aggregate view
  into a backdoor around the source module's own access control.
DISCONFIRMING_OBSERVATION: >
  A viewer restricted to their own or their reports' expenses reaches, via a drill-down click, an
  underlying record list containing someone else's expenses they could not open directly.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a viewer with a restricted approval/visibility scope, drill down from an aggregate tile and
  inspect the full set of records the resulting list actually contains.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q004

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q004
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A currency-converted total combines rows using one consistent, disclosed exchange-rate basis
  (such as a rate as of the report date, or as of the aggregation date) rather than mixing
  different rate bases silently across the rows being summed.
WHY_IT_MATTERS: >
  A total built from inconsistent rate bases is not a real number; it cannot be reconciled to any
  single source of truth and misstates spend without any visible sign that it has done so.
DISCONFIRMING_OBSERVATION: >
  Two expenses in different currencies entered on different dates are found to have been converted
  using two different, undisclosed rate bases within the same summed total.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Enter multi-currency expenses on different dates, wait for or trigger any applicable rate change,
  and inspect how the converted total was derived.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q005

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q005
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An expense rejected after already being counted in a period snapshot is excluded from later
  renders of that same snapshot's total, rather than the rejected amount remaining permanently
  baked into a figure presented as current.
WHY_IT_MATTERS: >
  A total that never sheds a rejected amount silently overstates spend indefinitely, and no
  reconciliation against the source will ever explain the gap.
DISCONFIRMING_OBSERVATION: >
  A period total computed after an expense's rejection still includes that expense's amount when
  the dashboard is reloaded or its scheduled refresh runs again.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Let an expense be counted in a period rollup, reject it, and re-render or re-trigger the rollup
  for the same period.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q006

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q006
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard refreshed on a schedule rather than live visibly discloses the point in time its data
  reflects, so a viewer cannot mistake a batch-refreshed figure for a real-time one.
WHY_IT_MATTERS: >
  A viewer who believes a stale figure is live will make an approval or budget decision on data
  that no longer matches the source.
DISCONFIRMING_OBSERVATION: >
  A dashboard built on a scheduled refresh presents its figures with no visible "as of" marker,
  timestamp, or other indication that they are not current to the moment of viewing.
EXPECTED_SURFACE: S5,S8
PRECONDITIONS: >
  Identify a dashboard widget known to refresh on a schedule and inspect whether its presentation
  discloses the data's effective timestamp.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q007

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q007
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An expense still in an unsubmitted, draft state does not appear in a rollup intended to represent
  committed spend.
WHY_IT_MATTERS: >
  Counting draft entries as committed spend overstates a budget position before anyone has actually
  chosen to submit that cost.
DISCONFIRMING_OBSERVATION: >
  A "committed spend" or equivalent total on the dashboard changes as soon as a draft expense is
  created, before it has been submitted.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a new expense and leave it in draft, then check whether a committed-spend aggregate moved.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q008

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q008
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Two viewers with different approval or visibility scopes see totals from the same dashboard
  widget scoped to what each is individually authorized to see, rather than one shared number
  computed under a single, broader scope.
WHY_IT_MATTERS: >
  A dashboard that computes one number for everyone regardless of who is looking either
  under-reports to the privileged viewer or over-discloses to the restricted one.
DISCONFIRMING_OBSERVATION: >
  Two accounts with genuinely different visibility scopes are shown the identical total from the
  same widget, where the correct scoped totals would differ.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Load the same dashboard widget as two viewers with different, known visibility scopes and compare
  the values shown.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q009

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q009
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A dashboard combining spend across more than one company or legal entity does not silently sum
  figures that should remain entity-scoped unless the viewer holds explicit cross-entity
  visibility.
WHY_IT_MATTERS: >
  Summing across entity boundaries without authorization exposes one entity's spend pattern to
  users of another and can misstate figures relied on for entity-level reporting.
DISCONFIRMING_OBSERVATION: >
  A viewer scoped to a single entity is shown, or a total silently includes, spend belonging to a
  different entity they hold no cross-entity right to see.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  In a multi-entity configuration, view a spend dashboard as a single-entity-scoped user and check
  whether any total includes another entity's figures.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q010

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q010
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an expense's category is changed after the fact, a category-based rollup reflects the
  corrected category rather than the classification in force when the rollup was last computed.
WHY_IT_MATTERS: >
  A category rollup that never absorbs a reclassification silently misattributes spend to the wrong
  budget line indefinitely.
DISCONFIRMING_OBSERVATION: >
  An expense reclassified from one category to another continues to appear under its old category
  in a rollup rendered after the reclassification.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reclassify an already-counted expense's category and re-render the category rollup.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q011

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q011
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard's aggregate value does not mix pre-edit and post-edit amounts of the same record
  within a single computed number when the underlying record is being edited concurrently with the
  aggregation.
WHY_IT_MATTERS: >
  A total that partially reflects two different states of the same record is internally
  inconsistent and cannot be reconciled against either state.
DISCONFIRMING_OBSERVATION: >
  A total computed while an expense's amount is being edited reflects neither the pre-edit nor the
  saved post-edit amount cleanly, or differs from both on repeated identical recomputation.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a dashboard recomputation at the same time an expense amount is being saved and inspect
  the resulting total for internal consistency.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q012

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q012
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Deactivating or archiving an employee record does not remove that employee's already-counted
  historical contribution from a period-based aggregate that included it before deactivation.
WHY_IT_MATTERS: >
  Historical spend totals should not shrink retroactively just because the person who incurred the
  cost has since left; that would misstate closed-period figures.
DISCONFIRMING_OBSERVATION: >
  A closed-period aggregate's total drops after the contributing employee's record is deactivated,
  with no corresponding change to the underlying expense records.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Deactivate an employee whose expenses are already reflected in a closed-period aggregate and
  re-render that aggregate.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q013

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q013
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rollup grouped by approver does not expose an employee's specific reporting-line manager to a
  viewer who is not otherwise entitled to see that reporting relationship.
WHY_IT_MATTERS: >
  Reporting-line information is organizationally sensitive; a dashboard grouping is not a licence
  to disclose it beyond whatever channel normally carries it.
DISCONFIRMING_OBSERVATION: >
  A viewer with no access to organizational reporting-line data can determine an employee's
  approver identity purely from an approver-grouped dashboard rollup.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a viewer without reporting-line visibility, inspect an approver-grouped rollup for any
  employee-to-approver linkage it exposes.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q014

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q014
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Sharing or exporting a dashboard snapshot does not carry forward access to underlying attachments
  (such as receipts) that the recipient of the snapshot is not independently authorized to open.
WHY_IT_MATTERS: >
  A snapshot meant to share summary figures becomes an unintended document-leak channel if it also
  hands out access to restricted source attachments.
DISCONFIRMING_OBSERVATION: >
  A recipient of a shared or exported dashboard snapshot can open an underlying receipt or
  attachment they could not access directly through the source module.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Share or export a dashboard snapshot to a recipient with no direct access to the source expense
  records and attempt to open a linked attachment from the snapshot.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q015

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q015
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A refund or reversal of a previously reimbursed expense appears as a distinct, visible adjustment
  in any aggregate that had already counted the original reimbursement, rather than silently
  overwriting the earlier figure with no trace.
WHY_IT_MATTERS: >
  A silent overwrite makes it impossible to explain, later, why a historical total changed or to
  audit that a reversal actually occurred.
DISCONFIRMING_OBSERVATION: >
  A reimbursement total changes after a reversal with no separate, inspectable record of the
  reversal itself anywhere in the aggregate's supporting detail.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reverse a previously reimbursed expense and inspect the aggregate before and after for a visible
  adjustment trail.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q016

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q016
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A "top spender" or similar ranking view does not surface an individual's identity to a viewer
  whose permission is limited to non-attributed, aggregate-only figures.
WHY_IT_MATTERS: >
  A ranking is individual-level disclosure by definition; presenting it to a viewer who should only
  see aggregates defeats the access model at the reporting layer.
DISCONFIRMING_OBSERVATION: >
  A viewer restricted to aggregate-only visibility can see a named individual attached to a ranked
  spend figure.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As an aggregate-only-scoped viewer, open any ranking or "top spender" style widget and check for
  named attribution.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q017

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q017
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When the underlying approval-workflow configuration changes (such as adding a required approval
  step), a historical aggregate already computed under the prior configuration is not silently
  recomputed as though the new rule had always applied.
WHY_IT_MATTERS: >
  Re-baselining history under a rule that did not exist at the time misrepresents what actually
  happened during that period.
DISCONFIRMING_OBSERVATION: >
  A historical period's "approved" total changes after an approval-workflow configuration change,
  with no expense in that period actually re-approved.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a historical approved-total figure, change the approval-workflow configuration, and
  re-render the same historical period's aggregate.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q018

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q018
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A real-time counter for "awaiting my approval" only counts records the current viewer is actually
  the assigned approver for, not all pending records across the organization.
WHY_IT_MATTERS: >
  An inflated "my" counter that actually reflects everyone's queue misleads an approver about their
  own workload and can mask records genuinely needing another approver's attention.
DISCONFIRMING_OBSERVATION: >
  Two approvers with disjoint queues are shown the identical "awaiting my approval" count, or a
  viewer's count includes records assigned to someone else.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Compare the "awaiting my approval" counter across two accounts known to have different assigned
  queues.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q019

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q019
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A period-over-period comparison widget uses the same fiscal period-boundary definition the source
  expense records use, not a differing definition introduced independently by the reporting layer.
WHY_IT_MATTERS: >
  A boundary mismatch silently shifts amounts between periods in the report that never actually
  moved in the underlying records, breaking reconciliation.
DISCONFIRMING_OBSERVATION: >
  An expense recorded just inside one fiscal period boundary is attributed to the adjacent period by
  the dashboard's comparison widget.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record an expense dated at a fiscal period boundary and compare its period attribution in the
  source record versus the dashboard's period-comparison widget.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q020

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q020
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An expense entered in a currency other than the reporting currency retains its original amount
  and currency alongside the converted figure in any drill-down, rather than the aggregate layer
  discarding the original values entirely.
WHY_IT_MATTERS: >
  Losing the original amount and currency makes it impossible to verify the conversion later or to
  reconcile against the employee's actual out-of-pocket currency.
DISCONFIRMING_OBSERVATION: >
  Drilling into a converted total's underlying record shows only the converted amount, with the
  original currency and amount nowhere visible.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Enter a foreign-currency expense, let it appear in a converted aggregate, then drill down and
  check whether the original amount and currency remain visible.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q021

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q021
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard tile aggregating by cost center either reflects a cost-center reassignment made after
  the expense was recorded, or clearly discloses which basis (original or current assignment) it is
  using, rather than leaving the basis unstated.
WHY_IT_MATTERS: >
  An unstated basis makes a cost-center total unverifiable and can silently misattribute spend to
  the wrong budget owner after a reassignment.
DISCONFIRMING_OBSERVATION: >
  A cost-center rollup's basis (original-at-entry versus current assignment) cannot be determined
  from the dashboard, and the two bases would produce different totals for a reassigned expense.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reassign an already-counted expense's cost center and compare the rollup's behaviour and any
  disclosure of which basis it used.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q022

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q022
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an underlying expense record's visibility is restricted (for example marked confidential),
  no aggregate exposes that expense's detail to a viewer who could not open the record directly.
WHY_IT_MATTERS: >
  A restricted record exists specifically to keep certain detail from certain viewers; an aggregate
  is not exempt from that restriction just because it summarizes rather than displays the record.
DISCONFIRMING_OBSERVATION: >
  A viewer who cannot open a restricted expense record can nonetheless infer or directly see its
  amount or category from a dashboard aggregate.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Mark an expense restricted/confidential, include it in a small enough group that its value is
  isolable, and check what an unauthorized viewer's aggregate reveals.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q023

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q023
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard that recalculates on a fixed schedule does not present a partially-updated aggregate,
  mid-refresh, as though it were a complete and internally consistent figure.
WHY_IT_MATTERS: >
  A partial figure presented as final can be acted on as if it were complete, when it actually
  reflects an arbitrary subset of the underlying records.
DISCONFIRMING_OBSERVATION: >
  A dashboard viewed during a scheduled refresh shows a total that is internally inconsistent with
  its own supporting detail, with no indication a refresh is in progress.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Observe a scheduled refresh in progress (or force one) and compare the aggregate shown mid-refresh
  against its supporting detail.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q024

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q024
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A viewer scoped to a single department's dashboard cannot infer another department's spend by
  cross-referencing an organization-wide total displayed alongside their own department's figure.
WHY_IT_MATTERS: >
  Placing a restricted-scope figure next to a broader total can let simple subtraction recover data
  the viewer was never meant to see.
DISCONFIRMING_OBSERVATION: >
  A department-scoped viewer can subtract their own department's disclosed total from a displayed
  organization-wide total to derive another department's figure with usable precision.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a single-department-scoped viewer, check whether the dashboard also displays an org-wide total
  alongside the department figure, and whether the remainder is derivable.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q025

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q025
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An aggregate figure computed before a bulk correction (such as a batch exchange-rate fix) is
  reconciled to reflect the correction, with the fact that a correction occurred left visible rather
  than the number simply drifting with no explanation.
WHY_IT_MATTERS: >
  An unexplained change to a previously reported figure undermines trust in every other number the
  dashboard has ever shown.
DISCONFIRMING_OBSERVATION: >
  A previously reported aggregate changes value after a bulk correction with no visible indication,
  anywhere in the dashboard, that a correction occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger or identify a bulk correction to previously aggregated data and check for a visible
  change-disclosure alongside the updated figure.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q026

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q026
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard widget filtered against specific employees or cost centers does not continue silently
  returning results for those references after the referenced records are deactivated or archived.
WHY_IT_MATTERS: >
  A filter silently keeping stale references produces results the configuration owner no longer
  intends and cannot explain by inspecting the current, active configuration.
DISCONFIRMING_OBSERVATION: >
  A widget filtered to a since-deactivated employee or cost center still returns data as though the
  filter reference were active, with no warning that the reference is stale.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Build a widget filtered to a specific employee or cost center, deactivate that reference, and
  re-render the widget.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q027

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q027
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two dashboard widgets built from the same expense data but refreshed at different times can
  disagree, and each is distinguishable by its own refresh timestamp rather than implying equal
  currency to the viewer.
WHY_IT_MATTERS: >
  Two disagreeing widgets with no way to tell which is more current leaves a viewer unable to decide
  which figure to trust.
DISCONFIRMING_OBSERVATION: >
  Two widgets on the same page show different totals for what should be the same underlying data,
  with no per-widget indication of each one's own refresh time.
EXPECTED_SURFACE: S5,S8
PRECONDITIONS: >
  Place two widgets covering overlapping data on refresh schedules that will drift apart, and
  compare their values and any per-widget timestamp.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q028

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q028
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling an entire expense report after its individual lines were already counted in an
  aggregate removes all of those lines from the aggregate, not merely the cancelled header record.
WHY_IT_MATTERS: >
  Leaving line-level amounts behind after their parent report is cancelled overstates spend by
  exactly the amount that was supposed to have been voided.
DISCONFIRMING_OBSERVATION: >
  An aggregate still includes one or more line amounts from a fully cancelled expense report.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel a multi-line expense report already reflected in an aggregate and re-render the aggregate.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q029

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q029
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Access to the dashboard does not itself grant an approval action; a viewer without approval
  authority cannot approve or reject an expense from within the dashboard even where the dashboard
  displays approval-related status.
WHY_IT_MATTERS: >
  A reporting surface that also exposes a live action control bypasses the separation between
  viewing and authorizing that the source module's permission model is built on.
DISCONFIRMING_OBSERVATION: >
  A viewer with dashboard access but no approval authority is able to trigger an approval or
  rejection action from within the dashboard interface.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a viewer with dashboard access but no approval authority, attempt to act on an approval-status
  element shown in the dashboard.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q030

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q030
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A drill-down link on an aggregate figure that no longer resolves to any record, because the
  underlying record was deleted, fails visibly rather than silently substituting a default value or
  a zero.
WHY_IT_MATTERS: >
  A silent substitution disguises a broken reference as legitimate data, hiding a data-integrity
  problem from anyone relying on the drill-down.
DISCONFIRMING_OBSERVATION: >
  Following a drill-down link to a deleted record produces a blank, zeroed, or otherwise plausible
  page instead of a visible error or not-found state.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Delete an expense record already referenced by a dashboard drill-down link and follow that link.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q031

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q031
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard grouped by employee that a non-manager viewer can access aggregates spend without
  exposing which specific employee corresponds to which value.
WHY_IT_MATTERS: >
  An employee-grouped view is individual-level by construction; giving it to a viewer without
  individual-level rights defeats the point of scoping them to aggregates.
DISCONFIRMING_OBSERVATION: >
  A non-manager viewer scoped to aggregate-only visibility can see a named-employee breakdown in an
  employee-grouped widget.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a non-manager, aggregate-scoped viewer, attempt to access or construct an employee-grouped
  breakdown.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q032

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q032
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where more than one approval stage exists, an "approved" bucket in an aggregate includes only
  expenses that have cleared every required stage, not merely the first.
WHY_IT_MATTERS: >
  Counting a partially approved expense as fully approved overstates confirmed, committed spend.
DISCONFIRMING_OBSERVATION: >
  An expense that has cleared only its first of several required approval stages appears in an
  "approved" total.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  In a multi-stage approval configuration, advance an expense through only the first stage and
  check whether it appears in a fully-approved aggregate.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q033

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q033
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard reporting an average expense amount does not misrepresent a distribution skewed by one
  unusually large expense as typical, and the underlying detail remains reachable to a viewer
  entitled to see it.
WHY_IT_MATTERS: >
  A single outlier can move an average enough to mislead about "typical" spend unless the dashboard
  surfaces the skew or the ability to inspect it.
DISCONFIRMING_OBSERVATION: >
  An average figure moves sharply due to one outlier expense with no way for an entitled viewer to
  discover or drill into that outlier from the average widget.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Introduce one unusually large expense into a group already shown as an average and check whether
  the outlier is discoverable from the average widget.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q034

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q034
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An expense report re-opened for correction after being marked paid is reflected in an aggregate in
  a way that is distinguishable from an expense that was paid and never subsequently touched.
WHY_IT_MATTERS: >
  Treating a reopened-and-corrected record identically to an untouched one hides that a paid amount
  was changed after payment, which is itself a fact worth being able to see.
DISCONFIRMING_OBSERVATION: >
  A reopened-then-corrected paid expense appears in every aggregate exactly as an untouched paid
  expense would, with no visible indication it was reopened.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reopen and correct a previously paid expense and compare its representation in aggregates against
  an untouched paid expense.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q035

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q035
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard shared with a party outside the organization does not expose more granular data than
  the sharing configuration intends, even where the underlying aggregate is built from individually
  restricted records.
WHY_IT_MATTERS: >
  External sharing is the highest-consequence disclosure boundary; a leak here reaches parties with
  no organizational relationship to fall back on.
DISCONFIRMING_OBSERVATION: >
  An externally shared dashboard link exposes a filter, drill-down, or export path reaching more
  granular data than the sharing configuration specified.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Configure an external share of a dashboard at a stated granularity and attempt to reach
  finer-grained data through any interactive control the shared view still offers.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q036

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q036
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where two duplicate expense records are later merged or one is voided, only one of the pair
  remains represented in any aggregate that had previously counted both.
WHY_IT_MATTERS: >
  A duplicate left counted twice after resolution silently overstates spend by exactly the
  duplicated amount.
DISCONFIRMING_OBSERVATION: >
  An aggregate still reflects both amounts of a pair after one has been voided or the pair merged
  into one record.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a duplicate pair already reflected separately in an aggregate, resolve the duplication, and
  re-render the aggregate.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q037

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q037
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A widget filtered to "this quarter" uses the fiscal-period definition configured for the
  organization, not a generic calendar quarter, when the organization's fiscal calendar differs from
  the calendar quarter.
WHY_IT_MATTERS: >
  A quarter widget built on the wrong calendar silently reports the wrong period to anyone relying on
  the organization's actual fiscal boundaries.
DISCONFIRMING_OBSERVATION: >
  In an organization with a non-calendar fiscal quarter, a "this quarter" widget's boundary dates do
  not match the configured fiscal quarter.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  In an organization configured with a non-calendar fiscal quarter, inspect a "this quarter" widget's
  actual date boundaries.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q038

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q038
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an expense's approver is reassigned to a different person, a "pending with me" aggregate
  updates to remove it from the original approver's queue rather than continuing to show it to both.
WHY_IT_MATTERS: >
  Showing a reassigned item to both approvers risks duplicate action or each assuming the other will
  act, leaving nobody actually responsible.
DISCONFIRMING_OBSERVATION: >
  After an approver reassignment, both the original and the new approver see the same expense in
  their respective "pending with me" aggregates.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Reassign a pending expense's approver and compare "pending with me" aggregates for both the
  original and new approver.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q039

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q039
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard total that blends reimbursable and non-reimbursable expense categories is clearly
  labeled as a blended figure, rather than being presented as a single unqualified "spend" number.
WHY_IT_MATTERS: >
  An unlabeled blend can be mistaken for a purely reimbursable total, misinforming a budget or
  cash-outlay decision.
DISCONFIRMING_OBSERVATION: >
  A total combining reimbursable and non-reimbursable amounts carries no label or distinction
  indicating it is a blend of the two.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Locate or configure a total spanning both reimbursable and non-reimbursable categories and inspect
  its labeling.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q040

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q040
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Concurrent approval actions by two managers on different lines of the same expense report at the
  same time do not produce an aggregate reflecting neither manager's final state.
WHY_IT_MATTERS: >
  A lost-update outcome under concurrency can leave a report's approval state inconsistent with what
  either manager actually decided.
DISCONFIRMING_OBSERVATION: >
  After two concurrent, non-conflicting approval actions on the same report, the resulting aggregate
  state matches neither manager's individually intended outcome.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Have two managers concurrently approve different lines of the same multi-line report and inspect
  the resulting aggregate state.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q041

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q041
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard configured to auto-refresh at a fixed interval marks itself visibly stale rather than
  silently continuing to display data past a failed refresh attempt.
WHY_IT_MATTERS: >
  Silent staleness after a failed refresh is indistinguishable from a genuinely current figure,
  removing the viewer's ability to know they should not trust it.
DISCONFIRMING_OBSERVATION: >
  A dashboard whose scheduled refresh fails continues to present its last-good figures with no
  visible staleness indicator.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Cause or simulate a refresh failure on an auto-refreshing widget and inspect the presentation
  afterward.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q042

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q042
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rollup exposed at a company-wide level does not carry department-level detail fine enough to
  reconstruct near-individual figures when a department's headcount is very small.
WHY_IT_MATTERS: >
  Fine-grained detail at the company level defeats the purpose of aggregating in the first place if
  it still lets a viewer reconstruct one person's figure.
DISCONFIRMING_OBSERVATION: >
  A company-wide rollup's department-level breakdown, combined with known small department
  headcount, allows recovery of an individual's amount.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Inspect a company-wide rollup's department-level granularity where at least one department has
  very few members.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q043

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q043
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An expense amount corrected after initial entry is reflected using the corrected amount in any
  aggregate computed after the correction, not the original erroneous amount.
WHY_IT_MATTERS: >
  Continuing to report a known-wrong amount after it has been fixed at the source defeats the point
  of allowing the correction at all.
DISCONFIRMING_OBSERVATION: >
  An aggregate rendered after an amount correction still reflects the original, uncorrected amount.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Correct an already-counted expense's amount and re-render any aggregate that includes it.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q044

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q044
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A viewer's ability to filter the dashboard by employee does not become a way to enumerate the full
  employee list beyond what that viewer would otherwise be authorized to browse.
WHY_IT_MATTERS: >
  A filter control with an unrestricted autocomplete or picklist can leak organizational headcount
  and names to a viewer who has no browsing right to that directory.
DISCONFIRMING_OBSERVATION: >
  A viewer with no employee-directory browsing right can enumerate employee names through the
  dashboard's employee filter control.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a viewer without directory-browsing rights, use the dashboard's employee filter and check what
  it allows them to enumerate.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q045

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q045
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A tile counting expenses "without a receipt attached" reflects the current attachment state of the
  source records, not a cached state from before a receipt was later added.
WHY_IT_MATTERS: >
  A stale "missing receipt" count can prompt unnecessary chasing of an employee who has already
  attached the required document.
DISCONFIRMING_OBSERVATION: >
  A missing-receipt tile continues to count an expense after a receipt has been attached to it,
  past any stated refresh window.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Attach a receipt to an expense already counted as missing one, then reload the tile within its
  refresh window.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q046

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q046
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard that serves data as of its last successful scheduled run continues to serve that data,
  clearly marked as such, if a subsequent scheduled refresh fails, rather than blanking out or
  throwing an error the viewer cannot interpret.
WHY_IT_MATTERS: >
  A dashboard that goes blank or errors uninformatively on a refresh failure denies the viewer any
  figure at all, when a clearly marked stale figure would still be useful.
DISCONFIRMING_OBSERVATION: >
  Following a refresh failure, the dashboard either shows no data or an uninterpretable error instead
  of the last-known-good figures with a staleness marker.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Simulate a scheduled-refresh failure and observe the dashboard's resulting presentation.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q047

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q047
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Reassigning an expense from one cost center to another after it was already reflected in that cost
  center's historical aggregate is handled by a defined rule — either retroactive reclassification
  or a point-in-time snapshot — rather than being left ambiguous between the two.
WHY_IT_MATTERS: >
  An undefined rule means two people reading the same historical figure at different times can
  legitimately disagree about what it should show, with neither provably wrong.
DISCONFIRMING_OBSERVATION: >
  Reassigning a historical expense's cost center produces a change in the historical aggregate that
  matches neither a stated retroactive rule nor a stated point-in-time snapshot rule.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reassign the cost center of an expense already reflected in a historical, closed-period aggregate
  and observe which rule (if either) the resulting change follows.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q048

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q048
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard combining current-year and prior-year expense totals for comparison correctly isolates
  each year's figures even where the prior year's period-closing process happened after some
  current-year data already existed.
WHY_IT_MATTERS: >
  A comparison that bleeds current-year activity into the prior-year figure, or vice versa,
  misstates the year-over-year trend it exists to show.
DISCONFIRMING_OBSERVATION: >
  A year-over-year comparison widget's prior-year figure changes after current-year data is entered,
  or the current-year figure includes activity dated in the prior year.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Enter current-year expenses after the prior year has closed and inspect a year-over-year comparison
  widget for cross-year bleed.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q049

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q049
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Exporting the dashboard's underlying data table to a shareable file does not bypass the same
  field-level restrictions (such as a hidden or masked amount) that apply when viewing the same data
  within the dashboard interface.
WHY_IT_MATTERS: >
  An export path that ignores field-level masking turns a properly restricted on-screen view into an
  unrestricted file the moment it is downloaded.
DISCONFIRMING_OBSERVATION: >
  A field masked or hidden in the dashboard's on-screen view appears unmasked in an exported file of
  the same data.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Identify a field masked or hidden on-screen for the current viewer, export the underlying data, and
  inspect the exported file for that field.
```

## G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q050

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_EXPENSE-Q050
MODULE: spreadsheet_dashboard_hr_expense
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A cached dashboard aggregate is invalidated and recomputed when the access-control configuration
  itself changes (such as a viewer's approval scope being reduced), rather than continuing to serve a
  total computed under the viewer's former, broader scope.
WHY_IT_MATTERS: >
  A cache that outlives a permission reduction hands a now-restricted viewer data their new,
  narrower scope should no longer include.
DISCONFIRMING_OBSERVATION: >
  A viewer whose approval or visibility scope has just been reduced still receives a cached
  aggregate reflecting their former, broader scope.
EXPECTED_SURFACE: S4,S8
PRECONDITIONS: >
  Reduce a viewer's approval/visibility scope after a cached aggregate has been computed for them,
  then reload the dashboard before any unrelated cache expiry.
```
