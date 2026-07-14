# SaaS Architecture Principles (ARC-WP-001)

Document ID: ARC-WP-001
Version: 0.1
Session: [SMEPLUS-26-07-10-001]
Control Level: /L99.99
Status: DRAFT
Approval Status: PREPARED FOR INDEPENDENT REVIEW / HOLD
Gate Status: HOLD

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | ARC-WP-001 |
| Deliverable | SAAS_ARCHITECTURE_PRINCIPLES.md |
| Version | 0.1 |
| Architecture Owner | Enterprise Architecture AI Owner |
| Supporting Owner | PMO Evidence AI |
| Independent Reviewer | ChatGPT L99 |
| Approval Authority | Boss |
| Created | 2026-07-14 |
| Evidence Path | 99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_ARCHITECTURE_ACCELERATION/SAAS_ARCHITECTURE_PRINCIPLES.md |
| Verification Status | NOT VERIFIED |

## 2. Purpose

Define the controlling SaaS architecture principles for the SMEsPlus Enterprise Suite. These principles are top-level architecture constraints that every domain document, ADR, module design and build decision in State 03 and later states must comply with. They extend and refine the earlier `01_SaaS_Foundation/ARCHITECTURE_PRINCIPLES.md` baseline for the Enterprise Suite scope.

## 3. Scope

- All State 03 architecture deliverables (ARC-WP-001 through ARC-WP-014).
- All modules in the SMEsPlus Enterprise Suite (Tenant Management, Organization Management, User and Role Management, Authorization, Approval Engine, Workflow Engine, Sales, Purchase, Inventory, Accounting, Customer CRM, Notification, Dashboard, Reporting, API Gateway).
- SaaS control planes: provisioning, entitlement, tenancy, security and observability.

## 4. Out of Scope

- Final technology-stack lock (remains HOLD, requires Boss decision).
- Implementation-level coding standards (owned by build state).
- Commercial pricing tables and contract terms.
- Any approval of a gate.

## 5. Architecture Owner

Enterprise Architecture AI Owner.

## 6. Supporting Owner

PMO Evidence AI.

## 7. Independent Reviewer

ChatGPT L99 (independent review) with Boss as final approval authority.

## 8. Dependencies

- `01_SaaS_Foundation/ARCHITECTURE_PRINCIPLES.md` (baseline principles AP-001..AP-012).
- STATE03_ARCHITECTURE_SCOPE_V2.md (domain authority).
- ARCHITECTURE_GATE_MODEL.md (gate conditions).
- ARC-WP-002 Tenant model, ARC-WP-004 Enterprise Control Layer, ARC-WP-008 Data Isolation, ARC-WP-009 IAM (principles are refined by these).

## 9. Assumptions

- A-001: SMEsPlus is delivered as a multi-tenant SaaS platform, not per-customer forks.
- A-002: An "Odoo-first" UI/UX reference informs the user experience, but source code is not copied (clean-room constraint applies).
- A-003: Enterprise Control, Approval Engine and Posting Engine are first-class platform capabilities, not per-module add-ons.
- A-004: Event history is treated as immutable business evidence.

## 10. Current State

Baseline principles exist in the SaaS Foundation (AP-001..AP-012) but do not yet cover Enterprise Control, posting-engine boundaries, immutable-event guarantees, evidence-by-default or the clean-room engineering constraint at the Enterprise Suite level. This document consolidates and extends them.

## 11. Target State

A single, authoritative principle set governing the Enterprise Suite, each principle stating an intent, a rule set and a measurable success criterion, and each traceable into ADRs (ARC-WP-012) and NFRs (ARC-WP-011).

## 12. Architecture Model

### PR-01 SaaS-First
Every capability is designed multi-tenant and subscription-driven before any single-tenant consideration. Success: a feature can be enabled for selected tenants without a new deployment.

### PR-02 Odoo-First UI/UX (Reference, Not Copy)
UI/UX patterns follow a familiar Odoo-style operational model for SME users. Success: navigation and record patterns match the reference model while all code is independently authored under the clean-room constraint (see PR-16).

### PR-03 SMEsPlus Enterprise Control
A dedicated Enterprise Control layer governs approvals, posting, segregation of duties and policy enforcement across modules. Success: no source module can post or approve outside the control layer's policy.

### PR-04 Modular Architecture
Modules are loosely coupled, independently activatable, and declare explicit dependencies. Success: a tenant runs only the modules it is entitled to.

### PR-05 Source-Module Execution
Business documents originate in an owning "source module" that is accountable for their lifecycle; downstream modules consume via defined interfaces only. Success: every business record has exactly one source-module owner.

### PR-06 Approval-Engine Boundary
Approval decisions are executed only by the Approval Engine using configurable rules; modules request approval, they do not self-approve. Success: no module contains embedded final-approval logic.

### PR-07 Posting-Engine Boundary
Financial and inventory posting is performed only by the Posting Engine from an approved source document. Success: no ledger or stock movement exists without a posting-engine transaction.

### PR-08 Immutable Event
Business events (creation, status change, posting, approval) are append-only and never mutated or deleted. Success: event history is reconstructable and tamper-evident.

### PR-09 Tenant Isolation
Tenant is the primary data boundary; every record carries tenant context and no query crosses tenants. Success: a cross-tenant read/write is structurally impossible (see ARC-WP-008).

### PR-10 Security-by-Design
Authentication, authorization, encryption in transit and at rest, and least privilege are designed in, not added later. Success: every endpoint passes a security review before promotion.

### PR-11 Evidence-by-Default
Every deliverable and critical action produces committed, traceable evidence (path, owner, timestamp, SHA, reviewer, status). Success: no progress is claimed without GitHub evidence ("No Evidence = No Progress").

### PR-12 API and Integration Control
Integration occurs only through versioned, contract-first APIs and controlled events; direct database coupling between modules is prohibited. Success: every integration has an API/event contract reference.

### PR-13 Observability and Auditability
Structured logging, metrics, tracing, health checks and immutable audit trails are mandatory for every service. Success: any incident is analyzable from system-produced data.

### PR-14 Backup and Recovery
Every stateful component has a defined backup, restore and recovery approach with measurable RPO/RTO (see ARC-WP-011). Success: a documented restore test can be executed.

### PR-15 Cost and Capacity
Capacity and cost are designed and monitored per tenant and per service. Success: capacity and cost targets are defined and observable.

### PR-16 Clean-Room Engineering Constraint
Learning material derived from any proprietary source system (including iTEST02) is used only for understanding; it is never converted directly into SMEsPlus code, schema or content. Success: no artifact traces to copied proprietary implementation (see `09_Security_Clean_Room`).

## 13. Architecture Decisions

- Refer to ARC-WP-012 for ADRs. Candidate ADRs raised by this document: ADR-ARC-001 (Enterprise Control mandatory), ADR-ARC-002 (immutable-event store), ADR-ARC-008 (tenant isolation model), ADR-ARC-016 (clean-room enforcement). Status of all: PROPOSED.

## 14. Security Considerations

Principles PR-09, PR-10, PR-11, PR-13 and PR-16 are security-load-bearing. Any deviation requires a recorded ADR and a risk entry (ARC-WP-013).

## 15. Privacy and Compliance Considerations

Evidence-by-default and immutable-event principles must not store restricted personal data in event payloads beyond lawful need; privacy detail is elaborated in ARC-WP-009 and ARC-WP-011. PDPA (Thailand) applicability is an open decision (DECISION REQUIRED).

## 16. Tenant-Isolation Considerations

PR-09 is the controlling principle; the concrete isolation option is selected in ARC-WP-008 and remains PROPOSED until approved.

## 17. Recovery and Continuity Considerations

PR-14 requires every stateful principle to map to a recovery capability; measurable RPO/RTO defined in ARC-WP-011.

## 18. Observability Considerations

PR-13 mandates observability for every service; concrete signals and thresholds are defined in ARC-WP-011 and ARC-WP-010.

## 19. Capacity and Cost Considerations

PR-15 requires per-tenant capacity and cost visibility; targets in ARC-WP-011.

## 20. Risks and Gaps

- R-001: Odoo-first reference risks clean-room contamination if not controlled (see ARC-WP-013).
- R-002: Immutable-event guarantee depends on an unselected data store (linked to ARC-WP-008).
- G-001: PDPA/compliance scope not yet defined.

## 21. Measurable Acceptance Criteria

| AC ID | Criterion | Verification Method | Required Evidence |
|---|---|---|---|
| AC-001 | All 16 principles present with intent, rules and success criteria | Document review | This file |
| AC-002 | Every principle traces to at least one ADR, NFR or downstream WP | Traceability check | ARC-WP-011/012 references |
| AC-003 | Clean-room constraint (PR-16) references clean-room policy | Link check | `09_Security_Clean_Room` |
| AC-004 | No principle uses vague criteria without a measurable or TBD-with-Owner marker | Review | This file |

## 22. Evidence Requirements

| Evidence ID | Type | GitHub Location | Owner | Reviewer | Verification Status |
|---|---|---|---|---|---|
| EV-ARC-001 | Principles document | This file path | Enterprise Architecture AI Owner | ChatGPT L99 | NOT VERIFIED |

## 23. Open Decisions

- OD-001: Confirm PDPA/compliance regime in scope. DECISION REQUIRED (Boss).
- OD-002: Confirm immutable-event storage technology. DECISION REQUIRED (depends on ARC-WP-008).

## 24. Gate Impact

- Gate A (Scope Baseline): principles are a required Gate A input — contributes, does not pass.
- Gate B (Architecture Baseline): principles constrain all Gate B artifacts.
- Recommendation: READY FOR INDEPENDENT REVIEW.

## 25. Change History

| Version | Date | Change | Author | Reviewer |
|---|---|---|---|---|
| 0.1 | 2026-07-14 | Initial draft prepared for independent review | Enterprise Architecture AI Owner (Claude Code drafting agent) | Pending (ChatGPT L99) |

## 26. Approval Status

PREPARED FOR INDEPENDENT REVIEW / HOLD. AI drafting does not equal approval. Independent ChatGPT L99 review and Boss decision remain mandatory.
