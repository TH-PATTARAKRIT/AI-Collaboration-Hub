# 28 — P03 COMPLETE COST-INJECTION POPULATION

**LAYER 2 — AUDIT QUARANTINE.**

Unit for the *rows* of this table: **one monetisation path** (U2 of `27` §3). Financial,
analytic and price effects are separate columns precisely so the reader can re-count under
any of the four units without re-reading the source.

Reachability column is measured against `iSMEs`, the only readable deployment in which
manufacturing has executed — `evidence/P03T_EXECUTED_OUTPUT.txt`.

---

## 1. The population

| ID | Cost type | Business event | Module · function | Financial | Analytic | WIP | FG | COGS | Scope | Idempotence control | Reachable in `iSMEs` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **M1** | Machine / work centre | Work-order time logged | `mrp_account` · `_cal_price` | **Yes** | No | **Yes** | **Yes** | via FG | `COMPANY` | move state | **NO** — 0 work orders |
| **M2** | Machine + labour relief | Order reaches done | `mrp_account` · `_post_labour` | **Yes** | No | **Yes** | No | indirect | `COMPANY` | **none** (`DC-15`) | **NO** — cost is zero |
| **M3** | Employee | Time log with an employee | `mrp_workorder` · `_cal_cost` | via M1/M2 | No | via M1/M2 | via M1/M2 | via FG | `COMPANY` | inherits M1/M2 | **NO** — module not installed |
| **M4** | Work centre, analytic | Work-order duration changes | `mrp_account` · `_create_or_update_analytic_entry` | No | **Yes** | No | No | No | `TENANT`/`COMPANY` — `36` | update-in-place | **NO** — 0 work orders |
| **M5** | Project, analytic | same event | `project_mrp_account` · override | No | **Yes** | No | No | No | as M4 | **none** (`DC-14`) | **NO** — module not installed |
| **M6** | Employee, analytic | Productivity record | `project_mrp_workorder_account` | No | **Yes** | No | No | No | as M4 | update-in-place | **NO** — module not installed |
| **M7** | Extra unit cost | Manual entry, or subcontract receipt | `mrp_account` · `_cal_price` | **Yes** | No | **Yes** | **Yes** | via FG | `COMPANY` | none — and **no relief** (`DC-03`) | **reachable, but 0 of 10,764 rows non-zero** |
| **M8** | WIP accrual | Period end | `mrp_account` wizard | **Yes** | No | **Yes** | No | No | `COMPANY` | **none** — re-runnable | **NO** — `mrp_accountant` not installed |
| **M9** | Standard cost | Price recompute from BOM | `mrp_account` · `_compute_bom_price` | **price only** | No | via standard | **Yes** | via FG | `COMPANY` | n/a — a recompute | **reachable**; no work centres so the operation term is 0 |
| **M10** | Direct material | Component issue | `stock_account` valuation | **Yes** | via move | **Yes** | **Yes** | via FG | `COMPANY` | move state | **YES — the only live path** |
| **M11** | Subcontract service | Subcontract receipt | `mrp_subcontracting_account` | **Yes** | No | **Yes** | **Yes** | via FG | `COMPANY` | move state | **NO** — module not installed |
| **M12** | Landed cost | Landed-cost record | `mrp_landed_costs` | **Yes** | No | **Yes** | **Yes** | via FG | `COMPANY` | record state | **NO — installed but 0 records ever created** (executed) |
| **M13** | By-product credit | By-product move | `mrp_account` · `_cal_price` | **Yes**, negative | No | **Yes** | **Yes** | via FG | `COMPANY` | move state | **YES — LIVE. 8,176 moves with non-zero cost share** |
| **M14** | Scrap loss | Scrap record | generic inventory-loss path | **Yes** | via move | No | No | No | `COMPANY` | move state | **YES — LIVE. 2,286 scrap records, 2,295 scrapped moves** |
| **M15** | Unbuild release | Unbuild order | `mrp_account` · `_get_out_svl_vals` | **Yes** | No | No | **Yes**, reversing | via FG | `COMPANY` | order state | **YES — LIVE. 987 unbuild orders, 4,132 unbuild moves** |
| — | Equipment depreciation | Depreciation posting | **no path** | — | **nets to zero** — `33` | **No** | **No** | **No** | `COMPANY` | — | **no path** |
| — | Maintenance, energy, indirect labour, fixed overhead | — | **no path** | — | — | **No** | **No** | **No** | — | — | **no path** |
| — | Variance | — | **no object** | — | — | — | — | — | — | — | — |
| — | Rework | — | **no object** | — | — | — | — | — | — | — | — |

## 2. Counts, per unit, executed

| Unit | Definition | Count over §1 |
|---|---|---|
| **U1** — writer of inventory carrying value | changes FG/WIP carrying value | **M1, M2, M7, M10, M11, M12, M13, M15 = 8** |
| **U2** — monetisation path | own rate **or** driver **or** destination ledger | **M1…M9 = 7 after the collapses P04 declares; 9 rows as listed** |
| **U3** — posting artefact | own artefact that lands | **9** across M1–M9 |
| **U4** — monetary computation | one arithmetic result | **6** |
| **Live in `iSMEs`** | executes with non-zero effect | **M10, M13, M14, M15 = 4**, plus M9's material term |

> **U1 = 8 here, against U1 = 2 in `27` §3.** The difference is deliberate and is not an
> inconsistency: `27` §3 counts writers of **conversion** cost — the subject of the AAS+
> veto — while this table counts writers of **inventory value** including materials,
> landed cost, by-products, unbuild and subcontracting. **Same unit name, different
> population.** Stated explicitly because `smeplus-count-unit-vs-population-lesson` records
> that declaring a unit does not save a count whose *population* silently shifts.

## 3. The result that matters

Fifteen mechanisms exist in source. **Four are live.**

**A correction to this file's own first draft.** It originally read *"One is live"*, on the
strength of `M10` alone, while the table above already marked `M13`, `M14` and `M15`
*reachable*. The headline did not reconcile with the table beneath it. The three were then
**measured** rather than argued:

| Mechanism | Executed measurement (`iSMEs`) |
|---|---|
| `M13` by-product | `stock_move.cost_share` non-zero = **8,176** |
| `M14` scrap | `stock_scrap` = **2,286**; `stock_move.scrapped` = **2,295** |
| `M15` unbuild | `mrp_unbuild` = **987**; `stock_move.unbuild_id` = **4,132** |
| positive control | `stock_move` = 103,949; `raw_material_production_id` = 41,029; `production_id` = 20,230 |

`M12` was measured the same way: `stock_landed_cost` = 0 rows in both databases against a
same-run control of `mrp_production` = 10,764 — installed, never used.

Recorded as research error `RE-P03-14`: a headline count asserted from one member instead
of enumerated from the table it summarised. This is `smeplus-totals-are-unverified-claims`
exactly — the finding rows were verified, the total describing them was not.

> **`P03T-F-04`. Of fifteen identified cost-injection mechanisms, exactly one — direct
> material issue — executes in the only deployment where manufacturing runs.** Eight are
> blocked by uninstalled modules, five by absent master data, and one (`M7`) is installed
> and reachable but carries a zero on all 10,764 rows.

`FACT VERIFIED`, bounded by `26` §5.
