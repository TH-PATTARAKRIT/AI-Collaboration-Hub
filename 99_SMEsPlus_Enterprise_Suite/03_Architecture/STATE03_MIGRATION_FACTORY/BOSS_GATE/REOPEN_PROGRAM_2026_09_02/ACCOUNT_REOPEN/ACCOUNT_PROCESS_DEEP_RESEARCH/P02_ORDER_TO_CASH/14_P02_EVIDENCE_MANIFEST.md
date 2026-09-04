# 14 — P02 EVIDENCE MANIFEST

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

## 1. Chain Of Custody

| Field | Value |
|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical branch | `SMEsPlus` — **not merged into, and not modified** |
| Working branch | `research/account-p02-order-to-cash-2026-09-04-001` |
| Base commit | `88f52cd` |
| Session clone | isolated, created for this session only |
| Direct link | `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/tree/research/account-p02-order-to-cash-2026-09-04-001` |
| Package path | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_PROCESS_DEEP_RESEARCH/P02_ORDER_TO_CASH/` |
| Jira | **No Jira issue was raised or transitioned by this session.** No Jira credential was exercised. Lineage is by branch and commit only. |
| Production code | **none written** |
| Production database | **not touched** |
| Installation / migration / deployment | **none** |
| Merge to the canonical branch | **none** |
| Reference tree | **read-only; no file modified** |

## 2. Evidence Population And Denominators

### 2.1 Primary reference source

| Field | Value |
|---|---|
| Root | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` |
| Total module directories in the root | **791** |
| Total source files in the root | **9,431** |
| Nature | reference ERP — **learning / benchmark only** |

### 2.2 The declared O2C path set

| Module role | model files | model lines |
|---|---|---|
| sales | 19 | 5,554 |
| sales management | 10 | 839 |
| sales–inventory bridge | 10 | 1,246 |
| inventory | 23 | 13,383 |
| inventory–accounting bridge | 15 | 3,143 |
| accounting | 52 | 30,127 |
| accounting (full) | 18 | 4,786 |
| delivery | 8 | 872 |
| Thai localisation | 6 | 140 |
| Thai localisation reports | 3 | 312 |
| **Total** | **164** | **60,402** |

**PATTERN** — module directories matching `sale* stock* account* delivery* l10n_th*` at the root, then
narrowed to the ten roles above by O2C relevance. **UNIT** — model file. The narrowing from the pattern
match to the ten roles **is** an author decision and is declared as such; the pattern match itself is not.

**Declared exclusions, by declaration and not by evidence:** subscriptions, point of sale, e-commerce,
rental, projects, manufacturing, deferred revenue, landed costs, payment providers, and every localisation
other than the Thai one. **Any of these could contribute an O2C-relevant event.** Where a finding depends
on one of them, it is marked `NOT YET SEARCHED`, never `VERIFIED ABSENCE`.

### 2.3 Complete enumerations claimed in this package

Each is a **closed denominator** — the population is a literal in the source, not a list the author chose.

| # | Enumeration | Count | Basis |
|---|---|---|---|
| E-01 | Order statuses | **4** | the status selection literal |
| E-02 | Movement statuses | **6** | the status selection literal |
| E-03 | Invoice-policy values | **2** | the policy selection literal |
| E-04 | Settlement-state values | **7** | the settlement-state selection literal |
| E-05 | Thai chart accounts | **27** | the chart data file, complete |
| E-06 | Thai taxes | **18** | the tax data file, complete |
| E-07 | Thai tax groups | **5** | the tax-group data file, complete |
| E-08 | Thai localisation files | **17 + 10 = 27** | directory enumeration |
| E-09 | Readers of the cost-line origin field | **4** | pattern over the whole root |
| E-10 | Lock-date field definitions | **22**, of which **5** are the substantive company locks | pattern over the whole root |
| E-11 | Lock-bypass sentinel occurrences | **5 lines, 3 files, 2 use sites** | pattern over the whole root |
| E-12 | Forced-period-date occurrences | **8 lines, 3 files** | pattern over the whole root |
| E-13 | Company-consistency flagged fields on the O2C chain | **71**, of which **31** sit on models that never auto-validate | pattern over the 13 chain files |
| E-14 | Overrides of the in-payment-state hook | **1** | pattern over all 9,431 files |
| E-15 | Withholding-tax rows in the Thai chart | **12 of 18** | the tax data file, complete |

### 2.4 Enumerations that are NOT complete, declared

| Item | Status |
|---|---|
| P02 business events (24) | Bounded by E-01, E-02 and the accounting transitions, **plus** track contributions. **Modules outside the path set are excluded by declaration.** |
| P02 accounting events (13) | Same bound. |
| Edge cases (34) | **Author-assembled from the directive's verb list plus track findings.** This is **not** a closed denominator and is not presented as one. |
| Account roles (16) | Derived from the 13 accounting events. Closed with respect to them; not closed with respect to unsearched modules. |

## 3. Evidence Identifiers

**80 evidence identifiers**, `EV-P02-001` … `EV-P02-080`, each resolving to `path:line` in
`13_P02_SOURCE_LINK_REGISTER.md`. Four track extracts carry their own citations under their own declared
denominators.

## 4. Reproducibility Statement

Every `FACT VERIFIED` in this package is reproducible by read-only shell inspection of the root in §2.1.
**No tooling, no database, no execution is required — and none was available.**

**This is the package's principal limitation.** One material question — whether cost-of-sales generation
is exploitably non-idempotent — is `UNRESOLVED — EVIDENCE REQUIRED` for exactly this reason, and the
specific reproduction that would settle it is written out in `12_P02_CONTRADICTION_REGISTER.md` C-04.

## 5. Clean-Room Control

| Control | Result |
|---|---|
| Layer classification | The package is **Layer 2 — audit quarantine**, except `19_P02_CORE_RECON_HANDOFF_PACK.md`, which is **Layer 1 — clean room**. |
| Vendor-token scan of the Layer 1 file | **Executed mechanically.** Patterns scanned: reference model prefixes, reference field prefixes, technical-method prefixes, privilege-elevation tokens, source file extensions, and the reference product name. **Result: no vendor token present.** The only pattern hits were substring false positives inside ordinary English words. |
| Verdict-vocabulary scan of the whole package | **Executed mechanically** for `PASS`, `FAIL`, `APPROVED`, `CERTIFIED`, `PRODUCTION READY`, `SIGN-OFF`. **Result: no prohibited verdict.** The only hits are the constitutional declaration itself, the phrase "none approved" on design-candidate headings, and ordinary English uses ("it cannot fail", "bypass"). |
| Thai naming | No Thai name, term or classification is asserted as validated anywhere in this package. |
| Statutory claims | **Eight Thai statutory questions, all `HOLD — STATUTORY EVIDENCE REQUIRED`, each with its sources named.** No Thai legal conclusion is stated. |
| Code transcription | No reference source code is reproduced. Citations are `path:line` plus behavioural description. Where a code fragment was necessary to establish a branch, it is three lines or fewer and appears only in the Layer-2 track extracts. |

## 6. Package Inventory And SHA-256

Generated at CP-FINAL over the package directory. Hashes are of the files as committed.
