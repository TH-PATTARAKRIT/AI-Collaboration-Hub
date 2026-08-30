# COA-G01 — Evidence Manifest

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Enumerate every document read or produced as evidence for this COA-G01 remediation pass | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | This artifact | 2026-08-30 22:27 +0700 | ChatGPT Independent Review (pending); PMO (pending); Boss (pending) | COMPLETE FOR THIS PASS (see explicit exclusions below) | Supports the SHA-256 manifest and Gate Report |

## GitHub `SMEsPlus` branch documents read (commit `d57cca7`)

`BOSS_GATE/`: `DOMAIN_01_ACCOUNTING_CORE_D_BOSS_GATE_DECISION_PACK.md`, `..._AF_TEAM_B_DESIGN_FINAL_GATE_DECISION_PACK.md`, `..._AG_BOSS_COA_LOCAL_TH_RULING.md`, `..._AH_BOSS_COA_DECISION_SUMMARY.md`, `..._AH_BOSS_FINAL_GATE_RULING.md`, `..._AJ_BOSS_ACCOUNT_TYPE_19_ACTIVE_RULING.md`, `..._AK_BOSS_THAI_COA_CLOSURE_AUTHORIZATION.md`, `..._AL_COA_CLOSURE_EVIDENCE_INDEX.md`, `..._AM_BOSS_COA_SAAS_ARCHITECTURE_AMENDMENT.md`, `..._AN_COA_CLOSURE_NEW_SESSION_CARRY_FORWARD_V2.md`, `..._AO_BOSS_CROSS_GATE_SAAS_INVARIANTS_RULING.md`, `..._AP_COA_CLOSURE_NEW_SESSION_CARRY_FORWARD_V3_CROSS_GATE_SAAS.md`, `README.md`.

`CHATGPT_AUDIT/DOMAIN_01_ACCOUNTING_CORE_AD_TEAM_B_INDEPENDENT_REAUDIT_ROUND8.md`

`PMO_VERIFICATION/DOMAIN_01_ACCOUNTING_CORE_AE_TEAM_B_DESIGN_PMO_VERIFICATION.md`, `..._AI_POST_BOSS_DECISION_REGISTER.md`

`TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_STANDARD/DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`, `DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md`, `DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`

`TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/B14_CLEAN_ROOM_PROVENANCE_MATRIX.md`

`TEAM_A/09_OPEN_QUESTIONS/UNKNOWN_AND_EVIDENCE_GAP_REGISTER.md`

`00_Architecture_Governance/THAILAND_BUSINESS_REALITY_USER_FITNESS_CONTROL_V1.md`, `STATE03_ENTERPRISE_MODULE_LEARNING_PRIORITY_MATRIX.md`

`00_Project_Governance/POLICIES/CONTROLLED_CARRY_FORWARD_AND_HANDOFF_POLICY.md`, `00_Project_Governance/DECISIONS/BOSS_DECISION_CONTROLLED_CARRY_FORWARD_GOVERNANCE_2026-08-30.md`

## Local `ACCOUNT` folder documents read (not on GitHub — see `COA_G01_SOURCE_CONFLICT_REGISTER.md` C-01)

`STATE03_DETAILED_FOLLOWUP/` — all 9 files (`STATE03_OPEN_ITEM_REGISTER.csv`, `STATE03_CARRY_FORWARD_REGISTER.csv`, `STATE03_BOSS_REVIEW_SUMMARY.md`, `STATE03_STEP_STATUS_REGISTER.md`/`.csv`, `STATE03_NEXT_ACTION_PLAN.md`, `STATE03_GATE_DECISION_REGISTER.md`, `STATE03_AUDIT_VETO_REVIEW.md`, `STATE03_EVIDENCE_GAP_REGISTER.csv`)

`STEP040304R2_STATE03_EVIDENCE_PACK/` — all 5 subfolder documents

`STEP040304R5_STATE03_FREEZE_EVIDENCE_PACK/02_FINDINGS_REGISTER/STEP040304R5_FINDINGS_REGISTER.md` (S1–S11 findings)

`STEP0303_TOOLCHAIN_MATRIX/02_THAI_TOOLCHAIN/STEP0303_THAI_LOCALIZATION_TOOLCHAIN.md` (T1–T9 findings)

`STEP0303R2_BOSS_TOOLCHAIN_RULING_SELECTION_GATE/`, `STEP0303R3_CORE_TOOLCHAIN_BOSS_RULING_CLOSURE/`, `STEP0303R4_FINAL_CLOSURE/`, `STEP0303R5_PLANNING_BASELINE_CLOSURE/` — folder contents reviewed for status/timeline reconciliation (C-02, C-03)

`Accounting Module Overview.docx`, `Accounting_Module_Technical_Review_v1.docx`, `SMEPLUS-26-06-29-001_Project_Constitution_v1.0.docx`, `SMEPLUS-26-06-29-001_Account_Working_Pack_Report_v1.0.docx` (converted via `textutil` for text extraction)

`07 SAAS ARCHITECH/SMEsPlus SaaS Architecture Review.pdf`

## Explicitly NOT read / out of scope for this pass

- Vendor source code bodies under `01 ACCOUNT/SOURCE CODE/` — folder/module names only were noted (clean-room rule: business facts and semantics only, never source code).
- The `03 DATABASE`, `03 DATABASE.zip`, and `04 FLOWCHART_BPMN` local folders — not opened; not claimed as reconciled by this pass.
- `05_.../AI_Collaboration_Framework_v2.3` and `06_.../UX_System_Design_Blueprint_Pack_v2.4` packages — not opened; unrelated to COA-G01 scope.
- Any primary Thai Revenue Department regulatory source (class H) — not invoked, per the Gate-appropriate evidence boundary (deferred to COA-G06).
- GitHub branches other than `SMEsPlus` (e.g. the ~50 `claude/...`, `agent/...`, `governance/...` branches visible in `git branch -a`) — not reviewed; this pass reconciles the `SMEsPlus` branch head only, as instructed.

## Verification instrument

`COA_G01_SHA256SUMS.txt` (this folder) contains SHA-256 checksums of every file produced by this session, computed after all content was finalized and immediately before the local commit.
