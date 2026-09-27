# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_product_matrix Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-SALE_PRODUCT_MATRIX-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_product_matrix`
**Wave:** W2
**Author Cell:** P-S9 (GMVQ Question Factory — Internal Production Team S9, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

`sale_product_matrix` is a BRIDGE module (GMVQ_BRIDGE_MODULE_RULE_V1.00). Its seam is grid entry of attribute combinations onto a SALES line specifically. Per the Bridge Module Rule, every question in this bank was tested against the seam question: "if this capability were removed and the order and the grid-entry mechanism were used entirely apart, would the question still make sense?" A YES answer means the question belongs to the base `sale` bank or to a sibling grid bank, not here, and was cut.

Two sibling grid banks already exist and were read in full before authoring: the master-data grid bank (`G03_PRODUCT_MATRIX`, document-agnostic — combination validity, generic pricing/tax resolution, permission, audit, tenant isolation, inline creation, concurrency) and the purchase-side grid bank (`G07_PURCHASE_PRODUCT_MATRIX`, vendor-specific — vendor catalogue restriction, vendor cost/lead-time/MOQ resolution, vendor-side three-way match, standing vendor commitments). This bank does not mirror either: it is built around what is genuinely SALES-side — which combinations a customer may be offered versus which exist; price-list coverage gaps per combination; available-to-promise at the actual moment of promising a customer; a combination promised then discontinued; the grid acting on an order already partially delivered or invoiced; how grid-created lines render on the customer-facing document; customer-specific negotiated combination terms and allocations; approval workflows triggered by grid-driven totals; concurrency and audit trail of bulk sales entry; cancellation/return of grid-created lines after partial fulfillment; and tenant/company-scope boundaries for customer-facing exposure.

## Control

- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$DIR"/*.md | sort` was run before writing a single question, against both `G03_PRODUCT_MATRIX_GMVQ_MVQ_48_V1.00_DRAFT.md` (48 questions) and `G07_PURCHASE_PRODUCT_MATRIX_GMVQ_MVQ_48_V1.00_DRAFT.md` (48 questions). No question in this bank restates either sibling's ground with the nouns swapped: the master-data bank's ground is document-agnostic grid mechanics and was left untouched; the purchase-side bank's ground is vendor-catalogue/cost/commitment resolution and was left untouched. Every question here is specific to customer-facing exposure, promise-time availability, and the sales order's own partial-delivery/partial-invoice lifecycle.
- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong, and the disconfirming observation is a distinct event for every question — no two questions share one failure event.
- No padding: 48 questions exist because they test 48 distinct material hypotheses at the seam. Depth requirement (55 shared + 48 module minimum = 103) is met once combined with the shared standard bank.
- This module carries one layer at the seam; the `LAYER` field is omitted throughout.
- Clean-room compliance: no vendor or product name, no technical identifier (model, table, field, method, XML ID, API path, standard or profile name), and no implementation shape appears anywhere in question text.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank. Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.
- Seam dimensions represented (GMVQ_BRIDGE_MODULE_RULE_V1.00 §3): ownership (Q001-Q002, Q005-Q008, Q020, Q022, Q025, Q029-Q031, Q036, Q038, Q045, Q048), timing (Q003-Q004, Q011), quantity and money (Q009, Q027-Q028, Q032), ordering (Q010, Q037), partiality (Q012, Q015, Q017-Q018, Q021, Q023), lifecycle mismatch (Q013-Q014, Q026, Q034), authority (Q016, Q024, Q033, Q035, Q043, Q046-Q047), reversal (Q019, Q041-Q042, Q044), error asymmetry (Q039-Q040).
- Coverage map: customer- and channel-specific combination exposure Q001-Q004 · price list coverage gaps per combination Q005-Q008 · available-to-promise at the moment of promising Q009-Q012 · a promised combination later discontinued Q013-Q016 · grid entry against an order already partially delivered Q017-Q020 · grid entry against an order already partially invoiced Q021-Q024 · customer-facing document rendering of grid-created lines Q025-Q028 · customer-specific restricted and negotiated combination terms Q029-Q032 · approval workflow triggered by grid-driven totals Q033-Q036 · concurrency and audit trail of bulk sales grid entry Q037-Q040 · cancellation and reversal of grid-created sales lines after partial fulfillment Q041-Q044 · tenant and company-scope boundary for customer-facing combination exposure Q045-Q048

## G08-SALE_PRODUCT_MATRIX-Q001

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q001
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The set of combinations offered to a specific customer through the grid reflects that customer's own
  eligibility, such as their price list, segment, or sales channel, not the full set of combinations that exist
  as valid sellable records generally.
WHY_IT_MATTERS: >
  Offering combinations a customer is not actually eligible to buy risks quoting products or terms the business
  never intended to extend to that customer.
DISCONFIRMING_OBSERVATION: >
  A combination excluded from a customer's applicable price list or segment still appears as selectable in the
  grid for that customer.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a combination excluded from one customer's applicable segment, and open the grid for an order to
  that customer.
```

## G08-SALE_PRODUCT_MATRIX-Q002

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q002
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a combination is valid generally but restricted to a specific sales channel, such as an online
  storefront versus direct sales, the grid used in a channel where the combination is not offered excludes it,
  rather than exposing every existing combination regardless of channel.
WHY_IT_MATTERS: >
  A combination sold through the wrong channel might carry different terms, availability, or regulatory status
  than intended for that channel.
DISCONFIRMING_OBSERVATION: >
  A combination restricted to one sales channel is selectable through the grid in a different channel where it
  is not meant to be offered.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Restrict a combination to one sales channel and attempt to select it through the grid in a document created
  under a different channel.
```

## G08-SALE_PRODUCT_MATRIX-Q003

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q003
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Switching the customer on an in-progress grid session re-evaluates which already-entered combinations remain
  eligible for the newly selected customer, rather than carrying over a prior customer's eligible set unchanged.
WHY_IT_MATTERS: >
  Combinations valid for the original customer may not be offerable to the newly selected one, and carrying them
  over silently could create lines the business never intended to offer that customer.
DISCONFIRMING_OBSERVATION: >
  Changing the customer mid-session leaves combinations selected under the previous customer's eligibility still
  present and unflagged, even though they are not offerable to the new customer.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Begin a grid session for one customer, select combinations, then switch to a different customer with a
  different eligible set, and observe whether the entered combinations are re-evaluated.
```

## G08-SALE_PRODUCT_MATRIX-Q004

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q004
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A combination newly made eligible for a customer after the grid was first opened in the current session is
  reachable by refreshing the grid, without requiring the order to be abandoned and restarted.
WHY_IT_MATTERS: >
  Forcing a restart to reach a combination that just became eligible unnecessarily discards whatever the user
  had already entered.
DISCONFIRMING_OBSERVATION: >
  A combination made eligible for the customer partway through an open grid session cannot be selected without
  discarding and restarting the entire order.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Open the grid, then make an additional combination eligible for the customer, and attempt to reach it without
  restarting the session.
```

## G08-SALE_PRODUCT_MATRIX-Q005

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q005
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combination absent from the customer's applicable price list resolves to an explicit exception at grid
  entry, rather than silently falling back to a generic list price with no indication the customer's own price
  list did not cover it.
WHY_IT_MATTERS: >
  A silent fallback can quietly charge or credit a different price than the one actually negotiated for that
  customer, without anyone noticing the gap.
DISCONFIRMING_OBSERVATION: >
  A combination missing from the customer's price list is entered through the grid at a generic price with no
  warning that the customer's own price list did not cover it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Remove a combination from a customer's specific price list and attempt to enter it through the grid for that
  customer.
```

## G08-SALE_PRODUCT_MATRIX-Q006

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q006
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a customer's price list covers some combinations in a grid session but not others, each combination
  resolves its own price independently according to whichever price list actually applies to it, rather than one
  combination's resolved list silently governing the whole session.
WHY_IT_MATTERS: >
  Letting one combination's price list bleed into others in the same session could apply prices the customer
  never actually negotiated for the rest.
DISCONFIRMING_OBSERVATION: >
  Two combinations in the same grid session, covered by different applicable price lists, both resolve to the
  price of only one of those lists.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure two combinations under different applicable price lists for the same customer, enter both in one
  grid session, and compare their resolved prices.
```

## G08-SALE_PRODUCT_MATRIX-Q007

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q007
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A discount or promotional rule scoped to specific combinations applies through the grid only to the
  combinations it actually covers, not uniformly to every combination entered in the same session.
WHY_IT_MATTERS: >
  A discount bleeding onto combinations it was never meant to cover misstates the price the customer should
  actually be charged.
DISCONFIRMING_OBSERVATION: >
  A combination outside the scope of an active promotional discount still receives that discount when entered
  alongside a covered combination in the same grid session.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Enter a discount-eligible combination and a non-eligible combination together in one grid session and check
  whether the discount applies to both.
```

## G08-SALE_PRODUCT_MATRIX-Q008

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q008
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combination-specific negotiated price override on file for a customer is honoured by the grid exactly as it
  would be by manual single-line entry for that same combination and customer.
WHY_IT_MATTERS: >
  A grid that bypasses a specific negotiated override charges the customer a different price than what was
  actually agreed with them.
DISCONFIRMING_OBSERVATION: >
  A combination with an on-file negotiated override for a customer resolves to a different price when entered
  through the grid than when entered as a single manual line.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a negotiated price override for a specific combination and customer, then compare the price resolved
  through the grid against manual single-line entry.
```

## G08-SALE_PRODUCT_MATRIX-Q009

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q009
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The availability shown per combination in the grid reflects what can actually be promised to a new customer
  commitment at that moment, not merely what physically exists in stock before accounting for what is already
  promised elsewhere.
WHY_IT_MATTERS: >
  Promising stock that is already committed to another customer's order creates a commitment the business cannot
  actually keep for one of the two customers.
DISCONFIRMING_OBSERVATION: >
  A combination already fully committed to other open orders still shows as available for a new promise through
  the grid.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Commit all available quantity of a combination to existing orders, then check what the grid shows as available
  for a new order.
```

## G08-SALE_PRODUCT_MATRIX-Q010

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q010
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two grid sessions for two different customers each attempting to promise the same limited quantity of a
  combination at nearly the same time do not both succeed in committing more than what is actually available.
WHY_IT_MATTERS: >
  Double-promising the same limited quantity creates a commitment to one customer that cannot actually be
  honoured once the other customer's order is also confirmed.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous grid sessions both successfully promise a combined quantity of the same combination
  exceeding what was actually available.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger two near-simultaneous grid sessions promising the same scarce combination against two different
  orders, and observe whether both succeed beyond actual availability.
```

## G08-SALE_PRODUCT_MATRIX-Q011

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q011
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The availability figure shown in the grid is evaluated at the moment the order is actually confirmed, not
  frozen at whatever it happened to be when the grid session was first opened, since availability can shift
  materially in the time between opening the grid and confirming the order.
WHY_IT_MATTERS: >
  Confirming against stale availability data can commit a customer to a quantity that was accurate only at some
  earlier moment and is no longer true.
DISCONFIRMING_OBSERVATION: >
  An order is confirmed with combination quantities based on availability data that has since changed, with no
  re-check at confirmation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Open the grid, allow the underlying availability to change through unrelated activity, then confirm the order
  and check whether availability was re-evaluated.
```

## G08-SALE_PRODUCT_MATRIX-Q012

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q012
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A combination with no availability at all is distinguishable in the grid from one with limited but nonzero
  availability, so a user can tell that no quantity can be promised apart from that some quantity can be
  promised but not the full requested amount.
WHY_IT_MATTERS: >
  Collapsing the two into one generic unavailable indicator prevents a user from making an informed partial-
  commitment decision.
DISCONFIRMING_OBSERVATION: >
  A combination with zero availability and one with limited but nonzero availability display identically in the
  grid.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Configure one combination with zero availability and another with limited availability, and compare how each
  displays in the grid.
```

## G08-SALE_PRODUCT_MATRIX-Q013

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q013
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combination that is discontinued after it has already been promised to a customer on an open, unfulfilled
  order line does not silently disappear from that order; it is flagged as no longer fulfillable so the
  commitment can be actively managed.
WHY_IT_MATTERS: >
  A silently vanishing line leaves the business unaware it has an outstanding promise to a customer that can no
  longer actually be kept.
DISCONFIRMING_OBSERVATION: >
  A combination discontinued after being promised on an open order line is removed from the order's display with
  no flag that the commitment can no longer be fulfilled.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Promise a combination on an open order, then discontinue that combination, and inspect how the existing order
  line is represented.
```

## G08-SALE_PRODUCT_MATRIX-Q014

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q014
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Attempting to add a discontinued combination through the grid on a new order is blocked identically to
  attempting to add it as a single manual line.
WHY_IT_MATTERS: >
  An inconsistency between the two entry paths would let a discontinued combination continue to be sold through
  whichever path happened not to enforce the block.
DISCONFIRMING_OBSERVATION: >
  A discontinued combination is blocked from single manual entry but remains selectable through the grid.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Discontinue a combination and attempt to add it both through the grid and through single manual entry,
  comparing the outcomes.
```

## G08-SALE_PRODUCT_MATRIX-Q015

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q015
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A discontinued combination that already has a quantity partially delivered retains its delivery history intact
  and correctly represents the un-deliverable remainder, rather than the discontinuation clearing or distorting
  what was already delivered.
WHY_IT_MATTERS: >
  Losing or distorting delivery history on discontinuation would misstate what the business has already actually
  provided to the customer.
DISCONFIRMING_OBSERVATION: >
  Discontinuing a combination with a partially delivered order line alters or removes the record of what
  quantity was already delivered.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Partially deliver a combination's order line, discontinue that combination, and inspect the order's delivery
  record afterward.
```

## G08-SALE_PRODUCT_MATRIX-Q016

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q016
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whoever manages the customer relationship for an order containing a newly discontinued, already-promised
  combination is notified of the specific line affected, rather than the discontinuation being discoverable only
  by someone happening to reopen that specific order.
WHY_IT_MATTERS: >
  Without active notification, a customer commitment that can no longer be kept may go unaddressed until the
  customer themselves discovers the failure.
DISCONFIRMING_OBSERVATION: >
  A combination discontinued while promised on an open order produces no notification to anyone associated with
  that order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Discontinue a combination that is promised on an open order and check whether any notification reaches the
  order's owner.
```

## G08-SALE_PRODUCT_MATRIX-Q017

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q017
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reopening the grid on an order where a combination has already been partially delivered does not allow that
  combination's ordered quantity to be reduced below the quantity already delivered.
WHY_IT_MATTERS: >
  Reducing a quantity below what has physically already left the business would understate a delivery that has
  already actually occurred.
DISCONFIRMING_OBSERVATION: >
  The grid allows a combination's ordered quantity to be reduced below the quantity already recorded as
  delivered for it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially deliver a combination on an order, reopen the grid, and attempt to reduce that combination's
  quantity below the delivered amount.
```

## G08-SALE_PRODUCT_MATRIX-Q018

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q018
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Adding a new combination through the grid to an order that already has other combinations partially delivered
  does not disturb the already-recorded delivery status of those untouched combinations.
WHY_IT_MATTERS: >
  A grid save that inadvertently resets or recalculates unrelated, already-delivered lines would corrupt a
  record of physical movement that has already actually happened.
DISCONFIRMING_OBSERVATION: >
  Adding a new combination through the grid to a partially delivered order changes the delivery status or
  quantity of a different, untouched combination on that same order.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Partially deliver one combination on an order, then add a new, unrelated combination through the grid, and
  check whether the delivered combination's status changed.
```

## G08-SALE_PRODUCT_MATRIX-Q019

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q019
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Using the grid to zero out a combination that has no delivery yet removes that line cleanly, while attempting
  the same action on a combination with an existing partial delivery instead reduces it only to the already-
  delivered quantity, with a clear indication that full removal was not possible.
WHY_IT_MATTERS: >
  Silently allowing full removal of a partially delivered line would erase the customer's rightful claim to
  receive the remainder, or misstate what has already shipped.
DISCONFIRMING_OBSERVATION: >
  Zeroing out a partially delivered combination through the grid removes the line entirely, with no
  representation of the quantity already delivered.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially deliver a combination, then use the grid to reduce its quantity to zero, and observe the outcome.
```

## G08-SALE_PRODUCT_MATRIX-Q020

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q020
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A stock or availability check that would block or warn on a manually entered line for an already-in-progress
  delivery process applies identically when the same combination and quantity are added through the grid to a
  partially delivered order.
WHY_IT_MATTERS: >
  A grid-specific exemption from checks that manual entry would enforce creates an inconsistent, exploitable gap
  in the same control.
DISCONFIRMING_OBSERVATION: >
  An availability check that blocks manual entry of an over-committed combination does not block the equivalent
  entry made through the grid on the same order.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a combination that would trigger an availability block on manual entry, then attempt the equivalent
  entry through the grid.
```

## G08-SALE_PRODUCT_MATRIX-Q021

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q021
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reopening the grid on an order where a combination has already been partially invoiced does not allow that
  combination's ordered quantity to be reduced below the quantity already invoiced.
WHY_IT_MATTERS: >
  Reducing the ordered quantity below what has already been billed would leave an invoiced quantity with no
  corresponding order line to justify it.
DISCONFIRMING_OBSERVATION: >
  The grid allows a combination's ordered quantity to be reduced below the quantity already invoiced for it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially invoice a combination on an order, reopen the grid, and attempt to reduce that combination's
  quantity below the invoiced amount.
```

## G08-SALE_PRODUCT_MATRIX-Q022

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q022
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where invoicing policy bills based on quantity delivered rather than quantity ordered, a change made through
  the grid to a combination's ordered quantity does not itself alter what has already been invoiced for the
  quantity actually delivered so far.
WHY_IT_MATTERS: >
  Conflating an ordered-quantity change with the already-invoiced delivered amount would misstate billed revenue
  that has nothing to do with the later order change.
DISCONFIRMING_OBSERVATION: >
  Changing a combination's ordered quantity through the grid alters the amount already invoiced for previously
  delivered quantity under a deliver-based invoicing policy.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Under deliver-based invoicing, partially deliver and invoice a combination, then change its ordered quantity
  through the grid, and check the already-invoiced amount.
```

## G08-SALE_PRODUCT_MATRIX-Q023

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q023
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Adding a new combination through the grid to an order already partially invoiced for other combinations does
  not alter the invoiced status or amount of those other, untouched combinations.
WHY_IT_MATTERS: >
  A grid save that recalculates unrelated already-invoiced lines would corrupt billing figures that already
  reflect a real financial transaction.
DISCONFIRMING_OBSERVATION: >
  Adding a new combination through the grid to a partially invoiced order changes the invoiced amount of a
  different, untouched combination on that order.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Partially invoice one combination on an order, then add a new, unrelated combination through the grid, and
  check whether the invoiced combination's figures changed.
```

## G08-SALE_PRODUCT_MATRIX-Q024

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q024
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A credit limit or customer-block control that would prevent further commitment on an over-limit account is
  still evaluated when the additional commitment comes from a grid session rather than a single manually entered
  line.
WHY_IT_MATTERS: >
  A control that only checks single-line entry gives an easy, unintended path around the same control through
  bulk grid entry.
DISCONFIRMING_OBSERVATION: >
  A customer already over their credit limit is still able to add further committed quantity through the grid
  with no block, although the identical single-line addition would be blocked.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Place a customer over their configured credit limit, then attempt to add further quantity both through the
  grid and through single manual entry, comparing the outcomes.
```

## G08-SALE_PRODUCT_MATRIX-Q025

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q025
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Lines created through the grid in a single session are represented on the customer-facing rendered document
  with the same level of individual detail as lines entered manually, not collapsed into one undifferentiated
  block that hides which specific combinations were actually ordered.
WHY_IT_MATTERS: >
  A collapsed block prevents the customer from verifying that the specific combinations, quantities, and prices
  they actually agreed to are what the document reflects.
DISCONFIRMING_OBSERVATION: >
  A rendered document represents several grid-created lines as a single summarized block with no per-combination
  detail visible.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create several lines through the grid, render the customer-facing document, and check whether each combination
  is individually represented.
```

## G08-SALE_PRODUCT_MATRIX-Q026

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q026
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The order in which grid-created combinations appear on the rendered document is stable and predictable across
  regenerations, not shuffled differently each time the same order is re-rendered.
WHY_IT_MATTERS: >
  An unstable line order makes it harder for the customer to compare successive versions of the same document
  line by line.
DISCONFIRMING_OBSERVATION: >
  Re-rendering the same order's document twice produces the grid-created lines in a different order each time.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Render the same order's document twice without changes and compare the ordering of grid-created lines.
```

## G08-SALE_PRODUCT_MATRIX-Q027

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q027
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A grid session that creates a very large number of lines renders on the customer-facing document without
  truncating or silently dropping any of the created lines, regardless of how the document is paginated.
WHY_IT_MATTERS: >
  A silently truncated document would misrepresent to the customer exactly what they are being asked to accept
  or have been billed for.
DISCONFIRMING_OBSERVATION: >
  A grid session creating more lines than fit on a single page results in a rendered document missing some of
  the created lines entirely.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create an unusually large number of lines through the grid and render the resulting document, verifying every
  line appears somewhere in the output.
```

## G08-SALE_PRODUCT_MATRIX-Q028

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q028
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A subtotal or grouping shown on the rendered document for a set of grid-created lines matches the sum the
  record itself holds for that same set, so the customer-facing summary is never a figure independently computed
  by the rendering step.
WHY_IT_MATTERS: >
  An independently computed summary that drifts from the record's own total creates two different answers to
  what the customer is actually being charged for that group.
DISCONFIRMING_OBSERVATION: >
  A subtotal shown for a group of grid-created lines on the rendered document differs from the sum of those same
  lines in the underlying record.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a group of lines through the grid, render the document, and compare its subtotal for that group against
  the record's own sum.
```

## G08-SALE_PRODUCT_MATRIX-Q029

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q029
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combination restricted to a defined set of approved customers is excluded from the grid for any customer
  outside that set, exactly as it would be excluded from manual entry for that customer.
WHY_IT_MATTERS: >
  An inconsistency between the two entry paths would let a restricted combination reach an unapproved customer
  through whichever path enforces the restriction less strictly.
DISCONFIRMING_OBSERVATION: >
  A combination restricted to approved customers is excluded from manual entry for an unapproved customer but
  remains selectable through the grid for that same customer.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Restrict a combination to approved customers, then attempt to add it for an unapproved customer through both
  manual entry and the grid.
```

## G08-SALE_PRODUCT_MATRIX-Q030

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q030
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A negotiated minimum order quantity specific to a customer for a given combination is enforced by the grid
  exactly as it would be by manual entry, not bypassed because the quantity was reached through bulk grid entry.
WHY_IT_MATTERS: >
  A minimum enforced on one entry path but not the other creates an easy, unintended way to place an order the
  negotiated terms were meant to prevent.
DISCONFIRMING_OBSERVATION: >
  An order quantity below a customer's negotiated minimum for a combination is accepted through the grid but
  would be rejected through manual entry.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure a customer-specific negotiated minimum order quantity for a combination and attempt an order below
  it through both the grid and manual entry.
```

## G08-SALE_PRODUCT_MATRIX-Q031

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q031
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a customer has a negotiated maximum quantity or allocation for a specific combination over a defined
  period, the grid draws down that allocation's remaining balance per combination, rather than treating the
  customer's other combinations as sharing an undifferentiated pool.
WHY_IT_MATTERS: >
  Treating a per-combination allocation as a shared pool could let the customer exceed the specific limit that
  was actually negotiated for that one combination.
DISCONFIRMING_OBSERVATION: >
  Ordering one combination through the grid reduces the remaining allocation balance of a different combination
  the customer has a separate allocation for.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure separate per-combination allocations for a customer, order one combination through the grid, and
  check whether the other combination's allocation balance changed.
```

## G08-SALE_PRODUCT_MATRIX-Q032

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q032
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Entering a combination through the grid after a customer's specific allocation for it is already exhausted
  falls back explicitly to whatever standard terms would apply outside that allocation, rather than silently
  continuing to apply the exhausted allocation's terms.
WHY_IT_MATTERS: >
  Continuing to apply exhausted preferential terms would extend a benefit beyond what was actually negotiated,
  at the business's cost.
DISCONFIRMING_OBSERVATION: >
  Ordering a combination through the grid after the customer's allocation for it is exhausted still applies the
  allocation's preferential terms.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Exhaust a customer's specific allocation for a combination, then order additional quantity of it through the
  grid, and check which terms apply.
```

## G08-SALE_PRODUCT_MATRIX-Q033

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q033
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An approval threshold based on order value is evaluated against the order's total after a bulk grid save, not
  against the total that existed immediately before the grid session began.
WHY_IT_MATTERS: >
  Evaluating against the pre-session total would let a grid session push an order well over an approval
  threshold without ever triggering the required approval.
DISCONFIRMING_OBSERVATION: >
  An order pushed over its approval threshold entirely by a grid session's bulk additions is not routed for the
  approval that threshold requires.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Bring an order to just below its approval threshold, then use the grid to add lines that push it over, and
  check whether approval is triggered.
```

## G08-SALE_PRODUCT_MATRIX-Q034

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q034
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order already approved while below a value threshold is returned to a pending-approval state if a
  subsequent grid session pushes its total over that threshold, rather than remaining approved on the strength
  of an approval that predates the added value.
WHY_IT_MATTERS: >
  An approval granted for a smaller commitment should not silently cover a materially larger one introduced
  afterward.
DISCONFIRMING_OBSERVATION: >
  An order already approved below the threshold remains in its approved state after a grid session adds enough
  value to cross the threshold.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Approve an order below the threshold, then use the grid to add lines crossing the threshold, and check the
  order's approval state.
```

## G08-SALE_PRODUCT_MATRIX-Q035

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q035
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An approval already granted for a specific set of combinations on an order is not treated as covering
  additional combinations introduced by a later grid session on the same order.
WHY_IT_MATTERS: >
  Treating a prior approval as automatically extending to new, unreviewed combinations defeats the purpose of
  requiring approval for what is actually being sold.
DISCONFIRMING_OBSERVATION: >
  A later grid session adds new combinations to an already-approved order without triggering a fresh approval
  requirement for those new combinations.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Approve an order for one set of combinations, then use the grid to add different combinations, and check
  whether fresh approval is required.
```

## G08-SALE_PRODUCT_MATRIX-Q036

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q036
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A mandatory line-level approval or flag required by business rule on a manually entered line, such as a below-
  cost price override, is equally required, not silently skipped, when the equivalent line is created via the
  grid.
WHY_IT_MATTERS: >
  A grid-specific gap in a line-level control creates an easy, unintended way to sell below cost without the
  review that manual entry would force.
DISCONFIRMING_OBSERVATION: >
  A below-cost price entered through the grid does not trigger the review flag that the identical price would
  trigger on a manually entered line.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure a below-cost review flag on manual entry, then enter an equivalent below-cost combination through
  the grid and check whether the flag triggers.
```

## G08-SALE_PRODUCT_MATRIX-Q037

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q037
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two users opening the grid for the same sales order at the same time do not have one user's save silently
  overwrite the other's unrelated changes without at least a conflict indication.
WHY_IT_MATTERS: >
  A silent overwrite discards a real change with no record that a conflict ever occurred.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous grid sessions on the same order result in one session's changes disappearing with no
  conflict indication to either user.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Open the grid for the same order in two sessions at nearly the same time, make different changes in each, and
  save both.
```

## G08-SALE_PRODUCT_MATRIX-Q038

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q038
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Bulk lines created in a single grid save on a sales order are individually recorded in that order's audit
  trail as distinct line-creation events, not collapsed into one undifferentiated batch entry that hides which
  specific combinations were added.
WHY_IT_MATTERS: >
  A collapsed batch entry prevents later reconstruction of exactly what was added to a customer's order and
  when.
DISCONFIRMING_OBSERVATION: >
  A grid save creating several lines produces one combined audit entry with no way to identify the individual
  combinations added.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create several lines in one grid save and inspect the order's audit trail for individual line-level detail.
```

## G08-SALE_PRODUCT_MATRIX-Q039

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q039
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A partial failure while committing a large grid of combinations to a sales order does not leave some
  combinations promised against limited availability while the rest of the intended lines silently never save.
WHY_IT_MATTERS: >
  A partial, silent failure would leave the business believing an order is smaller than the commitments it
  actually made against limited stock.
DISCONFIRMING_OBSERVATION: >
  A simulated partial failure during a large grid save leaves some combinations' availability committed while
  their corresponding order lines never actually appear on the order.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Simulate a partial failure while saving a large grid session and inspect whether committed availability
  matches the order lines that actually saved.
```

## G08-SALE_PRODUCT_MATRIX-Q040

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q040
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Performance degradation when saving an unusually large grid on a sales order does not result in a subset of
  the intended lines being saved while the system reports overall success.
WHY_IT_MATTERS: >
  A false success report on a partial save would leave staff and the customer both believing the full order was
  correctly captured when it was not.
DISCONFIRMING_OBSERVATION: >
  Saving an unusually large grid reports success while only some of the intended lines are actually present on
  the saved order.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Attempt to save an unusually large grid session and verify that every intended line is present when success is
  reported.
```

## G08-SALE_PRODUCT_MATRIX-Q041

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q041
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a sales order after partial delivery and partial invoicing of grid-created lines reverses each
  combination's outstanding commitment completely, leaving no partial residue of promised-but-uncancelled
  quantity for any combination.
WHY_IT_MATTERS: >
  A residual, uncancelled commitment left behind for even one combination continues to tie up availability the
  business believes has been freed.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order with partially fulfilled grid-created lines leaves one combination's outstanding promised
  quantity still committed after cancellation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially deliver and invoice several grid-created combinations, cancel the order, and verify every
  combination's outstanding commitment is released.
```

## G08-SALE_PRODUCT_MATRIX-Q042

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q042
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a single grid-created combination's line after its delivery has already been reflected in an
  invoice unwinds the invoice relationship in a defined order, rather than leaving an invoiced amount
  referencing a line that no longer exists.
WHY_IT_MATTERS: >
  An invoice left pointing at a deleted line creates unreconcilable billing history for that transaction.
DISCONFIRMING_OBSERVATION: >
  Cancelling a grid-created line that already has invoiced delivery removes the line while the existing invoice
  reference to it is left dangling or unexplained.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Invoice delivered quantity for one grid-created line, then cancel that specific line, and inspect how the
  existing invoice reference is handled.
```

## G08-SALE_PRODUCT_MATRIX-Q043

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q043
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Entering a negative quantity in the grid to represent a return of previously delivered goods, where the
  platform allows it, carries the same authorization and return-processing discipline that a manually entered
  return line would require.
WHY_IT_MATTERS: >
  A grid-specific gap in return authorization creates an easy, unintended way to process a return without the
  review manual entry would require.
DISCONFIRMING_OBSERVATION: >
  A negative quantity representing a return is accepted through the grid without the authorization or processing
  steps that an equivalent manual return line requires.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure return authorization requirements for manual entry, then attempt an equivalent negative-quantity
  return through the grid.
```

## G08-SALE_PRODUCT_MATRIX-Q044

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q044
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A combination's fully reversed order line, after cancellation and any associated credit note, is
  distinguishable in the order's history from a combination that was never ordered at all, so the fact that a
  commitment existed and was later reversed remains visible.
WHY_IT_MATTERS: >
  Erasing all trace of a reversed commitment loses information relevant to understanding the customer's actual
  order history and any pattern of cancellations.
DISCONFIRMING_OBSERVATION: >
  A fully cancelled and credited grid-created line leaves no trace in the order's history distinguishing it from
  a combination never ordered.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Fully cancel and credit a grid-created line, then inspect the order's history for any remaining trace of that
  reversed commitment.
```

## G08-SALE_PRODUCT_MATRIX-Q045

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q045
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A tenant's customer-specific combination eligibility, pricing, and allocation data are never visible or
  selectable within another tenant's grid session, even where combination names or structures happen to
  coincide.
WHY_IT_MATTERS: >
  Cross-tenant visibility of customer-specific commercial terms would breach the isolation the platform is
  expected to guarantee between unrelated businesses.
DISCONFIRMING_OBSERVATION: >
  A user in one tenant's grid session can select or view a combination's pricing or allocation data belonging to
  a different tenant.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user in one tenant, attempt to select or view a combination and its terms belonging to a different
  tenant's grid session.
```

## G08-SALE_PRODUCT_MATRIX-Q046

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q046
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A user's permission to sell against a specific company, branch, or warehouse scope is enforced per combination
  in the grid exactly as it is enforced in manual entry, when a combination is otherwise available across more
  than one such scope.
WHY_IT_MATTERS: >
  A grid-specific gap in scope enforcement would let a user commit stock or pricing from a scope they are not
  actually authorized to sell from.
DISCONFIRMING_OBSERVATION: >
  A user restricted to one company or branch scope is able to select, through the grid, a combination belonging
  to a scope they are not authorized for.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Restrict a user to one company or branch scope, then attempt to select a combination from a different scope
  through the grid.
```

## G08-SALE_PRODUCT_MATRIX-Q047

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q047
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Revoking a user's permission to use the grid feature takes effect for that user's next attempt to open it, and
  does not allow a session already open at the time of revocation to continue completing a save.
WHY_IT_MATTERS: >
  Allowing an already-open session to complete after revocation defeats the point of revoking access at that
  moment.
DISCONFIRMING_OBSERVATION: >
  A user's grid session, opened before their grid permission was revoked, is still able to complete a save after
  the revocation.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Open a grid session as a user, revoke that user's grid permission mid-session, and attempt to complete the
  save.
```

## G08-SALE_PRODUCT_MATRIX-Q048

```yaml
QID: G08-SALE_PRODUCT_MATRIX-Q048
MODULE: sale_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A multi-company sale, where the selling company and the company whose warehouse or branch scope actually holds
  the combination's availability differ, resolves availability and pricing from the scope actually authorized to
  sell it, not from whichever scope's data happens to be resolved first by the grid.
WHY_IT_MATTERS: >
  Resolving from the wrong scope could promise availability or apply pricing that the actual selling arrangement
  between the two companies does not support.
DISCONFIRMING_OBSERVATION: >
  A multi-company sale resolves a combination's availability or price from a company scope other than the one
  actually authorized for that sale.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a multi-company sale where selling and holding scopes differ, and check which scope the grid
  actually resolves availability and price from.
```

---
## GMVQ Internal QA Checklist

- [x] 48 distinct MVQ records; no padding — every record targets a distinct seam hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`, and no two records share one failure event.
- [x] Bridge Module Rule seam test applied to every question: removing the second capability and using the base order and that capability apart would make the question meaningless. No question restates base-module (`sale`) behavior with the bridge's name attached.
- [x] Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$DIR"/*.md | sort` was run before writing a single question, against both `G03_PRODUCT_MATRIX_GMVQ_MVQ_48_V1.00_DRAFT.md` (48 questions) and `G07_PURCHASE_PRODUCT_MATRIX_GMVQ_MVQ_48_V1.00_DRAFT.md` (48 questions). No question in this bank restates either sibling's ground with the nouns swapped: the master-data bank's ground is document-agnostic grid mechanics and was left untouched; the purchase-side bank's ground is vendor-catalogue/cost/commitment resolution and was left untouched. Every question here is specific to customer-facing exposure, promise-time availability, and the sales order's own partial-delivery/partial-invoice lifecycle.
- [x] Questions are behavioral and source-neutral; no vendor/product/standard name, technical identifier, or the module's own metadata name appears in question text.
- [x] Seam dimensions represented: ownership (Q001-Q002, Q005-Q008, Q020, Q022, Q025, Q029-Q031, Q036, Q038, Q045, Q048), timing (Q003-Q004, Q011), quantity and money (Q009, Q027-Q028, Q032), ordering (Q010, Q037), partiality (Q012, Q015, Q017-Q018, Q021, Q023), lifecycle mismatch (Q013-Q014, Q026, Q034), authority (Q016, Q024, Q033, Q035, Q043, Q046-Q047), reversal (Q019, Q041-Q042, Q044), error asymmetry (Q039-Q040).
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
