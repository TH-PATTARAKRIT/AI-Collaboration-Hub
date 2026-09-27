# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-SALE-MVQ70-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale`
**Wave:** W2
**Author Cell:** P-S1 (GMVQ Question Factory — Production Team P-S1)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 70

## Purpose

`sale` is the BASE module of G08 (31 modules, none previously had a bank). It owns the group's core invariants -- the quotation-to-confirmed-order boundary and what a change does to a confirmed line; price-list and manual-discount precedence and what happens when a price list changes while a quotation is still open; invoicing policy (ordered versus delivered quantity) and the divergence it produces; partial delivery and partial invoicing in either order; cancellation after partial delivery or partial invoicing; returns and credit notes; locking a confirmed order and the distinct authority to unlock it; currency rate capture and where a later rate difference lands; the moment tax is determined; committed date versus availability; down payments and their settlement; duplicate detection; a customer record merged or archived mid-order; multi-company and intercompany selling; margin and cost visibility as a permission question; and the audit trail of a price or quantity change on a confirmed order -- so that the 28 `sale_*` bridge banks in this group do not need to restate them and can instead ask what happens to these invariants at their own seam. Deep, explicit treatment is placed on the approval/execution/posting separation invariant: confirming an order must not itself execute fulfilment, and posting logic must not live inside the confirmation path.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 70 questions exist because they test 70 distinct material hypotheses, spread across business capability, business rule, state transition, configuration dependency, role/permission, exception path, cancellation, reversal, negative case, cross-module dependency, optional behaviour, auditability, tenant/company boundary, concurrency and ordering, and configuration reachability.
- Particular depth is placed on modification-after-confirmation and what it does to already-processed history (Q002-Q006), on invoicing-policy divergence (Q012-Q019), on cancellation and returns (Q020-Q026), and on the approval/execution/posting separation invariant (Q050-Q053).
- `LAYER: BASE` marks a foundation/configuration question (pricing setup, invoicing-policy definition, locking capability, multi-company scope, margin-visibility permission, numbering scheme, availability-check scope); `LAYER: PROCESS` marks a transactional/lifecycle question, since this module carries both layers.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.


## G08-SALE-Q001

```yaml
QID: G08-SALE-Q001
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Confirming a quotation changes it into a binding commitment distinct from an unconfirmed draft, and an unconfirmed record carries no such commitment.
WHY_IT_MATTERS: >
  If a draft is treated as a commitment, or a confirmed commitment can still be edited exactly like a draft, the boundary customers and staff rely on to know what has actually been agreed collapses.
DISCONFIRMING_OBSERVATION: >
  An unconfirmed record produces the same downstream effects (becoming eligible for delivery or for invoicing) as a confirmed one.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a quotation and leave it unconfirmed; attempt to deliver or invoice against it and observe whether this is permitted before confirmation.
```

## G08-SALE-Q002

```yaml
QID: G08-SALE-Q002
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Adding a new line to an already-confirmed order does not retroactively alter the quantity or value already recorded as delivered or invoiced for the lines that existed before the addition.
WHY_IT_MATTERS: >
  If adding a line could rewrite what was already delivered or billed, no confirmed commitment would ever be a stable record of what actually happened.
DISCONFIRMING_OBSERVATION: >
  Adding a line to a confirmed order changes the recorded delivered or invoiced amount of a pre-existing, already-processed line.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order, partially deliver and invoice one line, then add a new line to the same order and compare the pre-existing line's delivery and invoice records before and after.
```

## G08-SALE-Q003

```yaml
QID: G08-SALE-Q003
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Removing a line from a confirmed order that has already been partially delivered or invoiced is blocked, or handled through an explicit compensating action, rather than silently erasing the recorded quantity and value.
WHY_IT_MATTERS: >
  Silently deleting a line that already has real-world consequences would leave delivered goods or issued invoices with no corresponding order line to explain them.
DISCONFIRMING_OBSERVATION: >
  A line already partially delivered or invoiced can be removed from the order with no compensating record and no block, leaving an orphaned delivery or invoice.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Partially deliver or invoice one line of a confirmed order, then attempt to delete that line entirely and observe what happens to the existing delivery or invoice reference.
```

## G08-SALE-Q004

```yaml
QID: G08-SALE-Q004
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Increasing the ordered quantity on a confirmed line does not retroactively alter the delivery or invoice records already created for the portion of that line processed before the increase.
WHY_IT_MATTERS: >
  Retroactively rewriting history already acted on would make prior deliveries and invoices unreliable evidence of what actually happened.
DISCONFIRMING_OBSERVATION: >
  Increasing a confirmed line's quantity changes the quantity or value shown on a delivery or invoice already issued before the increase.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order line, deliver and invoice part of it, increase the ordered quantity, and compare the earlier delivery and invoice records before and after the increase.
```

## G08-SALE-Q005

```yaml
QID: G08-SALE-Q005
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Decreasing the ordered quantity on a confirmed line below the quantity already delivered or invoiced is either blocked or produces an explicit recorded exception, never a silent negative adjustment to history.
WHY_IT_MATTERS: >
  A silent negative adjustment could make the order quantity fall below what has already left the business or already been billed, with no trace that this happened.
DISCONFIRMING_OBSERVATION: >
  The ordered quantity is reduced below the already-delivered or already-invoiced quantity with no block and no recorded exception.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm and partially fulfil a line beyond a new intended quantity, then attempt to reduce the ordered quantity below what was already delivered or invoiced.
```

## G08-SALE-Q006

```yaml
QID: G08-SALE-Q006
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Changing the unit price on a confirmed line does not retroactively alter the price recorded on deliveries or invoices already issued for that line.
WHY_IT_MATTERS: >
  If a later price change could rewrite an already-issued invoice's price, the invoice would stop being reliable evidence of what the customer was actually charged.
DISCONFIRMING_OBSERVATION: >
  Changing a confirmed line's unit price changes the price shown on an invoice already issued for that line before the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm a line, invoice part of it, change the unit price, and compare the already-issued invoice's recorded price before and after the change.
```

## G08-SALE-Q007

```yaml
QID: G08-SALE-Q007
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  When a price-list rule and a manually entered discount both apply to the same line, an explicit precedence rule governs which one prevails, rather than both being silently combined with no record of which was actually applied.
WHY_IT_MATTERS: >
  Without a defined precedence, two staff pricing the same scenario could reach different totals with no way to say which pricing was correct or intended.
DISCONFIRMING_OBSERVATION: >
  The same line, priced under an identical price-list rule and an identical manual discount, produces different final prices depending only on the order of entry, with no record of which rule governed.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set up a line that qualifies for both a price-list rule and a manual discount, apply them in different orders, and compare the resulting price and any record of precedence.
```

## G08-SALE-Q008

```yaml
QID: G08-SALE-Q008
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A price-list change made after a quotation already exists does not silently reprice that already-open quotation; it takes effect only on lines or documents created after the change.
WHY_IT_MATTERS: >
  If an open quotation repriced itself whenever the underlying price list changed, a customer could never rely on a quoted price remaining the price they were quoted.
DISCONFIRMING_OBSERVATION: >
  An open quotation's line price changes automatically after the referenced price list is edited, with no separate action taken on the quotation itself.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a quotation referencing a price list, change the price-list rule, and re-open the existing quotation to check whether its line price changed on its own.
```

## G08-SALE-Q009

```yaml
QID: G08-SALE-Q009
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  The ability to manually override a computed price is governed by a permission distinct from the ordinary ability to create or confirm an order.
WHY_IT_MATTERS: >
  If any order-taker could override price without a separate authorization, the price list and discount rules protecting margin would be enforceable in name only.
DISCONFIRMING_OBSERVATION: >
  A user who can create and confirm orders but has not been granted price-override permission is nonetheless able to enter a price different from the computed one.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  As a user permitted to create and confirm orders but not permitted to override price, attempt to manually change a line's computed price.
```

## G08-SALE-Q010

```yaml
QID: G08-SALE-Q010
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where multiple discount rules can apply to the same line, an explicit stacking rule determines whether they combine, and how, rather than the outcome depending on an unspecified order of evaluation.
WHY_IT_MATTERS: >
  An unspecified stacking outcome means the same combination of qualifying discounts could produce different final prices on different occasions with no way to say which was correct.
DISCONFIRMING_OBSERVATION: >
  The same line qualifying for the same two discount rules produces a different combined discount depending only on an unrecorded order of application.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Configure two discount rules that both apply to one line, apply them, and repeat under conditions that should be identical to check whether the combined result is stable.
```

## G08-SALE-Q011

```yaml
QID: G08-SALE-Q011
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where a minimum-margin or minimum-price floor is configured, it is enforced at the point the price is set or overridden, not only reported after the fact.
WHY_IT_MATTERS: >
  A floor that is only reported afterward allows an order to be confirmed and fulfilled at a loss before anyone is informed the floor was breached.
DISCONFIRMING_OBSERVATION: >
  A line priced below the configured floor is confirmed without any block or warning at the point of entry, the breach only appearing in a later report.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a minimum-margin floor, enter a line price below it, and observe whether entry or confirmation is blocked or only later reported.
```

## G08-SALE-Q012

```yaml
QID: G08-SALE-Q012
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Invoicing policy (whether invoicing is driven by ordered quantity or by delivered quantity) is a property that governs when a line becomes eligible to invoice, and the two settings produce different eligible-to-invoice quantities for the same partially delivered line.
WHY_IT_MATTERS: >
  If both policies produced the same eligible amount, the distinction would be meaningless, and any business relying on delivery-based billing could be invoiced ahead of actual fulfilment without anyone noticing the difference.
DISCONFIRMING_OBSERVATION: >
  A line that is only partially delivered shows the identical eligible-to-invoice quantity under both an ordered-quantity policy and a delivered-quantity policy.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create two otherwise identical lines, one under each invoicing policy, deliver each partially by the same amount, and compare the eligible-to-invoice quantity each produces.
```

## G08-SALE-Q013

```yaml
QID: G08-SALE-Q013
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An order invoiced strictly on ordered quantity can be fully invoiced before any physical delivery has occurred.
WHY_IT_MATTERS: >
  Businesses that bill on commitment rather than fulfilment need this to be true, or their normal billing cycle would be blocked by a delivery step that policy says is irrelevant to invoicing.
DISCONFIRMING_OBSERVATION: >
  An order under an ordered-quantity invoicing policy cannot be invoiced until at least partial delivery has been recorded.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Confirm an order under an ordered-quantity invoicing policy with zero delivery recorded, and attempt to invoice it in full.
```

## G08-SALE-Q014

```yaml
QID: G08-SALE-Q014
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An order invoiced strictly on delivered quantity cannot be invoiced for quantity beyond what has actually been delivered, even where the full quantity was confirmed.
WHY_IT_MATTERS: >
  Allowing invoicing ahead of delivery under a delivery-based policy would defeat the entire purpose of choosing that policy and could bill a customer for goods not yet provided.
DISCONFIRMING_OBSERVATION: >
  An order under a delivered-quantity invoicing policy can be invoiced for a quantity greater than what has been recorded as delivered.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Confirm an order under a delivered-quantity invoicing policy, deliver only part of it, and attempt to invoice the full ordered quantity.
```

## G08-SALE-Q015

```yaml
QID: G08-SALE-Q015
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When delivered quantity exceeds ordered quantity, the invoiceable amount under a delivered-quantity policy is bounded by an explicit rule (the order quantity, the delivered quantity, or a defined tolerance), rather than being unbounded.
WHY_IT_MATTERS: >
  An unbounded invoiceable amount following an over-delivery could allow a customer to be billed for materially more than was ever agreed, with no configured limit catching it.
DISCONFIRMING_OBSERVATION: >
  An over-delivered line can be invoiced for the full over-delivered quantity with no limit tied to the originally ordered quantity or any configured tolerance.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Deliver a quantity greater than ordered on a delivered-quantity-policy line, and attempt to invoice the full delivered amount.
```

## G08-SALE-Q016

```yaml
QID: G08-SALE-Q016
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Changing a line's invoicing policy after some quantity has already been invoiced under the prior policy does not retroactively change the eligible-to-invoice quantity already consumed by the existing invoice.
WHY_IT_MATTERS: >
  If a policy change could retroactively alter what an already-issued invoice was allowed to bill, invoices already sent to a customer would stop being a stable record.
DISCONFIRMING_OBSERVATION: >
  Switching invoicing policy mid-order changes the quantity considered already invoiced on a prior, already-issued invoice for the same line.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Invoice part of a line under one invoicing policy, switch the line's policy, and check whether the already-issued invoice's recorded quantity changed.
```

## G08-SALE-Q017

```yaml
QID: G08-SALE-Q017
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Partial delivery followed later by partial invoicing correctly attributes the invoice to the quantity actually delivered at each stage, not to the full order quantity.
WHY_IT_MATTERS: >
  Attributing an invoice to the full order quantity regardless of what was actually delivered at that point would misstate what the customer had actually received when billed.
DISCONFIRMING_OBSERVATION: >
  An invoice issued after only a first partial delivery reflects the full order quantity rather than only the quantity delivered so far.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Deliver a line in two stages, invoice immediately after the first stage under a delivered-quantity policy, and check what quantity the invoice reflects.
```

## G08-SALE-Q018

```yaml
QID: G08-SALE-Q018
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Invoicing issued before any delivery has occurred (an invoice-first or deposit-style scenario) is tracked distinctly from invoicing tied to delivered quantity, so the two are not double-counted once delivery later occurs.
WHY_IT_MATTERS: >
  Without a distinct tracking of pre-delivery invoicing, a later delivery-triggered invoice could bill the same value again on top of what was already collected.
DISCONFIRMING_OBSERVATION: >
  After an order is invoiced before any delivery, a subsequent delivery-triggered invoice bills the same quantity or value a second time.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Invoice an order before any delivery, then deliver it and trigger any delivery-based invoicing, and check whether the same value is billed twice.
```

## G08-SALE-Q019

```yaml
QID: G08-SALE-Q019
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A backorder created from an under-delivery remains linked to the original order, and the remaining balance is derived from that link rather than requiring the order to be manually re-entered.
WHY_IT_MATTERS: >
  If the remaining balance had to be manually re-entered, the figure would depend on someone remembering the original commitment correctly rather than on a reliable link to it.
DISCONFIRMING_OBSERVATION: >
  An under-delivered line's remaining balance cannot be traced back to the original order line that produced it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Under-deliver a confirmed line, and trace the resulting outstanding balance back to the order line that originated it.
```

## G08-SALE-Q020

```yaml
QID: G08-SALE-Q020
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order with zero delivery and zero invoicing removes it from any pending-fulfilment view with no residual accounting or stock impact.
WHY_IT_MATTERS: >
  A cancelled order that never had any real-world effect should leave nothing behind; if it did, cancellation would not mean what it claims to mean.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order that was never delivered or invoiced still leaves a stock reservation, accounting entry, or pending-fulfilment listing behind.
EXPECTED_SURFACE: S1,S2,S5
PRECONDITIONS: >
  Confirm an order, cancel it before any delivery or invoicing, and check for any remaining stock reservation, accounting entry, or pending-task listing.
```

## G08-SALE-Q021

```yaml
QID: G08-SALE-Q021
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order after partial delivery does not reverse the delivery already recorded; it leaves the delivered portion as a completed fact while stopping further fulfilment of the undelivered remainder.
WHY_IT_MATTERS: >
  Reversing a delivery that already physically happened would make the record disagree with reality, and would misrepresent what the customer actually received.
DISCONFIRMING_OBSERVATION: >
  Cancelling a partially delivered order removes or alters the record of the delivery that had already occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Partially deliver a confirmed order, cancel it, and check whether the already-recorded delivery is preserved unchanged.
```

## G08-SALE-Q022

```yaml
QID: G08-SALE-Q022
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order after partial invoicing does not delete or silently alter the invoice already issued; unwinding the invoiced amount requires a distinct compensating document, not a direct edit to the original invoice.
WHY_IT_MATTERS: >
  Editing or deleting an already-issued invoice would destroy financial evidence of a transaction that legally and financially already occurred.
DISCONFIRMING_OBSERVATION: >
  Cancelling a partially invoiced order deletes or directly edits the amount on the invoice already issued.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Partially invoice a confirmed order, cancel it, and check whether the existing invoice is altered directly or only addressed through a separate compensating document.
```

## G08-SALE-Q023

```yaml
QID: G08-SALE-Q023
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An order cancelled after confirmation remains distinguishable, after the fact, from an order that was never confirmed at all.
WHY_IT_MATTERS: >
  If the two states became indistinguishable, no one reviewing history could tell whether a commitment was made and later withdrawn or never made in the first place.
DISCONFIRMING_OBSERVATION: >
  A cancelled-after-confirmation order and a never-confirmed order carry identical stored state with no way to tell them apart afterward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm and then cancel one order, leave a second order unconfirmed, and compare the two records' stored state afterward.
```

## G08-SALE-Q024

```yaml
QID: G08-SALE-Q024
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A credit note issued against a delivered and invoiced line is traceable back to the specific original order and line it corrects, not merely to the customer in general.
WHY_IT_MATTERS: >
  A credit traceable only to a customer, not to the specific order and line, would make it impossible to reconcile which original commitment the credit is actually correcting.
DISCONFIRMING_OBSERVATION: >
  A credit note issued to correct a specific invoiced line carries no stored reference back to that original order or line.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Issue a credit note against a specific invoiced line and check whether the credit note carries a traceable reference to that order and line.
```

## G08-SALE-Q025

```yaml
QID: G08-SALE-Q025
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A physical return of goods and the financial credit note correcting the corresponding invoice are tracked as related but distinguishable events, so that a return recorded with no corresponding credit note leaves an identifiable gap rather than silently balancing.
WHY_IT_MATTERS: >
  If a physical return and its financial correction were the same event, a returned item with no matching financial credit could go unnoticed, leaving the customer's account incorrectly stated.
DISCONFIRMING_OBSERVATION: >
  A recorded physical return with no corresponding credit note produces no identifiable discrepancy between physical and financial records.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record a physical return without issuing a corresponding credit note, and check whether this produces any identifiable, reviewable discrepancy.
```

## G08-SALE-Q026

```yaml
QID: G08-SALE-Q026
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A credit note can be issued for a quantity greater than what was actually delivered and invoiced only through an explicit override, not as an unchecked default path.
WHY_IT_MATTERS: >
  Allowing a credit beyond what was ever billed by default would let a credit note manufacture a financial liability that never corresponds to any real transaction.
DISCONFIRMING_OBSERVATION: >
  A credit note for a quantity greater than the original delivered and invoiced quantity is issued through the ordinary path with no override step or warning.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to issue a credit note for a quantity exceeding what was delivered and invoiced on the original line, without invoking any special override.
```

## G08-SALE-Q027

```yaml
QID: G08-SALE-Q027
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A confirmed order can be placed into a locked state that blocks further modification of its committed lines through the ordinary edit path.
WHY_IT_MATTERS: >
  Without a locking capability, a supposedly final, confirmed commitment remains as editable as an ordinary draft, defeating the purpose of confirmation as a control point.
DISCONFIRMING_OBSERVATION: >
  A confirmed order placed into its locked state can still have its committed lines edited through the ordinary edit path with no distinct unlock step.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm an order, lock it, and attempt to edit one of its lines through the ordinary editing path.
```

## G08-SALE-Q028

```yaml
QID: G08-SALE-Q028
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  The authority required to unlock a locked order for correction is distinct from the authority required to confirm or edit an ordinary open order.
WHY_IT_MATTERS: >
  If unlocking required no more authority than everyday order editing, locking would provide no real control at all.
DISCONFIRMING_OBSERVATION: >
  A user who can confirm and edit ordinary open orders, but has not been separately granted unlock authority, is nonetheless able to unlock a locked order.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  As a user permitted to confirm and edit ordinary orders but not granted unlock authority, attempt to unlock a locked order.
```

## G08-SALE-Q029

```yaml
QID: G08-SALE-Q029
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A change made to an order after it is unlocked leaves a record distinguishing that the order passed through a lock-then-unlock cycle, rather than looking identical to an order that was never locked.
WHY_IT_MATTERS: >
  Without such a distinguishing record, a reviewer could not tell a routine draft edit apart from a correction made to a document that had already been treated as final.
DISCONFIRMING_OBSERVATION: >
  An order edited after being unlocked shows no trace, on inspection, that it had previously been locked at all.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm, lock, unlock, and edit an order, then inspect its record for any trace that a lock/unlock cycle occurred.
```

## G08-SALE-Q030

```yaml
QID: G08-SALE-Q030
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The exchange rate captured at order confirmation is the rate carried by the order for its own valuation, independent of the company's exchange rate on a later date of delivery or invoicing.
WHY_IT_MATTERS: >
  If the order's own valuation silently tracked a later rate, neither party could rely on the rate that was actually agreed at confirmation.
DISCONFIRMING_OBSERVATION: >
  An order's own recorded valuation changes to reflect a new exchange rate on the delivery or invoice date rather than retaining the rate captured at confirmation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Confirm a foreign-currency order, allow the exchange rate to move, deliver or invoice later, and check which rate the order's own valuation reflects.
```

## G08-SALE-Q031

```yaml
QID: G08-SALE-Q031
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When invoicing occurs on a date with a different exchange rate than the order date, the resulting currency gain or loss lands in an identifiable accounting outcome rather than being silently absorbed into the invoiced revenue figure.
WHY_IT_MATTERS: >
  If a rate difference were silently folded into revenue, the true sales figure and the currency effect would become inseparable, misstating both.
DISCONFIRMING_OBSERVATION: >
  Invoicing a foreign-currency order at a rate different from the order's rate changes the recorded revenue figure with no separate identifiable currency gain or loss.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  Confirm a foreign-currency order at one rate, invoice it after the rate has moved, and check whether a distinct currency gain or loss is identifiable apart from the revenue amount.
```

## G08-SALE-Q032

```yaml
QID: G08-SALE-Q032
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A down payment collected at one exchange rate and settled against a final invoice at a later rate does not silently equalize the two rates; any resulting difference is identifiable rather than hidden inside the settled amount.
WHY_IT_MATTERS: >
  Hiding the rate difference inside the settled amount would make it impossible to tell how much of the final figure is genuine value versus a currency movement.
DISCONFIRMING_OBSERVATION: >
  Settling a foreign-currency down payment against a final invoice at a different rate produces a settled figure with no identifiable trace of the rate difference between the two events.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  Collect a foreign-currency down payment at one rate, settle it against a final invoice issued at a different rate, and check whether the rate difference is identifiable.
```

## G08-SALE-Q033

```yaml
QID: G08-SALE-Q033
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The tax rate applied to a line is determined at an identifiable point in the order's lifecycle, and a tax-rate change occurring after that determining point does not retroactively alter the line's already-determined tax.
WHY_IT_MATTERS: >
  Without a fixed determining point, the same order could show a different tax outcome purely depending on when someone happened to look at it, rather than on when the transaction actually occurred.
DISCONFIRMING_OBSERVATION: >
  A line's recorded tax changes after its determining point in the lifecycle has already passed, purely because the general tax rate changed afterward.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Confirm a line under one tax rate, change the general tax rate afterward, and check whether the already-determined line's recorded tax changes.
```

## G08-SALE-Q034

```yaml
QID: G08-SALE-Q034
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A tax exemption applied to a specific line can override a customer's default exemption status, and the line-level override persists independently of any later change to the customer's default.
WHY_IT_MATTERS: >
  If a line-level override were not independent of the customer default, correcting one line's tax treatment could unpredictably alter every other line referencing the same customer.
DISCONFIRMING_OBSERVATION: >
  Changing a customer's default tax-exemption status alters the tax already recorded on a line where an explicit line-level override had already been applied.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Apply a line-level tax-exemption override that differs from the customer's default, then change the customer's default and check whether the line's override is preserved.
```

## G08-SALE-Q035

```yaml
QID: G08-SALE-Q035
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A committed delivery date recorded on an order is stored as a value distinct from any date derived from actual stock or production availability, so the two can disagree without one silently overwriting the other.
WHY_IT_MATTERS: >
  If the committed date and the availability-derived date were the same stored value, a business could never tell whether it had promised something it could not yet deliver.
DISCONFIRMING_OBSERVATION: >
  An order's committed delivery date changes automatically whenever the underlying stock or production availability estimate changes.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Record a committed delivery date on an order, change the underlying stock or production availability estimate, and check whether the committed date changes on its own.
```

## G08-SALE-Q036

```yaml
QID: G08-SALE-Q036
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A quotation carries a validity or expiration date after which it can no longer be confirmed under its original terms without an explicit re-validation step.
WHY_IT_MATTERS: >
  Without an expiration concept, a customer could confirm a stale quotation at outdated pricing indefinitely, regardless of how long conditions had since changed.
DISCONFIRMING_OBSERVATION: >
  A quotation past its stated validity date can still be confirmed through the ordinary path with no re-validation step or warning.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set a validity date on a quotation, let that date pass, and attempt to confirm the quotation through the ordinary path.
```

## G08-SALE-Q037

```yaml
QID: G08-SALE-Q037
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Re-confirming an order after its quotation validity has lapsed does not silently reapply the original price list or discount without re-evaluating current pricing.
WHY_IT_MATTERS: >
  Silently honouring stale pricing after an explicit expiration would make the expiration date meaningless in practice, even if it exists formally.
DISCONFIRMING_OBSERVATION: >
  An order re-confirmed after its validity date has lapsed carries forward its original price and discount unchanged with no re-evaluation against current pricing.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Let a quotation's validity lapse, change the underlying price list, re-confirm the quotation, and check whether the price reflects the original or the current price list.
```

## G08-SALE-Q038

```yaml
QID: G08-SALE-Q038
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A down payment recorded against an order is applied against the final invoice as an explicit deduction, and the final invoice does not double-count the down-payment amount.
WHY_IT_MATTERS: >
  Double-counting a down payment would overbill the customer for an amount they already paid, undermining trust in the final invoice's accuracy.
DISCONFIRMING_OBSERVATION: >
  The final invoice for an order with a recorded down payment shows the full order value with no deduction for the amount already collected.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  Collect a down payment on an order, complete fulfilment, issue the final invoice, and check whether the down payment is deducted from the final amount due.
```

## G08-SALE-Q039

```yaml
QID: G08-SALE-Q039
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A down payment collected on an order later cancelled before further fulfilment leaves an identifiable outstanding balance requiring explicit resolution, rather than disappearing from the record.
WHY_IT_MATTERS: >
  If the collected amount simply disappeared from the record on cancellation, money already received would have no corresponding accounting trace at all.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order after collecting a down payment leaves no identifiable record of the amount still held and needing resolution.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Collect a down payment, cancel the order before any further fulfilment, and check whether an identifiable outstanding balance remains recorded.
```

## G08-SALE-Q040

```yaml
QID: G08-SALE-Q040
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The system distinguishes a genuine duplicate order (same customer, same lines, same timeframe) from two independent orders that happen to match closely, rather than silently merging them or allowing both through with no flag at all.
WHY_IT_MATTERS: >
  Silently merging two genuinely independent orders would lose one customer's real commitment, while never flagging true duplicates risks double fulfilment of the same request.
DISCONFIRMING_OBSERVATION: >
  Two orders with matching customer, lines, and timeframe are both confirmed with no flag, warning, or record that a likely duplicate was detected.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create two closely matching orders for the same customer in a short timeframe and observe whether any duplicate indication is raised at confirmation.
```

## G08-SALE-Q041

```yaml
QID: G08-SALE-Q041
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A customer record merged into another during the life of an open order leaves that order correctly attributed to the surviving customer record, with no orphaned reference to the merged-away record.
WHY_IT_MATTERS: >
  An order still pointing at a customer record that no longer effectively exists could become invisible to normal customer-facing views and fall through the cracks.
DISCONFIRMING_OBSERVATION: >
  After a customer merge, an order originally raised against the merged-away record still references that now-inactive record rather than the surviving one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Merge a customer record that has an open order into another customer record, and check which customer record the open order references afterward.
```

## G08-SALE-Q042

```yaml
QID: G08-SALE-Q042
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A customer record archived while an order remains open does not block operations already in progress on that order, but does prevent a new order from being raised against the archived record without an explicit reactivation.
WHY_IT_MATTERS: >
  Blocking in-progress work over a later archival decision would strand a legitimate open commitment, while allowing unrestricted new orders against an archived record defeats the purpose of archiving it.
DISCONFIRMING_OBSERVATION: >
  Archiving a customer with an open order blocks continued work on that already-open order, or alternatively still allows a brand-new order to be raised against the archived record with no reactivation step.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Archive a customer record that has one open order, then attempt to continue that open order and separately attempt to raise a brand-new order against the same archived record.
```

## G08-SALE-Q043

```yaml
QID: G08-SALE-Q043
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  An order raised under one company context cannot be confirmed, delivered, or invoiced from a different company context without an explicit intercompany mechanism recording the cross-company relationship.
WHY_IT_MATTERS: >
  Without this boundary, one legal entity's transactions could be silently fulfilled or billed through another entity's books, corrupting each entity's own financial record.
DISCONFIRMING_OBSERVATION: >
  An order created under one company is delivered or invoiced directly from a different company's context with no recorded intercompany relationship.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create an order under one company and attempt to deliver or invoice it directly from a different company context with no intercompany order in place.
```

## G08-SALE-Q044

```yaml
QID: G08-SALE-Q044
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An intercompany order between two companies within the same group produces a consistent pair of records, one on each side of the relationship, rather than a one-sided record visible only to the selling company.
WHY_IT_MATTERS: >
  A one-sided record would leave the buying company's own books with no corresponding entry for a transaction that, from its side, genuinely occurred.
DISCONFIRMING_OBSERVATION: >
  An intercompany order produces a record on the selling company's side with no corresponding record created on the buying company's side.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an intercompany order between two companies in the same group and check whether a corresponding record exists on both sides.
```

## G08-SALE-Q045

```yaml
QID: G08-SALE-Q045
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A price list or discount agreement scoped to one company is not applied to an order raised under a different company without an explicit sharing configuration.
WHY_IT_MATTERS: >
  Without this boundary, one company's negotiated pricing could leak into another company's transactions, misstating the terms actually agreed for each entity.
DISCONFIRMING_OBSERVATION: >
  An order raised under a company that is not in scope for a given price list nonetheless has that price list's rules applied to it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Scope a price list to one company only, then create an order under a different company and check whether that price list's rules are applied.
```

## G08-SALE-Q046

```yaml
QID: G08-SALE-Q046
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Visibility of the cost basis and resulting margin on a line is governed by a permission distinct from the permission to view or edit the order's price and quantity.
WHY_IT_MATTERS: >
  If margin visibility were tied to ordinary order-editing rights, every order-taker would see cost and margin data regardless of whether they were ever meant to.
DISCONFIRMING_OBSERVATION: >
  A user permitted to view and edit an order's price and quantity, but not granted margin-visibility permission, is nonetheless able to see the line's cost basis or margin.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user permitted to manage an order's price and quantity but not granted margin visibility, attempt to view that order's cost basis or margin figure.
```

## G08-SALE-Q047

```yaml
QID: G08-SALE-Q047
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A user without margin-visibility permission cannot derive the hidden cost figure indirectly through a computed total, export, or report that includes margin.
WHY_IT_MATTERS: >
  A permission that only blocks one screen while leaving the same figure recoverable through an export or report provides no real protection at all.
DISCONFIRMING_OBSERVATION: >
  A user without margin-visibility permission can obtain the underlying cost or margin figure through an export, computed total, or report rather than the direct field.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user without margin-visibility permission, attempt to obtain the cost or margin figure through an export, print, or report that touches the same order.
```

## G08-SALE-Q048

```yaml
QID: G08-SALE-Q048
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A change to the price on a confirmed line leaves a trace of the prior value, the new value, and who made the change, rather than overwriting the field with no history.
WHY_IT_MATTERS: >
  Without such a trace, a disputed price on a supposedly final commitment could never be resolved, since there would be no record of what it originally was or who changed it.
DISCONFIRMING_OBSERVATION: >
  Changing the price on a confirmed line leaves no retrievable record of the prior value or of who made the change.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Confirm a line, change its price, and attempt to retrieve a record of the prior value and the identity of who made the change.
```

## G08-SALE-Q049

```yaml
QID: G08-SALE-Q049
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A change to the quantity on a confirmed line leaves a trace equivalent to the price-change trail, distinguishing a later correction from the order's original confirmed commitment.
WHY_IT_MATTERS: >
  Without an equivalent trail, a quantity correction after confirmation would be indistinguishable from what was actually agreed at the moment of confirmation.
DISCONFIRMING_OBSERVATION: >
  Changing the quantity on a confirmed line leaves no retrievable record distinguishing the corrected quantity from the originally confirmed quantity.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Confirm a line, change its quantity, and attempt to retrieve a record distinguishing the original confirmed quantity from the corrected one.
```

## G08-SALE-Q050

```yaml
QID: G08-SALE-Q050
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Confirming an order does not itself trigger the physical fulfilment step; fulfilment is a separate action that must be initiated in its own right, even immediately after confirmation.
WHY_IT_MATTERS: >
  If confirmation itself executed fulfilment, the approval represented by confirmation and the physical act of fulfilling it would be the same event, removing any independent control over whether and when fulfilment actually happens.
DISCONFIRMING_OBSERVATION: >
  Confirming an order automatically produces a completed fulfilment record with no separate fulfilment action having been taken.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Confirm an order and, without taking any further action, check whether a fulfilment record already exists.
```

## G08-SALE-Q051

```yaml
QID: G08-SALE-Q051
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Confirming an order does not itself create a posted accounting entry; posting occurs only through the distinct invoicing and delivery-valuation steps that follow confirmation.
WHY_IT_MATTERS: >
  If confirmation itself posted accounting entries, the commercial approval step and the financial recognition step would be fused, making it impossible to review or control financial posting independently of commercial approval.
DISCONFIRMING_OBSERVATION: >
  Confirming an order produces a posted accounting entry before any invoicing or delivery valuation has taken place.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Confirm an order and, before any invoicing or delivery valuation occurs, check the accounting ledger for any posted entry attributable to that order.
```

## G08-SALE-Q052

```yaml
QID: G08-SALE-Q052
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The logic that determines the resulting accounting postings from an invoice tied to an order operates independently of the order-confirmation logic, so that a change limited to confirmation rules or routing cannot itself change a posted amount.
WHY_IT_MATTERS: >
  Posting logic embedded inside the confirmation path would be invisible to anyone reviewing only the confirmation rules, and could shift financial results as an undocumented side effect of an unrelated confirmation change.
DISCONFIRMING_OBSERVATION: >
  Changing only the confirmation rules or routing configuration, with the same underlying order and invoice otherwise unchanged, changes the resulting posted accounting amount.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Post the same order and invoice under two different confirmation-routing configurations and compare the resulting posted accounting amounts.
```

## G08-SALE-Q053

```yaml
QID: G08-SALE-Q053
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An order that is never confirmed, or that is cancelled prior to confirmation, leaves no posted accounting impact anywhere in the chain from quotation through delivery to invoice.
WHY_IT_MATTERS: >
  Any posted value from a commitment that was never actually confirmed would mean the confirmation gate can be bypassed entirely.
DISCONFIRMING_OBSERVATION: >
  An order rejected or cancelled prior to confirmation is found to have generated a posted accounting entry somewhere in the delivery or invoicing chain.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create an order, cancel it before confirmation, and check the full quotation-to-invoice chain for any posted accounting entry.
```

## G08-SALE-Q054

```yaml
QID: G08-SALE-Q054
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Shipping or handling charges added to an order after confirmation trigger a recomputation of tax and total consistent with the rule applied to ordinary lines, rather than being appended as an untaxed or unvalidated addition.
WHY_IT_MATTERS: >
  An untaxed or unvalidated addition would let a document's printed or posted total silently disagree with what the sum of its own lines and tax rules actually require.
DISCONFIRMING_OBSERVATION: >
  Adding a shipping or handling charge to a confirmed order changes the order's line content but leaves the total or tax uncomputed for that new charge.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Add a shipping or handling charge to an already-confirmed order and check whether tax and total are recomputed to include it.
```

## G08-SALE-Q055

```yaml
QID: G08-SALE-Q055
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Line-level rounding and order-total rounding, where both exist, are reconciled by an explicit rule so the sum of rounded lines and the rounded total do not silently diverge on the printed or posted document.
WHY_IT_MATTERS: >
  An unreconciled divergence between a summed set of rounded lines and a separately rounded total would make the printed document internally inconsistent by even a small amount, undermining trust in the figures.
DISCONFIRMING_OBSERVATION: >
  The sum of an order's individually rounded lines does not equal its separately computed rounded total, with no rule identifiable that explains or corrects the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct an order whose line amounts each require rounding and compare the sum of the rounded lines against the separately computed rounded total.
```

## G08-SALE-Q056

```yaml
QID: G08-SALE-Q056
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Multiple confirmed orders for the same customer can be combined onto a single invoice, and the resulting invoice remains traceable back to each contributing order and its specific lines.
WHY_IT_MATTERS: >
  An invoice that cannot be traced back to its contributing orders would make it impossible to reconcile a combined bill against the individual commitments it is supposed to represent.
DISCONFIRMING_OBSERVATION: >
  An invoice combining lines from more than one order does not retain a traceable reference back to each originating order and line.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Combine lines from two confirmed orders for the same customer onto a single invoice and check whether each line remains traceable to its originating order.
```

## G08-SALE-Q057

```yaml
QID: G08-SALE-Q057
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A single confirmed order can be split across multiple invoices without any line's cumulative invoiced quantity across those invoices exceeding what that line actually authorizes.
WHY_IT_MATTERS: >
  Without this constraint, splitting billing across several invoices could allow a line to be billed for more, in total, than the order ever actually confirmed.
DISCONFIRMING_OBSERVATION: >
  Splitting an order across multiple invoices allows the cumulative invoiced quantity for one line to exceed that line's own ordered or eligible quantity.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split a confirmed order's invoicing across two separate invoices and check whether their combined quantity for one line exceeds that line's authorized quantity.
```

## G08-SALE-Q058

```yaml
QID: G08-SALE-Q058
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A framework or blanket order that authorizes future releases is distinguished in state from an individual release confirmed against it, so that consuming a release reduces the remaining authorized balance on the framework rather than leaving it unchanged.
WHY_IT_MATTERS: >
  If releases did not draw down a tracked balance, a framework agreement's remaining authorization could never be relied on to reflect what has actually already been committed against it.
DISCONFIRMING_OBSERVATION: >
  Confirming an individual release against a framework order leaves the framework's remaining authorized balance unchanged.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set up a framework order with a defined authorized quantity, confirm one release against it, and check whether the framework's remaining balance was reduced.
```

## G08-SALE-Q059

```yaml
QID: G08-SALE-Q059
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A credit hold or blocked-account status on a customer is enforced at an identifiable point (quotation creation, confirmation, or delivery), and orders already past that point when the hold is applied are not silently exempted from any consequence.
WHY_IT_MATTERS: >
  If the enforcement point were unclear, staff could not predict at what stage a blocked customer's activity would actually be stopped, and orders in flight when a hold begins could slip through unexamined.
DISCONFIRMING_OBSERVATION: >
  A customer placed on hold has an order already past the enforcement point proceed to the next stage with no recorded check against the hold.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Place a customer on hold while one of their orders is already past the point where hold enforcement is defined to apply, and observe whether that order is checked against the hold.
```

## G08-SALE-Q060

```yaml
QID: G08-SALE-Q060
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Confirming an order against a customer already over its credit limit either blocks confirmation or produces an explicit recorded exception, rather than confirming silently with no trace that the limit was exceeded.
WHY_IT_MATTERS: >
  Silent confirmation over a credit limit would make the limit purely decorative, since breaching it would leave no evidence for anyone to act on afterward.
DISCONFIRMING_OBSERVATION: >
  An order confirmed while its customer is already over the configured credit limit shows no block and no recorded exception anywhere.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Set a customer's outstanding balance above its configured credit limit, confirm a new order for that customer, and check for a block or a recorded exception.
```

## G08-SALE-Q061

```yaml
QID: G08-SALE-Q061
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Order numbering is unique and does not silently reuse a number, even across a fiscal-year rollover or a gap left by a cancelled draft.
WHY_IT_MATTERS: >
  A reused order number would make two genuinely different commitments indistinguishable by their own reference number, undermining every process that cites that number.
DISCONFIRMING_OBSERVATION: >
  Two distinct orders, one created before and one after a fiscal-year rollover or a cancelled-draft gap, are found to carry the identical order number.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a draft order and cancel it, then create and confirm a new order across a numbering boundary such as a fiscal-year rollover, and check whether any number is reused.
```

## G08-SALE-Q062

```yaml
QID: G08-SALE-Q062
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Order numbering scoped per company or per branch does not collide with numbering from another company or branch sharing the same underlying sequence pattern.
WHY_IT_MATTERS: >
  A numbering collision across companies or branches would make an order reference ambiguous as soon as it needed to be understood outside its own originating unit.
DISCONFIRMING_OBSERVATION: >
  Two orders confirmed under different companies or branches on the same sequence pattern are found to carry the identical order number.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm one order under each of two companies or branches sharing the same numbering pattern and compare the resulting order numbers for a collision.
```

## G08-SALE-Q063

```yaml
QID: G08-SALE-Q063
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Confirming a line tied to a specific warehouse or stock location is checked for availability at that specific location, not against a combined total across all locations.
WHY_IT_MATTERS: >
  Checking only a combined total could confirm a commitment that is actually unavailable at the specific location the order depends on, even though stock exists somewhere else entirely.
DISCONFIRMING_OBSERVATION: >
  A line tied to a specific location is confirmed as available using a combined total across every location rather than the stock actually present at that specific location.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set stock so that a specific location has none of an item while other locations combined have plenty, and confirm a line tied specifically to the empty location.
```

## G08-SALE-Q064

```yaml
QID: G08-SALE-Q064
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Confirming the same order a second time, for example through a retried action, does not create a duplicate commitment or a duplicate downstream fulfilment record; confirmation is idempotent.
WHY_IT_MATTERS: >
  A non-idempotent confirmation could double an order's real-world consequences purely because of a retried click or a repeated automated call, with no user intent behind the duplication.
DISCONFIRMING_OBSERVATION: >
  Triggering the confirmation action twice on the same order produces two separate confirmed commitments or two separate downstream fulfilment records.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger the confirmation action on the same order twice in immediate succession and check whether this produces one confirmed commitment or two.
```

## G08-SALE-Q065

```yaml
QID: G08-SALE-Q065
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two users editing the same open order at overlapping times do not silently overwrite each other's change with no indication that a conflicting edit occurred.
WHY_IT_MATTERS: >
  A silent overwrite would let one user's change vanish with no trace, and neither user would have any way to know their work had been lost.
DISCONFIRMING_OBSERVATION: >
  Two users saving conflicting edits to the same open order in close succession results in the second save silently discarding the first, with no indication given to either user.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have two sessions open and edit the same open order concurrently, save both in close succession, and check whether either edit is silently lost with no indication.
```

## G08-SALE-Q066

```yaml
QID: G08-SALE-Q066
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A recurring or subscription-style order's renewal is tracked as a distinct generated document linked back to its origin, rather than being indistinguishable from a manually created new order.
WHY_IT_MATTERS: >
  If a renewal could not be traced back to its origin, no one could tell, from the renewed document alone, whether it represented a continuing commitment or an entirely new one.
DISCONFIRMING_OBSERVATION: >
  A renewal generated from a recurring order arrangement carries no stored reference back to the arrangement or order that produced it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Configure a recurring order arrangement, let it generate a renewal, and check whether the renewal references the arrangement that produced it.
```

## G08-SALE-Q067

```yaml
QID: G08-SALE-Q067
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Archiving or deleting a price list that is referenced by historical confirmed orders does not alter the price already recorded on those historical order lines.
WHY_IT_MATTERS: >
  If removing a price list could alter historical prices, closed transactions would no longer be a stable record of what was actually charged at the time.
DISCONFIRMING_OBSERVATION: >
  Archiving or deleting a price list changes the price shown on a historical, already-confirmed order line that had referenced it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm an order referencing a specific price list, archive or delete that price list, and check whether the historical order line's recorded price changed.
```

## G08-SALE-Q068

```yaml
QID: G08-SALE-Q068
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A free-of-charge or promotional line is excluded from revenue-bearing invoice totals while still appearing on the order and delivery record, rather than either being silently invoiced or silently omitted from the document entirely.
WHY_IT_MATTERS: >
  Silently invoicing it would overcharge the customer, while silently omitting it from the record entirely would leave no evidence the item was ever committed or delivered at all.
DISCONFIRMING_OBSERVATION: >
  A free-of-charge line either appears on the invoice with a non-zero charge, or is entirely absent from the order and delivery record.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Add a free-of-charge or promotional line to an order, carry it through delivery and invoicing, and check whether it is charged on the invoice and whether it appears on the order and delivery record.
```

## G08-SALE-Q069

```yaml
QID: G08-SALE-Q069
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An order created entirely as a no-charge sample, where such a designation exists, does not generate a posted revenue entry when delivered or closed.
WHY_IT_MATTERS: >
  Posting revenue for something explicitly designated as never chargeable would misstate actual sales performance with a transaction that was never intended to be one.
DISCONFIRMING_OBSERVATION: >
  An order explicitly designated as a no-charge sample generates a posted revenue entry once delivered or closed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an order designated as a no-charge sample, carry it through delivery and closure, and check the accounting ledger for any posted revenue entry.
```

## G08-SALE-Q070

```yaml
QID: G08-SALE-Q070
MODULE: sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A deposit or down payment can be applied against a specific line of an order rather than only against the order's total, and doing so reduces that line's own remaining invoiceable balance specifically.
WHY_IT_MATTERS: >
  Without line-level application, a deposit intended to cover one particular item could not be distinguished, in the record, from a deposit against the order as an undifferentiated whole.
DISCONFIRMING_OBSERVATION: >
  A deposit applied against a specific line reduces the order's overall remaining balance but leaves that specific line's own remaining invoiceable balance unchanged.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a deposit against one specific line of a multi-line order and check whether that line's own remaining invoiceable balance, not just the order total, is reduced.
```
