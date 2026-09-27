# SMEsPlus ENTERPRISE SUITE
## GMVQ — G07 PURCHASE / purchase_mrp Module Bridge MVQ Bank

**Document ID:** GMVQ-G07-PURCHASE_MRP-MVQ48-V1.00
**Group:** G07 PURCHASE
**Module Metadata:** `purchase_mrp`
**Wave:** W2
**Author Cell:** P15 (GMVQ Question Factory — Internal Production Team 15, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `purchase_mrp`, the bridge where production
demand generates procurement. Per the GMVQ Bridge Module Rule V1.00, every question here fails only
at the seam between an open production order's requirement and the procurement it triggers: computed
quantity and rounding, the demand's survival or disappearance as the production order changes,
consolidation versus duplication across multiple production orders, which date governs when the
component's need-date and the achievable delivery date disagree, review and authority before money
is committed, and traceability from a generated order back to the demand that caused it. No question
here concerns the physical receipt of goods — that seam belongs to `purchase_stock` — and no
question restates a pure production-scheduling behaviour (`mrp`) or a pure ordering behaviour
(`purchase`) in isolation; each was tested against the bridge rule's removal test before being kept,
and cross-checked against the sibling `purchase` bank's authored hypotheses on disk at authoring
time. Coverage spans business capability, business rule, state transition, configuration dependency,
role and permission, exception path, cancellation, reversal, negative case, cross-module dependency,
optional behaviour, auditability, tenant/company boundary, concurrency and ordering, runtime
reachability, configuration reachability, and source/runtime contradiction potential.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material seam hypotheses; none was
  trimmed or stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table,
  field, method, XML ID, API path), and the module's own metadata name never appears outside the
  `MODULE:` field.
- No question concerns the physical receipt of goods; that seam is reserved to `purchase_stock`.
- Every question passed the bridge removal test and was cross-checked against the `purchase` base
  bank's authored HYPOTHESIS lines on disk at authoring time to avoid restating its invariants.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G07-PURCHASE_MRP-Q001

```yaml
QID: G07-PURCHASE_MRP-Q001
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A single open production order's shortage for a purchased component generates procurement demand exactly once, not duplicated by a later recomputation of the same still-open order's needs.
WHY_IT_MATTERS: >
  Duplicate demand for the same shortage would generate excess procurement commitments and excess inventory that were never actually needed.
DISCONFIRMING_OBSERVATION: >
  Recomputing an unchanged, still-open production order's requirements a second time generates an additional procurement demand alongside the one already generated for the same shortage.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Generate procurement demand from an open production order, trigger a recomputation of that same order with nothing changed, and check for a second generated demand.
```

## G07-PURCHASE_MRP-Q002

```yaml
QID: G07-PURCHASE_MRP-Q002
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The generated procurement quantity respects any configured minimum order quantity or ordering multiple for that component, rather than requesting the raw shortage figure unmodified.
WHY_IT_MATTERS: >
  Ignoring a configured minimum or multiple would generate procurement requests the vendor cannot actually fulfil as specified.
DISCONFIRMING_OBSERVATION: >
  A component configured with a minimum order quantity or multiple generates a procurement demand for a raw shortage figure that does not respect that minimum or multiple.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a minimum order quantity or multiple for a component, create a production shortage smaller than or not aligned with it, and inspect the generated demand's quantity.
```

## G07-PURCHASE_MRP-Q003

```yaml
QID: G07-PURCHASE_MRP-Q003
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  When the raw shortage is smaller than the configured minimum order quantity, the generated demand is rounded up to that minimum rather than silently dropped as too small to act on.
WHY_IT_MATTERS: >
  Silently dropping a small shortage would leave a real production requirement permanently unfulfilled with no visible indication that anything was skipped.
DISCONFIRMING_OBSERVATION: >
  A shortage smaller than the configured minimum order quantity generates no procurement demand at all, with no record that a below-minimum need existed.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a production shortage smaller than the component's configured minimum order quantity and check whether any demand is generated at all.
```

## G07-PURCHASE_MRP-Q004

```yaml
QID: G07-PURCHASE_MRP-Q004
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reducing the production order's quantity after procurement demand has already been committed either reduces the generated demand correspondingly or raises a visible review flag — it does not leave the original, now-excessive committed quantity unremarked.
WHY_IT_MATTERS: >
  An unremarked excess commitment after a demand reduction would leave money committed to a need that no longer fully exists.
DISCONFIRMING_OBSERVATION: >
  Reducing a production order's quantity after its procurement demand was already committed leaves the committed procurement quantity unchanged with no flag noting the excess.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate and commit procurement demand from a production order, then reduce that order's quantity, and check whether the committed procurement is flagged as excessive.
```

## G07-PURCHASE_MRP-Q005

```yaml
QID: G07-PURCHASE_MRP-Q005
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a production order after its procurement demand has already been committed leaves a visible orphaned-demand indicator rather than silently discarding the link with no trace.
WHY_IT_MATTERS: >
  A silently discarded link would leave a committed procurement order with no visible reason attached to it, making it look like ordinary unrelated demand.
DISCONFIRMING_OBSERVATION: >
  Cancelling a production order whose demand was already committed to a procurement order leaves that procurement order with no indication that its originating demand was cancelled.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Commit procurement demand from a production order, cancel that production order, and inspect whether the procurement order shows any orphaned-demand indicator.
```

## G07-PURCHASE_MRP-Q006

```yaml
QID: G07-PURCHASE_MRP-Q006
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Rescheduling a production order's dates after its procurement demand already exists updates the generated demand's need-by date, or explicitly flags the mismatch — the two dates do not silently diverge with no signal.
WHY_IT_MATTERS: >
  A silently stale need-date would leave procurement planning against a date production no longer actually intends to use.
DISCONFIRMING_OBSERVATION: >
  Rescheduling a production order to a new date leaves its already-generated procurement demand's need-by date unchanged with no update or flag.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate procurement demand from a production order, reschedule that order's dates, and check whether the demand's need-by date reflects the change or is flagged.
```

## G07-PURCHASE_MRP-Q007

```yaml
QID: G07-PURCHASE_MRP-Q007
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Component demand from two open production orders needing the same component is either consolidated into one procurement request or kept distinct with clear traceability to each source — never merged in a way that loses which order needed how much.
WHY_IT_MATTERS: >
  Losing the per-order breakdown of a merged demand would make it impossible to later attribute a shortage or a delay to the production order actually responsible for it.
DISCONFIRMING_OBSERVATION: >
  Two production orders' demand for the same component merges into a single generated line with no way to determine how much of it came from which order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create two open production orders each needing the same component and inspect whether the resulting generated demand retains per-order attribution.
```

## G07-PURCHASE_MRP-Q008

```yaml
QID: G07-PURCHASE_MRP-Q008
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When two production orders' demand is consolidated into one generated procurement line, reducing or cancelling one contributing production order correctly reduces only that order's own share of the consolidated quantity.
WHY_IT_MATTERS: >
  Reducing the wrong share would either leave a genuine need uncovered or cancel procurement that another, still-active order still requires.
DISCONFIRMING_OBSERVATION: >
  Cancelling one of two production orders contributing to a consolidated procurement line reduces the consolidated quantity by more or less than that order's own actual contribution.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Consolidate demand from two production orders into one procurement line, cancel one of the two orders, and verify the resulting quantity reduction matches only that order's share.
```

## G07-PURCHASE_MRP-Q009

```yaml
QID: G07-PURCHASE_MRP-Q009
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Where the date production needs a component and the date procurement can realistically deliver it differ, both dates are retained rather than the generated order silently overwriting one with the other without recording that they disagree.
WHY_IT_MATTERS: >
  Silently overwriting the true need-date with an achievable delivery date, or the reverse, would hide a real scheduling conflict from anyone reviewing the plan.
DISCONFIRMING_OBSERVATION: >
  A generated procurement order shows only one date where the true production need-date and the realistically achievable delivery date differ, with no record of the other or of the disagreement.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a shortage where the achievable delivery date is later than production's need-date, and inspect which date or dates the generated order actually shows.
```

## G07-PURCHASE_MRP-Q010

```yaml
QID: G07-PURCHASE_MRP-Q010
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where the earliest achievable delivery date is later than the date production needs the component, that shortfall is surfaced as a visible exception rather than the generated order simply appearing on schedule against a silently adjusted date.
WHY_IT_MATTERS: >
  A shortage disguised as an on-time order would prevent anyone from acting on a genuine risk to the production schedule until it is too late.
DISCONFIRMING_OBSERVATION: >
  A generated order whose only achievable delivery date is later than production's need date appears identical, with no exception flag, to an order that can genuinely arrive on time.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Create a shortage with a lead time longer than the time remaining before production needs the component, and inspect whether the generated order is distinguishably flagged.
```

## G07-PURCHASE_MRP-Q011

```yaml
QID: G07-PURCHASE_MRP-Q011
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A change to the bill of materials after procurement has already been triggered for the original component list does not silently alter the quantity or identity on an already-generated procurement order.
WHY_IT_MATTERS: >
  Silently altering an already-generated, possibly already-committed order after the fact would change a vendor-facing commitment without any explicit action taken toward the vendor.
DISCONFIRMING_OBSERVATION: >
  Editing the bill of materials after procurement demand was already generated from it changes the quantity or component on the already-generated procurement order with no separate triggering action.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate procurement demand from a bill of materials, edit that bill of materials afterward, and check whether the already-generated procurement order changed.
```

## G07-PURCHASE_MRP-Q012

```yaml
QID: G07-PURCHASE_MRP-Q012
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Substituting a component during production after that component was already ordered leaves the original order's traceability to the original demand intact, and the substitution's own new demand is a distinct, separately visible event.
WHY_IT_MATTERS: >
  Conflating a substitution with the original demand would obscure that a change occurred and make it unclear which component is actually still needed and which was already ordered unnecessarily.
DISCONFIRMING_OBSERVATION: >
  Substituting a component after it was already ordered leaves no distinguishable record that a substitution occurred, or silently reattributes the original order to the new component.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Order a component for production, then substitute a different component in the production order, and inspect the resulting demand and traceability records.
```

## G07-PURCHASE_MRP-Q013

```yaml
QID: G07-PURCHASE_MRP-Q013
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  When a component is already reserved from existing stock or already covered by another open order, procurement demand is not separately generated for the quantity already covered by that reservation.
WHY_IT_MATTERS: >
  Generating demand for an already-covered quantity would create unnecessary procurement and inflate inventory beyond what production actually still needs.
DISCONFIRMING_OBSERVATION: >
  A component quantity already reserved or already on another open order still generates additional procurement demand for that same already-covered quantity.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve a component's needed quantity from existing stock or another open order, then trigger demand computation for a production order needing it, and check the generated demand quantity.
```

## G07-PURCHASE_MRP-Q014

```yaml
QID: G07-PURCHASE_MRP-Q014
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Demand generated for a component that already has an open, uncommitted procurement order outstanding either extends that existing order or is flagged as a potential duplicate, rather than silently generating an unrelated second order for the same need.
WHY_IT_MATTERS: >
  Two unrelated, unlinked orders for the same need would double the committed procurement without anyone realizing the need was already being addressed.
DISCONFIRMING_OBSERVATION: >
  A component with an existing open, uncommitted procurement order generates a wholly separate second procurement order for the same need, with no link or flag connecting the two.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an open, uncommitted procurement order for a component, then trigger new demand for that same component, and inspect whether it extends, flags, or duplicates the existing order.
```

## G07-PURCHASE_MRP-Q015

```yaml
QID: G07-PURCHASE_MRP-Q015
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A generated procurement order that has not yet been reviewed or confirmed by a person is distinguishable in state from one that has been reviewed, so money cannot be committed by automatic generation alone without a visible confirmation step.
WHY_IT_MATTERS: >
  An unreviewed order indistinguishable from a confirmed one would let automatically generated demand commit real money with no human checkpoint.
DISCONFIRMING_OBSERVATION: >
  A freshly auto-generated procurement order appears in the same state, and can be acted on by a vendor, identically to one a person has actually reviewed and confirmed.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Let procurement demand auto-generate an order and inspect its state before any person reviews it, comparing that state to a reviewed and confirmed order.
```

## G07-PURCHASE_MRP-Q016

```yaml
QID: G07-PURCHASE_MRP-Q016
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Where a generated order is configured to auto-confirm without review, that configuration is an explicit, visible setting rather than an unstated default that differs silently between components.
WHY_IT_MATTERS: >
  An unstated, inconsistent default would mean some components' demand commits money automatically while others do not, with nobody aware of the difference.
DISCONFIRMING_OBSERVATION: >
  Two components generate procurement demand with different auto-confirmation behaviour, and neither the setting nor its difference is visible anywhere in their configuration.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Compare the auto-confirmation behaviour of generated procurement for two different components and check whether any visible setting explains the difference.
```

## G07-PURCHASE_MRP-Q017

```yaml
QID: G07-PURCHASE_MRP-Q017
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Given a specific generated procurement line, the production order or orders whose demand caused it can be identified even after that production order has since completed, been cancelled, or been archived.
WHY_IT_MATTERS: >
  Losing this link after the source order's lifecycle moves on would make later audits unable to explain why a given procurement order was ever created.
DISCONFIRMING_OBSERVATION: >
  A generated procurement line's link to its originating production order no longer resolves once that production order has completed, been cancelled, or archived.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate procurement demand from a production order, advance that order to completion, cancellation, or archival, and check whether the procurement line's origin is still traceable.
```

## G07-PURCHASE_MRP-Q018

```yaml
QID: G07-PURCHASE_MRP-Q018
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where more than one production order contributed to a consolidated generated line, the traceability records the quantity or proportion attributable to each contributing order, not merely that some unspecified production demand exists.
WHY_IT_MATTERS: >
  An unspecified attribution would make it impossible to determine, after the fact, how much of a shared procurement order served which specific production need.
DISCONFIRMING_OBSERVATION: >
  A consolidated procurement line shows that more than one production order contributed to it but provides no breakdown of how much each one contributed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consolidate demand from two production orders into one procurement line and inspect whether the per-order contribution is individually recorded.
```

## G07-PURCHASE_MRP-Q019

```yaml
QID: G07-PURCHASE_MRP-Q019
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A component procured to replenish general stock is distinguishable from a component procured to satisfy a specific production order's named shortage, even when both appear as ordinary lines on the same generated procurement order.
WHY_IT_MATTERS: >
  Conflating the two would make it impossible to tell whether a given procured quantity is free stock or already spoken for by a specific production need.
DISCONFIRMING_OBSERVATION: >
  A procurement order combining a general-stock replenishment line and a production-order-specific line shows no way to distinguish which line serves which purpose.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate a procurement order containing both a general-stock replenishment line and a line tied to a specific production order's shortage, and inspect whether each is distinguishable.
```

## G07-PURCHASE_MRP-Q020

```yaml
QID: G07-PURCHASE_MRP-Q020
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a generated procurement order that was created to satisfy a specific production order's demand leaves that production order's shortage visibly unresolved again, rather than the production order continuing to believe the component is still incoming.
WHY_IT_MATTERS: >
  A production order that believes a cancelled procurement is still incoming would proceed toward a shortage it thinks is already covered.
DISCONFIRMING_OBSERVATION: >
  Cancelling a procurement order tied to a specific production order's demand leaves that production order still showing the component as covered or incoming.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate procurement demand for a specific production order's shortage, cancel the resulting procurement order, and inspect whether the production order's shortage reappears as unresolved.
```

## G07-PURCHASE_MRP-Q021

```yaml
QID: G07-PURCHASE_MRP-Q021
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  When the production order that caused a generated demand is deleted outright, the previously generated procurement order is not left with an unexplainable, dangling origin.
WHY_IT_MATTERS: >
  A procurement order with no explainable origin left behind after a deletion would be indistinguishable from ordinary demand nobody can now account for.
DISCONFIRMING_OBSERVATION: >
  Deleting the production order that caused a generated procurement order leaves that procurement order in place with no remaining indication of why it exists.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate procurement demand from a production order, delete that production order outright, and check the state of the previously generated procurement order.
```

## G07-PURCHASE_MRP-Q022

```yaml
QID: G07-PURCHASE_MRP-Q022
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A change to the component's replenishment trigger rule after demand has already been generated does not retroactively alter demand that was already committed under the prior rule.
WHY_IT_MATTERS: >
  Retroactively altering an already-committed demand would change a live procurement commitment purely because an unrelated configuration setting changed later.
DISCONFIRMING_OBSERVATION: >
  Changing a component's replenishment trigger rule after demand was already committed changes the quantity or existence of that already-committed demand.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Commit procurement demand for a component, change its replenishment trigger rule afterward, and check whether the already-committed demand changed.
```

## G07-PURCHASE_MRP-Q023

```yaml
QID: G07-PURCHASE_MRP-Q023
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where a production order's required quantity increases after procurement demand was already generated for the original, smaller quantity, the shortfall between the two is surfaced as new or additional demand rather than assumed already covered.
WHY_IT_MATTERS: >
  Assuming the increase is already covered would leave a genuine additional shortage silently unaddressed.
DISCONFIRMING_OBSERVATION: >
  Increasing a production order's required quantity after demand was already generated for a smaller amount produces no additional demand for the resulting shortfall.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate demand for a production order's original quantity, then increase that quantity, and check whether additional demand is generated for the difference.
```

## G07-PURCHASE_MRP-Q024

```yaml
QID: G07-PURCHASE_MRP-Q024
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Two components with an identical minimum order quantity rule but different actual shortages both round correctly and independently — one component's rounding computation does not affect the quantity generated for a different component.
WHY_IT_MATTERS: >
  A shared rounding computation bleeding across components would produce incorrect procurement quantities for components that were never actually short by that amount.
DISCONFIRMING_OBSERVATION: >
  Generating demand for two components sharing the same minimum order quantity rule but different shortages produces a rounded quantity for one that reflects the other's shortage rather than its own.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create two components with the same minimum order quantity setting but different shortages, generate demand for both together, and verify each rounds independently.
```

## G07-PURCHASE_MRP-Q025

```yaml
QID: G07-PURCHASE_MRP-Q025
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where a production order is split into two, the procurement demand attributable to the original order is divided or re-linked consistently with the split, not left pointing only at whichever resulting fragment happens to exist first.
WHY_IT_MATTERS: >
  An arbitrary attribution to only one fragment would misrepresent which portion of the split production actually still needs the procured component.
DISCONFIRMING_OBSERVATION: >
  Splitting a production order that already has generated procurement demand leaves that demand linked entirely to one resulting fragment regardless of which fragment actually retains the corresponding requirement.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate procurement demand from a production order, split that order into two, and inspect how the existing demand's link is distributed between the two resulting orders.
```

## G07-PURCHASE_MRP-Q026

```yaml
QID: G07-PURCHASE_MRP-Q026
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A component whose lead time exceeds the time remaining before production needs it produces a visible, distinguishable exception rather than a generated order indistinguishable from any on-time order.
WHY_IT_MATTERS: >
  An indistinguishable exception would mean nobody is alerted to a genuine risk of production stoppage until the missed date actually arrives.
DISCONFIRMING_OBSERVATION: >
  A component whose known lead time cannot meet production's need-by date generates a procurement order with no visible exception flag distinguishing it from a normally achievable order.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Configure a component's lead time to exceed the time remaining before a production order's need date, generate demand, and check for a distinguishing exception.
```

## G07-PURCHASE_MRP-Q027

```yaml
QID: G07-PURCHASE_MRP-Q027
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Demand from a released, firm production order and demand from a mere forecast or planned, not yet released, production order do not collapse into a single, undifferentiated procurement trigger without a visible distinction of firmness.
WHY_IT_MATTERS: >
  Committing real procurement money against a forecast that is not yet firm would create financial exposure for demand that may never actually materialize.
DISCONFIRMING_OBSERVATION: >
  Forecasted, not-yet-released production demand generates a committed procurement order with no distinguishing indication that the underlying production has not actually been released.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create both a released production order and a forecasted, unreleased one needing the same component, and inspect whether the resulting procurement demand distinguishes firmness.
```

## G07-PURCHASE_MRP-Q028

```yaml
QID: G07-PURCHASE_MRP-Q028
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A generated procurement order's need-by date, once the underlying production order's date changes again, is updated only through one defined recomputation process, not through two different automatic pathways producing two different resulting dates for the same case.
WHY_IT_MATTERS: >
  Two competing automatic pathways producing different dates for the same case would make the generated order's date unpredictable and untrustworthy.
DISCONFIRMING_OBSERVATION: >
  Changing a production order's date after procurement demand exists produces two different resulting need-by dates on the generated order depending on which triggering path caused the recomputation.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Change a production order's date through two different available paths that each trigger recomputation and compare the resulting generated order's need-by date in each case.
```

## G07-PURCHASE_MRP-Q029

```yaml
QID: G07-PURCHASE_MRP-Q029
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where a component is subcontracted (produced by a vendor from supplied materials) rather than simply purchased outright, the demand computation for that distinct scenario does not silently follow the same rounding and quantity path as an ordinary purchased component when the two are meant to differ.
WHY_IT_MATTERS: >
  Applying the wrong computation path would generate an incorrect quantity or an incorrect kind of procurement document for a fundamentally different kind of supply arrangement.
DISCONFIRMING_OBSERVATION: >
  A subcontracted component's generated demand follows the identical computation and rounding path as an ordinary purchased component, in a case where the two are configured to differ.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure one component as subcontracted and a comparable one as ordinarily purchased, generate demand for both, and compare the computation paths used.
```

## G07-PURCHASE_MRP-Q030

```yaml
QID: G07-PURCHASE_MRP-Q030
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A component that can be either manufactured or purchased depending on context generates procurement demand only through the path appropriate to how that specific production order will actually obtain it, not through both paths at once.
WHY_IT_MATTERS: >
  Triggering both paths at once would generate redundant procurement for a component the production order will actually make itself, or vice versa.
DISCONFIRMING_OBSERVATION: >
  A production order using the manufactured route for a make-or-buy component still generates a procurement demand for that same component as if it were also being purchased.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a component as make-or-buy, run a production order that resolves to the manufactured route, and check whether procurement demand is also generated.
```

## G07-PURCHASE_MRP-Q031

```yaml
QID: G07-PURCHASE_MRP-Q031
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing a production order from an in-progress or done state back to an earlier state does not leave any procurement demand it had generated still asserting that the demand is needed when the underlying requirement has, in fact, been undone.
WHY_IT_MATTERS: >
  A demand that still claims to be needed after its requirement was undone would drive unnecessary procurement for a need that no longer exists.
DISCONFIRMING_OBSERVATION: >
  Reversing a production order back to an earlier state leaves its previously generated procurement demand unchanged and still marked as needed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate procurement demand from a production order, reverse or unbuild that production order back to an earlier state, and inspect whether the demand still claims to be needed.
```

## G07-PURCHASE_MRP-Q032

```yaml
QID: G07-PURCHASE_MRP-Q032
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a generated procurement line already has a committed quantity and the underlying production need is later satisfied by some other means, the resulting surplus is surfaced as excess or no-longer-needed demand rather than silently absorbed as normal replenishment.
WHY_IT_MATTERS: >
  Silently absorbing a surplus as ordinary replenishment would hide the fact that a committed procurement no longer corresponds to any actual production need.
DISCONFIRMING_OBSERVATION: >
  A committed procurement quantity whose underlying production need was satisfied by other means shows no distinguishing surplus or no-longer-needed indicator.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Commit procurement demand for a production need, then satisfy that need through a substitute or reservation, and inspect whether the committed procurement is flagged as surplus.
```

## G07-PURCHASE_MRP-Q033

```yaml
QID: G07-PURCHASE_MRP-Q033
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Multiple recomputations of the same still-open production order's requirements over time do not each generate a fresh duplicate procurement demand for a shortage a prior computation already covered.
WHY_IT_MATTERS: >
  Repeated duplicate generation from routine recomputation would multiply procurement commitments for a single unchanged shortage every time something unrelated triggers a recompute.
DISCONFIRMING_OBSERVATION: >
  Triggering several unrelated recomputations of a production order whose shortage was already covered by a prior generated demand produces a new demand each time.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Generate demand covering a production order's full shortage, trigger several unrelated recomputations of that order, and check whether additional demand is generated each time.
```

## G07-PURCHASE_MRP-Q034

```yaml
QID: G07-PURCHASE_MRP-Q034
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where a component is needed at more than one level of a multi-level bill of materials for the same top-level production order, the aggregate demand generated is the correctly netted total, not the sum of each level's raw, unnetted requirement.
WHY_IT_MATTERS: >
  An unnetted sum across levels would overstate the true procurement need whenever the same component appears at more than one level of the same build.
DISCONFIRMING_OBSERVATION: >
  A component appearing at two levels of the same multi-level build generates a total demand equal to the simple sum of each level's raw requirement rather than the properly netted total.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Build a multi-level bill of materials where one component is required at two levels for the same top-level order, generate demand, and check the resulting total against the correctly netted figure.
```

## G07-PURCHASE_MRP-Q035

```yaml
QID: G07-PURCHASE_MRP-Q035
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A user who manually edits a generated procurement order's quantity downward, below what the production order actually needs, does not cause the production order to silently believe its full requirement is covered.
WHY_IT_MATTERS: >
  A production order that believes an under-quantity edit still covers it in full would proceed toward a shortage nobody is now tracking.
DISCONFIRMING_OBSERVATION: >
  Manually reducing a generated procurement order's quantity below the production order's actual need leaves the production order showing its requirement as fully covered.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate procurement demand matching a production order's full need, manually reduce the generated order's quantity, and check whether the production order still shows full coverage.
```

## G07-PURCHASE_MRP-Q036

```yaml
QID: G07-PURCHASE_MRP-Q036
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where the same production order needs the same component through two different routes, a main requirement and a byproduct-consumption requirement, both are reflected in the total generated demand, not only whichever route's computation happened to run last.
WHY_IT_MATTERS: >
  Reflecting only the last-run route would understate the true total need for a component consumed through more than one path in the same build.
DISCONFIRMING_OBSERVATION: >
  A production order consuming the same component through two distinct routes generates total demand reflecting only one route's requirement.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Configure a production order that consumes the same component through two distinct requirement routes, generate demand, and check whether the total reflects both.
```

## G07-PURCHASE_MRP-Q037

```yaml
QID: G07-PURCHASE_MRP-Q037
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A production order placed on hold after demand was generated does not cause its already-generated procurement order to be automatically treated as urgent — the procurement's priority reflects the current, on-hold state of the demand behind it, or the mismatch is surfaced.
WHY_IT_MATTERS: >
  Treating a paused requirement as urgent would misdirect procurement effort and vendor communication toward a need that is not currently being acted on.
DISCONFIRMING_OBSERVATION: >
  Placing a production order on hold leaves its already-generated procurement order marked with the same urgency as an active, unpaused requirement, with no flag noting the mismatch.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Generate procurement demand from an active production order, put that order on hold, and inspect whether the procurement order's priority or status reflects the change.
```

## G07-PURCHASE_MRP-Q038

```yaml
QID: G07-PURCHASE_MRP-Q038
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Demand generated for a component whose supply parameters mark it as make-to-order for one specific production order remains attributable to only that order, even if the generated procurement order is later manually edited to a larger quantity.
WHY_IT_MATTERS: >
  Losing the make-to-order attribution after a manual edit would let the surplus quantity be silently treated as if it could satisfy other, unrelated demand it was never intended for.
DISCONFIRMING_OBSERVATION: >
  Editing a make-to-order-generated procurement order to a larger quantity causes the entire quantity to appear available to satisfy other production orders' demand for the same component.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate a make-to-order procurement demand tied to one production order, manually increase its quantity, and check whether the surplus becomes available to other orders.
```

## G07-PURCHASE_MRP-Q039

```yaml
QID: G07-PURCHASE_MRP-Q039
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where two different production sites or warehouses each run their own production order for the same component, demand from each is scoped and generated according to its own site or warehouse boundary, not pooled across sites without an explicit configuration allowing that.
WHY_IT_MATTERS: >
  Unintended pooling across sites would generate procurement that satisfies one site's paperwork while leaving the other site's actual physical need unaddressed.
DISCONFIRMING_OBSERVATION: >
  Production orders at two different sites needing the same component generate a single pooled procurement demand with no site-scoped breakdown and no configuration explicitly enabling pooling.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Run production orders needing the same component at two different sites or warehouses and inspect whether the generated demand is scoped per site or pooled.
```

## G07-PURCHASE_MRP-Q040

```yaml
QID: G07-PURCHASE_MRP-Q040
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A change to the production order's routing or operation sequence, unrelated to component quantities, does not itself alter already-generated procurement demand for components whose required quantity is unaffected.
WHY_IT_MATTERS: >
  An unrelated routing change altering procurement demand would create unpredictable churn in vendor commitments for reasons that have nothing to do with what is actually needed.
DISCONFIRMING_OBSERVATION: >
  Changing a production order's operation sequence with no change to component quantities alters the quantity or existence of already-generated procurement demand for those components.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate procurement demand from a production order, change that order's routing or operation sequence without changing component quantities, and check whether the demand changed.
```

## G07-PURCHASE_MRP-Q041

```yaml
QID: G07-PURCHASE_MRP-Q041
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  The generated procurement order line preserves a reference back to the specific bill-of-materials line or component requirement that produced it, even after that bill of materials is later revised to a new version.
WHY_IT_MATTERS: >
  Losing this reference after a revision would make it impossible to determine, later, which version of the design actually drove a given procurement decision.
DISCONFIRMING_OBSERVATION: >
  Revising the bill of materials to a new version after procurement demand was generated causes the already-generated line's reference back to its originating requirement to no longer resolve.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate procurement demand from a bill of materials, revise that bill of materials to a new version, and check whether the generated line's reference to its origin still resolves.
```

## G07-PURCHASE_MRP-Q042

```yaml
QID: G07-PURCHASE_MRP-Q042
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where a component required by production is under an active blanket agreement or requisition, newly triggered demand correctly routes through that existing mechanism rather than bypassing it to create an unrelated ad hoc order.
WHY_IT_MATTERS: >
  Bypassing an active agreement would create procurement outside terms the business already committed to, potentially at a worse price or outside an already-negotiated arrangement.
DISCONFIRMING_OBSERVATION: >
  A component under an active blanket agreement generates new demand as a wholly separate ad hoc order that does not reference or draw against the existing agreement.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place a component under an active blanket agreement, trigger new production demand for it, and check whether the generated demand routes through the agreement or bypasses it.
```

## G07-PURCHASE_MRP-Q043

```yaml
QID: G07-PURCHASE_MRP-Q043
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A negative or zero net requirement, because on-hand stock or existing incoming supply already exceeds what production needs, does not generate a procurement demand line at all, rather than generating a zero- or negative-quantity order line.
WHY_IT_MATTERS: >
  A zero- or negative-quantity line would clutter procurement review with meaningless entries and risks being misread as a real, actionable requirement.
DISCONFIRMING_OBSERVATION: >
  A production order whose component need is already fully covered by existing stock or incoming supply generates a procurement line with a zero or negative quantity rather than no line at all.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Ensure a component's on-hand stock or incoming supply already exceeds a production order's need, trigger demand computation, and check whether any line is generated.
```

## G07-PURCHASE_MRP-Q044

```yaml
QID: G07-PURCHASE_MRP-Q044
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a production order's component consumption is tracked against a specific reserved lot or serial already earmarked for it, procurement triggered for a shortage of that same component does not accidentally consume or reserve that already-earmarked lot for a different purpose.
WHY_IT_MATTERS: >
  Accidentally reassigning an already-earmarked lot would create a false appearance of resolving a shortage while actually diverting stock away from the order it was reserved for.
DISCONFIRMING_OBSERVATION: >
  New procurement or reservation activity triggered by a separate shortage consumes or reassigns a lot already earmarked for a specific production order's own consumption.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Earmark a specific lot for one production order's consumption, trigger a shortage-driven procurement or reservation elsewhere for the same component, and check whether the earmarked lot is affected.
```

## G07-PURCHASE_MRP-Q045

```yaml
QID: G07-PURCHASE_MRP-Q045
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A production order created and then immediately deleted before any demand recomputation runs leaves no residual generated procurement demand behind, not even a subsequently orphaned one.
WHY_IT_MATTERS: >
  A residual demand from an order that never actually persisted would generate procurement for a need that, from the business's perspective, never really existed.
DISCONFIRMING_OBSERVATION: >
  Creating and immediately deleting a production order before any recomputation still results in a procurement demand appearing afterward.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Create a production order and delete it immediately, before triggering any recomputation, then check whether any procurement demand appears afterward.
```

## G07-PURCHASE_MRP-Q046

```yaml
QID: G07-PURCHASE_MRP-Q046
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Where the lead time information used to compute a generated order's dates is drawn from a source outside the specific production order, a later change to that outside source does not silently rewrite an already-committed generated order's dates without an explicit recomputation action.
WHY_IT_MATTERS: >
  A silent date rewrite driven by an unrelated configuration change would make an already-committed vendor-facing date change with no visible cause or approval.
DISCONFIRMING_OBSERVATION: >
  Changing outside lead-time information after a procurement order was already committed changes that committed order's dates with no recomputation action recorded.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Commit a generated procurement order whose dates depend on outside lead-time information, change that outside information, and check whether the committed order's dates changed with no recorded action.
```

## G07-PURCHASE_MRP-Q047

```yaml
QID: G07-PURCHASE_MRP-Q047
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Demand aggregated from several production orders into one procurement line, when partially received, does not attribute the entire received quantity to only the first-listed contributing production order in traceability records.
WHY_IT_MATTERS: >
  Misattributing a partial receipt entirely to one contributor would make it look like one production order's need was resolved while the others remain silently uncovered without any indication.
DISCONFIRMING_OBSERVATION: >
  A partial fulfilment of a procurement line aggregated from several production orders attributes the entire received quantity to only the first order listed, regardless of each order's actual share.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Aggregate demand from several production orders into one procurement line, partially fulfil it, and check how the partial quantity is attributed across the contributing orders.
```

## G07-PURCHASE_MRP-Q048

```yaml
QID: G07-PURCHASE_MRP-Q048
MODULE: purchase_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Duplicating a production order to plan a similar future run does not cause the copy to inherit a live link to the procurement demand already generated for the original order.
WHY_IT_MATTERS: >
  An inherited live link would make the new, unrelated planned run appear as though its procurement is already handled by demand that actually belongs to the original order.
DISCONFIRMING_OBSERVATION: >
  A duplicated production order shows its component demand as already covered by a procurement order that was actually generated for the original order it was copied from.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate procurement demand for a production order, duplicate that production order, and check whether the copy shows the same demand as already covered.
```

