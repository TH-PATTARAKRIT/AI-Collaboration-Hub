# [SMEPLUS-26-09-02-INV-CLEANROOM-REAUDIT-001]
# Inventory Independent Clean-Room Re-Audit for C-05 + Menu Reference Package / Claude Sonnet 5 Max / L999.999

## SINGLE END-TO-END NEW SESSION PROMPT

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 - Architecture`  
Domain: `INVENTORY / Clean-room / IP Provenance / Evidence Safety / Team B-C Precondition`  
Jira: `ERPPLUS-139`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Target Executor: `Claude Sonnet 5 Max`  
Execution Mode: `READ ONLY / INDEPENDENT RE-AUDIT / CLEAN-ROOM / EVIDENCE-FIRST / NO-DESIGN / CHECKPOINT-CONTROLLED / L999.999`  
Boss: `Sole Final Approver at Final Gate`

This session is created after Boss instructed PMO to proceed from the Inventory Menu-by-Menu Deep Challenge result.

This session is **not** a Final Solution for SMEsPlus.  
This session is **not** a development authorization.  
This session is **not** a Gate PASS.  
This session is **not** Team B, Team C or Development authorization.  
This session is an independent clean-room re-audit to determine whether the current Inventory evidence/reference package is safe enough for future controlled reliance.

---

## 1. Mission

Perform an independent Clean-Room Re-Audit of:

1. CORR-007B `N-A12-01` clean-room remediation, especially old files `08`/`09` and remediation file `17`;
2. Inventory Full Reopen package commit `170af9ea7a5afd127abcaae0ffb40aaa1fa25d4d`;
3. Inventory Menu-by-Menu Deep Challenge package branch `audit/inventory-menu-deep-challenge-2026-09-02-001`;
4. the 29 menu reference deliverables and issuing prompt preserved under that branch;
5. all direct-link and session-link records that may be used by future teams.

The audit must answer:

1. Is `C-05` truly remediated at the current branch surface?
2. Does any file still contain source code, schema, ORM, method, field, path or vendor-architecture leakage?
3. Does any file indirectly turn benchmark behavior into SMEsPlus design?
4. Are citations and references sufficient for audit traceability without exposing Layer 2 material?
5. Is the menu reference package safe for later Team B/C review after Boss approval?
6. What must remain quarantined?
7. What must be rewritten before any downstream reliance?
8. What still requires Boss-only review?

Target condition:

`INDEPENDENT CLEAN-ROOM RE-AUDIT PACKAGE PUBLISHED - NOT TEAM B/C AUTHORIZATION`

---

## 2. Absolute Authority Boundary

The executor may classify evidence safety only. The executor may not approve product design.

Hard prohibitions:

1. Do not declare `PASS`, `APPROVED`, `FINAL SOLUTION`, `READY FOR DEVELOPMENT`, `READY FOR PRODUCTION`, `TEAM B AUTHORIZED` or `TEAM C AUTHORIZED`.
2. Do not merge any branch.
3. Do not modify source evidence except in a separately proposed remediation list.
4. Do not open or reproduce quarantined source-level material unless the checkpoint explicitly requires controlled inspection.
5. Do not copy source code, ORM, schema, method names, field names, implementation paths or vendor architecture into outputs.
6. Do not convert clean-room learning into final SMEsPlus UI, schema, workflow or architecture.

Boss remains the sole Final Approver.

---

## 3. Mandatory Evidence Inputs

Inspect and cite these sources before conclusions:

| Evidence | Required Reference |
|---|---|
| Inventory Full Reopen execution branch | `audit/inventory-reopen-2026-09-02-inv-reopen-001` |
| Inventory Full Reopen commit | `170af9ea7a5afd127abcaae0ffb40aaa1fa25d4d` |
| Inventory Full Reopen closure | `19_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-REOPEN-001.md` |
| Material Unknown / Conflict Register | `13_INVENTORY_MATERIAL_UNKNOWN_CONFLICT_REGISTER.md` |
| Clean-room VETO findings | `10_CLEANROOM_IP_PROVENANCE_VETO_FINDINGS.md` |
| CORR-007B remediation branch | `audit/inventory-core-corr007b-3high-closure-010` |
| CORR-007B remediation commit | `9996072aa3a353dca99de4b22e8611171e24baf4` |
| Remediated CORR-007B file 08 | clean-room learning summary for account-led inventory period close |
| Remediated CORR-007B file 09 | clean-room learning summary for product category valuation policy |
| CORR-007B remediation record | `17_CORR007B_CLEAN_ROOM_REMEDIATION_RECORD.md` |
| Inventory Menu Deep Challenge branch | `audit/inventory-menu-deep-challenge-2026-09-02-001` |
| Menu package evidence commit | `473db147dd01859ff313b2920aba9d85bacff619` |
| Menu package closure update commit | `885f3cd5e920adae4c9746d13349c2bc50005aee` |
| Boss Final Gate package | `25_BOSS_FINAL_GATE_PACKAGE.md` |
| Menu coverage register | `02_INVENTORY_MENU_COVERAGE_REGISTER.md` |
| Object impact matrix | `03_INVENTORY_OBJECT_IMPACT_MATRIX.md` |
| Process handoff map | `04_INVENTORY_PROCESS_HANDOFF_MAP.md` |
| Thai naming register | `17_THAI_MENU_AND_REPORT_NAMING_REGISTER.md` |
| AI Expert overlay review | `23_AI_EXPERT_OVERLAY_REVIEW.md` |
| Session closure | `28_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001.md` |

If any required source cannot be fetched from GitHub, mark the session `HOLD / EVIDENCE REQUIRED`.

---

## 4. Clean-Room Audit Tests

Run these tests separately and preserve results:

### 4.1 Mechanical Leakage Scan

Search all files for:

- fenced code blocks;
- source-code syntax;
- ORM/model/schema terms;
- method/function names;
- field names;
- file paths;
- vendor-specific object identities;
- source comments copied into prose;
- benchmark terms used as SMEsPlus final design terms.

Do not reproduce hit content if it is sensitive. Record file, section, risk class and remediation action.

### 4.2 Citation and Provenance Scan

Verify that every major claim has one of:

- direct evidence link;
- carry-forward evidence link;
- explicit `UNKNOWN / EVIDENCE REQUIRED`;
- explicit `HOLD`;
- explicit Boss-only item.

### 4.3 Semantic Contamination Scan

Challenge whether benchmark behavior has become target architecture by stealth.

Classify each finding:

- `SAFE_CLEAN_ROOM_LEARNING`
- `NEEDS_WORDING_REWRITE`
- `NEEDS_QUARANTINE`
- `BOSS_ONLY_REVIEW`
- `FAIL / FROZEN`

### 4.4 Downstream Reliance Scan

Verify whether any file improperly authorizes:

- Team B design;
- Team C architecture;
- development;
- migration tooling;
- merge;
- Gate PASS;
- production.

Any such finding is material.

---

## 5. Mandatory C-05 Review

`C-05` is the controlling issue.

The executor must determine:

1. what the original `C-05` risk was;
2. which files were remediated;
3. whether the current branch surface is clean;
4. whether the old risk remains in git history;
5. whether Layer 2 Audit Quarantine is sufficiently defined;
6. whether Team B/C can safely read Layer 1 after Boss approval;
7. what conditions must be met before reliance;
8. whether any remaining file must be rewritten.

Allowed outcomes:

- `C-05 SURFACE REMEDIATED / HISTORY QUARANTINE REQUIRED`
- `C-05 PARTIAL / FURTHER REMEDIATION REQUIRED`
- `C-05 FAIL / FROZEN`

Do not mark `C-05 CLOSED` unless Boss issues a separate final decision.

---

## 6. Ai Audit SMEsPlus Required Challenge

Apply the full `Ai Audit SMEsPlus` structure:

`9 Veto Challenge Council + 9 Special Team Challenge + 4 AI Expert Overlay Roles`

Minimum focus:

| Layer | Required Challenge |
|---|---|
| 9 Veto Council | evidence integrity, clean-room boundary, gate status, no hidden authorization |
| 9 Special Team | menu evidence safety, object/impact matrix safety, handoff map safety, Thai naming safety, migration safety |
| 4 AI Expert Overlay | functional design risk, database identity risk, integration/localization risk, code/UI architecture leakage risk |

Every objection must be preserved. The most conservative unresolved material verdict controls the package.

---

## 7. Checkpoints

Boss will wait at the Final Gate. Intermediate checkpoints may proceed autonomously only if evidence criteria are met.

### CP-00 - Repository and Branch Safety

Verify repository, branch, HEAD, working tree, read-only mode, no production write, no merge, no Team B/C/Dev authorization.

### CP-01 - Evidence Intake

Fetch all mandatory evidence inputs from GitHub. If any link is missing, mark `HOLD / EVIDENCE REQUIRED`.

### CP-02 - CORR-007B C-05 Audit

Audit remediated files `08`/`09`, remediation file `17`, and C-05 preservation in the reopen/menu packages.

### CP-03 - Menu Package Mechanical Scan

Scan all 29 deliverables and issuing prompt for leakage patterns.

### CP-04 - Citation / Provenance / Claim Safety

Verify whether claims are properly sourced or marked unknown/hold.

### CP-05 - Semantic Contamination Challenge

Challenge whether benchmark behavior became design, schema, workflow or UI approval.

### CP-06 - Downstream Reliance Decision

Classify each package surface:

- `SAFE_FOR_BOSS_REVIEW`
- `SAFE_FOR_AI_AUDIT_ONLY`
- `SAFE_FOR_TEAM_B_AFTER_BOSS_APPROVAL`
- `HOLD_FOR_REWRITE`
- `BOSS_ONLY`
- `FAIL / FROZEN`

### CP-07 - Ai Audit SMEsPlus Challenge

Run 9 Veto + 9 Special Team + 4 AI Expert Overlay and preserve all objections.

### CP-08 - Boss Final Gate Package

Prepare direct findings and recommended next action. Do not declare PASS.

---

## 8. Required Output Files

Publish all outputs under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/CLEANROOM_REAUDIT_EXECUTION/`

Required files:

1. `00_EXECUTION_CHECKPOINT_LOG.md`
2. `01_MANDATORY_EVIDENCE_INTAKE_REGISTER.md`
3. `02_CORR007B_C05_CLEAN_ROOM_REAUDIT.md`
4. `03_MENU_PACKAGE_MECHANICAL_LEAKAGE_SCAN.md`
5. `04_CITATION_PROVENANCE_CLAIM_SAFETY_REGISTER.md`
6. `05_SEMANTIC_CONTAMINATION_CHALLENGE_REGISTER.md`
7. `06_DOWNSTREAM_RELIANCE_CLASSIFICATION_MATRIX.md`
8. `07_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md`
9. `08_AI_AUDIT_SMEPLUS_9_SPECIAL_TEAM_CHALLENGE.md`
10. `09_AI_EXPERT_OVERLAY_REVIEW.md`
11. `10_REMEDIATION_ACTION_REGISTER.md`
12. `11_BOSS_FINAL_GATE_PACKAGE.md`
13. `12_NEXT_PROMPT_RECOMMENDATION.md`
14. `13_SHA256_MANIFEST.txt`
15. `14_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-CLEANROOM-REAUDIT-001.md`

If a file cannot be completed due to missing evidence, create the file anyway and mark the affected rows as `HOLD / EVIDENCE REQUIRED`.

---

## 9. Final Gate Rules

At the end of the session, stop at one of:

- `READY FOR BOSS FINAL GATE REVIEW - CLEAN ROOM REAUDIT ONLY`
- `HOLD / EVIDENCE REQUIRED`
- `FAIL / FROZEN`

Do not state:

- `PASS`;
- `APPROVED`;
- `CLOSED`;
- `FINAL SOLUTION`;
- `READY FOR DEVELOPMENT`;
- `READY FOR PRODUCTION`;
- `TEAM B AUTHORIZED`;
- `TEAM C AUTHORIZED`.

---

## 10. GitHub Publication Requirement

Before closing the session, publish the prompt/output evidence to GitHub and provide:

1. Repository
2. Branch
3. Commit SHA
4. Direct GitHub link to `11_BOSS_FINAL_GATE_PACKAGE.md`
5. Direct GitHub link to `02_CORR007B_C05_CLEAN_ROOM_REAUDIT.md`
6. Direct GitHub link to `03_MENU_PACKAGE_MECHANICAL_LEAKAGE_SCAN.md`
7. Direct GitHub link to `06_DOWNSTREAM_RELIANCE_CLASSIFICATION_MATRIX.md`
8. Direct GitHub link to `10_REMEDIATION_ACTION_REGISTER.md`
9. Direct GitHub link to `14_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-CLEANROOM-REAUDIT-001.md`

If GitHub publication fails, do not claim the session is closed.

---

## 11. Starting Instruction for Claude

Start now.

Execute CP-00 first.

Proceed checkpoint by checkpoint without waiting for Boss confirmation only when evidence criteria are met.

Boss will wait at Final Gate.

Remember:

`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss is the sole Final Approver.`  
`Clean Room means business learning only; no source-code, schema, ORM, method, field, path or vendor architecture leakage.`  
`This session can classify clean-room safety but cannot approve SMEsPlus final design.`
