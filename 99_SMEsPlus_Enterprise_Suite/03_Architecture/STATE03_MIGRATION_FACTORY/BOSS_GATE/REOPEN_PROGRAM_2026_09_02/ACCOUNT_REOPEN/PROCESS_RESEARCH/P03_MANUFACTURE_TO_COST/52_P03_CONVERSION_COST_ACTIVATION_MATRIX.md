# 52 — CONVERSION-COST ACTIVATION MATRIX

**LAYER 2 — AUDIT QUARANTINE.**

What each conversion-cost mechanism requires to become reachable, and the measured
population of each requirement in the two manufacturing-bearing databases.

---

## 1. The matrix

`S` = `iSMEs` · `T` = `iTEST02`.

| Mechanism | Required module | Required master data | Required transaction | `S` | `T` | Observed execution |
|---|---|---|---|---|---|---|
| **Machine cost → FG** (`M1`) | `mrp_account` | work centre **with a rate** | work order with duration | mod ✅ / data **0 WC** | mod ✅ / **1 of 60 rated** | `T`: 3 work orders, 1,200 min |
| **Labour relief** (`M2`) | `mrp_account` | as `M1` **+ expense account** | order reaches `done` | ✅ / **0** | ✅ / **0 of 60 have an expense account** | `T`: 4 done work orders on the rated centre |
| **Employee cost** (`M3`) | `mrp_workorder`, `mrp_workorder_hr_account` | employee rate **or** work-centre employee rate | time log with employee | **module ABSENT** | ✅ / **0 of 60 rates, 0 of 27 costs** | **none** |
| **Work-centre analytic** (`M4`) | `mrp_account` | work-centre `analytic_distribution` | duration change | ✅ / **0 WC** | ✅ / **0 of 60 populated** | **none** |
| **Project analytic** (`M5`) | `project_mrp_account` | project on the order + distribution | duration change | **ABSENT** | **✅ INSTALLED** / no distribution | **none — but reachable** |
| **Employee analytic** (`M6`) | `project_mrp_workorder_account` | project + employee | time log | **ABSENT** | **✅ INSTALLED** | **none — but reachable** |
| **Extra unit cost** (`M7`) | `mrp_account` | a human typing a value | order valuation | ✅ / **0 of 10,764** | ✅ / **0 of 163** | **none** |
| **WIP accrual** (`M8`) | `mrp_accountant` | company WIP accounts | wizard run | **ABSENT** | **✅ INSTALLED** | not measured — `UNR-P03-12` |
| **Standard cost from BOM** (`M9`) | `mrp_account` | BOM + operations | price recompute | ✅ / **0 routing ops** | ✅ / **154 routing ops** | operation term is 0 in `S`, non-zero possible in `T` |
| **Subcontract** (`M11`) | `mrp_subcontracting_account` | subcontractor | subcontract receipt | **ABSENT** | ✅ INSTALLED | not measured |
| **Depreciation → cost** | *no module supplies it* | — | — | **no path** | **no path** | **none** |
| **Maintenance / energy / indirect labour / overhead** | *no module supplies it* | — | — | **no path** | **no path** | **none** |

## 2. The activation gradient

Conversion cost requires **four independent things** to line up: module installed, master
data created, a rate entered, and a transaction executed. Measured:

| Gate | `iSMEs` | `iTEST02` |
|---|---|---|
| 1. Modules installed | **partly** — 5 key modules absent | **fully** — all 15 present |
| 2. Work centres exist | **NO — 0** | **yes — 60** |
| 3. A rate is entered | n/a | **1 of 60** (1.7 %) |
| 4. Work orders execute against it | n/a | **3 with duration > 0** |

> **`P03R-F-04`. The conversion-cost apparatus fails at a different gate in each database:
> `iSMEs` fails at gate 1–2 (five modules absent, zero work centres); `iTEST02` passes 1
> and 2, fails at gate 3 (59 of 60 work centres unrated) — and fails a **fifth** gate the
> first draft of this matrix omitted: `iTEST02` has **no real-time valuation and no
> valuation-layer table at all**, so no conversion cost could post even if every rate were
> filled in.** `FACT VERIFIED`.

**Gate 5 — valuation mode.** `_post_labour` exits unless `valuation == 'real_time'`
(`mrp_account/models/mrp_production.py:74`); `_cal_price` writes a price only for
`fifo`/`average` (`:61-64`). Measured: `iSMEs` real-time with 18 FIFO + 8 average;
`iTEST02` periodic, standard, **no valuation layers**. The two databases are complementary
failures — `53` §0.

**This is a configuration finding, not only a code finding**, and it is the more useful of
the two for SMEsPlus: a costing model whose activation depends on a rate field being filled
in on every work centre will be **partially activated in practice**, producing costed and
uncosted output from the same plant.

## 3. Why the apparatus was never activated — the question §8 of the directive asks

Evidence supports three statements and refuses a fourth:

1. **`iSMEs` could not activate it** — the work-order module is not installed, so no work
   order, time log or employee cost can exist. `FACT VERIFIED`.
2. **`iTEST02` activated the structure but not the rates** — 60 work centres, 154
   operations, 204 work orders, and **one** rate. `FACT VERIFIED`.
3. **No deployment ever configured an expense account on a work centre** — 60 of 60 null.
   `FACT VERIFIED`.
4. **Why** the operators did not fill the rates — **UNRESOLVED**. It could be deliberate
   (material-only costing policy), incomplete implementation, or a migration that never
   finished. **P03 has no evidence and makes no inference.** `UNR-P03-13`.

Statement 4 is exactly where a plausible story would be easy and unfounded. It is left
open.
