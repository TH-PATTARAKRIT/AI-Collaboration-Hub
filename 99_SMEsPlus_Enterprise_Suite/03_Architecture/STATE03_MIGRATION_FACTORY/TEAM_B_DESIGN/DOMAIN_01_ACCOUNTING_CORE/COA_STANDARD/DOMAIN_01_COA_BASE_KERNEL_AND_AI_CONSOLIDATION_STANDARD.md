# DOMAIN_01 Accounting Core — SMEsPlus Thailand COA Base Kernel + AI Semantic Consolidation Standard

Date: 2026-08-30
Authority: Boss = Sole Final Approver

## Executive Decision

The Boss-approved Odoo18 workbook is a **source observation set**, not a target row-count mandate.

`389 source rows != 389 SMEsPlus target accounts`

The SMEsPlus Thailand COA shall be constructed using two controlled tracks:

1. **Track A — Source-Derived Base COA Kernel**
2. **Track B — AI Semantic Consolidation for non-kernel/customized accounts**

This replaces any interpretation that every source row must become one SMEsPlus account.

## Track A — Source-Derived Base COA Kernel

Learn from the authorized Odoo Accounting Core + Thailand localization source and identify the smallest defensible set of baseline accounts required by:

- core accounting behaviour;
- Thai localization / statutory treatment;
- AR/AP control;
- cash/bank/transfer/suspense flows;
- inventory/valuation defaults;
- tax/VAT/WHT/CIT handling;
- retained/current-year earnings;
- exchange gain/loss;
- default income/expense behaviour;
- reconciliation/control semantics.

Boss working expectation: approximately **32 baseline accounts**.

Governance treatment of the number `32`:

- `~32 = WORKING EXPECTATION / CANDIDATE RANGE`
- `Exact Base Kernel Count = TBD / EVIDENCE REQUIRED`
- Do not freeze exactly 32 until source anchors and business meaning are reconciled.

The currently inspected Thailand source template contains 144 COA rows and 15 active Account Types. This does not mean 144 target accounts are mandatory.

## Track B — AI Semantic Consolidation

For source accounts outside the Base COA Kernel, AI shall classify and consolidate by **business meaning**, not by source row identity or source code.

Mandatory transformation:

`Source Account -> Business Meaning -> Accounting Treatment -> Canonical Group -> SMEsPlus Target Account`

AI may consolidate N source accounts into 1 SMEsPlus target account where the accounting meaning/treatment is materially the same.

### Boss example

Source observations:

- รายได้จากการขายออนไลน์ - GRAB
- รายได้จากการขายออนไลน์ - LINEMAN
- รายได้จากการขายออนไลน์ - SHOPEE
- รายได้จากการขายออนไลน์ - LAZADA

Target canonical account candidate:

`รายได้จากการขายออนไลน์ / Online Sales Revenue`

The marketplace/channel identity shall not automatically create separate GL accounts.

## Dimension-over-Account-Proliferation Principle

If a distinction is operational/analytical rather than accounting-recognition driven, represent it as a **dimension / source attribute / subledger classification**, not by multiplying GL accounts.

Examples of dimensions that should normally remain outside the COA identity:

- Sales Channel / Marketplace
- Customer
- Product
- Branch / Location
- Salesperson
- Campaign
- Source System
- Marketplace Order Source

A product sold through GRAB, LINEMAN, SHOPEE and LAZADA should normally post to the same canonical revenue account when recognition, tax treatment and financial-statement presentation are the same.

## Mandatory Do-NOT-Merge Rules

AI must NOT consolidate accounts solely because names are similar if any of these differ materially:

1. Account Type / canonical accounting class
2. Balance Sheet vs Profit & Loss presentation
3. Thai tax/VAT/WHT/CIT treatment
4. Reconciliation requirement
5. AR/AP control-account role
6. Cash/bank/clearing/suspense behaviour
7. Inventory/valuation/cost-flow role
8. Currency restriction or monetary-item treatment
9. Statutory or regulatory reporting requirement
10. Retained earnings/current-year earnings semantics
11. Contra-account / allowance / accumulated depreciation role
12. Multi-company consolidation meaning
13. Any evidenced system-generated control dependency

If one of these differs, status = `KEEP SEPARATE` or `HOLD FOR REVIEW`.

## Required AI Classification Outcome Per Source Account

Each source row must receive one of:

- `BASE_KERNEL`
- `MERGE_TO_CANONICAL`
- `KEEP_SEPARATE`
- `RESERVED / NOT DEFAULT-TH`
- `HOLD / EVIDENCE_REQUIRED`

For `MERGE_TO_CANONICAL`, record:

- source account code/name;
- source account type;
- source business meaning;
- target canonical account;
- reason for merge;
- accounting-treatment equivalence evidence;
- retained source provenance.

## Source Evidence Already Established

### Core source

Team A SE-17 / direct source inspection establishes a 19-value Account Type universe.

### Thailand localization source

`l10n_th/data/template/account.account-th.csv`

- 144 source-template rows
- 15 Account Types used

### Boss-approved Odoo18 workbook

- 389 source rows
- 14 Account Type labels observed

These counts are **evidence inventories**, not target-count requirements.

## Base Kernel Discovery Method

Before final COA candidate generation, perform a controlled source read to identify accounts explicitly referenced by Thailand localization/core default configuration and accounts whose business role is required for Thai accounting/control.

Evidence sources include at minimum:

- `l10n_th/models/template_th.py`
- `l10n_th/data/template/account.account-th.csv`
- Team A source/deep-research evidence
- Boss-approved Odoo18 workbook tab

Every proposed Base Kernel account must have:

- business purpose;
- Account Type;
- source evidence anchor;
- Thai relevance;
- reason it cannot be safely derived as a mere dimension or optional company extension.

## Target Architecture

`Source Account Universe`
` -> Base Kernel Discovery`
` -> AI Semantic Consolidation`
` -> SMEsPlus Canonical Account Type`
` -> SMEsPlus Standard Thai COA Candidate`
` -> Company/Tenant COA Instance`
` -> Source Mapping / Provenance`

## Gate Effect

Approved design direction:

- Do not target 389 accounts merely because the workbook has 389 rows.
- Use source-learned baseline accounts as the foundation.
- Treat `~32` as a working Base Kernel expectation until exact evidence verification.
- Consolidate source-specific/channel-specific accounts by business meaning.
- Prefer dimensions over GL-account proliferation where accounting treatment is unchanged.
- Preserve all source-to-target provenance.

Exact Base Kernel count and exact final SMEsPlus Standard Thai COA count remain `TBD / EVIDENCE REQUIRED` until controlled reconciliation is complete.

No Development or Production authorization is created by this standard.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
