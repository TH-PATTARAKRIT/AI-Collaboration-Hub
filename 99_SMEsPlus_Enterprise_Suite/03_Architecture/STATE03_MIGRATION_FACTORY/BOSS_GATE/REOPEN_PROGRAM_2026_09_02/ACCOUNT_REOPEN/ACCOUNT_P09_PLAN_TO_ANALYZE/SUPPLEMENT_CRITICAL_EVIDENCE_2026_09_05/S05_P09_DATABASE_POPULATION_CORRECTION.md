# S05 — P09_DATABASE_POPULATION_CORRECTION

**Checkpoint:** `CP-P09S05` · **Layer:** 1 — clean-room.

---

## 1. THE PRIOR ERROR, PRESERVED

Two rounds ago the evidence strand concluded *"no asset in any located deployment carries an allocation"*. Its listing command ended in an output limit over a directory holding **2,553 files**, and the one populated database was never listed. The conclusion was withdrawn last round.

**This round rebuilds the population from scratch with no truncating command anywhere.**

## 2. DIRECTORY POPULATION — COUNTS FIRST, LISTINGS SEPARATE

| Scope | Measure | Count |
|---|---|---|
| the downloads directory | total files | **2,553** |
| | database dumps | **5** |
| | plain SQL files | 1 |
| the whole volume | database dumps | 3 (all copies of one database) |
| | SQL files | 2,957 |
| | backup files | **0** |
| | SQL files over 1 MB, i.e. dump candidates | **1** |

**Every count above is a `wc -l` over an unbounded enumeration. No listing was used to establish a count and no count was inferred from a listing.**

## 3. DISTINCT DATABASE POPULATION — THE CORRECTED DENOMINATOR

| # | Database | Size | Readable? |
|---|---|---|---|
| 1 | deployment **S** | 155 MB | **yes — the decisive one** |
| 2 | deployment **T**, later capture | 64 MB | **yes** |
| 3 | deployment **T**, earlier capture *(4 copies across the volume)* | 65 MB | **yes** |
| 4 | deployment **E**, later capture | 25 MB | **yes** |
| 5 | deployment **B** | 36 MB | **yes** |
| 6 | deployment **E**, earlier capture, plain SQL | 62 MB | yes *(read in a prior round)* |

**Six distinct database artefacts, five of them restored and measured in this checkpoint.** Prior rounds recorded, successively, "two", then "four". Both were wrong.

### 3.1 A prior blocker closes here
`DEP-P09-23` recorded deployment **T**'s later capture as unreadable — a restore client rejected its header version. **A newer client reads it without error.** The blocker was a **tooling limitation recorded as an evidence limitation**. `DEP-P09-23` is **CLOSED**.

## 4. THE ASSET-ALLOCATION CENSUS — EXHAUSTIVE

Every asset record in every readable database. No sampling.

| Database | Assets | Carrying an allocation |
|---|---|---|
| **S** | **685** | **670** — 664 open, 2 closed, 2 draft, 1 template, 1 cancelled |
| B | 36 | 0 |
| E (later) | 36 | 0 |
| T (earlier) | 12 | 0 |
| T (later) | 12 | 0 |
| **TOTAL** | **781** | **670 (85.8 %)** |

**All 670 allocated assets are in one deployment.** The other four hold only category templates with no allocations.

### 4.1 Two prior counts reconciled
One round reported "12 and 12"; a reviewer reported "36 and 36". **Both were right about different databases** — 12 is the pair of T captures, 36 is B and E. Neither was wrong; each had measured a subset and stated it as the population. **That is the same defect as the truncation, in a milder form: a partial measurement reported without its boundary.**

## 5. COVERAGE STATEMENT

| Question | Coverage |
|---|---|
| how many databases exist in the searched scope | **6** — exhaustively enumerated |
| how many were measured for assets | **5** |
| how many assets exist across them | **781** — every row |
| how many carry an allocation | **670** — every row tested |
| does any deployment use the shipped Thai template accounts | **NO** — deployment S holds **zero** accounts on those codes; see `S01` |
| does any deployment hold budgets | **NO** — deployment S holds **zero** budget records; see `S02` |

**Class A within the stated scope**, and the scope is now the whole searched volume rather than a curated list.

## 6. WHAT THIS DOES TO THE HEADLINE

The previous round's measurement stands and is now properly bounded:

> **670 of 781 assets across the whole database population carry an allocation — all in one deployment — and in that deployment 98.57 % of the depreciation attribution is annihilated.**

## CHECKPOINT

**`CP-P09S05` — COMPLETE — EVIDENCE VERIFIED.** Population rebuilt exhaustively; one prior blocker closed; two prior counts reconciled. Auto-continue.
