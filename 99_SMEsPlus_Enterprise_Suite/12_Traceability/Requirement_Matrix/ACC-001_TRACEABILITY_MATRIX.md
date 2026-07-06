# ACC-001 Traceability Matrix (Module-Level)

Document ID: SMEPLUS-STATE04-ACC-TRC-001
Owner: Functional Specification AI
Reviewer: Not yet assigned
Approver: Boss / Final Gate Owner
Status: DRAFT
Gate Status: HOLD
Source: `02_Functional_Design/ACC-001 Accounting Thailand Functional Design Specification Package.md` §5–§12
Generated: 2026-07-07

## Traceability Rule
No Traceability = No Gate Pass. No Gate Approval = No Next State.

## Chain
Functional Requirement → Business Rule → Business Process (Workflow) → Data Entity → API / UI → Evidence → Gap Status → UAT Case → Gate Result

## Matrix — All 20 FRs from ACC-001 §5

| FR ID | Business Rule | Business Process (Workflow) | Data Entity | API / UI | Evidence | Gap Status | UAT Case | Gate Result |
|---|---|---|---|---|---|---|---|---|
| FR-ACC-001 Accounting Setup | BR-ACC-009 | Not in a named WF section | AccountingPeriod | API-ACC-013 / SCR-ACC-002 | EVD-04-ACC-001-DOC-20260707-002 (independently sourced, PARTIAL/MATCHED) | PARTIAL | Not yet defined | HOLD |
| FR-ACC-002 Chart of Accounts | BR-ACC-010 | Not in a named WF section | Account | API-ACC-001, API-ACC-002 / SCR-ACC-003 | EVD-04-ACC-001-DOC-20260707-001/003 | MATCHED (internal) | Not yet defined | HOLD |
| FR-ACC-003 Journal Entry | BR-ACC-001 | WF-ACC-001 Journal Entry Workflow | JournalEntry, JournalLine | API-ACC-003 / SCR-ACC-004, SCR-ACC-005 | EVD-04-ACC-001-DOC-20260707-001/003 | MATCHED (internal) | Not yet defined | HOLD |
| FR-ACC-004 Journal Approval | BR-ACC-006 | WF-ACC-001 steps 4–5 | JournalEntry, AuditLog | API-ACC-004 / SCR-ACC-005 | EVD-04-ACC-001-DOC-20260707-001/003 | MATCHED (internal) | Not yet defined | HOLD |
| FR-ACC-005 Journal Posting | BR-ACC-002 | WF-ACC-001 steps 6–8 | JournalEntry, JournalLine | API-ACC-005 / SCR-ACC-005 | EVD-04-ACC-001-DOC-20260707-001/003 | MATCHED (internal) | Not yet defined | HOLD |
| FR-ACC-006 Reverse Journal | BR-ACC-002 | Not in a named WF section | JournalEntry | API-ACC-006 / SCR-ACC-005 | EVD-04-ACC-001-DOC-20260707-001/003 | MATCHED (internal) | Not yet defined | HOLD |
| FR-ACC-007 Accounts Receivable | BR-ACC-008 | WF-ACC-003 AR / Receipt Workflow | Invoice, Receipt | API-ACC-007, API-ACC-012 / SCR-ACC-006 | EVD-04-ACC-001-DOC-20260707-001/003 | MATCHED (internal) | Not yet defined | HOLD |
| FR-ACC-008 Accounts Payable | BR-ACC-007 | WF-ACC-002 Expense / AP Workflow | Bill, PaymentVoucher | API-ACC-008, API-ACC-011 / SCR-ACC-007 | EVD-04-ACC-001-DOC-20260707-001/003 | MATCHED (internal) | Not yet defined | HOLD |
| FR-ACC-009 VAT Management | BR-ACC-008 | WF-ACC-002 / WF-ACC-003 (VAT touchpoints) | TaxInvoice | API-ACC-009 / SCR-ACC-008 | EVD-04-ACC-001-DOC-20260707-001/003/005 | PARTIAL (legal review pending) | Not yet defined | HOLD |
| FR-ACC-010 WHT Management | BR-ACC-007 | WF-ACC-002 (WHT touchpoint) | WHTCertificate | API-ACC-010 / SCR-ACC-009 | EVD-04-ACC-001-DOC-20260707-001/003/005 | PARTIAL (legal review pending) | Not yet defined | HOLD |
| FR-ACC-011 Tax Invoice | Not mapped in ACC-001 §12 | Not in a named WF section | TaxInvoice | SCR-ACC-010 (no API listed) | EVD-04-ACC-001-DOC-20260707-001 only | **GAP** — no BR/API mapping in source | Not yet defined | HOLD |
| FR-ACC-012 Credit / Debit Note | Not mapped in ACC-001 §12 | Not in a named WF section | Not explicitly listed in §8 | Not listed | EVD-04-ACC-001-DOC-20260707-001 only | **GAP** — no BR/DB/API/UI mapping in source | Not yet defined | HOLD |
| FR-ACC-013 Bank & Cash | Not mapped in ACC-001 §12 | Not in a named WF section | BankAccount | SCR-ACC-011 (no API listed) | EVD-04-ACC-001-DOC-20260707-001 only | **GAP** — no BR/API mapping in source | Not yet defined | HOLD |
| FR-ACC-014 Period Closing | BR-ACC-004 | WF-ACC-004 Period Closing Workflow | AccountingPeriod | API-ACC-013 / SCR-ACC-012 | EVD-04-ACC-001-DOC-20260707-001/003 | MATCHED (internal) | Not yet defined | HOLD |
| FR-ACC-015 Financial Reports | Not mapped in ACC-001 §12 | Not in a named WF section | Not explicitly listed | API-ACC-014, API-ACC-015 / SCR-ACC-013 | EVD-04-ACC-001-DOC-20260707-001 only | **GAP** — no BR mapping in source | Not yet defined | HOLD |
| FR-ACC-016 Evidence Attachment | BR-ACC-005 | Not in a named WF section | Evidence | SCR-ACC-014 (no API listed) | EVD-04-ACC-001-DOC-20260707-001/003 | MATCHED (internal) | Not yet defined | HOLD |
| FR-ACC-017 Audit Trail | BR-ACC-006 | Not in a named WF section | AuditLog | SCR-ACC-015 (no API listed) | EVD-04-ACC-001-DOC-20260707-001/003 | MATCHED (internal) | Not yet defined | HOLD |
| FR-ACC-018 Export Reports | Not mapped in ACC-001 §12 | Not in a named WF section | Not explicitly listed | Not listed | EVD-04-ACC-001-DOC-20260707-001 only | **GAP** — no BR/DB/API/UI mapping in source | Not yet defined | HOLD |
| FR-ACC-019 API Integration | Not mapped in ACC-001 §12 | Not in a named WF section | Not explicitly listed | Not listed | EVD-04-ACC-001-DOC-20260707-001 only | **GAP** — no BR/DB/API/UI mapping in source | Not yet defined | HOLD |
| FR-ACC-020 Multi-Company / Branch Accounting | Not mapped in ACC-001 §12 | Not in a named WF section | Implied across all entities (tenant/company/branch scope) | Not listed | EVD-04-ACC-001-DOC-20260707-001 only | **GAP** — no BR/API/UI mapping in source | Not yet defined | HOLD |

## Status Legend
- MATCHED (internal): mapping exists inside ACC-001 §12, not yet independently verified against source code/DB
- PARTIAL: mapping exists but a dependent evidence item (e.g., legal review) is still pending
- GAP: no mapping exists in ACC-001 at all for one or more chain links

## Summary
20 FRs total. 10 MATCHED (internal, unverified). 2 PARTIAL. 8 GAP. 0 independently verified end-to-end except FR-ACC-001 (via the central v0.2 matrix). No UAT cases defined for any FR yet.

## Gate Result
HOLD — traceability is materially incomplete (8/20 FRs have no mapping at all; only 1/20 has independent source-code/DB verification). Cannot support Functional Design gate PASS in current state.
