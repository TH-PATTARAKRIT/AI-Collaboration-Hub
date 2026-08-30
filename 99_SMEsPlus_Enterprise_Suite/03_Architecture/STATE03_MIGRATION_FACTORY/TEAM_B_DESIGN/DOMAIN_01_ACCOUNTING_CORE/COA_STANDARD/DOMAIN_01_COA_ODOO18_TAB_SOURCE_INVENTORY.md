# DOMAIN_01 Accounting Core — Odoo18 Tab COA Source Inventory

Date: 2026-08-30

## Authority and Purpose

Boss authorized controlled extraction of the workbook `Account_Odoo18_19 sent 270369.xlsx`, tab `Odoo18`, as the first evidence step before finalizing `D01-GATE-A3 — COA Template / Instance Structure`.

This artifact records only what is directly observed from the Boss-approved source dataset. It does not convert source structure into SMEsPlus target architecture.

## Source

- File: `Account_Odoo18_19 sent 270369.xlsx`
- Boss-designated tab: `Odoo18`
- Google Drive file ID: `1KoprCep3eeYy49OcV0TTFQOlc1zq9m2f`
- Source URL: `https://docs.google.com/spreadsheets/d/1KoprCep3eeYy49OcV0TTFQOlc1zq9m2f/edit`
- Source role: Primary business-facing COA seed/reference for SMEsPlus Thailand COA standardization.

## Controlled Extraction Result

The first table corresponding to the Boss-designated `Odoo18` tab was read through its full serialized row range.

### Row inventory

- Data row index starts at: `0`
- Data row index ends at: `388`
- Total data rows: **389**
- Header row: present

The connector text projection exposes an unlabeled leading row index in addition to the business columns. That index is treated as projection/row-order metadata, not as a target accounting field.

### Business columns observed

| Column | Observed meaning | Governance treatment |
|---|---|---|
| `id` | Source record identifier / external provenance | Source metadata only; MUST NOT become SMEsPlus canonical identity |
| `name` | Account name | Business-facing reference input |
| `reconcile` | Reconciliation flag | Business behavior input; requires canonical rule mapping |
| `code` | Account code | Business-facing numbering reference; MUST NOT become canonical identity by itself |
| `account_type` | Business-facing Account Type classification | Approved as primary input for Odoo-like Account Type familiarity, subject to SMEsPlus-owned canonical IDs/rules |

### Observed Account Type labels in the Odoo18 table

The following labels were observed across rows `0–388`:

1. `Bank and Cash`
2. `Current Assets`
3. `Receivable`
4. `Current Liabilities`
5. `Fixed Assets`
6. `Depreciation`
7. `Payable`
8. `Non-current Liabilities`
9. `Equity`
10. `Income`
11. `Other Income`
12. `Cost of Revenue`
13. `Expenses`
14. `Current Year Earnings`

These labels are evidence of the source/business-facing classification vocabulary only. SMEsPlus canonical identifiers and classification rules remain independently designed.

## Boundary Evidence

Examples from the beginning of the table include:

- index `0`: `Cash Bakery`, code `110000002`, type `Bank and Cash`
- index `1`: `เงินสด`, code `111000010`, type `Bank and Cash`
- index `11`: `ลูกหนี้การค้า`, code `111600010`, type `Receivable`

Examples from the end of the table include:

- index `385`: `Undistributed Profits/Losses`, code `930007999`, type `Current Year Earnings`
- index `386`: `ใบเสร็จรับเงินค้างชำระ`, code `930008000`, type `Current Assets`
- index `387`: `การชำระเงินค้างชำระ`, code `930008001`, type `Current Assets`
- index `388`: `บัญชีพัก - ฐานภาษีมูลค่าเพิ่ม`, code `950001009`, type `Expenses`

## Item-1 Gate Result

Boss prerequisite item 1 from the COA ruling was:

> Extract and inventory the actual `Odoo18` tab rows/columns from the Boss-provided workbook.

**Result: PASS — EVIDENCE AVAILABLE.**

Evidence now establishes:

- exact first-tab data-row range `0–388`;
- total `389` data rows;
- five business columns;
- source-facing Account Type vocabulary;
- source identity and Drive location.

## What Is Not Yet Claimed

This extraction does NOT yet prove or approve:

- duplicate-account disposition;
- final numbering ranges;
- final SMEsPlus canonical Account Type IDs;
- final account-by-account canonical mapping;
- Balance Sheet/P&L correctness for every source row;
- VAT/WHT dependency mapping for every source row;
- multi-company extension policy at row level;
- exact final SMEsPlus Standard Thai COA content.

Those remain controlled next steps before exact COA Blueprint Freeze.

## Clean-Room Boundary

Allowed transformation remains:

`Odoo18 Tab COA → Business Meaning → SMEsPlus Canonical Accounting Classification → SMEsPlus Standard Thai COA Template → Company/Tenant COA Instance`

Prohibited:

- Odoo ORM/schema cloning
- source-code reuse
- technical-ID reuse as target identity
- module-architecture cloning
- vendor implementation copying

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
