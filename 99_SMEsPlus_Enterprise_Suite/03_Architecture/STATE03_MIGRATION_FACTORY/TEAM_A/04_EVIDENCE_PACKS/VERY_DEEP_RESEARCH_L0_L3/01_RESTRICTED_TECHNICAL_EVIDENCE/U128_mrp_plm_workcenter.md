# U128 Restricted Technical Evidence — mrp_plm + mrp_workcenter

**Unit ID:** U128  
**Title:** mrp_plm / mrp_workcenter — ECO presence check + workcenter capacity depth  
**G Group:** G07  
**Priority:** P2  
**Researcher:** DeepSeek Worker (Claude Sonnet 4.6)  
**Date:** 2026-10-02  
**Branch:** claude/local-odoo-source-research  

---

## 1. mrp_plm Presence Check

**Result: ABSENT**

Directory `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_plm` does not exist.

`mrp_plm` is an Odoo Enterprise module that provides Engineering Change Orders (ECO), BOM versioning, and PLM workflow. It is not shipped in the Community edition.

---

## 2. mrp_workcenter Depth Study

`mrp_workcenter` is not a standalone module. All workcenter models are defined inside `mrp/models/mrp_workcenter.py`.

**Source file:** `mrp/models/mrp_workcenter.py`

**Models defined:**
- `mrp.workcenter` (line 21) — inherits `mail.thread`, `resource.mixin`
- `mrp.workcenter.tag` (line 440)
- `mrp.workcenter.productivity.loss.type` (line 457)
- `mrp.workcenter.productivity.loss` (line 477)
- `mrp.workcenter.productivity` (line 504)
- `mrp.workcenter.capacity` (line 613)

---

## 3. VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U128-C001 | F-PLM-ABSENT-01 | mrp_plm — module directory | directory not present | ABSENT | mrp_plm module not in Community addons | GAP | `mrp_plm` module directory absent at `odoo/addons/mrp_plm`; ECO model `mrp.eco`, BOM versioning, and PLM approval workflow are Enterprise-only features | Engineering change order management module is absent from Community edition |
| U128-C002 | F-PLM-ABSENT-02 | mrp_plm — mrp.eco model | no source file | ABSENT | mrp.eco not present in Community | GAP | `mrp.eco` model (ECO state machine: new→confirmed→done), `_apply_rerouting` method, and responsible-user assignment are unavailable in Community | Engineering change order record with state transitions is absent from Community edition |
| U128-C003 | F-PLM-ABSENT-03 | mrp_plm — BOM versioning | no source file | ABSENT | mrp_plm BOM versioning absent | GAP | BOM version control via `mrp_plm` (active toggle on BOM lines, ECO attachment) is absent; only a single active BOM per product is maintained in Community | Bill of materials version management linked to change orders is absent from Community edition |
| U128-C004 | F-PLM-ABSENT-04 | mrp_plm — ECO type/stages | no source file | ABSENT | mrp.eco.type not present in Community | GAP | `mrp.eco.type` model with approval stages and stage routing is absent; no multi-stage PLM approval workflow in Community | Engineering change order approval stage configuration is absent from Community edition |
| U128-C005 | F-PLM-ABSENT-05 | mrp_plm — ECO responsible | no source file | ABSENT | ECO responsible user assignment absent | GAP | Responsible-user assignment, reviewer routing, and activity-based approval on ECOs is absent from Community | Change order responsible-user and reviewer assignment workflow is absent from Community edition |
| U128-C006 | F-WC-MODEL-01 | mrp/models/mrp_workcenter.py:21-26 | `class MrpWorkcenter` | C1 | mrp module installed | C1 | `mrp.workcenter` inherits `mail.thread` and `resource.mixin`; `_order = "sequence, id"`; `_check_company_auto = True`; resource type forced to `material` on create (line 299) | Work centre model with messaging, resource calendar integration, and company isolation |
| U128-C007 | F-WC-FIELDS-01 | mrp/models/mrp_workcenter.py:30 | `time_efficiency` field | C1 | mrp module installed | C1 | `time_efficiency` (Float) related to `resource_id.time_efficiency`, default 100; used as divisor in `_get_duration_expected` formula: `setup + cleanup + cycle_number * time_cycle * 100.0 / time_efficiency` (mrp_workorder.py:836) | Work centre time-efficiency percentage used to scale expected work order duration |
| U128-C008 | F-WC-FIELDS-02 | mrp/models/mrp_workcenter.py:42-43 | `time_start`, `time_stop` | C1 | mrp module installed | C1 | `time_start` (Float, Setup Time) and `time_stop` (Float, Cleanup Time) define fixed per-operation overhead minutes added to expected duration in `_get_duration_expected` | Work centre setup and cleanup time overhead fields added to each work order expected duration |
| U128-C009 | F-WC-FIELDS-03 | mrp/models/mrp_workcenter.py:65 | `oee_target` field | C1 | mrp module installed | C1 | `oee_target` (Float, default 90) stores the target OEE percentage; compared against computed `oee` field for dashboard display | Work centre OEE target percentage for overall equipment effectiveness benchmarking |
| U128-C010 | F-WC-OEE-01 | mrp/models/mrp_workcenter.py:244-267 | `_compute_oee` method | C1 | mrp module installed, productivity logs exist | C1 | OEE computed as `productive_time * 100.0 / (productive_time + blocked_time)` grouping `mrp.workcenter.productivity` records by `loss_type` over the last 30 days | Overall equipment effectiveness calculation from 30-day productive and blocked time logs |
| U128-C011 | F-WC-OEE-02 | mrp/models/mrp_workcenter.py:269-280 | `_compute_performance` method | C1 | mrp module installed | C1 | Performance computed as `100 * duration_expected_sum / duration_sum` for done work orders in last 30 days per workcenter | Work centre performance percentage comparing expected versus actual duration over trailing 30 days |
| U128-C012 | F-WC-STATE-01 | mrp/models/mrp_workcenter.py:54-57 | `working_state` field | C1 | mrp module installed | C1 | `working_state` Selection: normal / blocked / done; computed from open `mrp.workcenter.productivity` records; `loss_type` in ('productive','performance') → done; any other open log → blocked; no open log → normal | Real-time work centre status derived from open productivity log entries |
| U128-C013 | F-WC-CAPACITY-01 | mrp/models/mrp_workcenter.py:78-79 | `capacity_ids` field | C1 | mrp module installed | C1 | `capacity_ids` One2many to `mrp.workcenter.capacity`; stores product-specific parallel-production piece counts; used by `_get_capacity` to select matching capacity record by product and UOM | Work centre product-specific parallel capacity configuration for concurrent production planning |
| U128-C014 | F-WC-CAPACITY-02 | mrp/models/mrp_workcenter.py:427-437 | `_get_capacity` method | C1 | mrp module installed | C1 | `_get_capacity(product, unit, default_capacity=1)` returns tuple `(capacity, time_start, time_stop)`; priority: exact product+UOM match → product-agnostic UOM match → global defaults; zero capacity treated as `default_capacity` | Work centre capacity lookup method returning parallel pieces, setup time, and cleanup time for a given product |
| U128-C015 | F-WC-SCHED-01 | mrp/models/mrp_workcenter.py:339-408 | `_get_first_available_slot` method | C1 | mrp module installed | C1 | Forward/backward scheduling up to 700 days (50 × 14-day chunks); uses `resource_calendar_id._work_intervals_batch` for working hours and `_leave_intervals_batch` for existing work order conflicts; returns `(start_datetime, end_datetime)` or `(False, error_message)` | Work centre first-available-slot scheduling algorithm with forward and backward modes up to 700 days |
| U128-C016 | F-WC-SCHED-02 | mrp/models/mrp_workcenter.py:355-357 | `max_planning_iterations` config | C1 | mrp module installed | C1 | `ir.config_parameter` key `mrp.workcenter_max_planning_iterations` (default 50) controls planning horizon; `max(int(ICP.get_param(...,'50')), 1)` prevents zero-iteration edge case | Configurable work centre planning iteration limit controlling maximum scheduling horizon |
| U128-C017 | F-WC-ALT-01 | mrp/models/mrp_workcenter.py:68-76 | `alternative_workcenter_ids` field | C1 | mrp module installed | C1 | Many2many self-referential relation `mrp_workcenter_alternative_rel`; domain restricts to same company; `_check_alternative_workcenter` prevents self-referential assignment | Work centre alternative workcenter links for capacity dispatch and load balancing |
| U128-C018 | F-WC-PROD-01 | mrp/models/mrp_workcenter.py:504-610 | `MrpWorkcenterProductivity` model | C1 | mrp module installed | C1 | `mrp.workcenter.productivity` records time intervals (`date_start`, `date_end`) per work order; `duration` computed from `loss_id._convert_to_duration` which applies calendar-based duration for non-productive losses; `_close` auto-creates performance-loss records when `duration > duration_expected` | Work centre productivity time log model recording productive, blocked, and performance-loss intervals |
| U128-C019 | F-WC-PROD-02 | mrp/models/mrp_workcenter.py:477-501 | `MrpWorkcenterProductivityLoss` model | C1 | mrp module installed | C1 | `mrp.workcenter.productivity.loss` with `loss_type` Selection: availability/performance/quality/productive; `_convert_to_duration` applies working-hours calendar for availability/quality losses; raw elapsed time for productive/performance losses | Productivity loss reason model with four effectiveness categories and calendar-aware duration conversion |
| U128-C020 | F-WC-GRAPH-01 | mrp/models/mrp_workcenter.py:96-166 | `_compute_kanban_dashboard_graph` method | C1 | mrp module installed | C1 | Kanban dashboard graph shows 5-week window (−1 to +4 weeks); computes `duration_expected:sum` per workcenter per week; compares load against `resource_calendar_id.attendance_ids` total hours; excess load rendered separately | Work centre kanban dashboard load graph covering a five-week rolling window with capacity excess detection |
| U128-C021 | F-WO-DURATION-01 | mrp/models/mrp_workorder.py:811-836 | `_get_duration_expected` method | C1 | mrp module installed | C1 | Formula: `setup + cleanup + cycle_number * time_cycle * 100.0 / time_efficiency`; `cycle_number = ceil(qty_production / capacity)`; for alternative workcenter, recalculates cycle_number with new capacity; also handles no-operation case with qty_ratio scaling | Work order expected duration formula combining setup, cleanup, cycle count, operation time, and efficiency |
| U128-C022 | F-WO-STATE-01 | mrp/models/mrp_workorder.py:66-73 | `state` field Selection | C1 | mrp module installed | C1 | Work order states: blocked→ready→progress→done/cancel; `_compute_state` derives blocked/ready from `qty_ready`; `button_start` (line 656) transitions to progress; `button_finish` (line 705) transitions to done | Work order five-state lifecycle from blocked through completion or cancellation |
| U128-C023 | F-WO-SCHED-01 | mrp/models/mrp_workorder.py:456-481 | `_calculate_date_finished`, `_calculate_duration_expected` | C1 | mrp module installed | C1 | `_calculate_date_finished` calls `resource_calendar_id.plan_hours` with leave domain `['leave','other']`; `_calculate_duration_expected` calls `get_work_duration_data` with same domain; both fall back to naive timedelta when no calendar is set | Work order calendar-aware date and duration calculation methods integrating resource leaves |
| U128-C024 | F-ROUTING-01 | mrp/models/mrp_routing.py:9-142 | `MrpRoutingWorkcenter` model | C1 | mrp module installed | C1 | `mrp.routing.workcenter` links BOM to workcenter; `time_mode` Selection: manual/auto; `time_cycle` computed from last N done work orders when mode=auto; `time_total = setup + cleanup + cycle_number * time_cycle * 100 / time_efficiency`; supports operation dependencies via `blocked_by_operation_ids` | Routing operation model connecting bill of materials to work centre with fixed or computed cycle time |
| U128-C025 | F-ROUTING-02 | mrp/models/mrp_routing.py:47-56 | operation dependency fields | C1 | mrp module installed, `allow_operation_dependencies` enabled | C1 | `blocked_by_operation_ids` and `needed_by_operation_ids` Many2many on `mrp.routing.workcenter`; `_check_no_cyclic_dependencies` prevents cycles; mirrors work-order-level dependencies at BOM definition level | Routing operation dependency graph preventing cyclic operation sequences in bill of materials |

---

## 4. Summary

- **mrp_plm:** ABSENT from Community edition. ECO workflow, BOM versioning, and PLM approval stages are Enterprise-only. Migration to SMEsPlus requires either Enterprise licensing or custom development of change-order capability.
- **mrp_workcenter:** Fully present in Community via `mrp` module. Capacity scheduling (`_get_first_available_slot`), OEE calculation, productivity tracking, alternative workcenters, and product-specific capacity configuration are all C1-proven from source.
- **Duration formula:** `setup + cleanup + ceil(qty / capacity) * time_cycle * 100 / time_efficiency` — all components present and verified at mrp_workorder.py:836 and mrp_routing.py:121.
- **Total claims:** 25 (5 ABSENT, 20 C1)
