# VDR_CONFIGURATION_DEEPENING_REPORT.md
# Configuration OFF vs ON — what the gate census establishes, and what it does not

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Commissioning instruction §7: every applicable element must have its **CONFIG OFF vs CONFIG ON**
consequence determined.

---

## 1. Denominator and instrument

| Clause | Value |
|--------|-------|
| **POPULATION** | frozen `POPULATION_V3`, 5,074 items |
| **ELIGIBILITY** | classes for which `CONFIGURATION` is applicable → **4,112** |
| **UNIT** | one element, and its gate — not one gate |
| **PATTERN** | parsed declaration attributes across **twelve** element kinds, plus the settings census; **not** a `<button>`/`<field>` grep |
| **COVERAGE ASSERTION** | 4,112 of 4,112 eligible items carry a recorded `CONFIG_CONDITION` — **100%** |
| **POSITIVE CONTROL** | a synthetic gated element injected into the parse set was located and its gate resolved |

> **Why the pattern width matters.** An earlier round read gating from `<button>` and `<field>` only
> and published **87** gated elements. Widening to all twelve element kinds that can carry a gate gave
> **633**. The count did not grow because more evidence appeared; it grew because the instrument could
> finally see the population it claimed to measure. `CORR-F-07`.

## 2. The census — 4,112 elements

| Condition | n | % |
|-----------|--:|--:|
| **No element-level configuration condition** (established by census, instrument-validated) | 3,140 | 76.4% |
| **Gated by a group** | 709 | 17.2% |
| **Is itself a configuration switch** | 237 | 5.8% |
| Other recorded conditions | 26 | 0.6% |

**Distinct gates in use: 48.** Gated elements by class: gate-bearing view elements 525 · buttons 72 ·
extension menus 62 · menus 35 · fields 15.

### The ten most-used gates

| Gate | Elements |
|------|---------:|
| multi-location | 94 |
| unit-of-measure | 76 |
| production lot | 66 |
| **multi-company** | **65** |
| lot/serial tracking | 57 |
| **technical-only ("no one")** | **55** |
| stock manager role | 29 |
| routing | 26 |
| base user | 23 |
| quality user | 21 |

## 3. Findings

### `C3-F-01` — 76.4% of the configurable surface carries no element-level gate.
Three quarters of
elements appear regardless of configuration. Configuration in this system is concentrated: **48 gates
govern 709 elements**, and the remaining 3,140 are always present. For SMEsPlus this is a scoping
result — a derived design does not need a gate per element; it needs a small, well-chosen gate set.

### `C3-F-02` — 55 elements are gated to a technical-only group.
These are visible to no ordinary role.
They are *present* but *unreachable by any business user*, which is a different condition from either
OFF or ON and is the condition under which `CRITICAL-GAP-06` hides an object joining 91% of movements.
**A gate that hides an element from every business role is not a configuration option; it is a
concealment.** SMEsPlus should not inherit this pattern without an explicit decision.

### `C3-F-03` — multi-company is a gate on 65 elements, and it is a *display* gate.
It governs what is
shown, while actual isolation is enforced by record rules — of which **16 admit company-less records**
(`CRITICAL-GAP-04`). Turning the gate OFF does not turn isolation ON or OFF. **Anyone reasoning about
company isolation from the configuration surface alone will reach the wrong conclusion.**

### `C3-F-04` — the vocabulary correction, restated because it changed a published zero.
This session's
predecessor published *"zero occurrences of feature toggle / optional module / toggle across 5,193
lines"* as a controlled zero. It was false. **The corpus names the concept a "capability switch"** — 56
occurrences across 17 of 26 files, with a dedicated function *"Change a capability switch"* carrying all
eight depth dimensions, and a dedicated study rating its configuration risk HIGH. The positive control
had been the word `toggle`, drawn from my own vocabulary rather than the corpus's, **so it could not
fire, and its silence read as confirmation**. `RC-F-01` retracted; `CORR-F-37`.
> **The rule that follows:** a positive control must be drawn from the corpus being searched, never
> from the searcher's vocabulary.

## 4. Why CONFIGURATION is 0.17% RESEARCH-VERIFIED (7 of 4,112)

`DETERMINED` is 100%: every element's gate — or the determined absence of one — is established.

`RESEARCH-VERIFIED` requires the **OFF-vs-ON consequence across all nine axes**: visibility ·
reachability · what data is written · default value · validation applied · dependent function enabled ·
downstream financial effect · reversibility of the switch · behaviour of records created while the
setting was in the other state.

**Only 7 items meet it** — seven settings whose full OFF/ON consequence was traced end to end. For the
other 4,105, **the gate is known and the consequence is not.** Establishing the ninth axis in
particular — what happens to records created under the opposite setting — requires controlled installs
with the setting flipped, which this session did not perform and does not claim.

**The gap is named, sized, and reproducible. It is not closed.**
