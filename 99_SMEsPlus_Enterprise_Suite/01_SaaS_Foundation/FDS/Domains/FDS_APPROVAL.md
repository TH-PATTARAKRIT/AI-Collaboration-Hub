# FDS — Approval

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-APR
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines the generic multi-level Approval Workflow Engine reused by Purchase, Accounting, HR, and
other modules — one engine, many document types.

## 2. Scope
In Scope: approval workflow definition, request routing, approve/reject/return, delegation.
Out of Scope: module-specific approval business rules (e.g. Purchase Order thresholds — see Purchase
module FDS).

## 3. Depends On / Consumed By
Depends On: IAM, Role
Consumed By: Notification, Audit, Purchase, Accounting, HR (as document-type consumers)

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| APR-001 | Platform shall support a generic multi-level approval workflow engine | FD-010 | PARTIAL — evidenced by efaplus purchase_order_level_reject/purchase_request_level_reject pattern, pending TASK-005 source confirmation |
| APR-002 | Approval engine shall support reject-with-reason and return-to-requester | FD-011 | PARTIAL |
| APR-003 | Approval engine shall support configurable approval levels per document type | FD-012 | PARTIAL |
| APR-004 | Platform shall support delegation of approval authority (out-of-office) | FD-024 | GAP |

## 5. Business Rules
BR-APR-001: Approval routing is determined by document type + amount/threshold + requester's
role/branch.
BR-APR-002: A rejected approval request returns to the requester with a mandatory reject reason; it
does not auto-escalate.
BR-APR-003: Only an active user can be assigned as an Approver (see FDS_IAM.md BR-IAM-002).
BR-APR-004: Delegated approval authority must be time-bound (start/end date) and logged as a
distinct audit event from the delegate's own approvals.

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| ApprovalWorkflow | id, document_type, levels_config | Definition — evidenced pattern pending confirmation |
| ApprovalRequest | id, workflow_id, linked_record, current_level, status | Instance |
| ApprovalDelegation | delegator_id, delegate_id, start_date, end_date | GAP — new build |

## 7. Process / State Flow
Draft -> Submitted -> Pending Level N -> Approved | Rejected
Rejected -> Draft (on resubmission)

## 8. Permission Notes
Approval authority is role/threshold-based, not tied to a fixed persona name (see 20_PERMISSION
equivalent mapping in master FDS).

## 9. Notification Events
- approval.request_created (to first-level approver)
- approval.level_advanced (to next-level approver)
- approval.approved (to requester)
- approval.rejected (to requester, with reason)

## 10. Audit Events
- approval.decision (actor, level, decision, reason, timestamp) — first-class event, not just a
  status field change

## 11. Acceptance Criteria
AC-APR-001: Given an approval workflow with 2 levels, when a document is submitted, then it routes
to Level 1 first and only reaches Level 2 after Level 1 approval.
AC-APR-002: Given a Level 1 rejection, when the requester views the document, then they see the
reject reason and the document returns to Draft without reaching Level 2.

## 12. Open Items
- TASK-005: confirm source access/licensing for the `efaplus`-owned approval tables before treating
  this design as final rather than PARTIAL-evidenced.
- Confirm whether delegation (APR-004) is v1 scope or deferred.

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | efaplus dump: purchase_request, purchase_order_level_reject, purchase_request_level_reject (PARTIAL, pending TASK-005) |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
