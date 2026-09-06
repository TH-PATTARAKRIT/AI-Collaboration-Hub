# 10_XRECON_EVIDENCE_MANIFEST

**Session** `[SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-XRECON-001]` · branch `audit/account-xrecon-2026-09-06-001`
**Base** `origin/SMEsPlus` @ `41f3b32398b1a1613fd7302873d0b29527c782f8`

---

## 1. Frozen source SHAs — every material statement in this package traces to one of these

| Pxx | Branch | Frozen SHA | Role |
|---|---|---|---|
| **P06 IEV** | `audit/p06-independent-verifier-2026-09-06-001` | `b423eff340cc86bbf52d2a97271f167ad9096bba` | head; **addendum, substantive** |
| P06 IEV terminal | same | `dac6ac374a9445c46aa7c392c8c70ff264713f71` | terminal publication |
| **P06 source** | `research/account-p06-bank-to-reconcile-2026-09-04-001` | `1b018c104001eb4683166518a6161a8cd8ab5cee` | frozen audit surface |
| **P08 IEV** | `audit/p08-independent-verifier-2026-09-06-001` | `bd95d1d16009a7a7d293de53848f983403e87070` | head; late inbound addendum |
| P08 IEV terminal | same | `3ea9195` | **TERMINAL STATE B — authoritative** |
| **P08 source** | `research/account-p08-record-to-report-2026-09-04-001` | `00ccd663d55d72830c8e0db46e4cc1aa345d0af1` | frozen audit surface |
| **P09** | `research/account-p09-plan-to-analyze-2026-09-04-001` | `ec4d3d2f32c8ae72e53f043f53783beb07071ffb` | head; **BOOKKEEPING ONLY** |
| **P09 substantive** | same | `4778792196371c460d3e6ca87bf8d9adee760f47` | **authoritative for all P09 state** |
| **P11** | `research/account-core-reconciliation-2026-09-04-001` | `dc4cc4a6bb1ea2fac071925f5eb1c01c44072c4b` | head, substantive |
| P11 challenge surface | same | `9356557` | frozen review surface |
| **P07** *(existence only)* | `research/account-p07-th-tax-compliance-2026-09-04-001` | `ee2be30` | **name resolved, content NOT opened** |

## 2. Verification methods used

| Method | Where applied |
|---|---|
| `git rev-parse origin/<branch>` vs prompt-declared SHA | all four references — **4 of 4 MATCH, UNMOVED** |
| `git diff --stat <parent> <head>` | bookkeeping/addendum classification for P06, P08, P09 |
| `git diff <parent> <head> \| grep '^[-+][^-+]'` | P09 bookkeeping claim — **11 content lines, verified not asserted** |
| `git merge-base` + `git diff --name-only` | package PATH SET derivation (**not** author-supplied file lists) |
| `git ls-tree -r --name-only <SHA>` | artefact inventories; filename resolution |
| `git grep -n` / `-hoE` over `<SHA> -- <path>` | claim location and enumeration |
| `git archive <SHA> \| tar -x` + GNU `grep -rhoE` | **second instrument form** for every published count |
| synthetic injection | positive control on the P06 blocker enumeration (67 → 68) |
| positive control on every negative | `9356557`, `169,143`, `P06` file-count, `HO-` families |

**Instrument failures detected and recorded, not published as findings:** `git grep -o` returns nothing in
this environment (`XR-I-01`); `\b` is unsupported by `git grep`'s ERE (`XR-I-02`). Both are documented in
`04_` §4 and in the child prompts.

## 3. XRECON's own measured evidence

| ID | Claim | Instruments | Control |
|---|---|---|---|
| `XS-01` | P06 blocker population = **67**, contiguous 01–67 | `git grep -hoE` over `1b018c1`; `git archive` + GNU `grep` over **87** extracted files; sets `diff`-identical | synthetic injection **67 → 68** |
| `XS-02` | P11 decisions = **19** (`D-1`…`D-18` + `D-3b`); the `D-` namespace holds **3 families**; naive count = 23 | two padding conventions enumerated; cross-checked against `RESEARCH_ERROR_AND_REVISION_LOG`:1008 | — |
| `XS-03` | P08 decisions = **19** (`P08-BD-01…19`), distinct from P11's 19 | enumeration | P08's own `CP-S11` self-audit (`P08-CONTRA-45`) |
| `XS-04` | P08 outbound rows = **14** (`HO-01…14` in `54_`); `58_`'s 13 is a different population | `HO-` enumeration across `25_`, `54_`, `58_` | — |
| `XS-05` | 6 stale peer-SHA occurrences in 2 live P11 registers; **the 7 unmoved peers are pinned correctly** | `git grep -n` on three CORR2 heads across the whole P11 package | positive control after `XR-I-01` |
| `XS-06` | P11 carries P08's no-referent *"3 at 1e-7"* at **3 locations**, one of them a falsification | `git grep -nE '1e-7'` over P11 @ `dc4cc4a` | positive control `169,143` → 4 occurrences |

## 4. Pre-commit sweep — four checks of disjoint unit

| # | Unit | Check | Result |
|---|---|---|---|
| **1a** | distinct identifier | every `XRD-nnn` cited is defined in `02_`, and every defined one is cited | **11 = 11, zero orphans** |
| **1b** | distinct identifier | every `Q-*-nn` cited is defined in `07_` | **14 = 14, zero orphans** |
| **1c** | distinct identifier | every `RC-nn` cited is defined in `05_` | **7 = 7, zero orphans** |
| **1d** | distinct identifier | every `XS-nn` cited is defined in `01_` | **6 = 6, zero orphans** |
| **2** | line | prohibited PASS wording | **clean** — the single hit is the prohibition statement itself (`09_`:194, *"Accounting PASS declared \| NO"*) |
| **3** | filename | every cited peer `.md` resolves on a frozen SHA | **53 cited; 45 resolve; 7 are this package's own ellipsis abbreviations in table cells, not filenames; 1 is `19_P07_CORE_RECON_HANDOFF_PACK.md`, resolved separately at P07 `ee2be30`** |
| **4** | branch state | no peer branch modified, no force-update, no merge | **clean** |

**Note on check 3:** the seven "unresolved" entries are strings like `…AUTO_RESUME_STATE.md` produced by this
package's own abbreviation of long filenames inside narrow table cells. They are **not defective references**
— each is disambiguated by its row. Recorded rather than suppressed, because **an exception list that cannot
report itself is the defect this programme has hit before.**

## 5. Package contents — SHA-256

Computed over the working tree immediately before commit.

```
42af2a236aec0898948c5b6049d0082b1f010bb77b194a68aabb8256c2536712  00_XRECON_PREFLIGHT_AND_FREEZE_REGISTER.md
b6ab8d1818c0dc171894cbd7af36750394d8f3a98a62af5034db10d245fcad50  01_CROSS_PXX_FROZEN_EVIDENCE_SNAPSHOT.md
9203c67400693903deda87bd98b5e937b2780f4870e6f5cf1bca36d5157e4631  02_CROSS_PXX_ROOT_DEFECT_AND_LINEAGE_REGISTER.md
37963b8ba6dbc3eaa77ec29bd3e1264cbbeea678ba0e956dc5c49daf75ee1db7  03_CROSS_PXX_HANDOFF_AND_PROPAGATION_MATRIX.md
a7be430589920a762f158d86eb6fca37c0f5d4ea04c98d23fce6338b504aca2d  04_VERIFIER_AUTHORED_DEFECT_SEPARATION_REGISTER.md
355e47fef4c7babe065e05fa79526b5b01cc92aaf02ab7e8965c4d481ff4938d  05_CORRECTED_SURFACE_RECHALLENGE_REGISTER.md
842509dbc9cbf8f0eacb6f6fec0ed8e6fa0958702a990593146008d2505055fd  06_VETO_AND_BOSS_DECISION_DEPENDENCY_REGISTER.md
55100cfa1974b6c2d435278ece7e63ff04addac80fc719a739deda3a61ada2ed  07_OWNER_BOUNDED_CORRECTION_QUEUE.md
0594f2fce932eca2c925f5637bb7ed856733ced439ea07302c4d7f0b8a3234eb  08_OWNER_CORRECTION_PROMPT_PACK.md
413ce5f61df864c3edeb8142a35807b6150de6115a97d0cea3388e464adbb150  09_CROSS_PXX_RECONCILIATION_FINAL_REPORT.md

10_XRECON_EVIDENCE_MANIFEST.md  — SELF-EXCLUDED: a manifest cannot contain its own hash.
Its integrity is established by the commit SHA recorded in §6 and by the remote read-back.
```

## 6. Publication evidence

| Field | Value |
|---|---|
| **Branch** | `audit/account-xrecon-2026-09-06-001` |
| **Base** | `origin/SMEsPlus` @ `41f3b32398b1a1613fd7302873d0b29527c782f8` |
| **Commit SHA** | `COMMIT_SHA` |
| **Remote read-back** | `REMOTE_READBACK` |
| **Files published** | **11** |
| **Peer artefacts modified** | **0** |
| **Peer branches pushed to** | **0** |
| **Merged to `SMEsPlus`** | **NO** |

## 7. Scope attestation

| | |
|---|---|
| Root defects identified | **11** |
| Root defects **resolved by this session** | **0** — by mandate |
| Manifestations traced | **43** across **24** files |
| Owner-bounded queue items | **13** + 1 authority item |
| Child prompts generated | **4** |
| Child prompts **executed** | **0** |
| Fresh challenges required | **6** |
| Fresh challenges **run or satisfied here** | **0** |
| Vetoes standing | **17** · **discharged: 0** |
| Boss decisions open | **51** · **answered: 0** |
| Local published totals altered | **0** — preserved as audit lineage |
