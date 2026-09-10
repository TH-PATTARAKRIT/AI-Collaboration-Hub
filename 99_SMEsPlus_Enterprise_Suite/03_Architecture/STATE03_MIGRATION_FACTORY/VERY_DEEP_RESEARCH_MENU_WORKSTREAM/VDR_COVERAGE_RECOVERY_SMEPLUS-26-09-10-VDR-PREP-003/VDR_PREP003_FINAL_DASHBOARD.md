# VDR_PREP003_FINAL_DASHBOARD.md
# §20 Final Dashboard — every metric reported separately, none collapsed

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Register **R2 / `POPULATION_V4`**, post-challenge. Every figure below is derived from the frozen
register by a published formula in `VDR_COVERAGE_MEASUREMENT_SPEC.md`. **No qualitative estimate.**

---

## 1. Frozen populations (Checkpoint 01)

| Population | Count |
|------------|------:|
| `TOTAL_DISCOVERED_POPULATION` | **5,074** |
| `APPLICABLE_POPULATION` | **5,074** |
| `NON_APPLICABLE_POPULATION` | **0** |
| `CRITICAL_POPULATION` | **737 distinct** items (912 area-memberships; 175 are second or later mappings) |
| `OPTIONAL_FUNCTION_POPULATION` | **970** |
| `CONFIGURATION_DEPENDENT_POPULATION` | **946** |
| `RUNTIME_TESTABLE_POPULATION` | **5,071** |
| Applicable dimension cells | **30,906** |

**Exclusions from the applicable population: none.** `VDR_EXCLUSION_REGISTER.md` is deliberately empty —
the 180 cells R1 removed have all been restored, and the register exists so that no cell can leave a
denominator again without an id, a reason, evidence, a reviewer and a status.

## 2. The dashboard

| Metric | Numerator / Denominator | **Result** |
|--------|------------------------|-----------:|
| Source Presence Coverage % | 5,074 / 5,074 | **100.00%** |
| Runtime Reachability Coverage % | 4,256 / 5,071 | **83.93%** |
| **Runtime Observed Coverage %** | 77 / 5,071 | **1.52%** |
| Configuration Reachability % | 4,109 / 4,109 | **100.00%** |
| Optional Function Reachability % | 4,097 / 4,097 | **100.00%** |
| Process Coverage % | 0 / 1,561 | **0.00%** |
| Configuration Coverage % | 7 / 4,109 | **0.17%** |
| Optional Function Coverage % | 7 / 4,097 | **0.17%** |
| Cross-Module Coverage % | 0 / 2,909 | **0.00%** |
| Object/Data Coverage % | 0 / 2,863 | **0.00%** |
| Security Coverage % | 0 / 4,055 | **0.00%** |
| Edge/Reversal Coverage % | 0 / 1,167 | **0.00%** |
| Function Complete Coverage % | 0 / 5,074 | **0.00%** |
| **OVERALL VERIFIED COVERAGE %** | **0 / 5,074** | **0.00%** |
| *Determined-Complete, reported alongside and never merged with it* | 4,942 / 5,074 | *97.40%* |
| **Critical Areas Complete** | | **0 / 15** |
| **Open Critical Gaps** | | **6** |
| **SMEs Core Result** | | **3 challengers, 56 findings, 36 adopted; headline reduced from 1 of 15 to 0 of 15** |
| **PMO Certification** | | **DENIED** |

## 3. The two 100% figures, qualified — because a 100% is where this package failed before

**Source Presence Coverage = 100.00% means every item carries a pointer. It does not mean every pointer
resolves.** Resolved against the reference root:

| | Count | Share |
|---|---:|---:|
| resolves to **file and line** | 2,729 | 53.8% |
| resolves to **file only** | 2,159 | 42.5% |
| resolves to **no file** — the value is prose, e.g. *"derived from the model-declaration census"* | **186** | **3.7%** |

This is why `SOURCE` scores 100% on *presence* and **0.00%** on the research-verified grade: R1 graded
that dimension with an unconditional literal that could not fail, and 186 of its "reproducible pointers"
point at nothing (`CH-03`).

**Configuration and Optional Function Reachability = 100.00% means a condition and an activation route
are recorded for every eligible item.** 26 of those configuration conditions are runtime-activation
statements on automation rows rather than configuration determinations (`CH-25`), and the
optional-function classifier had **no branch capable of emitting two of its six classes** — one of which
was not empty (`CH-05`). A 100% reachability figure and a 0.17% depth figure describe the same
population; only the second one is a claim about understanding.

## 4. Reading this dashboard honestly

Three numbers carry the meaning:

- **Runtime Observed 1.52%** — 77 items whose existence was confirmed on a real deployment, against 83.93% whose *module* is installed. The gap between those two figures is the gap between *inferred* and *seen*.
- **Overall Verified Coverage 0.00%** — no item in this domain meets the depth standard on every dimension applicable to it. The gate is ≥95%.
- **Determined-Complete 97.40%** — what *is* established: for almost every item, the condition on almost every dimension is known, including where the determination is "none".

**97.40% determined and 0.00% verified is the true state of this preparation.** The programme knows
*what is there*. It does not yet know *how it behaves*.
