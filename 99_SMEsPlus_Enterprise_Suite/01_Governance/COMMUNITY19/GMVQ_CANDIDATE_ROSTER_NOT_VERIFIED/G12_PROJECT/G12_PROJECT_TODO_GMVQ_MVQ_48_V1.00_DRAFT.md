# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_todo Module MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_TODO-MVQ48-V1.00
**Group:** G12 PROJECT
**Module Metadata:** `project_todo`
**Wave:** W3 (GMVQ 25-Team Acceleration, 2026-09-27)
**Author Cell:** P12-5 (GMVQ Question Factory — Production Cell P12-5)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `project_todo`, a foundation-layer capability
(per GROUP_BRIEF_G12_PROJECT.md, listed among the low/no-bridge-arity modules expected to reach
the full 48-question floor easily). The subject matter is the informal personal/team task item —
distinct from a formal project task — and every business behaviour around its lifecycle: creation,
assignment, linkage to a project or project task, completion, recurrence, reminders, conversion,
deletion and reporting. This is not a bridge module and the seam-only removal test does not apply;
questions instead spread across the full dimension list in GMVQ_AUTHORING_STANDARD_V1.00 §5.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: these 48 questions test 48 distinct material hypotheses spread across business
  capability, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, cross-module dependency (to a linked project or task),
  optional behaviour, auditability, and concurrency/ordering.
- Question text is source-neutral: no vendor or product name, no technical identifier, and the
  module's own metadata name never appears outside the `MODULE:` field.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## G12-PROJECT_TODO-Q001

```yaml
QID: G12-PROJECT_TODO-Q001
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Marking a personal task item as done does not, by itself, silently mark a separately tracked
  project task complete unless an explicit link between the two is defined and that link is
  documented to cascade completion.
WHY_IT_MATTERS: >
  An undocumented cascade would let someone unintentionally close formal project work by finishing
  an informal personal reminder.
DISCONFIRMING_OBSERVATION: >
  Completing the personal task item marks a linked project task complete with no documented rule
  stating that this link cascades completion.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Link a personal task item to a project task, mark only the personal item done, and check whether
  the linked project task's own status changes.
```

## G12-PROJECT_TODO-Q002

```yaml
QID: G12-PROJECT_TODO-Q002
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Converting a personal task item into a full project task carries its description, due date and
  assignee across without loss or silent substitution of any of the three.
WHY_IT_MATTERS: >
  Silent loss of detail during conversion would leave the resulting project task incomplete or
  misassigned without anyone noticing at the moment of conversion.
DISCONFIRMING_OBSERVATION: >
  The resulting project task is missing, or shows a different value for, the description, due date
  or assignee that the original personal task item carried.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a personal task item with a description, due date and assignee, convert it into a project
  task, and compare all three values before and after.
```

## G12-PROJECT_TODO-Q003

```yaml
QID: G12-PROJECT_TODO-Q003
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting a project task that has a linked personal task item follows one documented rule for
  what happens to that linked item, rather than an unpredictable outcome that differs by how the
  deletion was triggered.
WHY_IT_MATTERS: >
  An unpredictable outcome would leave some personal items silently orphaned and others silently
  removed with no way to know which will happen in advance.
DISCONFIRMING_OBSERVATION: >
  Deleting the linked project task sometimes removes the personal item and sometimes leaves it
  dangling, with no documented rule explaining the difference.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Link a personal task item to a project task, delete the project task through more than one
  available path, and compare the resulting state of the personal item each time.
```

## G12-PROJECT_TODO-Q004

```yaml
QID: G12-PROJECT_TODO-Q004
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A personal task item can exist and be tracked without belonging to any project at all.
WHY_IT_MATTERS: >
  If every item were forced into a project, the capability would lose its value as a lightweight
  personal reminder tool independent of formal project structure.
DISCONFIRMING_OBSERVATION: >
  Creating a personal task item without selecting a project either fails or the item is silently
  attached to a default project the user did not choose.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to create a personal task item with no project selected and check whether it is created
  and remains unlinked.
```

## G12-PROJECT_TODO-Q005

```yaml
QID: G12-PROJECT_TODO-Q005
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reassigning a personal task item to a different user transfers full visibility of the item to
  that user rather than leaving a dangling reference the new assignee cannot actually see.
WHY_IT_MATTERS: >
  A reassignment the new owner cannot see would leave the work invisible to the person now
  responsible for it.
DISCONFIRMING_OBSERVATION: >
  After reassignment, the new assignee cannot locate the item in their own task list.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Reassign a personal task item to a second user and check whether that user can see it in their
  own list of items.
```

## G12-PROJECT_TODO-Q006

```yaml
QID: G12-PROJECT_TODO-Q006
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A recurring personal task item generates its next occurrence in the correct pattern once the
  current occurrence is completed, without generating duplicate occurrences or skipping one.
WHY_IT_MATTERS: >
  Duplicated or skipped occurrences would make a recurring reminder unreliable for anything time
  sensitive.
DISCONFIRMING_OBSERVATION: >
  Completing one occurrence of a recurring item produces zero or more than one next occurrence,
  or produces one at the wrong interval.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Set up a recurring personal task item, complete the current occurrence, and check the count and
  timing of the next occurrence generated.
```

## G12-PROJECT_TODO-Q007

```yaml
QID: G12-PROJECT_TODO-Q007
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A personal task item whose due date passes without completion is visibly flagged as overdue
  rather than remaining indistinguishable from an item that is not yet due.
WHY_IT_MATTERS: >
  An invisible overdue state would let missed work go unnoticed indefinitely.
DISCONFIRMING_OBSERVATION: >
  An item past its due date and not completed shows no distinguishable overdue indicator anywhere
  in the user's list.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create an item with a due date in the past that is not completed, and check whether it is shown
  differently from an item not yet due.
```

## G12-PROJECT_TODO-Q008

```yaml
QID: G12-PROJECT_TODO-Q008
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A personal task item linked to a project that is later archived reflects the project's archived
  state rather than continuing to appear as a fully active, actionable item.
WHY_IT_MATTERS: >
  Continuing to surface an item from an archived project as active work would mislead a user into
  acting on a project that is no longer live.
DISCONFIRMING_OBSERVATION: >
  The linked item still appears as an ordinary active item with no indication that its project has
  been archived.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Link a personal task item to a project, archive the project, and check how the item is displayed
  afterward.
```

## G12-PROJECT_TODO-Q009

```yaml
QID: G12-PROJECT_TODO-Q009
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Whether two users can be assigned joint responsibility for one personal task item, and if so
  what completing it by one of them means for the other, is a single documented rule rather than
  an undefined edge case.
WHY_IT_MATTERS: >
  An undefined edge case would leave one of the two assignees uncertain whether the work is
  actually finished.
DISCONFIRMING_OBSERVATION: >
  Assigning the item to a second user produces a result with no documented, consistent answer for
  what a completion by either party means for the other.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to assign one personal task item to more than one user and check what the interface
  allows and what one assignee completing it does to the other's view.
```

## G12-PROJECT_TODO-Q010

```yaml
QID: G12-PROJECT_TODO-Q010
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A personal task item created from a reminder on another business record carries a retrievable
  reference back to that originating record.
WHY_IT_MATTERS: >
  Losing the originating reference would strand the reminder as context-free text with no way back
  to what it was actually about.
DISCONFIRMING_OBSERVATION: >
  The item created from the reminder shows no way to navigate back to the record that generated it.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Generate a personal task item from a reminder set on another business record and check whether a
  reference back to that record is retrievable from the item.
```

## G12-PROJECT_TODO-Q011

```yaml
QID: G12-PROJECT_TODO-Q011
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Manually reordering personal task items within a list changes only their display order and does
  not silently change their due date or priority value.
WHY_IT_MATTERS: >
  A reorder that silently changed due dates would corrupt scheduling information through what looks
  like a purely cosmetic action.
DISCONFIRMING_OBSERVATION: >
  Dragging an item to a new position in the list changes its stored due date or priority value.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Record the due date and priority of an item, reorder it within its list, and compare both values
  afterward.
```

## G12-PROJECT_TODO-Q012

```yaml
QID: G12-PROJECT_TODO-Q012
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing a personal task item's priority level consistently changes its position in a
  priority-sorted list view.
WHY_IT_MATTERS: >
  An inconsistent sort would make priority meaningless as a way to decide what to work on first.
DISCONFIRMING_OBSERVATION: >
  Raising an item's priority does not move it ahead of lower-priority items in a view sorted by
  priority.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Change an item's priority level while viewing a list sorted by priority and check whether its
  position updates accordingly.
```

## G12-PROJECT_TODO-Q013

```yaml
QID: G12-PROJECT_TODO-Q013
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Completing a personal task item records a timestamp for that completion that remains retrievable
  afterward for audit purposes.
WHY_IT_MATTERS: >
  A missing completion timestamp would make it impossible to later establish when work was actually
  finished.
DISCONFIRMING_OBSERVATION: >
  No completion timestamp can be retrieved for an item after it has been marked done.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Mark an item complete and then check whether a completion timestamp is stored and retrievable.
```

## G12-PROJECT_TODO-Q014

```yaml
QID: G12-PROJECT_TODO-Q014
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A personal task item assigned to a user who is later deactivated follows one documented rule for
  ownership going forward, rather than becoming invisible to everyone with no owner at all.
WHY_IT_MATTERS: >
  Work silently losing its owner would let it disappear from anyone's responsibility with nobody
  aware it needs picking up.
DISCONFIRMING_OBSERVATION: >
  After the assignee is deactivated, the item is not visible in anyone's active list and no
  documented reassignment or escalation has occurred.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Assign an incomplete item to a user, deactivate that user, and check who, if anyone, can now see
  and act on the item.
```

## G12-PROJECT_TODO-Q015

```yaml
QID: G12-PROJECT_TODO-Q015
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Marking several personal task items done in a single bulk action updates each one independently,
  so that a failure on one item does not silently prevent the others from being marked done.
WHY_IT_MATTERS: >
  A single point of failure across a bulk action would leave a user believing everything was
  completed when part of it silently was not.
DISCONFIRMING_OBSERVATION: >
  A bulk completion action that fails partway leaves some selected items still showing as
  incomplete with no indication which ones failed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Select several items, mark them done in one bulk action, and check whether the completion state
  of each item, and any failure, is individually reported.
```

## G12-PROJECT_TODO-Q016

```yaml
QID: G12-PROJECT_TODO-Q016
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a linked personal task item's due date automatically follows a change to its linked
  project task's own due date is a single documented rule, not a behaviour that differs
  unpredictably between items.
WHY_IT_MATTERS: >
  Inconsistent propagation would leave some personal reminders correctly rescheduled and others
  silently stale after the same kind of change.
DISCONFIRMING_OBSERVATION: >
  Changing the linked project task's due date updates some linked personal items' due dates and
  not others, with no configuration difference explaining why.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Link two personal items to two project tasks configured identically, change both project tasks'
  due dates, and compare whether both linked items' due dates update the same way.
```

## G12-PROJECT_TODO-Q017

```yaml
QID: G12-PROJECT_TODO-Q017
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Filtering a list of personal task items by a specific project shows only items actually linked to
  that project, excluding unrelated unlinked items.
WHY_IT_MATTERS: >
  A filter that leaks unrelated items would make project-scoped review unreliable.
DISCONFIRMING_OBSERVATION: >
  Filtering by a specific project includes at least one item that has no link to that project.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create items linked to different projects plus one unlinked item, filter the list by one project,
  and check exactly which items appear.
```

## G12-PROJECT_TODO-Q018

```yaml
QID: G12-PROJECT_TODO-Q018
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A reminder configured on a personal task item for a specific time triggers at that time, not
  materially earlier or later.
WHY_IT_MATTERS: >
  A mistimed reminder undermines the entire purpose of setting one.
DISCONFIRMING_OBSERVATION: >
  The reminder notification arrives at a time materially different from the time configured on the
  item.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Set a reminder for a specific time on an item and record the actual time the notification is
  delivered.
```

## G12-PROJECT_TODO-Q019

```yaml
QID: G12-PROJECT_TODO-Q019
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reopening a previously completed personal task item restores the same item to the active list
  rather than creating a second, duplicate entry alongside the original.
WHY_IT_MATTERS: >
  A duplicate created by reopening would corrupt lists and completion counts with a phantom item.
DISCONFIRMING_OBSERVATION: >
  Reopening a completed item results in two entries appearing in the active list instead of one.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Complete an item, reopen it, and check how many entries for that item now appear in the active
  list.
```

## G12-PROJECT_TODO-Q020

```yaml
QID: G12-PROJECT_TODO-Q020
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A user who created a personal task item and then assigned it to someone else retains visibility
  into that item's later completion status.
WHY_IT_MATTERS: >
  Losing visibility after handing work off would prevent the original requester from ever knowing
  whether it was finished.
DISCONFIRMING_OBSERVATION: >
  After assigning the item to another user, the creator can no longer see the item or its
  completion status at all.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create an item, assign it to a second user, have that user complete it, and check whether the
  original creator can still see the completed status.
```

## G12-PROJECT_TODO-Q021

```yaml
QID: G12-PROJECT_TODO-Q021
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Converting a personal task item into a project task requires an explicit project selection and
  leaves no duplicate free-floating personal item behind once the conversion completes.
WHY_IT_MATTERS: >
  A leftover duplicate would let the same piece of work be tracked, and potentially completed,
  twice under two different identities.
DISCONFIRMING_OBSERVATION: >
  After conversion, the original personal item still exists separately alongside the newly created
  project task.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Convert a personal task item into a project task and check whether the original item still exists
  as a separate, independent entry afterward.
```

## G12-PROJECT_TODO-Q022

```yaml
QID: G12-PROJECT_TODO-Q022
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Attachments or formatted description content entered on a personal task item survive conversion
  into a project task rather than being silently dropped.
WHY_IT_MATTERS: >
  Silently dropped context would leave the resulting project task less informative than the item it
  came from.
DISCONFIRMING_OBSERVATION: >
  An attachment or formatted content present on the original item is missing from the resulting
  project task after conversion.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Add an attachment or formatted text to a personal task item's description, convert it into a
  project task, and check whether the content is preserved.
```

## G12-PROJECT_TODO-Q023

```yaml
QID: G12-PROJECT_TODO-Q023
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Deleting a personal task item that was already marked complete follows one documented rule for
  whether a completion record survives for later reference or the item is removed entirely.
WHY_IT_MATTERS: >
  An undocumented, inconsistent outcome would leave some completed work provable later and other
  completed work with no trace at all.
DISCONFIRMING_OBSERVATION: >
  Deleting two separately completed items produces different retained-record outcomes with no
  configuration difference explaining why.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete and then delete two similarly configured items, and compare whether any record of either
  completion remains retrievable afterward.
```

## G12-PROJECT_TODO-Q024

```yaml
QID: G12-PROJECT_TODO-Q024
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A personal task item created with a due date already in the past is accepted and immediately
  treated as overdue, the same as one that becomes overdue naturally over time.
WHY_IT_MATTERS: >
  Different treatment for a backdated item would make the overdue flag an unreliable signal.
DISCONFIRMING_OBSERVATION: >
  An item created with a past due date does not show the overdue indicator that an item which
  became overdue naturally would show.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create an item with a due date already in the past and compare its overdue indicator against an
  item that has aged past its due date naturally.
```

## G12-PROJECT_TODO-Q025

```yaml
QID: G12-PROJECT_TODO-Q025
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether completing a project task automatically completes every personal task item linked to it
  is a single documented rule applied consistently, not a behaviour that varies by item.
WHY_IT_MATTERS: >
  Inconsistent cascade would leave some linked reminders correctly closed and others stranded open
  after the same underlying event.
DISCONFIRMING_OBSERVATION: >
  Completing the project task closes some of its linked personal items automatically and leaves
  others open, with no configuration difference explaining the split.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Link two personal items identically to one project task, complete the project task, and compare
  whether both linked items change status the same way.
```

## G12-PROJECT_TODO-Q026

```yaml
QID: G12-PROJECT_TODO-Q026
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Assigning a personal task item to a project team member who holds only read-only access to that
  project resolves through one documented rule, rather than silently granting that member an
  ability their project role does not otherwise carry.
WHY_IT_MATTERS: >
  A silent permission escalation through assignment would bypass the project's own access controls.
DISCONFIRMING_OBSERVATION: >
  A read-only project member, once assigned a linked personal item, gains the ability to act on the
  project in ways their role would not otherwise permit.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Assign a personal task item linked to a project to a member with read-only project access and
  check whether that assignment changes what they can otherwise do in the project.
```

## G12-PROJECT_TODO-Q027

```yaml
QID: G12-PROJECT_TODO-Q027
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Exporting or printing a user's list of personal task items groups items by their linked project
  rather than presenting one flat, undifferentiated list.
WHY_IT_MATTERS: >
  An undifferentiated export would make it hard to see which items belong to which piece of work
  when reviewed outside the system.
DISCONFIRMING_OBSERVATION: >
  The exported list shows no grouping or indication of which project, if any, each item is linked
  to.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create items linked to two different projects plus one unlinked item, export the full list, and
  check how project linkage is represented in the export.
```

## G12-PROJECT_TODO-Q028

```yaml
QID: G12-PROJECT_TODO-Q028
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting a project entirely, rather than archiving it, follows one documented rule for what
  happens to personal task items that were linked to it, rather than leaving them referencing a
  project that no longer exists.
WHY_IT_MATTERS: >
  A dangling reference to a deleted project could break the item's display or silently hide it with
  no explanation to the user.
DISCONFIRMING_OBSERVATION: >
  After the linked project is deleted, the personal item still displays a reference to it that leads
  nowhere, or the item disappears with no record of why.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Link a personal item to a project, delete that project entirely where permitted, and check the
  resulting state of the linked item.
```

## G12-PROJECT_TODO-Q029

```yaml
QID: G12-PROJECT_TODO-Q029
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A personal task item marked private stays invisible to a project team member who otherwise has
  full access to that project, even though the item is linked to it.
WHY_IT_MATTERS: >
  A private marking that fails to hide the item would break an explicit visibility promise made to
  the user who set it.
DISCONFIRMING_OBSERVATION: >
  A project team member with full project access can see an item marked private that another member
  created and linked to the same project.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create a personal item linked to a project, mark it private, and check whether another full-access
  project member can see it.
```

## G12-PROJECT_TODO-Q030

```yaml
QID: G12-PROJECT_TODO-Q030
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An item created through a quick-entry shortcut is structurally identical, once saved, to one
  created through the standard entry form, so both display and behave identically afterward.
WHY_IT_MATTERS: >
  A structural mismatch between the two entry paths would make some items behave unpredictably
  depending purely on how they were created.
DISCONFIRMING_OBSERVATION: >
  An item created through the quick-entry shortcut is missing a capability, such as linking or
  reminders, that an item created through the standard form has.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create one item through a quick-entry path and one through the standard form with equivalent
  content, and compare their available capabilities afterward.
```

## G12-PROJECT_TODO-Q031

```yaml
QID: G12-PROJECT_TODO-Q031
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a personal task item's completion is a simple binary state or supports partial progress
  is one documented, consistent rule, and if partial progress exists, it is mapped predictably when
  the item is converted into a project task's own progress concept.
WHY_IT_MATTERS: >
  An inconsistent or undefined mapping would lose or misstate progress information at the moment of
  conversion.
DISCONFIRMING_OBSERVATION: >
  An item with partial progress recorded converts into a project task showing a progress value that
  does not correspond to the original partial value, with no documented mapping rule.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set a partial-progress state on an item if supported, convert it into a project task, and compare
  the progress value before and after.
```

## G12-PROJECT_TODO-Q032

```yaml
QID: G12-PROJECT_TODO-Q032
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A personal task item's due date is permitted to extend beyond its linked project's own deadline
  without silently truncating the item's due date to fit inside the project.
WHY_IT_MATTERS: >
  Silent truncation would misrepresent when the user actually intends to act, without their
  knowledge.
DISCONFIRMING_OBSERVATION: >
  An item's due date, set beyond the linked project's deadline, is silently changed to fall inside
  the project's timeline.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Link an item to a project and set its due date beyond the project's own deadline, then check
  whether the due date is preserved as entered.
```

## G12-PROJECT_TODO-Q033

```yaml
QID: G12-PROJECT_TODO-Q033
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two users edit the same shared personal task item's due date at the same time, the later
  save does not silently overwrite the earlier one with no indication that a conflicting edit
  occurred.
WHY_IT_MATTERS: >
  A silent overwrite would let one user's scheduling change vanish without either party knowing a
  conflict happened.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous edits to the same item's due date result in one silently disappearing with
  no conflict indication to either editor.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have two sessions edit the same shared item's due date within a short window of each other and
  check whether a conflict is surfaced or one edit is silently lost.
```

## G12-PROJECT_TODO-Q034

```yaml
QID: G12-PROJECT_TODO-Q034
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A personal task item's change history, including who changed what and when, remains retrievable
  after the item is marked done rather than being cleared at completion.
WHY_IT_MATTERS: >
  A history cleared at completion would remove exactly the record most likely to be needed for a
  later audit or dispute about what happened.
DISCONFIRMING_OBSERVATION: >
  No change history is retrievable for an item once it has been marked complete, even though history
  existed before completion.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Make several changes to an item, mark it complete, and then check whether its earlier change
  history is still retrievable.
```

## G12-PROJECT_TODO-Q035

```yaml
QID: G12-PROJECT_TODO-Q035
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Editing one occurrence's due date within a recurring series changes only that single occurrence,
  and does not silently shift every future occurrence of the series unless that whole-series option
  is explicitly chosen.
WHY_IT_MATTERS: >
  A single-occurrence edit that silently reshapes the entire series would surprise a user who only
  intended to fix one date.
DISCONFIRMING_OBSERVATION: >
  Editing one occurrence's due date changes the due dates of other, unrelated future occurrences in
  the series without the whole-series option having been chosen.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a recurring item, edit the due date of a single occurrence without choosing a whole-series
  option, and check whether other occurrences are affected.
```

## G12-PROJECT_TODO-Q036

```yaml
QID: G12-PROJECT_TODO-Q036
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a linked personal task item's own assignee automatically follows a reassignment of its
  linked project task is one documented rule, applied the same way every time rather than varying
  by item.
WHY_IT_MATTERS: >
  Inconsistent propagation of reassignment would leave some personal reminders correctly following
  the new owner and others silently pointing at the person who no longer owns the work.
DISCONFIRMING_OBSERVATION: >
  Reassigning the linked project task changes some linked personal items' assignees and leaves
  others unchanged, with no configuration difference explaining the split.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Link two personal items identically to one project task, reassign the project task, and compare
  whether both linked items' assignees update the same way.
```

## G12-PROJECT_TODO-Q037

```yaml
QID: G12-PROJECT_TODO-Q037
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A personal task item created with no due date at all is still included correctly in default list
  and report views rather than being silently excluded or causing a display error.
WHY_IT_MATTERS: >
  Silent exclusion of due-date-less items would let real work disappear from view entirely.
DISCONFIRMING_OBSERVATION: >
  An item with no due date does not appear in the default list view where a comparable item with a
  due date does appear.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create one item with a due date and one without, and compare whether both appear in the default
  list view.
```

## G12-PROJECT_TODO-Q038

```yaml
QID: G12-PROJECT_TODO-Q038
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Repeatedly editing a reminder's due time before it fires does not result in more than one
  notification actually being delivered for that single reminder.
WHY_IT_MATTERS: >
  Duplicate notifications from repeated edits would train users to ignore reminders altogether.
DISCONFIRMING_OBSERVATION: >
  Editing a reminder's time several times before it fires results in more than one notification
  being delivered for the same reminder.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Set a reminder, edit its scheduled time more than once before it fires, and count how many
  notifications are actually delivered.
```

## G12-PROJECT_TODO-Q039

```yaml
QID: G12-PROJECT_TODO-Q039
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A user removed from a project's team roster has their previously assigned, still-open personal
  task items linked to that project handled by one documented rule, rather than left silently
  assigned to someone who no longer has any access to the project.
WHY_IT_MATTERS: >
  Work stranded on someone who no longer has project access would never actually get done and
  nobody would be alerted to pick it up.
DISCONFIRMING_OBSERVATION: >
  After removal from the project, the former member still shows as the assignee of an open,
  project-linked item, with no reassignment, flag, or documented handling.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Remove a user from a project's team while they hold an open, project-linked personal item, and
  check how that item's assignment is handled afterward.
```

## G12-PROJECT_TODO-Q040

```yaml
QID: G12-PROJECT_TODO-Q040
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a personal task item's link to a project, once set at creation, can later be changed to
  point at a different project is one documented, consistent rule applied the same way in every
  place the item can be edited.
WHY_IT_MATTERS: >
  An inconsistent rule between creation and later editing would confuse users about whether
  re-linking is actually possible.
DISCONFIRMING_OBSERVATION: >
  Whether the project link can be changed after creation differs depending on which screen or path
  is used to edit the same item.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attempt to change a project-linked item's project through more than one available editing path
  and compare whether both permit the same change.
```

## G12-PROJECT_TODO-Q041

```yaml
QID: G12-PROJECT_TODO-Q041
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two separately created personal task items that both reference the same project task remain
  independent, so completing one does not silently mark the other complete unless an explicit
  dependency between the two items themselves is defined.
WHY_IT_MATTERS: >
  Unintended cross-completion between unrelated items would make individual tracking unreliable.
DISCONFIRMING_OBSERVATION: >
  Completing one of the two independently created items automatically marks the other complete with
  no dependency explicitly defined between them.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create two separate items both referencing the same project task with no dependency defined
  between them, complete one, and check the other's status.
```

## G12-PROJECT_TODO-Q042

```yaml
QID: G12-PROJECT_TODO-Q042
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a personal task item's priority, once inherited from its linked project task at creation,
  continues to follow later changes to that project task's own priority is one documented,
  consistently applied rule.
WHY_IT_MATTERS: >
  An undocumented, inconsistent answer would leave some reminders correctly reflecting the current
  priority and others silently stale.
DISCONFIRMING_OBSERVATION: >
  Changing the linked project task's priority updates some linked items' inherited priority and
  leaves others unchanged, with no documented rule explaining the split.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Link two items identically to a project task at the same priority, change the project task's
  priority, and compare whether both linked items update the same way.
```

## G12-PROJECT_TODO-Q043

```yaml
QID: G12-PROJECT_TODO-Q043
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Marking several overdue personal task items done in one bulk action records each item's own
  individual completion timestamp rather than a single shared timestamp applied to all of them.
WHY_IT_MATTERS: >
  A shared timestamp would misstate exactly when each individual item was actually finished.
DISCONFIRMING_OBSERVATION: >
  After a bulk completion action, every affected item shows the identical completion timestamp down
  to the same value, rather than each item's own moment of completion.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Bulk-complete several overdue items at slightly different moments within the same action and
  compare their recorded completion timestamps.
```

## G12-PROJECT_TODO-Q044

```yaml
QID: G12-PROJECT_TODO-Q044
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A personal task item created with no project link at all can later be linked retroactively to a
  project while preserving its original creation date and any completion history it already has.
WHY_IT_MATTERS: >
  Losing the original history during a later link would misrepresent when the item was actually
  created or finished.
DISCONFIRMING_OBSERVATION: >
  Linking an existing item to a project after the fact changes its recorded creation date or clears
  its prior completion history.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an unlinked item, complete it or record history on it, then link it to a project
  retroactively, and check whether creation date and history are preserved.
```

## G12-PROJECT_TODO-Q045

```yaml
QID: G12-PROJECT_TODO-Q045
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A project's activity feed shows the creation and the completion of a linked personal task item as
  two distinguishable events, rather than merging them into one generic, undated entry.
WHY_IT_MATTERS: >
  A merged entry would make it impossible to tell from the feed alone when work actually started
  versus when it actually finished.
DISCONFIRMING_OBSERVATION: >
  The activity feed shows only one combined entry for a linked item that covers both its creation
  and its later completion.
EXPECTED_SURFACE: S5,S6
PRECONDITIONS: >
  Create a project-linked item, complete it later, and check whether the project's activity feed
  shows the creation and completion as two separate events.
```

## G12-PROJECT_TODO-Q046

```yaml
QID: G12-PROJECT_TODO-Q046
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A due date and reminder time set by one user for another user in a different time zone are
  interpreted so that both users see the same intended moment, rather than one seeing a time
  shifted by the difference between the two zones.
WHY_IT_MATTERS: >
  A silent time-zone shift would cause the assignee to see a due date or reminder that does not
  match what the assignor actually intended.
DISCONFIRMING_OBSERVATION: >
  The assignor and the assignee, in different time zones, see different clock times displayed for
  what is supposed to be the same due date or reminder moment, with no adjustment explaining the
  difference.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Have a user in one time zone set a due date and reminder for a user in another time zone, and
  compare how the moment is displayed to each.
```

## G12-PROJECT_TODO-Q047

```yaml
QID: G12-PROJECT_TODO-Q047
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Creating a personal task item with the same title and due date as an existing incomplete item
  produces one documented, consistent outcome, whether that is a warning or simply allowing the
  duplicate, rather than an inconsistent response that differs case by case.
WHY_IT_MATTERS: >
  An inconsistent response to likely duplicates would leave users unable to predict whether their
  action will be flagged or silently accepted.
DISCONFIRMING_OBSERVATION: >
  Creating the same near-duplicate item twice in a row produces a warning the first time and none
  the second, or vice versa, with no configuration change between the two attempts.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create an item, then create a second item with the same title and due date twice in a row, and
  compare the system's response each time.
```

## G12-PROJECT_TODO-Q048

```yaml
QID: G12-PROJECT_TODO-Q048
MODULE: project_todo
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A personal task item left incomplete when its linked project reaches a fully closed state follows
  one documented rule for its own resulting status, rather than being silently ignored by the
  project's closure processing.
WHY_IT_MATTERS: >
  A silently ignored open item would leave apparently unfinished work with no visible connection to
  the fact that its project has already closed.
DISCONFIRMING_OBSERVATION: >
  After the linked project reaches a fully closed state, the incomplete item shows no status change
  and no indication anywhere that its project has closed.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Leave a project-linked personal item incomplete, close the project fully, and check the resulting
  status and any indication shown on the still-open item.
```
