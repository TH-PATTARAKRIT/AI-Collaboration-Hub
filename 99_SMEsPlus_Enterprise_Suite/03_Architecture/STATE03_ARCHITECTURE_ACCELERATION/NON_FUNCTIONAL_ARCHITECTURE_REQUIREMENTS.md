# Non-Functional Architecture Requirements (ARC-WP-011)

Document ID: ARC-WP-011
Version: 0.2
Session: [SMEPLUS-26-07-10-001]
Control Level: /L99.99
Status: DRAFT
Approval Status: PREPARED FOR REVIEW / HOLD
Gate Status: HOLD
Correction Reference: L99 Review Finding P1-01 (Batch 001 remediation)

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | ARC-WP-011 |
| Deliverable | NON_FUNCTIONAL_ARCHITECTURE_REQUIREMENTS.md |
| Version | 0.2 |
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

- A-001: Numeric targets below are **not** approved architecture baselines. Following L99 finding P1-01, every NFR is classified by evidence basis (APPROVED BASELINE / PROPOSED TARGET / ASSUMPTION / TBD WITH OWNER / REQUIRED HARD CONTROL). Claude Code cannot classify anything as APPROVED BASELINE because no Boss-approved capacity/business/SLA evidence exists yet.
- A-002: REQUIRED HARD CONTROLs are non-negotiable architecture controls (e.g., zero cross-tenant access) rather than tunable performance numbers.

## 10. Current State

Principles require performance/observability targets in SDS but no consolidated measurable NFR set exists for the Enterprise Suite.

## 11. Target State

A measurable NFR baseline that Gate B, C and D can test against.

## 12. Architecture Model (Classified NFRs)

### 12.1 Classification Legend
- **APPROVED BASELINE** — value approved by Boss with recorded evidence. (None yet; Claude Code cannot assign this.)
- **PROPOSED TARGET** — hypothesis requiring capacity/business/infrastructure validation.
- **ASSUMPTION** — working assumption that must be confirmed.
- **TBD WITH OWNER** — value not yet available; owner must supply.
- **REQUIRED HARD CONTROL** — non-negotiable architecture control (not a tunable number).

### 12.2 NFR Table (with classification)

| NFR ID | Category | Requirement | Classification | Verification |
|---|---|---|---|---|
| NFR-AVL-01 | Availability | Core services monthly uptime target (proposed 99.5%; GA aspiration 99.9%) | PROPOSED TARGET — REQUIRES CAPACITY / BUSINESS / INFRASTRUCTURE VALIDATION | Uptime monitor |
| NFR-PERF-01 | Response time | p95 interactive API ≤ 500 ms; p99 ≤ 1200 ms (proposed) | PROPOSED TARGET — REQUIRES CAPACITY / BUSINESS / INFRASTRUCTURE VALIDATION | Load test |
| NFR-PERF-02 | Throughput | Sustain ≥ 100 req/s per core instance (proposed) | PROPOSED TARGET — REQUIRES CAPACITY / BUSINESS / INFRASTRUCTURE VALIDATION | Load test |
| NFR-SCAL-01 | Scalability | Horizontal scale to 2× load by adding stateless instances, no code change | PROPOSED TARGET | Scaling test |
| NFR-SCAL-02 | Scalability | Support target active tenants on shared tier (proposed ~1,000) | ASSUMPTION — REQUIRES CAPACITY / BUSINESS VALIDATION | Capacity model |
| NFR-ISO-01 | Tenant isolation | Zero tolerated cross-tenant data access | REQUIRED HARD CONTROL | RLS/isolation test |
| NFR-SEC-01 | Security | Encryption in transit (TLS 1.2+) on all external endpoints; access-control enforced; MFA for privileged roles | REQUIRED HARD CONTROL | Security scan |
| NFR-SEC-02 | Security | No High/Critical vulnerability open at release | REQUIRED HARD CONTROL | SAST/DAST |
| NFR-AUD-01 | Auditability | All privileged/critical actions produce immutable audit evidence | REQUIRED HARD CONTROL | Audit test |
| NFR-POST-01 | Integrity | Idempotent posting (no duplicate ledger/stock effect) | REQUIRED HARD CONTROL | Idempotency test |
| NFR-BAK-01 | Backup | Backup and restore capability exists; backups encrypted at rest | REQUIRED HARD CONTROL | Backup log |
| NFR-REC-01 | Recoverability | Documented, tested restore procedure per stateful store | REQUIRED HARD CONTROL | Restore test |
| NFR-PRIV-01 | Privacy | Personal data classified and access-logged; retention enforced | REQUIRED HARD CONTROL (periods TBD) | Audit review |
| NFR-DR-01 | Disaster recovery | DR exercise passes at required service level | TBD WITH OWNER (DR level) | DR exercise |
| NFR-RPO-01 | RPO | Data-loss window for transactional data (proposed ≤ 15 min) | PROPOSED TARGET — TBD WITH OWNER | Recovery test |
| NFR-RTO-01 | RTO | Service restoration for critical services (proposed ≤ 4 h) | PROPOSED TARGET — TBD WITH OWNER | Recovery test |
| NFR-MNT-01 | Maintainability | Each module independently deployable; change lead-time measured | PROPOSED TARGET | Pipeline metric |
| NFR-DEP-01 | Deployability | Zero-manual-risk-step production deploy (AP-010) | REQUIRED HARD CONTROL | Pipeline audit |
| NFR-OBS-01 | Observability | All services emit logs/metrics/traces + health check | REQUIRED HARD CONTROL | Observability check |
| NFR-CAP-01 | Capacity | Per-tenant and per-service capacity metrics available | PROPOSED TARGET | Metrics review |
| NFR-RET-01 | Data retention | Retention policy per data class defined and enforced | TBD WITH OWNER (periods) | Policy review |
| NFR-COST-01 | Cost control | Per-tenant cost allocation available; cost alerts configured | PROPOSED TARGET — REQUIRES INFRASTRUCTURE BUDGET VALIDATION | FinOps report |

### 12.3 NFR Evidence Basis Table

| NFR ID | Proposed Value | Classification | Basis | Evidence Path | Owner | Validation Method | Decision Status | Gate Impact |
|---|---|---|---|---|---|---|---|---|
| NFR-AVL-01 | 99.5% / 99.9% GA | PROPOSED TARGET | Industry norm hypothesis; no SLA evidence | TBD WITH OWNER | NFR Architecture AI Owner | Uptime monitor over agreed window | DECISION REQUIRED | Gate B/D |
| NFR-PERF-01 | p95 ≤ 500 ms / p99 ≤ 1200 ms | PROPOSED TARGET | Hypothesis; no workload profile | TBD WITH OWNER | NFR Architecture AI Owner | Load test vs profile | DECISION REQUIRED | Gate B/C |
| NFR-PERF-02 | ≥ 100 req/s per instance | PROPOSED TARGET | Hypothesis; no workload profile | TBD WITH OWNER | Infrastructure AI Owner | Load test | DECISION REQUIRED | Gate C |
| NFR-SCAL-02 | ~1,000 tenants shared tier | ASSUMPTION | Sizing assumption AS-01 | ARCHITECTURE_RISK_ASSUMPTION_REGISTER.md | Data Architecture AI Owner | Capacity model | DECISION REQUIRED | Gate B |
| NFR-ISO-01 | 0 cross-tenant access | REQUIRED HARD CONTROL | PR-09 isolation principle | SAAS_ARCHITECTURE_PRINCIPLES.md; MULTI_TENANT_DATA_ISOLATION_OPTIONS.md | Data Architecture AI Owner | RLS/isolation test suite | REQUIRED | Gate B/D |
| NFR-SEC-01 | TLS 1.2+, MFA privileged | REQUIRED HARD CONTROL | AP-003 security-by-design | IDENTITY_ACCESS_ARCHITECTURE.md | Security Architecture AI Owner | Security scan | REQUIRED | Gate D |
| NFR-SEC-02 | 0 High/Critical at release | REQUIRED HARD CONTROL | Security policy | SAAS_ARCHITECTURE_PRINCIPLES.md (PR-10) | Security Architecture AI Owner | SAST/DAST | REQUIRED | Gate D |
| NFR-AUD-01 | 100% critical actions audited | REQUIRED HARD CONTROL | AP-008 audit-by-design | ENTERPRISE_CONTROL_LAYER.md | Enterprise Control AI Owner | Audit test | REQUIRED | Gate B/D |
| NFR-POST-01 | Idempotent posting | REQUIRED HARD CONTROL | ADR-ARC-017 | INTEGRATION_EVENT_ARCHITECTURE.md | Integration AI Owner | Idempotency test | REQUIRED | Gate B/C |
| NFR-BAK-01 | Backup+restore, encrypted | REQUIRED HARD CONTROL | PR-14 backup principle | LOGICAL_COMPONENT_ARCHITECTURE.md | Infrastructure AI Owner | Backup/restore log | REQUIRED | Gate D |
| NFR-RPO-01 | ≤ 15 min (proposed) | PROPOSED TARGET | No business RPO input | TBD WITH OWNER | NFR Architecture AI Owner | Recovery test | DECISION REQUIRED | Gate D |
| NFR-RTO-01 | ≤ 4 h (proposed) | PROPOSED TARGET | No business RTO input | TBD WITH OWNER | NFR Architecture AI Owner | Recovery test | DECISION REQUIRED | Gate D |
| NFR-DR-01 | DR at required level | TBD WITH OWNER | DR service level undefined | TBD WITH OWNER | Resilience AI Owner | DR exercise | DECISION REQUIRED | Gate D |
| NFR-RET-01 | Retention per data class | TBD WITH OWNER | Legal retention undefined | TBD WITH OWNER | Privacy AI Owner | Policy review | DECISION REQUIRED | Gate B/D |
| NFR-COST-01 | Per-tenant cost + alerts | PROPOSED TARGET | No infra budget | TBD WITH OWNER | FinOps AI Owner | FinOps report | DECISION REQUIRED | Gate D |

## 13. Architecture Decisions

- ADR-ARC-019 (NFR set adopted as measurable Gate B/C/D targets, each classified by evidence basis; no value represented as APPROVED BASELINE without Boss evidence): PROPOSED.

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

### 20.1 Required Missing Inputs (recorded gaps — feed STATE03_GAP_REGISTER.md)

| Gap ID | Missing Input | Needed For | Status |
|---|---|---|---|
| NFRGAP-01 | Expected concurrent users | PERF/SCAL targets | DECISION REQUIRED |
| NFRGAP-02 | Expected number of tenants | SCAL/capacity | DECISION REQUIRED |
| NFRGAP-03 | Average and peak transactions | PERF/throughput | DECISION REQUIRED |
| NFRGAP-04 | API workload profile | PERF-01/02 | DECISION REQUIRED |
| NFRGAP-05 | Data growth rate | capacity/cost | DECISION REQUIRED |
| NFRGAP-06 | Document storage volume | capacity/cost | DECISION REQUIRED |
| NFRGAP-07 | Reporting workload | PERF/capacity | DECISION REQUIRED |
| NFRGAP-08 | Customer SLA | AVL/RPO/RTO | DECISION REQUIRED |
| NFRGAP-09 | Infrastructure budget | COST-01 | DECISION REQUIRED |
| NFRGAP-10 | Backup window | BAK/REC | DECISION REQUIRED |
| NFRGAP-11 | Legal retention periods | RET-01/PRIV-01 | DECISION REQUIRED |
| NFRGAP-12 | RPO/RTO classification | RPO-01/RTO-01 | DECISION REQUIRED |
| NFRGAP-13 | DR service level | DR-01 | DECISION REQUIRED |

## 21. Measurable Acceptance Criteria

| AC ID | Criterion | Verification Method | Required Evidence |
|---|---|---|---|
| AC-001 | Every NFR classified (APPROVED BASELINE / PROPOSED TARGET / ASSUMPTION / TBD WITH OWNER / REQUIRED HARD CONTROL) | Review | Section 12.2 |
| AC-002 | No numeric target represented as APPROVED BASELINE without Boss evidence | Review | Section 12 |
| AC-003 | NFR Evidence Basis table present with basis, evidence path, owner, validation method, decision status | Review | Section 12.3 |
| AC-004 | No vague terms ("fast"/"secure") used as requirements | Review | Section 12 |
| AC-005 | Isolation NFR is REQUIRED HARD CONTROL, zero cross-tenant access | Review | NFR-ISO-01 |
| AC-006 | Missing business/infra inputs recorded as gaps | Review | Section 20.1 |

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
| 0.2 | 2026-07-14 | P1-01 remediation: every NFR classified by evidence basis; added NFR Evidence Basis table; recorded 13 missing business/infra input gaps; no value represented as approved baseline | NFR Architecture AI Owner (Claude Code Expert correction agent) | Pending (ChatGPT L99) |

## 26. Approval Status

PREPARED FOR REVIEW / HOLD. No numeric target is an approved baseline. Independent review and Boss decision remain mandatory.
