# 02 — BOSS DECISION QUEUE

| Field | Value |
|---|---|
| Session | `SMEPLUS-26-09-02-ACC-BOSS-DECISION-LEGAL-TAX-ROUTING-001` |
| Built from | Source `21_BOSS_FINAL_GATE_PACKAGE.md` §6; source `22_NEXT_PROMPT_RECOMMENDATION.md` §2; source `20_GAP_OWNER_GATE_IMPACT_REGISTER.md` §A–C |
| Source branch / commit | `audit/account-menu-process-deep-study-2026-09-02-001` / `5183e9f6ef4272e68c65d831580886e341118d53` |
| Purpose | Convert every open Boss-only item from the source package into a stable, trackable decision record. This queue decides nothing itself. |

`No Evidence = No Progress.` `Never Skip Gate.` `Boss is the sole Final Approver.`

Mandatory decision groups covered: **(1)** A1/A2 acknowledgement, **(2)** screenshots/`Sources` menu, **(3)** WHT module baseline, **(4)** SC-01..SC-10, **(5)** legal-tax review commissioning, **(6)** unmerged artefacts / G-A3 lineage, **(7)** COA-G01 unblock. Two additional Boss-routing items surfaced by source files 21/22 (Thai naming acceptance, Joint Session 3 convening) are included for completeness.

## Decision queue

| Decision ID | Source Item | Decision Required | Decision Authority | Evidence Required | Current Status | Gate Impact | Recommended Next Action | Output Needed |
|---|---|---|---|---|---|---|---|---|
| `ACC-DEC-001` | 20 EG-10; 21 §6.1; A1 §A | Acknowledge or reject Docker-based dump-metadata extraction (files A1/A2) as valid evidence | Boss | Prior authorization record for the extraction method, or Boss's explicit after-the-fact acceptance | `BOSS DECISION REQUIRED` | None directly; underlies all menu-tree facts in 02/03/05 | Boss reviews `03_EVIDENCE_ACCEPTANCE_DECISION_FORM.md` and checks Accept or Reject | Signed evidence acceptance form |
| `ACC-DEC-002` | 20 EG-02; 21 §6.2; 22 #1a | Identify/attach the menu screenshots referenced by the governing prompt; confirm what the `Sources` menu is | Boss | The original screenshot files, or a statement that none exist and file 02/05 transcription stands as the record | `BOSS DECISION REQUIRED` | None | Boss supplies screenshots or confirms transcription-only basis | Screenshot files or written confirmation, appended to `02_ACCOUNT_MENU_COVERAGE_REGISTER.md` provenance |
| `ACC-DEC-003` | 20 EG-05; 21 §6.3; 22 #1b | Rule on `l10n_th_withholding_tax_multi` as the WHT module baseline for `ACC-WHT-06`, given the benchmark instance ran WHT **without** it | Boss / Accounting-Tax | Confirmation of whether SMEsPlus WHT design should assume multi-rate WHT as in-scope, or single-rate as observed | `BOSS DECISION REQUIRED` | `COA-G06`; `ACC-WHT-06` (HIGH) | Boss reviews `04_ACC_WHT_06_MODULE_BASELINE_DECISION_PACK.md` and selects a baseline | Module baseline decision record |
| `ACC-DEC-004` | 20 SC-01 | Scope ruling: Fixed assets, depreciation, disposal | Boss | None beyond Boss's own scope intent (no COA gate currently covers this area) | `BOSS DECISION REQUIRED` | No gate defined | Boss marks IN / OUT / DEFERRED in `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` | Scope ruling, gate assignment if IN |
| `ACC-DEC-005` | 20 SC-02 | Scope ruling: Deferred revenues/expenses and recognition schedules | Boss | Same as above | `BOSS DECISION REQUIRED` | No gate defined | Same as `ACC-DEC-004` | Scope ruling |
| `ACC-DEC-006` | 20 SC-03 | Scope ruling: Budgets / budgetary positions / budget analysis | Boss | Same as above | `BOSS DECISION REQUIRED` | No gate defined | Same as `ACC-DEC-004` | Scope ruling |
| `ACC-DEC-007` | 20 SC-04 | Owner assignment: Treasury / Cash & Bank (never designed as a neighbour domain) | Boss | Candidate owner name (Team B / Treasury-specific role) | `GAP OWNER ROUTING REQUIRED` | No gate defined | Boss assigns an owner in `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §Treasury | Owner assignment |
| `ACC-DEC-008` | 20 SC-05 | Scope ruling: Employee expenses (HR→Accounting), Tax Returns closing menu, Cash Roundings, WT Certificates menu, manufacturing valuation, price difference, inventory write-down (113900) | Boss | Scope decision per item (may split across several) | `BOSS DECISION REQUIRED` | No gate defined / Joint | Boss rules item-by-item in `05` | Scope ruling(s) |
| `ACC-DEC-009` | 20 SC-06; 10 objections 7, 9 | Ownership ruling: VAT and CIT (Accounting Core vs a separate Tax domain); scope status of PND1/PND54/PP36 | Boss | Organizational decision on domain split | `BOSS DECISION REQUIRED` | `COA-G06` | Boss rules in `05`; feeds `06_LEGAL_TAX_REVIEW_BRIEF.md` scope | Ownership ruling |
| `ACC-DEC-010` | 20 SC-07; 14 OBJN-07 | In/out ruling: approval-before-posting workflow (`ACC-004` draft) | Boss | None beyond Boss intent | `BOSS DECISION REQUIRED` | `CO-02` | Boss rules IN/OUT in `05` | Scope ruling |
| `ACC-DEC-011` | 20 SC-08; 13 objections 2, 4 | Ownership ruling: analytic/dimension model; branch (สาขา) as dimension vs statutory attribute | Boss / Legal-Tax | Legal-tax input on whether branch is a statutory reporting unit in Thailand (feeds `06`) | `GAP OWNER ROUTING REQUIRED` + `LEGAL_TAX_REVIEW_REQUIRED` | `COA-G07` | Boss assigns owner in `05`; Legal-Tax reviewer addresses branch statutory status in `06` | Ownership ruling + legal-tax citation |
| `ACC-DEC-012` | 20 SC-09; 09 RU-08 | Owner assignment: Financial Reporting design (statement production is an OUT neighbour, not yet designed) | Boss | Candidate Team B owner | `GAP OWNER ROUTING REQUIRED` | `COA-G05` | Boss assigns owner in `10` §Financial Statement Taxonomy | Owner assignment |
| `ACC-DEC-013` | 20 SC-10; 17 VC-05 | Approval ruling: Standard COA template mechanics (`B13 DT-03`) — still unapproved | Boss | None beyond Boss's own prior-round decision record | `BOSS DECISION REQUIRED` | `COA-G04S` | Boss rules APPROVE / REJECT / MODIFY in `05` | Ruling on template mechanics |
| `ACC-DEC-014` | 20 EG-03; 21 §6.5; 22 #3 | Commission a licensed Thai legal-tax/accounting review of the consolidated statutory register (WHT, VAT, CIT, DBD/NPAE items) | Boss | Named reviewer or firm; engagement terms | `LEGAL_TAX_REVIEW_REQUIRED` | `COA-G05`, `COA-G06` | Boss commissions the review using `06_LEGAL_TAX_REVIEW_BRIEF.md` as the brief | Signed engagement + reviewer output (citations) |
| `ACC-DEC-015` | 22 #1d, #5; 15 objections 1–3 | Accept/reject the Thai candidate naming register (source file 15, 151 candidates) as the working vocabulary to submit for TBRAC validation; commission TBRAC validation | Boss / TBRAC (UNASSIGNED) | TBRAC reviewer roster (Thai accountants + SME owners) | `BOSS DECISION REQUIRED` (acceptance) then `ROUTING REQUIRED` (TBRAC roster) | UI vocabulary for future FDS; no gate directly | Boss accepts/rejects vocabulary as working draft; assigns/recruits TBRAC panel per `08_TBRAC_THAI_NAMING_VALIDATION_BRIEF.md` | Acceptance record + TBRAC panel roster |
| `ACC-DEC-016` | 20 EG-11; 21 §6.6; 22 #10 | Merge/lineage decision for the three unmerged Account artefacts (this package's predecessor, the prior Ai Audit package, the governing prompt file) | Boss / repo owner | None beyond Boss's own governance intent | `BOSS DECISION REQUIRED` | Discoverability from canonical branch; no COA gate | Boss selects an option in `11_BRANCH_LINEAGE_AND_MERGE_DECISION_OPTIONS.md` | Merge/lineage decision record |
| `ACC-DEC-017` | 20 EG-08; 22 #9 | Decision on the missing 18-deliverable Account Reopen package (`G-A3`): recreate it, or accept the prior Ai Audit package plus the menu-process-deep-study package as its replacement | Boss | None beyond Boss's own governance intent | `HOLD / EVIDENCE REQUIRED` | Evidence chain | Boss selects an option in `11` | Lineage decision record |
| `ACC-DEC-018` | 20 EG-01; 21 §6.7; 22 #2 | Unblock `COA-G01`: reissue/restore access to `งบการเงิน 2567.pdf` or equivalent source evidence (N-04); resolve N-05 and C-03; commission independent re-audit for CORR5; complete PMO verification | Boss / PMO / ChatGPT Audit | The PDF (or equivalent statutory source), N-05/C-03 resolution record, re-audit output, PMO checklist sign-off | `COA-G01 HOLD / EVIDENCE REQUIRED` (unchanged) | `COA-G01` → blocks `COA-G02`–`G05` | Boss and PMO execute `09_COA_G01_UNBLOCK_ROUTING_PACK.md` | Restored evidence + PMO checklist + re-audit record |
| `ACC-DEC-019` | 22 #4 | Convene Account x Inventory Joint Session 3 (`ERPPLUS-140`) | Boss | Inventory-side counterpart availability (Inventory reopen package already handed over its side per source file 20) | `PENDING JOINT SESSION 3` | Account + Inventory Backbone baseline HOLD | Boss convenes using `07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md` as the agenda | Joint session scheduled + attendee list |

## Coverage check

- Mandatory group 1 (A1/A2): `ACC-DEC-001` ✓
- Mandatory group 2 (screenshots/`Sources`): `ACC-DEC-002` ✓
- Mandatory group 3 (WHT module baseline): `ACC-DEC-003` ✓
- Mandatory group 4 (SC-01..SC-10): `ACC-DEC-004`–`ACC-DEC-013` ✓ (10 of 10)
- Mandatory group 5 (legal-tax review commissioning): `ACC-DEC-014` ✓
- Mandatory group 6 (unmerged artefacts / G-A3 lineage): `ACC-DEC-016`, `ACC-DEC-017` ✓
- Mandatory group 7 (COA-G01 unblock): `ACC-DEC-018` ✓
- Additional: naming acceptance/TBRAC (`ACC-DEC-015`), Joint Session 3 convening (`ACC-DEC-019`)

**19 of 19 rows populated. 0 decisions made by this session — every row is `BOSS DECISION REQUIRED`, `GAP OWNER ROUTING REQUIRED`, or `HOLD / EVIDENCE REQUIRED`.**
