# SMEsPlus ENTERPRISE SUITE
## GMVQ — G05 INVENTORY / repair Module MVQ Bank

**Document ID:** GMVQ-G05-REPAIR-MVQ48-V1.00
**Group:** G05 INVENTORY
**Module Metadata:** `repair`
**Wave:** W2
**Author Cell:** TEAM P05 (GMVQ Production Team — Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies module-specific research questions (MVQ) for the corrective-work-order capability within G05 INVENTORY: an item taken out of stock, worked on, and returned, replaced or scrapped. It targets who owns the item while corrective work is underway; parts consumed against the work and how they are valued; the item returning under a different identity, lot or serial than it left with; a serial-tracked unit whose history must survive the process; corrective work performed on an item still under an active commercial commitment; when and against what the cost of the work is recognised; work abandoned midway with parts already consumed; scrapping the item after parts were consumed for it; a customer-owned item on the premises and what the company's own valuation must exclude; the quantity or unit of the returned item differing from what went in; a corrective-work order cancelled after partial work; and who may authorise a scrap decision and what trace it leaves. Coverage is spread across business capability, business rule, state transition, configuration dependency, role and permission, exception path, cancellation, reversal, negative case, cross-module dependency, optional behaviour, auditability, tenant/company boundary, concurrency and ordering, runtime reachability, configuration reachability, and source/runtime contradiction potential.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses; none was trimmed or stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table, field, method, XML ID, API path), and the module's own metadata name never appears outside the `MODULE:` field and the `QID` — the generic term "corrective-work order" stands in for it throughout, and "the unit under corrective work" stands in for the item concerned.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/evidence from Lane A or Lane B.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank alone.
- This document is PREPARED ONLY / NOT APPROVED / NOT FROZEN. It is not Boss Final Approval.

## G05-REPAIR-Q001

```yaml
QID: G05-REPAIR-Q001
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An item brought in under a customer's ownership for corrective work is not added to the servicing company's own valued on-hand stock quantity merely because it is physically present on the premises.
WHY_IT_MATTERS: >
  Counting a customer's property as the company's own stock would overstate inventory and misattribute value that was never the company's to begin with.
DISCONFIRMING_OBSERVATION: >
  A customer-owned item logged for corrective work appears in the servicing company's own valued on-hand stock total.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Log a customer-owned item into a corrective-work order and check whether the company's own valued on-hand stock total changes as a result.
LAYER: BASE
```

## G05-REPAIR-Q002

```yaml
QID: G05-REPAIR-Q002
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An item that is the servicing company's own stock does not implicitly change ownership merely by being routed into a corrective-work order — it remains company property that happens to be undergoing work.
WHY_IT_MATTERS: >
  An implicit ownership change would corrupt stock ownership records for the company's own inventory without any transaction that actually transferred it.
DISCONFIRMING_OBSERVATION: >
  Routing a company-owned item into a corrective-work order changes its recorded ownership to something other than the company, with no ownership-transfer transaction behind the change.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Route a company-owned item into a corrective-work order and check its recorded ownership before and during the work.
LAYER: BASE
```

## G05-REPAIR-Q003

```yaml
QID: G05-REPAIR-Q003
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The recorded ownership status of an item under corrective work — company-owned, customer-owned, or unowned — determines whether it is included in the company's own valued on-hand inventory at all.
WHY_IT_MATTERS: >
  If inventory inclusion did not follow ownership, financial statements would misstate what the company actually owns.
DISCONFIRMING_OBSERVATION: >
  Two items under corrective work with different recorded ownership statuses are both included, or both excluded, from the company's valued on-hand inventory regardless of that difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place one company-owned and one customer-owned item into corrective-work orders and compare whether each is included in the company's valued on-hand inventory.
LAYER: BASE
```

## G05-REPAIR-Q004

```yaml
QID: G05-REPAIR-Q004
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A corrective-work order makes it possible to distinguish, for any single unit on the work floor, whose property it is, rather than treating every unit there identically regardless of ownership.
WHY_IT_MATTERS: >
  Without a visible ownership distinction on the floor, staff cannot know which items require different handling, insurance, or disposal treatment.
DISCONFIRMING_OBSERVATION: >
  Viewing a corrective-work order gives no indication of whether the unit involved is company-owned or customer-owned.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Open corrective-work orders for one company-owned and one customer-owned unit and check whether ownership is visibly stated in each.
LAYER: BASE
```

## G05-REPAIR-Q005

```yaml
QID: G05-REPAIR-Q005
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A part consumed against a corrective-work order is removed from ordinary on-hand stock and valued the same way any other stock-reducing consumption would be, not under a special work-order-only valuation rule.
WHY_IT_MATTERS: >
  A separate, undocumented valuation rule for these parts would make cost figures inconsistent with the rest of inventory accounting and hard to reconcile.
DISCONFIRMING_OBSERVATION: >
  A part consumed against a corrective-work order is valued at a different cost than an identical part consumed through an ordinary stock-reducing operation on the same date.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Consume identical parts through a corrective-work order and through an ordinary stock-reducing operation on the same date, and compare the recorded cost of each.
LAYER: PROCESS
```

## G05-REPAIR-Q006

```yaml
QID: G05-REPAIR-Q006
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When several distinct parts are consumed against one corrective-work order, each part's cost is individually attributable within the work-order record rather than collapsed into a single undifferentiated total.
WHY_IT_MATTERS: >
  A collapsed total prevents anyone from later working out which specific part drove the cost, which matters for pricing, warranty recovery, or dispute resolution.
DISCONFIRMING_OBSERVATION: >
  A corrective-work order with several parts consumed against it shows only one combined cost figure with no way to attribute cost back to an individual part.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consume three or more distinct parts against one corrective-work order and check whether each part's individual cost is separately visible.
LAYER: PROCESS
```

## G05-REPAIR-Q007

```yaml
QID: G05-REPAIR-Q007
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A part reserved for a corrective-work order but not yet actually consumed does not reduce the company's on-hand valued stock until the consumption itself actually occurs.
WHY_IT_MATTERS: >
  Reducing stock at reservation rather than consumption would overstate how much has actually been used and understate what is still physically available.
DISCONFIRMING_OBSERVATION: >
  On-hand valued stock decreases at the moment a part is reserved against a corrective-work order, before the part is actually consumed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reserve a part against a corrective-work order without consuming it yet, and check whether on-hand valued stock changes at reservation.
LAYER: PROCESS
```

## G05-REPAIR-Q008

```yaml
QID: G05-REPAIR-Q008
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Returning an unused, reserved part back to stock once a corrective-work order completes restores it to available on-hand stock rather than leaving it in an unusable state that is neither consumed nor available.
WHY_IT_MATTERS: >
  A part stuck in limbo is effectively lost inventory even though it physically still exists and could satisfy other demand.
DISCONFIRMING_OBSERVATION: >
  An unused part reserved against a completed corrective-work order remains unavailable to satisfy other demand even though it was never actually consumed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve a part against a corrective-work order, complete the work without consuming that part, and check whether it becomes available for other demand.
LAYER: PROCESS
```

## G05-REPAIR-Q009

```yaml
QID: G05-REPAIR-Q009
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where corrective work replaces a serialised unit's identity-bearing component such that the unit effectively carries a new identity on return, an explicit action is required to record that new identity — it is not carried forward silently under the original one.
WHY_IT_MATTERS: >
  A silently retained old identity on a unit whose identity-defining part has changed would make later traceability point to the wrong physical component history.
DISCONFIRMING_OBSERVATION: >
  A unit returned with a replaced identity-bearing component still carries its original identity with no explicit action or record showing the identity was reconsidered.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform corrective work that replaces a serialised unit's identity-bearing component, then check whether recording a new identity requires an explicit, visible action.
LAYER: PROCESS
```

## G05-REPAIR-Q010

```yaml
QID: G05-REPAIR-Q010
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A unit returned from corrective work under a different lot than the one it entered under can still be traced back to the original lot it arrived as.
WHY_IT_MATTERS: >
  Losing the link back to the original lot breaks recall and traceability exactly at the point a lot change was made.
DISCONFIRMING_OBSERVATION: >
  A unit returned under a new lot after corrective work cannot be traced back to the lot it was originally logged under when the work began.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete corrective work that changes a unit's lot assignment on return, then attempt to trace the returned unit back to its originally logged lot.
LAYER: PROCESS
```

## G05-REPAIR-Q011

```yaml
QID: G05-REPAIR-Q011
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The quantity of a product returned from corrective work under a new lot or serial is reconciled against the quantity that originally went in, so a returned unit cannot appear as an entirely new, disconnected receipt.
WHY_IT_MATTERS: >
  An unreconciled quantity would let stock effectively be created or lost across the corrective-work boundary with no record explaining the difference.
DISCONFIRMING_OBSERVATION: >
  A corrective-work order's output quantity under a new lot or serial shows no link back to, or reconciliation against, the quantity that was originally logged in.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Complete a corrective-work order that changes lot or serial on return, and check whether the returned quantity is reconciled against the quantity that entered.
LAYER: PROCESS
```

## G05-REPAIR-Q012

```yaml
QID: G05-REPAIR-Q012
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A serialised unit's prior movement and ownership history remains attached to its serial identity after corrective work completes, rather than the process starting a fresh history as though the unit were newly received.
WHY_IT_MATTERS: >
  Losing prior history at every corrective-work event would make long-lived serialised assets untraceable over their working life.
DISCONFIRMING_OBSERVATION: >
  A serialised unit's movement history recorded before corrective work is no longer visible or linked once the work completes.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a serialised unit's movement history, route it through a corrective-work order, and check whether the prior history remains visible afterward.
LAYER: BASE
```

## G05-REPAIR-Q013

```yaml
QID: G05-REPAIR-Q013
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A serial number that goes into corrective work and returns under that same, unchanged serial number does not lose any part of its pre-existing traceability chain.
WHY_IT_MATTERS: >
  Even the simplest case — same serial in, same serial out — must preserve history, or no more complex case involving an identity change ever could.
DISCONFIRMING_OBSERVATION: >
  A unit returned under the identical serial number it entered with shows a shorter or altered traceability chain than it had before the work began.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Route a serialised unit through corrective work with no identity change, and compare its traceability chain before and after.
LAYER: BASE
```

## G05-REPAIR-Q014

```yaml
QID: G05-REPAIR-Q014
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a serialised unit's identity does change during corrective work, an explicit link is retained between the old and new identity so the pre-existing history is not simply orphaned.
WHY_IT_MATTERS: >
  Without an explicit link, the old identity's history becomes an orphaned record disconnected from the unit that is now physically in service.
DISCONFIRMING_OBSERVATION: >
  A unit whose serial identity changed during corrective work shows no link connecting its new identity back to the old one's history.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform corrective work that changes a unit's serial identity and check for an explicit link between the old and new identity records.
LAYER: PROCESS
```

## G05-REPAIR-Q015

```yaml
QID: G05-REPAIR-Q015
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether a unit is still under an active commercial commitment (such as an open warranty or service contract) is identifiable at the point a corrective-work order is initiated for it, rather than the process being blind to that status.
WHY_IT_MATTERS: >
  Without this visibility, a commitment-covered unit could be billed as if it were not covered, or vice versa, purely by oversight.
DISCONFIRMING_OBSERVATION: >
  Initiating a corrective-work order for a unit under an active commercial commitment gives no indication of that commitment's existence.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Initiate a corrective-work order for a unit known to be under an active commercial commitment and check whether that status is surfaced.
LAYER: PROCESS
```

## G05-REPAIR-Q016

```yaml
QID: G05-REPAIR-Q016
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Performing corrective work on a unit under an active commercial commitment does not, by itself, alter or close out that commitment — the work and the commitment are tracked as related but distinct facts.
WHY_IT_MATTERS: >
  A commitment silently closed or altered by an unrelated work event would misrepresent what the business actually still owes the customer.
DISCONFIRMING_OBSERVATION: >
  Completing a corrective-work order on a unit changes the state of its linked commercial commitment with no separate action taken on the commitment itself.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Complete a corrective-work order on a unit under an active commercial commitment and check whether the commitment's own state changed as a side effect.
LAYER: PROCESS
```

## G05-REPAIR-Q017

```yaml
QID: G05-REPAIR-Q017
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The commercial-commitment status of a unit is visible to whoever authorises its corrective-work order, so a decision on whether to charge the customer can be made with that fact already in hand.
WHY_IT_MATTERS: >
  A decision-maker without visibility into commitment status is guessing, which leads to inconsistent billing decisions for equivalent cases.
DISCONFIRMING_OBSERVATION: >
  A user authorising a corrective-work order has no visible indication of the unit's commercial-commitment status at the point of authorisation.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  As the authorising role, open a corrective-work order for a unit under a known commercial commitment and check whether that status is presented at authorisation.
LAYER: PROCESS
```

## G05-REPAIR-Q018

```yaml
QID: G05-REPAIR-Q018
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The cost of a corrective-work order — parts plus any other recognised cost — is recognised at a defined point in its lifecycle, such as completion, rather than being scattered across whenever a part happens to be consumed with no aggregation.
WHY_IT_MATTERS: >
  Cost scattered with no aggregation point makes it impossible to answer a simple question like "what did this job cost" without manual reconstruction.
DISCONFIRMING_OBSERVATION: >
  A completed corrective-work order shows no single, aggregated total cost figure, only a scattering of individual consumption events with no defined recognition point.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Complete a corrective-work order with multiple parts consumed at different times and check for a single, defined cost-recognition point.
LAYER: PROCESS
```

## G05-REPAIR-Q019

```yaml
QID: G05-REPAIR-Q019
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A corrective-work order performed at a paying customer's request records its cost against that specific work order and customer, not pooled anonymously with unrelated work.
WHY_IT_MATTERS: >
  Pooled costs make it impossible to bill the right customer the right amount or to analyse profitability by job.
DISCONFIRMING_OBSERVATION: >
  The cost of a customer-billed corrective-work order cannot be isolated from the cost of other, unrelated work performed around the same time.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Run two customer-billed corrective-work orders concurrently and check whether each order's cost can be isolated from the other.
LAYER: PROCESS
```

## G05-REPAIR-Q020

```yaml
QID: G05-REPAIR-Q020
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An internal corrective-work order, performed on the company's own stock with no customer billing involved, still records and recognises its parts cost even though there is no revenue transaction attached to it.
WHY_IT_MATTERS: >
  If unbilled work recorded no cost at all, internal maintenance activity would be invisible to cost reporting even though real parts were genuinely consumed.
DISCONFIRMING_OBSERVATION: >
  An internal, unbilled corrective-work order that consumed real parts shows no recorded cost for those parts.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  Perform an internal, unbilled corrective-work order that consumes parts and check whether a cost is recorded for that consumption.
LAYER: PROCESS
```

## G05-REPAIR-Q021

```yaml
QID: G05-REPAIR-Q021
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A corrective-work order that is abandoned after parts have already been consumed against it does not silently return those parts to available stock as though they had never been used.
WHY_IT_MATTERS: >
  Silently un-consuming parts that were physically used would overstate available stock and understate the real cost already incurred.
DISCONFIRMING_OBSERVATION: >
  Abandoning a corrective-work order after parts consumption restores those consumed parts to available on-hand stock.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Consume parts against a corrective-work order, then abandon the order, and check whether the consumed parts reappear as available stock.
LAYER: PROCESS
```

## G05-REPAIR-Q022

```yaml
QID: G05-REPAIR-Q022
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An abandoned corrective-work order with cost already incurred is distinguishable in the record from one that was cancelled before any part was touched.
WHY_IT_MATTERS: >
  Treating the two the same would make it impossible to later separate genuine sunk cost from a clean, no-cost cancellation when reviewing outcomes.
DISCONFIRMING_OBSERVATION: >
  An abandoned-with-cost-incurred work order and a cancelled-before-any-consumption work order leave identical records with no distinguishing marker.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Abandon one corrective-work order after parts consumption and cancel another before any consumption, then compare the two resulting records.
LAYER: PROCESS
```

## G05-REPAIR-Q023

```yaml
QID: G05-REPAIR-Q023
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a corrective-work order is abandoned partway, the unit itself is left with a defined resulting status — returned as-is, held, or routed to a further decision — rather than being left in an undefined state with no next action recorded.
WHY_IT_MATTERS: >
  A unit with no defined status after an abandoned job can sit indefinitely with nobody responsible for deciding what happens to it next.
DISCONFIRMING_OBSERVATION: >
  After a corrective-work order is abandoned partway, the unit's status shows no defined value and no indication of what should happen to it next.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Abandon a corrective-work order partway through and check the resulting recorded status of the unit involved.
LAYER: PROCESS
```

## G05-REPAIR-Q024

```yaml
QID: G05-REPAIR-Q024
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Scrapping a unit after parts were already consumed for its corrective work retains the record of those consumed parts' cost rather than erasing it along with the scrapped unit.
WHY_IT_MATTERS: >
  Erasing the cost record on scrap would hide a genuine loss instead of surfacing it for review, understating the true cost of the failed job.
DISCONFIRMING_OBSERVATION: >
  Scrapping a unit under corrective work removes the record of parts already consumed against it, leaving no trace of that cost.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Consume parts against a corrective-work order, then scrap the unit, and check whether the consumed-parts cost record survives.
LAYER: PROCESS
```

## G05-REPAIR-Q025

```yaml
QID: G05-REPAIR-Q025
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Scrapping the unit under corrective work produces a distinct outcome record separate from a successful completion, so the two are not indistinguishable after the fact.
WHY_IT_MATTERS: >
  Indistinguishable outcomes would prevent any later reporting of scrap rate versus successful completion rate for corrective work.
DISCONFIRMING_OBSERVATION: >
  A scrapped unit's corrective-work order and a successfully completed one show the identical final status with no way to tell them apart.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete one corrective-work order successfully and scrap the unit on another, then compare the two final order records.
LAYER: PROCESS
```

## G05-REPAIR-Q026

```yaml
QID: G05-REPAIR-Q026
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Scrapping a customer-owned unit during corrective work is not, by that scrapping action, absorbed into the servicing company's own inventory loss or valuation as though the unit had been the company's own stock.
WHY_IT_MATTERS: >
  Absorbing a customer's loss into the company's own books would misstate the company's inventory results with a value it never actually owned.
DISCONFIRMING_OBSERVATION: >
  Scrapping a customer-owned unit produces an inventory-loss entry in the servicing company's own valuation records.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Scrap a customer-owned unit under corrective work and check whether the company's own inventory-loss or valuation records reflect it.
LAYER: PROCESS
```

## G05-REPAIR-Q027

```yaml
QID: G05-REPAIR-Q027
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A customer-owned unit physically present during corrective work does not contribute to the servicing company's own inventory valuation total at any point while the work is in progress.
WHY_IT_MATTERS: >
  Even a temporary inclusion would overstate the company's own reported inventory value for as long as the customer's unit sits on the premises.
DISCONFIRMING_OBSERVATION: >
  The company's own inventory valuation total changes when a customer-owned unit is logged in for corrective work, and changes back when it leaves.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Log a customer-owned unit in and out of a corrective-work order and monitor the company's own inventory valuation total throughout.
LAYER: BASE
```

## G05-REPAIR-Q028

```yaml
QID: G05-REPAIR-Q028
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Only the parts and labour genuinely consumed by the servicing company are valued as that company's own cost — the pre-existing value of a customer-owned unit being worked on is not folded into that cost.
WHY_IT_MATTERS: >
  Folding the customer's own item value into the company's cost would grossly overstate the true cost of the work performed.
DISCONFIRMING_OBSERVATION: >
  The recorded cost of a corrective-work order on a customer-owned unit includes the pre-existing value of the unit itself, not just the parts and labour applied.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  Perform corrective work on a customer-owned unit with a known pre-existing value, consume specific parts, and check what the recorded work cost actually includes.
LAYER: BASE
```

## G05-REPAIR-Q029

```yaml
QID: G05-REPAIR-Q029
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A customer-owned unit lost or damaged while under corrective work is tracked as a distinct liability or incident record rather than appearing as an adjustment to the servicing company's own stock valuation.
WHY_IT_MATTERS: >
  Recording it as a stock adjustment would hide a genuine liability to the customer inside routine inventory noise instead of surfacing it for resolution.
DISCONFIRMING_OBSERVATION: >
  Loss or damage to a customer-owned unit during corrective work only ever shows up as a change to the company's own stock valuation, with no distinct incident or liability record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record a loss or damage event for a customer-owned unit during corrective work and check what kind of record, if any, results.
LAYER: PROCESS
```

## G05-REPAIR-Q030

```yaml
QID: G05-REPAIR-Q030
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When corrective work legitimately changes the quantity of the item returned — several units consolidated into one, or one split into several — the record reconciles the quantity returned against the quantity that went in.
WHY_IT_MATTERS: >
  An unreconciled quantity change would let stock quietly appear or disappear across a legitimate consolidation or split with no explanation.
DISCONFIRMING_OBSERVATION: >
  A corrective-work order that consolidates or splits quantity on return shows no link reconciling the returned quantity against what originally went in.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Perform a corrective-work order that changes the returned quantity from what went in, and check for a reconciling link between the two.
LAYER: PROCESS
```

## G05-REPAIR-Q031

```yaml
QID: G05-REPAIR-Q031
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A corrective-work order that returns a unit in a different unit of measure than it was received in converts consistently between the two, and that conversion is traceable rather than assumed.
WHY_IT_MATTERS: >
  An untraceable, assumed conversion invites silent quantity errors whenever units of measure differ between intake and return.
DISCONFIRMING_OBSERVATION: >
  A corrective-work order returning a unit in a different unit of measure than it went in shows no visible conversion factor or traceable calculation.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Log a unit in one unit of measure, return it in a different one through corrective work, and check whether the conversion is visible and traceable.
LAYER: PROCESS
```

## G05-REPAIR-Q032

```yaml
QID: G05-REPAIR-Q032
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An unexplained quantity discrepancy between what entered corrective work and what was actually returned is flagged rather than passed through silently as though it were expected.
WHY_IT_MATTERS: >
  A silently absorbed discrepancy could mask theft, damage, or a data-entry error at the exact point where physical goods change hands.
DISCONFIRMING_OBSERVATION: >
  A corrective-work order completes with a returned quantity that does not match what went in, with no flag, warning, or required explanation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a corrective-work order with a deliberately mismatched returned quantity and check whether the discrepancy is flagged.
LAYER: PROCESS
```

## G05-REPAIR-Q033

```yaml
QID: G05-REPAIR-Q033
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a corrective-work order after some work and part consumption has already occurred does not retroactively erase the record of the work and parts already consumed.
WHY_IT_MATTERS: >
  Erasing evidence of real, already-incurred consumption on cancellation would hide a genuine cost and break the audit trail of what actually happened.
DISCONFIRMING_OBSERVATION: >
  Cancelling a corrective-work order after partial parts consumption removes all record that any consumption occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consume parts against a corrective-work order, cancel the order, and check whether the consumption record still exists afterward.
LAYER: PROCESS
```

## G05-REPAIR-Q034

```yaml
QID: G05-REPAIR-Q034
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cancelled corrective-work order with parts already consumed leaves that consumed cost attributed somewhere identifiable rather than orphaned with no owner.
WHY_IT_MATTERS: >
  An orphaned cost with no owner cannot be reported, recovered, or explained when someone later asks where the money went.
DISCONFIRMING_OBSERVATION: >
  The cost of parts consumed against a since-cancelled corrective-work order cannot be attributed to any identifiable order, job, or cost centre.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Cancel a corrective-work order after parts consumption and attempt to trace where the resulting cost is attributed.
LAYER: PROCESS
```

## G05-REPAIR-Q035

```yaml
QID: G05-REPAIR-Q035
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The unit associated with a corrective-work order cancelled after partial work has a defined resulting status rather than the cancellation leaving its physical state undocumented.
WHY_IT_MATTERS: >
  An undocumented physical state after cancellation leaves warehouse staff guessing what to actually do with the unit sitting in front of them.
DISCONFIRMING_OBSERVATION: >
  After a corrective-work order is cancelled following partial work, the unit's recorded status shows nothing indicating what state it is actually in.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel a corrective-work order after partial work and check the resulting recorded status of the unit.
LAYER: PROCESS
```

## G05-REPAIR-Q036

```yaml
QID: G05-REPAIR-Q036
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Authorising a scrap decision on a unit under corrective work is restricted to a defined role or permission, distinct from the permission needed merely to update the work order itself.
WHY_IT_MATTERS: >
  If ordinary update access were enough to authorise scrap, an irreversible destructive decision would carry no meaningful control at all.
DISCONFIRMING_OBSERVATION: >
  A user holding only ordinary work-order update permission is able to authorise a scrap decision without any additional, distinct permission.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Attempt to authorise a scrap decision as a user granted only ordinary work-order update permission and compare the outcome to an authorised role.
LAYER: PROCESS
```

## G05-REPAIR-Q037

```yaml
QID: G05-REPAIR-Q037
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scrap decision made during corrective work leaves a record of who authorised it and when, not merely a record that scrapping occurred.
WHY_IT_MATTERS: >
  Recording only that scrapping happened, without who decided it, removes accountability for an irreversible action.
DISCONFIRMING_OBSERVATION: >
  A scrap event on a unit under corrective work shows that scrapping occurred but no identifiable authoriser or timestamp for the decision.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Authorise and execute a scrap decision on a unit under corrective work and inspect the resulting record for the authoriser and timestamp.
LAYER: PROCESS
```

## G05-REPAIR-Q038

```yaml
QID: G05-REPAIR-Q038
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A technician without scrap-authorisation permission cannot complete a scrap action on a unit even while holding full access to update the corrective-work order itself.
WHY_IT_MATTERS: >
  Full work-order access without a separate scrap gate would let anyone who can touch the order also destroy the asset, collapsing the intended separation of duties.
DISCONFIRMING_OBSERVATION: >
  A technician with full work-order update access but no scrap-authorisation permission is able to successfully scrap the unit.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a technician with full work-order access but no scrap permission, attempt to complete a scrap action on the unit.
LAYER: PROCESS
```

## G05-REPAIR-Q039

```yaml
QID: G05-REPAIR-Q039
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A corrective-work order's lifecycle state (such as opened, in progress, completed, or cancelled) is consistent with the unit's actual recorded location and status, rather than the two being able to drift apart.
WHY_IT_MATTERS: >
  A drift between order state and unit status means staff cannot trust either record to reflect where the physical item actually is.
DISCONFIRMING_OBSERVATION: >
  A corrective-work order shows a completed state while the unit's own recorded status still shows it as under active work, or the reverse.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Move a corrective-work order through its lifecycle states and compare the order's state to the unit's own recorded status at each step.
LAYER: BASE
```

## G05-REPAIR-Q040

```yaml
QID: G05-REPAIR-Q040
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two corrective-work orders attempting at the same time to consume the same limited part cannot both succeed in consuming more of it than is actually on hand.
WHY_IT_MATTERS: >
  Allowing both to succeed would let recorded consumption exceed physical reality, silently creating negative or phantom stock.
DISCONFIRMING_OBSERVATION: >
  Two concurrent part-consumption attempts against a tightly limited quantity both report success, together exceeding what was actually on hand.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  With a part limited to a small on-hand quantity, issue two concurrent consumption attempts against it from two different corrective-work orders and compare both outcomes.
LAYER: PROCESS
```

## G05-REPAIR-Q041

```yaml
QID: G05-REPAIR-Q041
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Corrective work performed by one company or branch does not consume parts stock belonging to a different company or branch without an explicit, visible transfer between them.
WHY_IT_MATTERS: >
  Cross-boundary consumption with no visible transfer would corrupt each entity's own stock and cost records without an auditable transaction behind it.
DISCONFIRMING_OBSERVATION: >
  A corrective-work order under one company reduces stock recorded under a different company with no visible transfer transaction between the two.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Perform a corrective-work order under one company using a part nominally held under a different company, and check for a visible transfer record.
LAYER: PROCESS
```

## G05-REPAIR-Q042

```yaml
QID: G05-REPAIR-Q042
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A corrective-work order linked to an originating sales or service commitment remains linkable back to that commitment after the work order itself closes.
WHY_IT_MATTERS: >
  Losing the link on closure would make it impossible to later connect a completed job back to the commitment that justified it, for billing or warranty review.
DISCONFIRMING_OBSERVATION: >
  A closed corrective-work order that was originally linked to a sales or service commitment no longer shows that link once closed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Link a corrective-work order to an originating commitment, close the work order, and check whether the link is still visible afterward.
LAYER: PROCESS
```

## G05-REPAIR-Q043

```yaml
QID: G05-REPAIR-Q043
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Attempting to consume more of a part against a corrective-work order than is actually available in stock is prevented or explicitly flagged, not silently allowed to go negative without acknowledgment.
WHY_IT_MATTERS: >
  Silent negative consumption hides a real stock shortage behind a transaction that looks like it succeeded normally.
DISCONFIRMING_OBSERVATION: >
  A corrective-work order successfully consumes more of a part than is on hand with no warning, flag, or required acknowledgment.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to consume a quantity of a part against a corrective-work order that exceeds what is actually on hand.
LAYER: PROCESS
```

## G05-REPAIR-Q044

```yaml
QID: G05-REPAIR-Q044
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The full sequence of a corrective-work order — received, worked on, parts consumed, returned or scrapped — can be reconstructed after the fact from the record alone, not only from the memory of whoever performed it.
WHY_IT_MATTERS: >
  A sequence reconstructable only from memory disappears the moment the person involved is unavailable, which is exactly when a review is most needed.
DISCONFIRMING_OBSERVATION: >
  The recorded history of a completed corrective-work order omits one or more steps in its actual sequence, leaving a gap only the performing technician could fill in.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Complete a corrective-work order through its full sequence, then attempt to reconstruct that sequence solely from the recorded history.
LAYER: PROCESS
```

## G05-REPAIR-Q045

```yaml
QID: G05-REPAIR-Q045
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reopening or reversing a completed corrective-work order does not silently re-release the parts already consumed against it back into available stock without an explicit corrective action.
WHY_IT_MATTERS: >
  Silent re-release would create phantom available stock for parts that were, in physical fact, already used and cannot be recovered.
DISCONFIRMING_OBSERVATION: >
  Reopening a completed corrective-work order returns its already-consumed parts to available on-hand stock with no explicit corrective transaction.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a corrective-work order with parts consumed, then reopen or reverse it, and check whether the consumed parts reappear as available stock.
LAYER: PROCESS
```

## G05-REPAIR-Q046

```yaml
QID: G05-REPAIR-Q046
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a corrective-work order requires a linked originating commercial document before work can begin is a configurable, optional behaviour, and where it is required, an order lacking that link cannot be started.
WHY_IT_MATTERS: >
  If the requirement were cosmetic rather than enforced, a site relying on it for control would have no real protection against unauthorised or untracked work starting.
DISCONFIRMING_OBSERVATION: >
  With the linked-document requirement configured as mandatory, a corrective-work order without any linked originating document is still able to start.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Configure the linked-document requirement as mandatory, then attempt to start a corrective-work order with no linked originating document.
LAYER: PROCESS
```

## G05-REPAIR-Q047

```yaml
QID: G05-REPAIR-Q047
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Cost and valuation visibility for a corrective-work order is gated to a role authorised for that data, but completing the work order itself is not blocked by the absence of that same role.
WHY_IT_MATTERS: >
  If completion required cost visibility, a technician correctly barred from financial data would be unable to do their actual job of finishing the work.
DISCONFIRMING_OBSERVATION: >
  A technician without cost or valuation permission is unable to mark a corrective-work order complete purely because that permission is missing.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a technician with no cost or valuation permission, attempt to complete a corrective-work order and observe whether completion itself is blocked.
LAYER: PROCESS
```

## G05-REPAIR-Q048

```yaml
QID: G05-REPAIR-Q048
MODULE: repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A configuration that marks parts on a corrective-work order as billable to the customer actually causes those parts to be excluded from the company's own internal cost absorption, rather than the setting being cosmetic while the cost still lands internally regardless.
WHY_IT_MATTERS: >
  A cosmetic billable flag that does not actually change internal cost absorption would misstate the company's true internal cost of goods for every job marked that way.
DISCONFIRMING_OBSERVATION: >
  Parts marked billable to the customer on a corrective-work order still land in the company's own internal cost absorption exactly as an unbilled part would.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Mark parts as customer-billable on a corrective-work order and compare their treatment in internal cost absorption against an otherwise identical unbilled case.
LAYER: PROCESS
```
