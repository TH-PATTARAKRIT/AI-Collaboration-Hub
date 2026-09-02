# 20 — GAP / OWNER / GATE IMPACT REGISTER

| Field | Value |
|---|---|
| Session | `SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001` |
| Jira | `ERPPLUS-138` |
| Repository / Canonical Branch | `TH-PATTARAKRIT/AI-Collaboration-Hub` / `SMEsPlus` (base `788479552971940a126a542da5343944f7f3e0d4`) |
| Execution Branch | `audit/account-menu-process-deep-study-2026-09-02-001` |
| Document status | `PROCESS REFERENCE ONLY` — consolidated gap register; no gate moved; Boss sole Final Approver |

`No Evidence = No Progress.` `Never Skip Gate.` `Boss is the sole Final Approver.`

## 0. Vocabulary

Status: `HOLD / EVIDENCE REQUIRED` · `GAP OWNER ROUTING REQUIRED` · `BOSS DECISION REQUIRED` · `LEGAL_TAX_REVIEW_REQUIRED` · `PENDING JOINT SESSION 3` · `CARRY FORWARD`. Gate vocabulary per Boss AK (COA-G01..G08), Team B (CAP/CO/MG), `Joint Session 3` (ERPPLUS-140), `No gate defined`.

## A. Evidence gaps (EG)

| ID | Gap | Source | Owner | Verifier | Gate impact | Status |
|---|---|---|---|---|---|---|
| EG-01 | COA-G01 remains `HOLD / EVIDENCE REQUIRED — BOSS DECISION PENDING` (N-04 PDF, N-05, C-03, CORR5 re-audit, PMO) — inherited by every configuration handoff | 01 §B; prior AI Audit 08 | Boss / PMO / ChatGPT Audit | prior session | COA-G01..G04 | HOLD / EVIDENCE REQUIRED |
| EG-02 | Boss menu screenshots referenced by the prompt were not attached; Section 6 list used as transcription; `Sources` menu unidentifiable | 00 CP-02; 02 §2 | Boss | — | none | BOSS DECISION REQUIRED |
| EG-03 | Zero authoritative Thai statutory citations in the Account chain (VAT, CIT, PP30/PND/50 ทวิ forms, DBD FS format, NPAE cash-flow, statutory books, legal reserve, retention, depreciation rates, per-branch VAT, bad-debt write-off) | 18 ST-02; 10 §5; 09 §5; 12 §6; 14 OBJN-04 | Legal-Tax reviewer (UNASSIGNED) | — | COA-G05, COA-G06 | LEGAL_TAX_REVIEW_REQUIRED |
| EG-04 | OEEL-1 behaviour (reports engine, assets, follow-up, budgets, reconciliation workbench, bank sync, Tax Returns) unobservable under clean-room — all such menus mapped by label/business meaning only | 02 (38 HOLD rows); 15 RPT-02 | — | — | COA-G05 | HOLD / EVIDENCE REQUIRED (clean-room bound) |
| EG-05 | `l10n_th_withholding_tax_multi` not installed in benchmark instance while dependency present — module baseline for ACC-WHT-06 undecided | A2 §B.1; 10 | Boss / Accounting-Tax | this session (metadata) | COA-G06; ACC-WHT-06 HIGH | BOSS DECISION REQUIRED |
| EG-06 | AR/AP aging, allowance/write-off, asset register roll-forward, deferral schedules: no research performed; subledger tie-out at cutover unspecified (target G1) | 11; 12 §8; 09 RC-13; 18 ST-04 | Team A research (UNASSIGNED) | — | MG-C11; P0-10 | HOLD / EVIDENCE REQUIRED |
| EG-07 | Data-level balance of stored source entries never demonstrated (CF-01 data half; GAP-D01-11) | 14 OBJN-12 | Team A / migration lead (UNASSIGNED) | — | MG-C10 | HOLD / EVIDENCE REQUIRED |
| EG-08 | Missing 18-deliverable Account Reopen package (G-A3) and non-existent branch/commit cited in an earlier prompt (G-A1/G-A2) — unchanged | 01 §B.1 | Boss | prior session | evidence chain | HOLD / EVIDENCE REQUIRED |
| EG-09 | Independent verification of this package absent (single-session reading; sub-agent prose not re-read by a second party) | 17 VC-01/VC-09 | ChatGPT Audit role / PMO | — | none | HOLD / EVIDENCE REQUIRED |
| EG-10 | Docker-based extraction of three dump metadata tables (A1/A2) not covered by an explicit prior authorization record | 17 VC-08; A1 §A | Boss | — | none | BOSS DECISION REQUIRED (acknowledge or reject A1/A2 as evidence) |
| EG-11 | Three Account artefacts (this package, prior Ai Audit package, governing prompt) exist only on unmerged branches | 01 §A–§B | Boss / repo owner | — | discoverability | BOSS DECISION REQUIRED |

## B. Scope questions surfaced (SC) — challenge cannot add scope (Charter §9)

| ID | Item present in benchmark / implied by menus but not scoped | Source | Owner | Gate impact | Status |
|---|---|---|---|---|---|
| SC-01 | Fixed assets, depreciation, disposal (Boss lists them; no COA gate covers them) | 12 UK-02 | Boss | No gate defined | BOSS DECISION REQUIRED |
| SC-02 | Deferred revenues/expenses and recognition schedules (models absent in instance) | 12 UK-04 | Boss | No gate defined | BOSS DECISION REQUIRED |
| SC-03 | Budgets / budgetary positions / budget analysis (module not installed in instance) | 13 UK-03 | Boss | No gate defined | BOSS DECISION REQUIRED |
| SC-04 | Treasury / Cash & Bank (bank journals, statements, reconciliation rules, cheques, PromptPay, bank feeds) — neighbour never designed | 02 M-BNK-*; 18 ST-03 | Boss (assign owner) | No gate defined | GAP OWNER ROUTING REQUIRED |
| SC-05 | Employee expenses (HR -> Accounting), Tax Returns closing menu, Cash Roundings, WT Certificates menu, manufacturing valuation, price difference, inventory write-down (113900) | A1 §C.4; 08 objections 5–6; 04 HO-31 | Boss | No gate defined / Joint | BOSS DECISION REQUIRED |
| SC-06 | VAT and CIT ownership (Accounting Core vs separate Tax domain) — undecided since prior session; PND1 / PND54 / PP36 in chart but not in scope | 10 objections 7, 9; prior VC-06 | Boss | COA-G06 | BOSS DECISION REQUIRED |
| SC-07 | Approval-before-posting workflow (ACC-004 draft) — in or out | 14 OBJN-07 | Boss | CO-02 | BOSS DECISION REQUIRED |
| SC-08 | Analytic / dimension model ownership (no Team B neighbour named); branch (สาขา) as dimension vs statutory attribute | 13 objections 2, 4 | Boss / Legal-Tax | COA-G07 | GAP OWNER ROUTING REQUIRED + LEGAL_TAX_REVIEW_REQUIRED |
| SC-09 | Financial Reporting design owner (statement production is OUT neighbour, not designed) | 09 RU-08 | Boss | COA-G05 | GAP OWNER ROUTING REQUIRED |
| SC-10 | Standard COA template mechanics (B13 DT-03) — still unapproved | 17 VC-05 | Boss | COA-G04S | BOSS DECISION REQUIRED |

## C. Process / design objections carried to Boss (OB)

| ID | Objection | Source | Owner | Gate impact | Status |
|---|---|---|---|---|---|
| OB-01 | Tax-group closing accounts in the Thai template net purchase-side WHT liabilities against sales-side WHT assets — must not be inherited | 10 §2.2; 18 ST-07 | Accounting/Tax | COA-G06 | HOLD / EVIDENCE REQUIRED |
| OB-02 | Exempt-input-VAT template contradicts its own Thai description; no non-deductible input VAT; Undue VAT accounts without process | 10 objections 4, 6 | Accounting/Tax + Legal-Tax | COA-G06 | LEGAL_TAX_REVIEW_REQUIRED |
| OB-03 | Sales-side WHT: no report grid, no received-certificate tracking, no test — CIT credit chain unevidenced | 10 objection 10; WHT 02 | Accounting/Tax | COA-G06; ACC-WHT-02 | HOLD / EVIDENCE REQUIRED |
| OB-04 | Thai template `999999` current-year-earnings placeholder vs derived-RE model; designated RE account (321200) decision | 09 objection 3; 18 ST-04 | Team B / Boss at COA-G03 | COA-G03; MG-C15 | BOSS DECISION REQUIRED |
| OB-05 | Account Type alone cannot place several Thai statement lines (finance cost, CIT expense, tax receivables/payables, allowances) — COA-G05 depends on COA-G03 canonical semantics | 09 objection 2 | Team B | COA-G03/G05 | HOLD / EVIDENCE REQUIRED |
| OB-06 | Off-Balance rule 5 (engine must distinguish active type from included-in-statements) has no design artefact | 09 objection 8 | Team B / Reporting owner | COA-G05; AK handoff condition | GAP OWNER ROUTING REQUIRED |
| OB-07 | Consumption triggers for Thai document classes not enumerated (needed by CAP-03/CO-15) | 05 objection 5 | Team B | CAP-03 | HOLD / EVIDENCE REQUIRED |
| OB-08 | Hard / irreversible lock after statutory filing has no Team B counterpart; class-level locks may re-inherit fragmented shape | 14 OBJN-05/06 | Team B | CAP-04 | HOLD / EVIDENCE REQUIRED |
| OB-09 | SoD "supported, not mandated" needs a recorded compensating measure for 2-person SMEs | 14 OBJN-01 | Team B / Boss | CO-02 | HOLD / EVIDENCE REQUIRED |
| OB-10 | Backup/recovery and infrastructure tamper-resistance outside DOMAIN_01 with no located platform document | 14 OBJN-03 | Platform (UNASSIGNED) | none | GAP OWNER ROUTING REQUIRED |
| OB-11 | `TH-INV-03` deferred to COA-G06 but COA-G06 does not cover costing methods — gate scope mismatch | 08 objection 4 | Boss | COA-G06 / Joint | BOSS DECISION REQUIRED |
| OB-12 | Two parallel tracks (Inventory reopen vs prior Account Ai Audit) carry different readings of COA-G01/G02 status | 08 objection 1 | Boss | COA-G01/G02 | BOSS DECISION REQUIRED |
| OB-13 | Inventory G-2 "Accounting lock-exception model as template" — back-door inheritance risk at the Joint seam | 14 OBJN-08 | Joint / Clean-room VETO | Joint Session 3 | HOLD / EVIDENCE REQUIRED |
| OB-14 | BR-04/BR-05 identifier collision between Team A 06 and Team B B06 | 05 objection 1 | Team A / Team B | none | HOLD / EVIDENCE REQUIRED |
| OB-15 | Thai naming register unvalidated; two seed names refined without Boss instruction; กระทบยอด reserved for bank reconciliation by this session | 15 objections 1–3 | TBRAC (UNASSIGNED) / Boss | none | BOSS DECISION REQUIRED |
| OB-16 | Candidate monthly tax calendar contains no verified date — must not become design constants | 10 objection 8 | Legal-Tax | COA-G06 | LEGAL_TAX_REVIEW_REQUIRED |
| OB-17 | Thresholds (aging, approval) called "policy inputs" by analogy to CO-16 — session reasoning, not a Team B principle | 14 OBJN-10 | Team B | CO-16 | HOLD / EVIDENCE REQUIRED |
| OB-18 | Cash Flow Statement listed as Mandatory-area item while NPAE requirement unknown | 09 objection 6 | Legal-Tax / Boss | COA-G05 | LEGAL_TAX_REVIEW_REQUIRED |
| OB-19 | Rule-ID drift: Team B MG-C10 "BR-05 period validity" vs Team A BR-05 tax-country (period = BR-12) | 07 W-08; 06 | Team A / Team B | none | HOLD / EVIDENCE REQUIRED |
| OB-20 | Eight needed accounting concepts have no Thai template account (prepayment, contract liability, bad-debt expense, disposal gain/loss, stock inbound clearing, purchase variance, count difference, inter-company due-to/from); Off-Balance type has no template account | 06 §4; 07 W-09 | Team B at COA-G02/G03 | COA-G02/G03 | HOLD / EVIDENCE REQUIRED |
| OB-21 | AR/AP domain ownership undecided (B03 neighbour vs file 02 assignment vs file 11 proposal); CAP-07 applicability to received vendor documents unstated | 11 UKA-02/09 | Boss / Team B | CAP-07; no gate | BOSS DECISION REQUIRED |
| OB-22 | Source-side TB horizon for MG-C11 tie-out ambiguous (benchmark TB black-box) | 07 §4 | Migration lead (UNASSIGNED) | MG-C11 | HOLD / EVIDENCE REQUIRED |
| OB-23 | CLASS-D SMEsPlus-authored modules embody current practice invisible to this study; Boss CLASS-D ruling pending | 16 RRK-06; 11 UKA-11 | Boss | clean-room | BOSS DECISION REQUIRED |
| OB-24 | Candidate audit events in file 07 not in B04 §3 event list; G3 bridge-line Thai label invented by this session | 07 §3 | Team B | CAP-08 | HOLD / EVIDENCE REQUIRED |

## D. Joint Session 3 items (never closed here)

`N-A12-01` (full), `G-1`, `G-2`, `G-3`, `G-5`, `G-6`, posting-architecture fork, return-valuation basis (`CONFLICTING` inside Inventory first), Product Category dual ownership, multi-company transfer, company/tenant cross-domain enforcement, capitalised spare parts vs stock (12 UK-05), dimension assignment on inventory-originated lines (13 UK-06), inventory write-down (08 SC-20), manufacturing valuation. Source: 08 §4; Inventory reopen file 20. Status: `PENDING JOINT SESSION 3` (`ERPPLUS-140`).

## E. Gate impact summary

| Gate / control | Status after this session | Moved? |
|---|---|---|
| COA-G01 | HOLD / EVIDENCE REQUIRED — BOSS DECISION PENDING | No |
| COA-G02 | NOT STARTED | No |
| COA-G03 | NOT YET REACHED (OB-04/OB-05 inputs recorded) | No |
| COA-G04 / G04S | NOT YET REACHED / HOLD (SC-10) | No |
| COA-G05 | HOLD / EVIDENCE REQUIRED (EG-03, SC-09, OB-05/06, RU-01..08) | No |
| COA-G06 | HOLD / EVIDENCE REQUIRED (EG-03, EG-05, SC-06, OB-01..03) | No |
| COA-G07 | HOLD / EVIDENCE REQUIRED (SC-08) | No |
| COA-G08 | NOT YET REACHED | No |
| Account x Inventory | PENDING JOINT SESSION 3 | No |
| Assets / Deferrals / Budgets / Treasury / Analytic / HR-expense | No gate defined — BOSS SCOPE DECISION | n/a |

## F. Counts

Evidence gaps 11 · scope questions 10 · objections 24 · Joint items 15 (listed) · gates moved 0.
