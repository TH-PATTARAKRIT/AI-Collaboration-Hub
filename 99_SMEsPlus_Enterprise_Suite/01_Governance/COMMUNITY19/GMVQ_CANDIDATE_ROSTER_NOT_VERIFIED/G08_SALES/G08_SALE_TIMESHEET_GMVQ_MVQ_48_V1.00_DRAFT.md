# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_timesheet Module Bridge MVQ Bank

**Document ID:** GMVQ-G08-SALE_TIMESHEET-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_timesheet`
**Wave:** W2
**Author Cell:** P-S4 (GMVQ Question Factory — Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `sale_timesheet` — a BRIDGE per
GMVQ_BRIDGE_MODULE_RULE_V1.00, seam: recorded time becoming a billable line. The underlying time
record's own capture mechanics (how a duration is entered, general project or task
categorization) belong to time-recording's base family and are deliberately NOT re-asked here;
likewise the base `sale` order's own pricing, quotation and confirmation invariants are not
restated. This bank asks only what happens at the seam where recorded human time and a
customer-facing commercial document meet: time recorded against an order after it was invoiced or
closed; time recorded by someone with no relationship to the order; the unit recorded versus the
unit billed and the rounding between them; a rate that changes mid-period and which rate governs
time already recorded; time edited or deleted after it was billed; non-billable time reclassified
as billable and the reverse; a cap or fixed price on the engagement and time recorded beyond it;
approval of time before billing, and time billed without it; and time recorded against the wrong
order and later moved. Every question was tested against the bridge rule: if it would read equally
well with no customer-facing document in the picture at all, it was cut. Margin arithmetic drawn
from the cost of that recorded time is deliberately excluded from this bank — that is the separate
`sale_timesheet_margin` bank's subject (the Five-Margin Problem, per GROUP_BRIEF_G08_SALES.md).

The question text is source-neutral and does not expose vendor or product names, field names,
methods, schema, XML IDs, API shapes, or implementation algorithms. `MODULE: sale_timesheet`
appears only in the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` stating a concrete failure state,
  never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses at the seam
  between recorded time and a customer-facing charge; none was trimmed or stretched to hit count.
- Question text is source-neutral: no vendor or product name, no technical identifier (field,
  model, method, XML ID, API path); `sale_timesheet` appears only in the `MODULE:` field.
- BRIDGE MODULE per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question fails only at the seam. None
  restates a general time-recording capture invariant that holds with no customer-facing document
  present, and none restates a `sale` order invariant (pricing, quotation, confirmation) with this
  module's name attached.
- Margin arithmetic on billed time's underlying cost is out of scope for this bank by design — see
  the sibling `sale_timesheet_margin` bank.
- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G08_SALES/*.md
  2>/dev/null | sort` was run before authoring, against the `sale_expense` and
  `sale_expense_margin` banks already drafted in this run. No overlap found; those banks are
  scoped to a third-party-invoiced cost, not recorded human time.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/evidence.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## G08-SALE_TIMESHEET-Q001

```yaml
QID: G08-SALE_TIMESHEET-Q001
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Time recorded against an order after that order's related document has already been fully
  invoiced either blocks the entry or creates a distinct supplementary billing path — it is never
  silently absorbed into the already-issued invoice.
WHY_IT_MATTERS: >
  Silently changing an amount already issued to a customer destroys that document as a reliable
  record of what was actually communicated.
DISCONFIRMING_OBSERVATION: >
  Time recorded against a fully invoiced order changes the amount on the already-issued invoice
  with no separate supplementary line or document.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Fully invoice an order, then record additional time against it, and inspect whether the
  already-issued invoice changed.
```

## G08-SALE_TIMESHEET-Q002

```yaml
QID: G08-SALE_TIMESHEET-Q002
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Time recorded against an order that has been fully closed or locked for changes is either
  rejected outright or produces an explicit exception state, never silently accepted as if the
  order were still open.
WHY_IT_MATTERS: >
  Silently accepting time against a locked order bypasses whatever control locked it, and can
  reopen a commercial period the business already reported as final.
DISCONFIRMING_OBSERVATION: >
  Time is successfully recorded and billed against an order marked closed or locked, with no
  blocking step and no distinguishable exception state.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Close or lock an order, then attempt to record and bill time against it.
```

## G08-SALE_TIMESHEET-Q003

```yaml
QID: G08-SALE_TIMESHEET-Q003
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A person with no assigned role or relationship to a given order recording time against that order
  is either prevented at entry or clearly flagged as anomalous, not treated identically to time from
  an assigned team member.
WHY_IT_MATTERS: >
  Unrelated time reaching a customer's bill with no distinguishing check either signals a control
  gap or a genuine billing error nobody would otherwise catch.
DISCONFIRMING_OBSERVATION: >
  A person with no staffing or access relationship to an order records time against it, and that
  time proceeds to billing indistinguishably from an assigned team member's time.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  As a person with no assigned relationship to a given order, attempt to record time against it and
  observe whether it is blocked, flagged, or accepted without distinction.
```

## G08-SALE_TIMESHEET-Q004

```yaml
QID: G08-SALE_TIMESHEET-Q004
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Reassigning who is staffed on an order after time has already been recorded by a person now
  removed does not retroactively invalidate or hide that already-recorded time.
WHY_IT_MATTERS: >
  Hiding legitimately recorded time because of a later staffing change loses real work already
  performed and potentially already committed to the customer.
DISCONFIRMING_OBSERVATION: >
  Removing a person's staffing relationship to an order causes their already-recorded time on that
  order to disappear or become excluded from billing consideration.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Record time against an order, then remove that person's staffing relationship to the order, and
  inspect whether the previously recorded time is still present and billable.
```

## G08-SALE_TIMESHEET-Q005

```yaml
QID: G08-SALE_TIMESHEET-Q005
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The unit in which time is recorded and the unit in which it is billed are converted through one
  defined, consistent rounding rule, not a rule that varies unexplainedly by which record happens
  to be processed.
WHY_IT_MATTERS: >
  Inconsistent rounding produces different billed amounts for identical recorded durations, for no
  reason a customer or auditor could accept.
DISCONFIRMING_OBSERVATION: >
  Two identical recorded durations are converted to two different billed amounts with no stated
  rounding rule explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record two identical durations in the recording unit and compare their converted billed amounts.
```

## G08-SALE_TIMESHEET-Q006

```yaml
QID: G08-SALE_TIMESHEET-Q006
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Rounding applied when converting recorded time to billed time is applied per a defined,
  consistent policy across entries, not sometimes favoring the business and sometimes the customer
  with no rule governing which.
WHY_IT_MATTERS: >
  Rounding that inconsistently favors whichever side benefits looks, and may actually be, a
  systematic overcharge or undercharge with no defensible policy behind it.
DISCONFIRMING_OBSERVATION: >
  Across a sample of comparable entries, rounding favors the business roughly as often as it
  favors the customer with no stated policy determining which way any given entry rounds.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Examine the rounding direction across a sample of comparable time entries and compare it against
  any stated rounding policy.
```

## G08-SALE_TIMESHEET-Q007

```yaml
QID: G08-SALE_TIMESHEET-Q007
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A billing rate that changes mid-period is applied going forward from a clear, deliberate
  effective point; time already recorded before that point is not silently re-rated to the new
  value without an explicit reason to do so.
WHY_IT_MATTERS: >
  Silently re-rating already-recorded time changes what was already implicitly promised to the
  customer for work already performed.
DISCONFIRMING_OBSERVATION: >
  Time recorded before a rate change is billed at the new rate with no explicit, deliberate reason
  recorded for applying it retroactively.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Record time under one rate, change the rate mid-period, and inspect which rate the earlier
  recorded time is actually billed at.
```

## G08-SALE_TIMESHEET-Q008

```yaml
QID: G08-SALE_TIMESHEET-Q008
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where a rate change is deliberately intended to apply retroactively (an approved retroactive
  adjustment), that retroactive re-rating is visible as a distinct, explicit event, not
  indistinguishable from time that was always billed at the new rate.
WHY_IT_MATTERS: >
  An invisible retroactive adjustment cannot later be explained to a customer or auditor who asks
  why the billed rate differs from the rate that was in effect when the work was performed.
DISCONFIRMING_OBSERVATION: >
  A deliberate retroactive rate adjustment is applied with no record distinguishing it from time
  that was billed at that rate from the start.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a deliberate, approved retroactive rate adjustment to already-recorded time and inspect
  whether the adjustment is visible as a distinct event.
```

## G08-SALE_TIMESHEET-Q009

```yaml
QID: G08-SALE_TIMESHEET-Q009
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Editing the duration or description of a time entry after it has already been included on a
  customer-facing bill does not silently change the amount already billed to the customer without a
  corresponding, visible correcting action.
WHY_IT_MATTERS: >
  A bill that changes underneath the customer with no visible correction destroys the reliability
  of every bill the business has ever issued.
DISCONFIRMING_OBSERVATION: >
  Editing an already-billed time entry's duration changes the amount on the customer's existing
  bill with no separate correcting document or record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Bill a time entry to a customer, then edit that entry's duration, and inspect whether the
  existing customer bill changed.
```

## G08-SALE_TIMESHEET-Q010

```yaml
QID: G08-SALE_TIMESHEET-Q010
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Deleting a time entry after it has already been billed does not remove the customer-facing billed
  line along with it, leaving the two records to diverge invisibly.
WHY_IT_MATTERS: >
  A billed line that survives the deletion of its source entry, or vanishes without a trace either
  way, makes the two records permanently unreconcilable.
DISCONFIRMING_OBSERVATION: >
  Deleting an already-billed time entry silently removes or breaks the link to the corresponding
  billed line with no correcting record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Bill a time entry, then delete that entry, and inspect the state of the corresponding billed line
  and any correcting record.
```

## G08-SALE_TIMESHEET-Q011

```yaml
QID: G08-SALE_TIMESHEET-Q011
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Reclassifying a time entry from non-billable to billable after the fact makes it eligible for
  billing only through the same gate — approval, rate resolution, order state — that a billable
  entry recorded as such from the start would go through.
WHY_IT_MATTERS: >
  A reclassification shortcut around normal controls lets time bypass the same checks every other
  billable entry is required to pass.
DISCONFIRMING_OBSERVATION: >
  A time entry reclassified from non-billable to billable reaches a customer bill without passing
  through the approval or rate-resolution gate an originally-billable entry would require.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Record a non-billable time entry, reclassify it as billable, and trace whether it passes through
  the same gate as an originally-billable entry before reaching a bill.
```

## G08-SALE_TIMESHEET-Q012

```yaml
QID: G08-SALE_TIMESHEET-Q012
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Changing the billing rate applied to a time entry after that entry has already been approved and
  billed does not retroactively change the amount already billed for that entry; the new rate
  applies only to entries billed from that point forward.
WHY_IT_MATTERS: >
  A retroactive rate change silently altering an already-issued bill would make the customer's
  invoice history disagree with what was actually charged and approved at the time.
DISCONFIRMING_OBSERVATION: >
  Changing the billing rate applicable to a person or activity, after a time entry using the old
  rate was already approved and billed, changes the amount shown on that already-issued bill.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Approve and bill a time entry at one rate, then change the billing rate applicable to that
  person or activity, and inspect whether the already-issued bill for the earlier entry changes.
```

## G08-SALE_TIMESHEET-Q013

```yaml
QID: G08-SALE_TIMESHEET-Q013
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where an engagement has a fixed price or a time cap, recording time that pushes the total beyond
  that cap is either blocked or explicitly flagged for a decision, rather than continuing to
  accumulate as billable past the cap with no signal.
WHY_IT_MATTERS: >
  Silent accumulation past a cap either bills the customer for more than was agreed, or hides the
  fact that delivery is quietly exceeding what the engagement was priced for.
DISCONFIRMING_OBSERVATION: >
  Time recorded beyond a configured cap or fixed-price ceiling is accepted with no block, flag, or
  signal that the cap was exceeded.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Configure a time cap or fixed-price ceiling, record time beyond it, and observe whether any
  block or flag occurs.
```

## G08-SALE_TIMESHEET-Q014

```yaml
QID: G08-SALE_TIMESHEET-Q014
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Below a fixed-price cap, additional recorded time does not silently change the customer-facing
  billed amount at all, and this is visibly consistent with the fixed-price setup rather than
  entries appearing as if uncounted or lost.
WHY_IT_MATTERS: >
  Time that appears to vanish with no explanation is indistinguishable, to whoever recorded it,
  from a system error rather than the intended behaviour of a fixed-price arrangement.
DISCONFIRMING_OBSERVATION: >
  Time recorded within a fixed-price cap produces no visible record at all of having been counted
  toward that engagement, indistinguishable from time that was never recorded.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Record time within a fixed-price cap and inspect whether it is visibly counted toward the
  engagement even though it does not change the billed amount.
```

## G08-SALE_TIMESHEET-Q015

```yaml
QID: G08-SALE_TIMESHEET-Q015
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A configured requirement that time be approved before it can be billed is actually enforced at
  the point of billing; time can be billed without approval only where the design explicitly allows
  that as a distinct, visible exception, never as a silent bypass.
WHY_IT_MATTERS: >
  A bypassable approval gate charges a customer for time nobody with authority actually confirmed
  was legitimate.
DISCONFIRMING_OBSERVATION: >
  With an approval-before-billing requirement configured, unapproved time is nonetheless billed to
  the customer with no visible exception explaining why.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Configure a requirement that time be approved before billing, then attempt to bill an unapproved
  entry.
```

## G08-SALE_TIMESHEET-Q016

```yaml
QID: G08-SALE_TIMESHEET-Q016
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Rejected, not-approved time is excluded from what can be billed, and this exclusion is visible to
  whoever is preparing the bill, not just silently absent with no explanation of why an expected
  hour did not appear.
WHY_IT_MATTERS: >
  An unexplained gap in expected billable hours forces whoever prepares the bill to investigate
  blind, or to miss the gap entirely.
DISCONFIRMING_OBSERVATION: >
  Rejected time is simply absent from the billing preparation view with no indication that it was
  excluded, or why.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Reject a time entry, then prepare a bill for the period covering it, and inspect whether the
  exclusion is visible and explained.
```

## G08-SALE_TIMESHEET-Q017

```yaml
QID: G08-SALE_TIMESHEET-Q017
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Moving a time entry from the wrong order it was originally recorded against to the correct one
  preserves the entry's original recorded date and duration — the correction does not, after the
  fact, look indistinguishable from time that was recorded against the correct order from the start.
WHY_IT_MATTERS: >
  A correction that erases its own history makes it impossible to later audit whether a move was
  legitimate or was used to shift cost or billing between orders after the fact.
DISCONFIRMING_OBSERVATION: >
  A time entry moved from one order to another shows no trace, in the destination order's history,
  that it originated elsewhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a time entry against the wrong order, move it to the correct order, and inspect whether
  the move is traceable in the destination order's history.
```

## G08-SALE_TIMESHEET-Q018

```yaml
QID: G08-SALE_TIMESHEET-Q018
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Moving an already-billed time entry to a different order is either blocked or produces a visible
  correction on both the original and destination billing records, not a silent transfer that
  leaves one side wrong.
WHY_IT_MATTERS: >
  A silent one-sided transfer leaves the original order's billed total overstated, understated on
  the destination, or both, with nothing showing why.
DISCONFIRMING_OBSERVATION: >
  Moving an already-billed time entry to a different order changes only one of the two orders'
  billing records, leaving the other unreconciled.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Bill a time entry, move it to a different order, and inspect whether both the original and
  destination orders' billing records are correctly and visibly adjusted.
```

## G08-SALE_TIMESHEET-Q019

```yaml
QID: G08-SALE_TIMESHEET-Q019
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two people recording overlapping time against the same order at close to the same time does not
  cause one entry to silently overwrite or be lost due to the other.
WHY_IT_MATTERS: >
  A lost entry due to a race condition understates billable time with no indication to either
  person that their record did not survive.
DISCONFIRMING_OBSERVATION: >
  Two people recording time against the same order at close to the same time results in only one
  of the two entries surviving.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Have two people record separate time entries against the same order at close to the same time and
  verify both entries survive.
```

## G08-SALE_TIMESHEET-Q020

```yaml
QID: G08-SALE_TIMESHEET-Q020
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A single person recording more hours in one day than is plausible across all their entries for
  that day is either flagged or blocked, not accepted and billed with no check at all.
WHY_IT_MATTERS: >
  An implausible daily total billed with no check either indicates or enables billing for time that
  could not actually have been worked.
DISCONFIRMING_OBSERVATION: >
  A person's entries for a single day sum to an implausible total (for example, exceeding 24 hours)
  and are accepted and billed with no flag or block.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record enough time entries for one person on a single day to exceed a plausible daily total, and
  observe whether any flag or block occurs.
```

## G08-SALE_TIMESHEET-Q021

```yaml
QID: G08-SALE_TIMESHEET-Q021
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  In a multi-company setup, time is billed using the rate and currency belonging to the company
  that owns the customer's order, not the company the recording person happens to belong to, when
  the two differ.
WHY_IT_MATTERS: >
  Billing at the wrong company's rate or currency corrupts both companies' separately reportable
  results and may misstate the customer's actual charge.
DISCONFIRMING_OBSERVATION: >
  Time recorded by a person belonging to one company, billed to an order owned by a different
  company, is billed at the recording person's company's rate or currency rather than the order's.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  In a multi-company configuration, have a person from one company record time against an order
  owned by a different company, and inspect which company's rate and currency governed the bill.
```

## G08-SALE_TIMESHEET-Q022

```yaml
QID: G08-SALE_TIMESHEET-Q022
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Access to see and edit another team member's time entries is governed by an explicit permission
  distinct from being able to record one's own time — one does not imply the other.
WHY_IT_MATTERS: >
  Implicit access to edit colleagues' billable time is a control gap that could let a person alter
  a bill's basis without a dedicated permission ever having been granted for it.
DISCONFIRMING_OBSERVATION: >
  A person able to record their own time is also able to view or edit another team member's time
  entries with no separate permission having been granted for that.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a person granted only the ability to record their own time, attempt to view or edit another
  team member's time entries.
```

## G08-SALE_TIMESHEET-Q023

```yaml
QID: G08-SALE_TIMESHEET-Q023
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Where self-approval of one's own time for billing is not the intended design, the person who
  approves a given time entry for billing is distinguishable, in the audit trail, from the person
  who originally recorded it; where self-approval is permitted, that too is a visible, traceable
  fact.
WHY_IT_MATTERS: >
  An audit trail that cannot show whether an approval was independent or self-granted cannot
  support any later question about whether the approval control actually functioned.
DISCONFIRMING_OBSERVATION: >
  A time entry's approval record does not distinguish whether the approver was the same person who
  recorded the time.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Approve a time entry, both as the same person who recorded it and as a different person, and
  compare whether the audit trail distinguishes the two cases.
```

## G08-SALE_TIMESHEET-Q024

```yaml
QID: G08-SALE_TIMESHEET-Q024
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Every billed time line retains a durable link back to the original recorded time entry or entries
  it was derived from, even after rounding, aggregation, or rate conversion, so the billed amount
  can be traced back to what was actually recorded.
WHY_IT_MATTERS: >
  A billed line with no traceable source cannot be defended if a customer or auditor questions how
  it was arrived at.
DISCONFIRMING_OBSERVATION: >
  A billed time line, once rounded, aggregated, or converted, cannot be traced back to the specific
  recorded time entry or entries that produced it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Bill an aggregated, rounded, or rate-converted block of time and attempt to trace it back to its
  original recorded entries.
```

## G08-SALE_TIMESHEET-Q025

```yaml
QID: G08-SALE_TIMESHEET-Q025
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Time recorded against an order and later found to have been recorded under the wrong billing rate
  can be corrected, and the correction is visible as a distinct adjustment, not blended invisibly
  into the total.
WHY_IT_MATTERS: >
  An invisible correction to a rate error cannot be explained to a customer who asks why a
  previously billed total changed.
DISCONFIRMING_OBSERVATION: >
  Correcting a time entry's wrong billing rate changes a previously billed total with no distinct,
  visible adjustment record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Bill time recorded under an incorrect rate, correct the rate, and inspect whether the resulting
  change is visible as a distinct adjustment.
```

## G08-SALE_TIMESHEET-Q026

```yaml
QID: G08-SALE_TIMESHEET-Q026
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Cancelling the underlying order after time has already been recorded but not yet billed leaves
  that time in an explicit, resolved state — write-off, transfer, or hold — rather than an orphaned
  entry with no order left to bill it against.
WHY_IT_MATTERS: >
  An orphaned entry represents real, unresolved cost exposure or lost billable work with nobody
  accountable for resolving it.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order leaves unbilled time recorded against it in an indefinite state with no
  write-off, transfer, or hold ever applied.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record unbilled time against an order, cancel that order, and inspect the resulting state of the
  time entry.
```

## G08-SALE_TIMESHEET-Q027

```yaml
QID: G08-SALE_TIMESHEET-Q027
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A cap or fixed-price arrangement later changed mid-engagement — raised, removed, or converted to
  time-and-materials — applies to time recorded from that change forward in a clear, effective-dated
  way, and does not retroactively alter how already-billed time under the old arrangement is
  treated.
WHY_IT_MATTERS: >
  Retroactively reinterpreting already-billed time under a since-changed arrangement misstates what
  was actually agreed and charged at the time.
DISCONFIRMING_OBSERVATION: >
  Changing the engagement's cap or pricing arrangement alters the billed treatment of time that was
  already billed under the arrangement in effect when it was recorded.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Bill time under one pricing arrangement, change that arrangement mid-engagement, and inspect
  whether the already-billed time's treatment changed.
```

## G08-SALE_TIMESHEET-Q028

```yaml
QID: G08-SALE_TIMESHEET-Q028
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where the same underlying activity generates both an internal cost record and a customer-billable
  time entry, the two remain reconcilable to each other, and a discrepancy between the recorded
  internal time and the recorded billable time is not simply invisible.
WHY_IT_MATTERS: >
  An invisible discrepancy between internal and billable time hides either lost billable revenue
  or an overcharge, and nobody would know to look for it.
DISCONFIRMING_OBSERVATION: >
  A deliberately introduced discrepancy between internal cost time and billable time for the same
  activity cannot be found through any reconciliation the design offers.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Introduce a deliberate discrepancy between recorded internal time and recorded billable time for
  the same activity, and attempt to reconcile the two.
```

## G08-SALE_TIMESHEET-Q029

```yaml
QID: G08-SALE_TIMESHEET-Q029
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Time recorded but explicitly marked as an error before ever being approved or billed can be
  voided cleanly and does not persist as a phantom candidate for future billing.
WHY_IT_MATTERS: >
  A phantom error entry left in the billable pool risks being accidentally approved and billed
  later, well after anyone remembers it was a mistake.
DISCONFIRMING_OBSERVATION: >
  A time entry marked as an error before approval still appears as a selectable candidate for
  billing at a later point.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Mark a not-yet-approved time entry as an error, void it, and later check whether it still
  appears as a billing candidate.
```

## G08-SALE_TIMESHEET-Q030

```yaml
QID: G08-SALE_TIMESHEET-Q030
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Bulk-editing or bulk-approving many time entries at once does not silently apply an approval or
  rate to an entry that a reviewer did not actually intend to include in that batch.
WHY_IT_MATTERS: >
  A bulk action that silently sweeps in unintended entries can approve or re-rate time nobody
  actually reviewed for that specific case.
DISCONFIRMING_OBSERVATION: >
  A bulk approval or edit action applies to an entry outside the reviewer's intended selection,
  with no distinction from the entries deliberately included.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Perform a bulk approval or edit intended to cover a specific set of entries, and inspect whether
  it affected only that set.
```

## G08-SALE_TIMESHEET-Q031

```yaml
QID: G08-SALE_TIMESHEET-Q031
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Where the business's own policy requires a discernible link between billed time and a
  deliverable or activity, a customer-facing bill derived from recorded time shows enough structure
  to satisfy that link, rather than billing for time with no attributable activity at all.
WHY_IT_MATTERS: >
  A policy requiring traceable billing detail that the billing document does not actually satisfy
  is a control that exists on paper only.
DISCONFIRMING_OBSERVATION: >
  With a policy requiring an activity link configured, a customer bill derived from recorded time
  shows a charge with no discernible link to any deliverable or activity.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Configure a policy requiring billed time to link to a deliverable or activity, then generate a
  customer bill and inspect whether that link is actually present.
```

## G08-SALE_TIMESHEET-Q032

```yaml
QID: G08-SALE_TIMESHEET-Q032
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where recorded time is billed against a not-yet-confirmed, draft order, that billing is either
  blocked until confirmation or produces an explicit provisional state distinguishable from billing
  against a confirmed order.
WHY_IT_MATTERS: >
  Billing against a draft order that may still change or never be confirmed at all commits a
  customer charge to a commercial commitment that does not yet exist.
DISCONFIRMING_OBSERVATION: >
  Time is billed against a draft, unconfirmed order with no distinguishable provisional state
  compared to billing against a confirmed order.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record and attempt to bill time against a draft order that has not yet been confirmed.
```

## G08-SALE_TIMESHEET-Q033

```yaml
QID: G08-SALE_TIMESHEET-Q033
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A rate assigned per person, per role, or per project that could all apply to the same time entry
  is resolved in a defined, consistent order of precedence, not by whichever rate happens to be
  evaluated last.
WHY_IT_MATTERS: >
  An undefined precedence order means the same entry could be billed at different rates depending
  purely on incidental processing order.
DISCONFIRMING_OBSERVATION: >
  A time entry eligible for more than one rate source is billed using a rate that does not match
  any stated precedence order among the applicable sources.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set up a time entry where a per-person, per-role, and per-project rate could all apply, and
  determine which rate was actually used against any stated precedence order.
```

## G08-SALE_TIMESHEET-Q034

```yaml
QID: G08-SALE_TIMESHEET-Q034
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An entry recorded with zero duration or a negative duration is either rejected or handled through
  an explicit, visible correction mechanism, not silently accepted as ordinary billable time.
WHY_IT_MATTERS: >
  A silently accepted zero or negative entry can be a data-entry artifact masquerading as, or
  masking, a real correction with no visible trace of either.
DISCONFIRMING_OBSERVATION: >
  A zero-duration or negative-duration time entry is accepted and processed identically to an
  ordinary positive-duration billable entry.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to record a time entry with zero or negative duration and observe how it is handled.
```

## G08-SALE_TIMESHEET-Q035

```yaml
QID: G08-SALE_TIMESHEET-Q035
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Historical, already-billed time entries remain visible and queryable after the underlying order
  is archived or the assigned team member leaves the organisation — the audit trail does not depend
  on either still being active.
WHY_IT_MATTERS: >
  An audit trail that disappears when an order archives or a person leaves cannot support a
  billing dispute or an audit raised after either event.
DISCONFIRMING_OBSERVATION: >
  Archiving the order, or deactivating the team member who recorded the time, makes an
  already-billed historical time entry unqueryable or invisible.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Archive an order or deactivate a team member after their time was billed, and attempt to query
  the historical, already-billed entry.
```

## G08-SALE_TIMESHEET-Q036

```yaml
QID: G08-SALE_TIMESHEET-Q036
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A time entry's approval, once given, is not silently invalidated by an unrelated later edit to
  the order it targets — for example a price list change on the order — without an explicit reason
  tying the two events together.
WHY_IT_MATTERS: >
  Silently invalidating an unrelated approval creates unexplained gaps in what should be a stable
  approval record whenever any part of the order is later edited.
DISCONFIRMING_OBSERVATION: >
  An unrelated edit to the order, such as a price list change, causes a previously given time
  approval to be revoked or reset with no stated connection between the two.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Approve a time entry, make an unrelated edit to its order, and inspect whether the approval is
  still intact.
```

## G08-SALE_TIMESHEET-Q037

```yaml
QID: G08-SALE_TIMESHEET-Q037
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Recording time in a unit of measure the system does not recognise as convertible to the billing
  unit produces an explicit rejection or configuration prompt, not a silent default conversion at
  an arbitrary or undocumented rate.
WHY_IT_MATTERS: >
  A silent, undocumented conversion for an unrecognised unit can produce a billed amount that bears
  no defensible relationship to the time actually recorded.
DISCONFIRMING_OBSERVATION: >
  Time recorded in an unrecognised unit is billed at a converted amount with no configuration or
  prompt explaining how the conversion was derived.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record time in a unit not already configured as convertible to the billing unit and observe how
  the conversion is handled.
```

## G08-SALE_TIMESHEET-Q038

```yaml
QID: G08-SALE_TIMESHEET-Q038
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Where approval authority for time is delegated, for example to cover a manager on leave, the
  delegation is itself visible in the audit trail, distinct from the original manager's own
  approvals.
WHY_IT_MATTERS: >
  An audit trail that cannot distinguish a delegate's approvals from the original manager's own
  cannot later establish who actually exercised the approval authority.
DISCONFIRMING_OBSERVATION: >
  Time approved by a delegate during a manager's leave is recorded indistinguishably from an
  approval made by the manager personally.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Configure an approval delegation, have the delegate approve time during it, and inspect whether
  the delegation is visible in the resulting audit trail.
```

## G08-SALE_TIMESHEET-Q039

```yaml
QID: G08-SALE_TIMESHEET-Q039
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A time entry recorded far in the past relative to today is either flagged for review or allowed
  per a defined policy window; it is not accepted identically to same-day time with no
  distinguishing signal, where the business has configured any such control at all.
WHY_IT_MATTERS: >
  A large, unflagged backdating gap can indicate reconstructed or fabricated time with no mechanism
  ever surfacing the pattern for review.
DISCONFIRMING_OBSERVATION: >
  With a backdating control configured, a time entry recorded far outside its policy window is
  accepted identically to same-day time with no flag.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Configure a backdating policy window, record a time entry well outside that window, and observe
  whether it is flagged.
```

## G08-SALE_TIMESHEET-Q040

```yaml
QID: G08-SALE_TIMESHEET-Q040
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  The customer-facing billed amount for a block of time reflects the rate that was actually in
  effect and approved for that time, not a rate silently recalculated at invoice-generation time
  using whatever rate happens to be current then.
WHY_IT_MATTERS: >
  Recalculating at invoice time using a then-current rate can bill the customer at a rate that was
  never in effect when the work was actually performed and approved.
DISCONFIRMING_OBSERVATION: >
  A block of time approved under one rate is billed, at a later invoice-generation date, using a
  different, then-current rate instead of the rate actually in effect when it was approved.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Approve time under one rate, change the rate before invoice generation, and inspect which rate
  the resulting invoice actually uses.
```

## G08-SALE_TIMESHEET-Q041

```yaml
QID: G08-SALE_TIMESHEET-Q041
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where a project spans more than one billing period, splitting recorded time across periods for
  billing purposes does not double-count or drop any recorded duration at the period boundary.
WHY_IT_MATTERS: >
  A boundary error either overcharges the customer for duplicated time or silently drops billable
  work at the seam between two billing periods.
DISCONFIRMING_OBSERVATION: >
  Time recorded near a billing-period boundary is either billed in both adjacent periods or billed
  in neither.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Record time near a billing-period boundary and verify it is billed exactly once, in the correct
  period.
```

## G08-SALE_TIMESHEET-Q042

```yaml
QID: G08-SALE_TIMESHEET-Q042
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A person recording time against an order they were removed from access to, before the removal
  took effect, retains a traceable record of having done so — removal of access does not also
  remove the historical fact of the entry.
WHY_IT_MATTERS: >
  Erasing the historical fact of a legitimately recorded entry because access was later removed
  destroys evidence of work that genuinely occurred.
DISCONFIRMING_OBSERVATION: >
  Removing a person's access to an order also removes or hides the historical record of time they
  legitimately recorded against it before the removal.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Record time against an order, remove that person's access to the order, and inspect whether the
  earlier time entry remains traceable.
```

## G08-SALE_TIMESHEET-Q043

```yaml
QID: G08-SALE_TIMESHEET-Q043
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Non-billable time still recorded against a billable order for internal cost tracking is never
  accidentally included in a customer bill through the same aggregation that pulls in the genuinely
  billable entries.
WHY_IT_MATTERS: >
  An aggregation that does not distinguish billable from non-billable status overcharges the
  customer for time never intended to reach them.
DISCONFIRMING_OBSERVATION: >
  A non-billable time entry recorded against a billable order appears as part of the aggregated
  amount on a customer bill.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record both billable and non-billable time against the same order, generate a bill, and inspect
  whether the non-billable entry is excluded.
```

## G08-SALE_TIMESHEET-Q044

```yaml
QID: G08-SALE_TIMESHEET-Q044
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where a time entry is edited before ever being approved, only the final edited state is what
  approval and billing act on — an approval decision is never carried forward against an earlier,
  since-edited version of the entry.
WHY_IT_MATTERS: >
  Approving a version of an entry that no longer exists means nobody actually reviewed what is
  ultimately billed.
DISCONFIRMING_OBSERVATION: >
  A time entry edited after an approval decision was recorded against an earlier version proceeds
  to billing carrying that earlier approval, with the edited value never re-reviewed.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Approve a time entry, then edit it, and inspect whether the prior approval is treated as still
  valid for the edited value.
```

## G08-SALE_TIMESHEET-Q045

```yaml
QID: G08-SALE_TIMESHEET-Q045
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A rate cap negotiated at the customer or contract level, rather than per person, is applied to
  the aggregate billed time in a way that is visible and attributable, so time is not silently
  discounted or written off with nothing showing why the billed total differs from the sum of
  recorded time at standard rates.
WHY_IT_MATTERS: >
  An unexplained gap between recorded time at standard rates and the actual billed total looks
  like, and may actually be, an uncontrolled write-off nobody can account for.
DISCONFIRMING_OBSERVATION: >
  A contract-level rate cap reduces the billed total below the sum of recorded time at standard
  rates with no visible record showing the cap as the reason for the difference.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Configure a contract-level rate cap below the standard-rate total, generate a bill, and inspect
  whether the resulting reduction is visibly attributed to the cap.
```

## G08-SALE_TIMESHEET-Q046

```yaml
QID: G08-SALE_TIMESHEET-Q046
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Two orders under the same engagement sharing a single combined cap on billable hours have time
  recorded against either order counted against the shared cap consistently, rather than each order
  independently tracking its own cap while the business intended one shared limit.
WHY_IT_MATTERS: >
  Two independently tracked caps where one shared cap was intended can let the combined engagement
  quietly exceed the limit that was actually agreed.
DISCONFIRMING_OBSERVATION: >
  Two orders configured to share one combined hours cap each show time tracked against an
  independent per-order cap rather than the shared total.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure two orders to share one combined billable-hours cap, record time against each, and
  inspect whether the cap is tracked jointly or independently.
```

## G08-SALE_TIMESHEET-Q047

```yaml
QID: G08-SALE_TIMESHEET-Q047
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Time entries recorded through an automated integration, such as a calendar or scheduling feed,
  are subject to the same approval-before-billing gate as manually entered time, unless an
  explicit, visible exception says otherwise.
WHY_IT_MATTERS: >
  An automated feed that bypasses the approval gate lets unreviewed time reach a customer bill
  through a path nobody was watching for that risk.
DISCONFIRMING_OBSERVATION: >
  Time entries created through an automated integration reach billing without passing the same
  approval requirement manually entered time is subject to, and no visible exception explains why.
EXPECTED_SURFACE: S1,S4,S8
PRECONDITIONS: >
  Create a time entry through an automated integration and compare its approval path against a
  manually entered entry under the same configuration.
```

## G08-SALE_TIMESHEET-Q048

```yaml
QID: G08-SALE_TIMESHEET-Q048
MODULE: sale_timesheet
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Reopening a closed order specifically to record a legitimate missed time entry produces a
  visible, distinguishable trail showing the order was reopened for that purpose, rather than
  looking identical to an order that was simply never closed.
WHY_IT_MATTERS: >
  An indistinguishable reopening makes it impossible to later tell a legitimate correction from an
  order whose closure control silently never worked.
DISCONFIRMING_OBSERVATION: >
  Reopening a closed order to add a missed time entry leaves no trace distinguishing it from an
  order that was never closed in the first place.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close an order, reopen it to record a legitimate missed time entry, and inspect whether the
  reopening is visibly and distinctly traceable.
```

