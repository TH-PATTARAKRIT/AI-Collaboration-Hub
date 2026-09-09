# SA_AR_01 — FINAL-GATE BASELINE REPRODUCTION

## CP-SA-AR-10 — FINAL-GATE BASELINE REPRODUCED

Parent publication `9d5bc2db` · package `.../PHASE_SA_FINAL_BOSS_GATE_2026_09_09/` (13 files + manifest)
**Reproduced before any conclusion was changed.**

---

## 1. RESULT

**Twelve of the thirteen controlling figures reproduce exactly. One does not, and the parent package
contains its own contradiction.**

> ## `AR-F-01` — the headline **"26 surviving Boss decisions"** counts `F5` by **identifier**, while `F5`'s own decision card counts it by **decision**. On the decision unit the figure is **24**.

**Nothing about what Boss is asked changes.** Same 8 families, same 8 questions, same substance. What
changes is the number printed on the front of the pack, and a number on the front of a de-duplication
pack has to be right.

---

## 2. THE THIRTEEN FIGURES

| # | Figure | Parent | Reproduced | Instrument |
|---:|---|---|---|---|
| 1 | Package integrity | 13 files, manifest 13/13 | **13/13 `OK`** | `shasum -a 256 -c` over the archived tree |
| 2 | Surviving Boss decisions | **26** | **24** — see §3 | atomic re-decomposition against primary source |
| 3 | Decision families | 8 (`F1`–`F8`) | **8** | card headings |
| 4 | Boss acts | 5 | **5** — `B-7`, `C4-D-01`, `C4-D-02`, `AAS-V-02` discharge, Thai panel | `SA_FINAL_03` §4 rows, enumerated |
| 5 | Scope clarification | 1 (`FG-F-06`) | **1** | `SA_FINAL_06` §3.2 |
| 6 | Active vetoes | 6 | **6** — `AAS-V-01`, `-02`, `-03`, `RC-V-01`, `CF-V-01`, `CF-V-02` | distinct identifiers in the register |
| 7 | Vetoes discharged by self-action | 0 | **0** | every row's disposition names an issuer or Boss |
| 8 | Category 3 before the merge | 1 | **1** — the PMO act, and **only** it | `SA_FINAL_04` §4 has 13 obligation rows; exactly one is graded `3` |
| 9 | Category 3 owned by SMEs Core / document owner | 0 | **0** | same table |
| 10 | Independence | none completed | **none** | `SA_FINAL_06` §5 |
| 11 | `EC-07` clean independent passes | 0 of 2 | **0 of 2** | `SA_FINAL_06` §3.2 grading table |
| 12 | `E2E-07` | `TRAVERSABLE` | **`TRAVERSABLE [FG]`** | class column, `SA15` v2 §3 |
| 13 | `E2E-04` re-grade | withdrawn | **withdrawn** — row reads `NOT TRAVERSABLE`, §2 records the withdrawal | same |

**Scenario register, three shapes.** Class column of the 18 mandated rows → **2 / 15 / 1**. Summary
table → **2 / 15 / 1**. Identifier enumeration of the summary → **18 distinct, each appearing exactly
once**, `E2E-01`…`E2E-18` complete. **All three agree.**

**Verdict wording.** No affirmative `PASS` / `CERTIFIED` / `COMPLIANT` verdict is issued in the parent
package; every hit is an exit-criterion name, a quotation, a negation, a prohibition, or the package's
own sweep pattern.

---

## 3. `AR-F-01` — THE COUNT, SETTLED AT PRIMARY SOURCE

### 3.1 What the parent package says in two places

| Where | What it says |
|---|---|
| `SA_FINAL_02` §2 population table | `B5` decomposes to **6** atoms — `BLK-07` restatement, `BLK-08` restatement, **veto limb 2 restatement**, `POH-D-01`, `POH-D-02`, `POH-D-06` — **less 1** because *"`POH-D-06` **is** the three-restatement act and is not a seventh atom"*. Net **5** |
| `SA_FINAL_03` §1 summary table | `F5` **Members = 8**; **Total = 26**; *"Non-`F5` families sum to 18; 18 + 8 = 26"* |
| `SA_FINAL_03` `F5` decision card | *"**Eight identifiers, six decisions**; the three restatement subjects are one act"* |

**Six decisions and eight members cannot both be `F5`'s contribution to a total described as
"decisions".** The parent round corrected `27 → 26` by removing one double-count and left the unit
unrepaired: it fixed the number, not what the number counts.

### 3.2 What the primary register says

`SA_CORR3_03_PRODUCTION_OVERHEAD_PROOF.md` — read on `origin/architecture/phase-sa-corr3-proof-verification-2026-09-09-001`, the branch that owns it — defines **six** decisions and no more:

| Id | Subject, verbatim |
|---|---|
| `POH-D-01` | *"Confirm the declared departure from `BD-04`"* |
| `POH-D-02` | *"Depreciation-method election: straight-line absorbed at normal capacity, or units-of-production absorbed at normal capacity"* |
| `POH-D-03` | *"Is SETUP time productive?"* |
| `POH-D-04` | *"Are IDLE and NO_DEMAND one cause or two?"* |
| `POH-D-05` | *"Who owns the normal-capacity figure, and the review cadence"* |
| `POH-D-06` | **"`BLK-07` and `BLK-08`: confirm, or restate"** |

**Two things follow, and both cut against the parent's decomposition.**

1. **`POH-D-06` has two subjects, not three.** `BLK-07` and `BLK-08`. The register's own summary line
   reads *"`POH-D-01`, `POH-D-02`, `POH-D-06` returned by…"* — three `D` items from that group, never
   five or six.
2. **"Veto limb 2 restatement" is not a Boss decision at all.** Limb 2 is `POH-G-03` — a **`G`** item,
   an SMEs Core design gap: *"Veto limb 2 is undischarged and, as written, undischargeable."* The
   parent pack itself files limb 2 under `F5`'s **"Affected vetoes"** row, not its decision row. It was
   promoted into the decision population by the decomposition and nowhere else.

### 3.3 The corrected arithmetic

| CORR5 row | Atoms, decision unit |
|---|---:|
| B1, B2, B3, B4, B7, B8, B9, B12, B15 — one each | 9 |
| B5 → `POH-D-01`, `POH-D-02`, `POH-D-06` | **3** *(parent: 5)* |
| B6 → `XMC-D-01`, `C2-D-02` | 2 |
| B10 → `RC-D-01`…`-04`, `CF-D-01`, `CF-D-02` | 6 |
| B11 → `TV6-BOSS-01`, `TV6-BOSS-02` | 2 |
| B13 → `POH-D-03`, `-04`, `-05` | 3 |
| B14 → the five acts | 5 |
| **Candidates** | **30** *(parent: 32)* |
| less relocated to `ERPPLUS-152` (prepaid wallet) | −1 |
| less acts, not decisions | −5 |
| **Surviving Boss decisions** | **24** *(parent: 26)* |

**Second shape — sum the families instead of the rows:**

`F1` 2 · `F2` 3 · `F3` 2 · `F4` 2 · **`F5` 6** · `F6` 4 · `F7` 4 · `F8` 1 = **24**.
`24 + 1 relocated + 5 acts = 30` ✓ — the two shapes close on both the surviving figure and the
population.

### 3.4 Why this is worth a finding rather than a silent edit

**This is the fourth appearance of one defect class in this chain.** CORR5 committed it (`CHB-04`,
namespace singletons). The final gate committed it twice — `CHF-01`, which produced the `27 → 26`
half-correction now being completed, and the `SA15` §2/§3 divergence its own sweep caught. **The
package whose entire subject is "count the Boss decisions correctly" has now miscounted the Boss
decisions in three consecutive rounds, each time in the same family, `F5`.**

The programme's own rule covers it exactly: **declaring a population does not save a count whose unit
is conflated.** `F5` is the only family whose members are not one-identifier-one-decision, so it is the
only place the unit can slip, and it is where it slipped every time. **Controls belong where the last
defect was.**

---

## 4. WHAT DOES **NOT** CHANGE

| | |
|---|---|
| The eight questions Boss answers | **unchanged** |
| `F5`'s content | **unchanged** — restate `BLK-07`/`BLK-08`, plus the five elections under them |
| Any scenario, invariant, veto or dimension cell | **unchanged** |
| Category 3 | **unchanged** by this finding |
| The recommendation | **unchanged** by this finding |

**`AR-F-01` corrects a headline, not a conclusion.** It is published at this size because a
de-duplication register that cannot count its own output is the one artefact whose arithmetic a
reader is entitled to trust without re-deriving it — and three rounds running, that trust would have
been misplaced.

## 5. Checkpoint

> ## `CP-SA-AR-10 — FINAL-GATE BASELINE REPRODUCED`
> **12 of 13 figures reproduce exactly; 1 is corrected by `AR-F-01` (26 → 24 decisions, 32 → 30
> candidates) against the primary overhead register, on two agreeing shapes. Manifest 13/13. Scenario
> classes 2/15/1 on three shapes. 0 conclusions changed.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
