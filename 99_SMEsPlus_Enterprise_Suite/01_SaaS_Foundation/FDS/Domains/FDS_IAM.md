# FDS — IAM (Identity & Access Management)

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-IAM
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines User identity: authentication, session management, and user lifecycle within a Tenant. IAM
is the base for Role and Permission (see FDS_ROLE.md, FDS_PERMISSION.md).

## 2. Scope
In Scope: user creation, authentication, password policy, deactivation, bulk invitation, SSO support.
Out of Scope: role/permission assignment logic (see FDS_ROLE.md, FDS_PERMISSION.md).

## 3. Depends On / Consumed By
Depends On: Tenant
Consumed By: Role, Approval (as requester/approver), Audit (as actor), Notification (as recipient)

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| IAM-001 | Platform shall support user creation scoped to a tenant | FD-006 | MATCHED (Odoo res.users, extended) |
| IAM-002 | Platform shall support SSO/standard authentication mechanisms | FD-019 | See Matching Matrix |
| IAM-003 | Platform shall support password policy configuration per tenant | FD-020 | See Matching Matrix |
| IAM-004 | Platform shall support user deactivation without data loss | FD-021 | MATCHED (Odoo active flag pattern) |
| IAM-005 | Platform shall support bulk user invitation | FD-025 | See Matching Matrix |

## 5. Business Rules
BR-IAM-001: A user belongs to exactly one tenant (see BR-TEN-001).
BR-IAM-002: Only an active user can be assigned as an Approver (see FDS_APPROVAL.md BR-APR-003).
BR-IAM-003: Deactivating a user preserves their historical records (audit trail, approval history)
— it is a soft state change, not a delete.

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| User | id, tenant_id, email, status, default_branch_id | Maps to Odoo res.users, extended with tenant_id |
| UserInvitation | id, tenant_id, email, invited_by, status | Bulk invite tracking |

## 7. Process / State Flow
Invited -> Active -> Deactivated -> Active (reactivated)

## 8. Permission Notes
Admin/Tenant Owner manage users. Users manage their own profile/password within policy limits.

## 9. Notification Events
- user.invited
- user.deactivated
- user.password_reset_requested

## 10. Audit Events
- user.created, user.deactivated, user.role_changed, user.login_failed (security-relevant)

## 11. Acceptance Criteria
AC-IAM-001: Given a user is deactivated, when historical records they authored are viewed, then
those records remain intact and attributed to that user.

## 12. Open Items
- Confirm SSO provider(s) to support (Google Workspace, Microsoft, or platform-native only) —
  Architecture decision pending.

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | Odoo res.users (standard, MATCHED, extended with tenant_id) |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
