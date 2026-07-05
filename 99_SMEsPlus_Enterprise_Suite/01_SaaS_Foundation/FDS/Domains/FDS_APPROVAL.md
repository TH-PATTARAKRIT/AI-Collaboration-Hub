# FDS\_APPROVAL.md

Document ID: FDS-DOMAIN-APPROVAL-001

Version: v1.0.0

Status: Draft

Owner: SMEsPlus Product Team

Domain: Approval Workflow

Target Path:

`01\_SaaS\_Foundation/FDS/Domains/FDS\_APPROVAL.md`

---

# 1. Purpose

Approval Domain เป็นระบบกลางสำหรับการอนุมัติเอกสาร รายการ และธุรกรรมของทุก Module ภายใน SMEsPlus

ระบบต้องสามารถนำกลับไปใช้ซ้ำ (Reusable Workflow Engine) ได้โดยไม่ต้องพัฒนา Workflow ใหม่ในแต่ละ Module

---

# 2. Scope

## In Scope

- Approval Workflow

- Approval Step

- Approver Assignment

- Approve

- Reject

- Send Back

- Cancel Request

- Approval History

- Approval Notification

## Out of Scope

- BPM Engine

- Workflow Designer

- AI Approval

---

# 3. Actors

| Actor | Description |

|--------|-------------|

| Requester | ผู้ส่งคำขอ |

| Approver | ผู้อนุมัติ |

| Company Admin | จัดการ Workflow |

| Auditor | ตรวจสอบประวัติ |

---

# 4. Functional Requirements

## FR-APR-001 Create Approval Request

Permission

approval.request.create

API

POST /approval-requests

Acceptance Criteria

- Request Created

- Workflow Assigned

- Notification Sent

- Audit Recorded

---

## FR-APR-002 Approve Request

Permission

approval.approve

API

POST /approval-requests/{id}/approve

Acceptance Criteria

- Status = Approved

- Next Step Started

- Audit Recorded

---

## FR-APR-003 Reject Request

Permission

approval.reject

API

POST /approval-requests/{id}/reject

Acceptance Criteria

- Status = Rejected

- Comment Required

- Audit Recorded

---

## FR-APR-004 Send Back

Permission

approval.sendback

Acceptance Criteria

- Request Returned

- Reason Required

---

## FR-APR-005 Cancel Request

Permission

approval.cancel

Acceptance Criteria

- Only Requester

- Only Pending Status

- Audit Recorded

---

## FR-APR-006 View Approval History

Permission

approval.history

Acceptance Criteria

- Timeline Display

- Actor Display

- Timestamp Display

---

## FR-APR-007 Approval Dashboard

Permission

approval.read

Acceptance Criteria

- Pending

- Approved

- Rejected

- Waiting

---

# 5. Business Rules

BR-APR-001

Workflow Immutable After Start

BR-APR-002

Rejected Workflow Ends

BR-APR-003

Only Assigned Approver Can Approve

BR-APR-004

Approval History Cannot Be Deleted

---

# 6. User Stories

US-APR-001

Requester submits request.

US-APR-002

Approver approves request.

US-APR-003

Auditor reviews approval history.

---

# 7. Screen Mapping

UX-APR-001 Approval Inbox

UX-APR-002 Approval Detail

UX-APR-003 Approval Timeline

---

# 8. API Mapping

POST /approval-requests

POST /approval-requests/{id}/approve

POST /approval-requests/{id}/reject

POST /approval-requests/{id}/sendback

POST /approval-requests/{id}/cancel

GET /approval-history

---

# 9. Database Mapping

approval\_requests

approval\_steps

approval\_histories

approval\_comments

---

# 10. Security

RBAC

Tenant Isolation

Audit Required

---

# 11. Traceability

FR → SDS → API → DB → UX → QA

---

# 12. Status

Ready for SDS/API/DB/QA