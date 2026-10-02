# U47 — account remaining (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U47
- Modules: account (remaining areas — delta from U10/U30/U31/U32/U33)
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: DELTA-FIRST — covering only unread areas: account_bank_statement_line.py, res_currency.py, account_payment_register.py (wizard), accrued_orders.py (wizard), account_move_reversal.py (wizard), account_partial_reconcile.py, account_full_reconcile.py, account_reconcile_model.py, account_payment_term.py, account_cash_rounding.py. Source evidence only; no runtime proof; RT flags for runtime unknowns.

---

## CAP-U47-01 Bank Statement Line Model and Reconciliation Engine

### D1 Business purpose and process semantics
The bank statement line model represents a single imported or manually entered bank transaction. It is the unit of bank reconciliation — each line must be matched to one or more accounting entries (invoices, payments, or new journal entries) until the residual amount reaches zero, after which `is_reconciled` is set to True. Unreconciled lines park their counterpart balance in the journal's suspense account.

### D2 Architecture, data and object relationships
`account.bank.statement.line` uses `_inherits = {'account.move': 'move_id'}` to delegate its journal entry storage to `account.move`. Key fields: `move_id` (Many2one, required, ondelete=cascade), `statement_id` (Many2one to `account.bank.statement`), `payment_ids` (Many2many to `account.payment` via `account_payment_account_bank_statement_line_rel`), `amount`, `foreign_currency_id`, `amount_currency`, `amount_residual` (computed, stored), `is_reconciled` (computed, stored), `internal_index` (computed, stored). Three partial indexes: `_unreconciled_idx` on `(journal_id, company_id, internal_index) WHERE is_reconciled IS NOT TRUE`, `_orphan_idx` on same columns `WHERE statement_id IS NULL`, and `_main_idx` unconditional.

### D3 Source, technical and workflow logic
- On `create`, `move_type` is forced to `'entry'` (line 390) and `action_post()` is automatically called (line 420).
- Two journal items are always prepared: a liquidity line to `journal_id.default_account_id` and a counterpart to `journal_id.suspense_account_id` (lines 662–684).
- `_compute_internal_index` encodes date + complement-of-sequence + id as a string: `f'{date.strftime("%Y%m%d")}{MAXINT - sequence:0>10}{id:0>10}'` using MAXINT=2147483647 (lines 278–280).
- Running balance is computed via raw SQL: it finds the latest `account_bank_statement.balance_start` before the current line as an anchor point, then sums posted amounts forward (lines 199–256).
- `_seek_for_lines()` classifies move lines as liquidity, suspense, or other (lines 686–707); falls back to `account_type in ('asset_cash','liability_credit_card')` when no default-account match.
- `action_undo_reconciliation()` calls `line_ids.remove_move_reconcile()`, unlinks auto-generated `payment_ids`, and resets to suspense lines (lines 460–476).
- Bidirectional synchronisation: `_synchronize_from_moves` updates the statement line from move changes; `_synchronize_to_moves` pushes statement-line field changes back to the move. Both guard via `skip_account_move_synchronization` context key (lines 712–836).
- `_check_allow_unlink` prevents deletion if the parent statement is both valid and complete (lines 482–486).
- On `unlink`, for companies with restrictive audit trail, the move is cancelled before deletion instead of deleted (lines 430–437).

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| 1 | Data lifecycle | Created auto-posted (line 420); unlinked with cascade to move unless audit-trail applies (line 432); undo reconciliation resets to suspense |
| 2 | State machine | `is_reconciled` (computed stored, line 130); `checked` field inherited from account.move; no explicit state field on this model |
| 3 | Computation engine | `internal_index`: date+MAXINT-sequence+id encoding (line 278); `running_balance`: SQL anchor from statement.balance_start (lines 199–252); `is_reconciled` / `amount_residual` via `_seek_for_lines` (lines 287–314) |
| 4 | Access control / security | `_check_company_auto = True` (line 16); `bypass_search_access=True` on `move_id` (line 27); restrictive_audit_trail guard on unlink (line 432) |
| 5 | Integration / external | `payment_ids` M2M links to auto-generated payments (lines 52–56); `_find_or_create_bank_account` optionally creates `res.partner.bank` (lines 488–502); config param `account.skip_create_bank_account_on_reconcile` (line 492) |
| 6 | Error handling / constraints | `_check_amounts_currencies`: foreign_currency_id != currency_id required when both set (lines 320–333); UserError if suspense_account_id not set (lines 639–643); UserError if liquidity lines != 1 (lines 731–737) |
| 7 | Configuration / parametrisation | Uses `journal_id.suspense_account_id` (line 637) and `journal_id.default_account_id` (line 662) |
| 8 | Localisation / l10n hooks | `country_code` related to `company_id.account_fiscal_country_id.code` (line 110) |
| 9 | Automation / scheduling | None directly; RT: statement reconciliation models apply automatically when trigger='auto_reconcile' |
| 10 | Extension / override surface | `_prepare_move_line_default_vals` is the key override point for custom line creation logic (line 629); `_seek_for_lines` extensible |

---

## CAP-U47-02 Currency Table and Multi-Currency Reporting

### D1 Business purpose and process semantics
The `res.currency` extension in the account module creates a temporary PostgreSQL table called `account_currency_table` that enables multi-period, multi-company financial reports to aggregate amounts from different currencies at the correct rates (historical, current, or average). This powers the multicurrency balance sheet and income statement consolidation.

### D2 Architecture, data and object relationships
`_inherit = 'res.currency'` (line 10). Adds: `display_rounding_warning` (Boolean computed, warns on rounding change), `fiscal_country_codes` (Char, non-stored). Key methods: `_get_simple_currency_table`, `_check_currency_table_monocurrency`, `_get_monocurrency_currency_table_sql`, `_create_currency_table`. The temporary table columns: `company_id`, `period_key`, `date_from`, `date_next`, `rate_type` ('historical'/'current'/'average'), `rate`.

### D3 Source, technical and workflow logic
- `write()` override blocks reducing a currency's decimal precision if accounting entries already exist: calls `_has_accounting_entries()` which does `search_count` on `account.move.line` for that currency (lines 26–33, 35–41).
- `_check_currency_table_monocurrency` returns True when all companies share one currency (line 58): in that case a lightweight VALUES-based inline SQL substitutes the temp table (lines 67–72).
- `_create_currency_table` creates a `TEMPORARY TABLE account_currency_table ON COMMIT DROP` with an index and ANALYZE (lines 123–140). It builds via UNION ALL of four builder functions.
- Historical rates use a LATERAL join to look up the domestic rate per-row: `LEFT JOIN LATERAL (SELECT dr.rate FROM res_currency_rate dr WHERE ... ORDER BY dr.name DESC LIMIT 1) domestic_rate ON true` (lines 207–216).
- Average rates split the period into segments at every rate-change breakpoint for both the foreign and domestic currencies, weight each segment by number of days, and compute a day-weighted average (lines 252–313).
- Current rates: `DISTINCT ON (other_company.id)` with `ORDER BY other_company.id, rate.name DESC` to pick the most recent rate at or before `date_to` (lines 167–190).

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| 1 | Data lifecycle | Temp table created per reporting request, `ON COMMIT DROP` (line 131); destroyed at transaction end |
| 2 | State machine | N/A — functional utility model |
| 3 | Computation engine | Three rate types: current (DISTINCT ON latest), historical (lateral per-date), average (day-weighted breakpoint segments) |
| 4 | Access control / security | write() raises UserError if rounding reduced on used currency (line 31) |
| 5 | Integration / external | `_get_simple_currency_table` called by report engine; domestic-rate lateral join uses `res_currency_rate` table directly (line 208) |
| 6 | Error handling / constraints | `UserError` on rounding reduction after accounting use (line 31) |
| 7 | Configuration / parametrisation | `use_cta_rates` param (lines 98–99) enables historical/average in addition to current; `date_periods` list controls time periods |
| 8 | Localisation / l10n hooks | `fiscal_country_codes` field (line 17); `_get_fiscal_country_codes` returns codes for all active companies (line 13) |
| 9 | Automation / scheduling | None |
| 10 | Extension / override surface | All builder methods (`_get_table_builder_*`) are separate overridable methods; `use_cta_rates` parameter gating |

---

## CAP-U47-03 Payment Register Wizard

### D1 Business purpose and process semantics
The payment register wizard (`account.payment.register`) is the UI-backed transient model that converts one or multiple outstanding receivable/payable journal items into `account.payment` records. It handles grouping logic, installment-aware amounts, early payment discounts, payment difference write-offs, and exchange difference reconciliation.

### D2 Architecture, data and object relationships
`_name = 'account.payment.register'`, `_check_company_auto = True` (lines 13–15). Receives `line_ids` (M2M to `account.move.line`) via context. Computes `batches` (Binary field grouping lines by partner/account/currency/partner_bank). Key computed fields: `amount`, `payment_difference`, `payment_difference_handling`, `installments_mode`, `early_payment_discount_mode`, `can_edit_wizard`, `group_payment`, `writeoff_is_exchange_account`.

### D3 Source, technical and workflow logic
- `_compute_batches` groups lines by `frozendict({'partner_id','account_id','currency_id','partner_bank_id','partner_type'})` and merges inbound+outbound for same partner if unique bank per direction (lines 332–396).
- `default_get` filters lines to those with non-zero residual amounts and raises `UserError` for: no residual (line 975), multi-company root (line 976), sibling-company without parent access (line 978), mixed inbound/outbound (line 980), blocked invoices (line 982).
- `_get_total_amounts_to_pay` iterates installments from `account.move.line._get_installments_data()` with installment types: `overdue`, `next`, `before_date`, `early_payment_discount` (lines 628–701).
- `_create_payments` orchestrates three steps: `_init_payments` (create account.payment records), `_post_payments` (call `action_post`), `_reconcile_payments` (reconcile payment lines with source lines) (lines 1218–1299).
- Edit mode applies only when `can_edit_wizard=True` AND (single-line batch OR group_payment=True) (line 1235).
- Exchange difference handling: when `writeoff_is_exchange_account` is True and source/payment currencies differ, `force_balance` is added to payment vals forcing exact company-currency balance (lines 1028–1034).
- Early payment discount: calls `account.move._get_invoice_counterpart_amls_for_early_payment_discount` to build write-off lines (lines 1012–1025).
- QR code: generated via `partner_bank_id.build_qr_code_base64()` for manual outbound payments when `partner_bank_id.allow_out_payment` is True (lines 874–897).
- Trust check: `_compute_trust_values` validates that `partner_bank_id.allow_out_payment` is True for each batch when `require_partner_bank_account` is True (lines 399–426).
- Duplicate detection: delegates to `account.payment._fetch_duplicate_reference()` (lines 912–928).
- `action_create_payments` returns a window action to the created payment(s) (lines 1308–1332).
- Sibling-company payments: runs wizard under `sudo()` if lines belong to sibling companies (line 1292).
- Context key `dont_redirect_to_payments` suppresses the post-creation redirect (lines 1313–1314).

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| 1 | Data lifecycle | TransientModel; lines from context; payments created and posted in `action_create_payments` (line 1308) |
| 2 | State machine | `can_edit_wizard` gates edit mode; `installments_mode` selection (next/overdue/before_date/full) drives amount computation |
| 3 | Computation engine | `_get_total_amounts_to_pay` with installment decomposition (lines 628–701); currency conversion via `_convert_to_wizard_currency` (lines 597–626) |
| 4 | Access control / security | `_check_company_auto = True`; sibling-company sudo (line 1292); blocked invoice guard (line 982) |
| 5 | Integration / external | QR code via `res.partner.bank.build_qr_code_base64` (line 884); duplicate check via `account.payment._fetch_duplicate_reference` (line 928) |
| 6 | Error handling / constraints | 6 UserError cases in `default_get` (lines 947–983); untrusted bank account warnings (lines 399–426); UserError when all batches skip due to unvalidated bank accounts (lines 1229–1232) |
| 7 | Configuration / parametrisation | `installments_switch_html` renders switchable UI hints; `custom_user_amount` persists user-entered free-form amounts (lines 82–83) |
| 8 | Localisation / l10n hooks | `country_code` from `company_id.account_fiscal_country_id.code` (line 161) |
| 9 | Automation / scheduling | None; wizard is always user-initiated |
| 10 | Extension / override surface | `_create_payment_vals_from_wizard` (line 993), `_create_payment_vals_from_batch` (line 1054), `_init_payments` (line 1111), `_post_payments` (line 1172), `_reconcile_payments` (line 1187) are all independent override points |

---

## CAP-U47-04 Accrued Orders Wizard

### D1 Business purpose and process semantics
The accrued orders wizard (`account.accrued.orders.wizard`) creates a journal entry accruing the difference between delivered/received and invoiced quantities on purchase or sale orders at a given date. It simultaneously creates and posts the corresponding reversal entry on the next day, establishing a self-reversing accrual pair. The wizard is driven from `purchase.order`, `sale.order`, `purchase.order.line`, or `sale.order.line` active model context.

### D2 Architecture, data and object relationships
`_name = 'account.accrued.orders.wizard'`, `_check_company_auto = True` (lines 13–15). Fields: `journal_id` (Many2one, general journal), `date` (Date, defaults to last day of previous month), `reversal_date` (computed, date+1 day), `amount` (Monetary, optional override), `account_id` (Many2one, `liability_current` for purchase, `asset_current` for sale), `preview_data` (Text, JSON-encoded preview), `display_amount` (Boolean).

### D3 Source, technical and workflow logic
- `_get_default_date` returns the last day of the previous month: `date_utils.get_month(today)[0] - relativedelta(days=1)` (line 24).
- `_compute_reversal_date` ensures `reversal_date > date`, defaults to `date + 1 day` (lines 67–72).
- `_compute_move_vals` is the core computation method. It dispatches on `active_model` to get orders and lines (lines 138–144). `is_purchase` is determined from `orders._name == 'purchase.order'` (line 145).
- For purchase orders: uses `qty_invoiced_at_date` and `qty_received_at_date`; computes `price_unit_discounted`; handles price-diff account lines for perpetual valuation (lines 181–246).
- For sale orders: uses `qty_delivered_at_date` and `qty_invoiced_at_date`; handles perpetual stock valuation with separate `expense_account` and `stock_variation_account` entries (lines 247–311).
- Analytic distribution is aggregated by ratio of `price_total / total` for the global counterpart line (lines 321–328).
- Tax-inclusive price handling: if `order_line.tax_ids` contains price-inclusive taxes, uses `tax_ids.compute_all()` to get `total_excluded` (lines 197–205).
- `_get_product_expense_and_stock_var_accounts` returns `(False, False)` in base module — hook for inventory module override (lines 402–404).
- `create_entries`: validates `reversal_date > date`, calls `_compute_move_vals()`, creates and posts the move, then creates and posts the reversal with `_reverse_moves()` with a custom ref and the `reversal_date` (lines 378–400).
- Returns a window action on `account.move` filtered to both the accrual and reversal moves (lines 394–400).
- Cross-company guard: raises UserError if orders span multiple companies (line 147–148); and if orders use different currencies (lines 149–150).

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| 1 | Data lifecycle | Creates two moves (accrual + reversal) both posted in single `create_entries` call (lines 384–391) |
| 2 | State machine | No state on wizard; both created moves immediately posted |
| 3 | Computation engine | Quantity delta (delivered vs invoiced) × price unit; price-diff for perpetual valuation; day-weighted analytic distribution (lines 109–356) |
| 4 | Access control / security | `_check_company_auto = True`; single-company guard (line 147) |
| 5 | Integration / external | Reads `order_line.amount_to_invoice_at_date`, `qty_invoiced_at_date`, `qty_received_at_date`, `qty_delivered_at_date` from sale/purchase models; posts message to order via `order.message_post` (line 393) |
| 6 | Error handling / constraints | UserError for multi-company (line 148), multi-currency (line 150), reversal date not posterior (line 381) |
| 7 | Configuration / parametrisation | `account_id` domain dynamically switches between `liability_current` (purchase) and `asset_current` (sale) via context (lines 52–54); optional `amount` override for single-order custom accrual (lines 158–164) |
| 8 | Localisation / l10n hooks | Currency multi-currency support: amount_currency set when `order.currency_id != company.currency_id` (lines 124–128) |
| 9 | Automation / scheduling | None on wizard itself; RT: can be triggered by scheduled action targeting the wizard |
| 10 | Extension / override surface | `_get_product_expense_and_stock_var_accounts` is the stock module hook returning `(False, False)` in base (line 402–404); `_compute_move_vals` overridable |

---

## CAP-U47-05 Account Move Reversal Wizard

### D1 Business purpose and process semantics
The reversal wizard (`account.move.reversal`) creates a credit note or reversing journal entry for one or more posted moves. Supports two modes: `refund_moves` (simple reversal, leaving original open) and `modify_moves` (reversal + new copy with same content for amendment). Validates that all moves belong to a single company.

### D2 Architecture, data and object relationships
`_name = 'account.move.reversal'`, `_check_company_auto = True` (lines 8–13). Fields: `move_ids` (M2M to `account.move`, domain `state='posted'`), `new_move_ids` (M2M to `account.move`, result), `date`, `reason`, `journal_id`, `company_id`, `available_journal_ids`, `residual`, `currency_id`, `move_type`.

### D3 Source, technical and workflow logic
- `default_get` validates all moves are posted and single-company (lines 67–82).
- `_compute_available_journal_ids` restricts to journals of same type as original moves (lines 47–58).
- `_check_journal_type` constraint ensures selected journal matches move journal type (lines 60–64).
- `_prepare_default_reversal` builds reversal defaults: sets `auto_post='at_date'` when reversal date is in future, else `'no'` (line 106); handles `invoice_payment_term_id` for mixed early-pay discount computation (line 94).
- `reverse_moves` batches moves into two groups: those needing cancel (immediate reversal for non-auto-post entries) and others (lines 122–131). Calls `_reverse_moves(cancel=is_cancel_needed)`.
- In `modify_moves` mode: copies move data using `move.copy_data(include_business_fields=True)`, keeps only `product/line_section/line_subsection/line_note` lines, creates new move (lines 143–151).
- Logs message on original moves via `_message_log_batch` linking to the reversal (lines 138–140).
- Vendor bill copy in modify mode: copies `message_main_attachment_id` for inbound moves (lines 188–194).
- Returns window action to `account.move`, with `default_move_type` context key when all reversed moves share same type (lines 164–174).

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| 1 | Data lifecycle | TransientModel; original moves marked with log; new_move_ids stored on wizard |
| 2 | State machine | Requires `state='posted'` on input (line 15); `auto_post` set based on future date (line 106) |
| 3 | Computation engine | `_prepare_default_reversal` per-move defaults; batching by `is_cancel_needed` (lines 122–131) |
| 4 | Access control / security | `_check_company_auto = True`; single-company check in default_get (line 71) |
| 5 | Integration / external | Vendor bill attachment copy via `message_main_attachment_id.copy` (line 190) |
| 6 | Error handling / constraints | UserError: multi-company (line 72), non-posted moves (line 74–77); journal type constraint (lines 60–64) |
| 7 | Configuration / parametrisation | `is_modify` flag toggles between pure reversal and reversal+amendment (line 110, 176–180) |
| 8 | Localisation / l10n hooks | `country_code` from `company_id.country_id.code` (line 31) |
| 9 | Automation / scheduling | None |
| 10 | Extension / override surface | `_prepare_default_reversal` (line 92), `_modify_default_reverse_values` (line 182) |

---

## CAP-U47-06 Partial Reconcile Model and Tax Cash Basis Engine

### D1 Business purpose and process semantics
`account.partial.reconcile` records each individual match between a debit and a credit journal item. When all items in a group are fully matched, a `account.full.reconcile` record is created. On creation of each partial, the engine checks if tax cash-basis journal entries need to be created (for `tax_exigibility='on_payment'` taxes). On unlink, reversal moves are created for any CABA and exchange-difference entries.

### D2 Architecture, data and object relationships
`_name = 'account.partial.reconcile'` (line 10). Fields: `debit_move_id` (Many2one to `account.move.line`, indexed), `credit_move_id` (idem), `full_reconcile_id` (Many2one to `account.full.reconcile`, `btree_not_null` index), `exchange_move_id`, `draft_caba_move_vals` (Json), `amount` (company currency), `debit_amount_currency`, `credit_amount_currency`, `max_date` (computed, max of debit/credit dates), `company_id` (computed from invoice-side).

### D3 Source, technical and workflow logic
- `create` calls `_get_to_update_payments(from_state='in_process').state = 'paid'` then `_update_matching_number` (lines 157–161).
- `unlink` reverses CABA moves and exchange-diff moves; removes `full_reconcile_id`; resets payment state to `'in_process'` (lines 105–154).
- `_update_matching_number` implements a union-find graph algorithm: builds `number2lines` and `line2number` dicts by iterating partials sorted by id; merges graphs; bulk-updates `matching_number` on `account_move_line` via `execute_values` with pattern `'P' || source.number` for partial matches, or the `full_reconcile_id` for full matches (lines 193–238).
- `_collect_tax_cash_basis_values` determines `percentage` of payment (line 320–327): uses company currency if move currency is company currency, else foreign currency; handles case where both sides are invoices (rate from source line, not counterpart) (lines 302–308).
- `_create_tax_cash_basis_moves` creates CABA journal entries: groups lines by `_get_cash_basis_base_line_grouping_key_from_vals` / `_get_cash_basis_tax_line_grouping_key_from_vals` to aggregate small amounts; posts only when both source moves are posted (lines 534–713).
- CABA moves are created `skip_invoice_sync=True, skip_invoice_line_sync=True, skip_account_move_synchronization=True` (line 685–688).
- After CABA moves creation, tax lines on reconcilable accounts are reconciled via `_reconcile_plan` with context `add_caba_vals=True` (line 712).
- Lock date: CABA move date is `max(settlement_date, lock_date + 1 day)` (line 554).
- `forced_rate_from_register_payment` context key overrides payment rate for exchange diff (line 332–333).
- `_get_to_update_payments`: changes payment state `'in_process' → 'paid'` when partial amount matches full payment amount, handling group payments specially (lines 163–191).

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| 1 | Data lifecycle | Created on reconcile; `full_reconcile_id` set when complete; unlinked on un-reconcile with CABA reversal |
| 2 | State machine | Payment state transitions `in_process→paid` (on create) and `paid→in_process` (on unlink) (lines 153, 159) |
| 3 | Computation engine | Union-find matching number algorithm (lines 193–238); CABA percentage by currency (lines 314–327); day-weighted grouping for CABA aggregation |
| 4 | Access control / security | `company_id` computed from invoice-side (lines 96–99) |
| 5 | Integration / external | Links to `account.move` for CABA entries via `tax_cash_basis_rec_id` (line 565); `exchange_move_id` (line 24); lock-date check (line 553) |
| 6 | Error handling / constraints | `UserError` if no `tax_cash_basis_journal_id` on company (lines 276–279); `ValidationError` for missing currencies (lines 74–78) |
| 7 | Configuration / parametrisation | `tax_exigibility='on_payment'` on tax drives CABA creation (line 376); `draft_caba_move_vals` JSON stores snapshot for draft CABA detection |
| 8 | Localisation / l10n hooks | Reversal date respects lock dates (lines 141–147) |
| 9 | Automation / scheduling | None directly |
| 10 | Extension / override surface | `_prepare_cash_basis_base_line_vals` (line 365), `_prepare_cash_basis_tax_line_vals` (line 418), `_prepare_cash_basis_counterpart_base_line_vals` (line 397), `_prepare_cash_basis_counterpart_tax_line_vals` (line 449) |

---

## CAP-U47-07 Full Reconcile Model

### D1 Business purpose and process semantics
`account.full.reconcile` marks the completion of a reconciliation group — all involved journal items are fully matched. It stores the set of matched items and partial reconciles. On creation, it bulk-updates `full_reconcile_id` and `matching_number` on all related journal items via direct SQL for performance.

### D2 Architecture, data and object relationships
`_name = 'account.full.reconcile'` (line 5). Fields: `partial_reconcile_ids` (One2many to `account.partial.reconcile`), `reconciled_line_ids` (One2many to `account.move.line`).

### D3 Source, technical and workflow logic
- `create` extracts `reconciled_line_ids` and `partial_reconcile_ids` from Command lists, runs the base create without those fields, then bulk-updates via two `execute_values` calls (lines 22–44).
- After bulk update, calls `account.partial.reconcile._update_matching_number(fulls.reconciled_line_ids)` to set matching numbers (line 44).
- `unlink` captures `reconciled_line_ids` before unlink, then calls `_update_matching_number(amls.exists())` so surviving AMls get `'P<n>'` partial numbers instead of the now-invalid full reconcile id (lines 47–60).
- Uses `tracking_disable=True` context on super create to avoid mail tracking overhead (line 24).

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| 1 | Data lifecycle | Created when reconciliation is complete; unlinked on un-reconcile |
| 2 | State machine | Existence indicates full reconciliation; unlink reverts to partial matching numbers |
| 3 | Computation engine | Bulk SQL UPDATE via `execute_values` (lines 26–41) for performance at scale |
| 4 | Access control / security | None specific |
| 5 | Integration / external | Linked to `account.move.line.full_reconcile_id` (FK, ondelete set null); `account.partial.reconcile.full_reconcile_id` |
| 6 | Error handling / constraints | None specific; ValueError on unexpected Command (line 21) |
| 7 | Configuration / parametrisation | None |
| 8 | Localisation / l10n hooks | None |
| 9 | Automation / scheduling | None |
| 10 | Extension / override surface | create/unlink methods are the override points |

---

## CAP-U47-08 Reconcile Model (Bank Statement Matching Rules)

### D1 Business purpose and process semantics
`account.reconcile.model` defines named rules that the bank reconciliation screen uses to automatically suggest or reconcile counterpart journal entries. Rules have conditions (amount range, label matching, partner filter, journal filter) and one or more counterpart line templates with configurable amounts (fixed, percentage, regex-extracted).

### D2 Architecture, data and object relationships
`_name = 'account.reconcile.model'`, `_inherit = ['mail.thread']`, `_order = 'sequence, id'` (lines 94–99). `AccountReconcileModelLine` `_name = 'account.reconcile.model.line'`, `_inherit = ['analytic.mixin']` (lines 8–13). Line fields: `amount_type` (fixed/percentage/percentage_st_line/regex), `amount_string` (raw input), `amount` (computed Float), `account_id`, `partner_id`, `label`, `tax_ids`.

### D3 Source, technical and workflow logic
- `trigger` field: `'manual'` (suggest only) vs `'auto_reconcile'` (automatically complete reconciliation) (line 110).
- `_compute_can_be_proposed`: True when not a partner-mapping rule AND has at least one condition (label/amount/partner/auto) (lines 161–164).
- `_compute_partner_mapping`: detects single-line rules with partner but no account as partner mapping rules (lines 166–170).
- `_compute_float_amount`: parses `amount_string` to float, defaults to 0 on ValueError (lines 70–76).
- `_validate_amount` constraint: enforces non-zero for fixed/percentage types; validates regex syntax (lines 78–92).
- `action_reconcile_stat`: raw SQL `SELECT ARRAY_AGG(DISTINCT move_id) FROM account_move_line WHERE reconcile_model_id = %s` to find all moves created by this model (lines 178–191).
- Amount types: `percentage` = % of residual balance, `percentage_st_line` = % of statement line amount, `regex` = regex capture group from transaction label.

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| 1 | Data lifecycle | Persistent configuration; archivable via `active` field (line 102) |
| 2 | State machine | `trigger` selection: `manual` vs `auto_reconcile` (line 110) |
| 3 | Computation engine | `amount_type` drives amount computation in reconcile engine (RT: bank_statement reconciliation logic) |
| 4 | Access control / security | `_check_company_auto = True`; `company_id` readonly on model (line 107) |
| 5 | Integration / external | `analytic.mixin` inherited on line model (line 10); `reconcile_model_id` FK on `account.move.line` (referenced in SQL line 184) |
| 6 | Error handling / constraints | `_validate_amount` for non-zero and valid regex (lines 78–92); `_check_match_label_param` for regex validity (lines 152–159) |
| 7 | Configuration / parametrisation | `match_journal_ids` filter (line 126); `match_amount` with min/max (lines 130–137); `match_label` with contains/not_contains/regex (lines 138–146); `match_partner_ids` (line 147) |
| 8 | Localisation / l10n hooks | None directly |
| 9 | Automation / scheduling | `trigger='auto_reconcile'` enables auto-reconcile during bank statement processing (RT) |
| 10 | Extension / override surface | `line_ids` is copy=True enabling duplication; `copy_data` ensures unique names with "(copy)" suffix logic (lines 193–202) |

---

## CAP-U47-09 Payment Terms Model

### D1 Business purpose and process semantics
`account.payment.term` defines the schedule of payment installments for invoices: how the total is split across due dates (by percentage or fixed amount), with optional early payment discount. This drives the `invoice_date_due` field on invoices and the creation of payment-term journal items.

### D2 Architecture, data and object relationships
`_name = 'account.payment.term'`, `_order = 'sequence, id'` (lines 11–14). `AccountPaymentTermLine` defines individual installments: `value` (percent/fixed), `value_amount`, `delay_type` (days_after / days_after_end_of_month / days_after_end_of_next_month / days_end_of_month_on_the), `nb_days`, `days_next_month`. Header fields: `early_discount` (Boolean), `discount_percentage` (Float, default 2.0), `discount_days` (Integer, default 10), `early_pay_discount_computation` (included/excluded/mixed).

### D3 Source, technical and workflow logic
- `_compute_discount_computation` sets country-specific defaults: Belgium → 'mixed', Netherlands → 'excluded', all others → 'included' (lines 82–90).
- `_check_lines` constraint: percentages must sum to 100% (using `Payment Terms` decimal precision); early discount only allowed with single 100% line (lines 156–169).
- `_compute_terms` is the main computation method: builds a `pay_term` dict with `line_ids` list of `{date, company_amount, foreign_amount}`. The last line always gets the residual balance (lines 228–229). Uses `rate = abs(total_amount_currency / total_amount)` for currency conversion (line 190).
- Early discount balance for `excluded/mixed`: `total_amount - untaxed_amount * percentage` (tax part kept); for `included`: `total_amount * (1 - percentage)` (all discounted) (lines 203–208).
- `_get_due_date` on line model: implements all four delay types using `dateutil.relativedelta` (lines 310–327).
- `days_end_of_month_on_the` logic: `due_date + relativedelta(days=nb_days) + relativedelta(months=1, day=days_next_month)` (line 326).
- `_unlink_except_referenced_terms`: blocks deletion when referenced by any `account.move` (lines 258–261).
- Cash rounding integration in `_compute_terms`: applies `cash_rounding.compute_difference()` to each non-balance line, balance line inherits correct cash-rounded residual (lines 242–254).

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| 1 | Data lifecycle | Persistent; archived not deleted if referenced (line 258–261) |
| 2 | State machine | N/A — configuration model |
| 3 | Computation engine | `_compute_terms`: residual-tracking percentage/fixed split with cash-rounding correction (lines 171–256) |
| 4 | Access control / security | `_check_company_domain = models.check_company_domain_parent_of` (line 15) |
| 5 | Integration / external | Cash rounding via `account.cash.rounding.compute_difference()` in `_compute_terms` and `_get_amount_due_after_discount` (lines 74–77, 242–250) |
| 6 | Error handling / constraints | `ValidationError` for percent sum != 100, multi-line with early discount, non-positive discount values (lines 156–169); `days_next_month` must be 0–31 (lines 332–336) |
| 7 | Configuration / parametrisation | `early_pay_discount_computation` has country defaults (BE=mixed, NL=excluded, else=included) (lines 82–90) |
| 8 | Localisation / l10n hooks | `fiscal_country_codes` computed from allowed companies (line 52–53); discount computation country rules (lines 82–90) |
| 9 | Automation / scheduling | None |
| 10 | Extension / override surface | `_compute_terms` is the primary override point for custom installment logic |

---

## CAP-U47-10 Cash Rounding Model

### D1 Business purpose and process semantics
`account.cash.rounding` supports countries where the smallest circulating coin is larger than the currency's decimal unit (e.g., Switzerland rounds to 0.05 CHF). It computes a rounding adjustment for invoice totals using one of two strategies: adding a separate rounding line to the invoice, or modifying the largest tax amount.

### D2 Architecture, data and object relationships
`_name = 'account.cash.rounding'`, `_check_company_auto = True` (lines 8–17). Fields: `rounding` (Float, required), `strategy` ('biggest_tax'/'add_invoice_line'), `profit_account_id` (Many2one, company_dependent), `loss_account_id` (Many2one, company_dependent), `rounding_method` ('UP'/'DOWN'/'HALF-UP', default 'HALF-UP').

### D3 Source, technical and workflow logic
- `round(amount)`: calls `float_round(amount, precision_rounding=self.rounding, rounding_method=self.rounding_method)` (lines 51–57).
- `compute_difference(currency, amount)`: first rounds amount to currency precision, then `self.round(amount) - amount`, then rounds to currency again (lines 59–69). This gives the rounding delta to add/subtract.
- `validate_rounding` constraint: `rounding > 0` required (lines 45–49).
- `profit_account_id` and `loss_account_id` are `company_dependent=True`, meaning each company can configure different accounts (lines 25–39).

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| 1 | Data lifecycle | Persistent configuration |
| 2 | State machine | N/A |
| 3 | Computation engine | `round()` uses `float_round` with configurable method (line 57); `compute_difference` returns currency-rounded delta (line 69) |
| 4 | Access control / security | `_check_company_auto = True`; `profit_account_id`/`loss_account_id` check_company=True (lines 28, 34) |
| 5 | Integration / external | Called from `account.payment.term._compute_terms` (lines 242–250 of payment_term.py) and `_get_amount_due_after_discount` |
| 6 | Error handling / constraints | `ValidationError` if `rounding <= 0` (lines 45–49) |
| 7 | Configuration / parametrisation | Three rounding methods: UP, DOWN, HALF-UP (line 42–43); company-dependent profit/loss accounts |
| 8 | Localisation / l10n hooks | Designed for countries with coinage gap (e.g., CH 0.05, SE 0.50) |
| 9 | Automation / scheduling | None |
| 10 | Extension / override surface | `round()` and `compute_difference()` are utility methods that can be overridden |

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U47-C001 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:13 | `_inherits = {'account.move': 'move_id'}` | FACT | always | — | AccountBankStatementLine delegates its journal entry storage to account.move via _inherits | N-U47-001 |
| VDR-U47-C002 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:151 | `_unreconciled_idx = models.Index("(journal_id, company_id, internal_index) WHERE is_reconciled IS NOT TRUE")` | FACT | always | — | Partial index on unreconciled lines covers (journal_id, company_id, internal_index) | N-U47-001 |
| VDR-U47-C003 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:390 | `vals['move_type'] = 'entry'` | FACT | always | — | move_type is forced to 'entry' on every bank statement line create | N-U47-001 |
| VDR-U47-C004 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:420 | `st_lines.move_id.action_post()` | FACT | always | — | The linked account.move is automatically posted on statement line creation | N-U47-001 |
| VDR-U47-C005 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:278 | `st_line.internal_index = f'{st_line.date.strftime("%Y%m%d")}'` | FACT | always | — | internal_index encodes date as YYYYMMDD prefix | N-U47-001 |
| VDR-U47-C006 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:279 | `f'{MAXINT - st_line.sequence:0>10}'` | FACT | always | — | internal_index uses MAXINT(2147483647) minus sequence for reverse ordering, zero-padded to 10 digits | N-U47-001 |
| VDR-U47-C007 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:280 | `f'{st_line._origin.id:0>10}'` | FACT | always | — | internal_index appends the record ID zero-padded to 10 digits as the third component | N-U47-001 |
| VDR-U47-C008 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:637 | `counterpart_account_id = self.journal_id.suspense_account_id.id` | FACT | when counterpart_account_id not supplied | — | Default counterpart for new statement lines is the journal's suspense account | N-U47-002 |
| VDR-U47-C009 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:639 | `raise UserError(_(` | FACT | when suspense_account_id not set on journal | — | UserError raised if journal has no suspense account and no explicit counterpart_account_id | N-U47-002 |
| VDR-U47-C010 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:698 | `if line.account_id == self.journal_id.default_account_id:` | FACT | always | — | _seek_for_lines classifies move lines as liquidity when they match journal.default_account_id | N-U47-002 |
| VDR-U47-C011 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:700 | `elif line.account_id == self.journal_id.suspense_account_id:` | FACT | always | — | _seek_for_lines classifies lines as suspense when they match journal.suspense_account_id | N-U47-002 |
| VDR-U47-C012 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:705 | `liquidity_lines = self.move_id.line_ids.filtered(lambda l: l.account_id.account_type in ('asset_cash', 'liability_credit_card'))` | FACT | when no default_account_id match | — | Fallback liquidity detection uses account_type in ('asset_cash','liability_credit_card') | N-U47-002 |
| VDR-U47-C013 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:460 | `def action_undo_reconciliation(self):` | FACT | always | — | action_undo_reconciliation removes all reconciliations and auto-generated payments from a statement line | N-U47-002 |
| VDR-U47-C014 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:465 | `if st_line.checked and st_line.is_reconciled and not st_line.move_id._is_user_able_to_review():` | FACT | when checked+reconciled | C1 | ValidationError raised when non-accountant user tries to undo reconciliation on a validated entry | N-U47-002 |
| VDR-U47-C015 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:484 | `if self.statement_id.filtered(lambda stmt: stmt.is_valid and stmt.is_complete):` | FACT | always | — | Deletion blocked when parent statement is both valid and complete | N-U47-002 |
| VDR-U47-C016 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:432 | `tracked_lines = self.filtered(lambda stl: stl.company_id.restrictive_audit_trail)` | FACT | when restrictive_audit_trail=True | C1 | For audit-trail companies, the linked move is cancelled before the statement line is deleted | N-U47-002 |
| VDR-U47-C017 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:717 | `if self.env.context.get('skip_account_move_synchronization'):` | FACT | always | — | Both sync methods guard against infinite loops using skip_account_move_synchronization context key | N-U47-002 |
| VDR-U47-C018 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:492 | `str2bool(self.env['ir.config_parameter'].sudo().get_param("account.skip_create_bank_account_on_reconcile"))` | FACT | when account_number set | — | System parameter account.skip_create_bank_account_on_reconcile prevents auto-creation of partner bank accounts | N-U47-003 |
| VDR-U47-C019 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:506 | `all_reconcilable_account_ids = self.env['account.account'].sudo().search([` | FACT | always | — | _get_default_amls_matching_domain searches reconcilable accounts across the root company hierarchy | N-U47-002 |
| VDR-U47-C020 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:526 | ('account_id.account_type | FACT | always | — | AML matching domain excludes AR/AP lines that already have a linked payment | N-U47-002 |
| VDR-U47-C021 | FUNC-U47-F002 | account/models/res_currency.py:10 | `_inherit = 'res.currency'` | FACT | always | — | res.currency is extended by the account module to add currency table generation for reporting | N-U47-004 |
| VDR-U47-C022 | FUNC-U47-F002 | account/models/res_currency.py:30 | `if (rounding_val > record.rounding or rounding_val == 0) and record._has_accounting_entries():` | FACT | when rounding written | C1 | Writing a smaller rounding (more decimal places) or zero is blocked if accounting entries exist | N-U47-004 |
| VDR-U47-C023 | FUNC-U47-F002 | account/models/res_currency.py:58 | `return len(companies.currency_id) == 1` | FACT | always | — | Monocurrency optimization: single-currency company set bypasses temp table creation | N-U47-004 |
| VDR-U47-C024 | FUNC-U47-F002 | account/models/res_currency.py:68 | `SQL("(%(company_id)s, CAST(NULL AS VARCHAR), CAST(NULL AS DATE), CAST(NULL AS DATE), %(rate_type)s, 1)"` | FACT | monocurrency | — | Monocurrency table uses rate=1 for all companies inline as VALUES clause | N-U47-004 |
| VDR-U47-C025 | FUNC-U47-F002 | account/models/res_currency.py:131 | ON COMMIT DROP | FACT | multi-currency | — | Currency conversion table is a TEMPORARY TABLE created ON COMMIT DROP | N-U47-004 |
| VDR-U47-C026 | FUNC-U47-F002 | account/models/res_currency.py:136 | `CREATE INDEX account_currency_table_index ON account_currency_table (company_id, rate_type, date_from, date_next)` | FACT | multi-currency | — | Supporting index created immediately after temp table for query planner | N-U47-004 |
| VDR-U47-C027 | FUNC-U47-F002 | account/models/res_currency.py:175 | CASE WHEN rate.id | FACT | always | — | Three rate_type values: 'current', 'historical', 'average' in the currency table | N-U47-004 |
| VDR-U47-C028 | FUNC-U47-F002 | account/models/res_currency.py:168 | `SELECT DISTINCT ON (other_company.id)` | FACT | always | — | Current rate query uses DISTINCT ON to pick the most recent rate per company | N-U47-004 |
| VDR-U47-C029 | FUNC-U47-F002 | account/models/res_currency.py:207 | ON rate.currency_id = other_company.currency_id | FACT | use_cta_rates=True | — | Historical rates use a LATERAL join to find the domestic rate effective at each foreign rate's date | N-U47-004 |
| VDR-U47-C030 | FUNC-U47-F002 | account/models/res_currency.py:269 | `LEAD(breakpoint.date) OVER (PARTITION BY other_company.id ORDER BY breakpoint.date) AS next_date` | FACT | average rate | — | Average rate uses LEAD window function to find segment end-dates from breakpoint dates | N-U47-004 |
| VDR-U47-C031 | FUNC-U47-F002 | account/models/res_currency.py:250 | SUM(rate_with_days.domestic_rate | FACT | average rate | — | Day-weighted average rate is computed as sum(rate × days) / sum(days) | N-U47-004 |
| VDR-U47-C032 | FUNC-U47-F003 | account/wizard/account_payment_register.py:13 | `_name = 'account.payment.register'` | FACT | always | — | Payment register is a TransientModel named account.payment.register | N-U47-005 |
| VDR-U47-C033 | FUNC-U47-F003 | account/wizard/account_payment_register.py:63 | installments_mode = fields.Selection | FACT | always | — | Four installments modes: next, overdue, before_date, full | N-U47-005 |
| VDR-U47-C034 | FUNC-U47-F003 | account/wizard/account_payment_register.py:344 | `if len(lines.company_id.root_id) > 1:` | FACT | always | C1 | UserError raised if lines span multiple root companies | N-U47-005 |
| VDR-U47-C035 | FUNC-U47-F003 | account/wizard/account_payment_register.py:349 | `batches = defaultdict(lambda: {'lines': self.env['account.move.line']})` | FACT | always | — | Batches initialized as defaultdict keyed by frozendict of batch attributes | N-U47-005 |
| VDR-U47-C036 | FUNC-U47-F003 | account/wizard/account_payment_register.py:371 | merge = | FACT | multi-batch | — | Inbound and outbound batches for the same partner are merged when each direction has only one unique bank account | N-U47-005 |
| VDR-U47-C037 | FUNC-U47-F003 | account/wizard/account_payment_register.py:975 | `raise UserError(_("There's nothing left to pay` | FACT | always | — | UserError raised in default_get when no lines have residual amounts | N-U47-005 |
| VDR-U47-C038 | FUNC-U47-F003 | account/wizard/account_payment_register.py:980 | `if len(set(available_lines.mapped('account_type'))) > 1:` | FACT | always | C1 | Mixed inbound/outbound account types in same wizard call raise UserError | N-U47-005 |
| VDR-U47-C039 | FUNC-U47-F003 | account/wizard/account_payment_register.py:982 | `if any(move.payment_state == 'blocked' for move in available_lines.move_id):` | FACT | always | C1 | Blocked invoices (payment_state='blocked') raise UserError in default_get | N-U47-005 |
| VDR-U47-C040 | FUNC-U47-F003 | account/wizard/account_payment_register.py:1235 | `edit_mode = self.can_edit_wizard and (len(first_batch_result['lines']) == 1 or self.group_payment)` | FACT | always | — | Edit mode requires can_edit_wizard AND (single line OR group_payment enabled) | N-U47-005 |
| VDR-U47-C041 | FUNC-U47-F003 | account/wizard/account_payment_register.py:1122 | payments = self.env['account.payment'] | FACT | always | — | Payment creation uses skip_invoice_sync=True context to avoid triggering invoice sync | N-U47-005 |
| VDR-U47-C042 | FUNC-U47-F003 | account/wizard/account_payment_register.py:1185 | `payments.with_context(skip_sale_auto_invoice_send=True).action_post()` | FACT | always | — | Post payments suppresses automatic sale invoice sending via skip_sale_auto_invoice_send=True | N-U47-005 |
| VDR-U47-C043 | FUNC-U47-F003 | account/wizard/account_payment_register.py:1206 | `extra_context = {'forced_rate_from_register_payment': vals['rate']} if 'rate' in vals else {}` | FACT | exchange account | — | Exchange difference reconciliation uses forced_rate_from_register_payment context to override rate | N-U47-005 |
| VDR-U47-C044 | FUNC-U47-F003 | account/wizard/account_payment_register.py:1216 | `lines.move_id.matched_payment_ids = [Command.link(payment.id)]` | FACT | always | — | After reconciliation, payment is linked to source move via matched_payment_ids | N-U47-005 |
| VDR-U47-C045 | FUNC-U47-F003 | account/wizard/account_payment_register.py:1248 | `total_batch_residual = sum(first_batch_result['lines'].mapped('amount_residual_currency'))` | FACT | writeoff_is_exchange_account | — | Exchange difference rate computed as abs(total_residual_currency / amount) | N-U47-005 |
| VDR-U47-C046 | FUNC-U47-F003 | account/wizard/account_payment_register.py:878 | if pay.partner_bank_id | FACT | QR code | — | QR code generation requires partner_bank_id.allow_out_payment=True | N-U47-006 |
| VDR-U47-C047 | FUNC-U47-F003 | account/wizard/account_payment_register.py:882 | `and pay.payment_method_line_id.code == 'manual'` | FACT | QR code | — | QR code only generated for manual payment method | N-U47-006 |
| VDR-U47-C048 | FUNC-U47-F003 | account/wizard/account_payment_register.py:493 | `wizard.currency_id = wizard.journal_id.currency_id or wizard.source_currency_id or wizard.company_id.currency_id` | FACT | always | — | Wizard currency falls back: journal currency → source currency → company currency | N-U47-005 |
| VDR-U47-C049 | FUNC-U47-F003 | account/wizard/account_payment_register.py:314 | return len(lines.company_id) | FACT | multi-branch | — | Sibling-company detection triggers sudo mode for payment creation | N-U47-005 |
| VDR-U47-C050 | FUNC-U47-F003 | account/wizard/account_payment_register.py:1309 | `if self.is_register_payment_on_draft:` | FACT | draft invoices | — | For draft invoice payments, payment_difference_handling is forced to 'open' | N-U47-005 |
| VDR-U47-C051 | FUNC-U47-F004 | account/wizard/accrued_orders.py:12 | `_name = 'account.accrued.orders.wizard'` | FACT | always | — | Accrued orders wizard is account.accrued.orders.wizard TransientModel | N-U47-007 |
| VDR-U47-C052 | FUNC-U47-F004 | account/wizard/accrued_orders.py:24 | `return date_utils.get_month(fields.Date.context_today(self))[0] - relativedelta(days=1)` | FACT | always | — | Default accrual date is the last day of the previous month | N-U47-007 |
| VDR-U47-C053 | FUNC-U47-F004 | account/wizard/accrued_orders.py:67 | `if record.date and (not record.reversal_date or record.reversal_date <= record.date):` | FACT | always | — | reversal_date auto-sets to date+1 day when not explicitly set or when set before date | N-U47-007 |
| VDR-U47-C054 | FUNC-U47-F004 | account/wizard/accrued_orders.py:145 | `is_purchase = orders._name == 'purchase.order'` | FACT | always | — | is_purchase determined by model name being 'purchase.order' | N-U47-007 |
| VDR-U47-C055 | FUNC-U47-F004 | account/wizard/accrued_orders.py:147 | `if orders.filtered(lambda o: o.company_id != self.company_id):` | FACT | always | C1 | Cross-company accrual entries raise UserError | N-U47-007 |
| VDR-U47-C056 | FUNC-U47-F004 | account/wizard/accrued_orders.py:149 | `if orders.currency_id and len(orders.currency_id) > 1:` | FACT | always | C1 | Multi-currency order selection raises UserError | N-U47-007 |
| VDR-U47-C057 | FUNC-U47-F004 | account/wizard/accrued_orders.py:185 | `quantity_to_invoice = order_line.qty_invoiced_at_date - order_line.qty_received_at_date` | FACT | purchase | — | Purchase accrual quantity = invoiced_at_date minus received_at_date | N-U47-007 |
| VDR-U47-C058 | FUNC-U47-F004 | account/wizard/accrued_orders.py:248 | `qty_to_invoice = order_line.qty_delivered_at_date - order_line.qty_invoiced_at_date` | FACT | sale | — | Sale accrual quantity = delivered_at_date minus invoiced_at_date | N-U47-007 |
| VDR-U47-C059 | FUNC-U47-F004 | account/wizard/accrued_orders.py:318 | `if not self.company_id.currency_id.is_zero(total_balance):` | FACT | always | — | Global counterpart line created only when total_balance is non-zero | N-U47-007 |
| VDR-U47-C060 | FUNC-U47-F004 | account/wizard/accrued_orders.py:381 | `if self.reversal_date <= self.date:` | FACT | always | — | UserError raised in create_entries if reversal_date is not strictly after date | N-U47-007 |
| VDR-U47-C061 | FUNC-U47-F004 | account/wizard/accrued_orders.py:384 | `move = self.env['account.move'].create(move_vals)` | FACT | always | — | Accrual move created then posted with _post() | N-U47-007 |
| VDR-U47-C062 | FUNC-U47-F004 | account/wizard/accrued_orders.py:386 | reverse_move = move._reverse_moves | FACT | always | — | Reversal move created via move._reverse_moves with the reversal_date | N-U47-007 |
| VDR-U47-C063 | FUNC-U47-F004 | account/wizard/accrued_orders.py:402 | `def _get_product_expense_and_stock_var_accounts(self, product):` | FACT | always | — | Base module returns (False, False) from _get_product_expense_and_stock_var_accounts; hook for stock module | N-U47-007 |
| VDR-U47-C064 | FUNC-U47-F004 | account/wizard/accrued_orders.py:197 | `qty_to_invoice = order_line._get_qty_to_invoice_at_date()` | FACT | purchase, tax-inclusive | — | Tax-inclusive price lines use _get_qty_to_invoice_at_date and compute_all for price_subtotal | N-U47-007 |
| VDR-U47-C065 | FUNC-U47-F005 | account/wizard/account_move_reversal.py:7 | class AccountMoveReversal(models.TransientModel) | FACT | always | — | Reversal wizard model name is account.move.reversal | N-U47-008 |
| VDR-U47-C066 | FUNC-U47-F005 | account/wizard/account_move_reversal.py:15 | `move_ids = fields.Many2many('account.move', 'account_move_reversal_move', 'reversal_id', 'move_id', domain=[('state', '=', 'posted')])` | FACT | always | — | Only posted moves can be reversed; domain enforced at field level | N-U47-008 |
| VDR-U47-C067 | FUNC-U47-F005 | account/wizard/account_move_reversal.py:60 | `@api.constrains('journal_id', 'move_ids')` | FACT | always | — | Constraint ensures selected journal type matches the reversed entry's journal type | N-U47-008 |
| VDR-U47-C068 | FUNC-U47-F005 | account/wizard/account_move_reversal.py:94 | `mixed_payment_term = move.invoice_payment_term_id.id if move.invoice_payment_term_id.early_pay_discount_computation == 'mixed' else None` | FACT | reversal | — | Mixed early-pay discount payment terms are preserved on reversal | N-U47-008 |
| VDR-U47-C069 | FUNC-U47-F005 | account/wizard/account_move_reversal.py:106 | `'auto_post': 'at_date' if reverse_date > fields.Date.context_today(self) else 'no'` | FACT | future date | — | Reversal with future date sets auto_post='at_date' to post on that date | N-U47-008 |
| VDR-U47-C070 | FUNC-U47-F005 | account/wizard/account_move_reversal.py:127 | `is_cancel_needed = not is_auto_post and (is_modify or self.move_type == 'entry')` | FACT | always | — | Cancel (offsetting) of original move only when not auto_post AND (modify mode OR plain journal entry) | N-U47-008 |
| VDR-U47-C071 | FUNC-U47-F005 | account/wizard/account_move_reversal.py:146 | `data['line_ids'] = [line for line in data['line_ids'] if line[2]['display_type'] in ('product', 'line_section', 'line_subsection', 'line_note')]` | FACT | modify_moves | — | In modify mode, new copy only retains product/section/note lines from original | N-U47-008 |
| VDR-U47-C072 | FUNC-U47-F005 | account/wizard/account_move_reversal.py:138 | moves._message_log_batch | FACT | always | — | A message log entry linking to the reversal is posted on each original move | N-U47-008 |
| VDR-U47-C073 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:10 | `_name = 'account.partial.reconcile'` | FACT | always | — | Partial reconcile model records each individual debit-credit matching pair | N-U47-009 |
| VDR-U47-C074 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:24 | `exchange_move_id = fields.Many2one(comodel_name='account.move', index='btree_not_null')` | FACT | always | — | exchange_move_id on partial reconcile stores the exchange difference journal entry | N-U47-009 |
| VDR-U47-C075 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:64 | max_date = fields.Date | FACT | always | — | max_date stores the later of debit_move_id.date and credit_move_id.date | N-U47-009 |
| VDR-U47-C076 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:159 | `partials._get_to_update_payments(from_state='in_process').state = 'paid'` | FACT | on create | — | On partial reconcile creation, matching payments transition from in_process to paid state | N-U47-009 |
| VDR-U47-C077 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:153 | `to_update_payments.state = 'in_process'` | FACT | on unlink | — | On partial reconcile unlink, payments revert from paid to in_process state | N-U47-009 |
| VDR-U47-C078 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:227 | UPDATE account_move_line l | FACT | always | — | matching_number uses 'P' prefix for partial matches and the full_reconcile_id value for complete matches | N-U47-009 |
| VDR-U47-C079 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:274 | `journal = partial.company_id.tax_cash_basis_journal_id` | FACT | CABA | — | CABA entries use the company's tax_cash_basis_journal_id journal | N-U47-009 |
| VDR-U47-C080 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:276 | `if not journal:` | FACT | CABA | C1 | UserError if tax cash basis journal not configured on company | N-U47-009 |
| VDR-U47-C081 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:302 | `if partial.debit_move_id.move_id.is_invoice(include_receipts=True) and partial.credit_move_id.move_id.is_invoice(include_receipts=True):` | FACT | invoice-invoice reconcile | — | When reconciling two invoices (e.g., credit note vs invoice), rate from source line used, not counterpart | N-U47-009 |
| VDR-U47-C082 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:332 | `if 'forced_rate_from_register_payment' in self.env.context:` | FACT | exchange diff | — | forced_rate_from_register_payment context key overrides payment rate for CABA computation | N-U47-009 |
| VDR-U47-C083 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:554 | `move_date = max(partial_values['settlement_date'], lock_date + timedelta(days=1))` | FACT | CABA | — | CABA move date is max of settlement_date and lock_date+1 day | N-U47-009 |
| VDR-U47-C084 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:685 | moves = self.env['account.move'].with_context | FACT | CABA | — | CABA moves created with skip context keys to avoid sync side effects | N-U47-009 |
| VDR-U47-C085 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:690 | `moves[:len(moves_to_create_and_post)]._post(soft=False)` | FACT | CABA | — | Only CABA moves where both source moves are posted get auto-posted | N-U47-009 |
| VDR-U47-C086 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:200 | # By iterating | FACT | matching number | — | Union-find matching number algorithm processes partials in id order | N-U47-009 |
| VDR-U47-C087 | FUNC-U47-F007 | account/models/account_full_reconcile.py:5 | `_name = 'account.full.reconcile'` | FACT | always | — | Full reconcile model marks completion of a reconciliation group | N-U47-010 |
| VDR-U47-C088 | FUNC-U47-F007 | account/models/account_full_reconcile.py:26 | self.env.cr.execute_values | FACT | always | — | Full reconcile create uses bulk SQL execute_values instead of ORM for performance | N-U47-010 |
| VDR-U47-C089 | FUNC-U47-F007 | account/models/account_full_reconcile.py:24 | `super(AccountFullReconcile, self.with_context(tracking_disable=True)).create(vals_list)` | FACT | always | — | Full reconcile creation disables mail tracking to avoid overhead | N-U47-010 |
| VDR-U47-C090 | FUNC-U47-F007 | account/models/account_full_reconcile.py:55 | `amls = self.reconciled_line_ids` | FACT | unlink | — | On unlink, remaining reconciled lines have matching_number recalculated | N-U47-010 |
| VDR-U47-C091 | FUNC-U47-F008 | account/models/account_reconcile_model.py:94 | `_name = 'account.reconcile.model'` | FACT | always | — | Reconcile model is account.reconcile.model, inherits mail.thread for tracking | N-U47-011 |
| VDR-U47-C092 | FUNC-U47-F008 | account/models/account_reconcile_model.py:110 | `trigger = fields.Selection([('manual', 'Manual'), ('auto_reconcile', 'Automated')]` | FACT | always | — | Trigger field distinguishes manual suggestion from automated reconciliation | N-U47-011 |
| VDR-U47-C093 | FUNC-U47-F008 | account/models/account_reconcile_model.py:25 | amount_type = fields.Selection | FACT | always | — | Four amount computation types for reconcile model lines | N-U47-011 |
| VDR-U47-C094 | FUNC-U47-F008 | account/models/account_reconcile_model.py:161 | `model.can_be_proposed = not model.mapped_partner_id and (model.match_label or model.match_amount or model.match_partner_ids or model.trigger == 'auto_reconcile')` | FACT | always | — | can_be_proposed is False for pure partner-mapping rules or rules with no conditions | N-U47-011 |
| VDR-U47-C095 | FUNC-U47-F008 | account/models/account_reconcile_model.py:168 | `is_partner_mapping = model.match_label and len(model.line_ids) == 1 and model.line_ids[0].partner_id and not model.line_ids[0].account_id` | FACT | always | — | Partner mapping rules: single line with partner but no account, with label matching | N-U47-011 |
| VDR-U47-C096 | FUNC-U47-F008 | account/models/account_reconcile_model.py:184 | WHERE reconcile_model_id = %s | FACT | always | — | action_reconcile_stat retrieves distinct moves created by this model via raw SQL | N-U47-011 |
| VDR-U47-C097 | FUNC-U47-F009 | account/models/account_payment_term.py:11 | `_name = 'account.payment.term'` | FACT | always | — | Payment term model is account.payment.term | N-U47-012 |
| VDR-U47-C098 | FUNC-U47-F009 | account/models/account_payment_term.py:41 | early_pay_discount_computation | FACT | always | — | Three early payment discount tax computation modes: included, excluded, mixed | N-U47-012 |
| VDR-U47-C099 | FUNC-U47-F009 | account/models/account_payment_term.py:82 | `def _compute_discount_computation(self):` | FACT | always | — | Default discount computation mode is country-specific: BE=mixed, NL=excluded, all others=included | N-U47-012 |
| VDR-U47-C100 | FUNC-U47-F009 | account/models/account_payment_term.py:160 | `if float_round(total_percent, precision_digits=round_precision) != 100:` | FACT | constraint | — | Constraint uses Payment Terms decimal precision to check percentages sum to 100% | N-U47-012 |
| VDR-U47-C101 | FUNC-U47-F009 | account/models/account_payment_term.py:163 | `if len(terms.line_ids) > 1 and terms.early_discount:` | FACT | constraint | — | Early discount only valid on single-line 100% payment terms | N-U47-012 |
| VDR-U47-C102 | FUNC-U47-F009 | account/models/account_payment_term.py:190 | `rate = abs(total_amount_currency / total_amount) if total_amount else 0.0` | FACT | always | — | Currency rate derived from invoice amounts ratio, not from currency.rate table directly | N-U47-012 |
| VDR-U47-C103 | FUNC-U47-F009 | account/models/account_payment_term.py:227 | `on_balance_line = i == len(self.line_ids) - 1` | FACT | always | — | The last payment term line always receives the entire residual balance regardless of type | N-U47-012 |
| VDR-U47-C104 | FUNC-U47-F009 | account/models/account_payment_term.py:203 | `pay_term['discount_balance'] = company_currency.round(total_amount - untaxed_amount * discount_percentage)` | FACT | excluded/mixed | — | For excluded/mixed discount computation, only untaxed amount portion is discounted | N-U47-012 |
| VDR-U47-C105 | FUNC-U47-F009 | account/models/account_payment_term.py:207 | `pay_term['discount_balance'] = company_currency.round(total_amount * (1 - discount_percentage))` | FACT | included | — | For included discount computation, full invoice total is discounted | N-U47-012 |
| VDR-U47-C106 | FUNC-U47-F009 | account/models/account_payment_term.py:313 | `return date_utils.end_of(due_date, 'month') + relativedelta(days=self.nb_days)` | FACT | days_after_end_of_month | — | days_after_end_of_month delay type: end of month then add nb_days | N-U47-012 |
| VDR-U47-C107 | FUNC-U47-F009 | account/models/account_payment_term.py:316 | `return date_utils.end_of(due_date + relativedelta(months=1), 'month') + relativedelta(days=self.nb_days)` | FACT | days_after_end_of_next_month | — | days_after_end_of_next_month: end of next month plus nb_days | N-U47-012 |
| VDR-U47-C108 | FUNC-U47-F009 | account/models/account_payment_term.py:326 | `return due_date + relativedelta(days=self.nb_days) + relativedelta(months=1, day=days_next_month)` | FACT | days_end_of_month_on_the | — | days_end_of_month_on_the: add nb_days then jump to next month on specific day | N-U47-012 |
| VDR-U47-C109 | FUNC-U47-F010 | account/models/account_cash_rounding.py:8 | class AccountCashRounding(models.Model) | FACT | always | — | Cash rounding model is account.cash.rounding | N-U47-013 |
| VDR-U47-C110 | FUNC-U47-F010 | account/models/account_cash_rounding.py:22 | `strategy = fields.Selection([('biggest_tax', 'Modify tax amount'), ('add_invoice_line', 'Add a rounding line')],` | FACT | always | — | Two rounding strategies: modify biggest tax or add separate invoice line | N-U47-013 |
| VDR-U47-C111 | FUNC-U47-F010 | account/models/account_cash_rounding.py:25 | profit_account_id = fields.Many2one | FACT | always | — | Profit and loss accounts are company_dependent allowing per-company configuration | N-U47-013 |
| VDR-U47-C112 | FUNC-U47-F010 | account/models/account_cash_rounding.py:57 | `return float_round(amount, precision_rounding=self.rounding, rounding_method=self.rounding_method)` | FACT | always | — | round() delegates to float_round with configured precision and method | N-U47-013 |
| VDR-U47-C113 | FUNC-U47-F010 | account/models/account_cash_rounding.py:68 | `difference = self.round(amount) - amount` | FACT | always | — | compute_difference returns (rounded_amount - currency_rounded_amount) | N-U47-013 |
| VDR-U47-C114 | FUNC-U47-F010 | account/models/account_cash_rounding.py:45 | `if record.rounding <= 0:` | FACT | constraint | — | ValidationError if rounding precision is zero or negative | N-U47-013 |
| VDR-U47-C115 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:325 | `if st_line.foreign_currency_id == st_line.currency_id:` | FACT | constraint | — | ValidationError raised if foreign_currency_id equals journal currency_id | N-U47-003 |
| VDR-U47-C116 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:600 | `rate_journal2foreign_curr = journal_amount and abs(transaction_amount) / abs(journal_amount)` | FACT | multi-currency | — | Internal rate from bank-provided amounts used for counterpart calculation | N-U47-003 |
| VDR-U47-C117 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:448 | `if (el == 'statement_id' or el == 'journal_id' or el.startswith('date')) and self.env.context.get('show_running_balance_latest'):` | FACT | grouped display | RT | Running balance latest shown in grouped view only when show_running_balance_latest context set | N-U47-001 |
| VDR-U47-C118 | FUNC-U47-F003 | account/wizard/account_payment_register.py:296 | `source_amount = abs(sum(lines.mapped('amount_residual')))` | FACT | always | — | Source amount in wizard is absolute sum of all batch lines' amount_residual | N-U47-005 |
| VDR-U47-C119 | FUNC-U47-F003 | account/wizard/account_payment_register.py:508 | `move_payment_method_lines = wizard.line_ids.move_id.preferred_payment_method_line_id` | FACT | journal select | — | Journal selection prefers move's preferred_payment_method_line_id if unique and available | N-U47-005 |
| VDR-U47-C120 | FUNC-U47-F009 | account/models/account_payment_term.py:258 | `if self.env['account.move'].search_count([('invoice_payment_term_id', 'in', self.ids)], limit=1):` | FACT | unlink | — | Payment term deletion blocked when referenced by any account.move record | N-U47-012 |
| VDR-U47-C121 | FUNC-U47-F004 | account/wizard/accrued_orders.py:52 | `domain="[('account_type', '=', 'liability_current')] if context.get('active_model') in ['purchase.order', 'purchase.order.line'] else [('account_type', '=', 'asset_current')]"` | FACT | always | — | Accrual account domain: liability_current for purchase, asset_current for sale | N-U47-007 |
| VDR-U47-C122 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:376 | `tax_ids = base_line.tax_ids.flatten_taxes_hierarchy().filtered(lambda x: x.tax_exigibility == 'on_payment')` | FACT | CABA | — | Only taxes with tax_exigibility='on_payment' generate CABA entries | N-U47-009 |
| VDR-U47-C123 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:375 | `account = base_line.company_id.account_cash_basis_base_account_id or base_line.account_id` | FACT | CABA | — | CABA base line uses company.account_cash_basis_base_account_id or original account | N-U47-009 |
| VDR-U47-C124 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:440 | `account_id': tax_line.tax_repartition_line_id.account_id.id or tax_line.company_id.account_cash_basis_base_account_id.id or tax_line.account_id.id` | FACT | CABA | — | CABA tax line account: repartition account or cash_basis_base_account or original account | N-U47-009 |
| VDR-U47-C125 | FUNC-U47-F003 | account/wizard/account_payment_register.py:577 | `if wizard.journal_id.type == 'cash':` | FACT | cash journal | — | Cash journals never show partner bank account field | N-U47-005 |
| VDR-U47-C126 | FUNC-U47-F003 | account/wizard/account_payment_register.py:579 | `wizard.show_partner_bank_account = wizard.payment_method_line_id.code in self.env['account.payment']._get_method_codes_using_bank_account()` | FACT | non-cash | — | Partner bank account shown based on payment method code in _get_method_codes_using_bank_account() | N-U47-005 |
| VDR-U47-C127 | FUNC-U47-F002 | account/models/res_currency.py:233 | `date_from = date_utils.start_of(fields.Date.from_string(date_to), 'year')` | FACT | average rate | — | When no date_from provided for average rate, defaults to start of year containing date_to | N-U47-004 |
| VDR-U47-C128 | FUNC-U47-F008 | account/models/account_reconcile_model.py:8 | `_inherit = ['analytic.mixin']` | FACT | always | — | Reconcile model line inherits analytic.mixin for analytic distribution support | N-U47-011 |
| VDR-U47-C129 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:28 | `draft_caba_move_vals = fields.Json(string="Values that created the draft cash-basis entry")` | FACT | always | — | draft_caba_move_vals JSON field stores snapshot of move values used to create draft CABA entries | N-U47-009 |
| VDR-U47-C130 | FUNC-U47-F005 | account/wizard/account_move_reversal.py:176 | `def refund_moves(self):` | FACT | always | — | refund_moves calls reverse_moves(is_modify=False); modify_moves calls reverse_moves(is_modify=True) | N-U47-008 |
| VDR-U47-C131 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:411 | `to_write = {'statement_line_id': st_line.id, 'narration': st_line.narration, 'name': False}` | FACT | always | — | On create, move is written with statement_line_id reference and name=False | N-U47-001 |
| VDR-U47-C132 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:414 | `self.env.add_to_compute(self.env['account.move']._fields['name'], st_lines.move_id)` | FACT | always | — | Move name is re-computed (sequence) after statement line create to get proper name | N-U47-001 |
| VDR-U47-C133 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:417 | `self.env.remove_to_compute(self.env['account.move']._fields['narration'], st_lines.move_id)` | FACT | always | — | Narration field is removed from compute queue after create to prevent silent recompute | N-U47-001 |
| VDR-U47-C134 | FUNC-U47-F003 | account/wizard/account_payment_register.py:588 | `if unpaid_matched_payments := wizard.line_ids.move_id.reconciled_payment_ids.filtered(lambda p: p.state == 'in_process'):` | FACT | always | — | actionable_errors checks for in_process payments already matched to the same invoices | N-U47-005 |
| VDR-U47-C135 | FUNC-U47-F009 | account/models/account_payment_term.py:293 | compute='_compute_value_amount | FACT | always | — | Four delay types on payment term lines | N-U47-012 |
| VDR-U47-C136 | FUNC-U47-F003 | account/wizard/account_payment_register.py:25 | group_payment = | FACT | always | — | group_payment collapses multiple bills into a single payment per partner/bank | N-U47-005 |
| VDR-U47-C137 | FUNC-U47-F003 | account/wizard/account_payment_register.py:486 | `wizard.group_payment = len(wizard.batches[0]['lines'].move_id) == 1` | FACT | can_edit_wizard | — | group_payment defaults True when only one move in the batch (nothing to group) | N-U47-005 |
| VDR-U47-C138 | FUNC-U47-F004 | account/wizard/accrued_orders.py:321 | `total = sum(order.amount_total for order in orders)` | FACT | always | — | Analytic distribution for global counterpart is weighted by each order line's price_total / total_order_amount | N-U47-007 |
| VDR-U47-C139 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:96 | `if partial.debit_move_id.move_id.is_invoice(True):` | FACT | always | — | company_id on partial reconcile set to invoice-side company when one side is an invoice | N-U47-009 |
| VDR-U47-C140 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:362 | `def new(self, values=None, origin=None, ref=None):` | FACT | always | — | new() overridden to inject is_statement_line=True context | N-U47-001 |
| VDR-U47-C141 | FUNC-U47-F001 | account/models/account_bank_statement_line.py:843 | `statement_line_ids = fields.One2many('account.bank.statement.line', 'move_id', string='Statements')` | FACT | always | — | account.move gets a statement_line_ids reverse relation for performance optimisation | N-U47-001 |
| VDR-U47-C142 | FUNC-U47-F009 | account/models/account_payment_term.py:156 | `round_precision = self.env['decimal.precision'].precision_get('Payment Terms')` | FACT | constraint | — | Percentage sum validation uses the 'Payment Terms' decimal precision setting | N-U47-012 |
| VDR-U47-C143 | FUNC-U47-F003 | account/wizard/account_payment_register.py:850 | wizard.writeoff_is_exchange_account = all | FACT | always | — | writeoff_is_exchange_account requires: edit mode + reconcile handling + different currency + writeoff account matching exchange accounts | N-U47-005 |
| VDR-U47-C144 | FUNC-U47-F002 | account/models/res_currency.py:40 | return bool(self.env['account.move.line'].sudo | FACT | always | — | _has_accounting_entries checks both currency_id and company_currency_id on account.move.line | N-U47-004 |
| VDR-U47-C145 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:117 | `moves_to_reverse = self.env['account.move'].search([('tax_cash_basis_rec_id', 'in', self.ids)])` | FACT | unlink | — | CABA moves located for reversal by searching tax_cash_basis_rec_id field | N-U47-009 |
| VDR-U47-C146 | FUNC-U47-F006 | account/models/account_partial_reconcile.py:141 | `reversal_date = lock_dates[-1][0] + timedelta(days=1)` | FACT | unlink with lock date | — | CABA reversal date moved forward by one day past the most recent lock date | N-U47-009 |
| VDR-U47-C147 | FUNC-U47-F003 | account/wizard/account_payment_register.py:190 | `label = self.company_id.get_next_batch_payment_communication()` | FACT | multi-move outbound | INFERENCE | For multi-outbound payments, communication uses company's next batch payment sequence | N-U47-005 |
| VDR-U47-C148 | FUNC-U47-F005 | account/wizard/account_move_reversal.py:71 | `if len(move_ids.company_id) > 1:` | FACT | always | C1 | Reversal wizard raises UserError when moves belong to different companies | N-U47-008 |
| VDR-U47-C149 | FUNC-U47-F005 | account/wizard/account_move_reversal.py:74 | `if any(move.state != "posted" for move in move_ids):` | FACT | always | C1 | Reversal wizard raises UserError when any move is not posted | N-U47-008 |
| VDR-U47-C150 | FUNC-U47-F008 | account/models/account_reconcile_model.py:130 | match_amount = fields.Selection(selection= | FACT | always | — | Reconcile model journal filter restricted to bank/cash/credit journals | N-U47-011 |
