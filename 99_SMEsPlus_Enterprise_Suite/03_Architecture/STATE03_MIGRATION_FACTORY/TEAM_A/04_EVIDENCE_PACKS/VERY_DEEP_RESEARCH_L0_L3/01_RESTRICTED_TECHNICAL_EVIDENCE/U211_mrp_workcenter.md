# U211 — mrp_workcenter: Work Center Model, Capacity, OEE, Routing Operations on BOM (v19)

**Unit**: U211  
**Module**: mrp_workcenter  
**Research date**: 2026-10-02  
**Source tree**: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp`  
**Gate**: GREEN

---

## 1. Primary Source SHAs

| File | SHA-256 |
|------|---------|
| models/mrp_workcenter.py | `1e68a9ce1b7f3196cf83bc233ebf5380e66b64acdb8c55c44cd1c697a009daeb` |
| models/mrp_routing.py    | `39e560647e5a12c1cb313bd04d6dd793d28a15e45fdc5a1d061d6e9392c44019` |
| models/mrp_workorder.py  | `32b6d06e0de87c5a32a0b4018a0a32dc6f9365f0719a1153a8857848cbe60701` |

---

## 2. Migration Flags

### FLAG-1: `mrp.routing` standalone model — REMOVED
`grep -rn "class MrpRouting\b\|_name = 'mrp.routing'" addons/mrp/` returns **no results**. The dedicated `mrp.routing` model that existed in Odoo v14/v15/v16 (which held a named routing that could be reused across multiple BOMs) is **absent** in v19. There is no `mrp/models/mrp_routing_model.py` or any class declaring `_name = 'mrp.routing'`.

### FLAG-2: `mrp.routing.workcenter` — STILL PRESENT, but restructured
The model `mrp.routing.workcenter` (`models/mrp_routing.py:9`) continues to exist in v19, but:
- Field `bom_id = fields.Many2one('mrp.bom', ...)` is now **required** (`required=True`) and has `ondelete='cascade'` (line 23–25).
- There is **no** `routing_id` field anywhere in the model. Operations are bound directly to a BOM, not to a shared routing entity.
- The model was **not renamed** to `mrp.bom.operation`; it keeps the technical name `mrp.routing.workcenter` but semantically represents a BOM-level operation.

### FLAG-3: `routing_id` — REMOVED from `mrp.bom` and `mrp.production`
`grep -n "routing_id" models/mrp_bom.py` and `models/mrp_production.py` return **no results**. Both files have no `routing_id` field.

### FLAG-4: `capacity` scalar field — REPLACED by `capacity_ids` One2many
No simple `capacity = fields.Float(...)` exists on `mrp.workcenter`. Instead, `capacity_ids = fields.One2many('mrp.workcenter.capacity', 'workcenter_id', ...)` (line 78) links to the new `mrp.workcenter.capacity` model which supports per-product, per-UOM capacity entries.

---

## 3. `mrp.workcenter` Model Fields (mrp_workcenter.py)

| Field | Type | Line | Notes |
|-------|------|------|-------|
| `name` | Char | 29 | related to `resource_id.name`, stored |
| `time_efficiency` | Float | 30 | related to `resource_id.time_efficiency`, default 100 |
| `active` | Boolean | 31 | related to `resource_id.active` |
| `code` | Char | 33 | copy=False |
| `sequence` | Integer | 38 | default 1 |
| `costs_hour` | Float | 41 | tracking=True |
| `time_start` | Float | 42 | Setup Time (minutes) |
| `time_stop` | Float | 43 | Cleanup Time (minutes) |
| `routing_line_ids` | One2many → mrp.routing.workcenter | 44 | inverse of operation.workcenter_id |
| `oee_target` | Float | 65 | default 90 (percent) |
| `oee` | Float (computed) | 64 | `_compute_oee()` |
| `blocked_time` | Float (computed) | 58–60 | hours, last month |
| `productive_time` | Float (computed) | 61–63 | hours, last month |
| `performance` | Integer (computed) | 66 | last month |
| `workcenter_load` | Float (computed) | 67 | computed inside `_compute_workorder_count()` |
| `alternative_workcenter_ids` | Many2many → mrp.workcenter | 68–76 | self-referential m2m, same table |
| `tag_ids` | Many2many → mrp.workcenter.tag | 77 | new in post-v16 |
| `capacity_ids` | One2many → mrp.workcenter.capacity | 78–79 | per-product capacity entries |
| `resource_calendar_id` | Many2one → resource.calendar | 81 | check_company=True |
| `working_state` | Selection | 54–57 | `normal/blocked/done`, stored |

`mrp.workcenter` inherits `['mail.thread', 'resource.mixin']` (line 25–26). The `resource.mixin` supplies `resource_id` and `resource_calendar_id`.

---

## 4. `mrp.workcenter.capacity` Model (lines 613–646)

New model replacing a simple capacity float. Fields:

| Field | Type | Notes |
|-------|------|-------|
| `workcenter_id` | Many2one → mrp.workcenter | required, indexed |
| `product_id` | Many2one → product.product | optional; if absent applies to all products |
| `product_uom_id` | Many2one → uom.uom | computed from product, stored |
| `capacity` | Float | pieces in parallel; 0 means fallback to default |
| `time_start` | Float | per-product setup minutes |
| `time_stop` | Float | per-product cleanup minutes |

Unique index: `(workcenter_id, COALESCE(product_id, 0), product_uom_id)` (line 638–640).

`_get_capacity(product, unit, default_capacity=1)` at line 427 resolves priority: exact product+uom > no-product+unit > no-product+product uom > fallback to `(default_capacity, self.time_start, self.time_stop)`.

---

## 5. `mrp.routing.workcenter` (Operations) in v19 (mrp_routing.py)

Class declaration: `mrp_routing.py:9` — `_name = 'mrp.routing.workcenter'`

Key fields:

| Field | Type | Line | Notes |
|-------|------|------|-------|
| `name` | Char | 17 | Operation name, required |
| `active` | Boolean | 18 | default True |
| `workcenter_id` | Many2one → mrp.workcenter | 19 | required, check_company, tracking |
| `bom_id` | Many2one → mrp.bom | 23–25 | **required**, ondelete='cascade', index |
| `sequence` | Integer | 20–22 | default 100 |
| `time_mode` | Selection | 27–30 | `manual`/`auto` |
| `time_cycle_manual` | Float | 33–37 | minutes; default 60 |
| `time_cycle` | Float (computed) | 38 | `_compute_time_cycle()` |
| `blocked_by_operation_ids` | Many2many → mrp.routing.workcenter | 47–51 | operation-level dependencies |
| `needed_by_operation_ids` | Many2many → mrp.routing.workcenter | 52–56 | inverse of above |
| `cycle_number` | Integer (computed) | 57 | qty / capacity, rounded UP |
| `time_total` | Float (computed) | 58 | setup + cleanup + cycle_number * time_cycle / efficiency |
| `cost_mode` | Selection | 60–64 | `actual`/`estimated` |
| `cost` | Float (computed) | 65 | `(time_total/60) * workcenter.costs_hour` |

`_compute_time_cycle()` (lines 77–122): in `auto` mode, pulls last N done workorders, sums duration / effective cycle_number. In `manual` mode, returns `time_cycle_manual` directly.

Operations on BOM: `mrp.bom.operation_ids = One2many('mrp.routing.workcenter', 'bom_id', ...)` at `mrp_bom.py:51`.

---

## 6. OEE Computation (`_compute_oee`, mrp_workcenter.py:245–267)

```
oee = productive_time * 100.0 / (productive_time + blocked_time)
```

- Reads `mrp.workcenter.productivity` records from the last month (`date_start >= now - 1 month`) with `date_end != False`.
- Groups by `workcenter_id` and `loss_type`.
- `loss_type == 'productive'` → adds to `productive_time`.
- Any other `loss_type` → adds to `blocked_time`.
- If `productive_time == 0`, `oee = 0.0`.
- Source: lines 245–267.

---

## 7. Work Center Load Computation (`_compute_workorder_count`, lines 168–192)

`workcenter_load` = sum of `duration_expected` for workorders in states `('blocked', 'ready', 'progress')`.

```python
result_duration_expected[workcenter.id] += duration_sum  # for state in ('blocked','ready','progress')
workcenter.workcenter_load = result_duration_expected[workcenter.id]
```

Source: `mrp_workcenter.py:168–192`. `workcenter_load` is in **minutes** (same unit as `duration_expected` on `mrp.workorder`).

---

## 8. `mrp.workorder` Model (mrp_workorder.py)

| Field | Type | Line | Notes |
|-------|------|------|-------|
| `name` | Char | 31 | required |
| `workcenter_id` | Many2one → mrp.workcenter | 35–37 | required, index, check_company |
| `operation_id` | Many2one → mrp.routing.workcenter | 102–103 | index btree_not_null |
| `production_id` | Many2one → mrp.production | 44 | required, index btree |
| `state` | Selection | 66–73 | `blocked/ready/progress/done/cancel` |
| `date_start` | Datetime (computed+stored) | 78–82 | via leave_id |
| `date_finished` | Datetime (computed+stored) | 83–87 | via leave_id |
| `duration_expected` | Float (computed+stored) | 88–90 | minutes, `_compute_duration_expected()` |
| `duration` | Float (computed+stored) | 91–93 | minutes, actual |
| `leave_id` | Many2one → resource.calendar.leaves | 74–77 | slot in workcenter calendar |
| `time_ids` | One2many → mrp.workcenter.productivity | 118–119 | time tracking logs |
| `blocked_by_workorder_ids` | Many2many → mrp.workorder | 142–145 | workorder-level dependencies |

State machine (`_compute_state`, lines 152–160): transitions between `blocked` and `ready` driven by `qty_ready > 0`. Transitions to `progress` via `button_start()`, to `done` via `action_mark_as_done()`, to `cancel` via `action_cancel()`.

---

## 9. `_get_duration_expected()` (mrp_workorder.py:811–836)

Formula when `operation_id` is set:

```
duration_expected = setup + cleanup + cycle_number * time_cycle * 100.0 / time_efficiency
```

Where:
- `(capacity, setup, cleanup) = workcenter._get_capacity(product, product_uom_id, bom.product_qty or 1)`
- `cycle_number = ceil(qty_production / capacity)` (rounded UP)
- `time_cycle = operation_id.time_cycle`
- `time_efficiency = workcenter.time_efficiency` (default 100)

When `operation_id` is absent (manual workorder): scales existing `duration_expected` by qty ratio and efficiency.

---

## 10. `mrp.production` → `workorder_ids` Creation from BOM Operations

`_compute_workorder_ids()` at `mrp_production.py:606–660`:

1. Explodes BOM via `bom_id.explode(...)`.
2. For each `bom` in exploded set that has `operation_ids` and is not a duplicate phantom bom:
   - For each `operation` in `bom.operation_ids`:
     - Skips if `operation._skip_operation_line(product, ...)` returns True.
     - Creates `mrp.workorder` with: `name=operation.name`, `workcenter_id=operation.workcenter_id`, `operation_id=operation.id`, `state='ready'`.
3. Source: `mrp_production.py:630–657`.

---

## 11. `mrp.workcenter.tag` Model (mrp_workcenter.py:440–454)

```python
class MrpWorkcenterTag(models.Model):
    _name = 'mrp.workcenter.tag'
    name = fields.Char("Tag Name", required=True)
    color = fields.Integer("Color Index", default=_get_default_color)  # randint(1, 11)
```

Unique constraint on `name`. Referenced from `mrp.workcenter.tag_ids` (Many2many, line 77).

---

## 12. Scheduling: `_get_first_available_slot()` (mrp_workcenter.py:339–408)

Method on `mrp.workcenter`. Parameters: `start_datetime, duration (minutes), forward=True, leaves_to_ignore=False, extra_leaves_slots=[]`.

- Iterates up to `max_planning_iterations` (default 50, configurable via `ir.config_parameter` `mrp.workcenter_max_planning_iterations`) × 14-day windows = 700 days.
- Uses `resource_calendar_id._work_intervals_batch()` for available time and `resource_calendar_id._leave_intervals_batch(domain=[('time_type','=','other')])` for workorder-occupied slots.
- Returns `(start_datetime, end_datetime)` or `(False, 'error message')`.
- Source: lines 339–408.

---

## 13. Workorder Scheduling via `leave_id`

`mrp.workorder.date_start` and `date_finished` are computed from `leave_id.date_from` / `date_to` (lines 271–274). When `date_start` is set without a `leave_id`, `_set_dates()` creates a `resource.calendar.leaves` record with `time_type='other'` on the workcenter's calendar (lines 286–296). This is the mechanism by which scheduled workorders block time on the workcenter.

---

## 14. Summary of Architecture Change vs. v16

| Aspect | v16 (old) | v19 (current) |
|--------|-----------|---------------|
| `mrp.routing` model | Present (shared routing entity) | **REMOVED** |
| `routing_id` on mrp.bom | Present | **REMOVED** |
| `routing_id` on mrp.production | Present | **REMOVED** |
| Operations model | `mrp.routing.workcenter` with `routing_id` FK | `mrp.routing.workcenter` with `bom_id` FK (required, cascade) |
| BOM operations field | via `routing_id` → `mrp.routing.operation_ids` | direct `mrp.bom.operation_ids` |
| Capacity | Simple `capacity = Float` on workcenter | `capacity_ids = One2many → mrp.workcenter.capacity` (per-product) |
| Tags | Absent or minimal | `tag_ids = Many2many → mrp.workcenter.tag` |
