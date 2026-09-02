# 01 — PRIOR EVIDENCE AND LINEAGE REGISTER

| Field | Value |
|---|---|
| Session | `SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001` |
| Jira | `ERPPLUS-138` |
| Repository / Canonical Branch | `TH-PATTARAKRIT/AI-Collaboration-Hub` / `SMEsPlus` (base `788479552971940a126a542da5343944f7f3e0d4`) |
| Execution Branch | `audit/account-menu-process-deep-study-2026-09-02-001` |
| Mode | `READ ONLY / PROCESS BENCHMARK / CLEAN-ROOM / EVIDENCE-FIRST / L999.999` |
| Purpose | CP-01 output: which prior Account findings are usable for a menu-by-menu process study, which are insufficient, and what the prior Account terminal state is (kept `HOLD / EVIDENCE REQUIRED` unless Boss changes it). |

`No Evidence = No Progress.` `Never Skip Gate.` `Boss is the sole Final Approver.`

## A. Governing prompt lineage (verified this session)

| Item | Location | Commit | Verified |
|---|---|---|---|
| This session's governing prompt (published by Boss/PMO) | `BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/03_NEW_SESSION_PROMPT_SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001.md` | `d21a856d854deacd17d6f29cefbaca4425c72737` on `origin/prompt/account-menu-process-deep-study-2026-09-02` (2026-09-02 09:10 +0700), not yet merged to `SMEsPlus` | Yes — file identical in substance to the prompt received in chat; contains one reference to "provided screenshots" (line 391) but no attachments |
| Full Reopen Program | `BOSS_GATE/REOPEN_PROGRAM_2026_09_02/STATE03_BOSS_ACCOUNT_INVENTORY_FULL_REOPEN_PROGRAM_2026_09_02.md` | `42e04e639f2c83aeef6d7c313152a55170a4c6ef` (per prior session verification) | Present on base commit |
| Account Reopen pre-prompt 9-Veto challenge + new session prompt | `BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/00_*.md`, `01_*.md` | on base commit | Present |
| 9 Veto Council & Special Team Charter | `00_Project_Governance/NINE_VETO_COUNCIL_AND_SPECIAL_TEAM_CHARTER.md` | on base commit | Read — nine mandates used verbatim in files 17/18 |
| Reopen session package index | `BOSS_GATE/REOPEN_SESSIONS/2026_09_02/00_REOPEN_ACCOUNT_INVENTORY_SESSION_PACKAGE_INDEX.md` | on base commit | Read — names the 4 AI Expert overlay lenses (functional design, database design, integration/localization, code/UI) and the Joint session |

## B. Prior Account Ai Audit session (immediately preceding this one)

| Item | Value |
|---|---|
| Session | `SMEPLUS-26-09-02-ACC-AI-AUDIT-SMEPLUS-001` |
| Branch / commit | `origin/audit/account-ai-audit-smeplus-2026-09-02-001` @ `356c151` ("Add AI Audit SMEsPlus execution package for Account investigation"), local clone `ISOLATED_ACCOUNT_CORR5` — **not merged to `SMEsPlus`** |
| Package | `REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/AI_AUDIT_SMEPLUS_EXECUTION/` — 14 files + SHA-256 manifest |
| Terminal state recorded | **`HOLD / EVIDENCE REQUIRED`** (file 12) — retained unchanged by this session |
| Gate status recorded (file 08) | COA-G01 `HOLD / EVIDENCE REQUIRED — BOSS DECISION PENDING`; COA-G02 `NOT STARTED`; COA-G03 `NOT_YET_REACHED`; COA-G04..G08 `NOT_YET_REACHED` / `HOLD`; Account x Inventory `PENDING JOINT SESSION` |

### B.1 Usability classification of prior findings for a menu-by-menu process study

| Prior finding (source) | Classification for this study | Why |
|---|---|---|
| P0-5/6/7 monthly close, FY close, retained earnings resolved at design level (Team B B02/B07, Rounds 2-7) | `CARRY FORWARD — VERIFIED / NO MATERIAL DELTA` | Independently audited design principles; reused directly for M-CTL-02/04/05 and HO-19..23 |
| P0-8 Account x Inventory boundary principle resolved; scenarios (landed cost/returns/adjustments) untraced | `CARRY FORWARD — VERIFIED WITH PRECISION NOTE` | Principle reused for M-STK-10 / HO-14; scenario gaps carried as HOLD, now with Inventory reopen evidence (files 12/14/20) added |
| P0-2/3/4 WHT purchase PARTIAL, sales PARTIAL, multi-rate HIGH, 50 ทวิ 5 fields, PND3/53 monkey-patch (WHT branch) | `CARRY FORWARD — VERIFIED WITH PRECISION NOTE` | Reused for M-INV-04, M-ARP-06, M-RPT-08, OBJ-26..29; **new delta this session**: benchmark instance did not have `l10n_th_withholding_tax_multi` installed (A2) |
| P0-11 clean-room compliance rigorous (B14, quarantine registers) | `CARRY FORWARD — VERIFIED` | Quarantine rules applied verbatim: OEEL-1 bodies never opened; only manifest metadata and menu labels used |
| P0-12 AI control at governance level | `CARRY FORWARD — VERIFIED` | This package is a proposal; Boss remains sole approver |
| G-B1 VAT/CIT zero research | `REVALIDATE — NEW MATERIAL DELTA` | This study reads the LGPL Thai tax templates and PP30 grid line names (new evidence) but still performs **no statutory verification** — VAT/CIT remain `HOLD` |
| G-B5 AR/AP aging and asset roll-forward no research | `REVALIDATE — NEW MATERIAL DELTA` | Menus mapped (M-ARP-07..11, M-AST-*) with benchmark evidence of existence; behaviour black-box; research still absent |
| G-A3 missing 18-deliverable Account Reopen package | `HOLD / EVIDENCE REQUIRED` | Unchanged; not recreated |
| G-A1/G-A2 non-existent branch / commit `fc468ed` cited in the earlier governing prompt | `HOLD / EVIDENCE REQUIRED` | Unchanged; this session's prompt cites no such artefacts |
| VC-01 stale root-level `03_Architecture/STATE03_MIGRATION_FACTORY/` copy | `CARRY FORWARD — CONFIRMED` | Root copy again observed stale; not used |

### B.2 Why the prior rounds are insufficient for a process study (Boss's corrective premise, confirmed)

1. Prior rounds studied gates, evidence chains and contradictions; **no prior deliverable enumerates accounting menus** or maps input -> action -> output -> handoff per menu.
2. Team A Accounting Core registers (03/04/05/11/13/14/15/16) cover the readable posting core only; every Enterprise menu (reports, assets, follow-up, budgets, reconciliation workbench, bank sync) is `OEEL-1 BLACK-BOX` — the process view had never been assembled from the instance itself.
3. No prior deliverable produced Thai candidate names for menus/reports; the only Thai-language functional lineage is the STATE04-era draft `02_Functional_Design/ACC-001..005` (status `DRAFT / HOLD`, not Boss-approved).

## C. Prior evidence base loaded and used (with usability)

| Evidence | Path (relative to `03_Architecture/STATE03_MIGRATION_FACTORY/` unless stated) | Used for | Usability |
|---|---|---|---|
| Team A Accounting Core research (25 registers + DB registers) | `TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/` | posting core facts (states, rules, locks, automation, integration, config, reports touchpoints) | Usable — readable core only |
| Team A quarantine | `TEAM_A/05_QUARANTINE/CLEAN_ROOM_QUARANTINE_REGISTER.md`; `.../21_QUARANTINE_REGISTER.md` | licence boundaries for this study | Usable — binding |
| Team B Accounting Core blueprint (B00–B24, CORR rounds) | `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/` | SMEsPlus candidate principles (CAP-01..09, CO-01..16, MG-C01..16, B07 equity/fiscal model) | Usable — `APPROVE WITH CONTROL` (Boss AH), design only |
| Boss rulings AJ (19 active types, Off-Balance rule) and AK (COA-G01..G08 definitions) | `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AJ_*.md`, `AK_*.md` | gate mapping, account-type baseline | Usable — Boss authority |
| WHT closure branch (9 deliverables + manifest) | `origin/audit/account-wht-grpa-m18-closure-010` `TEAM_ACCOUNT/ACCOUNTING_TAX_WHT/GRPA_M18_CLOSURE/EXECUTION/` | WHT process map (file 10), OBJ-26..29 | Usable — Boss Partial Acceptance; unmerged branch |
| Inventory Reopen execution (20 files) | `origin/audit/inventory-reopen-2026-09-02-inv-reopen-001` `REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/EXECUTION/` (files 12, 14, 20 read) | stock/COGS boundary (file 08) | Usable — unmerged; Inventory-owned conclusions |
| CORR-007B clean-room learning files 08/09 | `origin/audit/inventory-core-corr007b-3high-closure-010` `INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/` | period close / category valuation learning | Usable — remediated clean-room versions |
| Draft Thai FDS lineage | `99_SMEsPlus_Enterprise_Suite/02_Functional_Design/ACC-001..ACC-005` | Thai naming lineage only (file 15) | Draft / HOLD — not authority |
| Community `account` menu XML | external `ACCOUNT/01 ACCOUNT/SOURCE CODE/01 ACCOUNT/account/views/account_menuitem.xml` (LGPL-3) | menu label evidence | Usable — labels only, no design reuse |
| Thai localization templates | external `.../02 OTHER/l10n_th/data/template/*.csv`, `data/account_tax_report_data.xml` (LGPL-3) | tax/account/asset template facts (file 09/10/12) | Usable — business facts only |
| Thai WHT addons readme (business description) | external `.../addons_extra/l10n_th_withholding_tax*/readme/*.rst` (AGPL-3) | WHT process description | Usable — description level |
| OEEL-1 module manifests | external `.../01 ACCOUNT/<module>/__manifest__.py` (name/summary/depends/licence only) | module attribution (A2, file 02) | Metadata only — bodies never opened |
| Benchmark instance dump metadata | external `iTEST02_2026-06-14_14-41-19.dump` -> `ir_ui_menu`, `ir_module_module`, `ir_act_window` (metadata tables only) | A1/A2 appendices; file 02 coverage | Usable — no business rows extracted; temporary copy deleted |
| `ACCOUNT/01 ACCOUNT/Accounting Module Overview.docx`, `Accounting_Module_Technical_Review_v1.docx` | external, root corpus | early Thai overview (0 embedded images — **no screenshots found**) | Low — superseded narrative |
| STEP040304 Thailand Functional Evidence | external `ACCOUNT/01 ACCOUNT/STEP040304_DEEP_RESEARCH/02_FUNCTIONAL_EVIDENCE/` | WHT/PND/partner identity facts (FE1–FE8) | Usable — prior clean-room learning |

## D. Evidence explicitly NOT available to this session

| Item | Consequence |
|---|---|
| Boss's menu screenshots referenced in prompt §9 CP-02 | Not attached; Section 6 list treated as the transcription; instance menu tree (A1) used as the checklist source; recorded as `EG-02` in file 20 |
| `งบการเงิน 2567.pdf` (N-04) | Thai statutory financial-statement format remains unevidenced — COA-G05 stays HOLD |
| Any Thai Revenue Department / DBD specification | Statutory correctness of PP30 / PND / 50 ทวิ / FS layouts remains `LEGAL_TAX_REVIEW_REQUIRED` |
| Behaviour of OEEL-1 modules (reports, assets, follow-up, reconciliation workbench, bank sync, budgets) | Menus mapped by label and business meaning only; behaviour `HOLD` |

## E. Prior Account terminal state

`HOLD / EVIDENCE REQUIRED` — carried forward unchanged. This session adds a process-reference layer; it does not move any COA gate.
