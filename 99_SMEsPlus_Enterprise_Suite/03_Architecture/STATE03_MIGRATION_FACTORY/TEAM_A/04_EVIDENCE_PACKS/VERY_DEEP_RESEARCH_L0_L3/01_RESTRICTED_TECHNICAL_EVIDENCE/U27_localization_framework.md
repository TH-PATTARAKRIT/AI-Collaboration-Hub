# U27 — localization_framework — Restricted Technical Evidence

> **RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION**
> Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**
> Unit: U27 `localization_framework` · Source revision: `19.0.post20260921` (Odoo 19 Community only) · Date: 2026-10-02
> Approved scope (programme owner): research and DEFINE, as a neutral CANDIDATE (not a requirement, not an approved design), the generic extension architecture **Country-Neutral Accounting Core -> Localization Framework -> Optional Country Packs**, so that each Company can use the accounting jurisdiction applicable to its own legal/accounting entity. `l10n_th` is in scope as the reference pack (content studied by U24; this unit studies the framework it plugs into). Non-Thai `l10n_*` modules are FUTURE OPTIONAL COUNTRY PACKS: only manifest, dependency, extension boundary, configuration pattern and integration contract were inspected; **no country tax/accounting rule was studied or adopted**.
> Modules studied: `account` (company jurisdiction fields, chart-template loader, fiscal positions, tax/tag/report country scoping, hook points), `base` (company tree, country install trigger, module registry), `base_vat` (hook only), `account_edi`, `account_edi_ubl_cii` (hook structure and country-conditional counts only), `account_qr_code_emv`, `account_qr_code_sepa`, `account_payment_interco`, `account_update_tax_tags` (manifest), `l10n_th` (all models, manifest, report data, template CSV counts), and 227 foreign `l10n_*` packs (mechanical manifest/AST scans plus 20 hand-read manifests and hook entry points).
> Read-only on source; DB queried only for configuration/structure (counts, flags, seeded configuration names). No Odoo started, no L5/AWT claims. Items needing execution are flagged `RT`. No V-level, completeness, coverage %, gate or approval is asserted. Nothing from `Extra_Thailand`, `Extra_Module_scgl` or any proprietary code was opened.
> Claim IDs `VDR-U27-C###`; neutral IDs `N-U27-###` (see `02_NEUTRAL_KNOWLEDGE/U27_localization_framework_NEUTRAL.md`). Claim ids in prose below are resolved at generation time; every statement is backed by a row in the final claims table.

## 0. Scope, method, Function-ID mapping, honest limits

| Capability | Function-ID | Note |
|---|---|---|
| CAP-U27-01 Jurisdiction assignment | FUNCTION MAPPING REQUIRED | no index entry for company-to-jurisdiction assignment |
| CAP-U27-02 Country-neutral core boundary | FUNCTION MAPPING REQUIRED | |
| CAP-U27-03 Localization framework mechanisms | FUNCTION MAPPING REQUIRED | |
| CAP-U27-04 Country-pack lifecycle | FUNCTION MAPPING REQUIRED | |
| CAP-U27-05 Extension-boundary taxonomy of packs | FUNCTION MAPPING REQUIRED | |
| CAP-U27-06 Multi-jurisdiction coexistence | MCT-F03 (Shared vs. per-company Chart of Accounts) used only on the three claims about account sharing, code per root and cash accounts; all others FUNCTION MAPPING REQUIRED | MCT-F03 genuinely matches only the shared/per-company chart question |
| CAP-U27-07 Gaps and candidate architecture | FUNCTION MAPPING REQUIRED | |

**Method.** (1) Full read of `account/models/chart_template.py` (1539 lines), `account/models/ir_module.py`, `l10n_th/**/*.py`, `l10n_th/__manifest__.py`, report data and CSV headers; targeted reads of `account/models/company.py`, `partner.py` (fiscal position and VAT hooks), `account_tax.py`, `account_report.py`, `account_account_tag.py`, `account_move.py` (fiscal position, tax country, report hook, posting signature), `account_move_send.py`, `sequence_mixin.py`, `account_journal.py`, `res_config_settings.py`, `account_security.xml`, `base/models/res_company.py`, `base/models/ir_module.py`, `base_vat` hook areas. (2) Mechanical scans over `odoo/addons`: manifest parse of all 231 `l10n_*` directories (227 foreign + `l10n_th` + 3 generic-mechanism modules); AST scan of `_inherit` blocks for model/method extension counts; AST scan of loader-class overrides; AST/regex scan of 31 core accounting-family modules for literal country codes (comparisons, lists, tables); regex guard-lint of selected pack overrides; independent recount of the 227-pack profile columns. The scan scripts were kept in the scratchpad, not in the output directory. (3) Restored DB read for configuration only.

**Not read / limits.** No foreign pack rule content (taxes, accounts, CSV data, i18n) was read; foreign pack hook bodies were read only to classify the lifecycle pattern (about 14 `__init__.py` files). `account_edi_ubl_cii` and `account_peppol` were scanned for country literals and hook structure only. The full `account_move.py`, `account_payment.py` and `account_report.py` engines are U11/U12/U13 territory and were not re-read. Heuristic regex counts (guard-lint) are marked INFERENCE. All runtime behaviour is `RT`.


---

## CAP-U27-01 Jurisdiction assignment of a company

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Tie each company (legal/accounting entity) to the jurisdiction whose tax reporting, currency, chart of accounts and fiscal positions apply to it, inside a database that may hold several companies. In Community this tie is not one field but a set of loosely coupled settings: address country, fiscal country, currency, loaded chart code, fiscal positions (with optional foreign registrations). VDR-U27-C001 VDR-U27-C003 VDR-U27-C280

### D2 Architecture / data
- Company: address country (partner-derived) VDR-U27-C285, `account_fiscal_country_id` (stored, computed, writable) VDR-U27-C001, `chart_template` selection VDR-U27-C003, root-delegated fields `currency_id`, fiscal-year end, storno, cash-basis switch VDR-U27-C020 VDR-U27-C021 VDR-U27-C022, hierarchy immutable VDR-U27-C024.
- Country-to-package link: manifest key `countries` synchronised into `module_country` VDR-U27-C007 VDR-U27-C008; computed list of uninstalled auto-install packages per company country VDR-U27-C009; install on company create/first country write VDR-U27-C011 VDR-U27-C012 VDR-U27-C010; installation of country-flagged auto-install modules checks all companies' countries VDR-U27-C013 VDR-U27-C257; chart loading afterwards VDR-U27-C014 VDR-U27-C015.
- Chart choice by country: selection sorted by country, guess = first VDR-U27-C004 VDR-U27-C005 VDR-U27-C006; branch uses parent's chart VDR-U27-C016 VDR-U27-C015; generic fallback pinned to a country VDR-U27-C063 VDR-U27-C064 VDR-U27-C065.
- Tax scoping: tax and tax group country default from fiscal country VDR-U27-C026 VDR-U27-C027; document tax country from fiscal position (foreign VAT) else company fiscal country VDR-U27-C028 with a validating constraint VDR-U27-C029 VDR-U27-C030; tags per country VDR-U27-C055 VDR-U27-C056 and selectable tags limited to fiscal and foreign-registration countries VDR-U27-C057; reports by country/chart/always VDR-U27-C053 VDR-U27-C054.
- Fiscal positions: one company each VDR-U27-C031; foreign registration VDR-U27-C032 VDR-U27-C033 VDR-U27-C034 VDR-U27-C035; domestic position VDR-U27-C036; matching VDR-U27-C037 VDR-U27-C038 VDR-U27-C039 VDR-U27-C040 VDR-U27-C042; hard-wired regional case VDR-U27-C041.
- Partner side: per-company properties VDR-U27-C043; global tax number VDR-U27-C044; validation hook VDR-U27-C045 VDR-U27-C046 VDR-U27-C047 VDR-U27-C048 VDR-U27-C049; source import coupling VDR-U27-C050 VDR-U27-C051 VDR-U27-C052.
- Thailand: pack flagged for one country VDR-U27-C058; template sets fiscal country VDR-U27-C059.

### D3 Logic
Assignment sequence for a new Thai company: create company with country TH -> `install_l10n_modules` (registry ready, not in test) -> `l10n_th` (auto_install ['account'], countries ['th']) installed if not yet -> `try_loading(guessed template, company)` in pre-commit when the company has no chart VDR-U27-C014 -> loader writes company values including `account_fiscal_country_id = base.th` VDR-U27-C059, currency from fiscal country when no entries VDR-U27-C018.
Changing country on an already-countried company does nothing VDR-U27-C012. Changing the fiscal country later is not guarded VDR-U27-C062.
State list:
- `company without country -> country set [first write triggers l10n install]` VDR-U27-C012
- `country set, no chart -> chart loaded [try_loading in pre-commit]` VDR-U27-C014
- `chart loaded, no entries -> other chart [wipe + load]` VDR-U27-C118
- `chart loaded, entries exist -> currency and price-include locked` VDR-U27-C023 VDR-U27-C152
- `document tax country != tax.country -> rejected` VDR-U27-C029

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | New company with country -> package auto-install -> chart load -> fiscal country and currency set (VDR-U27-C011 VDR-U27-C014 VDR-U27-C059 VDR-U27-C018). |
| 2 | Reversal/negative | Later country change triggers nothing (VDR-U27-C012); hierarchy cannot change (VDR-U27-C024); currency locked after entries (VDR-U27-C023); incompatible taxes rejected (VDR-U27-C029). |
| 3 | Multi-company | Delegated root fields and branch chart (VDR-U27-C020 VDR-U27-C016); fiscal position per company (VDR-U27-C031); partner properties per company, tax number global (VDR-U27-C043 VDR-U27-C044); package installation database-wide (VDR-U27-C257). |
| 4 | Side effects | Currency activated when a company is created with it (VDR-U27-C284); module_country maintenance (VDR-U27-C008); default taxes/properties (CAP-03). |
| 5 | Configuration/optionality | `countries`/`auto_install` manifest keys (VDR-U27-C007); fiscal country editable (VDR-U27-C001); validation component optional (VDR-U27-C045 VDR-U27-C061); generic chart (VDR-U27-C063). |
| 6 | Validation | Foreign-registration constraints (VDR-U27-C033); delegated-field constraint (VDR-U27-C022); report availability (VDR-U27-C054); tax country (VDR-U27-C029). |
| 7 | Roles/permissions | Chart load only for system admin (VDR-U27-C114); foreign taxes only for accounting managers (VDR-U27-C174); company rules on tax, journal, fiscal position (VDR-U27-C231 VDR-U27-C233 VDR-U27-C234). |
| 8 | Scheduled/automated | NOT APPLICABLE — triggers are synchronous (create/write/install); no cron is involved in jurisdiction assignment. |
| 9 | Exception/failure | Tax/country mismatch message (VDR-U27-C030); hierarchy error (VDR-U27-C024); install_l10n skipped when registry not ready, in tests or imports (VDR-U27-C010). |
| 10 | Accounting/compliance | Tax country selects tags, reports and reportable taxes (VDR-U27-C026 VDR-U27-C057 VDR-U27-C053); unguarded fiscal-country change after entries (VDR-U27-C062); generic chart pins another country (VDR-U27-C063). |

### DB reconciliation
VDR-U27-C060 VDR-U27-C061. Source vs DB: `l10n_th` manifest countries [th] <-> `module_country` row for l10n_th = TH (1 of 179 rows); `account_fiscal_country_id` = 217 = Thailand = company address country; `chart_template` = th; currency 134 = THB (active currencies: THB, USD). `l10n_th` `latest_version` 19.0.2.0 = manifest 2.0.

### Unknown / Runtime
VDR-U27-C062 (RT) · VDR-U27-C258 · VDR-U27-C259 · VDR-U27-C281 (RT) · behaviour of `install_l10n_modules` in a real create with the `skip_auto_install` config key set (not read).

---

## CAP-U27-02 Country-neutral accounting core boundary

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Establish what the accounting core provides when no country pack is installed, and where the core nevertheless carries country-keyed behaviour. This is the baseline for the Country-Neutral Accounting Core of the candidate architecture. Only counts and classification were produced; no country rule was read. VDR-U27-C066 VDR-U27-C276 VDR-U27-C260

### D2 Architecture
- Core provides: chart template registry that includes the core itself with a generic template VDR-U27-C066 VDR-U27-C067; posting VDR-U27-C068; lock dates VDR-U27-C069; sequence mixin and journal-level pattern override VDR-U27-C070 VDR-U27-C071; fiscal positions and tax country scoping (CAP-01); report availability (CAP-03).
- Documented core hook points designed to be overridden by packs: e-document VDR-U27-C072 VDR-U27-C073 VDR-U27-C074 VDR-U27-C075; document selection and title VDR-U27-C076 VDR-U27-C077; audit-trail flag VDR-U27-C078 VDR-U27-C079; partner fields required to invoice VDR-U27-C080; QR VDR-U27-C081 VDR-U27-C082 VDR-U27-C083.
- Country-conditional code in the core family, by kind:
  (a) country exposed as data to views/rules VDR-U27-C084 VDR-U27-C085;
  (b) literal comparisons VDR-U27-C086 VDR-U27-C087 VDR-U27-C088 VDR-U27-C089 VDR-U27-C091 VDR-U27-C096 VDR-U27-C097 VDR-U27-C041;
  (c) literal lists/tables VDR-U27-C090 VDR-U27-C092 VDR-U27-C093 VDR-U27-C094 VDR-U27-C095 VDR-U27-C098 VDR-U27-C099 VDR-U27-C100 VDR-U27-C104;
  (d) country-named formats and per-country branches in the shared e-document module VDR-U27-C101 VDR-U27-C102 VDR-U27-C103.
- Counts VDR-U27-C260 (table T2 in section 8).

### D3 Logic
No state machine. Classification rule used for the scan: Compare nodes with a 2-letter string constant and a country/code/vat context (excluding payment-method codes, languages, currencies, move types); list/tuple/set literals with 4 or more 2-letter uppercase codes making up at least 80 percent of elements; dict literals with 4 or more 2-letter keys. One hit in `account_peppol_response` (response codes) is a false positive and excluded. Country-as-data (a) was counted by regex and not classified further.

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Core installs and works with the generic template and no pack (VDR-U27-C066). |
| 2 | Reversal/negative | NOT APPLICABLE — boundary study; reversal belongs to U11. |
| 3 | Multi-company | Fiscal country exposure fields are evaluated per company (VDR-U27-C084 VDR-U27-C085). |
| 4 | Side effects | Generic template pins country and valuation style (VDR-U27-C063). |
| 5 | Configuration/optionality | Every hook defaults to neutral (VDR-U27-C073 VDR-U27-C080 VDR-U27-C081). |
| 6 | Validation | Audit-trail constraint (VDR-U27-C079). |
| 7 | Roles/permissions | NOT APPLICABLE — no new roles; see CAP-01 and CAP-06 for rules. |
| 8 | Scheduled/automated | NOT APPLICABLE. |
| 9 | Exception/failure | Template choice guard (VDR-U27-C095). |
| 10 | Accounting/compliance | Literal country behaviours in the core (VDR-U27-C089 VDR-U27-C091) mean neutrality does not hold; no rule studied. |

### DB reconciliation
Core family modules installed in the DB: account, account_add_gln, account_check_printing, account_edi, account_edi_proxy_client, account_edi_ubl_cii, account_fleet, account_payment, account_payment_interco, account_peppol_advanced_fields, account_qr_code_emv, account_qr_code_sepa, base_iban. Not installed: base_vat, account_peppol, account_debit_note, account_tax_python, account_update_tax_tags, l10n_account_withholding_tax. Consequence for the Thai deployment: the main accounting module (2 comparisons, 6 lists), check printing (one country-specific setting), the shared e-document module (40 comparisons), the SEPA QR module (one list) and the IBAN table are active; the tax-number validation component (4 comparisons, 62-country table) and the e-invoice network module are not. Core account seeds 125 access rows, 31 record rules, 10 groups, 2 cron jobs in the DB; source `ir.model.access.csv` has 125 rows, `account_security.xml` 31 rules and 10 groups, `service_cron.xml` 2 jobs (exact match; owned by U11/U13, reported for reconciliation only).

### Unknown / Runtime
VDR-U27-C279 · the generic template's anglo-saxon default versus Thai deployment is moot because the Thai template is loaded (VDR-U27-C065).

---

## CAP-U27-03 Localization framework mechanisms

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Provide a single, repeatable way for a country package to deliver a company's initial accounting configuration (accounts, taxes, groups, fiscal positions, journals, defaults, tags, reports) and to plug in country-specific document, identity, e-document, QR and numbering behaviour without touching the core. This is the Localization Framework layer of the candidate architecture.

### D2 Architecture
- Registry: decorator and metadata VDR-U27-C106 VDR-U27-C107; reflection VDR-U27-C108; module scan VDR-U27-C109 VDR-U27-C110 VDR-U27-C111.
- What a template defines: models and order VDR-U27-C105 VDR-U27-C125; template-level values VDR-U27-C132 VDR-U27-C133; CSV providers VDR-U27-C127 VDR-U27-C129 VDR-U27-C130; hard-coded journals VDR-U27-C131; parent chain VDR-U27-C124 VDR-U27-C126 VDR-U27-C128; unknown-field filtering VDR-U27-C134.
- Loader flow: entry VDR-U27-C112; admin only VDR-U27-C114; install on select VDR-U27-C115; context VDR-U27-C116; reload detection VDR-U27-C117; wipe VDR-U27-C118 VDR-U27-C119; branches VDR-U27-C120 VDR-U27-C123 VDR-U27-C139; order VDR-U27-C121; data loading VDR-U27-C135 VDR-U27-C136 VDR-U27-C137 VDR-U27-C138; post-load VDR-U27-C140 VDR-U27-C141 VDR-U27-C142; translations VDR-U27-C143; demo VDR-U27-C122.
- Reload/update: VDR-U27-C144 VDR-U27-C145 VDR-U27-C146 VDR-U27-C147 VDR-U27-C149 VDR-U27-C150 VDR-U27-C148 VDR-U27-C113; protection once entries exist VDR-U27-C151 VDR-U27-C152 VDR-U27-C153 VDR-U27-C023.
- Tax tag and report integration: VDR-U27-C154 VDR-U27-C155 VDR-U27-C156 VDR-U27-C055 VDR-U27-C056 VDR-U27-C053 VDR-U27-C157 VDR-U27-C158.
- Partner VAT/identity hook: VDR-U27-C254 VDR-U27-C255 VDR-U27-C045 VDR-U27-C046 VDR-U27-C048.
- Document layout/title hook: VDR-U27-C076 VDR-U27-C077 VDR-U27-C159 VDR-U27-C160 VDR-U27-C161.
- E-document registration: VDR-U27-C072 VDR-U27-C073 VDR-U27-C074 VDR-U27-C162 VDR-U27-C163 VDR-U27-C164 VDR-U27-C165 VDR-U27-C166.
- Payment method / QR: VDR-U27-C256 VDR-U27-C081 VDR-U27-C083 VDR-U27-C167.
- Number-format conventions: VDR-U27-C168 VDR-U27-C071 VDR-U27-C169 VDR-U27-C170 VDR-U27-C096.
- Auto-install by country dependency: VDR-U27-C171 VDR-U27-C172 VDR-U27-C013.
- Foreign-tax facility (cross-jurisdiction): VDR-U27-C173 VDR-U27-C174.

### D3 Logic
`try_loading(template_code, company, install_demo=False, force_create=True)` -> `_load`: admin check -> install owning module if needed -> context (company-only, en_US, `chart_template_load`) -> `reload_template = (code == company.chart_template)` -> set `company.chart_template` -> if not reload and no entries: wipe moves + template models of company tree -> `_get_chart_template_data` (root providers + parent chain providers, model order) -> branch reduces data to `res.company` -> (reload) `_pre_reload_data` -> `_pre_load_data` (company values, currency, anglo flag, code digits, unknown-field filter, untranslatable fields) -> `_load_data` (xmlid deref, delay, `_load_records` noupdate) -> `_post_load_data` -> translations -> group parent sync -> demo -> recursive for branches. VDR-U27-C121 VDR-U27-C112 VDR-U27-C118 VDR-U27-C135
State list:
- `no chart -> chart loaded [try_loading]` VDR-U27-C261
- `chart loaded -> reload [same code; user data kept]` VDR-U27-C117 VDR-U27-C144
- `chart loaded, no entries -> different chart [wipe]` VDR-U27-C118
- `chart loaded, entries -> different chart [no wipe; merge]` VDR-U27-C118 VDR-U27-C153
- `package uninstalled -> company chart cleared` VDR-U27-C183

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Template selected -> package installed -> data loaded in model order -> defaults set (VDR-U27-C112 VDR-U27-C121 VDR-U27-C140). |
| 2 | Reversal/negative | Different template wipes only without entries (VDR-U27-C118); reload keeps user data (VDR-U27-C144 VDR-U27-C150); changed taxes renamed [old] (VDR-U27-C147). |
| 3 | Multi-company | Per-company load; branches get company values only and reference root records (VDR-U27-C116 VDR-U27-C120 VDR-U27-C139 VDR-U27-C123). |
| 4 | Side effects | Product default taxes, property defaults, journals defaults (VDR-U27-C141 VDR-U27-C142 VDR-U27-C140); company currency (VDR-U27-C018). |
| 5 | Configuration/optionality | `force_create`, demo, code digits, parent chain (VDR-U27-C113 VDR-U27-C122 VDR-U27-C133 VDR-U27-C124). |
| 6 | Validation | Tag existence (VDR-U27-C155); unknown fields dropped (VDR-U27-C134); price-include guard (VDR-U27-C152). |
| 7 | Roles/permissions | System administrator only (VDR-U27-C114); no ACL rows for the abstract loader model in DB (0 rows). |
| 8 | Scheduled/automated | NOT APPLICABLE — loader is on-demand (no cron); translations are reloaded at term load (VDR-U27-C198). |
| 9 | Exception/failure | Missing tag `RedirectWarning` (VDR-U27-C155); demo errors swallowed (VDR-U27-C122); direct selection of two regional templates refused (VDR-U27-C095). |
| 10 | Accounting/compliance | Records noupdate under the core namespace (VDR-U27-C137 VDR-U27-C138); tags country-scoped (VDR-U27-C055); reload leaves duplicate-looking taxes (VDR-U27-C262). |

### DB reconciliation
Loader records in DB: external ids in module `account` with company prefix `1_`: 147 accounts, 18 taxes, 7 journals, 5 tax groups, 2 reconcile models (matches 147 account rows, 18 taxes, 7 journals, 5 tax groups). `account_tag` rows with applicability taxes: 13 (country Thailand); 3 reports from `l10n_th` and 3 from `account` (VDR-U27-C158). ir_rule: 5 global company rules on journal, account, tax group, tax and fiscal position, all with `parent_of` domains (source 149/155/167/173/191 of account_security.xml, see CAP-06). `account.chart.template` is an abstract model with no ACL and no table.

### Unknown / Runtime
VDR-U27-C264 (RT) · VDR-U27-C262 (RT) · VDR-U27-C263 · VDR-U27-C165 (RT: external services) · `_load_translations` internals were read, not exercised.

---

## CAP-U27-04 Country-pack lifecycle

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Describe how a country pack comes into a database, loads its data, upgrades and leaves, so that the candidate lifecycle (register, install, assign, upgrade, deactivate, uninstall) can be stated. Source: core mechanisms, `l10n_th` as reference, 227-pack profile (recounted) and about 16 hand-read samples (manifest, dependencies, hook entry points only).

### D2 Architecture
- Install triggers: manual; auto-install by dependency+country VDR-U27-C172 VDR-U27-C013 VDR-U27-C175; chart selection of an uninstalled pack VDR-U27-C115; first template on install VDR-U27-C199 VDR-U27-C200; company country VDR-U27-C012 VDR-U27-C011.
- Data loading: template loader (CAP-03); pack XML data (reports, views) loaded by module loader; Thai pack ships 2 data files and 1 demo file VDR-U27-C180 VDR-U27-C181 VDR-U27-C203.
- Hooks: Thai post-init VDR-U27-C176 VDR-U27-C177 VDR-U27-C178; pre-init VDR-U27-C195; scoped post-init patterns VDR-U27-C192 VDR-U27-C193 VDR-U27-C194; database-wide side effects VDR-U27-C188 VDR-U27-C189 VDR-U27-C190 VDR-U27-C191 VDR-U27-C248.
- Update/migration: VDR-U27-C185 VDR-U27-C186 VDR-U27-C187 VDR-U27-C182.
- Uninstall: VDR-U27-C183 VDR-U27-C184 VDR-U27-C196 VDR-U27-C197 VDR-U27-C265.
- Versioning: VDR-U27-C179; counts VDR-U27-C201.
- Translations on term load VDR-U27-C198.

### D3 Logic
1. `ir.module.module.write(state->installed)` on a module with templates: if the current company has no chart and the module offers a template matching its country (or generic), a callback is stored on the registry and executed in `_register_hook` VDR-U27-C199 VDR-U27-C200.
2. Company-level: `res.company.create/write` -> `install_l10n_modules` -> `button_immediate_install` of country-linked auto-install modules -> account override loads chart in pre-commit VDR-U27-C010 VDR-U27-C014.
3. Upgrade: version bump + `end-migrate*` script -> `try_loading(code, company, force_create=False)` per company with that chart, ordered `parent_path` VDR-U27-C185 VDR-U27-C186; tag preservation helper at post-init VDR-U27-C178.
4. Uninstall: `module_uninstall` clears `chart_template` on companies using the module's templates; loader-created records stay under the `account` namespace VDR-U27-C183 VDR-U27-C184; document packs clear stored per-company formats VDR-U27-C196.
State list:
- `uninstalled -> installed [manual / auto-install / chart selection]` VDR-U27-C172 VDR-U27-C115
- `installed (no chart on company) -> chart loaded [first-template callback]` VDR-U27-C199
- `installed -> upgraded [migration script calls try_loading force_create=False]` VDR-U27-C185
- `installed -> uninstalled [chart_template cleared, records kept]` VDR-U27-C183

### Pack samples (manifest/dependency/hook entry points only)
See table T4 in section 8 and claims VDR-U27-C204 VDR-U27-C205 VDR-U27-C206 VDR-U27-C207 VDR-U27-C208 VDR-U27-C212 VDR-U27-C213 VDR-U27-C214 VDR-U27-C215 VDR-U27-C216 VDR-U27-C218 VDR-U27-C210.

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Auto-install with accounting + company country -> template loaded -> post-init tag preservation (VDR-U27-C175 VDR-U27-C199 VDR-U27-C177). |
| 2 | Reversal/negative | Uninstall clears chart selection but keeps records (VDR-U27-C183 VDR-U27-C184); reinstall treats company as chartless (VDR-U27-C265). |
| 3 | Multi-company | Install is database-wide; hooks scoped by company country in some packs, database-wide in others (VDR-U27-C192 VDR-U27-C188 VDR-U27-C189 VDR-U27-C190). |
| 4 | Side effects | Group activation, rounding, language, identification type on all partners (VDR-U27-C188 VDR-U27-C189 VDR-U27-C191 VDR-U27-C190). |
| 5 | Configuration/optionality | Hooks, demo, migrations, countries and auto-install are individually optional (VDR-U27-C266 VDR-U27-C201). |
| 6 | Validation | Missing tags stop template loading (VDR-U27-C155). |
| 7 | Roles/permissions | Template load admin-only (VDR-U27-C114); Thai pack seeds no ACL/rule/group (VDR-U27-C180). |
| 8 | Scheduled/automated | Thai pack: none (0 cron/automation in DB); migrations run on upgrade (VDR-U27-C185). |
| 9 | Exception/failure | Template load errors surface at install; demo errors swallowed (VDR-U27-C122). |
| 10 | Accounting/compliance | Upgrade of tax data via `force_create=False` reload (VDR-U27-C185); existing-entry re-tagging is a separate optional tool (VDR-U27-C187). |

### DB reconciliation
Thai pack seeded rows in DB: account.report 3, ir.actions.report 1, ir.ui.view 3, ir.model.fields 14, ir.model.fields.selection 3, ir.model 5; ir.model.access 0, ir.rule 0, res.groups 0, ir.cron 0, base.automation 0 — equals source (no security/cron/automation data files) VDR-U27-C180. Module state: l10n_th installed, latest_version 19.0.2.0, demo false. 230 other l10n_* modules uninstalled; 188 l10n_* with auto_install flag; 1 l10n module with a version recorded.

### Unknown / Runtime
VDR-U27-C267 (RT) · VDR-U27-C265 (RT) · VDR-U27-C184 (RT) · behaviour of `skip_auto_install` config and of `button_immediate_install` inside create/write hooks (not read beyond the lines cited).

---

## CAP-U27-05 Extension-boundary taxonomy of packs (FUTURE OPTIONAL COUNTRY PACK facts)

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Classify the 227 foreign packs by what kind of extension they are, which core models and hooks they extend and how packs depend on one another, to inform the boundary between framework and pack. Facts only; no country rule studied; these packs are not in the current applicable scope.

### D2 Architecture
- Archetypes (recount vs heuristic) VDR-U27-C268 VDR-U27-C219 VDR-U27-C220 VDR-U27-C218 and profile corrections VDR-U27-C202 VDR-U27-C225 VDR-U27-C220 VDR-U27-C219.
- Extension counts by core model name VDR-U27-C224 (table T3).
- Hot hooks VDR-U27-C222 VDR-U27-C223.
- Families: VDR-U27-C221 VDR-U27-C207 VDR-U27-C208 VDR-U27-C209 VDR-U27-C210 VDR-U27-C211 VDR-U27-C216 VDR-U27-C218; framework contract VDR-U27-C217 VDR-U27-C250.
- Thai reference boundary VDR-U27-C227.
- Dependency pattern: 135 of 227 packs depend on at least one other l10n pack, 92 do not; in-degree leaders: l10n_syscohada 17, l10n_fr_account 9, l10n_din5008 8, l10n_gcc_invoice 8, l10n_latam_base 7, l10n_latam_invoice_document 6, l10n_in 5, l10n_es 5. Generic dependencies of the 227 packs: account 126, base_vat 43, account_edi_ubl_cii 39, base_iban 24, point_of_sale 18, base 9, account_debit_note 8, sale 7.

### D3 Logic
Archetype rule used for the recount (documented so it can be re-run): payroll/HR if a dependency starts with `hr` or the category is Human Resources; POS if it depends on `point_of_sale`/`pos_*` or category POS; chart if it hosts a template provider or the category is Account Charts; bridge if it depends on stock/sale/purchase/website_sale (or `_stock`, `_sale`, `_website_sale` modules) or the category is Sale/Purchase/Website/Sales; EDI if category EDI or it depends on an e-document/proxy/Peppol module; otherwise other. Ordering of the tests is as listed. Result: chart 125, edi 34, pos 24, bridge 24, other 16, hr 4 (heuristic: base country pack 116, edi 34, pos 17, bridge 16, payroll/hr 5, other extension 39); 43 disagreements (list kept in the scratchpad), mostly name-prefix and category cases.

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Chart packs host templates and extend the loader, company, partner, journal, tax (VDR-U27-C224). |
| 2 | Reversal/negative | Uninstall hooks exist for 14 packs (13 document packs, 1 regional tax pack) (VDR-U27-C196 VDR-U27-C197). |
| 3 | Multi-company | Regional families share templates through a parent chain (VDR-U27-C210 VDR-U27-C209). |
| 4 | Side effects | See CAP-04 side effects (VDR-U27-C188 VDR-U27-C189). |
| 5 | Configuration/optionality | Families, frameworks and hooks are optional layers (VDR-U27-C217). |
| 6 | Validation | NOT APPLICABLE at taxonomy level. |
| 7 | Roles/permissions | NOT APPLICABLE — no rule content studied. |
| 8 | Scheduled/automated | NOT APPLICABLE. |
| 9 | Exception/failure | Heuristic misclassification risk (VDR-U27-C220 VDR-U27-C202). |
| 10 | Accounting/compliance | Not assessed (no country rule studied). |

### DB reconciliation
Only `l10n_th` is installed in the DB (1 of 231 l10n modules). Of the 227 foreign packs none is installed (consistent with the scope classification). Profile counts for depends, auto_install, hooks and data files agree with an independent recount (0 disagreements on 5 columns x 227 packs) VDR-U27-C201.

### Unknown / Runtime
VDR-U27-C269 · profile column `core_acc_models_extended` unverifiable VDR-U27-C225 · `models_new`, `models_extended` and `tests_py` columns were not recounted.

---

## CAP-U27-06 Multi-jurisdiction coexistence in one database

**Function-ID(s):** MCT-F03 on sharing claims; otherwise FUNCTION MAPPING REQUIRED

### D1 Business purpose
Establish what Community supports when companies of different jurisdictions (for example a Thai company and a foreign-owned or foreign-parented entity) share one database, and where it breaks. All findings are from reading; the restored DB has one company so every item is `RT`.

### D2 Architecture
- Data scope: global company rules with `parent_of` VDR-U27-C231 VDR-U27-C232 VDR-U27-C233 VDR-U27-C234; consistency domain VDR-U27-C235; settings loads chart for the active company only VDR-U27-C244.
- Shared vs per-company: chart sharing and code per root VDR-U27-C236 VDR-U27-C237 VDR-U27-C238 (MCT-F03); tax uniqueness within root tree VDR-U27-C239 VDR-U27-C240; journals/sequences per company VDR-U27-C241; partner properties per company VDR-U27-C043.
- Lock dates: ancestor chain VDR-U27-C242 VDR-U27-C243.
- Currency/delegated fields VDR-U27-C020 VDR-U27-C022 VDR-U27-C023.
- Cross-company documents VDR-U27-C245 VDR-U27-C246.
- Cross-jurisdiction facility VDR-U27-C173 VDR-U27-C174 VDR-U27-C247.
- Database-wide pack effects VDR-U27-C248 VDR-U27-C188 VDR-U27-C190 VDR-U27-C191.
- Mixed jurisdiction keys inside the Thai pack VDR-U27-C159 VDR-U27-C228 VDR-U27-C229 VDR-U27-C230; guard-lint VDR-U27-C271.

### D3 Logic
- Two sibling root companies: each loads its own template (`try_loading` per company), its own taxes/tax groups/fiscal positions/journals (company required), shared global masters (countries, currencies, partners' tax numbers). Records are invisible across roots by global rules VDR-U27-C233 VDR-U27-C234.
- Parent and branch: branch sees the root's taxes, journals, positions through `parent_of` VDR-U27-C231, inherits currency/fiscal-year/storno/cash-basis VDR-U27-C020, takes root chart VDR-U27-C016, inherits max lock date VDR-U27-C242. Tax country check on documents depends on the branch's own fiscal country versus the root's tax country VDR-U27-C029 (RT).
- Cross-company: inter-company payment bridge posts clearing entries VDR-U27-C246; other flows UNKNOWN VDR-U27-C249.

### Company-structure cases (cross-reference U28)
| Case | Community fit | Pointers |
|---|---|---|
| Foreign-owned Thai subsidiary (own legal entity, THB, Thai chart) | Separate root company; cannot be a branch of a different-currency parent | VDR-U27-C259 VDR-U27-C022 VDR-U27-C024 |
| Thai branch of a Thai company | Branch company (shares chart, taxes, currency, inherits lock dates) or only a partner-level branch label | VDR-U27-C016 VDR-U27-C242 VDR-U27-C270 |
| Foreign parent consolidating Thai and foreign entities | No consolidation model established; reports per company | VDR-U27-C249 |
| Representative / regional office | No dedicated concept; company or partner only (UNKNOWN for statutory treatment) | VDR-U27-C270 |
| Thai company with foreign tax registration | Fiscal position with foreign tax number | VDR-U27-C032 VDR-U27-C028 |

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Separate roots with own charts coexist; branches share root configuration (VDR-U27-C233 VDR-U27-C016). |
| 2 | Reversal/negative | Hierarchy fixed (VDR-U27-C024); locks of parent bind branches (VDR-U27-C242). |
| 3 | Multi-company | This capability. |
| 4 | Side effects | Pack hooks act database-wide (VDR-U27-C248). |
| 5 | Configuration/optionality | Chart share through `company_ids`; foreign-tax facility optional (VDR-U27-C236 VDR-U27-C173). |
| 6 | Validation | Tax name uniqueness per root tree (VDR-U27-C239); tax country on documents (VDR-U27-C029). |
| 7 | Roles/permissions | Foreign taxes limited to accounting managers (VDR-U27-C174); global rules (VDR-U27-C233). |
| 8 | Scheduled/automated | NOT APPLICABLE. |
| 9 | Exception/failure | Mismatch errors (VDR-U27-C030); no consolidation (VDR-U27-C249). |
| 10 | Accounting/compliance | Mixed jurisdiction keys can disagree on one transaction (VDR-U27-C228 VDR-U27-C229 VDR-U27-C159). |

### DB reconciliation
1 company, 0 branches, 0 other roots: coexistence cannot be reconciled with DB. Rules in DB (5 global rules on journal, account, tax group, tax, fiscal position, `parent_of`) equal source. `account_payment_interco` installed (DB) matches VDR-U27-C245; its per-company interco settings were not read in the DB (fields on res_company not queried). `account_account_res_company_rel` has 147 rows (every account linked to the single company).

### Unknown / Runtime
VDR-U27-C249 · VDR-U27-C062 (RT) · cross-company posting with a differently-countried partner (RT) · branch with fiscal country different from root (RT) · behaviour of `account_enabled_tax_country_ids` access for non-member companies (read only).

---

## CAP-U27-07 Gaps and design-relevant observations

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
State, as observations and risks (not requirements), where Community's localization approach couples country behaviour to the core versus where it offers clean extension points, and record a neutral CANDIDATE architecture sketch in the neutral file only. The sketch is explicitly `CANDIDATE — NOT APPROVED DESIGN`.

### D2 Observations (each with pointers)
| # | Observation | Class | Pointers |
|---|---|---|---|
| O1 | Core literals: comparisons, lists, generic chart pinned to a country | coupling | VDR-U27-C089 VDR-U27-C090 VDR-U27-C086 VDR-U27-C063 VDR-U27-C273 VDR-U27-C277 |
| O2 | Shared e-document module is country-aware (40 comparisons, 7 country-named formats, regional builders) | coupling | VDR-U27-C101 VDR-U27-C102 VDR-U27-C103 VDR-U27-C278 |
| O3 | Core imports a country table from an optional module without declaring a dependency | coupling | VDR-U27-C050 VDR-U27-C051 VDR-U27-C052 |
| O4 | Packs override loader internals (post-load 7, load 5, utility bank accounts 4, ...) | coupling | VDR-U27-C226 |
| O5 | Same posting method overridden by 15 packs plus frameworks, guards per pack | risk | VDR-U27-C222 VDR-U27-C274 VDR-U27-C271 |
| O6 | Database-wide install side effects from single-country packs | risk | VDR-U27-C188 VDR-U27-C189 VDR-U27-C190 VDR-U27-C191 |
| O7 | Fiscal country change after entries unguarded; address/fiscal/currency independent | risk | VDR-U27-C062 VDR-U27-C258 |
| O8 | Branch cannot differ in currency; subsidiary of a different-currency parent must be a root | constraint | VDR-U27-C259 VDR-U27-C022 |
| O9 | Country duplicated between files (comment: keep aligned) | risk | VDR-U27-C252 |
| O10 | Chart guess for a country without pack depends on registry order | risk | VDR-U27-C253 |
| O11 | Template data of one pack reached from another via method inheritance on shared class | coupling | VDR-U27-C211 |
| O12 | Clean extension points: fiscal-position validator list, document selection, audit flag, format selection, extra-document dictionary, QR hooks, regional framework company method | clean | VDR-U27-C251 VDR-U27-C076 VDR-U27-C078 VDR-U27-C072 VDR-U27-C074 VDR-U27-C081 VDR-U27-C217 |
| O13 | Thai pack keys on three countries (company fiscal, partner, bank) | risk | VDR-U27-C159 VDR-U27-C228 VDR-U27-C229 |
| O14 | Auto-install by country only on first country assignment | constraint | VDR-U27-C012 |
| O15 | Reload leaves old and new taxes side by side | risk | VDR-U27-C262 |
| O16 | Profile heuristic errors (archetype, template column, core model count) | data quality | VDR-U27-C202 VDR-U27-C220 VDR-U27-C225 |

### D3 Candidate architecture sketch
The sketch (layers, contracts, lifecycle, company-to-jurisdiction assignment, rules, conformance checks, open risks) is written in vendor-free language in the NEUTRAL file, section "CANDIDATE — NOT APPROVED DESIGN". Derivation: O1-O16 above; clean extension points (O12) are the proposed contract surface; couplings (O1-O4, O11) are proposed to be moved behind contracts; risks (O5-O7, O13-O15) become rules and conformance checks. It is not a requirement and not approved.

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | NOT APPLICABLE — synthesis capability. |
| 2 | Reversal/negative | NOT APPLICABLE. |
| 3 | Multi-company | O7, O8, O13 and CAP-06. |
| 4 | Side effects | O6. |
| 5 | Configuration/optionality | O12, O14. |
| 6 | Validation | NOT APPLICABLE. |
| 7 | Roles/permissions | NOT APPLICABLE. |
| 8 | Scheduled/automated | NOT APPLICABLE. |
| 9 | Exception/failure | O10, O15. |
| 10 | Accounting/compliance | O1, O7; no country rule adopted. |

### DB reconciliation
NOT APPLICABLE beyond CAP-01 to CAP-06 reconciliations.

### Unknown / Runtime
VDR-U27-C275 (RT) · VDR-U27-C253 (RT).

---

## 8. Mechanical tables (restricted)

**T1 Profile verification (COUNTRY_PACK_BOUNDARY_PROFILE_227.tsv recounted from manifests and AST)**

| Profile column | Profile figure | Recount | Verdict |
|---|---|---|---|
| depends_count, auto_install, has_post_init_hook, has_uninstall_hook, data_files | per pack | per pack | 0 disagreements over 227 packs |
| auto_install True | 186 | 186 (129 list form + 57 true form) | agrees |
| has_post_init_hook / has_uninstall_hook | 30 / 14 | 30 / 14 (pre-init hook: 2, not in profile) | agrees |
| template_data_files > 0 | 10 packs | 125 packs have data/template dir; 115 have a template-level provider | CONTRA: column does not measure template data |
| archetype 'base country pack' | 116 | chart 125 | corrected: +8 chart packs the heuristic called 'other extension', +2 Croatian chart packs it called payroll, -1 layout pack (DIN 5008) it counted as base |
| archetype 'payroll/hr' | 5 | 3 time-off packs (+1 expense layout) | CONTRA: two Croatian chart packs misclassified by name prefix |
| archetype 'pos' | 17 | 24 | POS-bridge document packs counted as 'edi' by the heuristic |
| archetype 'edi' | 34 | 34 | agrees in total only: 14 document packs sit in its 'other extension' and 14 of its 'edi' packs are POS, bridge or other |
| archetype 'stock/sale/purchase/website bridge' | 16 | 24 | differs |
| archetype 'other extension' | 39 | 16 | differs |
| core_acc_models_extended > 0 | 119 packs | 176 (incl. loader) or 104 (excl. loader) | not reproducible, unverified |
| models_extended > 0 | 210 | 210 | agrees |
| models_new > 0, tests_py > 0 | 58, 97 | not recounted | not verified |

Claims: VDR-U27-C201 VDR-U27-C202 VDR-U27-C268 VDR-U27-C225 VDR-U27-C220 VDR-U27-C219.

**T2 Country-conditional code in the core family (31 modules), by kind**

| Kind | Count | Where (module: count) | Classification | Example claims |
|---|---|---|---|---|
| Literal country comparison (code) | 47 | account_edi_ubl_cii 40, base_vat 4, account 2, account_peppol 1 (account_peppol_response 1 hit excluded: response codes) | country-specific logic inside shared modules | VDR-U27-C101 VDR-U27-C089 VDR-U27-C096 VDR-U27-C097 |
| Literal country list | 11 | account 6 (company.py 5, chart_template.py 1), account_edi_ubl_cii 2, account_peppol 2, account_qr_code_sepa 1 | fixed country knowledge | VDR-U27-C090 VDR-U27-C092 VDR-U27-C094 VDR-U27-C098 |
| Literal country table (dict) | 4 | account 1 (structured reference), account_edi_ubl_cii 1 (address scheme by country), base_vat 1 (62 samples), base_iban 1 (70 templates) | fixed country knowledge | VDR-U27-C093 VDR-U27-C104 VDR-U27-C099 VDR-U27-C100 |
| Literal country comparison in views | 6 | account views 4 (report_invoice.xml 3, res_config_settings_views.xml 1), account_check_printing views 2 | country-specific presentation | VDR-U27-C086 VDR-U27-C087 VDR-U27-C088 |
| Country exposed as data (fiscal country code pattern, Python) | 38 occurrences in 9 core modules (112 in 48 packs) | account 28, account_peppol 2, stock_account 2, base_setup/base_vat/hr/point_of_sale/purchase/sale 1 each | generic mechanism | VDR-U27-C084 VDR-U27-C085 |
| Country condition pattern in views | 30 occurrences in 9 core modules (452 in 98 packs) | account 17, hr 4, account_check_printing 2, stock_delivery 2, others 1 | generic mechanism for pack visibility | VDR-U27-C260 |
| Country-named formats | 7 selection values | account_edi_ubl_cii res.partner | country-named registration in shared module | VDR-U27-C102 |
| Regional logic in detection | 1 | account partner fiscal-position detection (EU group) | hard-wired regional case | VDR-U27-C041 |
| Template-literal guard | 2 template codes | account chart_template (regional families) | hard-wired template guard | VDR-U27-C095 |

**T3a Core models extended by the 227 packs (count of packs, top 25)**

| Model | Packs |
|---|---|
| account.chart.template | 128 |
| account.move | 87 |
| res.company | 69 |
| res.partner | 65 |
| res.config.settings | 37 |
| account.tax | 35 |
| account.journal | 30 |
| account.move.send | 24 |
| account.move.line | 18 |
| product.template | 15 |
| pos.config | 14 |
| pos.order | 14 |
| res.partner.bank | 11 |
| account.move.reversal | 10 |
| stock.picking | 9 |
| uom.uom | 8 |
| account.payment | 8 |
| base.document.layout | 8 |
| sale.order | 7 |
| pos.session | 6 |
| account_edi_proxy_client.user | 6 |
| account.move.send.wizard | 6 |
| ir.attachment | 6 |
| account.fiscal.position | 5 |
| account.account | 5 |

Distinct models extended: 86; by >=5 packs: 26; by >=10 packs: 14 VDR-U27-C224

**T3b Most overridden core methods by packs (distinct packs, top 28, compute methods excluded)**

| Packs | Model::method |
|---|---|
| 15 | account.move::_post |
| 15 | account.move::_get_name_invoice_report |
| 15 | account.move.send::_get_all_extra_edis |
| 13 | res.partner::_commercial_fields |
| 13 | account.move.send::_get_alerts |
| 12 | account.move::button_draft |
| 11 | account.move::_get_import_file_type |
| 11 | account.move.send::_call_web_service_before_invoice_pdf_render |
| 9 | res.partner::_get_ubl_cii_formats_info |
| 9 | res.partner::_get_edi_builder |
| 9 | account.move.send::_get_invoice_extra_attachments |
| 8 | account.move::_auto_init |
| 8 | account.move.send::_call_web_service_after_invoice_pdf_render |
| 8 | account.move.reversal::_prepare_default_reversal |
| 7 | res.partner::_get_frontend_writable_fields |
| 7 | res.partner::_get_company_registry_labels |
| 7 | res.partner.bank::_get_error_messages_for_qr |
| 7 | res.partner.bank::_check_for_qr_code_errors |
| 7 | res.company::_localization_use_documents |
| 7 | account.move::_get_fields_to_detach |
| 7 | account.move.send::_hook_invoice_document_before_pdf_report_render |
| 7 | account.chart.template::_post_load_data |
| 6 | res.company::write |
| 6 | res.company::_load_pos_data_fields |
| 6 | res.company::_is_latam |
| 6 | account.move::_get_starting_sequence |
| 6 | account.move::_get_last_sequence_domain |
| 6 | account.move::_get_l10n_latam_documents_domain |

Source: AST scan of `_inherit`-only classes in 227 packs excluding tests/demo/migrations; counts of method overrides by distinct pack VDR-U27-C222 VDR-U27-C223.

**T4 Pack samples (manifest, dependency, hook entry points only)**

| Pack | Category | countries | auto_install | depends | hooks (pre/post/uninstall) | data/demo files | template codes hosted | models extended (count) |
|---|---|---|---|---|---|---|---|---|
| l10n_th | Accounting/Localizations/Account Charts | th | list ['account'] | account_qr_code_emv, account | -/_preserve_tag_on_taxes/- | 2/1 | th | 5 |
| l10n_de | Accounting/Localizations/Account Charts | de | list ['account'] | base_iban, base_vat, l10n_din5008, account, account_edi_ubl_cii | -/_post_init_hook/- | 4/1 | de_skr03,de_skr04 | 9 |
| l10n_in | Accounting/Localizations/Account Charts | in | list ['account'] | account_tax_python, base_vat, account_debit_note, account, iap | -/post_init/- | 34/2 | in | 15 |
| l10n_ar | Accounting/Localizations/Account Charts | ar | list ['account'] | l10n_latam_invoice_document, l10n_latam_base, account | -/-/- | 25/10 | ar_base,ar_ex,ar_ri | 15 |
| l10n_be | Accounting/Localizations/Account Charts | be | list ['account'] | account, account_edi_ubl_cii, base_iban, base_vat | -/-/- | 3/1 | be,be_asso,be_comp | 5 |
| l10n_fr_account | Accounting/Localizations/Account Charts | fr | list ['account'] | base_iban, base_vat, account, account_edi_ubl_cii, l10n_fr | -/_l10n_fr_post_init_hook/- | 7/1 | fr,gf,gp,mc,mq,re,yt | 5 |
| l10n_gf | Accounting/Localizations/Account Charts | gf | list ['account'] | l10n_fr_account, account | -/-/- | 0/0 | - | 0 |
| l10n_syscohada | Accounting/Localizations/Account Charts | - | False | account | -/-/- | 1/0 | syscebnl,syscohada | 1 |
| l10n_bf | Accounting/Localizations/Account Charts | bf | list ['account'] | l10n_syscohada, account | -/-/- | 1/1 | bf,bf_syscebnl | 1 |
| l10n_eu_oss | Accounting/Localizations | - | False | account | -/-/l10n_eu_oss_uninstall | 1/0 | - | 2 |
| l10n_it_edi | Accounting/Localizations/EDI | - | list ['l10n_it'] | l10n_it, account_edi_proxy_client, account_debit_note | -/_l10n_it_edi_post_init/uninstall_hook | 13/1 | - | 9 |
| l10n_dk_nemhandel | Accounting/Localizations/EDI | - | list ['account_edi_ubl_cii', 'l10n_dk'] | account_edi_proxy_client, account_edi_ubl_cii, l10n_dk | _pre_init_nemhandel/_post_init_nemhandel/uninstall_hook | 8/1 | - | 9 |
| l10n_sa_edi | Accounting/Localizations/EDI | sa | False | account_edi, account_edi_ubl_cii, l10n_sa, base_vat, certificate | -/_l10n_sa_edi_post_init/- | 13/1 | - | 13 |
| l10n_pe_pos | Accounting/Localizations/Point of Sale | - | True | l10n_pe, point_of_sale | -/-/- | 2/0 | - | 3 |
| l10n_latam_base | Accounting/Localizations | - | False | contacts, base_vat | -/_set_default_identification_type/- | 6/0 | - | 2 |
| l10n_latam_invoice_document | Accounting/Localizations | - | False | account, account_debit_note | -/-/- | 8/0 | - | 8 |
| l10n_din5008 | Accounting/Localizations | de,ch | True | account | -/-/- | 5/0 | - | 4 |
| l10n_gcc_invoice | Accounting/Localizations | - | False | account | -/_l10n_gcc_invoice_post_init/- | 2/0 | - | 5 |
| l10n_hr | Accounting/Localizations/Account Charts | hr | list ['account'] | account, base_vat | -/-/- | 2/1 | hr | 1 |
| l10n_fr_hr_holidays | Human Resources/Time Off | fr | list ['hr_holidays'] | hr_holidays | -/-/- | 1/1 | - | 3 |

Facts read from manifests (and `__init__.py` hook entry points for hooks); no rule content. Claims: VDR-U27-C204 VDR-U27-C205 VDR-U27-C206 VDR-U27-C207 VDR-U27-C208 VDR-U27-C212 VDR-U27-C213 VDR-U27-C214 VDR-U27-C215 VDR-U27-C216 VDR-U27-C218 VDR-U27-C210 VDR-U27-C175.

---

## 9. DISCOVERED SUPPORTING MODULES

Read only as far as needed: `base` (company tree, country install trigger, module registry, `res.partner.vat`), `base_vat` (hook override and country table; not installed in the DB), `account_edi` (legacy format registry; installed), `account_edi_ubl_cii` (format selection, builder/format-info hooks, country-literal scan; installed), `account_qr_code_emv` (QR hook defaults; installed), `account_qr_code_sepa` (country literal set; installed), `account_payment_interco` (inter-company bridge; installed), `account_update_tax_tags` (manifest only; not installed), `account_peppol` (country lists only; not installed), `account_check_printing` (one view condition; installed), `base_iban` (country table; installed), `l10n_latam_base` and `l10n_latam_invoice_document` (regional framework, manifests and hook contract; not installed), `l10n_fr_account`, `l10n_syscohada`, `l10n_bf`, `l10n_gf` (family/template-parent mechanism, manifests and template registry headers only), `l10n_din5008`, `l10n_gcc_invoice` (layout/regional packs, manifests), `l10n_eu_oss`, `l10n_it_edi`, `l10n_sa_edi`, `l10n_dk_nemhandel`, `l10n_pe_pos`, `l10n_de`, `l10n_in`, `l10n_ar`, `l10n_be`, `l10n_hr`, `l10n_fr_hr_holidays` (manifests and hook entry points only: FUTURE OPTIONAL COUNTRY PACK facts), `l10n_ch` (one migration script, pattern only). No foreign pack accounting/tax rule was studied.

## 10. Contradictions with prior evidence and profile
- CONTRA vs the supplied profile: `template_data_files` column, the `payroll/hr` class (l10n_hr, l10n_hr_kuna) and `core_acc_models_extended` (119) — see T1 and claims VDR-U27-C202 VDR-U27-C220 VDR-U27-C225. No contradiction with U13/U01/U11 findings was found; U13 CAP-U13-03 loader flow is consistent with CAP-U27-03 (this unit adds the registry scan, reload semantics for taxes/accounts/journals, branch handling and the foreign-tax facility).
- Observation extending U13: the generic template pins a non-Thai fiscal country and Anglo-Saxon stock accounting VDR-U27-C063 VDR-U27-C064; for the Thai database this is moot because the Thai template is loaded, but it matters for the neutral core.

## 11. Claims
| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U27-C001 | FUNCTION MAPPING REQUIRED | account/models/company.py:203 | account_fiscal_country_id = fields.Many2one( | FACT | always | — | Company has a stored, computed but user-writable fiscal country field described as the country whose tax reports the company uses. | N-U27-001 |
| VDR-U27-C002 | FUNCTION MAPPING REQUIRED | account/models/company.py:389 | if not record.account_fiscal_country_id: | FACT | always | — | The compute only fills the fiscal country from the company country when the fiscal country is still empty; afterwards it is independent of the address country. | N-U27-002 |
| VDR-U27-C003 | FUNCTION MAPPING REQUIRED | account/models/company.py:117 | chart_template = fields.Selection | FACT | always | — | Company stores the code of the chart template it was last loaded with, as a selection whose options depend on the company country. | N-U27-001 |
| VDR-U27-C004 | FUNCTION MAPPING REQUIRED | account/models/company.py:998 | def _chart_template_selection | FACT | always | — | The selectable chart templates are computed from the company country by the loader's selection function. | N-U27-001 |
| VDR-U27-C005 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:128 | t[1]['country_id'] != country.id | FACT | always | — | Template selection sorts the registry so that templates whose country equals the company country come first; _guess_chart_template simply takes the first entry. | N-U27-003 |
| VDR-U27-C006 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:132 | def _guess_chart_template | FACT | always | — | Guessing a template for a country returns the first element of the country-sorted selection. | N-U27-003 |
| VDR-U27-C007 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:826 | self._update_countries(terp.get('countries', [])) | FACT | module registry refresh | — | The manifest key 'countries' is synchronised into a module-to-country link table every time module metadata is refreshed. | N-U27-003 |
| VDR-U27-C008 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:847 | INSERT INTO module_country | FACT | module registry refresh | — | _update_countries inserts and deletes rows of the module_country link table so that it equals the countries listed in the manifest. | N-U27-003 |
| VDR-U27-C009 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:207 | def _compute_uninstalled_l10n_module_ids | FACT | always | — | Company computes the list of not-yet-installed auto-install modules linked to its country; the comment states it does not recurse and leaves the rest to button_install. | N-U27-003 |
| VDR-U27-C010 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:243 | def install_l10n_modules | FACT | registry ready and not in test mode | — | install_l10n_modules installs the country-linked uninstalled modules immediately, but only when the registry is ready and the call is not a test, import or install-mode call. | N-U27-003 |
| VDR-U27-C011 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:334 | companies_needs_l10n = companies.filtered('country_id') | FACT | company created with a country | — | On company creation, country-linked pack installation is triggered for companies that have a country. | N-U27-014 |
| VDR-U27-C012 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:371 | and self.filtered(lambda company: not company.country_id) | FACT | country written on company | — | On write, pack installation is triggered only for companies that had no country before; changing an existing country triggers nothing. | N-U27-014 |
| VDR-U27-C013 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:421 | module.country_ids & company_countries | FACT | module installation | — | An auto-install module that has countries is installed only if at least one existing company (any company in the database) has one of its countries. | N-U27-003 |
| VDR-U27-C014 | FUNCTION MAPPING REQUIRED | account/models/company.py:983 | if template_code != 'generic_coa': | FACT | accounting installed, company has country and no chart | — | After pack installation, a company with a country and without a chart gets a chart loaded in a pre-commit callback, using the parent's template or the country guess, unless the guess is the generic chart. | N-U27-003 |
| VDR-U27-C015 | FUNCTION MAPPING REQUIRED | account/models/company.py:982 | company.parent_id.chart_template or | FACT | branch company | — | For a company that has a parent, the parent's chart template takes precedence over guessing from the branch's own country. | N-U27-011 |
| VDR-U27-C016 | FUNCTION MAPPING REQUIRED | account/models/company.py:491 | if root_template := company.parent_ids[0].chart_template: | FACT | company created under a root that has a chart | — | A newly created company whose root has a chart template loads that same template in a pre-commit callback with demo disabled. | N-U27-011 |
| VDR-U27-C017 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:188 | company.country_id = chart_template_mapping.get('country_id') | FACT | loading a template on a company without country | — | If the company has no country, loading a template sets the company country to the template country. | N-U27-003 |
| VDR-U27-C018 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:509 | vals['currency_id'] = fiscal_country.currency_id.id | FACT | no accounting entries on the company tree | — | While the company tree has no entries, pre-load sets the company currency to the currency of the fiscal country named by the template (or current fiscal country). | N-U27-011 |
| VDR-U27-C019 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:507 | vals['currency_id'] = company.parent_id.currency_id.id | FACT | branch company | — | For a branch the loader takes the parent's currency instead. | N-U27-011 |
| VDR-U27-C020 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:119 | return ['currency_id'] | FACT | always | — | The base company model delegates its currency to the root company; account extends the same list with fiscal-year end day and month, storno flag and cash-basis switch. | N-U27-009 |
| VDR-U27-C021 | FUNCTION MAPPING REQUIRED | account/models/company.py:313 | 'fiscalyear_last_day', | FACT | accounting installed | — | Accounting adds fiscal-year end, storno and cash-basis switch to the root-delegated fields of a company tree. | N-U27-009 |
| VDR-U27-C022 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:433 | must be the same as it's | FACT | always | — | A constraint rejects a subsidiary whose delegated field differs from its root's value. | N-U27-009 |
| VDR-U27-C023 | FUNCTION MAPPING REQUIRED | account/models/company.py:759 | You cannot change the currency of | FACT | company tree has journal items | — | Writing a different currency on a company is refused once any journal item exists in its root's tree. | N-U27-009 |
| VDR-U27-C024 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:358 | The company hierarchy cannot be changed. | FACT | always | — | Writing the parent of an existing company raises an error: the tree cannot be reorganised after creation. | N-U27-010 |
| VDR-U27-C025 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:197 | self.currency_id = self.country_id.currency_id | FACT | form onchange | — | Selecting a country in the company form proposes that country's currency. | N-U27-001 |
| VDR-U27-C026 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:301 | tax.country_id = tax.company_id.account_fiscal_country_id or tax.company_id.country_id or | FACT | always | — | A tax's country is stored, computed from its company's fiscal country (else company country), and may be edited. | N-U27-012 |
| VDR-U27-C027 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:68 | group.country_id = group.company_id.account_fiscal_country_id or group.company_id.country_id | FACT | always | — | A tax group's country is likewise computed from its company's fiscal country. | N-U27-012 |
| VDR-U27-C028 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1946 | foreign_vat_records = self.filtered(lambda r: r.fiscal_position_id.foreign_vat) | FACT | always | — | A document's tax country is the country of its fiscal position when that position carries a foreign tax number, otherwise the fiscal country of the document's company. | N-U27-006 |
| VDR-U27-C029 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2858 | def _validate_taxes_country | FACT | on create or write of lines, fiscal position or company | — | A constraint compares the countries of all taxes on the document's lines with the document's tax country and raises if they differ. | N-U27-012 |
| VDR-U27-C030 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2870 | incompatible with your fiscal country | FACT | tax country mismatch without fiscal position | — | The error text for a mismatch tells the user to check the company fiscal country and the tax country. | N-U27-012 |
| VDR-U27-C031 | FUNCTION MAPPING REQUIRED | account/models/partner.py:39 | string='Company', required=True, readonly=True, index=True | FACT | always | — | Every fiscal position belongs to exactly one company (required, read-only after creation). | N-U27-001 |
| VDR-U27-C032 | FUNCTION MAPPING REQUIRED | account/models/partner.py:66 | foreign_vat = fields.Char(string="Foreign Tax ID" | FACT | always | — | A fiscal position can carry the company's own tax number in the region it maps, which turns it into a foreign registration. | N-U27-006 |
| VDR-U27-C033 | FUNCTION MAPPING REQUIRED | account/models/partner.py:139 | A fiscal position with a foreign | FACT | always | — | Within a company, foreign-registration fiscal positions of one country must carry the same foreign tax number (a second, different number in the same country is refused). | N-U27-006 |
| VDR-U27-C034 | FUNCTION MAPPING REQUIRED | account/models/company.py:238 | multi_vat_foreign_country_ids = fields.Many2many( | FACT | always | — | Company exposes the list of countries for which it has a foreign tax number, computed from its fiscal positions. | N-U27-006 |
| VDR-U27-C035 | FUNCTION MAPPING REQUIRED | account/models/company.py:403 | record.account_enabled_tax_country_ids = foreign_vat_fpos.country_id + record.account_fiscal_country_id | FACT | always | — | The countries for which a company uses tax features equal its fiscal country plus the countries of its foreign-registration positions. | N-U27-006 |
| VDR-U27-C036 | FUNCTION MAPPING REQUIRED | account/models/company.py:361 | company.domestic_fiscal_position_id = potential_domestic_fps[0] if potential_domestic_fps else | FACT | always | — | A company's domestic fiscal position is the first position matching the company's country (or a group containing it). | N-U27-005 |
| VDR-U27-C037 | FUNCTION MAPPING REQUIRED | account/models/partner.py:209 | company specific first, then sequence | FACT | always | — | Matching tries fiscal positions of the most specific company first (deeper in the tree), then by sequence, and returns the first that passes all validators. | N-U27-005 |
| VDR-U27-C038 | FUNCTION MAPPING REQUIRED | account/models/partner.py:215 | def _get_fpos_validation_functions | FACT | always | — | The validators are an overridable list: tax number required, postal range, region, country, country group (with excluded regions). | N-U27-005 |
| VDR-U27-C039 | FUNCTION MAPPING REQUIRED | account/models/partner.py:266 | partner manually set fiscal position always | FACT | always | — | A fiscal position set on the delivery partner or the partner overrides automatic detection. | N-U27-005 |
| VDR-U27-C040 | FUNCTION MAPPING REQUIRED | account/models/partner.py:277 | all_auto_apply_fpos = self.search | FACT | always | — | Automatic detection considers only positions flagged for auto-apply that belong to the current company's allowed set. | N-U27-005 |
| VDR-U27-C041 | FUNCTION MAPPING REQUIRED | account/models/partner.py:258 | eu_country_codes = set(self.env.ref('base.europe') | FACT | both company and partner have a tax number | — | Core fiscal-position detection reads the first two characters of both tax numbers and compares them with the members of the Europe country group to decide on an intra-EU case. | N-U27-028 |
| VDR-U27-C042 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1049 | .with_company(move.company_id)._get_fiscal_position( | FACT | always | — | A document computes its fiscal position in the context of the document's own company. | N-U27-005 |
| VDR-U27-C043 | FUNCTION MAPPING REQUIRED | account/models/partner.py:555 | property_account_position_id = fields.Many2one('account.fiscal.position', company_dependent=True | FACT | always | — | A partner's fiscal position (and receivable, payable, payment terms) are company-dependent values. | N-U27-018 |
| VDR-U27-C044 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:237 | vat = fields.Char(string='Tax ID' | FACT | always | — | The partner tax number is a single database-wide field, not company-dependent. | N-U27-018 |
| VDR-U27-C045 | FUNCTION MAPPING REQUIRED | account/models/partner.py:873 | return vat, country and country.code or | FACT | base_vat not installed | — | Core partner check _run_vat_checks is a no-op that returns the number unchanged together with the country code. | N-U27-015 |
| VDR-U27-C046 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:107 | def _run_vat_checks | FACT | base_vat installed | — | The validation component overrides the hook to infer the country from the number's prefix, format the number and validate it. | N-U27-004 |
| VDR-U27-C047 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:118 | vat_prefix, vat_number = self._split_vat(vat) | FACT | base_vat installed | — | The number is split into prefix and number; the prefix is compared with the country group of prefixed countries and, where applicable, used as the country of the check. | N-U27-013 |
| VDR-U27-C048 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:348 | check_func_name = 'check_vat_' + country_code.lower() | FACT | base_vat installed | — | Per-country validators are found by naming convention (a method called check_vat_ plus the country code) with a fallback to an external library; a country without validator is accepted. | N-U27-004 |
| VDR-U27-C049 | FUNCTION MAPPING REQUIRED | account/models/partner.py:1124 | def _deduce_country_code | FACT | always | — | A helper deduces the country of a number from its prefix, falling back to the partner country. | N-U27-013 |
| VDR-U27-C050 | FUNCTION MAPPING REQUIRED | account/models/company.py:14 | from odoo.addons.base_vat.models.res_partner import _ref_vat | FACT | always | — | The core company model imports a country table from the optional validation module at source level even though the core manifest does not depend on it. | N-U27-022 |
| VDR-U27-C051 | FUNCTION MAPPING REQUIRED | account/models/partner.py:14 | from odoo.addons.base_vat.models.res_partner import _ref_vat | FACT | always | — | The same source-level import exists in the core partner extension. | N-U27-022 |
| VDR-U27-C052 | FUNCTION MAPPING REQUIRED | account/__manifest__.py:17 | 'depends': ['base_setup', 'onboarding', 'product', 'analytic', 'portal', | FACT | always | — | The core accounting manifest declares no dependency on the tax-number validation module nor on any country pack. | N-U27-022 |
| VDR-U27-C053 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:73 | availability_condition = fields.Selection( | FACT | always | — | A report is available by one of three conditions: country matches, chart of accounts matches, always. | N-U27-056 |
| VDR-U27-C054 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:259 | The Availability is set to 'Country | FACT | always | — | A report conditioned on country must name its country. | N-U27-056 |
| VDR-U27-C055 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:15 | country_id = fields.Many2one | FACT | always | — | A tax-report tag carries the country for which it is available when applied on taxes; names are unique per country and applicability. | N-U27-055 |
| VDR-U27-C056 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:23 | unique(name, applicability, country_id) | FACT | always | — | Tag uniqueness is (name, applicability, country). | N-U27-055 |
| VDR-U27-C057 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5351 | allowed_country_ids = (False, rep_line.company_id.account_fiscal_country_id.id | FACT | always | — | Tags selectable on a tax distribution line are limited to tags without country, tags of the company's fiscal country and tags of its foreign-registration countries. | N-U27-006 |
| VDR-U27-C058 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:5 | 'countries': ['th'] | FACT | always | — | The Thailand pack declares itself for one country through the countries key. | N-U27-003 |
| VDR-U27-C059 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:23 | 'account_fiscal_country_id': 'base.th' | FACT | th template loaded | — | The Thailand template sets the company fiscal country to Thailand through its company-values provider; currency follows from the fiscal country at load time. | N-U27-001 |
| VDR-U27-C060 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:22 | self.env.company.id: { | OBSERVATION | restored database | — | Restored database: 1 company, no parent; chart template th; fiscal country = Thailand; company address country = Thailand; currency THB; cash-basis tax switch on; anglo-saxon flag off; 0 fiscal positions; 18 taxes and 5 tax groups, all with country Thailand; 1 installed l10n module (th); 188 localization modules carry the auto-install flag; module_country has 179 rows covering 157 modules. | N-U27-007 |
| VDR-U27-C061 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:17 | 'account_qr_code_emv', | OBSERVATION | restored database | — | Thailand pack depends on the QR module and the core only; tax-number validation (base_vat) is uninstalled in the restored database, so the core no-op validator is in effect. | N-U27-015 |
| VDR-U27-C062 | FUNCTION MAPPING REQUIRED | account/models/company.py:387 | def compute_account_tax_fiscal_country | INFERENCE | always | RT | Reading company.py for constraints and write guards (currency guard line 759, price-include guard lines 326-328, hierarchy guard in base) found none on account_fiscal_country_id after entries exist; not executed (RT). | N-U27-019 |
| VDR-U27-C063 | FUNCTION MAPPING REQUIRED | account/models/template_generic_coa.py:36 | 'account_fiscal_country_id': 'base.us' | FACT | generic chart loaded | — | The generic chart of accounts template pins the company fiscal country to the United States and switches anglo-saxon valuation on. | N-U27-016 |
| VDR-U27-C064 | FUNCTION MAPPING REQUIRED | account/models/template_generic_coa.py:35 | 'anglo_saxon_accounting': True, | FACT | generic chart loaded | — | The generic template also sets anglo-saxon accounting on; a template that does not set it gets False through setdefault. | N-U27-016 |
| VDR-U27-C065 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:514 | vals.setdefault('anglo_saxon_accounting', False) | FACT | any template load | — | The loader writes anglo_saxon_accounting False when the template does not specify it. | N-U27-016 |
| VDR-U27-C066 | FUNCTION MAPPING REQUIRED | account/models/template_generic_coa.py:8 | @template('generic_coa') | FACT | always | — | The core module itself registers one chart template (generic_coa) with CSV data under account/data/template, so the core is usable without any country pack. | N-U27-024 |
| VDR-U27-C067 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:35 | module.name == 'account' | FACT | always | — | The template registry scan covers modules of the localization category and the core module itself. | N-U27-024 |
| VDR-U27-C068 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5569 | def _post(self, soft=True): | FACT | always | — | Entry posting is a core method with a soft flag; country packs extend it by override. | N-U27-024 |
| VDR-U27-C069 | FUNCTION MAPPING REQUIRED | account/models/company.py:57 | SOFT_LOCK_DATE_FIELDS = [ | FACT | always | — | Soft lock-date fields (fiscal year, tax, sale, purchase) and a hard lock date are defined in the core company. | N-U27-024 |
| VDR-U27-C070 | FUNCTION MAPPING REQUIRED | account/models/sequence_mixin.py:267 | return "00000000" | FACT | always | — | The core sequence mixin defines the default starting sequence (and, at lines 43-44, the monthly and yearly regular expressions) used to parse and continue numbers. | N-U27-024 |
| VDR-U27-C071 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:86 | return self.journal_id.sequence_override_regex or super()._sequence_monthly_regex | FACT | always | — | A journal can override the number-parsing pattern, a core mechanism for atypical numbering schemes. | N-U27-043 |
| VDR-U27-C072 | FUNCTION MAPPING REQUIRED | account/models/partner.py:587 | selection=[],  # to extend | FACT | always | — | The partner's electronic-invoice format is a selection that is empty in the core and is meant to be extended by other modules. | N-U27-040 |
| VDR-U27-C073 | FUNCTION MAPPING REQUIRED | account/models/partner.py:706 | # TO OVERRIDE | FACT | always | — | The suggested electronic-invoice format for a partner is a no-op hook returning False, marked TO OVERRIDE. | N-U27-040 |
| VDR-U27-C074 | FUNCTION MAPPING REQUIRED | account/models/account_move_send.py:31 | def _get_all_extra_edis | FACT | always | — | The sending wizard exposes a dictionary of extra electronic documents (label, applicability function, help) that is empty in the core. | N-U27-040 |
| VDR-U27-C075 | FUNCTION MAPPING REQUIRED | account/models/account_move_send.py:387 | TO OVERRIDE - used to determine | FACT | always | — | Whether a sending method is shown for a company is an overridable hook defaulting to True. | N-U27-040 |
| VDR-U27-C076 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7374 | This method need to be inherit | FACT | always | — | The core invoice-report selection hook states in its docstring that localizations inherit it to print a custom invoice report; the default is the core report. | N-U27-039 |
| VDR-U27-C077 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:65 | name="invoice_title" | FACT | always | — | The core invoice layout exposes the document title as a named, replaceable block. | N-U27-039 |
| VDR-U27-C078 | FUNCTION MAPPING REQUIRED | account/models/company.py:347 | def _compute_force_restrictive_audit_trail | FACT | always | — | A company-level compliance flag (forced audit trail) is computed False in the core and designed to be overridden per company by packs. | N-U27-026 |
| VDR-U27-C079 | FUNCTION MAPPING REQUIRED | account/models/company.py:323 | Can't disable restricted audit trail: forced | FACT | always | — | The core constraint refuses switching off the restrictive audit trail when a localization forces it. | N-U27-026 |
| VDR-U27-C080 | FUNCTION MAPPING REQUIRED | account/models/partner.py:883 | def get_partner_localisation_fields_required_to_invoice | FACT | always | — | A hook returning the partner fields legally required to invoice for a country returns an empty list in the core. | N-U27-026 |
| VDR-U27-C081 | FUNCTION MAPPING REQUIRED | account/models/res_partner_bank.py:253 | def _get_error_messages_for_qr | FACT | always | — | The core bank-account model defines QR eligibility and data-check hooks (_get_error_messages_for_qr, _check_for_qr_code_errors) returning None. | N-U27-041 |
| VDR-U27-C082 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:52 | return None, None | FACT | EMV QR module installed | — | The EMV QR module defines the merchant-account hook as returning no data, to be supplied per country by packs. | N-U27-041 |
| VDR-U27-C083 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:124 | ('emv_qr', _("EMV Merchant-Presented QR-code"), 30) | FACT | EMV QR module installed | — | A QR method is registered by appending (code, label, priority) to the available-methods list. | N-U27-041 |
| VDR-U27-C084 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:299 | country_code = fields.Char(related='company_id.account_fiscal_country_id.code' | FACT | always | — | Sale orders expose the company's fiscal country code as a related field for view conditions; the same exposure exists on purchase, stock transfers, stock picking types, POS orders and invoices. | N-U27-027 |
| VDR-U27-C085 | FUNCTION MAPPING REQUIRED | account/models/uom_uom.py:41 | fiscal_country_codes = fields.Char(compute="_compute_fiscal_country_codes") | FACT | always | — | Product, unit of measure, currency, partner and payment-term models carry a computed list of the fiscal country codes of the allowed companies, for view conditions. | N-U27-027 |
| VDR-U27-C086 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:25 | o.partner_id.country_code == 'MA' | FACT | always | — | The core invoice report template has three branches on a literal country code (partner country) in the shared layout. | N-U27-029 |
| VDR-U27-C087 | FUNCTION MAPPING REQUIRED | account/views/res_config_settings_views.xml:87 | company_country_code in ('CH', 'UK') | FACT | always | — | A core settings block is shown depending on EU group membership or literal country codes. | N-U27-029 |
| VDR-U27-C088 | FUNCTION MAPPING REQUIRED | account_check_printing/views/res_config_settings_views.xml:26 | country_code != 'CA' | FACT | check printing module installed | — | Two settings rows in the check-printing module are visible only for a literal country code. | N-U27-029 |
| VDR-U27-C089 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:85 | if country_code == 'BE': | FACT | always | — | The default early-payment discount computation of a payment term is chosen by comparing the company country with two literal codes and otherwise 'included'. | N-U27-029 |
| VDR-U27-C090 | FUNCTION MAPPING REQUIRED | account/models/company.py:52 | STORNO_MANDATORY_COUNTRIES = { | FACT | always | — | Two literal country sets (11 mandatory, 4 optional) decide the default and visibility of the storno accounting option. | N-U27-030 |
| VDR-U27-C091 | FUNCTION MAPPING REQUIRED | account/models/company.py:453 | company.account_storno = company.account_fiscal_country_id.code in STORNO_MANDATORY_COUNTRIES | FACT | always | — | The storno default is computed from the company's fiscal country code against the literal set. | N-U27-029 |
| VDR-U27-C092 | FUNCTION MAPPING REQUIRED | account/models/company.py:34 | PEPPOL_DEFAULT_COUNTRIES = [ | FACT | always | — | Three literal lists (21, 5 and 34 codes) of countries for the e-invoice network live in the core company module, with a comment to keep them aligned with another module's manifest. | N-U27-030 |
| VDR-U27-C093 | FUNCTION MAPPING REQUIRED | account/tools/structured_reference.py:196 | check_per_country = { | FACT | always | — | A core tool maps six country codes to payment-reference validators and falls back to the international standard. | N-U27-030 |
| VDR-U27-C094 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:35 | SYSCOHADA_LIST = [ | FACT | always | — | The core loader holds a literal list of 17 country codes for a regional chart family and refuses direct selection of two regional templates by literal code. | N-U27-030 |
| VDR-U27-C095 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:168 | if template_code in {'syscohada', 'syscebnl'} | FACT | always | — | try_loading raises unless the company's chart already equals the regional template. | N-U27-030 |
| VDR-U27-C096 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:77 | if model.startswith(country_code): | FACT | journal creation | — | The default invoice-reference standard of a journal is chosen by matching the lower-cased company country code against the prefix of the selection values. | N-U27-029 |
| VDR-U27-C097 | FUNCTION MAPPING REQUIRED | account_peppol/models/res_company.py:201 | {'FR', 'GP', 'MQ', 'RE'} | FACT | e-invoice network module installed | — | The e-invoice network module has a literal country set for one national case. | N-U27-029 |
| VDR-U27-C098 | FUNCTION MAPPING REQUIRED | account_qr_code_sepa/models/res_bank.py:55 | non_iban_codes = { | FACT | SEPA QR module installed | — | The SEPA QR module holds a literal set of territory codes that are not IBAN prefixes. | N-U27-030 |
| VDR-U27-C099 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:25 | _ref_vat = { | FACT | base_vat installed | — | The validation module holds a table of sample tax numbers for 62 countries and 32 per-country check methods; it is itself the country-aware component. | N-U27-030 |
| VDR-U27-C100 | FUNCTION MAPPING REQUIRED | base_iban/models/res_partner_bank.py:146 | _map_iban_template = { | FACT | base_iban installed | — | The IBAN module holds a table of 70 country templates (an international standard). | N-U27-030 |
| VDR-U27-C101 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1365 | country_code == 'BE' | FACT | e-document module installed | — | The shared e-document module compares country codes literally 40 times in 12 files (a mechanical AST scan), e.g. in the shared UBL builder. | N-U27-031 |
| VDR-U27-C102 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:32 | "France (FacturX)" | FACT | e-document module installed | — | The shared e-document module registers country-named formats (seven) in the partner's format selection. | N-U27-031 |
| VDR-U27-C103 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/__init__.py:14 | from . import account_edi_xml_ubl_a_nz | FACT | e-document module installed | — | The shared module contains builder modules for named regional formats (e.g. a_nz, sg, nlcius, xrechnung, efff, facturx) inside the generic package. | N-U27-031 |
| VDR-U27-C104 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:58 | EAS_MAPPING = { | FACT | e-document module installed | — | A table keyed by country maps electronic-address schemes (62 country keys). | N-U27-031 |
| VDR-U27-C105 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:23 | TEMPLATE_MODELS = ( | FACT | always | — | A template can carry data for seven models: account groups, accounts, fiscal positions, tax groups, taxes, journals and reconcile models; this tuple also fixes the loading order. | N-U27-037 |
| VDR-U27-C106 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:53 | def template(template=None, model= | FACT | always | — | Template providers are plain functions marked with a decorator giving (template code, target model); the model defaults to template_data (the template-level values). | N-U27-036 |
| VDR-U27-C107 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:68 | wrapper._l10n_template = (template, model) | FACT | always | — | The decorator stores the (code, model) tuple on the function, and the module of origin is stored for code translations. | N-U27-036 |
| VDR-U27-C108 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:78 | def _template_register | FACT | always | — | The registry is built by reflecting over the loader class members that carry the marker; providers are grouped by template then model. | N-U27-036 |
| VDR-U27-C109 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:51 | getmembers(python_module, template_module) | FACT | always | — | The module-level 'account_templates' value is computed by importing each localization-category module's models package and scanning template_* submodules for decorated template-level functions. | N-U27-036 |
| VDR-U27-C110 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:48 | 'installed': module.state == "installed", | FACT | always | — | Each registry entry records name, parent, sequence, country, visibility, installed flag and owning module. | N-U27-036 |
| VDR-U27-C111 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:98 | def _get_chart_template_mapping | FACT | always | — | The mapping covers all modules not marked uninstallable (installed or not) and is cached by the ORM; hidden templates are filtered unless requested. | N-U27-036 |
| VDR-U27-C112 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:140 | def try_loading | FACT | always | — | try_loading(template_code, company, install_demo, force_create) is the public entry; with no code it guesses from the company country. | N-U27-045 |
| VDR-U27-C113 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:152 | prevents new creations and performs updates | FACT | always | — | force_create False prevents creation of new records and only updates existing ones. | N-U27-052 |
| VDR-U27-C114 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:183 | if not self.env.is_system(): | FACT | always | — | Only a system administrator may load a chart template. | N-U27-048 |
| VDR-U27-C115 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:193 | module.button_immediate_install() | FACT | template belongs to an uninstalled module | — | If the template's owning module is not installed, loading installs it first and then continues in the new registry. | N-U27-049 |
| VDR-U27-C116 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:206 | chart_template_load=True | FACT | always | — | Loading runs with the target company as the only allowed company, tracking disabled, the language forced to English and a marker context key. | N-U27-050 |
| VDR-U27-C117 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:210 | reload_template = template_code == company.chart_template | FACT | always | — | A reload is detected by equality of the requested code and the company's current chart template. | N-U27-051 |
| VDR-U27-C118 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:213 | if not reload_template and (not company.root_id._existing_accounting() | FACT | different template requested | — | When another template is chosen and the company tree has no entries (or demo is installed), existing moves and all records of the seven template models of the company are deleted first. | N-U27-060 |
| VDR-U27-C119 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:215 | for model in ('account.move',) + TEMPLATE_MODELS[::-1]: | FACT | different template requested and no entries | — | The deletion runs over moves and the template models in reverse order and detaches multi-company records from the tree instead of deleting them when they also belong to another company. | N-U27-060 |
| VDR-U27-C120 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:230 | 'res.company': data['res.company'], | FACT | company has a parent | — | For a branch the template data is reduced to the company-level values; accounts, taxes and so on are not recreated. | N-U27-050 |
| VDR-U27-C121 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:236 | self._pre_load_data(template_code, company, template_data, data) | FACT | always | — | Order: (reload only) pre-reload filtering, pre-load (company values), load data, post-load defaults, translations, account-group parent sync, demo, then subsidiaries. | N-U27-045 |
| VDR-U27-C122 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:245 | Install the demo data when the | FACT | install_demo True and not a reload | — | Demo data is loaded after the first template of a company and errors in demo loading are logged and swallowed inside a savepoint. | N-U27-058 |
| VDR-U27-C123 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:254 | for subsidiary in company.child_ids: | FACT | always | — | After loading a company, the same template is loaded recursively for each of its branches. | N-U27-050 |
| VDR-U27-C124 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:826 | for code in [None] + self._get_parent_template(template_code): | FACT | always | — | Template data is the merge of root-level providers (code None) and providers of the template and its parent chain; later values update earlier ones. | N-U27-047 |
| VDR-U27-C125 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:829 | key=lambda i: TEMPLATE_MODELS.index(i[0]) | FACT | always | — | Within a template the models are iterated in TEMPLATE_MODELS order, others last. | N-U27-046 |
| VDR-U27-C126 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1238 | def _get_parent_template | FACT | always | — | The parent chain is read from the 'parent' entry of the registry. | N-U27-047 |
| VDR-U27-C127 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1330 | data/template/{model} | FACT | always | — | Default providers read CSV files named data/template/<model>-<template>.csv inside the template's owning module. | N-U27-037 |
| VDR-U27-C128 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1328 | self._get_parent_template(template_code)[::-1] | FACT | always | — | CSV files are read parent first so that child rows override parent rows by id. | N-U27-047 |
| VDR-U27-C129 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1355 | except FileNotFoundError: | FACT | always | — | A missing CSV file is tolerated (debug log only), so a template may omit any model. | N-U27-037 |
| VDR-U27-C130 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1145 | @template(model='account.fiscal.position') | FACT | always | — | Root providers (code None) load accounts, groups, tax groups, taxes (with tag dereferencing) and fiscal positions from CSV for any template. | N-U27-037 |
| VDR-U27-C131 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1175 | "exch": { | FACT | always | — | Root journal provider hard-codes six journals (sales, purchases, miscellaneous, exchange difference, cash-basis taxes, bank); templates may add or change journals through their own provider. | N-U27-037 |
| VDR-U27-C132 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:497 | filter_properties = lambda key: | FACT | always | — | Template-level values are written to the company when the key is a company field (excluding property_ fields other than stock properties and the name). | N-U27-037 |
| VDR-U27-C133 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:521 | code_digits = int(template_data.get('code_digits', 6)) | FACT | always | — | Account codes are zero-padded to the template's code_digits (default 6) before loading. | N-U27-037 |
| VDR-U27-C134 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:530 | Exclude data of unknown fields present | FACT | unless l10n_check_fields_complete context | — | Keys in template data that are not fields of the target model are silently removed. | N-U27-054 |
| VDR-U27-C135 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:562 | def _load_data | FACT | always | — | Records are described as {model: {external id: values}}; references to other records are written as external ids and replaced by database ids at load time, so definitions can precede existence. | N-U27-046 |
| VDR-U27-C136 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:621 | def delay(all_data): | FACT | always | — | A delay step postpones relational fields whose target model is created later, so forward references resolve. | N-U27-046 |
| VDR-U27-C137 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:695 | 'noupdate': True, | FACT | always | — | Every loaded record is registered with an external id marked noupdate. | N-U27-053 |
| VDR-U27-C138 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1230 | return f"account.{company.id}_{xmlid}" | FACT | always | — | Template records get external ids in the core's namespace prefixed with the company id, regardless of which pack provides them. | N-U27-053 |
| VDR-U27-C139 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1235 | self.env.company.parent_ids[0] | FACT | always | — | Reference resolution falls back to the root company's records, which lets branches reuse the root's records. | N-U27-050 |
| VDR-U27-C140 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:700 | def _post_load_data | FACT | always | — | Post-load creates utility accounts, assigns suspense and cash-difference accounts to cash/bank journals, defaults the exchange and cash-basis journals, default sale/purchase accounts on journals and default taxes on the company. | N-U27-045 |
| VDR-U27-C141 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:751 | sudoed_products_sale._force_default_sale_tax(company) | FACT | always | — | Default taxes are applied on existing products only where the product already has a tax in another company. | N-U27-045 |
| VDR-U27-C142 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:769 | self.env['ir.default'].set(model, field, self.ref(value).id, company_id=company.id) | FACT | always | — | Property defaults (partner receivable/payable, product category stock journal and any additional properties) are stored per company as defaults. | N-U27-045 |
| VDR-U27-C143 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:239 | self._load_translations(companies=company) | FACT | always | — | Translations of translatable template fields are loaded after data (see language layer unit). | N-U27-045 |
| VDR-U27-C144 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:265 | def _pre_reload_data | FACT | reload | — | On reload the loader limits what it updates: it drops property defaults and reconcile models, skips journals and account groups that exist, and clears company values (except anglo-saxon). | N-U27-051 |
| VDR-U27-C145 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:273 | if prop.startswith('property_'): | FACT | reload | — | Property defaults are dropped from the template data on reload. | N-U27-051 |
| VDR-U27-C146 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:333 | def tax_template_changed | FACT | reload | — | A tax is considered changed on reload when its computation kind, amount or number of distribution lines differ. | N-U27-051 |
| VDR-U27-C147 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:397 | tax_to_rename.name = f"[old | FACT | reload and force_create | — | A changed tax is not modified in place: the existing tax is renamed with an [old] prefix and the new one is created. | N-U27-051 |
| VDR-U27-C148 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:378 | if not force_create: | FACT | reload | — | When creation is not forced, changed or missing taxes are skipped instead of created. | N-U27-052 |
| VDR-U27-C149 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:427 | repartition_line_values['tag_ids'] = tags or [Command.clear()] | FACT | reload | — | For an unchanged tax the reload only relinks fiscal positions, adds new mappings and refreshes report tags on distribution lines. | N-U27-051 |
| VDR-U27-C150 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:446 | # Prevents overriding user setting & | FACT | reload | — | For an existing account only tags are updated from the template; the reconcile flag is never overwritten. | N-U27-051 |
| VDR-U27-C151 | FUNCTION MAPPING REQUIRED | account/models/company.py:992 | def _existing_accounting | FACT | always | — | 'Entries exist' is true when any journal item exists in the company tree of the (root) company. | N-U27-060 |
| VDR-U27-C152 | FUNCTION MAPPING REQUIRED | account/models/company.py:328 | Cannot change Price Tax computation method | FACT | company has entries | — | The price-includes-tax setting cannot change once the company tree has entries. | N-U27-060 |
| VDR-U27-C153 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:505 | if not company.root_id._existing_accounting(): | FACT | always | — | Currency assignment during template loading is skipped when entries exist. | N-U27-060 |
| VDR-U27-C154 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1246 | def _get_tag_mapper | FACT | always | — | Tax report tags in template data are given by name (with the tag delimiter) and resolved against existing tags of the template country; an external id is used as is. | N-U27-055 |
| VDR-U27-C155 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1265 | raise RedirectWarning( | FACT | unless ignore_missing_tags | — | A tag missing for the template country aborts loading with a warning telling the user to update the pack first. | N-U27-059 |
| VDR-U27-C156 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:903 | 'applicability': 'taxes', | FACT | always | — | Tax tags are created from report expressions of the tax-tags engine, scoped to the report's country. | N-U27-055 |
| VDR-U27-C157 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:7 | ref="base.th" | FACT | th installed | — | The Thailand pack declares its tax report with country Thailand and availability 'country'. | N-U27-056 |
| VDR-U27-C158 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:9 | <field name="availability_condition">country</field> | OBSERVATION | restored database | — | Restored database: 6 reports exist; 3 come from the core (generic tax report and its two groupings) and 3 from the Thailand pack (tax report, PND53, PND3), each with country Thailand and availability 'country'. | N-U27-056 |
| VDR-U27-C159 | FUNCTION MAPPING REQUIRED | l10n_th/models/account_move.py:9 | if self.company_id.account_fiscal_country_id.code == 'TH': | FACT | th installed | — | The Thailand pack overrides the invoice-report hook and returns its report only when the document's company has fiscal country Thailand. | N-U27-039 |
| VDR-U27-C160 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:15 | <t name="invoice_title">Tax Invoice</t> | FACT | th installed | — | The Thailand pack inherits the core invoice layout, adds the partner branch label after the tax number and replaces the title block with an English literal 'Tax Invoice' (translatable template text). | N-U27-039 |
| VDR-U27-C161 | FUNCTION MAPPING REQUIRED | l10n_din5008/__manifest__.py:11 | 'countries': ['de', 'ch'] | OBSERVATION | mechanical scan | — | 8 packs extend the document layout settings model (a mechanical AST count); one document-layout pack is flagged for two countries and auto-installs, showing that layout packs are country-flagged but not charts. | N-U27-039 |
| VDR-U27-C162 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:31 | selection_add=[ | FACT | e-document module installed | — | Formats are registered by selection_add on the partner's format field; 15 packs add formats and 15 override the extra-document dictionary (mechanical AST count). | N-U27-040 |
| VDR-U27-C163 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:167 | def _get_ubl_cii_formats_info | FACT | e-document module installed | — | A format-info function returns per-format metadata and a builder-selection function maps the chosen format to a builder. | N-U27-040 |
| VDR-U27-C164 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:332 | def _get_edi_builder | FACT | e-document module installed | — | A separate function selects the builder object for the chosen format. | N-U27-040 |
| VDR-U27-C165 | FUNCTION MAPPING REQUIRED | account/models/account_move_send.py:704 | def _call_web_service_before_invoice_pdf_render | FACT | always | RT | The sending pipeline has before-render and after-render web-service hooks where packs call external services. | N-U27-040 |
| VDR-U27-C166 | FUNCTION MAPPING REQUIRED | account_edi/models/account_edi_format.py:8 | _name = 'account.edi.format' | FACT | account_edi installed | — | A legacy format registry model with unique code exists; 4 packs extend it. | N-U27-040 |
| VDR-U27-C167 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:29 | def _compute_country_proxy_keys | FACT | th installed | — | The Thailand pack plugs into the QR framework by overriding five hooks on the bank account (proxy keys, display of QR setting, merchant account info, eligibility error, data check), each keyed on the bank account's country. | N-U27-041 |
| VDR-U27-C168 | FUNCTION MAPPING REQUIRED | account/models/sequence_mixin.py:258 | def _get_starting_sequence | FACT | always | — | Starting sequence and last-sequence domain are overridable per document model; 6 packs override each of them (mechanical AST). | N-U27-043 |
| VDR-U27-C169 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:164 | ('euro', "European (RF83INV202400001)"), | FACT | always | — | The invoice-reference standard is a selection (full reference, European, numbers only) extended by 7 packs (mechanical grep of packs redefining this field). | N-U27-043 |
| VDR-U27-C170 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:706 | journal.refund_sequence = journal.type in ('sale', 'purchase') | FACT | always | — | Credit-note sequences are separate for sale and purchase journals. | N-U27-043 |
| VDR-U27-C171 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:825 | self._update_dependencies(terp.get('depends', []), terp.get('auto_install')) | FACT | always | — | The manifest auto_install value (true or a list of dependency names) is stored on the dependency rows as auto_install_required. | N-U27-044 |
| VDR-U27-C172 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:420 | states <= install_states and 'to install' | FACT | module installation | — | An auto-install module is selected when all of its required dependencies are installed or being installed and at least one of them is being installed now. | N-U27-044 |
| VDR-U27-C173 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:954 | def _instantiate_foreign_taxes | FACT | always | — | A framework facility instantiates the taxes of another country's template into an existing company, creating substitute accounts from the company's own chart, without fiscal positions or mappings. | N-U27-091 |
| VDR-U27-C174 | FUNCTION MAPPING REQUIRED | account/models/partner.py:300 | Only Accounting managers can create foreign | FACT | always | — | The user action to create foreign taxes from a foreign-registration position is limited to accounting managers and installs the other country's pack if needed. | N-U27-091 |
| VDR-U27-C175 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:20 | 'auto_install': ['account'] | FACT | always | — | The Thailand pack auto-installs when the core accounting module is installed and (through the countries flag) a company with country Thailand exists. | N-U27-064 |
| VDR-U27-C176 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:28 | 'post_init_hook': '_preserve_tag_on_taxes' | FACT | always | — | The Thailand pack has a post-init hook and no pre-init or uninstall hook. | N-U27-065 |
| VDR-U27-C177 | FUNCTION MAPPING REQUIRED | l10n_th/__init__.py:6 | preserve_existing_tags_on_taxes(env | FACT | th install | — | The hook calls the core helper that marks tag records of the pack as noupdate. | N-U27-065 |
| VDR-U27-C178 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:50 | update ir_model_data set noupdate = 't' | FACT | upgrade | — | The helper sets noupdate on the tag records of the module via SQL to keep existing tags during upgrades. | N-U27-065 |
| VDR-U27-C179 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:6 | 'version': '2.0' | FACT | always | — | The Thailand pack manifest version is 2.0; the restored database stores latest_version 19.0.2.0 for it. | N-U27-069 |
| VDR-U27-C180 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:21 | 'data': [ | OBSERVATION | restored database | — | The Thailand pack ships 2 data files (tax report data, invoice report view), 1 demo file and no security files; the restored database holds for the pack 0 access rows, 0 rules, 0 groups, 0 cron jobs, 0 automation rules, 3 reports, 1 print action and 3 views. | N-U27-072 |
| VDR-U27-C181 | FUNCTION MAPPING REQUIRED | l10n_th/demo/demo_company.xml:3 | partner_demo_company_th | FACT | demo data enabled | — | The pack ships a demo company with country Thailand (forcecreate); demo is not loaded in the restored database. | N-U27-070 |
| VDR-U27-C182 | FUNCTION MAPPING REQUIRED | l10n_th/__init__.py:2 | from . import models | OBSERVATION | source tree | — | The Thailand pack has no migrations directory (41 of 227 foreign packs have one). | N-U27-068 |
| VDR-U27-C183 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:112 | companies.chart_template = False | FACT | uninstall of a module hosting templates | — | Uninstalling a module that hosts chart templates clears chart_template on every company that used one of its templates; records created by the loader stay. | N-U27-067 |
| VDR-U27-C184 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:695 | 'noupdate': True, | INFERENCE | uninstall | RT | Inference from the loader (records get external ids in the core's namespace with noupdate) and the uninstall method (which only clears the company field): chart records are not owned by the pack and remain after uninstall; not executed (RT). | N-U27-067 |
| VDR-U27-C185 | FUNCTION MAPPING REQUIRED | l10n_ch/migrations/11.1/end-migrate_update_taxes.py:21 | try_loading('ch', company, force_create=False) | FACT | upgrade to a version with such a script | — | Template data updates on upgrade are delivered as version-keyed end-of-migration scripts that find companies with the pack's chart code and call try_loading with force_create=False (38 of the 83 pack migration scripts call try_loading, 31 with force_create=False). | N-U27-068 |
| VDR-U27-C186 | FUNCTION MAPPING REQUIRED | l10n_ch/migrations/11.1/end-migrate_update_taxes.py:7 | order="parent_path" | FACT | upgrade | — | The migration iterates companies ordered by parent_path, i.e. roots before branches. | N-U27-068 |
| VDR-U27-C187 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/__manifest__.py:4 | 'summary': 'Allow updating tax grids on | FACT | module installed | — | A separate core module provides a debug-mode wizard to re-tag existing entries after report changes; it is not installed in the restored database. | N-U27-068 |
| VDR-U27-C188 | FUNCTION MAPPING REQUIRED | l10n_de/__init__.py:8 | env['res.groups']._activate_group_account_secured() | FACT | install | — | A pack post-init hook applies the core 'secured entries' feature group to the read-only and invoicing groups, which are database-wide groups, i.e. a database-wide effect from a single-country pack. | N-U27-075 |
| VDR-U27-C189 | FUNCTION MAPPING REQUIRED | l10n_in/__init__.py:11 | group_user._apply_group(env.ref('account.group_cash_rounding')) | FACT | install | — | Another pack post-init hook enables cash rounding for all users (comment: for all companies). | N-U27-075 |
| VDR-U27-C190 | FUNCTION MAPPING REQUIRED | l10n_latam_base/__init__.py:8 | UPDATE res_partner | FACT | install | — | A regional base pack's post-init hook sets an identification type on every partner by SQL. | N-U27-075 |
| VDR-U27-C191 | FUNCTION MAPPING REQUIRED | l10n_gcc_invoice/__init__.py:5 | _activate_and_install_lang('ar_001') | FACT | install | — | A regional invoice pack's post-init hook activates and installs a language database-wide. | N-U27-075 |
| VDR-U27-C192 | FUNCTION MAPPING REQUIRED | l10n_fr_account/__init__.py:22 | fr_companies = env['res.company'].search([('partner_id.country_id.code', 'in', env['res.company']._get_france_country_codes())]) | FACT | install | — | A pack post-init hook restricts its sequence set-up to companies whose country belongs to the pack's country set - the pattern of scoping install effects by company country. | N-U27-066 |
| VDR-U27-C193 | FUNCTION MAPPING REQUIRED | l10n_it_edi/__init__.py:16 | for company in env['res.company'].search([('chart_template', '=', 'it'), | FACT | install | — | A document-pack post-init hook adds its own tax fields onto already loaded taxes of root companies whose chart template equals the base pack's code, via _load_data. | N-U27-066 |
| VDR-U27-C194 | FUNCTION MAPPING REQUIRED | l10n_sa_edi/__init__.py:6 | for company in env['res.company'].search([('chart_template', '=', 'sa'), | FACT | install | — | A second document pack uses the same pattern: update only existing taxes of companies with the base chart. | N-U27-066 |
| VDR-U27-C195 | FUNCTION MAPPING REQUIRED | l10n_dk_nemhandel/__init__.py:8 | def _pre_init_nemhandel(env): | FACT | install | — | A document pack uses a pre-init hook to create columns directly and backfill them by SQL to avoid ORM computation on large tables (performance pattern). | N-U27-065 |
| VDR-U27-C196 | FUNCTION MAPPING REQUIRED | account/models/partner.py:1179 | def _clear_removed_edi_formats | FACT | uninstall of a format pack | — | A core helper clears stored per-company format selections of removed formats; 13 document packs call it from an uninstall hook. | N-U27-067 |
| VDR-U27-C197 | FUNCTION MAPPING REQUIRED | l10n_eu_oss/__init__.py:7 | DELETE FROM ir_model_data WHERE module = | FACT | uninstall | — | One regional tax pack deletes its external-id rows for tax groups and accounts on uninstall, which detaches them from the module so they survive (inference from the SQL). | N-U27-067 |
| VDR-U27-C198 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:86 | def _load_module_terms | FACT | terms load | — | When module terms are loaded for the core module, chart-template and tax-tag translations are (re)loaded for the given languages. | N-U27-071 |
| VDR-U27-C199 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:69 | not self.env.company.chart_template | FACT | module install | — | When a module that hosts templates is installed, the first of its templates that matches the current company's country (or the generic one) is loaded on the current company only if that company has no chart yet; loading is deferred to the registry's register hook. | N-U27-064 |
| VDR-U27-C200 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:83 | self.env.registry._auto_install_template = try_loading | FACT | module install | — | The loading callback is stored on the registry and executed in _register_hook after the registry is ready. | N-U27-064 |
| VDR-U27-C201 | FUNCTION MAPPING REQUIRED | l10n_de/__manifest__.py:26 | 'auto_install': ['account'] | INFERENCE | mechanical re-count | — | Recounted from all 227 foreign manifests: 186 are auto-install (129 list form, 57 true form), 41 are not; 155 declare countries; 30 have a post-init hook, 14 an uninstall hook, 2 a pre-init hook; 175 declare a version; all 227 are LGPL-3. These agree with the profile columns (depends, auto_install, hooks, data counts: 0 disagreements). | N-U27-073 |
| VDR-U27-C202 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:1 | "id","name" | INFERENCE | mechanical re-count | CONTRA | Contradiction with the profile: its template_data_files column is non-zero for 10 packs, but 125 packs have a data/template directory and 115 packs define a template-level provider; the column does not measure template data files (its definition is not documented). | N-U27-083 |
| VDR-U27-C203 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:1 | "id" | OBSERVATION | source tree | — | Thailand template CSVs: 144 accounts, 18 taxes, 5 tax groups, plus one assets file; no fiscal-position, journal or group CSV (content studied in U13 and U24). | N-U27-070 |
| VDR-U27-C204 | FUNCTION MAPPING REQUIRED | l10n_de/__manifest__.py:36 | 'post_init_hook': '_post_init_hook' | FACT | sample | — | Sample base pack (Germany): depends on the validation, IBAN, layout and shared e-document modules, auto-installs with accounting, has a post-init hook, 4 data files and 1 demo file. | N-U27-074 |
| VDR-U27-C205 | FUNCTION MAPPING REQUIRED | l10n_in/__manifest__.py:69 | 'post_init_hook': 'post_init' | FACT | sample | — | Sample base pack (India): 34 data files, 2 demo files, depends on a Python-formula tax module, debit note and an IAP bridge; overrides the loader's _load and _post_load_data. | N-U27-074 |
| VDR-U27-C206 | FUNCTION MAPPING REQUIRED | l10n_ar/__manifest__.py:73 | 'l10n_latam_invoice_document' | FACT | sample | — | Sample base pack (Argentina): depends on two regional framework packs (document types and base) and has no hooks; overrides try_loading and _load. | N-U27-074 |
| VDR-U27-C207 | FUNCTION MAPPING REQUIRED | l10n_fr_account/__manifest__.py:38 | 'auto_install': ['account'], | FACT | sample | — | Sample family host (France): hosts 7 templates (fr plus six other-territory templates declared with parent fr); six stub packs depend on it and have no models. | N-U27-080 |
| VDR-U27-C208 | FUNCTION MAPPING REQUIRED | l10n_gf/__manifest__.py:11 | 'l10n_fr_account', | FACT | sample | — | A territory stub pack has no models or data and only depends on the family host plus account; its template is declared in the host. | N-U27-080 |
| VDR-U27-C209 | FUNCTION MAPPING REQUIRED | l10n_fr_account/models/template_gf.py:12 | 'parent': 'fr', | FACT | sample | — | The territory's template declares parent fr and also overrides the tag-dereference function to read tags of its parent's country. | N-U27-080 |
| VDR-U27-C210 | FUNCTION MAPPING REQUIRED | l10n_bf/models/template_bf.py:12 | 'parent': 'syscohada', | FACT | sample | — | A regional (OHADA-family) country pack declares parent syscohada and reuses the family's company-values function through super(). | N-U27-080 |
| VDR-U27-C211 | FUNCTION MAPPING REQUIRED | l10n_bf/models/template_bf.py:18 | super()._get_syscohada_res_company() | FACT | sample | — | Template providers of one pack are reached from another pack through Python method inheritance on the shared loader class. | N-U27-080 |
| VDR-U27-C212 | FUNCTION MAPPING REQUIRED | l10n_eu_oss/__manifest__.py:28 | uninstall_hook | FACT | sample | — | Sample regional tax pack (EU OSS): no countries flag, no auto-install, depends on accounting only, has an uninstall hook. | N-U27-074 |
| VDR-U27-C213 | FUNCTION MAPPING REQUIRED | l10n_it_edi/__manifest__.py:9 | 'auto_install': ['l10n_it'] | FACT | sample | — | Sample document pack (Italy e-invoicing): category EDI, depends on the base pack, proxy-client and debit-note modules, auto-installs when the base pack is installed, has post-init and uninstall hooks. | N-U27-074 |
| VDR-U27-C214 | FUNCTION MAPPING REQUIRED | l10n_dk_nemhandel/__manifest__.py:39 | 'pre_init_hook': '_pre_init_nemhandel' | FACT | sample | — | Sample document pack (Denmark): auto-installs when both the shared e-document module and the base pack are installed; has pre-init, post-init and uninstall hooks. | N-U27-074 |
| VDR-U27-C215 | FUNCTION MAPPING REQUIRED | l10n_pe_pos/__manifest__.py:13 | point_of_sale | FACT | sample | — | Sample POS bridge (Peru): depends on its base pack and point-of-sale; auto-install true; no hooks. | N-U27-074 |
| VDR-U27-C216 | FUNCTION MAPPING REQUIRED | l10n_latam_base/__manifest__.py:66 | 'post_init_hook': '_set_default_identification_type' | FACT | sample | — | Regional framework pack (LATAM base): no country, no auto-install, depends on contacts and the validation module; 7 packs depend on it and 6 on its invoice-document sibling. | N-U27-080 |
| VDR-U27-C217 | FUNCTION MAPPING REQUIRED | l10n_latam_invoice_document/models/res_company.py:9 | This method is to be inherited | FACT | sample | — | The regional document framework publishes a documented hook contract: a company method that localizations override to return True when they use government document types. | N-U27-084 |
| VDR-U27-C218 | FUNCTION MAPPING REQUIRED | l10n_din5008/__manifest__.py:10 | 'auto_install': True, | FACT | sample | — | Layout pack (DIN 5008): countries de and ch, auto-install true, depends on accounting only; 8 packs depend on it. | N-U27-080 |
| VDR-U27-C219 | FUNCTION MAPPING REQUIRED | l10n_fr_hr_holidays/__manifest__.py:7 | 'category': 'Human Resources/Time Off' | FACT | sample | — | The only HR-related packs are 3 time-off packs (plus one expense-layout pack), not payroll; the heuristic's 'payroll/hr' count of 5 includes l10n_hr and l10n_hr_kuna, which are accounting chart packs whose names merely start with hr. | N-U27-083 |
| VDR-U27-C220 | FUNCTION MAPPING REQUIRED | l10n_hr/__manifest__.py:16 | 'category': 'Accounting/Localizations/Account Charts' | FACT | sample | CONTRA | l10n_hr is an accounting chart pack (not HR); the profile's archetype heuristic misclassifies it by name prefix. | N-U27-083 |
| VDR-U27-C221 | FUNCTION MAPPING REQUIRED | l10n_syscohada/models/template_syscohada.py:8 | @template('syscohada') | FACT | sample | — | The family root hosts two templates (syscohada and syscebnl) and 17 packs declare children of them. | N-U27-080 |
| VDR-U27-C222 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5569 | def _post(self, soft=True): | INFERENCE | mechanical AST scan of 227 packs | — | _post is overridden by 15 foreign packs (same count for the invoice-report hook), among the most frequent core method overrides in the mechanical list (top of table T3b); a mechanical guard-lint finds 7 overrides with a country or chart condition in the body, 6 with another pack flag and 2 with none (heuristic regex, to verify). | N-U27-081 |
| VDR-U27-C223 | FUNCTION MAPPING REQUIRED | account/models/partner.py:715 | def _commercial_fields | INFERENCE | mechanical AST scan | — | res.partner._commercial_fields is overridden by 13 packs; the partner extensions overall (identity, bank, VAT) are used 65 times. | N-U27-081 |
| VDR-U27-C224 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:73 | class AccountChartTemplate(models.AbstractModel): | INFERENCE | mechanical AST scan | — | Of the 227 packs 210 extend at least one model; 86 distinct model names are extended; top: loader (128 packs), account move (87), company (69), partner (65), settings (37), tax (35), journal (30), send wizard (24), move line (18), product template (15), POS config (14), POS order (14); 14 models are extended by 10 or more packs and 26 by 5 or more; 176 packs extend at least one accounting model counting the loader, 104 excluding the loader. | N-U27-082 |
| VDR-U27-C225 | FUNCTION MAPPING REQUIRED | l10n_de/__manifest__.py:19 | 'depends': [ | INFERENCE | mechanical re-count | CONTRA | Profile column core_acc_models_extended (119 packs non-zero) could not be reproduced: 176 (including the loader) or 104 (excluding it) under my definitions; treat the profile figure as unverified. | N-U27-083 |
| VDR-U27-C226 | FUNCTION MAPPING REQUIRED | l10n_ar/models/account_chart_template.py:22 | def _load(self, template_code, company, install_demo | FACT | mechanical AST scan | — | Packs override loader internals: _post_load_data 7 packs, _load 5, _setup_utility_bank_accounts 4, _get_bank_fees_reco_account 3, _deref_account_tags 2 packs (7 overrides), _get_accounts_data_values 2, try_loading 1 - a coupling of packs to loader internals rather than to a declared contract. | N-U27-099 |
| VDR-U27-C227 | FUNCTION MAPPING REQUIRED | l10n_th/models/__init__.py:6 | from . import res_bank | FACT | always | — | The Thailand pack has 5 model files: template, partner, move, report action and bank account; it adds 1 computed partner field (branch label), 3 selection values on the bank account proxy type, 1 constraint, and overrides of the invoice-report hook, the print pre-render check and five bank-account QR hooks. | N-U27-085 |
| VDR-U27-C228 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_partner.py:13 | partner.country_code != 'TH' | FACT | th installed | — | The Thailand pack keys its partner branch label on the partner's own country. | N-U27-092 |
| VDR-U27-C229 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:20 | b.country_code == 'TH' | FACT | th installed | — | The Thailand pack keys bank-account checks on the bank account's country. | N-U27-092 |
| VDR-U27-C230 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:36 | country_code', '=', 'TH' | FACT | th installed | — | The Thailand commercial-invoice print action has a domain on the document's fiscal country code and sale journals. | N-U27-092 |
| VDR-U27-C231 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:149 | [('company_id', 'parent_of', company_ids)] | FACT | always | RT | Journals, taxes, tax groups, account groups and fiscal positions are visible only when their company is an ancestor of one of the user's selected companies (global record rules); accounts through company_ids. | N-U27-087 |
| VDR-U27-C232 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:155 | [('company_ids', 'parent_of', company_ids)] | FACT | always | RT | Accounts are visible when any of their companies is an ancestor of a selected company. | N-U27-087 |
| VDR-U27-C233 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:173 | [('company_id', 'parent_of', company_ids)] | FACT | always | RT | The tax rule uses the same ancestor test; sibling root companies do not see each other's taxes. | N-U27-087 |
| VDR-U27-C234 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:191 | [('company_id', 'parent_of', company_ids)] | FACT | always | RT | Fiscal positions follow the same ancestor test. | N-U27-087 |
| VDR-U27-C235 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:20 | check_company_domain_parent_of | FACT | always | RT | The company-consistency domain for tax, journal and fiscal-position links accepts records of the company or any ancestor (or no company). | N-U27-087 |
| VDR-U27-C236 | MCT-F03 | account/models/account_account.py:97 | company_ids = fields.Many2many('res.company', string='Companies', required=True | FACT | always | — | An account can belong to several companies at once (many-to-many, required), which is how a chart is shared. | N-U27-088 |
| VDR-U27-C237 | MCT-F03 | account/models/account_account.py:340 | record.code = record_root.code_store | FACT | always | RT | The account code is stored per root company, so branches share codes and different roots may code the same account differently. | N-U27-088 |
| VDR-U27-C238 | MCT-F03 | account/models/account_account.py:280 | len(a.sudo().company_ids) > 1 | FACT | always | RT | A cash account cannot belong to more than one company. | N-U27-088 |
| VDR-U27-C239 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:239 | ('company_id', 'child_of', tax.company_id.root_id.id) | FACT | always | RT | Tax names must be unique per type, scope and country within a root company tree. | N-U27-087 |
| VDR-U27-C240 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:232 | @api.constrains('company_id', 'name', 'type_tax_use', 'tax_scope', 'country_id') | FACT | always | — | The uniqueness constraint covers company, name, usage, scope and country, so two jurisdictions inside one root tree can reuse a tax name only with different countries. | N-U27-087 |
| VDR-U27-C241 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:172 | company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True | FACT | always | — | A journal belongs to exactly one company and numbering belongs to the journal; hence sequences are per company by construction. | N-U27-087 |
| VDR-U27-C242 | FUNCTION MAPPING REQUIRED | account/models/company.py:617 | for company in self.sudo().parent_ids: | FACT | always | RT | The effective soft lock date of a company is the maximum over itself and all its ancestors, with user exceptions evaluated per ancestor; a parent's lock date therefore binds its branches. | N-U27-089 |
| VDR-U27-C243 | FUNCTION MAPPING REQUIRED | account/models/company.py:447 | for c in company.with_context(active_test=False).sudo().parent_ids | FACT | always | RT | The hard lock date is likewise the maximum over the ancestors. | N-U27-089 |
| VDR-U27-C244 | FUNCTION MAPPING REQUIRED | account/models/res_config_settings.py:221 | if self.env.company == self.company_id and self.chart_template | FACT | settings save | RT | Choosing a chart in settings loads it only for the currently active company. | N-U27-087 |
| VDR-U27-C245 | FUNCTION MAPPING REQUIRED | account_payment_interco/__manifest__.py:4 | 'summary': "Enable Intercompany payments to reconcile | FACT | module installed | — | Community has an inter-company payment bridge (installed in the restored database): payments in one company reconcile invoices of another through clearing journals set per company. | N-U27-090 |
| VDR-U27-C246 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/account_move.py:30 | def _post(self, soft=True): | FACT | module installed | RT | The bridge extends posting to create clearing entries per company. | N-U27-090 |
| VDR-U27-C247 | FUNCTION MAPPING REQUIRED | account/models/partner.py:306 | localization_module.sudo().button_immediate_install() | FACT | always | RT | Creating foreign taxes installs the other country's pack database-wide (privilege elevated to sudo). | N-U27-091 |
| VDR-U27-C248 | FUNCTION MAPPING REQUIRED | l10n_in/__init__.py:9 | for all companies | FACT | install | — | The comment of a pack hook states the intent to activate cash rounding by default for all companies as soon as the module is installed: pack hooks act database-wide, not only on companies of the pack's country. | N-U27-094 |
| VDR-U27-C249 | FUNCTION MAPPING REQUIRED | n/a (no source line) | n/a | UNKNOWN | n/a | — | Whether Community offers cross-root consolidation of reports for a group of companies with different charts is not established by this study (reports can be selected per company; no consolidation model seen); MCT-F04 cross-check pending. | N-U27-097 |
| VDR-U27-C250 | FUNCTION MAPPING REQUIRED | l10n_latam_invoice_document/__manifest__.py:23 | extend company | FACT | sample | — | The regional document framework describes in its own manifest what a localization must do (depend on it, extend one company method, provide document type data with a country field). | N-U27-084 |
| VDR-U27-C251 | FUNCTION MAPPING REQUIRED | l10n_ar/models/account_fiscal_position.py:13 | def _get_fpos_validation_functions | FACT | sample | — | A pack extends the fiscal-position validator list by overriding the function and appending its own validators (clean extension point usage). | N-U27-103 |
| VDR-U27-C252 | FUNCTION MAPPING REQUIRED | account/models/company.py:34 | PEPPOL_DEFAULT_COUNTRIES = [ | FACT | always | — | A comment next to the literal lists says 'KEEP ALIGNED WITH ACCOUNT_PEPPOL MANIFEST -> COUNTRIES', i.e. country knowledge duplicated between a core file and another module's manifest. | N-U27-100 |
| VDR-U27-C253 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:127 | t[1]['name'] != 'generic_coa' if not country | INFERENCE | always | RT | The sort key for a missing country compares the template display name with the string generic_coa, and for a country with no pack nothing in the key prefers the generic template; which template a country without a pack receives therefore depends on registry order (reading only, not executed). | N-U27-101 |
| VDR-U27-C254 | FUNCTION MAPPING REQUIRED | account/models/partner.py:849 | def _check_vat(self, validation="error"): | FACT | always | — | _check_vat calls the _run_vat_checks hook with the commercial partner's country and the number, and rewrites the stored number when the hook returns a different (normalised) value. | N-U27-038 |
| VDR-U27-C255 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:166 | def _inverse_vat | FACT | base_vat installed | — | The validation component runs the check on every write of the number or the country. | N-U27-038 |
| VDR-U27-C256 | FUNCTION MAPPING REQUIRED | account/models/account_payment_method.py:76 | The id of the country needed | FACT | always | — | A payment method declares eligibility conditions - mode, journal types, currencies and the country needed on the company - through an information hook that modules extend. | N-U27-042 |
| VDR-U27-C257 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:409 | company_countries = self.env['res.company'].search([]).country_id | FACT | module installation | — | The country test for installing a country-flagged module looks at the union of the countries of all companies in the database; installation itself is database-wide. | N-U27-017 |
| VDR-U27-C258 | FUNCTION MAPPING REQUIRED | account/models/company.py:387 | def compute_account_tax_fiscal_country | INFERENCE | always | — | Country (address), fiscal country and currency are three independently stored values with only one-time defaulting between them (lines 387-390 here, base company currency onchange, and loader currency assignment), so inconsistent combinations are possible; the only validation found is document-level (taxes against tax country). | N-U27-020 |
| VDR-U27-C259 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:433 | must be the same as it's | INFERENCE | always | — | Because the currency is a delegated root field enforced by constraint, a company that needs a currency different from its parent's cannot be created as a branch of that parent. | N-U27-021 |
| VDR-U27-C260 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1424 | country_code == 'HU' | INFERENCE | mechanical AST scan of 31 core-family modules | — | Mechanical AST scan of the 31 core accounting-family modules (account, e-document, e-invoice network, QR, validators, sale, purchase, stock accounting, POS, product, units): 47 literal country-code comparisons (account_edi_ubl_cii 40, base_vat 4, account 2, account_peppol 1; one further hit, account_peppol_response, is a response-code false positive and is excluded), 11 literal country lists and 4 country tables; occurrences of the fiscal-country-code pattern in Python: 38 in 9 core modules versus 112 in 48 packs; occurrences of country-code conditions in views: 30 in 9 core modules versus 452 in 98 packs. | N-U27-032 |
| VDR-U27-C261 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:210 | reload_template = template_code == company.chart_template | INFERENCE | always | — | State list derived from lines 210-224 of the loader and module_uninstall in ir_module.py:106-115: no chart -> chart loaded (try_loading); chart loaded -> reload (same code); chart loaded -> other template (wipe only if no entries); package uninstalled -> company chart cleared, records kept. | N-U27-057 |
| VDR-U27-C262 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:397 | tax_to_rename.name = f"[old | INFERENCE | reload after posting | RT | Because changed taxes are renamed and recreated rather than updated, a reload on a company with posted documents leaves the old taxes in use and the new ones beside them (not executed). | N-U27-061 |
| VDR-U27-C263 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:530 | Exclude data of unknown fields present | INFERENCE | always | — | Unknown keys are deleted without a warning in the normal path (the checking context key enables strict mode), so misnamed fields in a pack are not reported. | N-U27-062 |
| VDR-U27-C264 | FUNCTION MAPPING REQUIRED | n/a (no source line) | n/a | UNKNOWN | n/a | RT | Reload, template switch with demo data and the external-service hooks were not executed; RT required. | N-U27-063 |
| VDR-U27-C265 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:112 | companies.chart_template = False | INFERENCE | uninstall then reinstall | RT | After uninstall the company chart selection is False while the loader's records remain, so a reinstall sees a company without chart; effect not executed. | N-U27-076 |
| VDR-U27-C266 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:20 | 'auto_install': ['account'] | INFERENCE | mechanical recount | — | Across the 227 other packs countries, auto_install, hooks, demo and migrations are individually optional and appear in many combinations (recount in the profile claim). | N-U27-077 |
| VDR-U27-C267 | FUNCTION MAPPING REQUIRED | n/a (no source line) | n/a | UNKNOWN | n/a | RT | Reinstall after uninstall, upgrade with posted entries and the effect of the Thai post-init tag step on existing tags were not executed; RT required. | N-U27-078 |
| VDR-U27-C268 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:7 | 'category': 'Accounting/Localizations/Account Charts' | INFERENCE | mechanical recount | — | Recount by dependencies and category: chart 125, electronic-document 34, POS bridge 24, stock/sale/purchase/website bridge 24, time-off or expense layout 4, other 16 (heuristic profile: 116, 34, 17, 16, 5, 39); disagreements on 43 packs, mostly document packs the profile put in 'other extension' and POS-flavoured document packs it put in 'edi'. | N-U27-079 |
| VDR-U27-C269 | FUNCTION MAPPING REQUIRED | n/a (no source line) | n/a | UNKNOWN | n/a | — | Package intent for borderline packs (layout, expense layout, regional framework) cannot be fixed from manifests alone. | N-U27-086 |
| VDR-U27-C270 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_partner.py:16 | code = partner.company_registry | INFERENCE | th installed | RT | The Thai branch label is derived from the partner's company registry value (Branch plus code, or Headquarter) and not from a company record; company-structure cases combine this with the delegated-field constraint (VDR-U27-C259, VDR-U27-C022) and the lock-date chain (VDR-U27-C242). | N-U27-093 |
| VDR-U27-C271 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5569 | def _post(self, soft=True): | INFERENCE | mechanical guard-lint | — | Mechanical regex lint of overrides in 227 packs: _post 15 (7 country or chart condition, 6 other pack flag, 2 none); invoice-report hook 15 (11 country or chart, 4 pack flag); sending alerts 13 (2, 8, 3); reset-to-draft 12 (3, 8, 1); extra-document dictionary 15 (1, 0, 14, which is expected because it only adds entries). Heuristic, to verify. | N-U27-095 |
| VDR-U27-C272 | FUNCTION MAPPING REQUIRED | account/models/company.py:617 | for company in self.sudo().parent_ids: | INFERENCE | always | RT | Because the lock chain and the delegated fields run through ancestors, a different-jurisdiction company created as a branch inherits the parent's locks, chart and currency. | N-U27-096 |
| VDR-U27-C273 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:87 | elif country_code == 'NL': | INFERENCE | always | — | Summary of the literal items under the core boundary capability (see claims in CAP-U27-02): comparisons, lists and a generic chart pinned to one country. | N-U27-098 |
| VDR-U27-C274 | FUNCTION MAPPING REQUIRED | l10n_latam_invoice_document/models/account_move.py:175 | def _post(self, soft=True): | FACT | sample | — | A regional framework overrides the same posting method that 15 packs override and the interco bridge also overrides; each guards itself with its own conditions. | N-U27-102 |
| VDR-U27-C275 | FUNCTION MAPPING REQUIRED | n/a (no source line) | n/a | UNKNOWN | n/a | RT | All observations in CAP-U27-07 derive from reading and static scans; none executed. | N-U27-104 |
| VDR-U27-C276 | FUNCTION MAPPING REQUIRED | account/models/company.py:53 | STORNO_OPTIONAL_COUNTRIES = { | INFERENCE | always | — | Classification of core country-conditional code into data exposure, literal comparison, literal list or table, and country-named format (see CAP-U27-02 claims for examples of each). | N-U27-025 |
| VDR-U27-C277 | FUNCTION MAPPING REQUIRED | account/models/template_generic_coa.py:36 | 'account_fiscal_country_id': 'base.us', | INFERENCE | always | — | Core contains literal comparisons, lists and a generic chart pinned to a country, so strict neutrality does not hold for the Community core. | N-U27-033 |
| VDR-U27-C278 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_a_nz.py:6 | class AccountEdiXmlUbl_A_Nz | INFERENCE | e-document module installed | — | Country-named builder classes live in the generic e-document package. | N-U27-034 |
| VDR-U27-C279 | FUNCTION MAPPING REQUIRED | n/a (no source line) | n/a | UNKNOWN | n/a | — | Reachability of each literal branch for a Thai company was not classified; static scan only. | N-U27-035 |
| VDR-U27-C280 | FUNCTION MAPPING REQUIRED | account/models/company.py:209 | The country to use the tax | FACT | always | — | The help of the fiscal-country field says it is the country whose tax reports the company uses, separate from the address country (company country is a different field). | N-U27-008 |
| VDR-U27-C281 | FUNCTION MAPPING REQUIRED | n/a (no source line) | n/a | UNKNOWN | n/a | RT | Multi-jurisdiction session behaviour and branch with different fiscal country were not executed; RT required. | N-U27-023 |
| VDR-U27-C282 | FUNCTION MAPPING REQUIRED | l10n_bf/__manifest__.py:12 | 'depends': [ | INFERENCE | mechanical manifest recount | — | Dependency pattern among the 227 packs (mechanical): 135 depend on at least one other l10n pack and 92 do not; in-degree leaders: l10n_syscohada 17, l10n_fr_account 9, l10n_din5008 8, l10n_gcc_invoice 8, l10n_latam_base 7, l10n_latam_invoice_document 6, l10n_in 5, l10n_es 5. Generic dependencies across the 227: account 126, base_vat 43, account_edi_ubl_cii 39, base_iban 24, point_of_sale 18, base 9, account_debit_note 8, sale 7. 26 modules host more than one template code (l10n_es 11, l10n_fr_account 7); 160 template codes exist in total including th. | N-U27-080 |
| VDR-U27-C283 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:14 | ondelete={'ewallet_id': 'set default' | FACT | th installed, uninstall | — | Selection values added by a pack declare an ondelete rule (here 'set default' for the three Thai proxy types) so that uninstalling the pack resets stored values; 39 packs use selection_add and 21 packs declare ondelete rules (mechanical grep); another pack resets its reference-standard value to the core default by lambda. | N-U27-067 |
| VDR-U27-C284 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:331 | Make sure that the selected currencies | FACT | company create | — | Creating a company activates its currency if it was inactive, so selecting a jurisdiction currency also enables it database-wide (currencies are global records). | N-U27-001 |
| VDR-U27-C285 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:78 | compute='_compute_address' | FACT | always | — | The company address country is derived from the company's partner address (compute with inverse), not stored on the company itself. | N-U27-001 |
