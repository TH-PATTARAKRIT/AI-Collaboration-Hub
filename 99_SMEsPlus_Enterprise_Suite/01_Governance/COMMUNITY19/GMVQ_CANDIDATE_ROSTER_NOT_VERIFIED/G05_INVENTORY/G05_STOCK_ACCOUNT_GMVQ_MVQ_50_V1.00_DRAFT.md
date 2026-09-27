# G05 INVENTORY — stock_account — Module Verification Questions (MVQ)

**Document ID:** GMVQ-W2-P02-G05-STOCK_ACCOUNT-V1.00-DRAFT
**Group:** G05 INVENTORY
**Wave:** W2
**Author Cell:** P02
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN

## Module Metadata
- **Module (metadata name):** `stock_account`
- **Role in group:** SEAM — physical movement to ledger entry (movement -> accounting)
- **Base module:** `stock`
- **actual_mvq_count:** 50
- **Standard bank reference:** 55 (shared, authored separately; not reproduced here)
- **Research depth (55 + actual_mvq):** 105

## Purpose
Module-specific research questions (MVQ) for the blind two-lane ROOM A study of `stock_account`.
Lane A (source reading) and Lane B (runtime observation only) each answer every question below
independently, joined on QID. Every question in this bank targets the seam this module exists to
cover, per the GMVQ Bridge Module Rule V1.00: if the accounting capability were removed and stock movements and the ledger were used entirely apart, the question would no longer make sense; every question here fails only at the moment a movement becomes a posted value.

## Control
- Directive: SMEPLUS-GMVQ-25TEAM-ACCELERATION-20260927-001
- Governed by: GMVQ_AUTHORING_STANDARD_V1.00.md, GMVQ_BRIDGE_MODULE_RULE_V1.00.md
- Clean Room: no vendor or reference source tree; generic ERP domain knowledge only; no technical
  identifiers (model/table/field/method names, XML IDs, API paths) in question text; no vendor or
  product names.
- Closed vocabularies enforced: RISK_TIER in {CRITICAL, HIGH, MEDIUM};
  OUTPUT_CLASS in {BUSINESS INVARIANT, RISK, BEHAVIOUR, CONFIGURATION, BOUNDARY}.
- This document is DRAFT question content only. Not approved, not frozen, not verified,
  not MASTER-ready. No merge, release, or gate closure is authorized by this file.

---


```yaml
QID: G05-STOCK_ACCOUNT-Q001
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The unit cost used to value an outbound movement is fixed at the costing method's value as of the moment the movement is validated, not recalculated later even if the inputs that would feed the running cost change afterward.
WHY_IT_MATTERS: >
  If the value can drift after the fact, every downstream margin, inventory asset and cost-of-sale figure derived from that movement becomes unreliable and unauditable.
DISCONFIRMING_OBSERVATION: >
  An outbound movement's posted value changes when a later inbound movement alters the running cost that would have applied at the moment of validation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Validate an outbound movement, record its posted value, then validate an inbound movement at a different cost, and re-check the first movement's posted value.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q002
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The accounting period a valuation entry lands in is governed by the date the movement is validated, not by any date typed on the originating document.
WHY_IT_MATTERS: >
  If period placement can be driven by an editable document date rather than the actual event date, period-end figures can be manipulated after the fact without an operational event to justify the shift.
DISCONFIRMING_OBSERVATION: >
  Two movements validated on the same calendar day, but originating from documents dated in different fiscal periods, post their valuation entries to different accounting periods.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create two receipt documents dated in different fiscal periods, validate both movements on the same day, and compare which period each valuation entry lands in.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q003
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A receipt movement creates an offsetting position in an interim clearing account that remains open until the corresponding bill is matched, and that position is observable before any bill exists.
WHY_IT_MATTERS: >
  If the interim position is invisible until a bill appears, there is no way to detect goods received but not yet billed, which is exactly the exposure the clearing account exists to surface.
DISCONFIRMING_OBSERVATION: >
  No interim position is visible for a receipt movement made before any bill is created, or a position only appears after the bill posts.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Validate a receipt with no bill yet recorded against it, then inspect the accounts affected by that movement.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q004
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a receipt movement is later invoiced at a different quantity or unit cost than what was physically received, the interim clearing position leaves a residual balance that persists rather than automatically netting to zero.
WHY_IT_MATTERS: >
  An interim account that always nets to zero regardless of a receipt/bill mismatch would be hiding exactly the discrepancies it is meant to expose, defeating its purpose as a control account.
DISCONFIRMING_OBSERVATION: >
  The interim clearing account nets to exactly zero after a bill is recorded for a different quantity or price than was received, with no residual visible anywhere.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Receive a quantity, then record a bill against that receipt for a different quantity or unit price, and inspect the interim account balance afterward.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q005
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A movement validated near a period boundary can have its valuation entry land in a different accounting period than the movement's own recorded date, when process timing decouples the two.
WHY_IT_MATTERS: >
  Silent period drift between the physical event and its accounting recognition is exactly the mismatch that makes reconciliation between operations and finance unreliable.
DISCONFIRMING_OBSERVATION: >
  The valuation entry's period always exactly matches the movement's own recorded date, with no observable exception under any timing condition tested.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Validate a movement dated at the very edge of a period boundary under conditions that delay processing, and compare the movement date to the entry's period.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q006
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A manual revaluation of on-hand stock changes the carrying value only of units still on hand and does not retroactively alter the cost already recognized for units that had already left stock before the revaluation.
WHY_IT_MATTERS: >
  Retroactively rewriting the cost of goods that already left would misstate a prior period's already-closed cost of sale and break any reconciliation performed against that period.
DISCONFIRMING_OBSERVATION: >
  A revaluation event changes the previously posted value of a movement that had already left stock before the revaluation was performed.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Sell part of a receipt's quantity, then trigger a manual revaluation on the remaining stock, and check whether the already-posted sale movement's value changed.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q007
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Switching the configured valuation method while cost layers already exist does not retroactively recompute the value of layers created under the previous method.
WHY_IT_MATTERS: >
  Silent retroactive recomputation on a pure configuration change, with no new movement, would let a setting change alone rewrite historical financial figures.
DISCONFIRMING_OBSERVATION: >
  Historical valuation entries change value, or the running valuation total shifts, purely because the configured method was changed with no new movement recorded.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Record several movements under one valuation method, change the configured method, and check whether prior entries or the running total shifted with no new movement.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q008
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reversing a movement whose valuation entry has already posted creates a new compensating entry rather than deleting or rewriting the original entry.
WHY_IT_MATTERS: >
  Editing a posted entry in place destroys the audit trail of what was originally recorded and reported, which is a control failure in any accounting process.
DISCONFIRMING_OBSERVATION: >
  The original valuation entry disappears or is edited in place when the movement it relates to is reversed.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Validate a movement, confirm its valuation entry posted, then reverse the movement and inspect whether the original entry still exists unmodified.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q009
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A movement that drives on-hand quantity negative is still valued and posted using the same costing rule as a movement leaving positive stock, without a distinct placeholder value standing in for an unknown cost.
WHY_IT_MATTERS: >
  If negative-stock movements post no value or a visibly different kind of value, the total carrying value of inventory becomes internally inconsistent and cannot be trusted until corrected.
DISCONFIRMING_OBSERVATION: >
  A movement that drives stock negative posts no valuation entry at all, or posts one using a value visibly different in kind from the normal costing rule, such as zero or an unflagged placeholder.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue an outbound movement for a quantity greater than what is on hand, and inspect the valuation entry it produces.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q010
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A scrap movement produces a valuation entry that removes the value of the scrapped quantity from the asset position, distinct in kind from the entry an ordinary sale movement would produce.
WHY_IT_MATTERS: >
  If scrap posts identically to a sale, the loss is being recorded as if it generated revenue-matched cost of sale rather than as a write-off, misstating both figures.
DISCONFIRMING_OBSERVATION: >
  Scrapping a quantity leaves the carrying value of on-hand stock unchanged, or produces an entry identical to what a normal sale movement would produce.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Scrap a quantity of stock and compare the resulting valuation entry to the entry a normal outbound sale of the same quantity would produce.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q011
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An inventory count adjustment that changes recorded quantity with no corresponding movement document still produces a valuation entry whenever the counted quantity differs from the system quantity.
WHY_IT_MATTERS: >
  A quantity correction with no accompanying valuation entry would leave the physical count and the ledger silently out of step, undermining the reason a perpetual valuation system exists.
DISCONFIRMING_OBSERVATION: >
  Recording a different counted quantity changes the on-hand quantity but produces no valuation entry, leaving the ledger and the physical count out of step with no reconciling record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record an inventory count that differs from the current system quantity and check whether a valuation entry was produced alongside the quantity change.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q012
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A transfer between two locations that both roll up to the same valuation and company scope produces no net valuation entry, only a location-level quantity record.
WHY_IT_MATTERS: >
  Posting a valuation entry for a movement that has no effect on the total asset value would overstate transaction volume in the ledger without a corresponding economic event.
DISCONFIRMING_OBSERVATION: >
  An internal transfer within a single valuation scope produces a valuation entry that changes the total carrying value of stock.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Transfer a quantity between two locations that both belong to the same company and valuation scope, and check whether the total carrying value changed.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q013
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A transfer between locations belonging to different companies produces a valuation entry pair, functioning as an internal sale and purchase rather than a plain relocation.
WHY_IT_MATTERS: >
  Treating a cross-company movement as a costless relocation would let value cross a legal-entity boundary with no accounting recognition on either side, which is a compliance exposure.
DISCONFIRMING_OBSERVATION: >
  A transfer that crosses a company boundary is valued and posted identically to a same-company relocation, with no inter-company entry pair created.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Transfer a quantity from a location owned by one company to a location owned by a different company, and inspect the accounting entries produced on each side.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q014
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the two companies in a cross-company transfer have different configured costing methods, the receiving side values the incoming quantity under its own configured method rather than carrying over the sending side's cost basis unmodified.
WHY_IT_MATTERS: >
  Carrying over a foreign cost basis unmodified would let one company's costing policy override another's, breaking the independence each company's books are supposed to have.
DISCONFIRMING_OBSERVATION: >
  The receiving company's valuation entry uses the exact cost basis from the sending company even though the receiving company's own configured method would produce a different value.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure two companies with different valuation methods, transfer a quantity between them, and compare the receiving side's posted value to what its own method should produce.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q015
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a fractional unit cost multiplied by quantity does not divide evenly into the currency's minor unit, the posted valuation amount is rounded and any residual is absorbed into a single identifiable difference rather than left unposted.
WHY_IT_MATTERS: >
  An unposted rounding residual, repeated across many movements, silently accumulates into a material, unexplained gap between quantity-times-cost and the ledger.
DISCONFIRMING_OBSERVATION: >
  A movement with a non-terminating unit-cost calculation posts an amount differing from quantity times rounded unit cost by more than the smallest currency unit, with no rounding difference recorded anywhere.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct a movement whose quantity and unit cost multiply to a non-terminating decimal amount, validate it, and check the posted amount against the raw calculation.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q016
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the accounting entry for a movement cannot be posted, for example because a required valuation account is not configured, the physical movement itself still completes and is not silently rolled back.
WHY_IT_MATTERS: >
  A movement that silently reverts because its accounting side failed would create an invisible gap between what the warehouse believes happened and what actually happened, with no independent record of the split.
DISCONFIRMING_OBSERVATION: >
  A movement is silently reverted or blocked from completing solely because its accounting counterpart could not be posted, and no independent record distinguishes the physical failure from the financial one.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Remove or misconfigure the valuation account for a product category, attempt to validate a movement in that category, and observe both the physical and accounting outcome.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q017
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Validating a movement dated inside an accounting period that has already been closed produces a hard stop or an automatic redate, rather than a silent post into the closed period.
WHY_IT_MATTERS: >
  A silent post into a closed period would let operational activity alter figures that reviewers and auditors have already treated as final.
DISCONFIRMING_OBSERVATION: >
  A movement dated inside a closed accounting period posts its valuation entry into that closed period with no warning, block, or redirection.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Close an accounting period, then attempt to validate a movement dated inside that period, and observe the system's response.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q018
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Under a layer-based costing method, outbound movements consume existing cost layers in a fixed, deterministic order rather than an order that can vary from run to run.
WHY_IT_MATTERS: >
  A non-deterministic consumption order would make the same sequence of movements produce different valuations on different occasions, which breaks reproducibility of financial results.
DISCONFIRMING_OBSERVATION: >
  Two outbound movements of identical quantity, issued back to back with no intervening receipt, are valued using cost drawn from different layers or in a different order between the two.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive stock in two batches at different costs, then issue two outbound movements back to back, and compare which layer's cost each drew from.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q019
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a movement after its related bill has already posted requires a separate corrective action; the cancellation alone does not automatically reverse or adjust the bill's own accounting.
WHY_IT_MATTERS: >
  An automatic silent edit to an already-posted bill, triggered by an unrelated cancellation elsewhere, would let one action alter financial records without a visible corrective trail.
DISCONFIRMING_OBSERVATION: >
  Cancelling the movement automatically edits or removes the already-posted bill's accounting entry with no separate corrective document created.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Validate a movement, record and post a bill against it, then cancel the movement and inspect whether the bill's own entry changed with no new corrective document.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q020
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a movement's recorded quantity is expressed in a unit different from the unit the valuation method's running cost is tracked in, the value posted is derived using one consistent conversion factor, not two different factors applied separately to the quantity and to the cost.
WHY_IT_MATTERS: >
  Two different conversion factors applied within the same calculation would silently distort the posted value without ever producing an error to flag the inconsistency.
DISCONFIRMING_OBSERVATION: >
  The quantity and the unit cost used within the same valuation entry are converted using inconsistent factors, producing a posted amount that does not equal the converted quantity times the converted unit cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a movement where the transacted unit differs from the unit the running cost is tracked in, and check the posted amount against quantity times unit cost using a single conversion factor.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q021
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Triggering a manual stock revaluation requires a permission distinct from the permission needed to record an ordinary stock movement.
WHY_IT_MATTERS: >
  If ordinary warehouse staff can change carrying values, the control that revaluation is meant to provide over financial figures is defeated.
DISCONFIRMING_OBSERVATION: >
  A user who can validate ordinary movements but has not been granted any accounting-related permission is still able to trigger a manual revaluation.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Grant a user only the permission to record ordinary movements, and attempt to have that user trigger a manual revaluation.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q022
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A manual revaluation leaves a traceable record identifying who performed it, when, and the before and after value, independent of the underlying accounting entry it produced.
WHY_IT_MATTERS: >
  Without an independent trace of who changed a carrying value and by how much, a revaluation cannot be distinguished from an unexplained, unauditable change to the books.
DISCONFIRMING_OBSERVATION: >
  After a revaluation, there is no way to determine who performed it or what the prior carrying value had been, only the new balance.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Trigger a manual revaluation and attempt to reconstruct, from available records, who performed it and what the value was immediately before.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q023
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A movement for a product category with no valuation account configured is blocked from validating rather than posting to a default or unrelated account.
WHY_IT_MATTERS: >
  Falling back to a default or unrelated account would misclassify the value in the ledger in a way that is easy to miss and hard to trace back to its true source.
DISCONFIRMING_OBSERVATION: >
  A movement for an unconfigured product category validates successfully and posts its value to some account other than a configured valuation account, with no warning raised.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Remove the valuation account configuration from a product category, then attempt to validate a movement in that category.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q024
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a movement produces an accounting entry at all is governed by a per-category or per-company configuration, not by a single global all-or-nothing setting.
WHY_IT_MATTERS: >
  A configuration that unexpectedly affects unrelated categories would make valuation behaviour unpredictable across a multi-line-of-business operation sharing one system.
DISCONFIRMING_OBSERVATION: >
  Changing the automated-posting configuration for one product category also changes whether movements in a different, unrelated category produce entries.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Set two product categories to different automated-posting configurations, then move stock in each and compare whether entries were produced.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q025
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two movements for the same product, validated by two different users at effectively the same moment, both receive a deterministic, non-conflicting cost, and neither valuation entry is lost.
WHY_IT_MATTERS: >
  A lost or overwritten valuation entry under concurrent activity would silently understate the ledger with no error to alert anyone that a transaction went unrecorded.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous movements for the same product result in one valuation entry overwriting or clobbering the other, or a running cost that reflects only one of the two.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Have two users validate movements for the same product at effectively the same time, and check that both resulting valuation entries exist and the running cost reflects both.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q026
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Whether two companies share a single running valuation or each maintains its own is a configuration decision, and stock movements between them behave differently depending on which mode is configured.
WHY_IT_MATTERS: >
  Assuming one behaviour regardless of the sharing configuration would make cross-company movement accounting incorrect for whichever mode was not assumed.
DISCONFIRMING_OBSERVATION: >
  A transfer between two companies posts identically regardless of whether they are configured to share or to separate their valuation.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a pair of companies first to share valuation and then to separate it, and compare the posting produced by an identical transfer under each configuration.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q027
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A direct manual change to a product's costing configuration, such as its standard cost, does not by itself retroactively value stock that moved before the change was made.
WHY_IT_MATTERS: >
  Retroactive revaluation triggered by a pure configuration edit, with no explicit revaluation action taken, would let a settings change alone rewrite historical figures without a deliberate step.
DISCONFIRMING_OBSERVATION: >
  Changing a costing configuration value retroactively alters the amount already posted for a movement that occurred before the configuration change.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Record a movement, then change the product's costing configuration value, and check whether the already-posted movement's amount changed.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q028
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reversing an outbound movement restores the returned quantity into current stock at a valuation determined at the time of the reversal, not necessarily the original layer's exact cost if that layer has since been exhausted.
WHY_IT_MATTERS: >
  Assuming the original exact cost is always available ignores that the layer it came from may no longer exist, which would make the reversal's valuation logic unspecified in a common case.
DISCONFIRMING_OBSERVATION: >
  A reversed outbound movement is always reinstated at the exact original cost even when the layer it was drawn from has since been fully consumed by other movements.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Issue an outbound movement, fully consume the layer it drew from with further movements, then reverse the original movement and inspect the cost it is reinstated at.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q029
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A movement's valuation entry posts only once the movement itself reaches a completed state; a movement still in a draft or waiting state produces no accounting entry.
WHY_IT_MATTERS: >
  An accounting entry existing ahead of the physical event it claims to represent would let the books reflect a transaction that has not actually happened yet.
DISCONFIRMING_OBSERVATION: >
  A movement still in a draft or waiting state already has a posted valuation entry associated with it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a movement and leave it in a draft or waiting state without validating it, then check whether any valuation entry already exists for it.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q030
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A movement whose net effect on quantity is zero, such as one fully corrected before completion, produces no valuation entry.
WHY_IT_MATTERS: >
  A non-zero entry for a transaction with no actual quantity effect would introduce a valuation change into the ledger with no corresponding physical event to justify it.
DISCONFIRMING_OBSERVATION: >
  A movement whose net effect on quantity is zero still produces a non-zero valuation entry.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct a movement whose corrections net its quantity effect to zero before completion, and check whether any valuation entry was produced.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q031
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The interim clearing balance is reachable through an ordinary reconciliation or reporting view without requiring direct inspection of raw ledger entries.
WHY_IT_MATTERS: >
  A balance that can only be found by inspecting raw ledger entries is effectively invisible to the people responsible for reconciling receipts against bills day to day.
DISCONFIRMING_OBSERVATION: >
  The interim clearing balance cannot be found anywhere except by inspecting raw ledger entries, with no dedicated reconciliation surface available.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  With an open interim balance present, attempt to find it through the ordinary reporting or reconciliation surfaces before resorting to raw ledger inspection.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q032
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Valuation configuration is scoped at the product-category and company level, not at the level of an individual warehouse or location.
WHY_IT_MATTERS: >
  If valuation could silently differ by warehouse for the same product and company, comparing the same product's cost across locations would be unreliable without knowing which location's setting applied.
DISCONFIRMING_OBSERVATION: >
  Two locations within the same company and category can be configured with different valuation methods for the same product.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Attempt to configure two locations under the same company and product category with different valuation methods, and observe whether the system allows it.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q033
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Under a running-average costing method, the average is recalculated at the moment of each receipt, so an outbound movement immediately following a receipt uses the just-updated average rather than the pre-receipt average.
WHY_IT_MATTERS: >
  Using a stale average would misstate the very next transaction's cost, and any accumulated lag would compound across a busy warehouse day.
DISCONFIRMING_OBSERVATION: >
  An outbound movement immediately following a receipt is valued at the average that existed before that receipt, ignoring the just-posted quantity and cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive a quantity at a cost that changes the running average, immediately issue an outbound movement, and check which average it was valued at.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q034
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Editing the quantity or cost inputs of a movement while it is still in a draft state produces no accounting entry until the movement is validated, and the final entry reflects only the values present at validation.
WHY_IT_MATTERS: >
  An entry that reflects intermediate, later-discarded edits would misstate the transaction actually recorded once the movement is finalized.
DISCONFIRMING_OBSERVATION: >
  An accounting entry exists, or reflects intermediate edited values, for a movement that has not yet been validated.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Edit the quantity or cost of a draft movement several times before validating it, then check whether any entry existed during those edits and whether the final entry matches only the validated values.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q035
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The sum of all valuation entries for a product over a period reconciles to the change in that product's on-hand carrying value over the same period, with no unexplained gap.
WHY_IT_MATTERS: >
  An unreconciled gap between posted entries and the observed change in carrying value means the ledger cannot be trusted to represent the actual asset position.
DISCONFIRMING_OBSERVATION: >
  Summing the period's valuation entries for a product produces a total that does not match the observed change in carrying value, with no reconciling item identified.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Over a defined period, record a mix of movements for one product, then sum the valuation entries and compare the total to the observed change in carrying value.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q036
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Returning received goods to a supplier before any bill has matched the receipt clears the corresponding interim position without leaving a residual balance.
WHY_IT_MATTERS: >
  A residual balance left behind by an unbilled return would misrepresent an open exposure to a bill that will never arrive.
DISCONFIRMING_OBSERVATION: >
  Returning unbilled goods leaves an interim balance for the returned quantity that never clears.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive a quantity with no bill recorded, return that quantity to the supplier, and check whether the interim balance for it cleared.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q037
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A transfer between two locations under one company posts, if it posts at all, in that company's own accounting currency, regardless of any currency associated with the transfer document itself.
WHY_IT_MATTERS: >
  A valuation entry posted in the wrong currency would misstate the company's own books in a way that is easy to overlook until consolidation.
DISCONFIRMING_OBSERVATION: >
  An internal transfer's valuation entry posts in a currency other than the owning company's accounting currency.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Perform an internal transfer using a document expressed in a different currency from the company's accounting currency, and check which currency the posted entry uses.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q038
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a receipt that has already been partially billed is blocked, or requires resolving the billed portion first, rather than silently discarding the billed link.
WHY_IT_MATTERS: >
  Silently discarding a billed link on cancellation would leave a bill pointing at a receipt that, from the receiving side, no longer exists.
DISCONFIRMING_OBSERVATION: >
  A partially billed receipt is cancelled outright with no warning about, or handling of, the already-billed portion.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Partially bill a receipt, then attempt to cancel the receipt and observe whether the system blocks, warns, or silently proceeds.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q039
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A movement of a composite item tracked as a single valued unit is valued as one line, not by summing the independently tracked valuations of components that are not themselves separately stocked.
WHY_IT_MATTERS: >
  Double-valuing a composite item, once as a whole and once through untracked components, would overstate the total asset position for the same physical goods.
DISCONFIRMING_OBSERVATION: >
  The valuation entry for a single tracked composite item's movement shows a value inconsistent with treating it as one line, with no documented component breakdown process behind the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Move a composite item tracked as a single valued unit and inspect whether its valuation entry is consistent with a single-line treatment.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q040
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A product category configured for manual or no automatic valuation produces stock movements with no accounting entries at all, and the system does not silently fall back to posting anyway.
WHY_IT_MATTERS: >
  A silent fallback to automatic posting despite a manual configuration would defeat the deliberate choice to keep that category's valuation outside the automated flow.
DISCONFIRMING_OBSERVATION: >
  A category configured for manual valuation still produces automatic accounting entries for ordinary movements.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a product category for manual valuation, move stock within that category, and check whether any automatic accounting entry was produced.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q041
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to which account a product category's valuation posts to is itself traceable to a user and a timestamp.
WHY_IT_MATTERS: >
  An untraceable change to a valuation account setting would let the destination of future financial postings be redirected with no record of who did it or when.
DISCONFIRMING_OBSERVATION: >
  The valuation account configured for a category can be changed with no record of who made the change or when.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Change the valuation account configured on a product category and then attempt to determine who made the change and when.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q042
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A movement created as part of a customer return is valued using the same costing rule as any other inbound movement, not automatically reinstated at the original outbound sale's cost.
WHY_IT_MATTERS: >
  Reinstating at the original sale cost regardless of what the costing rule would otherwise produce would let a return silently bypass the same valuation logic every other inbound movement is subject to.
DISCONFIRMING_OBSERVATION: >
  A returned-goods movement is valued at the exact cost it was originally sold at rather than under the costing rule currently applicable to inbound movements.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Sell a quantity, change conditions that would affect the running cost, then process a customer return of that quantity and check what cost the return is valued at.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q043
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A product explicitly configured to carry zero value, such as a non-valued consumable, generates movement records for quantity but no valuation entries.
WHY_IT_MATTERS: >
  A non-zero entry for a product explicitly configured as non-valued would contradict the configuration and misstate the asset position with a value the business explicitly chose not to track.
DISCONFIRMING_OBSERVATION: >
  A product configured as non-valued still generates a non-zero valuation entry for its movements.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a product as non-valued, move quantities of it, and check whether any valuation entry was produced.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q044
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A compensating entry created by reversing a posted movement carries a visible link back to the original entry it offsets.
WHY_IT_MATTERS: >
  A compensating entry with no visible link back to its origin is indistinguishable from an unrelated, unexplained posting during a review.
DISCONFIRMING_OBSERVATION: >
  A compensating entry exists with no traceable link back to the original entry, appearing as an unrelated posting.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Reverse a movement whose valuation entry already posted, and inspect whether the resulting compensating entry references the original entry.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q045
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A bill that arrives and would match before its corresponding receipt has been validated is held pending rather than posted against a receipt that does not yet exist.
WHY_IT_MATTERS: >
  Clearing an interim position against a receipt that does not exist yet would produce a reconciliation that has no underlying event to support it.
DISCONFIRMING_OBSERVATION: >
  A bill matches and clears an interim position for a receipt that has not yet been validated.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Record a bill referencing a receipt before that receipt has been validated, and observe whether the interim position clears.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q046
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When configured for periodic rather than perpetual valuation, individual movements do not generate per-movement accounting entries; value is recognized instead through a separate periodic process.
WHY_IT_MATTERS: >
  If per-movement entries still post under periodic configuration, the two valuation modes are not actually distinct, and the periodic process would double up or conflict with movement-level postings.
DISCONFIRMING_OBSERVATION: >
  A system configured for periodic valuation still generates a per-movement accounting entry identical to what perpetual mode would produce.
EXPECTED_SURFACE: S1,S2,S7,S8
PRECONDITIONS: >
  Configure periodic valuation, move stock, and check whether a per-movement accounting entry was produced before any periodic process has run.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q047
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Reversing a movement whose original entry sits in a since-locked fiscal year posts the compensating entry in the current open period rather than reopening the locked year.
WHY_IT_MATTERS: >
  Reopening a locked fiscal year to accommodate a reversal would undermine the entire purpose of locking a year, which is to make its figures immutable once closed.
DISCONFIRMING_OBSERVATION: >
  Reversing an old movement reopens or modifies an entry inside a fiscal year that has been locked.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Lock the fiscal year containing an old movement's entry, then reverse that movement and observe which period the compensating entry lands in.
LAYER: PROCESS
```

```yaml
QID: G05-STOCK_ACCOUNT-Q048
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Every valuation entry the module posts carries a traceable reference back to the specific stock movement that generated it.
WHY_IT_MATTERS: >
  An entry with no traceable origin cannot be explained during a reconciliation or an audit, regardless of whether its amount happens to be correct.
DISCONFIRMING_OBSERVATION: >
  A valuation entry exists that cannot be traced back to any specific stock movement.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Select a sample of posted valuation entries and attempt to trace each one back to the specific movement that generated it.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q049
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Deleting a movement while still in draft also removes any draft accounting entry associated with it, leaving no orphaned entry behind.
WHY_IT_MATTERS: >
  An orphaned draft entry left behind after its movement is deleted would clutter the books with a record that no longer corresponds to anything.
DISCONFIRMING_OBSERVATION: >
  Deleting a draft movement leaves behind a draft accounting entry with no movement left to justify it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a draft movement, note any draft entry associated with it, delete the movement, and check whether the entry still exists.
LAYER: BASE
```

```yaml
QID: G05-STOCK_ACCOUNT-Q050
MODULE: stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a later receipt arrives for a product that had gone negative, the movements that were valued while negative are corrected through an adjusting entry to reflect the true cost once known, rather than left permanently at their original placeholder value.
WHY_IT_MATTERS: >
  Never revisiting a negative-stock valuation once the true cost is known would leave a permanently incorrect cost baked into the books with no mechanism to ever correct it.
DISCONFIRMING_OBSERVATION: >
  Stock that was valued while negative is never revisited or corrected once the offsetting receipt arrives, permanently carrying its original valuation.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Drive a product's stock negative, then receive enough quantity to bring it positive again, and check whether the movements valued while negative were later adjusted.
LAYER: PROCESS
```
