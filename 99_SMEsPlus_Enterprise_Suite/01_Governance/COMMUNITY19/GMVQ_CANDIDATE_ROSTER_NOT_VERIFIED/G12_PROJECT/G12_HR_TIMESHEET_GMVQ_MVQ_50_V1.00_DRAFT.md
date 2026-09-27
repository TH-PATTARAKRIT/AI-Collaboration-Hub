# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / hr_timesheet Module MVQ Bank

**Document ID:** GMVQ-G12-HR_TIMESHEET-MVQ50-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `hr_timesheet`
**Wave:** W3
**Author Cell:** P12-1 (GMVQ Question Factory — Production Cell P12-1)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for logged working time entered against tasks or
projects by employees: entry validity, rate and cost consistency, approval and lock-period
integrity, and the boundary between an employee's own entries and what a manager can see or change.
Material ground: entry-time validation, historical rate integrity after a change, lock/approval
period enforcement, employee-versus-manager visibility, and reconciliation between an entry's task
context and its cost attribution.

Question text is source-neutral. It does not name the module, any vendor or product, or any
technical identifier (field, model, method, XML ID, API path).

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 50 questions exist because each tests a distinct material hypothesis, spread across
  the required dimensions (business capability, business rule, state transition, configuration
  dependency, role and permission, exception path, cancellation, reversal, negative case,
  cross-module dependency, optional behaviour, auditability, tenant/company boundary, concurrency
  and ordering, runtime reachability, configuration reachability).
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G12-HR_TIMESHEET-Q001

```yaml
QID: G12-HR_TIMESHEET-Q001
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A time entry cannot be saved with a negative duration; the system rejects it rather than accepting
  a value that would subtract from totals.
WHY_IT_MATTERS: >
  A negative duration accepted as an ordinary entry silently corrupts every total that sums entries
  without expecting a negative.
DISCONFIRMING_OBSERVATION: >
  A time entry with a negative duration is accepted and saved without rejection or warning.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to create a time entry with a negative duration value.
```

## G12-HR_TIMESHEET-Q002

```yaml
QID: G12-HR_TIMESHEET-Q002
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A time entry can be created without being linked to a specific task, at least where the
  configuration permits task-less logging, and such an entry is still fully counted in
  project-level and employee-level totals.
WHY_IT_MATTERS: >
  If task-less entries are silently excluded from totals, an employee's logged time can be
  materially understated without any visible warning.
DISCONFIRMING_OBSERVATION: >
  An entry logged without a task link is missing from a total that should include all logged time
  for that employee or project.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a time entry without a linked task, where permitted, and check whether it appears in
  relevant totals.
```

## G12-HR_TIMESHEET-Q003

```yaml
QID: G12-HR_TIMESHEET-Q003
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Once a time entry has been approved, an ordinary edit to its duration or date is either blocked or
  produces a visible, distinct trace, rather than silently altering an already-approved record.
WHY_IT_MATTERS: >
  An approval that can be silently undone by a later edit provides no real control over what was
  actually authorized.
DISCONFIRMING_OBSERVATION: >
  An approved time entry's duration or date is changed with no distinguishing indication that it
  differs from an edit to an entry that was never approved.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Approve a time entry, then edit its duration or date, and inspect what trace, if any, distinguishes
  this from editing an unapproved entry.
```

## G12-HR_TIMESHEET-Q004

```yaml
QID: G12-HR_TIMESHEET-Q004
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A defined lock or validation period prevents new or edited time entries from being recorded with a
  date falling inside that already-closed period, for every entry path, not only the primary
  interactive one.
WHY_IT_MATTERS: >
  A lock period enforced on one entry path but bypassable through another gives no real assurance
  that closed periods stay closed.
DISCONFIRMING_OBSERVATION: >
  A time entry dated inside a locked period is accepted through some entry path even though it would
  be rejected through another.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Lock a period and attempt to create or edit an entry dated within it through more than one
  available entry path.
```

## G12-HR_TIMESHEET-Q005

```yaml
QID: G12-HR_TIMESHEET-Q005
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An employee attempting to view or edit another employee's time entries is blocked unless they hold
  an explicit manager or administrative relationship to that employee.
WHY_IT_MATTERS: >
  Timesheet content can reveal what an employee is working on, for whom, and at what pace; unrestrained
  peer visibility is an unwanted disclosure.
DISCONFIRMING_OBSERVATION: >
  An employee with no manager or administrative relationship to a colleague can view or edit that
  colleague's time entries.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As an employee with no management relationship to a colleague, attempt to view or edit that
  colleague's time entries.
```

## G12-HR_TIMESHEET-Q006

```yaml
QID: G12-HR_TIMESHEET-Q006
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing an employee's cost rate does not retroactively change the cost attributed to time entries
  that were logged and already used in cost or billing calculations before the rate changed.
WHY_IT_MATTERS: >
  Retroactive rate reattribution would silently rewrite historical cost figures that may already have
  been reported, invoiced, or reconciled.
DISCONFIRMING_OBSERVATION: >
  After a cost-rate change, a previously logged and already-processed time entry's recorded cost
  updates to reflect the new rate.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Log a time entry, let it be used in a cost calculation, change the employee's cost rate, then
  re-inspect the earlier entry's recorded cost.
```

## G12-HR_TIMESHEET-Q007

```yaml
QID: G12-HR_TIMESHEET-Q007
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A time entry that has already been invoiced or otherwise consumed downstream is either prevented
  from further editing or produces a clear, visible warning that it is being altered after
  downstream use.
WHY_IT_MATTERS: >
  Editing time that has already been billed without any warning breaks the link between what was
  billed and what the record now shows.
DISCONFIRMING_OBSERVATION: >
  A time entry already consumed downstream is edited with the same unqualified experience as an
  entry that has not yet been used anywhere.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Carry a time entry through to downstream use, then attempt to edit its duration or date.
```

## G12-HR_TIMESHEET-Q008

```yaml
QID: G12-HR_TIMESHEET-Q008
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Duration values entered in different units (such as hours and a fractional-day equivalent) are
  converted using one consistent rule everywhere they are compared or totalled.
WHY_IT_MATTERS: >
  Inconsistent unit conversion silently distorts totals wherever two entries recorded in different
  units are combined.
DISCONFIRMING_OBSERVATION: >
  The same underlying amount of time entered in two different accepted units produces different
  totals when combined in a report.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enter equivalent amounts of time using two different accepted units and compare their combined
  total against the expected equivalent.
```

## G12-HR_TIMESHEET-Q009

```yaml
QID: G12-HR_TIMESHEET-Q009
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A running timer used to log time captures elapsed duration accurately and consistently, including
  across a browser refresh or a brief disconnect, rather than losing or inflating the interval.
WHY_IT_MATTERS: >
  A timer that silently loses accuracy across ordinary interruptions produces time records the
  employee never actually reviewed or confirmed.
DISCONFIRMING_OBSERVATION: >
  Elapsed time recorded by the timer differs materially from the actual elapsed wall-clock time after
  an ordinary interruption such as a page refresh.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Start a timer, allow a known interval to elapse including an interruption such as a refresh, stop
  it, and compare recorded duration to actual elapsed time.
```

## G12-HR_TIMESHEET-Q010

```yaml
QID: G12-HR_TIMESHEET-Q010
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A running timer left active across a date boundary attributes the resulting duration to a date in a
  defined, consistent way, rather than an arbitrary or undocumented split.
WHY_IT_MATTERS: >
  An undocumented date attribution for overnight timers makes daily totals unreliable exactly on the
  days most likely to be scrutinised.
DISCONFIRMING_OBSERVATION: >
  Stopping a timer that ran across midnight produces a date attribution that is inconsistent between
  repeated, otherwise identical attempts.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Start a timer before midnight, stop it after midnight, and inspect which date the resulting entry
  is attributed to, repeating to check consistency.
```

## G12-HR_TIMESHEET-Q011

```yaml
QID: G12-HR_TIMESHEET-Q011
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Attempting to log time against a project that has time-tracking disabled is blocked with a clear
  message, rather than silently accepted and then excluded from that project's reporting.
WHY_IT_MATTERS: >
  A silently accepted but silently excluded entry gives the employee false confidence their time was
  recorded when it effectively was not counted anywhere useful.
DISCONFIRMING_OBSERVATION: >
  A time entry is accepted against a project with time-tracking disabled, but the entry does not
  appear in any subsequent reporting for that project, with no warning given at entry time.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Disable time tracking on a project and attempt to log a time entry against it.
```

## G12-HR_TIMESHEET-Q012

```yaml
QID: G12-HR_TIMESHEET-Q012
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A bulk import of time entries applies the same validation rules — date range, negative duration,
  lock period — as an entry created interactively, rather than bypassing checks that the interactive
  path enforces.
WHY_IT_MATTERS: >
  A bulk path with weaker validation is a much larger-volume bypass of the same controls than any
  single interactive entry could achieve.
DISCONFIRMING_OBSERVATION: >
  An import file containing an entry that would be rejected interactively (negative duration, locked
  period date) is accepted through bulk import.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Construct an import file containing an entry that fails interactive validation and import it.
```

## G12-HR_TIMESHEET-Q013

```yaml
QID: G12-HR_TIMESHEET-Q013
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reversing an approval on a time entry — sending it back to unapproved — is itself a distinct,
  auditable action, not indistinguishable from the entry never having been approved at all.
WHY_IT_MATTERS: >
  A reversal that leaves no trace makes it impossible to tell later whether an entry was approved and
  then reconsidered, or simply never reviewed.
DISCONFIRMING_OBSERVATION: >
  After an approval is reversed, the entry's history shows no distinguishable record that an approval
  ever occurred and was withdrawn.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Approve a time entry, then reverse the approval, and inspect the entry's history.
```

## G12-HR_TIMESHEET-Q014

```yaml
QID: G12-HR_TIMESHEET-Q014
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Multiple time entries can be approved together in a single manager action, and doing so produces
  the same per-entry approval record as approving each one individually, rather than a single
  undifferentiated batch record.
WHY_IT_MATTERS: >
  A batch approval that cannot be traced back to individual entries makes it impossible to later
  determine exactly which entries a specific approval action actually covered.
DISCONFIRMING_OBSERVATION: >
  A batch approval action produces one generic record with no way to determine which specific entries
  were included.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Approve several time entries together in one action and inspect the resulting per-entry approval
  trace.
```

## G12-HR_TIMESHEET-Q015

```yaml
QID: G12-HR_TIMESHEET-Q015
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A description field on a time entry, where required by configuration, is actually enforced as
  mandatory at the point of saving, not merely suggested and skippable.
WHY_IT_MATTERS: >
  A configuration that claims description is mandatory but does not enforce it produces a false sense
  of data quality across every downstream report relying on that description.
DISCONFIRMING_OBSERVATION: >
  With description configured as mandatory, a time entry is saved successfully with the description
  left blank.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure description as mandatory and attempt to save a time entry with it left blank.
```

## G12-HR_TIMESHEET-Q016

```yaml
QID: G12-HR_TIMESHEET-Q016
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A time entry logged by an employee scoped to one company cannot be logged against, or attributed
  to, a project scoped to a different company.
WHY_IT_MATTERS: >
  A cross-company time entry would misattribute cost and effort across a boundary the whole
  multi-company model depends on staying intact.
DISCONFIRMING_OBSERVATION: >
  An employee scoped to one company successfully logs a time entry against a project scoped to a
  different company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As an employee scoped to one company, attempt to log time against a project scoped to a different
  company.
```

## G12-HR_TIMESHEET-Q017

```yaml
QID: G12-HR_TIMESHEET-Q017
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Moving a task that has logged time entries to a different project moves the association of those
  time entries consistently, so effort reporting for both the old and new project remains accurate
  rather than double-counting or losing the effort.
WHY_IT_MATTERS: >
  Effort silently duplicated or lost across a task move distorts cost and productivity reporting for
  both projects involved.
DISCONFIRMING_OBSERVATION: >
  After moving a task with logged time to a different project, the effort appears under both projects,
  or under neither, in reporting.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Log time against a task, move that task to a different project, and inspect effort reporting for
  both projects.
```

## G12-HR_TIMESHEET-Q018

```yaml
QID: G12-HR_TIMESHEET-Q018
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Entering a duplicate time entry — same employee, task, date, and duration as an existing one — is
  either flagged as a likely duplicate or accepted deliberately as a legitimate second entry, but the
  behaviour is consistent and not arbitrary.
WHY_IT_MATTERS: >
  Inconsistent duplicate handling means the same honest mistake sometimes gets caught and sometimes
  silently doubles reported effort.
DISCONFIRMING_OBSERVATION: >
  Submitting the same entry twice under identical conditions is flagged once and silently accepted
  another time, with no configuration explaining the difference.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Submit an identical time entry twice under the same conditions and compare outcomes across
  repeated attempts.
```

## G12-HR_TIMESHEET-Q019

```yaml
QID: G12-HR_TIMESHEET-Q019
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An employee is warned, or the system otherwise indicates, when two of their own entries on the same
  day overlap in time, rather than allowing an employee to appear logged to two tasks at once with no
  indication.
WHY_IT_MATTERS: >
  Overlapping entries usually indicate a data-entry mistake; silently accepting them without any
  signal removes the easiest opportunity to catch the error.
DISCONFIRMING_OBSERVATION: >
  Two entries for the same employee on the same day with overlapping time ranges are both accepted
  with no warning of the overlap.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create two overlapping time entries for the same employee on the same day.
```

## G12-HR_TIMESHEET-Q020

```yaml
QID: G12-HR_TIMESHEET-Q020
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Logging time on a day marked as a public holiday or the employee's day off produces at least a
  visible flag, rather than being treated identically to any ordinary working day with no
  distinction.
WHY_IT_MATTERS: >
  Unflagged holiday or off-day logging hides exactly the pattern a manager would want to review,
  whether for accuracy or for policy compliance.
DISCONFIRMING_OBSERVATION: >
  A time entry logged on a known holiday or scheduled day off is displayed identically to an entry on
  a normal working day, with no flag anywhere.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Log a time entry on a day configured as a holiday or day off for that employee and inspect how it
  is displayed.
```

## G12-HR_TIMESHEET-Q021

```yaml
QID: G12-HR_TIMESHEET-Q021
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Backdating a time entry beyond a defined lock or grace period requires an explicit override
  distinct from an ordinary entry made within the grace period.
WHY_IT_MATTERS: >
  Without a distinct override step, stale backdated entries are indistinguishable from timely ones,
  undermining any review process that relies on entry timeliness.
DISCONFIRMING_OBSERVATION: >
  An entry backdated well beyond the defined grace period is saved through the same unqualified
  action as an entry made promptly, with no override step or trace.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Attempt to create an entry dated well beyond the configured grace period and inspect what, if
  anything, distinguishes the action from a prompt entry.
```

## G12-HR_TIMESHEET-Q022

```yaml
QID: G12-HR_TIMESHEET-Q022
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A task's total logged time shown to a viewer reflects the same underlying figure regardless of
  whether that viewer reaches it through the task itself, a project-level report, or an
  employee-level report.
WHY_IT_MATTERS: >
  A total that disagrees depending on which report produced it means at least one of those reports is
  simply wrong, and nobody can tell which.
DISCONFIRMING_OBSERVATION: >
  The same task's total logged time differs between the task view, a project-level report, and an
  employee-level report covering the same period.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Log time against a task and compare its total across the task view, a project report, and an
  employee report.
```

## G12-HR_TIMESHEET-Q023

```yaml
QID: G12-HR_TIMESHEET-Q023
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting a task that has associated time entries either prevents the deletion or preserves the time
  entries as historical records rather than deleting the logged time silently along with the task.
WHY_IT_MATTERS: >
  Silent loss of logged time as a side effect of an unrelated task deletion destroys cost and
  productivity history with no one deciding to discard it.
DISCONFIRMING_OBSERVATION: >
  Deleting a task removes its associated time entries with no warning or preservation, indistinguishable
  from deleting a task with no logged time.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Log time against a task and attempt to delete that task, inspecting what happens to the time
  entries.
```

## G12-HR_TIMESHEET-Q024

```yaml
QID: G12-HR_TIMESHEET-Q024
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The cost figure attached to a time entry for internal reporting is not exposed to a viewer who is
  only authorized to see the entry's duration and description, such as a customer-facing or portal
  context.
WHY_IT_MATTERS: >
  Internal cost data leaking into a customer-facing surface reveals margin and staffing cost
  information that has nothing to do with what the customer was meant to see.
DISCONFIRMING_OBSERVATION: >
  A viewer scoped to duration-and-description-only visibility can see the entry's internal cost
  figure through some available surface.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a viewer scoped to duration-only visibility, attempt to reach the internal cost figure for a
  time entry through every available surface.
```

## G12-HR_TIMESHEET-Q025

```yaml
QID: G12-HR_TIMESHEET-Q025
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The distribution of a time entry's cost across an analytic or cost-tracking dimension, where
  configured, is consistent with the actual project and task the entry was logged against, not an
  independently editable value that can drift from the entry's own context.
WHY_IT_MATTERS: >
  A cost distribution that can silently disagree with the entry's own task or project produces cost
  reporting that does not actually reflect where the work happened.
DISCONFIRMING_OBSERVATION: >
  A time entry's cost distribution attributes it to a project or cost dimension different from the
  one the entry itself is logged against, with no explicit override recorded.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Log a time entry against a specific task and project and inspect its cost-distribution attribution
  for consistency.
```

## G12-HR_TIMESHEET-Q026

```yaml
QID: G12-HR_TIMESHEET-Q026
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A time entry can be flagged as an overtime or exception category, where such categorisation is
  configured, without that flag silently altering the entry's own recorded duration.
WHY_IT_MATTERS: >
  A categorisation flag that also changes the recorded number conflates two distinct pieces of
  information a reviewer needs to see separately.
DISCONFIRMING_OBSERVATION: >
  Marking an entry as an overtime or exception category changes its recorded duration value.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Where an overtime or exception category exists, apply it to an entry and compare the recorded
  duration before and after.
```

## G12-HR_TIMESHEET-Q027

```yaml
QID: G12-HR_TIMESHEET-Q027
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A correction to a previously submitted time entry is made through a new, separately visible
  adjustment rather than editing the original figure in place and losing what was originally
  recorded.
WHY_IT_MATTERS: >
  An in-place edit to an already-reviewed figure erases the ability to see what was originally
  reported before the correction.
DISCONFIRMING_OBSERVATION: >
  Correcting a previously submitted entry overwrites the original value with no separately visible
  trace of what it originally was.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit a time entry, then correct its duration, and inspect whether the original value remains
  traceable.
```

## G12-HR_TIMESHEET-Q028

```yaml
QID: G12-HR_TIMESHEET-Q028
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Exporting time entries for external handling masks or omits any internal cost figure by default,
  showing only duration and description unless cost is explicitly requested.
WHY_IT_MATTERS: >
  A routine export intended for scheduling or billing purposes should not casually leak internal cost
  data to whoever ends up handling the file.
DISCONFIRMING_OBSERVATION: >
  A standard export of time entries includes the internal cost figure by default with no explicit
  request for it.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Produce a standard export of time entries and inspect whether cost figures are included by
  default.
```

## G12-HR_TIMESHEET-Q029

```yaml
QID: G12-HR_TIMESHEET-Q029
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A time entry submitted through an integration or automated feed is subject to the same validation
  — lock period, negative duration, mandatory fields — as one entered interactively.
WHY_IT_MATTERS: >
  An automated feed with looser validation than the interactive path becomes the easiest route to
  inject invalid time data at volume.
DISCONFIRMING_OBSERVATION: >
  A time entry that would fail interactive validation is accepted through an integration or
  automated feed.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Submit an entry that fails interactive validation through an integration path and compare the
  outcome.
```

## G12-HR_TIMESHEET-Q030

```yaml
QID: G12-HR_TIMESHEET-Q030
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An employee terminated or deactivated mid-period retains their previously logged entries for that
  period unchanged and reportable, rather than the entries becoming inaccessible or being silently
  dropped from reporting.
WHY_IT_MATTERS: >
  A terminated employee's already-logged time is still real historical cost and effort that closing
  reports depend on.
DISCONFIRMING_OBSERVATION: >
  Deactivating an employee causes their previously logged, otherwise valid time entries to disappear
  from or become unreachable in period reporting.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Log time for an employee, deactivate that employee, and inspect whether their entries remain
  reportable for the period already logged.
```

## G12-HR_TIMESHEET-Q031

```yaml
QID: G12-HR_TIMESHEET-Q031
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two entries created concurrently for the same employee, task, and moment are not silently merged or
  one silently discarded without any indication to the entrant.
WHY_IT_MATTERS: >
  Silent merging or discarding under concurrent submission can lose legitimately distinct entries
  made close together, such as separate short tasks.
DISCONFIRMING_OBSERVATION: >
  Submitting two distinct, legitimate entries for the same employee and task in quick succession
  results in only one being retained with no indication of the loss.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Submit two distinct entries for the same employee and task in rapid succession and verify both are
  retained.
```

## G12-HR_TIMESHEET-Q032

```yaml
QID: G12-HR_TIMESHEET-Q032
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A minimum or maximum single-entry duration limit, where configured, is enforced consistently
  across every entry path rather than only on the primary interactive form.
WHY_IT_MATTERS: >
  A limit enforced on only one path is trivially bypassed through any other, defeating whatever
  business reason set the limit.
DISCONFIRMING_OBSERVATION: >
  An entry violating a configured duration limit is rejected through one entry path but accepted
  through another.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a duration limit and attempt to violate it through more than one entry path.
```

## G12-HR_TIMESHEET-Q033

```yaml
QID: G12-HR_TIMESHEET-Q033
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reassigning a time entry from one task to another preserves the entry's own history — who logged
  it and when — rather than the reassignment presenting as though the entry originated on the new
  task from the start.
WHY_IT_MATTERS: >
  A reassignment that erases the entry's original context makes any later review of task history
  incomplete or misleading.
DISCONFIRMING_OBSERVATION: >
  After reassigning a time entry to a different task, its history no longer shows when it was
  originally logged or against which task.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Log a time entry against one task, reassign it to a different task, and inspect its history.
```

## G12-HR_TIMESHEET-Q034

```yaml
QID: G12-HR_TIMESHEET-Q034
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Rounding applied to entered durations, where configured, is applied identically regardless of
  whether the entry came from a manual field, a timer, or an import.
WHY_IT_MATTERS: >
  Inconsistent rounding between entry paths introduces small but systematic discrepancies that
  compound across large volumes of entries.
DISCONFIRMING_OBSERVATION: >
  The same raw duration produces a different rounded result depending on whether it was entered
  manually, via a timer, or through import.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enter an identical raw duration through a manual field, a timer, and an import, and compare the
  rounded results.
```

## G12-HR_TIMESHEET-Q035

```yaml
QID: G12-HR_TIMESHEET-Q035
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An employee cannot approve their own time entries even where they hold a role that can approve
  entries generally, unless that self-approval is an explicit, documented exception.
WHY_IT_MATTERS: >
  Self-approval defeats the purpose of an approval control on the exact records most likely to be
  disputed or inflated.
DISCONFIRMING_OBSERVATION: >
  An employee holding approval rights successfully approves their own time entries with no
  documented exception permitting it.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As an employee with approval rights, attempt to approve one of your own time entries.
```

## G12-HR_TIMESHEET-Q036

```yaml
QID: G12-HR_TIMESHEET-Q036
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A time entry logged against a task that is later cancelled remains visible and reportable as
  historical effort, rather than disappearing along with the cancelled task.
WHY_IT_MATTERS: >
  Real time was spent even if the task was ultimately cancelled; losing that record understates
  actual effort expended.
DISCONFIRMING_OBSERVATION: >
  Cancelling a task removes or hides the time entries that were logged against it before
  cancellation.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Log time against a task, cancel the task, and inspect whether the logged time remains visible and
  reportable.
```

## G12-HR_TIMESHEET-Q037

```yaml
QID: G12-HR_TIMESHEET-Q037
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A weekly or periodic timesheet summary view totals exactly the same set of entries as would be
  found by listing and summing individual entries for that same period, with no entries silently
  excluded from the summary.
WHY_IT_MATTERS: >
  A summary total that quietly excludes some entries misrepresents actual logged effort to whoever
  relies on the summary rather than the detail.
DISCONFIRMING_OBSERVATION: >
  The periodic summary total differs from a manual sum of the individual entries for the same
  employee and period.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Log several entries across a period and compare the periodic summary total to a manual sum of the
  individual entries.
```

## G12-HR_TIMESHEET-Q038

```yaml
QID: G12-HR_TIMESHEET-Q038
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A negative-value correction entry used to reverse a previously logged, already-processed amount is
  itself traceable back to the specific original entry it corrects, not a standalone figure with no
  link to what it is adjusting.
WHY_IT_MATTERS: >
  An untraceable correction makes it impossible to later verify that a reversal actually offsets the
  right original entry and nothing else.
DISCONFIRMING_OBSERVATION: >
  A correction entry reversing previously processed time carries no reference back to the specific
  original entry being corrected.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Issue a correction entry reversing a previously processed amount and inspect whether it references
  the original entry.
```

## G12-HR_TIMESHEET-Q039

```yaml
QID: G12-HR_TIMESHEET-Q039
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a default task or activity exists for time entries with no explicit task selected, that
  default is applied consistently and is itself visible to the employee, not an invisible fallback
  that only shows up in reports.
WHY_IT_MATTERS: >
  An invisible default silently attributes effort to a task the employee never actually chose or
  saw, undermining the accuracy of that task's own reporting.
DISCONFIRMING_OBSERVATION: >
  An entry saved without an explicit task selection is later found attributed to a default task that
  was never shown to the employee at entry time.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Save an entry without explicitly selecting a task, where a default exists, and check what the
  employee actually saw versus what was recorded.
```

## G12-HR_TIMESHEET-Q040

```yaml
QID: G12-HR_TIMESHEET-Q040
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A manager who both assigns a task and approves the time logged against it is not the sole reviewer
  for entries flagged as materially exceeding the task's planned estimate; some further review point
  exists for that specific exception.
WHY_IT_MATTERS: >
  Combining task assignment, effort logging, and its own approval in one person removes any
  independent check on significant overruns specifically.
DISCONFIRMING_OBSERVATION: >
  An entry materially exceeding its task's planned estimate is approved solely by the same person who
  assigned the task, with no further review point triggered.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Log an entry materially exceeding its task's planned estimate and trace who reviews or approves it.
```

## G12-HR_TIMESHEET-Q041

```yaml
QID: G12-HR_TIMESHEET-Q041
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Filtering time entries by employee, task, or date range in a report returns a result consistent
  with filtering by the same criteria applied manually to the full entry list.
WHY_IT_MATTERS: >
  A filter that silently disagrees with a manual check undermines confidence in every filtered
  report produced from the same data.
DISCONFIRMING_OBSERVATION: >
  A filtered report omits or includes entries that a manual check of the same filter criteria against
  the full entry list would not.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Apply a filter to a report and compare its result against a manual check of the same criteria on
  the full entry list.
```

## G12-HR_TIMESHEET-Q042

```yaml
QID: G12-HR_TIMESHEET-Q042
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An entry's currency, where a cost figure is expressed in one, is fixed at the currency in effect
  when the entry was logged and does not silently convert using a later exchange rate when viewed
  afterward.
WHY_IT_MATTERS: >
  A silently re-converted historical figure no longer represents the actual cost recognised at the
  time the work happened.
DISCONFIRMING_OBSERVATION: >
  Viewing a previously logged entry's cost figure at a later date, after an exchange rate change,
  shows a different converted amount than what was originally recorded.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Log an entry with a cost figure in a given currency, change the relevant exchange rate, and
  re-inspect the entry's recorded cost.
```

## G12-HR_TIMESHEET-Q043

```yaml
QID: G12-HR_TIMESHEET-Q043
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A time entry logged against a task can still be logged when the task's own deadline has already
  passed, without the entry itself being silently blocked or its date silently coerced to the
  deadline.
WHY_IT_MATTERS: >
  Real work performed after a deadline is legitimate historical fact; blocking or distorting its
  entry would misrepresent what actually happened.
DISCONFIRMING_OBSERVATION: >
  Logging time against a task whose deadline has passed is blocked outright, or the entry's date is
  silently altered to match the deadline.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Attempt to log a time entry, dated after the fact, against a task whose deadline has already
  passed.
```

## G12-HR_TIMESHEET-Q044

```yaml
QID: G12-HR_TIMESHEET-Q044
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A change to which activities or task types are eligible for time logging does not retroactively
  invalidate or hide entries already logged under a type that is subsequently made ineligible.
WHY_IT_MATTERS: >
  Retroactively invalidating historical entries because a configuration changed later rewrites
  history based on a decision made after the fact.
DISCONFIRMING_OBSERVATION: >
  Making a task type ineligible for time logging causes previously logged entries of that type to
  disappear or show as invalid.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Log entries under a given task type, then make that type ineligible for logging, and inspect the
  earlier entries.
```

## G12-HR_TIMESHEET-Q045

```yaml
QID: G12-HR_TIMESHEET-Q045
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Deleting a time entry outright, as opposed to correcting it, is distinguishable in the audit trail
  from an entry that was simply never created, so a reviewer can tell that something was removed.
WHY_IT_MATTERS: >
  An undetectable deletion is indistinguishable from an entry that never existed, defeating any
  attempt to audit what was recorded and then removed.
DISCONFIRMING_OBSERVATION: >
  Deleting a time entry leaves no trace distinguishing the record's history from a period in which no
  entry was ever created.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create and then delete a time entry, and inspect whether any trace of its prior existence remains
  auditable.
```

## G12-HR_TIMESHEET-Q046

```yaml
QID: G12-HR_TIMESHEET-Q046
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A period-close or lock action applied by a manager to one employee's entries does not
  inadvertently lock entries belonging to a different employee that happen to fall in the same date
  range.
WHY_IT_MATTERS: >
  An overbroad lock could silently freeze another employee's still-open work, blocking their
  legitimate corrections without anyone intending that.
DISCONFIRMING_OBSERVATION: >
  Locking one employee's entries for a period also locks a different employee's entries for the same
  period who was not the intended target.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Apply a period lock scoped to one employee and check whether a different employee's entries for
  the same period are affected.
```

## G12-HR_TIMESHEET-Q047

```yaml
QID: G12-HR_TIMESHEET-Q047
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Time entries logged under a test or non-production configuration are not reachable by, or
  counted in, live production reporting under any shared-data condition.
WHY_IT_MATTERS: >
  Test entries leaking into production totals would silently distort cost and productivity figures
  with data nobody intended to be real.
DISCONFIRMING_OBSERVATION: >
  A time entry created under a test configuration appears in or affects a live production report.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Where a test/sandbox configuration exists alongside production, log an entry there and check for
  leakage into production reporting.
```

## G12-HR_TIMESHEET-Q048

```yaml
QID: G12-HR_TIMESHEET-Q048
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An employee viewing their own timesheet on a portal or self-service surface sees the same totals as
  a manager viewing the same employee's timesheet through the internal, non-portal view.
WHY_IT_MATTERS: >
  A discrepancy between the employee-facing and manager-facing totals for the same data means one of
  the two is simply presenting a wrong figure.
DISCONFIRMING_OBSERVATION: >
  The same employee's period total differs between their own self-service view and their manager's
  internal view of the identical period.
EXPECTED_SURFACE: S1,S4,S5
PRECONDITIONS: >
  Compare an employee's own view of their period total against their manager's view of the same
  period.
```

## G12-HR_TIMESHEET-Q049

```yaml
QID: G12-HR_TIMESHEET-Q049
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The full sequence of a time entry's lifecycle — creation, any correction, approval, and any
  reversal — can be reconstructed end to end from stored records alone, without relying on anyone's
  recollection of what happened.
WHY_IT_MATTERS: >
  If the lifecycle of a disputed entry cannot be reconstructed from records, the audit trail has
  failed at its most basic purpose for exactly the records most likely to be questioned.
DISCONFIRMING_OBSERVATION: >
  The full lifecycle of an entry that was created, corrected, approved, and later reversed cannot be
  reconstructed from stored records alone.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Take an entry through creation, correction, approval, and reversal, then attempt to reconstruct
  the full timeline using only stored records.
```

## G12-HR_TIMESHEET-Q050

```yaml
QID: G12-HR_TIMESHEET-Q050
MODULE: hr_timesheet
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A search or filter for time entries by free-text description performs a genuine text match rather
  than silently ignoring the description criterion and returning an unfiltered or differently
  filtered result.
WHY_IT_MATTERS: >
  A search that silently ignores part of its own stated criteria misleads whoever relies on the
  filtered result being complete and accurate.
DISCONFIRMING_OBSERVATION: >
  A description-based search returns entries that do not match the given text, or omits entries that
  do, inconsistent with a manual text check.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Run a description-based search for a known term and compare the result against a manual check of
  entries actually containing that term.
```
