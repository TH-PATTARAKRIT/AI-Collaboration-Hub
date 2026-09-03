# 36 — COST LINEAGE MATRIX
**LAYER 2 — AUDIT QUARANTINE**

Required matrix N (§82), §52. Each link classified as
`SOURCE VERIFIED` · `SOURCE CUSTOM` · `SMEsPlus DESIGN` · `UNRESOLVED`.

## 1. The chain the prompt asks about

```
Asset → Equipment → Production context → Work Center → Operation → Routing
      → MO → WIP → FG → COGS
```

| # | Link | Exists | Mechanism | Classification |
|---|---|---|---|---|
| L1 | **Asset → Equipment** | **Custom** | A manual `Many2one`, no inverse, no uniqueness, **three of four behaviours inert** | **`SOURCE CUSTOM`** — and defective, `19` |
| L2 | **Asset → cost pool** | **No** | Depreciation is posted to the GL and stops there | **`SMEsPlus DESIGN`** |
| L3 | **Equipment → production context** | Partial | Equipment names a work centre. There is no "production equipment" concept | `SOURCE VERIFIED` (the link) / `SMEsPlus DESIGN` (the context) |
| L4 | **Equipment → cost** | **No** | One inert float on the equipment record | **`SMEsPlus DESIGN`** |
| L5 | Work centre → hourly rate | Yes | **A manually entered float, default 0.00** | `SOURCE VERIFIED` |
| L6 | **Operation → Equipment** | **NO** | An operation names a work centre only | **`SMEsPlus DESIGN` — the structural gap** |
| L7 | Operation → Work centre | Yes | Required field | `SOURCE VERIFIED` |
| L8 | Routing → Operation | Yes | The bill-of-materials operation list | `SOURCE VERIFIED` |
| L9 | Operation → Work order | Yes | Generated per manufacturing order | `SOURCE VERIFIED` |
| L10 | Work order → cost | Yes | `duration ÷ 60 × rate`, **rate snapshotted at creation** | `SOURCE VERIFIED` |
| L11 | Work order → analytic | Yes | Lines from the work centre's distribution, updated on duration change | `SOURCE VERIFIED` |
| L12 | Work order cost → WIP/FG value | Yes | Σ work-order cost + extra unit cost − consumed value → finished move unit price → valuation layer | `SOURCE VERIFIED` |
| L13 | Work-centre cost → GL | Yes | Credit the work centre's expense account, debit stock valuation — **real-time valuation only** | `SOURCE VERIFIED`, conditional |
| L14 | FG → COGS | Yes | Ordinary stock valuation | `SOURCE VERIFIED` |
| L15 | **Maintenance → any cost** | **NO** | No monetary field exists anywhere in maintenance | **`SMEsPlus DESIGN`** |
| L16 | **Idle / downtime → cost** | **NO** | Not recorded | **`SMEsPlus DESIGN`** |
| L17 | **Absorption variance** | **NO** | Nothing computes absorbed versus actual | **`SMEsPlus DESIGN`** — `GAP-ABS-VAR` |
| L18 | **Post-depreciation internal usage** | **NO** | No concept | **`SMEsPlus DESIGN`** |
| L19 | Thai admissibility of depreciation absorbed into inventory | — | — | **`UNRESOLVED`** — `UNR-03` |

## 2. The picture in one line

> **L5 through L14 are built. L1 is built badly. L2, L4, L6, L15–L18 are not built
> at all. L19 is unknown.**

Ten of nineteen links exist and work. That is a far better starting position than
"no mechanism exists", which is where the prior session's evidence left it.

## 3. The two links that gate everything else

**L6 — Operation → Equipment.** Without it there is no measurement of which machine
did which job, so the machine-hour driver has no input. Every allocation must
average across the work centre.

**L1 — Asset → Equipment.** Without a reliable version of it there is no way to
attribute a depreciation figure to a machine at all. Today it is optional,
duplicable, editable on closed assets, and its disposal behaviour does not run.

Neither is interesting work. Both are prerequisites for all the interesting work.

## 4. Defects that will be inherited if L5–L14 are reused as-is

| # | Defect | Consequence for a depreciation-derived rate |
|---|---|---|
| 1 | **Cost is recognised when the order completes**, not when the machine ran (`FAIL-P09`) | A monthly pool lands in the completion month. Orders spanning a month end are misstated |
| 2 | **The rate is snapshotted onto the work order at creation** | A rate derived at month end does not apply to work orders already open |
| 3 | **L13 is conditional on real-time valuation** | For periodic-valued products the cost reaches the unit price and never reaches the ledger |
| 4 | **No absorption variance** | Under-utilisation silently disappears instead of becoming a period cost |

All four are **existing defects in the reference chain**, not new risks introduced
by the SMEsPlus design. They are listed here so that the design addresses them
deliberately rather than inheriting them silently.

## 5. Classification summary

| Classification | Links |
|---|---|
| `SOURCE VERIFIED` | 10 |
| `SOURCE CUSTOM` | 1 — and defective |
| `SMEsPlus DESIGN` | 7 |
| `UNRESOLVED` | 1 |
