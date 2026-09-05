# P07 — TAX REPORT TRACEABILITY

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Report Population

`POPULATION` = every artefact in the declared source set that produces a Thai tax output.
`UNIT` = one report definition or one export entry point. Enumerated by reading all 15
modules of `13 §5`.

| # | Output | Kind | Defined in | Handler | Statutory counterpart |
|---|---|---|---|---|---|
| `RPT-01` | Tax Report (lines 1–12) | `account.report` | `l10n_th/data/account_tax_report_data.xml:3` | generic | ภ.พ.30 structure (`S-15`) |
| `RPT-02` | PND53 | `account.report` | `l10n_th/data/account_tax_report_data.xml:227` | `l10n_th.pnd53.report.handler` | ภ.ง.ด.53 (`S-33`) |
| `RPT-03` | PND3 | `account.report` | `l10n_th/data/account_tax_report_data.xml:291` | `l10n_th.pnd3.report.handler` | ภ.ง.ด.3 (`S-33`) |
| `RPT-04` | Sales Tax Report (xlsx) | export button on `RPT-01` | `l10n_th_reports/models/tax_report_vat.py:17-23` | `l10n_th.tax.report.handler`, **overridden** by `l10n_th_reports_ext` | Output tax report (`S-25`) |
| `RPT-05` | Purchase Tax Report (xlsx) | export button on `RPT-01` | `l10n_th_reports/models/tax_report_vat.py:24-30` | same | Input tax report (`S-25`) |
| `RPT-06` | Sale Vat Report | `account.report` | `smesplus_account_reports/data/generic_tax_report.xml:3` | `account.sale.vat.report.handler` | Output tax report (`S-25`) |
| `RPT-07` | Sale Vat Report Zero | `account.report` | `:73` | `account.sale.vat.report.zero` | Output tax report, zero-rated portion |
| `RPT-08` | Purchase Vat Report | `account.report` | `:136` | `account.purchase.vat.report.handler` | Input tax report (`S-25`) |
| `RPT-09` | Purchase Vat Report Zero | `account.report` | `:~210` | `account.purchase.vat.report.zero` | Input tax report, zero-rated portion |
| `RPT-10` | PND53 CSV export | export button | `l10n_th_reports/models/tax_report_pnd.py:79-89` | overridden by `l10n_th_withholding_tax/models/tax_report_pnd.py` | ภ.ง.ด.53 schedule |
| `RPT-11` | PND3 CSV export | export button | `:116-126` | same override | ภ.ง.ด.3 schedule |
| `RPT-12` | Withholding Tax Report (xlsx / pdf / html) | wizard + transient model | `l10n_th_withholding_tax_report` | own | WHT register over certificates |
| `RPT-13` | Withholding tax certificate print | QWeb report | `l10n_th_withholding_tax_cert_form` | own | s.50 bis certificate (`S-31`) |
| `RPT-14` | Tax Invoice print | QWeb template | `l10n_th/views/report_invoice.xml:3` | — | Tax invoice (`S-19`) |
| `RPT-15` | Commercial Invoice print | QWeb report | `l10n_th/views/report_invoice.xml:19-36` | — | none (commercial document) |

`POPULATION = 15`.

## 2. Selection Traceability — What Each Report Actually Selects

| Report | Date attribute used | Row predicate | Partner handling | Amount source |
|---|---|---|---|---|
| `RPT-04`/`RPT-05` (vendor) | `strict_range` on the line date | membership of the base/tax tags for report lines 1, 5, 6, 7 | **retained** when absent, captioned `Selling goods or providing services` | signed sum of line balances, sign taken from `balance_negate` on each tag |
| `RPT-04`/`RPT-05` (SMEsPlus override) | same | same | same caption retained | same amounts, computed in one SQL aggregation instead of nested Python loops; the comment at `l10n_th_reports_ext/models/tax_report_vat.py:41-44` states the multi-tag duplication semantics are preserved, and the SQL does preserve them |
| `RPT-06`/`RPT-08` | `strict_range` on the line date | `tax_exigible` **and** `type_tax_use == report type` **and** `tax_group.name == {'en_US': 'VAT 7%'}` | **inner join** on `res_partner` — partnerless rows dropped | `sum(tdr.base_amount)`, `sum(tdr.tax_amount)` from the tax-detail query |
| `RPT-07`/`RPT-09` | `strict_range` on the line date | cash-basis guard, sale/purchase tax use, **and `move.amount_tax = 0`** | inner join on `res_partner` | base from `account_move_line.balance`; **tax from the move header `amount_tax`** |
| `RPT-10`/`RPT-11` (vendor) | `strict_range` on the move date | tag membership in income + remittance + surcharge | left join, may be null | `ABS(rate) × ABS(tax_base_amount) / 100`, recomputed |
| `RPT-10`/`RPT-11` (override) | `strict_range` on the move date | branch 1: `tax_line_id` not null; branch 2: `wt_tax_id` not null **and** `payment_id is null` **and** `payment_state != 'not_paid'` | left join | branch 1 recomputed from `tax_base_amount`; branch 2 recomputed from `price_subtotal` |
| `RPT-12` | `date.range` selected in the wizard, against the certificate | certificates with the selected `income_tax_form`, in the selected company | certificate line amounts |  **column omitted when this row was written; not re-derived — open** |

## 3. Column Consistency — Inspected and Found Consistent

Declared columns were compared against emitted columns for all four SMEsPlus reports. This
check was run because a column-shift defect was hypothesised; it is recorded even though it
found nothing, so that a later reviewer does not repeat it.

| Report | Declared columns | Emitted column dicts | Result |
|---|---|---|---|
| `RPT-06` Sale Vat Report | 11 | 11 | consistent |
| `RPT-07` Sale Vat Report Zero | 9 | 9 | consistent |
| `RPT-08` Purchase Vat Report | 11 | 11 | consistent |
| `RPT-09` Purchase Vat Report Zero | 11 | 11 | consistent |

**No column misalignment exists.** What does exist is an **asymmetry**: the sale-side zero
report has neither a `Tax Period Date` nor a `Tax Name` column, while its purchase-side
twin has both, and the two handlers differ correspondingly (the purchase-zero SQL selects
`tax_period`, the sale-zero SQL does not). Recorded as `P07-F-35`: the same statutory book
is rendered with different information depending on which side of the trade it reports.

## 4. Traceability Gaps Against the Statutory Chain

| # | Chain link required by the constitution | Traceable in the reports? | Gap |
|---|---|---|---|
| `T-01` | Source business event → tax report row | partially | The report row identifies the accounting move (`move_name`), so the source document is reachable. The **tax point** is not, because it is not the selector. |
| `T-02` | Tax document → tax report row | **no** | There is no tax-document object for VAT (`05 §2`), so a report row cannot cite the tax invoice it reports; it cites the accounting document name in a column labelled "Tax Invoice No." (`l10n_th_reports/models/tax_report_vat.py:113`). |
| `T-03` | Tax accounting event → tax report row | partially | True for tax lines. **False** for the withholding write-off line, which no PND report reads, and **false** for income-side WHT, which carries no tags. |
| `T-04` | Tax report → filing | partially | A filing framework exists in the base set (`account.return`, `account.return.type`, `account.return.check`, with states and computed deadlines) and **118** localisation modules provision it. Thailand registers one return type named `Tax`, with no periodicity, no deadline delay and no workflow; PND3, PND53 and PND54 are not registered. No branch filing unit. `P07-F-37`, `08 §5`. |
| `T-05` | Adjustment → original document | **no** | No original-tax-invoice reference was found in any of the 15 reports enumerated in §1 — class `B`, boundary: the Thai reporting layer of `13 §5`; the base application's own reversal linkage was not enumerated (`S-23` `S-24`). |
| `T-06` | Report row → auditable drill-down | partially | The SMEsPlus handlers construct synthetic row ids (`'~' + '~'.join((type, str(i)))`) and the auditability annotations are commented out (`account_generic_tax_report.py:111-114`). A user cannot drill from a statutory row back to its ledger lines. |

## 5. Two Implementations of One Statutory Book

`RPT-04`/`RPT-05` and `RPT-06`/`RPT-08` are both implementations of the s.87 output and
input tax reports. They differ in every material respect listed in §2. The declared source
set contains no statement of which is canonical, no guard preventing both from being
installed, and no reconciliation between them.

Consequence for reconciliation: for the same company and the same month, the two reports
can legitimately return **different totals**.

An earlier statement of this section claimed the difference is "systematic and
one-directional" and that the SMEsPlus reports are a strict subset of the vendor reports.
**That was overstated and is corrected here.** Four reasons, each source-derivable:

1. **The unit differs, so "subset" is not defined at row level.** The vendor generator emits
   one row per **move** (`l10n_th_reports/models/tax_report_vat.py:123` iterates moves).
   The SMEsPlus handler emits one row per group of
   `date, tax_period, move_name, ref, tax_names, partner fields, type_tax_use, group name,
   tax_repartition_line_id` (`account_generic_tax_report.py:60-70`). A move carrying two
   distinct taxes in the same group produces **more** SMEsPlus rows than vendor rows.
2. **The vendor path carries the same class of label dependency.** It resolves its tags by
   the literal report-line names `1. Sales amount`, `5. Output tax`,
   `6. Purchase amount…`, `7. Input tax…` (`tax_report_vat.py:38-39`, `:49-50`), through a
   plain name equality (`account/models/account_account_tag.py:88-96`). If any of those
   four names is changed or missing, the tag set is empty, the domain matches nothing, and
   the **vendor** report empties while the SMEsPlus one does not — the reverse direction.
3. **The SMEsPlus handler imposes no tag predicate at all.** A tax placed in the `VAT 7%`
   group whose repartition lines carry no report tag appears on the SMEsPlus report and not
   on the vendor report. Under the shipped Thai template that set happens to be empty.
4. **The magnitude is unstable.** Given `P07-F-01`, the SMEsPlus set can be the empty set.

Corrected statement: **on the shipped Thai tag and group configuration, and only there, the
SMEsPlus main reports select a subset of the moves the vendor reports select. The
containment is a property of that configuration, not of the two predicates, and it is
reversible at two separately named mutable labels.** No execution was performed (`U-02`).

## 5A. Further Report Defects Found During Independent Challenge

| ID | Defect | Evidence | Class |
|---|---|---|---|
| `P07-F-41` | The `Tax Name` column of the two main SMEsPlus VAT reports is structurally empty. The column selects `tl.tax_names` where `tl` is the **tax line** (`account_generic_tax_report.py:47`, `:54`), but `tax_names` is computed from `tax_ids` (`smesplus_account_reports/models/account_move_line.py:9-13`), which is empty on a tax line except under base-affecting cascades. The purchase-zero report reads the same field from the **base** line (`:420`) and does populate it. | declared at `data/generic_tax_report.xml:55-59`, `:191-195` | source-derived, not executed (`U-02`) |
| `P07-F-42` | Zero-rated and exempt VAT are probably grouped with, and closed against, the **withholding tax** control accounts. The four 0%/EXEMPT taxes carry a blank `tax_group_id` in the template, but `account.tax.tax_group_id` is `required=True, compute='_compute_tax_group_id', precompute=True` (`account/models/account_tax.py:156-161`) and the fallback takes the first Thai group under `_order = 'sequence asc, id'` (`:274-291`, `:28`). Every Thai group ships at the default sequence, so the lowest id wins, and the template creates `tax_group_1` = `WHT 1%` first — whose settlement accounts are `213500 WHT Payable` / `114401 WHT Receivable`. | `l10n_th/data/template/account.tax-th.csv`, `account.tax.group-th.csv` | **INFERRED from record-creation order during template load; NOT executed.** Class `D — UNKNOWN` pending a runtime check. If confirmed, zero-rated exports and exempt supplies close against withholding control accounts and a 0% VAT line is labelled `WHT 1%` in the invoice tax summary. Verification is `P07-U-20`. |
| `P07-F-43` | In all four SMEsPlus handlers, `return res` sits **outside** the `for column_group_key` loop while `res` is initialised **inside** it (`:186`, `:379`, `:569`), so with more than one column group only the last group's rows survive. Present in the predecessor file as well, so it is not a migration regression. | `account_generic_tax_report.py` | source-derived, not executed |
| `P07-F-44` | Dead and duplicated code introduced or retained by the migration: a second, unused query build (`:230`, `:406`), a `tax_details_query` computed and never referenced in the sale-zero handler (`:239`), and `table_references` / `search_condition` passed to `SQL()` for placeholders that do not occur in the statement (`:74-75`). | same file | source-derived |
| `P07-F-45` | Sign asymmetry in the sale-zero handler: the base is accumulated with `sign` and the tax without it (`:299-300`), while both are displayed with `sign` (`:333`, `:337`). Numerically inert only because `amount_tax` is pinned to zero by the row predicate; it renders `-0.00` per row against `0.00` in the total. | same file | source-derived |

## 6. Licence Dependency of Statutory Function

`l10n_th_reports` is licensed `OEEL-1` (Odoo Enterprise Edition Licence) and is the module
that defines the Thai tax report handlers, the PND handlers and the Thai tax report data
consumed by `l10n_th_reports_ext`. `smesplus_account_reports` depends on `account_reports`,
also Enterprise. Both SMEsPlus modules declare `LGPL-3`.

Thai statutory reporting in the declared source set therefore **depends on
Enterprise-licensed components**, and two `LGPL-3` SMEsPlus modules inherit from them. The
licensing consequence is outside this session's competence and is routed as
`P07-D-07` in `12_P07_DEPENDENCY_REGISTER.md`, not adjudicated here.
