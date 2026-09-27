# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_timesheet_holidays Module Bridge MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_TIMESHEET_HOLIDAYS-MVQ48-V1.00
**Group:** G12 PROJECT
**Module Metadata:** `project_timesheet_holidays`
**Wave:** W3 (GMVQ 25-Team Acceleration, 2026-09-27)
**Author Cell:** P12-5 (GMVQ Question Factory — Production Cell P12-5)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `project_timesheet_holidays`, a two-participant
seam (project time recording + an employee's leave/holiday calendar) listed in
GROUP_BRIEF_G12_PROJECT.md among the modules expected to reach the full 48-question floor normally.
The seam is where time logged against project work and an employee's declared or approved absence
can legitimately disagree, and something has to decide which governs, when, and what is surfaced.
Every question below was authored and checked against the removal test in
GMVQ_BRIDGE_MODULE_RULE_V1.00 §2: if project time recording and holiday/leave calendars were used
entirely apart from each other, would the question still be meaningful? A question that would still
make full sense as a pure project-time question, or as a pure leave-management question, with no
interaction between the two, was cut.

## Control

**Arity owned: TWO-PARTICIPANT (project time recording + leave/holiday calendar) only.**

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: these 48 questions test 48 distinct material seam hypotheses spread across ordering,
  partiality, ownership, timing, reversal, quantity, lifecycle mismatch, error asymmetry and
  authority, per GMVQ_BRIDGE_MODULE_RULE_V1.00 §3.
- Question text is source-neutral: no vendor or product name, no technical identifier, and the
  module's own metadata name never appears outside the `MODULE:` field.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q001

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q001
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Logging project time against a date that the employee's own calendar marks as a declared holiday
  is either blocked or clearly flagged as an exception, rather than accepted identically to an
  ordinary working day.
WHY_IT_MATTERS: >
  Accepting holiday-day time with no distinction would hide a scheduling conflict that a manager
  needs to see before approving the entry.
DISCONFIRMING_OBSERVATION: >
  Time logged on a day the employee's calendar declares a holiday is recorded with no indication
  distinguishing it from an ordinary working-day entry.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Log project time for an employee on a date their calendar declares a holiday and check whether the
  entry is flagged, blocked, or accepted without distinction.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q002

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q002
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project timesheet entry submitted for a date that overlaps an already-approved leave period for
  that same employee is surfaced as a conflict rather than accepted silently alongside the approved
  absence.
WHY_IT_MATTERS: >
  A silent conflict would let a manager approve time for work supposedly done while that same person
  was recorded as away.
DISCONFIRMING_OBSERVATION: >
  A timesheet entry for a date inside an approved leave period is accepted with no conflict shown
  anywhere to the approver.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Approve a leave period for an employee, then submit a project timesheet entry for a date inside
  that period, and check whether a conflict is surfaced.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q003

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q003
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Validating whether a given date is a working day for timesheet purposes uses the calendar actually
  assigned to that specific employee, rather than one default calendar applied to every employee
  regardless of their own assignment.
WHY_IT_MATTERS: >
  Applying one calendar to everyone would incorrectly flag or accept entries for employees whose
  actual holiday pattern differs from the default.
DISCONFIRMING_OBSERVATION: >
  Two employees with different assigned holiday calendars receive the same working-day validation
  result for a date that is a holiday under one calendar and not the other.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Assign two employees to different holiday calendars, log project time for both on a date that is a
  holiday under only one calendar, and compare the validation result each receives.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q004

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q004
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Declaring a new holiday for a date after project time has already been logged and approved for
  that date follows one documented rule for whether the existing entry is reopened for review, left
  untouched, or flagged, rather than an undefined outcome.
WHY_IT_MATTERS: >
  An undefined outcome would leave already-approved records in an inconsistent state relative to a
  policy that changed after the fact.
DISCONFIRMING_OBSERVATION: >
  Declaring the holiday retroactively produces no consistent, documented treatment of the
  already-approved entry for that date.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Approve a timesheet entry for a date, then declare that date a holiday afterward, and check what
  happens to the existing approved entry.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q005

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q005
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Time actually logged on a declared holiday, when permitted at all, is distinguishable in reporting
  from ordinary project time rather than blended into the same undifferentiated total.
WHY_IT_MATTERS: >
  Blending holiday-worked time into ordinary totals would hide that special handling, such as a
  different rate or compensating time off, might be owed.
DISCONFIRMING_OBSERVATION: >
  Time logged and approved on a declared holiday appears in reports identically to time logged on an
  ordinary day, with no distinguishing marker anywhere.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Log and approve project time on a declared holiday and check whether reporting distinguishes it
  from ordinary working-day time.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q006

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q006
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where a project team includes employees under different regional holiday calendars, each
  employee's timesheet is validated against their own calendar rather than one calendar chosen for
  the project as a whole being applied to every team member.
WHY_IT_MATTERS: >
  Applying one region's calendar to the whole team would misvalidate entries for members who
  actually observe a different set of holidays.
DISCONFIRMING_OBSERVATION: >
  A team member under a different regional calendar than the project's majority is validated against
  the majority's calendar rather than their own.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Staff a project with employees under two different regional holiday calendars, log time for both
  on a date that is a holiday in only one region, and compare validation outcomes.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q007

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q007
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A leave period approved for an employee that overlaps a project deadline is reflected in that
  employee's availability as shown to the project, rather than the project continuing to display
  them as fully available across the leave dates.
WHY_IT_MATTERS: >
  A project manager relying on a stale availability view could commit deadlines the team cannot
  actually meet.
DISCONFIRMING_OBSERVATION: >
  The project's view of the employee's availability shows them fully available on dates covered by
  their own already-approved leave.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Approve leave for an employee assigned to a project spanning that leave period, and check whether
  the project's availability view for that employee reflects the leave.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q008

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q008
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Submitting a leave request for a date range that already contains approved project timesheet
  entries surfaces that overlap for review rather than silently overwriting or ignoring the existing
  entries.
WHY_IT_MATTERS: >
  A silent overwrite would erase or hide a record of work already approved as having happened.
DISCONFIRMING_OBSERVATION: >
  Approving the leave request removes or overwrites the pre-existing timesheet entries for the
  overlapping dates with no review step ever presented.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Record approved timesheet entries for a date range, then submit and approve a leave request
  covering part of that range, and check whether the overlap is surfaced or the entries are altered.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q009

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q009
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Whether logging project time on a declared holiday affects that employee's separately tracked
  leave balance is one documented rule, not an unexplained side effect that differs case by case.
WHY_IT_MATTERS: >
  An unexplained balance change would make the leave entitlement figure impossible to trust or
  reconcile.
DISCONFIRMING_OBSERVATION: >
  Logging project time on a declared holiday changes the employee's leave balance with no documented
  rule stating that it should.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record the employee's leave balance, log project time on a declared holiday, and check whether the
  balance changes as a result.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q010

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q010
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A project task assigned to an employee who goes on an extended approved leave remains assigned to
  them but is distinguishably flagged as currently unavailable rather than presented identically to
  a task assigned to someone actively working.
WHY_IT_MATTERS: >
  An indistinguishable presentation would let a manager assume progress is being made on work that
  cannot actually proceed.
DISCONFIRMING_OBSERVATION: >
  A task assigned to an employee on extended approved leave shows no distinguishable indication of
  that unavailability anywhere the task is displayed.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Approve extended leave for an employee holding an assigned project task and check how that task is
  displayed during the leave period.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q011

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q011
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A manager approving a project timesheet entry logged on a date the holiday calendar marks as
  non-working requires an explicit override step, rather than the approval proceeding identically to
  an ordinary-day entry with no distinguishing action recorded.
WHY_IT_MATTERS: >
  Approving without an explicit override would leave no record that anyone consciously accepted an
  exception to the calendar.
DISCONFIRMING_OBSERVATION: >
  The manager approves a holiday-dated entry through the exact same action as an ordinary entry, with
  no override step or record distinguishing the exception.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Submit a timesheet entry for a date marked non-working and attempt to approve it, checking whether
  an explicit override action is required and recorded.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q012

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q012
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Changing an employee's assigned holiday calendar, for example after a change of work location,
  applies to timesheet validation from the effective date of the change forward, without silently
  reinterpreting timesheet entries already recorded under the previous calendar.
WHY_IT_MATTERS: >
  Retroactive reinterpretation would change the recorded status of entries that were valid when they
  were made.
DISCONFIRMING_OBSERVATION: >
  Changing the employee's calendar assignment causes a previously valid, already-recorded entry to
  be reclassified under the new calendar's rules.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a timesheet entry under one calendar assignment, change the employee's calendar assignment,
  and check whether the earlier entry's classification changes.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q013

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q013
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A holiday declared after a project's planned effort was already calculated for a date range is
  reflected the next time that planned-effort figure is recalculated, rather than the figure
  remaining permanently stale relative to the newly declared holiday.
WHY_IT_MATTERS: >
  A permanently stale planning figure would overstate available capacity for dates that are actually
  non-working.
DISCONFIRMING_OBSERVATION: >
  Recalculating the project's planned effort after the new holiday is declared still shows the same
  figure as if the holiday did not exist.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Calculate a project's planned effort for a date range, declare a new holiday inside that range,
  trigger a recalculation, and compare the figures.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q014

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q014
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The count of available working days used in a project's planned effort calculation for a specific
  employee excludes that specific employee's own declared holidays, rather than applying one flat
  count of working days assumed identical for every employee.
WHY_IT_MATTERS: >
  A flat assumption would overstate or understate an individual's actual capacity whenever their
  holiday count differs from the assumed average.
DISCONFIRMING_OBSERVATION: >
  Two employees with different numbers of declared holidays in the same date range show identical
  available-working-day counts in the project's planning calculation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Assign two employees with differing holiday counts in the same range to a project and compare each
  one's available-working-day figure in the planning calculation.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q015

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q015
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Unpaid leave and a declared paid holiday are recorded as distinguishable absence categories in
  project time reporting, rather than both appearing as the same generic non-working entry.
WHY_IT_MATTERS: >
  Conflating the two categories would make it impossible to see, from the project's own reporting,
  which type of absence actually occurred.
DISCONFIRMING_OBSERVATION: >
  An unpaid leave day and a declared holiday for the same employee appear identically in the
  project's time reporting with no distinguishing category.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Record one unpaid leave day and one declared holiday for the same employee and compare how each is
  categorized in the project's own time reporting.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q016

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q016
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A part-time employee's proportionally reduced holiday entitlement is what governs their timesheet
  and availability validation, rather than validation applying a full-time assumption regardless of
  their actual working proportion.
WHY_IT_MATTERS: >
  A full-time assumption applied to a part-time employee would misclassify their actual available
  days and misstate project capacity.
DISCONFIRMING_OBSERVATION: >
  A part-time employee's timesheet and availability validation produces the same result a
  full-time employee's would, disregarding the proportional entitlement difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a part-time employee with a proportionally reduced entitlement and compare their
  validation outcome against a full-time employee for the same dates.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q017

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q017
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A holiday that falls on a day the employee would not have worked anyway, with a substitute
  compensating day off applied under policy, is validated against the substitute day rather than the
  original calendar date for timesheet purposes.
WHY_IT_MATTERS: >
  Validating against the wrong date would either wrongly flag an ordinary working day or wrongly
  accept time on the day meant to actually be off.
DISCONFIRMING_OBSERVATION: >
  Timesheet validation treats the original holiday date as non-working while treating the actual
  substitute compensating day as an ordinary working day, or vice versa.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a holiday with a substitute compensating day off and log project time on both the
  original date and the substitute date, comparing validation for each.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q018

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q018
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a previously approved leave period after some of the employee's project work was
  reassigned to cover the gap requires a deliberate decision about that reassignment, rather than
  the reassignment silently and automatically reverting on its own.
WHY_IT_MATTERS: >
  A silent automatic reversion could hand work back to the original employee without anyone
  confirming they are actually available again or that the covering assignment should end.
DISCONFIRMING_OBSERVATION: >
  Cancelling the approved leave silently reverts the reassigned work back to the original employee
  with no confirmation step recorded.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Approve leave, reassign the affected project work to cover it, cancel the leave, and check whether
  the reassignment reverts automatically or requires a deliberate action.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q019

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q019
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Scheduling a project task's required work during a period the assigned employee already holds
  approved leave surfaces that conflict to whoever does the scheduling rather than allowing the
  schedule to proceed with no indication of the clash.
WHY_IT_MATTERS: >
  An unsurfaced clash could leave a project commitment built on a date the assigned person is
  already known to be unavailable.
DISCONFIRMING_OBSERVATION: >
  Scheduling the task's work inside the employee's already-approved leave period completes with no
  conflict shown to the person doing the scheduling.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Approve leave for an employee, then schedule required work for a task assigned to them inside that
  leave period, and check whether a conflict is surfaced.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q020

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q020
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where an employee has both a half-day leave request and a declared holiday on the same date, the
  combined expected working hours for that day for timesheet purposes reflect the two overlapping
  correctly rather than double-subtracting the same time twice.
WHY_IT_MATTERS: >
  Double-subtracting would understate the employee's expected hours and could misrepresent their
  timesheet compliance for that day.
DISCONFIRMING_OBSERVATION: >
  The expected working hours for the overlapping day are reduced by both the half-day leave and the
  full holiday independently, producing a negative or clearly incorrect expected-hours figure.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a date that is both a declared holiday and covered by a half-day leave request for one
  employee, and check the resulting expected working hours for that day.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q021

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q021
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A company-wide policy change adding a new mandatory holiday mid-year flags any already-approved
  future project timesheet entries that fall on the newly added date, rather than leaving them
  silently unreviewed.
WHY_IT_MATTERS: >
  Unreviewed future entries under a changed policy could leave planned work on a date the
  organization has since decided is non-working.
DISCONFIRMING_OBSERVATION: >
  Adding the new mandatory holiday leaves an already-approved future entry on that date with no
  flag or review prompt of any kind.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Have an already-approved future timesheet entry on a date, add a new mandatory holiday for that
  date, and check whether the entry is flagged for review.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q022

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q022
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Where a project is delivered for a customer whose own recognized non-working days differ from the
  performing employee's personal holiday calendar, timesheet validation applies one documented,
  consistently chosen calendar rather than an ambiguous mix of both with no stated precedence.
WHY_IT_MATTERS: >
  Ambiguous precedence between two calendars would make it unpredictable whether a given date is
  treated as working or not.
DISCONFIRMING_OBSERVATION: >
  For the same date, differing under the two calendars, the validation outcome is inconsistent
  across otherwise identical entries with no documented rule stating which calendar governs.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a project where the associated external calendar differs from the employee's personal
  calendar for a specific date, log time on that date, and check which calendar the validation
  actually applies.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q023

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q023
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A holiday configured as optional, where each employee individually decides whether to take it,
  applies the non-working treatment only to the timesheets of employees who actually chose to take
  that day, not to every employee under the same calendar uniformly.
WHY_IT_MATTERS: >
  A uniform blanket treatment would incorrectly flag or excuse time for employees who made the
  opposite individual choice.
DISCONFIRMING_OBSERVATION: >
  Two employees under the same calendar who made opposite individual choices about an optional
  holiday receive the identical timesheet validation treatment for that date.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure an optional holiday, have two employees make opposite individual choices about taking
  it, log time for both on that date, and compare validation outcomes.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q024

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q024
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Rejecting a timesheet entry specifically because it falls on a declared holiday produces a
  rejection reason that clearly identifies the holiday conflict, distinguishable from a rejection for
  an unrelated validation failure.
WHY_IT_MATTERS: >
  An indistinguishable rejection reason would leave the employee unable to tell what actually needs
  correcting.
DISCONFIRMING_OBSERVATION: >
  A rejection caused by a holiday-date conflict shows the same generic reason as a rejection caused
  by an unrelated validation failure.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Submit an entry that fails only because of a holiday-date conflict and one that fails for an
  unrelated reason, and compare the rejection reasons shown.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q025

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q025
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When two different projects both track planned resource capacity for the same employee, a
  declared holiday for that employee is excluded from the capacity calculation of both projects
  consistently, not only from one of them.
WHY_IT_MATTERS: >
  Excluding the holiday from only one project's capacity figure would make the two projects'
  planning numbers for the same person mutually inconsistent.
DISCONFIRMING_OBSERVATION: >
  One project's capacity figure for the employee excludes the declared holiday while the other
  project's capacity figure for the same employee and date does not.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Assign one employee to two projects with a shared declared holiday in range, and compare each
  project's own capacity calculation for that employee.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q026

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q026
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a project's own budgeted effort assumes a standard number of working days per period that
  differs from what the assigned employee's actual holiday calendar allows, that discrepancy is
  surfaced rather than the budget figure silently carrying forward unchanged.
WHY_IT_MATTERS: >
  An unsurfaced discrepancy would leave a project budget based on an assumption the assigned
  employee's actual calendar contradicts.
DISCONFIRMING_OBSERVATION: >
  A project's standard-working-day assumption for a period differs materially from the assigned
  employee's actual holiday-adjusted availability with no discrepancy shown anywhere.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set a project's standard-working-day assumption for a period and compare it against an assigned
  employee's actual holiday-adjusted availability for the same period.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q027

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q027
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Rescinding a previously declared holiday reopens timesheet submission for that now-ordinary date
  and reflects any leave that had specifically been taken to cover it, rather than leaving both in
  their pre-rescission state indefinitely.
WHY_IT_MATTERS: >
  Leaving both unchanged would mean a policy correction never actually reaches the affected records.
DISCONFIRMING_OBSERVATION: >
  Rescinding the holiday leaves timesheet submission for that date still blocked, or leaves leave
  taken specifically to cover it unaddressed, with no follow-up shown.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Declare a holiday, have an employee take leave to cover it, then rescind the holiday, and check the
  resulting state of both the timesheet block and the leave record.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q028

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q028
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project task's schedule remains shown as still planned for a date the assigned employee's leave
  has since been approved for, rather than automatically appearing complete or vacant with no visible
  connection between the two records.
WHY_IT_MATTERS: >
  A silently updated schedule with no visible cause would confuse anyone trying to understand why the
  plan changed.
DISCONFIRMING_OBSERVATION: >
  After the leave is approved, the task's planned schedule for that date changes with no visible
  reference connecting the change to the approved leave, or does not change at all despite the
  employee being unavailable.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Approve leave for an employee holding a scheduled task on the same date and check the task's
  displayed schedule state and whether any connection to the leave is visible.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q029

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q029
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Once a timesheet period is locked for closure, a leave record for a date inside that locked period
  cannot be created or edited without a documented reopening step, rather than silently succeeding
  against an accounting period that is supposed to be closed.
WHY_IT_MATTERS: >
  A silent edit against a closed period would corrupt records that were supposed to already be
  final.
DISCONFIRMING_OBSERVATION: >
  A leave record for a date inside a locked timesheet period is created or edited successfully with
  no reopening step recorded anywhere.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Lock a timesheet period for closure, then attempt to create or edit a leave record for a date
  inside it, and check whether the action requires a documented reopening step.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q030

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q030
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where an employee is recorded in a different time zone than the project's own operating time zone,
  which calendar day governs a holiday's timesheet check is resolved by one documented, consistently
  applied rule rather than an ambiguous result that shifts depending on which time zone happens to be
  used for the comparison.
WHY_IT_MATTERS: >
  An ambiguous resolution could validate the wrong calendar day for an employee working across a time
  zone boundary from the project.
DISCONFIRMING_OBSERVATION: >
  The same logged entry near a time-zone boundary is validated as falling on the holiday under one
  time-zone interpretation and not under another, with no documented rule stating which governs.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Have an employee in a different time zone from the project log time near a holiday's boundary and
  check which time zone's calendar day the validation actually uses.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q031

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q031
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  When an employee changes to a role or position that carries a different holiday calendar, that
  new calendar governs their timesheet validation from the effective date of the role change
  forward, rather than the old calendar's assumptions carrying over indefinitely.
WHY_IT_MATTERS: >
  Continuing to apply the old calendar after a role change would misvalidate the employee's actual
  going-forward working days.
DISCONFIRMING_OBSERVATION: >
  After the role change takes effect, timesheet validation for the employee still uses the previous
  role's calendar rather than the new one.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change an employee's role to one carrying a different holiday calendar, log time after the
  effective date, and check which calendar governs validation.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q032

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q032
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two managers independently approving, at nearly the same time, an overlapping leave request and a
  project-task time assignment for the same employee and date does not leave the system in a final
  state where both the leave and the active work assignment are simultaneously approved with no
  conflict ever raised.
WHY_IT_MATTERS: >
  A silently contradictory final state would mean the same person is simultaneously recorded as away
  and as actively committed to project work with no one aware of the contradiction.
DISCONFIRMING_OBSERVATION: >
  After both near-simultaneous approvals complete, the employee shows as both on approved leave and
  as holding an active, unflagged work assignment for the same date.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Have two managers approve, within a short window of each other, an overlapping leave request and a
  project time assignment for the same employee and date, then check the resulting combined state.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q033

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q033
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where a project defines its own working calendar distinct from an assigned employee's personal
  holiday calendar, which of the two actually governs whether a given date counts against the
  project's schedule for timesheet purposes is one documented, consistently applied precedence
  rule.
WHY_IT_MATTERS: >
  An undocumented precedence would make it unpredictable which calendar's holidays actually count
  for schedule purposes.
DISCONFIRMING_OBSERVATION: >
  For a date treated as a holiday under one of the two calendars but not the other, the project's
  own schedule validation gives inconsistent results across otherwise identical entries with no
  documented precedence rule.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a project's own working calendar to differ from an assigned employee's personal calendar
  for a specific date, log time on that date, and check which calendar the schedule validation
  actually follows.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q034

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q034
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Submitting a leave request that would take the employee's remaining entitlement below zero is
  either blocked or explicitly flagged for approval with the shortfall visible, rather than silently
  approved as though sufficient entitlement remained.
WHY_IT_MATTERS: >
  A silent approval past the entitlement would leave the resulting negative balance unaccounted for
  and undisclosed to whoever approves it.
DISCONFIRMING_OBSERVATION: >
  A leave request exceeding the employee's remaining entitlement is approved with no shortfall
  indication shown to the approver at any point.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Submit a leave request that would exceed the employee's remaining entitlement and check whether the
  shortfall is shown before or during approval.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q035

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q035
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A different absence category from a declared holiday, logged for a project workday, is reflected
  distinctly in project time reporting rather than conflated with a scheduled holiday as though the
  two were the same category of non-working time.
WHY_IT_MATTERS: >
  Conflating distinct absence categories would make it impossible to tell from project reporting
  which type of non-working time actually occurred.
DISCONFIRMING_OBSERVATION: >
  A different absence category and a declared holiday for the same employee appear identically in
  project time reporting with no distinguishing category shown.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Record one instance of a different absence category and one declared holiday for the same
  employee, and compare how each is categorized in project time reporting.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q036

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q036
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A holiday declared for the coming year, entered while a long-running project's forward schedule
  already spans that date, is reflected the next time the project's forward capacity plan is
  recalculated rather than the plan permanently ignoring holidays declared after the plan was first
  built.
WHY_IT_MATTERS: >
  A plan permanently blind to holidays declared afterward would drift further from reality the
  longer the project runs.
DISCONFIRMING_OBSERVATION: >
  Recalculating the long-running project's forward capacity plan after the new future holiday is
  declared still does not reflect it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Build a long-running project's forward capacity plan, declare a holiday for a future date already
  inside that plan's span, recalculate the plan, and compare the figures.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q037

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q037
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project task with no working calendar of its own explicitly assigned falls back to a default that
  still correctly excludes the assigned employee's actual declared holidays, rather than a default
  that assumes no holidays at all regardless of that employee's real calendar.
WHY_IT_MATTERS: >
  A holiday-blind default would misvalidate every task lacking an explicit calendar assignment for
  every employee it is given to.
DISCONFIRMING_OBSERVATION: >
  A task with no explicit calendar assignment validates time logged on the assigned employee's actual
  declared holiday as an ordinary working day.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Assign a task with no explicit working calendar to an employee with a declared holiday in range,
  log time on that holiday, and check the validation outcome.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q038

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q038
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Importing a full year's holiday calendar in bulk after several months of that year's timesheets
  have already been recorded prompts a review of the affected already-recorded dates rather than
  leaving them permanently unexamined against the newly imported calendar.
WHY_IT_MATTERS: >
  Permanently unexamined historical entries would leave a portion of the year's records inconsistent
  with the calendar the organization now considers correct.
DISCONFIRMING_OBSERVATION: >
  After the bulk import, none of the affected already-recorded entries are flagged for review against
  the newly imported calendar.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Record several months of timesheets, then bulk-import a full year's holiday calendar covering that
  same period, and check whether the affected entries are flagged for review.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q039

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q039
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  An external resource logging project time who has no holiday entitlement or calendar assigned at
  all is validated through one documented, distinct rule appropriate to that status, rather than
  either erroring with no defined behaviour or silently skipping holiday validation with no
  documented reason.
WHY_IT_MATTERS: >
  An undefined outcome for this case would leave external resource time either unusable or
  unvalidated with no one having decided that was acceptable.
DISCONFIRMING_OBSERVATION: >
  Logging time for an external resource with no assigned calendar produces an unhandled error, or
  silently skips holiday validation entirely with no documented rule saying that is intended.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Log project time for a resource with no holiday calendar or entitlement assigned and check how
  validation handles the case.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q040

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q040
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A leave request spanning a period that itself includes an already-declared holiday deducts from
  the employee's leave balance only for the actual working days in that span, not for the holiday
  date counted a second time within the requested range.
WHY_IT_MATTERS: >
  Double-counting the holiday inside the leave deduction would understate the employee's actual
  remaining entitlement.
DISCONFIRMING_OBSERVATION: >
  The leave balance deduction for the spanning request includes the holiday date as an additional
  day charged against the balance.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Submit a leave request spanning a period that includes an already-declared holiday and check
  exactly which dates are deducted from the leave balance.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q041

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q041
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where an employee is declared as holiday-calendar-linked to one work location but temporarily
  relocated for a project assignment to a different location, timesheet validation for the duration
  of that temporary assignment follows one documented, consistently applied rule for which
  location's calendar governs.
WHY_IT_MATTERS: >
  An undocumented choice between the two calendars would produce unpredictable validation for the
  duration of the temporary assignment.
DISCONFIRMING_OBSERVATION: >
  Timesheet validation for the temporarily relocated employee switches between the two locations'
  calendars inconsistently across otherwise identical entries during the assignment.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Temporarily relocate an employee to a project in a different location with a different calendar,
  log time during the assignment, and check which location's calendar governs validation.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q042

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q042
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A manager overriding a flagged holiday-timesheet conflict to force its approval leaves a
  distinguishable, auditable record of that override, rather than the conflict simply disappearing
  from view with no trace it ever occurred.
WHY_IT_MATTERS: >
  An untraceable override would remove the only evidence that an exception to the holiday policy was
  deliberately made rather than the result of a system error.
DISCONFIRMING_OBSERVATION: >
  After the override is used to force approval, no record distinguishes that entry from one that
  never had a conflict at all.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Force approval of a flagged holiday-timesheet conflict through an override and check whether an
  auditable record of that override is retrievable afterward.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q043

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q043
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Merging two holiday calendars during an organizational restructuring re-validates
  already-submitted-but-not-yet-approved timesheet entries for affected dates against the merged
  result, rather than leaving them pending under rules that no longer exist.
WHY_IT_MATTERS: >
  Approving a pending entry under a calendar that no longer exists could apply a rule the
  organization has already abandoned.
DISCONFIRMING_OBSERVATION: >
  A pending entry for an affected date is approved after the merge using the pre-merge calendar's
  classification with no re-validation against the merged calendar.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Have a pending timesheet entry for a date affected by a calendar merge, complete the merge, and
  check whether the entry is re-validated before it can be approved.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q044

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q044
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A task's automatically calculated expected-effort figure for a date range treats a half-day
  holiday inside that range as a partial exclusion proportional to the half day, rather than either
  ignoring it entirely or excluding a full day for a half-day holiday.
WHY_IT_MATTERS: >
  Treating a half-day holiday as a full-day exclusion, or ignoring it, would misstate the expected
  effort for that date range either way.
DISCONFIRMING_OBSERVATION: >
  The expected-effort calculation for a range containing a half-day holiday either shows no
  reduction at all or shows a full-day reduction for what is only a half-day holiday.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a half-day holiday inside a task's date range, trigger the expected-effort calculation,
  and check the size of the reduction applied.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q045

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q045
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An exported project timesheet report intended for external billing marks hours logged on a
  declared holiday distinctly, or excludes them per a documented rule, rather than presenting them
  identically to ordinary billable hours with no distinguishing marker in the export.
WHY_IT_MATTERS: >
  An undistinguished export could bill a customer for holiday-flagged time without disclosing that
  distinction, or silently omit legitimately worked holiday time.
DISCONFIRMING_OBSERVATION: >
  The exported billing report shows holiday-logged hours identically to ordinary hours with no
  distinguishing marker and no documented exclusion rule applied.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Log hours on a declared holiday, export the project's timesheet report for external billing, and
  check how those hours are represented in the export.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q046

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q046
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Deleting a declared holiday after timesheet entries for that date have already been validated
  against it leaves those entries' recorded classification intact rather than silently reclassifying
  history to match the holiday's absence.
WHY_IT_MATTERS: >
  Silently reclassifying historical entries would rewrite a record of what was true at the time the
  entry was actually made and approved.
DISCONFIRMING_OBSERVATION: >
  Deleting the holiday changes the classification shown on an already-approved historical entry for
  that date.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Approve a timesheet entry validated against a declared holiday, delete that holiday afterward, and
  check whether the historical entry's classification changes.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q047

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q047
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a leave approval and a holiday declaration for the same date are both entered by different
  people at nearly the same time, the resulting employee availability state for the project is one
  single, consistent value rather than depending on which of the two entries happened to be
  processed last with no reconciliation.
WHY_IT_MATTERS: >
  An outcome dependent purely on processing order, with no reconciliation, would make the final
  availability state effectively random from the users' point of view.
DISCONFIRMING_OBSERVATION: >
  Reversing the order in which the two near-simultaneous entries are processed produces a different
  final availability state for the same employee and date with no reconciliation step involved.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Enter a leave approval and a separate holiday declaration for the same date in each possible
  order and compare the resulting availability state each time.
```

## G12-PROJECT_TIMESHEET_HOLIDAYS-Q048

```yaml
QID: G12-PROJECT_TIMESHEET_HOLIDAYS-Q048
MODULE: project_timesheet_holidays
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a declared holiday after employees have already been prevented from submitting
  timesheet entries for that date under the holiday block reopens submission for that date rather
  than leaving the block permanently in place after its underlying cause no longer exists.
WHY_IT_MATTERS: >
  A block that outlives its own justification would permanently prevent legitimate work from ever
  being recorded for that date.
DISCONFIRMING_OBSERVATION: >
  After the holiday is cancelled, employees are still unable to submit timesheet entries for that
  date.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Have the holiday block prevent a submission attempt, cancel the declared holiday, and check
  whether submission for that date becomes possible.
```
