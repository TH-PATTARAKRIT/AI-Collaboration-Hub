# 07 — P03 ACCOUNTING EVENT REGISTER

**LAYER 2 — AUDIT QUARANTINE.**

Each accounting event is the effect of exactly one business event from `06`. Where that
mapping fails, it is stated.

---

## 1. Register

| ID | Accounting event | Triggered by | Trigger function | Date used | Class |
|---|---|---|---|---|---|
| `AE-01` | Raw material relieved from stock into production | `BE-05` | `_post_inventory` → `_action_done` on raw moves | Move date | `FACT VERIFIED` |
| `AE-02` | Finished goods taken into stock at computed cost | `BE-09` | `_cal_price` then `_action_done` on finished moves | Move date | `FACT VERIFIED` |
| `AE-03` | **Labour / work-centre cost absorbed** | `BE-06` (+ `BE-07`, which has no owner) | `_post_labour`, `mrp_account/models/mrp_production.py:72-106` | **`fields.Date.context_today(self)` — `:94`** | `FACT VERIFIED` |
| `AE-04` | By-product taken into stock at its cost share | `BE-10` | `_cal_price` `:55-62` | Move date | `FACT VERIFIED` |
| `AE-05` | Scrap written off | `BE-11` | Generic inventory-loss path | Move date | `FACT VERIFIED` |
| `AE-06` | Subcontract service capitalised, split from component cost | `BE-12` | `_generate_valuation_lines_data`, `mrp_subcontracting_account/models/stock_move.py:15-59` | Move date | `FACT VERIFIED` |
| `AE-07` | Period-end WIP accrued | `BE-16` | WIP wizard `confirm()` `:124-145` | Wizard date | `FACT VERIFIED` |
| `AE-08` | Period-end WIP reversed | **Nothing — it is automatic** | `_reverse_moves` `:146-150` | `reversal_date` | `FACT VERIFIED` |
| `AE-09` | Finished goods released on unbuild | `BE-15` | `_get_out_svl_vals`, `mrp_account/models/stock_move.py:44-67` | Move date | `FACT VERIFIED` |
| `AE-10` | Analytic cost recorded — work centre | `BE-06` | `_create_or_update_analytic_entry`, `mrp_account/models/mrp_workorder.py:41-54` | Analytic line date | `FACT VERIFIED` |
| `AE-11` | Analytic cost recorded — employee | `BE-06` | **Only if the Project bridge is installed** — `05` §7 | — | `FACT VERIFIED` |
| `AE-12` | Cancellation of an absorbed labour cost | `BE-14` | **None exists — §4** | — | `FACT VERIFIED` |
| `AE-13` | Variance recognised | — | **None exists — `10`** | — | `FACT VERIFIED` |
| `AE-14` | Unallocated fixed overhead expensed | — | **None exists — `02` §2** | — | `FACT VERIFIED` |

## 2. `AE-03` — the accounting date is system-derived

```
'date': fields.Date.context_today(self),
```
`mrp_account/models/mrp_production.py:94`

The entry that absorbs conversion cost takes **the date the button was pressed**, not:
- the MO's completion date,
- the finished move's date, which `AE-02` uses,
- or the time logs' dates, which are the evidence of when the work happened.

**Therefore `AE-02` and `AE-03` — two halves of one economic event — can fall in different
periods.** An MO completed on 30 September and confirmed on 2 October capitalises the cost
in September and relieves it in October. Both periods are misstated, in opposite
directions.

This is the manufacturing instance of the **system-derived accounting date** already
recorded for the core ledger in `smeplus-account-wave-a-core-findings`. P03 does not
re-adjudicate it; it registers that the defect recurs here, in the one entry that decides
inventory value. `FACT VERIFIED`. Recorded as `DC-09`.

## 3. Backdating

There is no mechanism to post `AE-03` to a chosen date. `_post_labour` accepts no date
argument. The only date control available anywhere in P03 is the WIP wizard's `date`
field, which governs a reversing accrual, not a real cost. `FACT VERIFIED`.

## 4. `AE-12` — cancellation asymmetry

On cancel (`BE-14`), `mrp_account/models/mrp_workorder.py:23-25` unlinks the work order's
**analytic** lines. Nothing unlinks or reverses a **financial** entry.

This is internally consistent only because `_post_labour` runs solely for MOs that reach
state `done` (`mrp_account/models/mrp_production.py:110`), so a cancelled MO never posted
one. **The asymmetry is therefore safe today and fragile by construction:** any future
path that posts labour before `done` — a partial-completion accrual, for instance —
inherits a cancellation path that cleans up analytic and leaves the ledger.

`SUPPORTED INTERPRETATION` on the fragility; `FACT VERIFIED` on the current behaviour.

## 5. Events with no accounting effect at all

`AE-13` and `AE-14` are listed with no trigger deliberately.

- **`AE-13` variance.** The reference product recognises no manufacturing variance. See
  `10_P03_VARIANCE_MATRIX.md` for why this is a structural absence, not a missing report.
- **`AE-14` unallocated fixed overhead.** TAS 2 ¶13, and `ASSET_DR_CONTINUATION` `BLK-06`
  closed by Boss decision `BD-02`, both require unallocated production overhead to be
  expensed in the period incurred. **There is no overhead pool, so there is nothing to
  leave unallocated, so no such entry can exist.** The absence is a consequence of the
  `02` §2 modelling gap, not an independent defect.

Both are routed forward as requirements, not resolved here.
