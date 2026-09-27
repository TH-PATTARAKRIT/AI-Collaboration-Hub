# SMEsPlus ENTERPRISE SUITE
## GMVQ — G04 ACCOUNT_BASE / account_tax_python Module MVQ Bank

**Document ID:** GMVQ-G04-ACCOUNT_TAX_PYTHON-MVQ48-V1.00
**Group:** G04 ACCOUNT_BASE
**Module Metadata:** `account_tax_python`
**Wave:** W1
**Author Cell:** TEAM 21 (GMVQ Primary Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific MVQ set (in addition to the 55 shared Standard
Questions) for a tax mechanism whose computation is expressed as a configurable rule
rather than a fixed rate. Questions target the authoring/activation boundary, rule
versioning against the tax point, determinism and reproducibility of a posted amount,
rounding behaviour, reachability from every runtime path (interactive, import,
integration, scheduled), failure and exception handling mid-posting, and the audit
trail that must tie a posted tax figure back to the exact rule text that produced it.
Where a question would otherwise require asserting a specific statutory rate, form, or
deadline, it is written in behavioural terms instead and carries
`LEGAL_TAX_REVIEW_REQUIRED: YES`.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: each of the 48 targets a distinct material hypothesis: none is a rephrasing
  of another question's failure mode.
- This bank is DRAFT question content only. It is not evidence, not approved, not frozen.
- `MODULE + QID` is a Research Evidence Join Key for the blind two-lane study only.
- No Thai statutory rate, form number, or filing deadline is asserted anywhere in this bank.
- Question text contains no vendor name, product name, model/field/method name, XML ID,
  API path, or the module's own metadata name.

## G04-ACCOUNT_TAX_PYTHON-Q001

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q001
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The person who may author the text of a configurable tax rule is not automatically
  the same person who may make that rule the one applied to live documents.
WHY_IT_MATTERS: >
  If drafting and activating are the same unchecked capability, an unreviewed formula
  can begin affecting posted tax amounts with no independent control point.
DISCONFIRMING_OBSERVATION: >
  A user able to write or edit rule text can also make it active for live computation
  with no distinct authorization step, approval, or second party involved.
EXPECTED_SURFACE: S4,S6,S7
PRECONDITIONS: >
  Identify the capability that edits rule text and the capability that activates a rule
  for use; compare whether one role holds both without an intervening control.
```

## G04-ACCOUNT_TAX_PYTHON-Q002

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q002
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A configurable tax rule is evaluated only against the tax base and the data explicitly
  needed to compute it, not against arbitrary other data on the document or related records.
WHY_IT_MATTERS: >
  A rule with unbounded data reach can leak or act on information that has nothing to do
  with tax computation, and that reach is invisible to anyone reading the posted amount.
DISCONFIRMING_OBSERVATION: >
  A rule is shown to read, and its result to vary with, a data value that is unrelated to
  the tax base and not declared as a rule input.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Construct two otherwise-identical documents differing only in an unrelated field and
  compare the rule's computed result.
```

## G04-ACCOUNT_TAX_PYTHON-Q003

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q003
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a configurable rule raises an error or returns a non-numeric result while a
  document is being posted, the posting is blocked rather than completed with a
  substituted or default tax amount.
WHY_IT_MATTERS: >
  A silent fallback to zero or a default amount on rule failure would post a financial
  document with a wrong tax figure that looks intentional.
DISCONFIRMING_OBSERVATION: >
  A document posts successfully, carrying a tax amount, even though the rule that was
  supposed to compute it errored or returned a non-numeric value during that posting.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Configure a rule that deliberately errors or returns an invalid result, attach it to a
  document, and attempt to post.
```

## G04-ACCOUNT_TAX_PYTHON-Q004

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q004
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Computing tax on the same document twice, with no change to the document or the rule
  in force, produces the identical amount both times.
WHY_IT_MATTERS: >
  Non-deterministic computation makes a posted figure unreproducible and destroys the
  ability to independently verify any tax amount later.
DISCONFIRMING_OBSERVATION: >
  Recomputing tax on an unchanged document, under an unchanged rule, yields a different
  amount than the first computation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Compute tax on a document, record the amount, trigger recomputation without altering
  the document or the rule, and compare.
```

## G04-ACCOUNT_TAX_PYTHON-Q005

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q005
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LEGAL_TAX_REVIEW_REQUIRED: YES
HYPOTHESIS: >
  The version of a configurable rule that is in force at the document's tax point date
  is the version used to compute its tax, even if a newer version has since become active.
WHY_IT_MATTERS: >
  Without a fixed version-at-tax-point rule, the same historical document could compute
  a different tax amount depending only on when someone happens to look at it.
DISCONFIRMING_OBSERVATION: >
  A document with a tax point date under an earlier rule version computes using the
  currently active rule version instead of the one in force at that date.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Activate a rule, let a document take its tax point under it, then activate a
  successor rule and recompute the same document.
```

## G04-ACCOUNT_TAX_PYTHON-Q006

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q006
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A posted document does not silently re-evaluate its tax rule on later view, export, or
  unrelated edit; its posted amount stays fixed unless an explicit correction path is used.
WHY_IT_MATTERS: >
  Silent re-evaluation of posted figures would let an unrelated later action change a
  historical financial amount with no correction record.
DISCONFIRMING_OBSERVATION: >
  Simply opening, exporting, or making an unrelated edit to a posted document changes
  its previously posted tax amount.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a document, record its tax amount, then open/export/edit an unrelated field and
  re-check the amount.
```

## G04-ACCOUNT_TAX_PYTHON-Q007

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q007
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where rounding occurs both inside a rule's own computation and again at document
  total level, the two roundings are distinguishable and the residual difference lands
  in a declared, traceable place rather than being absorbed silently.
WHY_IT_MATTERS: >
  An untracked rounding residual is a small, repeated discrepancy that never
  reconciles and erodes trust in every total that depends on it.
DISCONFIRMING_OBSERVATION: >
  A rounding difference between the rule's internal result and the document-level
  total exists but cannot be located in any line, adjustment, or reconciling record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Construct a document whose per-line rule computation and document-level rounding
  disagree by a small margin, then trace where the margin appears.
```

## G04-ACCOUNT_TAX_PYTHON-Q008

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q008
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A document created through a bulk import path has its tax computed by the same
  configurable rule engine, under the same version-selection logic, as a document
  entered interactively.
WHY_IT_MATTERS: >
  A tax engine that only runs on the interactive path leaves every imported document
  under-taxed, over-taxed, or entirely untaxed without anyone noticing.
DISCONFIRMING_OBSERVATION: >
  A document created by bulk import receives a different tax amount than an otherwise
  identical document entered interactively under the same rule and tax point.
EXPECTED_SURFACE: S1,S2,S3,S8
PRECONDITIONS: >
  Create matching documents via the interactive path and via bulk import under the
  same active rule and compare computed tax.
```

## G04-ACCOUNT_TAX_PYTHON-Q009

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q009
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A document or transaction created through an external system integration path is
  subject to the same configurable tax rule as one entered interactively, not a
  simplified or bypassed computation.
WHY_IT_MATTERS: >
  An integration shortcut that skips the rule engine creates a second, unaudited tax
  computation path with its own error surface.
DISCONFIRMING_OBSERVATION: >
  A transaction arriving through an external integration path carries a tax amount
  that the configured rule, given the same inputs, would not have produced.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Submit an equivalent transaction through the integration path and through the
  interactive path under the same rule and compare results.
```

## G04-ACCOUNT_TAX_PYTHON-Q010

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q010
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A scheduled or background process that creates or recomputes tax-bearing documents
  invokes the same rule and version-selection logic as an interactive user action.
WHY_IT_MATTERS: >
  A background path with its own tax logic can silently drift from the interactive
  path over time, with no user present to notice the divergence.
DISCONFIRMING_OBSERVATION: >
  A document produced or recomputed by a scheduled background pass carries a tax
  amount inconsistent with what the same active rule would produce interactively.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Trigger a scheduled or background pass that touches tax-bearing documents and
  compare its output to an interactive equivalent under the same rule.
```

## G04-ACCOUNT_TAX_PYTHON-Q011

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q011
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A document with a very large number of lines completes rule-based tax computation
  within a bounded time, or fails in a way that blocks posting cleanly rather than
  posting a partially-computed result.
WHY_IT_MATTERS: >
  A silent timeout that lets a large document post with only some lines taxed would
  understate tax with no visible error.
DISCONFIRMING_OBSERVATION: >
  A large document posts successfully while only a subset of its lines actually
  received a computed tax amount, with no error or warning raised.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Construct a document with a large number of lines under an active rule and attempt
  to post it, observing completion time and per-line results.
```

## G04-ACCOUNT_TAX_PYTHON-Q012

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q012
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A rule can be evaluated in a test or preview context against sample or draft data
  without producing any durable effect on live records, sequences, or logs.
WHY_IT_MATTERS: >
  Without a side-effect-free way to test a rule, every trial of a new formula risks
  contaminating live data or consuming a document number.
DISCONFIRMING_OBSERVATION: >
  Running a rule in a test or preview context leaves a durable trace in live data, a
  consumed sequence number, or a persisted record indistinguishable from a real one.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Run a rule against sample data using any preview/test facility, then inspect live
  data and sequences for residue.
```

## G04-ACCOUNT_TAX_PYTHON-Q013

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q013
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  For any posted document, the exact text or version identifier of the rule that
  produced its tax amount can be recovered later, not just the numeric result.
WHY_IT_MATTERS: >
  Without that link, a disputed tax figure cannot be defended or reproduced, and a
  later rule change cannot be distinguished from an original computation error.
DISCONFIRMING_OBSERVATION: >
  A posted document's tax amount exists with no recoverable record of which rule
  version or text produced it.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Post a document under a known rule version, later change the rule, and attempt to
  recover which version produced the original posted amount.
```

## G04-ACCOUNT_TAX_PYTHON-Q014

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q014
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LEGAL_TAX_REVIEW_REQUIRED: YES
HYPOTHESIS: >
  When a document's posting date, document date, and tax point date differ, the rule
  version selection is driven consistently by one declared date, not by whichever date
  happens to be visible in the entry screen at computation time.
WHY_IT_MATTERS: >
  An undeclared or inconsistent choice of driving date makes the same document eligible
  for two different rule versions depending on operator behaviour.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical documents, differing only in which of the three dates is
  set furthest from the others, receive their rule version from different dates.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Create documents with deliberately staggered posting, document, and tax point dates
  spanning a rule version change, and observe which date determines the version used.
```

## G04-ACCOUNT_TAX_PYTHON-Q015

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q015
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A document whose tax point falls inside a locked or closed accounting period cannot
  be newly posted with a rule-computed amount without an explicit override that is
  itself recorded.
WHY_IT_MATTERS: >
  A rule engine that bypasses period locking defeats the entire purpose of closing a
  period for financial reporting.
DISCONFIRMING_OBSERVATION: >
  A document with a tax point in a locked period posts, with a rule-computed tax
  amount, with no override flag or record of the exception.
EXPECTED_SURFACE: S1,S2,S6,S7
PRECONDITIONS: >
  Lock a period, then attempt to post a new document whose tax point falls inside it.
```

## G04-ACCOUNT_TAX_PYTHON-Q016

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q016
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LEGAL_TAX_REVIEW_REQUIRED: YES
HYPOTHESIS: >
  A new or amended rule is effective-dated: it applies to documents whose tax point
  falls on or after its effective date, and does not retroactively change the
  computation basis of an unposted document whose tax point predates it.
WHY_IT_MATTERS: >
  Silent retroactive application would let a rule edited today change what an
  unposted document dated last month is expected to owe.
DISCONFIRMING_OBSERVATION: >
  An unposted document with a tax point before a rule's effective date computes using
  the new rule anyway once the new rule is saved.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create an unposted document with a tax point before a pending rule change, save
  the rule change, and recompute the document.
```

## G04-ACCOUNT_TAX_PYTHON-Q017

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q017
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Editing or replacing a configurable rule after documents have already been posted
  under its prior version never changes the stored tax amount on those already-posted
  documents.
WHY_IT_MATTERS: >
  If editing a live rule reaches backward into posted history, no closed period is
  ever actually closed.
DISCONFIRMING_OBSERVATION: >
  The stored tax amount on a document posted under an earlier rule version changes
  after that rule is later edited or replaced.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a document under a known rule, record its tax amount, edit the rule, and
  re-inspect the posted document.
```

## G04-ACCOUNT_TAX_PYTHON-Q018

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q018
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reversing a posted document that carried a rule-computed tax amount reproduces that
  same original amount on the reversing entry, rather than recomputing tax fresh
  under whatever rule is active at reversal time.
WHY_IT_MATTERS: >
  A reversal that recomputes under a newer rule will not actually net the original
  entry to zero, leaving a residual no one can explain.
DISCONFIRMING_OBSERVATION: >
  A reversal generated after a rule change carries a tax amount different from the
  original posted document's amount, and the two do not net to zero.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a document, change the active rule, then reverse the original document and
  compare the reversal's tax amount to the original.
```

## G04-ACCOUNT_TAX_PYTHON-Q019

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q019
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling a document before it is posted leaves no rule-computed tax amount
  standing anywhere as though it had been finalized.
WHY_IT_MATTERS: >
  A provisional computation that survives cancellation could be picked up by a
  later report as though it were a real, live figure.
DISCONFIRMING_OBSERVATION: >
  After a document is cancelled pre-posting, its provisional rule-computed tax
  amount still appears in a total, report, or downstream record as active.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Enter a document under an active rule, allow provisional computation, cancel it
  before posting, and check for residue in any total or report.
```

## G04-ACCOUNT_TAX_PYTHON-Q020

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q020
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If one configurable rule is allowed to reference another rule's result, a circular
  reference between rules is detected and blocked rather than left to loop or crash
  during posting.
WHY_IT_MATTERS: >
  An undetected circular dependency turns a routine posting into an unpredictable
  hang or crash with no diagnostic pointing at the cause.
DISCONFIRMING_OBSERVATION: >
  Two rules configured to reference each other are accepted and only fail, hang, or
  loop at the moment a document is posted, with no earlier validation warning.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure two rules that reference each other's result and attempt to save the
  configuration, then attempt to post a document using them.
```

## G04-ACCOUNT_TAX_PYTHON-Q021

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q021
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A configurable rule scoped to one company or tenant cannot read or be influenced by
  data belonging to another company or tenant during evaluation.
WHY_IT_MATTERS: >
  A rule that reaches across tenant boundaries breaks the isolation the whole
  multi-tenant model depends on, silently and per computation.
DISCONFIRMING_OBSERVATION: >
  Changing a value in another company's data changes the computed tax result for a
  document in a company that should be isolated from it.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Set up two companies with a rule scoped to one; change data belonging to the other
  and recompute a document in the scoped company.
```

## G04-ACCOUNT_TAX_PYTHON-Q022

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q022
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  On a document issued in a foreign currency, the rule computes tax against a single,
  declared currency basis (document currency or company currency), not inconsistently
  against whichever is convenient at each step.
WHY_IT_MATTERS: >
  Mixing currency bases inside one computation produces a tax figure that does not
  reconcile against either currency's own totals.
DISCONFIRMING_OBSERVATION: >
  A foreign-currency document's tax computation uses the document currency for part of
  the calculation and the company currency for another part, with no reconciling step.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a foreign-currency document under an active rule and trace which currency
  basis each stage of the computation actually uses.
```

## G04-ACCOUNT_TAX_PYTHON-Q023

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q023
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Posting two documents concurrently while a rule they both depend on is being edited
  does not let one document post under the old rule text and the other under a
  half-saved version.
WHY_IT_MATTERS: >
  A torn read of an in-progress rule edit produces two postings on the same day that
  cannot both be right, with no way to tell which is which.
DISCONFIRMING_OBSERVATION: >
  Two concurrent postings against the same rule, overlapping an edit to that rule,
  produce different computations that correspond to no single, complete rule version.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Post two documents at the same time while saving an edit to the rule they share,
  and compare each posting's basis to the rule versions that actually existed.
```

## G04-ACCOUNT_TAX_PYTHON-Q024

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q024
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rule cannot produce, and the system will not post, a tax amount that is negative
  or exceeds a sane bound relative to the document's own base value without raising
  an exception.
WHY_IT_MATTERS: >
  An unbounded rule result posted without question can create a financial document
  that is nonsensical on its face and still stands as a system of record.
DISCONFIRMING_OBSERVATION: >
  A document posts successfully carrying a tax amount that is negative, or wildly
  disproportionate to its base value, with no exception or warning raised.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Configure a rule that deliberately returns a negative or disproportionate value and
  attempt to post a document under it.
```

## G04-ACCOUNT_TAX_PYTHON-Q025

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q025
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Deactivating a rule while documents in progress still reference it leaves those
  documents in a defined, visible state rather than silently falling back to a
  different rule or a fixed default.
WHY_IT_MATTERS: >
  An undocumented fallback when a rule is withdrawn mid-flight changes what a user
  believes they are about to post without telling them.
DISCONFIRMING_OBSERVATION: >
  A document already referencing a rule that is then deactivated posts using a
  different rule or a fixed default with no notice to the preparer.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Start a document under an active rule, deactivate the rule before posting, and
  observe what the document does next.
```

## G04-ACCOUNT_TAX_PYTHON-Q026

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q026
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Evaluating a configurable rule produces only the tax amount it is asked for; it does
  not, as a side effect, write to or modify any record unrelated to the document being
  taxed.
WHY_IT_MATTERS: >
  A computation step with hidden write side effects turns every tax calculation into
  an unaudited change to other data.
DISCONFIRMING_OBSERVATION: >
  Evaluating a rule against a document is shown to change a record other than the
  document's own tax amount and its direct posting artifacts.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Snapshot unrelated records, evaluate a rule against a document, and diff the
  snapshot afterward.
```

## G04-ACCOUNT_TAX_PYTHON-Q027

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q027
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Unposting a document that carried a rule-computed tax amount requires a distinct,
  traceable authorization and is not available to the same broad population that can
  merely view the document.
WHY_IT_MATTERS: >
  If unposting a taxed document is as easy as viewing it, every posted tax figure is
  only ever provisional.
DISCONFIRMING_OBSERVATION: >
  A user with only view-level access to a posted document is able to unpost it, or no
  trace is left of who unposted it and when.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Attempt to unpost a rule-taxed document using an account with view-only access, and
  separately check whether a successful unpost by an authorized user leaves a trace.
```

## G04-ACCOUNT_TAX_PYTHON-Q028

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q028
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A document that is not tied to any configurable rule, and has none assigned, is
  distinguishable from one that has a rule assigned but that rule evaluated to zero.
WHY_IT_MATTERS: >
  Conflating "no rule" with "rule computed zero" hides configuration mistakes behind a
  perfectly plausible-looking amount.
DISCONFIRMING_OBSERVATION: >
  A document with no rule assigned and one with a rule that computed zero are
  presented identically, with no way to tell which case occurred.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Create one document with no rule assigned and one with a rule that legitimately
  computes to zero, and compare how each is recorded.
```

## G04-ACCOUNT_TAX_PYTHON-Q029

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q029
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Summing the rule-computed tax across all lines of a multi-line document reconciles
  exactly, or with a fully-traceable residual, to the tax shown at document total level.
WHY_IT_MATTERS: >
  An untraceable gap between line-level and document-level tax is exactly the kind of
  discrepancy that undermines every downstream financial report.
DISCONFIRMING_OBSERVATION: >
  The sum of per-line rule-computed tax does not equal the document-level tax total,
  and the difference cannot be located in any adjustment or reconciling entry.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Build a multi-line document under an active rule, sum the per-line tax, and compare
  to the document-level total.
```

## G04-ACCOUNT_TAX_PYTHON-Q030

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q030
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A configurable rule applied to a credit note or other negative-value document
  produces a tax amount whose sign correctly mirrors the underlying value, not a
  positive amount on a reducing document.
WHY_IT_MATTERS: >
  A sign error on a credit note's tax silently increases, rather than reduces, a
  customer's or the business's tax position.
DISCONFIRMING_OBSERVATION: >
  A credit note under the same rule as an equivalent invoice produces a tax amount
  with the wrong sign relative to the value it is reducing.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an invoice and a corresponding credit note under the same rule and compare
  the sign and magnitude of each computed tax amount.
```

## G04-ACCOUNT_TAX_PYTHON-Q031

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q031
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Duplicating a posted document produces a new draft whose tax is recomputed fresh
  under the rule now in force, and does not silently carry forward the original
  posted amount as if it still applied.
WHY_IT_MATTERS: >
  A duplicate that inherits a stale posted amount can be posted again as though it
  were freshly and correctly computed, when it was not.
DISCONFIRMING_OBSERVATION: >
  A duplicated draft retains the original document's exact tax amount even though the
  rule in force has since changed, with no recomputation performed or flagged.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a document, change the active rule, duplicate the posted document, and inspect
  the duplicate's tax amount before it is posted.
```

## G04-ACCOUNT_TAX_PYTHON-Q032

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q032
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing a configurable rule does not retroactively alter figures that a related
  reporting or withholding process has already derived from documents taxed under the
  prior version.
WHY_IT_MATTERS: >
  A rule change that reaches into a downstream, already-issued obligation creates a
  mismatch between what was reported and what the system now shows.
DISCONFIRMING_OBSERVATION: >
  A downstream figure already derived from a posted document changes value after the
  rule that originally computed that document's tax is edited.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a document and let a dependent downstream figure be derived from it, then edit
  the originating rule and re-check the downstream figure.
```

## G04-ACCOUNT_TAX_PYTHON-Q033

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q033
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When a rule can be scoped to a specific company or branch, a company or branch with
  no rule of its own has a defined, visible fallback rather than silently inheriting
  an unrelated company's rule.
WHY_IT_MATTERS: >
  Silent inheritance across company boundaries means a new branch could start
  computing tax under a formula meant for a different legal entity.
DISCONFIRMING_OBSERVATION: >
  A company or branch with no rule configured computes tax using another company's
  scoped rule with no visible fallback declaration.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure a rule scoped to one company only, then compute tax for a document in a
  second company that has no rule of its own.
```

## G04-ACCOUNT_TAX_PYTHON-Q034

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q034
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a rule depends on an attribute that must be looked up elsewhere (for example on
  the counterparty), an unavailable or unset attribute causes a defined error or hold,
  not a silent substitution with an arbitrary value.
WHY_IT_MATTERS: >
  A silent substitution when required data is missing hides a data-quality problem
  inside what looks like a normal computed tax amount.
DISCONFIRMING_OBSERVATION: >
  A rule that depends on a missing or unset external attribute still returns a normal
  numeric result with no error, hold, or warning raised.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Configure a rule that depends on a counterparty attribute, leave that attribute
  unset, and compute tax on a document for that counterparty.
```

## G04-ACCOUNT_TAX_PYTHON-Q035

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q035
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The inputs and result of a rule's evaluation for a given document are retained
  somewhere durable, so a later dispute over the amount can be checked against what
  the rule actually saw, not only against the final figure.
WHY_IT_MATTERS: >
  Without a retained evaluation record, resolving a disputed tax amount reduces to
  trusting the number, with nothing to check it against.
DISCONFIRMING_OBSERVATION: >
  A posted document's tax amount exists but the specific inputs the rule used to
  reach it cannot be retrieved from any durable record.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Post a document under a rule with several inputs, then attempt to retrieve the
  exact input values the rule used for that computation.
```

## G04-ACCOUNT_TAX_PYTHON-Q036

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q036
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The capability to activate a configurable rule and the capability to approve or post
  the documents it will affect are separable, so one person cannot both decide the
  formula and be the one who posts under it unchecked.
WHY_IT_MATTERS: >
  Combining rule activation with posting authority in one person removes the last
  independent check on a change that affects every future tax amount.
DISCONFIRMING_OBSERVATION: >
  The same account is shown to both activate a rule and post documents computed
  under it, with no separation of duties control available to prevent that combination.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Identify the roles able to activate a rule and the roles able to post documents,
  and check whether the two sets can be, or are already, the same account.
```

## G04-ACCOUNT_TAX_PYTHON-Q037

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q037
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A document open for entry when a rule it depends on is edited and saved either picks
  up the new rule text at its next computation or is clearly shown to still be using
  the earlier snapshot, but never leaves that ambiguous.
WHY_IT_MATTERS: >
  An operator who cannot tell which rule version their in-progress document is using
  cannot know what amount they are actually about to post.
DISCONFIRMING_OBSERVATION: >
  A document open for entry recomputes silently to a different amount, with no
  indication to the operator, after the underlying rule is edited elsewhere.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Open a document for entry, edit and save the rule it depends on from elsewhere, and
  observe the open document's behaviour and any indication given.
```

## G04-ACCOUNT_TAX_PYTHON-Q038

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q038
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A freshly loaded computation always reflects the currently active rule; no cached
  result from a superseded rule version is served as though it were current.
WHY_IT_MATTERS: >
  A stale cached tax figure served after the rule has changed is indistinguishable
  from a correct figure until someone manually recomputes and compares.
DISCONFIRMING_OBSERVATION: >
  After a rule change, a freshly opened or freshly loaded computation still shows the
  result the superseded rule would have produced.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compute a value under one rule, change the rule, and reload the computation from a
  fresh session to check whether the old result persists.
```

## G04-ACCOUNT_TAX_PYTHON-Q039

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q039
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a document is assigned a configurable rule, any override to a fixed or
  manually entered tax amount instead of the rule's result is an explicit, visible
  action rather than a silent substitution.
WHY_IT_MATTERS: >
  A silent override hides the fact that a document's tax was not actually produced by
  the rule it appears to be governed by.
DISCONFIRMING_OBSERVATION: >
  A document assigned a rule shows a tax amount that does not match what the rule
  would compute, with no visible indication that a manual override occurred.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Assign a rule to a document, manually override the resulting amount, and check
  whether the override is visible on the document.
```

## G04-ACCOUNT_TAX_PYTHON-Q040

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q040
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rule configured to always fail blocks posting of every document that depends on
  it, rather than defaulting those documents to zero tax so they can still post.
WHY_IT_MATTERS: >
  Defaulting to zero on failure is the worst possible fallback: it looks like a valid,
  intentional exemption rather than a broken configuration.
DISCONFIRMING_OBSERVATION: >
  A document under a rule configured to always fail posts successfully with a zero
  tax amount rather than being blocked.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Configure a rule that always fails, attach it to a document, and attempt to post.
```

## G04-ACCOUNT_TAX_PYTHON-Q041

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q041
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Every record processed within a single bulk import batch is evaluated against the
  same rule snapshot; the rule does not change version partway through one batch.
WHY_IT_MATTERS: >
  A rule that changes mid-batch produces a single import file with two different tax
  bases inside it, defeating any expectation that a batch is internally consistent.
DISCONFIRMING_OBSERVATION: >
  Records within one bulk import batch are computed under two different rule
  versions because the rule changed while the batch was still running.
EXPECTED_SURFACE: S1,S2,S7,S8
PRECONDITIONS: >
  Start a large bulk import, change the active rule mid-run, and inspect whether
  records before and after the change used different rule versions.
```

## G04-ACCOUNT_TAX_PYTHON-Q042

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q042
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An aggregated tax figure appearing in a financial report can be reproduced by
  re-running the same rule versions against the same set of historical documents.
WHY_IT_MATTERS: >
  A reported total that cannot be reconstructed from its source documents and their
  governing rules cannot be defended under review.
DISCONFIRMING_OBSERVATION: >
  Re-running the applicable rule versions against the same historical documents
  produces a total that does not match the figure already shown in a report.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Take a reported aggregate tax figure for a closed period and recompute it from the
  underlying documents and the rule versions in force for each.
```

## G04-ACCOUNT_TAX_PYTHON-Q043

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q043
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The ability to view a rule's logic or text is a distinct permission from the ability
  to edit or activate it; a user can be granted one without the other.
WHY_IT_MATTERS: >
  If viewing and editing are bundled, reviewers who only need to read a rule for audit
  purposes must also be trusted with the power to change it.
DISCONFIRMING_OBSERVATION: >
  Granting read access to a rule's text necessarily also grants the ability to edit
  or activate it, with no way to separate the two.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Attempt to grant a user read-only visibility into a rule's text without granting
  edit or activation rights, and verify the boundary holds.
```

## G04-ACCOUNT_TAX_PYTHON-Q044

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q044
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rule-computed tax amount is checked against a sane upper bound relative to the
  document's own base value before posting, rather than accepted at face value
  regardless of magnitude.
WHY_IT_MATTERS: >
  Without any sanity bound, a configuration mistake that multiplies the base value
  many times over posts as an ordinary, unquestioned transaction.
DISCONFIRMING_OBSERVATION: >
  A document posts with a computed tax amount many times larger than its own base
  value, with no bound check or warning raised at any point.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Configure a rule that returns a wildly disproportionate value relative to the base
  and attempt to post a document under it.
```

## G04-ACCOUNT_TAX_PYTHON-Q045

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q045
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scheduled batch recompute process never alters the stored tax amount on a
  document that has already been posted; it acts only on documents not yet finalized.
WHY_IT_MATTERS: >
  A background job that silently touches posted history can rewrite closed-period
  figures with nobody present to notice or approve the change.
DISCONFIRMING_OBSERVATION: >
  A scheduled recompute pass changes the stored tax amount on a document that was
  already posted before the pass ran.
EXPECTED_SURFACE: S1,S2,S6,S8
PRECONDITIONS: >
  Post a document, record its tax amount, trigger the scheduled recompute pass, and
  re-check the posted document afterward.
```

## G04-ACCOUNT_TAX_PYTHON-Q046

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q046
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The audit trail for a document's tax amount distinguishes a value the rule computed
  from a value a person manually entered or overrode, rather than recording both the
  same way.
WHY_IT_MATTERS: >
  If a manual override looks identical to a rule computation in the trail, no later
  review can tell whether the formula or a person is responsible for a given figure.
DISCONFIRMING_OBSERVATION: >
  The audit trail entry for a manually overridden tax amount is indistinguishable
  from the entry for a rule-computed one.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Produce one document with a pure rule-computed amount and one with a manually
  overridden amount, and compare their audit trail entries.
```

## G04-ACCOUNT_TAX_PYTHON-Q047

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q047
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A rule that has been authored but never activated is not reachable from any live
  computation path, interactive or otherwise.
WHY_IT_MATTERS: >
  An unintended live reference to a draft rule would apply untested logic to real
  documents without anyone deciding to activate it.
DISCONFIRMING_OBSERVATION: >
  A document's tax computation is shown to use a rule that was authored but never
  marked active.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Author a rule and deliberately leave it inactive, then attempt to reach it from
  every available computation path.
```

## G04-ACCOUNT_TAX_PYTHON-Q048

```yaml
QID: G04-ACCOUNT_TAX_PYTHON-Q048
MODULE: account_tax_python
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The rule version that a configuration screen or setup record identifies as
  currently active is the same version that documents are actually computed against
  at that moment.
WHY_IT_MATTERS: >
  A mismatch between what the configuration claims is active and what actually runs
  means no configuration screen can be trusted to describe real behaviour.
DISCONFIRMING_OBSERVATION: >
  A document computed at a given moment uses a rule version different from the one
  the configuration screen identifies as active at that same moment.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Note the rule version the configuration identifies as active, compute a document at
  that moment, and compare which version actually produced the result.
```

