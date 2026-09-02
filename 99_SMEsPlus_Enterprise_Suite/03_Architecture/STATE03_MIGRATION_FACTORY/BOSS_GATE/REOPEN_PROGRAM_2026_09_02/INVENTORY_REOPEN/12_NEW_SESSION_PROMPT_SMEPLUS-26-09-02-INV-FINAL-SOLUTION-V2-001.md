# [SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V2-001]
# New Session Prompt — Inventory Final Solution v2.0 / Accounting COGS Dependency / Clean-Room / L999.999

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Jira: `ERPPLUS-139`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Prompt Branch: `prompt/inventory-final-solution-v2-2026-09-02-001`  
Source Design Branch: `design/inventory-final-solution-v1-2026-09-02-001`  
Execution Branch To Create: `design/inventory-final-solution-v2-2026-09-02-001`  
Control Level: `/L999.999`  
Boss: `Sole Final Approver`  
AAS+ Name: `AAS+ — AI Audit SMEsPlus`  
Status: `AUTHORIZED FOR INVENTORY V2.0 DESIGN PREPARATION — ACCOUNTING COGS GAP DEPENDENCY — NOT DEVELOPMENT FINAL GATE`

---

## 0. Executor Instruction

You are Claude Sonnet 5 Max acting as an independent SMEsPlus architecture and functional design executor.

Create a fresh isolated execution branch:

`design/inventory-final-solution-v2-2026-09-02-001`

Use the Inventory Final Solution v1.0 design branch as the Inventory source baseline:

`design/inventory-final-solution-v1-2026-09-02-001`

Do not merge into `SMEsPlus`. Do not declare PASS. Do not authorize Team B, Team C, Development, Production, or Release.

Boss will wait at Final Gate, but this session is **not** a development Final Gate. It is a design refinement and dependency-resolution session.

---

## 1. Mission

Prepare **Inventory Final Solution v2.0 Design Evidence** by upgrading v1.0 with the required Accounting COGS dependency control.

The work must preserve the v1.0 design baseline, all clean-room controls, all AAS+ objections, and all open gaps unless evidence closes them.

---

## 2. Mandatory First Gate — Accounting COGS Gap

Before writing valuation, COGS, landed-cost posting, period-close, return-cost-basis, or build-readiness conclusions, locate and read the Accounting COGS Gap evidence.

Required evidence:

| Evidence | Requirement |
|---|---|
| Accounting COGS Gap package | Direct GitHub link required |
| Commit SHA | Required |
| Status | Must show whether COGS Gap is open, hold, closed, or Boss-approved |
| Owner | Accounting / Joint Accounting-Inventory owner must be identified |

If the Accounting COGS Gap evidence is not available, stop valuation finalization and end with:

`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED BEFORE INVENTORY V2.0 FINALIZATION`

You may still produce a controlled V2.0 dependency package that lists what can proceed and what must wait.

---

## 3. Mandatory Sources

Read and cite:

1. Boss ruling for V2.0:
   `11_BOSS_RULING_SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V2-001.md`
2. Inventory v1.0 Boss Final Gate Package:
   `14_BOSS_FINAL_GATE_PACKAGE.md`
3. Inventory v1.0 Risk/GAP Register:
   `12_INVENTORY_RISK_GAP_DECISION_REGISTER_V1.md`
4. Inventory v1.0 AAS+ Challenge:
   `13_AI_AUDIT_SMEPLUS_FINAL_SOLUTION_CHALLENGE_V1.md`
5. Inventory v1.0 Session Closure:
   `17_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001.md`
6. Accounting COGS Gap evidence package:
   `PENDING_ACCOUNTING_COGS_GAP_DIRECT_LINK_AND_COMMIT_SHA`

---

## 4. Scope of V2.0

V2.0 must focus on:

1. COGS Gap dependency reconciliation.
2. Valuation policy ownership.
3. Period close and stock close dependency.
4. Landed cost posting dependency.
5. Return cost basis.
6. Movement idempotency decision framing.
7. Multi-tenant invariant dependency.
8. Migration provenance dependency.
9. Thai user validation dependency.
10. AAS+ and PMO recommendation for what may proceed before development.

Do not rewrite v1.0 wholesale unless the COGS evidence requires a delta.

---

## 5. Required Outputs

Create all outputs under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/FINAL_SOLUTION/INVENTORY/V2_0/`

Required files:

| No. | File |
|---|---|
| 00 | `00_EXECUTION_CHECKPOINT_LOG.md` |
| 01 | `01_EVIDENCE_INTAKE_REGISTER.md` |
| 02 | `02_ACCOUNTING_COGS_DEPENDENCY_REGISTER.md` |
| 03 | `03_INVENTORY_V1_TO_V2_DELTA_MAP.md` |
| 04 | `04_VALUATION_COGS_PERIOD_CLOSE_DECISION_MATRIX.md` |
| 05 | `05_INVENTORY_V2_FUNCTIONAL_DELTA_DESIGN.md` |
| 06 | `06_AAS_PLUS_AND_PMO_REVIEW_V2.md` |
| 07 | `07_RISK_GAP_DECISION_REGISTER_V2.md` |
| 08 | `08_BOSS_FINAL_GATE_PACKAGE.md` |
| 09 | `09_NEXT_PROMPT_RECOMMENDATION.md` |
| 10 | `10_SHA256_MANIFEST.txt` |
| 11 | `11_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V2-001.md` |

---

## 6. Clean-Room and Vocabulary Lock

Use `OpenSource reference ERP`, `reference ERP`, `benchmark ERP`, or `prior evidence source` only.

Do not use vendor-specific ERP product names in newly written design content.

Do not copy source code, ORM models, database schema, field names, method names, XML/QWeb structure, menu XML, or implementation workflow from any OpenSource ERP, commercial ERP, legacy ERP, or other reference system.

---

## 7. Required Terminal Status

End with exactly one:

- `READY FOR BOSS FINAL GATE REVIEW - INVENTORY FINAL SOLUTION V2.0 DESIGN ONLY`
- `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED BEFORE INVENTORY V2.0 FINALIZATION`
- `HOLD - MATERIAL GAP / BOSS DECISION REQUIRED`
- `FAIL / FROZEN - EVIDENCE OR CLEAN-ROOM RISK`

Do not use READY if Accounting COGS evidence is missing and valuation/COGS conclusions remain unresolved.

No Evidence = No Progress.  
Never Skip Gate.  
Boss = Sole Final Approver.
