# FDS — Notification

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-NOT
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines Notification: in-app and email delivery of system events (approvals, tenant lifecycle,
subscription changes) to the right user at the right time.

## 2. Scope
In Scope: notification generation, delivery channels (in-app, email), read/unread state.
Out of Scope: SMS/LINE Notify integration (future hook only, see FDS_INTEGRATION.md).

## 3. Depends On / Consumed By
Depends On: IAM, Approval
Consumed By: all modules that raise events

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| NOT-001 | Platform shall send in-app notifications for pending approvals | FD-013 | MATCHED (Odoo mail.activity pattern) |
| NOT-002 | Platform shall send email notifications for key lifecycle events | FD-014 | MATCHED (Odoo mail.message/mail.template) |

## 5. Business Rules
BR-NOT-001: Notification content must include enough context (document type, reference number,
requester) to act without opening the full record, where practical.
BR-NOT-002: Users can mark notifications read and view notification history; history is not deleted
on read.

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| Notification | id, user_id, event_type, payload, read_at | Maps to Odoo mail.message/mail.activity pattern |
| NotificationPreference | user_id, channel, enabled | Per-user channel opt-in/out |

## 7. Process / State Flow
Event Raised -> Notification Created -> Delivered (in-app + optionally email) -> Read

## 8. Permission Notes
Users only see their own notifications; no cross-user visibility.

## 9. Notification Events
N/A (this domain is the delivery mechanism itself)

## 10. Audit Events
- notification.delivered (system-level, low priority — not part of business audit trail)

## 11. Acceptance Criteria
AC-NOT-001: Given an approval request is created, when the notification event fires, then the
assigned approver receives an in-app notification within the platform's defined latency target.

## 12. Open Items
- Confirm latency target (e.g. near-real-time vs. batched) with Architecture.
- Confirm whether SMS/LINE Notify is v1 or deferred (Thai SME market context — common expectation).

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | Odoo mail.message, mail.activity (standard, MATCHED) |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
