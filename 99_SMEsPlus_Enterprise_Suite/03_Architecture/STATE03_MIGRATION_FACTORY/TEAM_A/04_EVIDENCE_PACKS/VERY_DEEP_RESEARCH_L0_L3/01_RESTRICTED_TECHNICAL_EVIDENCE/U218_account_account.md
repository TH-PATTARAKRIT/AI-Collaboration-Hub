# U218 — account.account: Chart of Accounts Model Deep Evidence

**Research Unit:** U218  
**Module:** account (models/account_account.py)  
**Source SHA256:** 75ad6073152c2419558703e5760eb2b93db33ab3cb758dfee258418acc921c11  
**Source Path:** odoo/addons/account/models/account_account.py  
**Line Count:** 1658  
**Gate:** GREEN  

---

## 1. Model Declaration

**File:** `odoo/addons/account/models/account_account.py`  
**Lines:** 19–25

```python
class AccountAccount(models.Model):
    _name = 'account.account'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Account"
    _order = "code, placeholder_code"
    _check_company_auto = True
    _check_company_domain = models.check_companies_domain_parent_of
```

Key notes:
- Inherits chatter (`mail.thread`) and activity tracking (`mail.activity.mixin`).
- `_check_company_auto = True` enables automatic company domain checks on relational fields.
- `_check_company_domain = models.check_companies_domain_parent_of` — the company check uses parent-of semantics (shared COA across company hierarchy).
- Default order is by `code, placeholder_code` (company-dependent code first, then fallback display code).

---

## 2. Field Inventory

### 2.1 Core Identity Fields

| Field | Line | Type | Key Attributes |
|---|---|---|---|
| `name` | 33 | `Char` | required, index='trigram', tracking=True, translate=True |
| `description` | 34 | `Text` | translate=True |
| `code` | 39 | `Char` | size=64, tracking=True, compute='_compute_code', search='_search_code', inverse='_inverse_code' |
| `code_store` | 40 | `Char` | company_dependent=True (JSONB per company in DB) |
| `placeholder_code` | 41 | `Char` | compute='_compute_placeholder_code', search='_search_placeholder_code' |
| `active` | 42 | `Boolean` | default=True, tracking=True (replaces old `deprecated` field) |

### 2.2 account_type Selection Field

**Lines:** 44–70

```python
account_type = fields.Selection(
    selection=[
        ("asset_receivable",    "Receivable"),
        ("asset_cash",          "Bank and Cash"),
        ("asset_current",       "Current Assets"),
        ("asset_non_current",   "Non-current Assets"),
        ("asset_prepayments",   "Prepayments"),
        ("asset_fixed",         "Fixed Assets"),
        ("liability_payable",   "Payable"),
        ("liability_credit_card","Credit Card"),
        ("liability_current",   "Current Liabilities"),
        ("liability_non_current","Non-current Liabilities"),
        ("equity",              "Equity"),
        ("equity_unaffected",   "Current Year Earnings"),
        ("income",              "Income"),
        ("income_other",        "Other Income"),
        ("expense",             "Expenses"),
        ("expense_other",       "Other Expenses"),
        ("expense_depreciation","Depreciation"),
        ("expense_direct_cost", "Cost of Revenue"),
        ("off_balance",         "Off-Balance Sheet"),
    ],
    string="Type", tracking=True,
    required=True,
    compute='_compute_account_type', store=True, readonly=False, precompute=True, index=True,
    ...
)
```

**19 account types total.** Pattern: `{group}_{subtype}` where group is `asset|liability|equity|income|expense|off`. The `internal_group` field is derived by splitting on `_` (line 650).

### 2.3 company_ids — Shared Chart of Accounts (M2M)

**Lines:** 97–99

```python
company_ids = fields.Many2many('res.company', string='Companies', required=True, readonly=False,
    depends_context=('uid',),
    default=lambda self: self.env.company)
```

- **M2M field** — one account record can be shared across multiple companies.
- `depends_context=('uid',)` prevents cache pollution between sudo/non-sudo calls.
- `default=lambda self: self.env.company` sets the creating company as initial owner.
- There is NO `company_id` Many2one field on this model in v19; `company_ids` M2M is the sole company relationship.
- Constraint at line 280: `asset_cash` accounts cannot be shared between companies.
- Constraint at line 272: accounts must belong to at least one company.

### 2.4 reconcile Field

**Lines:** 89–91

```python
reconcile = fields.Boolean(string='Allow Reconciliation', tracking=True,
    compute='_compute_reconcile', store=True, readonly=False, precompute=True,
    help="Check this box if this account allows invoices & payments matching of journal items.")
```

**Compute logic (_compute_reconcile, lines 665–674):**
```python
@api.depends('account_type')
def _compute_reconcile(self):
    for account in self:
        if account.internal_group in ('income', 'expense', 'equity'):
            account.reconcile = False
        elif account.account_type in ('asset_receivable', 'liability_payable'):
            account.reconcile = True
        elif account.account_type in ('asset_cash', 'liability_credit_card', 'off_balance'):
            account.reconcile = False
        # Other asset/liability: no change (user-controlled)
```

**Constraint (lines 27–31):** `asset_receivable` and `liability_payable` accounts MUST have `reconcile=True` (enforced by `_check_reconcile`).

**Constraint (lines 187–194):** `off_balance` accounts cannot be reconcilable and cannot have taxes.

**Toggle methods:**
- `_toggle_reconcile_to_true()` (lines 965–981): Direct SQL UPDATE on `account_move_line`; sets `reconciled=True` for zero-amount lines.
- `_toggle_reconcile_to_false()` (lines 983–1007): Blocks if partial reconciliations pending; resets `amount_residual` to 0.

### 2.5 tax_ids — Default Taxes

**Lines:** 92–95

```python
tax_ids = fields.Many2many('account.tax', 'account_account_tax_default_rel',
    'account_id', 'tax_id', string='Default Taxes',
    check_company=True,
    context={'append_fields': ['type_tax_use', 'company_id']})
```

- Junction table: `account_account_tax_default_rel`.
- `check_company=True` enforces company consistency.
- Context appends `type_tax_use` and `company_id` to fetched tax records.
- **Constraint:** `off_balance` accounts cannot have taxes (line 193).
- **Onchange (line 870–873):** When `account_type` changes to `off_balance`, `tax_ids` is cleared.
- **Write guard (line 1075):** Deprecating an account (setting `deprecated=True` via vals) blocked if account is used in a tax repartition line.

### 2.6 tag_ids

**Lines:** 104–112

```python
tag_ids = fields.Many2many(
    comodel_name='account.account.tag',
    relation='account_account_account_tag',
    compute='_compute_account_tags', readonly=False, store=True, precompute=True,
    string='Tags',
    help="Optional tags you may want to assign for custom reporting",
    ondelete='restrict',
    tracking=True,
)
```

- Compute via `_compute_account_tags` (line 609–612): inherits tags from the closest parent account by code prefix if none already set.

### 2.7 group_id

**Lines:** 113–114

```python
group_id = fields.Many2one('account.group', compute='_compute_account_group',
                           help="Account prefixes can determine account groups.")
```

**Compute logic (_compute_account_group, lines 418–448):** SQL query matching account code against `account_group.code_prefix_start` / `code_prefix_end` for the root company. Returns the longest-matching (most specific) group. Not stored; computed on demand.

### 2.8 currency_id

**Lines:** 35–36

```python
currency_id = fields.Many2one('res.currency', string='Account Currency', tracking=True,
    help="Forces all journal items in this account to have a specific currency ...")
```

- Optional. When set, all journal items on this account must use that currency.
- Constraint `_check_journal_consistency` (lines 196–267): validates currency matches any journal linking to this account.

### 2.9 opening_debit / opening_credit / opening_balance

**Lines:** 116–118

```python
opening_debit   = fields.Monetary(string="Opening Debit",   compute='_compute_opening_debit_credit', inverse='_set_opening_debit',   currency_field='company_currency_id')
opening_credit  = fields.Monetary(string="Opening Credit",  compute='_compute_opening_debit_credit', inverse='_set_opening_credit',  currency_field='company_currency_id')
opening_balance = fields.Monetary(string="Opening Balance", compute='_compute_opening_debit_credit', inverse='_set_opening_balance', currency_field='company_currency_id')
```

**Compute logic (_compute_opening_debit_credit, lines 576–603):** Reads from `account_move_line` filtered by `company.account_opening_move_id`. Returns debit, credit, balance per account. Inverse methods stage changes via `env.cr.precommit.data['import_account_opening_balance']` for batch update via `_load_precommit_update_opening_move()`.

---

## 3. code Field — Company-Dependent Architecture

The `code` field is NOT a simple stored `Char`. It is a computed field backed by `code_store` (company_dependent=True):

- **`code_store`** (line 40): JSONB column in DB, keyed by root company ID. Each company sees its own code.
- **`_compute_code`** (lines 337–340): reads `code_store` for the root company of `env.company`.
- **`_inverse_code`** (lines 345–354): writes `code_store` for the root company; invalidates and recomputes for all companies sharing the root.
- **`_search_code`** (lines 342–343): searches `code_store` via root company context.
- **`_ensure_code_is_unique`** (lines 1096–1146): enforces uniqueness across parent/child company hierarchy (same code cannot exist in parent or child company tree).

---

## 4. Deprecation in v19 — `active` replaces `deprecated`

In v19:
- Field `active = fields.Boolean(default=True, tracking=True)` at line 42 controls whether the account is visible/active.
- The old `deprecated` boolean field **does not exist** as a formal field definition in v19.
- Line 1075 contains `if vals.get('deprecated') and ...` — this is **legacy write-protection code** referencing the old field name. Since `deprecated` is no longer a field, this check is effectively dead code.
- Archiving (active=False) blocks the account from use in new entries without deleting it.
- **MIGRATION FLAG**: Projects migrating from v13/v14 must map `deprecated=True` → `active=False`.

---

## 5. name_search Override

**Lines:** 828–852 (`name_search` method; `_search_display_name` lines 854–868)

The `name_search` override:
1. If no `move_type` context: delegates to standard `super().name_search()`.
2. If `move_type` context present and `partner_id` context: pre-fetches most-frequent accounts for that partner (calls `_order_accounts_by_frequency_for_partner`).
3. If no name typed and suggestions exist: returns suggested accounts directly.
4. If name contains digits: searches across all types using `display_name ilike name`.
5. If name has no digits: also filters by `account_type` via `_get_name_search_account_types` (line 821–826).

**`_get_name_search_account_types`** (lines 821–826):
```python
move_type_accounts = {
    'out': ['income'],
    'in': ['expense', 'asset_fixed', 'expense_direct_cost'],
}
```
For customer invoices (`out_*`): shows only income accounts. For vendor bills (`in_*`): shows expense, fixed assets, and cost of revenue accounts.

**`_search_display_name`** (lines 854–868): searches by `code =like <term>%` OR `name ilike <term>` OR `description ilike <term>`.

---

## 6. internal_group Derived Field

**Lines:** 76–88, 649–663

`internal_group` is a Selection field derived from `account_type` by splitting on `_`:
- `asset_*` → `asset`
- `liability_*` → `liability`
- `equity*` → `equity`
- `income*` → `income`
- `expense*` → `expense`
- `off_balance` → `off`

Used by `_compute_include_initial_balance` (line 640): income/expense and `equity_unaffected` accounts do NOT carry their balance forward (reset at fiscal year end).

---

## 7. Account Group Model (AccountGroup)

**Lines:** 1514–1657

```python
class AccountGroup(models.Model):
    _name = 'account.group'
    _order = 'code_prefix_start'
```

Fields:
- `parent_id`: Many2one to self (hierarchical groups)
- `name`: display name
- `code_prefix_start`, `code_prefix_end`: define the range of account codes this group covers
- `company_id`: Many2one to `res.company` (root company, NOT shared M2M)

Groups are matched by SQL prefix comparison against account codes (see `_compute_account_group` lines 430–443). The most specific (longest prefix) match wins.

---

## 8. Migration Flags Summary

| Flag | Description |
|---|---|
| `user_type_id` REMOVED | In v16→v17: `user_type_id` (Many2one to `account.account.type`) was removed. Replaced by `account_type` selection directly on the account. No intermediate model. |
| `company_id` → `company_ids` | In v17: `company_id` Many2one replaced by `company_ids` Many2many for shared COA support. |
| `deprecated` → `active` | In v17+: `deprecated` boolean replaced by standard `active` field. `deprecated=True` → `active=False`. |
| `code` is company-dependent | `code_store` is JSONB (company_dependent=True). Migration must handle per-company codes. |
| `asset_cash` not shareable | Bank/Cash accounts cannot be in multiple companies' `company_ids`. |
| Opening balance via precommit | `opening_debit`/`opening_credit` use precommit batch pattern for bulk import. |

---

## 9. Key Constraints

| Method | Lines | Description |
|---|---|---|
| `_check_reconcile` | 27–31 | `asset_receivable`/`liability_payable` must have reconcile=True |
| `_constrains_reconcile` | 187–194 | `off_balance` cannot be reconcilable or have taxes |
| `_check_journal_consistency` | 196–267 | Currency on account must match any linked journal currency |
| `_check_company_consistency` | 269–288 | Must have ≥1 company; `asset_cash` cannot be multi-company |
| `_check_account_type_sales_purchase_journal` | 290–308 | Receivable/payable types cannot be used as default on sale/purchase journals |
| `_check_account_code` | 310–317 | Code must match `[A-Za-z0-9.]+` |
| `_ensure_code_is_unique` | 1096–1146 | Unique code across parent/child company hierarchy |
| `_unlink_except_contains_journal_items` | 1154–1157 | Cannot delete account with journal items |
