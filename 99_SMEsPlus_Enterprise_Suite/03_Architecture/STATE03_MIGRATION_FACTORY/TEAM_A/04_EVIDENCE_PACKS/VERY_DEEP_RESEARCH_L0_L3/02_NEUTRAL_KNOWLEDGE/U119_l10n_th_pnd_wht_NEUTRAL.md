# U119 — Thai PND and Withholding Tax: Neutral Business Knowledge
## Date: 2026-10-02
## Modules researched: l10n_th (l10n_th_pnd and l10n_th_withholding_tax are ABSENT in Community)

---

## 1. What Withholding Tax Means in Thailand

Thai law requires the paying party (the company making a payment) to deduct a percentage of income before paying a vendor or supplier. The deducted amount is held by the payer and remitted monthly to the Revenue Department on behalf of the vendor. The vendor receives a certificate proving that tax was deducted, which can be credited against the vendor's own annual income tax liability.

The Thai Revenue Department assigns different form numbers (called PND, from the Thai abbreviation for income tax form) based on the type of payee:

- PND1: Payroll income withheld from employees
- PND3: Income withheld from individual (natural person) vendors
- PND53: Income withheld from juristic (company) vendors
- PND54: Income withheld on payments sent overseas

The deduction rates vary by income type. Common rates in the Thai chart of accounts are 1% for transport, 2% for advertising, 3% for general services, and 5% for rental income.

---

## 2. What the Community Module Provides

The base Thai accounting module (l10n_th) ships the following withholding tax features:

**Tax templates**: Eight vendor-side withholding tax templates are pre-built covering four rates (1%, 2%, 3%, 5%) for both corporate payees (mapped to PND53) and individual payees (mapped to PND3). Four matching income-side templates record the tax deducted by customers on the company's own income. All twelve templates are standard tax records using the built-in tax system, not a separate withholding tax model.

**PND report definitions**: Two statutory tax reports are registered — one for PND53 and one for PND3. Each report contains lines for Total Income, Total Remittance, Surcharge, and Grand Total. These reports read directly from tax tags applied on the tax templates. The surcharge line is present for completeness but requires a manual entry since no automated penalty calculation is built in.

**Chart of accounts for WHT**: The Thai chart of accounts includes five dedicated withholding tax liability accounts: PND1 (payroll), PND3 (individual vendors), PND53 (corporate vendors), PND54 (overseas), and a WHT Payable consolidation account used for monthly remittance. On the asset side, a WHT Creditable account records tax deducted by customers, and a WHT Receivable account consolidates those credits for year-end corporate income tax offset.

**Invoice presentation**: The Thai invoice template displays the vendor branch name alongside the tax identification number, supporting the Thai requirement that tax invoices identify both the head office and branch code of the supplier.

---

## 3. How Withholding Tax Is Applied in Practice

Because Community does not include a dedicated withholding tax model, the standard purchase tax mechanism is used. When creating a vendor bill for a service subject to withholding, the user selects the appropriate WHT tax (for example, 3% service for a company vendor). The tax line posts a negative amount to the PND53 liability account, effectively reducing the amount to be paid to the vendor. The remaining balance due to the vendor is lower by the withheld amount.

At the end of each month, the business transfers the balance from PND53 (and PND3) accounts to the WHT Payable consolidation account and makes a single remittance to the Revenue Department.

The PND53 and PND3 reports in the Accounting module consolidate all transactions tagged with the relevant income and tax tags across the reporting period, providing a summary that corresponds to the statutory form. The user uses this summary to complete and file the paper or electronic PND form.

---

## 4. What Is Absent from Community

The following features are not present in Community and would require Enterprise modules or custom development:

**Withholding certificate generation**: No printable vendor withholding certificate (the document given to the vendor as proof of tax deduction) is provided. This is a statutory requirement when making payments subject to withholding. Enterprise includes a certificate template; Community does not.

**Automated WHT deduction at payment**: Enterprise includes a flow where the withholding tax amount is automatically computed and deducted when recording a vendor payment, with the WHT line created on the payment itself rather than on the bill. Community requires the WHT tax to be applied manually at bill time.

**Dedicated withholding tax model**: Enterprise uses a separate model for withholding tax records that stores each individual WHT transaction with the payee name, tax identification number, income type, and certificate number. Community uses only the standard journal entry without this structured record.

**PND54 report**: The chart of accounts includes an account for overseas payment withholding (PND54) but no PND54 report definition exists in Community. Overseas payment withholding cannot be reported through the built-in reporting framework without custom configuration.

**PND1 report**: Payroll withholding (PND1) has a dedicated liability account in the chart but no PND1 report definition is present. Payroll withholding reporting would need to come from a payroll module.

**Electronic submission**: No integration with the Revenue Department's electronic filing system is provided in Community.

---

## 5. Implications for SMEsPlus Migration

Any Thai business using SMEsPlus will need WHT certificate printing and ideally automated WHT deduction at payment. These gaps must be addressed through either Enterprise modules, approved OCA modules, or custom development in the migration plan. The PND3 and PND53 report totals are available in Community and can serve as a cross-check against manual filings, but the certificate and automated deduction workflows are a known gap requiring a planned resolution before go-live.
