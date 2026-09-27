# SMEsPlus ENTERPRISE SUITE
## GMVQ — G03 MASTER_DATA / product_matrix Module Adversarial MVQ Bank

**Document ID:** GMVQ-G03-PRODUCT_MATRIX-MVQ48-V1.00  
**Group:** G03 MASTER_DATA  
**Module Metadata:** `product_matrix`  
**Wave:** W1  
**Author Cell:** TEAM 18 (GMVQ Question Factory — Primary MVQ Authoring)  
**Review Cell:** PENDING  
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN  
**actual_mvq_count:** 48  
**Standard bank reference:** 55 (shared, not reproduced here)  
**Research depth:** 55 + 48 = 103  
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded  

## Purpose

This bank authors the module-specific MVQ set for `product_matrix` — grid entry of attribute
combinations onto a transaction line. It targets: the grid inventing lines for combinations
that do not exist as sellable records; precedence between grid quantities and existing manually
entered lines; reopening the grid on a document that was manually edited afterward; the effect of
later changes to the attribute master (rename, deactivate, delete, reorder, add) on already
grid-created lines; pricing and tax resolution per combination; the grid bypassing validations
that ordinary line entry enforces; permission to create a new combination during entry;
concurrency between two users on the same document; and the auditability of bulk-created lines.

The question text is source-neutral and does not expose vendor model names, field names, methods,
schema, XML IDs, API shapes, or implementation algorithms. `MODULE: product_matrix` appears only
in the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 48 questions exist because they test 48 distinct material hypotheses.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## G03-PRODUCT_MATRIX-Q001

```yaml
QID: G03-PRODUCT_MATRIX-Q001
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The grid entry mechanism must only create lines for attribute combinations that exist as valid
  sellable records, not synthesize a line for a combination that has never been defined as one.
WHY_IT_MATTERS: >
  An invented combination bypasses whatever process defines what is actually sellable, letting the
  grid transact something the business never approved.
DISCONFIRMING_OBSERVATION: >
  Entering values in the grid produces a transaction line for a combination that does not exist as
  a defined sellable record anywhere else in the system.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Use the grid to enter a combination of attribute values that has deliberately not been set up as
  a sellable variant beforehand.
```

## G03-PRODUCT_MATRIX-Q002

```yaml
QID: G03-PRODUCT_MATRIX-Q002
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A combination that has been deactivated or marked unavailable must be excluded from the grid
  identically to how it is excluded from ordinary single-line entry.
WHY_IT_MATTERS: >
  An inconsistent exclusion lets a deactivated combination re-enter transactions through one entry
  path while being correctly blocked on another.
DISCONFIRMING_OBSERVATION: >
  The grid allows quantity entry against a combination that ordinary single-line entry correctly
  refuses.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Deactivate one specific combination, then attempt entry via the grid and via the ordinary line-
  entry path and compare the outcomes.
```

## G03-PRODUCT_MATRIX-Q003

```yaml
QID: G03-PRODUCT_MATRIX-Q003
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The grid must not silently create a missing sellable record for a combination on the fly to
  satisfy entry, without that creation being visible as a distinct, auditable event.
WHY_IT_MATTERS: >
  Implicit record creation during a transaction obscures how many new combinations now exist and
  who effectively authorized them.
DISCONFIRMING_OBSERVATION: >
  After grid entry, a new combination record exists with no separate, attributable creation event
  distinct from the transaction that used it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Enter a genuinely new combination through the grid, complete the transaction, then search for a
  standalone creation event for that combination.
```

## G03-PRODUCT_MATRIX-Q004

```yaml
QID: G03-PRODUCT_MATRIX-Q004
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The set of combinations exposed in the grid must reflect the actual current valid-combination
  set for the product at the moment the grid is opened, not a cached or stale set from an earlier
  session.
WHY_IT_MATTERS: >
  A stale grid could offer combinations that are no longer valid or omit ones that now are,
  misleading the person entering the transaction.
DISCONFIRMING_OBSERVATION: >
  The grid displays a combination-selection state that does not match the current valid-
  combination set for that product at the time the grid was opened.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Change the valid combination set for a product, then open the grid in a session that had it open
  before the change, and again in a fresh session.
```

## G03-PRODUCT_MATRIX-Q005

```yaml
QID: G03-PRODUCT_MATRIX-Q005
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Attempting to enter a quantity against an invalid or nonexistent combination must produce an
  explicit rejection, not a silent zero-effect or a line that is dropped without notice.
WHY_IT_MATTERS: >
  Silent failure leaves the user believing a line was captured on the document when it was not.
DISCONFIRMING_OBSERVATION: >
  A quantity entered against an invalid combination disappears from the document with no visible
  rejection message anywhere in the session.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Enter a quantity against a combination known to be invalid and observe what happens to the
  document and to any messaging.
```

## G03-PRODUCT_MATRIX-Q006

```yaml
QID: G03-PRODUCT_MATRIX-Q006
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The grid must apply the same minimum or maximum order quantity and packaging-multiple rules per
  combination that ordinary single-line entry applies.
WHY_IT_MATTERS: >
  Bypassing quantity rules through the grid creates orders that the rest of the system would have
  refused if entered manually.
DISCONFIRMING_OBSERVATION: >
  A quantity accepted through the grid for a combination would have been rejected or rounded by
  ordinary single-line entry for the identical combination and quantity.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure a minimum order quantity or packaging multiple for one combination, then compare grid
  entry and ordinary entry of a violating quantity.
```

## G03-PRODUCT_MATRIX-Q007

```yaml
QID: G03-PRODUCT_MATRIX-Q007
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reopening the grid on a document that already has manually entered lines for some of the same
  combinations must show the manually entered quantities, not a blank grid whose save would
  overwrite them.
WHY_IT_MATTERS: >
  A blank re-display risks silently discarding manually entered work the moment the grid is saved
  again.
DISCONFIRMING_OBSERVATION: >
  Saving the grid after reopening it overwrites a quantity that had been manually set on the
  document to a different, unintended value.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Manually set a quantity on one line, then reopen the attribute grid for the same document and
  save without changing that combination.
```

## G03-PRODUCT_MATRIX-Q008

```yaml
QID: G03-PRODUCT_MATRIX-Q008
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the grid and an existing manual line disagree about which unit of measure or variant
  identity applies to the same combination, the conflict must resolve through one explicit,
  documented rule, not whichever entry point saved last.
WHY_IT_MATTERS: >
  Last-write-wins conflict resolution is invisible and unpredictable, making the resulting
  document's correctness a matter of timing.
DISCONFIRMING_OBSERVATION: >
  Two functionally identical entry attempts, one through the grid and one manual, for the same
  combination on the same document produce different final results depending only on save order,
  with no rule surfaced to the user.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a manual line for a combination, then use the grid to also set a quantity for that same
  combination, and observe the resulting document.
```

## G03-PRODUCT_MATRIX-Q009

```yaml
QID: G03-PRODUCT_MATRIX-Q009
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Increasing a quantity through the grid for a combination that already has a manually entered
  line must add to, replace, or create a second line according to one stated rule, applied
  consistently.
WHY_IT_MATTERS: >
  Inconsistent behaviour, sometimes adding and sometimes replacing, makes the resulting document
  unpredictable to whoever entered it.
DISCONFIRMING_OBSERVATION: >
  Repeating the identical grid action twice in a row on the same combination produces different
  outcomes, add versus replace, without an intervening change in context.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Perform the same grid quantity entry for one combination twice in immediate succession and
  compare the results.
```

## G03-PRODUCT_MATRIX-Q010

```yaml
QID: G03-PRODUCT_MATRIX-Q010
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A quantity of zero entered in the grid for a combination that previously had a manually entered
  nonzero line must remove that line, or explicitly flag it for removal, not leave a zero-quantity
  line silently on the document.
WHY_IT_MATTERS: >
  A hidden zero-quantity line can still affect downstream document totals, fulfillment counts, or
  reporting.
DISCONFIRMING_OBSERVATION: >
  After setting a grid cell to zero, a line for that combination with a nonzero effect remains on
  the document.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Set an existing line's combination to zero through the grid and inspect the resulting document
  lines.
```

## G03-PRODUCT_MATRIX-Q011

```yaml
QID: G03-PRODUCT_MATRIX-Q011
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Lines created by the grid must be distinguishable in origin from lines created manually, at
  least in an audit or detail view, so their provenance can be traced.
WHY_IT_MATTERS: >
  Without provenance, a reviewer cannot tell whether a bulk generation or a deliberate manual
  entry produced a given line.
DISCONFIRMING_OBSERVATION: >
  A line's audit or detail view gives no way to determine whether it originated from the grid or
  from manual entry.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create one line via the grid and one manually, then inspect whatever detail or history each line
  exposes.
```

## G03-PRODUCT_MATRIX-Q012

```yaml
QID: G03-PRODUCT_MATRIX-Q012
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The running total shown inside the grid while entering quantities must match the total that
  results on the saved document, including any existing manual lines not touched by the grid.
WHY_IT_MATTERS: >
  A grid total that ignores untouched manual lines misleads the user about the document's actual
  resulting state before they commit.
DISCONFIRMING_OBSERVATION: >
  The total displayed inside the grid differs from the saved document's total once existing manual
  lines are taken into account.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Add a manual line, then open the grid for other combinations and compare the grid's running
  total to the saved document total.
```

## G03-PRODUCT_MATRIX-Q013

```yaml
QID: G03-PRODUCT_MATRIX-Q013
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reopening the grid on a document where a line's price or tax was manually overridden after grid
  entry must preserve that override, not reset it to a recalculated value on save.
WHY_IT_MATTERS: >
  Silently discarding a manual override defeats a deliberate correction someone made to the
  document.
DISCONFIRMING_OBSERVATION: >
  Saving the grid again after a manual price or tax override on one of its lines reverts that line
  to a system-calculated value.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create lines via the grid, manually override price or tax on one resulting line, reopen the
  grid, and save without touching that combination.
```

## G03-PRODUCT_MATRIX-Q014

```yaml
QID: G03-PRODUCT_MATRIX-Q014
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reopening the grid on a document where a grid-created line has already been partially delivered
  or partially invoiced must not allow that line's quantity to be reduced below the already-
  processed amount.
WHY_IT_MATTERS: >
  Reducing a quantity below what has already shipped or been billed creates a document that
  contradicts its own fulfillment or billing history.
DISCONFIRMING_OBSERVATION: >
  The grid accepts and saves a quantity for a combination that is lower than the quantity already
  delivered or invoiced against that same line.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially deliver or invoice one grid-created line, then reopen the grid and attempt to reduce
  that combination's quantity below the processed amount.
```

## G03-PRODUCT_MATRIX-Q015

```yaml
QID: G03-PRODUCT_MATRIX-Q015
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reopening the grid must not silently delete or alter a line that was manually split, merged, or
  reordered after original grid creation, unless the user's current grid action explicitly targets
  that combination.
WHY_IT_MATTERS: >
  An unrelated grid save could destroy unrelated manual restructuring that someone deliberately
  performed on the document.
DISCONFIRMING_OBSERVATION: >
  Saving the grid after unrelated manual restructuring of the document removes or alters a line
  the current grid session never touched.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Manually split one grid-created line into two, reopen the grid for a different combination, and
  save.
```

## G03-PRODUCT_MATRIX-Q016

```yaml
QID: G03-PRODUCT_MATRIX-Q016
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A document in a state where line quantities are normally no longer editable must apply that same
  restriction to the grid, not allow the grid to bypass it.
WHY_IT_MATTERS: >
  A bypass through the grid undermines whatever workflow gate the state transition was meant to
  enforce.
DISCONFIRMING_OBSERVATION: >
  The grid successfully changes quantities on a document that is in a state where ordinary line
  editing is blocked.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Advance a document to a state that normally locks line editing, then attempt a grid-based
  change.
```

## G03-PRODUCT_MATRIX-Q017

```yaml
QID: G03-PRODUCT_MATRIX-Q017
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Canceling or discarding an open grid session before saving must leave the document exactly as it
  was before the grid was opened, with no partial effect.
WHY_IT_MATTERS: >
  A partial effect from an abandoned session is a silent, unintended change the user never asked
  to commit.
DISCONFIRMING_OBSERVATION: >
  Closing or canceling the grid without an explicit save still leaves some detectable change on
  the underlying document.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Open the grid, enter several quantities, then close it via a cancel or discard action rather
  than save, and inspect the document.
```

## G03-PRODUCT_MATRIX-Q018

```yaml
QID: G03-PRODUCT_MATRIX-Q018
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reopening the grid after the document's currency, price list, or applicable tax regime has
  changed must recalculate those values for grid-created lines using the new context, not silently
  keep values computed under the prior context.
WHY_IT_MATTERS: >
  Stale pricing or tax context on reopened lines misstates the document relative to its now-
  current commercial terms.
DISCONFIRMING_OBSERVATION: >
  A line created by the grid under a prior price list or tax context keeps that context's
  calculated values after the document's context has changed and the grid is reopened and saved.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create grid lines, change the document's price list, currency, or tax context, then reopen the
  grid and save without altering that combination.
```

## G03-PRODUCT_MATRIX-Q019

```yaml
QID: G03-PRODUCT_MATRIX-Q019
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Renaming an attribute value after the grid has been used to create lines referencing it must not
  silently relabel or reinterpret the meaning already recorded on those historical lines.
WHY_IT_MATTERS: >
  Relabeling history changes what a past, already-completed transaction is understood to have been
  about.
DISCONFIRMING_OBSERVATION: >
  A historical document line's displayed combination changes meaning after an attribute value is
  renamed, with no indication that a rename occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a grid line for a combination, rename one of its attribute values, then reopen the
  historical document.
```

## G03-PRODUCT_MATRIX-Q020

```yaml
QID: G03-PRODUCT_MATRIX-Q020
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Deactivating an attribute value after it has been used in grid-created lines must not remove
  those historical lines from view or prevent their historical document from being displayed
  correctly.
WHY_IT_MATTERS: >
  Deactivation is meant to prevent new use going forward, not erase or corrupt the historical
  record.
DISCONFIRMING_OBSERVATION: >
  A historical document containing a now-deactivated attribute-value combination fails to display
  correctly or loses that line.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a grid line using a specific attribute value, deactivate that value, then reopen the
  historical document.
```

## G03-PRODUCT_MATRIX-Q021

```yaml
QID: G03-PRODUCT_MATRIX-Q021
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting an attribute value that has been used in grid-created lines with recorded movement or
  financial history must be prevented, or must require an explicit, logged override, rather than
  succeeding silently.
WHY_IT_MATTERS: >
  Deleting a value with attached transactional history breaks referential integrity of every past
  transaction that used it.
DISCONFIRMING_OBSERVATION: >
  An attribute value with existing transactional history can be deleted through the same path used
  for one with no history, with no distinct warning or log entry.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Attempt to delete an attribute value that has movement, and separately one that has none, and
  compare the system's behaviour in each case.
```

## G03-PRODUCT_MATRIX-Q022

```yaml
QID: G03-PRODUCT_MATRIX-Q022
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Adding a new attribute value to an axis used by the grid must make it available in the grid for
  new entry without altering the identity of combinations that existed before the addition.
WHY_IT_MATTERS: >
  An addition should be purely additive; it must never renumber or reinterpret combinations that
  already exist.
DISCONFIRMING_OBSERVATION: >
  Adding a new attribute value changes which combination an existing historical line is understood
  to represent.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Add a new value to an attribute axis already used by existing grid-created lines, then inspect
  whether existing lines still map to the same combination.
```

## G03-PRODUCT_MATRIX-Q023

```yaml
QID: G03-PRODUCT_MATRIX-Q023
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reordering the display sequence of attribute values or axes must not change which combination a
  previously saved grid cell corresponds to.
WHY_IT_MATTERS: >
  Display order is purely presentational and must never carry semantic weight over what a saved
  line actually represents.
DISCONFIRMING_OBSERVATION: >
  After reordering attribute-value display sequence, a previously saved line's underlying
  combination is reported differently than before the reorder.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Reorder the displayed sequence of attribute values, then reopen a document with existing grid-
  created lines.
```

## G03-PRODUCT_MATRIX-Q024

```yaml
QID: G03-PRODUCT_MATRIX-Q024
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A combination that becomes newly valid after the grid was first opened in the current session
  must be reachable by refreshing the grid, not require abandoning and restarting document entry.
WHY_IT_MATTERS: >
  Forcing a full restart to reach a legitimate new combination is a usability failure, and
  silently omitting it with no way to reach it is worse.
DISCONFIRMING_OBSERVATION: >
  A combination made valid during an open grid session cannot be entered even after an explicit
  refresh of the grid within that same document session.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Open the grid, then have a new attribute value added elsewhere, and attempt to refresh and use
  it within the same session.
```

## G03-PRODUCT_MATRIX-Q025

```yaml
QID: G03-PRODUCT_MATRIX-Q025
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Each combination entered through the grid must resolve its own price according to the same
  price-list and pricing-rule precedence that a single manually entered line for that combination
  would use.
WHY_IT_MATTERS: >
  A shortcut pricing path specific to the grid could systematically misprice every bulk-entered
  line.
DISCONFIRMING_OBSERVATION: >
  The price assigned to a combination by the grid differs from the price that manual entry of the
  identical combination, quantity, and context would produce.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Enter the same combination and quantity once via the grid and once manually, under identical
  pricing context, and compare the resulting prices.
```

## G03-PRODUCT_MATRIX-Q026

```yaml
QID: G03-PRODUCT_MATRIX-Q026
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A combination-specific price override must be honoured by the grid exactly as it would be by
  manual entry.
WHY_IT_MATTERS: >
  An override the grid ignores silently reverts pricing to a default the business specifically
  overrode for a reason.
DISCONFIRMING_OBSERVATION: >
  A combination with a configured price override receives the base or default price instead when
  entered through the grid.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure a price override for one specific combination, then enter it through the grid and
  inspect the resulting price.
```

## G03-PRODUCT_MATRIX-Q027

```yaml
QID: G03-PRODUCT_MATRIX-Q027
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Tax determination for a grid-created line must use the same jurisdiction, customer, and product-
  category rules as manual entry, not a simplified or default tax treatment specific to bulk
  entry.
WHY_IT_MATTERS: >
  Incorrect tax on bulk-entered lines creates compliance exposure that scales with every
  combination entered through the grid.
DISCONFIRMING_OBSERVATION: >
  A grid-created line's tax differs from what manual entry of the identical line, customer, and
  context would calculate.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Compare tax calculated on a grid-created line against tax calculated on an identical manually
  entered line.
```

## G03-PRODUCT_MATRIX-Q028

```yaml
QID: G03-PRODUCT_MATRIX-Q028
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A quantity-based pricing break must apply per the same aggregation rule to grid-entered lines as
  it does elsewhere, whether per combination or across the whole document, consistently with
  however it is configured.
WHY_IT_MATTERS: >
  An inconsistent aggregation rule silently changes which quantities qualify for a price break
  depending only on the entry path used.
DISCONFIRMING_OBSERVATION: >
  Identical total quantity across several combinations qualifies for a quantity price break when
  entered as separate manual lines but not when entered through the grid, or vice versa, with no
  configuration explaining the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure a quantity price break, then enter the qualifying total quantity once as separate
  manual lines and once through the grid.
```

## G03-PRODUCT_MATRIX-Q029

```yaml
QID: G03-PRODUCT_MATRIX-Q029
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing the quantity of one combination within an already-populated grid must not recalculate
  or disturb the price or tax already resolved for a different, untouched combination in the same
  session.
WHY_IT_MATTERS: >
  Cross-cell interference would make bulk entry unpredictable and impossible to verify line by
  line before saving.
DISCONFIRMING_OBSERVATION: >
  Editing one cell's quantity in the grid changes the resolved price or tax shown for a different
  cell that was not edited.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Populate several combinations in the grid, then change the quantity of only one and inspect the
  others.
```

## G03-PRODUCT_MATRIX-Q030

```yaml
QID: G03-PRODUCT_MATRIX-Q030
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A currency or price-list change made on the document header after the grid has already populated
  lines must be reflected consistently across all grid-created lines, not applied to some and not
  others.
WHY_IT_MATTERS: >
  Partial application of a header-level change leaves the document internally inconsistent about
  which commercial terms actually apply.
DISCONFIRMING_OBSERVATION: >
  After a header-level currency or price-list change, some grid-created lines reflect the new
  context and others still reflect the old one.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Populate the grid, change the document header's currency or price list, and inspect all
  resulting lines.
```

## G03-PRODUCT_MATRIX-Q031

```yaml
QID: G03-PRODUCT_MATRIX-Q031
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A stock or availability check that would block or warn on a manually entered line must apply
  identically when the same combination and quantity are entered through the grid.
WHY_IT_MATTERS: >
  A bypassed availability check lets bulk entry commit to quantities the business cannot actually
  fulfill.
DISCONFIRMING_OBSERVATION: >
  A combination and quantity that would trigger an availability block or warning on manual entry
  passes silently through the grid.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Choose a combination with insufficient available stock and compare grid entry to manual entry.
```

## G03-PRODUCT_MATRIX-Q032

```yaml
QID: G03-PRODUCT_MATRIX-Q032
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A credit limit, customer block, or similar document-level control must still be enforced when it
  is the total effect of a grid session, not a single manual line, that pushes the document over
  the limit.
WHY_IT_MATTERS: >
  A control that only checks single-line changes can be defeated simply by making the same change
  through bulk grid entry instead.
DISCONFIRMING_OBSERVATION: >
  A grid session that in total exceeds a control threshold saves successfully with no warning or
  block, while an equivalent single manual line would have been blocked.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Set a document-level control threshold, then use the grid to exceed it in aggregate across
  multiple combinations in one save.
```

## G03-PRODUCT_MATRIX-Q033

```yaml
QID: G03-PRODUCT_MATRIX-Q033
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combination restricted to certain customers, channels, or contexts must be excluded from the
  grid in a context where it is not permitted, exactly as it would be excluded from manual entry.
WHY_IT_MATTERS: >
  The grid must not become a side door around an item the business deliberately restricted.
DISCONFIRMING_OBSERVATION: >
  A restricted combination is selectable and savable through the grid in a context where manual
  entry of the same combination is refused.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Configure a context-restricted combination, then attempt entry through the grid in a disallowed
  context and via manual entry.
```

## G03-PRODUCT_MATRIX-Q034

```yaml
QID: G03-PRODUCT_MATRIX-Q034
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A mandatory line-level field or approval required by business rule on a manually entered line
  must also be required, not silently skipped, when the equivalent line is created via the grid.
WHY_IT_MATTERS: >
  Skipping a mandatory control through bulk entry undermines the exact purpose the control was
  created for.
DISCONFIRMING_OBSERVATION: >
  A line created through the grid saves successfully despite missing a field or approval that
  manual entry of the same line would refuse to save without.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure a mandatory line-level requirement, then attempt equivalent entry through the grid and
  through manual entry.
```

## G03-PRODUCT_MATRIX-Q035

```yaml
QID: G03-PRODUCT_MATRIX-Q035
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A document-level total or line-count limit, where one is configured, must count grid-created
  lines the same way it counts manually entered lines.
WHY_IT_MATTERS: >
  An exemption for grid-created lines would let bulk entry silently exceed a ceiling the business
  intended to be absolute.
DISCONFIRMING_OBSERVATION: >
  A document exceeds a configured line-count or total limit only because the additional lines came
  from the grid rather than from manual entry.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure a line-count or total limit near the current document size, then add the remaining
  lines via the grid and observe whether the limit is enforced.
```

## G03-PRODUCT_MATRIX-Q036

```yaml
QID: G03-PRODUCT_MATRIX-Q036
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An approval workflow triggered by a document characteristic, such as total value or a specific
  combination, must trigger identically whether that characteristic was reached through grid entry
  or manual entry.
WHY_IT_MATTERS: >
  An approval gate that only recognizes manually entered triggers is a governance gap that bulk
  entry can exploit.
DISCONFIRMING_OBSERVATION: >
  A document that would trigger a required approval when the triggering line is entered manually
  does not trigger it when the same line is produced by the grid.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Configure an approval trigger, then reach the trigger condition once via manual entry and once
  via the grid.
```

## G03-PRODUCT_MATRIX-Q037

```yaml
QID: G03-PRODUCT_MATRIX-Q037
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Creating a brand-new combination inline during grid entry, where the platform allows it, must
  require the same permission that creating that combination through the ordinary product-
  maintenance path requires.
WHY_IT_MATTERS: >
  An inline shortcut must not grant a lesser-privileged user a capability they are not otherwise
  entitled to.
DISCONFIRMING_OBSERVATION: >
  A user without permission to create new product or variant records can nonetheless create one
  inline through the grid.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt inline combination creation in the grid using a user role that lacks product-maintenance
  permission.
```

## G03-PRODUCT_MATRIX-Q038

```yaml
QID: G03-PRODUCT_MATRIX-Q038
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combination created inline through the grid during a transaction must be visible to product-
  maintenance users through the ordinary master-data views, not exist only as a side effect
  trapped inside that one document.
WHY_IT_MATTERS: >
  An orphaned record invisible to master-data governance cannot be reviewed, corrected, or reused
  consistently by anyone else.
DISCONFIRMING_OBSERVATION: >
  A combination created inline via the grid does not appear in the ordinary product or variant
  maintenance listing used to manage combinations.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a new combination inline through the grid, then search for it in the standard master-data
  maintenance view.
```

## G03-PRODUCT_MATRIX-Q039

```yaml
QID: G03-PRODUCT_MATRIX-Q039
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user permitted to view and enter quantities in the grid but not permitted to see cost or
  margin data must not have either exposed to them through any grid-specific view.
WHY_IT_MATTERS: >
  A specialized bulk-entry view remains subject to the same data-visibility permissions as any
  other view in the system.
DISCONFIRMING_OBSERVATION: >
  The grid displays a cost or margin-derived figure to a user who does not have permission to see
  it elsewhere.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Open the grid as a user without cost or margin visibility and inspect every value the grid
  surfaces.
```

## G03-PRODUCT_MATRIX-Q040

```yaml
QID: G03-PRODUCT_MATRIX-Q040
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user's permission to enter lines against a specific company, branch, or warehouse scope must
  be enforced per combination in the grid exactly as it is enforced in manual entry, when
  combinations differ by scope-specific availability.
WHY_IT_MATTERS: >
  Scope enforcement that only applies outside the grid creates a bypass specific to bulk entry.
DISCONFIRMING_OBSERVATION: >
  The grid allows entry against a combination whose availability is restricted to a scope the
  current user does not have permission for, when manual entry of the same combination in the same
  scope is refused.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Restrict a combination's availability to a specific scope, then attempt grid entry as a user
  without access to that scope.
```

## G03-PRODUCT_MATRIX-Q041

```yaml
QID: G03-PRODUCT_MATRIX-Q041
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Revoking a user's permission to use the grid feature must take effect for that user's next
  attempt to open it, not merely for newly issued accounts, and must not allow a session already
  holding the grid open to save afterward.
WHY_IT_MATTERS: >
  A delayed revocation window leaves a live security gap for exactly as long as the stale session
  remains open.
DISCONFIRMING_OBSERVATION: >
  A user whose grid permission was revoked can still save an already-open grid session, or can
  still reopen the grid, after the revocation.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Open the grid as a user, revoke that user's grid permission mid-session, then attempt to save;
  separately, attempt to reopen the grid as that user.
```

## G03-PRODUCT_MATRIX-Q042

```yaml
QID: G03-PRODUCT_MATRIX-Q042
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The set of combinations offered in the grid must respect any per-role or per-scope restriction
  on which products or variants that role may transact, not show a universal set regardless of
  role.
WHY_IT_MATTERS: >
  Showing restricted combinations, even before any entry attempt, leaks their existence to a user
  who should not see them at all.
DISCONFIRMING_OBSERVATION: >
  The grid lists a combination that the current user's role is not permitted to transact at all,
  even before any attempt to enter a quantity.
EXPECTED_SURFACE: S1,S4,S5
PRECONDITIONS: >
  Restrict a product or variant to certain roles, then open the grid for it as a user outside
  those roles.
```

## G03-PRODUCT_MATRIX-Q043

```yaml
QID: G03-PRODUCT_MATRIX-Q043
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two users opening the grid for the same document at the same time must not have one user's save
  silently overwrite the other's unrelated changes without at least a conflict indication.
WHY_IT_MATTERS: >
  Silent last-write-wins on a shared document loses one user's genuine work without any notice to
  either party.
DISCONFIRMING_OBSERVATION: >
  One user's save through the grid removes or alters combinations that the other user had just
  added, with no conflict warning shown to either user.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Have two sessions open the grid on the same document concurrently, make non-overlapping changes
  in each, and save both.
```

## G03-PRODUCT_MATRIX-Q044

```yaml
QID: G03-PRODUCT_MATRIX-Q044
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Bulk lines created in a single grid save must be individually recorded in the document's audit
  trail as distinct line-creation events, not collapsed into one undifferentiated batch entry that
  hides which combinations were added.
WHY_IT_MATTERS: >
  An undifferentiated batch record prevents tracing a specific problematic line back to the save
  that created it.
DISCONFIRMING_OBSERVATION: >
  The audit trail for a grid save that created several lines cannot identify which specific
  combinations and quantities were added in that save.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create several lines in one grid save and inspect the resulting audit trail in detail.
```

## G03-PRODUCT_MATRIX-Q045

```yaml
QID: G03-PRODUCT_MATRIX-Q045
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A tenant's product attributes, combinations, and any grid configuration must never be visible or
  selectable within another tenant's grid session, even where attribute names happen to coincide.
WHY_IT_MATTERS: >
  Cross-tenant leakage of master data through a shared entry mechanism breaks the isolation the
  platform promises every tenant.
DISCONFIRMING_OBSERVATION: >
  A combination or attribute value belonging to one tenant appears as selectable within another
  tenant's grid session.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure similarly named attributes in two separate tenants and open the grid in each, checking
  for cross-tenant leakage.
```

## G03-PRODUCT_MATRIX-Q046

```yaml
QID: G03-PRODUCT_MATRIX-Q046
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Canceling or reversing a document whose lines were originally created via the grid must reverse
  each affected combination's quantity and financial effect completely, leaving no partial residue
  attributable to the grid's bulk-creation origin.
WHY_IT_MATTERS: >
  A bulk-created set of lines must be exactly as fully reversible as an equivalent set of manually
  entered lines.
DISCONFIRMING_OBSERVATION: >
  Reversing a document with grid-created lines leaves a residual quantity, financial effect, or
  open line for at least one combination that a fully manual equivalent document would not leave.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Fully cancel or reverse a document whose lines were created via the grid and compare the
  residual state to that of an equivalently reversed manual document.
```

## G03-PRODUCT_MATRIX-Q047

```yaml
QID: G03-PRODUCT_MATRIX-Q047
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Entering a negative quantity in the grid, where the platform allows negative quantity entry at
  all, must be subject to the same authorization and validation as a negative quantity entered
  manually.
WHY_IT_MATTERS: >
  An unchecked negative-quantity path through the grid is an easy route to an unauthorized credit
  or stock adjustment.
DISCONFIRMING_OBSERVATION: >
  A negative quantity entered through the grid saves without the authorization or validation step
  that an equivalent manual negative-quantity line requires.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Attempt a negative quantity entry through the grid and through manual entry, under identical
  authorization context, and compare.
```

## G03-PRODUCT_MATRIX-Q048

```yaml
QID: G03-PRODUCT_MATRIX-Q048
MODULE: product_matrix
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Performance degradation or a partial failure when saving an unusually large grid must not
  silently save a subset of the intended lines while reporting overall success.
WHY_IT_MATTERS: >
  A false success on a partial save creates an undetected gap between what the user intended to
  record and what was actually saved.
DISCONFIRMING_OBSERVATION: >
  A large grid save reports success while fewer lines exist on the document than were entered,
  with no error or warning identifying the shortfall.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Populate the grid with a large number of combinations in one session and save, then verify the
  resulting document line count against what was entered.
```

