# DOMAIN_01 Accounting Core — Boss Ruling: 19 Active Account Types for SMEsPlus Local Thailand

Date: 2026-08-30

## Authority

Boss = Sole Final Approver.

This ruling supersedes the prior design recommendation that four Core-supported Account Types be kept only as `RESERVED / NOT DEFAULT-TH`.

The underlying source observation remains valid: the inspected Thailand localization template (`l10n_th`) instantiates 15 Account Types, while the Core Accounting source supports 19.

## Boss Decision

**APPROVED WITH CONTROL — SMEsPlus Local Thailand shall support all 19 Core Accounting Account Types as active business capabilities.**

The four previously reserved types are confirmed by Boss as used in real business/accounting operations and shall not be excluded from the Thailand target baseline merely because the inspected `l10n_th` template does not instantiate them.

## Four Types Activated by Boss Business Requirement

| Source key | Business-facing label | SMEsPlus Thailand status | Financial-statement presentation principle |
|---|---|---|---|
| `asset_prepayments` | Prepayments | ACTIVE | Balance Sheet — Asset classification; presentation subgroup determined by approved reporting mapping |
| `liability_credit_card` | Credit Card | ACTIVE | Balance Sheet — Liability classification; presentation subgroup determined by approved reporting mapping |
| `expense_other` | Other Expenses | ACTIVE | Profit & Loss — Expense classification |
| `off_balance` | Off-Balance Sheet | ACTIVE | **Excluded from normal Balance Sheet and P&L totals by default**; report separately as memorandum/off-balance information where applicable |

## Off-Balance Sheet Control Rule

`Off-Balance Sheet` is an active Account Type, but its existence does not mean it belongs inside normal Balance Sheet totals.

Default SMEsPlus reporting rule:

1. Off-Balance accounts are operationally usable and postable only under approved accounting/control rules.
2. They must be excluded from ordinary Balance Sheet asset/liability/equity totals.
3. They must be excluded from ordinary Profit & Loss income/expense totals unless a separately approved accounting transformation creates a real financial-statement entry.
4. They may be presented in a dedicated `Off-Balance Sheet / Memorandum Accounts` section or report.
5. The reporting engine must distinguish `active account type` from `included in primary financial statements`.
6. Off-Balance activity must remain auditable, traceable, tenant/company isolated, and migration-mappable.

## Reconciled Account Type Baseline

Evidence layers now have different roles:

- Core Accounting source universe: **19 available Account Types**.
- Inspected `l10n_th` template: **15 Account Types instantiated** across 144 Thai template rows.
- Boss-approved Odoo18 workbook: **14 Account Type labels observed** across 389 source rows.
- SMEsPlus Local Thailand target baseline: **19 ACTIVE Account Types**, based on Source capability + Boss-approved Thailand business requirement.

Therefore:

`Source observation count != Target capability count`

and

`Template omission != Business prohibition`.

## Active 19-Type Business-Facing Set

1. Receivable
2. Bank and Cash
3. Current Assets
4. Non-current Assets
5. Prepayments
6. Fixed Assets
7. Payable
8. Credit Card
9. Current Liabilities
10. Non-current Liabilities
11. Equity
12. Current Year Earnings
13. Income
14. Other Income
15. Expenses
16. Other Expenses
17. Depreciation
18. Cost of Revenue
19. Off-Balance Sheet

## Clean-Room Boundary

The 19 business-facing Account Types are accepted as generic accounting/business semantics. SMEsPlus must still own its own canonical identifiers, reporting rules, control rules, data model, and implementation.

No Odoo ORM/schema/source-code/technical-ID/module architecture is authorized for reuse or cloning.

## Gate Effect

`SMEsPlus Local Thailand Account Type baseline = 19 ACTIVE TYPES`.

Prior recommendation `15 ACTIVE + 4 RESERVED` is **SUPERSEDED FOR TARGET DESIGN** by this Boss ruling.

The prior source-evidence statement remains historical fact and must not be rewritten: `l10n_th` was observed to instantiate 15 types.

No Development or Production authorization is created by this ruling.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
