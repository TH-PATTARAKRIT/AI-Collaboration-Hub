# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_project_stock_account Module Bridge MVQ Bank

**Document ID:** GMVQ-G08-SALE_PROJECT_STOCK_ACCOUNT-MVQ28-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_project_stock_account`
**Wave:** W2
**Author Cell:** P-S7 (GMVQ Question Factory — Production Team P-S7)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 28
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 28 = 83
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `sale_project_stock_account`, the four-participant
seam that is the ledger consequence of the order-project-stock triad: material cost recognition
timing against order revenue, work-in-progress and stock valuation double-counting, capitalisation
and write-off on project cancellation, cross-company cost attribution, period-boundary mismatches
between recognized revenue and recognized cost, and reconciliation authority at project closure. Per
the GMVQ Bridge Module Rule V1.00 and this group's own arity discipline, every question here was
authored and then re-audited against the strict four-participant removal test: if a question would
still be fully meaningful for a project that had no funding customer order at all (pure internal
project cost accounting), it does not belong here and was rewritten to bind explicitly to the
order's own revenue, price, currency, company or invoicing behaviour, or was cut. No question here
restates a `sale_project_stock` operational fact without adding the ledger dimension, and no question
restates a pure costing question that a non-project, non-order accounting bank would already ask.

## Control

**Arity owned: FOUR-PARTICIPANT (order + project + physical goods movement + ledger posting) only.**
Every question below requires all four to be present and interacting; a question meaningful for
project + stock + ledger alone, with no funding order in the picture, was excluded during this
authoring pass under the mandatory pre-freeze arity re-check described below.

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: these 28 questions test 28 distinct material seam hypotheses. The authoring pass was
  deliberately stopped short of 48: several additional candidate questions drafted during authoring
  were found, on the four-participant removal test, to be answerable by a project+stock+ledger
  scenario with no order in the picture at all, and were either rewritten to add a genuine order-side
  dependency (revenue recognition, invoiced price, order currency or company) or cut outright rather
  than kept as padding. That self-check, its outcome, and the resulting count are reported honestly
  per the no-padding rule rather than disguised by stretching wording to reach 48.
- Question text is source-neutral: no vendor or product name, no technical identifier, and the
  module's own metadata name never appears outside the `MODULE:` field.
- Every question passed the four-participant bridge removal test before being kept, and was
  cross-checked against the sibling `sale_project` and `sale_project_stock` banks' authored
  HYPOTHESIS lines at authoring time to avoid restating either bank's invariants without the ledger
  dimension.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q001

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q001
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Material issued to a project task funded by a customer order is not carried simultaneously as a cost already matched against that order's recognized revenue and as an asset value still sitting in stock valuation for the same units.
WHY_IT_MATTERS: >
  Double-counting the same units as both a matched cost and a valued asset would misstate both the order's margin and the business's stock position.
DISCONFIRMING_OBSERVATION: >
  The same issued units are shown as cost already matched against the order's recognized revenue while also still carried as an asset in stock valuation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue material from stock to an order-funded project task, recognize the order's associated revenue, and check whether stock valuation still separately carries the same units as an asset.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q002

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q002
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Revenue recognized against a project milestone and the material cost for the work that milestone represents land in the ledger in a way that a margin figure for that milestone can actually be computed, rather than falling into unreconciled periods with no cross-reference.
WHY_IT_MATTERS: >
  An unmatchable revenue and cost pair would make it impossible to know whether a milestone was actually profitable.
DISCONFIRMING_OBSERVATION: >
  A milestone's recognized revenue and its corresponding material cost land in different periods with no reference connecting them for margin calculation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reach a milestone that recognizes revenue in one period while its material was issued and costed in an earlier or later period, and check whether the two can be matched for margin.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q003

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q003
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order whose linked project already has material cost capitalized as work in progress results in a documented disposition of that capitalized cost referenced against the cancellation.
WHY_IT_MATTERS: >
  A stranded capitalized balance with no closing entry would leave the financial statements overstating an asset that no longer corresponds to any live order.
DISCONFIRMING_OBSERVATION: >
  Cancelling the order leaves the project's capitalized work-in-progress cost with no closing entry referencing the cancellation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Capitalize material cost as work in progress for an order-funded project, cancel the order, and check whether that capitalized cost receives a documented closing entry tied to the cancellation.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q004

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q004
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where the order, the project, and the fulfilling warehouse belong to three different company entities, material cost recognition is posted to one documented entity's ledger with any required inter-company transaction generated alongside it.
WHY_IT_MATTERS: >
  A missing inter-company step would leave one entity's books recognizing a cost with no corresponding transaction on the entity that actually supplied the goods.
DISCONFIRMING_OBSERVATION: >
  Material cost is recognized in a company's ledger without the corresponding inter-company transaction that should accompany a cross-entity movement.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  In a three-entity multi-company setup, issue material to a project and check whether cost recognition and any required inter-company entry both occur.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q005

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q005
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A material return from a project site tied to an order, after that order's accounting period has closed, posts through a documented rule for which period receives the reversal against that order's figures.
WHY_IT_MATTERS: >
  An undocumented outcome would leave the reversal either invisible or improperly reopening closed financial records.
DISCONFIRMING_OBSERVATION: >
  A return after the order's period close either fails to post against the order's figures anywhere, or silently reopens the closed period.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Close the accounting period for an order-funded project, then process a material return from its site, and check which period the reversal posts to in relation to that order.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q006

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q006
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A margin figure derived by pairing the order's invoiced price against the ledger's recognized material cost uses the cost figure that actually corresponds to the same units and timing as the invoice.
WHY_IT_MATTERS: >
  Pairing mismatched valuation layers would produce a margin figure that does not describe any transaction that actually happened.
DISCONFIRMING_OBSERVATION: >
  The computed margin pairs the invoiced price with a cost figure drawn from a different valuation layer or period than the units actually invoiced.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Invoice an order line whose underlying material was issued across more than one valuation layer, and check which cost figure the margin calculation actually uses.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q007

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q007
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project milestone invoice raised before the corresponding material has actually been issued from stock is either blocked or flagged in the ledger as revenue recognized ahead of its cost.
WHY_IT_MATTERS: >
  Presenting a margin as complete before the cost side has actually happened would overstate profitability that has not yet been earned.
DISCONFIRMING_OBSERVATION: >
  A milestone invoice raised ahead of material issue shows a margin computed as though the not-yet-incurred cost were already known and complete.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Raise a milestone invoice before the corresponding material has been issued, and check how the margin figure treats the not-yet-incurred cost.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q008

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q008
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Material issued to two tasks under the same order line from two different valuation layers has each task's recognized cost, when matched against that line's revenue, correctly split by the layer that actually supplied it.
WHY_IT_MATTERS: >
  A blended or single-layer cost applied to both tasks would misstate which task actually consumed the more expensive material.
DISCONFIRMING_OBSERVATION: >
  Matching the order's line revenue against its two tasks' costs uses the same blended unit cost for both, rather than each task's own valuation layer.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue material to two tasks under one order line from two different valuation layers, and check how each task's cost is matched against that line's revenue.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q009

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q009
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A project on hold after material cost was recognized against its order does not continue accruing further period-end cost activity matched against that same order's revenue as though work were still active.
WHY_IT_MATTERS: >
  Continued accrual against a paused project would overstate cost incurred against revenue for work that is not actually progressing.
DISCONFIRMING_OBSERVATION: >
  A paused, order-funded project continues to accrue period-end cost matched against its order's revenue identical to an active project, with no distinction.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Put an order-funded project on hold after cost recognition, run a period-end process, and check whether cost continues accruing against that order's revenue.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q010

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q010
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Correcting a misissue of material that was wrongly attributed to a project's order corrects both the project's work-in-progress figure and the order's own cost attribution together.
WHY_IT_MATTERS: >
  Fixing only one side would leave the order's own margin still reflecting an error that the project's own books no longer show, or vice versa.
DISCONFIRMING_OBSERVATION: >
  Correcting a misissue updates the project's work-in-progress figure but leaves the order's cost attribution still reflecting the original error, or vice versa.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Correct a material misissue that was wrongly attributed to a project's order, and check whether both the project's and the order's cost figures reflect the correction.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q011

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q011
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An order that is fully invoiced and closed while its linked project still shows an open work-in-progress balance for materials never actually consumed does not leave that balance stranded with no documented closing process.
WHY_IT_MATTERS: >
  A stranded open balance after the funding order has closed would overstate an asset with no remaining live commercial purpose.
DISCONFIRMING_OBSERVATION: >
  Closing the order leaves the project's unconsumed work-in-progress balance open indefinitely with no documented process ever closing it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Fully invoice and close an order while its project retains an open work-in-progress balance for unconsumed material, and check whether any process addresses that balance.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q012

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q012
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Where the order's currency, the project's internal cost-tracking currency, and the stock valuation's reporting currency all differ, the recognized cost figure uses one documented rate and moment consistently across views.
WHY_IT_MATTERS: >
  Inconsistent conversion between reports of the same transaction would make the recognized cost numerically unreliable.
DISCONFIRMING_OBSERVATION: >
  Two different reports of the same recognized cost, across the three currencies involved, use different conversion rates or moments for the same underlying transaction.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a project whose order currency, cost-tracking currency, and stock reporting currency all differ, and compare the recognized cost figure as shown in two different reports.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q013

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q013
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Material over-issued at a premium beyond an order's priced assumption is recognized as a distinguishable variance against that order's margin, rather than blended into the project's standard cost with no trace.
WHY_IT_MATTERS: >
  An invisible premium would hide the true cost of a shortage-driven decision from whoever reviews the order's profitability.
DISCONFIRMING_OBSERVATION: >
  A premium paid for expedited or substitute material is absorbed into the standard cost figure with no separately visible variance against that order's margin.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue material to an order-funded project at a premium cost above the order's priced assumption, and check whether the order's margin figure shows a distinguishable variance.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q014

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q014
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a project's completion is later revised downward after both its revenue and its material cost were already recognized at the higher completion percentage, the ledger's reversal treats the revenue side and the cost side consistently.
WHY_IT_MATTERS: >
  Reversing only one side would leave a margin figure that no longer corresponds to any real state of the order.
DISCONFIRMING_OBSERVATION: >
  Revising completion downward reverses the previously recognized revenue but leaves the corresponding cost recognition unchanged, or vice versa.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Recognize revenue and cost at a given completion percentage, revise the percentage downward, and check whether both sides of the reversal are treated consistently.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q015

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q015
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A returned item from a project whose funding order is already fully closed, with no open accounting period left for it, posts its credit to a documented destination rather than being silently dropped.
WHY_IT_MATTERS: >
  A silently dropped credit would leave a real physical return with no financial trace at all.
DISCONFIRMING_OBSERVATION: >
  A return against a fully closed, order-funded project with no open period either fails to post anywhere or is silently discarded with no record of the attempted return.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attempt to process a material return against a fully closed, order-funded project with no open accounting period, and check where, if anywhere, the credit posts.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q016

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q016
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where two projects under one order both draw material from a single delivery, the ledger's cost-of-goods figure set against that order's revenue is correctly split between the two projects.
WHY_IT_MATTERS: >
  Attributing the full cost to only one project would understate that project's margin and overstate the other's.
DISCONFIRMING_OBSERVATION: >
  The full cost of a shared delivery drawn on by two projects is attributed entirely to one project's cost figure, leaving the other showing none of its actual share.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Have two projects under one order draw material from a single shared delivery, and check how the resulting cost-of-goods figure is split between them.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q017

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q017
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order after partial material issue and partial milestone invoicing unwinds the recognized revenue and the recognized cost through a documented sequence, not leaving one reversed while the other is not with no plan to complete it.
WHY_IT_MATTERS: >
  A half-completed unwind would leave the ledger in a state that matches neither the pre-cancellation nor the post-cancellation reality.
DISCONFIRMING_OBSERVATION: >
  Cancelling the order leaves the ledger showing the cost reversed but the revenue not, or vice versa, with no documented remaining step to complete the unwind.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel an order after partial material issue and partial milestone invoicing, and check whether the resulting ledger state shows both sides of the unwind addressed.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q018

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q018
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A change to an item's standard cost after material was issued to an order-funded project does not retroactively restate that project's already-recognized cost as matched against the order's revenue, without a deliberate revaluation step.
WHY_IT_MATTERS: >
  An unintended retroactive restatement would change a previously reported margin with no one having decided to revalue it.
DISCONFIRMING_OBSERVATION: >
  A later standard-cost change silently alters a project's already-recognized cost figure, matched against its order's revenue, with no deliberate revaluation step having been taken.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Change an item's standard cost after material was already issued to an order-funded project at the prior standard, and check whether the project's already-recognized cost figure changes.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q019

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q019
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Attribution of material cost recognition, when the order's fulfilling warehouse belongs to a different company than the receiving project and the inter-company transaction for the goods has not yet posted, does not let the receiving side recognize a cost against the project ahead of that inter-company step.
WHY_IT_MATTERS: >
  Recognizing the cost early would let one entity's books claim an expense before the entities involved have actually formalized the transaction between them.
DISCONFIRMING_OBSERVATION: >
  The project's company recognizes a material cost before the corresponding inter-company transaction for that movement has actually been posted.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  In a cross-company setup, issue material to a project ahead of posting the inter-company transaction, and check whether the receiving side already shows a recognized cost.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q020

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q020
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A material return mid-period, after the project's milestone revenue for that period already assumed the material stayed consumed, results in the ledger's revenue figure being adjusted to reflect the returned, now-unconsumed material.
WHY_IT_MATTERS: >
  Leaving the revenue figure unchanged would recognize income for material the customer's project no longer actually holds.
DISCONFIRMING_OBSERVATION: >
  A mid-period return of material previously assumed consumed for milestone revenue has no effect at all on the already-recognized revenue figure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Recognize milestone revenue assuming material stays consumed, then return that material mid-period, and check whether the recognized revenue figure adjusts.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q021

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q021
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Whether material cost is recognized at the moment of issue to the project or only at the moment the customer is invoiced under the order is one documented, consistently applied rule across similar projects.
WHY_IT_MATTERS: >
  An unexplained difference in timing between similar projects would make cost recognition unpredictable and hard to audit.
DISCONFIRMING_OBSERVATION: >
  Two similarly configured projects recognize material cost at different moments, one at issue and one at invoicing, with no configuration difference explaining why.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Compare the cost-recognition timing of two similarly configured projects, one where material was issued well before invoicing and one where it was issued near invoicing.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q022

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q022
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where the order allows billing ahead of delivery while material has not yet been issued to the project, the ledger does not recognize any material cost against that prepaid revenue until the material is actually issued.
WHY_IT_MATTERS: >
  Pairing a prepayment with a cost that has not actually been incurred would present a margin as complete before any work happened.
DISCONFIRMING_OBSERVATION: >
  A prepayment recognized as revenue is immediately paired with a recognized material cost before any material has actually been issued to the project.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Recognize a prepayment on an order ahead of material issue to its project, and check whether any material cost is recognized against it before issue actually occurs.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q023

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q023
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A write-off of obsolete material originally issued to a now-abandoned, order-funded project posts to a single documented account, and does not silently change that order's own recognized margin without a documented rule that it should.
WHY_IT_MATTERS: >
  An unexplained change to a closed order's margin figure would make historical profitability reporting unreliable.
DISCONFIRMING_OBSERVATION: >
  A write-off for an abandoned project changes its originating order's recognized margin with no documented rule stating that write-offs affect order margin this way.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Write off material from an abandoned, order-funded project, and check whether that order's own recognized margin figure changes as a result.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q024

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q024
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  At project closure, reconciling the order's total invoiced amount against the project's total recognized cost uses one documented register as authoritative when a gap is found.
WHY_IT_MATTERS: >
  Two reconciliation views producing two different closing figures would make it impossible to know the project's actual final result.
DISCONFIRMING_OBSERVATION: >
  Two different closure reconciliation reports for the same project produce different closing figures because they treat different registers as authoritative.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a reconciliation gap between an order's invoiced total and a project's recognized cost, close the project, and compare the closing figure from two different reconciliation views.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q025

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q025
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A project spanning a fiscal year boundary, with material cost recognized in one year and the order's corresponding milestone revenue recognized in the next, shows that one-period mismatch visibly rather than smoothing it away.
WHY_IT_MATTERS: >
  A silently smoothed mismatch would hide a real timing difference that financial reporting is supposed to disclose.
DISCONFIRMING_OBSERVATION: >
  The cross-year mismatch between a project's recognized cost and its order's recognized revenue is smoothed away by an unexplained adjustment rather than shown as the actual timing difference it is.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Recognize a project's material cost in one fiscal year and its milestone revenue in the next, and check whether the resulting period mismatch is visible or silently adjusted away.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q026

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q026
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A partial delivery diverted to a different project than originally intended after leaving the warehouse has its ledger cost attribution follow the actual physical diversion, not remain attached to the originally intended project.
WHY_IT_MATTERS: >
  Cost attribution disagreeing with physical reality would misstate both projects' true margins.
DISCONFIRMING_OBSERVATION: >
  The ledger's cost attribution for diverted goods still shows the originally intended project as the cost bearer even though the goods were physically diverted elsewhere.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Divert a partial delivery to a different project after it leaves the warehouse, and check which project's cost the ledger actually attributes it to.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q027

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q027
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where one order funds two projects whose materials are costed under two different valuation methods, the order's combined margin figure correctly separates each project's true cost basis rather than blending the two into one indistinguishable figure.
WHY_IT_MATTERS: >
  A blended figure would make it impossible to tell which of the two projects was actually more profitable.
DISCONFIRMING_OBSERVATION: >
  The order's combined margin figure blends two projects' differently-valued costs into one figure that cannot be separated back into each project's true basis.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Fund two projects costed under two different valuation methods from one order, and check whether the order's combined margin figure can be separated back into each project's own basis.
```

## G08-SALE_PROJECT_STOCK_ACCOUNT-Q028

```yaml
QID: G08-SALE_PROJECT_STOCK_ACCOUNT-Q028
MODULE: sale_project_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Deleting a project whose material cost has already been posted to the ledger against its funding order leaves that posted entry intact and correctly referenced, rather than orphaned or silently reversed as a side effect of the deletion.
WHY_IT_MATTERS: >
  A silently reversed or orphaned posting would corrupt the order's own historical cost record with no one having decided to change it.
DISCONFIRMING_OBSERVATION: >
  Deleting the project either leaves its posted cost entry with a broken reference, or silently reverses that entry as an unintended side effect of the deletion.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Where project deletion is permitted, delete a project whose material cost was already posted to the ledger against its funding order, and check the state of that posted entry afterward.
```
