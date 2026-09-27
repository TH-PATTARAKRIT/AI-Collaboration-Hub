# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project Module MVQ Bank

**Document ID:** GMVQ-G12-PROJECT-MVQ50-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `project`
**Wave:** W3
**Author Cell:** P12-1 (GMVQ Question Factory — Production Cell P12-1)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the core project-management foundation
capability: projects, tasks, stages, milestones, dependencies, templates, and the portal-facing
surface of a project. As the strongest bank in the G12 group (Group Brief), it carries the core
project invariants that the group's bridge banks (project+expense, project+purchase, project+mrp,
project+stock, project+sale, project+account combinations) will later ask "what happens to this
invariant when a second capability is attached." Material ground: stage/lifecycle integrity,
template and recurrence fidelity, cross-company and portal boundary, dependency and scheduling
consistency, and auditability of ownership and configuration changes over time.

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

## G12-PROJECT-Q001

```yaml
QID: G12-PROJECT-Q001
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Archiving a project and deleting a project are distinct, reversible-versus-irreversible
  operations, not two labels for the same underlying action.
WHY_IT_MATTERS: >
  If archiving is silently destructive, a user reaching for the safer-sounding option loses data
  they believed was only being hidden.
DISCONFIRMING_OBSERVATION: >
  Archiving a project removes its tasks, history, or records in a way indistinguishable from
  deletion, or the two actions produce the same irreversible result.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a project with tasks, archive it and inspect what remains, then compare against deleting an
  equivalent project.
```

## G12-PROJECT-Q002

```yaml
QID: G12-PROJECT-Q002
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting a project that still holds active, incomplete tasks either blocks the deletion or
  surfaces an explicit warning naming what will be lost, rather than deleting silently.
WHY_IT_MATTERS: >
  Silent loss of incomplete work is far more damaging than the same loss after an explicit warning
  the user could have stopped.
DISCONFIRMING_OBSERVATION: >
  A project containing active, incomplete tasks is deleted with no warning distinguishing it from
  deleting an empty project.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a project with open tasks and attempt to delete the project outright.
```

## G12-PROJECT-Q003

```yaml
QID: G12-PROJECT-Q003
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A configured stage-change notification (email or message) fires reliably every time a task
  actually crosses that stage boundary, not only on some transitions and not on others reaching the
  same stage by a different path.
WHY_IT_MATTERS: >
  A notification rule that only sometimes fires is worse than no rule, because stakeholders learn to
  trust a signal that is not actually reliable.
DISCONFIRMING_OBSERVATION: >
  A task reaching the configured stage by drag-and-drop triggers the notification, but the same task
  reaching that stage through a bulk action or an automated rule does not, or vice versa.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Configure a stage-change notification, then move a task into that stage through at least two
  different mechanisms and compare outcomes.
```

## G12-PROJECT-Q004

```yaml
QID: G12-PROJECT-Q004
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Editing a single occurrence of a recurring task offers an explicit choice between changing only
  that occurrence and changing the whole series, rather than one silently affecting the other.
WHY_IT_MATTERS: >
  An edit intended for one occurrence that silently rewrites the whole series (or vice versa)
  destroys the planning value of recurrence.
DISCONFIRMING_OBSERVATION: >
  Editing one occurrence's date or content silently changes every other occurrence, or a change
  intended for the whole series applies to only one occurrence with no way to apply it broadly.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Set up a recurring task, generate several occurrences, and edit one occurrence's content or
  schedule.
```

## G12-PROJECT-Q005

```yaml
QID: G12-PROJECT-Q005
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Stopping a recurring task's pattern preserves the occurrences already generated; it does not
  retroactively remove completed or in-progress instances.
WHY_IT_MATTERS: >
  A recurrence stop is a forward-looking planning decision; treating it as retroactive destroys
  already-completed work records.
DISCONFIRMING_OBSERVATION: >
  Stopping the recurring pattern deletes or hides occurrences that were already generated and
  already completed or in progress.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate several occurrences of a recurring task, complete one, then stop the recurrence and
  inspect what remains.
```

## G12-PROJECT-Q006

```yaml
QID: G12-PROJECT-Q006
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A task held by a blocking-type dependency on an incomplete predecessor cannot be advanced to a
  completion state while that predecessor remains open.
WHY_IT_MATTERS: >
  A dependency that can simply be ignored provides no real sequencing guarantee, only the appearance
  of one.
DISCONFIRMING_OBSERVATION: >
  A task with an open blocking predecessor is moved to a completion state without any obstruction or
  warning.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure a blocking dependency between two tasks, leave the predecessor open, and attempt to
  complete the dependent task.
```

## G12-PROJECT-Q007

```yaml
QID: G12-PROJECT-Q007
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Completing all of a task's subtasks does not automatically force the parent task itself into a
  completed state without an explicit action on the parent.
WHY_IT_MATTERS: >
  Automatic completion by inference can close a parent task whose own remaining work was never
  captured as a subtask.
DISCONFIRMING_OBSERVATION: >
  A parent task's state changes to complete purely as a side effect of all subtasks being completed,
  with no explicit action taken on the parent itself.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a parent task with subtasks, complete every subtask, and check the parent's state without
  touching it directly.
```

## G12-PROJECT-Q008

```yaml
QID: G12-PROJECT-Q008
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A sub-project's time or effort totals roll up to its parent project in a defined, discoverable way,
  rather than the parent and sub-project being reported as entirely unrelated totals.
WHY_IT_MATTERS: >
  A hierarchy that does not aggregate defeats the purpose of establishing it in the first place.
DISCONFIRMING_OBSERVATION: >
  Work logged against a sub-project is not reflected in any parent-level total or view, or the
  relationship between the two totals is undocumented and inconsistent across views.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Establish a parent/sub-project relationship, log effort on the sub-project, and inspect
  parent-level reporting.
```

## G12-PROJECT-Q009

```yaml
QID: G12-PROJECT-Q009
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user scoped to one company cannot view or select tasks belonging to a project scoped to a
  different company in a multi-company environment.
WHY_IT_MATTERS: >
  Project and task content routinely includes commercially sensitive information whose exposure
  across company boundaries is a direct governance failure.
DISCONFIRMING_OBSERVATION: >
  A user restricted to one company can view, search, or select a task belonging to a project scoped
  to a different company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create projects under two distinct companies and attempt cross-company access as a single-company
  user.
```

## G12-PROJECT-Q010

```yaml
QID: G12-PROJECT-Q010
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A portal (external, non-employee) user can see only the tasks they are explicitly assigned to or
  following, not the full task list of the project they were given access to.
WHY_IT_MATTERS: >
  A portal scope that leaks the full internal task list exposes internal planning detail, staffing,
  and unrelated customer information to an external party.
DISCONFIRMING_OBSERVATION: >
  A portal user with access to a project can see tasks they are neither assigned to nor following.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  Grant a portal user access to a project containing tasks not assigned to or followed by them, and
  inspect what that user can see.
```

## G12-PROJECT-Q011

```yaml
QID: G12-PROJECT-Q011
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Creating a project from a template copies the stage structure and configuration only; it does not
  copy the instance data (specific tasks, assignees, or dates) of whatever project the template was
  originally derived from.
WHY_IT_MATTERS: >
  A template that leaks concrete instance data turns a reusable structure into a source of stale or
  confidential carryover.
DISCONFIRMING_OBSERVATION: >
  A project created from a template arrives already populated with specific task content, assignees,
  or dates that belong to a prior, unrelated project.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Save a populated project as a template, then create a new project from that template and inspect
  its initial content.
```

## G12-PROJECT-Q012

```yaml
QID: G12-PROJECT-Q012
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a task's assignee loses access to the project's company, the task is surfaced for
  reassignment rather than remaining silently assigned to a user who can no longer act on it.
WHY_IT_MATTERS: >
  A task assigned to someone who can no longer reach it is effectively invisible work that nobody is
  tracking as unowned.
DISCONFIRMING_OBSERVATION: >
  A task remains assigned to a user who has lost access to the relevant company, with nothing
  flagging it as needing reassignment.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Remove a task assignee's access to the project's company and inspect the task's state and any
  surfaced flag.
```

## G12-PROJECT-Q013

```yaml
QID: G12-PROJECT-Q013
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A milestone is only marked complete when its own defined completion criteria are met, not merely
  because its target date has passed or because some subset of related tasks happened to close.
WHY_IT_MATTERS: >
  A milestone that can complete itself on a technicality misrepresents actual progress to anyone
  relying on it, including a customer-facing portal view.
DISCONFIRMING_OBSERVATION: >
  A milestone shows as complete purely because its date has passed or because an unrelated task
  closed, while its actual defined deliverable remains unmet.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Set up a milestone with defined criteria, let its date pass without meeting the criteria, and
  check its displayed state.
```

## G12-PROJECT-Q014

```yaml
QID: G12-PROJECT-Q014
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing a milestone's target date has a defined, consistent effect on the deadlines of tasks
  linked to it — either it cascades explicitly or it deliberately does not — rather than an
  inconsistent, undocumented mix of both.
WHY_IT_MATTERS: >
  Inconsistent cascade behaviour means a planner cannot predict the effect of a single date change
  without checking every linked task individually.
DISCONFIRMING_OBSERVATION: >
  Changing the milestone date shifts some linked tasks' deadlines and leaves others unchanged with no
  documented rule explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Link several tasks to one milestone, change the milestone's date, and inspect each linked task's
  deadline afterward.
```

## G12-PROJECT-Q015

```yaml
QID: G12-PROJECT-Q015
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A task's priority indicator is computed and displayed identically across the kanban view, list
  view, and calendar view, rather than one view showing a different effective priority than another.
WHY_IT_MATTERS: >
  A priority signal that disagrees between views cannot be trusted for triage decisions made from
  whichever view happens to be open.
DISCONFIRMING_OBSERVATION: >
  The same task shows a different priority indicator, or none, depending on which view is used to
  inspect it.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Set a task's priority and inspect its representation across kanban, list, and calendar views.
```

## G12-PROJECT-Q016

```yaml
QID: G12-PROJECT-Q016
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Folding a kanban stage to hide its task cards changes only the display; it does not exclude that
  stage's tasks from counts, filters, or reports that a permission-scoped user would otherwise see.
WHY_IT_MATTERS: >
  A display convenience that silently drops data from underlying totals turns a visual choice into a
  reporting error.
DISCONFIRMING_OBSERVATION: >
  Folding a stage causes its tasks to disappear from a count, filter, or report that should still
  include them.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Fold a kanban stage containing tasks and compare task counts and filtered views before and after.
```

## G12-PROJECT-Q017

```yaml
QID: G12-PROJECT-Q017
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reordering or renaming a project's stages does not retroactively rewrite the historical record of
  which stage a task passed through and when.
WHY_IT_MATTERS: >
  Stage-duration and cycle-time analysis depends on the historical record being fixed at the time it
  occurred, independent of later configuration changes.
DISCONFIRMING_OBSERVATION: >
  After a stage is renamed or reordered, the historical trace of a task's past stage transitions
  reflects the new configuration rather than what actually happened at the time.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Move a task through several stages, then rename or reorder those stages, and inspect the task's
  historical stage trace.
```

## G12-PROJECT-Q018

```yaml
QID: G12-PROJECT-Q018
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Deleting a tag that is currently applied to tasks is either blocked with a warning naming the
  affected tasks, or silently removes the tag from those tasks — the actual behaviour is defined and
  consistent, not arbitrary.
WHY_IT_MATTERS: >
  Inconsistent tag-deletion behaviour makes any tag-based report unreliable, since a tag might vanish
  from history without a trace.
DISCONFIRMING_OBSERVATION: >
  Deleting an in-use tag produces different outcomes (block versus silent removal) on different
  occasions with no configuration explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply a tag to several tasks, then delete the tag and inspect the outcome, repeating to check
  consistency.
```

## G12-PROJECT-Q019

```yaml
QID: G12-PROJECT-Q019
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A completed task can still be reopened after the project itself has been archived, or is
  explicitly and consistently prevented from being reopened — not left in an undefined in-between
  state.
WHY_IT_MATTERS: >
  An undefined reopen behaviour on an archived project's task risks either silently reviving hidden
  work or blocking a legitimate correction with no explanation.
DISCONFIRMING_OBSERVATION: >
  Attempting to reopen a completed task under an archived project produces an unexplained error, or
  succeeds in one attempt and fails in an identical later attempt.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Archive a project containing a completed task, then attempt to reopen that task.
```

## G12-PROJECT-Q020

```yaml
QID: G12-PROJECT-Q020
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A task created automatically from an inbound message is not treated as trusted or verified simply
  because it arrived through the intake address; the sender's identity is not silently assumed
  authentic.
WHY_IT_MATTERS: >
  An intake channel that treats the visible sender address as verified identity is a spoofing vector
  for creating tasks, assigning followers, or triggering downstream automation.
DISCONFIRMING_OBSERVATION: >
  A task created from an inbound message assigns elevated trust — such as adding the apparent sender
  as an internal follower with expanded visibility — based only on the unverified sender address.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Send a message to the project's intake address from an address not associated with any known
  contact, and inspect the resulting task's fields and follower list.
```

## G12-PROJECT-Q021

```yaml
QID: G12-PROJECT-Q021
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The hours shown against a task as actually worked reflect the same underlying figure the linked
  time-tracking capability records, rather than a separately maintained number that can drift out of
  sync.
WHY_IT_MATTERS: >
  Two different numbers claiming to represent the same worked time destroys confidence in whichever
  one a manager happens to look at.
DISCONFIRMING_OBSERVATION: >
  The task's displayed worked-hours figure disagrees with the total shown by the linked
  time-tracking view for the same task.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Log time against a task through the time-tracking capability and compare the total shown on the
  task itself against the time-tracking total.
```

## G12-PROJECT-Q022

```yaml
QID: G12-PROJECT-Q022
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Assigning the same person to open tasks across multiple concurrent projects surfaces some
  indication of their combined workload, rather than each project reporting allocation in complete
  isolation from the others.
WHY_IT_MATTERS: >
  A resource shown as available in every project individually while being fully committed across all
  of them together leads directly to overcommitment.
DISCONFIRMING_OBSERVATION: >
  A person is shown as having capacity in each project's own view even though their combined
  assigned workload across projects clearly exceeds capacity, with nothing surfacing the conflict.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Assign one person to a heavy task load across two or more concurrent projects and look for any
  cross-project workload indicator.
```

## G12-PROJECT-Q023

```yaml
QID: G12-PROJECT-Q023
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Shifting a task's schedule in a timeline/gantt-style view propagates predictably to tasks that
  depend on it, following the dependency type actually configured, rather than moving dependents by
  an arbitrary or inconsistent amount.
WHY_IT_MATTERS: >
  Unpredictable cascading makes timeline planning actively misleading rather than merely
  unhelpful.
DISCONFIRMING_OBSERVATION: >
  Shifting one task's dates moves a dependent task by an amount inconsistent with the configured
  dependency type, or fails to move it when the dependency type requires it.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Configure a dependency between two tasks, shift the predecessor's schedule in the timeline view,
  and inspect the dependent task's resulting schedule.
```

## G12-PROJECT-Q024

```yaml
QID: G12-PROJECT-Q024
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A task's overdue indicator is computed identically regardless of which view — kanban badge, list
  column, or calendar marker — is used to display it.
WHY_IT_MATTERS: >
  A task that is flagged overdue in one view and not another undermines trust in whichever surface a
  manager happens to use for daily triage.
DISCONFIRMING_OBSERVATION: >
  The same task with the same deadline shows as overdue in one view and not overdue in another at the
  same point in time.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Set a task's deadline in the past and compare its overdue indicator across kanban, list, and
  calendar views.
```

## G12-PROJECT-Q025

```yaml
QID: G12-PROJECT-Q025
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing a project's manager does not silently reassign or alter ownership of tasks already
  assigned to specific individuals within that project.
WHY_IT_MATTERS: >
  A manager change is an administrative event that should not by itself disturb the working
  assignments already agreed for individual tasks.
DISCONFIRMING_OBSERVATION: >
  Changing the project's manager also changes the assignee recorded on existing tasks that were not
  touched directly.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Assign tasks to specific individuals, then change the project's manager, and inspect task
  assignments afterward.
```

## G12-PROJECT-Q026

```yaml
QID: G12-PROJECT-Q026
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing a task's assignee updates the set of people who receive its notifications so the new
  assignee is included and a no-longer-relevant previous assignee is not left receiving every
  update indefinitely.
WHY_IT_MATTERS: >
  Stale notification subscriptions either bury the new assignee's inbox in noise for someone no
  longer responsible, or leave the actual owner uninformed.
DISCONFIRMING_OBSERVATION: >
  After reassignment, the previous assignee keeps receiving every update as before, or the new
  assignee is not added to notifications at all.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reassign a task from one person to another and observe subsequent notification recipients on a
  further update.
```

## G12-PROJECT-Q027

```yaml
QID: G12-PROJECT-Q027
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A task marked private is hidden from the customer portal and from internal users who are neither
  assigned to it nor explicitly granted visibility, not merely hidden from the default list view.
WHY_IT_MATTERS: >
  A privacy control that only affects the default view while the record remains reachable through
  search, reports, or the portal is not actually a privacy control.
DISCONFIRMING_OBSERVATION: >
  A private task remains visible to an unrelated internal user or a portal user through search,
  direct link, or a report, despite not appearing in the default list.
EXPECTED_SURFACE: S1,S4,S5
PRECONDITIONS: >
  Mark a task private and attempt to reach it as an unrelated internal user and as a portal user
  through channels other than the default list.
```

## G12-PROJECT-Q028

```yaml
QID: G12-PROJECT-Q028
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Completing a recurring task's earliest generated occurrence does not cause future, not-yet-due
  occurrences to be generated ahead of their own schedule.
WHY_IT_MATTERS: >
  Occurrences generated ahead of schedule because an earlier one closed early misrepresent the
  actual planned cadence to anyone reviewing the schedule.
DISCONFIRMING_OBSERVATION: >
  Completing the earliest occurrence early causes a later occurrence, not yet due, to be generated
  ahead of its own scheduled date.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Complete the earliest generated occurrence of a recurring task well ahead of its due date and
  check whether later occurrences appear prematurely.
```

## G12-PROJECT-Q029

```yaml
QID: G12-PROJECT-Q029
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A project's colour or grouping tag used for visual organisation is applied consistently between
  the kanban board and any list or reporting view that also displays it.
WHY_IT_MATTERS: >
  Inconsistent visual grouping between views undermines the at-a-glance triage the colour coding is
  meant to support.
DISCONFIRMING_OBSERVATION: >
  The same project's colour or grouping tag differs between the kanban board and a list or reporting
  view.
EXPECTED_SURFACE: S5
PRECONDITIONS: >
  Set a project's colour or grouping tag and compare its representation across the kanban board and
  a list view.
```

## G12-PROJECT-Q030

```yaml
QID: G12-PROJECT-Q030
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Turning off customer-facing milestone visibility actually removes milestone information from what
  the portal user can see, rather than only removing it from one portal screen while leaving it
  reachable elsewhere in the portal.
WHY_IT_MATTERS: >
  A visibility toggle that is only partially honoured misleads whoever configured it into believing
  information is hidden that is not.
DISCONFIRMING_OBSERVATION: >
  With milestone visibility turned off, a portal user can still see milestone information through
  some other portal screen or export.
EXPECTED_SURFACE: S4,S5,S7
PRECONDITIONS: >
  Disable customer milestone visibility for a project and check every portal surface a customer can
  reach for that project.
```

## G12-PROJECT-Q031

```yaml
QID: G12-PROJECT-Q031
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Moving a task from one project to another preserves its linked records — attachments, logged time,
  and history — rather than silently detaching them or leaving them orphaned under the original
  project.
WHY_IT_MATTERS: >
  A task move that leaves its history behind produces a record that looks freshly created, hiding
  everything that happened before the move.
DISCONFIRMING_OBSERVATION: >
  After moving a task to a different project, its prior attachments, logged time, or history are
  missing or remain attached to the original project instead of following the task.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Attach a file, log time, and accumulate history on a task, then move it to a different project and
  inspect what followed.
```

## G12-PROJECT-Q032

```yaml
QID: G12-PROJECT-Q032
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting a task that has logged time entries against it is blocked, requires explicit override, or
  at minimum warns about the loss, rather than deleting the time record along with the task with no
  distinguishing safeguard.
WHY_IT_MATTERS: >
  Time entries often carry cost or billing significance; deleting them as a silent side effect of an
  unrelated task deletion destroys that record without anyone deciding to.
DISCONFIRMING_OBSERVATION: >
  A task with logged time entries is deleted through the same unqualified action used for a task with
  no logged time, with no distinguishing warning.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Log time against a task, then attempt to delete it and compare the experience against deleting a
  task with no logged time.
```

## G12-PROJECT-Q033

```yaml
QID: G12-PROJECT-Q033
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Deleting a stage that still contains tasks forces an explicit decision about what happens to those
  tasks — move them, or block the deletion — rather than deleting the tasks along with the stage as
  an unannounced side effect.
WHY_IT_MATTERS: >
  Tasks disappearing as an incidental consequence of a stage-configuration change is a serious,
  easily overlooked data-loss path.
DISCONFIRMING_OBSERVATION: >
  Deleting a stage that contains tasks removes those tasks along with it, with no prompt to move
  them elsewhere.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Populate a stage with tasks and attempt to delete that stage.
```

## G12-PROJECT-Q034

```yaml
QID: G12-PROJECT-Q034
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The set of values a task's closing state can take is a controlled, finite set rather than
  free-text, so reporting on why tasks were closed is actually reliable.
WHY_IT_MATTERS: >
  Free-text closing reasons cannot be reliably aggregated, undermining any report that groups tasks
  by why they ended.
DISCONFIRMING_OBSERVATION: >
  Two tasks closed for what is clearly the same underlying reason end up with differently worded,
  freely typed closing states that a report cannot group together.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Close several tasks for the same underlying reason and inspect whether the closing state field is
  a controlled selection or free text.
```

## G12-PROJECT-Q035

```yaml
QID: G12-PROJECT-Q035
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing the cost-tracking or analytic account linked to a project after tasks have already logged
  time against it does not retroactively reattribute that already-logged time to the newly linked
  account.
WHY_IT_MATTERS: >
  Retroactive reattribution of already-recognised cost would silently rewrite historical cost
  reporting after the fact.
DISCONFIRMING_OBSERVATION: >
  Changing the project's linked cost-tracking account causes previously logged time to be reported
  under the new account rather than the one in effect when it was logged.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Log time against a project under one cost-tracking link, change the link, and inspect how the
  earlier logged time is now reported.
```

## G12-PROJECT-Q036

```yaml
QID: G12-PROJECT-Q036
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Turning on a rating request for a project stage only affects future transitions into that stage;
  it does not retroactively generate rating requests for tasks that already passed through that
  stage before the setting was enabled.
WHY_IT_MATTERS: >
  Retroactive requests sent for events that already happened, sometimes long ago, confuse recipients
  and misrepresent the request as timely feedback.
DISCONFIRMING_OBSERVATION: >
  Enabling stage-based rating requests generates requests for tasks that transitioned through that
  stage before the setting was turned on.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Move tasks through a stage before rating requests are enabled for it, then enable the setting and
  check whether requests are generated for the earlier transitions.
```

## G12-PROJECT-Q037

```yaml
QID: G12-PROJECT-Q037
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Recurring task occurrences are counted once each in project-level totals and reports; the
  recurrence mechanism does not cause any occurrence to be double-counted or omitted.
WHY_IT_MATTERS: >
  A reporting error introduced specifically by the recurrence mechanism would silently distort every
  total that depends on task counts.
DISCONFIRMING_OBSERVATION: >
  A project-level total or report counts a recurring task's occurrences more than once, or omits
  one, compared to a manual count.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate several occurrences of a recurring task and compare a manual count against the project's
  own reported total.
```

## G12-PROJECT-Q038

```yaml
QID: G12-PROJECT-Q038
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a task has more than one assignee, completing the task attributes it in a way that still
  allows identifying which individual actually performed the completing action, rather than
  collapsing to an undifferentiated group credit.
WHY_IT_MATTERS: >
  Undifferentiated group credit on multi-assignee tasks makes individual accountability and
  performance review unreliable.
DISCONFIRMING_OBSERVATION: >
  A multi-assignee task's completion record shows no way to determine which of the assignees
  actually performed the completing action.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Assign a task to more than one person, have one of them complete it, and inspect what the
  completion record identifies.
```

## G12-PROJECT-Q039

```yaml
QID: G12-PROJECT-Q039
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Dragging several tasks together into a new kanban stage triggers that stage's configured
  automation once per task moved, not once for the whole batch and not skipped for tasks beyond the
  first.
WHY_IT_MATTERS: >
  A batch operation that only partially applies configured automation produces inconsistent
  downstream effects depending on how a move happened to be performed.
DISCONFIRMING_OBSERVATION: >
  Moving several tasks together into a stage with configured automation causes the automation to
  fire for only some of the moved tasks.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Configure stage automation, select multiple tasks, and move them together into that stage,
  checking that automation fired for every task moved.
```

## G12-PROJECT-Q040

```yaml
QID: G12-PROJECT-Q040
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A project shared through an unauthenticated or link-based sharing mechanism exposes only the
  specific scope intended for that share, not the full internal project content reachable by an
  authenticated internal user.
WHY_IT_MATTERS: >
  A share link is the easiest way for project content to escape entirely outside any access-control
  boundary; over-exposure here is not contained by any other control.
DISCONFIRMING_OBSERVATION: >
  Content accessed through an unauthenticated share link includes information beyond what was
  explicitly intended for external sharing, such as internal-only fields or unrelated tasks.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Where an unauthenticated or link-based sharing mechanism exists, generate a share for a limited
  scope and inspect exactly what is reachable through it.
```

## G12-PROJECT-Q041

```yaml
QID: G12-PROJECT-Q041
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The permission governing who can view or add an attachment on a task is consistent with the
  permission governing attachments at the project level, rather than one being effectively looser
  than the other.
WHY_IT_MATTERS: >
  A looser task-level attachment permission than the project's own policy is a bypass of whatever
  the project-level control was meant to enforce.
DISCONFIRMING_OBSERVATION: >
  A user blocked from adding or viewing an attachment at the project level is nonetheless able to do
  so on a specific task within that project.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Restrict attachment access at the project level and attempt the equivalent action on a task within
  that project.
```

## G12-PROJECT-Q042

```yaml
QID: G12-PROJECT-Q042
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Assigning a subtask to someone other than the parent task's assignee still keeps the parent
  assignee informed of the subtask's key status changes, rather than the parent assignee losing
  visibility once a subtask is delegated elsewhere.
WHY_IT_MATTERS: >
  A parent assignee who is accountable for overall delivery needs to know what is happening on
  delegated subtasks, not just the ones they personally hold.
DISCONFIRMING_OBSERVATION: >
  A subtask assigned to a different person completes or changes status with no visibility
  whatsoever reaching the parent task's assignee.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Assign a subtask to someone other than the parent's assignee, change the subtask's status, and
  check what the parent assignee is shown.
```

## G12-PROJECT-Q043

```yaml
QID: G12-PROJECT-Q043
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A project created from a template that defines task deadlines relative to the creation date does
  not produce tasks that are already overdue at the moment of creation.
WHY_IT_MATTERS: >
  A template producing instantly-overdue tasks trains users to ignore the overdue signal entirely,
  destroying its usefulness project-wide.
DISCONFIRMING_OBSERVATION: >
  A newly created project from a relative-date template contains tasks already flagged overdue
  before any work has had a chance to begin.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Build a template with short relative deadlines, create a project from it, and check task states
  immediately after creation.
```

## G12-PROJECT-Q044

```yaml
QID: G12-PROJECT-Q044
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where planned effort is compared against actual effort on a task, an overrun is flagged
  consistently whenever the threshold is crossed, not suppressed depending on which view or report
  the comparison happens to be shown in.
WHY_IT_MATTERS: >
  A flag that only appears in some views gives a false sense of control to anyone relying on a
  different view for the same information.
DISCONFIRMING_OBSERVATION: >
  A task that has genuinely exceeded its planned effort shows the overrun flag in one view but not in
  another that also displays planned-versus-actual figures.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Exceed a task's planned effort and compare the overrun indicator across every view that shows
  planned-versus-actual figures.
```

## G12-PROJECT-Q045

```yaml
QID: G12-PROJECT-Q045
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Duplicating a single task has a defined, discoverable scope for what is copied — description and
  configuration versus logged time, dependencies, and attachments — rather than an undocumented,
  inconsistent mix.
WHY_IT_MATTERS: >
  An undocumented duplication scope leads to duplicated time or dependency records nobody intended
  to copy, or missing detail nobody noticed was left behind.
DISCONFIRMING_OBSERVATION: >
  Duplicating the same task twice under identical conditions produces two copies with different sets
  of copied elements.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Duplicate a task that has logged time, dependencies, and attachments, and inspect exactly what
  appears on the copy.
```

## G12-PROJECT-Q046

```yaml
QID: G12-PROJECT-Q046
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A task explicitly cancelled remains distinguishable in reporting from a task that was genuinely
  completed; the two are not merged into a single closed count.
WHY_IT_MATTERS: >
  Merging cancelled work into completed-work totals overstates actual delivery and hides scope that
  was dropped rather than delivered.
DISCONFIRMING_OBSERVATION: >
  A report or count of completed tasks includes tasks that were actually cancelled, with no way to
  separate the two.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel one task and complete another under otherwise identical conditions, then inspect a report
  that totals closed or completed work.
```

## G12-PROJECT-Q047

```yaml
QID: G12-PROJECT-Q047
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A task cannot be assigned to a user who does not have access to the company that the task's project
  belongs to; the assignment is prevented rather than silently accepted.
WHY_IT_MATTERS: >
  An assignment that silently succeeds despite a company-access mismatch creates a task no
  authorized party in that company knows is theirs to act on.
DISCONFIRMING_OBSERVATION: >
  A task under one company's project is successfully assigned to a user with no access to that
  company, with no error or warning.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to assign a task to a user who lacks access to the task's company.
```

## G12-PROJECT-Q048

```yaml
QID: G12-PROJECT-Q048
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two users editing the same task's content at nearly the same time do not result in one user's
  change being silently discarded with no conflict indication to either party.
WHY_IT_MATTERS: >
  A silently discarded edit on shared work erodes trust in the tool and can lose real, unrecoverable
  input.
DISCONFIRMING_OBSERVATION: >
  Two concurrent edits to the same task field result in one change disappearing with neither user
  shown any conflict or warning.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Open the same task in two sessions and submit conflicting edits to the same field at nearly the
  same time.
```

## G12-PROJECT-Q049

```yaml
QID: G12-PROJECT-Q049
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A task that shows a now-deactivated employee or user as its historical assignee continues to
  display that historical attribution accurately, rather than the deactivation erasing or obscuring
  who actually did the work.
WHY_IT_MATTERS: >
  Historical accountability should not depend on whether the person involved is still an active
  user.
DISCONFIRMING_OBSERVATION: >
  Deactivating a user causes their historical task assignments to display incorrectly, blank, or
  reassigned rather than accurately attributed to them.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a task under a given assignee, deactivate that user, and inspect the task's historical
  attribution afterward.
```

## G12-PROJECT-Q050

```yaml
QID: G12-PROJECT-Q050
MODULE: project
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Changing which stage new tasks default into for a project does not retroactively move tasks that
  already exist in a different stage.
WHY_IT_MATTERS: >
  A default-stage configuration change is meant to affect future task creation only; retroactive
  movement would silently disturb work already in progress.
DISCONFIRMING_OBSERVATION: >
  Changing the default stage setting causes existing tasks in other stages to move into the new
  default stage.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Populate several stages with tasks, then change the project's default-stage configuration and
  inspect existing task placement afterward.
```
