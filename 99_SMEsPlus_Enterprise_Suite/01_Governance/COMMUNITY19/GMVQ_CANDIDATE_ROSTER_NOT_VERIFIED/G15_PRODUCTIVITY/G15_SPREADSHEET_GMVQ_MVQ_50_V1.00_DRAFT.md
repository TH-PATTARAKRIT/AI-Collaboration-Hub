# SMEsPlus ENTERPRISE SUITE
## GMVQ — G15 PRODUCTIVITY / spreadsheet Module MVQ Bank

**Document ID:** GMVQ-G15-SPREADSHEET-MVQ50-V1.00
**Group:** G15 PRODUCTIVITY (Wave W4)
**Module Metadata:** `spreadsheet`
**Wave:** W4
**Author Cell:** P15-1 (GMVQ Question Factory — Production Cell P15-1)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the collaborative spreadsheet capability — a
foundation module in the G15 Productivity group. The material ground covers formula recalculation
and dependency ordering, cross-sheet and cross-workbook referencing, structural edits (insertion,
deletion, merge), concurrent and offline editing conflicts, permission and protection scope,
version history, validation and import behaviour, and the tenant/company boundary.

Question text is source-neutral. It does not name the module, any vendor or product, or any
technical identifier. Generic terms such as "workbook", "sheet", "cell" and "range" are used
throughout in place of implementation-specific naming.

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

## G15-SPREADSHEET-Q001

```yaml
QID: G15-SPREADSHEET-Q001
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A formula referencing a cell on another sheet recalculates automatically when that source cell
  changes, rather than freezing at the value present when the formula was authored.
WHY_IT_MATTERS: >
  A formula that silently stops tracking its source turns a live calculation into a misleading,
  stale number.
DISCONFIRMING_OBSERVATION: >
  Changing the source cell's value produces no change in the dependent formula's result without an
  undocumented manual recalculation step.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a cross-sheet formula reference, change the source cell, and observe whether the dependent
  cell updates.
```

## G15-SPREADSHEET-Q002

```yaml
QID: G15-SPREADSHEET-Q002
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Inserting a row above cells referenced by a formula updates the formula's reference to track the
  same logical cell, rather than pointing at whatever now occupies the old coordinate.
WHY_IT_MATTERS: >
  A reference that silently repoints to the wrong cell after a structural edit corrupts every
  calculation built on it without any visible sign of error.
DISCONFIRMING_OBSERVATION: >
  Inserting a row shifts a formula's result because it now points at different data than what it
  originally referenced.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Build a formula referencing a specific cell, insert a row above it, and check the formula's
  reference and result.
```

## G15-SPREADSHEET-Q003

```yaml
QID: G15-SPREADSHEET-Q003
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A formula chain that refers back to itself is flagged as a circular reference rather than silently
  producing an unstable or incorrect number.
WHY_IT_MATTERS: >
  An undetected circular calculation can settle on a plausible-looking but meaningless figure that
  nobody has reason to question.
DISCONFIRMING_OBSERVATION: >
  A circular formula chain returns a plausible-looking number with no warning that the calculation is
  circular.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct a formula chain where a cell indirectly refers to itself and observe the result and any
  warning.
```

## G15-SPREADSHEET-Q004

```yaml
QID: G15-SPREADSHEET-Q004
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Concurrent edits to the same cell by two collaborators resolve to one defined, disclosed outcome
  rather than silently discarding one edit with no trace that a conflict occurred.
WHY_IT_MATTERS: >
  Silent loss of a collaborator's edit destroys trust in real-time collaboration and can discard
  meaningful data changes with no recourse.
DISCONFIRMING_OBSERVATION: >
  One collaborator's edit to a cell disappears after a near-simultaneous edit by another, with no
  indication a conflict occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  From two sessions, edit the same cell at nearly the same moment and inspect the resulting value and
  any conflict notice.
```

## G15-SPREADSHEET-Q005

```yaml
QID: G15-SPREADSHEET-Q005
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A protected or locked cell rejects a direct edit from a user without override permission through
  every entry path, including paste, not only through direct typing.
WHY_IT_MATTERS: >
  A protection that a paste operation bypasses is not a real control; it merely inconveniences the
  legitimate path while leaving the actual restriction open.
DISCONFIRMING_OBSERVATION: >
  Pasting a value into a protected cell succeeds for a user who lacks override permission, even
  though direct typing into it is blocked.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Protect a cell, deny override to a user, and have that user attempt both a direct edit and a paste
  into it.
```

## G15-SPREADSHEET-Q006

```yaml
QID: G15-SPREADSHEET-Q006
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A data validation rule restricting a cell to an allowed set of values is enforced on paste and
  import, not only on manual entry through the cell's own input control.
WHY_IT_MATTERS: >
  A validation rule enforced on only one entry path is a control with a known, easy bypass.
DISCONFIRMING_OBSERVATION: >
  Pasting or importing a value outside the allowed set bypasses a validation rule that blocks the
  same value when typed directly.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Configure a validation rule on a cell, then attempt an out-of-range value via typing, paste, and
  import.
```

## G15-SPREADSHEET-Q007

```yaml
QID: G15-SPREADSHEET-Q007
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Version history retains prior states of a sheet sufficient to restore a previous version, and
  restoring does not silently merge in intervening unsaved changes without notice.
WHY_IT_MATTERS: >
  An opaque merge during restore leaves nobody able to tell which cells came from which point in
  time, undermining the entire purpose of version history.
DISCONFIRMING_OBSERVATION: >
  Restoring an earlier version silently blends in edits made after that version, with no way to tell
  which cells came from which point in time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Save a version, make further edits, then restore the earlier version and inspect the outcome.
```

## G15-SPREADSHEET-Q008

```yaml
QID: G15-SPREADSHEET-Q008
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A named range's reference updates automatically when the ranged cells move due to row or column
  insertion, rather than continuing to point at fixed coordinates that no longer align.
WHY_IT_MATTERS: >
  A named range that drifts from its intended cells after a structural edit corrupts every formula
  that uses the name without any obvious sign.
DISCONFIRMING_OBSERVATION: >
  After inserting rows within a named range's span, formulas using that name compute against the
  wrong cells.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Define a named range, insert rows within its span, and check formulas using the name.
```

## G15-SPREADSHEET-Q009

```yaml
QID: G15-SPREADSHEET-Q009
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting a sheet within a workbook that other sheets' formulas reference leaves those formulas in a
  clearly broken error state rather than silently returning a plausible but wrong value.
WHY_IT_MATTERS: >
  A silently wrong value after a structural deletion is far more dangerous than an obvious error,
  because nobody has reason to check it.
DISCONFIRMING_OBSERVATION: >
  After deleting a referenced sheet, dependent formulas elsewhere show a normal-looking number
  instead of an error.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Reference one sheet's cells from another, delete the referenced sheet, and inspect the dependent
  formulas.
```

## G15-SPREADSHEET-Q010

```yaml
QID: G15-SPREADSHEET-Q010
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A sheet shared with view-only permission cannot have its stored values altered through any
  available interaction, including any duplication-then-swap style path.
WHY_IT_MATTERS: >
  A view-only restriction with any writable side channel is not an effective control on shared data.
DISCONFIRMING_OBSERVATION: >
  A view-only collaborator finds a path that changes the shared sheet's actual stored values.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Share a sheet as view-only and attempt every available interaction that might alter its stored
  content.
```

## G15-SPREADSHEET-Q011

```yaml
QID: G15-SPREADSHEET-Q011
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Exporting a sheet to a static file captures its currently computed values, not a stale cached value
  from before the last recalculation.
WHY_IT_MATTERS: >
  An export that reflects stale figures misleads anyone who treats it as a faithful snapshot of the
  live sheet.
DISCONFIRMING_OBSERVATION: >
  An exported file shows a value that disagrees with what the live sheet currently displays for the
  same cell, with no pending recalculation in progress.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Change a value, allow recalculation to settle, export the sheet, and compare the exported value to
  the live one.
```

## G15-SPREADSHEET-Q012

```yaml
QID: G15-SPREADSHEET-Q012
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Autofill series generation follows a disclosed, consistent pattern-detection rule, so the same
  starting values always produce the same continuation.
WHY_IT_MATTERS: >
  An unpredictable autofill result undermines confidence in a routine, frequently used feature.
DISCONFIRMING_OBSERVATION: >
  Filling the same two starting values in the same way on different occasions produces different
  extrapolated series with no configuration difference.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Repeat the same autofill operation from the same starting values on separate occasions and compare
  results.
```

## G15-SPREADSHEET-Q013

```yaml
QID: G15-SPREADSHEET-Q013
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Merging a range of cells that contained multiple distinct values does not discard the non-retained
  values without at least a confirmation or a recoverable trace.
WHY_IT_MATTERS: >
  Silent, unrecoverable data loss on a routine formatting action is a serious usability and integrity
  risk.
DISCONFIRMING_OBSERVATION: >
  Merging a range that contained multiple distinct values leaves no way to determine or recover the
  discarded ones.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Populate a range with distinct values, merge the cells, and attempt to recover the non-retained
  values.
```

## G15-SPREADSHEET-Q014

```yaml
QID: G15-SPREADSHEET-Q014
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A personal, unshared filter view applied by one collaborator does not alter the visible rows for
  other collaborators concurrently editing the same sheet.
WHY_IT_MATTERS: >
  A personal view leaking into the shared state would mean nobody could safely apply a filter without
  disrupting everyone else.
DISCONFIRMING_OBSERVATION: >
  One user's personal filter changes another concurrent user's visible row set on the same shared
  sheet.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  Apply a personal filter as one user while a second user is concurrently viewing the same sheet, and
  compare what each sees.
```

## G15-SPREADSHEET-Q015

```yaml
QID: G15-SPREADSHEET-Q015
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Locale-dependent parsing of a typed numeric value, such as the decimal separator convention, is
  applied consistently, so identical keystrokes do not silently produce a materially different stored
  number for users under different locale settings.
WHY_IT_MATTERS: >
  A silent locale-driven misparse of a number can turn a decimal point into a thousands separator or
  vice versa, producing an order-of-magnitude error nobody would think to check.
DISCONFIRMING_OBSERVATION: >
  Identical typed input produces silently different stored numeric values for collaborators under
  different locale settings, with no indication of the discrepancy.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Have users under two different locale settings type the identical numeric string into equivalent
  cells and compare stored values.
```

## G15-SPREADSHEET-Q016

```yaml
QID: G15-SPREADSHEET-Q016
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A formula error such as divide by zero propagates as a visible error state to every formula that
  depends on it, rather than being silently coerced to zero or blank somewhere in the dependency
  chain.
WHY_IT_MATTERS: >
  A silently absorbed error can make a downstream total look complete and correct when it is actually
  built on a failure.
DISCONFIRMING_OBSERVATION: >
  A downstream formula that depends on a cell in error state shows a normal numeric result instead of
  propagating the error.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Introduce a divide-by-zero error and check whether formulas depending on it also show an error.
```

## G15-SPREADSHEET-Q017

```yaml
QID: G15-SPREADSHEET-Q017
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Freezing rows or columns is a display and navigation convenience only, and does not alter how
  formulas reference or calculate against the frozen cells.
WHY_IT_MATTERS: >
  A display setting that silently changes calculation behaviour would be a hidden and unexpected side
  effect of a routine navigation feature.
DISCONFIRMING_OBSERVATION: >
  Freezing a row changes the result of a formula that references cells within it.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Note a formula's result, freeze the row or column it references, and re-check the result.
```

## G15-SPREADSHEET-Q018

```yaml
QID: G15-SPREADSHEET-Q018
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A conditional formatting rule that depends on another cell's value updates its visual state when
  that source cell changes, without requiring the formatted cell to be re-entered.
WHY_IT_MATTERS: >
  A formatting rule that lags behind its own trigger misleads anyone scanning the sheet visually for
  its current state.
DISCONFIRMING_OBSERVATION: >
  Changing the source cell referenced by a conditional formatting rule leaves the dependent cell's
  formatting unchanged until it is manually re-edited.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Configure conditional formatting dependent on another cell, change that cell, and observe whether
  formatting updates.
```

## G15-SPREADSHEET-Q019

```yaml
QID: G15-SPREADSHEET-Q019
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A linked external data source discloses how stale its currently displayed value is, rather than
  presenting a cached figure indistinguishably from a freshly fetched one.
WHY_IT_MATTERS: >
  An undisclosed staleness on external data can lead to decisions made on figures that are actually
  out of date.
DISCONFIRMING_OBSERVATION: >
  A linked external data value gives no indication of how long ago it was last refreshed.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Link an external data source, let time pass without refreshing, and check for any staleness
  disclosure.
```

## G15-SPREADSHEET-Q020

```yaml
QID: G15-SPREADSHEET-Q020
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Undo restores a cell to its exact prior value and formula across a sequence of several intervening
  edits, in true reverse order.
WHY_IT_MATTERS: >
  An undo history that does not reconstruct the true prior sequence can leave the sheet in a state the
  user never actually intended.
DISCONFIRMING_OBSERVATION: >
  Repeated undo steps do not reconstruct the exact sequence of prior states in reverse order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Make several successive edits to the same cell, then step back through undo and compare each state
  to the actual edit history.
```

## G15-SPREADSHEET-Q021

```yaml
QID: G15-SPREADSHEET-Q021
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting a row or column that removes cells referenced by a formula results in a defined error
  reference, rather than the formula silently computing against an unrelated, now-shifted cell.
WHY_IT_MATTERS: >
  A silent repoint to unrelated data after a deletion produces a wrong number with no visible sign
  that anything went wrong.
DISCONFIRMING_OBSERVATION: >
  Deleting a row referenced by a formula causes the formula to silently compute against different,
  unrelated data with no error shown.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reference a specific cell in a formula, delete the row containing it, and inspect the formula.
```

## G15-SPREADSHEET-Q022

```yaml
QID: G15-SPREADSHEET-Q022
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A sheet or workbook-level permission change takes effect for a collaborator's next action without
  requiring a fresh login.
WHY_IT_MATTERS: >
  A revocation that lags behind an active session lets someone keep acting on data they should no
  longer reach.
DISCONFIRMING_OBSERVATION: >
  A collaborator whose access was just revoked can continue editing within the same open session well
  past the revocation.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Revoke a collaborator's access while their session is active, then have them attempt to edit.
```

## G15-SPREADSHEET-Q023

```yaml
QID: G15-SPREADSHEET-Q023
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A workbook duplicated from a template retains only its structural layout and formulas relative to
  itself, not a live link back to the original template's own data.
WHY_IT_MATTERS: >
  A template that stays live-linked after duplication turns a reusable structure into an unintended
  data-sharing channel.
DISCONFIRMING_OBSERVATION: >
  Editing the original template after duplication also changes values in the already-duplicated copy.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Duplicate a workbook from a template, then edit the original template and check the copy.
```

## G15-SPREADSHEET-Q024

```yaml
QID: G15-SPREADSHEET-Q024
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A pivot-style aggregation over a range recalculates when the underlying source data changes, rather
  than requiring an unprompted manual refresh with no indication that one is needed.
WHY_IT_MATTERS: >
  A stale aggregation with no staleness signal can be mistaken for a current total.
DISCONFIRMING_OBSERVATION: >
  Changing source data leaves an aggregation table showing outdated totals with no visible indication
  that a refresh is pending.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Build an aggregation over a range, change the underlying source data, and check for a refresh
  indication.
```

## G15-SPREADSHEET-Q025

```yaml
QID: G15-SPREADSHEET-Q025
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A sheet approaching a size or row-count limit is handled with an explicit limit-reached notice
  rather than silently truncating or dropping data beyond the limit.
WHY_IT_MATTERS: >
  Silently dropped data at a hidden limit can cause a material record to simply disappear with no
  warning to the user.
DISCONFIRMING_OBSERVATION: >
  Data entered or imported beyond an undisclosed size limit disappears without any warning that a
  limit was hit.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Enter or import data that approaches and then exceeds a size limit, and observe the behaviour at the
  boundary.
```

## G15-SPREADSHEET-Q026

```yaml
QID: G15-SPREADSHEET-Q026
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reopening a sheet after an offline editing session reconciles the offline changes against edits
  others made in the meantime with a defined conflict outcome, rather than silently overwriting one
  side's work.
WHY_IT_MATTERS: >
  A silent overwrite on reconnection can discard a collaborator's work with no way to know it ever
  existed.
DISCONFIRMING_OBSERVATION: >
  Reconnecting after offline edits overwrites a collaborator's intervening online changes without any
  conflict indication.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Edit a sheet while offline while a second user edits the same area online, then reconnect and
  inspect the result.
```

## G15-SPREADSHEET-Q027

```yaml
QID: G15-SPREADSHEET-Q027
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A cell's displayed formatted value, such as a rounded or currency-formatted figure, never becomes
  what is actually used as the underlying stored value in subsequent calculations that reference it.
WHY_IT_MATTERS: >
  If display rounding leaks into calculation, small formatting choices silently change financial
  totals without anyone changing the underlying data.
DISCONFIRMING_OBSERVATION: >
  A formula referencing a cell computes using the visually rounded or formatted value rather than the
  cell's full underlying stored value.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Format a cell to display a rounded value, then build a formula referencing it and compare the
  formula's result to the true underlying value.
```

## G15-SPREADSHEET-Q028

```yaml
QID: G15-SPREADSHEET-Q028
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A sheet shared via a generated link honors the view-versus-edit permission chosen at share time and
  does not grant edit rights through a separate access path such as duplication followed by
  re-linking.
WHY_IT_MATTERS: >
  A permission that a workaround defeats is not a real boundary, and undermines every view-only
  sharing decision made through the feature.
DISCONFIRMING_OBSERVATION: >
  A link shared as view-only allows the recipient to make edits that persist to the original sheet
  through some available path.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Share a sheet as view-only via a link and attempt every available path to make a persisting edit.
```

## G15-SPREADSHEET-Q029

```yaml
QID: G15-SPREADSHEET-Q029
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A comment attached to a cell remains anchored to that specific cell's logical position even after
  rows or columns are inserted or reordered around it.
WHY_IT_MATTERS: >
  A comment that drifts to the wrong cell after a structural edit misattributes context to unrelated
  data.
DISCONFIRMING_OBSERVATION: >
  Inserting a row correctly shifts a cell's data but leaves its attached comment anchored to the
  wrong cell.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attach a comment to a cell, insert a row above it, and check whether the comment moved with the
  cell.
```

## G15-SPREADSHEET-Q030

```yaml
QID: G15-SPREADSHEET-Q030
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A script or macro capability, where available, runs only with the permission level of the user who
  explicitly triggers it, not with a fixed or elevated permission regardless of who runs it.
WHY_IT_MATTERS: >
  A macro running with elevated privilege becomes a permission-escalation path for anyone who can
  trigger it.
DISCONFIRMING_OBSERVATION: >
  A macro performs an action that the triggering user's own permissions would not otherwise allow
  them to perform directly.
EXPECTED_SURFACE: S4,S3
PRECONDITIONS: >
  Configure a macro performing a privileged action, then trigger it as a user who lacks that
  privilege directly.
```

## G15-SPREADSHEET-Q031

```yaml
QID: G15-SPREADSHEET-Q031
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A workbook belonging to one company or tenant is not selectable or referenceable from a session
  scoped to a different company.
WHY_IT_MATTERS: >
  A cross-tenant leak of spreadsheet data breaks the fundamental boundary the whole multi-company
  model depends on.
DISCONFIRMING_OBSERVATION: >
  Switching the active company context still allows opening or referencing a workbook belonging to a
  different company.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with access to two companies, create a workbook under one and switch the active company
  to the other.
```

## G15-SPREADSHEET-Q032

```yaml
QID: G15-SPREADSHEET-Q032
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Simultaneous save attempts by two collaborators on the same workbook produce a single, consistent
  final saved state rather than a corrupted or partially-written file.
WHY_IT_MATTERS: >
  A corrupted save under concurrent access could destroy an entire workbook's data with no recovery
  path.
DISCONFIRMING_OBSERVATION: >
  Near-simultaneous saves by two collaborators result in a workbook that fails to open correctly or
  loses an entire collaborator's changes without any conflict notice.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Trigger near-simultaneous saves from two sessions on the same workbook and inspect the result.
```

## G15-SPREADSHEET-Q033

```yaml
QID: G15-SPREADSHEET-Q033
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A formula referencing another external workbook discloses when that link is stale or unreachable,
  rather than silently substituting a cached or blank value with no indication.
WHY_IT_MATTERS: >
  An undisclosed stale external link can present outdated figures as though they were current.
DISCONFIRMING_OBSERVATION: >
  An external-workbook reference shows a value with no way to tell whether the external source is
  currently reachable or the value is stale.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Link to an external workbook, make that source unreachable, and check the referencing cell's
  display.
```

## G15-SPREADSHEET-Q034

```yaml
QID: G15-SPREADSHEET-Q034
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Text entered that resembles a number, such as an identifier with a leading zero, is preserved as
  entered rather than being silently coerced into a numeric type that drops meaningful formatting.
WHY_IT_MATTERS: >
  Silent coercion of an identifier into a number can permanently drop a leading zero that changes its
  meaning.
DISCONFIRMING_OBSERVATION: >
  A value such as an identifier with a leading zero is silently converted to a number and loses the
  leading zero without the user requesting numeric conversion.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enter a text-like identifier containing a leading zero into a cell and inspect the stored value.
```

## G15-SPREADSHEET-Q035

```yaml
QID: G15-SPREADSHEET-Q035
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Bulk pasting a range of relative-reference formulas correctly adjusts each pasted cell's reference
  to its new position, while any absolute references in the same range remain fixed.
WHY_IT_MATTERS: >
  A paste that mishandles relative versus absolute references silently produces wrong calculations
  across an entire pasted range.
DISCONFIRMING_OBSERVATION: >
  Pasting a range of relative-reference formulas into a new location fails to adjust references per
  cell, or an absolute reference in the range shifts when it should not.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Build a range containing both relative and absolute formula references, paste it elsewhere, and
  inspect the resulting references.
```

## G15-SPREADSHEET-Q036

```yaml
QID: G15-SPREADSHEET-Q036
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A protected range within an otherwise editable sheet is enforced for every collaborator with edit
  rights on the sheet as a whole, not only for those without any edit rights at all.
WHY_IT_MATTERS: >
  A protection that yields to general sheet edit rights is not actually protecting the range from the
  people most likely to accidentally alter it.
DISCONFIRMING_OBSERVATION: >
  A collaborator with general sheet edit rights can still alter a range that was explicitly protected
  within that sheet.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Protect a specific range within a sheet a collaborator can otherwise edit, then have that
  collaborator attempt to change it.
```

## G15-SPREADSHEET-Q037

```yaml
QID: G15-SPREADSHEET-Q037
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reverting a sheet to a previous saved version restores its associated metadata, such as validation
  rules, consistent with that version rather than applying the currently configured rules to old
  data.
WHY_IT_MATTERS: >
  A version restore mixing old data with current rules misrepresents what that historical version
  actually looked like.
DISCONFIRMING_OBSERVATION: >
  Restoring a previous version applies the sheet's current validation or configuration rules rather
  than the rules in force at that historical version.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Save a version, change a validation rule, and restore the earlier version to see which rule set
  applies.
```

## G15-SPREADSHEET-Q038

```yaml
QID: G15-SPREADSHEET-Q038
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A chart built from a range updates when the underlying range's data changes, without requiring the
  chart to be manually recreated.
WHY_IT_MATTERS: >
  A chart frozen at its creation moment misleads anyone using it to track current figures visually.
DISCONFIRMING_OBSERVATION: >
  Changing the data behind a chart's source range leaves the chart displaying the old values
  indefinitely.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Build a chart from a range, change the underlying data, and observe whether the chart updates.
```

## G15-SPREADSHEET-Q039

```yaml
QID: G15-SPREADSHEET-Q039
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Deactivating a collaborator's account does not retroactively alter the historical attribution of
  edits or comments they made while active.
WHY_IT_MATTERS: >
  Losing historical attribution when staff change destroys the ability to audit who actually made a
  change.
DISCONFIRMING_OBSERVATION: >
  A deactivated collaborator's prior edit history or comments become anonymous or reattributed after
  their account is removed.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Have a collaborator make edits and comments, deactivate their account, then inspect the history.
```

## G15-SPREADSHEET-Q040

```yaml
QID: G15-SPREADSHEET-Q040
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Programmatic access to a workbook's data returns values consistent with what the interactive
  interface currently shows for the same cell, not a differently cached or stale copy.
WHY_IT_MATTERS: >
  A divergence between programmatic and interactive views of the same data undermines any integration
  that relies on the data being consistent.
DISCONFIRMING_OBSERVATION: >
  Reading a cell's value through a programmatic path returns a different result than the interactive
  view for the same cell at the same moment with no pending recalculation.
EXPECTED_SURFACE: S3,S1
PRECONDITIONS: >
  Read a cell's value both interactively and through any available programmatic access at the same
  moment and compare.
```

## G15-SPREADSHEET-Q041

```yaml
QID: G15-SPREADSHEET-Q041
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Changing a workbook-level default currency or number format does not retroactively alter values
  already explicitly formatted differently at the cell level.
WHY_IT_MATTERS: >
  A default change that overrides deliberate cell-level formatting could silently misrepresent
  figures a user specifically formatted a certain way for a reason.
DISCONFIRMING_OBSERVATION: >
  Changing the workbook default format overrides cell-level formatting a user had explicitly set
  differently.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set an explicit cell-level format different from the workbook default, then change the workbook
  default and check the cell.
```

## G15-SPREADSHEET-Q042

```yaml
QID: G15-SPREADSHEET-Q042
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A collaborator removed from a workbook's share list loses the ability to retrieve live, updating
  data through any previously generated export or snapshot link tied to that workbook.
WHY_IT_MATTERS: >
  A live link that survives revocation is a persistent, unrevoked access path invisible to whoever
  removed the collaborator.
DISCONFIRMING_OBSERVATION: >
  A removed collaborator can still retrieve live, updating data for the workbook through a previously
  obtained export or snapshot link.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Obtain an export or snapshot link as a collaborator, remove that collaborator's access, and retest
  the link.
```

## G15-SPREADSHEET-Q043

```yaml
QID: G15-SPREADSHEET-Q043
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Recalculation across a workbook resolves dependency chains correctly so a formula never uses a
  stale pre-update value from another cell that also changed within the same recalculation pass.
WHY_IT_MATTERS: >
  A recalculation ordering bug can produce different results on different occasions for the exact
  same set of inputs, making the workbook unreliable.
DISCONFIRMING_OBSERVATION: >
  Within a single recalculation, a formula's result reflects an outdated value from another cell that
  had also just changed in the same pass.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Change two interdependent cells at once and inspect whether dependent formulas reflect both updated
  values consistently.
```

## G15-SPREADSHEET-Q044

```yaml
QID: G15-SPREADSHEET-Q044
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Hiding a row or column is a display setting that does not exclude the hidden data from a formula or
  aggregation referencing it, unless that function is explicitly defined to exclude hidden data.
WHY_IT_MATTERS: >
  A hide action that silently changes calculation results conflates a visual convenience with a data
  operation, producing surprising totals.
DISCONFIRMING_OBSERVATION: >
  Hiding a row silently excludes its value from a sum or aggregation formula that was not defined to
  exclude hidden rows.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Build a sum over a range, hide one of its rows, and check whether the sum changed.
```

## G15-SPREADSHEET-Q045

```yaml
QID: G15-SPREADSHEET-Q045
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Importing data from a file applies the same validation and type-coercion behaviour as manual entry,
  so import cannot introduce a value manual entry would have rejected or handled differently.
WHY_IT_MATTERS: >
  An import path with weaker validation is a controls gap that lets bad data into the sheet at scale.
DISCONFIRMING_OBSERVATION: >
  An imported file's value passes through unvalidated or differently typed compared to what typing
  the same value manually would produce.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Attempt to import a value that manual entry would reject or coerce differently, and compare
  outcomes.
```

## G15-SPREADSHEET-Q046

```yaml
QID: G15-SPREADSHEET-Q046
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A collaborator's cursor or selection indicator during real-time co-editing does not itself
  constitute or imply an edit; observing where someone is looking never changes stored cell content.
WHY_IT_MATTERS: >
  A presence indicator that could alter data would conflate a purely informational signal with a
  write operation, an unexpected and dangerous coupling.
DISCONFIRMING_OBSERVATION: >
  Another collaborator's presence indicator or selection alone causes a change to stored cell values.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Have one collaborator move their selection across cells while another monitors for any change to
  stored values with no explicit edit made.
```

## G15-SPREADSHEET-Q047

```yaml
QID: G15-SPREADSHEET-Q047
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A formula referencing a cell in a sheet the current viewer lacks permission to open computes and
  displays only what the viewer's own permission on the result cell allows, without exposing the
  restricted sheet's underlying data through an error message or tooltip.
WHY_IT_MATTERS: >
  An error message that leaks restricted data defeats the sheet-level permission it was meant to
  enforce.
DISCONFIRMING_OBSERVATION: >
  An error or tooltip on a formula referencing a restricted sheet reveals the underlying restricted
  data or structure to a viewer without access to that sheet.
EXPECTED_SURFACE: S4,S3
PRECONDITIONS: >
  Build a formula referencing a restricted sheet, then view it as a user without access to that
  sheet and inspect any error or tooltip content.
```

## G15-SPREADSHEET-Q048

```yaml
QID: G15-SPREADSHEET-Q048
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Scheduled or automatic save preserves the most recent user-confirmed edit even when a session
  interruption falls in the narrow window right after a keystroke and before the next autosave tick.
WHY_IT_MATTERS: >
  Silently losing the very last edit before an interruption is the worst-case failure mode for an
  autosave feature, since the user has no reason to suspect it happened.
DISCONFIRMING_OBSERVATION: >
  A session interruption shortly after an edit results in that edit being lost despite autosave being
  enabled, with no recovery indication.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Make an edit and immediately interrupt the session before the next expected autosave tick, then
  reopen and check whether the edit persisted.
```

## G15-SPREADSHEET-Q049

```yaml
QID: G15-SPREADSHEET-Q049
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A workbook's activity log records who changed which cell and when at a granularity sufficient to
  distinguish concurrent editors, not a single aggregated entry that cannot attribute the change.
WHY_IT_MATTERS: >
  An activity log that cannot attribute a change to a specific person defeats its purpose for
  accountability and dispute resolution.
DISCONFIRMING_OBSERVATION: >
  The activity log for a workbook edited by multiple concurrent users cannot attribute a specific
  cell change to a specific user.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Have two users edit different cells of the same workbook concurrently, then inspect the activity
  log's attribution.
```

## G15-SPREADSHEET-Q050

```yaml
QID: G15-SPREADSHEET-Q050
MODULE: spreadsheet
TYPE: MODULE
AUTHOR: P15-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A workbook shared with a guest or external user restricts that user's ability to further re-share
  it beyond what the owner explicitly allowed.
WHY_IT_MATTERS: >
  Unrestrained re-sharing turns a single deliberate sharing decision into an uncontrolled distribution
  of the underlying data.
DISCONFIRMING_OBSERVATION: >
  A guest recipient of a shared workbook is able to extend access to additional people beyond the
  sharing scope the owner configured.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Share a workbook with a guest with re-sharing not permitted, then attempt to re-share as that
  guest.
```
