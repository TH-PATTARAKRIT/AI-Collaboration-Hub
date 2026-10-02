# U220 — res.company: Multi-Company Fields, Currency, Partner, Account Setup
## STATE03 VDR Deep Research — Restricted Technical Evidence

**Unit**: U220  
**Addon scope**: `base` (models/res_company.py), `account` (models/company.py), `stock_account` (models/res_company.py), `l10n_th` (models/template_th.py)  
**Source tree**: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons`  
**Gate**: GREEN  
**Claims**: 22  

---

## 1. Base Model — res_company.py

**File**: `base/models/res_company.py`

### 1.1 Class Declaration
```
Line 31: class ResCompany(models.Model):
Line 32:     _name = 'res.company'
Line 33:     _description = 'Companies'
Line 34:     _order = 'sequence, name'
Line 35:     _inherit = ['format.address.mixin', 'format.vat.label.mixin']
Line 36:     _parent_store = True
```
- `_parent_store = True` enables the `parent_path` field and hierarchical `child_of` domain operator.

### 1.2 Core Fields

| Field | Type | Line | Notes |
|---|---|---|---|
| `name` | Char (related) | 48 | `related='partner_id.name'`, `required=True`, `store=True`, `readonly=False` — name is delegated to the linked partner |
| `active` | Boolean | 49 | default True |
| `sequence` | Integer | 50 | default=10, used for company switcher ordering |
| `parent_id` | Many2one → res.company | 51 | `index=True`, `ondelete='restrict'` — prevents deletion of parent company with active children |
| `child_ids` | One2many → res.company | 52 | inverse of parent_id, string='Branches' |
| `all_child_ids` | One2many → res.company | 53 | includes archived branches via `context={'active_test': False}` |
| `parent_path` | Char | 54 | indexed, used by `_parent_store` for hierarchical queries |
| `parent_ids` | Many2many (compute) | 55 | `compute='_compute_parent_ids'`, `compute_sudo=True` |
| `root_id` | Many2one (compute) | 56 | root company in hierarchy, also from `_compute_parent_ids` |
| `partner_id` | Many2one → res.partner | 57 | `required=True`, `index=True` — the linked partner record; all address/name/vat fields delegate to this partner |
| `currency_id` | Many2one → res.currency | 67 | `required=True`, `default=lambda self: self._default_currency_id()` |
| `user_ids` | Many2many → res.users | 68 | via `res_company_users_rel` table, columns `cid`/`user_id` — the set of users who belong to this company |

### 1.3 Currency Default and Fallback

**Line 45–46**:
```python
def _default_currency_id(self):
    return self.env.user.company_id.currency_id
```
- When a new company is created, the currency defaults to the **current user's company currency**. There is NO `_compute_currency_id()` method in base. The `_onchange_country_id` method sets `currency_id = country_id.currency_id` when a country is selected, but this is an onchange (UI only, not stored compute).

**Line 194–197** (`_onchange_country_id`):
```python
@api.onchange('country_id')
def _onchange_country_id(self):
    if self.country_id:
        self.currency_id = self.country_id.currency_id
```
- This is a UI-only onchange; it does NOT enforce currency when country is set programmatically.

### 1.4 Root-Delegated Field Mechanism

**Line 111–119** (`_get_company_root_delegated_field_names`):
```python
def _get_company_root_delegated_field_names(self):
    return ['currency_id']
```
- In `base`, only `currency_id` is root-delegated.
- `_get_view()` (line 256–262) marks these fields as `readonly="parent_id != False"` in the form view.
- On `create()` (line 317–320): if a `parent_id` is set, the delegated fields are copied from the root.
- On `write()` (line 385–397): if the root company modifies a delegated field, that change propagates to ALL branches via `sudo().search([('id', 'child_of', company.id), ('id', '!=', company.id)])`.

**Line 426–433** (`_check_root_delegated_fields` constraint):
```python
@api.constrains(lambda self: self._get_company_root_delegated_field_names() + ['parent_id'])
def _check_root_delegated_fields(self):
    for company in self:
        if company.parent_id:
            for fname in company._get_company_root_delegated_field_names():
                if company[fname] != company.parent_id[fname]:
                    ...
                    raise ValidationError(...)
```
- Enforces at DB level that branch company currency must equal root company currency.

### 1.5 Parent Hierarchy Compute

**Line 130–134** (`_compute_parent_ids`):
```python
@api.depends('parent_path')
def _compute_parent_ids(self):
    for company in self.with_context(active_test=False):
        company.parent_ids = self.browse(int(id) for id in company.parent_path.split('/') if id) if company.parent_path else company
        company.root_id = company.parent_ids[0]
```
- `root_id` is the first element of the `parent_ids` list (the topmost company with no parent).

### 1.6 Hierarchy Change Blocked

**Line 356–358** (`write`):
```python
def write(self, vals):
    if 'parent_id' in vals:
        raise UserError(self.env._("The company hierarchy cannot be changed."))
```
- **Migration flag**: `parent_id` is write-protected after creation. Branch/root relationship is immutable.

### 1.7 paperformat_id — Stays on base in v19

**Line 87**:
```python
paperformat_id = fields.Many2one('report.paperformat', 'Paper format', default=lambda self: self.env.ref('base.paperformat_euro', raise_if_not_found=False))
```
- `paperformat_id` remains on `base/models/res_company.py` in v19. It was NOT moved.

### 1.8 report_header and report_footer in v19

**Line 58–59**:
```python
report_header = fields.Html(string='Company Tagline', ...)
report_footer = fields.Html(string='Report Footer', ...)
```
- Both remain on the base model. `report_footer` is NOT removed in v19.

### 1.9 Archive Behavior

**Line 382–383** (`write`):
```python
if vals.get('active') is False:
    self.child_ids.active = False
```
- Archiving a company cascades to all direct children (branches).

**Line 409–424** (`_check_active` constraint):
- Cannot archive a company that still has active users with it as their `company_id`.

### 1.10 res.users.company_ids

**File**: `base/models/res_users.py`

**Line 247–248**:
```python
company_ids = fields.Many2many('res.company', 'res_company_users_rel', 'user_id', 'cid',
    string='Companies', default=lambda self: self.env.company.ids)
```
- Same join table as `res.company.user_ids` but with inverted columns.
- Line 501–509 (`_constrains company_id, company_ids`): enforces that `company_id` (the user's active company) is always a member of `company_ids`.

---

## 2. Account Extension — account/models/company.py

**File**: `account/models/company.py`

### 2.1 Fiscal Year Fields

**Line 74–75**:
```python
fiscalyear_last_day = fields.Integer(default=31, required=True)
fiscalyear_last_month = fields.Selection(MONTH_SELECTION, default='12', required=True)
```
- Default: fiscal year ends December 31 (calendar year).

### 2.2 Lock Date Fields

**Lines 76–102**:
| Field | Type | Tracking | Notes |
|---|---|---|---|
| `fiscalyear_lock_date` | Date | Yes | Global/Fiscal Lock Date — any entry on or before is locked |
| `tax_lock_date` | Date | Yes | Tax Return Lock Date — set automatically on tax closing entry |
| `sale_lock_date` | Date | Yes | Sales Lock Date |
| `purchase_lock_date` | Date | Yes | Purchase Lock Date |
| `hard_lock_date` | Date | Yes | Irreversible — cannot be removed or decreased (line 574–576) |

**SOFT_LOCK_DATE_FIELDS** (line 57–62): `['fiscalyear_lock_date', 'tax_lock_date', 'sale_lock_date', 'purchase_lock_date']`  
**LOCK_DATE_FIELDS** (line 64–67): all of the above plus `hard_lock_date`.

### 2.3 User Lock Dates (Exception-Aware)

**Lines 108–112** — computed fields:
```python
user_fiscalyear_lock_date = fields.Date(compute='_compute_user_fiscalyear_lock_date')
user_tax_lock_date = fields.Date(compute='_compute_user_tax_lock_date')
user_sale_lock_date = fields.Date(compute='_compute_user_sale_lock_date')
user_purchase_lock_date = fields.Date(compute='_compute_user_purchase_lock_date')
user_hard_lock_date = fields.Date(compute='_compute_user_hard_lock_date')
```
- These are context-dependent (`@api.depends_context('uid', 'ignore_exceptions')`).
- `_get_user_lock_date()` (line 607–640): walks `parent_ids`, checks for `account.lock_exception` records, and may relax the lock date for a specific user.
- **`user_hard_lock_date`** (line 443–448): takes the maximum hard_lock_date across all parent companies.

### 2.4 hard_lock_date Enforcement

**Line 569–576** (`_validate_locks`):
```python
if 'hard_lock_date' in new_locks:
    for company in self:
        if not company.hard_lock_date:
            continue
        if not hard_lock_date:
            raise UserError(_("The Hard Lock Date cannot be removed."))
        if hard_lock_date < company.hard_lock_date:
            raise UserError(_("A new Hard Lock Date must be posterior (or equal) to the previous one."))
```

### 2.5 chart_template Field

**Line 117**:
```python
chart_template = fields.Selection(selection='_chart_template_selection')
```
- Selection list is dynamically computed from `account.chart.template._select_chart_template(company.country_id)` (line 998–999).
- On company `create()` (line 487–499): if the root company has a `chart_template`, it auto-loads that template for the new branch company.

### 2.6 account_opening_date

**Line 169**:
```python
account_opening_date = fields.Date(string='Opening Entry', help="That is the date of the opening entry.")
```
- Used to determine fiscal year in `_check_fiscalyear_last_day` (line 330–345).

### 2.7 account_fiscal_country_id

**Lines 203–209**:
```python
account_fiscal_country_id = fields.Many2one(
    string="Fiscal Country",
    comodel_name='res.country',
    compute='compute_account_tax_fiscal_country',
    store=True,
    readonly=False,
    ...)
```
**Line 386–391** (`compute_account_tax_fiscal_country`):
```python
@api.depends('country_id')
def compute_account_tax_fiscal_country(self):
    for record in self:
        if not record.account_fiscal_country_id:
            record.account_fiscal_country_id = record.country_id
```
- Note: this only sets if NOT already set (stored, user-editable). This means a company can have a different fiscal country than its physical country.

### 2.8 account_default_pos_receivable_account_id

**Line 179**:
```python
account_default_pos_receivable_account_id = fields.Many2one('account.account', string="Default PoS Receivable Account", check_company=True)
```
- Used by Point of Sale module to set the default receivable account for POS transactions.

### 2.9 Root-Delegated Fields Extended by Account

**Lines 311–317**:
```python
def _get_company_root_delegated_field_names(self):
    return super()._get_company_root_delegated_field_names() + [
        'fiscalyear_last_day',
        'fiscalyear_last_month',
        'account_storno',
        'tax_exigibility',
    ]
```
- In addition to `currency_id`, account module delegates `fiscalyear_last_day`, `fiscalyear_last_month`, `account_storno`, and `tax_exigibility` to the root company.

### 2.10 Currency Change Guard in Account

**Lines 757–759** (`write`):
```python
if 'currency_id' in vals and vals['currency_id'] != company.currency_id.id:
    if company.root_id._existing_accounting():
        raise UserError(_('You cannot change the currency of the company since some journal items already exist'))
```
- Blocks currency change once any accounting entries exist at the root level.

### 2.11 Storno Accounting

**Lines 233–234** and **Lines 451–458**:
- `account_storno` is computed from `account_fiscal_country_id.code in STORNO_MANDATORY_COUNTRIES`.
- STORNO_MANDATORY_COUNTRIES (line 52): BA, CN, CZ, HR, PL, RO, RS, RU, SI, SK, UA.
- TH (Thailand) is NOT in storno countries — storno is off by default for Thai companies.

### 2.12 Deprecated Method

**Lines 1150–1157**:
```python
# Deprecated, removed in master.
def _check_tax_return_configuration(self):
    ...
    return
```
- `_check_tax_return_configuration` is marked as deprecated and is a no-op stub. Migration note: do not rely on this method.

---

## 3. Stock Account Extension — stock_account/models/res_company.py

**File**: `stock_account/models/res_company.py`

### 3.1 Stock Account Fields on Company

**Lines 12–17**:
```python
account_stock_journal_id = fields.Many2one('account.journal', string='Stock Journal', check_company=True)
account_stock_valuation_id = fields.Many2one('account.account', string='Stock Valuation Account', check_company=True)
account_production_wip_account_id = fields.Many2one('account.account', string='Production WIP Account', check_company=True)
account_production_wip_overhead_account_id = fields.Many2one('account.account', string='Production WIP Overhead Account', check_company=True)
```

**MIGRATION FLAG**: In v19:
- `account_stock_expense_id` and `account_stock_income_id` are **NOT fields on res.company**.
- `account_stock_expense_id` is a field on **`account.account`** (`stock_account/models/account_account.py`, line 10).
- There is NO `account_stock_income_id` in v19 at all — this name does not exist in the community codebase.

### 3.2 Inventory Valuation Fields on Company

**Lines 19–47**:
```python
inventory_period = fields.Selection([('manual','Manual'),('daily','Daily'),('monthly','Monthly')], ...)
inventory_valuation = fields.Selection([('periodic','Periodic (at closing)'),('real_time','Perpetual (at invoicing)')], ...)
cost_method = fields.Selection([('standard','Standard Price'),('fifo','First In First Out (FIFO)'),('average','Average Cost (AVCO)')], ...)
```
- These are company-level defaults; the actual per-product-category settings are propagated via `_set_category_defaults()` (line 371–377).

---

## 4. Thai Localization — l10n_th/models/template_th.py

**File**: `l10n_th/models/template_th.py`

### 4.1 Thai Chart Template Company Defaults

**Lines 19–43** (`_get_th_res_company`):
When the Thai chart of accounts is loaded, the following company fields are set:
| Company Field | Template Value |
|---|---|
| `account_fiscal_country_id` | `base.th` (Thailand) |
| `bank_account_code_prefix` | `'11120'` |
| `cash_account_code_prefix` | `'11110'` |
| `account_default_pos_receivable_account_id` | `l10n_th_account_112101` |
| `income_currency_exchange_account_id` | `l10n_th_account_421300` |
| `expense_currency_exchange_account_id` | `l10n_th_account_621200` |
| `account_sale_tax_id` | `tax_output_vat` |
| `account_purchase_tax_id` | `tax_input_vat` |
| `account_stock_valuation_id` | `l10n_th_account_113100` |
| `tax_exigibility` | `'True'` (cash basis enabled) |

**Implication**: Thai companies automatically enable cash basis accounting (`tax_exigibility = True`).

### 4.2 Thai Branch Name (VAT/company_registry)

**File**: `l10n_th/models/res_partner.py`, lines 9–18:
- `l10n_th_branch_name` is computed on `res.partner` (not `res.company` directly).
- For a Thai company partner, if `company_registry` is set → "Branch {code}", else → "Headquarter".
- This is accessed via `res.company.partner_id.company_registry` and `res.company.vat` (both delegated to partner).

### 4.3 VAT Placeholder for Thailand

**File**: `base_vat/models/res_partner.py`, line 80:
```python
'th': '1234545678781'
```
- When `account_fiscal_country_id` or `country_id` is Thailand, the VAT field shows `1234545678781` as placeholder (via `_compute_company_vat_placeholder` in account/models/company.py line 1125–1134).

---

## 5. Migration Flags Summary

| Flag ID | Area | Description |
|---|---|---|
| MF-220-01 | Stock accounts | `account_stock_expense_id` and `account_stock_income_id` are NOT on `res.company` in v19. `account_stock_expense_id` is on `account.account`; `account_stock_income_id` does not exist. |
| MF-220-02 | Hierarchy | `parent_id` cannot be changed after creation (`write()` raises UserError). Migration must set hierarchy correctly at create time. |
| MF-220-03 | Currency lock | Currency change is blocked once any journal items exist (account module write override). |
| MF-220-04 | Hard lock | `hard_lock_date` is new in v19 (not in v16/v17). Irreversible once set — migration must not populate this field unless intentional. |
| MF-220-05 | Storno | `account_storno` is auto-computed from fiscal country; Thailand is not a storno country. |
| MF-220-06 | paperformat_id | Remains on `base/models/res_company.py` line 87 — NOT moved in v19. |
| MF-220-07 | report_footer | Remains on `base/models/res_company.py` line 59 as Html field — NOT removed. |
| MF-220-08 | lock exceptions | New `account.lock_exception` model in v19 allows per-user lock overrides. `user_*_lock_date` computed fields respect these exceptions. |
| MF-220-09 | Thai template | Thai l10n enables `tax_exigibility = True` (cash basis) automatically on chart template load. |
| MF-220-10 | Deprecated | `_check_tax_return_configuration` is deprecated (no-op stub) — do not call from migration code. |
