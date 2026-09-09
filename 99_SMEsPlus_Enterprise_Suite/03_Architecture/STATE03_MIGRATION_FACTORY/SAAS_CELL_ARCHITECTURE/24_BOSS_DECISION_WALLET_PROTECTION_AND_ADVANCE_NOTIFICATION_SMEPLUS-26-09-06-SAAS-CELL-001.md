# BOSS DECISION — WALLET PROTECTION AND ADVANCE NOTIFICATION

Session: SMEPLUS-26-09-06-SAAS-CELL-001
Jira: ERPPLUS-151
Date: 2026-09-09
Status: BOSS APPROVED DIRECTION

## Boss decision

Boss approved the prepaid service wallet direction with mandatory advance notification so customers can understand current burn, projected cost, projected remaining balance, and when a top-up will be required.

The intent is to prevent surprise billing and prevent service interruption caused by an unexpected exhausted balance.

## Core principles

1. Customer wallet balance does not reset at month end.
2. Usage counters may reset by billing period, while historical usage and billing evidence remain immutable/auditable.
3. Customers shall receive advance notice before the wallet is expected to become insufficient.
4. SMEsPlus shall show both current balance and projected runway based on measurable usage.
5. Customer shall be able to understand whether a top-up is likely before service credit is exhausted.
6. Notification thresholds are mandatory, but exact numeric thresholds remain open until commercial and behavioral validation.
7. No Surprise Billing.
8. No Evidence = No Chargeable Overage.

## Wallet Protection model

Candidate protection states:

- NORMAL — sufficient projected service credit.
- INFORMATION — balance/runway has reduced enough to warrant awareness.
- WARNING — projected balance indicates top-up will likely be required within the defined planning window.
- TOP-UP REQUIRED — projected balance is insufficient for expected consumption or next required charge.

Exact threshold percentages or month-of-runway values are not frozen yet.

## Customer-facing minimum information

Customer dashboard should display at minimum:

- Current wallet balance.
- Base rental / subscription charge.
- Current measured usage.
- Current estimated monthly cost.
- Projected month-end cost.
- Projected month-end wallet balance.
- Estimated service runway.
- Projected shortfall, if any.
- Recommended top-up amount or top-up required status.
- Evidence/drill-down for chargeable usage.

## Operating principle

The customer should know before the balance is exhausted:

KNOW -> FORECAST -> WARN -> PREPARE -> TOP-UP / APPROVE -> CONSUME -> MEASURE -> AUDIT

## Commercial wording direction

SMEsPlus Standard may operate as a prepaid SaaS wallet:

Prepaid Service Credit
-> Base Rental deduction
-> Measured Usage deduction
-> Optional/Add-on deduction
-> Remaining Balance
-> Forecast / Warning / Top-up

The wallet is not to be represented as a guaranteed fixed number of months unless the contract explicitly defines a non-metered prepaid term. Estimated coverage must be described as usage-dependent.

## Open design items

The following are NOT frozen:

- Exact warning thresholds.
- Minimum required reserve.
- Auto top-up rules.
- Recommended top-up calculation.
- Grace period / restriction sequence when balance is exhausted.
- Transaction and processing charging units.
- Standard and Enterprise commercial rates.

These require Cost-to-Serve, transaction taxonomy, load testing, telemetry, margin simulation, and commercial validation before final freeze.
