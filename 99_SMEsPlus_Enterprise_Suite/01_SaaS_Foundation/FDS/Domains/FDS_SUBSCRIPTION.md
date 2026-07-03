# FDS — Subscription

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-SUB
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines Subscription: the tenant-level plan that gates which modules/features are enabled, and
tracks billing status at a functional level (payment processing detail is out of scope here).

## 2. Scope
In Scope: subscription plan definition, feature flag gating, plan change (upgrade/downgrade).
Out of Scope: payment gateway integration detail (see FDS_INTEGRATION.md), invoicing (Accounting FDS).

## 3. Depends On / Consumed By
Depends On: Tenant
Consumed By: Module (enablement gating), Reporting (plan-tier report access)

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| SUB-001 | Platform shall support tenant-level subscription plan and feature flags | FD-017 | GAP (identified as FR-FD-003 critical gap in prior matrix — RFQ/vendor items similarly flagged) |

## 5. Business Rules
BR-SUB-001: A tenant has exactly one active Subscription Plan at a time.
BR-SUB-002: Downgrading a plan that disables a module already in use requires explicit confirmation
and does not delete existing data for that module.

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| SubscriptionPlan | id, name, feature_flags, price_tier | Custom table — GAP, no existing evidence |
| TenantSubscription | tenant_id, plan_id, status, renewed_at | Links Tenant to active plan |

## 7. Process / State Flow
Trial -> Active -> Past Due -> Suspended (see FDS_TENANT.md) -> Active (renewed) | Cancelled

## 8. Permission Notes
Only Tenant Owner can change subscription plan; Platform Operator can view/adjust for support cases.

## 9. Notification Events
- subscription.plan_changed
- subscription.payment_past_due
- subscription.renewed

## 10. Audit Events
- subscription.plan_changed (actor, old_plan, new_plan)

## 11. Acceptance Criteria
AC-SUB-001: Given a tenant's plan does not include a module, when a user attempts to access that
module, then access is blocked with an upgrade prompt.

## 12. Open Items
- Subscription Service is a confirmed critical GAP (previously flagged as FR-FD-003 in the
  Functional Design Matching Matrix, no existing implementation evidence). Requires new-build design.
- Confirm billing/payment integration approach with Enterprise Architect AI before finalizing.

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | No confirmed source — GAP, critical priority per prior Matching Matrix |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
