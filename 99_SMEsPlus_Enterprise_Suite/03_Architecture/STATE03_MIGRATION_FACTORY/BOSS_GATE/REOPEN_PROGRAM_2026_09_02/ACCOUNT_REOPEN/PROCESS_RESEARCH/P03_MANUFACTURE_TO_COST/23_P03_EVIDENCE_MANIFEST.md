# 23 — P03 EVIDENCE MANIFEST

**LAYER 2 — AUDIT QUARANTINE.**

---

## 1. Session identity

| Field | Value |
|---|---|
| Session | `SMEPLUS-26-09-04-ACC-P03-M2C-REV2-001` |
| Correction applied mid-session | `SMEPLUS-26-09-04-ACC-REV2-CORR1` — Scope-Aware Constitution Correction |
| Process | P03 — Manufacture-to-Cost |
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical branch | `SMEsPlus` |
| Working branch | `research/account-p03-manufacture-to-cost-2026-09-04-001` |
| Base commit | `88f52cd` — *governance: approve canonical evidence acquisition flow* |
| Date | 2026-09-04 |
| Control level | `/L99999.99999` |
| Terminal state | **READY FOR CORE ACCOUNTING RECONCILIATION**, qualified in `21` §4 |

## 2. Primary source root

`/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/` — v18
Enterprise, build 20250608, 797 modules. Per-file SHA-256 for every cited artefact is in
`17_P03_SOURCE_LINK_REGISTER.md` §2. **The running system's configuration was not
available and caps every negative claim — `DEP-04`.**

## 3. Closure control 1 — prohibited verdict wording

Scan: `PASS`, `PASSED`, `FINAL FREEZE`, `IMPLEMENTATION AUTHORISED/AUTHORIZED`,
`DEVELOPMENT AUTHORISED/AUTHORIZED`, `Team B`, `Team C`, merge claims — across all
package files.

**Result: CLEAN.** Every match is either a governance statement declaring the wording
prohibited (`21` §5, `22` §5), a correct statement of clean-room routing policy
(`00` §1), or the word *merged* used technically for overlap-merged durations. **No
verdict, gate closure, authorisation or merge is declared anywhere in this package.**

Control required by `smeplus-subagent-pass-wording-defect`.

## 4. Closure control 2 — Layer 1 clean-room scan

Scan over `24_P03_CORE_RECON_HANDOFF_PACK.md`, the only Layer 1 file, for vendor model,
field, path, module and file-extension tokens.

**Result: CLEAN — zero vendor tokens.** The Layer 1 file states behaviour and consequence
in business language only, with no reference-product identifier of any kind.

Control required by `smeplus-clean-room-rules`.

## 4b. Closure control 3 — runtime evidence discipline (round 3)

| Control | Result |
|---|---|
| All database access read-only | **Complied** — `pg_restore` to stdout; no server started, no restore, no write |
| Every zero result re-run in a second form | **Complied** — `31` §4 records three forms for the `mrp_workcenter` zero |
| Every negative claim carries a positive control | **Complied** — `account_asset`/`res_company`/`stock_move` for the database zeros; `models.Model` for the custom-addon zeros |
| Totals enumerated, not asserted | **Complied** — §6 counts were produced by `grep -oE … | sort -u | wc -l`; four earlier assertions were found wrong and corrected (`22` §6) |
| A faulty counter caught before publication | **Recorded** — `RE-P03-13` |

## 5. Package integrity — SHA-256

```
ce452ab8c07c6cf28e6cfb91ead7f3cc44678ecc15472d0cd3975ab3bf29f9a2  00_README_LAYER_AND_METHOD.md
46425c14d0ea75cc2e2eabe9a56a1dc2e0b1110973dbbc750d5e36e0c34a6ee7  01_P03_PROCESS_MAP.md
d2df871c4ed86bfa32bfa6982ec9ba70ef3a0d3cc612dd56c947fe856e160162  02_P03_COST_COMPONENT_REGISTER.md
a52caa34b4bd0e60ef1d15472505ac9e0fe4892a0dbc1166baa542045c3d12b3  03_P03_WIP_FG_TRACE.md
0d6083640494e6299f39fdd0949a9f37f65e51131d9c4ea61d0bfcfaec93929d  04_P03_MACHINE_COST_OWNERSHIP_MATRIX.md
df90fd2eb87805b769d5b4ca79d267033381359b69de18030b4ab6a81472dac9  05_P03_DOUBLE_COUNTING_ATTACK.md
4af3b993608dbe4f5153a4c0a6fb573358a348e62ed18b38e8cb7ad3dc436130  06_P03_BUSINESS_EVENT_REGISTER.md
9741ee306e36352bc0fa7c5dbeb81781d37bdf568d2a9fb2fb568e2ba544c99f  07_P03_ACCOUNTING_EVENT_REGISTER.md
d36b02f58e9ee07ab47c2193b2024baa2354001207d02f30a5369ee764d3e9f1  08_P03_EVENT_TO_GL_MATRIX.md
f4cb6847d768f7be838c767d807d5c7070dcbd25b53f50da3e940a83329823ef  09_P03_MO_COST_TRACE.md
82e296352f1fa39329992ad78392e94d7bee3277c413c65f78038d05cb8afbe9  10_P03_VARIANCE_MATRIX.md
664b8278eaa6f2dd90aa2b1373f2efde92c0a6436e49bef564c01899b8aba767  11_P03_SCRAP_REWORK_MATRIX.md
167c5d06eb8c6c780aa9daaea07e55907a8111deb8ad3f87217a4461d5e60753  12_P03_CROSS_PROCESS_OWNERSHIP.md
a5a32850c3b9dc519b3fd556ad327b77e35d0b07fe4cf1786e5aceebaeb8dcfb  13_P03_PERIOD_CLOSE_AND_TOLERANCE.md
881b1a04e64b6082c4f229888c790447b1092510075c2d5738bfbd382bc07b2e  14_P03_DEPENDENCY_REGISTER.md
14f63a1f62c45f2024c16fb3a5f4a38d80148fc3cfd35173ac7363e47a8e5d46  15_P03_CROSS_INVENTORY_RECONCILIATION.md
274e87acf2958612dfcc14d1c39b12d89d4c8337fb7f231720d243e1eced703f  16_P03_CONTRADICTION_REGISTER.md
4e06da9c516d0d514708be45badd6799689bf9ca0a42db283c375805c6704650  17_P03_SOURCE_LINK_REGISTER.md
dea75b0aac19231d36323d52cad84ad8a7a481ae862e3b55f195f2b5f88b6394  18_P03_SCOPE_OWNERSHIP_MATRIX.md
e523502d610f255c4348768c0f7e9393329c861702a543dc3cff00d24f895119  19_P03_AAS03_CHALLENGE.md
2b59d02fd584610a5a552bd39685fb1ff92015c4bc674162885e651ffbd30576  20_P03_AAS_PLUS.md
02f66efb9dcb34ef0ae343d5b3ab7f4ba8122f029e206e7828e8365fed87e938  21_P03_PMO.md
b1c011f8ee02aa3dbd533378e21e02476a01f21b12dd09ab71e248f30c79f8d5  22_P03_REVISION_LOG.md
6ee5fc4581975d07ed9cec6ac196797238026649e3e001f9df7ed5c633bb3595  24_P03_CORE_RECON_HANDOFF_PACK.md
0e8f7c7fabb7f878acb5a8bfee87ce8296964ba6e9d201648b8cba0639f2fe45  25_P03_PEER_EVIDENCE_INTEGRATION_P04.md
b7f9315eb7acdc22fad6152610760cd1d7a9a5578cc388ac6c1835ef5f67cb8a  26_P03_CURRENT_STATE_RECONCILIATION.md
e87e0bb8f41498f73f57d53e607342bac5b62322129c90499d1be277c8b40cfb  27_P03_COST_MECHANISM_DENOMINATOR_RECONCILIATION.md
c55b6e2f17e8a7228a06365e900bdc27b67760dd283bc67a6db4297af7666ade  28_P03_COMPLETE_COST_INJECTION_POPULATION.md
2f4b9646f0aba52a8e7dfbfac9b6a3784f554bbe640c3ad5518b4decaf227091  29_P03_DC14_ANALYTIC_DUPLICATION_FORENSIC.md
fa14f1d96a70af0a0df18e11ad90f23084b3b162e4bc90ad9ae9f8c8848600a0  30_P03_DC15_IDEMPOTENCE_FORENSIC.md
85891d003b4925e3423bb32065b078d31e52b2e060f7fc751289b055cfe1a864  31_P03_DEP13_RUNTIME_COUNT.md
fa631d1d238595ae1749ae7d51e3d9f82fa6a640391d81765d296e1ffe8f9c66  32_P03_P04_B35_RECONCILIATION.md
5bc388e041196af88b902aa61d69bba9ac126c0eb100cbcc3fb341cee107a30f  33_P03_P09_ANALYTIC_NETTING_RECONCILIATION.md
a9642d7982f5e57afbb20c6598e2ba7640199a1668f197452f0109ed1479baba  34_P03_ZEROING_DOUBLE_COUNTING_MATRIX.md
4067303b9a2ae625dc75486a8a4c1be02140c0207836f3ddc542ac9aeee16f50  35_P03_HELP_TEXT_RUNTIME_TRUTH_MATRIX.md
09313633fc4eb06c012d6e680bae5bf696160eeb63d2e362f55a297f1cb7958c  36_P03_EQUIPMENT_ASSET_SCOPE_RECONCILIATION.md
f08aeacd10cbb9155b8ebaf9822bfe0fa0bb130537145e2fff9ed50482e38f2f  37_P03_SCOPE02_P11_HANDOFF.md
e7b416dab3fc7edab26d5a384a489fc6f83af1e0e3f4c211cd77f1cfe4c298ef  38_P03_AAS_PLUS_ONE_MECHANISM_POPULATION_PROOF.md
a2aaa2e2aa3522fa941fd78207d35972127d25249b0feb42cc00e527bac9b9cd  39_P03_CANONICAL_COST_OWNERSHIP_CANDIDATE_MATRIX.md
82256122e91da4f7e6d9bb9cd5b0dc32312ceebcb32a8e6cad70cabef0b89eb7  40_P03_FIXED_OVERHEAD_PATH_RECONCILIATION.md
99bd454c71eeb9047c6705f5161fce85f777da0a1cfefeed43bcaae05a5d59f5  41_P03_PEER_EVIDENCE_RECONCILIATION.md
5285c090dfb96e0ea6df74349b6f17d0e4cc8ce5612148a5e9bebcf12afc85b8  42_P03_DENOMINATOR_REVISION_RECORD.md
fb66816ed68af109bc91cf961ee142444a5fb5766150eb16e3363dc07d2a659c  44_P03_AAS03_TARGETED_CHALLENGE.md
5699b39571a8a34fd5b6926e3bfde09242c0ae1b8f5fa0c1c8121ea05dfafa25  45_P03_AAS_PLUS_VETO_RECHECK.md
955afe353ce4336ce6dd443c4d1c964d3a05ed7d1783f419230a39882ef6451b  46_P03_PMO_TARGETED_EXIT_REVIEW.md
7a67614951698d4005a29df133bea2be4eebf0220a5b6b275b7369515fb5e978  47_P03_UNRESOLVED_EVIDENCE_REGISTER.md
c8dd5a7cdb45d0e27b16ea45ac5855edf076c8b1e122b003d7be0218cd328176  evidence/P03T_EXECUTED_OUTPUT.txt
0059624345433173cb348c466a7c82d1a7e95e730bcdef86d07e5a480e453e35  evidence/P03T_db_rowcounts.py
```

`23_P03_EVIDENCE_MANIFEST.md` is excluded from its own manifest.

## 6. Finding inventory — **enumerated by `grep -oE … | sort -u | wc -l`, not asserted**

| Category | Count | Where |
|---|---|---|
| Double-counting / cost-integrity findings `DC-01` … `DC-15` | **15** | `05` |
| Of which Critical | 3 — `DC-01`, `DC-07`, `DC-11` | `05` §1 |
| Of which **live in any readable deployment** | **1** — `DC-13` | `26` §4 |
| Runtime findings `P03T-F-01` … `-07` | **7** | `26`, `27`, `28`, `31`, `34`, `38`, `40` |
| Contradictions `CTR-P03-01` … `-07` | **7** | `16` §1 |
| Gaps `P03-GAP-01` … `-08` | **8** | `16` §2, `39` §3 |
| Dependencies `DEP-01` … `DEP-17` | **17** | `14` |
| Unresolved (open) | **11** | `47` §1 |
| Tolerance-zero boundaries `TZ-01` … `TZ-08` | 8 | `13` §5 |
| Design candidates `R-01` … `R-16` | **16** | `21` §3, `30` §6, `36` |
| Self-challenge corrections `C-01` … `C-10` | 10 | `19` §6 |
| Targeted-challenge corrections `TC-01` … `TC-07` | **7** | `44` §6 |
| Research errors `RE-P03-11` … `-15` | **5** | `22` §6 |
| Preserved dissent | `D-01`…`D-03`, plus E1 and E4 in `44`/`45` | `20` §1, `44`, `45` §3 |
| Hypotheses tested and **discarded** | 2 — scrap-GL (round 1), and 4 mandated disproofs in `44` | `05` §9, `44` §2–§5 |
| **Prior blockers closed by this session** | **0** | `46` §4 |
| Peer claims adopted **without** verification | **0** | `25` §1, `41` §7 |
| Package files | **47** `.md` + `evidence/` | this directory |

## 7. What this manifest attests

1. Every deliverable required by the P03 directive exists — `21` §1.
2. Every negative claim carries POPULATION, PATTERN, PATH SET and UNIT, with one
   exception explicitly labelled weaker — `DEP-07`, per `C-06`.
3. No prior Asset, COGS, Inventory or Account blocker is closed, resolved or
   re-adjudicated.
4. No gate is closed, no verdict is declared, no implementation is authorised, and the
   branch is not merged.
5. The mid-session scope correction was applied substantively — it produced a new finding
   (`SCOPE-01`), not merely a relaxation — and its revalidation is disclosed as
   same-session and therefore weak — `20` §2 `AASP-05`.
