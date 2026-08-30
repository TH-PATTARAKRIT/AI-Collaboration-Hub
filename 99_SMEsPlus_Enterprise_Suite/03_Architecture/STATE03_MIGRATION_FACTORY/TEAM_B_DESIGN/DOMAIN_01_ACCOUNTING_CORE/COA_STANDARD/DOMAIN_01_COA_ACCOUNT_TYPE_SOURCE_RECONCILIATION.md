# DOMAIN_01 Accounting Core — Account Type Source Reconciliation

Date: 2026-08-30

## Executive Result

The previously reported **14 Account Type labels** are the types actually observed in the Boss-approved `Odoo18` workbook tab. They are **not** the complete Account Type universe evidenced by the learning source.

Three evidence layers now reconcile as follows:

1. Core Accounting source model: **19 available Account Types**.
2. Thailand localization source template (`l10n_th`): **15 Account Types actually used** across **144 Thai COA rows**.
3. Boss-approved `Odoo18` workbook tab: **14 Account Types actually used** across **389 rows**.

Therefore, for SMEsPlus Local Thailand, the evidence-backed candidate Account Type baseline is **15 active Thailand types**, subject to Boss/PMO freeze. The four remaining core types are source-supported but not used by the inspected Thailand template.

## Evidence Sources

### A. Team A Deep Research

`TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/02_SOURCE_EVIDENCE.md`

- `SE-17`: `account_account.py` lines 44–72 = `account_type` 19-value enumeration.

`TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/09_DATA_SEMANTIC_REGISTER.md`

- `account_type`: 19-value enumeration driving legal reporting and year-end behaviour.
- `internal_group`: coarse asset/liability/equity/income/expense/off grouping derived from type.

### B. Direct READ-ONLY Core Source Verification

Authorized source path:

`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/01 ACCOUNT/account/models/account_account.py`

Direct inspection confirmed these 19 source values/labels:

| Source key | Business-facing label |
|---|---|
| `asset_receivable` | Receivable |
| `asset_cash` | Bank and Cash |
| `asset_current` | Current Assets |
| `asset_non_current` | Non-current Assets |
| `asset_prepayments` | Prepayments |
| `asset_fixed` | Fixed Assets |
| `liability_payable` | Payable |
| `liability_credit_card` | Credit Card |
| `liability_current` | Current Liabilities |
| `liability_non_current` | Non-current Liabilities |
| `equity` | Equity |
| `equity_unaffected` | Current Year Earnings |
| `income` | Income |
| `income_other` | Other Income |
| `expense` | Expenses |
| `expense_other` | Other Expenses |
| `expense_depreciation` | Depreciation |
| `expense_direct_cost` | Cost of Revenue |
| `off_balance` | Off-Balance Sheet |

## Thailand Localization Source Proof

Authorized source path:

`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/l10n_th/data/template/account.account-th.csv`

Direct controlled analysis result:

- Thai COA rows: **144**
- Unique Account Types used: **15**

| Account Type key | Thai template row count | Business-facing label |
|---|---:|---|
| `asset_cash` | 3 | Bank and Cash |
| `asset_current` | 15 | Current Assets |
| `asset_fixed` | 22 | Fixed Assets |
| `asset_non_current` | 6 | Non-current Assets |
| `asset_receivable` | 4 | Receivable |
| `liability_payable` | 3 | Payable |
| `liability_current` | 13 | Current Liabilities |
| `liability_non_current` | 3 | Non-current Liabilities |
| `equity` | 3 | Equity |
| `equity_unaffected` | 1 | Current Year Earnings |
| `income` | 4 | Income |
| `income_other` | 6 | Other Income |
| `expense` | 42 | Expenses |
| `expense_depreciation` | 12 | Depreciation |
| `expense_direct_cost` | 7 | Cost of Revenue |

## Odoo18 Workbook Evidence

Existing controlled extraction evidence:

`COA_STANDARD/DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`

Commit: `ae2b0719081ef9497f08e3b3e1ea8329d053cf83`

Observed in 389 workbook rows: **14 labels**

- Bank and Cash
- Current Assets
- Receivable
- Current Liabilities
- Fixed Assets
- Depreciation
- Payable
- Non-current Liabilities
- Equity
- Income
- Other Income
- Cost of Revenue
- Expenses
- Current Year Earnings

## Reconciliation

### Thailand source vs Boss Odoo18 workbook

The Thailand source template contains every workbook-observed type **plus one additional active Thai type**:

- `asset_non_current` — **Non-current Assets**

The Thai source uses this type for items including long-term investments, investment property, software/intangible assets, goodwill, and accumulated amortization-related non-current asset accounts.

### Core source types not used by the inspected Thailand template

Four source-supported types are not used in `l10n_th/account.account-th.csv`:

1. `asset_prepayments` — Prepayments
2. `liability_credit_card` — Credit Card
3. `expense_other` — Other Expenses
4. `off_balance` — Off-Balance Sheet

This does **not** prove these concepts are invalid for Thailand. It proves only that the inspected Thailand source COA template does not instantiate them as Account Types.

## Controlled Design Recommendation

For the current **SMEsPlus Local Thailand** scope:

### Active Thailand Account Type Candidate = 15

Use the 15 Account Types evidenced by the Thailand localization template as the active candidate set.

The Boss-approved Odoo-like UX direction remains satisfied because these are the same generic business-facing Account Type labels from the reference accounting model.

### Core-only types = Reserved / Not in default Thailand baseline

Keep the four non-instantiated core types as `RESERVED / SOURCE-SUPPORTED / NOT DEFAULT-TH` until Thailand business evidence or Boss direction requires activation.

Do not silently delete them from provenance; do not include them in the default SMEsPlus Thailand COA without evidence.

## Gate Impact

- Previous statement `Odoo18 tab has 14 Account Types`: **still correct as workbook observation**.
- Interpretation `SMEsPlus Thailand should have only 14 types`: **not supported**.
- Evidence-backed Thailand candidate: **15 active types**.
- Core source universe: **19 types**.
- Difference requiring explicit control: **4 core-only reserved types**.

No development authorization is created by this reconciliation.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
