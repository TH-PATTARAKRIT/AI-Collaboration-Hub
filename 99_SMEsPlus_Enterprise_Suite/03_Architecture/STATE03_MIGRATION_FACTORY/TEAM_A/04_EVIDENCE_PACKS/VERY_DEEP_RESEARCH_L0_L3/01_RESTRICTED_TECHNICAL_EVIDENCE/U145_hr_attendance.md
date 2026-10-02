# U145 — hr_attendance: Timekeeping / Check-In / Check-Out Deep L3
**Unit:** U145 | **Group:** G09 | **Priority:** P2  
**Source tree (READ-ONLY):** `.../odoo/addons/hr_attendance/`

---

## 1. Module Manifest — Dependencies

**File:** `hr_attendance/__manifest__.py` line 18  
`'depends': ['hr', 'barcodes', 'base_geolocalize']`

Module version is `2.0`. Category: `Human Resources/Attendances`. The module is an `application`. Post-install hook `post_init_hook` and uninstall hook `uninstall_hook` are declared. Overtime ruleset and overtime rule XML data files are loaded at install time (lines 20–21), confirming overtime is bundled into Community.

---

## 2. Attendance Model Core Fields

**File:** `hr_attendance/models/hr_attendance.py`

| Field | Line | Type / Config |
|---|---|---|
| `employee_id` | 37 | Many2one `hr.employee`, required, cascade, indexed |
| `check_in` | 46 | Datetime, required, tracking=True, indexed, default=now |
| `check_out` | 47 | Datetime, optional (no required), tracking=True |
| `date` | 48 | Date, computed from check_in + employee tz, stored, precompute |
| `worked_hours` | 49 | Float, computed `_compute_worked_hours`, stored, readonly |
| `overtime_hours` | 51 | Float, computed `_compute_overtime_hours`, stored |
| `overtime_status` | 52–54 | Selection to_approve/approved/refused, computed+stored, readonly=False |
| `in_mode` | 61–67 | Selection: kiosk/systray/manual/technical, readonly, default=manual |
| `out_mode` | 73–79 | Selection: kiosk/systray/manual/technical/auto_check_out, readonly |
| `expected_hours` | 80 | Float, computed `_compute_expected_hours`, stored |
| `in_latitude`, `in_longitude` | 56–57 | Float(10,7), readonly |
| `in_ip_address` | 59 | Char, readonly |
| `in_browser` | 60 | Char, readonly |

Model inherits `mail.thread` (line 31), ordered by `check_in desc`.

---

## 3. `_compute_worked_hours` — Core Logic

**File:** `hr_attendance/models/hr_attendance.py` lines 163–195

```python
@api.depends('check_in', 'check_out')
def _compute_worked_hours(self):
    for attendance in self:
        if attendance.check_out and attendance.check_in and attendance.employee_id:
            attendance.worked_hours = attendance._get_worked_hours_in_range(
                attendance.check_in, attendance.check_out)
        else:
            attendance.worked_hours = False
```

The helper `_get_worked_hours_in_range` (lines 173–195):
1. Gets the employee's calendar via `_get_employee_calendar` (which falls back to company calendar).
2. For **flexible** calendars: no lunch deduction (`resource._is_flexible()` check line 192).
3. For **fixed** calendars: deducts lunch intervals via `employee._employee_attendance_intervals(..., lunch=True)`.
4. Returns `sum_intervals(attendance_intervals - lunch_intervals)` as float hours.

---

## 4. Overlap / Validity Constraints

**File:** `hr_attendance/models/hr_attendance.py` lines 197–246

Two constraints:
- `_check_validity_check_in_check_out` (line 197): raises if `check_out < check_in`.
- `_check_validity` (line 205): 
  - Maximum 1 open record (no check_out) per employee at a time.
  - No overlapping time slices with prior records.
  - Raises `ValidationError` on violation.

---

## 5. Employee Extension — `attendance_state`, `last_attendance_id`

**File:** `hr_attendance/models/hr_employee.py`

| Field | Lines | Detail |
|---|---|---|
| `attendance_ids` | 19–20 | One2many `hr.attendance`, officer+hr_user groups |
| `last_attendance_id` | 21–23 | Many2one computed, stored, officer+hr_user groups |
| `last_check_in` | 24–26 | Related to `last_attendance_id.check_in`, stored |
| `last_check_out` | 27–29 | Related to `last_attendance_id.check_out`, stored |
| `attendance_state` | 30–33 | Selection checked_in/checked_out, computed |
| `attendance_manager_id` | 13–18 | Many2one `res.users`, officer group only |
| `hours_today` | 36–38 | Float computed, officer+hr_user groups |
| `total_overtime` | 49 | Float computed, officer+hr_user groups |

`_compute_attendance_state` (lines 202–206): sets `checked_in` if `last_attendance_id` exists and has no `check_out`, otherwise `checked_out`.

---

## 6. `_attendance_action_change` — Toggle Check-In/Out

**File:** `hr_attendance/models/hr_employee.py` lines 208–245

The single method used by kiosk, systray, and badge scanner to toggle attendance:
- If `attendance_state != 'checked_in'`: creates new `hr.attendance` record with `check_in=now`. If `geo_information` passed, sets `in_*` geo fields.
- If `attendance_state == 'checked_in'`: finds open attendance and writes `check_out=now` + optional `out_*` geo fields.
- Raises `UserError` if no open record found during check-out.

---

## 7. Kiosk Controller — Routes

**File:** `hr_attendance/controllers/main.py`

| Route | Auth | Method | Purpose |
|---|---|---|---|
| `/hr_attendance/<token>` | public | GET | Render kiosk page (QWeb template) |
| `/hr_attendance/attendance_barcode_scanned` | public | jsonrpc | Badge/RFID scan → calls `_attendance_action_change` |
| `/hr_attendance/manual_selection` | public | jsonrpc | Manual employee selection with optional PIN |
| `/hr_attendance/systray_check_in_out` | user | jsonrpc | Systray toggle via logged-in user |
| `/hr_attendance/attendance_user_data` | user | jsonrpc | Get current user's attendance status |
| `/hr_attendance/employees_infos` | public | jsonrpc | List employees (name/dept filter only) |
| `/hr_attendance/kiosk_mode_menu/<company_id>` | user | GET | Redirect to kiosk URL, auto-logout |

Kiosk token is a UUID hex stored on `res.company.attendance_kiosk_key` (field visible only to `group_hr_attendance_user`).

**PIN security** (line 208): `manual_selection` checks `company.attendance_kiosk_use_pin` and compares `employee.pin == pin_code` before acting. No PIN = no check if `attendance_kiosk_use_pin` is False.

---

## 8. Kiosk Session Security

**File:** `hr_attendance/controllers/main.py` line 91–93  

Before opening kiosk mode, if the user has a password set, their session is logged out (`request.session.logout(keep_db=True)`). This prevents attendants from accessing the backend after the kiosk is opened. `has_password()` (lines 256–267) does a raw SQL check against `res_users.password` for the current user.

---

## 9. Overtime — IN Community (Not Enterprise-Only)

**File:** `hr_attendance/__manifest__.py` lines 20–21  
Overtime ruleset data and overtime rule data are loaded at install. The models `hr.attendance.overtime.line`, `hr.attendance.overtime.ruleset`, `hr.attendance.overtime.rule` are all present in the Community module.

**File:** `hr_attendance/models/hr_attendance.py` lines 322–368  
`_update_overtime` is called on `create`, `write`, `unlink` of attendance records. It:
1. Deletes existing overtime lines in the affected date range.
2. Groups attendances by ruleset.
3. Calls `ruleset.rule_ids._generate_overtime_vals_v2(...)` to recompute.
4. Creates new `hr.attendance.overtime.line` records.
5. Invalidates computed fields on attendance records.

---

## 10. Overtime Line Model

**File:** `hr_attendance/models/hr_attendance_overtime.py`

| Field | Line | Detail |
|---|---|---|
| `employee_id` | 12 | Many2one, cascade, indexed |
| `date` | 17 | Date, indexed |
| `status` | 18–25 | Selection to_approve/approved/refused, computed, stored, readonly=False |
| `duration` | 26 | Float "Extra Hours" |
| `manual_duration` | 27–30 | Float "Extra Hours (encoded)", computed from duration, editable |
| `time_start` | 33 | Datetime = attendance.check_in |
| `time_stop` | 34 | Datetime = attendance.check_out |
| `amount_rate` | 35 | Float "Overtime pay rate", default=1.0 |
| `rule_ids` | 39 | Many2many `hr.attendance.overtime.rule` |

`_compute_status` (lines 61–65): auto-sets to `to_approve` if company uses `by_manager` validation, else `approved`.

---

## 11. Overtime Ruleset

**File:** `hr_attendance/models/hr_attendance_overtime_ruleset.py`

| Field | Detail |
|---|---|
| `name` | Char, required |
| `rule_ids` | One2many `hr.attendance.overtime.rule` |
| `company_id` | Many2one `res.company` |
| `country_id` | Many2one `res.country` |
| `rate_combination_mode` | Selection max/sum, how multiple rule rates combine |
| `active` | Boolean |

`action_regenerate_overtimes` calls `_update_overtime` on eligible attendances. The `ruleset_id` is linked to `hr.version` (employee contract version), not to the company directly.

---

## 12. Write Access Control for Attendance Editing

**File:** `hr_attendance/models/hr_attendance.py` lines 376–388

`write()` raises `AccessError` if the user:
- Is not writing their own attendance (`employee_id not in user.employee_ids`), AND
- Does not have `group_hr_attendance_manager`, AND
- Is not the `attendance_manager_id` of the target employee.

This means: managers with `group_hr_attendance_manager` can edit any attendance. `attendance_manager_id` users can edit their managed employees. Regular users can only edit their own.

---

## 13. Security Groups (4 levels)

**File:** `hr_attendance/security/hr_attendance_security.xml`

| Group XML ID | Name | Scope |
|---|---|---|
| `group_hr_attendance_own_reader` | User: Read his own attendances | Read-only own records |
| `group_hr_attendance_officer` | Officer: Manage attendances | Manage assigned employees |
| `group_hr_attendance_user` | Officer: Manage all attendances | All employees, implies officer |
| `group_hr_attendance_manager` | Administrator | Full access, implies user |

`base.group_user` implies `group_hr_attendance_own_reader` (line 14–16), so all employees can read their own attendance.

---

## 14. Record Rules

**File:** `hr_attendance/security/hr_attendance_security.xml` lines 43–87

- **Multi-company rule** (global): restrict to company's employees.
- **Admin rule**: `group_hr_attendance_user` → domain `(1=1)` (full access).
- **Officer rule**: `group_hr_attendance_officer` → restricts to `attendance_manager_id == user.id` for CRUD.
- **Own reader rule**: `group_hr_attendance_own_reader` → read-only `employee_id.user_id == user.id`.

---

## 15. Model Access CSV

**File:** `hr_attendance/security/ir.model.access.csv`

| Access Row | Model | Group | R/W/C/D |
|---|---|---|---|
| admin | hr.attendance | manager | 1/1/1/1 |
| user | hr.attendance | user | 1/1/1/1 |
| officer | hr.attendance | officer | 1/1/1/1 |
| own_reader | hr.attendance | own_reader | 1/0/0/0 |
| overtime_line_officer | hr.attendance.overtime.line | officer | 1/1/1/1 |
| overtime_line_own_reader | hr.attendance.overtime.line | own_reader | 1/0/0/0 |

---

## 16. Cron Jobs

**File:** `hr_attendance/data/hr_attendance_data.xml`

| Cron | Interval | Method |
|---|---|---|
| Attendance: Automatically check-out employees | 4 hours | `_cron_auto_check_out` |
| Attendance: Detect Absences for employees | 4 hours | `_cron_absence_detection` |

**`_cron_auto_check_out`** (lines 601–658): Searches open attendances where company has `auto_check_out=True` and non-flexible calendar. Calculates if current duration + previous worked hours minus tolerance exceeds expected hours. If so, writes `check_out` set to schedule end and posts chatter message.

**`_cron_absence_detection`** (lines 660–697): Creates technical 1-second attendance records for employees absent on the previous day (company `absence_management=True`). If no overtime is generated (no negative overtime), the technical record is deleted.

---

## 17. Company Settings

**File:** `hr_attendance/models/res_company.py` lines 21–43

| Field | Default | Purpose |
|---|---|---|
| `attendance_kiosk_mode` | barcode_manual | How employees identify at kiosk |
| `attendance_kiosk_use_pin` | False | Require PIN for manual selection |
| `attendance_from_systray` | False | Enable systray widget |
| `attendance_overtime_validation` | no_validation | Auto-approve or require manager |
| `auto_check_out` | False | Enable cron auto-checkout |
| `auto_check_out_tolerance` | 2 hours | Tolerance before auto checkout triggers |
| `absence_management` | False | Enable absence detection cron |
| `attendance_device_tracking` | False | Capture GPS/IP/browser |
| `hr_attendance_display_overtime` | (unset) | Show overtime to employees |

Kiosk key is a UUID hex, regenerated via `_regenerate_attendance_kiosk_key`. `write()` on company triggers `_update_overtime` recompute if overtime thresholds changed.

---

## 18. Employee Public View Extension

**File:** `hr_attendance/models/hr_employee_public.py` (confirmed present)  
Exposes `attendance_state` and `last_check_in` on the public employee model for kiosk display.

---

## 19. Duplicate Prevention

**File:** `hr_attendance/models/hr_attendance.py` line 397–398

```python
def copy(self, default=None):
    raise exceptions.UserError(_('You cannot duplicate an attendance.'))
```

Attendance records cannot be duplicated via ORM `copy`.

---

## 20. `display_attendances` Computed Field

**File:** `hr_attendance/models/hr_employee.py` lines 94–109

Controls UI visibility of attendance tab on employee form. True if:
- User has `group_hr_attendance_user` (manager of all), OR
- User is an officer and `attendance_manager_id` matches, OR
- User is own reader and employee is their own employee record.

---

## 21. `attendance_manager_id` Auto-Group Assignment

**File:** `hr_attendance/models/hr_employee.py` lines 56–80

When `attendance_manager_id` is set on an employee, the target user is automatically added to `group_hr_attendance_officer`. When removed, `_clean_attendance_officers` removes the user from the group if they are no longer an attendance manager for any employee.

---

## 22. Geolocation Tracking

**File:** `hr_attendance/controllers/main.py` lines 57–75

`_get_geoip_response` captures: location (via `base_geolocalize`), latitude/longitude (GPS if available, else IP-based), `ip_address` from `request.geoip.ip`, `browser` from user-agent. Only active when `device_tracking_enabled=True` for the company. All geo data stored as `in_*` / `out_*` fields on the attendance record.

---

## 23. Overtime Approval Workflow

**File:** `hr_attendance/models/hr_attendance.py` lines 595–598 and `hr_attendance_overtime.py` lines 85–88

- `action_approve_overtime()` on attendance delegates to `linked_overtime_ids.action_approve()`.
- `action_refuse_overtime()` on attendance delegates to `linked_overtime_ids.action_refuse()`.
- `action_approve` writes `status='approved'`, `action_refuse` writes `status='refused'`.
- Approval triggers recompute of `overtime_status`, `validated_overtime_hours` on linked attendances.
