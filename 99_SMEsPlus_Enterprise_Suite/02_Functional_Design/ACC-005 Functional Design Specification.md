# ACC-005 Journal Posting — Functional Design Specification

Document ID: SMEPLUS-STATE04-ACC-005-FDS-001
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
Specification Package.md` §5 (FR-ACC-005), §6 (BR-ACC-002), §7 (WF-ACC-001
steps 6–8), §9, §10, §11, §12.

## 1. Purpose
Post approved journal entries into the general ledger, making them final and
locking them against direct edits (reversal-only from that point).

## 2. Scope
### In Scope
- Posting an approved journal, audit trail recording, GL/financial-report
  visibility
### Out of Scope
Same exclusions as ACC-001 §3. Reversal itself is FR-ACC-006 (not yet split
into a standalone file — remains inside ACC-001, listed NOT YET INCLUDED for
this batch per Boss instruction on ACC-006–010).

## 3. Functional Requirements
| FR ID | Function | Description | Priority | Reuse Type |
|---|---|---|---|---|
| FR-ACC-005 | Journal Posting | Post รายการบัญชีหลังอนุมัติ (post journal entry after approval) | Must | New |

## 4. Business Rules
| BR ID | Rule |
|---|---|
| BR-ACC-002 | รายการที่ post แล้วห้ามแก้ไขโดยตรง ต้อง reverse หรือ adjustment (posted entries cannot be edited directly — must be reversed or adjusted) |

## 5. Workflow — WF-ACC-001 Journal Entry Workflow (steps 6–8 relevant to this FR)
6. ระบบ post journal เมื่ออนุมัติ (system posts journal once approved)
7. ระบบบันทึก audit trail (system records audit trail)
8. รายการแสดงใน GL และรายงานการเงิน (entry appears in GL and financial reports)

## 6. Data Entities
| Entity | Key Fields |
|---|---|
| JournalEntry | journal_id, journal_no, journal_date, status, total_debit, total_credit |
| JournalLine | line_id, journal_id, account_id, debit, credit, description |

## 7. API Mapping
| API ID | Method | Endpoint | Purpose |
|---|---|---|---|
| API-ACC-005 | POST | /api/accounting/journals/{id}/post | Post journal |

## 8. UI Mapping
| Screen ID | Screen Name | Related FR |
|---|---|---|
| SCR-ACC-005 | Journal Entry Form | FR-ACC-005 |

## 9. Acceptance Criteria
| AC ID | Given | When | Then |
|---|---|---|---|
| AC-ACC-003 | Approver อนุมัติ journal | ระบบ post รายการ | รายการต้องแสดงใน GL (entry must appear in GL) |
| AC-ACC-004 | Journal post แล้ว | ผู้ใช้พยายามแก้ไข | ระบบต้องปฏิเสธและให้ reverse เท่านั้น (system must reject direct edit and allow only reversal) |

## 10. Evidence Requirement
Evidence exists only inside the consolidated ACC-001 document
(`EVD-04-ACC-001-DOC-20260707-001`/`-003`). No independent verification of the
post-lock enforcement (BR-ACC-002) has been performed — no code exists yet.

## 11. Traceability Requirement
See `12_Traceability/Requirement_Matrix/ACC-001_TRACEABILITY_MATRIX.md`, row
FR-ACC-005 — status: MATCHED (internal), not independently verified.

## 12. Gate Status
DRAFT. HOLD. Not APPROVED. Not BUILD READY. Ready only for ChatGPT L99 Re-Review
alongside the rest of this batch.
