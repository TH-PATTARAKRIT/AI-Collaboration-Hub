# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# New Session Prompt — Inventory-side Multi-tenant Invariant Set / RISK-U03 / GAP-FS-10 / L9999.9999

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Jira: `ERPPLUS-139`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Prompt Branch: `prompt/inventory-multitenant-invariant-set-2026-09-04-001`  
Source Review Branch: `review/inventory-r4-aas-pmo-review-2026-09-04-001`  
Source Review Tip: `e218e5b550a2a8f839f295876f0a3ff1ce3e69d4`  
Execution Branch To Create: `design/inventory-multitenant-invariant-set-2026-09-04-001`  
Output Folder: `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/MULTI_TENANT_INVARIANT_SET_EXECUTION/`  
Control Level: `/L9999.9999`  
Model: `Claude Opus 5 high`  
Boss: `Sole Final Approver`  
Status: `AUTHORIZED FOR DESIGN / SPECIFICATION ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 0. Executor Instruction

You are Claude Opus 5 high executing a controlled SMEsPlus Inventory design/specification evidence session.

Create a fresh isolated execution branch:

`design/inventory-multitenant-invariant-set-2026-09-04-001`

Use the source review branch as read-only evidence:

`review/inventory-r4-aas-pmo-review-2026-09-04-001`

Do not merge to `SMEsPlus`. Do not edit prior R4 or AAS+ / PMO review evidence. Do not authorize development. Do not write application code. Do not create database migrations. Do not declare PASS.

Your job is to design and prove the Inventory-side multi-tenant invariant set required to unblock `RISK-U03` / `GAP-FS-10` at the design/specification layer only.

Stop at:

`READY FOR BOSS DECISION — INVENTORY MULTI-TENANT INVARIANT SET DESIGN ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Governing Standard

Apply:

`ALL MODULE DEEP RESEARCH STANDARD = L1-L12 MANDATORY FULL DEPTH + L13+ NO CEILING`

For this session, L1-L12 must be applied to the multi-tenant invariant problem, not to re-run all Inventory R4 research.

Use L13+ automatically if evidence shows additional complexity. Every L13+ extension must state:

- Trigger.
- Evidence.
- Why L1-L12 is insufficient.
- New level objective.
- Checkpoint.
- Impact on Boss decision.

---

## 2. Mandatory Sources To Read First

Read and cite all required sources before drawing conclusions:

| No. | Source | Required Use |
|---:|---|---|
| 1 | `21_BOSS_AUTHORIZATION_SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001.md` | Current Boss authorization |
| 2 | `12_BOSS_DECISION_PACKAGE.md` from R4 AAS+ / PMO review | Rank 1 basis and Boss decision list |
| 3 | `11_PMO_NEXT_CONTROLLED_ACTION_RECOMMENDATION.md` | PMO work order and sequencing |
| 4 | `10_AAS_PLUS_INDEPENDENT_REVIEW_VERDICT.md` | HOLD conditions and review findings |
| 5 | `05_92_OPEN_ITEMS_LANE_SPLIT_REGISTER.md` | Blocker lane split and item ownership |
| 6 | `04_R4_F16_STRUCTURAL_BLOCKER_REVIEW.md` | Independent re-derivation of `R4-F-16` |
| 7 | `09_JOINT_DECISION_READINESS_MATRIX.md` | Why 0 of 22 scenarios remain unprovable |
| 8 | `13_SESSION_CLOSURE.md` | Publication record and terminal status |
| 9 | R4 source file `16_INVENTORY_ACCOUNTING_HANDOFF_CONTRACT_GAP_ANALYSIS.md` | Original handoff-element mapping |
| 10 | R4 source file `11_L10_L11_MIGRATION_AND_RECONCILIATION_PROOF.md` | Migration and reconciliation dependency context |
| 11 | R4 source file `09_L9_SAAS_MULTI_TENANT_MULTI_COMPANY_PROOF.md` | Original L9 proof failures |

If any source is missing, record `EVIDENCE GAP` and continue only where evidence remains sufficient.

---

## 3. Strict Scope

### In scope

Define the Inventory-side invariant set for:

1. Tenant isolation.
2. Company isolation.
3. Warehouse isolation.
4. Location isolation.
5. Product and product variant visibility.
6. Lot and serial traceability.
7. Package and packaging isolation.
8. Route and rule ownership.
9. Operation type ownership.
10. Stock move and transfer ownership.
11. Replenishment and scheduler execution boundary.
12. Inventory adjustment, scrap, return, and landed-cost context boundary.
13. Stock report and valuation report context boundary.
14. Event, audit trail, and immutable identity requirements.
15. Cross-module handoff contract fields needed by Accounting, Purchase, Sale, Manufacturing, Approval, Document, and Reporting.

### Out of scope

Do not decide or implement:

- COGS policy.
- Period-close policy.
- Valuation posting policy.
- Landed-cost accounting posting.
- Return cost basis.
- Thai statutory position.
- Source code.
- Database schema.
- API implementation.
- UI implementation.
- Team B or Team C work.
- Production or release.

Valuation-related content must remain marked:

`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`

---

## 4. Required L1-L12 Treatment

| Level | Required Treatment For This Session |
|---:|---|
| L1 | Define the business meaning of Inventory multi-tenant invariants in SMEsPlus |
| L2 | Identify UI, field, configuration, and context surfaces that must carry tenant/company/warehouse/location boundaries |
| L3 | Identify function-level enforcement points across stock operations and reports |
| L4 | Map dependencies to Accounting, Sale, Purchase, Manufacturing, Approval, Document, and Reporting |
| L5 | Define whole-system semantic rules: ownership, visibility, execution, reporting, and audit meaning |
| L6 | Attack contradictions, failures, edge cases, and cross-company leakage scenarios |
| L7 | Define Inventory control and internal-control obligations, including segregation and approval boundaries |
| L8 | Define identity, immutability, replay, event, and lineage requirements |
| L9 | Produce SaaS / multi-tenant / multi-company invariant set and proof matrix |
| L10 | Define migration, opening, historical continuity, and replay constraints related to tenant/company identity |
| L11 | Define reconciliation and end-to-end proof requirements for reports and handoffs |
| L12 | Perform adversarial audit challenge and veto: prove what still fails and why |

---

## 5. Required Deliverables

Create exactly these files in the output folder:

| No. | File | Purpose |
|---:|---|---|
| 00 | `00_EXECUTION_CHECKPOINT_LOG.md` | Step-by-step checkpoint trail |
| 01 | `01_EVIDENCE_INTAKE_AND_SOURCE_VERIFICATION.md` | Source verification and lineage |
| 02 | `02_RISK_U03_GAP_FS10_PROBLEM_STATEMENT.md` | Problem definition and evidence boundary |
| 03 | `03_INVENTORY_MULTI_TENANT_INVARIANT_SET.md` | Canonical invariant set |
| 04 | `04_CONTEXT_OWNERSHIP_AND_VISIBILITY_MATRIX.md` | Tenant/company/warehouse/location/product visibility matrix |
| 05 | `05_FUNCTION_ENFORCEMENT_POINT_MATRIX.md` | Function-by-function enforcement points |
| 06 | `06_CROSS_MODULE_HANDOFF_CONTRACT_FIELDS.md` | Handoff field contract and ownership |
| 07 | `07_L9_ISOLATION_PROOF_MATRIX.md` | L9 proof scenarios and acceptance criteria |
| 08 | `08_FAILURE_EDGE_CASE_AND_LEAKAGE_ATTACK_REGISTER.md` | L6/L12 adversarial failure analysis |
| 09 | `09_DATA_IDENTITY_IMMUTABILITY_AND_REPLAY_REQUIREMENTS.md` | L8/L10 requirements |
| 10 | `10_REPORTING_AND_RECONCILIATION_PROOF_REQUIREMENTS.md` | L11 reporting proof requirements |
| 11 | `11_OPEN_ITEMS_AND_DEPENDENCY_REGISTER.md` | Open items, owner, lane, blocker status |
| 12 | `12_AAS_PLUS_CHALLENGE_VERDICT.md` | AAS+ adversarial verdict |
| 13 | `13_PMO_NEXT_GATE_RECOMMENDATION.md` | PMO recommendation and next controlled action |
| 14 | `14_BOSS_DECISION_PACKAGE.md` | Boss decision package |
| 15 | `15_SESSION_CLOSURE.md` | Publication record and final status |
| 16 | `16_SHA256_MANIFEST.md` | SHA-256 manifest for all output files |

---

## 6. Acceptance Criteria

The session is acceptable only if it includes:

1. A canonical invariant list with stable IDs.
2. Explicit ownership of every invariant.
3. A context matrix covering tenant, company, warehouse, location, product, lot/serial, package, route, rule, operation type, move, transfer, adjustment, scrap, replenishment, scheduler, and reporting.
4. A proof matrix showing which of the previous 0/8 L9 proofs become structurally provable at the design level, and which remain blocked.
5. A cross-proof impact statement for the 22 Boss-approved scenarios.
6. A list of remaining blockers, with lane, owner, and evidence need.
7. Clear distinction between design/specification readiness and development readiness.
8. Clean-room compliance statement using reference-system language only.
9. No code, schema, migration, API, or implementation output.
10. Boss decision package and SHA-256 manifest.

---

## 7. Prohibited Declarations

Do not declare or imply:

- `PASS`
- `APPROVED`
- `CLOSED`
- `FINAL SOLUTION ACCEPTED`
- `READY FOR DEVELOPMENT`
- `READY FOR PRODUCTION`
- `TEAM B AUTHORIZED`
- `TEAM C AUTHORIZED`
- `MERGE APPROVED`
- `RELEASE AUTHORIZED`

Allowed final status is only:

`READY FOR BOSS DECISION — INVENTORY MULTI-TENANT INVARIANT SET DESIGN ONLY — NOT DEVELOPMENT FINAL GATE`

or a specific `HOLD` status backed by evidence.

---

## 8. Publication Requirement

Commit and push the execution branch. Record:

- Repository.
- Branch.
- Output folder.
- File list.
- Publication commit SHA.
- Direct GitHub links.
- SHA-256 manifest.

Do not close the session until all links and commit references resolve.

---

`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`
