# MODULE_MASTER_REGISTER

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-28-MIG-A-EXPERT-DR-001 |
| Date | 2026-08-28 |
| Phase | A1 — Source Forensic Inventory |
| Modules counted from evidence | **1,504** (manifest-parsed; zero parse errors; zero duplicate technical names across areas) |
| Machine companion (full row-level register) | `MODULE_MASTER_REGISTER_FULL.csv` — 1,504 rows, SHA-256 `f11b1d74…5e5faac` |
| Provenance | P7 (source observation) + P6 (customer-approved evidence) |
| Fact Status | VERIFIED FACT for counts/licenses/versions; SUPPORTED INFERENCE where marked |

## 1. Count Summary (measured, not estimated)

| Area | Modules | License profile | Role |
|---|---:|---|---|
| `01 ACCOUNT` | 62 | OEEL-1 42 · LGPL-3 20 | Accounting module set carved out of the Odoo 19 addons tree (all `account*`/`accountant*` names) |
| `02 OTHER` | 1,371 | OEEL-1 700 · LGPL-3 667 · OPL-1 4 | Remainder of the same Odoo 19 Enterprise addons tree (community + enterprise merged; incl. repo files README/LICENSE/COPYRIGHT of `odoo/enterprise`) |
| `addons_extra` | 69 | AGPL-3 22 · LGPL-3 21 · OPL-1 11 · UNDECLARED 12 · Other proprietary 2 · GPL-3 1 | Customer customizations + purchased third-party + OCA modules |
| `ks_dashboard_ninja` | 1 | OPL-1 | Ksolves Dashboard Ninja (paid, Chart.js/gridstack-based dashboard builder; 14 new models) |
| `ks_dn_advance` | 1 | OPL-1 | Ksolves Dashboard Ninja Advance (extension pack) |
| **TOTAL** | **1,504** | OEEL-1 744 · LGPL-3 706 · AGPL-3 22 · OPL-1 17 · UNDECLARED 12 · Other-prop. 2 · GPL-3 1 | — |

**Structural fact (VERIFIED):** `01 ACCOUNT` ∩ `02 OTHER` = ∅ (0 overlapping technical names;
modules in `02 OTHER` declare dependencies satisfied only by `01 ACCOUNT`, e.g. `l10n_ae → account`).
The two directories are complementary partitions of ONE Odoo 19.0 Enterprise addons tree.

## 2. Source-System Version Determination

**Odoo 19.0 Enterprise** — confidence HIGH. Evidence:
- `02 OTHER/README.md` badge → runbot repo `git-github-com-odoo-enterprise` (official `odoo/enterprise` repo README).
- `02 OTHER/LICENSE` → "Odoo Enterprise Edition License v1.0" (OEEL-1 declared by 744 modules).
- Odoo-19-only module family present: `ai`, `ai_account`, `ai_fields`, … (15 `ai*` modules), `auth_passkey`, `auth_timeout`, `api_doc`, `html_editor`.
- 8/10 sampled `addons_extra` manifests carry explicit `19.0.x` series prefixes.
- Core manifests are series-neutral by design (`base` 1.3, `web` 1.0, `account` 1.4) — not counter-evidence.
- Exact patch level within 19.0: **UNKNOWN** (no `release.py` in an addons-only bundle) → registered as evidence gap G-05.

## 3. `01 ACCOUNT` — 62 Accounting Modules by Capability Cluster

| Cluster | Modules |
|---|---:|
| Payments & collections | 11 |
| Core invoicing & accounting (`account`, `account_accountant`, …) | 8 |
| Bank statement import & online sync | 6 |
| EDI / Peppol / e-invoicing | 6 |
| Tax engines (Avatax, external tax, python tax) | 6 |
| Reporting & statutory (`account_reports`, SAF-T, intrastat…) | 6 |
| Fleet accounting bridges | 5 |
| AI document digitization / OCR (`account_extract`, invoice extract…) | 4 |
| Cross-app bridges (accountant_hr_expense, accountant_knowledge…) | 3 |
| Data migration / import (winbooks, SAF-T import, base import) | 3 |
| Assets & loans | 2 |
| Budgeting | 2 |

Notes (source facts): 12 of 62 manifests lack a `version` key (Odoo default `1.0` applies);
`account_peppol_advanced_fields` self-declares deprecated in its own manifest.

## 4. `02 OTHER` — 1,371-Module Landscape

| Family | Count | Family | Count |
|---|---:|---|---:|
| l10n (country localization) | 523 | project* | 31 |
| website* | 87 | theme* | 30 |
| pos* | 73 | mrp* | 24 |
| hr* | 67 | payment* | 23 |
| sale* | 58 | stock* | 22 |
| crm* | 10 | ai* | 15 |
| purchase* | 12 | industry* | 8 |
| other | 388 | account* | 0 (all in `01 ACCOUNT`) |

- Localization coverage: ~110 countries; **Thailand vendor-standard = 2 modules only**
  (`l10n_th`, `l10n_th_reports`) — the substantive Thai capability lives in `addons_extra`.
- `auto_install` modules: 680. Applications: 75. `installable: False`: 2 (`iot_box_image`, `iot_drivers`).
- Framework core present: `base` (1.3), `web` (1.0), `mail` (1.19).

## 5. `addons_extra` — 69 Customer/Third-Party Modules (row-level register)

Aggregates: **104 new models** (incl. wizards/report parsers), **171 model extensions**,
18 modules create new persistent tables, 36 extend existing models, 21 are Thai-localization-relevant,
2 define cron automation (`auto_database_backup`, `date_range`).
External integrations found: Monday.com (GraphQL), JasperReports Server (REST), 2C2P payment
gateway, Redis (sessions), Google Drive/Dropbox/OneDrive/Nextcloud/S3/SFTP (backup targets),
GeoNames, Thai Revenue Department VAT service (`rdws.rd.go.th`), OpenRouter LLM API
("DeepSeek" chat), PromptPay offline QR generation.

Business-domain spread: Reporting 10 · Tax-TH 9 · Other 9 · UI-UX 8 · Sales 6 · Product 5 ·
Purchase 4 · Approval 3 · Integration 3 · Inventory 3 · Payment 3 · System-Infra 3 ·
Accounting 1 · HR-Expense 1 · Security 1.

### Row-level table — 69 addons_extra modules

| Module | Version | License | Domain | Purpose | New/Ext models | DB impact | Integration | Cron | TH |
|---|---|---|---|---|---|---|---|---|---|
| `app_icon_hide` | 18.0.1.1.0 | LGPL-3 | UI-UX | Hides the mobile app icon element in the Odoo backend General Settings page using a single custom CSS asset. Pure cosmetic tweak with no business logic. | 0/0 | UI_ONLY | none | N | N |
| `auto_database_backup` | 19.0.1.0.0 | LGPL-3 | System-Infra | Schedules automatic database backups to local disk, remote SFTP, Google Drive, Dropbox, OneDrive, Nextcloud and Amazon S3, with email notification on success/failure. Stores cloud credentials/tokens in a backup-configura | 2/0 | NEW_TABLES | Google Drive, Dropbox, OneDrive (Microsoft Graph), Nextcloud, Amazon S3 (boto3), SFTP (paramiko) | Y | N |
| `base_location` | 19.0.1.0.3 | AGPL-3 | Other | OCA module providing an enhanced city/ZIP master (res.city.zip) so partner, company and employee addresses can be completed from a validated ZIP catalogue. | 1/5 | NEW_TABLES | none | N | Y |
| `base_location_geonames_import` | 19.0.0.0.2 | AGPL-3 | Other | OCA wizard that downloads a country's ZIP/city/state catalogue from download.geonames.org and loads it into the res.city.zip master data. | 1/1 | EXTENDS_EXISTING | GeoNames (HTTP download from download.geonames.org, wizard/geonames_import.py:101) | N | Y |
| `bi_print_journal_entries` | 1.0.0 | UNDECLARED | Reporting | Adds a QWeb PDF report to print journal entries from the accounting module. Report XML only, no Python models. | 0/0 | UI_ONLY | none | N | N |
| `bm_thai_rd_vat_company_search` | 19.0.1.0.0 | OPL-1 | Tax-TH | Looks up company registration data from the Thai Revenue Department VAT web service by tax ID and updates the partner record (name, address, branch/office type). Paid Bizmate module (29 USD). | 0/1 | EXTENDS_EXISTING | Thai Revenue Department VAT SOAP/JSON service (https://rdws.rd.go.th, models/res_partner.py:148) | N | Y |
| `contact_reference_sequence` | 19.0.1.0 | OPL-1 | Other | Automatically assigns the partner reference (ref) from ir.sequence records according to a new contact_group selection (customer/vendor/etc.) on create/write. | 0/1 | EXTENDS_EXISTING | none | N | N |
| `convert_amount_text_to_thai` | 19.0.1.0.0 | AGPL-3 | Reporting | Overrides res.currency amount-to-text so monetary amounts render as Thai baht text (via num2words) on printed documents. Method-only override, no schema change. | 0/1 | EXTENDS_EXISTING | none | N | Y |
| `courier_type` | 19.0.1.0.0 | LGPL-3 | Inventory | Customer-specific customization ('Custom any for SWR') adding courier/job-type master data (type.courier with job codes) and courier fields propagated across sale orders, purchase orders, pickings, lots, quants, move lin | 3/9 | NEW_TABLES | none | N | N |
| `cr_effective_date_entries` | 19.0.0.0 | AGPL-3 | Accounting | Wizard that lets authorized users (own security group) backdate transactions — set an effective date earlier than today on stock/accounting documents. | 1/1 | EXTENDS_EXISTING | none | N | N |
| `date_range` | 19.0.1.2.0 | LGPL-3 | Other | OCA server-ux module providing configurable date-range master data (date.range, date.range.type), a generator wizard and a search mixin used for period filtering by other modules. | 4/0 | NEW_TABLES | none | Y | N |
| `deepseek_r1` | 0.1 | GPL-3 | Integration | Adds an AI chatbot user/channel to Discuss that answers messages via an LLM API key configured in Settings. Despite the DeepSeek branding, the code calls OpenRouter (base_url https://openrouter.ai/api/v1) with model 'ope | 0/2 | CONFIG_ONLY | OpenRouter LLM API via openai python client (models/mail_channel.py:53); marketed as DeepSeek | N | N |
| `dev_print_cheque` | 19.0.1.3 | UNDECLARED | Payment | Configurable bank-cheque printing from vendor payments: per-bank cheque layout settings (positions, fonts) and a print wizard; bundles Thai baht-text helpers (bahttext.py, thainlp.py) for amount-in-words. | 4/1 | NEW_TABLES | none | N | Y |
| `equipment_sequence` | 19.0.1.4 | UNDECLARED | Other | Generates configurable sequence numbers for maintenance equipment and fixed assets via a prefix-configuration model (conf.prefix), wiring sequences into equipment categories, assets and receipts. | 1/5 | NEW_TABLES | none | N | N |
| `full_summarize_bills` | 19.0.0.1 | UNDECLARED | Reporting | Custom summarized vendor-bill/invoice PDF built with an in-house 'Report Designer' pattern: custom paperformat, QWeb body, abstract report parser and Thai baht-text helper (module/bahttext.py). | 1/3 | EXTENDS_EXISTING | none | N | Y |
| `hide_smesplus_menu` | 1.0 | LGPL-3 | UI-UX | JavaScript patch (static/src/js/user_menu_patch.js) that hides items from the backend user menu for internal users. No models or data. | 0/0 | UI_ONLY | none | N | N |
| `import_bridge_axis` | 19.0.0.0 | OPL-1 | Integration | Bulk data import/export bridge: ~2 dozen wizards to load customers, products, sale/purchase orders and lines, invoices, payments, bank statements, chart of accounts, journals/journal entries, BOMs, pricelists, inventory  | 26/3 | NEW_TABLES | none (file-based Excel/CSV import) | N | N |
| `invoice_promptpay` | 19.0.1.0 | UNDECLARED | Payment | Generates a Thai PromptPay QR payment code (from the company's PromptPay phone/ID configured in settings) and embeds it on the customer invoice PDF report. | 0/2 | EXTENDS_EXISTING | PromptPay (offline QR payload generation via python 'promptpay' library — no network API) | N | Y |
| `l10n_th_amount_to_text` | 19.0.1.0.0 | AGPL-3 | Reporting | OCA l10n-thailand module overriding res.currency amount-to-text to produce Thai baht text via num2words for printed documents. | 0/1 | EXTENDS_EXISTING | none | N | Y |
| `l10n_th_base_location` | 19.0.0.0.2 | AGPL-3 | Other | Thai address localization: loads Thai province/district/sub-district/ZIP data (bundled TH_en.txt/TH_th.txt GeoNames extracts) into the city/ZIP master and adapts partner/company address behavior for Thailand. | 0/5 | EXTENDS_EXISTING | GeoNames (bundled TH data files; import wizard extension) | N | Y |
| `l10n_th_partner` | 19.0.1.0.0 | AGPL-3 | Other | Thai partner conventions: Thai person titles and company-type prefix/suffix (e.g. บริษัท ... จำกัด) composed into the partner display name, with seeded res.partner.title and res.partner.company.type data. | 0/4 | EXTENDS_EXISTING | none | N | Y |
| `l10n_th_reports_ext` | 19.0.1.4 | LGPL-3 | Tax-TH | SMEsPlus extension of the standard Thai tax report handler (l10n_th.tax.report.handler): customizes VAT sales/purchase report content such as partner company-type titles and company details. Python-only, no views or data | 0/1 | EXTENDS_EXISTING | none | N | Y |
| `l10n_th_withholding_tax` | 19.0.1.4 | AGPL-3 | Tax-TH | Thai withholding tax (WHT): a WHT master table (account.withholding.tax with PND income-tax-form mapping), WHT deduction during payment registration, WHT fields on products/taxes/accounts/moves, and hooks into the PND re | 1/8 | NEW_TABLES | none | N | Y |
| `l10n_th_withholding_tax_cert` | 19.0.1.5 | AGPL-3 | Tax-TH | Creates and manages Thai withholding tax certificates (WHT cert and cert lines) from payments and journal entries, with a wizard to generate certificates and states tracked via chatter. | 3/3 | NEW_TABLES | none | N | Y |
| `l10n_th_withholding_tax_cert_form` | 19.0.1.0.2 | AGPL-3 | Tax-TH | Provides the printable PDF layout of the Thai withholding tax certificate (official RD form style) with Thai amount-to-text, custom paper format and report SCSS styling. | 1/1 | EXTENDS_EXISTING | none | N | Y |
| `l10n_th_withholding_tax_multi` | 19.0.1.0.2 | AGPL-3 | Tax-TH | Allows applying multiple withholding tax deductions on a single payment by extending the payment register and payment deduction models. | 0/3 | EXTENDS_EXISTING | none | N | Y |
| `l10n_th_withholding_tax_report` | 19.0.1.0.1 | AGPL-3 | Tax-TH | Generates Thai Revenue Department withholding tax return reports (PND1/PND3/PND53) from WHT certificates via a wizard, output as QWeb PDF (XLSX renderer present but its import is commented out). | 2/2 | EXTENDS_EXISTING | none | N | Y |
| `monday_smesplus_connector` | 19.0.1.0.0 | AGPL-3 | Integration | Connects Odoo to a Monday.com account and imports Users, Boards, Groups, Items and column values into local mirror models, mapping Monday users/customers to res.users/res.partner. | 6/2 | NEW_TABLES | Monday.com (GraphQL API v2 via requests.post to https://api.monday.com/v2) | N | N |
| `multi_level_approval` | 19.0.0.1 | OPL-1 | Approval | Generic multi-level approval engine: users create approval requests of configurable types that are reviewed and approved sequentially by multiple manager levels, with refusal-reason wizard and chatter tracking. | 5/0 | NEW_TABLES | none | N | N |
| `multi_level_approval_configuration` | 19.0.1.0 | OPL-1 | Approval | Extends the approval engine so approval flows can be attached to arbitrary models (Sale Order, Purchase Order, Purchase Request, etc.) and centralizes all requests, adding cancel/change-approver/rework/request wizards. | 4/7 | EXTENDS_EXISTING | none | N | N |
| `multi_level_approval_hr` | 19.0.1.0 | OPL-1 | Approval | Lets approval levels use HR-derived dynamic approvers such as the employee's line manager, coach, or department manager instead of fixed users. | 0/1 | EXTENDS_EXISTING | none | N | N |
| `nthub_binary_field_preview` | 19.0.1.0 | LGPL-3 | UI-UX | Adds a client-side widget (nt_binary_preview) to preview binary fields (PDF, image, text) directly in form/list views without downloading. | 0/0 | UI_ONLY | none | N | N |
| `oi_action_file` | 19.0.1.1.1 | OPL-1 | UI-UX | Utility providing a client action to download a file (via ir.attachment helper and a backend JS handler); used as a base by other Openinside modules. | 0/1 | UI_ONLY | none | N | N |
| `oi_jasper_report` | 19.0.1.0.0 | OPL-1 | Reporting | Executes reports hosted on an external JasperReports Server from Odoo: report definitions are stored locally (jasper.report) and run via a wizard that calls the Jasper REST API and returns the file for view/download/emai | 2/2 | NEW_TABLES | JasperReports Server (REST via requests.get with basic auth; URL/user/password in ir.config_parameter jasper_report.*) | N | N |
| `oi_pdf_viewer` | 19.0.1.1.5 | OPL-1 | UI-UX | Displays PDF files/reports on screen in the backend instead of forcing a download, via a JS pdf_viewer component and a helper on the abstract base model. | 0/1 | UI_ONLY | none | N | N |
| `om_data_remove` | 19.0.1.1 | LGPL-3 | System-Infra | Adds settings-screen buttons to wipe transactional data (sales, products, accounting, etc.) by executing raw SQL DELETE on whole tables and resetting related ir.sequence counters - a database reset/cleanup tool. | 0/1 | CONFIG_ONLY | none | N | N |
| `order_line_sequence` | 19.0.1.0.1 | AGPL-3 | Sales | Adds a visible line-number sequence to sale order, purchase order, invoice and stock move lines, in both backend views and the printed SO/PO/invoice/picking reports. | 0/4 | EXTENDS_EXISTING | none | N | N |
| `partner_company_type` | 19.0.1.0.0 | AGPL-3 | Other | Adds a configurable legal form / company type (e.g. Co., Ltd., PLC) to company partners, plus a locally re-created partner Title model with abbreviation. | 2/1 | NEW_TABLES | none | N | N |
| `partner_firstname` | 19.0.1.0.0 | AGPL-3 | Other | Splits partner names into separate first name and last name fields for individuals, with configurable name order and a post-init hook that back-fills existing partner records. | 0/3 | EXTENDS_EXISTING | none | N | N |
| `payment_2c2p` | 19.0.0.0 | Other proprietary | Payment | Website payment provider integration for the 2C2P gateway: customers checking out on the Odoo eCommerce site are redirected to 2C2P's hosted payment page, with a controller handling the return/callback and transaction st | 0/3 | EXTENDS_EXISTING | 2C2P payment gateway (redirect to https://t.2c2p.com/RedirectV3/Payment, demo https://demo2.2c2p.com/2C2PFrontEnd/RedirectV3/payment) | N | Y |
| `print_payment_remittance_adviec` | 19.0.1.1 | UNDECLARED | Reporting | Custom QWeb PDF 'Payment Remittance' report bound to payments (account.payment), with Thai baht amount-in-words (bahttext) support and a Report Designer flag on report actions. | 1/2 | EXTENDS_EXISTING | none | N | Y |
| `print_voucher_request` | 19.0.1.0 | UNDECLARED | Reporting | Custom QWeb PDF 'Voucher Request' report bound to journal entries/invoices (account.move) with Thai baht amount-in-words (bahttext) and Report Designer flag. | 1/2 | EXTENDS_EXISTING | none | N | Y |
| `product_brand_sale` | 19.0.1.0.1 | AGPL-3 | Sales | Brand management across sales and eCommerce: brands on products/customers/salespeople, brand filtering in sale orders and the web shop, brand dimension in sale analysis, plus optional split of deliveries and invoices per | 3/14 | NEW_TABLES | none | N | N |
| `product_category_filter` | 19.0.1.0.0 | AGPL-3 | Product | Adds a 'Show Category' flag on product categories and restricts the category dropdown on product templates to flagged categories only. | 0/2 | EXTENDS_EXISTING | none | N | N |
| `product_sequence` | 19.0.1.0 | LGPL-3 | Product | Auto-generates product internal references from per-category ir.sequence records with hierarchical prefixes (parent category prefix + own prefix), managing sequence lifecycle with the category. | 0/2 | EXTENDS_EXISTING | none | N | N |
| `product_stock_equipment` | 19.0.1.0 | UNDECLARED | Inventory | Automatically creates maintenance equipment records (with serial numbers) when inventory receipts/adjustments are validated for products flagged as equipment, linking stock moves to the maintenance module. | 0/5 | EXTENDS_EXISTING | none | N | N |
| `product_variant_reference` | 19.0.0.0 | OPL-1 | Product | Automatically generates each product variant's internal reference (default_code) from its attribute values such as brand, color and size, in attribute-sequence order. | 0/2 | EXTENDS_EXISTING | none | N | N |
| `purchase_discount_catalog` | 1.1 | OPL-1 | Purchase | Adds a discount wizard on purchase orders (mirroring Odoo's sale discount wizard) that inserts a discount line using a company-configured default discount product. | 1/2 | EXTENDS_EXISTING | none | N | N |
| `purchase_order_lines_discount` | 19.0.0.0 | AGPL-3 | Purchase | Adds fixed-amount and percentage discount fields on purchase order lines with two-way auto-calculation between the two, feeding into line amount computation. | 0/1 | EXTENDS_EXISTING | none | N | N |
| `purchase_request` | 19.0.1.0 | LGPL-3 | Purchase | Internal purchase-requisition workflow: employees raise requests for materials or services, which are tracked, approved/rejected, allocated against stock moves, and converted into RFQs/purchase orders via a wizard. | 6/10 | NEW_TABLES | none | N | N |
| `report_xlsx` | 19.0.1.0.1 | AGPL-3 | Reporting | Reporting engine that lets other modules define XLSX-type reports; provides the abstract report generator, ir.actions.report extension and the HTTP download controller. | 2/1 | EXTENDS_EXISTING | none | N | N |
| `report_xlsx_helper` | 19.0.1.0.0 | AGPL-3 | Reporting | Helper layer on top of report_xlsx providing formatting utilities and an abstract template-driven API to simplify building XLSX reports. | 1/2 | CONFIG_ONLY | none | N | N |
| `sale_gross_profit_record` | 19.0.1.1 | LGPL-3 | Sales | Records and displays gross-profit figures (margin, %margin, %GP, average price/qty, discount) per sale order line, with gross and net variants shown on the sale order. | 0/2 | EXTENDS_EXISTING | none | N | N |
| `sale_order_line_price_history` | 19.0.1.1.4 | AGPL-3 | Sales | Lets salespeople open a wizard from a sale order line showing the price history of that product for the customer, with configurable record limit. | 2/1 | UI_ONLY | none | N | N |
| `sale_productinfo_ext` | 19.0.1 | UNDECLARED | Product | Adds customer-specific product information (customer's product name/code per partner, mirroring the vendor supplierinfo pattern) maintained on products and used from sale orders. | 1/3 | NEW_TABLES | none | N | N |
| `smesplus_account_reports` | 19.0.1.4 | LGPL-3 | Tax-TH | Defines Thai-style Sale VAT and Purchase VAT reports (including zero-rated variants) with columns for Tax Period Date, Tax ID, Branch, tax base and tax amount, built on the Odoo Enterprise account_reports custom-handler  | 4/1 | EXTENDS_EXISTING | none | N | Y |
| `smesplus_advance_expense_request` | 19.0.1.0.0 | LGPL-3 | HR-Expense | Employee cash-advance workflow: staff request advances, the request is approved/rejected, posted to accounting, and later cleared/reconciled against expenses through dedicated wizards. | 5/4 | NEW_TABLES | none | N | N |
| `smesplus_custom_title_and_favicon` | 19.0.0.0.2 | LGPL-3 | UI-UX | Lets each company set a custom browser window title and favicon for the backend, replacing default Odoo branding. | 0/3 | EXTENDS_EXISTING | none | N | N |
| `smesplus_inventory_lot_filter` | 19.0.1.1 | LGPL-3 | Inventory | Filters lot/serial selection in stock move operations and scrap so users only see lots with on-hand quantity in the relevant source location. | 0/2 | UI_ONLY | none | N | N |
| `smesplus_product_image` | 19.0.1.0 | UNDECLARED | UI-UX | Shows the product image as a column in sale order lines, purchase order lines, stock moves and invoice/journal lines. | 0/4 | UI_ONLY | none | N | N |
| `smesplus_purchase_advance_payment` | 1.0.0 | LGPL-3 | Purchase | Adds a down-payment/advance-payment flow to purchase orders, mirroring the sale advance payment wizard: creates advance vendor bills using a configurable deposit product and expense account. | 1/2 | EXTENDS_EXISTING | none | N | N |
| `smesplus_so_section_bydivision` | 18.0.1.0.1 | LGPL-3 | Sales | Automatically groups sale order lines into sections by product division/brand (stored computed brand_id on lines) and adapts the website shop cart to that grouping. | 0/2 | EXTENDS_EXISTING | none | N | N |
| `smesplus_sol_global_discount` | 19.0.1.0.0 | LGPL-3 | Sales | Improves global discounting on sale orders: adds a discount type (per-line percent, global discount, fixed amount) and global percent on sale order lines, extending the standard sale.order.discount wizard. | 0/3 | EXTENDS_EXISTING | none | N | N |
| `smesplus_special_access_rights` | 19.0.1.0 | UNDECLARED | Security | Per-user dynamic access rights layered on top of standard ACLs: administrators map modules to models and grant/deny read/write/create/delete per user, plus control menu visibility per user. | 4/2 | NEW_TABLES | none | N | N |
| `smesplus_tax_period_date` | 19.0.0.1 | LGPL-3 | Tax-TH | Adds a Tax Period Date on journal entries which is propagated to tax lines (account.move.line), allowing VAT to be reported in a tax period different from the accounting date, as required for Thai VAT filing. | 0/2 | EXTENDS_EXISTING | none | N | Y |
| `smesplus_uom_ext` | 19.0.1.0 | UNDECLARED | Product | Utility extension of units of measure: helper methods to walk the UoM hierarchy (lower/upper/same-group UoMs via relative_uom_id) and a computed UoM filter on vendor pricelists. | 0/2 | UI_ONLY | none | N | N |
| `tracking_history` | 19.0.1.1 | LGPL-3 | Reporting | User activity audit report built from chatter log notes: a wizard filters mail messages by date range, user and module and presents them through a SQL-view report model. | 2/1 | EXTENDS_EXISTING | none | N | N |
| `web_window_title` | 19.0.0.0.1 | LGPL-3 | UI-UX | Lets administrators set a custom browser window title for the Odoo backend via a general settings option. | 0/2 | CONFIG_ONLY | none | N | N |
| `wk_redis_session` | 19.0.1.0 | Other proprietary | System-Infra | Replaces Odoo's filesystem session storage with Redis so HTTP sessions are shared and expired centrally, configured through general settings. | 0/1 | CONFIG_ONLY | Redis | N | N |

## 6. Notable Source-Fact Observations from `addons_extra` (forensic notes)

Quality / structure (SOURCE OBSERVATION — no target-design implication):
- **Duplicate module pair:** `convert_amount_text_to_thai` and `l10n_th_amount_to_text` are the
  same OCA module under two technical names (models byte-identical); both override `res.currency`.
- **Model-name collision:** `print_payment_remittance_adviec` declares
  `_name='report.print_voucher_request.report_invoice_custom_view'` — identical to the parser in
  `print_voucher_request`.
- **Dead/stray files:** `l10n_th_withholding_tax_report` ships `report_withholding_tax copy.py`,
  `.py_bkp` and `_xlsx_backup.py` variants (duplicate `_name='withholding.tax.report'`).
- **Empty/anomalous modules:** `nthub_binary_field_preview` ships no active Python models;
  `hide_smesplus_menu` has no `__init__.py` (loadability UNKNOWN).
- **Missing dependency in tree:** `l10n_th_withholding_tax_multi` depends on
  `account_payment_multi_deduction` — NOT present anywhere in the source tree (gap G-06).
- **Overlapping functionality:** `web_window_title` vs `smesplus_custom_title_and_favicon`
  (both define the same `res.config.settings` field and window-title JS).
- **Locally forked OCA modules:** `purchase_request` (ForgeFlow, fork adds deps on
  `smesplus_uom_ext`, `hr`, `project`), `sale_order_line_price_history`,
  `l10n_th_withholding_tax` (version restyled `19.0.1.4`, added `l10n_th_reports` dependency).
- **Enterprise coupling in customs:** `smesplus_account_reports → account_reports` (OEEL-1),
  `smesplus_advance_expense_request → account_asset` (OEEL-1),
  `l10n_th_reports_ext`/`l10n_th_withholding_tax → l10n_th_reports` (OEEL-1).

Security-relevant source facts (recorded for migration risk awareness, Class F):
- `bm_thai_rd_vat_company_search` calls the Thai RD VAT service with TLS verification disabled
  (`verify=False`, `models/res_partner.py:148`).
- `monday_smesplus_connector` stores its Monday.com API token in a plain Char field.
- `oi_jasper_report` stores Jasper credentials in `ir.config_parameter` and sends HTTP basic auth.
- `smesplus_special_access_rights` overrides `base._check_access` for ALL models.
- `deepseek_r1` performs a runtime `pip install openai` at module import.

## 7. Register Columns (per directive §16)

The full per-module register with all §16 columns lives in the machine companion
`MODULE_MASTER_REGISTER_FULL.csv` (area, technical_name, manifest name, version, license,
category, author, website, installable, application, auto_install, depends_count, depends,
summary, parse_error). Business-domain, DB-impact, and migration-relevance enrichment for the
69 customer modules is in §5's table above; enrichment for the 1,433 vendor modules is
deliberately deferred to domain-phase research (they are vendor-standard; their migration
relevance is governed by the approved 134-module scope — see SOURCE_BASELINE_RECONCILIATION.md).

## 8. Research Status per Area

| Area | Inventory | Deep research status |
|---|---|---|
| `01 ACCOUNT` (62) | COMPLETE (this session) | Clustered; domain-phase research pending (A4) |
| `02 OTHER` (1,371) | COMPLETE (this session) | Landscape-profiled; in-scope subset governed by approved 134-module scope |
| `addons_extra` (69) | COMPLETE (this session) | Forensic row-level pass done (manifest+models+integration); function-level research pending (A4) |
| `ks_*` (2) | COMPLETE (this session) | Forensic pass done |
