# 65 — P03 / P09 ZEROING ROOT-CAUSE RECONCILIATION

**LAYER 2 — AUDIT QUARANTINE.**
**P09 LAST CONSUMED SHA: `70f8d20`** (was `37f0d86` — material delta consumed).

---

## 1. What P09's delta added

`70f8d20` — *"P09 analytic economic integrity — challenge closure"*. Read from the branch,
not from a summary. Material content for P03:

- `AI08` separates **eight** distinct quantities for one event and shows **six different
  numbers** describe one depreciation. Only one is the economic cost, and it is not the one
  a cost-centre report presents.
- The mechanism *"annotates rows; cost attribution is an emergent property of which rows
  happen to get annotated."*
- `AI08` §3 lists **"manufacturing work-in-progress ledger entry — no record, gross 0, net
  0, economic cost X, attribution absent entirely."**
- `AI10` hands P03 four items, `H03-1` … `H03-4`.
- `TH-F-01`: on a Thai chart, both accumulated-depreciation accounts are typed as expense on
  asset-range codes, so budget consumption nets to zero too.

## 2. Are P03's and P09's zeroing the same defect?

> **No. Same net, different mechanism. Neither subsumes the other.**

| | **P09 zeroing** | **P03 zeroing** |
|---|---|---|
| Records created | **2** | **0** |
| Gross movement | 2X | **0** |
| Net | 0 | 0 |
| Cause | both journal legs carry the allocation; signed amounts cancel | the conversion-cost transaction **never occurs** |
| Ledger | analytic / management | inventory valuation and GL |
| Detectable | **yes**, at line level — the attribution exists | **no** — there is nothing to detect |
| Fix shape | change eligibility or sign semantics | **create the cost event at all** |
| Owner | **P09** | **P03** |

**A reader who merges them would conclude that fixing analytic eligibility restores
manufacturing cost. It would not.** `iSMEs` has 27 analytic accounts, **0** work-centre
distributions and **0** work centres: no analytic fix produces a conversion cost that was
never computed.

## 3. P03's answers to P09's four handoffs

| P09 item | P03 answer |
|---|---|
| **`H03-1`** the masking interaction — a work-centre rate may silently carry depreciation while the depreciation attribution shows zero | **CANNOT FIRE in any examined deployment.** `iSMEs`: 0 work centres. `iTEST02`: **0 of 60 carry an analytic distribution**, and only 1 of 60 carries a rate. The masking requires both. **Mechanism plausible, incidence zero.** `FACT VERIFIED` for the incidence; the policy question (*are SMEsPlus rates intended to recover depreciation?*) is `R-03` and stays **`DESIGN CANDIDATE`** |
| **`H03-2`** one duration change produces two management records at two rates | **Confirmed as mechanism** (`DC-05`, `DC-14`); **incidence zero** — no distributions exist anywhere |
| **`H03-3`** the work centre is an allocation carrier whose scope is undetermined | **Answered in part.** Scope determined in `36`/`64`: resource `TENANT`, rate `COMPANY`. Incidence: **0 of 60 company-less**. Carrier role confirmed — the column exists and is empty everywhere. `SCOPE-02` stays open for P11 |
| **`H03-4`** WIP has two unreconciled representations, one spawning no management record | **Confirmed** — `03` §3: production-cost account (category) vs production-WIP account (company), three resolvers, never reconciled. `mrp_accountant` is **absent in `iSMEs`** and installed in `iTEST02`, so the second representation cannot even be produced in the database that manufactures |

## 4. What P03 hands back to P09

| # | Finding | Class |
|---|---|---|
| `P03→P09-1` | `AI08` §3's manufacturing WIP row is **confirmed from the deployed data**: no management record, and in `iSMEs` no WIP representation at all | `FACT VERIFIED` |
| `P03→P09-2` | The masking interaction of `H03-1` **cannot fire** in any of four deployments: rates and distributions are never both present | `FACT VERIFIED` (incidence) |
| `P03→P09-3` | P09's *"annotates rows, attribution is emergent"* framing **generalises to inventory valuation**: `_cal_price` computes a value from whatever layers it is handed, with no test of plausibility. `55` shows the consequence at 10²¹ | **SUPPORTED INTERPRETATION** — offered, not asserted on P09's behalf |

## 5. Boundaries respected

P03 **does not** redefine management-accounting architecture, adjudicate `TH-F-01`
(statutory, P07/P09), or take a position on `HOLD-AS-01` / `DIS-09`. P09's determinations
are cited, not overridden.
