# U202 — hr_employee: Technical Evidence Pack (RESTRICTED)

**Unit:** U202  
**Module:** hr (hr_employee), resource (resource.calendar, resource.mixin)  
**Odoo Version:** 19.0.post20260921  
**Research Date:** 2026-10-02  
**Classification:** RESTRICTED — VDR internal use only

---

## 1. Source Paths Examined

| File | Role |
|------|------|
| `hr/models/hr_employee.py` | `hr.employee` model definition |
| `hr/models/hr_employee_public.py` | `hr.employee.public` SQL-view model |
| `hr/models/hr_version.py` | `hr.version` versioning / contract model |
| `hr/models/hr_job.py` | `hr.job` model |
| `hr/security/hr_security.xml` | Multi-company record rules |
| `resource/models/resource_mixin.py` | `resource.mixin` abstract model |
| `resource/models/resource_resource.py` | `resource.resource` concrete model |
| `resource/models/resource_calendar.py` | `resource.calendar` model |
| `resource/models/resource_calendar_attendance.py` | `resource.calendar.attendance` model |

---

## 2. hr.employee — Model Declaration

**File:** `hr/models/hr_employee.py`

```
_name = 'hr.employee'                                                    # line 39
_inherit = ['mail.thread.main.attachment', 'mail.activity.mixin',        # line 42
            'resource.mixin', 'avatar.mixin']
_inherits = {'hr.version': 'version_id'}                                 # line 45
```

**Critical v19 Architecture:** `hr.employee` uses `_inherits` (SQL delegation) to `hr.version`. The `version_id` is a computed non-stored Many2one pointing to `current_version_id`. This means every field defined on `hr.version` is directly accessible on `hr.employee` via delegation.

---

## 3. Key Field Evidence

### 3.1 resource_id

**File:** `hr/models/hr_employee.py`, line 85  
```python
resource_id = fields.Many2one('resource.resource', required=True)
```
Provided by `resource.mixin` (abstract model). `hr.employee` inherits `resource.mixin` via `_inherit`, meaning `resource_id` is auto-created on employee creation and links to the `resource.resource` table.

### 3.2 resource_calendar_id

**File:** `hr/models/hr_employee.py`, line 87  
```python
resource_calendar_id = fields.Many2one(
    related='version_id.resource_calendar_id',
    inherited=True, index=False, store=False, check_company=True)
```

- Not stored on `hr_employee` table; delegates to `hr.version.resource_calendar_id`
- On `hr.version` (line 150): `inverse='_inverse_resource_calendar_id'` — when the current version changes its calendar, `_inverse_resource_calendar_id()` (hr_version.py:665) also updates `employee.resource_id.calendar_id` to keep `resource.resource` in sync

### 3.3 active

**File:** `hr/models/hr_employee.py`, line 118  
```python
active = fields.Boolean('Active', related='resource_id.active', default=True, store=True, readonly=False)
```
`active` is delegated to `resource.resource.active`. Setting active=False archives the resource too.

**Archival methods** (hr_employee.py):
- `action_archive()` at line 1508 — calls super, empties `parent_id` and `coach_id` on other employees, and for single-employee archival opens the `hr.departure.wizard`
- `action_unarchive()` at line 1499 — calls super, clears `departure_reason_id`, `departure_description`, `departure_date`
- No `toggle_active()` override found; standard ORM `toggle_active` applies

### 3.4 job_id and department_id

These fields are defined on `hr.version` (not on `hr.employee` directly), accessed via `_inherits` delegation:

**File:** `hr/models/hr_version.py`
- `job_id = fields.Many2one('hr.job', check_company=True, tracking=True, index=True)` — line 130
- `department_id = fields.Many2one('hr.department', check_company=True, tracking=True, index=True)` — line 127
- `job_title = fields.Char(compute="_compute_job_title", inverse="_inverse_job_title", store=True, readonly=False, tracking=True)` — line 131

`job_title` auto-computes from `job_id.name` unless manually overridden (tracked by `is_custom_job_title`).

### 3.5 parent_id and coach_id

Defined directly on `hr.employee`:

**File:** `hr/models/hr_employee.py`
- `parent_id` at line 195: `fields.Many2one('hr.employee', 'Manager', tracking=True, index=True)`
- `coach_id` at line 198-202: computed from `parent_id`, stored=True, readonly=False

`coach_id` is auto-set to the manager when manager changes (line 815-822).

### 3.6 company_id

**File:** `hr/models/hr_employee.py`, line 119  
```python
company_id = fields.Many2one('res.company', required=True, tracking=True)
```
(Also provided via `resource.mixin` as related to `resource_id.company_id`, but redeclared directly on employee.)

`_onchange_company_id` at line 1538 warns when changing company on existing employee: "To avoid multi company issues...you should create another employee in the new company instead."

### 3.7 address_id (Work Address)

**File:** `hr/models/hr_version.py`, line 134-141  
```python
address_id = fields.Many2one(
    'res.partner',
    string='Work Address',
    default=_get_default_address_id,
    store=True, readonly=False, check_company=True, tracking=True)
```
`_get_default_address_id()` (line 42-44): returns the company's default partner address.

**MIGRATION FLAG:** In v16/v17 `address_id` (work address) lived directly on `hr.employee`. In v19 it lives on `hr.version` and is accessed via `_inherits` delegation.

---

## 4. hr.version — The New Versioning/Contract Model

**File:** `hr/models/hr_version.py`

```
_name = 'hr.version'    # line 35
_order = 'date_version' # line 39
```

**v19 Architecture Change:** The old `hr.contract` model from v16/v17 has been replaced by `hr.version`. The version model holds both contract data and a snapshot of work-related fields at a point in time. An employee can have multiple versions; the `current_version_id` computed field on `hr.employee` holds the active one.

Key `hr.version` fields:
- `date_version` (required, default=today) — the effective date of this version
- `contract_date_start` / `contract_date_end` / `trial_date_end` — contract span (group: `hr.group_hr_manager`)
- `wage` / `contract_wage` — wage fields (group: `hr.group_hr_manager`)
- `resource_calendar_id` — working schedule
- `structure_type_id` / `contract_type_id` — payroll structure linkage
- `is_current` / `is_past` / `is_future` / `is_in_contract` — computed booleans

Private information fields (all `groups="hr.group_hr_user"`):
- `private_street`, `private_street2`, `private_city`, `private_zip`, `private_state_id`, `private_country_id` — replaced the old `address_home_id` field
- `country_id` (nationality), `identification_id`, `ssnid`, `passport_id`, `sex`, `marital`
- `distance_home_work`, `km_home_work`, `distance_home_work_unit`

**MIGRATION FLAG:** `address_home_id` (a Many2one to `res.partner` for home address) present in v16/v17 is GONE in v19. Replaced by discrete private address fields on `hr.version`.

---

## 5. hr.employee.public — SQL View Model

**File:** `hr/models/hr_employee_public.py`

```python
_name = 'hr.employee.public'
_auto = False      # SQL view, not a real table  # line 14
_log_access = True
```

Initialized via `init()` at line 194-202:
```python
CREATE or REPLACE VIEW hr_employee_public_view as (
    SELECT <fields>
    FROM hr_employee e
    JOIN hr_version v ON v.id = e.current_version_id
)
```

The public view exposes only non-sensitive fields: `name`, `active`, `department_id`, `job_id`, `job_title`, `company_id`, `address_id`, `mobile_phone`, `work_phone`, `work_email`, `work_contact_id`, `user_id`, `resource_id`, `tz`, `resource_calendar_id`, `color`, etc. Private fields (bank accounts, identification numbers, salary data) are NOT exposed.

Multi-company record rule for `hr.employee.public` (hr_security.xml:45-50) mirrors the `hr.employee` rule.

---

## 6. resource.mixin — Abstract Mixin

**File:** `resource/models/resource_mixin.py`

```python
_name = 'resource.mixin'
```

Fields provided to inheriting models:
- `resource_id` at line 14: `Many2one('resource.resource', required=True, bypass_search_access=True, index=True, ondelete='restrict')`
- `company_id` at line 17: `related='resource_id.company_id'`, store=True
- `resource_calendar_id` at line 21: `related='resource_id.calendar_id'`, store=True
- `tz` at line 25: `related='resource_id.tz'`, readonly=False

`create()` at line 30: auto-creates a `resource.resource` record if `resource_id` is not provided.

**_get_work_days_data_batch()** at line 83:
- Signature: `_get_work_days_data_batch(self, from_datetime, to_datetime, compute_leaves=True, calendar=None, domain=None)`
- Groups resources by calendar, calls `calendar._work_intervals_batch()` or `calendar._attendance_intervals_batch()` depending on `compute_leaves`
- Returns `{employee_id: {'days': n, 'hours': h}}`
- Key: maps `resource_id` back to `employee.id` via `mapped_employees = {e.resource_id.id: e.id for e in self}`

---

## 7. resource.resource Model

**File:** `resource/models/resource_resource.py`

```python
_name = 'resource.resource'
_order = "name"
```

Key fields:
- `name`, `active`, `company_id`, `resource_type` (user/material), `user_id`
- `calendar_id`: `Many2one('resource.calendar', ...)` — the working schedule. Domain: `[('company_id', '=', company_id)]`
- `tz`: selection field (required)
- `time_efficiency`: float, default 100% (for manufacturing scheduling)

`hr.employee` uses `resource.resource` via delegation (not inheritance). The employee's `active`, `resource_calendar_id`, `tz`, `user_id` are all proxied from `resource.resource`.

---

## 8. resource.calendar Model

**File:** `resource/models/resource_calendar.py`

Key fields:
- `name` (required), `active`, `company_id`
- `schedule_type`: selection `[('flexible', 'Flexible'), ('fully_fixed', 'Fully Fixed')]` — line 77
- `flexible_hours`: Boolean, computed from `schedule_type == 'flexible'` — line 90
- `duration_based`: Boolean — "Attendance based on duration" — line 89
- `two_weeks_calendar`: Boolean — enables alternating 2-week schedule — line 108
- `hours_per_day`: float, stored computed — line 102
- `hours_per_week`: float, stored computed — line 104
- `full_time_required_hours`: float, defaults to company calendar's `hours_per_week` — line 93
- `tz`: timezone selection (required) — line 110
- `attendance_ids`: One2many to `resource.calendar.attendance` — line 65
- `global_leave_ids`: One2many to `resource.calendar.leaves` filtered by `resource_id = False` — line 97

**_attendance_intervals_batch()** at line 327: Returns work intervals grouped by resource, respects `two_weeks_calendar`, `flexible_hours`, and resource-specific calendars.

**_work_intervals_batch()** at line 556: Calls `_attendance_intervals_batch`, filters out lunch periods, subtracts leave intervals if `compute_leaves=True`.

**_get_attendance_intervals_days_data()** at line 627: Converts interval set to `{'days': n, 'hours': h}`. Uses `duration_days` proportionally. For flexible calendars, divides hours by `hours_per_day`.

**_get_hours_per_week()** at line 701: Sums `hour_to - hour_from` (or `duration_hours` for duration_based) across global attendances. Halves for 2-week calendars.

---

## 9. resource.calendar.attendance Model

**File:** `resource/models/resource_calendar_attendance.py`

```python
_name = 'resource.calendar.attendance'
_order = 'sequence, week_type, dayofweek, hour_from'
```

Fields:
- `dayofweek`: selection `[('0','Monday')..('6','Sunday')]`, index=True — line 15
- `hour_from` / `hour_to`: Float (hours since midnight) — lines 24, 27
- `day_period`: selection `[('morning','Morning'),('lunch','Break'),('afternoon','Afternoon'),('full_day','Full Day')]` — line 35
- `week_type`: selection `[('1','Second'),('0','First')]`, default=False — line 40 (for 2-week calendars)
- `duration_hours`: computed float (hour_to - hour_from, 0 for lunch) — line 31
- `duration_days`: computed float (0 for lunch, 1 for full_day, 0.5 or 1 for morning/afternoon) — line 32
- `calendar_id`: Many2one required, ondelete=cascade — line 33

**MIGRATION FLAG:** In v16/v17, `resource.calendar.attendance` had `date_from` and `date_to` fields enabling date-ranged attendance lines. These fields are ABSENT in v19. The attendance model is purely weekday-based; exceptions are handled via `resource.calendar.leaves`.

**`get_week_type(date)`** at line 68: Determines even/odd week via `floor((ordinal-1)/7) % 2`. Ensures strict alternation without the 53rd-week anomaly of ISO week numbers.

---

## 10. hr.job Model

**File:** `hr/models/hr_job.py`

```python
_name = 'hr.job'
_description = "Job Position"
_inherit = ['mail.thread']
_order = 'sequence'
```

Key fields:
- `name`: Char, required, index=trigram, translate=True — line 15
- `no_of_employee`: Integer, computed — current employees in this position — line 19
- `no_of_recruitment`: Integer — target new hires — line 21
- `expected_employees`: computed = `no_of_employee + no_of_recruitment` — line 17
- `department_id`: Many2one `hr.department`, check_company=True — line 38
- `company_id`: Many2one, default=current company — line 39
- `contract_type_id`: Many2one `hr.contract.type` — line 40
- `employee_ids`: One2many back to `hr.employee` via `job_id` — line 23

Unique constraint: `(name, company_id, department_id)` — line 42-44.

`_compute_employees()` at line 51: Uses `_read_group` on `hr.employee` filtered by `job_id`.

---

## 11. Multi-Company Access Control

**File:** `hr/security/hr_security.xml`

`hr_employee_comp_rule` (line 28): domain for `hr.employee`:
```python
['|', '|', '|',
    ('company_id', 'in', company_ids + [False]),
    ('parent_id.user_id', '=', user.id),
    ('id', '=', user.employee_id.parent_id.id),
    ('user_id', '=', user.id)
]
```

This means an employee record is visible if: (a) it belongs to the active companies; OR (b) the current user is the record's manager; OR (c) the record is the current user's own manager; OR (d) the record is the current user's own employee record. This cross-company manager visibility is intentional.

`hr_employee_public_comp_rule` mirrors the same rule for the public view.

---

## 12. Version Management on hr.employee

`create_version(values)` at line 571: Creates a new `hr.version` record by copying the current version with new `date_version`. Used to record contract/schedule changes over time.

`_get_version(date)` at line 559: Returns the version effective on a given date (most recent version with `date_version <= date`).

`_compute_current_version_id()` at line 527: Queries `hr.version` for the latest version with `date_version <= today`, stores in `current_version_id` (stored, computed field).

`_get_calendar_periods(start, stop)` at line 1641: Returns `{employee: [(start, stop, calendar)]}` considering which version is active during each contract period.

---

## 13. Migration Flags Summary

| Flag | Description |
|------|-------------|
| MIG-01 | `hr.contract` model from v16/v17 replaced by `hr.version` in v19 |
| MIG-02 | `address_home_id` (Many2one to res.partner for home address) REMOVED; replaced by discrete fields on `hr.version` |
| MIG-03 | `resource.calendar.attendance.date_from` / `date_to` REMOVED; attendance lines are purely weekday-based in v19 |
| MIG-04 | `resource_calendar_id` on `hr.employee` is now non-stored (related to `version_id.resource_calendar_id`); queries must use `current_version_id` |
| MIG-05 | `job_id`, `department_id`, `address_id` now reside on `hr.version`, accessed via `_inherits` delegation |
| MIG-06 | `hr.employee.public` is now a SQL VIEW joining `hr_employee` and `hr_version` (was a regular model in older versions) |
| MIG-07 | `toggle_active()` not overridden; use `action_archive()` / `action_unarchive()` which handle departure wizard and field cleanup |
