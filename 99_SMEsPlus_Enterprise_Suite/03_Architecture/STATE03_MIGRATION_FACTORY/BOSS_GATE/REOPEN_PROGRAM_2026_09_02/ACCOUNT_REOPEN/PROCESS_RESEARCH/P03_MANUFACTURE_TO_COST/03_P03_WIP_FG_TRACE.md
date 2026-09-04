# 03 — P03 WIP / FG TRACE

**LAYER 2 — AUDIT QUARANTINE.**

---

## 1. The intended cycle

For a real-time-valued, FIFO or average-costed manufactured product:

| Step | Entry | Source |
|---|---|---|
| 1. Raw issue | Dr **Production Cost**, Cr Stock (raw) | `mrp_account/models/stock_move.py:31-34 — _get_dest_account` returns `accounts_data['production']` when the destination is a production location |
| 2. FG receipt | Dr Stock (FG), Cr **Production Cost**, at `_cal_price`'s `total_cost` | `mrp_account/models/stock_move.py:26-29 — _get_src_account` |
| 3. Labour relief | Dr **Production Cost**, Cr Expense | `mrp_account/models/mrp_production.py:72-106 — _post_labour` |

After all three, the Production Cost account should be flat.

**Arithmetic of the intended cycle** — let `R` = raw value, `W` = work-centre cost,
`X` = extra cost:

```
Step 1:  Production  Dr R
Step 2:  Production  Cr (R + W + X)
Step 3:  Production  Dr W
--------------------------------------
Residual on Production:  Cr X
```

**The cycle does not close.** It closes only when `X = 0`. `FACT VERIFIED`.

## 2. `extra_cost` — the unrelieved residue

`_cal_price` capitalises `extra_cost` (`mrp_account/models/mrp_production.py:53-54`).
`_post_labour` relieves only `_cal_cost()` (`:82-84`), which is work-centre and employee
time. **`extra_cost` is capitalised and never relieved.**

**Enumeration of `extra_cost` writers and readers.**
POPULATION: all `*.py` in the declared source root, excluding `tests/`.
PATTERN: identifier `extra_cost`. UNIT: one occurrence.
Result — 6 occurrences, 4 files:

| Site | Role |
|---|---|
| `mrp_account/models/mrp_production.py:13` | field declaration |
| `mrp_account/models/mrp_production.py:53-54` | **capitalises into FG** |
| `mrp_account/models/mrp_production.py:69` | copies to backorder |
| `mrp_subcontracting_account/models/mrp_production.py:15` | sets it from the subcontract receipt |
| `mrp_subcontracting_account/models/stock_move.py:31` | **splits the credit — relieves it, for subcontracting only** |
| `mrp_subcontracting_account_enterprise/report/mrp_cost_structure.py:27` | report read |

**The documentation states the inverse of the behaviour.** The production-account field's
help text (`mrp_account/models/product.py:126-128`) reads: *"If there are any
workcenter/employee costs, this value will remain on the account once the production is
completed."* Work-centre and employee costs are **exactly what `_post_labour` clears**. The
residue that genuinely remains — `extra_cost` — is not mentioned. A reader following the
help text looks for the balance in the wrong place. Raised by P04, verified here — `25` §4.

**Conclusion.** Subcontract `extra_cost` *is* relieved, by a different mechanism
(`_generate_valuation_lines_data` splits the credit line between component cost and
service cost, crediting the service half to the stock-input account). Manually entered
`extra_cost` on a non-subcontract MO is relieved by **nothing**. `FACT VERIFIED`.

Recorded as `DC-03`.

## 3. Two WIP account families that never meet

| Family | Field | Written by | Reversed? |
|---|---|---|---|
| **A — Production Cost** | `property_stock_account_production_cost_id` on the product category | `_cal_price` / `_post_labour` / raw and finished moves | No — it is a real, permanent flow |
| **B — Production WIP** | `account_production_wip_account_id` and `account_production_wip_overhead_account_id` on the **company** | The WIP wizard only | **Yes — every entry auto-reverses the next day** |

Evidence for family B:
`mrp_account/wizard/mrp_wip_accounting.py:105` (debit account),
`:70-78 — _get_overhead_account`,
`:146-150` (`_reverse_moves` on `reversal_date`, forced later than `date` at `:128`).
Company fields at `stock_account/models/res_company.py:8-9`.

`_get_overhead_account` falls back to family A when the company field is unset
(`:74-78`), so the two families can silently share an account — but the fallback is
one-directional and nothing reconciles them.

**Consequences, all `FACT VERIFIED`:**

1. The balance sheet's WIP line and the account that actually carries production flow are
   different accounts.
2. Family B is an **estimate**, computed at `mrp_account/wizard/mrp_wip_accounting.py:85-88`
   from `product.standard_price`, never from the valuation layers that family A uses. For
   a FIFO or average-costed component the accrual is a different number from the
   consumption it accrues for.
3. Family B is a **reversing accrual**. Between the posting date and the reversal date the
   WIP balance is right; on every other day of the period it is zero. Period-end WIP is
   therefore correct only if someone ran the wizard with the right date and nobody looks
   the day after.
4. Family B has **no MO-level detail** — three summary lines for the whole selection
   (`:92-107`). MO-level WIP cannot be read from the ledger.

## 4. Standard-cost products break the cycle in the opposite direction

`_cal_price` writes `finished_move.price_unit` **only** when
`cost_method in ('fifo', 'average')` — `mrp_account/models/mrp_production.py:63-64`.
The by-product branch at `:61` is gated the same way.

`_post_labour` is gated on **valuation** only — `mo…product_id.valuation != 'real_time'`
at `:74` — **not** on cost method.

For a product that is **standard-costed *and* real-time valued**:

```
Step 1:  Production  Dr R
Step 2:  Production  Cr (standard × qty)          ← W and X never capitalised
Step 3:  Production  Dr W                          ← posted anyway
--------------------------------------------------
Residual on Production:  Dr (R + W − standard×qty)
```

**What the standard contains** — supplied by P04, verified here (`25` §4): the standard
price is built by `_compute_bom_price` (`mrp_account/models/product.py:87-94`) from
**planned** duration x `_total_cost_per_hour`, i.e. the work-centre rate plus, where the
employee bridge is installed, the employee rate x ratio
(`mrp_workorder_hr_account/models/mrp_routing.py:10-11`).

So the mismatch is sharper than the arithmetic above alone shows:

> **Standard overhead on *planned* duration is credited to the production account; actual
> overhead on *actual* duration is debited to it. The difference is stranded, with no
> variance account and no report line pointing at it.**

The work-centre cost is **debited to the production account and credited to an expense
account, while never entering inventory**. The expense account is relieved for a cost that
was never capitalised. `FACT VERIFIED`. Recorded as `DC-04`.

`ASSET_DR_CONTINUATION/22` §5 carries `UNR-C-03` — *how a standard-costed product complies
with TAS 2* — at Medium-High. **`DC-04` is the mechanism behind that question, found
independently from the P03 side.** It is reported to that register, not closed here.

## 5. Finished goods → COGS

The FG unit cost written by `_cal_price` is the **entire** P03 contribution to COGS.
Everything downstream — delivery, invoicing, the COGS entry itself — belongs to P02 and to
the COGS track, which is at **terminal HOLD** (`origin/research/cogs-targeted-resolution-2026-09-03-001`).

P03 therefore states its handoff as a **value**, not as an entry:

> The finished-goods unit cost handed to the COGS track is
> `(Σ raw valuation layers + work-centre cost + extra cost) × (1 − by-product share) ÷ qty`,
> and it **excludes every element listed as `CC-07` … `CC-14` in `02` §1**.

That exclusion is the single most important sentence P03 hands forward.

## 6. Semi-finished / multi-level

A semi-finished item is a manufactured product consumed by a parent MO. It therefore
enters the parent's `Σ raw valuation layers` at whatever value its own `_cal_price`
produced. **Every defect in §2, §4 and in `05` compounds once per BOM level.**
`SUPPORTED INTERPRETATION` — the compounding follows from the recursion; no multi-level
runtime evidence was available to this session.
