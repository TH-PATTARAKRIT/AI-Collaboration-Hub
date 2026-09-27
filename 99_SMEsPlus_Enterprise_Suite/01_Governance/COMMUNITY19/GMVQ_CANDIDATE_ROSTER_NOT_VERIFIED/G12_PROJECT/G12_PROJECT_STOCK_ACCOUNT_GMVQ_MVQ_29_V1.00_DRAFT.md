# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_stock_account Module Bridge MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_STOCK_ACCOUNT-MVQ29-V1.00
**Group:** G12 PROJECT
**Module Metadata:** `project_stock_account`
**Wave:** W3 (GMVQ 25-Team Acceleration, 2026-09-27)
**Author Cell:** P12-5 (GMVQ Question Factory — Production Cell P12-5)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 29
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 29 = 84
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `project_stock_account`, a three-participant seam
(project cost tracking + physical stock movement + ledger posting) flagged in
GROUP_BRIEF_G12_PROJECT.md as HIGH ARITY-EXHAUSTION RISK. The seam owned by this module is the
recognition of physical material movement as a cost against a project's own internal cost tracking
in the ledger, with **no funding customer order in the picture at all** — that order-and-revenue
case belongs to the already-authored `sale_project_stock_account` bank (G08) and to the
`sale_project_stock` bank, and per GROUP_BRIEF_G12_PROJECT.md's known duplicate-risk pairs, this bank
must ask a materially different seam question than either: internal budget/cost-centre attribution
and ledger posting for a project's own material consumption, not order-revenue matching.

## Control

**Arity owned: THREE-PARTICIPANT (project cost tracking + stock movement + ledger posting), with a
funding customer order explicitly OUT of scope for this bank.**

- Per GMVQ_BRIDGE_MODULE_RULE_V1.00 §5, the HYPOTHESIS lines of the sibling `sale_project_stock` and
  `sale_project_stock_account` banks (G08) were read before authoring. Every question below was
  checked against both: a question meaningful only because a funding order and its revenue exist was
  rejected as belonging to those banks, not this one.
- Every question passed the three-participant removal test: if this were project + stock issue with
  no ledger posting involved, or stock + ledger posting with no project cost tracking involved, would
  the question still be meaningful? Only NO on both counts was kept.
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: these 29 questions test 29 distinct material seam hypotheses. Per
  GMVQ_BRIDGE_MODULE_RULE_V1.00 §7 and GMVQ_AUTHORING_STANDARD_V1.00 §2, the authoring pass was
  stopped honestly below the 48 floor once further candidate questions were found, on the
  three-participant removal test, to require a funding order to remain meaningful (belonging to G08)
  or to be a pure stock-valuation question with no project cost-tracking dimension at all. See the
  ARITY EXHAUSTION STATEMENT below.
- Question text is source-neutral: no vendor or product name, no technical identifier, and the
  module's own metadata name never appears outside the `MODULE:` field.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## ARITY EXHAUSTION STATEMENT — the 48 floor is NOT reached by this bank

29 material seam questions are authored below, 19 short of the 48-question floor. This shortfall is
reported honestly per the no-padding rule rather than closed with manufactured questions.

Reasoning: `project_stock_account`'s genuine seam ground — cost of a physical stock movement being
attributed and posted against a project's own internal cost tracking, with no funding order and no
revenue side at all — is narrower than the four-participant `sale_project_stock_account` seam, which
additionally has order revenue, invoicing, order currency and order-side cancellation as separate
axes to interact with. Removing the order and revenue axis removes a large share of the ordering,
timing and reversal ground that made the G08 bank's seam rich. What remains here is real and
material (internal budget attribution, cost-centre reassignment, multi-company internal issue,
project archival/deletion against a posted entry, valuation-method consistency, permission boundary
on cost visibility) but was exhausted at 29 distinct, non-duplicative questions.

Candidate ground that was considered and REJECTED because it requires a funding order to remain
meaningful, and so belongs to the `sale_project_stock_account` (G08) bank, not this one, per the
known duplicate-risk pair in GROUP_BRIEF_G12_PROJECT.md:
- margin computed by pairing an invoiced price against recognized material cost — no order, no
  invoice, no margin concept exists in this bank's scope.
- revenue recognized ahead of, or behind, material cost at a milestone — no milestone revenue exists
  without a funding order.
- prepayment recognized ahead of material issue — prepayment is an order-side concept.

Candidate ground that was considered and REJECTED because it is a pure stock-valuation question with
no project cost-tracking dimension, and so belongs to a stock/accounting base bank, not this bridge:
- how a valuation layer is computed for a stock item in general, independent of which project (if
  any) consumed it.
- how a landed cost is allocated across a receipt — this is the distinct seam owned by the sibling
  `project_stock_landed_costs` bank, per GROUP_BRIEF_G12_PROJECT.md's own scoping of that pair.

## G12-PROJECT_STOCK_ACCOUNT-Q001

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q001
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Material issued from stock to a project posts a cost specifically attributed to that project's own
  internal cost tracking, rather than only to a generic warehouse consumption account with no
  project-level attribution at all.
WHY_IT_MATTERS: >
  Without project-level attribution, a project's true internal cost could never be assembled from the
  ledger, defeating the purpose of tracking project cost at all.
DISCONFIRMING_OBSERVATION: >
  Material issued to a named project posts only to a generic consumption account with no reference
  identifying which project actually consumed it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue material from stock to a specific project and check whether the resulting ledger posting
  carries a reference to that specific project.
```

## G12-PROJECT_STOCK_ACCOUNT-Q002

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q002
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Returning material to stock from a project reverses the previously posted cost against that same
  project's cost tracking, rather than leaving the original charge standing alongside an unrelated,
  unattributed credit.
WHY_IT_MATTERS: >
  A standing charge with an unattributed credit would overstate the project's true net material cost
  indefinitely.
DISCONFIRMING_OBSERVATION: >
  After the return, the project's cost tracking still shows the full original charge with no
  corresponding reversal linked to it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue material to a project, post its cost, return the material to stock, and check whether the
  project's cost tracking reflects a reversal.
```

## G12-PROJECT_STOCK_ACCOUNT-Q003

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q003
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a project carries a defined budget ceiling, cost postings from stock consumption are
  reflected against that budget's tracked consumption, so that exceeding the ceiling is at least
  detectable rather than invisible until a manual, unrelated review.
WHY_IT_MATTERS: >
  An invisible overrun would let a project's actual material spend exceed its approved budget with no
  built-in signal to anyone responsible for it.
DISCONFIRMING_OBSERVATION: >
  Posting cost that pushes the project past its defined budget ceiling produces no detectable change
  in any budget-consumption figure associated with that project.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Set a budget ceiling for a project, issue material that pushes posted cost past that ceiling, and
  check whether the budget-consumption figure reflects it.
```

## G12-PROJECT_STOCK_ACCOUNT-Q004

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q004
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Transferring material directly from one internal project to another attributes the cost removal to
  the originating project and the cost addition to the receiving project, without either double
  posting the cost to both or dropping it from both.
WHY_IT_MATTERS: >
  Double posting or dropping the cost would misstate one or both projects' true material cost after
  what is meant to be a neutral transfer between them.
DISCONFIRMING_OBSERVATION: >
  After an internal project-to-project transfer, either both projects show the cost, or neither does.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Transfer material directly from one project's consumption to another's and check the resulting cost
  postings on both projects.
```

## G12-PROJECT_STOCK_ACCOUNT-Q005

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q005
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project archived while still carrying unconsumed material cost posted against it does not leave
  that posted value stranded with no documented process ever addressing it.
WHY_IT_MATTERS: >
  A stranded value would overstate an asset or cost figure tied to a project no longer actively
  tracked.
DISCONFIRMING_OBSERVATION: >
  Archiving the project leaves its posted unconsumed material cost open indefinitely with no
  documented process that ever closes or addresses it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post unconsumed material cost against a project, archive the project, and check whether any
  process addresses the outstanding posted value.
```

## G12-PROJECT_STOCK_ACCOUNT-Q006

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q006
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Changing a project's assigned internal cost-tracking category after material cost has already been
  posted against it under the previous category does not silently reattribute the historical posting
  to the new category without a deliberate reclassification step.
WHY_IT_MATTERS: >
  A silent retroactive reattribution would misrepresent under which category the cost was actually
  incurred at the time.
DISCONFIRMING_OBSERVATION: >
  Changing the project's cost-tracking category changes the category shown on an already-posted
  historical entry with no deliberate reclassification action taken.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Post material cost against a project under one cost-tracking category, change the project's
  category, and check whether the historical posting's category changes.
```

## G12-PROJECT_STOCK_ACCOUNT-Q007

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q007
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where a project belongs to one company entity and the warehouse fulfilling its material issue
  belongs to another, cost recognition against the project posts with any required inter-company
  transaction generated alongside it, rather than posting to the project's company alone with no
  corresponding entry on the supplying entity.
WHY_IT_MATTERS: >
  A missing inter-company entry would leave the supplying entity's books with no record of goods it
  actually released.
DISCONFIRMING_OBSERVATION: >
  Material cost is recognized against the project's company with no corresponding inter-company
  transaction on the entity that actually supplied the goods.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  In a multi-company setup, issue material from a warehouse in one company to a project belonging to
  another, and check whether an inter-company entry accompanies the cost posting.
```

## G12-PROJECT_STOCK_ACCOUNT-Q008

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q008
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Issuing material to a project before its receipt has been formally recorded uses a documented
  provisional cost value that is later corrected once the receipt is confirmed, rather than an
  unexplained final value that never reconciles with the actual received cost.
WHY_IT_MATTERS: >
  An unreconciled provisional value would leave the project's cost figure permanently disconnected
  from the material's actual cost.
DISCONFIRMING_OBSERVATION: >
  The provisional cost posted before receipt confirmation is never corrected once the actual receipt
  cost becomes known.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue material to a project ahead of its formal receipt confirmation, later confirm the receipt at
  a different cost, and check whether the project's posted cost is corrected.
```

## G12-PROJECT_STOCK_ACCOUNT-Q009

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q009
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Deleting a material issue transaction that was already posted to a project's cost tracking removes
  or reverses the associated ledger entry consistently, rather than leaving a posted entry with no
  remaining source transaction to explain it.
WHY_IT_MATTERS: >
  An orphaned posted entry with no source transaction would break the traceability the ledger is
  supposed to provide.
DISCONFIRMING_OBSERVATION: >
  Deleting the source issue transaction leaves its posted ledger entry intact with no remaining
  reference explaining where it came from.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post cost from a material issue to a project, delete the source issue transaction where permitted,
  and check the resulting state of the posted ledger entry.
```

## G12-PROJECT_STOCK_ACCOUNT-Q010

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q010
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project's own cost report, showing total material cost consumed, agrees with the ledger's own
  total of postings attributed to that project when both are compared for the same period.
WHY_IT_MATTERS: >
  Two disagreeing totals for the same project would make it impossible to know the project's actual
  material cost with any confidence.
DISCONFIRMING_OBSERVATION: >
  The project's own cost report total and the ledger's total of postings attributed to that project,
  for the same period, do not match.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Generate a project's cost report for a period and independently total the ledger's postings
  attributed to that project for the same period, then compare the two.
```

## G12-PROJECT_STOCK_ACCOUNT-Q011

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q011
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Issuing the same material lot concurrently to two different projects splits both the physical
  quantity and its posted cost correctly between the two, without one project's posting silently
  absorbing the other's share.
WHY_IT_MATTERS: >
  One project silently absorbing the other's share would misstate both projects' true material cost
  for the same physical event.
DISCONFIRMING_OBSERVATION: >
  Concurrent issue of one lot to two projects results in the full cost posted against only one of the
  two projects.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue portions of the same material lot to two different projects at the same time and check the
  cost posted against each.
```

## G12-PROJECT_STOCK_ACCOUNT-Q012

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q012
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: LOW
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Reassigning a project's manager or owner does not alter the historical cost postings already made
  against that project under the previous manager.
WHY_IT_MATTERS: >
  Historical postings changing purely because of an administrative reassignment would corrupt the
  cost record's integrity for no operational reason.
DISCONFIRMING_OBSERVATION: >
  Reassigning the project's manager changes the value or attribution of an already-posted historical
  cost entry.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post cost against a project, reassign its manager, and compare the historical postings before and
  after the reassignment.
```

## G12-PROJECT_STOCK_ACCOUNT-Q013

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q013
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a project has sub-projects, the parent project's rolled-up material cost figure equals the
  sum of each sub-project's own posted cost, without double-counting cost that is also posted
  directly against the parent.
WHY_IT_MATTERS: >
  Double-counting at roll-up would overstate the parent project's true total material cost.
DISCONFIRMING_OBSERVATION: >
  The parent project's rolled-up cost figure exceeds the sum of its sub-projects' individually
  posted costs plus any cost posted directly against the parent itself.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post material cost against two sub-projects and against their shared parent project directly, then
  compare the parent's rolled-up figure against the sum of the parts.
```

## G12-PROJECT_STOCK_ACCOUNT-Q014

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q014
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where a project's internal budget is tracked in a different currency than the stock valuation's
  reporting currency, the posted cost figure uses one documented, consistent conversion rate and
  moment across both views.
WHY_IT_MATTERS: >
  Inconsistent conversion between the two views would make the project's own posted cost numerically
  unreliable.
DISCONFIRMING_OBSERVATION: >
  The project's budget-currency view and the ledger's reporting-currency view of the same posted
  cost use different conversion rates or moments.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a project whose budget currency differs from the stock valuation's reporting currency, post
  a material cost, and compare the two currency views of that same cost.
```

## G12-PROJECT_STOCK_ACCOUNT-Q015

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q015
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A negative-stock issue to a project, where the physical quantity is recorded before its own
  formal valuation is known, results in the project's posted cost being corrected once that
  valuation resolves, rather than remaining at whatever provisional figure was first used.
WHY_IT_MATTERS: >
  A permanently uncorrected provisional figure would leave the project's cost figure disconnected
  from the material's real, eventually-known cost.
DISCONFIRMING_OBSERVATION: >
  After the material's valuation resolves, the project's earlier posted provisional cost for the
  negative-stock issue remains unchanged.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue material to a project as a negative-stock movement ahead of its valuation being known, allow
  the valuation to resolve, and check whether the project's posted cost is corrected.
```

## G12-PROJECT_STOCK_ACCOUNT-Q016

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q016
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A change to an item's standard cost after material at the prior standard was already issued and
  posted to a project does not retroactively restate that project's already-posted cost without a
  deliberate revaluation step.
WHY_IT_MATTERS: >
  An unintended retroactive restatement would silently change a project's previously reported cost
  with no one having decided to revalue it.
DISCONFIRMING_OBSERVATION: >
  A later standard-cost change silently alters the project's already-posted cost for material issued
  under the prior standard, with no deliberate revaluation step taken.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Post material cost to a project at a given standard cost, change the item's standard cost
  afterward, and check whether the project's already-posted cost changes.
```

## G12-PROJECT_STOCK_ACCOUNT-Q017

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q017
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Scrapping or writing off material previously issued and posted to a project posts to a
  distinguishable write-off account rather than being folded silently into the project's ordinary
  consumption cost with no visible distinction.
WHY_IT_MATTERS: >
  An indistinguishable write-off would hide the true reason and magnitude of loss from anyone
  reviewing the project's cost.
DISCONFIRMING_OBSERVATION: >
  A write-off of previously issued project material posts to the exact same account as ordinary
  consumption, with no distinguishing marker anywhere.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Write off material previously issued and posted to a project, and check whether the write-off
  posts to a distinguishable account from ordinary consumption.
```

## G12-PROJECT_STOCK_ACCOUNT-Q018

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q018
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A project's real-time cost figure, viewed mid-period before any period-end posting batch has run,
  is either kept consistent with what the period-end batch will later post, or is clearly marked as
  provisional, rather than presenting a silently final-looking number that later changes without
  explanation.
WHY_IT_MATTERS: >
  A silently final-looking provisional number would mislead anyone making a decision based on it
  before period-end processing has actually occurred.
DISCONFIRMING_OBSERVATION: >
  The mid-period figure is presented with no provisional marking and later changes once period-end
  processing runs, with no indication beforehand that this could happen.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  View a project's cost figure mid-period before period-end processing runs, then compare it to the
  figure after processing completes.
```

## G12-PROJECT_STOCK_ACCOUNT-Q019

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q019
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A project team member permitted to request material issue for a project but not permitted to view
  accounting figures cannot see the posted monetary cost value through the material issue
  interaction itself.
WHY_IT_MATTERS: >
  Leaking the monetary cost value through the issue flow would bypass the accounting visibility
  restriction entirely.
DISCONFIRMING_OBSERVATION: >
  A user without accounting-view permission can see the posted monetary cost value while requesting
  or confirming a material issue for a project.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Grant a user permission to request material issue without accounting-view permission, have them
  perform the issue, and check whether any monetary cost value is visible to them.
```

## G12-PROJECT_STOCK_ACCOUNT-Q020

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q020
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Deleting a project entirely, rather than archiving it, while its material cost postings still exist
  in the ledger leaves those postings intact and referenced, rather than orphaned or silently reversed
  as an unintended side effect of the project's deletion.
WHY_IT_MATTERS: >
  A silently reversed or orphaned posting would corrupt the ledger's historical cost record with no
  one having decided to change it.
DISCONFIRMING_OBSERVATION: >
  Deleting the project either leaves its posted cost entries with a broken reference, or silently
  reverses them as a side effect of the deletion.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Where project deletion is permitted, delete a project whose material cost was already posted to
  the ledger, and check the state of those posted entries afterward.
```

## G12-PROJECT_STOCK_ACCOUNT-Q021

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q021
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project put on hold after material cost was already posted against it does not continue
  accruing further period-end costing activity as though work were still active.
WHY_IT_MATTERS: >
  Continued accrual against a paused project would overstate cost incurred for work that is not
  actually progressing.
DISCONFIRMING_OBSERVATION: >
  A paused project continues to accrue period-end cost activity identical to an active project, with
  no distinction.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Put a project on hold after cost has been posted against it, run a period-end process, and check
  whether cost continues accruing against it.
```

## G12-PROJECT_STOCK_ACCOUNT-Q022

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q022
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Correcting a misissue of material that was wrongly attributed to the wrong project corrects both
  the originally-charged project's posted cost and the correctly-intended project's posted cost
  together, not leaving one corrected while the other still reflects the error.
WHY_IT_MATTERS: >
  Fixing only one side would leave one project's cost figure still reflecting an error the other
  project's books no longer show.
DISCONFIRMING_OBSERVATION: >
  Correcting the misissue updates one project's posted cost but leaves the other still reflecting
  the original error.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Correct a material misissue that was wrongly attributed to one project instead of another, and
  check whether both projects' posted cost figures reflect the correction.
```

## G12-PROJECT_STOCK_ACCOUNT-Q023

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q023
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A return of material to stock from a project after the accounting period in which it was issued
  has already closed posts through a documented rule for which period receives the reversal.
WHY_IT_MATTERS: >
  An undocumented outcome would leave the reversal either invisible or improperly reopening a closed
  accounting period.
DISCONFIRMING_OBSERVATION: >
  A return after the issuing period's close either fails to post anywhere or silently reopens the
  closed period.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Close the accounting period in which material was issued to a project, then return that material,
  and check which period the reversal posts to.
```

## G12-PROJECT_STOCK_ACCOUNT-Q024

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q024
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Two projects drawing material from a single shared delivery split the resulting cost-of-goods
  figure between them according to what each actually consumed, rather than one project absorbing
  the full delivery cost.
WHY_IT_MATTERS: >
  One project absorbing the full cost would understate that project's margin against budget and
  overstate the other's.
DISCONFIRMING_OBSERVATION: >
  The full cost of a shared delivery drawn on by two projects is posted entirely to one project's
  cost figure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Have two projects draw material from a single shared delivery and check how the resulting cost is
  split between them.
```

## G12-PROJECT_STOCK_ACCOUNT-Q025

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q025
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A partial delivery physically diverted to a different project than originally intended after
  leaving the warehouse has its ledger cost attribution follow the actual physical diversion, not
  remain attached to the originally intended project.
WHY_IT_MATTERS: >
  Cost attribution disagreeing with physical reality would misstate both projects' true material
  cost.
DISCONFIRMING_OBSERVATION: >
  The ledger's cost attribution for the diverted goods still shows the originally intended project as
  the cost bearer even though the goods were physically diverted elsewhere.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Divert a partial delivery to a different project after it leaves the warehouse and check which
  project the ledger actually attributes the cost to.
```

## G12-PROJECT_STOCK_ACCOUNT-Q026

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q026
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Two similarly configured projects issuing comparable material consistently recognize the cost at
  the same point in the process — at issue or at some other defined moment — rather than one
  recognizing at issue and the other at a materially different point with no configuration
  difference explaining it.
WHY_IT_MATTERS: >
  An unexplained difference in recognition timing between similar projects would make cost
  recognition unpredictable and hard to audit.
DISCONFIRMING_OBSERVATION: >
  Two similarly configured projects recognize comparable material cost at materially different
  points in the process with no configuration difference explaining why.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Compare the cost-recognition timing of two similarly configured projects issuing comparable
  material and check whether any configuration difference explains a difference found.
```

## G12-PROJECT_STOCK_ACCOUNT-Q027

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q027
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A project spanning a fiscal year boundary, with part of its material cost posted in one year and
  part in the next, shows that split visibly in its own cost reporting rather than smoothing it into
  one undifferentiated total.
WHY_IT_MATTERS: >
  A silently smoothed split would hide a real cross-year timing difference that period-based
  financial reporting is supposed to disclose.
DISCONFIRMING_OBSERVATION: >
  The project's cost report for a period spanning the fiscal year boundary presents one blended
  figure with no visible split between the two fiscal years.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a project's material cost across a fiscal year boundary and check whether the project's cost
  report shows the split by year.
```

## G12-PROJECT_STOCK_ACCOUNT-Q028

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q028
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where one project's material is costed under two different valuation methods for two different
  batches, the project's combined cost figure keeps each batch's own basis separable rather than
  blending both into one figure that cannot be broken back down.
WHY_IT_MATTERS: >
  A blended, non-separable figure would make it impossible to tell which batch actually drove the
  project's cost.
DISCONFIRMING_OBSERVATION: >
  The project's combined cost figure blends two differently-valued batches into one figure that
  cannot be separated back into each batch's own basis.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue two batches costed under two different valuation methods to the same project and check
  whether the combined cost figure can be separated back into each batch's own basis.
```

## G12-PROJECT_STOCK_ACCOUNT-Q029

```yaml
QID: G12-PROJECT_STOCK_ACCOUNT-Q029
MODULE: project_stock_account
TYPE: MODULE
AUTHOR: P12-5
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project's period-end cost reconciliation between its own cost-tracking total and the ledger's
  posted total, when a gap is found, treats one documented register as authoritative rather than two
  reconciliation views producing two different closing figures.
WHY_IT_MATTERS: >
  Two disagreeing closing figures would make it impossible to know the project's actual final
  material cost.
DISCONFIRMING_OBSERVATION: >
  Two different reconciliation views of the same project, run for the same period, produce different
  closing cost figures because they treat different registers as authoritative.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a reconciliation gap between a project's own cost tracking and the ledger's posted total,
  then compare the closing figure produced by two different reconciliation views.
```
