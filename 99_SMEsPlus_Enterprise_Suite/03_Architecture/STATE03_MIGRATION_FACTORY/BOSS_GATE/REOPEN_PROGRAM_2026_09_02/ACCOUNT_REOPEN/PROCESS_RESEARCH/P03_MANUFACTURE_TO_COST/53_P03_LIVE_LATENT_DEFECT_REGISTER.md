# 53 — LIVE / LATENT DEFECT REGISTER

**LAYER 2 — AUDIT QUARANTINE.**

Authoritative population retrieved from `05` and `25`: **15 `DC-*` defects**. The count is
enumerated (`grep -oE '\`DC-[0-9]+\`' | sort -u | wc -l` = 15), not carried forward.

Five axes per the directive, then exactly one exposure class.

---

## 0. A correction to this file's own first draft — read this first

The first draft of this register classified **five** defects as live, on the strength of
`iTEST02`'s 60 work centres and its 60-of-60 missing expense accounts. **That was wrong**,
and it was caught by expert `E4`'s challenge in `69` §8, which asked why `DC-04`'s cost
method had never been measured.

Measuring it exposed **two gates the draft had skipped**:

| Gate | Source | `iSMEs` | `iTEST02` |
|---|---|---|---|
| `_post_labour` requires `valuation == 'real_time'` | `mrp_account/models/mrp_production.py:74` | **real_time on 15 categories** | **no valuation layers exist at all** |
| `_cal_price` writes a price only for `fifo`/`average` | `:61-64` | **18 fifo, 8 average, 0 standard** | **3 explicit categories: `standard` + `periodic`** |

And a third fact the draft had not established:

> **`iTEST02` is a test system, not a production deployment.** It holds **32 general-ledger
> lines**, **no `stock_valuation_layer` table**, and 163 manufacturing orders of which 102
> are cancelled. `iSMEs` holds 447,384 GL lines and 74,982 valuation rows.

**Nothing material posts in `iTEST02`.** Configuration existing there proves the apparatus
*can be configured*; it does not make a defect live.

> **`P03R-F-09`. The two preconditions for conversion cost to reach inventory — work
> centres with rates, and real-time valuation — have never co-existed in any examined
> deployment.** `iSMEs` has real-time valuation and **zero** work centres. `iTEST02` has 60
> work centres and **no valuation at all**. `FACT VERIFIED`.

**Round 3's "only `DC-13` is live" was correct. This round's draft "5 live" was not.**
Round 3 reached the right answer by an incomplete route (it had not seen `iTEST02`); this
draft reached a wrong answer by measuring configuration and skipping the gates. Recorded as
`RE-P03-19`.

## 1. The register


| ID | Source defect | Deployed config reachable | Observed execution | Financial effect | Management effect | **Exposure class** |
|---|---|---|---|---|---|---|
| `DC-01` machine cost on raw sum of overlapping logs | **VERIFIED** | **YES — `T`**: 7 of 13 work orders have >1 log | **1 overlap observed, zero-duration** | **0 measured** | none | **LATENT — CODE PRESENT, CONFIGURATION REACHED, EFFECT ZERO** |
| `DC-02` machine + employee rates on one interval | VERIFIED | **NO** — 0 of 60 employee rates, 0 of 27 employee costs | none | 0 | none | **UNREACHABLE IN VERIFIED DEPLOYMENT** |
| `DC-03` `extra_cost` never relieved | VERIFIED | **NO** — 0 non-zero of 10,927 orders | none | 0 | none | **LATENT — MODULE PRESENT, REQUIRED DATA ABSENT** |
| `DC-04` standard-cost relief mismatch | VERIFIED | **NO — measured** | none | 0 | none | **UNREACHABLE IN VERIFIED DEPLOYMENT.** `iSMEs`: 18 fifo + 8 average, **0 standard**. `iTEST02`: standard but **periodic**, so the relief never posts |
| `DC-05` analytic ≠ GL | VERIFIED | **NO** — 0 of 60 work centres carry a distribution | none | 0 | 0 | **LATENT — MODULE PRESENT, REQUIRED DATA ABSENT** |
| `DC-06` posted rate ignores the work-order snapshot | VERIFIED | rate configured on 1 of 60 in `T` | **no posting — `T` has no valuation** | 0 | none | **LATENT — CONFIGURATION REACHED, POSTING GATE NOT** |
| **`DC-07` relief credits product COGS** | VERIFIED | **60 of 60 work centres have NO expense account — the worst possible configuration** | **none — `_post_labour` requires real-time valuation, which `T` does not have** | **0** | none | **LATENT — CONFIGURATION FULLY REACHED, POSTING GATE NOT.** The single most exposed defect the moment valuation is switched to automated |
| `DC-08` expected cost injected as actual | VERIFIED | **YES — `T`**: 204 work orders exist | not isolated | unknown | none | **LATENT — REACHABLE** |
| `DC-09` relief dated today, not at the event | VERIFIED | only where `DC-07` fires | none | 0 | none | **LATENT — REACHABLE**, inherits `DC-07`'s gate |
| `DC-10` employee analytic inert | VERIFIED | **`project_mrp_workorder_account` IS INSTALLED in `T`** | none — no distributions | 0 | 0 | **LATENT — MODULE PRESENT, REQUIRED DATA ABSENT** — round 3's "confirmed inert" is **falsified** |
| `DC-11` company-dependent accounts resolved in the user's company | VERIFIED | **NO** — both manufacturing databases are single-company | none | 0 | none | **UNREACHABLE IN VERIFIED DEPLOYMENT** (but see §3) |
| `DC-12` rate applied twice in the cost report | VERIFIED | reporting only | n/a | 0 | report | **LATENT — REACHABLE** |
| **`DC-13` unbuild releases the first layer's cost** | VERIFIED | **YES — `S`: 987 unbuild orders** | **YES — 12 of the 30 corrupt valuation rows are unbuild** | **catastrophic — `55`** | none | **LIVE — OBSERVED** |
| `DC-14` project analytic double distribution | VERIFIED | **`project_mrp_account` IS INSTALLED in `T`** | none — no distributions | **0 financial by construction** | doubling possible | **LATENT — REACHABLE** — round 3's "not installed anywhere" is **falsified** |
| `DC-15` no idempotence marker | VERIFIED (absence) | the guard is absent in code unconditionally | **the relief entry never posts in any examined deployment** | 0 | none | **LATENT — REACHABLE.** The absence is unconditional; its consequence needs the entry to post |

## 2. Counts — enumerated row by row, after the §0 correction

| Class | Count | IDs |
|---|---|---|
| **LIVE — OBSERVED** | **1** | `DC-13` |
| **LIVE — CONFIGURED AND REACHABLE** | **0** | — |
| **LATENT — configuration fully reached, posting gate not** | **2** | `DC-06`, `DC-07` |
| **LATENT — code present, configuration reached, effect zero** | **1** | `DC-01` |
| **LATENT — module present, required data absent** | **3** | `DC-03`, `DC-05`, `DC-10` |
| **LATENT — reachable** | **5** | `DC-08`, `DC-09`, `DC-12`, `DC-14`, `DC-15` |
| **UNREACHABLE in verified deployment** | **3** | `DC-02`, `DC-04`, `DC-11` |
| **UNKNOWN** | **0** | — |

**Reconciliation: 1 + 0 + 2 + 1 + 3 + 5 + 3 + 0 = 15.** Every `DC-*` id appears exactly once.

**LIVE total: 1. LATENT total: 11. UNREACHABLE: 3.**

## 3. `DC-11` — unreachable, with a stated caveat

Both manufacturing databases are single-company. `BK12MAY26` has **44 companies** but zero
manufacturing. **The two conditions for `DC-11` have never coexisted in a readable
deployment** — that is not the same as the defect being safe, and it is recorded as
*unreachable in the verified deployment*, never as *cannot occur*.

## 4. Movement from round 3 — the honest version

| Movement | Count | IDs |
|---|---|---|
| Round-3 **reachability** claim falsified | 2 | `DC-10`, `DC-14` — the modules **are** installed in `iTEST02`; both remain latent |
| Round-3 `UNKNOWN` **resolved** | 1 | `DC-04` → **UNREACHABLE**, measured |
| **Narrowed** to unreachable | 1 | `DC-02` |
| **Confirmed live** | 1 | `DC-13` — and now with observed catastrophic effect (`55`) |
| Round-3 live count | **1** | **unchanged and correct** |

> **Round 3's headline — "only `DC-13` is live" — survives this round intact.** What changed
> is the *reason*: not "no deployment has work centres" (false), but "no deployment has work
> centres **and** real-time valuation together" (`P03R-F-09`). The conclusion was right; its
> stated ground was wrong, and a right conclusion resting on a wrong ground is worth
> correcting because the ground is what a design decision would be built on.
