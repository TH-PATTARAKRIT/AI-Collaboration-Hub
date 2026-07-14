# Architecture Risk and Assumption Register (ARC-WP-013)

Document ID: ARC-WP-013
Version: 0.1
Session: [SMEPLUS-26-07-10-001]
Control Level: /L99.99
Status: DRAFT
Approval Status: PREPARED FOR INDEPENDENT REVIEW / HOLD
Gate Status: HOLD

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | ARC-WP-013 |
| Deliverable | ARCHITECTURE_RISK_ASSUMPTION_REGISTER.md |
| Version | 0.1 |
| Architecture Owner | Architecture Risk AI Owner |
| Supporting Owner | PMO Evidence AI |
| Independent Reviewer | ChatGPT L99 |
| Approval Authority | Boss |
| Created | 2026-07-14 |
| Evidence Path | 99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_ARCHITECTURE_ACCELERATION/ARCHITECTURE_RISK_ASSUMPTION_REGISTER.md |
| Verification Status | NOT VERIFIED |

## 2. Purpose

Consolidate architecture risks and assumptions across ARC-WP-001..012, classify critical risks, and record mitigations, owners, evidence and gate impact.

## 3. Scope

All State 03 architecture risks and assumptions in the acceleration batch, including tenant isolation, IAM, data ownership, security, recovery, integration, dependency, clean-room, technology-stack and production-readiness categories.

## 4. Out of Scope

Risk acceptance/approval (Boss authority); build/operational risks outside architecture.

## 5. Architecture Owner

Architecture Risk AI Owner.

## 6. Supporting Owner

PMO Evidence AI.

## 7. Independent Reviewer

ChatGPT L99.

## 8. Dependencies

All ARC-WP-001..012; ARC-WP-014 evidence register.

## 9. Assumptions (Register)

| ID | Assumption | Impact if false | Owner | Status |
|---|---|---|---|---|
| AS-01 | Many small tenants, modest per-tenant volume | Isolation option (ARC-WP-008) may need revision | Data Architecture AI Owner | OPEN |
| AS-02 | JWT/RBAC/ABAC/RLS platform available | IAM/isolation design changes | Identity Architecture AI Owner | OPEN |
| AS-03 | Odoo-first UX is reference-only (no code copy) | Clean-room breach risk | Governance AI Owner | OPEN |
| AS-04 | Business events are immutable | Audit/replay guarantees weakened | Data Architecture AI Owner | OPEN |
| AS-05 | Company = legal/accounting boundary | Tenancy/posting model revision | Multi-Tenant AI Owner | OPEN |

## 10. Current State

Risks were embedded in individual documents; no consolidated, classified register existed.

## 11. Target State

A single classified risk/assumption register with mitigations and gate impact, feeding independent review and Boss decisions.

## 12. Architecture Model (Risk Register)

Fields: ID · category · description · cause · architecture impact · probability · severity · priority · owner · mitigation · evidence · target date · status · gate impact.

| ID | Category | Description | Cause | Impact | Prob | Sev | Priority | Owner | Mitigation | Evidence | Target | Status | Gate Impact |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RK-01 | Tenant isolation | RLS misconfiguration → cross-tenant leak | Shared-schema baseline | Data breach | Med | Critical | P0 | Data Architecture AI Owner | Automated RLS/isolation test suite; hybrid dedicated for regulated | MULTI_TENANT_DATA_ISOLATION_OPTIONS.md | TBD | OPEN | Gate B HOLD |
| RK-02 | IAM | Cross-tenant privilege escalation via mis-scoped role | ABAC scope defect | Unauthorized access | Med | Critical | P0 | Identity Architecture AI Owner | Deny-by-default, scope tests, review | IDENTITY_ACCESS_ARCHITECTURE.md | TBD | OPEN | Gate B HOLD |
| RK-03 | Data ownership | Ambiguous Company vs Branch legal entity | SME structure variance | Wrong posting boundary | Med | High | P1 | Multi-Tenant AI Owner | ADR-ARC-003/004 decision | TENANT_COMPANY_BRANCH_MODEL.md | TBD | OPEN | Gate B |
| RK-04 | Security | High/Critical vulnerability at release | Insufficient sec testing | Exploit | Low | Critical | P0 | Security Architecture AI Owner | SAST/DAST gate, security review | NON_FUNCTIONAL_ARCHITECTURE_REQUIREMENTS.md | TBD | OPEN | Gate D |
| RK-05 | Recovery | Unconfirmed RPO/RTO/DR level under-provisions resilience | Missing business input | Data loss/downtime | Med | High | P1 | NFR Architecture AI Owner | Confirm targets, restore/DR tests | NON_FUNCTIONAL_ARCHITECTURE_REQUIREMENTS.md | TBD | OPEN | Gate D |
| RK-06 | Integration | Non-idempotent consumer duplicates posting on retry | At-least-once delivery | Financial error | Med | Critical | P0 | Integration AI Owner | Idempotency keys (ADR-ARC-017) | INTEGRATION_EVENT_ARCHITECTURE.md | TBD | OPEN | Gate B/C |
| RK-07 | Architecture dependency | Accounting high fan-in bottleneck | Central posting consumer | Availability risk | Med | High | P1 | Solution Architecture AI Owner | Async posting, scaling | APPLICATION_MODULE_BOUNDARY.md | TBD | OPEN | Gate B/C |
| RK-08 | Clean-room compliance | Source implementation copied into code | Odoo-first misuse | Legal/IP breach | Low | Critical | P0 | Governance AI Owner | Clean-room policy enforcement (ADR-ARC-016) | SAAS_ARCHITECTURE_PRINCIPLES.md | TBD | OPEN | Gate B/D |
| RK-09 | Technology-stack decision | Stack not locked; event store/DB undecided | Pending Boss decision | Design churn | High | Med | P1 | Enterprise Architecture AI Owner | Keep decisions PROPOSED; ADRs | ARCHITECTURE_DECISION_REGISTER.md | TBD | OPEN | Gate B |
| RK-10 | Production readiness | Gate B/C/D evidence incomplete | Preparation phase | Premature build | High | High | P0 | PMO Evidence AI | Enforce No Evidence=No Progress; HOLD | STATE03_EVIDENCE_REGISTER.md | TBD | OPEN | Gate B/C/D HOLD |
| RK-11 | Privacy/compliance | PDPA/residency regime unconfirmed | Missing decision | Compliance gap | Med | High | P1 | Privacy AI Owner | Confirm regime; classify data | NON_FUNCTIONAL_ARCHITECTURE_REQUIREMENTS.md | TBD | OPEN | Gate B/D |
| RK-12 | Entitlement | Stale entitlement cache grants revoked access | Cache without invalidation | Unauthorized feature use | Med | High | P1 | SaaS Product AI Owner | Event-driven invalidation | SUBSCRIPTION_ENTITLEMENT_MODEL.md | TBD | OPEN | Gate B |

### Critical Risk Classification (P0/Critical)
RK-01 (tenant isolation), RK-02 (IAM), RK-04 (security), RK-06 (integration/posting), RK-08 (clean-room), RK-10 (production readiness) are the controlling critical risks holding Gate B/C/D.

## 13. Architecture Decisions

Risks map to ADRs in ARC-WP-012 (e.g., RK-01→ADR-ARC-008, RK-06→ADR-ARC-017, RK-08→ADR-ARC-016).

## 14. Security Considerations

RK-01, RK-02, RK-04, RK-08 are security-critical; unresolved status keeps Gate B/D on HOLD.

## 15. Privacy and Compliance Considerations

RK-11 tracks the unconfirmed compliance regime.

## 16. Tenant-Isolation Considerations

RK-01 is the controlling isolation risk (Critical).

## 17. Recovery and Continuity Considerations

RK-05 tracks recovery-target confirmation.

## 18. Observability Considerations

Each critical risk has an observable signal (isolation test, scope violation logs, DLQ depth) enabling detection.

## 19. Capacity and Cost Considerations

RK-07, RK-09 affect capacity/cost planning.

## 20. Risks and Gaps

Meta-gap: several risks lack target dates (TBD) pending Boss/Owner scheduling.

## 21. Measurable Acceptance Criteria

| AC ID | Criterion | Verification Method | Required Evidence |
|---|---|---|---|
| AC-001 | Every risk has all required fields | Review | Section 12 |
| AC-002 | Critical categories (isolation/IAM/security/clean-room/recovery/integration) each represented | Review | Section 12 |
| AC-003 | Each risk references evidence document | Traceability | Section 12 |
| AC-004 | Critical risks mapped to gate impact | Review | Section 12 |

## 22. Evidence Requirements

| Evidence ID | Type | GitHub Location | Owner | Reviewer | Verification Status |
|---|---|---|---|---|---|
| EV-ARC-013 | Risk/assumption register | This file path | Architecture Risk AI Owner | ChatGPT L99 | NOT VERIFIED |

## 23. Open Decisions

- Target dates and risk acceptance are Boss/Owner decisions. DECISION REQUIRED.

## 24. Gate Impact

- Gate B automatic-HOLD "critical risks have no owner" is mitigated (all risks have owners); residual open critical risks keep Gate B/C/D on HOLD. Contributes; does not pass.
- Recommendation: RECOMMEND HOLD.

## 25. Change History

| Version | Date | Change | Author | Reviewer |
|---|---|---|---|---|
| 0.1 | 2026-07-14 | Initial risk/assumption register | Architecture Risk AI Owner (Claude Code drafting agent) | Pending (ChatGPT L99) |

## 26. Approval Status

PREPARED FOR INDEPENDENT REVIEW / HOLD. Independent review and Boss decision remain mandatory.
