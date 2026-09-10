# VDR_RUNTIME_REACHABILITY_COVERAGE_REPORT.md
# Runtime Reachability — coverage, and the strength of each measurement

Session `[SMEPLUS-26-09-10-VDR-PREP-002]` · Layer: **LAYER 1 — CLEAN-ROOM.**

---

## 1. The measurement is not uniform, and is not reported as if it were

`GAP-INV-09` recorded reachability as `UNMEASURED` on **all 5,074** Learning Items. It is now measured
for 96.3% — **but by three different instruments of very different strength**, and collapsing them
into one percentage would repeat the defect this framework exists to prevent.

| Strength | What was observed | Items | Share |
|----------|-------------------|------:|------:|
| **A — ELEMENT OBSERVED** | the element itself was found, or not found, in a deployment's own records | **73** | **1.4%** |
| **B — MODULE INFERRED** | the element's module is installed on an observed deployment; the element itself was not looked for | 4,815 | 94.9% |
| **C — UNMEASURED** | no deployment observation applies | 186 | 3.7% |

**Only class A is a measurement of the element.** Class B is a *necessary condition* — if the module
is absent the element cannot exist — and it is **not sufficient**: a module can be installed and an
element still not present. The Pilot's own data shows this necessary condition is, for menus, also
sufficient in practice (**0 anomalies in 124 menu observations across two deployments**), which is
evidence for the inference but not proof of it.

## 2. Class A — what was actually observed

| Element class | Population | Observed | Reachable | Not reachable |
|---------------|-----------:|---------:|----------:|--------------:|
| Menus in the Inventory application | 62 | **62** | 52 (46 on all three series-19 deployments, 6 on one) | 10 — optional-module dependent |
| Scheduled jobs in the domain module set | 26 | **26** | **11 — all active, all with a real last-run timestamp** | 15 — module not installed |
| | **88** | **88** | **63** | **25** |

**Every one of the 11 reachable scheduled jobs has executed.** That is the strongest reachability
statement in the package: not *could run* — *did run*. Confirmed independently, with timestamps
reproduced to the second.

## 3. Coverage by the prompt's dimensions

| Dimension | Result | Basis |
|-----------|--------|-------|
| **Source Presence Coverage** | **100%** — 5,074 of 5,074 | every item carries a reproducible source pointer with root and generation |
| **Runtime Reachability Coverage (element-observed)** | **1.4%** — 73 of 5,074 | class A only |
| **Runtime Reachability Coverage (module-inferred)** | **96.3%** — 4,888 of 5,074 | classes A + B |
| **Configuration Reachability Coverage** | **8.9%** — 21 of 237 toggles resolved to an effect surface; **0 of 237 observed as set or unset on a deployment** except one | only one configuration parameter was checked against deployment state |
| **Optional Function Reachability** | **62.5%** — of the 16 optional-module-dependent surfaces identified, 10 were resolved against deployment installation state | |
| **Transactional Reachability** | **small-N, not 0%** | one target-generation deployment carries **3,642 on-hand rows and 14,441 movements**. `GAP-INV-09B` as first published was **wrong** and is replaced by `GAP-INV-09C` |

## 4. What changed because reachability was measured

| Finding | Before | After |
|---------|--------|-------|
| `HA-F-01` — opening a menu mutates data | `UNMEASURED` | **LIVE — the suppressing parameter is absent on both deployments** |
| `HA-F-01` row 4 — the scheduler menu | `UNMEASURED` | **LIVE — active and executed on both deployments** |
| valuation-closing job (`BOSS-DEC-12`) | `UNMEASURED` | **LIVE — active and executed on both**, and excluded from the domain by the mechanical rule |
| localisation surfaces (10 menus, 5 objects) | in the population | **installed on no observed deployment — outside the applicable baseline** |
| `OD-F-05` / `CRITICAL-GAP-01` — valuation object replaced | source-only | **RE-STATED** — the ledger table is absent, but the per-movement value is present on the movement row. The stronger claim was **retracted** (`00C` `RR-F-05 / RR-F-06`) |

## 5. Declared limits

1. **All five database identities are now examined**, but the census was run **after** the first two
   were chosen, and for both a newer copy existed that was not used (`GAP-INV-17`). Two published
   claims were false because artefacts listed in this package's own census were not opened.
2. **Cloud-storage trees were not swept** — traversal stalls on placeholder files. Declared as an
   evidence-affecting exclusion.
3. **No application server was run.** No UI execution, no controlled test transaction, no security
   response, no state-transition test.
4. **Three deployments are transacted — series 16, 18 and 19.** The target-generation one runs
   **periodic** valuation, so the movement → accounting link is unobservable (`GAP-INV-21`).
5. **Class B is an inference, not an observation**, for 94.9% of items — and re-challenge produced a
   **counter-example** at field level, so 96.3% is an **upper bound** (`RR-F-09`).

**None of these is closable by reading the artefacts already read.** Items 1 and 2 are closable by more
sweeping; items 3–5 need a running instance in the target generation with real stock.
