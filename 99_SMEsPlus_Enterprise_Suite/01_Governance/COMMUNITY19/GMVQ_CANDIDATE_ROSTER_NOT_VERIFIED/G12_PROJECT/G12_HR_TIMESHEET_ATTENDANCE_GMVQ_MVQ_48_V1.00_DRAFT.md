# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / hr_timesheet_attendance Module MVQ Bank

**Document ID:** GMVQ-G12-HR_TIMESHEET_ATTENDANCE-MVQ48-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `hr_timesheet_attendance`
**Wave:** W3
**Author Cell:** P12-1 (GMVQ Question Factory — Production Cell P12-1)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the link between physical presence
(check-in/check-out style attendance) and logged working time. Although named as a two-part
combination, the Group Brief classifies this module as foundation-level, not a bridge subject to
the seam-only rule, so this bank asks the full range of foundation questions about how attendance
observation is translated into time records: derivation and rounding of duration, correction
propagation, missing or duplicate punches, cross-midnight attribution, and the boundary between an
attendance-derived entry and one entered by hand for the same day.

Question text is source-neutral. It does not name the module, any vendor or product, or any
technical identifier (field, model, method, XML ID, API path).

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because each tests a distinct material hypothesis, spread across
  the required dimensions (business capability, business rule, state transition, configuration
  dependency, role and permission, exception path, cancellation, reversal, negative case,
  cross-module dependency, optional behaviour, auditability, tenant/company boundary, concurrency
  and ordering, runtime reachability, configuration reachability).
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G12-HR_TIMESHEET_ATTENDANCE-Q001

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q001
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A completed check-in/check-out pair generates a derived time entry whose duration matches the
  actual elapsed interval between the two recorded moments.
WHY_IT_MATTERS: >
  If the derived duration does not match the actual observed interval, the whole point of deriving
  time from attendance rather than manual entry is defeated.
DISCONFIRMING_OBSERVATION: >
  The derived time entry's duration does not match the elapsed interval between the recorded
  check-in and check-out moments.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Record a check-in and a later check-out with a known interval and inspect the resulting derived
  time entry's duration.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q002

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q002
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A check-in with no corresponding check-out is surfaced as an open, incomplete attendance record
  rather than silently generating a derived time entry with a fabricated or assumed end point.
WHY_IT_MATTERS: >
  A fabricated end point for a missing check-out invents worked time that was never actually
  observed.
DISCONFIRMING_OBSERVATION: >
  A check-in with no check-out produces a derived time entry with an end point that was never
  actually recorded.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Record a check-in with no corresponding check-out and inspect whether any derived time entry is
  generated and what end point it uses.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q003

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q003
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Correcting a check-in or check-out time after the fact updates the duration of the derived time
  entry that was generated from it, so the two do not silently drift apart.
WHY_IT_MATTERS: >
  A derived time entry that stops tracking corrections to its source attendance record becomes
  disconnected from the fact it was supposed to represent.
DISCONFIRMING_OBSERVATION: >
  Correcting the underlying check-in or check-out time leaves the previously derived time entry's
  duration unchanged.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Generate a derived time entry from a check-in/check-out pair, correct one of the two times, and
  re-inspect the derived entry's duration.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q004

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q004
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting an attendance record that already produced a derived time entry either removes or clearly
  flags that time entry, rather than leaving an orphaned entry with no attendance record to justify
  it.
WHY_IT_MATTERS: >
  An orphaned time entry with no supporting attendance record misrepresents the entry's actual
  origin and evidentiary basis.
DISCONFIRMING_OBSERVATION: >
  Deleting the source attendance record leaves its derived time entry intact with no flag indicating
  its supporting record is gone.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate a derived time entry from an attendance record, delete the attendance record, and inspect
  the time entry afterward.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q005

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q005
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an employee both has an attendance-derived time entry and separately logs a manual time entry
  for overlapping hours on the same day, the overlap is flagged rather than both being silently
  counted as additive worked time.
WHY_IT_MATTERS: >
  Silent double-counting of the same hours inflates reported effort and cost without anyone
  choosing that outcome.
DISCONFIRMING_OBSERVATION: >
  An attendance-derived entry and a manually logged entry covering the same overlapping hours are
  both counted in totals with no flag for the overlap.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate an attendance-derived entry and add a manual entry overlapping the same hours on the same
  day, then inspect the resulting totals.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q006

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q006
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An attendance-derived time entry for an employee with no assigned default project or task is
  handled by a defined, consistent fallback — flagged for manual assignment, or blocked from
  generation — not left silently unattributed.
WHY_IT_MATTERS: >
  A silently unattributed entry is effort that exists in totals but cannot be traced to any project
  or task for cost or billing purposes.
DISCONFIRMING_OBSERVATION: >
  An attendance-derived entry for an employee with no default project or task is generated with no
  attribution and no flag prompting assignment.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record attendance for an employee with no default project or task configured and inspect the
  resulting derived entry.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q007

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q007
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  More than one check-in/check-out pair recorded for the same employee on the same day are each
  reflected as their own derived time entry, rather than being merged into a single entry that hides
  the actual number of separate attendance sessions.
WHY_IT_MATTERS: >
  Merging distinct sessions into one entry hides gaps in the day that a reviewer might specifically
  want to see.
DISCONFIRMING_OBSERVATION: >
  Two separate check-in/check-out pairs on the same day produce a single merged derived entry that
  does not reflect the actual gap between the two sessions.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Record two separate check-in/check-out pairs for the same employee on the same day with a gap
  between them, and inspect the resulting derived entries.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q008

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q008
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Duration values derived from attendance are subject to the same rounding rule as durations entered
  manually, so a given elapsed interval does not produce a different reported duration depending on
  which entry path recorded it.
WHY_IT_MATTERS: >
  Two different rounding rules for the same underlying interval creates systematic discrepancies
  between attendance-derived and manually entered totals.
DISCONFIRMING_OBSERVATION: >
  The same elapsed interval produces a different rounded duration when recorded via attendance
  versus entered manually.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Produce the same elapsed interval through an attendance-derived entry and a manual entry, and
  compare the resulting rounded durations.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q009

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q009
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A check-in and check-out spanning midnight attributes the resulting duration to a date in a
  defined, consistent way, rather than an arbitrary or undocumented split between the two calendar
  days.
WHY_IT_MATTERS: >
  Undocumented, inconsistent date attribution across midnight makes daily totals unreliable on shift
  patterns that regularly cross the boundary.
DISCONFIRMING_OBSERVATION: >
  A check-in/check-out pair spanning midnight is attributed to a different date on repeated,
  otherwise identical attempts.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Record a check-in before midnight and a check-out after midnight, and inspect the resulting date
  attribution, repeating to check consistency.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q010

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q010
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A check-out recorded with no corresponding prior check-in for that employee on that day is rejected
  or flagged, rather than silently accepted as a valid attendance event.
WHY_IT_MATTERS: >
  A check-out with no matching check-in is either an error or evidence of a bypass; either way it
  should not be silently treated as normal.
DISCONFIRMING_OBSERVATION: >
  A check-out event with no preceding check-in for that employee that day is accepted with no flag or
  rejection.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to record a check-out for an employee with no open check-in for that day.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q011

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q011
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Attempting to check in again for an employee who already has an open, unclosed check-in is either
  blocked or automatically closes the existing session, but does not silently open a second
  concurrent session for the same employee.
WHY_IT_MATTERS: >
  Two concurrently open sessions for one employee makes it ambiguous which session a later check-out
  actually closes.
DISCONFIRMING_OBSERVATION: >
  An employee with an already-open check-in successfully opens a second, independently tracked open
  check-in without the first being closed or flagged.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  With an employee's check-in already open, attempt to record another check-in for the same
  employee.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q012

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q012
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An employee scoped to one company's attendance tracking cannot have their check-in/check-out
  events generate derived time entries against a project scoped to a different company.
WHY_IT_MATTERS: >
  A cross-company leak here would misattribute both presence and cost data across the boundary the
  multi-company model depends on.
DISCONFIRMING_OBSERVATION: >
  An attendance-derived entry for an employee scoped to one company is attributed to a project scoped
  to a different company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Record attendance for an employee scoped to one company where the resulting derived entry could
  reach a project scoped to a different company, and inspect the attribution.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q013

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q013
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Manually editing an attendance-derived time entry directly, independent of its source attendance
  record, is either prevented in favour of editing the source, or is flagged as having diverged from
  the source it was derived from.
WHY_IT_MATTERS: >
  An entry that can drift silently from its own source record loses the evidentiary link that made it
  trustworthy as an attendance-backed figure in the first place.
DISCONFIRMING_OBSERVATION: >
  A derived time entry is edited directly with no flag indicating it no longer matches its source
  attendance record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate a derived time entry from attendance, edit the derived entry directly rather than its
  source, and inspect whether any divergence is flagged.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q014

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q014
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Attendance totals reported through an attendance-specific report and the corresponding worked-time
  totals reported through a timesheet-specific report reconcile to the same underlying figures for
  the same employee and period.
WHY_IT_MATTERS: >
  Two official reports of the same underlying reality that disagree leave no way to know which one is
  actually correct.
DISCONFIRMING_OBSERVATION: >
  The attendance report's total for an employee and period does not reconcile with the timesheet
  report's total for the same employee and period.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate both an attendance report and a timesheet report for the same employee and period and
  compare totals.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q015

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q015
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An employee's own attendance and derived time records are visible to that employee, and to their
  manager, but not to an unrelated colleague with no management relationship.
WHY_IT_MATTERS: >
  Attendance patterns are a sensitive record of presence; unrestrained peer visibility exposes
  personal working-time patterns with no business need.
DISCONFIRMING_OBSERVATION: >
  An unrelated colleague with no management relationship can view another employee's attendance or
  derived time records.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a colleague with no management relationship, attempt to view another employee's attendance
  records.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q016

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q016
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Editing a check-in or check-out time inside an already-locked or approved payroll or reporting
  period is either prevented or requires an explicit override distinct from an ordinary edit outside
  the locked period.
WHY_IT_MATTERS: >
  Silent edits to attendance data underlying an already-closed period could retroactively invalidate
  figures already reported or paid out on.
DISCONFIRMING_OBSERVATION: >
  An attendance record dated inside a locked or approved period is edited through the same
  unqualified action used outside that period, with no override step or trace.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Lock a reporting period and attempt to edit a check-in or check-out time dated within it.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q017

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q017
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A check-in and check-out recorded through a mobile or remote device populate the same fields, with
  the same validation, as one recorded through a fixed on-premises method, rather than the remote
  path carrying looser data quality.
WHY_IT_MATTERS: >
  A remote entry channel with looser validation becomes the easiest path to record inaccurate or
  incomplete attendance data.
DISCONFIRMING_OBSERVATION: >
  A check-in or check-out recorded via a mobile or remote method skips a validation step or field
  that a fixed on-premises method enforces.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Record attendance through a mobile or remote method and through a fixed method, and compare
  validation applied to each.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q018

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q018
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Correcting a check-in or check-out time after the fact is recorded as a distinct correction,
  traceable back to the original recorded value, rather than silently overwriting it with no trace.
WHY_IT_MATTERS: >
  Attendance is exactly the kind of record where a later dispute may hinge on knowing both what was
  originally recorded and what it was changed to.
DISCONFIRMING_OBSERVATION: >
  Correcting a check-in or check-out time overwrites the original value with no trace of what it
  originally was.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a check-in or check-out, correct it, and inspect whether the original value remains
  traceable.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q019

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q019
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A public holiday or scheduled day off configured for an employee is at least flagged when
  attendance is recorded on that day, rather than treated identically to any ordinary working day.
WHY_IT_MATTERS: >
  Unflagged attendance on a day the employee was not scheduled to work hides exactly the anomaly a
  reviewer would want to see.
DISCONFIRMING_OBSERVATION: >
  Attendance recorded on a configured holiday or day off is displayed identically to attendance on an
  ordinary working day, with no flag anywhere.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a check-in/check-out on a day configured as a holiday or day off for that employee, and
  inspect how it is displayed.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q020

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q020
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deactivating or terminating an employee retains their historical attendance and derived time
  records unchanged and reportable, rather than making them inaccessible or excluding them from
  period reporting already closed.
WHY_IT_MATTERS: >
  A terminated employee's historical attendance may still be needed for payroll reconciliation or
  dispute resolution after they have left.
DISCONFIRMING_OBSERVATION: >
  Deactivating an employee causes their previously recorded attendance or derived time entries to
  become inaccessible or excluded from reporting.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Record attendance for an employee, deactivate that employee, and inspect whether the earlier
  records remain reportable.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q021

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q021
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A time zone change or daylight-saving transition occurring between a check-in and its check-out
  does not silently produce a negative or otherwise nonsensical derived duration.
WHY_IT_MATTERS: >
  A daylight-saving transition is a predictable, recurring event; a duration calculation that breaks
  on it will break on the same date every year.
DISCONFIRMING_OBSERVATION: >
  A check-in/check-out pair spanning a daylight-saving transition produces a derived duration that is
  negative or otherwise clearly wrong.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Record a check-in/check-out pair spanning a known daylight-saving transition and inspect the
  resulting derived duration.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q022

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q022
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two check-in events recorded at effectively the same timestamp for the same employee, such as from
  duplicate device submissions, are detected and deduplicated rather than both being retained as
  independent attendance sessions.
WHY_IT_MATTERS: >
  Undetected duplicate submissions from unreliable network conditions would double-count presence
  and any derived worked time.
DISCONFIRMING_OBSERVATION: >
  Two check-in submissions at effectively the same timestamp for the same employee both persist as
  independent sessions.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit two check-in events at effectively the same timestamp for the same employee and inspect
  whether both are retained.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q023

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q023
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a grace period or rounding rule applies to check-in and check-out times (for example,
  rounding to the nearest scheduling interval), it is applied consistently in both directions rather
  than always favouring one side.
WHY_IT_MATTERS: >
  A rounding rule that always rounds in the employer's or the employee's favour, undocumented, is a
  systematic bias rather than a neutral convenience.
DISCONFIRMING_OBSERVATION: >
  The configured rounding rule consistently favours one direction regardless of which side of the
  interval the actual time fell on, with no documentation of that bias.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record check-in and check-out times falling on both sides of a rounding interval and inspect
  whether the rounding is applied symmetrically.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q024

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q024
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An unusually short check-in/check-out interval, well below any plausible working session, produces
  at least a visible flag rather than being silently accepted and derived into an ordinary time
  entry.
WHY_IT_MATTERS: >
  An implausibly short session is a common signature of an accidental double-tap or a data-entry
  error; leaving it unflagged lets an obvious error pass straight into reporting.
DISCONFIRMING_OBSERVATION: >
  A check-in/check-out pair with an implausibly short interval generates a derived entry identical in
  presentation to any ordinary entry, with no flag.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Record a check-in immediately followed by a check-out and inspect whether the resulting derived
  entry is flagged as unusual.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q025

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q025
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An unusually long open check-in — well beyond any plausible single working session with no
  check-out — is flagged for review rather than silently continuing to accrue derived time
  indefinitely.
WHY_IT_MATTERS: >
  An indefinitely accruing open session, if ever closed or reported on, would produce a wildly
  inflated duration nobody actually worked.
DISCONFIRMING_OBSERVATION: >
  A check-in left open far beyond any plausible session length is not flagged, and would produce an
  unrealistically large duration if closed or reported on as-is.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Leave a check-in open well beyond a plausible working session and check for any review flag.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q026

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q026
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Attendance recorded through an integration or automated device feed is subject to the same
  validation as attendance recorded through the primary interactive method.
WHY_IT_MATTERS: >
  An automated feed with weaker validation is the highest-volume path for invalid attendance data to
  enter the system.
DISCONFIRMING_OBSERVATION: >
  An attendance event that would be rejected through the interactive method is accepted through an
  integration or automated feed.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Submit an attendance event that fails interactive validation through an integration path and
  compare the outcome.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q027

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q027
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A derived time entry keeps a reference back to the specific attendance event it was generated
  from, so its origin remains traceable rather than presenting identically to a manually created
  entry.
WHY_IT_MATTERS: >
  Losing the origin link makes it impossible to later distinguish attendance-backed entries from
  self-reported ones, which is often exactly the distinction a reviewer needs.
DISCONFIRMING_OBSERVATION: >
  A derived time entry carries no reference distinguishing it as attendance-derived rather than
  manually created.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate a derived time entry from attendance and inspect whether it is distinguishable from a
  manually created one.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q028

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q028
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a break or pause can be recorded within an open attendance session, the resulting derived
  time entry excludes the break duration from the counted worked time rather than counting the full
  span including the break.
WHY_IT_MATTERS: >
  A break silently counted as worked time overstates actual worked hours and any cost derived from
  them.
DISCONFIRMING_OBSERVATION: >
  A recorded break within an attendance session is still counted as worked time in the derived
  entry's duration.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Record a check-in, a break, and a check-out, and inspect whether the break duration is excluded
  from the derived entry.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q029

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q029
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether attendance-derived time entries are generated automatically or only after a manual review
  step is an explicit, discoverable configuration, not an undocumented default that differs
  unpredictably between employees or projects.
WHY_IT_MATTERS: >
  An undocumented, inconsistent generation rule makes it impossible to know whether a given day's
  worked time already appears in totals or is still awaiting review.
DISCONFIRMING_OBSERVATION: >
  Whether a derived entry appears automatically or awaits manual review differs between two
  otherwise identically configured employees or projects, with no discoverable setting explaining
  the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare derived-entry generation behaviour across two employees or projects expected to share the
  same configuration.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q030

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q030
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An attendance record for one employee cannot be attributed, through any correction or edit path, to
  a different employee's derived time entries.
WHY_IT_MATTERS: >
  Attendance misattributed to the wrong employee would corrupt both presence records and any cost
  calculation based on the wrong person's rate.
DISCONFIRMING_OBSERVATION: >
  An attendance record originally tied to one employee ends up generating or updating a derived time
  entry attributed to a different employee.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to reassign or correct an attendance record's employee attribution and inspect the effect
  on derived entries.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q031

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q031
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An employee's own view of their attendance and derived entries on a self-service surface shows the
  same figures a manager sees through the internal, non-self-service view for the same period.
WHY_IT_MATTERS: >
  A discrepancy between the employee-facing and manager-facing figures for the same underlying data
  means one of them is simply wrong.
DISCONFIRMING_OBSERVATION: >
  The same employee's attendance total for a period differs between their own self-service view and
  their manager's internal view.
EXPECTED_SURFACE: S1,S4,S5
PRECONDITIONS: >
  Compare an employee's own attendance view against their manager's view for the same period.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q032

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q032
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Attendance data captured under a test or non-production configuration is not reachable by, or
  counted in, live production time or payroll reporting under any shared-data condition.
WHY_IT_MATTERS: >
  Test attendance data leaking into production would silently distort worked-time totals with data
  nobody intended to be real.
DISCONFIRMING_OBSERVATION: >
  Attendance recorded under a test configuration appears in or affects live production reporting.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Where a test/sandbox configuration exists, record attendance there and check for leakage into
  production reporting.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q033

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q033
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two concurrent corrections to the same attendance record by two different reviewers do not result
  in one correction silently overwriting the other with no conflict indication.
WHY_IT_MATTERS: >
  A silently lost correction on attendance data can leave a record in a state nobody actually chose,
  and nobody knows to re-check.
DISCONFIRMING_OBSERVATION: >
  Two concurrent corrections to the same attendance record result in one being silently discarded
  with no conflict shown to either reviewer.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Open the same attendance record in two sessions and submit conflicting corrections at nearly the
  same time.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q034

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q034
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Exporting attendance-derived time entries for external handling presents the same duration figures
  as the internal view, without silent re-derivation or re-rounding specific to the export path.
WHY_IT_MATTERS: >
  An export that silently recomputes figures differently from the internal record undermines
  confidence in whichever figure an external recipient actually sees.
DISCONFIRMING_OBSERVATION: >
  An exported derived time entry's duration differs from the same entry's duration shown in the
  internal view.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Export a derived time entry and compare its duration against the internal view of the same entry.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q035

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q035
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where geolocation or device identity is captured alongside a check-in/check-out, a mismatch
  between the expected work location and the captured location is at least flagged, not silently
  accepted as an ordinary attendance event.
WHY_IT_MATTERS: >
  An unflagged location mismatch removes the one signal most likely to catch attendance recorded
  from somewhere the employee was not actually expected to be.
DISCONFIRMING_OBSERVATION: >
  A check-in captured at a location clearly inconsistent with the employee's expected work location
  is accepted with no flag.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Where location capture exists, record a check-in from a location inconsistent with the employee's
  expected work site and check for a flag.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q036

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q036
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A derived time entry generated from attendance can still be reassigned to a different task or
  project after generation, without breaking its traceable link back to the originating attendance
  record.
WHY_IT_MATTERS: >
  If reassignment breaks the link to the source attendance, the entry loses its evidentiary backing
  the moment anyone tries to correct its attribution.
DISCONFIRMING_OBSERVATION: >
  Reassigning a derived entry to a different task or project removes its traceable reference back to
  the originating attendance record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate a derived entry, reassign it to a different task or project, and check whether its
  attendance origin remains traceable.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q037

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q037
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Deleting an attendance-derived time entry directly does not silently reopen or alter the state of
  its originating attendance record as an unannounced side effect.
WHY_IT_MATTERS: >
  A side effect that reaches back into the source attendance record from an action on the derived
  entry is a hidden coupling a reviewer would not expect.
DISCONFIRMING_OBSERVATION: >
  Deleting a derived time entry changes the state or content of its originating attendance record.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Delete a derived time entry and inspect its originating attendance record for any unexpected
  change.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q038

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q038
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An employee's assigned working schedule (expected hours or shift pattern) is used, where
  configured, to flag attendance that falls outside it, rather than every attendance event being
  treated as equally expected regardless of the assigned schedule.
WHY_IT_MATTERS: >
  Without comparing actual attendance to the assigned schedule, unusual patterns such as consistent
  lateness or unscheduled work go completely unnoticed.
DISCONFIRMING_OBSERVATION: >
  Attendance clearly outside an employee's assigned schedule is treated identically to attendance
  within it, with no flag anywhere.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record attendance outside an employee's assigned schedule and inspect whether it is flagged.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q039

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q039
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A bulk correction affecting many employees' attendance records in one operation produces a
  per-record trace for each affected record, not a single undifferentiated bulk-action log line.
WHY_IT_MATTERS: >
  A single generic log line for a bulk correction makes it impossible to review which specific
  employees and values actually changed.
DISCONFIRMING_OBSERVATION: >
  A bulk correction across several employees' attendance records produces one generic log entry with
  no way to see which specific records and values changed.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Perform a bulk correction across several employees' attendance records and inspect the resulting
  trace.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q040

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q040
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An attendance-derived time entry that has already been consumed downstream — used in a cost
  calculation or an already-closed report — is either protected from silent further change or
  clearly flags that a change occurred after downstream use.
WHY_IT_MATTERS: >
  A silent change to figures already relied upon downstream breaks the link between what was
  reported and what the record now shows.
DISCONFIRMING_OBSERVATION: >
  A derived entry already used downstream is altered with the same unqualified experience as one that
  has not yet been used anywhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Carry a derived entry through to downstream use, then attempt to alter it, either directly or
  through its source attendance record.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q041

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q041
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Filtering or searching attendance-derived time entries by employee, project, or date range returns
  a result consistent with the same criteria applied manually against the full record set.
WHY_IT_MATTERS: >
  A filter that silently disagrees with a manual check undermines confidence in every filtered
  report produced from the same data.
DISCONFIRMING_OBSERVATION: >
  A filtered view of attendance-derived entries omits or includes entries that a manual check of the
  same criteria against the full set would not.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Apply a filter to attendance-derived entries and compare its result against a manual check of the
  same criteria.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q042

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q042
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A check-in or check-out timestamp, once recorded, is captured using a single consistent time
  reference (such as server time rather than the reporting device's own local clock), so two
  employees checking in from devices with different clock settings are not recorded with
  inconsistent, incomparable timestamps.
WHY_IT_MATTERS: >
  Attendance timestamps sourced from uncontrolled device clocks cannot be reliably compared or
  sequenced against each other.
DISCONFIRMING_OBSERVATION: >
  Two check-ins recorded at the same actual moment from devices with different local clock settings
  are stored with different timestamps not attributable to real time zone differences.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record check-ins from two devices with deliberately different local clock settings and compare the
  stored timestamps.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q043

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q043
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An attendance record inherited or migrated from a prior period retains the same derived time entry
  linkage as one created natively in the current period, rather than presenting as unlinked or
  differently structured historical data.
WHY_IT_MATTERS: >
  Migrated historical attendance that loses its derived-entry linkage becomes unusable for any
  later reconciliation against the same period's timesheet data.
DISCONFIRMING_OBSERVATION: >
  An attendance record from a prior period, after migration or carry-forward, shows no linkage to its
  derived time entry that a natively created record of the same kind would show.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Where historical attendance data has been migrated or carried forward, inspect its linkage to
  derived time entries against a natively created equivalent.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q044

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q044
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A shift assignment change made after attendance for that shift has already been recorded does not
  retroactively alter which shift the already-recorded attendance is attributed to.
WHY_IT_MATTERS: >
  Retroactive shift reattribution would silently rewrite which schedule an already-completed
  attendance event is judged against.
DISCONFIRMING_OBSERVATION: >
  Changing an employee's shift assignment after attendance was recorded changes which shift that
  earlier attendance record is now attributed to.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record attendance under one shift assignment, change the shift assignment, and inspect the earlier
  attendance record's attribution.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q045

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q045
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting an attendance record outright is distinguishable in the audit trail from a day on which no
  attendance was ever recorded, so a reviewer can tell that something was removed.
WHY_IT_MATTERS: >
  An undetectable deletion of an attendance record is indistinguishable from an absence that never
  needed explaining, defeating any audit of removed records.
DISCONFIRMING_OBSERVATION: >
  Deleting an attendance record leaves no trace distinguishing that day's history from one on which
  no attendance was ever recorded.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create and then delete an attendance record, and inspect whether any trace of its prior existence
  remains auditable.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q046

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q046
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The full lifecycle of a derived time entry — the originating check-in and check-out, any
  correction to either, and the resulting entry's own history — can be reconstructed end to end from
  stored records alone, without relying on anyone's recollection.
WHY_IT_MATTERS: >
  If this lifecycle cannot be reconstructed from records, a payroll or billing dispute over
  attendance-derived time has no way to be settled on evidence alone.
DISCONFIRMING_OBSERVATION: >
  The full lifecycle of a derived entry, including a correction to its source attendance, cannot be
  fully reconstructed from stored records alone.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Take an attendance record through creation, correction, and derivation into a time entry, then
  attempt to reconstruct the full timeline from stored records alone.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q047

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q047
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where an employee can submit their own correction request for a missed check-in or check-out, that
  request requires approval before it changes the actual attendance record, rather than the
  employee's own submission taking effect immediately and unreviewed.
WHY_IT_MATTERS: >
  Self-submitted attendance corrections taking effect without review remove the independent check
  that makes attendance data trustworthy in the first place.
DISCONFIRMING_OBSERVATION: >
  An employee's self-submitted correction to their own attendance record takes effect immediately
  with no approval step.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Where self-service correction exists, submit a correction as the employee and check whether it
  requires approval before taking effect.
```

## G12-HR_TIMESHEET_ATTENDANCE-Q048

```yaml
QID: G12-HR_TIMESHEET_ATTENDANCE-Q048
MODULE: hr_timesheet_attendance
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether attendance-derived time entries are billable or non-billable by default follows the same
  configuration rule applied to manually entered time on the same task, rather than an independent,
  possibly inconsistent default specific to the attendance-derived path.
WHY_IT_MATTERS: >
  An inconsistent billable default between manual and attendance-derived entries for the same task
  can silently misstate what is actually billable for that work.
DISCONFIRMING_OBSERVATION: >
  A manually entered time entry and an attendance-derived entry for the same task carry different
  billable defaults with no explicit configuration explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare the billable default of a manually entered time entry and an attendance-derived entry for
  the same task.
```
