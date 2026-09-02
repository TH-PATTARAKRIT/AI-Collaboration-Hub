# 22 — NEXT PROMPT RECOMMENDATION

| Field | Value |
|---|---|
| Session | `SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001` |
| Jira | `ERPPLUS-138` |
| Repository / Canonical Branch | `TH-PATTARAKRIT/AI-Collaboration-Hub` / `SMEsPlus` (base `788479552971940a126a542da5343944f7f3e0d4`) |
| Execution Branch | `audit/account-menu-process-deep-study-2026-09-02-001` |
| Document status | `PROCESS REFERENCE ONLY` — recommendation for Boss; nothing here is authorized until Boss decides |

`No Evidence = No Progress.` `Never Skip Gate.` `Boss is the sole Final Approver.`

## 1. What this package makes possible

The Account menu-by-menu process reference (files 02–16) now exists and has been challenged (files 17–19). It can be used as **input** for later Thai SMEsPlus accounting process design, but it cannot move any COA gate. The next controlled steps, in dependency order, are below. Each is a separate controlled prompt; none may be merged into another without a Boss decision.

## 2. Recommended next controlled actions (ordered)

| # | Recommended next prompt / action | Owner | Why now | Unblocks |
|---|---|---|---|---|
| 1 | **Boss decision batch on this package** — (a) attach or identify the menu screenshots and confirm the meaning of `Sources`; (b) rule on `l10n_th_withholding_tax_multi` module baseline (`ACC-WHT-06`) using the new instance fact that the benchmark ran without it; (c) scope decisions for Assets/Deferrals, Budgets, Treasury/Bank, Employee Expenses, Tax Returns, Cash Roundings (currently `No gate defined — BOSS SCOPE DECISION`); (d) accept or reject the Thai candidate naming register as the working vocabulary for TBRAC validation | Boss | All are Boss-only decisions surfaced by this study | Files 20 items EG-02, EG-05, SC-01..06; COA-G06 WHT path |
| 2 | **COA-G01 unblock** (unchanged from prior session): reissue `งบการเงิน 2567.pdf` access (N-04); decide N-05 / C-03; commission ChatGPT independent re-audit of CORR5; complete PMO verification | Boss / PMO / ChatGPT Audit | Every configuration handoff (HO-01) inherits G01 HOLD | COA-G02..G05 |
| 3 | **Legal-tax review prompt** — route the consolidated statutory register in file 10 §(c) (WHT 10 items + 6 engineering risks, VAT incl. Undue VAT and non-deductible input VAT, CIT/PND50, bad-debt deductibility, depreciation rates, Tax Units group filing, DBD statement format, cash-flow statement requirement for NPAEs, statutory books, legal reserve) to a licensed Thai tax/accounting adviser; output = authoritative citations per item | Boss (commission) / Legal-Tax reviewer | VAT and CIT research remain zero; every statutory claim in this package is `LEGAL_TAX_REVIEW_REQUIRED` | COA-G05, COA-G06 |
| 4 | **Account x Inventory Joint Session 3** (`ERPPLUS-140`) — trace HO-14/15/18/23 scenarios (receipt, delivery/COGS, return basis CONFLICTING, adjustment, landed cost, manufacturing, price difference), decide posting-architecture fork, close sequencing (G-1/G-2), opening-balance cross-proof (G-5), year-end RE design (G-6), category dual ownership | Boss (convene) / Joint | Inventory reopen has handed over its side (file 20 of that package); Account side now has a process map to meet it | Account + Inventory Backbone baseline HOLD |
| 5 | **TBRAC Thai user-fitness validation prompt** — validate the Thai candidate names (file 15) and the monthly close / tax calendar candidates with real Thai SME accountants and owners; record real-user evidence | TBRAC (UNASSIGNED) | Charter mandate 02 requires real-user evidence; benchmark Thai labels proven unreliable | UI vocabulary for future FDS |
| 6 | **AR/AP + Fixed Asset research pass (Team A style)** — aging semantics, allowance, write-off, subledger tie-out at cutover, asset register roll-forward, deferral schedules (prior G-B5 still open) | Team A (research) | Menus mapped but behaviour black-box; migration reconciliation cannot be signed off | MG-C11 subledger; P0-10 |
| 7 | **Treasury / Cash & Bank process reference prompt** — bank journals, statement import formats of Thai banks, reconciliation rules, cheque/PromptPay/transfer, bank-feed availability and PDPA review | Treasury (UNASSIGNED) | B03 names Treasury as a neighbour never designed; bank items in this package are `HOLD` | HO-11/HO-12 |
| 8 | **Financial statement taxonomy prompt (COA-G05)** — only after 2 and 3: map canonical accounts (19 types) to Thai NPAE statement lines; Off-Balance rule; mode labels | Team B (once G01–G04 clear) | Depends on G01 closure and DBD format evidence | COA-G05 |
| 9 | **Decision on the missing 18-deliverable Account Reopen package (G-A3)** — recreate, or accept the prior Ai Audit package plus this package as its replacement | Boss | Lineage hygiene | Evidence chain |
| 10 | **Merge decision** — whether to merge `audit/account-menu-process-deep-study-2026-09-02-001` (this package), `audit/account-ai-audit-smeplus-2026-09-02-001` and `prompt/account-menu-process-deep-study-2026-09-02` into `SMEsPlus`, or keep as unmerged evidence branches | Boss / repo owner | Three Account artefacts currently live only on unmerged branches | Discoverability from canonical branch |

## 3. What must NOT be the next prompt

- No Team B functional/UX design of accounting menus from this package alone — COA-G01 is HOLD and Thai statutory evidence is absent.
- No Team C / development / production prompt.
- No prompt that treats benchmark behaviour (Odoo) as approved SMEsPlus behaviour.
- No prompt that closes Inventory-owned or Joint items from the Account side.

## 4. Suggested prompt ID for the immediate next session

`SMEPLUS-26-09-0X-ACC-BOSS-DECISION-AND-LEGAL-TAX-ROUTING-001` — a short Boss decision + routing session consuming files 20 and 21 of this package, producing the decision record that unlocks items 2–7 above.
