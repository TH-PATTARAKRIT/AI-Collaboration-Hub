# SMEsPlus ENTERPRISE SUITE
## GMVQ — G15 PRODUCTIVITY / spreadsheet_dashboard_sale_timesheet Module Bridge MVQ Bank

**Document ID:** GMVQ-G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-MVQ40-V1.00
**Group:** G15 PRODUCTIVITY
**Module Metadata:** `spreadsheet_dashboard_sale_timesheet`
**Wave:** W4 (GMVQ 25-Team Acceleration, 2026-09-27)
**Author Cell:** P15-3 (GMVQ Question Factory — Production Cell P15-3)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 40
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 40 = 95
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `spreadsheet_dashboard_sale_timesheet`, a three-participant seam (live dashboard reporting layer + billable timesheet/hours data + sale revenue data). Per GROUP_BRIEF_G15_PRODUCTIVITY.md this module carries HIGH ARITY-EXHAUSTION RISK and a specific duplicate-risk warning against its `spreadsheet_dashboard_sale` sibling: every question below asks specifically about time-based rollup exposure — the point where logged or approved hours are combined with sale-side revenue in a reporting widget — and was cut wherever it would still make sense as a plain sale-dashboard question with the timesheet participant removed, or a plain payroll/timesheet question with the sale participant removed. The material ground worked is staleness between the two source domains' refresh and approval cycles, permission leakage through aggregation (individual hourly cost or rate exposure through a rollup that was meant to be aggregate-only), real-time-versus-batch mismatch between hours logged and revenue invoiced, and cross-record rollup exposure — the four failure classes named in the Group Brief — plus reversal, correction, multi-currency, multi-tenant and billing-model handling (fixed-price versus time-and-materials, retainer arrangements) specific to this combination.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure state, never a restatement of its own hypothesis.
- Arity control: every question requires the dashboard/reporting layer AND timesheet-side state AND sale-side state simultaneously; a question answerable by any two of the three alone was rewritten to add the missing dependency or cut.
- No padding: authoring was stopped at 40 distinct material seam hypotheses rather than stretched to reach 48; see the Arity Exhaustion Statement below.
- Question text is source-neutral: no vendor or product name, no technical identifier, and the module's own metadata name never appears outside the `MODULE:` field.
- Checked against the Bridge Module Rule's seam dimensions (ordering, partiality, ownership, timing, reversal, quantity and money, lifecycle mismatch, error asymmetry, authority) before being kept, and cross-checked against the sibling `spreadsheet_dashboard_event_sale` bank's authored HYPOTHESIS lines to avoid restating a generic aggregation-leakage pattern without this module's own time-based dimension.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## ARITY EXHAUSTION STATEMENT

This bank reaches 40 material questions, short of the 48-question floor set by GMVQ_AUTHORING_STANDARD_V1.00 §2. This shortfall is reported honestly rather than closed with manufactured questions, consistent with the module's flagged HIGH ARITY-EXHAUSTION RISK status and GMVQ_BRIDGE_MODULE_RULE_V1.00 §7.

Reasoning: the 40 questions above already work every seam dimension in GMVQ_BRIDGE_MODULE_RULE_V1.00 §3 for this specific three-way combination — ORDERING and TIMING (approval lag before invoicing, retainer billed ahead of hours, period-boundary attribution), PARTIALITY (split installments, overlapping hours, shared retainer pools across two orders), OWNERSHIP (which record is authoritative when a manager overrides billed hours without touching the timesheet), REVERSAL (post-invoice timesheet correction, refund after billed hours, reversed approval after invoicing), QUANTITY AND MONEY (multi-currency conversion consistency, two cost rates under one sale, fixed-price versus time-and-materials blending), LIFECYCLE MISMATCH (offboarded employee history, deleted pre-approval entry, cancelled sale with logged hours), and a dense cluster of AGGREGATION/PERMISSION-LEAKAGE questions specific to hourly-cost exposure (small-team inference, cross-team leakage, hidden cost-rate exposure through export or drill-through, contractor-versus-employee rate blending) that this module's own vocabulary (individual hourly cost, not individual event payment) keeps distinct from the sibling event-sale bank.

Candidate ground considered and REJECTED as belonging to a narrower sibling bank, not this three-way bridge (fails the removal test):
- "Does the sale-side revenue dashboard total correctly for a client" with no timesheet or hours dimension attached — this is a `spreadsheet_dashboard_sale` question, explicitly the sibling the Group Brief warns against restating.
- "Is a submitted timesheet entry correctly routed for approval" with no sale or revenue dimension at all — this is a pure timesheet/HR-module question with no funding sale in the picture.
- "Does a dashboard widget support a custom date-range filter" — a dashboard-only configuration question with no timesheet participant, already the domain of the base `spreadsheet_dashboard` bank.

Candidate ground considered and REJECTED as duplicating the sibling `spreadsheet_dashboard_event_sale` bank's material:
- The generic "small-group aggregate discloses an individual figure through successive totals" pattern was kept in both banks only because each instance names this module's own distinct consequence (an employee's individual hourly cost, not an attendee's payment) and its own distinct trigger (team membership change, not a registration change) — not as a restated pair.

## Questions

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q001

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q001
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combined revenue-per-billable-hour widget does not count timesheet entries that have been submitted but not yet approved as already-billed hours contributing to realized revenue.
WHY_IT_MATTERS: >
  Counting unapproved hours as realized revenue would overstate actual billed income before the hours were ever confirmed.
DISCONFIRMING_OBSERVATION: >
  An unapproved, submitted timesheet entry is already included in the combined widget's realized-revenue-per-hour figure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Submit a timesheet entry without approving it, then check whether the combined widget's realized billed-revenue figure already includes it.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q002

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q002
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A viewer permitted to see aggregate revenue-per-project figures but not individual employee timesheets cannot use a narrow date or person filter on the combined widget to infer a single named employee's logged hours or hourly cost.
WHY_IT_MATTERS: >
  A rollup narrowed to one person functions as an individual disclosure and defeats the purpose of aggregate-only permission.
DISCONFIRMING_OBSERVATION: >
  Narrowing the combined widget's filter to a single employee reveals that employee's individual logged hours or cost to a viewer without timesheet-level permission.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Grant a user permission to view only aggregate project revenue, narrow the combined widget's filter to a single employee, and check whether individual hour or cost detail becomes visible.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q003

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q003
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The combined widget's hours-logged figure and its invoiced-revenue figure, when drawn from refresh cycles of different ages, are not presented as though both were captured at the same moment.
WHY_IT_MATTERS: >
  Presenting two figures of different ages as one coherent snapshot would mislead a viewer about how current the combined picture actually is.
DISCONFIRMING_OBSERVATION: >
  The widget shows hours-logged and invoiced-revenue figures of visibly different refresh ages with no indication of the age mismatch.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a refresh of only the timesheet-side or only the sale-side data feeding a combined widget, and check whether the displayed figure indicates the resulting age mismatch.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q004

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q004
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a timesheet entry is corrected after the corresponding sale has already been invoiced using the original hours, the combined dashboard reconciles the two rather than continuing to show the original hours against the corrected timesheet total with no note.
WHY_IT_MATTERS: >
  An unreconciled discrepancy between invoiced hours and corrected hours would leave the combined figure internally inconsistent with no way to tell which is authoritative.
DISCONFIRMING_OBSERVATION: >
  After a timesheet correction post-invoicing, the combined widget shows the original invoiced hours and the corrected timesheet total with no note reconciling the two.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Invoice a sale using an employee's originally logged hours, then correct the underlying timesheet entry, and check whether the combined widget reconciles the two figures.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q005

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q005
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined utilization-versus-revenue widget scoped to a manager's own team does not surface another team's employee-level hourly figures through a cross-team summary total.
WHY_IT_MATTERS: >
  A cross-team summary that leaks another team's employee-level detail would defeat the manager's own-team scoping.
DISCONFIRMING_OBSERVATION: >
  A manager scoped to their own team can see another team's employee-level hourly figures through a shared cross-team summary total.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Scope a manager's combined widget access to their own team, view a cross-team summary total, and check whether another team's employee-level figures are visible.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q006

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q006
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a sale bills a fixed price regardless of actual hours logged, the combined dashboard's per-hour revenue figure for that engagement is computed from and clearly distinguished as a fixed-price engagement, rather than blended with time-and-materials engagements into one indistinguishable per-hour average.
WHY_IT_MATTERS: >
  Blending fixed-price and time-and-materials work into one average would produce a per-hour figure that describes no real engagement type accurately.
DISCONFIRMING_OBSERVATION: >
  A fixed-price engagement's hours are averaged into the same per-hour revenue figure as time-and-materials engagements with no distinction between the two billing types.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Compare the combined widget's per-hour revenue figure for a fixed-price engagement against a time-and-materials engagement, and check whether the two are distinguished or blended.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q007

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q007
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined widget aggregating billable hours across a small team does not let a viewer with only aggregate-level permission back-calculate one employee's individual hours by comparing successive totals as team membership changes.
WHY_IT_MATTERS: >
  Successive small-team totals can reveal an individual's hours through subtraction even when no single figure names that employee directly.
DISCONFIRMING_OBSERVATION: >
  Comparing the combined team total before and after a membership change reveals an individual employee's exact logged hours to a viewer without individual-level permission.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Add or remove one employee from a small team feeding a combined widget, and check whether comparing the totals before and after reveals that employee's individual hours.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q008

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q008
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Deleting a timesheet entry after its hours were already included in an invoiced sale leaves the combined dashboard's historical revenue-per-hour figure for that period intact and referenced, rather than silently recalculating history with the entry missing.
WHY_IT_MATTERS: >
  Silently recalculating closed historical figures would erase a legitimate past record with no trace that a deletion occurred.
DISCONFIRMING_OBSERVATION: >
  After deleting an already-invoiced timesheet entry, the combined widget's historical revenue-per-hour figure for that period changes with no record of the deletion.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Delete a timesheet entry whose hours were already invoiced and reflected in a historical combined widget, and check whether that historical figure remains intact and traceable.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q009

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q009
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined dashboard exported to a shared file for a client does not include underlying named-employee hour detail when the live widget itself only shows the client an aggregate billed-hours total.
WHY_IT_MATTERS: >
  An export exposing more than the live view would hand a client individual employee data the dashboard was never designed to disclose to them.
DISCONFIRMING_OBSERVATION: >
  An exported combined dashboard sent to a client includes named-employee hour detail that the client's live widget view only ever showed as an aggregate total.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Export a combined widget configured for client-facing aggregate-only viewing, and compare the exported content against what the live client view actually shows.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q010

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q010
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an employee's logged hours are reassigned from one project's sale to another after the original invoice was issued, the combined widget's per-project revenue-per-hour figure reflects the reassignment consistently on both the source and destination project.
WHY_IT_MATTERS: >
  Updating only one side of a reassignment would leave one project overstated and the other understated relative to its actual hours.
DISCONFIRMING_OBSERVATION: >
  After a cross-project hour reassignment, the combined widget updates the destination project's figure but leaves the source project's figure unchanged, or the reverse.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reassign an employee's already-invoiced logged hours from one project's sale to another, and check whether both projects' combined revenue-per-hour figures update consistently.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q011

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q011
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The combined widget's hours-pending-approval category and its hours-already-invoiced category do not overlap, meaning an hour entry counted as billed revenue is not simultaneously shown as still awaiting approval in the same dashboard.
WHY_IT_MATTERS: >
  An hour appearing in both categories at once would make the dashboard internally contradictory about that hour's actual status.
DISCONFIRMING_OBSERVATION: >
  The same timesheet hour entry appears simultaneously in the combined widget's billed-revenue figure and its pending-approval figure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Track a single timesheet entry through approval and invoicing, and check whether it ever appears in both the pending-approval and already-invoiced categories at once.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q012

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q012
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a sale is fully or partially refunded after the timesheet hours behind it were already marked as billed, the combined dashboard's revenue-per-hour figure is adjusted to reflect the refund rather than continuing to treat the refunded amount as recognized revenue.
WHY_IT_MATTERS: >
  Continuing to count refunded revenue would overstate the actual income the billed hours produced.
DISCONFIRMING_OBSERVATION: >
  After a sale refund, the combined widget's revenue-per-hour figure still includes the refunded amount as recognized revenue against the same hours.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Refund a sale whose underlying timesheet hours were already marked as billed, and check whether the combined revenue-per-hour figure adjusts for the refund.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q013

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q013
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A manager viewing a combined team productivity widget scoped to their direct reports cannot see individual hourly cost-to-serve figures for an employee who does not report to them, even when that employee's hours were logged against a shared project the manager can otherwise see at the aggregate level.
WHY_IT_MATTERS: >
  A shared-project aggregate view that leaks an out-of-scope employee's individual cost figure would defeat the manager's own reporting-line scoping.
DISCONFIRMING_OBSERVATION: >
  A manager can see an out-of-scope employee's individual hourly cost figure through a shared project's combined widget, despite that employee not reporting to them.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Have an out-of-scope employee log hours against a project a manager can otherwise see, and check whether that employee's individual cost figure becomes visible to the manager.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q014

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q014
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A combined dashboard configured with a scheduled, non-real-time refresh clearly indicates that displayed billable-hours figures may not include entries logged since the last refresh, rather than implying the figure is current.
WHY_IT_MATTERS: >
  An unlabeled scheduled refresh would let a viewer mistake a stale snapshot for the current, complete picture.
DISCONFIRMING_OBSERVATION: >
  A combined widget on a scheduled refresh presents its billable-hours figure with no indication that entries logged since the last refresh are excluded.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a combined widget to refresh on a fixed schedule, log new hours after the last refresh, and check whether the displayed figure indicates it may be incomplete.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q015

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q015
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where two employees log overlapping hours against the same billable task due to a shared assignment, the combined revenue-per-hour widget does not silently double count the same billed amount against both employees' individual productivity figures.
WHY_IT_MATTERS: >
  Double counting one billed amount across two employees would overstate the true billed output attributed to the team.
DISCONFIRMING_OBSERVATION: >
  The same billed amount for a shared task appears in full against both employees' individual productivity figures in the combined widget.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Have two employees log overlapping hours against one shared billable task, and check whether the combined widget counts the resulting billed amount once or against both employees.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q016

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q016
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A combined widget grouping revenue by project does not misattribute an employee's hours, once corrected from a wrong project code, to the originally incorrect project's historical rollup after the correction was applied.
WHY_IT_MATTERS: >
  Retaining a corrected entry's history under the wrong project would leave that project's historical figures permanently inaccurate.
DISCONFIRMING_OBSERVATION: >
  After correcting an hour entry's project code, the combined widget's historical rollup for the originally incorrect project still includes that entry.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Correct an hour entry's project code after it was logged against the wrong project, and check whether the originally incorrect project's historical rollup still includes it.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q017

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q017
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a client-facing view of the combined dashboard is configured to hide internal hourly cost rate while showing billed amount, the underlying query behind the widget does not expose the hidden cost-rate figure through an export, API response, or drill-through path available to that same client view.
WHY_IT_MATTERS: >
  A hidden field still reachable through export or drill-through would leak internal cost information to a client the dashboard was designed to protect it from.
DISCONFIRMING_OBSERVATION: >
  A client-facing export, API response, or drill-through derived from the combined widget reveals the internal hourly cost rate that the live view was configured to hide.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Configure a client-facing combined widget to hide internal cost rate, then check whether an export, API response, or drill-through from that same view reveals it.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q018

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q018
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A combined dashboard's currency handling, where an employee logs hours priced internally in one currency and the client is invoiced in another, uses one documented, consistently applied conversion moment for the combined per-hour figure rather than mixing rates across the same rollup.
WHY_IT_MATTERS: >
  Mixing conversion moments within one rollup would make the combined per-hour figure numerically incoherent even though every underlying amount is individually correct.
DISCONFIRMING_OBSERVATION: >
  Two entries shown in the same combined per-hour rollup are converted between the internal and invoicing currencies using different exchange-rate moments.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Log hours priced internally in one currency for a client invoiced in another, and compare the conversion basis used across entries in the same combined widget.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q019

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q019
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a sale is billed in advance of the timesheet hours actually being logged, such as a retainer arrangement, the combined widget does not present a per-hour revenue figure computed against hours that have not yet occurred as though the rate were already confirmed.
WHY_IT_MATTERS: >
  Presenting a rate for hours that have not happened yet would overstate the certainty of a figure that depends entirely on future work.
DISCONFIRMING_OBSERVATION: >
  The combined widget shows a confirmed per-hour revenue figure for a retainer period before any of the corresponding hours have actually been logged.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Bill a retainer sale in advance of any hours being logged against it, and check whether the combined widget presents a confirmed per-hour figure before hours occur.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q020

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q020
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A combined widget's cache invalidation triggered by an approved timesheet correction also invalidates the sale-side revenue portion of the same cached rollup, rather than updating only the hours half.
WHY_IT_MATTERS: >
  Updating only one half of a cached combined figure would leave hours and revenue permanently out of step after a correction.
DISCONFIRMING_OBSERVATION: >
  After a timesheet correction triggers cache invalidation, the combined widget's hours figure updates but the revenue figure continues to reflect the stale cached value.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Correct an approved timesheet entry that triggers cache invalidation, and check whether both the hours and revenue portions of the combined rollup are refreshed.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q021

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q021
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where an employee is removed from a project after logging billable hours already reflected in the combined dashboard, historical rollups referencing that employee's hours remain intact and correctly attributed rather than disappearing or reassigning to a generic bucket.
WHY_IT_MATTERS: >
  Losing or reassigning an offboarded employee's historical attribution would corrupt a legitimate past record for no operational reason.
DISCONFIRMING_OBSERVATION: >
  After an employee is removed from a project, the combined widget's historical rollup for their previously logged hours either disappears or is reassigned to an unnamed generic bucket.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Remove an employee from a project after they logged billable hours reflected in a historical combined rollup, and check whether that historical attribution remains intact.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q022

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q022
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined dashboard comparing billed revenue per hour across multiple employees does not allow a viewer permitted to see only their own row to infer a colleague's exact figure from a visible team-average change when the team is small enough for the delta to reveal it.
WHY_IT_MATTERS: >
  A team average that shifts predictably with one person's change functions as an individual disclosure in a small enough team.
DISCONFIRMING_OBSERVATION: >
  A viewer permitted to see only their own row can determine a colleague's exact per-hour figure from a change in the visible small-team average.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  In a small team, change one employee's logged hours and observe whether a viewer scoped to their own row can infer that employee's figure from the resulting average change.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q023

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q023
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where hours are logged against a sale that is later cancelled entirely before invoicing, the combined dashboard removes that engagement's projected revenue-per-hour figure from any in-progress summary rather than leaving it counted as pending revenue indefinitely.
WHY_IT_MATTERS: >
  Leaving a cancelled engagement counted as pending revenue would overstate the team's actual expected income.
DISCONFIRMING_OBSERVATION: >
  After a sale is cancelled before invoicing, the combined widget's in-progress summary still counts that engagement's projected revenue as pending.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel a sale before invoicing after hours were already logged against it, and check whether the combined widget's in-progress summary still counts its projected revenue.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q024

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q024
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A combined widget built once and not updated when a project's billing rate configuration changes continues to use the rate in effect at the time each hour was actually logged, rather than silently retroactively repricing historical hours at the new rate.
WHY_IT_MATTERS: >
  Retroactively repricing historical hours would change previously reported revenue figures with no one having decided to revalue them.
DISCONFIRMING_OBSERVATION: >
  After a project's billing rate configuration changes, the combined widget's historical revenue-per-hour figures for previously logged hours change to reflect the new rate.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a project's billing rate configuration after hours were already logged and reflected in a historical combined widget, and check whether that historical figure changes.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q025

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q025
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a single sale funds work tracked under two different tasks with two different internal cost rates, the combined per-task revenue-per-hour rollup keeps each task's figure separate rather than blending both cost rates into one task-level average.
WHY_IT_MATTERS: >
  Blending two distinct cost rates into one figure would make it impossible to tell which task actually consumed the more expensive labor.
DISCONFIRMING_OBSERVATION: >
  The combined per-task rollup shows one blended average cost rate rather than each task's own distinct rate.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Fund two tasks with different internal cost rates from one sale, and check whether the combined widget's per-task figures remain separate or are blended.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q026

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q026
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A combined dashboard's real-time indicator, where present, correctly identifies which half of the combined figure, hours or billed revenue, is actually live versus last-batch, rather than a single unqualified live label covering only one side.
WHY_IT_MATTERS: >
  An unqualified live label covering a partially batched figure would overstate how current the displayed information actually is.
DISCONFIRMING_OBSERVATION: >
  The widget's live indicator applies to the whole combined figure even though only the hours side or only the revenue side actually refreshes in real time.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure one side of a combined widget's data source to refresh in real time and the other on a batch schedule, and check what the widget's live indicator actually communicates.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q027

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q027
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a timesheet entry logged in error is deleted before approval, the combined widget's provisional revenue-per-hour projection updates to exclude it within the same refresh in which the deletion occurred.
WHY_IT_MATTERS: >
  Continuing to project revenue for a deleted entry would overstate expected income for hours that no longer exist.
DISCONFIRMING_OBSERVATION: >
  After deleting an unapproved erroneous timesheet entry, the combined widget's provisional revenue projection still includes it past the refresh in which it was deleted.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Delete an erroneous timesheet entry before approval, then check whether the next combined widget refresh removes it from the provisional revenue projection.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q028

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q028
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A cross-tenant clone of a combined sale-timesheet widget definition does not retain any live reference back to the source tenant's actual employee or client records.
WHY_IT_MATTERS: >
  A live cross-tenant reference would leak one customer's actual employee and billing data into a different customer's dashboard.
DISCONFIRMING_OBSERVATION: >
  A cloned combined widget in a new tenant displays live data originating from the source tenant's actual employee or client records.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Clone a combined sale-timesheet widget definition from one tenant into another, and check whether the cloned widget resolves to the source tenant's live data.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q029

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q029
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where an employee logs hours against a project spanning two different client sales, the combined widget's per-client revenue-per-hour split follows a documented allocation rule rather than assigning the same hour to both clients' figures.
WHY_IT_MATTERS: >
  Assigning the same hour to both clients would overstate the total billable time actually delivered across the two engagements.
DISCONFIRMING_OBSERVATION: >
  The combined widget's per-client split shows the same logged hour counted in full against both clients' revenue-per-hour figures.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Have an employee log hours against a project spanning two client sales, and check how the combined widget allocates that time between the two clients.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q030

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q030
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined dashboard aggregating revenue-per-hour across an entire practice does not let a viewer permitted to see only the practice-wide summary infer an individual project's exact figure when the summary happens to include just one active project for a given period.
WHY_IT_MATTERS: >
  A summary that degenerates to a single project's figure in a sparse period functions as a direct disclosure despite being presented as an aggregate.
DISCONFIRMING_OBSERVATION: >
  A practice-wide summary total, in a period containing only one active project, reveals that project's exact figure to a viewer not permitted to see individual project detail.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  View the practice-wide combined summary for a period containing only one active project, and check whether the summary discloses that project's exact individual figure.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q031

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q031
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a sale's payment terms allow invoicing to lag behind timesheet approval by a defined period, the combined widget labels the resulting gap as expected rather than presenting it as an unexplained discrepancy between hours worked and revenue shown.
WHY_IT_MATTERS: >
  An unexplained gap would make a normal, agreed billing lag look like a data error rather than a configured business term.
DISCONFIRMING_OBSERVATION: >
  The combined widget presents an agreed invoicing lag between approved hours and billed revenue as an unexplained discrepancy with no label indicating it is expected.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a sale with payment terms that allow invoicing to lag behind timesheet approval, and check whether the combined widget labels the resulting gap as expected.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q032

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q032
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined widget's drill-through from an aggregate revenue-per-hour cell to underlying detail respects the same row-level permission scoping as the aggregate view itself, rather than exposing full unfiltered timesheet and sale records to any viewer who can see the aggregate.
WHY_IT_MATTERS: >
  A drill-through that bypasses row-level scoping would let any viewer of the aggregate reach detail their permission was never meant to grant.
DISCONFIRMING_OBSERVATION: >
  Drilling through an aggregate revenue-per-hour cell exposes unfiltered timesheet and sale records to a viewer whose row-level permission is narrower than the aggregate they can see.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Grant a user narrower row-level permission than the aggregate combined widget they can view, drill through a rollup cell, and check whether unfiltered detail becomes visible.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q033

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q033
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where hours are logged by a contractor whose billing rate differs from an internal employee's, the combined dashboard's blended team average distinguishes the two distinct rate populations where a documented distinction is expected, rather than obscuring the actual internal cost composition.
WHY_IT_MATTERS: >
  Obscuring two genuinely different rate populations in one blended average would mislead a viewer about the team's actual cost makeup.
DISCONFIRMING_OBSERVATION: >
  The combined widget's team average blends contractor and employee rates into one figure with no distinction, where the configuration calls for the two to be shown separately.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have a contractor and an internal employee log hours at different billing rates on the same team, and check whether the combined widget distinguishes the two rate populations as configured.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q034

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q034
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A combined dashboard's period-boundary handling attributes each hour to one documented invoicing period consistently between the timesheet record and the sale-side revenue rollup, not different periods on each side.
WHY_IT_MATTERS: >
  Attributing the same hour to different periods on each side would make period-based revenue-per-hour figures internally inconsistent.
DISCONFIRMING_OBSERVATION: >
  An hour logged near a billing cutoff is attributed to one period on the timesheet side and a different period on the sale-side revenue rollup.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Log an hour near a billing period cutoff, and compare which invoicing period the timesheet record and the sale-side revenue rollup each attribute it to.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q035

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q035
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a timesheet approval is later reversed after its hours were already included in an issued invoice, the combined dashboard flags the resulting inconsistency rather than silently continuing to show the hours as both invoiced and no longer approved.
WHY_IT_MATTERS: >
  An unflagged conflict between invoiced and unapproved status would hide a real billing integrity problem from whoever reviews the dashboard.
DISCONFIRMING_OBSERVATION: >
  After a post-invoice approval reversal, the combined widget shows the same hours as both invoiced and unapproved with no flag indicating the conflict.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Reverse a timesheet approval after its hours were already included in an issued invoice, and check whether the combined widget flags the resulting inconsistency.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q036

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q036
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A combined widget's handling of a negative-hour correction, where time already logged and billed is removed, reduces the revenue-per-hour figure through a documented adjustment path rather than producing a negative or unexplained hours count.
WHY_IT_MATTERS: >
  An unexplained negative or nonsensical figure would look like a data error rather than a deliberate, traceable correction.
DISCONFIRMING_OBSERVATION: >
  A negative-hour correction to already-billed time produces a negative or unexplained hours count in the combined widget with no documented adjustment reference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply a negative-hour correction to a previously logged and billed time entry, and check how the combined widget's revenue-per-hour figure reflects the adjustment.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q037

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q037
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where two sales orders share one pool of pre-purchased hours, the combined dashboard's per-order revenue-per-hour figure allocates consumed hours to the correct order rather than double-counting the same logged hours against both orders' totals.
WHY_IT_MATTERS: >
  Double counting shared retainer hours across two orders would overstate the total billable time actually consumed from the shared pool.
DISCONFIRMING_OBSERVATION: >
  The same logged hours drawn from a shared retainer pool appear in full against both sales orders' combined revenue-per-hour totals.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Draw hours from one shared retainer pool against two different sales orders, and check whether the combined widget allocates the consumed hours correctly or double counts them.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q038

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q038
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combined dashboard's handling of hours logged by an employee covering for a colleague on leave does not misattribute the covering employee's hours to the absent employee's individual productivity figure.
WHY_IT_MATTERS: >
  Misattributing covering hours would produce an individual productivity figure that describes work the named employee never actually performed.
DISCONFIRMING_OBSERVATION: >
  Hours logged by an employee covering for a colleague on leave appear under the absent colleague's individual productivity figure in the combined widget.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have one employee cover billable work for a colleague on leave, and check which employee's individual productivity figure the combined widget attributes those hours to.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q039

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q039
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a manager overrides an approved timesheet's billable hours directly on the sale side without changing the underlying timesheet record, the combined dashboard indicates that its billed-hours figure diverges from the timesheet record.
WHY_IT_MATTERS: >
  Presenting the two figures as though they agree would hide a real override from anyone reviewing the timesheet record on its own.
DISCONFIRMING_OBSERVATION: >
  The combined widget shows the sale-side billed hours and the underlying timesheet record's hours as though they agree, despite a manager override that changed only the sale side.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Have a manager override billed hours directly on the sale side without changing the underlying timesheet record, and check whether the combined widget flags the resulting divergence.
```

## G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q040

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE_TIMESHEET-Q040
MODULE: spreadsheet_dashboard_sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined dashboard's scheduled export to an external stakeholder does not include a live query link that, if opened, would bypass the export's point-in-time permission filtering and expose current unfiltered data.
WHY_IT_MATTERS: >
  A live query link embedded in an export would let a recipient bypass the filtering the export itself was meant to enforce.
DISCONFIRMING_OBSERVATION: >
  Opening a live query link embedded in a scheduled export exposes current, unfiltered data beyond what the export's own point-in-time filtering allowed.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Generate a scheduled export of a combined widget for an external stakeholder, and check whether it contains a live query link that bypasses the export's own filtering.
```
