# ACC-004 Journal Approval — Functional Design Specification

Document ID: SMEPLUS-STATE04-ACC-004-FDS-001
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
Specification Package.md` §5 (FR-ACC-004), §6 (BR-ACC-006), §7 (WF-ACC-001
steps 4–5), §9, §10, §11, §12.

## 1. Purpose
Route journal entries through an approval step before they can be posted to the
general ledger, ensuring accountability and control over financial postings.

## 2. Scope
### In Scope
- Submit-for-approval action, approver decision (approve / reject / request
  revision), approval audit trail
### Out of Scope
Same exclusions as ACC-001 §3.

## 3. Functional Requirements
| FR ID | Function | Description | Priority | Reuse Type |
|---|---|---|---|---|
| FR-ACC-004 | Journal Approval | ส่งอนุมัติรายการบัญชี (submit journal entry for approval) | Must | Reuse Approval |

## 4. Business Rules
| BR ID | Rule |
|---|---|
| BR-ACC-006 | การอนุมัติทุกครั้งต้องบันทึก approver, timestamp, decision (every approval must record approver, timestamp, decision) |

## 5. Workflow — WF-ACC-001 Journal Entry Workflow (steps 4–5 relevant to this FR)
4. ส่งอนุมัติ (submit for approval)
5. Approver อนุมัติ / Reject / Request Revision (approver approves / rejects / requests revision)

## 6. Data Entities
| Entity | Key Fields |
|---|---|
| JournalEntry | journal_id, journal_no, journal_date, status, total_debit, total_credit |
| AuditLog | audit_id, ref_type, ref_id, action, actor_id, timestamp |

## 7. API Mapping
| API ID | Method | Endpoint | Purpose |
|---|---|---|---|
| API-ACC-004 | POST | /api/accounting/journals/{id}/submit | Submit journal for approval |

## 8. UI Mapping
| Screen ID | Screen Name | Related FR |
|---|---|---|
| SCR-ACC-005 | Journal Entry Form | FR-ACC-004 |

## 9. Acceptance Criteria
| AC ID | Given | When | Then |
|---|---|---|---|
| AC-ACC-002 | Journal มี evidence ครบ | ผู้ใช้ submit approval | ระบบต้องสร้าง approval task (system must create an approval task) |
| AC-ACC-010 | รายการอนุมัติถูก reject | ผู้ใช้เปิดเอกสาร | สถานะต้องเป็น Rejected และแก้ไขส่งใหม่ได้ (status must be Rejected and re-submittable) |

## 10. Evidence Requirement
Evidence exists only inside the consolidated ACC-001 document
(`EVD-04-ACC-001-DOC-20260707-001`/`-003`). "Reuse Approval" reuse-type per
ACC-001 §5 implies this should reuse an existing SaaS Foundation approval
engine — that reuse mapping/reference has not yet been confirmed against
`01_SaaS_Foundation/` (out of scope for this batch; flagged for follow-up).

## 11. Traceability Requirement
See `12_Traceability/Requirement_Matrix/ACC-001_TRACEABILITY_MATRIX.md`, row
FR-ACC-004 — status: MATCHED (internal), not independently verified.

## 12. Gate Status
DRAFT. HOLD. Not APPROVED. Not BUILD READY. Ready only for ChatGPT L99 Re-Review
alongside the rest of this batch.
