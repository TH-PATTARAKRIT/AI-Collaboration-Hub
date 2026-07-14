# Architecture Decision Register (ARC-WP-012)

Document ID: ARC-WP-012
Version: 0.2
Session: [SMEPLUS-26-07-10-001]
Control Level: /L99.99
Status: DRAFT
Approval Status: PREPARED FOR REVIEW / HOLD
Gate Status: HOLD
Correction Reference: L99 Review Finding P0-01 (Batch 001 remediation)

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | ARC-WP-012 |
| Deliverable | ARCHITECTURE_DECISION_REGISTER.md |
| Version | 0.2 |
| Architecture Owner | ADR Governance AI Owner |
| Supporting Owner | Enterprise Architecture AI Owner |
| Independent Reviewer | ChatGPT L99 |
| Approval Authority | Boss |
| Created | 2026-07-14 |
| Corrected | 2026-07-14 (P0-01 remediation) |
| Evidence Path | 99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_ARCHITECTURE_ACCELERATION/ARCHITECTURE_DECISION_REGISTER.md |
| Verification Status | NOT VERIFIED |

## 2. Purpose

Consolidate all candidate architecture decisions raised across ARC-WP-001..011 into a controlled register. Following L99 review finding P0-01, every ADR (ADR-ARC-001 through ADR-ARC-019) now uses one consistent structured format with all mandatory fields. No decision here is APPROVED BY BOSS; the drafting agent must not assign that status.

## 3. Scope

All State 03 architecture decisions in the acceleration batch.

## 4. Out of Scope

Final approval of any decision (Boss authority). Claude Code AI must not assign APPROVED BY BOSS.

## 5. Architecture Owner

ADR Governance AI Owner.

## 6. Supporting Owner

Enterprise Architecture AI Owner.

## 7. Independent Reviewer

ChatGPT L99.

## 8. Dependencies

All ARC-WP-001..011 documents; ARC-WP-013 (risks), ARC-WP-014 (evidence).

## 9. Assumptions

- A-001: Allowed statuses are PROPOSED, UNDER REVIEW, HOLD, SUPERSEDED, REJECTED, DECISION REQUIRED, APPROVED BY BOSS. Only Boss may assign APPROVED BY BOSS.
- A-002: Where a field value is not yet available it is recorded as `TBD WITH OWNER / DECISION REQUIRED`; no business approval is invented.

## 10. Current State

Version 0.1 recorded several ADRs in abbreviated form (P0-01 finding). Version 0.2 rewrites all 19 ADRs in one complete structure.

## 11. Target State

A single ADR register where every record carries all mandatory fields, an evidence reference, an owner and reviewer, a related-risk mapping and a gate impact, feeding independent review and Boss decisions.

## 12. Architecture Model (ADR Register)

Mandatory fields for every ADR: ADR ID · Title · Architecture Domain · Decision Required · Status · Context · Options · Recommended Option · Rationale · Positive Consequences · Negative Consequences / Trade-offs · Dependencies · Architecture Owner · Independent Reviewer · Target Decision Date · Evidence References · Related Risks · Gate Impact.

---

### ADR-ARC-001
- ADR ID: ADR-ARC-001
- Title: Mandatory Enterprise Control Layer
- Architecture Domain: Enterprise Control
- Decision Required: Adopt a mandatory Enterprise Control layer that governs (enforces policy/SoD around) approval and posting rather than letting modules self-approve or self-post?
- Status: PROPOSED
- Context: PR-03/06/07 require a control plane so that no source module approves or posts outside enterprise policy. Enterprise Control governs; it does not execute the engines.
- Options: (a) mandatory central control layer that enforces policy around Approval/Posting engines; (b) per-module embedded control; (c) no dedicated control layer.
- Recommended Option: (a)
- Rationale: Consistent SoD, auditability and restricted-action gating across modules; single point of policy enforcement.
- Positive Consequences: Uniform control; stronger audit; clear restricted-action gating.
- Negative Consequences / Trade-offs: Modules depend on the control layer; potential governance hotspot; requires careful boundary so control does not become an executor.
- Dependencies: ARC-WP-004, ARC-WP-005, ARC-WP-007.
- Architecture Owner: Enterprise Control Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: ENTERPRISE_CONTROL_LAYER.md; SAAS_ARCHITECTURE_PRINCIPLES.md (PR-03)
- Related Risks: RK-10 (production readiness); RK-06 (posting control)
- Gate Impact: Gate B (contributes; does not pass)

---

### ADR-ARC-002
- ADR ID: ADR-ARC-002
- Title: Immutable Event Store as System-of-Record for Business Events
- Architecture Domain: Data / Integration
- Decision Required: Use an append-only immutable event store as the system-of-record for business events (PR-08)?
- Status: PROPOSED
- Context: Auditability, replay and tamper-evidence require append-only events; storage technology is not yet locked.
- Options: (a) dedicated append-only event store; (b) audit table only; (c) no durable event store.
- Recommended Option: (a)
- Rationale: Tamper-evidence, replay for recovery, and audit reconstruction.
- Positive Consequences: Strong audit and recovery/replay; supports idempotent reprocessing.
- Negative Consequences / Trade-offs: Storage growth; requires retention/compaction policy; technology lock deferred (HOLD).
- Dependencies: ARC-WP-007, ARC-WP-010, ARC-WP-008.
- Architecture Owner: Data Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: LOGICAL_COMPONENT_ARCHITECTURE.md; INTEGRATION_EVENT_ARCHITECTURE.md
- Related Risks: RK-09 (technology-stack); RK-06 (idempotency/replay)
- Gate Impact: Gate B/C

---

### ADR-ARC-003
- ADR ID: ADR-ARC-003
- Title: Company as Legal and Accounting Boundary
- Architecture Domain: Tenancy
- Decision Required: Define Company (not Tenant or Branch) as the legal-entity and posting/accounting boundary?
- Status: PROPOSED
- Context: SME structures vary; posting and legal identity must attach to a defined level (ARC-WP-002).
- Options: (a) Company = legal/accounting boundary; (b) Tenant = boundary; (c) Branch = boundary.
- Recommended Option: (a)
- Rationale: Aligns with typical SME legal-entity/ledger structure; Branch is operational, Tenant is commercial.
- Positive Consequences: Clear ledger ownership per company; supports inter-company control.
- Negative Consequences / Trade-offs: Some SMEs may treat Branch as a quasi-legal unit; edge cases need mapping.
- Dependencies: ARC-WP-002.
- Architecture Owner: Multi-Tenant Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: TENANT_COMPANY_BRANCH_MODEL.md
- Related Risks: RK-03 (data ownership ambiguity)
- Gate Impact: Gate B

---

### ADR-ARC-004
- ADR ID: ADR-ARC-004
- Title: Explicit Approval-Gated Inter-Company Transactions
- Architecture Domain: Tenancy
- Decision Required: Require cross-company transactions to use an explicit, approval-gated inter-company document (no implicit cross-company posting)?
- Status: DECISION REQUIRED
- Context: Cross-company posting rules are not defined in functional specs; ambiguity is a data-ownership risk.
- Options: (a) explicit approval-gated inter-company document; (b) implicit cross-company posting; (c) prohibit cross-company transactions initially.
- Recommended Option: (a) — pending business confirmation
- Rationale: Controls and auditability for inter-company flows; prevents silent cross-boundary posting.
- Positive Consequences: Clear audit and SoD for inter-company; explicit control.
- Negative Consequences / Trade-offs: Additional document type and workflow; business process definition required.
- Dependencies: ARC-WP-002, ADR-ARC-003.
- Architecture Owner: Multi-Tenant Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: TENANT_COMPANY_BRANCH_MODEL.md
- Related Risks: RK-03 (data ownership ambiguity)
- Gate Impact: Gate B

---

### ADR-ARC-005
- ADR ID: ADR-ARC-005
- Title: Entitlement Evaluated at Gateway Before Business Logic
- Architecture Domain: SaaS Product
- Decision Required: Evaluate module/feature entitlement at the API Gateway before business logic, failing closed?
- Status: PROPOSED
- Context: Subscription-driven module activation (AP-006) requires deterministic, server-side entitlement checks.
- Options: (a) gateway-level pre-check, fail closed; (b) per-module checks; (c) client-side gating.
- Recommended Option: (a)
- Rationale: Central, consistent, fail-closed enforcement before any business effect.
- Positive Consequences: Consistent enforcement; reduced duplicated logic.
- Negative Consequences / Trade-offs: Requires low-latency entitlement resolution and cache invalidation on change.
- Dependencies: ARC-WP-003, ARC-WP-009.
- Architecture Owner: SaaS Product Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: SUBSCRIPTION_ENTITLEMENT_MODEL.md
- Related Risks: RK-12 (stale entitlement cache)
- Gate Impact: Gate B

---

### ADR-ARC-006
- ADR ID: ADR-ARC-006
- Title: Suspension/Expiry Preserves Data, Blocks Transactions
- Architecture Domain: SaaS Product
- Decision Required: On suspension/expiry, block new transactions but preserve tenant data (no deletion)?
- Status: PROPOSED
- Context: Lifecycle must protect customer data while enforcing commercial state.
- Options: (a) block transactions, preserve data; (b) delete/deactivate data on suspension; (c) read-only degrade only.
- Recommended Option: (a)
- Rationale: Data protection, recoverability on renewal, compliance.
- Positive Consequences: Safe reactivation; no data loss; clearer compliance posture.
- Negative Consequences / Trade-offs: Storage cost for suspended tenants; retention policy needed.
- Dependencies: ARC-WP-003, ARC-WP-002.
- Architecture Owner: SaaS Product Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: SUBSCRIPTION_ENTITLEMENT_MODEL.md
- Related Risks: RK-11 (privacy/retention)
- Gate Impact: Gate B

---

### ADR-ARC-007
- ADR ID: ADR-ARC-007
- Title: Posting Only From an Approved Source Document
- Architecture Domain: Enterprise Control
- Decision Required: Restrict the Posting Engine to post only from an approved source document?
- Status: PROPOSED
- Context: PR-07 posting boundary; financial correctness requires approval before posting.
- Options: (a) posting only from approved document; (b) modules post directly; (c) post then approve.
- Recommended Option: (a)
- Rationale: SoD, auditability, financial correctness.
- Positive Consequences: No unapproved postings; clear audit chain.
- Negative Consequences / Trade-offs: Adds a required approval step before posting; workflow orchestration needed.
- Dependencies: ARC-WP-004, ADR-ARC-009, ADR-ARC-017.
- Architecture Owner: Enterprise Control Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: ENTERPRISE_CONTROL_LAYER.md
- Related Risks: RK-06 (posting idempotency/correctness)
- Gate Impact: Gate B/C

---

### ADR-ARC-008
- ADR ID: ADR-ARC-008
- Title: Tenant Data Isolation = Controlled Hybrid (RLS Baseline)
- Architecture Domain: Data / Tenancy
- Decision Required: Adopt a hybrid isolation model (shared-schema + RLS baseline; dedicated database/schema for large or regulated tenants)?
- Status: PROPOSED / HOLD (must remain PROPOSED until Boss approval; Gate B automatic HOLD)
- Context: Expected many-small-tenant profile favors density; regulated/large tenants need stronger isolation (ARC-WP-008).
- Options: (a) database-per-tenant; (b) schema-per-tenant; (c) shared-schema + RLS; (d) hybrid (default c, escalate to a/b).
- Recommended Option: (d)
- Rationale: Balances density/cost for the SME long tail with an escalation path to physical isolation.
- Positive Consequences: Cost-efficient default; strong isolation where required; no re-architecture to escalate.
- Negative Consequences / Trade-offs: Two operational patterns; RLS defect risk requires rigorous automated testing.
- Dependencies: ARC-WP-002, ARC-WP-009, ARC-WP-011.
- Architecture Owner: Data Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: MULTI_TENANT_DATA_ISOLATION_OPTIONS.md
- Related Risks: RK-01 (cross-tenant leak); RK-11 (residency/compliance); RK-09 (stack)
- Gate Impact: Gate B (automatic HOLD until decided)

---

### ADR-ARC-009
- ADR ID: ADR-ARC-009
- Title: Non-Overridable Segregation-of-Duties Defaults for Financial Documents
- Architecture Domain: Enterprise Control
- Decision Required: Make SoD defaults for financial documents non-overridable (creator cannot be sole approver; approver cannot alter posted results)?
- Status: PROPOSED
- Context: Over-configurable SoD could permit self-approval (RK-02 adjacent).
- Options: (a) non-overridable financial SoD defaults; (b) fully configurable SoD; (c) no enforced SoD.
- Recommended Option: (a)
- Rationale: Prevents self-approval and post-hoc tampering; supports financial compliance.
- Positive Consequences: Strong control baseline; audit defensibility.
- Negative Consequences / Trade-offs: Less flexibility for very small tenants with few users (needs exception path).
- Dependencies: ARC-WP-004, ARC-WP-009.
- Architecture Owner: Enterprise Control Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: ENTERPRISE_CONTROL_LAYER.md
- Related Risks: RK-02 (privilege/SoD)
- Gate Impact: Gate B/C

---

### ADR-ARC-010
- ADR ID: ADR-ARC-010
- Title: Controlled Hybrid Module Integration
- Architecture Domain: Application
- Decision Required: Adopt a Controlled Hybrid Modular Architecture that distinguishes in-process module integration, shared-ORM transaction boundaries, controlled domain/service interfaces, external API/event boundaries, and prohibits direct cross-service database coupling — rather than forcing pure microservices or an uncontrolled monolith?
- Status: PROPOSED / HOLD
- Context: The prior ADR-ARC-010 (v0.1) required "APIs/events only, never shared tables" for all modules, which would force microservices and conflict with the SMEsPlus Odoo-first modular ERP direction (L99 finding P0-02).
- Options: (a) pure microservices (API/event only everywhere); (b) uncontrolled monolith (free shared-DB access); (c) controlled hybrid (in-process ERP modules may share ORM/transaction under controlled interfaces; external/cross-runtime must use API/events; no raw cross-module SQL; no direct cross-service DB coupling).
- Recommended Option: (c)
- Rationale: Matches Odoo-first modular ERP reality while preserving control, ownership and clean boundaries; avoids over-engineering internal modules and avoids uncontrolled coupling.
- Positive Consequences: Practical ERP runtime; transactional integrity for in-process modules; strict boundaries where they matter (control engines, external integration).
- Negative Consequences / Trade-offs: Requires disciplined documentation of shared transaction boundaries and controlled interfaces; "controlled" must be enforced or it degrades toward a monolith.
- Dependencies: ARC-WP-005, ARC-WP-007, ARC-WP-010, ADR-ARC-011.
- Architecture Owner: Solution Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: APPLICATION_MODULE_BOUNDARY.md; LOGICAL_COMPONENT_ARCHITECTURE.md; INTEGRATION_EVENT_ARCHITECTURE.md
- Related Risks: RK-07 (Accounting fan-in); RK-08 (clean-room)
- Gate Impact: Gate B

---

### ADR-ARC-011
- ADR ID: ADR-ARC-011
- Title: No Circular Synchronous Dependencies
- Architecture Domain: Application
- Decision Required: Prohibit circular synchronous dependencies between modules, resolving cross-module read/reporting needs via controlled read models, services or events?
- Status: PROPOSED
- Context: Sales↔Accounting / Purchase↔Accounting synchronous cycles create coupling and availability risk (RK-07); L99 finding P0-02 requires removing circular dependency depiction.
- Options: (a) prohibit sync cycles, use events/read models; (b) allow sync cycles; (c) allow with timeouts only.
- Recommended Option: (a)
- Rationale: Decouples modules; improves availability and testability; supports posting-through-control directional flow.
- Positive Consequences: No deadlock/availability cascades; clearer flow (Source → Control → Posting → Ledger → Event → Reporting).
- Negative Consequences / Trade-offs: Requires read models/eventing for cross-module queries; eventual consistency in some views.
- Dependencies: ARC-WP-005, ARC-WP-010, ADR-ARC-010.
- Architecture Owner: Solution Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: APPLICATION_MODULE_BOUNDARY.md; INTEGRATION_EVENT_ARCHITECTURE.md
- Related Risks: RK-07 (Accounting fan-in bottleneck)
- Gate Impact: Gate B/C

---

### ADR-ARC-012
- ADR ID: ADR-ARC-012
- Title: Single API Gateway as Sole External Ingress
- Architecture Domain: System Context
- Decision Required: Route all external traffic through a single API Gateway that performs authentication, TLS termination and tenant resolution?
- Status: PROPOSED
- Context: A single ingress reduces attack surface and centralizes tenant/entitlement resolution (ARC-WP-006).
- Options: (a) single API Gateway ingress; (b) per-module public endpoints; (c) mixed ingress.
- Recommended Option: (a)
- Rationale: Centralized security, tenant resolution and entitlement pre-check.
- Positive Consequences: Smaller attack surface; consistent auth; single throttling point.
- Negative Consequences / Trade-offs: Gateway is a capacity hotspot and must be highly available.
- Dependencies: ARC-WP-006, ARC-WP-009, ADR-ARC-005.
- Architecture Owner: Technical Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: SYSTEM_CONTEXT_ARCHITECTURE.md
- Related Risks: RK-02 (access), RK-07 (hotspot)
- Gate Impact: Gate B

---

### ADR-ARC-013
- ADR ID: ADR-ARC-013
- Title: External Identity Federation (SSO/IdP)
- Architecture Domain: IAM / System Context
- Decision Required: Support external identity federation (SSO/IdP) in addition to local identities?
- Status: DECISION REQUIRED
- Context: Some tenants may require SSO; scope and providers are unconfirmed (ARC-WP-009).
- Options: (a) local identities only initially; (b) local + optional federation; (c) federation-first.
- Recommended Option: (b) — pending business confirmation
- Rationale: Meets enterprise-tenant SSO needs without blocking the SME baseline.
- Positive Consequences: Broader tenant fit; enterprise readiness.
- Negative Consequences / Trade-offs: Added complexity, provider integration and testing; deferred until confirmed.
- Dependencies: ARC-WP-009, ARC-WP-006.
- Architecture Owner: Identity Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: IDENTITY_ACCESS_ARCHITECTURE.md; SYSTEM_CONTEXT_ARCHITECTURE.md
- Related Risks: RK-11 (compliance), RK-02 (IAM)
- Gate Impact: Gate B

---

### ADR-ARC-014
- ADR ID: ADR-ARC-014
- Title: Stateless Application Services + Asynchronous Backbone
- Architecture Domain: Logical / Infrastructure
- Decision Required: Design application services as stateless and horizontally scalable, with durable state in data/queue/event layers?
- Status: PROPOSED
- Context: AP-009 cloud-native; async backbone absorbs bursts (ARC-WP-007).
- Options: (a) stateless services + async backbone; (b) stateful services; (c) synchronous-only processing.
- Recommended Option: (a)
- Rationale: Horizontal scale, resilience, burst absorption.
- Positive Consequences: Simple scaling and recovery-by-restart; burst tolerance.
- Negative Consequences / Trade-offs: Requires external session/state and idempotent async handling; technology not yet locked (HOLD).
- Dependencies: ARC-WP-007, ADR-ARC-017.
- Architecture Owner: Technical Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: LOGICAL_COMPONENT_ARCHITECTURE.md
- Related Risks: RK-09 (stack), RK-05 (recovery)
- Gate Impact: Gate B/C

---

### ADR-ARC-015
- ADR ID: ADR-ARC-015
- Title: RBAC + ABAC, Deny-by-Default, Tenant-Scoped
- Architecture Domain: IAM
- Decision Required: Adopt RBAC baseline augmented by ABAC (tenant/company/branch/entitlement), deny-by-default, with no role granting cross-tenant access?
- Status: PROPOSED
- Context: AP-003 security-by-design; tenant isolation must hold at the access layer (ARC-WP-009).
- Options: (a) RBAC+ABAC deny-by-default; (b) RBAC only; (c) ACL-based.
- Recommended Option: (a)
- Rationale: Combines role manageability with fine-grained, tenant-scoped decisions.
- Positive Consequences: Strong isolation; least privilege; auditable decisions.
- Negative Consequences / Trade-offs: Higher check frequency needs caching with correct invalidation.
- Dependencies: ARC-WP-002, ARC-WP-003, ARC-WP-004.
- Architecture Owner: Identity Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: IDENTITY_ACCESS_ARCHITECTURE.md
- Related Risks: RK-02 (privilege escalation)
- Gate Impact: Gate B

---

### ADR-ARC-016
- ADR ID: ADR-ARC-016
- Title: Clean-Room Engineering Enforcement
- Architecture Domain: Governance / Security
- Decision Required: Enforce that no proprietary source-system implementation (including iTEST02) is copied into SMEsPlus code, schema or content; source learning is conceptual only?
- Status: PROPOSED
- Context: Odoo-first UX reference and source-learning material create IP/clean-room risk (PR-16, `09_Security_Clean_Room`).
- Options: (a) enforced clean-room policy with controls; (b) advisory-only; (c) no constraint.
- Recommended Option: (a)
- Rationale: Legal/IP protection; avoids source contamination.
- Positive Consequences: Defensible IP position; controlled reuse.
- Negative Consequences / Trade-offs: Requires enforcement mechanism (currently policy-level; automated check is an open gap GAP-SE-02).
- Dependencies: ARC-WP-001, ARC-WP-005.
- Architecture Owner: Architecture Governance AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: SAAS_ARCHITECTURE_PRINCIPLES.md; 09_Security_Clean_Room/09_Security_Clean_Room/iTEST02_clean_room_policy.md
- Related Risks: RK-08 (clean-room compliance)
- Gate Impact: Gate B/D

---

### ADR-ARC-017
- ADR ID: ADR-ARC-017
- Title: At-Least-Once Delivery with Idempotent Consumers
- Architecture Domain: Integration
- Decision Required: Adopt at-least-once event delivery with mandatory idempotent consumers (idempotency keys), retry with backoff and dead-letter handling?
- Status: PROPOSED
- Context: Reliable eventing without duplicate side effects, critical for posting (RK-06).
- Options: (a) at-least-once + idempotent consumers; (b) at-most-once; (c) exactly-once (often impractical).
- Recommended Option: (a)
- Rationale: Practical reliability; duplicates neutralized by idempotency.
- Positive Consequences: No message loss; safe retries and replay.
- Negative Consequences / Trade-offs: Every consumer must implement idempotency; ordering handled per-aggregate.
- Dependencies: ARC-WP-010, ADR-ARC-007.
- Architecture Owner: Integration and Event Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: INTEGRATION_EVENT_ARCHITECTURE.md
- Related Risks: RK-06 (duplicate posting on retry)
- Gate Impact: Gate B/C

---

### ADR-ARC-018
- ADR ID: ADR-ARC-018
- Title: Make Automation Integrates Only via Gateway and Signed Webhooks
- Architecture Domain: Integration
- Decision Required: Restrict Make automation to interact only through the API Gateway and signed, verified webhooks — never the data store or internal event bus directly?
- Status: PROPOSED
- Context: External automation must not bypass control or isolation (ARC-WP-010).
- Options: (a) gateway + signed webhooks only; (b) direct DB/bus access; (c) unsigned webhooks.
- Recommended Option: (a)
- Rationale: Preserves control, tenant scope and auditability for external automation.
- Positive Consequences: Controlled, revocable, tenant-scoped external automation.
- Negative Consequences / Trade-offs: Requires webhook signing/verification and scoped credentials management.
- Dependencies: ARC-WP-010, ARC-WP-006.
- Architecture Owner: Integration and Event Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: INTEGRATION_EVENT_ARCHITECTURE.md
- Related Risks: RK-02 (access); No additional mapped risk beyond integration security
- Gate Impact: Gate B

---

### ADR-ARC-019
- ADR ID: ADR-ARC-019
- Title: Measurable NFR Baseline (Classified by Evidence Basis)
- Architecture Domain: Non-Functional Requirements
- Decision Required: Adopt the ARC-WP-011 NFR set as measurable Gate B/C/D targets, each classified by evidence basis (APPROVED BASELINE / PROPOSED TARGET / ASSUMPTION / TBD WITH OWNER / REQUIRED HARD CONTROL) — no numeric target represented as an approved baseline without Boss evidence?
- Status: PROPOSED
- Context: L99 finding P1-01: v0.1 stated numeric targets without evidence basis.
- Options: (a) adopt classified NFR set; (b) adopt numeric targets as baselines (rejected — no evidence); (c) defer all NFRs.
- Recommended Option: (a)
- Rationale: Provides testable targets while honestly separating hard controls from unvalidated hypotheses.
- Positive Consequences: Clear validation obligations; no false "approved" baselines.
- Negative Consequences / Trade-offs: Several values remain TBD WITH OWNER pending business/infra input.
- Dependencies: ARC-WP-011, ARC-WP-007, ARC-WP-008, ARC-WP-009, ARC-WP-010.
- Architecture Owner: NFR Architecture AI Owner
- Independent Reviewer: ChatGPT L99
- Target Decision Date: TBD WITH OWNER / DECISION REQUIRED (Boss)
- Evidence References: NON_FUNCTIONAL_ARCHITECTURE_REQUIREMENTS.md
- Related Risks: RK-04 (security), RK-05 (recovery), RK-11 (privacy)
- Gate Impact: Gate B/D

---

### Summary Table

| ADR ID | Domain | Status | Owner | Reviewer | Related Risks | Target Decision Date | Evidence | Gate Impact |
|---|---|---|---|---|---|---|---|---|
| ADR-ARC-001 | Enterprise Control | PROPOSED | Enterprise Control AI Owner | ChatGPT L99 | RK-10,RK-06 | TBD WITH OWNER | ENTERPRISE_CONTROL_LAYER.md | Gate B |
| ADR-ARC-002 | Data/Integration | PROPOSED | Data Architecture AI Owner | ChatGPT L99 | RK-09,RK-06 | TBD WITH OWNER | LOGICAL_COMPONENT_ARCHITECTURE.md | Gate B/C |
| ADR-ARC-003 | Tenancy | PROPOSED | Multi-Tenant AI Owner | ChatGPT L99 | RK-03 | TBD WITH OWNER | TENANT_COMPANY_BRANCH_MODEL.md | Gate B |
| ADR-ARC-004 | Tenancy | DECISION REQUIRED | Multi-Tenant AI Owner | ChatGPT L99 | RK-03 | TBD WITH OWNER | TENANT_COMPANY_BRANCH_MODEL.md | Gate B |
| ADR-ARC-005 | SaaS Product | PROPOSED | SaaS Product AI Owner | ChatGPT L99 | RK-12 | TBD WITH OWNER | SUBSCRIPTION_ENTITLEMENT_MODEL.md | Gate B |
| ADR-ARC-006 | SaaS Product | PROPOSED | SaaS Product AI Owner | ChatGPT L99 | RK-11 | TBD WITH OWNER | SUBSCRIPTION_ENTITLEMENT_MODEL.md | Gate B |
| ADR-ARC-007 | Enterprise Control | PROPOSED | Enterprise Control AI Owner | ChatGPT L99 | RK-06 | TBD WITH OWNER | ENTERPRISE_CONTROL_LAYER.md | Gate B/C |
| ADR-ARC-008 | Data/Tenancy | PROPOSED / HOLD | Data Architecture AI Owner | ChatGPT L99 | RK-01,RK-11,RK-09 | TBD WITH OWNER | MULTI_TENANT_DATA_ISOLATION_OPTIONS.md | Gate B (HOLD) |
| ADR-ARC-009 | Enterprise Control | PROPOSED | Enterprise Control AI Owner | ChatGPT L99 | RK-02 | TBD WITH OWNER | ENTERPRISE_CONTROL_LAYER.md | Gate B/C |
| ADR-ARC-010 | Application | PROPOSED / HOLD | Solution Architecture AI Owner | ChatGPT L99 | RK-07,RK-08 | TBD WITH OWNER | APPLICATION_MODULE_BOUNDARY.md | Gate B |
| ADR-ARC-011 | Application | PROPOSED | Solution Architecture AI Owner | ChatGPT L99 | RK-07 | TBD WITH OWNER | APPLICATION_MODULE_BOUNDARY.md | Gate B/C |
| ADR-ARC-012 | System Context | PROPOSED | Technical Architecture AI Owner | ChatGPT L99 | RK-02,RK-07 | TBD WITH OWNER | SYSTEM_CONTEXT_ARCHITECTURE.md | Gate B |
| ADR-ARC-013 | IAM | DECISION REQUIRED | Identity Architecture AI Owner | ChatGPT L99 | RK-11,RK-02 | TBD WITH OWNER | IDENTITY_ACCESS_ARCHITECTURE.md | Gate B |
| ADR-ARC-014 | Logical/Infra | PROPOSED | Technical Architecture AI Owner | ChatGPT L99 | RK-09,RK-05 | TBD WITH OWNER | LOGICAL_COMPONENT_ARCHITECTURE.md | Gate B/C |
| ADR-ARC-015 | IAM | PROPOSED | Identity Architecture AI Owner | ChatGPT L99 | RK-02 | TBD WITH OWNER | IDENTITY_ACCESS_ARCHITECTURE.md | Gate B |
| ADR-ARC-016 | Governance/Security | PROPOSED | Architecture Governance AI Owner | ChatGPT L99 | RK-08 | TBD WITH OWNER | SAAS_ARCHITECTURE_PRINCIPLES.md | Gate B/D |
| ADR-ARC-017 | Integration | PROPOSED | Integration AI Owner | ChatGPT L99 | RK-06 | TBD WITH OWNER | INTEGRATION_EVENT_ARCHITECTURE.md | Gate B/C |
| ADR-ARC-018 | Integration | PROPOSED | Integration AI Owner | ChatGPT L99 | RK-02 | TBD WITH OWNER | INTEGRATION_EVENT_ARCHITECTURE.md | Gate B |
| ADR-ARC-019 | NFR | PROPOSED | NFR Architecture AI Owner | ChatGPT L99 | RK-04,RK-05,RK-11 | TBD WITH OWNER | NON_FUNCTIONAL_ARCHITECTURE_REQUIREMENTS.md | Gate B/D |

## 13. Architecture Decisions

This document IS the decision register; see Section 12.

## 14. Security Considerations

ADR-ARC-008/009/015/016/017/018 carry security weight; their status gates Gate B/D security posture.

## 15. Privacy and Compliance Considerations

ADR-ARC-006/008/013/015 depend on the confirmed compliance regime (DECISION REQUIRED).

## 16. Tenant-Isolation Considerations

ADR-ARC-008 is the isolation decision and remains PROPOSED / HOLD (Gate B automatic HOLD).

## 17. Recovery and Continuity Considerations

ADR-ARC-002/014/017 affect recovery/replay behavior.

## 18. Observability Considerations

Every ADR is traceable to an evidence document and a related risk, enabling review observability.

## 19. Capacity and Cost Considerations

ADR-ARC-008/010/014 shape the capacity/cost profile.

## 20. Risks and Gaps

- ADR-ARC-004 and ADR-ARC-013 are DECISION REQUIRED and block related Gate B items.
- ADR-ARC-008 and ADR-ARC-010 are PROPOSED / HOLD.
- No decision may be marked APPROVED BY BOSS by the AI (control enforced).

## 21. Measurable Acceptance Criteria

| AC ID | Criterion | Verification Method | Required Evidence |
|---|---|---|---|
| AC-001 | All 19 ADRs use the same complete 18-field structure | Review + validation script | Section 12 |
| AC-002 | No ADR marked APPROVED BY BOSS | Review + validation script | Section 12 |
| AC-003 | Every ADR has ≥1 evidence reference, an owner and a ChatGPT L99 reviewer | Review | Section 12 |
| AC-004 | Every ADR states Gate Impact and Related Risks (or "No current mapped risk") | Review | Section 12 |
| AC-005 | ADR-ARC-004/013 DECISION REQUIRED; ADR-ARC-008 PROPOSED/HOLD | Review | Section 12 |

## 22. Evidence Requirements

| Evidence ID | Type | GitHub Location | Owner | Reviewer | Verification Status |
|---|---|---|---|---|---|
| EV-ARC-012 | ADR register (v0.2) | This file path | ADR Governance AI Owner | ChatGPT L99 | NOT VERIFIED |

## 23. Open Decisions

- All ADRs are open pending independent review and Boss decision; ADR-ARC-004 and ADR-ARC-013 are DECISION REQUIRED; ADR-ARC-008 and ADR-ARC-010 are PROPOSED / HOLD.

## 24. Gate Impact

- Gate B input (critical ADR records). Contributes; does not pass.
- Recommendation: DECISION REQUIRED.

## 25. Change History

| Version | Date | Change | Author | Reviewer |
|---|---|---|---|---|
| 0.1 | 2026-07-14 | Initial ADR register | ADR Governance AI Owner (Claude Code drafting agent) | Pending (ChatGPT L99) |
| 0.2 | 2026-07-14 | P0-01 remediation: all 19 ADRs rewritten to full 18-field structure; ADR-ARC-010 replaced with Controlled Hybrid Module Integration | ADR Governance AI Owner (Claude Code Expert correction agent) | Pending (ChatGPT L99) |

## 26. Approval Status

PREPARED FOR REVIEW / HOLD. No ADR is approved. Boss decision mandatory.
