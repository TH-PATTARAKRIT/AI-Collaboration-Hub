# Architecture Decision Register (ARC-WP-012)

Document ID: ARC-WP-012
Version: 0.1
Session: [SMEPLUS-26-07-10-001]
Control Level: /L99.99
Status: DRAFT
Approval Status: PREPARED FOR INDEPENDENT REVIEW / HOLD
Gate Status: HOLD

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | ARC-WP-012 |
| Deliverable | ARCHITECTURE_DECISION_REGISTER.md |
| Version | 0.1 |
| Architecture Owner | ADR Governance AI Owner |
| Supporting Owner | Enterprise Architecture AI Owner |
| Independent Reviewer | ChatGPT L99 |
| Approval Authority | Boss |
| Created | 2026-07-14 |
| Evidence Path | 99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_ARCHITECTURE_ACCELERATION/ARCHITECTURE_DECISION_REGISTER.md |
| Verification Status | NOT VERIFIED |

## 2. Purpose

Consolidate the candidate architecture decisions raised across ARC-WP-001..011 into a controlled register. No decision here is APPROVED BY BOSS; all are PROPOSED or DECISION REQUIRED.

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

- A-001: Allowed statuses are PROPOSED, UNDER REVIEW, HOLD, SUPERSEDED, REJECTED, APPROVED BY BOSS. Only Boss may assign APPROVED BY BOSS.

## 10. Current State

Decisions were embedded in individual documents; no consolidated register existed.

## 11. Target State

A single ADR register with full fields per record, feeding independent review and Boss decisions.

## 12. Architecture Model (ADR Register)

Each record: ID · title · domain · decision required · status · context · options · recommendation · rationale · consequences · dependencies · owner · reviewer · target decision date · evidence reference.

### ADR-ARC-001 — Mandatory Enterprise Control Layer
- Domain: Enterprise Control. Status: PROPOSED.
- Decision required: Adopt a mandatory control layer for approval/posting/SoD?
- Context: Prevent modules self-approving/posting (PR-03/06/07).
- Options: (a) central control layer; (b) per-module control.
- Recommendation: (a). Rationale: consistency, SoD, auditability.
- Consequences: modules depend on control layer; potential hotspot.
- Dependencies: ARC-WP-004. Owner: Enterprise Control AI Owner. Reviewer: ChatGPT L99. Target: TBD with Boss. Evidence: ENTERPRISE_CONTROL_LAYER.md.

### ADR-ARC-002 — Immutable Event Store
- Domain: Data/Integration. Status: PROPOSED.
- Decision: Use an append-only immutable event store as system-of-record for business events (PR-08).
- Options: (a) dedicated event store; (b) audit table only.
- Recommendation: (a). Rationale: tamper-evidence, replay, audit.
- Consequences: storage growth, retention policy needed. Dependencies: ARC-WP-007/010/008. Owner: Data Architecture AI Owner. Reviewer: ChatGPT L99. Target: TBD. Evidence: LOGICAL_COMPONENT_ARCHITECTURE.md, INTEGRATION_EVENT_ARCHITECTURE.md.

### ADR-ARC-003 — Company as Legal/Accounting Boundary
- Domain: Tenancy. Status: PROPOSED. Decision: Company = posting/legal boundary. Options: Company vs Tenant vs Branch. Recommendation: Company. Rationale: SME legal-entity alignment. Consequences: ledger per company. Dependencies: ARC-WP-002. Owner: Multi-Tenant AI Owner. Reviewer: ChatGPT L99. Target: TBD. Evidence: TENANT_COMPANY_BRANCH_MODEL.md.

### ADR-ARC-004 — Explicit Inter-Company Transactions
- Domain: Tenancy. Status: DECISION REQUIRED. Decision: Cross-company transactions require an explicit approval-gated document. Recommendation: yes. Evidence: TENANT_COMPANY_BRANCH_MODEL.md.

### ADR-ARC-005 — Entitlement at Gateway
- Domain: SaaS Product. Status: PROPOSED. Decision: Evaluate entitlement at the gateway before business logic. Recommendation: yes; fail closed. Evidence: SUBSCRIPTION_ENTITLEMENT_MODEL.md.

### ADR-ARC-006 — Suspension Preserves Data
- Domain: SaaS Product. Status: PROPOSED. Decision: Suspension/expiry blocks transactions but preserves data (no deletion). Evidence: SUBSCRIPTION_ENTITLEMENT_MODEL.md.

### ADR-ARC-007 — Posting Only From Approved Document
- Domain: Enterprise Control. Status: PROPOSED. Decision: Posting Engine posts only from an approved source document. Evidence: ENTERPRISE_CONTROL_LAYER.md.

### ADR-ARC-008 — Tenant Data Isolation = Hybrid (RLS baseline)
- Domain: Data. Status: PROPOSED (must remain PROPOSED until Boss). Decision: Hybrid isolation, shared-schema+RLS baseline, dedicated for large/regulated tenants. Evidence: MULTI_TENANT_DATA_ISOLATION_OPTIONS.md.

### ADR-ARC-009 — Non-Overridable SoD Defaults (Financial)
- Domain: Enterprise Control. Status: PROPOSED. Decision: Financial-document SoD defaults are non-overridable. Evidence: ENTERPRISE_CONTROL_LAYER.md.

### ADR-ARC-010 — API/Event-Only Module Integration
- Domain: Application. Status: PROPOSED. Decision: No shared-database integration; APIs/events only. Evidence: APPLICATION_MODULE_BOUNDARY.md.

### ADR-ARC-011 — No Circular Synchronous Dependencies
- Domain: Application. Status: PROPOSED. Decision: Cycles resolved via events. Evidence: APPLICATION_MODULE_BOUNDARY.md.

### ADR-ARC-012 — Single API Gateway Ingress
- Domain: System Context. Status: PROPOSED. Decision: One API Gateway as sole external ingress. Evidence: SYSTEM_CONTEXT_ARCHITECTURE.md.

### ADR-ARC-013 — External Identity Federation
- Domain: IAM. Status: DECISION REQUIRED. Decision: Support external SSO/IdP federation? Evidence: IDENTITY_ACCESS_ARCHITECTURE.md, SYSTEM_CONTEXT_ARCHITECTURE.md.

### ADR-ARC-014 — Stateless Services + Async Backbone
- Domain: Logical/Infra. Status: PROPOSED. Evidence: LOGICAL_COMPONENT_ARCHITECTURE.md.

### ADR-ARC-015 — RBAC+ABAC Deny-by-Default
- Domain: IAM. Status: PROPOSED. Evidence: IDENTITY_ACCESS_ARCHITECTURE.md.

### ADR-ARC-016 — Clean-Room Enforcement
- Domain: Governance/Security. Status: PROPOSED. Decision: No proprietary source implementation copied into SMEsPlus. Evidence: SAAS_ARCHITECTURE_PRINCIPLES.md, `09_Security_Clean_Room`.

### ADR-ARC-017 — At-Least-Once + Idempotent Consumers
- Domain: Integration. Status: PROPOSED. Evidence: INTEGRATION_EVENT_ARCHITECTURE.md.

### ADR-ARC-018 — Make Integrates Only via Gateway/Signed Webhooks
- Domain: Integration. Status: PROPOSED. Evidence: INTEGRATION_EVENT_ARCHITECTURE.md.

### ADR-ARC-019 — Measurable NFR Baseline Adopted
- Domain: NFR. Status: PROPOSED. Evidence: NON_FUNCTIONAL_ARCHITECTURE_REQUIREMENTS.md.

### Summary Table

| ADR ID | Domain | Status | Owner | Target Decision Date | Evidence |
|---|---|---|---|---|---|
| ADR-ARC-001 | Enterprise Control | PROPOSED | Enterprise Control AI Owner | TBD with Boss | ENTERPRISE_CONTROL_LAYER.md |
| ADR-ARC-002 | Data/Integration | PROPOSED | Data Architecture AI Owner | TBD with Boss | LOGICAL_COMPONENT_ARCHITECTURE.md |
| ADR-ARC-003 | Tenancy | PROPOSED | Multi-Tenant AI Owner | TBD with Boss | TENANT_COMPANY_BRANCH_MODEL.md |
| ADR-ARC-004 | Tenancy | DECISION REQUIRED | Multi-Tenant AI Owner | TBD with Boss | TENANT_COMPANY_BRANCH_MODEL.md |
| ADR-ARC-005 | SaaS Product | PROPOSED | SaaS Product AI Owner | TBD with Boss | SUBSCRIPTION_ENTITLEMENT_MODEL.md |
| ADR-ARC-006 | SaaS Product | PROPOSED | SaaS Product AI Owner | TBD with Boss | SUBSCRIPTION_ENTITLEMENT_MODEL.md |
| ADR-ARC-007 | Enterprise Control | PROPOSED | Enterprise Control AI Owner | TBD with Boss | ENTERPRISE_CONTROL_LAYER.md |
| ADR-ARC-008 | Data | PROPOSED | Data Architecture AI Owner | TBD with Boss | MULTI_TENANT_DATA_ISOLATION_OPTIONS.md |
| ADR-ARC-009 | Enterprise Control | PROPOSED | Enterprise Control AI Owner | TBD with Boss | ENTERPRISE_CONTROL_LAYER.md |
| ADR-ARC-010 | Application | PROPOSED | Solution Architecture AI Owner | TBD with Boss | APPLICATION_MODULE_BOUNDARY.md |
| ADR-ARC-011 | Application | PROPOSED | Solution Architecture AI Owner | TBD with Boss | APPLICATION_MODULE_BOUNDARY.md |
| ADR-ARC-012 | System Context | PROPOSED | Technical Architecture AI Owner | TBD with Boss | SYSTEM_CONTEXT_ARCHITECTURE.md |
| ADR-ARC-013 | IAM | DECISION REQUIRED | Identity Architecture AI Owner | TBD with Boss | IDENTITY_ACCESS_ARCHITECTURE.md |
| ADR-ARC-014 | Logical/Infra | PROPOSED | Technical Architecture AI Owner | TBD with Boss | LOGICAL_COMPONENT_ARCHITECTURE.md |
| ADR-ARC-015 | IAM | PROPOSED | Identity Architecture AI Owner | TBD with Boss | IDENTITY_ACCESS_ARCHITECTURE.md |
| ADR-ARC-016 | Governance/Security | PROPOSED | Architecture Governance AI Owner | TBD with Boss | SAAS_ARCHITECTURE_PRINCIPLES.md |
| ADR-ARC-017 | Integration | PROPOSED | Integration AI Owner | TBD with Boss | INTEGRATION_EVENT_ARCHITECTURE.md |
| ADR-ARC-018 | Integration | PROPOSED | Integration AI Owner | TBD with Boss | INTEGRATION_EVENT_ARCHITECTURE.md |
| ADR-ARC-019 | NFR | PROPOSED | NFR Architecture AI Owner | TBD with Boss | NON_FUNCTIONAL_ARCHITECTURE_REQUIREMENTS.md |

## 13. Architecture Decisions

This document IS the decision register; see Section 12.

## 14. Security Considerations

ADR-ARC-008/015/016/017/018 carry security weight; their approval status gates Gate B/D security posture.

## 15. Privacy and Compliance Considerations

Decisions touching personal data (ADR-ARC-008, 013, 015) depend on the confirmed compliance regime.

## 16. Tenant-Isolation Considerations

ADR-ARC-008 is the isolation decision and remains PROPOSED (Gate B HOLD).

## 17. Recovery and Continuity Considerations

ADR-ARC-002/014/017 affect recovery/replay behavior.

## 18. Observability Considerations

Decisions are traceable to evidence documents enabling review observability.

## 19. Capacity and Cost Considerations

ADR-ARC-008/014 affect capacity/cost profile.

## 20. Risks and Gaps

- Decisions in DECISION REQUIRED status (ADR-ARC-004, 013) block related Gate B items until resolved.
- No decision may be marked APPROVED BY BOSS by the AI (control enforced).

## 21. Measurable Acceptance Criteria

| AC ID | Criterion | Verification Method | Required Evidence |
|---|---|---|---|
| AC-001 | Every ADR has all required fields | Review | Section 12 |
| AC-002 | No ADR marked APPROVED BY BOSS | Review | Section 12 |
| AC-003 | Each ADR references an evidence document | Traceability | Summary table |
| AC-004 | Statuses limited to the allowed set | Review | Section 12 |

## 22. Evidence Requirements

| Evidence ID | Type | GitHub Location | Owner | Reviewer | Verification Status |
|---|---|---|---|---|---|
| EV-ARC-012 | ADR register | This file path | ADR Governance AI Owner | ChatGPT L99 | NOT VERIFIED |

## 23. Open Decisions

- All ADRs are open pending independent review and Boss decision; ADR-ARC-004 and ADR-ARC-013 are DECISION REQUIRED.

## 24. Gate Impact

- Gate B input (critical ADR records). Contributes; does not pass.
- Recommendation: DECISION REQUIRED.

## 25. Change History

| Version | Date | Change | Author | Reviewer |
|---|---|---|---|---|
| 0.1 | 2026-07-14 | Initial ADR register | ADR Governance AI Owner (Claude Code drafting agent) | Pending (ChatGPT L99) |

## 26. Approval Status

PREPARED FOR INDEPENDENT REVIEW / HOLD. No ADR is approved. Boss decision mandatory.
