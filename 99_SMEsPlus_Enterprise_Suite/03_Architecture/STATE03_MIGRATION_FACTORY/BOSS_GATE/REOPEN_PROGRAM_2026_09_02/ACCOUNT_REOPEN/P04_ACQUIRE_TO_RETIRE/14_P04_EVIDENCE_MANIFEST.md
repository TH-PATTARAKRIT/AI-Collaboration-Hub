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
| `00_README_LAYER_AND_METHOD.md` | `e4384af1fae16c2bb4f9f646ee99aee09fc5b627215802c91d74b7c28922da1a` |
| `01_P04_UPSTREAM_CAPITALIZATION_TRACE.md` | `f653e7a8660ee969fd0f0c8ef78718b729e05b98d563dd863a9c504b3d9a2797` |
| `02_P04_ASSET_LIFECYCLE_MAP.md` | `561118e4b1e312b6ff3cfab4f350db256c1f8b6b8364d9975e4286eef4c742f0` |
| `03_P04_ASSET_EVENT_REGISTER.md` | `22cdef507de5b33c6ce41b8c00e64e694a77542d0a9f75bb3d64e9766a5366bd` |
| `04_P04_ASSET_TO_GL_MATRIX.md` | `f97d5e4239b9fd1eb4ed4bbce5a03173185f2df336ec5c9f234c30b944531dd6` |
| `05_P04_ASSET_EQUIPMENT_RELATIONSHIP.md` | `64ff3592bf0b8271e1269792c4a459e3d3ee139789d5fb9a184a2830fbb6ba8d` |
| `06_P04_DEPRECIATION_COST_HANDOFF.md` | `66742d10e8ae47cfc1a023d73d71ca6efbeabdcecd91a63830f076244557a376` |
| `07_P04_DISPOSAL_DERECOGNITION_MATRIX.md` | `11fe43914019bd9caf13d6727aa02d0ac9807f9deb151b7529ae0f03fec7d74a` |
| `08_P04_PRIOR_EVIDENCE_RECONCILIATION.md` | `e5970d358e188c1e0f5b99c8138f5cb09610b09885bf6b80ea51be4fbef780fe` |
| `09_P04_BOSS_DECISION_REGISTER.md` | `dcb600e9946eeb58b3ee21c1c266c9ad1c9b65e6f8c549f43d57f252b4092748` |
| `10_P04_BLOCKER_REGISTER.md` | `dfa2d8f267ff188bbb5d154923cfc4e8e28f6a0171f49b7081304924cef0d91f` |
| `11_P04_CROSS_PROCESS_OWNERSHIP.md` | `107ee7c93eb36eb37bea5947ab7936b02dcb2bf4f79ece0fc83baea4cb847339` |
| `12_P04_CONTRADICTION_REGISTER.md` | `ae3f9352751a6705ff095a7f68b4a36f18abdb615d523941dabe6adce32515a1` |
| `13_P04_SOURCE_LINK_REGISTER.md` | `329f05215855b1de9835253ecdfa6a39c1e315964c299e03416aad1ceb778ff3` |
| `15_P04_AAS03_CHALLENGE.md` | `3f020dd66f1a711bccbdc5e4bf97cbaf135646f96fc7f2cf7d3a6d2ac9c59a9f` |
| `16_P04_AAS_PLUS.md` | `330e3be84c1ebbe2efae043c0e5a47cc84bb84c0f8d3a92040da3b2c4db2d441` |
| `17_P04_PMO.md` | `641082e6343c662e9ea1d3350fce3fee4bf0885329a896b3161916858560cc0e` |
| `18_P04_REVISION_LOG.md` | `8e7467bc2078cec71206b3d4f67db19452b9808c81c8deb00483d8beaa496d78` |
| `19_P04_CORE_RECON_HANDOFF_PACK.md` | `046190f9a3c50ab213aea19653259ff76b92c2c0d7f3a1e75d45d68c264b9eb1` |
| `20_P04_SCOPE_OWNERSHIP_MATRIX.md` | `a7e3009f91c86a0e3507f66b609cc86b9f372236454c0e3c074c8be4144e6268` |

## 3. Evidence roots and their bounds

| ID | Root | Bound stated at every point of use |
|----|------|-----------------------------------|
| `EV-CODE` | Reference ERP v18 Enterprise, build `20250608` | **790 installable modules** (791 directories, one carrying no manifest and no content). The figure `797` quoted by prior packages is an entry count |
| `EV-CUST` | Project custom addon set, v18 line | **65 directories** (68 entries) |
| `EV-DB` | **39 database artefacts** on this host, census completed (`P04-F-126`); **8 identities keyed on `database.uuid` and read**, the remainder un-keyed, population **OPEN** across two trees, all carrying asset data — enumerated by **two archive signatures (`PGDMP` and zip-with-`dump.sql`), any extension, any depth, keyed on `database.uuid`**, after an extension-bounded first pass (`18` `P04-REV-27`) and a **single-signature, filename-keyed** second pass (`18` `P04-REV-35`) — the first enumeration reported four, one wrongly as empty; both errors are recorded at `18` `P04-REV-23`/`-24` — `iSMEs` (685 rows, **669 real**, **v16**); `iEVING`, `BK12MAY26` and `iTEST02` ×2 (**96 templates, zero real assets**, **v19**). **Reading the v1.16 archives requires a client newer than the host default** | **Read this session, after the deviation claiming no database access was tested and found false** (`18` `P04-REV-21`). **`idemo18_uat` WAS on this host** — at `~/OCC_BACKUP/`, outside an undeclared path set; found on the re-census and read (`P04-F-90`/`-91`/`-92`). It is **v18** (`base 18.0.1.3`) with **388 real assets**, which withdraws `P04-F-88` and falsifies the scope claim of `P04-F-85`  **THIS CENSUS IS SUPERSEDED AND IS A LOWER BOUND** (`18` `P04-REV-37`). It was taken over a path set — `~/Downloads` and the SMEsPlus tree — that was **author-chosen and never declared**. A census over a **declared** path set (`/Volumes` + `$HOME`, size bound >=1 MB stated, three signatures content-tested) has already returned **`idemo18_uat`** at `~/OCC_BACKUP/` — **v18, 388 real assets, the database two blockers were held open on** (`P04-F-90`) — plus a name-matched candidate set including further copies of `a1430edc`, `iEVING` 2026-03-31, `BK12MAY26` 2026-06-23, `iMSCG` ×2, `pankhamhom` ×2, `iErpOCC`, `iSCErP` and seven `OCC_Odoo18_Simulation_Lab` snapshots, **none of which is counted here because none has yet been uuid-keyed and content-verified**. Confirmed floor: **>=12 artefacts, >=8 snapshots, >=6 identities.** No count in this package is stated over the host until that census completes; every database-derived finding remains bounded to the identity named in it. |
| `EV-RT` | Runtime read-out, 2026-08-26, UAT database | Population query **unbounded** (280 returned). External-identifier query **restricted to 26 hand-picked names** — not a population statement. Field list **12 fields**, omitting the source-document link |
| `EV-HND` | Asset Actual Mapping handoff, 2026-08-26 | Project record |
| `EV-P1/P2/P3` | Three prior Asset packages | Commits `57cdb99`, `6c7512e`, `a852b6e`; heads `57cdb99`, `78067d2`, `54db9e1`. All branches intact and unmerged |
| `EV-LAW` | Thai statutory and standard-setter sources | Six sources; see `13` §4. TAS 16 rests on TFAC's **explanatory manual**, which states it is not part of the standards |

## 4. Register totals — executed, not quoted

| Register | Total |
|----------|-------|
| Findings (`P04-F-nn`) defined | **128** (`P04-F-18` withdrawn as a duplicate of `P04-F-23`; `P04-F-86`/`P04-F-87` added at `18` `P04-REV-35`; `P04-F-88`/`P04-F-89` at `P04-REV-36`; `P04-F-90`–`P04-F-92` at `P04-REV-37`; `P04-F-93`/`P04-F-94` at `P04-REV-38`; `P04-F-95`/`P04-F-96` at `P04-REV-39`; `P04-F-97`/`P04-F-98` at `P04-REV-40`; `P04-F-99` at `P04-REV-41`; `P04-F-100`/`P04-F-101` at `P04-REV-42`; `P04-F-102`/`P04-F-103` at `P04-REV-43`; `P04-F-104` at `P04-REV-44`; `P04-F-105`/`P04-F-106` at `P04-REV-45`; `P04-F-107`–`P04-F-110` at `P04-REV-46`; `P04-F-111`/`P04-F-112` at `P04-REV-47`; `P04-F-113` at `P04-REV-48`; `P04-F-114` at `P04-REV-49`; `P04-F-115` at `P04-REV-50`; `P04-F-116` at `P04-REV-51`; `P04-F-117` at `P04-REV-52`; `P04-F-118` at `P04-REV-53`; `P04-F-119` at `P04-REV-54`; `P04-F-120` at `P04-REV-55`; `P04-F-121` at `P04-REV-56`; `P04-F-122` at `P04-REV-57`; `P04-F-123` at `P04-REV-58`; `P04-F-124` at `P04-REV-59`; `P04-F-125` at `P04-REV-60`; `P04-F-126` at `P04-REV-61`; `P04-F-127` at `P04-REV-62`; `P04-F-128` at `P04-REV-63`; `P04-F-129` at `P04-REV-64`, where **`P04-F-88` is withdrawn one commit after publication**). *Executed in the same command that published this line — see `18` §5* |
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