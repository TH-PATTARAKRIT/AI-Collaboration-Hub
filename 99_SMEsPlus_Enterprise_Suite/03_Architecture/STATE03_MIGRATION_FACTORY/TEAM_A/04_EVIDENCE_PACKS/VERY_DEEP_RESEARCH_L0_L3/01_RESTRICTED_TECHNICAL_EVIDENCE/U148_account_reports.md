# U148 — account_reports: Financial Reporting Engine Deep L3
**Unit:** U148 | **Group:** G01 | **Priority:** P1
**Researcher:** DeepSeek STATE03 Worker
**Date:** 2026-10-02

---

## PRESENCE CHECK

**account_reports module: ABSENT** from Community edition at
`odoo/addons/account_reports`

The financial reporting engine is built into the core `account` module at
`odoo/addons/account/models/account_report.py` (Odoo 19.0.post20260921).

P&L and Balance Sheet are Enterprise-only data records; Community ships only the
Generic Tax Report as a data record.

---

## MODEL INVENTORY

| Model | Location | Purpose |
|---|---|---|
| `account.report` | `account/models/account_report.py:44` | Root report definition |
| `account.report.line` | `account/models/account_report.py:349` | Individual report lines |
| `account.report.expression` | `account/models/account_report.py:579` | Expression/formula per line |
| `account.report.column` | `account/models/account_report.py:932` | Column definitions |
| `account.report.external.value` | `account/models/account_report.py:947` | Stored manual / carryover values |

---

## DETAILED EVIDENCE

### 1. AccountReport core fields (account/models/account_report.py:44–116)

- `name` (Char, required, translatable) — L51
- `line_ids` (One2many → account.report.line) — L54
- `column_ids` (One2many → account.report.column) — L55
- `root_report_id` (Many2one → account.report) — L56: links a variant to its root
- `variant_report_ids` (One2many → account.report) — L57
- `section_report_ids` / `section_main_report_ids` (Many2many) — L58–59: composite reports
- `use_sections` (Boolean, computed from section_report_ids) — L60
- `chart_template` (Selection) — L65
- `country_id` (Many2one → res.country) — L66
- `only_tax_exigible` (Boolean) — L67
- `availability_condition` (Selection: country/coa/always) — L73
- `prefix_groups_threshold` (Integer, default 4000) — L80: threshold for auto prefix grouping
- `integer_rounding` (Selection: HALF-UP/UP/DOWN) — L81
- `default_opening_date_filter` (Selection: this_year/this_quarter/this_month/today/previous_month/previous_quarter/previous_year/this_return_period/previous_return_period) — L88
- `currency_translation` (Selection: current/cta) — L106

### 2. Filter fields (account/models/account_report.py:120–199)

All filter fields use `_compute_report_option_filter` which propagates from root_report_id or section parent:

- `filter_multi_company` (selector / tax_units) — L120
- `filter_date_range` (Boolean, default True) — L126
- `filter_show_draft` (Boolean, default True) — L131
- `filter_unreconciled` (Boolean, default False) — L136
- `filter_unfold_all` (Boolean) — L141
- `filter_hide_0_lines` (Selection: by_default/optional/never, default optional) — L146
- `filter_period_comparison` (Boolean, default True) — L152
- `filter_growth_comparison` (Boolean, default True) — L157
- `filter_journals` (Boolean) — L162
- `filter_analytic` (Boolean) — L167
- `filter_hierarchy` (Selection: by_default/optional/never, default optional) — L172
- `filter_account_type` (Selection: both/payable/receivable/disabled, default disabled) — L178
- `filter_partner` (Boolean) — L184
- `filter_aml_ir_filters` (Boolean) — L189
- `filter_budgets` (Boolean) — L195

### 3. AccountReportLine fields (account/models/account_report.py:349–396)

- `name` (Char, required, translatable) — L354
- `expression_ids` (One2many → account.report.expression) — L355
- `report_id` (Many2one, computed recursively from parent_id.report_id) — L356
- `hierarchy_level` (Integer, computed; root=1, child+=2 or +=3 if parent level=0) — L368: L403–410
- `parent_id` (Many2one → account.report.line) — L377
- `children_ids` (One2many) — L378
- `groupby` (Char) — L379: comma-sep aml fields, generates sublines when set
- `user_groupby` (Char, computed) — L380: validated against engine constraints
- `code` (Char, unique per report) — L386
- `foldable` (Boolean) — L387: if True, not unfolded by default
- `hide_if_zero` (Boolean) — L390
- `domain_formula`, `account_codes_formula`, `aggregation_formula`, `external_formula`, `tax_tags_formula` — L391–396: shortcut fields for XML brevity; write-only, create expressions via `_create_report_expression`

### 4. AccountReportExpression fields (account/models/account_report.py:579–633)

- `report_line_id` (Many2one → account.report.line, required, cascade) — L584
- `label` (Char, required; unique per line) — L586
- `engine` (Selection, required) — L587:
  - `domain` — Odoo domain against account.move.line
  - `tax_tags` — Tax tag formula; auto-creates account.account.tag records
  - `aggregation` — Aggregates other expression formulas by line code
  - `account_codes` — Account code prefix matching
  - `external` — Manually entered value
  - `custom` — Custom Python function
- `formula` (Char, required) — L599
- `subformula` (Char) — L600: for domain engine holds sum/neg_sum; for aggregation holds cross_report or conditional
- `date_scope` (Selection, default strict_range) — L601:
  - from_beginning, from_fiscalyear, to_beginning_of_fiscalyear
  - to_beginning_of_period, strict_range, previous_return_period
- `figure_type` (Selection: monetary/percentage/integer/float/date/datetime/boolean/string) — L614
- `green_on_positive` (Boolean, default True) — L615
- `blank_if_zero` (Boolean) — L616
- `auditable` (Boolean, computed from engine; all 5 non-custom engines are auditable) — L617: L688–689
- `carryover_target` (Char) — L620: formula `line_code.expression_label`; only valid on `_carryover_*`-labelled expressions; target must start with `_applied_carryover_`

### 5. Carryover Mechanism (account/models/account_report.py:635–929)

- `_check_carryover_target` constraint — L635–641:
  - expression label must start with `_carryover_`
  - target expression label must start with `_applied_carryover_`
- `_get_carryover_target_expression` — L911–929:
  - If `carryover_target` set: parses `line_code.expression_label` and searches
  - Else auto-resolves: strips `_carryover_` prefix and looks for `_applied_carryover_<main_label>`
- `AccountReportExternalValue.carryover_origin_expression_label` — L966: stores origin label for carried values
- `AccountReportExternalValue.carryover_origin_report_line_id` — L967: stores origin line

### 6. Aggregation Engine (account/models/account_report.py:800–883)

- `_expand_aggregations` — L800: recursively expands aggregation dependencies
- `sum_children` formula — L811: special keyword aggregating all children expressions
- Cross-report syntax — L815: `subformula = cross_report(<report_id>|<xml_id>)` allows aggregating lines from a different report
- AGGREGATION_ENGINE_FORMULA_REGEX — L37–41: validates aggregation formulas at model level
- `_get_aggregation_terms_details` — L860: parses `A.balance + B.balance` → `{'A': {'balance'}, 'B': {'balance'}}`

### 7. Tax Tags Engine + Tag Lifecycle (account/models/account_report.py:695–792)

- On expression create with engine=tax_tags: auto-creates `account.account.tag` with applicability='taxes' — L701–716
- On expression write with changed formula: renames tag if exclusively used by this expression, else creates new tag — L718–763
- On expression delete: archives tag if still referenced on journal item lines, else unlinks — L765–792

### 8. Account Codes Engine Regex (account/models/account_report.py:25–31)

```
ACCOUNT_CODES_ENGINE_SPLIT_REGEX: r"(?=[+-])"
ACCOUNT_CODES_ENGINE_TERM_REGEX: captures sign, prefix, excluded_prefixes, balance_character [DC]
```
- Prefix term syntax: `<sign><prefix>(\(<excluded>,…\))?[DC]?`
- D = Debit, C = Credit balance character
- tag() syntax supported in prefix: `tag(<tag_name>)`

### 9. Domain Engine Subformula (account/models/account_report.py:22, 493–517)

- DOMAIN_REGEX: `r'(-?sum)\((.*)\)'` — L22
- Subformula must be present (DB constraint at L626)
- `sum` or `-sum` accumulates matched aml amounts
- `domain_formula` shortcut field uses `ref()` resolution for XML referencing

### 10. AccountReportColumn (account/models/account_report.py:932–944)

- `expression_label` (Char, required) — L938: links column to expression by label
- `sortable` (Boolean) — L941
- `figure_type` (Selection, default monetary) — L942
- `blank_if_zero` (Boolean) — L943
- `custom_audit_action_id` (Many2one → ir.actions.act_window) — L944: override audit drill-down

### 11. Generic Tax Report (account/data/account_reports_data.xml:6–60)

Only report defined as data in Community:
- `generic_tax_report` — root report; filter_multi_company=tax_units; allow_foreign_vat=True; default_opening=previous_return_period; only_tax_exigible=True
- Two variants: group by Account>Tax and Tax>Account; both linked via `root_report_id`

### 12. use_in_tax_closing on Repartition Lines (account/models/account_tax.py:5341–5361)

- Field on `account.tax.repartition.line`, NOT on `account.report.expression`
- Auto-computed: repartition_type='tax' AND account_id set AND internal_group not in (income, expense)
- Controls whether the repartition line amount is included in tax closing entries

### 13. Report Variant Pattern (account/models/account_report.py:56–57, 233–237)

- `root_report_id` links a variant to a root
- Root report must have no root of its own (constraint _validate_root_report_id)
- Filter values on a variant are inherited from root via `_compute_report_option_filter`
- availability_condition='country' requires country_id to be set (constraint)

### 14. Copy Mechanism (account/models/account_report.py:290–321)

- `copy()` duplicates hierarchy by calling `_copy_hierarchy` recursively on root lines
- `code_mapping` dict tracks old_code→new_code during copy
- Aggregation formulas in copied expressions are updated with new codes via regex substitution

---

## COMMUNITY vs ENTERPRISE NOTE

- `account_reports` addon: **Enterprise-only** (OEEL-1 licensed)
- P&L, Balance Sheet, Audit Trail, General Ledger, Partner Ledger, Aged Receivable/Payable: all defined as Enterprise data
- Community provides the report framework (models, ORM, engine logic) but ships only Generic Tax Report as data

---

## RAW POINTERS

| File | Lines |
|---|---|
| `account/models/account_report.py` | 1–968 |
| `account/models/account_tax.py` | 5341–5361 |
| `account/data/account_reports_data.xml` | 1–63 |
| `account/__manifest__.py` | 1–60 |
