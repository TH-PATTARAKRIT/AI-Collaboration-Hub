# SMEsPlus ENTERPRISE SUITE
## GMVQ — G15 PRODUCTIVITY / spreadsheet_dashboard_stock_account Module Bridge MVQ Bank

**Document ID:** GMVQ-G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-MVQ48-V1.00
**Group:** G15 PRODUCTIVITY
**Module Metadata:** `spreadsheet_dashboard_stock_account`
**Wave:** W4 (GMVQ 25-Team Acceleration, 2026-09-27)
**Author Cell:** P15-3 (GMVQ Question Factory — Production Cell P15-3)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `spreadsheet_dashboard_stock_account`, treated per GROUP_BRIEF_G15_PRODUCTIVITY.md as a two-participant seam: the live dashboard reporting layer, and the combined stock-quantity-plus-ledger-valuation domain treated as one accounting-of-stock party (not three separately-counted parties). Every question below requires both the reporting layer and the combined stock/valuation domain simultaneously — a question that would still make sense as a pure stock-quantity or pure ledger-valuation question with the reporting layer removed does not belong here and was cut. This bank is deliberately distinct from G12's `project_stock_account` bank: that bank's seam is project-linkage (work-in-progress capitalisation, cost matched against a funding order), while this bank's seam is reporting-layer exposure (what a live or scheduled aggregation widget shows, to whom, and how current it is) — no question here restates a project-linkage hypothesis, and no question there is duplicated here. The material ground worked is staleness between the physical-quantity and posted-valuation refresh cycles, permission leakage through aggregation and drill-through, real-time-versus-batch mismatch, and cross-record rollup exposure — the four failure classes named in the Group Brief — plus revaluation, reversal, multi-currency, multi-company and cross-tenant handling of the combined reporting layer.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure state, never a restatement of its own hypothesis.
- Arity control: every question requires the dashboard/reporting layer AND the combined stock-quantity/valuation domain simultaneously; a question answerable by either alone, or by the project-linkage seam already owned by G12, was rewritten to add the missing dependency or cut.
- No padding: 48 questions exist because each tests a distinct material seam hypothesis, spread across the required dimensions (business rule, state transition, configuration dependency, role and permission, exception path, cancellation, reversal, negative case, cross-module dependency, auditability, tenant/company boundary, concurrency and ordering, runtime reachability).
- Question text is source-neutral: no vendor or product name, no technical identifier, and the module's own metadata name never appears outside the `MODULE:` field.
- Checked against the Bridge Module Rule's seam dimensions before being kept, and specifically checked against duplicating G12's `project_stock_account` bank's HYPOTHESIS lines: this bank never asks about work-in-progress capitalisation, project cost matching, or a funding order — that ground belongs to G12.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.

## Questions

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q001

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q001
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combined stock-value widget does not present its valuation figure as final before the corresponding accounting entry for a stock movement has actually posted.
WHY_IT_MATTERS: >
  Presenting an unposted valuation as final would mislead a viewer into treating provisional value as confirmed.
DISCONFIRMING_OBSERVATION: >
  The combined widget shows a stock valuation figure with no provisional label even though the underlying accounting entry has not yet posted.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a stock movement whose accounting entry has not yet posted, and check whether the combined widget presents the resulting valuation as final.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q002

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q002
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A viewer permitted to see an aggregate total stock value widget but not individual item cost prices cannot use a narrow category filter, down to a single low-count item, to back-calculate that item's unit cost.
WHY_IT_MATTERS: >
  A rollup narrowed to one item functions as an individual cost disclosure and defeats aggregate-only permission.
DISCONFIRMING_OBSERVATION: >
  Narrowing the combined widget's filter to a single low-count item reveals that item's unit cost to a viewer without item-cost permission.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Grant a user permission to view only aggregate stock value, narrow the combined widget's filter to a single low-count item, and check whether its unit cost becomes visible.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q003

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q003
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The combined widget's on-hand quantity figure and its valuation figure, when drawn from refresh cycles of different ages, are not presented as though both were captured at the same moment.
WHY_IT_MATTERS: >
  Presenting two figures of different ages as one coherent snapshot would mislead a viewer about how current the combined picture actually is.
DISCONFIRMING_OBSERVATION: >
  The widget shows on-hand quantity and valuation figures of visibly different refresh ages with no indication of the age mismatch.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a refresh of only the stock-quantity side or only the valuation side of a combined widget, and check whether the displayed figure indicates the resulting age mismatch.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q004

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q004
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a stock valuation method change is applied, the combined dashboard's historical trend for prior periods retains the valuation as originally computed, rather than silently restating history without a record that a revaluation occurred.
WHY_IT_MATTERS: >
  Silently restating closed historical figures would erase a legitimate past record and hide the fact that a deliberate revaluation happened.
DISCONFIRMING_OBSERVATION: >
  After a valuation method change, the combined widget's historical trend for prior periods changes with no record that a revaluation occurred.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Apply a stock valuation method change, then check whether the combined widget's historical trend for periods before the change remains as originally computed and traceable.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q005

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q005
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined widget scoped to a warehouse or branch does not surface another branch's item-level cost figures through a company-wide summary rollup shown to a viewer who lacks permission to see that branch's detail.
WHY_IT_MATTERS: >
  A company-wide summary that leaks another branch's item-level detail would defeat the branch-level scoping.
DISCONFIRMING_OBSERVATION: >
  A viewer without permission for another branch can see that branch's item-level cost figures through a company-wide summary rollup.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Scope a viewer's permission to one branch only, view a company-wide summary rollup, and check whether another branch's item-level detail is visible.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q006

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q006
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a stock count adjustment is entered but its accounting write-off has not yet posted, the combined dashboard's stock value figure does not present the adjusted quantity as already reflected in the ledger-confirmed valuation.
WHY_IT_MATTERS: >
  Showing an unposted adjustment as already confirmed would overstate the reliability of the displayed valuation.
DISCONFIRMING_OBSERVATION: >
  The combined widget's valuation figure already reflects a stock count adjustment whose accounting write-off has not yet posted.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Enter a stock count adjustment before its accounting write-off posts, and check whether the combined widget's valuation figure already reflects it as confirmed.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q007

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q007
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Exporting a combined stock-value dashboard to a shared file applies the same permission-based filtering the live widget applies, rather than exposing full unfiltered item-cost detail to whoever receives the export.
WHY_IT_MATTERS: >
  An export that bypasses live-view filtering would hand a recipient more cost detail than the dashboard itself ever showed them.
DISCONFIRMING_OBSERVATION: >
  An exported copy of the combined widget contains item-level cost detail that the same viewer's live widget never displayed.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Export a combined widget to a file as a user with aggregate-only permission, and compare the exported content against what the live widget shows that same user.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q008

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q008
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined widget aggregating value for a category with very few distinct items does not let a viewer with only aggregate-level permission infer a single item's unit cost from successive totals as stock quantity changes.
WHY_IT_MATTERS: >
  Successive small-category totals can reveal an item's unit cost through subtraction even when no single figure names that item directly.
DISCONFIRMING_OBSERVATION: >
  Comparing the combined category total before and after a quantity change reveals a single item's unit cost to a viewer without item-level permission.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Change the quantity of one item in a small category feeding a combined widget, and check whether comparing totals before and after reveals that item's unit cost.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q009

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q009
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Deleting an item that already has combined dashboard history referencing it leaves that historical valuation rollup intact and correctly referenced, rather than the widget erroring or silently reporting a zero value for prior periods.
WHY_IT_MATTERS: >
  Losing or zeroing historical figures on deletion would destroy a legitimate record of past valuation for no operational reason.
DISCONFIRMING_OBSERVATION: >
  After an item is deleted, the combined widget's historical rollup for that item either errors or reports zero instead of preserving the original figures.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Delete an item that has existing combined dashboard history, and check whether that history remains visible and correctly referenced.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q010

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q010
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a stock transfer between two company entities has not yet had its inter-company accounting entry posted, the combined dashboard does not show the receiving entity's stock value as already including the transferred goods' confirmed cost.
WHY_IT_MATTERS: >
  Recognizing the cost early would let one entity's books claim confirmed value before the entities involved formalized the transaction between them.
DISCONFIRMING_OBSERVATION: >
  The receiving entity's combined widget shows the transferred goods' confirmed cost before the corresponding inter-company entry has posted.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Transfer stock between two company entities ahead of posting the inter-company accounting entry, and check whether the receiving entity's combined widget already shows confirmed value.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q011

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q011
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A combined widget's cache invalidation triggered by an accounting-side revaluation also invalidates the stock-quantity portion of the same cached rollup where the two are shown together, rather than updating only the value half.
WHY_IT_MATTERS: >
  Updating only one half of a cached combined figure would leave quantity and value permanently out of step after a revaluation.
DISCONFIRMING_OBSERVATION: >
  After a revaluation triggers cache invalidation, the combined widget's value figure updates but its quantity figure continues to reflect the stale cached value.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger an accounting revaluation that invalidates a combined widget's cache, and check whether both the value and quantity portions of the rollup are refreshed.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q012

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q012
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where two valuation layers exist for the same item, the combined widget's blended average value figure is computed from a documented, consistent method rather than arbitrarily picking one layer's cost to represent the whole quantity.
WHY_IT_MATTERS: >
  Arbitrarily picking one layer's cost would misstate the true blended value of stock actually held across two different cost layers.
DISCONFIRMING_OBSERVATION: >
  The combined widget's blended value figure for an item with two valuation layers matches only one layer's unit cost rather than a documented blend of both.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Hold stock for one item across two valuation layers with different unit costs, and check which cost the combined widget's blended value figure actually reflects.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q013

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q013
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A combined widget's real-time indicator, where present, correctly identifies which half of the figure, quantity or value, is actually live versus last-batch, rather than a single unqualified live label covering only one side.
WHY_IT_MATTERS: >
  An unqualified live label covering a partially batched figure would overstate how current the displayed information actually is.
DISCONFIRMING_OBSERVATION: >
  The widget's live indicator applies to the whole combined figure even though only the quantity side or only the value side actually refreshes in real time.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure one side of a combined widget's data source to refresh in real time and the other on a batch schedule, and check what the widget's live indicator actually communicates.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q014

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q014
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a stock write-off is reversed after the combined dashboard already reflected the original write-off, the widget's historical figure for the original period is preserved as originally computed while a new period reflects the reversal.
WHY_IT_MATTERS: >
  Silently rewriting the original period's history would erase the record of what was actually reported at the time the write-off occurred.
DISCONFIRMING_OBSERVATION: >
  After a write-off reversal, the combined widget's figure for the original write-off period changes rather than a new period showing the reversal.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Reverse a stock write-off after the combined dashboard already reflected the original write-off in a closed period, and check which period the reversal is shown in.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q015

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q015
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined dashboard comparing stock value across multiple warehouses does not allow a viewer permitted to see only their own warehouse's row to infer another warehouse's exact value from a visible company-wide total change when the total includes only two warehouses.
WHY_IT_MATTERS: >
  A two-warehouse total that shifts predictably with one warehouse's change functions as an individual disclosure of the other's figure.
DISCONFIRMING_OBSERVATION: >
  A viewer permitted to see only their own warehouse's row can determine the other warehouse's exact value from a change in the visible two-warehouse company total.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  In a two-warehouse setup, change one warehouse's stock value and check whether a viewer scoped to the other warehouse can infer the change from the company-wide total.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q016

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q016
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a stock item's standard cost is changed, the combined dashboard's already-closed historical periods retain the valuation as computed at the time, rather than the standard-cost change silently retroactively repricing closed-period history.
WHY_IT_MATTERS: >
  Retroactively repricing closed-period history would change previously reported valuation with no one having decided to restate it.
DISCONFIRMING_OBSERVATION: >
  After a standard-cost change, the combined widget's already-closed historical periods show the item revalued at the new standard cost.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Change an item's standard cost after a historical period using the prior cost has already closed, and check whether that closed period's valuation changes.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q017

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q017
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined widget's drill-through from an aggregate stock-value cell to underlying item-level detail respects the same row-level permission scoping as the aggregate view itself, rather than exposing full unfiltered item cost records to any viewer who can see the aggregate.
WHY_IT_MATTERS: >
  A drill-through that bypasses row-level scoping would let any viewer of the aggregate reach cost detail their permission was never meant to grant.
DISCONFIRMING_OBSERVATION: >
  Drilling through an aggregate stock-value cell exposes unfiltered item cost records to a viewer whose row-level permission is narrower than the aggregate they can see.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Grant a user narrower row-level permission than the aggregate combined widget they can view, drill through a rollup cell, and check whether unfiltered item cost detail becomes visible.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q018

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q018
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a stock movement is recorded but later found to be a duplicate and reversed, the combined dashboard's value figure for the period in which the duplicate was reversed reflects the correction.
WHY_IT_MATTERS: >
  Continuing to count a duplicate movement's value indefinitely would overstate the true stock value for no operational reason.
DISCONFIRMING_OBSERVATION: >
  After a duplicate stock movement is reversed, the combined widget's value figure continues to include the duplicate's value past the period of the reversal.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a duplicate stock movement, reverse it, and check whether the combined widget's value figure for the reversal period reflects the correction.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q019

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q019
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A combined dashboard's currency handling, where stock is valued internally in one currency and a summary is shown in another reporting currency, uses one documented, consistently applied conversion moment across the same rollup rather than mixing rates within it.
WHY_IT_MATTERS: >
  Mixing conversion moments within one rollup would make the combined value figure numerically incoherent even though every underlying amount is individually correct.
DISCONFIRMING_OBSERVATION: >
  Two items shown in the same combined value rollup are converted between internal and reporting currencies using different exchange-rate moments.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Hold stock valued internally in one currency for a summary shown in another reporting currency, and compare the conversion basis used across items in the same combined widget.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q020

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q020
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a stock item is reclassified from one valuation category to another, the combined dashboard's trend line for that item shows the transition rather than blending pre- and post-reclassification values into one indistinguishable figure.
WHY_IT_MATTERS: >
  Blending the two categories' values would erase the record of a real change in how the item is treated.
DISCONFIRMING_OBSERVATION: >
  After a reclassification, the combined widget's trend line for that item blends pre- and post-reclassification values with no visible transition point.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reclassify a stock item's valuation category mid-period, and check whether the combined widget's trend line shows the transition or blends the two categories.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q021

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q021
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined widget aggregating stock value by product category does not let a viewer permitted to see only the category-level summary infer an individual item's exact value when the category happens to contain only one item.
WHY_IT_MATTERS: >
  A category summary that degenerates to a single item's figure functions as a direct disclosure despite being presented as an aggregate.
DISCONFIRMING_OBSERVATION: >
  A category-level summary total, for a category containing only one item, reveals that item's exact value to a viewer not permitted to see individual item detail.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  View the category-level combined summary for a category containing only one item, and check whether the summary discloses that item's exact individual value.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q022

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q022
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a stock count is performed mid-period and adjustments are still pending review, the combined dashboard labels the interim value as provisional rather than presenting it identically to a fully reconciled, reviewed figure.
WHY_IT_MATTERS: >
  Presenting an unreviewed interim figure as fully reconciled would overstate the reliability of a value still under review.
DISCONFIRMING_OBSERVATION: >
  The combined widget presents a mid-period stock count's interim value with no provisional label, identical in presentation to a fully reconciled figure.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Perform a mid-period stock count with adjustments still pending review, and check whether the combined widget labels the resulting value as provisional.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q023

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q023
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined dashboard's scheduled export to an external stakeholder does not include a live query link that, if opened, would bypass the export's point-in-time permission filtering and expose current unfiltered stock and cost data.
WHY_IT_MATTERS: >
  A live query link embedded in an export would let a recipient bypass the filtering the export itself was meant to enforce.
DISCONFIRMING_OBSERVATION: >
  Opening a live query link embedded in a scheduled export exposes current, unfiltered stock and cost data beyond what the export's own point-in-time filtering allowed.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Generate a scheduled export of a combined stock-value widget for an external stakeholder, and check whether it contains a live query link that bypasses the export's own filtering.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q024

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q024
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a returned item is received back into stock after a related accounting credit was already posted for the original sale, the combined widget reconciles the returned quantity and its value consistently on both sides.
WHY_IT_MATTERS: >
  Reconciling only one side would leave the combined figure showing a credit with no matching quantity, or a quantity with no matching credit.
DISCONFIRMING_OBSERVATION: >
  The combined widget shows the accounting credit for a return posted while the returned quantity has not yet reappeared in stock, or the reverse, with no reconciliation note.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post an accounting credit for a sale return before the returned item is received back into stock, and check whether the combined widget reconciles the quantity and value sides.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q025

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q025
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A combined widget's handling of negative stock, where an item is oversold before replenishment, does not present a nonsensical or silently zeroed valuation figure without a documented treatment for the negative-quantity state.
WHY_IT_MATTERS: >
  An unexplained zeroed or nonsensical figure would look like a data error rather than a deliberately handled edge case.
DISCONFIRMING_OBSERVATION: >
  The combined widget shows a zeroed or nonsensical valuation for an item in a negative-stock state with no documented treatment referenced.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Oversell an item into a negative-stock state before replenishment, and check how the combined widget's valuation figure handles the negative quantity.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q026

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q026
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a stock item is moved between two valuation methods' scope mid-period, the combined dashboard attributes value consistently to one documented method for that period rather than switching methods mid-rollup with no note.
WHY_IT_MATTERS: >
  An unexplained mid-period method switch would make the resulting figure impossible to interpret against either method consistently.
DISCONFIRMING_OBSERVATION: >
  The combined widget's value figure for an item switched between valuation methods mid-period blends both methods within the same period with no note of the switch.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Move a stock item between two valuation methods' scope mid-period, and check whether the combined widget attributes that period's value to one documented method or blends both.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q027

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q027
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A combined dashboard's period-boundary handling attributes a stock movement's value to one documented accounting period consistently between the physical stock record and the ledger-side rollup, not different periods on each side.
WHY_IT_MATTERS: >
  Attributing the same movement to different periods on each side would make period-based valuation figures internally inconsistent.
DISCONFIRMING_OBSERVATION: >
  A stock movement recorded near a period cutoff is attributed to one period on the physical stock record and a different period on the ledger-side rollup.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a stock movement near a period cutoff, and compare which accounting period the physical stock record and the ledger-side rollup each attribute it to.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q028

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q028
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a stock item's cost is adjusted downward due to obsolescence, the combined dashboard's write-down is distinguishable in the figure from an ordinary valuation fluctuation.
WHY_IT_MATTERS: >
  An indistinguishable write-down would hide a deliberate obsolescence decision inside what looks like routine valuation movement.
DISCONFIRMING_OBSERVATION: >
  A deliberate obsolescence write-down appears in the combined widget identically to an ordinary valuation fluctuation, with no distinguishing marker.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply an obsolescence write-down to an item's cost, and check whether the combined widget's figure distinguishes it from an ordinary valuation fluctuation.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q029

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q029
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined widget's handling of consignment or non-owned stock does not include that stock's value in a company's own owned-asset valuation total unless a documented rule states it should.
WHY_IT_MATTERS: >
  Including non-owned stock in an owned-asset total would overstate the company's actual owned inventory value.
DISCONFIRMING_OBSERVATION: >
  The combined widget's owned-asset valuation total includes consignment or non-owned stock's value with no documented rule permitting it.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Hold consignment or otherwise non-owned stock alongside owned inventory, and check whether the combined widget's owned-asset valuation total includes the non-owned stock's value.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q030

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q030
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a stock adjustment is entered by one user and later reversed by another, the combined dashboard's audit-facing detail shows both actions distinctly, rather than presenting only the net effect with no trace that a reversal occurred.
WHY_IT_MATTERS: >
  Showing only the net effect would hide a real sequence of actions from anyone auditing how a figure reached its current state.
DISCONFIRMING_OBSERVATION: >
  The combined widget's audit-facing detail for a reversed adjustment shows only the net effect with no separate record of the original entry and its reversal.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have one user enter a stock adjustment and another reverse it, and check whether the combined widget's audit-facing detail shows both actions distinctly.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q031

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q031
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined dashboard's handling of a stock item held in a bonded, quarantine, or otherwise restricted status does not include that item's full value in a generally available valuation total shown to a viewer without permission to know the restriction exists.
WHY_IT_MATTERS: >
  Including a restricted item's value in a general total would leak the existence of a restricted holding to a viewer never meant to know about it.
DISCONFIRMING_OBSERVATION: >
  A viewer without permission to know about a restricted-status item can nonetheless see its value reflected in a generally available combined valuation total.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Place an item in a bonded, quarantine, or otherwise restricted status, and check whether its value appears in a generally available combined valuation total to an unauthorized viewer.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q032

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q032
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a company-wide combined dashboard is cloned into a new tenant during a setup or migration process, the cloned widget definition does not retain any live reference back to the source tenant's actual stock or account records.
WHY_IT_MATTERS: >
  A live cross-tenant reference would leak one customer's actual stock and cost data into a different customer's dashboard.
DISCONFIRMING_OBSERVATION: >
  A cloned combined widget in a new tenant displays live data originating from the source tenant's actual stock or account records.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Clone a combined stock-account widget definition from one tenant into another during setup or migration, and check whether the cloned widget resolves to the source tenant's live data.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q033

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q033
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A combined widget's projected month-end stock value, based on pending but unposted transactions, is clearly distinguished from the confirmed, already-posted valuation shown in the same widget.
WHY_IT_MATTERS: >
  Blending a forecast with a confirmed figure would make it impossible to tell how much of the displayed value is actually settled.
DISCONFIRMING_OBSERVATION: >
  The combined widget shows a projected month-end value blended into the same figure as the confirmed, already-posted valuation with no distinction.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Have pending, unposted transactions alongside confirmed postings for month-end stock value, and check whether the combined widget distinguishes the projected figure from the confirmed one.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q034

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q034
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a stock revaluation is applied retroactively with proper authorization, the combined dashboard's audit trail records who applied it and when.
WHY_IT_MATTERS: >
  An untraceable retroactive change would make it impossible to hold anyone accountable for altering a historical figure.
DISCONFIRMING_OBSERVATION: >
  After an authorized retroactive revaluation, the combined widget's historical figure changes with no audit trail record of who applied it or when.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply an authorized retroactive stock revaluation, and check whether the combined widget's audit trail records who applied it and when.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q035

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q035
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A combined widget's total value figure for a multi-currency stock pool does not silently omit an item priced in a currency the widget's default display currency lacks a conversion rate for.
WHY_IT_MATTERS: >
  Silently omitting an item would understate the true total value with no indication that anything was left out.
DISCONFIRMING_OBSERVATION: >
  The combined widget's total value figure for a multi-currency pool omits an item whose currency lacks a conversion rate, with no flag indicating the omission.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Include in a stock pool an item priced in a currency the widget's display currency lacks a conversion rate for, and check whether the combined total silently omits it.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q036

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q036
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a stock count discrepancy is under active investigation and not yet resolved, the combined dashboard labels the affected item's value as under review rather than presenting it with the same confidence as a fully reconciled item.
WHY_IT_MATTERS: >
  Presenting a disputed figure with full confidence would mislead a viewer about how reliable that particular value actually is.
DISCONFIRMING_OBSERVATION: >
  The combined widget shows an item under active count-discrepancy investigation with the same presentation as a fully reconciled item, with no under-review label.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place an item's stock count under active investigation for a discrepancy, and check whether the combined widget labels its value as under review.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q037

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q037
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A combined dashboard's handling of a stock item moved between two branches using different valuation configurations reconciles the two configurations' figures at the point of transfer rather than silently applying the destination's configuration retroactively.
WHY_IT_MATTERS: >
  Retroactively applying the destination's configuration would misstate the value the item actually accrued at the source branch.
DISCONFIRMING_OBSERVATION: >
  After a cross-branch transfer between differently configured branches, the combined widget applies the destination's valuation configuration retroactively to value accrued at the source.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Transfer a stock item between two branches with different valuation configurations, and check whether the combined widget reconciles the transition or retroactively reconfigures the source value.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q038

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q038
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an accounting period is closed while a related stock movement's posting is still pending, the combined dashboard flags the discrepancy for that period rather than silently including the pending movement's value in the closed period's final figure.
WHY_IT_MATTERS: >
  Silently including a pending movement would let a closed period's reported figure change after the fact with no flag that anything was outstanding.
DISCONFIRMING_OBSERVATION: >
  The combined widget's closed-period figure silently includes a stock movement whose posting was still pending at the time of closure, with no flag.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Close an accounting period while a related stock movement's posting is still pending, and check whether the combined widget flags the resulting discrepancy for that period.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q039

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q039
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined widget's row-level access for a category manager scoped to only their assigned product categories does not surface another category's item-level value figures through a shared company-wide summary total.
WHY_IT_MATTERS: >
  A shared summary that leaks out-of-scope category detail would defeat the row-level scoping given to a category manager.
DISCONFIRMING_OBSERVATION: >
  A category manager scoped to specific categories can see, through a shared company-wide summary total, another category's item-level value figures.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Scope a category manager's access to specific product categories, and check whether a shared company-wide summary total exposes another category's item-level figures.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q040

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q040
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a stock item is subject to a pending price dispute with a supplier that could change its recorded cost, the combined dashboard does not present the disputed cost as final without indicating that a correction may follow.
WHY_IT_MATTERS: >
  Presenting a disputed cost as final would mislead a viewer into treating an unresolved figure as settled.
DISCONFIRMING_OBSERVATION: >
  The combined widget presents a stock item's disputed cost as final with no indication that a supplier price dispute could still change it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place an item's recorded cost under an active supplier price dispute, and check whether the combined widget presents the current cost as final or flags it as disputed.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q041

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q041
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A combined dashboard aggregating stock value trend over time attributes a late-arriving, backdated accounting correction to the period in which the correction was actually applied, not to the originally intended transaction period.
WHY_IT_MATTERS: >
  Misattributing a backdated correction to the wrong period would distort the trend line for a period that never actually saw that change.
DISCONFIRMING_OBSERVATION: >
  A backdated accounting correction appears in the combined trend widget under the period the original transaction occurred in, rather than the period the correction was actually applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a backdated accounting correction to a stock valuation history, and check which period the combined trend widget attributes the correction to.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q042

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q042
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where two items are consolidated into one identifier as part of a data cleanup, the combined dashboard's historical value trend for the surviving identifier does not silently absorb the merged item's prior history in a way that misrepresents what was actually held at each past point in time.
WHY_IT_MATTERS: >
  Silently merging two items' histories would misrepresent what was actually on hand at any given past date.
DISCONFIRMING_OBSERVATION: >
  After two items are consolidated into one identifier, the combined widget's historical trend for the surviving identifier shows a merged history that misrepresents what was actually held at past dates.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consolidate two stock items into one identifier as part of a data cleanup, and check whether the combined widget's historical trend correctly represents what was actually held at past dates.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q043

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q043
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A combined widget configured with a scheduled, non-real-time refresh clearly indicates that the displayed stock value may not include movements posted since the last refresh, rather than implying the figure is current.
WHY_IT_MATTERS: >
  An unlabeled scheduled refresh would let a viewer mistake a stale snapshot for the current, complete valuation.
DISCONFIRMING_OBSERVATION: >
  A combined widget on a scheduled refresh presents its stock value figure with no indication that movements posted since the last refresh are excluded.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a combined widget to refresh on a fixed schedule, post a new stock movement after the last refresh, and check whether the displayed figure indicates it may be incomplete.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q044

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q044
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a stock item's unit of measure is changed, the combined dashboard's value-per-unit trend reflects the change consistently rather than silently comparing pre- and post-change periods on an inconsistent basis.
WHY_IT_MATTERS: >
  Comparing periods on an inconsistent unit basis would make the trend line numerically meaningless across the change point.
DISCONFIRMING_OBSERVATION: >
  The combined widget's value-per-unit trend compares a pre-change period and a post-change period on inconsistent unit-of-measure bases with no adjustment or note.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a stock item's unit of measure, and check whether the combined widget's value-per-unit trend adjusts consistently across the change or compares mismatched bases.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q045

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q045
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a fully written-off item is later found and returned to usable stock, the combined dashboard reinstates its value through a documented adjustment rather than the item reappearing in the valuation total with no traceable adjustment event.
WHY_IT_MATTERS: >
  An untraceable reappearance would make it impossible to explain a sudden increase in valuation to anyone reviewing the figures later.
DISCONFIRMING_OBSERVATION: >
  A previously written-off item reappears in the combined valuation total with no traceable adjustment event recording its reinstatement.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Find and return a previously written-off item to usable stock, and check whether the combined widget's valuation reinstatement is recorded as a traceable adjustment.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q046

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q046
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a company operates in a jurisdiction requiring a specific statutory valuation method distinct from its internal management reporting method, the combined dashboard clearly labels which method a given figure represents.
WHY_IT_MATTERS: >
  An unlabeled figure could be mistaken for the wrong method entirely, leading to a compliance or management decision based on the wrong basis.
DISCONFIRMING_OBSERVATION: >
  The combined widget presents a valuation figure with no label indicating whether it represents the statutory or the internal management method.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a jurisdiction requiring a statutory valuation method distinct from internal management reporting, and check whether the combined widget labels which method each figure represents.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q047

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q047
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A combined widget's total does not let a viewer authorized only for a country-level rollup infer an individual company or branch's exact value within that country when the country happens to contain only one branch.
WHY_IT_MATTERS: >
  A country-level total that degenerates to a single branch's figure functions as a direct disclosure despite being presented as an aggregate.
DISCONFIRMING_OBSERVATION: >
  A country-level summary total, for a country containing only one branch, reveals that branch's exact value to a viewer not permitted to see individual branch detail.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  View the country-level combined summary for a country containing only one branch, and check whether the summary discloses that branch's exact individual value.
```

## G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q048

```yaml
QID: G15-SPREADSHEET_DASHBOARD_STOCK_ACCOUNT-Q048
MODULE: spreadsheet_dashboard_stock_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a stock movement is voided entirely, rather than reversed, the combined dashboard's historical figures for the period in which it was voided reflect its complete removal rather than either double-removing it or leaving a partial residual value.
WHY_IT_MATTERS: >
  An incomplete or double removal would leave the historical valuation either understated or overstated relative to what actually happened.
DISCONFIRMING_OBSERVATION: >
  After a stock movement is voided, the combined widget's historical figure for that period either still shows a partial residual value or removes more value than the voided movement originally added.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Void a stock movement entirely rather than reversing it, and check whether the combined widget's historical figure for that period reflects complete, accurate removal.
```
