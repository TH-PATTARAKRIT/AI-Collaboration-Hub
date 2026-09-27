# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_mrp_stock_landed_costs Module Bridge MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_MRP_STOCK_LANDED_COSTS-MVQ20-V1.00
**Group:** G12 PROJECT
**Module Metadata:** `project_mrp_stock_landed_costs`
**Wave:** GMVQ 25-Team Acceleration (2026-09-27)
**Author Cell:** P12-3 (GMVQ Question Factory — Production Cell P12-3)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 20
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 20 = 75
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `project_mrp_stock_landed_costs`, the
four-participant seam that exists only where all four are jointly in play: a project task's own
material cost tracking, the manufacturing order that produced the item concerned, the physical stock
movement of that item, AND a landed cost allocation (an additional charge such as freight, duty or
insurance applied on top of the item's base valuation). Per the GMVQ Bridge Module Rule V1.00 and
this group's own arity discipline, this bank was authored under the strict expectation, stated in
GROUP_BRIEF_G12_PROJECT.md, that a 3-4 way bridge may not reach 48 distinct seam questions honestly.

Mandatory pre-authoring sibling check performed per GMVQ_BRIDGE_MODULE_RULE_V1.00 §5:
`grep -h 'HYPOTHESIS'` was run against `G05_INVENTORY/G05_STOCK_LANDED_COSTS_GMVQ_MVQ_50_V1.00_DRAFT.md`
and `G06_MANUFACTURING/G06_MRP_LANDED_COSTS_GMVQ_MVQ_48_V1.00_DRAFT.md` in full before authoring. No
question below restates a pure `stock_landed_costs` hypothesis (allocation basis, reversal, period
lock, multi-lot/multi-location split — all with no project or manufacturing order in the picture) or
a pure `mrp_landed_costs` hypothesis (a later-arriving cost allocated back onto already-produced,
already-sold or already-scrapped output — with no project task or project-tracked consumption in the
picture). Every question here requires that a project task's own view of the material's cost is the
thing that can disagree with the landed-cost-and-production combination underneath it; a question
that would still make complete sense for a landed cost applied to manufactured stock with no project
task consuming it does not belong here.

## Control

**Arity owned: FOUR-PARTICIPANT (project task's material cost view + manufacturing order + physical
stock movement + landed cost allocation) only.** Every question below requires all four to be
jointly present; a question answerable by any three of the four with the project task removed does
not belong here.

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: these 20 questions test 20 distinct material seam hypotheses. A mandatory
  ARITY EXHAUSTION STATEMENT follows the questions, per GMVQ_BRIDGE_MODULE_RULE_V1.00 §7, because the
  48 floor is genuinely not reachable at this arity without duplicating lower-arity sibling ground.
- Question text is source-neutral: no vendor or product name, no technical identifier, and the
  module's own metadata name never appears outside the `MODULE:` field.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q001

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q001
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where a landed cost is applied to the components consumed by a production order, and that order's output is then issued to a project task, the task's own material cost view reflects the landed-cost-augmented value rather than the item's base manufacturing cost alone.
WHY_IT_MATTERS: >
  Showing only the base cost would understate the project task's true material cost by exactly the charge that was deliberately added to reflect the real cost of acquiring the components.
DISCONFIRMING_OBSERVATION: >
  A project task's own material cost view for an issued item shows only its base manufacturing cost, with no trace of a landed cost already applied to that item's consumed components.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost to the components of a production order, issue that order's output to a project task, and check whether the task's material cost view reflects the landed-cost-augmented value.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q002

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q002
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A landed cost that arrives and is applied only after a manufactured item has already been issued to a project task results in a documented restatement of that task's already-recognized material cost, rather than the task's figure remaining permanently understated.
WHY_IT_MATTERS: >
  A permanently understated figure would leave the project's own cost record silently missing a charge that legitimately belongs to material it already consumed.
DISCONFIRMING_OBSERVATION: >
  Applying a landed cost after the manufactured item was already issued to a project task leaves that task's recognized material cost unchanged, with no documented restatement.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Issue a manufactured item to a project task, then apply a landed cost to the components that produced it, and check whether the task's already-recognized cost is restated.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q003

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q003
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing or unbuilding a production order whose output, carrying an applied landed cost, was already issued to a project task correctly unwinds both the base manufacturing cost portion and the landed cost portion from that task's own recognized figure.
WHY_IT_MATTERS: >
  Unwinding only one of the two portions would leave the project task's cost figure matching neither the pre-reversal nor the post-reversal reality.
DISCONFIRMING_OBSERVATION: >
  Reversing or unbuilding the production order removes the base manufacturing cost from the project task's recognized figure but leaves the landed cost portion in place, or vice versa.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue a landed-cost-augmented manufactured item to a project task, reverse or unbuild the production order that made it, and check whether both cost portions are removed from the task's figure.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q004

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q004
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Returning an unused, landed-cost-augmented manufactured item from a project task back to stock credits the project task's own recognized cost by the item's full value, including its landed cost share, rather than only its base manufacturing cost.
WHY_IT_MATTERS: >
  Crediting only the base cost would leave the project task's figure overstated by the landed cost share of material it no longer holds.
DISCONFIRMING_OBSERVATION: >
  Returning a landed-cost-augmented item from a project task to stock credits the task's recognized cost by only the base manufacturing value, omitting the landed cost share.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue a landed-cost-augmented manufactured item to a project task, return the unused item to stock, and check the full value credited back against the task's recognized cost.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q005

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q005
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where two project tasks each draw a share of one manufactured batch that carries a single landed cost document, each task's own recognized cost reflects only its own proportionate share of that landed cost, not the document's full amount independently claimed by both.
WHY_IT_MATTERS: >
  Both tasks independently claiming the full landed cost would overstate the combined true material cost across the two projects.
DISCONFIRMING_OBSERVATION: >
  Two project tasks drawing from the same landed-cost-bearing manufactured batch each show the landed cost document's full amount in their own recognized cost, rather than a proportionate share.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply one landed cost document to a manufactured batch drawn on by two separate project tasks, and compare each task's recognized cost against its own proportionate share.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q006

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q006
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When two production runs, each carrying its own different landed cost per unit, are merged into one lot before issue to a project task, the task's recognized cost for units drawn from that lot reflects each unit's own originating landed cost rather than one blended figure applied to all.
WHY_IT_MATTERS: >
  A single blended figure would misstate the true cost of whichever specific units the project task actually consumed.
DISCONFIRMING_OBSERVATION: >
  A project task drawing from a merged lot shows the same blended per-unit cost for units that actually carried two different landed cost amounts before the merge.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Merge two production runs with different applied landed costs per unit into one lot, issue units from that lot to a project task, and check whether the task's recognized cost distinguishes the originating landed cost.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q007

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q007
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A project task fed by a production order whose several components each carry their own separately applied landed cost has a total recognized material cost that reconciles to the sum of the manufacturing operation cost and every component's own landed cost share.
WHY_IT_MATTERS: >
  A total that does not reconcile would mean at least one component's landed cost share was lost or duplicated somewhere in the roll-up to the project task.
DISCONFIRMING_OBSERVATION: >
  A project task's total recognized material cost does not equal the sum of its production order's operation cost and each consumed component's own landed cost share.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply separate landed costs to several components consumed by one production order feeding a project task, and check whether the task's total recognized cost reconciles to the sum of all the pieces.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q008

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q008
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project task closed or archived before a landed cost belonging to a component its linked production order already consumed is finally applied does not leave that landed cost's share with no documented destination once it does post.
WHY_IT_MATTERS: >
  A landed cost with nowhere documented to land would either be silently dropped or attributed to a project no reviewer would think to check.
DISCONFIRMING_OBSERVATION: >
  A landed cost applied after its consuming project task is closed or archived posts with no documented destination connecting it back to that task's already-closed cost record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Close or archive a project task whose linked production order already consumed a component awaiting a landed cost, apply that landed cost afterward, and check where its share is documented.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q009

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q009
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where the project's company, the company operating the production run, and the company that recorded the landed cost charge are three different entities, the project task's recognized material cost posts against one documented entity's ledger with any required inter-company transactions generated alongside it.
WHY_IT_MATTERS: >
  A missing inter-company step across three entities would leave at least one entity's books recognizing a cost with no corresponding transaction on the entity that actually incurred it.
DISCONFIRMING_OBSERVATION: >
  The project task's recognized material cost, combining production and a landed cost from three different companies, posts without the corresponding inter-company transactions that a three-entity movement should generate.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Configure a project, its production run, and its landed cost charge under three different companies, issue material to the project task, and check whether all required inter-company entries are generated.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q010

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q010
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Where a landed cost charge is recorded in a currency different from both the manufacturing order's own costing currency and the project's own reporting currency, the project task's recognized material cost uses one documented rate and moment consistently across views.
WHY_IT_MATTERS: >
  Inconsistent conversion between reports of the same three-currency transaction would make the project task's recognized cost numerically unreliable.
DISCONFIRMING_OBSERVATION: >
  Two different reports of the same project task's recognized material cost, across the three currencies involved, use different conversion rates or moments for the same underlying landed cost and production event.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost in a third currency to a production order feeding a project task whose own currency and whose production's costing currency both differ, and compare the task's cost across two reports.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q011

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q011
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project closed while a landed cost targeting a component its production order already consumed remains only partly posted does not leave that partial posting's remainder silently abandoned with no path to complete it against the now-closed project's task.
WHY_IT_MATTERS: >
  A silently abandoned remainder would leave a real charge permanently unresolved with no visible trace connecting it back to the project it belongs to.
DISCONFIRMING_OBSERVATION: >
  Closing the project while a targeting landed cost remains only partly posted leaves the unposted remainder with no documented path to complete it against the task's record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Leave a landed cost targeting a project task's consumed component only partly posted, close the project, and check whether a documented path remains to complete the posting.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q012

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q012
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Scrap recorded during production of a project-destined item that also carries an applied landed cost share has that landed cost share reflected in the project task's own scrap-cost reporting rather than silently absorbed into the task's good-output cost figure.
WHY_IT_MATTERS: >
  Absorbing the scrapped share into good-output cost would inflate the reported cost of the material the project actually still has, while hiding the true cost of what was lost.
DISCONFIRMING_OBSERVATION: >
  A project task's scrap-cost reporting for a scrapped, landed-cost-bearing item shows no landed cost share, while its good-output cost figure appears inflated by that same amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Scrap a portion of production output that carries an applied landed cost share, destined for a project task, and check whether the task's scrap-cost reporting reflects that share.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q013

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q013
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Changing a landed cost's allocation basis after the manufactured item it targets has already been issued to a project task does not retroactively rewrite that task's already-recognized cost without a deliberate, separate revaluation step.
WHY_IT_MATTERS: >
  An unintended retroactive rewrite would change a previously reported project task cost with no one having decided to revalue it.
DISCONFIRMING_OBSERVATION: >
  Changing a landed cost's allocation basis after issue to a project task silently alters the task's already-recognized cost with no deliberate revaluation step having been taken.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Issue a landed-cost-bearing manufactured item to a project task, change the landed cost's allocation basis afterward, and check whether the task's already-recognized cost changes.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q014

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q014
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where two separate landed cost documents target the same manufactured batch — one applied before and one after a project task consumes from it — the task's total recognized cost reflects both allocations rather than only the one that existed at the moment of consumption.
WHY_IT_MATTERS: >
  Reflecting only the first allocation would leave the project task's cost permanently missing a charge that legitimately applies to material it already consumed.
DISCONFIRMING_OBSERVATION: >
  A project task's total recognized cost includes only the landed cost document applied before its consumption, with no update once a second landed cost document targeting the same batch is applied afterward.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a first landed cost to a manufactured batch, consume part of it into a project task, apply a second landed cost to the same batch afterward, and check whether the task's cost reflects both.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q015

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q015
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a production order's output is split between a portion issued to a project task and a portion sold externally, a landed cost applied afterward allocates its share to each portion according to the treatment appropriate to it — asset-side for the project-held portion, cost-of-sale-side for the sold portion — rather than treating both portions identically.
WHY_IT_MATTERS: >
  Treating both portions identically would misstate either the project's own asset cost or the cost of goods already sold, depending on which one absorbed the wrong treatment.
DISCONFIRMING_OBSERVATION: >
  A landed cost applied to a split batch allocates its share using the same treatment for both the project-held portion and the externally sold portion, rather than distinguishing asset-side from cost-of-sale-side treatment.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split one production order's output between a project task and an external sale, apply a landed cost to the batch afterward, and check whether each portion receives its appropriate treatment.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q016

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q016
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a still-draft landed cost document that targeted a receipt underlying a production order whose output was already issued to a project task leaves that task's already-recognized material cost completely untouched.
WHY_IT_MATTERS: >
  A residual effect from a cancelled draft would let a charge that was never actually applied still influence the project task's reported cost.
DISCONFIRMING_OBSERVATION: >
  Cancelling a still-draft landed cost document changes the recognized material cost of a project task whose material it targeted, even though the document was never applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a draft landed cost targeting a receipt underlying material already issued to a project task, cancel the draft, and check whether the task's recognized cost is affected.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q017

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q017
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where every unit of a manufactured batch has already been fully consumed by a project task by the time a landed cost targeting that batch arrives, the entire allocation is recognized as an adjustment against the project task's own already-recognized cost rather than failing outright for lack of any remaining on-hand unit to absorb it.
WHY_IT_MATTERS: >
  Failing outright would leave a real charge with nowhere to go, even though the project task that actually consumed the material is fully identifiable.
DISCONFIRMING_OBSERVATION: >
  A landed cost targeting a batch that a project task has already fully consumed fails to apply at all, rather than posting as an adjustment against that task's already-recognized cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Fully consume a manufactured batch into a project task, then apply a landed cost targeting that same batch, and check whether it posts as a project-side cost adjustment or fails outright.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q018

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q018
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A residual amount left over when a landed cost's allocation basis does not divide evenly across several project tasks drawing from the same manufactured batch is assigned to a specific, identifiable task rather than silently disappearing from the total allocated.
WHY_IT_MATTERS: >
  A disappearing residual would mean the sum of what the project tasks show no longer equals the landed cost document's own total charge.
DISCONFIRMING_OBSERVATION: >
  The sum of the recognized cost shares across all project tasks drawing from a landed-cost-bearing batch is less than the landed cost document's own total charge, with no task shown as holding the residual.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed cost that does not divide evenly across several project tasks drawing from the same batch, and check whether the residual is assigned to an identifiable task.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q019

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q019
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A project task's recognized material cost can be decomposed to show which landed cost documents, if any, contributed to it, distinct from the underlying production order's own base cost.
WHY_IT_MATTERS: >
  Without that decomposition, no one reviewing the task's cost could tell how much of it came from the production itself versus from charges added afterward.
DISCONFIRMING_OBSERVATION: >
  A project task's recognized material cost presents only a single combined figure, with no way to identify which landed cost documents, if any, contributed to it versus the base production cost.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Apply a landed cost to a production order feeding a project task, and check whether the task's cost detail can be decomposed into its base production cost and its landed cost contribution.
```

## G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q020

```yaml
QID: G12-PROJECT_MRP_STOCK_LANDED_COSTS-Q020
MODULE: project_mrp_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-3
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A landed cost discovered only during reconciliation of a project task's cost after the project has already closed, and dated inside an accounting period that has since been locked, posts through one documented rule for which period actually receives it relative to the project's own closed figures.
WHY_IT_MATTERS: >
  An undocumented outcome would leave the reversal either invisible against the closed project or improperly reopening records that were already locked.
DISCONFIRMING_OBSERVATION: >
  A landed cost discovered after project closure, dated within an already-locked period, either fails to post anywhere against the project's closed figures, or silently reopens the locked period with no documented rule governing which happens.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Close a project and lock its accounting period, then discover and attempt to apply a landed cost dated within that locked period against one of its already-closed tasks, and check where it posts.
```

## ARITY EXHAUSTION STATEMENT — the 48 floor is NOT met by this bank

Actual count: 20. Shortfall: 28 short of the 48 floor. Reported honestly per
GMVQ_BRIDGE_MODULE_RULE_V1.00 §7 and GMVQ_AUTHORING_STANDARD_V1.00 §2 rather than closed with
manufactured questions. This is the group's own stated expectation for this module —
GROUP_BRIEF_G12_PROJECT.md flags `project_mrp_stock_landed_costs` by name as "4-way: project+mrp+
stock+landed-cost valuation" under "HIGH ARITY-EXHAUSTION RISK, apply the seam-only test strictly, do
not force 48" — and the honest count landed at the low end of that expectation.

Reasoning: a genuine four-participant seam here requires that a project task's own material cost view
be the thing that can disagree with the manufacturing-plus-landed-cost combination underneath it. That
is a narrow intersection. This bank's 20 questions work the seam dimensions in
GMVQ_BRIDGE_MODULE_RULE_V1.00 §3 that survive the four-participant removal test — ORDERING/TIMING
(landed cost arriving after project issue, two landed costs before and after consumption, discovery
after project closure against a locked period), PARTIALITY (batch split between project-held and
externally sold portions, uneven allocation residual across several tasks, merged lots with differing
originating landed costs), OWNERSHIP (three-company attribution, cost decomposition traceability),
REVERSAL (unbuild/reversal propagation across both cost portions, return-to-stock full-value credit,
cancelled draft leaving no residual effect), QUANTITY AND MONEY (three-currency conversion
consistency, full-consumption edge case with no on-hand unit remaining, per-component reconciliation
of a total), and LIFECYCLE MISMATCH (closed task with a late-arriving landed cost, project closed with
a partially-posted landed cost, scrap carrying its own landed cost share). Each dimension is
represented at least once; several genuinely only support one honest question at this arity before
further variants would either restate an already-covered failure event with a noun swapped, or quietly
drop the project-task participant and become a `stock_landed_costs` or `mrp_landed_costs` question in
disguise.

Candidate ground that was considered and REJECTED because it duplicates a HYPOTHESIS already on disk
in a lower-arity sibling (checked per §5 against `grep -h 'HYPOTHESIS'` on
`G05_INVENTORY/G05_STOCK_LANDED_COSTS_GMVQ_MVQ_50_V1.00_DRAFT.md` and
`G06_MANUFACTURING/G06_MRP_LANDED_COSTS_GMVQ_MVQ_48_V1.00_DRAFT.md` before authoring):
- Allocation-basis mechanics in general (value versus weight versus quantity producing a different
  per-unit result), permission to apply a landed cost distinct from permission to draft one, a
  negative/rebate landed cost using the same posting mechanism as a positive one, and a landed cost
  requiring a confirmed receipt before it can apply — all already `stock_landed_costs`'s own ground
  with no project task changing the answer, and were not re-asked here with a project task silently
  attached but playing no real role in the failure.
- A later-arriving cost restated against already-sold or already-scrapped output in general, and
  whether a downstream restatement links back to its triggering allocation in the retained trail —
  already `mrp_landed_costs`'s own ground; kept here only in the one place a project task specifically
  is what receives or loses that restatement (Q002, Q012), not as a general re-ask of the mechanism.
- "a project's total manufacturing cost reconciles to the sum of its components' costs" with no
  landed cost involved at all — that is `project_mrp_account`'s ground (already authored in this
  group) and does not belong in a bank whose whole reason for existing is the landed cost leg.

Candidate ground REJECTED as belonging to a different module or arity, not this bridge:
- A landed cost's interaction with a customer order's revenue recognition or invoiced price would add
  a fifth participant (a funding sale) that this module does not have; that ground, where it exists at
  all, belongs to a sale-side bridge, not here.
- A project task's own scheduling or delivery-commitment consequence of a landed-cost-driven cost
  change is a scope/schedule question, not a cost-view question; the bridge test applied here (does it
  fail only when the project's material COST view, manufacturing, stock movement, AND landed cost are
  all four present?) answers NO for a scheduling framing, so it was left as `project_mrp` or
  `project_mrp_sale` ground rather than kept here.
