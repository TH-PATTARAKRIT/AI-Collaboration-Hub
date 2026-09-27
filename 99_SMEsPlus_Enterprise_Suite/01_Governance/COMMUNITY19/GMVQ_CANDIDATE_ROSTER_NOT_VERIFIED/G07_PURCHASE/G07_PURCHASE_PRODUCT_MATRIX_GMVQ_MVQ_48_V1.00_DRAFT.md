# SMEsPlus ENTERPRISE SUITE
## GMVQ — G07 PURCHASE / purchase_product_matrix Module Adversarial MVQ Bank

**Document ID:** GMVQ-G07-PURCHASE_PRODUCT_MATRIX-MVQ48-V1.00  
**Group:** G07 PURCHASE  
**Module Metadata:** `purchase_product_matrix`  
**Wave:** W2  
**Author Cell:** P16 (GMVQ Question Factory — Production Team P16)  
**Review Cell:** PENDING  
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN  
**actual_mvq_count:** 48  
**Standard bank reference:** 55 (shared, not reproduced here)  
**Research depth:** 55 + 48 = 103  
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded  

## Purpose

This bank authors the module-specific MVQ set for `purchase_product_matrix` — grid entry of attribute combinations onto a purchase document. It is a BRIDGE module per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question below fails only at the seam between the grid-entry capability and vendor-facing procurement, and would not make sense if either capability were used without the other. It deliberately does not restate the existing sales-side combination-matrix bank (G03_PRODUCT_MATRIX) with the nouns swapped; it targets ground that exists only on the buying side: which combinations a specific vendor can actually supply versus what is merely a valid combination in master data; vendor-specific pricing, minimum order quantity, and lead time that vary by combination; a vendor discontinuing a combination while an order is open; three-way match and receipt/billing state carried at the combination level; the effect of a bulk grid save on approval thresholds already granted or about to be breached; standing vendor price or quantity commitments drawn down per combination; and a vendor catalogue that does not recognise a combination the internal master data allows.

The question text is source-neutral and does not expose vendor model names, field names, methods, schema, XML IDs, API shapes, or implementation algorithms. `MODULE: purchase_product_matrix` appears only in the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 48 questions exist because they test 48 distinct material hypotheses.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
- Bridge module: every question targets the seam between grid-based combination entry and vendor-facing procurement only, per GMVQ_BRIDGE_MODULE_RULE_V1.00 §2. Removing either the grid or the purchase context makes the question meaningless — that is the test applied before inclusion.

## G07-PURCHASE_PRODUCT_MATRIX-Q001

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q001
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The grid must restrict the combinations it offers to ones the currently selected vendor
  is actually set up to supply, not the full purchasable combination set defined in master
  data.
WHY_IT_MATTERS: >
  Ordering a combination the vendor cannot actually supply produces a commitment that will
  fail at fulfilment, wasting the buying cycle and misleading whoever relies on the order
  as a supply plan.
DISCONFIRMING_OBSERVATION: >
  The grid lets a combination be entered and saved on the order even though the selected
  vendor has no linkage or agreement covering that combination.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Select a vendor known to supply only a subset of the product's combinations, then
  attempt grid entry across the full combination set.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q002

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q002
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A combination that is valid in master data generally, but is not linked to the currently
  selected vendor, must be rejected or excluded from grid entry for that vendor.
WHY_IT_MATTERS: >
  Allowing it exposes the order to a combination the current vendor was never contracted
  to sell, which either fails on receipt or silently substitutes an unagreed item.
DISCONFIRMING_OBSERVATION: >
  A combination with no supply linkage to the selected vendor is offered and accepted by
  the grid without any warning or block.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Use a combination linked to a different vendor than the one currently selected on the
  document, and attempt grid entry.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q003

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q003
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Switching the vendor on an in-progress grid session must re-evaluate which already-
  entered combinations remain valid for the new vendor.
WHY_IT_MATTERS: >
  Carrying combinations validated for one vendor onto a different vendor's order creates
  lines the new vendor never agreed to supply, without anyone reviewing the change.
DISCONFIRMING_OBSERVATION: >
  Changing the vendor after some combinations are already entered leaves those
  combinations on the order unchanged and unflagged, even where the new vendor cannot
  supply them.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Populate several combinations in the grid, then change the order's vendor before saving,
  and inspect whether the already-entered lines are re-checked.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q004

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q004
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A combination supplied by more than one vendor at different terms must resolve to the
  terms of the vendor actually selected on the document, not a default vendor.
WHY_IT_MATTERS: >
  Applying another vendor's price or terms to an order placed with a different vendor
  misstates what was actually agreed and what will be billed.
DISCONFIRMING_OBSERVATION: >
  A combination supplied by two vendors at different prices shows terms belonging to a
  vendor other than the one selected on the document.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Set up the same combination as available from two vendors with different price or lead
  time, select one vendor on the document, and enter that combination via the grid.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q005

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q005
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Each combination's cost must resolve from that specific combination's negotiated vendor
  price, where one exists, rather than falling back to a generic per-product cost that
  ignores combination-level negotiation.
WHY_IT_MATTERS: >
  Falling back to a generic per-product cost ignores negotiated terms specific to that
  combination, misstating the true procurement cost.
DISCONFIRMING_OBSERVATION: >
  A combination with its own negotiated vendor price is entered via the grid but priced at
  the generic product cost instead.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set a combination-specific negotiated price distinct from the product's general cost,
  then enter that combination through the grid.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q006

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q006
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A single grid session entering multiple combinations for the same vendor must evaluate
  each combination's minimum order quantity independently; meeting one combination's
  minimum must not be treated as satisfying a shortfall on a different combination in the
  same save.
WHY_IT_MATTERS: >
  Letting one combination's surplus quantity mask another's shortfall means an order can
  be placed below what the vendor actually requires per item, risking rejection or a
  surprise adjustment on the vendor's side.
DISCONFIRMING_OBSERVATION: >
  A grid session where one combination is well above its minimum and another is below its
  own minimum saves without flagging the combination that is short.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure two combinations from the same vendor with different minimum order quantities,
  enter one above and one below its own minimum in the same grid session, and save.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q007

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q007
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A vendor minimum order quantity that applies at the vendor level across multiple
  combinations, as distinct from one that applies separately to each combination, must be
  identified consistently by the grid, which must not silently pick whichever
  interpretation makes the current session's quantities pass.
WHY_IT_MATTERS: >
  Treating a per-vendor minimum as satisfied by combining unrelated combinations, when the
  vendor actually requires the minimum per combination, or the reverse, produces an order
  the vendor may refuse or fulfil differently than intended.
DISCONFIRMING_OBSERVATION: >
  A session that only meets the minimum when combination quantities are pooled together
  saves as compliant without indicating which interpretation of the minimum was applied.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a vendor minimum that is ambiguous as to whether it applies per combination or
  across the vendor relationship, and enter multiple combinations whose individual
  quantities are each below a plausible per-combination minimum.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q008

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q008
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A vendor price that is effective-dated from a specific date must apply to grid-created
  lines based on the order's own date, not the date the grid session happened to be
  opened.
WHY_IT_MATTERS: >
  Using a stale price because the grid session was started before a new price took effect
  misstates the cost the vendor will actually charge.
DISCONFIRMING_OBSERVATION: >
  A combination priced through the grid reflects the price in effect when the grid was
  opened rather than the price in effect on the order's actual date.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Open the grid before a scheduled vendor price change takes effect, leave the session
  open past that effective date, then complete entry and save.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q009

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q009
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Grid-created lines for combinations with different vendor lead times must each carry
  their own expected receipt date, not a single document-level date applied uniformly
  across all combinations.
WHY_IT_MATTERS: >
  Collapsing distinct vendor lead times into one document-level date makes some
  combinations appear late or early relative to when the vendor actually commits to
  deliver them.
DISCONFIRMING_OBSERVATION: >
  Two combinations with different vendor-quoted lead times show the same expected receipt
  date on the saved order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Configure two combinations from the same vendor with materially different lead times,
  enter both through the grid, and compare resulting expected receipt dates.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q010

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q010
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A combination's expected receipt date resolved through the grid must reflect the
  vendor's current lead time at the moment the order is actually confirmed, not a lead
  time cached from an earlier grid session on the same document that was opened but never
  completed.
WHY_IT_MATTERS: >
  Carrying forward a stale estimate from an abandoned session misrepresents how long the
  vendor will actually take once the order is finally confirmed.
DISCONFIRMING_OBSERVATION: >
  An order confirmed well after an earlier, abandoned grid session still shows the
  expected receipt date calculated during that earlier session, even though the vendor's
  lead time has since changed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Open the grid and let it resolve a lead time, abandon the session without confirming the
  order, wait for the vendor's lead time to change, then reopen the grid, complete entry,
  and confirm.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q011

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q011
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where lead time depends on the quantity ordered for a combination, a later change to
  that combination's quantity must re-resolve its expected receipt date, not leave the
  original date stale.
WHY_IT_MATTERS: >
  Leaving a stale lead time after a quantity change misrepresents how long the vendor will
  actually take to deliver the revised amount.
DISCONFIRMING_OBSERVATION: >
  Increasing a combination's quantity to a level the vendor quotes a longer lead time for
  leaves the original, shorter expected receipt date unchanged.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Configure a combination whose lead time depends on order quantity, enter an initial
  quantity through the grid, then increase it to a quantity with a longer quoted lead
  time.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q012

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q012
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combination the vendor discontinues after the order line was created must not silently
  disappear from the open order; it must be flagged as no longer fulfillable.
WHY_IT_MATTERS: >
  A silently vanishing order line hides a real supply problem, leaving whoever is tracking
  the order unaware that part of it will never arrive.
DISCONFIRMING_OBSERVATION: >
  A combination marked discontinued by the vendor no longer appears on an order that still
  has an open, unreceived quantity for it, with no flag explaining the removal.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an order with an open combination line, mark that combination as discontinued by
  the vendor, and reload the order.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q013

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q013
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Attempting to add a combination the vendor has discontinued through the grid on a new
  document must be blocked identically to attempting it as a single manual line.
WHY_IT_MATTERS: >
  Allowing the grid to place a fresh commitment for something the vendor no longer
  supplies creates an order guaranteed to fail at fulfilment.
DISCONFIRMING_OBSERVATION: >
  A combination the vendor has discontinued is accepted into a new order through the grid
  without the block that would stop it as a manual line.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Mark a combination discontinued for the selected vendor, then attempt to enter it both
  via the grid and via a manual line on a new document.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q014

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q014
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A discontinued combination that already has a quantity partially received must retain
  its received history and correctly represent the un-receivable remainder, rather than
  closing or hiding the line.
WHY_IT_MATTERS: >
  Hiding or closing the line loses the record of what was actually received and
  misrepresents the outstanding shortfall as resolved.
DISCONFIRMING_OBSERVATION: >
  A partially received, now-discontinued combination's line disappears from the order or
  shows as complete despite an unreceived remainder.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive part of a combination's ordered quantity, then mark that combination
  discontinued by the vendor, and review the order line.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q015

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q015
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Each combination created via the grid must be individually matchable against its own
  receipt and bill lines, not aggregated into a single matched total that hides which
  combination is over- or under-received.
WHY_IT_MATTERS: >
  An aggregated match total hides which specific combination is over- or under-received,
  defeating the purpose of matching at the line level.
DISCONFIRMING_OBSERVATION: >
  A discrepancy on one combination's receipt is absorbed into a combined match total that
  shows the order as fully matched.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Enter several combinations through the grid, receive a quantity different from ordered
  on just one, and review the match status per combination.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q016

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q016
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A receipt recorded against a grid-created line must reduce only that specific
  combination's outstanding quantity, not the outstanding quantity of a different
  combination on the same order.
WHY_IT_MATTERS: >
  Crediting the wrong combination's outstanding balance leaves one combination appearing
  fulfilled while another remains open despite having actually received the goods.
DISCONFIRMING_OBSERVATION: >
  Recording a receipt for one combination reduces the outstanding quantity shown against a
  different combination on the same order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an order with two grid-created combinations, receive against one specifically,
  and check the outstanding quantity on both.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q017

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q017
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A vendor bill referencing a combination must match against the grid-created order line
  for that same combination, not against whichever order line happens to share the same
  base product regardless of combination.
WHY_IT_MATTERS: >
  Matching by base product alone lets a bill for one combination be recorded against a
  different combination's order line, misstating what was actually billed for each.
DISCONFIRMING_OBSERVATION: >
  A vendor bill line for one combination matches against a different combination's order
  line that shares the same base product.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an order with two combinations of the same base product through the grid, then
  record a vendor bill referencing one specific combination.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q018

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q018
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A three-way match discrepancy on one grid-created combination must not block or distort
  the matching status of other, unrelated combinations from the same grid session.
WHY_IT_MATTERS: >
  Letting one combination's mismatch affect the match status of unrelated combinations
  obscures which specific commitment actually has a problem.
DISCONFIRMING_OBSERVATION: >
  A price or quantity discrepancy on one grid-created combination causes an unrelated
  combination's own match to show as unresolved.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create several combinations through the grid, introduce a mismatch on the receipt or
  bill of just one, and review the match status of the others.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q019

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q019
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reopening the grid on an order where some combinations already have a recorded receipt
  must not allow those combinations' ordered quantity to be reduced below the quantity
  already received.
WHY_IT_MATTERS: >
  Allowing the ordered quantity to drop below what has already arrived leaves a negative
  or nonsensical outstanding balance and misstates the vendor commitment.
DISCONFIRMING_OBSERVATION: >
  The grid saves a reduced quantity for a combination that is lower than the quantity
  already recorded as received for it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive part of a combination's ordered quantity, reopen the grid, and attempt to reduce
  that combination's quantity below the received amount.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q020

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q020
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reopening the grid on an order where some combinations are already reflected on a vendor
  bill must not allow those combinations' ordered quantity to be reduced below the
  quantity already billed.
WHY_IT_MATTERS: >
  Reducing the order below an amount already reflected on a vendor bill creates a mismatch
  between what was agreed and what was actually invoiced.
DISCONFIRMING_OBSERVATION: >
  The grid saves a reduced quantity for a combination that is lower than the quantity
  already reflected on a vendor bill for it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a vendor bill against part of a combination's ordered quantity, reopen the grid,
  and attempt to reduce that combination's quantity below the billed amount.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q021

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q021
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Adding a new combination through the grid to an order that is already partially received
  or billed must not disturb the already-recorded receipt or billing status of
  combinations untouched by that grid session.
WHY_IT_MATTERS: >
  An unrelated combination's settled receipt or billing status changing as a side effect
  of adding something new erodes trust in the order's recorded history.
DISCONFIRMING_OBSERVATION: >
  Adding a new combination through the grid to a partially received or billed order
  changes the receipt or billing status already recorded against an untouched combination.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Partially receive or bill one combination on an order, then use the grid to add a
  different, new combination, and re-check the first combination's status.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q022

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q022
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Using the grid to zero out a combination that has no receipt or billing yet must remove
  that line cleanly, while the same action on a combination with existing receipt or
  billing history must be prevented or require explicit handling.
WHY_IT_MATTERS: >
  Removing a line that already has real receipt or billing history erases evidence of an
  actual transaction that occurred.
DISCONFIRMING_OBSERVATION: >
  The grid removes a combination's line entirely even though it already has recorded
  receipt or billing history against it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Attempt to zero out, through the grid, one combination with no history and a separate
  combination that already has receipt or billing recorded.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q023

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q023
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An approval threshold based on order value must be evaluated against the order's total
  after a bulk grid save, not against the total that existed immediately before the grid
  was opened.
WHY_IT_MATTERS: >
  Checking against the pre-grid total lets a bulk addition push the order well past an
  intended spending control without triggering the review meant to catch it.
DISCONFIRMING_OBSERVATION: >
  An order's total after a grid save exceeds the approval threshold, yet the order remains
  in an approved or auto-approved state as if the threshold check used the earlier, lower
  total.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Approve or auto-approve an order below the threshold, then use the grid to add enough
  combinations to push the total over the threshold, and save.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q024

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q024
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An order already approved while below a threshold must be returned to a pending-approval
  state if a grid session pushes its total over that threshold, not remain approved on the
  strength of a total that no longer applies.
WHY_IT_MATTERS: >
  Letting an order stay approved on the strength of a total that no longer applies defeats
  the purpose of a value-based approval control.
DISCONFIRMING_OBSERVATION: >
  An order that was approved while below the threshold remains marked approved after a
  grid session raises its total above the threshold.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Approve an order below the threshold, reopen the grid, add combinations to exceed the
  threshold, save, and check the approval state.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q025

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q025
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A per-combination or per-category spending limit, where one exists, must be evaluated
  using the quantities and values the grid actually created, not the number of grid
  actions taken to create them.
WHY_IT_MATTERS: >
  Evaluating by how many grid actions were taken rather than what was actually committed
  lets a single large entry evade a limit meant to catch large commitments.
DISCONFIRMING_OBSERVATION: >
  A spending limit tied to a category is not triggered by one large grid-created
  combination because the grid recorded it as a single action rather than by its value.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure a per-category spending limit, enter a single combination through the grid
  whose value alone exceeds it, and save.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q026

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q026
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An approval already granted for a specific set of combinations must not be treated as
  covering additional combinations introduced by a later grid session on the same order.
WHY_IT_MATTERS: >
  Treating a later addition as already covered by an earlier approval lets new commitments
  go through without the review they require.
DISCONFIRMING_OBSERVATION: >
  Combinations added through a second grid session on an already-approved order are
  treated as approved without a fresh approval check.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Get an order approved for an initial set of combinations, then reopen the grid and add
  further combinations, and check whether a new approval step is triggered.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q027

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q027
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combination that is absent from the selected vendor's catalogue, even where it is
  accepted internally as valid, must produce an explicit exception at grid entry, not a
  line that is silently created without vendor recognition.
WHY_IT_MATTERS: >
  Silently creating a line the vendor has no record of leads to a rejected or misrouted
  order once it reaches the vendor.
DISCONFIRMING_OBSERVATION: >
  A combination not present in the selected vendor's catalogue is entered through the grid
  and saved without any exception or warning.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Use a combination that exists in internal master data but has no corresponding record in
  the selected vendor's catalogue, and attempt grid entry.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q028

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q028
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combination recognized differently between the internal master data and the vendor's
  catalogue must not be silently reconciled by the grid assuming one side is correct.
WHY_IT_MATTERS: >
  Picking a side without surfacing the conflict risks acting on stale or wrong information
  from whichever source was silently trusted.
DISCONFIRMING_OBSERVATION: >
  A combination defined differently between internal master data and the vendor catalogue
  is entered and saved with no indication that the two disagreed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Define a combination one way internally and a conflicting way in the vendor's catalogue
  data, then attempt grid entry for it.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q029

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q029
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling a purchase order after partial receipt and partial billing of grid-created
  lines must reverse each combination's outstanding commitment completely, leaving no
  residual vendor obligation attributable to combinations that were never received.
WHY_IT_MATTERS: >
  A residual vendor obligation left behind after cancellation is a hidden liability nobody
  is tracking.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order with several grid-created combinations, some partially received and
  billed, leaves an outstanding commitment on a combination that was never received.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially receive and bill some combinations on a grid-created order, leave others
  untouched, cancel the order, and review what remains open per combination.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q030

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q030
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling a single grid-created combination's line after its receipt has already been
  reflected in a vendor bill match must unwind that match in a defined order, rather than
  leaving the bill matched to a line that no longer exists.
WHY_IT_MATTERS: >
  Leaving a vendor bill matched to a line that no longer exists corrupts the accounting
  trail for that vendor relationship.
DISCONFIRMING_OBSERVATION: >
  Cancelling a single combination's line whose receipt was already reflected in a vendor
  bill match leaves the bill referencing a line that has been removed.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Match a receipt and vendor bill against one grid-created combination, then cancel just
  that combination's line.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q031

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q031
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Multiple combinations from the same grid session quoted by the vendor in different
  currencies must each retain their own vendor-quoted currency and rate through to receipt
  and bill matching, not be collapsed to the order header's currency for matching
  purposes.
WHY_IT_MATTERS: >
  Collapsing distinct vendor-quoted currencies to the header currency for matching
  purposes misstates what was actually agreed and can distort the recorded cost.
DISCONFIRMING_OBSERVATION: >
  A combination quoted by the vendor in a currency different from the order header is
  matched at receipt or billing using the header's currency and rate instead of its own.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure two combinations from the same vendor quoted in different currencies, enter
  both through the grid, and follow each through to receipt and bill matching.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q032

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q032
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Rounding applied per combination when converting a vendor's foreign-currency price must
  not accumulate a residual difference between the grid's displayed session total and the
  total actually recorded on the saved order.
WHY_IT_MATTERS: >
  A silent rounding gap between what the grid displayed and what was actually recorded
  undermines confidence in the session total as a check.
DISCONFIRMING_OBSERVATION: >
  The total shown in the grid during entry differs from the total recorded on the saved
  order once each combination's foreign-currency conversion is rounded.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Populate several combinations priced in a foreign currency through the grid, note the
  session total, save, and compare to the recorded order total.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q033

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q033
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a combination's tax basis is legitimately determined at a different time on the
  order than on the eventual vendor bill, the grid must not force both to share a single
  tax determination frozen at the moment of grid entry.
WHY_IT_MATTERS: >
  Forcing both moments to share one determination made at grid entry ignores a legitimate
  change in tax basis between placing the order and receiving the bill.
DISCONFIRMING_OBSERVATION: >
  A combination's tax is fixed at the value determined during grid entry even where the
  applicable basis has legitimately changed by the time the vendor bill arrives.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Enter a combination through the grid under one tax basis, change the condition that
  determines tax basis before the vendor bill is recorded, and check whether the bill re-
  determines tax.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q034

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q034
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two purchase orders drawing on the same limited standing vendor commitment through the
  grid at the same time must not each be allowed to independently confirm a quantity that,
  combined with the other, exceeds the commitment's actual remaining balance.
WHY_IT_MATTERS: >
  Letting two concurrent confirmations each check the balance independently allows the
  shared allocation to be oversubscribed, leaving one order committed to a quantity the
  vendor commitment can no longer honour.
DISCONFIRMING_OBSERVATION: >
  Two purchase orders, each drawing on the same standing vendor commitment through the
  grid at roughly the same time, both confirm successfully even though their combined
  quantity exceeds the commitment's remaining balance.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set up a standing vendor commitment with a limited remaining balance, and have two
  purchase orders each enter, through the grid, a quantity from that commitment that
  individually fits but combined exceeds it, confirming both at nearly the same time.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q035

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q035
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where the same combination could be drawn from two different standing vendor commitments
  with different remaining balances, the grid must resolve deterministically which
  commitment a newly entered quantity draws from, not leave it ambiguous which balance was
  decremented.
WHY_IT_MATTERS: >
  An unclear draw against one of two commitments means neither balance can be reconciled
  with confidence afterward.
DISCONFIRMING_OBSERVATION: >
  A combination covered by two standing vendor commitments with different remaining
  balances is entered through the grid, and it cannot be determined afterward which
  commitment's balance was reduced.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Set up the same combination under two standing vendor commitments with different
  remaining balances, and enter a quantity for it through the grid.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q036

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q036
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A vendor's rejection or renegotiation of a specific combination's terms after grid entry
  but before order confirmation must be capturable against that single combination,
  without requiring the entire grid session's lines to be discarded and re-entered.
WHY_IT_MATTERS: >
  Forcing a full re-entry over one combination's issue wastes the rest of a correctly
  entered session and invites new errors on re-entry.
DISCONFIRMING_OBSERVATION: >
  Addressing a vendor's rejection of one combination's terms requires discarding and re-
  entering every other combination from the same grid session.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Enter several combinations through the grid, then have the vendor reject or renegotiate
  the terms of just one before confirmation, and attempt to correct only that one.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q037

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q037
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A tenant's vendor-specific combination pricing, minimum order quantity, and lead time
  data must never be visible or selectable within another tenant's grid session, even
  where vendor names or combination attributes happen to coincide.
WHY_IT_MATTERS: >
  Cross-tenant visibility of negotiated vendor terms is a direct confidentiality and data-
  isolation failure between unrelated businesses.
DISCONFIRMING_OBSERVATION: >
  A combination's vendor-specific price, minimum order quantity, or lead time from one
  tenant appears or is selectable within a different tenant's grid session.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure the same or similarly attributed combination under two different tenants with
  different vendor terms, and open the grid under the second tenant.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q038

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q038
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A user permitted to enter quantities in the grid but not permitted to commit spend above
  a personal authorization limit must have that limit enforced across the whole grid
  session's combined value, not only against whichever single combination is being entered
  at a given moment.
WHY_IT_MATTERS: >
  Checking the limit one combination at a time lets a user assemble, through many
  individually small entries, a total commitment their own authorization was never meant
  to allow.
DISCONFIRMING_OBSERVATION: >
  A user whose personal authorization limit is below the value of a completed grid session
  is able to save that session because each individual combination entered was, on its
  own, within the limit.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user with a personal spend authorization limit, enter through the grid several
  combinations that are each individually within that limit but that together exceed it,
  and save.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q039

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q039
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Creating a brand-new combination inline during grid entry on a purchase document, where
  the platform allows it, must require both the same permission and the same vendor-
  linkage step that creating that combination through the ordinary procurement master-data
  path requires.
WHY_IT_MATTERS: >
  A shortcut that skips the vendor-linkage step lets a new combination reach an order
  without ever being properly connected to a supplying vendor.
DISCONFIRMING_OBSERVATION: >
  A brand-new combination is created inline during grid entry without the permission check
  or vendor-linkage step that the ordinary master-data creation path requires.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user without the permission normally required to create new combinations, attempt
  to create one inline during grid entry.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q040

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q040
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a combination is restricted to a defined set of approved vendors or purchasing
  categories, the grid must enforce that same restriction for whichever vendor is
  currently selected, not treat bulk entry as a separate path exempt from the approved-
  vendor list.
WHY_IT_MATTERS: >
  An approved-vendor list that only manual entry respects leaves the grid as an
  unmonitored route to commit a restricted combination to a vendor the business never
  approved for it.
DISCONFIRMING_OBSERVATION: >
  A combination restricted to an approved-vendor list is entered and saved through the
  grid for a vendor that list does not include.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Restrict a combination to a defined set of approved vendors, select a different vendor
  on the document, and attempt entry of that combination through the grid.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q041

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q041
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the grid allows a negative quantity to represent a return of previously received
  goods to the vendor, that action must carry the same authorization and vendor-return
  validation that initiating a return through the ordinary return process requires.
WHY_IT_MATTERS: >
  A return routed silently through bulk grid entry, bypassing the checks the ordinary
  return process applies, is an easy way to record an unauthorized credit against a
  vendor.
DISCONFIRMING_OBSERVATION: >
  A negative quantity entered through the grid to record a return to the vendor saves
  without the authorization step or return validation that the ordinary return process
  requires for the same action.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to record a return-to-vendor through the grid using a negative quantity, and
  compare the checks applied against initiating the same return through the ordinary
  return process.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q042

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q042
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A partial failure while committing a large grid of combinations to a purchase order must
  not leave some combinations reserved against a vendor's finite commitment while the
  order meant to consume that reservation fails to save.
WHY_IT_MATTERS: >
  A reservation left drawn down against a finite commitment while the order that was
  supposed to use it never actually saved wastes part of a limited vendor allowance for
  nothing.
DISCONFIRMING_OBSERVATION: >
  A large grid save partially fails, and a combination's quantity remains counted against
  a limited-quantity vendor commitment even though its order line did not save.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Populate a large grid drawing on a combination with a limited-quantity vendor
  commitment, force a partial save failure, and check the commitment's remaining balance
  against what actually saved.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q043

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q043
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A configuration limiting how many distinct combinations may appear on a single purchase
  order, where one exists, must count grid-created lines the same way it counts manually
  entered lines.
WHY_IT_MATTERS: >
  A limit that only counts manually entered lines lets the grid be used to exceed a
  control the business put in place for a reason.
DISCONFIRMING_OBSERVATION: >
  A configured limit on the number of distinct combinations per order is exceeded by a
  grid save without being blocked, even though the same limit blocks manual entry at that
  count.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a maximum combination count per order, populate the grid to exceed it, and
  separately attempt to exceed it via manual entry.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q044

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q044
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a specific combination on the order was driven by a stock or production
  replenishment need, replacing it through the grid with a different combination must not
  silently satisfy the original need without flagging that the fulfilling combination
  changed.
WHY_IT_MATTERS: >
  A silently substituted combination can leave the actual originating need unmet while
  every system record shows it as resolved.
DISCONFIRMING_OBSERVATION: >
  A combination that was driven by a specific replenishment need is replaced through the
  grid with a different combination, and the originating need shows as satisfied with no
  record of the substitution.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an order line for a combination driven by a specific replenishment need, then use
  the grid to replace that combination with a different one, and check whether the change
  is flagged.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q045

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q045
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A combination covered by a standing vendor price or quantity commitment must have the
  grid draw down that commitment's remaining balance per combination, not treat the
  commitment as a single pool shared indifferently across all combinations entered in the
  session.
WHY_IT_MATTERS: >
  Treating a commitment as one pool across combinations lets one combination's usage
  silently consume a balance intended for another.
DISCONFIRMING_OBSERVATION: >
  Entering one combination through the grid reduces the remaining balance recorded against
  a different combination's standing vendor commitment.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set up two combinations each with their own allocation within the same standing vendor
  commitment, enter a quantity for one through the grid, and check both remaining
  balances.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q046

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q046
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Entering a combination through the grid after its specific allocation within a standing
  vendor commitment is already exhausted must fall back explicitly to the vendor's
  standard terms, not silently continue applying the exhausted commitment's price.
WHY_IT_MATTERS: >
  Silently continuing to apply an exhausted commitment's price misstates what the vendor
  will actually charge once that allocation is used up.
DISCONFIRMING_OBSERVATION: >
  A combination entered through the grid after its standing commitment allocation is
  exhausted is still priced at the commitment's rate with no indication the allocation ran
  out.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Exhaust a combination's specific allocation within a standing vendor commitment, then
  enter additional quantity for that combination through the grid.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q047

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q047
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A vendor becoming ineligible to receive new orders during an open grid session, such as
  through suspension or deactivation, must halt further grid entry against that vendor,
  not allow the session to complete as though the vendor remained eligible.
WHY_IT_MATTERS: >
  Completing an order against a vendor no longer eligible to receive it produces a
  commitment the business has already decided it will not honour.
DISCONFIRMING_OBSERVATION: >
  A grid session that was opened against a vendor still eligible completes and saves
  normally even though that vendor was suspended or deactivated before the session was
  confirmed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Open the grid against an eligible vendor, suspend or deactivate that vendor while the
  session remains open, then complete entry and attempt to confirm.
```

## G07-PURCHASE_PRODUCT_MATRIX-Q048

```yaml
QID: G07-PURCHASE_PRODUCT_MATRIX-Q048
MODULE: purchase_product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reopening the grid on an order after the vendor's catalogue for one combination changed
  (price, minimum order quantity, or lead time revised) must clearly distinguish which
  already-created lines still reflect the old terms from which were re-resolved, rather
  than presenting all lines as current.
WHY_IT_MATTERS: >
  Presenting every line as current when some still reflect superseded terms hides which
  commitments need review after a vendor change.
DISCONFIRMING_OBSERVATION: >
  Reopening the grid after a combination's vendor terms changed shows all lines, old and
  re-resolved, with no distinction of which reflect the prior terms.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create combinations through the grid, change one combination's vendor price, minimum
  order quantity, or lead time, then reopen the grid and compare how lines are presented.
```
