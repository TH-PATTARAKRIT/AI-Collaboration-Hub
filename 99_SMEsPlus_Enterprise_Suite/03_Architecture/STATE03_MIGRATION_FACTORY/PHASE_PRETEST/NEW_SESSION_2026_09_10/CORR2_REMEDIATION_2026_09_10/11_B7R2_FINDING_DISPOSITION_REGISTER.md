# 11 — B-7 ROUND-2 FINDING DISPOSITION REGISTER

# `17 DISPOSITIONED · 17 CORRECTIONS LANDED IN A NAMED ARTEFACT · 0 REVISION-LOG-ONLY`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Baseline: `c91d5840` · Boss: **SOLE FINAL APPROVER**

> **A revision log is not a correction.** The programme has previously accepted findings whose
> corrections were **described in a disposition table and never edited into any register**.
> **This file therefore records, per finding, the artefact and the section where the correction actually
> exists — and `§4` audits that claim mechanically rather than asserting it.**

---

## 1. DISPOSITION METHOD

`0` prior artefacts are modified. **Corrections are published as superseding artefacts** — the method the
package itself declares and which Round 2 verified as legitimate. **The obligation that follows is that
the superseding artefact must actually contain the corrected value**, which is what `§4` tests.

---

## 2. THE REGISTER

| ID | Canonical disposition | **Correction, as applied** | **Landed in** | Residual |
|---|---|---|---|---|
| `R2-F-01` | **CONFIRMED — WIDENED** | Independence classified `NOT ESTABLISHED` for **both** rounds; `4` root causes; exit condition `2`'s cure **withdrawn**; `6` remediation requirements | **`02_` §2–§10** · `03_` row `2` · `09_` `ZT-05` | rerun (`16_`) |
| `R2-F-02` | **CONFIRMED** | both SHAs recorded; content identity proved by empty diff; no finding turns on it | **`01_` §2** | resume-state pointer convention |
| `R2-F-03` | **CONFIRMED** | manifest entries measured `15` in **`4` command shapes**; `17_`'s `14` recorded as wrong | **`01_` §2** · `08_` §4 | none |
| `R2-F-04` | **CONFIRMED** | count `16` confirmed **correct**; named range shown wrong (includes `13_`, omits `17_`) | **`01_` §2** · `08_` §4 | none |
| `R2-F-05` | **CONFIRMED** | `3 of 4` re-placements on external authority, `1` on the executor's reading — **separated in a table, not in prose** | **`03_` §1** · `04A_` §5 | `BOSS-CORR2-RD01` |
| `R2-F-06` | **CONFIRMED — STRENGTHENED** | denominator re-derived **`14`**; condition `11` restored; **the package's own carrier already published `14`** (resume L227) | **`03_` §2, §4** | `BOSS-CORR2-RD01` |
| `R2-F-07` | **CONFIRMED** | `SC-54` cl. `5` quoted verbatim and applied; `E2E-04`'s `D` limb identified as the unexamined move | **`04A_` §5** | `BOSS-CORR2-RD01` |
| `R2-F-08` | **CONFIRMED — PATH SET WIDENED** | searched **all `194` branches, whole trees**; positive control fires at `9`; classified `AUTHORITY NOT DURABLY PROVEN`; `04A_` produced **instead of** `04_` | **`04A_` §2, §3, §6** | `BOSS-CORR2-RD01` |
| `R2-F-09` | **CONFIRMED** | three `X-nn` populations enumerated; `X-14`'s two resolutions shown | **`01_` §2** · `08_` row `22` | rename in the successor package |
| `R2-F-10` | **CONFIRMED** | `36_`'s status fields shown identical before and after; re-stated as *heading clarified*, not *conclusion reversed* | **`01_` §2** | none |
| `R2-F-11` | **CONFIRMED — STRENGTHENED** | crosswalk **derived in full** at the Boss text; `9 of 10`, `11 of 12`; `Purchase → Inventory` proved absent in `3` shapes with a firing control; **`CORE-07` discharged as a mapping** | **`06_` §2, §3, §5, §6** | **`BOSS-CORR1-01`** |
| `R2-F-12` | **CONFIRMED** | `0` occurrences of the caveat in `05_`/`10_` against a control firing at `3`; `N/A` re-classified **CONDITIONAL** under `§24` | **`06_` §4** · `09_` `ZT-04` | carry the condition in the row |
| `R2-F-13` | **MODIFIED** | substance **confirmed and strengthened** (`8 of 11` properties differ; ground falsified twice); **evidence-base clause corrected** — the contradiction is on-baseline at `05_` L49; two identical off-baseline copies located | **`07_` §1–§5** | element `15` |
| `R2-F-14` | **CONFIRMED — ENLARGED** | all `21` membership claims audited; **`11` defective in `8` classes**, not `4 + 1`; `10_` §1 superseded | **`08_` §2, §3** | enumerate `IR`/`AR` |
| `R2-F-15` | **MODIFIED** | `BOSS-CORR1-01` half **confirmed** (`0` occurrences); `SC-SMT-01` half **corrected** — it *is* addressed at `11_` L17; defect re-stated as **open vs askable conflation**, with `11_`'s own two-directional application shown | **`05_` §3, §5** | `4` Boss decisions |
| `R2-F-16` | **CONFIRMED** | `4` live exit denominators enumerated and reconciled in one table | **`03_` §4** | supersession markers |
| `R2-F-17` | **CONFIRMED** | membership settled per condition: **`2` genuine circular defects, `1` misclassified, `1` relocated**; `14_` §5's *"`3` → `0`"* shown unsupported | **`03_` §5** | none |

---

## 3. FINDINGS RAISED BY THIS SESSION — beyond the `17`

| ID | Finding | Severity | Where |
|---|---|---|---|
| **`CORR2-IPA-02`** | **Round 1's independence is a display-name change on the audited party's own credential** — the address is identical across `12 of 12` canonical commits | **MATERIAL** | `02_` §3 |
| **`CORR2-FD-01`** | **`3` open `CORR1` obligations dropped** (`CORR1-F-02`, `CORR1-F-03`, `CORE-03`) **and the identifier `CORE-07` re-used** for a different obligation, announced as *"new"* | **MATERIAL** | `10_` §2 |
| **`CORR2-XW-01`** | **`Purchase → Inventory` is in neither the declared `12` nor the tested `18`** — goods receipt, the primary inventory inflow | **MATERIAL** | `06_` §5 |
| **`CORR2-XW-02`** | **Declared class `12` is covered by no contract row**, and no accounting-period object exists | **MATERIAL** | `06_` §6 |
| **`CORR2-COV-01`** | **Configuration and Optional-Function Reachability have NO declared population** — two applicable dimensions are unmeasurable | **MATERIAL** | `09_` §4 |
| **`CORR2-BDP-01`** | Open-Boss-decision register conflates **open** with **askable**, and applies the rule in **both directions in adjacent rows** | **MATERIAL** | `05_` §3 |
| **`CORR2-BDP-02`** | `BOSS-CORR1-01` dropped in silence — `9` files → `0` | **MATERIAL** | `05_` §3 |
| **`CORR2-MF-01`** | The `MF-03` contradiction is **internal to the frozen package**; Round 2 went off-baseline unnecessarily and mis-classified `T8` as undischargeable | **MODERATE** | `07_` §1 |
| **`CORR2-MF-02`** | The `Standard`-costing asymmetry holds only if the **standard cost is itself independent of the migration** — untested; in a cutover it is migrated data | **MODERATE** | `07_` §7 |
| **`CORR2-XW-03`** | `05_` publishes the crosswalk as complete for the legs it derived while `CORE-04` is open on the whole; the un-derived leg carried both material findings | **MODERATE** | `06_` §6 |

**`7` MATERIAL · `3` MODERATE = `10` new findings**, none of which either B-7 round raised.

*(This package defines `14` `CORR2-*` identifiers. The `4` not listed above are `CORR2-IPA-01`, `-03`,
`-04` and `-05`: `-01` is Round 2's own `R2-F-01` confirmed rather than a new finding, `-03` is its
consequence for exit condition `2`, and `-04` and `-05` are **recorded in the executor's favour**. The
`10` above are the findings this session raises **against** the package.)*

---

## 4. AUDIT OF THIS DISPOSITION TABLE — the check the programme has previously failed

**Claim under test:** *every `Landed in` cell names an artefact and section that exists in this package
and carries the corrected value.*

```
POPULATION : the 17 "Landed in" cells above
UNIT       : (finding, artefact) pair
PATTERN    : does the named CORR2 artefact exist, and does it carry the finding's corrected value?
PATH SET   : CORR2_REMEDIATION_2026_09_10/**

01_  exists   carries R2-F-02, -03, -04, -09, -10  as re-measured values          OK
02_  exists   carries the independence classification and the withdrawal          OK
03_  exists   carries denominator 14, the 4-denominator reconciliation, CGD set   OK
04A_ exists   carries the 194-branch negative and the ratification question       OK
05_  exists   carries the 4-decision population and the conflation finding        OK
06_  exists   carries the full crosswalk, the N/A re-classification, both gaps    OK
07_  exists   carries the 11-property comparison and NOT DECIDABLE                OK
08_  exists   carries the 21-row audit and supersedes 10_ §1                      OK
09_  exists   carries ZT-04 and ZT-05                                             OK
10_  exists   carries the restored obligations and CORE-07 collision              OK

CELLS NAMING AN ARTEFACT THAT DOES NOT EXIST      0
CELLS WHOSE ARTEFACT DOES NOT CARRY THE VALUE     0
FINDINGS DISPOSITIONED IN PROSE ONLY              0
```

**Every correction is in a register, not only in this table.**

---

## 5. WHAT WAS NOT CORRECTED, AND WHY

| Not corrected | Reason |
|---|---|
| `10_`, `14_`, `08_`, `05_`, `09_` of the recovery package | **superseding artefacts published; `0` prior files modified.** The method is the package's own and was verified legitimate |
| `d878a603`'s verdict text | **audit lineage. Preserved unmodified**, including the `3` accounts this session corrected |
| `5bd36d62`'s verdict text | audit lineage, preserved |
| The `B4′` `12`-member denominator | **Boss-reserved.** Evidence only (`13_`) |
| `MF-03`'s classification | **NOT DECIDABLE.** Re-asserting either class would repeat the defect |
| `CORE-07`'s collision, in the source files | recorded and renamed **forward**; prior files unmodified |

---

## 6. CHECKPOINT

> **`17` dispositioned · `15` CONFIRMED · `2` MODIFIED · `0` DISPROVED · `0` lost ·
> `17 of 17` corrections landed in a named artefact and section, **audited mechanically** ·
> `0` corrections exist only in this table · **`10` new findings raised by this session, `7` MATERIAL** ·
> `0` prior artefacts modified · `0` evidence waived.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the sole Final Approver.**
