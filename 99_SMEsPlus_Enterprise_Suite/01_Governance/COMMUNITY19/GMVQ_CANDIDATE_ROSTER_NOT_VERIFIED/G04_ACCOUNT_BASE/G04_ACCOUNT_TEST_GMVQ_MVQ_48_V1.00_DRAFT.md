# SMEsPlus ENTERPRISE SUITE
## GMVQ — G04 ACCOUNT_BASE / account_test Module MVQ Bank

**Document ID:** GMVQ-G04-ACCOUNT_TEST-MVQ48-V1.00
**Group:** G04 ACCOUNT_BASE
**Module Metadata:** `account_test`
**Wave:** W1
**Author Cell:** TEAM 21 (GMVQ Primary Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN / REVISED R3
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific MVQ set (in addition to the 55 shared Standard
Questions) for consistency checks run over accounting data. Questions target the
reliability of a check's own verdict — false negatives on broken data and false
positives on correct data — the gap between a check's declared scope and what it
actually covers, behaviour against locked versus open periods, checks that mutate the
data they inspect, per-company and cross-company scope, checks presented as full
assurance when they only sampled, a suite that silently skips a check that itself
errored, and whether a check result is meaningful evidence without the data version it
ran against.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: each of the 48 targets a distinct material hypothesis: none is a rephrasing
  of another question's failure mode.
- This bank is DRAFT question content only. It is not evidence, not approved, not frozen.
- `MODULE + QID` is a Research Evidence Join Key for the blind two-lane study only.
- No Thai statutory rate, form number, or filing deadline is asserted anywhere in this bank.
- Question text contains no vendor name, product name, model/field/method name, XML ID,
  API path, or the module's own metadata name.

## G04-ACCOUNT_TEST-Q001

```yaml
QID: G04-ACCOUNT_TEST-Q001
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A consistency check reports a failure whenever the specific condition it is meant to
  detect is actually present in the data; it does not pass on data that violates it.
WHY_IT_MATTERS: >
  A check that gives a clean result on broken data is worse than no check at all,
  because it is trusted evidence that hides the exact problem it exists to find.
DISCONFIRMING_OBSERVATION: >
  Data deliberately constructed to violate the condition the check targets still
  receives a passing result from that check.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Construct data that deliberately violates one check's stated condition and run
  that check against it.
```

## G04-ACCOUNT_TEST-Q002

```yaml
QID: G04-ACCOUNT_TEST-Q002
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A consistency check does not report a failure against data that has been
  independently verified to satisfy the condition it is meant to test.
WHY_IT_MATTERS: >
  A check that flags correct data as broken trains reviewers to distrust or ignore
  its output, hiding the real failures among the false alarms.
DISCONFIRMING_OBSERVATION: >
  Data independently verified to be correct is reported as failing by the check
  meant to test that same condition.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Construct data verified correct against one check's stated condition and run
  that check against it.
```

## G04-ACCOUNT_TEST-Q003

```yaml
QID: G04-ACCOUNT_TEST-Q003
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The actual scope of records a check inspects matches what its stated name or
  description implies, rather than covering a narrower or broader set silently.
WHY_IT_MATTERS: >
  A check whose real coverage differs from its label gives reviewers false
  confidence about exactly what has, and has not, been verified.
DISCONFIRMING_OBSERVATION: >
  A check's declared name or description implies one scope of records, but tracing
  its actual execution shows it covers a different set.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Read a check's stated description and independently trace which records it
  actually inspects during a run.
```

## G04-ACCOUNT_TEST-Q004

```yaml
QID: G04-ACCOUNT_TEST-Q004
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A check run against data inside a locked or closed accounting period still
  evaluates and reports on that data, rather than silently excluding closed
  periods from its scope.
WHY_IT_MATTERS: >
  If checks quietly stop looking once a period is closed, exactly the data that
  can no longer be corrected without a formal reopening goes permanently unverified.
DISCONFIRMING_OBSERVATION: >
  Data known to violate a check's condition, sitting inside a locked period, is
  excluded from the check's result with no indication that it was skipped.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Place data that violates a check's condition inside a locked period and run
  the check, then inspect its result and stated coverage.
```

## G04-ACCOUNT_TEST-Q005

```yaml
QID: G04-ACCOUNT_TEST-Q005
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A check behaves the same way, in terms of which records it inspects, whether the
  data it examines sits in an open period or a closed one, unless a difference is
  explicitly declared.
WHY_IT_MATTERS: >
  An undeclared behavioural difference between open and closed periods means the
  same check silently means two different things depending on when it is run.
DISCONFIRMING_OBSERVATION: >
  The same check, given equivalent data, inspects a different set of records
  depending on whether the enclosing period is open or closed, with no declared reason.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Run the same check against equivalent data sets, one in an open period and one
  in a closed period, and compare coverage.
```

## G04-ACCOUNT_TEST-Q006

```yaml
QID: G04-ACCOUNT_TEST-Q006
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Running a consistency check is a read-only action: it does not write to, lock, or
  otherwise alter the data it is inspecting as a side effect of evaluation.
WHY_IT_MATTERS: >
  A check that mutates data while claiming only to verify it can mask its own
  interference as the very inconsistency it was meant to detect.
DISCONFIRMING_OBSERVATION: >
  Running a check changes a value, a lock state, or any other property of the
  data it inspected, beyond producing its pass/fail result.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Snapshot the target data, run a check against it, and diff the snapshot
  afterward for any change.
```

## G04-ACCOUNT_TEST-Q007

```yaml
QID: G04-ACCOUNT_TEST-Q007
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A check's result declares which company's data it evaluated; it is not left
  ambiguous whether the check ran against one company or every company at once.
WHY_IT_MATTERS: >
  An unlabelled scope means a passing result for one company can be mistaken for
  clearance across the whole tenant, or vice versa.
DISCONFIRMING_OBSERVATION: >
  A check's reported result does not state which company or companies it
  evaluated, and that scope cannot be determined from the result alone.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Run a check in an environment with more than one company and inspect whether
  the result states its company scope.
```

## G04-ACCOUNT_TEST-Q008

```yaml
QID: G04-ACCOUNT_TEST-Q008
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A check evaluating data across more than one company does not aggregate or net
  values from different companies together in a way that could mask an
  imbalance that exists within a single company.
WHY_IT_MATTERS: >
  Cross-company netting can make one company's real inconsistency invisible
  because another company's opposite imbalance cancels it out in the total.
DISCONFIRMING_OBSERVATION: >
  A check passes on a combined, multi-company total even though one company
  within that total, viewed alone, violates the condition being checked.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Construct two companies where one alone violates a check's condition but the
  combination appears balanced, then run the check across both.
```

## G04-ACCOUNT_TEST-Q009

```yaml
QID: G04-ACCOUNT_TEST-Q009
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a check evaluates only a sample of eligible records rather than all of
  them, its result states that it sampled, rather than being presented as
  full-population assurance.
WHY_IT_MATTERS: >
  A sampled result presented as complete assurance leads reviewers to close an
  item that was never actually fully verified.
DISCONFIRMING_OBSERVATION: >
  A check's result is presented as covering all eligible records while its
  actual execution only examined a subset, with no disclosure of the sampling.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Identify a check that samples rather than examines every eligible record and
  inspect whether its reported result discloses that.
```

## G04-ACCOUNT_TEST-Q010

```yaml
QID: G04-ACCOUNT_TEST-Q010
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If one check in a suite errors out during its own execution, the suite's
  summary makes that failure-to-run visible, rather than silently omitting it
  and reporting only the checks that completed.
WHY_IT_MATTERS: >
  A silently skipped, errored check looks identical to a check that ran and
  passed, hiding exactly the area least verified.
DISCONFIRMING_OBSERVATION: >
  A check that itself errors during a suite run is absent from the summary with
  no distinguishing mark from a check that ran and passed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Force one check in a suite to error during execution and inspect how the
  suite's overall summary represents that check.
```

## G04-ACCOUNT_TEST-Q011

```yaml
QID: G04-ACCOUNT_TEST-Q011
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A check's result is recorded together with an identifiable version or snapshot
  of the data it ran against, so the result can later be understood as applying
  to a specific state of the data rather than to data in general.
WHY_IT_MATTERS: >
  A pass/fail result with no data version attached cannot be trusted after the
  underlying data has since changed; it is evidence of nothing verifiable.
DISCONFIRMING_OBSERVATION: >
  A stored check result carries no way to determine which state or snapshot of
  the data it was evaluated against.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Run a check, then later attempt to determine from the stored result alone
  which version of the data it was evaluated against.
```

## G04-ACCOUNT_TEST-Q012

```yaml
QID: G04-ACCOUNT_TEST-Q012
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When an individual check can be excluded or disabled from a suite run, that
  exclusion is visible in the suite's result, not silently absent from both the
  pass list and the fail list.
WHY_IT_MATTERS: >
  An invisibly disabled check makes a clean suite result indistinguishable from
  one where the riskiest check was quietly turned off.
DISCONFIRMING_OBSERVATION: >
  A check disabled ahead of a suite run leaves no trace of its exclusion in the
  suite's reported result.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Disable one check ahead of a suite run and inspect whether the result
  discloses that exclusion.
```

## G04-ACCOUNT_TEST-Q013

```yaml
QID: G04-ACCOUNT_TEST-Q013
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Running the same check twice against unchanged data produces the identical
  pass/fail result both times.
WHY_IT_MATTERS: >
  A non-deterministic check cannot be relied on as evidence: the same underlying
  facts should not yield different verdicts by chance.
DISCONFIRMING_OBSERVATION: >
  Running the same check twice against data that has not changed between runs
  produces two different results.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Run a check against a fixed data set, then immediately run it again without
  any change to that data, and compare results.
```

## G04-ACCOUNT_TEST-Q014

```yaml
QID: G04-ACCOUNT_TEST-Q014
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A check running concurrently with an in-progress posting either sees a
  consistent before-or-after state of that posting, not a partially-written,
  torn state that produces a spurious failure.
WHY_IT_MATTERS: >
  A check that reads a document mid-write can report a false inconsistency that
  has nothing to do with any real data problem.
DISCONFIRMING_OBSERVATION: >
  A check flags an inconsistency solely because it read a document while a
  legitimate posting to that same document was still in progress.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger a check to run at the same moment a document is mid-posting and
  inspect whether the check's result reflects a torn read.
```

## G04-ACCOUNT_TEST-Q015

```yaml
QID: G04-ACCOUNT_TEST-Q015
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A check documented as covering a business rule also covers the closely related
  variants of that rule, rather than covering only the most common case while
  implying full coverage of the rule family.
WHY_IT_MATTERS: >
  Partial coverage presented under one general label leaves an untested variant
  looking exactly as verified as the case that was actually tested.
DISCONFIRMING_OBSERVATION: >
  A closely related variant of the rule a check claims to cover is shown to be
  entirely untouched by that check's actual logic.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Identify a check's declared rule coverage, construct a closely related variant
  of that rule, and determine whether the check actually evaluates it.
```

## G04-ACCOUNT_TEST-Q016

```yaml
QID: G04-ACCOUNT_TEST-Q016
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A check verifying that debits equal credits confirms that balance per
  currency where multiple currencies are involved, not only after everything
  has been converted into a single reporting total.
WHY_IT_MATTERS: >
  A converted-total balance can hide a real per-currency imbalance that a
  currency-blind check would never surface.
DISCONFIRMING_OBSERVATION: >
  Data with a genuine imbalance in one currency, that happens to net to zero
  once converted to the reporting currency, passes the balance check.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Construct a multi-currency imbalance that cancels out only after conversion
  and run the balance check against it.
```

## G04-ACCOUNT_TEST-Q017

```yaml
QID: G04-ACCOUNT_TEST-Q017
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A check on document numbering distinguishes a gap in the sequence from a
  reused number, reporting each as its own distinct kind of issue rather than a
  single undifferentiated numbering anomaly.
WHY_IT_MATTERS: >
  A gap and a reused number point to very different root causes and different
  remediation; conflating them wastes the entire point of running the check.
DISCONFIRMING_OBSERVATION: >
  A sequence containing a gap and a sequence containing a reused number are
  reported by the check as the same kind of finding.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Construct one sequence with a gap and one with a reused number and run the
  numbering check against each.
```

## G04-ACCOUNT_TEST-Q018

```yaml
QID: G04-ACCOUNT_TEST-Q018
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A check on reversed documents verifies that the reversal actually restores
  the original state, not merely that the visible totals happen to net to zero.
WHY_IT_MATTERS: >
  A reversal that nets to zero at the total level can still leave the wrong
  lines, accounts, or dimensions affected; only checking the total misses that.
DISCONFIRMING_OBSERVATION: >
  A reversal that nets to zero overall, but restores the wrong underlying
  lines or dimensions, is reported by the check as consistent.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Construct a reversal that nets to zero at total level but misattributes the
  underlying lines, and run the reversal-consistency check against it.
```

## G04-ACCOUNT_TEST-Q019

```yaml
QID: G04-ACCOUNT_TEST-Q019
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A check triggered manually and the same check triggered on a schedule
  evaluate the same scope of data, rather than one being a narrower or
  differently-configured variant of the other under the same name.
WHY_IT_MATTERS: >
  If the manual and scheduled runs quietly differ in scope, a clean scheduled
  result can be mistaken for the same assurance a manual run would give.
DISCONFIRMING_OBSERVATION: >
  A check run manually and the same check run on schedule, against identical
  data, produce different sets of findings.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Run a check manually and via its scheduled path against the same data and
  compare the findings from each.
```

## G04-ACCOUNT_TEST-Q020

```yaml
QID: G04-ACCOUNT_TEST-Q020
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The ability to trigger a check and the ability to see its failing detail
  down to the specific record are governed by the same permission, so a user
  who can run a check is not blocked from seeing what it found.
WHY_IT_MATTERS: >
  A check result with no visible detail is unactionable; a user trusted to run
  it but not to see its findings cannot do anything useful with a failure.
DISCONFIRMING_OBSERVATION: >
  A user able to trigger a check receives only a pass/fail count and cannot
  access which specific records the check flagged.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Run a check as a user with execution rights and attempt to access the
  specific failing records behind a non-passing result.
```

## G04-ACCOUNT_TEST-Q021

```yaml
QID: G04-ACCOUNT_TEST-Q021
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Marking a failing check result as acknowledged or resolved without fixing
  the underlying data is itself a recorded, traceable action, not an
  unattributed state change.
WHY_IT_MATTERS: >
  An untraceable way to wave off a failure lets a known inconsistency
  disappear from view with no record of who decided to accept it.
DISCONFIRMING_OBSERVATION: >
  A failing check result can be marked resolved or acknowledged with no
  record of who did it, when, or why the underlying data was not changed.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Acknowledge or dismiss a failing check result without changing the
  underlying data and inspect whether that action is traceable.
```

## G04-ACCOUNT_TEST-Q022

```yaml
QID: G04-ACCOUNT_TEST-Q022
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Changing a check's configurable sensitivity threshold affects only future
  runs; it does not retroactively reclassify a previously stored pass or fail
  result that was produced under the old threshold.
WHY_IT_MATTERS: >
  Retroactive reclassification would let a threshold change silently rewrite
  history, turning yesterday's documented failure into today's clean record.
DISCONFIRMING_OBSERVATION: >
  A previously stored check result changes its pass/fail classification after
  the check's threshold is edited, with no new run having occurred.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Store a check result under one threshold, change the threshold, and
  re-inspect the previously stored result without re-running the check.
```

## G04-ACCOUNT_TEST-Q023

```yaml
QID: G04-ACCOUNT_TEST-Q023
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A check that reports a count of issues also identifies which specific
  records those issues belong to, rather than leaving the reviewer only a
  number with no path to the affected data.
WHY_IT_MATTERS: >
  A bare count with no identified records cannot be acted on; the finding
  exists only as an abstract statistic.
DISCONFIRMING_OBSERVATION: >
  A check reports a nonzero count of issues but provides no way to identify
  which specific records those issues correspond to.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce a failing check result with more than one issue and attempt to
  trace each issue back to a specific record.
```

## G04-ACCOUNT_TEST-Q024

```yaml
QID: G04-ACCOUNT_TEST-Q024
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A check reporting zero issues means every eligible record was evaluated and
  found compliant, not that some records were silently excluded from
  evaluation as exceptions.
WHY_IT_MATTERS: >
  Excluding records to reach a clean result is functionally the same as never
  checking them, but looks identical to genuine full compliance.
DISCONFIRMING_OBSERVATION: >
  A check reports zero issues while records that meet its stated scope were
  actually excluded from evaluation rather than evaluated and passed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Introduce records that meet a check's stated scope but would be treated as
  exceptions, run the check, and determine whether they were evaluated or
  silently excluded.
```

## G04-ACCOUNT_TEST-Q025

```yaml
QID: G04-ACCOUNT_TEST-Q025
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where one check's evaluation depends on the output of another check, a
  failure of the upstream check to run at all is reflected as a distinct,
  visible gap in the downstream check's result, not treated as a pass.
WHY_IT_MATTERS: >
  A dependent check that silently treats a missing upstream result as a pass
  compounds one failure into a false clean bill for everything downstream.
DISCONFIRMING_OBSERVATION: >
  A downstream check reports a pass even though the upstream check it depends
  on did not run or errored out.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Prevent an upstream check from running or force it to error, then run the
  downstream check that depends on it and inspect the result.
```

## G04-ACCOUNT_TEST-Q026

```yaml
QID: G04-ACCOUNT_TEST-Q026
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A check on tax computation consistency validates the amount actually stored
  on the posted document, not a value freshly recomputed by the check itself
  under whatever logic is currently active.
WHY_IT_MATTERS: >
  If the check recomputes fresh, a later change to the computation logic makes
  every historical document look wrong even though nothing about it changed.
DISCONFIRMING_OBSERVATION: >
  A posted document's tax check result changes after the computation logic is
  later modified, even though the document itself was never touched.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a document, record its tax consistency check result, change the
  computation logic elsewhere, and re-run the check against the same document.
```

## G04-ACCOUNT_TEST-Q027

```yaml
QID: G04-ACCOUNT_TEST-Q027
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A check run against a very large data set either completes within a bounded
  time or fails cleanly and says so, rather than returning a partial result
  presented as though it were complete.
WHY_IT_MATTERS: >
  A partial result presented as complete is worse than an outright failure,
  because it is trusted precisely where it is least reliable.
DISCONFIRMING_OBSERVATION: >
  A check against a very large data set returns a result covering only part of
  the eligible records, with no indication that it is incomplete.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Run a check against a data volume large enough to strain normal completion
  time and inspect whether the result discloses partial coverage.
```

## G04-ACCOUNT_TEST-Q028

```yaml
QID: G04-ACCOUNT_TEST-Q028
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Adding a new check to the suite does not change the meaning of pass/fail
  results already stored from before that check existed.
WHY_IT_MATTERS: >
  If a later addition retroactively reinterprets old results, a stored
  historical pass can silently stop meaning what it meant when it was recorded.
DISCONFIRMING_OBSERVATION: >
  A previously stored, unchanged check result is presented differently, or its
  historical pass/fail status changes, after a new unrelated check is added
  to the suite.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Store a check result, add a new check to the suite, and re-inspect the
  previously stored result for any change.
```

## G04-ACCOUNT_TEST-Q029

```yaml
QID: G04-ACCOUNT_TEST-Q029
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  There is a durable, retrievable record of who triggered a given check run,
  when, and against what scope, not just the pass/fail outcome itself.
WHY_IT_MATTERS: >
  Without who/when/scope attached, a check result cannot be defended as
  evidence of anything specific during a later review.
DISCONFIRMING_OBSERVATION: >
  A stored check result exists with no retrievable record of who triggered it,
  when, or against what scope.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Trigger a check run and attempt to retrieve who ran it, when, and its scope
  from the durable record alone.
```

## G04-ACCOUNT_TEST-Q030

```yaml
QID: G04-ACCOUNT_TEST-Q030
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Re-running a check after the underlying data has been corrected reflects the
  corrected state; it does not continue to fail, or continue to pass, based on
  a cached prior evaluation.
WHY_IT_MATTERS: >
  A check that does not actually re-evaluate cannot be used to confirm a fix,
  which is one of its most basic uses.
DISCONFIRMING_OBSERVATION: >
  A check re-run immediately after the underlying violation is corrected still
  returns the same failing result it gave before the correction.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce a failing check result, correct the underlying data, and re-run the
  same check to see whether the result reflects the correction.
```

## G04-ACCOUNT_TEST-Q031

```yaml
QID: G04-ACCOUNT_TEST-Q031
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where data is organized by branch beneath a company, a check evaluates
  branch-level consistency separately from the head-office aggregate, rather
  than only ever checking the combined total.
WHY_IT_MATTERS: >
  A branch-level imbalance can be invisible in an aggregate that happens to
  net out across branches, leaving a real local problem unchecked.
DISCONFIRMING_OBSERVATION: >
  A branch with a genuine inconsistency passes because the check only ever
  evaluates the combined head-office total, which nets the imbalance away.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Construct a branch-level inconsistency that nets out in the aggregate and
  run the check at both branch and aggregate scope.
```

## G04-ACCOUNT_TEST-Q032

```yaml
QID: G04-ACCOUNT_TEST-Q032
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A check's finding distinguishes a genuine data inconsistency from a
  legitimate, approved manual adjustment that happens to look unusual, rather
  than flagging both identically as a violation.
WHY_IT_MATTERS: >
  Flagging every approved exception the same as a real error trains reviewers
  to dismiss findings on sight, burying the real ones among routine noise.
DISCONFIRMING_OBSERVATION: >
  A properly approved manual adjustment, with its own recorded justification,
  is flagged by the check identically to an unexplained inconsistency.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an approved, justified manual adjustment alongside an unexplained
  inconsistency and compare how the check reports each.
```

## G04-ACCOUNT_TEST-Q033

```yaml
QID: G04-ACCOUNT_TEST-Q033
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A check's output distinguishes findings by severity where they genuinely
  differ in consequence, rather than presenting every finding at the same
  flat level regardless of how serious it is.
WHY_IT_MATTERS: >
  Flattened severity forces a reviewer to manually re-triage every finding
  from scratch, defeating the point of running the check at all.
DISCONFIRMING_OBSERVATION: >
  Two findings with clearly different business consequence are reported by
  the check with no distinguishing severity or priority.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce one minor and one materially serious finding from the same check
  run and compare how each is presented.
```

## G04-ACCOUNT_TEST-Q034

```yaml
QID: G04-ACCOUNT_TEST-Q034
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a check only examines a recent time window rather than full history,
  its result states that time-scope explicitly, rather than reading as
  coverage of all records regardless of age.
WHY_IT_MATTERS: >
  An undisclosed time window means an old, unresolved inconsistency can sit
  permanently outside the window a passing result appears to cover.
DISCONFIRMING_OBSERVATION: >
  A check's result gives no indication that it only examined a recent window,
  even though older eligible records outside that window were never evaluated.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Place a known violation outside a check's actual time window and confirm
  whether the check's result discloses the window it used.
```

## G04-ACCOUNT_TEST-Q035

```yaml
QID: G04-ACCOUNT_TEST-Q035
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A check intended to catch a document that should have been posted by now
  evaluates that condition per accounting period, not only as a single
  global count that could hide which period the shortfall belongs to.
WHY_IT_MATTERS: >
  A global count without period attribution cannot tell a reviewer which
  period is actually incomplete, undermining any attempt to close it correctly.
DISCONFIRMING_OBSERVATION: >
  A check reports overdue unposted documents as a single global figure with
  no way to attribute them to the specific period each belongs to.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create overdue unposted documents spanning more than one period and inspect
  whether the check's result attributes them by period.
```

## G04-ACCOUNT_TEST-Q036

```yaml
QID: G04-ACCOUNT_TEST-Q036
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Which individual checks actually ran in a given suite execution can be
  listed afterward, not just the overall pass/fail count for that execution.
WHY_IT_MATTERS: >
  Without an enumerable list of what ran, a reviewer cannot confirm a suite
  execution actually covered the checks it is assumed to cover.
DISCONFIRMING_OBSERVATION: >
  A completed suite execution's record shows only an aggregate pass/fail
  count with no way to list which individual checks were included.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Run a full suite execution and attempt to retrieve the list of individual
  checks that were actually included in that run.
```

## G04-ACCOUNT_TEST-Q037

```yaml
QID: G04-ACCOUNT_TEST-Q037
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A check that depends on a configuration being present (such as a defined
  lock date) degrades to a clear, labelled non-applicable result when that
  configuration is absent, rather than misreporting a pass or fail it cannot
  actually support.
WHY_IT_MATTERS: >
  A check that fabricates a verdict when it lacks the configuration it needs
  gives false confidence about a condition it never actually evaluated.
DISCONFIRMING_OBSERVATION: >
  A check dependent on an absent configuration still returns an ordinary pass
  or fail rather than a distinct not-applicable or cannot-evaluate result.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Remove the configuration a given check depends on and run that check to see
  what result it returns.
```

## G04-ACCOUNT_TEST-Q038

```yaml
QID: G04-ACCOUNT_TEST-Q038
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A check that inspects currency-converted values accounts for expected
  rounding tolerance, so a routine rounding-scale difference is not itself
  reported as an inconsistency.
WHY_IT_MATTERS: >
  A check that flags ordinary rounding as a violation generates constant false
  alarms, which reviewers learn to ignore, burying real currency mismatches.
DISCONFIRMING_OBSERVATION: >
  A difference attributable only to routine rounding at the currency
  conversion scale is reported by the check as an inconsistency.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Construct a currency conversion difference within ordinary rounding
  tolerance and run the relevant check against it.
```

## G04-ACCOUNT_TEST-Q039

```yaml
QID: G04-ACCOUNT_TEST-Q039
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A check can be invoked in a preview or dry mode that produces its verdict
  without leaving any durable log entry, lock, or other persisted trace as a
  side effect of invocation itself.
WHY_IT_MATTERS: >
  Without a side-effect-free invocation, every exploratory or test run of a
  check pollutes the same evidence trail as a formally recorded one.
DISCONFIRMING_OBSERVATION: >
  Invoking a check in a preview or dry mode still leaves a durable log entry
  or lock indistinguishable from a formally recorded run.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Invoke a check using any available preview or dry-run facility and inspect
  whether it leaves a durable trace identical to a normal run.
```

## G04-ACCOUNT_TEST-Q040

```yaml
QID: G04-ACCOUNT_TEST-Q040
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A consistency check never modifies the data it evaluates as an embedded
  cleanup or auto-correction step; finding and fixing are kept as separate,
  independently authorized actions.
WHY_IT_MATTERS: >
  A check that silently repairs what it finds destroys the evidence of the
  original inconsistency before anyone can review whether the repair was right.
DISCONFIRMING_OBSERVATION: >
  Running a check changes the very data it just evaluated, such that the
  original inconsistency it found can no longer be reproduced afterward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Introduce a known inconsistency, run the relevant check, and verify whether
  the inconsistency still exists in the data immediately afterward.
```

## G04-ACCOUNT_TEST-Q041

```yaml
QID: G04-ACCOUNT_TEST-Q041
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A check on document number uniqueness catches a collision created by two
  concurrent creations at the moment of creation, not only when a later,
  separate audit pass happens to run.
WHY_IT_MATTERS: >
  A uniqueness problem caught only long after the fact means both colliding
  documents may already have been acted on as though each were unique.
DISCONFIRMING_OBSERVATION: >
  Two documents created concurrently are assigned a colliding number, and the
  collision is only detected by a later separate check run, not at creation.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Force two concurrent document creations likely to collide on numbering and
  observe when, if ever, the collision is detected.
```

## G04-ACCOUNT_TEST-Q042

```yaml
QID: G04-ACCOUNT_TEST-Q042
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Checks of comparable severity behave consistently in whether a failure
  blocks further processing or only produces a warning; the same class of
  issue is not a hard stop in one check and a soft warning in another with no
  declared reason.
WHY_IT_MATTERS: >
  Inconsistent blocking behaviour across equally severe issues means the
  system's real risk tolerance is accidental rather than deliberate policy.
DISCONFIRMING_OBSERVATION: >
  Two checks addressing comparably severe issues differ in whether a failure
  blocks processing, with no declared policy explaining the difference.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Compare the blocking behaviour of two checks addressing issues of
  comparable declared severity.
```

## G04-ACCOUNT_TEST-Q043

```yaml
QID: G04-ACCOUNT_TEST-Q043
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A check inspecting entries does not treat a reversal-created compensating
  entry as an unrelated original entry, and so does not count the same
  underlying issue twice, once for the original and once for its reversal.
WHY_IT_MATTERS: >
  Double-counting a single issue across an entry and its own reversal
  inflates the apparent scale of a problem and misdirects remediation effort.
DISCONFIRMING_OBSERVATION: >
  A single underlying issue is reported twice by the check, once against the
  original entry and once against the compensating entry that reversed it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an entry with a known issue, reverse it, and run the check to see
  whether the issue is reported once or twice.
```

## G04-ACCOUNT_TEST-Q044

```yaml
QID: G04-ACCOUNT_TEST-Q044
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A jurisdiction-specific validation mixed into a general consistency suite is
  labelled as jurisdiction-specific, rather than appearing as though it
  applies universally to every company regardless of jurisdiction.
WHY_IT_MATTERS: >
  An unlabelled jurisdiction-specific check either wrongly fails companies it
  should not apply to, or is wrongly assumed to cover companies it never checks.
DISCONFIRMING_OBSERVATION: >
  A jurisdiction-specific check runs against, or is reported for, a company
  outside that jurisdiction with no label distinguishing its limited applicability.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Run the full suite against a company outside the relevant jurisdiction and
  inspect how any jurisdiction-specific check is represented in the result.
```

## G04-ACCOUNT_TEST-Q045

```yaml
QID: G04-ACCOUNT_TEST-Q045
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A stored check result records the version of the check's own logic that
  produced it, so that a later change to the check does not retroactively
  reinterpret what an old pass or fail actually meant.
WHY_IT_MATTERS: >
  Without a recorded logic version, nobody can tell whether an old result
  reflects the check as it exists today or a since-changed, possibly weaker
  or stronger, earlier version.
DISCONFIRMING_OBSERVATION: >
  A stored check result carries no identifiable version of the check logic
  that produced it, so it cannot be distinguished from a result the current
  logic would produce.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Store a check result, later modify the check's own logic, and attempt to
  determine which logic version produced the earlier stored result.
```

## G04-ACCOUNT_TEST-Q046

```yaml
QID: G04-ACCOUNT_TEST-Q046
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A check for which its condition is not applicable to a given record records
  that as a distinct not-applicable outcome, rather than folding it into the
  passed outcome as though it had actually been evaluated and satisfied.
WHY_IT_MATTERS: >
  Counting not-applicable as passed inflates the appearance of verified
  coverage with records the check never truly assessed.
DISCONFIRMING_OBSERVATION: >
  A record for which the check's condition genuinely does not apply is
  reported identically to a record that was evaluated and found compliant.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Introduce a record to which a check's condition does not apply and inspect
  whether its outcome is distinguished from a genuine pass.
```

## G04-ACCOUNT_TEST-Q047

```yaml
QID: G04-ACCOUNT_TEST-Q047
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An exported or reported version of a check result carries the same
  disclosed limitations — sampling, time window, scope — as the live result
  it was taken from, rather than presenting as an unqualified clean bill once
  it leaves the live system.
WHY_IT_MATTERS: >
  A caveat that is visible live but dropped on export lets exactly the same
  qualified result be used externally as though it were unconditional.
DISCONFIRMING_OBSERVATION: >
  A check result carrying a live disclosed limitation is exported or reported
  externally with that limitation omitted.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce a check result with a disclosed limitation, export or report it
  externally, and compare the two for that disclosure.
```

## G04-ACCOUNT_TEST-Q048

```yaml
QID: G04-ACCOUNT_TEST-Q048
MODULE: account_test
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When a tenant-specific configuration narrows a check's scope beneath what its shared
  documentation describes, that narrowing is itself visible somewhere the documentation, the
  configuration, or the check's own result can be read — it is not silently invisible to
  someone relying on the documented scope.
WHY_IT_MATTERS: >
  Two tenants nominally running "the same" check can end up covered to different extents; a
  reviewer reading only the shared documentation has no way to know a specific tenant's actual
  coverage has been quietly reduced.
DISCONFIRMING_OBSERVATION: >
  A tenant's actual check coverage is narrower than the check's shared documentation states,
  and neither the documentation, the configuration screen, nor the check's result for that
  tenant shows any sign that a narrowing has been applied.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Configure a per-tenant override that narrows a check's scope beneath its documented
  coverage, run the check for that tenant, and inspect whether the documentation,
  configuration surface, or result output reflects the narrowing.
```

## CHANGE_REASON (R3)

- **QID revised:** G04-ACCOUNT_TEST-Q048
- **Returned by:** M4 (GMVQ Master Audit Team), DUPLICATE_OVERLAP finding against
  G04-ACCOUNT_TEST-Q003
- **Directive:** SMEPLUS-GMVQ-20P-5AUDIT-20260927-004
- **Old event tested:** a check's actual implemented scope silently diverging from what its
  own name, description, or configuration states it covers — a wording-only variant of Q003's
  identical event.
- **New event tested:** a per-tenant configuration override narrowing a check's scope beneath
  its shared documentation, with that narrowing invisible in the documentation, configuration
  surface, or the check's own result for that tenant.
- **Disposition:** QID preserved, question rewritten in place per authoring standard section 7.
  No silent correction — recorded here per governance requirement.
