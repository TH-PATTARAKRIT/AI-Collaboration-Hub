# P10 — CLASS C CROSS-PROCESS COMPARISON

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D16`.

---

## 1. What Class `C` Means Here

`C — NOT SEARCHED`. Not *absent*, not *agreed*, not *disputed*. **Nobody looked.**

The prior round recorded that P10's scope determinations had **not been compared line by line** with the peers' own scope matrices, classed the comparison `C`, and routed it to the cross-process process. **Routing a class `C` item does not discharge it** — it names who will look, not that anyone has.

## 2. What Was Class `C`, and What Can Now Be Compared

Peer packages have moved since the prior round: the asset process by ten commits, the analytic process by two, the cross-process process by twelve. Their scope matrices are therefore available at a later state than P10 read.

| # | Object | Was | Can P10 compare it now? | Action |
|---|--------|-----|-------------------------|--------|
| `CC-1` | Day-count convention **definitions** = PLATFORM | `C` | **No** — no peer has published a determination on convention definitions | **Preserved as `C`**; P10's determination stands unopposed, which is not the same as agreed |
| `CC-2` | Period-grid **algorithm** = PLATFORM | `C` | **No** — the ledger process's matrix does not address it | Preserved as `C` |
| `CC-3` | Recognition **event schema** = PLATFORM | `C` | **Partly** — the ledger process establishes no such object exists, which is consistent with P10 holding the schema, and the cross-process process names it Boss decision `D-5` | **Consistent, not compared.** The determination expires on `D-5` — `SX-01` |
| `CC-4` | Service **window** = TENANT | `C` | **No** | Preserved as `C` |
| `CC-5` | Fiscal calendar instance = COMPANY | `C` | **No** — the ledger process reports the ledger has **no period object**, which does not settle the scope of a calendar it does not have | Preserved as `C`, with the peer fact recorded beside it |
| `CC-6` | Recognition **attribution** scope | `C` | **YES — compared this round** | See §3 |
| `CC-7` | Recognition **event**, **base**, **posting act** = COMPANY | `C` | **No** | Preserved as `C` |

**One of seven has been compared. Six remain class `C`.**

## 3. The One Comparison Performed

`CC-6`. The analytic process has published a position: *a company-scoped attribution requirement shall never be enforced through a tenant-scoped structure*, and the finding that the structure carrying attribution **has no company field at all**.

P10's determination: the attribution requirement is COMPANY-scoped; the structure's scope is **undefined**; the requirement may not be enforced through it.

| Comparison | Result |
|------------|--------|
| Do the two determinations agree? | **Yes, and they were reached independently** |
| Do they use the same rule for an absent scope value? | **Yes** — an unset scope is undefined, not universal |
| Does either bind the other? | No. Both are positions, and P10 adopted the analytic process's as a design constraint |
| Class after comparison | **Agreed — but both are POSITIONS, not adopted boundaries.** Neither may be used to eliminate an option |

The last row is written explicitly because that is the error this round exists to repair. **Two processes agreeing is not adoption.**

## 4. Why the Remaining Six Cannot Be Closed by P10

A comparison needs two published determinations. For six of the seven, **no peer has published one** — the objects are P10's alone so far. P10 cannot compare its determination with silence, and must not read silence as agreement.

> **Class `C` is preserved for `CC-1`, `CC-2`, `CC-4`, `CC-5`, `CC-7`, and for the unexamined remainder of `CC-3`.** The dependency on the cross-process process (`PD-10`) is **exact**: it needs those peers to publish scope determinations for the same objects, and until they do the comparison is not deferred — it is **impossible**.

## 5. What P10 Asks the Cross-Process Process For

1. Determine whether any peer has published a scope determination on the six objects.
2. Where two exist, compare them and report agreement or contradiction.
3. Where only P10's exists, say so — an unopposed determination should be visibly unopposed, not silently ratified.
