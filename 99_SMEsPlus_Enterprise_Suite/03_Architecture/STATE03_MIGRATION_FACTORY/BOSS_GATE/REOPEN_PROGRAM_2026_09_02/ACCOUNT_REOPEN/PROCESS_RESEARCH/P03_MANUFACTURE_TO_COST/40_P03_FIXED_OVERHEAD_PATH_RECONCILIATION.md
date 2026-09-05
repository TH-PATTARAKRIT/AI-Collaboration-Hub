# 40 — P03 FIXED OVERHEAD PATH RECONCILIATION

**LAYER 2 — AUDIT QUARANTINE.**

Revisited only where **material new evidence** arrived — from P04 (asset), P09 (analytic),
and this round's runtime evidence. Per the directive: no path is invented to satisfy a
target design.

---

## 1. Prior position

`02` §1: `CC-07` … `CC-14` — equipment depreciation, building depreciation, right-of-use
depreciation, planned maintenance, energy, indirect labour, fixed overhead generally —
**no injection path found**, bounded by `DEP-04`.

## 2. Reconciliation, element by element

| Element | Prior | New evidence | Classification now |
|---|---|---|---|
| **Equipment depreciation** | No path found | P04-F-49 + P09 + P03 verification: the analytic route **nets to zero**; no asset reference exists anywhere in the manufacturing modules | **NO PATH VERIFIED** — upgraded from *not found* to *the one candidate route is structurally incapable* |
| **Building depreciation** | No path found | same asset mechanism | **NO PATH VERIFIED** |
| **Right-of-use depreciation** | No path found | same | **NO PATH VERIFIED** |
| **Planned maintenance** | No path found | `mrp_maintenance` links equipment → **work centre**, never equipment → operation or → asset. It carries no cost | **NO PATH VERIFIED** |
| **Energy / utilities** | No path found | none | **NO PATH VERIFIED** |
| **Indirect labour** | No path found | `hr_hourly_cost` is installed in `BK12MAY26` but **not** in `iSMEs`; and it prices *direct* time logs, not indirect labour | **NO PATH VERIFIED** |
| **Fixed overhead as a pool** | No path, no denominator | none | **NO PATH VERIFIED** — no pool object exists to allocate |
| **The work-centre rate as a carrier** | Rejected by `ASSET_DR_CONTINUATION/07` §3 | Runtime: **0 work centres exist**, so the rejected carrier is also an empty one | **NO PATH VERIFIED**, and now moot in the live data |

## 3. The strengthening, and why it survives `DEP-04`

The prior conclusion was bounded: *no path found within the declared source scope, and the
installed-module list is unknown.*

Two of those bounds are now removed:

1. **The analytic route is structurally incapable, not merely unused.** The distribution
   sits on both equal-and-opposite legs of the depreciation entry, so the net is zero **by
   construction**. This does not depend on which modules are installed — `02` §5.
2. **The installed-module lists are now known** for two databases. Neither contains any
   module supplying an overhead path. `DEP-04` is `PARTIALLY CLOSED` — `26` §6.

> **`P03T-F-06`. Fixed production overhead has no path into inventory value, and the one
> route commonly assumed to carry it cannot carry it.** `FACT VERIFIED`, bounded to the
> declared source root and the three readable deployments.

## 4. The finding that supersedes this file's own subject

Fixed overhead was the prior rounds' gap. Runtime evidence makes it the *smaller* half:

> **Conversion cost is zero in its entirety** — machine, labour and overhead alike (`34`
> §2). A fixed-overhead absorption model would, if built today, allocate overhead onto a
> conversion-cost base that does not exist.

**This orders the remediation**, and the ordering is the useful output: a capacity
denominator and an absorption model (`R-05`, `R-14`) are premature until work centres,
routing operations, work orders and time capture exist at all. `ASSET_DR_CONTINUATION`
`BLK-07` — normal capacity vs actual hours — is a decision about a denominator whose
**numerator has no data source in any live deployment**.

**P03 does not reopen `BLK-07` and does not recommend on it.** It records that the
decision, whichever way Boss takes it, cannot be implemented against current data, and
reports that to the Asset register as `P03 → BLK-07` supporting evidence.

## 5. P04's third option — noted, not adopted

P04 reports that TAS 16 permits a **zero units-of-production charge when idle**, opening a
**third option** on `BLK-07` beyond normal-capacity and actual-hours.

**P03 records it and takes no position.** `BLK-07` is Asset-owned and Boss-decided;
P03 evaluating a third option would be exactly the cross-track adjudication
`smeplus-session-execution-pattern` forbids. Carried as `DEP-01` unchanged, with the third
option noted.
