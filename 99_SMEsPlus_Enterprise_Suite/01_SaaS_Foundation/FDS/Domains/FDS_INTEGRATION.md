# FDS — Integration

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-INT
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines Integration: the stable API contract surface that lets modules (Accounting, Purchase,
Inventory, etc.) and external systems (e-Tax invoice, banking, SMS/LINE Notify) consume Foundation
services without duplicating logic.

## 2. Scope
In Scope: internal module-to-module API contract, external integration hook points, versioning.
Out of Scope: specific external system implementation (e.g. actual e-Tax invoice integration — that
belongs to the Accounting module FDS).

## 3. Depends On / Consumed By
Depends On: Module
Consumed By: all business modules, external systems

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| INT-001 | Platform shall expose a stable API contract for module integration | FD-018 | GAP |

## 5. Business Rules
BR-INT-001: API contract versioning must be defined so module updates don't silently break other
modules (supports BO-004 marketplace goal).
BR-INT-002: External integration points are exposed only through defined hooks (event subscriptions),
not direct database access.

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| APIContractVersion | id, module_code, version, deprecated_at | GAP — no existing evidence |
| IntegrationWebhook | id, event_type, target_url, tenant_id | For external system hooks |

## 7. Process / State Flow
N/A — contract/configuration entity.

## 8. Permission Notes
Only Admin/Platform Operator can configure external integration webhooks.

## 9. Notification Events
- integration.webhook_failed (to Admin, operational alert)

## 10. Audit Events
- integration.webhook_configured, integration.api_version_deprecated

## 11. Acceptance Criteria
AC-INT-001: Given a module is updated to a new API version, when a consuming module still calls the
prior version, then the prior version continues to function until its declared deprecation date.

## 12. Open Items
- API gateway approach is pending an Architecture ADR (see FDS_TENANT.md/master FDS Appendix C).
- Full OpenAPI-level contract to be produced jointly with Integration AI once ADR lands.

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | No confirmed source — GAP, pending Architecture ADR |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
