# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_gelato_stock Module MVQ Bank

**Document ID:** GMVQ-G08-SALE_GELATO_STOCK-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_gelato_stock`
**Wave:** W2
**Author Cell:** GMVQ PRODUCTION TEAM P-S10
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This bank supplies the module-specific MVQ set for `sale_gelato_stock`, the seam where an external
on-demand production and fulfilment provider's output meets your own stock records. Per the G08
SALES group brief this module is a bridge: it owns almost no behaviour of its own, and every
question below fails only where the defining condition applies — goods you never physically held
must still be reflected correctly in inventory and valuation, or deliberately must not be. Ground
covered includes whether a movement is recorded at all for goods that never entered a location and
what that record actually claims, what availability and available-to-promise mean for an item
produced on demand rather than held as a finite quantity, what happens to a movement already
created when the provider then fails to ship, lot or serial traceability for a unit made by someone
else, the valuation of an item that only ever existed in transit, a physical return arriving for an
item that never physically left, reconciling the provider's own reported shipped quantity against
your recorded movements, the accounting period a movement and its corresponding provider charge
land in, whether stock and sales reports correctly include or exclude on-demand items, and which
source fulfils an order for a product offered both from your own stock and through the provider.
Every question passes the seam test: if the item were instead drawn from stock you actually held in
one of your own locations, the question would no longer make sense; a question that would still
make sense either way was cut during authoring rather than included. Coverage is spread across
business capability, business rule, state transition, configuration dependency, role and
permission, exception path, cancellation, reversal, negative case, cross-module dependency,
optional behaviour, auditability, tenant/company boundary, concurrency and ordering, runtime
reachability, configuration reachability, and source/runtime contradiction potential. This bank
supplements the 55-question Standard bank; combined research depth for this module is
55 + 48 = 103.

This module is deliberately distinguished from the existing `stock_dropshipping` bank in the same
programme: dropshipping concerns an already-existing catalogue item shipped from a third-party
supplier's own pre-existing stock, with the supplier acting purely as an alternate stock source for
an otherwise ordinary product. This module's defining condition is that the item is manufactured
specifically for the order, typically personalised, and the "stock" question is not about sourcing
an existing item from elsewhere but about how to represent, value and report on goods that pass
through a genuine production step outside your own operation and never occupy a location you
control at any point in their existence. No question in this bank restates a dropshipping question
with the noun changed; the sibling bank's HYPOTHESIS lines were read in full before authoring and
none is duplicated here. This module is also distinguished from its own sibling `sale_gelato`
bank in this group: that bank fails at the commercial and production relationship with the
provider (pricing, personalisation content, cancellation, delivery evidence, catalogue volatility,
credentials, invoicing, privacy); this bank fails only where that relationship's output meets
your stock, valuation, traceability and reporting records.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses; none was
  trimmed or stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table,
  field, method, XML ID, API path), and the module's own metadata name never appears outside the
  `MODULE:` field — "the external on-demand production and fulfilment provider" (or "the
  provider" once established within a question) stands in for it throughout.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_GELATO_STOCK-Q001

```yaml
QID: G08-SALE_GELATO_STOCK-Q001
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A sale fulfilled entirely through the external on-demand production and fulfilment provider still produces a stock movement record reflecting that the goods left directly from the provider, distinctly marked as never having physically entered one of your own locations, rather than either no movement being recorded at all or a movement being recorded as if it had passed through your own location.
WHY_IT_MATTERS: >
  If no movement is recorded, the sale is invisible to any process that depends on stock movement history; if it is recorded as a normal internal movement, later reports will wrongly imply physical custody that never occurred.
DISCONFIRMING_OBSERVATION: >
  A completed sale fulfilled by the provider produces either no stock movement record at all, or one indistinguishable from a movement that physically passed through one of your own locations.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Complete a sale fulfilled entirely by the provider and inspect what stock movement record, if any, results and how it is marked.
```

## G08-SALE_GELATO_STOCK-Q002

```yaml
QID: G08-SALE_GELATO_STOCK-Q002
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The location representing goods fulfilled by the external on-demand production and fulfilment provider is a distinct, identifiable point in your stock configuration rather than an unlabelled or generic point indistinguishable from other movement types.
WHY_IT_MATTERS: >
  Without a distinct, identifiable point, movements from provider-fulfilled sales cannot be separated from other kinds of movement for any later analysis.
DISCONFIRMING_OBSERVATION: >
  The point representing provider-fulfilled goods in the stock configuration cannot be distinguished from the point used for an entirely different kind of movement.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Inspect the stock configuration used for provider-fulfilled sales and determine whether it is distinctly identifiable from other movement types.
```

## G08-SALE_GELATO_STOCK-Q003

```yaml
QID: G08-SALE_GELATO_STOCK-Q003
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the process generating a stock movement for a sale fulfilled by the external on-demand production and fulfilment provider is retried after an error, it does not create a second, duplicate movement record for the same original sale.
WHY_IT_MATTERS: >
  A duplicate movement for goods that never physically existed on your side would misstate stock activity twice over for a single real transaction.
DISCONFIRMING_OBSERVATION: >
  Retrying the movement-generation process after a simulated error produces two movement records for what was a single sale.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Simulate an error partway through generating a stock movement for a provider-fulfilled sale, retry the process, and check whether one or two movement records result.
```

## G08-SALE_GELATO_STOCK-Q004

```yaml
QID: G08-SALE_GELATO_STOCK-Q004
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The stock movement record generated for a provider-fulfilled sale retains a traceable link back to the specific transaction with the external on-demand production and fulfilment provider that it represents, rather than existing as a standalone record with no way to trace its origin.
WHY_IT_MATTERS: >
  Without that link, a later question about why a specific movement exists, or which provider transaction it corresponds to, cannot be answered.
DISCONFIRMING_OBSERVATION: >
  A stock movement record for a provider-fulfilled sale cannot be traced back to the specific provider transaction that produced it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate a movement for a provider-fulfilled sale and attempt to trace it back to the specific provider transaction it represents.
```

## G08-SALE_GELATO_STOCK-Q005

```yaml
QID: G08-SALE_GELATO_STOCK-Q005
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The state of the stock movement representing a provider-fulfilled sale advances in step with the real production and shipping progress reported by the external on-demand production and fulfilment provider, rather than being set to a completed state immediately at order time regardless of whether anything has actually shipped yet.
WHY_IT_MATTERS: >
  A movement marked complete before anything has actually shipped misrepresents stock activity as having already happened when it has not.
DISCONFIRMING_OBSERVATION: >
  A stock movement for a provider-fulfilled sale shows a completed state at the moment of order confirmation, before the provider has reported any actual shipment.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Place a provider-fulfilled order and check the movement's state at order confirmation versus after the provider actually reports shipment.
```

## G08-SALE_GELATO_STOCK-Q006

```yaml
QID: G08-SALE_GELATO_STOCK-Q006
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An item fulfilled on demand by the external on-demand production and fulfilment provider is not counted within any calculation of physically available stock in a location you control, since no finite quantity of it is actually held there.
WHY_IT_MATTERS: >
  Counting an on-demand item as reservable physical stock could let it be allocated against, or compete for, capacity that does not actually exist in your own location.
DISCONFIRMING_OBSERVATION: >
  An on-demand item appears within a calculation or report of physically available stock in one of your own locations as though a countable quantity of it were actually held there.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Inspect a report or calculation of physically available stock and check whether an on-demand item appears in it as reservable physical quantity.
```

## G08-SALE_GELATO_STOCK-Q007

```yaml
QID: G08-SALE_GELATO_STOCK-Q007
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  What is shown to the customer as available-to-promise for an on-demand item reflects a deliberately configured stance about the external on-demand production and fulfilment provider's own production capability, rather than being whatever an unrelated stock-based calculation happens to produce by accident for an item with no physical stock.
WHY_IT_MATTERS: >
  An accidental availability figure derived from a calculation meant for physically stocked items could show an on-demand item as unavailable, blocking sales the business could actually fulfil, or as available with no real basis at all.
DISCONFIRMING_OBSERVATION: >
  The availability shown to a customer for an on-demand item is a byproduct of a stock calculation intended for physically held items, with no deliberate configuration governing what it should show instead.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Inspect what availability figure or message is shown for an on-demand item and trace whether it comes from a deliberate configuration or an incidental calculation.
```

## G08-SALE_GELATO_STOCK-Q008

```yaml
QID: G08-SALE_GELATO_STOCK-Q008
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the external on-demand production and fulfilment provider itself signals a capacity constraint or backlog affecting a catalogue item, that constraint is reflected somewhere in what is shown or promised for that item, rather than availability always being presented as unconstrained regardless of the provider's own signal.
WHY_IT_MATTERS: >
  Presenting unlimited availability while the provider itself is constrained sets a customer expectation the business cannot actually meet.
DISCONFIRMING_OBSERVATION: >
  The provider reports a capacity constraint for a catalogue item, and nothing shown to the customer or to staff reflects that constraint afterward.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Simulate the provider signalling a capacity constraint on a catalogue item and check whether anything shown for that item changes as a result.
```

## G08-SALE_GELATO_STOCK-Q009

```yaml
QID: G08-SALE_GELATO_STOCK-Q009
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Availability calculated for an item produced on demand by the external on-demand production and fulfilment provider does not interact with, consume, or get blocked by stock reservations made for conventionally stocked items, since the two represent fundamentally different kinds of supply.
WHY_IT_MATTERS: >
  If the two are not kept separate, a reservation against real physical stock could incorrectly affect what is shown as available for an item that was never drawing from that same stock.
DISCONFIRMING_OBSERVATION: >
  Reserving quantity of a conventionally stocked item changes the availability shown for an unrelated on-demand item, or vice versa, with no shared cause justifying the interaction.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve quantity against a conventionally stocked item and check whether the availability shown for an unrelated on-demand item changes as a result.
```

## G08-SALE_GELATO_STOCK-Q010

```yaml
QID: G08-SALE_GELATO_STOCK-Q010
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a stock movement has already been recorded for a provider-fulfilled sale and the external on-demand production and fulfilment provider then fails to ship it, the movement is cancelled or reversed to reflect that nothing actually moved, rather than being left standing as though the goods had shipped.
WHY_IT_MATTERS: >
  A standing movement for goods that were never actually shipped misstates stock activity and any downstream report or reconciliation built on it.
DISCONFIRMING_OBSERVATION: >
  A stock movement remains in a completed state after the provider has reported that it will not ship the goods the movement represents.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Record a movement for a provider-fulfilled sale, then have the provider report a shipping failure, and check whether the movement is reversed or left standing.
```

## G08-SALE_GELATO_STOCK-Q011

```yaml
QID: G08-SALE_GELATO_STOCK-Q011
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a movement is reversed because the external on-demand production and fulfilment provider failed to ship, that reversal is recorded as a distinct, traceable event rather than the original movement simply being deleted with no trace that it ever existed or was undone.
WHY_IT_MATTERS: >
  Silent deletion of a failed movement removes the evidence a later audit would need to understand what happened and why.
DISCONFIRMING_OBSERVATION: >
  A movement known to have been reversed due to a provider shipping failure leaves no retrievable trace that it ever existed or was reversed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger a provider shipping failure on an order with an already-recorded movement, and check whether the reversal leaves a retrievable trace.
```

## G08-SALE_GELATO_STOCK-Q012

```yaml
QID: G08-SALE_GELATO_STOCK-Q012
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A shipping failure reported by the external on-demand production and fulfilment provider after the accounting period in which the original movement was recorded has already closed can still be reflected against that specific, already-closed movement, rather than falling outside any period the correction can still be applied to.
WHY_IT_MATTERS: >
  If a late-reported failure cannot be corrected against its original period, the stock and valuation impact of goods that never actually shipped permanently overstates that closed period.
DISCONFIRMING_OBSERVATION: >
  A shipping failure reported after period close cannot be linked to or corrected against the specific movement it invalidates.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a movement in one period, close that period, then report a provider shipping failure for that same movement, and trace whether a correction can still be applied.
```

## G08-SALE_GELATO_STOCK-Q013

```yaml
QID: G08-SALE_GELATO_STOCK-Q013
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the external on-demand production and fulfilment provider ships only some units of a multi-unit order line, the stock movement reflects that partial quantity actually shipped, rather than the movement being forced into an all-shipped or all-failed state that misrepresents the split.
WHY_IT_MATTERS: >
  An all-or-nothing movement for a partially shipped line either overstates what actually left the provider or understates the portion that genuinely did ship.
DISCONFIRMING_OBSERVATION: >
  A line where the provider shipped only part of the ordered quantity results in a movement showing either the full quantity or none of it as shipped.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have the provider report a partial shipment against a multi-unit line and inspect whether the resulting movement reflects the actual split quantity.
```

## G08-SALE_GELATO_STOCK-Q014

```yaml
QID: G08-SALE_GELATO_STOCK-Q014
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where an item type would normally require lot or batch identity to be tracked, a unit produced by the external on-demand production and fulfilment provider either has that identity captured through information the provider supplies, or the system explicitly records that the identity could not be captured, rather than silently defaulting to no tracking at all.
WHY_IT_MATTERS: >
  Silently skipping lot tracking for provider-produced units defeats the purpose of tracking that item type at all, and would be invisible until a recall made the gap matter.
DISCONFIRMING_OBSERVATION: >
  A unit of a lot-tracked item type fulfilled by the provider carries no lot identity and no record explaining why none was captured.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Complete a provider-fulfilled sale of an item type that would normally require lot tracking, and check whether a lot identity, or an explicit note of its absence, is recorded.
```

## G08-SALE_GELATO_STOCK-Q015

```yaml
QID: G08-SALE_GELATO_STOCK-Q015
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a lot identity is captured for a unit fulfilled by the external on-demand production and fulfilment provider, that identity remains linked to the specific customer who received it, so that a later recall affecting that lot can be traced through to the affected customer using the existing records.
WHY_IT_MATTERS: >
  A lot identity with no link to the receiving customer is useless the moment a recall actually needs to reach that customer.
DISCONFIRMING_OBSERVATION: >
  A lot identity is captured for a provider-fulfilled unit, but no retrievable record connects that lot to the specific customer who received it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Capture a lot identity for a provider-fulfilled unit, then attempt to trace from that lot to the specific customer who received it.
```

## G08-SALE_GELATO_STOCK-Q016

```yaml
QID: G08-SALE_GELATO_STOCK-Q016
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether lot or serial identity is expected to be captured for a provider-fulfilled item is configured per product according to that product's own tracking requirement, rather than being a single fixed behaviour applied uniformly to every item the external on-demand production and fulfilment provider fulfils regardless of type.
WHY_IT_MATTERS: >
  A single fixed behaviour either forces unnecessary tracking overhead onto items that do not need it, or silently skips tracking for items that do.
DISCONFIRMING_OBSERVATION: >
  Two provider-fulfilled products with different stated tracking requirements are handled with the identical lot or serial capture behaviour regardless of that difference.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Compare the lot or serial capture behaviour for two provider-fulfilled products with different stated tracking requirements.
```

## G08-SALE_GELATO_STOCK-Q017

```yaml
QID: G08-SALE_GELATO_STOCK-Q017
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Given a specific unit fulfilled by the external on-demand production and fulfilment provider, the existing records can reconstruct, end to end, which of its transactions produced the unit, when it moved, and which customer received it, even though no physical custody checkpoint of your own was ever created for it.
WHY_IT_MATTERS: >
  Without an end-to-end reconstruction, a serious traceability question — such as a safety recall — has no complete answer for provider-fulfilled units specifically.
DISCONFIRMING_OBSERVATION: >
  For a specific provider-fulfilled unit, the existing records cannot be assembled into a complete chain from production through to the receiving customer.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Select a specific provider-fulfilled unit and attempt to reconstruct its full chain of custody from the existing records alone.
```

## G08-SALE_GELATO_STOCK-Q018

```yaml
QID: G08-SALE_GELATO_STOCK-Q018
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A valuation entry is created for an item fulfilled by the external on-demand production and fulfilment provider at a point consistent with your normal costing timing, rather than being omitted altogether on the reasoning that the item never occupied a physical location of your own.
WHY_IT_MATTERS: >
  Omitting valuation entirely for provider-fulfilled sales would understate cost of goods sold and misstate margin for every such transaction.
DISCONFIRMING_OBSERVATION: >
  A completed provider-fulfilled sale shows no valuation entry anywhere, in contrast to how a conventionally stocked sale is valued.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a provider-fulfilled sale and a conventionally stocked sale, and compare whether each produces a valuation entry.
```

## G08-SALE_GELATO_STOCK-Q019

```yaml
QID: G08-SALE_GELATO_STOCK-Q019
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An item fulfilled by the external on-demand production and fulfilment provider does not receive more than one valuation posting for the same unit sold, even where its movement passes through more than one recorded state on the way to completion.
WHY_IT_MATTERS: >
  A duplicated valuation posting for the same physical unit overstates cost of goods sold and distorts reported margin.
DISCONFIRMING_OBSERVATION: >
  A single provider-fulfilled unit shows two separate valuation postings corresponding to the same underlying transaction.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Trace a provider-fulfilled unit through every state its movement passes through and count how many valuation postings result.
```

## G08-SALE_GELATO_STOCK-Q020

```yaml
QID: G08-SALE_GELATO_STOCK-Q020
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A provider-fulfilled item that has been produced and shipped by the external on-demand production and fulfilment provider but not yet delivered is not valued as though it were on-hand stock sitting in one of your own locations, since it never actually occupies one.
WHY_IT_MATTERS: >
  Valuing an in-transit, provider-held item as though it were your own on-hand stock overstates the inventory asset your business actually holds.
DISCONFIRMING_OBSERVATION: >
  An item shipped by the provider but not yet delivered to the customer appears in a valuation of on-hand stock at one of your own locations.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Identify a provider-fulfilled item that has shipped but not yet been delivered, and check whether it appears in any on-hand valuation for one of your own locations.
```

## G08-SALE_GELATO_STOCK-Q021

```yaml
QID: G08-SALE_GELATO_STOCK-Q021
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A historical inventory valuation or on-hand report generated for a past date correctly excludes provider-fulfilled items from appearing as on-hand stock, including for a date falling between the order being placed and the external on-demand production and fulfilment provider actually shipping it, in every report or view that reflects quantity or value, not only the primary one.
WHY_IT_MATTERS: >
  An inconsistency between reports would let a secondary view overstate historical inventory even when the primary report is correct.
DISCONFIRMING_OBSERVATION: >
  A historical report for a past date shows a provider-fulfilled item as on-hand stock in at least one view, even though the primary report correctly excludes it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate more than one historical inventory view for a past date falling within a provider order's production window, and check each for the presence of that item as on-hand stock.
```

## G08-SALE_GELATO_STOCK-Q022

```yaml
QID: G08-SALE_GELATO_STOCK-Q022
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cost adjustment reported by the external on-demand production and fulfilment provider after its transaction's normal accounting period has already closed can still be attached to that specific, already-closed transaction's valuation, rather than falling outside any period the correction can still be applied to.
WHY_IT_MATTERS: >
  An adjustment that cannot be attached to its own transaction after close either gets lost or gets misapplied to an unrelated period.
DISCONFIRMING_OBSERVATION: >
  A late cost adjustment from the provider cannot be linked to, or correctly applied against, the specific closed transaction it actually belongs to.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Close the accounting period for a provider-fulfilled transaction, then introduce a late cost adjustment from the provider for that same transaction, and trace whether it can still be applied correctly.
```

## G08-SALE_GELATO_STOCK-Q023

```yaml
QID: G08-SALE_GELATO_STOCK-Q023
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A customer return of an item fulfilled by the external on-demand production and fulfilment provider that physically arrives at one of your own locations is recognisable, at the point of receipt, as an item your own stock records never show as having left that location in the first place, rather than being processed identically to an ordinary return of previously-held stock.
WHY_IT_MATTERS: >
  Processing it identically to an ordinary return would create a receipt with no corresponding original shipment for it to reverse, leaving the stock record internally inconsistent.
DISCONFIRMING_OBSERVATION: >
  A return of a provider-fulfilled item is received and processed with no distinction from an ordinary return, despite your own stock records showing it never left your location to begin with.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Process the physical return of a provider-fulfilled item at one of your own locations and compare the handling against an ordinary return of previously-held stock.
```

## G08-SALE_GELATO_STOCK-Q024

```yaml
QID: G08-SALE_GELATO_STOCK-Q024
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A returned item fulfilled by the external on-demand production and fulfilment provider, once physically received, is assigned an explicit stock disposition reflecting that it was personalised or made to order, rather than defaulting silently to the same resalable status given to an ordinary returned item.
WHY_IT_MATTERS: >
  Defaulting a personalised return to resalable status risks it being sold to a customer it was never made for.
DISCONFIRMING_OBSERVATION: >
  A returned provider-fulfilled item is assigned a resalable stock status with no distinct disposition decision reflecting that it was made to order.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Receive a returned provider-fulfilled item and check what stock disposition it is assigned.
```

## G08-SALE_GELATO_STOCK-Q025

```yaml
QID: G08-SALE_GELATO_STOCK-Q025
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The valuation reversal recorded for a returned item fulfilled by the external on-demand production and fulfilment provider is consistent with, and does not exceed, the original valuation posted for that item's sale, even though the item is only now physically arriving in your location for the first time.
WHY_IT_MATTERS: >
  A reversal not tied back to the original transaction's own valuation could overstate or understate the actual financial impact of the return.
DISCONFIRMING_OBSERVATION: >
  The valuation reversal recorded for a returned provider-fulfilled item exceeds, or bears no traceable relationship to, the amount originally valued for that item's sale.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Process a return of a provider-fulfilled item and compare the resulting valuation reversal against the original valuation posted for its sale.
```

## G08-SALE_GELATO_STOCK-Q026

```yaml
QID: G08-SALE_GELATO_STOCK-Q026
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The quantity the external on-demand production and fulfilment provider reports as shipped over a given period can be reconciled against the quantity your own stock movements recorded as shipped for that same period, rather than the two figures having no defined way to be compared.
WHY_IT_MATTERS: >
  Without a way to compare the two figures, a systematic gap between what the provider says it shipped and what your own records show could persist undetected indefinitely.
DISCONFIRMING_OBSERVATION: >
  There is no way to line up the provider's own reported shipped quantity for a period against your own recorded movement quantity for that same period.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Obtain the provider's reported shipped quantity for a period and attempt to reconcile it against your own recorded stock movements for that same period.
```

## G08-SALE_GELATO_STOCK-Q027

```yaml
QID: G08-SALE_GELATO_STOCK-Q027
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A discrepancy found between the external on-demand production and fulfilment provider's reported shipped quantity and your own recorded movement quantity is surfaced as an exception requiring investigation, rather than one of the two figures being silently adjusted to match the other with no record of the disagreement.
WHY_IT_MATTERS: >
  Silently overwriting one figure to match the other destroys the evidence that a real discrepancy, potentially indicating a billing or fulfilment error, ever occurred.
DISCONFIRMING_OBSERVATION: >
  A known discrepancy between the provider's reported quantity and your own recorded quantity results in one figure being adjusted with no retained record that a discrepancy was ever found.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Introduce a known discrepancy between the provider's reported quantity and your own recorded movement quantity, and observe how it is surfaced or resolved.
```

## G08-SALE_GELATO_STOCK-Q028

```yaml
QID: G08-SALE_GELATO_STOCK-Q028
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Reconciliation between the external on-demand production and fulfilment provider's reported shipped quantity and your own recorded movements occurs on a defined, recurring basis, rather than depending on a staff member remembering to perform it manually with no schedule behind it.
WHY_IT_MATTERS: >
  A reconciliation that depends entirely on someone remembering to run it will eventually be skipped, and a growing discrepancy will go undetected for longer each time.
DISCONFIRMING_OBSERVATION: >
  No defined recurring process exists for reconciling the provider's reported quantity against your own recorded movements; it happens only if a staff member initiates it manually.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Determine whether reconciliation between provider-reported and internally-recorded quantity is triggered by a defined schedule or depends entirely on manual initiation.
```

## G08-SALE_GELATO_STOCK-Q029

```yaml
QID: G08-SALE_GELATO_STOCK-Q029
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a single reported shipment from the external on-demand production and fulfilment provider covers multiple customer orders, reconciliation can be performed at the level of each individual order's own movement, rather than only being possible in aggregate across the whole consolidated shipment.
WHY_IT_MATTERS: >
  Aggregate-only reconciliation could conceal a discrepancy affecting one specific order within an otherwise-matching consolidated shipment.
DISCONFIRMING_OBSERVATION: >
  A discrepancy affecting one order within a multi-order consolidated shipment cannot be isolated because reconciliation is only possible at the aggregate shipment level.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reconcile a consolidated provider shipment covering multiple orders and check whether the reconciliation can be performed at the level of each individual order.
```

## G08-SALE_GELATO_STOCK-Q030

```yaml
QID: G08-SALE_GELATO_STOCK-Q030
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The accounting period in which a stock movement fulfilled by the external on-demand production and fulfilment provider is recorded, and the period in which its corresponding charge from that provider is recognised, are either the same period, or, where they differ, that difference is identifiable rather than hidden inside two unrelated figures.
WHY_IT_MATTERS: >
  An unidentifiable timing mismatch between the movement and its cost prevents anyone from later explaining why a period's stock activity and its costs do not line up.
DISCONFIRMING_OBSERVATION: >
  A provider-fulfilled movement's period and its corresponding cost's period differ with no way to identify that a difference exists or what caused it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Arrange for a provider-fulfilled movement and its corresponding cost to land in different periods, and check whether that difference can be identified from the records.
```

## G08-SALE_GELATO_STOCK-Q031

```yaml
QID: G08-SALE_GELATO_STOCK-Q031
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a movement fulfilled by the external on-demand production and fulfilment provider and recorded in one period is later found, after that period has closed, to correspond to goods that were never actually shipped, a correction path exists that reaches back to affect that specific movement rather than the error remaining permanently embedded in a closed period with no route to fix it.
WHY_IT_MATTERS: >
  An error with no correction path permanently misstates a closed period's stock and cost figures with no way to ever fix it.
DISCONFIRMING_OBSERVATION: >
  A movement discovered after period close to represent goods that never shipped has no available path to correct it against that closed period.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Close a period containing a provider-fulfilled movement, then discover that the underlying goods never actually shipped, and check whether a correction path exists.
```

## G08-SALE_GELATO_STOCK-Q032

```yaml
QID: G08-SALE_GELATO_STOCK-Q032
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Once a movement fulfilled by the external on-demand production and fulfilment provider has been booked into a specific accounting period, that period assignment is preserved and does not silently shift to a different period if the movement record is later touched again for an unrelated reason.
WHY_IT_MATTERS: >
  A period assignment that can silently shift undermines any historical report that already relied on the movement being in its originally booked period.
DISCONFIRMING_OBSERVATION: >
  A movement's period assignment changes after an unrelated later edit to the movement record, with nothing having deliberately triggered a period reassignment.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Book a provider-fulfilled movement into a period, make an unrelated later edit to the movement record, and check whether its period assignment is preserved.
```

## G08-SALE_GELATO_STOCK-Q033

```yaml
QID: G08-SALE_GELATO_STOCK-Q033
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A stock or sales report that includes items fulfilled by the external on-demand production and fulfilment provider clearly distinguishes them from items that actually moved through one of your own locations, rather than presenting both kinds of activity under a single undifferentiated figure.
WHY_IT_MATTERS: >
  A conflated figure makes it impossible to separately judge the performance of on-demand fulfilment from the performance of your own physical operation.
DISCONFIRMING_OBSERVATION: >
  A stock or sales report presents provider-fulfilled and physically-moved items under one combined figure with no way to distinguish the two.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate a stock or sales report covering a period with both provider-fulfilled and physically-moved items, and check whether the two are distinguishable.
```

## G08-SALE_GELATO_STOCK-Q034

```yaml
QID: G08-SALE_GELATO_STOCK-Q034
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  For each standard stock report, whether it includes or excludes items fulfilled by the external on-demand production and fulfilment provider is a documented, deliberate choice specific to that report's purpose, rather than an incidental side effect of how the report happens to be built.
WHY_IT_MATTERS: >
  An undocumented, incidental inclusion or exclusion means nobody can say with confidence whether a given report's figures are meant to reflect on-demand activity or not.
DISCONFIRMING_OBSERVATION: >
  A standard stock report's inclusion or exclusion of provider-fulfilled items cannot be traced to any documented, deliberate design choice for that report.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Inspect a standard stock report for whether it includes provider-fulfilled items, and check whether that behaviour is documented as deliberate.
```

## G08-SALE_GELATO_STOCK-Q035

```yaml
QID: G08-SALE_GELATO_STOCK-Q035
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two different reports drawing on the same underlying period of sales activity, one of which includes items fulfilled by the external on-demand production and fulfilment provider and the other of which is expected to reconcile with it, actually agree once the treatment of those items in each is accounted for.
WHY_IT_MATTERS: >
  Two reports that should reconcile but silently do not, because of an unstated difference in how they treat on-demand items, undermines trust in either figure.
DISCONFIRMING_OBSERVATION: >
  Two reports covering the same period and the same underlying activity produce different totals with the difference traceable only to an undocumented difference in how each treats provider-fulfilled items.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate two reports expected to reconcile for the same period, one of which reflects provider-fulfilled items differently, and compare their totals.
```

## G08-SALE_GELATO_STOCK-Q036

```yaml
QID: G08-SALE_GELATO_STOCK-Q036
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where the same product can be fulfilled either from your own stock or through the external on-demand production and fulfilment provider, an explicit, defined rule determines which source fulfils a given order, rather than the choice being made inconsistently or left undetermined.
WHY_IT_MATTERS: >
  An undefined choice of source could result in an order fulfilled from the more expensive or slower path when the cheaper or faster one was actually available, with nobody having decided that outcome on purpose.
DISCONFIRMING_OBSERVATION: >
  Two otherwise-identical orders for a dual-sourced product are fulfilled from two different sources with no discoverable rule explaining why.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Place two otherwise-identical orders for a product available from both your own stock and the provider, and determine what rule, if any, governs which source fulfils each.
```

## G08-SALE_GELATO_STOCK-Q037

```yaml
QID: G08-SALE_GELATO_STOCK-Q037
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If your own physical stock for a dual-sourced product is exhausted while the product is still being offered for sale, new orders are either routed to the external on-demand production and fulfilment provider or the product is prevented from further sale from that exhausted source, rather than being allowed to oversell against stock that no longer exists.
WHY_IT_MATTERS: >
  Overselling against exhausted physical stock with no fallback and no block leaves an order that nothing can actually fulfil.
DISCONFIRMING_OBSERVATION: >
  A new order for a dual-sourced product is accepted against your own stock after that stock is already exhausted, with no failover to the provider and no block on the sale.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Exhaust your own stock for a dual-sourced product while it remains offered for sale, then place a new order and observe what source it is fulfilled from.
```

## G08-SALE_GELATO_STOCK-Q038

```yaml
QID: G08-SALE_GELATO_STOCK-Q038
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  For a dual-sourced product, whether a completed order was actually fulfilled from your own stock or through the external on-demand production and fulfilment provider remains recorded and retrievable after the transaction is finished, rather than the finished record looking identical either way.
WHY_IT_MATTERS: >
  Without that record, the business cannot analyse how often each source is actually being used, or investigate a problem traced to one source specifically.
DISCONFIRMING_OBSERVATION: >
  A completed order for a dual-sourced product gives no way to determine afterward which source actually fulfilled it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete an order for a dual-sourced product and attempt to determine afterward which source actually fulfilled it.
```

## G08-SALE_GELATO_STOCK-Q039

```yaml
QID: G08-SALE_GELATO_STOCK-Q039
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A multi-unit order for a dual-sourced product that is actually fulfilled using both your own stock and the external on-demand production and fulfilment provider together is represented in the record as a genuine split between the two sources, rather than being forced to appear as though only one source fulfilled the entire quantity.
WHY_IT_MATTERS: >
  Forcing a split fulfilment to appear single-sourced hides the true cost and traceability mix behind that order.
DISCONFIRMING_OBSERVATION: >
  An order genuinely fulfilled using both sources is recorded as though only one source fulfilled the entire quantity.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Fulfil a multi-unit order for a dual-sourced product using a mix of your own stock and the provider, and check whether the record reflects the actual split.
```

## G08-SALE_GELATO_STOCK-Q040

```yaml
QID: G08-SALE_GELATO_STOCK-Q040
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a shipment confirmation from the external on-demand production and fulfilment provider and a manual correction to the same stock movement are both applied at close to the same time, the movement ends in one defined, consistent state rather than whichever update happened to apply last silently overwriting the other with no record of the conflict.
WHY_IT_MATTERS: >
  An unresolved race between an automatic provider update and a manual correction could leave a movement in a state nobody actually intended, with no trace that a conflict occurred.
DISCONFIRMING_OBSERVATION: >
  Applying a provider shipment confirmation and a manual correction to the same movement in close succession leaves the movement in a state that matches neither update as documented, with no record that both were attempted.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Apply a provider shipment confirmation and a manual correction to the same movement in close succession and inspect the resulting state and any record of the conflict.
```

## G08-SALE_GELATO_STOCK-Q041

```yaml
QID: G08-SALE_GELATO_STOCK-Q041
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a provider-fulfilled sale's fulfilment is cancelled after its stock valuation entry has
  already been posted, a reversing entry is produced that unwinds the valuation, rather than the
  original valuation entry standing against a fulfilment that no longer occurred.
WHY_IT_MATTERS: >
  A cancelled fulfilment that leaves its valuation entry standing overstates the business's
  recorded inventory cost for output that was never actually produced or delivered.
DISCONFIRMING_OBSERVATION: >
  A provider fulfilment is cancelled after its valuation entry was posted, and no reversing entry
  appears -- the original valuation entry remains as the only record of it.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Complete a provider-fulfilled sale through the point its valuation entry is posted, then cancel
  that fulfilment with the provider, and check whether a reversing entry is produced.
```

## G08-SALE_GELATO_STOCK-Q042

```yaml
QID: G08-SALE_GELATO_STOCK-Q042
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  In a multi-tenant deployment, the stock location and movement records representing one tenant's sales fulfilled by the external on-demand production and fulfilment provider are not visible to, or reachable from, a process or report scoped to a different tenant.
WHY_IT_MATTERS: >
  Cross-tenant visibility into provider-fulfilled stock activity would expose one tenant's sales volume and customer fulfilment pattern to another tenant.
DISCONFIRMING_OBSERVATION: >
  A report or process scoped to one tenant is able to retrieve or display stock movement records belonging to a different tenant's provider-fulfilled sales.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  In a multi-tenant configuration, attempt to retrieve provider-fulfilled stock movement records for one tenant from a process or report scoped to a different tenant.
```

## G08-SALE_GELATO_STOCK-Q043

```yaml
QID: G08-SALE_GELATO_STOCK-Q043
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Visibility into the cost or valuation figure attached to the stock movement of an item fulfilled by the external on-demand production and fulfilment provider is governed by the same role-based permission that controls cost visibility for a conventionally stocked item, rather than being exposed more broadly because the movement sits outside the normal stock flow.
WHY_IT_MATTERS: >
  A cost figure exposed more broadly just because it arose from a different fulfilment path defeats the purpose of the normal permission control on cost data.
DISCONFIRMING_OBSERVATION: >
  A user without permission to see cost or valuation data for conventional stock can nonetheless see it for a provider-fulfilled item's movement.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Compare what a user without cost-visibility permission can see for a conventionally stocked item's valuation versus a provider-fulfilled item's valuation.
```

## G08-SALE_GELATO_STOCK-Q044

```yaml
QID: G08-SALE_GELATO_STOCK-Q044
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  If the product record representing a dual-sourced item, or one fulfilled by the external on-demand production and fulfilment provider, is archived or discontinued while a movement for it is still open and unresolved, that open movement is not silently orphaned or made unreachable by the product's own change in status.
WHY_IT_MATTERS: >
  An orphaned movement tied to an archived product could become permanently unresolved, misstating open stock activity with no way to close it out.
DISCONFIRMING_OBSERVATION: >
  Archiving the product record for an item with a still-open movement makes that movement unreachable or impossible to resolve afterward.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Archive or discontinue a product with a still-open provider-fulfilled movement and check whether that movement remains reachable and resolvable.
```

## G08-SALE_GELATO_STOCK-Q045

```yaml
QID: G08-SALE_GELATO_STOCK-Q045
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an order is cancelled after its stock movement has already been created but before the external on-demand production and fulfilment provider has shipped anything, the movement is reversed to reflect the cancellation, rather than remaining recorded as though the goods were still going to move.
WHY_IT_MATTERS: >
  A movement left standing after its own order was cancelled misstates pending stock activity for an order that will never actually complete.
DISCONFIRMING_OBSERVATION: >
  An order is cancelled before the provider ships anything, but its stock movement remains in an active, unreversed state afterward.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Create a movement for an order, cancel the order before the provider reports any shipment, and check whether the movement is reversed.
```

## G08-SALE_GELATO_STOCK-Q046

```yaml
QID: G08-SALE_GELATO_STOCK-Q046
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the external on-demand production and fulfilment provider's charge for an item is in a different currency than your stock valuation is kept in, the valuation posting uses a documented, consistent conversion point and rate, rather than an unspecified or inconsistently-timed conversion.
WHY_IT_MATTERS: >
  An inconsistent conversion point could make the recorded valuation of the same item differ depending only on when the conversion happened to be applied, with no substantive reason for the difference.
DISCONFIRMING_OBSERVATION: >
  Two otherwise-identical provider-fulfilled valuation postings, both converted from the same foreign charge, use two different, undocumented conversion rates or points with no stated reason.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post valuation for two provider-fulfilled items charged in a foreign currency and compare the conversion point and rate each posting used.
```

## G08-SALE_GELATO_STOCK-Q047

```yaml
QID: G08-SALE_GELATO_STOCK-Q047
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a single shipment from the external on-demand production and fulfilment provider contains more than one unit of a lot- or serial-tracked item, each unit's own identity is captured distinctly, rather than the whole shipment being recorded under one shared identity that could not later distinguish the individual units.
WHY_IT_MATTERS: >
  A shared identity across multiple units defeats the purpose of unit-level tracking the moment more than one unit needs to be told apart, such as in a partial recall.
DISCONFIRMING_OBSERVATION: >
  A shipment containing several units of a serial-tracked item is recorded under a single shared identity with no way to distinguish one unit from another afterward.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive a single provider shipment containing multiple units of a lot- or serial-tracked item and check whether each unit's identity is captured distinctly.
```

## G08-SALE_GELATO_STOCK-Q048

```yaml
QID: G08-SALE_GELATO_STOCK-Q048
MODULE: sale_gelato_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A product that is not configured for ordinary stock tracking, but is sold through the external on-demand production and fulfilment provider, still produces a cost or valuation record for that sale, rather than the absence of ordinary stock tracking also silently suppressing any cost recognition for the provider-fulfilled transaction.
WHY_IT_MATTERS: >
  If lacking stock tracking also suppresses cost recognition, a whole category of provider-fulfilled sales could go completely uncosted with nothing surfacing the gap.
DISCONFIRMING_OBSERVATION: >
  A provider-fulfilled sale of a product with no ordinary stock tracking enabled produces no cost or valuation record of any kind.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Sell a product with ordinary stock tracking disabled through the provider and check whether a cost or valuation record is produced.
```
