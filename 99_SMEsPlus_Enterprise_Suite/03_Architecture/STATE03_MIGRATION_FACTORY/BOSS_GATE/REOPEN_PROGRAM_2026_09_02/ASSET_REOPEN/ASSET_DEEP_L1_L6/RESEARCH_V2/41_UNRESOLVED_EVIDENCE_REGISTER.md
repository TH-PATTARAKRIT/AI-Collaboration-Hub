# 41 — UNRESOLVED EVIDENCE REGISTER
**LAYER 2 — AUDIT QUARANTINE**

Every open item, with **why it is unknown**, **what evidence would close it**,
**business and design impact**, and **whether it blocks final Asset design** (§99).

Items are ordered by priority, not by number.

---

## Tier 1 — Blocking, and answerable quickly

### `UNR-02` — Which computation mode are the 217 running assets using? **[BLOCKING]**

| | |
|---|---|
| **Why unknown** | The runtime read-out captured state, company, template link, accounts, duration and values — but **not the prorata computation mode**. The Asset Model export shows a method label with no v18 implementation found in this workspace, and its provenance (v14 or v18) is not established |
| **Evidence required** | On the UAT: the distribution of `prorata_computation_type` across the 280 assets; and the origin of the Asset Model export |
| **How to get it** | One grouped read over the asset model, same mechanism as the read-out already captured on 2026-08-26 |
| **Business impact** | **High.** If the assets are on the 30/360 default, every February is overstated by 8% and every 31-day month understated by 1.9%, permanently. Annual totals differ by only 0.05%, so no annual check will find it |
| **Design impact** | Determines whether SMEsPlus must build a Thai method or select a configuration |
| **Blocks final design?** | **YES** |
| Related | `CTR-01`, `BA-01`, `16` §3.4, `17` |

### `UNR-08` — How many assets share an equipment link? **[BLOCKING for costing]**

| | |
|---|---|
| **Why unknown** | The custom link has no uniqueness constraint and no inverse; nothing reports duplicates. Raised by Expert 2 at Levels 2, 4 and 6 |
| **Evidence required** | Counts on the UAT: assets with the link populated; equipment records referenced more than once; parent/child assets among the 280 |
| **Business impact** | **High if any duplicates exist** — a duplicated machine's cost pool doubles |
| **Design impact** | Uniqueness is a **correctness precondition** for per-machine costing, not data hygiene |
| **Blocks final design?** | **YES for the costing design.** No for the depreciation design |
| Related | `19` §4, `36` §3 |

### `UNR-09` — Is the confirm path guarded by the lock date?

| | |
|---|---|
| **Why unknown** | The asset module's disposal and modify paths check the fiscal lock date. Confirm and pause do not. Whether the underlying posting layer catches it is not determinable from this module |
| **Evidence required** | Confirm an asset with a past acquisition date into a locked period on the UAT |
| **Business impact** | **High if unguarded** — confirm posts an asset's entire life at once, so a single action could post into a closed period |
| **Design impact** | SMEsPlus must guard it explicitly regardless |
| **Blocks final design?** | No — the design decision is the same either way |
| Note | Expert 3 rates this High; Expert 4 declines to rate an untested path (`D3-01`). Both positions preserved |

---

## Tier 2 — Blocking, and requiring an authority decision

### `UNR-03` — Does Thai practice permit depreciation to be absorbed into inventory value? **[BLOCKING]**

| | |
|---|---|
| **Why unknown** | Not a software question. Raised by Expert 3 at Level 4, still unanswered at Level 6 |
| **Evidence required** | Thai accounting/tax authority position on absorbing depreciation into inventory cost, and any timing difference it creates for tax |
| **Business impact** | **Precondition for the entire SMEsPlus costing proposition** |
| **Blocks final design?** | **YES** |
| **Owner** | Accounting-Tax track. `HOLD / EVIDENCE REQUIRED` |

### `UNR-B3` / `UNR-27` — May off-balance internal usage accumulate without bound? **[BLOCKING]**

| | |
|---|---|
| **Why unknown** | No precedent in the reference system or in any standard consulted. Expert 2 objects that an unbounded accumulator with no terminating rule is a design defect; Expert 1 holds that the bound is a policy choice (`D5-01`) |
| **Evidence required** | **A Boss policy decision**, plus the Accounting-Tax track's view |
| **Business impact** | Determines whether lifetime economic contribution is a durable measure or an ever-growing number |
| **Blocks final design?** | **YES for the management ledger** |
| **Owner** | Boss |

### `UNR-23` — How are off-balance accounts treated in Thai statutory financial statements? **[BLOCKING]**

| | |
|---|---|
| **Why unknown** | Never established. The management-ledger design rests on it |
| **Evidence required** | Thai statutory reporting treatment of that account classification |
| **Blocks final design?** | **YES for the management ledger** |
| **Owner** | Accounting-Tax track. `HOLD / EVIDENCE REQUIRED` |

### `UNR-01` — Is the Thai pro-ration unit legally the day?

| | |
|---|---|
| **Why unknown** | Primary text says *period* (`ระยะเวลา`), not *days* (`จำนวนวัน`) |
| **Evidence required** | A Revenue Department ruling or departmental instruction |
| **Business impact** | Determines whether the 30/360 default is merely inaccurate or non-compliant |
| **Blocks final design?** | **No** — the daily basis is the conservative choice either way |
| **Owner** | Accounting-Tax track. `HOLD / EVIDENCE REQUIRED` |

---

## Tier 3 — Non-blocking, evidence-gathering

| ID | Item | Why unknown | Impact | Blocks? |
|---|---|---|---|---|
| `UNR-04` | UAT installed-module list | Never obtained. **Caps every negative finding in this package** | Medium | No |
| `UNR-05` | UAT build identity vs the workspace source | Never verified. Underpins the whole method | Medium | No |
| `UNR-06` | Parent/child relationships among the 280 assets | Not captured | Low | No |
| `UNR-07` | Are the 35 account-less assets the same 35 in draft? | The read-out grouped state and accounts separately | Low | No |
| `UNR-10` | Transactional boundaries of the multi-step modify operation | Not determinable statically | Medium | No |
| `UNR-11` | Assets whose analytic differs from their own posted entries | Nothing reports it | Medium | No |
| `UNR-12` | Multi-company asset behaviour | Untouched | Low | No |
| `UNR-13` | Which custom behaviours actually execute | Three found inert; there may be more | **Medium-High** | No |
| `UNR-14` | Absorption variance — does any mechanism exist elsewhere? | Searched in the asset and manufacturing paths only | Medium | No |
| `UNR-15` | Are work-centre hourly rates set at all on the UAT? | Not captured. Default is 0.00 | **Medium** — if unset, no machine cost is in FG today | No |
| `UNR-16` | Runtime event trace | Not captured | Low | No |
| `UNR-17` | Are off-balance accounts permitted in the work-centre / valuation path? | Only the asset side was checked | Medium | No |
| `UNR-18` | Where does unabsorbed depreciation go? | **Boss policy**, not a research finding | Medium | No |
| `UNR-19` | Is the simplified internal rate (residual ÷ original lifetime days) what the Boss intends? | Design question | Medium | No |
| `UNR-20` | TFAC primary texts on property, plant and equipment | Not obtained | Medium | No |
| `UNR-21` | Does Thai tax permit suspending depreciation on an owned asset? | Bears on the pause function | Medium | No |
| `UNR-22` | Statutory standing of the 1-baht residual convention | Not researched | Low | No |
| `UNR-24` | Correct grain for a per-machine rate | Open design decision | Medium | No |
| `UNR-25` | Board-invariant violations from migration | Constraint is ORM-only | Medium | No |
| `UNR-26` | Import-field usage across the 280 | The sanctioned way to break sub-ledger/GL agreement | **Medium-High** | No |

---

## The six items the experts added that the Boss's hypotheses do not yet cover

Carried from `11`. None invalidates the design; each is a hole that would otherwise
surface during build.

| # | Item | Raised by |
|---|---|---|
| 1 | Re-entry: a fully depreciated asset receiving a capital improvement | Expert 1 |
| 2 | A terminating rule for cumulative internal usage | Expert 2 |
| 3 | The disposal path for the management ledger, once the residual is absorbed | Expert 3 |
| 4 | Rate snapshotting on work orders spanning a month end | Expert 4 |
| 5 | Volume and granularity of per-machine, per-operation cost records | Expert 4 |
| 6 | Where unabsorbed depreciation goes | AAS+ |

---

## Summary

| | Count |
|---|---|
| **Blocking final Asset design** | **6** — `UNR-02`, `UNR-08`, `UNR-03`, `UNR-B3`, `UNR-23`, and the design decision behind item 2 above |
| Non-blocking, evidence-gathering | 21 |
| Design holes surfaced for the Boss | 6 |
| **Answerable in one UAT session** | **9** — `UNR-02`, `UNR-04`, `UNR-05`, `UNR-06`, `UNR-07`, `UNR-08`, `UNR-11`, `UNR-15`, `UNR-26` |

**Of the six blockers, four require an authority decision** (Boss or Accounting-Tax)
and cannot be researched. **Two require access to the running UAT** and would take
minutes.

The prior session's register carried 29 items, four blocking, mostly for want of
implementation-level mechanism detail. Those are now resolved from source. The
remaining items are of a different kind: they need the **running system** or an
**authority ruling**, not more analysis. That is the boundary of what this method
can reach.
