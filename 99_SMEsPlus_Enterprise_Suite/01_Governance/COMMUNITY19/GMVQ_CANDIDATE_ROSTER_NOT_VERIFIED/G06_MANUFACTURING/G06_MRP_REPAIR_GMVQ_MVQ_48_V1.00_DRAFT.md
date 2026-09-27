# SMEsPlus ENTERPRISE SUITE
## GMVQ — G06 MANUFACTURING / mrp_repair Module Adversarial MVQ Bank

**Document ID:** GMVQ-G06-MRP_REPAIR-MVQ48-V1.00
**Group:** G06 MANUFACTURING
**Module Metadata:** `mrp_repair`
**Wave:** W2
**Author Cell:** P10
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) questions for `mrp_repair`, a BRIDGE module per
GMVQ_BRIDGE_MODULE_RULE_V1.00: it exists only to make repair work and production structures
(a bill of materials and operations, rather than a simple parts list) behave correctly together,
and owns almost no behaviour of its own.

Every question below was tested against the bridge rule: "if this capability were removed and
repair and production structures were used entirely apart, would the question still make sense?"
A question that survives that test is not in this bank. Every question here fails only at the
seam — the point where a repair's own facts (what was consumed, what it cost, what identity the
item carries) and a manufacturing structure's facts can legitimately disagree.

Coverage spans the seam categories from the bridge rule: ordering, partiality, ownership, timing,
reversal, quantity and money, lifecycle mismatch, error asymmetry, and authority, applied across
the concrete grounds in the group brief — structured consumption tracking, identity and serial
history across the operation, abandoned partial repair, capitalised/expensed/billed cost,
warranty and commitment survival, nested serial traceability, in-house-versus-purchased origin,
and reversal of a completed repair.

The question text is source-neutral. It does not name any vendor or product, any technical
identifier (model, table, field, method, XML ID, API path), or the module's own metadata name —
`mrp_repair` appears only in the `MODULE:` field of each question block, never in question text.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` — a concrete result that
  would prove the paired `HYPOTHESIS` wrong, not a restatement of it.
- No padding: each of the 48 questions tests a materially distinct hypothesis; no two share a
  disconfirming observation or reduce to a variation of another question in this bank.
- `LAYER: BASE` marks questions about the seam's own configuration (whether structured repair is
  enabled, who may authorise it, what a repair without a structure defaults to). `LAYER: PROCESS`
  marks questions about behaviour during a live repair, reversal, or downstream event. Both
  layers exist for this seam and are tagged throughout.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/observation
  from the relevant lane.
- `MODULE + QID` is a Research Evidence Join Key only. No coverage or compliance status is
  derived from the existence of a question.
- This document is PREPARED ONLY / NOT FROZEN. It carries no Boss approval and authorizes no
  merge, release, or gate closure.

## G06-MRP_REPAIR-Q001

```yaml
QID: G06-MRP_REPAIR-Q001
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Components drawn during a repair against a structure originally defined for manufacture are
  tracked through the same consumption mechanism as an ordinary production consumption, not a
  separate, less rigorous path.
WHY_IT_MATTERS: >
  A separate, weaker consumption path for repair would let repair-driven stock movements escape
  the same valuation and traceability rigor that a manufacturing consumption receives.
DISCONFIRMING_OBSERVATION: >
  A component consumed during a structured repair leaves a different, less detailed consumption
  record than the same component consumed during ordinary production from the same structure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Consume a component through a structured repair and consume an equivalent component through
  ordinary production of the same structure; compare the resulting consumption records.
```

## G06-MRP_REPAIR-Q002

```yaml
QID: G06-MRP_REPAIR-Q002
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The item's own identity (its serial or lot) persists unchanged across a repair operation —
  repair does not implicitly create a new identity for what is physically the same unit.
WHY_IT_MATTERS: >
  A silently new identity severs the unit's prior history (warranty, prior repairs, original
  production record) from the physical item that customers and technicians still treat as one
  continuous thing.
DISCONFIRMING_OBSERVATION: >
  An item repaired through a structured repair operation is left referenced under a different
  serial or lot identity than the one it held immediately before the repair began.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a serialized item's identity before a structured repair, perform the repair, and check
  whether the same identity is still associated with the item afterward.
```

## G06-MRP_REPAIR-Q003

```yaml
QID: G06-MRP_REPAIR-Q003
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A repair abandoned partway through, after some structured components have already been
  consumed, leaves those components in a defined, documented state (returned, written off, or
  explicitly retained against the item) rather than an undocumented limbo with no record of what
  happened to them.
WHY_IT_MATTERS: >
  Components left in an undocumented state after an abandoned repair are neither available for
  reuse nor accounted for as a loss, and the item's own cost picture becomes unreliable.
DISCONFIRMING_OBSERVATION: >
  Abandoning a repair after partial component consumption leaves those components neither
  returned to stock, written off, nor recorded against the item, with no trace of their
  disposition.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Begin a structured repair, consume some but not all listed components, then abandon the repair
  without completing it; check the disposition of the consumed components.
```

## G06-MRP_REPAIR-Q004

```yaml
QID: G06-MRP_REPAIR-Q004
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a completed repair's cost is capitalised onto the item, expensed as a period cost, or
  charged to a customer is governed by one defined, discoverable rule per repair, and is not left
  to whichever posting path happens to run first.
WHY_IT_MATTERS: >
  An undefined cost treatment means the same repair could be silently absorbed as overhead in one
  case and capitalised onto an asset's value in another, producing incomparable financial results.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical completed repairs, with no stated difference in billing or asset
  treatment, post their cost differently — one capitalised, one expensed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete two comparable repairs under the same configuration and compare how each one's total
  cost is actually posted.
```

## G06-MRP_REPAIR-Q005

```yaml
QID: G06-MRP_REPAIR-Q005
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Whether an item's existing warranty survives, is reset, or is voided by a repair is an explicit,
  recorded determination made as part of the repair, rather than an incidental side effect that
  depends on which repair path was used.
WHY_IT_MATTERS: >
  An incidental, unrecorded warranty outcome means neither the customer nor the business can
  later establish what warranty state actually applies after the repair.
DISCONFIRMING_OBSERVATION: >
  Completing a repair changes an item's warranty state with no explicit record of that
  determination having been made, discoverable only by comparing before-and-after warranty
  status.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Note an item's warranty state before a structured repair, complete the repair, and check for an
  explicit recorded determination of the warranty outcome.
```

## G06-MRP_REPAIR-Q006

```yaml
QID: G06-MRP_REPAIR-Q006
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a repair consumes a component that is itself serial- or lot-tracked, the resulting nested
  trace — the item, the specific component unit consumed, and that component's own prior history
  — remains reconstructable after the repair, not collapsed into a generic "a component of this
  type was used" record.
WHY_IT_MATTERS: >
  Losing the nested trace defeats a recall: if the consumed component itself later proves
  defective, there is no way to identify which repaired items received that specific unit.
DISCONFIRMING_OBSERVATION: >
  Tracing a repaired item's history after the fact returns only the type of component consumed,
  not which specific serial or lot unit of that component was actually used.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Repair an item using a serial- or lot-tracked component, then attempt to trace the repaired
  item's history down to the specific component unit consumed.
```

## G06-MRP_REPAIR-Q007

```yaml
QID: G06-MRP_REPAIR-Q007
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Repairing an item that was originally produced in-house (with its own manufacturing ancestry)
  and repairing an equivalent item that was purchased with no such ancestry are both able to draw
  against the same structured repair mechanism, without the purchased item's lack of ancestry
  silently blocking or degrading the repair.
WHY_IT_MATTERS: >
  If a purchased item cannot use structured repair the same way an in-house item can, repair
  quality and traceability become dependent on an item's origin rather than its actual current
  condition and needs.
DISCONFIRMING_OBSERVATION: >
  A purchased item with no manufacturing ancestry is refused a structured repair, or receives a
  visibly degraded (less tracked) repair, that an equivalent in-house-produced item does not.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt a structured repair on an item produced in-house and on an equivalent item that was
  purchased, and compare whether both can complete the repair with the same rigor.
```

## G06-MRP_REPAIR-Q008

```yaml
QID: G06-MRP_REPAIR-Q008
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Reversing a completed repair returns consumed components to stock, reverses any cost already
  posted, and restores the item's prior state (identity, warranty, commitment) consistently as
  one coordinated undo, rather than reversing some of these effects while leaving others in
  place.
WHY_IT_MATTERS: >
  A partial reversal leaves the item's records internally contradictory — for example, components
  physically back in stock while the item's cost history still shows them consumed.
DISCONFIRMING_OBSERVATION: >
  Reversing a completed repair restores some effects (for example, component stock) but leaves
  another effect (for example, posted cost or warranty state) unchanged from its post-repair
  value.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Complete a repair with recorded cost, component consumption, and a warranty-state change, then
  reverse it and check whether every one of those effects is consistently undone.
```

## G06-MRP_REPAIR-Q009

```yaml
QID: G06-MRP_REPAIR-Q009
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A repair validates its component and operation list against the version of the structure that
  was current when the repair itself was started, not silently against whatever version the
  structure happens to be at the moment the repair is later completed.
WHY_IT_MATTERS: >
  Validating against a structure version that changed mid-repair means what the repair asked for
  at the start may no longer match what it is checked against at the end, for no reason connected
  to the actual repair work.
DISCONFIRMING_OBSERVATION: >
  A structure is edited after a repair using it has started, and the in-progress repair's
  component or operation list silently changes to match the edited structure rather than the
  version in force when it began.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Start a repair against a structure, edit the structure's component list while the repair is
  still in progress, and check which version the in-progress repair actually reflects.
```

## G06-MRP_REPAIR-Q010

```yaml
QID: G06-MRP_REPAIR-Q010
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A repair that consumes only some of a structure's listed components (skipping optional ones) is
  recorded distinctly from a repair that consumes the full structure, so the difference is visible
  after the fact rather than both looking like a full-structure repair.
WHY_IT_MATTERS: >
  Without that distinction, a partial repair's actual scope is lost, and later review cannot tell
  a full structural repair from one that only used part of it.
DISCONFIRMING_OBSERVATION: >
  A repair that consumes only some of a structure's listed components produces a completed-repair
  record indistinguishable from one that consumed the full structure.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete one repair consuming only some of a structure's optional components and one consuming
  the full structure, and compare the two completed records.
```

## G06-MRP_REPAIR-Q011

```yaml
QID: G06-MRP_REPAIR-Q011
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When an item's own serial history and the structure's defined component list disagree about
  what should currently be inside the item (for example, a component the structure lists as
  standard was never actually installed on this unit), the item's own recorded history is treated
  as authoritative for that specific unit's repair, not the structure's generic definition.
WHY_IT_MATTERS: >
  Treating the generic structure as authoritative over the unit's own actual history can lead a
  repair to assume the presence of a component that was never really there, or to overwrite a
  legitimate prior customization.
DISCONFIRMING_OBSERVATION: >
  A repair proceeds as though a component were present on a unit, based solely on the structure's
  definition, when that unit's own history shows it was never actually installed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Repair a unit whose actual component history diverges from its structure's generic definition,
  and check which source the repair treats as authoritative for that divergence.
```

## G06-MRP_REPAIR-Q012

```yaml
QID: G06-MRP_REPAIR-Q012
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing a repair whose consumed component was itself serial- or lot-tracked correctly
  unwinds the nested trace back to the exact unit that was consumed, rather than returning a
  generic quantity of that component type to stock with the specific unit's identity lost.
WHY_IT_MATTERS: >
  Losing the specific unit's identity on reversal means the returned stock can no longer be
  distinguished from any other unit of that component, undoing the traceability the original
  consumption preserved.
DISCONFIRMING_OBSERVATION: >
  Reversing a repair that consumed a specific serial- or lot-tracked component unit returns a
  generic quantity of that component type to stock, with the original specific unit's identity no
  longer recoverable.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Repair an item using a serial- or lot-tracked component, then reverse the repair and check
  whether the returned stock still carries the original specific unit's identity.
```

## G06-MRP_REPAIR-Q013

```yaml
QID: G06-MRP_REPAIR-Q013
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A repair consuming a different quantity of a structured component than the structure specifies
  (more or less than called for) records that variance explicitly, and the variance affects the
  repair's cost outcome in a way consistent with how a comparable variance would be treated in
  ordinary production.
WHY_IT_MATTERS: >
  An unrecorded or inconsistently treated quantity variance during repair hides genuine excess
  consumption or shortage, and produces a repair cost that cannot be reconciled against the
  structure it claims to follow.
DISCONFIRMING_OBSERVATION: >
  A repair consuming a different quantity of a component than the structure specifies leaves no
  variance record, or the variance affects cost differently than an equivalent variance would in
  ordinary production of the same structure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Perform a repair consuming a different quantity of a structured component than specified, and
  compare the recorded variance and cost effect to an equivalent production-quantity variance.
```

## G06-MRP_REPAIR-Q014

```yaml
QID: G06-MRP_REPAIR-Q014
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A structure that is later archived or deprecated for manufacturing purposes remains referenceable
  for the traceability of repairs already completed against it, and a new repair can still be
  correctly evaluated against whatever the current status of that structure actually permits,
  rather than either silently vanishing from history or silently permitting new repairs against a
  structure no longer meant for active use.
WHY_IT_MATTERS: >
  Losing the reference breaks historical traceability, while silently allowing new repairs against
  a deprecated structure defeats the purpose of deprecating it in the first place.
DISCONFIRMING_OBSERVATION: >
  After a structure is archived, a previously completed repair's traceability no longer resolves
  back to it, or a brand-new repair is freely initiated against the archived structure with no
  distinction from an active one.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Archive a structure that was used in a completed repair, then check both that repair's
  traceability and whether a new repair can still be started against the archived structure.
```

## G06-MRP_REPAIR-Q015

```yaml
QID: G06-MRP_REPAIR-Q015
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If the step that posts a repair's cost fails after component consumption has already been
  recorded, the consumption is rolled back or clearly flagged as unposted, rather than left as an
  orphaned consumption with no corresponding cost record and no flag.
WHY_IT_MATTERS: >
  An orphaned consumption with no cost and no flag is invisible to both inventory reconciliation
  and financial review — stock is gone, but nothing shows why or at what cost.
DISCONFIRMING_OBSERVATION: >
  Forcing the cost-posting step of a repair to fail after component consumption leaves the
  consumption recorded with no cost entry and no visible flag indicating the failure.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Consume components on a repair, then interrupt or fail the cost-posting step before it
  completes, and check the resulting state of the consumption record.
```

## G06-MRP_REPAIR-Q016

```yaml
QID: G06-MRP_REPAIR-Q016
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Executing a repair that draws against a manufacturing structure requires a permission distinct
  from the permission needed to execute ordinary production against that same structure.
WHY_IT_MATTERS: >
  If the same permission covers both, an actor authorised only for routine production work can
  also perform repairs with customer-facing cost and warranty consequences they were never meant
  to control.
DISCONFIRMING_OBSERVATION: >
  A user holding only ordinary production-execution rights is able to initiate and complete a
  structured repair with no additional permission check.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with production-execution rights only, attempt to initiate a structured repair and
  observe whether it is permitted.
```

## G06-MRP_REPAIR-Q017

```yaml
QID: G06-MRP_REPAIR-Q017
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A repair that is billed to a customer and one that is treated as a warranty or internal repair
  are distinguished in the record in a way that prevents a billable repair's component consumption
  from also being silently counted toward internal manufacturing cost metrics as if it were
  ordinary production.
WHY_IT_MATTERS: >
  Double-counting a billed repair's consumption into internal production cost metrics distorts
  those metrics with cost that was already recovered from a customer.
DISCONFIRMING_OBSERVATION: >
  A repair marked as customer-billable has its component consumption appear in an internal
  manufacturing cost metric alongside ordinary, non-billable production consumption with no
  distinguishing marker.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a customer-billed repair and check whether its consumption appears, undistinguished,
  in a metric intended to reflect internal production cost only.
```

## G06-MRP_REPAIR-Q018

```yaml
QID: G06-MRP_REPAIR-Q018
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An item repaired more than once over its life accumulates a composed, chained traceability
  record across all of its repairs, rather than each new repair overwriting or replacing the
  record left by the one before it.
WHY_IT_MATTERS: >
  An overwritten history makes it impossible to see a pattern of recurring failure on the same
  item, which is exactly the signal a warranty or quality review needs to catch.
DISCONFIRMING_OBSERVATION: >
  After a second repair on the same item, the record of the first repair is no longer visible or
  is replaced rather than retained alongside the second.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Repair the same serialized item twice, with time between the two events, and check whether both
  repair records remain visible together afterward.
```

## G06-MRP_REPAIR-Q019

```yaml
QID: G06-MRP_REPAIR-Q019
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An item that enters repair while carrying an open commitment (reserved for delivery, or under
  an active contract) has that commitment explicitly preserved, explicitly paused, or explicitly
  cancelled as a recorded decision — not silently dropped with no trace that it ever existed.
WHY_IT_MATTERS: >
  A silently dropped commitment can surface later as a broken promise to whoever the item was
  committed to, with no record of when or why the commitment disappeared.
DISCONFIRMING_OBSERVATION: >
  An item with an open delivery or contract commitment enters repair, and after the repair that
  commitment is gone with no record of it having been preserved, paused, or cancelled.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Place an open commitment on an item, send that item into repair, and check the commitment's
  state and any accompanying record both during and after the repair.
```

## G06-MRP_REPAIR-Q020

```yaml
QID: G06-MRP_REPAIR-Q020
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where the item being repaired is itself a sub-assembly with its own structure, and a component
  of it also needs repair, the seam either explicitly supports repairing that nested component in
  turn, or explicitly and predictably refuses to, rather than behaving inconsistently depending on
  how deep the nesting happens to be.
WHY_IT_MATTERS: >
  Inconsistent nested-repair support means the same class of multi-level assembly can sometimes be
  properly repaired down to the faulty component and sometimes cannot, for no principled reason.
DISCONFIRMING_OBSERVATION: >
  Attempting to repair a component nested within the item under repair succeeds in one case and is
  refused in an otherwise comparable case, with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt a repair that requires repairing a component nested within the item under repair, on two
  comparable multi-level assemblies, and compare the outcome.
```

## G06-MRP_REPAIR-Q021

```yaml
QID: G06-MRP_REPAIR-Q021
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Scrap or byproduct generated by removing components during a repair is valued and recorded
  through the same path as scrap or byproduct generated during ordinary production, not a
  separate, less rigorous repair-specific path.
WHY_IT_MATTERS: >
  A weaker repair-specific scrap path can leave removed material unaccounted for in valuation,
  understating true repair cost or overstating available stock.
DISCONFIRMING_OBSERVATION: >
  Scrap generated by a repair operation is recorded with less valuation detail than equivalent
  scrap generated by an ordinary production operation using the same structure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Generate scrap during a structured repair and during ordinary production of the same structure,
  and compare how each scrap event is valued and recorded.
```

## G06-MRP_REPAIR-Q022

```yaml
QID: G06-MRP_REPAIR-Q022
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  An item with no repair-eligible structure defined at all is either explicitly refused a
  structured repair, or explicitly and visibly falls back to an unstructured (simple parts list)
  repair — the outcome is not a silent, undocumented fallback indistinguishable from a genuinely
  structured repair.
WHY_IT_MATTERS: >
  A silent fallback can make an unstructured repair look, in the record, as though it followed a
  defined structure when it never actually did.
DISCONFIRMING_OBSERVATION: >
  Repairing an item with no defined repair-eligible structure produces a completed repair record
  that presents as structured, with no indication that no structure actually governed it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt a structured repair on an item with no repair-eligible structure defined, and inspect
  the resulting record for a clear indication of the fallback.
```

## G06-MRP_REPAIR-Q023

```yaml
QID: G06-MRP_REPAIR-Q023
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A structured repair requires the item to be in a defined state (for example, returned or logged
  as under a service claim) before it can begin, rather than being startable against an item in
  any arbitrary state such as one still shown as actively in a customer's possession with no
  return recorded.
WHY_IT_MATTERS: >
  Allowing repair to start on an item with no recorded return or claim disconnects the repair
  record from the physical event that is supposed to have triggered it.
DISCONFIRMING_OBSERVATION: >
  A structured repair is successfully started against an item with no recorded return, service
  claim, or equivalent triggering state.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to start a structured repair on an item with no prior return or service-claim record,
  and observe whether the system permits it.
```

## G06-MRP_REPAIR-Q024

```yaml
QID: G06-MRP_REPAIR-Q024
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two structured repair operations cannot both be active against the same serialized item at the
  same time — a second attempt is blocked or clearly queued rather than silently allowed to
  proceed in parallel with the first.
WHY_IT_MATTERS: >
  Two parallel repairs on one physical unit can each consume components and post cost against an
  item that can only physically be repaired once at a time, corrupting both records.
DISCONFIRMING_OBSERVATION: >
  A second structured repair is started and allowed to proceed against a serialized item that
  already has an active, incomplete repair in progress.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Start a structured repair on a serialized item, and while it remains open, attempt to start a
  second structured repair on the same item.
```

## G06-MRP_REPAIR-Q025

```yaml
QID: G06-MRP_REPAIR-Q025
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A repair recorded as complete with zero components consumed (for example, an inspection-only
  visit) is accepted as a distinct, valid category of repair outcome, rather than being either
  silently rejected or recorded indistinguishably from a repair that did consume components.
WHY_IT_MATTERS: >
  If a no-component repair cannot be recorded as such, either genuine inspection visits go
  unlogged, or they get recorded in a way indistinguishable from a repair that actually replaced
  parts.
DISCONFIRMING_OBSERVATION: >
  Completing a repair with zero components consumed is either rejected outright, or is recorded in
  a way indistinguishable from a repair that did consume components.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a structured repair with zero components consumed and inspect how the outcome is
  recorded compared to a component-consuming repair.
```

## G06-MRP_REPAIR-Q026

```yaml
QID: G06-MRP_REPAIR-Q026
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Completing a structured repair updates only the item's own repair and service history, and does
  not silently alter the item's own manufacturing bill-of-materials or structure lineage record as
  though the repair were itself a new production event.
WHY_IT_MATTERS: >
  If repair silently rewrites manufacturing lineage, the record of how the item was originally
  built becomes indistinguishable from how it was later repaired, corrupting both histories.
DISCONFIRMING_OBSERVATION: >
  Completing a repair changes the item's recorded original manufacturing structure or lineage,
  rather than being recorded solely as a separate repair event.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record an item's manufacturing lineage before a repair, complete the repair, and check whether
  that lineage record is altered afterward.
```

## G06-MRP_REPAIR-Q027

```yaml
QID: G06-MRP_REPAIR-Q027
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a repair draws components from a defined manufacturing structure at all is a
  configuration set per item or item category, with a defined, documented default for items where
  it has never been explicitly configured.
WHY_IT_MATTERS: >
  An undocumented default means it is unpredictable, for a newly introduced item, whether repair
  will follow the structured or unstructured path until someone happens to test it.
DISCONFIRMING_OBSERVATION: >
  A newly created item category, with the structured-repair setting never explicitly configured,
  produces an unpredictable choice between structured and unstructured repair across repeated
  trials.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Create a new item category with the structured-repair configuration untouched, and initiate
  repair on items of that category across more than one trial.
```

## G06-MRP_REPAIR-Q028

```yaml
QID: G06-MRP_REPAIR-Q028
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A structure that defines both components and operations (labor steps) has its operations
  portion actually reachable and recordable during a repair, rather than the repair mechanism
  silently ignoring the operations and drawing only the component list.
WHY_IT_MATTERS: >
  If operations are silently ignored, labor time and the specific steps performed during a repair
  are never captured, even though the structure defines them as part of the work.
DISCONFIRMING_OBSERVATION: >
  Repairing against a structure that defines operations produces a completed repair record with no
  trace of those operations having been recorded or performed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Repair an item against a structure that defines both components and operations, and check
  whether the operations portion is reachable and recorded during the repair.
```

## G06-MRP_REPAIR-Q029

```yaml
QID: G06-MRP_REPAIR-Q029
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The specific version of the structure actually used for a given repair is permanently recorded
  against that repair event, rather than only inferable from the structure's current state after
  the fact.
WHY_IT_MATTERS: >
  Without a permanent version reference, a later audit cannot know what components and operations
  a historical repair was actually validated against once the structure itself has since changed.
DISCONFIRMING_OBSERVATION: >
  For a completed repair, no stored record indicates which version of the structure it was
  validated against — the answer is only obtainable by inspecting the structure's current,
  possibly since-changed, definition.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Complete a repair against a structure, then change the structure afterward, and check whether the
  repair's own record still correctly states which version it actually used.
```

## G06-MRP_REPAIR-Q030

```yaml
QID: G06-MRP_REPAIR-Q030
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Components abandoned mid-repair (per the partial-repair case) that are themselves lot- or
  serial-tracked retain their own individual identity when returned to stock, rather than being
  merged back anonymously into an undifferentiated quantity.
WHY_IT_MATTERS: >
  Merging tracked components back anonymously destroys the ability to later isolate that specific
  unit if it is implicated in a quality issue.
DISCONFIRMING_OBSERVATION: >
  A lot- or serial-tracked component consumed and then returned after an abandoned repair loses
  its individual identity and appears in stock as an undifferentiated quantity.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consume a lot- or serial-tracked component into a repair, abandon the repair before completion,
  and check whether the returned component retains its original individual identity.
```

## G06-MRP_REPAIR-Q031

```yaml
QID: G06-MRP_REPAIR-Q031
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Repair cost capitalised onto an item that is never intended for resale (an item held and used
  internally) follows a capitalisation path that correctly reflects that item's own nature, rather
  than the same path used for an item held for sale, which could misstate the value of stock meant
  for a customer.
WHY_IT_MATTERS: >
  Capitalising an internal item's repair cost through a sale-inventory path can inflate the
  reported value of goods actually intended for customers.
DISCONFIRMING_OBSERVATION: >
  Repair cost capitalised onto an internally held item posts through the same valuation path as
  repair cost capitalised onto an item held for sale, with no distinction between the two.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Capitalise repair cost onto an internally used item and onto an item held for sale, and compare
  the valuation path each one actually uses.
```

## G06-MRP_REPAIR-Q032

```yaml
QID: G06-MRP_REPAIR-Q032
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A repair on an item owned or logged under one company or branch is blocked, at the point the
  repair is started, from drawing components against a structure defined under a different company
  or branch, rather than the mismatch being discoverable only after components have already been
  consumed.
WHY_IT_MATTERS: >
  Discovering a cross-company mismatch only after consumption has already occurred means the
  incorrect consumption has already affected the wrong company's stock and valuation.
DISCONFIRMING_OBSERVATION: >
  A repair is allowed to begin and consume components against a structure defined under a
  different company than the item's own, with the mismatch only noticed afterward, if at all.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Attempt to start a repair on an item under one company, referencing a structure defined under a
  different company, and check when (if at all) the mismatch is caught.
```

## G06-MRP_REPAIR-Q033

```yaml
QID: G06-MRP_REPAIR-Q033
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a repair uses some components from the defined structure and some ad hoc components not on
  the structure at all, the ad hoc portion is tracked with the same cost and lot rigor as the
  structured portion, not with looser or missing detail.
WHY_IT_MATTERS: >
  A weakly tracked ad hoc portion means the true full cost and traceability of a mixed repair is
  understated, even though the ad hoc components are just as physically consumed as the structured
  ones.
DISCONFIRMING_OBSERVATION: >
  A repair combining structured and ad hoc components records full cost and lot detail for the
  structured portion but only partial or missing detail for the ad hoc portion.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Perform a repair using both structure-listed and ad hoc components, and compare the recorded
  detail for each portion.
```

## G06-MRP_REPAIR-Q034

```yaml
QID: G06-MRP_REPAIR-Q034
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing a repair after the repaired item has already been consumed into a further downstream
  operation (for example, shipped or used as a component elsewhere) either explicitly refuses the
  reversal or explicitly accounts for the downstream consumption as part of undoing it, rather than
  silently reversing the repair in isolation as though the item were still sitting untouched.
WHY_IT_MATTERS: >
  An isolated reversal that ignores downstream consumption can return components to stock or
  reverse cost on an item that, physically, is no longer available to actually be un-repaired.
DISCONFIRMING_OBSERVATION: >
  Reversing a repair on an item already consumed downstream completes as though the item were
  still untouched, with no acknowledgment of the downstream consumption in the reversal record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Complete a repair, consume the repaired item into a further downstream operation, then attempt
  to reverse the original repair and observe the outcome.
```

## G06-MRP_REPAIR-Q035

```yaml
QID: G06-MRP_REPAIR-Q035
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a consumed component itself carries its own separate warranty, repairing with a new such
  component correctly establishes or transfers that component's own nested warranty independently
  of, and without corrupting, the overall item's own warranty state.
WHY_IT_MATTERS: >
  Conflating a component's own warranty with the item's overall warranty can either lose the
  component's independent coverage or incorrectly extend the item's coverage based on an unrelated
  part.
DISCONFIRMING_OBSERVATION: >
  Installing a component with its own separate warranty during a repair changes the overall item's
  warranty state with no distinct, independent record of the component's own warranty.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Repair an item using a component that carries its own separate warranty, and check whether that
  component's warranty is tracked independently from the item's overall warranty state.
```

## G06-MRP_REPAIR-Q036

```yaml
QID: G06-MRP_REPAIR-Q036
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Referencing, for a purchased (non-manufactured) item, a structure that was actually authored for
  manufacturing a different, merely equivalent item is either explicitly permitted with a clear
  cross-reference recorded, or explicitly blocked — not silently allowed to proceed as though the
  structure and the item were the same thing.
WHY_IT_MATTERS: >
  A silent cross-reference between a purchased item and an unrelated manufacturing structure can
  apply component and cost assumptions to the purchased item that were never actually validated
  for it.
DISCONFIRMING_OBSERVATION: >
  A purchased item's repair proceeds against a structure authored for a different manufactured
  item, with no recorded cross-reference and no distinction from repairing the item the structure
  was actually meant for.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt a structured repair on a purchased item using a structure authored for manufacturing a
  different, merely similar item, and observe whether it is permitted and how it is recorded.
```

## G06-MRP_REPAIR-Q037

```yaml
QID: G06-MRP_REPAIR-Q037
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If an item's own serial identifier changes (for example, relabeled) while a repair on it is still
  in progress, the in-progress repair record follows the item to its new identifier rather than
  becoming orphaned under the old, now-abandoned one.
WHY_IT_MATTERS: >
  An orphaned repair record under a superseded identifier disappears from the item's visible
  history from the point of relabeling onward, as though the repair had never happened.
DISCONFIRMING_OBSERVATION: >
  Relabeling an item's serial identifier while a repair is in progress leaves the repair record
  attached to the old identifier, no longer visibly linked to the item under its new one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Start a repair on a serialized item, relabel the item's serial identifier while the repair is
  still in progress, and check whether the repair record follows the item.
```

## G06-MRP_REPAIR-Q038

```yaml
QID: G06-MRP_REPAIR-Q038
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a given repair is billed to a customer is a decision made per repair, and that decision
  does not change which components-consumption path (structured versus ad hoc) is available for
  that repair.
WHY_IT_MATTERS: >
  If billable status silently gates access to the structured consumption path, a warranty repair
  and a billable repair on the same item type could end up tracked with different rigor for no
  reason connected to the actual repair work.
DISCONFIRMING_OBSERVATION: >
  Marking a repair as customer-billable, versus warranty or internal, changes whether the
  structured component-consumption path is available for an otherwise identical repair.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt a structured repair marked as billable and one marked as warranty on the same item type,
  and compare whether both can use the same consumption path.
```

## G06-MRP_REPAIR-Q039

```yaml
QID: G06-MRP_REPAIR-Q039
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A repair operation consuming components from a different location than the item's own current
  location is permitted only when that cross-location movement is itself explicitly tracked, not
  silently allowed as an unrecorded transfer.
WHY_IT_MATTERS: >
  An unrecorded cross-location consumption leaves the receiving location's stock records and the
  repair's own cost basis disconnected from where the components actually physically came from.
DISCONFIRMING_OBSERVATION: >
  A repair consumes components from a location other than the item's own current location with no
  corresponding movement or transfer record between the two locations.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Perform a repair drawing components from a different location than the item's current location,
  and check whether a transfer or movement record is created between them.
```

## G06-MRP_REPAIR-Q040

```yaml
QID: G06-MRP_REPAIR-Q040
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A repair referencing a structure that includes a component the business no longer stocks or
  sells at all is either explicitly blocked from starting, or explicitly proceeds into a defined
  stock-out state that is visible to whoever is executing the repair, rather than failing in an
  undocumented or unclear way.
WHY_IT_MATTERS: >
  An unclear failure at this point leaves a technician unable to tell whether the repair cannot
  proceed at all or is simply waiting on stock that will never arrive.
DISCONFIRMING_OBSERVATION: >
  Starting a repair against a structure that includes a discontinued, no-longer-stocked component
  produces an unclear or undocumented failure state rather than an explicit block or an explicit,
  visible stock-out.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Reference a structure containing a discontinued component in a new repair, and observe the
  resulting state when that component cannot be sourced.
```

## G06-MRP_REPAIR-Q041

```yaml
QID: G06-MRP_REPAIR-Q041
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Repair cost capitalised onto an item's valuation remains transparently visible when that item is
  later sold — the buyer-facing or downstream valuation reflects the repair cost as a distinct,
  traceable component, rather than the repair cost being absorbed invisibly into a single blended
  figure.
WHY_IT_MATTERS: >
  An invisibly absorbed repair cost makes it impossible to later separate what an item originally
  cost from what was spent repairing it, undermining any review of repair economics after the sale.
DISCONFIRMING_OBSERVATION: >
  An item's repair cost, once capitalised, cannot be distinguished from its original valuation once
  the item is later sold or moved further downstream.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Capitalise a repair's cost onto an item's valuation, later sell or transfer the item, and check
  whether the repair cost remains identifiable as a distinct component of the final valuation.
```

## G06-MRP_REPAIR-Q042

```yaml
QID: G06-MRP_REPAIR-Q042
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A repair whose structure defines operations, but for which no labor is actually recorded against
  any of those operations, is still recognised as a valid, completable repair rather than being
  silently blocked from completion for lacking labor detail.
WHY_IT_MATTERS: >
  If skipping labor recording silently blocks completion, a legitimate quick repair (or one where
  labor is tracked elsewhere) becomes unable to close out even though the actual repair work is
  done.
DISCONFIRMING_OBSERVATION: >
  A repair with components consumed but no labor recorded against its defined operations cannot be
  marked complete, or is blocked from completion, with no override available.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Consume components on a repair without recording any labor against its defined operations, and
  attempt to mark the repair complete.
```

## G06-MRP_REPAIR-Q043

```yaml
QID: G06-MRP_REPAIR-Q043
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A repair already marked complete cannot be reopened and modified through an informal edit — any
  change after completion is required to go through the same reversal path that correctly returns
  components and reverses cost, rather than bypassing that logic entirely.
WHY_IT_MATTERS: >
  An informal reopen-and-edit path that bypasses reversal logic can leave components, cost, and
  identity records inconsistent with whatever the edited repair now claims happened.
DISCONFIRMING_OBSERVATION: >
  A completed repair is reopened and its component or cost details are changed directly, with no
  corresponding reversal of the original consumption or cost posting.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Complete a repair, then attempt to reopen and directly edit its component or cost details rather
  than issuing a formal reversal, and observe whether that is permitted.
```

## G06-MRP_REPAIR-Q044

```yaml
QID: G06-MRP_REPAIR-Q044
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Multiple simultaneous structured repairs, each against a different serialized unit of the same
  item template and referencing the same structure, keep their component consumption records
  correctly isolated per unit rather than one unit's consumption bleeding into another's record.
WHY_IT_MATTERS: >
  Bleed-through between concurrent repairs of the same item template would misattribute cost and
  component usage between physically distinct units.
DISCONFIRMING_OBSERVATION: >
  Running two simultaneous repairs against different serialized units of the same item template
  results in a component consumption appearing against the wrong unit's record.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Start two structured repairs at the same time against different serialized units of the same
  item template, referencing the same structure, and check that each unit's consumption record
  stays isolated.
```

## G06-MRP_REPAIR-Q045

```yaml
QID: G06-MRP_REPAIR-Q045
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When an item fails again shortly after a repair and enters a second repair, the traceability
  chain makes the sequence explicit (this is a repeat repair following the earlier one), rather
  than presenting the second repair as though it were the item's first and only repair event.
WHY_IT_MATTERS: >
  Without an explicit link, a pattern of repeat failure on the same item after repair is invisible
  to whoever is reviewing repair quality or a warranty claim.
DISCONFIRMING_OBSERVATION: >
  A second repair on an item that failed shortly after an earlier repair is recorded with no
  explicit link back to that earlier repair.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Repair an item, have it fail again shortly afterward, repair it a second time, and check whether
  the second repair's record explicitly references the first.
```

## G06-MRP_REPAIR-Q046

```yaml
QID: G06-MRP_REPAIR-Q046
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where separation of duties between approving a repair and executing its component consumption is
  intended, that separation is enforced by the seam itself (a distinct approval step required
  before consumption) rather than left entirely to unenforced policy that a single actor could
  simply ignore.
WHY_IT_MATTERS: >
  Unenforced separation of duties is not actually separation — a single actor can both authorise
  and execute a repair with customer-facing cost or warranty consequences with no independent
  check.
DISCONFIRMING_OBSERVATION: >
  The same user is able to both approve a repair and execute its component consumption with no
  distinct approval step or independent check enforced between the two actions.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a single user, attempt to both approve a repair and execute its component consumption, and
  observe whether a distinct, independently enforced approval step is required.
```

## G06-MRP_REPAIR-Q047

```yaml
QID: G06-MRP_REPAIR-Q047
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing a repair issued after other business events (such as a period close or an inventory
  valuation run) have already incorporated that repair's cost correctly restates those downstream
  figures, rather than leaving them permanently inconsistent with the now-reversed repair.
WHY_IT_MATTERS: >
  A reversal that cannot reach back into already-closed downstream figures leaves the books
  permanently overstating or understating cost relative to what actually happened.
DISCONFIRMING_OBSERVATION: >
  Reversing a repair whose cost was already incorporated into a subsequent period close or
  valuation run leaves that closed figure unchanged and inconsistent with the reversal.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a repair, let its cost be incorporated into a subsequent period close or valuation run,
  then reverse the repair and check whether the closed figure is correctly restated.
```

## G06-MRP_REPAIR-Q048

```yaml
QID: G06-MRP_REPAIR-Q048
MODULE: mrp_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The decision of whether a repair's consumption is tracked through the structured manufacturing
  path or an unstructured one is made once, at the start of the repair, and does not silently
  change partway through the same repair event depending on which component is being consumed at
  that moment.
WHY_IT_MATTERS: >
  A mid-repair switch between tracking paths would produce one completed repair record that is
  partly rigorous and partly not, with no way to tell from the outside which components received
  which treatment.
DISCONFIRMING_OBSERVATION: >
  Within a single repair event, some components are consumed through the structured path and
  others through an unstructured path, with no documented rule explaining the split.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Perform a single repair consuming a mix of components, some clearly on the defined structure and
  some not, and check whether the tracking path used is consistent and documented for both.
```
