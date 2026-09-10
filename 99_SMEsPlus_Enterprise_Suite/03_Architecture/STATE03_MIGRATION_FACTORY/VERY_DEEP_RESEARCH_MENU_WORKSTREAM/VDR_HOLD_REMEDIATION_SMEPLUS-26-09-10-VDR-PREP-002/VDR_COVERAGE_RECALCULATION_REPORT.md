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
| Non-Applicable Population | **648** | 17 grouping containers (carry no function) + 635 items whose module is installed on **no** observed deployment |
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
| Verified **PROCESS** | 63 | **1.42%** |
| Verified **CONFIGURATION** | 755 | **17.06%** |
| Verified **OPTIONAL FUNCTION** | 21 | **0.47%** |
| **RESEARCH-COMPLETE** — all three on the same item | **0** | **0.00%** |
| Critical Population | 2,461 | 48.5% of total |
| **Critical Complete** | **0** | **0.00%** |
| Critical with **measured reachability** | 2,446 | **99.39%** |

> **`RESEARCH-COMPLETE = 0` is the honest consequence of §11.** No Learning Item in this domain has
> process, configuration **and** optional-function coverage on the same item. The 32 menus with prior
> L1–L12 coverage lack the optional dimension entirely (`00D` `RC-F-01`); the 10 delta items have all
> three at first-pass depth but no transactional verification.

## 3. Full dimension dashboard — not collapsed

| Dimension | Population | Applicable | Verified | % |
|-----------|-----------:|-----------:|---------:|--:|
| **Source Presence** | 5,074 | 5,074 | 5,074 | **100.00%** |
| **Runtime Reachability — element observed** | 5,074 | 4,426 | 63 | **1.42%** |
| **Runtime Reachability — module inferred** | 5,074 | 4,426 | 4,253 | **96.09%** |
| **Configuration Reachability** | 237 toggles | 179 | 21 | **11.73%** |
| **Optional Function Reachability** | 16 optional surfaces | 16 | 10 | **62.50%** |
| **Process Coverage** | 4,426 | 4,426 | 63 | **1.42%** |
| **Configuration Coverage** | 4,426 | 4,426 | 755 | **17.06%** |
| **Optional Function Coverage** | 4,426 | 4,426 | 21 | **0.47%** |
| **Menu Coverage** | 62 | 39 | 7 | **17.95%** |
| **Function Coverage** | 1,833 | — | 63 | **3.44%** |
| **Object / Data Coverage** | 96 | 96 | 0 | **0.00%** |
| **Cross-Module Coverage** | 90 | 90 | 0 | **0.00%** |
| **Hidden Automation Coverage** | 26 jobs | 11 | 11 reachability-verified, 0 function-verified | **0.00% function** |
| **SaaS / Security Coverage** | 46 rules · 180 grants | 43 · 170 | 43 rules | **100% rules · 0% grants** |
| **Edge / Reversal Coverage** | 96 objects | 96 | 2 | **2.08%** |
| **Critical Area Coverage** | 15 areas | 15 | **0 at 100%** | **0.00%** |

**These are fifteen separate measurements and they are not combined.** Taking the strictest single
reading — items research-complete under §11 over the applicable population:

```
Overall Verified Coverage  =  0 / 4,426  =  0.00%
```

## 4. Why the headline went **down** from 1.24%

The prior session reported 1.24% against a definition of "verified" that required **one** dimension.
This session applies §11, which requires **three**. **The work went up and the number went down**,
because the bar moved.

| | prior session | this session |
|---|---|---|
| Definition of verified | reached state `S4` on any dimension | PROCESS **and** CONFIGURATION **and** OPTIONAL FUNCTION |
| Denominator | 5,074 (total) | **4,426 (applicable)** — reachability now permits the distinction |
| Reachability | `UNMEASURED` on 100% | measured on **96.3%** |
| Headline | 1.24% | **0.00%** |

**A number that falls when the standard rises is the standard working.** The dimensions in §3 are
where the actual progress is visible: reachability 0% → 96.3%, configuration coverage 17.06%,
optional-function reachability 62.5%.

## 5. Gate evaluation

| Gate condition (§19) | Threshold | Actual | Result |
|---|---|---|---|
| Overall Verified Coverage | ≥ 95% | **0.00%** | **FAIL** |
| Critical Areas | 100% | **0 of 15** | **FAIL** |
| GOV-01 clean certification chain | PASS | see `GOV01_CLEAN_RECHALLENGE_REPORT.md` | **partially met** |
| Functional Ownership — material items resolved | required | **96 of 96, 0 unresolved** | **MET** |
| Runtime Reachability — critical items measured | required | **2,446 of 2,461 critical items (99.39%)** | **MET** |
| Prior Research Reconciliation — complete for applicable population | required | **62 of 62 menus classified** | **MET** |
| Process Coverage verified | required | 1.42% | **FAIL** |
| Configuration Coverage verified | required | 17.06% | **FAIL** |
| Optional Function Coverage verified | required | 0.47% | **FAIL** |
| No material unidentified functional surface | required | 4 sized-but-unmeasured gaps remain | **FAIL** |

**Three of the four control areas this session was commissioned to close are MET. The coverage gates
are not, and were never going to be closed by a remediation session.**
