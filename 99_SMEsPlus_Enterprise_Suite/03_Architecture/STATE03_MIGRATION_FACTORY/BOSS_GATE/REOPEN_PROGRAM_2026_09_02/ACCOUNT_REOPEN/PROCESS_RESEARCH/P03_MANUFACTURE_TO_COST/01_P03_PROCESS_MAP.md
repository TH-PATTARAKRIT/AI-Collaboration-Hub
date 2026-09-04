# 01 — P03 PROCESS MAP

**LAYER 2 — AUDIT QUARANTINE.**

Session `SMEPLUS-26-09-04-ACC-P03-M2C-REV2-001`.

---

## 1. The chain, and the single question asked of every link

The mandated chain:

```
Demand → BOM → Routing → Operation → Work Order → Raw Material Issue → WIP
      → Labour / Service / Equipment / Overhead → Semi-Finished → Finished Goods
      → Inventory Valuation → Delivery → COGS
```

At every link this session asked one question and only one:

> **Does an economic cost enter WIP here, and if so, through how many paths?**

## 2. Link-by-link

| # | Link | Cost enters? | Path | Class |
|---|---|---|---|---|
| 1 | **Demand** (forecast, reorder, sales-driven) | No | — | `FACT VERIFIED` |
| 2 | **BOM** | No — planning only | BOM drives a *standard* via `_compute_bom_price`; it is a price-setting action on the product master, not a posting | `FACT VERIFIED` |
| 3 | **Routing / Operation** | No | Carries the expected duration and the link to the work centre | `FACT VERIFIED` |
| 4 | **Work Order** | **Yes — the only labour/machine entry point** | `_cal_cost()` | `FACT VERIFIED` |
| 5 | **Raw Material Issue** | **Yes** | Raw stock moves → valuation layers → aggregated at `_post_inventory` | `FACT VERIFIED` |
| 6 | **WIP** | Is the destination, not a source | Two unreconciled account families — see `03` §3 | `FACT VERIFIED` |
| 7 | **Labour** | Yes | Inside `_cal_cost()`, from employee time logs | `FACT VERIFIED` |
| 8 | **Service / Subcontract** | Yes | `extra_cost`, set from the subcontract receipt | `FACT VERIFIED` |
| 9 | **Equipment / Depreciation** | **No systematic path exists** | See `04` — this is the P03 headline gap | `FACT VERIFIED` (scope declared) |
| 10 | **Overhead** | Only as whatever a human folded into the work-centre hourly rate | No overhead object, no absorption base, no capacity denominator | `FACT VERIFIED` |
| 11 | **Semi-Finished** | Inherits, via a child MO or a nested BOM | Recursive; each level repeats links 4–10 | `FACT VERIFIED` |
| 12 | **Finished Goods** | Receives | `_cal_price()` writes the finished move's unit price | `FACT VERIFIED` |
| 13 | **Inventory Valuation** | Owned by the Inventory track, not P03 | Cross-reference only | `FACT VERIFIED` |
| 14 | **Delivery → COGS** | Owned by P02 / COGS track | COGS is terminal HOLD; P03 does not resolve it | `FACT VERIFIED` |

## 3. The two cost injection points, stated precisely

**Declared unit — added after P04 peer review; see `25` §2.**

> **POPULATION:** the module set of `02` §3. **PATTERN:** any function that writes a value
> reaching inventory carrying value. **PATH SET:** the declared source root.
> **UNIT: one writer that changes the carrying value of inventory.**

The original text of this section asserted "exactly two writers" **with no declared unit**,
which is the defect `smeplus-denominator-completeness-rule` names. Under the unit now
declared the count is two. Under P04's broader disjunctive unit — own rate field **or** own
driver **or** own destination ledger — the count is **nine**, correctly including the
analytic and planning paths this section excludes. Both are right under their own unit;
neither supersedes the other. See `25` §2.

Under the unit declared here, the chain reduces to exactly two writers:

### Injection point 1 — `_cal_price()`
`mrp_account/models/mrp_production.py:40-65 — MrpProduction._cal_price`

```
total_cost = -Σ(consumed valuation layers) + work_center_cost + extra_cost
finished_move.price_unit = total_cost × (1 - byproduct_share) ÷ quantity
```

This is what makes finished goods *worth* something. It runs inside `_post_inventory`.

### Injection point 2 — `_post_labour()`
`mrp_account/models/mrp_production.py:72-106 — MrpProduction._post_labour`

This is the **absorption** entry that stops injection point 1 from creating value out of
nothing: it debits the production account and credits an expense account for the same
work-centre cost that `_cal_price` capitalised.

**The design intent is sound: capitalise, then relieve.** Every material finding in `05`
is a failure of the *pairing* between these two, not of either idea.

## 4. Where the pairing breaks — index into `05`

| Break | `_cal_price` does | `_post_labour` does | Result |
|---|---|---|---|
| `extra_cost` | Capitalises it | **Ignores it** | Permanent residue |
| Standard-cost product | **Skips capitalisation** | Still posts | Permanent residue, opposite sign |
| Duration basis | Uses `_cal_cost` raw sum | Uses `_cal_cost` raw sum | Consistent with each other, **inconsistent with the displayed duration** |
| Analytic mirror | Not involved | Not involved | A third, different number |

## 5. Process states researched

The directive requires all of: create / confirm / partial / cancel / reverse / return /
correct / backdate / close. Coverage and result:

| State | Covered in | Result |
|---|---|---|
| create / confirm | `09` §2 | No cost effect until work orders log time |
| **partial completion** | `09` §5 | Backorder splits carry `extra_cost` forward — `_get_backorder_mo_vals` copies it; **quantity-proportionality of expected duration verified, no double count found on the split path itself** |
| **cancel** | `09` §6 | Work-order analytic lines are unlinked; **the financial labour entry has no cancellation path because it is only posted at `done`** |
| **reverse (unbuild)** | `11` §4 | Releases FG at the **first** valuation layer's unit cost, not the layer actually consumed |
| return | `12` §3 | Production returns are not a manufacturing object; they resolve to the Inventory track |
| correct | `10` §5 | No cost correction object exists in the declared scope |
| **backdate** | `08` `AE-03` | The labour entry takes **today's** date, not the MO's |
| close | `13` §4 | Period close depends on the WIP wizard, which reverses itself the next day |

## 6. What P03 found is missing from the target side

`END_TO_END_BUSINESS_PROCESS_MATRIX.md` v0.1 enumerates `E2E-001` … `E2E-010`.

- **POPULATION:** all 10 declared end-to-end processes.
- **PATTERN:** any process whose Start Module or Related Modules include manufacturing,
  production, work order, BOM or routing.
- **PATH SET:** `99_SMEsPlus_Enterprise_Suite/END_TO_END_BUSINESS_PROCESS_MATRIX.md`,
  plus `MODULE_SPEC_*.md` at the suite root.
- **UNIT:** one declared process; one declared module specification.

**Result: 0 of 10 processes and 0 of 15 module specifications cover manufacturing.**
There is no `MODULE_SPEC_MANUFACTURING.md`. `FACT VERIFIED`.

This is recorded as `P03-GAP-01` in `16_P03_CONTRADICTION_REGISTER.md`: P03 is being
researched against a target baseline that does not yet admit the process exists.
