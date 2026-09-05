# 61 — DEP-04 CLOSURE RECONCILIATION

**LAYER 2 — AUDIT QUARANTINE.**

---

## 1. Authoritative definition, retrieved

`DEP-04`, P03 `14`: *the running system's installed-module list is unknown, and **caps every
negative claim in the package**.* Originally raised by the Asset track as priority-1 query
`Q-04`, on the reasoning that every "does not exist" in two research packages was bounded by
source trees and that the bound could not be dropped until the installed modules were known.

## 2. Closure evidence

| Database | Installed modules | Obtained |
|---|---|---|
| `BK12MAY26` | **251** | round 3 |
| `iSMEs` | **190** | round 3 |
| `iTEST02` | **453** | **round 4** — via already-running runtime, `62` |
| `iEVING` | not extracted; manufacturing tables empty, so no manufacturing claim rests on it | — |

> **`DEP-04` — CLOSED for all four databases that carry manufacturing evidence.**
> Three module lists obtained; the fourth database has no manufacturing data for any
> negative claim to be bounded by.

## 3. Which negative claims can now be upgraded

| Claim | Was | Now |
|---|---|---|
| No fixed-overhead path into inventory | bounded by unknown modules | **Upgraded** — the plausibly relevant modules (`mrp_maintenance`, `hr_hourly_cost`, `mrp_landed_costs`, `mrp_accountant`, `mrp_subcontracting`) are **all installed in `iTEST02`** and still supply no path (`58`) |
| No depreciation reference in manufacturing modules | bounded | **Upgraded** — confirmed across the complete installed set |
| The analytic route cannot carry depreciation | independent of modules | unchanged — it was never bounded by `DEP-04` |
| No custom addon overrides manufacturing cost | bounded by 3 roots | unchanged — `27` §7, independent of `DEP-04` |

## 4. Which claims are **downgraded** by the same evidence

`DEP-04`'s closure cuts both ways, and this is the part a closure report most easily omits:

| Round-3 claim | Status |
|---|---|
| *"`project_mrp_account` not installed in any readable dump"* → `DC-14` unreachable | **FALSIFIED** — installed in `iTEST02` |
| *"`project_mrp_workorder_account` not installed"* → `DC-10` confirmed inert | **FALSIFIED** — installed in `iTEST02` |
| *"the conversion-cost apparatus has never been switched on"* | **FALSIFIED beyond `iSMEs`** — 60 work centres, 204 work orders in `iTEST02` |

**Closing `DEP-04` overturned three round-3 conclusions and strengthened two.** That is the
correct behaviour of an evidence gap being closed, and it is why the gap mattered.

## 5. What remains bounded

| Residual | Effect |
|---|---|
| No claim extends to a system not represented by these four dumps | every negative keeps *"in the examined deployments"* — `63` |
| Two schema generations are present (`iTEST02` has no `stock_valuation_layer`) | findings are not carried between them without saying so — `UNR-P03-11` |
| Whether any of these is the migration target | **`UNR-P03-10`**, Boss/programme — unchanged |

## 6. Reported to the Asset track

`Q-04` was framed against the **running** system. Four dumps are not that object.
**P03 does not close `Q-04`**; it supplies three complete installed-module lists as evidence
toward it, and the Asset register's status is quoted unchanged.
