# CORR-007B — 9 Special Team Challenge Report

Project: SMEsPlus ENTERPRISE SUITE  
Branch: `audit/inventory-core-corr007b-3high-closure-010`  
Context: Boss-approved supplementary challenge mechanism for issue-specific deep proof  
Status: Supplementary challenge publication only; not Gate PASS; not Team B/C authorization

## 1. Boss Clarification

Boss clarified the dual mandate:

1. **9 Veto Challenge Council** = main duty / mandatory gate-control challenge.
2. **9 Special Team Challenge** = supplementary deep-dive duty for specific concerns raised by Boss.

Both report directly to Boss only.

The 9 Special Team Challenge is used to eliminate deep risks such as:

- WHT multi-type / multi-rate scenarios;
- Product Category valuation policy;
- Manual vs Automated valuation;
- Periodic vs Perpetual accounting behavior;
- monthly close;
- Month 12 year-end close;
- stock.move cut-off;
- inventory valuation to GL reconciliation;
- retained earnings under Equity / Account Category 3;
- source + dump functional learning gaps.

## 2. Supplementary Challenge Mandate

When Boss raises a specific concern, the 9 Special Team Challenge must:

1. isolate the concern;
2. define the business scenario;
3. locate source and dump evidence;
4. challenge functional behavior, not only method names;
5. identify database/migration impact;
6. identify accounting/localization impact;
7. identify code/UI/report impact;
8. decide whether the issue is resolved, controlled, or remains high;
9. produce a traceable deep-proof deliverable.

## 3. 9 Challenge Capacities for Special Deep-Dive

| # | Capacity | Special Deep-Dive Responsibility |
|---:|---|---|
| 1 | Team A — Source Extraction & Observation | Extract source/dump facts and prevent unsupported inference |
| 2 | Team B — SMEsPlus Canonical Domain Design | Translate facts into clean-room SMEsPlus canonical semantics |
| 3 | Figma / UX Team | Verify whether workflow is operable by real users and testable in UAT |
| 4 | Team C — Engineering / Migration Adapter / Implementation | Challenge feasibility without authorizing build |
| 5 | Team D — Independent QA / Compliance / Regression | Challenge reproducibility, regression, and compliance risks |
| 6 | Leader Functional Design | Produce FSD-grade workflow and event matrix; challenge business completeness |
| 7 | Leadership Database Design | Produce ER/schema/migration map implications; challenge data integrity |
| 8 | Lead Integration & Localization | Challenge Thai accounting/tax/localization/API behavior |
| 9 | Lead Code & UI Architect | Challenge source/UI/QWeb/report evidence and clean-room boundary |

## 4. N-A12-01 Special Challenge Scope

Boss raised that the prior N-A12-01 proof did not cover the full functional design of monthly close and year-end close.

The Special Team Challenge must prove or keep open the following:

### 4.1 Monthly Close

- Accounting initiates close / lock.
- Inventory must control stock-impact transaction cut-off.
- Stock movement backdating into a closed period must be blocked or correction-controlled.
- Ending quantity and ending inventory value must be established.
- Ending balance must carry forward to the next month.

### 4.2 Month 12 Year-End Close

- Month 12 close is still a monthly close.
- It additionally closes income and expense accounts.
- Remaining profit/loss transfers to retained earnings under Equity / Account Category 3.
- Inventory ending value must reconcile to GL before year-end carry-forward.

### 4.3 Periodic vs Perpetual / Manual vs Automated

- Determine whether the source/dump supports Periodic, Perpetual, or both.
- Identify configuration owner, especially Product Category.
- Prove Manual valuation behavior.
- Prove Automated valuation behavior.
- Prove effect on stock.move accounting entries during the month.
- Prove month-end adjustment / reconciliation behavior.

### 4.4 Product Category Valuation Policy

Boss supplied screenshots showing Product Category-level configuration for:

- Costing Method;
- Inventory Valuation = Manual / Automated;
- Stock Journal;
- Stock Input Account;
- Stock Output Account;
- Stock Valuation Account;
- Income Account;
- Expense Account.

The Special Team Challenge must prove how products inherit valuation behavior from Product Category and how this affects stock.move and GL.

## 5. Special Challenge Finding

The earlier N-A12-01 disposition is insufficient for functional baseline publication.

Corrected status:

`N-A12-01 = HIGH FUNCTIONAL DESIGN GAP UNTIL MONTHLY CLOSE / YEAR-END CLOSE / PRODUCT CATEGORY VALUATION / PERIODIC-PERPETUAL PROOF IS COMPLETE`

## 6. Required Next Proof

A future or reopened CORR-007B package must produce:

- functional workflow diagram;
- event matrix;
- Account x Inventory close contract;
- Product Category valuation matrix;
- source + dump semantic proof;
- retained earnings close treatment;
- revised Boss decision recommendation.

This report does not declare Gate PASS and does not authorize Team B or Team C.
