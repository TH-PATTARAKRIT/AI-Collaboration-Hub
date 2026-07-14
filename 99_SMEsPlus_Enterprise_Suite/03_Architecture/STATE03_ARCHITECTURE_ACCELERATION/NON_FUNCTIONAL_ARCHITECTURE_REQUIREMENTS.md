# Non-Functional Architecture Requirements (ARC-WP-011)

Document ID: ARC-WP-011
Version: 0.1
Session: [SMEPLUS-26-07-10-001]
Control Level: /L99.99
Status: DRAFT
Approval Status: PREPARED FOR INDEPENDENT REVIEW / HOLD
Gate Status: HOLD

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | ARC-WP-011 |
| Deliverable | NON_FUNCTIONAL_ARCHITECTURE_REQUIREMENTS.md |
| Version | 0.1 |
| Architecture Owner | NFR Architecture AI Owner |
| Supporting Owner | Infrastructure Architecture AI Owner |
| Independent Reviewer | ChatGPT L99 |
| Approval Authority | Boss |
| Created | 2026-07-14 |
| Evidence Path | 99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_ARCHITECTURE_ACCELERATION/NON_FUNCTIONAL_ARCHITECTURE_REQUIREMENTS.md |
| Verification Status | NOT VERIFIED |

## 2. Purpose

Define measurable non-functional requirements (NFRs) for the SMEsPlus Enterprise Suite. Every requirement is either measurable or explicitly marked `TBD with Owner`. Vague terms ("fast", "secure") are not permitted.

## 3. Scope

Availability, performance, response time, throughput, scalability, tenant isolation, security, privacy, auditability, recoverability, backup, DR, RPO, RTO, maintainability, deployability, observability, capacity, data retention, cost control.

## 4. Out of Scope

- Final target values approval (Boss decision).
- Load-test execution (build/release state).

## 5. Architecture Owner

NFR Architecture AI Owner.

## 6. Supporting Owner

Infrastructure Architecture AI Owner.

## 7. Independent Reviewer

ChatGPT L99.

## 8. Dependencies

- ARC-WP-007 (layers), ARC-WP-008 (isolation), ARC-WP-009 (security), ARC-WP-010 (events).

## 9. Assumptions

- A-001: Values below are proposed baselines pending Boss confirmation; those needing business input are marked TBD with Owner.

## 10. Current State

Principles require performance/observability targets in SDS but no consolidated measurable NFR set exists for the Enterprise Suite.

## 11. Target State

A measurable NFR baseline that Gate B, C and D can test against.

## 12. Architecture Model (NFR Table)

| NFR ID | Category | Measurable Requirement (proposed) | Verification |
|---|---|---|---|
| NFR-AVL-01 | Availability | Core services monthly uptime ≥ 99.5% (target 99.9% at GA) — GA target TBD with Owner | Uptime monitor |
| NFR-PERF-01 | Response time | p95 interactive API response ≤ 500 ms; p99 ≤ 1200 ms under nominal load | Load test |
| NFR-PERF-02 | Throughput | Sustain ≥ 100 requests/s per core service instance at p95 target | Load test |
| NFR-SCAL-01 | Scalability | Horizontal scale to 2× load by adding stateless instances, no code change | Scaling test |
| NFR-SCAL-02 | Scalability | Support ≥ 1,000 active tenants on shared tier — exact target TBD with Owner | Capacity model |
| NFR-ISO-01 | Tenant isolation | Zero cross-tenant data access in isolation test suite (0 tolerated) | RLS/isolation test |
| NFR-SEC-01 | Security | 100% external endpoints TLS 1.2+; MFA enforced for privileged roles | Security scan |
| NFR-SEC-02 | Security | No High/Critical vulnerabilities open at release | SAST/DAST |
| NFR-PRIV-01 | Privacy | Personal data fields classified and access-logged; retention enforced | Audit review |
| NFR-AUD-01 | Auditability | 100% of critical actions produce immutable audit events | Audit test |
| NFR-REC-01 | Recoverability | Documented, tested restore procedure for each stateful store | Restore test |
| NFR-BAK-01 | Backup | Automated backups ≥ every 24h; encrypted at rest | Backup log |
| NFR-DR-01 | Disaster recovery | DR exercise passes at required level (level TBD with Owner) | DR exercise |
| NFR-RPO-01 | RPO | Data loss window ≤ 15 minutes for transactional data — TBD with Owner to confirm | Recovery test |
| NFR-RTO-01 | RTO | Service restoration ≤ 4 hours for critical services — TBD with Owner to confirm | Recovery test |
| NFR-MNT-01 | Maintainability | Each module independently deployable; change lead-time measured | Pipeline metric |
| NFR-DEP-01 | Deployability | Zero-manual-risk-step production deploy (AP-010) | Pipeline audit |
| NFR-OBS-01 | Observability | 100% services emit logs/metrics/traces + health check | Observability check |
| NFR-CAP-01 | Capacity | Per-tenant and per-service capacity metrics available | Metrics review |
| NFR-RET-01 | Data retention | Retention policy per data class defined and enforced — periods TBD with Owner | Policy review |
| NFR-COST-01 | Cost control | Per-tenant cost allocation available; cost alerts configured | FinOps report |

## 13. Architecture Decisions

- ADR-ARC-019 (NFR baseline set adopted as measurable Gate B/C/D targets): PROPOSED.

## 14. Security Considerations

NFR-SEC-01/02, NFR-ISO-01, NFR-AUD-01 are security-critical and feed Gate D test evidence.

## 15. Privacy and Compliance Considerations

NFR-PRIV-01 and NFR-RET-01 depend on the confirmed compliance regime (DECISION REQUIRED).

## 16. Tenant-Isolation Considerations

NFR-ISO-01 tolerates zero cross-tenant access and is a Gate B/D hard requirement.

## 17. Recovery and Continuity Considerations

NFR-REC/BAK/DR/RPO/RTO define the measurable recovery envelope; several values are TBD with Owner.

## 18. Observability Considerations

NFR-OBS-01 mandates full-signal coverage; thresholds/alerts derive from PERF and AVL targets.

## 19. Capacity and Cost Considerations

NFR-CAP-01 and NFR-COST-01 provide the capacity/cost measurement basis.

## 20. Risks and Gaps

- R-011-01: Unconfirmed RPO/RTO/DR-level could under-provision resilience. Severity: High. Status: DECISION REQUIRED.
- G-011-01: Several targets are TBD with Owner pending business input.

## 21. Measurable Acceptance Criteria

| AC ID | Criterion | Verification Method | Required Evidence |
|---|---|---|---|
| AC-001 | Every listed category has a measurable value or TBD-with-Owner | Review | Section 12 |
| AC-002 | No vague terms ("fast"/"secure") used as requirements | Review | Section 12 |
| AC-003 | Isolation NFR tolerates zero cross-tenant access | Review | NFR-ISO-01 |
| AC-004 | RPO/RTO expressed as time values | Review | NFR-RPO/RTO |

## 22. Evidence Requirements

| Evidence ID | Type | GitHub Location | Owner | Reviewer | Verification Status |
|---|---|---|---|---|---|
| EV-ARC-011 | NFR baseline | This file path | NFR Architecture AI Owner | ChatGPT L99 | NOT VERIFIED |

## 23. Open Decisions

- OD-011-01: Confirm availability GA target, RPO, RTO, DR level. DECISION REQUIRED.
- OD-011-02: Confirm retention periods per data class. DECISION REQUIRED.

## 24. Gate Impact

- Gate B input (measurable NFRs) and Gate D test basis. Contributes; does not pass.
- Recommendation: READY FOR INDEPENDENT REVIEW.

## 25. Change History

| Version | Date | Change | Author | Reviewer |
|---|---|---|---|---|
| 0.1 | 2026-07-14 | Initial measurable NFR baseline | NFR Architecture AI Owner (Claude Code drafting agent) | Pending (ChatGPT L99) |

## 26. Approval Status

PREPARED FOR INDEPENDENT REVIEW / HOLD. Independent review and Boss decision remain mandatory.
