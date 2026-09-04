# P06_EVIDENCE_MANIFEST.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Repository:** TH-PATTARAKRIT/AI-Collaboration-Hub
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001
**Base commit:** `88f52cd7ba6dc40b8951c4bfc4e0016af7cbb7ad` (origin/SMEsPlus)
**Generated:** 2026-09-04T16:08:08Z
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. Package integrity — SHA-256

Computed over the deliverable files in this directory at manifest time. The manifest necessarily excludes itself.

| File | Lines | Bytes | SHA-256 |
|---|---|---|---|
| `01_P06_PAYMENT_STATE_MODEL.md` | 276 | 24456 | `e31513a1af10172ec7e9ca130db7cc40d10fe7161fafd04db6689d2e2b62f5eb` |
| `02_P06_BANK_EVENT_REGISTER.md` | 210 | 21174 | `8aaa296751bd0f861dad306c569c6545916980963588539b14709724868f69e3` |
| `03_P06_SETTLEMENT_STATE_MATRIX.md` | 155 | 13809 | `e7ab942b9bd98e80a592b4c9119e5a00b4c53a753451106e3973907061751639` |
| `04_P06_RECONCILIATION_MODEL.md` | 248 | 21869 | `8984b0f9476e8a1598aa288215f61002673561688a9b07cc121660840bf2340f` |
| `05_P06_EVENT_TO_GL_MATRIX.md` | 179 | 17460 | `ce059dccee5a56743b5fd889c65de0c8ae0f32a4ac14dbe1716b2fae473ee881` |
| `06_P06_FX_FEE_INTEREST_MATRIX.md` | 204 | 16260 | `2c9da2c199aacc0830e77e30a342b23c34f87b7d36999a43ad4675722d627cdf` |
| `07_P06_DUPLICATE_MATCH_ATTACK.md` | 252 | 22749 | `de59a506f668f4af22fd982c726c5eb6120d0c225724ca84232960d1f683b546` |
| `08_P06_PAYMENT_PROVIDER_TRACE.md` | 226 | 19669 | `004f5653a50e9b9ee2ff59e763e2611e62deab5e78c48a6b4b34b7f8b82b47eb` |
| `09_P06_CROSS_PROCESS_OWNERSHIP.md` | 125 | 13749 | `89929f9850e87382400a348e8dd36693987588494559fc14e9df18e52e69821a` |
| `10_P06_EDGE_CASE_MATRIX.md` | 210 | 21813 | `e498b0e79cddaf5f11082448e5c7be36957d12b764c0259e346cfff81bb6db5a` |
| `11_P06_CONTRADICTION_REGISTER.md` | 112 | 15112 | `8dfe3e8d0973faeb2d25983e9435a58e570038b855395a4e2d382f922ac662a4` |
| `12_P06_SOURCE_LINK_REGISTER.md` | 124 | 11926 | `848c939885a426942f4a48bc022c733b5961de6bcefd38c1bf4be04f54d223ef` |
| `14_P06_REVISION_LOG.md` | 115 | 10448 | `850338891d8d6e042df4a94bd3c832a8038e79447357140f8cd3ab3c91173e9b` |
| `15_P06_AAS03_CHALLENGE.md` | 116 | 12564 | `b2d8a7daf39fe744cd28736cf27842ac0d6c7328de881106474639abd4578f03` |
| `16_P06_AAS_PLUS.md` | 143 | 14214 | `84cd452476941cdeba3f3846192050c8f50f270a64c04b044921a4bfdf53aecc` |
| `17_P06_PMO.md` | 164 | 12248 | `84dededd9719d482e2319fff5557178bcbd534c2dcd1bfd5e5022d135e1bc4a2` |
| `18_P06_CORE_RECON_HANDOFF_PACK.md` | 145 | 9746 | `a01a74b99631c2ae6badf61e6bea06ca31b118f5081a5b8e170e502c57dff5a4` |
| `19_P06_SCOPE_OWNERSHIP_MATRIX.md` | 214 | 25562 | `856df27195101edcdab19af118d9f4e1faf3605720c1b43c370d1155ebb3d9d6` |
| `20_P06_CUSTOM_MODULE_DELTA.md` | 205 | 21249 | `e3bca376b04ccd0da7481c708875aac540e027c58a58bdef8081766be047a0e6` |

**Files: 19  ·  Total lines: 3423**

---

## 2. Evidence sources relied upon

Full declaration, including search boundaries, is in `12_P06_SOURCE_LINK_REGISTER.md`, which is the **controlling denominator document** for this package. Summary:

| Ref | Source | Layer | Access verified |
|---|---|---|---|
| S-01 | Reference ERP v18 Enterprise source tree (`18.0+e.20250608`) | L2-SRC | 2026-09-04, directory listing |
| S-02 | Project custom addon set, v18 line — 68 modules | L2-CUST | 2026-09-04 |
| S-03 | Legacy v14 tree — 127 modules | L2-CUST | 2026-09-04 |
| S-04 | Runtime bank-journal extract, 12 journals across 2 companies, `VERIFIED_LIVE_UAT` | L2-RUN | 2026-09-04, file read |
| S-05 | This repository at base commit `88f52cd` | L1-REPO | 2026-09-04 |
| S-06 | Jira, `scgl.atlassian.net`, cloud id `67b5858f-f930-4950-af26-aa7662000e77` | EXT-JIRA | **2026-09-04, authenticated — tested, not inherited** |
| S-07 | The Boss session prompt (the only source of the P06 process definition) | — | — |

Two further custom copies (`t8master`, `18.0.4_smeplus_v2`) were enumerated for the copy denominator in `20_`. **Which copy is deployed is unknown to this session and is asserted nowhere.**

---

## 3. Sources deliberately not consulted

Declared so that no later summary can silently upgrade a Class-C to a Class-A.

| Ref | Not consulted | Consequence |
|---|---|---|
| NC-01 | Any live or UAT database | every runtime claim is second-hand; 16 Class-D items |
| NC-02 | Reference ERP v19 line | out of scope |
| NC-03 | Thai bank host-to-host / ISO 20022 counterparty specifications | CAMT field population is **HOLD** |
| NC-04 | Thai statutory requirements for reconciliation retention, cheque handling, e-payment records | all **HOLD**, routed to Accounting-Tax |
| NC-05 | Full behavioural diff of every custom copy | only version strings and presence compared |
| NC-06 | Jira description and comment bodies; projects other than ERPPLUS | Class B beyond the declared summary scan |
| NC-07 | Confluence | not searched |
| NC-08 | The custom approval modules (`multi_level_approval*`) | **downgraded `P06-B-22` from Class A to Class B at challenge** |

---

## 4. Denominators of record

| Denominator | Value | Boundary |
|---|---|---|
| Reference modules in P06 scope | 57 | `ls $V18E` depth 1, declared grep pattern |
| Bank-event ingestion doors | **7** | module-borne 6 + manual keying 1 — see the correction recorded in `02_` and `14_` REV-E-01 |
| Bank-event identity fields | 2 | on `account.bank.statement.line` |
| Doors attaching no identity | **4 of 7** | CSV, QIF, OCR, manual |
| Format parsers populating an identity | **2 of 4** | CAMT, OFX |
| Payment states | 5 | `account.payment.state` selection |
| Invoice payment states | 7 | `PAYMENT_STATE_SELECTION` |
| Batch states | 3 | `account.batch.payment.state` |
| Widget states | 3 | `bank_rec_widget.state` |
| Widget line flags | 8 | `flag` selection |
| Reconcile rule types | 3 | `rule_type` selection |
| Write-off amount types | 4 | `amount_type` selection |
| Settlement cells characterised | **18 of 60** | 42 are Class C — explicitly not asserted unreachable |
| Event→GL rows | 31 | the declared P06 event set |
| Scope-determined objects | 30 | the P06 semantic trace |
| Custom modules in P06 scope | 12 (CUST18) + 6 (CUST14-only) | declared module population |
| Custom copies compared | 4 roots — 65 / 127 / 57 / 47 modules | depth-1 directory count |
| Custom modules touching the bank statement | **0 of 12** | declared grep pattern |
| Jira ERPPLUS population | 146 | project scope |
| Jira ERPPLUS items matching P06 domain | **0** | summary field, 6 declared patterns |
| Repository hits for the P06 identifier | **0** | all tracked `.md`/`.yaml` at `88f52cd` |
| Sibling `research/account-p0[1-5]` branches on origin | **0** | `git ls-remote`, at fetch time |

**Every count above states its POPULATION, PATTERN, PATH SET and UNIT in the file that produced it.** None was author-chosen.

---

## 5. Findings and blockers

| Category | Count |
|---|---|
| Attacks executed (statically) | 8 |
| CONFIRMED DEFECT classifications | 7 |
| HOLD — SCOPE EVIDENCE REQUIRED | 1 attack + 3 scope items |
| Type I contradictions (internal to the reference) | 28, of which 17 HIGH |
| Type II contradictions (code vs its own documentation) | 7 |
| Type III (internal to this package / between sources) | 8 |
| Blockers raised | 42 |
| Open items | 42 — C:18 · D:16 · HOLD:8 |
| AAS-03 challenges | 18 |
| Amendments produced by challenge | 6, including **1 classification downgrade** |
| Author errors recorded | 4 |
| AAS+ vetoes | 2 |
| Dissents preserved | 6 |

---

## 6. Control scans

| Scan | Result |
|---|---|
| Prohibited verdict wording | **0 verdict uses** across all files |
| Negative-claim tokens | 4 unbounded instances found and repaired (REV-E-03) |
| Class-restatement check | **no B/C/D restated as A**; one A→B downgrade |
| Tenant-scope assumption (CORR1) | 2 occurrences, both revalidated |
| Clean-room layer | all files carry LAYER 2 |
| PII | real bank account numbers present in S-04 **not reproduced** |

---

## 7. Verification instruction

To verify this package:
```
shasum -a 256 -c   # against the table in §1
git log -1 --format=%H research/account-p06-bank-to-reconcile-2026-09-04-001
```
Then confirm each cited `file:line` against source S-01/S-02/S-03 at the paths declared in `12_`. **A citation that cannot be resolved against a source listed in `12_` is inadmissible** and must be raised as a contradiction.

---

# End
