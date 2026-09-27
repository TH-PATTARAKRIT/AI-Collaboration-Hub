# SMEsPlus ENTERPRISE SUITE
## GMVQ — G04 ACCOUNT_BASE / l10n_account_withholding_tax Module MVQ Bank

**Document ID:** GMVQ-G04-L10N_ACCOUNT_WITHHOLDING_TAX-MVQ48-V1.00
**Group:** G04 ACCOUNT_BASE
**Module Metadata:** `l10n_account_withholding_tax`
**Wave:** W1
**Author Cell:** TEAM 23 (GMVQ Question Factory — Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN / REVISED R1
**CHANGE_REASON (R1):** Returned by GMVQ MASTER AUDIT TEAM M4 under Boss directive SMEPLUS-GMVQ-20P-5AUDIT-20260927-004 — closed-vocabulary (RISK_TIER / OUTPUT_CLASS) field-value defect(s) corrected by production (R1). 1 RISK_TIER value (LOW) outside the enum re-tiered to MEDIUM.
**actual_mvq_count:** 48

## Purpose
This bank supplies the module-specific research questions for `l10n_account_withholding_tax`
— tax withheld at payment time by the payer on behalf of the payee. It is written for a blind
two-lane study: Lane A reads reference source, Lane B observes a running system, and neither
sees the other's answers. Question text is source-neutral throughout.

## Control
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread
  across invoice/payment timing and period straddling, partial payment, one payment covering
  several invoices or one invoice across several payments, over/under-withholding correction,
  the computation base, currency and rounding, reversal of a withholding-bearing payment,
  reconciliation against the amount payable to the authority and the certificate issued,
  the certificate's own numbering sequence, and authorization to change attribution after
  posting.
- Per the group brief's Thai-tax prohibition, no question asserts a specific statutory rate,
  form number, or filing deadline. Every question whose hypothesis depends on such a rule is
  written behaviourally and carries `LEGAL_TAX_REVIEW_REQUIRED: YES`.
- This bank is DRAFT authoring output only. Not approved, not frozen, not verified.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived here.

---

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q001

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q001
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LEGAL_TAX_REVIEW_REQUIRED: YES
HYPOTHESIS: >
  When the configured statutory rate in force at invoice time differs from the configured
  statutory rate in force at payment time, the amount withheld is computed using the rate in
  force at the tax point the withholding obligation is actually anchored to, not whichever
  rate happens to be current when the entry is keyed.
WHY_IT_MATTERS: >
  Anchoring to the wrong point in time misstates the withheld amount even when every
  individual rate value used was, at some moment, correct.
DISCONFIRMING_OBSERVATION: >
  With two different configured rates in force at invoice time and at payment time, the
  withheld amount matches neither rate applied consistently to a single, defensible tax
  point, or the choice of tax point is not evident from the record.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure two different statutory rate values effective on either side of a date, create an
  invoice before that date, and pay it after, then inspect which rate was actually applied.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q002

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q002
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an invoice and its payment fall in different accounting periods, the withholding
  obligation is recognized in a single, determinate period rather than being ambiguous
  between the two.
WHY_IT_MATTERS: >
  An ambiguous period assignment can cause a withholding obligation to be reported in both
  periods, or in neither.
DISCONFIRMING_OBSERVATION: >
  The withholding entry's recognized period cannot be determined unambiguously, or differs
  depending on which report is used to look at it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an invoice in one accounting period and pay it in the next, then check which single
  period the resulting withholding entry is recognized in across all available views.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q003

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q003
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A payment made after the accounting period containing its invoice has been locked or
  closed produces a defined, visible outcome — blocked, redirected to the current period, or
  otherwise flagged — rather than an unhandled failure.
WHY_IT_MATTERS: >
  A closed period exists specifically to prevent silent changes to reported figures; a
  withholding entry landing there unremarked defeats that control.
DISCONFIRMING_OBSERVATION: >
  Posting a payment against an invoice from a locked or closed prior period succeeds with no
  indication of how the period conflict was resolved.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Lock or close the accounting period containing an invoice, then attempt to post a payment
  against that invoice that would generate a withholding entry.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q004

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q004
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A payment awaiting its withholding determination is held in a distinguishable intermediate
  state, and there is an observable event that moves it to determined.
WHY_IT_MATTERS: >
  Without a distinguishable intermediate state, a payment could be treated as fully settled
  before its withholding consequence is actually known.
DISCONFIRMING_OBSERVATION: >
  A payment that has not yet had its withholding determined is indistinguishable, in status,
  from one that has.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a payment scenario where withholding determination might be delayed and inspect
  whether an intermediate status exists and what event resolves it.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q005

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q005
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A payment cannot be posted to completion while its withholding determination is still
  outstanding, without at least an explicit acknowledgement that no withholding entry was
  created.
WHY_IT_MATTERS: >
  A payment that silently completes without its withholding leaves an obligation untracked
  with no trace that anything was skipped.
DISCONFIRMING_OBSERVATION: >
  A payment posts to completion with no withholding entry and no record indicating that
  withholding was skipped, deferred, or found not applicable.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Construct a payment scenario where withholding would normally apply, interrupt or bypass
  the determination step if possible, and observe whether posting still completes silently.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q006

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q006
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a payment's tax point date and its posting date fall on opposite sides of a period
  close, that combination is either prevented or explicitly flagged, rather than accepted
  silently.
WHY_IT_MATTERS: >
  An unflagged mismatch between the date that fixes the tax treatment and the date the entry
  actually lands in can misstate which period bears the obligation.
DISCONFIRMING_OBSERVATION: >
  A payment with a tax point date before a period close and a posting date after it is
  accepted with no warning, block, or flag referencing the mismatch.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Construct a payment whose tax point date and posting date straddle a period close and
  attempt to post it.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q007

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q007
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A partial payment against an invoice computes withholding on the amount actually paid,
  not on the full invoice amount.
WHY_IT_MATTERS: >
  Withholding on the full amount when only part has been paid over-withholds against the
  payee on every partial payment.
DISCONFIRMING_OBSERVATION: >
  A partial payment for a fraction of an invoice's total produces a withholding amount
  computed as though the full invoice had been paid.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Pay a known fraction of an invoice's total and inspect the withholding amount computed for
  that partial payment.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q008

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q008
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Each of several sequential partial payments against the same invoice carries its own
  separately computed and individually traceable withholding amount.
WHY_IT_MATTERS: >
  Merging partial payments' withholding into one undifferentiated total prevents tracing any
  single payment's actual contribution.
DISCONFIRMING_OBSERVATION: >
  After several partial payments, the withholding amount attributable to any one specific
  partial payment cannot be individually identified.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Make three or more partial payments against one invoice and attempt to trace the
  withholding amount specific to each.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q009

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q009
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The sum of withholding computed across all partial payments that fully settle an invoice
  equals, within a defined and traceable rounding tolerance, what a single full payment
  would have withheld.
WHY_IT_MATTERS: >
  An unexplained gap between the two paths means partial-payment handling is quietly
  under- or over-withholding relative to the single-payment case.
DISCONFIRMING_OBSERVATION: >
  The cumulative withholding across all partial payments differs from the single-payment
  equivalent by more than a documented rounding tolerance, with no explanation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Fully settle one invoice through several partial payments and, separately, an identical
  invoice through one full payment, then compare cumulative withholding.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q010

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q010
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a partial payment that already generated a withholding entry, before further
  partial payments are made, removes or clearly reverses that withholding entry rather than
  leaving it standing against a payment that no longer exists.
WHY_IT_MATTERS: >
  An orphaned withholding entry left after its payment is cancelled overstates the amount
  withheld with no valid payment behind it.
DISCONFIRMING_OBSERVATION: >
  Cancelling a partial payment leaves its associated withholding entry in place, unreversed,
  attached to a payment that no longer exists.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Make a partial payment that generates a withholding entry, cancel that payment, and
  inspect the state of the withholding entry.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q011

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q011
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  For any one invoice, a reviewer can trace every partial payment's individual withholding
  contribution back to that specific invoice, not merely to the payee in general.
WHY_IT_MATTERS: >
  A trail that only reaches the payee, not the specific invoice, cannot support a
  document-level reconciliation.
DISCONFIRMING_OBSERVATION: >
  Given one invoice paid through several partial payments, the recorded trail links the
  withholding amounts to the payee but not distinctly to that one invoice.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Settle one invoice through several partial payments and attempt to reconstruct, from the
  records alone, the withholding tied to that specific invoice.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q012

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q012
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A single payment covering multiple invoices allocates the total withholding across those
  invoices in a proportion that is visible and reconcilable, not an opaque single total.
WHY_IT_MATTERS: >
  An opaque total cannot be checked against each invoice's own liability, and cannot be
  reconciled invoice by invoice later.
DISCONFIRMING_OBSERVATION: >
  A payment covering several invoices produces one withholding total with no visible
  breakdown of how much is attributed to each invoice.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Make one payment covering two or more invoices and inspect whether the resulting
  withholding is broken down per invoice.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q013

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q013
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a single payment covers invoices with different withholding liability (one liable,
  one not), withholding is computed per invoice according to each invoice's own liability,
  not applied uniformly across the whole payment.
WHY_IT_MATTERS: >
  Applying one liability determination to a mixed batch either over-withholds on the
  non-liable invoice or under-withholds on the liable one.
DISCONFIRMING_OBSERVATION: >
  A payment covering one withholding-liable invoice and one non-liable invoice applies the
  same withholding treatment to both.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Combine one withholding-liable and one non-liable invoice into a single payment and inspect
  the treatment applied to each.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q014

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q014
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing how a posted payment's amount is allocated across its covered invoices produces a
  corresponding, visible change to the per-invoice withholding attribution, rather than
  leaving it tied to the original, now-superseded allocation.
WHY_IT_MATTERS: >
  Withholding attribution that silently disagrees with the current allocation misstates which
  invoice the withholding actually relates to.
DISCONFIRMING_OBSERVATION: >
  After a payment's invoice allocation is changed, the per-invoice withholding still reflects
  the original allocation with no update and no flag.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Change the invoice allocation on a posted payment that generated per-invoice withholding
  and inspect whether the withholding attribution follows.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q015

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q015
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When one invoice is settled across several separate payments over time, the mechanism
  prevents the cumulative withholding across all of them from exceeding what that invoice's
  full amount would generate in a single payment.
WHY_IT_MATTERS: >
  Without a cumulative check, treating each payment independently can over-withhold on an
  invoice paid off gradually.
DISCONFIRMING_OBSERVATION: >
  An invoice settled through several separate payments accumulates total withholding
  exceeding the single-payment equivalent, with nothing preventing or flagging it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Settle one invoice through several separate payments spaced over time and compare the
  cumulative withholding against the single-payment equivalent.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q016

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q016
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two payments processed at nearly the same time against overlapping invoices for the same
  partner do not each compute withholding as though the other had not yet happened, producing
  an inconsistent combined result.
WHY_IT_MATTERS: >
  A race between concurrent payments against shared invoices can double-count or
  under-count the remaining liable amount.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous payments against overlapping invoices for one partner produce a
  combined withholding total inconsistent with processing them one after the other.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Submit two payments in close succession against overlapping invoices for the same partner
  and compare the combined result to a sequential run of the same payments.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q017

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q017
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When under-withholding is discovered after posting, a corrective path exists that does not
  require reversing the entire original payment to fix only the withheld amount.
WHY_IT_MATTERS: >
  Forcing a full reversal for a narrow correction multiplies the number of entries touched
  and the risk of introducing new errors while fixing the first one.
DISCONFIRMING_OBSERVATION: >
  The only available way to correct an under-withheld amount is to reverse the entire
  original payment, with no narrower corrective path available.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Post a payment with a deliberately understated withholding amount and attempt to correct
  just the withheld amount without reversing the whole payment.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q018

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q018
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Correcting an over-withheld amount posts the adjustment to an identifiable account and
  entry, distinguishable from an ordinary new withholding transaction.
WHY_IT_MATTERS: >
  An adjustment that looks like an ordinary new withholding event cannot later be told apart
  from one, muddying reconciliation.
DISCONFIRMING_OBSERVATION: >
  A correction for over-withholding posts as an entry indistinguishable in kind from an
  ordinary new withholding transaction.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a payment with a deliberately overstated withholding amount, correct it, and inspect
  how the correcting entry is distinguished from an ordinary transaction.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q019

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q019
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Correcting a posted withholding amount also flags or updates any certificate reference tied
  to it, rather than leaving a certificate that no longer matches the corrected amount
  unremarked.
WHY_IT_MATTERS: >
  A certificate that silently disagrees with the corrected books misleads the payee and
  anyone relying on the certificate as proof of what was withheld.
DISCONFIRMING_OBSERVATION: >
  A withholding amount is corrected while its associated certificate reference is left
  showing the pre-correction amount with no flag of the mismatch.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Correct a posted withholding amount that already has an associated certificate reference
  and inspect whether the certificate reference reflects or flags the change.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q020

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q020
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Correcting a withholding amount on a payment that has already posted requires an
  authorization distinct from ordinary payment entry.
WHY_IT_MATTERS: >
  If any ordinary user can correct posted tax-relevant amounts unremarked, the posting
  control provides no real separation of duties.
DISCONFIRMING_OBSERVATION: >
  A user holding only ordinary payment-entry rights can correct a posted withholding amount
  with no additional authorization step.
EXPECTED_SURFACE: S2,S4
PRECONDITIONS: >
  As a user with only ordinary payment-entry rights, attempt to correct a posted withholding
  amount.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q021

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q021
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A corrected withholding amount is recorded with an explicit link back to the original
  erroneous entry it corrects, not as an unrelated new entry a reviewer must guess the
  connection for.
WHY_IT_MATTERS: >
  Without an explicit link, a reviewer reconciling withholding cannot tell a correction from
  an unrelated additional transaction.
DISCONFIRMING_OBSERVATION: >
  A correcting entry for a withholding amount carries no field or reference connecting it
  back to the entry it corrects.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Correct a posted withholding amount and inspect the correcting entry for an explicit link
  to the original entry.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q022

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q022
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Whether withholding is computed on the gross document amount or on an amount net of
  another tax already applied to the same document is a consistent, documented rule, not a
  behaviour that varies unexplained by document.
WHY_IT_MATTERS: >
  An inconsistent base silently changes the withheld amount by the value of the other tax,
  in either direction, without anyone deciding that outcome.
DISCONFIRMING_OBSERVATION: >
  Two otherwise comparable documents, both carrying another tax alongside withholding,
  compute the withholding base inconsistently (one gross, one net) with no documented rule
  explaining the difference.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Create two comparable documents that each carry withholding alongside another tax and
  compare the base each uses for the withholding computation.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q023

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q023
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A document whose lines individually differ in withholding liability computes withholding
  per qualifying line, not across the document's total amount.
WHY_IT_MATTERS: >
  A document-wide computation on a mixed document either withholds on non-liable lines or
  misses part of the liable ones.
DISCONFIRMING_OBSERVATION: >
  A document with one withholding-liable line and one non-liable line computes withholding
  as a function of the whole document total rather than the liable line alone.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a document with a withholding-liable line and a non-liable line and inspect the
  resulting withholding base.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q024

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q024
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A configuration change to whether the withholding base is gross or net applies only to
  documents created after the change, not retroactively to open documents created under the
  prior configuration.
WHY_IT_MATTERS: >
  Retroactive reinterpretation of the base for already-open documents can silently change
  amounts the business already committed to.
DISCONFIRMING_OBSERVATION: >
  Changing the base configuration alters the computed withholding on a document that was
  already open and unposted under the prior configuration, without an explicit
  re-evaluation action.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Create an open, unposted document under one base configuration, change the configuration,
  and re-open the document to see whether its computed base changed.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q025

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q025
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A document combining withholding-liable and non-liable lines never includes the
  non-liable portion in the amount used to compute withholding.
WHY_IT_MATTERS: >
  Including a non-liable line in the base over-withholds against the payee on an amount that
  was never subject to withholding.
DISCONFIRMING_OBSERVATION: >
  The computed withholding base on a mixed document includes any portion attributable to a
  non-liable line.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Build a document mixing a withholding-liable and a clearly non-liable line and verify
  exactly which amount the withholding is computed against.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q026

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q026
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Adjusting a document line's amount after the withholding base was first computed
  recomputes the withholding, rather than leaving a stale amount based on the pre-adjustment
  line value.
WHY_IT_MATTERS: >
  A stale withholding amount left after a line adjustment misstates the amount actually owed
  against the current document.
DISCONFIRMING_OBSERVATION: >
  Adjusting a withholding-liable line's amount leaves the previously computed withholding
  unchanged and unflagged as stale.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Compute withholding on a document, then adjust the amount of a liable line, and inspect
  whether the withholding recomputes.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q027

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q027
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LEGAL_TAX_REVIEW_REQUIRED: YES
HYPOTHESIS: >
  For a foreign-currency invoice whose withholding is computed and remitted in local
  currency, the exchange rate applied is the one specified by the configured statutory rule
  governing which rate to use, and that choice is consistent for every such document rather
  than an incidental side effect of whichever rate happened to be cached.
WHY_IT_MATTERS: >
  Using an inconsistent or unintended rate misstates the local-currency amount withheld and
  remitted, independent of the correctness of the invoice's own currency conversion.
DISCONFIRMING_OBSERVATION: >
  Two otherwise comparable foreign-currency documents produce local-currency withholding
  amounts computed from visibly different exchange-rate bases, with no configured rule
  explaining the difference.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Create a foreign-currency invoice and pay it on a date with a different prevailing rate,
  then determine which rate the local-currency withholding amount was actually computed
  from.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q028

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q028
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Rounding of the withheld amount is applied at one clearly defined level (line or document),
  and the resulting residual difference is posted to an identifiable place rather than
  silently absorbed into the withheld amount itself.
WHY_IT_MATTERS: >
  An unidentified residual silently changes the withheld amount by a rounding artefact that
  no one can locate later.
DISCONFIRMING_OBSERVATION: >
  A rounding residual from the withholding computation cannot be located in any specific
  account or line, and the withheld amount does not match a direct computation from the
  documented rate and base.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct a document whose withholding computation produces a rounding residual and trace
  where that residual is posted.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q029

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q029
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Rounding differences accumulated across many small payments to the same payee over time
  are tracked in a way that lets the accumulated drift be identified, rather than
  disappearing unaccounted into the withheld totals.
WHY_IT_MATTERS: >
  Small per-payment rounding differences can compound into a material, unexplained drift
  over a large volume of payments.
DISCONFIRMING_OBSERVATION: >
  After many small payments to one payee, no mechanism or report identifies the accumulated
  rounding drift separately from the underlying withheld amounts.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Process a large number of small payments to one payee that each produce a small rounding
  difference and look for any accumulated-drift tracking.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q030

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q030
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A currency-rate correction applied after a withholding entry has posted results in a
  visible restatement of the withheld amount, or an explicit decision not to restate it,
  rather than an unremarked, unexplained discrepancy.
WHY_IT_MATTERS: >
  A silent discrepancy between the posted amount and what the corrected rate implies leaves
  the books internally inconsistent with no explanation.
DISCONFIRMING_OBSERVATION: >
  After a currency-rate correction, the posted withholding amount disagrees with what the
  corrected rate implies, with no restatement and no documented decision not to restate.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a foreign-currency withholding entry, then apply a correction to the exchange rate
  used, and check whether and how the withheld amount responds.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q031

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q031
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a payment amount is small enough that the computed withholding rounds to zero, a
  traceable record of the computation still exists, rather than the withholding step being
  silently skipped with no trace it was even considered.
WHY_IT_MATTERS: >
  A silently skipped computation is indistinguishable from a computation that was simply
  never run, which weakens the audit trail for small transactions.
DISCONFIRMING_OBSERVATION: >
  For a payment whose computed withholding rounds to zero, no record exists showing that a
  withholding computation was performed and produced zero, as opposed to never running at
  all.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Process a payment small enough that its computed withholding rounds to zero and look for a
  record of the computation having occurred.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q032

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q032
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reversing a posted payment that carried a withholding entry produces an outcome (full
  restoration to the pre-withholding state, or a distinct compensating entry) that is
  determinate and shown clearly in the audit trail, rather than left ambiguous as to which
  occurred.
WHY_IT_MATTERS: >
  An ambiguous reversal leaves a reviewer unable to tell whether the withholding obligation
  was actually undone or merely offset, which changes what remains owed to the authority.
DISCONFIRMING_OBSERVATION: >
  Reversing a withholding-bearing payment leaves the audit trail unclear as to whether the
  original withholding state was restored or a separate compensating entry was created.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a payment that generates a withholding entry, reverse the payment, and determine from
  the audit trail alone which reversal mechanism occurred.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q033

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q033
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A withholding certificate already issued for a payment that is subsequently reversed
  transitions to an explicit voided or superseded status, rather than remaining as though it
  were still current.
WHY_IT_MATTERS: >
  A payee holding a certificate that the payer has since invalidated, with no corresponding
  status change, has documentary proof of an amount that no longer reflects the books.
DISCONFIRMING_OBSERVATION: >
  Reversing a payment whose withholding certificate was already issued leaves that
  certificate showing an active, current status with no void or supersession indicated.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Issue a withholding certificate for a payment, then reverse the payment, and inspect the
  certificate's resulting status.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q034

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q034
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a payment consists of multiple withholding-bearing components, one component's
  withholding can be reversed on its own without forcing the reversal of the entire
  underlying payment.
WHY_IT_MATTERS: >
  Requiring a full payment reversal to fix one component multiplies the scope of every
  correction beyond what the actual error requires.
DISCONFIRMING_OBSERVATION: >
  A payment with multiple withholding-bearing components cannot have one component's
  withholding reversed without reversing the payment in its entirety.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Construct a payment with more than one withholding-bearing component and attempt to
  reverse just one component's withholding.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q035

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q035
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reversing a withholding-bearing payment has a defined, consistent effect on the
  certificate numbering sequence — either the number is retired or it is available for
  reuse — rather than an effect that differs unpredictably by case.
WHY_IT_MATTERS: >
  An unpredictable effect on the numbering sequence makes the sequence's own integrity
  unverifiable.
DISCONFIRMING_OBSERVATION: >
  Reversing two comparable withholding-bearing payments, each with an issued certificate,
  produces different outcomes for the certificate number in each case with no rule
  explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Reverse two comparable withholding-bearing payments that each had an issued certificate
  and compare what happens to each certificate number.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q036

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q036
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The reversal of a withholding-bearing payment is linked, bidirectionally, to the original
  entry: the original shows it was reversed and the reversal shows what it reverses.
WHY_IT_MATTERS: >
  A one-directional link leaves half of any audit trace unreachable, depending which entry
  a reviewer starts from.
DISCONFIRMING_OBSERVATION: >
  Starting from either the original withholding entry or its reversal, the other cannot be
  reached through an explicit reference.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reverse a withholding-bearing payment and check, from each of the two resulting entries,
  whether the other is explicitly referenced.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q037

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q037
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  For any given period, the sum of withholding recorded across all payments to a payee
  reconciles exactly to the amount recorded as payable to the tax authority for that payee
  and period.
WHY_IT_MATTERS: >
  A gap between the two figures means either an obligation has gone unrecorded or an amount
  has been recorded that no underlying payment supports.
DISCONFIRMING_OBSERVATION: >
  For a chosen period and payee, the total withheld across payments and the amount recorded
  as payable to the authority do not match, with no reconciling explanation available.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  For one payee and period, total the withholding recorded across all payments and compare
  it against the recorded amount payable to the tax authority.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q038

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q038
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A discrepancy between the amount actually withheld and the amount stated on the
  certificate issued to the payee is detectable through a built-in check, not only through a
  manual side-by-side comparison an operator has to think to run.
WHY_IT_MATTERS: >
  Relying on manual comparison for a mismatch this consequential means it typically goes
  undetected until the payee or the authority raises it.
DISCONFIRMING_OBSERVATION: >
  A deliberately engineered discrepancy between the withheld amount and the certificate
  amount is not surfaced by any built-in check, only found by manual comparison.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Engineer a case where the certificate amount and the actually withheld amount diverge and
  look for a built-in check that would surface it.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q039

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q039
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LEGAL_TAX_REVIEW_REQUIRED: YES
HYPOTHESIS: >
  A certificate cannot be issued referencing a payment that has not yet completed posting;
  the sequencing required by the configured statutory rule is enforced, not merely
  documented as expected practice.
WHY_IT_MATTERS: >
  A certificate issued ahead of the payment it documents can state an amount that the books
  do not yet, or may never, actually support.
DISCONFIRMING_OBSERVATION: >
  A certificate can be generated and issued referencing a payment that has not completed
  posting, with no block or warning about the out-of-order sequencing.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Attempt to issue a certificate for a payment that has not yet completed posting.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q040

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q040
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  For a given period, a reviewer can reconcile every certificate issued against the
  corresponding payable-to-authority balance using records internal to the system, without
  needing to build a manual cross-reference outside it.
WHY_IT_MATTERS: >
  If reconciliation requires an external manual cross-reference, the reconciliation is only
  as reliable as whoever remembers to build and maintain that external artefact.
DISCONFIRMING_OBSERVATION: >
  Reconciling issued certificates against the payable-to-authority balance for a period
  cannot be done from records internal to the system without external manual
  cross-referencing.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  For one period, attempt to reconcile all issued certificates against the payable-to-
  authority balance using only records available inside the system.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q041

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q041
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The certificate numbering sequence is maintained independently of the payment and invoice
  numbering sequences, and this separation holds even when certificates are issued
  concurrently with other document types.
WHY_IT_MATTERS: >
  A numbering sequence that is not truly independent can develop unexplained gaps or
  collisions the moment it is stressed under concurrent activity.
DISCONFIRMING_OBSERVATION: >
  Concurrent issuance of certificates alongside other document types produces a gap,
  collision, or cross-contamination between the certificate sequence and another document's
  sequence.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Issue certificates concurrently with other document types being created and inspect the
  certificate sequence for gaps or collisions.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q042

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q042
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LEGAL_TAX_REVIEW_REQUIRED: YES
HYPOTHESIS: >
  A gap or a reused number in the certificate sequence is detectable through an available
  check, given that the configured statutory rule requires the sequence to be gapless and
  non-reused.
WHY_IT_MATTERS: >
  An undetectable gap or reuse defeats the purpose of a sequence requirement meant to prove
  completeness to the authority.
DISCONFIRMING_OBSERVATION: >
  A deliberately introduced gap or reused number in the certificate sequence is not
  detectable through any available check or report.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Engineer a gap or a reused number in the certificate sequence and attempt to detect it
  using only available checks or reports.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q043

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q043
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LEGAL_TAX_REVIEW_REQUIRED: YES
HYPOTHESIS: >
  Where certificate numbering is maintained per company or per branch, as the configured
  statutory rule requires, issuance from one company or branch never draws from, or writes
  into, another's numbering series.
WHY_IT_MATTERS: >
  A cross-boundary draw on another entity's series breaks the per-entity completeness the
  statutory rule is meant to guarantee.
DISCONFIRMING_OBSERVATION: >
  A certificate issued under one company or branch context is assigned a number from a
  different company's or branch's series.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Issue certificates from two different company or branch contexts in close succession and
  verify each draws only from its own series.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q044

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q044
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Voiding a certificate after issuance has a defined, consistent effect on its number
  (permanently retired, or explicitly reissued to a new certificate under a recorded rule)
  rather than an effect that differs unpredictably by case.
WHY_IT_MATTERS: >
  An unpredictable outcome for a voided certificate's number makes the sequence's own
  history impossible to explain to a reviewer.
DISCONFIRMING_OBSERVATION: >
  Voiding two comparable certificates results in different outcomes for their numbers (one
  retired, one silently reassigned) with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Void two comparable certificates and compare what happens to each of their numbers.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q045

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q045
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Changing which tax category or rate a posted withholding entry was computed under requires
  an authorization distinct from the authorization needed for an ordinary, non-tax-relevant
  edit to the same payment.
WHY_IT_MATTERS: >
  If changing the tax basis of a posted entry needs no more authorization than any routine
  edit, a control that should sit specifically on tax-relevant changes does not actually
  exist.
DISCONFIRMING_OBSERVATION: >
  A user holding only ordinary edit rights, with no distinct tax-configuration
  authorization, can change the tax category or rate attribution of a posted withholding
  entry.
EXPECTED_SURFACE: S2,S4
PRECONDITIONS: >
  As a user with only ordinary edit rights, attempt to change the tax category or rate
  attribution of a posted withholding entry.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q046

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q046
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A post-posting change to a withholding entry's attribution is logged with the actor, the
  original attribution, and the new attribution, not merely that a change occurred.
WHY_IT_MATTERS: >
  A log entry missing the before-and-after values cannot support a reviewer assessing
  whether the change was appropriate.
DISCONFIRMING_OBSERVATION: >
  The log for a post-posting attribution change records that a change happened but omits
  either the original or the new attribution value.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Make a post-posting change to a withholding entry's attribution and inspect the fields
  captured in the resulting log entry.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q047

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q047
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A post-posting change to withholding attribution requires some accompanying business
  justification to be recorded before the change can be saved, rather than the field being
  present but unenforced.
WHY_IT_MATTERS: >
  An unenforced justification field gives the appearance of a control without actually
  requiring anyone to state a reason.
DISCONFIRMING_OBSERVATION: >
  A post-posting attribution change saves successfully with the justification field left
  empty.
EXPECTED_SURFACE: S2,S4,S6
PRECONDITIONS: >
  Attempt a post-posting attribution change while leaving any business-justification field
  empty and see whether the save is accepted.
```

## G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q048

```yaml
QID: G04-L10N_ACCOUNT_WITHHOLDING_TAX-Q048
MODULE: l10n_account_withholding_tax
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Changing withholding attribution on an already-posted entry is only reachable through a
  controlled reversal-and-repost path, not through a direct in-place edit of the posted
  entry's tax attribution.
WHY_IT_MATTERS: >
  A direct in-place edit path on a posted tax-relevant entry bypasses the visibility a
  reversal-and-repost path would otherwise guarantee.
DISCONFIRMING_OBSERVATION: >
  A posted entry's withholding attribution can be changed through a direct in-place edit,
  with no reversal or repost step involved.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Attempt to change a posted entry's withholding attribution directly, without invoking any
  reversal or repost mechanism, and observe whether it succeeds.
```
