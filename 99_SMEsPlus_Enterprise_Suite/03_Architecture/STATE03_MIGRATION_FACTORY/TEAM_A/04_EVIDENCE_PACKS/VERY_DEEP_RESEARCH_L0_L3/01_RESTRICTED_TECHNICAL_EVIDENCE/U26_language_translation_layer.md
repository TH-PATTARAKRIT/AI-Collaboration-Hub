# U26 language_translation_layer — RESTRICTED TECHNICAL EVIDENCE

> **RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION**
> Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**

| Field | Value |
|---|---|
| Unit | U26 `language_translation_layer` (VDR L2/L3 worker output) |
| Modules studied | `base` (res.lang, wizards, ir.module loading, ir.qweb t-lang, ir.actions.report, res.country/currency/partner/users), plus framework core outside `odoo/addons` (`odoo/tools/translate.py`, `odoo/orm/fields_textual.py`, `odoo/orm/models.py`, `odoo/orm/environments.py`, `odoo/http.py`, `odoo/modules/loading.py`, `odoo/cli/i18n.py`, `odoo/service/db.py`, `odoo/tools/convert.py`, `odoo/tools/misc.py`, `odoo/tools/config.py`), and focused reads of `account`, `sale`, `purchase`, `stock`, `product`, `uom`, `analytic`, `l10n_th`, `mail`, `web` (JS l10n), `http_routing`, `website`, `website_sale`, `portal`, `auth_signup`, `transifex`, `base_import_module`, `base_setup`, `account_check_printing`, `sale_management`, `l10n_gcc_invoice` (not installed) |
| Source revision | `19.0.post20260921` (Odoo 19 Community) |
| Date | 2026-10-02 |
| Claim-ID prefix / Neutral prefix | `VDR-U26-C###` (addons tree, checked by vdr_check.py) and `CORE-U26-K###` (framework core outside `odoo/addons`, section 12B, checked by a separate script) / `N-U26-###` |
| Method | static source read (every pointer viewed) + mechanical scans (Unicode block, regex counts, po statistics, file counts) + read-only configuration queries on the restored DB (counts, flags, names of seeded configuration only; no business, partner, user or credential values; no translation text recorded). No source modified, Odoo not started, no git state change. |
| Limits | No V-level, completeness, coverage %, Gate PASS or Clean-Room approval is asserted. Anything needing execution is flagged `RT`. This unit studies a design constraint comparison only: no design is proposed and no Thai text is presented as a requirement; Thai strings are never reproduced here. |

## 0. Scope notes and standing design constraint

**Standing design constraint (programme owner; concerns the future SMEsPlus design, not Odoo).** Canonical and default language English (en_US); Thai (th_TH) as a translation layer with stable translation keys; no Thai UI text hard-coded in source. Approved delta (coordinator, 2026-10-02): technical and business terminology is English, default UI language English, Thai UI is a translation layer; Thai statutory documents may use a legally required Thai presentation independently of UI language; CAP-U26-09 and CAP-U26-05 therefore establish how Odoo selects document language and where fixed-language text lives. Observations only.

**Core architectural findings (each backed by claims below).**

| # | Finding | Claims |
|---|---|---|
| 1 | Code-level terms: the English source sentence IS the key. No symbolic keys exist. Lookup = (owning module, language) -> {English sentence: translation}; module detected from the calling frame. No plural, no context argument; extraction keywords are only `_`, `_lt` (py) and `_t` (js). | CORE-U26-K007, CORE-U26-K008, CORE-U26-K011, CORE-U26-K023, CORE-U26-K024, CORE-U26-K021, VDR-U26-C058 |
| 2 | Data-level terms: stored in jsonb per translatable field as {lang: text} with `en_US` always present; stable identifier of a translated record = external id (module.xmlid) + field name (+ source term for term-level fields), used by po `model:`/`model_terms:` entries and by `field@lang` columns in data files. | CORE-U26-K028, CORE-U26-K029, CORE-U26-K042, CORE-U26-K050, CORE-U26-K051, VDR-U26-C178 |
| 3 | English is the base and fallback everywhere: code (identity), data (`COALESCE(lang, en_US)`), chart templates (loaded in en_US then translated). | CORE-U26-K008, CORE-U26-K030, CORE-U26-K031, VDR-U26-C056 |
| 4 | Thai in Community is a translation layer in files (th.po in 406 modules; `@th_TH`/`@th` columns in l10n_th data), NOT hard-coded in Python; but Thai script is present as data outside translation files in 16 files, including 77 province names that have no English value (non-translatable field). | VDR-U26-C166, VDR-U26-C167, VDR-U26-C171, VDR-U26-C173, VDR-U26-C156, VDR-U26-C086, VDR-U26-C088 |
| 5 | Document language is chosen by the document partner's language via the template directive t-lang (52 uses, none a constant); the report action has no language field; stored invoice PDFs are not regenerated; a fixed-second-language precedent exists only in a non-installed localization (hard-coded language code in the template). | VDR-U26-C193, VDR-U26-C216, VDR-U26-C201, VDR-U26-C202, VDR-U26-C212 |
| 6 | Locale data per language is limited to numeric Gregorian date/time patterns, week start, grouping, separators and direction; no calendar-era, numeral or collation setting; amount-in-words depends on an external optional library whose Thai support cannot be established from the source tree. | VDR-U26-C005, CORE-U26-K058, VDR-U26-C138, VDR-U26-C141, VDR-U26-C147 |

**Function-ID mapping.** The existing 53-entry Function-ID index contains no language/translation function; every capability is `FUNCTION MAPPING REQUIRED`.

**Framework core caveat.** The worker specification limits the claims checker to `odoo/addons`. The language and translation mechanism is implemented largely in framework core files outside that tree. Those claims are listed in section 12B with ids `CORE-U26-K###` and the same nine columns; they were anchor-checked by a separate script (result reported in section 13) but are NOT covered by `vdr_check.py`.

**Read and not read (honest).** Read in full: `base/models/res_lang.py`, `base/wizard/base_language_install.py`, `base_export_language.py`, `base_import_language.py`, `tools/translate.py` (lines 1-90, 405-1065, 1192-1515 and 1516-1930; NOT read: the `xml_translate`/`html_translate` term converters at 90-405 and the QWeb/spreadsheet extractors at 1066-1191), `orm/fields_textual.py` (lines 30-480), `account/models/chart_template.py` (lines 18-70, 190-260, 520-700, 1355-1560), `http_routing` ir_http (lines 255-420), `transifex/models/*`, `cli/i18n.py` (lines 1-260). Read partly: `orm/models.py` (3495-3760, 5275-5310), `base/models/ir_module.py` (870-1000), `base/models/res_users.py`, `res_partner.py`, `res_country.py`, `mail_render_mixin.py`, `mail_template.py`, `website/models/*` (language parts), account send wizard/models (language parts), report templates (language directives only). Not read: term converters (`xml_translate`, `html_translate`) beyond signatures, translation dialog JS, `ir_ui_view` translation write path, spreadsheet term extraction, `website` copy-on-write view translation details, `base_import_module` beyond the `_load_module_terms` hook, `.po` contents (counted by script only; no text reproduced). A non-Community file `odoo/addons/STATE03_SMD_SOURCE_VERIFICATION_FINDINGS.md` exists in the studied folder and contains Thai text; it was excluded and not relied upon.

## CAP-U26-01 Language master and activation

**Function-ID:** FUNCTION MAPPING REQUIRED

**D1 — business purpose & process semantics.** One catalogue entry per language defines how text, numbers, dates, week and direction behave; activating an entry loads its translations and makes it selectable for users, contacts, websites and templates. Business purpose: control which languages the installation speaks and how locale-dependent values print. VDR-U26-C001, VDR-U26-C002, VDR-U26-C022, VDR-U26-C016

**D2 — architecture / data / object relationships.** res.lang (global, no company field) is referenced by res.partner.lang and res.users.lang (selection values = language code, not many2one), website.language_ids / default_lang_id (many2one), mail.template.lang (expression), base.language.install (many2many). Settings live in ir.default (res.partner.lang) and company partner. Cache: LangDataDict via ormcache 'stable'. VDR-U26-C020, VDR-U26-C044, VDR-U26-C043

**D3 — source / technical / workflow logic.**

- Activation: user clicks Activate / runs Install wizard -> res.lang.action_unarchive or base.language.install.lang_install -> set active -> ir.module.module._update_translations(codes[, overwrite]) -> _load_module_terms (CAP-U26-04). VDR-U26-C016, VDR-U26-C037
- Creation outside catalogue: _create_lang(code) reads OS locale (setlocale / nl_langinfo / localeconv), builds the row, creates active. VDR-U26-C017
- Database init: install_lang() reads config load_language (first code) else en_US, activates or creates it, sets ir.default and company partner lang. VDR-U26-C018, VDR-U26-C019, VDR-U26-C036, CORE-U26-K006
- Session language resolution: context_get / get_lang / pre_dispatch fallback chain. VDR-U26-C046, CORE-U26-K002, VDR-U26-C048, CORE-U26-K001

State diagram:

- inactive -> active [action_unarchive or lang_install; translations loaded] (VDR-U26-C016)
- active -> inactive [write active=False; blocked if used by users, partners or websites] (VDR-U26-C025, VDR-U26-C026, VDR-U26-C043)
- inactive -> deleted [unlink; not for en_US, not if active] (VDR-U26-C029, VDR-U26-C030)

**Ten dimensions.**

| # | Dimension | Behaviour (claims) |
|---|---|---|
| 1 | Happy path | Install wizard or Activate button activates, loads translation files for all installed modules, shows a success notification. VDR-U26-C037, VDR-U26-C016 |
| 2 | Reversal / negative | Deactivate only when unused by users, contacts, websites; deactivation discards the default partner language; delete only inactive non-base language. VDR-U26-C025, VDR-U26-C026, VDR-U26-C027, VDR-U26-C029, VDR-U26-C030 |
| 3 | Multi-company / data scope | res.lang has no company field and no record rule (DB 0 rules): the catalogue is global. Company influence is only through the company partner's language in the fallback chain. VDR-U26-C046, VDR-U26-C049 |
| 4 | Side effects | Cache clear; url_code shortening on activation; translations of every installed module reloaded; website and account hooks on load. VDR-U26-C023, VDR-U26-C028, VDR-U26-C097, VDR-U26-C103 |
| 5 | Configuration & optionality | load_language (first only) and ir.default res.partner.lang; date/time/grouping/separator/week/direction per row; settings screen entry. VDR-U26-C018, VDR-U26-C019, VDR-U26-C042 |
| 6 | Validation & constraints | Unique name/code/url_code; code immutable; at least one active; directive whitelist; AM/PM onchange. VDR-U26-C010, VDR-U26-C024, VDR-U26-C011, VDR-U26-C012, VDR-U26-C013 |
| 7 | Roles & permissions | System: CRUD and install wizard; others read. Menus debug-only. DB confirms 4 res.lang ACL rows and no rules. VDR-U26-C040, VDR-U26-C039, VDR-U26-C041, VDR-U26-C183 |
| 8 | Scheduled / automated | None for this capability (translation refresh cron belongs to CAP-U26-04). NOT APPLICABLE for res.lang itself. |
| 9 | Exception & failure | No active language logs an error at registry hook; formatting with inactive language raises UserError; unknown locale warns and uses default locale data. VDR-U26-C014, VDR-U26-C032, VDR-U26-C017 |
| 10 | Accounting, audit, compliance | No accounting effect. Locale knobs are limited to numeric Gregorian patterns; no calendar-era or collation setting exists, relevant to statutory date presentation (see CAP-U26-06). VDR-U26-C005, CORE-U26-K058 |

**DB reconciliation (configuration only).** res_lang 93 rows, 1 active (en_US), th_TH present inactive with source values; ir_default res.partner.lang = en_US; all partners/users en_US; website 29 rows en_US only; ir_rule rows for res.lang: 0; ir_model_access: res.lang 4 rows (source: 4). VDR-U26-C035, VDR-U26-C049, VDR-U26-C050

**Unknown / Runtime list.**

- RT: loading of translations upon activation of a new language (timing, memory).
- RT: _create_lang output for locales absent from the catalogue depends on the host OS.
- UNKNOWN: effect on cached web-client localization after activation (client clears caches on lang_install RPC per localization_service.js:39-44, read but not claimed).

## CAP-U26-02 Translatable source strings (code-level terms)

**Function-ID:** FUNCTION MAPPING REQUIRED

**D1 — business purpose & process semantics.** Business purpose: allow program-defined terms (messages, labels built in code, exception texts, computed phrases) to be shown in the reader's language. CORE FINDING: the English source text is the lookup key; no stable symbolic keys exist for code-level terms. CORE-U26-K007, CORE-U26-K008

**D2 — architecture / data / object relationships.** Data structures: process-wide dicts CodeTranslations.python_translations / web_translations keyed (module, lang) -> {source_text: translation}; fed from <module>/i18n/<lang>.po (and i18n_extra) filtered by comment tags odoo-python / odoo-javascript. Not stored in the DB. CORE-U26-K017, CORE-U26-K018, CORE-U26-K019, CORE-U26-K020

**D3 — source / technical / workflow logic.**

- Call: _('text', args) / env._('text') / _lt('text') -> _get_translation_source (module from frame, lang from context/env/request/user) -> get_translation(module, lang, source, args) -> source if en_US; else pools.get(source, source) -> apply markup/lazy/list handling -> translation % args with fallback to source on format errors. CORE-U26-K015, CORE-U26-K016, CORE-U26-K012, CORE-U26-K011, CORE-U26-K007, CORE-U26-K009, CORE-U26-K010
- Client: _t(source, ...) -> TranslatedString -> translatedTerms[module][source] ?? global[source] ?? source -> sprintf. VDR-U26-C052, VDR-U26-C051, VDR-U26-C053
- Extraction (export): scan python (_ , _lt), JS (_t), QWeb, spreadsheets in installed modules -> po entries with comments odoo-python/odoo-javascript; strings without letters skipped. CORE-U26-K023, CORE-U26-K026, CORE-U26-K025
- Chart-template data uses the same pools with module taken from the @template function. VDR-U26-C054, VDR-U26-C055, VDR-U26-C056

State diagram:

- not translated -> translated [po file contains non-empty msgstr for the English sentence in module pool] (CORE-U26-K007, CORE-U26-K018)
- translated -> orphaned [English wording edited; old msgid no longer matches] (CORE-U26-K007 inference, see RISK)

**Ten dimensions.**

| # | Dimension | Behaviour (claims) |
|---|---|---|
| 1 | Happy path | English sentence matched in the module's pool for the reader language; placeholders formatted. CORE-U26-K007, CORE-U26-K010 |
| 2 | Reversal / negative | No match: English returned. Bad placeholders: error logged, English used. Missing lang: untranslated and warning. CORE-U26-K007, CORE-U26-K010, CORE-U26-K012 |
| 3 | Multi-company / data scope | NOT APPLICABLE: code translations are process-global per module and language; no company dimension. CORE-U26-K017 |
| 4 | Side effects | None on data; log entries on failure; lazy terms evaluated late. CORE-U26-K013 |
| 5 | Configuration & optionality | Languages active; i18n_extra folder; default_lang on lazy terms; regional override of generic file. CORE-U26-K019, CORE-U26-K020, CORE-U26-K014 |
| 6 | Validation & constraints | No escaped newlines in terms; lazy terms not comparable; one translation per sentence per module. CORE-U26-K022, CORE-U26-K013, CORE-U26-K021 |
| 7 | Roles & permissions | NOT APPLICABLE at call time. Editing is by supplying files (CAP-U26-04). |
| 8 | Scheduled / automated | NOT APPLICABLE (the optional external-service reload job is in CAP-U26-04). |
| 9 | Exception & failure | Invalid context language raises; malformed translation logged; lookups never raise for missing terms. CORE-U26-K001, CORE-U26-K012, CORE-U26-K010 |
| 10 | Accounting, audit, compliance | Error messages shown to users and validation texts depend on this mechanism; wording edits change keys. No plural, no context key. CORE-U26-K024, CORE-U26-K023, CORE-U26-K021 |

**DB reconciliation (configuration only).** No DB storage of code translations (read from files at runtime). The external-service module's table of code translations has 0 rows. VDR-U26-C102

**Unknown / Runtime list.**

- RT: memory growth of in-process pools with many languages x modules.
- RT: partially translated regional file behaviour (th_TH overriding th) not exercised; th_TH has no own file in Community.
- UNKNOWN: whether any addon registers keys differently from msgid-by-source — none found in files read.

## CAP-U26-03 Translatable data on records

**Function-ID:** FUNCTION MAPPING REQUIRED

**D1 — business purpose & process semantics.** Business purpose: names and texts of master data and screens may be edited per language, with English as the guaranteed fallback. CORE-U26-K027, CORE-U26-K030

**D2 — architecture / data / object relationships.** Storage: one jsonb column per translatable stored field holding {lang: text} (plus en_US); term fields store structured text with terms translated inside. Catalogue of translatable fields: ir_model_fields.translate (DB 357 stored). CORE-U26-K028, CORE-U26-K029, VDR-U26-C085

**D3 — source / technical / workflow logic.**

- Read: value[lang] if present else value['en_US'] (cache fallback; SQL COALESCE for search/order). CORE-U26-K030, CORE-U26-K031
- Write whole-value field: set current lang entry; also en_US when en_US inactive. Term field: rebuild dictionary of terms and re-translate other languages. CORE-U26-K033, CORE-U26-K034
- Edit per language: update_field_translations(field, {lang: value}) with write ACL + field access; get_field_translations for the dialog. CORE-U26-K037, CORE-U26-K038
- Export of record translations: TranslationRecordReader / export wizard model mode; creates external ids. CORE-U26-K041, CORE-U26-K042, VDR-U26-C092
- Chart-template data: created in English, then translated via _load_translations from fname@lang columns or code translations; account.journal.code translated although untranslatable. VDR-U26-C082, VDR-U26-C083, VDR-U26-C081

State diagram:

- English-only -> multi-language [value written in another language or imported translation] (CORE-U26-K033, CORE-U26-K046)
- translated -> English fallback [translation removed with False/empty] (CORE-U26-K037)

**Ten dimensions.**

| # | Dimension | Behaviour (claims) |
|---|---|---|
| 1 | Happy path | Edit in translation dialog stores per-language text; reading with that language returns it. CORE-U26-K037, CORE-U26-K038, CORE-U26-K033 |
| 2 | Reversal / negative | False or empty removes the translation; reading falls back to English. CORE-U26-K037, CORE-U26-K030 |
| 3 | Multi-company / data scope | Translation values are not company-scoped; they follow the record. Chart records are per company with company-prefixed external ids, translated per company. VDR-U26-C082 |
| 4 | Side effects | Search/order language-dependent; trigram prefilter; document line text frozen at creation; export creates external ids. CORE-U26-K031, CORE-U26-K032, VDR-U26-C075, CORE-U26-K041 |
| 5 | Configuration & optionality | Field table: see section CAP table below; sale/purchase/l10n_th declare none. VDR-U26-C059, VDR-U26-C061, VDR-U26-C062, VDR-U26-C063, VDR-U26-C065, VDR-U26-C079 |
| 6 | Validation & constraints | No context-dependent stored translated fields; fragment-count consistency for term fields. CORE-U26-K035, CORE-U26-K036, CORE-U26-K034 |
| 7 | Roles & permissions | Write on record and field required to edit translations; mail template adds dynamic-template right. CORE-U26-K037, VDR-U26-C182 |
| 8 | Scheduled / automated | NOT APPLICABLE (no cron for data translations). |
| 9 | Exception & failure | Term extraction errors logged per record in export; missing external ids created. CORE-U26-K042, CORE-U26-K041 |
| 10 | Accounting, audit, compliance | Tax, account, journal, payment-term, report and company header/footer names are translatable, so printed documents change with language; posted document lines keep frozen text. VDR-U26-C059, VDR-U26-C063, VDR-U26-C064, VDR-U26-C070, VDR-U26-C075, VDR-U26-C076 |

**DB reconciliation (configuration only).** 357 stored translatable fields over 179 models (295 standard, 59 html, 3 xml); sampled counts of stored values: product.template.name 16, account.account.name 147, account.tax.name 18, account.journal.name 7, account.payment.term.name 10, account.tax.group.name 5, uom.uom.name 30, ir_ui_menu.name 729, ir_ui_view.arch_db 7113, ir.actions.report.name 78, res.country.name 251, mail.template.name 62; the number of values with any key other than en_US is 0 in every translatable column counted (338 columns, 52,892 non-null values). VDR-U26-C085

**Unknown / Runtime list.**

- RT: term-level re-alignment after English edits.
- RT: trigram prefilter effect on performance for large product lists.
- UNKNOWN: ir.actions.* inherited-column storage was counted through their own tables only for the report and window tables; per-table counts for ir_act_url/client/server not separately verified.

### CAP-U26-03 table — translatable stored fields (module -> model -> fields), from restored DB `ir_model_fields` joined to the declaring module's external id, cross-checked against source definitions in claims

Totals: 357 stored translatable fields over 179 models (translate kinds: standard=whole value, html_translate and xml_translate=term level). Declaring-module field counts (top 12): base: 42; account: 26; website_slides: 22; website_blog: 21; website: 17; website_forum: 17; event: 15; survey: 13; test_website: 12; mail: 11; test_orm: 11; gamification: 9. Modules with 0 translatable fields: sale=0, purchase=0, l10n_th=0, portal=0, sale_stock=0, purchase_stock=0, stock_account=0, account_payment=0, purchase_requisition=0, sale_project=0.

| Module (declaring) | Model | Translatable stored fields |
|---|---|---|
| account | account.account | description, name |
| account | account.account.tag | name |
| account | account.cash.rounding | name |
| account | account.fiscal.position | name, note (html_translate) |
| account | account.group | name |
| account | account.incoterms | name |
| account | account.journal | name |
| account | account.journal.group | name |
| account | account.payment.method | name |
| account | account.payment.term | name, note (html_translate) |
| account | account.reconcile.model | name |
| account | account.reconcile.model.line | label |
| account | account.report | name |
| account | account.report.column | name |
| account | account.report.line | name |
| account | account.tax | description (html_translate), invoice_label, invoice_legal_notes (html_translate), name |
| account | account.tax.group | name, preceding_subtotal |
| account | res.company | invoice_terms (html_translate), invoice_terms_html (html_translate) |
| analytic | account.analytic.account | name |
| analytic | account.analytic.plan | name |
| base | ir.actions.act_url | help (html_translate), name |
| base | ir.actions.act_window | help (html_translate), name |
| base | ir.actions.act_window_close | help (html_translate), name |
| base | ir.actions.actions | help (html_translate), name |
| base | ir.actions.client | help (html_translate), name |
| base | ir.actions.report | help (html_translate), name, print_report_name |
| base | ir.actions.server | help (html_translate), name |
| base | ir.embedded.actions | name |
| base | ir.model | name |
| base | ir.model.constraint | message |
| base | ir.model.fields | field_description, help |
| base | ir.model.fields.selection | name |
| base | ir.module.category | description, name |
| base | ir.module.module | description, shortdesc, summary |
| base | ir.ui.menu | name |
| base | ir.ui.view | arch_db (xml_translate) |
| base | res.company | company_details (html_translate), report_footer (html_translate), report_header (html_translate) |
| base | res.country | name, vat_label |
| base | res.country.group | name |
| base | res.currency | currency_subunit_label, currency_unit_label |
| base | res.groups | comment, name |
| base | res.groups.privilege | name |
| base | res.partner.category | name |
| base | res.partner.industry | full_name, name |
| crm | crm.lost.reason | name |
| crm | crm.recurring.plan | name |
| crm | crm.stage | name |
| delivery | delivery.carrier | carrier_description, name |
| digest | digest.digest | name |
| digest | digest.tip | name, tip_description (html_translate) |
| mail | ir.actions.server | name |
| mail | mail.activity.type | default_note (html_translate), name, summary |
| mail | mail.alias | alias_bounced_content (html_translate) |
| mail | mail.message.subtype | description, name |
| mail | mail.template | body_html, description, name, subject |
| mrp | mrp.workcenter.productivity.loss | name |
| payment | payment.method | name |
| payment | payment.provider | auth_msg (html_translate), cancel_msg (html_translate), done_msg (html_translate), name, pending_msg (html_translate), pre_msg (html_translate) |
| product | product.attribute | name |
| product | product.attribute.value | name |
| product | product.pricelist | name |
| product | product.tag | name |
| product | product.template | description (html_translate), description_purchase, description_sale, name |
| project | project.project | label_tasks, name |
| project | project.project.stage | name |
| project | project.role | name |
| project | project.tags | name |
| project | project.task.type | name |
| sale_management | sale.order.template | note (html_translate) |
| sale_management | sale.order.template.line | name |
| stock | product.removal | method, name |
| stock | product.template | description_picking, description_pickingin, description_pickingout |
| stock | stock.picking.type | name |
| stock | stock.route | name |
| stock | stock.rule | name |
| stock | stock.scrap.reason.tag | name |
| uom | uom.uom | name |

Not translatable (source-confirmed): product.category.name, stock.warehouse.name, stock.location.name, res.country.state.name, res.partner.name, sale.order.line.name, account.move.line.name, account.journal.code (translated only at chart load by an explicit exception). Claims: VDR-U26-C068, VDR-U26-C069, VDR-U26-C075, VDR-U26-C076, VDR-U26-C083

## CAP-U26-04 Translation files, import and export

**Function-ID:** FUNCTION MAPPING REQUIRED

**D1 — business purpose & process semantics.** Business purpose: ship, load, extend and extract translations without code changes, per module and language, with controlled overwrite. VDR-U26-C089, VDR-U26-C090

**D2 — architecture / data / object relationships.** Artifacts: <module>/i18n/<lang>.po and <module>.pot; optional i18n_extra; data files with @lang columns; DB: jsonb columns and (module transifex) transifex.code.translation. Wizards: base.language.install/import/export. CLI: odoo i18n. VDR-U26-C086, VDR-U26-C092, VDR-U26-C093, CORE-U26-K053

**D3 — source / technical / workflow logic.**

- Load: install/upgrade module -> _update_translations(all langs, overwrite=config) -> topological order -> _load_module_terms -> importer.load_file(po) + data-file readers -> importer.save(overwrite) -> single batch SQL; account/website/website_sale hooks follow. CORE-U26-K043, VDR-U26-C089, VDR-U26-C090, VDR-U26-C091, CORE-U26-K045, CORE-U26-K046, VDR-U26-C103, VDR-U26-C097, VDR-U26-C098
- Import wizard: activate/create lang -> TranslationImporter.load(buf, fmt, code) -> save(overwrite). VDR-U26-C093, VDR-U26-C094
- Export wizard / CLI: TranslationModuleReader or RecordReader -> writer (po/csv/tgz) grouped by source. VDR-U26-C092, CORE-U26-K053, CORE-U26-K055, CORE-U26-K026
- Fallback of untranslated terms: English source (code) / English value (data). CORE-U26-K007, CORE-U26-K030

State diagram:

- language file absent -> loaded [module install/language activate] (VDR-U26-C090)
- translation present -> overwritten [overwrite flag and record not noupdate, or forced] (CORE-U26-K045)

**Ten dimensions.**

| # | Dimension | Behaviour (claims) |
|---|---|---|
| 1 | Happy path | Activate language -> all installed modules' Thai-or-other files loaded; module update reloads. VDR-U26-C089, CORE-U26-K043 |
| 2 | Reversal / negative | No undo: overwrite replaces; no-translation modules logged; import failure raises. CORE-U26-K045, VDR-U26-C090, VDR-U26-C094 |
| 3 | Multi-company / data scope | NOT APPLICABLE for files; chart translation applies per company through chart template reload. VDR-U26-C082 |
| 4 | Side effects | Cache clear and invalidation after save; website copy-on-write translations; account tag translations. CORE-U26-K045, VDR-U26-C097, VDR-U26-C103 |
| 5 | Configuration & optionality | --i18n-overwrite with -u; --load-language; wizard overwrite defaults. CORE-U26-K044, VDR-U26-C038, VDR-U26-C093 |
| 6 | Validation & constraints | Skip rules for empty/code/obsolete/unknown; formats csv/po only for import. CORE-U26-K047, CORE-U26-K048, VDR-U26-C094 |
| 7 | Roles & permissions | Import/install: system; export: any internal user; menus: debug. DB confirms. VDR-U26-C095, VDR-U26-C096, VDR-U26-C039, VDR-U26-C183 |
| 8 | Scheduled / automated | Transifex reload job weekly (read-only list); no cron for loading. VDR-U26-C100, VDR-U26-C101, VDR-U26-C102 |
| 9 | Exception & failure | Unknown language error log; unreadable file logged; import UserError. CORE-U26-K049, VDR-U26-C094, VDR-U26-C090 |
| 10 | Accounting, audit, compliance | Overwrite can change printed statutory wording of taxes/accounts on non-protected records; protected (noupdate) records keep customizations. CORE-U26-K045, CORE-U26-K046 |

**DB reconciliation (configuration only).** 356 installed modules, 310 with th.po; res_lang: 1 active; no non-English translations stored; transifex table 0 rows; Transifex cron active weekly; language wizards ACL as source. VDR-U26-C087, VDR-U26-C102, VDR-U26-C183

**Unknown / Runtime list.**

- RT: duration/memory of loading 310 Thai files on activation.
- RT: effect of overwrite on customised master data.
- UNKNOWN: contents of translation quality (not assessed; no translation text reproduced).

### CAP-U26-04 table — translation files (counts only, no text)

| Measure | Value | Claim |
|---|---|---|
| Community module manifests under odoo/addons | 692 | VDR-U26-C086 |
| Modules with an i18n folder / with a .pot template | 607 / 606 | VDR-U26-C086 |
| Modules shipping th.po / th_TH.po / i18n_extra Thai | 406 / 0 / 0 | VDR-U26-C086 |
| Installed modules (DB) / of which with th.po | 356 / 310 | VDR-U26-C087 |
| th.po entries total / translated | 64,199 / 52,873 | VDR-U26-C088 |
| per module entries/translated: base 6569/5608; account 3171/2684; sale 862/773; purchase 587/499; stock 1809/1565; product 749/603; uom 63/52; analytic 162/155; mail 2090/1681; portal 229/205; web 4375/4143; website 3084/2325; http_routing 26/24; l10n_th 23/23 | counts | VDR-U26-C088 |

## CAP-U26-05 Per-user, per-partner and per-template language

**Function-ID:** FUNCTION MAPPING REQUIRED

**D1 — business purpose & process semantics.** Business purpose: the interface follows the user; customer-facing output follows the customer; emails follow template or recipient; portal/website follow request choice. VDR-U26-C109, VDR-U26-C106, VDR-U26-C117, VDR-U26-C125

**D2 — architecture / data / object relationships.** Fields: res.partner.lang (stored computed selection), res.users inherits it; mail.template.lang expression; website.language_ids/default_lang_id; cookie frontend_lang; wizard lang for invoice send. VDR-U26-C107, VDR-U26-C108, VDR-U26-C116, VDR-U26-C128

**D3 — source / technical / workflow logic.**

- User session: stored lang -> request best_lang -> company partner lang -> en_US -> first active. VDR-U26-C109, CORE-U26-K004
- Document line text: product description rendered with partner/document language and frozen. VDR-U26-C110, VDR-U26-C111, VDR-U26-C113, VDR-U26-C114, VDR-U26-C115
- Email: template.lang expression or first customer partner lang -> _classify_per_lang -> render per language. VDR-U26-C117, VDR-U26-C118, VDR-U26-C119
- Invoice send: default mail_lang from template -> wizard lang -> recompute -> send; message model description translated. VDR-U26-C121, VDR-U26-C122, VDR-U26-C123
- Website/portal: URL prefix, cookie, context, website default; frontend list from website; prefix for non-default. VDR-U26-C125, VDR-U26-C126, VDR-U26-C127, VDR-U26-C129, VDR-U26-C130

State diagram:

- contact language unset -> set [computed from parent or default] (VDR-U26-C045)
- language in use -> locked [cannot deactivate while used] (VDR-U26-C025, VDR-U26-C026, VDR-U26-C043)

**Ten dimensions.**

| # | Dimension | Behaviour (claims) |
|---|---|---|
| 1 | Happy path | Customer with language X receives invoice/order/email in X regardless of staff language (document language detailed in CAP-U26-09). VDR-U26-C106, VDR-U26-C117 |
| 2 | Reversal / negative | Language not active -> cannot be chosen; unset language falls back along the chain. VDR-U26-C107, VDR-U26-C109 |
| 3 | Multi-company / data scope | Language values are not company-scoped; fallback uses the company partner language; websites have their own language lists. VDR-U26-C109, VDR-U26-C128 |
| 4 | Side effects | Frozen line descriptions; cookie set; URL prefixes; invitation mail language. VDR-U26-C111, VDR-U26-C125, VDR-U26-C130, VDR-U26-C131 |
| 5 | Configuration & optionality | website module needed for language selection; browser redirect flag; template language expression. VDR-U26-C128, VDR-U26-C116 |
| 6 | Validation & constraints | Selection restricted to active languages; deactivation guards. VDR-U26-C107, VDR-U26-C025 |
| 7 | Roles & permissions | Users write own lang (self-writeable); admin sets others; website admins set website languages. VDR-U26-C047, VDR-U26-C120 |
| 8 | Scheduled / automated | NOT APPLICABLE. |
| 9 | Exception & failure | Invalid request language is corrected to the fallback; unknown template lang yields empty/fallback. VDR-U26-C048, VDR-U26-C127 |
| 10 | Accounting, audit, compliance | Customer-facing financial documents carry the partner language; an unintended partner language changes statutory wording. VDR-U26-C193, VDR-U26-C110 |

**DB reconciliation (configuration only).** All partners (7) and users' partners (4) = en_US; ir_default partner lang en_US; websites: 29 rows each only en_US. VDR-U26-C049, VDR-U26-C133

**Unknown / Runtime list.**

- RT: browser-language redirect and cookie interplay across domains.
- UNKNOWN: portal PDF download language path (not traced).

## CAP-U26-06 Formats and locale-dependent behaviours for Thailand

**Function-ID:** FUNCTION MAPPING REQUIRED

**D1 — business purpose & process semantics.** Business purpose: show numbers, amounts, dates and addresses in the conventions of the target locale and country. VDR-U26-C134, CORE-U26-K058, VDR-U26-C151

**D2 — architecture / data / object relationships.** Inputs: res.lang row (formats), res.currency (symbol, position, decimals, unit labels), res.country (address layout, name position, required flags, vat label), res.partner display address. Libraries: babel (dates), external num2words (words), Intl/Luxon in browser. CORE-U26-K056, VDR-U26-C136, VDR-U26-C154, VDR-U26-C141

**D3 — source / technical / workflow logic.**

- Amount: format_amount / monetary widget -> lang.format with grouping -> symbol before/after. CORE-U26-K057, VDR-U26-C134, VDR-U26-C136
- Date: posix pattern from res.lang -> posix_to_ldml -> babel.dates.format_date(locale from code). CORE-U26-K058, CORE-U26-K059
- Amount in words: currency.amount_to_text -> num2words(int, lang=iso_code).title(), fallback English; labels from currency; shown on invoice when company flag. VDR-U26-C141, VDR-U26-C144, VDR-U26-C145, VDR-U26-C150
- Address: country.address_format with state/country names -> display address. VDR-U26-C151, VDR-U26-C154, VDR-U26-C152
- Calendar era: no source handling found (grep for buddhist/calendar overrides: none); date patterns numeric Gregorian. VDR-U26-C005, CORE-U26-K058, VDR-U26-C138

State diagram:

- language row formats -> applied to rendering at read time (no stored formatted values) (VDR-U26-C134, CORE-U26-K058)

**Ten dimensions.**

| # | Dimension | Behaviour (claims) |
|---|---|---|
| 1 | Happy path | Formatted amounts, dates and addresses follow the language/country rows. CORE-U26-K057, CORE-U26-K058, VDR-U26-C154 |
| 2 | Reversal / negative | Missing num2words -> empty words; unsupported language -> English words; inactive language -> error. VDR-U26-C141, VDR-U26-C142, VDR-U26-C032 |
| 3 | Multi-company / data scope | Currency and country are per company/partner; formatting language is the render context language. CORE-U26-K056 |
| 4 | Side effects | None stored; strings embed currency unit labels. VDR-U26-C141 |
| 5 | Configuration & optionality | Company option for words; currency position; country layout; vat label; num2words dependency. VDR-U26-C150, VDR-U26-C136, VDR-U26-C152, VDR-U26-C143 |
| 6 | Validation & constraints | Date/time directive whitelist; address format validity constraint (res.country _check_address_format not claimed). VDR-U26-C012 |
| 7 | Roles & permissions | NOT APPLICABLE beyond configuration rights. |
| 8 | Scheduled / automated | NOT APPLICABLE. |
| 9 | Exception & failure | Words fallbacks; babel_locale_parse fallback to default/en_US. VDR-U26-C141, CORE-U26-K059 |
| 10 | Accounting, audit, compliance | Amount in words and tax identifier label appear on tax documents; Thai words support and Buddhist-era year are UNKNOWN/absent; province names Thai-only. VDR-U26-C147, VDR-U26-C156, VDR-U26-C161 |

**DB reconciliation (configuration only).** THB active, symbol after, 0.01 rounding; company chart th, display_invoice_amount_total_words true; country TH address layout as above; 77 TH states; 2131 states total; database collation en_US.UTF-8; extensions pg_trgm only. VDR-U26-C149, VDR-U26-C155, VDR-U26-C157, VDR-U26-C158

**Unknown / Runtime list.**

- UNKNOWN: whether the installed num2words version supports Thai (library not in source tree, not installed locally; requirements pin 0.5.10/0.5.13). Resolve by installing the pinned library and calling it with 'th' and with the iso code.
- RT: browser rendering of Thai locale (Intl may apply the Buddhist calendar in non-token outputs); server patterns are Gregorian.
- RT: production database collation.

## CAP-U26-07 Hard-coded text audit

**Function-ID:** FUNCTION MAPPING REQUIRED

**D1 — business purpose & process semantics.** Business purpose: measure where user-facing text lives (code, data, translation files) and whether any Thai text is hard-coded in source, to compare with the programme's design constraint. Observations only. VDR-U26-C162, VDR-U26-C166, VDR-U26-C167

**D2 — architecture / data / object relationships.** Method: mechanical scans (regex counts, Unicode block U+0E00-U+0E7F) over odoo/ (Community); po statistics parsed by script; DB counts. Counts reproduced in claims; no translation text is reproduced. VDR-U26-C162, VDR-U26-C163, VDR-U26-C164, VDR-U26-C165

**D3 — source / technical / workflow logic.**

- Python code: gettext calls and exception messages counted per module; no Thai-script literal in non-test Python. VDR-U26-C162, VDR-U26-C166
- Data: Thai in l10n_th per-language columns and name@th fields; Thai province names in base; language catalogue native names; currency symbol. VDR-U26-C167, VDR-U26-C168, VDR-U26-C169, VDR-U26-C170, VDR-U26-C171, VDR-U26-C173, VDR-U26-C174, VDR-U26-C175
- Translation files: th.po entry counts by module. VDR-U26-C165, VDR-U26-C088
- Loader behaviour: @lang fields never reach the base value; translation applied by importer/chart loader. VDR-U26-C178, CORE-U26-K061

State diagram:

- English base value + Thai per-language value (record id + field + lang) in data files (VDR-U26-C178, VDR-U26-C167)

**Ten dimensions.**

| # | Dimension | Behaviour (claims) |
|---|---|---|
| 1 | Happy path | English base and Thai value coexist; Thai shown only when Thai active. VDR-U26-C178, VDR-U26-C167, VDR-U26-C171 |
| 2 | Reversal / negative | Where Thai is the only value (province names) no English exists. VDR-U26-C173 |
| 3 | Multi-company / data scope | NOT APPLICABLE for scans; chart data is copied per company on load. VDR-U26-C178 |
| 4 | Side effects | NOT APPLICABLE. |
| 5 | Configuration & optionality | Demo Thai literal only with demo data. VDR-U26-C172 |
| 6 | Validation & constraints | NOT APPLICABLE. |
| 7 | Roles & permissions | NOT APPLICABLE. |
| 8 | Scheduled / automated | NOT APPLICABLE. |
| 9 | Exception & failure | UNKNOWN: effect of renaming xmlids on Thai columns (inference only). |
| 10 | Accounting, audit, compliance | Chart-of-accounts and tax report line names exist in Thai as data translations; tax names in the chart have no Thai column. VDR-U26-C167, VDR-U26-C168, VDR-U26-C171 |

**DB reconciliation (configuration only).** No Thai-script literal was queried; DB holds only en_US keys in translatable columns; res_lang name for th_TH is native-script (counted not printed); res_country_state has 77 TH rows. VDR-U26-C035, VDR-U26-C157

**Unknown / Runtime list.**

- UNKNOWN: one non-Community artifact in the studied folder contains Thai text (excluded).
- UNKNOWN: Thai literals inside binary or generated assets (e.g. spreadsheet JSON, images) were scanned only as text.

### CAP-U26-07 table — where user-facing text lives (mechanical counts; excl. tests, i18n and static)

| Module | py files | gettext calls | raise Exception( | raise with bare literal | field defs | string/help literals (py) | xml files | xml string= attrs | placeholder/help attrs | `<field name="name">` seeded | files with Thai script | th.po entries (total/model/code/model_terms) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| l10n_th | 8 | 8 | 4 | 0 | 2 | 0 | 3 | 0 | 0 | 33 | 6 | 23/14/8/1 |
| account | 86 | 688 | 278 | 0 | 1160 | 905 | 72 | 633 | 124 | 335 | 0 | 3171/1793/730/938 |
| sale | 36 | 104 | 31 | 0 | 271 | 224 | 35 | 162 | 44 | 141 | 0 | 862/448/127/349 |
| purchase | 23 | 64 | 18 | 0 | 183 | 104 | 22 | 160 | 22 | 81 | 0 | 587/296/92/246 |
| stock | 57 | 278 | 105 | 0 | 719 | 290 | 71 | 495 | 93 | 301 | 0 | 1809/976/341/690 |
| product | 38 | 110 | 46 | 0 | 245 | 158 | 30 | 166 | 23 | 255 | 0 | 749/490/138/176 |
| uom | 4 | 4 | 2 | 0 | 9 | 2 | 3 | 5 | 1 | 36 | 0 | 63/51/7/7 |
| analytic | 11 | 14 | 9 | 0 | 56 | 34 | 7 | 25 | 5 | 53 | 0 | 162/111/32/33 |

Note: the scan shows 1 (account) and 2 (stock) raise-with-literal hits and these are joins of pre-built message lists (3 false positives) so the table lists 0 real bare-literal raises; l10n_th 'files with Thai script' = 4 CSV + 2 XML (6). Claims: VDR-U26-C162, VDR-U26-C163, VDR-U26-C164, VDR-U26-C165, VDR-U26-C166

### CAP-U26-07 table — Thai-script literals outside translation files in the Community tree (counts of files / lines only)

| Location (module / area) | Files | Lines with Thai script | Kind | Claim |
|---|---|---|---|---|
| base (data) | 3 | 77 + 1 + 1 | res.country.state.csv (77 province names, sole value), res.lang.csv (1 language name), res_currency_data.xml (1 symbol character) | VDR-U26-C173, VDR-U26-C174, VDR-U26-C175 |
| l10n_th (data) | 6 | 144 + 18 + 5 + 12 + 30 + 1 | account/tax/tax-group/asset template CSV columns `@th_TH`; tax report `name@th`; demo company city | VDR-U26-C167, VDR-U26-C168, VDR-U26-C169, VDR-U26-C170, VDR-U26-C171, VDR-U26-C172 |
| l10n_kh (data) | 1 | 1 | one stray Thai-block character inside Khmer text (module not installed) | VDR-U26-C176 |
| web (static lib/src) | 4 | 14 + 1 + 230 + 1 | fullcalendar locales, pdfjs viewer and Thai localization file, language self-name list | VDR-U26-C177 |
| tests (web search test, test_mail gateway test) | 2 | 2 + 2 | test fixtures | VDR-U26-C166 |
| Python files outside tests | 0 | 0 | none | VDR-U26-C166 |

## CAP-U26-08 Roles, security, failure behaviour and performance of translation administration

**Function-ID:** FUNCTION MAPPING REQUIRED

**D1 — business purpose & process semantics.** Business purpose: control who may administer languages and translations, and understand failure and performance characteristics. VDR-U26-C179, VDR-U26-C180, VDR-U26-C181

**D2 — architecture / data / object relationships.** ACL rows (res.lang, three wizards, transifex), menu groups (group_no_one), absence of record rules, one translation cron, caches and batch limits. VDR-U26-C179, VDR-U26-C180, VDR-U26-C187, CORE-U26-K062

**D3 — source / technical / workflow logic.**

- Edit: record write + field access -> _update_field_translations. VDR-U26-C182, CORE-U26-K037
- Admin: system group for catalogue changes, install, import. VDR-U26-C040, VDR-U26-C039, VDR-U26-C095
- Failure paths: UserError for invalid language, import errors; log-and-fallback for placeholders. CORE-U26-K065, VDR-U26-C185, CORE-U26-K010

State diagram:

- language config -> only changeable by administrators (VDR-U26-C040)

**Ten dimensions.**

| # | Dimension | Behaviour (claims) |
|---|---|---|
| 1 | Happy path | Administrator activates/imports; users read catalogue; editors edit translations with write rights. VDR-U26-C179, VDR-U26-C182 |
| 2 | Reversal / negative | Guards on deactivation and deletion; import errors roll back. VDR-U26-C025, VDR-U26-C185 |
| 3 | Multi-company / data scope | No record rules on catalogue; translations unscoped. VDR-U26-C183 |
| 4 | Side effects | Cache invalidation after changes. VDR-U26-C023 |
| 5 | Configuration & optionality | Developer-mode menus; Transifex module optional. VDR-U26-C181, VDR-U26-C100 |
| 6 | Validation & constraints | Uniqueness and constraint checks (CAP-U26-01). VDR-U26-C010 |
| 7 | Roles & permissions | Export open to internal users; import/install system-only. VDR-U26-C180, VDR-U26-C183 |
| 8 | Scheduled / automated | One cron (Transifex reload, 7 days) in DB. VDR-U26-C100, VDR-U26-C183 |
| 9 | Exception & failure | See neutral fail rule. VDR-U26-C184, VDR-U26-C185, VDR-U26-C186, CORE-U26-K065 |
| 10 | Accounting, audit, compliance | No dedicated translation audit trail; change tracking only where fields are tracked (UNKNOWN). VDR-U26-C182 |

**DB reconciliation (configuration only).** ir_model_access rows as claim; 0 ir_rule; 1 cron; 0 automations; menus 4. VDR-U26-C183

**Unknown / Runtime list.**

- UNKNOWN: whether translation edits create tracking messages for tracked fields.
- RT: load impact of activating many languages.

## CAP-U26-09 Document and report presentation language

**Function-ID:** FUNCTION MAPPING REQUIRED

**D1 — business purpose & process semantics.** Business purpose (observation only): establish how a document's language is selected and whether it can differ from the viewer's UI language, and where fixed document wording lives, so the target design can separate UI language from document-presentation language. VDR-U26-C191, VDR-U26-C193, VDR-U26-C201

**D2 — architecture / data / object relationships.** Objects: QWeb t-lang directive; report templates (account, sale, purchase, stock, l10n_th); res.partner.lang; mail.template.lang; invoice send wizard lang; ir.actions.report (no language field); stored invoice PDF binary. VDR-U26-C191, VDR-U26-C201, VDR-U26-C205, VDR-U26-C202

**D3 — source / technical / workflow logic.**

- Print: report action -> render template -> t-call document with t-lang=<partner language expression> -> o.with_context(lang) -> body, header, footer rendered in that language -> PDF split per article using data-oe-lang. VDR-U26-C193, VDR-U26-C195, VDR-U26-C196, VDR-U26-C194, VDR-U26-C197, VDR-U26-C199, VDR-U26-C200
- Stored invoice PDF: rendered once in the document language and saved on the invoice; not regenerated. VDR-U26-C202, VDR-U26-C203
- Email: template lang expression (may be constant) -> _render_lang -> classify per language -> render; staff can override in wizard. VDR-U26-C205, VDR-U26-C206, VDR-U26-C207
- Thailand: l10n_th invoice and commercial invoice documents use the partner language; title is an English literal in arch; Thai wording is in th.po. VDR-U26-C209, VDR-U26-C208, VDR-U26-C210, VDR-U26-C211
- Fixed second language precedent: dual-language block with code written into the template (not installed here). VDR-U26-C212, VDR-U26-C213

State diagram:

- document rendered in partner language -> stored on invoice -> reused (VDR-U26-C202)

**Ten dimensions.**

| # | Dimension | Behaviour (claims) |
|---|---|---|
| 1 | Happy path | Document in the partner language independent of staff language. VDR-U26-C193, VDR-U26-C195, VDR-U26-C196 |
| 2 | Reversal / negative | No partner language: payment receipt falls back to company partner language; delivery slip to viewer language; stored PDF is not regenerated after language change. VDR-U26-C194, VDR-U26-C197, VDR-U26-C202 |
| 3 | Multi-company / data scope | Company header/footer fields are per company and translatable; language is per partner, not per company. VDR-U26-C214, VDR-U26-C070 |
| 4 | Side effects | Email subject/body/model description follow chosen language; attachment follows partner language. VDR-U26-C207, VDR-U26-C202 |
| 5 | Configuration & optionality | No report-level language setting; email template expression; optional dual-language company flag in a non-installed localization. VDR-U26-C201, VDR-U26-C205, VDR-U26-C213 |
| 6 | Validation & constraints | t-lang only on t-call; language must be active. VDR-U26-C192 |
| 7 | Roles & permissions | Report actions limited by groups (invoice reports); no language-specific permission. VDR-U26-C203 |
| 8 | Scheduled / automated | NOT APPLICABLE. |
| 9 | Exception & failure | Missing master-data translation shows English inside translated document (inference). VDR-U26-C215 |
| 10 | Accounting, audit, compliance | Statutory invoice text is composed from report arch text, code phrases and translatable master data in the partner language; no fixed-language mechanism for the main invoice exists in Community. VDR-U26-C210, VDR-U26-C216, VDR-U26-C201 |

**DB reconciliation (configuration only).** DB: 78 report rows; invoice, Thai commercial invoice, sale, purchase, stock reports exist; no language column; stored PDF attachments: 0 (no invoices). VDR-U26-C204

**Unknown / Runtime list.**

- RT: portal download path language; wkhtmltopdf font coverage for Thai script.
- UNKNOWN: the output of a Thai-language invoice with Thai active (not run).
- UNKNOWN: whether any non-Community extension in the studied tree fixes the language (out of scope).

## 11. Runtime / AWT-required register (U26)

- RT-1 Language activation: time/memory when loading 310 Thai files; actual effect of overwrite on customised records (CAP-U26-01/04).
- RT-2 Creation of a language outside the catalogue depends on host OS locale data (CAP-U26-01).
- RT-3 Amount in words with the pinned number-to-words library for Thai, for English fallback, and without the library (CAP-U26-06).
- RT-4 Browser rendering of Thai locale (possible Buddhist-calendar year from Intl in non-token outputs; numerals) and wkhtmltopdf Thai font coverage (CAP-U26-06/09).
- RT-5 Rendering of an invoice with Thai active: which parts remain English (missing master-data translations), stored PDF not regenerated (CAP-U26-09).
- RT-6 Term-level translation re-alignment after English edits; trigram prefilter performance (CAP-U26-03).
- RT-7 Browser-language redirect and cookie across multiple websites/domains (CAP-U26-05).
- RT-8 Whether translation edits create tracking messages for tracked fields (CAP-U26-08).

## 12. DISCOVERED SUPPORTING MODULES and framework files

Community modules reached beyond a single owner and read only as far as needed: `account` (chart_template, ir_module hook, send wizard, reports), `sale`, `purchase`, `stock`, `product`, `uom`, `analytic`, `sale_management`, `l10n_th`, `mail` (render mixin, template), `web` (JS l10n, webclient controller, report templates), `http_routing`, `website`, `website_sale`, `portal`, `auth_signup`, `base_setup`, `base_import_module`, `transifex`, `account_check_printing`, `l10n_gcc_invoice` (precedent only; not installed), `l10n_kh` and `l10n_tr_nilvera_einvoice` (grep only). Framework core outside the addons tree: `odoo/tools/translate.py`, `odoo/orm/fields_textual.py`, `odoo/orm/models.py`, `odoo/orm/environments.py`, `odoo/http.py`, `odoo/modules/loading.py`, `odoo/cli/i18n.py`, `odoo/service/db.py`, `odoo/tools/convert.py`, `odoo/tools/misc.py`, `odoo/tools/config.py`, `odoo/tools/babel/python_extractor.py` (signature comments only). Contradictions with prior evidence: none found (U01 C435-C440 agree: res_lang guards, install wizard, context_get chain; U01 listed `res_lang.py` beyond lines 110-128/388-404 as not read; this unit read it fully).

## 12A. Claims table A (odoo/addons; verified by vdr_check.py)

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U26-C001 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:50 | _name = 'res.lang' | FACT | always | — | res.lang is the language master model with description 'Languages', ordered active desc then name. | N-U26-001 |
| VDR-U26-C002 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:73 | string='Locale Code' | FACT | always | — | Fields code (locale code), iso_code (name of the po files to use), url_code (language code shown in URLs) and active; code, name and url_code are required except iso_code. | N-U26-001 |
| VDR-U26-C003 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:74 | name of po files | FACT | always | — | iso_code help: the ISO code is the name of the po files used for translations. | N-U26-001 |
| VDR-U26-C004 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:77 | Right-to-Left | FACT | always | — | direction is a required selection ltr or rtl, default ltr. | N-U26-001 |
| VDR-U26-C005 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:58 | def _get_date_format_selection | FACT | always | — | date_format selection lists nine strftime patterns (%d/%m/%Y, %m/%d/%Y, %Y/%m/%d and the same with - and . separators); default %m/%d/%Y. | N-U26-002 |
| VDR-U26-C006 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:81 | %I:%M:%S %p | FACT | always | — | time_format selection has only two values: 24-hour %H:%M:%S (default) and 12-hour %I:%M:%S %p. | N-U26-002 |
| VDR-U26-C007 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:89 | First Day of Week | FACT | always | — | week_start is a required selection '1' (Monday) to '7' (Sunday), default '7'. | N-U26-002 |
| VDR-U26-C008 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:92 | Indian Grouping | FACT | always | — | grouping selection offers only '[3,0]' International and '[3,2,0]' Indian; default '[3,0]'. | N-U26-002 |
| VDR-U26-C009 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:96 | Decimal Separator | FACT | always | — | decimal_point (default '.') and thousands_sep (default ',') are free chars with trim disabled. | N-U26-002 |
| VDR-U26-C010 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:114 | _code_uniq = models.Constraint | FACT | always | — | SQL uniqueness on name, code and url_code (lines 110-121). | N-U26-005 |
| VDR-U26-C011 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:127 | At least one language must be active | FACT | registry ready | — | _check_active raises when no language record exists after the change; skipped while the registry is loading. | N-U26-005 |
| VDR-U26-C012 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:135 | Invalid date/time format directive | FACT | always | — | _check_format rejects date/time patterns containing any directive from DATETIME_FORMATS_MAP except %y. | N-U26-005 |
| VDR-U26-C013 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:143 | Using 24-hour clock format with AM/PM | FACT | form edit | — | _onchange_format replaces %H with %I when %p is also present and returns a notification. | N-U26-005 |
| VDR-U26-C014 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:159 | No language is active | FACT | registry load | — | _register_hook logs an error (no exception) when no language exists. | N-U26-005 |
| VDR-U26-C015 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:161 | def _activate_lang | FACT | always | — | _activate_lang only sets active=True; _activate_and_install_lang (line 171) calls action_unarchive, which also loads translations. | N-U26-004 |
| VDR-U26-C016 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:337 | Automatically load translation | FACT | always | — | action_unarchive on a language calls _update_translations(codes) on every installed module (lines 334-342). | N-U26-004 |
| VDR-U26-C017 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:195 | Unable to get information for locale | FACT | language created outside the catalogue | RT | _create_lang reads date/time format, separators and grouping from the host OS locale (setlocale/localeconv); if the locale is unavailable it warns and uses the default locale values. | N-U26-009 |
| VDR-U26-C018 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:248 | def install_lang | FACT | database creation | — | install_lang takes the first of config load_language or en_US, activates or creates it, sets ir.default for res.partner.lang when unset and writes lang on the main company partner when empty (lines 248-269). | N-U26-009 |
| VDR-U26-C019 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:264 | IrDefault.set('res.partner', 'lang' | FACT | no default stored | — | The database-wide default contact language is an ir.default row on res.partner.lang. | N-U26-009 |
| VDR-U26-C020 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:315 | @tools.ormcache('field', cache='stable') | FACT | always | — | _get_active_by caches active languages' CACHED_FIELDS (id, name, code, iso_code, url_code, active, direction, date_format, time_format, week_start, grouping, decimal_point, thousands_sep, flag_image_url) in the 'stable' cache. | N-U26-013 |
| VDR-U26-C021 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:294 | Dummy LangData | FACT | always | — | _get_data returns a dummy LangData with False values for inactive languages; LangDataDict.__getitem__ builds it for missing keys (lines 35-46). | N-U26-013 |
| VDR-U26-C022 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:311 | def get_installed | FACT | always | — | get_installed returns (code, name) pairs of active languages ordered by name; it is the selection source for partner, user, wizards and export. | N-U26-001 |
| VDR-U26-C023 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:346 | self.env.registry.clear_cache('stable') | FACT | create/write/unlink | — | create, write and unlink clear the 'stable' registry cache. | N-U26-013 |
| VDR-U26-C024 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:355 | Language code cannot be modified | FACT | always | — | write rejects any change of code. | N-U26-005 |
| VDR-U26-C025 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:358 | currently used by users | FACT | deactivation | — | Deactivation raises UserError if any active user uses the language; a third check (lines 361-362) covers archived users 'used by automated processes'. | N-U26-006 |
| VDR-U26-C026 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:360 | currently used by contacts | FACT | deactivation | — | Deactivation raises UserError if any active partner uses the language. | N-U26-006 |
| VDR-U26-C027 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:364 | discard_values | FACT | deactivation | — | Deactivation discards the ir.default value for res.partner.lang for those codes. | N-U26-006 |
| VDR-U26-C028 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:369 | shortest version | FACT | activation | — | When a regional language is activated its url_code is shortened to the bare language code if the short code is free and the other language inactive. | N-U26-004 |
| VDR-U26-C029 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:395 | can not be deleted | FACT | always | — | _unlink_except_default_lang forbids deleting en_US, the context language, and any active language. | N-U26-007 |
| VDR-U26-C030 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:400 | cannot delete the language which is Active | FACT | always | — | Active languages must be deactivated before deletion. | N-U26-007 |
| VDR-U26-C031 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:418 | def format(self, percent | FACT | always | — | res.lang.format applies the record's decimal_point, thousands_sep and grouping to a number format and raises UserError if the language is not installed (lines 418-429). | N-U26-013 |
| VDR-U26-C032 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:428 | is not installed | FACT | formatting with inactive language | — | Formatting with a language that is not active raises UserError 'The language %s is not installed.' | N-U26-013 |
| VDR-U26-C033 | FUNCTION MAPPING REQUIRED | base/data/res.lang.csv:2 | base.lang_en | FACT | always | — | Shipped English (US) row: date %m/%d/%Y, time %I:%M:%S %p, week_start 7, grouping [3,0], '.' and ','. | N-U26-003 |
| VDR-U26-C034 | FUNCTION MAPPING REQUIRED | base/data/res.lang.csv:87 | th_TH | FACT | always | — | Shipped Thai row: code th_TH, iso_code th, ltr, grouping [3,0], '.' and ',', date %d/%m/%Y, time %H:%M:%S, week_start 7; the language name literal is written in Thai script (data, see CAP-U26-07). | N-U26-003 |
| VDR-U26-C035 | FUNCTION MAPPING REQUIRED | base/data/res.lang.csv:1 | id","name","code" | OBSERVATION | restored DB | — | The file has 93 data rows; the DB res_lang table holds 93 rows, exactly 1 active (en_US), 89 ltr and 4 rtl; th_TH is inactive with the CSV values unchanged. | N-U26-003 |
| VDR-U26-C036 | FUNCTION MAPPING REQUIRED | base/data/res_lang_data.xml:11 | name="install_lang" | FACT | module base init | — | Base data calls res.lang.install_lang inside a noupdate block. | N-U26-009 |
| VDR-U26-C037 | FUNCTION MAPPING REQUIRED | base/wizard/base_language_install.py:35 | def lang_install | FACT | always | — | lang_install sets lang_ids active, then _update_translations(codes, overwrite) over all installed modules. | N-U26-004 |
| VDR-U26-C038 | FUNCTION MAPPING REQUIRED | base/wizard/base_language_install.py:23 | Overwrite Existing Terms | FACT | always | — | Wizard flag overwrite defaults to True and help states customised translations are overwritten by official ones. | N-U26-004 |
| VDR-U26-C039 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:136 | access_base_language_install | FACT | always | — | base.language.install is restricted to base.group_system (read/write/create). | N-U26-012 |
| VDR-U26-C040 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:72 | access_res_lang_group_system | FACT | always | — | res.lang: public, portal and internal read only; group_system full CRUD (lines 69-72). | N-U26-012 |
| VDR-U26-C041 | FUNCTION MAPPING REQUIRED | base/views/base_menus.xml:13 | id="menu_translation" | FACT | always | — | Translations menu (with Import/Export and Application Terms) is limited to base.group_no_one (debug mode). | N-U26-012 |
| VDR-U26-C042 | FUNCTION MAPPING REQUIRED | base_setup/views/res_config_settings_views.xml:34 | id="languages" | FACT | base_setup installed | — | General settings has a Languages block with a language count, Add Languages and Manage Languages buttons. | N-U26-012 |
| VDR-U26-C043 | FUNCTION MAPPING REQUIRED | website/models/res_lang.py:15 | currently used on a website | FACT | website installed | — | Deactivation is blocked when any website lists the language. | N-U26-006 |
| VDR-U26-C044 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:221 | All the emails and documents sent | FACT | always | — | res.partner.lang is a stored computed selection of installed languages, readonly=False; help: all emails and documents sent to this contact are translated in this language. | N-U26-011 |
| VDR-U26-C045 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:403 | partner.parent_id.lang or | FACT | always | — | _compute_lang: child contact uses parent lang, else default_get lang, else env.lang; a contact without lang takes default_get lang or env.lang (lines 398-405). | N-U26-011 |
| VDR-U26-C046 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:707 | context > request > company | FACT | always | — | context_get resolves lang: user.lang if active, else request.best_lang, else company partner lang, else DEFAULT_LANG, else the first active language (lines 706-718). | N-U26-010 |
| VDR-U26-C047 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:193 | 'lang', 'tz', 'api_key_ids' | FACT | always | — | lang is in the users' self-writeable preference fields. | N-U26-010 |
| VDR-U26-C048 | FUNCTION MAPPING REQUIRED | base/models/ir_http.py:320 | request.update_context(lang=get_lang(env).code) | FACT | every dispatched request | — | pre_dispatch re-validates the request context language through get_lang (falls back to company language, English or the first installed). | N-U26-010 |
| VDR-U26-C049 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:285 | def _get_data | OBSERVATION | restored DB | — | DB: ir_default res.partner.lang = en_US; all 7 partners and the 4 users' partners have lang en_US; no ir_rule rows exist for res.lang or the language wizards. | N-U26-009 |
| VDR-U26-C050 | FUNCTION MAPPING REQUIRED | website/models/website.py:126 | website_lang_rel | OBSERVATION | restored DB | — | DB: website has 29 rows, each with only en_US in website_lang_rel and en_US as default_lang_id, auto_redirect_lang true. | N-U26-009 |
| VDR-U26-C051 | FUNCTION MAPPING REQUIRED | web/static/src/core/l10n/translation.js:171 | translatedTerms[this.context] | FACT | always | — | Client _t resolves translatedTerms[module][source] then translatedTermsGlobal[source] then source; the module context is injected by the transpiler. | N-U26-019 |
| VDR-U26-C052 | FUNCTION MAPPING REQUIRED | web/static/src/core/l10n/translation.js:95 | export function _t(source | FACT | always | — | Client _t(source, ...substitutions) has no plural/context parameter. | N-U26-022 |
| VDR-U26-C053 | FUNCTION MAPPING REQUIRED | web/static/src/core/l10n/translation.js:34 | function translationSprintf | FACT | always | — | Client substitutions follow the same rules: iterables formatted as lists, markup escapes non-markup content. | N-U26-021 |
| VDR-U26-C054 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:39 | def get_python_translation | FACT | chart template load | — | get_python_translation(module, lang, value) looks up code translations for the exact language, then for lang.split('_')[0]. | N-U26-025 |
| VDR-U26-C055 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1457 | def _get_field_translation | FACT | chart template load | — | _get_field_translation(record, fname, lang) prefers explicit fname@lang then fname@generic in the template data, else the code translation of record[fname] from the module that defined the template function. | N-U26-025 |
| VDR-U26-C056 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:196 | code translation we load | FACT | chart template load | — | A chart template is loaded with context lang='en_US'; code translations are applied afterwards by _load_translations. | N-U26-025 |
| VDR-U26-C057 | FUNCTION MAPPING REQUIRED | l10n_th/i18n/th.po:19 | Plural-Forms | OBSERVATION | shipped file | — | The shipped Thai file declares nplurals=1; plural=0 and contains no msgid_plural entries (0 msgid_plural in any module .pot). | N-U26-022 |
| VDR-U26-C058 | FUNCTION MAPPING REQUIRED | l10n_th/i18n/th.po:23 | #: model:ir.model,name | OBSERVATION | shipped file | — | Entries carry source references ('#: model:...', 'code:...', 'model_terms:...') and msgid is the English text; no entry has a symbolic key or msgctxt (0 msgctxt in any module .pot or th.po). | N-U26-016 |
| VDR-U26-C059 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:80 | name = fields.Char(string='Tax Name' | FACT | always | — | account.tax.name translate=True (line 80); invoice_label translate=True (135); description html_translate (134); invoice_legal_notes translate=True (211). | N-U26-034 |
| VDR-U26-C060 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:32 | name = fields.Char(required=True, translate=True) | FACT | always | — | account.tax.group.name translate=True (line 32); preceding_subtotal translate=True (61). | N-U26-034 |
| VDR-U26-C061 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:33 | name = fields.Char(string="Account Name" | FACT | always | — | account.account.name and description are translatable (lines 33-34); account.account.tag.name (1522). | N-U26-034 |
| VDR-U26-C062 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:95 | name = fields.Char(string='Journal Name' | FACT | always | — | account.journal.name translate=True (95); account.journal.group name translate=True (22); journal code is a plain field. | N-U26-034 |
| VDR-U26-C063 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:23 | name = fields.Char(string='Payment Terms' | FACT | always | — | account.payment.term.name and note (Html) translate=True (lines 23, 25). | N-U26-034 |
| VDR-U26-C064 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:51 | name = fields.Char(string="Name", required=True, translate=True) | FACT | always | — | account.report name (line 51), account.report.column name (354) and account.report.line name (937) translate=True: financial and tax report titles are translatable data. | N-U26-034 |
| VDR-U26-C065 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:44 | name = fields.Char('Name', index='trigram' | FACT | always | — | product.template.name translate=True with trigram index (line 44); description, description_purchase, description_sale translate=True (47-51); stock adds description_picking/out/in (stock/models/product.py:870-872). | N-U26-034 |
| VDR-U26-C066 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:34 | name = fields.Char('Unit Name' | FACT | always | — | uom.uom.name translate=True (line 34). | N-U26-034 |
| VDR-U26-C067 | FUNCTION MAPPING REQUIRED | stock/models/stock_location.py:523 | name = fields.Char('Route', required=True, translate=True) | FACT | always | — | stock.route.name translate=True (523); stock.picking.type.name translate=True (stock/models/stock_picking.py:27); stock.rule name (stock_rule.py:58). | N-U26-034 |
| VDR-U26-C068 | FUNCTION MAPPING REQUIRED | stock/models/stock_warehouse.py:35 | name = fields.Char('Warehouse', required=True | FACT | always | — | stock.warehouse.name has no translate; stock.location.name (stock_location.py:29) and product.category.name (product/models/product_category.py:17) also have no translate. | N-U26-034 |
| VDR-U26-C069 | FUNCTION MAPPING REQUIRED | base/models/res_country.py:205 | name = fields.Char(string='State Name', required=True, | FACT | always | — | res.country.state.name has no translate (single stored value); res.country.name (line 38) and vat_label (75) translate=True. | N-U26-034 |
| VDR-U26-C070 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:58 | report_header = fields.Html | FACT | always | — | res.company report_header, report_footer, company_details translate=True (58-60); invoice terms html fields translate via account. | N-U26-034 |
| VDR-U26-C071 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:45 | currency_unit_label = fields.Char | FACT | always | — | res.currency.currency_unit_label and currency_subunit_label translate=True (45-46); they feed the amount-in-words text. | N-U26-034 |
| VDR-U26-C072 | FUNCTION MAPPING REQUIRED | base/models/ir_ui_view.py:162 | arch_db = fields.Text(string='Arch Blob' | FACT | always | — | ir.ui.view.arch_db translate=xml_translate: screen and report-template text is term-translated data; ir.ui.menu.name (ir_ui_menu.py:23) and ir.actions.* name (ir_actions.py:67) translate=True. | N-U26-034 |
| VDR-U26-C073 | FUNCTION MAPPING REQUIRED | base/models/ir_actions_report.py:186 | print_report_name = fields.Char | FACT | always | — | ir.actions.report.name and print_report_name (the PDF file name expression) are translatable (line 186). | N-U26-034 |
| VDR-U26-C074 | FUNCTION MAPPING REQUIRED | mail/models/mail_template.py:51 | subject = fields.Char('Subject', translate=True | FACT | always | — | mail.template name (39), description (41), subject (51) and body_html (71) are translatable; the language of a render is chosen per recipient (CAP-U26-05). | N-U26-034 |
| VDR-U26-C075 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:123 | compute='_compute_name' | FACT | always | — | sale.order.line.name is a stored computed Text without translate; _compute_name builds it in the order's partner language (lines 405-415). | N-U26-035 |
| VDR-U26-C076 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:111 | string='Label' | FACT | always | — | account.move.line.name (Label) is a stored computed Char without translate. | N-U26-035 |
| VDR-U26-C077 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:515 | def _compute_translated_product_name | FACT | always | — | translated_product_name recomputes the product display_name in the order language on the line. | N-U26-035 |
| VDR-U26-C078 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:617 | def _get_product_purchase_description | FACT | always | — | Purchase line description is built from the product with context lang = get_lang(partner.lang) (lines 402-407) and stored in a plain field. | N-U26-035 |
| VDR-U26-C079 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:2285 | def _get_lang | INFERENCE | always | — | sale, purchase, l10n_th and stock_account declare no translate=True fields of their own (DB: 0 translatable fields attributed to sale, purchase, l10n_th, sale_stock, purchase_stock, stock_account); sale.order.template (sale_management) is the only sales-side translatable model. | N-U26-034 |
| VDR-U26-C080 | FUNCTION MAPPING REQUIRED | sale_management/models/sale_order_template.py:19 | Terms and conditions | FACT | sale_management installed | — | sale.order.template.note is html_translate and sale.order.template.line.name translate=True. | N-U26-034 |
| VDR-U26-C081 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:23 | TEMPLATE_MODELS = ( | FACT | always | — | Chart template records are created for account.group, account.account, account.fiscal.position, account.tax.group, account.tax, account.journal, account.reconcile.model. | N-U26-036 |
| VDR-U26-C082 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1480 | def _load_translations | FACT | chart load / language install | — | _load_translations gathers fname@lang values from the template data into a TranslationImporter keyed by model/field/xmlid/lang and saves with overwrite=False; then fills missing translations from code translations (lines 1480-1539). | N-U26-036 |
| VDR-U26-C083 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1367 | def _get_untranslatable_fields_to_translate | FACT | chart load | — | account.journal.code is translated at load even though not translatable, into company.partner_id.lang or get_lang code (lines 1359-1378). | N-U26-036 |
| VDR-U26-C084 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:90 | env['account.chart.template']._load_translations(langs=langs) | FACT | language install with account installed | — | account overrides _load_module_terms: after loading po files it reloads chart template translations and tax tag translations for the langs (immediately, or delayed until registry ready). | N-U26-036 |
| VDR-U26-C085 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:551 | Translate HTML terms | OBSERVATION | restored DB | — | DB: ir_model_fields has 357 stored translatable fields (295 whole-value, 59 html term, 3 xml term) over 179 models; counted values per sample: product.template.name 16, account.account.name 147, account.tax.name 18, account.journal.name 7, account.payment.term.name 10, ir_ui_menu.name 729, ir_ui_view.arch_db 7113; none has a key other than en_US. | N-U26-037 |
| VDR-U26-C086 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:880 | def _update_translations | OBSERVATION | source tree count | — | Mechanical count over odoo/addons: 692 manifests, 607 modules with i18n/, 606 .pot files, 406 modules with i18n/th.po, 0 th_TH.po, 0 i18n_extra Thai files (only account_edi_proxy_client has i18n_extra). | N-U26-041 |
| VDR-U26-C087 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:887 | update_mods = self.filtered | OBSERVATION | restored DB | — | DB: 356 installed modules; 310 have th.po; the 46 without are: account_payment_interco, api_doc, mail_bot_hr, mrp_subcontracting_repair, project_mrp_sale, rpc, sale_mrp_margin, sale_sms, website_google_map, theme_default, theme_test_custo and 35 test_* modules; 96 further th.po exist in uninstalled modules. | N-U26-042 |
| VDR-U26-C088 | FUNCTION MAPPING REQUIRED | l10n_th/i18n/th.po:24 | msgid "Account Chart Template" | OBSERVATION | source tree count | — | th.po totals over 406 files: 64,199 entries, 52,873 translated; per module (entries/translated): base 6569/5608, account 3171/2684, sale 862/773, purchase 587/499, stock 1809/1565, product 749/603, mail 2090/1681, web 4375/4143, website 3084/2325, l10n_th 23/23. In the same files: 28,430 'model', 19,663 'code', 19,485 'model_terms' references. | N-U26-042 |
| VDR-U26-C089 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:880 | def _update_translations | FACT | always | — | _update_translations(filter_lang, overwrite) defaults to all installed languages, filters modules in states installed/to install/to upgrade, topologically sorts them by dependencies and calls _load_module_terms(mod_names, langs, overwrite) (lines 880-893). | N-U26-043 |
| VDR-U26-C090 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:974 | Load PO files of the given modules | FACT | always | — | _load_module_terms loads, per module and language, every get_po_paths file, then every manifest data/demo .xml/.csv with module= (embedded @lang columns), logs 'no translation for language' if none, then translation_importer.save(overwrite). | N-U26-043 |
| VDR-U26-C091 | FUNCTION MAPPING REQUIRED | base/models/ir_module.py:990 | translation_importer.save(overwrite=overwrite) | FACT | always | — | A single TranslationImporter is shared by all modules and languages and saved once at the end. | N-U26-043 |
| VDR-U26-C092 | FUNCTION MAPPING REQUIRED | base/wizard/base_export_language.py:38 | def act_getfile | FACT | always | — | Export wizard: formats csv/po/tgz (default po), export_type module or model (domain via ast.literal_eval), lang '__new__' exports a template (.pot); file name derives from iso code or module or model. | N-U26-046 |
| VDR-U26-C093 | FUNCTION MAPPING REQUIRED | base/wizard/base_import_language.py:30 | def import_lang | FACT | always | — | Import wizard activates or creates the language, loads .po/.csv via TranslationImporter and saves with the overwrite flag (default True). | N-U26-044 |
| VDR-U26-C094 | FUNCTION MAPPING REQUIRED | base/wizard/base_import_language.py:45 | not imported due to format mismatch | FACT | always | — | Any exception while reading the file becomes a UserError with file name and technical details (valid formats .csv, .po). | N-U26-048 |
| VDR-U26-C095 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:137 | access_base_language_import | FACT | always | — | base.language.import is group_system only. | N-U26-047 |
| VDR-U26-C096 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:140 | access_base_language_export | FACT | always | — | base.language.export is granted to base.group_user (all internal users); read/write/create. | N-U26-047 |
| VDR-U26-C097 | FUNCTION MAPPING REQUIRED | website/models/ir_module_module.py:495 | Add missing website specific translation | FACT | website installed | — | website._load_module_terms copies translations of generic QWeb views to website-specific copies with the same key. | N-U26-049 |
| VDR-U26-C098 | FUNCTION MAPPING REQUIRED | website_sale/models/ir_module_module.py:12 | Add missing website_sale-specific translations | FACT | website_sale installed | — | website_sale._load_module_terms copies checkout-step translations with jsonb merges, honoring overwrite. | N-U26-049 |
| VDR-U26-C099 | FUNCTION MAPPING REQUIRED | base_import_module/models/ir_module.py:66 | Translations for imported data modules only works | FACT | base_import_module installed | — | Imported (non-filesystem) modules load translations only from attached po files named <module>_<lang>.po. | N-U26-049 |
| VDR-U26-C100 | FUNCTION MAPPING REQUIRED | transifex/data/transifex_data.xml:13 | model.reload() | FACT | transifex installed | — | Cron 'Transifex: Reload code translations' runs model.reload() every 7 days; reload deletes all rows of transifex.code.translation and reloads code translations of installed modules for installed non-English languages. | N-U26-047 |
| VDR-U26-C101 | FUNCTION MAPPING REQUIRED | transifex/security/ir.model.access.csv:2 | access_transifex_code_translation | FACT | always | — | transifex.code.translation is readable by group_system only. | N-U26-047 |
| VDR-U26-C102 | FUNCTION MAPPING REQUIRED | transifex/models/transifex_code_translation.py:69 | def reload | OBSERVATION | restored DB | — | DB: transifex is installed; cron exists, active, every 7 days; table transifex_code_translation has 0 rows; res_lang has one active language; base.language.import/install need system, export user. | N-U26-050 |
| VDR-U26-C103 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:86 | def _load_module_terms | FACT | account installed | — | account._load_module_terms: after the base loading, if 'account' is among the modules, chart template translations and tax tag translations are reloaded; delayed until registry load when loading. | N-U26-049 |
| VDR-U26-C104 | FUNCTION MAPPING REQUIRED | web/controllers/webclient.py:19 | def bootstrap_translations | FACT | login page | — | Login page translations are read from <module>/i18n/<generic lang>.po for bootstrap modules, using only the main language of the request. | N-U26-043 |
| VDR-U26-C105 | FUNCTION MAPPING REQUIRED | web/controllers/webclient.py:47 | def translations(self | FACT | always | — | /web/webclient/translations returns client terms for the requested active language and modules, with a hash for cache validation; an inactive language is replaced by None (default). | N-U26-043 |
| VDR-U26-C106 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:221 | All the emails and documents sent | FACT | always | — | res.partner.lang help text: all emails and documents sent to this contact are translated in this language. | N-U26-054 |
| VDR-U26-C107 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:35 | def _lang_get | FACT | always | — | The lang selection is res.lang.get_installed(), i.e. active languages only. | N-U26-112 |
| VDR-U26-C108 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:159 | inherits from res.partner | FACT | always | — | res.users inherits res.partner: user language is the contact's language field. | N-U26-053 |
| VDR-U26-C109 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:707 | context > request > company | FACT | always | — | context_get: stored lang if active, else request.best_lang, else company partner lang, else DEFAULT_LANG, else first installed. | N-U26-053 |
| VDR-U26-C110 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:2285 | def _get_lang | FACT | always | — | sale.order._get_lang returns partner_id.lang unless the partner is public, else env.lang. | N-U26-055 |
| VDR-U26-C111 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:410 | lang = line.order_id._get_lang() | FACT | always | — | sale.order.line._compute_name renders the product description with context lang = order lang and stores it in the plain name field. | N-U26-055 |
| VDR-U26-C112 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:518 | lang=line.order_id._get_lang() | FACT | always | — | translated_product_name = product.display_name in the order language (computed, not stored). | N-U26-055 |
| VDR-U26-C113 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:403 | lang=get_lang(self.env, self.partner_id.lang).code | FACT | always | — | Purchase line description uses get_lang(env, partner.lang) i.e. the vendor's language if active. | N-U26-055 |
| VDR-U26-C114 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:556 | product = line.product_id.with_context(lang=line.move_id.partner_id.lang) | FACT | always | — | Invoice line label computed with product in move partner lang, else line partner lang. | N-U26-055 |
| VDR-U26-C115 | FUNCTION MAPPING REQUIRED | stock/models/stock_move.py:2447 | def _get_lang | FACT | always | — | stock.move._get_lang = picking partner lang, else move partner lang, else current user lang; used for move descriptions (lines 810-816, 1836). | N-U26-055 |
| VDR-U26-C116 | FUNCTION MAPPING REQUIRED | mail/models/mail_render_mixin.py:57 | Optional translation language (ISO code) | FACT | always | — | mail.render.mixin.lang (inherited by mail.template) is a Char expression (e.g. {{ object.partner_id.lang }}); if not set the main partner's language is used. | N-U26-056 |
| VDR-U26-C117 | FUNCTION MAPPING REQUIRED | mail/models/mail_render_mixin.py:721 | def _render_lang | FACT | always | — | _render_lang: if template.lang is set render it per record, else take the first customer partner's lang from _mail_get_partners. | N-U26-056 |
| VDR-U26-C118 | FUNCTION MAPPING REQUIRED | mail/models/mail_render_mixin.py:750 | def _classify_per_lang | FACT | always | — | _classify_per_lang groups records by language (or template_preview_lang) and returns the template with that lang in context for each group. | N-U26-056 |
| VDR-U26-C119 | FUNCTION MAPPING REQUIRED | mail/models/mail_render_mixin.py:763 | template_preview_lang | FACT | preview | — | A context key template_preview_lang overrides the language for all records. | N-U26-056 |
| VDR-U26-C120 | FUNCTION MAPPING REQUIRED | mail/models/mail_render_mixin.py:113 | def _update_field_translations | FACT | always | — | mail.render.mixin._update_field_translations (inherited by mail.template) re-checks dynamic-template access for every language written. | N-U26-056 |
| VDR-U26-C121 | FUNCTION MAPPING REQUIRED | account/models/account_move_send.py:170 | def _get_default_mail_lang | FACT | always | — | Invoice send default mail_lang = template._render_lang([move.id])[move.id]. | N-U26-057 |
| VDR-U26-C122 | FUNCTION MAPPING REQUIRED | account/wizard/account_move_send_wizard.py:207 | def _compute_lang | FACT | send wizard | — | Send wizard lang is computed from the template (or get_lang(env).code when no template) and drives recomputation of partners, subject and body (lines 207-235). | N-U26-057 |
| VDR-U26-C123 | FUNCTION MAPPING REQUIRED | account/models/account_move_send.py:683 | model_description = move.with_context(lang=mail_lang).type_name | FACT | always | — | The email model description is translated into the chosen mail language. | N-U26-057 |
| VDR-U26-C124 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:582 | lang = template._render_lang([ctx['default_res_id']])[ctx['default_res_id']] | FACT | always | — | Purchase order composer language: template language when set, else context language; applied by with_context(lang=lang). | N-U26-057 |
| VDR-U26-C125 | FUNCTION MAPPING REQUIRED | http_routing/models/ir_http.py:309 | frontend_lang | FACT | http_routing installed | — | Requested language order: URL, cookie frontend_lang, context, default; the request language is stored in the frontend_lang cookie (lines 361-364, 404-410, 517-518). | N-U26-058 |
| VDR-U26-C126 | FUNCTION MAPPING REQUIRED | http_routing/models/ir_http.py:259 | def _get_default_lang | FACT | http_routing installed | — | Default frontend language = ir.default res.partner.lang, else the first active language; website overrides it with the website default_lang_id. | N-U26-058 |
| VDR-U26-C127 | FUNCTION MAPPING REQUIRED | http_routing/models/ir_http.py:302 | def get_nearest_lang | FACT | http_routing installed | — | get_nearest_lang maps a code to a frontend language, trying exact code then any language with the same prefix. | N-U26-058 |
| VDR-U26-C128 | FUNCTION MAPPING REQUIRED | website/models/website.py:125 | language_ids = fields.Many2many | FACT | website installed | — | website.language_ids (default all active languages), default_lang_id (default = ir.default or first active), auto_redirect_lang default True. | N-U26-058 |
| VDR-U26-C129 | FUNCTION MAPPING REQUIRED | website/models/res_lang.py:19 | def _get_frontend | FACT | website installed | — | Frontend languages come from the current website's language_ids and get an hreflang (short code shortened once per language group). | N-U26-058 |
| VDR-U26-C130 | FUNCTION MAPPING REQUIRED | website/models/ir_http.py:313 | path = '/' + request.lang.url_code + path | FACT | website installed | — | Non-default languages are prefixed with url_code in website URLs. | N-U26-058 |
| VDR-U26-C131 | FUNCTION MAPPING REQUIRED | auth_signup/models/res_users.py:204 | user_lang = user.lang or self.env.lang or 'en_US' | FACT | auth_signup installed | — | Password reset / invitation email is rendered in the user's language with subject translated in that language. | N-U26-058 |
| VDR-U26-C132 | FUNCTION MAPPING REQUIRED | portal/controllers/portal.py:801 | address_values['lang'] = request.lang.code | FACT | portal installed | — | A portal-created address gets the request language. | N-U26-058 |
| VDR-U26-C133 | FUNCTION MAPPING REQUIRED | website/models/website.py:111 | def _default_language | OBSERVATION | restored DB | — | DB: 29 website rows, each with only en_US; res_lang active count 1; partners/users all en_US. | N-U26-060 |
| VDR-U26-C134 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:418 | def format(self, percent | FACT | always | — | Number formatting applies lang.decimal_point, thousands_sep and grouping via intersperse; grouping literal parsed with ast.literal_eval. | N-U26-064 |
| VDR-U26-C135 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:503 | def intersperse | FACT | always | — | intersperse inserts the separator according to the grouping counts (0 repeats the last count). | N-U26-064 |
| VDR-U26-C136 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:42 | position = fields.Selection | FACT | always | — | res.currency.position is 'after' (default) or 'before'. | N-U26-114 |
| VDR-U26-C137 | FUNCTION MAPPING REQUIRED | web/static/src/core/l10n/localization_service.js:87 | weekStart: userLocalization.week_start | FACT | web client | — | The web client builds dateFormat/timeFormat from the language record (strftimeToLuxonFormat), decimalPoint, thousandsSep, grouping, direction and weekStart. | N-U26-065 |
| VDR-U26-C138 | FUNCTION MAPPING REQUIRED | web/static/src/core/l10n/localization_service.js:110 | Settings.defaultNumberingSystem = numberingSystem | FACT | web client | RT | Luxon default locale is the user's language; the numbering system is 'latn' except for ar-sa/ar-sy/ar-001, bn, bo, pa-in, ta; there is no calendar override, so any Buddhist-year rendering by Intl for Thai in localized (non-token) outputs is runtime behaviour. | N-U26-074 |
| VDR-U26-C139 | FUNCTION MAPPING REQUIRED | web/static/src/core/l10n/dates.js:543 | numberingSystem: "latn" | FACT | web client | — | Dates sent to the server are serialized with the Latin numbering system. | N-U26-065 |
| VDR-U26-C140 | FUNCTION MAPPING REQUIRED | base/models/ir_qweb.py:2810 | == 'rtl' | FACT | always | — | Asset bundles are generated as RTL when the environment language's direction is rtl. | N-U26-065 |
| VDR-U26-C141 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:175 | def amount_to_text | FACT | always | — | amount_to_text builds words with num2words(number, lang=<res.lang iso_code of get_lang(env)>) .title(), falling back to English on NotImplementedError; returns '' with a warning if num2words is not importable; result is composed through env._ with currency_unit_label/subunit labels. | N-U26-066 |
| VDR-U26-C142 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:184 | The library 'num2words' is missing | FACT | num2words missing | RT | num2words import is optional (try/except, num2words = None). | N-U26-067 |
| VDR-U26-C143 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:14 | from num2words import num2words | FACT | always | — | The dependency is imported at module top; requirements.txt pins num2words 0.5.10/0.5.13 (not in the source tree). | N-U26-066 |
| VDR-U26-C144 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2218 | def _compute_amount_total_words | FACT | always | — | account.move.amount_total_words = currency.amount_to_text(amount_total) with commas removed. | N-U26-066 |
| VDR-U26-C145 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:410 | display_invoice_amount_total_words | FACT | company option on | — | The invoice report prints amount_total_words only when company.display_invoice_amount_total_words is set. | N-U26-067 |
| VDR-U26-C146 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:102 | pay.check_amount_in_words = pay.currency_id.amount_to_text | FACT | account_check_printing installed | — | Printed cheque words use the same amount_to_text. | N-U26-066 |
| VDR-U26-C147 | FUNCTION MAPPING REQUIRED | l10n_th/models/account_move.py:7 | def _get_name_invoice_report | INFERENCE | l10n_th installed | — | l10n_th models contain only: account_move._get_name_invoice_report, ir_actions_report._pre_render_qweb_pdf, res_bank proxy checks, res_partner.l10n_th_branch_name and the chart template; a grep for amount_to_text/num2words/baht across l10n_th finds none, and the only num2words users in Community are base res_currency, l10n_gcc_invoice and l10n_tr_nilvera_einvoice. | N-U26-067 |
| VDR-U26-C148 | FUNCTION MAPPING REQUIRED | base/data/res_currency_data.xml:1499 | <field name="currency_unit_label">Baht | FACT | always | — | THB: full_name 'Thai baht', symbol is U+0E3F, rounding 0.01, active False, unit label 'Baht', subunit label 'Satang' (English source literals). | N-U26-072 |
| VDR-U26-C149 | FUNCTION MAPPING REQUIRED | base/data/res_currency_data.xml:1492 | id="THB" | OBSERVATION | restored DB | — | DB: THB active, position after, rounding 0.01, unit label Baht; company chart template th, fiscal country set, display_invoice_amount_total_words = true. | N-U26-072 |
| VDR-U26-C150 | FUNCTION MAPPING REQUIRED | account/models/company.py:152 | display_invoice_amount_total_words | FACT | always | — | company.display_invoice_amount_total_words is a Boolean (default False). | N-U26-114 |
| VDR-U26-C151 | FUNCTION MAPPING REQUIRED | base/models/res_country.py:44 | address_format = fields.Text | FACT | always | — | res.country.address_format default '%(street)s\n%(street2)s\n%(city)s %(state_code)s %(zip)s\n%(country_name)s' with state_name/state_code/country_name/country_code available. | N-U26-068 |
| VDR-U26-C152 | FUNCTION MAPPING REQUIRED | base/models/res_country.py:70 | name_position = fields.Selection | FACT | always | — | name_position before/after address; state_required default False, zip_required default True (lines 70-78). | N-U26-114 |
| VDR-U26-C153 | FUNCTION MAPPING REQUIRED | base/models/res_country.py:75 | vat_label = fields.Char | FACT | always | — | vat_label translate=True, prefetch=True. | N-U26-068 |
| VDR-U26-C154 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:1177 | def _prepare_display_address | FACT | always | — | _prepare_display_address takes the country's format, injects state/country names and codes plus formatting address fields, prefixing the company name when present. | N-U26-068 |
| VDR-U26-C155 | FUNCTION MAPPING REQUIRED | base/models/res_country.py:44 | address_format = fields.Text | OBSERVATION | restored DB | — | DB: country TH address_format is street / street2 / city / state_name+zip / country_name on separate lines, name_position before, state_required false, zip_required true, no vat_label; 39 countries differ from the US layout. | N-U26-068 |
| VDR-U26-C156 | FUNCTION MAPPING REQUIRED | base/data/res.country.state.csv:1471 | state_th_001 | FACT | always | — | 77 rows with id state_th_001.. and country base.th; the name column of all 77 is Thai script (non-translatable field); codes TH-xx. | N-U26-069 |
| VDR-U26-C157 | FUNCTION MAPPING REQUIRED | base/models/res_country.py:198 | class ResCountryState | OBSERVATION | restored DB | — | DB: res_country_state 2131 rows total, 77 for TH. | N-U26-069 |
| VDR-U26-C158 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:33 | index='trigram' | OBSERVATION | restored DB | — | DB collation en_US.UTF-8 (datcollate, datctype), encoding UTF8, extensions pg_trgm and plpgsql only (no unaccent). | N-U26-070 |
| VDR-U26-C159 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_partner.py:18 | Headquarter | FACT | l10n_th installed | — | l10n_th_branch_name: for Thai companies returns env._('Branch %(code)s', code) or env._('Headquarter'); computed in the env language of the partner record. | N-U26-071 |
| VDR-U26-C160 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:5 | l10n_th_branch_name | FACT | l10n_th installed | — | The Thai invoice document inserts the branch label after the partner VAT in the three address layouts. | N-U26-071 |
| VDR-U26-C161 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:15 | Tax Invoice | FACT | l10n_th installed | — | The Thai invoice document replaces the invoice title with the English source sentence 'Tax Invoice' inside the view arch. | N-U26-071 |
| VDR-U26-C162 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_partner.py:17 | partner.env._( | INFERENCE | mechanical scan | — | Scan (excl. tests, i18n, static) of gettext calls (_(, _lt(, env._() per module: l10n_th 8, account 688, sale 104, purchase 64, stock 278, product 110, uom 4, analytic 14; raise Exception( counts 4, 278, 31, 18, 105, 46, 2, 9; raise with a bare literal first argument: 0 real (3 false positives joining lists: account/models/account_move_send.py:328, stock/models/stock_move.py:483, stock/models/stock_rule.py:472). | N-U26-077 |
| VDR-U26-C163 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:111 | string='Label' | INFERENCE | mechanical scan | — | Scan of Python field string=/help= literals: l10n_th 0, account 905, sale 224, purchase 104, stock 290, product 158, uom 2, analytic 34; of fields.* definitions: 2, 1160, 271, 183, 719, 245, 9, 56. | N-U26-078 |
| VDR-U26-C164 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:23 | Tax ID | INFERENCE | mechanical scan | — | Scan of XML string=" attributes: l10n_th 0, account 633, sale 162, purchase 160, stock 495, product 166, uom 5, analytic 25; placeholder/help attrs 0, 124, 44, 22, 93, 23, 1, 5; <field name="name"> seeded names 33, 335, 141, 81, 301, 255, 36, 53; report templates carry English literal text such as 'Tax ID'. | N-U26-078 |
| VDR-U26-C165 | FUNCTION MAPPING REQUIRED | l10n_th/i18n/th.po:15 | Language: th | OBSERVATION | source tree count | — | th.po entries (total/translated/model/code/model_terms): l10n_th 23/23/14/8/1; account 3171/2684/1793/730/938; sale 862/773/448/127/349; purchase 587/499/296/92/246; stock 1809/1565/976/341/690; product 749/603/490/138/176; uom 63/52/51/7/7; analytic 162/155/111/32/33. | N-U26-079 |
| VDR-U26-C166 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:10 | def _get_th_template_data | INFERENCE | mechanical scan | — | Unicode scan U+0E00-U+0E7F over odoo/: no .py file outside tests has Thai characters; the only .py hit is addons/test_mail/tests/test_mail_gateway.py (2 lines); l10n_th Python files contain only English strings and xml ids. | N-U26-080 |
| VDR-U26-C167 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:1 | name@th_TH | FACT | chart load | — | Header has name@th_TH and description@th_TH columns; 144 data rows, all 144 carry Thai in both columns; the base name and description columns are English. | N-U26-081 |
| VDR-U26-C168 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:1 | description@th_TH | FACT | chart load | — | 72 tax rows, only description@th_TH has Thai (18 rows); name and invoice_label are English only. | N-U26-081 |
| VDR-U26-C169 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax.group-th.csv:1 | name@th_TH | FACT | chart load | — | 6 lines, 5 tax group rows with Thai in name@th_TH. | N-U26-081 |
| VDR-U26-C170 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.asset-th.csv:1 | name@th_TH | FACT | account.asset model present | — | 12 rows with Thai in name@th_TH for account.asset records (model not defined in Community accounting; file inert unless an asset module exists). | N-U26-081 |
| VDR-U26-C171 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:5 | name@th | FACT | module install | — | 30 <field name='name@th'> values with Thai script next to 30 English name fields in 54 records; loaded through the data-file translation reader because the file is in the manifest data list (l10n_th/__manifest__.py:22). | N-U26-081 |
| VDR-U26-C172 | FUNCTION MAPPING REQUIRED | l10n_th/demo/demo_company.xml:7 | name="city" | FACT | demo data | — | Demo company record sets city to a Thai literal (1 line); demo is not loaded in the studied DB. | N-U26-117 |
| VDR-U26-C173 | FUNCTION MAPPING REQUIRED | base/data/res.country.state.csv:1471 | state_th_001 | FACT | always | — | 77 Thai province rows carry the Thai name as the sole value in a non-translatable field (also counted in CAP-U26-06). | N-U26-081 |
| VDR-U26-C174 | FUNCTION MAPPING REQUIRED | base/data/res.lang.csv:87 | th_TH | FACT | always | — | Language names use the form 'English / native script': 65 of the 93 rows have non-ASCII names; the Thai row's name contains Thai script. | N-U26-081 |
| VDR-U26-C175 | FUNCTION MAPPING REQUIRED | base/data/res_currency_data.xml:1496 | <field name="symbol"> | FACT | always | — | THB symbol is the single character U+0E3F. | N-U26-081 |
| VDR-U26-C176 | FUNCTION MAPPING REQUIRED | l10n_kh/data/template/account.account-kh.csv:21 | VAT Input | FACT | l10n_kh installed | — | Line 21 of the Cambodian chart file contains a single character from the Thai Unicode block inside Khmer text in its name@km_KH column (likely a stray character; module not installed in the studied DB). | N-U26-081 |
| VDR-U26-C177 | FUNCTION MAPPING REQUIRED | web/static/src/core/l10n/time.js:9 | // Thai | FACT | always | — | web src time.js lists the language self-name 'Thai' in script (1 line); also web/static/lib/fullcalendar locales-all.global.js (14 lines), pdfjs viewer.js (1) and pdfjs locale/th/viewer.ftl (230 lines), and a test web/static/tests/core/utils/search.test.js (2). | N-U26-081 |
| VDR-U26-C178 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:679 | if '@' in key or key == '__translation_module__' | FACT | chart load | — | Chart data records carry <field>@<lang> keys that are stripped before creating the record and then used by _load_translations; the English field is the base value. | N-U26-082 |
| VDR-U26-C179 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:69 | access_res_lang_public | FACT | always | — | res.lang ACL: public, portal, internal read-only; system CRUD (rows 69-72). No ir.rule exists for res.lang or language wizards (DB: 0). | N-U26-085 |
| VDR-U26-C180 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:140 | access_base_language_export | FACT | always | — | language wizards: export group_user (1,1,1,0), install and import group_system (1,1,1,0) (rows 136-140). | N-U26-085 |
| VDR-U26-C181 | FUNCTION MAPPING REQUIRED | base/views/base_menus.xml:15 | id="menu_translation_export" | FACT | always | — | Translations, Import/Export and Application Terms menus require group_no_one (debug mode). | N-U26-085 |
| VDR-U26-C182 | FUNCTION MAPPING REQUIRED | mail/models/mail_render_mixin.py:102 | _check_access_right_dynamic_template | FACT | mail template translation edit | — | Editing a mail template translation re-checks the dynamic-template right per language; generic translation edit needs write on record and field (orm/models.py:3557-3559). | N-U26-085 |
| VDR-U26-C183 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:137 | access_base_language_import | OBSERVATION | restored DB | — | DB ir_model_access for res.lang (4 rows: public, portal, user read; system CRUD), base.language.install/import (system), base.language.export (user); 0 ir_rule rows; ir_cron has 1 translation-related row (Transifex reload, active, 7 days); 0 automation rules; 4 menus named Translations, Import / Export, Application Terms, Languages. | N-U26-086 |
| VDR-U26-C184 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:323 | Field "%s" is not cached | FACT | always | — | _get_active_by raises UserError for a field outside CACHED_FIELDS. | N-U26-087 |
| VDR-U26-C185 | FUNCTION MAPPING REQUIRED | base/wizard/base_import_language.py:43 | Could not import the file due to a format mismatch | FACT | import | — | Import errors are logged as a warning and re-raised as UserError. | N-U26-087 |
| VDR-U26-C186 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:184 | cannot render textual amounts | FACT | num2words missing | RT | Missing num2words yields empty amount_to_text and a warning. | N-U26-087 |
| VDR-U26-C187 | FUNCTION MAPPING REQUIRED | base/models/ir_http.py:437 | def _get_web_translations_hash | FACT | web client | — | Web translations are cached by (frozenset(modules), lang) and returned with a sha1 hash; the controller sends content only when the hash differs. | N-U26-088 |
| VDR-U26-C188 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:275 | CACHED_FIELDS | FACT | always | — | Active language data cached in the 'stable' ormcache; fields must not depend on other models or context. | N-U26-088 |
| VDR-U26-C189 | FUNCTION MAPPING REQUIRED | website_sale/models/ir_module_module.py:25 | PSQL functions take 100 args max | FACT | website_sale | — | Language lists are split into batches of 50 to respect the 100-argument limit of PostgreSQL functions. | N-U26-089 |
| VDR-U26-C190 | FUNCTION MAPPING REQUIRED | transifex/models/transifex_code_translation.py:32 | LOCK TABLE | FACT | transifex installed | — | _load_code_translations locks the table in exclusive mode NOWAIT and returns False if the lock is unavailable. | N-U26-088 |
| VDR-U26-C191 | FUNCTION MAPPING REQUIRED | base/models/ir_qweb.py:262 | Used to serve the called template | FACT | always | — | t-lang on a t-call renders the called template with the given language (alias of t-options-lang; only valid on a t-call node). | N-U26-093 |
| VDR-U26-C192 | FUNCTION MAPPING REQUIRED | base/models/ir_qweb.py:2649 | t-lang is an alias of t-options-lang | FACT | always | — | _compile_directive_lang raises SyntaxError if t-lang is used without t-call. | N-U26-093 |
| VDR-U26-C193 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:671 | <t t-set="lang" t-value="o.partner_id.lang"/> | FACT | always | — | account.report_invoice sets lang = o.partner_id.lang per document and calls the invoice document with t-lang=lang (lines 668-676); the document first does o = o.with_context(lang=lang) (line 4). | N-U26-092 |
| VDR-U26-C194 | FUNCTION MAPPING REQUIRED | account/views/report_payment_receipt_templates.xml:107 | o.partner_id.lang or o.company_id.partner_id.lang | FACT | always | — | Payment receipt: partner lang, else company partner lang. | N-U26-092 |
| VDR-U26-C195 | FUNCTION MAPPING REQUIRED | sale/report/ir_actions_report_templates.xml:393 | t-lang="doc.partner_id.lang" | FACT | always | — | Sales order and pro forma: t-lang=doc.partner_id.lang (lines 393, 407). | N-U26-092 |
| VDR-U26-C196 | FUNCTION MAPPING REQUIRED | purchase/report/purchase_order_templates.xml:157 | t-lang="o.partner_id.lang" | FACT | always | — | Purchase order: t-lang=o.partner_id.lang; the quotation report likewise (purchase_quotation_templates.xml:81). | N-U26-092 |
| VDR-U26-C197 | FUNCTION MAPPING REQUIRED | stock/models/stock_picking.py:2050 | def _get_report_lang | FACT | always | — | Delivery slip language = first move's partner lang, else picking partner lang, else env.lang; report_deliveryslip.xml:320 and report_return_slip.xml:41 pass it to t-lang. | N-U26-092 |
| VDR-U26-C198 | FUNCTION MAPPING REQUIRED | stock/report/report_deliveryslip.xml:6 | o._get_report_lang() | FACT | always | — | Delivery slip template switches language through _get_report_lang(). | N-U26-092 |
| VDR-U26-C199 | FUNCTION MAPPING REQUIRED | base/models/ir_actions_report.py:420 | set context language to body language | FACT | PDF pipeline | — | When splitting header/footer/body, each article's data-oe-lang attribute re-sets the context language for the layout render (lines 418-424); web layouts and the invoice template emit data-oe-lang from o.env.context lang. | N-U26-093 |
| VDR-U26-C200 | FUNCTION MAPPING REQUIRED | web/views/report_templates.xml:358 | data-oe-lang | FACT | always | — | All web external layouts add data-oe-lang to the article div from the record's context language. | N-U26-093 |
| VDR-U26-C201 | FUNCTION MAPPING REQUIRED | base/models/ir_actions_report.py:186 | print_report_name = fields.Char | INFERENCE | always | — | ir.actions.report declares type, model, report_type, report_name, report_file, groups, multi, paperformat, print_report_name, attachment_use, attachment, domain (lines 165-192) and no language field; a grep for forced/force lang/report lang finds only stock _get_report_lang. | N-U26-094 |
| VDR-U26-C202 | FUNCTION MAPPING REQUIRED | account/models/account_move_send.py:747 | we don't regenerate pdf if it already exists | FACT | invoice send flow | — | Invoice PDF is created once into invoice_pdf_report_file via _pre_render_qweb_pdf and not regenerated when invoice_pdf_report_id exists (lines 407-434, 747, 761). | N-U26-095 |
| VDR-U26-C203 | FUNCTION MAPPING REQUIRED | account/views/account_report.xml:14 | <field name="attachment"/> | FACT | always | — | The invoice PDF print actions leave attachment empty (not saved by the report action); only original vendor bills use attachment_use (line 28). | N-U26-095 |
| VDR-U26-C204 | FUNCTION MAPPING REQUIRED | account/views/account_report.xml:9 | report_name">account.report_invoice_with_payments | OBSERVATION | restored DB | — | DB ir_act_report_xml has 78 rows; account.report_invoice, report_invoice_with_payments, l10n_th.report_commercial_invoice, sale/purchase/stock reports exist; attachment_use true only for account.report_original_vendor_bill; no report row carries a language setting (no such column). | N-U26-094 |
| VDR-U26-C205 | FUNCTION MAPPING REQUIRED | mail/models/mail_render_mixin.py:57 | Optional translation language (ISO code) | FACT | always | — | Template lang (mail.render.mixin.lang): expression such as {{ object.partner_id.lang }}; a literal code would be a fixed language. | N-U26-096 |
| VDR-U26-C206 | FUNCTION MAPPING REQUIRED | mail/models/mail_render_mixin.py:735 | rendered_langs = self._render_template( | FACT | always | — | mail template lang is rendered as an inline template per record (any expression, including a constant). | N-U26-096 |
| VDR-U26-C207 | FUNCTION MAPPING REQUIRED | account/wizard/account_move_send_wizard.py:210 | mail_lang | FACT | send wizard | — | Send wizard passes mail_lang to the send routine; subject/body/partners are recomputed when lang changes. | N-U26-096 |
| VDR-U26-C208 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:19 | report_commercial_invoice | FACT | l10n_th installed | — | l10n_th.report_commercial_invoice sets lang = o.partner_id.lang and calls account.report_invoice_document with t-lang=lang; its report action is limited by domain to country TH and sale journals (lines 19-37). | N-U26-098 |
| VDR-U26-C209 | FUNCTION MAPPING REQUIRED | l10n_th/models/account_move.py:10 | l10n_th.report_invoice_document | FACT | l10n_th installed | — | For companies with fiscal country TH _get_name_invoice_report returns l10n_th.report_invoice_document; l10n_th/views/report_invoice.xml:40-46 routes the generic invoice report to it with t-lang=lang. | N-U26-098 |
| VDR-U26-C210 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:14 | invoice_title | FACT | l10n_th installed | — | The Thai document replaces the invoice_title node with the English literal 'Tax Invoice' (view arch data). | N-U26-097 |
| VDR-U26-C211 | FUNCTION MAPPING REQUIRED | l10n_th/i18n/th.po:127 | model_terms:ir.ui.view,arch_db | OBSERVATION | source tree | — | th.po holds exactly 1 model_terms entry for the l10n_th report view and 8 code entries; all 23 entries are translated; the Thai text is therefore in a translation file, not in the template. | N-U26-098 |
| VDR-U26-C212 | FUNCTION MAPPING REQUIRED | l10n_gcc_invoice/views/report_invoice.xml:7 | t-set="lang_sec" | FACT | l10n_gcc_invoice installed (not installed in DB) | — | l10n_gcc invoice computes lang_sec = _get_code('ar_001') (or en_US when the main lang is ar_001) and renders o_sec = o.with_context(lang=lang_sec), gated by display_in_lang_sec (lines 7-12). | N-U26-099 |
| VDR-U26-C213 | FUNCTION MAPPING REQUIRED | l10n_gcc_invoice/models/res_company.py:7 | l10n_gcc_dual_language_invoice | FACT | l10n_gcc_invoice installed | — | The dual-language invoice option is a company Boolean 'GCC Formatted Invoices'. | N-U26-099 |
| VDR-U26-C214 | FUNCTION MAPPING REQUIRED | web/views/report_templates.xml:354 | o_company_#{company.id}_layout article | FACT | always | — | External layouts render company header/footer fields (translatable) inside the same article block and therefore in the document language. | N-U26-097 |
| VDR-U26-C215 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:135 | invoice_label = fields.Char | FACT | always | — | Printed tax names come from account.tax.name and invoice_label (translatable), read in the document language context o.with_context(lang=lang). | N-U26-097 |
| VDR-U26-C216 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:674 | t-lang="lang" | INFERENCE | mechanical scan | — | Mechanical grep of t-lang= across odoo/addons XML: 52 occurrences; values: lang (28), event.lang or event.env.lang (5), lang and lang.replace (4), event.lang or attendee.env.lang (4), doc.partner_id.lang (4), o.partner_id.lang (2), o._mail_get_customer().lang or o.env.lang (2), o._get_report_lang() (2), o.vendor_id.lang (1); no string constants. | N-U26-093 |
| VDR-U26-C217 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:277 | Please promise all these fields | FACT | always | — | CACHED_FIELDS docstring: the cached fields must not depend on other models or context and must not be translated. | N-U26-104 |
| VDR-U26-C218 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:212 | be 100% cross-platform | FACT | language created from OS locale | — | Date/time formats are mapped to the C-standard directives to be cross-platform. | N-U26-104 |
| VDR-U26-C219 | FUNCTION MAPPING REQUIRED | web/static/src/core/l10n/translation.js:103 | avoid conflicting | FACT | always | — | Client docstring: providing the module context avoids conflicting translations (example: 'table' in a restaurant module vs a spreadsheet). | N-U26-105 |
| VDR-U26-C220 | FUNCTION MAPPING REQUIRED | web/controllers/webclient.py:22 | for translating the login page | FACT | login page | — | bootstrap_translations docstring: local po translations only for the login page and database chrome, in the browser language, until a session exists. | N-U26-111 |
| VDR-U26-C221 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:419 | Format() will return the language-specific output | FACT | always | — | res.lang.format docstring: returns the language-specific output for float values from the language's data. | N-U26-113 |
| VDR-U26-C222 | FUNCTION MAPPING REQUIRED | base/models/res_country.py:159 | The layout contains an invalid format key | FACT | always | — | _check_address_format tries the layout against all known address keys and raises UserError on ValueError/KeyError. | N-U26-115 |
| VDR-U26-C223 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:565 | The data can contain translation values | FACT | always | — | _load_data docstring: template data can contain translation values (name@fr_FR) to translate the name. | N-U26-116 |
| VDR-U26-C224 | FUNCTION MAPPING REQUIRED | transifex/__manifest__.py:14 | speed up translations | FACT | transifex installed | — | Manifest description: the purpose is to speed up translations of the main modules. | N-U26-120 |
| VDR-U26-C225 | FUNCTION MAPPING REQUIRED | base/views/base_menus.xml:14 | id="menu_translation_app" | FACT | always | — | Application Terms menu is restricted to base.group_no_one. | N-U26-121 |
| VDR-U26-C226 | FUNCTION MAPPING REQUIRED | transifex/models/transifex_code_translation.py:37 | langs = [lang for lang, _ in self._get_languages() if lang != 'en_US'] | FACT | transifex installed | — | _load_code_translations loads only installed languages other than en_US. | N-U26-122 |
| VDR-U26-C227 | FUNCTION MAPPING REQUIRED | base/models/ir_qweb.py:262 | Used to serve the called template | FACT | always | — | t-lang documentation: serves the called template in another language. | N-U26-123 |
| VDR-U26-C228 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:334 | def action_unarchive | INFERENCE | always | — | The only state of a language is the active flag; activation goes through action_unarchive (loads translations, lines 334-342), deactivation through write with guards (lines 352-364), deletion through unlink with guards (lines 392-404). | N-U26-008 |
| VDR-U26-C229 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:97 | thousands_sep = fields.Char | INFERENCE | always | — | res.lang defines only name, code, iso_code, url_code, active, direction, date_format, time_format, week_start, grouping, decimal_point, thousands_sep, flag_image (lines 72-108): no field for calendar era, collation or numeral system. | N-U26-014 |
| VDR-U26-C230 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | Behaviour of a bulk activation of many catalogue languages and of languages created from host locale data cannot be determined without running Odoo. | N-U26-015 |
| VDR-U26-C231 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | Memory behaviour of the unbounded per-(module, lang) pools and exact fallback behaviour for partially translated regional files are not verifiable statically. | N-U26-027 |
| VDR-U26-C232 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:134 | description = fields.Html(string='Description', translate=html_translate) | FACT | always | — | html_translate (callable) marks term-level translation, e.g. account.tax.description; most Char fields use translate=True (whole value). | N-U26-029 |
| VDR-U26-C233 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | Re-alignment of term-level translations after bulk English edits and the performance of the trigram prefilter on large catalogues are not verifiable statically. | N-U26-040 |
| VDR-U26-C234 | FUNCTION MAPPING REQUIRED | base/wizard/base_language_install.py:23 | Overwrite Existing Terms | INFERENCE | always | — | Overwrite defaults to True in the install wizard and the import wizard, so a casual activation replaces customised translations on records not flagged noupdate (see im_save). | N-U26-051 |
| VDR-U26-C235 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:140 | access_base_language_export | INFERENCE | always | — | Because the export wizard is granted to internal users, any internal user can export the term catalogue and record translations of models they can read. | N-U26-051 |
| VDR-U26-C236 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | Load time and memory of loading 310 Thai files, and the effect of overwrite on customised records, need execution. | N-U26-052 |
| VDR-U26-C237 | FUNCTION MAPPING REQUIRED | website/models/website.py:127 | default=_active_languages | FACT | website installed | — | website.language_ids default = all active languages; an onchange resets default_lang_id to the first language when the default leaves the list (lines 223-227). | N-U26-059 |
| VDR-U26-C238 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:2291 | return self.env.lang | INFERENCE | always | — | The order language is the partner's language (public partner excluded) and otherwise the environment language; there is no override setting. | N-U26-061 |
| VDR-U26-C239 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:2288 | is_public | INFERENCE | always | — | For public/anonymous partners the order language is the staff environment language. | N-U26-062 |
| VDR-U26-C240 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | Cookie/redirect behaviour across several websites and domains and portal download language are not verifiable statically. | N-U26-063 |
| VDR-U26-C241 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:6 | o.with_context(lang=lang) | INFERENCE | always | — | Inside a document the formatting language is the context language set by o.with_context(lang=lang) with lang = partner language, so monetary and date widgets follow the partner. | N-U26-073 |
| VDR-U26-C242 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | Whether num2words supports Thai (library not in tree, not installed) and how the browser locale renders Thai dates/numerals cannot be established statically; pinned versions 0.5.10/0.5.13 per requirements.txt. | N-U26-075 |
| VDR-U26-C243 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_partner.py:18 | Headquarter | INFERENCE | always | — | Example of the three locations: the code sentence 'Headquarter' (code), the report view arch (data, l10n_th/views/report_invoice.xml:15) and l10n_th/i18n/th.po (translation file) for the Thai wording. | N-U26-076 |
| VDR-U26-C244 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:2 | l10n_th_account_111100 | INFERENCE | chart load | — | Per-language values are keyed by the id column (record external id) and field; an id change orphans the value. | N-U26-084 |
| VDR-U26-C245 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | — | A file outside the Community module structure (a programme verification note inside the studied folder) contains Thai text; excluded from counts. | N-U26-083 |
| VDR-U26-C246 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:140 | access_base_language_export | INFERENCE | always | — | Coarse rights: export to all internal users; translation edit needs only write on the field; no translation-specific group or audit model exists in the files read. | N-U26-090 |
| VDR-U26-C247 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | Tracking of translation edits on tracked fields and load impact of many active languages are not verifiable statically. | N-U26-091 |
| VDR-U26-C248 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:6 | o.with_context(lang=lang) | INFERENCE | always | — | Master data printed on the document (taxes, accounts, units, company header/footer) is read with the document language context and falls back to English per field when a value is missing. | N-U26-100 |
| VDR-U26-C249 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:671 | <t t-set="lang" t-value="o.partner_id.lang"/> | INFERENCE | always | — | The body language is fixed by o.partner_id.lang, so the viewer's UI language does not enter the document body. | N-U26-101 |
| VDR-U26-C250 | FUNCTION MAPPING REQUIRED | account/models/account_move_send.py:747 | we don't regenerate pdf if it already exists | INFERENCE | invoice send flow | — | A stored invoice PDF keeps the language and master-data wording of its first generation. | N-U26-102 |
| VDR-U26-C251 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | Output of a Thai-language invoice with Thai active (fonts, numerals, year), portal download language and cached preview language need execution. | N-U26-103 |

## 12B. Claims table B (framework core outside odoo/addons; paths relative to `odoo/`; NOT checked by vdr_check.py)

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| CORE-U26-K001 | FUNCTION MAPPING REQUIRED | orm/environments.py:302 | Invalid language code | FACT | always | — | Environment.lang reads context['lang'] and raises UserError for a code that is neither en_US nor an active language. | N-U26-013 |
| CORE-U26-K002 | FUNCTION MAPPING REQUIRED | tools/misc.py:1308 | def get_lang | FACT | always | — | get_lang picks lang_code if installed, else context lang, else the company partner's lang, else en_US if installed, else the first installed language. | N-U26-010 |
| CORE-U26-K003 | FUNCTION MAPPING REQUIRED | http.py:231 | DEFAULT_LANG = 'en_US' | FACT | always | — | The framework-level default language constant is en_US. | N-U26-010 |
| CORE-U26-K004 | FUNCTION MAPPING REQUIRED | http.py:1909 | def best_lang | FACT | HTTP request | — | Request.best_lang derives a locale code from the Accept-Language header (territory form language_TERRITORY or babel alias). | N-U26-010 |
| CORE-U26-K005 | FUNCTION MAPPING REQUIRED | tools/translate.py:1807 | def load_language | FACT | database init / CLI | — | load_language creates a base.language.install wizard for the language and runs lang_install; used by registry loading (modules/loading.py:414-421) and CLI loadlang. | N-U26-004 |
| CORE-U26-K006 | FUNCTION MAPPING REQUIRED | service/db.py:78 | modules._update_translations(lang) | FACT | database creation | — | _initialize_db sets config load_language then updates translations of installed modules for that language. | N-U26-009 |
| CORE-U26-K007 | FUNCTION MAPPING REQUIRED | tools/translate.py:419 | def get_translation | FACT | always | — | get_translation(module, lang, source, args): lang 'en_US' returns source; otherwise code_translations.get_python_translations(module, lang).get(source, source). The lookup key is the source string within (module, lang). | N-U26-018 |
| CORE-U26-K008 | FUNCTION MAPPING REQUIRED | tools/translate.py:423 | if lang == 'en_US': | FACT | always | — | For en_US the translation equals the source and the module is not used. | N-U26-018 |
| CORE-U26-K009 | FUNCTION MAPPING REQUIRED | tools/translate.py:433 | isinstance(a, Markup) | FACT | args present | — | If any argument is Markup the translation is escaped; LazyGettext args are translated into lang; iterable args are formatted with format_list. | N-U26-021 |
| CORE-U26-K010 | FUNCTION MAPPING REQUIRED | tools/translate.py:455 | Bad translation %r for string %r | FACT | always | — | Formatting uses translation % args; on TypeError/ValueError/KeyError it logs the bad translation and returns source % args. | N-U26-021 |
| CORE-U26-K011 | FUNCTION MAPPING REQUIRED | tools/translate.py:459 | def get_translated_module | FACT | always | — | The module is derived from the calling frame's __name__ (odoo.addons.<module>) or the file path; non-addon code falls back to 'base'. | N-U26-019 |
| CORE-U26-K012 | FUNCTION MAPPING REQUIRED | tools/translate.py:525 | def _get_lang | FACT | always | — | Language detection order: local context.get('lang'), kwargs context, self.env.lang, request env lang, guessed user language via res.users.context_get, default_lang, else '' with a warning (translation skipped). | N-U26-020 |
| CORE-U26-K013 | FUNCTION MAPPING REQUIRED | tools/translate.py:586 | class LazyGettext | FACT | always | — | LazyGettext defers get_translation until __str__/_translate; equality, hashing and ordering raise NotImplementedError so lazy terms cannot be compared. | N-U26-106 |
| CORE-U26-K014 | FUNCTION MAPPING REQUIRED | tools/translate.py:658 | class LazyTranslate | FACT | always | — | LazyTranslate(module, default_lang) builds LazyGettext terms; its default language is en_US for module base. | N-U26-017 |
| CORE-U26-K015 | FUNCTION MAPPING REQUIRED | tools/translate.py:681 | _ = get_text_alias | FACT | always | — | The public function _ is get_text_alias(source, *args, **kwargs) and takes one source string plus args or kwargs (not both); _lt is LazyGettext. | N-U26-017 |
| CORE-U26-K016 | FUNCTION MAPPING REQUIRED | orm/environments.py:315 | def _(self, source | FACT | always | — | env._(source, *args) translates with the environment language; en_US skips module lookup; errors are logged at debug and the source is returned. | N-U26-017 |
| CORE-U26-K017 | FUNCTION MAPPING REQUIRED | tools/translate.py:1858 | class CodeTranslations | FACT | always | — | CodeTranslations caches python_translations and web_translations per (module_name, lang) in dicts {src: value}. | N-U26-023 |
| CORE-U26-K018 | FUNCTION MAPPING REQUIRED | tools/translate.py:1898 | PYTHON_TRANSLATION_COMMENT in row | FACT | always | — | Python code translations are the po rows of type code whose comments contain 'odoo-python' with a non-empty value; JS ones use 'odoo-javascript'. | N-U26-023 |
| CORE-U26-K019 | FUNCTION MAPPING REQUIRED | tools/translate.py:1837 | def get_po_paths | FACT | always | — | get_po_paths yields <module>/i18n/<base>.po and <module>/i18n_extra/<base>.po for each of get_base_langs(lang) that exists. | N-U26-023 |
| CORE-U26-K020 | FUNCTION MAPPING REQUIRED | tools/translate.py:1823 | def get_base_langs | FACT | always | — | get_base_langs('th_TH') = ['th', 'th_TH']: the generic language file is loaded first and the regional file overrides it; special cases exist for es and zh_HK. | N-U26-023 |
| CORE-U26-K021 | FUNCTION MAPPING REQUIRED | tools/translate.py:862 | found_code_occurrence | FACT | po reading | — | PoFileReader keeps only the first code occurrence per entry (unicity constraint on code translation); the code translation is keyed by msgid only. | N-U26-106 |
| CORE-U26-K022 | FUNCTION MAPPING REQUIRED | tools/translate.py:687 | Translation terms may not include escaped newlines | FACT | export | — | quote() asserts that source terms contain no literal backslash-n sequence. | N-U26-106 |
| CORE-U26-K023 | FUNCTION MAPPING REQUIRED | tools/translate.py:1491 | extract_keywords={'_': None, '_lt': None} | FACT | export | — | Python extraction keywords are '_' and '_lt' with None (single message argument); JS uses '_t' (line 1497). No plural or context keywords are registered. | N-U26-022 |
| CORE-U26-K024 | FUNCTION MAPPING REQUIRED | tools/translate.py:982 | 'Plural-Forms': '' | FACT | export | — | PoFileWriter writes an empty Plural-Forms header. | N-U26-022 |
| CORE-U26-K025 | FUNCTION MAPPING REQUIRED | tools/translate.py:1218 | any(x.isalpha() for x in sanitized_term) | FACT | export | — | Only terms with at least one alphabetic character are exported. | N-U26-024 |
| CORE-U26-K026 | FUNCTION MAPPING REQUIRED | tools/translate.py:1465 | def _export_translatable_resources | FACT | export | — | Export scans *.py (python), static/src *.js (_t) and *.xml (QWeb), spreadsheet dashboards, plus orm/osv/report/modules/service/tools in the framework path; only installed modules. | N-U26-024 |
| CORE-U26-K027 | FUNCTION MAPPING REQUIRED | orm/fields_textual.py:35 | whether the field is translated | FACT | always | — | BaseString.translate is False, True or a callable(callback, value): True translates the whole value, a callable (html_translate, xml_translate) splits it into terms. | N-U26-108 |
| CORE-U26-K028 | FUNCTION MAPPING REQUIRED | orm/fields_textual.py:72 | convert_column_translatable | FACT | schema update | — | A translatable stored field is converted to a jsonb column (convert_column_translatable) and back when translate is removed. | N-U26-028 |
| CORE-U26-K029 | FUNCTION MAPPING REQUIRED | orm/fields_textual.py:97 | PsycopgJson({'en_US': value | FACT | insert | — | On insert the column value is {'en_US': value, <env lang>: value}. | N-U26-028 |
| CORE-U26-K030 | FUNCTION MAPPING REQUIRED | orm/fields_textual.py:229 | def get_translation_fallback_langs | FACT | read | — | Fallback languages are (lang, 'en_US'); for en_US only en_US. | N-U26-028 |
| CORE-U26-K031 | FUNCTION MAPPING REQUIRED | orm/fields_textual.py:414 | SQL("COALESCE(%s)" | FACT | search/order | — | to_sql builds COALESCE(col->>lang, col->>'en_US') so search and order use the reader language with English fallback. | N-U26-032 |
| CORE-U26-K032 | FUNCTION MAPPING REQUIRED | orm/fields_textual.py:451 | a prefilter using trigram index | FACT | pg_trgm available and index='trigram' | — | Operators in/like/ilike/=like/=ilike get a trigram prefilter over jsonb_path_query_array(col, '$.*') (all languages) ANDed with the base condition. | N-U26-032 |
| CORE-U26-K033 | FUNCTION MAPPING REQUIRED | orm/fields_textual.py:329 | # model translation | FACT | write on stored translatable field | — | Whole-value write updates only the current language entry; when en_US is not an active language en_US is written as well (lines 329-338). | N-U26-030 |
| CORE-U26-K034 | FUNCTION MAPPING REQUIRED | orm/fields_textual.py:340 | # model term translation | FACT | write on term-translated field | — | Term-level write rebuilds the translation dictionary and re-translates all stored languages with the new structure (lines 340-405). | N-U26-030 |
| CORE-U26-K035 | FUNCTION MAPPING REQUIRED | orm/fields_textual.py:65 | cannot depend on context | FACT | always | — | Translated stored fields cannot depend on context (warning at setup, assertion on write). | N-U26-038 |
| CORE-U26-K036 | FUNCTION MAPPING REQUIRED | orm/fields_textual.py:59 | Translated stored related field | FACT | always | — | A stored related translatable field logs a warning because it is not computed correctly in all languages. | N-U26-038 |
| CORE-U26-K037 | FUNCTION MAPPING REQUIRED | orm/models.py:3510 | def _update_field_translations | FACT | always | — | update_field_translations/_update_field_translations: ensure_one, check_access('write') on the record and _check_field_access(field,'write'); {lang: value}, False removes the translation and falls back to en_US. | N-U26-031 |
| CORE-U26-K038 | FUNCTION MAPPING REQUIRED | orm/models.py:3670 | def get_field_translations | FACT | always | — | get_field_translations returns [{lang, source, value}] for the requested or all installed languages and a context with translation_type and translation_show_source. | N-U26-031 |
| CORE-U26-K039 | FUNCTION MAPPING REQUIRED | orm/models.py:5301 | sql_field = self._field_to_sql(alias, fname, query) | FACT | ordering | — | _order_field_to_sql uses _field_to_sql, hence the translated COALESCE expression, so ordering is in the reader language (database collation applies). | N-U26-032 |
| CORE-U26-K040 | FUNCTION MAPPING REQUIRED | orm/models.py:450 | _translate: bool = True | FACT | always | — | Model flag _translate=False disables translation export for a model. | N-U26-108 |
| CORE-U26-K041 | FUNCTION MAPPING REQUIRED | tools/translate.py:1310 | class TranslationRecordReader | FACT | record export | — | TranslationRecordReader exports translatable stored fields of chosen records and creates external ids (__ensure_xml_id) for records lacking one. | N-U26-033 |
| CORE-U26-K042 | FUNCTION MAPPING REQUIRED | tools/translate.py:1221 | def _export_imdinfo | FACT | export | — | Export emits type 'model' for whole-value and 'model_terms' for term fields, named <model>,<field>, referenced by module.xmlid; empty value when translation equals source. | N-U26-033 |
| CORE-U26-K043 | FUNCTION MAPPING REQUIRED | modules/loading.py:234 | module._update_translations(overwrite=overwrite) | FACT | module install/upgrade | — | After a module's data and migrations load, translations for all installed languages are updated with overwrite=config['overwrite_existing_translations'] (default False). | N-U26-043 |
| CORE-U26-K044 | FUNCTION MAPPING REQUIRED | tools/config.py:409 | overwrite_existing_translations | FACT | command line | — | --i18n-overwrite (default False) is refused unless --update is also given; --load-language lists languages to load. | N-U26-110 |
| CORE-U26-K045 | FUNCTION MAPPING REQUIRED | tools/translate.py:1609 | For a record with 'noupdate' in | FACT | always | — | save(): an existing translation is overwritten if force_overwrite or (not noupdate and overwrite); otherwise existing translations are kept; 'existing' means a jsonb key for the language or a term differing from en_US. | N-U26-044 |
| CORE-U26-K046 | FUNCTION MAPPING REQUIRED | tools/translate.py:1711 | value_query = SQL("m.%(field)s | FACT | always | — | Whole-value import merges jsonb in three precedence orders (force_overwrite, overwrite, keep) via a single UPDATE per batch (cr.IN_MAX). | N-U26-044 |
| CORE-U26-K047 | FUNCTION MAPPING REQUIRED | tools/translate.py:1584 | if row.get('type') == 'code':  # ignore code translations | FACT | always | — | The DB importer ignores empty values and code-type entries, rows for other languages than the base-language chain, models or fields not present/translatable/stored. | N-U26-045 |
| CORE-U26-K048 | FUNCTION MAPPING REQUIRED | tools/translate.py:900 | Skipped deprecated occurrence | FACT | po reading | — | Obsolete entries are skipped; selection:, sql_constraint: and constraint: occurrences are skipped as deprecated; unknown occurrences log 'malformed po file'. | N-U26-045 |
| CORE-U26-K049 | FUNCTION MAPPING REQUIRED | tools/translate.py:1566 | language not found | FACT | always | — | Loading a file for a language that is not active logs an error and returns without loading. | N-U26-048 |
| CORE-U26-K050 | FUNCTION MAPPING REQUIRED | tools/translate.py:788 | class XMLDataFileReader | FACT | always | — | XML data files may carry <field name='<field>@<lang>'> next to the base field; each yields a type 'model' translation keyed by record id and field. | N-U26-043 |
| CORE-U26-K051 | FUNCTION MAPPING REQUIRED | tools/translate.py:754 | class CSVDataFileReader | FACT | always | — | CSV data files may carry '<field>@<lang>' columns; the model is the file name before '-'; entries are keyed by id column and field. | N-U26-043 |
| CORE-U26-K052 | FUNCTION MAPPING REQUIRED | tools/convert.py:399 | continue  # used for translations | FACT | data loading | — | When loading data, fields named with '@' are skipped by the record loader (used for translations only); CSV loader strips '@' columns (lines 730-743). | N-U26-043 |
| CORE-U26-K053 | FUNCTION MAPPING REQUIRED | cli/i18n.py:19 | IMPORT_EXTENSIONS | FACT | CLI | — | odoo i18n import/export/loadlang: import accepts .po/.csv, export .po/.pot/.tgz/.csv; export writes <module>/i18n/<iso_code>.po or <module>.pot; loadlang runs load_language. | N-U26-046 |
| CORE-U26-K054 | FUNCTION MAPPING REQUIRED | tools/translate.py:839 | pot_path = get_pot_path | FACT | po reading | — | When a .po is read from disk its sibling <module>.pot is merged in to refresh comments. | N-U26-046 |
| CORE-U26-K055 | FUNCTION MAPPING REQUIRED | tools/translate.py:947 | we now group the translations by source | FACT | export | — | PoFileWriter groups rows by source text: one translation per English source; the first non-identical translation wins. | N-U26-046 |
| CORE-U26-K056 | FUNCTION MAPPING REQUIRED | tools/misc.py:1342 | def formatLang | FACT | always | — | formatLang rounds with float_round (method/unit options), uses get_lang(env) record .format and appends the currency symbol before/after by currency.position with NON_BREAKING_SPACE (lines 1400-1407). | N-U26-064 |
| CORE-U26-K057 | FUNCTION MAPPING REQUIRED | tools/misc.py:1635 | def format_amount | FACT | always | — | format_amount uses currency.decimal_places, lang.format with grouping, replaces spaces with NBSP and prefixes/suffixes the symbol by currency.position. | N-U26-064 |
| CORE-U26-K058 | FUNCTION MAPPING REQUIRED | tools/misc.py:1449 | posix_to_ldml(lang.date_format | FACT | always | — | format_date converts the language's strftime pattern to LDML with the babel locale of lang.code and calls babel.dates.format_date; no calendar argument is passed. | N-U26-065 |
| CORE-U26-K059 | FUNCTION MAPPING REQUIRED | tools/misc.py:1330 | def babel_locale_parse | FACT | always | — | babel_locale_parse falls back to the default locale and then en_US when the code is unknown. | N-U26-065 |
| CORE-U26-K060 | FUNCTION MAPPING REQUIRED | service/db.py:146 | LC_COLLATE 'C' | FACT | database creation | — | New databases are created with LC_COLLATE 'C' when the template is template0, otherwise the template's collation; pg_trgm is always created, unaccent only when configured. | N-U26-070 |
| CORE-U26-K061 | FUNCTION MAPPING REQUIRED | tools/convert.py:399 | continue  # used for translations | FACT | data load | — | The generic XML/CSV record loader ignores '@' fields so they never reach the base value. | N-U26-118 |
| CORE-U26-K062 | FUNCTION MAPPING REQUIRED | tools/translate.py:1630 | split_every(cr.IN_MAX | FACT | always | — | Importer batches records by cr.IN_MAX per query. | N-U26-088 |
| CORE-U26-K063 | FUNCTION MAPPING REQUIRED | tools/translate.py:1861 | self.python_translations = {} | FACT | always | — | Python and web code translations are stored in two unbounded dicts keyed by (module, lang) for the process lifetime. | N-U26-088 |
| CORE-U26-K064 | FUNCTION MAPPING REQUIRED | tools/translate.py:637 | raise NotImplementedError() | FACT | always | — | LazyGettext equality, hash and ordering raise NotImplementedError. | N-U26-089 |
| CORE-U26-K065 | FUNCTION MAPPING REQUIRED | orm/environments.py:301 | cannot translate here because we do not have a valid language | FACT | always | — | An invalid context language raises UserError('Invalid language code'). | N-U26-087 |
| CORE-U26-K066 | FUNCTION MAPPING REQUIRED | tools/translate.py:591 | This eases the search for terms to translate | FACT | always | — | LazyGettext docstring: lazy strings declared early ease the search for terms to translate. | N-U26-105 |
| CORE-U26-K067 | FUNCTION MAPPING REQUIRED | orm/fields_textual.py:336 | make sure value_en is meaningful | FACT | en_US inactive | — | Comment: if en_US is not active, en_US is always written to make sure value_en is meaningful. | N-U26-107 |
| CORE-U26-K068 | FUNCTION MAPPING REQUIRED | tools/translate.py:1523 | helps speeding up the whole import | FACT | always | — | TranslationImporter docstring: loading many files then importing them all at once speeds up the whole import. | N-U26-109 |
| CORE-U26-K069 | FUNCTION MAPPING REQUIRED | tools/translate.py:847 | Because the POT comments are correct | FACT | po reading | — | Comment: POT comments are correct upstream while PO comments tend to be outdated, hence the merge. | N-U26-109 |
| CORE-U26-K070 | FUNCTION MAPPING REQUIRED | tools/translate.py:764 | split('-')[0] | FACT | csv data file | — | CSVDataFileReader derives the model from the file name before '-' and pairs '<field>@<lang>' with '<field>' (lines 764, 769-785). | N-U26-119 |
| CORE-U26-K071 | FUNCTION MAPPING REQUIRED | tools/translate.py:427 | code_translations.get_python_translations(module, lang).get(source, source) | INFERENCE | always | — | Lookup is an exact dict .get(source, source): if the English wording in code changes, the previous msgid no longer matches and the sentence falls back to English until the po file is regenerated. | N-U26-026 |
| CORE-U26-K072 | FUNCTION MAPPING REQUIRED | orm/fields_textual.py:374 | closest_term | INFERENCE | term-level write | — | When English fragments change, the writer matches old and new terms by closeness and drops translations of terms with no close match (lines 367-387). | N-U26-039 |

