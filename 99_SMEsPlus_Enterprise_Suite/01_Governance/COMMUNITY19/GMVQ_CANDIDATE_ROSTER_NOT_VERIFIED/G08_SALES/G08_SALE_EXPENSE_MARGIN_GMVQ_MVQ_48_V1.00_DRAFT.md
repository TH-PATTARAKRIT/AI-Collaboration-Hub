# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_expense_margin Module Bridge MVQ Bank (Margin Variant)

**Document ID:** GMVQ-G08-SALE_EXPENSE_MARGIN-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_expense_margin`
**Wave:** W2
**Author Cell:** P-S4 (GMVQ Question Factory — Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `sale_expense_margin` — a BRIDGE per
GMVQ_BRIDGE_MODULE_RULE_V1.00 and one of the five margin variants named in the Five-Margin Problem
(GROUP_BRIEF_G08_SALES.md). Per that brief, this bank's cost is specifically A THIRD PARTY'S
INVOICE TO THE BUSINESS, arriving after the fact, possibly in another currency and another period —
never a standing item attribute (`sale_margin`'s ground), a stock valuation layer (`sale_stock_margin`'s
ground), or a production outcome (`sale_mrp_margin`'s ground); this cell stayed off those three cost
bases throughout authoring. This bank also does not restate the sibling `sale_expense` bank's seam
questions about the re-invoiced customer line itself (approval gating, re-invoicing basis, double
billing, tax, employee-detail exposure) — it asks only what the LATENESS AND EXTERNALITY of the true
cost does to the margin figure computed from it: a margin computed and reported before the supplier's
actual invoice ever arrives, and whether it is ever restated; a supplier invoicing more, or less,
than the employee originally claimed; two different currency legs (cost side, revenue side) that a
margin figure must not silently assume are the same; a cost landing in an accounting period after the
revenue it relates to was already recognised; an expense never claimed at all, leaving a margin
permanently computed against a cost of zero with nothing to say so; a supplier credit arriving after
the margin was already reported; and whether anything at all signals that a currently healthy-looking
margin is healthy only because its true cost has not arrived yet. Every question was tested against
the bridge rule: if it would read equally well with no margin figure being computed at all, it was cut.

The question text is source-neutral and does not expose vendor or product names, field names,
methods, schema, XML IDs, API shapes, or implementation algorithms. `MODULE: sale_expense_margin`
appears only in the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` stating a concrete failure state,
  never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses about the
  timing, revisability and externality of a third-party-invoiced cost inside a margin figure; none
  was trimmed or stretched to hit count.
- Question text is source-neutral: no vendor or product name, no technical identifier (field,
  model, method, XML ID, API path); `sale_expense_margin` appears only in the `MODULE:` field.
- FIVE-MARGIN PROBLEM discipline: this bank's cost basis is a third party's invoice arriving after
  the fact. It does not use a standing item cost, a stock valuation layer, or a production outcome
  as its ground — those belong to `sale_margin`, `sale_stock_margin`, and `sale_mrp_margin`
  respectively and were deliberately avoided.
- BRIDGE MODULE per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question fails only at the seam between a
  late, external, foreign-currency-prone cost and the margin figure computed from it. None restates
  the sibling `sale_expense` bank's own seam ground (approval gating, re-invoicing basis, tax on the
  customer line, employee-detail exposure, double billing) — that bank owns the billing seam; this
  bank owns only the margin arithmetic drawn from the same underlying cost.
- Cross-check against the sibling `sale_timesheet_margin` bank (the other margin bank authored by
  this same cell in this run) was performed at authoring time: no question or `DISCONFIRMING_OBSERVATION`
  in either bank shares a failure event with the other. This bank's failure events are all rooted in
  an external invoice's timing, currency and revisability; the sibling's are all rooted in an
  internally recorded person-hour's timing, rate and revisability. No pair was found to collapse to
  the same underlying event.
- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G08_SALES/*.md
  2>/dev/null | sort` was run before authoring, against the `sale_expense` bank already drafted in
  this run and the group brief's explicit list of what `sale_margin`, `sale_stock_margin`, and
  `sale_mrp_margin` own. No overlap found or accepted without direct verification.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/evidence.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## G08-SALE_EXPENSE_MARGIN-Q001

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q001
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A margin figure computed using the employee's claimed amount as a stand-in for cost, before the
  supplier's actual invoice has arrived, is distinguishable from a margin computed after the actual
  invoice is known — the two are never presented identically.
WHY_IT_MATTERS: >
  A viewer who cannot tell a provisional margin from a settled one may make a decision based on a
  figure that is still expected to move.
DISCONFIRMING_OBSERVATION: >
  A margin based only on the employee's claimed amount is shown with no distinguishing indicator
  from a margin already confirmed against the supplier's actual invoice.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Compute a margin for a sale whose only cost input is an employee's claimed amount, with no
  supplier invoice yet recorded, and compare its presentation to a fully settled margin.
```

## G08-SALE_EXPENSE_MARGIN-Q002

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q002
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  When the supplier's actual invoice later differs from the employee's original claim, the margin
  figure for that specific sale is restated, or at minimum flagged as stale, somewhere reviewable —
  it does not stand permanently at its original, now-incorrect value with nothing indicating a
  restatement is due.
WHY_IT_MATTERS: >
  A margin that never catches up to the true cost silently misstates profitability for as long as
  anyone continues to rely on it.
DISCONFIRMING_OBSERVATION: >
  A supplier invoice recorded at a different amount than the employee's claim produces no
  restatement, flag, or reviewable indicator against the sale's already-reported margin.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Report a margin based on an employee's claim, then record the supplier's actual invoice at a
  different amount, and inspect whether the earlier margin figure is restated or flagged.
```

## G08-SALE_EXPENSE_MARGIN-Q003

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q003
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A supplier invoicing an amount higher than the employee originally claimed produces a downward
  margin correction that is traceable to that specific sale, not blended silently into a later
  period's aggregate margin with no link back to the originating sale.
WHY_IT_MATTERS: >
  A correction with no traceable link back to its sale cannot be explained to anyone who asks why
  a later period's margin moved.
DISCONFIRMING_OBSERVATION: >
  A supplier invoice higher than the employee's claim changes an aggregate margin figure with no
  traceable adjustment record pointing back to the originating sale.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record a supplier invoice higher than the employee's original claim for a sale whose margin was
  already reported, and attempt to trace the resulting correction back to that sale.
```

## G08-SALE_EXPENSE_MARGIN-Q004

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q004
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A supplier invoicing an amount lower than the employee originally claimed produces a
  corresponding upward margin correction traceable to the same originating sale.
WHY_IT_MATTERS: >
  A margin permanently understated because a favorable correction was never applied hides real
  profitability from whoever relies on the figure.
DISCONFIRMING_OBSERVATION: >
  A supplier invoice lower than the employee's claim produces no upward correction to the
  originating sale's previously reported margin.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record a supplier invoice lower than the employee's original claim for a sale whose margin was
  already reported, and inspect whether an upward correction is applied and traceable.
```

## G08-SALE_EXPENSE_MARGIN-Q005

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q005
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  The currency rate used to value the cost side of the margin (the supplier's invoice, or its
  employee-claim stand-in) and the rate used to value the revenue side are each captured explicitly,
  so a margin computed across the two never silently assumes they were the same rate when they were
  genuinely different.
WHY_IT_MATTERS: >
  Assuming a single shared rate across two legs that were actually priced at different moments
  produces a margin figure that cannot be reconciled to either leg's real value.
DISCONFIRMING_OBSERVATION: >
  A margin computed from a foreign-currency cost and a differently-timed revenue leg cannot be
  reproduced using the two legs' actual, individually recorded rates.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Compute a margin where the cost leg and the revenue leg were each converted at genuinely
  different points in time, and attempt to reproduce the reported margin from each leg's own rate.
```

## G08-SALE_EXPENSE_MARGIN-Q006

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q006
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where the cost-side rate and the revenue-side rate genuinely differ because of the real timing gap
  between the expense and the customer billing, the reported margin reflects the actual pair of
  rates used rather than a single rate applied to both legs for computational convenience.
WHY_IT_MATTERS: >
  Collapsing two genuinely different rates into one for convenience manufactures a margin figure
  that does not correspond to any real financial event.
DISCONFIRMING_OBSERVATION: >
  A margin computation applies one single exchange rate to both the cost leg and the revenue leg
  despite the two legs having been actually converted at documented, different rates.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a case with a documented timing gap producing two different real rates on the cost and
  revenue legs, and inspect which rate or rates the margin computation actually used.
```

## G08-SALE_EXPENSE_MARGIN-Q007

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q007
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  An expense cost landing in an accounting period after the period in which the related sale's
  revenue was already recognised is attributed back to that originating sale's margin, rather than
  only affecting whichever period it happens to land in with no link to the earlier revenue.
WHY_IT_MATTERS: >
  A cost detached from the revenue it belongs to misstates both the earlier period (overstated
  margin) and the later period (an unexplained cost with no matching revenue).
DISCONFIRMING_OBSERVATION: >
  A late-arriving cost is recorded and affects only the period it lands in, with no attribution
  back to the sale and revenue period it actually relates to.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Recognise revenue for a sale in one period, then record its true cost in a later period, and
  inspect whether that cost is attributed back to the originating sale's margin.
```

## G08-SALE_EXPENSE_MARGIN-Q008

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q008
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When cost and revenue for the same sale fall in different periods, the margin reported during the
  revenue period is distinguishable from the margin reported once the late cost is known, so a
  viewer can tell whether a given margin figure is final or still open.
WHY_IT_MATTERS: >
  Without that distinction, a viewer has no way to know whether a margin figure they are looking at
  can still change.
DISCONFIRMING_OBSERVATION: >
  A margin reported before a known cost has arrived and the same margin after that cost is booked
  are presented identically with no indicator of which state applies.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  View a sale's margin before its true cost has arrived, then again after, and compare whether the
  two presentations are distinguishable.
```

## G08-SALE_EXPENSE_MARGIN-Q009

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q009
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  An expense that an employee never claims at all, and so is never captured as a cost, results in a
  margin for that sale that carries some mechanism flagging it as based on an incomplete cost — or
  the design explicitly has no such mechanism, and that absence is at least a consistent, known
  answer rather than an accidental gap.
WHY_IT_MATTERS: >
  A margin permanently overstated by a cost that was simply never claimed looks identical to a
  genuinely profitable sale, with no way for anyone to tell the difference.
DISCONFIRMING_OBSERVATION: >
  A sale with a real, known but never-claimed cost shows a margin with no distinguishable
  difference from a sale genuinely incurring no such cost, and no mechanism anywhere signals the gap.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Identify a sale where a cost was incurred but the corresponding expense was never submitted, and
  inspect whether the reported margin shows any sign of an unclaimed cost.
```

## G08-SALE_EXPENSE_MARGIN-Q010

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q010
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A configured or observable staleness window — time elapsed since the sale with no corresponding
  cost yet claimed — is either used to flag a margin as suspect, or no such mechanism exists at
  all, and which of the two is true is a consistent, discoverable answer.
WHY_IT_MATTERS: >
  Without knowing which answer holds, nobody can tell whether a high margin with old, uncosted
  sales is a genuine signal or simply a design gap nobody addressed.
DISCONFIRMING_OBSERVATION: >
  Two sales of the same age with no cost recorded are treated inconsistently by whatever staleness
  mechanism (or absence of one) the design has, with no policy explaining the difference.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Leave two comparable sales with no cost claimed for the same elapsed time and compare whether and
  how each is flagged as having a stale, incomplete cost basis.
```

## G08-SALE_EXPENSE_MARGIN-Q011

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q011
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A supplier credit note issued against a previously invoiced expense, arriving after that
  expense's cost was already reflected in a reported margin, produces a distinct, traceable
  adjustment to the originating sale's margin rather than an unlinked credit recorded elsewhere in
  the accounts.
WHY_IT_MATTERS: >
  An unlinked credit means the margin benefit of a real cost reduction never reaches the sale it
  actually belongs to.
DISCONFIRMING_OBSERVATION: >
  A supplier credit against a previously booked cost is recorded with no traceable adjustment to
  the specific sale's margin that cost originally affected.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Book a supplier invoice as cost for a sale's margin, then receive a supplier credit against that
  same invoice, and trace whether the sale's margin is adjusted accordingly.
```

## G08-SALE_EXPENSE_MARGIN-Q012

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q012
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Two supplier credits of different sizes, arriving against two different originating sales, are
  each attributed to their own sale's margin, not pooled into one undifferentiated adjustment.
WHY_IT_MATTERS: >
  Pooling credits erases which specific sale actually benefited, corrupting per-sale profitability
  analysis with an arbitrary allocation.
DISCONFIRMING_OBSERVATION: >
  Two supplier credits belonging to two different sales are applied as one combined adjustment with
  no way to tell which sale received how much of the benefit.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Receive two separate supplier credits against costs originally attributed to two different
  sales, and inspect how each credit is attributed in the resulting margin figures.
```

## G08-SALE_EXPENSE_MARGIN-Q013

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q013
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A margin currently reported as healthy while its entire cost side remains provisional — no
  supplier invoice received yet — is distinguishable, wherever a reviewer would look, from a margin
  whose cost side is fully settled.
WHY_IT_MATTERS: >
  A healthy-looking margin that is only healthy because its cost has not yet arrived can lead to a
  commercial decision (repeat the deal, discount further) made on a number that is not yet real.
DISCONFIRMING_OBSERVATION: >
  A margin with a fully provisional cost side is displayed identically, in every place a reviewer
  would check, to a margin whose cost is fully known and settled.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Report a margin for a sale with no supplier invoice yet received against its expense cost, and
  compare its presentation everywhere it appears against a fully settled sale's margin.
```

## G08-SALE_EXPENSE_MARGIN-Q014

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q014
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The point at which a provisional margin becomes a settled one — the supplier invoice being
  recorded — is a single, identifiable event, not something that happens gradually or ambiguously
  across several partial updates with no final, identifiable state.
WHY_IT_MATTERS: >
  An ambiguous transition makes it impossible to know, at any given moment, whether a margin figure
  can still be relied upon as final.
DISCONFIRMING_OBSERVATION: >
  A margin's transition from provisional to settled cannot be pinned to a single identifiable event
  and instead appears to shift gradually with no clear final state.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Record the supplier invoice that settles a previously provisional margin and inspect whether the
  transition is a single identifiable event or an ambiguous, gradual one.
```

## G08-SALE_EXPENSE_MARGIN-Q015

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q015
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Multiple sales sharing costs from a single consolidated supplier invoice — for example one trip
  billed across several customer engagements — have that invoice's total apportioned to each sale's
  margin in a way that is visible and consistent, not left entirely to whichever sale happened to be
  updated first.
WHY_IT_MATTERS: >
  An arbitrary, first-touched apportionment can attribute an entire shared cost to one customer
  while leaving the others looking artificially more profitable than they are.
DISCONFIRMING_OBSERVATION: >
  A single consolidated supplier invoice covering several sales is applied in full to only the
  first sale processed, leaving the others' margins unaffected by a cost they should share.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record one consolidated supplier invoice covering costs for more than one sale and inspect how
  its total is apportioned across each sale's margin.
```

## G08-SALE_EXPENSE_MARGIN-Q016

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q016
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A margin already reported to a role without visibility into individual cost detail is not
  silently changed underneath that role by a later cost correction with no indication that a
  change occurred.
WHY_IT_MATTERS: >
  A number that moves with no visible signal to the person relying on it undermines their ability
  to trust any figure they were previously given.
DISCONFIRMING_OBSERVATION: >
  A margin figure visible to a role without cost detail access changes value with no indicator,
  timestamp, or notice that a correction occurred.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  As a role without cost-detail access, observe a margin figure, trigger a cost correction behind
  it, and check whether any signal of the change reaches that role.
```

## G08-SALE_EXPENSE_MARGIN-Q017

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q017
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Reversing the customer sale entirely (cancellation or full credit) after a supplier cost has
  already been booked against its margin unwinds or flags the margin figure for that sale, rather
  than leaving a margin computed for a sale that no longer commercially stands.
WHY_IT_MATTERS: >
  A margin left standing for a sale that was cancelled misrepresents actual realised profitability
  in any report that still counts it.
DISCONFIRMING_OBSERVATION: >
  A sale is fully cancelled after its cost was booked and its margin was reported, and that margin
  remains visible with no flag or adjustment reflecting the cancellation.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Book a supplier cost and report a margin for a sale, then fully cancel that sale, and inspect
  whether the margin figure is unwound or flagged.
```

## G08-SALE_EXPENSE_MARGIN-Q018

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q018
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A supplier invoice for the cost side that arrives but is disputed or contested by the business
  (rather than simply differing in amount) leaves the margin in an explicitly unresolved state,
  rather than adopting either the disputed figure or the employee's original claim by default.
WHY_IT_MATTERS: >
  Silently defaulting to either figure during a genuine dispute reports a margin that may need to
  move again once the dispute resolves, with nothing signaling that possibility.
DISCONFIRMING_OBSERVATION: >
  A disputed supplier invoice is adopted, or ignored in favor of the employee's claim, in the
  margin figure with no indication that the underlying cost is actually contested.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a supplier invoice that the business formally disputes, and inspect how the sale's margin
  reflects that dispute, if at all.
```

## G08-SALE_EXPENSE_MARGIN-Q019

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q019
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  The margin figure's cost-timing gap — sale recognised now, true cost known later — is treated
  consistently regardless of whether the underlying expense is large or small; there is no
  threshold below which the late-cost handling is simply skipped while above it is tracked.
WHY_IT_MATTERS: >
  An undisclosed materiality threshold means small late costs quietly and permanently escape the
  same correction discipline larger ones receive, for no stated reason.
DISCONFIRMING_OBSERVATION: >
  A small late-arriving cost is not attributed back to its sale's margin the way a large one
  documented as handled correctly would be, with no stated threshold explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare how a small late-arriving cost and a large late-arriving cost are each attributed back to
  their respective sales' margins.
```

## G08-SALE_EXPENSE_MARGIN-Q020

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q020
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Where the business has configured a policy for how long to wait for a supplier invoice before
  treating a margin as final regardless, that policy is applied uniformly across sales and is
  itself visible, not an implicit default nobody actually set.
WHY_IT_MATTERS: >
  An invisible, undocumented finality rule means nobody can explain why one sale's margin was
  finalized without its true cost while another was not.
DISCONFIRMING_OBSERVATION: >
  Two comparable sales with equally overdue supplier invoices are finalized as final margins at
  different points with no documented, uniformly applied policy explaining the difference.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Configure or locate the policy for finalizing a margin despite a missing supplier invoice, and
  compare its application across two comparable overdue sales.
```

## G08-SALE_EXPENSE_MARGIN-Q021

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q021
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An expense originally marked non-billable, later reclassified and billed to the customer, does
  not silently update the margin of a sale already reported as closed before the reclassification
  happened, without an explicit reopening step.
WHY_IT_MATTERS: >
  A closed, already-communicated margin figure that changes with no visible reopening event
  undermines confidence in every other figure marked closed.
DISCONFIRMING_OBSERVATION: >
  Reclassifying a non-billable expense as billable after its sale's margin was already closed
  changes that closed margin with no visible reopening event.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close a sale's margin, then reclassify a previously non-billable expense on that sale as
  billable, and inspect whether the closed margin changes and how.
```

## G08-SALE_EXPENSE_MARGIN-Q022

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q022
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where a margin computed from the employee's claim and a margin later computed from the actual
  supplier invoice happen to arrive at the same amount, a record of which of the two figures was
  actually used at report time still exists — coincidental agreement does not erase the
  provisional-versus-final distinction.
WHY_IT_MATTERS: >
  If coincidental agreement erases the distinction, the next case where the two figures genuinely
  differ has no established pattern of being tracked either.
DISCONFIRMING_OBSERVATION: >
  A margin whose claim-based and invoice-based figures happen to match shows no record of which
  basis was actually used to produce the reported figure.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce a case where the employee's claim and the supplier's eventual invoice are for the same
  amount, and inspect whether the margin record still states which one was used.
```

## G08-SALE_EXPENSE_MARGIN-Q023

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q023
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where a single sale draws on expenses submitted by more than one employee, a delay in just one of
  those employees' claims or one supplier's invoice does not block or corrupt the margin
  contribution already known from the others — each cost line is tracked and reconciled
  independently.
WHY_IT_MATTERS: >
  Letting one slow cost line block or corrupt the whole sale's margin computation makes the figure
  only as timely as its slowest contributor, for no necessary reason.
DISCONFIRMING_OBSERVATION: >
  A single delayed cost line among several on the same sale prevents the margin from reflecting the
  other, already-known cost lines correctly.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record several cost lines for one sale from different employees or suppliers, delay just one of
  them, and inspect the margin's treatment of the others.
```

## G08-SALE_EXPENSE_MARGIN-Q024

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q024
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Access to the margin figure and access to the underlying supplier invoice or employee claim
  amount behind it are governed by distinct permission scopes, so a role permitted to see the
  margin outcome is not automatically shown the granular cost detail behind it.
WHY_IT_MATTERS: >
  Collapsing the two permissions into one exposes granular, potentially sensitive cost detail to
  anyone who only needed to know whether a sale was profitable.
DISCONFIRMING_OBSERVATION: >
  A role granted visibility into a sale's margin outcome can, through that same access, also see
  the granular supplier invoice or employee claim amounts behind it.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a role granted margin-outcome visibility only, attempt to access the underlying supplier
  invoice or employee claim detail for that same sale.
```

## G08-SALE_EXPENSE_MARGIN-Q025

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q025
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  In a multi-company setup, the margin figure for a sale in one company is computed only from costs
  booked as attributable to that same company; a supplier invoice recorded against a different
  company's books does not silently feed another company's customer margin.
WHY_IT_MATTERS: >
  A cross-company leak of cost into the wrong entity's margin corrupts both companies' separately
  reportable financial results.
DISCONFIRMING_OBSERVATION: >
  A supplier invoice booked under one company is found contributing to the reported margin of a
  sale belonging to a different company.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  In a multi-company configuration, book a supplier invoice under one company and inspect whether
  it appears in the margin of a sale belonging to a different company.
```

## G08-SALE_EXPENSE_MARGIN-Q026

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q026
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When the employee's claim and the supplier's invoice are recorded in two different foreign
  currencies, neither matching the customer's invoicing currency, the margin computation tracks
  each leg's own conversion rather than collapsing both into one assumed rate.
WHY_IT_MATTERS: >
  Collapsing a genuinely three-currency case into one rate compounds an error into the reported
  margin that cannot be traced back to any real conversion event.
DISCONFIRMING_OBSERVATION: >
  A three-currency cost case produces a margin figure that cannot be reproduced from the two
  separately recorded conversion rates actually used for the claim and the invoice.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record an employee claim and a supplier invoice in two different foreign currencies for the same
  cost, neither matching the customer's invoicing currency, and attempt to reproduce the margin from
  each leg's own rate.
```

## G08-SALE_EXPENSE_MARGIN-Q027

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q027
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A margin figure exported or reported at a point in time before a known-pending supplier invoice
  has arrived carries some indication that it is not final, distinguishable from a margin reported
  after all expected costs for that sale are already in.
WHY_IT_MATTERS: >
  An exported figure with no such indication can circulate outside the system and be treated as
  final long after it has been superseded.
DISCONFIRMING_OBSERVATION: >
  A margin exported while a known supplier invoice is still pending carries no indication,
  anywhere in the export, that it is provisional.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Export or report a margin for a sale with a known-pending supplier invoice and inspect whether
  the export indicates the figure is provisional.
```

## G08-SALE_EXPENSE_MARGIN-Q028

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q028
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a single supplier expense is allocated across more than one sale, each sale's margin
  reflects only its own allocated share of that cost, and the shares sum to the expense's full
  recorded amount without double-counting or dropping any portion.
WHY_IT_MATTERS: >
  Double-counting or dropping a shared cost across the sales that share it would overstate or
  understate profitability for each one, and the two errors would not be visible from either sale
  alone.
DISCONFIRMING_OBSERVATION: >
  The cost portions attributed to each sale from a single allocated supplier expense do not sum to
  that expense's full recorded amount, or the same portion appears in more than one sale's margin.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Allocate a single supplier expense across two or more sales, then inspect each sale's margin
  contribution from that expense and total them against its full recorded amount.
```

## G08-SALE_EXPENSE_MARGIN-Q029

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q029
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Voiding an employee's expense claim entirely, found to be a genuine error rather than fraud,
  after its estimated cost had already been folded into a reported margin, removes that estimated
  cost from the margin cleanly, rather than leaving a phantom cost with nothing behind it.
WHY_IT_MATTERS: >
  A phantom cost that is never removed permanently understates a margin for a cost that never
  actually existed.
DISCONFIRMING_OBSERVATION: >
  Voiding an employee's claim after its estimate was folded into a reported margin leaves that
  margin unchanged, still reflecting the now-voided estimated cost.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Fold an employee claim's estimate into a reported margin, then void that claim as an error, and
  inspect whether the margin is corrected.
```

## G08-SALE_EXPENSE_MARGIN-Q030

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q030
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  The margin figure's cost basis for a given sale can be traced, on demand, back to the specific
  expense claim or supplier invoice it was drawn from; there is no version of the margin that is a
  bare number with no path back to what produced it.
WHY_IT_MATTERS: >
  A margin nobody can trace back to its source cost cannot be verified, corrected, or trusted when
  it is challenged.
DISCONFIRMING_OBSERVATION: >
  A reported margin figure cannot be traced back, on demand, to the specific expense claim or
  supplier invoice that produced its cost side.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Take a reported margin figure for a sale and attempt to trace its cost side back to the specific
  expense claim or supplier invoice that produced it.
```

## G08-SALE_EXPENSE_MARGIN-Q031

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q031
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A markup or fixed re-invoicing price set on the customer-facing side, independent of true cost,
  does not by itself hide the underlying true-cost timing gap in the margin calculation — the
  margin still reflects true cost once known, not just the fixed customer price minus the
  employee's original estimate.
WHY_IT_MATTERS: >
  A margin permanently anchored to the employee's estimate rather than the true settled cost
  understates the real timing risk a fixed-price re-invoicing arrangement carries.
DISCONFIRMING_OBSERVATION: >
  A fixed-price re-invoiced sale's margin continues to be computed against the employee's original
  estimate even after the true supplier cost is known and differs from it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Re-invoice an expense at a fixed customer price, record the true supplier cost once it differs
  from the employee's estimate, and inspect which figure the sale's margin actually uses.
```

## G08-SALE_EXPENSE_MARGIN-Q032

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q032
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Reporting periods that close (month-end, quarter-end) while a margin remains provisional either
  carry that margin forward as still-open in the next period's reporting, or explicitly note it was
  closed provisional — it does not simply vanish from future visibility once its original period
  closes.
WHY_IT_MATTERS: >
  A provisional margin that disappears at period-close means its eventual true value, once known,
  has nowhere to be reported at all.
DISCONFIRMING_OBSERVATION: >
  A margin still provisional at period-close is absent from both that period's closing report and
  any later reporting once its true cost becomes known.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Close a reporting period while a sale's margin remains provisional, and check whether that
  margin is carried forward, flagged, or reported once its true cost later arrives.
```

## G08-SALE_EXPENSE_MARGIN-Q033

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q033
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A supplier invoice that arrives at a value the business considers implausible relative to what
  was claimed is handled through a distinguishable state from a routine, expected correction, not
  applied to the margin through the same silent path.
WHY_IT_MATTERS: >
  Treating an implausible cost identically to a routine correction removes the one moment a
  reviewer might have caught an error or an irregularity before it reached the margin figure.
DISCONFIRMING_OBSERVATION: >
  A supplier invoice far outside any plausible range for the claim it corresponds to updates the
  sale's margin through the exact same silent path as an ordinary, small correction.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a supplier invoice at an implausible multiple of the original employee claim and compare
  how the resulting margin update is handled against an ordinary correction.
```

## G08-SALE_EXPENSE_MARGIN-Q034

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q034
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  When a supplier expense already counted in a sale's margin is subsequently rejected or fully
  credited back by the supplier, the margin recalculates to remove that cost, rather than
  continuing to reflect a cost that, in the end, was never actually incurred.
WHY_IT_MATTERS: >
  A margin that keeps counting a reversed cost overstates how unprofitable a sale actually was,
  misleading anyone who reviews it after the correction was made.
DISCONFIRMING_OBSERVATION: >
  A sale's margin still reflects the cost of a supplier expense after that expense has been fully
  rejected or credited back by the supplier.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Include a supplier expense in a sale's margin, then fully reject or credit that expense back,
  and check whether the margin recalculates to exclude it.
```

## G08-SALE_EXPENSE_MARGIN-Q035

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q035
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Configuration for how a re-invoicing markup interacts with margin reporting, such as a fixed
  uplift percentage, is itself visible in whatever margin report references it, rather than the
  margin number being unexplainable without separately knowing the configuration.
WHY_IT_MATTERS: >
  A margin figure that depends on an invisible configuration value cannot be sanity-checked or
  explained by anyone who does not already know that configuration exists.
DISCONFIRMING_OBSERVATION: >
  A margin report shows a figure that depends on a configured markup uplift, with no reference to
  that configuration anywhere the figure is presented.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Configure a fixed markup uplift affecting margin reporting and inspect whether that configuration
  is referenced anywhere the resulting margin is shown.
```

## G08-SALE_EXPENSE_MARGIN-Q036

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q036
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where no explicit foreign-exchange gain or loss handling exists for the gap between the rate at
  expense-claim time and the rate at supplier-invoice time, that gap is not silently absorbed into
  the margin as if it were part of the underlying cost — the two are distinguishable if the
  business ever looks.
WHY_IT_MATTERS: >
  Blending a currency timing effect into the operating margin figure misattributes an exchange-rate
  outcome as if it were a change in the actual underlying cost of the work.
DISCONFIRMING_OBSERVATION: >
  A margin movement caused purely by a currency rate difference between claim time and invoice
  time cannot be distinguished, in the record, from a movement caused by the underlying cost itself
  changing.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Produce a case where only the exchange rate moved between claim time and invoice time, with the
  underlying cost otherwise unchanged, and inspect whether the margin record distinguishes the two.
```

## G08-SALE_EXPENSE_MARGIN-Q037

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q037
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A sale whose entire cost side consists of expenses still pending supplier invoices reports a
  margin state that is meaningfully distinguishable from a sale whose cost side is fully known,
  even where their headline percentages happen to look similar.
WHY_IT_MATTERS: >
  Two sales that look equally profitable at a glance, when one is entirely provisional, mislead
  whoever is comparing them for a decision.
DISCONFIRMING_OBSERVATION: >
  A fully provisional sale and a fully settled sale with similar headline margin percentages are
  presented with no distinguishing indicator of their different certainty.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Compare a sale whose cost is entirely pending against one whose cost is fully settled, where
  both show a similar headline margin percentage, for any distinguishing indicator.
```

## G08-SALE_EXPENSE_MARGIN-Q038

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q038
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  The originating employee's identity and the specific supplier's identity are not required to be
  exposed on the margin report itself for the cost-timing and correction mechanics above to
  function — margin correctness does not depend on that detail being visible at the
  margin-reporting layer.
WHY_IT_MATTERS: >
  If margin correctness silently depends on identity detail being shown, restricting that detail
  for privacy (per the sibling billing bank) would break the margin figure itself.
DISCONFIRMING_OBSERVATION: >
  Restricting employee or supplier identity detail from a margin report causes the margin
  computation or its correction mechanics to stop functioning correctly.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Restrict employee and supplier identity detail from a margin report's visibility and verify
  whether the margin figure and its correction mechanics still function correctly.
```

## G08-SALE_EXPENSE_MARGIN-Q039

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q039
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A duplicate supplier invoice recorded twice in error for the same original expense claim does not
  double-count that cost against the sale's margin.
WHY_IT_MATTERS: >
  A duplicated cost understates a margin for a reason that has nothing to do with the sale's actual
  economics and is purely a data-entry artifact.
DISCONFIRMING_OBSERVATION: >
  The same supplier invoice recorded twice in error is reflected as two separate costs against the
  same sale's margin.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record the same supplier invoice twice against the same original expense claim and inspect
  whether the sale's margin reflects the cost once or twice.
```

## G08-SALE_EXPENSE_MARGIN-Q040

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q040
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When the customer's invoice for the re-invoiced expense is itself cancelled or credited after the
  true supplier cost is already known, the margin computation reflects the actual net revenue
  realised, not the originally billed amount that no longer stands.
WHY_IT_MATTERS: >
  A margin computed against revenue that was subsequently reversed overstates profitability for a
  sale that did not, in the end, realise that revenue.
DISCONFIRMING_OBSERVATION: >
  A sale whose customer-facing invoice was cancelled or credited still shows a margin computed
  against the original, no-longer-standing billed amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel or credit a customer invoice for a re-invoiced expense after its true supplier cost is
  already known, and inspect whether the sale's margin reflects the reduced net revenue.
```

## G08-SALE_EXPENSE_MARGIN-Q041

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q041
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A change to the standard markup or fixed-price policy going forward does not retroactively alter
  the margin already computed and reported for sales invoiced under the prior policy.
WHY_IT_MATTERS: >
  Retroactively repricing historical margins under a new policy misstates the profitability that
  was actually realised under the policy that genuinely applied at the time.
DISCONFIRMING_OBSERVATION: >
  Changing the standard markup policy alters the already-reported margin of a sale invoiced before
  the policy change.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Report a margin under one markup policy, change the policy going forward, and inspect whether the
  earlier sale's reported margin changed.
```

## G08-SALE_EXPENSE_MARGIN-Q042

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q042
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where a sale's margin depends on a supplier invoice that is itself later fully written off as
  uncollectable by the vendor or otherwise voided by the business, the margin reflects that the
  cost was ultimately zero, distinct from a margin where the cost was paid in full.
WHY_IT_MATTERS: >
  Leaving a written-off cost still counted against the margin understates profitability for a cost
  the business never actually bore.
DISCONFIRMING_OBSERVATION: >
  A supplier invoice fully written off or voided by the business still counts as a real cost
  against the originating sale's reported margin.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Write off or void a supplier invoice previously counted as cost for a sale's margin, and inspect
  whether the margin reflects the write-off.
```

## G08-SALE_EXPENSE_MARGIN-Q043

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q043
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A supplier expense recorded in a currency other than the sale's own contributes to that sale's
  margin using the exchange rate in effect when the cost was actually incurred, not whatever rate
  is in effect at the later moment the margin happens to be viewed.
WHY_IT_MATTERS: >
  Using a later exchange rate would make a settled sale's recorded margin drift over time purely
  from currency movement, for a cost that was already fixed and unchanging.
DISCONFIRMING_OBSERVATION: >
  Viewing the same settled sale's margin on two different later dates, with no new cost recorded
  in between, produces two different margin figures attributable only to exchange-rate movement.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a foreign-currency supplier expense against a sale, allow the exchange rate to move, then
  compare the sale's margin figure as computed on two different later dates.
```

## G08-SALE_EXPENSE_MARGIN-Q044

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q044
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Sales sharing a single umbrella customer engagement, where one late supplier invoice covers costs
  for several separate orders under that engagement, have the cost apportioned to each order's own
  margin rather than dumped entirely onto whichever order was open at the time the invoice was
  recorded.
WHY_IT_MATTERS: >
  Dumping a shared cost onto one order overstates that order's cost and understates the others,
  distorting per-order profitability across the same engagement.
DISCONFIRMING_OBSERVATION: >
  A supplier invoice covering costs for several orders under one engagement is applied entirely to
  a single order's margin rather than apportioned across the orders it actually relates to.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record one supplier invoice covering costs for several orders under a shared engagement and
  inspect how it is apportioned across each order's margin.
```

## G08-SALE_EXPENSE_MARGIN-Q045

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q045
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An expense claim rejected outright — not paid to the employee, not billed to the customer — that
  was nonetheless provisionally counted as an estimated cost in an interim margin report is removed
  from that estimate once rejected, not left in as a phantom cost indefinitely.
WHY_IT_MATTERS: >
  A rejected claim's cost that lingers in a margin estimate understates profitability for a cost
  that will now never actually be incurred by either the business or the customer.
DISCONFIRMING_OBSERVATION: >
  Rejecting an expense claim that was already counted as an estimated cost in an interim margin
  leaves that estimate unchanged, still including the rejected amount.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Count an unapproved expense's estimate into an interim margin, then reject that expense outright,
  and inspect whether the interim margin is corrected.
```

## G08-SALE_EXPENSE_MARGIN-Q046

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q046
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  The margin design does not assume that an employee's claimed amount and the supplier's eventual
  invoice will always match — the gap between them is treated as a routine, expected condition to
  reconcile, not an edge case the design can simply ignore.
WHY_IT_MATTERS: >
  A design that treats the claim-invoice gap as rare rather than routine will systematically
  under-invest in the reconciliation mechanics every other question in this bank depends on.
DISCONFIRMING_OBSERVATION: >
  A routine, moderate difference between an employee's claim and the supplier's invoice has no
  defined reconciliation path at all, and only extreme mismatches receive any handling.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Introduce a routine, moderate difference between an employee's claim and the supplier's eventual
  invoice and check whether a defined reconciliation path exists for it.
```

## G08-SALE_EXPENSE_MARGIN-Q047

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q047
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A supplier invoice arriving in a currency different from the one the employee originally claimed
  in has both conversions tracked distinctly, rather than the supplier leg silently inheriting the
  already-used rate from the employee-claim leg.
WHY_IT_MATTERS: >
  Reusing one leg's rate for the other leg produces a cost figure that does not correspond to any
  actual conversion that took place.
DISCONFIRMING_OBSERVATION: >
  A supplier invoice in a currency different from the employee's original claim is converted using
  the rate already recorded for the claim, rather than its own actual conversion rate.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record an employee claim in one currency and a supplier invoice for the same cost in a different
  currency, and inspect which rate is used to convert the supplier leg.
```

## G08-SALE_EXPENSE_MARGIN-Q048

```yaml
QID: G08-SALE_EXPENSE_MARGIN-Q048
MODULE: sale_expense_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where margin visibility is restricted by role, a role with visibility into a customer's overall
  account profitability cannot infer a specific person's pending supplier cost from the margin
  figure alone, when the underlying cost detail itself is a separately restricted permission.
WHY_IT_MATTERS: >
  A margin figure precise enough to reverse-engineer a restricted cost detail defeats the purpose
  of restricting that detail in the first place.
DISCONFIRMING_OBSERVATION: >
  A role with only account-level margin visibility can derive a specific restricted cost amount by
  comparing margin figures across a small enough set of engagements.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a role with only account-level margin visibility, attempt to derive a specific restricted cost
  detail by comparing margin figures across a small, comparable set of engagements.
```

