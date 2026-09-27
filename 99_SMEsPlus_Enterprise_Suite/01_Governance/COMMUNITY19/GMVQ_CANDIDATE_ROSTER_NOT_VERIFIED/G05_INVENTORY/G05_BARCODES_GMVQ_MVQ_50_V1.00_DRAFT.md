# G05 INVENTORY — MODULE-SPECIFIC QUESTION BANK (MVQ)

- Document ID: G05-BARCODES-GMVQ-MVQ-V1.00-DRAFT
- Group: G05 INVENTORY
- Module Metadata: barcodes
- Wave: W2
- Author Cell: P06
- Review Cell: PENDING
- Status: DRAFT / AUTHORING COMPLETE / NOT FROZEN
- actual_mvq_count: 50
- Purpose: Module-specific research questions (MVQ) for the blind two-lane study. Lane A
  reads reference source and answers independently; Lane B observes a running system only.
  The Reconciler joins answers on MODULE + QID. This bank covers scanning as an alternative
  input path to the normal form — not the meaning of what is scanned (see the sibling bank
  for structured-symbol decoding).
- Control: Authored under GMVQ_AUTHORING_STANDARD_V1.00.md and GMVQ_BRIDGE_MODULE_RULE_V1.00.md.
  Clean Room: no vendor or reference source tree was consulted in authoring this bank; content
  draws on generic ERP/WMS domain knowledge and industry-standard warehouse-operations concepts
  only. Not approved. Not frozen. Not verified. Not MASTER-ready. DRAFT content only. This
  document does not authorize any merge, release, or STATE/gate closure.

## A/B boundary note
This bank is scoped strictly to the scan EVENT as an input path: focus, timing, commit
semantics, attribution, and how a scan interacts with reservation/availability and the audit
trail. Any question about interpreting the CONTENTS of a structured symbol into distinct
business facts (item, lot, quantity, date parsed out of one string) belongs to the sibling
bank `barcodes_gs1_nomenclature` and is intentionally excluded here to avoid the near-duplicate
defect described in GMVQ_BRIDGE_MODULE_RULE_V1.00.md.

---
```yaml
QID: G05-BARCODES-Q001
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scanned action can move a record past a state boundary that requires an explicit
  confirmation step when the same transition is performed through the standard form.
WHY_IT_MATTERS: >
  Bypassing a required confirmation lets an irreversible operation complete without the
  human check the process was designed to require.
DISCONFIRMING_OBSERVATION: >
  An operator scans a step-completing identifier and the operation completes with no
  confirmation prompt, where the identical transition through the form always requires one.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Identify a workflow step whose form path shows a confirmation dialog before committing.
  Reach the equivalent state using only a scan and observe whether the same checkpoint appears.
```

```yaml
QID: G05-BARCODES-Q002
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A permission check that gates a field-level edit on the form is enforced identically when
  the equivalent change is triggered by a scan.
WHY_IT_MATTERS: >
  A scan path that bypasses role or permission enforcement breaks a security invariant that
  is assumed to hold across every input surface, not only the form.
DISCONFIRMING_OBSERVATION: >
  A user lacking edit permission on the form successfully changes the underlying value by
  scanning, with no permission error raised.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Set up a user role without edit rights on a given field/step. Attempt the change via the
  form (expect denial), then attempt the same change via scan.
```

```yaml
QID: G05-BARCODES-Q003
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A scan cannot advance a workflow past a step that has an unmet approval requirement.
WHY_IT_MATTERS: >
  An approval gate that a scan can silently skip removes the control the gate exists to
  provide, with no compensating record.
DISCONFIRMING_OBSERVATION: >
  The workflow state advances past an unapproved step purely from a scan event, with no
  approval record created and no block encountered.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Configure a step that requires approval before proceeding. Attempt to reach the next state
  by scan alone, without satisfying the approval.
```

```yaml
QID: G05-BARCODES-Q004
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Validation rules that check quantity, location, or product compatibility on the form are
  evaluated identically when the same data arrives via scan.
WHY_IT_MATTERS: >
  Inconsistent validation between input surfaces creates a path for invalid combinations to
  enter the record undetected.
DISCONFIRMING_OBSERVATION: >
  A combination the form rejects (e.g., an incompatible location/product pairing) is silently
  accepted when the identical data is supplied by scan.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Identify a combination the form is known to reject. Reproduce the identical combination
  through a scan sequence and compare the outcome.
```

```yaml
QID: G05-BARCODES-Q005
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A scan-triggered state change produces the same required downstream effects (triggering a
  dependent capability) as the equivalent form action.
WHY_IT_MATTERS: >
  A downstream effect that silently fails to fire from a scan creates a gap between what
  looks complete and what actually happened.
DISCONFIRMING_OBSERVATION: >
  A scan completes the visible step but a dependent downstream effect that always fires from
  the form does not fire, with no error surfaced.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Identify a step whose form completion always triggers a known downstream effect. Complete
  the same step by scan and check whether the effect occurred.
```

```yaml
QID: G05-BARCODES-Q006
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The system displays an unambiguous indicator of which document is currently the scan target
  before it accepts a content-changing scan.
WHY_IT_MATTERS: >
  Without a clear active-target indicator, a scan intended for one document can silently
  modify another.
DISCONFIRMING_OBSERVATION: >
  Two documents are open in the same session and a scan is applied to one that carries no
  visible active-target indicator, with no warning shown.
EXPECTED_SURFACE: S5
PRECONDITIONS: >
  Open two scannable documents in the same session. Observe whether the interface marks
  which one is live before a scan is submitted.
```

```yaml
QID: G05-BARCODES-Q007
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Switching between two open documents in the same session does not silently retarget a scan
  queued or triggered before the switch.
WHY_IT_MATTERS: >
  A retargeted scan can apply data to the wrong record without the operator ever choosing to.
DISCONFIRMING_OBSERVATION: >
  An operator switches views and a scan intended for the first document is applied against
  the second, with no prompt confirming the change of target.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Begin a scan-driven operation on document A, switch focus to document B mid-operation, and
  observe which document receives the next scan.
```

```yaml
QID: G05-BARCODES-Q008
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An ambiguous scan target — no single document unambiguously active — causes the scan to be
  rejected rather than silently applied to a default.
WHY_IT_MATTERS: >
  A silent default under ambiguity is a plausible route to data being recorded against the
  wrong document with no operator awareness.
DISCONFIRMING_OBSERVATION: >
  With no document explicitly active, a scan is silently applied to whichever document was
  most recently touched, with no ambiguity notice.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Reach a session state where no document is clearly the active scan target, then submit a
  scan and observe what receives it.
```

```yaml
QID: G05-BARCODES-Q009
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A scan misapplied to the wrong document is recoverable through a defined correction path
  that does not require the document to already be posted or closed.
WHY_IT_MATTERS: >
  Without a correction path, a focus-related mistake becomes a permanent data-quality defect.
DISCONFIRMING_OBSERVATION: >
  Once a scan has been misapplied to the wrong open document, no path exists to correct it
  short of an irreversible workaround (e.g., a full reversal of an already-posted document).
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deliberately misapply a scan to the wrong of two open documents, then attempt to correct it
  through ordinary means.
```

```yaml
QID: G05-BARCODES-Q010
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A multi-tab or multi-window session cannot let a scan fire against a document that the
  current view has already navigated away from.
WHY_IT_MATTERS: >
  A scan applied to a document no longer on screen is invisible to the operator at the moment
  it happens, delaying discovery of any error.
DISCONFIRMING_OBSERVATION: >
  A scan targets a document that the active view already navigated away from, and the change
  is only discovered later by returning to that document.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Open a document, navigate away without closing the underlying session state, then submit a
  scan and check which document is affected.
```
```yaml
QID: G05-BARCODES-Q011
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Scanning the same identifier twice in immediate succession against the same target
  increments the recorded quantity rather than creating a duplicate line.
WHY_IT_MATTERS: >
  Whether a repeat scan increments or duplicates changes the recorded quantity and the
  shape of the record; getting it wrong either overstates or fragments the entry.
DISCONFIRMING_OBSERVATION: >
  Two identical scans in a row against the same target produce two separate lines for the
  same item instead of one line with an increased quantity.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Scan one identifier once, note the resulting line, then scan the identical identifier again
  against the same target and compare the result.
```

```yaml
QID: G05-BARCODES-Q012
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a repeat scan increments, replaces, or errors is a configurable behaviour at the
  workflow/step level, not identical everywhere by hardcoded default.
WHY_IT_MATTERS: >
  A one-size-fits-all repeat-scan behaviour may be wrong for at least one of the steps that
  use scanning, and a lack of configurability forces a workaround elsewhere.
DISCONFIRMING_OBSERVATION: >
  The same repeat-scan behaviour appears identically across two different workflow steps with
  no configuration point that could differentiate them.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare repeat-scan behaviour on two different steps that scanning supports, and check for
  any configuration setting governing the behaviour on each.
```

```yaml
QID: G05-BARCODES-Q013
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A repeat scan that would push a running count past a defined limit is rejected with a
  distinguishable error, not silently capped or silently accepted.
WHY_IT_MATTERS: >
  A silently capped or silently accepted over-limit scan hides a discrepancy between what was
  physically scanned and what was recorded.
DISCONFIRMING_OBSERVATION: >
  Repeat scans past a defined limit are accepted with the excess silently dropped, or accepted
  in full with no error, and no operator-visible signal either way.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Identify a step with a defined scan-count limit and drive repeat scans past it, observing
  what is recorded and what feedback, if any, appears.
```

```yaml
QID: G05-BARCODES-Q014
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An accidental double-trigger producing two nearly-simultaneous identical scan events is
  deduplicated within a short window rather than recorded as two operator actions.
WHY_IT_MATTERS: >
  Hardware or reader double-fire is a known real-world occurrence; without deduplication it
  silently doubles recorded quantities.
DISCONFIRMING_OBSERVATION: >
  Two scan events arriving within a very short interval are both recorded as separate,
  independent operator actions.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Simulate two rapid, near-simultaneous identical scan events against the same target and
  inspect how many distinct actions are recorded.
```

```yaml
QID: G05-BARCODES-Q015
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The outcome of a repeat scan (increment, replace, or error) for a given step is consistent
  across sessions, not dependent on hidden session state.
WHY_IT_MATTERS: >
  An unpredictable repeat-scan outcome erodes operator trust in what a scan will do and makes
  the behaviour untestable.
DISCONFIRMING_OBSERVATION: >
  The same identifier, scanned twice against the same kind of target, produces different
  outcomes on different occasions with no observable state difference explaining it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Repeat the identical repeat-scan scenario in two separate sessions under otherwise identical
  conditions and compare outcomes.
```

```yaml
QID: G05-BARCODES-Q016
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a scanned identifier resolves to more than one candidate record, the system requires
  explicit disambiguation rather than silently selecting one.
WHY_IT_MATTERS: >
  A silent pick among ambiguous candidates can commit a transaction against the wrong record
  entirely, with the operator unaware a choice was even made.
DISCONFIRMING_OBSERVATION: >
  An identifier known to match two records is scanned and one is selected automatically with
  no visible choice ever offered to the operator.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create two records that share the same scannable identifier (by configuration or data
  overlap) and scan that identifier.
```

```yaml
QID: G05-BARCODES-Q017
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A disambiguation choice, once made, is remembered for the remainder of a single continuous
  operation rather than re-asked on every subsequent scan of the same identifier.
WHY_IT_MATTERS: >
  Re-prompting for the same disambiguation repeatedly slows operators and creates pressure to
  pick carelessly just to move past the prompt.
DISCONFIRMING_OBSERVATION: >
  The operator is asked to disambiguate the same conflicting identifier repeatedly within a
  single continuous operation.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger a disambiguation prompt, make a choice, then scan the same ambiguous identifier
  again within the same operation.
```

```yaml
QID: G05-BARCODES-Q018
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A scope boundary limiting which records are eligible candidates is applied before offering
  disambiguation, so a record outside the current operation's scope is never offered.
WHY_IT_MATTERS: >
  Offering an out-of-scope record as a candidate creates a path to acting on data the current
  operation should never be able to reach.
DISCONFIRMING_OBSERVATION: >
  A record that should be excluded from the current operation's scope appears as a selectable
  match during disambiguation.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Set up an identifier collision where one of the colliding records sits outside the current
  operation's scope, then scan the identifier.
```

```yaml
QID: G05-BARCODES-Q019
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An identifier that was ambiguous at scan time is logged distinctly from one that matched a
  single record cleanly, even once resolved.
WHY_IT_MATTERS: >
  Without a distinct trace, a data-quality problem (duplicate identifiers) becomes invisible
  once resolved once.
DISCONFIRMING_OBSERVATION: >
  No observable trace exists that a given scan was ever ambiguous, once resolution has
  occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger and resolve a disambiguation event, then inspect the record and any log for a trace
  that ambiguity occurred.
```

```yaml
QID: G05-BARCODES-Q020
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two records sharing an identifier due to a data-quality error, rather than by design, surface
  as an actionable signal rather than being silently absorbed by a disambiguation pick.
WHY_IT_MATTERS: >
  An unreported duplicate-identifier condition can recur silently on every future scan of that
  identifier.
DISCONFIRMING_OBSERVATION: >
  The duplicate-identifier condition produces no signal anywhere an operator or supervisor
  could see it, before or after resolution.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Introduce an unintentional identifier collision between two records and scan it, then check
  for any surfaced signal beyond the immediate pick.
```
```yaml
QID: G05-BARCODES-Q021
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A scanned line is held in an uncommitted buffer until an explicit save or validate step,
  rather than being written to the permanent record on every individual scan.
WHY_IT_MATTERS: >
  Whether scans buffer or commit immediately determines what an interruption leaves behind and
  how a mistake mid-sequence can be corrected.
DISCONFIRMING_OBSERVATION: >
  Each individual scan is immediately and irreversibly committed to the permanent record with
  no intermediate review state before a save step.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Perform a sequence of scans without triggering the final save/validate action, then inspect
  whether the underlying record already reflects them.
```

```yaml
QID: G05-BARCODES-Q022
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An interrupted session (closed or lost before saving) leaves no partial or orphaned record
  behind — buffered scans are discarded cleanly.
WHY_IT_MATTERS: >
  An orphaned partial record from an interrupted session is a data-integrity defect that may
  go unnoticed until it affects a later operation.
DISCONFIRMING_OBSERVATION: >
  After a session is interrupted before saving, a partial or orphaned record is found in the
  persisted state.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Begin a scan sequence, interrupt the session before any save/validate step, then inspect the
  persisted state for remnants.
```

```yaml
QID: G05-BARCODES-Q023
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If scans commit immediately rather than buffering, an early scan in a sequence can be
  reversed independently without first reversing every scan recorded after it.
WHY_IT_MATTERS: >
  Requiring a full unwind to fix one early mistake makes correction disproportionately costly
  and encourages workarounds that skip proper reversal.
DISCONFIRMING_OBSERVATION: >
  Reversing an early scan in an immediately-committed sequence requires first reversing every
  later scan in that sequence.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record a sequence of immediately-committing scans, then attempt to reverse only the first
  one without touching the rest.
```

```yaml
QID: G05-BARCODES-Q024
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The buffered-versus-immediate commit behaviour for a given step is the same regardless of
  which device or client submitted the scan.
WHY_IT_MATTERS: >
  Device-dependent commit semantics for the identical step would make the record's integrity
  guarantees dependent on which hardware happened to be used.
DISCONFIRMING_OBSERVATION: >
  The same step behaves as buffered on one client and as immediate on another with no
  configuration difference between them.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Perform the same scan step from two different client types or devices and compare commit
  timing.
```

```yaml
QID: G05-BARCODES-Q025
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A session interrupted mid-buffer can be resumed from where it left off, rather than forcing
  the operator to restart the entire sequence.
WHY_IT_MATTERS: >
  Forcing a full restart after every interruption increases operator error and re-work,
  especially for long scan sequences.
DISCONFIRMING_OBSERVATION: >
  Any interruption of a buffered scan sequence forces the operator to re-scan everything
  already captured in that session.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Begin a long buffered scan sequence, interrupt it, then reopen the same operation and check
  whether prior scans are still present.
```

```yaml
QID: G05-BARCODES-Q026
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A queued (offline) scan is re-validated against current state at the moment it is applied,
  not only at the moment it was originally captured.
WHY_IT_MATTERS: >
  State can change materially between capture and application; applying against stale
  assumptions can silently produce an inconsistent result.
DISCONFIRMING_OBSERVATION: >
  A queued scan applies successfully even though the state it depended on had changed in the
  meantime, producing a result inconsistent with current reality.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Capture a scan offline against a given state, change that state before reconnecting, then
  apply the queued scan and observe the result.
```

```yaml
QID: G05-BARCODES-Q027
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A queued scan that fails re-validation on application is surfaced to a human for resolution,
  rather than being silently dropped or silently forced through.
WHY_IT_MATTERS: >
  A silently dropped or silently forced queued scan means physical work the operator believes
  is recorded may not be, or may be recorded incorrectly, with nobody aware.
DISCONFIRMING_OBSERVATION: >
  A queued scan that no longer matches current state at application time disappears with no
  record and no notification to anyone.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Create conditions where a queued scan will fail re-validation on application, then check for
  any notification or record of the failure.
```

```yaml
QID: G05-BARCODES-Q028
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Queued scans from the same offline session are applied in the order they were captured, not
  reordered on application.
WHY_IT_MATTERS: >
  Reordering can change the outcome of a sequence of scans that depend on each other's effects
  (e.g., a location move followed by a pick from that location).
DISCONFIRMING_OBSERVATION: >
  Two queued scans from the same offline session apply out of capture sequence, producing a
  different outcome than applying them in order would have.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Capture two order-dependent scans offline in a known sequence, reconnect, and verify the
  application order.
```

```yaml
QID: G05-BARCODES-Q029
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An offline scan retains its true capture time as distinct from its later application time,
  for any rule that depends on when the physical action happened.
WHY_IT_MATTERS: >
  Using application time in place of capture time for a time-sensitive rule can misrepresent
  when the physical event actually occurred.
DISCONFIRMING_OBSERVATION: >
  A time-sensitive rule evaluates a queued scan against the time it was applied rather than
  the time it was originally captured.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Capture a scan offline at one time, apply it much later, and check which timestamp a
  time-sensitive rule uses.
```

```yaml
QID: G05-BARCODES-Q030
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Conflicting queued scans from two different devices covering the same target are resolved by
  an explicit, visible rule rather than an unannounced last-write-wins.
WHY_IT_MATTERS: >
  An unannounced overwrite silently discards one operator's recorded work with no way to know
  it happened.
DISCONFIRMING_OBSERVATION: >
  Two queued scans from different devices conflict on application and one is silently
  overwritten with no trace of the discarded scan.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Queue conflicting offline scans from two devices against the same target, reconnect both,
  and observe how the conflict is resolved and recorded.
```
```yaml
QID: G05-BARCODES-Q031
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Every scanned action records which operator or device performed it, at the same fidelity as
  the equivalent typed action.
WHY_IT_MATTERS: >
  Losing attribution on the scan path creates a gap in accountability that does not exist on
  the form path.
DISCONFIRMING_OBSERVATION: >
  A scanned action is stored with no identifiable operator or device, while the equivalent
  typed action always records one.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Perform the same logical action once via scan and once via the form, under known operator
  identity, and compare what is recorded.
```

```yaml
QID: G05-BARCODES-Q032
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A shared or generic scanning device does not attribute an action to whichever user session
  happens to be open when the process requires individual accountability, without an explicit
  operator-identification step.
WHY_IT_MATTERS: >
  Misattribution on a shared device defeats accountability for exactly the actions that most
  need it.
DISCONFIRMING_OBSERVATION: >
  A shift-shared scanning device attributes an action to a user who was not the one physically
  performing it, with no operator-identification step ever occurring.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Use a shared device logged in under one identity while a different person physically
  performs the scan, and check the recorded attribution.
```

```yaml
QID: G05-BARCODES-Q033
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Switching the logged-in operator mid-session does not retroactively reattribute scans that
  were already recorded under the previous operator.
WHY_IT_MATTERS: >
  Retroactive reattribution would corrupt the historical accountability record for actions
  that already occurred.
DISCONFIRMING_OBSERVATION: >
  Switching operators changes the attribution shown for scans that were recorded before the
  switch took place.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Record scans under one operator identity, switch to a different operator mid-session, and
  re-check the attribution of the earlier scans.
```

```yaml
QID: G05-BARCODES-Q034
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Operator attribution for a historical scan is preserved even after that operator's account
  is later deactivated.
WHY_IT_MATTERS: >
  Losing attribution on account deactivation would erase accountability precisely for
  personnel who have left, when historical review matters most.
DISCONFIRMING_OBSERVATION: >
  Deactivating an operator's account causes their historical scanned actions to appear
  unattributed or reattributed to someone else.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Record scans under a given operator, deactivate that operator's account, and re-check the
  historical attribution.
```

```yaml
QID: G05-BARCODES-Q035
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A supervisor override performed via scan (authorizing an exception) records the identity of
  the overriding operator distinctly from the original operator on the record.
WHY_IT_MATTERS: >
  Merging the override identity into the original operator's identity hides who actually
  authorized an exception.
DISCONFIRMING_OBSERVATION: >
  An override action recorded via scan shows only the original operator, with no trace of who
  authorized the exception.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Trigger an exception requiring supervisor override, perform the override via scan, and
  inspect the record for both identities.
```

```yaml
QID: G05-BARCODES-Q036
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scan cannot reassign a unit that is already reserved for a different demand to a new
  purpose without an explicit override step.
WHY_IT_MATTERS: >
  Silently reassigning reserved stock breaks the commitment the reservation represents to
  whoever it was made for.
DISCONFIRMING_OBSERVATION: >
  A scanned action consumes a unit already reserved for a different demand, with no override
  step and no warning shown.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Reserve a unit for one demand, then attempt to consume the same unit for a different demand
  purely by scanning it.
```

```yaml
QID: G05-BARCODES-Q037
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Forcing availability via scan (bypassing an out-of-stock or reservation block) leaves a
  distinguishable trace that an ordinary, unforced scan does not.
WHY_IT_MATTERS: >
  Without a distinguishable trace, a forced exception looks identical to normal operation in
  later review, hiding how often the control was bypassed.
DISCONFIRMING_OBSERVATION: >
  A forced-availability scan is indistinguishable in the stored record from an ordinary scan
  against genuinely available stock.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Force availability through a scan against an out-of-stock or reserved unit, then compare the
  resulting record to an ordinary successful scan.
```

```yaml
QID: G05-BARCODES-Q038
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Forcing availability through a scan requires a permission level higher than the one needed
  to perform an ordinary scan.
WHY_IT_MATTERS: >
  If any operator able to scan can also force availability, the override loses its function as
  a control.
DISCONFIRMING_OBSERVATION: >
  An operator holding only ordinary scan permission is able to force availability with no
  additional permission check encountered.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Attempt to force availability using an account that holds only baseline scanning permission.
```

```yaml
QID: G05-BARCODES-Q039
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Forcing availability through a scan does not itself resolve the reservation it bypassed —
  that reservation still requires its own separate resolution.
WHY_IT_MATTERS: >
  If forcing availability silently closes out the bypassed reservation, the original demand
  loses visibility into the fact its claim was never actually honoured.
DISCONFIRMING_OBSERVATION: >
  Forcing availability silently cancels or marks fulfilled the reservation it bypassed, with no
  separate record distinguishing that outcome.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Force availability past an existing reservation, then check the state and history of that
  original reservation afterward.
```

```yaml
QID: G05-BARCODES-Q040
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A reservation that a scan is about to override is checked at the moment of the scan, not
  against a stale snapshot taken earlier in the session.
WHY_IT_MATTERS: >
  Acting on a stale snapshot can cause an override to fire against a reservation that had
  already been legitimately released, needlessly forcing an exception that was not needed.
DISCONFIRMING_OBSERVATION: >
  A scan overrides a reservation that had already been released before the scan occurred,
  because the check used information from earlier in the session.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Load a session state where a reservation exists, release that reservation through another
  channel, then perform the scan without refreshing the session view first.
```
```yaml
QID: G05-BARCODES-Q041
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scan asserting a quantity greater than what is currently available triggers a
  distinguishable warning or block rather than succeeding exactly as an in-range scan would.
WHY_IT_MATTERS: >
  Treating an over-quantity scan identically to a normal one hides a discrepancy between the
  physical count and the recorded count.
DISCONFIRMING_OBSERVATION: >
  A scan for a quantity larger than what is available is accepted with no different treatment
  than a scan within the available quantity.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to scan a quantity that exceeds what the system currently shows as available for the
  target, and observe the response.
```

```yaml
QID: G05-BARCODES-Q042
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether an over-quantity scan is hard-blocked or only warned is governed by a configurable
  policy at the step or role level, not a single hardcoded behaviour everywhere.
WHY_IT_MATTERS: >
  A single hardcoded policy may be too strict for some operations and too permissive for
  others; configurability lets the control match the actual risk.
DISCONFIRMING_OBSERVATION: >
  The same over-quantity condition is always hard-blocked, or always merely warned, regardless
  of any policy setting for step or role.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare over-quantity handling for two different steps or roles and look for a configuration
  point that distinguishes them.
```

```yaml
QID: G05-BARCODES-Q043
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An over-quantity scan that is allowed through with a warning is recorded as an exception,
  distinguishable from an ordinary in-range scan.
WHY_IT_MATTERS: >
  Without a distinguishing record, later review cannot tell which scans required an exception
  to be allowed through.
DISCONFIRMING_OBSERVATION: >
  An over-quantity scan that was allowed produces a record indistinguishable from a normal,
  in-range scan.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Allow an over-quantity scan through its warning, then compare its stored record to an
  ordinary in-range scan's record.
```

```yaml
QID: G05-BARCODES-Q044
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Cumulative over-scanning across several partial scans against the same target is evaluated
  against the original total available, not only against the remaining balance at each step.
WHY_IT_MATTERS: >
  Checking only the remaining balance at each step lets a series of individually-small
  over-scans together exceed the true original total without ever triggering a warning.
DISCONFIRMING_OBSERVATION: >
  Several small over-scans, each individually within the remaining balance shown at the time,
  together exceed the original total with no warning ever raised.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Perform a sequence of small partial scans against one target that, in total, exceed the
  original available quantity, checking after each one.
```

```yaml
QID: G05-BARCODES-Q045
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A scan asserting a zero or negative quantity is rejected rather than silently accepted as a
  no-op or as a valid entry.
WHY_IT_MATTERS: >
  A silently accepted zero or negative quantity can corrupt totals or mask a data-entry problem
  with the scanning device or the encoded value.
DISCONFIRMING_OBSERVATION: >
  A scan asserting a zero or negative quantity is accepted and recorded as if it were an
  ordinary positive entry.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit a scan-derived quantity of zero and, separately, a negative value, and observe the
  system's response to each.
```

```yaml
QID: G05-BARCODES-Q046
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The audit trail records the input method (scan versus manual entry) as a distinguishable
  attribute of an action, not only the resulting value.
WHY_IT_MATTERS: >
  Without recording input method, an investigation into a scanning-specific defect cannot
  distinguish affected records from unaffected ones after the fact.
DISCONFIRMING_OBSERVATION: >
  The audit trail entry for a scanned action is structurally identical to one for a typed
  action, with no way to tell them apart.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Perform equivalent actions once by scan and once by manual entry, then compare the audit
  trail entries for each.
```

```yaml
QID: G05-BARCODES-Q047
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A scanned action later corrected by a manual edit preserves the original scanned value in the
  audit trail, not only the final corrected value.
WHY_IT_MATTERS: >
  Losing the original value on correction removes the ability to tell, after the fact, how
  large or how frequent scan corrections actually are.
DISCONFIRMING_OBSERVATION: >
  After a manual correction, the audit trail shows only the corrected value with no record that
  the original entry came from a scan or what that original value was.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a value via scan, correct it manually afterward, and inspect the audit trail for the
  original scanned value.
```

```yaml
QID: G05-BARCODES-Q048
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The device or terminal identity used for a scan is retained in the audit trail wherever the
  process treats device identity as material to the operation.
WHY_IT_MATTERS: >
  Where device identity matters (e.g., a fixed warehouse terminal versus a handheld reader),
  losing it removes information needed to investigate a device-specific problem.
DISCONFIRMING_OBSERVATION: >
  Two scans performed from clearly different devices produce audit trail entries with no
  device distinction, in a process where that distinction is meant to be material.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Perform the same scanned action from two identifiably different devices and compare what
  device information, if any, is retained.
```

```yaml
QID: G05-BARCODES-Q049
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A rapid sequence of distinct scans produces one audit trail entry per discrete action, not a
  single aggregated entry that loses the individual sequence.
WHY_IT_MATTERS: >
  Collapsing a sequence into one aggregated entry prevents reconstructing exactly what was
  scanned, in what order, and when.
DISCONFIRMING_OBSERVATION: >
  A sequence of distinct scans collapses into a single audit trail entry that cannot be broken
  back out into the individual actions.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Perform a rapid sequence of several distinct scans and inspect the audit trail for one entry
  per action versus a single aggregate.
```

```yaml
QID: G05-BARCODES-Q050
MODULE: barcodes
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An attempted scan that fails validation still leaves a trace that the attempt occurred,
  distinct from a scan that succeeded.
WHY_IT_MATTERS: >
  Without a trace of failed attempts, repeated failed scans (which may indicate a data-quality
  or hardware problem) are invisible to later review.
DISCONFIRMING_OBSERVATION: >
  A failed scan attempt leaves no trace at all, indistinguishable from the attempt never having
  happened.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Deliberately trigger a scan that fails validation (e.g., an unrecognised or invalid
  identifier) and check for any resulting trace.
```
