# ACC-003 Journal Entry — Functional Design Specification

Document ID: SMEPLUS-STATE04-ACC-003-FDS-001
Version: v0.1 (DRAFT — split from ACC-001)
Status: DRAFT
Gate Status: HOLD
Owner: Functional Specification AI
Reviewer: Not yet assigned
Approver: Boss / Final Gate Owner

## Execution Control Metadata (Batch 01 remediation — 2026-07-14)

| Field | Value |
|---|---|
| Draft Status | DRAFT — split from ACC-001; not independently authored |
| Reviewer | Not yet assigned (named independent reviewer required; must not be Claude) |
| Reviewer Sign-off | NONE |
| Build Eligibility | NOT BUILD ELIGIBLE |
| Execution Evidence | NONE (no build/test/execution evidence exists) |
| Gate Status | HOLD |
| Authoritative Gate Status | See `CURRENT_GATE_STATUS.md` (HOLD — NEED EXECUTION EVIDENCE) |
| Batch Manifest | `ACC_GAP_CLOSURE_BATCH01_MANIFEST_SHA256.txt` |

This metadata does not approve, verify, or build-qualify the document. It records that the file remains a reviewer-unconfirmed draft with no execution evidence.
Source: extracted from `ACC-001 Accounting Thailand Functional Design
Specification Package.md` §5 (FR-ACC-003), §6 (BR-ACC-001), §7 (WF-ACC-001), §8,
§9, §10, §11, §12.

## 1. Purpose
Record double-entry journal transactions (debit/credit) as the core general
ledger input mechanism for SMEsPlus Accounting.

## 2. Scope
### In Scope
- Manual journal entry creation, evidence attachment, submission for approval
### Out of Scope
Per ACC-001 §3 (payroll calc, inventory costing, manufacturing cost accounting,
direct bank payment execution, direct e-Filing unless approved).

## 3. Functional Requirements
| FR ID | Function | Description | Priority | Reuse Type |
|---|---|---|---|---|
| FR-ACC-003 | Journal Entry | บันทึกรายการบัญชี เดบิต เครดิต (record journal transactions, debit/credit) | Must | New |

## 4. Business Rules
| BR ID | Rule |
|---|---|
| BR-ACC-001 | Journal Entry ต้องมี Debit = Credit ก่อนบันทึกหรือ post (debit must equal credit before saving or posting) |

## 5. Workflow — WF-ACC-001 Journal Entry Workflow (steps 1–3 relevant to this FR)
1. Accountant สร้าง Journal Entry (accountant creates journal entry)
2. ระบบตรวจ Debit = Credit (system validates debit = credit)
3. แนบ evidence (attach evidence)
(Steps 4–8 — approval and posting — belong to ACC-004 and ACC-005 respectively;
see those documents.)

## 6. Data Entities
| Entity | Key Fields |
|---|---|
| JournalEntry | journal_id, journal_no, journal_date, status, total_debit, total_credit |
| JournalLine | line_id, journal_id, account_id, debit, credit, description |

## 7. API Mapping
| API ID | Method | Endpoint | Purpose |
|---|---|---|---|
| API-ACC-003 | POST | /api/accounting/journals | Create journal |

## 8. UI Mapping
| Screen ID | Screen Name | Related FR |
|---|---|---|
| SCR-ACC-004 | Journal Entry List | FR-ACC-003 |
| SCR-ACC-005 | Journal Entry Form | FR-ACC-003 |

## 9. Acceptance Criteria
| AC ID | Given | When | Then |
|---|---|---|---|
| AC-ACC-001 | ผู้ใช้สร้าง journal | Debit และ Credit ไม่เท่ากัน | ระบบต้องไม่ให้ submit (system must block submission) |

## 10. Evidence Requirement
Evidence exists only inside the consolidated ACC-001 document
(`EVD-04-ACC-001-DOC-20260707-001`/`-003`). No independent verification of the
debit=credit validation logic has been performed (no code exists yet — Build
Ready gate not reached).

## 11. Traceability Requirement
See `12_Traceability/Requirement_Matrix/ACC-001_TRACEABILITY_MATRIX.md`, row
FR-ACC-003 — status: MATCHED (internal), not independently verified.

## 12. Gate Status
DRAFT. HOLD. Not APPROVED. Not BUILD READY. Ready only for ChatGPT L99 Re-Review
alongside the rest of this batch.
