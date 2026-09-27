# SMEsPlus ENTERPRISE SUITE
## GMVQ — G07 PURCHASE / purchase Module Adversarial MVQ Bank

**Document ID:** GMVQ-G07-PURCHASE-MVQ62-V1.00
**Group:** G07 PURCHASE
**Module Metadata:** `purchase`
**Wave:** W2
**Author Cell:** P14 (GMVQ Question Factory — Internal Production Team 14, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 62

## Purpose

`purchase` is the BASE module of G07 (9 modules, none previously had a bank). It owns the group's core
invariants — the order as a commitment that can change after confirmation, quantity ordered versus received
versus billed and the tolerance governing each, price on the order versus price on the bill, currency and tax
timing between order/receipt/bill, vendor terms and lead time, approval thresholds and segregation of duties,
duplicate detection, vendor-record lifecycle mid-order, multi-company/branch boundaries, audit trail of
post-confirmation changes, and the approval/execution/posting separation invariant — so that the eight bridge
banks in this group (`purchase_stock`, `purchase_mrp`, `purchase_product_matrix`, `purchase_repair`,
`purchase_edi_ubl_bis3`, `purchase_requisition`, `purchase_requisition_sale`, `purchase_requisition_stock`) do
not need to restate them and can instead ask what happens to these invariants at their own seam. Per the
Bridge Module Rule, the three-way-match seam between an order and a physical incoming movement is left to the
`purchase_stock` bridge; this bank treats receipt and billing at the level of order-line quantities and values,
not warehouse movement mechanics.

Question text is source-neutral: no vendor or product name, no technical identifier (model, table, field,
method, XML ID, API path), and no reference to how any specific implementation is built. Language is generic
procurement/business behaviour throughout — "order", "vendor", "bill", "receipt" and "line" are used as plain
business terms, never as technical identifiers.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 62 questions exist because they test 62 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, auditability, tenant/company boundary, and configuration reachability.
- Particular depth is placed on the approval/execution/posting separation invariant (Q060–Q062), on
  quantity/price/tolerance reconciliation across order, receipt and bill (Q011–Q024), and on approval-threshold
  integrity including split-order evasion and segregation of duties (Q043–Q048).
- `LAYER: BASE` marks a foundation/configuration question (vendor terms, pricing agreements, tolerance and
  threshold configuration, multi-company setup); `LAYER: PROCESS` marks a transactional/lifecycle question,
  since this module carries both layers.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a
  Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G07-PURCHASE-Q001

```yaml
QID: G07-PURCHASE-Q001
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Confirming an order changes its status to a binding commitment distinct from an unconfirmed draft or
  quotation state, and an unconfirmed record carries no such commitment.
WHY_IT_MATTERS: >
  If a draft is treated as a commitment, or a confirmed order can be edited exactly like a draft, the boundary
  vendors and approvers rely on to know what has actually been committed collapses.
DISCONFIRMING_OBSERVATION: >
  An order in an unconfirmed state produces the same downstream effects (a vendor being sent the order, or
  eligibility for receipt or billing) as a confirmed order.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create an order and leave it unconfirmed; attempt to receive goods or record a bill against it and observe
  whether the system permits or blocks this before confirmation.
```

## G07-PURCHASE-Q002

```yaml
QID: G07-PURCHASE-Q002
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Increasing the ordered quantity on a line after confirmation does not retroactively alter the receipt or
  billing history already recorded against the portion of that line processed before the change.
WHY_IT_MATTERS: >
  Retroactive rewriting of history that has already been acted on would make prior receipts and bills
  unreliable evidence of what actually happened.
DISCONFIRMING_OBSERVATION: >
  After increasing a confirmed line's quantity, a receipt or bill recorded before the change shows a different
  quantity or value than it did at the time it was recorded.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order, record a partial receipt and partial bill against one line, then increase that line's
  ordered quantity; compare the receipt and bill records before and after.
```

## G07-PURCHASE-Q003

```yaml
QID: G07-PURCHASE-Q003
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reducing the ordered quantity on a confirmed line below the quantity already received is either blocked or
  forces an explicit resolution, rather than silently truncating the recorded receipt history.
WHY_IT_MATTERS: >
  Silent truncation would leave physical stock already received with no corresponding order record, breaking
  the link between what was committed and what physically arrived.
DISCONFIRMING_OBSERVATION: >
  Reducing the ordered quantity below the received quantity succeeds without warning and the previously
  recorded receipt is reduced, hidden, or deleted to match.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order, receive the full quantity on one line, then attempt to reduce the ordered quantity below
  the received amount and observe the system's response.
```

## G07-PURCHASE-Q004

```yaml
QID: G07-PURCHASE-Q004
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Changing the price on a confirmed line changes only the price applied going forward and does not
  retroactively alter the recorded value of goods already received under the prior price.
WHY_IT_MATTERS: >
  Retroactively repricing history would misstate the valuation basis that was in effect at the actual moment
  of receipt.
DISCONFIRMING_OBSERVATION: >
  Changing a confirmed line's price alters the value already recorded for a receipt event that occurred before
  the price change.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Confirm an order, receive part of a line at its original price, change the line's price, and compare the
  receipt's recorded value before and after the price change.
```

## G07-PURCHASE-Q005

```yaml
QID: G07-PURCHASE-Q005
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Removing a line from a confirmed order that already has a partial receipt recorded against it does not
  delete or hide the existing receipt record.
WHY_IT_MATTERS: >
  Deleting a line that already has real-world consequences attached would erase evidence of goods that
  physically arrived.
DISCONFIRMING_OBSERVATION: >
  Removing a confirmed line with a partial receipt against it also removes the receipt record, or the receipt
  record becomes unreachable and unaccounted for.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order with a line, receive part of that line's quantity, then attempt to remove the line and
  observe what happens to the associated receipt record.
```

## G07-PURCHASE-Q006

```yaml
QID: G07-PURCHASE-Q006
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Adding a new line to an already-confirmed order that itself exceeds an approval threshold requires the added
  line, or the order as a whole, to pass through approval again, rather than inheriting the original approval
  automatically.
WHY_IT_MATTERS: >
  An approval given for one committed value should not silently extend to cover additional value added
  afterward.
DISCONFIRMING_OBSERVATION: >
  Adding a line whose value alone or combined with the existing order exceeds the approval threshold does not
  trigger any new approval step.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Confirm an order below the approval threshold, then add a line that pushes the total above the threshold,
  and observe whether approval is re-required.
```

## G07-PURCHASE-Q007

```yaml
QID: G07-PURCHASE-Q007
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Changing the delivery date on a confirmed order updates the outstanding commitment date without altering the
  record of dates that were already met or missed for portions already delivered.
WHY_IT_MATTERS: >
  Rewriting historical delivery dates would make lead-time and on-time performance measurement meaningless.
DISCONFIRMING_OBSERVATION: >
  Changing the committed delivery date on an order also changes the recorded date of a receipt event that
  already occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order, receive part of it on a given date, change the order's committed delivery date, and check
  whether the earlier receipt's recorded date changed.
```

## G07-PURCHASE-Q008

```yaml
QID: G07-PURCHASE-Q008
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A confirmed order reaches a closed state only when a defined completion condition is met (such as full
  receipt and full billing, or an explicit manual close), not merely because time has elapsed since
  confirmation.
WHY_IT_MATTERS: >
  An order that closes itself on a timer rather than on actual fulfilment would hide genuinely outstanding
  commitments from anyone reviewing open orders.
DISCONFIRMING_OBSERVATION: >
  An order with an outstanding unreceived or unbilled quantity moves to a closed state on its own, with no
  explicit action and no completion condition met.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Confirm an order, leave part of it unreceived and unbilled, and leave the record untouched for an extended
  period to see whether its status changes unattended.
```

## G07-PURCHASE-Q009

```yaml
QID: G07-PURCHASE-Q009
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where reopening a closed order is permitted, doing so is a distinguishable, recorded action, not
  indistinguishable in the record from the order never having closed.
WHY_IT_MATTERS: >
  An audit reviewing why a supposedly closed commitment became active again needs to see that it happened, and
  when, and by whom.
DISCONFIRMING_OBSERVATION: >
  A closed order becomes editable and receives new receipts or bills with no visible trace that it was
  reopened, by whom, or when.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close a fully processed order, then attempt to reopen it (or add further activity to it) and inspect whether
  the reopening is recorded.
```

## G07-PURCHASE-Q010

```yaml
QID: G07-PURCHASE-Q010
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order that has zero recorded receipt and zero recorded billing leaves no residual
  outstanding-commitment record anywhere in reporting.
WHY_IT_MATTERS: >
  A cancelled commitment that still appears as open would overstate what a vendor or buyer actually expects to
  happen.
DISCONFIRMING_OBSERVATION: >
  After cancelling an order with no receipt or billing activity, it still appears in a listing of outstanding
  or expected orders.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Confirm an order, take no further action, cancel it outright, and check any outstanding-order reporting for
  its continued presence.
```

## G07-PURCHASE-Q011

```yaml
QID: G07-PURCHASE-Q011
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The ordered, received, and billed quantities for a line are each tracked as independently observable values,
  not derived only from whichever event happened most recently.
WHY_IT_MATTERS: >
  If only the latest value survives, nobody can independently verify whether what was ordered, what arrived,
  and what was paid for actually agree.
DISCONFIRMING_OBSERVATION: >
  After a sequence of receipt and billing events, the system cannot show the ordered quantity, the received
  quantity, and the billed quantity as three separate figures for the same line.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Confirm a line, partially receive it, partially bill it, and check whether ordered, received, and billed
  quantities are all separately visible for that line.
```

## G07-PURCHASE-Q012

```yaml
QID: G07-PURCHASE-Q012
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A configurable tolerance governs how far a received quantity may exceed or fall short of the ordered quantity
  before the difference is flagged as an exception requiring attention.
WHY_IT_MATTERS: >
  Without a defined tolerance, every minor real-world variance either blocks processing, or every variance,
  however large, passes silently.
DISCONFIRMING_OBSERVATION: >
  Receiving a quantity far outside any reasonable variance from what was ordered proceeds with no flag,
  exception, or configurable threshold governing it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a receipt-quantity tolerance, then receive a quantity that falls within it and one that falls
  outside it, and compare the system's handling of each.
```

## G07-PURCHASE-Q013

```yaml
QID: G07-PURCHASE-Q013
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A configurable tolerance, which may be set independently of the receipt tolerance, governs how far a billed
  quantity may differ from the received quantity before it is flagged.
WHY_IT_MATTERS: >
  Billing and receiving variances arise from different real-world causes and a single shared tolerance may be
  inappropriate for both.
DISCONFIRMING_OBSERVATION: >
  The billing-quantity tolerance cannot be set to a different value than the receipt-quantity tolerance, or no
  such billing tolerance exists at all.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Look for a configuration setting governing acceptable variance between received and billed quantity, and
  test whether it can be set independently of receipt tolerance.
```

## G07-PURCHASE-Q014

```yaml
QID: G07-PURCHASE-Q014
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A line that has received less than the ordered quantity remains eligible for further receipt rather than
  being treated as complete.
WHY_IT_MATTERS: >
  Treating a partially received line as finished would hide a genuinely outstanding delivery obligation from
  the buyer and vendor.
DISCONFIRMING_OBSERVATION: >
  A line that has received less than its ordered quantity is marked complete, or no longer accepts a further
  receipt against the shortfall.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Confirm a line, receive less than the full ordered quantity, and attempt to record a further receipt for the
  remainder.
```

## G07-PURCHASE-Q015

```yaml
QID: G07-PURCHASE-Q015
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Receiving a quantity greater than ordered, even within tolerance, does not silently increase the recorded
  ordered quantity of the line.
WHY_IT_MATTERS: >
  If a received-quantity overage silently rewrites what was ordered, an over-delivery could be laundered into
  looking like it was always the plan, hiding a vendor performance issue.
DISCONFIRMING_OBSERVATION: >
  After receiving more than the ordered quantity, the line's recorded ordered quantity itself has changed to
  match what was received.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm a line, receive a quantity above the ordered amount but within tolerance, and check whether the
  original ordered quantity value changed.
```

## G07-PURCHASE-Q016

```yaml
QID: G07-PURCHASE-Q016
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Billing a quantity greater than the quantity actually received is either blocked or produces a visible
  exception, rather than being silently accepted and posted.
WHY_IT_MATTERS: >
  Paying for a quantity that never arrived, unnoticed, is a direct financial loss with no compensating control.
DISCONFIRMING_OBSERVATION: >
  A bill for a quantity greater than what was received for that line is recorded and posted with no exception,
  warning, or block of any kind.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Receive a known quantity on a line, then attempt to record a bill for a greater quantity and observe whether
  it is blocked, flagged, or silently accepted.
```

## G07-PURCHASE-Q017

```yaml
QID: G07-PURCHASE-Q017
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Multiple separate receipt events against the same line accumulate correctly toward the ordered quantity,
  rather than each event being evaluated only against the original order quantity in isolation.
WHY_IT_MATTERS: >
  If each receipt event is compared to the full order quantity rather than to what remains outstanding, a
  legitimate second delivery could be wrongly treated as a large overage.
DISCONFIRMING_OBSERVATION: >
  A second, legitimate partial receipt against a line already partially received is flagged as exceeding
  tolerance measured against the full original quantity rather than against what remained outstanding.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm a line, receive part of it in two or more separate events, and check that each event is evaluated
  against the remaining outstanding quantity, not the original total.
```

## G07-PURCHASE-Q018

```yaml
QID: G07-PURCHASE-Q018
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A line that is fully billed while only partially received is distinguishable, from the receipt perspective,
  from a line that is genuinely fully processed.
WHY_IT_MATTERS: >
  Conflating "fully billed" with "fully received" would let a paid-for shortfall disappear from anyone checking
  outstanding deliveries.
DISCONFIRMING_OBSERVATION: >
  A line billed in full while only partially received shows as fully complete in receipt-status reporting, with
  no indication of the shortfall.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Confirm a line, bill it in full while receiving only part of the quantity, and check its status in
  receipt-tracking versus billing-tracking views.
```

## G07-PURCHASE-Q019

```yaml
QID: G07-PURCHASE-Q019
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A difference between the price on the order and the price on the bill, beyond a defined tolerance, produces
  an exception requiring resolution rather than the bill's price being silently accepted.
WHY_IT_MATTERS: >
  Silently accepting whatever price a vendor bills removes the buyer's ability to enforce the price actually
  agreed at order time.
DISCONFIRMING_OBSERVATION: >
  A bill priced well outside any reasonable tolerance of the order price posts with no flag, warning, or hold
  of any kind.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Confirm an order at one price, then record a bill for the same line at a materially different price and
  observe whether an exception is raised.
```

## G07-PURCHASE-Q020

```yaml
QID: G07-PURCHASE-Q020
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  The party authorized to accept a price variance between order and bill is identifiable and their acceptance
  is recorded, whether that authority is the same as or different from whoever confirmed the original order.
WHY_IT_MATTERS: >
  Without a recorded acceptance, nobody can later show who decided the business was willing to pay more than
  originally agreed.
DISCONFIRMING_OBSERVATION: >
  A price variance is resolved and the bill proceeds to posting with no record of who accepted the variance or
  on what basis.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Trigger a price-variance exception on a bill, resolve it by accepting the new price, and check whether the
  acceptance and its author are recorded.
```

## G07-PURCHASE-Q021

```yaml
QID: G07-PURCHASE-Q021
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Accepting a price variance on a bill does not retroactively rewrite the price recorded on the original
  confirmed order.
WHY_IT_MATTERS: >
  The order price is the historical record of what was actually agreed at commitment time; overwriting it
  would erase evidence of the original commitment.
DISCONFIRMING_OBSERVATION: >
  After accepting a price variance on a bill, the original order line's recorded price has changed to match
  the bill.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order at one price, bill it at a different accepted price, and compare the order's recorded price
  before and after acceptance.
```

## G07-PURCHASE-Q022

```yaml
QID: G07-PURCHASE-Q022
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A change to a vendor's general pricing after an order is confirmed does not alter the price already committed
  on that confirmed line.
WHY_IT_MATTERS: >
  A committed order should reflect the price agreed at the moment of commitment, not whatever the vendor's
  price list says afterward.
DISCONFIRMING_OBSERVATION: >
  Updating the vendor's general pricing after confirmation changes the price shown or applied on an
  already-confirmed order line.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order at a given price, then change the vendor's general pricing for that item, and check the
  confirmed order line's price afterward.
```

## G07-PURCHASE-Q023

```yaml
QID: G07-PURCHASE-Q023
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Where more than one pricing agreement could apply to the same vendor and item, the system consistently
  applies the one in force at order-confirmation time to that order, not whichever happens to be in force
  later.
WHY_IT_MATTERS: >
  An inconsistent or time-shifting pricing basis would make it impossible to predict, or later reconstruct,
  which agreement actually governed a given commitment.
DISCONFIRMING_OBSERVATION: >
  Two orders confirmed under identical pricing-agreement conditions resolve to different prices, or the same
  order's applicable price changes depending on when it is looked up rather than when it was confirmed.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set up two overlapping pricing agreements for the same vendor and item with different validity, confirm an
  order within the overlap, and verify which price was applied and that it stays fixed.
```

## G07-PURCHASE-Q024

```yaml
QID: G07-PURCHASE-Q024
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where tax can be determined either at order-confirmation time or at billing time, the system records which
  point in time actually governed the tax applied to the posted transaction, rather than only showing two
  candidate calculations with no record of which was used.
WHY_IT_MATTERS: >
  An unrecorded tax basis leaves no way to justify the tax actually applied if it is later questioned.
DISCONFIRMING_OBSERVATION: >
  The posted transaction shows a tax amount with no way to determine whether it was calculated using
  order-time or bill-time conditions.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Confirm an order under one tax condition, change the condition, bill it, and check whether the record shows
  which tax basis was actually used.
```

## G07-PURCHASE-Q025

```yaml
QID: G07-PURCHASE-Q025
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  When matching a bill to a receipt is configured as mandatory, a bill recorded before a matching receipt
  exists is held in a state that does not post value to accounts.
WHY_IT_MATTERS: >
  Posting value for goods not yet confirmed as received defeats the purpose of requiring the match at all.
DISCONFIRMING_OBSERVATION: >
  With matching configured as mandatory, a bill recorded with no matching receipt posts its value to accounts
  anyway.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure mandatory matching between bill and receipt, record a bill for an order with no receipt yet
  recorded, and check whether it posts.
```

## G07-PURCHASE-Q026

```yaml
QID: G07-PURCHASE-Q026
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Recording a receipt with no corresponding order, or against a mismatched order reference, results in an
  identifiable exception state rather than an automatically fabricated order being created to absorb it.
WHY_IT_MATTERS: >
  An automatically fabricated commitment would create a paper trail suggesting something was approved that
  never actually was.
DISCONFIRMING_OBSERVATION: >
  Recording a receipt with no order reference results in a new order being generated automatically, with no
  exception raised and no approval step involved.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Attempt to record a receipt of goods with no order reference, or with a reference to a non-existent order,
  and observe how the system handles it.
```

## G07-PURCHASE-Q027

```yaml
QID: G07-PURCHASE-Q027
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A receipt recorded with no valid order behind it is visibly flagged as an exception, distinguishable from an
  ordinary receipt against a valid commitment.
WHY_IT_MATTERS: >
  An unflagged unauthorized receipt would be indistinguishable from ordinary business, hiding goods that
  arrived with no approved spend behind them.
DISCONFIRMING_OBSERVATION: >
  A receipt recorded without a valid order appears identical, in every report and record, to a receipt properly
  matched to an approved order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a receipt with no valid order behind it (where the system permits this at all) and compare its
  appearance in reporting to a normally matched receipt.
```

## G07-PURCHASE-Q028

```yaml
QID: G07-PURCHASE-Q028
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A bill matched against a receipt that itself turns out to correspond to goods with no valid order does not
  proceed silently to posting.
WHY_IT_MATTERS: >
  A chain of exceptions that each individually get waved through would let an entirely unauthorized spend
  reach the ledger as if it were ordinary.
DISCONFIRMING_OBSERVATION: >
  A bill matched to an unauthorized receipt posts without any exception surfacing the underlying missing order.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create a receipt with no valid order, then bill against that receipt and observe whether posting proceeds
  without an exception.
```

## G07-PURCHASE-Q029

```yaml
QID: G07-PURCHASE-Q029
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where a bill references an order that was cancelled before the goods on that bill were ever received, the
  mismatch between the bill and the cancelled commitment is surfaced rather than silently processed.
WHY_IT_MATTERS: >
  Paying against a commitment that was formally withdrawn, without anyone noticing, is a control failure that
  ordinary review would otherwise catch.
DISCONFIRMING_OBSERVATION: >
  A bill referencing a cancelled order, for goods never received under it, is recorded and posted with no
  warning that the order behind it was cancelled.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm and then cancel an order with no receipt against it, then attempt to record a bill referencing that
  order.
```

## G07-PURCHASE-Q030

```yaml
QID: G07-PURCHASE-Q030
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  When matching is configured as mandatory, an order that reaches fully billed status with zero recorded
  receipt is either blocked from billing or left with a persistent, visible unmatched flag.
WHY_IT_MATTERS: >
  A fully paid order with nothing ever received is exactly the pattern a matching control exists to prevent.
DISCONFIRMING_OBSERVATION: >
  With matching configured as mandatory, an order becomes fully billed with zero receipt recorded against it
  and no unmatched flag remains visible anywhere.
EXPECTED_SURFACE: S1,S2,S6,S7
PRECONDITIONS: >
  Configure mandatory matching, then attempt to bill an order in full with no receipt recorded, and check for a
  block or a persistent exception flag.
```

## G07-PURCHASE-Q031

```yaml
QID: G07-PURCHASE-Q031
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Manually closing an order while a bill against it is still outstanding does not extinguish, hide, or
  otherwise resolve that outstanding liability.
WHY_IT_MATTERS: >
  If closing an order also silently clears the liability owed, real debt to a vendor could disappear from view
  without ever being paid or written off deliberately.
DISCONFIRMING_OBSERVATION: >
  Closing an order with an outstanding, unpaid bill against it causes that bill's liability to disappear from
  outstanding-payables tracking.
EXPECTED_SURFACE: S1,S2,S5
PRECONDITIONS: >
  Confirm an order, record a bill against it that remains unpaid, close the order manually, and check whether
  the bill's liability still appears as outstanding.
```

## G07-PURCHASE-Q032

```yaml
QID: G07-PURCHASE-Q032
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order after partial receipt leaves the already-received portion and its accounting impact
  intact, voiding only the unreceived remainder.
WHY_IT_MATTERS: >
  Reversing a delivery that physically already happened, just because the rest of the order is cancelled, would
  misstate both stock and financial records.
DISCONFIRMING_OBSERVATION: >
  Cancelling a partially received order also reverses, deletes, or hides the value and record of the portion
  already received.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Confirm an order, receive part of one line, cancel the order, and check whether the received portion's record
  and value remain intact.
```

## G07-PURCHASE-Q033

```yaml
QID: G07-PURCHASE-Q033
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order after partial billing leaves the existing bill's liability intact and does not
  retroactively unbill or reverse it as a side effect of the cancellation itself.
WHY_IT_MATTERS: >
  A bill already issued represents a real liability that requires its own deliberate reversal process, not an
  automatic side effect of cancelling the order it came from.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order with an existing bill against it also reverses or deletes that bill with no separate
  action taken to do so.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Confirm an order, bill part of it, cancel the order, and check whether the existing bill remains in place
  unless separately reversed.
```

## G07-PURCHASE-Q034

```yaml
QID: G07-PURCHASE-Q034
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling only the unreceived remainder of a partially received order does not require first reversing the
  portion already received.
WHY_IT_MATTERS: >
  Forcing a full reversal of completed activity just to cancel what never happened would create unnecessary and
  risky rework of settled records.
DISCONFIRMING_OBSERVATION: >
  Attempting to cancel the unreceived remainder of a partially received line is blocked unless the
  already-received portion is reversed first.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Confirm a line, receive part of it, and attempt to cancel only the remaining unreceived quantity without
  touching the received portion.
```

## G07-PURCHASE-Q035

```yaml
QID: G07-PURCHASE-Q035
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An order cancelled outright, with no receipt or billing ever recorded against it, leaves no trace of itself
  in reporting on outstanding or expected commitments.
WHY_IT_MATTERS: >
  A cancelled commitment that still inflates outstanding-order figures would misrepresent genuine open exposure
  to vendors.
DISCONFIRMING_OBSERVATION: >
  An order cancelled with zero activity still appears in a report of currently outstanding or expected orders.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Confirm an order, take no receipt or billing action, cancel it, and check its presence in outstanding-order
  reporting.
```

## G07-PURCHASE-Q036

```yaml
QID: G07-PURCHASE-Q036
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where a bill already exists against a line that is later cancelled, the cancellation event by itself does not
  touch the ledger; reversing the bill's already-posted value requires a separate, explicit action.
WHY_IT_MATTERS: >
  A cancellation that silently reaches into posted accounting entries would let a non-accounting action alter
  the ledger without a distinct, reviewable accounting act.
DISCONFIRMING_OBSERVATION: >
  Cancelling a line with an existing posted bill against it changes posted ledger amounts with no separate
  reversing entry or action visible.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Confirm and bill a line so its value posts, then cancel the line and check whether the posted value changed
  without a distinct reversing action.
```

## G07-PURCHASE-Q037

```yaml
QID: G07-PURCHASE-Q037
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  For an order in a foreign currency, the exchange rate applied at order confirmation and the rate applied at
  billing are each recorded as distinct values, rather than one rate being assumed to apply to both events.
WHY_IT_MATTERS: >
  Conflating the two rates would hide the currency exposure that exists between the moment a commitment is made
  and the moment it is actually paid for.
DISCONFIRMING_OBSERVATION: >
  The rate recorded at order confirmation and the rate recorded at billing for the same order are shown as
  identical even though the two events occurred under genuinely different market rates.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Confirm a foreign-currency order at one rate, allow the rate to change, bill it, and check whether both rates
  are separately recorded.
```

## G07-PURCHASE-Q038

```yaml
QID: G07-PURCHASE-Q038
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A difference between the rate implied at order confirmation and the rate applied at billing produces a
  recognized gain or loss, rather than silently adjusting the value originally committed on the order.
WHY_IT_MATTERS: >
  An unrecognized currency difference would understate or overstate financial results without ever appearing
  as a distinct, explainable item.
DISCONFIRMING_OBSERVATION: >
  A currency rate difference between order and bill changes the recorded order value itself with no separate
  gain or loss appearing anywhere.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Confirm a foreign-currency order, change the rate before billing, bill it, and check for a recognized gain or
  loss versus a silently adjusted order value.
```

## G07-PURCHASE-Q039

```yaml
QID: G07-PURCHASE-Q039
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where a receipt itself carries a valuation using a rate in force at receipt time, that interim valuation is
  distinguishable from, and reconcilable against, the value ultimately billed.
WHY_IT_MATTERS: >
  Without a reconcilable interim value, nobody can verify whether the eventual billed value correctly accounts
  for timing differences in the exchange rate.
DISCONFIRMING_OBSERVATION: >
  The value recorded at receipt time and the value ultimately billed cannot both be seen and compared; one
  silently overwrites the other with no reconciling record.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Confirm a foreign-currency order, record a receipt with its own valuation, then bill it at a later rate, and
  check whether both values remain visible and reconcilable.
```

## G07-PURCHASE-Q040

```yaml
QID: G07-PURCHASE-Q040
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Changing a vendor's currency configuration after an order confirmed in the original currency does not
  retroactively convert the already-confirmed order into the new currency.
WHY_IT_MATTERS: >
  Retroactive currency conversion of a settled commitment would change the real value owed without any
  transaction actually happening.
DISCONFIRMING_OBSERVATION: >
  Changing the vendor's configured currency after order confirmation changes the currency or converted value
  shown on the already-confirmed order.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm an order in the vendor's original currency, change the vendor's configured currency afterward, and
  check whether the confirmed order's currency or value changed.
```

## G07-PURCHASE-Q041

```yaml
QID: G07-PURCHASE-Q041
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A vendor's payment terms and lead time are captured on the order at the time of confirmation and are not
  silently re-derived from the vendor's current master record if that record changes afterward.
WHY_IT_MATTERS: >
  An order should reflect the terms actually agreed at commitment time, not terms that happen to be current
  whenever someone later looks at the order.
DISCONFIRMING_OBSERVATION: >
  Changing the vendor's payment terms or lead time after an order is confirmed changes the terms shown on that
  already-confirmed order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order capturing the vendor's current terms and lead time, change those values on the vendor
  record, and check whether the confirmed order's terms changed.
```

## G07-PURCHASE-Q042

```yaml
QID: G07-PURCHASE-Q042
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Missing the committed delivery date does not, by itself, automatically change the order's status; any status
  change for a missed date follows an explicit rule or explicit action.
WHY_IT_MATTERS: >
  An order silently changing state because a date passed could mask a genuine vendor performance failure that
  deserves visibility, not automatic reclassification.
DISCONFIRMING_OBSERVATION: >
  An order's status changes automatically the moment its committed delivery date passes with nothing received,
  with no rule or action configured to cause that.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Confirm an order with a committed delivery date, let that date pass with nothing received, and observe
  whether and how its status changes.
```

## G07-PURCHASE-Q043

```yaml
QID: G07-PURCHASE-Q043
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  An approval threshold based on total order value applies to the order's full committed value, not to each
  line evaluated separately, so an order whose total exceeds the threshold requires approval even if no single
  line does.
WHY_IT_MATTERS: >
  Evaluating the threshold line by line would let a large order avoid approval entirely simply by having
  several lines each individually under the limit.
DISCONFIRMING_OBSERVATION: >
  An order whose total value exceeds the approval threshold confirms without approval because each individual
  line falls under the threshold.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure an approval threshold, create an order with several lines each below it but totalling above it, and
  attempt to confirm it.
```

## G07-PURCHASE-Q044

```yaml
QID: G07-PURCHASE-Q044
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A person without authority to approve above a given threshold cannot confirm an order whose value exceeds
  that threshold, regardless of which path or screen is used to attempt the confirmation.
WHY_IT_MATTERS: >
  An approval threshold that can be bypassed through an alternate path provides no real control at all.
DISCONFIRMING_OBSERVATION: >
  A person without sufficient approval authority succeeds in confirming an order above their threshold through
  some path other than the primary approval action.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Assign a limited approval threshold to a test user, attempt to confirm an order above that threshold as that
  user through every available path, and check whether any path succeeds.
```

## G07-PURCHASE-Q045

```yaml
QID: G07-PURCHASE-Q045
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a single procurement need is deliberately split into multiple smaller orders each falling under an
  approval threshold, the pattern is detectable, and the applicable control treats the combined need as
  requiring the higher-level approval it would have needed as one order.
WHY_IT_MATTERS: >
  If splitting an order defeats the threshold entirely, the approval control provides no real limit on spend,
  only on how orders happen to be structured.
DISCONFIRMING_OBSERVATION: >
  Multiple orders to the same vendor, for the same need, each kept just under the approval threshold, confirm
  with no control detecting or flagging the combined value.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Configure an approval threshold, raise several smaller orders to the same vendor for related items each under
  the threshold, and check whether any control surfaces the pattern.
```

## G07-PURCHASE-Q046

```yaml
QID: G07-PURCHASE-Q046
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Increasing a confirmed order's value, through added lines or changed quantity or price, past an approval
  threshold triggers re-evaluation of approval for the increased value, rather than the modification bypassing
  approval because the order was already confirmed once.
WHY_IT_MATTERS: >
  A one-time approval that never gets re-checked would let an order be confirmed small and then expanded freely
  with no further oversight.
DISCONFIRMING_OBSERVATION: >
  A confirmed order's value is increased past the approval threshold through a later modification and no new
  approval step is triggered.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Confirm an order below the approval threshold, then modify it (quantity, price, or new lines) to exceed the
  threshold, and check whether approval is re-required.
```

## G07-PURCHASE-Q047

```yaml
QID: G07-PURCHASE-Q047
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The record of who approved an order, at what value, and when, persists unchanged regardless of later
  modifications made to that order.
WHY_IT_MATTERS: >
  Losing or rewriting the original approval record would make it impossible to show what was actually approved
  versus what the order later became.
DISCONFIRMING_OBSERVATION: >
  Modifying a confirmed order changes or removes the record of its original approval, approver, or the value at
  which it was approved.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order with a recorded approval, modify the order afterward, and check whether the original
  approval record remains intact and unchanged.
```

## G07-PURCHASE-Q048

```yaml
QID: G07-PURCHASE-Q048
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where segregation-of-duties is configured for order approval, a person cannot approve an order they
  themselves raised, regardless of what other role or permission they separately hold.
WHY_IT_MATTERS: >
  Letting the requester also approve their own request removes the independent check the separation is meant
  to provide.
DISCONFIRMING_OBSERVATION: >
  A person who raised an order is able to approve that same order themselves, even with segregation-of-duties
  configured to prevent it.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Configure segregation-of-duties for approval, raise an order as a given user who also holds approval
  authority, and attempt to have that same user approve it.
```

## G07-PURCHASE-Q049

```yaml
QID: G07-PURCHASE-Q049
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Two orders for the same vendor, items, and quantities placed close together in time are not automatically
  merged or silently discarded, since they may represent a deliberate, legitimate repeat need.
WHY_IT_MATTERS: >
  Automatically collapsing similar-looking orders could silently cancel a genuine second need without anyone
  deciding to do so.
DISCONFIRMING_OBSERVATION: >
  Creating a second order closely matching an existing one for the same vendor and items results in it being
  silently merged into or replaced by the first, with no explicit action taken.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create an order, then create a second one shortly after for the same vendor, items, and quantities, and
  observe whether both persist independently.
```

## G07-PURCHASE-Q050

```yaml
QID: G07-PURCHASE-Q050
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A vendor bill that duplicates one already recorded against the same order and receipt is either blocked from
  being recorded again or is surfaced as a likely duplicate before it can post.
WHY_IT_MATTERS: >
  An unflagged duplicate bill leads directly to paying twice for the same goods.
DISCONFIRMING_OBSERVATION: >
  Recording a second bill with the same vendor, order, receipt, and amount as an existing bill proceeds to
  posting with no duplicate warning of any kind.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record a bill against an order and receipt, then attempt to record a second bill with matching vendor, order,
  receipt, and amount details.
```

## G07-PURCHASE-Q051

```yaml
QID: G07-PURCHASE-Q051
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If a duplicate bill is posted despite the available safeguards, the resulting doubled liability is visible in
  outstanding-payables reporting rather than being absorbed invisibly, so the error remains discoverable and
  correctable.
WHY_IT_MATTERS: >
  A doubled liability that never surfaces anywhere would allow an actual double payment to occur with nothing
  in the system pointing to the error.
DISCONFIRMING_OBSERVATION: >
  Two duplicate bills are both posted and the resulting doubled amount does not appear as an anomaly anywhere in
  outstanding-payables or vendor-balance reporting.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Force two duplicate bills to post against the same order and receipt (bypassing or overriding any warning),
  then inspect vendor-balance and payables reporting for visibility of the duplication.
```

## G07-PURCHASE-Q052

```yaml
QID: G07-PURCHASE-Q052
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A duplicate order raised independently by two different people for the same underlying need is only
  preventable through visible order data at entry time; no hidden mechanism silently resolves it on their
  behalf without their awareness.
WHY_IT_MATTERS: >
  A silent resolution mechanism that neither requester is aware of could leave one of them believing their need
  was addressed when it was not.
DISCONFIRMING_OBSERVATION: >
  Two different people each raise an order for the same need and one order is silently altered or removed
  without either person taking that action or being informed.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Have two different users independently raise similar orders for the same vendor and need, and check whether
  either order changes without an explicit, attributable action by a user.
```

## G07-PURCHASE-Q053

```yaml
QID: G07-PURCHASE-Q053
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Archiving a vendor record does not remove, hide, or block already-confirmed orders against that vendor from
  continuing through receipt and billing.
WHY_IT_MATTERS: >
  Losing access to a legitimately outstanding commitment just because the vendor record was archived would
  strand real, unfulfilled business.
DISCONFIRMING_OBSERVATION: >
  Archiving a vendor causes an already-confirmed order against it to disappear from view, or blocks further
  receipt or billing against that order.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Confirm an order against a vendor, archive the vendor record, and attempt to continue receiving and billing
  against the existing order.
```

## G07-PURCHASE-Q054

```yaml
QID: G07-PURCHASE-Q054
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Merging one vendor record into another while an order is still active preserves the link between the existing
  confirmed order, its receipts and bills, and an identifiable vendor identity, without breaking traceability to
  who the original commitment was actually made with.
WHY_IT_MATTERS: >
  Losing traceability to the original counterparty on a merge would make it impossible to later verify who a
  historical commitment was really made with.
DISCONFIRMING_OBSERVATION: >
  After merging the vendor on an active order into another vendor record, the order's receipt and billing
  history can no longer be traced to a coherent vendor identity, or the original counterparty becomes
  unidentifiable.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order against a vendor, partially process it, merge that vendor record into another, and check
  whether the order's history remains traceable.
```

## G07-PURCHASE-Q055

```yaml
QID: G07-PURCHASE-Q055
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Whether a vendor record archived mid-order still permits receiving and billing the remaining outstanding
  quantity, or explicitly blocks it, is a defined and consistent behaviour, not something that differs by which
  screen or action is used.
WHY_IT_MATTERS: >
  Inconsistent behaviour depending on the path taken would make the actual rule unpredictable to whoever is
  trying to close out the commitment.
DISCONFIRMING_OBSERVATION: >
  Whether further receipt or billing is possible against an order for an archived vendor differs depending on
  which screen, path, or action is used to attempt it.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Confirm an order against a vendor, archive the vendor mid-order, and attempt to receive and bill the remaining
  quantity through every available path.
```

## G07-PURCHASE-Q056

```yaml
QID: G07-PURCHASE-Q056
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  The same vendor can hold independent open orders under two different companies or branches, with one
  company's or branch's order activity neither visible nor editable from the other's scope.
WHY_IT_MATTERS: >
  Cross-company visibility or editability of another entity's commitments would breach the separation each
  company or branch relies on for its own accountability.
DISCONFIRMING_OBSERVATION: >
  An order raised for a vendor under one company or branch is visible or editable by a user scoped only to a
  different company or branch sharing that same vendor.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Confirm orders for the same vendor under two different companies or branches, and check each company's or
  branch's user for visibility or edit access to the other's order.
```

## G07-PURCHASE-Q057

```yaml
QID: G07-PURCHASE-Q057
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  An approval threshold configured for one company or branch does not apply to, or get inherited by, an order
  raised under a different company or branch, even when both share the same vendor.
WHY_IT_MATTERS: >
  A threshold leaking across company or branch boundaries would let one entity's spend controls be silently
  governed by rules set for a different entity.
DISCONFIRMING_OBSERVATION: >
  An order confirmed under one company or branch is subject to an approval threshold value configured for a
  different company or branch.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Configure different approval thresholds for two companies or branches, confirm an order for the shared vendor
  under each, and check which threshold applied in each case.
```

## G07-PURCHASE-Q058

```yaml
QID: G07-PURCHASE-Q058
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A change to price or quantity on a confirmed order produces a visible record of the prior value, the new
  value, who made the change, and when it was made.
WHY_IT_MATTERS: >
  Without this record, nobody reviewing a confirmed order later can tell it was ever changed from what was
  originally approved.
DISCONFIRMING_OBSERVATION: >
  A price or quantity change on a confirmed order leaves no visible record of the prior value, the change's
  author, or its timing.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Confirm an order, change the price or quantity on a line, and check whether the prior value, new value,
  author, and timestamp are all recorded and visible.
```

## G07-PURCHASE-Q059

```yaml
QID: G07-PURCHASE-Q059
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  The audit record of a change made to a confirmed order is not itself editable or deletable through the
  normal order-modification actions available to an ordinary user.
WHY_IT_MATTERS: >
  An audit trail that can be edited by the same actions that created the change it is meant to record provides
  no real assurance at all.
DISCONFIRMING_OBSERVATION: >
  A user able to modify a confirmed order is also able to edit or delete the audit record of a prior change to
  that same order through ordinary actions.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Make a recorded change to a confirmed order, then attempt, as an ordinary user, to edit or remove the audit
  record of that change.
```

## G07-PURCHASE-Q060

```yaml
QID: G07-PURCHASE-Q060
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Confirming (approving) an order changes only its approval or confirmation status and does not, by itself,
  create the receipt or billing records that would execute the commitment.
WHY_IT_MATTERS: >
  If approval itself executes the commitment, the separation between deciding to commit and actually carrying
  it out collapses into a single unreviewed action.
DISCONFIRMING_OBSERVATION: >
  Confirming an order, with no further action by anyone, results in a receipt or a bill already existing for
  that order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Confirm an order and, without taking any further action, check whether a receipt or bill has already been
  created for it.
```

## G07-PURCHASE-Q061

```yaml
QID: G07-PURCHASE-Q061
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The logic that determines the eventual accounting postings arising from a bill tied to an order operates
  independently of the order-approval decision logic, so that changing only the approval routing or
  configuration cannot change the resulting posted amounts.
WHY_IT_MATTERS: >
  Posting logic embedded inside the approval path would be invisible to anyone who only reviewed the approval
  rules, and could shift financial results as a side effect of an unrelated approval change.
DISCONFIRMING_OBSERVATION: >
  Changing only the approval routing or configuration for orders, with the same underlying order and bill
  otherwise unchanged, changes the resulting posted accounting amounts.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Post the same order and bill under two different approval configurations and compare the resulting posted
  amounts.
```

## G07-PURCHASE-Q062

```yaml
QID: G07-PURCHASE-Q062
MODULE: purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An order that is rejected or cancelled before ever being approved leaves no posted accounting impact anywhere
  in the chain from order through receipt to bill.
WHY_IT_MATTERS: >
  Any posted value from a commitment that was never actually approved would mean the approval gate can be
  bypassed entirely.
DISCONFIRMING_OBSERVATION: >
  An order rejected or cancelled prior to approval is found to have generated a posted accounting entry
  somewhere in the receipt or billing chain.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create an order, reject or cancel it before any approval is granted, and check the full order-to-bill chain
  for any posted accounting entry.
```
