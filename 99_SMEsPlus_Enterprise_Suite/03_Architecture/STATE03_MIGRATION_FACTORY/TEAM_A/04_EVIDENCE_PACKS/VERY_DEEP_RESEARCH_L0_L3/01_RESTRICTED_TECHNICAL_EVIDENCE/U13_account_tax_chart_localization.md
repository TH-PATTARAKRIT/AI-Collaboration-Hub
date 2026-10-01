# U13 — account_tax_chart_localization — Restricted Technical Evidence

> **RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION**
> Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**
> Unit: U13 `account_tax_chart_localization` · Source revision: `19.0.post20260921` (Odoo 19 Community only) · Date: 2026-10-02
> Modules studied: `account` (taxes, fiscal positions, chart of accounts, chart-template loader, currency/cash-rounding use, company accounting settings, partner accounting properties, analytic hook on journal items, tax-report support data), `l10n_th`, `account_edi`, `account_edi_ubl_cii`, `account_qr_code_emv`, `account_add_gln`.
> Read-only on source; DB queried only for configuration/structure (counts, flags, seeded configuration, ACL/rule/cron rows). No Odoo started, no L5/AWT claims. Items needing execution are flagged `RT`.
> No V-level, completeness, coverage %, gate or approval is asserted. Nothing from `Extra_Thailand`, `Extra_Module_scgl` or any proprietary code was opened or used; `l10n_th` here is the Community module only.
> Claim IDs `VDR-U13-C###`; neutral IDs `N-U13-###` (see `02_NEUTRAL_KNOWLEDGE/U13_account_tax_chart_localization_NEUTRAL.md`). Claim references in the prose below are claim IDs resolved at generation time; every statement is backed by a row in section 11.

## 0. Scope, method and Function-ID mapping

| Capability | Function-ID | Note |
|---|---|---|
| CAP-U13-01 Tax computation engine | FUNCTION MAPPING REQUIRED | no index entry for tax engine |
| CAP-U13-02 Fiscal positions and mapping | FUNCTION MAPPING REQUIRED | no index entry |
| CAP-U13-03 Chart of accounts and loader | MCT-F03 (shared vs per-company chart) used only on the claims that concern sharing of accounts between companies; everything else FUNCTION MAPPING REQUIRED | MCT-F03 genuinely matches only the shared/per-company question |
| CAP-U13-04 Currencies in accounting, cash rounding | FUNCTION MAPPING REQUIRED | base currency model hand-off to U01 |
| CAP-U13-05 Company accounting settings, period configuration | PCO-F02 (fiscal year/period configuration) on fiscal-year/opening claims; PCO-F01 on lock-date field claims (fields only; engine is U11) | |
| CAP-U13-06 Partner accounting properties | FUNCTION MAPPING REQUIRED | |
| CAP-U13-07 Analytic distribution on journal items (account side) | FUNCTION MAPPING REQUIRED | analytic model itself is U02 |
| CAP-U13-08 Thai localization | FUNCTION MAPPING REQUIRED | |
| CAP-U13-09 E-invoicing, QR, GLN | FUNCTION MAPPING REQUIRED | |
| CAP-U13-10 Roles, rules, jobs, failures | FUNCTION MAPPING REQUIRED | |

Method: full read of `account/models/account_tax.py` (engine, repartition, groups), `partner.py` (fiscal position and partner properties), `account_account.py`, `chart_template.py`, `company.py`, `res_currency.py`, `account_cash_rounding.py`, `res_config_settings.py`, `ir_module.py`, analytic hooks in `account_move_line.py`, the whole of `l10n_th`, `account_edi`, `account_add_gln`, `account_qr_code_emv`, and structure/trigger points of `account_edi_ubl_cii` (breadth, not field mappings). Base-module reads of `base/models/res_currency.py`, `analytic/models/analytic_mixin.py`, `analytic/models/analytic_plan.py` and `base/security/base_security.xml` were limited to what the capabilities need (see section 12).

---

## CAP-U13-01 Tax computation engine

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Turn the taxes attached to a document line (percent, fixed, division, group) into base amounts, per-tax amounts and totals, in document and company currency, honouring price-included taxes, rounding method, discount, invoice versus refund distribution, tags and accounts, so that the same numbers appear in the form preview, the posted journal items, tax totals and electronic exports. VDR-U13-C085

### D2 Architecture, data, objects
- `account.tax` (fields: `amount_type`, `type_tax_use`, `sequence`, `price_include_override`, `include_base_amount`, `is_base_affected`, `tax_group_id`, `country_id`, `tax_exigibility`, `cash_basis_transition_account_id`, `children_tax_ids`, `fiscal_position_ids`, `original_tax_ids`, `analytic`, `invoice_repartition_line_ids`, `refund_repartition_line_ids`) VDR-U13-C001 VDR-U13-C002 VDR-U13-C003.
- `account.tax.repartition.line` (factor_percent, repartition_type base/tax, document_type invoice/refund, account_id, tag_ids, use_in_tax_closing) VDR-U13-C036.
- `account.tax.group` (sequence, country, payable/receivable/advance accounts, preceding_subtotal) VDR-U13-C055.
- Company: `tax_calculation_rounding_method`, `account_price_include`, `tax_exigibility`; product `taxes_id`/`supplier_taxes_id`; account `tax_ids`; `account.account.tag` (applicability taxes).
- Consumers: `account.move` (`_get_rounded_base_and_tax_lines`, `_compute_tax_totals`, dynamic tax lines), `account.move.line` (`_compute_tax_ids`, price subtotal/total), `compute_all` legacy API, EDI builders (`_validate_taxes`).

### D3 Source/technical/workflow logic
Control/data flow (account/models/account_tax.py):
1. `_prepare_base_line_for_taxes_computation` builds a base-line dict from any record. VDR-U13-C080
2. `_add_tax_details_in_base_lines` applies the discount, calls `_get_tax_details` per line, converts with the line rate and rounds per line only for `round_per_line`. VDR-U13-C019 VDR-U13-C020
3. `_get_tax_details`: flatten groups VDR-U13-C004, batch VDR-U13-C005, evaluate fixed, then price-included (reverse), then price-excluded (normal) VDR-U13-C006 VDR-U13-C007; `_propagate_extra_taxes_base` adjusts bases VDR-U13-C017; formulas VDR-U13-C008 VDR-U13-C009 VDR-U13-C010 VDR-U13-C011; negative factor taxes get a mirrored reverse-charge entry VDR-U13-C034.
4. `_round_base_lines_tax_details`: raw rounding, manual amounts VDR-U13-C081, then global redistribution VDR-U13-C024 VDR-U13-C025.
5. `_add_accounting_data_to_base_line_tax_details`: repartition per document type VDR-U13-C041, tags VDR-U13-C043, accounts VDR-U13-C042, delta spread VDR-U13-C044.
6. `_prepare_tax_lines`: grouping key VDR-U13-C045, analytic copy VDR-U13-C046, zero lines VDR-U13-C047, add/update/delete VDR-U13-C048.
7. `_get_tax_totals_summary` groups by tax group VDR-U13-C051 VDR-U13-C052 VDR-U13-C053; invoice entry VDR-U13-C054.

State list (tax lifecycle; no workflow field exists):
- `created (default distribution lines) -> in use [first journal item references it] (VDR-U13-C067)`
- `active -> archived [write active=False; no guard] (VDR-U13-C069)`
- `in use -> deletion refused [unlink] (VDR-U13-C066)`
- `on_invoice -> on_payment [write tax_exigibility; needs reconcilable transition account] (VDR-U13-C071)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Line with taxes -> base line dict -> details -> rounding -> accounting data -> tax journal lines; totals via tax groups (VDR-U13-C080, VDR-U13-C048, VDR-U13-C054). Default taxes from product/account then fiscal position (VDR-U13-C077, VDR-U13-C078). |
| 2 | Reversal / cancel / negative | Refund uses refund distribution lines (VDR-U13-C041); negative factors create reverse-charge pairs (VDR-U13-C034); delete of used tax refused (VDR-U13-C066); archive not guarded (VDR-U13-C069). |
| 3 | Multi-company / data scope | Taxes company-owned with parent-of checks; filter walks up company hierarchy (VDR-U13-C076); company change blocked if used (VDR-U13-C065); names unique across tree (VDR-U13-C061); country defaults from company (VDR-U13-C060). |
| 4 | Side effects / cross-module | Tags feed tax report engine; analytic distribution copied to tax lines (VDR-U13-C046); EDI export revalidates repartition (VDR-U13-C079); product defaults (VDR-U13-C077); tax group accounts used by tax closing (VDR-U13-C055). |
| 5 | Configuration / optionality | Rounding method and price-include default per company (VDR-U13-C023, VDR-U13-C013); price mode locked after entries (VDR-U13-C014); per-tax price override (VDR-U13-C012); caba flag note only (VDR-U13-C070, VDR-U13-C072). |
| 6 | Validation / constraints | Repartition mirror and totals (VDR-U13-C027, VDR-U13-C028, VDR-U13-C029, VDR-U13-C030, VDR-U13-C031, VDR-U13-C032); group children (VDR-U13-C062, VDR-U13-C063, VDR-U13-C064); group country (VDR-U13-C057); account/tag domains (VDR-U13-C037, VDR-U13-C038). |
| 7 | Roles / permissions | ACL/rules in CAP-U13-10: manager full, others read (VDR-U13-C460, VDR-U13-C469). |
| 8 | Scheduled / automated | NOT APPLICABLE — engine is synchronous; no cron belongs to taxes (see VDR-U13-C477). |
| 9 | Exception / failure | ValidationError messages listed in rows 2 and 6; unknown numeric behaviour flagged (VDR-U13-C088). |
| 10 | Accounting / audit / compliance | Tax lines and base tags feed statutory reports; closing flag and accounts (VDR-U13-C039); change logging only after use (VDR-U13-C068); rounding deltas (VDR-U13-C086). |

### DB reconciliation (config only)
18 taxes, all percent, all sequence 1, none cash-basis (VDR-U13-C083); zero and exempt VAT taxes sit in group WHT 1% (VDR-U13-C082); withholding taxes negative (VDR-U13-C084); repartition rows 36+36 with 12 closing-flagged tax lines; company rounding round_globally, tax_excluded.

### Unknown / Runtime
VDR-U13-C088 · VDR-U13-C087. Cash-basis settlement is a note only (U11/U12).

---

## CAP-U13-02 Fiscal positions and tax/account mapping

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Adapt taxes and accounts on a document to the partner situation (country, VAT presence, zip, state, delivery address), automatically or by manual choice. VDR-U13-C130

### D2 Architecture
`account.fiscal.position` (+ `account.fiscal.position.account`), tax link table `account_fiscal_position_account_tax_rel` VDR-U13-C104, `account.tax.original_tax_ids` (Replaces) VDR-U13-C103, partner company-dependent default VDR-U13-C124, move field VDR-U13-C115, company `domestic_fiscal_position_id` VDR-U13-C099.

### D3 Logic
`_get_fiscal_position`: manual wins VDR-U13-C107 -> no country -> none VDR-U13-C108 -> candidates auto_apply VDR-U13-C109 -> sorted VDR-U13-C110 -> validators VDR-U13-C111 (VDR-U13-C112, VDR-U13-C113) ; EU same-prefix delivery rule VDR-U13-C114. Application: `map_tax` VDR-U13-C102, `map_account` VDR-U13-C105; lines VDR-U13-C119 VDR-U13-C120; price VDR-U13-C121.

State list:
- `active -> archived [write active] (VDR-U13-C129)`
- `document without position -> position computed [partner/shipping/company change] (VDR-U13-C115)`
- `position changed on document with lines -> update prompt [onchange] (VDR-U13-C117)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Partner country matches an auto position -> taxes/accounts mapped on lines (VDR-U13-C109, VDR-U13-C102, VDR-U13-C119). |
| 2 | Reversal/negative | Archive instead of delete; delete blocked when referenced by moves (ondelete restrict) (VDR-U13-C129, VDR-U13-C118); mapped accounts cannot be deleted (VDR-U13-C157). |
| 3 | Multi-company | Company-owned, company-specific tried first (VDR-U13-C110); partner property company-dependent (VDR-U13-C124); parent-of rule (VDR-U13-C469). |
| 4 | Side effects | Tax country on move follows foreign-VAT position (VDR-U13-C123); price adaptation (VDR-U13-C121); foreign tax creation may install localization (VDR-U13-C125). |
| 5 | Configuration/optionality | auto_apply, vat_required, zip/state/country/group criteria (VDR-U13-C090, VDR-U13-C091, VDR-U13-C092); chart template may ship positions (VDR-U13-C126); none shipped by th (VDR-U13-C127). |
| 6 | Validation | zip range (VDR-U13-C093, VDR-U13-C094); foreign VAT rules (VDR-U13-C095, VDR-U13-C096, VDR-U13-C097, VDR-U13-C098); account mapping unique (VDR-U13-C106); document tax country (VDR-U13-C122). |
| 7 | Roles | manager full, internal read (VDR-U13-C463); foreign tax creation manager only (VDR-U13-C125). |
| 8 | Scheduled | NOT APPLICABLE — no job. |
| 9 | Exception/failure | ValidationError messages in row 6; AccessError for non-managers (VDR-U13-C125). |
| 10 | Accounting/compliance | Wrong position changes taxes on posted-to-be documents; document country consistency enforced (VDR-U13-C122). |

### DB reconciliation
0 fiscal positions, no domestic position, default purchase-receipt position unset (VDR-U13-C128).

### Unknown / Runtime
VDR-U13-C131.

---

## CAP-U13-03 Chart of accounts, account types, guards, company chart loading

**Function-ID(s):** MCT-F03 (shared vs per-company chart) for sharing claims; otherwise FUNCTION MAPPING REQUIRED

### D1 Business purpose
Maintain the ledger account list per company (types drive reports/closing), guard integrity (deletion, type/currency changes), allow sharing across a company tree, and create a country chart for a company by loading a template. VDR-U13-C133

### D2 Architecture
`account.account` with `company_ids` M2M VDR-U13-C141 and per-root code in company-dependent `code_store` VDR-U13-C142 VDR-U13-C143; `account.group` prefixes VDR-U13-C168; `account.account.tag` VDR-U13-C173; `account.root` (prefix root, not studied further); loader `account.chart.template` (AbstractModel) driven by `@template` functions, CSV files, `ir.module.module.account_templates` VDR-U13-C207; DB table `account_account_res_company_rel`.

### D3 Logic
Account guards: VDR-U13-C137 VDR-U13-C138 VDR-U13-C147 VDR-U13-C148 VDR-U13-C144 VDR-U13-C156 VDR-U13-C157 VDR-U13-C158; dead check VDR-U13-C159; archive VDR-U13-C160.
Loader flow (`try_loading` -> `_load`): VDR-U13-C177 -> admin check VDR-U13-C179 -> module install VDR-U13-C180 -> context VDR-U13-C181 -> reload detection VDR-U13-C182 -> optional wipe VDR-U13-C183 -> `_get_chart_template_data` VDR-U13-C186 (+ CSV VDR-U13-C187) -> `_pre_reload_data` (reload only) VDR-U13-C197 -> `_pre_load_data` (VDR-U13-C189, VDR-U13-C190, VDR-U13-C191) -> `_load_data` VDR-U13-C193 -> `_post_load_data` VDR-U13-C194 VDR-U13-C195 VDR-U13-C196 -> translations -> group parent sync VDR-U13-C172 -> demo VDR-U13-C201 -> subsidiaries VDR-U13-C202.
Re-running: reload semantics VDR-U13-C198 VDR-U13-C199 VDR-U13-C200; existing data with different template VDR-U13-C184.

State list:
- `company without chart -> chart loaded [try_loading/settings/module install/company create] (VDR-U13-C204, VDR-U13-C205, VDR-U13-C203)`
- `chart loaded (no entries) -> other chart [wipe + load] (VDR-U13-C183)`
- `chart loaded -> same chart reload [reload path] (VDR-U13-C182)`
- `account active -> archived [active=False; no write guard] (VDR-U13-C160)`
- `localization module uninstalled -> company chart_template cleared (VDR-U13-C208)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Settings/localization install -> `try_loading(th)` -> accounts, tax groups, taxes, journals, reconcile models, company defaults (VDR-U13-C177, VDR-U13-C194). |
| 2 | Reversal/negative | Account delete guards (VDR-U13-C156); wipe on chart switch without entries (VDR-U13-C183); unmerge (VDR-U13-C164); reload keeps user data (VDR-U13-C199). |
| 3 | Multi-company | Accounts shared via company_ids (VDR-U13-C141); code per root (VDR-U13-C142); cash accounts single-company (VDR-U13-C147); branches inherit chart (VDR-U13-C202); rule (VDR-U13-C150); groups per root (VDR-U13-C169). |
| 4 | Side effects | Company currency from template (VDR-U13-C189); property defaults for partners/categories (VDR-U13-C195); default taxes on products (VDR-U13-C194); translations; demo (VDR-U13-C201). |
| 5 | Configuration/optionality | force_create, demo (VDR-U13-C200, VDR-U13-C201); code_digits (VDR-U13-C191); template discovery (VDR-U13-C207). |
| 6 | Validation | reconcile/type/off-balance (VDR-U13-C137, VDR-U13-C138); codes (VDR-U13-C146, VDR-U13-C144, VDR-U13-C145); currency (VDR-U13-C152, VDR-U13-C153); type vs journal (VDR-U13-C154, VDR-U13-C155); group overlap/length (VDR-U13-C170, VDR-U13-C171); tag uniqueness (VDR-U13-C174). |
| 7 | Roles | Only system admin loads (VDR-U13-C179); manager edits accounts (VDR-U13-C462). |
| 8 | Scheduled | NOT APPLICABLE — loader is on-demand (no cron). |
| 9 | Exception/failure | Missing tag RedirectWarning (VDR-U13-C209); umbrella template (VDR-U13-C178); non-admin AccessError (VDR-U13-C179); demo errors swallowed (VDR-U13-C201). |
| 10 | Accounting/compliance | Types drive report/closing (VDR-U13-C133, VDR-U13-C135); unaffected earnings (VDR-U13-C176); residual reset on reconcile toggle (VDR-U13-C140). |

### DB reconciliation
Counts and types: VDR-U13-C212 VDR-U13-C214 VDR-U13-C213 VDR-U13-C217; template data VDR-U13-C211; transfer-prefix oddity VDR-U13-C216; unused asset file VDR-U13-C215.

### Unknown / Runtime
VDR-U13-C218 · VDR-U13-C184 (RT) · VDR-U13-C215.

---

## CAP-U13-04 Currencies in accounting and cash rounding

**Function-ID(s):** FUNCTION MAPPING REQUIRED (base currency model hand-off to U01)

### D1 Business purpose
Record each entry in company (base) currency and, when different, the document currency with a rate; keep rounding consistent; offer cash rounding for coin-less cash settlement. VDR-U13-C260

### D2 Architecture
`res.currency`/`res.currency.rate` (base) with account extensions VDR-U13-C221; move `invoice_currency_rate`, `expected_currency_rate` VDR-U13-C234; line `currency_rate`, `amount_currency`, `balance` VDR-U13-C239 VDR-U13-C240; company exchange journal/accounts VDR-U13-C253; `account.cash.rounding` VDR-U13-C243.

### D3 Logic
Rate selection VDR-U13-C226 VDR-U13-C227 VDR-U13-C228; conversion VDR-U13-C230; document currency VDR-U13-C231; rate date VDR-U13-C233; recompute VDR-U13-C235; manual-rate protection at post VDR-U13-C238; cash rounding `_recompute_cash_rounding_lines` VDR-U13-C247 (VDR-U13-C248, VDR-U13-C249).

State list:
- `draft invoice -> rate recomputed [currency/date/company change] (VDR-U13-C235)`
- `rate manually edited -> kept [protecting at post] (VDR-U13-C238)`
- `cash rounding set -> rounding line created/updated/removed [dynamic lines] (VDR-U13-C247)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Foreign invoice: rate at invoice date -> line balance = amount/rate -> posted (VDR-U13-C233, VDR-U13-C240). |
| 2 | Reversal/negative | Sign constraints (VDR-U13-C241); precision cannot be reduced (VDR-U13-C221); refresh rate (VDR-U13-C237). |
| 3 | Multi-company | Rates on root company only (VDR-U13-C228, VDR-U13-C229); company currency fixed after entries (VDR-U13-C219); cash rounding accounts company-dependent (VDR-U13-C245). |
| 4 | Side effects | Multi-currency group auto-toggle (VDR-U13-C225); tax rounding both currencies (VDR-U13-C257); display of taxes in company currency (VDR-U13-C255, VDR-U13-C256). |
| 5 | Configuration | Cash rounding group (VDR-U13-C251); strategies/methods (VDR-U13-C243); live rates optional module (VDR-U13-C262). |
| 6 | Validation | positive rate (VDR-U13-C236); debit xor credit (VDR-U13-C242); rounding > 0 (VDR-U13-C223, VDR-U13-C244); journal/account currency (VDR-U13-C153). |
| 7 | Roles | currency/rate manager only (VDR-U13-C464); cash rounding invoicing (VDR-U13-C252). |
| 8 | Scheduled | NOT APPLICABLE — no rate cron in account (VDR-U13-C262). |
| 9 | Exception | UserError on company currency change (VDR-U13-C219); warning without profit account (VDR-U13-C250). |
| 10 | Accounting/compliance | stored document rate (VDR-U13-C261); exchange accounts (VDR-U13-C253); zero rate rows fallback (VDR-U13-C259). |

### DB reconciliation
VDR-U13-C258; cash rounding rules: 0 rows.

### Unknown / Runtime
VDR-U13-C259 (RT); VDR-U13-C262.

---

## CAP-U13-05 Accounting company settings and period configuration

**Function-ID(s):** PCO-F02 (fiscal year/period configuration) on fiscal-year claims; PCO-F01 on lock-date field claims; others FUNCTION MAPPING REQUIRED

### D1 Business purpose
Per-company accounting parameters: fiscal year end, opening date/entry, lock-date fields, price and rounding defaults, anglo flag, default accounts/taxes, storno, audit trail, cash basis, credit limit feature. VDR-U13-C295

### D2 Architecture
`res.company` fields VDR-U13-C263 VDR-U13-C273; `res.config.settings` related fields VDR-U13-C290; wizard `account.financial.year.op` VDR-U13-C265 VDR-U13-C271; consumers: `_get_sequence_date_range` VDR-U13-C268, resequence VDR-U13-C269.

### D3 Logic
Fiscal year: no model; `compute_fiscalyear_dates` VDR-U13-C266; validity VDR-U13-C264; branch delegation VDR-U13-C267. Lock fields: write validation `_validate_locks` VDR-U13-C276 VDR-U13-C277 VDR-U13-C278; exceptions recreated VDR-U13-C275; tax lock set by closing VDR-U13-C274. Chart defaults VDR-U13-C281 VDR-U13-C282 VDR-U13-C283 VDR-U13-C284; anglo VDR-U13-C279 VDR-U13-C280; cash basis VDR-U13-C285 VDR-U13-C286; storno VDR-U13-C287; audit VDR-U13-C288.

State list:
- `no opening date -> opening date set [wizard]; draft opening move date = opening - 1 day (VDR-U13-C271)`
- `lock date unset -> set [write; validated] (VDR-U13-C275)`
- `hard lock -> removal/decrease refused (VDR-U13-C276)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Admin sets fiscal year end/opening date via onboarding wizard (VDR-U13-C265, VDR-U13-C271). |
| 2 | Reversal/negative | Hard lock irreversible (VDR-U13-C276); cash basis cannot be switched off with caba taxes (VDR-U13-C286); price mode locked (VDR-U13-C014). |
| 3 | Multi-company | Root-delegated fields (VDR-U13-C267); settings per company; `account_fiscal_country_id` (VDR-U13-C291). |
| 4 | Side effects | Prefix change renumbers accounts (VDR-U13-C283); category defaults (VDR-U13-C282); sequence ranges (VDR-U13-C268, VDR-U13-C296). |
| 5 | Configuration | Anglo, storno, audit trail, autopost, credit limit (VDR-U13-C279, VDR-U13-C287, VDR-U13-C288, VDR-U13-C289, VDR-U13-C290); onboarding text vs fields (VDR-U13-C270). |
| 6 | Validation | last day (VDR-U13-C264); locks (VDR-U13-C277, VDR-U13-C278). |
| 7 | Roles | settings need accounting manager; ACL see CAP-U13-10 (no company-field-specific ACL read). |
| 8 | Scheduled | NOT APPLICABLE for settings; autopost cron belongs to U11 (VDR-U13-C476). |
| 9 | Exception | UserError/RedirectWarning on locks (VDR-U13-C276, VDR-U13-C277). |
| 10 | Accounting/compliance | Lock dates protect closed periods (engine U11); tax lock date semantics (VDR-U13-C274). |

### DB reconciliation
VDR-U13-C293 VDR-U13-C294.

### Unknown / Runtime
VDR-U13-C297 · VDR-U13-C296.

---

## CAP-U13-06 Partner accounting properties and defaults

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Per-company partner defaults used when documents are created: control accounts, fiscal position, payment terms, credit control, sending preferences, trust and autopost. VDR-U13-C316

### D2 Architecture
`res.partner` extension in `account/models/partner.py`: VDR-U13-C298 VDR-U13-C299 VDR-U13-C300 VDR-U13-C304 VDR-U13-C308 VDR-U13-C309 VDR-U13-C310 VDR-U13-C311; company-dependent storage VDR-U13-C314; commercial sync VDR-U13-C301; chart-load defaults VDR-U13-C303.

### D3 Logic
Account resolution for term lines: VDR-U13-C302; credit/debit totals VDR-U13-C307; credit-limit visibility VDR-U13-C305; parent change guard VDR-U13-C312; delete guard VDR-U13-C313. Credit-limit enforcement: VDR-U13-C306.

State list:
- `partner created -> defaults from ir.default [chart load/settings] (VDR-U13-C303)`
- `partner re-parented -> lines recommercialised [write] (VDR-U13-C312)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Partner defaults feed invoice term line account (VDR-U13-C302). |
| 2 | Reversal/negative | Delete refused when used (VDR-U13-C313); re-parent refused on VAT mismatch (VDR-U13-C312). |
| 3 | Multi-company | Fields company-dependent (VDR-U13-C314); `credit` totals within root tree (VDR-U13-C307). |
| 4 | Side effects | Commercial fields propagate to contacts (VDR-U13-C301); chart load defaults (VDR-U13-C303, VDR-U13-C317). |
| 5 | Configuration | Credit limit feature (VDR-U13-C305, VDR-U13-C290); sending/format (VDR-U13-C310). |
| 6 | Validation | domains on account types (VDR-U13-C298, VDR-U13-C299); ondelete restrict. |
| 7 | Roles | credit fields visible to invoicing/readonly (VDR-U13-C304). |
| 8 | Scheduled | NOT APPLICABLE. |
| 9 | Exception | UserError texts (VDR-U13-C312, VDR-U13-C313). |
| 10 | Accounting/compliance | Control account defaults decide ledger posting (VDR-U13-C302). |

### DB reconciliation
VDR-U13-C315

### Unknown / Runtime
VDR-U13-C306 · VDR-U13-C317.

---

## CAP-U13-07 Analytic distribution on journal items (account side)

**Function-ID(s):** FUNCTION MAPPING REQUIRED (analytic model: U02)

### D1 Business purpose
Allocate a journal item to analytic accounts by percentage, enforce plan applicability, and keep analytic lines in step with posted items. VDR-U13-C350

### D2 Architecture
`analytic.mixin` JSON field on `account.move.line` VDR-U13-C318 VDR-U13-C320; `account.analytic.line` extended VDR-U13-C339; plan applicability extensions VDR-U13-C326 VDR-U13-C327; distribution model extensions VDR-U13-C325.

### D3 Logic
Default: VDR-U13-C323 (VDR-U13-C324); validate: VDR-U13-C329 VDR-U13-C330 (VDR-U13-C331); has_invalid VDR-U13-C334; post: VDR-U13-C335 -> VDR-U13-C336 -> VDR-U13-C337 VDR-U13-C338 VDR-U13-C340; edit: VDR-U13-C341 VDR-U13-C342; analytic line edits VDR-U13-C344 VDR-U13-C345; tax lines VDR-U13-C347.

State list:
- `draft line -> no analytic lines (VDR-U13-C342)`
- `draft -> posted [post] -> analytic lines created (VDR-U13-C335)`
- `posted + distribution edit -> analytic lines deleted and recreated (VDR-U13-C341)`
- `analytic line edited/deleted -> distribution recomputed (VDR-U13-C344)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Distribution set (or defaulted) -> post -> analytic lines (VDR-U13-C323, VDR-U13-C335). |
| 2 | Reversal/negative | Cascade deletion (VDR-U13-C343); recompute on analytic line delete (VDR-U13-C344). |
| 3 | Multi-company | analytic line company; applicability per company (VDR-U13-C328). |
| 4 | Side effects | Analytic lines carry journal, partner, product (VDR-U13-C339); profitability classification (account analytic line model not studied in depth). |
| 5 | Configuration | Precision VDR-U13-C322; plans/rules (VDR-U13-C349). |
| 6 | Validation | mandatory 100% (VDR-U13-C330); account match (VDR-U13-C346). |
| 7 | Roles | ACL (VDR-U13-C348). |
| 8 | Scheduled | NOT APPLICABLE. |
| 9 | Exception | ValidationError/RedirectWarning on missing distribution (see `_validate_analytic_distribution`, VDR-U13-C336). |
| 10 | Accounting/compliance | Rounding spread (VDR-U13-C338); bypass risk (VDR-U13-C333, VDR-U13-C332). |

### DB reconciliation
VDR-U13-C349

### Unknown / Runtime
VDR-U13-C351 · VDR-U13-C333.

---

## CAP-U13-08 Thai localization (`l10n_th`) — Community only

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Provide a Thai chart, VAT and withholding taxes with report grids, Thai tax invoice layout, partner branch label and Thai QR payment support. Scope statement: Community module only; nothing from `Extra_Thailand` was opened or used. VDR-U13-C357 VDR-U13-C393

### D2 Architecture
Manifest VDR-U13-C352 VDR-U13-C355; template VDR-U13-C358 VDR-U13-C359; CSVs (accounts 144 rows, taxes 18, groups 5, asset file unused) VDR-U13-C362 VDR-U13-C369; report XML VDR-U13-C370 VDR-U13-C373 VDR-U13-C374; overrides: VDR-U13-C376 VDR-U13-C379 VDR-U13-C380 VDR-U13-C381.

### D3 Logic
Conditional behaviours: invoice document selection when company fiscal country TH VDR-U13-C376; bank QR rules only for country TH VDR-U13-C382 VDR-U13-C384 VDR-U13-C385; commercial invoice domain VDR-U13-C378; branch label VDR-U13-C380. What changes core behaviour: VDR-U13-C392. Template quirks: cash-basis flag VDR-U13-C360, surcharge tags unused VDR-U13-C375, no fiscal positions/groups VDR-U13-C390, no e-invoice format VDR-U13-C389.

State list:
- `module installed -> chart template th loaded on company [auto-install flow] (VDR-U13-C205)`
- `bank account TH + proxy type set -> QR eligible [constraint/validation] (VDR-U13-C382)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Thai invoice printed with Tax Invoice title + branch; VAT/WHT taxes tag base and tax lines to report grids (VDR-U13-C377, VDR-U13-C362). |
| 2 | Reversal/negative | Refund distribution lines mirror (VDR-U13-C362); WHT negative taxes (VDR-U13-C366). |
| 3 | Multi-company | Behaviour decided per company fiscal country and per bank country (VDR-U13-C376, VDR-U13-C386); template data written for loading company (VDR-U13-C359). |
| 4 | Side effects | Cash-basis switch on (VDR-U13-C360); stock valuation account passed (VDR-U13-C361); post-install tag preservation (VDR-U13-C356). |
| 5 | Configuration/optionality | auto-install, demo (VDR-U13-C352, VDR-U13-C388). |
| 6 | Validation | 13-digit tax id, 10-digit mobile (VDR-U13-C382); print guard (VDR-U13-C379). |
| 7 | Roles | none declared by the module (VDR-U13-C392); ACL inherited from account. |
| 8 | Scheduled | NOT APPLICABLE — no cron (VDR-U13-C477). |
| 9 | Exception | UserError (commercial print), ValidationError (QR proxy), QR error messages (VDR-U13-C387). |
| 10 | Accounting/compliance | Grid mapping, WHT accounts, report formulas (VDR-U13-C371, VDR-U13-C372); statutory conformity unknown (VDR-U13-C394). |

### DB reconciliation
VDR-U13-C391 VDR-U13-C390 VDR-U13-C083 VDR-U13-C212

### Unknown / Runtime
VDR-U13-C394 · VDR-U13-C375 · runtime rendering of Thai layout (RT, not executed).

---

## CAP-U13-09 E-invoicing, payment QR and location number

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Breadth study: framework for per-invoice electronic documents with queueing and cancellation; send-time export/import of UBL/CII formats; EMV QR payload; GLN field. VDR-U13-C418 VDR-U13-C456

### D2 Architecture
`account.edi.format` / `account.edi.document` VDR-U13-C395 VDR-U13-C397; journal selection VDR-U13-C412; move extension VDR-U13-C400; UBL/CII abstract builders `account.edi.common`, `account.edi.ubl`, `account.edi.cii`, concrete `account.edi.xml.*` VDR-U13-C422; partner format/EAS fields VDR-U13-C419 VDR-U13-C437; tax fields VDR-U13-C436; QR VDR-U13-C446; GLN VDR-U13-C444.

### D3 Logic (trigger points, validation, exports, failure)
- Post-time framework: VDR-U13-C400 -> job preparation VDR-U13-C404 -> processing VDR-U13-C402 -> cron VDR-U13-C406 (VDR-U13-C407) -> cancel flow VDR-U13-C403 VDR-U13-C410 VDR-U13-C409 VDR-U13-C408.
- Send-time exporter: partner format (VDR-U13-C421, VDR-U13-C420) -> need test VDR-U13-C423 -> before-PDF export VDR-U13-C424 -> constraints VDR-U13-C433 VDR-U13-C434 VDR-U13-C432 VDR-U13-C431 -> after-PDF: facturx embed VDR-U13-C425 VDR-U13-C426, UBL embed VDR-U13-C427 -> link VDR-U13-C428.
- Import: VDR-U13-C440 VDR-U13-C441 VDR-U13-C442.
- QR: VDR-U13-C450 VDR-U13-C447 VDR-U13-C448 VDR-U13-C449 VDR-U13-C451.

State list (framework document):
- `(none) -> to_send [post, applicable format] (VDR-U13-C400)`
- `to_send -> sent [job success]; to_send -> to_send with error [job failure; blocking level default error] (VDR-U13-C402)`
- `sent -> to_cancel [button_cancel / request cancellation] (VDR-U13-C409, VDR-U13-C410)`
- `to_cancel -> cancelled [cancel success; move reset to draft then cancelled] (VDR-U13-C403)`
- `to_cancel -> sent [abandon request] (VDR-U13-C409)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Send & Print: partner format required -> builder -> XML linked; framework path only when a concrete format exists (VDR-U13-C424, VDR-U13-C428, VDR-U13-C399). |
| 2 | Reversal/negative | EDI cancellation, abandon, reset guard (VDR-U13-C409, VDR-U13-C408); document delete on journal change (VDR-U13-C412). |
| 3 | Multi-company | Jobs batched per company (VDR-U13-C404); partner format company-dependent (VDR-U13-C310); company Peppol alerts (VDR-U13-C429). |
| 4 | Side effects | Attachments, PDF embedding (VDR-U13-C415, VDR-U13-C427, VDR-U13-C425); superuser attachment creation (VDR-U13-C428); mail waits for documents (VDR-U13-C411). |
| 5 | Configuration | Format list/country mapping (VDR-U13-C418); cron inactive (VDR-U13-C417); config parameter (VDR-U13-C443). |
| 6 | Validation | Tax structure (VDR-U13-C431), line tax (VDR-U13-C432), CII/BIS3 rules (VDR-U13-C433, VDR-U13-C434), endpoint (VDR-U13-C438), uniqueness (VDR-U13-C396). |
| 7 | Roles | EDI ACL (VDR-U13-C416). |
| 8 | Scheduled | EDI web-service cron daily/20 jobs, inactive (VDR-U13-C406, VDR-U13-C417); send-invoices cron (VDR-U13-C475). |
| 9 | Exception/failure | Errors become titled list + fallback PDF (VDR-U13-C424, VDR-U13-C482); LockError skip (VDR-U13-C405); attach delete/resequence guards (VDR-U13-C413, VDR-U13-C414). |
| 10 | Accounting/compliance | No Thai format (VDR-U13-C389); tax category codes (VDR-U13-C435); embedded Factur-X risk (VDR-U13-C454). |

### DB reconciliation
VDR-U13-C417 VDR-U13-C443; installed state of the five modules confirmed; `account_peppol` not installed; `base_vat` not installed (see section 12).

### Unknown / Runtime
VDR-U13-C455 · VDR-U13-C454 · actual XML content not generated (RT) · PINT layers and country format files not analysed field-by-field (breadth only).

---

## CAP-U13-10 Roles, record rules, ACL, data scope, exceptions, scheduled jobs

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose
Who may read/change taxes, accounts, fiscal positions, currencies; how multi-company scope applies; what runs on a schedule. VDR-U13-C483

### D2 Architecture
Groups VDR-U13-C457 VDR-U13-C458 VDR-U13-C459; ACL CSV rows VDR-U13-C460 VDR-U13-C461 VDR-U13-C462 VDR-U13-C463 VDR-U13-C464 VDR-U13-C465 VDR-U13-C466 VDR-U13-C467 VDR-U13-C468; global rules VDR-U13-C469 VDR-U13-C470; company checks VDR-U13-C471 VDR-U13-C472; crons VDR-U13-C475 VDR-U13-C476.

### D3 Logic
ACL gate (model access by group) -> record rule (company parent-of) -> `_check_company_auto` domains -> model constraints. Elevated reads: VDR-U13-C473. Admin-only operations: VDR-U13-C474. Failure catalogue: VDR-U13-C480 VDR-U13-C481 VDR-U13-C482.

State list (jobs):
- `send-invoices cron: active daily (VDR-U13-C477)`
- `autopost cron: active daily (engine U11) (VDR-U13-C476)`
- `EDI queue cron: inactive until a web-service format is created (VDR-U13-C406, VDR-U13-C417)`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Manager edits taxes/accounts; internal users read (VDR-U13-C460, VDR-U13-C462). |
| 2 | Reversal | Deletion guards in CAP-U13-01/03 (VDR-U13-C480). |
| 3 | Multi-company | Parent-of rules (VDR-U13-C469, VDR-U13-C150); rate rule (VDR-U13-C470); branch inheritance (VDR-U13-C471). |
| 4 | Side effects | Sudo uniqueness check (VDR-U13-C473). |
| 5 | Configuration | Cash rounding group (VDR-U13-C459); group chain (VDR-U13-C457). |
| 6 | Validation | see CAP-U13-01/02/03. |
| 7 | Roles / ACL / rules (declared vs DB) | Declared rows above; DB confirmed (VDR-U13-C478, VDR-U13-C479). |
| 8 | Scheduled | VDR-U13-C475, VDR-U13-C476, VDR-U13-C406; DB states VDR-U13-C477. |
| 9 | Exception | VDR-U13-C480, VDR-U13-C481, VDR-U13-C482. |
| 10 | Security/compliance | Chart loading admin only (VDR-U13-C474); localisation adds no groups (VDR-U13-C392). |

### DB reconciliation
VDR-U13-C478 VDR-U13-C479 VDR-U13-C477. ACL counts per model were read from `ir_model_access` joined to `ir_model`/`res_groups`; rules from `ir_rule`; crons from `ir_cron`/`ir_model_data`. Analytic and project/stock rules also present in DB belong to other units.

### Unknown / Runtime
VDR-U13-C484.

---

## 11. Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U13-C001 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:85 | Percentage Tax Included | FACT | always | - | amount_type selection offers group, fixed, percent and division (labelled Percentage Tax Included); default is percent. | N-U13-002 |
| VDR-U13-C002 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:18 | TYPE_TAX_USE = [ | FACT | always | - | type_tax_use is one of sale, purchase, none; none means the tax cannot be used by itself but can be a child inside a group (help text of the field). | N-U13-003 |
| VDR-U13-C003 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:132 | order in which the tax lines | FACT | always | - | sequence (default 1) defines the order in which taxes are applied; model _order is sequence,id. | N-U13-004 |
| VDR-U13-C004 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:895 | def _flatten_taxes_and_sort_them | FACT | always | - | Group taxes are flattened: a group is replaced by its children sorted by sequence, id; the group's own sequence positions the children, and a map child to parent group is kept. | N-U13-004 |
| VDR-U13-C005 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:923 | def _batch_for_taxes_computation | FACT | always | - | Taxes are batched (same amount_type, same price_include unless special mode, same include_base_amount) so that price-included percent or division taxes of one batch are computed together. | N-U13-006 |
| VDR-U13-C006 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1257 | eval_tax_amount(tax._eval_tax_amount_fixed_amount | FACT | always | - | Evaluation order in _get_tax_details: first fixed taxes in reverse order, then price-included taxes in reverse order (line 1262), then price-excluded taxes in normal order (line 1267). | N-U13-006 |
| VDR-U13-C007 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1262 | eval_tax_amount(tax._eval_tax_amount_price_included, tax) | FACT | always | - | Price-included taxes are evaluated by iterating the sorted taxes in reverse, after fixed taxes have been evaluated. | N-U13-006 |
| VDR-U13-C008 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1111 | to_price_excluded_factor | FACT | tax price-included, amount_type percent | - | Price-included percent tax: amount = raw_base * (1/(1+sum of batch percents)) * percent/100 (factor forced to 0 when total percentage is -100%). | N-U13-007 |
| VDR-U13-C009 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1134 | incl_base_multiplicator | FACT | tax price-excluded, amount_type division | - | Price-excluded division tax: amount = raw_base * percent/100 / (1 - sum of batch percents) with multiplicator 1 when batch total is 100%. | N-U13-007 |
| VDR-U13-C010 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1095 | evaluation_context['quantity'] * self.amount | FACT | amount_type fixed | - | Fixed tax amount = sign(price_unit) * quantity * amount, independent of the price magnitude. | N-U13-007 |
| VDR-U13-C011 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1115 | return raw_base * self.amount / 100.0 | FACT | amount_type division, price-included | - | Price-included division tax: amount = raw_base * percent/100 (line 1115). | N-U13-007 |
| VDR-U13-C012 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:327 | tax.company_price_include == 'tax_included' | FACT | always | - | price_include is true when price_include_override is tax_included, or when the company default is tax_included and no override is set. | N-U13-005 |
| VDR-U13-C013 | FUNCTION MAPPING REQUIRED | account/models/company.py:275 | default='tax_excluded', | FACT | always | - | Company field account_price_include is required with default tax_excluded. | N-U13-005 |
| VDR-U13-C014 | FUNCTION MAPPING REQUIRED | account/models/company.py:328 | Cannot change Price Tax computation method | FACT | company has any journal item | - | Constraint forbids changing account_price_include once the company (or its children) has accounting entries (_existing_accounting). | N-U13-025 |
| VDR-U13-C015 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:148 | Affect Base of Subsequent Taxes | FACT | always | - | include_base_amount (default False) makes taxes of higher sequence computed on base plus this tax; is_base_affected (default True) lets a later tax opt out of being affected. | N-U13-008 |
| VDR-U13-C016 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:723 | self.include_base_amount = True | FACT | UI edit | - | Onchange of price_include sets include_base_amount to True. | N-U13-008 |
| VDR-U13-C017 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:976 | def _propagate_extra_taxes_base | FACT | always | - | _propagate_extra_taxes_base adds the amount of one tax as extra base to taxes before/after it depending on price_include, include_base_amount, is_base_affected and special mode. | N-U13-008 |
| VDR-U13-C018 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1204 | elif special_mode == 'total_included': | FACT | always | - | special_mode False, total_excluded or total_included changes the starting base interpretation; has_negative_factor taxes are forced price-excluded. | N-U13-006 |
| VDR-U13-C019 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1763 | price_unit_after_discount | FACT | always | - | Discount percent is applied to the unit price before the tax computation; quantity and discount come from the base line. | N-U13-010 |
| VDR-U13-C020 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1788 | 'raw_total_excluded': taxes_computation['total_excluded'] / rate | FACT | document currency differs from company currency | - | Amounts are computed in document currency and converted to company currency by dividing by the line rate; company-currency amounts are rounded at this stage only for round_per_line. | N-U13-010 |
| VDR-U13-C021 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1182 | rounding_method == 'round_per_line' | FACT | rounding method round_per_line | - | With round_per_line each tax amount (and the raw base) is rounded with currency rounding at computation time. | N-U13-009 |
| VDR-U13-C022 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1762 | company.tax_calculation_rounding_method | FACT | always | - | Rounding method defaults to the company field tax_calculation_rounding_method when the caller passes none. | N-U13-009 |
| VDR-U13-C023 | FUNCTION MAPPING REQUIRED | account/models/company.py:132 | default='round_globally', | FACT | always | - | Company tax_calculation_rounding_method selection (round_globally labelled Round per Tax, round_per_line) defaults to round_globally. | N-U13-009 |
| VDR-U13-C024 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2292 | self._round_tax_details_tax_amounts(base_lines, company) | FACT | always | - | _round_base_lines_tax_details first rounds raw values per line, applies manual amounts, then performs document-level global rounding of tax amounts and bases. | N-U13-009 |
| VDR-U13-C025 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1840 | def _distribute_delta_amount_smoothly | FACT | always | - | Rounding deltas are distributed in smallest-currency units across lines/taxes proportionally to absolute factors, remainder going to the biggest factors first. | N-U13-009 |
| VDR-U13-C026 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1913 | Round base + tax, then subtract | FACT | mixed mode, price-included | - | In mixed mode price-included groups round base+tax then derive the base; price-excluded groups round base and tax independently. | N-U13-009 |
| VDR-U13-C027 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:557 | exactly one line for the base | FACT | always | - | Invoice and refund distributions must each contain exactly one base line. | N-U13-017 |
| VDR-U13-C028 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:574 | should have the same number of | FACT | always | - | Invoice and refund distribution must have the same number of lines. | N-U13-017 |
| VDR-U13-C029 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:578 | at least one tax repartition line | FACT | amount_type not group-without-lines | - | Both distributions need at least one tax-type line (groups with no repartition lines at all are exempt). | N-U13-017 |
| VDR-U13-C030 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:585 | same percentages, in the same order | FACT | always | - | Invoice and refund lines are paired by order and must have the same repartition_type and factor_percent. | N-U13-017 |
| VDR-U13-C031 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:591 | total factor (+) equals to 100 | FACT | always | - | Sum of positive tax factors must equal 100% (precision 2 digits). | N-U13-018 |
| VDR-U13-C032 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:594 | total factor (-) equals to 100 | FACT | only when negative factors exist | - | If any negative tax factor exists the negatives must total -100% (reverse-charge pattern). | N-U13-018 |
| VDR-U13-C033 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:509 | has_negative_factor = bool | FACT | always | - | has_negative_factor is true when an invoice tax repartition line has a negative factor; such taxes yield an extra reverse-charge tax data entry. | N-U13-013 |
| VDR-U13-C034 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1230 | reverse_charge_taxes_data[tax.id] = { | FACT | tax with negative factor | - | For negative-factor taxes a second tax_data with is_reverse_charge True and negated amount is generated alongside the normal one. | N-U13-013 |
| VDR-U13-C035 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:492 | Command.create({'document_type': 'invoice', 'repartition_type': 'base' | FACT | tax created without lines | - | When a tax is created without distribution lines default base and tax lines (no tags, no account, 100%) are created for both invoice and refund. | N-U13-011 |
| VDR-U13-C036 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5326 | Factor to apply on the account | FACT | always | - | Repartition line carries factor_percent (default 100), repartition_type base or tax, document_type invoice or refund, optional account, tag_ids, sequence, use_in_tax_closing. | N-U13-011 |
| VDR-U13-C037 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5333 | 'asset_receivable', 'liability_payable', 'off_balance' | FACT | always | - | Repartition account domain excludes receivable, payable and off-balance accounts. | N-U13-023 |
| VDR-U13-C038 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5336 | domain=[('applicability', '=', 'taxes')] | FACT | always | - | Repartition tag_ids are limited to tags of applicability taxes; tag domain further limits by fiscal country and foreign VAT countries of the company (lines 5349-5353). | N-U13-023 |
| VDR-U13-C039 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5360 | rep_line.account_id.internal_group not in ('income', 'expense') | FACT | always | - | use_in_tax_closing defaults true for tax-type lines whose account is not income or expense group (precomputed, editable). | N-U13-011 |
| VDR-U13-C040 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5371 | self.account_id = None | FACT | UI edit | - | Onchange of repartition_type to base clears the account. | N-U13-011 |
| VDR-U13-C041 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2394 | repartition_lines_field = 'refund_repartition_line_ids' | FACT | document is refund | - | Refund base lines use the refund repartition lines; invoice lines use invoice repartition lines. | N-U13-013 |
| VDR-U13-C042 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2438 | or base_line['account_id'] | FACT | repartition has no account | - | If a tax repartition line has no account the tax amount goes to the account of the base line. | N-U13-012 |
| VDR-U13-C043 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2412 | if not tax_data['is_reverse_charge'] and (include_caba_tags | FACT | tax exigible on invoice (or caba tags included) | - | Base repartition tags are added to the base line tags; product account_tag_ids are added too; cash-basis taxes only contribute tags when include_caba_tags is set. | N-U13-012 |
| VDR-U13-C044 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2444 | Distribute the delta on the repartition | FACT | always | - | Rounding differences between a tax amount and the sum of its repartition amounts are spread over repartition lines using the same smooth distribution. | N-U13-012 |
| VDR-U13-C045 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2331 | 'tax_repartition_line_id': tax_rep.id, | FACT | always | - | Tax journal lines are keyed by partner, currency, analytic distribution, account, tax_ids, repartition line, group tax and tags so that equal keys merge. | N-U13-014 |
| VDR-U13-C046 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2337 | if tax.analytic or not tax_rep.use_in_tax_closing | FACT | always | - | Analytic distribution is copied to a tax line only when the tax has the analytic flag or the repartition line is not used in tax closing. | N-U13-014 |
| VDR-U13-C047 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3115 | Remove tax lines having a zero | FACT | always | - | Aggregated tax lines whose amount_currency and balance are zero are dropped unless the key carries __keep_zero_line. | N-U13-014 |
| VDR-U13-C048 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3128 | tax_lines_to_update = [] | FACT | always | - | _prepare_tax_lines compares computed keys with existing tax lines and returns lists to add, update or delete. | N-U13-014 |
| VDR-U13-C049 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:4975 | def compute_all | FACT | always | - | compute_all is the legacy single-line API that wraps the new engine and returns total_excluded, total_included, total_void, base_tags and per-repartition tax dictionaries. | N-U13-001 |
| VDR-U13-C050 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5029 | 'force_price_include' in self.env.context | FACT | context flag | - | compute_all maps context force_price_include to special mode total_included or total_excluded and handle_price_include False to total_excluded. | N-U13-006 |
| VDR-U13-C051 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2823 | def tax_group_grouping_function | FACT | always | - | Document tax totals are aggregated per tax group of the involved taxes. | N-U13-015 |
| VDR-U13-C052 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2830 | values['grouping_key'].sequence | FACT | always | - | Tax groups in totals are ordered by group sequence then id. | N-U13-015 |
| VDR-U13-C053 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2873 | tax_group.preceding_subtotal or | FACT | always | - | Group field preceding_subtotal names the subtotal row the group is displayed after; default label is Untaxed Amount. | N-U13-015 |
| VDR-U13-C054 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1843 | move.tax_totals = self.env['account.tax']._get_tax_totals_summary( | FACT | invoices and receipts | - | Invoice tax_totals is computed from rounded base lines with the move cash rounding passed in; non-invoice moves get None. | N-U13-015 |
| VDR-U13-C055 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:39 | Tax current account used as a | FACT | always | - | Tax group has tax_payable_account_id, tax_receivable_account_id and advance_tax_payment_account_id used as counterparts of the tax closing entry. | N-U13-016 |
| VDR-U13-C056 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:68 | group.company_id.account_fiscal_country_id or | FACT | always | - | Tax group country defaults (stored, editable) to the company fiscal country else company country. | N-U13-021 |
| VDR-U13-C057 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:265 | tax group must have the same | FACT | tax group has a country | - | A tax group having a country must have the same country as the tax that uses it. | N-U13-021 |
| VDR-U13-C058 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:319 | ('country_id', '=', False), | FACT | tax group empty or mismatched | - | If a tax has no tax group (or country/company mismatch) it is assigned the first group of the same country, else the first group without country; groups are searched in sequence,id order. | N-U13-027 |
| VDR-U13-C059 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:160 | required=True, precompute=True, | FACT | always | - | tax_group_id is required on the tax (computed, stored, editable). | N-U13-027 |
| VDR-U13-C060 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:301 | tax.company_id.account_fiscal_country_id or tax.company_id.country_id | FACT | always | - | Tax country (required, stored) defaults to the company fiscal country else company country. | N-U13-035 |
| VDR-U13-C061 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:249 | Tax names must be unique | FACT | type_tax_use not none | - | Names must be unique per company tree, type_tax_use, tax_scope and country (checked at create and when those fields change). | N-U13-019 |
| VDR-U13-C062 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:606 | application scope of taxes in a | FACT | amount_type group | - | Children must have type_tax_use none or equal to the group's, and tax_scope empty or equal. | N-U13-020 |
| VDR-U13-C063 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:611 | Nested group of taxes are not | FACT | amount_type group | - | A child of a group tax may not itself be a group. | N-U13-020 |
| VDR-U13-C064 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:600 | Recursion found for tax | FACT | amount_type group | - | Cycles through children_tax_ids are rejected. | N-U13-020 |
| VDR-U13-C065 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:626 | You can't change the company of | FACT | tax already on journal items | - | Changing company_id of a tax is refused when journal items referencing it exist outside the new company tree. | N-U13-022 |
| VDR-U13-C066 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5133 | cannot delete taxes that are currently | FACT | tax is_used | - | Deleting a used tax raises ValidationError advising archival. | N-U13-022 |
| VDR-U13-C067 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:372 | ('account_move_line_ids', '!=', False), | FACT | always | - | is_used is true when the tax appears on any journal item or reconcile model line (plus taxes reported by the legacy hook for custom modules). | N-U13-024 |
| VDR-U13-C068 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:470 | only log the modification of the | FACT | tax is used | - | Chatter logging of tracked fields and formatted repartition changes happens only when the tax is already used. | N-U13-024 |
| VDR-U13-C069 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:125 | Set active to false to hide | INFERENCE | always | - | Taxes are archived through the active field; the model write override (lines 669-670) only sanitises values and no active-specific constraint was found, so archival of a used tax is not blocked by code in this module. | N-U13-024 |
| VDR-U13-C070 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:167 | default='on_invoice', | FACT | always | - | tax_exigibility selection on_invoice (default) or on_payment; with on_payment the tax lines are posted to cash_basis_transition_account_id until payment (note only, engine in U11/U12). | N-U13-026 |
| VDR-U13-C071 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:275 | cash basis transition account needs to | FACT | tax_exigibility on_payment, not during chart load | - | On_payment taxes require a reconcilable transition account except when context chart_template_load is set. | N-U13-026 |
| VDR-U13-C072 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5380 | return self.tax_id.cash_basis_transition_account_id | FACT | tax on_payment and no caba_no_transition_account context | - | For on_payment taxes the target tax account is the transition account instead of the repartition account. | N-U13-026 |
| VDR-U13-C073 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:711 | self.invoice_label = "{0:.4g}%".format(self.amount) | FACT | UI edit percent or division | - | Onchange of amount fills invoice_label with the percentage when label is empty. | N-U13-001 |
| VDR-U13-C074 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:283 | dynamic_fiscal_position_id | FACT | UI context | - | Tax name_search can be filtered by fiscal position through context keys (dynamic_fiscal_position_id, search_default_domestictax, hide_original_tax_ids). | N-U13-030 |
| VDR-U13-C075 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1342 | def _adapt_price_unit_to_another_taxes | FACT | all original taxes price-included | - | Price unit is adapted to new taxes only when all original taxes are price-included: price is first brought to total_excluded then price-included delta of new taxes is added. | N-U13-030 |
| VDR-U13-C076 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5095 | It goes through the company hierarchy | FACT | multi-company hierarchy | - | _filter_taxes_by_company walks from the company up through its parents until a match is found. | N-U13-028 |
| VDR-U13-C077 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:973 | tax_ids = filtered_taxes_id or account_taxes | FACT | sale document line | - | Sale line default taxes come from the product taxes_id (company-filtered) else the account default taxes of type sale; purchase symmetric with supplier_taxes_id. | N-U13-028 |
| VDR-U13-C078 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:991 | tax_ids = self.move_id.fiscal_position_id.map_tax(tax_ids) | FACT | document has fiscal position | - | After default taxes are chosen the fiscal position maps them (see CAP-U13-02). | N-U13-030 |
| VDR-U13-C079 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:400 | tax._validate_repartition_lines() | FACT | account_edi_ubl_cii installed, UBL/CII export | - | Electronic export first calls the repartition validation of each line tax and converts a failure into a ValidationError naming the tax. | N-U13-017 |
| VDR-U13-C080 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1663 | 'analytic_distribution': load('analytic_distribution', None), | FACT | always | - | A base line dictionary carries product, uom, taxes, price_unit, quantity, discount, currency, rate, sign, is_refund, partner, account and analytic distribution plus manual overrides. | N-U13-001 |
| VDR-U13-C081 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2256 | Apply 'manual_tax_amounts' | FACT | base line has manual_tax_amounts | - | User-entered manual tax or base amounts override the computed ones after raw rounding (for down payments, combo, global discount). | N-U13-009 |
| VDR-U13-C082 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:10 | tax_input_vat_0 | OBSERVATION | DB company chart th loaded | - | The template rows for 0% and exempt VAT taxes give no tax_group_id; in the DB all four (0% and 0% EXEMPT, sale and purchase) are assigned the group named WHT 1% (id 1) by the fallback, while 7% VAT uses group VAT 7%. | N-U13-031 |
| VDR-U13-C083 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:22 | tax_output_vat_exempted | OBSERVATION | DB company chart th loaded | - | DB holds 18 taxes, all percent type, all sequence 1, all on_invoice exigibility, none with include_base_amount, none with cash_basis transition account; rounding round_globally, price tax_excluded. | N-U13-025 |
| VDR-U13-C084 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:58 | tax_wht_income_1 | OBSERVATION | DB company chart th loaded | - | Withholding taxes are negative percentages (-1,-2,-3,-5); purchase ones post tax to liability accounts without closing flag, sale ones (price_include_override tax_excluded) post to an asset account; DB repartition rows: 36 invoice and 36 refund lines, 12 tax lines flagged for tax closing. | N-U13-011 |
| VDR-U13-C085 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:902 | PLZ KEEP BOTH METHODS CONSISTENT | FACT | always | - | Engine docstrings state that the same computation exists in client-side code (account_tax.js) and both must be kept consistent, so that the form preview, the server and exports agree. | N-U13-036 |
| VDR-U13-C086 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1904 | The delta in term of tax | INFERENCE | round_globally | - | Docstring example: two lines each rounded to 33.79 tax versus 67.57 on the whole document gives a -0.01 delta that is redistributed, so a line-level tax can differ by one currency unit from line computed in isolation (lines 1896-1908). | N-U13-032 |
| VDR-U13-C087 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:909 | return tax.sequence, tax.id or None | INFERENCE | DB company chart th loaded | - | All 18 DB taxes have sequence 1, so the evaluation order of taxes combined on one line is decided by record identifier (sort key sequence then id); results are order-independent for percent taxes that neither affect the base nor are affected, but untested for other combinations. | N-U13-033 |
| VDR-U13-C088 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | runtime | RT | UNKNOWN - EVIDENCE INSUFFICIENT: numeric results (rounding deltas, totals) for combined Thai taxes such as 7% VAT with a withholding tax on one line were not executed; resolve by an AWT runtime test with representative invoices. | N-U13-034 |
| VDR-U13-C089 | FUNCTION MAPPING REQUIRED | account/models/partner.py:27 | _name = 'account.fiscal.position' | FACT | always | - | Fiscal position is a company-scoped record (required company_id, ordered by sequence, active flag) with account mapping lines, taxes, notes and detection criteria. | N-U13-050 |
| VDR-U13-C090 | FUNCTION MAPPING REQUIRED | account/models/partner.py:52 | auto_apply = fields.Boolean | FACT | always | - | auto_apply (Detect Automatically) makes a position eligible for automatic selection when criteria match. | N-U13-053 |
| VDR-U13-C091 | FUNCTION MAPPING REQUIRED | account/models/partner.py:53 | vat_required = fields.Boolean | FACT | always | - | vat_required restricts a position to partners having a VAT number. | N-U13-053 |
| VDR-U13-C092 | FUNCTION MAPPING REQUIRED | account/models/partner.py:57 | Apply only if delivery country matches. | FACT | always | - | country_id restricts to delivery country; country_group_id restricts to countries of a group; state_ids restricts to federal states; zip_from/zip_to define a zip range. | N-U13-053 |
| VDR-U13-C093 | FUNCTION MAPPING REQUIRED | account/models/partner.py:116 | You have to configure both | FACT | always | - | Zip range needs both ends and zip_to must be greater than zip_from, otherwise ValidationError. | N-U13-060 |
| VDR-U13-C094 | FUNCTION MAPPING REQUIRED | account/models/partner.py:186 | rjust(max_length, '0') | FACT | create/write with zip range | - | Numeric zip bounds are left-padded with zeros to the same length before storing. | N-U13-060 |
| VDR-U13-C095 | FUNCTION MAPPING REQUIRED | account/models/partner.py:127 | without assigning it a state | FACT | foreign_vat set | - | A foreign-VAT position inside the company's own fiscal country must have states when that country has states. | N-U13-061 |
| VDR-U13-C096 | FUNCTION MAPPING REQUIRED | account/models/partner.py:139 | A fiscal position with a foreign | FACT | foreign_vat set | - | Only one foreign VAT value per country per company is allowed across fiscal positions. | N-U13-061 |
| VDR-U13-C097 | FUNCTION MAPPING REQUIRED | account/models/partner.py:130 | country outside of the selected country | FACT | foreign_vat set | - | Country must be inside the selected country group when both are set. | N-U13-061 |
| VDR-U13-C098 | FUNCTION MAPPING REQUIRED | account/models/partner.py:123 | country of the foreign VAT number | FACT | foreign_vat set | - | A foreign VAT requires a country on the position. | N-U13-061 |
| VDR-U13-C099 | FUNCTION MAPPING REQUIRED | account/models/company.py:354 | potential_domestic_fps | FACT | always | - | Company domestic_fiscal_position_id is computed as the lowest-sequence position whose country equals the company country or (no country) whose group contains it. | N-U13-065 |
| VDR-U13-C100 | FUNCTION MAPPING REQUIRED | account/models/partner.py:77 | position == position.company_id.domestic_fiscal_position_id | FACT | always | - | Position.is_domestic is true only for the company's domestic position. | N-U13-065 |
| VDR-U13-C101 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:355 | tax.is_domestic = not tax.fiscal_position_ids or | FACT | always | - | A tax is domestic when it has no fiscal positions or includes the company's domestic position. | N-U13-065 |
| VDR-U13-C102 | FUNCTION MAPPING REQUIRED | account/models/partner.py:158 | return taxes.filtered(lambda tax: not tax.fiscal_position_ids) | FACT | position has no tax_ids | - | map_tax with no position returns taxes unchanged; with a position lacking taxes it keeps only taxes without fiscal_position_ids; otherwise each tax is replaced by its mapped alternatives (unmapped taxes pass through). | N-U13-056 |
| VDR-U13-C103 | FUNCTION MAPPING REQUIRED | account/models/partner.py:103 | for src_tax in dest_tax.original_tax_ids | FACT | always | - | tax_map is derived from the position taxes: each destination tax maps all taxes listed in its original_tax_ids ('Replaces'). | N-U13-056 |
| VDR-U13-C104 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:98 | account_fiscal_position_account_tax_rel | FACT | always | - | Tax to fiscal position link is a many2many stored in account_fiscal_position_account_tax_rel; original_tax_ids ('Replaces') is a second many2many account_tax_alternatives restricted to domestic taxes of same type. | N-U13-051 |
| VDR-U13-C105 | FUNCTION MAPPING REQUIRED | account/models/partner.py:165 | def map_account | FACT | always | - | map_account returns the destination account of the first mapping for the source account or the account itself. | N-U13-057 |
| VDR-U13-C106 | FUNCTION MAPPING REQUIRED | account/models/partner.py:329 | 'unique (position_id,account_src_id,account_dest_id)' | FACT | always | - | Account mapping unique constraint per position, source and destination; both accounts required and company-checked. | N-U13-062 |
| VDR-U13-C107 | FUNCTION MAPPING REQUIRED | account/models/partner.py:266 | partner manually set fiscal position always | FACT | always | - | If the delivery partner (else the invoicing partner) has property_account_position_id for the company it is returned without any criteria check. | N-U13-052 |
| VDR-U13-C108 | FUNCTION MAPPING REQUIRED | account/models/partner.py:274 | if not partner.country_id: | FACT | no manual position | - | Without a partner country no automatic position is returned. | N-U13-054 |
| VDR-U13-C109 | FUNCTION MAPPING REQUIRED | account/models/partner.py:277 | ('auto_apply', '=', True) | FACT | no manual position, partner has country | - | Candidate positions are the auto_apply positions of the active company hierarchy; the first matching one wins. | N-U13-053 |
| VDR-U13-C110 | FUNCTION MAPPING REQUIRED | account/models/partner.py:209 | company specific first, then sequence | FACT | always | - | Candidates are sorted by (more specific company first, then sequence) and the first passing all validators is returned. | N-U13-053 |
| VDR-U13-C111 | FUNCTION MAPPING REQUIRED | account/models/partner.py:215 | def _get_fpos_validation_functions | FACT | always | - | Validators: vat_required, zip range, states, country, country group (partner state not in the group's excluded states); all must pass. | N-U13-053 |
| VDR-U13-C112 | FUNCTION MAPPING REQUIRED | account/models/partner.py:226 | fpos.zip_from <= partner.zip <= fpos.zip_to | FACT | position has zip range | - | Zip match is a string comparison between the partner zip and the padded bounds. | N-U13-053 |
| VDR-U13-C113 | FUNCTION MAPPING REQUIRED | account/models/partner.py:878 | return bool(self.vat and self.vat != '/') | FACT | always (VAT check hook) | - | The VAT validity used by vat_required is only 'VAT set and not /' in the base hook (overridable). | N-U13-053 |
| VDR-U13-C114 | FUNCTION MAPPING REQUIRED | account/models/partner.py:263 | intra_eu and vat_exclusion | FACT | company and partner have VAT | - | When company and partner share the same VAT country prefix inside the EU and the partner country equals the company country, the invoicing partner is used instead of the delivery address. | N-U13-055 |
| VDR-U13-C115 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1049 | ._get_fiscal_position( | FACT | document partner/shipping/company change | - | Move fiscal_position_id is computed (stored, editable, precomputed) from partner, delivery partner and company via _get_fiscal_position. | N-U13-059 |
| VDR-U13-C116 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1039 | receipt_fiscal_position = { | FACT | document type in_receipt | - | Purchase receipts take company.account_purchase_receipt_fiscal_position_id when set instead of detection. | N-U13-059 |
| VDR-U13-C117 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2680 | self.show_update_fpos = self.line_ids and | FACT | UI edit | - | Changing the fiscal position on a document with lines raises a flag that offers to update the lines. | N-U13-059 |
| VDR-U13-C118 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:461 | compute='_compute_fiscal_position_id', store=True, readonly=False, precompute=True, | FACT | always | - | Move field fiscal_position_id uses ondelete restrict (a used position cannot be deleted). | N-U13-059 |
| VDR-U13-C119 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:667 | get_product_accounts(fiscal_pos=fiscal_position) | FACT | product line on invoice | - | Invoice product lines pick income or expense account through product accounts mapped by the fiscal position. | N-U13-057 |
| VDR-U13-C120 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:659 | line.move_id.fiscal_position_id.map_account | FACT | payment_term line | - | Receivable/payable term lines are also mapped through the fiscal position account mapping. | N-U13-057 |
| VDR-U13-C121 | FUNCTION MAPPING REQUIRED | account/models/product.py:262 | # Apply fiscal position. | FACT | product with taxes and a fiscal position | - | Default unit price is adapted when the fiscal position maps price-included taxes to other taxes. | N-U13-058 |
| VDR-U13-C122 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2869 | not compatible with your fiscal position | FACT | document line taxes | - | Constraint rejects entries whose line taxes belong to countries incompatible with the fiscal position country (or the company fiscal country). | N-U13-063 |
| VDR-U13-C123 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1948 | tax_country_id = fiscal_position_id.country_id | FACT | fiscal position has foreign_vat | - | Move tax_country_id follows the fiscal position country when the position has a foreign VAT. | N-U13-063 |
| VDR-U13-C124 | FUNCTION MAPPING REQUIRED | account/models/partner.py:555 | property_account_position_id = fields.Many2one | FACT | always | - | Partner default fiscal position is a company-dependent field with help text 'determines the taxes/accounts used'. | N-U13-052 |
| VDR-U13-C125 | FUNCTION MAPPING REQUIRED | account/models/partner.py:300 | Only Accounting managers can create foreign | FACT | action create foreign taxes | - | Creating foreign taxes from a foreign-VAT position is restricted to accounting managers or admin and may install the localization module of that country. | N-U13-066 |
| VDR-U13-C126 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1146 | def _get_account_fiscal_position | FACT | chart load | - | Chart templates provide fiscal positions through a CSV named per template; the loader tolerates missing files. | N-U13-064 |
| VDR-U13-C127 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1356 | No file %s found for template | OBSERVATION | DB chart th loaded | - | l10n_th ships no fiscal position file (its template folder has only account, tax, tax group and an asset file); the DB has 0 fiscal positions and the company has no domestic position. | N-U13-064 |
| VDR-U13-C128 | FUNCTION MAPPING REQUIRED | account/models/company.py:128 | account_purchase_receipt_fiscal_position_id = fields.Many2one | OBSERVATION | DB | - | DB has zero fiscal positions; therefore no auto-detection or mapping occurs and company default purchase receipt position is unset. | N-U13-067 |
| VDR-U13-C129 | FUNCTION MAPPING REQUIRED | account/models/partner.py:36 | By unchecking the active field | FACT | always | - | Fiscal positions can be archived through active without deletion. | N-U13-069 |
| VDR-U13-C130 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:463 | Fiscal positions are used to adapt | FACT | always | - | Field help: fiscal positions adapt taxes and accounts for particular customers or sales orders and invoices; the default comes from the customer. | N-U13-070 |
| VDR-U13-C131 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | runtime | RT | UNKNOWN - EVIDENCE INSUFFICIENT: no fiscal position exists in the DB, so detection, mapping and price adaptation were never exercised for the Thai company; resolve by creating a sample position in a test database. | N-U13-068 |
| VDR-U13-C132 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:64 | ("off_balance", "Off-Balance Sheet"), | FACT | always | - | account_type selection has 19 values: asset_receivable, asset_cash, asset_current, asset_non_current, asset_prepayments, asset_fixed, liability_payable, liability_credit_card, liability_current, liability_non_current, equity, equity_unaffected, income, income_other, expense, expense_other, expense_depreciation, expense_direct_cost, off_balance. | N-U13-081 |
| VDR-U13-C133 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:69 | Account Type is used for information | FACT | always | - | Help text states the type is used for legal reports and for the rules to close a fiscal year and generate opening entries. | N-U13-109 |
| VDR-U13-C134 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:650 | account_type.split('_', maxsplit=1)[0] | FACT | always | - | internal_group (equity, asset, liability, income, expense, off) is derived from the first token of account_type. | N-U13-083 |
| VDR-U13-C135 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:642 | account.internal_group not in ['income', 'expense'] | FACT | always | - | include_initial_balance is true except for income/expense group and equity_unaffected, i.e. P&L accounts reset each fiscal year. | N-U13-083 |
| VDR-U13-C136 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:670 | elif account.account_type in ('asset_receivable', 'liability_payable'): | FACT | account_type changes | - | reconcile is computed False for income/expense/equity, True for receivable/payable, False for cash/credit card/off-balance; other asset/liability types keep the stored value. | N-U13-083 |
| VDR-U13-C137 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:31 | You cannot have a receivable/payable account | FACT | always | - | Receivable and payable accounts must be reconcilable. | N-U13-083 |
| VDR-U13-C138 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:192 | An Off-Balance account can not be | FACT | account_type off_balance | - | Off-balance accounts cannot be reconcilable nor carry default taxes. | N-U13-083 |
| VDR-U13-C139 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:999 | if some partial reconciliations are still | FACT | toggling reconcile to False | - | Switching reconcile off is refused while lines have partial reconciliations; toggling on/off rewrites amount_residual fields of unreconciled lines by SQL. | N-U13-087 |
| VDR-U13-C140 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:965 | def _toggle_reconcile_to_true | FACT | toggling reconcile to True | - | Turning reconcile on resets residual amounts to the line balance and marks zero lines as reconciled. | N-U13-087 |
| VDR-U13-C141 | MCT-F03 | account/models/account_account.py:97 | string='Companies', required=True | FACT | always | - | Accounts belong to one or more companies through company_ids (many2many, required, default current company); the chart is therefore shareable across companies rather than duplicated. | N-U13-085 |
| VDR-U13-C142 | MCT-F03 | account/models/account_account.py:40 | code_store = fields.Char(company_dependent=True) | FACT | always | - | Code is stored in a company-dependent field and read/written at the root company, so companies of the same root share one code. | N-U13-084 |
| VDR-U13-C143 | MCT-F03 | account/models/account_account.py:340 | record.code = record_root.code_store | FACT | always | - | _compute_code and _inverse_code operate with company = root company of the current company. | N-U13-084 |
| VDR-U13-C144 | MCT-F03 | account/models/account_account.py:1145 | Account codes must be unique. | FACT | create/write of code or companies | - | Duplicate codes are rejected across parent and child companies of every company of the account. | N-U13-084 |
| VDR-U13-C145 | MCT-F03 | account/models/account_account.py:1111 | The code must be set for | FACT | always | - | A code must exist for every company root the account belongs to. | N-U13-084 |
| VDR-U13-C146 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:315 | alphanumeric characters and dots | FACT | always | - | Account code may contain only letters, digits and dots (regex ^[A-Za-z0-9.]+$) and is limited to 64 chars. | N-U13-084 |
| VDR-U13-C147 | MCT-F03 | account/models/account_account.py:281 | Bank & Cash accounts cannot be | FACT | asset_cash accounts | - | Accounts of type asset_cash cannot belong to more than one company. | N-U13-085 |
| VDR-U13-C148 | MCT-F03 | account/models/account_account.py:288 | since there are some journal items | FACT | removing a company from an account | - | A company cannot be unlinked from an account that already has journal items of that company. | N-U13-085 |
| VDR-U13-C149 | MCT-F03 | account/models/account_account.py:275 | must be assigned to at least | FACT | always | - | An account without any company is rejected. | N-U13-085 |
| VDR-U13-C150 | MCT-F03 | account/security/account_security.xml:153 | Account multi-company | FACT | always | - | Global record rule limits accounts to those whose company_ids are parents of the user's allowed companies (company_ids parent_of rule). | N-U13-085 |
| VDR-U13-C151 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:36 | Forces all journal items in this | FACT | account has currency_id | - | Account currency forces journal items to that currency; entries with no currency may use any. | N-U13-086 |
| VDR-U13-C152 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:1073 | You cannot set a currency on | FACT | writing currency_id | - | Setting a currency is refused when existing lines carry a different foreign currency. | N-U13-086 |
| VDR-U13-C153 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:264 | The foreign currency set on the | FACT | journal has foreign currency | - | Journal foreign currency and the currency of its default account and payment-method accounts must match. | N-U13-086 |
| VDR-U13-C154 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:308 | already in use in a 'sale' | FACT | account_type change | - | An account that is the default account of a sale or purchase journal cannot become receivable or payable. | N-U13-093 |
| VDR-U13-C155 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:333 | You cannot change the type of | FACT | account_type change | - | An account referenced as default account of any journal cannot be switched to receivable or payable. | N-U13-093 |
| VDR-U13-C156 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:1157 | You cannot perform this action on | FACT | unlink of account | - | Deleting an account with journal items is refused (ondelete at_uninstall False). | N-U13-092 |
| VDR-U13-C157 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:1162 | set on the account mapping of | FACT | unlink of account | - | Deleting an account used in a fiscal position account mapping is refused. | N-U13-092 |
| VDR-U13-C158 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:1167 | which are set on a tax | FACT | unlink of account | - | Deleting an account set on a tax repartition line is refused. | N-U13-092 |
| VDR-U13-C159 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:1075 | vals.get('deprecated') | INFERENCE | write with a deprecated key | - | write() contains a guard 'You cannot deprecate an account that is used in a tax distribution' keyed on vals deprecated; no field named deprecated is declared in this model (active is the archive flag), so the guard is apparently dead code and archival of accounts used in tax distribution is not blocked here (grep over account models shows the key only at this line). | N-U13-092 |
| VDR-U13-C160 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:42 | active = fields.Boolean(default=True, tracking=True) | INFERENCE | always | - | Archival uses active (tracked); no write override guards archival; error text of unlink guards mentions deactivate but the checks are on unlink only (ondelete decorators). | N-U13-091 |
| VDR-U13-C161 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:450 | def _get_used_account_ids | FACT | always | - | Computed used flag is true when any journal item references the account. | N-U13-091 |
| VDR-U13-C162 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:1189 | You cannot merge accounts. | FACT | merge via generic method | - | The generic record-merge method refuses to merge accounts; merging is only possible through the dedicated wizard. | N-U13-094 |
| VDR-U13-C163 | FUNCTION MAPPING REQUIRED | account/wizard/account_merge_wizard.py:44 | grouping_fields = ['account_type', 'non_trade', 'currency_id', 'reconcile', | FACT | merge wizard | - | The wizard groups candidate accounts by type, non-trade flag, currency, reconcile and active (optionally name) and excludes bank/cash types. | N-U13-094 |
| VDR-U13-C164 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:1192 | Split the account `self` into several | FACT | account with several companies | - | action_unmerge splits a shared account into one account per company keeping each company's code; refused for single-company accounts or when user lacks access to all its companies. | N-U13-094 |
| VDR-U13-C165 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:1019 | Please create new accounts from the | FACT | name_create outside import | - | Quick-create of accounts by name is refused except during file import. | N-U13-080 |
| VDR-U13-C166 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:468 | def _search_new_account_code | FACT | account creation with prefix | - | New accounts created with prefix and digits get the first free code by incrementing (with .copy fallback up to 99). | N-U13-084 |
| VDR-U13-C167 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:614 | def _get_closest_parent_account | FACT | account with code and no type or tags | - | Missing account_type and tag_ids are copied from the closest lower code in the company (default type asset_current). | N-U13-089 |
| VDR-U13-C168 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:1515 | _name = 'account.group' | FACT | always | - | Account group has prefix start/end, parent and company (default root company of the active company). | N-U13-088 |
| VDR-U13-C169 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:437 | agroup.code_prefix_start <= LEFT(account_code.code | FACT | always | - | Account.group_id is computed by matching the account code against group prefixes of the root company, choosing the longest prefix. | N-U13-088 |
| VDR-U13-C170 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:1585 | same granularity | FACT | always | - | Groups with the same prefix length in the same company must not overlap. | N-U13-088 |
| VDR-U13-C171 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:1529 | The length of the starting and | FACT | always | - | SQL constraint requires equal prefix start and end lengths. | N-U13-088 |
| VDR-U13-C172 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:1617 | def _adapt_parent_account_group | FACT | group create/write | - | Parent group is set to the group with longest enclosing prefix; sync is delayed during chart load and re-run afterwards. | N-U13-088 |
| VDR-U13-C173 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:12 | applicability = fields.Selection | FACT | always | - | Account tag applicability is accounts, taxes or products; tax tags are country-bound. | N-U13-089 |
| VDR-U13-C174 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:24 | A tag with the same name | FACT | always | - | Tag names are unique per applicability and country. | N-U13-089 |
| VDR-U13-C175 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:113 | "account_tag_operating", | FACT | unlink | - | The three cash-flow master tags (operating, financing, investing) cannot be deleted. | N-U13-092 |
| VDR-U13-C176 | FUNCTION MAPPING REQUIRED | account/models/company.py:844 | Do not assume '999999' doesn't exist | FACT | chart load | - | Unaffected earnings account of type equity_unaffected is reused if present else created with code 999999 (or next lower free code). | N-U13-090 |
| VDR-U13-C177 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:140 | def try_loading | FACT | always | - | try_loading(template_code, company, install_demo=False, force_create=True) is the public entry; when no code is given the template is guessed from company country. | N-U13-082 |
| VDR-U13-C178 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:169 | shouldn't be selected directly | FACT | template syscohada or syscebnl | - | Regional umbrella templates cannot be loaded directly. | N-U13-095 |
| VDR-U13-C179 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:184 | Only administrators can install chart templates | FACT | always | - | _load raises AccessError unless the caller is a system administrator, then runs as sudo. | N-U13-095 |
| VDR-U13-C180 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:193 | module.button_immediate_install() | FACT | template module not installed | - | If the localization module is uninstalled it is installed immediately and the registry reset. | N-U13-095 |
| VDR-U13-C181 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:206 | chart_template_load=True, | FACT | always | - | Loading runs with context: company-only, tracking disabled, group sync delayed, language en_US, chart_template_load flag. | N-U13-095 |
| VDR-U13-C182 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:210 | reload_template = template_code == company.chart_template | FACT | always | - | Loading the template already set on the company is treated as a reload. | N-U13-097 |
| VDR-U13-C183 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:224 | records.with_context({MODULE_UNINSTALL_FLAG: True}).unlink() | FACT | template change, no entries (or install_demo) | - | For a root company switching to another template with no accounting entries (or when demo is requested) all moves and records of the template models (groups, accounts, fiscal positions, tax groups, taxes, journals, reconcile models) are unlinked first; shared accounts are only detached from the company tree. | N-U13-096 |
| VDR-U13-C184 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:213 | not company.root_id._existing_accounting() or install_demo | INFERENCE | template change with existing entries | RT | With existing accounting entries and a different template the wipe is skipped (lines 213-224) and template data is merged by xml id into existing records without the reload protections; the effect on duplicates is not exercised here. | N-U13-108 |
| VDR-U13-C185 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:23 | TEMPLATE_MODELS = ( | FACT | always | - | A template can create records of account.group, account.account, account.fiscal.position, account.tax.group, account.tax, account.journal and account.reconcile.model (in that order) plus company values. | N-U13-082 |
| VDR-U13-C186 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:821 | def _get_chart_template_data | FACT | always | - | Template data is assembled from root @template functions then each parent template chain, later functions overriding earlier values per xml id. | N-U13-082 |
| VDR-U13-C187 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1330 | data/template/{model} | FACT | always | - | Accounts, groups, tax groups, taxes and fiscal positions are read from CSV files named model-template under the localization module data/template folder. | N-U13-082 |
| VDR-U13-C188 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1175 | "exch": { | FACT | always | - | Root template creates journals Sales (INV), Purchases (BILL), Miscellaneous (MISC), Exchange Difference (EXCH), Cash Basis Taxes (CABA) and Bank, plus two reconcile models (Internal Transfers, Bank Fees). | N-U13-082 |
| VDR-U13-C189 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:509 | vals['currency_id'] = fiscal_country.currency_id.id | FACT | root company without accounting entries | - | Company currency is set to the currency of the template fiscal country when no entries exist (branches take the parent currency). | N-U13-102 |
| VDR-U13-C190 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:514 | vals.setdefault('anglo_saxon_accounting', False) | FACT | always | - | Anglo-Saxon flag is reset to False unless the template sets it (generic template sets True). | N-U13-100 |
| VDR-U13-C191 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:521 | code_digits = int(template_data.get('code_digits', 6)) | FACT | always | - | Account codes from templates are right-padded with zeros to code_digits (default 6). | N-U13-082 |
| VDR-U13-C192 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:530 | Exclude data of unknown fields present | FACT | always | - | Template keys naming fields that do not exist in the registry are silently dropped unless l10n_check_fields_complete is set. | N-U13-082 |
| VDR-U13-C193 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1230 | return f"account.{company.id}_{xmlid}" | FACT | always | - | Template records get xml ids account.<company id>_<template id> and are loaded noupdate. | N-U13-082 |
| VDR-U13-C194 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:706 | Unaffected earnings account on the company | FACT | always | - | Post-load sets journal suspense and cash-difference accounts, CABA and exchange journals, default sale/purchase journal accounts and default taxes on the company, default taxes on products with no taxes of the company, and cash-basis flag when on_payment taxes exist. | N-U13-100 |
| VDR-U13-C195 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:766 | for field, model in self._get_property_accounts(additional_properties).items(): | FACT | always | - | Template property accounts (receivable, payable, stock journal) become ir.default values for the company (partner and product category defaults). | N-U13-100 |
| VDR-U13-C196 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:927 | def _create_outstanding_accounts | FACT | root company | - | Utility accounts (suspense, cash difference, early payment discount, transfer) are created only when the company field is empty; Outstanding Receipts and Outstanding Payments accounts are always created for root companies. | N-U13-100 |
| VDR-U13-C197 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:265 | def _pre_reload_data | FACT | reload of same template | - | On reload property values are dropped, company values cleared, reconcile models skipped and existing journals matched by code or name are kept. | N-U13-097 |
| VDR-U13-C198 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:397 | tax_to_rename.name = f"[old | FACT | reload and tax template changed | - | A tax whose amount type, amount or repartition line count differs from the template is renamed with an [old] prefix and a new tax created (when force_create); unchanged taxes only get fiscal position links and repartition tags refreshed. | N-U13-097 |
| VDR-U13-C199 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:448 | on existing accounts, only tag_ids are | FACT | reload | - | Existing accounts (matched by xml id or by code prefix) only receive tag updates; the reconcile flag is never overridden and nothing is created when force_create is False. | N-U13-097 |
| VDR-U13-C200 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:151 | force_create: Determines the loading behavior. | FACT | always | - | force_create=False performs updates on existing data without creating new records. | N-U13-098 |
| VDR-U13-C201 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:245 | Install the demo data when the | FACT | install_demo and not reload | - | Demo data is loaded in a savepoint after the first template on a company; failures are logged and do not roll back the chart. | N-U13-098 |
| VDR-U13-C202 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:254 | for subsidiary in company.child_ids: | FACT | company has child companies | - | Subsidiaries are loaded recursively with the same template; for a child company only res.company data is applied. | N-U13-099 |
| VDR-U13-C203 | FUNCTION MAPPING REQUIRED | account/models/company.py:491 | root_template := company.parent_ids[0].chart_template | FACT | company create | - | Creating a company under a root that has a chart template schedules loading that template at precommit. | N-U13-099 |
| VDR-U13-C204 | FUNCTION MAPPING REQUIRED | account/models/res_config_settings.py:222 | self.chart_template != self.company_id.chart_template | FACT | settings save | - | Saving settings with a different chart_template triggers try_loading; reload_template button reloads the current one. | N-U13-082 |
| VDR-U13-C205 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:83 | self.env.registry._auto_install_template = try_loading | FACT | localization module installed on company without chart | - | Installing a localization module on a company without chart_template loads its first template matching the company country (or generic_coa). | N-U13-101 |
| VDR-U13-C206 | FUNCTION MAPPING REQUIRED | account/models/company.py:982 | template_code = company.parent_id.chart_template or | FACT | company country set, no template | - | install_l10n_modules schedules try_loading with the parent template or the guessed country template (not for generic_coa). | N-U13-101 |
| VDR-U13-C207 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:30 | def _compute_account_templates | FACT | always | - | Available templates are discovered from the python models of account and localization-category modules via @template-decorated functions. | N-U13-101 |
| VDR-U13-C208 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:112 | companies.chart_template = False | FACT | localization module uninstall | - | Uninstalling a localization module clears chart_template on companies that used its templates. | N-U13-101 |
| VDR-U13-C209 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1267 | missing tax tag %(tag_name)s for country | FACT | template references unknown tax tag | - | Loading stops with a RedirectWarning inviting to update the localization when a tax tag named in the template does not exist (unless ignore_missing_tags). | N-U13-103 |
| VDR-U13-C210 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:954 | def _instantiate_foreign_taxes | FACT | foreign-VAT fiscal position | - | Foreign taxes for another country are created from that country's template with accounts cloned from the local ones; skipped when taxes of that country already exist. | N-U13-107 |
| VDR-U13-C211 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:12 | 'code_digits': '6', | FACT | template th | - | Template th sets code_digits 6 and default receivable 112100, payable 212100, stock valuation 113100 and down payment 212400 accounts. | N-U13-106 |
| VDR-U13-C212 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:2 | l10n_th_account_111100 | OBSERVATION | DB company chart th loaded | - | DB holds 147 accounts: 144 from the template file, 2 Outstanding accounts and 1 bank journal default account; all 6-digit numeric codes, none archived, none with foreign currency, 0 account groups. | N-U13-106 |
| VDR-U13-C213 | MCT-F03 | account/models/account_account.py:97 | string='Companies', required=True | OBSERVATION | DB | - | DB has 1 company and 147 account-company links (every account on exactly 1 company), so the shared-versus-per-company question is not exercised: no shared accounts exist. | N-U13-106 |
| VDR-U13-C214 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.account-th.csv:7 | l10n_th_account_112100 | OBSERVATION | DB | - | DB account types: 4 receivable, 3 payable, 4 cash, 17 current assets, 22 fixed assets, 6 non-current assets, 13 current liabilities, 3 non-current liabilities, 3 equity, 1 equity_unaffected (code 999999), 4 income, 6 other income, 42 expense, 12 depreciation, 7 direct cost; no off-balance or credit-card accounts. | N-U13-106 |
| VDR-U13-C215 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.asset-th.csv:2 | l10n_th_account | INFERENCE | Community only | - | A depreciation-model data file exists in the template folder but the root template functions cover only the seven template models; no Community function reads it (inferred from chart_template.py root functions at lines 1127-1220). | N-U13-105 |
| VDR-U13-C216 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:26 | 'transfer_account_code_prefix': 'l10n_th_account_11120' | OBSERVATION | DB company chart th loaded | - | Template th passes the string l10n_th_account_11120 (a template id form) as transfer_account_code_prefix; the DB company holds that literal text; since transfer_account_id is set directly the prefix is not used to create the transfer account. | N-U13-104 |
| VDR-U13-C217 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1230 | return f"account.{company.id}_{xmlid}" | OBSERVATION | DB company chart th loaded | CONTRA | DB holds 179 company-prefixed template identifiers under module account (147 accounts, 18 taxes, 7 journals, 5 tax groups, 2 reconcile models); CONTRA B01 section 2.1 which cites 181 for this class (difference of 2 not explained here). | N-U13-106 |
| VDR-U13-C218 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | runtime | RT | UNKNOWN - EVIDENCE INSUFFICIENT: the effect of reloading template th on this database (renamed taxes, tag refresh, missing records) was not executed; resolve by a reload on a copy. | N-U13-110 |
| VDR-U13-C219 | FUNCTION MAPPING REQUIRED | account/models/company.py:759 | You cannot change the currency of | FACT | company currency write | - | Company currency change is refused when journal items exist (checked on the root company tree). | N-U13-131 |
| VDR-U13-C220 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:509 | vals['currency_id'] = fiscal_country.currency_id.id | FACT | chart load, no entries | - | Chart loading sets the company currency from the fiscal country (company write also activates the currency). | N-U13-131 |
| VDR-U13-C221 | FUNCTION MAPPING REQUIRED | account/models/res_currency.py:31 | You cannot reduce the number of | FACT | currency rounding write | - | Raising the rounding factor (fewer decimals) or setting it to zero is refused if the currency already appears on journal items as foreign or company currency. | N-U13-137 |
| VDR-U13-C222 | FUNCTION MAPPING REQUIRED | account/models/res_currency.py:35 | def _has_accounting_entries | FACT | always | - | Usage test counts journal items where the currency is the line currency or the company currency. | N-U13-137 |
| VDR-U13-C223 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:54 | CHECK (rounding>0) | FACT | always | - | Currency rounding factor must be positive; code is unique; decimal_places is derived from rounding. | N-U13-137 |
| VDR-U13-C224 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:118 | cannot be deactivated | FACT | always | - | A currency set on a company cannot be archived. | N-U13-138 |
| VDR-U13-C225 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:89 | active_currency_count > 1 | FACT | currency create/archive | - | The multi-currency user group is applied to all internal users automatically when more than one currency is active and removed otherwise. | N-U13-138 |
| VDR-U13-C226 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:128 | ('company_id', 'in', (False, company.root_id.id)), | FACT | always | - | Rate lookup uses the latest rate on or before the date among rates of the root company or without company (company-specific ordered first). | N-U13-133 |
| VDR-U13-C227 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:138 | COALESCE((%s), (%s), 1.0) | FACT | no rate on or before date | - | If no rate exists on or before the date the earliest rate is used; if the currency has no rate at all the factor is 1.0. | N-U13-133 |
| VDR-U13-C228 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:276 | rates only ever live on the | FACT | branch companies | - | Conversion resolves rates against the root company; rates for branch companies are refused. | N-U13-133 |
| VDR-U13-C229 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:477 | Currency rates should only be created | FACT | always | - | Currency rates may only be created for main (non-branch) companies; one rate per day per currency and company; rate must be > 0. | N-U13-133 |
| VDR-U13-C230 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:303 | return to_currency.round(to_amount) if round else to_amount | FACT | always | - | _convert multiplies by the conversion rate and rounds to the target currency unless round is false; zero amount returns 0. | N-U13-135 |
| VDR-U13-C231 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1123 | invoice.statement_line_id.foreign_currency_id | FACT | document creation | - | Move currency defaults to bank statement line foreign currency, else journal currency, else existing value, else company currency. | N-U13-132 |
| VDR-U13-C232 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:547 | line.currency_id = line.move_id.currency_id | FACT | invoice lines | - | Invoice lines take the move currency; other lines keep their currency or default to the company currency; cogs lines use company currency. | N-U13-132 |
| VDR-U13-C233 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1132 | return self.invoice_date or fields.Date.context_today(self) | FACT | invoices | - | The date used for the document rate is invoice_date, else today. | N-U13-133 |
| VDR-U13-C234 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:543 | Currency rate from company currency to | FACT | always | - | invoice_currency_rate is stored, precomputed, editable and not copied. | N-U13-134 |
| VDR-U13-C235 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1155 | move.invoice_currency_rate = move.expected_currency_rate | FACT | invoices and receipts | - | The stored invoice rate is recomputed from the expected rate when currency, company or invoice date change. | N-U13-134 |
| VDR-U13-C236 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2883 | The currency rate must be strictly | FACT | foreign-currency invoice | - | Foreign-currency invoices require invoice_currency_rate > 0. | N-U13-134 |
| VDR-U13-C237 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6095 | def refresh_invoice_currency_rate | FACT | user action | - | refresh_invoice_currency_rate resets the document rate to the expected rate. | N-U13-134 |
| VDR-U13-C238 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5644 | is_manual_rate = invoice.invoice_currency_rate != | FACT | posting a customer invoice without invoice date | - | When invoice date is empty at posting it is set to today and the rate recomputed unless the user changed the rate manually. | N-U13-134 |
| VDR-U13-C239 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:766 | date=line.move_id.invoice_date or line.move_id.date | FACT | non-invoice entries with currency | - | For non-invoice lines the rate is the conversion at invoice date or entry date; for invoices it is the move invoice_currency_rate. | N-U13-133 |
| VDR-U13-C240 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:780 | line.amount_currency = line.currency_id.round(line.balance * line.currency_rate) | FACT | amount_currency unset | - | Default foreign amount is balance times rate rounded to line currency; same-currency non-invoice lines force amount_currency to balance. | N-U13-135 |
| VDR-U13-C241 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:489 | The amount expressed in the secondary | FACT | always | - | Database check: balance and amount_currency must have the same sign (zero allowed). | N-U13-136 |
| VDR-U13-C242 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:485 | Wrong credit or debit value in | FACT | always | - | Database check: a line cannot have both debit and credit. | N-U13-136 |
| VDR-U13-C243 | FUNCTION MAPPING REQUIRED | account/models/account_cash_rounding.py:15 | _name = 'account.cash.rounding' | FACT | always | - | Cash rounding rule has rounding precision (default 0.01), strategy (add_invoice_line default or biggest_tax) and method UP, DOWN or HALF-UP (default). | N-U13-139 |
| VDR-U13-C244 | FUNCTION MAPPING REQUIRED | account/models/account_cash_rounding.py:49 | Please set a strictly positive rounding | FACT | always | - | Rounding precision must be strictly positive. | N-U13-140 |
| VDR-U13-C245 | FUNCTION MAPPING REQUIRED | account/models/account_cash_rounding.py:25 | profit_account_id = fields.Many2one( | FACT | always | - | Profit and loss accounts are company-dependent, company-checked, and exclude receivable/payable types. | N-U13-140 |
| VDR-U13-C246 | FUNCTION MAPPING REQUIRED | account/models/account_cash_rounding.py:68 | difference = self.round(amount) - amount | FACT | always | - | compute_difference rounds the document total to currency precision, rounds it to the cash precision, and returns the rounded difference. | N-U13-139 |
| VDR-U13-C247 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3076 | def _recompute_cash_rounding_lines | FACT | invoice with invoice_cash_rounding_id | - | A rounding line is created, updated or removed on the document; when strategy changes the old line is replaced; no line if already rounded. | N-U13-141 |
| VDR-U13-C248 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3123 | if self.invoice_cash_rounding_id.strategy == 'biggest_tax': | FACT | strategy biggest_tax | - | biggest_tax adds the difference as a tax-repartition line on the tax line with the largest absolute balance; nothing is done when the document has no tax line. | N-U13-139 |
| VDR-U13-C249 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3141 | elif self.invoice_cash_rounding_id.strategy == 'add_invoice_line': | FACT | strategy add_invoice_line | - | add_invoice_line posts the difference on the loss account when positive and a loss account is set, else on the profit account, with taxes cleared. | N-U13-139 |
| VDR-U13-C250 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2769 | def _onchange_invoice_cash_rounding_id | FACT | UI edit | - | Selecting an add_invoice_line cash rounding without a profit account raises a warning. | N-U13-140 |
| VDR-U13-C251 | FUNCTION MAPPING REQUIRED | account/views/account_move_views.xml:1555 | groups="account.group_cash_rounding" | FACT | always | - | The cash rounding field on the invoice form is visible only to users in the cash rounding group (enabled by a settings toggle). | N-U13-142 |
| VDR-U13-C252 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:3 | access_account_cash_rounding_uinvoice | FACT | always | - | Cash rounding rules are fully editable by Invoicing group and read-only for the readonly group. | N-U13-142 |
| VDR-U13-C253 | FUNCTION MAPPING REQUIRED | account/models/company.py:134 | income_currency_exchange_account_id = fields.Many2one( | FACT | always | - | Company holds exchange journal, gain account (income group) and loss account (expense/other expense) used by foreign exchange difference entries (engine in U12). | N-U13-143 |
| VDR-U13-C254 | FUNCTION MAPPING REQUIRED | account/models/partner.py:507 | partner.currency_id = partner.sudo().company_id.currency_id | FACT | always | - | Partner currency is derived from its company or the current company, not stored. | N-U13-130 |
| VDR-U13-C255 | FUNCTION MAPPING REQUIRED | account/models/company.py:153 | display_invoice_tax_company_currency = fields.Boolean( | FACT | always | - | Company option (default True) displays taxes in company currency on sale documents with taxes when document is in a different currency. | N-U13-130 |
| VDR-U13-C256 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1851 | and move.company_currency_id != move.currency_id | FACT | sale documents, foreign currency | - | tax_totals display_in_company_currency is true only for sale documents in a currency other than the company currency having tax groups. | N-U13-130 |
| VDR-U13-C257 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1937 | ('_currency', currency), | FACT | always | - | Global rounding of taxes is performed independently in the document currency and in the company currency. | N-U13-144 |
| VDR-U13-C258 | FUNCTION MAPPING REQUIRED | account/models/res_currency.py:15 | display_rounding_warning = fields.Boolean | OBSERVATION | DB | - | DB has two active currencies (THB company currency, USD) both rounding 0.01 with 2 decimal places and zero rate rows. | N-U13-145 |
| VDR-U13-C259 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:138 | COALESCE((%s), (%s), 1.0) | INFERENCE | DB with zero rate rows | RT | With no rate rows the lookup returns 1.0 for every currency, so a USD document would convert at 1:1 until rates are entered (inferred from _get_rates fallback and the empty rate table; not executed). | N-U13-145 |
| VDR-U13-C260 | FUNCTION MAPPING REQUIRED | account/models/account_cash_rounding.py:11 | smallest coinage has been removed | FACT | always | - | Class docstring: cash rounding exists because in some countries the smallest coins are withdrawn so cash invoices must be rounded (example 0.05). | N-U13-148 |
| VDR-U13-C261 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:539 | compute='_compute_invoice_currency_rate', store=True, precompute=True, | FACT | always | - | The conversion rate used by a document is stored on the document and recomputed until changed manually, so later rate changes do not alter existing documents. | N-U13-147 |
| VDR-U13-C262 | FUNCTION MAPPING REQUIRED | account/models/res_config_settings.py:92 | module_currency_rate_live | INFERENCE | settings | - | Automatic currency rates are exposed only as a settings toggle that installs an optional module; Community accounting itself contains no rate-fetching job (no cron in account referencing currency rates). | N-U13-146 |
| VDR-U13-C263 | PCO-F02 | account/models/company.py:74 | fiscalyear_last_day = fields.Integer(default=31, required=True) | FACT | always | - | Fiscal year is configured only by last day (default 31) and last month (default 12) on the company; both required; no fiscal-year or period records are stored by this module. | N-U13-161 |
| VDR-U13-C264 | PCO-F02 | account/models/company.py:345 | Invalid fiscal year last day | FACT | always | - | Constraint checks the last day against the length of the chosen month (using the opening-date year or the current year); 29 February is accepted explicitly. | N-U13-172 |
| VDR-U13-C265 | PCO-F02 | account/wizard/setup_wizards.py:38 | Incorrect fiscal year date: day is | FACT | onboarding wizard | - | Onboarding wizard validates day/month against leap year 2020 and writes company fields together to avoid per-field constraint failures. | N-U13-172 |
| VDR-U13-C266 | PCO-F02 | account/models/company.py:1122 | date_utils.get_fiscal_year(current_date | FACT | always | - | compute_fiscalyear_dates returns date_from/date_to of the fiscal year containing a date from the last day/month. | N-U13-161 |
| VDR-U13-C267 | PCO-F02 | account/models/company.py:311 | def _get_company_root_delegated_field_names | FACT | branch companies | - | fiscalyear_last_day, fiscalyear_last_month, account_storno and tax_exigibility are delegated to the root company of a branch. | N-U13-171 |
| VDR-U13-C268 | PCO-F02 | account/models/account_move.py:4313 | def _get_sequence_date_range | FACT | journal sequence resets year_range or year_range_month | - | Entry sequence date ranges for year-range resets are derived from the company fiscal year end (cross-ref U11 numbering). | N-U13-162 |
| VDR-U13-C269 | PCO-F02 | account/wizard/account_resequence.py:104 | date_start, date_end = get_fiscal_year | FACT | resequence wizard | - | Resequence preview keys moves by fiscal-year range using the company fiscal year end. | N-U13-162 |
| VDR-U13-C270 | PCO-F02 | account/data/onboarding_data.xml:33 | Define your fiscal years &amp; tax | INFERENCE | onboarding step text | - | Onboarding step description mentions tax returns periodicity, but the underlying wizard has only opening date and fiscal year end fields; no periodicity field was found in account or l10n_th sources (grep for periodicity found only a sequence docstring). | N-U13-168 |
| VDR-U13-C271 | PCO-F02 | account/wizard/setup_wizards.py:61 | fields.Date.from_string(opening_date) - timedelta(days=1) | FACT | opening move draft | - | Changing the opening date moves a draft opening entry to the day before the opening date. | N-U13-170 |
| VDR-U13-C272 | PCO-F02 | account/models/company.py:169 | account_opening_date = fields.Date(string='Opening Entry' | FACT | always | - | Company stores opening journal entry reference and opening date (date from which accounting is managed). | N-U13-170 |
| VDR-U13-C273 | PCO-F01 | account/models/company.py:57 | SOFT_LOCK_DATE_FIELDS = [ | FACT | always | - | Company has soft lock fields fiscalyear_lock_date, tax_lock_date, sale_lock_date, purchase_lock_date plus hard_lock_date (all tracked dates); enforcement engine belongs to U11. | N-U13-163 |
| VDR-U13-C274 | PCO-F01 | account/models/company.py:85 | automatically set when the tax closing | FACT | always | - | Help text states tax_lock_date is set automatically when the tax closing entry is posted. | N-U13-163 |
| VDR-U13-C275 | PCO-F01 | account/models/company.py:770 | active_exceptions._recreate() | FACT | company write | - | Writing lock dates invalidates user lock fields and recreates active lock exceptions affecting the changed fields. | N-U13-163 |
| VDR-U13-C276 | PCO-F01 | account/models/company.py:574 | The Hard Lock Date cannot be | FACT | hard_lock_date write | - | Hard lock date can neither be removed nor moved backwards. | N-U13-163 |
| VDR-U13-C277 | PCO-F01 | account/models/company.py:584 | There are still draft entries in | FACT | hard_lock_date write | - | A hard lock is refused while draft entries exist up to that date. | N-U13-163 |
| VDR-U13-C278 | PCO-F01 | account/models/company.py:602 | There are still unreconciled bank statement | FACT | fiscal or hard lock write | - | Fiscal/hard locks are refused while unreconciled bank statement lines exist in the period. | N-U13-163 |
| VDR-U13-C279 | FUNCTION MAPPING REQUIRED | account/models/company.py:144 | Use anglo-saxon accounting | FACT | always | - | anglo_saxon_accounting is a company boolean (default False). | N-U13-165 |
| VDR-U13-C280 | FUNCTION MAPPING REQUIRED | account/models/template_generic_coa.py:35 | 'anglo_saxon_accounting': True, | FACT | template generic_coa | - | Only the generic chart template sets the flag True; loading any other chart resets it to False unless the template says otherwise. | N-U13-165 |
| VDR-U13-C281 | FUNCTION MAPPING REQUIRED | account/models/company.py:286 | This account will be used when | FACT | always | - | Company income_account_id and expense_account_id (restricted by an account domain) feed product category defaults and default accounts of sales and purchase journals. | N-U13-166 |
| VDR-U13-C282 | FUNCTION MAPPING REQUIRED | account/models/company.py:1145 | def _set_category_defaults | FACT | company create/write | - | Company create/write re-applies ir.default values for product category income and expense accounts from company income/expense accounts. | N-U13-166 |
| VDR-U13-C283 | FUNCTION MAPPING REQUIRED | account/models/company.py:750 | company.reflect_code_prefix_change(company.bank_account_code_prefix | FACT | bank or cash prefix write | - | Changing bank or cash account code prefix renumbers existing cash and credit-card accounts having the old prefix. | N-U13-166 |
| VDR-U13-C284 | FUNCTION MAPPING REQUIRED | account/models/company.py:126 | account_sale_tax_id = fields.Many2one | FACT | always | - | Company default sale tax and default purchase tax are company-checked many2one fields set by chart loading. | N-U13-166 |
| VDR-U13-C285 | FUNCTION MAPPING REQUIRED | account/models/company.py:220 | tax_exigibility = fields.Boolean(string='Use Cash Basis') | FACT | always | - | Company flag enabling cash-basis taxes together with a cash-basis journal and base-tax account (note only). | N-U13-160 |
| VDR-U13-C286 | FUNCTION MAPPING REQUIRED | account/models/res_config_settings.py:280 | You cannot disable this setting because | FACT | settings UI | - | Cash-basis setting cannot be switched off while any tax of the company is on_payment. | N-U13-160 |
| VDR-U13-C287 | FUNCTION MAPPING REQUIRED | account/models/company.py:453 | company.account_fiscal_country_id.code in STORNO_MANDATORY_COUNTRIES | FACT | always | - | Storno accounting default depends on the fiscal country (mandatory list, optional list); Thailand is in neither list. | N-U13-167 |
| VDR-U13-C288 | FUNCTION MAPPING REQUIRED | account/models/company.py:323 | Can't disable restricted audit trail: forced | FACT | restrictive_audit_trail false while forced | - | Restrictive audit trail is optional unless a localization forces it (base compute returns False). | N-U13-169 |
| VDR-U13-C289 | FUNCTION MAPPING REQUIRED | account/models/company.py:269 | autopost_bills = fields.Boolean(string='Auto-validate bills', default=True) | FACT | always | - | Company flag autopost_bills defaults True. | N-U13-160 |
| VDR-U13-C290 | FUNCTION MAPPING REQUIRED | account/models/res_config_settings.py:237 | self.env['ir.default'].set( | FACT | settings save | - | Default partner credit limit is stored as ir.default for the company; account_use_credit_limit enables the feature. | N-U13-160 |
| VDR-U13-C291 | FUNCTION MAPPING REQUIRED | account/models/company.py:387 | def compute_account_tax_fiscal_country | FACT | always | - | account_fiscal_country_id is stored, editable, and defaults to the company country when empty. | N-U13-160 |
| VDR-U13-C292 | FUNCTION MAPPING REQUIRED | account/models/company.py:116 | expects_chart_of_accounts = fields.Boolean | FACT | always | - | expects_chart_of_accounts defaults True; get_chart_of_accounts_or_fail redirects to configuration when the company has no account. | N-U13-160 |
| VDR-U13-C293 | PCO-F02 | account/models/company.py:75 | fiscalyear_last_month = fields.Selection(MONTH_SELECTION | OBSERVATION | DB company | - | DB company: fiscal year end 31 December, all five lock dates empty, opening date and opening entry empty, anglo flag false, cash-basis flag true, storno false, tax return lock unset. | N-U13-173 |
| VDR-U13-C294 | FUNCTION MAPPING REQUIRED | account/models/company.py:129 | tax_calculation_rounding_method = fields.Selection([ | OBSERVATION | DB company | - | DB company: rounding round_globally, price tax_excluded, display tax in company currency true, autopost bills true, credit limit feature enabled with default limit 0, no QR code option, no quick-encoding mode. | N-U13-173 |
| VDR-U13-C295 | FUNCTION MAPPING REQUIRED | account/wizard/setup_wizards.py:16 | Date from which the accounting is | FACT | always | - | Opening date is defined as the date from which accounting is managed and is the date of the opening entry. | N-U13-176 |
| VDR-U13-C296 | PCO-F02 | account/models/account_move.py:4317 | fiscalyear_last_day = self.company_id.fiscalyear_last_day | INFERENCE | sequence reset year_range | RT | Because year-range sequence ranges are computed from the company fiscal year end at the time of numbering, changing the end after entries exist may place new entries in different ranges (not executed). | N-U13-174 |
| VDR-U13-C297 | PCO-F02 | n/a | n/a | UNKNOWN | Enterprise or other modules | RT | UNKNOWN - EVIDENCE INSUFFICIENT: tax return periodicity, tax closing entry creation and period locking workflows are not implemented in account or l10n_th sources read; resolve by checking modules that reference use_in_tax_closing and the tax lock date. | N-U13-175 |
| VDR-U13-C298 | FUNCTION MAPPING REQUIRED | account/models/partner.py:550 | property_account_receivable_id = fields.Many2one | FACT | always | - | Partner receivable account is a company-dependent field limited to receivable-type accounts, company-checked, ondelete restrict. | N-U13-190 |
| VDR-U13-C299 | FUNCTION MAPPING REQUIRED | account/models/partner.py:545 | property_account_payable_id = fields.Many2one | FACT | always | - | Partner payable account is company-dependent, limited to payable-type accounts, ondelete restrict. | N-U13-190 |
| VDR-U13-C300 | FUNCTION MAPPING REQUIRED | account/models/partner.py:563 | property_supplier_payment_term_id = fields.Many2one | FACT | always | - | Customer and vendor payment terms are company-dependent partner fields (terms engine is U12). | N-U13-202 |
| VDR-U13-C301 | FUNCTION MAPPING REQUIRED | account/models/partner.py:715 | def _commercial_fields | FACT | always | - | Receivable, payable, fiscal position, both payment terms and credit limit are commercial fields synchronised from the commercial partner to contacts. | N-U13-192 |
| VDR-U13-C302 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:656 | accounts.get(('res.company', move.company_id.id, account_type)) | FACT | payment_term line account computation | - | Receivable or payable line account: account of the previous term line of the move, else commercial partner property, else company partner property, else first active receivable or payable account of the company; then mapped by fiscal position. | N-U13-193 |
| VDR-U13-C303 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:766 | for field, model in self._get_property_accounts(additional_properties).items(): | FACT | chart load | - | Chart load stores receivable/payable defaults as company default values for new partners (not written on existing partners). | N-U13-193 |
| VDR-U13-C304 | FUNCTION MAPPING REQUIRED | account/models/partner.py:530 | Set a value greater than 0.0 | FACT | account_use_credit_limit enabled | - | credit_limit is a company-dependent float restricted to invoicing/readonly groups; use_partner_credit_limit is true when it differs from the company default. | N-U13-194 |
| VDR-U13-C305 | FUNCTION MAPPING REQUIRED | account/models/partner.py:691 | self.show_credit_limit = self.env.company.account_use_credit_limit | FACT | always | - | Credit limit is shown only when the company has the credit limit feature enabled. | N-U13-201 |
| VDR-U13-C306 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | sale module | - | UNKNOWN - EVIDENCE INSUFFICIENT: the enforcement of the credit limit at order or invoice confirmation is not in account or l10n_th; resolve by reading the sale module credit-limit check. | N-U13-195 |
| VDR-U13-C307 | FUNCTION MAPPING REQUIRED | account/models/partner.py:393 | AND account_move_line.reconciled IS NOT TRUE | FACT | always | - | Partner credit and debit totals sum unreconciled residuals on receivable/payable lines of posted entries in the root company tree. | N-U13-194 |
| VDR-U13-C308 | FUNCTION MAPPING REQUIRED | account/models/partner.py:574 | trust = fields.Selection([('good', 'Good Debtor') | FACT | always | - | Degree of trust is a company-dependent selection (good, normal, bad). | N-U13-190 |
| VDR-U13-C309 | FUNCTION MAPPING REQUIRED | account/models/partner.py:611 | Ask after 3 validations without edits | FACT | always | - | Partner autopost_bills selection (always, ask, never) defaults to ask and is required. | N-U13-190 |
| VDR-U13-C310 | FUNCTION MAPPING REQUIRED | account/models/partner.py:577 | invoice_sending_method = fields.Selection( | FACT | always | - | Invoice sending method (manual, email) and eInvoice format store are company-dependent partner fields. | N-U13-190 |
| VDR-U13-C311 | FUNCTION MAPPING REQUIRED | account/models/partner.py:608 | supplier_rank = fields.Integer(default=0, copy=False) | FACT | always | - | customer_rank and supplier_rank order partners by number of generated documents (default 0). | N-U13-199 |
| VDR-U13-C312 | FUNCTION MAPPING REQUIRED | account/models/partner.py:766 | invoicing address of another if they | FACT | parent_id change with posted lines | - | Changing a partner's parent is refused when the partner has journal lines and a different VAT than the new parent; otherwise commercial partner is updated on all lines. | N-U13-196 |
| VDR-U13-C313 | FUNCTION MAPPING REQUIRED | account/models/partner.py:806 | The partner cannot be deleted because | FACT | unlink partner | - | A partner referenced by draft or posted moves cannot be deleted. | N-U13-196 |
| VDR-U13-C314 | FUNCTION MAPPING REQUIRED | account/models/partner.py:559 | property_payment_term_id = fields.Many2one | FACT | always | - | Receivable, payable, fiscal position, payment terms, credit limit, trust and sending fields are declared company_dependent=True: each company stores its own value for the same partner. | N-U13-192 |
| VDR-U13-C315 | FUNCTION MAPPING REQUIRED | account/models/partner.py:545 | property_account_payable_id = fields.Many2one | OBSERVATION | DB | - | DB defaults for partners in the company: receivable account 112100 Trade Receivables, payable 212100 Trade Payables, credit limit 0, trust normal; DB has 10 payment terms and 7 partners (counts only). | N-U13-197 |
| VDR-U13-C316 | FUNCTION MAPPING REQUIRED | account/models/partner.py:613 | Automatically post bills for this trusted | FACT | always | - | Partner autopost setting exists to post bills of trusted vendors automatically. | N-U13-200 |
| VDR-U13-C317 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:769 | self.env['ir.default'].set(model, field | INFERENCE | chart load | - | Chart-load receivable and payable accounts are stored as defaults; they apply to partners created afterwards, and existing partners keep their stored value, so a later chart change does not repoint them (not executed). | N-U13-198 |
| VDR-U13-C318 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:22 | _inherit = ["analytic.mixin"] | FACT | always | - | Journal item inherits the analytic mixin so each line can carry an analytic_distribution JSON; the account module adds the inverse that syncs analytic lines. | N-U13-210 |
| VDR-U13-C319 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:439 | inverse="_inverse_analytic_distribution", | FACT | always | - | analytic_distribution on journal items has an inverse that triggers creation/update of analytic lines. | N-U13-216 |
| VDR-U13-C320 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:16 | analytic_distribution = fields.Json( | FACT | always | - | Distribution is a stored, computed, copyable, editable JSON; keys are analytic account ids (comma-separated when several plans are combined), values percentages. | N-U13-211 |
| VDR-U13-C321 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:202 | float_round(distribution, decimal_precision) | FACT | create/write | - | Percentages are rounded to the decimal precision named Percentage Analytic on create and write (key __update__ is passed through). | N-U13-211 |
| VDR-U13-C322 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:171 | precision_get('Percentage Analytic') | FACT | always | - | Precision comes from the decimal precision Percentage Analytic; DB value is 2. | N-U13-211 |
| VDR-U13-C323 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1252 | cache[arguments] or line.analytic_distribution | FACT | product lines or non-invoice moves | - | Default distribution is the union of the related-record distribution and the matching distribution-model result, otherwise the current value. | N-U13-212 |
| VDR-U13-C324 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1266 | "account_prefix": self.account_id.code, | FACT | always | - | Distribution model matching arguments: product, product category, partner, partner categories, account code prefix, company and related root plans. | N-U13-212 |
| VDR-U13-C325 | FUNCTION MAPPING REQUIRED | account/models/account_analytic_distribution_model.py:34 | def _get_applicable_models | FACT | always | - | Account-side distribution models add account prefix (comma or semicolon list), product and product category criteria. | N-U13-212 |
| VDR-U13-C326 | FUNCTION MAPPING REQUIRED | account/models/account_analytic_plan.py:12 | ('invoice', 'Invoice'), | FACT | always | - | Plan applicability business domains are extended with invoice and bill (vendor bill) in addition to general. | N-U13-221 |
| VDR-U13-C327 | FUNCTION MAPPING REQUIRED | account/models/account_analytic_plan.py:59 | def _get_score | FACT | always | - | Applicability rule score adds one point per matching account prefix and product category criterion; a non-matching criterion returns -1. | N-U13-213 |
| VDR-U13-C328 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:246 | def _get_applicability | FACT | always | - | Plan applicability is that of the highest-scoring rule for the company, else the plan default applicability (optional, mandatory, unavailable). | N-U13-213 |
| VDR-U13-C329 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:183 | if self.env.context.get('validate_analytic', False): | FACT | context validate_analytic | - | Mandatory plan enforcement (100% on each mandatory root plan) runs only when the context key validate_analytic is true. | N-U13-214 |
| VDR-U13-C330 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:196 | One or more lines require a | FACT | validate_analytic true | - | Missing 100% on a mandatory plan raises ValidationError; sums are per root plan with the plan precision. | N-U13-214 |
| VDR-U13-C331 | FUNCTION MAPPING REQUIRED | account/views/account_move_views.xml:706 | context="{'validate_analytic': True, 'disable_abnormal_invoice_detection': False}" | FACT | UI post/confirm buttons | - | The Post and Confirm buttons of the move form and the validation wizard confirm button set validate_analytic True. | N-U13-214 |
| VDR-U13-C332 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3138 | exchange_moves_to_post.with_context(validate_analytic=False)._post(soft=False) | FACT | exchange difference entries | - | Exchange difference entries are posted with validate_analytic explicitly False (mandatory-plan check skipped for them). | N-U13-222 |
| VDR-U13-C333 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:183 | validate_analytic | INFERENCE | posting without the UI context | RT | grep over account and analytic shows validate_analytic set only by the move form Post/Confirm buttons, the validation wizard button, has_invalid_analytics and the exchange-entry post; no default sets it in _post, so posting through other entry points (import, autopost cron, external call) does not run the mandatory check unless the caller sets the key (not exercised). | N-U13-222 |
| VDR-U13-C334 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2054 | def _compute_has_invalid_analytics | FACT | product lines on non receivable/payable/cash/credit-card accounts | - | has_invalid_analytics flags lines whose distribution violates plan applicability for domain invoice, bill or general. | N-U13-214 |
| VDR-U13-C335 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5709 | to_post.line_ids._create_analytic_lines() | FACT | posting | - | Posting creates analytic lines for all lines of moves being posted in one batch. | N-U13-215 |
| VDR-U13-C336 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3221 | def _create_analytic_lines | FACT | posting or distribution change on posted line | - | _create_analytic_lines first validates the distribution then creates analytic line records without re-triggering sync (skip_analytic_sync). | N-U13-215 |
| VDR-U13-C337 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3260 | amount = -self.balance * (100 - | FACT | distribution totals 100% on a plan | - | Analytic amount is -balance * percentage / 100; when a plan reaches 100% the amount is balance remainder to avoid drift. | N-U13-215 |
| VDR-U13-C338 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3297 | def _round_analytic_distribution_line | FACT | always | - | Analytic amounts are rounded to company currency and the rounding error is spread over lines in cent steps. | N-U13-215 |
| VDR-U13-C339 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3280 | 'category': 'invoice' if self.move_id.is_sale_document() else | FACT | always | - | Analytic line records date, partner, product, uom, quantity, general account, ref, move line link, responsible user (invoice user or current user), company and category invoice, vendor_bill or other. | N-U13-224 |
| VDR-U13-C340 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3243 | if not self.company_currency_id.is_zero(line_values.get('amount')): | FACT | always | - | Analytic lines with zero amount are not created. | N-U13-215 |
| VDR-U13-C341 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1457 | lines_to_modify.analytic_line_ids.unlink() | FACT | distribution edit on posted line | - | Editing the distribution of a posted line deletes its analytic lines and recreates them. | N-U13-216 |
| VDR-U13-C342 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1813 | Remove analytic lines created for draft | FACT | create or write of draft lines | - | Draft journal items do not keep analytic lines (removed after distribution update). | N-U13-216 |
| VDR-U13-C343 | FUNCTION MAPPING REQUIRED | account/models/account_analytic_line.py:43 | ondelete='cascade', | FACT | always | - | Analytic line move_line_id uses ondelete cascade. | N-U13-217 |
| VDR-U13-C344 | FUNCTION MAPPING REQUIRED | account/models/account_analytic_line.py:177 | affected_move_lines._update_analytic_distribution() | FACT | analytic line edit/delete | - | Writing amount, move_line_id or plan columns of an analytic line, or deleting it, recomputes the distribution of the linked journal item. | N-U13-217 |
| VDR-U13-C345 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3292 | -analytic_line.amount / line.balance * 100 | FACT | always | - | Distribution percentage is recomputed as -amount / balance * 100 for each analytic line, or 100 when balance is zero. | N-U13-217 |
| VDR-U13-C346 | FUNCTION MAPPING REQUIRED | account/models/account_analytic_line.py:70 | The journal item is not linked | FACT | always | - | general_account_id must equal the account of the linked journal item. | N-U13-219 |
| VDR-U13-C347 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2337 | if tax.analytic or not tax_rep.use_in_tax_closing | FACT | tax lines | - | Tax lines receive the base line distribution only for taxes flagged analytic or repartition lines not used in tax closing. | N-U13-218 |
| VDR-U13-C348 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:48 | access_account_analytic_accountant | FACT | always | - | Analytic accounts, plans and applicabilities are fully editable by the full accounting group; analytic distribution models by the invoicing group; analytic lines are editable by invoicing group. | N-U13-220 |
| VDR-U13-C349 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:408 | class AccountAnalyticApplicability | OBSERVATION | DB | - | DB has one analytic plan (Project), zero applicability rules and zero distribution models, so no plan is mandatory; counts of analytic accounts and lines are 1 and 2. | N-U13-220 |
| VDR-U13-C350 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3238 | distribution_on_each_plan corresponds to the proportion | FACT | always | - | Comment states the per-plan running proportion exists to give the real amount when a plan reaches 100% distribution. | N-U13-225 |
| VDR-U13-C351 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | runtime | RT | UNKNOWN - EVIDENCE INSUFFICIENT: posting with mandatory plans and multi-plan combined accounts was not executed; resolve by an AWT run with a mandatory plan and partial distribution. | N-U13-223 |
| VDR-U13-C352 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:16 | 'depends': [ | FACT | module l10n_th installed | - | l10n_th depends only on account_qr_code_emv and account. | N-U13-250 |
| VDR-U13-C353 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:20 | 'auto_install': ['account'], | FACT | always | - | l10n_th is auto-installed whenever account is installed (the chart itself is applied to a company by a separate loading step). | N-U13-249 |
| VDR-U13-C354 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:29 | 'license': 'LGPL-3', | FACT | always | - | Module license is LGPL-3 and the manifest declares country th (line 5). | N-U13-241 |
| VDR-U13-C355 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:22 | 'data/account_tax_report_data.xml', | FACT | always | - | Data files: Thai tax report definitions and invoice report view; demo file creates a TH demo company; post_init_hook preserves existing tags. | N-U13-240 |
| VDR-U13-C356 | FUNCTION MAPPING REQUIRED | l10n_th/__init__.py:6 | preserve_existing_tags_on_taxes(env, 'l10n_th') | FACT | module install | - | post_init_hook marks existing tax-tag xml records of l10n_th as noupdate so upgrades keep existing tags (helper in account chart_template). | N-U13-249 |
| VDR-U13-C357 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:14 | 'author': 'Almacom (http://almacom.co.th/)', | FACT | always | - | The manifest names author Almacom and depends only on the Community modules account and account_qr_code_emv; no source from Extra_Thailand was opened or used in this study. | N-U13-241 |
| VDR-U13-C358 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:9 | @template('th') | FACT | always | - | Template th is registered with @template; it sets no name or parent, so the chart name is derived from the country (Thailand). | N-U13-240 |
| VDR-U13-C359 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:23 | 'account_fiscal_country_id': 'base.th', | FACT | template th loaded | - | Company data: fiscal country Thailand, bank prefix 11120, cash prefix 11110, default sale tax output VAT 7%, purchase tax input VAT 7%, income account 411100, expense account 511100, exchange gain 421300 and loss 621200, suspense 111201, transfer account 111202, early-payment accounts, POS receivable, cash difference accounts. | N-U13-249 |
| VDR-U13-C360 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:41 | 'tax_exigibility': 'True' | FACT | template th loaded | - | Template sets the company cash-basis flag (string True) although none of the shipped taxes is cash-basis. | N-U13-249 |
| VDR-U13-C361 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:40 | 'account_stock_valuation_id': 'l10n_th_account_113100', | FACT | stock accounting installed | - | Stock valuation account value is passed on the company; it is dropped silently when the field does not exist in the registry. | N-U13-249 |
| VDR-U13-C362 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:6 | tax_output_vat | FACT | template th | - | Output VAT 7% (sale, group VAT 7%) has base lines tagged 1. Sales amount and tax lines tagged 5. Output tax on account 213200 with tax-closing flag; refund lines mirror. | N-U13-242 |
| VDR-U13-C363 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:2 | tax_input_vat | FACT | template th | - | Input VAT 7% (purchase) tags 6 and 7 and posts tax to account 114200. | N-U13-242 |
| VDR-U13-C364 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:14 | tax_output_vat_0 | FACT | template th | - | Output VAT 0% base is tagged both 1. Sales amount and 2. Less sales subject to 0% tax rate; tax lines are tagged 5. Output tax on account 213200. | N-U13-242 |
| VDR-U13-C365 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:22 | tax_output_vat_exempted | FACT | template th | - | Output VAT exempt base is tagged 1. Sales amount and 3. Less exempted sales; tax lines are tagged 5. Output tax on account 213200. | N-U13-242 |
| VDR-U13-C366 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:26 | tax_wht_co_1 | FACT | template th | - | Purchase withholding for companies at -1,-2,-3,-5 percent (transport, advertising, service, rental), base tag Income PND53 and tax tag PND53 on account 213302, no tax-closing flag. | N-U13-243 |
| VDR-U13-C367 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:42 | tax_wht_pers_1 | FACT | template th | - | Purchase withholding for individuals same rates with tags Income PND3 and PND3 on account 213301. | N-U13-243 |
| VDR-U13-C368 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:62 | tax_wht_income_2 | FACT | template th | CONTRA | Sales-side withholding tax (taxes withheld by customers) is a negative-percent tax forced tax_excluded posting to account 114300; DB shows 114300 is of type asset_current (not receivable), CONTRA the prior candidate map MODULE_l10n_th section 6 which calls it receivable-type. | N-U13-243 |
| VDR-U13-C369 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax.group-th.csv:6 | tax_group_vat_7 | FACT | template th | - | Five tax groups: WHT 1,2,3,5 percent (payable 213500, receivable 114401) and VAT 7% (payable 213400, receivable 114400), all country Thailand. | N-U13-242 |
| VDR-U13-C370 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:4 | <field name="name">Tax Report</field> | FACT | module data | - | Tax Report (country Thailand, availability country, allow foreign VAT) with output tax, input tax, VAT payable/excess, carried forward and net tax lines driven by tax-tag expressions and aggregations. | N-U13-244 |
| VDR-U13-C371 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:126 | OUTPUTTAX_TAX.balance - INPUTTAX_TAX.balance | FACT | module data | - | Line 8 Tax payable = output tax minus input tax; line 9 excess is the reverse (INPUTTAX_TAX minus OUTPUTTAX_TAX). | N-U13-244 |
| VDR-U13-C372 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:152 | most_recent | FACT | module data | - | Line 10 excess carried forward uses an external-value expression with formula most_recent plus a tag and an aggregation of applied carryover balance. | N-U13-244 |
| VDR-U13-C373 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:228 | <field name="name">PND53</field> | FACT | module data | - | PND53 report: total income (tag Income PND53), remittance (tag PND53), surcharge (tag SUR53) and total. | N-U13-244 |
| VDR-U13-C374 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:292 | <field name="name">PND3</field> | FACT | module data | - | PND3 report: income (tag Income PND3), remittance (tag PND3), surcharge (tag SUR3) and total. | N-U13-244 |
| VDR-U13-C375 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:273 | <field name="formula">SUR53</field> | INFERENCE | module data | - | Surcharge tags SUR53 and SUR3 exist in reports but no shipped tax references them (template taxes use only Income PND and PND tags), so surcharge lines are fed only by manual tagging. | N-U13-252 |
| VDR-U13-C376 | FUNCTION MAPPING REQUIRED | l10n_th/models/account_move.py:10 | return 'l10n_th.report_invoice_document' | FACT | company fiscal country TH | - | Invoice report selection returns the Thai invoice document when the company fiscal country is Thailand; otherwise standard. | N-U13-245 |
| VDR-U13-C377 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:15 | <t name="invoice_title">Tax Invoice</t> | FACT | Thai fiscal country | - | Thai invoice template shows partner branch label after VAT and replaces the invoice title by Tax Invoice. | N-U13-245 |
| VDR-U13-C378 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:36 | <field name="domain">[('country_code', '=', 'TH'), ('journal_id.type', '=', | FACT | always | - | Commercial Invoice report is bound to moves with country TH in sale journals. | N-U13-245 |
| VDR-U13-C379 | FUNCTION MAPPING REQUIRED | l10n_th/models/ir_actions_report.py:13 | Only invoices could be printed. | FACT | commercial invoice report on non invoices | - | Printing the commercial invoice on any record that is not an invoice or receipt raises UserError. | N-U13-245 |
| VDR-U13-C380 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_partner.py:17 | partner.env._("Branch %(code)s", code=code) | FACT | company partner in Thailand | - | l10n_th_branch_name (non-stored) is empty unless the partner is a company in Thailand; then Branch plus company_registry, or Headquarter when registry is empty. | N-U13-248 |
| VDR-U13-C381 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:12 | ('merchant_tax_id', 'Merchant Tax ID'), | FACT | always | - | Bank proxy types are extended with ewallet_id, merchant_tax_id and mobile (ondelete set default). | N-U13-246 |
| VDR-U13-C382 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:24 | The Merchant Tax ID must be | FACT | bank with country TH | - | Merchant tax id must be 13 digits and mobile number 10 digits; other proxy types except none are rejected for Thai bank accounts. | N-U13-247 |
| VDR-U13-C383 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:47 | re.sub(r"^0", "66", self.proxy_value).zfill(13) | FACT | proxy mobile | - | For QR payload a leading 0 of the mobile number is replaced by 66 and padded to 13 digits. | N-U13-246 |
| VDR-U13-C384 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:49 | (0, 'A000000677010111'), | FACT | bank with country TH | - | Merchant account information uses tag 29 with application id A000000677010111 and a sub-tag 1 mobile, 2 merchant tax id or 3 ewallet. | N-U13-246 |
| VDR-U13-C385 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:57 | if currency.name not in ['THB']: | FACT | qr method emv_qr, bank TH | - | EMV QR for Thai banks is allowed only for THB; the user-visible message names PayNow (copied wording). | N-U13-246 |
| VDR-U13-C386 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:37 | bank_th.display_qr_setting = True | FACT | bank with country TH | - | EMV QR settings tab is displayed for Thai bank accounts with proxy keys ewallet_id, merchant_tax_id, mobile. | N-U13-246 |
| VDR-U13-C387 | FUNCTION MAPPING REQUIRED | l10n_th/models/res_bank.py:65 | The PayNow Type must be either | FACT | qr generation for TH bank | - | QR code generation errors if the proxy type is not one of the three Thai types. | N-U13-246 |
| VDR-U13-C388 | FUNCTION MAPPING REQUIRED | l10n_th/demo/demo_company.xml:33 | <value>th</value> | FACT | demo data loaded | - | Demo data creates a TH Company and loads chart th with demo on it (demo not loaded in the restored DB). | N-U13-249 |
| VDR-U13-C389 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:178 | 'ubl_sg': {'countries': ['SG'], 'on_peppol': False} | FACT | account_edi_ubl_cii installed | - | UBL/CII format country map lists FR, DE, NL, SG, AU/NZ and EU Peppol countries; Thailand is absent, as is TH in the EAS mapping (grep on TH found nothing), so no Thai e-invoice format exists in Community. | N-U13-253 |
| VDR-U13-C390 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:6 | class AccountChartTemplate(models.AbstractModel): | OBSERVATION | DB | - | l10n_th defines no function for fiscal positions, account groups, journals or reconcile models: the DB has 0 fiscal positions, 0 account groups, 7 journals from the root template (and stock) and 2 reconcile models. | N-U13-252 |
| VDR-U13-C391 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:19 | @template('th', 'res.company') | OBSERVATION | DB | - | DB: module l10n_th installed, company chart th, fiscal country Thailand, currency THB, 5 tax groups, 13 tax tags (country Thailand), 3 Thai tax reports plus generic ones, one invoice report action. | N-U13-251 |
| VDR-U13-C392 | FUNCTION MAPPING REQUIRED | l10n_th/models/ir_actions_report.py:8 | def _pre_render_qweb_pdf | FACT | always | - | Core behaviour touched by l10n_th: invoice report document selection, a pre-render guard for its own report, extra bank proxy types and QR rules; nothing alters tax computation, posting or lock logic. | N-U13-250 |
| VDR-U13-C393 | FUNCTION MAPPING REQUIRED | l10n_th/__manifest__.py:12 | Thai accounting chart and localization. | FACT | always | - | Manifest description: chart of accounts and localization for Thailand. | N-U13-255 |
| VDR-U13-C394 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | legal review | - | UNKNOWN - EVIDENCE INSUFFICIENT: conformity of the shipped tax grids, reports and invoice layout with current statutory Thai requirements (tax invoice content, numbering, e-tax) is outside the source evidence. | N-U13-254 |
| VDR-U13-C395 | FUNCTION MAPPING REQUIRED | account_edi/models/account_edi_document.py:26 | state = fields.Selection([('to_send', 'To Send') | FACT | account_edi installed | - | account.edi.document links a move and an EDI format with state to_send, sent, to_cancel, cancelled, last error (html) and blocking_level info, warning or error; attachment readable only by system group. | N-U13-275 |
| VDR-U13-C396 | FUNCTION MAPPING REQUIRED | account_edi/models/account_edi_document.py:41 | UNIQUE(edi_format_id, move_id) | FACT | always | - | Only one EDI document per move per format. | N-U13-279 |
| VDR-U13-C397 | FUNCTION MAPPING REQUIRED | account_edi/models/account_edi_format.py:58 | def _get_move_applicability | FACT | always | - | Base format class returns no applicability, needs no web service, is compatible only with sale journals, is enabled by default and reports no configuration errors; concrete formats must override. | N-U13-270 |
| VDR-U13-C398 | FUNCTION MAPPING REQUIRED | account_edi/models/account_edi_format.py:40 | activate cron | FACT | format created needing web services | - | Creating a format that needs web services activates the EDI cron; formats are added to compatible journals by recompute. | N-U13-287 |
| VDR-U13-C399 | FUNCTION MAPPING REQUIRED | account_edi/models/account_edi_format.py:8 | _name = 'account.edi.format' | INFERENCE | Community modules installed here | - | Concrete account.edi.format overrides exist in l10n_sa_edi, l10n_es_edi_sii, l10n_eg_edi_eta and l10n_sa_edi_pos (grep); none is part of this study or installed, and account_edi_ubl_cii does not inherit the format model, so no format is registered for the Thai company. | N-U13-271 |
| VDR-U13-C400 | FUNCTION MAPPING REQUIRED | account_edi/models/account_move.py:246 | Invalid invoice configuration: | FACT | journal has applicable format | - | On post, for each format enabled on the journal that reports applicability, configuration errors raise UserError; otherwise a document is created (or reset) in state to_send and non web-service documents are processed immediately, then the cron is triggered. | N-U13-274 |
| VDR-U13-C401 | FUNCTION MAPPING REQUIRED | account_edi/models/account_move.py:43 | def _compute_edi_state | FACT | always | - | Move edi_state aggregates only web-service documents: sent if all sent, cancelled if all cancelled, else to_send, else to_cancel, else empty. | N-U13-275 |
| VDR-U13-C402 | FUNCTION MAPPING REQUIRED | account_edi/models/account_edi_document.py:11 | DEFAULT_BLOCKING_LEVEL = 'error' | FACT | job result handling | - | Success moves a document to sent and clears errors; failure stores the error text and blocking level (default error). | N-U13-275 |
| VDR-U13-C403 | FUNCTION MAPPING REQUIRED | account_edi/models/account_edi_document.py:157 | The user requested a cancellation of | FACT | cancel job success | - | A successful cancel moves the document to cancelled and, when all web-service documents are cancelled and the move is posted, resets the move to draft then cancels it. | N-U13-276 |
| VDR-U13-C404 | FUNCTION MAPPING REQUIRED | account_edi/models/account_edi_document.py:81 | documents = self.filtered(lambda d: d.state == | FACT | always | - | Jobs exclude documents blocked by an error; documents are batched per format, state, company and optional format batching key, else one job per move. | N-U13-277 |
| VDR-U13-C405 | FUNCTION MAPPING REQUIRED | account_edi/models/account_edi_document.py:222 | documents.lock_for_update() | FACT | web-service jobs | - | Web-service jobs lock documents, moves and attachments; on LockError the job is skipped (cron) or a UserError is raised (manual); a commit is made between jobs when several run. | N-U13-277 |
| VDR-U13-C406 | FUNCTION MAPPING REQUIRED | account_edi/data/cron.xml:6 | model._cron_process_documents_web_services(job_count=20) | FACT | always | - | EDI cron runs daily with at most 20 jobs per run and is shipped inactive (active False in the data file). | N-U13-287 |
| VDR-U13-C407 | FUNCTION MAPPING REQUIRED | account_edi/models/account_edi_document.py:244 | ('move_id.state', '=', 'posted'), | FACT | cron run | - | Cron selects documents in to_send or to_cancel on posted moves with blocking level not error and triggers itself again when jobs remain (lines 242-251). | N-U13-287 |
| VDR-U13-C408 | FUNCTION MAPPING REQUIRED | account_edi/models/account_move.py:296 | because an electronic document has already | FACT | reset to draft | - | Reset to draft is refused while a web-service document is sent and cancellable; the user must request EDI cancellation instead. | N-U13-276 |
| VDR-U13-C409 | FUNCTION MAPPING REQUIRED | account_edi/models/account_move.py:312 | move._check_fiscal_lock_dates() | FACT | request EDI cancellation | - | Requesting EDI cancellation first checks fiscal lock dates and moves sent web-service documents to to_cancel; it can be abandoned back to sent. | N-U13-276 |
| VDR-U13-C410 | FUNCTION MAPPING REQUIRED | account_edi/models/account_move.py:275 | def button_cancel(self): | FACT | move cancel | - | Cancelling a move sets unsent documents to cancelled and sent ones to to_cancel, processes sync documents and triggers the cron. | N-U13-276 |
| VDR-U13-C411 | FUNCTION MAPPING REQUIRED | account_edi/models/account_move.py:230 | edi_documents_to_send = self.edi_document_ids.filtered | FACT | sending invoices | - | A move with a document in to_send is not ready to be sent by mail. | N-U13-274 |
| VDR-U13-C412 | FUNCTION MAPPING REQUIRED | account_edi/models/account_journal.py:38 | Cannot deactivate (%s) on this journal | FACT | journal edit | - | A format with pending to_send/to_cancel web-service documents cannot be removed from a journal; for sync formats the pending documents are deleted. | N-U13-278 |
| VDR-U13-C413 | FUNCTION MAPPING REQUIRED | account_edi/models/ir_attachment.py:16 | You can't unlink an attachment being | FACT | attachment delete | - | Attachments of EDI documents of web-service formats cannot be deleted. | N-U13-279 |
| VDR-U13-C414 | FUNCTION MAPPING REQUIRED | account_edi/wizard/account_resequence.py:20 | have already been sent and cannot | FACT | resequence wizard | - | Moves with sent web-service documents cannot be resequenced. | N-U13-279 |
| VDR-U13-C415 | FUNCTION MAPPING REQUIRED | account_edi/models/ir_actions_report.py:39 | edi_document.edi_format_id._prepare_invoice_report(writer, edi_document) | FACT | single sale invoice PDF, not draft | - | Invoice PDF rendering lets each EDI document embed content through the format hook. | N-U13-270 |
| VDR-U13-C416 | FUNCTION MAPPING REQUIRED | account_edi/security/ir.model.access.csv:5 | access_account_edi_document_group_invoice | FACT | always | - | EDI formats and documents are readable by internal users and fully editable by the Invoicing group. | N-U13-278 |
| VDR-U13-C417 | FUNCTION MAPPING REQUIRED | account_edi/data/cron.xml:9 | <field name="active">False</field> | OBSERVATION | DB | - | DB: 0 EDI formats, 0 EDI documents, EDI cron inactive. | N-U13-287 |
| VDR-U13-C418 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:167 | def _get_ubl_cii_formats_info | FACT | account_edi_ubl_cii installed | - | Formats: ubl_bis3 (EU Peppol countries, on Peppol, embeds attachments), xrechnung (DE), nlcius (NL), ubl_a_nz (NZ, AU), ubl_sg (SG), facturx (FR), zugferd (DE). | N-U13-271 |
| VDR-U13-C419 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:38 | ('ubl_sg', "Singapore (BIS Billing 3.0 SG)"), | FACT | always | - | Partner invoice_edi_format selection is extended with seven UBL/CII choices so any partner can be set manually regardless of country. | N-U13-271 |
| VDR-U13-C420 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:195 | def _get_suggested_ubl_cii_edi_format | FACT | always | - | Suggestion by partner country returns the format with smallest sequence (xrechnung for Leitweg EAS); countries not mapped (including Thailand) yield no suggestion. | N-U13-290 |
| VDR-U13-C421 | FUNCTION MAPPING REQUIRED | account/models/partner.py:705 | def _get_suggested_invoice_edi_format | FACT | only account installed | - | The base suggested invoice format returns False and is not overridden by account_edi_ubl_cii (overrides exist only in country modules such as l10n_pl_edi); the stored partner format, when empty, therefore leaves the send flow without a UBL format. | N-U13-290 |
| VDR-U13-C422 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:332 | def _get_edi_builder | FACT | always | - | Format to builder mapping: xrechnung to ubl_de, facturx and zugferd to cii, ubl_a_nz, nlcius to ubl_nl, ubl_bis3, ubl_sg. | N-U13-271 |
| VDR-U13-C423 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:363 | def _need_ubl_cii_xml | FACT | send or export | - | XML is needed when none is stored, the move is a sale document (or an exportable self-billed purchase) and the format is a UBL/CII format. | N-U13-280 |
| VDR-U13-C424 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:130 | xml_content, errors = ( | FACT | Send and print with UBL/CII format | - | Before the PDF is rendered the builder exports the invoice; errors are placed in invoice_data with error_but_continue so a fallback PDF can still be produced; success stores attachment values bound to field ubl_cii_xml_file. | N-U13-280 |
| VDR-U13-C425 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:166 | Always silently generate a Factur-X and | FACT | PDF generated in send flow | - | A Factur-X XML is always generated and embedded into the invoice PDF unless the chosen format already is Factur-X; no country condition on this step. | N-U13-282 |
| VDR-U13-C426 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:201 | writer.convert_to_pdfa() | FACT | format facturx or zugferd, or commercial partner FR or DE (not EAS 0204), and company fiscal country FR or DE | - | PDF/A conversion with metadata is attempted only when the invoice country (company fiscal country) is France or Germany; failures are logged, not raised. | N-U13-282 |
| VDR-U13-C427 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:229 | def _postprocess_invoice_ubl_xml | FACT | UBL formats (not facturx/zugferd) | - | For UBL formats the invoice PDF (and supported extra attachments) is inserted as AdditionalDocumentReference elements at an anchor node. | N-U13-281 |
| VDR-U13-C428 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:311 | self.env['ir.attachment'].with_user(SUPERUSER_ID).create(attachments_vals) | FACT | invoice sent successfully | - | Generated XML attachments are created as superuser and linked to the moves. | N-U13-280 |
| VDR-U13-C429 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:45 | Please fill in your company's VAT | FACT | Peppol format selected | - | Info alerts prompt completing company or partner Peppol address (EAS and endpoint) and installing the French Chorus Pro module when applicable. | N-U13-285 |
| VDR-U13-C430 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2719 | def _export_invoice(self, invoice): | FACT | UBL export | - | Export flow: validate taxes, build document values and nodes, run constraints, render XML; returns XML bytes and a set of error strings. | N-U13-283 |
| VDR-U13-C431 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:396 | def _validate_taxes | FACT | UBL/CII export | - | Tax repartition structure is validated before export and converted into a ValidationError naming the tax. | N-U13-283 |
| VDR-U13-C432 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:550 | Each invoice line should have at | FACT | UBL/CII export | - | Common constraint: every product line that requires a tax must have at least one tax. | N-U13-283 |
| VDR-U13-C433 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:788 | def _cii_constraints | FACT | CII/Factur-X export | - | CII constraints check payment instructions (bank account number), seller postal address, identifier and contact, buyer postal address, intra-community delivery and Canary IGI rate. | N-U13-283 |
| VDR-U13-C434 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:307 | def _invoice_constraints_peppol_en16931_ubl | FACT | UBL BIS3 export | - | BIS3 adds Peppol national rules by supplier country (Norway VAT format, Belgian company registry checks). | N-U13-283 |
| VDR-U13-C435 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:420 | if tax.ubl_cii_tax_category_code: | FACT | UBL/CII export | - | Tax category code (S, E, Z, AE, G, K, L, M, O, B) comes from the tax field, else is predicted from supplier/customer countries, zero amount and negative-factor taxes. | N-U13-284 |
| VDR-U13-C436 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_tax.py:7 | ubl_cii_tax_category_code = fields.Selection( | FACT | always | - | Taxes carry optional tax category code and exemption reason code; codes AE, E, G, O, K require an exemption reason. | N-U13-284 |
| VDR-U13-C437 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:279 | def _compute_peppol_eas | FACT | partner country in EAS map | - | Partner peppol_eas and peppol_endpoint are computed and stored from country, VAT and company registry using a country to scheme mapping; endpoint format is validated. | N-U13-285 |
| VDR-U13-C438 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:155 | def _check_peppol_fields | FACT | endpoint and EAS set | - | Constraint validates endpoint format by scheme (e.g. 10 digits for 0208, SIRET check for 0009, email for EM). | N-U13-285 |
| VDR-U13-C439 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:64 | def _get_invoice_legal_documents | FACT | export XML action | - | Export XML returns the stored attachment or, with fallback, builds one on demand when the partner format requires XML. | N-U13-280 |
| VDR-U13-C440 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:251 | def _get_import_file_type | FACT | file import | - | Imported XML is classified (UBL attached document, CII, BIS3, XRechnung, NLCIUS, A-NZ, SG, UBL 2.0/2.1) from customization id or version id; decoder priority is 20. | N-U13-286 |
| VDR-U13-C441 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:564 | def _import_invoice_ubl_cii | FACT | file import | - | Import refuses invoices that already have lines, sets move type from journal type and document sign, fills the invoice in a creation context, corrects tax totals within 0.05 and logs a message with source attachments. | N-U13-286 |
| VDR-U13-C442 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1453 | def _import_invoice_retrieve_taxes | FACT | file import | - | Taxes, products, UoM, accounts and partners are retrieved through search plans (predictive and exact) rather than created. | N-U13-286 |
| VDR-U13-C443 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/data/ir_config_parameter_data.xml:5 | account_edi_ubl_cii.disable_pdf_in_xml | OBSERVATION | DB | - | Config parameter disable_pdf_in_xml (False) controls extracting PDFs embedded in imported XML. | N-U13-287 |
| VDR-U13-C444 | FUNCTION MAPPING REQUIRED | account_add_gln/models/res_partner.py:7 | global_location_number = fields.Char(string="GLN" | FACT | account_add_gln installed | - | Partner gets a free-text Char field global_location_number (GLN); the entire model extension is this single field with no constraint or format check. | N-U13-272 |
| VDR-U13-C445 | FUNCTION MAPPING REQUIRED | account_add_gln/views/res_partner_views.xml:10 | invisible="type != 'delivery'" | FACT | always | - | GLN field is displayed on the sales and purchases page and in the child address form only when the partner type is delivery. | N-U13-272 |
| VDR-U13-C446 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:124 | rslt.append(('emv_qr', _("EMV Merchant-Presented QR-code"), 30)) | FACT | account_qr_code_emv installed | - | EMV QR is registered as a QR method with sequence 30 on bank accounts. | N-U13-273 |
| VDR-U13-C447 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:90 | qr_code_str += '6304' | FACT | qr method emv_qr | - | Payload concatenates tag-length-value fields (format indicator, dynamic QR, merchant account info, category 0000, currency code, amount, country, merchant name 25 chars, city 15 chars, optional reference) then CRC16 over the string. | N-U13-273 |
| VDR-U13-C448 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/models/res_bank.py:112 | return _("Missing Merchant Account Information.") | FACT | qr method emv_qr | - | QR is refused when merchant info, partner city, proxy type or proxy value is missing; base class supplies no merchant info so only country modules (Thailand) can produce a QR. | N-U13-273 |
| VDR-U13-C449 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/const.py:36 | 'THB': '764', | FACT | qr method emv_qr | - | A fixed mapping from currency name to numeric ISO code (including THB 764) is used; a currency missing from the mapping raises KeyError at payload build. | N-U13-273 |
| VDR-U13-C450 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6795 | def _generate_qr_code(self, silent_errors=False): | FACT | invoice display_qr_code | - | An invoice uses its qr_code_method if set (error raised if not eligible) else the first eligible method in sequence; method is stored after successful generation. | N-U13-273 |
| VDR-U13-C451 | FUNCTION MAPPING REQUIRED | account_qr_code_emv/views/res_bank_views.xml:11 | <page string="EMV QR Settings" | FACT | bank with display_qr_setting | - | Bank form gets an EMV QR Settings page (proxy type, proxy value, include reference) only when the country module enables it. | N-U13-273 |
| VDR-U13-C452 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/__manifest__.py:39 | 'auto_install': True, | FACT | always | - | account_edi_ubl_cii depends on account only and is auto-installed; account_edi depends on account; account_qr_code_emv depends on account; account_add_gln depends on account and is auto-installed. | N-U13-288 |
| VDR-U13-C453 | FUNCTION MAPPING REQUIRED | account_edi/__manifest__.py:15 | 'depends' : ['account'], | FACT | always | - | account_edi manifest depends only on account and ships a cron, views and ACL. | N-U13-288 |
| VDR-U13-C454 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:170 | xml_facturx = self.env['account.edi.xml.cii']._export_invoice(invoice)[0] | INFERENCE | sending an invoice from any company | RT | The embedded Factur-X is built with no country test and its error set is discarded, so a Thai company invoice sent by this flow carries a CII attachment that is not required locally and may be incomplete (not executed). | N-U13-291 |
| VDR-U13-C455 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | runtime | RT | UNKNOWN - EVIDENCE INSUFFICIENT: behaviour of Send and Print when the Factur-X export raises (for example invalid tax structure) and the actual file naming for Thai invoices were not executed; resolve by an AWT send test. | N-U13-292 |
| VDR-U13-C456 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/__manifest__.py:11 | retrieve the PDF with only the | FACT | always | - | Manifest states the PDF is embedded in the XML for UBL formats so a receiver can obtain the PDF from the XML alone. | N-U13-293 |
| VDR-U13-C457 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:55 | <record id="group_account_invoice" model="res.groups"> | FACT | always | - | Group Invoicing implies the internal user group; Basic implies Invoicing; Show Full Accounting Features implies Basic and Readonly; Administrator implies Invoicing and is given to the root and admin users. | N-U13-320 |
| VDR-U13-C458 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:73 | <record id="group_account_manager" model="res.groups"> | FACT | always | - | Administrator group carries privilege Accounting and is assigned to the root and administrator users at install. | N-U13-320 |
| VDR-U13-C459 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:86 | <record id="group_cash_rounding" model="res.groups"> | FACT | always | - | Additional technical groups: cash rounding, partial purchase deductibility, delivery address, inalterability, validate bank account. | N-U13-332 |
| VDR-U13-C460 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:77 | access_account_tax_manager | FACT | always | - | account.tax: read for internal users, readonly and invoicing groups; create/write/delete only for account manager. | N-U13-321 |
| VDR-U13-C461 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:89 | access_account_tax_group_manager | FACT | always | - | account.tax.group and account.tax.repartition.line: read-only except account manager (full). | N-U13-321 |
| VDR-U13-C462 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:68 | access_account_account_manager | FACT | always | - | account.account: full for account manager; read for readonly, invoicing, internal user and partner manager groups. | N-U13-321 |
| VDR-U13-C463 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:21 | access_account_fiscal_position_product_manager | FACT | always | - | Fiscal positions and account mappings: full for account manager, read for all internal users. | N-U13-321 |
| VDR-U13-C464 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:6 | access_res_currency_account_manager | FACT | always | - | Currency and currency rate: full for account manager group (base also grants full to its own administrator group and read to users). | N-U13-324 |
| VDR-U13-C465 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:62 | access_account_group_manager | FACT | always | - | Account groups: full for manager, read for basic and readonly. | N-U13-321 |
| VDR-U13-C466 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:79 | access_account_account_tax,account.account.tag | FACT | always | - | Account tags: full for the full-accounting group, read for invoicing, readonly and internal users. | N-U13-321 |
| VDR-U13-C467 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:2 | access_account_cash_rounding_readonly | FACT | always | - | Cash rounding: read-only for readonly group, full for Invoicing group. | N-U13-321 |
| VDR-U13-C468 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:52 | access_account_analytic_distribution_invoice | FACT | always | - | Analytic distribution models are fully editable by the Invoicing group, read by readonly group. | N-U13-321 |
| VDR-U13-C469 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:171 | <field name="name">Tax multi-company</field> | FACT | always | - | Global rule: taxes visible when company_id is a parent of the user's allowed companies; same pattern for tax groups, fiscal positions, account groups; repartition lines also visible when company empty; accounts use company_ids parent_of. | N-U13-322 |
| VDR-U13-C470 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:63 | multi-company currency rate rule | FACT | always | - | Global rule on currency rates: company is a parent of allowed companies or empty. | N-U13-324 |
| VDR-U13-C471 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:30 | _check_company_domain = models.check_company_domain_parent_of | FACT | always | - | Taxes and tax groups use check_company_auto with parent-of domain, so records of a parent company can be used by branches. | N-U13-322 |
| VDR-U13-C472 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:25 | _check_company_domain = models.check_companies_domain_parent_of | FACT | always | - | Account company check uses the multi-company parent-of domain on company_ids. | N-U13-322 |
| VDR-U13-C473 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:246 | if duplicates := self.sudo().search(Domain.OR(domains)): | INFERENCE | tax name collision | - | Tax name uniqueness is checked with sudo across the company tree and the error lists the clashing taxes and company names, which could reveal names the user cannot otherwise see. | N-U13-327 |
| VDR-U13-C474 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:184 | raise AccessError(_("Only administrators can install chart | FACT | always | - | Loading or reloading a chart template is restricted to system administrators. | N-U13-323 |
| VDR-U13-C475 | FUNCTION MAPPING REQUIRED | account/data/service_cron.xml:17 | model._cron_account_move_send() | FACT | always | - | Daily cron Send invoices automatically processes up to 10 posted moves with pending sending data, as the root user. | N-U13-325 |
| VDR-U13-C476 | FUNCTION MAPPING REQUIRED | account/data/service_cron.xml:9 | model._autopost_draft_entries() | FACT | always | - | Daily cron posts draft auto-post entries dated up to today (engine in U11). | N-U13-325 |
| VDR-U13-C477 | FUNCTION MAPPING REQUIRED | account/data/service_cron.xml:13 | ir_cron_account_move_send | OBSERVATION | DB | - | DB: send-invoices cron active (1 day), auto-post cron active (1 day), EDI web-service cron inactive; no cron belongs to l10n_th, account_qr_code_emv, account_add_gln or account_edi_ubl_cii. | N-U13-325 |
| VDR-U13-C478 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:74 | access_account_tax_internal_user | OBSERVATION | DB | - | DB ir_model_access rows for tax, tax group, repartition, account, fiscal position, currency, cash rounding, account group, tag and EDI models match the CSV (tax: manager 1111, invoicing/readonly/internal 1000; cash rounding: Invoicing 1111, readonly 1000). | N-U13-329 |
| VDR-U13-C479 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:189 | <field name="name">Account fiscal Mapping company rule</field> | OBSERVATION | DB | - | DB ir_rule rows are global with domains company parent_of company_ids for tax, tax group, repartition, account (company_ids), fiscal position, account group and currency rate. | N-U13-322 |
| VDR-U13-C480 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5131 | unlink_except_tax_used | FACT | tax delete | - | Failure paths of taxes: delete when used, duplicate name, invalid repartition, group nesting or cycle, tax group country mismatch, company change when used, cash-basis transition account not reconcilable. | N-U13-326 |
| VDR-U13-C481 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1265 | raise RedirectWarning( | FACT | chart load | - | Chart load failure paths: non-admin, regional umbrella template, missing tax tag (redirect to update localization), module install; demo failures are swallowed. | N-U13-326 |
| VDR-U13-C482 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:143 | invoice_data['error_but_continue'] = True | FACT | XML export errors | - | XML export errors are reported as a titled error list and allow a fallback PDF; other exceptions (for example invalid tax structure) raise ValidationError. | N-U13-326 |
| VDR-U13-C483 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:37 | shallow access | FACT | always | - | Security comment: with only Invoicing installed only the Invoicing and Administrator groups should be used; the other groups give shallow access to accounting features. | N-U13-331 |
| VDR-U13-C484 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | DB user data | RT | UNKNOWN - EVIDENCE INSUFFICIENT: assignment of users to the accounting groups and resulting effective permissions were not studied (user data excluded); resolve by an AWT role test. | N-U13-330 |

---

## 12. Report items

**DISCOVERED SUPPORTING MODULES** (read only as far as needed): `base` (res_currency, security rules), `analytic` (mixin, plan applicability; U02 owns), `base_vat` (imported by `account/models/partner.py` and `company.py` for reference tables; state `uninstalled` in DB, so `_run_vat_checks` in `account` is the no-op stub — VAT numbers are not validated in this DB), `product` (default taxes, account getters), `account_peppol` (named in alerts and company constants, not installed), country modules named by grep only (`l10n_sa_edi`, `l10n_es_edi_sii`, `l10n_eg_edi_eta`, `l10n_pl_edi`, `l10n_dk_nemhandel`, `l10n_tr_nilvera`, `l10n_fr_pdp`, `l10n_hr_edi`, `l10n_it_edi`) — not opened beyond the grep lines.

**Contradictions with prior evidence (CONTRA):** (a) prior candidate map `MODULE_l10n_th` section 6 calls account 114300 a receivable-type tax-credit account; DB shows type asset_current (see `th.tax.wht.sale`). (b) B01 section 2.1 cites 181 company-prefixed chart records under `account`; observed 179 (see `coa.db.ids`). No contradiction found with the prior counts of 144 accounts, 18 taxes, 5 tax groups, surcharge-tag gap, QR rules. DELTA additions to prior evidence: zero/exempt VAT taxes fall into group WHT 1% by fallback; transfer-prefix literal; Factur-X always embedded in send flow; `deprecated` guard on accounts is dead code; DB cron/ACL confirmations.

**Runtime/AWT-required (RT) list:** numeric tax results for Thai combos (VDR-U13-C088); reload of th (VDR-U13-C218); chart switch with entries (VDR-U13-C184); USD conversion with no rate rows (VDR-U13-C259); fiscal-year change vs sequence ranges (VDR-U13-C296); mandatory analytic plan on programmatic post (VDR-U13-C333, VDR-U13-C351); Send & Print with embedded Factur-X (VDR-U13-C454, VDR-U13-C455); fiscal position behaviour (VDR-U13-C131); role assignment (VDR-U13-C484); Thai statutory conformity (VDR-U13-C394).

**Hand-offs:** U01 base currency/rate model; U02 analytic plans/accounts/applicability engine; U11 posting, lock engine, autopost cron, tax closing, sequences; U12 payments, reconcile, exchange difference, payment terms, cash-basis settlement.

**Capabilities covered:** CAP-U13-01 to CAP-U13-10 (all ten attempted; e-invoicing is breadth-only by instruction; field-level UBL/CII mappings and PINT/country format files were not studied).
