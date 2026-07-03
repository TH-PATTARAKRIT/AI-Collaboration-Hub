# FDS — Role

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-ROL
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines Role: a named bundle of Permissions assigned to Users. Roles let Admins manage access at the
job-function level instead of per-permission.

## 2. Scope
In Scope: role creation/editing, role templates for common personas, role assignment to users.
Out of Scope: fine-grained permission definitions (see FDS_PERMISSION.md).

## 3. Depends On / Consumed By
Depends On: IAM
Consumed By: Permission, Approval (role-based routing), all modules (access gating)

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| ROL-001 | Platform shall support role-based access control | FD-007 | MATCHED (Odoo res.groups) |
| ROL-002 | Platform shall support role templates for common personas | FD-026 | See Matching Matrix |

## 5. Business Rules
BR-ROL-001: Role permission changes take effect immediately for new sessions; existing sessions may
require re-authentication (exact behavior pending Architecture confirmation).
BR-ROL-002: A user may be assigned more than one role; effective permissions are the union.

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| Role | id, tenant_id, name, is_template | Maps to Odoo res.groups, extended |
| RoleTemplate | id, name, description | Seed data for common personas (P-001..P-006) |
| UserRole | user_id, role_id | Assignment join table |

## 7. Process / State Flow
Role Defined -> Assigned to User(s) -> Edited (propagates to all assigned users) -> Archived

## 8. Permission Notes
Only Admin/Tenant Owner can create or edit Roles.

## 9. Notification Events
- role.assigned (to the affected user, informational)

## 10. Audit Events
- role.created, role.permissions_changed, role.assigned_to_user

## 11. Acceptance Criteria
AC-ROL-001: Given an Admin edits a Role's permissions, when an assigned user's session refreshes,
then the new permission set is enforced.

## 12. Open Items
- Confirm session-refresh vs. immediate-enforcement behavior with Architecture.

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | Odoo res.groups (standard, MATCHED) |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
