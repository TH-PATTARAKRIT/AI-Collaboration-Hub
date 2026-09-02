# [SMEPLUS-26-09-02-ACC-BOSS-DECISION-LEGAL-TAX-ROUTING-001]
# Account Boss Decision, Legal-Tax Routing & Controlled Next-Step Package / L999.999

## 1. PROJECT IDENTITY

Project: SMEsPlus ENTERPRISE SUITE  
STATE: STATE03 - Architecture  
Workstream: ACCOUNT_REOPEN / MENU_PROCESS_DEEP_STUDY follow-up  
Jira: ERPPLUS-138  
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub  
Canonical Branch: SMEsPlus  
Execution Mode: Evidence-first / Boss decision routing only  
Executor: Claude session selected by Boss  
Boss: Sole Final Approver

SMEsPlus is a new Thai SaaS ERP design candidate. Open ERP / Odoo is a process benchmark only.

This prompt is NOT:
- a final accounting solution prompt
- a Team B functional design prompt
- a Team C development prompt
- a Gate PASS prompt
- an authorization to merge, close, reopen, or approve any Gate

Hard rules:
- No Evidence = No Progress.
- Never Skip Gate.
- Boss is the sole Final Approver.
- Do not copy Open ERP / Odoo code, schema, ORM, workflow, Thai labels, or report names.
- Do not declare PASS, APPROVED, CLOSED, FINAL SOLUTION, DEVELOPMENT READY, or PRODUCTION READY.

## 2. SOURCE PACKAGE TO VERIFY FIRST

Before writing any output, fetch and verify this exact source package:

| Field | Value |
|---|---|
| Source Execution Branch | `audit/account-menu-process-deep-study-2026-09-02-001` |
| Source Publication Commit | `5183e9f6ef4272e68c65d831580886e341118d53` |
| Source Base Commit | `788479552971940a126a542da5343944f7f3e0d4` |
| Source Package Path | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/MENU_PROCESS_DEEP_STUDY_EXECUTION/` |

Mandatory source files to read:

1. `02_ACCOUNT_MENU_COVERAGE_REGISTER.md`
2. `03_ACCOUNT_OBJECT_IMPACT_MATRIX.md`
3. `04_ACCOUNT_PROCESS_HANDOFF_MAP.md`
4. `20_GAP_OWNER_GATE_IMPACT_REGISTER.md`
5. `21_BOSS_FINAL_GATE_PACKAGE.md`
6. `22_NEXT_PROMPT_RECOMMENDATION.md`
7. `23_SHA256_MANIFEST.txt`
8. `24_SESSION_CLOSURE_SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001.md`

Direct source links pinned to commit:

- `02_ACCOUNT_MENU_COVERAGE_REGISTER.md`: https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/5183e9f6ef4272e68c65d831580886e341118d53/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/MENU_PROCESS_DEEP_STUDY_EXECUTION/02_ACCOUNT_MENU_COVERAGE_REGISTER.md
- `03_ACCOUNT_OBJECT_IMPACT_MATRIX.md`: https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/5183e9f6ef4272e68c65d831580886e341118d53/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/MENU_PROCESS_DEEP_STUDY_EXECUTION/03_ACCOUNT_OBJECT_IMPACT_MATRIX.md
- `04_ACCOUNT_PROCESS_HANDOFF_MAP.md`: https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/5183e9f6ef4272e68c65d831580886e341118d53/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/MENU_PROCESS_DEEP_STUDY_EXECUTION/04_ACCOUNT_PROCESS_HANDOFF_MAP.md
- `20_GAP_OWNER_GATE_IMPACT_REGISTER.md`: https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/5183e9f6ef4272e68c65d831580886e341118d53/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/MENU_PROCESS_DEEP_STUDY_EXECUTION/20_GAP_OWNER_GATE_IMPACT_REGISTER.md
- `21_BOSS_FINAL_GATE_PACKAGE.md`: https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/5183e9f6ef4272e68c65d831580886e341118d53/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/MENU_PROCESS_DEEP_STUDY_EXECUTION/21_BOSS_FINAL_GATE_PACKAGE.md
- `22_NEXT_PROMPT_RECOMMENDATION.md`: https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/5183e9f6ef4272e68c65d831580886e341118d53/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/MENU_PROCESS_DEEP_STUDY_EXECUTION/22_NEXT_PROMPT_RECOMMENDATION.md
- `24_SESSION_CLOSURE_SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001.md`: https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/5183e9f6ef4272e68c65d831580886e341118d53/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/MENU_PROCESS_DEEP_STUDY_EXECUTION/24_SESSION_CLOSURE_SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001.md

Checkpoint CP-00:
- Confirm branch, commit, package path, and SHA-256 manifest.
- If any source file is missing or checksum fails, stop and report `SOURCE PACKAGE VERIFICATION HOLD`.

## 3. SESSION PURPOSE

Create a short controlled decision-and-routing package from files 20, 21, and 22.

The purpose is to prepare Boss and workstream owners for the next controlled actions:

1. Boss decision batch on this Account menu/process package.
2. COA-G01 unblock routing.
3. Legal-tax review routing for WHT, VAT, CIT, DBD/NPAE, statutory reports, and Thai accounting controls.
4. Account x Inventory Joint Session 3 routing.
5. TBRAC Thai user-fitness validation for Thai menu/report names.
6. AR/AP + Fixed Asset research pass routing.
7. Treasury / Cash & Bank process reference routing.
8. Financial statement taxonomy dependency routing.
9. Missing 18-deliverable Account Reopen lineage decision.
10. Merge/lineage decision for unmerged Account branches.

Do not decide these items for Boss. Convert them into decision records, owner routes, evidence requirements, and next prompt packs.

## 4. MANDATORY BOSS DECISION QUEUE

Build a decision queue from `21_BOSS_FINAL_GATE_PACKAGE.md` section 6 and `22_NEXT_PROMPT_RECOMMENDATION.md` section 2.

Each row must contain:

| Field | Required content |
|---|---|
| Decision ID | Stable ID, e.g. `ACC-DEC-001` |
| Source Item | File and section reference |
| Decision Required | Exact decision needed |
| Decision Authority | Boss / PMO / Legal-Tax Reviewer / TBRAC / Joint Session / Team A / Team B |
| Evidence Required | Concrete evidence needed before movement |
| Current Status | `HOLD / EVIDENCE REQUIRED`, `ROUTING REQUIRED`, or `BOSS DECISION REQUIRED` |
| Gate Impact | Which Gate or workstream is blocked |
| Recommended Next Action | Action only, no approval language |
| Output Needed | Prompt, review brief, evidence register, or final decision record |

Mandatory decision groups:

1. A1/A2 metadata extraction acknowledgement or rejection.
2. Menu screenshots and `Sources` menu identification.
3. `l10n_th_withholding_tax_multi` baseline for `ACC-WHT-06`.
4. SC-01..SC-10 scope decisions.
5. Legal-tax review commissioning.
6. Three unmerged Account artefacts and missing G-A3 / 18-deliverable lineage decision.
7. COA-G01 unblock items.

## 5. LEGAL-TAX ROUTING REQUIREMENTS

Create a legal-tax routing brief. It must not give legal or tax advice as final truth.

Minimum coverage:

- WHT: all multi-rate issues, sales-side WHT chain, purchase-side WHT liability, tax group closing accounts, PND3, PND53, PND1, PND54, PP36 where applicable.
- VAT: output VAT, input VAT, exempt VAT, non-deductible input VAT, Undue VAT, PP30.
- CIT: PND50, bad-debt deductibility, depreciation rate evidence, legal reserve if relevant.
- DBD/NPAE: statement format, cash-flow requirement, statutory books, audit trail, Thai report names.
- Evidence fields: authoritative source, citation, effective date, reviewer, conclusion, implementation impact, open questions.

Every statutory item must remain `LEGAL_TAX_REVIEW_REQUIRED` until reviewed by a qualified Thai legal-tax/accounting reviewer or supported by authoritative legal/tax source evidence.

## 6. THAI NAMING AND USER-FITNESS ROUTING

Use file 15 as candidate vocabulary only.

Create a TBRAC validation brief requiring:

- Thai accountant review.
- Thai SME owner/user review.
- Evidence that names are understandable in Thai business usage.
- Explicit rejection of mistranslated benchmark labels.
- Separate mapping for internal technical object name vs Thai menu/report display name.

Do not approve any Thai name as final.

## 7. JOINT ACCOUNT x INVENTORY ROUTING

Create a Joint Session 3 routing brief for `ERPPLUS-140`.

Minimum coverage:

- Receipt posting.
- Delivery / COGS posting.
- Return basis conflict.
- Adjustment.
- Landed cost.
- Manufacturing.
- Price difference.
- Opening balance cross-proof.
- Monthly close sequence.
- Year-end retained earnings design.
- Product category dual ownership.

Do not close Inventory-owned or Joint items from Account side.

## 8. COA-G01 UNBLOCK ROUTING

Create COA-G01 unblock routing without changing Gate status.

Mandatory items:

- Reissue or restore access to `งบการเงิน 2567.pdf` or equivalent source evidence.
- Resolve N-05 and C-03 Boss decision items.
- Prepare independent re-audit instruction for CORR5.
- Prepare PMO verification checklist.
- Preserve current status as `COA-G01 HOLD / EVIDENCE REQUIRED` until actual verification and Boss decision.

## 9. CHECKPOINTS

Checkpoint CP-01 - Source Verification:
- Complete before analysis.
- Verify source commit and manifest.

Checkpoint CP-02 - Decision Queue Complete:
- Decision queue contains all 7 mandatory decision groups.
- Every row has owner, evidence, status, and gate impact.

Checkpoint CP-03 - Routing Briefs Complete:
- Legal-tax, TBRAC, Joint Session 3, COA-G01 unblock, AR/AP + Fixed Asset, Treasury, and Financial Statement Taxonomy routes are written.

Checkpoint CP-04 - Boss Final Gate Package:
- Produce final Boss review package.
- Do not declare approval.
- Stop at `BOSS FINAL DECISION REQUIRED - ROUTING PACKAGE PUBLISHED`.

If a checkpoint cannot be completed, mark the checkpoint `HOLD` and explain the missing evidence.

## 10. REQUIRED OUTPUT PATH

Create all outputs under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/BOSS_DECISION_LEGAL_TAX_ROUTING_EXECUTION/`

## 11. REQUIRED OUTPUT FILES

Create these files:

1. `00_EXECUTION_CHECKPOINT_LOG.md`
2. `01_SOURCE_PACKAGE_VERIFICATION_REGISTER.md`
3. `02_BOSS_DECISION_QUEUE.md`
4. `03_EVIDENCE_ACCEPTANCE_DECISION_FORM.md`
5. `04_ACC_WHT_06_MODULE_BASELINE_DECISION_PACK.md`
6. `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md`
7. `06_LEGAL_TAX_REVIEW_BRIEF.md`
8. `07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md`
9. `08_TBRAC_THAI_NAMING_VALIDATION_BRIEF.md`
10. `09_COA_G01_UNBLOCK_ROUTING_PACK.md`
11. `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md`
12. `11_BRANCH_LINEAGE_AND_MERGE_DECISION_OPTIONS.md`
13. `12_NEXT_CONTROLLED_PROMPT_PACKS.md`
14. `13_BOSS_FINAL_GATE_PACKAGE.md`
15. `14_SHA256_MANIFEST.txt`
16. `15_SESSION_CLOSURE_SMEPLUS-26-09-02-ACC-BOSS-DECISION-LEGAL-TAX-ROUTING-001.md`

## 12. OUTPUT QUALITY RULES

Every output must include:

- Source branch and commit.
- Evidence location.
- Owner or `UNASSIGNED`.
- Status.
- Gate impact.
- Next action.
- Explicit non-claim if relevant.

Use Thai for Boss-facing summary and Thai menu/report communication. Use English technical terms only where necessary for precision.

## 13. PUBLICATION REQUIREMENTS

After outputs are written:

1. Run checksum manifest.
2. Verify `sha256sum -c`.
3. Run `git diff --check`.
4. Commit only the new output files.
5. Push to a dedicated GitHub branch.
6. Provide:
   - Repo
   - Branch
   - Commit SHA
   - Direct GitHub link to `02_BOSS_DECISION_QUEUE.md`
   - Direct GitHub link to `06_LEGAL_TAX_REVIEW_BRIEF.md`
   - Direct GitHub link to `07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md`
   - Direct GitHub link to `09_COA_G01_UNBLOCK_ROUTING_PACK.md`
   - Direct GitHub link to `13_BOSS_FINAL_GATE_PACKAGE.md`
   - Direct GitHub link to `15_SESSION_CLOSURE_SMEPLUS-26-09-02-ACC-BOSS-DECISION-LEGAL-TAX-ROUTING-001.md`

Do not open PR unless Boss explicitly orders.
Do not merge to `SMEsPlus`.
Stop at:

`BOSS FINAL DECISION REQUIRED - ROUTING PACKAGE PUBLISHED`
