# SC-18 — `F5` REMAINING DECISION READINESS

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Head consumed `ce987553`
**One card per open `F5` election. These are SMEs Core recommendations, NOT Boss rulings.**
Ruled already and not re-asked: **`POH-D-06`** — restate; normal capacity confirmed (`SC-BD-06`).

---

## `POH-D-01` — declared departure from `BD-04` (one driver per cost class)

| | |
|---|---|
| **Exact decision** | Confirm or refuse the declared departure from `BD-04`'s one-driver-per-cost-class rule |
| **SMEs Core recommendation** | **Confirm the departure**, scoped to the overhead cost classes that need it, with the departure **declared per class** rather than granted generally |
| **Alternatives** | hold `BD-04` strictly (forces a single driver where evidence shows more than one is needed) · grant a general exemption (removes the rule) |
| **Consequence** | Absorption can model classes that genuinely have distinct drivers; a per-class declaration keeps `BD-04` intact as the default |
| **Thai statutory dependency** | **None** |
| **Rulable now?** | **YES** |
| **Blocks** | later implementation only — not Phase SA closure, not Pre-Test entry |
| **Evidence** | `SC-06` `F5` card · `SA_CORR3_03` `POH-D-01` · `BD-04` |

## `POH-D-02` — straight-line vs units-of-production, absorbed at normal capacity

> ### ⚠ `DO NOT PRESENT AS READY FOR BOSS RULING`

| | |
|---|---|
| **Exact decision** | The absorption method — straight-line or units-of-production — at the confirmed normal-capacity denominator |
| **SMEs Core recommendation** | **WITHHELD.** None is offered, and none may be inferred |
| **Why withheld** | **Two statutory dependencies are unresolved**: `POH-D-02`'s **tax consequences are unresearched**, and the **over-absorption cap's strength** is a declared statutory dependency under `HOLD` (`SC-SMT-11`). A method recommendation that ignores its tax consequence is an unmeasured consequence clause |
| **Thai statutory dependency** | **YES — blocking.** Standing `HOLD / EVIDENCE REQUIRED` |
| **Rulable now?** | **NO** |
| **The control that matters** | **The Thai panel being *commissioned* is NOT Thai statutory validation being *completed*.** `SC-BD-10` approved the commissioning; `SC-20` records it as **approved, not started, no evidence received**. **No panel result exists. None is fabricated here** |
| **Blocks** | costing method design. **Not Phase SA closure by itself, but it must not be ruled ahead of its evidence** |
| **Evidence** | `SC-06` `F5` card · `SC-03` `SC-SMT-11` · `SC-BD-06` §8.3 · `SC-20` (panel status) |

## `POH-D-03` — is `SETUP` time productive?

| | |
|---|---|
| **Exact decision** | Whether `SETUP` time counts as productive time for absorption |
| **SMEs Core recommendation** | **Productive.** Setup is a necessary condition of the output it precedes, so excluding it would push a genuine production cost into the period as if it were idleness — which is the failure mode `BLK-07` §6 rejected for actual-hours (*"capitalises idleness into inventory"*), inverted |
| **Alternatives** | non-productive (setup absorbed as period cost) · configurable per work centre |
| **Consequence** | Product cost carries the setup burden of the run that required it; short runs cost more per unit, which is economically true |
| **Thai statutory dependency** | **None identified.** Not asserted absent — **`NOT FOUND IN SEARCHED SCOPE`**, the searched scope being the `F5` evidence set |
| **Rulable now?** | **YES** |
| **Blocks** | later implementation only |
| **Evidence** | `SC-06` `F5` card · `SA_CORR3_03` `POH-D-03` · `BLK-07` §6 |

## `POH-D-04` — are `IDLE` and `NO_DEMAND` one cause or two?

| | |
|---|---|
| **Exact decision** | Whether idleness and absence-of-demand are a single cause code or two |
| **SMEs Core recommendation** | **Two.** They have different owners and different management responses — `IDLE` is a capacity/operations fact, `NO_DEMAND` is a commercial fact. Collapsing them destroys the distinction at the point of measurement, and no later analysis can recover it |
| **Alternatives** | one cause (simpler, loses the split) · two with a shared parent class |
| **Consequence** | Unabsorbed-overhead analysis can attribute cause; `BD-02` already closes where unabsorbed overhead **goes**, so this decides only how it is **explained** |
| **Thai statutory dependency** | **None** — `BD-02` already fixes the destination, which is the statutory-sensitive half |
| **Rulable now?** | **YES** |
| **Blocks** | later implementation and reporting only |
| **Evidence** | `SC-06` `F5` card · `SA_CORR3_03` `POH-D-04` · `BD-02` |

## `POH-D-05` — who owns the normal-capacity figure and its review cadence?

| | |
|---|---|
| **Exact decision** | Ownership of the normal-capacity figure, and how often it is reviewed |
| **SMEs Core recommendation** | **Owner: Manufacturing/Operations proposes; Accounting Core approves** — because the figure is an absorption denominator with statutory consequences, so the body that owns statutory posting must approve it. **Cadence: a fixed periodic review with a recorded basis per revision**, and **revision as an event, not an edit** |
| **Alternatives** | Operations owns outright · Accounting owns outright · no defined cadence |
| **Consequence** | The denominator stops drifting silently. **`MTA-11`'s pattern applies here too — a figure with no review cadence degrades toward permanence**, and no cadence is designed anywhere in the corpus |
| **Thai statutory dependency** | **Indirect** — the figure's *strength* interacts with the over-absorption cap under `HOLD` (`SC-SMT-11`). **Ownership and cadence do not depend on that**, so this is rulable while `POH-D-02` is not |
| **Rulable now?** | **YES** |
| **Blocks** | later implementation; and it is the control that keeps `POH-D-02`'s eventual answer honest over time |
| **Evidence** | `SC-06` `F5` card · `SA_CORR3_03` `POH-D-05` · `SC-SMT-11` · `MTA-11` |

---

## Readiness summary

| ID | Recommendation | Rulable now |
|---|---|:--:|
| `POH-D-01` | confirm the departure, declared per class | **YES** |
| **`POH-D-02`** | **WITHHELD — statutory `HOLD`** | **NO** |
| `POH-D-03` | `SETUP` is productive | **YES** |
| `POH-D-04` | two causes | **YES** |
| `POH-D-05` | Operations proposes, Accounting Core approves; fixed cadence, revision as event | **YES** |

> **4 of 5 are recommendation-complete and rulable. `POH-D-02` is deliberately outside the ruling
> interface, and the reason is evidence, not caution.**

**None of the five is a Category-3 gap, and none gates Pre-Test entry.**
