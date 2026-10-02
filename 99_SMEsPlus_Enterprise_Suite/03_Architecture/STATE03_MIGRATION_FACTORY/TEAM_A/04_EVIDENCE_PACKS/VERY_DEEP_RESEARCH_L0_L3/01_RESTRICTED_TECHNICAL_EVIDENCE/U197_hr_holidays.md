# U197 — hr_holidays: Leave Request and Allocation Model
## STATE03 VDR — Restricted Technical Evidence (L0–L3)

**Source tree (READ-ONLY):**
`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_holidays/`

**Module version:** 1.6 (manifest)
**Research date:** 2026-10-02

---

## 1. hr.leave — State Machine

**File:** `models/hr_leave.py`

### States (line 129–135)
```python
state = fields.Selection([
    ('confirm', 'To Approve'),
    ('refuse', 'Refused'),
    ('validate1', 'Second Approval'),
    ('validate', 'Approved'),
    ('cancel', 'Cancelled'),
], default='confirm')
```

**No `draft` state** — leaves are created directly in `confirm` state (default). This is a migration flag vs. v16/v17 where `draft` existed.

### State transitions — `_get_next_states_by_state()` (line 1412–1456)

- `confirm` → `validate1` (officer or time_off_manager, when `validation_type == 'both'`)
- `confirm` → `validate` (officer or time_off_manager with `validation_type == 'manager'`)
- `confirm` → `refuse` (officer or time_off_manager)
- `validate1` → `validate` (officer or time_off_manager)
- `validate1` → `refuse` (officer)
- `validate` → `refuse` (officer)
- `validate`, `validate1`, `refuse` → `cancel` (own leave only, non-past unless officer)

### Key action methods

| Method | File:line | Transitions |
|--------|-----------|-------------|
| `action_approve()` | hr_leave.py:1188 | confirm→validate1 OR confirm→validate (routes by `can_validate`) |
| `_action_validate()` | hr_leave.py:1276 | Sets state='validate'; calls `_validate_leave_request()` |
| `action_refuse()` | hr_leave.py:1303 | confirm/validate1/validate → refuse |
| `_move_validate_leave_to_confirm()` | hr_leave.py:1209 | validate→confirm (back-to-approval) |
| `_action_user_cancel()` | hr_leave.py:1342 | validate/validate1/refuse → cancel (own only) |

### Who can validate

Determined by `_check_approval_update()` (line 1458) and `_get_next_states_by_state()` (line 1412):

- **Superuser:** always allowed (line 1460)
- **`group_hr_holidays_user` (Officer):** full access to all state transitions
- **`leave_manager_id` on employee (time_off_manager):** can validate/refuse based on `validation_type`
- **Employees cannot validate their own leaves** (checked at line 950 in allocation; same principle in leave via `is_own_leave`)

`leave_validation_type` on `hr.leave.type` controls the flow:
- `no_validation` — auto-approved
- `hr` — by Time Off Officer
- `manager` — by Employee's Approver
- `both` — both approvals required (uses validate1 intermediate state)

---

## 2. hr.leave Key Fields

**File:** `models/hr_leave.py`

| Field | Type | Line | Notes |
|-------|------|------|-------|
| `state` | Selection | 129 | confirm/refuse/validate1/validate/cancel |
| `holiday_status_id` | Many2one → hr.leave.type | 138 | Required |
| `employee_id` | Many2one → hr.employee | 153 | Required |
| `company_id` | Many2one → res.company | 157 | Computed from employee_company_id (line 694) |
| `employee_company_id` | related employee.company_id | 156 | Stored |
| `date_from` | Datetime (computed) | 172 | Computed from request_date_from (line 462) |
| `date_to` | Datetime (computed) | 174 | Computed from request_date_to (line 462) |
| `request_date_from` | Date | 212 | User-facing start date (NOT date_from) |
| `request_date_to` | Date | 213 | User-facing end date (NOT date_to) |
| `number_of_days` | Float (computed, stored) | 176 | Duration in days |
| `number_of_hours` | Float (computed, stored) | 179 | Duration in hours |
| `validation_type` | related holiday_status_id.leave_validation_type | 150 | |
| `max_leaves` | Float (computed) | 168 | From `_compute_leaves()` |
| `virtual_remaining_leaves` | Float (computed) | 169 | Available balance |
| `first_approver_id` | Many2one → hr.employee | 186 | Written by action_approve |
| `second_approver_id` | Many2one → hr.employee | 189 | Written by _action_validate for 'both' |
| `can_approve` | Boolean (computed) | 193 | _check_approval_update('validate1') |
| `can_validate` | Boolean (computed) | 194 | _check_approval_update('validate') |

**MIGRATION FLAG:** `date_from`/`date_to` are now fully computed fields derived from `request_date_from`/`request_date_to`. In v16, `date_from`/`date_to` were the primary input fields. Direct writes to `date_from`/`date_to` are rejected (comment at line 210).

---

## 3. hr.leave Balance Computation

**`_compute_leaves()` (hr_leave.py:770)**

```python
def _compute_leaves(self):
    date_from = ...fields.Date.today()
    employee_days_per_allocation = self.employee_id._get_consumed_leaves(
        self.holiday_status_id, date_from)[0]
    for leave in self:
        virtual_remaining_leaves = 0
        max_leaves = 0
        for allocation, allocation_dict in employee_days_per_allocation[...]:
            if allocation and (not allocation.date_to or allocation.date_to >= date_from):
                max_leaves += allocation_dict['max_leaves']
                virtual_remaining_leaves += allocation_dict['virtual_remaining_leaves']
        leave.virtual_remaining_leaves = virtual_remaining_leaves
        leave.max_leaves = max_leaves
```

**`_get_consumed_leaves()` (hr_employee.py:415)** — aggregates validated allocations and leaves in `confirm/validate1/validate` state to produce per-allocation balance data.

---

## 4. Leave Balance Enforcement

**`_check_validity()` (hr_leave.py:806)**

Called on create/write (line 943, 1005). Raises `ValidationError` when:
- Leave type `requires_allocation=True` but employee has no allocation (`max_leaves == 0` → line 822)
- `allows_negative=True`: allows overdraft up to `max_allowed_negative` (line 815–828)
- `allows_negative=False`: raises if new leaves increase excess count vs. previous state (line 839–844)

---

## 5. hr.leave.allocation Model

**File:** `models/hr_leave_allocation.py`

### Allocation types (line 119–122)
```python
allocation_type = fields.Selection([
    ('regular', 'Regular Allocation'),
    ('accrual', 'Accrual Allocation')
], default='regular', required=True, readonly=True)
```

### Key fields

| Field | Type | Line | Notes |
|-------|------|------|-------|
| `state` | Selection | 58–66 | confirm/refuse/validate1/validate (NO `draft`) |
| `date_from` | Date | 67 | Start of validity (required) |
| `date_to` | Date | 69 | End of validity (optional) |
| `allocation_type` | Selection | 119 | regular or accrual |
| `accrual_plan_id` | Many2one → hr.leave.accrual.plan | 124 | Used only for accrual type |
| `number_of_days` | Float (store, readonly=False) | 82 | Manual allocation amount |
| `number_of_days_display` | Float (computed) | 85 | For accrual: theoretical grant amount |
| `lastcall` | Date | 112 | Last accrual computation date |
| `nextcall` | Date | 116 | Next accrual trigger date |
| `validation_type` | related allocation_validation_type | 101 | From leave type |
| `approver_id` | Many2one → hr.employee | 95 | First approver |
| `second_approver_id` | Many2one → hr.employee | 98 | Second approver |

### Allocation approval chain

- `action_approve()` (line 899): routes to `validate1` (if can_approve) or `_action_validate()` (if can_validate)
- `_action_validate()` (line 916): sets state='validate', writes approver_id / second_approver_id
- `action_refuse()` (line 929): requires state in confirm/validate/validate1

---

## 6. hr.leave.accrual.plan

**File:** `models/hr_leave_accrual_plan.py`

| Field | Line | Notes |
|-------|------|-------|
| `name` | 15 | Plan name |
| `time_off_type_id` | 16 | Optional; restricts to one leave type |
| `level_ids` | 21 | One2many → hr.leave.accrual.level |
| `company_id` | 24 | Computed from time_off_type_id.company_id or env.company |
| `transition_mode` | 26 | immediately / end_of_accrual |
| `is_based_on_worked_time` | 31 | Excludes unpaid leaves from computation |
| `accrued_gain_time` | 34 | start / end of accrual period |
| `can_be_carryover` | 39 | Boolean |
| `carryover_date` | 40 | year_start / allocation / other |
| `added_value_type` | 63 | day / hour (plan-level default) |

---

## 7. hr.leave.accrual.level

**File:** `models/hr_leave_accrual_plan_level.py`

| Field | Line | Notes |
|-------|------|-------|
| `accrual_plan_id` | 21 | Parent plan |
| `start_count` + `start_type` | 23–30 | Delay before level activates (days/months/years) |
| `milestone_date` | 31 | creation / after |
| `added_value` | 39 | Accrual rate amount (digits 16,5) |
| `added_value_type` | 40 | day / hour |
| `frequency` | 45 | hourly/daily/weekly/bimonthly/monthly/biyearly/yearly |
| `cap_accrued_time` | 104 | Boolean: cap balance |
| `maximum_leave` | 106 | Maximum balance cap |
| `cap_accrued_time_yearly` | 109 | Annual accrual cap |
| `maximum_leave_yearly` | 112 | Annual cap amount |
| `action_with_unused_accruals` | 115 | lost / all (carry-over) |
| `carryover_options` | 125 | unlimited / limited |
| `postpone_max_days` | 134 | Max carry-over days |

---

## 8. hr.leave.type (hr.leave.type)

**File:** `models/hr_leave_type.py`

| Field | Line | Notes |
|-------|------|-------|
| `name` | 44 | Required, translatable |
| `leave_validation_type` | 87 | no_validation/hr/manager/both |
| `allocation_validation_type` | 96 | no_validation/hr/manager/both |
| `requires_allocation` | 92 | Boolean (default True) |
| `employee_requests` | 93 | Boolean: allow self-allocation requests |
| `company_id` | 73 | Optional; scopes leave type to company |
| `country_id` | 75 | Computed from company, stored |
| `request_unit` | 109 | day/half_day/hour |
| `unpaid` | 113 | Boolean |
| `allows_negative` | 125 | Allow overdraft |
| `max_allowed_negative` | 127 | Max overdraft days |
| `accruals_ids` | 122 | One2many → hr.leave.accrual.plan |
| `time_type` | 107 | other (Worked Time) / leave (Absence) |
| `support_document` | 117 | Requires supporting doc |
| `include_public_holidays_in_duration` | 114 | Ignore public holidays |

---

## 9. Multi-Company Scoping

**hr.leave.company_id** (hr_leave.py:157, 694):
```python
holiday.company_id = holiday.employee_company_id or holiday.department_id.company_id or self.env.company
```
Derived from the employee's company, not directly set.

**hr.leave.type.company_id** (hr_leave_type.py:73):
Optional field. When set, only employees of that company can use this leave type. The `_domain_holiday_status_id` in allocation (line 35) filters by `company_id in env.companies.ids + [False]`.

**hr.leave.accrual.plan.company_id** (hr_leave_accrual_plan.py:24):
Computed from `time_off_type_id.company_id` or `env.company`.

**Security rules** (upgrades/1.6/pre-migrate.py):
Domain updated to: `["|", ("employee_id", "=", False), ("employee_id.company_id", "in", company_ids), "|", ("holiday_status_id.company_id", "=", False), ("holiday_status_id.company_id", "in", company_ids)]`

---

## 10. Migration Flags (v16/v17 → v19)

| Flag | Detail |
|------|--------|
| **No `draft` state on hr.leave** | hr.leave default state is `confirm`; `draft` state removed. Any v16/v17 records in `draft` must be migrated to `confirm` or handled. |
| **date_from/date_to are computed, not input** | `request_date_from` / `request_date_to` are now the input fields. Direct writes to `date_from`/`date_to` are rejected. v17 called these `holiday_date_from`/`holiday_date_to` in some versions — check source records. |
| **hr.leave.report remains** | `hr.leave.report` still exists as a SQL view (report/hr_leave_report.py:6), not removed. |
| **allocation_type field is readonly=True** | Cannot change after creation (line 122). |
| **can_be_carryover on accrual plan** | New field in this version; ensure accrual plan migration sets this. |
| **allows_negative + max_allowed_negative** | New negative cap feature on hr.leave.type; no equivalent in v16. |

---

## 11. `_get_responsible_for_approval()` (hr_leave.py:1539)

Determines notification recipients:
- `validation_type == 'manager'` or `both` + state `confirm`: employee's `leave_manager_id`, or `parent_id.user_id`, or `responsible_ids`
- `validation_type == 'hr'` or `both` + state `validate1`: `holiday_status_id.responsible_ids`
