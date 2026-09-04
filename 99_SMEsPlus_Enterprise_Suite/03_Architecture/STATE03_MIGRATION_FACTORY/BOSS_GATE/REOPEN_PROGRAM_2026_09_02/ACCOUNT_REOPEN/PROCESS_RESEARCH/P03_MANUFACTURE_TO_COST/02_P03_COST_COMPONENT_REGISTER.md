# 02 — P03 COST COMPONENT REGISTER

**LAYER 2 — AUDIT QUARANTINE.**

The cost **taxonomy** (direct/indirect, fixed/variable, item nature, and each element's
statutory destination) is already established and adopted in
`ASSET_DR_CONTINUATION/12_MANUFACTURING_COST_CLASSIFICATION_MATRIX.md`
(`origin/research/asset-deep-continuation-2026-09-04-001`).

**This register does not re-derive it.** It asks the one question that document did not:
**by what code path does each element actually reach WIP, and is that path single?**

---

## 1. Register

Legend for *Paths*: the number of independent writers that can put this element into
inventory value. The canonical target is exactly **1**.

| ID | Cost element | Reaches WIP? | Injection path | Paths | Class |
|---|---|---|---|---|---|
| `CC-01` | Direct material | Yes | Raw stock moves → valuation layers, summed in `_cal_price` | 1 | `FACT VERIFIED` |
| `CC-02` | Indirect material / consumables | Yes, if on the BOM | Same as `CC-01` | 1 | `FACT VERIFIED` |
| `CC-03` | **Machine / work-centre time** | Yes | `_cal_cost()` machine half → `_cal_price` | **1 financial, but see `05` `DC-01`** | `FACT VERIFIED` |
| `CC-04` | **Direct labour (employee)** | Yes | `_cal_cost()` employee half → `_cal_price` | 1 financial | `FACT VERIFIED` |
| `CC-05` | Subcontract / outside processing | Yes | `extra_cost` ← subcontract receipt price | 1 | `FACT VERIFIED` |
| `CC-06` | Manual extra cost | Yes | `extra_cost`, keyed by a human | 1 capitalisation, **0 relief** | `FACT VERIFIED` |
| `CC-07` | **Equipment depreciation** | **No path — and the one candidate path is structurally incapable**, §5 | — | **0** | `FACT VERIFIED`, scope §3 |
| `CC-08` | Factory building depreciation | **No path** | — | **0** | `FACT VERIFIED`, scope §3 |
| `CC-09` | Right-of-use asset depreciation | **No path** | — | **0** | `FACT VERIFIED`, scope §3 |
| `CC-10` | Maintenance — planned | **No path** | — | **0** | `FACT VERIFIED`, scope §3 |
| `CC-11` | Maintenance — unplanned | n/a — must be period expense | Reaches P&L by its own accounting, not via P03 | 0 | `FACT VERIFIED` |
| `CC-12` | Energy / utilities | **No path** | — | **0** | `FACT VERIFIED`, scope §3 |
| `CC-13` | Indirect labour / factory supervision | **No path** | — | **0** | `FACT VERIFIED`, scope §3 |
| `CC-14` | Fixed overhead generally | **No path, and no denominator** | — | **0** | `FACT VERIFIED`, scope §3 |
| `CC-15` | Landed production cost | Only via the landed-cost module, applied to receipts | Outside the MO cost model | 1, foreign | `SUPPORTED INTERPRETATION` |
| `CC-16` | Scrap loss | Not re-absorbed into good units | Generic inventory-loss path | 0 into WIP | `FACT VERIFIED` |
| `CC-17` | By-product credit | Yes, as a **negative** share of `total_cost` | `_cal_price` `cost_share` | 1 | `FACT VERIFIED` |
| `CC-18` | Co-product | **Not modelled as a distinct concept** | Represented as a by-product with a cost share | — | `FACT VERIFIED` |
| `CC-19` | Rework cost | **No object exists** | — | 0 | `FACT VERIFIED`, scope §3 |
| `CC-20` | Variance (actual vs standard) | Absorbed silently into the production account | No variance object | 0 explicit | `FACT VERIFIED` |

## 2. The shape of the result

Of twenty elements, **eleven have exactly one injection path, eight have none, and one (`CC-15`) has a single path that lies outside the MO cost model.** 11 + 8 + 1 = 20.

*(Corrected by AAS-03 `C-07`; the first draft of this sentence miscounted its own register.)*

The eight with none — `CC-07` … `CC-14`, excluding `CC-11` which is correctly a period
expense — are precisely the elements that
`ASSET_DR_CONTINUATION/12` §3 classifies as **fixed production overhead that TAS 2 ¶12
names expressly as part of conversion cost**.

> **The reference product has no mechanism to capitalise fixed production overhead into
> inventory.** The only vehicle that could carry it — the work-centre hourly rate — was
> examined and **rejected** on evidence in `ASSET_DR_CONTINUATION/07` §3, and that
> rejection stands unchanged here.

This is not a configuration gap. It is a modelling gap, and it is the same one
`ASSET_DR_CONTINUATION/12` §2 identifies from the asset side. P03 reaches it
independently, from the cost-injection side, and the two agree.

**Caveat, inline at AAS+ `AASP-03`'s insistence.** All eight "no path" rows stand or fall
together on the scope in §3. The running system's installed-module list is **unknown**
(`DEP-04`, and Asset query `Q-04` at priority 1). A single unexamined installed module
supplying an overhead path would overturn this entire conclusion. The conclusion is
therefore stated as **bounded by the declared source root**, and must not be quoted
without that bound.

## 3. Scope of every negative claim in §1

Required by `smeplus-deep-research-negative-claim-standard`. "No path" above means
**NO EVIDENCE FOUND within this declared scope**, and must not be read as
"the function does not exist".

- **POPULATION:** the manufacturing-related module set of the v18 Enterprise source tree
  — `mrp`, `mrp_account`, `mrp_account_enterprise`, `mrp_accountant`, `mrp_workorder`,
  `mrp_workorder_hr_account`, `mrp_subcontracting`, `mrp_subcontracting_account`,
  `mrp_landed_costs`, `mrp_maintenance`, plus `stock_account`, `hr_hourly_cost`,
  `account_asset`, `maintenance`, `project_mrp_workorder_account`.
- **PATTERN:** identifier search across `*.py` for the cost-rate and cost-posting
  vocabulary — `costs_hour`, `_cal_cost`, `_total_cost_per_hour`, `employee_cost`,
  `hourly_cost`, `extra_cost`, `_post_labour`, `_cal_price`,
  `account_production_wip*`, `property_stock_account_production_cost_id`, `rework`.
- **PATH SET:** `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/`
  (797 modules; the target-generation Enterprise tree).
- **UNIT:** one identifier occurrence in one source file, excluding `tests/`.

**Not covered by this scope, and therefore not claimed either way:** the running UAT
system's installed-module list. `ASSET_DR_CONTINUATION/22` §4 raises exactly this as
query `Q-04` at priority 1. **P03 inherits that dependency rather than assuming an
answer** — see `14_P03_DEPENDENCY_REGISTER.md` `DEP-04`.

## 4. Elements where the rate's *content* is undeclared — `DESIGN CANDIDATE`

`CC-03` and `CC-04` are charged on the same time interval at two different rates. That
is legitimate two-element absorption **if and only if** the machine rate excludes labour.

Nothing in the reference product declares, constrains or validates what the machine rate
contains. A site that enters a fully-loaded rate and also runs employee time logs
double-charges labour, and no control detects it.

**`DC-02` in `05` records this.** The SMEsPlus requirement it generates:
*the content of every cost rate must be a declared, validated attribute of the rate, not
a convention in an administrator's head.*

## 5. Why the believed depreciation route cannot work — verified after P04 peer review

`CC-07` … `CC-09` are recorded above as "no path". The route practitioners most often
assume carries depreciation into a cost pool is the **analytic dimension**. It cannot.

`account_asset/models/account_move.py:297-299` sets `analytic_distribution` on **both**
lines of the depreciation entry. The two lines are equal and opposite, so the analytic
amounts generated are `+x` and `-x`.

> **The analytic dimension nets to zero on a depreciation entry and can never accumulate a
> depreciation cost pool.**

`FACT VERIFIED`. Raised by P04 and independently verified from source here — `25` §5.

**This statement survives `DEP-04`**, unlike the rest of §2: it does not depend on which
modules are installed, only on how the depreciation entry is built. It is therefore the
strongest single element of the `02` §2 conclusion, and the one a reviewer should attack
last rather than first.
