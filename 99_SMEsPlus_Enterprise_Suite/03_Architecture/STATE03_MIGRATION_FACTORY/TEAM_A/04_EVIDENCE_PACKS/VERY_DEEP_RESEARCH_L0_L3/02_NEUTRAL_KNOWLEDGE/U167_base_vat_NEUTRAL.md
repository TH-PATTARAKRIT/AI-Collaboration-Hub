# U167 — base_vat: Neutral Knowledge
**Unit:** U167 | **Module:** base_vat | **Group:** G02 | **Priority:** P1 (TH)
**Date:** 2026-10-02 | **Scope:** Thailand Accounting Localization

---

## VDR Claims Table

| # | Claim ID | Layer | Claim (plain prose) | Location | Verified | TH-Relevant | Confidence | Notes |
|---|----------|-------|---------------------|----------|----------|-------------|------------|-------|
| 1 | U167-C01 | L0 | The module is named "VAT Number Validation", version 2.0, licensed LGPL-3, and depends only on the account module | `__manifest__.py` | YES | YES | HIGH | Core dependency is account, not l10n_th |
| 2 | U167-C02 | L0 | Two validation tiers exist: an offline check-digit rule and an online EU VIES database check via Odoo IAP | `__manifest__.py` description | YES | PARTIAL | HIGH | VIES tier does not apply to Thailand |
| 3 | U167-C03 | L1 | The validation entry point is a model method that overrides the base account module, accepting country, VAT string, partner name, and a validation mode parameter | `res_partner.py:107` | YES | YES | HIGH | `_run_vat_checks()` signature |
| 4 | U167-C04 | L1 | A forward-slash character stored as the VAT value is accepted as an explicit declaration of "no valid VAT", bypassing all format checks | `res_partner.py:112-116` | YES | YES | HIGH | Business rule for intentional omission |
| 5 | U167-C05 | L1 | The dictionary that maps country codes to example VAT formats includes Thailand with the reference value being a 13-digit all-numeric string | `res_partner.py:80` | YES | YES | HIGH | `'th': '1234545678781'` |
| 6 | U167-C06 | L1 | The low-level validator dispatches to a model method named after the country code first, then falls back to the python-stdnum library, and if neither exists accepts any value | `res_partner.py:346-350` | YES | YES | HIGH | Priority: custom method > stdnum > True |
| 7 | U167-C07 | L1 | Thailand has a dedicated custom validation method that delegates entirely to the python-stdnum Thai Tax Identification Number module rather than implementing its own logic | `res_partner.py:894-896` | YES | YES | HIGH | `check_vat_th()` calls `stdnum.th.tin.is_valid` |
| 8 | U167-C08 | L1 | The Thai Tax Identification Number is 13 digits long, all numeric, and supports a hyphenated display format with dashes separating digit groups | `test_vat_numbers.py:240` | YES | YES | HIGH | Valid formats confirmed by test cases |
| 9 | U167-C09 | L2 | The test suite includes a dedicated Thai VAT test that verifies three valid TIN formats and confirms four invalid values raise a validation error | `test_vat_numbers.py:234-245` | YES | YES | HIGH | `test_vat_th()` function present |
| 10 | U167-C10 | L1 | Validation errors are raised as ValidationError (blocking record save), not as UserError or warning, and include the wrong value, partner name, and expected format hint | `res_partner.py:159-162` | YES | YES | HIGH | `raise ValidationError(msg)` |
| 11 | U167-C11 | L1 | The VAT formatter is a separate dispatcher that tries a country-specific format method first and falls back to the python-stdnum compact function | `res_partner.py:946-954` | YES | YES | MEDIUM | No `format_vat_th()` exists for Thailand |
| 12 | U167-C12 | L1 | No Thailand-specific VAT formatting method exists in the codebase, so Thai TINs may be stored in whatever form the user enters unless stdnum normalises them | `res_partner.py` (absent) | YES | YES | HIGH | `format_vat_th` not found anywhere |
| 13 | U167-C13 | L1 | The company model gains only one new field from this module: a Boolean flag controlling whether EU VIES online verification is enabled | `res_company.py:10` | YES | PARTIAL | HIGH | `vat_check_vies` field; irrelevant for TH |
| 14 | U167-C14 | L1 | The UI triggers a non-blocking format check on every VAT or country field change, while a write operation triggers a hard blocking check | `res_partner.py:166-171` | YES | YES | HIGH | Dual-mode: onchange=False, inverse=error |
| 15 | U167-C15 | L1 | A context key allows bypassing all VAT validation when records are created or updated via external API integrations | `res_partner.py:146` | YES | YES | HIGH | `no_vat_validation` context key |
| 16 | U167-C16 | L2 | The VIES online check uses Odoo's IAP service with a webhook callback pattern, enabling asynchronous status updates via a scheduled cron job | `res_partner.py:271-312` | YES | NO | HIGH | Not applicable to Thailand (non-EU) |
| 17 | U167-C17 | L2 | The Thailand localization module (l10n_th) does not depend on base_vat and contains no VAT validation code; Thai TIN validation is fully and exclusively handled by base_vat | `l10n_th/__manifest__.py` | YES | YES | HIGH | No override, no extension, no dependency |
| 18 | U167-C18 | L2 | Two boolean fields on the partner record track EU VIES validity and whether VIES validation is applicable to a given partner; for Thai partners these fields are always false or inapplicable | `res_partner.py:94-104` | YES | YES | HIGH | `vies_valid` and `perform_vies_validation` |
| 19 | U167-C19 | L1 | The error message builder respects a country-level VAT label field, substituting the local tax authority's preferred terminology for the generic label "VAT" when defined | `res_partner.py:353-388` | YES | YES | MEDIUM | No custom vat_label observed for Thailand |
| 20 | U167-C20 | L2 | The country model extension adds a computed field indicating whether a foreign fiscal position with a foreign VAT exists for the current company, used in the VIES validation gating logic | `res_country.py:7-18` | YES | LOW | HIGH | Not Thai-specific; affects fiscal position logic |

---

## Summary: Thai VAT Validation in base_vat

The Thai Tax Identification Number (TIN) is validated through a dedicated `check_vat_th()` method that delegates to python-stdnum's `th.tin` module. The expected format is 13 consecutive digits (e.g., `1234545678781`), with hyphenated variants also accepted. Validation errors surface as `ValidationError` and block the record save. The Thailand localization module (`l10n_th`) has no dependency on `base_vat` and performs no VAT override — the entire Thai TIN validation chain resides in `base_vat`. The EU VIES online verification path is not applicable to Thailand.

---

## TH-Relevant Claims Summary

| Claim | TH-Impact |
|-------|-----------|
| U167-C01 | Module depends only on account; TH installs base_vat independently |
| U167-C05 | Thai TIN reference format is 13-digit numeric (`1234545678781`) |
| U167-C06 | Dispatch priority: `check_vat_th` method takes precedence over stdnum vat module |
| U167-C07 | `check_vat_th()` uses `stdnum.th.tin.is_valid` — verified delegation chain |
| U167-C08 | 13-digit TIN; supports plain and hyphenated display formats |
| U167-C09 | Dedicated test `test_vat_th` confirms 3 valid and 4 invalid cases |
| U167-C10 | ValidationError blocks save; user sees expected format hint |
| U167-C12 | No `format_vat_th()` — possible inconsistent storage of hyphenated vs. plain TINs |
| U167-C14 | UI onchange warns; write inverse hard-validates — same for TH as all countries |
| U167-C15 | `no_vat_validation` context bypasses TH TIN check in API integrations |
| U167-C17 | l10n_th has zero VAT validation code; base_vat owns Thai TIN exclusively |
