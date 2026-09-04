# ACCOUNT WAVE A — CORE LEDGER & CLOSING — Research Package Index

Session: `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`
Program: `[SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001] Accounting Domain Full-Spectrum Deep Research Program`
Wave: `WAVE A — CORE LEDGER & CLOSING`
Branch: `research/account-wave-a-core-2026-09-04-001`
Base commit: `8d2c8aa`
Date: 2026-09-04
Terminal state: see `26_ACCOUNT_WAVE_A_FINAL_RESEARCH_GATE_REPORT.md`

## Layering

| Layer | Content | Audience |
|---|---|---|
| **Layer 2 — audit quarantine** | `LAYER2_EVIDENCE_QUARANTINE/`, `EXPERT_REVIEW/`, `CHALLENGE/` — carry `file:line -- method` citations into a reference ERP source tree | Boss / PMO / AI-Audit only. Must not be transcribed into any downstream reference or design package. |
| **Layer 1 — clean room** | everything else in this folder — business semantics, control intent, decisions, expressed in neutral vocabulary and citing `EV-0NN` identifiers rather than source locations | May inform Team B design input after Boss gate |

Every `EV-0NN` reference in a Layer 1 file resolves to an entry in
`LAYER2_EVIDENCE_QUARANTINE/E00_PRIMARY_EVIDENCE_BASE.md`.

## Contents

| # | File | Level / Register |
|---|---|---|
| 00 | `00_README_PACKAGE_INDEX.md` | this index |
| E0 | `LAYER2_EVIDENCE_QUARANTINE/E00_PRIMARY_EVIDENCE_BASE.md` | primary evidence, EV-001..EV-023 |
| 01 | `01_L1_DOMAIN_SEMANTIC_MAP.md` | Level 1 |
| 02 | `02_ACCOUNT_WAVE_A_FUNCTION_COVERAGE_REGISTER.md` | Register 1 |
| 03 | `03_ACCOUNT_WAVE_A_UI_FIELD_SEMANTIC_REGISTER.md` | Level 2 / Register 2 |
| 04 | `04_L3_FUNCTION_FORENSIC_REGISTER.md` | Level 3 |
| 05 | `05_ACCOUNT_WAVE_A_CROSS_MODULE_DEPENDENCY_MAP.md` | Level 4 / Register 5 |
| 06 | `06_L5_WHOLE_SYSTEM_ACCOUNTING_SEMANTIC_MODEL.md` | Level 5 |
| 07 | `07_ACCOUNT_WAVE_A_ACCOUNTING_EVENT_REGISTER.md` | Register 6 |
| 08 | `08_ACCOUNT_WAVE_A_EVENT_TO_GL_MATRIX.md` | Register 3 |
| 09 | `09_ACCOUNT_WAVE_A_SOURCE_OF_TRUTH_REGISTER.md` | Register 4 |
| 10 | `10_ACCOUNT_WAVE_A_STATE_TRANSITION_REGISTER.md` | Register 7 |
| 11 | `11_ACCOUNT_WAVE_A_RECONCILIATION_MATRIX.md` | Register 8 |
| 12 | `12_ACCOUNT_WAVE_A_PERIOD_CLOSE_MATRIX.md` | Register 9 |
| 13 | `13_ACCOUNT_WAVE_A_CURRENCY_AND_FX_MATRIX.md` | Register 10 |
| 14 | `14_L7_ACCOUNT_WAVE_A_CONTROL_MATRIX.md` | Level 7 / Register 11 |
| 15 | `15_L8_ACCOUNT_WAVE_A_IDENTITY_IMMUTABILITY_REGISTER.md` | Level 8 / Register 12 |
| 16 | `16_L9_ACCOUNT_WAVE_A_SAAS_BOUNDARY_REGISTER.md` | Level 9 / Register 13 |
| 17 | `17_L10_ACCOUNT_WAVE_A_MIGRATION_SEMANTIC_REQUIREMENTS.md` | Level 10 |
| 18 | `18_L11_CORE_LEDGER_RECONCILIATION_PROOF_MATRIX.md` | Level 11 |
| 19 | `19_L6_ACCOUNT_WAVE_A_FAILURE_EDGE_CASE_REGISTER.md` | Level 6 / Register 14 |
| 20 | `20_ACCOUNT_WAVE_A_CONTRADICTION_REGISTER.md` | Register 16 |
| 21 | `21_ACCOUNT_WAVE_A_UNKNOWN_EVIDENCE_GAP_REGISTER.md` | Register 15 |
| 22 | `22_ACCOUNT_WAVE_A_SEMANTIC_TRANSFER_REGISTER.md` | Register 19 |
| 23 | `23_ACCOUNT_WAVE_A_EXPERT_REVIEW_REGISTER.md` | Register 17 |
| 24 | `24_ACCOUNT_WAVE_A_AUDIT_VETO_REGISTER.md` | Register 18 / Level 12 |
| 25 | `25_ACCOUNT_WAVE_A_CHECKPOINT_LINEAGE.md` | Checkpoint protocol record |
| 26 | `26_ACCOUNT_WAVE_A_FINAL_RESEARCH_GATE_REPORT.md` | Register 20 — Final Gate package |
| X | `EXPERT_REVIEW/` | AAS-03 four independent expert reviews — **Layer 2** |
| C | `CHALLENGE/` | independent adversarial challenge register — **Layer 2** |

## Governing rules applied

- `No Evidence = No Progress` — every material conclusion carries an `EV-0NN` reference or is marked `UNKNOWN — EVIDENCE REQUIRED`.
- `Never Skip Gate` — Levels 1 through 12 executed; checkpoints recorded in file 25.
- Evidence classes are never merged: `VERIFIED FACT`, `REFERENCE BEHAVIOUR`, `INFERENCE`, `RECOMMENDATION`, `UNKNOWN — EVIDENCE REQUIRED`.
- Reference implementation is a **benchmark, not an authority**. Nothing is adopted because the reference does it.
- Thai statutory positions are `HOLD / EVIDENCE REQUIRED` and routed to the Accounting-Tax track. Thai names are candidate / UNVALIDATED.
- This package makes **no approval, no gate movement, and no implementation authorisation**. Boss is the sole Final Approver.

---

## CORR1 — Evidence Reconciliation & Negative-Claim Rescoping (2026-09-04)

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`, branch
`research/account-wave-a-corr1-2026-09-04-001`, parent commit `f8bc069`.

**CORR1 is the governing layer.** Where a numbered file above conflicts with a CORR1 file, the CORR1
file governs. Numbered files are retained unedited for lineage and carry a correction banner.

| File | Content | Layer |
|---|---|---|
| `CORR1/C01_ACCOUNT_WAVE_A_CORR1_MASTER_RECONCILIATION.md` | master reconciliation and lineage | 1 |
| `CORR1/C02_ACCOUNT_WAVE_A_ACCEPTED_CORRECTIONS_REGISTER.md` | all 20 accepted corrections, reconciled into the artefacts | 1 |
| `CORR1/C03_ACCOUNT_WAVE_A_CONTRADICTED_CLAIMS_REGISTER.md` | the 6 contradicted claims, re-examined | 1 |
| `CORR1/C04_ACCOUNT_WAVE_A_NEGATIVE_CLAIM_SCOPE_REGISTER.md` | negative-claim rescoping, classes A–E | 1 |
| `CORR1/C05_ACCOUNT_WAVE_A_SEVERE_FINDINGS_REGISTER.md` | the 5 severe findings, independently reconciled | 1 |
| `CORR1/C06_ACCOUNT_WAVE_A_FX_MISSING_RATE_FORENSIC.md` | missing-rate forensic | **2** |
| `CORR1/C07_ACCOUNT_WAVE_A_DATE_SEMANTIC_MATRIX.md` | date semantics, 7 concepts | **2** |
| `CORR1/C08_ACCOUNT_WAVE_A_L11_RECONCILIATION_RERUN.md` | L11 re-run + BALANCED BUT WRONG register — **supersedes file 18** | 1 |
| `CORR1/C09_ACCOUNT_WAVE_A_CONTROL_SUPPRESSION_REACHABILITY.md` | `GAP-C04` closed | **2** |
| `CORR1/C10_ACCOUNT_WAVE_A_CORR1_GATE_REPORT.md` | CORR1 gate report — **supersedes file 26** | 1 |
| `CORR1/L12_FRESH_REVIEW/` | fresh independent adversarial review, two reviewers | **2** |
| `99_SMEsPlus_Enterprise_Suite/00_PROJECT_STANDARD/SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD.md` | project-wide negative-claim control standard | 1 |

### New governing rule issued by CORR1

> `NO EVIDENCE FOUND ≠ FUNCTION DOES NOT EXIST`

Absence of evidence within a searched scope shall not be reported as absence of behaviour across the
whole system. Every material negative claim declares its search boundary and carries a class
(`A` verified absence within scope · `B` not found in searched scope · `C` not yet searched ·
`D` unknown · `E` contradicted). B, C and D are never converted to A.
