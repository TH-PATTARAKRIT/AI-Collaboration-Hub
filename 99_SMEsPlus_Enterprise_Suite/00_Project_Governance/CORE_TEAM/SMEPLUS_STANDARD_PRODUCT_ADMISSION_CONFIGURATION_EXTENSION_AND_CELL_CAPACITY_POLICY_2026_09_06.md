# SMEsPlus Standard Product Admission, Configuration & Extension, and Cell Capacity Policy

Project: SMEsPlus ENTERPRISE SUITE
Effective Date: 2026-09-06
Authority: Boss = Sole Final Approver
Status: BOSS APPROVED / EFFECTIVE

## 1. Purpose

This policy strengthens the SMEsPlus Standard operating model by controlling Product Scope, Engineering Scope, and Infrastructure Cost together.

It formalizes three mandatory controls:

1. STANDARD PRODUCT ADMISSION RULE
2. STANDARD CONFIGURATION & EXTENSION BOUNDARY
3. STANDARD CELL CAPACITY & TELEMETRY POLICY

This policy complements the approved SMEsPlus Standard Product & Upward Mobility Policy and does not reset or invalidate prior verified evidence.

## 2. STANDARD PRODUCT ADMISSION RULE

A customer request does not automatically become Standard Core scope.

Every material request proposed for Standard Core must be evaluated against at least:

- broad reusable business value across multiple customers or target segments
- ERP semantic correctness
- architecture fit
- SaaS tenant/company isolation impact
- financial/accounting/control impact where applicable
- maintainability
- testability
- upgrade compatibility
- operational cost
- infrastructure cost per tenant
- security impact
- support burden
- product strategy alignment

Possible dispositions:

- ADMIT TO STANDARD CORE
- CONFIGURE, DO NOT CODE
- USE APPROVED EXTENSION POINT
- ENTERPRISE-SPECIFIC CANDIDATE
- FUTURE PRODUCT CANDIDATE
- REJECT / NOT STANDARD CORE SCOPE

Mandatory principle:

**Product decisions must be evidence-driven, not loudest-customer-driven.**

## 3. STANDARD CONFIGURATION & EXTENSION BOUNDARY

SMEsPlus Standard shall prefer controlled configuration before customer-specific Core customization.

Decision order:

Configuration -> Policy -> Workflow -> Entitlement -> Master Data -> Reporting -> Approved Extension Point -> Core Change

Examples of intended configuration surfaces may include:

- approval rules
- document numbering
- tax setup
- warehouse/location setup
- accounting policy
- role/permission
- reporting options
- workflow parameters

Approved extension boundaries may include, subject to architecture and security review:

- API
- webhook
- event
- custom report interface
- external workflow integration
- approved plugin/extension interface

Mandatory principles:

**Configuration should absorb variation before Code does.**

**Extension should absorb uniqueness before Core does.**

No extension may weaken tenant isolation, accounting integrity, auditability, upgradeability, or security controls.

## 4. STANDARD CELL CAPACITY & TELEMETRY POLICY

Standard deployment uses shared-resource multi-tenant cells and may scale horizontally across many servers/cells while preserving one SMEsPlus Core product and codebase.

Cell capacity shall not be defined only by a fixed tenant count.

Each Standard Cell must have a measurable Capacity Envelope that may include:

- active tenant count
- transaction throughput
- storage utilization
- database load / IOPS
- CPU and memory utilization
- queue/background job load
- report load
- integration load
- AI workload where applicable
- response-time / SLA indicators
- safety margin

When a cell approaches a controlled threshold, the default action is to stop new tenant placement and add/use another Standard Cell rather than overloading the existing Cell.

Mandatory principle:

**Capacity should scale by adding Cells before overloading a Cell.**

No architecture constant such as "1 Cell = N tenants" may be frozen without measured workload evidence.

## 5. PRODUCT TELEMETRY

SMEsPlus shall measure product usage and operational cost where practical so Product decisions can be based on evidence.

Telemetry may include:

- feature usage
- active users
- transaction frequency
- error rate
- support ticket frequency
- performance cost
- adoption by tenant
- infrastructure cost by workload class

Feature/Product Review dispositions may include:

- KEEP
- IMPROVE
- SIMPLIFY
- DEPRECATE

More capability is acceptable when it is useful, controlled, maintainable, testable, and actually applicable.

More capability without meaningful usage, business value, maintainability, or strategic purpose is waste.

## 6. STANDARD CUSTOMER REQUEST FLOW

Customer Request
-> Existing Configuration Check
-> Reusability / Business Value Check
-> ERP Semantic Review
-> Architecture / SaaS / Security Review
-> Financial / Control Impact Review where applicable
-> Maintainability / Testability / Upgrade Review
-> Cost / Capacity Review
-> Product Disposition
-> Controlled Prompt / Work Package if admitted

AGPO controls intake, evidence, challenge, prompt, and gate flow.
IEDA participates when ERP semantics/process/data/control/intelligence are affected.
PEESA participates when enterprise/SaaS/engineering/capability risk is material.
9 Veto independently challenges material risk.
ADGO executes only after applicable authorization.
Boss remains sole Final Approver.

## 7. Standard vs Enterprise Boundary

STANDARD
= Shared Resource / Multi-tenant Cells / Cost Optimized

ENTERPRISE
= Dedicated Resource / Dedicated Tenant Environment

STANDARD -> ENTERPRISE
= normal supported upgrade path

ENTERPRISE -> STANDARD
= not a normal commercial offering; controlled exception only with capacity, security, contract, technical review, and Boss approval.

Standard is shared-resource, not low-quality. Standard and Enterprise preserve the same minimum integrity principles for tenant isolation, security, accounting correctness, transaction integrity, auditability, backup, restore, reconciliation, and upgradeability.

## 8. Constitutional Operating Principles

- No customer request automatically becomes Core scope.
- No configuration-capable variation should force Core customization.
- No extension may bypass security or accounting integrity.
- No Cell may be intentionally overloaded when another Cell can be provisioned.
- No telemetry claim = no evidence-based product conclusion.
- No Evidence = No Verified Progress.
- Never Skip Gate.
- Boss remains sole Final Approver.

## 9. Final Product Philosophy

**Do not customize the Core for every customer. Design the Core so that most customers do not need customization.**

**More capability is acceptable when useful. More capability without actual need or usage is waste.**
