# LAYER 2 — P10 RAW SOURCE CITATION REGISTER (AUDIT QUARANTINE)

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001`
Classification: **LAYER 2 — AUDIT QUARANTINE. Boss / PMO / AI-Audit only.**
Distribution: MUST NOT be transcribed into Layer 1 deliverables, reference packages, or any Team B artefact.
Layer 1 documents cite the `E-P10-nnn` identifier only.

## 0. Declared Reference Roots

| ID | Root | Modules (`find -name __manifest__.py \| wc -l`) | Role |
|----|------|-----|------|
| `RR-1` | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608` | 1753 | **Primary reference root for this session** (contains `odoo/addons` = 790 and `odoo/addons_archive` = 959) |
| `RR-2` | `/Volumes/iMacSys/CLAUDE AI/MIGRATION/ODOO18/odoo-18.0+e.20250608` | 793 | Same build string, **different content** — no `addons_archive`. Divergence recorded as `P10-C-07`. |
| `RR-3` | `/Volumes/iMacSys/ODOO/SOURCE CODE/ODOO 18/odoo-18.0.post20260605` | 683 | Community line, used for edition-boundary proof |
| `RR-4` | `/Volumes/iMacSys/CLAUDE AI/MIGRATION/ODOO18/odoo-18.0.post20260605` | 687 | Community line, second copy |
| `RR-5` | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18` | 2727 | Includes project custom addon sets |
| `RR-6` | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo14` | 133 | Legacy line, custom Thai modules |

All `file:line` citations below are relative to `RR-1/odoo/`.

## 1. Evidence Register

| ID | Citation (`path:line -- method`) | What it establishes | Class |
|----|----------------------------------|---------------------|-------|
| `E-P10-001` | `addons/account_accountant/models/account_move.py:439-453 -- AccountMoveLine fields` | The entire deferral schedule is two `Date` fields on a journal item (`deferred_start_date`, `deferred_end_date`), both `copy=False`, plus two computed booleans. No schedule model exists. | VERIFIED FACT |
| `E-P10-002` | `addons/account_accountant/models/account_move.py:109-115 -- _post` | Deferral generation is triggered inside `_post`, after `super()._post()`, gated on the company method being `on_validation` and any line carrying a start date. | VERIFIED FACT |
| `E-P10-003` | `addons/account_accountant/models/account_move.py:145-149 -- _get_deferred_entries_method` | Generation method is read from `self.company_id` (document company) and is direction-selected by `is_outbound()`. | VERIFIED FACT |
| `E-P10-004` | `addons/account_accountant/models/account_move.py:229-231 -- _get_deferred_amounts_by_line` | The **amount computation method** is read from `self.env.company` (active company), not from the document's company. Journal and account in the same flow are read from `self.company_id`. | VERIFIED FACT |
| `E-P10-005` | `addons/account_accountant/models/account_move.py:160-176 -- _get_deferred_diff_dates` | Month arithmetic uses a **30-day synthetic month**; the last calendar day of any month is normalised to day 30. | VERIFIED FACT |
| `E-P10-006` | `addons/account_accountant/models/account_move.py:179-196 -- _get_deferred_period_amount` | Three computation methods: `day` (true calendar days), `month` (30/360), `full_months` (both ends snapped to day 1). | VERIFIED FACT |
| `E-P10-007` | `addons/account_accountant/models/account_move.py:563-590 -- _get_deferred_ends_of_month / _get_deferred_periods` | Recognition periods are always calendar-month segments. The *computation* may be daily; the *schedule* is monthly in every configuration. | VERIFIED FACT |
| `E-P10-008` | `addons/account_accountant/models/account_move.py:258-353 -- _generate_deferred_entries` | One "fully deferred" entry dated at the source move date plus one entry per month-end, each `auto_post='at_date'`, all created in one transaction at posting time. | VERIFIED FACT |
| `E-P10-009` | `addons/account_accountant/models/account_move.py:313-321 -- _generate_deferred_entries` | Rounding residue is forced into the **last** period by `force_balance = remaining_balance`. | VERIFIED FACT |
| `E-P10-010` | `addons/account_accountant/models/account_move.py:335-353 -- _generate_deferred_entries` | Same-month self-cancelling pairs are detected by `(date.replace(day=1), amount_total)` equality and unlinked. Amount equality is part of the key. | VERIFIED FACT |
| `E-P10-011` | `addons/account_accountant/models/account_move.py:604-614 -- _get_deferred_lines_values` | The generated deferral line carries `account_id`, `product_id`, `product_category_id`, `balance`, `name`, `analytic_distribution`. **No `amount_currency`, no `currency_id`.** | VERIFIED FACT |
| `E-P10-012` | `addons/account_accountant/models/account_move.py:485-501 -- AccountMoveLine.write` | Changing `account_id` is blocked once deferral entries exist. This is the only in-flight mutation guard found on the deferral surface. | VERIFIED FACT |
| `E-P10-013` | `addons/account_accountant/models/account_move.py:124-134 -- button_draft` | Reset-to-draft reverses or unlinks the deferral entries; a deferral grouping more than one original move blocks reset entirely. | VERIFIED FACT |
| `E-P10-014` | `addons/account_accountant/models/account_move.py:477-483 -- copy_data` | Deferral dates are propagated on copy **only** under the `move_reverse_cancel` context; every other copy path drops them. | VERIFIED FACT |
| `E-P10-015` | `addons/account_accountant/models/account_move.py:507-522 -- _compute_has_abnormal_deferred_dates` | A UI-level warning flag for the 12-month-plus-one-day case. Advisory only; no constraint. | VERIFIED FACT |
| `E-P10-016` | `addons/account_accountant/models/account_move.py:555-560 -- _check_deferred_dates` | Constraint: start without end is rejected; start later than end is rejected. | VERIFIED FACT |
| `E-P10-017` | `addons/account_accountant/models/account_move.py:526-540 -- _has_deferred_compatible_account` | Eligibility is by account type and document direction; enforced by `onchange` only. | VERIFIED FACT |
| `E-P10-018` | `addons/account_accountant/models/res_company.py:18-71` | Eight company-level settings: journal, account, generation method (`on_validation` / `manual`), computation method (`day` / `month` / `full_months`), for expense and revenue independently. | VERIFIED FACT |
| `E-P10-019` | `addons/account_reports/models/account_deferred_reports.py:481-538 -- _get_moves_to_defer / _generate_deferral_entry` | The grouped path reads journal, deferral account, rounding currency and the lock-date check from `self.env.company`, while the line population is scoped by `get_report_company_ids(options)`. | VERIFIED FACT |
| `E-P10-020` | `addons/account_reports/models/account_deferred_reports.py:502 -- _generate_deferral_entry` | Explicit lock-date guard raising `UserError`. No equivalent exists in `E-P10-008`. | VERIFIED FACT |
| `E-P10-021` | `addons/account_reports/models/account_deferred_reports.py:519-523 -- _generate_deferral_entry` | The grouped path books a period-end entry and a next-day reversal — an accrual shape, not a recognition shape. | VERIFIED FACT |
| `E-P10-022` | `addons/account_reports/models/account_deferred_reports.py:48-62 and 84-105 -- _get_domain / _get_select` | The only duplicate-generation control on the grouped path. Key = existence of a related deferral move with `date = period end` AND (`state = posted` OR (`auto_post = at_date` AND `date >= today`)). | VERIFIED FACT |
| `E-P10-023` | `addons/account_reports/data/deferred_reports.xml:9 and :33` | Both deferred reports declare `filter_multi_company = selector`. | VERIFIED FACT |
| `E-P10-024` | `addons/account/wizard/accrued_orders.py:10-55 -- AccruedExpenseRevenue` | Accrual is a transient wizard. Default date = last day of previous month. Account domain is direction-dependent. | VERIFIED FACT |
| `E-P10-025` | `addons/account/wizard/accrued_orders.py:65-70 -- _compute_reversal_date` | Reversal date defaults to accrual date + 1 day and is user-editable. | VERIFIED FACT |
| `E-P10-026` | `addons/account/wizard/accrued_orders.py:117-127 and 138-142 -- _get_aml_vals / _compute_move_vals` | `amount_currency` / `currency_id` are set **only** when exactly one order is selected and its currency differs from the company currency. Mixed-currency and mixed-company selections raise. | VERIFIED FACT |
| `E-P10-027` | `addons/account/wizard/accrued_orders.py:143, 243, 250, 259-267 -- _compute_move_vals / create_entries` | `orders_with_entries` is initialised to `[]`, returned, and iterated — and is **never appended to anywhere in the module**. The chatter message linking the accrual entry back to its source order therefore never executes. | VERIFIED FACT |
| `E-P10-028` | `addons/account/wizard/accrued_orders.py:245-258 -- create_entries` | Both the accrual and its reversal are posted with `_post()` (hard), not `_post(soft=True)`. | VERIFIED FACT |
| `E-P10-029` | `addons/account_asset/models/account_asset.py:636-648 -- compute_depreciation_board` | The asset board is a persistent set of draft entries, destroyed and rebuilt on recompute, then posted. | VERIFIED FACT |
| `E-P10-030` | `addons/account_asset/models/account_asset.py:535-536 and 890-891 -- write / set_to_close` | Asset carries explicit lock-date guards on both in-flight mutation and disposal. | VERIFIED FACT |
| `E-P10-031` | `addons/account_asset/models/account_asset.py:254-271 and 724-741 -- _compute_lifetime_days / _get_delta_days` | Two day conventions selected by `prorata_computation_type`: `constant_periods` (30/360) and `daily_computation` (true calendar). Consistent with the prior Asset session finding. | VERIFIED FACT |
| `E-P10-032` | `addons/account_loans/models/account_loan_line.py:4-46 -- AccountLoanLine` | A persistent schedule model with a date, principal, interest, and a **reverse link** `generated_move_ids` keyed on `generating_loan_line_id`. | VERIFIED FACT |
| `E-P10-033` | `addons/account_loans/models/account_loan.py:175-300 -- action_confirm` | Entry generation stamps `generating_loan_line_id` and `is_loan_payment_move` on every generated move, sets `company_id` explicitly, uses `auto_post='at_date'`, and posts only entries dated on or before today. | VERIFIED FACT |
| `E-P10-034` | `addons/account_loans/models/account_loan_line.py:18` | `currency_id` is `related='company_id.currency_id'` — the loan schedule cannot express a foreign currency. | VERIFIED FACT |
| `E-P10-035` | `addons/account/models/account_move.py:4922-4926 -- _post` | Under `soft=True`, any move dated after today is left in draft and forced to `auto_post='at_date'`. | VERIFIED FACT |
| `E-P10-036` | `addons/account/models/account_move.py:4934-4936 -- _post` | When a move being posted violates a lock date, **`move.date` is overwritten** with `_get_accounting_date(...)`. No exception, no chatter, no flag. | VERIFIED FACT |
| `E-P10-037` | `addons/account/models/account_move.py:5655-5692 -- _get_accounting_date` | The replacement date is derived from the lock date + 1 day, the sequence reset pattern and today — not from the recognition schedule. | VERIFIED FACT |
| `E-P10-038` | `addons/account/models/account_move.py:5430-5455 -- _autopost_draft_entries` | The auto-post cron searches drafts with **no company filter**, batches 100, and calls `_post()` under the cron user's company context. | VERIFIED FACT |
| `E-P10-039` | `addons/account/models/account_move.py:264-285 and 4035-4045 -- auto_post fields / _copy_recurring_entries` | A fourth, independent time mechanism: recurring entries (`monthly`/`quarterly`/`yearly` + `auto_post_until` + `auto_post_origin_id`) which copy a move forward in time. | VERIFIED FACT |
| `E-P10-040` | `addons/account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:477-480` and `addons/account_edi_ubl_cii/models/account_edi_common.py:512-528` | The same two deferral date fields are exported as, and imported from, the statutory `InvoicePeriod` of an electronic invoice. | VERIFIED FACT |
| `E-P10-041` | `addons/sale_subscription/models/sale_order_line.py:255-273` | Subscription billing writes the recognition period onto the invoice line from the billing plan. | VERIFIED FACT |
| `E-P10-042` | `addons/account_accountant/views/account_move_views.xml:17-21, 53-55, 76-104` | The deferral surface in the UI is two optional, hidden-by-default columns plus two navigation buttons. There is no schedule screen. | VERIFIED FACT |
| `E-P10-043` | `addons/account_reports/data/menuitems.xml:20-21` | Two reporting menus (`Deferred Revenue`, `Deferred Expense`) under reporting management, read-only group. | VERIFIED FACT |
| `E-P10-044` | Path-set enumeration `P10_ENUM_01` / `P10_ENUM_02` | `account_accountant`, `account_reports`, `account_asset`, `account_loans` and `sale_subscription` are **absent from `RR-3` and `RR-4`**; the accrual wizard and recurring entries are present in the base accounting module. Deferral, asset and loan recognition are edition-gated; accrual is not. | VERIFIED FACT (scope: `RR-3`, `RR-4`) |
| `E-P10-045` | `addons/account/models/account_move.py:4814-4830 -- _unlink_or_reverse` | Three-way disposal of generated entries: unlink, cancel (audit-trail protected), or reverse. Which one applies is decided per move, not per schedule. | VERIFIED FACT |

## 2. Enumeration Artefacts

- `p10_scripts/p10_enum_01_path_set.sh` → `raw/P10_ENUM_01_PATH_SET.txt`
- `p10_scripts/p10_enum_02_mechanisms.sh` → `raw/P10_ENUM_02_MECHANISMS.txt`

Both scripts declare POPULATION, PATTERN, UNIT and PATH SET in their header and are re-runnable by a third party without modification.

## 3. Evidence Added by Independent Challenge (AAS-03 rounds 1–4)

Every item below was **re-verified by the primary author against primary source** before being admitted. Items the author could not re-verify are marked as such and are not used in Layer 1.

| ID | Citation (`path:line -- method`) | What it establishes | Class | Re-verified by author |
|----|----------------------------------|---------------------|-------|------------------------|
| `E-P10-046` | `addons/account_reports/models/account_deferred_reports.py:482 -- _get_moves_to_defer` | The grouped path computes from `DEFERRED_DATE_MIN` (`1900-01-01`) every run — it is **cumulative-to-date**, so a skipped month is absorbed by the next run. A genuine catch-up mechanism. | VERIFIED FACT | Yes |
| `E-P10-047` | `addons/account/wizard/account_automatic_entry_wizard.py:14-19, 262-314 -- _get_move_line_dict_vals_change_period` | A further period-reallocation mechanism that **does** carry `amount_currency` and `currency_id` on every generated line. | VERIFIED FACT | Yes |
| `E-P10-048` | `addons/account_asset/models/account_asset.py:1042-1097 -- _create_move_before_date`, called from `addons/account_asset/wizard/asset_modify.py:283 -- modify` and `account_asset.py:988 -- pause` | The asset catch-up is a **stub entry cut at the modification date**. `_recompute_board` (`:649-708`) is purely prospective and is **not** the catch-up device. | VERIFIED FACT | Yes |
| `E-P10-049` | `addons/account_asset/models/account_asset.py:20 -- class AccountAsset._description` = `'Asset/Revenue Recognition'`; `:693` live comment `# For deferred revenues, we should invert the amounts.` | Depreciation and deferred revenue were **one engine** in this product line. Directly bears on the Boss's standing warning. | VERIFIED FACT | Yes |
| `E-P10-050` | `addons/account_reports/models/account_deferred_reports.py:494 -- _get_moves_to_defer` passes `self._get_deferred_report_type() == 'expense'` (a boolean) into `:552 -- _get_deferred_lines(…, is_reverse, …)`, which forwards it at `:561` to `addons/account_accountant/models/account_move.py:198 -- _get_deferred_amounts_by_line(…, deferred_type)`, whose `:230` tests `deferred_type == "expense"`. Contrast the display path at `account_deferred_reports.py:428`, which passes the correct string. | **A boolean can never equal `"expense"`, so the grouped generation path always applies the REVENUE allocation method — on both reports.** The report *displays* one allocation and the generate button *posts* another whenever the two direction settings differ. | VERIFIED FACT | Yes — call site, callee signature, branch and the correct display call all read directly |
| `E-P10-051` | `addons/account_accountant/models/account_move.py:243 -- _get_deferred_lines` | No caller anywhere in `addons`: the only call site resolves to the reports handler's own same-named method with a different signature. Dead code carrying a `force_balance` and `grouping_field` capability that nothing uses. | VERIFIED FACT | Yes |
| `E-P10-052` | `addons/account_accountant/models/account_move.py:30-47` (both many-to-many definitions); `addons/account_reports/models/account_deferred_reports.py:526-531` | The source-document ↔ deferral-entry links carry **no company check**, and the grouped path writes the relation with raw SQL that bypasses the ORM entirely. | VERIFIED FACT | Partially — field definitions re-read; the raw-SQL insert re-read; the absence of a company check across all overlays is class `B` |
| `E-P10-053` | `addons/account/models/account_report.py` (model body); `addons/account_reports/models/account_deferred_reports.py` (zero occurrences of `companies`) | The report object and its handler carry **no company at all**, yet the handler creates and posts a company-owned journal entry. | VERIFIED FACT | Yes for the handler; the report model scan is reviewer-supplied, class `B` |
| `E-P10-054` | `addons/account/models/account_move.py:831-834 -- _compute_company_id` | An entry created without an explicit company takes its company from the journal, falling back to the active company. This is how the grouped deferral entry acquires its owner. | VERIFIED FACT | Yes |
| `E-P10-055` | `addons/account/models/account_account.py:25` (`_check_company_domain = check_companies_domain_parent_of`) and the ORM helper it names | Account/company compatibility is satisfied when **any** company in the account's company set is a parent of the entry's company. With a shared chart, the cross-company check does not fire. | VERIFIED FACT | Yes for the assignment line; the helper body is reviewer-supplied, class `B` |
| `E-P10-056` | `addons/account/models/account_move.py:2355-2375 -- _get_unbalanced_moves` | Balance validation sums company-currency amounts only. **No mechanism in P10 has a foreign-currency integrity backstop.** | VERIFIED FACT | Reviewer-supplied, class `B` — not independently re-read by the author |
| `E-P10-057` | `addons/account_accountant/views/account_move_views.xml:20-21` (read-only once deferred) vs `:54-55` (no read-only) | The only protection against editing a schedule that has already generated entries is **view-level and present on one view of two**. | VERIFIED FACT | Yes |
| `E-P10-058` | `addons/account_reports/tests/test_deferred_reports.py`, `addons/account_accountant/tests/test_deferred_management.py` | Zero multi-company and zero foreign-currency deferral tests. Explains why the scope and currency defects survived upstream. | VERIFIED FACT (scope: those two files, pattern declared in the challenge report) | Reviewer-supplied, class `B` |
| `E-P10-059` | `addons/account/models/account_move.py:4805-4830 -- _can_be_unlinked / _is_protected_by_audit_trail / _unlink_or_reverse` | The cancel branch is **unreachable**: reaching it requires the same expression to be both false and true. With the audit trail on, a previously-posted generated entry is always reversed, never cancelled. | VERIFIED FACT | Yes — all three method bodies re-read |
| `E-P10-060` | `addons/account/models/company.py:53-99` (five lock-date fields) and `:598-663 -- _get_lock_date_violations / _get_violated_lock_dates` | Recognition entries post to general journals and carry no tax, so **only the fiscal-year lock and the hard lock ever bind them**. | VERIFIED FACT | Reviewer-supplied, class `B` — path corrected from the author's brief, which named a non-existent file |
| `E-P10-061` | `addons/account/wizard/accrued_orders.py:231 -- _compute_move_vals` | The balancing counterpart line is built from the whole order set, so it fails the single-order test and carries no currency; with one foreign-currency order it is stamped with the foreign currency and a zero foreign amount. | VERIFIED FACT | Yes for the call; the resulting posted state is `INFERENCE` |
| `E-P10-062` | `addons/account_loans/models/account_loan.py:373-375 -- action_reset` vs `:391-397 -- action_cancel / action_set_to_draft` | Three teardown paths reverse the generated entries first; the fourth deletes the schedule without touching them, orphaning posted entries. | VERIFIED FACT | Yes |
| `E-P10-063` | `addons/account_loans/models/account_loan.py:54-57` (help text says "up to this date (included)") vs `:202` (strict less-than) | Off-by-one: the line dated exactly on the skip boundary is generated, against the documented intent. | VERIFIED FACT | Yes |
| `E-P10-064` | `addons/account_loans/models/account_loan.py:175-300 -- action_confirm`, state assignment at `:299-300` | Confirmation contains no state guard and no check for existing generated entries; a fully historical schedule leaves the state unchanged, so the action remains available. | VERIFIED FACT | Reviewer-supplied; author re-read `:373-375` and the state assignment, class `B` for the full re-entrancy path |
| `E-P10-065` | `addons/account_reports/models/account_deferred_reports.py:108, 113, 116, 142 -- _get_lines / _fetch_lines` | The fetched line set is cached under a **bare literal key**, not parameterised by report, direction, period or draft/posted selection, and the cache lives for the whole database cursor. | VERIFIED FACT | Yes |
| `E-P10-066` | `addons/account/models/account_move.py:5436, 5451 -- _autopost_draft_entries` | A scheduled entry that fails to post once is flagged unchecked, and the same routine's own filter then excludes unchecked entries permanently. | VERIFIED FACT | Yes |
| `E-P10-067` | `addons/account_auto_transfer/models/transfer_model.py:15, 33-42` | A further periodic mechanism with start date, stop date and frequency, generating entries on a schedule. | VERIFIED FACT | Yes |
| `E-P10-068` | `addons/account/models/account_move.py:2377-2394 -- _check_fiscal_lock_dates`, invoked from `:3230-3235` | The date-change guard evaluates the record's **current** date, not the incoming one, so it validates the source period and never the destination. | VERIFIED FACT | Reviewer-supplied, class `B` — not independently re-read by the author |

### 3.1 Author re-verification statement

Of the 23 challenge-originated items, **14 were re-read line-by-line by the primary author** and are carried as VERIFIED FACT without qualification. **9 are carried as reviewer-supplied with class `B`** and are marked in the table. Per `Independent Review != Truth`, none of the nine is used as the sole support for a Layer 1 finding that changes a gate outcome; each is cross-referenced to an author-verified item or is recorded in the unknown register.

## 4. Deployed-Database Evidence (Stage E cross-layer correlation)

Added after `P10-R-08`. Source: three readable deployed database archives on the execution host; a fourth is class `C` (archive format not openable by the host's tooling). Extraction script `p10_scripts/p10_enum_03_deployed_schema.sh`, raw output `raw/P10_ENUM_03_DEPLOYED_SCHEMA.txt`.

Databases: A (`BK12MAY26_2026-08-03`), B (`iEVING_2026-07-23`), C (`iSMEs_2026-07-11`), D (`iTEST02_2026-07-14`, unreadable).

| ID | Observation | Databases | Class |
|----|-------------|-----------|-------|
| `E-P10-069` | `public.account_move_line` carries `deferred_start_date` and `deferred_end_date` | A, B — **absent in C** | VERIFIED FACT |
| `E-P10-070` | `public.account_move_deferred_rel` exists | A, B — absent in C | VERIFIED FACT |
| `E-P10-071` | `public.res_company` carries all eight deferral configuration columns | A (195 cols), B (188 cols) — absent in C | VERIFIED FACT |
| `E-P10-072` | `public.account_account` has **no `company_id` column**; company linkage is only `public.account_account_res_company_rel (account_account_id, res_company_id)` | A, B. **C has `company_id integer NOT NULL`** | VERIFIED FACT |
| `E-P10-073` | Chart sharing: A = 545 relation rows, 544 distinct accounts, 11 distinct companies, **1 account in more than one company**. B = 544 rows, 544 accounts, 11 companies, **0 accounts shared** | A, B | VERIFIED FACT |
| `E-P10-074` | `public.res_company` holds **44 rows** in each of A and B. All 44 have `generate_deferred_expense_entries_method = on_validation`, `deferred_expense_amount_computation_method = month`, `generate_deferred_revenue_entries_method = on_validation`, `deferred_revenue_amount_computation_method = month`. **Asymmetric configurations: 0.** 43 of 44 have at least one deferral account or journal set | A, B | VERIFIED FACT |
| `E-P10-075` | `public.account_move_deferred_rel` contains **0 rows** in both A and B. The data-only extraction artefact is **886 bytes, header only**, proving an empty table rather than a failed extraction | A, B | VERIFIED FACT |
| `E-P10-076` | `public.account_loan*` present in A and B, **absent in C**. `public.account_transfer_model` **absent in A and B, present in C**. `public.account_asset` present in all three | A, B, C | VERIFIED FACT |

### 4.1 Control applied

Every zero above is reported together with the byte size of the artefact it was counted from. This control was adopted from a peer session's recorded lesson, in which an empty extraction produced six fabricated class-`A` absences caught only by a line count.
