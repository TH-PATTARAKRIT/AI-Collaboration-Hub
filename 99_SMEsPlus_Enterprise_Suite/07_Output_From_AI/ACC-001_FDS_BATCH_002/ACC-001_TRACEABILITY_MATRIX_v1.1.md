# ACC-001 Traceability Matrix v1.1

Document ID: SMEPLUS-ACC001-TRC-v1.1
Previous Version: SMEPLUS-STATE04-ACC-TRC-001 (20 FRs, 8 GAP)
Version: v1.1
Batch: FDS-ACC-BATCH-002
Status: DRAFTED — REQUIRES CHATGPT L99 REVIEW
Gate Status: HOLD / REVIEW REQUIRED
Owner: Functional Specification AI
Revised By: Claude AI (/L99.99, FDS-ACC-BATCH-002)
Generated: 2026-07-08 (Asia/Bangkok)

---

## Traceability Rule

No Traceability = No Gate Pass. No Gate Approval = No Next State.

## Chain

FR → BR → Business Process (WF) → Data Entity → API → UI Screen → Acceptance Criteria → Evidence → Gap Status → UAT Case → Gate

## Changes from v1.0

- FR-ACC-001 mis-mapping corrected (was mapped to Period Closing API/AC — now mapped to Setup APIs/AC)
- FR-ACC-011/012/013/015/018/019/020 previously GAP — now mapped
- Document Status Enumeration added to WF column
- All BR/API references updated to v1.1 numbering

---

## Full Traceability Matrix — All 20 FRs

| FR ID | Function | Business Rule(s) | Business Process (WF) | Data Entity | API Mapping | UI Screen | Acceptance Criteria | Evidence | Gap Status | UAT Case | Gate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FR-ACC-001 | Accounting Setup | BR-ACC-009, BR-ACC-010 | Config (no named WF) | DocumentSequence, TaxCode, WHTType, AccountingPeriod, FiscalYear | API-ACC-S01, S02, S03, S04, S05, S06, S07, S08 | SCR-ACC-002a, 002b, 002c, 002d | AC-ACC-022 | EVD-v1.1-001 | ADDRESSED — corrected from mis-mapping | Not yet defined | HOLD |
| FR-ACC-002 | Chart of Accounts | BR-ACC-010 | Config (no named WF) | Account | API-ACC-001, API-ACC-002 | SCR-ACC-003 | AC-ACC-022 | EVD-v1.1-001 | MATCHED | Not yet defined | HOLD |
| FR-ACC-003 | Journal Entry | BR-ACC-001, BR-ACC-015 | WF-ACC-001 (steps 1-3) | JournalEntry, JournalLine | API-ACC-003 | SCR-ACC-004, SCR-ACC-005 | AC-ACC-001, AC-ACC-002 | EVD-v1.1-001 | MATCHED | Not yet defined | HOLD |
| FR-ACC-004 | Journal Approval | BR-ACC-006 | WF-ACC-001 (steps 4-5) | JournalEntry, AuditLog | API-ACC-004, API-ACC-004b, API-ACC-004c | SCR-ACC-005 | AC-ACC-002, AC-ACC-006 | EVD-v1.1-001 | MATCHED | Not yet defined | HOLD |
| FR-ACC-005 | Journal Posting | BR-ACC-002 | WF-ACC-001 (steps 6-8) | JournalEntry, JournalLine | API-ACC-005 | SCR-ACC-005 | AC-ACC-003, AC-ACC-005a, AC-ACC-005b | EVD-v1.1-001 | MATCHED | Not yet defined | HOLD |
| FR-ACC-006 | Reverse Journal | BR-ACC-002, BR-ACC-014 | WF-ACC-001 (reversal branch) | JournalEntry | API-ACC-006 | SCR-ACC-005 | AC-ACC-007, AC-ACC-008 | EVD-v1.1-001 | MATCHED | Not yet defined | HOLD |
| FR-ACC-007 | Accounts Receivable | BR-ACC-008, BR-ACC-015 | WF-ACC-003 | Invoice, Receipt, TaxInvoice | API-ACC-007, API-ACC-012 | SCR-ACC-006, SCR-ACC-010a, SCR-ACC-010b | AC-ACC-012, AC-ACC-013, AC-ACC-014 | EVD-v1.1-001 | MATCHED | Not yet defined | HOLD |
| FR-ACC-008 | Accounts Payable | BR-ACC-007, BR-ACC-015 | WF-ACC-002 | Bill, PaymentVoucher, WHTCertificate | API-ACC-008, API-ACC-011c | SCR-ACC-007 | AC-ACC-019, AC-ACC-020 | EVD-v1.1-001 | MATCHED | Not yet defined | HOLD |
| FR-ACC-009 | VAT Management | BR-ACC-008, BR-ACC-013 | WF-ACC-002/003 VAT touchpoints | TaxInvoice, TaxCode | API-ACC-009 | SCR-ACC-008 | AC-ACC-012, AC-ACC-016, AC-ACC-018 | EVD-v1.1-001, EVD-v1.1-002 | PARTIAL — LEGAL_TAX_REVIEW_REQUIRED | Not yet defined | HOLD |
| FR-ACC-010 | WHT Management | BR-ACC-007 | WF-ACC-002 WHT touchpoint | WHTCertificate, WHTType | API-ACC-010, API-ACC-R03 | SCR-ACC-009, SCR-ACC-018 | AC-ACC-019, AC-ACC-020, AC-ACC-021 | EVD-v1.1-001, EVD-v1.1-002 | PARTIAL — LEGAL_TAX_REVIEW_REQUIRED | Not yet defined | HOLD |
| FR-ACC-011 | Tax Invoice | BR-ACC-011, BR-ACC-009 | WF-ACC-003 (TI issuance) | TaxInvoice, TaxCode, DocumentSequence | API-ACC-011, API-ACC-011b | SCR-ACC-010a | AC-ACC-015, AC-ACC-024, AC-ACC-025 | EVD-v1.1-001, EVD-v1.1-002 | ADDRESSED — was GAP; LEGAL_TAX_REVIEW_REQUIRED | Not yet defined | HOLD |
| FR-ACC-012 | Credit / Debit Note | BR-ACC-012, BR-ACC-009 | New WF (ref. §7) | CreditNote, DebitNote, DocumentSequence | API-ACC-CN01, CN02, DN01, DN02 | SCR-ACC-016, SCR-ACC-017 | AC-ACC-017, AC-ACC-018 | EVD-v1.1-001, EVD-v1.1-002 | ADDRESSED — was GAP; LEGAL_TAX_REVIEW_REQUIRED | Not yet defined | HOLD |
| FR-ACC-013 | Bank & Cash | BR-ACC-015 | WF-ACC-005 | BankAccount, BankStatement, StatementLine, ReconciliationMatch | API-ACC-BS01, BS02, BS03, BS04, BS05, BS06, API-ACC-011c | SCR-ACC-011a, SCR-ACC-011b, SCR-ACC-011c | AC-ACC-026 | EVD-v1.1-001 | ADDRESSED — was GAP | Not yet defined | HOLD |
| FR-ACC-014 | Period Closing | BR-ACC-004 | WF-ACC-004 | AccountingPeriod, FiscalYear | API-ACC-013 | SCR-ACC-012 | AC-ACC-009, AC-ACC-010, AC-ACC-011 | EVD-v1.1-001 | MATCHED | Not yet defined | HOLD |
| FR-ACC-015 | Financial Reports | BR-ACC-010 | Report generation (no named WF) | JournalEntry, JournalLine, Account | API-ACC-014, API-ACC-015, API-ACC-R01, API-ACC-R02 | SCR-ACC-013a, 013b, 013c, 013d | AC-ACC-022 | EVD-v1.1-001 | ADDRESSED — was GAP | Not yet defined | HOLD |
| FR-ACC-016 | Evidence Attachment | BR-ACC-005 | All document WFs | Evidence | SaaS Foundation API | SCR-ACC-014 | AC-ACC-026, AC-ACC-027 | EVD-v1.1-001 | MATCHED | Not yet defined | HOLD |
| FR-ACC-017 | Audit Trail | BR-ACC-006 | All document WFs | AuditLog | SaaS Foundation API | SCR-ACC-015 | AC-ACC-023 | EVD-v1.1-001 | MATCHED | Not yet defined | HOLD |
| FR-ACC-018 | Export Reports | BR-ACC-010 | Export (no named WF) | Report output layer | API-ACC-018 | SCR-ACC-019 | AC-ACC-022 | EVD-v1.1-001 | ADDRESSED — was GAP | Not yet defined | HOLD |
| FR-ACC-019 | API Integration | BR-ACC-010 | API contract (no named WF) | All entities | All API-ACC-* | — (API-only FR) | AC-ACC-023 | EVD-v1.1-001 | ADDRESSED — was GAP | Not yet defined | HOLD |
| FR-ACC-020 | Multi-Company/Branch | BR-ACC-009, BR-ACC-010 | All WFs (tenant scope) | All entities (tenant_id, company_id, branch_id) | All API-ACC-* (JWT) | All screens | AC-ACC-023 | EVD-v1.1-001 | ADDRESSED — was GAP | Not yet defined | HOLD |

---

## Summary

| Status | Count (v1.0) | Count (v1.1) |
|---|---|---|
| MATCHED (internal, unverified) | 10 | 10 |
| PARTIAL (legal review pending) | 2 | 2 (FR-ACC-009, 010) |
| ADDRESSED — corrected/completed | 0 | 7 (FR-ACC-001, 011, 012, 013, 015, 018, 019, 020 = 8 rows: 001 corrected + 7 previously GAP) |
| GAP | 8 | 0 |
| UAT cases defined | 0 | 0 |

All 20 FRs now have full chain mapping. Legal review required for FR-ACC-009/010/011/012.

## Gate Result

HOLD — traceability chain complete in v1.1 draft, but: (a) no row independently verified against source code/DB except FR-ACC-001 partial match via v0.2 matrix; (b) legal review items remain; (c) UAT cases not yet defined. Cannot support gate PASS.

PREPARED ONLY / NOT APPROVED / REQUIRES CHATGPT L99 REVIEW
