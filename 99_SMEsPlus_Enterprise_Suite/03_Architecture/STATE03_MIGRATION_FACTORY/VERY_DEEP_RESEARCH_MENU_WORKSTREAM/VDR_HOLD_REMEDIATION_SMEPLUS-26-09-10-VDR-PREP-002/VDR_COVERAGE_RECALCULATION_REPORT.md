# VDR_COVERAGE_RECALCULATION_REPORT.md
# Coverage recalculated from the reconciled population

Session `[SMEPLUS-26-09-10-VDR-PREP-002]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Rule applied: `VDR_COVERAGE_RULE.md` v1.0 plus the three-dimension rule of this prompt's §11.

---

## 1. The denominator changed, so every prior percentage is superseded

**No stale denominator is reused.** The population now carries a measured reachability class on every
row, so an **applicable** population can be computed for the first time.

| Population (§18) | Count | Note |
|---|---:|---|
| **Total Source Population** | **5,074** | rows; 4,699 distinct identities |
| Non-Applicable Population | **648** | 635 items whose module is installed on **no** observed deployment, **∪** 17 grouping containers — **4 items are in both sets**. The first version presented these as a sum, which gives 652 |
| **APPLICABLE Population** | **4,426** | 87.2% of total |
| Source-Present Population | 5,074 | **100%** — every row carries a reproducible pointer with root and generation |
| Runtime-Reachable — **element observed** | **63** | the element itself was found in a deployment's records |
| Runtime-Reachable — **module inferred** | 4,190 | necessary condition only, not observation |
| Reachability **unmeasured** | 186 | 3.7% |
| Configuration-Reachable Population | 21 of 237 | group-toggles resolved to an effect surface |
| Optional-Function Population | 62 | group-toggles + module-installer toggles |

## 2. Verified populations — the three mandatory dimensions

| Verified population | Count | Of applicable |
|---|---:|---:|
| Verified **PROCESS** | **59** | **1.33%** — corrected: 4 of the 63 are non-applicable rows |
| Verified **CONFIGURATION** | **677** | **15.30%** — corrected: 78 of the 755 are non-applicable rows |
| Verified **OPTIONAL FUNCTION** | 21 | **0.47%** |
| **RESEARCH-COMPLETE** — all three on the same item | **NOT DETERMINABLE** | the register carries **one ordinal status per row** and cannot represent three dimensions; the previous `0` was a property of the schema — `CORR-F-38` |
| Critical Population | 2,461 | 48.5% of total |
| **Critical Complete** | **NOT DETERMINABLE** | as above |
| Critical with **measured reachability** | 2,446 | **99.39%** |

> **`RESEARCH-COMPLETE = 0` is WITHDRAWN on two independent grounds.**
> Its premise was false — the prior corpus **does** cover the optional dimension, under the name
> *capability switch* (`00D` `RC-F-01`, retracted). And it was **unfalsifiable by construction**: this
> register carries **one ordinal status per row**, so no row could ever record three dimensions. The
> zero was a property of the data model, not an observation about the domain.
>
> **What can honestly be said:** the 29 menus with prior coverage have process, configuration and
> optional-function coverage and lack **runtime**; the 10 delta items have all three at first-pass
> depth and lack **transactional verification**. Neither set can be scored against §11 until the
> register carries three independent dimension columns (`CORR-F-38`).

## 3. Full dimension dashboard — not collapsed

| Dimension | Population | Applicable | Verified | % |
|-----------|-----------:|-----------:|---------:|--:|
| **Source Presence** | 5,074 | 5,074 | 5,074 | **100.00%** |
| **Runtime Reachability — element observed** | 5,074 | 4,426 | 63 | **1.42% of applicable** (73 of 5,074 = 1.44% of total; the two bases differ and both are stated) |
| **Runtime Reachability — module inferred** | 5,074 | 4,426 | 4,253 | **96.09%** |
| **Configuration Reachability** | 237 toggles | 179 | 21 | **11.73%** |
| **Optional Function Reachability** | 16 optional surfaces | 16 | 10 | **62.50%** |
| **Process Coverage** | 4,426 | 4,426 | **59** | **1.33%** |
| **Configuration Coverage** | 4,426 | 4,426 | **677** | **15.30%** |
| **Optional Function Coverage** | 4,426 | 4,426 | 21 | **0.47%** |
| **Menu Coverage** | 62 | 39 | 7 | **17.95%** |
| **Function Coverage** | 1,833 | — | 63 | **3.44%** |
| **Object / Data Coverage** | 96 | 96 | 0 | **0.00%** |
| **Cross-Module Coverage** | 90 | 90 | 0 | **0.00%** |
| **Hidden Automation Coverage** | 26 jobs | 11 | 11 reachability-verified, 0 function-verified | **0.00% function** |
| **SaaS / Security Coverage** | 46 rules · 180 grants | 43 · 170 | 43 rules | **100% rules · 0% grants** |
| **Edge / Reversal Coverage** | 96 objects | 96 | 2 | **2.08%** |
| **Critical Area Coverage** | 15 areas | 15 | **0 at 100%** | **0.00%** |

**These are fifteen separate measurements and they are not combined.**

**No single "overall verified coverage" figure is published this round.** The §11 three-dimension
reading is not computable from the current register (`CORR-F-38`), and the one-dimension reading that
the prior session used is not comparable to it. Publishing either as *the* headline would be the
collapse this framework forbids.

The two readings that **are** computable, each with its denominator:

```
process-verified over applicable        =   59 / 4,426  =  1.33%
configuration-verified over applicable  =  677 / 4,426  = 15.30%
```

## 4. Why there is no single headline this round

The prior session published **1.24%** against a one-dimension definition of *verified*. This session
set out to publish a three-dimension figure under §11 and **cannot**, for a reason worth stating
plainly: **the register cannot represent a three-dimension item**, so any figure it produced would be
zero by construction.

| | prior session | this session |
|---|---|---|
| Definition of verified | `S4` on any one dimension | PROCESS **and** CONFIGURATION **and** OPTIONAL FUNCTION |
| Denominator | 5,074 (total) | **4,426 (applicable)** — reachability now permits the distinction |
| Reachability | `UNMEASURED` on 100% | measured on **96.3%**, and re-challenge produced a **counter-example** to the inference behind 94.9% of it |
| Headline | 1.24% | **withheld** — not computable, `CORR-F-38` |

**Where the actual progress is:** reachability 0% → 96.3% (with its inference now bounded);
five deployments across three generations examined; ownership resolved for 96 of 96 objects; and a
`CRITICAL` finding retracted because the evidence did not support it.

**A round that withdraws its own headline, retracts a `CRITICAL` finding and publishes no replacement
number is not a failed round.** It is the difference between a measurement and a number.

## 5. Gate evaluation

| Gate condition (§19) | Threshold | Actual | Result |
|---|---|---|---|
| Overall Verified Coverage | ≥ 95% | **not computable this round** — see §3 | **FAIL — the gate cannot be met and cannot currently be measured** |
| Critical Areas | 100% | **0 of 15** | **FAIL** |
| GOV-01 clean certification chain | PASS | see `GOV01_CLEAN_RECHALLENGE_REPORT.md` | **partially met** |
| Functional Ownership — material items resolved | required | **96 of 96, 0 unresolved** | **MET** |
| Runtime Reachability — critical items measured | required | **2,446 of 2,461 critical items (99.39%)** | **MET** |
| Prior Research Reconciliation — complete for applicable population | required | **62 of 62 menus classified** | **MET** |
| Process Coverage verified | required | **1.33%** | **FAIL** |
| Configuration Coverage verified | required | **15.30%** | **FAIL** |
| Optional Function Coverage verified | required | **not separately measurable** — this session's measurement of it was withdrawn (`RC-F-01`) | **FAIL** |
| No material unidentified functional surface | required | 4 sized-but-unmeasured gaps remain | **FAIL** |

**Three of the four control areas this session was commissioned to close are MET. The coverage gates
are not, and were never going to be closed by a remediation session.**
