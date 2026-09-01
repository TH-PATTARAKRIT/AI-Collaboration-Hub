# [SMEPLUS-26-09-02-INV-REOPEN-001]
# Claude Sonnet 5 Max Execution Prompt — Inventory Full Reopen / AI Audit SMEsPlus / L999.999

## SINGLE CONTROLLED EXECUTION PROMPT FOR CLAUDE SONNET 5 MAX

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Jira: `ERPPLUS-139`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Execution Branch: `audit/inventory-reopen-2026-09-02-inv-reopen-001`  
Execution Folder: `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/EXECUTION/`  
Model: `Claude Sonnet 5 Max`  
Control Level: `/L999.999`  
Boss: `Sole Final Approver`  
Mode: `READ ONLY / EVIDENCE-FIRST / DELTA-FIRST / CLEAN-ROOM / MATERIAL-UNKNOWN-EXHAUSTION`

This is an execution prompt for the existing Inventory Reopen session. Do not create a new project, new domain, or duplicate session package.

---

## 0. Mandatory Source Prompt Load

Before execution, fetch and read the full contents of these canonical files from branch `SMEsPlus`:

1. `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/00_PRE_PROMPT_9VETO_CHALLENGE_AND_READINESS.md`
2. `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/01_NEW_SESSION_PROMPT_SMEPLUS-26-09-02-INV-REOPEN-001.md`
3. This execution prompt.

Mandatory governance input commits from the canonical prompt:

- Full Reopen Program: `42e04e639f2c83aeef6d7c313152a55170a4c6ef`
- Inventory 9-Veto Challenge / Readiness: `3cfb26faf04dddda6aea5f59e201ee1f008b94dd`
- NEW PROMPT Governance v2.0: `03b4244b2101e8c0a89d36255cc654fc2537c748`
- 9 Veto / 9 Special Team Charter: `5d81d628b9b159f89a93da7ab920c42ef8f09555`
- Global Challenge Ledger: `f8d940900896a5a11e7232bac0e829fc5a60e908`

Do not proceed from memory. If any required source cannot be fetched, publish `HOLD / EVIDENCE REQUIRED` with the failed path/ref.

---

## 1. Boss-Defined AI Audit SMEsPlus Structure

For this session, `AI Audit SMEsPlus` means the complete Boss-defined audit and challenge structure:

`9 Veto Challenge Council + 9 Special Team Challenge + 4 AI Expert Overlay Roles`

AI Audit SMEsPlus has authority to:

- challenge;
- contradict;
- verify;
- expose unknowns;
- test evidence integrity;
- prevent premature closure;
- force HOLD where evidence is missing.

AI Audit SMEsPlus has no authority to:

- declare PASS;
- close Gates;
- authorize Team B;
- authorize Team C;
- authorize Development;
- merge;
- release;
- approve production;
- override Boss Final Gate.

Boss remains the sole Final Approver.

---

## 2. Correct Team Layers To Lock Before Work

| Layer | Count | Authority | Must Publish |
|---|---:|---|---|
| `9 Veto Challenge Council` | 9 | Primary challenge body | Separate findings by Veto track |
| `9 Special Team Challenge` | 9 | Supplementary deep-dive challenge | Separate material delta findings |
| `4 AI Expert Overlay Roles` | 4 | Expert overlay only | Cross-challenge notes and contradictions |
| `Boss` | 1 | Sole Final Approver | Final Gate decision only |

Do not collapse these layers into one generic 9-team summary. Do not replace the 9+9 structure with the 4 AI Expert Roles.

---

## 3. Execution Authority And Checkpoint Rule

Boss will wait at the Final Gate. During execution, Claude may pass internal checkpoints and continue without asking Boss for confirmation when evidence supports continuation.

Checkpoint approval is operational continuation only. It is not Gate PASS, Boss approval, final closure, Team B authorization, Team C authorization, or development readiness.

For every checkpoint, publish a short checkpoint record inside the relevant deliverable or closure file:

- `Checkpoint ID`
- `Evidence inspected`
- `Result: CONTINUE / HOLD / FAIL`
- `Reason`
- `% Board / % STATE / % STEP based only on evidence`
- `Next action`

If a checkpoint is `HOLD` or `FAIL`, stop execution and publish the HOLD/FAIL evidence. Do not hide the blocker.

---

## 4. Mandatory Parallel Safety

Before creating or modifying execution artifacts:

1. Create an isolated Inventory worktree.
2. Create/use branch `audit/inventory-reopen-2026-09-02-inv-reopen-001`.
3. Verify current branch before every commit.
4. Never reuse Account worktree or Account branch.
5. Never reuse Joint Account x Inventory worktree or branch.
6. Never commit Inventory evidence to an Account or Joint branch.
7. Never commit Account or Joint evidence to the Inventory branch.
8. Do not push until final branch verification is complete.
9. Include branch/worktree verification in `19_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-REOPEN-001.md`.

Checkpoint `CP-00` cannot pass until these are verified.

---

## 5. Mandatory Checkpoints

### CP-00 — Branch, Worktree, Source Prompt Verification

Verify:

- current branch;
- isolated worktree;
- canonical prompt files loaded;
- required execution folder exists or is created under the correct path;
- no existing execution deliverables are overwritten without evidence.

Output: checkpoint note in session closure draft.

### CP-01 — Prior Evidence Chain Reconstruction

Reconstruct from immutable evidence:

- historical `GROUP_A_SALES_INVENTORY_PURCHASE` Inventory evidence;
- DR-002 Account-grade Inventory Deep Research;
- DR-002 execution artifacts;
- corrective/supersession records through CORR-005;
- independent-review lineage;
- IDR-007 readiness `54025627d63eb4055ff89f602454d9122876dfb2`;
- IDR-007 prompt `d5261b7a61cc317bccbaaf466c26417da6ba3486`;
- any later IDR-007 result if found;
- Boss `bh_* / bhpro_*` Inventory source-scope exclusions;
- Accounting / Inventory backbone roadmap and current Account state.

Output: `01_INVENTORY_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md`

### CP-02 — AI Audit SMEsPlus Question Lock

Build the Inventory Question Fingerprint Index before asking new questions.

Classify each question:

- `CLOSED_WITH_EVIDENCE — DO NOT REASK`
- `CARRY_FORWARD — NO MATERIAL DELTA`
- `REOPEN_ELIGIBLE — DELTA TRIGGER EXISTS`
- `CONFLICTING — REOPEN REQUIRED`
- `UNKNOWN — STILL MATERIAL`
- `SUPERSEDED — HISTORICAL ONLY`

Output: fingerprint index and delta trigger map.

### CP-03 — 9 Veto Challenge Council Findings

Execute all nine Veto tracks separately:

1. Audit VETO / Evidence & Governance
2. TBRAC / Thailand Business Reality & User Fitness
3. IBPV / Business Process & Design Integrity
4. IDTM / Data, Identity, Reconciliation & Integrity
5. IESA / ERP & SaaS System Integrity
6. Financial / Accounting / Tax / Statutory VETO
7. Security / Privacy / Resilience VETO
8. Clean-Room / IP / Provenance VETO
9. AI Control / Automation / Human Oversight VETO

Output: deliverables `03` through `11`.

### CP-04 — 9 Special Team Challenge Findings

Execute the nine Special Team challenges as supplementary deep-dive over the same evidence base. At minimum, answer:

1. Product Category / Product Group valuation-policy ownership and boundary.
2. Manual vs Automated inventory valuation as source behavior and target hypothesis.
3. Periodic vs Perpetual stock/accounting as an interface issue.
4. Standard / FIFO / AVCO only where source/dump evidence supports it.
5. `stock.move`, `stock.quant`, `stock.picking`, valuation layer and physical movement semantics.
6. Physical count / cycle count / adjustment / freeze / conflict / backdate behavior.
7. Stock cut-off and opening/closing stock quantity continuity.
8. Stockable / Consumable / Service routing and edge cases.
9. Items requiring Session 3: Account x Inventory Joint Reopen.

Output: integrated findings inside deliverables `02`, `12`, `13`, `14`, `15`, and `20`.

### CP-05 — 4 AI Expert Overlay Review

Apply these expert overlays without replacing the 9+9 structure:

| AI Expert Overlay Role | Required Challenge |
|---|---|
| Leader Functional Design | Validate Inventory user flow, Figma-UX readiness, UAT flow, and exception workflow coverage. |
| Leadership Database Design | Validate movement identity, stock ledger, snapshot/derived quantity discipline, migration replay and idempotency. |
| Lead Integration & Localization | Validate Accounting/Tax/Thai localization handoff boundaries and HOLD routing. |
| Lead Code & UI Architect | Validate clean-room target boundary, Node.js SaaS implications, and no Odoo/QWeb/model/workflow cloning. |

Output: overlay notes and contradictions in deliverables `13`, `14`, `16`, `17`, and `20`.

### CP-06 — Full Coverage Register

Cover all 40 mandatory Inventory coverage items from the canonical prompt.

For each item, record:

`Prior Status / Prior Evidence / Delta / Current Evidence / Unknown / Veto Track / Special Team / AI Expert Overlay / Accounting Dependency / Gate Impact`

Output: `02_INVENTORY_FULL_COVERAGE_STATUS_REGISTER.md`

### CP-07 — Accounting Boundary And Joint Session Routing

Classify every accounting-dependent item using only these statuses:

- `INVENTORY_OWNED_STOCK_FACT`
- `ACCOUNTING_INTERFACE_REQUIREMENT`
- `PENDING_ACCOUNT_SESSION`
- `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION`
- `OUT_OF_INVENTORY_SCOPE`

Inventory must not close:

- COA / Account Type / Account Group conclusions;
- final journal entry design;
- VAT / WHT / CIT statutory conclusions;
- retained earnings / current-year earnings logic;
- Account lock-date policy as Accounting truth;
- Inventory valuation to GL reconciliation as final Accounting closure;
- Account x Inventory Backbone baseline.

Output: deliverables `14` and `20`.

### CP-08 — Final Evidence Package And Manifest

Publish all required deliverables and SHA-256 manifest.

Output: deliverables `17`, `18`, and `19`.

### CP-09 — Final Gate Ready Stop

Stop at one of the permitted terminal statuses:

- `INVENTORY FULL REOPEN DEEP REVALIDATION COMPLETE — READY FOR INDEPENDENT REOPEN AUDIT`
- `HOLD / EVIDENCE REQUIRED`
- `FAIL / FROZEN — MATERIAL EVIDENCE / GOVERNANCE / CLEAN-ROOM FAILURE`

Do not proceed beyond this stop condition.

---

## 6. Required Deliverables

Publish exactly under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/EXECUTION/`

Required files:

1. `01_INVENTORY_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md`
2. `02_INVENTORY_FULL_COVERAGE_STATUS_REGISTER.md`
3. `03_AUDIT_VETO_DEEP_FINDINGS.md`
4. `04_TBRAC_DEEP_FINDINGS.md`
5. `05_IBPV_DEEP_FINDINGS.md`
6. `06_IDTM_DEEP_FINDINGS.md`
7. `07_IESA_DEEP_FINDINGS.md`
8. `08_FINANCIAL_ACCOUNTING_INTERFACE_VETO_FINDINGS.md`
9. `09_SECURITY_PRIVACY_RESILIENCE_VETO_FINDINGS.md`
10. `10_CLEANROOM_IP_PROVENANCE_VETO_FINDINGS.md`
11. `11_AI_CONTROL_AUTOMATION_VETO_FINDINGS.md`
12. `12_STOCKABLE_CONSUMABLE_SERVICE_DEEP_PROOF.md`
13. `13_INVENTORY_MATERIAL_UNKNOWN_CONFLICT_REGISTER.md`
14. `14_INVENTORY_ACCOUNTING_DEPENDENCY_REGISTER.md`
15. `15_INVENTORY_GATE_REOPEN_OR_CARRY_FORWARD_REGISTER.md`
16. `16_INVENTORY_NEXT_CONTROLLED_ACTION_AND_OWNER_MATRIX.md`
17. `17_INVENTORY_REOPEN_DEEP_REVALIDATION_REPORT.md`
18. `18_INVENTORY_REOPEN_SHA256_MANIFEST.txt`
19. `19_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-REOPEN-001.md`
20. `20_INVENTORY_PENDING_JOINT_SESSION_3_INTERFACE_REGISTER.md`

If evidence is missing, create the relevant deliverable with `HOLD / EVIDENCE REQUIRED`. Do not fabricate closure.

---

## 7. Mandatory Reporting Format At Each Checkpoint

Every checkpoint report must include:

| Field | Required Content |
|---|---|
| Checkpoint | `CP-xx` |
| Result | `CONTINUE / HOLD / FAIL` |
| Evidence | file path, commit SHA, branch, source artifact, or explicit missing evidence |
| AI Audit SMEsPlus Impact | 9 Veto / 9 Special Team / 4 AI Expert Overlay impact |
| % Board | evidence-based only |
| % STATE | evidence-based only |
| % STEP | evidence-based only |
| Open Risks | concise list |
| Next Action | next checkpoint or stop condition |

Do not invent percentages. If no reliable baseline exists, write `TBD — BASELINE REQUIRED`.

---

## 8. Hard Rules

`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`  
`FULL REOPEN != RESET TO ZERO.`  
`No repeated question without a material delta.`  
`No Answer Key Before Research.`  
`No Cross-Team Execution.`  
`No Evidence Preservation = No Lifecycle Promotion.`  
`No Material Unknown Exhaustion = No Inventory Evidence Gate PASS.`  
`AI must not fabricate stock movements, quantities, valuation facts or historical events to make migration/reconciliation pass.`

Clean-room principles are mandatory:

1. `Reference Only` — Odoo / SAP / Salesforce / Legacy / Dump are learning and business-semantic proof only.
2. `No Copy / No Clone / No Reuse` — no source code, XML, QWeb, ORM, schema, workflow, naming pattern, or application architecture reuse.
3. `Migrate Business Facts + Business Semantics Only` — not legacy application architecture.
4. `SMEsPlus Target Design Must Be Original` — clean-room Node.js SaaS target design with Boss approval.

---

## 9. Final Stop Instruction

When all authorized work is complete, publish the evidence package, SHA-256 manifest, and session closure record, then stop.

Do not start Account Reopen.  
Do not start Account x Inventory Joint Reopen.  
Do not start Team B.  
Do not start Team C.  
Do not start Development.  
Do not declare Gate PASS.  
Do not declare Boss approval.

Final output to Boss must include:

- execution branch;
- commit SHA;
- execution folder;
- direct GitHub links to all 20 deliverables;
- checkpoint summary `CP-00..CP-09`;
- terminal status;
- explicit list of HOLD items, if any.
