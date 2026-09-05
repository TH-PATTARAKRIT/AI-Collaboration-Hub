# P03 — FIXED-OVERHEAD INJECTION MATRIX

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P03-05`. No expansion into maintenance, energy or HR
domains.

---

## 1. Per-component disposition

| Component | Source mechanism | Configured | Exercised | Driver / event | Target cost object | Fin vs mgmt | **Gap class** |
|---|---|---|---|---|---|---|---|
| **Depreciation** | **absent** — no asset reference in any manufacturing module, either series | n/a | n/a | none | none | financial only, to P&L | **SOURCE GAP** |
| **Planned maintenance** | **absent** — `mrp_maintenance` links equipment → **work centre** and carries **no cost** | installed in 2 of 4 DBs | no | none | none | — | **SOURCE GAP** |
| **Repair** | no evidence of a distinct repair-cost path within the P03 boundary | — | — | — | — | — | **SOURCE GAP** (scope-bounded) |
| **Energy / utilities** | **absent** | n/a | n/a | none | none | — | **SOURCE GAP** |
| **Indirect labour** | **absent** — `hr_hourly_cost` prices **direct** time logs only | installed in 2 of 4 DBs | no | none | none | — | **SOURCE GAP** |
| **Overhead pool + capacity denominator** | **absent** — no pool object exists | n/a | n/a | none | none | — | **SOURCE GAP** |
| **Machine cost via the work-centre rate** | **present** | **1 of 60** work centres rated | **no** — the deployment with rates has no valuation | work-order duration | MO → WIP → FG | financial | **CONFIGURATION + DEPLOYMENT GAP** |

## 2. Why these are source gaps and not configuration gaps

The distinguishing test is whether **installing the plausibly-relevant module** creates a
path. It does not:

| Module | Installed where | Supplies an inventory path? |
|---|---|---|
| `mrp_maintenance` | `iTEST02`, `BK12MAY26` | **No** — equipment ↔ work centre only, no cost |
| `hr_hourly_cost` | `iTEST02`, `BK12MAY26` | **No** — direct time logs only |
| `mrp_landed_costs` | all four | **No** for conversion cost; and **0 landed-cost records** anywhere |
| `mrp_accountant` | `iTEST02` only | WIP accrual only, **self-reversing**, and **not installed** in the manufacturing database |
| `account_asset` | all four (733 assets across three) | **No manufacturing reference in either direction** |

> **`P03R-F-08` restated with a complete installed-module population across four databases:
> fixed production overhead has no path into inventory value, with every plausibly relevant
> module installed in at least one deployment.**

## 3. The candidate route, and why it cannot carry the cost

The analytic dimension is the route most often assumed. It **cannot**:
`account_asset` writes the distribution onto **both** legs of the depreciation entry; the legs
are equal and opposite; the analytic amounts are mirror images and **net to zero**.

Independently reached by **P04**, **P09** and **P03**. **Structural, not configuration-
dependent, and independent of `MD-01`** — it does not rest on which series was read, only on
how a two-legged entry is built.

## 4. Version bound

Source read in **series 18**; the deployment runs **series 16** (`MD-01`). The negative is
therefore stated as: **no path found in the series read, and no path exercised in any of the
four databases measured.** The *measured* half is version-independent; the *source* half is
not.

## 4b. The conclusion is TWO claims, not one — `CC-04`

Challenge forced this split. Stating them as one claim overstated the weaker half:

| Claim | Evidence base | Status |
|---|---|---|
| *No fixed-overhead mechanism exists in the source* | series 18 read, series 19 cross-checked | **BOUNDED TO 18/19.** Cannot be asserted of the series-16 deployment |
| *No fixed-overhead cost is exercised in any of the four deployments* | the databases themselves | **VERSION-INDEPENDENT — survives `MD-01` entirely** |

**The measured claim is the load-bearing one**, and it is the one a design decision should
rest on.

## 5. Disposition

> **`CQ-P03-05` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** that no fixed-overhead
> component reaches inventory value in any examined deployment.
>
> Whether SMEsPlus **must** capitalise them is **`BOSS DECISION REQUIRED`** and sits on the
> Asset register as `BLK-07` / `BLK-08`. **P03 does not reopen, recommend on, or evaluate
> P04's third option.** `DEP-01` unchanged.
