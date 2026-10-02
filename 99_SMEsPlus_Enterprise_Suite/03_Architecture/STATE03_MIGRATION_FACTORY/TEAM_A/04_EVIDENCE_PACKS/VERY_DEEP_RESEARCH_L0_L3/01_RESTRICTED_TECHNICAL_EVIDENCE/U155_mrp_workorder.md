# U155 — mrp_workorder: Detailed Workorders (MRP Community)

**Unit:** U155 | **G Group:** G07 | **Priority:** P2  
**Researcher:** DeepSeek Worker — STATE03 VDR  
**Date:** 2026-10-02  
**Odoo Version:** 19.0.post20260921 Community (LGPL-3)

---

## STANDALONE ADDON STATUS: ABSENT

The directory `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_workorder` does **not exist** in the Community source tree.

**However:** The `mrp.workorder` model and full workorder lifecycle machinery is built directly into the Community `mrp` addon at:
`odoo/addons/mrp/models/mrp_workorder.py` (959 lines)

All claims below are sourced from the Community `mrp` addon. Claims C01–C03 document the ABSENT standalone addon. Claims C04–C22 document the PRESENT embedded workorder machinery.

---

## VDR CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| C01 | F-ABSENT-ADDON | mrp_workorder/ | directory does not exist | ABSENT | unconditional | HARD | The standalone `mrp_workorder` addon directory is absent from the Community addons tree; the path `odoo/addons/mrp_workorder` yields no such file or directory | See neutral C01 |
| C02 | F-ADDON-LOCATION | mrp/__manifest__.py:12 | `'depends': ['product', 'stock', 'resource']` | ABSENT-SCOPE | unconditional | HARD | The Community `mrp` addon declares no dependency on a `mrp_workorder` addon; the workorder model is bundled directly rather than supplied by a separate package | See neutral C02 |
| C03 | F-COMMUNITY-MRP-WO | mrp/__manifest__.py:29 | `'views/mrp_workorder_views.xml'` | PRESENT | unconditional | INFO | The `mrp` manifest registers `mrp_workorder_views.xml` and `mrp_workorder_templates.xml`, confirming workorder UI is part of the Community mrp module itself | See neutral C03 |
| C04 | F-MODEL-DECL | mrp/models/mrp_workorder.py:15-18 | `class MrpWorkorder(models.Model)` `_name = 'mrp.workorder'` | PRESENT | unconditional | HARD | The `mrp.workorder` model is declared in `mrp/models/mrp_workorder.py` line 15 with `_name = 'mrp.workorder'`, ordered by `sequence, leave_id, date_start, id` | See neutral C04 |
| C05 | F-WORKCENTER-FIELD | mrp/models/mrp_workorder.py:35-37 | `workcenter_id = fields.Many2one('mrp.workcenter', 'Work Center', required=True, index=True, check_company=True)` | PRESENT | unconditional | HARD | The `workcenter_id` field is a required Many2one to `mrp.workcenter`, indexed and company-checked; it drives calendar-based scheduling via `resource.calendar.leaves` | See neutral C05 |
| C06 | F-STATE-MACHINE | mrp/models/mrp_workorder.py:66-73 | `state = fields.Selection([('blocked','Blocked'),('ready','To Do'),('progress','In Progress'),('done','Finished'),('cancel','Cancelled')])` | PRESENT | unconditional | HARD | The workorder state machine defines five states: blocked, ready, progress, done, cancel; state is a stored computed field; the initial default is `ready` | See neutral C06 |
| C07 | F-STATE-COMPUTE | mrp/models/mrp_workorder.py:151-160 | `def _compute_state(self)` | PRESENT | depends on qty_ready | HARD | `_compute_state` transitions between `blocked` and `ready` based on `qty_ready`: if `qty_ready > 0` the workorder is `ready`; otherwise it is `blocked`; states `progress`, `done`, `cancel` are set by explicit methods | See neutral C07 |
| C08 | F-TIME-IDS | mrp/models/mrp_workorder.py:118-119 | `time_ids = fields.One2many('mrp.workcenter.productivity', 'workorder_id', copy=False)` | PRESENT | unconditional | HARD | Time tracking records are stored as a One2many to `mrp.workcenter.productivity`; each record holds `date_start`, `date_end`, `loss_id`, `user_id`, and a computed `duration` field | See neutral C08 |
| C09 | F-DURATION-COMPUTE | mrp/models/mrp_workorder.py:347-355 | `def _compute_duration(self)` | PRESENT | depends on time_ids.duration | HARD | Real duration is computed by calling `get_duration()` which sums all `mrp.workcenter.productivity` intervals grouped by loss type; `duration_unit` = duration / max(qty_produced, 1); `duration_percent` tracks deviation from expected | See neutral C09 |
| C10 | F-BUTTON-START | mrp/models/mrp_workorder.py:656-703 | `def button_start(self, raise_on_invalid_state=False)` | PRESENT | state not in done/cancel | HARD | `button_start` creates an `mrp.workcenter.productivity` record via `_prepare_timeline_vals()` with `date_start = now()` and no `date_end`; it also writes `state='progress'` and creates a `resource.calendar.leaves` slot if one does not already exist | See neutral C10 |
| C11 | F-BUTTON-FINISH | mrp/models/mrp_workorder.py:705-736 | `def button_finish(self)` | PRESENT | state not in done/cancel | HARD | `button_finish` calls `end_all()` to close all open productivity lines, then writes `state='done'`, `date_finished=now()`, `qty_produced`, and captures `costs_hour` from the workcenter at completion time | See neutral C11 |
| C12 | F-TIMELINE-VALS | mrp/models/mrp_workorder.py:876-895 | `def _prepare_timeline_vals(self, duration, date_start, date_end=False)` | PRESENT | unconditional | HARD | Productivity entries are created with a `loss_id` set to the `productive` loss type when duration ≤ expected, or `performance` loss type when duration exceeds expected; a UserError is raised if neither loss type is configured | See neutral C12 |
| C13 | F-PRODUCTIVITY-MODEL | mrp/models/mrp_workcenter.py:505-550 | `class MrpWorkcenterProductivity(models.Model)` `_name = 'mrp.workcenter.productivity'` | PRESENT | unconditional | HARD | The `mrp.workcenter.productivity` model stores `workcenter_id`, `workorder_id`, `user_id`, `loss_id`, `date_start`, `date_end`, and a computed `duration` in minutes; it is the canonical time-tracking record for workorders | See neutral C13 |
| C14 | F-CLOSE-TIMER | mrp/models/mrp_workcenter.py:594-610 | `def _close(self)` | PRESENT | date_end is None | HARD | `_close()` writes `date_end = now()` on open productivity lines; if `wo.duration > wo.duration_expected` it creates or re-labels a separate `performance` record for the overrun portion | See neutral C14 |
| C15 | F-MO-BLOCKING | mrp/models/mrp_production.py:594 | `elif production.workorder_ids and all(wo_state in ('done', 'cancel') for wo_state in production.workorder_ids.mapped('state'))` | PRESENT | unconditional | HARD | The MO `_compute_state` transitions the manufacturing order to `to_close` only when ALL workorders are in state `done` or `cancel`; any workorder still in `blocked`, `ready`, or `progress` keeps the MO in `progress` state and prevents closure | See neutral C15 |
| C16 | F-WO-GENERATION | mrp/models/mrp_production.py:606-660 | `def _compute_workorder_ids(self)` | PRESENT | state == draft | HARD | In draft state, `_compute_workorder_ids` iterates BOM `operation_ids` via `bom_id.explode()` and constructs workorder create/update/delete commands; each operation's `workcenter_id`, `name`, and sequence are copied to the new workorder record | See neutral C16 |
| C17 | F-WO-LINKING | mrp/models/mrp_production.py:1669-1696 | `def _link_workorders_and_moves(self)` | PRESENT | unconditional | HARD | When `allow_workorder_dependencies=True`, `_link_workorders_and_moves` reads `operation_id.blocked_by_operation_ids` to build Many2many dependency links; when False it chains workorders sequentially so each is blocked by its predecessor | See neutral C17 |
| C18 | F-PLAN-WORKORDER | mrp/models/mrp_workorder.py:582-636 | `def _plan_workorder(self, replan=False)` | PRESENT | state in blocked/ready | HARD | `_plan_workorder` calls `workcenter._get_first_available_slot()` for the assigned workcenter and all alternatives; it picks the workcenter with the earliest finish date, creates a `resource.calendar.leaves` slot, and writes `leave_id` and `workcenter_id` back to the workorder | See neutral C18 |
| C19 | F-DURATION-EXPECTED | mrp/models/mrp_workorder.py:811-836 | `def _get_duration_expected(self, alternative_workcenter=False, ratio=1)` | PRESENT | unconditional | HARD | Expected duration is computed as `setup + cleanup + cycle_number * time_cycle * 100.0 / time_efficiency` using `workcenter._get_capacity()`; for alternative workcenters the same formula is recalculated with the alternative's capacity and efficiency | See neutral C19 |
| C20 | F-CONFLICT-DETECT | mrp/models/mrp_workorder.py:838-862 | `def _get_conflicted_workorder_ids(self)` | PRESENT | unconditional | INFO | A raw SQL query detects scheduling conflicts by testing `OVERLAPS` between `date_start`/`date_finished` intervals for workorders in the same workcenter both in state `blocked` or `ready` | See neutral C20 |
| C21 | F-WO-DEPENDENCIES | mrp/models/mrp_workorder.py:142-149 | `blocked_by_workorder_ids`, `needed_by_workorder_ids` Many2many | PRESENT | allow_workorder_dependencies | HARD | Workorder dependencies are stored as a self-referencing Many2many through `mrp_workorder_dependencies_rel`; cyclic dependencies raise a `ValidationError` via `_check_no_cyclic_dependencies` | See neutral C21 |
| C22 | F-QTY-READY | mrp/models/mrp_workorder.py:249-262 | `def _compute_qty_ready(self)` | PRESENT | unconditional | HARD | The quantity ready to process (`qty_ready`) is bounded by the minimum `qty_produced` of all predecessor workorders in the dependency chain, enabling progressive production through sequential operations | See neutral C22 |

---

## KEY FINDINGS SUMMARY

- **Standalone addon ABSENT:** `mrp_workorder` as a separate installable addon does not exist in Community 19. The Enterprise edition ships a richer `mrp_workorder` addon adding tablet UI, quality steps, and additional state transitions.
- **Community workorder model IS PRESENT** in `mrp/models/mrp_workorder.py` (959 lines) as an integral part of the base `mrp` module.
- **State machine:** 5 states — `blocked → ready → progress → done/cancel`. Transition to `progress` via `button_start()`; to `done` via `button_finish()` / `action_mark_as_done()`.
- **Time tracking:** `mrp.workcenter.productivity` records with `date_start`/`date_end`; `duration` is computed from intervals. `_close()` handles overrun classification into `performance` loss type.
- **MO blocking:** Manufacturing order cannot advance to `to_close` until ALL workorders are `done` or `cancel` (`mrp_production.py:594`).
- **Workorder generation:** `_compute_workorder_ids()` generates workorders from BOM operation lines during draft state; `_link_workorders_and_moves()` wires up sequential or dependency-based blocking chains.
- **No quality integration:** No `quality_control` dependency or quality step model found in Community mrp; that belongs to the Enterprise `mrp_workorder` addon.
