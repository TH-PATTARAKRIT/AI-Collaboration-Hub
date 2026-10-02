# U100 Neutral Knowledge — Thai Tax Localization
## DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

**Unit**: U100
**Date**: 2026-10-02
**Status**: GATE-PASS

---

| NR-ID | Statement |
|---|---|
| NR-U100-001 | The Thailand accounting localization module is named "Thailand - Accounting", scoped to Thailand, and depends on the core accounting module and an EMV QR code module. It auto-installs when the accounting module is activated for Thai companies. |
| NR-U100-002 | The Thai localization auto-installs when the core accounting module is activated for a Thai-country company. No separate manual installation step is required. |
| NR-U100-003 | A post-installation hook preserves existing tax tags on taxes when the module is installed, preventing loss of tax tag assignments during setup. |
| NR-U100-004 | A withholding tax group for 1% WHT is defined with a designated payable account and a receivable account. Both accounts are mapped at the tax group level for all 1% WHT transactions. |
| NR-U100-005 | A withholding tax group for 2% WHT is defined with the same payable and receivable WHT accounts as the 1% group. |
| NR-U100-006 | A withholding tax group for 3% WHT is defined. |
| NR-U100-007 | A withholding tax group for 5% WHT is defined. |
| NR-U100-008 | A VAT tax group for the standard 7% VAT rate is defined, mapping to a VAT payable account and a VAT receivable account distinct from the WHT accounts. |
| NR-U100-009 | Input VAT at 7% (standard rate) is pre-configured as a purchase tax template, posting to the input VAT receivable account. Its tax tag links to the Thai VAT return line for deductible input tax. |
| NR-U100-010 | Output VAT at 7% (standard rate) is pre-configured as a sales tax template, posting to the output VAT payable account. Its tax tag links to the Thai VAT return line for taxable sales. |
| NR-U100-011 | Input VAT at 0% is pre-configured for purchases entitled to the 0% reduced rate (such as certain international transport services). |
| NR-U100-012 | Output VAT at 0% is pre-configured for exports and other 0%-rated sales. Its tax tags link to the VAT return lines for both total sales and the deduction for 0%-rated sales. |
| NR-U100-013 | Input VAT Exempted (0% exempt) is pre-configured for purchases from VAT-exempt suppliers or for non-deductible input tax. |
| NR-U100-014 | Output VAT Exempted (0% exempt) is pre-configured for VAT-exempt sales such as agricultural produce and residential rental. Its tax tags link to the exempted-sales deduction line on the VAT return. |
| NR-U100-015 | A corporate withholding tax at 1% for transportation payments is pre-configured as a purchase tax. It posts to the PND53 (corporate income tax remittance) payable account using a negative rate so the amount reduces the invoice payable. |
| NR-U100-016 | A corporate withholding tax at 2% for advertising payments is pre-configured as a purchase tax posting to the PND53 payable account with a negative rate. |
| NR-U100-017 | A corporate withholding tax at 3% for service payments is pre-configured as a purchase tax posting to the PND53 payable account with a negative rate. |
| NR-U100-018 | A corporate withholding tax at 5% for rental payments is pre-configured as a purchase tax posting to the PND53 payable account with a negative rate. |
| NR-U100-019 | A personal withholding tax at 1% for transportation payments is pre-configured as a purchase tax. It posts to the PND3 (personal income tax remittance) payable account with a negative rate. |
| NR-U100-020 | A personal withholding tax at 2% for advertising payments is pre-configured as a purchase tax posting to the PND3 payable account with a negative rate. |
| NR-U100-021 | A personal withholding tax at 3% for service payments is pre-configured as a purchase tax posting to the PND3 payable account with a negative rate. |
| NR-U100-022 | A personal withholding tax at 5% for rental payments is pre-configured as a purchase tax posting to the PND3 payable account with a negative rate. |
| NR-U100-023 | A seller-side withholding income tax receivable at 1% (transportation) is pre-configured as a sales tax. The deducted WHT amount posts to a prepaid tax receivable account, to be claimed as a tax credit. |
| NR-U100-024 | A seller-side withholding income tax receivable at 2% (advertising) is pre-configured as a sales tax posting to the prepaid tax receivable account. |
| NR-U100-025 | A seller-side withholding income tax receivable at 3% (service) is pre-configured as a sales tax posting to the prepaid tax receivable account. |
| NR-U100-026 | A seller-side withholding income tax receivable at 5% (rental) is pre-configured as a sales tax posting to the prepaid tax receivable account. |
| NR-U100-027 | The Thai chart of accounts template uses 6-digit account codes. Default accounts for trade receivables, trade payables, and stock valuation are mapped at chart-of-accounts template level. |
| NR-U100-028 | When a Thai company is set up, the default sale tax is automatically set to the 7% output VAT template and the default purchase tax to the 7% input VAT template. |
| NR-U100-029 | The Thai company template enables cash-basis tax accounting by setting the tax exigibility flag, meaning VAT is recognized at payment rather than at invoicing. |
| NR-U100-030 | A Thai VAT tax report (equivalent to the PP.30 form) is provided as a standard tax report for Thai companies, covering output tax, input tax, and the net VAT payable or excess. It permits foreign VAT configuration. |
| NR-U100-031 | A PND53 withholding tax remittance report for corporate payees is provided, covering total income subject to WHT, total tax remitted, surcharges, and a combined total. |
| NR-U100-032 | A PND3 withholding tax remittance report for individual payees is provided, with the same structure as PND53. |
| NR-U100-033 | The Thai VAT report line 8 (tax payable) is computed as output tax minus input tax and is displayed only when the result is positive. |
| NR-U100-034 | Excess input VAT from a prior period is automatically carried forward to line 10 of the current period VAT return using the most-recent external carryover mechanism. |
| NR-U100-035 | For Thai companies, the standard invoice print report is replaced with a Thai-localized invoice report template. For all other countries, the standard report is used. |
| NR-U100-036 | Thai company partners have a computed branch name field: if a company registry code is present it displays "Branch [code]"; otherwise it displays "Headquarter". This supports Thai tax invoice branch identification requirements. |
| NR-U100-037 | Thai bank account QR code proxy types are restricted to ewallet ID, 13-digit merchant tax ID, and 10-digit mobile number. Validation errors are raised for invalid formats. |
| NR-U100-038 | Thai EMV QR code generation is restricted to Thai Baht (THB) currency only. |
| NR-U100-039 | Withholding tax on purchases uses negative percentage amounts so that the WHT reduces the amount payable on the vendor invoice, reflecting the buyer's obligation to remit WHT directly to the Revenue Department. |
| NR-U100-040 | Seller-side withholding income taxes are configured with tax-excluded price inclusion, ensuring the WHT is computed on the pre-tax invoice base amount. |
