# U229 — res.currency: Currency Rate Model, Multi-Currency Conversion, _convert, Rate Computation

**Unit**: U229  
**Module**: `res.currency` (base) + `res.currency` (account extension)  
**Source**: Community only  
**SHA-prefix**: 4cbd38884786  
**Research Date**: 2026-10-02  

---

## Source Files Examined

1. `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/base/models/res_currency.py`  
2. `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/account/models/res_currency.py`

---

## 1. `res.currency` Fields

### `name` — ISO 4217 Currency Code
- **File**: `base/models/res_currency.py:27`
- `name = fields.Char(string='Currency', size=3, required=True, help="Currency Code (ISO 4217)")`
- Unique constraint enforced: `_unique_name = models.Constraint('unique (name)', ...)` at line 49–52.

### `symbol`
- **File**: `base/models/res_currency.py:30`
- `symbol = fields.Char(help="Currency sign, to be used when printing amounts.", required=True)`

### `rate` (computed, display)
- **File**: `base/models/res_currency.py:31–33`
- `rate = fields.Float(compute='_compute_current_rate', string='Current Rate', digits=0, ...)`
- Help: "The rate of the currency to the currency of rate 1."
- This is a **computed field** — NOT stored in `res.currency`. The actual raw rate is stored in `res.currency.rate.rate`.

### `inverse_rate` (computed, display)
- **File**: `base/models/res_currency.py:33–35`
- `inverse_rate = fields.Float(compute='_compute_current_rate', digits=0, readonly=True, ...)`
- Help: "The currency of rate 1 to the rate of the currency."

### `rate_ids`
- **File**: `base/models/res_currency.py:36`
- `rate_ids = fields.One2many('res.currency.rate', 'currency_id', string='Rates')`

### `rounding`
- **File**: `base/models/res_currency.py:37–38`
- `rounding = fields.Float(string='Rounding Factor', digits=(12, 6), default=0.01, ...)`
- Help: "Amounts in this currency are rounded off to the nearest multiple of the rounding factor."
- DB constraint: `CHECK (rounding>0)` at line 53–56.

### `decimal_places` (computed, stored)
- **File**: `base/models/res_currency.py:39–40`
- `decimal_places = fields.Integer(compute='_compute_decimal_places', store=True, ...)`
- Formula (line 165–168): `int(math.ceil(math.log10(1/currency.rounding)))` when `0 < rounding < 1`, else `0`.

### `active`
- **File**: `base/models/res_currency.py:41`
- `active = fields.Boolean(default=True)`
- Cannot be deactivated if a company uses this currency (lines 108–118).

### `position`
- **File**: `base/models/res_currency.py:42–43`
- `position = fields.Selection([('after', 'After Amount'), ('before', 'Before Amount')], default='after', ...)`

### `iso_numeric`
- **File**: `base/models/res_currency.py:28`
- `iso_numeric = fields.Integer(string="Currency numeric code.", ...)`

---

## 2. `res.currency.rate` Model

### Class declaration
- **File**: `base/models/res_currency.py:346–350`
```python
class ResCurrencyRate(models.Model):
    _name = 'res.currency.rate'
    _description = "Currency Rate"
    _order = "name desc, id"
    _check_company_domain = models.check_company_domain_parent_of
```

### `name` (date field)
- **File**: `base/models/res_currency.py:353–354`
- `name = fields.Date(string='Date', required=True, index=True, default=fields.Date.context_today)`

### `rate` (stored, raw technical rate)
- **File**: `base/models/res_currency.py:355–360`
```python
rate = fields.Float(
    digits=0,
    aggregator="avg",
    help='The rate of the currency to the currency of rate 1',
    string='Technical Rate'
)
```
- **CRITICAL**: This is the stored rate in DB. It is **NOT** an inverse from v16/v17. It represents "how many units of this currency equal 1 unit of the reference currency." For EUR when company_currency=USD: rate is stored as e.g. 0.91 (EUR per 1 USD).
- DB constraint: `CHECK (rate>0)` at lines 383–386.

### `company_rate` (computed+inverse)
- **File**: `base/models/res_currency.py:361–367`
- Computed: `currency_rate.rate / last_rate[company]` — company-relative display rate.
- Inverse: sets `rate = company_rate * last_rate[company]`.

### `inverse_company_rate` (computed+inverse)
- **File**: `base/models/res_currency.py:368–374`
- Computed: `1.0 / company_rate`
- Inverse: sets `company_rate = 1.0 / inverse_company_rate`

### `company_id`
- **File**: `base/models/res_currency.py:376–377`
- `company_id = fields.Many2one('res.company', ..., default=lambda self: self.env.company.root_id)`
- Rates are only valid on **root companies** (branch companies forbidden — line 473–477).

### Uniqueness constraint
- **File**: `base/models/res_currency.py:379–382`
- `_unique_name_per_day = models.Constraint('unique (name,currency_id,company_id)', "Only one currency rate per day allowed!")`
- Only ONE rate per (date, currency, company) combination is allowed.

---

## 3. `_get_rates()` — Rate Lookup Method

**File**: `base/models/res_currency.py:120–139`

```python
def _get_rates(self, company, date):
    if not self.ids:
        return {}
    currency_query = self._as_query(ordered=False)
    currency_id = self.env['res.currency']._field_to_sql(currency_query.table, 'id')
    Rate = self.env['res.currency.rate']
    rate_query = Rate._search([
        ('name', '<=', date),
        ('company_id', 'in', (False, company.root_id.id)),
    ], order='company_id.id, name DESC', limit=1)
    rate_query.add_where(SQL("%s = %s", Rate._field_to_sql(rate_query.table, 'currency_id'), currency_id))
    rate_fallback = Rate._search([
        ('company_id', 'in', (False, company.root_id.id)),
    ], order='company_id.id, name ASC', limit=1)
    rate_fallback.add_where(SQL("%s = %s", Rate._field_to_sql(rate_fallback.table, 'currency_id'), currency_id))
    rate = Rate._field_to_sql(rate_query.table, 'rate')
    return dict(self.env.execute_query(currency_query.select(
        currency_id,
        SQL("COALESCE((%s), (%s), 1.0)", rate_query.select(rate), rate_fallback.select(rate))
    )))
```

**Key behaviors**:
1. Primary lookup: finds the **latest rate on or before** `date` for the given currency and company.
2. Fallback: if no rate exists on or before `date`, uses the **oldest available rate** (ascending order) for the currency.
3. Final fallback: returns `1.0` if no rate at all is found.
4. Both company-specific (`company_id = root_id`) and global (`company_id = False/NULL`) rates are eligible.
5. Company-specific rates take priority over global rates (SQL `ORDER BY company_id.id` puts company-specific last in `DESC` ordering).

---

## 4. `_compute_current_rate()` — Display Rate Computation

**File**: `base/models/res_currency.py:141–160`

```python
@api.depends('rate_ids.rate')
@api.depends_context('to_currency', 'date', 'company', 'company_id')
def _compute_current_rate(self):
    date = self.env.context.get('date') or fields.Date.context_today(self)
    company = self.env['res.company'].browse(self.env.context.get('company_id')) or self.env.company
    to_currency = self.browse(self.env.context.get('to_currency')) or company.currency_id
    currency_rates = (self + to_currency)._get_rates(self.env.company, date)
    for currency in self:
        currency.rate = (currency_rates.get(currency.id) or 1.0) / currency_rates.get(to_currency.id)
        currency.inverse_rate = 1 / currency.rate
        if currency != company.currency_id:
            currency.rate_string = '1 %s = %.6f %s' % (to_currency.name, currency.rate, currency.name)
        else:
            currency.rate_string = ''
```

**Formula**: `displayed_rate = raw_rate(self) / raw_rate(to_currency)`  
The `to_currency` defaults to the company currency. When displaying relative to company currency, `to_currency.rate = 1.0` (base), so `displayed_rate = raw_rate(self)`.

---

## 5. `_get_conversion_rate()` — Conversion Factor

**File**: `base/models/res_currency.py:272–282`

```python
@api.model
def _get_conversion_rate(self, from_currency, to_currency, company=None, date=None):
    if from_currency == to_currency:
        return 1
    company = (company or self.env.company).root_id
    if company in self.env['res.company'].browse(self.env.user._get_company_ids()).root_id:
        from_currency = from_currency.sudo()
    date = date or fields.Date.context_today(self)
    return from_currency.with_company(company).with_context(to_currency=to_currency.id, date=str(date)).inverse_rate
```

Returns `from_currency.inverse_rate` in context of `to_currency`. `inverse_rate = 1 / rate = 1 / (raw_rate(from) / raw_rate(to)) = raw_rate(to) / raw_rate(from)`.

**Net formula**: conversion_rate = `raw_rate(to_currency) / raw_rate(from_currency)`

---

## 6. `_convert()` — Main Conversion Method

**File**: `base/models/res_currency.py:284–303`

```python
def _convert(self, from_amount, to_currency, company=None, date=None, round=True):
    self, to_currency = self or to_currency, to_currency or self
    assert self, "convert amount from unknown currency"
    assert to_currency, "convert amount to unknown currency"
    if from_amount:
        to_amount = from_amount * self._get_conversion_rate(self, to_currency, company, date)
    else:
        return 0.0
    return to_currency.round(to_amount) if round else to_amount
```

**Formula**: `to_amount = from_amount * (raw_rate(to_currency) / raw_rate(from_currency))`  
Rounding applied via `to_currency.round(to_amount)` if `round=True`.  
Zero/falsy `from_amount` returns `0.0` immediately (line 300).

---

## 7. `round()` Method

**File**: `base/models/res_currency.py:216–223`

```python
def round(self, amount):
    self.ensure_one()
    return tools.float_round(amount, precision_rounding=self.rounding)
```

Uses `tools.float_round` with `precision_rounding=self.rounding`. The `rounding` field (default 0.01) determines the precision.

---

## 8. `_compute_decimal_places()` Method

**File**: `base/models/res_currency.py:162–168`

```python
@api.depends('rounding')
def _compute_decimal_places(self):
    for currency in self:
        if 0 < currency.rounding < 1:
            currency.decimal_places = int(math.ceil(math.log10(1/currency.rounding)))
        else:
            currency.decimal_places = 0
```

For THB: `rounding=0.01` → `decimal_places = ceil(log10(100)) = ceil(2.0) = 2`.

---

## 9. Thai Baht (THB) Specifics

No THB-specific override exists in the Community source. THB behaves as a standard currency:
- `rounding=0.01` (standard default) → `decimal_places=2`
- `position='after'` (standard default)
- Symbol: ฿ (stored in `symbol` field)
- No special logic; follows all standard `_convert()` and `_get_rates()` paths.

---

## 10. Base Currency (Company Currency) — Rate = 1.0

In `_get_rates()`: the `COALESCE(..., 1.0)` fallback at line 138 ensures that if no rate record exists for a currency, it returns `1.0`. For the company's base currency, Odoo convention is that a rate record with `rate=1.0` exists, or the fallback 1.0 is used. This makes the formula:

- For base currency: `raw_rate = 1.0`
- For other currency: `raw_rate` = stored `res.currency.rate.rate` value

Conversion from/to base currency: `amount * (1.0 / raw_rate)` or `amount * raw_rate`.

---

## 11. Multi-Company Rate Separation

- `res.currency.rate.company_id` defaults to `self.env.company.root_id` (line 377).
- Constraint at lines 473–477 prevents creating rates for branch (child) companies.
- `_get_rates()` filters by `company_id IN (False, company.root_id.id)` — null = shared global rate.
- `_get_conversion_rate()` always resolves to `company.root_id` (line 278).

---

## 12. `_sanitize_vals()` — Write Priority Rules

**File**: `base/models/res_currency.py:388–393`

```python
def _sanitize_vals(self, vals):
    if 'inverse_company_rate' in vals and ('company_rate' in vals or 'rate' in vals):
        del vals['inverse_company_rate']
    if 'company_rate' in vals and 'rate' in vals:
        del vals['company_rate']
    return vals
```

Priority: `rate > company_rate > inverse_company_rate`. Prevents conflicting field writes.

---

## 13. Account Module Extension (`account/models/res_currency.py`)

### Rounding protection
**File**: `account/models/res_currency.py:26–33`
```python
def write(self, vals):
    if 'rounding' in vals:
        rounding_val = vals['rounding']
        for record in self:
            if (rounding_val > record.rounding or rounding_val == 0) and record._has_accounting_entries():
                raise UserError(...)
    return super().write(vals)
```
Prevents reducing decimal places (increasing rounding) on a currency already used in accounting entries.

### `_create_currency_table()` — Reporting Currency Table
**File**: `account/models/res_currency.py:74–140`
Creates a temporary PostgreSQL table `account_currency_table` with columns:
`(company_id, period_key, date_from, date_next, rate_type, rate)`

Rate types: `'current'`, `'historical'`, `'average'`

For `'current'` rates (line 175): `main_company_unit_factor / rate.rate` — converting other_company currency to main_company currency.

For `'historical'` rates (line 204): `COALESCE(domestic_rate.rate, 1) / rate.rate` — lateral join to get domestic rate at the time of each historical entry.

For `'average'` rates (line 250): weighted average: `SUM(domestic_rate / foreign_rate * days) / SUM(days)` — time-weighted conversion rate over a period.

---

## 14. Migration Flag: Rate Direction Convention

**V19 observation**: The stored `rate` field in `res.currency.rate` represents "number of this currency units per 1 unit of the reference currency." This is the same as Odoo v16/v17 convention. The field `string='Technical Rate'` and help text "The rate of the currency to the currency of rate 1" confirm this.

**No change** in rate direction convention between v16/v17 and v19.

The `company_rate` and `inverse_company_rate` computed fields are display-layer inversions only; the underlying stored `rate` field direction is unchanged.

---

## 15. `_select_companies_rates()` — SQL Helper for Reports

**File**: `base/models/res_currency.py:305–320`

```python
def _select_companies_rates(self):
    return """
        SELECT
            r.currency_id,
            COALESCE(r.company_id, c.id) as company_id,
            r.rate,
            r.name AS date_start,
            (SELECT name FROM res_currency_rate r2
             WHERE r2.name > r.name AND
                   r2.currency_id = r.currency_id AND
                   (r2.company_id is null or r2.company_id = c.id)
             ORDER BY r2.name ASC
             LIMIT 1) AS date_end
        FROM res_currency_rate r
        JOIN res_company c ON (r.company_id is null or r.company_id = c.id)
    """
```

Returns rate ranges per company. Used by reporting layer to join rate history.

---

## Summary of Key Technical Findings

| Topic | Finding |
|---|---|
| Rate storage direction | `res.currency.rate.rate` = units of this currency per 1 unit of base. Unchanged from v16/v17. |
| Conversion formula | `to_amount = from_amount * (to_rate / from_rate)` |
| Rate lookup fallback | Latest rate on or before date; then oldest rate; then 1.0 |
| One rate per day | DB UNIQUE constraint: `(name, currency_id, company_id)` |
| Branch companies | Cannot have rate records; always resolved via root_id |
| Account extension | Adds rounding protection, currency table for reports |
| THB | rounding=0.01, decimal_places=2, no special overrides |
| `inverse_rate` | = 1/rate (display only, not stored in res.currency.rate) |
