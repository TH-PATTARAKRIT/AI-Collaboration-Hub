# P04 — EQUIPMENT WITHOUT AN ASSET

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P04-04`. Source basis series 18 / custom `18.0.x`.

---

## 1. The default case is equipment with no asset, and it is created by the warehouse

Module **`product_stock_equipment`** (installed, `18.0.1.0`; 11 copies of 3 distinct trees on
this host — the copy census was already published):

| Element | Evidence |
|---|---|
| Product flag | `product.template.equipment_ok` — *"Is Equipment"* |
| Forced product shape | `@api.onchange('equipment_ok')` sets `type='consu'`, `tracking='serial'` |
| Per-move opt-in | `stock.move.create_equipment` (Boolean), `product_equipment_ok` |
| **Trigger** | `stock.picking.button_validate()` → `create_equipment()` → `self.env['maintenance.equipment'].create(...)` |
| Defaults carried | `category_id`, maintenance team, technician, `equipment_assign_to` from the product template |
| Reverse view | `product.template.equipment_ids`, `equipment_count`, `action_view_equipment` |

> **`P04-F-150`. An operational equipment record is created by validating a goods receipt, and
> nothing in that path touches `account.asset`, a depreciation schedule, or any asset account.**
> The financial treatment of the receipt is whatever the product's stock/expense configuration
> already dictates. **Equipment existing without being a financial asset is not a gap in the
> estate — it is the default and the only automatic path.** `FACT VERIFIED`.

## 2. The asset side is manual, later, and one-way

There is **no** automatic creation of an `account.asset` from an equipment record, and none
from the receipt. The only connection is the manual `name_asset` link of `CQ-P04-03`, which a
user sets on the asset, and which becomes irreversible on validation (`P04-F-149`).

**Consequence for the Boss policy input** *"Equipment may exist without being a financial
Asset"*: **already true, already the default.** What the estate does **not** have is the
converse control — nothing prevents an equipment record from being expensed on receipt **and**
capitalised as an asset afterwards. **No check, anywhere, tests whether the value behind a
`name_asset` link was already expensed.** Stated as an absence with its denominator: the four
live model files of `equipment_sequence` and the four of `product_stock_equipment` contain no
such test; `account_asset` cannot contain one because it does not know the equipment exists.

> **`P04-F-151`. Double-counting between expensed equipment and a capitalised asset is
> unprevented by construction**, because the two sides are joined only by a field the user
> sets after both events have already been recorded. `FACT VERIFIED` as an absence;
> **frequency in the deployments is NOT measured** — it needs a per-identity query joining
> equipment to assets, which is a **runtime** question and is registered as `P04-B-53`
> rather than asserted.

## 3. Lifecycle, maintenance and cost tracking of a non-asset equipment record

| Capability | Present? | Evidence |
|---|---|---|
| Lifecycle states | `status` — `eqp` → `tass` only, one-way (`P04-F-149`) | custom |
| Maintenance requests / teams / technicians | **yes**, reference `maintenance` module | installed |
| **Cost** | **one `Float` field**, `maintenance.py:152 cost = fields.Float('Cost')` | reference |
| Any posting to the ledger | **none** — `0` references to `account.move` or `account.analytic` in the whole `maintenance` models directory | reference |
| Analytic tagging | **none** | reference |
| Link to production usage | **none** — see `CQ-P04-07` | P03 + P04 |

> **`P04-F-152`. Maintenance cost in the reference product is a statistical float. It reaches
> no journal, no analytic account and no cost object.** The `maintenance` models directory
> contains **zero** references to `account.move` or `account.analytic`. `FACT VERIFIED`,
> denominator: every `.py` in `addons/maintenance/models/`.

## 4. What this settles for the design

The Boss policy set requires *non-productive depreciation attributed to a named operational
cause* and *no unclassified depreciation*. §3 establishes that the **cause side has no
accounting representation at all** in the reference product: maintenance knows the cost, the
ledger never hears about it, and the two are not joinable.

> Therefore every mechanism in the Design Input Pack for non-productive attribution is a
> **`DESIGN CANDIDATE`**, not a configuration of existing behaviour. **P04 states only that the
> reference product provides no mechanism** — the same formulation P03 used for its half, and
> for the same reason.

## 5. Disposition

> **`CQ-P04-04` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`.**
> Non-asset equipment: **supported, automatic, warehouse-triggered**. Financial exclusion:
> **complete** — no path from equipment into asset accounting.
> New findings `P04-F-150`, `P04-F-151`, `P04-F-152`. One runtime measurement is registered,
> not guessed: `P04-B-53`.
