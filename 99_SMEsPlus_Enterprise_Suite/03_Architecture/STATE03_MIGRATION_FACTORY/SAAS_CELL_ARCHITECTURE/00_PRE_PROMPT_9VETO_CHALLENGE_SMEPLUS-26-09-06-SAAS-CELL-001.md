# [SMEPLUS-26-09-06-SAAS-CELL-001]
# PRE-PROMPT 9 VETO CHALLENGE — Two-Tier Cell Architecture, Standard Product Governance & Upward Mobility / L9999.9999

Project: SMEsPlus ENTERPRISE SUITE
Date: 2026-09-06
Boss: Sole Final Approver
Mode: DELTA-FIRST / NO RESET / NO REPEATED QUESTION WITHOUT MATERIAL DELTA

## 1. Purpose

Prepare the next controlled session for SMEsPlus SaaS architecture continuation without losing the accumulated conversation, Boss decisions, governance history, or already-approved product/architecture principles.

This is NOT a restart. Existing approved evidence remains valid unless a documented material delta contradicts it.

Mandatory rule: Challenge First -> Prompt Second -> Execution Third.

## 2. Prior Approved Context Carried Forward

### 2.1 Product identity
- SMEsPlus is a new clean-room Node.js SaaS ERP.
- Open-source and legacy ERP products are reference / learning / benchmark only.
- No source-code clone, schema clone, ORM clone, workflow clone, or product-core dependency on a reference ERP.
- One SMEsPlus product and one Core codebase.

### 2.2 SMEs Team structure
Boss-facing umbrella name: SMEs Team (SMT).
Internal permanent units remain separated:
- AGPO — Architecture, Governance & Prompt Office
- IEDA — Intelligent ERP Design Authority
- PEESA — Principal Enterprise ERP & SaaS Advisor
- 9 Veto Challenge Council — independent challenge/veto
- ADGO — authorized technical execution/delivery only after applicable authorization
Boss remains sole Final Approver.

### 2.3 ERP Strengthening Standard
Strictly enforced:
- One Business Concept = One Canonical Meaning
- Cross-domain business/data/reconciliation contracts
- Exception-first design
- Financial integrity backbone
- Explicit scope/ownership
- Reconciliation as first-class capability
- Trusted intelligence only from verified/reconciled facts

Constitutional rules include:
NO SEMANTIC DEFINITION = NO DESIGN FREEZE
NO CROSS-DOMAIN CONTRACT = NO INTEGRATION FREEZE
NO REVERSAL/CORRECTION PATH = NO TRANSACTION RELEASE
NO RECONCILIATION RULE = NO FINANCIAL FEATURE FREEZE
NO PROVABLE OWNERSHIP = DENY/HOLD
NO TESTABLE ACCEPTANCE = REQUIREMENT INCOMPLETE
NO EVIDENCE = NO VERIFIED PROGRESS
NO TRUSTED FACT = NO TRUSTED INTELLIGENCE

### 2.4 Mandatory major-domain artifacts
1. Domain Semantic Model
2. End-to-End Process Map
3. Business Rule & Exception Register
4. Cross-Domain Handoff Contract
5. Financial / Control Impact Matrix
6. Requirement-Test-Evidence Traceability Matrix

### 2.5 SaaS scope baseline
- PLATFORM / TENANT / COMPANY are explicit scopes.
- Tenant = Security / Customer Boundary.
- Company = Legal / Accounting / Business Boundary inside a Tenant.
- Unrelated independent companies are separate Tenants by default.
- Business relationship != shared Tenant.
- Common service provider != shared Tenant.
- Multi-tenant membership != multi-tenant execution context.
- Trusted Execution Context is mandatory.
- Cross-tenant deny-by-default.
- Ownership must be provable.
- AI retrieval/context/tooling must enforce tenant isolation before model exposure.

### 2.6 Two deployment tiers only
Boss-approved direction:

STANDARD
= Shared Resource
= Multi-tenant Cells
= Cost-optimized for Thai SMEs

ENTERPRISE
= Dedicated Resource
= Dedicated Tenant Environment
= SLA / isolation / performance optimized

No PRIVATE third tier as a separate commercial tier.

Deployment tier != company size.
Deployment tier != number of companies.
Deployment tier != holding structure.
Deployment tier = resource isolation + SLA + operational requirement.

### 2.7 One Core, many Cells
- Many Standard servers/cells are allowed, including potentially very large counts.
- Scale horizontally by adding Cells/Servers.
- Do not fork Core source code per customer or per Cell.
- Infrastructure scaling belongs in SaaS/Deployment layers, not customer-specific Core forks.
- Standard across the country must NOT depend on one national monolithic database/server.

Core principle:
ONE SMEPLUS PRODUCT
ONE CORE CODEBASE
MANY DEPLOYMENT CELLS

### 2.8 Standard vs Enterprise quality
Standard is shared-resource, not low-quality.
Standard and Enterprise must preserve the same minimum integrity principles for:
- tenant isolation
- security
- accounting correctness
- transaction integrity
- auditability
- backup / restore
- reconciliation
- upgradeability

### 2.9 Mobility policy
STANDARD -> ENTERPRISE
= normal supported upgrade path.

ENTERPRISE -> STANDARD
= not a normal commercial offering.

Architecture may remain technically reversible only under controlled exception with capacity/security/contract review and Boss approval.

Commercially one-way; technically reversible only by controlled exception.
Tenant identity must not change when moving deployment tier.
Tenant Identity != Server Identity != Database Identity != Cell Identity.

### 2.10 Standard product philosophy
Standard is NOT customer-by-customer customization.
Customer request != automatic Standard Core scope.

Boss principle:
More capability is acceptable when it is useful, controlled, maintainable, testable and applicable.
More capability without real usage/business value is waste.

Design objective:
Do not customize the Core for every customer. Design the Core so that most customers do not need customization.

### 2.11 Standard request decision order
Configuration -> Policy -> Workflow -> Entitlement -> Master Data -> Reporting -> Approved Extension Point -> Core Change

Configuration before customization.
Extension before Core change.

### 2.12 Product admission rule
Evaluate:
- broad reusable value
- ERP semantic correctness
- architecture fit
- tenant/security impact
- financial/control impact
- maintainability
- testability
- upgradeability
- support burden
- operational cost
- infrastructure cost per tenant
- strategic fit

Product decisions must be evidence-driven, not loudest-customer-driven.

### 2.13 Cell capacity and telemetry
Capacity is a measurable envelope, not a fixed tenant-count constant.
Review at least:
- active tenants
- throughput
- storage
- DB load / IOPS
- CPU / memory
- queue/background jobs
- reports
- integrations
- AI workload where applicable
- response indicators
- safety margin

When approaching limits:
STOP NEW PLACEMENT -> ADD/USE ANOTHER STANDARD CELL.

Telemetry should support product and capacity decisions through:
- feature usage
- active users
- transaction frequency
- error rate
- support tickets
- performance cost
- adoption by tenant
- workload/infrastructure cost

Product dispositions: KEEP / IMPROVE / SIMPLIFY / DEPRECATE.

### 2.14 Engineering capability direction
Adopt with controlled refinement:
- Domain-Driven Design / bounded contexts
- canonical data modeling
- business-document state machines
- strict TypeScript domain contracts
- runtime validation + DB integrity + authorization + invariants
- high-integrity transaction engineering
- idempotency / duplicate-effect prevention
- temporal integrity
- immutable finalized business facts with reversal/correction facts
- comprehensive audit trail
- tenant/company scope propagation through trusted execution context

Freeze invariants before mechanisms.
Examples such as AsyncLocalStorage, PostgreSQL RLS, schema-per-tenant, DB-per-tenant, specific locking strategy, or microservices are implementation mechanisms requiring evidence, not constitutional rules.

### 2.15 Database / infrastructure cost objective
Target market: Thai SMEs.
Architecture must minimize database/server/OS/infrastructure licensing and operations cost per Standard tenant while preserving required integrity.

Do not force Enterprise-grade dedicated infrastructure cost onto Standard SME customers.

Candidate technology/topology may include PostgreSQL/shared clusters/dedicated resources, but exact mechanism is not frozen by this session history.

## 3. 9 Veto Delta Challenge

### Veto 1 — Governance / Evidence
Question: Is there any approved decision above that lacks canonical evidence or has been superseded?
Finding: Current session carries explicit Boss approvals and recorded GitHub/Jira evidence from prior conversation. Do not reopen unless material contradiction appears.
Result: NO MATERIAL NEW QUESTION.

### Veto 2 — Thailand Business Reality
Question: Does the two-tier model fit Thai SME affordability while allowing stronger isolation for customers who require it?
Finding: Direction is materially aligned. Remaining work is capacity/cost evidence, not reopening the two-tier decision.
Result: CARRY FORWARD.

### Veto 3 — ERP / Business Process Integrity
Question: Does infrastructure tiering risk splitting ERP semantics?
Control required: Same Core semantics, contracts, accounting rules and migration identity across Standard and Enterprise.
Result: REQUIRE ARCHITECTURE CONTRACT, not a new Boss question.

### Veto 4 — Data / Identity / Migration
Question: Can Standard -> Enterprise migration preserve tenant identity, business identity and historical traceability?
Control required: Tenant identity independent from physical placement; migration plan must preserve referential, financial, audit and reconciliation integrity.
Result: MATERIAL DESIGN TASK.

### Veto 5 — SaaS / System Integrity
Question: Can Standard scale to many Cells without code fork and without a national single-point architecture?
Control required: placement/routing/cell identity/version compatibility/health and capacity contracts.
Result: MATERIAL DESIGN TASK.

### Veto 6 — Financial / Accounting / Tax
Question: Can deployment movement change accounting semantics, posting, period, tax or reconciliation behavior?
Required answer: NO. Tier/Cell movement must be infrastructure movement, not business-semantic transformation.
Result: FREEZE AS INVARIANT.

### Veto 7 — Security / Privacy / Resilience
Question: Does shared Standard weaken isolation or backup/restore boundaries?
Required answer: NO. Shared resources still require tenant isolation, encrypted/isolated backup domains, restore-boundary safety and noisy-neighbor controls.
Result: MATERIAL DESIGN TASK.

### Veto 8 — Clean-Room / Provenance
Question: Does the design depend on copying architecture/mechanisms from a reference ERP?
Required answer: NO. External systems remain reference/benchmark only.
Result: PASS DIRECTIONALLY / CONTINUE PROVENANCE CONTROL.

### Veto 9 — AI / Automation / Human Oversight
Question: Can AI workload create noisy-neighbor or cross-tenant leakage in Standard Cells?
Control required: tenant-safe retrieval, workload quota/isolation, async/background controls, traceability and human-governed product decisions.
Result: MATERIAL DESIGN TASK.

## 4. Special Team Triggers

Triggered for next session:
- SaaS Architecture / Cell topology
- Tenant placement and mobility
- Database topology and cost model
- Capacity engineering / noisy-neighbor control
- Backup / restore / DR separation
- Standard product configuration/extension boundary
- Migration Standard -> Enterprise
- Telemetry and product evidence

## 5. Readiness Decision

PRE-PROMPT CHALLENGE RESULT:
READY TO ISSUE CONTROLLED NEW SESSION PROMPT.

No need to re-ask Boss about already-approved principles above.
Next session must produce design/evidence for implementation mechanisms and trade-offs without silently changing approved business/product direction.

No Team C / production authorization is created by this challenge.
No Database mechanism is frozen by this challenge.
No Microservices mandate is created by this challenge.

Boss remains sole Final Approver.
