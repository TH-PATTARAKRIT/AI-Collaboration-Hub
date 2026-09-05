# 34 — P03 ZEROING vs DOUBLE-COUNTING MATRIX

**LAYER 2 — AUDIT QUARANTINE.**

Two opposite defects, tested against every cost type. A package that only hunts
double-counting will miss the larger failure, which in this system is **zeroing**.

- **Failure A — ZEROING.** A real economic cost exists and reaches nothing.
- **Failure B — DOUBLE COUNTING.** One economic cost enters a ledger more than once.

---

## 1. The matrix

Amounts are per the `iSMEs` deployment. "Live" means the mechanism executes there.

| Cost type | Economic source | Management attribution | WIP injection | FG carrying cost | COGS | Failure |
|---|---|---|---|---|---|---|
| **Direct material** | Purchase / valuation layer | via move distribution | **Yes** | **Yes** | via FG | **None** — the one sound path |
| **Machine / work centre** | Machine occupancy | none — 0 work centres | **0** | **0** | **0** | **A — ZEROING, total** |
| **Direct labour** | Employee time | none — module not installed | **0** | **0** | **0** | **A — ZEROING, total** |
| **Equipment depreciation** | Asset depreciation, posted | **2 lines netting to 0** | **0** | **0** | **0** | **A — ZEROING, twice over** |
| **Planned maintenance** | Maintenance cost | none | **0** | **0** | **0** | **A — ZEROING** |
| **Energy / utilities** | Supplier bill | none | **0** | **0** | **0** | **A — ZEROING** |
| **Indirect labour** | Payroll | none | **0** | **0** | **0** | **A — ZEROING** |
| **Fixed overhead** | various | none — no pool exists | **0** | **0** | **0** | **A — ZEROING** |
| **Extra unit cost** | Manual / subcontract | none | Yes, if set | Yes, if set | via FG | **B latent** (`DC-03`) — 0 of 10,764 rows |
| **Subcontract service** | Vendor bill | none | Yes | Yes | via FG | none — module not installed |
| **Scrap** | Inventory loss | via move | No | No | No | **A** — no normal-loss absorption |
| **By-product** | Cost share | none | negative | negative | via FG | none |

## 2. The result, stated plainly

> **`P03T-F-05`. Every conversion-cost element in the manufacturing chain exhibits Failure
> A. Not one exhibits Failure B in live data.**

Eight cost types reach inventory value at zero. The double-counting defects this package
spent two rounds establishing — `DC-01`, `DC-03`, `DC-04`, `DC-07`, `DC-14` — are all
**latent**: real in code, unreachable in the deployments that exist.

**This inverts the practical priority of the whole P03 package** and must be stated in
those terms rather than buried:

| | Prior rounds' emphasis | After runtime evidence |
|---|---|---|
| Dominant risk | Double counting into WIP | **Zeroing — conversion cost never enters inventory at all** |
| `DC-01` | Headline, Critical | Real, verified, **latent** |
| Fixed overhead absence | One finding among many | **The whole of conversion cost, not just its fixed part** |

## 3. Why both attacks were still required

Running only the double-counting attack would have produced a technically correct package
that missed the larger defect. Running only the zeroing attack would have declared the
system safe — no duplication is observable — while leaving `DC-01` undetected against the
day a work centre is created.

**The two failures are not alternatives.** A system can zero a cost today and double it
tomorrow through the same unconfigured mechanism, which is exactly this system's position.

## 4. The one cost that is neither zeroed nor doubled

Direct material. It flows: purchase → valuation layer → component issue → production
account → finished-goods valuation. `15` §4 already recorded that P03 consumes the
valuation-layer value without re-deriving it, and called it *the one structural thing in
the reference manufacturing cost model that this session found unambiguously right*.

Runtime evidence confirms it: 74,982 valuation layers against 103,949 stock moves, and
9,807 completed orders carrying material cost.

## 5. TAS 2 consequence — routed, not adjudicated

`ASSET_DR_CONTINUATION/12` §3 classifies direct labour and variable production overhead as
**conversion cost that TAS 2 ¶12 requires in inventory**.

> Inventory in `iSMEs` is carried at **material cost only**. This is not the *fixed*-overhead
> gap the prior rounds identified. It is the absence of **conversion cost entirely.**

`ASSET_DR_CONTINUATION` `UNR-C-03` asks how a standard-costed product complies with TAS 2.
P03 supplies a harder instance: how does an **actual-costed** product comply when its
conversion cost is structurally zero? **Routed to the Asset register and to P11. Not
closed here** — it is a statutory question and P03 makes no statutory claim.
