# SMEsPlus ENTERPRISE SUITE
## GMVQ — G15 PRODUCTIVITY / spreadsheet_dashboard_hr_timesheet Module Bridge MVQ Bank

**Document ID:** GMVQ-G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-MVQ50-V1.00
**Group:** G15 PRODUCTIVITY (Wave W4)
**Module Metadata:** `spreadsheet_dashboard_hr_timesheet`
**Wave:** W4
**Author Cell:** P15-2 (GMVQ Question Factory — Wave W4 Acceleration, Cell P15-2)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 50 = 105
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `spreadsheet_dashboard_hr_timesheet` — a 2-way
BRIDGE per GMVQ_BRIDGE_MODULE_RULE_V1.00 and GROUP_BRIEF_G15_PRODUCTIVITY.md, seam: a live
collaborative dashboard drawing rollups and tiles from logged-time data it does not itself own. The
underlying timesheet entry's own logging, validation, and correction mechanics belong to the
time-tracking base family and are deliberately NOT re-asked here. This bank asks only what becomes
true or uncertain **because a dashboard layer sits on top of** that data: staleness of a running,
not-yet-saved timer versus confirmed logged time; aggregation that exposes individual-level hours
through small-team rollups or peer visibility; real-time versus batch-refresh mismatch; period and
time-zone boundary handling that can differ between the source and the reporting layer;
utilization figures that combine two independently changing inputs; and whether dashboard access
itself is mistaken for, or grants, a validation action the source module gates behind its own
permission model. Every question was tested against the bridge rule: if it would read equally well
with no dashboard in the picture at all — i.e. it is really a question about logging, validating,
or billing time on its own — it was cut. This bank is also deliberately distinct from a
sale-plus-timesheet billing seam (a different bridge's subject): here the concern is dashboard
exposure and staleness of hours data, never whether hours are correctly re-invoiced to a customer.

The question text is source-neutral and does not expose vendor or product names, field names,
methods, schema, XML IDs, API shapes, or implementation algorithms. `MODULE:
spreadsheet_dashboard_hr_timesheet` appears only in the structured metadata field, never inside
question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` stating a concrete failure state,
  never a restatement of its own hypothesis.
- No padding: 50 questions exist because they test 50 distinct material hypotheses at the seam
  between a reporting/dashboard layer and logged-time data; none was trimmed or stretched to hit
  count.
- BRIDGE MODULE per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question fails only at the seam. None
  restates a timesheet logging, validation, or billing-rate invariant that holds with no dashboard
  layer present, and none restates a customer re-invoicing invariant belonging to a sale-timesheet
  billing bridge.
- Mandatory pre-authoring sibling check performed: `01_QUESTION_BANKS/G15_PRODUCTIVITY/` held only
  this cell's own `spreadsheet_dashboard_hr_expense` bank on disk at authoring time (checked
  directly); its HYPOTHESIS text was reviewed and no overlap found. Overlap against this cell's own
  `spreadsheet_dashboard_im_livechat` and `spreadsheet_dashboard_sale` drafts was checked directly
  at authoring time; no overlap found.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/evidence.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q001

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q001
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rollup of hours logged by team does not reveal an individual's own daily hours to a peer who
  could not see that individual's timesheet directly.
WHY_IT_MATTERS: >
  Individual work-pattern detail is sensitive between peers; a team rollup is supposed to protect it
  behind aggregation, not merely relabel it.
DISCONFIRMING_OBSERVATION: >
  A peer with no direct visibility into a colleague's timesheet can determine that colleague's
  individual daily hours from a team rollup, because the team is small enough to isolate the figure.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a team member with no manager-level visibility, inspect a team-hours rollup for a small team and
  check whether an individual's figure is isolable.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q002

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q002
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An "hours logged today" counter reflects entries actually saved to the source record, not entries
  still open in an unsaved editing session.
WHY_IT_MATTERS: >
  Counting unsaved, editable entries as logged time overstates confirmed work before the employee
  has committed to the figure.
DISCONFIRMING_OBSERVATION: >
  A today's-hours counter increases while an entry is being typed but not yet saved, then does not
  match what is actually persisted if the edit is abandoned.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Begin editing a new time entry without saving it and observe whether a live hours counter reflects
  the unsaved value.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q003

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q003
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An in-progress running timer is either excluded from a real-time hours total or clearly marked
  provisional, rather than being blended indistinguishably with confirmed, stopped-and-saved logged
  time.
WHY_IT_MATTERS: >
  A provisional, still-running duration is not a fact yet; presenting it as equal to confirmed hours
  misstates the total until the timer actually stops.
DISCONFIRMING_OBSERVATION: >
  A real-time hours total includes a still-running timer's elapsed duration with no visual or
  structural distinction from confirmed logged hours.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Start a timer, let it run, and inspect a real-time hours total for how the running duration is
  represented relative to confirmed entries.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q004

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q004
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Drilling from an aggregate hours figure into the underlying entries enforces the same "own team
  only" visibility restriction the source timesheet list enforces, not a broader default scope
  introduced by the reporting layer.
WHY_IT_MATTERS: >
  A reporting layer more permissive than the record it summarizes turns an aggregate tile into a
  backdoor around the source module's own access control.
DISCONFIRMING_OBSERVATION: >
  A viewer restricted to their own team's timesheets reaches, via drill-down, entries belonging to
  people outside that team.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a viewer scoped to one team, drill down from an aggregate hours tile and inspect the full set of
  entries the resulting list contains.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q005

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q005
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Billable and non-billable hours are never combined into a single, unlabeled total that a viewer
  could mistake for billable time alone.
WHY_IT_MATTERS: >
  An unlabeled blend can misinform a billing or capacity decision that depends specifically on the
  billable portion.
DISCONFIRMING_OBSERVATION: >
  A total combining billable and non-billable hours carries no label or breakdown distinguishing the
  two.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Log both billable and non-billable hours in the same period and inspect any combined total's
  labeling.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q006

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q006
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard showing utilization (logged hours versus expected or contracted hours) recomputes when
  either the logged-hours source or the expected-hours configuration changes, not only when one of
  the two is updated.
WHY_IT_MATTERS: >
  A utilization figure driven by two inputs that does not react to a change in either one becomes
  silently wrong the moment either side moves.
DISCONFIRMING_OBSERVATION: >
  Utilization stays unchanged after either the logged-hours total or the expected-hours
  configuration is updated, when the other side did not also change.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change only the expected-hours configuration for an employee, leaving logged hours untouched, and
  check whether utilization recomputes.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q007

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q007
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A period-boundary mismatch between the reporting layer's week or period definition and the source
  timesheet's configured period does not attribute the same logged hour to two different periods
  across the two.
WHY_IT_MATTERS: >
  An hour double-counted or lost across a period boundary mismatch corrupts both the current and
  adjacent period's totals.
DISCONFIRMING_OBSERVATION: >
  An hour logged near a period boundary is attributed to a different period in the dashboard than in
  the source timesheet record.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Log an entry at a period boundary and compare its period attribution between the source record and
  the dashboard.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q008

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q008
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An employee's historical logged hours remain visible in a period-based aggregate that already
  included them even after that employee's record is deactivated or archived.
WHY_IT_MATTERS: >
  A closed period's total should not shrink retroactively just because the person who logged the
  hours has since left.
DISCONFIRMING_OBSERVATION: >
  A closed-period hours aggregate drops after the contributing employee's record is deactivated, with
  no change to the underlying entries.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Deactivate an employee whose hours are already reflected in a closed-period aggregate and
  re-render that aggregate.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q009

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q009
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A correction to a previously submitted timesheet entry is reflected in any aggregate computed
  after the correction, not the original, now-superseded figure.
WHY_IT_MATTERS: >
  Continuing to report a known-wrong number of hours after it has been corrected at the source
  defeats the point of allowing the correction.
DISCONFIRMING_OBSERVATION: >
  An aggregate rendered after an hours correction still reflects the original, uncorrected value.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Correct an already-counted entry's logged hours and re-render any aggregate that includes it.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q010

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q010
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A manager's "my team's hours" view only includes employees who currently report to that manager,
  not employees who once did but have since moved elsewhere.
WHY_IT_MATTERS: >
  A stale reporting-line aggregate misrepresents current team capacity and could expose a former
  report's ongoing activity to a manager no longer entitled to see it.
DISCONFIRMING_OBSERVATION: >
  An employee who no longer reports to a given manager still appears in that manager's "my team"
  hours aggregate.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Reassign an employee to a different manager and check whether the former manager's team aggregate
  still includes them.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q011

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q011
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Hours logged against a project a viewer has no access to are not individually attributable within
  a rollup shown to that viewer, even where the total figure includes them.
WHY_IT_MATTERS: >
  A rollup that lets a viewer trace hours back to a project they cannot otherwise see defeats the
  project-level access restriction.
DISCONFIRMING_OBSERVATION: >
  A viewer with no access to a given project can identify that project's contribution within a
  rollup they can see.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a viewer without access to a specific project, inspect a rollup that includes hours logged
  against it and check for identifiable attribution.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q012

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q012
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard combining hours from multiple time zones attributes each entry to a single,
  consistently defined business day rather than shifting an entry's day depending on which zone the
  aggregate happens to be computed in.
WHY_IT_MATTERS: >
  A day-attribution that depends on the viewer's or server's time zone produces different daily
  totals for the same underlying entries depending on who or what computed them.
DISCONFIRMING_OBSERVATION: >
  The same entry is attributed to different calendar days depending on the time zone in effect when
  the aggregate is computed or viewed.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Log an entry near midnight in one time zone and compare its day attribution when the aggregate is
  computed under a different zone.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q013

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q013
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An "hours pending validation" aggregate only counts entries genuinely awaiting validation, not
  entries already validated or already rejected.
WHY_IT_MATTERS: >
  A pending count that includes resolved entries misleads a validator about their actual outstanding
  workload.
DISCONFIRMING_OBSERVATION: >
  A pending-validation count includes an entry that has already been validated or rejected.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Validate or reject a previously pending entry and check whether it still appears in a
  pending-validation aggregate.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q014

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q014
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A scheduled or batch-refreshed hours dashboard visibly indicates its "as of" time so a viewer does
  not mistake it for a live, second-by-second figure.
WHY_IT_MATTERS: >
  A viewer who believes a stale figure is live may make a staffing or workload decision on data that
  no longer matches the source.
DISCONFIRMING_OBSERVATION: >
  A batch-refreshed hours widget presents its figures with no visible timestamp or staleness
  indicator.
EXPECTED_SURFACE: S5,S8
PRECONDITIONS: >
  Identify a widget known to refresh on a schedule and inspect whether it discloses its effective
  timestamp.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q015

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q015
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two dashboard widgets built from the same timesheet data but refreshed at different times can
  disagree, and each is distinguishable by its own refresh timestamp rather than implying equal
  currency.
WHY_IT_MATTERS: >
  Two disagreeing widgets with no way to know which is more current leave a viewer unable to decide
  which figure to act on.
DISCONFIRMING_OBSERVATION: >
  Two widgets covering the same underlying hours show different totals with no per-widget indication
  of their own refresh time.
EXPECTED_SURFACE: S5,S8
PRECONDITIONS: >
  Place two overlapping-data widgets on refresh schedules that will drift apart and compare their
  values and any per-widget timestamps.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q016

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q016
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling an entire timesheet period (not a single entry) removes all of that period's entries
  from any aggregate that had already counted them.
WHY_IT_MATTERS: >
  Leaving entry-level hours behind after their parent period is cancelled overstates logged time by
  exactly the amount that was supposed to have been voided.
DISCONFIRMING_OBSERVATION: >
  An aggregate still includes one or more entries from a fully cancelled timesheet period.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel a multi-entry timesheet period already reflected in an aggregate and re-render the
  aggregate.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q017

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q017
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Overlapping entries for the same employee across two different tasks in the same time window are
  not silently double-counted as twice the elapsed calendar time in a total-hours aggregate.
WHY_IT_MATTERS: >
  Double counting overlapping time inflates apparent capacity and utilization beyond what actually
  occurred.
DISCONFIRMING_OBSERVATION: >
  A total-hours figure for a window with genuinely overlapping entries equals or exceeds the sum of
  both entries rather than reflecting the true elapsed time, with no flag noting the overlap.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Log two overlapping entries for the same employee in the same window and inspect the resulting
  total-hours aggregate for the window.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q018

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q018
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard grouped by project does not expose which specific individual logged the hours to a
  viewer who holds only project-level, not individual-level, visibility.
WHY_IT_MATTERS: >
  A project-level view is supposed to protect individual attribution; leaking it defeats the scoping
  the reporting layer was built to provide.
DISCONFIRMING_OBSERVATION: >
  A viewer with project-level-only visibility can see a named individual attached to hours within a
  project-grouped widget.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a project-level-only-scoped viewer, inspect a project-grouped hours widget for named
  attribution.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q019

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q019
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Reassigning a logged entry from one project or task to another after it was already reflected in
  that project's historical aggregate is handled by a defined rule — retroactive move or
  point-in-time snapshot — rather than being left ambiguous between the two.
WHY_IT_MATTERS: >
  An undefined rule means two readings of the same historical figure at different times can
  legitimately disagree, with neither provably wrong.
DISCONFIRMING_OBSERVATION: >
  Reassigning a historical entry's project produces a change in the historical aggregate matching
  neither a stated retroactive rule nor a stated snapshot rule.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reassign the project of an entry already reflected in a closed-period aggregate and observe which
  rule, if either, the resulting change follows.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q020

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q020
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A cached dashboard total is invalidated and recomputed when a viewer's access scope is reduced,
  rather than continuing to serve a total computed under their former, broader scope.
WHY_IT_MATTERS: >
  A cache that outlives a permission reduction hands a now-restricted viewer data their narrower
  scope should no longer include.
DISCONFIRMING_OBSERVATION: >
  A viewer whose scope has just been reduced still receives a cached total reflecting their former,
  broader scope.
EXPECTED_SURFACE: S4,S8
PRECONDITIONS: >
  Reduce a viewer's visibility scope after a cached total has been computed for them, then reload
  the dashboard before any unrelated cache expiry.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q021

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q021
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Concurrent edits by two people to overlapping timesheet entries for the same period do not produce
  an aggregate reflecting neither person's final saved state.
WHY_IT_MATTERS: >
  A lost-update outcome under concurrency can leave a period's total inconsistent with what either
  person actually saved.
DISCONFIRMING_OBSERVATION: >
  After two concurrent, non-conflicting edits to the same period, the resulting aggregate matches
  neither edit's final intended state.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Have two people concurrently edit different entries within the same period and inspect the
  resulting aggregate.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q022

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q022
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rollup exposed at a company-wide level does not carry team-level detail fine enough to
  reconstruct near-individual hour figures when a team's headcount is very small.
WHY_IT_MATTERS: >
  Fine-grained detail at the company level defeats the purpose of aggregating if it still lets a
  viewer reconstruct one person's figure.
DISCONFIRMING_OBSERVATION: >
  A company-wide rollup's team-level breakdown, combined with known small team headcount, allows
  recovery of an individual's hours.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Inspect a company-wide rollup's team-level granularity where at least one team has very few
  members.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q023

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q023
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An employee's own personal dashboard view of their logged hours matches exactly what a manager's
  drill-down into that same employee shows, with no silent discrepancy between the two presentations
  of the same underlying data.
WHY_IT_MATTERS: >
  Two different presentations of the same underlying hours disagreeing undermines trust in whichever
  one is actually wrong.
DISCONFIRMING_OBSERVATION: >
  An employee's self-view total for a period differs from a manager's drill-down total for the same
  employee and period.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Compare an employee's own hours view for a period against a manager's drill-down view of the same
  employee and period.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q024

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q024
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A tile counting entries "missing a task assignment" reflects the current assignment state of the
  source records, not a cached state from before the assignment was later added.
WHY_IT_MATTERS: >
  A stale missing-assignment count can prompt unnecessary follow-up on an entry already corrected.
DISCONFIRMING_OBSERVATION: >
  A missing-assignment tile continues to count an entry after a task has been assigned to it, past
  any stated refresh window.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Assign a task to an entry already counted as missing one, then reload the tile within its refresh
  window.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q025

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q025
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Deleting a task or project after hours were logged against it does not remove those hours from
  historical aggregates that already included them, though it may affect where a new drill-down
  points.
WHY_IT_MATTERS: >
  A historical total should not shrink just because its referenced task or project was later
  removed.
DISCONFIRMING_OBSERVATION: >
  A historical aggregate's total drops after the task or project it was logged against is deleted.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Delete a task/project already reflected in a historical hours aggregate and re-render that
  aggregate.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q026

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q026
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An "hours this quarter" widget uses the fiscal-period definition configured for the organization,
  not a generic calendar quarter, when the two differ.
WHY_IT_MATTERS: >
  A quarter widget built on the wrong calendar silently reports the wrong period to anyone relying on
  the organization's actual fiscal boundaries.
DISCONFIRMING_OBSERVATION: >
  In an organization with a non-calendar fiscal quarter, a "this quarter" hours widget's boundary
  dates do not match the configured fiscal quarter.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  In an organization with a non-calendar fiscal quarter, inspect a "this quarter" hours widget's
  actual date boundaries.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q027

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q027
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Exporting the dashboard's underlying entry-level data to a shareable file does not bypass the same
  visibility restriction that applies when viewing the same entries within the dashboard interface.
WHY_IT_MATTERS: >
  An export path that ignores the on-screen restriction turns a properly scoped view into an
  unrestricted file the moment it is downloaded.
DISCONFIRMING_OBSERVATION: >
  A viewer exports entry-level data and the exported file contains entries the same viewer could not
  see on screen.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a scoped viewer, export the underlying entry-level data and compare its contents to what is
  visible on screen.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q028

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q028
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard combining current-period and prior-period totals for comparison correctly isolates
  each period's figures even where the prior period's closing or lock process happened after some
  current-period entries already existed.
WHY_IT_MATTERS: >
  A comparison that bleeds current-period activity into the prior-period figure, or vice versa,
  misstates the period-over-period trend it exists to show.
DISCONFIRMING_OBSERVATION: >
  A period-comparison widget's prior-period figure changes after current-period data is entered, or
  the current-period figure includes activity dated in the prior period.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Enter current-period entries after the prior period has closed and inspect a period-comparison
  widget for cross-period bleed.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q029

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q029
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard auto-refreshing at a fixed interval marks itself visibly stale rather than silently
  continuing to display data past a failed refresh attempt.
WHY_IT_MATTERS: >
  Silent staleness after a failed refresh is indistinguishable from a genuinely current figure,
  removing the viewer's ability to know they should not trust it.
DISCONFIRMING_OBSERVATION: >
  A dashboard whose scheduled refresh fails continues to present its last-good figures with no
  visible staleness indicator.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Cause or simulate a refresh failure on an auto-refreshing hours widget and inspect the presentation
  afterward.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q030

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q030
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Access to the hours dashboard does not itself grant the ability to validate or approve a timesheet
  entry from within the dashboard, even where the dashboard displays validation status.
WHY_IT_MATTERS: >
  A reporting surface that also exposes a live validation control bypasses the separation between
  viewing and authorizing that the source module's permission model is built on.
DISCONFIRMING_OBSERVATION: >
  A viewer with dashboard access but no validation authority is able to trigger a validation or
  rejection action from within the dashboard interface.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a viewer with dashboard access but no validation authority, attempt to act on a
  validation-status element shown in the dashboard.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q031

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q031
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A drill-down link on an aggregate figure that no longer resolves to any entry, because the entry
  was deleted, fails visibly rather than silently substituting a default value or a zero.
WHY_IT_MATTERS: >
  A silent substitution disguises a broken reference as legitimate data, hiding a data-integrity
  problem from anyone relying on the drill-down.
DISCONFIRMING_OBSERVATION: >
  Following a drill-down link to a deleted entry produces a blank or zeroed page instead of a
  visible error or not-found state.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Delete an entry already referenced by a dashboard drill-down link and follow that link.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q032

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q032
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard reporting average hours per employee does not misrepresent a distribution skewed by
  one employee working unusually long hours as if it were typical, and the underlying detail remains
  reachable to a viewer entitled to see it.
WHY_IT_MATTERS: >
  A single outlier can move an average enough to mislead about "typical" workload unless the
  dashboard surfaces the skew or lets an entitled viewer inspect it.
DISCONFIRMING_OBSERVATION: >
  An average-hours figure moves sharply due to one outlier employee with no way for an entitled
  viewer to discover or drill into that outlier from the average widget.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Introduce one employee with unusually long hours into a group shown as an average and check
  whether the outlier is discoverable from the average widget.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q033

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q033
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where hours are later converted to a cost figure for a combined hours-and-cost dashboard, the
  conversion uses one consistent, disclosed rate basis across the aggregate rather than mixing
  different bases silently.
WHY_IT_MATTERS: >
  A total built from inconsistent rate bases cannot be reconciled to any single source of truth and
  misstates cost without any visible sign that it has done so.
DISCONFIRMING_OBSERVATION: >
  Two employees' hours converted to cost on different dates are found to have used two different,
  undisclosed rate bases within the same summed total.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Log hours across a rate change and inspect how a combined hours-and-cost total was derived.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q034

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q034
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard aggregating hours by department does not silently include hours logged by contractors
  or temporary staff unless the aggregate is explicitly scoped to include them.
WHY_IT_MATTERS: >
  Blending employment categories without disclosure misstates a workforce metric meant to reflect
  one specific category.
DISCONFIRMING_OBSERVATION: >
  A department hours total changes when a contractor's or temporary staff member's hours are added,
  with no disclosure that non-employee hours are included.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Log hours for a contractor or temporary staff member in a department and inspect whether the
  department aggregate discloses their inclusion.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q035

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q035
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A viewer's ability to filter an hours dashboard by employee does not become a way to enumerate the
  full employee list beyond what that viewer would otherwise be authorized to browse.
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

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q036

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q036
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a timesheet entry moves from an unapproved to an approved state, an aggregate distinguishing
  approved from unapproved hours updates within the dashboard's stated refresh window rather than
  continuing to show it in the prior bucket indefinitely.
WHY_IT_MATTERS: >
  A stuck bucket misrepresents how much confirmed, approved time actually exists at any given
  moment.
DISCONFIRMING_OBSERVATION: >
  An entry approved well outside any stated refresh window still appears in the unapproved bucket of
  an approved/unapproved aggregate.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Approve a previously unapproved entry and check the approved/unapproved aggregate after the stated
  refresh window has elapsed.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q037

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q037
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A dashboard combining hours across more than one company or legal entity does not silently sum
  figures that should remain entity-scoped unless the viewer holds explicit cross-entity visibility.
WHY_IT_MATTERS: >
  Summing across entity boundaries without authorization exposes one entity's staffing pattern to
  users of another and can misstate entity-level reporting.
DISCONFIRMING_OBSERVATION: >
  A viewer scoped to a single entity is shown, or a total silently includes, hours belonging to a
  different entity they hold no cross-entity right to see.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  In a multi-entity configuration, view an hours dashboard as a single-entity-scoped user and check
  whether any total includes another entity's figures.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q038

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q038
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A rejected timesheet entry that required rework is excluded from a "confirmed hours" aggregate
  until it is resubmitted and re-approved, not counted on the strength of its first submission
  alone.
WHY_IT_MATTERS: >
  Counting a rejected entry as confirmed overstates verified, approved time before rework has
  actually been accepted.
DISCONFIRMING_OBSERVATION: >
  A rejected entry still awaiting resubmission appears in a "confirmed hours" aggregate.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reject an entry requiring rework and check whether it still appears in a confirmed-hours
  aggregate before resubmission.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q039

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q039
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A real-time "currently clocked in" indicator only reflects sessions still genuinely open, not
  sessions that ended abnormally without a proper close event.
WHY_IT_MATTERS: >
  A stuck "clocked in" status for a session that actually ended misrepresents who is currently
  working and can mislead a real-time staffing view.
DISCONFIRMING_OBSERVATION: >
  An employee whose session ended abnormally (without a proper stop) continues to be shown as
  clocked in indefinitely.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  End a timer session abnormally (without the normal stop action) and observe how long the
  clocked-in indicator persists.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q040

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q040
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard widget configured against a filter referencing a specific employee or project does not
  continue silently returning stale results after that referenced record is deactivated or archived.
WHY_IT_MATTERS: >
  A filter silently keeping stale references produces results the configuration owner no longer
  intends and cannot explain by inspecting the current, active configuration.
DISCONFIRMING_OBSERVATION: >
  A widget filtered to a since-deactivated employee or project still returns data as though the
  reference were active, with no warning that it is stale.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Build a widget filtered to a specific employee or project, deactivate that reference, and
  re-render the widget.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q041

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q041
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An aggregate figure computed before a bulk correction (such as a batch unit or rate fix) is
  reconciled to reflect the correction, with the fact that a correction occurred left visible rather
  than the number simply drifting with no explanation.
WHY_IT_MATTERS: >
  An unexplained change to a previously reported figure undermines trust in every other number the
  dashboard has ever shown.
DISCONFIRMING_OBSERVATION: >
  A previously reported hours aggregate changes value after a bulk correction with no visible
  indication that a correction occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger or identify a bulk correction to previously aggregated hours data and check for a visible
  change-disclosure alongside the updated figure.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q042

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q042
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A utilization percentage does not exceed logically possible bounds (such as well over 100% for a
  standard period) without a visible explanation, such as overlapping entries or overtime, being
  reachable from the figure.
WHY_IT_MATTERS: >
  An unexplained impossible-looking percentage undermines confidence in the entire utilization
  metric.
DISCONFIRMING_OBSERVATION: >
  A utilization figure well above 100% is displayed with no way to discover the overlap or overtime
  driving it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Produce a utilization figure driven by overlapping or overtime entries and check whether the cause
  is discoverable from the widget.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q043

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q043
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A drill-down from a project-level hours total to individual contributor entries respects the same
  project-membership restriction that governs direct access to the project's own timesheet list.
WHY_IT_MATTERS: >
  A drill-down that ignores project membership turns the reporting layer into a way around the
  project's own access control.
DISCONFIRMING_OBSERVATION: >
  A viewer without project membership reaches individual contributor entries for that project via a
  drill-down from a project-level total.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a viewer without membership in a given project, attempt to drill down from that project's
  hours total to individual entries.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q044

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q044
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard grouping hours by client, via the project they were logged against, does not expose
  one client's staffing pattern to a viewer authorized to see only their own client relationship.
WHY_IT_MATTERS: >
  Cross-client staffing detail is competitively and contractually sensitive; a client-scoped viewer
  should never see another client's pattern.
DISCONFIRMING_OBSERVATION: >
  A viewer scoped to one client's data can see hours or staffing detail attributable to a different
  client in a client-grouped widget.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a viewer scoped to a single client relationship, inspect a client-grouped hours widget for any
  other client's detail.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q045

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q045
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An entry made against a task later merged into a different task is represented once, not twice, in
  any aggregate that would otherwise double count it across the merge.
WHY_IT_MATTERS: >
  A merge that leaves the same hours counted under both the old and new task inflates the combined
  total by exactly the merged amount.
DISCONFIRMING_OBSERVATION: >
  After merging two tasks, an aggregate spanning both shows a combined total higher than the sum of
  the genuinely distinct entries.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Merge two tasks that each already had hours logged against them and inspect a combined aggregate
  for double counting.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q046

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q046
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A manager who loses management responsibility for an employee mid-period sees that employee's
  hours drop out of "my team" aggregates for the appropriate portion of the period, not remain
  permanently attributed to them.
WHY_IT_MATTERS: >
  Permanently attributing a former report's hours to a manager who no longer manages them
  misrepresents both the manager's actual team and the employee's actual reporting line during the
  period.
DISCONFIRMING_OBSERVATION: >
  A "my team" aggregate for a manager continues to include a former report's hours for periods
  after the reporting-line change, with no split at the change point.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Change an employee's manager mid-period and inspect both managers' "my team" aggregates spanning
  the change.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q047

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q047
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard widget cached from before a bulk import of historical timesheet data does not silently
  omit the imported records from subsequent totals indefinitely.
WHY_IT_MATTERS: >
  A cache that never absorbs a bulk import produces totals that permanently understate history by
  exactly the imported amount.
DISCONFIRMING_OBSERVATION: >
  A widget's historical total remains unchanged after a bulk import of historical entries that
  should have altered it, even well after any stated refresh window.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Perform a bulk import of historical timesheet data and check a previously cached historical
  aggregate after the stated refresh window.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q048

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q048
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A viewer granted only a read-only, aggregate-level role cannot use dashboard interactions, such as
  a group-by or filter control, to reconstruct individual-level entries the direct timesheet list
  view would otherwise hide from them.
WHY_IT_MATTERS: >
  An interactive reporting control that can be narrowed down to a single row is functionally
  equivalent to direct record access, defeating the aggregate-only restriction.
DISCONFIRMING_OBSERVATION: >
  A read-only, aggregate-scoped viewer can narrow a group-by or filter control until it isolates a
  single individual's entries.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As an aggregate-only-scoped viewer, attempt to use group-by or filter controls to isolate a single
  individual's entries.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q049

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q049
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard reporting logged hours against budgeted or planned hours for a project reflects a
  change to the planned-hours configuration made after some hours were already logged, without
  silently re-baselining already-elapsed periods.
WHY_IT_MATTERS: >
  Re-baselining an already-elapsed period against a plan that did not exist at the time misrepresents
  how the project actually tracked against its plan during that period.
DISCONFIRMING_OBSERVATION: >
  A historical period's planned-versus-actual comparison changes after the planned-hours
  configuration is updated, for a period that had already elapsed under the old plan.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a project's planned-hours configuration after a period has elapsed and re-render that
  period's planned-versus-actual comparison.
```

## G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q050

```yaml
QID: G15-SPREADSHEET_DASHBOARD_HR_TIMESHEET-Q050
MODULE: spreadsheet_dashboard_hr_timesheet
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Sharing a dashboard snapshot outside the organization does not carry forward drill-down access to
  the underlying, access-restricted entry-level data even though the aggregate figures are shared.
WHY_IT_MATTERS: >
  External sharing is the highest-consequence disclosure boundary; a snapshot meant to share summary
  figures should not also hand out entry-level access to parties with no organizational
  relationship.
DISCONFIRMING_OBSERVATION: >
  A recipient of an externally shared dashboard snapshot can drill down into individual entry-level
  data not covered by the sharing configuration.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Share a dashboard snapshot externally at aggregate granularity and attempt to drill down into
  entry-level data from the shared view.
```
