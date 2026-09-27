# SMEsPlus ENTERPRISE SUITE
## GMVQ — G04 ACCOUNT_BASE / account_update_tax_tags Module MVQ Bank

**Document ID:** GMVQ-G04-ACCOUNT_UPDATE_TAX_TAGS-MVQ48-V1.00
**Group:** G04 ACCOUNT_BASE (Wave W1)
**Module Metadata:** `account_update_tax_tags`
**Wave:** W1
**Author Cell:** TEAM 22 (GMVQ Question Factory — Internal Production Team 22, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for a maintenance capability that re-applies
reporting classifications to tax-related lines, including historical ones. Per the Group G04 brief
this is the highest-risk group in the programme: the capability rewrites already-posted history,
so the material ground is what the pass may change, what it must never change, how a reviewer
proves after the fact that only the classification moved, and how the pass itself is authorized,
scoped, and reversed.

Question text is source-neutral. It does not name the module, any vendor or product, or any
technical identifier (field, model, method, XML ID, API path). Generic business and behavioural
language is used throughout — "reporting tag" and "reporting classification" refer to the business
concept, never to an implementation identifier.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because each tests a distinct material hypothesis, spread across
  the required dimensions (business rule, state transition, configuration dependency, role and
  permission, exception path, cancellation, reversal, negative case, cross-module dependency,
  auditability, tenant/company boundary, concurrency and ordering, runtime reachability).
- Where a question depends on a specific Thai statutory rule that cannot be stated with confidence,
  it is written in behavioural terms and carries `LEGAL_TAX_REVIEW_REQUIRED: YES`. No rate, form
  number, or filing deadline is asserted anywhere in this bank.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q001

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q001
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A pass that re-applies reporting classifications to tax-related lines changes only the
  classification field on each line and never the amount, the account, the posting period, or the
  posted/unposted state.
WHY_IT_MATTERS: >
  If the pass can silently touch any of these, a tag-correction exercise becomes an undisclosed
  restatement of posted history.
DISCONFIRMING_OBSERVATION: >
  After the pass runs, any line shows a changed amount, account, posting period, or posted/unposted
  state where only the reporting classification was expected to change.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Capture a full field-level snapshot of a sample of tax-relevant lines before running the pass in
  a controlled scope, run it, and compare every field, not only the classification field.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q002

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q002
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The pass never alters a historical line's document date or tax point date as a side effect of
  reclassifying it.
WHY_IT_MATTERS: >
  The tax point date drives which reporting period a transaction belongs to; an incidental shift
  would move an obligation between periods without anyone deciding to do so.
DISCONFIRMING_OBSERVATION: >
  A line's document date or tax point date differs after the pass ran compared to before.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Using the same before/after snapshot approach as Q001, compare the date fields specifically for
  every line in scope.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q003

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q003
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Running the pass against a period that is locked or closed is either blocked outright or requires
  an explicit override that leaves its own distinct trace, and never proceeds exactly as it would
  for an open period.
WHY_IT_MATTERS: >
  A lock or close date exists specifically to freeze a period; an undifferentiated bypass defeats
  the control's purpose.
DISCONFIRMING_OBSERVATION: >
  Lines dated within a locked or closed period are rewritten with no override record that
  distinguishes that run from an ordinary run against an open period.
EXPECTED_SURFACE: S2,S4,S6,S7
PRECONDITIONS: >
  Lock or close a period containing tax-relevant historical lines, then invoke the pass with a
  scope that includes that period.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q004

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q004
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Reaching into a fiscal year that has been formally closed for reporting purposes requires a
  distinct, higher-level authorization than the ordinary run permission, not the same grant used
  for an open year.
WHY_IT_MATTERS: >
  A formally closed year is a stronger boundary than a lock date; treating it the same as an open
  year removes a control the business relies on.
DISCONFIRMING_OBSERVATION: >
  A formally closed year's lines are changed under the same authorization level used for an open
  year, with no additional gate.
EXPECTED_SURFACE: S2,S4,S7
PRECONDITIONS: >
  Attempt the pass against a formally closed fiscal year using an account that holds only the
  ordinary run permission.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q005

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q005
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the pass is interrupted partway through a batch, the lines already processed and the lines not
  yet reached remain distinguishable afterward.
WHY_IT_MATTERS: >
  An unrecoverable interruption that leaves no way to tell what was and was not converted turns a
  routine failure into a data-integrity incident.
DISCONFIRMING_OBSERVATION: >
  After a forced interruption, there is no reliable way to determine which lines were converted and
  which were not yet reached.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Start the pass over a large batch and force termination partway through, then inspect the
  resulting state.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q006

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q006
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A batch left half-converted by an interrupted run does not leave the tax reporting basis
  internally inconsistent in a way that would double-count or omit an amount from a report drawn
  immediately afterward.
WHY_IT_MATTERS: >
  A report generated on mixed old/new classifications can misstate a filed obligation without
  anyone realizing the underlying pass never finished.
DISCONFIRMING_OBSERVATION: >
  A report generated immediately after an interrupted, unresumed run either omits or double-counts
  an amount because of mixed old and new classifications.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Force an interruption mid-batch, then generate the relevant report without resuming or rolling
  back the run.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q007

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q007
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Running the pass a second time over the same scope, with no intervening change, produces no
  further data changes.
WHY_IT_MATTERS: >
  Non-idempotent maintenance passes are unsafe to re-run after an uncertain first attempt, which is
  exactly when someone is most likely to re-run one.
DISCONFIRMING_OBSERVATION: >
  A second, immediate run over an unchanged scope alters a line that the first run already
  correctly classified.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Run the pass once and capture state, run it again unchanged, and compare the two states.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q008

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q008
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A run that changes nothing still records that it executed, so run history cannot be confused with
  "never run".
WHY_IT_MATTERS: >
  A reviewer relying on run history to establish that a check was performed needs a no-op run to be
  as visible as one that made changes.
DISCONFIRMING_OBSERVATION: >
  A no-op second run leaves no record in run history that it executed at all.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Run the pass twice over an unchanged scope and inspect the run history log for both executions.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q009

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q009
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Two invocations of the pass over overlapping scope running at the same time do not both write the
  same line, and neither invocation's outcome is silently lost.
WHY_IT_MATTERS: >
  Concurrent writes to posted tax history without ordering control can corrupt the reporting basis
  in a way that is hard to detect afterward.
DISCONFIRMING_OBSERVATION: >
  Overlapping concurrent runs leave a line in an inconsistent state, or one run's outcome
  disappears with no trace.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger two overlapping invocations against the same scope at nearly the same time.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q010

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q010
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An ordinary posting or correction transaction occurring on an in-scope line while the pass is
  mid-run is not silently overwritten, and the pass does not proceed against stale data without
  detecting the conflict.
WHY_IT_MATTERS: >
  A maintenance pass that ignores concurrent ordinary activity can lose a legitimate correction
  made by someone else at the same time.
DISCONFIRMING_OBSERVATION: >
  A concurrent ordinary transaction's effect is lost, or the pass completes against stale data with
  no conflict detected or reported.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Start the pass over a scope, and during its run, post or correct one of the in-scope lines
  through the ordinary transaction path.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q011

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q011
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A reviewer can prove, from a retained artefact rather than an operator's assertion, that a given
  run changed only the reporting classification and nothing else.
WHY_IT_MATTERS: >
  "Only the tag changed" is exactly the claim a reviewer must be able to verify independently on a
  pass that rewrites posted history, not simply accept.
DISCONFIRMING_OBSERVATION: >
  The only record of what a run changed is a summary count or a free-text note, with no line-level
  before/after artefact a reviewer can independently inspect.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Run the pass, then attempt to reconstruct a line-level before/after comparison using only what
  the system retains, without asking the operator.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q012

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q012
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The before/after evidence artefact produced by a run is immutable once produced.
WHY_IT_MATTERS: >
  An editable evidence record can be made to match a claim made after the fact, defeating its
  purpose as independent proof.
DISCONFIRMING_OBSERVATION: >
  The record of what a run changed can itself be edited or regenerated with different content after
  the run completed.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Attempt to alter a previously produced run evidence record through any available path.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q013

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q013
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Every individual line change is attributable to the specific run that made it, not merely to "a
  maintenance pass has run at some point".
WHY_IT_MATTERS: >
  Without per-run attribution, a dispute about a specific line's history cannot be resolved even
  though a general run log exists.
DISCONFIRMING_OBSERVATION: >
  A changed line cannot be traced to a specific run identifier, timestamp, and operator.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Run the pass twice with different scopes over time, then attempt to attribute a given line's
  current classification to one specific run.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q014

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q014
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The run record captures which mapping ruleset was applied to each line, since the ruleset used to
  decide the new classification can itself change over time.
WHY_IT_MATTERS: >
  Without this, a later reviewer cannot tell whether two lines with different outcomes were treated
  inconsistently or simply converted under different rules.
DISCONFIRMING_OBSERVATION: >
  Two lines converted under different mapping ruleset versions show identical run metadata with no
  way to tell which ruleset version applied to which.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Change the mapping configuration between two runs and compare the recorded metadata for lines
  touched by each.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q015

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q015
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Regenerating a report that was already filed for a period, after the pass has touched that
  period's lines, surfaces a flag when the regenerated figure differs from the filed one.
WHY_IT_MATTERS: >
  A silent divergence between a filed statutory report and what the system would now produce is a
  governance and compliance exposure that must not go unnoticed.
DISCONFIRMING_OBSERVATION: >
  Regenerating a previously filed report after the pass produces a different figure with no flag
  distinguishing it from the originally filed version.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  File or lock a report for a period, run the pass over that period's lines, then regenerate the
  same report and compare.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q016

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q016
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where the reporting classification scheme itself has changed version, the pass applies the scheme
  version that was in force for each line's own tax point date, rather than blanket-applying the
  current scheme to historical lines, unless retroactive application was explicitly authorized.
WHY_IT_MATTERS: >
  Applying today's scheme to yesterday's transactions without authorization is a retroactive change
  to a filed basis, not a correction.
DISCONFIRMING_OBSERVATION: >
  Historical lines governed by an earlier scheme version are reclassified under the current scheme
  with no explicit retroactive authorization recorded.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Introduce a new scheme version effective from a given date, then run the pass over lines dated
  both before and after that date.
LEGAL_TAX_REVIEW_REQUIRED: YES
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q017

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q017
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reprinting or re-exporting a historical document after its tax lines were reclassified indicates
  that the classification shown differs from what was shown at original issuance.
WHY_IT_MATTERS: >
  A reprinted document that silently shows today's classification as if it were the original
  misrepresents what was actually issued at the time.
DISCONFIRMING_OBSERVATION: >
  A reprinted historical document shows the new classification with no indication that it differs
  from the original.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Reclassify a line belonging to an already-issued historical document, then reprint or re-export
  that document.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q018

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q018
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelled or reversed transactions' tax-related lines are handled by an explicit, stated rule
  (included, excluded, or flagged), rather than by whatever the pass happens to do to any line it
  encounters.
WHY_IT_MATTERS: >
  Reclassifying a cancelled transaction's lines as if they were still live can misstate what
  actually remains in the reporting basis.
DISCONFIRMING_OBSERVATION: >
  A cancelled or reversed transaction's tax lines are reclassified with no distinct handling from
  an active, posted line.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Include a cancelled transaction and a reversed transaction's lines in the pass's scope and
  observe the treatment of each.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q019

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q019
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Draft, unposted tax-relevant lines are either excluded from the pass's scope, or if included, are
  distinguishable in the run record from posted historical lines.
WHY_IT_MATTERS: >
  A pass advertised as correcting historical (posted) data should not silently also touch data that
  has not yet been finalized, without saying so.
DISCONFIRMING_OBSERVATION: >
  Draft lines are reclassified indistinguishably from posted historical lines in the run record.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place both draft and posted lines in scope, run the pass, and inspect the run record for a
  distinction between the two.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q020

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q020
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A single invocation of the pass operates within one company's data scope unless a cross-company
  mode is an explicit, separately authorized option.
WHY_IT_MATTERS: >
  An invocation that reaches beyond its declared company scope breaks the tenant/company boundary
  the whole programme treats as a mandatory review dimension.
DISCONFIRMING_OBSERVATION: >
  An invocation scoped to one company alters lines belonging to a different company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Run the pass with an explicit single-company scope in a multi-company environment and inspect all
  companies' data afterward.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q021

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q021
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a cross-company invocation mode exists, its evidence breaks down which company's lines were
  changed under which authorization, rather than presenting the multi-company change as a single
  undifferentiated action.
WHY_IT_MATTERS: >
  Each company is a separate legal and audit boundary; a merged record defeats company-level
  accountability.
DISCONFIRMING_OBSERVATION: >
  A cross-company run's evidence does not break down the changes it made by company.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Invoke the cross-company mode where one exists and inspect the resulting evidence record.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q022

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q022
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A line's branch or sub-entity attribution survives reclassification unchanged.
WHY_IT_MATTERS: >
  Branch and head-office attribution drives which entity's report an amount lands in; an incidental
  reassignment would move that without a business decision to do so.
DISCONFIRMING_OBSERVATION: >
  A line's branch or sub-entity attribution differs after the pass compared to before.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Capture branch attribution before and after for a sample of lines spanning multiple branches.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q023

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q023
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a line has no unambiguous new classification available under the current mapping, the pass
  leaves it flagged for a manual decision rather than guessing or defaulting silently.
WHY_IT_MATTERS: >
  A silent default on an ambiguous line manufactures a false appearance of confident classification.
DISCONFIRMING_OBSERVATION: >
  An ambiguous line receives a classification with no flag distinguishing it from an unambiguous,
  confidently mapped line.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Construct a line whose attributes match more than one mapping rule and run the pass over it.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q024

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q024
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A line that already carries the correct target classification is left untouched — no write, no
  modification event — rather than rewritten with an identical value.
WHY_IT_MATTERS: >
  A phantom rewrite of an already-correct line pollutes the modification history and makes later
  before/after review noisier and less trustworthy.
DISCONFIRMING_OBSERVATION: >
  An already-correct line shows a new modification event after the pass despite no actual value
  change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Pre-set a line to the target classification, run the pass, and inspect its modification history.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q025

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q025
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A line's recorded exchange rate and converted amount, where the transaction is expressed in a
  currency other than the accounting currency, are not altered by a reclassification pass.
WHY_IT_MATTERS: >
  Currency conversion feeds the accounting value of a transaction; touching it under the guise of a
  tag correction would be an undisclosed valuation change.
DISCONFIRMING_OBSERVATION: >
  The exchange rate or converted amount on a multi-currency line differs after the pass compared to
  before.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Include multi-currency lines in scope and compare their rate and amount fields before and after
  the pass runs.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q026

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q026
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rounding adjustment line associated with a document is not reassigned to a different reporting
  classification than the substantive lines it reconciles, unless that divergence is an explicit,
  documented rule.
WHY_IT_MATTERS: >
  A rounding line separated from the classification of the amounts it reconciles can distort a
  report by a small but systematic amount across many documents.
DISCONFIRMING_OBSERVATION: >
  A rounding line's classification diverges from the substantive lines it reconciles with no
  documented rule explaining why.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Identify a document carrying a rounding adjustment line and inspect classification consistency
  after the pass runs.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q027

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q027
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The pass never triggers renumbering or reassignment of a document's own sequence number as a side
  effect of reclassifying its lines.
WHY_IT_MATTERS: >
  Document numbering is itself a control; an incidental renumbering from an unrelated maintenance
  action would break that control's integrity.
DISCONFIRMING_OBSERVATION: >
  A document's sequence number changes after its lines are reclassified.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Capture document numbers before and after for a sample of documents spanning several numbering
  series.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q028

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q028
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The mapping used to decide new classifications passes through a defined review step before it
  becomes available to a run, distinct from the step that actually executes the pass.
WHY_IT_MATTERS: >
  Without a separate review gate, a single actor could both define what changes and cause the
  change to happen.
DISCONFIRMING_OBSERVATION: >
  A newly edited mapping is applied by a run with no separate review action having occurred first.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Edit the mapping and attempt to run the pass immediately, without performing any review or
  approval action on the edit.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q029

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q029
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Only an account holding the specific grant to trigger the pass can do so; broad general
  administrative access alone is not sufficient.
WHY_IT_MATTERS: >
  A pass that rewrites posted history should not be reachable by the same broad grant that covers
  unrelated day-to-day administration.
DISCONFIRMING_OBSERVATION: >
  An account with general administrative access, but without the specific grant, is able to trigger
  the pass.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Attempt to trigger the pass from an account holding broad administrative rights but lacking the
  specific permission, if such a distinction exists.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q030

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q030
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  No available path — interactive, scheduled, or programmatic — can trigger the pass without
  leaving a trace of who or what triggered it and when.
WHY_IT_MATTERS: >
  A maintenance action that rewrites tax history without a trace is the single scenario the
  programme's audit requirements exist to prevent.
DISCONFIRMING_OBSERVATION: >
  A run exists in the data's history with no attributable trigger identity or timestamp.
EXPECTED_SURFACE: S4,S6,S8
PRECONDITIONS: >
  Trigger the pass through every available path (interactive, scheduled, programmatic where
  present) and check for a trace on each.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q031

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q031
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If the pass can be scheduled to run unattended in the background, the existence of that schedule
  and its authorization are themselves visible and auditable, not a hidden default.
WHY_IT_MATTERS: >
  An unattended pass rewriting posted history is a materially different risk than an
  operator-triggered one and needs its own visible authorization trail.
DISCONFIRMING_OBSERVATION: >
  An unattended scheduled run exists with no visible configuration record of who enabled it or
  under what authorization.
EXPECTED_SURFACE: S6,S7,S8
PRECONDITIONS: >
  Inspect whether an unattended scheduling capability exists for the pass and, if so, examine its
  configuration trail.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q032

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q032
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A preview or dry-run capability, where offered, shows exactly the set of changes a live run over
  the same unchanged scope would actually make.
WHY_IT_MATTERS: >
  A preview that misrepresents the live outcome gives a reviewer false confidence before an
  irreversible rewrite of history.
DISCONFIRMING_OBSERVATION: >
  A preview's reported change set differs from what actually occurs when the identical, unchanged
  scope is run live immediately after.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Run preview mode over a scope, then run live over the identical unchanged scope, and compare the
  two change sets.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q033

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q033
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The pass can be scoped to a filtered subset, such as a date range or a specific set of accounts,
  rather than only offering an all-or-nothing invocation over the entire historical dataset.
WHY_IT_MATTERS: >
  Forcing an all-or-nothing scope means a narrow, well-understood correction cannot be made without
  touching unrelated historical data.
DISCONFIRMING_OBSERVATION: >
  The only available invocation touches the entire historical dataset with no way to constrain
  scope.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Attempt to invoke the pass against a narrow, explicitly bounded subset of the data.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q034

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q034
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A document type that is out of scope for statutory tax reporting is not reached by the pass even
  if it technically carries a classification-bearing line.
WHY_IT_MATTERS: >
  Reaching into out-of-scope document types expands the blast radius of a maintenance pass beyond
  its stated purpose.
DISCONFIRMING_OBSERVATION: >
  An out-of-reporting-scope document type's lines are reclassified by the pass.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Ensure the environment includes a document type explicitly outside statutory reporting scope and
  run the pass broadly.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q035

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q035
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Lines related to tax withheld at the point of payment are explicitly included or explicitly
  excluded from the pass's reach by a stated rule, not swept in incidentally.
WHY_IT_MATTERS: >
  Withholding lines reconcile against a separate certificate trail; treating them like ordinary tax
  lines without a stated rule risks breaking that reconciliation.
DISCONFIRMING_OBSERVATION: >
  Withholding-related lines are reclassified with no rule statement distinguishing their treatment
  from ordinary tax lines.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Include withholding-related lines in the environment and inspect whether the pass's scope
  definition addresses them explicitly.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q036

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q036
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a withholding line's classification changes, any previously issued certificate or equivalent
  reconciling document tied to it is flagged for review rather than left silently disconnected.
WHY_IT_MATTERS: >
  A certificate already handed to a counterparty that no longer matches the underlying line is a
  reconciliation and compliance exposure.
DISCONFIRMING_OBSERVATION: >
  A withholding line tied to an already-issued certificate is reclassified with no flag connecting
  the change to the existing certificate.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Reclassify a withholding line that already has an issued certificate and observe whether any
  linkage or flag is raised.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q037

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q037
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where results feed a consolidated report spanning multiple companies or branches, reclassifying
  only some of the contributing entities does not silently produce a consolidated figure mixing
  pre- and post-reclassification bases without indicating the mismatch.
WHY_IT_MATTERS: >
  A consolidated figure that blends two different bases without disclosure misstates the group
  position.
DISCONFIRMING_OBSERVATION: >
  A consolidated report combines entities reclassified at different times with no indication of the
  mismatch.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  Reclassify one of several entities feeding a consolidated report and regenerate the consolidated
  figure.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q038

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q038
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A run that fails partway through, due to an error on one row, still records that the overall run
  failed, and does not roll back rows that were already correctly and independently processed.
WHY_IT_MATTERS: >
  Either silently applying a partial success as if it were a clean run, or over-broadly rolling back
  unrelated correct data, both misstate what actually happened.
DISCONFIRMING_OBSERVATION: >
  After a failed run, either the completed rows show no record that the run overall failed, or
  unrelated previously-correct data is reverted along with the failed portion.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Force an error partway through a run (for example, a constraint violation on one row) and inspect
  both the processed rows and the run's own recorded status.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q039

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q039
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The history of runs is retained for at least as long as the applicable financial record retention
  period, not purged on an unrelated, shorter cycle.
WHY_IT_MATTERS: >
  A maintenance pass that touches tax history should remain reviewable for as long as the
  transactions themselves are required to be retained.
DISCONFIRMING_OBSERVATION: >
  A run's history is no longer available for inspection well within the period financial records
  are otherwise required to be retained.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Inspect the retention configuration or observed behavior for run history against the retention
  period applied to financial records generally.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q040

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q040
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A data extract taken for tax filing purposes before the pass ran is flagged as potentially stale
  once the pass changes the same underlying data, rather than continuing to be treated as current.
WHY_IT_MATTERS: >
  An extract used for a filing decision that silently becomes outdated can lead to a filing based on
  data the system itself has since changed.
DISCONFIRMING_OBSERVATION: >
  A previously taken extract continues to be referenced as current with no staleness indication
  after the underlying data changes.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Take an extract, run the pass over the same lines, and check whether anything flags the extract as
  now stale.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q041

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q041
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reversing the effect of a prior run is itself a distinct, authorized, and audited action, not
  simply repeating a run with an older mapping with no record that it was a reversal.
WHY_IT_MATTERS: >
  An undo that looks identical to an ordinary forward run leaves no way to tell, later, that a
  correction was actually undone.
DISCONFIRMING_OBSERVATION: >
  An undo of a prior run's effect leaves no record distinguishing it as a reversal rather than an
  ordinary forward run.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Attempt to reverse a prior run's effect and inspect whether the reversal is recorded as such.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q042

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q042
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A reversal restores each line's exact original classification, rather than reapplying a generic
  "previous" mapping that may not match what that specific line actually held before.
WHY_IT_MATTERS: >
  A reversal that produces a plausible-but-wrong prior state is worse than no reversal capability,
  because it looks correct without being correct.
DISCONFIRMING_OBSERVATION: >
  A reversed line ends up with a classification different from what it held immediately before the
  original run.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Capture pre-run classification, run the pass, then reverse it, and compare the reversed state to
  the original.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q043

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q043
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A report generated concurrently with an in-progress run reflects one consistent snapshot, not a
  mix of pre- and post-change values within the same report.
WHY_IT_MATTERS: >
  A report that straddles a run in progress can present figures that never actually existed at any
  single point in time.
DISCONFIRMING_OBSERVATION: >
  A report generated while a run is in progress shows some lines reflecting the new classification
  and others the old, within what should be one consistent snapshot.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger the pass and, while it is running, generate a report covering the same scope.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q044

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q044
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The mapping's own change history is retained separately from run history, so a superseded mapping
  version can still be reviewed independently of any run that used it.
WHY_IT_MATTERS: >
  Reviewing why a past run produced a given outcome requires being able to see the exact rule set
  that was in force at the time.
DISCONFIRMING_OBSERVATION: >
  A past mapping version cannot be reconstructed once superseded, even though runs that used it are
  still recorded.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Change the mapping twice and attempt to retrieve the exact prior version after each change.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q045

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q045
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An unrelated inconsistency or reconciliation check over the same tax basis does not flip its
  pass/fail outcome purely because of when it happened to run relative to the reclassification pass.
WHY_IT_MATTERS: >
  A check whose result depends on run timing rather than the substance of the data cannot be trusted
  as evidence of anything.
DISCONFIRMING_OBSERVATION: >
  A reconciliation or consistency check's pass/fail outcome changes solely due to timing relative to
  the reclassification pass, with no substantive data reason.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Run a reconciliation or consistency check immediately before and immediately after the pass over
  the same data and compare outcomes.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q046

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q046
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user's company-scoped permission to trigger the pass for one company cannot be used to trigger
  it for a company that user does not otherwise have access to.
WHY_IT_MATTERS: >
  Company selection at invocation time must itself be subject to the same scoping as everything
  else the user does, or the boundary is only cosmetic.
DISCONFIRMING_OBSERVATION: >
  A user's company-scoped permission is not actually enforced when selecting the target company for
  the run.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Attempt to invoke the pass targeting a company outside the operator's assigned access.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q047

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q047
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  For every line it examines, the pass reports one of three distinguishable outcomes — changed,
  left unchanged because already correct, or flagged for manual decision — rather than only an
  aggregate count.
WHY_IT_MATTERS: >
  An aggregate-only report cannot support the line-level review this group's risk profile requires.
DISCONFIRMING_OBSERVATION: >
  The run output provides only a total count with no way to retrieve which specific lines fell into
  which of the three outcomes.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Run the pass over a mixed scope containing all three outcome types and inspect the available
  output.
```

## G04-ACCOUNT_UPDATE_TAX_TAGS-Q048

```yaml
QID: G04-ACCOUNT_UPDATE_TAX_TAGS-Q048
MODULE: account_update_tax_tags
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The pass is reachable only through its own defined administrative execution path, and never occurs
  as an incidental side effect of an unrelated bulk data operation.
WHY_IT_MATTERS: >
  A reclassification effect hiding inside an unrelated bulk operation would bypass every control
  built specifically around the dedicated pass.
DISCONFIRMING_OBSERVATION: >
  An unrelated bulk update or import operation touching the same lines triggers the same
  reclassification effect as the dedicated pass.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Perform an unrelated bulk data operation touching the same lines and check whether any
  reclassification occurs as a side effect.
```
