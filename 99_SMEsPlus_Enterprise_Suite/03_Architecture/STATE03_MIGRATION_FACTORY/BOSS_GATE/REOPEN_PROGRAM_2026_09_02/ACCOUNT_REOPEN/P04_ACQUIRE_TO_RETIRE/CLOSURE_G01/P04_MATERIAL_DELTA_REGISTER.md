# P04 — MATERIAL DELTA REGISTER (G01 CLOSURE)

**LAYER 2.** Constitution §5. Every additional pass declares ID → CQ → bounded surface →
insufficiency → stop condition, **before** execution.

---

| ID | CQ | Bounded evidence surface | Why prior evidence insufficient | Stop condition | Outcome |
|---|---|---|---|---|---|
| **MD-P04-01** | `CQ-P04-12`; bounds `-01`,`-02`,`-03` | Deployment/version evidence **already enumerated** in `13` `EV-DB`. **No new archive discovery** | `P04-F-85` established the generations differ; it never asked whether the matching source is obtainable | Every asset-bearing identity has a stated series, and closability is answered once | **CLOSED.** P04 does not reproduce P03's defect; residual source gap `UNRESOLVED`, `P04-B-51` |
| **MD-P04-02** | `CQ-P04-01` | `account_asset/models/account_asset.py` — `_onchange_model_id`, `create`, `write`, field defaults | The base package described model→asset transfer generically; the exact field set and the write paths were never enumerated | The ten fields and every call site are named | **CLOSED.** `P04-F-145`, `P04-F-146` |
| **MD-P04-03** | `CQ-P04-01` | Every invocation of `_onchange_model_id` across the reference tree | **A disproof of MD-P04-02's headline was mandatory** and had not been run | Either an invocation outside the form exists, or none does | **CLOSED — HEADLINE FALSIFIED.** `_auto_create_asset` calls it. Finding withdrawn and reissued narrower |
| **MD-P04-04** | `CQ-P04-03` | `equipment_sequence` — 8 model files, `__init__.py`, both custom trees; definitions of `account.asset.asset` in all 3 declared trees with a positive control | The base package said *"partly dead code"* without characterising which part or why | The live link and the dead link are each identified | **CLOSED.** `P04-F-148`, `P04-F-149` |
| **MD-P04-05** | `CQ-P04-03` | v18 core `models.py` / `fields.py`; `account_asset` view button names | Three v17-era constructs sat inside a live class; whether each fires was unknown | Each of `validate`, `name_get`, `states=` classified live or dead | **CLOSED.** `validate` live; `name_get` dead; `states=` ignored → no readonly control |
| **MD-P04-06** | `CQ-P04-04`, `-08` | `addons/maintenance/models/*.py` — every file | Non-productive cause attribution had no established accounting representation either way | Whether maintenance reaches `account.move` / `account.analytic` at all | **CLOSED.** Zero references. `P04-F-152` |
| **MD-P04-07** | `CQ-P04-09` | `account_asset` `write()` analytic propagation | The net-to-zero effect was **measured** but its cause was never located in source | The statement that writes the distribution is identified | **CLOSED.** `P04-F-153` — one line, written to all `line_ids` |
| **MD-P04-08** | `CQ-P04-03` | The installed-module set already held in this session | *"`_inherit` on a missing model ⇒ cannot install"* was a plausible inference, not evidence | Whether `equipment_sequence` is recorded installed | **CLOSED — INFERENCE FALSIFIED.** It is installed at `18.0.1.6`; the file is simply never imported |

## Candidate deltas **rejected** as non-material (Class E) — recorded, not opened

| Candidate | Why rejected |
|---|---|
| Per-line rounding policy of the depreciation board | Not required by `CQ-P04-02`; opening it widens the run |
| UI reachability of `name_asset`; degraded label from the dead `name_get` | Cannot change an accounting conclusion |
| Full trace of `_compute_board_amount` | `CQ-P04-02` asks for the day convention, which `_get_delta_days` answers completely |
| The other 1,270 modules in the reference tree | No declared CQ reaches them |
| Re-enumerating the host for series-16 source | **Forbidden** — Constitution §6; P03 already did it with a firing control |

> **Five candidate deltas declined. Eight executed. Two of the eight falsified a claim this run
> had already written down** — and in both cases the falsifier was the mandated disproof, not a
> re-reading.
