# U230 — hr.version: New Model Replacing hr.contract in Odoo 19 CE
## Restricted Technical Evidence Pack

**Unit:** U230  
**Module:** hr (hr.version)  
**Source tree:** `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons`  
**Research date:** 2026-10-02  
**Gate:** GREEN

---

## 1. Model Existence Confirmed

`hr.version` is declared at:

- **File:** `hr/models/hr_version.py`
- **Line 35:** `_name = 'hr.version'`
- **Line 36:** `_description = 'Version'`
- **Line 37:** `_inherit = ['mail.thread', 'mail.activity.mixin']`
- **Line 39:** `_order = 'date_version'`

The model is registered in `hr/models/__init__.py` line 5: `from . import hr_version`.

---

## 2. hr.employee._inherits Confirmed

**File:** `hr/models/hr_employee.py`

- **Line 45:** `_inherits = {'hr.version': 'version_id'}`

The `version_id` field on `hr.employee` is declared at lines 48–56:

```python
version_id = fields.Many2one(
    'hr.version',
    compute='_compute_version_id',
    search='_search_version_id',
    ondelete='cascade',
    required=True,
    store=False,
    compute_sudo=True,
    groups="hr.group_hr_user")
```

Key attributes:
- **Not stored** (`store=False`) — computed dynamically
- `ondelete='cascade'` — employee deletion cascades to version
- `required=True` — employees cannot exist without a version
- `groups="hr.group_hr_user"` — HR user group required

---

## 3. version_id Computation Logic

**File:** `hr/models/hr_employee.py`, lines 504–515

```python
@api.depends('current_version_id')
@api.depends_context('version_id')
def _compute_version_id(self):
    context_version_id = self.env.context.get('version_id', False)
    context_version = self.env['hr.version'].browse(context_version_id).exists() if context_version_id else self.env['hr.version']

    for employee in self:
        if context_version.employee_id == self:
            version = context_version
        else:
            version = employee.current_version_id
        employee.version_id = version
```

`version_id` resolves to:
1. The context-supplied `version_id` if it belongs to this employee
2. Otherwise `current_version_id` (the latest version effective today)

---

## 4. current_version_id Field

**File:** `hr/models/hr_employee.py`, lines 57–62:

```python
current_version_id = fields.Many2one(
    'hr.version',
    compute='_compute_current_version_id',
    store=True,
    bypass_search_access=True,
)
```

Computed at lines 527–542:
```python
@api.depends('version_ids.date_version', 'version_ids.active', 'active')
def _compute_current_version_id(self):
    for employee in self:
        version = self.env['hr.version'].search(
            [('employee_id', 'in', employee.ids), ('date_version', '<=', fields.Date.today())],
            order='date_version desc',
            limit=1,
        )
        new_current_version = False
        if version:
            new_current_version = version
        elif employee.version_ids:
            new_current_version = employee.version_ids[0]
        if employee.current_version_id != new_current_version:
            employee.current_version_id = new_current_version
```

`current_version_id` is **stored** and triggers on version date changes. A cron `_cron_update_current_version_id` (line 544) recomputes it daily.

---

## 5. version_ids One2many

**File:** `hr/models/hr_employee.py`, lines 68–74:

```python
version_ids = fields.One2many(
    'hr.version',
    'employee_id',
    string='Employee Versions',
    groups="hr.group_hr_user",
    required=True
)
```

An employee has a history of versions. At least one must always exist (enforced by `_unlink_except_last_version` at `hr_version.py` lines 294–299).

---

## 6. hr.version Key Fields

All fields confirmed at `hr/models/hr_version.py`:

### Work / Job Information
| Field | Type | Line |
|---|---|---|
| `department_id` | Many2one('hr.department') | 127 |
| `job_id` | Many2one('hr.job') | 130 |
| `job_title` | Char (computed from job_id.name) | 131 |
| `address_id` | Many2one('res.partner') | 134 |
| `work_location_id` | Many2one('hr.work.location') | 142 |
| `employee_type` | Selection | 119 |

### Contract Fields (previously on hr.contract)
| Field | Type | Line |
|---|---|---|
| `contract_date_start` | Date | 156 |
| `contract_date_end` | Date | 157 |
| `trial_date_end` | Date | 160 |
| `date_start` | Date (computed) | 162 |
| `date_end` | Date (computed) | 163 |
| `wage` | Monetary | 178 |
| `contract_wage` | Monetary (computed) | 180 |
| `contract_type_id` | Many2one('hr.contract.type') | 185 |
| `structure_type_id` | Many2one('hr.payroll.structure.type') | 173 |
| `contract_template_id` | Many2one('hr.version') | 169 |
| `hr_responsible_id` | Many2one('res.users') | 192 |

### Version Metadata
| Field | Type | Line |
|---|---|---|
| `date_version` | Date (required) | 64 |
| `employee_id` | Many2one('hr.employee') | 54 |
| `company_id` | Many2one('res.company', computed) | 52 |
| `active` | Boolean | 62 |
| `name` | Char | 60 |

### Personal Information (now versioned)
| Field | Line |
|---|---|
| `country_id` | 71 |
| `identification_id` | 73 |
| `ssnid` | 78 |
| `passport_id` | 80 |
| `sex` | 81 |
| `marital` | 107 |
| `private_street`/`private_city`/etc. | 87–95 |

### Status Computed Fields
| Field | Line |
|---|---|
| `is_current` | 164 |
| `is_past` | 165 |
| `is_future` | 166 |
| `is_in_contract` | 167 |

### Departure
| Field | Line |
|---|---|
| `departure_reason_id` | 145 |
| `departure_description` | 147 |
| `departure_date` | 148 |

### Working Hours
| Field | Line |
|---|---|
| `resource_calendar_id` | 150 |
| `is_flexible` | 151 |
| `is_fully_flexible` | 152 |

---

## 7. hr.contract ABSENT from CE19

Exhaustive grep for `_name = 'hr.contract'` and `class HrContract` across all CE19 addons returned **zero results**. The `hr.contract` model does not exist in Odoo 19 Community Edition.

Only `hr.contract.type` survives as a classification/lookup model (`hr/models/hr_contract_type.py`, line 8).

---

## 8. Delegated Field Access: department_id / job_id

Via `_inherits = {'hr.version': 'version_id'}`, when code accesses `employee.department_id`, Odoo's ORM delegates to the version table column. However, because `version_id` is computed (not stored), the ORM requires special handling.

**File:** `hr/models/hr_employee.py`, lines 181–192 show these fields explicitly re-declared as `related` with `inherited=True`:

```python
contract_date_start = fields.Date(readonly=False, related="version_id.contract_date_start", inherited=True, ...)
contract_date_end = fields.Date(readonly=False, related="version_id.contract_date_end", inherited=True, ...)
...
structure_type_id = fields.Many2one(readonly=False, related='version_id.structure_type_id', inherited=True, ...)
contract_type_id = fields.Many2one(readonly=False, related='version_id.contract_type_id', inherited=True, ...)
```

The comment at line 180: "All version fields needing a specific group to be accessible should also have `inherited=True` set on its definition to make sure those fields are linked to `_inherits` on `hr.version`."

`department_id` and `job_id` are inherited via the `_inherits` mechanism directly — they reside on `hr_version` table and are accessed through delegation. For SQL queries, the `_field_to_sql` override at line 553–557 maps `version_id` to `current_version_id`:

```python
def _field_to_sql(self, alias: str, field_expr: str, query: (Query | None) = None) -> SQL:
    if field_expr == 'version_id':
        field_expr = 'current_version_id'
    return super()._field_to_sql(alias, field_expr, query)
```

---

## 9. hr.employee Public Model SQL JOIN

**File:** `hr/models/hr_employee_public.py`, lines 187–201:

```python
version_fields = self.env['hr.version']._fields
...
JOIN hr_version v
  ON v.id = e.current_version_id
```

The public employee view joins to `hr_version` via `current_version_id`.

---

## 10. hr.version Create Logic / Contract Templates

**File:** `hr_version.py`, lines 284–292:

```python
@api.model_create_multi
def create(self, vals_list):
    Version = self.env['hr.version']
    for vals in vals_list:
        if 'contract_template_id' in vals:
            contract_vals = Version.get_values_from_contract_template(...)
            vals.update({**contract_vals, **vals})
    return super().create(vals_list)
```

`hr.version` records without an `employee_id` serve as **contract templates**. The `contract_template_id` field (line 169) is a Many2one to `hr.version` itself with domain `employee_id = False`.

Template whitelist fields (`_get_whitelist_fields_from_template`, line 446):
`['job_id', 'department_id', 'contract_type_id', 'structure_type_id', 'wage', 'resource_calendar_id', 'hr_responsible_id']`

---

## 11. Version Lifecycle: create_version()

**File:** `hr/models/hr_employee.py`, lines 571–643

`create_version(values)` copies an existing version to a new date:
1. Finds the version effective at the requested `date_version`
2. Copies all fields to a new `hr.version` record
3. Applies override values
4. Returns the new version

`create_contract(date)` at lines 645–667 wraps `create_version` to also set `contract_date_start`.

---

## 12. Constraints and Data Integrity

**File:** `hr_version.py`:

- **Line 197–200:** `_check_contract_start_date_defined` — end date requires start date
- **Line 202–205:** `_check_unique_date_version` — unique index on `(employee_id, date_version)` where `active = TRUE AND employee_id IS NOT NULL`
- **Lines 294–299:** `_unlink_except_last_version` — cannot delete the last version of an employee
- **Lines 302–309:** `write()` — cannot archive all versions; cannot reassign all versions away from an employee
- **Lines 239–278:** `_check_dates()` — prevents contract date overlap for same employee

---

## 13. hr.department Structure (v19)

**File:** `hr/models/hr_department.py`

No structural changes. `member_ids` at line 26 is:
```python
member_ids = fields.One2many('hr.employee', 'department_id', ...)
```

Because `department_id` is on `hr.version` and delegated to `hr.employee`, `member_ids` effectively reads the current version's department. The field `manager_id` (line 25) remains Many2one to `hr.employee`.

---

## 14. resource_calendar_id Inverse

**File:** `hr_version.py`, lines 665–670:

```python
def _inverse_resource_calendar_id(self):
    for employee, versions in self.grouped('employee_id').items():
        current_version = employee.current_version_id
        for version in versions:
            if version == current_version and employee.resource_id.calendar_id != version.resource_calendar_id:
                employee.resource_id.calendar_id = version.resource_calendar_id
```

Only the **current** version's `resource_calendar_id` propagates to the `resource.resource` record.

---

## 15. Migration Impact Summary

| Previous (Odoo ≤18) | Odoo 19 CE |
|---|---|
| `hr.contract` model | ABSENT — replaced by `hr.version` |
| `hr.contract.wage` | `hr.version.wage` (line 178) |
| `hr.contract.date_start` | `hr.version.contract_date_start` (line 156) |
| `hr.contract.date_end` | `hr.version.contract_date_end` (line 157) |
| `hr.contract.state` | ABSENT — no state machine on versions |
| `hr.contract.job_id` | `hr.version.job_id` (line 130) |
| `hr.contract.department_id` | `hr.version.department_id` (line 127) |
| `hr.employee.contract_id` | ABSENT — replaced by `version_id` / `version_ids` |
| `hr.employee.department_id` (direct) | Delegated from `hr.version.department_id` via `_inherits` |
| `hr.employee.job_id` (direct) | Delegated from `hr.version.job_id` via `_inherits` |
| `hr.contract.struct_id` | `hr.version.structure_type_id` |
| Contract templates (if any) | `hr.version` records where `employee_id = False` |
