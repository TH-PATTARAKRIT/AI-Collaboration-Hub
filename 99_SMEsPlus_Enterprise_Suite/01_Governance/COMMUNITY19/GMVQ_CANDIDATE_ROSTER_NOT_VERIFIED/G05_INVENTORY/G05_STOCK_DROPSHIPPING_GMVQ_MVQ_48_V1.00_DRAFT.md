# SMEsPlus ENTERPRISE SUITE
## GMVQ — G05 INVENTORY / stock_dropshipping Module MVQ Bank

**Document ID:** GMVQ-G05-STOCK_DROPSHIPPING-MVQ48-V1.00
**Group:** G05 INVENTORY
**Module Metadata:** `stock_dropshipping`
**Wave:** W2
**Author Cell:** GMVQ PRODUCTION TEAM P04
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This bank supplies the module-specific MVQ set for `stock_dropshipping`, fulfillment where goods
move directly from a supplier to a customer without ever occupying a physical location of your own.
Per the G05 INVENTORY group brief, this is a top-risk area because it is the one path in the group
where a movement is real for accounting and for the customer while no physical custody or count of
your own ever verifies it, so the questions reach past the document flow into valuation, margin
recognition, quantity trust, privacy exposure between customer and supplier, and traceability with
no physical checkpoint. Every question passes the seam test: if the absence of physical custody were
removed — that is, if the same transaction were instead fulfilled from your own stock — the question
would no longer make sense; a question that would still make sense either way was cut during
authoring rather than included. Coverage is spread across business capability, business rule, state
transition, configuration dependency, role and permission, exception path, cancellation, reversal,
negative case, cross-module dependency, optional behaviour, auditability, tenant/company boundary,
concurrency and ordering, runtime reachability, configuration reachability, and source/runtime
contradiction potential. This bank supplements the 55-question Standard bank; combined research
depth for this module is 55 + 48 = 103.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses; none
  was trimmed or stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table,
  field, method, XML ID, API path), and the module's own metadata name never appears outside the
  `MODULE:` field — generic terms such as "drop-shipped line" or "the arrangement" stand in for it
  throughout.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G05-STOCK_DROPSHIPPING-Q001

```yaml
QID: G05-STOCK_DROPSHIPPING-Q001
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A distinct, defined event marks a drop-shipped line as received-equivalent for accounting and downstream purposes, even though no physical receipt ever occurs on any of your own premises; the record does not remain permanently in an unresolved 'awaiting receipt' state.
WHY_IT_MATTERS: >
  If nothing ever formally substitutes for physical receipt, every downstream process that depends on receipt having happened either never fires or fires against an undefined condition.
DISCONFIRMING_OBSERVATION: >
  A drop-shipped line's status stays indefinitely in an awaiting-receipt condition with no defined event ever resolving it, even after the transaction is otherwise treated as finished.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Carry a drop-shipped order line through to the point where the supplier is known to have shipped it, and inspect what, if anything, marks it as received on your side.
```

## G05-STOCK_DROPSHIPPING-Q002

```yaml
QID: G05-STOCK_DROPSHIPPING-Q002
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A single, stated evidence source is treated as authoritative for marking a drop-shipped customer order fulfilled, rather than the fulfilled status depending on whichever of several inconsistent signals happens to arrive first.
WHY_IT_MATTERS: >
  If fulfilled status can be set by any of several unreconciled signals, two otherwise-identical orders can end up fulfilled on different logical grounds with no way to tell which applied.
DISCONFIRMING_OBSERVATION: >
  Two equivalent drop-shipped orders are marked fulfilled based on two different kinds of evidence, with nothing in the record distinguishing which evidence justified which order's status.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trace what specific event or evidence causes a drop-shipped order's fulfilled status to be set, and check whether that source is consistent across more than one order.
```

## G05-STOCK_DROPSHIPPING-Q003

```yaml
QID: G05-STOCK_DROPSHIPPING-Q003
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A valuation or costing entry is created for a drop-shipped line at the point cost logically transfers to you, consistent with normal costing timing, rather than either never posting a cost at all or posting it twice.
WHY_IT_MATTERS: >
  No cost ever posting means margin can never be correctly known for that sale; a cost posted twice overstates expense and understates margin without anyone noticing why.
DISCONFIRMING_OBSERVATION: >
  A drop-shipped line's sale is recognized with no corresponding cost ever posted, or with two separate cost postings for what was a single supplier shipment.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a drop-shipped transaction end to end and inspect whether, and how many times, a costing entry was created for it.
```

## G05-STOCK_DROPSHIPPING-Q004

```yaml
QID: G05-STOCK_DROPSHIPPING-Q004
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Margin on a drop-shipped line is only ever recognized once both the cost side and the revenue side of the transaction exist; it is not recognized one-sided while only the supplier bill or only the customer invoice has arrived.
WHY_IT_MATTERS: >
  One-sided margin recognition means a reported profit figure includes revenue with no matching cost, or cost with no matching revenue, either of which misstates the period's result.
DISCONFIRMING_OBSERVATION: >
  A margin or profit figure for a drop-shipped line is reported before both the supplier-side cost document and the customer-side revenue document exist.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create the customer invoice for a drop-shipped line before the supplier invoice exists, and check whether any margin figure is reported for that line in the interim.
```

## G05-STOCK_DROPSHIPPING-Q005

```yaml
QID: G05-STOCK_DROPSHIPPING-Q005
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a supplier ships less than was ordered on a drop-shipped line and that shortfall is known before the customer is invoiced, the customer-facing document reflects the actual shipped quantity rather than the originally ordered quantity.
WHY_IT_MATTERS: >
  Invoicing a customer for quantity you know was never actually shipped to them creates a billing dispute and a liability for goods that do not exist on their end.
DISCONFIRMING_OBSERVATION: >
  A customer is invoiced for the original ordered quantity on a drop-shipped line after the supplier's actual, lower shipped quantity was already known.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a supplier shipment quantity lower than ordered on a drop-shipped line before generating the customer invoice, and check what quantity the customer invoice uses.
```

## G05-STOCK_DROPSHIPPING-Q006

```yaml
QID: G05-STOCK_DROPSHIPPING-Q006
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a supplier quantity shortfall on a drop-shipped line is discovered only after the customer was already invoiced at the ordered quantity, a defined correction path exists to reconcile the two rather than leaving the mismatch unresolved indefinitely.
WHY_IT_MATTERS: >
  An unreconciled late-discovered shortfall leaves either the customer overbilled or the business unaware it owes a correction, with no process ever forcing that to surface.
DISCONFIRMING_OBSERVATION: >
  A known shortfall between what the supplier actually shipped and what the customer was already invoiced for a drop-shipped line has no path or record leading toward a correction.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Invoice a customer at the ordered quantity, then later record a lower actual supplier-shipped quantity for the same line, and check what happens next.
```

## G05-STOCK_DROPSHIPPING-Q007

```yaml
QID: G05-STOCK_DROPSHIPPING-Q007
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An over-shipment by the supplier on a drop-shipped line that is never explicitly reported back into the system leaves a detectable gap somewhere in the records, even though no physical count on your own side ever occurs to catch it directly.
WHY_IT_MATTERS: >
  If the system is structurally blind to an unreported over-shipment, an entire category of supplier billing error can never be caught by anyone, no matter how carefully records elsewhere are reviewed.
DISCONFIRMING_OBSERVATION: >
  A supplier ships and invoices for a quantity higher than the order and the drop-ship transaction closes with no record anywhere reflecting a mismatch between ordered and invoiced-by-supplier quantity.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Simulate a supplier invoice for a higher quantity than was ordered on a drop-shipped line and check whether any record surfaces the discrepancy.
```

## G05-STOCK_DROPSHIPPING-Q008

```yaml
QID: G05-STOCK_DROPSHIPPING-Q008
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Only the information a supplier genuinely needs to fulfill a drop-shipped order — the ship-to address and what was ordered — is transmitted to the supplier; the price the customer is being charged is not exposed to the supplier through the same document flow.
WHY_IT_MATTERS: >
  Exposing your customer-facing price to your own supplier hands them information they can use against your margin in future negotiations, for no operational benefit.
DISCONFIRMING_OBSERVATION: >
  A document sent to the supplier for fulfillment purposes also carries the price charged to the customer.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Generate the document sent to the supplier to trigger a drop-ship fulfillment and inspect its full content for customer-facing pricing.
```

## G05-STOCK_DROPSHIPPING-Q009

```yaml
QID: G05-STOCK_DROPSHIPPING-Q009
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Nothing on the shipment-related material the customer actually receives or sees for a drop-shipped order exposes the supplier's own identity or address in a way the customer could use to bypass you directly in the future.
WHY_IT_MATTERS: >
  A customer discovering the real supplier behind a drop-shipped item can go around you next time, which is the core commercial risk of this fulfillment model if left uncontrolled.
DISCONFIRMING_OBSERVATION: >
  A document or package element the customer receives for a drop-shipped order reveals the supplier's name or address to the customer.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trace every document and label associated with a drop-shipped order that the customer would plausibly see and check each for supplier-identifying information.
```

## G05-STOCK_DROPSHIPPING-Q010

```yaml
QID: G05-STOCK_DROPSHIPPING-Q010
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The system defines, for a drop-shipped item, where a customer return is expected to physically go — back to the supplier directly, or to a location of yours — rather than defaulting silently to a normal return flow that assumes you have a location ready to receive it.
WHY_IT_MATTERS: >
  A return flow that assumes physical custody you don't have will direct a customer to send an item somewhere nobody is expecting it, or generate a return authorization for a location that will never actually receive the item.
DISCONFIRMING_OBSERVATION: >
  A return is initiated on a drop-shipped item and the resulting instructions or documents assume it will arrive at one of your own locations with no route back to the actual supplier defined.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Initiate a return on an order line that was originally drop-shipped and inspect where the return process directs the physical item.
```

## G05-STOCK_DROPSHIPPING-Q011

```yaml
QID: G05-STOCK_DROPSHIPPING-Q011
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a drop-ship return is defined as going directly to the supplier, any valuation reversal recorded on your side for that return is consistent with, and does not exceed, the original valuation event that was recorded for the sale, even though you never take physical custody of the returned item.
WHY_IT_MATTERS: >
  A valuation reversal disconnected from an actual physical movement risks reversing a cost that was never really yours to reverse, or reversing the wrong amount.
DISCONFIRMING_OBSERVATION: >
  A valuation reversal is posted for a drop-ship return that does not match, in amount or basis, the original valuation event posted when the item was sold.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Process a return on a drop-shipped sale that returns directly to the supplier, and compare the resulting valuation reversal to the original sale's valuation event.
```

## G05-STOCK_DROPSHIPPING-Q012

```yaml
QID: G05-STOCK_DROPSHIPPING-Q012
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a customer cancels a drop-shipped order after the supplier has already dispatched the goods, the system distinguishes this case from a clean cancellation before anything moved, rather than presenting cancellation as equally complete and final in both situations.
WHY_IT_MATTERS: >
  Treating a cancellation as clean when goods are physically already in transit from the supplier leaves an item arriving with nobody expecting it and no process to deal with it.
DISCONFIRMING_OBSERVATION: >
  Cancelling a drop-shipped order after the supplier has already shipped produces the same outcome and the same record as cancelling one before the supplier ever shipped.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel one drop-shipped order before the supplier ships and a second, equivalent one after the supplier has already shipped, and compare the resulting records.
```

## G05-STOCK_DROPSHIPPING-Q013

```yaml
QID: G05-STOCK_DROPSHIPPING-Q013
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a customer cancels a drop-shipped order after having already paid or been invoiced, but before the supplier-side purchase is cancelled or credited, the two sides of the unwind (customer refund and supplier order cancellation) are linked such that neither can be left permanently orphaned from the other.
WHY_IT_MATTERS: >
  An unwind that only addresses the customer side leaves a live supplier commitment that nobody is tracking, or one that only addresses the supplier side leaves a customer owed a refund that never happens.
DISCONFIRMING_OBSERVATION: >
  A cancelled drop-shipped order shows the customer-side refund or credit completed while the corresponding supplier-side order remains open with no linkage flagging that it still needs resolution, or the reverse.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Cancel a drop-shipped order after the customer has already been invoiced and before the supplier order is addressed, then check whether the two sides of the unwind remain linked.
```

## G05-STOCK_DROPSHIPPING-Q014

```yaml
QID: G05-STOCK_DROPSHIPPING-Q014
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An internal movement document generated for a drop-shipped transaction that never physically happened at any of your locations is distinguishable from a document representing a real, physical movement, so it cannot be mistaken for one in a later quantity reconciliation.
WHY_IT_MATTERS: >
  A symbolic movement record that looks identical to a real one would let a stock count reconciliation treat a transaction that never touched your shelves as though it had, corrupting the reconciliation.
DISCONFIRMING_OBSERVATION: >
  A document generated for a drop-shipped transaction is indistinguishable, in a quantity or location reconciliation, from a document representing a movement that actually occurred at one of your locations.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a drop-shipped transaction and compare the resulting internal documents against those of a normal warehouse movement, from the perspective of a stock reconciliation process.
```

## G05-STOCK_DROPSHIPPING-Q015

```yaml
QID: G05-STOCK_DROPSHIPPING-Q015
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an item type would normally require lot or serial identity to be captured, the system either captures that identity for a drop-shipped unit through the information available (such as supplier-provided data) or explicitly records that this identity could not be captured, rather than silently defaulting to an untracked state.
WHY_IT_MATTERS: >
  A silent gap in lot or serial capture removes traceability exactly where it might matter most later, such as a recall, with no one aware the gap exists until it is needed.
DISCONFIRMING_OBSERVATION: >
  A drop-shipped unit of an item type that normally requires lot or serial tracking completes its transaction with no lot or serial identity recorded and no indication that the absence was ever noted or explained.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Drop-ship a unit of an item type that would normally require lot or serial tracking and check what identity information, if any, ends up recorded against it.
```

## G05-STOCK_DROPSHIPPING-Q016

```yaml
QID: G05-STOCK_DROPSHIPPING-Q016
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a lot or serial identity is captured for a drop-shipped unit, that identity remains linked to the specific customer who received it, so a later recall affecting that lot can be traced to the affected customer through the existing records.
WHY_IT_MATTERS: >
  A recall that cannot be traced to who actually received the affected lot defeats the entire purpose of lot tracking for a drop-shipped item.
DISCONFIRMING_OBSERVATION: >
  A lot or serial identity is recorded for a drop-shipped sale but cannot be connected back to the specific customer order it was sold through.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Drop-ship a lot- or serial-tracked item with its identity captured, and check whether that identity can be traced forward to the specific customer who received it.
```

## G05-STOCK_DROPSHIPPING-Q017

```yaml
QID: G05-STOCK_DROPSHIPPING-Q017
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  On an order with some lines fulfilled from your own stock and other lines drop-shipped, each line's fulfillment proceeds independently along its own path, with neither line's method or status blocking or altering the other's.
WHY_IT_MATTERS: >
  Coupling the two paths means a delay or exception on the drop-shipped line could hold up a line that was otherwise ready to ship from stock, or vice versa, for no real reason.
DISCONFIRMING_OBSERVATION: >
  A delay or exception on one line of a mixed order prevents progress on, or changes the status of, a different line on the same order that uses a different fulfillment method.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create an order with one line fulfilled from stock and one line drop-shipped, introduce a delay on one line, and check whether the other line's progress is affected.
```

## G05-STOCK_DROPSHIPPING-Q018

```yaml
QID: G05-STOCK_DROPSHIPPING-Q018
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  On a customer-facing delivery record that combines a warehouse-fulfilled line and a drop-shipped line, the different actual origins and different actual delivery timings of each line are represented honestly, rather than merged into a single delivery event that overstates what actually happened as one occurrence.
WHY_IT_MATTERS: >
  A single merged delivery event hides that part of the order came from a different party at a different time, which matters the moment a customer disputes when or whether part of the order arrived.
DISCONFIRMING_OBSERVATION: >
  A mixed order's customer-facing delivery record shows a single delivery event covering both a warehouse-fulfilled line and a drop-shipped line that actually arrived separately and at different times.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Fulfill a mixed order's lines through different methods and at different actual times, and inspect the resulting customer-facing delivery record for whether it reflects that split.
```

## G05-STOCK_DROPSHIPPING-Q019

```yaml
QID: G05-STOCK_DROPSHIPPING-Q019
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the supplier invoice for a drop-shipped transaction lands in a different accounting period than the customer invoice, the cost and the revenue for that same transaction are still matched to each other for margin purposes, rather than each falling into whichever period its own document happened to land in and misstating both periods.
WHY_IT_MATTERS: >
  Mismatched period recognition on the two sides of the same transaction misstates margin in both the period that gets a cost with no matching revenue and the period that gets revenue with no matching cost.
DISCONFIRMING_OBSERVATION: >
  The reported margin for a period includes a drop-shipped transaction's revenue without its matching cost, or its cost without its matching revenue, because the two documents landed in different periods.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Arrange a drop-shipped transaction so the supplier invoice and customer invoice fall in different accounting periods, and inspect how margin is reported for each period.
```

## G05-STOCK_DROPSHIPPING-Q020

```yaml
QID: G05-STOCK_DROPSHIPPING-Q020
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a customer invoice for a drop-shipped line is issued before the corresponding supplier invoice ever arrives, an accrual or equivalent placeholder for the expected cost is created, so revenue is not left standing against a recorded cost of zero.
WHY_IT_MATTERS: >
  Revenue recognized against no cost at all overstates margin for as long as the supplier invoice is outstanding, which can be an extended and uncontrolled period.
DISCONFIRMING_OBSERVATION: >
  A drop-shipped transaction shows revenue recognized with a zero recorded cost for an extended period while the supplier invoice remains outstanding, with no accrual standing in for the expected cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Invoice a customer for a drop-shipped line well before the supplier invoice is expected to arrive, and inspect what cost, if any, is reflected against that revenue in the interim.
```

## G05-STOCK_DROPSHIPPING-Q021

```yaml
QID: G05-STOCK_DROPSHIPPING-Q021
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The evidence source relied on to mark a drop-shipped order delivered, and the fact that you did not independently witness the delivery yourself, is visible on the record rather than presented with the same confidence as a delivery your own operation executed and confirmed directly.
WHY_IT_MATTERS: >
  Treating third-party-reported delivery evidence as equivalent in confidence to a delivery you personally confirmed hides the real evidentiary weakness exactly where a later dispute will test it.
DISCONFIRMING_OBSERVATION: >
  A drop-shipped order's delivered status carries no indication of what evidence it rests on, appearing identical in confidence to an order you fulfilled and confirmed delivery of yourself.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Mark a drop-shipped order delivered based on third-party evidence and inspect the record for any indication of the evidence source or its limits.
```

## G05-STOCK_DROPSHIPPING-Q022

```yaml
QID: G05-STOCK_DROPSHIPPING-Q022
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a customer disputes ever receiving a drop-shipped order that is marked delivered, the record retains enough information to show that the delivered status rests on a third-party claim rather than your own direct confirmation, so the two situations are not indistinguishable after the fact.
WHY_IT_MATTERS: >
  Without this distinction, every delivery dispute on a drop-shipped order looks, from the record alone, exactly as strong or weak as a dispute over an order you delivered yourself, which is not true.
DISCONFIRMING_OBSERVATION: >
  After a customer disputes receipt, the record provides no way to tell that the original delivered status came from a third party rather than your own confirmation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Mark a drop-shipped order delivered from third-party evidence, then simulate a customer dispute over receipt, and check what the record can show about the basis for the original status.
```

## G05-STOCK_DROPSHIPPING-Q023

```yaml
QID: G05-STOCK_DROPSHIPPING-Q023
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A drop-ship supplier who never ships and never responds does not leave the order indefinitely presented as still normally proceeding; after a reasonable window, the situation is surfaced as an exception requiring attention rather than remaining silent.
WHY_IT_MATTERS: >
  An order silently stuck behind an unresponsive supplier, with nothing ever flagging it, means the customer is left waiting with nobody actively working the problem.
DISCONFIRMING_OBSERVATION: >
  A drop-ship order whose supplier never ships and never responds continues to display a normal in-progress status indefinitely with nothing ever escalating it as an exception.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Simulate a drop-ship supplier that never confirms or ships an order and observe whether, after a reasonable period, anything flags the order as an exception.
```

## G05-STOCK_DROPSHIPPING-Q024

```yaml
QID: G05-STOCK_DROPSHIPPING-Q024
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  On a multi-line drop-ship order fulfilled by more than one supplier at different times, the customer-facing status reflects the split reality of partial arrival rather than a single all-or-nothing status that cannot represent part of the order having already arrived.
WHY_IT_MATTERS: >
  A single status that can only say fully done or not done at all hides genuinely useful information from the customer and from support staff about what has actually happened so far.
DISCONFIRMING_OBSERVATION: >
  An order with lines from two different suppliers, one of which has already shipped and one of which has not, is shown with a single overall status that does not distinguish the two.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a multi-line drop-ship order sourced from two different suppliers, advance one supplier's line further than the other, and check the order's overall customer-facing status.
```

## G05-STOCK_DROPSHIPPING-Q025

```yaml
QID: G05-STOCK_DROPSHIPPING-Q025
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the supplier's actual invoiced cost for a drop-shipped line differs from the cost that was assumed when the customer order was placed, the margin or valuation for that line is updated to reflect the real supplier cost rather than remaining frozen at the earlier estimate indefinitely.
WHY_IT_MATTERS: >
  A margin figure left frozen at an estimate that was already proven wrong by the actual supplier invoice misstates profitability for as long as nobody manually corrects it.
DISCONFIRMING_OBSERVATION: >
  The margin reported for a drop-shipped line still reflects an estimated supplier cost after the actual, different supplier invoice for that same line has already been recorded.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a supplier invoice with a cost different from the estimate assumed at order time, and check whether the line's reported margin updates to reflect it.
```

## G05-STOCK_DROPSHIPPING-Q026

```yaml
QID: G05-STOCK_DROPSHIPPING-Q026
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The system provides an explicit point at which responsibility for tax or duty on a drop-shipped line is determined, rather than silently assuming it is identical to a line fulfilled from your own warehouse when the goods physically cross a boundary your warehouse-fulfilled sales never would.
WHY_IT_MATTERS: >
  Silently assuming identical tax treatment for a fundamentally different physical movement risks a filing that does not match what actually happened to the goods.
DISCONFIRMING_OBSERVATION: >
  A drop-shipped line whose goods physically cross a boundary a warehouse-fulfilled equivalent would not is treated identically for tax purposes with no distinguishing determination point in the record.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a drop-shipped line where the goods move across a boundary a warehouse-fulfilled equivalent would not, and check whether tax treatment is separately determined for it.
```

## G05-STOCK_DROPSHIPPING-Q027

```yaml
QID: G05-STOCK_DROPSHIPPING-Q027
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  In a multi-company setup, a drop-ship transaction attributes the supplier purchase to the correct legal company and the customer sale to the correct legal company even when those two are different entities, without either leg posting to the wrong company's books.
WHY_IT_MATTERS: >
  A purchase or sale posted to the wrong legal entity in a drop-ship arrangement misstates both companies' books and can create an intercompany discrepancy nobody planned for.
DISCONFIRMING_OBSERVATION: >
  A drop-ship transaction spanning two legal companies posts the purchase or the sale leg to a company other than the one actually responsible for that side of the transaction.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Set up a drop-ship transaction where the purchasing company and the selling company are different legal entities, and check which company each posted document actually belongs to.
```

## G05-STOCK_DROPSHIPPING-Q028

```yaml
QID: G05-STOCK_DROPSHIPPING-Q028
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  In a multi-tenant deployment, no drop-ship configuration causes one tenant's customer address or order detail to become visible to, or to be processed through, a supplier record scoped to a different tenant.
WHY_IT_MATTERS: >
  Customer data crossing a tenant boundary through a supplier relationship is exactly the kind of cross-tenant leakage that undermines the isolation the whole platform depends on.
DISCONFIRMING_OBSERVATION: >
  A customer address or order detail belonging to one tenant appears in, or is transmitted through, a supplier record or document scoped to a different tenant.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  If tenant-scoped supplier records exist, check whether a drop-ship transaction in one tenant can reference or expose data through a supplier record belonging to another.
```

## G05-STOCK_DROPSHIPPING-Q029

```yaml
QID: G05-STOCK_DROPSHIPPING-Q029
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A drop-shipped line is excluded from any calculation of physically available-to-promise stock; it is never counted as though it were reservable inventory sitting in a location you actually control.
WHY_IT_MATTERS: >
  Counting a drop-shipped line as available physical stock would let the system promise a customer stock that does not, and never will, exist on your premises.
DISCONFIRMING_OBSERVATION: >
  A drop-shipped line's quantity is included in a figure that reports physically available stock at one of your locations.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a drop-shipped line for an item and check whether its quantity appears in any calculation of that item's physically available stock.
```

## G05-STOCK_DROPSHIPPING-Q030

```yaml
QID: G05-STOCK_DROPSHIPPING-Q030
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the supplier-side purchase behind a drop-ship order is cancelled while the customer-side sale remains active, that mismatch is surfaced as an exception requiring a decision, rather than leaving the customer order appearing to proceed normally with no remaining source of goods.
WHY_IT_MATTERS: >
  A customer order left 'in progress' with its only source of supply already cancelled behind the scenes will eventually fail the customer with no warning that anything was ever wrong.
DISCONFIRMING_OBSERVATION: >
  A customer order remains in a normal in-progress status after its underlying supplier purchase was cancelled, with nothing distinguishing it from an order that still has a live source of goods.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel the supplier-side purchase behind an active drop-ship customer order and check how the customer order's status responds.
```

## G05-STOCK_DROPSHIPPING-Q031

```yaml
QID: G05-STOCK_DROPSHIPPING-Q031
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the process that turns a customer order line into a supplier purchase is retried after an error, it does not create a second, duplicate purchase to the supplier for the same original demand.
WHY_IT_MATTERS: >
  A duplicated supplier purchase from a retry means a real second shipment can go out to the same customer, or you pay the supplier twice for one sale.
DISCONFIRMING_OBSERVATION: >
  Retrying the process that generates a supplier purchase from a customer order line, after an earlier attempt already partly succeeded, results in two separate supplier purchases for the same original line.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Interrupt the process that creates a supplier purchase from a drop-ship order line partway through, then retry it, and check whether one or two supplier purchases result.
```

## G05-STOCK_DROPSHIPPING-Q032

```yaml
QID: G05-STOCK_DROPSHIPPING-Q032
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a supplier can only partially fulfill a drop-ship order immediately and promises the remainder later, the unfulfilled remainder is tracked as a distinct, still-open obligation rather than the partial shipment being treated as though it closed the full original quantity.
WHY_IT_MATTERS: >
  Treating a partial shipment as though it closed the whole order means the still-owed remainder is forgotten and the customer never actually receives what they ordered.
DISCONFIRMING_OBSERVATION: >
  A drop-ship order shows fully closed status after only a partial supplier shipment, with no separate record of the remaining quantity still owed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a partial supplier shipment against a drop-ship order for less than the full ordered quantity and check the order's resulting status and any record of the shortfall.
```

## G05-STOCK_DROPSHIPPING-Q033

```yaml
QID: G05-STOCK_DROPSHIPPING-Q033
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If an order line is changed from drop-ship to warehouse fulfillment, or the reverse, before it completes, any quantity already progressed under the original method is carried over correctly, so the total quantity is never counted twice across both methods.
WHY_IT_MATTERS: >
  A method switch that does not carry over prior progress risks fulfilling, and counting, the same quantity once under each method.
DISCONFIRMING_OBSERVATION: >
  After a line is switched between drop-ship and warehouse fulfillment mid-progress, the total quantity recognized as fulfilled across both methods exceeds the quantity originally ordered.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Make partial progress on a line under one fulfillment method, switch it to the other method, complete it, and check the total quantity recognized as fulfilled.
```

## G05-STOCK_DROPSHIPPING-Q034

```yaml
QID: G05-STOCK_DROPSHIPPING-Q034
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Whether a given order line was actually fulfilled by drop-ship, as opposed to from your own stock, remains recorded and retrievable after the transaction is finished, rather than the finished record looking identical either way.
WHY_IT_MATTERS: >
  Reporting or an audit that needs to know how much of the business's fulfillment is drop-shipped cannot answer that question if the distinction disappears once a line is complete.
DISCONFIRMING_OBSERVATION: >
  A completed order line's record provides no way to determine after the fact whether it was fulfilled by drop-ship or from your own stock.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete one drop-shipped line and one warehouse-fulfilled line, then inspect their finished records for whether the fulfillment method is still determinable.
```

## G05-STOCK_DROPSHIPPING-Q035

```yaml
QID: G05-STOCK_DROPSHIPPING-Q035
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A specific product or a specific supplier being usable for drop-ship fulfillment is subject to an explicit configuration or authorization point, rather than any order being routable as a drop-ship to any supplier with no gate at all.
WHY_IT_MATTERS: >
  With no gate, an order could be drop-shipped through a supplier never actually vetted or approved for that role, with no one having decided that was acceptable.
DISCONFIRMING_OBSERVATION: >
  An order line is successfully routed as a drop-ship to a supplier with no explicit configuration ever having designated that supplier as eligible for drop-ship fulfillment of that product.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Attempt to drop-ship a product through a supplier with no drop-ship sourcing configuration set up for that product and supplier combination.
```

## G05-STOCK_DROPSHIPPING-Q036

```yaml
QID: G05-STOCK_DROPSHIPPING-Q036
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An attempt to drop-ship a line with no valid supplier sourcing information fails with a clear, actionable exception, rather than proceeding into an undefined or silently broken state.
WHY_IT_MATTERS: >
  A silent failure at this point leaves an order line stuck with no indication of what is actually missing, wasting time chasing a problem the system already knew about.
DISCONFIRMING_OBSERVATION: >
  An order line with no valid drop-ship supplier link enters an undefined or stuck state with no explanatory exception raised.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to drop-ship an order line for a product with no supplier sourcing information configured and observe what happens.
```

## G05-STOCK_DROPSHIPPING-Q037

```yaml
QID: G05-STOCK_DROPSHIPPING-Q037
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a supplier rejects or cannot fulfill a drop-ship order after it has already been promised to the customer, a defined path exists to source the item another way (from stock or a different supplier) rather than the order simply stalling with no route forward.
WHY_IT_MATTERS: >
  An order with no defined recovery path when the sole planned source falls through leaves the customer's commitment unresolved with nobody actively working an alternative.
DISCONFIRMING_OBSERVATION: >
  A drop-ship order whose supplier rejects it after being promised to the customer has no available path to re-source the item and remains stalled.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Have a supplier reject or fail an already-promised drop-ship order and check what options, if any, are available to re-source the item.
```

## G05-STOCK_DROPSHIPPING-Q038

```yaml
QID: G05-STOCK_DROPSHIPPING-Q038
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An order consisting entirely of drop-shipped lines, with no line ever touching your own stock, still produces a coherent and correct overall order status, rather than a status calculation that assumes at least one physically fulfilled line producing a wrong or stuck result.
WHY_IT_MATTERS: >
  An order-status assumption that quietly requires a warehouse-fulfilled line to work correctly would fail specifically on the all-drop-ship case, which is exactly the case this capability exists to support.
DISCONFIRMING_OBSERVATION: >
  An order made up entirely of drop-shipped lines shows an overall status that is incorrect, stuck, or inconsistent with the actual state of its lines.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create an order where every line is drop-shipped, progress the lines to completion, and check whether the overall order status correctly reflects that.
```

## G05-STOCK_DROPSHIPPING-Q039

```yaml
QID: G05-STOCK_DROPSHIPPING-Q039
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cost adjustment from the supplier that arrives after a drop-ship transaction's normal accounting period has closed can still be attached to that specific, already-closed transaction's margin, rather than falling outside any period the transaction can still be corrected in.
WHY_IT_MATTERS: >
  A late cost adjustment that cannot be attached to its transaction anymore either gets lost entirely or gets dumped into an unrelated period, misstating both the original transaction's margin and whatever period absorbs the stray cost.
DISCONFIRMING_OBSERVATION: >
  A late-arriving supplier cost adjustment for a specific closed drop-ship transaction cannot be linked back to that transaction's own margin and is recorded, if at all, disconnected from it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Close out a drop-ship transaction's accounting period, then introduce a late supplier cost adjustment for that same transaction, and check whether it can still be attached to it.
```

## G05-STOCK_DROPSHIPPING-Q040

```yaml
QID: G05-STOCK_DROPSHIPPING-Q040
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a drop-shipped line's supplier invoice and customer invoice are in different currencies, the margin calculation uses a documented, consistent conversion point and rate rather than mixing two unrelated conversion moments from each side.
WHY_IT_MATTERS: >
  Mixing two arbitrary, unrelated currency conversion moments produces a margin figure that cannot be reproduced or explained, and can be wrong in either direction depending on rate movement between the two moments.
DISCONFIRMING_OBSERVATION: >
  The margin calculated for a cross-currency drop-shipped line cannot be reproduced from a single, stated conversion rate and date applied consistently to both sides.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a drop-shipped transaction with the supplier invoiced in one currency and the customer invoiced in another, and inspect the basis used to calculate margin.
```

## G05-STOCK_DROPSHIPPING-Q041

```yaml
QID: G05-STOCK_DROPSHIPPING-Q041
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a customer is refunded for a cancelled drop-ship order before the corresponding supplier-side cancellation or credit is confirmed, that mismatch remains linked and visible rather than the two sides being tracked with no relationship to each other.
WHY_IT_MATTERS: >
  Refunding the customer while still being charged by the supplier, with nothing linking the two, means the loss goes unnoticed until someone happens to reconcile it much later, if ever.
DISCONFIRMING_OBSERVATION: >
  A customer refund for a cancelled drop-ship order is recorded with no visible link to the state of the corresponding supplier-side cancellation or credit.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Refund a customer for a cancelled drop-ship order before the supplier-side cancellation is confirmed, and check whether the two are linked in the record.
```

## G05-STOCK_DROPSHIPPING-Q042

```yaml
QID: G05-STOCK_DROPSHIPPING-Q042
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A single consolidated supplier shipment covering multiple customer orders correctly splits its delivery evidence and its cost allocation back to each individual customer order, rather than one shipment event being applied wholesale to only one order while the others are left unresolved.
WHY_IT_MATTERS: >
  A consolidated shipment applied to only one of several orders it actually covers leaves the other orders looking unfulfilled when the goods have, in reality, already gone out.
DISCONFIRMING_OBSERVATION: >
  A single supplier shipment known to cover several customer orders is reflected as resolving only one of those orders, leaving the others without their share of the delivery evidence or cost allocation.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Simulate one supplier shipment intended to cover several distinct customer orders and check how its evidence and cost are distributed across those orders.
```

## G05-STOCK_DROPSHIPPING-Q043

```yaml
QID: G05-STOCK_DROPSHIPPING-Q043
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a supplier ships a drop-shipped item to the customer in a different packaging or unit-of-measure quantity than the customer ordered, the conversion between the two is applied consistently on both the cost side and the customer-facing document, so the two sides do not disagree about the underlying quantity.
WHY_IT_MATTERS: >
  A unit-conversion mismatch between the supplier-facing and customer-facing sides of the same physical shipment produces a quantity or cost figure that does not actually correspond to what moved.
DISCONFIRMING_OBSERVATION: >
  The quantity or cost recorded on the supplier side of a drop-shipped transaction does not reconcile, after unit conversion, with the quantity recorded on the customer side of the same transaction.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set up a drop-shipped line where the supplier's shipping unit differs from the customer's ordering unit, and compare the converted quantities on each side.
```

## G05-STOCK_DROPSHIPPING-Q044

```yaml
QID: G05-STOCK_DROPSHIPPING-Q044
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A historical inventory valuation or on-hand report for a past date correctly excludes drop-shipped lines from ever appearing as on-hand stock, including for a date that falls between the order being placed and the supplier actually shipping it, in every report or view that reflects quantity, not only the primary one.
WHY_IT_MATTERS: >
  A drop-shipped line leaking into even one secondary quantity view, for even a historical date, would misstate a stock position that someone later relies on for a decision or a reconciliation.
DISCONFIRMING_OBSERVATION: >
  A drop-shipped line's quantity appears as on-hand stock in any report or view for a date within the window between order placement and actual supplier shipment.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place a drop-shipped order, wait until it falls inside the order-to-ship window, and check every available quantity or valuation report or view for that period.
```

## G05-STOCK_DROPSHIPPING-Q045

```yaml
QID: G05-STOCK_DROPSHIPPING-Q045
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Given a specific drop-shipped unit, the existing records can reconstruct, end to end, who supplied it, when it moved, and who received it, even though no physical custody checkpoint of your own was ever created for it.
WHY_IT_MATTERS: >
  An inability to answer a basic chain-of-custody question for a drop-shipped unit, when asked for a compliance or dispute reason, leaves the business unable to demonstrate what actually happened.
DISCONFIRMING_OBSERVATION: >
  Asked to reconstruct the chain of custody for a specific drop-shipped unit, the existing records cannot connect the supplier, the movement, and the receiving customer into one coherent trace.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Pick one completed drop-shipped transaction and attempt to reconstruct its full chain — supplier, movement, and customer — using only the existing records.
```

## G05-STOCK_DROPSHIPPING-Q046

```yaml
QID: G05-STOCK_DROPSHIPPING-Q046
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A supplier invoice that arrives for a quantity not matching any existing customer order line surfaces as a clear exception requiring resolution, rather than being capable of silently attaching itself to the wrong transaction with nothing to catch the mismatch.
WHY_IT_MATTERS: >
  With no independent physical count to catch a mismatched invoice, a silent wrong attachment can misstate the cost of an unrelated, otherwise-correct transaction with nothing prompting anyone to check.
DISCONFIRMING_OBSERVATION: >
  A supplier invoice with a quantity that matches no existing customer order line is nonetheless attached to some transaction with no exception or flag raised about the mismatch.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Submit a supplier invoice quantity that does not correspond to any real customer order line and observe what the system does with it.
```

## G05-STOCK_DROPSHIPPING-Q047

```yaml
QID: G05-STOCK_DROPSHIPPING-Q047
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a drop-shipped line's customer-side price is part of a bundled or promotional pricing structure, the supplier's cost for that line can still be mapped cleanly to that specific line's share of revenue, so whether that particular line was profitable remains answerable.
WHY_IT_MATTERS: >
  If bundling breaks the per-line cost-to-revenue link, a business selling bundles that include drop-shipped components loses the ability to know which specific items in the bundle are actually profitable.
DISCONFIRMING_OBSERVATION: >
  A drop-shipped line inside a bundled or promotional price cannot be matched to its own supplier cost to determine whether that specific line was profitable.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Sell a drop-shipped item as part of a bundled or promotional price, and check whether that specific line's margin can still be independently determined.
```

## G05-STOCK_DROPSHIPPING-Q048

```yaml
QID: G05-STOCK_DROPSHIPPING-Q048
MODULE: stock_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deactivating or delisting a supplier record does not retroactively affect a drop-ship order to that supplier that is already open and mid-fulfillment; the in-flight order remains protected until it reaches its own resolution.
WHY_IT_MATTERS: >
  A supplier record going inactive for future ordering reasons should never silently orphan a transaction that already has real goods moving under it.
DISCONFIRMING_OBSERVATION: >
  An in-progress drop-ship order to a supplier is disrupted, blocked, or loses tracking of its state at the moment that supplier's record is deactivated.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Open a drop-ship order to a supplier, then deactivate that supplier's record while the order is still mid-fulfillment, and check what happens to the open order.
```
