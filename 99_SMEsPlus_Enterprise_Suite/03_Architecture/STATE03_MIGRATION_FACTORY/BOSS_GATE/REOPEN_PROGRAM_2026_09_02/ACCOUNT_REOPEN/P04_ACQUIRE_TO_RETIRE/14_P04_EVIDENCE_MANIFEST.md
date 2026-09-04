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
| `00_README_LAYER_AND_METHOD.md` | `949b9d843ec0d8a0e8d6b119585b27a93915e6b4b942fdac98fac6e70b26ec8b` |
| `01_P04_UPSTREAM_CAPITALIZATION_TRACE.md` | `89bfd8b2a8d06e89b2f140d4b9a03de4277e49b5f7673271a37a8ee7dc518aae` |
| `02_P04_ASSET_LIFECYCLE_MAP.md` | `561118e4b1e312b6ff3cfab4f350db256c1f8b6b8364d9975e4286eef4c742f0` |
| `03_P04_ASSET_EVENT_REGISTER.md` | `ed31187344fa46246cf5c3f59c9444a212ad454b0ee62bb360dc2fcf81ad2a51` |
| `04_P04_ASSET_TO_GL_MATRIX.md` | `f97d5e4239b9fd1eb4ed4bbce5a03173185f2df336ec5c9f234c30b944531dd6` |
| `05_P04_ASSET_EQUIPMENT_RELATIONSHIP.md` | `196e3ffd03beeb7336aa7b97040144605dd005bd7af32e7280fa2de48b39d703` |
| `06_P04_DEPRECIATION_COST_HANDOFF.md` | `36608d4e537b31990d1f446ccdd0f9360dbc7d01f166c9ebb42772417fcaf958` |
| `07_P04_DISPOSAL_DERECOGNITION_MATRIX.md` | `3bb56965e3c88884cbbc8e5be5dab350ec3a11169fdc3731c3fc0c275506cee3` |
| `08_P04_PRIOR_EVIDENCE_RECONCILIATION.md` | `e5970d358e188c1e0f5b99c8138f5cb09610b09885bf6b80ea51be4fbef780fe` |
| `09_P04_BOSS_DECISION_REGISTER.md` | `9b868be27dcdc5ca19f969ffa12a924de7b2d250f84e690458c6ae28d2c40dd5` |
| `10_P04_BLOCKER_REGISTER.md` | `4405b8a83199c2cb1a31e138df103ee968be45b47a2302b1fc9eec101e3aca77` |
| `11_P04_CROSS_PROCESS_OWNERSHIP.md` | `9a6fc9a19dc48c12ceb932309e4fc7479c1f72ec95ba38470090595687ba1ba5` |
| `12_P04_CONTRADICTION_REGISTER.md` | `4a54d8b13cfff34602ef2d1c9a2c10b8a43934ff943dfaf4cad6904874038e79` |
| `13_P04_SOURCE_LINK_REGISTER.md` | `81bf79393e93e88e8a423ba2fdfe5e82f504bf062fff8753a0a1651492c686f5` |
| `15_P04_AAS03_CHALLENGE.md` | `62e4462fe9244e4d866197c63e5a15af8e6be73ed5efaf9be8efbc9c195567b5` |
| `16_P04_AAS_PLUS.md` | `b8ddb76b3179fcd52047e71ade1f5ed7826782db44c138ac05752d9774e8627f` |
| `17_P04_PMO.md` | `ad69d0ccd419db3d620fb0fdb700510da788dc8e65c6258686f0d8705865f2bd` |
| `18_P04_REVISION_LOG.md` | `314604c9fa11142a1a5edf42575fe2e84287a5cec5a29169662daf7fa67342a1` |
| `19_P04_CORE_RECON_HANDOFF_PACK.md` | `f0bc531d02e68857c9577e710026ed74b9084766041b6506a184862d66203b6a` |
| `20_P04_SCOPE_OWNERSHIP_MATRIX.md` | `86326f4ef4bea0f9c03832abc0cc08b64881b43a89e14674faf01de3f3e82ff9` |

## 3. Evidence roots and their bounds

| ID | Root | Bound stated at every point of use |
|----|------|-----------------------------------|
| `EV-CODE` | Reference ERP v18 Enterprise, build `20250608` | **790 installable modules** (791 directories, one carrying no manifest and no content). The figure `797` quoted by prior packages is an entry count |
| `EV-CUST` | Project custom addon set, v18 line | **65 directories** (68 entries) |
| `EV-RT` | Runtime read-out, 2026-08-26, UAT database | Population query **unbounded** (280 returned). External-identifier query **restricted to 26 hand-picked names** — not a population statement. Field list **12 fields**, omitting the source-document link |
| `EV-HND` | Asset Actual Mapping handoff, 2026-08-26 | Project record |
| `EV-P1/P2/P3` | Three prior Asset packages | Commits `57cdb99`, `6c7512e`, `a852b6e`; heads `57cdb99`, `78067d2`, `54db9e1`. All branches intact and unmerged |
| `EV-LAW` | Thai statutory and standard-setter sources | Six sources; see `13` §4. TAS 16 rests on TFAC's **explanatory manual**, which states it is not part of the standards |

## 4. Register totals — executed, not quoted

| Register | Total |
|----------|-------|
| Findings (`P04-F-nn`) defined | **64** (`P04-F-18` withdrawn as a duplicate of `P04-F-23`) |
| Blockers (`P04-B-nn`) — register rows | **42** — 3 re-registered from the handover residue, 39 opened by this session |
| Contradictions | 16 inherited · 7 new · 7 re-opened from the residue |
| Revisions | 13 — 6 against prior packages, 3 against this session's own work, 4 from independent challenge |
| Expert disagreements preserved | 4 new · 7 inherited and re-opened · 2 between this session and the independent reviewer |
| Scope determinations | 14 objects and 10 operations classified; 2 on **HOLD — SCOPE EVIDENCE REQUIRED** |
| Peer dependencies | 8, all **OPEN**; findings published to 5 owning sessions |
| Statutory sources retrieved this session | 6 |

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
| Blocker identifiers referenced but absent from the register | **0** (five were found missing mid-session and registered — `18` `P04-REV-10`) |

## 6. Terminal status

**READY FOR CORE ACCOUNTING RECONCILIATION.**

No asset final freeze. No approval. No merge. No implementation authorisation.
The independent-challenge veto on starting costing implementation and the prior
gate's governance conditions are **not discharged**.