# TRACEABILITY_MATRIX.md

**Version:** v1.1  
**Status:** P0 Module Traceability Baseline  
**Owner:** Functional Specification AI / SMEsPlus PMO  
**Project:** SMEsPlus Enterprise Suite  
**Branch:** SMEsPlus  
**Last Updated:** 2026-07-06

---

# Purpose

เอกสารนี้ใช้ควบคุม Traceability ของ Functional Specification ตั้งแต่ Requirement ถึง Evidence และ Gate Result

This matrix links functional requirements to business rules, workflows, data mapping, API mapping, UI mapping, acceptance criteria, evidence, and gate result.

---

# Traceability Rule

ทุก Functional Requirement ต้องมีการเชื่อมโยงอย่างน้อย

```text
Functional Requirement
-> Business Rule
-> Business Process / Workflow
-> Module
-> Database Mapping
-> API / Event Mapping
-> UI Mapping
-> Acceptance Criteria
-> Evidence
-> Gate Result
```

No Evidence = No Progress

---

# Status Definition

| Status | Meaning |
|---|---|
| NEW | New requirement, not yet reviewed |
| MATCHED | Evidence and mapping are complete |
| PARTIAL | Some evidence exists but mapping is incomplete |
| GAP | Missing required evidence or mapping |
| HOLD | Cannot proceed until owner resolves issue |
| RETIRE | Requirement should not continue |
| APPROVED | Reviewed and accepted by authorized owner |

---

# Matrix

| FR ID | Function | Module | Business Rule ID | Workflow ID | DB Mapping | API/Event Mapping | UI Mapping | Acceptance Criteria | Evidence Location | Owner | Reviewer | Gate Result | Status | Next Action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FR-000 | AI Session Bootstrap Control | Repository Governance | BR-000 | WF-000 | N/A | N/A | N/A | AI can resume from repository source of truth | AI_SESSION_BOOTSTRAP.md | PMO AI / Liza | Repository Owner | REVIEW REQUIRED | PARTIAL | Keep bootstrap current |
| FR-001 | Functional Specification Bootstrap | Functional Design | BR-001 | WF-001 | Pending | Pending | Pending | Functional AI can start FDS without repeated explanation | FUNCTIONAL_SPECIFICATION_STANDARD.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose module FR IDs |
| FR-P0-001 | Authentication and Authorization Baseline | Authentication and Authorization | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_AUTHORIZATION.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-002 | Tenant Management Baseline | Tenant Management | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_TENANT_MANAGEMENT.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-003 | Organization Management Baseline | Organization Management | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_ORGANIZATION_MANAGEMENT.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-004 | User and Role Management Baseline | User and Role Management | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_USER_ROLE_MANAGEMENT.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-005 | Customer CRM Baseline | Customer CRM | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_CUSTOMER_CRM.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-006 | Sales Baseline | Sales | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_SALES.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-007 | Purchase Baseline | Purchase | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_PURCHASE.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-008 | Inventory Baseline | Inventory | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_INVENTORY.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-009 | Accounting Baseline | Accounting | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_ACCOUNTING.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-010 | Approval Engine Baseline | Approval Engine | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_APPROVAL_ENGINE.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-011 | Workflow Engine Baseline | Workflow Engine | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_WORKFLOW_ENGINE.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-012 | Notification Baseline | Notification | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_NOTIFICATION.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-013 | Dashboard Baseline | Dashboard | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_DASHBOARD.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-014 | Reporting Baseline | Reporting | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_REPORTING.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |
| FR-P0-015 | API Gateway Baseline | API Gateway | MODULE | MODULE | Baseline | Baseline | Baseline | Baseline | MODULE_SPEC_API_GATEWAY.md | Functional Specification AI | PMO AI | REVIEW REQUIRED | PARTIAL | Decompose into detailed FR records |

---

# Evidence Requirement

Evidence must include

- File path or link
- Owner
- Timestamp
- Reviewer or verifier
- Status
- Gate impact

If evidence is missing, mark status as `GAP` or `HOLD`.

---

# Functional Specification Use

Functional Specification AI must update this matrix when producing or reviewing

- Functional Specification
- Business Rules
- Workflow
- Database Mapping
- API Mapping
- UI Mapping
- Acceptance Criteria
- UAT / QA input

---

# Next Process

1. Create Functional Requirement Catalog.
2. Decompose each P0 module into detailed FR records.
3. Link each FR to Business Rule, Workflow, DB Mapping, API Mapping, UI Mapping, Acceptance Criteria, and Evidence.
4. Move module records from PARTIAL to MATCHED only after evidence is complete.

---

# End
