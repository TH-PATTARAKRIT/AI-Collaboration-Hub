# U198 — hr_timesheet: Timesheet Model, Project Link, Analytic Line Creation
## STATE03 VDR — Restricted Technical Evidence

**Research Unit**: U198  
**Module**: hr_timesheet (primary), project, analytic  
**Odoo Version**: 19.0.post20260921 (Community)  
**Date**: 2026-10-02  
**Gate**: GREEN  

---

## 1. Module Structure and Dependencies

**File**: `hr_timesheet/__manifest__.py`

```
'depends': ['hr', 'hr_hourly_cost', 'analytic', 'project', 'uom']
```

Key dependency: `hr_hourly_cost` provides `hourly_cost` field on `hr.employee` (Monetary, groups=`hr.group_hr_user`, default=0.0). This is distinct from `hr_timesheet` itself.

---

## 2. account.analytic.line — Base Model

**File**: `analytic/models/analytic_line.py` : lines 163–274

Base `account.analytic.line` fields (before hr_timesheet extension):

| Field | Type | Notes |
|-------|------|-------|
| name | Char | required |
| date | Date | required, default=today |
| amount | Monetary | required, default=0.0 |
| unit_amount | Float | default=0.0 — hours/days quantity |
| product_uom_id | Many2one(uom.uom) | unit |
| partner_id | Many2one(res.partner) | check_company |
| user_id | Many2one(res.users) | index |
| company_id | Many2one(res.company) | required, readonly, default=env.company |
| currency_id | related company_id.currency_id | store=True, compute_sudo=True |
| account_id | Many2one(account.analytic.account) | from AnalyticPlanFieldsMixin, index, check_company |

The `account_id` field is defined in `AnalyticPlanFieldsMixin` (abstract model `analytic.plan.fields.mixin`) at line 16, not directly on `account.analytic.line`.

---

## 3. account.analytic.line — hr_timesheet Extension

**File**: `hr_timesheet/models/hr_timesheet.py` : lines 16–561

```python
class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
```

### 3.1 Added Fields (hr_timesheet-specific)

| Field | Type | Definition line | Notes |
|-------|------|----------------|-------|
| task_id | Many2one(project.task) | line 62 | compute=_compute_task_id, store=True, readonly=False, index='btree_not_null' |
| parent_task_id | Many2one(project.task) | line 66 | related='task_id.parent_id', store=True, index='btree_not_null' |
| project_id | Many2one(project.project) | line 67 | compute=_compute_project_id, inverse=_inverse_project_id, store=True, readonly=False, index=True |
| user_id | Many2one(res.users) | line 70 | compute=_compute_user_id, store=True, readonly=False (override) |
| employee_id | Many2one(hr.employee) | line 71 | index=True, help mentions 'hourly cost' |
| job_title | Char | line 73 | related='employee_id.job_title' |
| department_id | Many2one(hr.department) | line 74 | compute=_compute_department_id, store=True, compute_sudo=True |
| manager_id | Many2one(hr.employee) | line 75 | related='employee_id.parent_id', store=True |
| encoding_uom_id | Many2one(uom.uom) | line 76 | compute=_compute_encoding_uom_id |
| partner_id | Many2one(res.partner) | line 77 | compute=_compute_partner_id, store=True, readonly=False (override) |
| readonly_timesheet | Boolean | line 78 | compute=_compute_readonly_timesheet, compute_sudo=True |
| milestone_id | Many2one(project.milestone) | line 79 | related='task_id.milestone_id' |
| message_partner_ids | Many2many(res.partner) | line 80 | compute=_compute_message_partner_ids |
| calendar_display_name | Char | line 81 | compute=_compute_calendar_display_name |

### 3.2 Compute Logic — Key Relationships

**_compute_encoding_uom_id** (line 127):
```python
analytic_line.encoding_uom_id = analytic_line.company_id.timesheet_encode_uom_id
```
Encoding UOM is inherited from the company's `timesheet_encode_uom_id`.

**_compute_project_id** (line 138):
```python
@api.depends('task_id.project_id')
def _compute_project_id(self):
    for line in self:
        if not line.task_id.project_id or line.project_id == line.task_id.project_id:
            continue
        line.project_id = line.task_id.project_id
```
project_id is derived from task when task has a project.

**_inverse_project_id** (line 145):
```python
def _inverse_project_id(self):
    for line in self:
        if line.task_id.project_id != line.project_id:
            line.sudo().task_id = False
```
When project changes and it mismatches the task's project, task is cleared.

**_compute_task_id** (line 150):
```python
@api.depends('project_id')
def _compute_task_id(self):
    self.filtered(lambda t: not t.project_id).task_id = False
```
Removes task when project is removed.

**_compute_user_id** (line 162):
```python
@api.depends('employee_id.user_id')
def _compute_user_id(self):
    for line in self:
        line.user_id = line.employee_id.user_id if line.employee_id else self._default_user()
```
user_id is derived from employee.

**_compute_partner_id** (line 131):
```python
@api.depends('task_id.partner_id', 'project_id.partner_id')
def _compute_partner_id(self):
    super()._compute_partner_id()
    for timesheet in self:
        if timesheet.project_id:
            timesheet.partner_id = timesheet.task_id.partner_id or timesheet.project_id.partner_id
```

---

## 4. Analytic Line Create/Write Flow

**File**: `hr_timesheet/models/hr_timesheet.py` : lines 219–392

### 4.1 create() — lines 219–362

The create method is highly detailed:

1. **Calendar validation** (if `timesheet_calendar` context): Checks that employee has valid working intervals on the date; skips creation for non-working days.

2. **Project/task validation** (lines 245–262): 
   - If task has no project_id → raises `ValidationError('Timesheets cannot be created on a private task.')`
   - If task provided without project → `vals['project_id'] = task.project_id.id`
   - Sets `company_id` from task or project company

3. **Analytic account preprocessing** (line 258–262):
   ```python
   vals.update({
       fname: account_id
       for fname, account_id in self._timesheet_preprocess_get_accounts(vals).items()
       if fname not in vals
   })
   ```

4. **UOM defaulting** (lines 264–265):
   ```python
   if not vals.get('product_uom_id'):
       vals['product_uom_id'] = company.project_time_mode_id.id
   ```

5. **Name defaulting** (lines 267–268):
   ```python
   if not vals.get('name'):
       vals['name'] = '/'
   ```

6. **Employee resolution** (lines 279–337): Complex multi-step lookup mapping user_id to employee_id with company filtering.

7. **Post-process** (lines 342–344):
   ```python
   for line, values in zip(lines, vals_list):
       if line.project_id:  # applied only for timesheet
           line._timesheet_postprocess(values)
   ```

### 4.2 write() — lines 364–391

Similar preprocessing of analytic accounts. Calls `_timesheet_postprocess()` on lines with `project_id`.

### 4.3 _timesheet_preprocess_get_accounts() — lines 423–439

**File**: `hr_timesheet/models/hr_timesheet.py` : lines 423–439

```python
def _timesheet_preprocess_get_accounts(self, vals):
    project = self.env['project.project'].sudo().browse(vals.get('project_id'))
    if not project:
        return {}
    company = self.env['res.company'].browse(vals.get('company_id'))
    mandatory_plans = [plan for plan in self._get_mandatory_plans(company, business_domain='timesheet')
                       if plan['column_name'] != 'account_id']
    missing_plan_names = [plan['name'] for plan in mandatory_plans if not project[plan['column_name']]]
    if missing_plan_names:
        raise ValidationError(...)
    return {
        fname: project[fname].id
        for fname in self._get_plan_fnames()
    }
```
Copies analytic plan account fields FROM the project TO the timesheet line.

### 4.4 _timesheet_postprocess() and _timesheet_postprocess_values() — lines 441–480

**File**: `hr_timesheet/models/hr_timesheet.py` : lines 441–480

```python
def _timesheet_postprocess(self, values):
    sudo_self = self.sudo()
    values_to_write = self._timesheet_postprocess_values(values)
    for timesheet in sudo_self:
        if values_to_write[timesheet.id]:
            timesheet.write(values_to_write[timesheet.id])
    return values

def _timesheet_postprocess_values(self, values):
    result = {id_: {} for id_ in self.ids}
    sudo_self = self.sudo()
    if any(field_name in values for field_name in ['unit_amount', 'employee_id', 'account_id']):
        for timesheet in sudo_self:
            if not timesheet.account_id.active:
                raise ValidationError(...)
            accounts = timesheet._get_analytic_accounts()
            companies = timesheet.company_id | accounts.company_id | timesheet.task_id.company_id | timesheet.project_id.company_id
            if len(companies) > 1:
                raise ValidationError('The project, the task and the analytic accounts of the timesheet must belong to the same company.')
            cost = timesheet._hourly_cost()
            amount = -timesheet.unit_amount * cost
            amount_converted = timesheet.employee_id.currency_id._convert(
                amount, timesheet.account_id.currency_id or timesheet.currency_id, self.env.company, timesheet.date)
            result[timesheet.id].update({'amount': amount_converted})
    return result
```

**Key**: `amount = -unit_amount * hourly_cost`. The amount is negative (cost is a debit in analytic accounting). Currency conversion is applied from employee's currency to account's currency.

### 4.5 _hourly_cost() — lines 503–505

```python
def _hourly_cost(self):
    self.ensure_one()
    return self.employee_id.hourly_cost or 0.0
```

`employee_id.hourly_cost` is defined in `hr_hourly_cost/models/hr_employee.py` line 9. If employee has no hourly_cost, amount=0.

---

## 5. project.project — hr_timesheet Extension

**File**: `hr_timesheet/models/project_project.py` : lines 10–296

### 5.1 Base account_id field

**File**: `project/models/project_project.py` : line 98

```python
account_id = fields.Many2one('account.analytic.account', copy=False,
    domain="['|', ('company_id', '=', False), ('company_id', '=?', company_id)]",
    ondelete='set null')
```
This is the primary analytic account field on `project.project`. Named `account_id` NOT `analytic_account_id`.

### 5.2 allow_timesheets field

**File**: `hr_timesheet/models/project_project.py` : line 13

```python
allow_timesheets = fields.Boolean(
    "Timesheets", compute='_compute_allow_timesheets', store=True, readonly=False,
    default=True)
```

**_compute_allow_timesheets** (lines 47–49):
```python
@api.depends('account_id')
def _compute_allow_timesheets(self):
    without_account = self.filtered(lambda t: t._origin and not t.account_id)
    without_account.update({'allow_timesheets': False})
```
If the existing project has no analytic account, allow_timesheets=False.

### 5.3 Analytic account auto-creation

**create()** (lines 131–140):
```python
if analytic_accounts_vals := self._get_processed_analytic_account_vals(vals_list):
    analytic_accounts = self.env['account.analytic.account'].create(...)
    for vals, analytic_account in zip(analytic_accounts_vals, analytic_accounts):
        vals['account_id'] = analytic_account.id
return super().create(vals_list)
```

**write()** (lines 142–148):
```python
if vals.get('allow_timesheets') and not vals.get('account_id'):
    project_wo_account = self.filtered(lambda project: not project.account_id and not project.is_template)
    if project_wo_account:
        project_wo_account._create_analytic_account()
```

Constraint `_check_allow_timesheet` (lines 98–106): Raises if `allow_timesheets=True` but no `account_id` and not a template.

### 5.4 Time tracking fields on project.project

| Field | Line | Type | Compute |
|-------|------|------|---------|
| allow_timesheets | 13 | Boolean | _compute_allow_timesheets (depends account_id) |
| timesheet_ids | 25 | One2many(account.analytic.line, project_id) | — |
| timesheet_encode_uom_id | 26 | Many2one(uom.uom) | _compute_timesheet_encode_uom_id |
| total_timesheet_time | 27 | Float | _compute_total_timesheet_time (groups=timesheet_user) |
| is_internal_project | 31 | Boolean | _compute_is_internal_project |
| remaining_hours | 32 | Float | _compute_remaining_hours, compute_sudo=True |
| is_project_overtime | 33 | Boolean | _compute_remaining_hours |
| allocated_hours | 34 | Float | tracking=True |
| effective_hours | 35 | Float | _compute_remaining_hours, compute_sudo=True |

**_compute_remaining_hours** (lines 68–79):
```python
@api.depends('allow_timesheets', 'timesheet_ids.unit_amount', 'allocated_hours')
def _compute_remaining_hours(self):
    timesheets_read_group = self.env['account.analytic.line']._read_group(
        [('project_id', 'in', self.ids)], ['project_id'], ['unit_amount:sum'])
    timesheet_time_dict = {project.id: unit_amount_sum for project, unit_amount_sum in timesheets_read_group}
    for project in self:
        project.effective_hours = round(timesheet_time_dict.get(project.id, 0.0), 2)
        project.remaining_hours = project.allocated_hours - project.effective_hours
        project.is_project_overtime = project.remaining_hours < 0
```

---

## 6. project.task — hr_timesheet Extension

**File**: `hr_timesheet/models/project_task.py` : lines 29–291

### 6.1 Timesheet Fields on project.task

| Field | Line | Type | Notes |
|-------|------|------|-------|
| allow_timesheets | 34 | Boolean | compute=_compute_allow_timesheets, search=_search_allow_timesheets, compute_sudo, readonly |
| analytic_account_active | 33 | Boolean | related='project_id.analytic_account_active' |
| remaining_hours | 38 | Float | compute=_compute_remaining_hours, store=True, readonly |
| remaining_hours_percentage | 39 | Float | compute, search |
| effective_hours | 40 | Float | compute=_compute_effective_hours, compute_sudo, store=True |
| total_hours_spent | 41 | Float | compute=_compute_total_hours_spent, store=True |
| progress | 42 | Float | compute=_compute_progress_hours, store=True, aggregator='avg' |
| overtime | 43 | Float | compute=_compute_progress_hours, store=True |
| subtask_effective_hours | 44 | Float | compute=_compute_subtask_effective_hours, recursive=True, store=True |
| timesheet_ids | 45 | One2many(account.analytic.line, task_id) | — |
| encode_uom_in_days | 46 | Boolean | compute=_compute_encode_uom_in_days |
| allocated_hours | — | Float | from base project.task (project/models/project_task.py:196) |

### 6.2 Computation Logic

**_compute_effective_hours** (lines 83–92):
```python
@api.depends('timesheet_ids.unit_amount')
def _compute_effective_hours(self):
    if not any(self._ids):
        for task in self:
            task.effective_hours = sum(task.timesheet_ids.mapped('unit_amount'))
        return
    timesheet_read_group = self.env['account.analytic.line']._read_group(
        [('task_id', 'in', self.ids)], ['task_id'], ['unit_amount:sum'])
    timesheets_per_task = {task.id: amount for task, amount in timesheet_read_group}
    for task in self:
        task.effective_hours = timesheets_per_task.get(task.id, 0.0)
```

**_compute_remaining_hours** (lines 127–133):
```python
@api.depends('effective_hours', 'subtask_effective_hours', 'allocated_hours')
def _compute_remaining_hours(self):
    for task in self:
        if not task.allocated_hours:
            task.remaining_hours = 0.0
        else:
            task.remaining_hours = task.allocated_hours - task.effective_hours - task.subtask_effective_hours
```

**_compute_subtask_effective_hours** (lines 140–143):
```python
@api.depends('child_ids.effective_hours', 'child_ids.subtask_effective_hours')
def _compute_subtask_effective_hours(self):
    for task in self.with_context(active_test=False):
        task.subtask_effective_hours = sum(
            child_task.effective_hours + child_task.subtask_effective_hours
            for child_task in task.child_ids)
```
Recursive (uses `recursive=True` on the field).

**_compute_progress_hours** (lines 94–103):
```python
@api.depends('effective_hours', 'subtask_effective_hours', 'allocated_hours')
def _compute_progress_hours(self):
    for task in self:
        if (task.allocated_hours > 0.0):
            task_total_hours = task.effective_hours + task.subtask_effective_hours
            task.overtime = max(task_total_hours - task.allocated_hours, 0)
            task.progress = round(task_total_hours / task.allocated_hours, 2)
        else:
            task.progress = 0.0
            task.overtime = 0
```

---

## 7. res.company — hr_timesheet Extension

**File**: `hr_timesheet/models/res_company.py` : lines 8–66

Key fields:
- `project_time_mode_id` — Many2one(uom.uom), default=hours, UOM used in projects/tasks
- `timesheet_encode_uom_id` — Many2one(uom.uom), default=hours, encoding UOM for timesheets  
- `internal_project_id` — Many2one(project.project), default Internal project (auto-created on company create)

Company auto-creates an internal project (`_create_internal_project_task`, lines 46–66) when a new company is created.

---

## 8. Multi-company Handling

**File**: `hr_timesheet/models/hr_timesheet.py` : lines 256–257 and 469–471

**During create**:
```python
company = task.company_id or project.company_id or self.env['res.company'].browse(vals.get('company_id'))
vals['company_id'] = company.id
```

**During _timesheet_postprocess_values**:
```python
accounts = timesheet._get_analytic_accounts()
companies = timesheet.company_id | accounts.company_id | timesheet.task_id.company_id | timesheet.project_id.company_id
if len(companies) > 1:
    raise ValidationError('The project, the task and the analytic accounts of the timesheet must belong to the same company.')
```
Cross-company timesheet creation is blocked.

---

## 9. Timesheet Approval / Validation

**No timesheet approval flow exists in Community 19.**

The `_is_readonly()` method (line 112) always returns `False` in Community:
```python
def _is_readonly(self):
    self.ensure_one()
    # is overridden in other timesheet related modules
    return False
```

`readonly_timesheet` field (line 78) is computed via `_compute_readonly_timesheet()` (lines 117–125). It checks `_is_readonly()` and restricts portal users.

The `hr_timesheet_sheet` module (timesheet approval/validation with draft/confirmed/done states) was an Enterprise feature in v16/v17 and is NOT present in Community 19 or v19 at all.

---

## 10. Security Groups

```
group_hr_timesheet_user    — basic timesheet user (view own timesheets)
group_hr_timesheet_approver — can see all timesheets, approve
group_timesheet_manager    — full manager access
```

**Domain for project_id** (line 51–54): Non-managers see only projects with `privacy_visibility in ['employees', 'portal']` or where they are followers.

**Domain for employee_id** (line 56–60): Non-approvers can only see own employee records.

---

## 11. analytic_applicability Extension

**File**: `hr_timesheet/models/analytic_applicability.py` : lines 6–15

Adds `'timesheet'` as a business_domain selection to `account.analytic.applicability`. This allows analytic plans to be configured as mandatory/optional for timesheets specifically.

---

## 12. MIGRATION FLAGS (v16/v17 → v19)

| Flag | Description |
|------|-------------|
| `sheet_id` field REMOVED | In v16, `hr_timesheet_sheet` (Enterprise) added `sheet_id` Many2one to `account.analytic.line`. This field does NOT exist in Community v19. Any migration from Enterprise v16 with timesheet sheets must handle this field. |
| `analytic_account_id` renamed → `account_id` | The project analytic field is `account_id` (not `analytic_account_id`) in v19 — actually this was `account_id` in v16 too, but important to note. |
| `planned_hours` renamed → `allocated_hours` | The `planned_hours` field on `project.task` (used in v16) is now `allocated_hours` in v19. |
| No `timesheet_manager_id` | No such field exists in Community v19. Was never in Community. |
| `timesheet_encode_uom_id` on company | In v16, this was set via `res.config.settings`. In v19, it's a company field accessed via settings inverse. |
| Amount sign convention unchanged | `amount = -unit_amount * hourly_cost` (negative = cost). Convention unchanged from v16/v17. |
| `product_uom_id` default from company | In v19, `product_uom_id` defaults to `company.project_time_mode_id` (not hardcoded hours). |

---

## 13. _get_timesheet_cost() — NOT PRESENT in Community 19

The function `_get_timesheet_cost()` does NOT exist in Community 19. The equivalent is `_hourly_cost()` at line 503 which returns `self.employee_id.hourly_cost or 0.0`. In Enterprise/sale_timesheet, the cost computation is overridden to incorporate billing policy.

---

## 14. Key Pointers Summary

| Topic | File | Lines |
|-------|------|-------|
| Base analytic line model | `analytic/models/analytic_line.py` | 163-274 |
| hr_timesheet AccountAnalyticLine | `hr_timesheet/models/hr_timesheet.py` | 16-561 |
| create() full logic | `hr_timesheet/models/hr_timesheet.py` | 219-362 |
| _timesheet_postprocess_values() | `hr_timesheet/models/hr_timesheet.py` | 450-480 |
| _hourly_cost() | `hr_timesheet/models/hr_timesheet.py` | 503-505 |
| project.project allow_timesheets | `hr_timesheet/models/project_project.py` | 13-15 |
| project.project account_id (base) | `project/models/project_project.py` | 98 |
| project.project auto-create analytic | `hr_timesheet/models/project_project.py` | 131-148 |
| project.task effective_hours | `hr_timesheet/models/project_task.py` | 40, 83-92 |
| project.task remaining_hours | `hr_timesheet/models/project_task.py` | 38, 127-133 |
| project.task allocated_hours | `project/models/project_task.py` | 196 |
| company timesheet_encode_uom_id | `hr_timesheet/models/res_company.py` | 24-25 |
| hourly_cost on employee | `hr_hourly_cost/models/hr_employee.py` | 9-10 |
| analytic_applicability business_domain | `hr_timesheet/models/analytic_applicability.py` | 7-15 |
