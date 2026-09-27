# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_project_stock Module Bridge MVQ Bank

**Document ID:** GMVQ-G08-SALE_PROJECT_STOCK-MVQ36-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_project_stock`
**Wave:** W2
**Author Cell:** P-S7 (GMVQ Question Factory — Production Team P-S7)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 36
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 36 = 91
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `sale_project_stock`, the three-participant seam
where goods physically move under a project-linked order. Per the GMVQ Bridge Module Rule V1.00,
every question here fails only where an order, a project, AND a physical goods movement all three
have to be present at once: whether a movement counts as customer delivery or project consumption,
reservation and reallocation across competing demands, site-versus-registered-address delivery,
over-consumption and shortage attribution, returns from a project site, traceability of tracked
units, and multi-location/multi-company boundaries on the physical movement itself. No question here
is a pure order+project question (that is `sale_project`'s bank) and no question is a ledger/costing
question (that is `sale_project_stock_account`'s bank); every question was tested against the bridge
removal test for all three participants, not just two, before being kept.

## Control

**Arity owned: THREE-PARTICIPANT (order + project + physical goods movement) only.** Every question
below requires an order, a project, and an actual or attempted stock movement to co-occur; removing
any one of the three would either make the question meaningless or move it into `sale_project`'s or
a plain `sale_stock`-type bank instead. No question here requires a ledger/accounting posting to be
material — that dependency is reserved to `sale_project_stock_account`.

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: these 36 questions test 36 distinct material seam hypotheses; the authoring pass was
  stopped here rather than stretched toward 48, per the no-padding rule.
- Question text is source-neutral: no vendor or product name, no technical identifier, and the
  module's own metadata name never appears outside the `MODULE:` field.
- No question concerns an accounting/ledger entry; that seam is reserved to `sale_project_stock_account`.
- Every question passed the three-participant bridge removal test before being kept, and was
  cross-checked against the sibling `sale_project` bank's authored HYPOTHESIS lines at authoring
  time to avoid restating a pure order+project invariant.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_PROJECT_STOCK-Q001

```yaml
QID: G08-SALE_PROJECT_STOCK-Q001
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A single outward movement of goods under a project-linked order is classified as either delivered to the customer or consumed by the project, not both, and that classification determines what the order shows as fulfilled.
WHY_IT_MATTERS: >
  A movement counted as both, or as neither, would make it impossible to know whether the customer's order was actually fulfilled.
DISCONFIRMING_OBSERVATION: >
  The same movement is recorded as both a customer delivery and a project consumption, or as neither, leaving the order's fulfilled quantity ambiguous.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Move goods out under a project-linked order in a way that could be read either way, and check which single classification the order's fulfilment record reflects.
```

## G08-SALE_PROJECT_STOCK-Q002

```yaml
QID: G08-SALE_PROJECT_STOCK-Q002
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Materials reserved specifically to fulfil a project-linked order's line are not silently reallocated to an unrelated order without the original order's promise being visibly downgraded.
WHY_IT_MATTERS: >
  Reallocating reserved material with no visible downgrade would leave the customer's promised order silently unfulfillable.
DISCONFIRMING_OBSERVATION: >
  Reserved materials are taken by a different, unrelated order and the project-linked order's own promised fulfilment shows no change or warning.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reserve stock for a project-linked order's line, reallocate it to a different order, and check whether the original order's fulfilment promise reflects the loss.
```

## G08-SALE_PROJECT_STOCK-Q003

```yaml
QID: G08-SALE_PROJECT_STOCK-Q003
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  An order specifying delivery to a project site address rather than the customer's registered address updates the order's delivered status through the same rule as any other address.
WHY_IT_MATTERS: >
  A silent gap specific to site deliveries would leave project-based orders unreliably tracked compared to ordinary ones.
DISCONFIRMING_OBSERVATION: >
  Goods delivered to a project site address do not update the order's delivered status the way an equivalent delivery to the customer's registered address would.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure an order to deliver to a project site address distinct from the customer's registered address, complete the delivery, and check whether the order's status updates normally.
```

## G08-SALE_PROJECT_STOCK-Q004

```yaml
QID: G08-SALE_PROJECT_STOCK-Q004
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When the project consumes more material at the site than the order's line originally priced for, that overage is visibly flagged rather than silently absorbed with no trace of the excess.
WHY_IT_MATTERS: >
  An unflagged overage could go unbilled and unnoticed, or be discovered only much later with no record of when it happened.
DISCONFIRMING_OBSERVATION: >
  Material consumed beyond the order's priced quantity is absorbed into existing records with no visible flag that an overage occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cause the project to consume more of an item than the order's line quantity, and check whether the overage is visibly flagged anywhere.
```

## G08-SALE_PROJECT_STOCK-Q005

```yaml
QID: G08-SALE_PROJECT_STOCK-Q005
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A return of unused material from a project site is recorded through one documented path rather than falling into a gap where neither the order nor the project reflects it.
WHY_IT_MATTERS: >
  An unrecorded return would leave both the order's and the project's material figures overstated indefinitely.
DISCONFIRMING_OBSERVATION: >
  Unused material returned from a project site is not reflected in either the order's records or the project's records.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Return unused material from a project site after partial consumption, and check whether the return appears in the order's record, the project's record, or neither.
```

## G08-SALE_PROJECT_STOCK-Q006

```yaml
QID: G08-SALE_PROJECT_STOCK-Q006
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Putting a project on hold after materials have already been issued to it does not silently reclassify those already-issued materials as available again for a different order without an explicit release action.
WHY_IT_MATTERS: >
  Silently freeing paused-project material for another order could leave the paused project short when it resumes, without anyone deciding that trade-off.
DISCONFIRMING_OBSERVATION: >
  Materials already issued to a paused project appear as freely available for a different order with no explicit release step recorded.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Issue materials to a project under an order, put the project on hold, and check whether those materials appear available for reallocation without an explicit release.
```

## G08-SALE_PROJECT_STOCK-Q007

```yaml
QID: G08-SALE_PROJECT_STOCK-Q007
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A material shortage affecting a project-linked order is reported against a single documented location, not two disagreeing shortage views that a person has to reconcile manually with no cross-reference.
WHY_IT_MATTERS: >
  Two disagreeing shortage views would leave it unclear which team is responsible for resolving the shortfall.
DISCONFIRMING_OBSERVATION: >
  The order's own shortage report and the project's own shortage report disagree about the same underlying shortage, with no cross-reference between them.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a material shortage affecting a project-linked order, and compare how the shortage appears in the order's own view versus the project's own view.
```

## G08-SALE_PROJECT_STOCK-Q008

```yaml
QID: G08-SALE_PROJECT_STOCK-Q008
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When several orders feed material into one project's shared pool and a shortage hits, which order's committed goods take priority is decided by a documented rule visible after the fact.
WHY_IT_MATTERS: >
  An arbitrary, invisible priority decision could quietly favour one customer's order over another with no accountability.
DISCONFIRMING_OBSERVATION: >
  A shortage across a shared material pool resolves in a way that cannot be explained or traced back to any documented priority rule.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a shortage affecting a project's shared material pool fed by more than one order, and check whether the resulting priority decision is visible and traceable.
```

## G08-SALE_PROJECT_STOCK-Q009

```yaml
QID: G08-SALE_PROJECT_STOCK-Q009
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An order's lines all showing as delivered per stock records does not, by itself, make the linked project's own consumption tracking assume that material has actually been used on site.
WHY_IT_MATTERS: >
  Conflating logistics-complete with consumption-complete would overstate real progress to anyone relying on the project's own view.
DISCONFIRMING_OBSERVATION: >
  The project's own progress or consumption reporting shows material as consumed simply because the order recorded it as delivered, without independent confirmation of on-site use.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Deliver all of an order's lines to a project site without yet logging on-site consumption, and check whether the project's own reporting treats the material as consumed.
```

## G08-SALE_PROJECT_STOCK-Q010

```yaml
QID: G08-SALE_PROJECT_STOCK-Q010
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A serial- or lot-tracked item issued to a project under an order remains traceable back to that specific order and delivery event even after the project has drawn on it.
WHY_IT_MATTERS: >
  A broken trace would leave a later warranty or traceability check on the order unable to identify what was actually supplied.
DISCONFIRMING_OBSERVATION: >
  A traceability or warranty check on the order cannot identify which specific serial or lot was actually issued to the project against that order's line.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Issue a serial- or lot-tracked item to a project under an order, and later attempt to trace that specific unit back from the order.
```

## G08-SALE_PROJECT_STOCK-Q011

```yaml
QID: G08-SALE_PROJECT_STOCK-Q011
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order after some of its goods have already been delivered to and consumed by the project site does not retroactively make the already-consumed goods disappear from either record.
WHY_IT_MATTERS: >
  Erasing a completed delivery and consumption record would make it impossible to account for goods that already physically left the business.
DISCONFIRMING_OBSERVATION: >
  Cancelling the order removes or hides the record of goods already delivered to and consumed by the project.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deliver and consume part of an order's goods at a project site, cancel the order, and check whether the already-completed delivery and consumption records remain intact.
```

## G08-SALE_PROJECT_STOCK-Q012

```yaml
QID: G08-SALE_PROJECT_STOCK-Q012
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A project spanning multiple physical locations feeding one order's delivery correctly represents the order's overall delivered status as the combination of all site-level partial deliveries.
WHY_IT_MATTERS: >
  Reflecting only the first site's delivery would understate how much of the order has actually shipped.
DISCONFIRMING_OBSERVATION: >
  The order's delivered status reflects only the first site delivery recorded for a multi-site project, ignoring the others.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Deliver an order's goods to a project across more than one physical location, and check whether the order's overall delivered status accounts for all locations.
```

## G08-SALE_PROJECT_STOCK-Q013

```yaml
QID: G08-SALE_PROJECT_STOCK-Q013
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The project drawing down delivered material across many small internal issues over an extended period does not allow the total issued quantity to silently exceed what the order actually delivered.
WHY_IT_MATTERS: >
  Unbounded over-issue across many small transactions could consume far more material than the order ever accounted for, with no single event flagging it.
DISCONFIRMING_OBSERVATION: >
  The project's cumulative internal issues of a material exceed the quantity the order actually delivered, with no block or warning at the point of over-issue.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Deliver a fixed quantity of material under an order, issue it to the project in many small increments exceeding that quantity, and check whether the excess is blocked or flagged.
```

## G08-SALE_PROJECT_STOCK-Q014

```yaml
QID: G08-SALE_PROJECT_STOCK-Q014
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where a single project draws material from more than one order, consumption logged against a task is traceable back to which specific order's delivery actually supplied it.
WHY_IT_MATTERS: >
  Arbitrary attribution would make it impossible to reconcile which customer's order actually paid for the material a task consumed.
DISCONFIRMING_OBSERVATION: >
  Material consumed by a project task cannot be traced back to which of several contributing orders actually supplied it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Feed one project's material pool from more than one order, consume material on a task, and attempt to trace that consumption back to its supplying order.
```

## G08-SALE_PROJECT_STOCK-Q015

```yaml
QID: G08-SALE_PROJECT_STOCK-Q015
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A quality or inspection hold placed on goods destined for a project-linked order blocks both the order's delivered-status update and the project's ability to log consumption of that held material.
WHY_IT_MATTERS: >
  Allowing either side to proceed around an active hold would defeat the purpose of the hold entirely.
DISCONFIRMING_OBSERVATION: >
  Material under an active quality hold can still be logged as consumed by the project, or the order can still show it as delivered, despite the hold.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place a quality or inspection hold on goods intended for a project-linked order, and attempt both to advance the order's delivered status and to log project consumption of the held material.
```

## G08-SALE_PROJECT_STOCK-Q016

```yaml
QID: G08-SALE_PROJECT_STOCK-Q016
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Goods delivered to a project site and then internally transferred to a different, unrelated project leave a visible record of that transfer.
WHY_IT_MATTERS: >
  A silent transfer would leave the original order's fulfilment record claiming to serve a project that no longer actually holds the goods.
DISCONFIRMING_OBSERVATION: >
  Goods transferred from the originally intended project to a different one leave the original order's record showing no change, with no trace of the transfer.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deliver goods to a project site under an order, transfer them internally to a different project, and check whether the original order's record reflects the transfer.
```

## G08-SALE_PROJECT_STOCK-Q017

```yaml
QID: G08-SALE_PROJECT_STOCK-Q017
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  When the order's delivered date and the project's own logged consumption date disagree, the order's delivery-based invoicing calculation uses one documented date consistently.
WHY_IT_MATTERS: >
  An inconsistent choice of date would make invoicing timing unpredictable and hard to reconcile after the fact.
DISCONFIRMING_OBSERVATION: >
  The order's invoicing calculation uses different dates, delivery versus consumption, inconsistently across otherwise similar cases.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a case where the order's delivery date and the project's logged consumption date differ, and check which date the order's invoicing calculation actually uses.
```

## G08-SALE_PROJECT_STOCK-Q018

```yaml
QID: G08-SALE_PROJECT_STOCK-Q018
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Closing a project before an order's remaining, still-pending delivery for it has shipped either cancels that pending delivery or leaves it clearly flagged as belonging to a now-closed project.
WHY_IT_MATTERS: >
  An unflagged pending delivery for a closed project could ship unnoticed to a site no one is tracking anymore.
DISCONFIRMING_OBSERVATION: >
  A pending delivery for an order continues unflagged and unresolved after its linked project has already been closed, with no indication of the mismatch.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close a project while an order linked to it still has an undelivered remainder pending, and check how that pending delivery is treated.
```
## G08-SALE_PROJECT_STOCK-Q019

```yaml
QID: G08-SALE_PROJECT_STOCK-Q019
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Complimentary or goodwill goods issued to a project site outside of any priced order line are recorded so that a reconciliation of order-delivered against project-received can still explain the difference.
WHY_IT_MATTERS: >
  An unexplained reconciliation gap would make it impossible to distinguish a goodwill gesture from an unrecorded loss.
DISCONFIRMING_OBSERVATION: >
  Goodwill goods issued to the project site create an unexplained discrepancy between the order's delivered record and the project's received record, with no reference recorded.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Issue complimentary goods to a project site outside the priced order lines, and check whether the resulting gap between order and project records is explained anywhere.
```

## G08-SALE_PROJECT_STOCK-Q020

```yaml
QID: G08-SALE_PROJECT_STOCK-Q020
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a project site receives a substitute item in place of the one actually ordered due to a stock-out, the order's delivered-quantity reconciliation flags the substitution rather than silently treating it as satisfying the original item.
WHY_IT_MATTERS: >
  An unflagged substitution would misrepresent what the customer actually received against what they ordered.
DISCONFIRMING_OBSERVATION: >
  A substituted item is recorded against the order as fulfilling the original ordered item's quantity with no flag that a substitution occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deliver a substitute item to a project site in place of the ordered item, and check whether the order's fulfilment record flags the substitution.
```

## G08-SALE_PROJECT_STOCK-Q021

```yaml
QID: G08-SALE_PROJECT_STOCK-Q021
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A backorder on an order tied to a project blocks the order's own fulfilment view from showing complete, and its effect on the project's own material-readiness indicator is a separately documented rule.
WHY_IT_MATTERS: >
  An undocumented assumption either way could make the project appear ready to proceed when it is not, or block it when it need not be.
DISCONFIRMING_OBSERVATION: >
  The project is treated as materially ready to proceed despite an unresolved backorder on the order supplying it, with no documented rule connecting the two states.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a backorder on an order feeding a project, and check whether the project's own readiness indicator accounts for the unresolved backorder.
```

## G08-SALE_PROJECT_STOCK-Q022

```yaml
QID: G08-SALE_PROJECT_STOCK-Q022
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where the order's fulfilling warehouse belongs to a different company than the project in a multi-company setup, the physical movement's stock valuation and delivery record are attributed to one documented company.
WHY_IT_MATTERS: >
  An ambiguous attribution across companies could mix one entity's inventory records with another's without proper separation.
DISCONFIRMING_OBSERVATION: >
  The same physical movement's valuation or delivery record appears attributable to either company with no single documented authority resolving it.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  In a multi-company setup, deliver goods under an order to a project belonging to a different company, and check which company's records are authoritative for the movement.
```

## G08-SALE_PROJECT_STOCK-Q023

```yaml
QID: G08-SALE_PROJECT_STOCK-Q023
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project task being marked complete does not, by itself, retroactively change the linked order's delivered-quantity record if the underlying goods movement was never actually finalized.
WHY_IT_MATTERS: >
  Letting a task's completion status drive the order's own delivery record would decouple what was recorded from what physically happened.
DISCONFIRMING_OBSERVATION: >
  Marking a project task complete changes the order's own delivered-quantity record even though the corresponding goods movement was never actually finalized.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Mark a project task complete before its corresponding goods movement is finalized, and check whether the order's delivered-quantity record changes as a result.
```

## G08-SALE_PROJECT_STOCK-Q024

```yaml
QID: G08-SALE_PROJECT_STOCK-Q024
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Goods damaged at a project site after delivery but before being logged as consumed are attributed to a single documented cause path that determines how any replacement is ordered.
WHY_IT_MATTERS: >
  An unattributed damage event would leave it unclear whether a replacement should be charged to the order or handled separately.
DISCONFIRMING_OBSERVATION: >
  Damage discovered at the project site after delivery has no documented attribution, leaving it unclear whether a replacement should be ordered against the original order or handled separately.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record goods as damaged at a project site after delivery but before consumption, and check whether the damage is attributed to a documented cause path.
```

## G08-SALE_PROJECT_STOCK-Q025

```yaml
QID: G08-SALE_PROJECT_STOCK-Q025
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An emergency reallocation that pulls stock earmarked for a project-linked order to cover a different, unrelated order results in a visible change to the original order's promised date or quantity.
WHY_IT_MATTERS: >
  A customer-facing promise that silently stays the same while its supporting stock is gone would set an expectation the business can no longer meet.
DISCONFIRMING_OBSERVATION: >
  Stock earmarked for a project-linked order is reallocated to a different order without the original order's promised date or quantity reflecting any change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reallocate stock earmarked for a project-linked order to a different, unrelated order, and check whether the original order's promise updates to reflect the loss.
```

## G08-SALE_PROJECT_STOCK-Q026

```yaml
QID: G08-SALE_PROJECT_STOCK-Q026
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Where the order supports partial invoicing per delivery but the project's milestone billing expects material fully on site, a partial delivery satisfying only the order's own trigger does not also satisfy the project's separate milestone trigger without a documented, intended link.
WHY_IT_MATTERS: >
  An unintended cross-trigger could release a milestone invoice for work that is not actually materially ready.
DISCONFIRMING_OBSERVATION: >
  A partial delivery under the order's own policy also releases a project milestone invoice that was defined to require full on-site material, with no documented link explaining why.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure an order for partial delivery invoicing and a project milestone requiring full on-site material, make a partial delivery, and check whether the project milestone is also triggered.
```

## G08-SALE_PROJECT_STOCK-Q027

```yaml
QID: G08-SALE_PROJECT_STOCK-Q027
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Confirming delivery of goods to a project site while another user simultaneously puts the project on hold resolves to one consistent, recorded outcome rather than an unrecorded race.
WHY_IT_MATTERS: >
  An unrecorded race condition could leave it unknown whether a delivery actually proceeded or was silently dropped.
DISCONFIRMING_OBSERVATION: >
  Near-simultaneous delivery confirmation and project hold produce an inconsistent or unrecorded outcome for whether the delivery actually proceeded.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a delivery confirmation and a project hold action for the same project at nearly the same time, and check the resulting delivery state and whether it is consistently explainable.
```

## G08-SALE_PROJECT_STOCK-Q028

```yaml
QID: G08-SALE_PROJECT_STOCK-Q028
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Stock already soft-reserved by an order for an earlier project phase is visible to later phases of the same project as committed rather than as freely available.
WHY_IT_MATTERS: >
  A later phase planning against stock that is actually already committed would build its own promise on a false assumption of availability.
DISCONFIRMING_OBSERVATION: >
  A later project phase's material availability view shows stock as free that is actually already soft-reserved by an earlier phase of the same project's order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve stock for an early phase of a multi-phase project's order, and check whether a later phase's own availability view correctly shows that stock as already committed.
```

## G08-SALE_PROJECT_STOCK-Q029

```yaml
QID: G08-SALE_PROJECT_STOCK-Q029
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a project site is closed or relocated, an order still configured to ship to the old site address either blocks the shipment or clearly flags the stale address.
WHY_IT_MATTERS: >
  Shipping to an address that no longer exists would waste the goods and delay the customer with no warning to anyone.
DISCONFIRMING_OBSERVATION: >
  An order tied to a relocated or closed project site proceeds to ship to the old address with no flag or block.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Close or relocate a project site after an order was configured to ship there, and attempt to proceed with that shipment.
```

## G08-SALE_PROJECT_STOCK-Q030

```yaml
QID: G08-SALE_PROJECT_STOCK-Q030
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A defective replacement issued to a project site to correct previously consumed material is traceable back to the original order line it corrects.
WHY_IT_MATTERS: >
  An untraceable replacement would make it impossible to reconcile what was actually delivered against what the order originally specified.
DISCONFIRMING_OBSERVATION: >
  A replacement issued for defective material consumed at the project site has no recorded link back to the original order line or the defective consumption it corrects.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Issue a replacement for material found defective after project consumption, and check whether the replacement is traceable back to the original order line.
```

## G08-SALE_PROJECT_STOCK-Q031

```yaml
QID: G08-SALE_PROJECT_STOCK-Q031
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  At project closure, a reconciliation between the project's total logged consumption and the order's total delivered quantity treats one of the two as the documented authoritative figure when they disagree.
WHY_IT_MATTERS: >
  An unassigned discrepancy at closure would leave the true material outcome permanently unresolved.
DISCONFIRMING_OBSERVATION: >
  A discrepancy found between the project's logged consumption and the order's delivered record at closure has no documented rule for which figure governs the reconciliation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a discrepancy between a project's logged consumption and its order's delivered record, close the project, and check whether the reconciliation resolves to a documented authoritative figure.
```

## G08-SALE_PROJECT_STOCK-Q032

```yaml
QID: G08-SALE_PROJECT_STOCK-Q032
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Goods consumed at the project site by a subcontractor working on behalf of the company are distinguished in the records from goods consumed directly by the company's own staff.
WHY_IT_MATTERS: >
  Indistinguishable records would make it impossible to know how much company-owned material was effectively handed to a third party.
DISCONFIRMING_OBSERVATION: >
  Material consumed by a subcontractor at the project site is recorded identically to material consumed by the company's own staff, with no way to distinguish the two afterward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have a subcontractor consume company-supplied material at a project site alongside the company's own staff, and check whether the two are distinguishable in the records.
```

## G08-SALE_PROJECT_STOCK-Q033

```yaml
QID: G08-SALE_PROJECT_STOCK-Q033
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Increasing the order's quantity after some goods have already been delivered to the project correctly updates what the project's own consumption tracking still expects to receive.
WHY_IT_MATTERS: >
  A project that believes its need was already fully met by the smaller original quantity would under-plan for the additional amount now due.
DISCONFIRMING_OBSERVATION: >
  The project's own tracking continues to show its material need as fully met after the order's quantity was increased, ignoring the additional amount now due.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Increase a confirmed order's quantity after partial delivery to its linked project, and check whether the project's own outstanding-need tracking reflects the increase.
```

## G08-SALE_PROJECT_STOCK-Q034

```yaml
QID: G08-SALE_PROJECT_STOCK-Q034
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When two project tasks draw from the same delivered batch of material under one order line, one task over-consuming its share does not silently reduce what remains available to the other task without any warning.
WHY_IT_MATTERS: >
  An unwarned shortfall would leave the second task's own team unaware they are about to run short.
DISCONFIRMING_OBSERVATION: >
  One task's over-consumption from a shared delivered batch silently leaves the other task short, with neither task flagged about the shortfall.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have two project tasks draw from the same delivered batch under one order line, cause one to over-consume, and check whether the other task is warned of reduced availability.
```

## G08-SALE_PROJECT_STOCK-Q035

```yaml
QID: G08-SALE_PROJECT_STOCK-Q035
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Reversing a project's logged over-issue of material returns that quantity to the order's own available-to-deliver pool through a documented path.
WHY_IT_MATTERS: >
  A reversal that vanishes into an untracked adjustment would leave neither the order nor the project able to account for the quantity.
DISCONFIRMING_OBSERVATION: >
  Reversing an over-issue at the project removes the quantity from the project's record without it reappearing anywhere in the order's own available or delivered figures.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reverse a logged over-issue of material at the project, and check whether the reversed quantity is traceable back into the order's own stock figures.
```

## G08-SALE_PROJECT_STOCK-Q036

```yaml
QID: G08-SALE_PROJECT_STOCK-Q036
MODULE: sale_project_stock
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Duplicating a project to plan a similar future engagement does not cause the duplicate to
  inherit a live stock reservation or lot assignment held by the original project's still-open
  order line.
WHY_IT_MATTERS: >
  An inherited live reservation would let the new, unrelated project silently draw on, or appear
  to already hold, stock actually reserved for the original engagement's own commitment.
DISCONFIRMING_OBSERVATION: >
  A duplicated project's order line shows the same stock reservation or lot assignment as the
  original project's still-open order line.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Duplicate a project whose order line currently holds an open stock reservation or lot
  assignment, and check whether the duplicate's order line shows that same reservation or lot
  assignment.
```
