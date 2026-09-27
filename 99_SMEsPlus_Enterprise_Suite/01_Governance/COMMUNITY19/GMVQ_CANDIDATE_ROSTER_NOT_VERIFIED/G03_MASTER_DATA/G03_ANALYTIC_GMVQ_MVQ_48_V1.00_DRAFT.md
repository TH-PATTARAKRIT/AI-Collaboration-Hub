# SMEsPlus ENTERPRISE SUITE
## GMVQ — G03 MASTER_DATA / analytic Module MVQ Bank

**Document ID:** GMVQ-G03-ANALYTIC-MVQ48-V1.00
**Group:** G03 MASTER_DATA
**Module Metadata:** `analytic`
**Wave:** W1
**Author Cell:** TEAM 14 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded

## Purpose

This bank supplies the module-specific MVQ set for the cost/profit reporting dimension
attached to transactions for management reporting (distribution across dimensions, plans
and hierarchies). It targets the accounting-adjacent material this group must cover:
distribution totals, post-close changes, archived dimension values still carrying history,
hierarchy rollup correctness, the one-way relationship to the financial ledger, cross-company
sharing, and auditability of re-allocation. Question text is source-neutral and does not
expose vendor names, field names, methods, schema, XML IDs, or API shapes.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because they test 48 distinct material hypotheses.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- Output remains source-neutral; `MODULE + QID` is a Research Evidence Join Key only.
- No Formal Coverage is derived from this bank.
- Produced under GMVQ_AUTHORING_STANDARD_V1.00 and GROUP_BRIEF_G03_MASTER_DATA.
- This bank is DRAFT / PREPARED ONLY. It is not approved, frozen, or verified.

## G03-ANALYTIC-Q001

```yaml
QID: G03-ANALYTIC-Q001
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a transaction amount is split across more than one cost/profit dimension value, the
  shares recorded against that transaction must sum to the full transaction amount, with any
  tolerance defined and enforced rather than silently accepted.
WHY_IT_MATTERS: >
  An unenforced total lets management reports overstate or understate cost/profit by
  dimension, misleading resource allocation decisions.
DISCONFIRMING_OBSERVATION: >
  A transaction is saved and posted with dimension shares that sum to materially more or less
  than 100% of the transaction amount, with no warning, block, or recorded tolerance rule.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Create a transaction eligible for dimension distribution, split it across three dimension
  values with shares that intentionally sum to 85%, and attempt to save and post it.
```

## G03-ANALYTIC-Q002

```yaml
QID: G03-ANALYTIC-Q002
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Changing the dimension distribution recorded against a transaction after that transaction
  has been posted to the financial ledger must not silently alter the posted ledger entry.
WHY_IT_MATTERS: >
  The management-reporting dimension is expected to ride alongside the ledger, not rewrite it
  after the fact; a silent change would break reconciliation between the two.
DISCONFIRMING_OBSERVATION: >
  Editing the dimension distribution on an already-posted transaction changes the debit/credit
  amount, account, or posting date of the underlying ledger entry.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a transaction with an initial dimension distribution, then edit the distribution shares
  or dimension values and re-check the ledger entry for that transaction.
```

## G03-ANALYTIC-Q003

```yaml
QID: G03-ANALYTIC-Q003
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A dimension value that is archived or deactivated while historical transactions still
  reference it must continue to display correctly on those historical transactions and their
  reports.
WHY_IT_MATTERS: >
  Losing the label or grouping on historical data after routine housekeeping would corrupt
  past management reports without any transaction ever changing.
DISCONFIRMING_OBSERVATION: >
  After a dimension value is archived, a historical transaction or report that references it
  shows a blank, an error, or a different dimension value in place of the original.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Post several transactions against a dimension value, archive that dimension value, then
  reopen the historical transactions and regenerate a report covering that period.
```

## G03-ANALYTIC-Q004

```yaml
QID: G03-ANALYTIC-Q004
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  An archived or deactivated dimension value must not be selectable for new transactions
  while remaining selectable for correcting or reversing existing ones that already reference
  it.
WHY_IT_MATTERS: >
  Blocking all use of an archived value, including corrections, forces awkward workarounds;
  allowing it for brand-new activity defeats the purpose of archiving.
DISCONFIRMING_OBSERVATION: >
  An archived dimension value either remains selectable on a brand-new, unrelated transaction,
  or becomes unselectable for reversing/correcting a transaction that already carries it.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Archive a dimension value already used on a posted transaction, then attempt both a new
  unrelated transaction and a reversal of the existing one.
```

## G03-ANALYTIC-Q005

```yaml
QID: G03-ANALYTIC-Q005
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A hierarchy of dimension values (parent/child groupings for rollup) must not allow a value
  to become its own ancestor, directly or through a chain.
WHY_IT_MATTERS: >
  A cyclical hierarchy would make rollup reporting loop indefinitely or silently produce wrong
  totals.
DISCONFIRMING_OBSERVATION: >
  A dimension value can be set as a descendant of itself, either directly or through a chain
  of intermediate parents, and the system accepts it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Build a three-level hierarchy of dimension values and attempt to set the top-level value's
  parent to one of its own descendants.
```

## G03-ANALYTIC-Q006

```yaml
QID: G03-ANALYTIC-Q006
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A rollup total shown at a parent dimension value must equal the sum of the amounts recorded
  against its children, at the moment the report is generated.
WHY_IT_MATTERS: >
  A mismatch between a summary figure and its detail undermines confidence in every report
  built on the hierarchy.
DISCONFIRMING_OBSERVATION: >
  A generated rollup report shows a parent total that does not equal the sum of its children's
  amounts for the same period, with no reconciling explanation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post transactions against several child dimension values under one parent, then generate a
  rollup report and manually sum the children's figures.
```

## G03-ANALYTIC-Q007

```yaml
QID: G03-ANALYTIC-Q007
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a cost/profit dimension is mandatory or optional can be configured per transaction
  type or per account, and that configuration is actually enforced at entry, not only
  documented.
WHY_IT_MATTERS: >
  A dimension declared mandatory but not enforced leaves gaps in management reporting that
  are discovered only after the fact.
DISCONFIRMING_OBSERVATION: >
  A transaction type or account configured to require a dimension value can be saved and
  posted with no dimension value assigned.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure one account or transaction type to require a dimension value, then attempt to
  post a transaction against it with the dimension left blank.
```

## G03-ANALYTIC-Q008

```yaml
QID: G03-ANALYTIC-Q008
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Cost/profit dimension plans and their values can be scoped to a single company/tenant or
  explicitly shared across companies, and a plan not marked as shared must not be usable
  outside its owning company.
WHY_IT_MATTERS: >
  An unintended cross-company leak of a dimension plan would mix one tenant's
  management-reporting structure into another's.
DISCONFIRMING_OBSERVATION: >
  A dimension plan or value created under one company appears as selectable, or is used, on
  a transaction belonging to a different company without an explicit sharing configuration.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Create a dimension plan restricted to Company A, then attempt to select or reference it
  from a transaction created under Company B.
```

## G03-ANALYTIC-Q009

```yaml
QID: G03-ANALYTIC-Q009
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Merging or consolidating two dimension values that both carry historical transaction
  history must preserve the full combined history under a single resulting value, not drop
  or duplicate it.
WHY_IT_MATTERS: >
  Silent loss or duplication of historical distribution during a merge would corrupt every
  downstream management report for prior periods.
DISCONFIRMING_OBSERVATION: >
  After merging two dimension values that each had posted history, the resulting value's
  total activity is less than, or more than, the sum of the two originals.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post distinct sets of transactions against two separate dimension values, merge them into
  one, and compare the combined total to the sum of the two originals.
```

## G03-ANALYTIC-Q010

```yaml
QID: G03-ANALYTIC-Q010
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A default dimension value inherited from a related master record (such as a product or
  partner) can be overridden on an individual transaction line, and that override is what is
  retained going forward.
WHY_IT_MATTERS: >
  If the inherited default keeps re-asserting itself, a deliberate manual correction on a
  transaction would be silently lost.
DISCONFIRMING_OBSERVATION: >
  A transaction line where the user manually overrides the inherited dimension value reverts
  to the inherited default after a save, a recompute, or a background pass.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Create a transaction line that inherits a default dimension value, manually override it,
  save, and trigger any recompute or background refresh available.
```

## G03-ANALYTIC-Q011

```yaml
QID: G03-ANALYTIC-Q011
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a distribution splits an amount across dimension values using percentages, rounding
  differences on any single transaction are absorbed in a deterministic, disclosed way rather
  than left to accumulate unassigned.
WHY_IT_MATTERS: >
  Undisclosed rounding leakage across many transactions can accumulate into a materially
  wrong reporting variance over a period.
DISCONFIRMING_OBSERVATION: >
  The sum of the rounded per-dimension amounts on a distributed transaction does not equal
  the original transaction amount, and no dimension value is assigned the rounding remainder.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split a transaction amount that does not divide evenly (for example, a three-way split of
  an odd-cent total) and inspect the resulting per-dimension figures.
```

## G03-ANALYTIC-Q012

```yaml
QID: G03-ANALYTIC-Q012
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Re-allocating an amount from one dimension value to another after the fact leaves a
  traceable record of the change, distinct from the original entry.
WHY_IT_MATTERS: >
  Without a trace, a reviewer cannot distinguish an originally correct distribution from one
  that was corrected later, undermining audit confidence in every historical report.
DISCONFIRMING_OBSERVATION: >
  A re-allocation between dimension values can be performed such that the original
  distribution and the correction are indistinguishable afterward, with no log, history
  record, or linked adjustment entry.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post a transaction with an initial distribution, perform a re-allocation to a different
  dimension value, and inspect available history/audit views for both states.
```

## G03-ANALYTIC-Q013

```yaml
QID: G03-ANALYTIC-Q013
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A single transaction line can require values from more than one independent dimension plan
  at once (for example, a department plan and a project plan together) without one plan's
  entry overwriting the other's.
WHY_IT_MATTERS: >
  Businesses commonly need to slice the same cost by more than one axis at once; collapsing
  them into one value loses one whole reporting dimension.
DISCONFIRMING_OBSERVATION: >
  Assigning a value from a second independent dimension plan to a transaction line clears or
  overwrites the value already assigned from the first plan.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Configure two independent dimension plans as applicable to the same transaction line,
  assign a value from each, and save.
```

## G03-ANALYTIC-Q014

```yaml
QID: G03-ANALYTIC-Q014
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A deactivated dimension plan (not just a single value within it) that is still referenced
  by a scheduled or recurring transaction template continues to be honoured until the
  template itself is updated, rather than silently dropping the dimension on the next
  generated occurrence.
WHY_IT_MATTERS: >
  A silent drop would produce a run of undimensioned transactions with no warning to the
  person who deactivated the plan.
DISCONFIRMING_OBSERVATION: >
  A recurring transaction template referencing a since-deactivated dimension plan generates
  its next occurrence with the dimension silently blank and no warning surfaced.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Set up a recurring transaction template using a dimension plan, deactivate that plan, and
  let or force the next scheduled occurrence to generate.
```

## G03-ANALYTIC-Q015

```yaml
QID: G03-ANALYTIC-Q015
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Access to view or edit cost/profit dimension detail on a transaction can be restricted
  independently from access to the transaction's core financial fields.
WHY_IT_MATTERS: >
  Management-reporting detail is often more sensitive or more widely shared than raw
  financial amounts; conflating the two permissions removes a control businesses expect.
DISCONFIRMING_OBSERVATION: >
  A user permission configuration that grants access to a transaction's core fields but
  withholds dimension detail still exposes the dimension detail, or vice versa.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure a role with access to transaction core fields but not dimension detail (or the
  reverse), then inspect what that role can actually see and edit.
```

## G03-ANALYTIC-Q016

```yaml
QID: G03-ANALYTIC-Q016
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Once a reporting period is closed/locked, the dimension distribution on transactions dated
  within that period cannot be edited through the normal entry path.
WHY_IT_MATTERS: >
  Allowing silent edits to a closed period's distribution would let management reports for a
  "final" period keep moving after stakeholders have already relied on them.
DISCONFIRMING_OBSERVATION: >
  A transaction dated inside a closed/locked period has its dimension distribution
  successfully changed through the normal entry path with no override or warning recorded.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Post a transaction, close/lock the period it falls in, and attempt to edit its dimension
  distribution through the standard entry screen.
```

## G03-ANALYTIC-Q017

```yaml
QID: G03-ANALYTIC-Q017
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A reversal or credit transaction generated against an original distributed transaction
  mirrors the original's dimension distribution rather than requiring it to be re-entered or
  leaving it blank.
WHY_IT_MATTERS: >
  A reversal that loses the original distribution breaks the ability to net the two entries
  out cleanly in a management report by dimension.
DISCONFIRMING_OBSERVATION: >
  A system-generated reversal or credit of a distributed transaction carries no dimension
  distribution, or a different one than the original, without user intervention.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a distributed transaction, then generate its standard reversal/credit and compare the
  dimension distribution on both.
```

## G03-ANALYTIC-Q018

```yaml
QID: G03-ANALYTIC-Q018
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Duplicating an existing transaction as a starting point for a new one carries over its
  dimension distribution by default, including references to any archived dimension values,
  without silently dropping them.
WHY_IT_MATTERS: >
  A user who duplicates a transaction expects the working defaults, including dimension
  detail, to come with it; a silent drop causes undimensioned activity to slip through.
DISCONFIRMING_OBSERVATION: >
  Duplicating a transaction whose original distribution referenced an archived dimension
  value produces a copy with the dimension silently cleared rather than carried over or
  flagged.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Archive a dimension value referenced on a posted transaction, then duplicate that
  transaction and inspect the resulting distribution.
```

## G03-ANALYTIC-Q019

```yaml
QID: G03-ANALYTIC-Q019
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A transaction created or imported through a non-interactive path (bulk import or an
  integration) is subject to the same dimension validation rules (required plans, valid
  values, totals) as one entered interactively.
WHY_IT_MATTERS: >
  A bypass through a non-interactive path would let bad or missing dimension data enter
  management reports while the interactive screen appears fully controlled.
DISCONFIRMING_OBSERVATION: >
  A transaction created through a bulk import or integration path is accepted with a missing
  required dimension, an invalid dimension value, or a distribution that does not sum
  correctly, where the same input would be rejected interactively.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Configure a required dimension and a distribution total rule, then submit an equivalent
  invalid case through the interactive screen and through a bulk/import or integration path.
```

## G03-ANALYTIC-Q020

```yaml
QID: G03-ANALYTIC-Q020
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A background/scheduled recompute of rollup or hierarchy totals reflects distribution
  changes made since the last run within a bounded, disclosed staleness window, rather than
  silently serving indefinitely stale figures.
WHY_IT_MATTERS: >
  An unbounded staleness window would let a manager act on a rollup report that no longer
  reflects reality with no indication that it is outdated.
DISCONFIRMING_OBSERVATION: >
  A rollup figure remains visibly unchanged well beyond the disclosed refresh interval after
  an underlying distribution change, with no staleness indicator shown.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Note the current rollup figure, change an underlying distribution, and observe how long it
  takes the rollup to reflect the change relative to any documented refresh interval.
```

## G03-ANALYTIC-Q021

```yaml
QID: G03-ANALYTIC-Q021
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Searching, filtering, or reporting by dimension value from one company/tenant's session
  cannot surface a dimension value's activity belonging to another company/tenant that has
  not explicitly shared it.
WHY_IT_MATTERS: >
  A cross-tenant leak through a search or filter path is as serious as one through direct
  record access, and is easy to overlook when testing only the create/edit screens.
DISCONFIRMING_OBSERVATION: >
  A search, filter, or report run from one company/tenant's context returns activity or
  totals belonging to a dimension value scoped to a different, non-sharing company/tenant.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Post transactions with distinct dimension values under two separate companies with no
  sharing configured, then run a cross-cutting search or report from each company's context.
```

## G03-ANALYTIC-Q022

```yaml
QID: G03-ANALYTIC-Q022
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Renaming a dimension value updates its label wherever it is referenced, including on
  historical reports regenerated after the rename, without altering the historical amounts
  themselves.
WHY_IT_MATTERS: >
  A rename is a labeling change only; if it silently alters amounts, or if it fails to
  propagate and produces inconsistent labels across reports, either failure undermines trust
  in the reporting.
DISCONFIRMING_OBSERVATION: >
  Renaming a dimension value changes a historical transaction's recorded amount, or produces
  inconsistent labels for the same underlying value across different reports generated after
  the rename.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post historical transactions against a dimension value, rename that value, and regenerate
  reports covering both the historical and current period.
```

## G03-ANALYTIC-Q023

```yaml
QID: G03-ANALYTIC-Q023
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Moving a dimension value to a different parent within the hierarchy after historical
  transactions were posted against it does not retroactively change which parent's rollup
  those historical transactions are counted under, unless an explicit re-statement is
  performed.
WHY_IT_MATTERS: >
  A structural reorganization of the hierarchy should not silently rewrite prior periods'
  reported totals by parent grouping.
DISCONFIRMING_OBSERVATION: >
  After a dimension value is moved to a new parent, a historical rollup report for a period
  before the move shows the value's prior activity now counted under the new parent instead
  of the original one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post transactions against a dimension value under Parent A, move that value under Parent B,
  then regenerate the rollup report for the period before the move.
```

## G03-ANALYTIC-Q024

```yaml
QID: G03-ANALYTIC-Q024
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Disabling the cost/profit dimension distribution feature entirely, mid-period, does not
  remove, hide, or corrupt the distribution already recorded on transactions posted before
  the feature was disabled.
WHY_IT_MATTERS: >
  A tenant that later re-enables the feature, or an auditor reviewing prior activity, needs
  the historical distribution intact regardless of the current feature toggle state.
DISCONFIRMING_OBSERVATION: >
  After the distribution feature is disabled and later re-enabled, previously recorded
  dimension distributions on posted transactions are missing, blank, or different from what
  was originally recorded.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Post distributed transactions, disable the distribution feature at the configuration level,
  then re-enable it and inspect the previously posted transactions.
```

## G03-ANALYTIC-Q025

```yaml
QID: G03-ANALYTIC-Q025
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two users editing the dimension distribution of the same transaction at the same time
  cannot both save conflicting distributions such that the transaction ends up with an
  inconsistent or partially-overwritten split.
WHY_IT_MATTERS: >
  A silent last-write-wins on a financially meaningful split can leave a transaction with a
  distribution nobody actually intended.
DISCONFIRMING_OBSERVATION: >
  Two concurrent edits to the same transaction's distribution both appear to succeed, but the
  saved result matches neither editor's intended split and no conflict is surfaced to either
  user.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Open the same transaction's distribution in two sessions, make differing changes in each,
  and save both in close succession.
```

## G03-ANALYTIC-Q026

```yaml
QID: G03-ANALYTIC-Q026
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Deleting a dimension value that still has historical transaction activity against it is
  either prevented outright, or handled through an archiving path that preserves the
  historical link, rather than allowing a hard delete that orphans historical distributions.
WHY_IT_MATTERS: >
  A hard delete of a referenced dimension value would leave historical reports pointing at
  nothing, silently corrupting past management data.
DISCONFIRMING_OBSERVATION: >
  A dimension value with existing historical transaction activity can be hard-deleted, and
  the historical transactions afterward show a missing, blank, or broken reference where the
  dimension value used to be.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post a transaction against a dimension value, then attempt to permanently delete that
  dimension value and inspect the historical transaction afterward.
```

## G03-ANALYTIC-Q027

```yaml
QID: G03-ANALYTIC-Q027
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The set of dimension plans applicable to a given transaction type is driven by
  configuration that is consistently enforced, not by which plans happen to have been used
  previously on similar transactions.
WHY_IT_MATTERS: >
  If applicability is inferred from history rather than configuration, two functionally
  identical transactions could end up requiring different dimensions depending on unrelated
  prior activity.
DISCONFIRMING_OBSERVATION: >
  Two transactions of the identical configured type present different sets of required or
  available dimension plans, with no configuration difference between them.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure one transaction type's applicable dimension plans, then create two separate
  transactions of that type from different starting contexts and compare the dimension plans
  each offers.
```

## G03-ANALYTIC-Q028

```yaml
QID: G03-ANALYTIC-Q028
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A budget or planned figure recorded against a dimension value for comparison purposes does
  not itself move when the actual transactions' distribution is later corrected, unless the
  correction is explicitly re-applied to the budget.
WHY_IT_MATTERS: >
  Conflating budget and actual through a shared dimension correction path would make a
  budget-vs-actual comparison meaningless, since the baseline would chase the actuals.
DISCONFIRMING_OBSERVATION: >
  Editing the distribution of an already-posted actual transaction changes the previously
  recorded budget/planned figure for the same dimension value and period.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a budget figure against a dimension value and period, post an actual transaction
  against the same dimension and period, then edit the actual transaction's distribution and
  re-check the budget figure.
```

## G03-ANALYTIC-Q029

```yaml
QID: G03-ANALYTIC-Q029
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A dimension plan configured as required for a given account or transaction type remains
  enforced consistently regardless of which module or entry point the transaction originates
  from.
WHY_IT_MATTERS: >
  If enforcement only applies to one entry point, a transaction created through a different
  path could silently bypass a control the business believes is universal.
DISCONFIRMING_OBSERVATION: >
  A transaction against an account configured to require a dimension can be posted without
  that dimension when entered from one origin/entry point, while the same account blocks it
  from another.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Configure a required dimension on an account, then attempt to post a transaction lacking
  that dimension from two different entry points that both post to the same account.
```

## G03-ANALYTIC-Q030

```yaml
QID: G03-ANALYTIC-Q030
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a transaction's total amount is corrected after distribution has already been
  applied, the distributed shares are recalculated or flagged for review rather than
  silently left summing to the old, now-incorrect total.
WHY_IT_MATTERS: >
  A stale distribution that no longer sums to the corrected transaction amount would
  misstate every dimension's reported share without any visible warning.
DISCONFIRMING_OBSERVATION: >
  A transaction's total amount is changed after distribution was applied, and the
  distributed shares remain unchanged and un-flagged even though they no longer sum to the
  new total.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a distribution to a transaction, then change the transaction's total amount and
  inspect whether the distribution shares are recalculated, flagged, or left stale.
```

## G03-ANALYTIC-Q031

```yaml
QID: G03-ANALYTIC-Q031
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a transaction that carried a dimension distribution removes or reverses that
  distribution's effect on rollup reporting in the same way it reverses the transaction's
  financial effect, rather than leaving the dimension total intact while the ledger effect
  is reversed.
WHY_IT_MATTERS: >
  A mismatch between the cancelled ledger effect and a still-standing dimension total would
  make the management report disagree with the books for the same event.
DISCONFIRMING_OBSERVATION: >
  After a distributed transaction is cancelled, its financial effect is reversed in the
  ledger but its amount still appears, unreversed, in the dimension rollup report.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a distributed transaction, cancel it through the standard cancellation path, and
  compare the ledger and the dimension rollup report afterward.
```

## G03-ANALYTIC-Q032

```yaml
QID: G03-ANALYTIC-Q032
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A dimension value's currency or company association, where applicable, is consistently
  applied when aggregating amounts across dimension values that belong to different
  currencies or companies, rather than summing raw figures without conversion.
WHY_IT_MATTERS: >
  Summing unconverted multi-currency amounts under one dimension total would produce a
  materially meaningless figure presented as if it were comparable.
DISCONFIRMING_OBSERVATION: >
  A rollup report combines amounts recorded in different currencies under a shared dimension
  value into a single total without any conversion or without disclosing that conversion was
  not applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post transactions in two different currencies against dimension values that roll up to the
  same parent, then generate the combined rollup report.
```

## G03-ANALYTIC-Q033

```yaml
QID: G03-ANALYTIC-Q033
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A dimension plan's structure (its hierarchy depth, allowed values) can be extended going
  forward without altering how previously posted transactions are already classified under
  the prior structure.
WHY_IT_MATTERS: >
  Evolving a reporting structure over time is normal business practice; if every structural
  change silently reclassifies history, no report from before the change remains
  reproducible.
DISCONFIRMING_OBSERVATION: >
  Adding a new level or value to a dimension plan's hierarchy changes how a previously
  posted transaction, unrelated to the addition, is classified or reported.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Post transactions under the existing dimension plan structure, extend the plan's hierarchy
  with a new level or branch, and regenerate a historical report covering the prior
  transactions.
```

## G03-ANALYTIC-Q034

```yaml
QID: G03-ANALYTIC-Q034
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An automated or templated distribution rule (a standing percentage split applied to a
  class of transactions) can be updated without retroactively re-splitting transactions that
  already applied the prior version of the rule.
WHY_IT_MATTERS: >
  Retroactive re-splitting on a template update would silently rewrite historical management
  figures every time a standing rule is revised for future use.
DISCONFIRMING_OBSERVATION: >
  Updating a standing distribution template's percentages changes the recorded distribution
  on transactions that were already posted under the prior version of the template.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Post transactions using a standing distribution template, update the template's
  percentages, and re-check the distribution recorded on the already-posted transactions.
```

## G03-ANALYTIC-Q035

```yaml
QID: G03-ANALYTIC-Q035
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A transaction line left with a partially completed distribution (some, but not all, of the
  amount allocated) is either blocked from posting or clearly flagged as incomplete, rather
  than posting silently with the unallocated remainder simply dropped.
WHY_IT_MATTERS: >
  A silently dropped remainder understates every dimension's reported share by an amount
  that never appears anywhere in the reporting.
DISCONFIRMING_OBSERVATION: >
  A transaction with a distribution allocating less than the full transaction amount posts
  successfully with the unallocated remainder simply absent from all dimension totals and
  with no flag.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enter a distribution that allocates only part of a transaction's amount across dimension
  values and attempt to post it.
```

## G03-ANALYTIC-Q036

```yaml
QID: G03-ANALYTIC-Q036
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A dimension value name or code can be safely reused within one company's plan without
  colliding with an identically named value that exists, deliberately unshared, under a
  different company.
WHY_IT_MATTERS: >
  If identical names across companies are internally treated as the same record,
  distribution intended for one company's reporting silently mixes into another's.
DISCONFIRMING_OBSERVATION: >
  Creating a dimension value with the same name/code as an existing unshared value in a
  different company causes the two to be treated as one record, or causes activity under one
  to appear under the other.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Create identically named, unshared dimension values under two separate companies, post
  transactions against each, and verify their totals remain separate.
```

## G03-ANALYTIC-Q037

```yaml
QID: G03-ANALYTIC-Q037
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A mass/bulk tool that reassigns many transactions from one dimension value to another
  produces the same auditable trail per affected transaction as a manual one-by-one
  reassignment would.
WHY_IT_MATTERS: >
  A bulk tool that skips the audit trail to save time creates an easy way to move large
  amounts of reported cost or profit between dimensions with no accountability.
DISCONFIRMING_OBSERVATION: >
  Transactions reassigned through a bulk/mass tool show no individual trace of the change,
  while the same reassignment done manually one at a time does produce a trace.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reassign a batch of transactions from one dimension value to another using any bulk/mass
  tool available, and compare the resulting audit trail to a manual single-transaction
  reassignment.
```

## G03-ANALYTIC-Q038

```yaml
QID: G03-ANALYTIC-Q038
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The list/summary view total for a dimension value and the detailed drill-down/report total
  for the same value and period always agree after a distribution edit, rather than one view
  reflecting the edit before the other.
WHY_IT_MATTERS: >
  Two disagreeing totals for the same figure, shown in two places in the same system,
  destroys trust in both without telling the user which one is correct.
DISCONFIRMING_OBSERVATION: >
  Immediately after editing a distribution, the summary/list total for the affected
  dimension value disagrees with the detailed drill-down total for the same value and
  period.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Edit the distribution on a transaction, then immediately compare the dimension's
  summary/list total against its detailed drill-down for the same period.
```

## G03-ANALYTIC-Q039

```yaml
QID: G03-ANALYTIC-Q039
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A rounding tolerance configured for distribution totals (how far short of, or over, 100%
  is accepted) applies consistently regardless of the number of dimension values a
  transaction is split across.
WHY_IT_MATTERS: >
  A tolerance that effectively loosens as more splits are added would let heavily split
  transactions carry a larger unexplained gap than simply split ones.
DISCONFIRMING_OBSERVATION: >
  A transaction split across many dimension values is accepted with a total further from
  100% than an otherwise identical transaction split across only two values, under the same
  configured tolerance.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a fixed rounding tolerance, then compare the maximum accepted deviation on a
  two-way split versus an eight-way split of an equivalent amount.
```

## G03-ANALYTIC-Q040

```yaml
QID: G03-ANALYTIC-Q040
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a dimension value that determines eligibility for a downstream process (such as
  inclusion in a specific management report or approval routing) is changed on a
  transaction, that transaction is re-evaluated against the downstream process rather than
  continuing to be treated under its original dimension.
WHY_IT_MATTERS: >
  A stale downstream classification would let a transaction keep bypassing or receiving a
  control that no longer matches its actual dimension.
DISCONFIRMING_OBSERVATION: >
  Changing a transaction's dimension value that governs a downstream report or routing rule
  does not change which downstream process the transaction is subject to.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Identify a downstream process keyed off a dimension value, change that value on an
  existing transaction, and check whether the downstream classification updates.
```

## G03-ANALYTIC-Q041

```yaml
QID: G03-ANALYTIC-Q041
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A hierarchy of dimension values has a bounded, disclosed maximum depth, and exceeding that
  depth is rejected explicitly rather than silently truncating the structure or degrading
  rollup accuracy.
WHY_IT_MATTERS: >
  Silent truncation at an undisclosed depth limit would make some parent totals quietly
  wrong with no indication to the user that the hierarchy exceeded a limit.
DISCONFIRMING_OBSERVATION: >
  Building a hierarchy beyond the documented depth limit is accepted, and the rollup for the
  excess levels is dropped, merged, or miscounted with no error shown.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Build a dimension hierarchy one level beyond any documented depth limit and inspect
  whether it is rejected or silently mishandled in the rollup.
```

## G03-ANALYTIC-Q042

```yaml
QID: G03-ANALYTIC-Q042
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Exporting transaction detail that includes dimension distribution respects the same
  access restriction on dimension visibility that applies to viewing it on-screen, rather
  than exposing full detail through the export path alone.
WHY_IT_MATTERS: >
  A restriction enforced only in the interface and not in export/reporting paths is not a
  real restriction; it simply moves the leak to a less obvious path.
DISCONFIRMING_OBSERVATION: >
  A user restricted from viewing dimension detail on-screen can obtain that same detail
  through a generic export or reporting function.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Restrict a role from viewing dimension detail, then have that role attempt a generic
  export or report covering the same transactions.
```

## G03-ANALYTIC-Q043

```yaml
QID: G03-ANALYTIC-Q043
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A correction that re-allocates part of one transaction's distribution to a different
  dimension value is represented as its own traceable adjustment rather than as a silent
  edit of the original transaction's stored distribution record.
WHY_IT_MATTERS: >
  If a correction overwrites the original record in place, an auditor comparing a report
  generated before the correction to the current data has no way to know the underlying data
  changed at all.
DISCONFIRMING_OBSERVATION: >
  A re-allocation correction updates the original transaction's stored distribution record
  in place with no separate adjustment record, entry, or version retained.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post a transaction with a distribution, perform a re-allocation correction, and check
  whether the original record is overwritten or a distinct adjustment is created.
```

## G03-ANALYTIC-Q044

```yaml
QID: G03-ANALYTIC-Q044
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Restoring a previously archived/deactivated dimension value returns it to active use with
  its historical link to prior transactions intact, without requiring those historical
  transactions to be re-linked manually.
WHY_IT_MATTERS: >
  If reactivation breaks the historical link, a routine archive-then-restore cycle would
  permanently sever a value from its own history.
DISCONFIRMING_OBSERVATION: >
  After a dimension value is archived and then reactivated, historical transactions that
  referenced it before archiving no longer show the correct link to it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post transactions against a dimension value, archive it, reactivate it, and verify the
  historical transactions still reference it correctly.
```

## G03-ANALYTIC-Q045

```yaml
QID: G03-ANALYTIC-Q045
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A dimension plan or value marked shared across companies can still be restricted from use
  on certain transaction types or accounts on a per-company basis, rather than sharing being
  all-or-nothing.
WHY_IT_MATTERS: >
  Businesses often want a shared reporting structure with per-company exceptions; an
  all-or-nothing sharing model forces either full exposure or full duplication of the
  structure.
DISCONFIRMING_OBSERVATION: >
  Attempting to restrict a shared dimension plan or value from a specific transaction type
  or account within one company has no effect, and it remains fully available there
  regardless of the restriction.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Mark a dimension plan as shared across companies, then attempt a per-company restriction
  on one transaction type or account and verify it is honoured.
```

## G03-ANALYTIC-Q046

```yaml
QID: G03-ANALYTIC-Q046
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A transaction posted using a dimension value that is later found to have been entered
  against the wrong plan (a value from an unrelated dimension plan mistakenly applied) can
  be corrected without requiring the original ledger entry to be reversed and re-posted from
  scratch.
WHY_IT_MATTERS: >
  If the only correction path is a full reversal and re-post, minor dimension miscoding
  becomes disproportionately expensive to fix, discouraging correction.
DISCONFIRMING_OBSERVATION: >
  Correcting a dimension value mistakenly assigned from the wrong plan is only possible by
  reversing and re-posting the entire underlying financial transaction, with no lighter
  correction path available.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a transaction with a dimension value taken from the wrong plan by mistake, and
  attempt to correct just the dimension assignment.
```

## G03-ANALYTIC-Q047

```yaml
QID: G03-ANALYTIC-Q047
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A note, memo, or free-text field attached to a specific distribution line is preserved
  when that line's dimension value or share is edited, rather than being cleared as a side
  effect of the edit.
WHY_IT_MATTERS: >
  Losing an explanatory note whenever the underlying figure is corrected removes exactly the
  context a reviewer would need to understand why the correction was made.
DISCONFIRMING_OBSERVATION: >
  Editing the dimension value or share on a distribution line clears an existing note/memo
  attached to that line, even though the note itself was not edited.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attach a note to a distribution line, then edit the line's dimension value or share and
  check whether the note survives.
```

## G03-ANALYTIC-Q048

```yaml
QID: G03-ANALYTIC-Q048
MODULE: analytic
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A user's ability to create or edit dimension plans and hierarchy structure (a
  configuration-level action) is governed by a distinct permission from the ability to
  merely assign an existing dimension value on a transaction (a data-entry-level action).
WHY_IT_MATTERS: >
  Conflating the two would let ordinary transaction-entry staff restructure the company's
  whole reporting hierarchy, or block them from routine entry until they are granted
  configuration rights.
DISCONFIRMING_OBSERVATION: >
  A role granted only transaction-entry rights can create, edit, or restructure dimension
  plans and hierarchy, or a role granted only configuration rights is blocked from assigning
  an existing dimension value on a transaction.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure two roles, one with only transaction-entry rights and one with only
  dimension-configuration rights, and test each against both kinds of action.
```

