# U24 — thailand_localization — Restricted Technical Evidence

> **RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION**
> Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**
> Unit: U24 `thailand_localization` · Source revision: `19.0.post20260921` (Odoo 19 Community only) · Date: 2026-10-02
> Modules studied: `l10n_th` (every file), `account_qr_code_emv` (Thai-relevant parts), `base_vat` (Thai TIN path), `base_address_extended` (street/address relevance), `l10n_account_withholding_tax` (as optional mechanism for the Thai tax set), `account_debit_note`, and Thai-relevant settings of `account`. Adjacent generic files read as needed: `account` (tax engine batching, company settings, partner, move sequence, chart loader, ir_module, report templates, journals), `base` (ir_module country gate, res_partner, res_currency, res.lang, report action), `payment` data (PromptPay method), `web` company header.
> Read-only on source; DB queried for configuration/structure only (counts, flags, names of seeded configuration, ACL/rule/cron rows). No Odoo started, no L5/AWT claim. Items needing execution are flagged `RT`.
> Scope rules applied: accounting localization scope = Thailand; multi-currency, foreign customers/vendors and international transactions are IN scope for the Thai touchpoints (deep mechanics in U25/U26); non-Thai `l10n_*` modules are classed **FUTURE OPTIONAL COUNTRY PACK** and described only by manifest, dependency, extension boundary and installation state. Nothing from `Extra_Thailand`, `Extra_Module_scgl` or any proprietary code was opened or used. Thai UI strings are noted as translatable-text observations over English source keys (English is canonical), never as requirements; no Thai legal requirement is asserted — anything legal is `UNKNOWN`.
> No V-level, completeness, coverage %, gate or approval is asserted. Claim IDs `VDR-U24-C###`; neutral IDs `N-U24-###` (see `02_NEUTRAL_KNOWLEDGE/U24_thailand_localization_NEUTRAL.md`).
> Prior work reused, not redone: U13 (CAP-U13-01..05 and CAP-U13-08), U23 (CAP-U23-01 withholding on payment, CAP-U23-02 debit note, CAP-U23-03 partner tax-number validation, formula tax), U11/U12 entry lifecycle and payments, C02 notes. This unit adds the Thai end-to-end application and DELTA findings listed in section 13.

## 0. Scope, method and Function-ID mapping

| Capability | Function-ID | Note |
|---|---|---|
| CAP-U24-01 Thai chart of accounts structure and loading | MCT-F03 on claims about per-company chart ownership; otherwise FUNCTION MAPPING REQUIRED | MCT-F03 is "Shared vs. per-company Chart of Accounts"; used only where a claim states company-dependent account codes or per-company loading |
| CAP-U24-02 Thai VAT | MCT-F03 on the fiscal-position resolution claim only; otherwise FUNCTION MAPPING REQUIRED | no index entry for tax computation or tax reports |
| CAP-U24-03 Withholding tax in the Thai tax set | FUNCTION MAPPING REQUIRED | no index entry for withholding |
| CAP-U24-04 Tax invoice, receipt, credit and debit note documents | FUNCTION MAPPING REQUIRED | SDV-F07 (return after invoicing via credit note) does not match document layout |
| CAP-U24-05 Thai partner identity and address | FUNCTION MAPPING REQUIRED | |
| CAP-U24-06 Payments, PromptPay/EMV QR and bank/journal setup | FUNCTION MAPPING REQUIRED | payment registration is U12 |
| CAP-U24-07 Period, lock and fiscal-year behaviour | PCO-F01 (lock dates) and PCO-F02 (fiscal year/period configuration) on matching claims | fields/defaults only; posting engine is U11 |
| CAP-U24-08 Thai statutory-output gaps | PCO-F02 on the periodicity gap only; otherwise FUNCTION MAPPING REQUIRED | negative-search claims |
| CAP-U24-09 Country-pack boundary and cross-border touchpoints | FUNCTION MAPPING REQUIRED | |

Method: full read of every non-i18n file of `l10n_th` (manifest, `__init__`, 5 model files, 4 template CSVs, tax-report XML 355 lines, invoice report XML, demo company XML, EMV test), of `account_qr_code_emv` (models, const, view), `base_vat` (Thai path, `_run_vat_checks`, `_check_vat_number`, `_split_vat`, `_format_vat_number`, tests for TH, manifest, cron), `base_address_extended` (models, manifest, ACL), `account_debit_note` (models, wizard, report view, manifest), `l10n_account_withholding_tax` (manifest, tax model, withholding line entry builder, ACL). Targeted reads in `account` and `base` for each cross-reference. A mechanical script produced the CAP-U24-09 table from manifests plus `00_CONTROL/COUNTRY_PACK_BOUNDARY_PROFILE_227.tsv`. See section 14 for what was not read.

Thai-relevant tax set traced exactly (18 taxes, DB = source): 6 VAT (output 7%, input 7%, output 0%, input 0%, output 0% EXEMPT, input 0% EXEMPT), 8 purchase withholding (company 1/2/3/5% -> PND53, individual 1/2/3/5% -> PND3), 4 sale withholding (1/2/3/5%, tax_excluded, account 114300). Verified: `l10n_th` does not depend on `l10n_account_withholding_tax` and no Thai tax carries the on-payment flag; the Thai set is entirely ordinary negative-percentage taxes booked at document posting (`tax_exigibility` on_invoice for all 18).

## CAP-U24-01 Thai chart of accounts structure and loading

**Function-ID(s):** MCT-F03 (claims VDR-U24-C031, VDR-U24-C032, VDR-U24-C025, VDR-U24-C038); otherwise FUNCTION MAPPING REQUIRED.

### D1 Business purpose
Give a Thailand-registered company a ready ledger (144 six-digit accounts), Thai default accounts and default VAT taxes, withholding taxes, tax-report grid labels and tax-report definitions, loaded when the localisation module is installed on a company located in Thailand. VDR-U24-C001 VDR-U24-C005

### D2 Architecture
Module `l10n_th` (depends `account_qr_code_emv`, `account`; VDR-U24-C001) = template function `_get_th_template_data` and `_get_th_res_company` (VDR-U24-C007 VDR-U24-C010), four CSV files (`account.account-th.csv` 144 rows, `account.tax-th.csv` 18 taxes / 72 repartition rows, `account.tax.group-th.csv` 5 groups, `account.asset-th.csv` 12 rows unused), tax-report XML, invoice report view, QR bank override, partner computed field. Generic loader: `account/models/chart_template.py` (`try_loading` VDR-U24-C027, `_load`, `_load_data`, `_post_load_data`, `_setup_utility_bank_accounts` VDR-U24-C033); auto-trigger in `account/models/ir_module.py` (VDR-U24-C005); country gate in `base/models/ir_module.py` (VDR-U24-C004). Account semantics per type counts VDR-U24-C015; digit scheme VDR-U24-C016.

Account semantics (counts and meaning, from the CSV): assets 111xxx cash/bank/suspense/transfer, 112xxx receivables (112100 trade, 112101 POS, 112190 allowance, 112200 other), 113xxx inventories, 114xxx tax assets (114100 undue input VAT, 114200 input VAT, 114300 WHT creditable, 114400 VAT receivable, 114401 WHT receivable, 114500 prepaid CIT PND 51), 115xxx investments, 12xxxx non-current/fixed assets with paired accumulated-depreciation accounts; liabilities 211xxx borrowings, 212xxx payables, 213xxx tax liabilities (VDR-U24-C019), 22xxxx non-current; equity 311100, 321100, 321200; income 411xxx/42xxxx; direct cost 511xxx; expenses 611xxx-631100; technical 999999. Only 24 accounts are wired by template data (VDR-U24-C021); the rest are free for manual selection (VDR-U24-C022).

### D3 Logic
Install `l10n_th` -> if the company has no chart and its country equals TH, the first template (th) is queued to load at registry start (VDR-U24-C005 VDR-U24-C006) -> `try_loading` -> `_load` (admin only VDR-U24-C028; records loaded in en_US VDR-U24-C029) -> `_get_chart_template_data` merges `template_data` and per-model functions plus CSV rows (empty cells skipped VDR-U24-C026; missing files skipped VDR-U24-C025) -> `_post_load_data` creates bank/outstanding accounts (VDR-U24-C033), sets journal suspense/cash-difference accounts (VDR-U24-C035), income/expense defaults on sale/purchase journals (VDR-U24-C034), default taxes -> translations loaded after -> child companies loaded the same way (VDR-U24-C031).

State list:
- `no chart -> th loaded [install on TH company, or manual load by admin]` (VDR-U24-C005)
- `th loaded -> th reloaded [try_loading with same code: reload_template]` (VDR-U24-C030)
- `th loaded -> other chart [different code on a company without accounting: old template records and moves deleted first]` (VDR-U24-C030)

Template quirks: `tax_exigibility` set as string 'True' (VDR-U24-C012); `transfer_account_code_prefix` passed as a template-id string (VDR-U24-C013); asset CSV not loaded by any core function (VDR-U24-C023 VDR-U24-C024); no fiscal position/group/journal/reconcile-model files (VDR-U24-C025).

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Install on a TH company loads 144 accounts, 18 taxes, 5 groups, 3 reports, defaults (VDR-U24-C005, VDR-U24-C038). |
| 2 | Reversal/cancel/negative path | Reload refreshes; switching chart on a company with no accounting deletes previous template records; not allowed to delete when accounting exists (condition on `_existing_accounting`) (VDR-U24-C030). |
| 3 | Multi-company / data scope | Account code stored per company (VDR-U24-C032); loader runs on child companies (VDR-U24-C031); cross-reference U27/U28. |
| 4 | Side effects and cross-module triggers | Creates outstanding/bank accounts, sets journal defaults, default taxes on company and on products that already had taxes (VDR-U24-C033, VDR-U24-C034, VDR-U24-C035); post-init hook preserves tags (VDR-U24-C036). |
| 5 | Configuration and optionality | Auto-install gated by company country (VDR-U24-C004); demo creates TH Company (VDR-U24-C037); chart code digits fixed to 6 (VDR-U24-C008). |
| 6 | Validation and constraints | Admin-only loading (VDR-U24-C028); account type counts and flags fixed by CSV (VDR-U24-C015). |
| 7 | Roles and permissions | No ACL/rule/group declared by `l10n_th` (manifest data list VDR-U24-C216; DB 0 rows); core ACL for accounts: administrator edit, others read; multi-company rule on accounts (VDR-U24-C230). |
| 8 | Scheduled/automated behaviour | NOT APPLICABLE — no cron or automation declared by `l10n_th` or the loader (DB: 0 cron rows for module). |
| 9 | Exception and failure behaviour | Missing template files skipped silently (VDR-U24-C025); demo-load failure is logged and does not roll back the chart (generic loader, not re-read line by line). |
| 10 | Accounting, stock, audit, security and compliance | Chart of accounts correctness vs statutory formats UNKNOWN (VDR-U24-C041); Thai names are translation columns (VDR-U24-C040); account semantics only (counts). |

### DB reconciliation (config only)
Source CSV 144 accounts -> DB 147 (144 + bank 111203 + Outstanding Receipts 111204 + Outstanding Payments 111205) (VDR-U24-C038, VDR-U24-C033); account types DB equal file counts except cash 3->4 and current assets 15->17. Journals DB 7 = INV, BILL, MISC, EXCH, CABA, BNK1, STJ (VDR-U24-C039); 0 account groups; 0 fiscal positions; 2 reconcile models; company chart_template `th`, fiscal country Thailand, THB, code prefixes 11120/11110, transfer prefix literal `l10n_th_account_11120` (VDR-U24-C013); cash-basis flag true (VDR-U24-C012); anglo-saxon false; opening date empty. th_TH language exists but inactive; demo not loaded.

### Unknown / Runtime
VDR-U24-C041 · RT: auto-load order at registry start (VDR-U24-C005) · UNKNOWN: whether an external asset module would load the asset CSV (no Community function; U13 C215 aligned).

---

## CAP-U24-02 Thai VAT: taxes, tags, accounts and standard sale and purchase entries

**Function-ID(s):** MCT-F03 on VDR-U24-C065 only; otherwise FUNCTION MAPPING REQUIRED.

### D1 Business purpose
Six VAT records (7%, 0%, exempt; input and output) whose distribution lines post VAT to Thai VAT accounts and attach Thai return-grid labels so a VAT summary can be totalled from posted entries. VDR-U24-C069

### D2 Architecture
`account.tax-th.csv` rows 2-25 (VAT) with repartition (invoice/refund x base/tax), `account.tax.group-th.csv` (group VAT 7%), tax tags (13 DB rows) created from tag names in repartition cells (delimiter `||`), `account_tax_report_data.xml` (3 `account.report` records, 24 lines, 24 expressions, 3 columns). Engine (generic): `account/models/account_tax.py` (percent evaluation VDR-U24-C056, batching VDR-U24-C064, group fallback VDR-U24-C049, totals per group VDR-U24-C050, closing flag VDR-U24-C053); defaults VDR-U24-C059 VDR-U24-C058; price and rounding settings VDR-U24-C060 VDR-U24-C062; fiscal positions VDR-U24-C065.

Tax records (DB = source; ids 1-6): 7% purchase = Input VAT 7% (114200, tags 6/7); 7% sale = Output VAT 7% (213200, tags 1/5); 0% purchase/sale; 0% EXEMPT purchase/sale. Traced as VDR-U24-C042 VDR-U24-C043 VDR-U24-C044 VDR-U24-C045 VDR-U24-C046 VDR-U24-C047. Standard sale of 100 (INFERENCE VDR-U24-C079): customer receivable 107 (company receivable 112100) / revenue 100 (product income account, default 411100) / output VAT 7 on 213200 with tag 5; base line tag 1. Standard purchase of 100: expense 100 / input VAT 7 on 114200 tag 7 (base tag 6) / payable 107 (212100). Credit notes use refund distribution lines with the same accounts and tags (VDR-U24-C042). Zero-rate/exempt taxes keep the base grid label and post a zero tax line only if the engine keeps zero lines (RT).

### D3 Logic
Product default taxes -> invoice line taxes -> `_get_tax_details` evaluates percent excluded taxes as base x amount/100 (VDR-U24-C056) -> repartition lines give tax-line accounts and tags -> tax lines grouped on the document by repartition line; tax totals grouped per tax group (VDR-U24-C050) -> posting writes lines (U11). Closing flag: VAT lines True, withholding lines False (VDR-U24-C053) but unused by Community routines (VDR-U24-C054 VDR-U24-C055). Account description texts document manual month-end transfers: VDR-U24-C255 VDR-U24-C256 VDR-U24-C257. VAT report lines 1-12 total tags: output lines read with sign reversed (VDR-U24-C070), payable/excess formulas (VDR-U24-C071), carryover (VDR-U24-C073 VDR-U24-C205); no engine/UI in Community (VDR-U24-C075).

State list:
- `tax active -> tax archived [user]` (generic; not deleted when used)
- `document draft -> posted [post]: tax lines fixed on posting (VAT recognised at posting, no cash basis: VDR-U24-C057)`

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Sale/purchase with default 7% taxes yields VAT lines on 213200/114200 with grid tags (VDR-U24-C079, RT numeric). |
| 2 | Reversal/cancel/negative path | Refund distribution lines mirror invoice lines (VDR-U24-C042, VDR-U24-C078); VAT closing, return and reversal of returns not in Community (VDR-U24-C055). |
| 3 | Multi-company / data scope | Taxes, groups, accounts company-scoped by multi-company rules (VDR-U24-C230); chart loaded per company (VDR-U24-C031). |
| 4 | Side effects and cross-module triggers | Product default taxes (VDR-U24-C058); tax totals per group (VDR-U24-C050); tag-based report formulas (VDR-U24-C070); company-currency tax display for foreign-currency sales (VDR-U24-C067, cross-ref U25). |
| 5 | Configuration and optionality | Price included vs excluded (VDR-U24-C060, VDR-U24-C061); rounding (VDR-U24-C062); no fiscal positions (VDR-U24-C066); report definitions optional. |
| 6 | Validation and constraints | Constraints on repartition mirror, 100% sums, tax group country (generic, see U13); name uniqueness; used taxes cannot be deleted. RISK of group fallback (VDR-U24-C048). |
| 7 | Roles and permissions | Tax maintenance admin only; others read (VDR-U24-C229). |
| 8 | Scheduled/automated behaviour | NOT APPLICABLE — no cron or scheduled VAT routine in Community. |
| 9 | Exception and failure behaviour | No VAT-return engine: definitions stored without evaluator (VDR-U24-C075); statutory conformity UNKNOWN. |
| 10 | Accounting, stock, audit, security and compliance | Posted VAT lines are the tax-return source via tags; closing/periodicity absent (VDR-U24-C055); stats: 18 taxes, 72 repartition lines; zero and exempt taxes under group WHT 1% (VDR-U24-C048). |

### DB reconciliation (config only)
18 taxes DB = 18 source (6 VAT + 8 purchase WHT + 4 sale WHT), 72 repartition lines (4 per tax), 5 tax groups, 13 Thai tags (10 used by taxes, 3 unused: 10. Excess carried forward, SUR53, SUR3 — VDR-U24-C074), 3 Thai account reports + generic ones; report expression engines DB: tax_tags 13, aggregation 15, external 1 (Thai 24 expressions + 5 generic). company: account_sale_tax_id = 2 (Output VAT 7%), account_purchase_tax_id = 1 (Input VAT 7%), price tax_excluded, rounding round_globally, exigibility flag true, fiscal positions 0, domestic fiscal position none, `display_invoice_tax_company_currency` true (VDR-U24-C057). No Thai tax has `include_base_amount`, `cash_basis_transition_account_id`, or a non-default sequence; all `is_base_affected` true.

### Unknown / Runtime
VDR-U24-C076 · RT numeric results of combined 7% VAT plus withholding and rounding (VDR-U24-C064, VDR-U24-C079) · RT whether zero tax lines persist · UNKNOWN statutory conformity of grids and rates.

---

## CAP-U24-03 Withholding tax in the Thai tax set

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Model withholding tax as ordinary negative-percentage taxes so that a vendor bill or customer invoice shows the withheld amount, reduces payable/receivable and accumulates withheld amounts in dedicated accounts, with PND 53/PND 3 grid labels. Optional alternative mechanism (not used by the Thai set): payment-time withholding add-on. VDR-U24-C095

### D2 Architecture
Taxes (DB = source): purchase company payee `tax_wht_co_1/2/3/5` -> base label Income PND53, tax label PND53, account 213302 (VDR-U24-C080); purchase individual payee `tax_wht_pers_1/2/3/5` -> Income PND3 / PND3, account 213301 (VDR-U24-C082); sale `tax_wht_income_1/2/3/5` -> no labels, account 114300, price-excluded override (VDR-U24-C083). Category wording is in English description text with th_TH translation (VDR-U24-C084). Groups WHT 1/2/3/5% (VDR-U24-C087). Reports PND53 and PND3 (VDR-U24-C089, VDR-U24-C090). Optional mechanism `l10n_account_withholding_tax`: flag `is_withholding_tax_on_payment` (VDR-U24-C095, rules VDR-U24-C096), computation filter (VDR-U24-C097), core hook (VDR-U24-C098), entry builder (VDR-U24-C099, VDR-U24-C100), ACL (VDR-U24-C101); installed state (VDR-U24-C102); dependants named in manifests are future optional country packs (VDR-U24-C103).

### D3 Logic
Document-time: tax selected per line (company vs individual payee chosen by picking the tax; no partner-driven selection VDR-U24-C091) -> engine computes negative percent on the untaxed base (VDR-U24-C056, VDR-U24-C086) -> tax line to 213302/213301 (purchase) or 114300 (sale) with closing flag False (VDR-U24-C081) -> payable (purchase) = base + VAT - withholding; receivable (sale) reduced by withholding (INFERENCE from tax sign; numeric RT). Booked at posting because exigibility is on_invoice for all 18 (VDR-U24-C085); month-end consolidation and CIT credit are only described in account text (VDR-U24-C259 VDR-U24-C258 VDR-U24-C260); no certificate object, no payment-time step. If a Thai tax were flagged on-payment (technically allowed by the add-on rules: negative, not group/division): tax ignored at document computation (VDR-U24-C097), registered on the payment as cash net of withholding + tax item + base pair, number required (VDR-U24-C100) — not configured in this DB.

State list:
- `bill draft -> bill posted [post]: withholding tax line created at posting, payable reduced` (VDR-U24-C085)
- `invoice posted -> credit note [reverse]: refund distribution lines mirror` (VDR-U24-C080)
- (add-on, not used) `payment draft with withholding lines -> posted [net amount not negative]` (VDR-U24-C099)

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Vendor bill with 3% company-payee withholding: expense 100, VAT 7, withholding line -3 on 213302, payable 104 (INFERENCE, RT) (VDR-U24-C080). |
| 2 | Reversal/cancel/negative path | Credit note mirrors lines (VDR-U24-C080); payment-time add-on cancellation behaviour UNKNOWN (U23 C062). |
| 3 | Multi-company / data scope | Taxes company-scoped (VDR-U24-C230); template per company. |
| 4 | Side effects and cross-module triggers | Postings to 213301/213302/114300; grid labels feed PND reports (VDR-U24-C089); none to tax closing (VDR-U24-C081). |
| 5 | Configuration and optionality | Taxes selected manually; add-on optional and uninstalled (VDR-U24-C102); sale WHT forced excluded (VDR-U24-C083); purchase WHT follows company setting (VDR-U24-C092). |
| 6 | Validation and constraints | No Thai-specific constraint; add-on constrains negative, non group/division (VDR-U24-C096). |
| 7 | Roles and permissions | Tax edit admin only (VDR-U24-C229); add-on ACL 2 rows for invoicing group (VDR-U24-C101). |
| 8 | Scheduled/automated behaviour | NOT APPLICABLE — no cron or automation in Thai set or add-on. |
| 9 | Exception and failure behaviour | Add-on raises UserError without withholding number (VDR-U24-C100); Thai set has no dedicated failure mode. |
| 10 | Accounting, stock, audit, security and compliance | Withholding certificate/return absent (VDR-U24-C104); statutory timing/rates UNKNOWN; foreign payee (PND 54) not modelled (VDR-U24-C093); creditable asset 114300 type current asset (VDR-U24-C088). |

### DB reconciliation (config only)
12 withholding taxes (8 purchase, 4 sale) of 18 total; groups 1-4 (WHT 1/2/3/5%) payable 213500 receivable 114401; add-on `l10n_account_withholding_tax` uninstalled (0 external ids, no flag column) (VDR-U24-C102); accounts 213300-213303 exist, 213300 and 213303 referenced by no tax (VDR-U24-C093); Thai tags Income PND53, PND53, Income PND3, PND3 used; SUR53/SUR3 unused (VDR-U24-C074).

### Unknown / Runtime
VDR-U24-C104 · RT numeric results (VDR-U24-C086) · UNKNOWN effect of converting Thai taxes to payment-time on history and report grids (U23 aligned) · UNKNOWN statutory rates and timing.

---

## CAP-U24-04 Tax invoice, receipt, credit note and debit note documents

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Print customer invoices with a Thai title and buyer-branch label for Thai-fiscal-country companies; provide a Commercial Invoice document; relate credit notes, debit notes, receipts and numbering to the standard accounting flows. Title text and branch words are English source strings with Thai translations (translatable text, not requirements).

### D2 Architecture
`l10n_th/models/account_move.py` selector override (VDR-U24-C106) over core selector (VDR-U24-C105); core report dispatch (VDR-U24-C107) plus Thai elif (VDR-U24-C108); Thai template `report_invoice_document` (primary inherit; title replace VDR-U24-C109; branch label VDR-U24-C115); `report_commercial_invoice` (VDR-U24-C119) bound by domain (VDR-U24-C118, semantics VDR-U24-C121) with print guard (VDR-U24-C120); translations (VDR-U24-C123); core title block (VDR-U24-C110, VDR-U24-C111); receipts (VDR-U24-C113, VDR-U24-C114, VDR-U24-C112); debit-note add-on (VDR-U24-C134, VDR-U24-C135, VDR-U24-C136, VDR-U24-C137, VDR-U24-C139); amount in words (VDR-U24-C129, VDR-U24-C130, VDR-U24-C131, VDR-U24-C132, VDR-U24-C133).

Choice of layout (observation requested by programme owner): the Thai layout is selected by the **company fiscal country** (fixed in code: VDR-U24-C106); the title string is **fixed in the template** as the English source `Tax Invoice` (VDR-U24-C109); only the rendered wording follows the **partner language** through `t-lang` (VDR-U24-C122) and the catalogue (VDR-U24-C123). A customer with an English language record therefore gets the English title on the Thai layout; the layout cannot be driven by UI language.

Numbering: sales-side `INV/YYYY/00000` with Gregorian year (VDR-U24-C124, VDR-U24-C125); credit notes prefix R (VDR-U24-C126); payments prefix P (VDR-U24-C127); debit notes prefix D (VDR-U24-C136).

### D3 Logic
Print -> report action -> `account.report_invoice` -> `_get_name_invoice_report()` returns Thai name when company fiscal country is TH (VDR-U24-C106) -> Thai document renders standard body with `invoice_title` replaced by `Tax Invoice` for posted `out_invoice` only (VDR-U24-C110); partner VAT line followed by branch label (VDR-U24-C115); QR/totals/words from standard body (VDR-U24-C187, VDR-U24-C131). Commercial Invoice -> pre-render guard (VDR-U24-C120) -> standard document in partner language (VDR-U24-C119). Debit note (add-on, not installed): wizard VDR-U24-C135 -> `copy` with `debit_origin_id` (VDR-U24-C139) -> title VDR-U24-C137; with the Thai layout the Thai title replacement is applied after parent extensions (VDR-U24-C138, RT).

State list:
- `out_invoice draft -> posted [post]`: title changes from `Draft Invoice` to `Tax Invoice` (Thai) (VDR-U24-C110)
- `out_invoice posted -> cancelled`: title `Cancelled Invoice` (standard)
- `posted invoice -> credit note [reverse]`: title `Credit Note` (VDR-U24-C111)

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Thai company posts a customer invoice; PDF shows Tax Invoice, buyer VAT and branch label (VDR-U24-C109, VDR-U24-C115). |
| 2 | Reversal/cancel/negative path | Credit note keeps `Credit Note` title (VDR-U24-C111); debit note via add-on only (VDR-U24-C135); cancelled/draft standard titles. |
| 3 | Multi-company / data scope | Layout depends on each company's fiscal country (VDR-U24-C106); documents are company-scoped. |
| 4 | Side effects and cross-module triggers | Report print domain and guard (VDR-U24-C118, VDR-U24-C120); QR block uses bank and company switch (VDR-U24-C187); base report test registers the Commercial Invoice (VDR-U24-C224). |
| 5 | Configuration and optionality | Words flag, QR, dedicated credit/debit sequences, commercial invoice are optional (VDR-U24-C130, VDR-U24-C126). |
| 6 | Validation and constraints | No Thai-field enforcement on posting (VDR-U24-C128); commercial print guard (VDR-U24-C120); debit wizard guards (VDR-U24-C135). |
| 7 | Roles and permissions | Accounting invoice group prints documents; debit wizard ACL: invoicing group read/write/create (VDR-U24-C134 source ACL 1 row); no groups declared by `l10n_th`. |
| 8 | Scheduled/automated behaviour | NOT APPLICABLE — none for the Thai documents (core send/print crons are U11/U12). |
| 9 | Exception and failure behaviour | UserError on commercial print of non-invoices (VDR-U24-C120); words library missing returns empty text with a log warning (base amount_to_text, VDR-U24-C132); QR failure silent in print but raises for a stored ineligible method (VDR-U24-C188). |
| 10 | Accounting, stock, audit, security and compliance | Gregorian-year numbering (VDR-U24-C125); seller TIN from company header only (VDR-U24-C117); no seller branch, no abbreviated/combined documents, no e-tax (VDR-U24-C140); statutory content UNKNOWN. |

### DB reconciliation (config only)
`l10n_th` source: 3 QWeb templates (`report_invoice_document`, `report_commercial_invoice`, `report_invoice`) and 1 `ir.actions.report` (Commercial Invoice) -> DB 3 views, 1 report action (module-owned). INV and BILL journals `refund_sequence` true, `payment_sequence` false; BNK1 `payment_sequence` true (VDR-U24-C126, VDR-U24-C127). Company `display_invoice_amount_total_words` = true in DB (setter not identifiable; not set by the Thai template — VDR-U24-C130); `qr_code` false; `account_debit_note` uninstalled; `th_TH` language inactive.

### Unknown / Runtime
VDR-U24-C140 · RT rendering of Thai layout and debit-note title interplay (VDR-U24-C138) · RT whether num2words renders Thai (VDR-U24-C132) · UNKNOWN statutory document requirements.

---

## CAP-U24-05 Thai partner identity (tax ID, branch) and address

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Identify Thai customers and vendors by tax identifier (`vat`, label Tax ID) and branch label (from `company_registry`), validate the identifier when the optional add-on is installed, and keep addresses in the generic Thai layout.

### D2 Architecture
Core: `res.partner.vat`, `company_registry` (VDR-U24-C144), label (VDR-U24-C145), duplicate warnings (VDR-U24-C157 VDR-U24-C158), validation stub (VDR-U24-C146), VAT-required hook (VDR-U24-C159). Thai: computed `l10n_th_branch_name` (VDR-U24-C141 VDR-U24-C142 VDR-U24-C143). Add-on `base_vat` (not installed): dependency VDR-U24-C148, Thai check VDR-U24-C149, example VDR-U24-C150, tests VDR-U24-C151, run/skip rules VDR-U24-C152 VDR-U24-C153 VDR-U24-C154, prefix split VDR-U24-C155, normalisation VDR-U24-C156; core imports its reference table VDR-U24-C147. Address: format VDR-U24-C160; `base_address_extended` (not installed) VDR-U24-C161 VDR-U24-C162 VDR-U24-C163.

### D3 Logic
Edit partner `vat`/country -> (base_vat installed) inverse `_check_vat` -> `_run_vat_checks`: split prefix, format via stdnum compact if available, `_check_vat_number` -> `check_vat_th` -> stdnum th.tin `is_valid` -> ValidationError with expected format 13 digits or silently accepted when validation off/context key (VDR-U24-C152). With base_vat uninstalled (this DB) the stub returns value unchanged (VDR-U24-C146). Branch label computed at render time; empty for non-company or non-TH partners and therefore for contact children (VDR-U24-C142). Company vs individual payee for withholding is user-selected by tax (VDR-U24-C164).

State list:
- `vat typed -> validated [base_vat installed, validation error mode]` / `vat typed -> accepted unchanged [base_vat not installed]` (VDR-U24-C146)
- `branch registry empty -> label Headquarter`; `registry set -> label Branch <code>` (VDR-U24-C143)

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Partner company in TH with vat and registry: invoice shows Tax ID and Branch label (VDR-U24-C143, VDR-U24-C115). |
| 2 | Reversal/cancel/negative path | Clearing vat/registry empties the label; `/` marks no identifier (add-on) (VDR-U24-C154). |
| 3 | Multi-company / data scope | Partner `company_id` scoping and bank company rule apply (VDR-U24-C231); duplicate detection by company scope (VDR-U24-C157). |
| 4 | Side effects and cross-module triggers | Branch label on invoice only; fiscal position `vat_required` uses validity hook (VDR-U24-C159). |
| 5 | Configuration and optionality | Validation add-on optional (VDR-U24-C148); label Tax ID default (VDR-U24-C145); extended address optional (VDR-U24-C161). |
| 6 | Validation and constraints | Add-on: 13-digit format with check digit (library) (VDR-U24-C151); no branch-code validation anywhere. |
| 7 | Roles and permissions | Partner creation rights are generic partner-manager groups; `l10n_th` declares none; `base_address_extended` ACL 2 rows for res_city (source) — not installed. |
| 8 | Scheduled/automated behaviour | Add-on declares one cron (VIES update, source) — EU-only, NOT APPLICABLE to TH; DB uninstalled (VDR-U24-C148). |
| 9 | Exception and failure behaviour | ValidationError text with expected format (VDR-U24-C150); library absence UNKNOWN. |
| 10 | Accounting, stock, audit, security and compliance | Duplicate warnings for same registry/vat (VDR-U24-C157); stored form after validation UNKNOWN (VDR-U24-C156); statutory identifier/branch format UNKNOWN (VDR-U24-C165). |

### DB reconciliation (config only)
`l10n_th_branch_name`: 2 `ir.model.fields` rows (res.partner, res.users via delegation) ; `base_vat` uninstalled (no cron row, no `vies_valid` column); `base_address_extended` uninstalled; Thai states in `res_country_state`: 77; country Thailand `vat_label` null; address format as VDR-U24-C160.

### Unknown / Runtime
VDR-U24-C165 · RT stored vat form after validation (VDR-U24-C156) · RT interplay of branch warnings (INFERENCE from VDR-U24-C157).

---

## CAP-U24-06 Payments, PromptPay/EMV QR and bank/journal setup

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Print a PromptPay-style EMV merchant QR on customer invoices (is PromptPay supported? Yes, as a static-account credit-transfer QR with mobile/tax-ID/e-wallet proxy; no payment/reconciliation linkage), and provide the Thai template's bank and cash-related journal/account setup.

### D2 Architecture
Bridge `account_qr_code_emv` (VDR-U24-C166): method registry (VDR-U24-C167), payload (VDR-U24-C168), CRC (VDR-U24-C169), serialisation (VDR-U24-C170), merchant fields (VDR-U24-C172, VDR-U24-C183), MCC (VDR-U24-C173), additional-data hook (VDR-U24-C174), proxy fields (VDR-U24-C175), generic error check (VDR-U24-C182). Thai `res.partner.bank` extension: proxy types (VDR-U24-C176), constraint (VDR-U24-C177), tag 29 and AID (VDR-U24-C178), mobile normalisation (VDR-U24-C179), THB only (VDR-U24-C180), proxy error (VDR-U24-C181); test vector (VDR-U24-C184, VDR-U24-C185). Move side: display (VDR-U24-C187), generation (VDR-U24-C188), bank selection (VDR-U24-C189), holder country (VDR-U24-C186). Online route: VDR-U24-C191, VDR-U24-C192, VDR-U24-C193 (cross-ref U20). Journals/accounts: VDR-U24-C190.

### D3 Logic
Print invoice -> template calls `_generate_qr_code(silent_errors=True)` -> needs `company.qr_code` and a customer/vendor invoice type (VDR-U24-C187) -> stored method else first eligible; Thai bank (holder country TH) eligible only for THB (VDR-U24-C180) -> `_check_for_qr_code_errors` requires city, proxy type/value (VDR-U24-C183, VDR-U24-C181) -> payload tags 00,01 `12`,29 (AID + proxy sub-tag),52 `0000`,53 `764`,54 amount,58 `TH`,59,60 + `6304` CRC (VDR-U24-C168, VDR-U24-C184) -> base64 barcode image in the report. The QR encodes the invoice residual in the document currency. No reference tag for Thailand (VDR-U24-C174).

State list:
- `qr_code_method empty -> emv_qr [first successful generation]` (VDR-U24-C188)
- `emv_qr stored -> print error [currency changed to non-THB or proxy removed]` (VDR-U24-C180, VDR-U24-C188)
- `bank proxy none -> eligible [proxy type and value set, constraint passes]` (VDR-U24-C177)

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Company switch on, THB invoice, company bank with mobile proxy and city -> QR image on PDF (VDR-U24-C184). |
| 2 | Reversal/cancel/negative path | Non-THB or missing proxy -> error; silent skip when no method stored (VDR-U24-C188, VDR-U24-C185). |
| 3 | Multi-company / data scope | Holder partner bank rule scopes proxies per company (VDR-U24-C231); journal accounts per company (VDR-U24-C032). |
| 4 | Side effects and cross-module triggers | No payment/reconciliation hook from QR (VDR-U24-C194); online PromptPay method inactive (VDR-U24-C191). |
| 5 | Configuration and optionality | Company QR switch off in DB (VDR-U24-C187); `include_reference` has no effect for TH (VDR-U24-C174); optional gateways (VDR-U24-C192). |
| 6 | Validation and constraints | 13/10-digit regexes (VDR-U24-C177); THB only (VDR-U24-C180); name/city truncation (VDR-U24-C172). |
| 7 | Roles and permissions | Bank accounts: partner-bank 'Creation' group edits; accountants read; `account_qr_code_emv` declares no ACL/rule/group (DB 0) (VDR-U24-C166). |
| 8 | Scheduled/automated behaviour | NOT APPLICABLE — no cron for QR or Thai bank logic. |
| 9 | Exception and failure behaviour | UserError messages: THB only (PayNow wording), proxy type, city (VDR-U24-C180, VDR-U24-C181); base missing-info check ineffective (VDR-U24-C182). |
| 10 | Accounting, stock, audit, security and compliance | Payload length/CRC mismatch risk for non-ASCII merchant text (VDR-U24-C171); banking-app acceptance UNKNOWN (VDR-U24-C195); cheque method present generic. |

### DB reconciliation (config only)
`account_qr_code_emv`: 0 ACL, 0 rules, 0 groups, 0 cron, 1 view, 12 model-field rows, 1 model row; `res.partner.bank.proxy_type` selection DB: none, ewallet_id, merchant_tax_id, mobile; `res_partner_bank` rows 0; journal BNK1 (suspense 111201, default 111203) has 3 payment method lines (manual in/out, checks out) (VDR-U24-C190); no cash journal; company `qr_code` false; `payment_method` promptpay inactive, all real providers disabled (VDR-U24-C191); 10 payment terms, 25 payment methods rows.

### Unknown / Runtime
VDR-U24-C195 · RT payload character vs byte lengths (VDR-U24-C171) · RT gateway behaviour (U20).

---

## CAP-U24-07 Period, lock and fiscal-year behaviour

**Function-ID(s):** PCO-F01 and PCO-F02 on matching claims; otherwise FUNCTION MAPPING REQUIRED

### D1 Business purpose
Define the fiscal year end and lock dates; record that Community has no tax-return periodicity or closing routine and no non-Gregorian calendar.

### D2 Architecture
`account/models/company.py` fields (VDR-U24-C196, VDR-U24-C199, VDR-U24-C200), check (VDR-U24-C197), sequence effect (VDR-U24-C198), lock exception model (VDR-U24-C201), placeholder (VDR-U24-C203), onboarding text (VDR-U24-C204), Thai VAT report previous-period scope (VDR-U24-C205), language record (VDR-U24-C206).

### D3 Logic
Fiscal year end (31/12 default; Thai template sets none) feeds sequence prefix and opening-balance checks; lock dates postpone entries to later dates by journal sequence (VDR-U24-C202); the tax-lock help text depends on a closing entry that Community never creates (VDR-U24-C055); VAT report carryover refers to a return-period concept not defined here (VDR-U24-C205); no calendar conversion code (VDR-U24-C207).

State list:
- `period open -> period locked [lock date set at or after end]` (VDR-U24-C199)
- `locked -> reopened for a user [lock exception, not under hard lock]` (VDR-U24-C201, VDR-U24-C200)

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Defaults 31/12 and empty lock dates (DB) (VDR-U24-C196, VDR-U24-C199). |
| 2 | Reversal/cancel/negative path | Exceptions reopen non-hard locks (VDR-U24-C201); hard lock irreversible (VDR-U24-C200). |
| 3 | Multi-company / data scope | Lock dates are company fields; scope is the company (U27/U28 for hierarchy). |
| 4 | Side effects and cross-module triggers | Fiscal year end drives sequence naming (VDR-U24-C198). |
| 5 | Configuration and optionality | Thai template leaves fiscal year and locks unset (VDR-U24-C196). |
| 6 | Validation and constraints | Day/month validity (VDR-U24-C197). |
| 7 | Roles and permissions | Lock settings editable by accounting administrators (generic). |
| 8 | Scheduled/automated behaviour | NOT APPLICABLE — no cron; no tax periodicity. |
| 9 | Exception and failure behaviour | No-op deprecated tax-return check (VDR-U24-C203). |
| 10 | Accounting, stock, audit, security and compliance | No VAT period engine, no BE-year support (VDR-U24-C208, VDR-U24-C207); filing deadlines UNKNOWN. |

### DB reconciliation (config only)
res_company: fiscalyear_last_day 31, fiscalyear_last_month 12, fiscalyear_lock_date/tax_lock_date/sale_lock_date/purchase_lock_date/hard_lock_date all null, account_opening_date null, THB with rounding 0.01 and 2 decimals; language th_TH present but inactive (only en_US active); res_lang th_TH date_format %d/%m/%Y.

### Unknown / Runtime
VDR-U24-C207 · VDR-U24-C208 · RT browser rendering of dates in Thai locale (not examined).

---

## CAP-U24-08 Thai statutory-output gaps (not present in Community)

**Function-ID(s):** PCO-F02 on the periodicity gap only; otherwise FUNCTION MAPPING REQUIRED

### D1 Business purpose
Make visible which Thai-expected outputs exist or do not exist in Community source, each with the search done; no legal requirement is asserted.

### D2 Architecture
Present: VDR-U24-C216, chart/taxes/reports (CAP-U24-01..03), documents (CAP-U24-04), QR (CAP-U24-06). Absent: see claims below (UNKNOWN class with `n/a` pointers carry the grep). Searches ran over `odoo/addons` (py, xml, csv, js) excluding `l10n_th`, i18n and tests; matches in foreign packs are listed by name only.

### D3 Logic
Gap register (each `NOT PRESENT IN COMMUNITY SOURCE` unless stated):
1. VAT return form/filing (PP 30 style) and VAT books — VDR-U24-C209
2. Withholding certificates, PND 1/2/54 reports, PND filing — VDR-U24-C210
3. e-Tax invoice / e-Receipt format — VDR-U24-C211
4. Abbreviated or combined tax invoice, seller branch, mandatory-field enforcement — VDR-U24-C212
5. Buddhist-era year printing — VDR-U24-C207
6. Amount in words — PARTIALLY PRESENT generically; Thai text unknown — VDR-U24-C213 (VDR-U24-C129, VDR-U24-C130, VDR-U24-C132)
7. Input-VAT proration, foreign-payee withholding, Thai financial statement formats — VDR-U24-C214
8. Tax periodicity/closing — VDR-U24-C215 (VDR-U24-C208)
Foreign-owned Thai companies, subsidiaries, branches, representative and regional offices: nothing Thai-specific exists beyond the generic company hierarchy (VDR-U24-C223, VDR-U24-C031); legal needs UNKNOWN (VDR-U24-C217).

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Present items are listed in D2; the gap list is the deliverable. |
| 2 | Reversal/cancel/negative path | NOT APPLICABLE — a register of absences has no reversal path. |
| 3 | Multi-company / data scope | Gaps apply to every Thai-fiscal-country company; no multi-company nuance observed. |
| 4 | Side effects and cross-module triggers | NOT APPLICABLE — no code. |
| 5 | Configuration and optionality | Any missing output would be an add-on or custom build, outside Community. |
| 6 | Validation and constraints | NOT APPLICABLE. |
| 7 | Roles and permissions | NOT APPLICABLE. |
| 8 | Scheduled/automated behaviour | NOT APPLICABLE. |
| 9 | Exception and failure behaviour | NOT APPLICABLE. |
| 10 | Accounting, stock, audit, security and compliance | Compliance consequences UNKNOWN; each gap is a negative search, not a requirement (VDR-U24-C217). |

### DB reconciliation (config only)
No DB configuration relates to the absent outputs; Thai report records 3/24/24 equal source; `account_edi`/`account_edi_ubl_cii` installed with no Thai format.

### Unknown / Runtime
All gap claims are UNKNOWN-class negative searches (RT where the generic facility depends on an external library).

---

## CAP-U24-09 Country-pack boundary and cross-border touchpoints

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
State the mechanical boundary between the Thai localisation and the 227 non-Thai localisation packs (**FUTURE OPTIONAL COUNTRY PACK**), and the Thai touchpoints with multi-currency and cross-border behaviour (in scope; deep mechanics U25/U26; company structure U27/U28).

### D2 Architecture
Country gate on auto-install (VDR-U24-C218, VDR-U24-C004); on-demand foreign-pack path (VDR-U24-C219, VDR-U24-C220); foreign VAT registrations (VDR-U24-C221, VDR-U24-C222); Thai package footprint (VDR-U24-C223, VDR-U24-C224); packs depending on generic add-ons (VDR-U24-C103, VDR-U24-C225); DB install state (VDR-U24-C226). Table in Appendix A is mechanical from manifests and the boundary profile; no pack's accounting rules were read.

### D3 Logic
`button_install` auto-installs a pack only if its auto-install dependencies are met AND (no countries OR a company in a pack country) (VDR-U24-C004). With one Thai company: no other pack installs automatically; a Thai company that creates a foreign fiscal position with `action_create_foreign_taxes` installs that pack on demand (VDR-U24-C219). Thai cross-border touchpoints: THB company currency, foreign-currency documents with taxes in company currency (VDR-U24-C067, VDR-U24-C227), zero-rate tax picked manually (VDR-U24-C066), QR THB-only (VDR-U24-C180), no foreign-payee withholding (VDR-U24-C093).

State list:
- `pack uninstalled -> pack installed [auto-install gate satisfied or manual install or foreign taxes action]` (VDR-U24-C004, VDR-U24-C219)

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | One Thai company: only `l10n_th` installed (VDR-U24-C226). |
| 2 | Reversal/cancel/negative path | Uninstalling a chart module clears `chart_template` on companies that used it (generic `module_uninstall`). |
| 3 | Multi-company / data scope | Pack gate evaluated across all companies (VDR-U24-C004); a foreign-country company would trigger its pack. |
| 4 | Side effects and cross-module triggers | 119 packs extend core accounting models (profile) — collision risk with the Thai document selector (VDR-U24-C105). |
| 5 | Configuration and optionality | Packs are optional and deferred. |
| 6 | Validation and constraints | Foreign taxes action restricted to accounting managers (VDR-U24-C219). |
| 7 | Roles and permissions | Roles: accounting managers for the foreign taxes action; otherwise generic. |
| 8 | Scheduled/automated behaviour | NOT APPLICABLE — no scheduled behaviour in boundary logic. |
| 9 | Exception and failure behaviour | Foreign taxes helper stops when taxes of the country exist (VDR-U24-C220). |
| 10 | Accounting, stock, audit, security and compliance | Cross-border and structure questions UNKNOWN (VDR-U24-C228); no country-specific rules studied. |

### DB reconciliation (config only)
`ir_module_module`: l10n_th installed; 230 other `l10n_*` uninstalled; companies: 1; `account_peppol`, `base_vat`, `account_debit_note`, `l10n_account_withholding_tax`, `base_address_extended` uninstalled; `account_qr_code_emv`, `account_edi`, `account_edi_ubl_cii`, `account_add_gln` installed.

### Unknown / Runtime
VDR-U24-C228 · RT behaviour when a foreign-country company is added (auto-install on next install flow).

---

## Appendix A. Mechanical country-pack boundary table (CAP-U24-09)

Source: manifests of `odoo/addons/l10n_*` (231 directories) + `00_CONTROL/COUNTRY_PACK_BOUNDARY_PROFILE_227.tsv`; installation state from the restored DB. Columns: auto = manifest `auto_install` (T = true/all deps, list = named deps); cty = manifest `countries`; core-ext = count of core accounting models extended (profile); models = generic accounting/partner/company models extended by name; hooks = core hook methods overridden (from a fixed list of posting/numbering/tax/document hooks); archetype from the profile. Class for all rows below the first four: **FUTURE OPTIONAL COUNTRY PACK**. No accounting rule of any pack was studied.

**Non-pack l10n names (4):** `l10n_th` (installed; THAI LOCALIZATION), `l10n_account_withholding_tax` (generic mechanism, uninstalled), `l10n_account_withholding_tax_pos` (generic mechanism, uninstalled), `l10n_account_edi_ubl_cii_tests` (test helper, uninstalled).

| module | class | state | archetype | auto | cty | core-ext | models extended | core hooks overridden |
|---|---|---|---|---|---|---|---|---|
| l10n_ae | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ae | 1 | account.chart.template,account.move | account.move._get_name_invoice_report |
| l10n_ae_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 0 | - | - |
| l10n_anz_ubl_pint | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | au,nz | 2 | account.move,res.partner | - |
| l10n_ar | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ar | 7 | account.chart.template,account.fiscal.position,account.journal,account.move,account.move.line,account.tax.group,res.company,res.partner,res.partner.bank | account.journal.write,account.move._get_last_sequence_domain,account.move._get_name_invoice_report,account.move._get_starting_sequence,account.move._post,res.company.write |
| l10n_ar_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 1 | res.partner | - |
| l10n_ar_stock | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 0 | - | - |
| l10n_ar_website_sale | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | ar | 1 | res.config.settings | - |
| l10n_ar_withholding | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | ar | 5 | account.chart.template,account.move,account.payment,account.payment.register,account.tax,res.company,res.config.settings,res.partner | account.payment.register._compute_amount |
| l10n_at | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | at | 1 | account.chart.template,account.journal | - |
| l10n_au | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | au | 4 | account.chart.template,account.move,account.payment,res.company,res.partner,res.partner.bank | account.move._get_name_invoice_report |
| l10n_bd | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | bd | 0 | account.chart.template | - |
| l10n_be | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | be | 4 | account.chart.template,account.journal,account.move,account.tax,res.partner | - |
| l10n_be_pos_restaurant | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 0 | account.chart.template | - |
| l10n_be_pos_sale | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 0 | - | - |
| l10n_bf | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | bf | 0 | account.chart.template | - |
| l10n_bg | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | bg | 0 | account.chart.template | - |
| l10n_bg_ledger | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | T | bg | 2 | account.journal,account.move | - |
| l10n_bh | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | bh | 0 | account.chart.template | - |
| l10n_bj | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | bj | 0 | account.chart.template | - |
| l10n_bo | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | bo | 0 | account.chart.template | - |
| l10n_br | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | br | 6 | account.chart.template,account.fiscal.position,account.journal,account.move,account.tax,res.company,res.partner,res.partner.bank | account.move._get_last_sequence_domain |
| l10n_br_sales | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | T | - | 0 | - | - |
| l10n_br_website_sale | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 0 | - | - |
| l10n_ca | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ca | 2 | account.chart.template,res.company,res.partner | - |
| l10n_cd | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | cd | 0 | account.chart.template | - |
| l10n_cf | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | cf | 0 | account.chart.template | - |
| l10n_cg | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | cg | 0 | account.chart.template | - |
| l10n_ch | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ch | 3 | account.chart.template,account.journal,account.move,account.move.send,account.payment,res.partner.bank | res.partner.bank.create,res.partner.bank.write |
| l10n_ch_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 0 | - | - |
| l10n_ci | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ci | 0 | account.chart.template | - |
| l10n_cl | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | cl | 5 | account.chart.template,account.move,account.move.line,account.tax,res.company,res.partner | account.move._compute_tax_totals,account.move._get_last_sequence_domain,account.move._get_name_invoice_report,account.move._get_starting_sequence,account.move._post |
| l10n_cm | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | cm | 0 | account.chart.template | - |
| l10n_cn | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | cn | 1 | account.chart.template,account.move | - |
| l10n_cn_city | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | cn | 0 | - | - |
| l10n_co | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | co | 0 | account.chart.template | - |
| l10n_co_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 0 | - | - |
| l10n_cr | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | cr | 0 | account.chart.template | - |
| l10n_cy | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | cy | 0 | account.chart.template | - |
| l10n_cz | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | cz | 2 | account.chart.template,account.move,res.company | - |
| l10n_de | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | de | 7 | account.account,account.chart.template,account.journal,account.move,account.tax,res.company,res.partner | account.account.write,account.move._post,res.company.write |
| l10n_din5008 | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | T | de,ch | 1 | res.company,res.config.settings | - |
| l10n_din5008_expense | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | T | - | 0 | - | - |
| l10n_din5008_purchase | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 0 | - | - |
| l10n_din5008_repair | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | T | - | 0 | - | - |
| l10n_din5008_sale | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 0 | - | - |
| l10n_din5008_stock | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 0 | - | - |
| l10n_dk | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | dk | 3 | account.account,account.chart.template,account.journal,res.partner | - |
| l10n_dk_fik | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | T | - | 2 | account.journal,account.move | - |
| l10n_dk_nemhandel | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | account_edi_ubl_cii,l10n_dk | - | 4 | account.journal,account.move,account.move.send,res.company,res.config.settings,res.partner | res.partner.create,res.partner.write |
| l10n_dk_nemhandel_response | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | T | - | 2 | account.move,res.partner | account.move._post,account.move.button_cancel |
| l10n_dk_oioubl | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | T | - | 2 | account.move,res.partner | - |
| l10n_do | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | do | 0 | account.chart.template | - |
| l10n_dz | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | dz | 0 | account.chart.template | - |
| l10n_ec | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ec | 6 | account.chart.template,account.journal,account.move,account.tax,account.tax.group,res.company,res.partner | account.move._get_last_sequence_domain,account.move._get_starting_sequence |
| l10n_ec_sale | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 0 | - | - |
| l10n_ec_stock | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 0 | account.chart.template | - |
| l10n_ee | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ee | 2 | account.chart.template,account.tax,res.company | - |
| l10n_eg | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | eg | 1 | account.chart.template,account.tax | - |
| l10n_eg_edi_eta | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | eg | 5 | account.journal,account.move,res.company,res.config.settings,res.partner | account.move.button_draft |
| l10n_es | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | es | 4 | account.chart.template,account.move,account.tax,res.company,res.config.settings,res.partner | - |
| l10n_es_edi_facturae | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | l10n_es | - | 4 | account.chart.template,account.move,account.move.send,account.tax,res.company,res.partner | - |
| l10n_es_edi_sii | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | es | 2 | account.move,account.move.send,res.company,res.config.settings | - |
| l10n_es_edi_tbai | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | - | 3 | account.move,account.move.line,account.move.send,res.company,res.config.settings | account.move.button_draft |
| l10n_es_edi_tbai_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | - | 1 | res.company | - |
| l10n_es_edi_verifactu | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | - | 4 | account.chart.template,account.move,account.move.send,account.tax,res.company,res.config.settings,res.partner | - |
| l10n_es_edi_verifactu_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | - | 2 | account.move,res.company | - |
| l10n_es_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | - | - | 2 | account.move,res.company,res.config.settings | - |
| l10n_et | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | et | 0 | account.chart.template | - |
| l10n_eu_oss | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | - | 1 | res.company,res.config.settings | - |
| l10n_fi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | fi | 3 | account.chart.template,account.journal,account.move,res.partner | - |
| l10n_fi_sale | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 0 | - | - |
| l10n_fr | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | - | fr | 2 | res.company,res.partner | res.company.create,res.company.write |
| l10n_fr_account | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | account | fr | 3 | account.chart.template,account.move,res.company,res.partner | - |
| l10n_fr_facturx_chorus_pro | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | fr | 1 | account.move | - |
| l10n_fr_hr_holidays | FUTURE OPTIONAL COUNTRY PACK | uninstalled | payroll/hr | hr_holidays | fr | 1 | res.company,res.config.settings | - |
| l10n_fr_hr_work_entry_holidays | FUTURE OPTIONAL COUNTRY PACK | uninstalled | payroll/hr | hr_work_entry_holidays | fr | 0 | - | - |
| l10n_fr_pdp | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | l10n_fr_account,auth_totp_mail | - | 5 | account.journal,account.move,account.move.send,account.tax,res.company,res.config.settings,res.partner | account.move._post,account.move.button_cancel,account.move.button_draft |
| l10n_fr_pdp_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 2 | account.move,res.company | - |
| l10n_fr_pos_cert | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 2 | account.fiscal.position,res.company | account.fiscal.position.write,res.company.create,res.company.write |
| l10n_ga | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ga | 0 | account.chart.template | - |
| l10n_gcc_invoice | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | - | 3 | account.move,account.move.line,res.company,res.config.settings | account.move._get_name_invoice_report,account.move.create |
| l10n_gcc_invoice_stock_account | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 0 | - | - |
| l10n_gcc_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 0 | res.config.settings | - |
| l10n_ge | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | - | GE | 0 | account.chart.template | - |
| l10n_gf | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | gf | 0 | - | - |
| l10n_gn | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | gn | 0 | account.chart.template | - |
| l10n_gp | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | gp | 0 | - | - |
| l10n_gq | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | gq | 0 | account.chart.template | - |
| l10n_gr | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | gr | 0 | account.chart.template | - |
| l10n_gr_edi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | gr | 7 | account.fiscal.position,account.move,account.move.line,account.move.send,account.tax,res.company,res.config.settings,res.partner | account.move._get_name_invoice_report |
| l10n_gr_edi_e_invoo | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | l10n_gr_edi | gr | 2 | account.move,account.move.send,res.company | - |
| l10n_gt | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | gt | 0 | account.chart.template | - |
| l10n_gw | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | gw | 0 | account.chart.template | - |
| l10n_hk | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | hk | 0 | account.chart.template,res.partner.bank | - |
| l10n_hn | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | hn | 0 | account.chart.template | - |
| l10n_hr | FUTURE OPTIONAL COUNTRY PACK | uninstalled | payroll/hr | account | hr | 0 | account.chart.template | - |
| l10n_hr_edi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | - | 7 | account.chart.template,account.journal,account.move,account.move.line,account.move.send,account.tax,res.company,res.config.settings,res.partner | account.move._post |
| l10n_hr_kuna | FUTURE OPTIONAL COUNTRY PACK | uninstalled | payroll/hr | - | hr | 0 | account.chart.template | - |
| l10n_hu | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | hu | 2 | account.chart.template,account.move,res.partner | account.move._post |
| l10n_hu_edi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | l10n_hu | - | 5 | account.chart.template,account.move,account.move.send,account.tax,res.company,res.config.settings,res.partner | account.move._get_name_invoice_report,res.config.settings.create |
| l10n_hu_edi_receive | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | - | 2 | account.move,res.company | - |
| l10n_id | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | id | 1 | account.chart.template,account.move,res.partner.bank | account.move._compute_tax_totals |
| l10n_id_efaktur_coretax | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | T | - | 4 | account.move,account.move.line,res.partner | - |
| l10n_id_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 0 | - | - |
| l10n_ie | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ie | 1 | account.chart.template,account.journal | - |
| l10n_il | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | il | 0 | account.chart.template | - |
| l10n_in | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | in | 10 | account.account,account.chart.template,account.journal,account.move,account.move.line,account.payment,account.report,account.tax,res.company,res.config.settings,res.partner | account.move._get_name_invoice_report,account.move._post,account.tax._prepare_base_line_for_taxes_computation,res.company.create,res.company.write,res.partner.create,res.partner.write |
| l10n_in_edi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | in | 4 | account.move,account.move.line,account.move.send,res.company,res.config.settings,res.partner | account.move._post,account.move.button_draft |
| l10n_in_ewaybill | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | in | 2 | account.move,res.company,res.config.settings | - |
| l10n_in_ewaybill_irn | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | T | - | 0 | - | - |
| l10n_in_ewaybill_stock | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 0 | - | - |
| l10n_in_hr_holidays | FUTURE OPTIONAL COUNTRY PACK | uninstalled | payroll/hr | hr_holidays | in | 0 | - | - |
| l10n_in_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 6 | account.move,account.move.line,account.tax,res.company,res.partner | - |
| l10n_in_purchase_stock | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 1 | account.move | - |
| l10n_in_sale | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 0 | - | - |
| l10n_in_sale_stock | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 1 | account.move | - |
| l10n_in_stock | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 0 | - | - |
| l10n_iq | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | iq | 0 | account.chart.template | - |
| l10n_it | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | it | 2 | account.chart.template,account.move,account.tax | - |
| l10n_it_edi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | l10n_it | - | 4 | account.chart.template,account.move,account.move.send,account.tax,res.company,res.config.settings,res.partner | account.move._post,account.move.button_draft |
| l10n_it_edi_doi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | it | 5 | account.chart.template,account.fiscal.position,account.move,account.tax,res.company,res.partner | account.move._post |
| l10n_it_edi_sale | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | - | 0 | - | - |
| l10n_it_stock_ddt | FUTURE OPTIONAL COUNTRY PACK | uninstalled | stock/sale/purchase/website bridge | T | - | 1 | account.move | - |
| l10n_jo | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | jo | 0 | account.chart.template | - |
| l10n_jo_edi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | l10n_jo | jo | 3 | account.move,account.move.send,account.tax,res.company,res.config.settings | account.move._get_name_invoice_report,account.move._post,account.move.button_draft |
| l10n_jo_edi_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | jo | 2 | account.move,res.company,res.config.settings | - |
| l10n_jp | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | jp | 0 | account.chart.template | - |
| l10n_jp_ubl_pint | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | jp | 2 | account.move,res.partner | - |
| l10n_ke | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ke | 3 | account.chart.template,account.move,account.tax,res.company | - |
| l10n_ke_edi_tremol | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | ke | 3 | account.move,account.move.send,res.company,res.config.settings,res.partner | - |
| l10n_kh | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | - | kh | 0 | account.chart.template,res.partner.bank | - |
| l10n_km | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | km | 0 | account.chart.template | - |
| l10n_kr | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | kr | 0 | account.chart.template | - |
| l10n_kw | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | kw | 0 | account.chart.template | - |
| l10n_kz | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | kz | 0 | account.chart.template | - |
| l10n_latam_base | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | - | 2 | res.company,res.partner | res.company.create,res.partner._check_vat |
| l10n_latam_check | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | - | 4 | account.chart.template,account.journal,account.move,account.move.line,account.payment,account.payment.register | account.journal.create,account.move.button_draft,account.payment._compute_amount,account.payment.action_post,account.payment.register._compute_amount |
| l10n_latam_invoice_document | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | - | 4 | account.chart.template,account.journal,account.move,account.move.line,res.company | account.move._compute_name,account.move._get_last_sequence_domain,account.move._get_starting_sequence,account.move._post |
| l10n_lb_account | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | account | lb | 0 | account.chart.template | - |
| l10n_lk | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | lk | 0 | account.chart.template | - |
| l10n_lk_invoice | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | l10n_lk | - | 3 | account.move,res.company,res.partner | account.move._get_name_invoice_report,account.move._get_starting_sequence |
| l10n_lt | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | lt | 2 | account.chart.template,account.journal,account.tax | - |
| l10n_lu | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | lu | 0 | account.chart.template | - |
| l10n_lv | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | lv | 0 | account.chart.template | - |
| l10n_ma | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ma | 2 | account.chart.template,account.journal,res.partner | - |
| l10n_mc | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | mc | 0 | - | - |
| l10n_ml | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ml | 0 | account.chart.template | - |
| l10n_mn | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | mn | 0 | account.chart.template | - |
| l10n_mq | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | mq | 0 | - | - |
| l10n_mr | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | - | mr | 0 | account.chart.template | - |
| l10n_mt | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | mt | 0 | account.chart.template | - |
| l10n_mt_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | mt | 0 | - | - |
| l10n_mu_account | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | account | mu | 1 | account.chart.template,account.move | account.move._get_name_invoice_report |
| l10n_mx | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | mx | 4 | account.account,account.chart.template,account.move.line,account.tax,res.company,res.config.settings,res.partner.bank | account.account.create |
| l10n_my | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | my | 1 | account.chart.template | - |
| l10n_my_edi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | my | 6 | account.move,account.move.line,account.move.send,account.tax,res.company,res.config.settings,res.partner | account.move._get_name_invoice_report |
| l10n_my_edi_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | my | 0 | - | - |
| l10n_my_ubl_pint | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | my | 3 | account.move,res.company,res.partner | - |
| l10n_mz | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | mz | 0 | account.chart.template | - |
| l10n_ne | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ne | 0 | account.chart.template | - |
| l10n_ng | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ng | 0 | account.chart.template | - |
| l10n_nl | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | nl | 2 | account.chart.template,account.journal,res.company | - |
| l10n_no | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | no | 5 | account.chart.template,account.journal,account.move,account.tax,res.company,res.partner | - |
| l10n_nz | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | nz | 3 | account.chart.template,account.move,account.payment,res.partner | account.move._get_name_invoice_report |
| l10n_om | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | T | om | 0 | account.chart.template | - |
| l10n_pa | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | pa | 0 | account.chart.template | - |
| l10n_pe | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | pe | 4 | account.chart.template,account.move,account.tax,res.company,res.partner | - |
| l10n_pe_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 1 | res.partner | - |
| l10n_ph | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ph | 5 | account.chart.template,account.move,account.payment,account.tax,res.company,res.partner | - |
| l10n_pk | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | pk | 0 | account.chart.template | - |
| l10n_pl | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | pl | 4 | account.chart.template,account.move,res.company,res.config.settings,res.partner | - |
| l10n_pl_bank_verification | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | T | - | 1 | account.payment,account.payment.register | - |
| l10n_pl_edi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | l10n_pl | - | 4 | account.journal,account.move,account.move.send,res.company,res.config.settings,res.partner | account.move.button_draft |
| l10n_pl_edi_jst | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | - | 2 | account.move,res.partner | - |
| l10n_pt | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | pt | 2 | account.account,account.chart.template,account.tax | - |
| l10n_qa | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | qa | 0 | account.chart.template | - |
| l10n_re | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | re | 0 | - | - |
| l10n_ro | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ro | 1 | account.chart.template,res.partner | - |
| l10n_ro_cpv_code | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | - | 1 | - | - |
| l10n_ro_edi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | - | 3 | account.move,account.move.send,res.company,res.config.settings,res.partner | - |
| l10n_ro_edi_stock | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | - | 0 | - | - |
| l10n_ro_edi_stock_batch | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | - | 0 | - | - |
| l10n_rs | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | rs | 1 | account.chart.template,account.move | - |
| l10n_rs_edi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | rs | 3 | account.move,account.move.send,res.company,res.config.settings,res.partner | account.move.button_draft |
| l10n_rw | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | rw | 0 | account.chart.template | - |
| l10n_sa | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | sa | 1 | account.chart.template,account.move | account.move._get_name_invoice_report,account.move._post,account.move.write |
| l10n_sa_edi | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | sa | 6 | account.chart.template,account.journal,account.move,account.move.line,account.move.send,account.tax,res.company,res.config.settings,res.partner | account.move.button_draft,res.company.write |
| l10n_sa_edi_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | sa | 2 | account.move,res.company | - |
| l10n_sa_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 0 | - | - |
| l10n_sa_withholding_tax | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | l10n_sa | - | 0 | - | - |
| l10n_se | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | se | 4 | account.chart.template,account.journal,account.move,res.company,res.partner | - |
| l10n_sg | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | sg | 3 | account.chart.template,account.move,res.company,res.partner,res.partner.bank | - |
| l10n_sg_ubl_pint | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | sg | 3 | account.move,account.tax,res.partner | - |
| l10n_si | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | si | 2 | account.chart.template,account.journal,account.move | - |
| l10n_sk | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | sk | 2 | account.chart.template,account.move,res.company | - |
| l10n_sn | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | sn | 0 | account.chart.template | - |
| l10n_syscohada | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | - | - | 0 | account.chart.template | - |
| l10n_td | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | td | 0 | account.chart.template | - |
| l10n_test_pos_qr_payment | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | - | - | 0 | - | - |
| l10n_tg | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | tg | 0 | account.chart.template | - |
| l10n_tn | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | tn | 0 | account.chart.template | - |
| l10n_tr | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | tr | 3 | account.chart.template,account.journal,account.move.line | - |
| l10n_tr_nilvera | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | - | 3 | account.journal,res.company,res.config.settings,res.partner | - |
| l10n_tr_nilvera_base_vat | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | T | - | 1 | res.partner | - |
| l10n_tr_nilvera_edispatch | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | - | tr | 1 | res.partner | - |
| l10n_tr_nilvera_einvoice | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | l10n_tr_nilvera | - | 2 | account.journal,account.move,account.move.send | account.move._post,account.move.button_draft |
| l10n_tr_nilvera_einvoice_extended | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | l10n_tr_nilvera_einvoice | - | 6 | account.chart.template,account.move,account.move.line,account.move.send,account.tax,res.company,res.config.settings,res.partner | - |
| l10n_tw | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | tw | 0 | account.chart.template | - |
| l10n_tw_edi_ecpay | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | tw | 5 | account.move,account.move.line,account.move.send,account.tax,res.company,res.config.settings,res.partner | account.move.button_draft |
| l10n_tw_edi_ecpay_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | - | 1 | account.tax | - |
| l10n_tw_edi_ecpay_website_sale | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | - | 1 | res.partner | - |
| l10n_tz_account | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | account | tz | 0 | account.chart.template | - |
| l10n_ua | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ua | 0 | account.chart.template | - |
| l10n_ug | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ug | 0 | account.chart.template | - |
| l10n_uk | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | gb | 0 | account.chart.template | - |
| l10n_us | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | - | us | 0 | res.partner.bank | - |
| l10n_us_account | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | account | us | 0 | account.chart.template | - |
| l10n_uy | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | uy | 4 | account.chart.template,account.move,account.tax,res.company,res.partner | account.move._get_last_sequence_domain,account.move._get_starting_sequence |
| l10n_uy_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | pos | T | - | 0 | - | - |
| l10n_uz | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | - | uz | 1 | account.chart.template,res.partner | - |
| l10n_ve | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | ve | 0 | account.chart.template | - |
| l10n_vn | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | vn | 1 | account.chart.template,account.move,res.partner.bank | - |
| l10n_vn_edi_viettel | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | - | vn | 3 | account.move,account.move.send,res.company,res.config.settings,res.partner | account.move._post,account.move.button_draft |
| l10n_vn_edi_viettel_pos | FUTURE OPTIONAL COUNTRY PACK | uninstalled | edi | T | vn | 3 | account.move,res.company,res.config.settings,res.partner | - |
| l10n_yt | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | yt | 0 | - | - |
| l10n_za | FUTURE OPTIONAL COUNTRY PACK | uninstalled | base country pack | account | za | 0 | account.chart.template | - |
| l10n_zm_account | FUTURE OPTIONAL COUNTRY PACK | uninstalled | other extension | account | zm | 1 | account.chart.template,account.move | account.move._get_name_invoice_report |

Rows: 227 packs.

## Appendix B. Thai tax set as loaded (DB configuration, invoice-side distribution)

| id | name | use | rate | group (DB) | price override | tax account | base grid label(s) | tax grid label | closing flag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 7% | purchase | 7.0000 | VAT 7% | - | 114200 | 6. Purchase amount (input-tax deduction) | 7. Input tax | t |
| 2 | 7% | sale | 7.0000 | VAT 7% | - | 213200 | 1. Sales amount | 5. Output tax | t |
| 3 | 0% | purchase | 0.0000 | WHT 1% | - | 114200 | 6. Purchase amount (input-tax deduction) | 7. Input tax | t |
| 4 | 0% | sale | 0.0000 | WHT 1% | - | 213200 | 1. Sales amount ; 2. Less sales subject to 0% tax rate | 5. Output tax | t |
| 5 | 0% EXEMPT | purchase | 0.0000 | WHT 1% | - | 114200 | 6. Purchase amount (input-tax deduction) | 7. Input tax | t |
| 6 | 0% EXEMPT | sale | 0.0000 | WHT 1% | - | 213200 | 1. Sales amount ; 3. Less exempted sales | 5. Output tax | t |
| 7 | 1% WH C T | purchase | -1.0000 | WHT 1% | - | 213302 | Income PND53 | PND53 | f |
| 8 | 2% WH C A | purchase | -2.0000 | WHT 2% | - | 213302 | Income PND53 | PND53 | f |
| 9 | 3% WH C S | purchase | -3.0000 | WHT 3% | - | 213302 | Income PND53 | PND53 | f |
| 10 | 5% WH C R | purchase | -5.0000 | WHT 5% | - | 213302 | Income PND53 | PND53 | f |
| 11 | 1% WH P T | purchase | -1.0000 | WHT 1% | - | 213301 | Income PND3 | PND3 | f |
| 12 | 2% WH P A | purchase | -2.0000 | WHT 2% | - | 213301 | Income PND3 | PND3 | f |
| 13 | 3% WH P S | purchase | -3.0000 | WHT 3% | - | 213301 | Income PND3 | PND3 | f |
| 14 | 5% WH P R | purchase | -5.0000 | WHT 5% | - | 213301 | Income PND3 | PND3 | f |
| 15 | 1% WH T | sale | -1.0000 | WHT 1% | tax_excluded | 114300 |  |  | f |
| 16 | 2% WH A | sale | -2.0000 | WHT 2% | tax_excluded | 114300 |  |  | f |
| 17 | 3% WH S | sale | -3.0000 | WHT 3% | tax_excluded | 114300 |  |  | f |
| 18 | 5% WH R | sale | -5.0000 | WHT 5% | tax_excluded | 114300 |  |  | f |

Note: ids 3-6 (0% and 0% EXEMPT) sit in group WHT 1% by the fallback; labels shortened in the two longest cells.

## 10. DB reconciliation summary (configuration only; source declared vs restored DB)

| module | source ACL | source rules | source groups | source crons | source automations | DB state | DB rows for the module (ACL / rules / groups / crons / automations) | other seeded configuration |
|---|---|---|---|---|---|---|---|---|
| l10n_th | 0 | 0 | 0 | 0 | 0 | installed | 0 / 0 / 0 / 0 / 0 | report records 3, columns 3, lines 24, expressions 24 (source = DB); QWeb views 3; report action 1; model-field rows 14, selection rows 3, model rows 5; chart records under the accounting module: accounts 147 (144 + 3 utility), taxes 18, tax groups 5, repartition lines 72, Thai tags 13 |
| account_qr_code_emv | 0 | 0 | 0 | 0 | 0 | installed | 0 / 0 / 0 / 0 / 0 | 1 view, 12 model-field rows, 1 selection row |
| base_vat | 0 | 0 | 0 | 1 (VIES update, daily) | 0 | uninstalled | 0 (no rows) | cron absent from DB |
| base_address_extended | 2 (city) | 0 | 0 | 0 | 0 | uninstalled | 0 | not applicable |
| l10n_account_withholding_tax | 2 | 0 | 0 | 0 | 0 | uninstalled | 0 | no flag column on the tax table |
| account_debit_note | 1 | 0 | 0 | 0 | 0 | uninstalled | 0 | not applicable |

Generic configuration read for context: payment methods 25 rows (1 PromptPay, inactive), providers all disabled except placeholder/demo entries, payment terms 10, reconcile models 2, account groups 0, fiscal positions 0, partner bank accounts 0, journals 7, languages active: en_US only.

## 11. Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U24-C001 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:17 | 'account_qr_code_emv', | FACT | always | — | The Thai package declares exactly two dependencies, the EMV payment-QR bridge and the core accounting application. | N-U24-014 |
| VDR-U24-C002 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:5 | 'countries': ['th'], | FACT | always | — | The manifest declares country th, which gates auto-install by company country. | N-U24-005 |
| VDR-U24-C003 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:20 | 'auto_install': ['account'], | FACT | always | — | The package is auto-installable when the accounting application is installed. | N-U24-005 |
| VDR-U24-C004 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:421 | module.country_ids & company_countries | FACT | button_install flow | — | An auto-install module that declares countries is installed only when at least one company belongs to one of those countries; this is the mechanism that restricts the Thai package to Thai-country databases. | N-U24-005 |
| VDR-U24-C005 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:83 | self.env.registry._auto_install_template = try_loading | FACT | module newly installed, company has no chart_template, company country equals template country or template is generic_coa | RT | On installation of a chart module the first template whose country equals the current company country is loaded on the current company at registry start; runtime order not executed. | N-U24-004 |
| VDR-U24-C006 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:74 | self.env.company.country_id.id and tvals['country_id'] | FACT | same | — | The guessed template is the first one whose country matches the company country or the generic chart. | N-U24-004 |
| VDR-U24-C007 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:9 | @template('th') | FACT | always | — | Template th is registered through the template decorator and returns template-level data (code digits and default account keys). | N-U24-001 |
| VDR-U24-C008 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:12 | 'code_digits': '6', | FACT | template th loaded | — | Account codes are normalised to six digits. | N-U24-002 |
| VDR-U24-C009 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:13 | 'property_account_receivable_id': 'l10n_th_account_112100', | FACT | template th loaded | — | Default receivable is account 112100 (Trade Receivables); default payable 212100, stock valuation 113100 and down payment 212400 follow on the next lines. | N-U24-006 |
| VDR-U24-C010 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:23 | 'account_fiscal_country_id': 'base.th', | FACT | template th loaded | — | Company data sets Thailand as fiscal country and the bank and cash code prefixes 11120 and 11110. | N-U24-006 |
| VDR-U24-C011 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:27 | 'account_default_pos_receivable_account_id' | FACT | template th loaded | — | Company data maps point-of-sale receivable, exchange gain and loss, bank suspense, early-payment discount loss and gain, cash-difference income and loss, transfer account, default expense and income accounts and default sale and purchase taxes to Thai accounts and taxes. | N-U24-006 |
| VDR-U24-C012 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:41 | 'tax_exigibility': 'True' | FACT | template th loaded | — | The company cash-basis feature flag is set by the template (value passed as the string True) although no shipped tax is cash-basis. | N-U24-017 |
| VDR-U24-C013 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:26 | 'transfer_account_code_prefix': 'l10n_th_account_11120' | OBSERVATION | DB company chart th | — | The transfer-account prefix is passed as an account template key rather than digits, and the company in the DB holds that literal text; the transfer account is set directly so the prefix is unused for creation. | N-U24-017 |
| VDR-U24-C014 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:145 | l10n_th_account_999999 | FACT | always | — | The account file ends at line 145 with the current-year earnings account 999999, so with the header line it holds 144 account rows. | N-U24-001 |
| VDR-U24-C015 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:1 | "id","code","name","account_type" | INFERENCE | always | — | Counted over the file: 42 expense, 22 asset_fixed, 15 asset_current, 13 liability_current, 12 expense_depreciation, 7 expense_direct_cost, 6 asset_non_current, 6 income_other, 4 asset_receivable, 4 income, 3 asset_cash, 3 liability_payable, 3 liability_non_current, 3 equity, 1 equity_unaffected; 30 rows reconcile True, 3 rows non_trade True, no row carries tag_ids. | N-U24-009 |
| VDR-U24-C016 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:2 | l10n_th_account_111100 | INFERENCE | always | — | First-digit distribution over the 144 codes: 1 assets 50, 2 liabilities 19, 3 equity 3, 4 income 10, 5 direct costs 7, 6 expenses 54, 9 one technical account; all codes are unique and six characters long. | N-U24-002 |
| VDR-U24-C017 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:18 | l10n_th_account_114300 | FACT | always | — | Account 114300 WHT Creditable is a current-asset type, reconcilable. | N-U24-010 |
| VDR-U24-C018 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:19 | l10n_th_account_114400 | FACT | always | — | Accounts 114400 VAT Receivable and 114401 WHT Receivable are receivable type with non_trade True; 213400 VAT Payable and 213500 WHT Payable are payable type, 213500 with non_trade True. | N-U24-010 |
| VDR-U24-C019 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:63 | l10n_th_account_213303 | FACT | always | — | Withholding liability accounts 213300 (PND 1), 213301 (PND 3), 213302 (PND 53), 213303 (PND 54) exist as current-liability accounts; 213100 and 114100 are the undue output and undue input VAT accounts. | N-U24-010 |
| VDR-U24-C020 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:123 | non_trade = fields.Boolean | FACT | always | — | The non_trade flag places an account under Non Trade Receivable or Payable in reports and filters instead of trade. | N-U24-010 |
| VDR-U24-C021 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:30 | 'account_journal_suspense_account_id': 'l10n_th_account_111201', | INFERENCE | template th loaded | — | Counting distinct account keys referenced in the template function, the tax file and the tax-group file gives 24 accounts plus the bank prefix key; the remaining 120 accounts are not wired by template data (cited lines: template_th.py 13-40, account.tax-th.csv, account.tax.group-th.csv). | N-U24-012 |
| VDR-U24-C022 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:3 | l10n_th_account_114200 | INFERENCE | template th | — | No shipped tax references the undue VAT accounts 114100 and 213100, the PND 1 account 213300 or the PND 54 account 213303; VAT taxes use 114200 and 213200, withholding taxes use 213301 and 213302 and sale-side withholding uses 114300. | N-U24-012 |
| VDR-U24-C023 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.asset-th.csv:2 | l10n_th_asset_land_improvements | FACT | always | — | An asset-category file with 12 rows (linear methods of 3, 5, 10 and 20 years) is shipped in the template folder. | N-U24-013 |
| VDR-U24-C024 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:23 | TEMPLATE_MODELS = ( | FACT | always | — | The core loader handles seven template models (account group, account, fiscal position, tax group, tax, journal, reconcile model); no asset model is in the list, and the Community source has no asset model. | N-U24-013 |
| VDR-U24-C025 | MCT-F03 | account/models/chart_template.py:1356 | No file %s found for template | OBSERVATION | DB chart th loaded | — | A missing template file is skipped silently; the Thai folder has no account group, fiscal position, journal or reconcile-model file, and the DB has 0 account groups, 0 fiscal positions, 7 journals and 2 reconcile models from the generic template. | N-U24-017 |
| VDR-U24-C026 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1337 | if key != 'id' and value | FACT | CSV loading | — | Empty CSV cells are skipped when records are built, which is why blank tax-group cells in the Thai tax file fall back to the default group lookup. | N-U24-017 |
| VDR-U24-C027 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:140 | def try_loading | FACT | always | — | try_loading takes template code, company and demo flag and delegates to the loader after warning about an unloaded registry. | N-U24-004 |
| VDR-U24-C028 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:184 | Only administrators can install chart templates | FACT | always | — | Loading a chart template raises an access error unless the user is a system administrator. | N-U24-016 |
| VDR-U24-C029 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:196 | we load everything in 'en_US' | FACT | always | — | All template records are loaded in en_US and translations applied afterwards (cross-reference U26 for the translation mechanism). | N-U24-016 |
| VDR-U24-C030 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:210 | reload_template = template_code == company.chart_template | FACT | always | — | Loading the same code again is a reload; for a different code on a company with no accounting the previous template records and moves are deleted before loading. | N-U24-011 |
| VDR-U24-C031 | MCT-F03 | account/models/chart_template.py:254 | for subsidiary in company.child_ids: | FACT | company has child companies | — | The loader is re-run for each child company with the same template (cross-reference U27/U28 for company structure). | N-U24-015 |
| VDR-U24-C032 | MCT-F03 | account/models/account_account.py:40 | code_store = fields.Char(company_dependent=True) | FACT | always | — | The account code is stored as a company-dependent value; DB shows code_store as a JSON map keyed by company id. | N-U24-015 |
| VDR-U24-C033 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:893 | def _setup_utility_bank_accounts | FACT | after template load | — | After data load the loader creates bank, outstanding receipts and outstanding payments accounts from the bank prefix; DB shows 111203 Bank, 111204 Outstanding Receipts, 111205 Outstanding Payments in addition to the 144 template accounts (147 total). | N-U24-007 |
| VDR-U24-C034 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:725 | sale_journal.default_account_id = company.income_account_id | FACT | after load | — | Sale and purchase journals receive the company default income and expense accounts (DB: INV 411100, BILL 511100). | N-U24-008 |
| VDR-U24-C035 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:712 | journal.suspense_account_id = journal.suspense_account_id | FACT | after load | — | Cash, bank and credit journals get the company suspense and cash-difference accounts (DB: BNK1 suspense 111201). | N-U24-007 |
| VDR-U24-C036 | FUNCTION MAPPING REQUIRED | l10n_th/__init__.py:6 | preserve_existing_tags_on_taxes(env, 'l10n_th') | FACT | module install | — | The post-install hook protects existing tax-tag records of the Thai package during upgrades. | N-U24-011 |
| VDR-U24-C037 | FUNCTION MAPPING REQUIRED | l10n_th/demo/demo_company.xml:31 | try_loading | FACT | demo data loaded | — | Demo data creates a TH Company and loads chart th on it; the restored DB has demo disabled. | N-U24-011 |
| VDR-U24-C038 | MCT-F03 | l10n_th/data/template/account.account-th.csv:3 | l10n_th_account_111200 | OBSERVATION | DB company chart th | — | DB: 147 account rows, all with an account-module external id; account types DB-side: 4 asset_cash (3 template plus bank), 17 asset_current (15 plus 2 outstanding), others equal to the file counts. | N-U24-009 |
| VDR-U24-C039 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:720 | company.currency_exchange_journal_id = self.ref | OBSERVATION | DB company chart th | — | DB journals: INV, BILL, MISC, EXCH, CABA, BNK1 (bank, default account 111203, manual in and out methods plus a checks method) and STJ inventory valuation; there is no cash journal although account 111100 Cash on Hand and the cash prefix exist. | N-U24-008 |
| VDR-U24-C040 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:1 | "name@th_TH" | FACT | always | — | Thai names and descriptions are carried as translation columns of the same CSV records (columns suffixed with the th_TH locale), keeping English as the stable source key (cross-reference U26). | N-U24-016 |
| VDR-U24-C041 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | legal review | — | UNKNOWN - EVIDENCE INSUFFICIENT: conformity of the Thai chart to statutory chart or financial-statement formats cannot be derived from source; resolve against an authoritative statutory source. | N-U24-018 |
| VDR-U24-C042 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:2 | tax_input_vat | FACT | template th | — | Input VAT 7 percent (purchase, group VAT 7%): base tagged 6. Purchase amount that is entitled to deduction of input tax from output tax in tax computation; tax line tagged 7. Input tax on account 114200 with tax-closing flag True; refund lines mirror. | N-U24-020 |
| VDR-U24-C043 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:6 | tax_output_vat | FACT | template th | — | Output VAT 7 percent (sale, group VAT 7%): base tagged 1. Sales amount; tax line tagged 5. Output tax on account 213200 with tax-closing flag True; refund lines mirror. | N-U24-020 |
| VDR-U24-C044 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:14 | tax_output_vat_0 | FACT | template th | — | Output VAT 0 percent base carries two labels joined by the delimiter (1. Sales amount and 2. Less sales subject to 0% tax rate); the tax line carries label 5. Output tax on account 213200. | N-U24-021 |
| VDR-U24-C045 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:22 | tax_output_vat_exempted | FACT | template th | — | Output VAT 0% EXEMPT base carries 1. Sales amount and 3. Less exempted sales; the tax line carries label 5. Output tax on account 213200. | N-U24-021 |
| VDR-U24-C046 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:10 | tax_input_vat_0 | FACT | template th | — | Input VAT 0 percent uses the same two input labels (6 and 7) and account 114200 as the 7 percent input tax. | N-U24-034 |
| VDR-U24-C047 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:18 | tax_input_vat_exempted | FACT | template th | — | Input VAT 0% EXEMPT also uses the same input labels (6 and 7) and account 114200; only its name and description differ from the 0 percent input tax. | N-U24-034 |
| VDR-U24-C048 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:10 | tax_input_vat_0 | OBSERVATION | DB company chart th | — | The 0 percent and exempt rows (sale and purchase) give no tax group cell; DB assigns all four the group named WHT 1%, while the 7 percent VAT taxes use group VAT 7%. | N-U24-033 |
| VDR-U24-C049 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:316 | ('country_id', '=', country.id), | FACT | tax created without group | — | A tax without a group takes the first group of its country (then the first group without country), which explains the fallback to the first Thai group. | N-U24-033 |
| VDR-U24-C050 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2824 | return tax_data['tax'].tax_group_id if tax_data else None | FACT | document totals | — | Document tax totals are aggregated per tax group, so group membership decides the heading under which a tax is shown. | N-U24-033 |
| VDR-U24-C051 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax.group-th.csv:6 | "tax_group_vat_7","VAT 7%" | FACT | template th | — | Five Thai tax groups: WHT 1%, 2%, 3%, 5% (payable 213500, receivable 114401) and VAT 7% (payable 213400, receivable 114400). | N-U24-027 |
| VDR-U24-C052 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:372 | "tax_payable_account_id", "tax_receivable_account_id" | INFERENCE | Community only | — | Within Community the group payable and receivable accounts are consumed only by the foreign-tax instantiation helper (chart_template.py lines 372 and 996), not by any posting routine; the field help names the Tax Closing Entry as their purpose. | N-U24-027 |
| VDR-U24-C053 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5360 | rep_line.account_id.internal_group not in ('income', 'expense') | FACT | always | — | The tax-closing flag defaults to True for tax-type distribution lines whose account is not income or expense; the Thai file sets it explicitly True for VAT lines and False for withholding lines. | N-U24-027 |
| VDR-U24-C054 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2337 | if tax.analytic or not tax_rep.use_in_tax_closing | FACT | always | — | In Community the flag changes only whether the analytic distribution is copied onto the tax line (and a reporting query); no closing entry routine uses it. | N-U24-027 |
| VDR-U24-C055 | FUNCTION MAPPING REQUIRED | account/models/company.py:85 | automatically set when the tax closing | FACT | always | — | The tax lock date help text names a tax closing entry, but the Community source has no routine that creates such an entry (grep for closing entry and periodicity outside country packs returned nothing in account). | N-U24-027 |
| VDR-U24-C056 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1130 | return raw_base * self.amount / 100.0 | FACT | percent tax excluded from price | — | A percent tax excluded from the price is computed as base times amount over 100, so a negative percentage yields a negative tax amount without special handling. | N-U24-025 |
| VDR-U24-C057 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:22 | tax_output_vat_exempted | OBSERVATION | DB company chart th | — | DB holds 18 taxes, all percent type, all sequence 1, all on_invoice exigibility, none with include_base_amount, all with is_base_affected True, none with a cash-basis transition account; 72 repartition lines (4 per tax). | N-U24-025 |
| VDR-U24-C058 | FUNCTION MAPPING REQUIRED | account/models/product.py:44 | default=lambda self: self.env.companies.account_sale_tax_id | FACT | product created | — | Product sales taxes default to the company default sale tax (output VAT 7 percent here) and supplier taxes to the company default purchase tax. | N-U24-023 |
| VDR-U24-C059 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:33 | 'account_sale_tax_id': 'tax_output_vat', | FACT | template th loaded | — | The Thai template sets the default sale tax to output VAT 7 percent and the default purchase tax to input VAT 7 percent. | N-U24-023 |
| VDR-U24-C060 | FUNCTION MAPPING REQUIRED | account/models/company.py:275 | default='tax_excluded', | FACT | always | — | Company price-include setting defaults to tax excluded; DB value is tax_excluded and the Thai template does not change it. | N-U24-024 |
| VDR-U24-C061 | FUNCTION MAPPING REQUIRED | account/models/company.py:328 | Cannot change Price Tax computation method | FACT | company already invoicing | — | The price-include setting cannot be changed once the company has started invoicing. | N-U24-024 |
| VDR-U24-C062 | FUNCTION MAPPING REQUIRED | account/models/company.py:130 | ('round_globally', 'Round per Tax'), | FACT | always | — | Tax rounding defaults to round_globally (labelled Round per Tax); DB value is round_globally. | N-U24-024 |
| VDR-U24-C063 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:58 | tax_excluded | FACT | template th | — | Only the four sale-side withholding taxes carry the price-excluded override; no Thai VAT or purchase withholding tax carries an override. | N-U24-025 |
| VDR-U24-C064 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:956 | tax.price_include == batch[0].price_include | INFERENCE | company switched to tax included | RT | Taxes are batched only when they share the price-include state, so under an included default the purchase VAT and withholding taxes would form one batch while the overridden sale withholding taxes would not; numeric effect not executed. | N-U24-035 |
| VDR-U24-C065 | MCT-F03 | account/models/partner.py:277 | all_auto_apply_fpos = self.search( | FACT | always | — | A fiscal position is resolved from a manual partner assignment first, then from automatic positions matching zip, state, country or country group; with no positions defined (DB: 0) no mapping occurs. | N-U24-029 |
| VDR-U24-C066 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1356 | No file %s found for template | OBSERVATION | DB chart th | — | The Thai folder ships no fiscal position file and the company has no domestic fiscal position; export, zero-rate and exempt supplies must be taxed by explicit selection or user-created positions. | N-U24-029 |
| VDR-U24-C067 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1850 | move.company_id.display_invoice_tax_company_currency | FACT | sale document, currency differs from company currency, taxes present | — | Tax totals are flagged for display in company currency only for sale documents whose currency differs from the company currency; the company setting defaults to True and DB shows True (cross-reference U25 for multi-currency). | N-U24-030 |
| VDR-U24-C068 | FUNCTION MAPPING REQUIRED | base/data/res_currency_data.xml:1499 | <field name="currency_unit_label">Baht</field> | OBSERVATION | DB | — | Thai baht is the company currency in the DB, with two decimals and rounding 0.01; unit label Baht and subunit label Satang come from base currency data. | N-U24-030 |
| VDR-U24-C069 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:4 | <field name="name">Tax Report</field> | FACT | module data | — | A Thailand tax report definition named Tax Report is attached to the generic tax report as variant, country Thailand, availability condition country, allow_foreign_vat True. | N-U24-026 |
| VDR-U24-C070 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:73 | <field name="formula">-5. Output tax</field> | FACT | module data | — | Output sales and output-tax lines read tags with a leading minus (reversed sign) while input lines read tags without it. | N-U24-026 |
| VDR-U24-C071 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:126 | OUTPUTTAX_TAX.balance - INPUTTAX_TAX.balance | FACT | module data | — | Line 8 tax payable is output tax minus input tax with if_above(THB(0)); line 9 excess is input minus output with the same subformula. | N-U24-026 |
| VDR-U24-C072 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:127 | if_above(THB(0)) | FACT | module data | — | The positive-part subformulas hard-code the THB currency literal. | N-U24-036 |
| VDR-U24-C073 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:152 | most_recent | FACT | module data | — | Line 10 excess carried forward uses an external-value expression (most_recent, previous return period) plus a tag; line 12 net excess is the carryover target. | N-U24-026 |
| VDR-U24-C074 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:273 | <field name="formula">SUR53</field> | INFERENCE | template th | — | Surcharge tags SUR53 and SUR3 and the tag 10. Excess tax payment carried forward from last period exist in report definitions but no shipped tax repartition line uses them (DB: 13 Thai tags; the tax file uses the other 10). | N-U24-036 |
| VDR-U24-C075 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:45 | _name = 'account.report' | INFERENCE | Community only | — | Community defines the report, line, column and expression models with ACL rows (14 DB rows) but DB has 0 window actions and 0 views on them and the source has no method that evaluates the expressions; a grep for get_report_information found only a foreign-pack test. | N-U24-031 |
| VDR-U24-C076 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Enterprise reporting add-on | RT | UNKNOWN - EVIDENCE INSUFFICIENT: how the Thai report definitions would be rendered, which period scope applies and how carryover is stored are not in Community source; resolve by reading the reporting add-on that evaluates account.report (not in scope). | N-U24-037 |
| VDR-U24-C077 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5336 | tag_ids = fields.Many2many(string="Tax Grids" | OBSERVATION | DB company chart th | — | DB: 13 account tags with country Thailand and applicability taxes (grids 1,2,3,5,6,7,10, Income PND53, PND53, SUR53, Income PND3, PND3, SUR3). | N-U24-022 |
| VDR-U24-C078 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5339 | sequence = fields.Integer(string="Sequence", default=1, | FACT | always | — | Invoice and refund repartition lines are matched by order, so the Thai file lists base then tax in the same order for both. | N-U24-032 |
| VDR-U24-C079 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:7 | l10n_th_account_213200 | INFERENCE | template th | RT | A standard Thai sale of 100 with Output VAT 7 percent yields (by repartition lines) receivable 107, revenue 100 on the product income account and output VAT 7 on 213200; a purchase mirrors with input VAT on 114200 and payable 107; numeric posting not executed. | N-U24-020 |
| VDR-U24-C080 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:26 | "tax_wht_co_1","1% WH C T" | FACT | template th | — | Company-payee withholding taxes tax_wht_co_1, 2, 3, 5 are purchase taxes with amounts -1, -2, -3, -5, groups tax_group_1/2/3/5, base label Income PND53 and tax label PND53 on account 213302, refund lines mirrored. | N-U24-039 |
| VDR-U24-C081 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:27 | "PND53","l10n_th_account_213302","False" | FACT | template th | — | The tax distribution lines of the company-payee withholding taxes carry use_in_tax_closing False. | N-U24-045 |
| VDR-U24-C082 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:42 | "tax_wht_pers_1","1% WH P T" | FACT | template th | — | Individual-payee withholding taxes tax_wht_pers_1, 2, 3, 5 use labels Income PND3 and PND3 on account 213301. | N-U24-039 |
| VDR-U24-C083 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:58 | "tax_wht_income_1","1% WH T" | FACT | template th | — | Sale-side withholding taxes tax_wht_income_1, 2, 3, 5 are sale taxes with negative amounts, price_include_override tax_excluded, no tag cells, tax distribution on account 114300 with closing flag False. | N-U24-040 |
| VDR-U24-C084 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:26 | Company Withholding Tax 1% (Transportation) | FACT | template th | — | The category wording (Transportation, Advertising, Service, Rental) is carried in the tax description text, an English source string with a th_TH translation column (translatable text, not a requirement). | N-U24-039 |
| VDR-U24-C085 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:164 | tax_exigibility = fields.Selection( | OBSERVATION | DB company chart th | — | DB: all 18 Thai taxes have tax_exigibility on_invoice, so withholding is booked at document posting. | N-U24-042 |
| VDR-U24-C086 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:148 | include_base_amount = fields.Boolean | OBSERVATION | DB company chart th | — | DB: no Thai tax has include_base_amount set and all have sequence 1, so no tax changes the base of another; withholding is computed on the untaxed amount (inference from engine batching, numeric result RT). | N-U24-043 |
| VDR-U24-C087 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax.group-th.csv:2 | "tax_group_1","WHT 1%" | FACT | template th | — | Withholding groups WHT 1, 2, 3, 5 percent point to payable 213500 and receivable 114401. | N-U24-044 |
| VDR-U24-C088 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:18 | l10n_th_account_114300 | OBSERVATION | DB company chart th | — | DB: account 114300 is of type asset_current (not receivable); an earlier candidate source map described it as receivable. | N-U24-040 |
| VDR-U24-C089 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:228 | <field name="name">PND53</field> | FACT | module data | — | PND53 report: Total Income (tag Income PND53), Total Remittance (tag PND53), Surcharge (tag SUR53), Total. | N-U24-046 |
| VDR-U24-C090 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:292 | <field name="name">PND3</field> | FACT | module data | — | PND3 report: Total Income (tag Income PND3), Total Remittance (tag PND3), Surcharge (tag SUR3), Total. | N-U24-046 |
| VDR-U24-C091 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:1 | "id","name","description","invoice_label" | INFERENCE | template th | — | The tax file header has fiscal_position_ids and original_tax_ids columns but every row leaves them empty, so no mapping selects company or individual withholding from the partner. | N-U24-052 |
| VDR-U24-C092 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:26 | "tax_wht_co_1","1% WH C T" | INFERENCE | company switched to tax included | RT | The purchase withholding rows leave price_include_override empty, so they follow the company price-include setting, while sale-side rows are fixed to tax_excluded. | N-U24-053 |
| VDR-U24-C093 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:60 | l10n_th_account_213300 | INFERENCE | template th | — | Accounts 213300 (PND 1) and 213303 (PND 54) have no tax record pointing to them; no Thai tax models payees in those categories. | N-U24-055 |
| VDR-U24-C094 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/__manifest__.py:7 | 'depends': ['account'], | FACT | add-on installed | — | The withholding-on-payment add-on depends only on account; it is independent of the Thai package, whose manifest has no reference to it. | N-U24-051 |
| VDR-U24-C095 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/models/account_tax.py:14 | string="Withhold On Payment" | FACT | add-on installed | — | The add-on adds the Withhold On Payment flag: the tax does not affect accounts until payment registration. | N-U24-047 |
| VDR-U24-C096 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/models/account_tax.py:46 | tax.amount_type in ['group', 'division'] | FACT | add-on installed | — | A flagged tax may not be a group or division type; the onchange forces on-invoice exigibility and price-excluded and clears the flag when the amount is not negative. | N-U24-048 |
| VDR-U24-C097 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/models/account_tax.py:78 | base_line['filter_tax_function'] = lambda t: not t.is_withholding_tax_on_payment | FACT | add-on installed | — | Flagged taxes are excluded from the document tax computation unless the payment flow requests them. | N-U24-047 |
| VDR-U24-C098 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:284 | def _prepare_move_withholding_lines | FACT | always (core hook) | — | The core payment model defines the hook for withholding lines (empty without the add-on). | N-U24-047 |
| VDR-U24-C099 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/models/account_withholding_line.py:348 | For an invoice for 1000 | FACT | add-on installed | — | Documented result for 1000 at 10 percent: outstanding 900, receivable -1000, tax withheld 100, base 1000, base counterpart 1000. | N-U24-047 |
| VDR-U24-C100 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/models/account_withholding_line.py:366 | Please enter the withholding number | FACT | add-on installed | — | A withholding line without a name and without a sequence on the tax raises a UserError; otherwise the number comes from the tax sequence. | N-U24-048 |
| VDR-U24-C101 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/security/ir.model.access.csv:3 | access_account_payment_withholding_line | FACT | add-on installed | — | The add-on declares 2 ACL rows (register-wizard line and payment line) for the invoicing group, 0 record rules, 0 groups, 0 crons. | N-U24-049 |
| VDR-U24-C102 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/__manifest__.py:3 | 'name': 'Withholding Tax on Payment', | OBSERVATION | DB | — | DB: add-on state uninstalled, no external ids, no flag column on the tax table; so the 18 Thai taxes are all ordinary document-time taxes. | N-U24-049 |
| VDR-U24-C103 | FUNCTION MAPPING REQUIRED | l10n_ph/__manifest__.py:14 | l10n_account_withholding_tax | OBSERVATION | source only | — | FUTURE OPTIONAL COUNTRY PACK: manifests of l10n_kh, l10n_ph and l10n_sa_withholding_tax depend on the add-on (mechanical grep of manifests); no rules studied. | N-U24-051 |
| VDR-U24-C104 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | — | NOT PRESENT IN COMMUNITY SOURCE: withholding certificate (Thai 50 Tawi style), withholding return filing format, creditable-withholding settlement. Search: grep -rIil -E 'withholding certificate / certificate of withholding / tawi / e-tax / pnd' over odoo/addons (excluding l10n_th, i18n, tests) returned only unrelated country data; the add-on receipt template shows a withholding table but no certificate. | N-U24-056 |
| VDR-U24-C105 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7373 | def _get_name_invoice_report | FACT | always | — | The core document selector returns account.report_invoice_document and states that localisations may override it. | N-U24-062 |
| VDR-U24-C106 | FUNCTION MAPPING REQUIRED | l10n_th/models/account_move.py:10 | return 'l10n_th.report_invoice_document' | FACT | company account_fiscal_country_id code is TH | — | The Thai override returns the Thai invoice document when the company fiscal country is Thailand, else defers to super. | N-U24-062 |
| VDR-U24-C107 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:672 | o._get_name_invoice_report() == 'account.report_invoice_document' | FACT | always | — | The core invoice report template dispatches on the selector value and renders the standard document only for the standard name. | N-U24-062 |
| VDR-U24-C108 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:42 | o._get_name_invoice_report() == 'l10n_th.report_invoice_document' | FACT | always | — | The Thai package adds the elif branch to the core invoice report so print actions (including Studio-based ones) reach the Thai document. | N-U24-062 |
| VDR-U24-C109 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:15 | <t name="invoice_title">Tax Invoice</t> | FACT | Thai variant, posted out_invoice | — | The Thai template replaces the element named invoice_title with the fixed text Tax Invoice. | N-U24-057 |
| VDR-U24-C110 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:65 | <t name="invoice_title">Invoice</t> | FACT | always | — | The replaced element is the posted out_invoice title only; draft (Draft Invoice), cancelled, out_refund (Credit Note) and vendor titles are separate named elements and are untouched. | N-U24-067 |
| VDR-U24-C111 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:74 | <t name="credit_note_title">Credit Note</t> | FACT | always | — | Posted customer credit notes print the standard title Credit Note, also in the Thai variant. | N-U24-060 |
| VDR-U24-C112 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:62 | <t t-set="layout_document_title"> | INFERENCE | always | — | The title block (lines 62-120) has branches for out_invoice, out_refund, in_invoice and in_refund only; out_receipt and in_receipt have none, so receipts get no type title. | N-U24-060 |
| VDR-U24-C113 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:150 | ('out_receipt', 'Sales Receipt'), | FACT | always | — | Move types out_receipt (Sales Receipt) and in_receipt (Purchase Receipt) exist in core. | N-U24-060 |
| VDR-U24-C114 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:777 | self.payment_receipt_title = _('Payment Receipt') | FACT | always | — | The payment receipt document has the generic title Payment Receipt and exposes a hook to override it; the Thai package does not override it. | N-U24-060 |
| VDR-U24-C115 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:5 | o.partner_id.l10n_th_branch_name | FACT | Thai variant | — | The branch name is rendered after the partner vat in the three address layouts (not same as shipping, same as shipping, no shipping). | N-U24-057 |
| VDR-U24-C116 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:21 | id="partner_vat_address_not_same_as_shipping" | FACT | partner has vat | — | The buyer tax identifier is printed only when the partner has a vat value, labelled with the country vat_label or Tax ID. | N-U24-064 |
| VDR-U24-C117 | FUNCTION MAPPING REQUIRED | web/views/report_templates.xml:339 | <span t-esc="company.vat">US12345671</span> | FACT | company has vat | — | The seller tax identifier is printed by the shared company header and footer, not by the invoice document; nothing prints a seller branch. | N-U24-064 |
| VDR-U24-C118 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:36 | <field name="domain">[( | FACT | always | — | The Commercial Invoice report action is bound to account.move with domain country_code TH and journal type sale. | N-U24-059 |
| VDR-U24-C119 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:23 | <t t-call="account.report_invoice_document" t-lang="lang"/> | FACT | always | — | The Commercial Invoice renders the standard invoice document with lang set to the partner language, hence the generic title Invoice. | N-U24-059 |
| VDR-U24-C120 | FUNCTION MAPPING REQUIRED | l10n_th/models/ir_actions_report.py:13 | Only invoices could be printed. | FACT | commercial invoice report | — | A pre-render guard raises UserError unless every record is an invoice or receipt of either side. | N-U24-070 |
| VDR-U24-C121 | FUNCTION MAPPING REQUIRED | base/models/ir_actions_report.py:192 | the action will only appear | FACT | always | — | A report action domain only controls on which records the print action appears. | N-U24-068 |
| VDR-U24-C122 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:22 | <t t-set="lang" t-value="o.partner_id.lang"/> | FACT | Commercial Invoice | — | The Commercial Invoice picks its language from the customer partner; the Thai tax-invoice branch of the core report does the same through the lang variable of the core template. | N-U24-062 |
| VDR-U24-C123 | FUNCTION MAPPING REQUIRED | l10n_th/i18n/th.po:128 | msgid "Tax Invoice" | FACT | th_TH language loaded | — | The Thai rendering of Tax Invoice is a translation catalogue entry keyed on the English source (also Branch %(code)s and Headquarter); the English text is the canonical key. | N-U24-062 |
| VDR-U24-C124 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4294 | starting_sequence = "%s/%s/%s" % (self.journal_id.code, year_part | FACT | sale, bank, cash, credit journals | — | Sales-side documents start from journal code / year part / 00000 (annual); other journals use code / year / month / 0000. | N-U24-063 |
| VDR-U24-C125 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4277 | year_part = "%04d" % move_date.year | FACT | always | — | The year in the sequence prefix is the Gregorian calendar year of the document date; for a staggered fiscal year it becomes a two-digit span. | N-U24-071 |
| VDR-U24-C126 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4308 | starting_sequence = "R" + starting_sequence | FACT | journal refund_sequence, out_refund or in_refund | — | Credit notes get the prefix R when the journal has a dedicated credit-note sequence; the journal flag defaults to True for sale and purchase journals (account_journal.py:706) and DB INV and BILL journals have it True. | N-U24-063 |
| VDR-U24-C127 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4310 | starting_sequence = "P" + starting_sequence | FACT | journal payment_sequence | — | Payments get the prefix P on journals with a dedicated payment sequence (DB: BNK1 True). | N-U24-063 |
| VDR-U24-C128 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:16 | @api.constrains('proxy_type', 'proxy_value', 'partner_id') | INFERENCE | always | — | The only constraint declared by the Thai package concerns bank proxy fields; no check on invoice posting, partner tax identifier, branch or seller data exists in its five Python files. | N-U24-064 |
| VDR-U24-C129 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2220 | move.amount_total_words = move.currency_id.amount_to_text | FACT | always | — | Core computes the amount in words from the currency amount_to_text and strips commas. | N-U24-065 |
| VDR-U24-C130 | FUNCTION MAPPING REQUIRED | account/models/company.py:152 | display_invoice_amount_total_words = fields.Boolean | FACT | always | CONTRA | CONTRA with the unit brief that listed amount in words as a Thai gap: a generic switch exists; it has no default, the Thai template does not set it (several foreign packs do), and DB shows the flag True with the setter not identifiable from source. | N-U24-065 |
| VDR-U24-C131 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:410 | t-if="o.company_id.display_invoice_amount_total_words" | FACT | flag on | — | The invoice layout prints Total amount in words only when the company flag is on. | N-U24-065 |
| VDR-U24-C132 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:181 | return num2words(number, lang='en').title() | FACT | num2words lacks the language | RT | amount_to_text uses the external num2words library with the user language iso code and falls back to English on NotImplementedError; whether it supports Thai depends on the installed library version (not in source tree). | N-U24-065 |
| VDR-U24-C133 | FUNCTION MAPPING REQUIRED | base/data/res_currency_data.xml:1500 | <field name="currency_subunit_label">Satang</field> | FACT | always | — | Currency labels for baht are Baht and Satang. | N-U24-065 |
| VDR-U24-C134 | FUNCTION MAPPING REQUIRED | account_debit_note/__manifest__.py:15 | 'depends': ['account'], | FACT | add-on | — | The debit-note add-on depends only on account and is not part of the Thai package (DB: uninstalled, 1 ACL row in source, 0 rules, 0 crons). | N-U24-066 |
| VDR-U24-C135 | FUNCTION MAPPING REQUIRED | account_debit_note/wizard/account_debit_note.py:35 | You can only debit posted moves. | FACT | add-on | — | The wizard refuses non-posted moves, moves already linked to a debit note and move types other than customer or vendor invoice or credit note. | N-U24-070 |
| VDR-U24-C136 | FUNCTION MAPPING REQUIRED | account_debit_note/models/account_move.py:50 | starting_sequence = "D" + starting_sequence | FACT | journal debit_sequence, debit_origin_id set | — | A dedicated debit-note sequence prefixes D; the journal flag defaults True for sale and purchase journals. | N-U24-066 |
| VDR-U24-C137 | FUNCTION MAPPING REQUIRED | account_debit_note/views/report_invoice.xml:8 | <t t-if="o.debit_origin_id">Debit Note</t> | FACT | add-on | — | The add-on rewrites the core invoice_title element to Debit Note when a document has an original, and similarly for draft, cancelled and proforma titles. | N-U24-066 |
| VDR-U24-C138 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:14 | <t name="invoice_title" position="replace"> | INFERENCE | both modules installed | RT | The Thai template is a primary inherit of the core document and replaces the same invoice_title element after parent extensions are applied, so a posted Thai debit note is expected to print Tax Invoice; not executed (earlier U23 RT item). | N-U24-069 |
| VDR-U24-C139 | FUNCTION MAPPING REQUIRED | account_debit_note/wizard/account_debit_note.py:69 | default_values['line_ids'] = [(5, 0, 0)] | FACT | copy_lines False | — | Unless copy-lines is chosen the debit note starts with no lines; the default values (lines 59-69) also link the original and clear payment terms. | N-U24-066 |
| VDR-U24-C140 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | — | NOT PRESENT IN COMMUNITY SOURCE: abbreviated tax invoice, combined tax invoice and receipt, seller branch printing, Buddhist-era year printing, mandatory-field enforcement for Thai tax invoices. Search: grep -rIil for 'abbreviated tax invoice / simplified tax invoice / buddhist / tax invoice' over odoo/addons excluding l10n_th: only foreign packs and an emoji table matched; no field-level check exists in the five Thai Python files. | N-U24-073 |
| VDR-U24-C141 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_partner.py:9 | l10n_th_branch_name = fields.Char(compute="_compute_l10n_th_branch_name") | FACT | module installed | — | The only partner field added is the non-stored computed char l10n_th_branch_name (DB shows it on res.partner and, through delegation, res.users). | N-U24-075 |
| VDR-U24-C142 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_partner.py:13 | partner.country_code != 'TH': | FACT | always | — | The branch name is empty unless the partner is a company whose country code is TH. | N-U24-075 |
| VDR-U24-C143 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_partner.py:18 | "Headquarter") | FACT | company partner in TH | — | Value is the translatable Branch %(code)s built from company_registry, or Headquarter when the registry is empty. | N-U24-075 |
| VDR-U24-C144 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:241 | company_registry = fields.Char(string="Company ID" | FACT | always | — | The registration field is the generic Company ID char; the Thai package does not relabel it (no registry-label override). | N-U24-086 |
| VDR-U24-C145 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:491 | self.vat_label = self.env.company.country_id.vat_label or _("Tax ID") | FACT | always | — | The identifier label is the company country vat_label, else Tax ID; DB country Thailand has no vat_label. | N-U24-082 |
| VDR-U24-C146 | FUNCTION MAPPING REQUIRED | account/models/partner.py:873 | return vat, country and country.code | FACT | base_vat not installed | — | The core _run_vat_checks returns the vat unchanged and the country code; with base_vat uninstalled (DB) no identifier validation occurs. | N-U24-077 |
| VDR-U24-C147 | FUNCTION MAPPING REQUIRED | account/models/partner.py:14 | from odoo.addons.base_vat.models.res_partner import _ref_vat | OBSERVATION | always | — | Core imports the reference-format table from the validation add-on module path even when the add-on is not installed, so placeholders can use its table (Thai example 1234545678781). | N-U24-078 |
| VDR-U24-C148 | FUNCTION MAPPING REQUIRED | base_vat/__manifest__.py:37 | 'depends': ['account'], | FACT | add-on | — | The validation add-on depends only on account; DB state uninstalled (source: 0 ACL, 1 cron, 0 rules). | N-U24-082 |
| VDR-U24-C149 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:895 | check_func = stdnum.util.get_cc_module('th', 'tin').is_valid | FACT | add-on installed, partner country TH | — | Thai identifiers are validated by the th tin module of the python-stdnum library (external). | N-U24-078 |
| VDR-U24-C150 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:80 | 'th': '1234545678781', | FACT | add-on installed | — | The expected-format example for th is a 13-digit number, shown in the validation error. | N-U24-078 |
| VDR-U24-C151 | FUNCTION MAPPING REQUIRED | base_vat/tests/test_vat_numbers.py:240 | for tin in ['1234545678781', '1-2345-45678-78-1', '0-99-4-000-61772-1']: | FACT | add-on tests | — | Add-on tests accept compact and hyphenated 13-digit numbers with a valid last digit and reject a wrong last digit and a letter in the first position. | N-U24-078 |
| VDR-U24-C152 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:146 | if not validation or self.env.context.get('no_vat_validation'): | FACT | add-on installed | — | Validation is skipped when validation is False or the context key no_vat_validation is set; 'setnull' returns an empty value instead of raising. | N-U24-079 |
| VDR-U24-C153 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:166 | def _inverse_vat(self): | FACT | add-on installed | — | The vat and country_id fields use an inverse that runs the check on every write; the onchange runs it without raising. | N-U24-079 |
| VDR-U24-C154 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:117 | To explicitly indicate no (valid) VAT | FACT | add-on installed | — | A one-character identifier other than / raises an error under validation error mode; / is the explicit no-identifier marker. | N-U24-079 |
| VDR-U24-C155 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:218 | def _split_vat(self, vat): | FACT | add-on installed | — | A leading two-letter alphabetic prefix is treated as a country prefix; a number starting with digits (Thai form) has no prefix and is checked against the partner country. | N-U24-078 |
| VDR-U24-C156 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:948 | stdnum_vat_fix_func = getattr(stdnum.util.get_cc_module(country_code, 'vat'), 'compact', None) | INFERENCE | add-on installed | RT | Normalisation uses a compact function only if the library has a th vat module; whether th has one is not determinable here, so the stored form is UNKNOWN. | N-U24-085 |
| VDR-U24-C157 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:487 | partner.same_company_registry_partner_id = bool(partner.company_registry) | FACT | always | — | Same-registry detection searches other partners (not children) with an equal company_registry in the company scope; same-vat detection is parallel; both feed a warning alert. | N-U24-080 |
| VDR-U24-C158 | FUNCTION MAPPING REQUIRED | base/views/res_partner_views.xml:109 | name="warning_tax" | FACT | form edit mode | — | The duplicate detection is displayed as a warning alert on the partner form, not a constraint. | N-U24-080 |
| VDR-U24-C159 | FUNCTION MAPPING REQUIRED | account/models/partner.py:875 | def _get_vat_required_valid | FACT | fiscal position vat_required | — | A fiscal position can require a partner vat; the core hook returns whether vat is set and is not / (VIES refinement exists only in the add-on for EU contexts). | N-U24-082 |
| VDR-U24-C160 | FUNCTION MAPPING REQUIRED | base/data/res_country_data.xml:1411 | %(street)s\n%(street2)s\n%(city)s\n%(state_name)s %(zip)s\n%(country_name)s | FACT | always | — | Country Thailand uses the generic address format with street, street2, city, state, zip and country; DB has 77 Thai states. | N-U24-081 |
| VDR-U24-C161 | FUNCTION MAPPING REQUIRED | base_address_extended/__manifest__.py:23 | 'depends': ['base', 'contacts'], | FACT | add-on | — | The extended-address add-on depends on base and contacts and, per its description, is primarily for electronic-invoice city codes; DB uninstalled. | N-U24-082 |
| VDR-U24-C162 | FUNCTION MAPPING REQUIRED | base_address_extended/models/res_partner.py:37 | partner.update(tools.street_split(partner.street)) | FACT | add-on installed | — | The add-on stores street_name, street_number and street_number2 computed by splitting the street value. | N-U24-081 |
| VDR-U24-C163 | FUNCTION MAPPING REQUIRED | base_address_extended/models/res_country.py:10 | enforce_cities = fields.Boolean( | FACT | add-on installed | — | A country can enforce choosing a city from a city list; the add-on ships no Thai city data (no data directory). | N-U24-081 |
| VDR-U24-C164 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:42 | tax_wht_pers_1 | INFERENCE | template th | — | Individual and company payee variants are separate taxes; the partner type is not read by any Thai code, so selection is manual or by user-created positions. | N-U24-083 |
| VDR-U24-C165 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | legal review | — | UNKNOWN - EVIDENCE INSUFFICIENT: statutory format of Thai taxpayer and branch identifiers; stdnum th.tin rules (library is outside the source tree); resolve by reading the library version used at runtime and an authoritative statute. | N-U24-087 |
| VDR-U24-C166 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/__manifest__.py:11 | 'depends': ['account'], | FACT | always | — | The EMV bridge depends on account only and is installed in the DB (0 ACL, 0 rules, 0 crons, 1 view, 12 fields). | N-U24-088 |
| VDR-U24-C167 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:124 | rslt.append(('emv_qr', _("EMV Merchant-Presented QR-code"), 30)) | FACT | bridge installed | — | The bridge registers the emv_qr method with sequence 30. | N-U24-092 |
| VDR-U24-C168 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:75 | (1, '12'), | FACT | emv_qr | — | Payload tags: 0 format 01, 1 initiation 12 (dynamic), merchant account tag, 52 category, 53 currency, 54 amount, 58 country, 59 name, 60 city, 62 additional data, then 6304 and CRC-16. | N-U24-088 |
| VDR-U24-C169 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:40 | def _get_crc16 | FACT | emv_qr | — | CRC-16 polynomial 0x1021 with initial value 0xFFFF; the CRC is computed over the UTF-8 encoded string. | N-U24-100 |
| VDR-U24-C170 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:22 | return f'{header:02}{len(str(value)):02}{value}' | FACT | emv_qr | — | Each field is encoded as two-digit tag, two-digit length of the string in characters, then the value. | N-U24-100 |
| VDR-U24-C171 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:91 | crc = self._get_crc16(bytes(qr_code_str, 'utf-8')) | INFERENCE | non-ASCII merchant text | RT | Length counts characters but the CRC covers bytes; Thai script in merchant name or city would diverge (lines 21-22 and 91); not executed. | N-U24-100 |
| VDR-U24-C172 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:67 | merchant_name = self.partner_id.name and | FACT | emv_qr | — | Merchant name is the holder partner name with accents removed, cut to 25 characters, else NA; city is cut to 15; _remove_accents does not transliterate non-Latin scripts. | N-U24-099 |
| VDR-U24-C173 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:58 | return '0000' | FACT | emv_qr | — | The default merchant category code is 0000 and l10n_th does not override it. | N-U24-094 |
| VDR-U24-C174 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:54 | def _get_additional_data_field(self, comment): | FACT | emv_qr | — | The additional-data hook returns None and l10n_th does not override it, so the include_reference option adds nothing for Thailand. | N-U24-094 |
| VDR-U24-C175 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:15 | proxy_type = fields.Selection([('none', 'None')] | FACT | bridge installed | — | proxy_type defaults to none; the Thai package adds ewallet_id, merchant_tax_id and mobile with ondelete set default. | N-U24-093 |
| VDR-U24-C176 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:12 | ('merchant_tax_id', 'Merchant Tax ID'), | FACT | module installed | — | Thai proxy types: Ewallet ID, Merchant Tax ID, Mobile Number. | N-U24-093 |
| VDR-U24-C177 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:18 | tax_id_re = re.compile(r'^[0-9]{13}$') | FACT | bank country TH | — | Merchant tax id must be 13 digits; mobile 10 digits (mobile_re); proxy type outside the three, none or empty is rejected; ewallet id format is not validated. | N-U24-093 |
| VDR-U24-C178 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:49 | (0, 'A000000677010111'), | FACT | bank country TH | — | Merchant account information uses tag 29 with application id A000000677010111 (PromptPay) and sub-tag 1 mobile, 2 merchant tax id, 3 e-wallet. | N-U24-089 |
| VDR-U24-C179 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:47 | re.sub(r"^0", "66", self.proxy_value).zfill(13) | FACT | proxy mobile | — | For mobile proxy the leading 0 becomes 66 and the value is left-padded with zeros to 13 characters. | N-U24-093 |
| VDR-U24-C180 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:57 | if currency.name not in ['THB']: | FACT | emv_qr, bank TH | — | EMV QR for Thai bank accounts is eligible only for THB; the message text names PayNow (copied wording). | N-U24-101 |
| VDR-U24-C181 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:65 | The PayNow Type must be either | FACT | emv_qr, bank TH | — | Generation errors if the proxy type is not one of the three Thai types. | N-U24-101 |
| VDR-U24-C182 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:111 | if not self._get_merchant_account_info(): | INFERENCE | always | — | _get_merchant_account_info returns a tuple (never falsy), so the Missing Merchant Account Information check never fires; the effective checks are city, proxy type and proxy value plus the Thai overrides. | N-U24-101 |
| VDR-U24-C183 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:114 | return _("Missing Merchant City.") | FACT | emv_qr | — | The holder partner must have a city. | N-U24-092 |
| VDR-U24-C184 | FUNCTION MAPPING REQUIRED | l10n_th/tests/test_l10n_th_emv_qr.py:77 | '00020101021229370016A0000006770101110113006681070406052040000530376454031005802TH5914company_1_data6008Thailand63048B76' | FACT | test run | — | The shipped test fixes the full payload for a mobile proxy: tag 29 A000000677010111, mobile 0066810704060, MCC 0000, currency 764, amount 100, country TH. | N-U24-089 |
| VDR-U24-C185 | FUNCTION MAPPING REQUIRED | l10n_th/tests/test_l10n_th_emv_qr.py:47 | Using invoice currency other than | FACT | test run | — | Tests assert a UserError for USD, for a missing city and for a bank without PromptPay proxy information. | N-U24-096 |
| VDR-U24-C186 | FUNCTION MAPPING REQUIRED | base/models/res_bank.py:102 | country_code = fields.Char(related='partner_id.country_code' | FACT | always | — | The bank account country code is that of the account holder partner, so Thai QR rules depend on the holder's country, not on a bank-country field. | N-U24-092 |
| VDR-U24-C187 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2206 | and move.company_id.qr_code | FACT | always | — | display_qr_code is true for customer and vendor invoices and receipts when the company switch qr_code is on (DB: off; field labelled Display SEPA QR-code). | N-U24-092 |
| VDR-U24-C188 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6795 | def _generate_qr_code | FACT | always | — | Generation picks the stored method or the first eligible one, raises UserError for a stored ineligible method, uses amount_residual and the payment reference, and stores the method after success. | N-U24-096 |
| VDR-U24-C189 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1926 | move.bank_partner_id = move.company_id.partner_id | FACT | inbound document | — | For customer documents the bank account is looked up on the company partner (or the journal bank account of the preferred payment method); DB has 0 partner bank accounts and the bank journal has no bank account linked, so no QR can appear yet. | N-U24-098 |
| VDR-U24-C190 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:927 | def _create_outstanding_accounts | OBSERVATION | DB company chart th | — | DB: one bank journal BNK1 (default 111203, suspense 111201) with 3 payment method lines (manual inbound, manual outbound, checks outbound); 0 cash journals; 2 reconcile models; 10 payment terms. | N-U24-095 |
| VDR-U24-C191 | FUNCTION MAPPING REQUIRED | payment/data/payment_method_data.xml:2867 | <record id="payment_method_promptpay" model="payment.method"> | FACT | payment app installed | — | A Prompt Pay payment method (code promptpay, active False by default, no tokenization) exists in payment data; DB shows it inactive. | N-U24-090 |
| VDR-U24-C192 | FUNCTION MAPPING REQUIRED | payment/data/payment_provider_data.xml:57 | ref('payment.payment_method_promptpay') | FACT | payment app installed | — | The data lists promptpay among supported methods of providers adyen, asiapay, stripe and xendit (cross-reference U20); DB: all real providers disabled. | N-U24-090 |
| VDR-U24-C193 | FUNCTION MAPPING REQUIRED | payment_xendit/const.py:38 | 'promptpay', | FACT | xendit | — | Xendit constants list promptpay, linepay and shopeepay under TH. | N-U24-090 |
| VDR-U24-C194 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:97 | def _get_qr_code_generation_params | INFERENCE | always | — | The QR code generation parameters carry only payload and barcode settings; there is no hook that links a QR scan to a payment record or reconciliation. | N-U24-098 |
| VDR-U24-C195 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | runtime | RT | UNKNOWN - EVIDENCE INSUFFICIENT: banking-app acceptance of the payload (dynamic indicator 12 with a mobile or tax-id proxy, MCC 0000, no reference tag) and gateway behaviour; resolve by scanning a generated sample in a test banking app. | N-U24-103 |
| VDR-U24-C196 | PCO-F02 | account/models/company.py:74 | fiscalyear_last_day = fields.Integer(default=31, required=True) | FACT | always | — | Fiscal year last day defaults to 31; last month defaults to 12 (next line); DB 31 and 12 and the Thai template does not set them. | N-U24-106 |
| VDR-U24-C197 | PCO-F02 | account/models/company.py:345 | Invalid fiscal year last day | FACT | always | — | A constraint rejects a last day outside the month length unless it is 29 February. | N-U24-112 |
| VDR-U24-C198 | PCO-F02 | account/models/account_move.py:4280 | is_staggered_year = last_month != 12 | FACT | sequence creation | — | A fiscal year ending other than 31 December makes the starting sequence use a two-digit year span and a shorter counter. | N-U24-106 |
| VDR-U24-C199 | PCO-F01 | account/models/company.py:58 | 'fiscalyear_lock_date', | FACT | always | — | SOFT_LOCK_DATE_FIELDS lists fiscal year, tax, sale and purchase lock dates; hard_lock_date is a fifth field; DB: all five are null. | N-U24-107 |
| VDR-U24-C200 | PCO-F01 | account/models/company.py:101 | irreversible and does not allow | FACT | always | — | The hard lock date cannot be excepted; the other lock dates can have exceptions (model account.lock_exception). | N-U24-107 |
| VDR-U24-C201 | PCO-F01 | account/models/account_lock_exception.py:54 | ('tax_lock_date', 'Tax Return Lock Date'), | FACT | always | — | The lock exception model lists the tax return lock date among its lockable fields. | N-U24-111 |
| VDR-U24-C202 | PCO-F01 | account/models/company.py:79 | in accordance with its journal's sequence | FACT | always | — | Lock-date help texts state that entries on or before the date are postponed to a later date according to the journal sequence. | N-U24-107 |
| VDR-U24-C203 | PCO-F02 | account/models/company.py:1151 | def _check_tax_return_configuration | FACT | always | — | The tax-return configuration check is a deprecated no-op to be overridden by localisations; l10n_th does not override it. | N-U24-108 |
| VDR-U24-C204 | PCO-F02 | account/data/onboarding_data.xml:33 | tax returns periodicity | INFERENCE | onboarding step | — | An onboarding step text mentions fiscal years and tax-return periodicity, but the underlying wizard offers only opening date and fiscal-year end. | N-U24-108 |
| VDR-U24-C205 | PCO-F02 | l10n_th/data/account_tax_report_data.xml:153 | <field name="date_scope">previous_return_period</field> | FACT | report data | — | The Thai VAT report line 10 uses the date scope previous_return_period for its carried-forward value, a concept with no definition in Community accounting. | N-U24-109 |
| VDR-U24-C206 | FUNCTION MAPPING REQUIRED | base/data/res.lang.csv:87 | "base.lang_th","Thai | FACT | th_TH language loaded | — | The Thai language record uses date format %d/%m/%Y, decimal point . and week start 7; there is no calendar-system field; DB: th_TH exists but is not active (only en_US active). | N-U24-113 |
| VDR-U24-C207 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | RT | NOT PRESENT IN COMMUNITY SOURCE: Buddhist-era year printing or calendar conversion. Search: grep -rIil 'buddhist' over odoo/addons py/xml/csv/js excluding i18n matched only an emoji table; grep for outputCalendar/defaultOutputCalendar found only a test framework reference; client-side date rendering by the browser locale not examined (RT). | N-U24-114 |
| VDR-U24-C208 | PCO-F02 | n/a | n/a | UNKNOWN | Community source | — | NOT PRESENT IN COMMUNITY SOURCE: tax-return periodicity and tax closing entry. Search: grep -rIn 'tax_closing / closing entry / periodicity / account_tax_periodicity' over odoo/addons (py, xml) outside country packs and tests: only unrelated modules and the lock-date help text matched. | N-U24-114 |
| VDR-U24-C209 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | — | NOT PRESENT IN COMMUNITY SOURCE: VAT return form/filing (PP 30 style) and sales/purchase tax invoice books. Search: grep -rIil -E '\bpp ?30\b / pp\.30' over odoo/addons py/xml/csv/js excluding l10n_th: only a Croatian tax CSV matched; the Thai report definitions (account_tax_report_data.xml, 3 report records, 24 lines) are definitions without engine or UI. | N-U24-117 |
| VDR-U24-C210 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | — | NOT PRESENT IN COMMUNITY SOURCE: withholding certificate, certificate numbers, PND 1/2/54 reports, PND filing format. Search: grep -rIil -E 'withholding certificate / certificate of withholding / tawi' (matches only unrelated foreign data) and grep for \bpnd matched only l10n_th; only PND 3 and PND 53 report definitions exist. | N-U24-118 |
| VDR-U24-C211 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:178 | 'ubl_sg': {'countries': ['SG'], 'on_peppol': False} | INFERENCE | account_edi_ubl_cii installed | — | The e-invoice format-to-country map lists country-specific formats such as SG; grep for TH or th_TH in account_edi_ubl_cii models found none, and grep -rIil -E 'e-?tax / etda / rd\.go\.th / thai revenue' outside l10n_th found only a Korean tax data file and false positives. | N-U24-119 |
| VDR-U24-C212 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | — | NOT PRESENT IN COMMUNITY SOURCE: abbreviated tax invoice, combined tax invoice and receipt, seller branch on documents. Search: grep -rIil -E 'abbreviated tax invoice / simplified tax invoice' outside l10n_th matched only foreign packs (sa, ae, gcc pos); l10n_th prints only buyer branch (views/report_invoice.xml lines 5-13). | N-U24-120 |
| VDR-U24-C213 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | external library | RT | PARTIALLY PRESENT: generic amount-in-words exists (company switch) but Thai text output depends on num2words (not in source tree); grep for bahttext / baht_text / baht text returned nothing. | N-U24-121 |
| VDR-U24-C214 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | — | NOT PRESENT IN COMMUNITY SOURCE: VAT ledger books, input-VAT proration/non-deductible split for Thailand, foreign-payee withholding taxes, Thai financial statement formats. Search: the Thai tax file has 18 taxes (none for foreign payees) and the Thai report file has 3 reports; grep for 'financial statement' over l10n_th returned nothing. | N-U24-122 |
| VDR-U24-C215 | PCO-F02 | n/a | n/a | UNKNOWN | Community source | — | NOT PRESENT IN COMMUNITY SOURCE: tax-return periodicity and tax closing entry (see CAP-U24-07 search). | N-U24-123 |
| VDR-U24-C216 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:22 | 'data/account_tax_report_data.xml', | FACT | always | — | The Thai package data files are the tax report definitions and the invoice report view only; there is no wizard, controller, cron or security file in the package. | N-U24-116 |
| VDR-U24-C217 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | legal review | — | UNKNOWN - EVIDENCE INSUFFICIENT: which outputs a foreign-owned Thai subsidiary, a foreign-company branch, representative office or regional office needs; resolve with an authoritative statutory source. | N-U24-124 |
| VDR-U24-C218 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:421 | module.country_ids & company_countries | INFERENCE | mechanical scan of manifests and DB | — | Scan of odoo/addons/l10n_*/__manifest__.py: 231 directories, 1 installed (l10n_th), 230 uninstalled; 118 uninstalled packs are country-gated auto-install packs whose auto-install dependencies are installed; 0 non-country-gated auto-install packs have their dependencies installed. | N-U24-127 |
| VDR-U24-C219 | FUNCTION MAPPING REQUIRED | account/models/partner.py:306 | localization_module.sudo().button_immediate_install() | FACT | action_create_foreign_taxes | — | FUTURE OPTIONAL COUNTRY PACK mechanism: creating foreign taxes for a fiscal position installs the localisation module of the fiscal position country when it is not installed; the action is restricted to accounting managers (the check precedes it). | N-U24-128 |
| VDR-U24-C220 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:954 | def _instantiate_foreign_taxes | FACT | foreign fiscal position | — | The helper creates the foreign tax groups and taxes on the company and stops if taxes for that country already exist. | N-U24-128 |
| VDR-U24-C221 | FUNCTION MAPPING REQUIRED | account/models/company.py:238 | multi_vat_foreign_country_ids | FACT | always | — | The company can hold foreign VAT registrations as foreign countries; the Thai report definition sets allow_foreign_vat True (report data line 8). | N-U24-129 |
| VDR-U24-C222 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:8 | <field name="allow_foreign_vat" eval="True"/> | FACT | report data | — | The Thai Tax Report definition allows foreign VAT. | N-U24-129 |
| VDR-U24-C223 | FUNCTION MAPPING REQUIRED | l10n_th/models/__init__.py:6 | from . import res_bank | FACT | always | — | The Thai package imports five model files (template, res_partner, account_move, ir_actions_report, res_bank); none extends res.company, so it adds no company-level field. | N-U24-130 |
| VDR-U24-C224 | FUNCTION MAPPING REQUIRED | base/tests/test_reports.py:36 | 'l10n_th.report_commercial_invoice': invoice_domain, | FACT | tests | — | The base report test registry names the Thai commercial invoice report; it is the only reference to the Thai package outside the package in Community (grep over py, xml, csv, js). | N-U24-131 |
| VDR-U24-C225 | FUNCTION MAPPING REQUIRED | l10n_in/__manifest__.py:24 | 'account_debit_note', | OBSERVATION | source only | — | FUTURE OPTIONAL COUNTRY PACK: manifests of l10n_co, l10n_ec, l10n_hu_edi, l10n_in, l10n_it_edi, l10n_pe and l10n_sa depend on the debit-note add-on (mechanical grep). | N-U24-131 |
| VDR-U24-C226 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:5 | 'countries': ['th'], | OBSERVATION | DB | — | DB: ir_module state installed for l10n_th only among l10n_* names; 230 other l10n_* modules uninstalled; account_qr_code_emv, account_edi, account_edi_ubl_cii installed; account_debit_note, base_vat, base_address_extended, l10n_account_withholding_tax, account_peppol uninstalled. | N-U24-125 |
| VDR-U24-C227 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1850 | move.company_id.display_invoice_tax_company_currency | OBSERVATION | DB | — | Company currency in the DB is THB; foreign-currency sale documents show taxes in company currency when the setting is on (cross-reference U25). | N-U24-129 |
| VDR-U24-C228 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | company structure | — | UNKNOWN - EVIDENCE INSUFFICIENT: structuring of foreign-owned Thai subsidiaries, foreign-company branches, representative offices and regional offices; resolve via units on company structure and an authoritative statutory source. | N-U24-133 |
| VDR-U24-C229 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:77 | access_account_tax_manager | FACT | always | — | ACL: account.tax is readable by internal users, readonly and invoicing groups and fully editable by account.group_account_manager; tax group and repartition line follow the same pattern. | N-U24-134 |
| VDR-U24-C230 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:171 | Tax multi-company | FACT | always | — | Global record rules named Tax multi-company, Tax group multi-company, Account multi-company and Journal multi-company scope these records to the allowed companies; the partner bank rule is in base security. | N-U24-134 |
| VDR-U24-C231 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:57 | Partner bank company rule | FACT | always | — | Partner bank accounts are covered by a global company rule, so a Thai QR proxy belongs to the company that owns the account holder. | N-U24-099 |
| VDR-U24-C232 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:39 | 'income_account_id': 'l10n_th_account_411100', | INFERENCE | template th loaded | — | Lines 12-41 of the template supply default receivable, payable, income, expense, tax and bank-related accounts, so a first invoice needs no manual account setup. | N-U24-003 |
| VDR-U24-C233 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:18 | "tax_input_vat_exempted" | FACT | template th | — | Rows 2-25 define six VAT taxes (input and output at 7%, 0% and 0% EXEMPT), each with invoice and refund base and tax distribution lines (four lines each). | N-U24-019 |
| VDR-U24-C234 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:125 | Set active to false | FACT | always | — | A tax is archived by clearing active; DB shows all 18 Thai taxes active. | N-U24-028 |
| VDR-U24-C235 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:164 | tax_exigibility = fields.Selection( | OBSERVATION | DB company chart th | — | DB: tax_exigibility is on_invoice for all 18 Thai taxes, so VAT is recognised at posting; none is on_payment. | N-U24-028 |
| VDR-U24-C236 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:70 | "tax_wht_income_5","5% WH R" | INFERENCE | template th | — | Rows 26-73 hold 12 withholding taxes: 8 purchase (4 company payee, 4 individual payee) and 4 sale, at -1, -2, -3, -5 percent. | N-U24-038 |
| VDR-U24-C237 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1130 | return raw_base * self.amount / 100.0 | INFERENCE | percent tax excluded | — | Because a percent tax is base times amount, a negative percent already yields a withheld (negative) amount with the ordinary engine, with no extra module. | N-U24-041 |
| VDR-U24-C238 | FUNCTION MAPPING REQUIRED | l10n_th/models/__init__.py:2 | from . import template_th | INFERENCE | always | — | The Thai package defines no withholding model, status or certificate object (its models are template, partner, move, report action and bank). | N-U24-050 |
| VDR-U24-C239 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | legal review | — | UNKNOWN - EVIDENCE INSUFFICIENT: whether document-time recognition of withholding matches the statutory point of obligation; resolve with an authoritative statutory source. | N-U24-054 |
| VDR-U24-C240 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:3 | primary="True" | INFERENCE | always | — | The Thai invoice document is a primary inherit of the core document whose only edits are the branch label and title; l10n_th overrides no posting, numbering or tax method. | N-U24-061 |
| VDR-U24-C241 | FUNCTION MAPPING REQUIRED | l10n_th/i18n/th.po:76 | msgid "Headquarter" | FACT | th_TH language loaded | — | Branch %(code)s and Headquarter have Thai catalogue entries keyed on the English text (translatable text observation). | N-U24-058 |
| VDR-U24-C242 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | — | NOT PRESENT IN COMMUNITY SOURCE: seller branch printing and abbreviated or combined tax documents; l10n_th adds only o.partner_id.l10n_th_branch_name (buyer side) and the web company header prints company.vat only. | N-U24-072 |
| VDR-U24-C243 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:238 | vat_label = fields.Char(string='Tax ID Label' | FACT | always | — | The identifier label is a computed char (Tax ID by default); the identifier itself is the generic vat field. | N-U24-074 |
| VDR-U24-C244 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_partner.py:16 | code = partner.company_registry | FACT | company partner in TH | — | The branch value is taken from the generic company_registry field; l10n_th adds no dedicated branch field. | N-U24-076 |
| VDR-U24-C245 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_partner.py:14 | partner.l10n_th_branch_name = "" | INFERENCE | always | — | The file has no constraint or onchange on company_registry, so any text (or none) is accepted as branch value. | N-U24-084 |
| VDR-U24-C246 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:79 | (54, amount), | INFERENCE | emv_qr | — | The payload carries the transaction amount (invoice residual) so the payer does not type amount or account details; scanning behaviour RT. | N-U24-091 |
| VDR-U24-C247 | FUNCTION MAPPING REQUIRED | account/views/res_config_settings_views.xml:235 | id="qr_code_invoices" | FACT | always | — | The invoice QR code is a company-dependent accounting setting (Add a payment QR-code to your invoices). | N-U24-097 |
| VDR-U24-C248 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6828 | rslt = self.partner_bank_id.build_qr_code_base64(self.amount_residual | INFERENCE | foreign-currency invoice | — | The QR is built from amount_residual and the document currency with no conversion to baht, and Thai bank accounts accept THB only, so a foreign-currency invoice cannot carry a Thai QR (cross-ref U25). | N-U24-102 |
| VDR-U24-C249 | PCO-F02 | account/models/company.py:75 | fiscalyear_last_month = fields.Selection(MONTH_SELECTION, default='12' | FACT | always | — | The fiscal year end is two company fields (day, month) with defaults 31 and 12; no period object exists. | N-U24-104 |
| VDR-U24-C250 | PCO-F01 | account/models/company.py:76 | fiscalyear_lock_date = fields.Date( | FACT | always | — | A fiscal-year lock date field closes earlier periods; tax, sale and purchase lock dates and a hard lock date complete the set. | N-U24-105 |
| VDR-U24-C251 | PCO-F02 | l10n_th/models/template_th.py:23 | 'account_fiscal_country_id': 'base.th', | INFERENCE | template th loaded | — | The Thai company data (lines 22-41) contains no fiscal-year or lock-date key, so these remain at their generic defaults. | N-U24-110 |
| VDR-U24-C252 | FUNCTION MAPPING REQUIRED | l10n_th/__init__.py:2 | from . import models | FACT | always | — | The Thai package Python is only a models import plus a post-init hook; there is no wizard, controller or cron, so outputs beyond reports and documents are not code-provided. | N-U24-115 |
| VDR-U24-C253 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:408 | def button_install | INFERENCE | programme profile of manifests | — | Profile counts of the 227 non-Thai packs by archetype: base country pack 116, electronic invoice 34, other extension 39, point of sale 17, stock/sale/purchase/website bridge 16, payroll or HR 5 (from COUNTRY_PACK_BOUNDARY_PROFILE_227.tsv). | N-U24-126 |
| VDR-U24-C254 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7373 | def _get_name_invoice_report | INFERENCE | another pack installed | — | The document selector is a shared override point (the core comment names l10n_ar); 119 of 227 packs extend core accounting models per the profile, so a second pack could collide with the Thai override. | N-U24-132 |
| VDR-U24-C255 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:16 | Move to 'Input VAT' upon payment | FACT | template th | — | Account 114100 description: undue input VAT from service bills not yet paid, to be moved to Input VAT upon payment; no code does this (no shipped tax uses 114100). | N-U24-135 |
| VDR-U24-C256 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:17 | transferred to VAT Payable/Receivable at month-end | FACT | template th | — | Account 114200 description says its balance is transferred to VAT Payable/Receivable at month-end; the Community source has no closing routine (see CAP-U24-07). | N-U24-135 |
| VDR-U24-C257 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:59 | Net VAT liability (Output VAT | FACT | template th | — | Account 213200 Output VAT is described as net VAT liability to be remitted (PP.30) although tax lines post gross output VAT to it; 213400 VAT Payable is the intended settlement account (descriptive text, translatable). | N-U24-135 |
| VDR-U24-C258 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:18 | Claimable against year-end CIT | FACT | template th | — | Account 114300 description: income tax deducted by customers, claimable against year-end corporate income tax. | N-U24-136 |
| VDR-U24-C259 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:65 | moved here from PND specific accounts | FACT | template th | — | Account 213500 description: net withholding liability moved here from the PND-specific accounts at month end; no code performs the move. | N-U24-136 |
| VDR-U24-C260 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:63 | Tax deducted from payments sent Overseas | FACT | template th | — | Account 213303 description: tax deducted from payments sent overseas (PND 54); 213300 description: employee salaries (PND 1); neither is used by any shipped tax. | N-U24-055 |

## 12. Report items

**DISCOVERED SUPPORTING MODULES** (read only as far as needed): `base` (ir_module country gate and install flow, res_partner vat/registry/duplicate warning, res_currency amount_to_text, res.lang data, report action domain, security rules, res_bank holder country), `account` (tax engine, company, partner/fiscal position, move sequence and QR, chart loader, ir_module chart trigger, journals, report templates, ACL/rules), `web` (company header seller TIN), `payment` (PromptPay payment method and provider data) and `payment_xendit` (TH methods) read for the QR/online route only (U20 owns), `account_edi_ubl_cii` (format country map, grep only), `contacts` (dependency of `base_address_extended`), `account_report` data model (definitions only), foreign packs `l10n_kh`, `l10n_ph`, `l10n_sa_withholding_tax`, `l10n_co`, `l10n_ec`, `l10n_hu_edi`, `l10n_in`, `l10n_it_edi`, `l10n_pe`, `l10n_sa` (manifest dependency lines only; FUTURE OPTIONAL COUNTRY PACK).

**Contradictions with prior evidence:**
(1) CONTRA to the unit brief (not to a prior file): amount in words was listed as an expected Thai gap, but a generic facility exists in Community (company switch, document field, report block, currency labels Baht/Satang) and the DB company flag is on; only Thai-language output is UNKNOWN (claim flagged).
(2) DELTA to U13 CAP-U13-08 prose "Thai invoice printed with Tax Invoice title": the title replacement applies only to the posted customer-invoice title; credit notes, draft and cancelled documents keep standard titles; the Commercial Invoice prints the standard title.
(3) Consistent with U13: 144 accounts, 18 taxes, 5 groups, tag counts, group fallback to WHT 1%, 114300 asset type, unused SUR tags, transfer prefix literal, QR rules. Consistent with U23: Thai set uses ordinary document-time taxes; base_vat stub; debit-note/Thai title interplay remains RT.
DELTA additions: (a) exact per-account wiring (24 of 144 used by templates; undue VAT, PND1, PND54 accounts unused); (b) payload-length/CRC observation for non-ASCII text; (c) base QR missing-information check is ineffective; (d) additional-data tag and MCC not Thai-specific; (e) company/individual withholding chosen only by tax selection; (f) price-included risk for purchase-side taxes; (g) Thai layout choice is fixed by company fiscal country with title rendering by partner language; (h) country-pack auto-install gate and on-demand foreign taxes path; (i) tax report definitions have no UI/engine in Community; (j) account.asset template CSV not loadable by Community core.

**Runtime/AWT-required (RT) list:** auto-load order at registry start; numeric results of VAT plus withholding combinations and rounding; zero tax line persistence; Thai layout and debit-note title rendering; num2words Thai support; stored vat form after validation (stdnum th); QR payload scan acceptance and non-ASCII merchant text; gateway behaviour; browser date rendering in Thai locale; behaviour when a foreign-country company is added.

**Hand-offs:** U11 posting/locks, U12 payments/reconcile/exchange difference, U13 tax engine details, U20 payment providers, U25 multi-currency, U26 translation mechanism, U27/U28 localisation framework and company structure.

## 14. Not read / limits
Not read: python-stdnum and num2words libraries (outside source tree; Thai TIN rules and Thai number words UNKNOWN); the `account_report` expression-evaluation code beyond model definitions and the generic tax-report data; `account_edi_ubl_cii` beyond the format-country map; payment gateway code beyond the PromptPay data lines; `l10n_account_withholding_tax` wizards and JS beyond manifest, tax model and the entry builder (U23 covers); `base_vat` VIES/IAP code; `base_address_extended` views; `tools.street_split` regexes were read in `odoo/tools/misc.py` but are not citable by the pointer checker (outside addons). No foreign pack accounting rule was read. The shared scratch file `/private/tmp/claude-501/q.sh` was (re)created by this unit as a read-only psql helper; other workers should not rely on its prior content. No capability is claimed complete.
