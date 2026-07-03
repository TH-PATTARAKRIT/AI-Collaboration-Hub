# FDS — Module

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-MOD
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines Module: the registry of enable/disable-able functional module groups (Accounting, Purchase,
Inventory, Sales, CRM, Manufacturing, HR, Payroll, etc.) available to a tenant, gated by Subscription.
Supports BO-004 (future module marketplace).

## 2. Scope
In Scope: module registry, enable/disable per tenant, dependency checking between modules.
Out of Scope: individual module business logic (owned by each module's own FDS package).

## 3. Depends On / Consumed By
Depends On: Subscription
Consumed By: Integration (module-to-module contract), all business modules (enablement check)

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| MOD-001 | Platform shall support module enable/disable per tenant based on subscription | FD-017 (shared with Subscription) | GAP |
| MOD-002 | Platform shall enforce module dependency rules (e.g. Purchase may require Inventory) | New — not in original FD-001..030 set | GAP — NEW |

## 5. Business Rules
BR-MOD-001: A module cannot be enabled if its declared dependencies are not also enabled.
BR-MOD-002: Disabling a module hides its UI/menu but does not delete its data (supports re-enable).

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| Module | id, code, name, depends_on | Registry entity — GAP, no existing evidence |
| TenantModule | tenant_id, module_id, is_enabled | Per-tenant enablement state |

## 7. Process / State Flow
Available -> Enabled -> Disabled -> Enabled (re-enable, data intact)

## 8. Permission Notes
Only Tenant Owner (within plan limits) or Platform Operator can enable/disable modules.

## 9. Notification Events
- module.enabled
- module.disabled

## 10. Audit Events
- module.enabled, module.disabled (actor, module_code)

## 11. Acceptance Criteria
AC-MOD-001: Given a tenant disables Inventory while Purchase (which depends on it) is enabled, when
the disable action is attempted, then the system blocks it and explains the dependency.

## 12. Open Items
- This domain is flagged NEW (not present in the original FD-001–030 set) — requires PMO AI
  confirmation it should be added to the Matching Matrix as a tracked requirement.

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | No confirmed source — GAP / NEW |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
