# U140 — hr_leave (hr_holidays) Absence/Leave Management Deep L3
**Unit:** U140 | **Group:** G09 | **Priority:** P2 | **Date:** 2026-10-02

---

## L1 — Module Identity & Dependencies

- **Module path:** `odoo/addons/hr_holidays`
- **Technical name in Odoo 19:** `hr_holidays` (the user-facing name is "Time Off")
- **Manifest:** `hr_holidays/__manifest__.py:5-7`
  - `'name': 'Time Off'`
  - `'version': '1.6'`
  - `'category': 'Human Resources/Time Off'`
- **Dependencies** (`__manifest__.py:27`): `['hr', 'calendar', 'resource']`
- **No dependency on payroll in base module.** Payroll integration is handled by the separate `hr_work_entry_holidays` module (`hr_work_entry_holidays/__manifest__.py:17`): `'depends': ['hr_holidays', 'hr_work_entry']`

---

## L2 — Core Models

### 2.1 Leave Type — `hr.leave.type`
**File:** `hr_holidays/models/hr_leave_type.py`

Key fields (lines 44–128):
- `leave_validation_type` (line 87–91): Selection `['no_validation', 'hr', 'manager', 'both']`, default `'hr'`
- `allocation_validation_type` (line 96–100): same options
- `responsible_ids` (line 81–86): Many2many to `res.users` — filters for `group_hr_holidays_user`
- `requires_allocation` (line 92): Boolean, default True
- `employee_requests` (line 93): Boolean — controls if employees can self-allocate
- `request_unit` (line 109–112): Selection `['day', 'half_day', 'hour']`
- `time_type` (line 107–108): Selection `['other', 'leave']` — determines whether it's "Worked Time" or "Absence"
- `unpaid` (line 113): Boolean
- `allows_negative` (line 125): Boolean — allows negative leave balance cap
- `max_allowed_negative` (line 127): Integer — max excess days when negative allowed
- `accruals_ids` (line 122): One2many to `hr.leave.accrual.plan`
- `include_public_holidays_in_duration` (line 114): Boolean — public holidays counted in leave duration

### 2.2 Leave Request — `hr.leave`
**File:** `hr_holidays/models/hr_leave.py`

Key fields (lines 129–247):
- `state` (line 129–135): Selection `['confirm', 'refuse', 'validate1', 'validate', 'cancel']`, default `'confirm'`
  - Note: there is **no 'draft' state** in the leave request — records are created directly in `confirm`
- `holiday_status_id` (line 138–147): Many2one to `hr.leave.type`
- `employee_id` (line 153): Many2one to `hr.employee`
- `date_from` (line 172–173): Datetime, **computed** from `request_date_from`
- `date_to` (line 174–175): Datetime, **computed** from `request_date_to`
- `request_date_from` (line 212): Date — user-facing start date
- `request_date_to` (line 213): Date — user-facing end date
- `number_of_days` (line 176–178): Float, computed and stored
- `number_of_hours` (line 179–181): Float, computed and stored
- `validation_type` (line 150): related to `holiday_status_id.leave_validation_type`
- `first_approver_id` (line 186–188): Many2one `hr.employee`
- `second_approver_id` (line 189–191): Many2one `hr.employee`
- `can_approve` (line 193): computed Boolean
- `can_validate` (line 194): computed Boolean
- `can_refuse` (line 195): computed Boolean
- `can_cancel` (line 196): computed Boolean
- `meeting_id` (line 185): Many2one to `calendar.event` — created on validation

### 2.3 Leave Allocation — `hr.leave.allocation`
**File:** `hr_holidays/models/hr_leave_allocation.py`

Key fields (lines 58–135):
- `state` (line 58–66): Selection `['confirm', 'refuse', 'validate1', 'validate']`, default `'confirm'`
- `allocation_type` (line 119–122): Selection `['regular', 'accrual']`, default `'regular'`
- `accrual_plan_id` (line 124–126): Many2one to `hr.leave.accrual.plan`
- `date_from` (line 67): Date — allocation validity start
- `date_to` (line 69): Date — allocation validity end
- `number_of_days` (line 82–84): Float
- `lastcall` (line 112): Date — last accrual run date
- `nextcall` (line 116): Date — next scheduled accrual date
- `validation_type` (line 101): related to `holiday_status_id.allocation_validation_type`
- `approver_id` / `second_approver_id` (lines 95–100): approval tracking

---

## L3 — Approval State Machine

### Leave Request State Machine (`hr.leave`)
States: `confirm` → `validate1` (if `validation_type == 'both'`) → `validate`; or `confirm` → `validate` (if single validation)
Refuse: any of `confirm/validate1/validate` → `refuse`
Cancel: `validate` → `cancel` (via wizard)

**Key method: `action_approve`** (`hr_leave.py:1188–1203`):
- Splits leaves into "to validate" (single validation) vs "to approve" (first step of dual validation)
- For dual validation: writes `state = 'validate1'`, sets `first_approver_id`
- For single validation: calls `_action_validate`
- Guard: checks `can_validate` or `can_approve`

**Key method: `_action_validate`** (`hr_leave.py:1276–1301`):
- Writes `state = 'validate'`
- Sets `second_approver_id` (for `validation_type == 'both'`) or `first_approver_id`
- Calls `_validate_leave_request` — creates resource calendar leave and calendar meeting

**Key method: `action_refuse`** (`hr_leave.py:1303–1322`):
- Allowed from `confirm`, `validate`, `validate1`
- Writes `state = 'refuse'`, deactivates associated `meeting_id`
- Posts chatter notification to employee

**Key method: `_validate_leave_request`** (`hr_leave.py:1095–1128`):
- Calls `_create_resource_leave` — creates `resource.calendar.leaves` entries
- Conditionally creates `calendar.event` meeting if `create_calendar_meeting` is True on the leave type
- Posts "Your leave has been accepted" chatter message to the employee

**Approval authorization — `_check_approval_update`** (`hr_leave.py:1458–1513`):
- Officers (`group_hr_holidays_user`) can approve/validate leaves for anyone (except own leaves)
- `leave_manager_id` (time off manager per employee) can first-approve dual-validation leaves
- Managers (`group_hr_holidays_manager`) have unrestricted access
- Self-approval blocked: only Administrators may approve their own requests

**Responsible for approval — `_get_responsible_for_approval`** (`hr_leave.py:1539–1553`):
- `validation_type == 'manager'`: checks `employee_id.leave_manager_id`, then `parent_id.user_id`, then `responsible_ids`
- `validation_type == 'hr'`: uses `holiday_status_id.responsible_ids`
- `validation_type == 'both'` (confirm state): manager flow; (validate1 state): HR flow

**Auto-approval** (`hr_leave.py:956–960`): When `validation_type == 'no_validation'`, the leave is auto-approved on create via `action_approve` in sudo.

### Leave Allocation State Machine (`hr.leave.allocation`)
**`action_approve`** (`hr_leave_allocation.py:899–914`):
- Same pattern: "to validate" vs "to approve" split
- Writes `state = 'validate1'` for first step, then calls `_action_validate`

**`_action_validate`** (`hr_leave_allocation.py:916–927`):
- Sets `state = 'validate'`, records `approver_id`/`second_approver_id`

**`action_refuse`** (`hr_leave_allocation.py:929–936`):
- Writes `state = 'refuse'`

---

## L4 — Accrual System

### Accrual Plan — `hr.leave.accrual.plan`
**File:** `hr_holidays/models/hr_leave_accrual_plan.py`

- `level_ids` (line 21): One2many to `hr.leave.accrual.level`
- `transition_mode` (line 26–29): `['immediately', 'end_of_accrual']`
- `is_based_on_worked_time` (line 31–33): Boolean — excludes unpaid time off
- `accrued_gain_time` (line 34–38): `['start', 'end']` — gain at period start or end
- `can_be_carryover` (line 39): Boolean
- `carryover_date` (line 40–45): `['year_start', 'allocation', 'other']`
- `added_value_type` (line 63–64): `['day', 'hour']`

### Accrual Level — `hr.leave.accrual.level`
**File:** `hr_holidays/models/hr_leave_accrual_plan_level.py`

- `frequency` (line 45–53): `['hourly', 'daily', 'weekly', 'bimonthly', 'monthly', 'biyearly', 'yearly']`
- `added_value` (line 39): Float — days/hours per period
- `start_count` / `start_type` (lines 23–30): delay before accrual starts (days/months/years)

### Cron Job — `ir_cron_data.xml:4–11`
- Name: "Accrual Time Off: Updates the number of time off"
- Model: `hr.leave.allocation`
- Code: `model._update_accrual()`
- Interval: 1 day

**`_update_accrual`** method (`hr_leave_allocation.py:676–687`):
- Searches for validated accrual allocations with `nextcall <= today`
- Calls `_process_accrual_plans` on each

### Second cron — `ir_cron_data.xml:13–20`
- Name: "Time Off: Cancel invalid leaves"
- Model: `hr.leave`
- Code: `model._cancel_invalid_leaves()`
- Interval: 1 day

**`_cancel_invalid_leaves`** (`hr_leave.py:1682–1716`):
- Checks leaves in the next 31 days linked to accrual allocations
- Cancels leaves where the accrual balance is insufficient (or exceeds negative cap)

---

## L5 — Work Entry Integration (Bridge Module)

**Module:** `hr_work_entry_holidays` (auto-install when both `hr_holidays` and `hr_work_entry` are installed)
**Manifest:** `hr_work_entry_holidays/__manifest__.py:17`: `'auto_install': True`

### `HrLeaveType` extension (`hr_work_entry_holidays/models/hr_leave.py:9–12`):
- Adds `work_entry_type_id` field (Many2one to `hr.work.entry.type`)

### `HrLeave` extension (`hr_work_entry_holidays/models/hr_leave.py:15–175`):
- **`_prepare_resource_leave_vals`** (line 18–21): Injects `work_entry_type_id` into resource leave creation
- **`_validate_leave_request`** (line 127–130): Calls `super()` then `_cancel_work_entry_conflict` in sudo
- **`_cancel_work_entry_conflict`** (line 23–87): On leave validation:
  1. Creates leave work entries via `hr.version._get_work_entries_values`
  2. Fetches overlapping existing work entries
  3. Archives work entries completely covered by the leave
  4. Adjusts overlapping work entries at the boundaries
- **`action_refuse`** (line 132–139): Calls `_regen_work_entries` to restore attendance entries
- **`_regen_work_entries`** (line 151–165): Archives leave work entries, recreates attendance work entries for the period
- **`_compute_can_cancel`** (line 167–175): A leave with already-validated work entries CANNOT be cancelled

### Key finding: payroll impact is indirect via `hr.work.entry`
The leave module itself has no accounting or payroll entries. The `hr_work_entry_holidays` bridge creates `hr.work.entry` records typed as leave, which are then consumed by payroll modules (Enterprise) to compute deductions. This means **no payroll integration in Community-only deployments**.

---

## L6 — Security

**File:** `hr_holidays/security/hr_holidays_security.xml`

### Groups (lines 9–30):
1. `group_hr_holidays_responsible` (line 9–12): "Time Off Responsible" — implied by `base.group_user`
2. `group_hr_holidays_user` (line 14–19): "Officer: Manage all requests" — implies `group_hr_holidays_responsible` + `hr.group_hr_user`
3. `group_hr_holidays_manager` (line 21–30): "Administrator" — implies `group_hr_holidays_user`; assigned to admin/root users

### Record rules for `hr.leave`:
- **Base employee read** (line 34–42): domain `[('employee_id.user_id', '=', user.id)]` — employees can only read own leaves
- **Base employee write** (line 44–59): write/create only for own leaves not yet approved, OR for manager-type leaves where user is `leave_manager_id`
- **Responsible read** (line 72–82): `leave_manager_id` can read managed employees' leaves
- **Officer read** (line 99–107): unrestricted read/write/create/unlink on all leaves
- **Manager** (line 126–131): unrestricted all operations
- **Multicompany rule** (line 133–137): filters by `company_id`

### Self-approval blocked:
`_check_approval_update` (line 1458–1513): Officers (`group_hr_holidays_user`) cannot approve their own leaves unless they are superuser or Administrator (`group_hr_holidays_manager`).

---

## L7 — Resource Calendar Integration

- On leave validation, `_create_resource_leave` (`hr_leave.py:1066–1071`) creates `resource.calendar.leaves` records
- These block the employee's work calendar for payroll hour computation
- The `_prepare_resource_leave_vals` method (`hr_leave.py:1051–1064`) includes `time_type` and `elligible_for_accrual_rate` from the leave type

---

## L8 — Mandatory Days

**Model:** `hr.leave.mandatory.day` (`hr_holidays/models/hr_leave_mandatory_day.py:8`)
- Employees cannot request leave on mandatory days unless they have `group_hr_holidays_user`
- Check occurs in `_check_validity` (`hr_leave.py:846–847`):
  ```python
  if not is_leave_user and any(leave.has_mandatory_day for leave in self):
      raise ValidationError(_('You are not allowed to request time off on a Mandatory Day'))
  ```

---

## L9 — Accounting/Payroll Integration

**ABSENT in Community.** The `hr_holidays` module has no accounting entries, no journal entries, and no payslip integration. The `hr_work_entry_holidays` module bridges to `hr.work.entry` only — payroll deduction requires Enterprise payroll modules.

---

## L10 — Reports

**File:** `hr_holidays/report/hr_leave_report.py`
- `hr.leave.report` — SQL view combining allocations and leave requests (line 5–9)
- `_auto = False` — built as PostgreSQL view via `init` method (line 34–35)
- Exposes: `leave_id`, `allocation_id`, `employee_id`, `number_of_days`, `leave_type` (allocation/request), `state`, `date_from`, `date_to`, `company_id`
- Note: leave requests appear with **negative** `number_of_days` (line 72) to represent consumption

**Calendar report:** `hr_leave_report_calendar.py` — separate view for calendar display

**Employee type report:** `hr_leave_employee_type_report.py` — per-employee per-type summary

---

## L11 — Duration Calculation Notes

`_get_durations` (`hr_leave.py` around line 565–683):
- Handles flexible employees: uses actual hours directly
- Handles standard employees: uses `_list_work_time_per_day` (for day-unit) or `_get_work_days_data_batch` (for hour/half-day unit)
- Public holidays optionally excluded via `include_public_holidays_in_duration` flag
- Days are rounded up to full day for `request_unit == 'day'` (line 678–679)

---

## Key Finding
The state machine for leave requests in Odoo 19 has NO 'draft' state — requests are created directly in 'confirm'. Dual validation adds an intermediate 'validate1' state. The integration with hr.work.entry (bridge module `hr_work_entry_holidays`) is auto-installed and automatically creates/archives work entries on leave approval/refusal, replacing pre-existing attendance entries for the leave period. Payroll deductions require Enterprise modules; Community installs get the work entry bridge but no payslip-level deduction.
