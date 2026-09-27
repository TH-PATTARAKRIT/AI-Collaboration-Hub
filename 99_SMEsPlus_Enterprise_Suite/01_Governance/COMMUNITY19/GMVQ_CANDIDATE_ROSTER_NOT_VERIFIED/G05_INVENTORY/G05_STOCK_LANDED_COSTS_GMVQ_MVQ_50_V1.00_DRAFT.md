# G05 INVENTORY — stock_landed_costs — Module Verification Questions (MVQ)

**Document ID:** GMVQ-W2-P02-G05-STOCK_LANDED_COSTS-V1.00-DRAFT
**Group:** G05 INVENTORY
**Wave:** W2
**Author Cell:** P02
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN

## Module Metadata
- **Module (metadata name):** `stock_landed_costs`
- **Role in group:** SEAM — a cost arriving after the goods, pushed back onto units already received, sold, split, scrapped, or already in a closed period
- **Base module:** `stock`
- **actual_mvq_count:** 50
- **Standard bank reference:** 55 (shared, authored separately; not reproduced here)
- **Research depth (55 + actual_mvq):** 105

## Purpose
Module-specific research questions (MVQ) for the blind two-lane ROOM A study of `stock_landed_costs`.
Lane A (source reading) and Lane B (runtime observation only) each answer every question below
independently, joined on QID. Every question in this bank targets the seam this module exists to
cover, per the GMVQ Bridge Module Rule V1.00: if the accounting and timing capability were removed and the charge were simply added to a fresh, still-open receipt with nothing having moved or been billed since, the question would no longer make sense; every question here fails only at the seam between a late-arriving cost and units whose state has already moved on.

## Control
- Directive: SMEPLUS-GMVQ-25TEAM-ACCELERATION-20260927-001
- Governed by: GMVQ_AUTHORING_STANDARD_V1.00.md, GMVQ_BRIDGE_MODULE_RULE_V1.00.md
- Clean Room: no vendor or reference source tree; generic ERP domain knowledge only; no technical
  identifiers (model/table/field/method names, XML IDs, API paths) in question text; no vendor or
  product names.
- Closed vocabularies enforced: RISK_TIER in {CRITICAL, HIGH, MEDIUM};
  OUTPUT_CLASS in {BUSINESS INVARIANT, RISK, BEHAVIOUR, CONFIGURATION, BOUNDARY}.
- This document is DRAFT question content only. Not approved, not frozen, not verified,
  not MASTER-ready. No merge, release, or gate closure is authorized by this file.

---


```yaml
QID: G05-STOCK_LANDED_COSTS-Q001
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Selecting a different allocation basis, such as value, weight, quantity, or volume, for the same landed cost produces a different per-unit cost addition on at least one of the receipt lines it is applied to.
WHY_IT_MATTERS: >
  If the basis choice never actually changes the outcome, the allocation-basis configuration is cosmetic, and the resulting per-unit costs cannot be trusted to reflect the basis the business believes was used.
DISCONFIRMING_OBSERVATION: >
  Changing the allocation basis produces an identical per-line addition to every line regardless of the differing value, weight, quantity, or volume attributes of those lines.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply the same landed cost charge to a multi-line receipt under two different allocation bases, and compare the per-line results.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q002
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the allocation basis does not divide the total cost evenly across lines, a residual amount is assigned to a specific, identifiable line rather than silently disappearing.
WHY_IT_MATTERS: >
  An unaccounted residual, repeated across many landed cost documents, silently accumulates into a material unexplained gap between the entered charge and what was actually posted.
DISCONFIRMING_OBSERVATION: >
  The sum of the per-line allocated amounts does not equal the total landed cost, and no line or record accounts for the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost whose total does not divide evenly under the chosen basis, and check that the sum of the per-line amounts equals the total charge.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q003
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a landed cost is applied to a receipt from which some units have already left stock, the value attributable to the already-departed units is recognized as a cost-of-sale-side adjustment rather than added only to the remaining on-hand valuation.
WHY_IT_MATTERS: >
  Loading the entire late-arriving cost onto units still on hand would overstate the remaining inventory's value while understating the true cost of the units already sold.
DISCONFIRMING_OBSERVATION: >
  The entire landed cost is added only to the units still on hand, with no adjustment recognized for the portion attributable to units that had already left.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Sell part of a receipt's quantity, then apply a landed cost to that receipt, and check whether any adjustment was recognized for the already-departed portion.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q004
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The per-unit valuation increase from a landed cost is computed the same way for both the departed portion and the remaining portion of a receipt line, even though the accounting destination differs between the two.
WHY_IT_MATTERS: >
  A different per-unit increase for departed versus remaining units, for the same cost, would mean the allocation method itself is inconsistent depending purely on when a unit happened to leave.
DISCONFIRMING_OBSERVATION: >
  The per-unit cost increase applied to the remaining on-hand units differs from the per-unit amount used to compute the adjustment for departed units, for the same landed cost line.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost to a line with both departed and remaining quantity, and compare the per-unit increase implied on each side.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q005
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Applying a landed cost dated inside an accounting period that has already been closed is blocked or redirected to the current open period rather than silently posting into the closed period.
WHY_IT_MATTERS: >
  Silently posting a late cost into a period reviewers have already treated as final would let a landed cost quietly alter figures that are supposed to be immutable.
DISCONFIRMING_OBSERVATION: >
  A landed cost applied after its period was closed posts its valuation entries into that closed period with no warning or redirection.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Close an accounting period, then attempt to apply a landed cost dated inside that period, and observe the system's response.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q006
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Applying a second landed cost document referencing the same receipt for what is otherwise the same charge adds a further, independent allocation rather than silently detecting and blocking it as a duplicate.
WHY_IT_MATTERS: >
  If a duplicate charge is silently merged or blocked with no independent trace, there is no way to tell whether the business was actually billed once or twice, or whether the true duplicate was ever caught.
DISCONFIRMING_OBSERVATION: >
  A second landed cost document for an otherwise identical charge on the same receipt is silently merged with, or silently replaces, the first, leaving no independent trace of both having existed.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Apply one landed cost to a receipt, then apply a second, otherwise identical landed cost to the same receipt, and check whether both allocations exist independently.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q007
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reversing an applied landed cost creates a compensating adjustment to valuation rather than deleting or rewriting the original allocation entries.
WHY_IT_MATTERS: >
  Editing a posted allocation in place, instead of compensating it, destroys the audit trail of what was originally allocated and later reversed.
DISCONFIRMING_OBSERVATION: >
  Reversing a landed cost removes or edits the original valuation entries in place, leaving no trace that an allocation was ever posted and then reversed.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Apply a landed cost, confirm its entries posted, then reverse it and inspect whether the original entries still exist alongside a new compensating entry.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q008
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reversing a landed cost that had partly been recognized as a cost-of-sale-side adjustment against already-departed units re-adjusts that expensed portion, not just the remaining on-hand valuation.
WHY_IT_MATTERS: >
  Reversing only the on-hand side while leaving the already-expensed side untouched would make the total reversal incomplete, leaving a portion of the original cost permanently and incorrectly recognized.
DISCONFIRMING_OBSERVATION: >
  Reversing a landed cost only undoes the on-hand valuation impact and leaves the previously recognized cost-of-sale-side adjustment untouched.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost to a receipt with both departed and remaining quantity, then reverse it and check whether both the on-hand and cost-of-sale-side effects were undone.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q009
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Applying a landed cost to a receipt where some received units were later scrapped still allocates a cost share to the scrapped quantity, recognized as an expense rather than added to a valuation that no longer exists.
WHY_IT_MATTERS: >
  Silently skipping the scrapped share and redistributing it onto the remaining units would inflate the remaining stock's value with cost that actually belongs to inventory that is already gone.
DISCONFIRMING_OBSERVATION: >
  The landed cost allocation silently skips the scrapped quantity's share, redistributing it only across the remaining units with no separate accounting for the scrapped portion.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Scrap part of a receipt's received quantity, then apply a landed cost to that receipt, and check how the scrapped portion's share was treated.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q010
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the receipt's lot has since been split into sub-lots, a landed cost applied afterward distributes its allocation across all resulting sub-lots in proportion to their remaining quantity.
WHY_IT_MATTERS: >
  Allocating only to one resulting sub-lot, or failing to find any lot at all, would leave part of the received quantity permanently untouched by a cost that legitimately applies to all of it.
DISCONFIRMING_OBSERVATION: >
  A landed cost applied after a lot split is allocated only to one of the resulting sub-lots, or fails to find any lot to allocate to.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split a received lot into sub-lots, then apply a landed cost to the original receipt line, and check how the allocation was distributed across the resulting sub-lots.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q011
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing the allocation basis or the per-line split after a landed cost has already posted requires a new corrective posting; the originally posted entries are not silently rewritten.
WHY_IT_MATTERS: >
  Silently rewriting already-posted entries after an allocation change would erase the record of what was actually reported for a prior period, without any corrective document to explain the change.
DISCONFIRMING_OBSERVATION: >
  Changing the allocation configuration after posting silently updates the already-posted valuation entries without any new corrective entry.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Apply and post a landed cost, then change its allocation basis afterward, and inspect whether the original entries changed in place or a new correction was created.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q012
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Applying, or posting, a landed cost requires a permission distinct from the permission needed merely to create a draft landed cost document, and the application is attributed to the user who triggered it.
WHY_IT_MATTERS: >
  If any user who can draft a landed cost can also post it unattributed, there is no control separating who may propose a cost allocation from who may commit it to the books.
DISCONFIRMING_OBSERVATION: >
  A landed cost can be moved from draft to posted with no record of which user triggered the posting, or by a user who holds no more than draft-creation rights.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Grant a user only draft-creation rights on landed costs, and attempt to have that user post one to completion.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q013
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Once a landed cost is applied, the receipt's own valuation record reflects the added cost, making the receipt itself the record any general stock valuation report reads from.
WHY_IT_MATTERS: >
  If a standard valuation report keeps showing the pre-landed-cost figure, anyone relying on that report without separately consulting the landed cost document would be working from a stale, understated value.
DISCONFIRMING_OBSERVATION: >
  A stock valuation report continues to reflect the pre-landed-cost value even after the landed cost has been applied, requiring the landed cost document itself to be consulted separately to see the true value.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Apply a landed cost to a receipt, then check whether a general stock valuation report already reflects the added cost.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q014
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A landed cost cannot be applied while the vendor bill or charge document it draws its amount from is still unconfirmed or in draft.
WHY_IT_MATTERS: >
  Posting a value drawn from a charge that is not yet confirmed would let an amount that could still change flow into the books as if it were final.
DISCONFIRMING_OBSERVATION: >
  A landed cost is successfully applied and posts a value drawn from a charge document that itself is still unconfirmed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attempt to apply a landed cost whose charge amount is sourced from a vendor bill that has not yet been confirmed, and observe the outcome.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q015
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the landed cost's charge is recorded in a currency different from the receiving company's accounting currency, the amount allocated to stock is converted at a rate tied to the landed cost's own date, not the original receipt's date.
WHY_IT_MATTERS: >
  Using the receipt's older rate for a charge that arrived later would mix two different points in time into a single converted figure, producing a value that matches neither date's true rate.
DISCONFIRMING_OBSERVATION: >
  The allocated amount uses the exchange rate from the original receipt date rather than the landed cost's own posting date, or mixes the two inconsistently.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a foreign-currency landed cost, dated later than its receipt, to a receipt recorded under a different exchange rate, and check which date's rate was used.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q016
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A landed cost can still be applied to a receipt that has reached a completed state; completion of the receipt does not lock it against a later landed cost.
WHY_IT_MATTERS: >
  If a completed receipt could never accept a landed cost, every late-arriving charge, which is the entire reason this capability exists, would have nowhere to go.
DISCONFIRMING_OBSERVATION: >
  A completed receipt cannot accept a landed cost at all, or accepting one silently reopens the receipt's own operational state.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Complete a receipt fully, then attempt to apply a landed cost to it, and observe whether it is accepted and whether the receipt's own state is disturbed.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q017
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If posting the accounting entries for a landed cost fails partway, none of the valuation changes take effect; there is no state where quantities show an updated cost but no entry exists to support it.
WHY_IT_MATTERS: >
  A partially applied landed cost, with an updated value but no supporting entry, would create inventory figures the ledger cannot explain if anyone reconciled the two at that moment.
DISCONFIRMING_OBSERVATION: >
  A failed landed cost posting leaves stock valuation partially updated while the accounting entries are missing or incomplete.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Force the accounting posting step of a landed cost to fail partway through, and check whether any valuation change took effect without a supporting entry.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q018
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A user with permission to edit stock valuation configuration but no accounting permissions cannot independently apply a landed cost, since applying it requires both scopes to be satisfied.
WHY_IT_MATTERS: >
  If either scope alone were sufficient, a user could allocate cost into the books without ever having been granted the accounting authority that action actually represents.
DISCONFIRMING_OBSERVATION: >
  A user holding only stock-side permissions is able to apply a landed cost and post its accounting entries without any accounting-side permission being checked.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Grant a user only stock-side configuration permissions, withhold accounting permissions, and attempt to have that user apply a landed cost.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q019
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The sum of all per-line allocations from one landed cost document always equals the total charge amount entered on that document.
WHY_IT_MATTERS: >
  A mismatch between the entered charge and the sum actually allocated would mean part of what the business was billed is either fabricated or has vanished from the books.
DISCONFIRMING_OBSERVATION: >
  The sum of the per-line allocated amounts differs from the document's total charge amount, with the difference unexplained.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost with a specific total charge across several lines, then sum the resulting per-line allocations and compare to the entered total.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q020
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling a landed cost document while still in draft leaves the underlying receipt's valuation completely untouched.
WHY_IT_MATTERS: >
  Any valuation effect from a document that was never actually applied would mean draft-stage content is leaking into the books before anyone confirmed it.
DISCONFIRMING_OBSERVATION: >
  Cancelling a draft, unapplied landed cost still changes the valuation of the receipt it targeted.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a draft landed cost targeting a receipt, cancel it before applying, and check whether the receipt's valuation changed at all.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q021
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A landed cost entered with a negative amount, representing a credit or rebate, is allocated and posted using the same mechanism as a positive charge, reducing rather than increasing the affected valuation.
WHY_IT_MATTERS: >
  If negative charges are rejected or silently treated as positive, a legitimate rebate could never be reflected in inventory valuation through the mechanism built for exactly this kind of adjustment.
DISCONFIRMING_OBSERVATION: >
  A negative landed cost amount is rejected outright, or is silently treated as a positive addition to valuation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost with a negative charge amount to a receipt, and check whether it reduced the affected valuation using the same allocation mechanism as a positive charge.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q022
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A landed cost document is scoped to a single company and can only target receipts owned by that same company.
WHY_IT_MATTERS: >
  A landed cost that could reach across a company boundary would let one legal entity's cost allocation directly alter another entity's books with no inter-company recognition.
DISCONFIRMING_OBSERVATION: >
  A landed cost document is able to allocate cost onto a receipt that belongs to a different company than the landed cost document itself.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to apply a landed cost created under one company against a receipt owned by a different company, and observe whether it is allowed.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q023
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether confirming a landed cost document immediately posts its accounting entries, or leaves the allocation computed but unposted pending a separate action, is a distinct and observable step rather than a single combined action with no intermediate state.
WHY_IT_MATTERS: >
  If confirmation and posting cannot be told apart, there is no way to review a computed allocation before it becomes a committed accounting entry, removing an opportunity to catch an error before it is posted.
DISCONFIRMING_OBSERVATION: >
  There is no way to observe an intermediate state where the allocation has been computed but not yet posted; confirmation and posting are indistinguishable as a single atomic event with no separate trace.
EXPECTED_SURFACE: S1,S2,S5
PRECONDITIONS: >
  Confirm a landed cost document and attempt to observe whether a computed-but-unposted state exists before the accounting entries actually post.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q024
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The added per-unit cost from an applied landed cost is reflected in that unit's own valuation record, reachable without cross-referencing the landed cost document separately.
WHY_IT_MATTERS: >
  If the true current cost can only be reconstructed by manually adding together a receipt and every landed cost document that ever touched it, ordinary valuation lookups will systematically understate value.
DISCONFIRMING_OBSERVATION: >
  The only way to determine a specific unit's true current cost, after a landed cost was applied, is to manually add together the receipt and every landed cost document that has targeted it.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Apply a landed cost to a receipt, then check a specific unit's own valuation record for whether the added cost is already reflected there.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q025
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a given type of charge, such as freight, insurance, or customs, is eligible to be applied as a landed cost is governed by a configuration marking on that charge type, not available for any arbitrary line item.
WHY_IT_MATTERS: >
  Allowing any arbitrary line item into a landed cost allocation, with no eligibility control, would let unrelated costs be pushed into inventory valuation with no governance over what belongs there.
DISCONFIRMING_OBSERVATION: >
  Any charge line at all, with no eligibility marking, can be pulled into a landed cost allocation.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Attempt to apply a charge line with no landed-cost eligibility marking as a landed cost, and observe whether the system allows it.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q026
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The allocation basis actually applied when a landed cost posts is exactly the basis selected on the document at the time of posting, not a different default silently substituted.
WHY_IT_MATTERS: >
  A silent substitution of the actual basis used, versus what the document shows as selected, would make the visible configuration a false representation of what was actually posted.
DISCONFIRMING_OBSERVATION: >
  The posted allocation reflects a different basis than the one shown as selected on the document.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Select a specific allocation basis on a landed cost document, apply it, and compare the posted per-line split to what that selected basis should produce.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q027
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Editing the charge lines or target receipts of a landed cost while still in draft produces no valuation change until the document is applied.
WHY_IT_MATTERS: >
  A valuation change appearing before a document is actually applied would mean draft edits are leaking into the books ahead of any deliberate confirmation.
DISCONFIRMING_OBSERVATION: >
  A valuation change already exists that traces back to a landed cost document that has not yet been applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Edit the charge lines and target receipts of a draft landed cost several times, and check whether any valuation change exists before the document is applied.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q028
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A unit's current valuation can be decomposed to show which landed cost documents, if any, contributed to it, distinct from its original receipt cost.
WHY_IT_MATTERS: >
  Without this decomposition, a reviewer cannot tell whether an unexpected value is due to the original purchase or to a subsequent cost that arrived later, making the figure hard to explain.
DISCONFIRMING_OBSERVATION: >
  There is no way to determine, for a given unit, whether any part of its current value came from a landed cost versus its original receipt.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a landed cost to a receipt, then attempt to decompose a specific unit's current value into its original receipt cost and any landed cost contribution.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q029
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a single receipt's lines span multiple locations or warehouses, a landed cost applied to that receipt allocates across all of those lines regardless of which physical location each line moved to.
WHY_IT_MATTERS: >
  Silently omitting lines in other locations would leave part of the charged cost with no unit it was ever allocated to, understating the value of stock that legitimately incurred it.
DISCONFIRMING_OBSERVATION: >
  A landed cost applied to a multi-location receipt only allocates to lines in one of the locations, silently omitting the others.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive stock across multiple locations on a single receipt, apply a landed cost to that receipt, and check whether every location's lines received a share.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q030
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two independently created landed cost documents that both target the same receipt line are each applied and posted as separate, additive allocations rather than one silently overwriting the effect of the other.
WHY_IT_MATTERS: >
  One allocation silently erasing another would mean a legitimately incurred cost simply vanishes from the books with no error or trace to explain where it went.
DISCONFIRMING_OBSERVATION: >
  Applying a second landed cost to a line already affected by a first landed cost erases or overwrites the first allocation's effect instead of adding to it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply one landed cost to a receipt line, then apply a second, independent landed cost to the same line, and check whether both effects are present.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q031
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Attempting to apply a landed cost against a receipt line that has since been deleted or fully reversed is blocked with an identifiable error rather than silently allocating to nothing.
WHY_IT_MATTERS: >
  A silent no-op allocation would leave the entered charge amount with no unit it was ever posted against, an unexplained gap that is easy to miss until reconciliation.
DISCONFIRMING_OBSERVATION: >
  A landed cost applies without error against a receipt line that no longer exists, with the allocated amount unaccounted for anywhere.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Delete or fully reverse a receipt line, then attempt to apply a landed cost that targets it, and observe the outcome.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q032
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A landed cost cannot be applied to a receipt that has not yet reached a confirmed or received state.
WHY_IT_MATTERS: >
  Allowing a cost to attach to a receipt that might still change or never complete would let inventory valuation be built on an event that has not actually happened yet.
DISCONFIRMING_OBSERVATION: >
  A landed cost is successfully applied against a receipt still in a draft, unconfirmed state.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attempt to apply a landed cost to a receipt that is still in a draft, unconfirmed state, and observe whether it is accepted.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q033
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A landed cost document can be scoped to a subset of a receipt's lines, and lines not included receive no valuation change from that document.
WHY_IT_MATTERS: >
  Bleeding an allocation onto lines that were never selected would misattribute cost to units the charge was never actually meant to cover.
DISCONFIRMING_OBSERVATION: >
  Applying a landed cost scoped to specific lines also changes the valuation of receipt lines that were not selected.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost scoped to only some lines of a multi-line receipt, and check whether the unselected lines' valuation changed.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q034
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A landed cost can still be applied to a receipt line whose product has since been archived or discontinued, since the allocation targets the historical movement, not the product's current active state.
WHY_IT_MATTERS: >
  Blocking a legitimate late cost purely because the product was later discontinued would leave a real charge with nowhere to be recorded, even though the historical movement it applies to is unaffected by the product's current status.
DISCONFIRMING_OBSERVATION: >
  Applying a landed cost fails or is blocked solely because the product on the targeted receipt line has since been archived.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Archive the product on a receipt line after receiving it, then attempt to apply a landed cost to that receipt line.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q035
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reversing a receipt that already has an applied landed cost also reverses or flags the landed cost's own allocation, rather than leaving an allocation attached to a movement that no longer exists.
WHY_IT_MATTERS: >
  An allocation left standing against a movement that has been undone would keep cost in the books with no underlying physical event left to justify it.
DISCONFIRMING_OBSERVATION: >
  Reversing the underlying receipt leaves the previously applied landed cost's valuation entries standing, now attached to a movement that has been undone.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost to a receipt, then reverse the receipt itself, and check what happened to the landed cost's own valuation entries.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q036
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When value is used as the allocation basis, the value used is each line's own extended receipt cost at the time of allocation, not a value read from an unrelated source such as a current sales price.
WHY_IT_MATTERS: >
  Basing a cost allocation on a sales price would tie an internal valuation calculation to an external, unrelated figure that has nothing to do with what was actually paid to receive the goods.
DISCONFIRMING_OBSERVATION: >
  A value-based allocation splits the cost using a figure other than each line's own extended receipt cost, such as a sales price or an unrelated valuation field.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a value-based landed cost to lines whose receipt cost and sales price differ, and check which figure the allocation actually used.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q037
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A weight- or volume-based allocation cannot silently succeed for a line whose product has no weight or volume recorded; it either blocks or falls back to a defined default with a visible indication.
WHY_IT_MATTERS: >
  A silent zero or undefined substitution for missing weight or volume data would misallocate cost with no indication that the underlying data was ever missing.
DISCONFIRMING_OBSERVATION: >
  A weight- or volume-based allocation completes and produces a share for a line whose product has no recorded weight or volume, with no indication that a default or zero was substituted.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a weight- or volume-based landed cost to a receipt containing a line whose product has no recorded weight or volume, and observe the outcome.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q038
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A landed cost applies its share correctly to lines whose products use different configured valuation methods from one another, each updated according to its own method's mechanics.
WHY_IT_MATTERS: >
  If mixing valuation methods within one allocation breaks one method's own mechanics, the resulting cost for that line would no longer be a valid figure under any method at all.
DISCONFIRMING_OBSERVATION: >
  Applying one landed cost document across lines with differing valuation methods causes one method's updated lines to be valued incorrectly relative to what that method alone would produce.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a single landed cost across receipt lines whose products use two different configured valuation methods, and check each line's result against what its own method alone should produce.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q039
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If every line a landed cost targeted has, since document creation, been fully consumed such that no on-hand quantity remains to receive an asset-side share, the entire allocation is recognized as a cost-of-sale-side adjustment rather than failing outright.
WHY_IT_MATTERS: >
  Failing outright, or silently discarding the allocation, would leave a legitimately incurred cost with no accounting recognition anywhere simply because timing happened to consume all the stock first.
DISCONFIRMING_OBSERVATION: >
  A landed cost targeting lines with zero remaining on-hand quantity fails to apply at all, or silently discards the allocation with no accounting effect anywhere.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Fully consume all quantity on a receipt's lines, then apply a landed cost targeting that receipt, and observe whether an allocation is still recognized.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q040
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A very small total landed cost still produces a nonzero allocation to at least one line, with fractional-currency handling resolved rather than the whole allocation vanishing to zero.
WHY_IT_MATTERS: >
  An allocation that rounds to zero on every line would make the entered charge amount disappear from the books entirely, even though it was genuinely incurred.
DISCONFIRMING_OBSERVATION: >
  A landed cost small enough to round to zero on every individual line disappears from the ledger, with the entered charge amount unaccounted for.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost with a total small enough that even distribution would round to zero per line, and check whether the total amount is still reflected somewhere in the ledger.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q041
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Correcting the vendor bill amount that a landed cost's charge was originally drawn from, after the landed cost has already applied, does not retroactively change the already-posted allocation; a new adjustment is required.
WHY_IT_MATTERS: >
  A silent retroactive change to an already-posted allocation, triggered by editing an unrelated source document, would let historical figures shift with no corrective document to explain why.
DISCONFIRMING_OBSERVATION: >
  Editing the originating vendor bill amount after the landed cost was applied silently changes the already-posted valuation entries with no new adjustment document.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Apply a landed cost sourced from a vendor bill, then edit that vendor bill's amount afterward, and check whether the already-posted landed cost entries changed.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q042
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The exchange rate applied when converting a foreign-currency landed cost to the receiving company's base currency is the rate in effect at the landed cost's own date, not the receipt's original date.
WHY_IT_MATTERS: >
  Using the receipt's original rate for a charge dated later would produce a converted value that corresponds to neither date's actual market rate.
DISCONFIRMING_OBSERVATION: >
  The conversion uses the receipt's original exchange rate rather than the landed cost's own date, producing a value inconsistent with the landed cost's stated date.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a foreign-currency landed cost dated after its receipt to a company whose base currency differs, and check which date's exchange rate was used in the conversion.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q043
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Entries generated by a landed cost are distinguishable in a ledger inspection from the ordinary receipt valuation entry they augment, not merged into a single indistinguishable line.
WHY_IT_MATTERS: >
  Merging the two into one indistinguishable line would make it impossible, during a review, to tell how much of a unit's value came from the original purchase versus a later added cost.
DISCONFIRMING_OBSERVATION: >
  There is no way, from the ledger, to tell whether a valuation entry originated from the original receipt or from a subsequently applied landed cost.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a landed cost to a receipt, then inspect the ledger to determine whether the original receipt entry and the landed cost's entry can be told apart.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q044
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A landed cost applied long after the original receipt, where the company's base accounting currency has since changed, is posted in the currency in effect at the landed cost's own date, and the historical receipt entries are not retroactively restated.
WHY_IT_MATTERS: >
  Retroactively restating old entries to a new base currency would alter figures that were already reported and closed under the currency in effect at the time.
DISCONFIRMING_OBSERVATION: >
  Applying a late landed cost restates or edits the historical receipt entries to the new base currency instead of only posting its own new entries in the currently effective currency.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Change a company's base accounting currency, then apply a landed cost to a receipt recorded under the old currency, and check whether the historical entries were altered.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q045
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An already-applied landed cost cannot be edited directly; changing its content requires cancelling or reversing it first and creating a new one.
WHY_IT_MATTERS: >
  Direct in-place editing of an already-posted document would let a committed accounting event be silently rewritten with no separate corrective record.
DISCONFIRMING_OBSERVATION: >
  The charge amount or allocation basis of an already-applied landed cost can be edited in place, with the previously posted entries updating to match, with no new document created.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Apply a landed cost, then attempt to directly edit its charge amount or allocation basis, and observe whether the change is permitted in place.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q046
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A landed cost's allocated amounts only ever land on receipt lines explicitly included as targets of that document.
WHY_IT_MATTERS: >
  Cost appearing against a line that was never selected as a target would mean the allocation mechanism is reaching beyond the scope the document itself declares.
DISCONFIRMING_OBSERVATION: >
  Some portion of a landed cost's total charge is found posted against a receipt line that was never selected as a target of that document.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost scoped to specific receipt lines, then check every line in the ledger with a posted amount traceable to that document against the document's declared targets.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q047
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A landed cost still in draft has no effect on any value shown when inspecting current stock valuation.
WHY_IT_MATTERS: >
  A draft, unapplied document already affecting the visible valuation would mean stock figures reflect a cost the business has not actually committed to yet.
DISCONFIRMING_OBSERVATION: >
  Stock valuation figures already reflect a landed cost's amount while that landed cost document is still in draft, unapplied.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a draft landed cost against a receipt, and before applying it, check whether current stock valuation already reflects its amount.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q048
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a landed cost dated earlier is applied after one dated later has already posted, the earlier one still allocates against the state of the receipt at the time it is actually applied, not retroactively inserted ahead of the later one.
WHY_IT_MATTERS: >
  Retroactively reordering an already-posted document to make room for a late-applied, earlier-dated one would rewrite figures that were already final at the time the later one posted.
DISCONFIRMING_OBSERVATION: >
  Applying an earlier-dated landed cost after a later-dated one has already posted causes the later one's already-posted entries to be renumbered, reordered, or altered.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a later-dated landed cost first, then apply an earlier-dated one afterward, and check whether the already-posted later entries were altered.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q049
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The system requires an explicit allocation basis selection before a landed cost can be applied; there is no silent default basis assumed when none is chosen.
WHY_IT_MATTERS: >
  A silent, undocumented default basis would let cost be split using a method nobody actually chose, with no way to know afterward which basis was actually used.
DISCONFIRMING_OBSERVATION: >
  A landed cost applies successfully with no allocation basis ever selected, using some undocumented default split.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to apply a landed cost document with no allocation basis selected, and observe whether the system blocks it or applies an undocumented default.
LAYER: BASE
```

```yaml
QID: G05-STOCK_LANDED_COSTS-Q050
MODULE: stock_landed_costs
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The ratio between the cost-of-sale-side adjustment and the remaining-valuation-side adjustment, for a landed cost applied against a partially-departed receipt line, matches the ratio of departed to remaining quantity on that line.
WHY_IT_MATTERS: >
  A mismatch between the split of the adjustment and the actual departed/remaining quantity ratio would mean the allocation between expense and asset is arbitrary rather than tied to what genuinely already left stock.
DISCONFIRMING_OBSERVATION: >
  The split between the cost-of-sale-side adjustment and the remaining-valuation-side adjustment does not match the departed and remaining quantity ratio, with no other documented factor explaining the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost to a receipt line with a known departed and remaining quantity split, and check whether the expense/asset split of the adjustment matches that quantity ratio.
LAYER: PROCESS
```
