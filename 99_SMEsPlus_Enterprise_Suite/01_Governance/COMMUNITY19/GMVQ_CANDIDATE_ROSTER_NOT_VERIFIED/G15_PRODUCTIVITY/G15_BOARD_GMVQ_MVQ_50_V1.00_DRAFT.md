# SMEsPlus ENTERPRISE SUITE
## GMVQ — G15 PRODUCTIVITY / board Module MVQ Bank

**Document ID:** GMVQ-G15-BOARD-MVQ50-V1.00
**Group:** G15 PRODUCTIVITY (Wave W4)
**Module Metadata:** `board`
**Wave:** W4
**Author Cell:** P15-1 (GMVQ Question Factory — Production Cell P15-1)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the kanban/planning board capability — a
foundation module in the G15 Productivity group per the Group Brief. The material ground covers
card and column state transitions, ordering and concurrency, board/card/attachment permission
scope, automation and background processing, cross-module linking, auditability, and the
tenant/company boundary, as required for a foundation module carrying the group's deepest
treatment.

Question text is source-neutral. It does not name the module, any vendor or product, or any
technical identifier (field, model, method, XML ID, API path). Generic terms such as "column",
"card", "board" and "structural definition" are used throughout in place of any implementation-
specific naming.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 50 questions exist because each tests a distinct material hypothesis, spread across
  business capability, business rule, state transition, configuration dependency, role and
  permission, exception path, cancellation, reversal, negative case, cross-module dependency,
  optional behaviour, auditability, tenant/company boundary, concurrency and ordering, and runtime
  reachability.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G15-BOARD-Q001

```yaml
QID: G15-BOARD-Q001
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Moving a card to a new position within a column is durably persisted as the authoritative order
  for every viewer, not merely a local or client-side ordering.
WHY_IT_MATTERS: >
  Divergent card order between users undermines the board's usefulness as a shared source of truth
  for priority and sequencing.
DISCONFIRMING_OBSERVATION: >
  Two different users viewing the same board see the cards in a different order after one of them
  moves a card, with no synchronization occurring.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Open the same board in two sessions, move a card in one, refresh the other, and compare order.
```

## G15-BOARD-Q002

```yaml
QID: G15-BOARD-Q002
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When a column defines a maximum card count, the system prevents or explicitly flags moving an
  additional card in once that limit is reached, rather than silently accepting the move.
WHY_IT_MATTERS: >
  A work-in-progress limit is a control for flow discipline; a silent bypass defeats the reason it
  was configured.
DISCONFIRMING_OBSERVATION: >
  Moving a card into a column already at its configured maximum succeeds with no warning, block, or
  recorded exception.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure a column limit, fill the column to capacity, then attempt one more move into it.
```

## G15-BOARD-Q003

```yaml
QID: G15-BOARD-Q003
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A card's movement between columns is recorded in an auditable history distinct from its current
  position, not only reflected in where it currently sits.
WHY_IT_MATTERS: >
  Without a trace of prior state, no one can reconstruct how or when a card actually progressed,
  which defeats process review and accountability.
DISCONFIRMING_OBSERVATION: >
  After several column moves, no trace exists of what column a card previously occupied or when the
  change happened.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Move a card through several columns, then inspect whatever history or activity trail is available.
```

## G15-BOARD-Q004

```yaml
QID: G15-BOARD-Q004
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Archiving a card removes it from the active view while the underlying record and its history
  remain retrievable, rather than being irrecoverably destroyed.
WHY_IT_MATTERS: >
  Treating archiving as equivalent to deletion removes accountability for closed work and can defeat
  audit requirements.
DISCONFIRMING_OBSERVATION: >
  Archiving a card also erases its comment or activity history so that it cannot be restored intact.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Add comments and history to a card, archive it, then attempt to view or restore it.
```

## G15-BOARD-Q005

```yaml
QID: G15-BOARD-Q005
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two users dragging the same card to different columns at the same time resolve to one
  deterministic final state rather than corrupting the card into an inconsistent state.
WHY_IT_MATTERS: >
  A card left inconsistent between columns can be lost from work tracking entirely or double-counted
  in more than one place.
DISCONFIRMING_OBSERVATION: >
  After simultaneous conflicting moves, the card appears in two different columns for different
  viewers, or its column becomes unreadable or contradictory.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  From two concurrent sessions, move the same card to two different columns at nearly the same
  moment.
```

## G15-BOARD-Q006

```yaml
QID: G15-BOARD-Q006
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user without access to a board cannot view its cards through a direct reference to a specific
  card, even while otherwise authenticated.
WHY_IT_MATTERS: >
  A board-level permission that a direct link can bypass is not an effective control at all.
DISCONFIRMING_OBSERVATION: >
  A user who is not a member of the board can open a specific card by direct reference and see its
  content.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Obtain a direct reference to a card on a board the test user is not a member of, and attempt to
  open it.
```

## G15-BOARD-Q007

```yaml
QID: G15-BOARD-Q007
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A board marked private to its creator is not listed or discoverable through search by other users
  in the same company.
WHY_IT_MATTERS: >
  A private board that is discoverable defeats the purpose of marking it private and can expose
  sensitive planning content.
DISCONFIRMING_OBSERVATION: >
  Another user's search or board directory surfaces the name or content of a board marked private to
  its creator.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  Create a private board, then search for it and browse the board directory as a different user.
```

## G15-BOARD-Q008

```yaml
QID: G15-BOARD-Q008
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Removing a user from a board, or from the company, does not silently delete or strip attribution
  from cards they created or were assigned.
WHY_IT_MATTERS: >
  Losing attribution when staff change destroys the historical record of who did what.
DISCONFIRMING_OBSERVATION: >
  Cards previously owned by or assigned to a removed user vanish, or lose all historical attribution
  of that fact.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have a user create and be assigned cards, remove that user, then inspect the cards.
```

## G15-BOARD-Q009

```yaml
QID: G15-BOARD-Q009
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An automation rule that triggers on a card entering a given column fires exactly once per
  qualifying transition, not repeatedly on every later edit of a card already sitting there.
WHY_IT_MATTERS: >
  A repeatedly firing automation can send duplicate notifications or duplicate downstream actions,
  eroding trust in the automation entirely.
DISCONFIRMING_OBSERVATION: >
  Editing an unrelated field on a card already resting in the trigger column re-fires the
  automation.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure a column-entry automation, move a card in, then edit an unrelated field on that card and
  observe whether the automation fires again.
```

## G15-BOARD-Q010

```yaml
QID: G15-BOARD-Q010
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A recurring card template generates its next instance on its defined schedule independent of any
  user opening the board in the interim.
WHY_IT_MATTERS: >
  A recurrence that depends on someone happening to open the board is not a reliable schedule and
  will silently miss cycles.
DISCONFIRMING_OBSERVATION: >
  A recurring card's next instance only appears once a user manually opens or interacts with the
  board, indicating no independent process created it on schedule.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Configure a recurring card, let its next due cycle pass with nobody opening the board, then check
  whether the instance was created.
```

## G15-BOARD-Q011

```yaml
QID: G15-BOARD-Q011
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a card is overdue is evaluated consistently for every viewer with access, not dependent on
  each viewer's own local clock or time zone.
WHY_IT_MATTERS: >
  An overdue status that disagrees by viewer breaks any shared understanding of what is actually
  late.
DISCONFIRMING_OBSERVATION: >
  Two users in different time zones see conflicting overdue status for the same card with the same
  due date at the same real moment.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Set a due date near a time-zone boundary and compare overdue status across users in different time
  zones.
```

## G15-BOARD-Q012

```yaml
QID: G15-BOARD-Q012
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A bulk operation across multiple selected cards reports, per card, which succeeded and which
  failed, rather than reporting a single blanket success when some cards were not actually updated.
WHY_IT_MATTERS: >
  A false blanket success hides partial failures that later surface as missing or wrong data with no
  warning.
DISCONFIRMING_OBSERVATION: >
  A bulk operation reports overall success while some of the selected cards were not actually
  changed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Select a mixed set of cards, including at least one that should fail the operation, and run a bulk
  action.
```

## G15-BOARD-Q013

```yaml
QID: G15-BOARD-Q013
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A card's checklist completion percentage is derived directly from the state of its checklist items
  and cannot drift out of agreement with them.
WHY_IT_MATTERS: >
  A progress figure that disagrees with the items it summarizes misleads anyone relying on it to
  judge how much work remains.
DISCONFIRMING_OBSERVATION: >
  The displayed checklist progress on a card disagrees with the count of items actually marked
  complete within it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Add a checklist, mark some items complete, and compare the displayed percentage to a manual count.
```

## G15-BOARD-Q014

```yaml
QID: G15-BOARD-Q014
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A file attached to a card enforces the same access control as the card itself, so a person without
  card access cannot fetch the attachment through a bare reference.
WHY_IT_MATTERS: >
  An attachment reachable outside the card's own permission model is a direct data leak independent
  of the board's access controls.
DISCONFIRMING_OBSERVATION: >
  An attachment reference remains fetchable by someone without board or card permission after their
  access is revoked.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Attach a file to a card, capture its reference, revoke the accessing user's permission, then
  attempt to fetch the file with that reference.
```

## G15-BOARD-Q015

```yaml
QID: G15-BOARD-Q015
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A card linked to a record in another business area reflects that record's current state rather
  than a frozen copy taken at the moment the link was made.
WHY_IT_MATTERS: >
  A silently frozen copy misleads anyone using the board to track the live status of that other
  record.
DISCONFIRMING_OBSERVATION: >
  The linked reference on the card continues to show information that has since changed at the
  source, with no indication that it may be stale.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Link a card to a record elsewhere, change that record, then reopen the card.
```

## G15-BOARD-Q016

```yaml
QID: G15-BOARD-Q016
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting the source record a card links to leaves a recoverable and explicit broken-link
  indication rather than crashing the board view or silently vanishing the card.
WHY_IT_MATTERS: >
  An unhandled failure on a broken link can take down an entire shared board for everyone rather than
  degrading gracefully for the one affected card.
DISCONFIRMING_OBSERVATION: >
  Opening a board containing a card linked to a now-deleted record produces an unhandled error, or
  removes the card without any notice.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Link a card to a record, delete that record, then reopen the board.
```

## G15-BOARD-Q017

```yaml
QID: G15-BOARD-Q017
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Creating a new board from a template carries over only the structural definition (columns, labels)
  and not the template board's own live cards or assignees.
WHY_IT_MATTERS: >
  A template that leaks live content turns a reusable structure into an accidental data-sharing
  channel.
DISCONFIRMING_OBSERVATION: >
  A board created from a template inherits live cards or assignees belonging to the source template
  board.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Populate a template board with cards and assignees, then create a new board from that template.
```

## G15-BOARD-Q018

```yaml
QID: G15-BOARD-Q018
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Assigning a card to a user who lacks board access either is prevented or triggers an explicit
  access grant, rather than silently leaving that user unable to see their own assignment.
WHY_IT_MATTERS: >
  An assignment nobody can see defeats the purpose of assigning it and hides accountability gaps.
DISCONFIRMING_OBSERVATION: >
  A card is assigned to a user who, upon logging in, cannot locate or open the board containing it.
EXPECTED_SURFACE: S4,S1
PRECONDITIONS: >
  Assign a card to a user who is not currently a board member, then check that user's own access.
```

## G15-BOARD-Q019

```yaml
QID: G15-BOARD-Q019
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Cards, labels, and board templates belonging to one company are not visible or selectable from a
  session scoped to a different company on the same login.
WHY_IT_MATTERS: >
  A cross-company leak of board content breaks the tenant boundary that the whole multi-company model
  depends on.
DISCONFIRMING_OBSERVATION: >
  Switching the active company context still shows board content belonging to a different company.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with access to two companies, create board content under one and switch the active
  company to the other.
```

## G15-BOARD-Q020

```yaml
QID: G15-BOARD-Q020
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Undoing a card move restores both its prior column and its prior position within that column, not
  merely the prior column with the card appended at the end.
WHY_IT_MATTERS: >
  A partial undo silently changes the board's ordering as a side effect of correcting an unrelated
  mistake.
DISCONFIRMING_OBSERVATION: >
  Undoing a move places the card in the correct column but at a different position than it held
  before the move.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Note a card's exact position, move it, then use undo and compare the resulting position.
```

## G15-BOARD-Q021

```yaml
QID: G15-BOARD-Q021
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Concurrent edits to the same card's description by two users resolve to one defined, disclosed
  outcome rather than silently discarding one edit with no trace.
WHY_IT_MATTERS: >
  Silent data loss on concurrent edits erodes trust in collaborative editing and can discard
  meaningful work with no recourse.
DISCONFIRMING_OBSERVATION: >
  One user's edit to a card description disappears after a near-simultaneous edit by another, with no
  record that a conflict occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  From two sessions, edit the same card's description at nearly the same time and compare the
  outcome and any conflict notice.
```

## G15-BOARD-Q022

```yaml
QID: G15-BOARD-Q022
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Comments posted on a card remain attributed to their original author even after that author's
  account is later deactivated.
WHY_IT_MATTERS: >
  Losing comment attribution destroys accountability for decisions and instructions recorded on the
  card.
DISCONFIRMING_OBSERVATION: >
  A deactivated user's prior comments become anonymous or are reattributed to a different user.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Have a user post comments on a card, deactivate that user's account, then review the comments.
```

## G15-BOARD-Q023

```yaml
QID: G15-BOARD-Q023
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Exporting a board reflects only the cards and columns the exporting user has permission to see, not
  the full underlying board content.
WHY_IT_MATTERS: >
  An export that ignores view-level restrictions is a bypass of the permission model through a
  different feature.
DISCONFIRMING_OBSERVATION: >
  An export produced by a user with restricted column visibility includes cards from columns that
  user could not view in the interface.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Restrict a user's visibility to certain columns, then have that user export the board and inspect
  the result.
```

## G15-BOARD-Q024

```yaml
QID: G15-BOARD-Q024
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A card belongs to only one column as its primary state, and any secondary grouping (such as a
  swimlane or tag) does not create a second, conflicting notion of the card's current stage.
WHY_IT_MATTERS: >
  Two disagreeing notions of "current stage" make status reporting unreliable and confuse anyone
  relying on the board.
DISCONFIRMING_OBSERVATION: >
  The system reports two different current-stage values for the same card across different views.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Configure a secondary grouping alongside columns, then compare the stage shown in each view for the
  same card.
```

## G15-BOARD-Q025

```yaml
QID: G15-BOARD-Q025
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Archiving an entire board does not orphan a reference from an active record elsewhere that still
  points at one of its cards; the reference remains navigable or is clearly flagged.
WHY_IT_MATTERS: >
  A silently broken cross-reference elsewhere in the system misleads users who trust that reference to
  still be valid.
DISCONFIRMING_OBSERVATION: >
  A reference elsewhere in the system to a card on an archived board resolves to an unexplained error.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a reference elsewhere pointing at a card, archive the board it belongs to, then follow the
  reference.
```

## G15-BOARD-Q026

```yaml
QID: G15-BOARD-Q026
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reordering columns on a board is a shared structural change visible identically to every member,
  not a per-viewer personalization masquerading as a shared layout.
WHY_IT_MATTERS: >
  A layout that silently diverges between members breaks the shared mental model a board is meant to
  provide.
DISCONFIRMING_OBSERVATION: >
  One member's column reordering is not reflected when another member opens the same board.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Reorder columns as one member, then open the same board as a different member and compare.
```

## G15-BOARD-Q027

```yaml
QID: G15-BOARD-Q027
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A background process that flags cards as stale after a configurable period of inactivity runs
  independent of any user opening the board.
WHY_IT_MATTERS: >
  A staleness flag that only updates on manual page opens is unreliable for surfacing neglected work.
DISCONFIRMING_OBSERVATION: >
  Stale-card flags only update at the moment a user manually opens the board, indicating no
  independent scheduled evaluation exists.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Configure a staleness threshold, leave a card inactive past it with nobody opening the board, then
  check whether the flag was set.
```

## G15-BOARD-Q028

```yaml
QID: G15-BOARD-Q028
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A card explicitly marked restricted to a smaller group is enforced even against users who otherwise
  have full access to the board it sits on.
WHY_IT_MATTERS: >
  Card-level confidentiality that a general board permission overrides is not a real control.
DISCONFIRMING_OBSERVATION: >
  A user with general board access can open a card explicitly marked restricted to a smaller group.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Mark a card restricted to a subset of members, then attempt to open it as a member outside that
  subset.
```

## G15-BOARD-Q029

```yaml
QID: G15-BOARD-Q029
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Moving a card back out of a completion column reopens any dependent automation state, so a
  completion notification already sent is not reissued or left contradicting the reverted state.
WHY_IT_MATTERS: >
  Contradictory completion signals after a reversal mislead anyone downstream who trusted the earlier
  completion.
DISCONFIRMING_OBSERVATION: >
  A card moved back to an active column still displays as complete elsewhere, or an automation reissues
  its completion action inappropriately.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Move a card to a completion column with an automation attached, then move it back out and check
  dependent state.
```

## G15-BOARD-Q030

```yaml
QID: G15-BOARD-Q030
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Bulk card creation through import enforces the same required-field and validation rules as manual
  single-card creation, not a relaxed set.
WHY_IT_MATTERS: >
  An import path that skips validation is a controls bypass that produces incomplete or invalid data
  at scale.
DISCONFIRMING_OBSERVATION: >
  An import accepts cards missing data that manual creation would reject.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Attempt to import cards missing a required field and compare to attempting the same through manual
  creation.
```

## G15-BOARD-Q031

```yaml
QID: G15-BOARD-Q031
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to a card's due date is recorded in a way that is distinguishable from the card's general
  last-modified stamp, identifying who changed the date and when.
WHY_IT_MATTERS: >
  Without a distinguishable trail, nobody can determine whether or why a deadline commitment was
  changed after the fact.
DISCONFIRMING_OBSERVATION: >
  The history for a due-date change cannot be distinguished from other field edits in the audit
  trail.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Change a card's due date, then inspect the history alongside an unrelated field edit.
```

## G15-BOARD-Q032

```yaml
QID: G15-BOARD-Q032
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A board-wide label is managed centrally such that renaming it updates every card using it
  consistently, rather than requiring the label to be reapplied card by card.
WHY_IT_MATTERS: >
  Inconsistent labeling after a rename defeats the purpose of using shared labels for filtering and
  reporting.
DISCONFIRMING_OBSERVATION: >
  Renaming a label leaves some cards still displaying the old label text.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply a shared label to several cards, rename the label, then check every card using it.
```

## G15-BOARD-Q033

```yaml
QID: G15-BOARD-Q033
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A membership change to a board (adding or removing a member) takes effect for that member's next
  action, without requiring them to log out and back in.
WHY_IT_MATTERS: >
  Access changes that lag behind an active session let a removed member keep acting on data they
  should no longer reach.
DISCONFIRMING_OBSERVATION: >
  A removed member retains the ability to change cards on the board within the same active session
  well after removal.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Remove a member from a board while they have an active session open, then have them attempt a card
  change.
```

## G15-BOARD-Q034

```yaml
QID: G15-BOARD-Q034
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A checklist item with its own assignee and due date surfaces in that assignee's personal task view
  independent of the parent card being opened.
WHY_IT_MATTERS: >
  A sub-assignment invisible outside the parent card is easy to miss and defeats the purpose of
  assigning it individually.
DISCONFIRMING_OBSERVATION: >
  A checklist item assigned to someone does not appear in any personal task list for them outside the
  parent card.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Assign a checklist item to a user with its own due date, then check that user's personal task view.
```

## G15-BOARD-Q035

```yaml
QID: G15-BOARD-Q035
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Duplicating a card does not carry the original card's comment or activity history over as though it
  occurred on the new duplicate.
WHY_IT_MATTERS: >
  A duplicate that inherits another card's history misrepresents what actually happened on the new
  card.
DISCONFIRMING_OBSERVATION: >
  A duplicated card displays the original's historical comments as if they occurred on the new card.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Add comments to a card, duplicate it, and inspect the duplicate's history.
```

## G15-BOARD-Q036

```yaml
QID: G15-BOARD-Q036
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Applying a filter to a board view is a display-only operation that does not alter the stored card
  order or column membership seen by other viewers.
WHY_IT_MATTERS: >
  A filter that leaks into the shared data model would silently reorganize the board for everyone
  else based on one person's temporary view.
DISCONFIRMING_OBSERVATION: >
  Applying a filter changes what a different, non-filtering user sees as the card's actual column or
  position.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Apply a filter as one user, then check the board's actual state as a different, unfiltered user.
```

## G15-BOARD-Q037

```yaml
QID: G15-BOARD-Q037
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A logged time entry on a card is attributed to the user who logged it and cannot have its
  attribution altered by another member without a recorded change.
WHY_IT_MATTERS: >
  Silent reattribution of logged time undermines any reporting or accountability built on that data.
DISCONFIRMING_OBSERVATION: >
  A member other than the original logger can change the attributed user on an existing time entry
  without any recorded trace of the change.
EXPECTED_SURFACE: S6,S4
PRECONDITIONS: >
  Log time as one user, then attempt to alter its attribution as a different member.
```

## G15-BOARD-Q038

```yaml
QID: G15-BOARD-Q038
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Changing a default board template's structure does not retroactively alter boards already created
  from it.
WHY_IT_MATTERS: >
  Retroactive structural changes to existing boards can silently disrupt in-flight work that depended
  on the prior structure.
DISCONFIRMING_OBSERVATION: >
  Changing the default template afterward silently restructures the columns of boards already
  created.
EXPECTED_SURFACE: S7,S1
PRECONDITIONS: >
  Create a board from a template, then change the template and check whether the existing board
  changed.
```

## G15-BOARD-Q039

```yaml
QID: G15-BOARD-Q039
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A card in an automation chain that triggers an external notification does not resend that
  notification if the same qualifying transition is reached again through an undo followed by a
  redo.
WHY_IT_MATTERS: >
  A duplicate notification for a single logical event misrepresents to recipients that something new
  happened.
DISCONFIRMING_OBSERVATION: >
  Undoing and then redoing the same move causes a duplicate outbound notification for one logical
  transition.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Trigger a notifying automation with a move, undo the move, then redo it and observe notifications.
```

## G15-BOARD-Q040

```yaml
QID: G15-BOARD-Q040
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user can move a card into a column only if their role has been granted move permission for that
  column, distinct from general board view or comment rights.
WHY_IT_MATTERS: >
  Without a distinct move permission, anyone who can comment can also alter workflow state, which is
  a broader capability than intended.
DISCONFIRMING_OBSERVATION: >
  A user with view-and-comment-only rights on the board is able to move cards between columns.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Grant a user view-and-comment-only rights, then attempt to move a card as that user.
```

## G15-BOARD-Q041

```yaml
QID: G15-BOARD-Q041
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The board's activity feed reflects events in the true chronological order they occurred, not the
  order in which underlying writes happened to complete under load.
WHY_IT_MATTERS: >
  A feed out of true order misrepresents the sequence of events to anyone reviewing what happened.
DISCONFIRMING_OBSERVATION: >
  Under concurrent activity, the feed displays two related events, such as a comment before the move
  it responds to, out of their actual sequence.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Generate closely-timed related events under concurrent load and compare the feed order to actual
  occurrence order.
```

## G15-BOARD-Q042

```yaml
QID: G15-BOARD-Q042
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Renaming a board or editing its description does not disturb the position or column assignment of
  its existing cards.
WHY_IT_MATTERS: >
  A structural metadata edit that silently reshuffles cards would make routine housekeeping
  destructive.
DISCONFIRMING_OBSERVATION: >
  Renaming a board resets or reorders its cards.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Note card positions, rename the board, and re-check the positions.
```

## G15-BOARD-Q043

```yaml
QID: G15-BOARD-Q043
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Guest or external access to a board is scoped to specific cards or columns explicitly shared,
  rather than granting the same visibility as an internal member by default.
WHY_IT_MATTERS: >
  A guest with default internal-level visibility can see far more of the board than was intended when
  they were invited.
DISCONFIRMING_OBSERVATION: >
  A guest granted access to one card can browse the rest of the board's cards and columns.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Grant a guest access scoped to a single card, then attempt to browse the rest of the board as that
  guest.
```

## G15-BOARD-Q044

```yaml
QID: G15-BOARD-Q044
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A card cannot exist as the same live record on two different boards at once; moving it between
  boards relocates it rather than creating a dual presence.
WHY_IT_MATTERS: >
  A card active on two boards at once creates ambiguity about which board's process actually owns it.
DISCONFIRMING_OBSERVATION: >
  After moving a card to another board, it still appears as an active, editable card on the original
  board.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Move a card from one board to another, then check whether it still appears active on the original.
```

## G15-BOARD-Q045

```yaml
QID: G15-BOARD-Q045
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A configured "definition of done" for a column, stating criteria required before a card can enter
  it, is enforced at the point of the move, not merely shown as unenforced guidance text.
WHY_IT_MATTERS: >
  Guidance with no functional enforcement is easily ignored under time pressure, defeating the
  process control it was meant to provide.
DISCONFIRMING_OBSERVATION: >
  A card missing the stated required criteria is still allowed to move into a column that declares
  them mandatory.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure mandatory entry criteria for a column, then attempt to move in a card that does not meet
  them.
```

## G15-BOARD-Q046

```yaml
QID: G15-BOARD-Q046
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Restoring an archived card returns it to its last known column and position, rather than a default
  first column, unless that original column no longer exists.
WHY_IT_MATTERS: >
  Restoring to the wrong column re-injects a card into the wrong stage of the workflow, misleading
  anyone tracking progress.
DISCONFIRMING_OBSERVATION: >
  Restoring an archived card always places it in the first column regardless of which column it was
  archived from.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Archive a card from a non-first column, then restore it and check its resulting column.
```

## G15-BOARD-Q047

```yaml
QID: G15-BOARD-Q047
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Company-wide search for card content only returns results from boards the searching user has
  permission to access.
WHY_IT_MATTERS: >
  A search that ignores board-level permission is a systemic bypass of every board's access controls
  at once.
DISCONFIRMING_OBSERVATION: >
  A company-wide search surfaces the title or content of a card on a board the searching user cannot
  open.
EXPECTED_SURFACE: S4,S3
PRECONDITIONS: >
  Create a card with distinctive text on a board the test user cannot access, then search for that
  text as that user.
```

## G15-BOARD-Q048

```yaml
QID: G15-BOARD-Q048
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A card declared blocked by an unfinished dependency is at minimum flagged as a warning, if not
  prevented, when an attempt is made to move it to completion.
WHY_IT_MATTERS: >
  Silently allowing a blocked card to complete hides a real dependency violation from anyone relying
  on the board to reflect true readiness.
DISCONFIRMING_OBSERVATION: >
  A card marked blocked by an unfinished dependency can be moved to a completion state with no warning
  or recorded conflict.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Mark a card as blocked by another unfinished card, then attempt to move the blocked card to
  completion.
```

## G15-BOARD-Q049

```yaml
QID: G15-BOARD-Q049
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A board notification preference such as mute is personal to the user who sets it and does not
  suppress notifications for other members of the same board.
WHY_IT_MATTERS: >
  A personal preference that silently affects others would mean nobody could rely on their own
  notification settings taking effect.
DISCONFIRMING_OBSERVATION: >
  One member muting a board's notifications also silences notifications for other members.
EXPECTED_SURFACE: S4,S8
PRECONDITIONS: >
  Have one member mute board notifications, then check whether another member still receives them.
```

## G15-BOARD-Q050

```yaml
QID: G15-BOARD-Q050
MODULE: board
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a card's assignee changes, the previous assignee's outstanding reminders tied to that card are
  resolved rather than continuing to fire for someone no longer responsible.
WHY_IT_MATTERS: >
  Reminders that keep firing for the wrong person create noise and confusion about who currently owns
  the work.
DISCONFIRMING_OBSERVATION: >
  The former assignee continues to receive due-date reminders for a card after it was reassigned to
  someone else.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Set a due-date reminder on a card, reassign the card to a different user, then observe whether the
  former assignee still receives reminders.
```
