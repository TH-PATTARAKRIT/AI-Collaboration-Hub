# SMEsPlus ENTERPRISE SUITE
## GMVQ — G06 MANUFACTURING / mrp_subcontracting_account Module MVQ Bank

**Document ID:** GMVQ-G06-MRP_SUBCONTRACTING_ACCOUNT-MVQ48-V1.00
**Group:** G06 MANUFACTURING
**Module Metadata:** `mrp_subcontracting_account`
**Wave:** W2
**Author Cell:** P12
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose
This bank supplies the module-specific research questions for `mrp_subcontracting_account` —
the seam between production performed by an outside party and the owning company's own
ledger: where value sits while components are away, how the outside party's service cost
enters the produced item's valuation, and what happens at loss, reversal, revaluation and
period close for stock the company owns but does not physically hold. It is written for a
blind two-lane study: Lane A reads reference source, Lane B observes a running system, and
neither sees the other's answers. Question text is source-neutral throughout and contains no
model, field, or module identifier.

## Control
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- Bridge-module rule applied: every question below fails the "remove the second capability"
  test — none would still make sense if either the outside-party production capability or
  the ledger/valuation capability were removed and the other used alone. Base subcontracting
  invariants (ownership at the external party, unreturned components, traceability across an
  unobserved boundary) belong to `mrp_subcontracting` and are deliberately not repeated here.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread
  across location-of-value tracking, service-cost capitalization timing, consumption-variance
  classification, loss and write-off, period close, related-party treatment, revaluation
  propagation, reversal integrity, multi-hop subcontracting, and account-configuration reach.
- This bank is DRAFT authoring output only. Not approved, not frozen, not verified.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived here.

---

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q001

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q001
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  While components are physically located at an outside party performing work on them, their
  value remains recognized as the owning company's asset in a distinct location-of-value
  state, not removed from the balance sheet and not merged into a generic on-hand valuation.
WHY_IT_MATTERS: >
  If ownership value silently disappears from the books while goods are away, both the
  balance sheet and any reconciliation against a physical count at the external site become
  wrong in ways nobody is positioned to catch.
DISCONFIRMING_OBSERVATION: >
  Components sent to an outside party for work are removed from the owning company's valued
  inventory with no distinguishable location-of-value record showing they are still owned and
  merely relocated.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Send components to an outside party for a production step and inspect the valuation ledger
  and location records before any output is received back.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q002

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q002
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Value held at an outside party is tracked as its own distinguishable position, separate from
  ordinary on-hand stock and separate from goods simply in transit between two of the owning
  company's own locations.
WHY_IT_MATTERS: >
  Collapsing an externally-held position into ordinary transit or on-hand value hides a
  materially different risk profile — a third party's custody — from anyone reading the
  valuation by position.
DISCONFIRMING_OBSERVATION: >
  A valuation report grouped by position shows externally-held component value merged
  indistinguishably into either ordinary on-hand stock or ordinary in-transit stock.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Compare a valuation-by-position report for components at an outside party against the same
  report for components in ordinary transit and ordinary on-hand stock.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q003

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q003
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A subcontracted production order that never reaches completion still leaves the value of the
  components sent visible on the owning company's own financial statements indefinitely,
  rather than the value quietly dropping out of reported figures.
WHY_IT_MATTERS: >
  An order that stalls forever without a completion event must not become a way to make owned
  value invisible to whoever reads the statements.
DISCONFIRMING_OBSERVATION: >
  An indefinitely open subcontracted order shows the sent components' value neither on the
  statements as owned stock nor as any other traceable balance, effectively vanishing from
  reported figures.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Send components to an outside party under an order deliberately left open with no output
  ever received, then inspect financial statements produced well after the normal cycle time.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q004

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q004
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The cost billed for the outside party's work is added into the valuation of the item
  produced, rather than being expensed separately with no link to the item it produced.
WHY_IT_MATTERS: >
  If the service cost never reaches the produced item's value, the item's cost is understated
  and margin on anything made that way is systematically overstated.
DISCONFIRMING_OBSERVATION: >
  An item produced through outside work is valued using only its components' cost, with the
  billed service cost posted somewhere that has no traceable link to that item's valuation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a subcontracted order with a billed service amount and inspect the resulting
  valuation of the produced item for a component attributable to that service.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q005

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q005
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the produced output is received before the outside party's service is billed, the
  item's initial valuation uses a determinable estimate of the service cost rather than
  treating the service as free of cost until a bill eventually arrives.
WHY_IT_MATTERS: >
  Valuing subcontracted output as if the outside labor cost nothing, for however long billing
  is delayed, misstates margin and stock value for that whole window.
DISCONFIRMING_OBSERVATION: >
  Output received before the service is billed carries a valuation with no cost component for
  the outside work at all, for an extended period with no estimate or accrual in place.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Receive subcontracted output before the service invoice arrives, then inspect the item's
  valuation immediately after receipt and again once the invoice is later recorded.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q006

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q006
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the outside party's service is billed before the produced output is received, the
  billed cost is held in a position awaiting the output rather than expensed immediately with
  no future link to the item it will value.
WHY_IT_MATTERS: >
  A service cost expensed on arrival with no forward link either duplicates cost once output
  lands or permanently under-costs the item, and nobody reviewing the item's valuation can
  tell which happened.
DISCONFIRMING_OBSERVATION: >
  A service billed ahead of the matching output is expensed at once, and when the output later
  arrives, its valuation shows no reduction of that already-expensed amount and no reference
  back to it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record the outside party's service bill before the corresponding output is received, then
  receive the output and inspect whether the two are reconciled.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q007

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q007
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A discrepancy between the quantity of components the outside party's documentation implies
  were consumed and the quantity the owning company's own records show as sent is surfaced as
  a distinguishable fact, not silently absorbed into whichever number was recorded last.
WHY_IT_MATTERS: >
  An unsurfaced discrepancy between two competing consumption stories means nobody can tell
  whether stock was lost, over-reported, or double-counted.
DISCONFIRMING_OBSERVATION: >
  The two consumption figures disagree for a given order and no report, flag, or record makes
  that disagreement visible; the system simply reflects one of the two numbers as if there
  were no other.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Engineer a case where the quantity implied by the outside party's own documentation differs
  from the quantity the owning company's records show as sent, then look for any surfaced
  comparison.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q008

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q008
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a consumption discrepancy is surfaced, it is classified into a distinct category (for
  example a costed variance versus a loss to be written off) rather than left as an
  unclassified number a user must interpret unaided.
WHY_IT_MATTERS: >
  An unclassified discrepancy forces every reviewer to independently decide what kind of
  problem it is, which produces inconsistent accounting treatment for the same underlying
  event.
DISCONFIRMING_OBSERVATION: >
  A surfaced consumption discrepancy carries no classification distinguishing an expected
  costing variance from an unexplained loss; both look identical in the record.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Produce two discrepancy cases with different underlying causes and compare how each is
  categorized in the resulting record.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q009

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q009
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Components confirmed lost while at the outside party can be moved out of the owning
  company's valued stock through an explicit write-off action that leaves a record of the
  loss, rather than only being removable by quietly editing the on-hand quantity.
WHY_IT_MATTERS: >
  A loss that can only be cleared by silently editing quantity leaves no evidence of what
  happened, which defeats any later audit of what the company actually still owns.
DISCONFIRMING_OBSERVATION: >
  The only way to remove confirmed-lost externally-held components from valued stock is a
  direct quantity correction with no accompanying loss record or reason captured.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Confirm a loss of components at the outside party and attempt to clear them from stock
  through whatever mechanism is available, then inspect what trace that action leaves.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q010

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q010
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A write-off of components lost at the outside party removes value at the same cost basis
  those components carried while held there, not a default or zero value unrelated to their
  recorded worth.
WHY_IT_MATTERS: >
  Writing off a loss at the wrong value either overstates or understates the financial impact
  of an event that already represents money the company will not recover.
DISCONFIRMING_OBSERVATION: >
  A write-off of externally-held components posts an amount that does not match the cost basis
  recorded for those components immediately before the loss.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Write off components confirmed lost at an outside party and compare the posted amount to
  their last recorded cost basis at that location.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q011

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q011
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A period-end valuation run includes the value of components currently held at an outside
  party in the total it reports, rather than only counting value physically inside the owning
  company's own locations.
WHY_IT_MATTERS: >
  Excluding externally-held value from a period-end total understates assets for every period
  in which any subcontracted order is open, silently, every single close.
DISCONFIRMING_OBSERVATION: >
  A period-end valuation total omits the value of components held at an outside party at the
  close date, with no line item accounting for it anywhere in the close output.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Hold components at an outside party across a period boundary and run the standard
  period-end valuation, then check whether the externally-held value appears in the total.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q012

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q012
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the outside party performing the work belongs to the same corporate group as the owning
  company, the value and cost flows are still recorded on each company's own books
  separately, rather than netted or skipped because the two sides are related.
WHY_IT_MATTERS: >
  Silently netting a related-party flow instead of recording it on each entity's own books
  breaks each entity's individual financial statements and any intercompany reconciliation.
DISCONFIRMING_OBSERVATION: >
  A subcontracted order performed by a related-party outside entity produces no separate
  recorded flow on that entity's own books, or the flow is netted away before either company's
  statements are produced.
EXPECTED_SURFACE: S1,S2,S4,S7
PRECONDITIONS: >
  Configure the outside party as a related entity within the same corporate group, run a
  subcontracted order, and inspect each company's own books independently.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q013

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q013
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a service performed by a related-party outside entity is billed at the same terms as
  an unrelated party, or at a distinct configured basis, is an explicit, inspectable setting
  rather than an undocumented side effect of how the two companies happen to be linked.
WHY_IT_MATTERS: >
  An undocumented difference in related-party pricing behavior is exactly the kind of thing a
  tax or audit review needs to find, and cannot find if it isn't configured explicitly.
DISCONFIRMING_OBSERVATION: >
  A related-party outside service is priced differently from an equivalent unrelated-party
  service, and no setting anywhere identifies that a different basis is being applied.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Run equivalent subcontracted orders with a related-party outside entity and with an
  unrelated one, and compare the pricing basis applied to each against any documented
  configuration.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q014

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q014
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the owning company revalues a component's cost while units of it are currently held at an
  outside party, the externally-held units' value is updated by that revaluation on the same
  basis as units still on the owning company's own premises.
WHY_IT_MATTERS: >
  A component that gets left at its old cost merely because it happens to be away at the
  moment of revaluation produces an inconsistent stock value that depends on physical location
  rather than accounting policy.
DISCONFIRMING_OBSERVATION: >
  A revaluation applied to a component updates the value of units on the owning company's own
  premises but leaves units of the same component held at an outside party at their prior
  cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Hold some units of a component at an outside party and some on-site, trigger a revaluation
  of that component, and compare the resulting value of both populations.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q015

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q015
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A revaluation that occurs while a subcontracted order is in progress is reflected in the
  eventual output's valuation using the component cost as of consumption, not the cost as of
  the moment the order was originally started.
WHY_IT_MATTERS: >
  Locking in a stale pre-revaluation cost for output that is actually consumed after the
  revaluation misstates the produced item's cost relative to current component value.
DISCONFIRMING_OBSERVATION: >
  Output consumed after a mid-order revaluation is valued using the component's
  pre-revaluation cost, with no update to reflect the cost as of actual consumption.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Start a subcontracted order, revalue a component it consumes while the order is still open,
  complete the order, and inspect which cost basis the output valuation used.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q016

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q016
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reversing a receipt of subcontracted output after its value has already posted to the ledger
  produces an offsetting entry that unwinds exactly the amount originally posted, rather than
  leaving the original posting standing alongside an unrelated correction.
WHY_IT_MATTERS: >
  A reversal that doesn't exactly offset the original posting leaves a residual misstatement
  that nobody has a reason to go looking for.
DISCONFIRMING_OBSERVATION: >
  Reversing an already-posted receipt leaves the ledger with a net value different from zero
  for that transaction, or leaves the original entry unreferenced by whatever correction was
  made.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a subcontracted receipt's value, then reverse the receipt, and compare the net ledger
  effect of the original posting and its reversal.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q017

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q017
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a receipt is reversed after the produced item it valued has already been consumed or
  sold onward, the system distinguishes that case from a clean reversal and surfaces it rather
  than silently applying the same unwind as if nothing downstream had happened.
WHY_IT_MATTERS: >
  Silently unwinding a valuation whose value has already flowed into a sale or further
  production leaves a downstream cost figure resting on value that officially no longer
  exists.
DISCONFIRMING_OBSERVATION: >
  A receipt reversal proceeds identically whether or not the item it valued has already moved
  downstream, with no distinct handling or flag for the case where downstream consumption has
  already occurred.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Receive and value subcontracted output, consume or sell it onward, then attempt to reverse
  the original receipt and observe what happens to the downstream cost.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q018

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q018
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The ledger treatment for externally-held stock only activates for orders actually routed
  through the outside-party production capability, and has no effect on production orders
  that do not send anything outside.
WHY_IT_MATTERS: >
  A ledger behavior that leaks into ordinary in-house production would apply an
  externally-held cost treatment to stock that never left the building.
DISCONFIRMING_OBSERVATION: >
  An ordinary in-house production order, with no outside party involved at all, shows the same
  externally-held valuation treatment or location-of-value state as a genuinely subcontracted
  one.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Run one ordinary in-house production order and one genuinely subcontracted order side by
  side and compare which valuation treatment each receives.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q019

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q019
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a partial receipt of output and the outside party's service bill for that same order
  are recorded at effectively the same time, the resulting valuation reflects both events
  exactly once each, without either being silently dropped or doubled.
WHY_IT_MATTERS: >
  A race between two nearly simultaneous postings that both touch the same order's valuation
  can silently duplicate or drop cost if the two aren't sequenced deterministically.
DISCONFIRMING_OBSERVATION: >
  Recording a partial receipt and its matching service bill at nearly the same time results in
  a valuation that reflects one of the two events twice, or drops one of them entirely.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Arrange for a partial receipt and its corresponding service bill to be recorded in immediate
  succession and inspect the resulting valuation for double-counting or omission.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q020

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q020
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When output is received in multiple partial deliveries against one subcontracted order, each
  partial delivery's valuation carries its proportionate share of the order's total service
  cost, rather than the entire service cost landing on only one of the partials.
WHY_IT_MATTERS: >
  Dumping the whole service cost onto a single partial delivery misstates the cost of every
  unit in that batch and understates every other batch from the same order.
DISCONFIRMING_OBSERVATION: >
  Two partial deliveries of equal quantity from the same subcontracted order carry materially
  different per-unit service cost with no business reason for the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive a subcontracted order in at least two partial deliveries and compare the per-unit
  service cost recorded on each.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q021

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q021
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An outside-party arrangement billed at zero cost for the service still tracks the
  location-of-value state for the components sent, rather than the absence of a billed amount
  causing the externally-held tracking itself to be skipped.
WHY_IT_MATTERS: >
  If a zero-cost arrangement quietly disables the ownership tracking, any genuinely free or
  intercompany-absorbed service arrangement becomes a blind spot for stock at a third party.
DISCONFIRMING_OBSERVATION: >
  An order with a billed service amount of zero shows no location-of-value tracking for the
  components sent, unlike an otherwise identical order with a nonzero service amount.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a subcontracted order with a service cost of zero and compare its
  location-of-value tracking to an otherwise identical order with a nonzero cost.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q022

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q022
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Months after a subcontracted order completes, the specific service bill that contributed to
  a given produced item's valuation can still be identified by an explicit reference, not only
  by searching for bills near the same date.
WHY_IT_MATTERS: >
  A cost basis that can only be justified by "it was probably this bill, the dates are close"
  does not survive a real audit challenge.
DISCONFIRMING_OBSERVATION: >
  After enough time has passed that the surrounding activity is no longer memorable, the only
  way to identify which service bill contributed to an item's valuation is by comparing dates,
  with no explicit stored reference.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a subcontracted order, wait past the point where the sequence would only be
  recalled from records rather than memory, and attempt to trace the produced item's valuation
  back to its contributing service bill using only stored references.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q023

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q023
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Access to change how externally-held value or service cost gets posted is restricted to
  roles with a financial configuration permission, distinct from the operational permission
  needed merely to record that output was received.
WHY_IT_MATTERS: >
  If receiving a shipment on the warehouse floor also grants the ability to change how that
  receipt values the ledger, accounting control is effectively bypassed by a purely
  operational action.
DISCONFIRMING_OBSERVATION: >
  A user holding only the operational permission to record receipts is also able to alter the
  valuation or posting treatment applied to a subcontracted receipt.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Assign a user only the operational receiving permission, with no financial configuration
  permission, and attempt to alter the valuation treatment of a subcontracted receipt.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q024

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q024
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The accounting treatment applied to subcontracted production (for example which accounts
  absorb the service cost) can be set at the level of the individual product or product
  category, not only as one global setting applied identically to every subcontracted item.
WHY_IT_MATTERS: >
  A single global setting cannot represent a company that subcontracts different product lines
  under genuinely different accounting treatments, forcing a workaround that itself becomes a
  source of misclassification.
DISCONFIRMING_OBSERVATION: >
  Two different products, both produced through outside-party work, cannot be given different
  accounting treatment for their subcontracting cost; only one setting exists and it applies
  to all of them.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Attempt to configure two distinct subcontracted products with different accounting treatment
  for their externally-performed work and observe whether the configuration surface allows it.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q025

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q025
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The accounting treatment that documentation or configuration screens describe for a
  subcontracted transaction is the treatment that actually posts to the ledger for that same
  transaction, with no divergence between the two.
WHY_IT_MATTERS: >
  A gap between the described treatment and the posted treatment means anyone relying on the
  documentation to explain the books is relying on something false.
DISCONFIRMING_OBSERVATION: >
  The configuration screen or documentation for a subcontracted transaction's treatment
  describes one outcome, and the actual posted entries for an equivalent transaction show a
  different outcome.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Read the documented or configured description of a subcontracted transaction's accounting
  treatment, then run that transaction and compare the actual postings against the
  description.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q026

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q026
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a subcontracted process yields a secondary output alongside the main produced item,
  that secondary output's value is tracked as its own distinguishable amount rather than being
  folded silently into the main item's cost.
WHY_IT_MATTERS: >
  A secondary output whose value is invisibly merged into the main item overstates the main
  item's cost and leaves the secondary output unaccounted for entirely.
DISCONFIRMING_OBSERVATION: >
  A subcontracted process that produces both a main item and a secondary output posts value
  only for the main item, with the secondary output's cost impact unrecoverable from the
  record.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Run a subcontracted order configured to yield a secondary output alongside its main product
  and inspect whether the secondary output's value is separately identifiable.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q027

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q027
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a subcontracted order that has an accrued, not-yet-billed service cost either
  reverses that accrual explicitly or leaves it clearly flagged for resolution, rather than
  leaving it posted with no link to a now-cancelled order.
WHY_IT_MATTERS: >
  An accrual left orphaned by a cancellation becomes a balance nobody can explain the origin of
  when the books are later reviewed.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order with an accrued unbilled service cost leaves that accrual posted and
  unresolved, with no reversal and no flag connecting it to the cancellation.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Accrue an unbilled service cost against an open subcontracted order, cancel the order, and
  inspect whether the accrual is resolved or left standing.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q028

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q028
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the outside party's actual bill differs from an amount the owning company had already
  accrued for that service, the difference is posted as an identifiable adjustment rather than
  the original accrual simply being silently overwritten with no trace of the original
  estimate.
WHY_IT_MATTERS: >
  Overwriting an estimate without recording the adjustment hides the fact that the original
  estimate was wrong, which matters for improving future estimates and for audit trail
  integrity.
DISCONFIRMING_OBSERVATION: >
  An accrued service cost estimate is replaced by the actual billed amount with no separate
  adjustment entry and no way to recover what the original estimate had been.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Accrue an estimated service cost, then record an actual bill for a different amount, and
  inspect whether the difference appears as a traceable adjustment.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q029

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q029
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When two separate companies within the same deployment both subcontract work to the same
  outside party, each company's externally-held value and service cost post only to that
  company's own books, never to the other's.
WHY_IT_MATTERS: >
  A shared outside party being used as a bridge between two companies' books is exactly the
  kind of leak that turns two supposedly separate sets of financial statements into one
  contaminated set.
DISCONFIRMING_OBSERVATION: >
  A subcontracted transaction run under one company shows any valuation or posting effect on a
  different company's books, where the only thing the two companies share is the same outside
  party.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Configure two separate companies to subcontract to the same outside party, run a transaction
  under each, and inspect whether either company's books show any effect from the other's
  transaction.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q030

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q030
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether the outside party's service cost is capitalized into the produced item's value or
  expensed directly is a distinct, inspectable configuration choice, not a behavior fixed
  unconditionally one way with no setting governing it.
WHY_IT_MATTERS: >
  A company with a legitimate policy of expensing certain service costs rather than
  capitalizing them needs that to be a real, documented choice, not something achievable only
  by fighting the default behavior.
DISCONFIRMING_OBSERVATION: >
  No configuration exists to choose between capitalizing and expensing the outside party's
  service cost; the behavior is fixed with nothing to inspect or change.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Look for a setting governing whether subcontracted service cost is capitalized or expensed,
  and attempt to change it and observe whether the posted treatment actually changes.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q031

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q031
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A service bill issued in a currency different from the owning company's functional currency
  is converted using a rate tied to a defined point in the transaction's own timeline, not an
  arbitrary or inconsistent rate that varies depending on when someone happens to look.
WHY_IT_MATTERS: >
  An inconsistent conversion point means the same transaction can show different costs to
  different reviewers depending purely on when they checked, which makes the cost figure
  unreliable.
DISCONFIRMING_OBSERVATION: >
  Viewing the same foreign-currency subcontracted service cost at two different times, with no
  new transaction event in between, shows two different converted amounts with no revaluation
  event explaining the change.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a subcontracted service bill in a currency different from the functional currency and
  inspect the converted amount at two different times with no intervening transaction.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q032

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q032
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an order's total service cost is allocated across several partial deliveries, the sum
  of the amounts allocated to each delivery equals the order's total billed service cost, with
  any rounding remainder assigned deterministically rather than simply lost.
WHY_IT_MATTERS: >
  A rounding remainder that disappears instead of being assigned somewhere is a small, silent,
  and permanently unreconcilable difference between the order total and what actually posted.
DISCONFIRMING_OBSERVATION: >
  The sum of service cost allocated across an order's partial deliveries does not equal the
  order's total billed service cost, and no rounding-remainder rule accounts for the gap.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split an order's service cost across at least three partial deliveries chosen so a rounding
  remainder is unavoidable, then sum the allocated amounts against the order total.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q033

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q033
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A scheduled background pass that computes accruals or revaluations includes every open
  subcontracted order in its scope, not only orders that happen to have had some other recent
  activity.
WHY_IT_MATTERS: >
  An accrual pass that skips quiet, long-open subcontracted orders would let their accounting
  drift silently out of step with orders that get touched more often.
DISCONFIRMING_OBSERVATION: >
  An open subcontracted order with no recent activity is skipped by a scheduled accrual or
  revaluation pass that other, more recently touched open orders are included in.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Leave one subcontracted order open and untouched for an extended period alongside another
  that receives regular activity, then run the scheduled pass and compare whether both were
  included.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q034

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q034
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A credit note issued by the outside party against a previously billed service reduces the
  produced item's recorded cost by a traceable amount, rather than posting as an unrelated
  credit with no link back to the item it originally valued.
WHY_IT_MATTERS: >
  A credit with no link back to the item leaves that item's valuation overstated indefinitely,
  since nothing connects the correction to what it was correcting.
DISCONFIRMING_OBSERVATION: >
  A credit note against a subcontracting service bill posts with no reference to the original
  bill or the item it valued, and the item's valuation remains unchanged after the credit.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record a service bill for a subcontracted order, then record a credit note against it, and
  inspect whether the produced item's valuation reflects the credit.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q035

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q035
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A service billed in full for an order that ultimately yields zero received output does not
  get silently absorbed into unrelated inventory value; it is recognized as a cost with no
  offsetting asset created.
WHY_IT_MATTERS: >
  A fully billed service with no output either inflates the cost of some unrelated item it gets
  dumped onto, or vanishes, and either way the loss on that failed order is hidden.
DISCONFIRMING_OBSERVATION: >
  A fully billed service for an order that yields zero output shows its cost absorbed into the
  valuation of a different, unrelated item, rather than recognized against the failed order
  itself.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Bill the full service cost for a subcontracted order that ultimately receives zero output and
  inspect where that cost ends up posted.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q036

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q036
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Reporting a suspected loss of components at an outside party and approving the resulting
  financial write-off are governed by distinct permissions, so the person observing or
  reporting a loss is not automatically the same person who can post its financial
  consequence.
WHY_IT_MATTERS: >
  Collapsing reporting and approval into the same permission removes the second-person check
  that write-offs specifically exist to enforce.
DISCONFIRMING_OBSERVATION: >
  The same single permission is sufficient both to report a loss at the outside party and to
  approve the financial write-off that results from it.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Attempt to report a loss and approve its write-off using only the permission associated with
  reporting, and observe whether the approval step also succeeds.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q037

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q037
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The ledger's ability to post a service cost against subcontracted output does not strictly
  require a commercial purchasing capability to be active; an internally recorded cost figure
  is sufficient to drive the valuation.
WHY_IT_MATTERS: >
  If ledger valuation silently requires the commercial ordering capability to be present, a
  company using only the internal production side of subcontracting without formal purchasing
  would get no valuation at all, with no warning why.
DISCONFIRMING_OBSERVATION: >
  With the commercial purchasing capability disabled or absent, a subcontracted order with an
  internally recorded cost figure produces no service-cost valuation on the output, and no
  message explains the omission.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Disable or remove the commercial purchasing capability while keeping an internally recorded
  cost figure for a subcontracted order, and inspect the resulting output valuation.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q038

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q038
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Changing which location represents an outside party's held stock, while components of that
  party are already recorded as being there, is either blocked or triggers an explicit
  migration of the existing valued quantities, rather than orphaning the value silently under
  the old location.
WHY_IT_MATTERS: >
  A silently orphaned valuation under a location nobody points to any more becomes untraceable
  stock value the next time anyone reconciles positions.
DISCONFIRMING_OBSERVATION: >
  Reassigning the location representing an outside party, while value is already recorded
  there, leaves that value under a location no longer referenced by the party's configuration,
  with no migration or block having occurred.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record component value at an outside party's assigned location, then change that assignment,
  and inspect what happens to the previously recorded value.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q039

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q039
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The figure used as the outside party's reported component consumption for a completed order
  carries a record of who or what confirmed it, distinguishing a confirmed figure from a
  figure automatically assumed with no confirmation step.
WHY_IT_MATTERS: >
  A costing figure with no confirmation trail cannot be defended later as anything other than
  an unverified assumption, however material the resulting variance turns out to be.
DISCONFIRMING_OBSERVATION: >
  The reported consumption figure used in costing a completed subcontracted order carries no
  record of confirmation, and it is not possible to tell whether it was ever checked against
  anything.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a subcontracted order using a reported consumption figure and inspect whether any
  confirmation of that figure is recorded.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q040

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q040
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  No combination of component cost, service cost, and correction events on a subcontracted
  order can drive the produced item's recorded unit valuation below zero.
WHY_IT_MATTERS: >
  A negative unit valuation is not a real accounting state for a physical item and signals that
  some correction or reversal chain has gone further than the original transaction it was
  meant to undo.
DISCONFIRMING_OBSERVATION: >
  A sequence of corrections, reversals, or credits on a subcontracted order results in the
  produced item carrying a recorded unit valuation below zero.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Chain a receipt, a reversal, a credit note, and a re-receipt on the same subcontracted order
  and inspect the resulting unit valuation at each step for a negative result.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q041

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q041
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A service bill for a subcontracted order that arrives after its accounting period has been
  closed is either posted into a still-open period with an explicit link back to the original
  order, or blocked outright with a clear reason, rather than silently altering the closed
  period's figures.
WHY_IT_MATTERS: >
  A closed period whose totals change without anyone deciding to reopen it defeats the entire
  purpose of having a close.
DISCONFIRMING_OBSERVATION: >
  Recording a late service bill for an order whose accounting period is already closed
  silently changes that closed period's reported totals with no reopening step and no warning.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Close the accounting period covering a subcontracted order's component consumption, then
  record the service bill after the close, and inspect whether the closed period's figures
  change.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q042

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q042
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Components returned from the outside party without the order itself being cancelled re-enter
  the owning company's ordinary valued stock at the same cost basis they carried while
  externally held, rather than at a re-derived or default cost.
WHY_IT_MATTERS: >
  Re-deriving a fresh cost on return rather than carrying the existing basis forward would let
  a simple physical return event change reported stock value with no transaction that actually
  justifies a cost change.
DISCONFIRMING_OBSERVATION: >
  Components returned from the outside party, with the order still open, re-enter valued stock
  at a cost different from what they carried immediately before the return, with no
  revaluation event to justify the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Return a portion of components from the outside party without cancelling the order, and
  compare the returned components' cost basis before and after the return.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q043

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q043
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Components mistakenly recorded as sent to the wrong outside party can be corrected to
  reflect the correct party without a break in the continuous cost-basis record for those
  units.
WHY_IT_MATTERS: >
  A correction that resets the cost basis, rather than merely correcting which party holds the
  units, would make an administrative fix look like an unrelated financial event.
DISCONFIRMING_OBSERVATION: >
  Correcting which outside party holds a set of components changes their recorded cost basis,
  when nothing about the correction should have altered value at all.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record components as sent to the wrong outside party, correct the party, and compare the
  cost basis before and after the correction.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q044

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q044
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When no explicit account assignment has been configured for subcontracting cost on a given
  product or category, the system requires that gap to be resolved before posting, rather than
  silently falling back to an arbitrary default account with no indication a fallback occurred.
WHY_IT_MATTERS: >
  A silent fallback to an arbitrary account scatters subcontracting cost across whatever the
  generic default happens to be, making it invisible to anyone reviewing subcontracting cost
  specifically.
DISCONFIRMING_OBSERVATION: >
  A subcontracted transaction with no explicit account assignment configured posts
  successfully to a default account with no warning or record that a fallback was used.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Remove or leave unset the explicit account assignment for a subcontracted product's cost and
  attempt to post a transaction for it.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q045

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q045
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Editing the component list that defines a subcontracted item, after orders using the prior
  version have already received and posted output, does not retroactively alter the valuation
  already posted for those completed orders.
WHY_IT_MATTERS: >
  Allowing a later definition change to reach back and rewrite an already-closed transaction's
  value would make historical figures unstable and unauditable.
DISCONFIRMING_OBSERVATION: >
  Editing the component list for a subcontracted item changes the already-posted valuation of
  orders that completed under the prior definition.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Complete a subcontracted order and post its valuation, then edit the item's component list,
  and inspect whether the already-posted order's valuation changes.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q046

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q046
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where output from one outside party is itself sent onward as input to a second subcontracted
  step, the second step's produced item value includes both the first step's full accumulated
  cost and the second step's own service cost, not merely the original raw component cost with
  one of the two service costs dropped.
WHY_IT_MATTERS: >
  Dropping either hop's service cost in a two-hop chain understates the final item's true cost
  by exactly the part of the process that was, this time, outsourced twice.
DISCONFIRMING_OBSERVATION: >
  A twice-subcontracted item's final valuation is missing the service cost from one of the two
  outside-party steps, reflecting only a single hop's added cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Chain two subcontracted steps so the first step's output becomes the second step's input,
  complete both, and inspect whether the final valuation reflects both steps' service costs.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q047

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q047
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A tool that corrects or adjusts subcontracting valuations in bulk across many orders at once
  applies the same posting rules and leaves the same audit trail as correcting one order
  individually, rather than taking a faster path that skips controls that apply to single
  transactions.
WHY_IT_MATTERS: >
  A bulk path that skips individual controls turns a convenience feature into the easiest way
  to make a large, under-scrutinized change to reported figures.
DISCONFIRMING_OBSERVATION: >
  Using a bulk correction tool across many subcontracted orders produces postings with less
  audit detail, or skips a control, that the same correction made one order at a time would
  have required.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Perform the same valuation correction on one order individually and on several orders via any
  available bulk mechanism, and compare the resulting postings and audit detail.
```

## G06-MRP_SUBCONTRACTING_ACCOUNT-Q048

```yaml
QID: G06-MRP_SUBCONTRACTING_ACCOUNT-Q048
MODULE: mrp_subcontracting_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A service bill still in a draft or unconfirmed state has no effect on the produced item's
  posted valuation; only a confirmed bill can move value.
WHY_IT_MATTERS: >
  Letting an unconfirmed, possibly-still-being-edited bill already affect posted valuation
  means the books can move based on a number that might still change before anyone finalizes
  it.
DISCONFIRMING_OBSERVATION: >
  Entering a service bill in a draft, unconfirmed state changes the produced item's posted
  valuation before that bill is confirmed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a service bill for a subcontracted order and leave it unconfirmed, then inspect the
  produced item's posted valuation before confirming the bill.
```
