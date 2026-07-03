# FDS — Division

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-DIV
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines Division: a department/unit under a Branch (e.g., Sales Division, Warehouse Division within
one branch). Optional granularity layer for larger customers.

## 2. Scope
In Scope: division hierarchy under branch, division-scoped grouping for reporting/approval routing.
Out of Scope: Branch detail (see FDS_BRANCH.md), HR org-chart detail (HR module FDS, Priority 3).

## 3. Depends On / Consumed By
Depends On: Branch
Consumed By: IAM (optional division-scoped users), Approval (optional division-based routing), Reporting

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| DIV-001 | Platform shall support division/department under a branch | FD-005 | GAP |

## 5. Business Rules
BR-DIV-001: A division belongs to exactly one branch.
BR-DIV-002: Division is optional — a branch may operate with zero divisions defined for smaller
customers (simple case must not require division setup).

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| Division | id, branch_id, name, is_active | Custom table |

## 7. Process / State Flow
Division Created -> Active -> Deactivated (soft delete)

## 8. Permission Notes
Division-level scoping is an optional refinement of branch-level scoping (see FDS_PERMISSION.md).

## 9. Notification Events
- division.created

## 10. Audit Events
- division.created, division.deactivated

## 11. Acceptance Criteria
AC-DIV-001: Given a branch has no divisions defined, when a user views records, then branch-level
scoping alone governs visibility (division is not a blocking requirement).

## 12. Open Items
- Confirm whether Division is needed for Priority 1–2 modules or can be deferred to Priority 3 (HR).

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | No confirmed source — GAP, custom build required |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
