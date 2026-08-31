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

## ROUND 2 ADDITIONS (session `SMEPLUS-26-08-30-COA-G01R2-001`, 2026-08-31)

### New GitHub documents read

`00_Architecture_Governance/THAILAND_BUSINESS_REALITY_USER_FITNESS_CONTROL_V1.md` (commit `d57cca7`, Jira `ERPPLUS-134`) — governing source for `COA_G01_TBRAC_TB01_TB13_MATRIX_R2.md`.

`TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/` — all 31 files (not individually read by Round 1; read in full this session).

`TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/SONNET_DEEP_SYNTHESIS/` — all 17 files (not read by Round 1; read in full this session — source of the "20 residual unknowns" trace).

`TEAM_A/09_OPEN_QUESTIONS/UNKNOWN_AND_EVIDENCE_GAP_REGISTER.md` — re-read for the 11-vs-20 scope reconciliation.

`CHATGPT_AUDIT/` — all 18 files (full Team B independent-audit chronology, Rounds 1–8, read this session for `COA_G01_TEAM_A_SOURCE_CLASS_A_RECONCILIATION_R2.md` §5 and to check for any audit trail covering `c530138`).

`PMO_VERIFICATION/` — all 4 files.

`TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/B14_CLEAN_ROOM_PROVENANCE_MATRIX.md` — re-read in full; at the time of this CORR1 read, the coverage gap spanned 4 `COA_STANDARD` documents (the temporary `c530138` file was still present). **Corrected CORR2:** current count is 3 — see `COA_G01_CORR2_POST_PUBLICATION_CLOSURE.md`.

`TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_STANDARD/DOMAIN_01_COA_G01_SOURCE_BASELINE_RECONCILIATION.md` (commit `c530138`) — read in full; content investigated and classified `CONFLICTING EVIDENCE / UNVERIFIED SELF-DECLARED RESULT`, not adopted as evidence.

`BOSS_GATE/` — full current `ls -la` listing taken to confirm the `AH`/`AQ` letter-collision pattern and the current file set.

Jira `ERPPLUS-132` — full comment history (8 comments) read via the Atlassian connector to establish the Jira-side audit trail (or its absence, for `c530138`/`8fceca0`).

### New Round 2 deliverables produced (this folder)

`COA_G01_CURRENT_STATE_ADDENDUM_R2.md`, `COA_G01_TEAM_A_SOURCE_CLASS_A_RECONCILIATION_R2.md`, `COA_G01_WORKBOOK_PROVENANCE_AND_ROW_LINEAGE_R2.md`, `COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md`, `COA_G01_TBRAC_TB01_TB13_MATRIX_R2.md`, `COA_G01_PRE_PROMPT_FINDING_CLOSURE_REGISTER_R2.md`, `SESSION_CLOSURE_R2.md`.

### Round 1 files updated in place this session (not replaced)

`COA_G01_SOURCE_CONFLICT_REGISTER.md` (C-04 resolved, C-07 added), `COA_G01_OPEN_UNKNOWN_REGISTER.md` (11-vs-20 reconciliation added, N-01..N-05 Round 2 status added), `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md` (4th uncovered document noted), `COA_G01_SAAS_INVARIANT_COMPLIANCE.md` (SI-08 contradiction check, `c530138` competing matrix noted), `COA_G01_GATE_REPORT.md` (§15 Round 2 update and terminal status appended).

### GitHub document also updated this session (outside this folder)

`BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AL_COA_CLOSURE_EVIDENCE_INDEX.md` — corrected to remove the unqualified PASS/zero-gaps claims introduced by commit `8fceca0`, without deleting prior text from git history.

## CORR1 ADDITIONS (Boss directive `COA-G01R2-CORR1`, 2026-08-31)

### New file

`COA_G01_CORR1_POST_PUBLICATION_CLOSURE.md` — confirms the correction package, branch, file count, SHA-256 verification result, and restated Gate status.

### Files updated in place (CORR1)

`COA_G01_PRE_PROMPT_FINDING_CLOSURE_REGISTER_R2.md` (finding-count arithmetic corrected: 14/4/6=24 for Q/R/E, S tracked separately), `COA_G01_SOURCE_BASELINE_REGISTER.md`, `COA_G01_THAI_RELEVANCE_REGISTER.md`, `COA_G01_ACCOUNT_CONCEPT_UNIVERSE.md` (all three previously untouched, now updated), `COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md` (fully rebuilt: 19 per-type subsections, all 17 AS §8.7 fields explicit, Evidence Character/Fact Status separated), `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md` (real document-level review of all 4 COA_STANDARD documents executed), `COA_G01_TBRAC_TB01_TB13_MATRIX_R2.md` (TB-06 corrected to an allowed status), `COA_G01_TEAM_A_SOURCE_CLASS_A_RECONCILIATION_R2.md` (62/64/65 file-count reproducibly reconciled, `06_DOMAIN_RESEARCH` off-by-one corrected), `COA_G01_GATE_REPORT.md` (§16 CORR1 section appended).

### GitHub document also updated (outside this folder)

`BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AL_COA_CLOSURE_EVIDENCE_INDEX.md` — Gate status label corrected to `HOLD / CORRECTION REQUIRED + EVIDENCE REQUIRED`.

## CORR2 ADDITIONS (Boss directive `COA-G01R2-CORR2`, 2026-08-31)

### New file

`COA_G01_CORR2_POST_PUBLICATION_CLOSURE.md` — confirms the CORR2 correction package per directive §4.6.

### GitHub document updated (outside this folder)

`TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_STANDARD/DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md` — explicit source-column clean-room disclaimer added per directive §4.2. **Now included in the SHA-256 operational set below, per directive §4.5.**

### Files updated in place (CORR2)

`COA_G01_PRE_PROMPT_FINDING_CLOSURE_REGISTER_R2.md` (R-08/E-07 corrected, Q/R/E totals recomputed mechanically to 14/6/4=24), `COA_G01_SOURCE_CONFLICT_REGISTER.md` (C-06 status update, C-07 current-vs-historical clarification), `COA_G01_OPEN_UNKNOWN_REGISTER.md` (N-03 resolved), `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md` (new CORR2 six-part current-state section), `COA_G01_CURRENT_STATE_ADDENDUM_R2.md` (chronology items 9–10 added), `COA_G01_GATE_REPORT.md` (§15.2 corrected, §17 CORR2 section appended), this manifest.

### GitHub document also updated (outside this folder)

`BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AL_COA_CLOSURE_EVIDENCE_INDEX.md` — references both CORR1 and CORR2; C-06 description narrowed to its current, accurate form.

### SHA-256 operational set, per directive §4.5 (explicit)

The rebuilt `COA_G01_SHA256SUMS.txt` covers: every current file in this folder except the checksum file itself; the Boss authorization artifact AQ (existing convention, unchanged); and, **new this pass**, all 3 current `COA_STANDARD` documents (`DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`, `DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md`, `DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`) — these were reviewed as evidence in CORR1/CORR2 but never previously included in this folder's own checksum manifest.

## CORR3 ADDITIONS (Boss directive `COA-G01R2-CORR3`, 2026-08-31)

### New file

`COA_G01_CORR3_POST_PUBLICATION_CLOSURE.md` — confirms the CORR3 correction package per directive §5.

### GitHub document updated (outside this folder)

`TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_STANDARD/DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md` — controlled supersession notice added (finding `AUD2-01`): the document's original "15 active Thailand types" recommendation is marked historical/superseded; current target restated as 19 ACTIVE by Boss ruling. Source evidence (15/144/14/389 counts) preserved unaltered. **Already included in the SHA-256 operational set since CORR2.**

### Files updated in place (CORR3)

`BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AL_COA_CLOSURE_EVIDENCE_INDEX.md` (finding `AUD2-02`: rejected Connected Drive claim and misleading Class E/F "reconciled source layers" bullets replaced with evidence-supported wording, Source Classes E/F explicitly restated `EVIDENCE_MISSING`; finding `AUD2-03`: file count corrected 21→25 physical/24 markdown/28 operational (including this CORR3 closure artifact itself), open-unknown count corrected 5→4, ChatGPT review status updated to reflect the CORR2 audit having occurred), `COA_G01_OPEN_UNKNOWN_REGISTER.md` (top metadata row given an explicit CORR3 current-state correction: open N-series = 4, not 5), `COA_G01_GATE_REPORT.md` (§8 given a CORR3 current-state correction; §18 CORR3 section appended), this manifest.

### Mechanical file-count recomputation (finding `AUD2-03`, per directive §6 — not copied from the prior count)

Recomputed directly from the CORR3 working tree, 2026-08-31, **after** this manifest and the new CORR3 closure artifact were both written (self-referential count — see the note in `COA_G01_CORR3_POST_PUBLICATION_CLOSURE.md`):
- Files physically present in `COA_G01_EVIDENCE/`: **25** (24 Markdown + 1 SHA-256 checksum file — `ls -1 | wc -l`).
- Markdown files in the SHA-256 operational set: **24** (`ls -1 *.md | wc -l`).
- Total operational SHA-256 entries: **28** (24 local Markdown + 1 external `AQ` ruling + 3 external `COA_STANDARD` documents).

### SHA-256 operational set — composition unchanged from CORR2 (local Markdown + AQ + 3 COA_STANDARD documents), one file added to the local Markdown count (this CORR3 closure artifact)

24 local Markdown + `AQ` + 3 `COA_STANDARD` documents = 28 entries; every hash recomputed to reflect CORR3 edits.

## Verification instrument

`COA_G01_SHA256SUMS.txt` (this folder) contains SHA-256 checksums of every file in the operational set above (Round 1 + Round 2 + CORR1 + CORR2 + CORR3), recomputed after all CORR3 content was finalized and immediately before the local commit. Reproducible verification command recorded in that file's header.
