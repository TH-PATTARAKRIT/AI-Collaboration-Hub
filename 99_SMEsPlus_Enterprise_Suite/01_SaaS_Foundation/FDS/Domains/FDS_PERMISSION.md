# FDS — Permission

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-PRM
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines Permission: fine-grained, action-on-object access rights, and record-level rules (e.g.
branch-scoped visibility) that compose into Roles.

## 2. Scope
In Scope: permission model (module/action/object), record rules for tenant/branch/division scoping.
Out of Scope: Role bundling logic (see FDS_ROLE.md).

## 3. Depends On / Consumed By
Depends On: Role
Consumed By: all modules (access enforcement)

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| PRM-001 | Platform shall support custom permission groups per module | FD-008 | MATCHED (Odoo ir.model.access) |
| PRM-002 | Platform shall support record-level access rules (e.g. branch-scoped visibility) | FD-009 | MATCHED (Odoo ir.rule) |

## 5. Business Rules
BR-PRM-001: Record-level rules (branch/division scoping) are enforced at the data-access layer, not
only in the UI (see FDS_TENANT.md NFR/security cross-reference).
BR-PRM-002: Permission changes are additive within a role; removing a permission from a role removes
it from all users holding only that role.

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| Permission | id, module, action, object | Maps to Odoo ir.model.access |
| RecordRule | id, model, domain_filter, role_id | Maps to Odoo ir.rule |

## 7. Process / State Flow
N/A — Permission is a configuration entity, not a lifecycle-driven one.

## 8. Permission Notes
See 20_PERMISSION_MAPPING equivalent in the master FDS for the persona x action matrix.

## 9. Notification Events
None directly — permission changes surface via role.permissions_changed (see FDS_ROLE.md).

## 10. Audit Events
- permission.assigned_to_role, permission.removed_from_role

## 11. Acceptance Criteria
AC-PRM-001: Given a Branch Manager role has a branch-scoped record rule, when that user queries any
governed model, then only records matching their branch are returned.

## 12. Open Items
- None currently blocking; depends on FDS_ROLE.md open items.

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | Odoo ir.model.access, ir.rule (standard, MATCHED) |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
