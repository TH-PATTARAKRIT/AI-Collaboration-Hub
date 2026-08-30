# SMEsPlus Enterprise Module Learning Priority Matrix

Document ID: STATE03-ENTERPRISE-MODULE-LEARNING-PRIORITY-MATRIX
Version: 0.1
Date: 2026-08-30
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Jira: ERPPLUS-133
Boss: Sole Final Approver
Control Level: /L99.99
Status: CONTROLLED BASELINE DRAFT / CATALOG RECONCILIATION REQUIRED

## 1. Boss Decision

Boss approved creation of the `SMEsPlus Enterprise Module Learning Priority Matrix` as the Master Register for prioritizing learning across the complete SMEsPlus SaaS ERP capability catalog.

The governing principle is:

- `MODULE CATALOG = 100% IN SCOPE` after each capability is confirmed in the approved SMEsPlus product baseline.
- `LEARNING ORDER = PRIORITIZED BY DEPENDENCY`.
- `MODULE EXCLUSION = NONE unless Boss explicitly removes it through governance`.
- Every confirmed SMEsPlus module/capability must operate under the shared SaaS foundation.
- Priority/Wave does not mean optionality or exclusion.

## 2. Critical Evidence Boundary

The existing Team A source inventory contains **1,504 technical source modules**. That number is a research inventory only and is **NOT an approved SMEsPlus product-module count**.

Source evidence:

- `TEAM_A/01_SOURCE_REGISTRY/MODULE_MASTER_REGISTER.md`
- `TEAM_A/01_SOURCE_REGISTRY/MODULE_MASTER_REGISTER_FULL.csv`
- `TEAM_A/A2_SYSTEM_KNOWLEDGE_MAP.md`

The current target capability rows below are therefore a controlled candidate catalog for reconciliation. They must not be called complete until matched against the approved product baseline / TOR / functional scope / current architecture evidence.

No completion percentage may be claimed until the denominator and weights are evidence-backed.

## 3. Parallel Architecture Tracks

The matrix is executed in parallel with, not instead of:

| Track | Scope | Current control |
|---|---|---|
| A | Thailand COA Closure | ERPPLUS-132 / COA-G01 → G08 |
| B | SaaS Platform Architecture | Tenant, IAM, Entitlement, Security, Audit, Event, API/Integration, Data Governance, Observability, Platform Controls |
| C | Enterprise Shared Domains | Party, Product, UOM, Tax, Currency, Company/Branch, Location, Dimension, Shared Reference Data |
| D | Business Module Learning | All confirmed SMEsPlus modules/capabilities organized by Wave 0–8 |

## 4. Universal SaaS Contract

Every confirmed SMEsPlus module/capability must be compatible with the following platform controls, whether consumed directly or indirectly:

1. Tenant boundary
2. Organization / Company / Branch context
3. IAM / permission controls
4. Subscription / entitlement controls
5. Security controls
6. Audit / evidence controls
7. Event and integration governance
8. Data governance / privacy / compliance
9. Multi-company behavior
10. SaaS lifecycle / configuration / release compatibility

Modules with financial impact must also comply with the approved Accounting/COA contract before final design freeze.

## 5. Wave Definitions

### Wave 0 — SaaS Platform Foundation

Learning first because every module depends on these shared platform controls.

Candidate capabilities:

1. Tenant / Organization / Company / Branch
2. IAM / User / Role / Permission
3. Subscription / Plan / Entitlement
4. Security Platform Controls
5. Audit / Evidence / Traceability
6. Immutable Event / Event Bus / Outbox Semantics
7. Workflow / Approval Engine
8. Notification Service
9. Document / Attachment Platform Service
10. API / Integration / Webhook Framework
11. Data Governance / Privacy / Compliance
12. Localization / Locale / Language / Timezone
13. Observability / Logging / Metrics / Tracing
14. Platform Configuration / Feature Controls
15. Usage Metering / Quota / Limit Controls
16. Background Job / Scheduler Service

### Wave 1 — Shared Business Master

1. Party / Customer / Supplier / Contact
2. Product / Service
3. Product Category / Classification
4. UOM
5. Pricing / Pricelist
6. Tax Master
7. Payment Terms
8. Fiscal Calendar / Period Reference
9. Location / Warehouse Master
10. Currency / Exchange Rate
11. Dimension / Analytic Structure
12. Shared Reference / Sequence / Numbering Data

### Wave 2 — Core Transaction Backbone

1. Sales
2. Purchase
3. Inventory / Warehouse
4. Accounting Core / COA

### Wave 3 — Financial Operations

1. Accounts Receivable (AR)
2. Accounts Payable (AP)
3. Cash Management
4. Bank Management
5. Payment
6. Reconciliation
7. Expense
8. Asset
9. Thailand Tax Accounting
10. Budget Control
11. Financial Reporting

### Wave 4 — Commercial & Customer

1. CRM
2. POS
3. eCommerce
4. Marketplace
5. Subscription Commerce
6. Recurring Billing
7. Promotion / Loyalty
8. Customer Service / Helpdesk

### Wave 5 — Operations

1. Manufacturing / MRP
2. BOM / Production Master
3. Maintenance
4. Quality
5. Procurement Planning / Replenishment
6. Logistics / Delivery
7. Fleet
8. Project / Timesheet / Service Delivery

### Wave 6 — People

1. HR Core / Employee
2. Organization / Position / Job
3. Recruitment
4. Attendance
5. Leave
6. Employee Claim
7. Payroll
8. Benefits
9. Performance
10. Employee Self-Service

### Wave 7 — Management / Control / Enterprise

1. FP&A / Planning
2. Consolidation
3. Management Accounting
4. BI / Dashboard
5. KPI / Scorecard
6. Document Management Business App
7. Knowledge Base
8. Approval Center / Approval Operations
9. Audit / Compliance Workspace
10. Enterprise Administration

### Wave 8 — Extension & Ecosystem

1. External Connector Framework
2. Banking Connector
3. Payment Gateway
4. Government Integration
5. Marketplace Connector
6. Logistics Connector
7. EDI / e-Invoice / e-Document Integration
8. Import / Export
9. Migration Factory
10. Public / Partner API

## 6. Priority Logic

Learning may run ahead where dependency analysis permits. Design freeze may not run ahead of unresolved upstream architecture gates.

Control rule:

`Learning Ahead = Allowed`

`Design Ahead of Dependency Gate = Controlled / HOLD where dependency is unresolved`

`Development Ahead of Approved Architecture = NOT AUTHORIZED`

Financial-impact examples:

- Sales, Purchase, Inventory, AR, AP, Payment, Expense, Asset, Payroll and MRP costing may be learned before COA freeze.
- Their final posting/account/tax design must not be frozen until the relevant Accounting/COA and Thailand tax gates are satisfied.

## 7. Cross-Module Semantic Reconciliation Rule

Module-specific discoveries must not create duplicate canonical models.

Required flow:

`MODULE-SPECIFIC FACT → SHARED SEMANTIC CANDIDATE → CROSS-MODULE RECONCILIATION → CANONICAL DOMAIN OWNER`

Examples:

- Sales + Purchase + Inventory + MRP → Canonical Product Domain
- Sales + CRM + AR + Purchase + AP → Canonical Party Domain
- Sales + Purchase + Inventory + Asset + Payroll → Accounting / Tax Contract where financial impact exists

## 8. Mandatory Row-Level Matrix Fields

The machine-readable companion register must contain:

- Wave
- Module / Capability
- Capability Type
- Target Scope Status
- Learning Priority
- Upstream Dependency
- Shared Domain Dependency
- Accounting Dependency
- SaaS Dependency
- Thailand Localization Dependency
- Learning Gate
- Design Freeze Gate
- Evidence Location
- Owner
- Reviewer
- Verification Status
- Gate Impact
- Notes / Unknowns

## 9. Catalog Completeness Gate

Before this register may be declared complete:

1. Reconcile candidate capabilities against approved project baseline / TOR / functional scope.
2. Reconcile against current STATE03 Module Architecture evidence.
3. Reconcile against DOMAIN learning evidence without turning source technical modules into target modules.
4. Register every confirmed product capability exactly once in the target catalog hierarchy.
5. Register shared/platform capabilities separately from business applications where architecture ownership differs.
6. Identify any duplicate, alias, composite or missing capability.
7. Obtain independent review.
8. Submit completeness result to Boss for final catalog approval/freeze.

Until then:

`Catalog Status = CATALOG RECONCILIATION REQUIRED`

`Catalog Completion % = TBD / BASELINE REQUIRED`

## 10. Immediate Learning Priority

Subject to catalog reconciliation, the first parallel learning set is:

- Wave 0 — SaaS Platform Foundation
- Wave 1 — Enterprise Shared Domains
- Wave 2 — Sales
- Wave 2 — Purchase
- Wave 2 — Inventory / Warehouse
- Wave 2 — Accounting Core / COA continues under ERPPLUS-132

This does not authorize final design freeze or development.

## 11. Evidence / Ownership Register

| Item | Owner | Evidence location | Timestamp | Reviewer | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Boss authorization to create Enterprise Module Learning Priority Matrix | Boss | Chat decision + ERPPLUS-133 + this GitHub artifact | 2026-08-30 | ChatGPT | RECORDED | Opens matrix/catalog reconciliation work only |
| Source technical-module inventory boundary | Team A Evidence | `MODULE_MASTER_REGISTER.md`, `MODULE_MASTER_REGISTER_FULL.csv`, `A2_SYSTEM_KNOWLEDGE_MAP.md` | 2026-08-28/29 | ChatGPT | VERIFIED AS RESEARCH INVENTORY | Prevents 1,504 source modules becoming target scope by inference |
| Candidate target capability catalog v0.1 | UNASSIGNED | This document + row-level CSV companion | 2026-08-30 | ChatGPT | DRAFT / RECONCILIATION REQUIRED | Blocks catalog completeness claim |
| Full catalog reconciliation | UNASSIGNED | TBD | TBD | ChatGPT | NOT STARTED | Blocks final target module catalog freeze |

## 12. Administrative Red Flags

- Assignee: `UNASSIGNED`
- Due Date: `TBD`
- STEP linkage: `TBD / BASELINE LINKAGE REQUIRED`
- Catalog denominator: `TBD / BASELINE REQUIRED`
- Wave/module completion percentages: `TBD / BASELINE REQUIRED`

## 13. Authority Boundaries

This authorization covers learning-priority matrix creation, catalog reconciliation and controlled learning sequencing only.

Development Authorization = **NOT GRANTED**.
Production Authorization = **NOT GRANTED**.
No confirmed module may be excluded without Boss approval.
No Wave may be interpreted as optional scope solely because it has a later priority.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
