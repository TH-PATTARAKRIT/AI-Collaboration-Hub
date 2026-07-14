# Identity and Access Architecture (ARC-WP-009)

Document ID: ARC-WP-009
Version: 0.1
Session: [SMEPLUS-26-07-10-001]
Control Level: /L99.99
Status: DRAFT
Approval Status: PREPARED FOR INDEPENDENT REVIEW / HOLD
Gate Status: HOLD

## 1. Document Control

| Field | Value |
|---|---|
| Document ID | ARC-WP-009 |
| Deliverable | IDENTITY_ACCESS_ARCHITECTURE.md |
| Version | 0.1 |
| Architecture Owner | Identity Architecture AI Owner |
| Supporting Owner | Multi-Tenant Architecture AI Owner |
| Independent Reviewer | ChatGPT L99 |
| Approval Authority | Boss |
| Created | 2026-07-14 |
| Evidence Path | 99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_ARCHITECTURE_ACCELERATION/IDENTITY_ACCESS_ARCHITECTURE.md |
| Verification Status | NOT VERIFIED |

## 2. Purpose

Define the identity and access architecture: identity sources, authentication and authorization models, RBAC, data-scope binding to tenant/company/branch, privileged access, service accounts, session and MFA concepts, and the joiner/mover/leaver lifecycle.

## 3. Scope

- Authentication, authorization, RBAC and data scope.
- Privileged access, service accounts, API auth, sessions, MFA.
- Access review, SoD, logging/audit.

## 4. Out of Scope

- Isolation storage mechanism (ARC-WP-008).
- Enterprise-control approval logic (ARC-WP-004).

## 5. Architecture Owner

Identity Architecture AI Owner.

## 6. Supporting Owner

Multi-Tenant Architecture AI Owner.

## 7. Independent Reviewer

ChatGPT L99.

## 8. Dependencies

- ARC-WP-002 (scopes), ARC-WP-003 (entitlement), ARC-WP-004 (SoD), MODULE_SPEC_AUTHORIZATION.md, MODULE_SPEC_USER_ROLE_MANAGEMENT.md, FR_DETAIL_AUTHORIZATION.md.

## 9. Assumptions

- A-001: JWT-based authentication and RBAC+ABAC per SaaS Foundation AP-003.
- A-002: Every request resolves tenant before authorization.
- A-003: MFA is supported (MFA-ready) with enforcement configurable per tenant.

## 10. Current State

Authorization and User/Role modules define roles and permissions functionally (FR-AUTH), and principles mandate JWT/RBAC/ABAC/MFA-ready, but no consolidated IAM architecture with data-scope binding and lifecycle exists.

## 11. Target State

An authoritative IAM model binding identity → role → permission → data scope, with privileged-access control, service-account governance, MFA, sessions and JML lifecycle, addressing the Gate B "identity and access scope unclear" HOLD condition.

## 12. Architecture Model

### 12.1 Identity Sources
- Local SMEsPlus identities (baseline).
- Optional external federation (SSO/IdP) — DECISION REQUIRED (see ARC-WP-006).

### 12.2 Authentication Model
Token-based (JWT) authentication at the API Gateway; short-lived access tokens plus refresh; MFA challenge configurable per tenant and mandatory for privileged roles.

### 12.3 Authorization Model
RBAC as the baseline (roles → permissions) augmented by ABAC attributes (tenant, company, branch, entitlement) for data-scope decisions. Deny-by-default.

### 12.4 RBAC and Permission Groups
Permissions grouped into roles; roles assigned per organizational scope. Standard roles: Tenant Admin, Company Admin, Branch User, Approver, Auditor (read-only), Platform Operator.

### 12.5 Data Scope
Every authorization decision combines role permission with the user's assigned tenant/company/branch scope (ARC-WP-002). No permission grants cross-tenant access.

### 12.6 Privileged Access and Service Accounts
Privileged/platform-operator access is time-bound, MFA-enforced and fully audited. Service accounts are non-interactive, least-privilege, scoped, with rotating credentials; no shared human/service credentials.

### 12.7 API Authentication and Sessions
API clients authenticate via tokens/keys scoped to tenant and entitlement; sessions have idle and absolute timeouts; token revocation on subscription/role change.

### 12.8 Joiner–Mover–Leaver Lifecycle
- Joiner: provisioned with scoped roles on activation.
- Mover: scope/role change triggers re-evaluation and token refresh.
- Leaver: immediate deactivation and session/token revocation; data retained per policy.

### 12.9 Access Review and SoD
Periodic access review (configurable cadence) with evidence; SoD rules (ARC-WP-004) prevent conflicting role combinations.

## 13. Architecture Decisions

- ADR-ARC-015 (RBAC+ABAC, deny-by-default, tenant-scoped): PROPOSED.
- ADR-ARC-013 (External identity federation): PROPOSED / DECISION REQUIRED.

## 14. Security Considerations

IAM is the primary access-control surface; MFA for privileged roles, deny-by-default, short-lived tokens and immediate leaver revocation are load-bearing. Cross-tenant escalation is a critical risk.

## 15. Privacy and Compliance Considerations

User identity data is personal data; access reviews and audit logs must themselves respect retention/minimization. Auditor role is read-only.

## 16. Tenant-Isolation Considerations

No role or token can widen scope beyond the assigned tenant; ABAC scope check is mandatory on every data access.

## 17. Recovery and Continuity Considerations

Identity service outage must fail closed (no access) not open; token validation must be restorable; break-glass privileged access is audited.

## 18. Observability Considerations

Authentication successes/failures, privileged actions, and scope-violation attempts are logged and alertable; anomalous access is detectable.

## 19. Capacity and Cost Considerations

Token validation and authorization checks are high-frequency; caching with correct invalidation on role/entitlement change controls cost/latency.

## 20. Risks and Gaps

- R-009-01: Cross-tenant privilege escalation via mis-scoped role. Severity: Critical.
- R-009-02: Stale token after leaver/role change. Severity: High. Mitigation: revocation on change.
- G-009-01: Federation/SSO decision open.

## 21. Measurable Acceptance Criteria

| AC ID | Criterion | Verification Method | Required Evidence |
|---|---|---|---|
| AC-001 | Auth model deny-by-default with tenant-scoped ABAC | Review | Sections 12.3/12.5 |
| AC-002 | Privileged access MFA-enforced and audited | Review | Section 12.6 |
| AC-003 | JML lifecycle defined incl. leaver revocation | Review | Section 12.8 |
| AC-004 | No role grants cross-tenant access | Review | Section 12.5 |

## 22. Evidence Requirements

| Evidence ID | Type | GitHub Location | Owner | Reviewer | Verification Status |
|---|---|---|---|---|---|
| EV-ARC-009 | IAM architecture | This file path | Identity Architecture AI Owner | ChatGPT L99 | NOT VERIFIED |

## 23. Open Decisions

- OD-009-01: External identity federation/SSO. DECISION REQUIRED.
- OD-009-02: Access-review cadence and MFA enforcement policy per tenant. DECISION REQUIRED.

## 24. Gate Impact

- Gate B automatic-HOLD condition "identity and access scope unclear" is addressed here. Contributes; does not pass.
- Recommendation: READY FOR INDEPENDENT REVIEW.

## 25. Change History

| Version | Date | Change | Author | Reviewer |
|---|---|---|---|---|
| 0.1 | 2026-07-14 | Initial draft | Identity Architecture AI Owner (Claude Code drafting agent) | Pending (ChatGPT L99) |

## 26. Approval Status

PREPARED FOR INDEPENDENT REVIEW / HOLD. Independent review and Boss decision remain mandatory.
