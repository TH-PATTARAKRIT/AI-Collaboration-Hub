# 04 — P03 MACHINE COST OWNERSHIP MATRIX

**LAYER 2 — AUDIT QUARANTINE.**

The prompt names this as a mandatory critical attack:

> Work Center Cost · Equipment Cost · Operation Cost · Asset Depreciation Allocation ·
> MO Cost · Service Cost · Overhead Allocation **must NOT create duplicate economic cost.**

---

## 1. Prior evidence this file is bound by

`ASSET_DR_CONTINUATION/07` §3 (`origin/research/asset-deep-continuation-2026-09-04-001`)
put the hypothesis *"Work Centre = Cost Bucket"* to challenge and **rejected it on
evidence**, demoting the work centre from cost bucket to resource group. `22` §6 records
three further rejected readings, including *"treating the work-centre hourly rate as the
cost bucket for depreciation"*.

**P03 does not reopen that ruling.** This matrix takes it as settled and asks the
consequent P03 question: *given that the rate is rejected as the vehicle, what carries
machine cost into WIP today, and what must SMEsPlus own?*

## 2. The ownership matrix

| Candidate owner | Does it exist in the reference product? | Does it inject cost into WIP? | Verdict |
|---|---|---|---|
| **Work centre** | Yes — with exactly one hourly cost scalar (`mrp/models/mrp_workcenter.py:43`) | **Yes — the only machine-cost injector** | Injects, but **rejected as the correct owner** by `ASSET_DR_CONTINUATION/07` §3 |
| **Equipment / machine record** | Yes, in the maintenance domain | **No** — `ASSET_DR_CONTINUATION/06` §4 found its own cost field to be a second, inert, unreconciled source | Does not inject |
| **Operation / routing line** | Yes | No — it reads the work centre's rate (`mrp_account/models/mrp_routing.py:10-12 — _total_cost_per_hour`) | Pass-through only |
| **Work order** | Yes — carries a rate **snapshot** field | **No** — `ASSET_DR_CONTINUATION/22` §6 established that neither the valuation nor the ledger path reads the snapshot; P03 confirms independently: `_cal_cost` reads `wo.workcenter_id.costs_hour`, never `wo.costs_hour` (`mrp/models/mrp_workorder.py:587`) | **Inert. Confirms `CTR-C-06`.** |
| **Asset / depreciation** | Yes, in the asset domain | **No path found** — scope in `02` §3 | The gap |
| **MO** | Yes | Only as the aggregation point | Aggregator, not owner |
| **Overhead object** | **Does not exist** in the declared scope | — | The second gap |

## 3. The independent confirmation of `CTR-C-06`

`ASSET_DR_CONTINUATION` rejected reliance on the work-order rate snapshot as a rate
guarantee. P03 reached the same conclusion by a different route and states the mechanism:

| Reader | Rate source | Cited |
|---|---|---|
| `_cal_cost` — **the value that is posted** | `wo.workcenter_id.costs_hour` | `mrp/models/mrp_workorder.py:587` |
| Analytic mirror | `wo.workcenter_id.costs_hour` | `mrp_account/models/mrp_workorder.py:46` |
| `_compute_expected_operation_cost` — **display only** | `self.costs_hour or self.workcenter_id.costs_hour` | `mrp/models/mrp_workorder.py:906` |
| `_get_current_theorical_operation_cost` — **display only** | `self.costs_hour or self.workcenter_id.costs_hour` | `mrp/models/mrp_workorder.py:909-912` |
| Cost-structure report | `CASE WHEN wo.costs_hour = 0.0 THEN wc.costs_hour ELSE wo.costs_hour END` | `mrp_workorder_hr_account/report/mrp_cost_structure.py:61` |

**Every path that posts money ignores the snapshot. Every path that shows a number to a
human honours it.** Change the work centre's rate after a work order has run and the
report and the ledger will disagree, permanently and silently. `FACT VERIFIED`.

Recorded as `DC-06`.

## 4. Duplicate-cost test, element by element

The mandated attack, run as a test rather than an assertion. `Y` = a second independent
injection of the same economic cost exists.

| Pair tested | Duplicate? | Reasoning |
|---|---|---|
| Work-centre cost **vs** equipment cost | **No** | The equipment cost field is inert. Cannot duplicate what never posts |
| Work-centre cost **vs** operation cost | **No** | Operation reads the work centre. One rate, one read |
| Work-centre cost **vs** asset depreciation | **No — today** | No depreciation path exists. **`Y` the moment SMEsPlus adds one without retiring the rate** |
| Work-centre cost **vs** employee cost | **Conditional `Y`** | Same interval, two rates, no control on the machine rate's content — `DC-02` |
| Work-centre cost **vs itself**, across overlapping time logs | **`Y` — confirmed** | `DC-01`, the headline finding |
| MO cost **vs** work-order cost | **No** | MO cost is the sum of its work orders |
| Service cost **vs** component cost, subcontracting | **No** | Explicitly split at `mrp_subcontracting_account/models/stock_move.py:28-32` |
| Overhead allocation **vs** anything | **Not testable** | No overhead object exists |

## 5. What SMEsPlus must own — `DESIGN CANDIDATE`

Stated as requirements, not as a design. No implementation is authorised; the AAS+ veto
from `ASSET_DR_CONTINUATION` stands and is restated in `21_P03_PMO.md` §3.

| # | Requirement | Because |
|---|---|---|
| `R-01` | Machine cost must be owned at the grain the business asked for, not at the resource group | `ASSET_DR_CONTINUATION/07` §3 |
| `R-02` | **Exactly one** cost injection path per economic cost, enforced structurally, not by convention | `05` `DC-01` … `DC-04` |
| `R-03` | Every cost rate must declare its content as a validated attribute | `DC-02` |
| `R-04` | The rate in force at the time of the event must be the rate that posts — snapshot and posting must read the same field | `DC-06` |
| `R-05` | A fixed-overhead absorption model with an explicit **capacity denominator** must exist before any depreciation reaches inventory | `CC-07` … `CC-14`; TAS 2 ¶13 |
| `R-06` | The machine-hour base must be an **overlap-merged** interval, and the same number must serve display, analytic and ledger | `DC-01`, `DC-05` |

## 6. The dependency that governs `R-05`

`R-05` cannot be specified until `ASSET_DR_CONTINUATION` `BLK-07` is decided:

> Is the productive allocation rate `period depreciation ÷ normal capacity hours` or
> `period depreciation ÷ actual productive hours`?
> **Status: HOLD — DESIGN DECISION REQUIRED. Owner: Boss.**

**P03 does not decide it and does not recommend against the prior recommendation.**
The Asset package recommends *normal capacity* and records the alternative as
`REJECTED — INVALID ASSUMPTION`. P03 adds one observation in support, from its own
evidence: the reference product's only existing rate is a **flat hourly scalar with no
denominator at all**, so there is no incumbent behaviour to preserve and no migration
cost attached to choosing the compliant option. Recorded as `DEP-01`.
