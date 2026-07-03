# FDS — Branch

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-BRN
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines Branch: an operational location under a Company (e.g., a retail outlet, warehouse, or
regional office). Branches let a Company operate across multiple physical or logical sites while
sharing one legal entity.

## 2. Scope
In Scope: branch hierarchy under company, branch-scoped data visibility, branch-level default
stock/location binding for Inventory.
Out of Scope: Division detail (see FDS_DIVISION.md), Inventory location detail (Inventory module FDS).

## 3. Depends On / Consumed By
Depends On: Company
Consumed By: Division, IAM (branch-scoped users), Approval (branch-based routing), Inventory, Sales

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| BRN-001 | Platform shall support branch hierarchy under a company | FD-004 | GAP — needs Database Design AI + evidence pass |
| BRN-002 | Platform shall support branch-level stock/location default binding for Inventory | FD-023 | See Matching Matrix |

## 5. Business Rules
BR-BRN-001: A branch belongs to exactly one company.
BR-BRN-002: A user's default branch scoping determines their default record visibility (see
FDS_PERMISSION.md for override rules).

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| Branch | id, company_id, name, address, is_active | Custom table — not a stock Odoo concept |

## 7. Process / State Flow
Branch Created -> Active -> Deactivated (soft delete, data retained)

## 8. Permission Notes
Branch Manager sees own-branch data by default; Admin/Owner can see all branches under the company.

## 9. Notification Events
- branch.created

## 10. Audit Events
- branch.created, branch.deactivated

## 11. Acceptance Criteria
AC-BRN-001: Given a Branch Manager logs in, when they view any module list view, then only their
assigned branch's records are shown by default.

## 12. Open Items
- Confirm exact table/model naming with Database Design AI (currently GAP status, no existing
  evidence found in efaplus dump or Odoo source).

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
