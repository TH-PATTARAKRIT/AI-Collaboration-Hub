# PND3 / PND53 Filing & Export Module — Deep-Inspection Proof

**Deliverable ID:** 04_ACC_WHT_PND3_PND53_FILING_PROOF
**Prepared by:** Team A4 — PND3/PND53 Filing Proof Team
**Repo:** `TH-PATTARAKRIT/AI-Collaboration-Hub`
**Branch:** `audit/account-wht-grpa-m18-closure-010`
**Evidence base:** CORR-007A commit `deceb7339b39eba309236782f159f8393224f5fd` (branch `audit/inventory-core-corr007a-grpa-m18-wht-50twi-009`) — cited by CORR-007A **by reference only**, not deep-inspected there. This document is the independent deep inspection.
**Date:** 2026-09-02
**Mode:** Evidence-first / clean-room / **no development authorization**. This is a read-only source-code audit. No application code was written or modified. No commands were executed against the source tree beyond `find`, `grep`, `wc -l`, and `shasum -a 256`.
**Reference tree examined (read-only, external to the git repo):**
`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/l10n_th_reports/` (primary target)
`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/addons_extra/l10n_th_withholding_tax/` (cross-reference)

This is an Odoo Thai-localization addon tree used as a **REFERENCE / benchmark source only**. It is **not** part of the SMEsPlus Node.js SaaS ERP target architecture. Nothing in this document should be read as a statement about SMEsPlus application code.

---

## 1. Module identity & structural finding

### 1.1 `02 OTHER/l10n_th_reports` — the module named in the CORR-007A citation

- `__manifest__.py` (full file read): name `"Thailand - Accounting Reports"`, version `1.0`, `depends: ["l10n_th", "account_reports"]`, `data: ["data/account_return_data.xml", "data/account_tax_report_data.xml"]`, `auto_install: True`.
  SHA-256: `e5018a7020328dc6ace63e2e3e2d13c1775a58d372bf042372851a0778a88c9`
  Path: `02 OTHER/l10n_th_reports/__manifest__.py`

This manifest declares only two data files and no test/i18n entries (tests and i18n load automatically by Odoo convention, not via `data`). Critically, `l10n_th_reports` **depends on `l10n_th`** — the base Thai localization module. Both `l10n_th` and `l10n_th_reports` are present as sibling directories under `02 OTHER/`.

### 1.2 CRITICAL STRUCTURAL FINDING: two files literally named `tax_report_pnd.py` exist in the tree, and they are NOT independent/duplicate — one silently overrides the other

`find` confirmed exactly two files named `tax_report_pnd.py` in the entire source tree:

1. `02 OTHER/l10n_th_reports/models/tax_report_pnd.py` — SHA-256 `346ab7b52ddba341accac959369439d7b249167db6e882a3ffaafd0eba62a3` (146 lines) — **defines** `l10n_th.pnd.report.handler` (base class, `_name` + `_inherit`), `l10n_th.pnd53.report.handler`, and `l10n_th.pnd3.report.handler`.
2. `addons_extra/l10n_th_withholding_tax/models/tax_report_pnd.py` — SHA-256 `41726222e1effd5774f40cde15c6cdf79e2ab5195eb44ef0cbe5fc5ce03401f` (104 lines) — **monkey-patches** `l10n_th.pnd.report.handler` using Odoo's `_inherit`-without-`_name` pattern (file 2, lines 4-5: `class L10n_ThPndReportHandler(models.AbstractModel): _inherit = 'l10n_th.pnd.report.handler'`).

This is Odoo's standard class-inheritance mechanism: when a second addon declares `_inherit = 'l10n_th.pnd.report.handler'` without its own `_name`, any method it redefines **replaces the base implementation at runtime for every subclass**, including `l10n_th.pnd53.report.handler` and `l10n_th.pnd3.report.handler`. Both classes inherit `_rows()` from `l10n_th.pnd.report.handler`, so if `addons_extra/l10n_th_withholding_tax` is installed alongside `l10n_th_reports`, **the `_rows()` method actually executed by the PND3/PND53 CSV export is the one in file 2, not the one in file 1.**

Confirmed dependency direction: `addons_extra/l10n_th_withholding_tax/__manifest__.py` (SHA-256 `903d9061ba5c16e68f0155309edb263088f1b5253b93ff8dc3b8bf3de12f199`), line 11: `"depends": ["account", 'l10n_th_reports']`. So `l10n_th_withholding_tax` (author: Ecosoft/OCA, version `19.0.1.4`, license AGPL-3) explicitly depends on and extends `l10n_th_reports`.

**Behavioral consequence:** the `_rows()` query in file 1 (lines 25-71) reads only `account_move_line.tax_line_id → account_tax`. The `_rows()` override in file 2 (lines 7-104) executes a **UNION of two SELECTs** — the original tax-line path, **plus a second SELECT that joins `account_withholding_tax awt ON awt.id = account_move_line.wt_tax_id`**, filtered additionally by `account_move_line.payment_id IS NULL AND account_move_line__move_id.payment_state != 'not_paid'` (file 2, lines 86-92). This second branch pulls partner "title" from `res_partner_company_type` via `jsonb_extract_path_text(rcp1.name, 'en_US')` (file 2, lines 22-26, 58-61) instead of the hardcoded Thai literal `'บริษัท'`/`''` used in file 1's caller.

**Finding:** whether PND3/PND53 CSV output reflects the simple tax-line query or the payment-state-filtered withholding-tax-table union is entirely dependent on which modules are installed and load order — this is not visible from `l10n_th_reports` alone. Anyone auditing only file 1 (as CORR-007A did, by citation without deep inspection) would miss this override entirely. **This is exactly the kind of gap CORR-007A's citation-only reference could not have caught.**

### 1.3 `tax_report_vat.py` — confirmed OUT OF SCOPE for PND3/PND53

`02 OTHER/l10n_th_reports/models/tax_report_vat.py` (SHA-256 `f030f0ef828bae2dc4de855d55bc60daf05ab2319451c8852039b5921b3ec6f`, 178 lines) defines `l10n_th.tax.report.handler`, a **separate model** producing **XLSX** (via `xlsxwriter`, lines 70-177) for `l10n_th_print_sale_tax_report` / `l10n_th_print_purchase_tax_report` (lines 36-56). It reads `1. Sales amount` / `5. Output tax` / `6. Purchase amount...` / `7. Input tax...` VAT tax-tags (lines 38-39, 49-50), not PND income-type tags. It shares no class hierarchy with `l10n_th.pnd.report.handler`. **Confirmed: this file is VAT-specific and structurally independent of the PND3/PND53 handlers.** It is cited here only to establish that boundary, per task scope.

### 1.4 The `account.report` records for PND3/PND53 are NOT defined inside `l10n_th_reports`

`02 OTHER/l10n_th_reports/data/account_tax_report_data.xml` (SHA-256 `b7937b8a6eeaf78ee9e48e1a0d75b4bae6c228109983f1bf32e2999aafca2cc`, 12 lines, full file):

```xml
<record id="l10n_th.tax_report_pnd53" model="account.report">
    <field name="custom_handler_model_id" ref="model_l10n_th_pnd53_report_handler"/>
</record>
<record id="l10n_th.tax_report" model="account.report">
    <field name="custom_handler_model_id" ref="model_l10n_th_tax_report_handler"/>
</record>
<record id="l10n_th.tax_report_pnd3" model="account.report">
    <field name="custom_handler_model_id" ref="model_l10n_th_pnd3_report_handler"/>
</record>
```

The record IDs are prefixed `l10n_th.` — meaning these are XML-inherited edits to `account.report` records that are **defined in the base `l10n_th` module**, not created here. `l10n_th_reports` only *attaches its custom Python handler* to pre-existing report definitions. Confirmed by direct grep: the actual `account.report` line/expression/tag-template definitions (`tax_report_pnd53`, `tax_report_total_income_pnd53`, `tax_report_total_remittance_pnd53`, `tax_report_surcharge_pnd53`, and the PND3 equivalents) live in `02 OTHER/l10n_th/data/account_tax_report_data.xml` lines 227-355 — a sibling module that was **out of the assigned deep-inspection scope** for this audit and was **not deep-audited here**. This is itself a scope boundary finding: the report-line structure, tag amounts, and column groupings that ultimately gate which move lines land in the PND3 vs. PND53 CSV are governed by a module this audit did not deep-inspect.

`02 OTHER/l10n_th_reports/data/account_return_data.xml` (SHA-256 `acb083cdf1fea365f94831f064ff5db846639194077128456a4fad2be7aa41`, 10 lines, full file) registers one `account.return.type` named "Tax" pointing at `l10n_th.tax_report` (the VAT report, not PND3/PND53) — this file does not register PND3/PND53 as return types at all.

### 1.5 The "50-twi" certificate module is confirmed structurally separate (independent re-confirmation of CORR-007A's boundary claim)

`addons_extra/l10n_th_withholding_tax_cert/__manifest__.py` (name "Thai Localization - Withholding Tax Certificate", `depends: ["l10n_th_withholding_tax"]`) was checked for a `tax_report_pnd.py` file: **none exists in that module's directory tree** (file listing performed; only `models/account_account.py`, `models/account_move.py`, `models/account_payment.py`, `models/withholding_tax_cert.py`). This independently reconfirms CORR-007A's claim that the PND3/PND53 filing/export module is code-separate from the 50-twi certificate print module — the two do not share a `tax_report_pnd.py` file, though `l10n_th_withholding_tax_cert` does transitively depend on `l10n_th_withholding_tax`, which in turn depends on and monkey-patches `l10n_th_reports` (see §1.2). They are separate concerns wired through a shared dependency chain, not through shared filing code.

---

## 2. PND3 proof

**Handler class:** `L10n_ThPnd3ReportHandler` — `02 OTHER/l10n_th_reports/models/tax_report_pnd.py`, lines 111-145 (`_name = 'l10n_th.pnd3.report.handler'`, `_inherit = ["l10n_th.pnd.report.handler"]`).

**Export method:** `l10n_th_print_pnd_tax_report_pnd3(self, options)`, lines 128-145. Wired to a UI button via `_custom_options_initializer` (lines 116-126: `'name': _('PND3')`, `'action': 'export_file'`, `'action_param': 'l10n_th_print_pnd_tax_report_pnd3'`, `'file_export_type': _('CSV')`).

Method body (lines 129-135):
```python
report = self.env.ref("l10n_th.tax_report_pnd3")
tag_templates = (
    self.env.ref("l10n_th.tax_report_total_income_pnd3")
    + self.env.ref("l10n_th.tax_report_total_remittance_pnd3")
    + self.env.ref("l10n_th.tax_report_surcharge_pnd3")
)
data = self._rows(options, report, [('tax_tag_ids', 'in', tag_templates._get_matching_tags().ids)])
```
No `title=` argument is passed here (contrast PND53, §3), so the `title` column defaults to `''` (base `_rows` default at line 25 of file 1: `title=''`). Confirmed against test expectation in `tests/test_tax_report.py` line 125: title field is empty for PND3 rows.

Independently verified against `tests/test_tax_report.py::test_pnd3_report` (lines 88-128) — this test builds an `in_invoice` (vendor bill) with two WHT taxes at rates `-1.00` and `-2.00`, posts it, and asserts the exported CSV rows show `Tax Type` = `Transportation` and `Advertising` respectively, matching the `CASE tax.amount` mapping (§5 below).

**Verdict: PND3 IS supported** by a concrete, callable, tested export method.

---

## 3. PND53 proof

**Handler class:** `L10n_ThPnd53ReportHandler` — `02 OTHER/l10n_th_reports/models/tax_report_pnd.py`, lines 74-108 (`_name = 'l10n_th.pnd53.report.handler'`, `_inherit = ["l10n_th.pnd.report.handler"]`).

*(This matches the line range CORR-007A cited by reference — 74-108 for PND53, 111-145 for PND3 — confirming the citation was accurate against the file as currently read, at least for the primary/non-overridden handler.)*

**Export method:** `l10n_th_print_pnd_tax_report_pnd53(self, options)`, lines 91-108. Wired to a UI button (lines 79-89: `'name': _('PND53')`, action_param `'l10n_th_print_pnd_tax_report_pnd53'`, `file_export_type: CSV`).

Method body (lines 92-98):
```python
report = self.env.ref('l10n_th.tax_report_pnd53')
tag_templates = (
    self.env.ref("l10n_th.tax_report_total_income_pnd53")
    + self.env.ref("l10n_th.tax_report_total_remittance_pnd53")
    + self.env.ref("l10n_th.tax_report_surcharge_pnd53")
)
data = self._rows(options, report, [('tax_tag_ids', 'in', tag_templates._get_matching_tags().ids)], title='บริษัท')
```
Here `title='บริษัท'` (Thai for "Company/juristic entity") is hardcoded and passed explicitly — unlike PND3. This is the one visible, in-file differentiator between the two handlers' output content (see §4).

Independently verified against `tests/test_tax_report.py::test_pnd53_report` (lines 46-86) — builds an `in_invoice` with WHT taxes at `-3.00` and `-2.00`, asserts `Title` column = `บริษัท` and `Tax Type` = `Service`/`Advertising`.

**Verdict: PND53 IS supported** by a concrete, callable, tested export method.

---

## 4. How PND3 and PND53 are distinguished in code

Three distinct, separately-verified mechanisms were found, at three different layers. **None of them lives entirely inside `l10n_th_reports`.**

**(a) Separate Python classes/methods, same shared query engine (`02 OTHER/l10n_th_reports/models/tax_report_pnd.py`).** `L10n_ThPnd3ReportHandler` (lines 111-145) and `L10n_ThPnd53ReportHandler` (lines 74-108) are separate `AbstractModel` subclasses, each with its own export method and its own `env.ref()` set of tag templates (`tax_report_total_income_pnd3` vs. `..._pnd53`, etc. — defined externally in `l10n_th`, §1.4). The only in-file content difference is the `title=''` vs. `title='บริษัท'` argument (§3). Both call the *same* inherited `_rows()` method — meaning **the actual row-selection logic is identical between PND3 and PND53**; only the `domain` (which tag_ids to match) and the `title` literal differ. Nothing in `_rows()` itself branches on "PND3-ness" vs. "PND53-ness" — the distinction is entirely a data/configuration-tag concern, resolved by whatever move lines happen to carry the `tax_report_total_income_pnd3` vs. `_pnd53` tags.

**(b) A payee-type gate at tax-*selection* time, one dependency layer away (`addons_extra/l10n_th_withholding_tax/models/account_move.py`, SHA-256 `eeee0f520afc86ccafe80d016b9dfb242647ae29f792044263aeef30a5391ac`).** `_compute_tax_domain` (lines 39-103) computes which `account.withholding.tax` records (field `wt_tax_ids`, line 36) are *offerable* on an invoice line, based on `move_type` **and partner company-vs-individual status**:
  - Lines 53-74 (purchase-type moves `in_receipt`/`in_invoice`/`in_refund`): if `rec.partner_id.is_company` is true → WHT tax choices filtered to those whose `tax_tag_ids[0].name` contains the substring `'pnd53'` (case-insensitive, line 73); if the partner is *not* a company (an individual) → filtered to tags containing `'pnd3'` (line 82). This is the actual "individual vs. juristic payee → PND3 vs. PND53" business rule for the withholding-agent (purchase) side.
  - Lines 85-95 (sale-type moves `out_receipt`/`out_invoice`/`out_refund`): WHT choices are filtered only by `type in ('sale','none',False)` on `account.withholding.tax` — **no PND3/PND53 tag-name split is applied on the sale side** (see §6).

This logic is **fragile**: it is a case-insensitive **substring match on a free-text tag name** (`'pnd3' in l.tax_tag_ids[0].name.lower()`), indexed at `[0]` of a recordset with no ordering guarantee stated in the code shown, and it governs only which tax is *offered* on the UI/compute domain for the field `wt_tax_id` on `account.move.line` (line 9-15 of the same file), which is declared `store=True, readonly=False` — i.e., an editable, stored default, not an ORM-enforced constraint. Nothing in `tax_report_pnd.py` re-validates this at export time.

**(c) The report/tag registry itself (`02 OTHER/l10n_th/data/account_tax_report_data.xml`, lines 227-355 — NOT deep-audited here, see §1.4).** This is where `tax_report_pnd3`/`tax_report_pnd53` `account.report` records and their `tax_report_total_income_pnd3`/`_pnd53` etc. line/expression (tag) definitions actually live. This governs, at the database-tag level, which move lines are structurally eligible to appear in each report's CSV via the `tax_tag_ids in [...]` domain in §2/§3. **Not examined in depth in this audit — flagged as an unresolved dependency for statutory-correctness review (§7).**

**Conclusion:** PND3 vs. PND53 distinction is **not a single, auditable business rule inside the filing module**. It is the *composite effect* of (a) which export method a user clicks, (b) a substring-matched tag-name gate three layers away, in a different module, that only advises what tax is *selectable* (not enforced), and (c) an externally-defined tag registry not in the assigned inspection scope. **This is a materially significant finding for statutory-correctness review.**

---

## 5. CSV/export field mapping table

**Encoding/format:** Both PND3 and PND53 export **CSV**, built manually by string concatenation — no `csv` stdlib module is used. Row-writer: `_csv_row(*data, delimiter=",")` (`02 OTHER/l10n_th_reports/models/tax_report_pnd.py`, lines 7-9):
```python
def _csv_row(*data, delimiter=","):
    return delimiter.join(data) + '\n'
```
No quoting/escaping of embedded commas or newlines in field values (e.g., a partner street address containing a comma would corrupt the CSV) — **NOT FOUND**: no `csv.writer`, no quote-escaping logic anywhere in this file. Output is produced via `output.encode()` (lines 100-102, 106; default Python UTF-8) and returned with `"file_type": "csv"` (lines 104-108, 141-145). No explicit charset/BOM handling is present — **NOT FOUND**: no `encode('utf-8-sig')`, no BOM prefix, no `cp874`/Windows-Thai codepage handling anywhere in the file, despite the presence of Thai-language content (`'บริษัท'`, Thai header text via `_()` translation).

**Column layout** (hardcoded, `_headers()`, lines 20-23 — identical for PND3 and PND53):

| # | Header (English label via `_()`) | SQL source column | Notes |
|---|---|---|---|
| 1 | No. | `ROW_NUMBER() OVER(ORDER BY move date, partner name, move name, line id)` cast to text | Sequential, computed at query time |
| 2 | Tax ID | `COALESCE(partner.vat, '')` | |
| 3 | Title | literal `%(title)s` param — `''` for PND3, `'บริษัท'` for PND53 | Hardcoded string, not derived from partner data in the primary handler (the OCA override, §1.2, instead derives it from `res_partner_company_type`) |
| 4 | Contact Name | `COALESCE(partner.name, '')` | |
| 5 | Street | `COALESCE(partner.street, '')` | |
| 6 | Street2 | `COALESCE(partner.street2, '')` | |
| 7 | City | `COALESCE(partner.city, '')` | |
| 8 | State | `COALESCE(state.name, '')` via `res_country_state` | |
| 9 | Zip | `COALESCE(partner.zip, '')` | |
| 10 | Branch Number | `COALESCE(partner.company_registry, '')` | Primary handler uses `company_registry`; the OCA override (`tax_report_vat.py`-style union, file 2) instead uses `COALESCE(partner.branch, '')` — a **different source field for the same header**, another consequence of the override in §1.2 |
| 11 | Invoice/Bill Date | `TO_CHAR(move.date, 'dd/mm/YYYY')` | Buddhist-era conversion **NOT FOUND** — this formats the Gregorian year, not Thai Buddhist Era (BE = CE+543), with no BE conversion logic anywhere in the file |
| 12 | Tax Rate | `ROUND(ABS(tax.amount), decimal_places)` | Labeled "Tax Rate" in the header but this is the raw negative WHT tax percentage (e.g. `-3.00`), absolute-valued |
| 13 | Total Amount | `ROUND(ABS(account_move_line.tax_base_amount), decimal_places)` | i.e., the WHT base amount, not the invoice total |
| 14 | WHT Amount | `ROUND(ABS(tax.amount * tax_base_amount / 100), decimal_places)` | Computed at query time from rate × base |
| 15 | WHT Condition | hardcoded literal `'1'` | **Always the literal string `1` for every row** — no branching logic found anywhere in the file that ever produces a different value. `NOT FOUND`: no lookup, no field, no config source for this column — it is a hardcoded constant. |
| 16 | Tax Type | `CASE tax.amount WHEN -1 THEN 'Transportation' WHEN -2 THEN 'Advertising' WHEN -3 THEN 'Service' WHEN -5 THEN 'Rental' ELSE '' END` (lines 48-54) | See §6 |

Column layout is **identical between PND3 and PND53** (same `_headers()` method, inherited, not overridden by either subclass). File naming: `"Tax Report PND53"` / `"Tax Report PND3"` (lines 105, 142) — plain descriptive names, not the official form-number filenames a Revenue Department e-filing tool would expect (no evidence either way on what filename convention, if any, is required — see §7).

---

## 6. Tax-type / WHT income-type mapping logic

The **only** WHT income-type classification found anywhere in `tax_report_pnd.py` is the SQL `CASE` expression at lines 48-54 (identical, duplicated verbatim, in the OCA override at `addons_extra/l10n_th_withholding_tax/models/tax_report_pnd.py` lines 39-45 and again at lines 74-80):

```sql
CASE tax.amount
    WHEN -1 THEN 'Transportation'
    WHEN -2 THEN 'Advertising'
    WHEN -3 THEN 'Service'
    WHEN -5 THEN 'Rental'
    ELSE ''
END tax_type
```

**Findings:**
- The mapping keys off the **raw numeric WHT tax rate/percentage** (`tax.amount`, e.g. `-1`, `-2`, `-3`, `-5`), not an income-type code (Thai WHT practice recognizes categories such as ค่าจ้างทำของ/service fees, ค่าเช่า/rental, ค่าโฆษณา/advertising, ดอกเบี้ย/interest, เงินปันผล/dividends, ค่าวิชาชีพ/professional fees, รางวัล/prizes, etc., several of which can share the same statutory rate, e.g. many professional-fee and service categories are both taxed at 3%).
- Only **four** rate values are mapped; every other rate (e.g. `-10` for dividends, or any custom/negotiated rate) silently maps to the empty string via `ELSE ''`. **NOT FOUND**: no dictionary, no `selection` field, no configuration table anywhere in the module that maps a WHT income-type *code* (as opposed to a bare percentage) to a label.
- Because the mapping is rate-based and not code-based, **two genuinely different statutory income categories that happen to share a rate would be reported under the same (possibly wrong) label**, and any category not in this list of four is reported with a **blank Tax Type cell** in the exported CSV with no warning.
- This mapping is duplicated three times in the tree (once in the primary handler, twice in the OCA override's two UNION branches) with no shared constant/dict — a maintenance/consistency risk independent of statutory correctness.

**Verdict:** tax-type mapping exists but is narrow, rate-keyed (not code-keyed), covers only 4 categories, and silently blanks anything else. This is a concrete, source-verifiable gap, separate from any statutory-format question.

---

## 7. Filing period / report-period logic

**In `tax_report_pnd.py` itself:** no explicit `date_from`/`date_to` computation exists. The only period-related call is `report._get_report_query(options, 'strict_range', domain)` (line 26, and reused inside the OCA override, file 2 line 8). This method belongs to Odoo's core `account_reports` addon — an out-of-tree dependency declared in `__manifest__.py` line 15 (`"account_reports"`) — **not present in this source tree**, so its internal date-window logic could not be inspected as part of this audit. `NOT FOUND` (in-tree): no code in `l10n_th_reports` that itself parses, validates, or computes a Thai filing month/year from the report options.

**For contrast**, `tax_report_vat.py` (out of scope for PND3/53 but instructive) *does* contain explicit period-handling code at lines 60-61 and 99-101:
```python
date_from = options['date'].get('date_from')
date_to = options['date'].get('date_to')
...
date_from = fields.Date.to_date(date_from).strftime('%d/%m/%Y')
date_to = fields.Date.to_date(date_to).strftime("%d/%m/%Y")
```
No equivalent exists in `tax_report_pnd.py` — the PND3/PND53 handlers rely entirely on the generic `account.report` options/period machinery inherited from `account_reports`, with `'strict_range'` mode passed at the query-builder call. There is no PND3/PND53-specific "filing month" concept (e.g., no explicit "this must be the 7th/15th of the following month" due-date logic, no month-locking, no re-filing/amendment marker) anywhere in this module.

**Test evidence:** `tests/test_tax_report.py` uses `@freeze_time('2023-06-30')` with `self._generate_options(report, '2023-05-01', '2023-05-31')` (lines 46, 79, 88, 121) — a full calendar-month range — confirming the generic date-range mechanism is exercised, but this is test scaffolding calling the *generic* `account.report` options API, not module-specific period logic.

---

## 8. What remains for Legal/Tax sign-off (LEGAL_TAX_REVIEW_REQUIRED)

**No official government filing-layout specification, revision number, or column-order standard is referenced anywhere in the examined source** — not in code comments, not in docstrings, not in the test file, not in `i18n/th.po` (full file read, 257 lines), not in `i18n/l10n_th_reports.pot`. A targeted grep for `revenue department`, `กรมสรรพากร`, `ภ.ง.ด`, `form spec`, `layout spec`, `revision`, `column order`, `government form`, `official format` across the entire module returned **zero substantive matches** — the only hits were unrelated PO-file tooling metadata (`PO-Revision-Date:`) and the Thai UI labels `ภ.ง.ด. 3` / `ภ.ง.ด. 53` (button/model display names only, not spec citations). This confirms the module's authors did not encode a traceable link to any authoritative Revenue Department form-layout document, RD Prep software column spec, or e-filing schema version.

**This audit team explicitly states:** we have **not** seen an official Thai Revenue Department e-filing format specification, and **do not** declare that this module's CSV output satisfies actual PND3/PND53 e-filing format requirements. The following items are flagged **LEGAL_TAX_REVIEW_REQUIRED**, each requiring comparison against an official specification this audit does not have access to:

1. **Column order and column set** — the 16-column layout in §5 (No., Tax ID, Title, Contact Name, Street, Street2, City, State, Zip, Branch Number, Invoice/Bill Date, Tax Rate, Total Amount, WHT Amount, WHT Condition, Tax Type) has no cited source confirming it matches the RD's expected PND3/PND53 e-filing column order, delimiter convention, or required field set.
2. **"WHT Condition" hardcoded to literal `'1'`** — no explanation, no lookup, no evidence this is the correct condition code for every row in every circumstance (e.g., paid-in-full vs. lump-sum vs. one-time conditions that Thai WHT forms typically distinguish).
3. **Tax-type mapping is rate-keyed, covers only 4 of the many statutory WHT income-type categories, and silently blanks the rest** (§6) — needs comparison against the RD's actual income-type code list (often referenced as ประเภทเงินได้ 1-40 series or similar) to determine what fraction of real-world transactions would file with a blank/wrong category.
4. **No Buddhist-era (BE) date conversion found** — dates are formatted `dd/mm/YYYY` in the Gregorian calendar (§5, column 11); Thai official forms conventionally expect BE years (CE+543). Needs verification against the actual e-filing/print format expected.
5. **No CSV quoting/escaping** — embedded delimiters or newlines in address fields are not escaped (§5); needs verification this cannot corrupt a real submission file.
6. **No character-encoding/BOM handling found** for a CSV that must carry Thai text — plain UTF-8 `.encode()` with no BOM; whether the RD's intake tooling requires a specific codepage or BOM is unverified.
7. **PND3-vs-PND53 payee classification (§4) is a fragile, non-authoritative substring match** on a tag *name* string in a different, dependency-layer module (`l10n_th_withholding_tax`), not enforced at export time by `tax_report_pnd.py` itself, and not applied at all on the sale side (§4b, §9 below). Whether this reliably produces statutorily-correct PND3/PND53 routing for edge cases (e.g., a partner whose `is_company` flag is misconfigured, or a WHT tax record whose `wt_tax_id` was set through a path other than the compute-default) is unverified from source alone.
8. **The actual report-line/tag-template definitions that gate which move lines qualify for each report** live in `02 OTHER/l10n_th/data/account_tax_report_data.xml` lines 227-355 — a module explicitly **out of this audit's assigned deep-inspection scope** (§1.4). Full statutory review cannot be complete without deep-inspecting that file's tag/amount logic as well.
9. **Which `_rows()` implementation actually runs is deployment-dependent** (§1.2) — the primary handler's simple tax-line query vs. the OCA override's payment-state-filtered UNION with `account_withholding_tax`. Statutory sign-off must specify which module combination is the intended production configuration, since the two produce materially different result sets (different `Branch Number` source field, different `Title` derivation, additional payment-state filtering present only in the override).

**None of the above can be resolved by further source-code reading. They require an official RD specification document and a tax/legal reviewer's sign-off — this audit stops at "what the code does," not "whether what the code does is statutorily correct."**

---

## 9. Stock/inventory dependency check

Explicit grep performed per governing rule #4, across both examined module trees:

```
grep -rn "stock\.move\|stock\.quant\|stock\.picking" \
  "02 OTHER/l10n_th_reports/"                    → 0 matches (exit code 1, no matches)
grep -rn "stock\.move\|stock\.quant\|stock\.picking" \
  "addons_extra/l10n_th_withholding_tax/"        → 0 matches (exit code 1, no matches)
```

**Verdict: NOT FOUND.** No reference to `stock.move`, `stock.quant`, or `stock.picking` exists anywhere in either the primary PND3/PND53 filing module or its cross-referenced withholding-tax dependency module. The PND3/PND53 filing/export code path has **no inventory-module coupling** — it operates exclusively on `account.move`, `account.move.line`, `account.tax`, `res.partner`, `res.country.state`, and (in the OCA override) `account.withholding.tax` / `res.partner.company.type`.

---

## 10. What this proves / does not prove

**Proves (source-verified, evidence cited above):**
- PND3 and PND53 are each supported by a distinct, callable, tested export method producing CSV (§2, §3).
- The two are code-distinguished by separate handler classes/methods sharing one query engine, gated by externally-defined report/tag configuration and a fragile tag-name substring match at the tax-selection layer (§4).
- A concrete, enumerable CSV column layout exists and is identical across both forms (§5).
- A tax-type mapping exists but is narrow and rate-keyed, not a full statutory income-type code table (§6).
- The module has no inventory-system (`stock.*`) coupling whatsoever (§9).
- The PND3/PND53 filing module is code-separate from the 50-twi certificate print module (independently reconfirmed, §1.5).
- A structurally significant, previously-uncited monkey-patch override of the filing module's core query method exists in a dependency addon (§1.2) — this changes what data actually reaches the CSV depending on installed-module configuration, and was invisible to a citation-only reference (as CORR-007A's was).

**Does NOT prove:**
- That the CSV output is accepted by, or conforms to, any actual Thai Revenue Department e-filing format, column order, encoding, or revision (§7/§8) — no official specification was available to this audit.
- That the PND3/PND53 income-type/condition columns are statutorily complete or correct (§6, §8.2-8.3).
- That the sale-side vs. purchase-side (withholding-agent-paid vs. withholding-received-as-payee) separation is enforced anywhere inside the filing module itself — it is not (§4b, §6) — this audit found the separation logic exists one dependency layer away, in `account_move.py`, as an advisory tax-selection domain only, not a report-time validation.
- That the module's behavior is deterministic/config-independent — it is not, per the two-implementations-of-`_rows()` finding (§1.2).

---

## 11. Disposition input for the final Boss recommendation team

**Recommended disposition: split, per the two findings this audit distinguishes.**

- **Code path / export mechanism ("does a PND3 and PND53 CSV export exist, is it wired, is it tested"): RESOLVED-AS-STRUCTURE.** Both forms have real, tested, callable export methods producing CSV with a defined column layout. This part of the question is answered from source with high confidence.

- **Statutory-layout / filing correctness ("is this CSV what the Revenue Department actually requires"): CONTROLLED CARRY-FORWARD, pending Legal/Tax review against an official specification this audit team does not possess.** This audit cannot and does not recommend RESOLVED for statutory correctness, per governing rule #3. The nine specific items in §8 must be checked against an authoritative RD specification before any statutory sign-off.

- **Do NOT recommend REMAINS HIGH** — the code-path existence question is not open or ambiguous; a real, tested mechanism was found (unlike, e.g., a stub or TODO). REMAINS HIGH would overstate the uncertainty of what is source-verifiable.

- **Additional flag for the Boss team's attention, beyond the standard PASS/CARRY-FORWARD axis:** the monkey-patch override (§1.2) and the fragile PND3/PND53 tag-name substring classification (§4b) are **engineering-risk findings independent of the legal/tax question** — they affect whether the *same* input data produces the *same* output CSV across environments, and whether payee classification is robust. These should be tracked as a distinct action item regardless of how the statutory-layout question resolves.

This audit team makes **no Gate PASS declaration** and **does not authorize Team B or Team C** to proceed on the strength of this document alone, per governing rules #5 and #3.

---

## Appendix: full SHA-256 citation list

| File | SHA-256 |
|---|---|
| `02 OTHER/l10n_th_reports/__manifest__.py` | `e5018a7020328dc6ace63e2e3e2d13c1775a58d372bf042372851a0778a88c9` |
| `02 OTHER/l10n_th_reports/models/tax_report_pnd.py` | `346ab7b52ddba341accac959369439d7b249167db6e882a3ffaafd0eba62a3` |
| `02 OTHER/l10n_th_reports/models/tax_report_vat.py` | `f030f0ef828bae2dc4de855d55bc60daf05ab2319451c8852039b5921b3ec6f` |
| `02 OTHER/l10n_th_reports/data/account_return_data.xml` | `acb083cdf1fea365f94831f064ff5db846639194077128456a4fad2be7aa41` |
| `02 OTHER/l10n_th_reports/data/account_tax_report_data.xml` | `b7937b8a6eeaf78ee9e48e1a0d75b4bae6c228109983f1bf32e2999aafca2cc` |
| `02 OTHER/l10n_th_reports/tests/test_tax_report.py` | `2e4971e3a31238550443c3bd529eaef4ad90725436e0ef6211838cb31eed3e2` |
| `02 OTHER/l10n_th_reports/i18n/th.po` | `9e9a769a91b850af45bf1dafeee7b33b36630307692c66c66d63f3e5b5245bd` |
| `02 OTHER/l10n_th_reports/i18n/l10n_th_reports.pot` | `f4c910ace643ed98563122f2761cc727ac76f703b753fb2a2953526b034435e` |
| `addons_extra/l10n_th_withholding_tax/__manifest__.py` | `903d9061ba5c16e68f0155309edb263088f1b5253b93ff8dc3b8bf3de12f199` |
| `addons_extra/l10n_th_withholding_tax/models/tax_report_pnd.py` | `41726222e1effd5774f40cde15c6cdf79e2ab5195eb44ef0cbe5fc5ce03401f` |
| `addons_extra/l10n_th_withholding_tax/models/account_move.py` | `eeee0f520afc86ccafe80d016b9dfb242647ae29f792044263aeef30a5391ac` |
| `addons_extra/l10n_th_withholding_tax/models/account_withholding_tax.py` | `ea813264c2bb7b9d41b4fdc4544f4d709f56ebe5c2422ac317bfe5e098eca44` |
| `addons_extra/l10n_th_withholding_tax/models/account_tax.py` | `7af94ba85aa8a88cc4f9fcda91f4ac6eccd8545482e5812f31dc1d7486b51f3` |
| `addons_extra/l10n_th_withholding_tax/models/product.py` | `85bad9505a97a45bcec3144d6662cd4124f98bd5d72f19c9aa1e737a7daf333` |

All hashes computed via `shasum -a 256 <path>` against the file states read during this audit session (2026-09-02). Note: `02 OTHER/l10n_th/data/account_tax_report_data.xml` (referenced in §1.4/§8.8 as the location of the actual report/tag definitions) was **not hashed** as it was explicitly out of this audit's assigned deep-inspection scope — flagged for a future, separately-scoped deep inspection.
