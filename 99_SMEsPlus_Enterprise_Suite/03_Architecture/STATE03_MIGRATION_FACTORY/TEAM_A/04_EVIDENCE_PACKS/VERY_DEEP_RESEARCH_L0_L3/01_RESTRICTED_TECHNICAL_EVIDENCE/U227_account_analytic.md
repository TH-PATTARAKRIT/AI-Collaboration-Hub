# U227 — account.analytic.account: Plan Hierarchy, Distribution Mixin, Mandatory Validation
**Research Unit**: U227  
**Module**: analytic (Odoo 19.0.post20260921 Community)  
**Scope**: account.analytic.account, account.analytic.plan, analytic.mixin, account.analytic.line, account.move.line (analytic bridge)  
**Source root**: `odoo/addons/analytic/models/`  
**Gate**: GREEN  
**Claim count**: 25  

---

## 1. account.analytic.account — Model Definition

**File**: `analytic/models/analytic_account.py`

```
Class AccountAnalyticAccount(models.Model)
  _name = 'account.analytic.account'         line 12
  _inherit = ['mail.thread']                  line 13
  _order = 'plan_id, name asc'               line 15
  _check_company_auto = True                  line 16
  _check_company_domain = models.check_company_domain_parent_of  line 17
  _rec_names_search = ['name', 'code']        line 18
```

### Core Fields

| Field | Type | Attributes | Line |
|-------|------|------------|------|
| `name` | Char | required, index='trigram', tracking=True, translate=True | 20 |
| `code` | Char | string='Reference', index='btree', tracking=True | 27 |
| `active` | Boolean | default=True, tracking=True | 32 |
| `plan_id` | Many2one → account.analytic.plan | required, index=True | 38 |
| `root_plan_id` | Many2one → account.analytic.plan | computed: `plan_id.root_id`, store=True | 44 |
| `color` | Integer | related: `plan_id.color` | 50 |
| `company_id` | Many2one → res.company | default: env.company | 61 |
| `partner_id` | Many2one → res.partner | check_company=True, bypass_search_access=True | 67 |
| `line_ids` | One2many → account.analytic.line | inverse_name='auto_account_id' | 55 |

**Critical**: `account.analytic.account` has **NO** `parent_id` field — it is a FLAT structure. Hierarchy lives entirely on `account.analytic.plan`, not on the account itself.

### Constraints

`_check_company_consistency()` at line 96: raises `UserError` if company changed while analytic lines for a different company exist.

### write() override

`write()` at line 237 detects `plan_id` change and calls `_update_accounts_in_analytic_lines()` to migrate analytic line column values from old plan column to new plan column before saving.

---

## 2. account.analytic.plan — Hierarchy Model

**File**: `analytic/models/analytic_plan.py`

```
Class AccountAnalyticPlan(models.Model)
  _name = 'account.analytic.plan'    line 14
  _parent_store = True               line 16  ← Odoo adjacency + path hierarchy
  _rec_name = 'complete_name'        line 17
  _order = 'sequence asc, id'        line 18
```

### Key Fields

| Field | Type | Notes | Line |
|-------|------|-------|------|
| `name` | Char | required, translate=True; inverse=`_inverse_name` triggers column sync | 23 |
| `parent_id` | Many2one → self | ondelete='cascade'; domain excludes child_of self | 29 |
| `parent_path` | Char | index='btree'; Odoo _parent_store path | 37 |
| `root_id` | Many2one → self | computed from parent_path | 38 |
| `children_ids` | One2many → self | string="Childrens" | 43 |
| `complete_name` | Char | computed recursively: `parent.complete_name / name`, store=True | 52 |
| `default_applicability` | Selection | optional/mandatory/unavailable; **company_dependent=True** | 77 |
| `applicability_ids` | One2many → account.analytic.applicability | domain by company | 87 |

### _column_name() — Dynamic DB Column Resolution

```python
def _strict_column_name(self):  # line 115
    project_plan, _other_plans = self._get_all_plans()
    return 'account_id' if self == project_plan else f"x_plan{self.id}_id"

def _column_name(self):  # line 120
    return self.root_id._strict_column_name()
```

The **project plan** gets the column name `account_id` on `account.analytic.line`.  
All other root plans get dynamically-named columns `x_plan{id}_id`.  
Sub-plans share their root's column name — they do not get separate columns.

### _sync_plan_column() — Dynamic Field Creation

At line 319: creates/deletes `ir.model.fields` entries for each plan column on all models inheriting `analytic.plan.fields.mixin`. Root plans get a stored Many2one field; sub-plans get a non-stored computed related field for groupby hierarchy.

### get_relevant_plans() — Plan Availability

At line 213: returns filtered plan list based on `_get_applicability(**kwargs)` scoring:
- Plans with `all_account_count == 0` are excluded.
- Plans returning `'unavailable'` from `_get_applicability()` are excluded.
- Forced re-inclusion for plans whose accounts are already in an existing distribution.

### _get_applicability() — Scoring Algorithm

At line 246:
- Baseline score: 0.5 (low-priority, company-only match).
- Each `applicability_ids` rule scores: `0.5` (company match) + `1.0` (business_domain match) or `-1` (domain mismatch).
- First rule exceeding current score wins.
- Returns `default_applicability` if no rule beats baseline.

### AccountAnalyticApplicability — Per-Domain Applicability

Model at line 408, fields:
- `analytic_plan_id` Many2one to plan
- `business_domain` Selection (base: 'general')
- `applicability` Selection (optional/mandatory/unavailable)
- `company_id` Many2one

`_get_score()` at line 449: scores 0.5 for company match + 1.0 for business_domain match.

---

## 3. analytic.mixin — JSON Distribution Mixin

**File**: `analytic/models/analytic_mixin.py`

```
Class AnalyticMixin(models.AbstractModel)
  _name = 'analytic.mixin'    line 12
```

### Fields

| Field | Type | Notes | Line |
|-------|------|-------|------|
| `analytic_distribution` | Json | compute=`_compute_analytic_distribution`, store=True, copy=True, readonly=False | 16 |
| `analytic_precision` | Integer | store=False; default from `decimal.precision` "Percentage Analytic" | 22 |
| `distribution_analytic_account_ids` | Many2many | computed; search enabled | 26 |

### analytic_distribution Format

Keys are **string representations of account IDs**, potentially comma-separated for multi-plan lines:
- Single account: `{"42": 100}` — account 42 gets 100%
- Split: `{"42": 60, "57": 40}` — two accounts 60%+40%
- Cross-plan combined: `{"12,34": 100}` — accounts 12 AND 34 together (one from each plan) get 100%

The comma-separated key format allows a single distribution entry to set accounts across multiple plans simultaneously.

### _validate_distribution() — Mandatory Check

```python
def _validate_distribution(self, **kwargs):  # line 182
    if self.env.context.get('validate_analytic', False):
        mandatory_plans_ids = [plan['id'] for plan in
            self.env['account.analytic.plan'].sudo().with_company(self.company_id)
            .get_relevant_plans(**kwargs) if plan['applicability'] == 'mandatory']
        if not mandatory_plans_ids:
            return
        decimal_precision = self.env['decimal.precision'].precision_get('Percentage Analytic')
        distribution_by_root_plan = {}
        for analytic_account_ids, percentage in (self.analytic_distribution or {}).items():
            for analytic_account in self.env['account.analytic.account']
                    .browse(map(int, analytic_account_ids.split(","))).exists():
                root_plan = analytic_account.root_plan_id
                distribution_by_root_plan[root_plan.id] += percentage
        for plan_id in mandatory_plans_ids:
            if float_compare(distribution_by_root_plan.get(plan_id, 0), 100,
                             precision_digits=decimal_precision) != 0:
                raise ValidationError(_("One or more lines require a 100% analytic distribution."))
```

**Key**: only fires when `validate_analytic=True` is in context. Validation checks each mandatory plan's sum equals exactly 100% (using `float_compare` with precision from `decimal.precision`).

### _sanitize_values() — Float Normalization

At line 198: rounds each distribution percentage to `decimal_precision` digits. Also preserves `__update__` key untouched.

### create() / write() Override

Both at lines 175/169 call `_sanitize_values()` to normalize all distribution percentages on save.

### GIN Index

`init()` at line 32 creates a GIN index on `analytic_distribution` JSON keys for fast search: `regexp_split_to_array(jsonb_path_query_array(...), '\D+')`.

### _merge_distribution() — Partial Plan Update

At line 244: handles `__update__` sentinel key. When present, merges new distribution values (for changing plans) with preserved existing values (for non-changing plans), normalizing to maintain 100% total.

---

## 4. analytic.plan.fields.mixin — Dynamic Plan Columns on Analytic Lines

**File**: `analytic/models/analytic_line.py`

```
Class AnalyticPlanFieldsMixin(models.AbstractModel)
  _name = 'analytic.plan.fields.mixin'    line 12
```

### Static Fields

| Field | Type | Notes | Line |
|-------|------|-------|------|
| `account_id` | Many2one → account.analytic.account | 'Project Account'; ondelete='restrict' | 16 |
| `auto_account_id` | Many2one → account.analytic.account | computed context-dependent magic field | 26 |

### _get_plan_domain()

```python
def _get_plan_domain(self, plan):  # line 87
    return [('plan_id', 'child_of', plan.id)]
```

This domain restricts the available accounts in a plan column to those belonging to the plan's subtree (including all children). Used in `fields_get()` and `_patch_view()` to set domain on field nodes.

### _check_account_id Constraint

At line 93: `@api.constrains(lambda self: self._get_plan_fnames())` — raises `ValidationError` if no plan column has a value. This means **at least one analytic account must be set on each analytic line**.

---

## 5. account.analytic.line — Analytic Line Model

**File**: `analytic/models/analytic_line.py` (line 163)

```
Class AccountAnalyticLine(models.Model)
  _name = 'account.analytic.line'
  _inherit = ['analytic.plan.fields.mixin']   ← gets dynamic plan columns
  _order = 'date desc, id desc'
  _check_company_auto = True
```

### Fields

| Field | Type | Notes | Line |
|-------|------|-------|------|
| `name` | Char | required | 170 |
| `date` | Date | required, index=True | 174 |
| `amount` | Monetary | required, default=0.0 | 180 |
| `unit_amount` | Float | Quantity | 185 |
| `company_id` | Many2one → res.company | required, readonly | 204 |
| `category` | Selection | other/invoice/vendor_bill | 218 |
| `analytic_distribution` | Json | computed (not stored on line itself) + inverse | 227 |

`analytic_distribution` on `account.analytic.line` is a **computed** display field — not stored separately. `_compute_analytic_distribution()` at line 237 returns `{self._get_distribution_key(): 100}`.

The `account_id` field (from `analytic.plan.fields.mixin`) holds the project plan's analytic account. Other plans get dynamic `x_plan{id}_id` columns.

---

## 6. account.move.line — Analytic Bridge

**File**: `account/models/account_move_line.py`

### analytic_distribution on move line

```python
analytic_distribution = fields.Json(     # line 438
    inverse="_inverse_analytic_distribution",
)
analytic_line_ids = fields.One2many(     # line 434
    comodel_name='account.analytic.line', inverse_name='move_line_id',
    string='Analytic lines',
)
```

The field is **originally defined in `analytic.mixin`** (inherited); `account.move.line` adds the `inverse` method.

### _validate_analytic_distribution()

```python
def _validate_analytic_distribution(self):  # line 3188
```

Called at journal entry posting. Iterates product-type lines, calls `_validate_distribution()` with `validate_analytic=True` (implicit via context), business_domain = `invoice/bill/general`. Raises `ValidationError` (single move) or `RedirectWarning` (batch).

### _create_analytic_lines()

```python
def _create_analytic_lines(self):  # line 3221
    self._validate_analytic_distribution()
    analytic_line_vals = []
    for line in self:
        analytic_line_vals.extend(line._prepare_analytic_lines())
    self.env['account.analytic.line'].with_context(context).create(analytic_line_vals)
```

Called at journal entry posting. First validates, then creates all analytic lines.

### _prepare_analytic_lines()

```python
def _prepare_analytic_lines(self):  # line 3234
    analytic_line_vals = []
    if self.analytic_distribution:
        distribution_on_each_plan = {}
        for account_ids, distribution in self.analytic_distribution.items():
            line_values = self._prepare_analytic_distribution_line(
                float(distribution), account_ids, distribution_on_each_plan)
            if not self.company_currency_id.is_zero(line_values.get('amount')):
                analytic_line_vals.append(line_values)
        self._round_analytic_distribution_line(analytic_line_vals)
    return analytic_line_vals
```

Iterates each `{"account_ids": percentage}` entry, creates one `account.analytic.line` per entry. Zero-amount lines are excluded. Rounding correction applied after to ensure amounts sum correctly.

### _prepare_analytic_distribution_line()

```python
def _prepare_analytic_distribution_line(self, distribution, account_ids,  # line 3249
                                         distribution_on_each_plan):
```

- Resolves comma-separated `account_ids` string to `account.analytic.account` records.
- For the last distribution entry in a plan (sum reaches 100%), uses exact remainder to avoid floating-point drift.
- Sets `account_field_values[account.plan_id._column_name()] = account.id` for each account.
- Returns dict with `name`, `date`, plan-column fields, `partner_id`, `unit_amount`, `product_id`, `amount`, `general_account_id`, `move_line_id`, `category`.

---

## 7. account.analytic.distribution.model — Auto-Apply Models

**File**: `analytic/models/analytic_distribution_model.py`

```
Class AccountAnalyticDistributionModel(models.Model)
  _name = 'account.analytic.distribution.model'
  _inherit = ['analytic.mixin']    ← stores analytic_distribution JSON
```

`_get_distribution()` at line 61: returns merged distribution from all matching models by partner/partner_category/company. Used to auto-prefill `analytic_distribution` on new invoices, PO/SO lines.

---

## 8. Migration Flags — CRITICAL for STATE03

### analytic_account_id (Many2one) — REMOVED in v16

In Odoo v15 and earlier, `account.move.line` had:
```python
analytic_account_id = fields.Many2one('account.analytic.account', ...)
```
This field is **completely absent** from v16+ / v19. The entire single-account paradigm was replaced by the JSON `analytic_distribution` field.

**Migration action required**: Any v15 data or customization referencing `analytic_account_id` on `account.move.line`, `sale.order.line`, `purchase.order.line`, or `hr.expense` must be migrated to `analytic_distribution` JSON format.

### analytic_tag_ids (Many2many) — REMOVED in v16

`analytic_tag_ids` was a Many2many to `account.analytic.tag` on move lines in v15. The `account.analytic.tag` model is entirely removed in v16+. Tags were used for distribution. This functionality has been subsumed into the JSON distribution model.

**Migration action required**: Remove all references to `analytic_tag_ids` and `account.analytic.tag`.

### account.analytic.account.parent_id — NEVER EXISTED (plan hierarchy is different)

In v15, `account.analytic.account` had a `parent_id` for hierarchical chart-of-accounts-style organisation. In v16+, this was **removed**. The hierarchy now lives on `account.analytic.plan` (via `parent_id` + `_parent_store`).

### New Distribution Format

| v15 | v19 |
|-----|-----|
| `analytic_account_id` Many2one (single) | `analytic_distribution` JSON dict |
| `analytic_tag_ids` Many2many + tag distributions | Merged into `analytic_distribution` |
| Single analytic account per line | Multiple accounts across multiple plans |
| Percentage on `account.analytic.tag.analytic_distribution` | Percentage directly in JSON keys |

---

## Source Paths Reference

| File | Canonical path |
|------|---------------|
| Account model | `analytic/models/analytic_account.py` |
| Plan model | `analytic/models/analytic_plan.py` |
| Mixin | `analytic/models/analytic_mixin.py` |
| Analytic line | `analytic/models/analytic_line.py` |
| Distribution model | `analytic/models/analytic_distribution_model.py` |
| Move line bridge | `account/models/account_move_line.py` |
