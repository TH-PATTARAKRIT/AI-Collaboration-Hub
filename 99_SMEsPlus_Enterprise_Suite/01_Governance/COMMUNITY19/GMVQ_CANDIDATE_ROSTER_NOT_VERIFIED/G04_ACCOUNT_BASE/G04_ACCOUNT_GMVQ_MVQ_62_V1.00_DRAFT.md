# SMEsPlus ENTERPRISE SUITE
## GMVQ — G04 ACCOUNT_BASE / account Module Adversarial MVQ Bank

**Document ID:** GMVQ-G04-ACCOUNT-MVQ62-V1.00
**Group:** G04 ACCOUNT_BASE
**Module Metadata:** `account`
**Wave:** W1
**Author Cell:** TEAM 20 (GMVQ Question Factory — Internal Production Team 20, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 62

## Purpose

`account` is the accounting core of the group and the highest-risk module in the programme: chart of accounts,
journals, entries, posting, periods, lock dates, reversal, currency, document numbering, and tax basis all sit
inside it. This bank supplements the 35 Standard Questions with module-specific, adversarial questions targeting
the mandatory review dimensions for this group, with particular depth on the approval/execution/posting
separation invariant, period and lock-date discipline, reversal versus compensating-entry semantics, document
numbering integrity under concurrency and failure, rounding residuals, multi-currency rate handling, and
cross-company/branch attribution. The bank exceeds the 48-question floor because this module's risk surface
warrants it; no question here is padding — every one targets a distinct, falsifiable hypothesis.

Question text is source-neutral: no vendor or product name, no technical identifier (model, table, field,
method, XML ID, API path), and no reference to how any specific implementation is built. Language is generic
accounting/business behaviour throughout.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 62 questions exist because they test 62 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, cross-module dependency, auditability, tenant/company boundary,
  concurrency/ordering, and runtime/configuration reachability.
- Questions carrying `LEGAL_TAX_REVIEW_REQUIRED: YES` state no specific statutory rate, form number, or filing
  deadline; they are written in behavioural terms only, per the Group Brief's Thai-tax prohibition.
- `LAYER: BASE` marks a foundation/configuration question; `LAYER: PROCESS` marks a transactional/posting-time
  question, since this module carries both layers.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a Research
  Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G04-ACCOUNT-Q001

```yaml
QID: G04-ACCOUNT-Q001
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Approving a transaction that requires approval must only change its approval status and must not, by itself,
  create or update the accounting entries for that transaction.
WHY_IT_MATTERS: >
  If approval performs the posting, the two controls collapse into one actor and one action, removing the
  compensating control the separation exists to provide.
DISCONFIRMING_OBSERVATION: >
  Recording an approval decision by itself results in ledger entries appearing for the transaction, with no
  separate posting action performed by anyone.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Configure a transaction type to require approval before posting; approve it and inspect whether ledger entries
  exist and who or what created them.
```

## G04-ACCOUNT-Q002

```yaml
QID: G04-ACCOUNT-Q002
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The logic that determines debit/credit lines, accounts, and amounts for a transaction executes independently
  of the approval decision logic, so that changing the approval outcome alone cannot alter the resulting entries.
WHY_IT_MATTERS: >
  Posting logic embedded inside the approval path is invisible to reviewers who only reviewed for approval, and
  any change to approval rules could unexpectedly re-derive entries.
DISCONFIRMING_OBSERVATION: >
  Changing only the approval workflow configuration (routing, approver count, approval reason) changes the
  resulting ledger entry amounts or accounts for the same underlying transaction.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Post the same transaction under two different approval configurations and compare the resulting entries line
  by line.
```

## G04-ACCOUNT-Q003

```yaml
QID: G04-ACCOUNT-Q003
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A transaction whose approval is rejected or withdrawn has zero accounting impact; no partial or draft-only
  ledger entries persist as if posted.
WHY_IT_MATTERS: >
  Partial posting under rejection corrupts the ledger with entries that have no corresponding approved business
  event.
DISCONFIRMING_OBSERVATION: >
  After rejecting or withdrawing an approval, some accounting entries for that transaction remain visible in a
  posted or semi-posted state.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Submit a transaction for approval, reject it, and inspect the ledger and any draft-entry stores for residue.
```

## G04-ACCOUNT-Q004

```yaml
QID: G04-ACCOUNT-Q004
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A transaction type configured to require approval before posting cannot be posted through any alternate
  supported entry point that skips the approval step.
WHY_IT_MATTERS: >
  A control that only blocks one path is not a control; the weakness noted in UI-only security applies equally
  to workflow-only approval.
DISCONFIRMING_OBSERVATION: >
  The same transaction can be posted through a bulk action, an import, an API call, or a related document flow
  without the approval step being enforced.
EXPECTED_SURFACE: S1,S2,S3,S4
PRECONDITIONS: >
  Identify every supported way to create and post the transaction type, then attempt each without completing
  approval.
```

## G04-ACCOUNT-Q005

```yaml
QID: G04-ACCOUNT-Q005
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Every action that posts or unposts (reverses the posted state of) a transaction leaves an identifiable trace
  of who performed it and when, regardless of which supported path was used.
WHY_IT_MATTERS: >
  Without a trace, posting and unposting become a way to alter financial state without accountability.
DISCONFIRMING_OBSERVATION: >
  A transaction changes from posted to unposted (or the reverse) with no corresponding trace entry identifying
  an actor and timestamp.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Post a transaction, then unpost it through each supported path, and inspect the audit or log trail after each.
```

## G04-ACCOUNT-Q006

```yaml
QID: G04-ACCOUNT-Q006
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  An actor with elevated privilege who can post on behalf of another still records the transaction under one
  explicit accounting scope (company/branch), not an ambiguous or blended one.
WHY_IT_MATTERS: >
  Ambiguous scope on privileged actions undermines the boundary the rest of the ledger depends on.
DISCONFIRMING_OBSERVATION: >
  A privileged actor's posting action produces an entry whose company or branch scope is ambiguous, blank, or
  spans more than one scope without explicit multi-scope semantics.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Use a privileged account to post transactions while switching active company/branch context mid-session.
```

## G04-ACCOUNT-Q007

```yaml
QID: G04-ACCOUNT-Q007
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A transaction's document date, posting date, and tax point date are tracked as distinct values, and the
  accounting period is determined by the posting date, not by the document date.
WHY_IT_MATTERS: >
  Conflating these dates misstates which period bears the financial impact and can misalign tax point
  recognition with actual delivery.
DISCONFIRMING_OBSERVATION: >
  Two transactions with the same document date but different posting dates land in the same accounting period,
  or the period is derived from the document date instead.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a transaction dated in one period but posted in a later period, and inspect which period the entry
  lands in.
```

## G04-ACCOUNT-Q008

```yaml
QID: G04-ACCOUNT-Q008
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When the tax point date differs from the posting date, both are tracked independently, so that a tax report
  by tax point date does not silently use the posting date instead.
WHY_IT_MATTERS: >
  A report drawing the wrong date field would misstate a filing period without any visible error.
DISCONFIRMING_OBSERVATION: >
  A transaction with a distinct tax point date is reported as belonging to the posting-date period on a
  tax-point-based report.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set a tax point date different from the posting date on a transaction and run a report keyed to tax point
  date.
LEGAL_TAX_REVIEW_REQUIRED: YES
```

## G04-ACCOUNT-Q009

```yaml
QID: G04-ACCOUNT-Q009
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Editing the document date after posting does not silently move the transaction to a different accounting
  period.
WHY_IT_MATTERS: >
  A posted transaction's period should require a controlled correction, not an incidental edit.
DISCONFIRMING_OBSERVATION: >
  Changing the document date on an already-posted transaction changes which period it is reported under, without
  going through a correction or reversal control.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a transaction, then edit its document date, and check the reporting period before and after.
```

## G04-ACCOUNT-Q010

```yaml
QID: G04-ACCOUNT-Q010
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A transaction dated before the earliest date the current accounting configuration recognizes as open is
  rejected or clearly flagged, not silently posted into an ambiguous period.
WHY_IT_MATTERS: >
  Silent acceptance of an out-of-range date can misstate the first reporting period after go-live or migration.
DISCONFIRMING_OBSERVATION: >
  A document dated before the configured start of operations posts without any warning or period ambiguity
  flag.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Attempt to post a document dated earlier than the configured opening date of the accounting scope.
```

## G04-ACCOUNT-Q011

```yaml
QID: G04-ACCOUNT-Q011
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a transaction spans a period boundary conceptually (delivered in one period, invoiced in the next), the
  two events are recorded on their own dates rather than forced onto a single shared date.
WHY_IT_MATTERS: >
  Forcing a single date for a multi-event transaction hides the true timing of each financial event.
DISCONFIRMING_OBSERVATION: >
  Two genuinely distinct events for the same transaction (delivery and invoicing) are recorded under one
  identical forced date regardless of when each occurred.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a transaction whose linked events naturally occur on different dates and inspect the recorded date for
  each.
```

## G04-ACCOUNT-Q012

```yaml
QID: G04-ACCOUNT-Q012
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Once a period is locked or closed, no new transaction may post into it through any supported path, including
  import, API, or a scheduled process.
WHY_IT_MATTERS: >
  A lock date that only blocks manual entry is not a lock date.
DISCONFIRMING_OBSERVATION: >
  A new transaction dated inside a locked period is successfully posted through import, API, or a scheduled
  process even though manual entry is blocked.
EXPECTED_SURFACE: S1,S2,S3,S8
PRECONDITIONS: >
  Lock a period, then attempt to post into it through each available path.
```

## G04-ACCOUNT-Q013

```yaml
QID: G04-ACCOUNT-Q013
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A late-arriving document for a locked period is redirected to post in an open period, or explicitly blocked;
  it is never silently accepted with a locked-period date.
WHY_IT_MATTERS: >
  Silent acceptance defeats the purpose of the lock and produces entries no closed report reflects.
DISCONFIRMING_OBSERVATION: >
  A document dated within a locked period is accepted and posted with that original date, with no redirection
  or block.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Lock a period, then submit a document dated inside it and observe the outcome.
```

## G04-ACCOUNT-Q014

```yaml
QID: G04-ACCOUNT-Q014
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A correction to a transaction whose original period is locked is recorded in an open period, referencing the
  original, rather than editing the original entry in place.
WHY_IT_MATTERS: >
  Editing a locked-period entry in place would change closed, reported figures after the fact.
DISCONFIRMING_OBSERVATION: >
  A correction to a transaction in a locked period changes the original entry's values in place instead of
  creating a new, separately dated correction.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Lock the period containing a posted transaction, then attempt to correct that transaction.
```

## G04-ACCOUNT-Q015

```yaml
QID: G04-ACCOUNT-Q015
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A reversal of a transaction whose original period is locked is dated in an open period, not forced or
  defaulted into the locked original period.
WHY_IT_MATTERS: >
  A reversal dated into a locked period would itself violate the lock it is meant to respect.
DISCONFIRMING_OBSERVATION: >
  Reversing a transaction from a locked period produces a reversal entry dated inside that locked period.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Lock a period containing a posted transaction, then reverse it and inspect the reversal's date.
```

## G04-ACCOUNT-Q016

```yaml
QID: G04-ACCOUNT-Q016
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The lock date is enforced per accounting scope (company/branch) and does not accidentally block, or fail to
  block, postings in a different scope that has its own, different lock date.
WHY_IT_MATTERS: >
  A shared or misapplied lock date could either over-block a scope that should remain open or under-block one
  that should be closed.
DISCONFIRMING_OBSERVATION: >
  Locking one company/branch's period also blocks, or fails to block, posting in a different scope with an
  independent lock date.
EXPECTED_SURFACE: S1,S2,S4,S7
PRECONDITIONS: >
  Set different lock dates on two scopes and attempt postings dated between the two lock dates in each.
```

## G04-ACCOUNT-Q017

```yaml
QID: G04-ACCOUNT-Q017
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Only a role explicitly authorized to manage periods may move or remove a lock date; a general posting role
  cannot unlock a period as a side effect of another action.
WHY_IT_MATTERS: >
  An incidental unlock would defeat the control without anyone deciding to open the period.
DISCONFIRMING_OBSERVATION: >
  A user without period-management authority causes the lock date to move or clear as a side effect of an
  unrelated action.
EXPECTED_SURFACE: S4,S6,S7
PRECONDITIONS: >
  As a user with only posting rights, attempt actions near a lock date boundary and check whether the lock date
  itself changes.
```

## G04-ACCOUNT-Q018

```yaml
QID: G04-ACCOUNT-Q018
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The system distinguishes, and records which of, two reversal shapes occurred: an exact mirror-image reversal
  restoring the pre-transaction balance, versus an independent compensating entry that nets to the same balance
  through different lines.
WHY_IT_MATTERS: >
  A reviewer tracing history needs to know whether a reversal is a literal undo or a separate business event
  that happens to offset it.
DISCONFIRMING_OBSERVATION: >
  Two different reversal mechanisms (mirror reversal and compensating entry) leave an identical audit trail
  with no way to tell which occurred.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Perform a mirror reversal on one transaction and a compensating entry on an equivalent transaction, then
  compare the audit trail of each.
```

## G04-ACCOUNT-Q019

```yaml
QID: G04-ACCOUNT-Q019
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A reversal references the original transaction it reverses, and the original shows that it has been reversed;
  neither side can be updated without the other.
WHY_IT_MATTERS: >
  A one-sided reversal link breaks traceability from either direction of lookup.
DISCONFIRMING_OBSERVATION: >
  A reversal exists that does not reference its original, or an original shows no indication that a reversal
  was recorded against it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reverse a posted transaction and inspect both the original and the reversal record for mutual reference.
```

## G04-ACCOUNT-Q020

```yaml
QID: G04-ACCOUNT-Q020
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing an already-reversed transaction a second time is blocked, or does not silently double the financial
  impact.
WHY_IT_MATTERS: >
  A double reversal would misstate the ledger by an amount equal to the original transaction.
DISCONFIRMING_OBSERVATION: >
  A transaction that is already reversed can be reversed again, producing a net financial effect different from
  the intended single reversal.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Reverse a posted transaction, then attempt to reverse it a second time through every supported path.
```

## G04-ACCOUNT-Q021

```yaml
QID: G04-ACCOUNT-Q021
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A partial reversal (reversing only some lines or some amount of a transaction) leaves the remaining unreversed
  portion clearly identifiable and separately traceable.
WHY_IT_MATTERS: >
  An all-or-nothing reversal model forces workarounds that lose the audit link for partial corrections.
DISCONFIRMING_OBSERVATION: >
  A partial reversal either is impossible to represent cleanly or leaves the remaining unreversed amount without
  a clear link back to the original.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Attempt a partial reversal of a multi-line transaction and inspect how the remainder is represented.
```

## G04-ACCOUNT-Q022

```yaml
QID: G04-ACCOUNT-Q022
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  The accounts, journal, and analytic attribution used by a reversal are derived from the original transaction,
  not from whatever defaults are active for the actor performing the reversal at the time.
WHY_IT_MATTERS: >
  A reversal using the reverser's current defaults instead of the original's context can post to the wrong
  journal or account.
DISCONFIRMING_OBSERVATION: >
  Reversing the same original transaction under two different active default configurations produces reversals
  posted to different accounts or journals.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Change the active posting defaults, then reverse a transaction originally posted under different defaults,
  and compare the reversal's accounts to the original's.
```

## G04-ACCOUNT-Q023

```yaml
QID: G04-ACCOUNT-Q023
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a posted transaction is either blocked outright or itself generates a reversing accounting entry;
  a posted transaction cannot become cancelled while its ledger entries silently disappear.
WHY_IT_MATTERS: >
  Entries that vanish without a trace break reconciliation between the document trail and the ledger.
DISCONFIRMING_OBSERVATION: >
  Cancelling a posted transaction removes or hides its ledger entries with no reversing entry and no record that
  a cancellation occurred.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a transaction, then invoke cancellation, and inspect the ledger and the document's history afterward.
```

## G04-ACCOUNT-Q024

```yaml
QID: G04-ACCOUNT-Q024
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A cancelled transaction retains its original document number and history; the number is not freed for reuse
  by a new, unrelated transaction.
WHY_IT_MATTERS: >
  Reused numbers on cancelled documents break the sequential integrity a numbering series exists to guarantee.
DISCONFIRMING_OBSERVATION: >
  The document number of a cancelled transaction is later assigned to a different, unrelated transaction.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a posted transaction and continue creating new transactions in the same series to check for number
  reuse.
```

## G04-ACCOUNT-Q025

```yaml
QID: G04-ACCOUNT-Q025
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A transaction that is part of a linked chain (it settles, or is settled by, another document) cannot be
  cancelled while that link is active without the dependent side being addressed first.
WHY_IT_MATTERS: >
  Cancelling one side of a linked pair while leaving the other intact creates an orphaned reference.
DISCONFIRMING_OBSERVATION: >
  Cancelling a transaction leaves a linked document referencing it as still active, with no warning or
  corrective action.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Link two transactions through a settlement relationship, then attempt to cancel one side.
```

## G04-ACCOUNT-Q026

```yaml
QID: G04-ACCOUNT-Q026
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Each numbering series produces strictly increasing numbers with no gap left by a number being allocated and
  then discarded without a recorded reason.
WHY_IT_MATTERS: >
  Unexplained gaps in a legally meaningful sequence invite doubt about missing or hidden transactions.
DISCONFIRMING_OBSERVATION: >
  A gap appears in a numbering series with no corresponding cancelled or voided record accounting for the
  missing number.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create and then abandon (without saving, or by triggering a validation failure after number allocation)
  several draft transactions, and inspect the resulting sequence for unexplained gaps.
```

## G04-ACCOUNT-Q027

```yaml
QID: G04-ACCOUNT-Q027
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Two transactions created concurrently in the same numbering series never receive the same number.
WHY_IT_MATTERS: >
  A duplicate document number in a financial series is a direct integrity failure with legal exposure.
DISCONFIRMING_OBSERVATION: >
  Two concurrently created transactions in the same numbering series end up with identical numbers.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger near-simultaneous creation of two transactions in the same series from separate sessions and compare
  the assigned numbers.
```

## G04-ACCOUNT-Q028

```yaml
QID: G04-ACCOUNT-Q028
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  When numbering is scoped per company and per branch, a series never mixes numbers across two different
  company/branch scopes, even when both scopes share the same numbering pattern or prefix.
WHY_IT_MATTERS: >
  Cross-scope number mixing breaks the per-entity sequential guarantee each scope's series is meant to provide.
DISCONFIRMING_OBSERVATION: >
  Two transactions in different company/branch scopes, using series with the same pattern, draw from a single
  shared counter instead of independent ones.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure identical-looking series patterns in two scopes and create transactions in both to inspect whether
  counters are independent.
```

## G04-ACCOUNT-Q029

```yaml
QID: G04-ACCOUNT-Q029
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If number allocation fails partway through (the surrounding transaction fails validation after a number was
  drawn), the failure is handled by either releasing the number cleanly and recording why, or reserving it
  against a recorded void — never left in an undocumented, ambiguous state.
WHY_IT_MATTERS: >
  Ambiguous partial-failure handling is exactly where unexplained gaps and silent duplication both originate.
DISCONFIRMING_OBSERVATION: >
  A failed transaction leaves its drawn number in a state that is neither released with a reason nor recorded
  as voided.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Force a validation failure after triggering number allocation and inspect the resulting state of that number.
```

## G04-ACCOUNT-Q030

```yaml
QID: G04-ACCOUNT-Q030
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Changing a numbering series' pattern or starting point does not retroactively renumber, or create ambiguity
  for, transactions already posted under the previous pattern.
WHY_IT_MATTERS: >
  Retroactive renumbering would break every existing external reference to those documents.
DISCONFIRMING_OBSERVATION: >
  Changing a series configuration changes the displayed or stored number of a transaction posted before the
  change.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Post transactions under one series configuration, change the configuration, and re-inspect the earlier
  transactions' numbers.
```

## G04-ACCOUNT-Q031

```yaml
QID: G04-ACCOUNT-Q031
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A background or scheduled process that allocates numbers from the same series as interactive posting is
  subject to the same uniqueness and gap-accounting guarantees as interactive posting.
WHY_IT_MATTERS: >
  A separate, less-guarded allocation path for automated posting is a common source of silent duplication.
DISCONFIRMING_OBSERVATION: >
  A number collision or unexplained gap occurs specifically when a scheduled process and an interactive user
  allocate from the same series close together in time.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Trigger a scheduled posting process and an interactive posting in the same series at close to the same time
  and inspect the resulting numbers.
```

## G04-ACCOUNT-Q032

```yaml
QID: G04-ACCOUNT-Q032
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  An import that creates transactions with pre-existing external numbers is handled distinctly from the
  internal sequence, and does not silently consume or corrupt the internal counter.
WHY_IT_MATTERS: >
  Blending externally supplied numbers into an internal sequential counter can create both duplicates and
  unexplained jumps.
DISCONFIRMING_OBSERVATION: >
  Importing transactions carrying their own external numbers changes the next number the internal sequence
  would allocate, in a way that produces a gap or collision.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Import a batch of transactions carrying pre-set external numbers, then create a new transaction interactively
  and check the number it receives.
```

## G04-ACCOUNT-Q033

```yaml
QID: G04-ACCOUNT-Q033
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Rounding applied at the line level and rounding applied at the document total level are both visible, and the
  residual difference between summed rounded lines and the rounded total is posted to a distinct, identifiable
  account rather than absorbed into an unrelated line.
WHY_IT_MATTERS: >
  An untracked rounding residual silently distorts whichever account absorbs it.
DISCONFIRMING_OBSERVATION: >
  A rounding residual between line-level and document-level totals is added into a substantive revenue,
  expense, or tax line rather than a distinct rounding account.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct a transaction whose line amounts, when summed, differ by a rounding unit from the rounded document
  total, and inspect where the difference posts.
```

## G04-ACCOUNT-Q034

```yaml
QID: G04-ACCOUNT-Q034
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Tax computed on a rounded line amount versus tax computed on the unrounded amount and then rounded follows a
  documented, consistent choice, applied the same way across all transactions of that type.
WHY_IT_MATTERS: >
  An inconsistent rounding order produces small but real differences between similar transactions, undermining
  reconciliation.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical transactions compute a different tax amount purely because of when rounding is
  applied in the calculation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct two equivalent transactions that would round differently depending on calculation order and compare
  the tax result.
LEGAL_TAX_REVIEW_REQUIRED: YES
```

## G04-ACCOUNT-Q035

```yaml
QID: G04-ACCOUNT-Q035
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Changing the rounding precision or method for a currency does not retroactively recompute already-posted
  transactions' stored amounts.
WHY_IT_MATTERS: >
  Retroactive recomputation of posted amounts would silently alter closed financial history.
DISCONFIRMING_OBSERVATION: >
  Changing the currency's rounding configuration changes the stored amount of a transaction posted before the
  change.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Post a transaction, change the currency's rounding precision, and re-inspect the transaction's stored amounts.
```

## G04-ACCOUNT-Q036

```yaml
QID: G04-ACCOUNT-Q036
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  The rounding difference between summing per-line tax amounts and computing tax once on the document subtotal
  is bounded and explicit, never large enough to be mistaken for a computation error, and is disclosed on the
  document.
WHY_IT_MATTERS: >
  An undisclosed large tax rounding gap would look like a defect in the tax calculation itself.
DISCONFIRMING_OBSERVATION: >
  The gap between per-line tax summation and single-total tax computation exceeds a minimal rounding unit, or
  is not shown anywhere on the document.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct a multi-line, multi-rate transaction and compare both tax computation methods against what is
  actually posted and disclosed.
LEGAL_TAX_REVIEW_REQUIRED: YES
```

## G04-ACCOUNT-Q037

```yaml
QID: G04-ACCOUNT-Q037
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A transaction denominated in a foreign currency stores the exchange rate used at the document date,
  independent of whatever rate is current at posting or at later payment.
WHY_IT_MATTERS: >
  Losing the document-date rate makes it impossible to reconstruct why an entry has the values it has.
DISCONFIRMING_OBSERVATION: >
  Re-opening a foreign-currency transaction later shows a rate different from the one in force at its original
  document date, with no rate history preserved.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a foreign-currency transaction, change the currency's rate afterward, and re-inspect the transaction's
  stored rate.
```

## G04-ACCOUNT-Q038

```yaml
QID: G04-ACCOUNT-Q038
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When payment on a foreign-currency transaction occurs at a different rate than the document, the resulting
  exchange gain or loss posts to a distinct, identifiable account, not blended into the original revenue/expense
  or receivable/payable account.
WHY_IT_MATTERS: >
  Blending exchange differences into operational accounts misstates both the currency result and the
  operational result.
DISCONFIRMING_OBSERVATION: >
  A payment settled at a different rate than the original document changes the balance of the original
  revenue/expense account rather than posting the difference to a dedicated exchange account.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a foreign-currency transaction, then settle it at a materially different rate, and inspect which accounts
  absorb the difference.
```

## G04-ACCOUNT-Q039

```yaml
QID: G04-ACCOUNT-Q039
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An open foreign-currency balance can be revalued at a period-end rate without altering the original
  transaction's stored rate or amount; revaluation produces its own adjustment entry.
WHY_IT_MATTERS: >
  Overwriting the original amount during revaluation would destroy the transaction's original basis.
DISCONFIRMING_OBSERVATION: >
  Running a period-end revaluation changes the original transaction's stored amount instead of producing a
  separate adjustment entry.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Run a period-end revaluation over an open foreign-currency balance and compare the original transaction before
  and after.
```

## G04-ACCOUNT-Q040

```yaml
QID: G04-ACCOUNT-Q040
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  The source of the exchange rate (manually entered versus an automatically fetched rate) used on a given
  transaction is recorded, so a reviewer can tell which rate governed that transaction.
WHY_IT_MATTERS: >
  Without recording the rate source, a reviewer cannot judge whether a rate was appropriate or overridden.
DISCONFIRMING_OBSERVATION: >
  A transaction's posted entry gives no indication of whether the rate applied was manually overridden or taken
  from an automatic source.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post one transaction with an automatically supplied rate and another with a manually overridden rate, then
  compare what each record discloses.
```

## G04-ACCOUNT-Q041

```yaml
QID: G04-ACCOUNT-Q041
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A multi-currency transaction always carries a value in the accounting scope's base/functional currency
  alongside the transaction currency; no posted entry exists in a foreign currency alone.
WHY_IT_MATTERS: >
  Reports and consolidations depend on every entry having a comparable base-currency value.
DISCONFIRMING_OBSERVATION: >
  A posted entry exists with a value only in the foreign transaction currency and no corresponding base-currency
  amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a foreign-currency transaction and inspect the entry for a base-currency value alongside the
  transaction-currency value.
```

## G04-ACCOUNT-Q042

```yaml
QID: G04-ACCOUNT-Q042
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Every posted entry is balanced: total debits equal total credits at the level the accounting model defines as
  atomic, with no supported path able to post an unbalanced entry.
WHY_IT_MATTERS: >
  An unbalanced entry is the most fundamental possible corruption of a double-entry ledger.
DISCONFIRMING_OBSERVATION: >
  An entry posts successfully through any supported path (interactive, import, API, scheduled) with debits not
  equal to credits.
EXPECTED_SURFACE: S1,S2,S3,S8
PRECONDITIONS: >
  Attempt to construct and post a deliberately unbalanced entry through each available path.
```

## G04-ACCOUNT-Q043

```yaml
QID: G04-ACCOUNT-Q043
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Each journal restricts postings to a defined set of allowed accounts or account types; posting outside that
  set is blocked or explicitly flagged, not silently allowed.
WHY_IT_MATTERS: >
  Unrestricted journals defeat the organizational control journals are meant to provide.
DISCONFIRMING_OBSERVATION: >
  A posting to an account outside a journal's configured restriction succeeds without warning or block.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a journal with a restricted account set and attempt to post to an account outside that set.
```

## G04-ACCOUNT-Q044

```yaml
QID: G04-ACCOUNT-Q044
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Deactivating or archiving an account that has historical postings does not remove or hide those historical
  postings from reports that reference the account.
WHY_IT_MATTERS: >
  Archiving as a substitute for deletion must not have deletion's effect on historical reporting.
DISCONFIRMING_OBSERVATION: >
  Archiving an account causes historical entries referencing it to disappear from, or be miscounted in,
  historical reports.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post entries to an account, archive the account, and re-run a historical report covering the posting date.
```

## G04-ACCOUNT-Q045

```yaml
QID: G04-ACCOUNT-Q045
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  An account marked as requiring a secondary tracking dimension (such as a partner or analytic tag) cannot be
  posted to without that dimension supplied, through any posting path.
WHY_IT_MATTERS: >
  Missing required dimensions break reconciliation and sub-ledger detail that downstream reports depend on.
DISCONFIRMING_OBSERVATION: >
  A posting to a dimension-required account succeeds through some path (import or API) without the required
  dimension.
EXPECTED_SURFACE: S1,S2,S3,S7
PRECONDITIONS: >
  Configure an account to require a tracking dimension and attempt postings without it through each available
  path.
```

## G04-ACCOUNT-Q046

```yaml
QID: G04-ACCOUNT-Q046
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A single accounting entry belongs to exactly one company scope; an inter-company transaction is represented
  as two or more linked, single-scope entries, never one entry attributed to multiple companies at once.
WHY_IT_MATTERS: >
  A multi-scope entry breaks every report and control that assumes one entry belongs to one legal entity.
DISCONFIRMING_OBSERVATION: >
  An inter-company transaction produces a single entry whose company attribution spans more than one company,
  rather than linked entries each within a single company.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Create an inter-company transaction and inspect whether it produces one multi-scope entry or linked
  single-scope entries.
```

## G04-ACCOUNT-Q047

```yaml
QID: G04-ACCOUNT-Q047
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A user authorized to post in one company/branch cannot post an entry attributed to a different company/branch
  they are not authorized for, even through a document that references both.
WHY_IT_MATTERS: >
  Cross-scope authorization leakage through a linking document is a realistic bypass of the company boundary.
DISCONFIRMING_OBSERVATION: >
  A user posts, or causes to be posted, an entry attributed to a company/branch scope they have no authorization
  for, via a document referencing an authorized scope.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Give a user authorization to only one scope, then have them process a document that references or links to a
  second scope.
```

## G04-ACCOUNT-Q048

```yaml
QID: G04-ACCOUNT-Q048
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Branch-level reporting rolls up correctly to the head-office/company level without double-counting or omitting
  entries attributed to a branch.
WHY_IT_MATTERS: >
  A roll-up defect would misstate both the branch and the consolidated company result.
DISCONFIRMING_OBSERVATION: >
  The sum of branch-level figures does not match the company-level figure for the same period and accounts,
  with no reconciling explanation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post entries across several branches under one company and compare branch-level totals against the
  company-level total for the same period.
```

## G04-ACCOUNT-Q049

```yaml
QID: G04-ACCOUNT-Q049
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The permission to post a transaction and the permission to unpost (reverse the posted state of) a transaction
  are independently assignable; granting one does not implicitly grant the other.
WHY_IT_MATTERS: >
  Bundling post and unpost authority removes the ability to give someone forward-only posting rights.
DISCONFIRMING_OBSERVATION: >
  A user granted only posting permission is nonetheless able to unpost a transaction, or vice versa.
EXPECTED_SURFACE: S4,S6,S7
PRECONDITIONS: >
  Grant a user posting permission only, then attempt an unpost action, and repeat with the permissions reversed.
```

## G04-ACCOUNT-Q050

```yaml
QID: G04-ACCOUNT-Q050
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Unposting a transaction is itself an auditable event distinct from any subsequent edit or re-post; a reviewer
  can see that a transaction was unposted, by whom, and when, even if it is later re-posted unchanged.
WHY_IT_MATTERS: >
  An unpost that leaves no separate trace when immediately re-posted could be used to quietly reopen and
  re-close a period's figures.
DISCONFIRMING_OBSERVATION: >
  A transaction that is unposted and then re-posted unchanged shows no trace of the intervening unpost event.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Unpost a transaction, immediately re-post it without changes, and inspect the audit trail for a record of the
  unpost.
```

## G04-ACCOUNT-Q051

```yaml
QID: G04-ACCOUNT-Q051
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Marking two or more entries as reconciled against each other is reversible, and reversing it restores each
  entry to its prior open/unreconciled state without altering their amounts.
WHY_IT_MATTERS: >
  An irreversible or amount-altering reconciliation would make correcting a mistaken match destructive.
DISCONFIRMING_OBSERVATION: >
  Undoing a reconciliation changes the amount of one of the entries involved, or leaves one entry in an
  inconsistent reconciled/unreconciled state.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Reconcile two entries, then undo the reconciliation, and inspect both entries' state and amounts.
```

## G04-ACCOUNT-Q052

```yaml
QID: G04-ACCOUNT-Q052
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An entry cannot be reconciled against entries from a different company/branch scope, or against an
  amount/currency that does not correspond to it, without an explicit override that is itself recorded.
WHY_IT_MATTERS: >
  Cross-scope or mismatched reconciliation would let genuinely unrelated entries be marked as settled against
  each other.
DISCONFIRMING_OBSERVATION: >
  Two entries from different company scopes, or with clearly mismatched open amounts, are reconciled against
  each other with no override recorded.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Attempt to reconcile entries across scopes or with mismatched amounts and inspect what is required to
  complete it.
```

## G04-ACCOUNT-Q053

```yaml
QID: G04-ACCOUNT-Q053
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Partially reconciling an entry (settling part of its amount) leaves the remaining open balance correctly
  reflected and still available for further reconciliation.
WHY_IT_MATTERS: >
  A defect here would leave receivables/payables permanently misstated after any partial settlement.
DISCONFIRMING_OBSERVATION: >
  After a partial reconciliation, the remaining open balance on the entry is incorrect, missing, or no longer
  reconcilable.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially reconcile a multi-installment entry and inspect the remaining open balance afterward.
```

## G04-ACCOUNT-Q054

```yaml
QID: G04-ACCOUNT-Q054
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A transaction posted after a financial report for its period has already been generated is flagged as
  affecting a previously issued report, rather than being silently included as if the report had never been
  produced.
WHY_IT_MATTERS: >
  Silent inclusion could let a previously issued report be quietly superseded without anyone knowing it changed.
DISCONFIRMING_OBSERVATION: >
  Regenerating a report for an already-reported period includes a later-dated posting with no indication that
  the figures differ from what was previously issued.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Generate a period report, then post an additional transaction dated in that period, and regenerate the report
  to compare.
```

## G04-ACCOUNT-Q055

```yaml
QID: G04-ACCOUNT-Q055
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A change to how an account maps onto financial statement line items (its report classification) does not
  retroactively change what an already-issued report showed, only future report runs.
WHY_IT_MATTERS: >
  Retroactive reclassification would make a previously distributed report an unreliable historical record.
DISCONFIRMING_OBSERVATION: >
  Changing an account's report classification alters the figures a previously generated and saved report
  displays when reopened.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Generate and save a report, change the underlying account classification, and reopen the saved report to
  compare.
```

## G04-ACCOUNT-Q056

```yaml
QID: G04-ACCOUNT-Q056
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The taxable basis used to compute a transaction's tax is derived from the transaction's own line amounts at
  the applicable date, not from a stale or cached total computed earlier in the document's lifecycle.
WHY_IT_MATTERS: >
  A stale basis would compute tax on values the document no longer reflects.
DISCONFIRMING_OBSERVATION: >
  Editing a transaction's line amounts before posting does not change the tax amount computed at posting.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Edit line amounts on a draft transaction after tax was first computed, then post it and check whether the tax
  reflects the final amounts.
LEGAL_TAX_REVIEW_REQUIRED: YES
```

## G04-ACCOUNT-Q057

```yaml
QID: G04-ACCOUNT-Q057
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When the configured statutory rate for a tax changes, transactions already posted under the previous rate
  retain that rate; only transactions dated on or after the change's effective date use the new rate, unless an
  explicit retroactive action is taken.
WHY_IT_MATTERS: >
  A rate change that silently retroactively recomputes existing transactions would misstate already-reported tax
  figures.
DISCONFIRMING_OBSERVATION: >
  Changing the configured rate alters the computed tax amount of a transaction already posted under the earlier
  rate, without an explicit retroactive action being taken.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Post a transaction under one configured rate, change the rate, and re-inspect the earlier transaction's
  computed tax.
LEGAL_TAX_REVIEW_REQUIRED: YES
```

## G04-ACCOUNT-Q058

```yaml
QID: G04-ACCOUNT-Q058
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A tax computed with a rule expressed as a configurable formula produces the same result as an equivalent
  fixed-rate configuration for the same inputs, so the two computation styles are not silently inconsistent with
  each other on shared transactions.
WHY_IT_MATTERS: >
  Divergent results between computation styles for logically equivalent configurations would make tax totals
  unpredictable.
DISCONFIRMING_OBSERVATION: >
  A transaction computes a different tax amount depending only on whether the applicable rule is expressed as a
  formula or as an equivalent fixed rate.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure two logically equivalent tax rules, one as a fixed rate and one as a formula, and compare results on
  the same transaction.
LEGAL_TAX_REVIEW_REQUIRED: YES
```

## G04-ACCOUNT-Q059

```yaml
QID: G04-ACCOUNT-Q059
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An amount withheld at payment is linked back to the specific invoice(s) it relates to, so the sum of withheld
  amounts against an invoice can be reconciled to that invoice's own tax basis.
WHY_IT_MATTERS: >
  An unlinked withholding amount cannot be defended in an audit of that invoice's tax treatment.
DISCONFIRMING_OBSERVATION: >
  A withheld amount recorded at payment shows no traceable link to the invoice(s) whose basis it was computed
  from.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record a payment with withholding against an invoice and inspect whether the withheld amount is linked back
  to that invoice.
LEGAL_TAX_REVIEW_REQUIRED: YES
```

## G04-ACCOUNT-Q060

```yaml
QID: G04-ACCOUNT-Q060
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A withholding certificate reference, once issued for a payment, cannot be silently replaced or altered by a
  later edit to the payment; a correction produces a new, distinctly identified certificate reference and
  preserves the old one's record.
WHY_IT_MATTERS: >
  An overwritten certificate reference destroys the audit trail a payee would need to substantiate the
  withholding.
DISCONFIRMING_OBSERVATION: >
  Editing a payment after its withholding certificate reference was issued silently changes or removes that
  reference without preserving the original.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Issue a withholding certificate reference for a payment, then edit the payment, and inspect whether the
  original reference is preserved.
LEGAL_TAX_REVIEW_REQUIRED: YES
```

## G04-ACCOUNT-Q061

```yaml
QID: G04-ACCOUNT-Q061
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A maintenance pass that re-applies reporting tags to historical tax-related lines changes only the tag
  attribution, never the underlying amount, account, date, or posted status of the line it touches.
WHY_IT_MATTERS: >
  A tag-maintenance pass overstepping into amounts or dates would silently rewrite closed financial history
  under the guise of routine maintenance.
DISCONFIRMING_OBSERVATION: >
  Running the tag-maintenance pass changes a historical line's amount, account, date, or posted status, not
  only its reporting tag.
EXPECTED_SURFACE: S1,S2,S6,S8
PRECONDITIONS: >
  Record the amount, account, date, and posted status of a set of historical lines, run the tag-maintenance
  pass, and compare before and after.
```

## G04-ACCOUNT-Q062

```yaml
QID: G04-ACCOUNT-Q062
MODULE: account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A consistency check over accounting data correctly fails on data that is genuinely inconsistent (for example
  an unbalanced entry reachable only through a bypassed path), and does not pass merely because the data was
  reachable only through a non-interactive path.
WHY_IT_MATTERS: >
  A check that only examines interactively created data would give false assurance while a bypass path silently
  corrupts the ledger.
DISCONFIRMING_OBSERVATION: >
  The consistency check reports no issue on data known to be inconsistent because that data was introduced
  through a non-interactive path the check does not examine.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Introduce a known inconsistency through a non-interactive path and run the consistency check to see whether
  it is detected.
```

---
## GMVQ Internal QA Checklist

- [x] 62 distinct MVQ records (exceeds the 48 floor; no padding — every record targets a distinct hypothesis).
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`.
- [x] Questions are behavioral and source-neutral; no vendor/product name, technical identifier, or module name
      appears in question text.
- [x] Approval / execution / posting separation represented (Q001-Q006).
- [x] Posting date / document date / tax point date represented (Q007-Q011).
- [x] Lock date / closed period vs late document, correction, reversal represented (Q012-Q017).
- [x] Reversal-as-restoration vs compensating entry, and audit trail, represented (Q018-Q022).
- [x] Cancellation of a posted document represented (Q023-Q025).
- [x] Document numbering under concurrency, failure, and per-company/branch series represented (Q026-Q032).
- [x] Rounding at line/document/tax level and the residual represented (Q033-Q036).
- [x] Multi-currency: rate at document vs payment, and where the difference lands, represented (Q037-Q041).
- [x] Journal integrity and debit/credit invariants represented (Q042-Q045).
- [x] Cross-company/branch attribution represented (Q046-Q048).
- [x] Who may post/unpost and traceability represented (Q049-Q050).
- [x] Reconciliation represented (Q051-Q053).
- [x] Financial report impact represented (Q054-Q055).
- [x] Tax basis / VAT / retroactive vs effective-dated rate change represented (Q056-Q058).
- [x] Withholding tax reconciliation to invoice and certificate trail represented (Q059-Q060).
- [x] Historical tag-maintenance pass boundary represented (Q061).
- [x] Inconsistency-check reachability (non-interactive bypass path) represented (Q062).
- [x] No specific Thai statutory rate, form number, or filing deadline asserted anywhere; every question
      depending on one carries `LEGAL_TAX_REVIEW_REQUIRED: YES`.
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
