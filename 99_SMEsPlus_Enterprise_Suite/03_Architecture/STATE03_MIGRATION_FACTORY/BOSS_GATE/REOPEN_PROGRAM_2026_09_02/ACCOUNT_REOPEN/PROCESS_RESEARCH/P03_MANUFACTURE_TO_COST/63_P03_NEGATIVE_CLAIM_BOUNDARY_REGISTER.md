# 63 — NEGATIVE-CLAIM BOUNDARY REGISTER

**LAYER 2 — AUDIT QUARANTINE.**

Permitted: *"NO PATH VERIFIED IN THE EXAMINED DEPLOYMENTS."*
Forbidden: *"NO PATH EXISTS."*

Every negative claim P03 makes, with its evidence population.

---

## 1. Register

| Claim | Population | Version / schema | Modules | Databases | Companies | Config | Unknowns |
|---|---|---|---|---|---|---|---|
| No fixed-overhead path into inventory | 797-module source root | v18 Ent. b20250608 | 4 lists: 251/190/453 | 4 | 1, 1, 44, 44 | all work-centre configs read | systems not in these 4 |
| No depreciation reference in manufacturing modules | same | same | same | — | — | — | other versions |
| Analytic route cannot carry depreciation | source | version-independent by construction | n/a | n/a | n/a | n/a | **none — structural** |
| No rework object | 797 modules, `tests/` excluded | v18 | — | — | — | — | other versions |
| No normal/abnormal scrap distinction | same | v18 | — | — | — | — | other versions |
| No custom addon overrides manufacturing cost | 3 roots, 1,325 `.py` | v18 line | — | — | — | — | roots not in the 3 |
| No tenant concept in manufacturing source | 4 modules | v18 | — | — | — | — | other versions |
| No mutual exclusion between duplication mechanisms | source + 4 databases | v18 | complete | 4 | — | 60 work centres read | — |
| **No company-less work centre** | **60 rows, `iTEST02`** | that schema | 453 | **1 of 4** | 1 | all 60 read | the other 3 have **no work centres at all** |
| No employee cost configured | 60 work centres + 27 time logs | `iTEST02` | 453 | 1 | 1 | all read | — |
| No `extra_cost` used | **10,927 MO rows** across both | both | — | 2 | — | — | — |
| No payroll↔absorption bridge | module set + `hr_payroll_account` | v18 | — | — | — | — | **PATTERN NOT MECHANICAL** — `C-06`, weakest claim in the package |

## 2. Claims **withdrawn** this round because their population grew

| Withdrawn claim | Why |
|---|---|
| *"`project_mrp_account` is not installed in any readable dump"* | It **is** installed in `iTEST02` |
| *"`project_mrp_workorder_account` is not installed"* | It **is** installed in `iTEST02` |
| *"the conversion-cost apparatus has never been switched on"* | 60 work centres, 154 routing operations, 204 work orders in `iTEST02` |
| *"containerised tooling is not available"* | Docker and Colima were **already running** — `62` §6 |

**Four negative claims withdrawn in one round.** All four were correctly bounded when
written; three were bounded to "three readable dumps" and one to an unchecked assumption
about this session's own capabilities. **Only the fourth was a discipline failure** — the
first three are the bound working exactly as intended.

## 3. The distinction that matters

| Kind | Example | Verdict |
|---|---|---|
| Correctly bounded, later overturned by a larger population | `DC-14` unreachable *"in the three readable dumps"* | **Not an error.** The claim was true of its stated population and was never stated more widely |
| Bounded to an **unchecked assumption** | *"containerised tooling not available"* | **An error** — the population was assumed, not enumerated |

`smeplus-deep-research-negative-claim-standard` covers the first; `smeplus-evidence-base-is-itself-a-claim` covers the second. **This round produced one of each**, which is the clearest available demonstration that they are different failures.

## 4. Standing form

Every P03 negative reads: *"NO EVIDENCE FOUND within POPULATION / PATTERN / PATH SET /
UNIT."* No P03 artefact contains an unbounded *"does not exist"*, and `23` §3 records the
scan that verifies it.
