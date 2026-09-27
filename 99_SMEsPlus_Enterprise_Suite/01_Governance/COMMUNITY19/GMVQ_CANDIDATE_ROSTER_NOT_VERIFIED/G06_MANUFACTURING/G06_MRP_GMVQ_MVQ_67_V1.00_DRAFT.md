# SMEsPlus ENTERPRISE SUITE
## GMVQ — G06 MANUFACTURING / mrp Module Adversarial MVQ Bank

**Document ID:** GMVQ-G06-MRP-MVQ67-V1.00
**Group:** G06 MANUFACTURING
**Module Metadata:** `mrp`
**Wave:** W2
**Author Cell:** TEAM P08 (GMVQ Question Factory — Production Team P08)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 67

## Purpose

`mrp` is the base module of G06 MANUFACTURING and the group's highest-risk module: the bill of materials as a
versioned structure, routings and work order sequencing, component consumption and substitution, yield and
scrap, by-product valuation, lot and serial traceability, and the boundary between production activity and its
accounting consequence all sit inside it. Eleven other modules in this group extend or bridge against this
module; this bank exists to own the group's core invariants so that the bridge banks do not have to restate
them, per the Bridge Module Rule. The bank targets 60-70 material questions because this module's risk surface,
and its role as the shared foundation for the group, warrants depth beyond the floor; no question here is
padding — every one targets a distinct, falsifiable hypothesis.

Question text is source-neutral: no vendor or product name, no technical identifier (model, table, field,
method, XML ID, API path), and no reference to how any specific implementation is built. Language is generic
manufacturing/business behaviour throughout.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: each question tests a distinct material hypothesis, spread across business capability, business
  rule, state transition, configuration dependency, role/permission, exception path, cancellation, reversal,
  negative case, cross-module (ledger) dependency, auditability, tenant/company boundary, concurrency/ordering,
  and runtime/configuration reachability.
- `LAYER: BASE` marks a foundation/configuration or structural question (the bill, routing, master setup);
  `LAYER: PROCESS` marks a transactional/execution-time question, since this module carries both layers.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a
  Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.
- Per the Bridge Module Rule §6, `mrp` is a base module and this bank carries the group's core invariants for
  bill versioning, consumption, yield/scrap, by-products, work order sequence, traceability, and the production-
  to-ledger boundary. Bridge banks in this group (the `mrp_subcontracting*` family, `mrp_account`,
  `mrp_landed_costs`, `mrp_product_expiry`, `mrp_repair`) must not restate these; they ask what happens to these
  invariants when a second capability is attached.

## G06-MRP-Q001

```yaml
QID: G06-MRP-Q001
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A production order records, at the moment it is created, which version of the product structure it is built
  against, so that a later revision to that structure does not silently change what the order is understood
  to require.
WHY_IT_MATTERS: >
  If an order silently tracks whatever the structure currently says rather than a fixed reference, revising a
  structure for a future change also rewrites the requirement for every order already in progress, which the
  people who opened those orders never agreed to.
DISCONFIRMING_OBSERVATION: >
  Revising the structure for a product changes the component list or quantities shown on an order that was
  already open before the revision was made, with no record of which version the order was originally opened
  under.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Open a production order against a structure, then revise the structure's components or quantities, then
  re-open the existing order and compare its recorded requirement to the revised structure.
```

## G06-MRP-Q002

```yaml
QID: G06-MRP-Q002
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  When a structure is revised, the superseded version remains retrievable rather than being overwritten in
  place so that its prior content can no longer be reconstructed.
WHY_IT_MATTERS: >
  Without a retrievable prior version, no one can later answer what an order that closed under the old
  structure was actually supposed to require, which removes the ability to audit past production against its
  own rules.
DISCONFIRMING_OBSERVATION: >
  After a structure is revised, there is no way to view or reconstruct the component list and quantities that
  were in effect immediately before the revision.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record the full component list and quantities of a structure, revise it, and then attempt to retrieve the
  pre-revision version.
```

## G06-MRP-Q003

```yaml
QID: G06-MRP-Q003
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An order that is still open when its structure is revised either continues to compute its expected
  requirement from the version it started under, or is explicitly and visibly moved onto the new version — it
  does not end up in an undefined mixture of the two.
WHY_IT_MATTERS: >
  A mixed state, where some already-consumed lines reflect the old version and remaining lines silently
  reflect the new one, produces a requirement that never corresponded to any single approved structure.
DISCONFIRMING_OBSERVATION: >
  An open order, after its structure is revised, shows some component lines consistent with the original
  version and other lines consistent with the revised version, with no explicit action having moved it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Partially consume components on an open order under one structure version, revise the structure, then
  inspect the order's remaining expected lines.
```

## G06-MRP-Q004

```yaml
QID: G06-MRP-Q004
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A structure can be scheduled to take effect from a defined future point, and orders started before that
  point are not retroactively subject to it.
WHY_IT_MATTERS: >
  Effective-dated structure changes are how a planned engineering change is rolled out without disturbing
  production already committed under the prior design; collapsing the two into one immediate change removes
  that control.
DISCONFIRMING_OBSERVATION: >
  A structure change scheduled to take effect on a future date is already reflected in requirements for an
  order opened, and still in progress, before that date.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Schedule a structure revision for a future effective date, open and partially process an order before that
  date arrives, and inspect its requirement.
```

## G06-MRP-Q005

```yaml
QID: G06-MRP-Q005
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The system prevents two structures for the same output from being simultaneously active in a way that
  leaves it ambiguous which one a new order should follow.
WHY_IT_MATTERS: >
  An ambiguous active structure means the requirement a new order receives depends on an undocumented
  tie-break rather than a deliberate choice, which is not reproducible or explainable after the fact.
DISCONFIRMING_OBSERVATION: >
  Two structures for the same output are both active at once, and opening a new order for that output does
  not make explicit, at the time of creation, which one was selected or why.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to activate a second structure for an output that already has an active structure, and open a new
  order for that output.
```

## G06-MRP-Q006

```yaml
QID: G06-MRP-Q006
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Which structure version an order was actually opened under remains visible on that order after the order is
  completed and closed, not only while it is in progress.
WHY_IT_MATTERS: >
  A later dispute about why an order consumed the quantities it did can only be resolved if the version it
  followed is still recorded once the order is finished, not just during its active life.
DISCONFIRMING_OBSERVATION: >
  A completed and closed order no longer shows, or shows incorrectly, which structure version it was opened
  against.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete and close an order, then inspect its record for the structure version reference some time
  afterward.
```

## G06-MRP-Q007

```yaml
QID: G06-MRP-Q007
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Removing or deactivating a component line from a structure does not remove the historical record of that
  component's use on orders that already referenced the structure before the change.
WHY_IT_MATTERS: >
  If deactivating a line erases its trace from past orders, the historical requirement and consumption record
  for those orders becomes incomplete after the fact, which corrupts retrospective audit.
DISCONFIRMING_OBSERVATION: >
  After a component line is removed or deactivated on a structure, an already-completed order that consumed
  that component no longer shows it in its own historical requirement or consumption record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete an order that consumes a specific component, then remove or deactivate that component's line on
  the structure, then re-inspect the completed order's own record.
```

## G06-MRP-Q008

```yaml
QID: G06-MRP-Q008
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A structure's own quantity ratios, how much of each component per unit of output, are stored independently
  of any single order, so that a change made through one order's exceptional handling cannot alter what the
  structure itself specifies for future orders.
WHY_IT_MATTERS: >
  If handling an exception on one order leaks back into the shared structure definition, every future order
  silently inherits what was meant to be a single order's exception.
DISCONFIRMING_OBSERVATION: >
  An unusual component quantity recorded on one specific order appears as the new standard quantity on the
  shared structure when a different, later order is opened.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record an atypical component quantity on one order's requirement, then open an unrelated new order for the
  same output and compare its starting requirement to the structure's defined standard.
```

## G06-MRP-Q009

```yaml
QID: G06-MRP-Q009
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a different item is consumed in place of a structure's planned component, the record of what was
  actually consumed names the substituted item, not the originally planned one.
WHY_IT_MATTERS: >
  If the consumption record still names the planned component after a substitution, every downstream use of
  that record — cost, traceability, stock accuracy — is describing an event that did not happen.
DISCONFIRMING_OBSERVATION: >
  After a substitution is made and recorded, the order's consumption history still shows the originally
  planned component rather than, or with no distinction from, the item that was actually used.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a substitution of one component for another during an order's consumption step, then inspect the
  resulting consumption record.
```

## G06-MRP-Q010

```yaml
QID: G06-MRP-Q010
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The value attributed to a substituted component's consumption reflects the cost of the item actually
  consumed, not the cost of the item that had been planned.
WHY_IT_MATTERS: >
  Valuing a substitution at the planned item's cost misstates the true cost of the output whenever the
  substitute has a different cost, which corrupts margin and inventory valuation for that order.
DISCONFIRMING_OBSERVATION: >
  A substituted component with a materially different cost from the planned component still results in the
  order's cost calculation using the planned component's cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set a distinct cost for a substitute item versus the planned component, perform the substitution on an
  order, and trace the resulting cost calculation.
```

## G06-MRP-Q011

```yaml
QID: G06-MRP-Q011
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A substitution between items measured in incompatible units is either blocked or requires an explicit,
  recorded conversion, rather than being accepted at face value.
WHY_IT_MATTERS: >
  Accepting a mismatched-unit substitution without conversion silently misstates the physical quantity
  actually consumed.
DISCONFIRMING_OBSERVATION: >
  A substitution is accepted between two items whose units of measure are incompatible, with no conversion
  applied and no record of how the quantity was reconciled.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to substitute a component with an item recorded in an incompatible unit of measure during
  consumption.
```

## G06-MRP-Q012

```yaml
QID: G06-MRP-Q012
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Whether a person recording production may substitute a component at all is governed by an assignable
  permission, distinct from the general permission to record ordinary consumption.
WHY_IT_MATTERS: >
  Substitution changes what was actually built and its cost; treating it as equivalent to routine consumption
  removes a control point that should exist specifically because substitution is a deviation from the
  approved structure.
DISCONFIRMING_OBSERVATION: >
  A person who can record ordinary component consumption can also perform a substitution with no separate
  permission check and no distinguishing trace of having done so.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Assign a role that can record consumption but attempt to restrict substitution specifically, then test
  whether that role can still substitute.
```

## G06-MRP-Q013

```yaml
QID: G06-MRP-Q013
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The traceability chain recorded for a finished unit reflects the lot or serial of the item actually
  consumed after a substitution, not the lot or serial that would have been consumed under the original plan.
WHY_IT_MATTERS: >
  If traceability still points at the planned component's lot, a recall or quality investigation on the
  substituted item's lot will not find the finished units that actually contain it.
DISCONFIRMING_OBSERVATION: >
  Tracing a finished unit produced with a substituted component leads back to the lot of the originally
  planned component rather than the lot of the item actually consumed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform a substitution using an item from a specific lot, complete the order, and trace the finished unit's
  component lineage.
```

## G06-MRP-Q014

```yaml
QID: G06-MRP-Q014
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A structure level configured to pass through without being separately stocked or tracked does not itself
  accumulate an inventory record; consumption is attributed to the components beneath it.
WHY_IT_MATTERS: >
  If a pass-through level is treated as a real stocked item, a phantom balance appears that does not
  correspond to anything physically held, corrupting on-hand quantity and valuation.
DISCONFIRMING_OBSERVATION: >
  A structure level configured as pass-through shows a non-zero, separately tracked inventory balance of its
  own after orders that use it are processed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure an intermediate structure level as pass-through, process an order that uses it, and inspect
  whether that level accumulated its own stock balance.
```

## G06-MRP-Q015

```yaml
QID: G06-MRP-Q015
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  When a structure references another structure as one of its components, exploding the full requirement
  aggregates quantities across every level without omitting or double-counting a component that appears at
  more than one level.
WHY_IT_MATTERS: >
  A component used both directly and inside a sub-structure that is under- or over-counted misstates the true
  requirement, which drives an incorrect reservation and an incorrect expected consumption.
DISCONFIRMING_OBSERVATION: >
  A component that appears both directly on a structure and inside one of its nested sub-structures is
  counted only once, or counted twice, in the exploded requirement rather than reflecting its true combined
  quantity.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Build a multi-level structure where the same component appears at two levels, then compute the full
  exploded requirement for an order and check the aggregated quantity.
```

## G06-MRP-Q016

```yaml
QID: G06-MRP-Q016
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Revising a sub-structure that is nested inside a parent structure affects an order already in progress for
  the parent according to the same version rule that governs a direct structure revision — it is not treated
  differently just because the change entered through a nested level.
WHY_IT_MATTERS: >
  A different rule for nested changes than for direct changes creates a second, silent path to the same
  problem the version rule exists to prevent.
DISCONFIRMING_OBSERVATION: >
  An order already open for a parent structure changes its requirement when a nested sub-structure is
  revised, even though a direct revision of the parent's own structure would not have changed that same
  order's requirement.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Open an order for a parent structure, revise a nested sub-structure it references, and compare the order's
  requirement before and after against the direct-revision behaviour already established.
```

## G06-MRP-Q017

```yaml
QID: G06-MRP-Q017
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A structure cannot be configured so that, through any chain of nested references, an item ends up listed as
  a component of itself.
WHY_IT_MATTERS: >
  A self-referential structure has no finite exploded requirement, and any process that tries to compute one
  either fails unpredictably or loops indefinitely.
DISCONFIRMING_OBSERVATION: >
  A structure is successfully saved in a configuration where following its nested component references, at
  some depth, leads back to the same item as one of its own components.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to configure a structure so that an item is nested, at some depth, as a component of itself, and
  observe whether the configuration is accepted.
```

## G06-MRP-Q018

```yaml
QID: G06-MRP-Q018
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Consuming a quantity of a component greater than the structure specifies for the order is either blocked,
  or permitted only with the excess recorded as a distinguishable variance — it does not silently blend into
  the order's cost as if it had been planned.
WHY_IT_MATTERS: >
  An unrecorded excess consumption both understates remaining stock unexpectedly and overstates the finished
  output's cost without anyone being able to see why.
DISCONFIRMING_OBSERVATION: >
  An order's recorded consumption exceeds the structure's specified quantity for a component, and nothing in
  the order's record distinguishes the excess from the quantity that was planned.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record consumption of a component in a quantity greater than the structure specifies, then inspect whether
  the excess is separately identifiable.
```

## G06-MRP-Q019

```yaml
QID: G06-MRP-Q019
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Consuming less of a component than the structure specifies, a favourable variance, is captured as a
  distinguishable fact rather than the shortfall simply not appearing anywhere.
WHY_IT_MATTERS: >
  An unrecorded favourable variance hides information about a structure that may be systematically
  over-specified, or about an unauthorized economy being made in production, either of which should be
  visible.
DISCONFIRMING_OBSERVATION: >
  An order closes having consumed less of a component than the structure specifies, with no record anywhere
  that a shortfall against the planned quantity occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close an order having recorded less consumption of a component than the structure specifies, then look for
  a record of the shortfall.
```

## G06-MRP-Q020

```yaml
QID: G06-MRP-Q020
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An over- or under-consumption variance on an order is attributable to a specific order and component, not
  aggregated anonymously across all orders for the same output.
WHY_IT_MATTERS: >
  An anonymous aggregate variance cannot be traced back to a specific cause, a bad batch, an inaccurate
  structure, an operator error, which removes the ability to act on it.
DISCONFIRMING_OBSERVATION: >
  A variance figure exists only as a pooled total across many orders, with no way to attribute a specific
  portion of it back to the individual order and component that produced it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Generate variances on several distinct orders for the same output, then attempt to attribute a reported
  variance total back to an individual order.
```

## G06-MRP-Q021

```yaml
QID: G06-MRP-Q021
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Recording a consumption variance on an order does not itself modify the structure's own defined standard
  quantity.
WHY_IT_MATTERS: >
  If a single order's actual experience silently rewrites the shared standard, the standard stops representing
  an agreed specification and instead drifts with whatever happened most recently.
DISCONFIRMING_OBSERVATION: >
  After a variance is recorded on an order, the structure's own defined standard quantity for that component
  has changed to match the actual consumption, without a separate deliberate revision.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a variance on an order and then inspect the structure's own standard quantity for that component
  afterward.
```

## G06-MRP-Q022

```yaml
QID: G06-MRP-Q022
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Inventory is reduced for a component only when its consumption is actually recorded against an order, not
  automatically in step with the order's expected output quantity.
WHY_IT_MATTERS: >
  Reducing stock based on an assumed rather than an actual consumption event would make the inventory record
  diverge from what was physically used whenever the two differ.
DISCONFIRMING_OBSERVATION: >
  A component's on-hand quantity decreases in line with an order's expected output before or without the
  corresponding actual consumption being recorded.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set an order's expected output quantity, delay recording actual component consumption, and check whether
  on-hand quantity has already moved.
```

## G06-MRP-Q023

```yaml
QID: G06-MRP-Q023
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Recording consumption against one production order cannot be attributed to, or affect the cost of, a
  different production order.
WHY_IT_MATTERS: >
  Cross-attribution between unrelated orders means the cost of one product silently absorbs the material use
  of another, corrupting both orders' costs at once.
DISCONFIRMING_OBSERVATION: >
  Recording a consumption entry while one order is selected results in the quantity or cost impact appearing
  against a different order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Run two production orders concurrently and attempt to record consumption in a way that could be misattributed
  between them, then verify against which order the entry lands.
```

## G06-MRP-Q024

```yaml
QID: G06-MRP-Q024
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When an order produces fewer good units than planned, the shortfall is captured as a distinguishable fact
  rather than the order simply closing as if the lower quantity had always been the target.
WHY_IT_MATTERS: >
  If a shortfall is invisible, no one can see that a process is systematically under-yielding, and the
  components already consumed for the missing units appear to have vanished for no recorded reason.
DISCONFIRMING_OBSERVATION: >
  An order that produces fewer good units than its planned quantity closes with no distinguishable record that
  a shortfall against the plan occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete an order with a good-output quantity below its planned quantity, then inspect the order's record for
  a distinguishable shortfall indicator.
```

## G06-MRP-Q025

```yaml
QID: G06-MRP-Q025
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Scrapping a partially built item during production is recorded as a transaction distinct from ordinary
  component consumption, carrying its own value.
WHY_IT_MATTERS: >
  If a scrapped partial build is folded into ordinary consumption with no separate value, the cost of the
  scrap is invisible and cannot be tracked, questioned, or reduced.
DISCONFIRMING_OBSERVATION: >
  Scrapping a partially built item during an order leaves no transaction distinguishable from ordinary
  component consumption, and no value is attributed to the scrap event itself.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Scrap a partially built item mid-order and inspect whether a distinct, valued transaction was recorded for
  it.
```

## G06-MRP-Q026

```yaml
QID: G06-MRP-Q026
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A scrap transaction can be attributed to a defined cause or reason category, distinguishing it from an
  unexplained loss.
WHY_IT_MATTERS: >
  Anonymous scrap with no cause attached cannot be analysed for a systematic problem, whereas categorised
  scrap can be tracked back to a specific process or material issue over time.
DISCONFIRMING_OBSERVATION: >
  A scrap transaction can be recorded with no cause or reason attached at all, and no way to add one later.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to record a scrap transaction and check whether a cause or reason field is required, optional, or
  absent.
```

## G06-MRP-Q027

```yaml
QID: G06-MRP-Q027
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Reducing an order's expected output quantity partway through production is a distinct, recorded action, not
  something that happens implicitly by the order simply being closed at whatever quantity was actually
  achieved.
WHY_IT_MATTERS: >
  If a lowered expectation is indistinguishable from an order that always intended that quantity, no one
  reviewing the order later can tell that the original plan was not met.
DISCONFIRMING_OBSERVATION: >
  An order's originally planned output quantity cannot be recovered once the order closes at a lower actual
  quantity, with no trace of the reduction as a distinct event.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Open an order with a planned output quantity, reduce it or close at a lower quantity, and check whether the
  original plan remains visible.
```

## G06-MRP-Q028

```yaml
QID: G06-MRP-Q028
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The cost impact of yield loss on an order is attributed to a visible position in that order's cost
  breakdown, rather than being spread silently and undetectably across the good units produced.
WHY_IT_MATTERS: >
  If yield loss cost is silently absorbed into the good units, the reported unit cost of the product is
  inflated by a hidden amount that no one can see or question.
DISCONFIRMING_OBSERVATION: >
  An order with a significant yield shortfall shows no distinguishable yield-loss cost component, with the
  full component cost instead spread evenly across the good units actually produced.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete an order with a material yield shortfall and inspect its cost breakdown for a distinguishable loss
  component versus an evenly spread unit cost.
```

## G06-MRP-Q029

```yaml
QID: G06-MRP-Q029
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A by-product produced alongside the main output receives its own recorded value, separate from the value
  attributed to the main output.
WHY_IT_MATTERS: >
  If a by-product's value is folded undifferentiated into the main output, the main output's cost is
  misstated and the by-product's own value is invisible for any later use or sale.
DISCONFIRMING_OBSERVATION: >
  An order that produces a by-product records no separate value for it, with the by-product's material and
  processing cost entirely subsumed into the main output's cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete an order configured to produce both a main output and a by-product, then inspect whether the
  by-product has its own recorded value.
```

## G06-MRP-Q030

```yaml
QID: G06-MRP-Q030
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The method by which value is split between the main output and a by-product is a defined, visible setting,
  not an undocumented default that can change without anyone choosing to change it.
WHY_IT_MATTERS: >
  An invisible split method means the same order run twice under identical conditions could report different
  costs for the main output with no explanation available to whoever asks why.
DISCONFIRMING_OBSERVATION: >
  The proportion of value allocated to the main output versus a by-product differs between two otherwise
  identical orders, with no configuration change made between them and no record explaining the difference.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Run two otherwise identical orders producing the same main output and by-product, and compare the resulting
  value split between them.
```

## G06-MRP-Q031

```yaml
QID: G06-MRP-Q031
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A by-product's own lot or serial traceability is recorded independently of the main output's traceability,
  even though both originate from the same order.
WHY_IT_MATTERS: >
  If the by-product inherits or is conflated with the main output's trace, a quality issue found in one
  cannot be correctly scoped to only the units it actually affects.
DISCONFIRMING_OBSERVATION: >
  Tracing a by-product unit produces the same, indistinguishable trace record as the main output unit from the
  same order, rather than its own.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete an order producing a tracked by-product alongside a tracked main output, and compare the two
  units' trace records.
```

## G06-MRP-Q032

```yaml
QID: G06-MRP-Q032
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Not recording or not confirming a by-product that the structure defines does not silently increase the
  recorded value of the main output to absorb what the by-product would have carried.
WHY_IT_MATTERS: >
  An automatic reallocation when a by-product goes unrecorded would inflate the main output's cost based on an
  assumption no one explicitly made, rather than reflecting what was actually produced.
DISCONFIRMING_OBSERVATION: >
  An order whose by-product is not recorded or confirmed shows a higher main-output unit cost than an
  otherwise identical order where the by-product was recorded, with no explicit reallocation decision made.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Run two otherwise identical orders, recording the by-product on one and omitting it on the other, and
  compare the resulting main-output unit cost.
```

## G06-MRP-Q033

```yaml
QID: G06-MRP-Q033
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  When operations on an order are configured to run in a required sequence, completing a later operation
  before an earlier required one is either blocked or recorded as an explicit, visible exception.
WHY_IT_MATTERS: >
  Silently allowing sequence to be skipped defeats the purpose of declaring a sequence at all, and hides a
  real process deviation that quality or scheduling would want to know about.
DISCONFIRMING_OBSERVATION: >
  An operation configured to require a prior operation's completion can be completed first, with no block and
  no visible record that the sequence was bypassed.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Configure two operations on an order with a required sequence, attempt to complete the later one first, and
  observe the result.
```

## G06-MRP-Q034

```yaml
QID: G06-MRP-Q034
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Skipping an intermediate operation entirely and completing only a later one leaves the skipped operation
  visibly incomplete, rather than it being silently marked complete to keep the order's overall status
  consistent.
WHY_IT_MATTERS: >
  A silently auto-completed operation creates a false record that work happened which did not, which corrupts
  both the time or quantity record for that operation and anyone relying on it as evidence.
DISCONFIRMING_OBSERVATION: >
  An intermediate operation that was never actioned shows as complete once a later operation on the same order
  is completed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a later operation on an order while leaving an earlier intermediate operation unactioned, then
  inspect the intermediate operation's own status.
```

## G06-MRP-Q035

```yaml
QID: G06-MRP-Q035
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Operations that are configured to be eligible for parallel execution are not forced into a strict sequence
  by default; sequence is enforced only where it has been explicitly configured.
WHY_IT_MATTERS: >
  Forcing sequence where none was intended would block legitimate concurrent work and misrepresent the actual
  process the structure was designed to allow.
DISCONFIRMING_OBSERVATION: >
  Two operations explicitly configured as not requiring a sequence between them cannot both be worked on or
  completed independently, one being blocked until the other finishes.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure two operations on an order with no sequence dependency between them, and attempt to work on both
  independently.
```

## G06-MRP-Q036

```yaml
QID: G06-MRP-Q036
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing an operation's completed status after the fact leaves a record of who reversed it and when,
  rather than the operation simply reverting to an incomplete state with no trace that it was ever marked
  done.
WHY_IT_MATTERS: >
  An untraceable reversal of a completed operation removes accountability for a change to the production
  record and could be used to quietly rewrite what actually happened.
DISCONFIRMING_OBSERVATION: >
  An operation's status is reverted from complete back to incomplete with no record anywhere of who performed
  the reversal or when.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Mark an operation complete, then reverse that status, and inspect the record for who performed the reversal
  and when.
```

## G06-MRP-Q037

```yaml
QID: G06-MRP-Q037
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A quantity reported by the person performing an operation and a quantity later corrected by a supervisor
  both remain visible on the order's record, rather than the correction silently overwriting the original with
  no trace of the discrepancy.
WHY_IT_MATTERS: >
  If the original figure is overwritten with no trace, a pattern of over- or under-reporting by a particular
  operation or person becomes invisible, and the correction cannot itself be reviewed.
DISCONFIRMING_OBSERVATION: >
  A supervisor's corrected quantity replaces the originally reported quantity on an order with no remaining
  record of what was first reported.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Report a quantity for an operation, have it corrected by a different role, and inspect whether the original
  reported value remains visible.
```

## G06-MRP-Q038

```yaml
QID: G06-MRP-Q038
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Time recorded against an operation is attributed to the specific person or resource that performed it,
  distinguishable from a default or estimated duration the system might otherwise apply.
WHY_IT_MATTERS: >
  If actual and defaulted time are indistinguishable, labour cost and efficiency figures for an operation
  cannot be trusted to reflect what actually happened versus what the system assumed.
DISCONFIRMING_OBSERVATION: >
  The time recorded against a completed operation cannot be identified as either an actual reported duration
  or a system-applied default.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete one operation with an actively reported duration and leave a comparable operation to receive any
  default duration, then compare how each is distinguished in the record.
```

## G06-MRP-Q039

```yaml
QID: G06-MRP-Q039
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A discrepancy between a reported quantity or time and what was originally expected for an operation is
  preserved as a visible fact, not silently reconciled back to the expected value with no trace that a
  discrepancy occurred.
WHY_IT_MATTERS: >
  Silent self-correction to the expected value hides exactly the information, that reality diverged from the
  plan, that this kind of record exists to capture.
DISCONFIRMING_OBSERVATION: >
  An operation reported with a quantity or time different from what was expected shows only the expected value
  once saved, with no trace that a different value was actually reported.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Report a quantity or time for an operation that differs from its expected value, save it, and inspect
  whether the discrepancy remains visible.
```

## G06-MRP-Q040

```yaml
QID: G06-MRP-Q040
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Whether an operation can be marked complete before the components it depends on have had their consumption
  recorded is a defined, consistent rule, not one that varies unpredictably by how the operation is reached.
WHY_IT_MATTERS: >
  An inconsistent rule means the same real-world situation, completing work before its material is recorded,
  is sometimes permitted and sometimes not, for no reason connected to the actual state of the order.
DISCONFIRMING_OBSERVATION: >
  Marking an operation complete ahead of its component consumption succeeds through one supported path and is
  blocked through another supported path, for the same order and the same operation.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Identify more than one supported way to mark an operation complete ahead of its component consumption, and
  attempt each to compare the outcome.
```

## G06-MRP-Q041

```yaml
QID: G06-MRP-Q041
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order after it has already consumed some components and produced some output leaves the
  already-consumed components in a distinguishable, recorded state rather than silently returning them to
  available stock as if consumption never happened.
WHY_IT_MATTERS: >
  Silently reverting consumption on cancellation makes stock appear available that was physically used, which
  can lead to double-use of the same physical material.
DISCONFIRMING_OBSERVATION: >
  Cancelling a partially consumed order returns the already-consumed component quantities to available stock
  automatically, with no distinct record of the reversal decision.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Partially consume components and produce partial output on an order, cancel it, and inspect what happens to
  the already-consumed quantities.
```

## G06-MRP-Q042

```yaml
QID: G06-MRP-Q042
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a partially completed order does not erase the record that partial output was actually produced
  before cancellation.
WHY_IT_MATTERS: >
  If cancellation retroactively erases evidence of partial output, physical units that exist and may already
  be in use or in stock become untraceable to the order that made them.
DISCONFIRMING_OBSERVATION: >
  After cancelling a partially completed order, there is no remaining record that any output had been produced
  before the cancellation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce partial output on an order, cancel the order, and inspect whether the partial output remains on
  record.
```

## G06-MRP-Q043

```yaml
QID: G06-MRP-Q043
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing, unbuilding, a completed order returns the original components at the value and lot or serial
  they were originally consumed at, not a freshly re-derived default value or an unspecified lot.
WHY_IT_MATTERS: >
  Returning components at a re-derived value rather than their original recorded value creates a valuation
  gain or loss that has no real transaction behind it, and returning them with no lot reference breaks
  traceability.
DISCONFIRMING_OBSERVATION: >
  Unbuilding a completed order returns components valued or lotted differently from how they were originally
  recorded as consumed on that same order.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Complete an order with tracked, valued component consumption, then unbuild it, and compare the returned
  components' value and lot reference to the original consumption record.
```

## G06-MRP-Q044

```yaml
QID: G06-MRP-Q044
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Unbuilding one completed order cannot reverse consumption that actually belongs to a different order, even
  where both orders consumed the same component.
WHY_IT_MATTERS: >
  Cross-order reversal would restore stock and adjust costs for the wrong order entirely, corrupting two
  orders' records with a single action.
DISCONFIRMING_OBSERVATION: >
  Unbuilding one order affects the recorded consumption or cost of a different order that shares the same
  component.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Run two orders that both consume the same component, unbuild one of them, and check whether the other
  order's own consumption record was affected.
```

## G06-MRP-Q045

```yaml
QID: G06-MRP-Q045
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Components reserved for a cancelled order, but never actually consumed, are released and made available to
  other demand rather than remaining locked indefinitely against the cancelled order.
WHY_IT_MATTERS: >
  Stock locked against a cancelled order that will never consume it is unavailable to legitimate demand for no
  operational reason, which understates true availability elsewhere.
DISCONFIRMING_OBSERVATION: >
  A component reserved for an order that is subsequently cancelled remains unavailable to other demand after
  the cancellation.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve a component on an order, cancel the order without consuming the component, and check whether the
  reservation is released for other demand.
```

## G06-MRP-Q046

```yaml
QID: G06-MRP-Q046
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing an order whose output has already been consumed elsewhere, used in another order, shipped, or
  otherwise moved on, is blocked or explicitly flagged, rather than silently proceeding and leaving the
  downstream consumption pointing at output that no longer exists.
WHY_IT_MATTERS: >
  Silently allowing the reversal would create a downstream record that references output which has been
  retroactively un-produced, an inconsistency that can surface as an unexplained inventory shortfall much
  later.
DISCONFIRMING_OBSERVATION: >
  An order whose output has already been consumed by another transaction can be fully unbuilt with no block,
  warning, or flag referencing the downstream consumption.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Complete an order, consume its output in a downstream transaction, then attempt to unbuild the original
  order and observe whether the downstream use is flagged.
```

## G06-MRP-Q047

```yaml
QID: G06-MRP-Q047
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Recording consumption of a component when the required quantity is not physically on hand either blocks the
  action or explicitly and visibly permits stock to go negative — it does not silently record the consumption
  as if the quantity had been available.
WHY_IT_MATTERS: >
  A silent, unflagged negative-stock consumption hides a real shortage that should be a visible operational
  problem, and can mask a shortfall until a much later physical count discovers it.
DISCONFIRMING_OBSERVATION: >
  Consumption is recorded for a quantity greater than what is on hand, with the resulting negative or
  insufficient stock position not visibly flagged anywhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to record consumption of a component in a quantity exceeding what is currently on hand, and observe
  whether the system blocks, warns, or silently accepts it.
```

## G06-MRP-Q048

```yaml
QID: G06-MRP-Q048
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A quantity of a component reserved for one order is not simultaneously counted as available to satisfy a
  different order's demand for the same component.
WHY_IT_MATTERS: >
  Double-counting a reserved quantity as available elsewhere means two orders can both plan around the same
  physical units, guaranteeing one of them cannot actually be fulfilled as planned.
DISCONFIRMING_OBSERVATION: >
  The same physical quantity of a component is shown as available to a second order's demand while it remains
  reserved and unconsumed against a first order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve a component quantity against one order, then check whether that same quantity appears available when
  checking a second order's demand for the same component.
```

## G06-MRP-Q049

```yaml
QID: G06-MRP-Q049
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The quantity of a component reserved against open orders is distinguishable from total on-hand quantity when
  a person checks availability for a new order.
WHY_IT_MATTERS: >
  If reserved and on-hand quantities are shown as one undifferentiated figure, whoever is planning a new order
  has no way to know how much is genuinely free to commit.
DISCONFIRMING_OBSERVATION: >
  Checking availability for a component shows only a single combined figure with no way to see how much of it
  is already reserved against other open orders.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Reserve part of a component's stock against an open order, then check the availability view for that
  component and look for a breakdown between reserved and free quantity.
```

## G06-MRP-Q050

```yaml
QID: G06-MRP-Q050
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling the reservation held by one order makes that quantity available to competing demand promptly,
  rather than the quantity remaining effectively held for some indefinite further period.
WHY_IT_MATTERS: >
  A reservation that lingers after it is cancelled understates true availability and can cause a planner to
  unnecessarily source or delay against a shortage that no longer exists.
DISCONFIRMING_OBSERVATION: >
  A component's reservation is cancelled on one order, but the quantity does not become available to a second
  order's demand check performed immediately afterward.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Cancel a reservation on one order and immediately check whether the released quantity is available to a
  second order.
```

## G06-MRP-Q051

```yaml
QID: G06-MRP-Q051
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Proceeding with consumption despite a component shortage, when this is permitted at all, leaves a trace of
  who authorized or performed the override.
WHY_IT_MATTERS: >
  An untraceable override removes accountability for a decision to accept negative stock or force production
  ahead of material availability, which is exactly the kind of decision that should be attributable to a
  person.
DISCONFIRMING_OBSERVATION: >
  Consumption is recorded past a component shortage with no record of who performed or approved the override.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Force consumption through a component shortage and inspect the record for who is attributed to that action.
```

## G06-MRP-Q052

```yaml
QID: G06-MRP-Q052
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When two orders compete for the same limited quantity of a component, which one is satisfied first follows a
  deterministic, identifiable rule, such as order date or a defined priority, rather than depending on which
  one happened to be processed first by chance.
WHY_IT_MATTERS: >
  A non-deterministic allocation makes production planning unreliable, since the same starting conditions
  could produce a different outcome each time depending on incidental timing.
DISCONFIRMING_OBSERVATION: >
  Running the same competing-demand scenario for two orders more than once, under identical priority and
  order-date conditions, allocates the limited component to a different order on different runs.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Create two orders with identical priority and date competing for a limited component quantity, and observe
  the allocation rule applied.
```

## G06-MRP-Q053

```yaml
QID: G06-MRP-Q053
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A finished unit's lot or serial can be traced backward to the specific lots or serials of every tracked
  component actually consumed to produce it.
WHY_IT_MATTERS: >
  Backward traceability is the mechanism that lets a quality issue found in a finished unit be traced to the
  specific incoming material responsible, rather than to every batch of that material ever received.
DISCONFIRMING_OBSERVATION: >
  Tracing a finished unit's lot or serial backward does not surface the specific component lots or serials
  that were actually consumed to produce it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete an order using tracked component lots or serials, and trace the finished unit backward to its
  component origins.
```

## G06-MRP-Q054

```yaml
QID: G06-MRP-Q054
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A component's lot or serial can be traced forward to every finished unit it contributed to, across every
  order that consumed it.
WHY_IT_MATTERS: >
  Forward traceability is what makes a recall possible: without it, a defective incoming lot cannot be
  connected to the full set of finished units that may be affected.
DISCONFIRMING_OBSERVATION: >
  Tracing a component lot or serial forward misses one or more finished units that were actually produced
  using it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consume the same tracked component lot across more than one order, then trace that lot forward and check
  that every resulting finished unit is found.
```

## G06-MRP-Q055

```yaml
QID: G06-MRP-Q055
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a substitution changes which lot or serial was actually consumed, the traceability chain reflects the
  actual lot consumed, not the lot that would have been consumed under the original plan.
WHY_IT_MATTERS: >
  A traceability chain that still points at the planned rather than the actual lot after a substitution
  defeats both forward and backward tracing for exactly the events where a substitution made them most
  necessary.
DISCONFIRMING_OBSERVATION: >
  Backward tracing a finished unit produced with a substituted component surfaces the originally planned lot
  rather than the lot of the item actually consumed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform a substitution using a specific lot, complete the order, and backward-trace the finished unit.
```

## G06-MRP-Q056

```yaml
QID: G06-MRP-Q056
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a produced lot is later split across different locations or used by different downstream orders, the
  traceability link back to the original consumption event is preserved for each resulting portion.
WHY_IT_MATTERS: >
  If splitting a lot breaks the link back to its origin, only the portion that happens to keep the original
  record remains traceable, and the rest becomes untraceable exactly when a recall needs to reach it.
DISCONFIRMING_OBSERVATION: >
  After a produced lot is split, one or more of the resulting portions no longer trace back to the original
  production order and its component consumption.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce a tracked lot, split it across two locations or downstream uses, and trace each resulting portion
  back to its origin.
```

## G06-MRP-Q057

```yaml
QID: G06-MRP-Q057
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Traceability data recorded for an order persists after that order is cancelled or reversed, rather than
  being deleted along with the order.
WHY_IT_MATTERS: >
  If cancelling or reversing an order deletes its traceability record, any physical units that already exist
  from the partial run before cancellation become untraceable.
DISCONFIRMING_OBSERVATION: >
  Cancelling or unbuilding an order removes the traceability record connecting its consumed components to
  whatever output had already been produced.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce partial tracked output on an order, cancel or unbuild the order, and check whether the traceability
  record for the already-produced output still exists.
```

## G06-MRP-Q058

```yaml
QID: G06-MRP-Q058
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When components are consumed on an order in one accounting period but the order's output is not received
  until a following period, the value of the components already consumed is recognisable as an in-process
  position at the end of the first period, rather than the value disappearing from view between the two
  periods.
WHY_IT_MATTERS: >
  If the consumed value is neither still shown as work-in-process nor yet shown as finished-output value, it
  is unaccounted for at the period end, which misstates the position at exactly the moment a closing figure is
  produced.
DISCONFIRMING_OBSERVATION: >
  At the end of a period in which components were consumed but no output was yet received, the value of those
  components does not appear in any in-process or work-in-progress position.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Consume components on an order near the end of a period without completing the order, close the period, and
  check for a recognisable in-process value.
```

## G06-MRP-Q059

```yaml
QID: G06-MRP-Q059
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Closing an accounting period does not block or corrupt an order that is legitimately still open and
  spanning that period boundary.
WHY_IT_MATTERS: >
  If period close forces an order closed or blocks further recording against it, production activity is
  disrupted by an accounting event that should be able to coexist with genuinely ongoing work.
DISCONFIRMING_OBSERVATION: >
  Closing a period forces a still-open order into a closed or corrupted state, or blocks all further recording
  against it, even though the order has not itself been completed.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Leave an order open and spanning a period boundary, close the earlier period, and observe the effect on the
  still-open order.
```

## G06-MRP-Q060

```yaml
QID: G06-MRP-Q060
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Value recorded for an order that spans a period boundary is attributed to the period in which each
  underlying event actually occurred, not entirely to the period in which the order happens to finally close.
WHY_IT_MATTERS: >
  Attributing all value to the closing period regardless of when consumption actually happened shifts cost
  between periods, which distorts each period's own reported result.
DISCONFIRMING_OBSERVATION: >
  An order spanning two periods attributes the full value of components consumed in the earlier period to the
  later period in which the order happens to close.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Consume components in one period and complete the order in the following period, then check which period
  the consumption value is attributed to.
```

## G06-MRP-Q061

```yaml
QID: G06-MRP-Q061
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Scheduling an order against a resource's declared capacity does not silently permit that resource to be
  planned beyond its declared capacity without an explicit warning or override being recorded.
WHY_IT_MATTERS: >
  Silent over-scheduling defeats the purpose of declaring a capacity limit at all, and creates a schedule that
  looks feasible on paper but cannot actually be executed.
DISCONFIRMING_OBSERVATION: >
  An order is scheduled against a resource whose declared capacity is already fully committed for that
  window, with no warning and no recorded override.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Fully commit a resource's declared capacity for a window, then attempt to schedule an additional order
  against the same resource and window.
```

## G06-MRP-Q062

```yaml
QID: G06-MRP-Q062
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A resource that becomes unavailable partway through an operation produces a visible exception, rather than
  the operation continuing to appear scheduled or in progress through the unavailable window as if nothing
  had changed.
WHY_IT_MATTERS: >
  An operation that silently continues on paper despite the resource being unavailable creates a schedule and
  a status that no longer describe what is physically happening.
DISCONFIRMING_OBSERVATION: >
  A resource marked unavailable mid-operation leaves the operation showing as normally scheduled or in
  progress, with no visible exception raised.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Mark a resource unavailable while an operation using it is in progress, and check whether an exception
  becomes visible.
```

## G06-MRP-Q063

```yaml
QID: G06-MRP-Q063
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When two orders are scheduled to the same limited resource in an overlapping window, which one takes
  priority follows a deterministic, identifiable rule rather than an arbitrary or unexplained outcome.
WHY_IT_MATTERS: >
  An unexplained priority outcome makes the schedule unreliable for planning, since the same conflict could
  resolve differently with no way to predict or justify which order wins.
DISCONFIRMING_OBSERVATION: >
  Two orders competing for the same resource and window, under identical stated priority, resolve differently
  on separate occasions with no identifiable rule explaining the difference.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Schedule two orders to the same resource in an overlapping window with identical stated priority, and
  observe how the conflict resolves.
```

## G06-MRP-Q064

```yaml
QID: G06-MRP-Q064
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Force-closing or force-completing an order ahead of its normal completion conditions is restricted to a role
  holding a specific authority for that action, distinct from the ordinary role that records day-to-day
  consumption and completion.
WHY_IT_MATTERS: >
  If any ordinary production role can force an order closed regardless of its actual state, the completion
  conditions the process depends on, full consumption, sequence, output confirmation, become optional in
  practice for anyone who chooses to bypass them.
DISCONFIRMING_OBSERVATION: >
  A role with only ordinary day-to-day production permissions can force-close or force-complete an order
  without a separate, distinguishing permission being required.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Attempt a force-close or force-complete action on an order using a role with only ordinary production
  permissions, and observe whether it is permitted.
```

## G06-MRP-Q065

```yaml
QID: G06-MRP-Q065
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order that is in progress leaves a record of who performed the cancellation and when,
  distinct from and not overwriting the order's own completion or output timestamps.
WHY_IT_MATTERS: >
  If the cancellation actor and time are not recorded separately, or overwrite the order's other timestamps,
  there is no way to later establish who decided to stop the order and when that decision was made.
DISCONFIRMING_OBSERVATION: >
  Cancelling an in-progress order leaves no separate record of who cancelled it or when, or that record
  overwrites the order's own completion or output timestamp.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel an order that is in progress and inspect the record for a cancellation actor and timestamp distinct
  from the order's other timestamps.
```

## G06-MRP-Q066

```yaml
QID: G06-MRP-Q066
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Reopening an order that has already reached a closed or done state is either not possible through ordinary
  action, or leaves an explicit, visible trace — it does not silently revert to an earlier state as if it had
  never been closed.
WHY_IT_MATTERS: >
  A silent reopen removes the meaning of closed as a fixed point in the record, since anyone could later
  discover the order had been quietly reworked with no sign that it happened.
DISCONFIRMING_OBSERVATION: >
  A closed or done order is reverted to an earlier, open state with no visible record that a reopening
  occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close or mark an order done, attempt to reopen it, and inspect whether the action is blocked or left an
  explicit trace.
```

## G06-MRP-Q067

```yaml
QID: G06-MRP-Q067
MODULE: mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A person with no assigned production authorization for a given order cannot record consumption or
  completion against that order.
WHY_IT_MATTERS: >
  If authorization is not actually enforced at the point of recording consumption or completion, the
  assignment of production roles is a label with no operational effect, and anyone can act on any order.
DISCONFIRMING_OBSERVATION: >
  A person with no production authorization assigned for a specific order is able to record consumption or
  mark completion against that order regardless.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to record consumption or completion against an order using a person or role with no production
  authorization assigned for it, and observe whether the action is blocked.
```
