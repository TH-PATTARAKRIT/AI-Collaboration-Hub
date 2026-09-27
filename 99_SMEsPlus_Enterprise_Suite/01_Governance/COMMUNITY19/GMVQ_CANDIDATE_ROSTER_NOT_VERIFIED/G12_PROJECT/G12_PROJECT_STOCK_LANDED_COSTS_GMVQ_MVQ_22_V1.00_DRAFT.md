# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_stock_landed_costs Module Bridge MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_STOCK_LANDED_COSTS-MVQ22-V1.00
**Group:** G12 PROJECT
**Module Metadata:** `project_stock_landed_costs`
**Wave:** W3 (GMVQ 25-Team Acceleration, 2026-09-27)
**Author Cell:** P12-5 (GMVQ Question Factory — Production Cell P12-5)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 22
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 22 = 77
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `project_stock_landed_costs`, a three-participant
seam (project material consumption + physical stock receipt + landed-cost valuation, e.g. freight,
duty or insurance allocated onto a receipt) flagged in GROUP_BRIEF_G12_PROJECT.md as HIGH
ARITY-EXHAUSTION RISK. Per the group brief's own scoping of this pair against the sibling
`project_mrp_stock_landed_costs` bank, **manufacturing is explicitly out of scope here** — this bank
covers only the direct receipt-to-project-issue chain, with no work order in between. It is also kept
distinct from the sibling `project_stock_account` bank in this same group: that bank owns the general
ledger-posting seam for a project's own stock consumption; this bank owns specifically the additional
cost layer that a landed-cost allocation attaches to material before or after a project consumes it.

## Control

**Arity owned: THREE-PARTICIPANT (project consumption + stock receipt + landed-cost valuation), with
manufacturing explicitly OUT of scope.**

- Per GMVQ_BRIDGE_MODULE_RULE_V1.00 §5, this bank's own sibling, `project_stock_account`, was authored
  in the same session; every question below was checked against that bank's HYPOTHESIS lines to keep
  the two banks asking about a different seam (general ledger cost posting vs. the landed-cost
  allocation layer specifically) rather than restating the same ground with a different label.
- Every question passed the three-participant removal test: if this were project + stock issue with
  no landed cost ever allocated, or stock + landed-cost allocation with no project ever consuming the
  material, would the question still be meaningful? Only NO on both counts was kept.
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: these 22 questions test 22 distinct material seam hypotheses. See the ARITY EXHAUSTION
  STATEMENT below for why the authoring pass honestly stopped short of the 48-question floor.
- Question text is source-neutral: no vendor or product name, no technical identifier, and the
  module's own metadata name never appears outside the `MODULE:` field.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## ARITY EXHAUSTION STATEMENT — the 48 floor is NOT reached by this bank

22 material seam questions are authored below, 26 short of the 48-question floor. This shortfall is
reported honestly per the no-padding rule rather than closed with manufactured questions.

Reasoning: the genuine seam ground unique to `project_stock_landed_costs` is narrow by construction.
It is not "how landed costs are allocated" in general (a pure stock/accounting question, owned by a
base costing bank, not this bridge) and not "how a project's stock consumption posts to the ledger"
in general (owned by the sibling `project_stock_account` bank in this same group). What remains is
specifically the interaction of landed-cost timing, proration and reversal with a project's own
consumption of the receipt the landed cost attaches to. That intersection was worked across ordering
(cost known before/after issue), partiality (a receipt split across projects, or split between
issued and remaining stock), ownership (which register is authoritative when landed cost and project
consumption disagree), timing (provisional vs. settled cost), reversal (bill cancellation, vendor
credit, return to supplier), quantity and money (allocation basis, over/under absorption,
multi-currency), lifecycle mismatch (a closed project, a closed lot) and authority (who may
reallocate). Each of these axes is represented at least once; further candidates repeated an axis
already covered by a different triggering event, or required manufacturing to remain meaningful and
so belong to `project_mrp_stock_landed_costs` instead, or required no project participation at all
and so belong to a base landed-cost bank.

Candidate ground that was considered and REJECTED because it requires manufacturing to remain
meaningful, and so belongs to the sibling `project_mrp_stock_landed_costs` bank per
GROUP_BRIEF_G12_PROJECT.md's own scoping of this pair:
- a landed cost allocated to raw material that is then consumed by a manufacturing order before
  reaching the project — this pulls in a work-order stage that does not exist in a direct
  receipt-to-project chain.

Candidate ground that was considered and REJECTED because it is a pure ledger-posting question with
no landed-cost dimension, and so belongs to the sibling `project_stock_account` bank instead:
- whether a project's total cost report agrees with the ledger's total posted cost for that project
  in general — already the specific subject of that bank's own reconciliation question.
- whether transferring material between two internal projects splits cost correctly — already that
  bank's own question, with no landed-cost dimension added by repeating it here.

## G12-PROJECT_STOCK_LANDED_COSTS-Q001

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q001
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Material issued to a project from a receipt that carried an allocated landed cost has that landed
  cost's proportional share included in the project's recognized material cost, not just the
  material's own base purchase price.
WHY_IT_MATTERS: >
  Omitting the landed-cost share would understate the project's true material cost by the full amount
  of freight, duty or similar charges actually incurred to bring the material in.
DISCONFIRMING_OBSERVATION: >
  The project's recognized cost for the issued material equals only the base purchase price, with no
  share of the receipt's allocated landed cost included.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Allocate a landed cost to a receipt, issue part of that receipt to a project, and check whether the
  project's recognized cost includes a proportional landed-cost share.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q002

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q002
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A landed cost that arrives and is recorded after material from the same receipt has already been
  issued and costed to a project results in a documented adjustment to that project's recognized
  cost, rather than the late-arriving charge being applied only to the material remaining in stock.
WHY_IT_MATTERS: >
  Applying the late charge only to remaining stock would leave the project permanently understated
  for material it already consumed from the same shipment.
DISCONFIRMING_OBSERVATION: >
  After the late landed cost is recorded, the project's already-posted cost for the previously issued
  material is unchanged and no separate adjustment is posted for it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue material to a project, then record a landed cost against the same receipt afterward, and
  check whether the project's cost reflects an adjustment for its share.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q003

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q003
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a single receipt's landed cost is allocated across material drawn by several different
  projects, each project's share of the allocated cost is proportional to what that project actually
  consumed from the receipt, rather than an equal split regardless of quantity.
WHY_IT_MATTERS: >
  An equal split regardless of quantity would misstate the true cost for every project except the one
  that happened to draw the average share.
DISCONFIRMING_OBSERVATION: >
  Two projects drawing materially different quantities from the same receipt are shown carrying an
  identical landed-cost share.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Have two projects draw different quantities from a single receipt carrying an allocated landed
  cost, and compare each project's resulting landed-cost share.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q004

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q004
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Where a landed cost is configured to allocate by a basis other than value, such as weight or
  volume, a project's attributed share reflects that configured basis rather than always falling
  back to a value-proportional split regardless of what was configured.
WHY_IT_MATTERS: >
  Silently ignoring the configured basis would allocate cost using an assumption the business
  explicitly chose not to use.
DISCONFIRMING_OBSERVATION: >
  A landed cost configured to allocate by weight or volume still shows the project's share computed
  proportionally to value instead.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a landed cost to allocate by a basis other than value on a receipt where the project's
  share by that basis differs from its share by value, and check which basis the resulting project
  cost actually reflects.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q005

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q005
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Returning material to the supplier after it was issued to a project with an allocated landed-cost
  share already included reverses both the base cost and the landed-cost share together, not the
  base cost alone.
WHY_IT_MATTERS: >
  Reversing only the base cost would leave the project overstated by the landed-cost share of
  material it no longer actually holds.
DISCONFIRMING_OBSERVATION: >
  The reversal for the returned material removes only the base cost from the project's figure,
  leaving the landed-cost share still posted.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue landed-cost-inclusive material to a project, return it to the supplier, and check whether
  both the base cost and the landed-cost share are reversed from the project's figure.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q006

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q006
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Material issued and costed to a project before the landed-cost invoice for its receipt has been
  finalized uses a documented provisional figure that is corrected once the landed cost settles,
  rather than a final-looking figure that never reconciles with the settled amount.
WHY_IT_MATTERS: >
  An unreconciled provisional figure would leave the project's cost permanently disconnected from
  the true, eventually-known landed cost.
DISCONFIRMING_OBSERVATION: >
  Once the landed-cost invoice settles at a different amount than assumed, the project's earlier
  posted cost is never corrected to reflect it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue material to a project before its receipt's landed cost is finalized, later finalize the
  landed cost at a different amount, and check whether the project's cost is corrected.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q007

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q007
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a single receipt accumulates more than one separate landed-cost charge over time, such as a
  freight bill followed later by a separate duty bill, a project's cost reflects each charge as it is
  recorded, without a later charge overwriting the share already attributed from an earlier one.
WHY_IT_MATTERS: >
  An overwrite would silently erase a cost the project had already correctly been attributed for a
  different charge on the same receipt.
DISCONFIRMING_OBSERVATION: >
  Recording the second landed-cost charge on the receipt replaces the project's previously attributed
  share from the first charge rather than adding to it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record two separate landed-cost charges on the same receipt at different times after material was
  issued to a project, and check whether the project's cost reflects both.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q008

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q008
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where only part of a landed-cost-bearing receipt has been issued to a project and the rest remains
  in stock, the allocated landed cost is split between the issued portion attributed to the project
  and the remaining portion still carried as stock valuation.
WHY_IT_MATTERS: >
  Attributing the full landed cost to only one of the two portions would either overstate the
  project's cost or understate the remaining stock's valuation.
DISCONFIRMING_OBSERVATION: >
  The full landed cost is attributed entirely to the project's issued portion, or entirely to the
  remaining stock, rather than split between the two.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue part of a landed-cost-bearing receipt to a project, leave the rest in stock, and check how
  the landed cost is split between the two.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q009

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q009
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a landed-cost bill after its share was already attributed to a project's recognized
  material cost decreases that project's cost correspondingly rather than leaving the cancelled
  charge's share permanently embedded in the project's figure.
WHY_IT_MATTERS: >
  A permanently embedded cancelled charge would overstate the project's true material cost
  indefinitely.
DISCONFIRMING_OBSERVATION: >
  After the landed-cost bill is cancelled, the project's recognized cost still includes the share
  originally attributed from it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attribute a landed-cost share to a project's material cost, cancel the underlying landed-cost bill,
  and check whether the project's cost decreases accordingly.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q010

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q010
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where a landed-cost bill's currency differs from the project's own cost-tracking currency, the
  project's attributed share uses one documented, consistent conversion rate and moment rather than
  differing between two separate views of the same charge.
WHY_IT_MATTERS: >
  Inconsistent conversion would make the project's attributed landed-cost share numerically
  unreliable.
DISCONFIRMING_OBSERVATION: >
  Two different views of the same project's landed-cost share, expressed in the two currencies
  involved, use different conversion rates or moments.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a landed-cost bill in a currency different from the project's own cost-tracking currency and
  compare two views of the resulting attributed share.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q011

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q011
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Writing off or scrapping material previously issued to a project that included an allocated
  landed-cost share includes that landed-cost share in the write-off value, not just the material's
  base cost.
WHY_IT_MATTERS: >
  Excluding the landed-cost share from the write-off would leave part of a genuinely lost value
  unaccounted for.
DISCONFIRMING_OBSERVATION: >
  The write-off value recorded for the lost material equals only its base cost, excluding the
  landed-cost share it carried.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Write off landed-cost-inclusive material previously issued to a project and check whether the
  write-off value includes the landed-cost share.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q012

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q012
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where a receipt carrying a landed cost is received into one company and issued to a project
  belonging to a different company, the landed-cost share attributed to the project's cost is
  accompanied by any required inter-company transaction, rather than crossing the company boundary
  with no corresponding entry.
WHY_IT_MATTERS: >
  A missing inter-company entry would leave the receiving entity's books recognizing a cost with no
  matching transaction on the entity that actually incurred the landed charge.
DISCONFIRMING_OBSERVATION: >
  The project's company recognizes the landed-cost share with no corresponding inter-company entry
  on the entity that received the goods and incurred the charge.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  In a multi-company setup, issue landed-cost-bearing material received in one company to a project
  in another, and check whether an inter-company entry accompanies the attributed share.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q013

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q013
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Changing the landed-cost allocation basis after some projects have already consumed material
  costed under the previous basis does not retroactively recompute those already-posted project
  costs without a deliberate revaluation step.
WHY_IT_MATTERS: >
  An unintended retroactive recompute would silently change a previously reported project cost with
  no one having decided to revalue it.
DISCONFIRMING_OBSERVATION: >
  Changing the allocation basis silently changes an already-posted project cost figure with no
  deliberate revaluation step taken.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Post a project's cost under one landed-cost allocation basis, change the basis afterward, and check
  whether the already-posted project cost changes.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q014

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q014
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a landed-cost bill's amount does not match the quantity or value actually received on the
  receipt it is applied to, the resulting over- or under-absorbed amount is reconciled through a
  documented process, rather than silently distorting every project that drew from that receipt with
  no visibility into the discrepancy.
WHY_IT_MATTERS: >
  An unreconciled discrepancy would leave every project sharing that receipt with a materially wrong
  cost figure and no way to know why.
DISCONFIRMING_OBSERVATION: >
  A landed-cost bill that does not match the receipt it is applied to produces distorted project
  costs with no reconciliation record identifying the over- or under-absorbed amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a landed-cost bill whose amount does not match the receipt it covers, issue material to a
  project from it, and check whether the resulting discrepancy is reconciled and disclosed.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q015

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q015
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project archived while a landed cost is still pending allocation against material it has already
  consumed does not leave that pending cost permanently stranded with no documented process ever
  attributing it.
WHY_IT_MATTERS: >
  A permanently stranded pending cost would leave a real charge with nowhere to land once its
  intended project is no longer active.
DISCONFIRMING_OBSERVATION: >
  Archiving the project leaves the pending landed cost unattributed indefinitely with no documented
  process addressing it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Have a landed cost still pending allocation against material already consumed by a project, archive
  the project, and check whether any process addresses the pending cost afterward.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q016

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q016
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A landed cost recorded against a lot that a project has already fully consumed, with that lot's own
  record subsequently closed, can still be attributed back to the project that historically consumed
  it rather than becoming unattributable once the lot is closed.
WHY_IT_MATTERS: >
  An unattributable late charge would leave a real cost with no project to book it against, even
  though the consuming project is a matter of historical record.
DISCONFIRMING_OBSERVATION: >
  A landed cost recorded after the lot's record is closed cannot be attributed to the project that
  historically consumed that lot.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Fully consume and close a lot against a project, then record a landed cost against that lot
  afterward, and check whether it can still be attributed to the consuming project.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q017

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q017
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two projects drawing from the same landed-cost-bearing receipt, one before the landed cost settles
  and one after, are shown with a documented, consistent cost basis for the physically identical
  material rather than two silently different, unreconciled cost bases for the same batch.
WHY_IT_MATTERS: >
  Two silently different cost bases for physically identical material would make it impossible to
  compare the two projects' true material cost.
DISCONFIRMING_OBSERVATION: >
  The two projects show materially different cost bases for the same physical batch with no
  documented reconciliation explaining the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Have one project draw from a receipt before its landed cost settles and a second project draw from
  the same receipt after settlement, and compare the two resulting cost bases.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q018

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q018
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A vendor credit or rebate related to a landed cost, received after a project already consumed
  material under the original higher cost, results in a documented adjustment to the project's
  recognized cost rather than the credit being absorbed with no effect on the project figure at all.
WHY_IT_MATTERS: >
  An unreflected credit would leave the project permanently overstated relative to the true net cost
  actually incurred.
DISCONFIRMING_OBSERVATION: >
  A landed-cost vendor credit received after project consumption has no effect on the project's
  recognized cost figure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive a vendor credit related to a landed cost already attributed to a project's consumed
  material and check whether the project's cost figure is adjusted.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q019

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q019
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Reallocating a landed cost already attributed to one or more projects requires a permission level
  distinct from ordinary material-issue permission, so that a user without that specific authority
  cannot silently change how much landed cost a project carries.
WHY_IT_MATTERS: >
  Allowing an ordinary issue-level user to reallocate landed cost would let project cost figures be
  altered by someone without the authority to make that financial decision.
DISCONFIRMING_OBSERVATION: >
  A user holding only ordinary material-issue permission is able to reallocate a landed cost already
  attributed to a project.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to reallocate an already-attributed landed cost as a user with only ordinary material-issue
  permission and check whether the action is permitted.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q020

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q020
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A partial credit note against a landed-cost bill, issued after a project already consumed material
  costed under the original full amount, is applied proportionally to that project's attributed
  share rather than either ignored or applied as a full reversal that overcorrects the project's
  cost.
WHY_IT_MATTERS: >
  Ignoring the partial credit would overstate the project's true cost; overcorrecting with a full
  reversal would understate it.
DISCONFIRMING_OBSERVATION: >
  A partial credit note against the landed-cost bill produces either no change to the project's cost
  or a full reversal of the entire original landed-cost share, rather than a proportional
  correction.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue a partial credit note against a landed-cost bill already attributed to a project's consumed
  material and check how the correction is applied to the project's cost.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q021

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q021
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where material queued for issue to more than one project has a materially different volume-to-value
  ratio between the projects, switching the landed-cost allocation basis between one project's issue
  and the next does not happen silently within the life of a single receipt.
WHY_IT_MATTERS: >
  A silent basis switch mid-receipt would let two projects drawing from the identical receipt be
  costed under two different, undocumented allocation rules.
DISCONFIRMING_OBSERVATION: >
  Two projects drawing from the same receipt show their landed-cost shares computed under two
  different allocation bases with no documented reason for the switch.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Issue material from one receipt to two projects with materially different volume-to-value ratios
  and check whether both projects' shares are computed under the same allocation basis.
```

## G12-PROJECT_STOCK_LANDED_COSTS-Q022

```yaml
QID: G12-PROJECT_STOCK_LANDED_COSTS-Q022
MODULE: project_stock_landed_costs
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A landed cost recorded against a receipt after the project that consumed material from it has
  already reached a fully closed state posts to a documented destination rather than being silently
  dropped with no record of the attempted attribution.
WHY_IT_MATTERS: >
  A silently dropped late cost would leave a real financial charge with no trace of ever having been
  processed.
DISCONFIRMING_OBSERVATION: >
  Recording the landed cost after the consuming project's closure either fails silently or leaves no
  retrievable record of where, if anywhere, the cost was posted.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Fully close a project that already consumed material from a receipt, then record a landed cost
  against that receipt afterward, and check where, if anywhere, the cost posts.
```
