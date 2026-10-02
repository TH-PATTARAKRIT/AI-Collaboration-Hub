# U192 — product.category Accounting Property Accounts (L3 Technical Evidence)

**Unit:** U192 | **Group:** G01/G06 | **Priority:** P1 | **Status:** COMPLETE
**Source base:** Odoo Community 19.0.post20260921
**Research date:** 2026-10-02

---

## 1. ACCOUNT MODULE — ProductCategory Extension

**File:** `odoo/addons/account/models/product.py` (lines 14–30)

### Fields on `product.category` (_inherit)

| Field | Type | company_dependent | ondelete | Help |
|---|---|---|---|---|
| `property_account_income_categ_id` | Many2one → `account.account` | True | restrict | Used when validating a customer invoice |
| `property_account_expense_categ_id` | Many2one → `account.account` | True | restrict | Used at vendor bill validation (or COGS at customer invoice in Anglo-Saxon / perpetual mode) |

**Domain filter applied to both fields:**
```python
ACCOUNT_DOMAIN = "[('account_type', 'not in', ('asset_receivable','liability_payable','asset_cash','liability_credit_card','off_balance'))]"
```
This excludes receivable, payable, cash, credit card, and off-balance account types.

**Both fields carry `tracking=True`** — changes are recorded in the chatter.

---

## 2. ACCOUNT MODULE — ProductTemplate Extension

**File:** `odoo/addons/account/models/product.py` (lines 37–92)

### Product-level override fields (on `product.template`)

| Field | company_dependent | ondelete | Purpose |
|---|---|---|---|
| `property_account_income_id` | True | restrict | Product-level income account override; leave empty to use category |
| `property_account_expense_id` | True | restrict | Product-level expense override; help explicitly notes Anglo-Saxon behaviour |

### `_get_product_accounts()` — Resolution Logic (lines 68–79)

```
INCOME account resolution order:
  1. product.template.property_account_income_id          (product-level)
  2. _get_category_account('property_account_income_categ_id')  (category tree walk)
  3. company.income_account_id                            (company fallback)

EXPENSE account resolution order:
  1. product.template.property_account_expense_id         (product-level)
  2. _get_category_account('property_account_expense_categ_id') (category tree walk)
  3. company.expense_account_id                           (company fallback)
```

**Returns dict:** `{'income': <account>, 'expense': <account>}`

### `_get_category_account(field_name)` — Category Tree Walk (lines 81–92)

```python
def _get_category_account(self, field_name):
    categ = self.categ_id
    while categ:
        account = categ[field_name]
        if account:
            return account
        categ = categ.parent_id
    return self.env['account.account']
```

**Key behaviour:** walks `categ_id → parent_id` iteratively upward. The first non-empty value found wins. If no category in the entire hierarchy has the account set, returns an empty recordset and the company fallback kicks in.

**No parent inheritance is automatic** — parent category accounts are NOT automatically copied to child categories at creation. They are only _consulted dynamically_ at account resolution time.

### `get_product_accounts(fiscal_pos=None)` — Public API (lines 94–98)

Applies fiscal position mapping on top of `_get_product_accounts()`. Called by invoice line, purchase line, etc.

---

## 3. STOCK_ACCOUNT MODULE — ProductCategory Extension

**File:** `odoo/addons/stock_account/models/product.py` (lines 725–787)

### Fields on `product.category` (_inherit)

| Field | Type | company_dependent | Notes |
|---|---|---|---|
| `property_valuation` | Selection (periodic/real_time) | True | Inventory valuation mode |
| `property_cost_method` | Selection (standard/fifo/average) | True | Costing method |
| `property_stock_journal` | Many2one → `account.journal` | True | Journal for automated stock entries |
| `property_stock_valuation_account_id` | Many2one → `account.account` | True | Stock valuation account (balance sheet asset) |
| `property_price_difference_account_id` | Many2one → `account.account` | True | Price difference account (std cost only) |
| `account_stock_variation_id` | Many2one → `account.account` | False (related) | Related: `property_stock_valuation_account_id.account_stock_variation_id` |

**NOTE — v16→v19 Schema Change:** `property_stock_account_input_categ_id` and `property_stock_account_output_categ_id` **do NOT exist in v19**. These fields from Odoo ≤16 have been removed. V19 uses a single `property_stock_valuation_account_id` with a linked `account_stock_variation_id` (set on the account.account record itself).

---

## 4. STOCK_ACCOUNT MODULE — ProductTemplate `_get_product_accounts()` Override

**File:** `odoo/addons/stock_account/models/product.py` (lines 130–156)

### Stock Valuation Resolution (lines 136–141)

```
STOCK VALUATION account resolution order:
  1. categ_id.property_stock_valuation_account_id
  2. categ_id._fields['property_stock_valuation_account_id'].get_company_dependent_fallback(categ_id)
  3. env.company.account_stock_valuation_id

STOCK VARIATION:
  accounts['stock_variation'] = accounts['stock_valuation'].account_stock_variation_id
```

**`get_company_dependent_fallback()`** (defined in `odoo/orm/fields.py` line 794): queries `ir.default` with superuser + current company to get the default value set for the model/field/company. This is the Odoo 19 replacement for `ir.property` read for company-dependent fields.

### Stock Journal Resolution (lines 149–156)

```
STOCK JOURNAL resolution order:
  1. categ_id.property_stock_journal
  2. categ_id._fields['property_stock_journal'].get_company_dependent_fallback(categ_id)
  3. env.company.account_stock_journal_id
```

---

## 5. COMPANY-SCOPED DEFAULTS — `ir.default` Mechanism

**File:** `odoo/addons/account/models/company.py` (lines 1145–1148)

```python
def _set_category_defaults(self):
    for company in self:
        self.env['ir.default'].set('product.category', 'property_account_expense_categ_id',
            company.expense_account_id.id, company_id=company.id)
        self.env['ir.default'].set('product.category', 'property_account_income_categ_id',
            company.income_account_id.id, company_id=company.id)
```

**Mechanism:** `company_dependent=True` fields in Odoo 19 store per-company defaults in `ir.default` (model: `product.category`, field name, company_id). When a `product.category` record has no explicit value for the field, the framework reads the `ir.default` for that company. This is analogous to the `ir.property` mechanism in Odoo ≤16, but replaced.

**Company-level fallback fields** (`res.company`):
- `income_account_id` → propagated as default to `property_account_income_categ_id`
- `expense_account_id` → propagated as default to `property_account_expense_categ_id`
- `account_stock_valuation_id` → used as third-tier fallback in stock valuation resolution
- `account_stock_journal_id` → used as third-tier fallback in stock journal resolution

---

## 6. REMOVAL STRATEGY — ProductCategory (stock module, NOT stock_account)

**File:** `odoo/addons/stock/models/product.py` (lines 1303–1319)

```python
removal_strategy_id = fields.Many2one(
    'product.removal', 'Force Removal Strategy',
    help="Set a specific removal strategy that will be used regardless of the source location..."
    tracking=True,
)
```

**Options via `product.removal`:** FIFO, LIFO, Closest location, FEFO (requires Expiration Dates), Least Packages (FIFO + fewest packages).

**NOT in stock_account** — this is defined in the `stock` module, not `stock_account`. It controls picking strategy, not accounting entries.

---

## 7. THAI l10n (l10n_th) PRODUCT CATEGORY CONFIGURATION

**Finding:** The Thai COA module (`l10n_th`) provides only:
- `account.account-th.csv` — chart of accounts
- `account.tax-th.csv` — VAT tax definitions
- `account.asset-th.csv` — asset definitions
- `account.tax.group-th.csv` — tax groups
- `demo/demo_company.xml` — demo company (no product.category account assignments found)

**Conclusion:** l10n_th does **NOT** pre-configure `property_account_income_categ_id`, `property_account_expense_categ_id`, or `property_stock_valuation_account_id` on any `product.category` records in demo data. Thai accounts must be manually assigned to product categories after COA installation, or set at the company level via `income_account_id`/`expense_account_id`.

---

## 8. `account_journal_id` on product.category

**Finding:** There is **no** field named `account_journal_id` on `product.category`. The journal field is `property_stock_journal` (a company_dependent Many2one to `account.journal`). It is used only for automated (perpetual/real_time) inventory valuation journal entries.

---

## 9. ProductProduct._get_product_accounts()

**File:** `odoo/addons/account/models/product.py` (lines 220–221) and `stock_account/models/product.py` (inherits from ProductTemplate via `product_tmpl_id`).

```python
class ProductProduct(models.Model):
    _inherit = "product.product"

    def _get_product_accounts(self):
        return self.product_tmpl_id._get_product_accounts()
```

`product.product` delegates directly to `product.template._get_product_accounts()`. No variant-level account override beyond what the template provides.

---

## 10. Full Account Chain Summary (L3)

```
Customer Invoice → account.move.line → product.product._get_product_accounts()
  → product.template._get_product_accounts()  [account module]
      INCOME:
        ① product.template.property_account_income_id  [company_dependent, product-level]
        ② product.category._get_category_account('property_account_income_categ_id')
            → walks categ_id → parent_id until non-empty found
        ③ res.company.income_account_id  [global company fallback]
      EXPENSE (COGS in Anglo-Saxon/perpetual):
        ① product.template.property_account_expense_id
        ② product.category._get_category_account('property_account_expense_categ_id')
        ③ res.company.expense_account_id
  → stock_account module adds:
      STOCK_VALUATION:
        ① product.category.property_stock_valuation_account_id
        ② ir.default fallback for that field (company-scoped)
        ③ res.company.account_stock_valuation_id
      STOCK_VARIATION:
        Derived: stock_valuation_account.account_stock_variation_id
      STOCK_JOURNAL:
        ① product.category.property_stock_journal
        ② ir.default fallback
        ③ res.company.account_stock_journal_id
  → fiscal position mapping applied via get_product_accounts(fiscal_pos)
```

---

## Source Files Read

| File | Lines Read |
|---|---|
| `account/models/product.py` | 1–559 |
| `stock_account/models/product.py` | 1–787 |
| `stock_account/models/account_account.py` | 1–13 |
| `stock/models/product.py` | 1303–1331 (categ removal_strategy) |
| `account/models/company.py` | 282–295, 1145–1148 |
| `odoo/orm/fields.py` | 794–801 |
