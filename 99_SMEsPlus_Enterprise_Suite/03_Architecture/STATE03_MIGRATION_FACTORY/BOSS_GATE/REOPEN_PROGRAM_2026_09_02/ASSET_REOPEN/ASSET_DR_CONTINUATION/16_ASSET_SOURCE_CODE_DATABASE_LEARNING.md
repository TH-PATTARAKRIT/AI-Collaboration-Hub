# 16 — SOURCE CODE / DATABASE LEARNING (LEVEL 18)

**LAYER 2 — AUDIT QUARANTINE.** Contains reference-ERP module, model, field and file
names with line references. **Nothing in this file may be transcribed into any
Team-B-facing package.** Its purpose is that a reviewer can re-run every check.

**Clean-room statement.** This session read source to learn **business semantics**. No
source was copied, no schema cloned, no ORM reproduced, no workflow implementation
transplanted. SMEsPlus remains a new clean-room Node.js SaaS ERP. Every design
statement in `19` is expressed in neutral domain terms and is traceable to a *semantic*
finding here, never to an implementation.

---

## 1. Evidence roots

| ID | Root | Identity |
|---|---|---|
| `EV-CODE` | Reference ERP v18 Enterprise addons tree | build `18.0+e.20250608`; **797 modules**, re-counted this session |
| `EV-CUST` | Project custom addon set, v18 line | `equipment_sequence` manifest version `18.0.1.6`, re-read this session |
| `EV-PLAT` | The platform core of `EV-CODE` (`odoo/api.py`, `odoo/fields.py`, `odoo/models.py`) | Used to establish what a custom module's constructs actually do |

## 2. Checks re-run this session, with locators

| # | Claim | Locator | Result |
|---|---|---|---|
| 1 | Operation carries no equipment reference | `mrp/models/mrp_routing.py` lines 17–59 — full field list of `mrp.routing.workcenter` | Confirmed. Only `workcenter_id` |
| 2 | Equipment→work centre is many-to-one | `mrp_maintenance/models/mrp_maintenance.py` — `maintenance.equipment.workcenter_id`, a `Many2one`; inverse `mrp.workcenter.equipment_ids` is the `One2many` | Confirmed |
| 3 | Maintenance request has no monetary field | `maintenance/models/maintenance.py`, `MaintenanceRequest` field block | Confirmed — none |
| 4 | Maintenance blocks capacity only | Same file; `_recreate_leaves` creates `resource.calendar.leaves`; `mrp_maintenance` overrides `_get_unavailability_intervals` with a direct SQL read of scheduled equipment maintenance | Confirmed |
| 5 | Maintenance carries a planned/unplanned axis | `maintenance.request.maintenance_type` ∈ {`corrective`, `preventive`} | Confirmed — **new use, see `09` §6** |
| 6 | Equipment has an inert `cost` field | `maintenance/models/maintenance.py` `MaintenanceEquipment.cost`; grep for `.cost` in the module returns **no consumer** | Confirmed — **new finding** |
| 7 | Downtime taxonomy exists | `mrp/models/mrp_workcenter.py` — `mrp.workcenter.productivity`, `mrp.workcenter.productivity.loss`, `mrp.workcenter.productivity.loss.type` with categories `availability` / `performance` / `quality` / `productive` | Confirmed — **new finding** |
| 8 | Idle time is expressible | `mrp.workcenter.productivity.workorder_id` is **optional** | Confirmed |
| 9 | Downtime duration respects the working calendar | `MrpWorkcenterProductivityLoss._convert_to_duration` — non-productive categories convert via `_get_work_days_data_batch` | Confirmed |
| 10 | Day convention constants | `account_asset/models/account_asset.py` lines 15–16: `DAYS_PER_MONTH = 30`, `DAYS_PER_YEAR = DAYS_PER_MONTH * 12` | Confirmed |
| 11 | Three prorata modes; default is not daily | Same file, `prorata_computation_type` ∈ {`none`, `constant_periods`, `daily_computation`}, `default='constant_periods'` | Confirmed |
| 12 | `none` backdates to the fiscal-year start | `_compute_prorata_date` — sets `prorata_date` to `compute_fiscalyear_dates(...)['date_from']` | Confirmed |
| 13 | Lock guard on disposal, not on confirm | `set_to_close` raises before `_get_user_fiscal_lock_date`; `validate` has no such check | Confirmed |
| 14 | Analytic distribution copied to entries at creation; only draft entries rewritten | `write()` — `if move.state == 'draft' and 'analytic_distribution' in vals` | Confirmed |
| 15 | Off-balance excluded from asset account fields | `account_asset/models/account_asset.py` lines 91, 98, 105 — domains exclude `off_balance` | Confirmed |
| 16 | **Platform-wide off-balance firewall** | `account/models/account_move_line.py` `_check_off_balance` — an `@api.constrains` that raises if any line's account is `off_balance` while any other line's is not | Confirmed — **new finding, `C-03`** |
| 17 | Work-centre expense account has **no** such domain | `mrp_account/models/mrp_workcenter.py` — `expense_account_id` declared with `check_company=True` only | Confirmed — **new finding, the trap in `05` §8** |
| 18 | Machine cost = duration × **live** work-centre rate | `mrp/models/mrp_workorder.py` `_cal_cost` line 587 uses `wo.workcenter_id.costs_hour` | Confirmed — **correction `C-02`** |
| 19 | The work-order rate field is written at **completion** | Same file lines ~662 and ~715, in the mark-done paths; the field's own comment says "at time of work order completion" | Confirmed — **correction `C-01`** |
| 20 | The snapshot is read only by reporting helpers | `_compute_expected_operation_cost`, `_compute_current_operation_cost`, `_get_current_theorical_operation_cost` | Confirmed |
| 21 | Machine cost enters FG value only for FIFO/average | `mrp_account/models/mrp_production.py` `_cal_price` — `if finished_move.product_id.cost_method in ('fifo', 'average')` | Confirmed |
| 22 | The labour ledger entry is dated **today** | Same file, `_post_labour` — `'date': fields.Date.context_today(self)` | Confirmed — **new finding, `T-02`** |
| 23 | The labour entry runs only under real-time valuation | Same method — `if ... product_id.valuation != 'real_time': continue` | Confirmed |
| 24 | Ledger line is stamped back onto the time logs | Same method — `workorders[line.account_id].time_ids.write({'account_move_line_id': line.id})` | Confirmed |
| 25 | Cancelling a work order **deletes** analytic lines | `mrp_account/models/mrp_workorder.py` `action_cancel` and `unlink` — `.unlink()` on the analytic lines | Confirmed — **new finding, `EC-19`** |
| 26 | **No normal-capacity or absorption-variance mechanism anywhere** | Case-insensitive search of all 797 modules for `normal_capacity`, `absorption_variance`, `under_absor`, `over_absor`, `overhead_absor`; and `variance` within `mrp_account` and `stock_account` | **Zero hits.** Exhaustive negative |
| 27 | Product taxonomy is two-dimensional | `product/models/product_template.py` `type` ∈ {`consu`, `service`, `combo`}; `stock/models/product.py` `is_storable` is a separate boolean | Confirmed — **correction to a common assumption** |
| 28 | Multi-company rules | `account_asset/security/account_asset_security.xml` (`parent_of`); `maintenance/security/maintenance.xml` and `mrp/security/mrp_security.xml` (`company_ids + [False]` for equipment, work centre, BoM, operations; strict `company_ids` for work orders and time logs) | Confirmed — **new finding, `14` §2** |

## 3. Custom module forensics — re-verified and widened

Module `equipment_sequence`, version `18.0.1.6`.

**Package loading.** `__init__.py` imports `models` only — **not `wizard`**.
`models/__init__.py` imports five of the eight files present:

| File | Imported | Effect |
|---|---|---|
| `maintenance_equipment_category.py` | **Yes** | Live. Defines `code`, `complete_code_group`, `eq_categ_sequence_id` |
| `maintenance_equipment.py` | **Yes** | Live. Adds `ref_mt`, `status`, `internal_ref`; generates the internal reference |
| `account_asset.py` | **Yes** | Live. **The asset→machine link** |
| `stock_picking.py` | **Yes** | Live |
| `conf_prefix.py` | **Yes** | Live |
| `equipment_sequence.py` | **No** | **Dead.** A superseded earlier version of the category model |
| `equipment_category_sup.py` | **No** | **Dead.** Defines a model `equipment.category.sup` that consequently does not exist |
| `om_asset_asset.py` | **No** | **Dead.** Targets a **different** asset model from a previous generation |
| `wizard/asset_modify.py` | **No** | **Dead.** Contains the disposal→retirement behaviour |

**A near-miss worth recording, because it is how a false High finding is avoided.**
The live `maintenance_equipment.py` reads `category_id.complete_code_group`,
`category_id.code` and `category_id.eq_categ_sequence_id` — all of which are also
defined in the **dead** `equipment_sequence.py`. That looks, at first reading, like
equipment creation must fail. It does not: the **live** `maintenance_equipment_category.py`
defines the same three names. The dead file is a superseded duplicate, not a missing
dependency. **The check was run before the conclusion was formed, not after.**

**A second construct verified rather than assumed.** Both live custom models declare
`@api.model def create(self, vals)` — the single-dict form. In this platform generation
that still works: `odoo/api.py` `model()` detects a method named `create` and wraps it
with `model_create_single`, which accepts either a dict or a list. The cost is a
deprecation warning and the **loss of batch creation** — records are created one at a
time. Performance only, not correctness.

**The four intended link behaviours** (`06` §5) — three inert:

| Behaviour | Construct | Why it does nothing |
|---|---|---|
| Draft-only editing | `states={'draft': [('readonly', False)]}` on the field | The `states` attribute appears **nowhere** in `odoo/fields.py` in this generation. Dead metadata |
| Display the machine reference | `def name_get(self)` | `name_get` appears **nowhere** in `odoo/models.py` in this generation; it was replaced by `_compute_display_name`. Never called |
| Retire the machine on sale/disposal | `wizard/asset_modify.py` `sell_dispose` | The `wizard` package is never imported |
| Claim the machine on confirm | `validate()` override | **Works.** Writes `status = 'tass'` |

**The fifth defect, new this session.** The claim is a **one-way ratchet**: `validate()`
sets the status to claimed; **nothing anywhere sets it back**. Cancellation does not,
unlinking does not, and disposal — which was meant to — never runs. A machine claimed by
a cancelled asset is permanently excluded from the link's selection domain
(`domain="[('status', '=', 'eqp')]"`) with no user-facing remedy.

**Uniqueness.** No `_sql_constraints`, no `@api.constrains` on the link. The
selection-domain filter is a *soft* guard only — `06` §5.

## 4. What was learned — semantics only

The following are the transferable *business* lessons. They are stated without
reference to any implementation and are the only content permitted to seed `19`.

**Worth adopting:**

1. A depreciation schedule that **is** the ledger entries, not a parallel table.
2. Never edit a posted entry: catch up, reverse the future, rebuild forward.
3. Compute each period from the **cumulative** total, so rounding cannot drift.
4. Value is a derivation, never a stored column.
5. Status is read-only; every transition is a guarded operation.
6. Enforce class boundaries **structurally**, the way the off-balance firewall does.
7. Record downtime as **named causes classified into a small fixed set of categories**,
   not as a hard-coded enumeration.
8. Distinguish **planned** from **unplanned** maintenance as a first-class fact.
9. Let a non-productive interval exist with **no** production reference, so idleness is
   representable.
10. Measure non-productive duration against the **working calendar**, not wall-clock.
11. Stamp the ledger line back onto the evidence that produced it.

**Worth refusing:**

1. A 30/360 default.
2. Any mode that backdates depreciation to the fiscal-year start.
3. Labels that misdescribe behaviour — above all one that silently selects between two
   arithmetics.
4. Several accounting events behind one button.
5. Money-changing fields that are invisible on screen.
6. **A single rate that merges the cost pool with the allocation basis.**
7. Rate-bearing configuration changed with no audit trail.
8. **Storing a snapshot that no consumer reads.**
9. **Deleting** allocation records on cancellation instead of reversing them.
10. A monetary field on the operational record that duplicates the financial record.
11. Company-optional master data in a multi-tenant deployment.

## 5. Database evidence

**None obtained this session.** The running UAT was unreachable (`01` §6). All
population and configuration facts are carried from the 2026-08-26 read-out in
`LIN-02`, at their original classification and date. No database fact in this package
is newer than that, and none was inferred to fill the gap.
