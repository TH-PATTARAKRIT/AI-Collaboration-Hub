# 08 — DEEP LEVEL 4: CROSS-MODULE MATRIX
**LAYER 2 — AUDIT QUARANTINE**

Method required by §40: **not** foreign-key-first. The graph below was built from
module dependencies, model definitions, field definitions, method call chains and
runtime evidence, in that order.

## 1. The decisive measurement

Exhaustive search of the reference ERP v18 Enterprise addons tree — **797
modules** — for any reference to the asset model:

| Module referencing the asset model | Relationship |
|---|---|
| the asset module itself | owner |
| a loans module | unrelated finance feature |
| a project-accounting module | unrelated feature |

**Three. And zero from maintenance, equipment, manufacturing, work centres,
operations, routing, stock, product or purchase.**

This is not "we could not find a link". It is an exhaustive negative over the
whole product. `FACT VERIFIED`

The asset domain's cross-module surface, natively, consists of exactly two edges:
**vendor bill → asset** and **asset → journal entry**.

## 2. Module relationship matrix

`N` native · `C` custom (project) · `—` verified absent

| From ↓ / To → | Asset | Equipment | Maintenance | Work Center | Operation | MO / WO | Stock | Product | Bill | GL | Analytic |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Asset** | self-tree `N` | **`C`** | — | — | — | — | — | — | `N` (source) | `N` | `N` |
| **Equipment** | — | | `N` | **`N`** | — | — | `C` | `C` | — | — | — |
| **Maintenance** | — | `N` | | `N` | — | `N` (reference only) | — | — | — | — | — |
| **Work Center** | — | `N` (inverse) | `N` | | `N` (inverse) | `N` | — | — | — | `N` | `N` |
| **Operation** | — | **—** | — | `N` | | `N` | — | — | — | — | — |
| **MO / WO** | — | — | `N` | `N` | `N` | | `N` | `N` | — | `N` | `N` |
| **Bill** | `N` | — | — | — | — | — | — | `N` | | `N` | `N` |

The two cells that decide the whole SMEsPlus question are marked in bold:

- **Asset → Equipment** exists, and only because this project built it.
- **Operation → Equipment** does **not** exist, natively or custom.

## 3. The structural gap, stated precisely — §44

```
        Operation ──────────► Work Center ◄────────── Equipment
                                                          │
                                                          │  (custom, project-built)
                                                          ▼
                                                        Asset
```

An Operation names a **Work Center**. Equipment names a **Work Center**. A Work
Center holds **many** Equipment. Therefore:

> **There is no path from a job to the specific machine that performed it.**

The Boss's "toll gate" requirement — *whoever uses the machine receives that
machine's cost; whoever does not, does not* — cannot be satisfied on this model.
Any allocation built on it necessarily spreads a work centre's cost across every
job that passed through the work centre, regardless of which of its machines was
actually used.

`VERIFIED SOURCE GAP`. The Boss's concern is not a misunderstanding of the source;
it is an accurate reading of a real structural limitation, and `Operation →
Equipment` is a legitimate SMEsPlus extension candidate.

## 4. Product → Equipment → Asset — the actual routes, §42

The prompt warned against assuming one universal path. Correct warning; there are
three, and they do not join up.

| Route | Exists | Mechanism |
|---|---|---|
| Product → Equipment | **`C`** | A custom module creates equipment records from stock/inventory events, keyed on serial number, driven by a flag on the product template |
| Vendor bill → Asset | **`N`** | The only native capitalisation route |
| Equipment → Asset | **`C`, one direction only** | A custom `Many2one` **from the asset**, chosen manually by the accountant |
| Product → Asset | — | none |
| Purchase order → Asset | — | none |
| Goods receipt → Asset | — | none |

The consequence is worth stating plainly:

> Buying a machine produces **two independent records created by two different
> people from two different documents**: an Equipment record from the warehouse
> receipt, and an Asset record from the vendor bill. **Nothing joins them
> automatically.** The join is a manual dropdown, chosen by an accountant, on the
> asset form, with no inverse and no uniqueness constraint.

That is the real state of Asset↔Equipment integration on this project.
`FACT VERIFIED` — see `19`.

## 5. Maintenance — §43 answered

What maintenance contributes: request tracking, corrective vs preventive
classification, stages, teams, technicians, scheduling, recurrence, MTBF and MTTR,
and — through the manufacturing bridge — **blocking work-centre capacity** by
writing unavailability onto the resource calendar.

What maintenance contributes to **cost**: **nothing.**

| Looked for | Found |
|---|---|
| Cost field on a maintenance request | **None** |
| Currency field on a maintenance request | **None** |
| Spare-part consumption linked to a request | **None** |
| Labour cost or rate on a request | **None** (duration in hours only) |
| Any account or analytic on a request | **None** |
| Cost field on equipment | **One plain float, `Cost`** — no currency, no account, no analytic, no journal |
| Downtime → cost | **None** |

`FACT VERIFIED` — field enumeration of the maintenance models.

This is stronger than the previous session's finding that maintenance cost does
not flow to production. **There is no maintenance cost figure in the system at
all.** Maintenance's only production effect is on **capacity**, never on cost.

Classification: **`VERIFIED SOURCE GAP`**, and a clean SMEsPlus differentiator.

## 6. The production cost chain — what actually exists

This is the correction that most changes the SMEsPlus opportunity. Traced end to
end in primary source:

| # | Link | Mechanism | Status |
|---|---|---|---|
| 1 | Work Center → hourly rate | A **manually entered float**, default 0.00 | `N` — **and this is the weak link** |
| 2 | Hourly rate → Work Order cost | `duration ÷ 60 × rate`; the rate is **snapshotted onto the work order** when it is created | `N` |
| 3 | Work Order cost → analytic | Analytic lines written from the work centre's own distribution, tagged as manufacturing-order category, updated whenever duration changes | `N` |
| 4 | Work Order cost → finished goods valuation | Σ work-order costs + extra unit cost + consumed material value → the finished move's unit price → stock valuation layer | `N` |
| 5 | Work-centre cost → GL | On completion, a "Labour" entry credits the work centre's expense account (or the product's) and debits stock valuation | `N` — only when the product is real-time valued |
| 6 | FG valuation → COGS | Ordinary stock valuation | `N` |
| 7 | **Depreciation → the hourly rate in link 1** | **nothing** | **`VERIFIED GAP`** |
| 8 | **Equipment → any of links 1–6** | **nothing** | **`VERIFIED GAP`** |

**Links 2 through 6 exist and work. Only links 7 and 8 are missing.**

The previous session's conclusion — "no documented mechanism connects asset
depreciation to work centre / MO / product cost" — is `CONFIRMED AGAIN` and made
precise: the *absorption machinery* is complete; the *cost pool derivation* and the
*equipment dimension* are what is absent.

For SMEsPlus this reframes the work from "build production costing" to "**derive
the rate that production costing already consumes, per machine**". See `27`.

## 7. Data ownership and source-of-truth matrix — §41

| Data object | Business owner | Model owner | **Source of truth** | Consumers |
|---|---|---|---|---|
| Original asset value | Accounting | asset | **the vendor bill line balances** | asset, reports |
| Accumulated depreciation | Accounting | — | **the posted journal entries** | book value, reports |
| Book value | Accounting | asset (stored) | **derived: entries + salvage + child tree** | reports, disposal |
| Not-depreciable value | Accounting | asset | the asset row | base, disposal |
| Depreciation amount per period | Accounting | journal entry | **the journal entry** | GL, analytic |
| Asset analytic distribution | Controlling | asset | the asset row (seeded from the bill) | future entries only |
| Equipment identity | Operations | equipment | the equipment row | maintenance, work centre |
| Equipment ↔ Asset association | **disputed** | asset (custom field) | the asset row, manually set | nothing consumes it |
| Equipment operational status | Operations | equipment | the equipment row — **and it is mutated by the asset confirm** | maintenance |
| Work centre hourly rate | **Controlling — manually** | work centre | the work centre row | work orders, MO cost |
| Work order cost | Controlling | work order | `duration × snapshotted rate` | valuation, analytic, GL |
| Machine usage / downtime | Operations | productivity records | those records | capacity only |
| FG cost | Costing | stock valuation layer | the valuation layer | COGS |

Two rows deserve attention:

- **Equipment ↔ Asset association is owned by nothing.** It is set on the asset by
  an accountant and consumed by no function except a status flip. It is a label.
- **Work centre hourly rate is owned by a human.** Its correctness is a manual
  control. Nothing derives it, validates it, or reconciles it to actual cost.
  That is exactly the space SMEsPlus is proposing to occupy.

## 8. Event-to-GL matrix

See `34_EVENT_TO_GL_MATRIX.md`.

## 9. Cost lineage

See `36_COST_LINEAGE_MATRIX.md`.

## 10. Four Expert opinions

See `09_LEVEL4_FOUR_EXPERT_OPINIONS.md`.
