# ACC-002 Chart of Accounts — Functional Design Specification

Document ID: SMEPLUS-STATE04-ACC-002-FDS-001
Version: v0.1 (DRAFT — split from ACC-001)
Status: DRAFT
Gate Status: HOLD
Owner: Functional Specification AI
Reviewer: Not yet assigned
Approver: Boss / Final Gate Owner
Source: extracted and expanded from `ACC-001 Accounting Thailand Functional Design
Specification Package.md` §5 (FR-ACC-002), §6 (BR-ACC-010), §8, §9, §10, §12.
This is a split-out draft, not a newly invented requirement — content traces back
to the consolidated ACC-001 package.

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

## 1. Purpose
Provide chart-of-accounts management for SMEsPlus Accounting (Thailand): creating,
organizing, and maintaining the account tree used by all downstream journal,
AR/AP, and reporting functions.

## 2. Scope
### In Scope
- Create / read / update chart-of-accounts entries
- Parent-child account hierarchy
- Account type classification
### Out of Scope (per ACC-001 §3)
- Full payroll calculation, inventory costing, manufacturing cost accounting
- Direct e-Filing / certified e-Tax provider submission unless integration approved

## 3. Functional Requirements
| FR ID | Function | Description | Priority | Reuse Type |
|---|---|---|---|---|
| FR-ACC-002 | Chart of Accounts | สร้างและจัดการผังบัญชี (create and manage chart of accounts) | Must | New |

## 4. Business Rules
| BR ID | Rule |
|---|---|
| BR-ACC-010 | ผู้ใช้ต้องมี permission ตาม role และ scope ก่อนเข้าถึงรายการบัญชี (user must have role/scope permission before accessing accounting records) |

## 5. Workflow
**GAP:** ACC-001 does not define a dedicated workflow section for Chart of
Accounts setup (no WF-ACC-00X covers this). Assumed to be a standard admin
CRUD workflow (create → validate hierarchy → save → audit log), but this is
an assumption, not sourced from ACC-001. Requires reviewer confirmation.

## 6. Data Entities
| Entity | Key Fields |
|---|---|
| Account | account_id, account_code, account_name, account_type, parent_account_id |

## 7. API Mapping
| API ID | Method | Endpoint | Purpose |
|---|---|---|---|
| API-ACC-001 | GET | /api/accounting/accounts | Get chart of accounts |
| API-ACC-002 | POST | /api/accounting/accounts | Create account |

## 8. UI Mapping
| Screen ID | Screen Name | Related FR |
|---|---|---|
| SCR-ACC-003 | Chart of Accounts | FR-ACC-002 |

## 9. Acceptance Criteria
| AC ID | Given | When | Then |
|---|---|---|---|
| AC-ACC-008 | ผู้ใช้ไม่มี permission | เข้าหน้ารายงานบัญชี | ระบบต้องปฏิเสธการเข้าถึง (system must deny access) |

**Gap:** no acceptance criterion in ACC-001 specifically covers account-hierarchy
validation (e.g., preventing circular parent references). Not yet defined.

## 10. Evidence Requirement
Evidence for this FR currently exists only as a row inside the consolidated
ACC-001 document (`EVD-04-ACC-001-DOC-20260707-001` / `-003` in
`07_Output_From_AI/ACC-001_EVIDENCE_REGISTER.md`). No independent source-code/DB
verification has been performed for Chart of Accounts specifically.

## 11. Traceability Requirement
See `12_Traceability/Requirement_Matrix/ACC-001_TRACEABILITY_MATRIX.md`, row
FR-ACC-002 — status: MATCHED (internal), not independently verified.

## 12. Gate Status
DRAFT. HOLD. Not APPROVED. Not BUILD READY. Ready only for ChatGPT L99 Re-Review
alongside the rest of this batch.
