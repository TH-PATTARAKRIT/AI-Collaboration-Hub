# Multi-Tenant Data Isolation Options (ARC-WP-008)

Document ID: ARC-WP-008
Version: 0.1
Session: [SMEPLUS-26-07-10-001]
Control Level: /L99.99
Status: DRAFT
Approval Status: PREPARED FOR INDEPENDENT REVIEW / HOLD
Gate Status: HOLD
Decision Status: PROPOSED (must remain PROPOSED until approved by Boss)

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | ARC-WP-008 |
| Deliverable | MULTI_TENANT_DATA_ISOLATION_OPTIONS.md |
| Version | 0.1 |
| Architecture Owner | Data Architecture AI Owner |
| Supporting Owner | Access Architecture AI Owner |
| Independent Reviewer | ChatGPT L99 |
| Approval Authority | Boss |
| Created | 2026-07-14 |
| Evidence Path | 99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_ARCHITECTURE_ACCELERATION/MULTI_TENANT_DATA_ISOLATION_OPTIONS.md |
| Verification Status | NOT VERIFIED |

## 2. Purpose

Compare multi-tenant data isolation options for SMEsPlus and record a recommendation (status PROPOSED) across security, operations, backup/recovery, scaling, cost, migration complexity and compliance dimensions.

## 3. Scope

- Isolation options: database-per-tenant, schema-per-tenant, shared-schema with tenant key, hybrid.
- Comparison and a recommendation with rationale (PROPOSED only).

## 4. Out of Scope

- Final selection/approval (Boss decision, remains HOLD).
- Physical DB engine selection (stack not locked).

## 5. Architecture Owner

Data Architecture AI Owner.

## 6. Supporting Owner

Access Architecture AI Owner.

## 7. Independent Reviewer

ChatGPT L99.

## 8. Dependencies

- ARC-WP-002 (tenant model), ARC-WP-009 (access), ARC-WP-011 (NFR backup/RPO/RTO).

## 9. Assumptions

- A-001: Tenant is the hard isolation boundary (PR-09).
- A-002: SME tenant count is expected to be large with modest per-tenant volume (assumption; DECISION REQUIRED to confirm sizing).
- A-003: RLS-capable data platform is available (per SaaS Foundation AP-003).

## 10. Current State

SaaS Foundation mandates tenant isolation and database RLS (AP-002, AP-003) but the isolation option is not decided.

## 11. Target State

A reviewed comparison and a PROPOSED recommendation feeding an ADR (ARC-WP-012), pending Boss approval.

## 12. Architecture Model

### 12.1 Options
- **O1 Database-per-tenant**: one physical database per tenant.
- **O2 Schema-per-tenant**: one schema per tenant in a shared database.
- **O3 Shared-schema with tenant key**: single schema, `tenant_id` on every row, enforced by RLS.
- **O4 Hybrid**: shared-schema by default; dedicated database/schema for large or regulated tenants.

### 12.2 Comparison

| Dimension | O1 DB-per-tenant | O2 Schema-per-tenant | O3 Shared-schema | O4 Hybrid |
|---|---|---|---|---|
| Security/isolation | Strongest | Strong | Moderate (RLS-dependent) | Strong (tunable) |
| Operational simplicity | Low (many DBs) | Moderate | High | Moderate |
| Backup/recovery granularity | Per-tenant native | Per-schema | Logical/filtered | Per-tenant for dedicated |
| Scaling | Costly at high tenant count | Better | Best density | Best balance |
| Cost | Highest | Moderate | Lowest | Moderate |
| Migration complexity | High (schema drift across DBs) | Moderate | Low | Moderate/High |
| Privacy/compliance | Easiest data residency | Moderate | Hardest per-tenant residency | Tunable |

### 12.3 Recommendation (PROPOSED)
**O4 Hybrid**, defaulting to **O3 shared-schema + RLS** for the SME long tail and provisioning **O1/O2 dedicated** for large or regulated tenants. This balances density/cost for many small tenants with strong isolation where required.

### 12.4 Rationale
- Aligns with expected many-small-tenant profile (density/cost).
- Preserves an escalation path for enterprise/regulated tenants without re-architecting.
- Keeps RLS as the baseline enforcement while allowing physical isolation on demand.

## 13. Architecture Decisions

- ADR-ARC-008 (Tenant data isolation = Hybrid, RLS baseline): PROPOSED. Must remain PROPOSED until Boss approval.

## 14. Security Considerations

RLS baseline requires rigorous policy testing; a single RLS defect risks cross-tenant exposure. Dedicated isolation mitigates for high-risk tenants.

## 15. Privacy and Compliance Considerations

Data residency for regulated tenants is more easily met with dedicated databases (O1/O4). PDPA/residency requirements: DECISION REQUIRED.

## 16. Tenant-Isolation Considerations

This document is the core Gate B "tenant isolation strategy" input; automatic HOLD applies until a decision is approved.

## 17. Recovery and Continuity Considerations

Per-tenant restore is native in O1/O4-dedicated and filtered/logical in O3; RPO/RTO targets in ARC-WP-011 must be achievable under the chosen option.

## 18. Observability Considerations

Cross-tenant access attempts must be logged and alertable regardless of option; RLS policy coverage must be measurable.

## 19. Capacity and Cost Considerations

O3 maximizes density/lowest cost; O1 highest cost. Hybrid lets cost scale with tenant risk profile.

## 20. Risks and Gaps

- R-008-01: RLS misconfiguration → cross-tenant leak. Severity: Critical. Mitigation: automated RLS test suite.
- R-008-02: Hybrid increases operational surface (two patterns). Severity: Medium.
- G-008-01: Tenant sizing/residency requirements unconfirmed.

## 21. Measurable Acceptance Criteria

| AC ID | Criterion | Verification Method | Required Evidence |
|---|---|---|---|
| AC-001 | Four options compared across seven dimensions | Review | Section 12.2 |
| AC-002 | Recommendation recorded as PROPOSED with rationale | Review | Sections 12.3/12.4 |
| AC-003 | Decision status remains PROPOSED (not approved) | Review | Header + Section 13 |
| AC-004 | Cross-tenant leak risk classified Critical | Review | Section 20 |

## 22. Evidence Requirements

| Evidence ID | Type | GitHub Location | Owner | Reviewer | Verification Status |
|---|---|---|---|---|---|
| EV-ARC-008 | Isolation options analysis | This file path | Data Architecture AI Owner | ChatGPT L99 | NOT VERIFIED |

## 23. Open Decisions

- OD-008-01: Approve isolation option. DECISION REQUIRED (Boss).
- OD-008-02: Confirm tenant sizing and data-residency requirements. DECISION REQUIRED.

## 24. Gate Impact

- Gate B automatic-HOLD condition "tenant isolation unclear" applies until decided. Contributes; does not pass. Currently HOLD.
- Recommendation: DECISION REQUIRED.

## 25. Change History

| Version | Date | Change | Author | Reviewer |
|---|---|---|---|---|
| 0.1 | 2026-07-14 | Initial draft with PROPOSED recommendation | Data Architecture AI Owner (Claude Code drafting agent) | Pending (ChatGPT L99) |

## 26. Approval Status

PREPARED FOR INDEPENDENT REVIEW / HOLD. Recommendation is PROPOSED only. Independent review and Boss decision remain mandatory.
