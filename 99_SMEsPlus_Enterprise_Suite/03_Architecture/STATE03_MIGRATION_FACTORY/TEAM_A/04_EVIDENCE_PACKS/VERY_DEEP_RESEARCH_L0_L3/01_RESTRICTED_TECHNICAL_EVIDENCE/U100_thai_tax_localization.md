# U100 — Thai Tax Localization (L1/L2/L3) — P0 TH
## DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

**Unit**: U100
**Phase**: Third-Pass — P0 Thai Tax
**Scope**: l10n_th Chart of Accounts, Thai VAT templates; l10n_th_withholding_tax if present
**Modules**: l10n_th (only — l10n_th_withholding_tax does NOT exist as a separate module)
**Function-IDs targeted**: NEW:U100-F01 through U100-F12
**L-levels**: L1, L2, L3
**Proof layers**: P1, P3
**Flags**: TH
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: U24 (localization framework), U13 (account tax chart localization)

---

## Module Presence Findings

Only ONE Thai localization module exists under the addons root:
- `l10n_th/` — **PRESENT** (Thai Accounting — CoA + VAT + WHT + QR + Reports)
- `l10n_th_withholding_tax/` — **ABSENT** (no separate WHT module)
- `l10n_th_wht/` — **ABSENT**

All Thai tax functionality (VAT, withholding tax PND3/PND53, tax reports) is contained within `l10n_th`.

**Addons root**: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons`

---

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U100-001 | U100-F01 | l10n_th/__manifest__.py:3 | 'name': 'Thailand - Accounting' | DEF | always | TH | Module `l10n_th` is named "Thailand - Accounting"; `countries` is `['th']`; depends on `account_qr_code_emv` and `account` | NR-U100-001 |
| U100-002 | U100-F01 | l10n_th/__manifest__.py:20 | 'auto_install': ['account'] | CONFIG | when account installed | TH | `l10n_th` auto-installs when `account` is installed for Thai companies | NR-U100-002 |
| U100-003 | U100-F01 | l10n_th/__manifest__.py:28 | 'post_init_hook': '_preserve_tag_on_taxes' | TRIGGER | post_install | TH | `_preserve_tag_on_taxes` post-init hook runs after module install to preserve tax tags | NR-U100-003 |
| U100-004 | U100-F02 | l10n_th/data/template/account.tax.group-th.csv:2 | "tax_group_1","WHT 1%" | DEF | always | TH | Tax group `tax_group_1` = "WHT 1%" maps payable account `l10n_th_account_213500` and receivable `l10n_th_account_114401` | NR-U100-004 |
| U100-005 | U100-F02 | l10n_th/data/template/account.tax.group-th.csv:3 | "tax_group_2","WHT 2%" | DEF | always | TH | Tax group `tax_group_2` = "WHT 2%" defined with same payable/receivable WHT accounts | NR-U100-005 |
| U100-006 | U100-F02 | l10n_th/data/template/account.tax.group-th.csv:4 | "tax_group_3","WHT 3%" | DEF | always | TH | Tax group `tax_group_3` = "WHT 3%" defined | NR-U100-006 |
| U100-007 | U100-F02 | l10n_th/data/template/account.tax.group-th.csv:5 | "tax_group_5","WHT 5%" | DEF | always | TH | Tax group `tax_group_5` = "WHT 5%" defined | NR-U100-007 |
| U100-008 | U100-F02 | l10n_th/data/template/account.tax.group-th.csv:6 | "tax_group_vat_7","VAT 7%" | DEF | always | TH | Tax group `tax_group_vat_7` = "VAT 7%" maps payable account `l10n_th_account_213400` and receivable `l10n_th_account_114400` | NR-U100-008 |
| U100-009 | U100-F03 | l10n_th/data/template/account.tax-th.csv:2 | "tax_input_vat","7%","Input VAT 7%" | DEF | type_tax_use=purchase | TH | `tax_input_vat` is Input VAT 7% (`amount_type=percent`, `amount=7.0`, `type_tax_use=purchase`), account `l10n_th_account_114200` | NR-U100-009 |
| U100-010 | U100-F03 | l10n_th/data/template/account.tax-th.csv:6 | "tax_output_vat","7%","Output VAT 7%" | DEF | type_tax_use=sale | TH | `tax_output_vat` is Output VAT 7% (`amount_type=percent`, `amount=7.0`, `type_tax_use=sale`), account `l10n_th_account_213200` | NR-U100-010 |
| U100-011 | U100-F03 | l10n_th/data/template/account.tax-th.csv:10 | "tax_input_vat_0","0%","Input VAT 0%" | DEF | type_tax_use=purchase | TH | `tax_input_vat_0` is Input VAT 0% for 0%-rated purchases (e.g. certain international transport) | NR-U100-011 |
| U100-012 | U100-F03 | l10n_th/data/template/account.tax-th.csv:14 | "tax_output_vat_0","0%","Output VAT 0%" | DEF | type_tax_use=sale | TH | `tax_output_vat_0` is Output VAT 0% for 0%-rated sales (export); tags include line `2. Less sales subject to 0% tax rate` | NR-U100-012 |
| U100-013 | U100-F03 | l10n_th/data/template/account.tax-th.csv:18 | "tax_input_vat_exempted","0% EXEMPT" | DEF | type_tax_use=purchase | TH | `tax_input_vat_exempted` is Input VAT Exempted (0%, purchase) for VAT-exempt input or non-deductible input tax | NR-U100-013 |
| U100-014 | U100-F03 | l10n_th/data/template/account.tax-th.csv:22 | "tax_output_vat_exempted","0% EXEMPT" | DEF | type_tax_use=sale | TH | `tax_output_vat_exempted` is Output VAT Exempted (0%, sale) for VAT-exempt sales (e.g. agricultural produce, residential rental) | NR-U100-014 |
| U100-015 | U100-F04 | l10n_th/data/template/account.tax-th.csv:26 | "tax_wht_co_1","1% WH C T","Company Withholding Tax 1%" | DEF | type_tax_use=purchase | TH | `tax_wht_co_1` is Company WHT 1% (Transportation), `amount=-1.0`, PND53 tag, account `l10n_th_account_213302` | NR-U100-015 |
| U100-016 | U100-F04 | l10n_th/data/template/account.tax-th.csv:30 | "tax_wht_co_2","2% WH C A","Company Withholding Tax 2%" | DEF | type_tax_use=purchase | TH | `tax_wht_co_2` is Company WHT 2% (Advertising), `amount=-2.0`, PND53 tag, account `l10n_th_account_213302` | NR-U100-016 |
| U100-017 | U100-F04 | l10n_th/data/template/account.tax-th.csv:34 | "tax_wht_co_3","3% WH C S","Company Withholding Tax 3%" | DEF | type_tax_use=purchase | TH | `tax_wht_co_3` is Company WHT 3% (Service), `amount=-3.0`, PND53 tag, account `l10n_th_account_213302` | NR-U100-017 |
| U100-018 | U100-F04 | l10n_th/data/template/account.tax-th.csv:38 | "tax_wht_co_5","5% WH C R","Company Withholding Tax 5%" | DEF | type_tax_use=purchase | TH | `tax_wht_co_5` is Company WHT 5% (Rental), `amount=-5.0`, PND53 tag, account `l10n_th_account_213302` | NR-U100-018 |
| U100-019 | U100-F05 | l10n_th/data/template/account.tax-th.csv:42 | "tax_wht_pers_1","1% WH P T","Personal Withholding Tax 1%" | DEF | type_tax_use=purchase | TH | `tax_wht_pers_1` is Personal WHT 1% (Transportation), `amount=-1.0`, PND3 tag, account `l10n_th_account_213301` | NR-U100-019 |
| U100-020 | U100-F05 | l10n_th/data/template/account.tax-th.csv:46 | "tax_wht_pers_2","2% WH P A","Personal Withholding Tax 2%" | DEF | type_tax_use=purchase | TH | `tax_wht_pers_2` is Personal WHT 2% (Advertising), `amount=-2.0`, PND3 tag, account `l10n_th_account_213301` | NR-U100-020 |
| U100-021 | U100-F05 | l10n_th/data/template/account.tax-th.csv:50 | "tax_wht_pers_3","3% WH P S","Personal Withholding Tax 3%" | DEF | type_tax_use=purchase | TH | `tax_wht_pers_3` is Personal WHT 3% (Service), `amount=-3.0`, PND3 tag, account `l10n_th_account_213301` | NR-U100-021 |
| U100-022 | U100-F05 | l10n_th/data/template/account.tax-th.csv:54 | "tax_wht_pers_5","5% WH P R","Personal Withholding Tax 5%" | DEF | type_tax_use=purchase | TH | `tax_wht_pers_5` is Personal WHT 5% (Rental), `amount=-5.0`, PND3 tag, account `l10n_th_account_213301` | NR-U100-022 |
| U100-023 | U100-F06 | l10n_th/data/template/account.tax-th.csv:58 | "tax_wht_income_1","1% WH T","Withholding Income Tax 1%" | DEF | type_tax_use=sale | TH | `tax_wht_income_1` is seller-side WHT receivable 1% (Transportation), `amount=-1.0`, account `l10n_th_account_114300` | NR-U100-023 |
| U100-024 | U100-F06 | l10n_th/data/template/account.tax-th.csv:62 | "tax_wht_income_2","2% WH A" | DEF | type_tax_use=sale | TH | `tax_wht_income_2` is seller-side WHT receivable 2% (Advertising), account `l10n_th_account_114300` | NR-U100-024 |
| U100-025 | U100-F06 | l10n_th/data/template/account.tax-th.csv:66 | "tax_wht_income_3","3% WH S" | DEF | type_tax_use=sale | TH | `tax_wht_income_3` is seller-side WHT receivable 3% (Service), account `l10n_th_account_114300` | NR-U100-025 |
| U100-026 | U100-F06 | l10n_th/data/template/account.tax-th.csv:70 | "tax_wht_income_5","5% WH R" | DEF | type_tax_use=sale | TH | `tax_wht_income_5` is seller-side WHT receivable 5% (Rental), account `l10n_th_account_114300` | NR-U100-026 |
| U100-027 | U100-F07 | l10n_th/models/template_th.py:9 | @template('th') | DEF | always | TH | `AccountChartTemplate._get_th_template_data` decorated `@template('th')` returns `code_digits=6`, AR=`l10n_th_account_112100`, AP=`l10n_th_account_212100` | NR-U100-027 |
| U100-028 | U100-F07 | l10n_th/models/template_th.py:33 | 'account_sale_tax_id': 'tax_output_vat' | ASSIGN | company setup | TH | Default sale tax is `tax_output_vat` (Output VAT 7%); default purchase tax is `tax_input_vat` (Input VAT 7%) | NR-U100-028 |
| U100-029 | U100-F07 | l10n_th/models/template_th.py:41 | 'tax_exigibility': 'True' | CONFIG | company setup | TH | Thai company template sets `tax_exigibility=True`, enabling cash-basis tax accounting | NR-U100-029 |
| U100-030 | U100-F08 | l10n_th/data/account_tax_report_data.xml:4 | model="account.report" | DEF | country=TH | TH | Thai VAT tax report record `tax_report` (รายงานภาษี) created with `root_report_id=account.generic_tax_report`, `allow_foreign_vat=True`, `availability_condition=country` | NR-U100-030 |
| U100-031 | U100-F08 | l10n_th/data/account_tax_report_data.xml:227 | id="tax_report_pnd53" | DEF | country=TH | TH | PND53 report record (ภ.ง.ด. 53) created for corporate WHT; lines: Total Income (INCOME_PND53), Total Remittance (P53), Surcharge (S53), Total | NR-U100-031 |
| U100-032 | U100-F08 | l10n_th/data/account_tax_report_data.xml:291 | id="tax_report_pnd3" | DEF | country=TH | TH | PND3 report record (ภ.ง.ด. 3) created for personal WHT; lines: Total Income (INCOME_PND3), Total Remittance (P3), Surcharge (S3), Total | NR-U100-032 |
| U100-033 | U100-F09 | l10n_th/data/account_tax_report_data.xml:122 | id="tax_report_vat_payable" | CALC | if output > input | TH | VAT line 8 "Tax payable" uses aggregation formula `OUTPUTTAX_TAX.balance - INPUTTAX_TAX.balance` with `subformula=if_above(THB(0))` | NR-U100-033 |
| U100-034 | U100-F09 | l10n_th/data/account_tax_report_data.xml:148 | id="tax_report_vat_payment_last_period" | CALC | carryover | TH | VAT line 10 "Excess tax payment carried forward" uses `engine=external`, `formula=most_recent`, `date_scope=previous_return_period`; VAT credit carries forward automatically | NR-U100-034 |
| U100-035 | U100-F10 | l10n_th/models/account_move.py:9 | if self.company_id.account_fiscal_country_id.code == 'TH' | GUARD | country=TH | TH | `AccountMove._get_name_invoice_report` returns `l10n_th.report_invoice_document` when fiscal country is TH; otherwise delegates to super() | NR-U100-035 |
| U100-036 | U100-F11 | l10n_th/models/res_partner.py:9 | l10n_th_branch_name = fields.Char | DEF | is_company + country_code=TH | TH | `ResPartner.l10n_th_branch_name` computed field returns branch code label or "Headquarter" for Thai company partners | NR-U100-036 |
| U100-037 | U100-F12 | l10n_th/models/res_bank.py:17 | def _check_th_proxy(self) | GUARD | country_code=TH | TH | `ResPartnerBank._check_th_proxy` validates Thai proxy types: `ewallet_id`, `merchant_tax_id` (13-digit regex), `mobile` (10-digit regex); raises `ValidationError` on mismatch | NR-U100-037 |
| U100-038 | U100-F12 | l10n_th/models/res_bank.py:56 | if currency.name not in ['THB'] | GUARD | qr_method=emv_qr, country=TH | TH | QR code generation for Thai bank accounts only allowed in THB currency | NR-U100-038 |
| U100-039 | U100-F04 | l10n_th/data/template/account.tax-th.csv:26 | "amount":"-1.0" | CALC | WHT purchase | TH | WHT taxes use **negative** `amount` values (e.g., `-1.0`, `-2.0`, `-3.0`, `-5.0`) so WHT reduces the invoice payable amount on purchase invoices | NR-U100-039 |
| U100-040 | U100-F06 | l10n_th/data/template/account.tax-th.csv:58 | "price_include_override","tax_excluded" | CONFIG | WHT income | TH | Seller-side WHT income taxes (`tax_wht_income_*`) have `price_include_override=tax_excluded` ensuring WHT is computed on the pre-tax base | NR-U100-040 |

---

## Absence Notes

- `l10n_th_withholding_tax` module: **NOT PRESENT** in Odoo 19 Community addons. WHT functionality is fully embedded in `l10n_th` via `account.tax` templates with negative percent amounts and PND3/PND53 tax tags.
- No `account.withhold` custom model exists; WHT uses standard `account.tax` mechanism with negative amounts.
- No PND1 (payroll WHT) support found in `l10n_th` — PND1 is typically handled via payroll module.
- No fiscal position records found in `l10n_th` (fiscal positions for export/zero-rate are expected to be configured manually or via user setup).
