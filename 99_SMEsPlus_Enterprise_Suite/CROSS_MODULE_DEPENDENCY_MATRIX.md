# CROSS_MODULE_DEPENDENCY_MATRIX.md

Version: v0.1
Status: Draft Baseline
Project: SMEsPlus Enterprise Suite
Mode: L99
Owner: Functional Specification AI
Updated: 2026-07-06

---

# Purpose

This matrix identifies dependency between P0 modules for functional design, integration, UI flow, data flow, and testing.

---

# Dependency Matrix

| Source Module | Depends On | Dependency Type | Evidence | Status |
|---|---|---|---|---|
| Sales | Customer CRM | Customer selection | MODULE_SPEC_SALES.md | PARTIAL |
| Sales | Inventory | Fulfillment reference | MODULE_SPEC_SALES.md | PARTIAL |
| Sales | Accounting | Invoice and revenue reference | MODULE_SPEC_SALES.md | PARTIAL |
| Purchase | Inventory | Receiving reference | MODULE_SPEC_PURCHASE.md | PARTIAL |
| Purchase | Accounting | Vendor bill reference | MODULE_SPEC_PURCHASE.md | PARTIAL |
| Inventory | Product and Organization | Stock scope reference | MODULE_SPEC_INVENTORY.md | PARTIAL |
| Accounting | Sales and Purchase | Posting source reference | MODULE_SPEC_ACCOUNTING.md | PARTIAL |
| Approval Engine | Sales and Purchase | Approval process reference | MODULE_SPEC_APPROVAL_ENGINE.md | PARTIAL |
| Workflow Engine | Approval Engine | Status flow reference | MODULE_SPEC_WORKFLOW_ENGINE.md | PARTIAL |
| Notification | Approval Engine and Workflow Engine | Alert trigger reference | MODULE_SPEC_NOTIFICATION.md | PARTIAL |
| Dashboard | Sales, Purchase, Inventory, Accounting | KPI source reference | MODULE_SPEC_DASHBOARD.md | PARTIAL |
| Reporting | All P0 modules | Report source reference | MODULE_SPEC_REPORTING.md | PARTIAL |
| API Gateway | All P0 modules | API entry reference | MODULE_SPEC_API_GATEWAY.md | PARTIAL |

---

# Rule

No Evidence equals No Progress.

---

# Next Process

1. Validate each dependency during detailed FR decomposition.
2. Link dependency to API, DB entity, UI flow, and UAT case.
3. Move status from PARTIAL to MATCHED only after evidence is complete.

---

# End
