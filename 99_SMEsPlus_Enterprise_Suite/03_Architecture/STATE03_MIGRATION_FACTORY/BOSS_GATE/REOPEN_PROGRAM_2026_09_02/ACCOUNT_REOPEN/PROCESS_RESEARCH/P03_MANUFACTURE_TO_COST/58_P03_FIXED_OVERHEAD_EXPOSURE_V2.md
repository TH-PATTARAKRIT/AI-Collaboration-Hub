# 58 — FIXED OVERHEAD EXPOSURE V2

**LAYER 2 — AUDIT QUARANTINE.** Supersedes `40` on reachability only; `40`'s source
analysis stands.

---

## 1. Per-element classification, four databases

| Element | Classification | Evidence |
|---|---|---|
| **Equipment depreciation** | **NO SOURCE PATH** | no asset reference in any manufacturing module; the analytic candidate route **nets to zero by construction** (`02` §5, P04-F-49, P09) |
| **Building depreciation** | **NO SOURCE PATH** | same asset mechanism |
| **Right-of-use depreciation** | **NO SOURCE PATH** | same |
| **Planned maintenance** | **NO SOURCE PATH** | `mrp_maintenance` **is installed in `iTEST02`** and links equipment → work centre only; it carries **no cost** |
| **Energy / utilities** | **NO SOURCE PATH** | no mechanism found in 4 module sets |
| **Indirect labour** | **NO SOURCE PATH** | `hr_hourly_cost` installed in `iTEST02`; it prices **direct** time logs only |
| **Overhead pool** | **NO SOURCE PATH, NO DENOMINATOR** | no pool object exists |
| **Machine cost via the work-centre rate** | **SOURCE PATH EXISTS — CONFIGURATION NOT ENABLED** | **1 of 60** work centres rated. This is the one element that moved |

## 2. What changed from `40`

`40` classified everything as *NO PATH VERIFIED*, bounded by three databases and by
`DEP-04`. With `DEP-04` **fully closed on four databases**:

| Change | Detail |
|---|---|
| The bound is removed | `DEP-04` closed 4 of 4 — `61` |
| One element reclassified | machine cost via the rate: from *no path* to **path exists, 1.7 % enabled** |
| Seven elements **confirmed** | `mrp_maintenance` and `hr_hourly_cost` being installed in `iTEST02` **strengthens** the negative: the modules that would most plausibly carry maintenance and indirect labour are present **and still carry no path to inventory** |
| The analytic route | remains **structurally incapable**, and that is independent of installation |

> **`P03R-F-08`. Fixed production overhead has no path into inventory value in any of the
> four deployed databases, with every plausibly relevant module installed in at least one
> of them.** This is the strongest form this negative has taken, and it is now bounded by a
> **complete** module population rather than an unknown one. `FACT VERIFIED`.

## 3. The bound that remains

Still bounded to: the declared source root, and four dumped databases of **two different
schema generations** (`iTEST02` has no `stock_valuation_layer` table — `51` §6). Not a
claim about a running system, and not a claim about versions not represented here.

Per `63`, the permitted form is *"NO PATH VERIFIED IN THE EXAMINED DEPLOYMENTS"*, never
*"no path exists"*.

## 4. Consequence for `BLK-07`

Unchanged and reinforced. `BLK-07` decides the **denominator** of a fixed-overhead
absorption rate. Measured: the **numerator** has no data source in any of the four
databases, and the one mechanism that could carry it is enabled on 1 work centre of 60.

**P03 does not reopen, recommend on, or evaluate the third option P04 opened.** Recorded to
the Asset register as supporting evidence, `DEP-01` unchanged.
