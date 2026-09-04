# 09 — P03 MO COST TRACE

**LAYER 2 — AUDIT QUARANTINE.**

The full execution trace of one manufacturing order's cost, in call order, with the state
variants the directive requires.

---

## 1. The call chain

```
button_mark_done                         mrp/models/mrp_production.py:2041
 └─ _post_inventory                      mrp/models/mrp_production.py:1734
     ├─ raw moves _action_done            → AE-01, raw valuation layers
     ├─ per work order:
     │    duration_expected recomputed
     │    if duration == 0 → duration = duration_expected      ← DC-08
     ├─ _cal_price(consumed_moves)        mrp_account/models/mrp_production.py:40
     │    ├─ Σ work_order._cal_cost()                          ← DC-01, DC-02
     │    ├─ + extra_cost × qty                                ← DC-03
     │    └─ writes finished_move.price_unit  (fifo/average only) ← DC-04
     ├─ finished moves _action_done        → AE-02, AE-04
     └─ _post_labour  (state == done)     mrp_account/models/mrp_production.py:72
          ├─ account resolved in the WRONG company             ← DC-11
          ├─ credit defaults to product COGS                   ← DC-07
          └─ date = today                                      ← DC-09
```

## 2. Create and confirm

No cost effect. `_cal_price` on the base model is a no-op returning `True`
(`mrp/models/mrp_production.py:1730-1732`); all cost behaviour is added by the accounting
module. A site without the accounting module manufactures with **no conversion cost at
all** and no error. `FACT VERIFIED`.

## 3. The finished-goods cost formula, exactly

`mrp_account/models/mrp_production.py:44-64`:

```
work_center_cost = Σ over work orders of _cal_cost()
extra_cost       = self.extra_cost × quantity
total_cost       = −Σ(consumed layers' value) + work_center_cost + extra_cost

by-product j:  price_unit = total_cost × share_j / 100 / qty_j     (fifo/average only)
finished:      price_unit = total_cost × (1 − Σshare/100) / qty    (fifo/average only)
```

**Three observations.**

1. `finished_move.ensure_one()` at `:48` — an MO producing more than one finished move of
   its own product raises. The formula assumes a single finished move.
2. The by-product rounding at `:64` uses `float_round(1 − share/100, precision_rounding=0.0001)`
   while each by-product's own share at `:62` is unrounded. For shares that do not
   terminate at four decimals the parts do not sum to the whole. Immaterial in amount,
   but it means **`total_cost` is not conserved across the split**. `FACT VERIFIED`.
3. Cost shares are constrained: `≥ 0` per line and `≤ 100` in total, at both BOM level
   (`mrp/models/mrp_bom.py:199-202`) and MO level (`mrp/models/mrp_production.py:872-874`).
   **The constraint permits exactly 100**, which drives the finished product's unit cost to
   **zero**. A boundary, not a defect — but it is a boundary with no warning, and it is
   the configuration by which a co-product set is expressed. Recorded as a
   tolerance-zero boundary in `13` §5.

## 4. Partial completion and backorders

`_get_backorder_mo_vals` (`mrp/models/mrp_production.py:1786`) is extended by the
accounting module at `:67-70` to copy `extra_cost` to the backorder.

**Tested for double counting; none found on this path.** `extra_cost` is a **unit** cost —
`_cal_price` multiplies it by the quantity of the finished move being valued (`:53`), so
copying it to a backorder charges it once per unit across the split, not twice.
`FACT VERIFIED`.

Work orders are split with the MO, so each backorder's `_cal_cost` sums only its own time
logs. **The split path itself is sound.** What is not sound is what `DC-08` does to it:
each split MO whose work orders carry no time logs independently injects its own
`duration_expected`, and `duration_expected` is recomputed per split
(`_post_inventory`, `mrp/models/mrp_production.py`). Proportionality therefore depends on
`_get_duration_expected` scaling linearly with quantity — which it does for the cycle-time
component but **not** for the work centre's setup and cleanup times, which are per-order.

> **Splitting an MO into N backorders charges setup and cleanup N times.**

`SUPPORTED INTERPRETATION` — the reasoning follows from the code read; no runtime
confirmation was available. Recorded as `UNR-P03-02`, and it is the item this session most
wants confirmed at UAT.

## 5. Cancellation

`_action_cancel` (`mrp/models/mrp_production.py:1682`) cancels unfinished moves and work
orders. Work-order cancellation unlinks analytic lines
(`mrp_account/models/mrp_workorder.py:23-25`). No financial reversal exists, and none is
needed today — see `07` §4.

## 6. Reversal — unbuild

`mrp/models/mrp_unbuild.py:action_unbuild` reverses quantities: consumes the finished
product, produces the components. Cost behaviour is at
`mrp_account/models/stock_move.py:44-67`, which forces the released unit cost to the MO's
finished-goods layer rather than letting the ordinary outbound costing apply.

The intent is right — release what was actually built. The implementation takes
`[0].unit_cost`, the **first** matching layer (`DC-13`).

There is a second, acknowledged limitation in the source itself at
`mrp/models/mrp_unbuild.py:31`: a comment recording that more than one lot-tracked unbuild
against the same MO will fail because prior unbuilds are not accounted for. **Recorded as
a known limitation of the reference product, verified in place.** `FACT VERIFIED`.

## 7. Backdating and correction

No path exists to post conversion cost to a chosen date (`07` §3), and no cost-correction
object was found within the scope declared in `02` §3. `FACT VERIFIED`.
