# 26 — SOURCE PRESENCE CLOSURE MATRIX

# `18 FAILING ROWS WORKED · 12 CLOSED · 6 STILL BELOW FLOOR · 5 NEW ROWS ADDED`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Authority: `§16` of the ruling prompt · Boss: **SOLE FINAL APPROVER**

> **`§16`: no percentage may be improved by denominator shrinkage, unsupported exclusion, `N/A`
> manipulation, duplicate removal without evidence, or scope rewriting.** Every closure below is
> attributed to one of exactly four causes, and the cause is named per row: **`[R]`** Boss ruling ·
> **`[E]`** an error of this session corrected · **`[W]`** work performed this session ·
> **`[D]`** denominator changed by the ruling.

---

## 2. `CORR2-SPC-01` — MATERIAL · A PATH-SET ERROR OF THIS SESSION'S OWN

**Found by re-running `09_`'s own instrument at a wider path set, as `§22` requires.**

`08_` rows `9`–`12` classified the `IR` and `AR` denominators **`UNSUPPORTED`** and
**`EVIDENCE OUTSIDE PATH SET`**, on this measurement:

```
09_/08_ declared PATH SET : NEW_SESSION_2026_09_10/**          (80 files)
  max distinct IR-nn in any file                    6
  max distinct AR-nn in any file                   10
  conclusion published: "membership NOT NAMED"
```

**Re-run at the frozen tree, which is where the cited authority actually lives:**

```
PATH SET : STATE03_MIGRATION_FACTORY/**             (779 files)
  SA_CORR2_05_INVENTORY_CONVERGENCE_RECONCILIATION.md   IR-01..IR-18   18 distinct, 18 rows
  SA_CORR2_06_ACCOUNTING_CONVERGENCE_RECONCILIATION.md  AR-01..AR-29   29 distinct, 28 rows
  POSITIVE CONTROL  IR-99 -> 0   (the instrument discriminates)
```

> **`SA_CORR2_05` and `SA_CORR2_06` are on the frozen tree. They were outside the path set I declared,
> not outside the evidence base.** `08_` treated *"outside my declared boundary"* as *"unsupported"* —
> **the exact evidence-location defect this package spends `04A_` and `07_` documenting.**

**Rows corrected: `4`.** `IR 20` · `IR reconciled 14` · `AR 30` · `AR reconciled 15` — all four move
from `DEFECTIVE` to **`SOUND`**.

### 2.1 The memberships, now enumerated rather than asserted

```
IR   18 base rows measured:  RECONCILED 14 · PARTIAL 3 · NOT RECONCILED 1
     + MF-01, MF-02 (B9', both NOT RECONCILED)
     = 20 :  14 / 3 / 3     <- reproduces the published "IR 14/3/3" EXACTLY
     RECONCILED members: IR-01 .. IR-14

AR   29 base ids over 28 rows (one row carries AR-13 and AR-14):
       RECONCILED 12 · PARTIAL 14 · NO POSTING BY DESIGN 3  (AR-07, AR-08, AR-09)
     + MF-01 (B9', NOT RECONCILED)
     = 30 :  15 / 14 / 1    <- reproduces the published "AR 15/14/1" EXACTLY,
                               treating NO POSTING BY DESIGN as reconciled
     RECONCILED members: AR-01..AR-06, AR-07*, AR-08*, AR-09*, AR-10, AR-13, AR-14,
                         AR-15, AR-16, AR-28        (* NO POSTING BY DESIGN)
```

**Two published decompositions reproduce to the row.** `06_`'s `IR 14/3/3` and `AR 15/14/1` were
correct, and `08_` was wrong to call their membership unsupported.

### 2.2 My own instrument failures in this measurement — reported, not repaired silently

| # | Failure | Detection | Correction |
|---:|---|---|---|
| `1` | status-column extractor took the **last** pipe field, which is empty because rows end with `\|`. It returned **`0` verdicts for every row** — a clean zero indistinguishable from a file with no verdicts | implausibility: `18` rows, `0` verdicts | scan cells in reverse for a verdict token |
| `2` | verdict vocabulary was `{RECONCILED, PARTIAL, NOT RECONCILED}`. **`3` `AR` rows carry a fourth class, `NO POSTING BY DESIGN`**, and returned `None` | arithmetic: `12 + 14 = 26 ≠ 29` | rows read directly; the class is what closes `AR` to `15` |
| `3` | `AR` **row count `28` ≠ id count `29`** — one row carries two identifiers | row/id comparison run as a matter of course | **the unit is the identifier, not the row**; both counts published |

> **Failure `2` is the one that mattered.** Had `12 + 14` summed to `29`, the missing class would never
> have been looked for and `AR`'s published `15` would have been reported as irreproducible.

---

## 3. THE `18` FAILING ROWS, WORKED

| # | Row | Was | **Now** | Cause | Basis |
|---:|---|---:|---:|:-:|---|
| `1` | Classes reached by a contract row | `91.7 %` | **`70.6 %`** | **`[D]`** | denominator `12 → 17`; **coverage falls because the true scope widened** (`21_` §2.1) |
| `2` | Contract rows reaching a class | `90.0 %` | **`100 %`** ✔ | **`[R]`** | row `4` now reaches `BC-17` |
| `3` | Applicable `XMC-H` rows contract-sufficient | `0 %` | **`0 %`** | — | unchanged; `0 of 16` |
| `4` | Contract rows contract-compliant | `0 %` | **`0 %`** | — | `SA_CORR4_02` §5 states it itself |
| `5` | `N/A` rows carrying their defeating condition | `0 %` | **`100 %`** ✔ | **`[R]`+`[W]`** | `20_` §4 — all `8` required attributes determined for `XMC-H-15`/`-16` |
| `6` | `IR` membership enumerated | `30.0 %` | **`100 %`** ✔ | **`[E]`** | §2 — my path-set error |
| `7` | `AR` membership enumerated | `33.3 %` | **`100 %`** ✔ | **`[E]`** | §2 |
| `8` | `MF-03` discriminators tested | `16.7 %` | **`100 %`** ✔ | **`[W]`** | `25_` §3 — all `13` compared |
| `9` | Re-placements on external authority | `75.0 %` | **`100 %`** ✔ | **`[R]`** | `17_` §1.3 — express exemption supplies the fourth authority |
| `10` | `SC-54` governing clauses applied | `66.7 %` | **`100 %`** ✔ | **`[R]`** | cl. `5` expressly addressed |
| `11` | Exit conditions satisfied | `35.7 %` | **`50.0 %`** | `[R]`+`[E]` | `19_` — `+1` by ruling, `+1` by corrected error |
| `12` | Readiness scenarios `WRITABLE` | `81.8 %` | **`81.8 %`** | — | **`B5′` unruled; `PROVISIONAL`.** Not closable below Boss, and **not re-asked** |
| `13` | Denominators with sound named membership | `47.6 %` | **`100 %`** ✔ | `[E]`+`[W]` | `30_` §2 — re-derived on the **current** `26` denominators |
| `14` | Open Boss decisions correctly carried | `25.0 %` | **`100 %`** ✔ | **`[W]`** | `05_`/`13_` carry all `4`; askability recorded separately |
| `15` | `CORR1` open obligations carried forward | `0 %` | **`100 %`** ✔ | **`[W]`** | `24_` — `3` restored |
| `16` | Identifiers free of redefinition | `0 %` | **`100 %`** ✔ | **`[R]`+`[W]`** | `24_` §3 — `CORE-07`/`CORE-08` resolved as ruled |
| `17` | FD blockers closed | `0 %` | **`10.0 %`** | **`[R]`** | `29_` — `2 of 20` closed |
| `18` | Ruling acts with a durable artefact | `0 %` | **`100 %`** ✔ | **`[R]`+`[W]`** | `17_` created **before** application; `R-D-01` has no residual independent effect (§4) |

**Counted from the table above, not asserted:**

```
rows meeting 96%+ : 2, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 18   = 12
rows below floor  : 1, 3, 4, 11, 12, 17                        =  6
CHECK  12 + 6                                                  = 18  OK
```

> **Correction applied to this file's own headline before publication:** the summary line first read
> *"`9` closed · `9` still below"*. **Counting the table returns `12` and `6`.** The headline is
> corrected to **`12 closed · 6 still below`**, and the error is left visible here rather than
> overwritten, per `§22`.

---

## 4. `R-D-01`'S RESIDUAL EFFECT — measured, because row `18` depends on it

| Question | Answer |
|---|---|
| Does `R-D-01` still have independent constitutional effect? | **NO** |
| Why | `BOSS-CORR2-RD01` rules on **all four** re-placements: `9`, `10`, `12` re-placed; condition `11` **retained with its limbs separated**. Every act `R-D-01` performed is now performed by a ruling **with a durable record** (`17_`) |
| Is `R-D-01`'s missing artefact therefore cured? | **The defect is not erased — it is superseded.** `04A_` remains as lineage. **`ZT-08` is measured on acts *in force*, and all `3` in force are recorded** |
| Authority acts in force | `BOSS-CORR2-RD01` · `BOSS-CORR1-01` · `BOSS-CORR2-IND` — **`3`, all at `17_`** |

---

## 5. THE `6` THAT REMAIN BELOW FLOOR

| Row | Coverage | Why it cannot close at this phase | Owner | Closable below Boss? |
|---|---:|---|---|---|
| `1` classes reached by a contract row | **`70.6 %`** | the `10`-row register is a **different unit** — emitting flows, not boundary classes. `5` classes cannot be expressed in its shape (`21_` §5) | Architecture / Contract Semantics | **YES** — a contract register whose unit is the boundary class |
| `3` `XMC-H` rows contract-sufficient | **`0 %`** | `0 of 16`. Requires an **emitter-authored artefact** for each; `FINAL_SOLUTION` holds `30` paths, **`0` outside `INVENTORY`** | SMEs Core per module | **YES**, and it is the largest single body of work in the programme |
| `4` contract rows contract-compliant | **`0 %`** | *"does not mean built, proven, verified or compliant"* — compliance is a **Build/Test** property | — | **NO — phase.** Deferred with contract |
| `11` exit conditions satisfied | **`50.0 %`** | `7` conditions fail on their own merits (`19_`) | mixed | partly |
| `12` readiness `WRITABLE` | **`81.8 %`** | **`B5′` unruled** — the figure is `PROVISIONAL` by authority, not by evidence | **Boss** | **NO** — and **not re-asked**, per `§20` |
| `17` FD blockers closed | **`10.0 %`** | `18 of 20` open (`29_`) | mixed | partly |

---

## 6. NEW ROWS ADDED BY THIS ROUND

**Declaring two populations and expanding the boundary set creates measurements that did not exist.
They are added, not hidden.**

| Row | Denominator | Numerator | Coverage | Floor | Verdict | Source |
|---|---:|---:|---:|---:|---|---|
| Declared classes with an `XMC-H` row | `17` | `16` | **`94.1 %`** | `96 %` | **HOLD** | `20_` §5 — `BC-17` |
| `BC-17` mandatory chain legs proven | `4` | **`0`** | **`0 %`** | `96 %` | **HOLD** | `21_` §4 |
| Configuration items with a complete semantic contract | `12` | `5` | **`41.7 %`** | `96 %` | **HOLD** | `22_` §6 |
| Optional functions with a complete contract | `8` | `1` | **`12.5 %`** | `96 %` | **HOLD** | `23_` §6 |
| Conditional applicability items fully attributed | `2` | `2` | **`100 %`** | `100 %` | **MEETS** | `20_` §4 |

**`5` new rows · `1` meets · `4` below floor.**

> **`CORR2-SPC-02` — MODERATE.** Closing `12` rows and adding `4` failing ones is the correct outcome of `§12`
> and `§13`, **not a regression**. A dimension that could not be measured was reported as
> *"unmeasurable"*; it is now measured and fails. **The package is more honest and no better.**

---

## 7. WHAT WAS **NOT** DONE TO IMPROVE A PERCENTAGE

| Prohibited | Confirmed not done |
|---|---|
| denominator shrinkage | **`0`** — the boundary denominator **rose** `12 → 17`, exit **held** at `14`, FD blockers **rose** `11 → 20` |
| unsupported exclusion | **`0`** — `XMC-H-15`/`-16` are `CONDITIONAL`, not `N/A`; `MF-03` is `UNRESOLVED`, not excluded; lot/serial excluded as **UNPROVEN, not absent** |
| `N/A` manipulation | **`0`** — `N/A` count is unchanged and both instances are re-classified **more strictly** |
| duplicate removal without evidence | **`0`** — the `AR-13`·`AR-14` shared row is reported, not collapsed |
| scope rewriting | **`0`** — scope was widened **by Boss**, and every measure that worsened is published |

---

## 8. CHECKPOINT

> **`18` failing rows worked individually · **`12` closed to `≥ 96 %`, `6` remain below** ·
> `5` new rows added, `4` of them failing · **`CORR2-SPC-01`: `4` rows were wrong because of a
> path-set error of my own — `SA_CORR2_05`/`06` are on the frozen tree** · both `IR` and `AR`
> decompositions **reproduce to the row**, memberships now enumerated ·
> **`3` of my own instrument failures reported, one of which changed a result** ·
> this file's own headline count **corrected from `9/9` to `12/6` by counting its own table** ·
> **`0` percentages improved by any prohibited means.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
