# 14 — P04 EVIDENCE MANIFEST

Layer: **2 — audit quarantine** (except file `19`, which is Layer 1).

Session: `SMEPLUS-26-09-04-ACC-P04-A2R-REV2-001`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `research/account-p04-acquire-to-retire-2026-09-04-001`
Base: `origin/SMEsPlus` at `88f52cd`
Path: `.../BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/P04_ACQUIRE_TO_RETIRE/`

---

## 1. Deliverables

The 19 filenames required by the governing prompt are preserved **verbatim**;
the numeric prefix is ordering only. Two files are additional: `00`, the layer
and method declaration, and `20`, required by the mid-session Scope-Aware
Constitution Correction.

| File | Bytes | Content |
|------|-------|---------|
| `00_README_LAYER_AND_METHOD.md` | 7,021 | Layer, method, classification vocabulary, negative-claim and denominator standards, reading order |
| `01_P04_UPSTREAM_CAPITALIZATION_TRACE.md` | 24,268 | Every path by which an asset comes into existence; the designation chain; runtime bounds |
| `02_P04_ASSET_LIFECYCLE_MAP.md` | 10,080 | Acquire-to-retire lifecycle against the estate; states; missing transitions; unhosted stages |
| `03_P04_ASSET_EVENT_REGISTER.md` | 9,216 | 24 events, triggers, state effects, accounting effects, event-level control findings |
| `04_P04_ASSET_TO_GL_MATRIX.md` | 8,796 | Account-resolution chain; event-to-entry matrix; multi-currency; period control; the reconciliation gap |
| `05_P04_ASSET_EQUIPMENT_RELATIONSHIP.md` | 10,507 | Asset-equipment-work-centre-operation chain; imported prior evidence re-verified; population corrections |
| `06_P04_DEPRECIATION_COST_HANDOFF.md` | 19,288 | Cost monetisation paths with declared unit; reconciliation failures; the analytic finding; the third denominator option |
| `07_P04_DISPOSAL_DERECOGNITION_MATRIX.md` | 26,601 | Disposal mechanics; TAS 16 derecognition, impairment and cessation; Thai destruction and VAT evidence |
| `08_P04_PRIOR_EVIDENCE_RECONCILIATION.md` | 10,503 | Import of the three prior Asset packages; audit lineage; the handover residue |
| `09_P04_BOSS_DECISION_REGISTER.md` | 8,136 | Standing Boss decisions with new evidence; decisions carried forward; decisions this session adds |
| `10_P04_BLOCKER_REGISTER.md` | 19,650 | 42 rows: 3 re-registered, 39 opened here; ranking; runtime evidence set |
| `11_P04_CROSS_PROCESS_OWNERSHIP.md` | 15,022 | P01, P03, P08, P09, P10 boundaries; ownership rulings; cross-process publication performed |
| `12_P04_CONTRADICTION_REGISTER.md` | 9,140 | 16 inherited, 7 new, 7 re-opened from the residue; what this session closed |
| `13_P04_SOURCE_LINK_REGISTER.md` | 9,783 | Every source with its pattern and path set; executed populations; declared negatives; statutory classification discipline |
| `15_P04_AAS03_CHALLENGE.md` | 11,521 | Four experts across six levels; four disagreements preserved unresolved |
| `16_P04_AAS_PLUS.md` | 20,774 | Self-challenge and independent adversarial challenge, kept separate; 25 review findings; area verdicts; the veto |
| `17_P04_PMO.md` | 12,456 | Constitution compliance; clean-room verification; declared deviations; executed progress figures |
| `18_P04_REVISION_LOG.md` | 11,207 | 13 revisions: 6 against prior packages, 3 against this session, 4 from independent challenge |
| `19_P04_CORE_RECON_HANDOFF_PACK.md` | 14,530 | LAYER 1 - clean-room business learning. The only file cleared to seed downstream design material |
| `20_P04_SCOPE_OWNERSHIP_MATRIX.md` | 16,386 | Scope-aware matrix under REV2-CORR1; revalidation of affected findings; peer dependencies |

## 2. SHA-256

Regenerate with `shasum -a 256 *.md` in this directory and compare against
`SHA256SUMS.txt`, which is committed alongside and is the authoritative list.

The table below covers the **20 other files**; this manifest cannot contain its
own hash, and `SHA256SUMS.txt` carries all **21**.

| File | SHA-256 |
|------|---------|
| `00_README_LAYER_AND_METHOD.md` | `e569eb7b671cae1196443123da111aef7a2746e9186a468e4d88d45602d504f1` |
| `01_P04_UPSTREAM_CAPITALIZATION_TRACE.md` | `ef7d7716c973eb8d9dfd862a0a1b9e2d13b2c524e8c98f7e49e2bf0cc5c9d0a3` |
| `02_P04_ASSET_LIFECYCLE_MAP.md` | `561118e4b1e312b6ff3cfab4f350db256c1f8b6b8364d9975e4286eef4c742f0` |
| `03_P04_ASSET_EVENT_REGISTER.md` | `ed31187344fa46246cf5c3f59c9444a212ad454b0ee62bb360dc2fcf81ad2a51` |
| `04_P04_ASSET_TO_GL_MATRIX.md` | `f97d5e4239b9fd1eb4ed4bbce5a03173185f2df336ec5c9f234c30b944531dd6` |
| `05_P04_ASSET_EQUIPMENT_RELATIONSHIP.md` | `196e3ffd03beeb7336aa7b97040144605dd005bd7af32e7280fa2de48b39d703` |
| `06_P04_DEPRECIATION_COST_HANDOFF.md` | `e920f7a6e611812f9a2c7a14d622d0d328108631cd813eb3c735a9b3b78377be` |
| `07_P04_DISPOSAL_DERECOGNITION_MATRIX.md` | `73498c37afaceb7557a1a4f304eeb7a53c943bf77364926f85e69038c756b413` |
| `08_P04_PRIOR_EVIDENCE_RECONCILIATION.md` | `e5970d358e188c1e0f5b99c8138f5cb09610b09885bf6b80ea51be4fbef780fe` |
| `09_P04_BOSS_DECISION_REGISTER.md` | `ce1a873fff38c8b45854238719efbce1386fd3f97f0c6058bc1991af98f00dfc` |
| `10_P04_BLOCKER_REGISTER.md` | `d6db03495fa9fc7f668075b385a02a6f12fd4c7f19a0c074bb095baa419d0aac` |
| `11_P04_CROSS_PROCESS_OWNERSHIP.md` | `96ce4558fb1e4e13fdaa65c8d78d7bda2c9cede7ab5098d9028795d5f6d80086` |
| `12_P04_CONTRADICTION_REGISTER.md` | `4a54d8b13cfff34602ef2d1c9a2c10b8a43934ff943dfaf4cad6904874038e79` |
| `13_P04_SOURCE_LINK_REGISTER.md` | `58182ff004ea65ffe27eaaf33b6d89593f4b255be73669249a56cff70fea7687` |
| `15_P04_AAS03_CHALLENGE.md` | `62e4462fe9244e4d866197c63e5a15af8e6be73ed5efaf9be8efbc9c195567b5` |
| `16_P04_AAS_PLUS.md` | `2fae6db9ea4af1e4f31095a5b5875b00e9c15544c79bfbdccec058dfc58c7c20` |
| `17_P04_PMO.md` | `271e71d9ffd9ceebf2f8c99ff2cee47e0a9fc278b95684cf3f495aa337fec269` |
| `18_P04_REVISION_LOG.md` | `8d39155035c9506db10ebe4ffb34dfefbf5a98d5d4b1f9533dbd7b70fe459478` |
| `19_P04_CORE_RECON_HANDOFF_PACK.md` | `046190f9a3c50ab213aea19653259ff76b92c2c0d7f3a1e75d45d68c264b9eb1` |
| `20_P04_SCOPE_OWNERSHIP_MATRIX.md` | `401b79203854b3b2b69da0e44c3371e9b372f68ba59837ba18fe796ff8711e78` |

## 3. Evidence roots and their bounds

| ID | Root | Bound stated at every point of use |
|----|------|-----------------------------------|
| `EV-CODE` | Reference ERP v18 Enterprise, build `20250608` | **790 installable modules** (791 directories, one carrying no manifest and no content). The figure `797` quoted by prior packages is an entry count |
| `EV-CUST` | Project custom addon set, v18 line | **65 directories** (68 entries) |
| `EV-DB` | **10 files · 7 snapshots · 5 database identities — SUPERSEDED, LOWER BOUND** across two trees, all carrying asset data — enumerated by **two archive signatures (`PGDMP` and zip-with-`dump.sql`), any extension, any depth, keyed on `database.uuid`**, after an extension-bounded first pass (`18` `P04-REV-27`) and a **single-signature, filename-keyed** second pass (`18` `P04-REV-35`) — the first enumeration reported four, one wrongly as empty; both errors are recorded at `18` `P04-REV-23`/`-24` — `iSMEs` (685 rows, **669 real**, **v16**); `iEVING`, `BK12MAY26` and `iTEST02` ×2 (**96 templates, zero real assets**, **v19**). **Reading the v1.16 archives requires a client newer than the host default** | **Read this session, after the deviation claiming no database access was tested and found false** (`18` `P04-REV-21`). **`idemo18_uat` WAS on this host** — at `~/OCC_BACKUP/`, outside an undeclared path set; found on the re-census and read (`P04-F-90`/`-91`/`-92`). It is **v18** (`base 18.0.1.3`) with **388 real assets**, which withdraws `P04-F-88` and falsifies the scope claim of `P04-F-85`  **THIS CENSUS IS SUPERSEDED AND IS A LOWER BOUND** (`18` `P04-REV-37`). It was taken over a path set — `~/Downloads` and the SMEsPlus tree — that was **author-chosen and never declared**. A census over a **declared** path set (`/Volumes` + `$HOME`, size bound >=1 MB stated, three signatures content-tested) has already returned **`idemo18_uat`** at `~/OCC_BACKUP/` — **v18, 388 real assets, the database two blockers were held open on** (`P04-F-90`) — plus a name-matched candidate set including further copies of `a1430edc`, `iEVING` 2026-03-31, `BK12MAY26` 2026-06-23, `iMSCG` ×2, `pankhamhom` ×2, `iErpOCC`, `iSCErP` and seven `OCC_Odoo18_Simulation_Lab` snapshots, **none of which is counted here because none has yet been uuid-keyed and content-verified**. Confirmed floor: **>=12 artefacts, >=8 snapshots, >=6 identities.** No count in this package is stated over the host until that census completes; every database-derived finding remains bounded to the identity named in it. |
| `EV-RT` | Runtime read-out, 2026-08-26, UAT database | Population query **unbounded** (280 returned). External-identifier query **restricted to 26 hand-picked names** — not a population statement. Field list **12 fields**, omitting the source-document link |
| `EV-HND` | Asset Actual Mapping handoff, 2026-08-26 | Project record |
| `EV-P1/P2/P3` | Three prior Asset packages | Commits `57cdb99`, `6c7512e`, `a852b6e`; heads `57cdb99`, `78067d2`, `54db9e1`. All branches intact and unmerged |
| `EV-LAW` | Thai statutory and standard-setter sources | Six sources; see `13` §4. TAS 16 rests on TFAC's **explanatory manual**, which states it is not part of the standards |

## 4. Register totals — executed, not quoted

| Register | Total |
|----------|-------|
| Findings (`P04-F-nn`) defined | **100** (`P04-F-18` withdrawn as a duplicate of `P04-F-23`; `P04-F-86`/`P04-F-87` added at `18` `P04-REV-35`; `P04-F-88`/`P04-F-89` at `P04-REV-36`; `P04-F-90`–`P04-F-92` at `P04-REV-37`; `P04-F-93`/`P04-F-94` at `P04-REV-38`; `P04-F-95`/`P04-F-96` at `P04-REV-39`; `P04-F-97`/`P04-F-98` at `P04-REV-40`; `P04-F-99` at `P04-REV-41`; `P04-F-100`/`P04-F-101` at `P04-REV-42`, where **`P04-F-88` is withdrawn one commit after publication**). *Executed in the same command that published this line — see `18` §5* |
| Blockers (`P04-B-nn`) — register rows | **51** — enumerated row by row, 50 distinct identifiers, no duplicates. *The figure stood at 45 and was wrong before this session touched it: four section headings understated their own contents (§4, §6A, §6B, §7A), and the published total agreed with neither the headings nor the rows. Corrected at `18` `P04-REV-38` — this package states that totals are unverified claims and had one in its own governing register.* |
| Contradictions | 16 inherited · 7 new · 7 re-opened from the residue |
| Revisions | 34 — 6 against prior packages, 3 against this session's own work, 4 from independent challenge |
| Recurrences of the enumeration / unit defect | **9 instances across 4 actors — P04's declared half**, `@ ae525fc`, verified unchanged by P07 at `c839bfe`. **No joint total is published**; halves are not summed (`18` §5b) |
| Expert disagreements preserved | 4 new · 7 inherited and re-opened · 2 between this session and the independent reviewer |
| Scope determinations | 14 objects and 10 operations classified; 2 on **HOLD — SCOPE EVIDENCE REQUIRED** |
| Peer dependencies | 8; findings published to 5 owning sessions. **P11 and P07 replied**: P11 answered 2 (**still open**) and returned twice more; P07 dispositioned 3 and returned 2 to P04 — both routed to Boss, both holds confirmed rather than lifted (`11` §6.1) |
| Statutory sources | **7 retrieved by this session · 1 taken in as peer-published** (`P04-LAW-H`, retrieved by P07; reliance stated) |
| Peer packages read **at source** | **1** — P11 at commit `2e284ef` (**now stale**; P11 head `b68ae17`). P04 had wrongly asserted it could not (`18` `P04-REV-19`); the branches were on the same remote throughout |

Every count in this table was produced by executing a match over the package,
not by carrying a figure forward. Two counts in earlier drafts were quoted
rather than executed and were wrong; both are recorded in `18`.

## 5. Verification scans

| Scan | Result |
|------|--------|
| Clean-room token scan of file `19` (Layer 1), declared scrub list | **0 hits on every token** |
| Clean-room scan **extended** with UI-label forms after independent challenge | **0 hits on every form**; one residue found and replaced |
| Prohibited-wording scan across the package — `PASS`, `FINAL FREEZE`, `MERGED`, `IMPLEMENTATION AUTHORIZED`/`AUTHORISED`, `APPROVED`, `Team B`, `Team C` | **0 hits** other than explicit negations and quotations of prior recorded positions |
| Finding identifiers referenced but never defined | **0** |
| **Independent-review dispositions audited against the files they name** | **24 checked, 22 verified, 2 defects found and fixed** — run with a positive and negative control after a peer's equivalent audit failed silently (`16` §3.1.1) |
| Blocker identifiers referenced but absent from the register | **0** (five were found missing mid-session and registered — `18` `P04-REV-10`) |

## 6. Terminal status

**READY FOR CORE ACCOUNTING RECONCILIATION.**

No asset final freeze. No approval. No merge. No implementation authorisation.
The independent-challenge veto on starting costing implementation and the prior
gate's governance conditions are **not discharged**.