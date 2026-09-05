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
| Subdirectories in the root | **791** |
| …of which carry a module manifest | **790** — the figure “791 modules” used in an earlier draft was one too many; corrected after independent challenge |
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
| E-16 | Delivered-quantity derivation methods | **5** | the base selection plus three independent extensions, pattern over the sales module family |
| E-17 | Writers of the valuation-layer ↔ accounting-line link | **1**, on the purchase side | pattern over the whole root, tests excluded |
| E-18 | Places exposing the split-recognition toggle to a user | **1**, in an Enterprise module | pattern over the whole root |
| E-19 | Thai VAT taxes carrying a tax group | **2 of 6** | the tax data file, complete |

### 2.4 Enumerations that are NOT complete, declared

| Item | Status |
|---|---|
| P02 business events (24) | Bounded by E-01, E-02 and the accounting transitions, **plus** track contributions, **plus** the path set declared in §2.2. **Modules outside that path set are excluded by declaration.** Drop-shipping and credit control (challenge findings CH-21, CH-22) would each add events and are **not** included. |
| P02 accounting events (13) | Same bound. |
| Edge cases (37) | **Author-assembled from the directive's verb list plus track findings.** **Not** a closed denominator and not presented as one. The independent challenge named **eight further situations with no case**: drop-shipping, credit control, period-end unrealised FX revaluation, bill-and-hold, outbound consignment, warranty/return provision at point of sale, freight charges and their tax treatment, and serial/lot-identified cost of sales. **All eight are accepted as gaps and none is closed.** |
| Account roles (16) | Derived from the 13 accounting events. Closed with respect to them; not closed with respect to unsearched modules. |

## 3. Evidence Identifiers

**101 evidence identifiers**, `EV-P02-001` … `EV-P02-101` — of which `EV-P02-081` … `EV-P02-101` were added during and after the independent challenge, each resolving to `path:line` in
`13_P02_SOURCE_LINK_REGISTER.md`. Four track extracts carry their own citations under their own declared
denominators.

## 4. Reproducibility Statement

Every `FACT VERIFIED` in the source-derived files is reproducible by read-only shell inspection of the root
in §2.1 — no tooling and no server required.

**Deployed-database findings are separate and carry their own record.** They are reproducible by offline
extraction from the archive named in `21_P02_DEPLOYED_DATABASE_EVIDENCE.md` §1, using restore tooling
already present on the host, **with no server started, nothing restored and nothing written**.

**The package originally declared that no database evidence existed and used that as its principal
limitation. The declaration was false and untested** — five deployed archives were on the host throughout.
Recorded as `RE-13` and `C-17`; what one pass produced is in `21`.

**What remains genuinely absent is runtime execution.** `C-04` is still `UNRESOLVED — EVIDENCE REQUIRED`,
now for a narrower and more informative reason: the deployed database examined carries **zero**
cost-of-sales lines, because split recognition is off there — **so it cannot exhibit duplicated ones.**

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

Regenerated after the peer-sourced population correction. The manifest file itself is excluded.

| File | SHA-256 | Bytes |
|---|---|---|
| `00_README_PACKAGE_INDEX.md` | `809e6bdf6e84fdc5f204b082ff1e2f806005a94fa75173fee21650c9fe47ee6a` | 13591 |
| `01_P02_PROCESS_MAP.md` | `399f34ad1a30f670e25cea730323e91b9ab4ad0003df20ebb103c8e826fd4c5b` | 24902 |
| `02_P02_INVOICE_POLICY_MATRIX.md` | `75109d0f4dfee623b9349fd5b7b06f7f50ddac1347ddb54c1ea09811655e6a5d` | 9083 |
| `03_P02_DELIVERY_COGS_TRACE.md` | `c7e1c40c63328a670ad84a99142f8007e49018a9fb90d2ccb145b38e9d4930a0` | 20672 |
| `04_P02_REVENUE_AR_TRACE.md` | `db733aa6be21ecbbc5df3fc5453c1d1c168ebd048622ac13f093156ca62920b2` | 17817 |
| `05_P02_BUSINESS_EVENT_REGISTER.md` | `c58e2ff818a1e4d6dfe941f1bb83582c8bc3d30453b2a26f203c8d45448ee4ce` | 12378 |
| `06_P02_ACCOUNTING_EVENT_REGISTER.md` | `cb49682ba6aaa3e4317b1de8351a0e887c0587df3bbeabc701124a503d174c7f` | 10485 |
| `07_P02_EVENT_TO_GL_MATRIX.md` | `1912d9bb0ef2cc693a4f5cbba2acb4062d5e79136bc99527f593e88bc65adef9` | 12965 |
| `08_P02_RETURN_CREDIT_REFUND_MATRIX.md` | `88571678101605551fda2b90bb551ffa5388aa505c9b0eeb844109867938fc77` | 11184 |
| `09_P02_PAYMENT_RECONCILIATION_MATRIX.md` | `a86d533f84f514c5988bf85987b2f171ca4adf15b42bd427e8b8b1e47c32a87e` | 12927 |
| `10_P02_CROSS_PROCESS_OWNERSHIP.md` | `6716a38fe361d3310b246b6645c3f452c4248b64eac96b36da7f1838bcc65875` | 11142 |
| `11_P02_EDGE_CASE_MATRIX.md` | `1864669506be50b180eabed4353336c76c791bc01ad6d91fa65dfa366e42c6c7` | 21561 |
| `12_P02_CONTRADICTION_REGISTER.md` | `f8e8a08e8989c04beb4565cb8a1293cfabcfdbe04fbfec8bb10197acff99eb3c` | 27111 |
| `13_P02_SOURCE_LINK_REGISTER.md` | `eb0ca93242e91800129a31d1a67b26558a2d133ea0f955042bc097407b506c78` | 20549 |
| `15_P02_REVISION_LOG.md` | `4f7e44089159330cdf2444e1a404d4561017df4d6bba86c881969c336d859dc3` | 27394 |
| `16_P02_AAS03_CHALLENGE.md` | `db16ea602f01aca9d0d2317291382fdaf02bd91d45e19bc6bd6abe2184edb28d` | 13815 |
| `17_P02_AAS_PLUS.md` | `82aa54064c74bffb58c740129812b340198fe4e6a202a9d00265c16c1be171b7` | 18833 |
| `18_P02_PMO.md` | `3942e9e5ac38ea9323ba6fb7cb355667be8346fdee8fe757ade5c49378fd4e34` | 21387 |
| `19_P02_CORE_RECON_HANDOFF_PACK.md` | `db27eb35ea71064e16cc51ef56d3d4ff1fd332c46e0f958a26ce2cbfd4897625` | 22457 |
| `20_P02_SCOPE_OWNERSHIP_MATRIX.md` | `2d8b1f1609707b3383e0ab3b3b8727f5b802d39e5e57e737eb5e7fb05020b48a` | 20277 |
| `21_P02_DEPLOYED_DATABASE_EVIDENCE.md` | `6d15018b8a0ee82f347cbc9ee0cb0bcaef134519460d4f586df407b637e89aa3` | 10631 |
| `22_P02_TARGETED_CLOSURE_DEPLOYED_EVIDENCE.md` | `78a512ab4e3605f44b948058028758a14d9697f6d66fa073b210f7a9f3a54314` | 40579 |
| `23_P02_CLOSURE_RECONCILIATION_REGISTER.md` | `3e3140c3427919e4bc8ebe50bc35b725d4da313e0c199bee524ea5672155a4d2` | 15204 |
| `24_P02_EIGHT_BUSINESS_SCENARIOS.md` | `06bf969ed1ae3b812afae0f056f97e286adf8377ace50040ab7dccdc8eaed7f1` | 9364 |
| `25_P02_CLOSURE_CHALLENGE_AND_CORRECTIONS.md` | `5746d3ab0f3a4066c1734d628f449bf878f348093783054ee7d078d803b64be8` | 16775 |
| `26_P02_V18_DEPLOYMENT_EVIDENCE.md` | `8eacf7270176113052b333236e86c8beb6a932863bc5258373053cbd6eb75f04` | 14442 |
| `L2_AUDIT_QUARANTINE/T1_RETURN_CREDIT_REFUND_EVIDENCE.md` | `c578f92e3e9855e013aee8a41e394181846b777ea76f7cac2ed706e82206d3b8` | 23754 |
| `L2_AUDIT_QUARANTINE/T2_PAYMENT_RECONCILIATION_EVIDENCE.md` | `b71883d42bb567b43579c9d668c6704f0e8ed2675c67e4460532ada8d6072f0d` | 28868 |
| `L2_AUDIT_QUARANTINE/T3_TAX_VAT_WHT_THAI_EVIDENCE.md` | `05702ce52c6e28c0bd3aad2ae87bfb809c16ef67369488104e5b89423b815b6e` | 30198 |
| `L2_AUDIT_QUARANTINE/T4_SCOPE_BOUNDARY_AND_CLOSE_EVIDENCE.md` | `cfeb7eb3310501209ea48062129247ee1986bcfc0ab3701433182ce3e1eaf6ed` | 35586 |

**Package total:** 31 files, 7634 lines.
