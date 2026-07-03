# FDS — Tenant

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-TEN
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines the Tenant entity: the top-level isolation boundary for every customer organization on the
SMEsPlus SaaS platform. All Company, Branch, User, and business data ultimately belong to exactly
one Tenant.

## 2. Scope
In Scope: tenant provisioning, status lifecycle (Pending Setup / Active / Suspended / Terminated),
data isolation, onboarding checklist, data export/portability.
Out of Scope: billing/payment processing detail (see FDS_SUBSCRIPTION.md), Company/Branch detail
(see FDS_COMPANY.md, FDS_BRANCH.md).

## 3. Depends On / Consumed By
Depends On: — (root entity)
Consumed By: Company, IAM, Subscription, Configuration, all business modules (indirectly)

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| TEN-001 | Platform shall support tenant provisioning with unique tenant identifier | FD-001 | See Matching Matrix |
| TEN-002 | Platform shall isolate data access strictly by tenant | FD-002 | See Matching Matrix |
| TEN-003 | Platform shall support tenant onboarding checklist/wizard | FD-027 | See Matching Matrix |
| TEN-004 | Platform shall support data export per tenant | FD-028 | See Matching Matrix |
| TEN-005 | Platform shall support tenant suspension without data deletion | FD-029 | See Matching Matrix |
| TEN-006 | Platform shall support tenant termination with data retention policy | FD-030 | See Matching Matrix |

## 5. Business Rules
BR-TEN-001: A user belongs to exactly one tenant; cross-tenant accounts are not permitted in v1.
BR-TEN-002: Suspended tenants retain read/export access but lose write access until reinstated.
BR-TEN-003: Terminated tenants' data is retained per data-retention policy before permanent deletion
(policy duration pending Legal/Compliance input).

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| Tenant | id, name, status, created_at, plan_id | Root isolation entity |
| TenantOnboardingChecklist | tenant_id, step, completed_at | Drives onboarding wizard UI |

## 7. Process / State Flow
Pending Setup -> Active -> Suspended -> Active (reinstated)
Active/Suspended -> Terminated (retention period) -> Deleted

## 8. Permission Notes
Only Platform Operator (internal) can Suspend/Terminate a tenant. Tenant Owner can initiate export
and view onboarding status.

## 9. Notification Events
- tenant.provisioned
- tenant.suspended
- tenant.reinstated
- tenant.terminated

## 10. Audit Events
- tenant.status_changed (actor, old_status, new_status, reason)

## 11. Acceptance Criteria
AC-TEN-001: Given a new tenant is provisioned, when a user from another tenant queries any
Foundation entity, then no data from this tenant is returned.
AC-TEN-002: Given a tenant is suspended, when the tenant attempts a write action, then the action
is blocked while read/export remains available.

## 12. Open Items
- Confirm multi-tenancy implementation strategy (company-level isolation vs. schema-per-tenant) via
  Architecture ADR.
- Confirm data retention duration for Terminated tenants (Legal/Compliance).

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | SMEsPlus custom SaaS control layer (no direct Odoo core equivalent; GAP per Matching Matrix) |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
