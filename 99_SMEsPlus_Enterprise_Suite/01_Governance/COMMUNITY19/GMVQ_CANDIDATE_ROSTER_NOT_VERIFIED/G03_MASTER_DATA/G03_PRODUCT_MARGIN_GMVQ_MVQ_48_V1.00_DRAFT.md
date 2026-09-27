# SMEsPlus ENTERPRISE SUITE
## GMVQ — G03 MASTER_DATA / product_margin Module Adversarial MVQ Bank

**Document ID:** GMVQ-G03-PRODUCT_MARGIN-MVQ48-V1.00  
**Group:** G03 MASTER_DATA  
**Module Metadata:** `product_margin`  
**Wave:** W1  
**Author Cell:** TEAM 18 (GMVQ Question Factory — Primary MVQ Authoring)  
**Review Cell:** PENDING  
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN  
**actual_mvq_count:** 48  
**Standard bank reference:** 55 (shared, not reproduced here)  
**Research depth:** 55 + 48 = 103  
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded  

## Purpose

This bank authors the module-specific MVQ set for `product_margin` — derived margin figures
computed from transactional cost and revenue. It targets cost-basis integrity, recomputed-vs-stored
semantics and restatement, cross-company and multi-currency consolidation, partial delivery and
invoicing, returns and cancellations, reconciliation against financial statements, permission
separation between cost and margin visibility, export and audit exposure, concurrency in background
recomputation, and tenant/company boundary integrity. Per the Group Brief for G03 MASTER_DATA,
particular weight is given to derived-figure recompute-versus-restate behaviour and to auditability
of any master-data change that alters a financial outcome.

The question text is source-neutral and does not expose vendor model names, field names, methods,
schema, XML IDs, API shapes, or implementation algorithms. `MODULE: product_margin` appears only
in the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 48 questions exist because they test 48 distinct material hypotheses.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## G03-PRODUCT_MARGIN-Q001

```yaml
QID: G03-PRODUCT_MARGIN-Q001
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A margin figure must be computed from a cost basis that matches the cost basis the accounting
  record used for the same transaction, not a different, concurrently available cost value.
WHY_IT_MATTERS: >
  A mismatched basis produces a management number that never reconciles to the ledger, undermining
  trust in every downstream report built on it.
DISCONFIRMING_OBSERVATION: >
  The margin shown for a transaction differs from cost-minus-revenue as recorded in the posted
  accounting entries for that same transaction, with no documented reconciling item.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Capture the cost value active at posting time and the cost value active at report time when the
  two differ, then compare the reported margin to the posted entries for the same transaction.
```

## G03-PRODUCT_MARGIN-Q002

```yaml
QID: G03-PRODUCT_MARGIN-Q002
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a margin figure is stored at the time of the transaction rather than recomputed on read,
  the stored value must remain retrievable and distinguishable from a live recomputation using
  current data.
WHY_IT_MATTERS: >
  Without that distinction an analyst cannot tell whether a displayed number reflects the past
  transaction or a present-day recalculation.
DISCONFIRMING_OBSERVATION: >
  A margin value on a historical record recalculates to a different number after underlying inputs
  change, with no indication that a recomputation occurred.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record a transaction, change a cost or price input afterward, then reopen the transaction and
  inspect its margin figure.
```

## G03-PRODUCT_MARGIN-Q003

```yaml
QID: G03-PRODUCT_MARGIN-Q003
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the cost basis for a product changes after transactions have already posted, margin figures
  on those already-posted transactions must not restate unless an explicit recomputation action is
  invoked.
WHY_IT_MATTERS: >
  Silent restatement changes historical management reports with no audit trail explaining why the
  numbers moved.
DISCONFIRMING_OBSERVATION: >
  Historical transactions show a different margin figure after a cost-basis change, with no
  recomputation action logged anywhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post transactions under one cost basis, change the cost basis, then reopen the historical
  transactions without running any recompute action.
```

## G03-PRODUCT_MARGIN-Q004

```yaml
QID: G03-PRODUCT_MARGIN-Q004
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An explicit recomputation of historical margin figures after a cost-basis change must leave an
  auditable record of which figures changed, from what value, to what value, and under what
  authorization.
WHY_IT_MATTERS: >
  Without that trail a restated number cannot be explained during a financial review or audit.
DISCONFIRMING_OBSERVATION: >
  A bulk margin recomputation changes stored figures but leaves no retrievable record identifying
  the affected transactions or their prior values.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Trigger a recomputation after a cost-basis change and inspect whatever trail the system produces
  for it.
```

## G03-PRODUCT_MARGIN-Q005

```yaml
QID: G03-PRODUCT_MARGIN-Q005
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The margin figure must use the same rounding and precision rules for its cost input as the
  accounting entries do, not an independent rounding convention specific to margin reporting.
WHY_IT_MATTERS: >
  Independent rounding creates a persistent, unexplained gap between the reported margin and the
  books that never nets to zero.
DISCONFIRMING_OBSERVATION: >
  The margin figure and the corresponding posted cost differ only because of a rounding rule
  specific to the margin calculation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Choose a transaction with a cost value that does not divide evenly and compare rounding
  behaviour in the margin figure and in the posted entry.
```

## G03-PRODUCT_MARGIN-Q006

```yaml
QID: G03-PRODUCT_MARGIN-Q006
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A product with no recorded cost at all must produce a margin state that is explicit about
  missing data, not a numeric value silently computed from an assumed zero cost.
WHY_IT_MATTERS: >
  A silent zero-cost assumption overstates margin and can mislead a pricing or discounting
  decision.
DISCONFIRMING_OBSERVATION: >
  A transaction line for a product with no cost history reports a margin equal to full revenue
  with no flag indicating the cost input was absent.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Transact a product that has never had a cost recorded and inspect the reported margin and any
  accompanying indicator.
```

## G03-PRODUCT_MARGIN-Q007

```yaml
QID: G03-PRODUCT_MARGIN-Q007
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Consolidating margin across companies configured with different valuation settings must not
  silently blend incompatible valuation methods into one number without disclosing that a blend
  occurred.
WHY_IT_MATTERS: >
  An undisclosed blend of valuation methods produces a consolidated figure that no single
  company's method actually supports.
DISCONFIRMING_OBSERVATION: >
  A consolidated margin report combines figures from companies with different valuation methods
  with no note that the underlying methods differ.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Configure two companies with different valuation settings, transact comparable products in each,
  and inspect a consolidated margin report.
```

## G03-PRODUCT_MARGIN-Q008

```yaml
QID: G03-PRODUCT_MARGIN-Q008
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Currency conversion inside a margin calculation must use the rate that applied at the
  transaction date, not a current spot rate, unless an explicit revaluation is requested.
WHY_IT_MATTERS: >
  Using a moving rate inside a supposedly historical figure makes the same past transaction report
  a different margin every time it is viewed.
DISCONFIRMING_OBSERVATION: >
  The margin figure for a completed historical transaction changes over time purely because the
  current exchange rate moved, with no revaluation action taken.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a foreign-currency transaction, allow the exchange rate to move, and reopen the
  transaction's margin figure without running a revaluation.
```

## G03-PRODUCT_MARGIN-Q009

```yaml
QID: G03-PRODUCT_MARGIN-Q009
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A margin figure aggregated across companies with different functional currencies must state, or
  make discoverable, which rate and convention was used for the roll-up.
WHY_IT_MATTERS: >
  An unstated roll-up convention makes the consolidated number impossible to independently verify.
DISCONFIRMING_OBSERVATION: >
  A multi-currency consolidated margin figure cannot be traced to the specific rate or convention
  used to combine the underlying currencies.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Produce a consolidated margin figure spanning companies with different functional currencies and
  attempt to trace the roll-up methodology.
```

## G03-PRODUCT_MARGIN-Q010

```yaml
QID: G03-PRODUCT_MARGIN-Q010
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A margin figure for a transaction between two companies within the same tenant must not be
  computed against a price that was itself adjusted for intercompany purposes, without disclosing
  that adjustment.
WHY_IT_MATTERS: >
  An undisclosed intercompany price adjustment makes an internal transfer look like an external
  market-rate sale or vice versa.
DISCONFIRMING_OBSERVATION: >
  An intercompany transaction's margin figure uses the intercompany price with no indication that
  the price differs from the equivalent external price.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure a distinct intercompany price for a product, transact it between two companies, and
  inspect the resulting margin figure and its disclosure.
```

## G03-PRODUCT_MARGIN-Q011

```yaml
QID: G03-PRODUCT_MARGIN-Q011
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A margin figure must respect the valuation method configured at the company where the
  transaction actually posted, not the valuation method of the product's originating or default
  company.
WHY_IT_MATTERS: >
  Using the wrong company's valuation method silently misstates margin for every transaction
  outside the product's home company.
DISCONFIRMING_OBSERVATION: >
  A transaction posted in a company with one valuation method produces a margin figure that
  matches the valuation method of a different company instead.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure two companies with different valuation methods sharing the same product, transact in
  the non-default company, and inspect which method the margin reflects.
```

## G03-PRODUCT_MARGIN-Q012

```yaml
QID: G03-PRODUCT_MARGIN-Q012
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where cost and revenue use different currency-rate types (for example an average rate for cost
  and a transaction rate for revenue), the margin calculation must not silently combine the two
  rate types as if they were the same.
WHY_IT_MATTERS: >
  Combining incompatible rate types produces a margin figure that reflects no coherent single
  conversion methodology.
DISCONFIRMING_OBSERVATION: >
  The margin figure for a foreign-currency transaction cannot be reproduced using either rate type
  alone, only by an undocumented mix of both.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure a scenario where cost and revenue are converted using different rate types and attempt
  to reproduce the reported margin from each rate type independently.
```

## G03-PRODUCT_MARGIN-Q013

```yaml
QID: G03-PRODUCT_MARGIN-Q013
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A margin figure computed before a document is fully delivered must be visibly distinguished as
  provisional, not presented identically to the margin of a fully delivered document.
WHY_IT_MATTERS: >
  Treating a provisional figure as final can drive a business decision on a number that has not
  yet settled.
DISCONFIRMING_OBSERVATION: >
  A partially delivered document's margin figure is displayed with no indication that delivery,
  and therefore the figure, is incomplete.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Partially deliver a document with multiple lines and inspect how its margin figure is presented
  relative to a fully delivered equivalent.
```

## G03-PRODUCT_MARGIN-Q014

```yaml
QID: G03-PRODUCT_MARGIN-Q014
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A margin figure driven by the invoiced amount, when only part of a document has been invoiced,
  must not overstate margin relative to the full committed transaction.
WHY_IT_MATTERS: >
  An invoiced-only view can flatter margin by comparing partial revenue against a cost basis
  intended for the whole commitment.
DISCONFIRMING_OBSERVATION: >
  The margin percentage shown for a partially invoiced document is higher than the margin the
  fully invoiced document would show, purely as an artifact of partial invoicing.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially invoice a multi-line document and compare its margin figure and percentage to the
  fully invoiced equivalent.
```

## G03-PRODUCT_MARGIN-Q015

```yaml
QID: G03-PRODUCT_MARGIN-Q015
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A return or credit note must reduce the previously recognized margin using the same cost and
  revenue basis that produced the original figure, not a current-value basis.
WHY_IT_MATTERS: >
  Reversing a historical figure with today's values creates a mismatch between the original sale's
  margin and its own reversal.
DISCONFIRMING_OBSERVATION: >
  The margin reduction recorded for a return differs from the original transaction's margin
  components because current cost or price values were used instead of the original ones.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a sale, allow cost or price to change, then process a full return and compare the
  reversal's basis to the original sale's basis.
```

## G03-PRODUCT_MARGIN-Q016

```yaml
QID: G03-PRODUCT_MARGIN-Q016
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Canceling a document that already contributed to a margin figure must remove that contribution
  from every aggregate margin report it fed, not merely from the document's own individual
  display.
WHY_IT_MATTERS: >
  A cancellation that only clears the single-document view leaves aggregate reports permanently
  overstated.
DISCONFIRMING_OBSERVATION: >
  An aggregate margin report still reflects a document's contribution after that document has been
  fully canceled.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Include a document in a period's aggregate margin report, cancel the document, and regenerate
  the aggregate report.
```

## G03-PRODUCT_MARGIN-Q017

```yaml
QID: G03-PRODUCT_MARGIN-Q017
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A partial return must adjust the margin figure proportionally without introducing rounding drift
  that compounds across multiple partial returns against the same document.
WHY_IT_MATTERS: >
  Compounding rounding drift across several partial returns can silently accumulate into a
  materially wrong final margin.
DISCONFIRMING_OBSERVATION: >
  After several partial returns against the same document, the sum of the remaining and returned
  margin components no longer equals the original margin, beyond a single rounding unit.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Process several successive partial returns against one document and reconcile the sum of
  remaining and returned margin to the original figure.
```

## G03-PRODUCT_MARGIN-Q018

```yaml
QID: G03-PRODUCT_MARGIN-Q018
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A credit note issued in a later accounting period than the original sale must have its margin
  adjustment recorded in an auditable, identifiable period, not silently restate the original
  period's already-closed figure.
WHY_IT_MATTERS: >
  Restating a closed period without record breaks the integrity of financial statements already
  issued for that period.
DISCONFIRMING_OBSERVATION: >
  Issuing a credit note in a later period changes the margin figure attributed to the original,
  already-closed period with no separate adjustment record in the later period.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Close a period containing a sale, then issue a credit note for it in a subsequent period and
  inspect where the margin adjustment lands.
```

## G03-PRODUCT_MARGIN-Q019

```yaml
QID: G03-PRODUCT_MARGIN-Q019
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a margin report disagrees with the financial statements for the same period, the system
  must expose a reconciling explanation, not present both figures as independently authoritative
  with no way to reconcile them.
WHY_IT_MATTERS: >
  Two unreconciled 'authoritative' numbers for the same period is a direct governance and audit
  failure.
DISCONFIRMING_OBSERVATION: >
  A margin report and the corresponding financial statement disagree for the same period and no
  reconciling detail is discoverable anywhere.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Compare a period's margin report total to the corresponding financial-statement figures and
  attempt to trace any discrepancy to a specific cause.
```

## G03-PRODUCT_MARGIN-Q020

```yaml
QID: G03-PRODUCT_MARGIN-Q020
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An aggregate margin figure for a period must equal the sum of the transaction-level margins that
  compose it, not a separately, independently computed macro figure.
WHY_IT_MATTERS: >
  A macro figure computed by a different method than its stated components cannot be verified or
  trusted by drilling down.
DISCONFIRMING_OBSERVATION: >
  Summing the transaction-level margins shown as the detail behind a period total does not equal
  the period total itself.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Take a period's aggregate margin figure, sum its listed transaction-level detail, and compare
  the two totals.
```

## G03-PRODUCT_MARGIN-Q021

```yaml
QID: G03-PRODUCT_MARGIN-Q021
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A manually overridden price or manually overridden cost on a single transaction must flow into
  the margin figure exactly as entered, not be silently re-derived from the standard or list
  values.
WHY_IT_MATTERS: >
  Ignoring a deliberate manual override defeats the specific correction the business intended.
DISCONFIRMING_OBSERVATION: >
  A transaction with a manually overridden price or cost shows a margin figure computed from the
  un-overridden standard value instead.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Manually override the price or cost on one transaction and compare the resulting margin to what
  the override, versus the standard value, would produce.
```

## G03-PRODUCT_MARGIN-Q022

```yaml
QID: G03-PRODUCT_MARGIN-Q022
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A discount applied at the transaction-line level versus at the document-header level must be
  reflected in the margin figure at the level it was actually granted, without being double-
  applied or omitted.
WHY_IT_MATTERS: >
  Double-applying or dropping a discount produces a margin figure that does not match what the
  customer was actually charged.
DISCONFIRMING_OBSERVATION: >
  The margin figure for a document does not change when a header-level discount is applied, or
  changes twice as much as the discount amount would predict.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a discount once at the line level and once at the header level on comparable documents and
  verify the margin impact matches the discount amount exactly once in each case.
```

## G03-PRODUCT_MARGIN-Q023

```yaml
QID: G03-PRODUCT_MARGIN-Q023
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A margin figure for a component sold within a bundle at an allocated price must use the
  allocation actually applied to that specific transaction, not the component's stand-alone list
  price.
WHY_IT_MATTERS: >
  Using the stand-alone price for a bundled component misstates margin for every bundled sale.
DISCONFIRMING_OBSERVATION: >
  The margin figure for a bundled component matches its stand-alone list price rather than the
  price it was actually allocated within the bundle.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Sell a product both stand-alone and within a bundle at a different allocated price, and compare
  the margin figures for each.
```

## G03-PRODUCT_MARGIN-Q024

```yaml
QID: G03-PRODUCT_MARGIN-Q024
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A loss-making transaction must retain and display a negative margin, not have that value clamped
  to zero or masked when it feeds an aggregate report.
WHY_IT_MATTERS: >
  Clamping or masking a loss hides exactly the transactions that most need management attention.
DISCONFIRMING_OBSERVATION: >
  A transaction known to be sold below cost shows a margin of zero, or is silently excluded from
  an aggregate margin report, instead of showing a negative value.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Record a transaction priced below its recorded cost and inspect both its own margin figure and
  its treatment in an aggregate report.
```

## G03-PRODUCT_MARGIN-Q025

```yaml
QID: G03-PRODUCT_MARGIN-Q025
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user with visibility of the margin figure but not the underlying cost value must not be able
  to derive the cost from the margin and revenue figures both being visible to them.
WHY_IT_MATTERS: >
  Exposing two of three linked figures effectively exposes the third, defeating the intent of
  restricting cost visibility.
DISCONFIRMING_OBSERVATION: >
  A user permitted to see margin and revenue, but not cost, can arithmetically reconstruct the
  cost figure from what is shown to them.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user with margin and revenue visibility but no cost visibility, attempt to derive the cost
  value for a transaction from the figures displayed.
```

## G03-PRODUCT_MARGIN-Q026

```yaml
QID: G03-PRODUCT_MARGIN-Q026
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Permission to see cost and permission to see margin must be independently configurable grants,
  not bundled into a single permission that always grants or denies both together.
WHY_IT_MATTERS: >
  Bundling the two removes the business's ability to give a role visibility into profitability
  without exposing raw cost data, or vice versa.
DISCONFIRMING_OBSERVATION: >
  Granting or revoking one of cost visibility or margin visibility for a role always changes the
  other as well, with no way to configure them independently.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Attempt to configure a role with margin visibility but not cost visibility, and a separate role
  with the reverse, and verify both are independently achievable.
```

## G03-PRODUCT_MARGIN-Q027

```yaml
QID: G03-PRODUCT_MARGIN-Q027
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A report or list view that includes margin as a column must enforce the same cost-visibility
  restriction that the single-record detail view enforces, not expose the figure more broadly.
WHY_IT_MATTERS: >
  A restriction enforced on one view and not another is not a restriction at all, only an
  inconvenience.
DISCONFIRMING_OBSERVATION: >
  A user denied margin visibility on a single-record detail view can still see a margin column in
  a list or report view.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  As a user without margin visibility, open both a single-record detail view and a list or report
  view that includes margin as a column.
```

## G03-PRODUCT_MARGIN-Q028

```yaml
QID: G03-PRODUCT_MARGIN-Q028
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A user denied margin visibility on the primary screen must not be able to reach the same figure
  through a different supported path, such as an export, an alternate report, or an integration.
WHY_IT_MATTERS: >
  A restriction that only covers one entry point is trivially bypassed through any other path to
  the same data.
DISCONFIRMING_OBSERVATION: >
  A user denied margin visibility on the primary screen can obtain the same figure through an
  export, an alternate report, or an API response.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  As a user without margin visibility, attempt to obtain the figure through every alternate
  supported path available to that role.
```

## G03-PRODUCT_MARGIN-Q029

```yaml
QID: G03-PRODUCT_MARGIN-Q029
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Revoking a user's cost or margin visibility must take effect on views that are already open or
  cached for that user, not only on views opened after the revocation.
WHY_IT_MATTERS: >
  A revocation that leaves an already-open view unaffected gives a false sense that access was
  actually cut off.
DISCONFIRMING_OBSERVATION: >
  A user whose cost or margin visibility was revoked can still see the figure in a view that was
  already open at the moment of revocation.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Open a margin-containing view as a user, revoke that user's margin visibility, and observe
  whether the already-open view still shows the figure.
```

## G03-PRODUCT_MARGIN-Q030

```yaml
QID: G03-PRODUCT_MARGIN-Q030
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A scheduled or automated distribution of a report, such as an emailed or exported file, must
  honor the actual recipient's margin-visibility permission, not the permission of the user who
  configured the schedule.
WHY_IT_MATTERS: >
  A schedule configured by a privileged user must not become a channel that leaks restricted data
  to a less-privileged recipient.
DISCONFIRMING_OBSERVATION: >
  A scheduled report containing margin figures is delivered to a recipient who does not personally
  have margin-visibility permission.
EXPECTED_SURFACE: S3,S4,S8
PRECONDITIONS: >
  Configure a scheduled report containing margin data with a privileged configurer and a recipient
  who lacks margin visibility, and inspect the delivered content.
```

## G03-PRODUCT_MARGIN-Q031

```yaml
QID: G03-PRODUCT_MARGIN-Q031
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Exporting transaction data to a file or spreadsheet must exclude the margin or cost figure for a
  user who lacks visibility of it on screen.
WHY_IT_MATTERS: >
  An export is a supported path and must not become the one place a restriction is forgotten.
DISCONFIRMING_OBSERVATION: >
  A file exported by a user without margin or cost visibility contains that figure anyway.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  As a user without margin visibility, export a set of transactions to a file and inspect its
  contents for the restricted figure.
```

## G03-PRODUCT_MARGIN-Q032

```yaml
QID: G03-PRODUCT_MARGIN-Q032
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An export that includes both revenue and a cost-derived figure together must be logged as a
  distinct, identifiable event from an export of revenue alone, given the combination's greater
  sensitivity.
WHY_IT_MATTERS: >
  Without a distinct log entry, a governance review cannot tell how often the more sensitive
  combined data actually left the system.
DISCONFIRMING_OBSERVATION: >
  The audit log for an export containing both revenue and cost-derived data is indistinguishable
  from the log entry for an export of revenue alone.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Perform one export of revenue only and one export including a cost-derived figure, then compare
  the resulting audit log entries.
```

## G03-PRODUCT_MARGIN-Q033

```yaml
QID: G03-PRODUCT_MARGIN-Q033
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A saved or shared filter, view, or report definition that includes margin must not itself grant
  margin visibility to a user it is shared with beyond that user's own underlying permission.
WHY_IT_MATTERS: >
  A shared view must not become an indirect way to hand out a permission the sharer does not
  control.
DISCONFIRMING_OBSERVATION: >
  A user without margin-visibility permission can see margin data by opening a saved view or
  filter shared by a user who does have that permission.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a privileged user, save and share a view containing margin data with a user lacking margin
  visibility, then open that shared view as the recipient.
```

## G03-PRODUCT_MARGIN-Q034

```yaml
QID: G03-PRODUCT_MARGIN-Q034
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Any manual override of a margin input, such as cost, price, or allocation, must be individually
  attributable to a specific user and timestamp, not merged into an anonymous batch change.
WHY_IT_MATTERS: >
  Unattributed overrides make it impossible to question or correct the person who made a specific
  pricing or costing decision.
DISCONFIRMING_OBSERVATION: >
  A margin-input override applied as part of a batch operation cannot be traced to the individual
  user who authorized or triggered it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform a batch update that overrides a margin input for several transactions and inspect the
  resulting attribution in the audit trail.
```

## G03-PRODUCT_MARGIN-Q035

```yaml
QID: G03-PRODUCT_MARGIN-Q035
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The audit trail for a margin-affecting change must record the value before and after the change,
  not merely the fact that a change occurred.
WHY_IT_MATTERS: >
  Knowing only that a change happened, without the before and after values, makes the audit record
  useless for reconstructing what actually happened.
DISCONFIRMING_OBSERVATION: >
  The audit entry for a margin-affecting change shows that a change occurred but does not retain
  the prior or new value.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a margin-affecting input and inspect exactly what the audit trail records about the
  before and after state.
```

## G03-PRODUCT_MARGIN-Q036

```yaml
QID: G03-PRODUCT_MARGIN-Q036
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A margin figure derived through an external integration, such as an e-commerce channel
  connector, must be subject to the same access and audit controls as one derived through the
  primary interface.
WHY_IT_MATTERS: >
  An integration path that bypasses the platform's own controls creates an unmonitored side door
  to sensitive data.
DISCONFIRMING_OBSERVATION: >
  Margin data reaches or is derivable through an external integration without the access
  restriction or audit logging that applies to the primary interface.
EXPECTED_SURFACE: S1,S3,S4,S6
PRECONDITIONS: >
  Trace how margin-relevant data flows through an external integration and compare the access and
  audit controls applied there to those on the primary interface.
```

## G03-PRODUCT_MARGIN-Q037

```yaml
QID: G03-PRODUCT_MARGIN-Q037
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scheduled background recomputation of margin figures must read its cost and revenue inputs
  from a single, consistent point in time within one pass, not from two different points in time.
WHY_IT_MATTERS: >
  Mixing inputs from different moments within a single pass produces internally inconsistent
  figures that cannot be explained by any single valid state.
DISCONFIRMING_OBSERVATION: >
  Within one recomputation pass, some transactions reflect a cost or price update made mid-pass
  while others in the same pass do not.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a background recomputation and make a cost or price change while it is running, then
  inspect whether the change is applied consistently across the whole pass.
```

## G03-PRODUCT_MARGIN-Q038

```yaml
QID: G03-PRODUCT_MARGIN-Q038
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two concurrent edits, one to the cost basis and one to the transaction price, occurring before
  either is saved, must not silently produce a margin based on only one of the two changes.
WHY_IT_MATTERS: >
  A margin silently based on a stale half of two concurrent edits misstates the transaction
  without any error being raised.
DISCONFIRMING_OBSERVATION: >
  After two concurrent edits to cost and price are both saved, the resulting margin reflects only
  one of the two changes.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Open the same transaction in two sessions, change cost in one and price in the other before
  either saves, then save both and inspect the resulting margin.
```

## G03-PRODUCT_MARGIN-Q039

```yaml
QID: G03-PRODUCT_MARGIN-Q039
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A background recomputation of margin figures that fails partway through must not leave some
  transactions restated and others not without flagging that a partial run occurred.
WHY_IT_MATTERS: >
  An unflagged partial run leaves the dataset in an inconsistent, undetectable mixed state.
DISCONFIRMING_OBSERVATION: >
  After an interrupted background recomputation, some transactions show updated figures and others
  do not, with no indication that the run was incomplete.
EXPECTED_SURFACE: S1,S8,S6
PRECONDITIONS: >
  Interrupt a background margin-recomputation job partway through and inspect the resulting state
  of transactions processed versus not yet processed.
```

## G03-PRODUCT_MARGIN-Q040

```yaml
QID: G03-PRODUCT_MARGIN-Q040
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Changing a company-wide cost valuation method must explicitly define whether existing margin
  figures are recomputed under the new method, frozen under the prior method, or flagged as
  computed under a superseded method.
WHY_IT_MATTERS: >
  Leaving this undefined means nobody, including the business itself, can say what method any
  given historical figure actually reflects.
DISCONFIRMING_OBSERVATION: >
  After a company-wide valuation-method change, historical margin figures show no indication of
  which valuation method actually produced them.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change the company-wide cost valuation method and inspect how historical margin figures are
  labeled or treated afterward.
```

## G03-PRODUCT_MARGIN-Q041

```yaml
QID: G03-PRODUCT_MARGIN-Q041
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A margin figure requested while a background recomputation job is actively running must not
  return a value that mixes pre-job and post-job inputs for the same transaction.
WHY_IT_MATTERS: >
  A figure blending two computation states for one transaction is not a valid value under either
  state.
DISCONFIRMING_OBSERVATION: >
  A margin figure retrieved while a recomputation job is in progress does not match either the
  pre-job or the post-job value once the job completes.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Request a specific transaction's margin figure while a background recomputation job is actively
  running, then compare it to the value before and after the job.
```

## G03-PRODUCT_MARGIN-Q042

```yaml
QID: G03-PRODUCT_MARGIN-Q042
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The timing of the last background margin-recomputation pass must be visible or otherwise
  knowable, so a potentially stale figure can be distinguished from a freshly computed one.
WHY_IT_MATTERS: >
  Without a last-run indicator, a user cannot judge how much to trust a displayed margin figure's
  currency.
DISCONFIRMING_OBSERVATION: >
  There is no way, anywhere in the system, to determine when a displayed margin figure was last
  recomputed.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Locate a margin figure on a record and attempt to determine, through any available means, when
  it was last computed.
```

## G03-PRODUCT_MARGIN-Q043

```yaml
QID: G03-PRODUCT_MARGIN-Q043
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A tenant's margin figures and underlying cost data must never be reachable, even in aggregate or
  summarized form, by a report or process running in the context of a different tenant.
WHY_IT_MATTERS: >
  Cross-tenant leakage of financial figures, even aggregated, breaks the isolation guarantee the
  platform is built on.
DISCONFIRMING_OBSERVATION: >
  A report or aggregate figure generated in one tenant's context includes, even indirectly, margin
  or cost data originating from another tenant.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Generate an aggregate margin report in one tenant's context and verify it contains no data
  traceable to a different tenant.
```

## G03-PRODUCT_MARGIN-Q044

```yaml
QID: G03-PRODUCT_MARGIN-Q044
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Archiving or deactivating a product with transactional history must not remove or hide the
  margin figures already computed for its historical transactions.
WHY_IT_MATTERS: >
  Deactivation is meant to stop future use, not erase the historical record needed for past-period
  reporting.
DISCONFIRMING_OBSERVATION: >
  Historical margin figures for a product's past transactions become inaccessible or disappear
  after the product is archived or deactivated.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Archive or deactivate a product that has completed transaction history, then attempt to retrieve
  the margin figures for its historical transactions.
```

## G03-PRODUCT_MARGIN-Q045

```yaml
QID: G03-PRODUCT_MARGIN-Q045
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A bulk price or cost update applied to many products at once must produce margin changes that
  are individually traceable to the specific bulk operation that caused them.
WHY_IT_MATTERS: >
  An untraceable bulk-caused shift in many margin figures at once makes it impossible to identify
  or reverse the cause of an anomaly.
DISCONFIRMING_OBSERVATION: >
  Margin figures for several products change following a bulk update, but no record identifies the
  specific bulk operation responsible for the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a bulk price or cost update to multiple products at once and attempt to trace the
  resulting margin changes back to that specific operation.
```

## G03-PRODUCT_MARGIN-Q046

```yaml
QID: G03-PRODUCT_MARGIN-Q046
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A transaction line with a manually entered price of zero, such as a deliberate promotional
  giveaway, must produce a margin state that is explicit about the deliberate zero, not
  indistinguishable from a data-entry error.
WHY_IT_MATTERS: >
  An indistinguishable zero-price line makes it impossible to separate genuine giveaways from
  costly mistakes in a margin review.
DISCONFIRMING_OBSERVATION: >
  A deliberately zero-priced promotional line and an accidental zero-priced line produce identical
  margin records with no distinguishing indicator.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Enter one deliberate zero-price promotional line and, separately, simulate an accidental zero-
  price entry, then compare the resulting margin records.
```

## G03-PRODUCT_MARGIN-Q047

```yaml
QID: G03-PRODUCT_MARGIN-Q047
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing a product's income or expense account at the account or category level, intended only
  for future accounting classification, must not silently shift previously computed margin
  figures.
WHY_IT_MATTERS: >
  A reclassification meant to apply going forward should not retroactively rewrite historical
  management numbers.
DISCONFIRMING_OBSERVATION: >
  Previously computed margin figures for past transactions change after only the account
  classification for future transactions was updated.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Change a product or category's income or expense account and inspect whether previously computed
  historical margin figures are affected.
```

## G03-PRODUCT_MARGIN-Q048

```yaml
QID: G03-PRODUCT_MARGIN-Q048
MODULE: product_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A margin figure for a document that spans multiple companies or branches must be attributed to
  the correct company or branch boundary, not reported once and duplicated or omitted in either
  boundary's own report.
WHY_IT_MATTERS: >
  Incorrect attribution across boundaries either overstates one entity's results or silently drops
  the transaction from both.
DISCONFIRMING_OBSERVATION: >
  The same cross-boundary document's margin appears in both companies' reports in full, or in
  neither, rather than correctly attributed or apportioned.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Create a transaction spanning two companies or branches and inspect how its margin is reflected
  in each entity's own report.
```

