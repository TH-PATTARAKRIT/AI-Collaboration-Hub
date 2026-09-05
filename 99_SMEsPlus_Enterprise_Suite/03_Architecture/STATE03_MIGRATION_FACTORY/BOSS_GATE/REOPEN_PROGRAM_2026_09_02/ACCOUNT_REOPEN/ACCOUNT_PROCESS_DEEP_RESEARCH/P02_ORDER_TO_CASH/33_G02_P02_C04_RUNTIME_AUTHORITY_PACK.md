# 33 — G02-P02 `C-04` RUNTIME / AUTHORISATION BOUNDARY

`LAYER 2 — AUDIT QUARANTINE.` Task **C4**. Baseline `ff8be51`.

**Status: `BOSS AUTHORISATION REQUIRED` — read-only routes exhausted and evidenced, and the
authorisation now requested is materially smaller than previously assumed.**

> ## ⚠ CORRECTION BANNER — `C-41`, `C-42`; AAS-03 Expert 4, CONFIRMED
>
> **`C-41` — the runtime population was author-chosen by container name.** §2 enumerated the lab from
> the two `occ-*` containers. **`docker ps` returns three.** The third, `bhpro92-db`, holds **two more
> databases, both 19.0.1.3**, both with the stock stack installed:
>
> | database | gen | AML | `anglo_saxon_accounting` |
> |---|---|---|---|
> | `bhpro92_test` | **19.0.1.3** | 0 | NULL |
> | `bhpro_tracking_test_20260901` | **19.0.1.3** | 0 | **`true`** |
>
> **`P02-F-33a`'s verdict survives** — both are also transaction-empty, so *no database in the lab has
> ever posted a journal line* still holds across **9**, not 7. **Its denominator does not.** This is the
> package's own recurring `PATH SET` defect, this time on *runtime* evidence: the enumeration was by
> container name, not by an executed census. **The declared PATH SET for runtime evidence is hereby
> every running postgres container, and the command is `docker ps`.**
>
> **Two consequences that change the ask.** §5.10 said the run "says nothing about v19" and treated
> that as unavoidable — **it is not**: a v19 target now exists. And
> `bhpro_tracking_test_20260901` is a live **anglo-ON / `inventory_valuation='periodic'`** instance on
> the target generation with zero transactions — a **fifth member of the discriminating identity set**,
> and a never-transacted control obtained without any authorisation.
>
> **`C-42` — §5.9 as scoped tests a determined question.** Expert 4 shows
> `_stock_account_prepare_anglo_saxon_out_lines_vals` reads no existing COGS lines and
> `move.invoice_line_ids` structurally excludes them, so a manual re-invocation **must** double. The
> pack's stated inference rule ("unchanged ⇒ a guard exists in practice") names an outcome that cannot
> occur — it buys a confirmation, not a discrimination. Worse, `03` §6 already identified the
> *reachability* mechanism: a **future-dated** sale document posted through a **soft-mode** caller,
> re-posted by the autopost cron. §5.4/§5.9 describe a **hard-mode** `action_post` run, which reproduces
> neither half. **The two files put different questions under one identifier.**
>
> **Revised request, superseding §5.9:** reproduce `03` §6's mechanism — post a future-dated invoice for
> a storable, real-time product through a soft-mode caller, assert the COGS pair on a draft move, let
> the autopost path post it, and count. **Target company `id=1` (`My Company`), not a real-entity
> record. `pg_dump` becomes mandatory, not recommended. A v19 counterpart target is now available and
> should be named.**

**Nothing was mutated to produce this file.** Every statement below came from `docker ps`, `psql`
`SELECT`, and reading files. No install, no upgrade, no restore, no transaction, no configuration write.

---

## 1. What `C-04` Is

Cost-of-sales **idempotency**: whether the invoice-side cost generator, run twice over the same
document, produces duplicate cost lines. `03` §6 established there is **no guard** in the standard
source; whether it is **exploitable** was left `UNRESOLVED` because it requires executing the path twice.

## 2. Read-Only Exhaustion — Executed, Not Assumed

`30`/`L-01` corrected the old reason for this blocker: the session **does** have database access. So the
read-only route was actually run.

**A live lab exists and was inspected.** Docker is running: `occ-odoo18-db` (postgres:16, up 6 days) and
`occ-odoo18-webtest` (odoo:18.0, up 6 days).

| Lab database | journal lines | posted moves | valuation-layer table | verdict |
|---|---|---|---|---|
| `occ_anglo_test` | **0** | **0** | present | never transacted |
| `occ_perp_sim` | **0** | **0** | present | never transacted |
| `occ_sim` | 0 | 0 | **absent** | stock stack not installed |
| `occ_sim_fresh` | 0 | 0 | absent | " |
| `occ_website_sim` | 0 | 0 | absent | " |
| `occ_wht_sim` | 0 | 0 | absent | " |
| `occ_wht_multi_sim` | 0 | 0 | absent | " |

**`P02-F-33a`. No database in the lab has ever posted a journal line.** Retained evidence was also
checked: `evidence/perpetual_at_invoicing/02_sim_inventory.txt` is a real prior run, but its output
stops at a chart-of-accounts dump — **it never reached a transaction**. `C-04` therefore **cannot** be
answered from existing state. That is now a measured negative, not an assumption.

## 3. What The Read-Only Pass *Did* Close

These were runtime-verified from the live lab and require no authorisation:

| ID | Fact | Class |
|---|---|---|
| `P02-F-33b` | On a fresh v18 install with the Thai localisation, **`anglo_saxon_accounting = false` on all four Thai companies** (`NULL` on the template company). | **`DEPLOYED BEHAVIOUR VERIFIED`** — previously a source claim (`EV-P02-042`/`043`). |
| `P02-F-33c` | `ir_default` for `property_valuation` is **`"manual_periodic"`, company-independent (global)**; `property_stock_account_input_categ_id` and `…output_categ_id` default to **`false`**; **`property_stock_valuation_account_id` has no default row at all.** | **`DEPLOYED BEHAVIOUR VERIFIED`** — confirms `EV-P02-100`/`117` at runtime. |
| `P02-F-33d` | The Thai chart supplies `130000 Inventory` and `510000 Cost of Revenue (expense_direct_cost)` per company, **but no stock interim account** — the test script must *create* `130100` before it can exercise the split path. | **`DEPLOYED BEHAVIOUR VERIFIED`** — independent corroboration of `EV-P02-044`/`045`. |

**The configuration premise in `00` §3b is now verified at runtime, not only in source.** That is a real
gain from this round and it did not require a single write.

## 4. Why The Authorisation Is Now Smaller

Previously assumed: install the perpetual stack, then transact. **`occ_anglo_test` already has it:**

```
account 18.0.1.3 · l10n_th 18.0.2.0 · purchase_stock 18.0.1.2 · sale 18.0.1.2
sale_stock 18.0.1.0 · stock 18.0.1.1 · stock_account 18.0.1.1     — all state='installed'
```

**No module installation or upgrade is requested.** The request reduces to *creating transactions in an
already-prepared, transaction-empty, disposable database*.

---

## 5. `C-04` BOSS AUTHORISATION PACK

### 5.1 Exact command
```
docker exec -i occ-odoo18-webtest odoo shell -d occ_anglo_test --no-http \
  < /Users/admin/OCC_Odoo18_Simulation_Lab/scripts/anglo_gross_profit_test.py
```
plus **one** appended idempotency step, which is the only new code (§5.9).

### 5.2 Exact target
Container `occ-odoo18-db`, database **`occ_anglo_test`** (51 MB, 0 journal lines, 0 posted moves).
**Not** `occ_sim` and **not** any customer database.

### 5.3 Exact modules / configuration required
None installed. The script writes configuration: `res_company(id=2).anglo_saxon_accounting = True`;
creates account `130100` if absent; creates a real-time product category, warehouse `ATW`, one product
(cost 60 / price 100), one supplier, one customer.

### 5.4 Exact writes / state changes
`res.company` (1 field) · `account.account` (1 create) · `product.category` (1) · `stock.warehouse` (1) ·
`product.template` (1) · `res.partner` (2) · `purchase.order` + receipt `button_validate` + vendor bill
`action_post` · `sale.order` + delivery `button_validate` + customer invoice `action_post` ·
**`env.cr.commit()`**. Then §5.9 re-runs the invoice-side cost generator on the same posted invoice.

### 5.5 Snapshot / reset
**No snapshot of `occ_anglo_test` exists** — it is disposable and empty, so none is needed.
Recommended pre-step: `docker exec occ-odoo18-db pg_dump -U odoo -Fc occ_anglo_test > occ_anglo_test_pre_c04.dump`.

### 5.6 Rollback
`docker exec occ-odoo18-db dropdb -U odoo --if-exists occ_anglo_test` then `createdb`, optionally
restoring §5.5. `occ_sim` has its own proven path (`scripts/reset_to_baseline.sh`, snapshot +
`sha256`) — **not needed here, and not to be run**, since it would reset a different database.

### 5.7 Isolation proof
`LAB_STATUS.md`: *no connection to customer UAT DB; no customer credentials stored; no customer
accounting data modified.* Independently confirmed here: the target holds **0 journal lines and 0 posted
moves**, so no accounting history can be damaged. **Caveat recorded honestly:** the four company
*records* carry real OCC entity names, copied by a chart install. They contain no transactions. If Boss
requires it, the run can be pointed at company `id=1` (`My Company`) instead of `id=2`.

### 5.8 Evidence to retain
`SNAP` lines at all five stages (notably `AFTER_DELIVERY_BEFORE_INVOICE`), the `GROSS_PROFIT / REVENUE /
COGS / INTERIM` block, `display_type` distribution of `account_move_line` before and after the second
run, `stock_valuation_layer` count and `account_move_id` linkage, plus the full session log.

### 5.9 The question the run answers
**Exactly one: is the invoice-side cost generator idempotent?** Method: after the invoice posts,
re-invoke the anglo cost-line generator for the same move and **count `display_type='cogs'` lines
before and after**. Unchanged ⇒ a guard exists in practice; doubled ⇒ `C-04` is a **live** defect.

Secondary, obtained free: the first direct observation anywhere in this package of the split path
**executing** — outcome 1 of `P02-F-05`, never yet witnessed in 17 deployed databases.

### 5.10 What it will NOT answer
Nothing about the **deployed** estate: `iSMEs` (16.0), the 1.7M-line v14 deployment, or any v19
database. It runs standard v18 code with **none** of the 189 unreadable custom modules
(`inherit_sales`/`inherit_inventory` included), so it **cannot** establish deployed behaviour anywhere.
It also says nothing about v19, whose mechanism differs and whose guard is absent (`P02-F-05c`).

### 5.11 Maximum scope requested
> Authority to execute **one** scripted run, and one appended idempotency step, against the **single
> disposable database `occ_anglo_test`** in the local `occ-odoo18-db` container, with no module
> install/upgrade, no touching of any other database, and a stated drop-and-recreate rollback.

**Not requested:** any change to `occ_sim` or the other five lab databases, any customer/production/UAT
system, any module installation, any repeat runs.

---

## 6. Disposition

**`C-04` remains OPEN — reclassified `BLOCKED — BOSS AUTHORISATION`, not `BLOCKED — EVIDENCE REQUIRED`.**
This is the only P02-owned item in this round that cannot be advanced without a decision, and per §14 of
the prompt no work was left waiting on it: `31`, `32`, `34`–`43` were completed regardless.
