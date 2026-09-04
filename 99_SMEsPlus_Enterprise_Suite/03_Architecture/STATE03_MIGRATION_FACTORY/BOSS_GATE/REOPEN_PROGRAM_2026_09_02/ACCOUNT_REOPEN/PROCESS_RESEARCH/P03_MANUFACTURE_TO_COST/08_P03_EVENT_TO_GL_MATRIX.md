# 08 — P03 EVENT-TO-GL MATRIX

**LAYER 2 — AUDIT QUARANTINE.**

Accounts are named by role, not by code. Account resolution is company-dependent; where
the resolution itself is defective this is stated.

---

## 1. Matrix

| Event | Dr | Cr | Amount | Source of the account |
|---|---|---|---|---|
| `AE-01` raw issue | **Production Cost** | Stock — raw | Valuation-layer value | `_get_dest_account`, `mrp_account/models/stock_move.py:31-34` |
| `AE-02` FG receipt | Stock — FG | **Production Cost** | `_cal_price` `total_cost` | `_get_src_account`, `:26-29` |
| `AE-03` labour absorption | **Production Cost** | Work-centre expense **or, by default, product COGS** | `_cal_cost()` | `mrp_account/models/mrp_production.py:81, 90-91` |
| `AE-04` by-product receipt | Stock — by-product | **Production Cost** | `total_cost × share ÷ qty` | `_cal_price` `:61-62` |
| `AE-05` scrap | Scrap / inventory loss | Stock | Valuation-layer value | Generic path |
| `AE-06` subcontract receipt | Stock — FG | Split: **Stock Input** for the service half, valuation account for the component half | `extra_cost × qty`, remainder | `mrp_subcontracting_account/models/stock_move.py:33-55` |
| `AE-07` WIP accrual | **Production WIP (company field)** | Stock Valuation + **WIP Overhead** | `compo_value + overhead_value` | `mrp_account/wizard/mrp_wip_accounting.py:92-107` |
| `AE-08` WIP reversal | reverse of `AE-07` | | same | `:146-150` |
| `AE-09` unbuild | Stock — components | Stock — FG | First layer's unit cost | `mrp_account/models/stock_move.py:49-51` |

## 2. Account resolution — three different resolvers for what should be one WIP

| Event | Account field | Level | Company context |
|---|---|---|---|
| `AE-01`, `AE-02`, `AE-03`, `AE-04` | `property_stock_account_production_cost_id` | Product **category** | `AE-03` resolves it **in the wrong company** — `DC-11` |
| `AE-07` debit | `account_production_wip_account_id` | **Company** | `self.env.company` |
| `AE-07` overhead credit | `account_production_wip_overhead_account_id`, falling back to the category property then to stock-input | **Company**, then category | `self.env.company`, then a company-dependent fallback |

**Three resolvers, two levels, one concept.** `FACT VERIFIED`. See `03` §3.

## 3. Balance test per event

An entry is *self-balancing* if the code guarantees Dr = Cr.

| Event | Self-balancing? | How |
|---|---|---|
| `AE-01`, `AE-02`, `AE-04`, `AE-05`, `AE-09` | Yes | Generic valuation machinery |
| `AE-03` | **Yes, by construction** | `labour_amounts[account] -= workcenter_cost` at `:91` forces the offset before creation |
| `AE-06` | **Yes** | The original credit line is deleted at `:34` and replaced by two lines summing to it |
| `AE-07` | **Yes, but only if a human agrees** | `confirm()` raises unless credits equal debits (`:126-127`) — the wizard's lines are **user-editable** (`readonly=False`, `:67`) |

`AE-07` is the only entry in P03 whose amount a user may overwrite before posting, with no
record of the overwrite. `FACT VERIFIED`.

## 4. Where the matrix does not close

| Residue | Account left carrying it | Cause |
|---|---|---|
| `extra_cost`, non-subcontract | Production Cost, **credit** | `DC-03` |
| Standard-cost conversion cost | Production Cost, **debit** | `DC-04` |
| Overlap-inflated machine cost | Capitalised into **Stock — FG** | `DC-01` |
| Labour credited to COGS | **COGS**, wrong period | `DC-07` |

The first two are visible as a non-zero Production Cost balance and are in principle
detectable at close. **The third and fourth are not detectable from the ledger at all** —
they are arithmetically balanced entries carrying the wrong amount to the right accounts,
and the wrong amount to a defensible account, respectively.

That asymmetry is the reason `09` and `10` exist: the material errors in P03 do not
present as an out-of-balance.
