# A2 — Benchmark Installed Accounting Modules — iTEST02 Instance (Metadata Only)

| Field | Value |
|---|---|
| Session | `SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001` |
| Jira | `ERPPLUS-138` |
| Project / STATE | `SMEsPlus ENTERPRISE SUITE` / `STATE03 - Architecture` |
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical Branch | `SMEsPlus` (base commit `788479552971940a126a542da5343944f7f3e0d4`, 2026-09-02 08:47 +0700) |
| Execution Branch | `audit/account-menu-process-deep-study-2026-09-02-001` (isolated worktree `ACCOUNT_MENU_PROCESS_DEEP_STUDY_2026_09_02_EXECUTION`) |
| Executor | Claude (this session), on behalf of Boss; Boss = Sole Final Approver |
| Mode | `READ ONLY / PROCESS BENCHMARK / CLEAN-ROOM / EVIDENCE-FIRST / MENU-BY-MENU / CHECKPOINT-CONTROLLED / L999.999` |
| Document status | `PROCESS REFERENCE ONLY` — not a Gate PASS, not a Final Solution, not development/production authorization, not an approved SMEsPlus UI/schema/workflow |
| Clean-room rule | Open ERP / Odoo and the iTEST02 dump are used only as `PROCESS BENCHMARK / MENU COVERAGE CHECKLIST / BUSINESS CAPABILITY REFERENCE / RISK DISCOVERY SOURCE`. No source code, ORM, schema, workflow-as-architecture, or menu name is adopted as final SMEsPlus design. Thai names below are **candidates only**. |
| Purpose of this file | Evidence appendix: accounting-related modules recorded as `installed` in the benchmark instance (`ir_module_module` metadata: technical name, version, licence, display name). Used to classify which Boss-listed menus were actually available in the benchmark and to attribute menus to licence classes for clean-room control. |

`No Evidence = No Progress.` `Never Skip Gate.` `Boss is the sole Final Approver.` `Open ERP / Odoo = Process Benchmark Only.` `SMEsPlus = New Thai Business Process Design Candidate, not final solution.`

## A. Facts

- Installed modules in instance: 486 (all applications). Accounting-related subset below: 59.
- Licence classes observed in subset: LGPL-3 (community, readable), OEEL-1 (Odoo Enterprise — **black-box / metadata-only** under Team A quarantine Q-01..Q-05), AGPL-3 (OCA/Ecosoft Thai localization — readable for understanding, implementation reuse prohibited), OPL-1 (purchased, separately classified), CLASS-D (third-party/undeclared, quarantined: `dev_print_cheque`, `invoice_promptpay`, `print_voucher_request`).

| Technical name | Version | Licence | Display name (en / th as installed) | Author |
|---|---|---|---|---|
| `account` | 19.0.1.4 | LGPL-3 | {"en_US": "Invoicing", "th_TH": "ใบแจ้งหนี้"} | Odoo S.A. |
| `account_3way_match` | 19.0.1.0 | OEEL-1 | {"en_US": "Vendor Bill: Release to Pay", "th_TH": "บิลค่าใช้จ่าย"} | UNKNOWN / EVIDENCE REQUIRED |
| `account_accountant` | 19.0.1.1 | OEEL-1 | {"en_US": "Invoicing", "th_TH": "ใบแจ้งหนี้"} | Odoo S.A. |
| `account_accountant_fleet` | 19.0.1.0 | OEEL-1 | {"en_US": "Accounting/Fleet bridge", "th_TH": "การเชื่อมต่อระหว่าง ระบบบัญชี/การขนส่ง"} | Odoo S.A. |
| `account_add_gln` | 19.0.1.0 | LGPL-3 | {"en_US": "Add Partner GLN"} | Odoo S.A. |
| `account_asset` | 19.0.1.0 | OEEL-1 | {"en_US": "Assets Management", "th_TH": "การจัดการสินทรัพย์"} | Odoo S.A. |
| `account_asset_fleet` | 19.0.1.0 | OEEL-1 | {"en_US": "Assets/Fleet bridge", "th_TH": "การเชื่อมต่อระหว่าง สินทรัพย์/ขนส่ง"} | Odoo S.A. |
| `account_bank_statement_import` | 19.0.1.0 | OEEL-1 | {"en_US": "Account Bank Statement Import", "th_TH": "รายการเดินบัญชีธนาคาร"} | Odoo S.A. |
| `account_bank_statement_import_camt` | 19.0.1.0 | OEEL-1 | {"en_US": "Import CAMT Bank Statement", "th_TH": "รายการเดินบัญชีธนาคาร"} | Odoo S.A. |
| `account_bank_statement_import_csv` | 19.0.1.0 | OEEL-1 | {"en_US": "Import CSV Bank Statement", "th_TH": "รายการเดินบัญชีธนาคาร"} | Odoo S.A. |
| `account_bank_statement_import_ofx` | 19.0.1.0 | OEEL-1 | {"en_US": "Import OFX Bank Statement", "th_TH": "รายการเดินบัญชีธนาคาร"} | Odoo S.A. |
| `account_base_import` | 19.0.1.0 | OEEL-1 | {"en_US": "Accounting Import", "th_TH": "การนำเข้าบัญชี"} | Odoo S.A. |
| `account_discount_catalog` | 19.0.1.1 | OPL-1 | {"en_US": "Account ( Invoice & Bill ) - Discount Wizard Catalog"} | MPP, SCGLegacy(Thailand) Co.,Ltd |
| `account_edi_ubl_cii` | 19.0.1.0 | LGPL-3 | {"en_US": "Import/Export electronic invoices with UBL/CII", "th_TH": "นำเข้า/ส่งออกใบแจ้งหนี้อิเล็กทรอนิกส์ด้วย UBL/CII"} | Odoo S.A. |
| `account_fiscal_categories` | 19.0.1.0 | OEEL-1 | {"en_US": "Account Fiscal Report"} | Odoo S.A. |
| `account_fiscal_categories_fleet` | 19.0.1.0 | OEEL-1 | {"en_US": "Fiscal Categories on Fleets"} | Odoo S.A. |
| `account_fleet` | 19.0.1.0 | LGPL-3 | {"en_US": "Accounting/Fleet bridge", "th_TH": "การเชื่อมต่อระหว่าง ระบบบัญชี/การขนส่ง"} | Odoo S.A. |
| `account_followup` | 19.0.1.1 | OEEL-1 | {"en_US": "Payment Follow-up Management", "th_TH": "การจัดการติดตามผลการชำระเงิน"} | Odoo S.A. |
| `account_inter_company_rules` | 19.0.1.1 | OEEL-1 | {"en_US": "Inter Company Module for Sale/Purchase Orders and Invoices", "th_TH": "โมดูลระหว่างบริษัทสำหรับการขาย/ใบสั่งซื้อและใบแจ้งหนี้"} | Odoo S.A. |
| `account_intrastat` | 19.0.1.1 | OEEL-1 | {"en_US": "Intrastat Reports", "th_TH": "รายงานอินทราสแทต"} | Odoo S.A. |
| `account_loans` | 19.0.1.0 | OEEL-1 | {"en_US": "Loans Management", "th_TH": "การจัดการสินเชื่อ"} | Odoo S.A. |
| `account_online_synchronization` | 19.0.1.0 | OEEL-1 | {"en_US": "Online Bank Statement Synchronization", "th_TH": "การซิงโครไนซ์ใบแจ้งยอดธนาคารออนไลน์"} | Odoo S.A. |
| `account_payment` | 19.0.2.0 | LGPL-3 | {"en_US": "Payment - Account", "th_TH": "บัญชี"} | Odoo S.A. |
| `account_payment_multi_deduction` | 19.0.1.0.2 | AGPL-3 | {"en_US": "Payment Register with Multiple Deduction"} | Ecosoft, Odoo Community Association (OCA) |
| `account_qr_code_emv` | 19.0.1.0 | LGPL-3 | {"en_US": "account_qr_code_emv", "th_TH": "account_qr_code_emv"} | Odoo SA |
| `account_qr_code_sepa` | 19.0.0.1 | LGPL-3 | {"en_US": "Account SEPA QR Code", "th_TH": "บัญชีรหัส QR โค้ด SEPA"} | Odoo S.A. |
| `account_reports` | 19.0.1.0 | OEEL-1 | {"en_US": "Accounting Reports", "th_TH": "รายงานทางบัญชี"} | Odoo S.A. |
| `accountant` | 19.0.1.1 | OEEL-1 | {"en_US": "Accounting", "th_TH": "ระบบบัญชี"} | Odoo S.A. |
| `accountant_fleet` | 19.0.1.0 | OEEL-1 | {"en_US": "Accounting - Fleet"} | Odoo S.A. |
| `accountant_hr_expense` | 19.0.1.0 | OEEL-1 | {"en_US": "Accounting - Expense"} | Odoo S.A. |
| `analytic` | 19.0.1.2 | LGPL-3 | {"en_US": "Analytic Accounting", "th_TH": "บัญชีวิเคราะห์"} | Odoo S.A. |
| `analytic_enterprise` | 19.0.0.1 | OEEL-1 | {"en_US": "Analytic Accounting Enterprise", "th_TH": "บริษัทวิเคราะห์บัญชี"} | Odoo S.A. |
| `dev_print_cheque` | 19.0.1.3 | LGPL-3 | {"en_US": "Dynamic Print Cheque - Check writing"} | DevIntelle Consulting Service Pvt.Ltd |
| `hr_expense` | 19.0.2.1 | LGPL-3 | {"en_US": "Expenses", "th_TH": "บัญชีรายจ่าย"} | Odoo S.A. |
| `invoice_promptpay` | 19.0.1.0 | LGPL-3 | {"en_US": "PromptPay Invoice Report"} | SCGL |
| `l10n_th` | 19.0.2.0 | LGPL-3 | {"en_US": "Thailand - Accounting", "th_TH": "ประเทศไทย - ระบบบัญชี"} | Almacom (http://almacom.co.th/) |
| `l10n_th_amount_to_text` | 19.0.1.0.0 | AGPL-3 | {"en_US": "Thai Localization - Convert Amount Text to Thai"} | Ecosoft, Odoo Community Association (OCA) |
| `l10n_th_base_location` | 19.0.0.0.2 | AGPL-3 | {"en_US": "Thai Localization - Base Location"} | Ecosoft, Odoo Community Association (OCA) |
| `l10n_th_partner` | 19.0.1.0.1 | AGPL-3 | {"en_US": "Thai Localization - Partner"} | Ecosoft, Odoo Community Association (OCA) |
| `l10n_th_reports` | 19.0.1.0 | OEEL-1 | {"en_US": "Thailand - Accounting Reports", "th_TH": "ประเทศไทย - รายงานการบัญชี"} | Odoo PS |
| `l10n_th_reports_ext` | 19.0.1.4 | LGPL-3 | {"en_US": "Thailand - Localization Accounting Reports"} | SCG Legacy |
| `l10n_th_withholding_tax` | 19.0.1.4 | AGPL-3 | {"en_US": "Thai Localization - Withholding Tax"} | Ecosoft, Odoo Community Association (OCA) |
| `l10n_th_withholding_tax_cert` | 19.0.1.4 | AGPL-3 | {"en_US": "Thai Localization - Withholding Tax Certificate"} | Ecosoft, Odoo Community Association (OCA),SCG LEGACY |
| `l10n_th_withholding_tax_cert_form` | 19.0.1.0.2 | AGPL-3 | {"en_US": "Thai Localization - Withholding Tax Certificate Form"} | Ecosoft, Odoo Community Association (OCA), SCG LEGACY |
| `l10n_th_withholding_tax_report` | 19.0.1.0.1 | AGPL-3 | {"en_US": "Thailand Localization - Withholding Tax Report"} | Ecosoft, Odoo Community Association (OCA) |
| `mrp_account` | 19.0.1.0 | LGPL-3 | {"en_US": "Accounting - MRP", "th_TH": "ระบบบัญชี - MRP"} | Odoo S.A. |
| `mrp_account_enterprise` | 19.0.1.0 | OEEL-1 | {"en_US": "Accounting - MRP", "th_TH": "ระบบบัญชี - MRP"} | Odoo S.A. |
| `mrp_accountant` | 19.0.1.0 | OEEL-1 | {"en_US": "Mrp Accounting", "th_TH": "Mrp ระบบบัญชี"} | Odoo S.A. |
| `payment` | 19.0.2.0 | LGPL-3 | {"en_US": "Payment Engine", "th_TH": "เครื่องมือการชำระเงิน"} | Odoo S.A. |
| `payment_custom` | 19.0.2.0 | LGPL-3 | {"en_US": "Payment Provider: Custom Payment Modes", "th_TH": "ผู้ให้บริการชำระเงิน: โหมดการชำระเงินแบบกำหนดเอง"} | Odoo S.A. |
| `print_voucher_request` | 19.0.1.0 | LGPL-3 | {"en_US": "Voucher Request"} | SCG LEGACY(THAILAND) CO.,LTD(HEAD OFFICE) |
| `purchase` | 19.0.1.2 | LGPL-3 | {"en_US": "Purchase", "th_TH": "การจัดซื้อ"} | Odoo S.A. |
| `purchase_stock` | 19.0.1.2 | LGPL-3 | {"en_US": "Purchase Stock", "th_TH": "การซื้อ"} | Odoo S.A. |
| `sale` | 19.0.1.2 | LGPL-3 | {"en_US": "Sales", "th_TH": "การขาย"} | Odoo S.A. |
| `sale_stock` | 19.0.1.0 | LGPL-3 | {"en_US": "Sales and Warehouse Management", "th_TH": "การขายและการจัดการคลังสินค้า"} | Odoo S.A. |
| `sale_stock_product_expiry` | 19.0.0.1 | LGPL-3 | {"en_US": "Sale Stock Product Expiry"} | Odoo S.A. |
| `stock` | 19.0.1.1 | LGPL-3 | {"en_US": "Inventory", "th_TH": "สินค้าคงคลัง"} | Odoo S.A. |
| `stock_account` | 19.0.1.1 | LGPL-3 | {"en_US": "WMS Accounting", "th_TH": "ระบบบัญชี WMS"} | Odoo S.A. |
| `stock_accountant` | 19.0.1.0 | OEEL-1 | {"en_US": "Stock Accounting", "th_TH": "ระบบบัญชีของสต็อก"} | Odoo S.A. |

## B. Material findings (facts for file 02 / file 10)

1. `l10n_th_withholding_tax_multi` is **NOT installed** in iTEST02, while its OCA dependency `account_payment_multi_deduction` (19.0.1.0.2, AGPL-3) **is installed**. This is new evidence for Boss decision item `ACC-WHT-06` (multi-rate WHT HIGH gap): the reference deployment observed here ran the base WHT module without the multi module. It does not by itself decide the intended SMEsPlus module baseline — Boss decision still required.
2. `account_budget`, `account_debit_note`, `account_batch_payment`, `account_check_printing`, `account_reports_cash_basis`, `account_saft` are **not installed**; Boss-listed Budgets / Budgetary Positions / Budget Analysis / Debit Note menus therefore come from screenshots of a different configuration or version, not from this instance.
3. Thai localization stack installed: `l10n_th` (LGPL-3, chart + taxes + PP30/PND report lines), `l10n_th_reports` (OEEL-1), `l10n_th_reports_ext` (LGPL-3, SMEsPlus-authored VAT report hook), `l10n_th_withholding_tax` / `_cert` / `_cert_form` / `_report` (AGPL-3), `l10n_th_partner`, `l10n_th_amount_to_text`, `l10n_th_base_location` (AGPL-3).
4. Stock-accounting bridge installed: `stock_account` (LGPL-3), `stock_accountant` (OEEL-1), `mrp_account` (+enterprise), `purchase_stock`, `sale_stock` — the Account x Inventory boundary is live in the benchmark instance.
5. `hr_expense` + `accountant_hr_expense` installed — Employee Expenses appear under Vendors in the accounting menu; this is an Expense -> Accounting handoff not in Boss Section 6 list (flagged in file 04).
