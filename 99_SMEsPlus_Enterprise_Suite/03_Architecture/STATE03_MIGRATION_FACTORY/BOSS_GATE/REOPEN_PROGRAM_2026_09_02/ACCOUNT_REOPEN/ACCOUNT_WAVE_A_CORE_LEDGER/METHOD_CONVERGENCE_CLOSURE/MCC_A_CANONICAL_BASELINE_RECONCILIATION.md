# MCC_A — CANONICAL BASELINE RECONCILIATION

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · commit `33cdc6fa009c4eafcca543c253ccad19e97fd0dc`
Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001` · Standard `SMEPLUS-DR-MC-001`
Depth `VERY DEEP / L99999.99999`

> **Recommendation only. Boss is the sole Final Approver. No `PASS` is declared here.**

---

## 1. Parent package verification — done before anything else

| Check | Method | Result |
|---|---|---|
| Parent commit exists | `git log -1 --format='%H %ci %s' 33cdc6fa009c4eafcca543c253ccad19e97fd0dc` | **VERIFIED.** `2026-09-04 11:58:22 +0700`, subject *"research(account-wave-a): method convergence round — enumeration universe, GB-04 root cause, MC-01..MC-10, fresh independent convergence review"* |
| This session's branch derives from it | `git checkout -b research/account-wave-a-mcc-2026-09-04-001 33cdc6fa…` in a **fresh clone** | **VERIFIED.** Lineage `33cdc6f ← 56288c4 ← aea4853 ← dd61e40 ← 93ad4d5` |
| Method Convergence Standard present | file exists at `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/SMEPLUS_DEEP_RESEARCH_METHOD_CONVERGENCE_STANDARD.md` on this branch | **VERIFIED** (added by `aea4853`) |
| Canonical baseline file count | `find … -name '*.md' -not -path '*/METHOD_CONVERGENCE/*' \| wc -l` | **64** — reproduces the parent figure exactly |
| Parent MC package file count | `find …/METHOD_CONVERGENCE -name '*.md' \| wc -l` | **15** (12 numbered + 3 `LAYER2_MC_EVIDENCE`) |
| Primary source reachable | `SRC-A` … `SRC-F` re-tested this session | **VERIFIED.** See `MCC_C` §1 |

**Working-surface correction of record.** The parent round recorded (`MCE-012`) that a stale working
copy produced a false negative. This session avoided the class by cloning fresh from `origin` and
branching from the **verified commit hash**, not from a folder. The declared working surface of this
session is that clone and nothing else, plus the read-only Layer 2 source roots named in `MCC_C` §1.

---

## 2. Canonical status of each targeted object, as inherited

Reconstructed by reading the parent artefacts, **not** by restating the parent gate report.

### 2.1 `GB-03` — inconsistent company scoping over one rate table

| Round | Position | Source |
|---|---|---|
| `CORR1` (`93ad4d5`) | Raised. Rate-table scoping inconsistent across paths | `C05`, `C06` |
| `GAPCLOSE` (`dd61e40`) | **Four** distinct company-scoping rules over one rate table. `FX-08` reported **closed with evidence** as a `VERIFIED DEFECT` | `G02` §B1-02, `G03` §8, `G10` §2 |
| `MC` (`33cdc6f`) author pass | **Six** rules, "complete". Rules 5 and 6 new | `MCE-007` |
| `MC` fresh review | `MCE-007` **INVALID in its central mechanism**; rule count **≥9**; `MCE-007` rules 3 and 5 **withdrawn as characterised**; `P-08a` reverted `ENUMERATED → HOLD` | `MCX-02`, `MCX-03` |
| `MC` gate | **`GB-03` RE-OPENED** | `11` §7 |

**Inherited status carried into this round: `RE-OPENED`, rule count `≥9` and not bounded,
`FX-08` closure resting on evidence never tested against a model-level constraint layer.**

### 2.2 `FX-08` — branch-company rate context

Recorded mechanism (`G03` §3): *"the writer stores `company_id = <branch>` and the resolver looks
for `company_id ∈ (NULL, <root>)`. The two do not intersect."*
Recorded disposition (`G03` §8): **`VERIFIED DEFECT`**.
Recorded residuals: `FX08-R1` class `C`, `FX08-R2` class `C` (later claimed closed by `MCE-007`,
then **re-opened** by `MCX-02`), `FX08-R3` `INFERENCE`.

### 2.3 `MCU-13` — the re-verification instruction

`MCD-02 — GATING`: *"`FX-08` requires targeted re-verification against
`base/models/res_currency.py:458-462`."* The parent round explicitly declined to declare `FX-08`
invalid, on two stated grounds: `G03` holds verified facts it did not re-read, and *"a constraint can
be bypassed by paths that do not go through it (raw SQL: `P-21d` = 62 sites)."*

> **Both grounds are testable, and this round tests them.** `MCC_C` §4 and §5.

### 2.4 `AC-02` — corrected at the parent round

The raw-SQL rate path `base/models/res_currency.py:294-308` **includes** null-company rows and, via
`COALESCE(r.company_id, c.id)`, attributes each to **every** company — the opposite of the position
accepted at `G09`, in the more dangerous direction. Its sole consumer in the build is a
product-margin report, not an accounting consolidation table.

**Independently re-read this session at primary source. CONFIRMED in both particulars.** The `JOIN`
predicate is `(r.company_id is null or r.company_id = c.id)` and the projection is
`COALESCE(r.company_id, c.id) as company_id`. Nothing about that changed.

### 2.5 Gating unknowns

17 `GATING` (`MCU-01`…`MCU-17`), of which the parent round **opened three** (`MCU-13`, `MCU-16`,
`MCU-17`) and **closed none**.

### 2.6 Balanced-but-wrong

19 classes; register carries 27 cases; corrected floor **29** (two cases a reviewer asked to be
registered were lost — `RB-01`).

### 2.7 Negative claims

Four claims reached class `A — VERIFIED ABSENCE` in the programme's history, all at the parent round.
`MC-05` **NOT MET**: the negative-claim control was applied over 41.9% of the package by volume and
asserted over 100%.

---

## 3. Inconsistencies among parent registers — detected before new research

Required by the round instruction §4.4. Each was found by reading the registers against each other,
and each is recorded whether or not it favours this round.

### `MCC-BR-01` — the parent's own unknown denominator is 24 enumerated + 35 range-allocated, not 59 enumerated

**`VERIFIED FACT.`** File `06` §3 reports `Total enumerated: 59`. Reconstructed from its own body:

| Class | Ids | Individually stated? |
|---|---|---|
| `GATING` | `MCU-01`…`MCU-17` — 17 | **Yes**, one row each |
| `NON-GATING` | `MCU-20 … MCU-24` (5) · `MCU-25 … MCU-32` (8) · `MCU-33 … MCU-35` (3) = 16 | **No** — three grouped rows, one description each |
| `ROUTED` | `MCU-40 … MCU-46` (7) · `MCU-47` · `MCU-48 … MCU-54` (7) · `MCU-55` · `MCU-56` · `MCU-57` · `MCU-58` = 19 | **Partly** — 4 individually, 15 in three ranges |
| `OUT OF SCOPE` | `MCU-60`, `MCU-61` — 2 | Yes |
| `UNCLASSIFIED` | 5 orphan `GAP-*` ids | Yes (as orphans) |
| **Total** | **59** | **24 individually stated · 35 allocated inside a range** |

The arithmetic is sound. **The enumeration is not.** 59 is a count of allocated id slots. For 35 of
them no statement of the unknown exists — the same defect the round convicted the parent `41` of,
one layer down. **`MC-06` cannot be `MET` on this register.** Recorded as `MCC-D-01`.

### `MCC-BR-02` — register `21` is id-consistent; only the orphan claim survives

**`VERIFIED FACT`, and it partly exonerates register `21`.** Independent recount:

- Distinct id-bearing rows in register `21`: **28** — A 8 · B 4 · C 7 · D 7 · F 2.
- Its own `Counts` table: 8 + 4 + 7 + 7 + 2 = **28**. **Reconciles exactly.**
- Distinct `GAP-*` ids in register `21`: **14**. Distinct `GAP-*` ids cited across files `01`–`26`:
  **19**. Orphans: `GAP-A03`, `GAP-A04`, `GAP-C01`, `GAP-G01`, `GAP-H03` — **5**, confirming the
  parent's reduction of a reviewer's "six" to five.

> The parent round wrote *"Register `21`'s own count table totals **28**"* as evidence **against** the
> register. It is in fact evidence that register `21` is the **only** unknown artefact in the package
> that reconciles to its own count. The defect is confined to the 5 orphan ids. **Correction recorded
> in this round's favour is not the point; the point is that it was recorded at all.**

### `MCC-BR-03` — two id schemes, one denominator

**`VERIFIED FACT.`** Register `21` carries `GAP-*` (14), `TX-*` (7), `CL-*` (5), `FE-02`, `TI-05`,
`XM-01`. File `06` carries `MCU-*`. **No mapping between the two schemes exists in any file.** The
`41` and the `59` are therefore not two counts of one population; they are counts of **two
differently-keyed populations**, and no arithmetic can reconcile them. This is the true cause of the
non-reconciliation, and neither round named it. Carried to `MCC_E`.

### `MCC-BR-04` — `MCE-007` rule 6 was never withdrawn, and it is the accounting resolver

**`VERIFIED FACT.`** `MCX-02` withdrew `MCE-007` rules **3 and 5**. Rule **6**
(`account/models/res_currency.py:229`, `_check_company_domain(main_company)`) stands. It is cited
in `MCE-008` as *"the accounting currency table"*. Read at primary source this session, line `229`
is **not** the currency table; it is `_get_currency_table_fiscal_year_bounds`, a helper that finds
the **earliest rate row** in order to bound fiscal years. The currency table's own rate selection is
in four other methods in the same file and uses a **different** scoping expression. `MCE-008`'s
correction of `AC-02` was right about `_select_companies_rates`; its replacement attribution is
**imprecise**. Corrected in `MCC_C` §3.

### `MCC-BR-05` — `MC-06` reported `MET` on a register that fails `MC-01`

**`VERIFIED FACT`, method-level.** File `06` §4 declares `MC-06` *"MET for the population enumerated
here"* while file `11` declares `MC-01` **NOT MET** because the round's own surface was under-bounded.
A classification test cannot be `MET` over a population whose boundedness test failed, because the
denominator of the classification is the disputed object. **`MC-06` is re-run in `MCC_I` and does not
survive.**

### `MCC-BR-06` — the parent gate report's blocker table and file `06` disagree on `MCU-04`

**`VERIFIED FACT`, low materiality, recorded for lineage.** File `06` §2.3 **reclassifies** `MCU-04`
(report definitions carry no company dimension) from a routed medium unknown to `GATING`, and it duly
appears in the `GATING` table. File `11` §7 does not carry it into any blocker row. It is therefore a
gating unknown with no blocker. Not an arithmetic error — a **propagation** gap, i.e. `GB-06` acting
on the same round that discovered `GB-06`.

---

## 4. Correction lineage — preserved, not overwritten

Per `DR-NC-06`, nothing in the parent package is edited by this session.

| Artefact | Status under this round |
|---|---|
| `MCE00` | **Not edited.** Governed by `MCE02`, and now additionally by `MCC_C` where they conflict |
| `MCE02` | **Not edited.** `MCC-BR-04` corrects one attribution inside it; the correction is recorded here, not there |
| File `06` (unknown classification) | **Not edited.** `MCC-BR-01` and `MCC-D` govern |
| Files `01`–`26`, `CORR1/*`, `GAPCLOSE/*` | **Not edited.** `GB-06` remains open; this round does not silently repair it |
| `G03` (`FX-08`) | **Not edited.** `MCC_C` is the governing re-verification |

**Governing order established for this round and stated once:**
`MCC_* (this round) > MCE02 > MCE00 > GAPCLOSE > CORR1 > files 01–26`,
**for the specific claims each corrects, and for no others.**

---

## 5. Checkpoint A

> ## `BASELINE RECONCILED — WITH SIX RECORDED INCONSISTENCIES`

The parent package is internally readable, its lineage verifies, and its evidence base is intact.
Six inconsistencies were found among the registers **before** new research began; none prevents this
round from proceeding, and two (`MCC-BR-01`, `MCC-BR-03`) are themselves material findings that go to
`MC-06` and to the denominator reconciliation.

**This is not `BASELINE CONFLICT HOLD`.** No inconsistency found is of a kind that makes the
underlying evidence unusable — every one is a counting, keying or propagation defect above the
evidence layer, and in each case the primary source was re-readable and was re-read.

## 6. Progress at Checkpoint A

| Metric | Value | Denominator basis |
|---|---|---|
| `% MCC Phase completion` | **1 of 11** (9.1%) | Phases A–K, fixed by the round instruction |
| `% Baseline objects reconstructed` | **6 of 6** (100%) | `GB-03`, `FX-08`, `MCU-13`, `AC-02`, gating unknowns, balanced-but-wrong |
| `% Gating Unknown Closure` | **0 of 17** (0%) | inherited denominator, itself under test in `MCC_D` |
| `% Denominator reconciliation` | `PERCENTAGE NOT REPORTABLE — DENOMINATOR NOT VERIFIED` | two id schemes, no mapping — `MCC-BR-03` |
| `% Evidence coverage` | `PERCENTAGE NOT REPORTABLE — DENOMINATOR NOT VERIFIED` | the parent's own 95.5% figure is invalidated by an unapplied correction notice (`MCE02`) |

---

> ### FIGURE-GOVERNANCE NOTICE — appended mechanically, package-wide
>
> **`MCC_00_CANONICAL_FIGURES_REGISTER.md` governs every published figure and disposition in this
> package.** Where a figure in this file differs from a row in `MCC_00`, **`MCC_00` governs**; the text
> here stands unedited so the lineage is visible (`DR-NC-06`).
>
> This notice was appended to **every** Layer-1 file by one command, after the independent audit panel
> found that this round had failed to propagate its own last correction to three of its own files
> (`MCC_J` `J-16`). It is the mechanism, not the intention, that `ER-CORE-3` requires.
