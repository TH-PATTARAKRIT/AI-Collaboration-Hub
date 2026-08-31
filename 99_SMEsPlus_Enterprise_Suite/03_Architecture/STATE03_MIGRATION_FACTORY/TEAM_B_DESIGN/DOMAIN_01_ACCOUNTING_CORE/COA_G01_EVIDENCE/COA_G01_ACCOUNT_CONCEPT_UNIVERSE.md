# COA-G01 — Account Concept Universe

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Reconcile every significant accounting concept with Tenant/Company Context relevance | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | GitHub `SMEsPlus` branch; local `ACCOUNT` folder | 2026-08-30 22:27 +0700 | ChatGPT Independent Review (pending); Boss (pending) | HOLD / EVIDENCE REQUIRED (see per-concept status) | Feeds COA-G02/G03 base-kernel and consolidation work; does not itself select a base kernel |

Per the Boss SaaS Context Clarification (`BOSS_GATE/..._AQ_...md`), every concept below is tagged with its **Tenant Context relevance** and **Company Context relevance** in addition to its accounting classification. This register does not select Base Kernel candidates (see `COA_G01_BASE_KERNEL_CANDIDATE_INPUT.md`) — it only classifies the concept universe itself.

## Concept-level reconciliation

| Concept | Accounting Type family (of the 19 approved) | Tenant Context relevance | Company Context relevance | Fact status | Evidence |
|---|---|---|---|---|---|
| Receivable | Receivable | Not tenant-owned data itself (a posting account); operations against it are Company-scoped | Mandatory | VERIFIED FACT | Core source enum + `AJ` ruling |
| Bank and Cash | Bank and Cash | n/a (account definition) | Mandatory | VERIFIED FACT | Core source enum + `AJ` |
| Current Assets / Non-current Assets | Current Assets, Non-current Assets | n/a | Mandatory | VERIFIED FACT | Core source enum + `AJ` |
| Prepayments | Prepayments | n/a | Mandatory | VERIFIED FACT | Core source enum + `AJ` |
| Fixed Assets | Fixed Assets | n/a | Mandatory | VERIFIED FACT | Core source enum + `AJ` |
| Payable | Payable | n/a | Mandatory | VERIFIED FACT | Core source enum + `AJ` |
| Credit Card | Credit Card | n/a | Mandatory | VERIFIED FACT | Core source enum + `AJ` |
| Current Liabilities / Non-current Liabilities | Current Liabilities, Non-current Liabilities | n/a | Mandatory | VERIFIED FACT | Core source enum + `AJ` |
| Equity / Current Year Earnings | Equity, Current Year Earnings | n/a | Mandatory | VERIFIED FACT | Core source enum + `AJ` |
| Income / Other Income | Income, Other Income | n/a | Mandatory | VERIFIED FACT | Core source enum + `AJ` |
| Expenses / Other Expenses / Depreciation / Cost of Revenue | Expenses, Other Expenses, Depreciation, Cost of Revenue | n/a | Mandatory | VERIFIED FACT | Core source enum + `AJ` |
| Off-Balance Sheet | Off-Balance Sheet | n/a | Mandatory; excluded from ordinary BS/P&L totals by default (Boss ruling) | VERIFIED FACT | `AJ`; session prompt §7 |
| Account Code / Account Name | (attribute, not a type) | Not canonical identity at any context level | Not canonical identity at any context level | BOSS RULING (SI-05) | Repeated across `AG`, `AJ`, `AL`, `AO`, `AP` |
| Account Group | (Company-maintainable grouping) | n/a | Company-maintainable, but must not redefine Account Type or canonical meaning | BOSS RULING | Session prompt §7; `AL` SI-09 |
| Financial Statement Mapping | (cross-cutting) | n/a | Independent from Company Account Group | BOSS RULING | Session prompt §7 |
| Standard Thai COA Template | (Platform-level artifact, not an account type) | **Platform Context** — must not be tenant-owned mutable data (SI-03) | Company COA Instance is derived from it, not the reverse | BOSS RULING (SI-03/SI-04) + AQ clarification | `AG` §4; AQ ruling |
| Tax Branch (sub-Company entity) | (organizational, not an account type) | Mandatory where Thai statutory filing applies | Mandatory — Company Context alone (2-level) is insufficient for Thai filing | VERIFIED FACT (ported to GitHub, CORR4 — `COA_G01_LOCAL_STATE03_SOURCE_PORT_MANIFEST_R4.md`; C-01 RESOLVED) | Local finding S5 |
| WHT recognition timing (at payment, not invoice) | Affects Payable/Receivable posting behavior | n/a | Company-scoped posting rule | VERIFIED FACT (ported to GitHub, CORR4 — `COA_G01_LOCAL_STATE03_SOURCE_PORT_MANIFEST_R4.md`; C-01 RESOLVED) | Local finding S2 |
| Thai statutory reference data (WHT income types/rates/conditions) | Cross-cutting configuration, not a fixed account type | Should be Platform-published versioned reference data (supports SI-10) | Company may reference but should not fork | VERIFIED FACT (ported to GitHub, CORR4 — `COA_G01_LOCAL_STATE03_SOURCE_PORT_MANIFEST_R4.md`; C-01 RESOLVED); classification as "must be versioned data, not code" is a design implication, not itself Boss-ruled yet | Local finding S4 |
| Thai party identity (tax ID + tax branch + Thai company title) | Party/master-data concept, not an account type | n/a | Company-scoped master data | VERIFIED FACT (ported to GitHub, CORR4 — `COA_G01_LOCAL_STATE03_SOURCE_PORT_MANIFEST_R4.md`; C-01 RESOLVED) | Local finding S3 |

## ROUND 2 UPDATE (2026-08-31): relationship to `COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md`

This document defines the **concept universe** (which concepts exist and their Tenant/Company Context relevance) and remains authoritative for that scope. `COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md` (new, Round 2) is the authoritative document for the **full 17-field completeness** required by AS §8.7 (Source, Source Evidence, Business Meaning, Thailand Relevance, Account Type, Financial Class, Normal Balance, Reconciliation behaviour, Tax relevance, FS relevance, System/control dependency, Base Kernel candidacy, Canonicalization relevance, Evidence strength, **Evidence Character and Fact Status kept as two distinct, non-merged fields per CORR1**, Conflict/Gap/Unknown, Clean-room status) for each of the 19 Account Types. The two documents do not duplicate authority: this file scopes *what* the concepts are; the Round 2 completeness document scopes *every mandatory fact about each one*.

## Explicitly out of scope for this concept universe

- Row-level mapping of the 389 Odoo18 workbook rows to canonical SMEsPlus accounts — that is COA-G03 (AI Semantic Consolidation) work, not COA-G01.
- Selection of the Base Kernel accounts — see `COA_G01_BASE_KERNEL_CANDIDATE_INPUT.md`, which supplies candidate input only, not a decision.
- Any statement that a concept above is "the same as" or "maps one-to-one with" any Odoo/`l10n_th` model, table, or field name — clean-room rules forbid asserting structural equivalence; only business meaning is carried forward.
