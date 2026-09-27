# SMEsPlus ENTERPRISE SUITE
## GMVQ — G06 MANUFACTURING / mrp_landed_costs Module Adversarial MVQ Bank

**Document ID:** GMVQ-G06-MRP_LANDED_COSTS-MVQ48-V1.00
**Group:** G06 MANUFACTURING
**Module Metadata:** `mrp_landed_costs`
**Wave:** W2
**Author Cell:** P09 (GMVQ Question Factory — Internal Production Team P09, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This module is the seam through which a cost that arrives later, from outside production, is pushed backward
onto units that production already finished. Under the bridge-module rule, every question in this bank fails
only at that seam: the allocation basis used to spread a later cost across produced units and the residual left
when the split is not even; a cost arriving after some of the output was already sold or already consumed into
a further production order — whether that triggers a restatement or the difference lands elsewhere; a cost
arriving after the accounting period has closed; a cost arriving twice, or an allocation being reversed; a cost
applying to output that has since been scrapped; a cost applying to a lot that was split or merged into another
order's input; an allocation changed after it has already been posted; the interaction between this later cost
and any variance already recognized at production time, and whether the same money is ever counted twice; and
who may apply an allocation, and how a reviewer proves afterward exactly which units absorbed it.

Every question was tested against the bridge-module seam test: if production and a later, externally arriving
cost were used entirely apart from one another, the question would not make sense. Each one turns on the moment
a cost that did not exist when the units were produced is pushed backward onto those units after the fact —
never on how production itself computes its own cost (which belongs to the base manufacturing module, or to the
sibling production-to-ledger seam) and never on a pure external-cost-document invariant with no connection to
production output.

Question text is source-neutral: no vendor or product name, no technical identifier (model, table, field,
method, XML ID, API path), and no reference to how any specific implementation is built. Language is generic
business/behavioural language throughout.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across business
  invariant, exception path, configuration dependency, role/permission, reversal, negative case, cross-module
  dependency, auditability, tenant/company boundary, and runtime/period reachability.
- This module carries one layer (the later-cost-to-produced-unit seam only); the `LAYER` field is omitted
  throughout.
- Checked against the bridge-module rule before authoring: no sibling bank existed on disk for this group at
  authoring time (`G06_MANUFACTURING` had no prior banks). Within this production run, this bank's ground is held
  strictly to a cost that arrives from outside production, after the fact, and must be pushed backward onto
  output already produced — distinct from the sibling `mrp_account` bank's ground, which is the cost production
  itself generates as it runs. The two are held apart by design: this bank never asks how a variance was
  originally recognized at production time, only what happens when a later, independent cost interacts with a
  unit that already carries one.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a Research
  Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G06-MRP_LANDED_COSTS-Q001

```yaml
QID: G06-MRP_LANDED_COSTS-Q001
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A cost that arrives after production, and is meant to be pushed back onto units already produced, is
  distributed across exactly those units using a stated, declared basis, rather than an arbitrary or
  undocumented split.
WHY_IT_MATTERS: >
  An undocumented split cannot be defended, reproduced, or checked, and silently misstates the true landed value
  of the affected units.
DISCONFIRMING_OBSERVATION: >
  A later-arriving cost is applied to a set of produced units, and the resulting per-unit share cannot be
  explained by any declared, retrievable basis.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a later-arriving external cost to a known set of produced units using a specific stated basis, then
  verify the resulting per-unit shares actually match that basis.
```

## G06-MRP_LANDED_COSTS-Q002

```yaml
QID: G06-MRP_LANDED_COSTS-Q002
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The basis actually used for a specific allocation is recorded as part of that allocation's own evidence, rather
  than only existing as an inferred, unrecorded global default.
WHY_IT_MATTERS: >
  If the basis used is not recorded with the allocation itself, a reviewer later has no way to confirm what rule
  was actually applied versus what the current default happens to be.
DISCONFIRMING_OBSERVATION: >
  An already-applied allocation's record shows the resulting values but not which basis produced them, and the
  current default basis has since changed.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Apply an allocation under one basis, later change the system's default basis, then check whether the original
  allocation's record still shows which basis it actually used.
```

## G06-MRP_LANDED_COSTS-Q003

```yaml
QID: G06-MRP_LANDED_COSTS-Q003
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the units originally eligible for an allocation no longer exist in their original form by the time a
  later cost arrives, the allocation still resolves to a defined destination rather than failing with no result.
WHY_IT_MATTERS: >
  A cost that cannot find its destination and is simply dropped is a real cost never reflected anywhere in the
  books.
DISCONFIRMING_OBSERVATION: >
  A later-arriving cost referencing units that have since been transformed or otherwise no longer exist in their
  original form fails to post anywhere, with no destination recorded for it.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Transform or otherwise change the eligible units before applying a later-arriving cost that references them,
  and observe whether the allocation still finds a destination.
```

## G06-MRP_LANDED_COSTS-Q004

```yaml
QID: G06-MRP_LANDED_COSTS-Q004
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the chosen allocation basis does not divide the cost evenly across the eligible units, the resulting
  residual amount lands in a defined place, rather than being dropped or arbitrarily loaded entirely onto one
  unit.
WHY_IT_MATTERS: >
  An arbitrary residual destination would make the affected unit's cost depend on rounding mechanics rather than
  any real economic basis.
DISCONFIRMING_OBSERVATION: >
  An allocation that does not divide evenly leaves an unaccounted residual, or dumps the entire residual on one
  arbitrarily chosen unit with no stated rule for why that unit was chosen.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Allocate a cost amount across a number of units chosen so the division does not come out even, and check where
  the residual amount lands.
```

## G06-MRP_LANDED_COSTS-Q005

```yaml
QID: G06-MRP_LANDED_COSTS-Q005
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Once an allocated later-arriving cost is applied, it changes the affected units' valuation using the same
  ledger dimension that the units' original production cost uses, so the two are comparable rather than sitting
  in incompatible categories.
WHY_IT_MATTERS: >
  If the allocated cost lands in an incompatible category, the unit's total cost can no longer be computed as one
  meaningful figure.
DISCONFIRMING_OBSERVATION: >
  An allocated cost is applied to a unit, but the resulting valuation change is recorded in a category that
  cannot be combined with the unit's original production cost to produce one total figure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a later-arriving cost allocation to a produced unit and check whether the resulting valuation change
  combines with the unit's original cost in the same reportable figure.
```

## G06-MRP_LANDED_COSTS-Q006

```yaml
QID: G06-MRP_LANDED_COSTS-Q006
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cost submitted for allocation against a reference that turns out to have no eligible units at all is flagged
  as a gap requiring attention, rather than being silently discarded or posted with no destination.
WHY_IT_MATTERS: >
  A silently discarded cost with nowhere to land is a real, unrecorded loss that nobody would ever be prompted to
  investigate.
DISCONFIRMING_OBSERVATION: >
  A cost submitted for allocation against a reference with no eligible units produces no flag, warning, or
  exception, and the cost simply does not appear anywhere afterward.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Submit a later-arriving cost referencing a production event whose units no longer have any eligible destination,
  and observe what happens to that cost.
```

## G06-MRP_LANDED_COSTS-Q007

```yaml
QID: G06-MRP_LANDED_COSTS-Q007
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A later-arriving cost for output that has already been sold either restates the cost of goods already
  recognized for that sale, or is redirected to a defined alternate destination — the choice follows one
  deterministic rule, not an ad hoc decision made differently each time.
WHY_IT_MATTERS: >
  An ad hoc choice would make the same kind of event produce different financial outcomes purely by circumstance,
  breaking comparability between periods.
DISCONFIRMING_OBSERVATION: >
  A later-arriving cost referencing already-sold output lands in one destination in one case and a different,
  unexplained destination in an otherwise-identical case.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Sell output, then apply a later-arriving cost referencing it, and repeat with an otherwise-identical scenario,
  comparing where the cost lands both times.
```

## G06-MRP_LANDED_COSTS-Q008

```yaml
QID: G06-MRP_LANDED_COSTS-Q008
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A later-arriving cost for output already consumed as a component in a further production order propagates into
  that further order's own valuation, or is deliberately and visibly not propagated, according to one stated
  rule — it is not simply ignored without a decision either way.
WHY_IT_MATTERS: >
  Silent non-propagation would leave a further order's own valuation understated with no indication that an
  upstream cost affecting it was ever received.
DISCONFIRMING_OBSERVATION: >
  A later-arriving cost referencing output already consumed into a further production order results in no visible
  effect on, or decision recorded about, that further order's own valuation.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Consume produced output into a further production order, then apply a later-arriving cost referencing the
  original output, and check whether the further order's valuation is affected or a decision not to affect it is
  recorded.
```

## G06-MRP_LANDED_COSTS-Q009

```yaml
QID: G06-MRP_LANDED_COSTS-Q009
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether output counts as already sold or already consumed elsewhere for allocation purposes is evaluated at the
  moment the later cost is actually applied, not at the moment the original output was produced, so a unit sold
  in between is correctly classified.
WHY_IT_MATTERS: >
  Evaluating status at the wrong moment would misclassify units that changed status in the interim, sending their
  share of cost to the wrong destination.
DISCONFIRMING_OBSERVATION: >
  A unit sold after production but before a later cost is applied is treated by the allocation as though it were
  still on hand, based on its status at production time rather than at allocation time.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Produce a unit, sell it, then apply a later-arriving cost referencing the original production, and check which
  status the allocation actually used.
```

## G06-MRP_LANDED_COSTS-Q010

```yaml
QID: G06-MRP_LANDED_COSTS-Q010
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a later-arriving cost triggers a downstream restatement, the retained trail links the triggering
  allocation and the resulting downstream posting together.
WHY_IT_MATTERS: >
  Without that link, a reviewer seeing a downstream figure change has no way to determine why it changed or trace
  it back to its cause.
DISCONFIRMING_OBSERVATION: >
  A downstream posting changes as a result of a later-arriving allocation, but the retained trail for that
  downstream posting shows no link back to the allocation that caused it.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Trigger a downstream restatement via a later-arriving allocation and attempt to trace the downstream change
  back to its triggering allocation using only the retained trail.
```

## G06-MRP_LANDED_COSTS-Q011

```yaml
QID: G06-MRP_LANDED_COSTS-Q011
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When part of a batch of output was sold and part remains on hand at the time a later cost arrives, each portion
  is treated according to its own actual status, rather than the whole batch being treated uniformly as if all of
  it were still on hand.
WHY_IT_MATTERS: >
  Uniform treatment of a mixed-status batch would misstate either the sold portion's cost of goods or the
  remaining portion's inventory value.
DISCONFIRMING_OBSERVATION: >
  A later-arriving cost applied to a batch that is partly sold and partly on hand treats the entire batch
  identically, ignoring the split between the two statuses.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Produce a batch, sell part of it, keep the rest on hand, then apply a later-arriving cost referencing the whole
  batch and check whether the two portions are treated differently according to status.
```

## G06-MRP_LANDED_COSTS-Q012

```yaml
QID: G06-MRP_LANDED_COSTS-Q012
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A later-arriving cost applied to output that was sold and then returned by a customer reflects the unit's
  current status at the time of allocation, not its status at some earlier point in its history.
WHY_IT_MATTERS: >
  Using a stale status would send the returned unit's cost share to the wrong destination, such as into cost of
  goods sold for a sale that no longer stands.
DISCONFIRMING_OBSERVATION: >
  A unit that was sold, then returned and restocked, is treated by a later-arriving allocation as still sold,
  rather than reflecting its current, back-in-stock status.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Sell a unit, process its return back into stock, then apply a later-arriving cost referencing the original
  production and check which status the allocation used.
```

## G06-MRP_LANDED_COSTS-Q013

```yaml
QID: G06-MRP_LANDED_COSTS-Q013
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A later-arriving cost whose natural date falls within an accounting period that has since been closed does not
  post into that closed period; it lands in an open period, or is otherwise redirected, according to a defined
  rule.
WHY_IT_MATTERS: >
  A silent posting into a closed period would invalidate figures that have already been reported, reviewed, and
  relied upon by others.
DISCONFIRMING_OBSERVATION: >
  A later-arriving cost with a natural date inside an already-closed period posts directly into that closed
  period with no block or redirection.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Close an accounting period, then apply a later-arriving cost whose natural date falls within that closed
  period, and observe where it actually posts.
```

## G06-MRP_LANDED_COSTS-Q014

```yaml
QID: G06-MRP_LANDED_COSTS-Q014
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a late-arriving cost, when redirected out of a closed period, posts at its own original document date
  or at the date of the open period receiving it follows one stated, consistent rule.
WHY_IT_MATTERS: >
  An inconsistent dating rule would make it impossible to predict, from one late cost to the next, which period
  will actually carry the charge.
DISCONFIRMING_OBSERVATION: >
  Two otherwise-identical late-arriving costs, both redirected out of the same closed period, end up posted under
  two different dating conventions.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Apply two otherwise-identical late-arriving costs referencing a closed period and compare the posting dates
  each one actually receives.
```

## G06-MRP_LANDED_COSTS-Q015

```yaml
QID: G06-MRP_LANDED_COSTS-Q015
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A late-arriving cost's allocation calculation still correctly references the original historical production
  data even though the period that data belongs to has since been locked.
WHY_IT_MATTERS: >
  If locking a period also corrupts or hides the historical data an allocation needs, a late cost referencing
  that period could be misallocated with no way to detect it.
DISCONFIRMING_OBSERVATION: >
  A late-arriving cost's allocation, calculated after the referenced period has been locked, uses incorrect or
  substituted historical data rather than the original production figures.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Lock a period, then apply a late-arriving cost referencing production that occurred in that period, and verify
  the allocation used the correct original historical data.
```

## G06-MRP_LANDED_COSTS-Q016

```yaml
QID: G06-MRP_LANDED_COSTS-Q016
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cost applied after its originating period has closed is distinguishable in the trail from one applied within
  its original period, so a reviewer can tell which reporting period actually carried a given charge.
WHY_IT_MATTERS: >
  Without that distinction, a reviewer cannot tell whether a charge appearing in the current period is a normal
  current-period cost or a correction belonging to an earlier period.
DISCONFIRMING_OBSERVATION: >
  A cost applied after period close is recorded identically, with no distinguishing marker, to a cost that was
  applied within its own original period.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Apply one cost within its own period and another after its period has closed, and compare whether the two are
  distinguishable in the retained trail.
```

## G06-MRP_LANDED_COSTS-Q017

```yaml
QID: G06-MRP_LANDED_COSTS-Q017
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Two separate late-arriving costs for the same original production event, applied in two different subsequent
  periods, are each posted independently without one silently overwriting or replacing the other's posting.
WHY_IT_MATTERS: >
  One late cost overwriting another would silently lose a real, distinct financial event.
DISCONFIRMING_OBSERVATION: >
  Applying a second late-arriving cost referencing the same original production event, in a later period than the
  first, causes the first one's posting to disappear or be replaced.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply two separate late-arriving costs referencing the same original production event in two different
  subsequent periods and check whether both postings persist independently.
```

## G06-MRP_LANDED_COSTS-Q018

```yaml
QID: G06-MRP_LANDED_COSTS-Q018
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Submitting the same external cost document for allocation a second time is detected and prevented from
  doubling the amount charged to the affected units.
WHY_IT_MATTERS: >
  An undetected duplicate submission would silently double a real cost onto units that only actually incurred it
  once.
DISCONFIRMING_OBSERVATION: >
  The same external cost document is submitted for allocation twice, and the affected units end up charged twice
  the correct amount with no duplicate warning raised.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Submit the same external cost document for allocation twice against the same units and observe whether a
  duplicate is detected.
```

## G06-MRP_LANDED_COSTS-Q019

```yaml
QID: G06-MRP_LANDED_COSTS-Q019
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reversing an already-applied allocation restores the affected units' valuation to exactly what it was
  immediately before that allocation was applied, not to a default, zero, or some other unrelated value.
WHY_IT_MATTERS: >
  A reversal that lands on the wrong value would either understate or overstate the unit's valuation relative to
  its true, pre-allocation state.
DISCONFIRMING_OBSERVATION: >
  Reversing an allocation leaves the affected unit's valuation at a value different from what it held immediately
  before the allocation was originally applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a unit's valuation before an allocation, apply the allocation, then reverse it and compare the resulting
  valuation against the original recorded value.
```

## G06-MRP_LANDED_COSTS-Q020

```yaml
QID: G06-MRP_LANDED_COSTS-Q020
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A partial reversal of an allocation leaves the un-reversed remainder correctly and consistently valued,
  reflecting exactly the amount still meant to apply.
WHY_IT_MATTERS: >
  An inconsistent partial reversal would leave the affected unit's valuation reflecting neither the original nor
  the intended corrected amount.
DISCONFIRMING_OBSERVATION: >
  Partially reversing an allocation leaves the affected unit's valuation at an amount that matches neither the
  original allocation nor the original amount minus the reversed portion.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply an allocation, then reverse only part of it, and check whether the remaining valuation matches the
  original amount minus the reversed portion.
```

## G06-MRP_LANDED_COSTS-Q021

```yaml
QID: G06-MRP_LANDED_COSTS-Q021
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Reversing an allocation after the affected output has already moved further downstream either propagates the
  reversal to that downstream position by a defined rule, or explicitly does not — the outcome is a deliberate
  choice, not silence.
WHY_IT_MATTERS: >
  Silent non-propagation would leave a downstream figure permanently overstated by an amount that was, in fact,
  reversed upstream.
DISCONFIRMING_OBSERVATION: >
  Reversing an allocation whose affected output has already moved downstream produces no visible effect on, and
  no recorded decision about, the downstream position.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Apply an allocation, move the affected output downstream, then reverse the allocation and check for an effect
  on, or explicit decision about, the downstream position.
```

## G06-MRP_LANDED_COSTS-Q022

```yaml
QID: G06-MRP_LANDED_COSTS-Q022
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Both an original allocation and any later reversal of it remain visible in the retained trail as linked events,
  rather than the reversal replacing or deleting the original record.
WHY_IT_MATTERS: >
  A reviewer needs both records to understand what was originally charged and what corrected it.
DISCONFIRMING_OBSERVATION: >
  After an allocation is reversed, the original allocation record is no longer retrievable from the trail,
  leaving only the reversal.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Apply and then reverse an allocation, and check whether both the original and the reversal remain independently
  retrievable afterward.
```

## G06-MRP_LANDED_COSTS-Q023

```yaml
QID: G06-MRP_LANDED_COSTS-Q023
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The portion of a later-arriving cost allocated to units that have since been scrapped lands in a defined
  destination, rather than simply being lost with no destination at all.
WHY_IT_MATTERS: >
  A silently lost cost share for scrapped units is a real financial loss that would never appear anywhere in the
  books.
DISCONFIRMING_OBSERVATION: >
  A later-arriving cost allocated in part to scrapped units results in that portion having no destination
  anywhere in the posted records.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Scrap part of a batch of output, then apply a later-arriving cost referencing the whole batch, and check where
  the scrapped portion's share lands.
```

## G06-MRP_LANDED_COSTS-Q024

```yaml
QID: G06-MRP_LANDED_COSTS-Q024
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A unit scrapped before a later cost arrives, and a unit scrapped only after a cost has already been allocated to
  it, are each treated according to distinguishable, defined rules — not identically purely by coincidence of
  implementation.
WHY_IT_MATTERS: >
  Treating both cases identically without a deliberate rule risks either double-counting a loss or failing to
  reverse a cost that no longer has anywhere valid to sit.
DISCONFIRMING_OBSERVATION: >
  A unit scrapped before allocation and a unit scrapped after allocation end up with identical treatment despite
  the underlying timing being materially different, with no rule found to explain why that identical treatment is
  correct.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Scrap one unit before applying a later-arriving allocation and scrap an otherwise-identical unit only after the
  allocation has already been applied to it, then compare the resulting treatment of each.
```

## G06-MRP_LANDED_COSTS-Q025

```yaml
QID: G06-MRP_LANDED_COSTS-Q025
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The portion of a later-arriving cost that lands on scrapped output is identifiable in the trail as distinct
  from the portion landing on saleable output.
WHY_IT_MATTERS: >
  Without that distinction, a reviewer cannot separate genuine landed cost on sellable inventory from loss
  already absorbed by scrap.
DISCONFIRMING_OBSERVATION: >
  A later-arriving cost split between scrapped and saleable output posts as a single undifferentiated figure,
  with no way to tell how much landed on each.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Apply a later-arriving cost to a set of units that includes both scrapped and saleable output, and check
  whether the two portions are separately identifiable afterward.
```

## G06-MRP_LANDED_COSTS-Q026

```yaml
QID: G06-MRP_LANDED_COSTS-Q026
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The destination used for the scrapped portion of a later-arriving cost is the same destination used for scrap
  value recognized during production itself, or a documented reason exists for treating the two differently.
WHY_IT_MATTERS: >
  Two different, undocumented destinations for what is economically the same kind of loss would fragment the true
  total scrap loss across two places nobody would think to add back together.
DISCONFIRMING_OBSERVATION: >
  The scrapped portion of a later-arriving cost posts to a destination different from the one used for scrap
  recognized during production, with no documented reason for the difference.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Compare the posting destination used for scrap recognized during production against the destination used for
  the scrapped portion of a later-arriving allocation.
```

## G06-MRP_LANDED_COSTS-Q027

```yaml
QID: G06-MRP_LANDED_COSTS-Q027
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When every unit originally eligible for an allocation has been scrapped by the time the cost arrives, the
  entire cost still resolves to a defined destination, rather than being posted nowhere because no saleable unit
  remains.
WHY_IT_MATTERS: >
  A cost that cannot post because its intended destination is entirely gone is a real financial event dropped for
  want of a place to record it.
DISCONFIRMING_OBSERVATION: >
  A later-arriving cost referencing a batch that has been entirely scrapped by the time it arrives fails to post
  anywhere.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Scrap an entire batch of output, then apply a later-arriving cost referencing that batch, and observe whether
  the cost still resolves to a defined destination.
```

## G06-MRP_LANDED_COSTS-Q028

```yaml
QID: G06-MRP_LANDED_COSTS-Q028
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A later-arriving cost originally tied to a batch of output that was subsequently split into smaller lots
  remains traceable to, and allocable across, those resulting smaller lots individually.
WHY_IT_MATTERS: >
  If the traceability link is lost at the split, a cost arriving afterward has no correct destination and either
  misallocates or fails outright.
DISCONFIRMING_OBSERVATION: >
  A batch is split into smaller lots, and a later-arriving cost referencing the original batch cannot be
  allocated across the resulting lots at all, or is allocated to only one of them.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split a produced batch into smaller lots, then apply a later-arriving cost referencing the original batch, and
  check whether it correctly allocates across the resulting lots.
```

## G06-MRP_LANDED_COSTS-Q029

```yaml
QID: G06-MRP_LANDED_COSTS-Q029
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A later-arriving cost tied to output that was merged with other output is allocated according to a defined
  rule that accounts for the merge, rather than being lost at the point of merge.
WHY_IT_MATTERS: >
  A cost lost at a merge point is a real charge that never reaches any valuation, understating whatever absorbed
  the merged material.
DISCONFIRMING_OBSERVATION: >
  Output that was merged with other output before a later-arriving cost arrives results in that cost failing to
  allocate to the merged result at all.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Merge produced output with other output, then apply a later-arriving cost referencing the original output, and
  check whether it allocates to the merged result.
```

## G06-MRP_LANDED_COSTS-Q030

```yaml
QID: G06-MRP_LANDED_COSTS-Q030
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The traceability link from an originally produced batch to its split or merged descendants survives long enough
  that a cost arriving well after the split or merge event can still find its correct destination.
WHY_IT_MATTERS: >
  A traceability link that degrades or is dropped over time would make correct allocation dependent on how
  quickly the external cost happens to arrive, for no principled reason.
DISCONFIRMING_OBSERVATION: >
  A later-arriving cost applied a significant time after a split or merge event fails to correctly reach the
  resulting descendants, whereas the same cost applied immediately after the split or merge would have succeeded.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Split or merge a batch, wait a significant interval, then apply a later-arriving cost referencing the original
  batch, and check whether it still correctly reaches the resulting descendants.
```

## G06-MRP_LANDED_COSTS-Q031

```yaml
QID: G06-MRP_LANDED_COSTS-Q031
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When part of a split lot has itself already been consumed into a different production order before a later cost
  arrives, the allocation correctly follows that portion into its new context, rather than treating the original
  lot as though it were still whole and unconsumed.
WHY_IT_MATTERS: >
  Treating an already-consumed portion as still available would misallocate a real cost share to inventory that
  no longer exists in that form.
DISCONFIRMING_OBSERVATION: >
  A later-arriving cost applied after part of a split lot has already been consumed into a different order
  allocates as though the entire original lot were still intact and available.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split a lot, consume part of the split portion into a different production order, then apply a later-arriving
  cost referencing the original lot, and check whether the allocation correctly reflects the already-consumed
  portion.
```

## G06-MRP_LANDED_COSTS-Q032

```yaml
QID: G06-MRP_LANDED_COSTS-Q032
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  After a split or merge, a reviewer can reconstruct from retained evidence which resulting units carry which
  share of an originally-allocated later-arriving cost.
WHY_IT_MATTERS: >
  Without that reconstructability, a reviewer cannot verify that a cost applied before a split or merge actually
  followed the material correctly afterward.
DISCONFIRMING_OBSERVATION: >
  After a split or merge involving a unit that already carries an allocated later-arriving cost, no retained
  evidence shows how that cost's share was distributed among the resulting units.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Apply a later-arriving cost to a unit, then split or merge that unit, and attempt to reconstruct the resulting
  distribution of the cost from retained evidence alone.
```

## G06-MRP_LANDED_COSTS-Q033

```yaml
QID: G06-MRP_LANDED_COSTS-Q033
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing the basis or amount of an already-posted allocation produces an explicit, separate adjusting entry,
  rather than silently rewriting the originally posted values.
WHY_IT_MATTERS: >
  Silently rewriting a posted value destroys the record of what was actually reported for a period that may
  already have been closed and relied upon.
DISCONFIRMING_OBSERVATION: >
  Changing an already-posted allocation's basis or amount alters the original posted values in place, with no
  separate adjusting entry created.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post an allocation, then change its basis or amount, and check whether the original posted values remain intact
  alongside a new adjusting entry.
```

## G06-MRP_LANDED_COSTS-Q034

```yaml
QID: G06-MRP_LANDED_COSTS-Q034
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Both an original allocation and any subsequent change made to it remain visible and linked in the retained
  trail.
WHY_IT_MATTERS: >
  A reviewer needs to see the original figure and the change together to understand what was corrected and why.
DISCONFIRMING_OBSERVATION: >
  After an allocation is changed, the trail shows only the new figures, with no retrievable record of the
  original allocation it replaced.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Post an allocation, change it, and check whether both the original and the change remain independently
  retrievable afterward.
```

## G06-MRP_LANDED_COSTS-Q035

```yaml
QID: G06-MRP_LANDED_COSTS-Q035
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A change made to an allocation after the affected units have already moved downstream is handled according to a
  defined rule stating whether and how the downstream position is touched, rather than being left undefined.
WHY_IT_MATTERS: >
  An undefined outcome here means the same kind of correction could behave completely differently between two
  occurrences with no way to predict which.
DISCONFIRMING_OBSERVATION: >
  Changing an allocation whose affected units have already moved downstream produces no defined, observable
  effect on, or decision recorded about, the downstream position.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Apply an allocation, move the affected units downstream, then change the allocation and check for a defined
  effect on, or decision about, the downstream position.
```

## G06-MRP_LANDED_COSTS-Q036

```yaml
QID: G06-MRP_LANDED_COSTS-Q036
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change that reduces an allocated amount below what has already been reflected in downstream valuation does
  not produce a nonsensical negative remaining value without a defined resolution for that situation.
WHY_IT_MATTERS: >
  An unresolved negative value propagating through valuation figures would be visibly wrong and could corrupt any
  calculation that assumes valuations are non-negative.
DISCONFIRMING_OBSERVATION: >
  Reducing an allocation below the amount already reflected downstream produces a negative remaining valuation
  figure with no defined resolution or flag for that state.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply an allocation, let its effect propagate downstream, then reduce the allocation below the amount already
  propagated and observe the resulting figures.
```

## G06-MRP_LANDED_COSTS-Q037

```yaml
QID: G06-MRP_LANDED_COSTS-Q037
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing an already-posted allocation is restricted to a distinct level of authorization, separate from the
  authorization needed to create a fresh allocation.
WHY_IT_MATTERS: >
  If ordinary allocation-creation access is enough to alter an already-posted one, the additional control
  intended for changing posted figures does not actually exist.
DISCONFIRMING_OBSERVATION: >
  A user holding only ordinary allocation-creation access is able to change an already-posted allocation.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to change an already-posted allocation using an account that holds only ordinary allocation-creation
  access.
```

## G06-MRP_LANDED_COSTS-Q038

```yaml
QID: G06-MRP_LANDED_COSTS-Q038
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A later-arriving external cost allocated to output is treated as an addition on top of any production-time
  variance already recognized for that same output, rather than the two being layered in a way that counts the
  same underlying money twice.
WHY_IT_MATTERS: >
  Double counting the same real cost through two different mechanisms would overstate the unit's true cost
  without any single figure looking obviously wrong on its own.
DISCONFIRMING_OBSERVATION: >
  A unit's total recognized cost, after both a production-time variance and a later external allocation are
  applied, is higher than the sum of the two amounts would independently justify, or shows the same underlying
  difference counted through both.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Produce a unit with a recognized production-time variance, then apply a later-arriving external allocation to
  the same unit, and check whether the two combine correctly without double counting.
```

## G06-MRP_LANDED_COSTS-Q039

```yaml
QID: G06-MRP_LANDED_COSTS-Q039
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When both a production-time variance and a later external allocation touch the same unit's valuation, the two
  amounts remain individually identifiable in the trail, rather than merging into one indistinguishable figure.
WHY_IT_MATTERS: >
  An indistinguishable merged figure makes it impossible to audit which part of a unit's cost came from
  production itself and which came from a later external event.
DISCONFIRMING_OBSERVATION: >
  A unit that carries both a production-time variance and a later external allocation shows only a single
  combined valuation figure, with no way to separate the two contributing amounts.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Apply both a production-time variance and a later external allocation to the same unit, and check whether the
  two amounts remain separately identifiable.
```

## G06-MRP_LANDED_COSTS-Q040

```yaml
QID: G06-MRP_LANDED_COSTS-Q040
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A later-arriving cost that is, in substance, a correction to a value already captured by a production-time
  variance does not require an undocumented manual step to avoid being booked twice; if such a step is in fact
  required, that limitation is at least surfaced rather than hidden.
WHY_IT_MATTERS: >
  A hidden reliance on a manual step that nobody is told about is a control gap that will eventually be missed,
  producing an undetected double booking.
DISCONFIRMING_OBSERVATION: >
  A later cost that duplicates a production-time variance's underlying correction is booked in full alongside the
  existing variance, with no automatic reconciliation and no documented manual step calling attention to the
  overlap.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Construct a later-arriving cost that corrects the same underlying rate a production-time variance already
  captured, apply it, and check whether the overlap is reconciled or at least flagged.
```

## G06-MRP_LANDED_COSTS-Q041

```yaml
QID: G06-MRP_LANDED_COSTS-Q041
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A report of total realized cost for a given output unit over a given period includes both its production-time
  variance and any later external allocation applied to it, rather than reflecting only one of the two.
WHY_IT_MATTERS: >
  A report missing one of the two components would understate the unit's true total cost, misleading whoever
  relies on that report for margin or pricing decisions.
DISCONFIRMING_OBSERVATION: >
  A total-cost report for a unit that has both a production-time variance and a later external allocation
  reflects only one of the two amounts.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply both a production-time variance and a later external allocation to a unit, generate a total-cost report
  for it, and check whether both amounts are reflected.
```

## G06-MRP_LANDED_COSTS-Q042

```yaml
QID: G06-MRP_LANDED_COSTS-Q042
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The order in which a production-time variance and a later external allocation are posted for the same unit does
  not change the final total valuation reached for that unit.
WHY_IT_MATTERS: >
  A result that depends on posting order would make the same real sequence of events produce different final
  figures depending purely on timing coincidence.
DISCONFIRMING_OBSERVATION: >
  Posting a production-time variance before a later external allocation produces a different final valuation for
  the unit than posting the same two events in the reverse order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a production-time variance and a later external allocation to two otherwise-identical units in opposite
  orders, and compare the final valuations.
```

## G06-MRP_LANDED_COSTS-Q043

```yaml
QID: G06-MRP_LANDED_COSTS-Q043
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A reviewer examining a unit's final valuation can decompose it into three distinguishable components: its
  original production cost, its production-time variance, and any later external allocation.
WHY_IT_MATTERS: >
  Without that decomposition, a reviewer cannot verify any single component is correct, only the opaque total.
DISCONFIRMING_OBSERVATION: >
  A unit's final valuation, once all three components have been applied, cannot be broken back down into the
  three original component amounts from the retained records.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Apply a production-time variance and a later external allocation to a unit's original production cost, then
  attempt to decompose the final valuation back into the three components using retained records alone.
```

## G06-MRP_LANDED_COSTS-Q044

```yaml
QID: G06-MRP_LANDED_COSTS-Q044
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Applying a later-arriving external cost allocation is restricted to a defined level of authorization, distinct
  from the authorization needed for ordinary production recording.
WHY_IT_MATTERS: >
  If ordinary production access is sufficient to apply an allocation affecting valuation and margin, the intended
  control over who may do so does not actually exist.
DISCONFIRMING_OBSERVATION: >
  A user holding only ordinary production-recording access is able to apply a later-arriving external cost
  allocation.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to apply a later-arriving allocation using an account that holds only ordinary production-recording
  access.
```

## G06-MRP_LANDED_COSTS-Q045

```yaml
QID: G06-MRP_LANDED_COSTS-Q045
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  After an allocation is applied, a reviewer can identify, without ambiguity, exactly which units absorbed which
  share of the cost.
WHY_IT_MATTERS: >
  Without that traceability, nobody can later verify or challenge which units actually ended up carrying a given
  external cost.
DISCONFIRMING_OBSERVATION: >
  After an allocation is applied across several units, the retained evidence does not allow a reviewer to
  determine, unit by unit, what share each one absorbed.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Apply an allocation across several units and attempt to determine, from retained evidence alone, each unit's
  absorbed share.
```

## G06-MRP_LANDED_COSTS-Q046

```yaml
QID: G06-MRP_LANDED_COSTS-Q046
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The identity of the person or role that applied a given allocation is retained alongside the allocation record
  itself, not only alongside the originating external cost document.
WHY_IT_MATTERS: >
  If accountability is only attached to the originating document, a reviewer examining the allocation itself has
  no way to know who was responsible for how it was applied.
DISCONFIRMING_OBSERVATION: >
  An allocation record shows what was applied and to which units, but does not itself retain who applied it, even
  though the originating document does.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Apply an allocation and check whether the identity of the person who applied it is retained on the allocation
  record itself.
```

## G06-MRP_LANDED_COSTS-Q047

```yaml
QID: G06-MRP_LANDED_COSTS-Q047
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An allocation applied by an actor who does not hold the required authorization, through some alternate entry
  path that bypasses the normal check, is either prevented outright or is independently detectable after the
  fact.
WHY_IT_MATTERS: >
  An undetectable bypass of the authorization control makes the control meaningless in practice, regardless of
  how it is documented.
DISCONFIRMING_OBSERVATION: >
  An allocation applied through an alternate entry path by an actor lacking the required authorization succeeds,
  and no independent record afterward distinguishes it from a properly authorized allocation.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Attempt to apply an allocation through an alternate entry path using an account lacking the required
  authorization, and check both whether it succeeds and whether it is later detectable as improperly authorized.
```

## G06-MRP_LANDED_COSTS-Q048

```yaml
QID: G06-MRP_LANDED_COSTS-Q048
MODULE: mrp_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the produced units eligible for an allocation belong to more than one company or legal entity, an
  allocation spanning them is either prevented outright, or is split per entity in a way that keeps each entity's
  absorbed share separately provable.
WHY_IT_MATTERS: >
  An allocation that crosses entity boundaries without a separately provable per-entity share would make it
  impossible to demonstrate that each entity's own books reflect only its own share of a shared external cost.
DISCONFIRMING_OBSERVATION: >
  An allocation applied across units belonging to more than one company results in a combined figure with no way
  to determine how much each individual entity's own books actually absorbed.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Apply a later-arriving cost allocation across a set of units spanning more than one company, and check whether
  each entity's absorbed share is separately provable afterward.
```

---
## GMVQ Internal QA Checklist

- [x] 48 distinct MVQ records; no padding — every record targets a distinct hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`.
- [x] Questions are behavioral and source-neutral; no vendor/product name, technical identifier, or module name
      appears in question text.
- [x] Bridge-module seam test applied to every question: each fails only where a cost arriving from outside
      production, after the fact, is pushed backward onto units already produced; none would still make sense
      with production and a later external cost used entirely apart.
- [x] Allocation basis across produced units and the residual represented (Q001-Q006).
- [x] Cost arriving after output already sold or consumed into a further order represented (Q007-Q012).
- [x] Cost arriving after the accounting period closed represented (Q013-Q017).
- [x] Cost arriving twice, or an allocation being reversed, represented (Q018-Q022).
- [x] Cost applying to output that was scrapped represented (Q023-Q027).
- [x] Cost applying to a lot split or merged into another order's input represented (Q028-Q032).
- [x] Allocation changed after posting represented (Q033-Q037).
- [x] Interaction with variance already recognized at production time — double counting — represented
      (Q038-Q043).
- [x] Who may apply an allocation, and traceability of which units absorbed it, represented (Q044-Q048).
- [x] Role/permission boundary represented (Q037, Q044, Q047).
- [x] Tenant/company boundary represented (Q048).
- [x] Reversal represented (Q019-Q022).
- [x] Cross-module dependency represented (Q005, Q010, Q039, Q043).
- [x] Runtime/period reachability represented (Q013-Q017).
- [x] No specific Thai legal or tax requirement asserted anywhere in this bank.
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
