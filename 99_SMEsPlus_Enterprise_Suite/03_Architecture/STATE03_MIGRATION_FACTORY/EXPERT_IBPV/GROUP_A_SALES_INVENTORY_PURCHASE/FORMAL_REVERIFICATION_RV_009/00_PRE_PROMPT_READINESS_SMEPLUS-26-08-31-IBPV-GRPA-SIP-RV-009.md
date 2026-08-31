# [SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009]
# GROUP A — Formal IBPV Re-Verification Pre-Prompt Five-Unit Challenge & Readiness / L999.999

Project: SMEsPlus ENTERPRISE SUITE  
STATE: STATE03 — Architecture  
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone  
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team  
Lifecycle Stage: Formal re-verification after TEAM B CORR-008  
Boss: Sole Final Approver  
Risk Class: HIGH  
Canonical Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Canonical Baseline at Challenge Start: `89ad2244e10264c6bde0588c4a05d91ea10de373`  
Original TEAM B Design Commit: `b98a3b9fb435845dbd15fae79db63b0b73a82420`  
Prior Formal IBPV Commit: `535724c0a2a5d0a972713f513dc567d8b27fc89b`  
Corrected TEAM B CORR-008 Commit: `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`  
Dedicated Re-Verification Branch: `ibpv/group-a-sip-formal-reverification-009`

## 1. Boss Authorization

Boss authorizes Formal IBPV Re-Verification of the corrected TEAM B GROUP A package after CORR-008.

This authorization means:

- EXPERT IBPV may independently re-perform the nine CORR-008 closure claims;
- EXPERT IBPV may reassess the Pre-Development Blocking Rule against the corrected package;
- EXPERT IBPV may create and push verification evidence to the dedicated IBPV branch;
- the session must continue autonomously until a terminal recommendation or true stop condition.

This authorization does **not** mean:

- TEAM B is Final;
- CORR-008 is automatically accepted;
- Pre-Development Gate is automatically PASS;
- Team C is authorized;
- any unresolved Boss-policy or external-domain item is silently waived.

## 2. Five-Unit Pre-Prompt Challenge

### 2.1 Audit VETO — Evidence / Governance Challenge

Status: **NO VETO — PROCEED WITH INDEPENDENT RE-VERIFICATION**

Mandatory controls:

1. Freeze `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45` as the corrected TEAM B input.
2. Do not accept TEAM B files 22–28 as proof merely because they say `CLOSED`; reproduce each original FV-006 finding and inspect the corrected design sections independently.
3. Re-perform SHA-256/manifest integrity for the corrected package and verify branch ancestry from the frozen TEAM B baseline.
4. Verify the claimed 13 corrected baseline files and 7 new corrective deliverables; no TEAM A or prior IBPV artifact may have been modified by TEAM B.
5. Do not edit TEAM B design artifacts during re-verification. Findings must be reported, not repaired by IBPV.
6. Reassess package-wide consistency and regressions, not only the nine rows in TEAM B's closure register.
7. Re-open the prior Pre-Development Gate recommendation and explicitly dispose every previously blocking or held item; no silent drop.
8. No Team C, code, merge, release or production action.

### 2.2 TBRAC — Thailand Reality Challenge

Status: **PROCEED — STRICT EVIDENCE CLASSIFICATION REQUIRED**

Challenge questions:

- Did any CORR-008 correction convert generic SaaS, approval, retry, archival or warehouse semantics into a Thailand-wide claim without evidence?
- Did SaaS/Tenant reconciliation import Domain-01 Accounting/Tax-Branch-specific rules into GROUP A without evidence?
- Are real-user-validation items still explicitly classified and carried forward where appropriate?

Mandatory rule: `Reference behavior ≠ Customer practice ≠ Thailand reality ≠ SMEsPlus target requirement.`

### 2.3 EXPERT IBPV — Formal Verification Challenge

Status: **FORMAL LIFECYCLE STAGE REACHED — PROCEED**

Formal re-verification must independently answer, for all nine CORR-008 findings:

1. Is the original FV-006 concern reproducible?
2. Does the cited corrected design actually close it?
3. Are state/event/owner/handoff/audit semantics complete where applicable?
4. Did the correction create any new conflict or hidden dependency?
5. Is the closure traceable and future-verifiable?

Special scrutiny:

- denied-approval state/event/downstream wind-down;
- retry/idempotency business invariant;
- failed hard-handoff reconciliation/convergence;
- sequential-approval wording vs unverified legacy enforcement;
- identity-based self-approval prevention;
- event transport/ordering/consumer-failure semantics;
- lot/serial/package ownership and lifecycle;
- shared-master archival/history preservation;
- SaaS/Tenant baseline traceability and classification.

IBPV must also reassess residual items that CORR-008 did not purport to close, including the Sales/Purchase cancellation-gate Accounting dependency, missing legacy approval internal-logic evidence, the three deferred policy defaults, and any race-condition finding that remained open after CORR-008.

### 2.4 EXPERT IDTM — Future Testability Challenge

Status: **PROCEED — ADVISORY ONLY**

Re-verification should challenge whether corrected semantics are testable later without dictating implementation:

- duplicate Confirm / Movement Execution must have observable pass/fail truth;
- event ordering and duplicate/replay semantics must be precise enough for concurrency tests;
- failure compensation must have explicit convergence truth;
- denied approval must have an observable terminal/control outcome;
- tenant/company isolation claims must be distinguishable between design invariant and runtime proof;
- archival and ownership rules must produce exact invariants for future tests.

No Formal IDTM test matrix is created in this session.

### 2.5 EXPERT IESA — ERP & SaaS System-Level Challenge

Status: **PROCEED — SYSTEM-INTEGRITY LENS ONLY**

Re-verification must look for systemic consequences of local corrections:

- orphan demand after rejected approval;
- duplicated commercial/physical effects on retry;
- unresolved cross-domain commits;
- approval/SoD audit weakness;
- cross-tenant or cross-company leakage;
- broken historical traceability from hard deletion;
- local rules that improperly reach into Accounting Core authority.

IESA is advisory only; Formal IESA is not active.

## 3. Consolidated Challenge Result

| Unit | Result |
|---|---|
| Audit VETO | NO VETO — independent re-performance required |
| TBRAC | PROCEED — preserve evidence/Thailand classification |
| IBPV | PROCEED — formal re-verification lifecycle stage reached |
| IDTM | PROCEED — future-testability advisory only |
| IESA | PROCEED — system-integrity advisory only |

## 4. SaaS / Tenant Ruling for Re-Verification

The re-verification must **not** ask whether SMEsPlus should be Multi-Tenant. That principle is already controlled at project level.

For GROUP A, IBPV must verify whether CORR-008 correctly separates:

1. `EXISTING BOSS-CONTROLLED SAAS INVARIANT` — Tenant context mandatory; Company context mandatory where company-scoped;
2. `EVIDENCE-SUPPORTED GROUP A DESIGN ELABORATION`;
3. `TEAM B CANONICAL DESIGN CHOICE WITH EXPLICIT RATIONALE`;
4. `CONTROLLED ASSUMPTION / REQUIRES FUTURE VERIFICATION`;
5. any genuinely unresolved structural decision.

A missing prior structural blueprint is not, by itself, authority to re-open the already-approved Multi-Tenant mandate. Conversely, TEAM B may not disguise a new structural choice as if Boss had already approved that exact shape.

## 5. Prompt Readiness Decision

```text
Target: Formal IBPV Re-Verification of TEAM B CORR-008 corrected GROUP A design
Risk: HIGH
Five-Unit Challenge: COMPLETE
Critical Blocking Unknown Before Start: NONE
Corrected Input: 359f96c0cfee2f74955fe7e8f1d0110ec21a0a45
Independent Reviewer: EXPERT IBPV
Reviewer Branch: ibpv/group-a-sip-formal-reverification-009
Team B Editing During Review: PROHIBITED
TEAM C / Development: NOT AUTHORIZED
Formal IDTM: NOT ACTIVE
Formal IESA: NOT ACTIVE
Readiness: READY
```

## 6. Required Terminal Boundary

The re-verification may conclude only with an evidence-based recommendation such as:

- `FORMAL IBPV RE-VERIFICATION COMPLETE — READY FOR BOSS PRE-DEVELOPMENT GATE DECISION`
- `FORMAL IBPV RE-VERIFICATION COMPLETE — REWORK REQUIRED / NOT READY FOR DEVELOPMENT`
- `EVIDENCE MISSING / NOT READY FOR DEVELOPMENT`

It may not declare `BOSS APPROVED`, `FINAL APPROVED`, `TEAM C AUTHORIZED`, `DEVELOPMENT READY`, `RELEASE APPROVED`, or `PRODUCTION READY`.

`Ask until materially clear — not until everyone agrees.`  
`Independent experts verify the design; only Boss decides whether the lifecycle may advance.`