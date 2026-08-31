# COA-G01 — Source Baseline Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Reconcile Evidence Universe classes A–I for COA-G01 | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | GitHub `SMEsPlus` branch @ `d57cca7`; local `SMEsPlus ENTERPRISE SUITE/ACCOUNT` folder | 2026-08-30 22:27 +0700 | ChatGPT Independent Review (pending); PMO (pending); Boss (pending) | HOLD / EVIDENCE REQUIRED (see per-class status) | Determines whether COA-G01 evidence base is complete |

## Evidence Universe reconciliation (A–I)

| Class | Description | Status | Evidence |
|---|---|---|---|
| A | Team A Deep Research / Accounting Core evidence | VERIFIED FACT (GitHub-committed evidence now fully inventoried, Round 2; local-only S1–S11/T1–T9 remains partial per C-01) | **Round 2 (2026-08-31):** full reproducible inventory of the GitHub-committed Team A evidence base — 62 markdown files / 65 files total across all cited paths, see `COA_G01_TEAM_A_SOURCE_CLASS_A_RECONCILIATION_R2.md` for the exact reproducible command and per-category (process/state-event/security/integration/edge-case/migration/data) completeness assessment. Local `STATE03` findings S1–S11 (frozen 2026-08-23), local Thai toolchain findings T1–T9 remain **not yet committed to GitHub** — see `COA_G01_SOURCE_CONFLICT_REGISTER.md` item C-01, unchanged by Round 2. |
| B | Authorized Accounting Core learning source (`account_account.py`) | VERIFIED FACT | 19-value `account_type` enumeration, lines 44–72, cited in `TEAM_B_DESIGN/.../COA_STANDARD/DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`. |
| C | Thailand localization `l10n_th` | VERIFIED FACT | `l10n_th/data/template/account.account-th.csv` — 144 rows, 15 Account Types used. Cited in the same reconciliation document. |
| D | Boss-approved `Odoo18` workbook tab | VERIFIED FACT (extraction only; raw workbook file **confirmed unrecoverable from this environment, Round 2 whole-volume search**) | 389 data rows (index 0–388), 5 columns (`id`, `name`, `reconcile`, `code`, `account_type`), 14 `account_type` labels used. Evidence commit `ae2b0719081ef9497f08e3b3e1ea8329d053cf83` (verified: "evidence(state03): inventory Odoo18 COA tab rows and columns"). **Round 2 (2026-08-31):** a whole-volume filesystem search (not just the local-folder search Round 1 performed) found the source `.xlsx` nowhere on this machine, no Drive-sync cache, no hash of the file itself — see `COA_G01_WORKBOOK_PROVENANCE_AND_ROW_LINEAGE_R2.md` for the full reproducible search and its effect on commit `c530138`'s unverified "direct re-verification" claim. This remains logged as a traceability gap (`COA_G01_OPEN_UNKNOWN_REGISTER.md` N-01), now independently reconfirmed rather than merely asserted. |
| E | Boss-provided Thai COA business requirements | EVIDENCE_MISSING | No file matching this description was found in GitHub or the local `ACCOUNT` folder. The nearest substitute is the evidence-derived S1–S11/T1–T9 behavior-statement pack (class A), which is explicitly a *behavior observation* record, not a Boss-issued requirements document. Do not treat S1–S11/T1–T9 as a substitute for E without Boss confirmation. |
| F | Boss-provided Thai financial-statement presentation evidence | EVIDENCE_MISSING (confirmed absent, not inferred) | Local `ACCOUNT` folder docx sources (`Accounting Module Overview.docx`, `Accounting_Module_Technical_Review_v1.docx`, working-pack reports) name report types (Trial Balance, Balance Sheet, P&L, etc.) but contain no actual Thai statement layout/example. Whole-tree search for Thai-language financial statement terms (งบดุล, งบกำไรขาดทุน, งบการเงิน) returned no genuine Thai-source hits — only non-Thai vendor localization files already excluded from scope. Per session control, this is retained as EVIDENCE_MISSING and **must not be fabricated or inferred**. |
| G | Existing Boss rulings, PMO evidence, ChatGPT audit evidence | VERIFIED FACT (genuine artifacts); **one purported item in this class explicitly excluded, Round 2** | 23 `BOSS_GATE`/`CHATGPT_AUDIT`/`PMO_VERIFICATION` documents read in full on the `SMEsPlus` branch (see `COA_G01_EVIDENCE_MANIFEST.md` for the full list), plus the full 18-round `CHATGPT_AUDIT/` chronology and 4-file `PMO_VERIFICATION/` set read in Round 2. **Not included in this class:** commit `c530138`'s inline "ChatGPT Independent Evidence Review = PASS" declaration — investigated and classified `CONFLICTING EVIDENCE / UNVERIFIED SELF-DECLARED RESULT` (`COA_G01_SOURCE_CONFLICT_REGISTER.md` C-07); it does not meet this class's evidentiary bar (no separate reviewer, no PMO artifact, no Jira record). |
| H | Primary Thai regulatory sources (where statutory facts are claimed) | NOT INVOKED AT THIS GATE | COA-G01 is a source-baseline classification Gate (see Gate-appropriate evidence boundary). No statutory fact requiring primary Revenue Department verification is asserted as VERIFIED FACT by this remediation pass; where Thai statutory behavior is cited (e.g. WHT-at-payment recognition, S2), it is cited as a **source-system behavior observation** (class A/C), not as an independently verified statutory rule. Primary regulatory verification is deferred to `COA-G06 — Thailand Tax Accounting Controls`. |
| I | Authoritative cloud/security sources (generic SaaS facts) | NOT INVOKED AT THIS GATE | No generic SaaS/cloud architecture fact requiring external authoritative citation was asserted as VERIFIED FACT by this remediation pass. Deferred to `COA-G04S`. |

## Headline source-count facts (Boss-controlled; must not be re-derived or altered here)

| Fact | Status | Source |
|---|---|---|
| Core Accounting source model exposes 19 available Account Types | VERIFIED FACT | `account_account.py` lines 44–72 |
| `l10n_th` template instantiates 15 of those 19 types across 144 rows | VERIFIED FACT | `DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md` |
| Boss-approved `Odoo18` workbook tab uses 14 Account Type labels across 389 rows | VERIFIED FACT | `DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`, commit `ae2b0719...` |
| SMEsPlus Local Thailand target = 19 ACTIVE Account Types | BOSS RULING (APPROVED WITH CONTROL) | `BOSS_GATE/..._AJ_BOSS_ACCOUNT_TYPE_19_ACTIVE_RULING.md` |
| `389 source rows != 389 target accounts` | BOSS RULING | Repeated verbatim across AL, AM, AN, AP |
| `~32 Base Kernel` | WORKING EXPECTATION ONLY | `TEAM_B_DESIGN/.../COA_STANDARD/DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md` |
| Exact Base Kernel count | TBD / EVIDENCE REQUIRED | same |
| Exact final Standard Thai COA count | TBD / EVIDENCE REQUIRED | same |

No figure in this table has been altered, rounded, or resolved by this session. Values marked TBD remain TBD.
