# P04 — BOUNDED DEEPENING LOG (G01)

**LAYER 2.** Constitution §6: every material search declares CQ, purpose, exact boundary,
denominator unit, expected result class and stop condition **before** execution.

| # | CQ | Boundary declared | Unit | Result |
|---|---|---|---|---|
| 1 | `CQ-P04-07` | This repository's refs only; path patterns `*P03*`, `*MANUFACTURE*` | file | P03 branch located; mandated SHA refused by remote; head `bc767a8` verified **by content** |
| 2 | `CP-01` | The four mandated SHAs, individually | commit | 2 resolve, 2 are near-miss transcriptions — **declared, not silently repaired** |
| 3 | `CQ-P04-12` | Local PostgreSQL: is a server running? Tool named: `/opt/homebrew/bin/psql` 16.15, `pg_restore` present | server | **No postmaster.** All DB evidence is archives — capability stated with the tool, per this package's own rule |
| 4 | `CQ-P04-01` | `addons/account_asset/models/account_asset.py` | field / method | 10 inherited fields, defaults, `create`, `write` |
| 5 | `CQ-P04-01` | **Every** `_onchange_model_id` in the reference tree | call site | **Disproof succeeded** — `account_move.py:252` |
| 6 | `CQ-P04-02` | `_get_delta_days`, `DAYS_PER_MONTH/YEAR`, lifetime computes | branch | Two implementations; hybrid 30/360 characterised |
| 7 | `CQ-P04-03` | `account_asset`, `maintenance`, `mrp_maintenance` module trees, both directions | reference | **0**, positive control **1** |
| 8 | `CQ-P04-03` | Both declared custom addon trees: modules referencing **both** models | module | Exactly one — `equipment_sequence` |
| 9 | `CQ-P04-03` | Definitions of `account.asset.asset` across all 3 declared trees | definition | **0**, positive control fires |
| 10 | `CQ-P04-03` | `equipment_sequence/models/__init__.py` | import | 5 of 8 files imported |
| 11 | `CQ-P04-03` | Writes of equipment `status` in both custom trees | write | **4, all `'tass'`; 0 writes of `'eqp'`** |
| 12 | `CQ-P04-03` | v18 core `models.py`, `fields.py`; asset view button names | construct | `validate` live, `name_get` dead, `states=` ignored |
| 13 | `CQ-P04-04` | `product_stock_equipment/models/*` | trigger | Receipt-validation creation path |
| 14 | `CQ-P04-08` | `addons/maintenance/models/*.py` — all | reference | **0** to `account.move` / `account.analytic` |
| 15 | `CQ-P04-09` | `account_asset` `write()` | statement | Distribution written to **all** `line_ids` |
| 16 | `CQ-P04-10` | `set_to_close`, `_get_depreciation_amount_end_of_lifetime` | method | Lock raises; end-of-life clamps |
| 17 | `CQ-P04-03` | The installed-module set held in session | module row | `equipment_sequence 18.0.1.6` **installed** |

**Searches declined, and why:** whole-estate sweep for series-16 source (§6, and P03 has already
done it); whole-`/Volumes` traversal; any new archive census; any adjacent-Pxx recursive search;
any Google-Drive or backup sweep. **None was necessary to answer a declared CQ.**

> **Scope monotonicity held.** Every pass above is inside `account_asset`, `maintenance`,
> `mrp_maintenance`, the two declared custom trees, the v18 core, or evidence already in this
> package. **The run went deeper 17 times and never wider.**
