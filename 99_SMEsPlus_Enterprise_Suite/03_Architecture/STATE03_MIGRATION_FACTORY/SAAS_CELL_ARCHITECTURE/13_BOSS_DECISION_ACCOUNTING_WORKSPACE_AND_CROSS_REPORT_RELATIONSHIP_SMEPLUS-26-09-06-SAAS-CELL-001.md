# BOSS DECISION — ACCOUNTING WORKSPACE + CROSS-REPORT RELATIONSHIP

Session: [SMEPLUS-26-09-06-SAAS-CELL-001]
Project: SMEsPlus ENTERPRISE SUITE
Jira: ERPPLUS-151
Status: BOSS-APPROVED DIRECTION / DETAIL DESIGN PENDING

## 1. Boss Decision

The Accounting area shall use one major workspace with three controlled responsibility groups:

1. Invoicing
2. General Ledger
3. Finance

The menu grouping may be shared under Accounting, while authorization and operational responsibilities remain independently controllable.

Navigation hierarchy does not imply authorization equivalence.

## 2. User-Facing Structure

Accounting
- Invoicing
  - Customer Invoices
  - Vendor Bills
  - Credit Notes
  - Debit Notes
- General Ledger
  - Journal Entries
  - General Ledger
  - Trial Balance
  - Reconciliation
  - Period Closing
  - Financial Statements
- Finance
  - Receipts
  - Payments
  - Cash
  - Bank
  - Payment Batches
  - Cash Position

Thai controlled localization:

บัญชี
- ใบแจ้งหนี้
- บัญชีแยกประเภท
- การเงิน

Detailed Thai terms remain subject to controlled semantic localization.

## 3. Responsibility Boundary

### Invoicing
Owns business billing documents and commercial receivable/payable documents.

### General Ledger
Owns accounting meaning, Dr/Cr, journals, posting, ledger, reconciliation, period close and financial statements.

### Finance
Owns receipt/payment execution, cash, bank and settlement operations.

Finance users are not required to determine debit/credit accounting logic. Accounting rules and Posting Engine remain controlled separately.

## 4. Cross-Report Relationship Requirement

Boss requires reports from Invoicing, General Ledger and Finance to be mutually traceable and reconcilable.

Required principle:

BUSINESS DOCUMENT -> ACCOUNTING POSTING -> MONEY SETTLEMENT -> RECONCILIATION -> FINANCIAL REPORT

Reports must not become disconnected silos.

### 4.1 Invoicing to General Ledger

A Customer Invoice / Vendor Bill report must be traceable to the resulting accounting entry and GL impact.

Expected relationship examples:
- Invoice -> AR / Revenue / Tax posting
- Vendor Bill -> AP / Expense / Asset / Inventory / Tax posting
- Credit Note -> reversal/adjustment accounting effect

### 4.2 Finance to General Ledger

A Receipt / Payment report must be traceable to the accounting posting produced by the settlement.

Examples:
- Customer Receipt -> Bank/Cash and AR clearing
- Supplier Payment -> AP clearing and Bank/Cash
- Advance Receipt/Payment -> controlled advance accounts

### 4.3 Invoicing to Finance

Users must be able to understand which invoices/bills are:
- Unpaid
- Partially Paid
- Paid
- Overdue
- Reconciled
- Reversed / Credited

### 4.4 General Ledger to Source

GL and Trial Balance drill-down must retain lineage to the originating business document and settlement where applicable.

### 4.5 Financial Statements to Evidence

Financial statements must be drillable/reconcilable through GL to source documents, payment/receipt settlement, and relevant control evidence.

## 5. Minimum Traceability Keys — Candidate Design Requirement

Detailed data model is not frozen, but reports should preserve enough common lineage to relate the three responsibility groups. Candidate traceability fields include:

- Tenant ID
- Company ID
- Business Document ID / Number
- Business Event ID
- Accounting Entry / Posting Reference
- Payment / Receipt Reference
- Reconciliation Reference
- Counterparty
- Currency
- Transaction Date
- Posting Date
- Settlement Date
- Status
- Source Module / Source Process

Exact schema and mechanism remain subject to later architecture/data design gates.

## 6. Reporting Principle

Each operational area owns its operational report, but reports must reconcile to the same canonical business facts.

Invoicing Report
  -> explains what was billed

Finance Report
  -> explains what money was received/paid

Accounting Report
  -> explains the Dr/Cr and financial meaning

Reconciliation
  -> proves that these views correspond to the same controlled transaction lifecycle

## 7. SoD / Permission Principle

Menu grouping shall not weaken segregation of duties.

Possible role separation includes:
- Invoice Creator
- Invoice Approver
- Payment Maker
- Payment Approver
- Accountant / Posting Reviewer
- Reconciliation Operator
- Period Closer

Visibility and actions may be independently enabled/disabled by role and authority.

## 8. Canonical Flow

Invoicing
  -> Accounting Recognition
  -> Finance Settlement
  -> Accounting Reconciliation
  -> Financial Reporting

Accounting therefore participates both before and after settlement: recognition first, reconciliation/closing later.

## 9. Governance

- Boss is sole Final Approver.
- No Evidence = No Progress.
- Never Skip Gate.
- This decision establishes the approved architecture direction for menu/workspace grouping and report relationship.
- Detailed menu labels, report catalogue, permission matrix, posting handoff and data schema remain subject to subsequent Deep Research and evidence gates.
