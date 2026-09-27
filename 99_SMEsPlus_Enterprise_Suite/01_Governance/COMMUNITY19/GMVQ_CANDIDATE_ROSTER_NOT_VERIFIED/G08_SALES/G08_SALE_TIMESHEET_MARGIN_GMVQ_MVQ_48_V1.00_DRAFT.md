# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_timesheet_margin Module Bridge MVQ Bank (Margin Variant)

**Document ID:** GMVQ-G08-SALE_TIMESHEET_MARGIN-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_timesheet_margin`
**Wave:** W2
**Author Cell:** P-S4 (GMVQ Question Factory — Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `sale_timesheet_margin` — a BRIDGE per
GMVQ_BRIDGE_MODULE_RULE_V1.00 and one of the five margin variants named in the Five-Margin Problem
(GROUP_BRIEF_G08_SALES.md). Per that brief, this bank's cost is specifically RECORDED HUMAN TIME AT
A RATE THAT MAY ITSELF CHANGE, AND MAY BE EDITED RETROACTIVELY — never a standing item attribute
(`sale_margin`'s ground), a stock valuation layer (`sale_stock_margin`'s ground), a production
outcome (`sale_mrp_margin`'s ground), or a third party's invoice (`sale_expense_margin`'s ground);
this cell stayed off those four cost bases throughout authoring. This bank also does not restate
the sibling `sale_timesheet` bank's seam questions about the billed line itself (approval gating,
unit/rounding, caps, wrong-order moves) — it asks only what the REVISABILITY BY A HUMAN of both the
recorded time and the rate applied to it does to the margin figure computed from them: a person's
cost rate changed after time was recorded, and whether history restates; time deleted or reassigned
after a margin was already reported; a person's cost rate being confidential while their margin
contribution is visible; unrecorded time making a margin look better than it is; time recorded in
bulk at the end of a period and a margin swinging on one person's memory; a blended team rate hiding
an expensive individual; and the margin on a fixed-price engagement where more time simply erodes
it, and when that erosion becomes visible. Every question was tested against the bridge rule: if it
would read equally well with no margin figure being computed at all, it was cut.

The question text is source-neutral and does not expose vendor or product names, field names,
methods, schema, XML IDs, API shapes, or implementation algorithms. `MODULE: sale_timesheet_margin`
appears only in the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` stating a concrete failure state,
  never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses about the
  revisability of a human-recorded cost and its rate inside a margin figure; none was trimmed or
  stretched to hit count.
- Question text is source-neutral: no vendor or product name, no technical identifier (field,
  model, method, XML ID, API path); `sale_timesheet_margin` appears only in the `MODULE:` field.
- FIVE-MARGIN PROBLEM discipline: this bank's cost basis is recorded human time at a rate that may
  itself change and may be edited retroactively. It does not use a standing item cost, a stock
  valuation layer, a production outcome, or a third-party invoice as its ground — those belong to
  `sale_margin`, `sale_stock_margin`, `sale_mrp_margin`, and `sale_expense_margin` respectively and
  were deliberately avoided.
- BRIDGE MODULE per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question fails only at the seam between
  revisable human-recorded time and rate, and the margin figure computed from them. None restates
  the sibling `sale_timesheet` bank's own seam ground (approval gating, unit/rounding, caps, wrong-
  order moves) — that bank owns the billing seam; this bank owns only the margin arithmetic drawn
  from the same underlying recorded time.
- Cross-check against the sibling `sale_expense_margin` bank (the other margin bank authored by
  this same cell in this run) was performed at authoring time: no question or
  `DISCONFIRMING_OBSERVATION` in either bank shares a failure event with the other. This bank's
  failure events are all rooted in an internally recorded person-hour's timing, rate, and
  revisability; the sibling's are all rooted in an external invoice's lateness, currency, and
  externality. No pair was found to collapse to the same underlying event.
- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G08_SALES/*.md
  2>/dev/null | sort` was run before authoring, against the `sale_expense`, `sale_expense_margin`,
  and `sale_timesheet` banks already drafted in this run, and against the group brief's explicit
  list of what `sale_margin`, `sale_stock_margin`, and `sale_mrp_margin` own. No overlap found or
  accepted without direct verification.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/evidence.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## G08-SALE_TIMESHEET_MARGIN-Q001

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q001
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A person's internal cost rate that is changed after time was already recorded at the old rate
  does not retroactively re-rate that already-recorded time's contribution to a previously reported
  margin, unless an explicit restatement action is deliberately taken.
WHY_IT_MATTERS: >
  An ordinary rate change (a raise, a role change) silently rewriting historical margins would make
  every past margin figure only as stable as the next person's next pay change.
DISCONFIRMING_OBSERVATION: >
  Changing a person's cost rate going forward alters the previously reported margin of a sale whose
  time was recorded and reported before the change.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Report a margin based on a person's time at one cost rate, change that person's rate, and inspect
  whether the earlier reported margin changed.
```

## G08-SALE_TIMESHEET_MARGIN-Q002

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q002
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where a retroactive cost-rate correction is deliberately applied to fix a data-entry error in the
  rate itself, that correction is visibly distinguishable, wherever a margin report references it,
  from an ordinary rate change that only applies going forward.
WHY_IT_MATTERS: >
  Without that distinction, a legitimate error correction and an inappropriate retroactive
  repricing look identical to anyone reviewing why a historical margin moved.
DISCONFIRMING_OBSERVATION: >
  A deliberate retroactive rate-error correction changes historical margins with no record
  distinguishing it from an ordinary going-forward rate change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a deliberate retroactive correction to a person's previously mis-entered cost rate and
  inspect whether the correction is visibly distinct from an ordinary rate change.
```

## G08-SALE_TIMESHEET_MARGIN-Q003

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q003
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Deleting a time entry after the margin computed from it was already reported produces a visible,
  traceable adjustment to that specific sale's margin, not a silent recalculation that leaves no
  record of what changed or why.
WHY_IT_MATTERS: >
  A silent recalculation with no trace makes it impossible to later explain why a previously
  reported margin figure is no longer what it was.
DISCONFIRMING_OBSERVATION: >
  Deleting a time entry that already contributed to a reported margin changes that margin with no
  traceable adjustment record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Report a margin based partly on a specific time entry, delete that entry, and inspect whether the
  resulting change to the margin is traceable.
```

## G08-SALE_TIMESHEET_MARGIN-Q004

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q004
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Reassigning a time entry from one person to another after a margin was reported based on the
  original person's cost rate re-evaluates that entry's cost contribution using the correct
  person's rate, and the change is traceable back to the reassignment.
WHY_IT_MATTERS: >
  A reassignment that does not re-rate the cost leaves a margin computed against the wrong person's
  pay, which can be materially different from the person who actually did the work.
DISCONFIRMING_OBSERVATION: >
  Reassigning a time entry to a different person leaves the sale's margin still computed using the
  original person's cost rate.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Report a margin based on a time entry attributed to one person, reassign that entry to a
  different person with a different cost rate, and inspect whether the margin is re-evaluated.
```

## G08-SALE_TIMESHEET_MARGIN-Q005

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q005
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A person's individual cost rate remains inaccessible to a role permitted only to see aggregate
  margin outcomes, even though that margin figure is mathematically derived from the rate — the
  margin is not itself computed or displayed in a way that lets the rate be reverse-engineered from
  a single entry.
WHY_IT_MATTERS: >
  A margin figure precise enough to reveal a confidential rate through simple arithmetic defeats the
  purpose of restricting that rate in the first place.
DISCONFIRMING_OBSERVATION: >
  A role with only margin-outcome visibility can derive a specific person's confidential cost rate
  from a single time entry's contribution to a known-revenue engagement.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a role with only margin-outcome visibility, attempt to derive a person's cost rate from a
  single-entry, known-revenue engagement's margin figure.
```

## G08-SALE_TIMESHEET_MARGIN-Q006

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q006
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Where margin visibility is granted at an order or engagement level to someone without cost-rate
  access, a margin computed from just one person's single time entry does not effectively disclose
  that person's confidential rate by simple arithmetic against the known revenue.
WHY_IT_MATTERS: >
  This is the single-entry case of Q005's general boundary; a single-person engagement is the
  easiest case for confidentiality to accidentally fail.
DISCONFIRMING_OBSERVATION: >
  A single-person engagement's margin, shown to a role without cost-rate access, allows that
  person's rate to be computed directly from the known revenue and the shown margin.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create a single-person, single-entry engagement, grant margin visibility without cost-rate
  access, and attempt to derive the person's rate from the shown figures.
```

## G08-SALE_TIMESHEET_MARGIN-Q007

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q007
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Unrecorded time — work genuinely performed but never logged — is not distinguishable, in the
  margin figure alone, from work that was genuinely completed at no cost; the design either has
  some mechanism to flag this gap or explicitly does not, and that answer holds consistently.
WHY_IT_MATTERS: >
  A margin permanently overstated by unlogged labor looks identical to a genuinely efficient,
  low-cost delivery, with no way for anyone to tell the two apart.
DISCONFIRMING_OBSERVATION: >
  A sale with real, known but never-logged labor shows a margin indistinguishable from a sale
  genuinely requiring no labor, with no mechanism anywhere signaling the gap.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Identify a sale where work was performed but the corresponding time was never logged, and inspect
  whether the reported margin shows any sign of the unrecorded cost.
```

## G08-SALE_TIMESHEET_MARGIN-Q008

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q008
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A sale whose margin looks favourable primarily because a significant share of its actual delivery
  time has not yet been recorded is not presented identically, wherever margin is surfaced, to a
  sale whose time recording is materially complete.
WHY_IT_MATTERS: >
  Two margins that look the same but rest on very different completeness of cost data can lead to
  the same wrong comparison Q037 in the sibling expense-margin bank warns against.
DISCONFIRMING_OBSERVATION: >
  A sale with materially incomplete time recording and a sale with complete recording, showing
  similar headline margins, are presented with no distinguishing indicator of that difference.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Compare a sale with materially incomplete recorded time against one with complete recording,
  both showing a similar margin, for any distinguishing indicator.
```

## G08-SALE_TIMESHEET_MARGIN-Q009

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q009
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Time recorded in a single large batch well after the work was performed affects the margin for
  the period in which the time is dated as performed, not silently attributed to the period in
  which it happened to be entered, where the two differ.
WHY_IT_MATTERS: >
  Attributing a large late batch to the entry period rather than the work period misstates
  profitability for both the period that actually bore the cost and the period that did not.
DISCONFIRMING_OBSERVATION: >
  A large batch of time entered well after the fact, dated to an earlier work period, affects the
  margin of the entry period rather than the period the work is dated to.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Enter a large batch of time, dated to an earlier work period, well after that period has closed,
  and inspect which period's margin is affected.
```

## G08-SALE_TIMESHEET_MARGIN-Q010

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q010
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where a large late batch of time materially changes a margin already reported as final for a
  prior period, that change is visible as a restatement of the earlier period's figure, not folded
  invisibly into the current period with no link back.
WHY_IT_MATTERS: >
  A material change folded into the wrong period with no restatement misstates both periods and
  hides that the earlier "final" figure was not actually final.
DISCONFIRMING_OBSERVATION: >
  A large late batch of time materially changing a prior period's already-closed margin is reported
  entirely within the current period with no visible restatement of the prior period.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Close a period's margin as final, then enter a large late batch of time dated to that period, and
  inspect whether the prior period's figure is restated.
```

## G08-SALE_TIMESHEET_MARGIN-Q011

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q011
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A blended average cost rate applied across a team assigned to an engagement does not, on its own,
  prevent the true margin computed from each individual's actual rate from being derivable
  somewhere in the design — an expensive individual's actual cost is not permanently absorbed and
  hidden by the blend with no way to see the underlying detail.
WHY_IT_MATTERS: >
  A blend that permanently hides an expensive individual's true cost can make a genuinely
  unprofitable engagement look acceptable indefinitely.
DISCONFIRMING_OBSERVATION: >
  An engagement staffed by a team with one materially more expensive individual shows a margin that
  cannot, through any available path, be recomputed from each individual's own actual rate.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Staff an engagement with a team containing one materially more expensive individual, and attempt
  to recompute the engagement's true margin from each individual's actual rate.
```

## G08-SALE_TIMESHEET_MARGIN-Q012

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q012
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Where a blended rate is the business's deliberate choice for customer-facing pricing, the
  internal margin computation still has access to real individual rates, so the internal margin
  itself is not distorted by the same blending used for the customer price.
WHY_IT_MATTERS: >
  Letting a customer-pricing convenience leak into the internal margin computation would make the
  business's own profitability figure as imprecise as the price it deliberately simplified for the
  customer.
DISCONFIRMING_OBSERVATION: >
  An engagement priced to the customer using a blended rate shows an internal margin that is itself
  computed from that same blended rate rather than each individual's real cost.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a blended customer-facing rate for a team engagement and inspect whether the internal
  margin computation uses the blended rate or each individual's real cost.
```

## G08-SALE_TIMESHEET_MARGIN-Q013

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q013
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  On a fixed-price engagement, additional recorded time beyond what was originally estimated
  visibly erodes the reported margin, since revenue is fixed and cost keeps accruing, rather than
  the margin figure appearing static or unaffected while cost keeps growing underneath it.
WHY_IT_MATTERS: >
  A margin that appears unaffected while real cost keeps growing hides the exact risk a fixed-price
  arrangement is supposed to make visible to whoever is delivering it.
DISCONFIRMING_OBSERVATION: >
  Recording additional time well beyond the original estimate on a fixed-price engagement produces
  no visible change in that engagement's reported margin.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record time on a fixed-price engagement well beyond its original estimate and inspect whether the
  reported margin changes accordingly.
```

## G08-SALE_TIMESHEET_MARGIN-Q014

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q014
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where the business has any mechanism for interim margin visibility at all, the point at which
  margin erosion on a fixed-price engagement becomes visible to whoever is accountable for it is
  not deferred until the engagement fully closes.
WHY_IT_MATTERS: >
  Erosion only visible at closure removes any chance to act on a fixed-price engagement that is
  going wrong while there is still time to intervene.
DISCONFIRMING_OBSERVATION: >
  An in-progress, actively eroding fixed-price engagement's margin is unobtainable through any
  interim view before the engagement closes, despite the design having an interim visibility
  mechanism for other purposes.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Mid-engagement, on a fixed-price arrangement showing erosion, attempt to obtain an interim margin
  figure before the engagement closes.
```

## G08-SALE_TIMESHEET_MARGIN-Q015

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q015
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Changing a person's billing rate after a period has already been closed and its margin reported
  does not retroactively alter the margin already reported for that closed period; the new rate
  applies only to time recorded from that point forward.
WHY_IT_MATTERS: >
  A retroactive rate change silently altering a closed period's reported margin would make a
  previously reported, possibly already-reviewed figure disagree with itself later, with no
  recorded reason why.
DISCONFIRMING_OBSERVATION: >
  Changing a person's billing rate after a period is closed changes the margin figure already
  reported for that closed period.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Close a period and note its reported margin, then change the billing rate for a person whose
  time was recorded in that period, and check whether the closed period's reported margin changes.
```

## G08-SALE_TIMESHEET_MARGIN-Q016

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q016
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Two people on the same engagement, one whose cost rate was corrected upward and one whose
  recorded time was corrected downward around the same reporting date, each produce a
  distinguishable, separately traceable adjustment to the margin, not one blended, unexplained
  delta.
WHY_IT_MATTERS: >
  A blended, unexplained delta from two unrelated corrections makes it impossible to know which
  correction actually caused how much of the margin's movement.
DISCONFIRMING_OBSERVATION: >
  Two unrelated corrections applied around the same date produce a single combined margin change
  with no way to attribute how much came from each correction.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a rate correction for one person and a time correction for another on the same engagement
  around the same date, and inspect whether each is separately traceable in the resulting margin.
```

## G08-SALE_TIMESHEET_MARGIN-Q017

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q017
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A cost-rate history for each person is retained such that a margin for time recorded in the past
  can always be recomputed using the rate that was actually in effect for that past period, not the
  person's current rate applied retroactively by mistake.
WHY_IT_MATTERS: >
  Recomputing historical time at a current rate rather than the rate in effect then produces a
  margin for a cost that was never actually incurred.
DISCONFIRMING_OBSERVATION: >
  Recomputing a margin for time recorded under a past rate uses the person's current rate instead
  of the rate that was actually in effect when the time was recorded.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Change a person's cost rate, then recompute the margin for time they recorded before the change,
  and inspect which rate the recomputation actually uses.
```

## G08-SALE_TIMESHEET_MARGIN-Q018

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q018
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where a person's cost rate is set at a company or branch level in a multi-company setup, time
  recorded by that person against an order belonging to a different company's customer resolves
  which rate governs deliberately and consistently, not by silently defaulting to whichever
  company's record happens to be read first.
WHY_IT_MATTERS: >
  An undeliberate cross-company rate resolution corrupts the margin reported by whichever company
  ends up on the wrong side of the default.
DISCONFIRMING_OBSERVATION: >
  Time recorded by a person against an order belonging to a different company than their own
  produces a margin using a rate resolution that cannot be explained by any stated, consistent
  policy.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  In a multi-company configuration, have a person record time against an order belonging to a
  different company than the one their cost rate is set under, and inspect how the rate is
  resolved.
```

## G08-SALE_TIMESHEET_MARGIN-Q019

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q019
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Editing recorded time's duration after a margin was reported produces a visible incremental
  adjustment to that margin, distinguishable from the original figure, rather than the historical
  reported margin being silently overwritten with no trace of its earlier value.
WHY_IT_MATTERS: >
  A silently overwritten historical figure makes it impossible to later know what was actually
  reported and relied upon before the edit.
DISCONFIRMING_OBSERVATION: >
  Editing a time entry's duration after its margin was reported overwrites the previously reported
  figure with no trace of the earlier value or the adjustment that produced the new one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Report a margin based on a time entry, edit that entry's duration, and inspect whether the
  earlier reported figure remains traceable alongside the new one.
```

## G08-SALE_TIMESHEET_MARGIN-Q020

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q020
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where an engagement's margin is computed from time entries still pending approval alongside
  already-approved ones, the margin figure indicates that it includes unapproved cost estimates,
  distinguishable from a margin computed purely from approved time.
WHY_IT_MATTERS: >
  A margin blending approved and unapproved cost with no indication looks more certain than it
  actually is.
DISCONFIRMING_OBSERVATION: >
  A margin computed from a mix of approved and unapproved time entries is presented identically to
  a margin computed from fully approved time only.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Compute a margin from a mix of approved and unapproved time entries and compare its presentation
  to a margin computed from fully approved time.
```

## G08-SALE_TIMESHEET_MARGIN-Q021

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q021
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A person leaving the organisation, and their user record being deactivated, does not remove their
  historical time entries' cost contribution from previously reported margins on engagements they
  worked.
WHY_IT_MATTERS: >
  Losing a departed person's cost contribution from historical margins would retroactively and
  incorrectly inflate profitability figures already reported and relied upon.
DISCONFIRMING_OBSERVATION: >
  Deactivating a person who has left removes or zeroes out their historical time's cost
  contribution from a previously reported margin.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Report a margin including a person's recorded time, deactivate that person's user record after
  they leave, and inspect whether the previously reported margin changed.
```

## G08-SALE_TIMESHEET_MARGIN-Q022

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q022
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a time entry is approved by one approver while, at close to the same time, another person
  with authority over it edits or rejects that same entry, the resulting margin reflects one
  well-defined outcome rather than a value that mixes the approved version with the edited or
  rejected one.
WHY_IT_MATTERS: >
  A margin built from a mixed, inconsistent outcome of a concurrent approval conflict would not
  correspond to any decision anyone actually made.
DISCONFIRMING_OBSERVATION: >
  The margin for a time entry approved by one person and near-simultaneously edited or rejected by
  another reflects a value that matches neither the approved version nor the edited or rejected
  version cleanly.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Have one approver approve a time entry while another person edits or rejects the same entry at
  close to the same time, then inspect which value the resulting margin reflects.
```

## G08-SALE_TIMESHEET_MARGIN-Q023

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q023
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A team member's cost-rate confidentiality is preserved even when that same person is also the one
  who recorded their own time — being able to log one's own hours does not imply visibility into
  how that time is costed for margin purposes.
WHY_IT_MATTERS: >
  If logging one's own time implied cost-rate visibility, every employee who records time would
  automatically see their own confidential rate exposed through the margin tooling.
DISCONFIRMING_OBSERVATION: >
  A person able to log their own time can, through that same access, view the cost rate applied to
  their own hours for margin purposes.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a person with only the ability to log their own time, attempt to view the cost rate applied to
  those hours in any margin-related view.
```

## G08-SALE_TIMESHEET_MARGIN-Q024

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q024
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  The margin figure for an engagement with a hard cap on billable hours reflects that time recorded
  beyond the cap still incurred real cost even though it produced no additional revenue, rather than
  time beyond the cap disappearing from the cost side along with disappearing from the bill.
WHY_IT_MATTERS: >
  Dropping capped-out time from the cost side as well as the bill hides the true cost of delivering
  an engagement that ran over its cap.
DISCONFIRMING_OBSERVATION: >
  Time recorded beyond a billable-hours cap is excluded from the engagement's margin cost side
  entirely, the same way it is excluded from the bill.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record time beyond a configured billable-hours cap and inspect whether that time still appears
  as cost in the engagement's margin, despite not being billed.
```

## G08-SALE_TIMESHEET_MARGIN-Q025

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q025
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A time entry still awaiting approval does not contribute to the margin calculation of its sale
  or engagement; only entries that have actually been approved are counted, and only from the
  point they are approved.
WHY_IT_MATTERS: >
  Counting unapproved time in margin would let an unreviewed, possibly incorrect entry silently
  affect a reported profitability figure before anyone has confirmed it is correct.
DISCONFIRMING_OBSERVATION: >
  A time entry still awaiting approval is already reflected in the margin figure for its sale or
  engagement.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a time entry and leave it pending approval, then inspect whether the margin figure for
  its sale or engagement already reflects that entry's cost.
```

## G08-SALE_TIMESHEET_MARGIN-Q026

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q026
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where one person's time is recorded against an engagement using an overtime or premium rate for
  part of their hours and a standard rate for the rest, the margin computation reflects both rates
  distinctly for the actual hours each applied to, not one blended rate applied to the whole.
WHY_IT_MATTERS: >
  Blending a premium and a standard rate into one figure understates the true cost of the hours that
  actually incurred the premium.
DISCONFIRMING_OBSERVATION: >
  A person's mixed standard and premium hours are costed in the margin using a single blended rate
  rather than each portion's actual rate.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a mix of standard-rate and premium-rate hours for one person on an engagement and inspect
  which rate or rates the resulting margin actually applies.
```

## G08-SALE_TIMESHEET_MARGIN-Q027

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q027
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A margin already reported and then affected by a bulk correction, such as a rate-card-wide
  adjustment applied to many people at once, shows, for any individual affected sale, which of its
  changed figure came from that bulk correction rather than from an unrelated, engagement-specific
  event.
WHY_IT_MATTERS: >
  An unattributed change makes it impossible to explain to a reviewer why a specific sale's margin
  moved at the same time as an unrelated, company-wide event.
DISCONFIRMING_OBSERVATION: >
  A sale's margin changes at the same time as a bulk rate-card correction, with no record
  attributing the change to that correction specifically.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a bulk rate-card correction affecting many people, and inspect whether an individual
  affected sale's margin change is attributed to that correction.
```

## G08-SALE_TIMESHEET_MARGIN-Q028

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q028
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Time voided as a data-entry error before ever contributing to a reported margin leaves no
  residual cost contribution, distinguishable from time that was genuinely recorded and only later
  reversed after already affecting a reported figure.
WHY_IT_MATTERS: >
  Treating a pre-report void and a post-report reversal identically obscures whether a reported
  margin was ever actually wrong at the time it was issued.
DISCONFIRMING_OBSERVATION: >
  Time voided before any margin was ever reported using it is recorded identically to time reversed
  after already contributing to a reported margin.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Void a time entry before any margin report uses it, and separately reverse a different entry
  after a margin report already used it, and compare how the two are recorded.
```

## G08-SALE_TIMESHEET_MARGIN-Q029

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q029
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A person recording implausibly large end-of-period time, such as an entire week logged in one
  entry on the last day, does not receive materially different margin treatment, at least not
  silently, than time recorded incrementally as it occurred — if the business treats reconstructed
  time differently, that difference is visible somewhere.
WHY_IT_MATTERS: >
  An unsignaled difference in treatment means a business relying on memory-reconstructed time at
  period-end has no way to know its margin figures carry more uncertainty than incrementally
  recorded ones.
DISCONFIRMING_OBSERVATION: >
  A large, single end-of-period entry reconstructing a week of work is folded into a margin
  identically to incrementally recorded time, with no visible distinction anywhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a large block of time as one end-of-period entry reconstructing several days of work, and
  compare its treatment in the resulting margin against incrementally recorded time.
```

## G08-SALE_TIMESHEET_MARGIN-Q030

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q030
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  The margin design does not assume that all time worked was actually recorded — treating recording
  completeness as a deliberate, known answer rather than an unexamined assumption is itself a
  consistent, discoverable property of the design.
WHY_IT_MATTERS: >
  A design built on an unexamined assumption of full recording will produce margins that are
  systematically optimistic wherever recording is actually incomplete, with nobody having decided
  that trade-off.
DISCONFIRMING_OBSERVATION: >
  No mechanism, indicator, or documented answer exists anywhere addressing whether the margin
  figure assumes complete time recording, and the question cannot be answered from the design as
  observed.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Search the margin design's observable behaviour and documentation for any explicit treatment of
  the assumption that recorded time is complete.
```

## G08-SALE_TIMESHEET_MARGIN-Q031

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q031
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where two engagements are billed at the same fixed price and staffed by teams with different
  blended cost profiles, their reported margins are not forced to look identical by the
  blended-rate reporting layer when their true, individually-costed margins actually differ.
WHY_IT_MATTERS: >
  Two engagements that look equally profitable purely because of how a blended rate is reported,
  while their real costs genuinely differ, hides a real difference in delivery efficiency or
  staffing cost from whoever compares them.
DISCONFIRMING_OBSERVATION: >
  Two same-price engagements staffed with genuinely different-cost teams report identical margins
  despite their true, individually-costed margins actually differing.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Staff two same-fixed-price engagements with teams of genuinely different individual cost
  profiles, and compare the two reported margins against their true, individually-costed values.
```

## G08-SALE_TIMESHEET_MARGIN-Q032

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q032
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A correction to a person's cost rate that is backdated to a specific past effective date restates
  margin only for time recorded on or after that effective date, not for time recorded before it
  under a rate that was genuinely in effect then.
WHY_IT_MATTERS: >
  A backdated correction applied too broadly restates margins for time that was correctly costed
  under the rate genuinely in effect at the time.
DISCONFIRMING_OBSERVATION: >
  A rate correction backdated to a specific effective date also restates margins for time recorded
  before that effective date.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Apply a rate correction backdated to a specific effective date, and inspect whether margins for
  time recorded before that date are also restated.
```

## G08-SALE_TIMESHEET_MARGIN-Q033

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q033
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Access to see which specific individuals worked on an engagement and their respective recorded
  hours is a permission distinguishable from access to see the margin percentage the engagement
  produced — one does not serve as a backdoor into the other by default.
WHY_IT_MATTERS: >
  If staffing visibility implied margin visibility, a role that only needed to know who worked on
  an engagement would incidentally learn its profitability, or vice versa.
DISCONFIRMING_OBSERVATION: >
  A role granted only staffing and hours visibility for an engagement can also see that
  engagement's margin percentage with no separate permission granted for it.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a role granted only staffing and recorded-hours visibility, attempt to view the engagement's
  margin percentage.
```

## G08-SALE_TIMESHEET_MARGIN-Q034

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q034
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A margin swing caused entirely by one person's large, late-entered time correction is
  attributable, in an audit trail, to that specific correction event, not indistinguishable from
  ordinary week-to-week margin variation.
WHY_IT_MATTERS: >
  An unattributed swing forces a reviewer to investigate blind whether a margin move reflects a
  genuine trend or a single correction event.
DISCONFIRMING_OBSERVATION: >
  A margin swing caused by one large, late-entered correction is indistinguishable, in the audit
  trail, from ordinary period-to-period margin variation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Introduce one large, late-entered time correction causing a margin swing, and attempt to
  attribute that swing to the specific correction through the audit trail.
```

## G08-SALE_TIMESHEET_MARGIN-Q035

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q035
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where recorded time on a fixed-price engagement is deliberately capped or written off internally
  to protect a margin figure, that write-off is itself a visible, distinct action, not
  indistinguishable from time that was genuinely never performed.
WHY_IT_MATTERS: >
  An indistinguishable write-off makes a deliberately protected margin figure look like a
  genuinely efficient delivery, hiding real cost overrun from anyone reviewing the engagement.
DISCONFIRMING_OBSERVATION: >
  Time deliberately written off to protect a fixed-price engagement's margin leaves no record
  distinguishing it from work that genuinely never occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deliberately write off recorded time on a fixed-price engagement to protect its margin, and
  inspect whether that write-off is visibly distinct from time that never occurred.
```

## G08-SALE_TIMESHEET_MARGIN-Q036

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q036
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Two people with different cost rates recording an identical number of hours against the same
  engagement contribute different, individually correct amounts to the cost side of that
  engagement's margin, not an averaged or a single flat contribution per hour regardless of who
  logged it.
WHY_IT_MATTERS: >
  A flat per-hour cost regardless of who actually worked misattributes cost between two people whose
  real pay genuinely differs.
DISCONFIRMING_OBSERVATION: >
  Two people with materially different cost rates, each recording the same number of hours, are
  found contributing an identical cost amount to the engagement's margin.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Have two people with different cost rates record the same number of hours on one engagement, and
  compare each one's actual cost contribution to the resulting margin.
```

## G08-SALE_TIMESHEET_MARGIN-Q037

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q037
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A rate change applied company-wide, such as an annual rate-card refresh taking effect on a
  specific date, does not affect the margin for time recorded before that date on engagements that
  are still open and being actively margin-tracked.
WHY_IT_MATTERS: >
  A company-wide refresh that reaches backward into already-recorded time on open engagements
  misstates the cost of work already performed under the prior rate.
DISCONFIRMING_OBSERVATION: >
  A company-wide rate-card refresh changes the margin contribution of time recorded, on a still-open
  engagement, before the refresh's effective date.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Apply a company-wide rate-card refresh to a still-open, actively tracked engagement and inspect
  whether time recorded before the refresh date is affected.
```

## G08-SALE_TIMESHEET_MARGIN-Q038

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q038
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Where a person's time is recorded against an engagement but their cost rate was never configured
  at all, the margin computation either blocks, flags, or defaults in a documented way; it does not
  silently treat the missing rate as zero cost with no indication that a rate was actually missing.
WHY_IT_MATTERS: >
  Silently treating a missing rate as zero cost overstates a margin for a genuine data gap rather
  than a genuinely low-cost contribution.
DISCONFIRMING_OBSERVATION: >
  A person with no configured cost rate contributes zero cost to an engagement's margin with no
  flag or indication that the rate was actually missing.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Record time for a person whose cost rate was never configured, and inspect how that time's cost
  contribution is handled in the resulting margin.
```

## G08-SALE_TIMESHEET_MARGIN-Q039

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q039
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A margin figure that a role with account-level visibility sees for a customer's overall engagement
  history does not let that role infer any single person's specific cost rate by comparing margins
  across engagements that differ only in which one person was staffed.
WHY_IT_MATTERS: >
  Comparable, differenced engagement margins can leak a confidential individual rate to a role that
  was never granted rate-level access.
DISCONFIRMING_OBSERVATION: >
  A role with only account-level margin visibility can derive a specific person's cost rate by
  comparing two engagements that differ only in which one person was staffed.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a role with account-level margin visibility, compare two otherwise-identical engagements
  differing only in one staffed person, and attempt to derive that person's cost rate.
```

## G08-SALE_TIMESHEET_MARGIN-Q040

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q040
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Deleting an entire engagement's worth of time entries in bulk, whether as a correction or an
  error, after margin was reported for it produces one clear, traceable margin-adjustment event, not
  many small silent changes with no single explanation tying them together.
WHY_IT_MATTERS: >
  Many small untied changes look like unrelated noise rather than the single bulk event that
  actually caused them, making the real cause much harder to find later.
DISCONFIRMING_OBSERVATION: >
  A bulk deletion of an engagement's time entries produces many separate, unlinked changes to the
  reported margin with no single event tying them together.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Bulk-delete an engagement's time entries after its margin was reported, and inspect whether the
  resulting margin change is recorded as one traceable event.
```

## G08-SALE_TIMESHEET_MARGIN-Q041

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q041
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  On a time-and-materials engagement with no cap, the margin's sensitivity to individually recorded
  hours is at least as visible, per unit of time, as it is on a fixed-price engagement — erosion is
  not visible only on the fixed-price case while the equivalent effect on an uncapped engagement is
  hidden because revenue also grows with time.
WHY_IT_MATTERS: >
  If margin sensitivity is only surfaced for the fixed-price case, a business relying on this
  design would systematically under-monitor its uncapped, time-and-materials engagements.
DISCONFIRMING_OBSERVATION: >
  A per-hour change in recorded time visibly moves a fixed-price engagement's reported margin, but
  the equivalent change on an uncapped time-and-materials engagement produces no comparably visible
  margin signal.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Compare the visibility of a per-hour margin change on a fixed-price engagement against an
  equivalent change on an uncapped time-and-materials engagement.
```

## G08-SALE_TIMESHEET_MARGIN-Q042

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q042
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where a person is staffed on an engagement at a specific negotiated rate that differs from their
  general cost rate elsewhere in the business, the engagement-specific rate is what the margin uses
  for that person's contribution there, not their general rate silently substituted instead.
WHY_IT_MATTERS: >
  Substituting the general rate for a deliberately negotiated engagement-specific one misstates the
  true cost the business actually agreed to bear for that engagement.
DISCONFIRMING_OBSERVATION: >
  A person staffed at a negotiated engagement-specific rate has their margin contribution computed
  using their general cost rate instead.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Set a negotiated, engagement-specific cost rate for a person that differs from their general
  rate, and inspect which rate the engagement's margin actually uses.
```

## G08-SALE_TIMESHEET_MARGIN-Q043

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q043
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Reopening a closed, already-margin-reported engagement to record a legitimate missed time entry
  produces a visible restatement of that engagement's margin, distinguishable from an engagement
  whose margin was correct on first close.
WHY_IT_MATTERS: >
  An indistinguishable reopening makes it impossible to later tell a legitimate late correction
  from an engagement whose original closing figure was simply wrong.
DISCONFIRMING_OBSERVATION: >
  Reopening a closed, margin-reported engagement to add a missed time entry produces a margin
  change with no visible restatement distinguishing it from a normally correct closing figure.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close and report the margin for an engagement, reopen it to record a legitimate missed entry, and
  inspect whether the resulting margin change is a visible restatement.
```

## G08-SALE_TIMESHEET_MARGIN-Q044

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q044
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A cost-rate history retained for margin recomputation purposes is itself subject to the same
  confidentiality boundary as the current rate — being able to see that a rate changed on a certain
  date does not imply being shown what the rate actually was, for a role not otherwise entitled to
  see it.
WHY_IT_MATTERS: >
  A history view that exposes past rate values to a role restricted from the current rate is a
  side-door around the same confidentiality boundary Q005 requires for the present.
DISCONFIRMING_OBSERVATION: >
  A role restricted from seeing a person's current cost rate can nonetheless see that person's past
  rate values through a rate-history view used for margin recomputation.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  As a role restricted from a person's current cost rate, attempt to view that person's past rate
  values through any rate-history or margin-recomputation view.
```

## G08-SALE_TIMESHEET_MARGIN-Q045

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q045
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where recorded time for the same person is split across two engagements in the same period, an
  error correcting one engagement's hours does not silently alter the cost attributed to the other
  engagement's margin.
WHY_IT_MATTERS: >
  A correction that leaks across engagements misstates the margin of an engagement that had nothing
  to do with the original error.
DISCONFIRMING_OBSERVATION: >
  Correcting one engagement's recorded hours for a person also changes the margin of a different
  engagement that same person split their time with, with no relationship between the two errors.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Split one person's time across two engagements in the same period, correct an hours error on one,
  and inspect whether the other engagement's margin was affected.
```

## G08-SALE_TIMESHEET_MARGIN-Q046

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q046
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where the business has any mechanism for interim margin tracking over an engagement's life rather
  than only a single final number, a fixed-price engagement's margin trend shows erosion happening
  incrementally as time accrues, rather than the margin appearing static until one large
  recalculation at closure reveals the full erosion at once.
WHY_IT_MATTERS: >
  A margin that only reveals its full erosion at closure gives no chance to notice and respond to a
  worsening engagement while it is still in progress.
DISCONFIRMING_OBSERVATION: >
  An interim-tracking mechanism exists, yet a fixed-price engagement's margin trend shows no
  incremental erosion as time accrues, only a single large drop recorded at closure.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Track a fixed-price engagement's margin over its life using any available interim mechanism, and
  inspect whether erosion appears incrementally or only as one drop at closure.
```

## G08-SALE_TIMESHEET_MARGIN-Q047

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q047
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A person's cost rate is versioned and governed distinctly from any general personnel or
  HR-side rate-change process, such that a margin recomputation does not depend on directly reading
  a system of record whose access rules are governed by a different, broader personnel-data
  permission boundary than margin reporting itself uses.
WHY_IT_MATTERS: >
  If margin recomputation directly depends on a broader personnel-data store, whoever has access to
  run a margin recomputation implicitly gains a path into personnel data they were never granted
  access to on its own terms.
DISCONFIRMING_OBSERVATION: >
  Running a margin recomputation requires or grants access to a general personnel-data record whose
  own permission boundary is broader than margin reporting's stated access rules.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a role permitted to run margin recomputations but not general personnel-data access, attempt a
  recomputation and observe whether it requires or exposes personnel-data access beyond margin
  reporting's own boundary.
```

## G08-SALE_TIMESHEET_MARGIN-Q048

```yaml
QID: G08-SALE_TIMESHEET_MARGIN-Q048
MODULE: sale_timesheet_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where two different currencies are involved because a person's cost rate is set in one currency
  and the engagement bills the customer in another, the margin computation tracks each leg's own
  rate at the time it applied, rather than assuming the rate used for the customer-facing currency
  conversion also governs the internal cost-side conversion.
WHY_IT_MATTERS: >
  Assuming one shared rate across a customer-facing conversion and an unrelated internal cost
  conversion produces a margin that does not correspond to either conversion that actually occurred.
DISCONFIRMING_OBSERVATION: >
  A margin computed where the cost-side currency and the customer-facing currency differ cannot be
  reproduced using each leg's own actual, independently recorded conversion rate.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set a person's cost rate in one currency and bill the customer in another for the same
  engagement, and attempt to reproduce the resulting margin from each leg's own conversion rate.
```

