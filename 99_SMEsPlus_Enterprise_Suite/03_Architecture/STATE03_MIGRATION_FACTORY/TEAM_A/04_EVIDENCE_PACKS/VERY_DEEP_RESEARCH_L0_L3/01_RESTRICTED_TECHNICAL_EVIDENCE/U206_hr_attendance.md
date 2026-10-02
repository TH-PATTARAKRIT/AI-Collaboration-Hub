# U206 — hr_attendance: Restricted Technical Evidence
**Unit:** U206  
**Module:** hr_attendance  
**Source tree:** `odoo-19.0.post20260921/odoo/addons/hr_attendance`  
**Research date:** 2026-10-02  
**Gate:** GREEN

---

## 1. Module Overview

- **Manifest version:** `2.0` — `/addons/hr_attendance/__manifest__.py:6`
- **Dependencies:** `hr`, `barcodes`, `base_geolocalize`
- **License:** LGPL-3
- **Post-install hook:** `post_init_hook` (initialises default ruleset data)
- **Python models:** `hr.attendance`, `hr.attendance.overtime.line`, `hr.attendance.overtime.rule`, `hr.attendance.overtime.ruleset`, `hr.version` (extended), `hr.employee` (extended), `hr.employee.public` (extended), `res.company` (extended), `res.config.settings` (extended)

---

## 2. `hr.attendance` Model — Full Field Inventory

**Source:** `/addons/hr_attendance/models/hr_attendance.py`

| Field | Type | Key attributes | Line |
|---|---|---|---|
| `employee_id` | Many2one → `hr.employee` | required, ondelete=cascade, index=True, group_expand | 37–38 |
| `department_id` | Many2one → `hr.department` | related employee_id.department_id, readonly | 39–40 |
| `manager_id` | Many2one → `hr.employee` | related employee_id.parent_id, readonly | 41–42 |
| `attendance_manager_id` | Many2one → `res.users` | related employee_id.attendance_manager_id | 43–44 |
| `is_manager` | Boolean | compute=_compute_is_manager | 45 |
| `check_in` | Datetime | required, default=now, tracking=True, index=True | 46 |
| `check_out` | Datetime | optional (NULL = open), tracking=True | 47 |
| `date` | Date | compute=_compute_date, store=True, index=True, precompute=True, required | 48 |
| `worked_hours` | Float | compute=_compute_worked_hours, store=True, readonly | 49 |
| `color` | Integer | compute=_compute_color | 50 |
| `overtime_hours` | Float | compute=_compute_overtime_hours, store=True | 51 |
| `overtime_status` | Selection | to_approve/approved/refused, compute+store+tracking, readonly=False | 52–54 |
| `validated_overtime_hours` | Float | compute=_compute_validated_overtime_hours, store+tracking, readonly | 55 |
| `expected_hours` | Float | compute=_compute_expected_hours, store, aggregator=sum | 80 |
| `in_latitude` | Float | digits=(10,7), readonly, aggregator=None | 56 |
| `in_longitude` | Float | digits=(10,7), readonly, aggregator=None | 57 |
| `in_location` | Char | GPS or IP-derived | 58 |
| `in_ip_address` | Char | readonly | 59 |
| `in_browser` | Char | readonly | 60 |
| `in_mode` | Selection | kiosk/systray/manual/technical, readonly, default=manual | 61–67 |
| `out_latitude` | Float | digits=(10,7), readonly, aggregator=None | 68 |
| `out_longitude` | Float | digits=(10,7), readonly, aggregator=None | 69 |
| `out_location` | Char | GPS or IP-derived | 70 |
| `out_ip_address` | Char | readonly | 71 |
| `out_browser` | Char | readonly | 72 |
| `out_mode` | Selection | kiosk/systray/manual/technical/**auto_check_out**, readonly, default=manual | 73–79 |
| `device_tracking_enabled` | Boolean | related employee_id.company_id.attendance_device_tracking | 81 |
| `linked_overtime_ids` | Many2many → `hr.attendance.overtime.line` | compute=_compute_linked_overtime_ids, readonly=False | 82 |

**NOT PRESENT (migration flags):**
- No `hr_attendance_reason_ids` field — not in Community 19
- No `out_reason_id` field — not in Community 19
- No direct `company_id` field — accessed via `employee_id.company_id`

---

## 3. `_compute_worked_hours` — Formula

**Source:** `/addons/hr_attendance/models/hr_attendance.py:162–195`

```
_compute_worked_hours:
  if check_out AND check_in AND employee_id:
      worked_hours = _get_worked_hours_in_range(check_in, check_out)
  else:
      worked_hours = False   # NULL stored when check_out is missing
```

**`_get_worked_hours_in_range(start_dt, end_dt)`** — lines 173–195:

1. Resolves `calendar` via `_get_employee_calendar()` (employee calendar or company calendar)
2. Converts start/end to employee TZ
3. If `check_out < check_in` in TZ → return 0.0
4. **Flexible calendar:** `lunch_intervals = []` (no deduction)
5. **Fixed calendar:** `lunch_intervals = employee._employee_attendance_intervals(start, end, lunch=True)`
6. Final: `sum_intervals(Intervals([(start_tz, end_tz, self)]) - lunch_intervals)`

Key: `worked_hours` is **duration minus lunch breaks** for fixed schedules, **raw duration** for flexible schedules. Unit is **decimal hours** (float).

---

## 4. Open Attendance Detection (NULL check_out)

- `check_out = False` (NULL) means employee is currently **checked in** (open record)
- `_compute_worked_hours` line 171: returns `False` (not 0) when `check_out` is missing
- `_compute_color` line 100–103: open record → color=1 if check_in older than 24h; color=10 if recent
- `_compute_display_name` line 137–141: "From %s" format (no check_out)
- `attendance_state` on employee: `'checked_in'` when `last_attendance_id.check_out` is False

**`_check_validity` constraint** (lines 205–246): enforces max 1 open attendance per employee. If a second open record is attempted → `ValidationError("the employee hasn't checked out since...")`

**`_cron_auto_check_out`** (lines 601–658): company setting `auto_check_out=True` triggers nightly cron. Logic: if `current_duration + previous_worked - tolerance > expected_worked_hours` then auto-close at end of working day with `out_mode='auto_check_out'`.

**`action_archive` on hr.employee** (`hr_employee.py:82–92`): when employee is archived, any open attendance is auto-closed at `fields.Datetime.now()`.

---

## 5. Overtime in Community v19

**MAJOR ARCHITECTURE CHANGE vs v16/v17:**

v19 Community uses a fully new overtime engine with three models:

### 5a. `hr.attendance.overtime.line` — `/addons/hr_attendance/models/hr_attendance_overtime.py`

| Field | Type | Details | Line |
|---|---|---|---|
| `employee_id` | Many2one → hr.employee | required, ondelete=cascade | 12–14 |
| `company_id` | Many2one | related employee_id.company_id | 15 |
| `date` | Date | index, required | 17 |
| `status` | Selection | to_approve/approved/refused, compute+stored+readonly=False | 18–25 |
| `duration` | Float | Extra Hours (computed by ruleset engine) | 27 |
| `manual_duration` | Float | Extra Hours (encoded) — manager can override | 27–31 |
| `time_start` | Datetime | = attendance.check_in (links to attendance) | 33 |
| `time_stop` | Datetime | = attendance.check_out | 34 |
| `amount_rate` | Float | Overtime pay rate, default=1.0 | 35 |
| `rule_ids` | Many2many → hr.attendance.overtime.rule | Applied rules | 39 |

**DB constraint:** `_overtime_start_before_end` CHECK(time_stop > time_start) — line 56–59

**NOTE:** The GIST exclusion constraint (no overlapping overtimes) is commented out (lines 48–55) — not active in v19.

**Status logic** (`_compute_status` line 62–65): if company `attendance_overtime_validation == 'by_manager'` → `'to_approve'`; else → `'approved'`

### 5b. `hr.attendance.overtime.ruleset` — `/addons/hr_attendance/models/hr_attendance_overtime_ruleset.py`

- `name`, `description`, `rule_ids`, `company_id`, `country_id`, `rate_combination_mode` (max/sum), `active`
- `rate_combination_mode`: max = highest rate wins; sum = additive extra percentages

### 5c. `hr.attendance.overtime.rule` — `/addons/hr_attendance/models/hr_attendance_overtime_rule.py`

Two computation modes:
1. **`quantity`**: overtime = worked hours - expected hours (per day or week). Expected hours from contract (`expected_hours_from_contract=True`) or fixed (`expected_hours`). Tolerances: `employer_tolerance`, `employee_tolerance`.
2. **`timing`**: overtime on specific timing types: work_days / non_work_days / leave / schedule (outside a fixed calendar).

Fields: `base_off`, `timing_type`, `timing_start`, `timing_stop`, `resource_calendar_id`, `expected_hours`, `quantity_period` (day/week), `paid`, `amount_rate`.

### 5d. Link to `hr.attendance`

- `overtime_hours` on `hr.attendance` = `sum(linked_overtime_ids.mapped('duration'))` — line 119–120
- `validated_overtime_hours` = sum of approved lines `manual_duration` — line 123–125
- `overtime_status` derived from statuses of all linked overtime lines — lines 106–115
- `expected_hours` = `worked_hours - overtime_hours` — line 93–96
- Overtime recalculated on `create`, `write` (when employee_id/check_in/check_out change), `unlink`

### 5e. Key compute method: `_update_overtime` (lines 322–368)

- Deletes all affected `hr.attendance.overtime.line` records
- Re-creates them using `ruleset.rule_ids._generate_overtime_vals_v2(...)`
- Called on every attendance create/write/unlink affecting check_in or check_out

---

## 6. `_check_validity` Constraint — Overlap Prevention

**Source:** `/addons/hr_attendance/models/hr_attendance.py:205–246`

Two separate `@api.constrains` decorators:

**Constraint 1: `_check_validity_check_in_check_out`** (lines 197–203)
- Raises ValidationError if `check_out < check_in`

**Constraint 2: `_check_validity`** (lines 205–246)
- Per attendance: checks `last_attendance_before_check_in` — if that record has `check_out > new check_in` → overlap error
- If `check_out = False` (open): searches for any other open record (no check_out) for same employee → error if found
- If `check_out` present: verifies that last record before `check_out` == last record before `check_in` (no records between them)

---

## 7. Kiosk Mode

**Controller:** `/addons/hr_attendance/controllers/main.py`

- **URL pattern:** `/hr_attendance/{token}` where token = `company.attendance_kiosk_key` (UUID hex)
- **Auth:** public (no login required for kiosk)
- **Barcode scan:** `/hr_attendance/attendance_barcode_scanned` — matches `employee.barcode` field; calls `_attendance_action_change()` — line 193–201
- **Manual selection with PIN:** `/hr_attendance/manual_selection` — line 203–211: validates `employee.pin == pin_code` when `company.attendance_kiosk_use_pin = True`
- **Kiosk modes on company:** `barcode`, `barcode_manual`, `manual` (see `res.company.attendance_kiosk_mode`)
- **No `hr.attendance.kiosk` model** — kiosk is purely a controller + frontend JS app

**Company kiosk settings** (`res_company.py:21–43`):
- `attendance_kiosk_mode`: barcode/barcode_manual/manual
- `attendance_barcode_source`: scanner/front/back camera
- `attendance_kiosk_delay`: Integer (seconds)
- `attendance_kiosk_key`: UUID hex, company-specific token
- `attendance_kiosk_use_pin`: Boolean — enables PIN verification at kiosk
- `attendance_from_systray`: Boolean
- `attendance_device_tracking`: Boolean — enables GPS/IP capture

---

## 8. Multi-Company

- **No `company_id` field directly on `hr.attendance`** — company is derived via `employee_id.company_id`
- `device_tracking_enabled` is a related field on attendance: `employee_id.company_id.attendance_device_tracking` — line 81
- `hr.attendance.overtime.line.company_id`: related via `employee_id.company_id` — line 15
- `hr.attendance.overtime.ruleset.company_id`: direct Many2one — line 13
- `hr.attendance.overtime.rule.company_id`: related via `ruleset_id.company_id` — line 124
- `_cron_auto_check_out`: iterates `to_verify.employee_id.company_id` per-company — line 628
- `_read_group_employee_id`: filters by `company_id in allowed_company_ids` — line 573

---

## 9. `hr.employee` Extensions (hr_attendance module)

**Source:** `/addons/hr_attendance/models/hr_employee.py`

| Field | Type | Notes | Line |
|---|---|---|---|
| `attendance_manager_id` | Many2one → res.users | Attendance Approver; grants officer group on set | 13–18 |
| `attendance_ids` | One2many → hr.attendance | groups=officer,hr_user | 19–20 |
| `last_attendance_id` | Many2one → hr.attendance | computed+stored | 21–23 |
| `last_check_in` | Datetime | related last_attendance_id.check_in, stored | 24–26 |
| `last_check_out` | Datetime | related last_attendance_id.check_out, stored | 27–29 |
| `attendance_state` | Selection | checked_in/checked_out, computed | 30–33 |
| `hours_last_month` | Float | computed — current month to today | 34 |
| `hours_last_month_overtime` | Float | validated overtime in current month | 35 |
| `hours_today` | Float | computed live | 36–38 |
| `hours_previously_today` | Float | today hours before current session | 39–41 |
| `last_attendance_worked_hours` | Float | worked hours in last attendance | 42–44 |
| `hours_last_month_display` | Char | formatted string | 45–46 |
| `overtime_ids` | One2many → hr.attendance.overtime.line | groups=officer,hr_user | 47–48 |
| `total_overtime` | Float | sum of approved manual_duration | 49 |
| `display_extra_hours` | Boolean | related company_id.hr_attendance_display_overtime | 50 |
| `ruleset_id` | Many2one | related version_id.ruleset_id, groups=hr_manager | 52 |

**`_compute_hours_last_month`** (lines 126–157): iterates `attendance_ids` filtered to current-month range in employee TZ. Sums `worked_hours` and `validated_overtime_hours`.

**`_attendance_action_change`** (lines 208–245):
- If not checked_in: creates new `hr.attendance` with `check_in = now`, optional geo fields
- If checked_in: finds open attendance (check_out=False), writes `check_out = now`

---

## 10. `hr.version` Extension

**Source:** `/addons/hr_attendance/models/hr_version.py`

- Adds `ruleset_id` field (Many2one → `hr.attendance.overtime.ruleset`) to `hr.version`
- Default = `hr_attendance.hr_attendance_default_ruleset` if available
- Links employee's contract version → overtime calculation ruleset
- Employee's `ruleset_id` is a related field: `version_id.ruleset_id` (via hr_employee.py line 52)

---

## 11. Absence Management (New in v19)

**Source:** `/addons/hr_attendance/models/hr_attendance.py:660–697`

- `_cron_absence_detection`: daily cron that creates **technical attendance** records for employees with no attendance that day
- Technical attendance: `check_in` = midnight local, `check_out` = check_in + 1 second, `in_mode = 'technical'`, `out_mode = 'technical'`
- Triggers overtime recalculation → negative overtime lines generated for absent employees
- Only fires when `company.absence_management = True`
- Unlinks technical attendances if they produce zero overtime (no effect)

---

## 12. Migration Flags Summary

| Flag | Description |
|---|---|
| MF-1 | `hr.attendance.overtime` model (v16/v17) → replaced by `hr.attendance.overtime.line` + ruleset/rule models in v19 |
| MF-2 | `out_reason_id` — NOT present in Community v19 |
| MF-3 | `hr_attendance_reason_ids` — NOT present in Community v19 |
| MF-4 | `overtime_company_threshold` and `overtime_employee_threshold` on res.company — marked "TODO: Remove in master" (legacy fields) |
| MF-5 | `in_mode`/`out_mode` — new values added: `technical` and `auto_check_out` |
| MF-6 | `hr.version.ruleset_id` — new field linking contract version → overtime ruleset (new concept in v19) |
| MF-7 | `absence_management` company flag — new in v19, triggers technical attendance creation |
| MF-8 | GIST overlap constraint on overtime.line is commented out (not enforced at DB level) |
| MF-9 | `date` field on hr.attendance — computed+stored, derived from check_in in employee TZ; was not precomputed in earlier versions |
| MF-10 | `_update_overtime` called on CRUD — no separate scheduled computation; fully event-driven in v19 |
