# SMEsPlus ENTERPRISE SUITE
## GMVQ — G07 PURCHASE / purchase_stock Module Bridge MVQ Bank

**Document ID:** GMVQ-G07-PURCHASE_STOCK-MVQ48-V1.00
**Group:** G07 PURCHASE
**Module Metadata:** `purchase_stock`
**Wave:** W2
**Author Cell:** P15 (GMVQ Question Factory — Internal Production Team 15, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `purchase_stock`, the bridge where a confirmed
commercial order becomes an incoming physical movement and the three-way match (order, movement,
bill) is reconciled at the physical-document level. Per the GMVQ Bridge Module Rule V1.00, every
question here fails only at the seam between the order and the movement it generates: creation and
identity of the movement, unit conversion between the ordered unit and the stock-keeping unit,
location and company boundary at the point of physical receipt, movement lifecycle (validation,
correction, cancellation, reversal, return), timing between the order's dates and the movement's
own scheduled and actual dates, and the traceability that must survive edits on either side. The
base `purchase` bank already owns the order-line-level bookkeeping of ordered/received/billed
quantities, their tolerances, and price/currency/tax variance; this bank does not restate that
arithmetic and instead asks what happens to it at the point where a physical movement is actually
created, corrected, or reversed. Every question was checked against the sibling `purchase` bank's
authored hypotheses before being kept, and against the bridge removal test: if `purchase` and
`stock` were used entirely apart, the question would no longer make sense. Coverage spans business
capability, business rule, state transition, configuration dependency, role and permission,
exception path, cancellation, reversal, negative case, cross-module dependency, optional behaviour,
auditability, tenant/company boundary, concurrency and ordering, runtime reachability, configuration
reachability, and source/runtime contradiction potential.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material seam hypotheses; none was
  trimmed or stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table,
  field, method, XML ID, API path), and the module's own metadata name never appears outside the
  `MODULE:` field.
- Every question passed the bridge removal test and was cross-checked against the `purchase` base
  bank's authored HYPOTHESIS lines on disk at authoring time to avoid restating its invariants.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G07-PURCHASE_STOCK-Q001

```yaml
QID: G07-PURCHASE_STOCK-Q001
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Confirming an order creates exactly one linked incoming movement for the ordered quantity, never zero and never a silent duplicate.
WHY_IT_MATTERS: >
  A missing movement leaves the vendor commitment untracked in the warehouse; a duplicate movement overstates expected incoming stock and can trigger a false over-receipt exception later.
DISCONFIRMING_OBSERVATION: >
  Confirming a single order line produces either no linked movement at all, or two separate movements each carrying the full ordered quantity.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Confirm an order with at least one stockable line and inspect the count and quantity of movements linked to that line immediately afterward.
```

## G07-PURCHASE_STOCK-Q002

```yaml
QID: G07-PURCHASE_STOCK-Q002
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  The movement's expected quantity is the order line's quantity converted into the stock-keeping unit, not the order's display quantity carried over unconverted when the two units differ.
WHY_IT_MATTERS: >
  An unconverted quantity silently understates or overstates what the warehouse expects to receive whenever the buying unit and the stocking unit differ.
DISCONFIRMING_OBSERVATION: >
  An order line entered in a unit that is not the stock-keeping unit produces a linked movement whose expected quantity equals the raw entered number rather than its converted equivalent.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Order a component in a purchasing unit different from its stock-keeping unit and compare the order line's quantity against the linked movement's expected quantity.
```

## G07-PURCHASE_STOCK-Q003

```yaml
QID: G07-PURCHASE_STOCK-Q003
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A stock-side automatic replenishment trigger that generates a new order line for an existing vendor commitment is subject to the same approval threshold that a manually added line of the same value would require, rather than bypassing it because the trigger originated from the stock side.
WHY_IT_MATTERS: >
  An unreviewed value threshold that only applies to manually created lines would let automated replenishment commit money above the approval limit with no human checkpoint.
DISCONFIRMING_OBSERVATION: >
  A reordering-rule-generated line whose value exceeds the approval threshold is added to a confirmed order with no approval step, while a manually added line of the same value would have required one.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure an approval threshold, trigger an automatic replenishment that exceeds it, and compare the resulting approval requirement against a manually added line of the same value.
```

## G07-PURCHASE_STOCK-Q004

```yaml
QID: G07-PURCHASE_STOCK-Q004
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Receiving a quantity greater than what was ordered is either blocked outright or requires an explicit action to accept the excess — it is not silently recorded as if it matched the order.
WHY_IT_MATTERS: >
  Silently accepting an over-receipt hides a discrepancy that may indicate a vendor error, a miscount, or an unauthorized quantity change, with downstream billing consequences.
DISCONFIRMING_OBSERVATION: >
  A receipt for a quantity above the ordered amount validates with no distinguishing indicator, warning, or required confirmation compared to an exact-quantity receipt.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Attempt to receive more than the ordered quantity on a line and observe whether the system treats it identically to an exact-match receipt.
```

## G07-PURCHASE_STOCK-Q005

```yaml
QID: G07-PURCHASE_STOCK-Q005
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  An under-receipt within a configured tolerance is treated as line-complete for receiving purposes, while an under-receipt beyond that tolerance leaves the line visibly open on the receiving side, and the two are not treated identically.
WHY_IT_MATTERS: >
  Collapsing both cases into an identical receiving status would hide genuine shortages that fall outside the accepted tolerance band from whoever is following up on the physical delivery.
DISCONFIRMING_OBSERVATION: >
  Two receipts short of the ordered quantity by different margins — one within, one beyond a configured tolerance — are both reported as receiving-complete with no distinguishing status.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a receipt tolerance, then produce one under-receipt inside it and one beyond it on comparable lines, and compare the resulting receiving status.
```

## G07-PURCHASE_STOCK-Q006

```yaml
QID: G07-PURCHASE_STOCK-Q006
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Recording a receipt while the order is still in an unconfirmed state is either prevented or produces a visibly exceptional record, distinguishable from a normal post-confirmation receipt.
WHY_IT_MATTERS: >
  A receipt against an order nobody has committed to may record goods and cost against a commitment that could still change or be withdrawn.
DISCONFIRMING_OBSERVATION: >
  A receipt is recorded and validated against an order line while the order itself remains unconfirmed, with no different treatment from a receipt against a confirmed order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to record a receipt against an order line before confirming the order, and observe whether the action is blocked or flagged.
```

## G07-PURCHASE_STOCK-Q007

```yaml
QID: G07-PURCHASE_STOCK-Q007
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Increasing an order line's quantity after a partial receipt already exists does not alter the quantity already recorded on the earlier, already-validated movement.
WHY_IT_MATTERS: >
  Retroactively changing an already-validated physical record would misstate what was actually received on that date.
DISCONFIRMING_OBSERVATION: >
  After a partial receipt is validated, increasing the order line's ordered quantity changes the already-validated movement's recorded quantity rather than only affecting the still-outstanding remainder.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Partially receive an order line, then increase its ordered quantity, and inspect whether the already-validated movement's quantity changed.
```

## G07-PURCHASE_STOCK-Q008

```yaml
QID: G07-PURCHASE_STOCK-Q008
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A quantity physically received that was never present on any line of the order it accompanies (an unplanned extra item in the same delivery) is attached to that order only through an explicit, visible action, and is never silently merged into an existing line's received quantity.
WHY_IT_MATTERS: >
  Silently merging an unplanned extra item into an existing line's received quantity would misstate what that line's own vendor commitment was actually fulfilled by.
DISCONFIRMING_OBSERVATION: >
  An item delivered alongside an order but not present on any of its lines increases the received quantity of an existing, unrelated line with no explicit linking action recorded.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive a delivery that includes an item not present on any line of the order it accompanies, and inspect how that extra item is recorded relative to the order's existing lines.
```

## G07-PURCHASE_STOCK-Q009

```yaml
QID: G07-PURCHASE_STOCK-Q009
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Cancelling an order line that has an outstanding (not-yet-received) linked movement leaves that movement in an explicitly reconciled state rather than an unresolved, dangling expectation.
WHY_IT_MATTERS: >
  An unresolved expectation of incoming goods that no longer has a live order behind it can be received in error or distort inventory planning.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order line leaves its linked, not-yet-received movement still active and receivable with no indication that its originating order line was cancelled.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order, cancel a line before it is received, and inspect the state of the movement that was linked to that line.
```

## G07-PURCHASE_STOCK-Q010

```yaml
QID: G07-PURCHASE_STOCK-Q010
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A movement can be traced back to the specific order line that generated it even after that order has since been modified in unrelated ways.
WHY_IT_MATTERS: >
  Losing this link after an unrelated edit would break the ability to reconcile what was received against what was actually ordered.
DISCONFIRMING_OBSERVATION: >
  After an unrelated edit to the order (a different line, a note, a date on another line), a previously linked movement no longer shows which order line generated it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate a movement from an order line, edit an unrelated part of the same order, and check whether the movement's link to its originating line still resolves.
```

## G07-PURCHASE_STOCK-Q011

```yaml
QID: G07-PURCHASE_STOCK-Q011
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  When goods are received at a location other than the one specified on the order, that discrepancy is either blocked or recorded as an explicit exception rather than silently reassigning the receipt to the new location as if it were expected.
WHY_IT_MATTERS: >
  Silent reassignment would hide a fulfilment discrepancy that may indicate a shipping error or an unauthorized redirection of goods.
DISCONFIRMING_OBSERVATION: >
  A receipt processed at a location different from the order's specified destination validates with no warning, flag, or record distinguishing it from an on-location receipt.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Confirm an order specifying one destination location, then process the receipt at a different location and observe the resulting record.
```

## G07-PURCHASE_STOCK-Q012

```yaml
QID: G07-PURCHASE_STOCK-Q012
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  When goods are received under a company other than the one that placed the order, cross-company controls govern the resulting movement rather than the receipt silently reassigning cost and ownership across the company boundary.
WHY_IT_MATTERS: >
  An uncontrolled cross-company reassignment would move cost and stock ownership across a legal and accounting boundary without the safeguards that boundary requires.
DISCONFIRMING_OBSERVATION: >
  A receipt recorded under a company different from the ordering company completes without any cross-company control, approval, or distinguishing record.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Place an order under one company and attempt to record its receipt under a different company, observing what controls, if any, apply.
```

## G07-PURCHASE_STOCK-Q013

```yaml
QID: G07-PURCHASE_STOCK-Q013
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  The conversion factor between the order's purchasing unit and the stock-keeping unit is applied identically at every step of the seam — order, movement, and any correction — rather than two independently derived conversions producing different physical quantities for the same line.
WHY_IT_MATTERS: >
  Two different conversion results for the same physical goods would make it impossible to know how much was actually ordered versus actually received.
DISCONFIRMING_OBSERVATION: >
  The physical quantity implied by the order line and the physical quantity recorded on its linked movement disagree once both are converted to the same unit, with no explanatory correction recorded.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Use an order line and its linked movement expressed in different units, convert both to a common unit independently, and compare the results.
```

## G07-PURCHASE_STOCK-Q014

```yaml
QID: G07-PURCHASE_STOCK-Q014
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing a completed movement after a vendor bill has already been matched against it produces a visible variance on the bill match rather than leaving the bill matched against a quantity that no longer physically exists.
WHY_IT_MATTERS: >
  An unflagged mismatch between a paid-for quantity and an unreceived quantity is a direct financial exposure.
DISCONFIRMING_OBSERVATION: >
  Reversing an already-bill-matched movement leaves the bill's matched status and quantity unchanged, with no variance, warning, or required corrective action.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Match a vendor bill to a completed receipt, then reverse that receipt, and inspect whether the bill match reflects the reversal.
```

## G07-PURCHASE_STOCK-Q015

```yaml
QID: G07-PURCHASE_STOCK-Q015
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where an order line is fulfilled by several partial receipts on different dates, the costing basis for each specific quantity is drawn from that quantity's own receipt date, not uniformly from the date of the line's final receipt.
WHY_IT_MATTERS: >
  Using one date for all partial quantities would misstate the timing of cost recognition for units that actually arrived on different dates.
DISCONFIRMING_OBSERVATION: >
  Two quantities received on different dates against the same line both carry a costing date equal to the final receipt's date rather than each one's own.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive one order line in two partial shipments on two different dates and inspect the costing date recorded against each partial quantity.
```

## G07-PURCHASE_STOCK-Q016

```yaml
QID: G07-PURCHASE_STOCK-Q016
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  An outstanding movement that no longer has a corresponding open order behind it (because the order was cancelled, deleted, or otherwise closed elsewhere) is flagged as an exception rather than left reachable as an ordinary pending receipt.
WHY_IT_MATTERS: >
  A pending receipt with no live order behind it can be received in error, recording stock and cost for a commitment that no longer exists.
DISCONFIRMING_OBSERVATION: >
  A movement whose originating order was cancelled remains listed and receivable as an ordinary pending expectation with no distinguishing flag.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order, cancel it after the movement was created but before receipt, and check the state and visibility of the now-orphaned movement.
```

## G07-PURCHASE_STOCK-Q017

```yaml
QID: G07-PURCHASE_STOCK-Q017
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  The date used to judge whether a delivery is late is drawn consistently from the same one of either the order's promised date or the movement's own scheduled date across every report and screen that shows lateness — not one on one screen and the other elsewhere.
WHY_IT_MATTERS: >
  Two different definitions of late in use side by side would make on-time-delivery reporting internally inconsistent and untrustworthy.
DISCONFIRMING_OBSERVATION: >
  The order's promised date and the movement's scheduled date differ, and two different views of lateness for the same line use two different dates without acknowledging the difference.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Set an order's promised date and its linked movement's scheduled date to different values, then compare how lateness is reported in more than one place.
```

## G07-PURCHASE_STOCK-Q018

```yaml
QID: G07-PURCHASE_STOCK-Q018
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A return of previously received goods back to the vendor carries a traceable link back to the original receipt and order, rather than existing as an unrelated, freestanding movement.
WHY_IT_MATTERS: >
  A return with no link back to its origin cannot be reconciled against what was originally billed and paid for.
DISCONFIRMING_OBSERVATION: >
  A return-to-vendor movement for previously received goods carries no reference back to the original order or the original receiving movement.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive goods against an order, then create a return of some of that quantity, and inspect whether the return references the original receipt or order.
```

## G07-PURCHASE_STOCK-Q019

```yaml
QID: G07-PURCHASE_STOCK-Q019
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A discrepancy identified during receiving (short, over, or damaged) is recorded in a way that is traceable back to the specific order line and movement involved, not left as an informal note disconnected from either document.
WHY_IT_MATTERS: >
  A discrepancy that cannot be traced to its line cannot be pursued with the vendor or reflected accurately in the eventual bill match.
DISCONFIRMING_OBSERVATION: >
  A discrepancy noted during a receipt exists only as free text or is not linked to the specific order line and movement it occurred on.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a receipt with a deliberate quantity or condition discrepancy and inspect whether the resulting record links back to the specific line and movement.
```

## G07-PURCHASE_STOCK-Q020

```yaml
QID: G07-PURCHASE_STOCK-Q020
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  When one order line is fulfilled by more than one movement, the line's recorded received quantity is the sum of all of them, not just the most recently validated one.
WHY_IT_MATTERS: >
  Counting only the latest movement would understate how much has actually arrived whenever more than one shipment fulfils the same line.
DISCONFIRMING_OBSERVATION: >
  After two separate movements validate against the same order line, the line's received quantity equals only the second movement's quantity rather than the sum of both.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Fulfil a single order line through two separate validated movements and compare the line's received quantity against the sum of both.
```

## G07-PURCHASE_STOCK-Q021

```yaml
QID: G07-PURCHASE_STOCK-Q021
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where a vendor's delivery carries lot or serial identity for a tracked component, that identity captured at receipt is retained through to the matching stage rather than being dropped once the movement validates.
WHY_IT_MATTERS: >
  Losing tracked identity at the seam defeats traceability requirements that exist specifically to follow a tracked unit from vendor to eventual use.
DISCONFIRMING_OBSERVATION: >
  A lot or serial number captured during receiving is no longer retrievable from the order or its matching records once the movement is validated.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive a lot- or serial-tracked component against an order, capturing the tracked identity, and check whether it remains attached to the order's records afterward.
```

## G07-PURCHASE_STOCK-Q022

```yaml
QID: G07-PURCHASE_STOCK-Q022
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A movement generated for an order denominated in a foreign currency does not itself attempt to resolve a monetary value; whichever document is authoritative for cost governs it, and that authority is applied consistently rather than switching document by document.
WHY_IT_MATTERS: >
  An inconsistent authority for cost between the order, the movement, and the bill would produce unpredictable valuation results for the same goods.
DISCONFIRMING_OBSERVATION: >
  Two otherwise comparable foreign-currency order lines derive their movement's cost basis from two different authoritative documents (one from the order, one from the bill) with no configuration explaining the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place two comparable foreign-currency orders, receive and bill each, and compare which document's rate or amount the resulting movement valuation actually used.
```

## G07-PURCHASE_STOCK-Q023

```yaml
QID: G07-PURCHASE_STOCK-Q023
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Backordering the unreceived remainder of a partially received line preserves a traceable link to the same original order line, rather than creating a new expectation that appears unrelated to the original commitment.
WHY_IT_MATTERS: >
  A backorder disconnected from its origin would make it impossible to see that it is the continuation of an existing commitment rather than an unrelated new one.
DISCONFIRMING_OBSERVATION: >
  The backordered remainder of a partially received line appears as a movement with no reference back to the original order line it continues.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Partially receive an order line so that a backorder is generated for the remainder, and inspect whether that backorder references the original line.
```

## G07-PURCHASE_STOCK-Q024

```yaml
QID: G07-PURCHASE_STOCK-Q024
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  An unrelated action elsewhere in the system (merging orders, splitting orders, mass edits) does not silently change a movement's already-set expected quantity without a distinct, traceable action that explains the change.
WHY_IT_MATTERS: >
  An untraceable change to expected quantity would make it impossible to reconstruct why a warehouse is expecting a different amount than originally ordered.
DISCONFIRMING_OBSERVATION: >
  An order-level bulk action changes a linked movement's expected quantity with no separate record explaining that the change occurred or why.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform a bulk or merge action on orders that have existing linked movements, and inspect whether any resulting quantity change on those movements is separately recorded.
```

## G07-PURCHASE_STOCK-Q025

```yaml
QID: G07-PURCHASE_STOCK-Q025
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A movement forced directly to a completed state through an alternate or administrative path, bypassing the ordinary receiving screen, is still subject to the same three-way match evaluation as a movement completed through the ordinary receiving path.
WHY_IT_MATTERS: >
  An alternate completion path that escapes the same evaluation would let a bypass silently defeat the very discrepancy checks the three-way match exists to enforce.
DISCONFIRMING_OBSERVATION: >
  A movement completed through an alternate or administrative path produces no discrepancy flag for a quantity mismatch that the ordinary receiving path would have flagged for an equivalent case.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Complete a movement with a quantity mismatch through an alternate or administrative path rather than the ordinary receiving screen, and compare the resulting discrepancy handling to the ordinary path.
```

## G07-PURCHASE_STOCK-Q026

```yaml
QID: G07-PURCHASE_STOCK-Q026
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Authority to accept a quantity beyond the ordered amount (waiving the over-receipt tolerance) is restricted to a defined role, not implicitly available to whoever happens to be processing the receipt.
WHY_IT_MATTERS: >
  Unrestricted authority to accept excess quantities removes a control point meant to catch vendor errors or unauthorized deliveries.
DISCONFIRMING_OBSERVATION: >
  A user with no elevated permission is able to accept and validate an over-received quantity with no distinct authorization step from an ordinary exact-match receipt.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Attempt an over-receipt as a user without elevated permissions and observe whether an authorization step is required beyond the ordinary receiving action.
```

## G07-PURCHASE_STOCK-Q027

```yaml
QID: G07-PURCHASE_STOCK-Q027
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reopening a closed order to record a late receipt is a recorded action — who reopened it and when — rather than an unaudited silent state change.
WHY_IT_MATTERS: >
  An unaudited reopening of a closed commitment removes the ability to know who allowed a late delivery back into an otherwise settled order.
DISCONFIRMING_OBSERVATION: >
  A closed order is reopened to accept a late receipt with no audit entry recording who performed the reopening or when.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Close an order, then reopen it to record a late receipt, and check the audit trail for a record of the reopening action.
```

## G07-PURCHASE_STOCK-Q028

```yaml
QID: G07-PURCHASE_STOCK-Q028
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  In a scenario where the order and the movement disagree on which company or warehouse should record the transaction (such as a drop-ship arrangement), exactly one of the two is defined as authoritative for the stock record, and that choice is explicit rather than accidental.
WHY_IT_MATTERS: >
  An undefined authority between the order's and the movement's company or warehouse would leave stock ownership ambiguous in exactly the scenarios most likely to involve a third party.
DISCONFIRMING_OBSERVATION: >
  A drop-ship-style order produces a stock record whose company or warehouse ownership cannot be traced to a defined rule and differs unpredictably between otherwise similar cases.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure an order to be fulfilled through a drop-ship-style arrangement and inspect which company or warehouse the resulting stock record is attributed to.
```

## G07-PURCHASE_STOCK-Q029

```yaml
QID: G07-PURCHASE_STOCK-Q029
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A vendor bill matched against a movement quantity that is later corrected triggers a visible variance on the bill rather than leaving the bill's matched status based on a quantity that has since changed.
WHY_IT_MATTERS: >
  An unflagged variance after a correction hides the fact that what was billed no longer matches what was actually received.
DISCONFIRMING_OBSERVATION: >
  Correcting a movement's quantity after its bill match leaves the bill's match status and displayed matched quantity unchanged and unflagged.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Match a bill to a receipt, correct the receipt's quantity afterward, and inspect whether the bill match reflects a variance.
```

## G07-PURCHASE_STOCK-Q030

```yaml
QID: G07-PURCHASE_STOCK-Q030
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  When an order line is split into two scheduled deliveries after a movement already exists for it, the existing movement's link is preserved to whichever resulting line actually corresponds to the delivery already recorded.
WHY_IT_MATTERS: >
  A movement left pointing at the wrong resulting line after a split would misattribute an already-recorded physical delivery.
DISCONFIRMING_OBSERVATION: >
  Splitting an order line that already has a movement results in that movement's link pointing to neither resulting line correctly, or to both ambiguously.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a movement against an order line, split that line into two scheduled parts, and inspect which resulting line the movement remains linked to.
```

## G07-PURCHASE_STOCK-Q031

```yaml
QID: G07-PURCHASE_STOCK-Q031
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A movement manually created with no reference to any order line does not silently update the received quantity of an order line it was never actually linked to.
WHY_IT_MATTERS: >
  An unlinked movement altering an order line's figures would corrupt the reconciliation between what was ordered and what has been recorded as received.
DISCONFIRMING_OBSERVATION: >
  Creating a movement with no order reference changes the received quantity shown on an order line that the movement was never linked to.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a stock movement with no reference to any order and check whether any order line's received quantity changes as a result.
```

## G07-PURCHASE_STOCK-Q032

```yaml
QID: G07-PURCHASE_STOCK-Q032
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two receipts processed concurrently against the same order line do not result in the received quantity being double-counted.
WHY_IT_MATTERS: >
  Double-counting under concurrent processing would overstate what has arrived and could trigger an incorrect over-receipt exception or an incorrect line-closed status.
DISCONFIRMING_OBSERVATION: >
  Two receipts processed at effectively the same time against one order line result in a recorded received quantity greater than the sum of what each individually recorded.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger two near-simultaneous receipt validations against the same order line and compare the resulting received quantity against the expected sum.
```

## G07-PURCHASE_STOCK-Q033

```yaml
QID: G07-PURCHASE_STOCK-Q033
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  When the order's purchasing unit has no valid, configured conversion to the stock-keeping unit, the receipt is blocked or explicitly flagged rather than silently proceeding at an assumed one-to-one rate.
WHY_IT_MATTERS: >
  A silent one-to-one assumption where no real conversion exists would record a physically incorrect quantity with no indication that anything was wrong.
DISCONFIRMING_OBSERVATION: >
  A component ordered in a unit with no defined conversion to its stock-keeping unit still produces a receivable movement using an implicit one-to-one quantity, with no flag.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Order a component in a purchasing unit deliberately left without a defined conversion to its stock unit, and attempt to receive it.
```

## G07-PURCHASE_STOCK-Q034

```yaml
QID: G07-PURCHASE_STOCK-Q034
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The three-way match's evaluation of quantity agreement uses the movement's actual validated (physically confirmed) quantity once the movement has been processed, not the movement's original expected or demand quantity that predates that confirmation.
WHY_IT_MATTERS: >
  Matching against the pre-confirmation expected quantity instead of what was physically confirmed would let a bill pass the match against a figure that was never actually verified as received.
DISCONFIRMING_OBSERVATION: >
  The three-way match reports agreement using a movement's original expected quantity even after that movement has since been validated with a different, physically confirmed quantity.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a movement, validate it with a quantity different from its original expected quantity, and check which of the two figures the three-way match actually uses.
```

## G07-PURCHASE_STOCK-Q035

```yaml
QID: G07-PURCHASE_STOCK-Q035
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Correcting a quantity on an already-validated receipt requires a distinct corrective action, and the original validated quantity remains visible in the audit trail rather than being overwritten in place.
WHY_IT_MATTERS: >
  Overwriting a validated physical record in place would erase evidence of what was actually recorded at the time of receipt.
DISCONFIRMING_OBSERVATION: >
  Editing an already-validated receipt's quantity changes the original figure in place with no separate corrective record and no trace of the original value.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Validate a receipt, then correct its quantity, and inspect the audit trail for whether the original value is still visible.
```

## G07-PURCHASE_STOCK-Q036

```yaml
QID: G07-PURCHASE_STOCK-Q036
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Receiving a lot- or serial-tracked component with no tracked identity captured produces a blocked or explicitly incomplete movement, not one that passes through with only a bare quantity as if fully compliant.
WHY_IT_MATTERS: >
  Silently accepting an untracked receipt for a component that requires tracking defeats the traceability the tracking requirement exists to guarantee.
DISCONFIRMING_OBSERVATION: >
  A component configured to require lot or serial tracking validates a receipt with no tracked identity recorded and no distinguishing flag.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Attempt to receive a lot- or serial-tracking-required component while providing no tracked identity, and observe whether validation is blocked or flagged.
```

## G07-PURCHASE_STOCK-Q037

```yaml
QID: G07-PURCHASE_STOCK-Q037
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A movement whose scheduled date has passed with nothing received is distinguishable in reporting from one that was received on or before its scheduled date.
WHY_IT_MATTERS: >
  Treating overdue and on-time movements identically would hide genuinely late deliveries from anyone reviewing outstanding commitments.
DISCONFIRMING_OBSERVATION: >
  A movement overdue against its scheduled date with nothing received appears identically to an on-time, already-received movement in the same status view.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Let a movement's scheduled date pass with nothing received, and compare its status display against a movement that was received on time.
```

## G07-PURCHASE_STOCK-Q038

```yaml
QID: G07-PURCHASE_STOCK-Q038
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  The seam correctly generates a movement for a stockable order line while generating none for a service or non-stocked line, even when both lines appear on the same order.
WHY_IT_MATTERS: >
  Generating a spurious movement for a service line, or failing to generate one for a stockable line, would corrupt either the service billing flow or the physical receiving flow.
DISCONFIRMING_OBSERVATION: >
  An order containing both a stockable line and a service line produces a movement for the service line, or produces none for the stockable line.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order with one stockable line and one service line and inspect which lines produced a linked movement.
```

## G07-PURCHASE_STOCK-Q039

```yaml
QID: G07-PURCHASE_STOCK-Q039
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an already-validated movement (a receipt cancellation) does not leave the order line's received quantity unchanged as if the cancelled receipt still counted.
WHY_IT_MATTERS: >
  A cancelled receipt that still counts toward received would misstate the line's true outstanding quantity.
DISCONFIRMING_OBSERVATION: >
  Cancelling a validated movement leaves the order line's received quantity exactly as it was before the cancellation, with the quantity still counted as received.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Validate a receipt, then cancel that movement, and compare the order line's received quantity before and after the cancellation.
```

## G07-PURCHASE_STOCK-Q040

```yaml
QID: G07-PURCHASE_STOCK-Q040
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A vendor's own packing or delivery reference captured at receipt is retained on the movement or order pairing for later reconciliation rather than discarded once the receipt validates.
WHY_IT_MATTERS: >
  Losing the vendor's own reference removes a natural key needed to reconcile a delivery against the vendor's own shipping records later.
DISCONFIRMING_OBSERVATION: >
  A vendor delivery reference entered during receiving is no longer retrievable from the order or movement records once the receipt is validated.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a receipt with a vendor-supplied delivery reference and check whether that reference is still visible on the order or movement afterward.
```

## G07-PURCHASE_STOCK-Q041

```yaml
QID: G07-PURCHASE_STOCK-Q041
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A quantity received against an order line that has already been fully invoiced is flagged rather than passing through as an ordinary receipt, since it changes what fully received and billed already meant for that line.
WHY_IT_MATTERS: >
  An unflagged late receipt against an already-settled line hides a discrepancy between what was billed and what has now actually arrived.
DISCONFIRMING_OBSERVATION: >
  A receipt recorded against a line already fully invoiced validates identically to an ordinary receipt with no flag noting the line was already considered settled.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Fully invoice an order line, then record an additional receipt against that same line, and observe whether any flag distinguishes it.
```

## G07-PURCHASE_STOCK-Q042

```yaml
QID: G07-PURCHASE_STOCK-Q042
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A change to the vendor's lead time after the order is confirmed does not silently rewrite an already-scheduled movement's date without an explicit rescheduling action being taken.
WHY_IT_MATTERS: >
  An unexplained silent date change would make it impossible to tell whether a delivery date moved because of a deliberate reschedule or an unrelated configuration change.
DISCONFIRMING_OBSERVATION: >
  Changing a vendor's configured lead time after an order is confirmed changes the already-created movement's scheduled date with no rescheduling action recorded.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Confirm an order, then change the vendor's lead time setting afterward, and check whether the existing movement's scheduled date changed with no recorded action.
```

## G07-PURCHASE_STOCK-Q043

```yaml
QID: G07-PURCHASE_STOCK-Q043
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A return-to-vendor movement's quantity cannot exceed what was actually received under that order line without an explicit override, since exceeding it would mean returning goods that were never actually received.
WHY_IT_MATTERS: >
  Allowing a return larger than what was received would let a physically impossible transaction pass through unchallenged.
DISCONFIRMING_OBSERVATION: >
  A return-to-vendor movement for a quantity greater than what was ever received against the line validates with no override step or warning.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive a known quantity against a line, then attempt to return a larger quantity to the vendor against that same line.
```

## G07-PURCHASE_STOCK-Q044

```yaml
QID: G07-PURCHASE_STOCK-Q044
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When the order line's price changes after the goods were physically received but before the bill is matched, which price governs the eventual accounting follows a defined, consistent rule rather than being decided arbitrarily by whichever price happens to be current when matching runs.
WHY_IT_MATTERS: >
  An arbitrary, order-of-operations-dependent price resolution would make the same physical delivery cost different amounts depending purely on timing.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical deliveries, differing only in when the bill match was run relative to a price change, resolve to two different governing prices with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive goods, change the order line's price before matching the bill, and observe which price the resulting accounting actually used.
```

## G07-PURCHASE_STOCK-Q045

```yaml
QID: G07-PURCHASE_STOCK-Q045
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A movement generated from an order retains a stable, traceable link to that order across a change of the order's responsible buyer, so historical traceability is not scoped only to whoever currently owns the order.
WHY_IT_MATTERS: >
  Traceability that breaks on a reassignment would make it impossible to audit a delivery once responsibility for the order has moved to someone else.
DISCONFIRMING_OBSERVATION: >
  Reassigning an order's responsible buyer causes its already-linked movements to no longer resolve back to that order, or to show only the new buyer's history.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Generate a movement from an order, reassign the order's responsible buyer, and check whether the movement's link to the order still resolves fully.
```

## G07-PURCHASE_STOCK-Q046

```yaml
QID: G07-PURCHASE_STOCK-Q046
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a single physical delivery covers lines from more than one order to the same vendor, each order line's received quantity is attributed to its own order rather than merged into one undifferentiated total.
WHY_IT_MATTERS: >
  Merging quantities across orders would make it impossible to tell which order was actually fulfilled by how much of a combined delivery.
DISCONFIRMING_OBSERVATION: >
  Recording one combined delivery covering two separate orders to the same vendor results in the received quantity being attributed to only one of the two orders, or summed without attribution to either.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Place two separate orders with the same vendor and record one combined delivery covering lines from both, then inspect how the received quantity was attributed.
```

## G07-PURCHASE_STOCK-Q047

```yaml
QID: G07-PURCHASE_STOCK-Q047
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A physical destination location that is archived or deactivated after an order is confirmed but before its movement is received does not cause that movement to be silently redirected to an unrelated active location with no visible resolution.
WHY_IT_MATTERS: >
  A silently redirected receipt would place received goods somewhere other than where the order intended, with no record explaining why.
DISCONFIRMING_OBSERVATION: >
  Archiving the destination location on a confirmed, not-yet-received order's movement results in that movement pointing to a different, unrelated location with no flag or resolution step recorded.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Confirm an order, archive or deactivate its movement's destination location before receipt, and observe how the movement's destination is resolved.
```

## G07-PURCHASE_STOCK-Q048

```yaml
QID: G07-PURCHASE_STOCK-Q048
MODULE: purchase_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A movement that is cancelled and replaced by a corrected one (for example, undoing a miscounted receipt) is matched by the three-way match using only the corrected, currently valid movement — a bill cannot match against a movement quantity that has since been superseded and no longer represents the physical record.
WHY_IT_MATTERS: >
  Matching against a superseded movement would validate a bill against a physical record that has already been withdrawn as incorrect.
DISCONFIRMING_OBSERVATION: >
  A bill match reports agreement using a cancelled, superseded movement's quantity rather than the quantity on the movement that actually replaced it.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Cancel a validated movement due to a miscount, record a corrected replacement movement, and check which of the two the eventual bill match actually uses.
```

