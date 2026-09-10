# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E0 — Baseline & Empirical HOLD Register

Status: E0 EVIDENCE
Jira: ERPPLUS-156
Parent: ERPPLUS-152 / [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
Final Approver: Boss only
Build / Merge / Deployment / Production: HOLD

## 1. Verified Boss-Approved Entrance Baseline

Boss approval evidence:
- `CORE_RESOURCE_GOVERNANCE/61_G11_BOSS_FINAL_APPROVAL_AND_SESSION_CLOSURE.md`
- Approval scope: conceptual Core Resource Governance architecture only.

Approved STANDARD direction:
`Bounded multi-tenant Cells + evidence-based placement + targeted isolated execution lanes for selected heavy workloads where required`.

Approved ENTERPRISE direction:
`Dedicated full-Tenant resource/isolation boundary using the same Core product semantics`.

Mandatory separation:
`PACKAGE != TENANT != CAPACITY ENTITLEMENT != CELL != SERVER != DATABASE HOST`.

Canonical organization hierarchy:
`PLATFORM -> TENANT -> ORGANIZATION ROOT / GROUP -> COMPANY -> BRANCH`.

## 2. Current Product Identity Reconciliation

Current September architecture evidence repeatedly identifies SMEsPlus as a NEW clean-room Node.js SaaS ERP, including:
- `00_Project_Governance/CORE_TEAM/PRINCIPAL_ENTERPRISE_ERP_SAAS_ADVISOR_AND_CAPABILITY_UPLIFT_2026_09_06.md`;
- `SAAS_CELL_ARCHITECTURE/01_NEW_SESSION_PROMPT_SMEPLUS-26-09-06-SAAS-CELL-001.md`;
- `SAAS_CELL_ARCHITECTURE/02_SESSION_CONTINUITY_REGISTER_SMEPLUS-26-09-06-SAAS-CELL-001.md`.

A July technology-stack document (`00_PROJECT_STANDARD/TECHNOLOGY_STACK_STANDARD.md`, Version 1.0, Last Updated 2026-07-06) still states FastAPI/Python as backend and therefore conflicts with the current September Node.js product identity.

E0 disposition:
- current Node.js clean-room product identity = `CURRENT ARCHITECTURE BASELINE`;
- July FastAPI/Python backend entries = `STALE / CONFLICTING EXECUTION BASELINE — DO NOT USE FOR EMPIRICAL RUNTIME CLAIMS WITHOUT FORMAL RECONCILIATION`;
- other tool entries from that file may be evaluated individually as candidate tools, not silently inherited as runtime truth.

No E0 experiment may benchmark a stale backend stack and present the result as SMEsPlus capacity evidence.

## 3. Empirical HOLD Register

The following remain HOLD exactly as carried from G11:

| ID | Item | State | Promotion requirement |
|---|---|---|---|
| EH-01 | Tenant count per Cell | EMPIRICAL HOLD | representative sustainable Cell load evidence |
| EH-02 | CPU/RAM limits | EMPIRICAL HOLD | production-intent workload + fairness + failure evidence |
| EH-03 | DB connection/query limits | EMPIRICAL HOLD | DB contention/latency/lock evidence |
| EH-04 | Worker/Queue limits | EMPIRICAL HOLD | queue wait/depth/fairness/recovery evidence |
| EH-05 | DB/File/Archive quotas | EMPIRICAL HOLD | logical usage + physical amplification + CTS evidence |
| EH-06 | Placement/admission thresholds | EMPIRICAL HOLD | multidimensional headroom + stale telemetry + failure tests |
| EH-07 | Protected Mode thresholds/actions | EMPIRICAL/POLICY HOLD | safety tests + ERP integrity + Commercial/UX/Legal validation |
| EH-08 | Package prices/rates/weights | COMMERCIAL HOLD | actual CTS + commercial/tax validation + Boss decision |
| EH-09 | Target margin | COMMERCIAL HOLD | actual CTS + commercial model + Boss decision |
| EH-10 | RPO/RTO values | EMPIRICAL HOLD | repeated recovery drills target-vs-achieved |
| EH-11 | Mixed-package vs package-class Cell winner | EMPIRICAL HOLD | predeclared A/B evidence |
| EH-12 | Scale-up vs scale-out trigger | EMPIRICAL HOLD | comparative CTS/performance/recovery evidence |
| EH-13 | Standard->Enterprise crossover | EMPIRICAL HOLD | sustained workload + CTS + recovery/isolation evidence |
| EH-14 | Exact DB tenancy topology | IMPLEMENTATION HOLD | security/performance/ops/recovery proof + Architecture Review |
| EH-15 | Container/Kubernetes/VM/cgroup mechanism | IMPLEMENTATION HOLD | mechanism-specific proof + Architecture Review |
| EH-16 | Object storage/provider | IMPLEMENTATION HOLD | isolation/performance/recovery/cost proof |
| EH-17 | Backup/KMS/replication mechanism | IMPLEMENTATION HOLD | recovery/security/cost proof |
| EH-18 | Wallet statutory Accounting/VAT/revenue treatment | ACCOUNTING/COMMERCIAL HOLD | Accounting + Commercial controlled handoff |

`No measured evidence = no numerical freeze.`

## 4. Non-Reopen Rule

The empirical program does not reopen the Boss-approved conceptual architecture merely because a number or mechanism is still unknown.

Controlled Re-entry is required only when empirical evidence materially contradicts a conceptual invariant or makes the approved architecture unsafe/unviable for the affected scope.

## 5. E0 Baseline Disposition

`BASELINE RECONCILED WITH ONE MATERIAL DOCUMENT-CONFLICT CONTROLLED: JULY PYTHON/FASTAPI STACK MUST NOT BE USED AS CURRENT RUNTIME TRUTH.`

All numerical/mechanism/commercial HOLDs remain visible and owned by the follow-on evidence program.