# P03 — OPERATION → EQUIPMENT → COST CAUSALITY

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P03-06`. Within Manufacture-to-Cost only.
**The Asset domain is not redesigned here.**

---

## 1. What source proves

| Claim | Proven? | Evidence |
|---|---|---|
| Operation → **Work Centre** | **YES** | the routing-operation model carries a work-centre reference |
| Operation → **specific Equipment** | **NO** | the routing-operation model declares **no equipment field**; verified in series 18, and P04 verified the same independently |
| Equipment → Work Centre | **YES** | a maintenance-bridge link, `mrp_maintenance` |
| Equipment → Asset | **NO** | **no reference in either direction** |
| Time log → machine | **NO** | every measurement resolves to a **work centre**; the machine dimension exists nowhere in the measurement chain |

> The chain is `asset ✗ equipment → work centre ← operation`, **broken on the asset side and
> broken again immediately after.** Verified with `mrp_maintenance` **installed**, which
> removes the "the module was missing" objection.

## 2. Can work-centre membership establish actual machine usage?

> **No.** Membership is a *configuration* fact; usage is an *event* fact, and no event
> records a machine.

Worse, and measured: machine cost is charged as a function of **human time logs**. A machine
running unattended generates no log and therefore no cost; two operators at one machine
generate two logs and, under `DC-01`'s raw-sum base, two machine-hours.

> **Machine cost in the reference product is not causally connected to machine use.**
> `FACT VERIFIED`.

## 3. Evidence boundary for equipment usage cost entering MO/WIP/FG

**There is none.** No equipment cost enters an MO, WIP or FG in any examined deployment:

| Gate | Result |
|---|---|
| A path from equipment or asset into manufacturing cost | **none in source** |
| The one vehicle that could carry it — the work-centre rate | **rejected** by `ASSET_DR_CONTINUATION/07` §3, and enabled on **1 of 60** work centres |
| Deployments where any machine cost reached finished goods | **0 of 4** |

## 4. Boss-approved policy inputs — carried, not converted

Carried as **policy**, explicitly **not** as benchmark facts, and not evaluated:

- productive depreciation allocation → WIP/FG;
- non-productive depreciation → a named operational cause;
- **no unclassified depreciation**;
- continuous post-depreciation internal usage has **no residual cap**;
- financial depreciation ≠ managerial / internal usage allocation;
- **work-centre membership alone ≠ cost absorption** — §2 is the evidence that the reference
  product cannot satisfy this even if asked;
- off-balance tracking must not be cross-posted as financial WIP.

**P03 states only that the reference product provides no mechanism for any of them.** Whether
SMEsPlus builds one, and on which denominator, is `BLK-07` — **Boss, Asset-owned, untouched.**

## 5. Disposition

> **`CQ-P03-06` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`.**
> Operation → work centre: proven. Operation → equipment: **proven absent**.
> Equipment usage cost into MO/WIP/FG: **no path, no evidence, in four deployments**.
> The design question is **`BOSS DECISION REQUIRED`** on the Asset register, not here.
