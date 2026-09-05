# 50 — P03 CURRENT STATE: RUNTIME INVERSION

**LAYER 2 — AUDIT QUARANTINE.**
Supplemental continuation `SMEPLUS-26-09-05-…-RUNTIME-INVERSION-RISK-RECLASSIFICATION-001`.
**NO RESET.** Files `00`–`47` stand. Baseline `506cf65` verified as HEAD and as remote.

---

## 1. The material delta of this round, in one sentence

> **A fourth database was opened, and it falsifies the central negative claim of round 3.**

Round 3 concluded that the conversion-cost apparatus "has never been switched on", bounded
to *three readable deployments*. The fourth deployment — `iTEST02`, previously unreadable —
has **60 work centres, 154 routing operations, 204 work orders, 27 time logs**, and **every
manufacturing module installed**, including the two that round 3 recorded as *not installed
in any readable dump*.

**The bound was correct. The conclusion inside the bound was correct. The conclusion did
not survive the bound being lifted.** That is the whole lesson of this round and it is
stated first rather than buried.

## 2. Two deployments, two opposite failures

| | `iSMEs` | `iTEST02` |
|---|---|---|
| Manufacturing orders | **10,764** (9,807 done) | 163 (8 done) |
| Work centres | **0** | **60** |
| Routing operations | **0** | 154 |
| Work orders | **0** | 204 |
| Time logs | **0** | 27 |
| Modules installed | 190, **missing** work-order, HR-account, project, accountant, subcontracting | **453, all present** |
| Conversion cost | **structurally zero** | **configured and posting** |
| Dominant failure | **ZEROING** | **misdirection + latent duplication** |
| Valuation ledger | **30 corrupt rows, ±1e21** | no valuation table |

**Neither database alone tells the truth about the reference product.** Round 3 saw only
the first and generalised. This round sees both and generalises to neither.

## 3. The finding round 3 did not reach at all

Round 3 measured `stock_valuation_layer` row counts and inferred that material cost reaches
finished goods. This round **measured the values**, and found something else:

> **`P03R-F-01`. Thirty valuation rows in `iSMEs` carry values up to ±1.5 × 10²¹, and the
> general ledger does not contain them.** All 25 that claim a journal entry point at
> entries that exist and carry **completely different, sane amounts** — 25 mismatched, 0
> matched. The subsidiary valuation ledger and the general ledger have **diverged**.

Net effect on the valuation ledger: **−194,847,920.10 against a clean base of
400,338,755.98 — a −48.7 % distortion of total inventory valuation.**

The corruption originates in **vendor goods receipts and their bill revaluations**, not in
manufacturing (`55` §3). Manufacturing **inherited and amplified** it: 18 of the 30 corrupt
rows are manufacturing-origin.

## 4. Reclassification summary

Full register in `53`. Headline movements from round 3:

| Defect | Round 3 | Round 4 | Why |
|---|---|---|---|
| `DC-07` relief credits COGS | LATENT | **LATENT — configuration fully reached, posting gate not** | **60 of 60** work centres have no expense account — the worst possible configuration — but `iTEST02` has **no real-time valuation**, so the relief never posts. See `53` §0 |
| `DC-13` unbuild first-layer cost | LIVE | **LIVE — OBSERVED, and implicated in `P03R-F-01`** | 12 of 30 corrupt rows are unbuild |
| `DC-14` project analytic | "module not installed anywhere" | **LATENT — REACHABLE** | `project_mrp_account` **is** installed in `iTEST02` |
| `DC-10` employee analytic inert | "CONFIRMED INERT" | **NOT INERT** | `project_mrp_workorder_account` **is** installed in `iTEST02` |
| `DC-01` overlapping logs | LATENT, no work orders | **LATENT — REACHABLE, effect measured at zero** | 7 of 13 work orders have multiple logs; 1 genuinely overlaps; that log has **zero duration** |
| `DC-02` two rates on one interval | LATENT | **UNREACHABLE in both** | 0 of 60 employee rates; 0 of 27 non-zero employee costs |
| `DC-03` `extra_cost` residue | LATENT | **UNREACHABLE in both** | 0 non-zero across 10,764 + 163 rows |

**Two round-3 *reachability* claims are falsified** (`DC-14`, `DC-10` — the modules are
installed). **One `UNKNOWN` is resolved to unreachable** (`DC-04`). **Round 3's live count
of 1 is unchanged and correct** — see `53` §0, where this round's own draft claim of "5
live" is corrected.

## 4b. The correction this round made to itself

This round's first draft classified five defects as live. **Measuring the two posting gates
disproved it.** `_post_labour` requires real-time valuation; `_cal_price` writes a price only
for FIFO/average. `iTEST02` — the database with 60 work centres — has **no valuation layer
table, 32 general-ledger lines, and periodic valuation**. It is a **test system**, and
nothing material posts there.

> **`P03R-F-09`. Work centres with rates and real-time valuation have never co-existed in
> any examined deployment.** `iSMEs` has the valuation and no work centres; `iTEST02` has
> the work centres and no valuation.

Round 3's *"only `DC-13` is live"* is therefore **correct**, and this round's draft was not.
`RE-P03-19`.

## 5. What is *not* withdrawn

Every source defect remains `FACT VERIFIED` **as code**. Reachability is a separate axis and
is now measured on four databases instead of asserted on three. Nothing in this round makes
a defect harmless; `DC-01` in particular has its precondition present and its effect at zero
only because one log happened to have zero duration.

## 6. Closures

| Item | Status |
|---|---|
| **`DEP-04`** installed-module list | **FULLY CLOSED — 4 of 4 databases** |
| **`UNR-P03-07`** `iTEST02` unreadable | **CLOSED** — opened with an already-running runtime and an already-cached image; no environment change (`62`) |
| **`DEP-13` / `P04-B-35`** incidence | **EXECUTED WITH A REAL POPULATION: 0 of 60** company-less work centres |
