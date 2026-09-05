# 32 — G02-P02 CUSTOM ADDON FORENSIC DELTA

`LAYER 2 — AUDIT QUARANTINE.` Task **C3**. Baseline `ff8be51`. **OLD SESSION CONTINUATION.**

Trace order used throughout: **Module → Model → Field/Relation → Function/Event → Database/Runtime
effect.** Foreign keys were not used as the primary semantic method.

**Coverage statement.** `31` identifies **46 distinct P02-relevant custom modules with readable source**
and **189 (database, module) pairs with none**. This file works the modules that can **materially change
a P02 finding**; the rest are listed in `31` and are `SOURCE GAP` or not material. **Every module below
was read. No conclusion here rests on a module name.**

---

## CA-01 — `scgl_product_category_company` (18.0.1.5.0) — installed in `551ab874` — **ADDS A CONTROL**

**Trace.** `product.category` gains `company_ids` (m2m) + `usage_type` + per-use booleans →
`product.template._scgl_assert_company_allowed()` → raised from **`@api.constrains`** on
`sale.order.line`, `purchase.order.line`, `stock.move`, **`account.move.line`**, and from method
overrides on `sale.order.action_confirm`, `stock.picking.button_validate`, **`account.move.action_post`**.

| Determination | |
|---|---|
| Class | **OVERRIDES — but by *adding* enforcement the standard product does not have** |
| Effect on a published finding | **`SF-01` is qualified.** `20` records that the reference's company boundary is *data, not structure*. In this deployment a **structural** product↔company scope control exists **at the data layer** — `@api.constrains` fires on create/write, so imports and scripts are covered, not only the form. |
| Scope semantics (`CORR1`) | Empty `company_ids` = **global = allowed**. The control is **opt-in per category**, default open. A separate `scgl_scope_conflict` state returns **deny**. So the module implements *conflict = deny* but **not** *missing = deny*. |
| Does it touch cost recognition? | **No.** It never reads or writes `property_valuation` or the three stock accounts. **`P02-F-05` is unaffected.** |
| UI-vs-data | `name_search` filtering is bypassable via context `scgl_scope_selection_bypass`; **the `@api.constrains` are not.** The selection filter is cosmetic; the constraint is real. |

**`P02-F-32a`.** A deployment has independently built the scope control the reference lacks, and built it
at the correct layer. **This is evidence for the SMEsPlus design candidate, from a real deployment** —
and it is opt-in, which is the part a platform must not copy.

---

## CA-02 — `scgl_date_range_auto_period` (18.0.1.0.0) — installed in `551ab874` — **NAME ≠ BEHAVIOUR**

**Trace.** `date.range.type` → `scgl_create_year_periods()` / `scgl_close_old_periods(months_back=3)` →
cron `scgl_run_auto_period_maintenance` → **writes `{"active": False}` on `date.range` records only.**

| Determination | |
|---|---|
| Class | **IRRELEVANT TO ACCOUNTING CONTROL — and materially misleading by name** |
| Evidence | `grep` for `lock`, `fiscalyear`, `tax_lock`, `hard_lock` across the entire module: **zero hits.** |
| Effect | A cron named *"close old periods"* archives a reporting dimension. **It sets no accounting lock date and prevents no posting.** A period shown as closed remains fully postable. |
| Scope (`CORR1`) | The search filters `company_id = False`, so **company-specific ranges are never archived** — the automation silently skips exactly the multi-company case. |

**`P02-F-32b`.** This is the prompt's *"never treat module name as proof of behaviour"* rule realised in
a live installed module: **the strongest-sounding period control in the deployment has no accounting
effect.** Routed to **P08** (period close) as an observation, not a defect of P02.

---

## CA-03 — `scgl_occ_transportation_costs` (18.0.1.0.0) — installed in `551ab874` — **SCENARIO 7 EVIDENCE**

**Trace.** `sale.order` gains `vehicle_id`, `driver_id`, weights, `transport_ids` (`transport.cost.line`),
`transport_model_id`, and **`net_cost` / `unit_cost` / `total_cost` as computed Monetary fields**.

| Determination | |
|---|---|
| Class | **NEW DATA, NO ACCOUNTING EVENT** |
| Effect | Freight is computed and stored **on the order** and never posted. There is no journal entry, no cost line, no allocation to the delivered goods. |
| Effect on `24` | **Business scenario 7 (freight/delivery charges + tax) gains a deployed data point**: in this deployment freight is a **management statistic**, so freight never enters COGS, revenue or tax through this module. |
| Dead code found | `wizard/account_payment_register.py` overrides `_create_payments` — **the entire file is commented out.** Present, installed, inert. |

**`P02-F-32c`.** A file that exists, is shipped, and does nothing. **Presence of an override file is not
evidence of an override** — the second instance of that shape in this round.

---

## CA-04 — `account_payment_multi_deduction` (18.0.1.0.2, OCA/Ecosoft) — lab-readable — **MATERIAL TO SETTLEMENT**

**Trace.** `account.payment.register` (+`analytic.mixin`) → new
`payment_difference_handling = 'reconcile_multi_deduct'` → `deduction_ids` →
`_update_vals_multi_deduction()` → **multiple write-off lines created from one payment registration**,
balance enforced by `@api.constrains` (`sum(deductions) == payment_difference`).

| Determination | |
|---|---|
| Class | **OVERRIDES the settlement mechanism** |
| Effect on P02 | `09`'s payment/reconciliation matrix assumes the standard **single** write-off. Here **one receipt can be settled to N accounts chosen at registration time.** |
| Effect on a published finding | **`P02-F-43` is widened, not refuted.** Separation still exists only in the outstanding-account configuration; this module adds a second, operator-chosen route by which a receipt's residual reaches arbitrary accounts. |
| Routing | **P06** (settlement/reconciliation) — exact question in `39`. |

---

## CA-05 — `l10n_th_withholding_tax` family (18.0.1.4, OCA) — lab-readable — **ROUTED, NOT ADJUDICATED**

Three installed variants (`…`, `…_cert`, `…_multi`) plus `scgl_wht_control`. Models touched:
`account.move`, `account.payment`, `account.withholding.tax`, `product`.

**Determination: `PEER DEPENDENCY`.** Thai WHT is **P07-owned**. P02 records only that (a) WHT overrides
are installed in the v18 deployment's estate and in three v19 deployments, and (b) **P05 previously found
Thai WHT implemented twice** — consistent with this family plus a custom control module. **P02 does not
decide Thai law and does not re-adjudicate P07's domain.** Routed in `39`.

---

## 2. Modules Read And Found Not Material

| Module | Why not material to P02 |
|---|---|
| `scgl_account_coa_control` | chart presentation/governance; no posting path |
| `scgl_uom_archive`, `scgl_chatter_compact`, `scgl_custom_title_and_favicon`, `scgl_document_terms_conditions` | presentation / master-data hygiene |
| `scgl_multi_approve_core` | approval routing; **does not alter accounting derivation** — approval state is not a posting trigger in the read code |
| `scgl_stock_fleet`, `scgl_dashboard_core` | fleet master data; reporting |

## 3. What C3 Re-Opens

| Finding | Action |
|---|---|
| `SF-01` (reference boundary is data, not structure) | **Qualified** by `CA-01` — a deployment has structural enforcement. Recorded in `37`. |
| `24` scenario 7 (freight) | **Gains deployed evidence** (`CA-03`). Carried to `35`. |
| `P02-F-43` (settlement separation) | **Widened** by `CA-04`. Carried to `37` and routed to P06. |
| Period-integrity line | **`CA-02` adds a false-assurance instance.** Routed to P08. |
| `P02-F-05` (three outcomes) | **Unchanged.** No readable custom module touches valuation mode or the stock accounts. |

## 4. Bound On This File

**189 P02-relevant (database, module) pairs could not be read**, including `inherit_sales` and
`inherit_inventory` on two generations and the entire `cu_*`/`cff_*` estate of the 1.7M-line v14
deployment. **Nothing in §1–§3 generalises to those.** The custom-addon delta is complete **for the
readable set only**, and that bound is the single largest open item in `31`/`32`.
