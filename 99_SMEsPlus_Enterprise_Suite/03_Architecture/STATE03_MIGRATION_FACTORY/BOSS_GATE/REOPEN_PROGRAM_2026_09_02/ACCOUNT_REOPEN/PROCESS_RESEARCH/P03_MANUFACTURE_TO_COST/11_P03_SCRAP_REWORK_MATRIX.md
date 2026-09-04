# 11 — P03 SCRAP / REWORK MATRIX

**LAYER 2 — AUDIT QUARANTINE.**

---

## 1. Scrap — what exists

Manufacturing extends the generic scrap record with a manufacturing-order link, a
work-order link, and kit handling (`mrp/models/stock_scrap.py`).

| Behaviour | Present? | Evidence |
|---|---|---|
| Scrap can be linked to an MO | Yes | `:10-12` |
| Scrap can be linked to a work order | Yes — but **informational only** | `:13-15`, and the source comment says so in place |
| Source location follows MO state | Yes | `:23-39` |
| The scrap move is attributed to the MO's raw or finished side | Yes | `:41-49` |
| **Normal vs abnormal scrap distinction** | **No** | scope §3 |
| **Re-absorption of normal scrap into good units** | **No** | scope §3 |
| **A manufacturing scrap expense account** | **No** | scope §3 |
| Replenishment of scrapped material | Yes | `:83-90` |

## 2. What that means for cost

Scrap is valued and posted by the generic inventory-loss path — full stop. Therefore:

1. **All scrap is abnormal, in effect.** Every scrapped unit's cost leaves inventory to a
   loss account. None is re-absorbed into the surviving good units.
2. `ASSET_DR_CONTINUATION/12` §3 classifies *abnormal waste* as a period expense and, by
   the same standard, normal process loss as part of conversion cost. **The reference
   product implements one of the two and has no way to express the other.**
3. The work-order link is informational, so scrap cannot be attributed to the operation
   that caused it. **Scrap has no cost causality.** This is the same failure mode as
   `BE-07` in `06` §3 — the record exists, the causal link does not.

`FACT VERIFIED`.

## 3. Rework — a verified negative

**Enumeration.** POPULATION: all files under the declared source root
(`/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/`, 797 modules).
PATTERN: case-insensitive `rework` in `*.py`. UNIT: one file containing at least one match.

**Result: 1 file, and it is unrelated** — an authentication module, where the string
occurs incidentally. **No manufacturing rework object, field, state or cost path was found
anywhere in the population.**

Stated to the required standard: **NO EVIDENCE FOUND within this scope.** This is not a
claim that rework is impossible to express — an operator can model it as a second MO
consuming the defective item — it is a claim that **no first-class rework concept exists**,
so rework cost cannot be identified, reported or accounted for as rework.

The repair module (`mrp_repair`) was examined and is a **field/after-sales repair** flow,
not production rework. It is not a substitute.

`FACT VERIFIED`, scope declared.

## 4. Consequences for SMEsPlus — `DESIGN CANDIDATE`

| # | Requirement | Because |
|---|---|---|
| `R-07` | Scrap must carry a **normal / abnormal** classification, decided at or before the scrap event | TAS 2 ¶13, and `ASSET_DR_CONTINUATION/12` §3 |
| `R-08` | Normal scrap must be absorbed into the good units of the same cost object; abnormal scrap must be expensed | as above |
| `R-09` | Scrap must be attributable to the operation that caused it, not merely annotated with one | `06` §3, cost causality |
| `R-10` | Rework must be a first-class event with its own cost, distinguishable from original production and from repair | §3 |

**None of these is authorised for implementation.** `R-07` and `R-08` in particular depend
on `ASSET_DR_CONTINUATION` `BLK-07`, because "normal" is meaningless without a normal
capacity or normal loss rate to measure against. Recorded as `DEP-02`.

## 5. By-product, co-product, production return

| Concept | Modelled? | Note |
|---|---|---|
| **By-product** | Yes, as a finished move with a cost share | `09` §3 |
| **Co-product** | **Not distinctly** | Expressed as by-products whose shares sum to 100, which zeroes the main product. A joint-product cost model does not exist. `FACT VERIFIED` |
| **Production return** | **Not a manufacturing object** | A return of finished goods is an inventory movement; it does not reverse conversion cost. The only reversal of conversion cost is unbuild — `09` §6 |

The co-product row connects to the COGS track's **Joint Closure** work, which
`smeplus-cogs-targeted-resolution-status` records as **content-empty**. P03 registers that
the joint/co-product cost model is unaddressed on both tracks and belongs to neither by
default — `12_P03_CROSS_PROCESS_OWNERSHIP.md` `OWN-07`.
