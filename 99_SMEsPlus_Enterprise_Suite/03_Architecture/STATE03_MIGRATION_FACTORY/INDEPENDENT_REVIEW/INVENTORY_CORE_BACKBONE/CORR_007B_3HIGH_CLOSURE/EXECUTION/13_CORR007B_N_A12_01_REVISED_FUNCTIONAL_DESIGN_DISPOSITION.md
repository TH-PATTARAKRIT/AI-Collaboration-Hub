# CORR-007B — N-A12-01 Revised Functional Design Disposition

Project: SMEsPlus ENTERPRISE SUITE  
Branch: `audit/inventory-core-corr007b-3high-closure-010`  
Context: Boss-approved correction after 9 Veto Challenge Council + 9 Special Team Challenge governance ruling  
Status: Revised disposition publication only; not Gate PASS; not Team B/C authorization

## 1. Prior CORR-007B Disposition

The prior CORR-007B package classified `N-A12-01` as:

`CONTROLLED ACCOUNTING x INVENTORY CROSS-PROOF CARRY-FORWARD`

That classification was acceptable only for source-code ownership classification: Inventory source mechanisms were proven, while the remaining cross-proof required Accounting evidence.

## 2. Boss Challenge

Boss challenged that this did not reach Functional Design depth.

Boss clarified the actual business issue:

1. Accounting closes every month.
2. Month 12 is still a monthly close, but it has year-end character.
3. Every monthly close produces ending balances that carry forward to the next month.
4. Month 12 additionally closes income and expense accounts.
5. Net profit/loss is transferred to retained earnings under Equity / Account Category 3.
6. Accounting controls the close process.
7. Inventory must support stock movement cut-off / backdate control.
8. Inventory must establish stock quantity and inventory value as of the close date.
9. Inventory valuation must reconcile to Accounting / GL.
10. Periodic vs Perpetual, and Manual vs Automated valuation, change the posting behavior during the month and at month-end.
11. Product Category / Product Group-level valuation policy is a core reference learning point.

## 3. Corrected Classification

`N-A12-01 = REOPENED HIGH FUNCTIONAL DESIGN GAP`

Full corrected label:

`N-A12-01 — ACCOUNT-LED MONTHLY CLOSE, YEAR-END CLOSE, STOCK CUT-OFF, PRODUCT CATEGORY VALUATION POLICY, PERIODIC/PERPETUAL POSTING BEHAVIOR, CARRY-FORWARD BALANCE, GL RECONCILIATION, AND RETAINED EARNINGS FUNCTIONAL DESIGN GAP — HIGH UNTIL PROVEN`

## 4. Sub-item Disposition

| Sub-item | Description | Current status |
|---|---|---|
| `N-A12-01-A` | Inventory source lock-date mechanism | SOURCE MECHANISM PROVEN |
| `N-A12-01-B` | Inventory accounting_date / force_period_date propagation | SOURCE MECHANISM PROVEN |
| `N-A12-01-C` | Monthly close functional workflow | NOT PROVEN |
| `N-A12-01-D` | Month 12 year-end close to retained earnings | NOT PROVEN |
| `N-A12-01-E` | Inventory valuation to GL reconciliation | NOT PROVEN |
| `N-A12-01-F` | Opening balance / carry-forward to next month/year | NOT PROVEN |
| `N-A12-01-G` | Periodic vs Perpetual / Manual vs Automated behavior | NOT PROVEN |
| `N-A12-01-H` | Product Category-level valuation policy impact | NOT PROVEN |
| `N-A12-01-I` | Clean-room SMEsPlus target close design | NOT PROVEN |

## 5. Required Functional Design Proof

N-A12-01 cannot be counted as functionally closed until the following are proven with source + dump evidence and clean-room target reasoning:

1. Accounting-led monthly close workflow.
2. Inventory stock.move cut-off / backdate control in closed periods.
3. Ending stock quantity as of close date.
4. Ending inventory value as of close date.
5. Periodic vs Perpetual valuation behavior.
6. Manual vs Automated valuation behavior.
7. Product Category / Product Group valuation policy ownership.
8. Standard / FIFO / AVCO close behavior.
9. Inventory / COGS / Stock Input / Stock Output / Stock Valuation account impact.
10. Month 12 year-end close to retained earnings under Equity / Account Category 3.
11. Opening balance carry-forward to next month/year.
12. Inventory valuation to GL reconciliation.
13. Exception handling for post-close correction and backdating.
14. Functional workflow diagram.
15. Account x Inventory event matrix.
16. Clean-room SMEsPlus target close contract.

## 6. Impact on Baseline Publication

`Account + Inventory Backbone Reference Baseline = HOLD`

Reason:

The current evidence package does not yet prove the monthly/year-end close functional design required for downstream teams to rely on Account x Inventory as a controlled functional baseline.

The previous statement `Pure Inventory High blockers = 0` must be qualified as:

`Pure Inventory source-mechanism blockers = 0; Account x Inventory functional design blocker N-A12-01 remains HIGH.`

## 7. Required Next Deliverables

The next proof cycle must produce at least:

1. `N_A12_01_MONTHLY_CLOSE_FUNCTIONAL_WORKFLOW.md`
2. `N_A12_01_PRODUCT_CATEGORY_VALUATION_POLICY_MATRIX.md`
3. `N_A12_01_PERIODIC_PERPETUAL_BEHAVIOR_PROOF.md`
4. `N_A12_01_YEAR_END_RETAINED_EARNINGS_PROOF.md`
5. `N_A12_01_ACCOUNT_INVENTORY_GL_RECONCILIATION_PROOF.md`
6. `N_A12_01_CLEAN_ROOM_TARGET_CLOSE_CONTRACT.md`

## 8. Final Disposition

`N-A12-01 = HIGH FUNCTIONAL DESIGN GAP — REOPENED`

This revised disposition supersedes any interpretation that N-A12-01 is functionally closed.

This is not Gate PASS.  
This is not Team B authorization.  
This is not Team C authorization.  
Boss remains the sole Final Approver.
