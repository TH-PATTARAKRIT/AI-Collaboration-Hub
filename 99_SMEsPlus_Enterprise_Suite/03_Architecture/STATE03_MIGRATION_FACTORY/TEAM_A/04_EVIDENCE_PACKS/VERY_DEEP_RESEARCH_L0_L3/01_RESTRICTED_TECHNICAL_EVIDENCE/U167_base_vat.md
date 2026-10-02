# U167 — base_vat: Restricted Technical Evidence
**Unit:** U167 | **Module:** base_vat | **Group:** G02 | **Priority:** P1 (TH)
**Date:** 2026-10-02 | **Scope:** Thailand Accounting Localization

---

## 1. Module Identity (`__manifest__.py`)

- **Name:** VAT Number Validation
- **Version:** 2.0
- **Category:** Accounting/Accounting
- **Depends:** `['account']`
- **License:** LGPL-3
- **Author:** Odoo S.A.
- **Data files:** `data/ir_cron.xml`, `views/res_config_settings_views.xml`, `views/res_partner_views.xml`

The manifest documents two validation tiers: (1) offline check using known national rules (check digit), always available; (2) online EU VIES check when `vat_check_vies` is enabled on the company, querying the European VIES database via Odoo IAP. For non-EU countries (including Thailand), VIES is not applicable — offline validation always applies.

---

## 2. Models Structure

Files under `base_vat/models/`:
- `res_partner.py` — core validation logic, country-specific check functions, `check_vat_th()`
- `res_company.py` — adds `vat_check_vies` Boolean field to company
- `res_config_settings.py` — exposes `vat_check_vies` via company settings
- `res_country.py` — adds `has_foreign_fiscal_position` computed field

---

## 3. Validation Entry Point — `_run_vat_checks()`

**File:** `base_vat/models/res_partner.py`, lines 107–164

```python
@api.model
def _run_vat_checks(self, country, vat, partner_name='', validation='error'):
```

Overrides the base `account` module method. Key logic:
1. Skips if `country` or `vat` is empty (returns `vat, False`)
2. Handles `'/'` as explicit "no VAT" marker
3. Splits VAT into country prefix + number via `_split_vat()`
4. Handles EU prefix country group
5. Calls `_format_vat_number()` to normalise (compact) the VAT
6. Calls `_check_vat_number()` for the actual validation
7. On failure: raises `ValidationError` (if `validation='error'`) or returns `('', country_code)` (if `validation='setnull'`)

The `no_vat_validation` context key bypasses validation entirely — used for API pushes from external platforms.

---

## 4. VAT Country Mapping (`_ref_vat` dict)

**File:** `base_vat/models/res_partner.py`, lines 25–88

The `_ref_vat` dict maps lowercase 2-letter country codes to example/expected VAT format strings. It is used in error messages only — it is NOT a routing table for which validator to call. The validation routing occurs in `_check_vat_number()`.

**Thailand entry:**
```python
'th': '1234545678781',
```

This indicates the expected format is a 13-digit numeric TIN (Tax Identification Number).

Countries with explicit entries include: al, ar, at, au, be, bg, br, cr, ch, cl, co, cy, cz, de, dk, do, ec, ee, es, fi, fr, gb, gr, hu, hr, id, ie, il, in, is, it, jp, kr, lt, lu, lv, ma, mc, mt, mx, nl, no, nz, pe, ph, pl, pt, ro, rs, ru, se, si, sk, sm, **th**, tr, ua, uy, uz, ve, xi, sa.

---

## 5. Validation Dispatcher — `_check_vat_number()`

**File:** `base_vat/models/res_partner.py`, lines 346–350

```python
@api.model
def _check_vat_number(self, country_code, vat_number):
    check_func_name = 'check_vat_' + country_code.lower()
    check_func = getattr(self, check_func_name, None) or getattr(stdnum.util.get_cc_module(country_code, 'vat'), 'is_valid', None)
    return check_func(vat_number) if check_func else True
```

Priority order:
1. Model method named `check_vat_<cc>` (e.g., `check_vat_th`) — Odoo custom
2. `stdnum.util.get_cc_module(cc, 'vat').is_valid` — python-stdnum library
3. If neither exists: returns `True` (no validation, any value accepted)

---

## 6. Thailand-Specific Validator — `check_vat_th()`

**File:** `base_vat/models/res_partner.py`, lines 894–896

```python
def check_vat_th(self, vat):
    check_func = stdnum.util.get_cc_module('th', 'tin').is_valid
    return check_func(vat)
```

- Uses python-stdnum module `th.tin` (Thai Tax Identification Number), NOT `th.vat`
- The stdnum `th.tin` module validates Thai 13-digit TINs per Thai Revenue Department specification
- Supports both plain 13-digit format (`1234545678781`) and hyphenated display format (`1-2345-45678-78-1`)
- The `check_vat_th()` method is a thin wrapper — all checksum and format logic resides in python-stdnum

**Reference VAT example from `_ref_vat`:** `'1234545678781'` (13 digits, all numeric)

---

## 7. VAT Formatter — `_format_vat_number()`

**File:** `base_vat/models/res_partner.py`, lines 946–954

```python
@api.model
def _format_vat_number(self, country_code, vat):
    stdnum_vat_fix_func = getattr(stdnum.util.get_cc_module(country_code, 'vat'), 'compact', None)
    format_func_name = 'format_vat_' + country_code.lower()
    format_func = getattr(self, format_func_name, None) or stdnum_vat_fix_func
    if format_func:
        vat = format_func(vat)
    return vat
```

For Thailand (`TH`):
- No custom `format_vat_th()` method exists in the codebase
- Falls back to `stdnum.util.get_cc_module('th', 'vat').compact` if that module exists in stdnum
- If no compact function: VAT is stored as-entered

---

## 8. Company VAT Storage — `res_company.py`

**File:** `base_vat/models/res_company.py`, lines 1–11

```python
class ResCompany(models.Model):
    _inherit = 'res.company'
    vat_check_vies = fields.Boolean(string='Verify VAT Numbers')
```

- `base_vat` adds only the `vat_check_vies` Boolean to `res.company`
- The `vat` field itself is defined upstream in `base` module on `res.partner` and inherited by `res.company`
- VIES validation is a company-level setting; when enabled, EU VAT numbers are verified online via IAP

---

## 9. Error Surfacing

**File:** `base_vat/models/res_partner.py`, lines 159–163

Validation errors surface as `ValidationError` (from `odoo.exceptions`), NOT `UserError`. The error message includes:
- The wrong VAT number
- The partner name (or omits it for public user)
- The expected format from `_ref_vat` (e.g., `1234545678781` for Thailand)
- Country's `vat_label` if set (falls back to "VAT")

`ValidationError` prevents the record save and is displayed to the user inline in the form view.

---

## 10. VIES Partner Fields

**File:** `base_vat/models/res_partner.py`, lines 94–104

```python
vies_valid = fields.Boolean(string="Intra-Community Valid", ...)
perform_vies_validation = fields.Boolean(compute='_compute_perform_vies_validation')
```

- `vies_valid`: stored Boolean, indicates EU VIES validity; recomputed on VAT change
- `perform_vies_validation`: computed, True only when partner VAT prefix differs from company country AND `vat_check_vies` is enabled
- For Thai companies (TH prefix), `perform_vies_validation` is always False (TH is not EU)

---

## 11. Test Coverage — Thai VAT (`test_vat_th`)

**File:** `base_vat/tests/test_vat_numbers.py`, lines 234–245

```python
def test_vat_th(self):
    test_partner = self.env["res.partner"].create({
        "name": "TH Company",
        "country_id": self.env.ref("base.th").id,
    })
    for tin in ['1234545678781', '1-2345-45678-78-1', '0-99-4-000-61772-1']:
        test_partner.vat = tin

    for tin in ['1234545678782', '1-2345-45678-78-2', '0-99-4-000-61772-2', 'X-99-4-000-61772-1']:
        with self.assertRaises(ValidationError):
            test_partner.vat = tin
```

Valid test cases: plain 13-digit (`1234545678781`), hyphenated long form (`1-2345-45678-78-1`), and alternative hyphenated form (`0-99-4-000-61772-1`).
Invalid cases: wrong check digit, non-numeric prefix (`X-`).

---

## 12. l10n_th Integration Analysis

**File:** `l10n_th/__manifest__.py`

```python
'depends': ['account_qr_code_emv', 'account'],
```

- `l10n_th` does NOT depend on `base_vat`
- `l10n_th` does NOT override or extend VAT validation
- `l10n_th` models directory contains only `template_th.py` (chart of accounts) and `res_bank.py` (bank account handling)
- Thai VAT/TIN validation is fully owned by `base_vat` via `check_vat_th()` + stdnum `th.tin`
- No conflict or override between `l10n_th` and `base_vat`

---

## 13. VIES IAP Architecture

**File:** `base_vat/models/res_partner.py`, lines 263–297

The VIES check uses Odoo IAP (In-App Purchase service) at `https://vies.api.odoo.com`. The flow:
1. `_check_vies_iap()` posts a request with the VAT, db UUID, client credentials, and a webhook URL
2. IAP returns status: `"valid"`, `"unassigned"`, `"pending"`, or `"fault"`
3. A cron job `_cron_check_vies_iap()` polls IAP for pending status updates
4. Webhook at `/base_vat/1/webhook_update_vies` receives async updates from IAP

For Thailand (non-EU), this entire VIES path is never triggered.

---

## 14. `_inverse_vat()` and Trigger Chain

**File:** `base_vat/models/res_partner.py`, lines 166–171

```python
def _inverse_vat(self):
    self._check_vat()

@api.onchange('vat', 'country_id')
def _onchange_vat(self):
    self._check_vat(validation=False)
```

- `_inverse_vat` triggers on write (store=True inverse) — uses `validation='error'` (raises)
- `_onchange_vat` triggers on UI change — uses `validation=False` (no error raised, just format check)
- This dual-mode ensures UI users see validation warnings but API writes get hard errors

---

## 15. `no_vat_validation` Context Key

**File:** `base_vat/models/res_partner.py`, line 146

```python
if not validation or self.env.context.get('no_vat_validation'):
    return vat_to_return, code_to_check
```

Allows bypassing all VAT validation. Used when importing from external platforms (EDI, API integrations) where format control is not possible.

---

## 16. `vat_check_vies` Settings Exposure

**File:** `base_vat/models/res_config_settings.py`, lines 9–10

```python
vat_check_vies = fields.Boolean(related='company_id.vat_check_vies', readonly=False,
    string='Verify VAT Numbers')
```

The VIES setting is exposed in the Company configuration settings form. For Thai deployments, this setting has no functional impact on Thai TIN validation (only affects EU VIES lookup).

---

## 17. Thailand TIN Format (stdnum `th.tin`)

Based on the test cases and reference VAT:
- Format: 13 consecutive digits
- Display variants: `XXXXXXXXXXXXX`, `X-XXXX-XXXXX-XX-X`, `X-XX-X-XXX-XXXXX-X`
- Validation: check digit algorithm (per Thai Revenue Department specification)
- Character constraint: all digits (no letters)
- The `check_vat_th()` delegates entirely to `stdnum.util.get_cc_module('th', 'tin').is_valid`

---

## 18. `format_vat_*` Pattern for Thailand

No `format_vat_th()` method is defined in `base_vat`. This means:
- Input passed to `_format_vat_number('th', vat)` will attempt `stdnum.get_cc_module('th', 'vat').compact`
- If stdnum's `th.vat` module lacks a `compact` function (or the module is `th.tin` not `th.vat`), the VAT is stored as-entered
- Users entering hyphenated Thai TINs (`1-2345-45678-78-1`) may have them stored with hyphens unless stdnum normalises them

---

## Source File Paths

| File | Path |
|------|------|
| Manifest | `odoo/addons/base_vat/__manifest__.py` |
| Partner model | `odoo/addons/base_vat/models/res_partner.py` |
| Company model | `odoo/addons/base_vat/models/res_company.py` |
| Config settings | `odoo/addons/base_vat/models/res_config_settings.py` |
| Country model | `odoo/addons/base_vat/models/res_country.py` |
| VAT tests | `odoo/addons/base_vat/tests/test_vat_numbers.py` |
| l10n_th manifest | `odoo/addons/l10n_th/__manifest__.py` |
