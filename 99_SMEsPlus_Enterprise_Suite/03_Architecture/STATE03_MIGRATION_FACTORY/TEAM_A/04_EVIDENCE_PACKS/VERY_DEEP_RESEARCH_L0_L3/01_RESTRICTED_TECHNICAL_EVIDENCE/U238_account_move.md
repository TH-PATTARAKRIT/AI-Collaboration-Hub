# U238 — account.move header model, `_post()` pipeline and payment status (Odoo 19 Community)

RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

## 0. Unit header

| Item | Value |
|---|---|
| Unit | U238 |
| Module | account_move (model `account.move`, description "Journal Entry", addon `account`) |
| Release studied | 19.0.post20260921 (Community; read-only source tree) |
| Research date | 2026-10-02 |
| Scope | header level only: move_type, state, payment_state; the `_post()` pipeline; amount computation; invoice header fields; sequence and lock-date interplay; reversal; auto-post; Thai-relevant header fields |
| Not duplicated here | line level (U204), tax engine (U224), sequence and lock engine (U114), lifecycle (U79), credit-note immutability (U122), payment terms (U212), reconcile engine (U239) |
| Pointer convention | paths are relative to `odoo-19.0.post20260921/odoo/addons/`; `file:N` is one line, `file:N-M` a range |
| Claim register | final section of this file (C001 to C026); the narrative cites claims by short id (for example C004) |

## 1. Evidence base and limits

### 1.1 Sources read

| Source | Use |
|---|---|
| account/models/account_move.py (7489 lines) | primary; every pointer in the claim register was read in range |
| account/models/sequence_mixin.py | `_sequence_matches_date` (138), `_constrains_date_sequence` (156), `_set_next_sequence` (425) |
| account/models/company.py | lock-date helpers (640-748), settings fields (97, 112, 128, 153, 233, 246-269, 319-323) |
| account/models/account_move_line.py | `remove_move_reconcile` (3146), reconciliation unlink on protected-field write (1862-1885) |
| account/models/account_journal.py, partner.py, account_payment.py, account_partial_reconcile.py | call sites and field declarations located by search (journal 1134; partner 610-616; payment 255-259, 912-914; partial reconcile 24, 117-119, 562) |
| account/security/ir.model.access.csv, account_security.xml | ACL and record-rule rows (36-41; 128-132, 232-290) |
| sale/models/account_move.py, sale_order.py | link fields, `_post`, `button_draft`, `button_cancel`, `_reverse_moves`, `_invoice_paid_hook` extensions |
| purchase/models/account_invoice.py, purchase_order.py | origin composition, purchase-order matching, link fields |
| stock_account/models/account_move.py | `copy_data`, `_post`, `button_draft`, `button_cancel` extensions |
| sale_stock, purchase_stock, account_payment (account_move.py) | delivery-date population, post extension, payment-link fields (listing and excerpts) |
| l10n_th (all 18 files listed; account_move.py, ir_actions_report.py, res_partner.py, res_bank.py, report_invoice.xml read; data CSV searched) | Thai header relevance |
| 00_CONTROL/WORKER_SPEC_L2_L3.md; U11, U12, U33, U79, U122 evidence files | format and deduplication only |
| Database `itest19c_research` (restored copy) | configuration and structure queries only; no business data recorded |

### 1.2 Limits and vocabulary

- No Odoo process was started and no business data was read.
- The `account` addon has no `migrations` directory in this tree, so every v16/v17 comparison below is INFERENCE (from in-tree deprecation markers, comments and recollection of earlier releases) and PENDING CLAUDE VERIFICATION.
- Class: FACT = read directly in source or database; OBSERVATION = seen in data or configuration; INFERENCE = deduced from source plus convention; UNKNOWN = not determinable statically.
- Flags: RT = runtime (AWT) verification required; CONTRA = contradicts prior evidence (named in the claim); an em dash = none.

## 2. Model identity (shared context)

| Attribute | Value | Pointer |
|---|---|---|
| `_name` | account.move | account/models/account_move.py:73-82 |
| `_description` | "Journal Entry" | account/models/account_move.py:73-82 |
| `_inherit` | portal.mixin, mail.thread.main.attachment, mail.activity.mixin, sequence.mixin, product.catalog.mixin, account.document.import.mixin | account/models/account_move.py:73-82 |
| `_order` | date desc, name desc, invoice_date desc, id desc | account/models/account_move.py:77 |
| `_check_company_auto` | True (company consistency of relational fields is auto-checked) | account/models/account_move.py:79 |
| `_sequence_index` | journal_id (sequence chains are per journal) | account/models/account_move.py:80 |
| Constants | `MAX_HASH_VERSION = 4` (47); `PAYMENT_STATE_SELECTION` (49-57); `TYPE_REVERSE_MAP` (59-67); `EMPTY`, `BYPASS_LOCK_CHECK` (69-70) | account/models/account_move.py:47-70 |

## CAP-U238-01 Document type, status and payment-status model

Function-ID: FUNCTION MAPPING REQUIRED (no entry of the existing function index covers header type, state or payment state)
Claims: C001, C002, C003, C004, C005

### D1 Structure

| Field or constant | Pointer | Declaration summary |
|---|---|---|
| `move_type` | account/models/account_move.py:143-160 | Selection with 7 values; string 'Type'; required, readonly, tracking, change_default, index; default "entry" |
| `state` | account/models/account_move.py:130-142 | Selection draft "Draft", posted "Posted", cancel "Cancelled"; string 'Status'; required, readonly, copy=False, tracking; default draft |
| `PAYMENT_STATE_SELECTION` | account/models/account_move.py:49-57 | not_paid "Not Paid", in_payment "In Payment", paid "Paid", partial "Partially Paid", reversed "Reversed", blocked "Blocked", invoicing_legacy "Invoicing App Legacy" |
| `payment_state` | account/models/account_move.py:606-612 | Selection from the constant; string "Payment Status"; compute `_compute_payment_state`, store, readonly, copy=False, tracking |
| `status_in_payment` | account/models/account_move.py:613-622 | NEW in the studied release; Selection = the 7 payment states plus draft, posted, sent, cancel (11 values); non-stored; copy=False |
| `TYPE_REVERSE_MAP` | account/models/account_move.py:59-67 | entry to entry; out_invoice to out_refund; out_refund to out_invoice; in_invoice to in_refund; in_refund to in_invoice; out_receipt to out_refund; in_receipt to in_refund |

`move_type` values and labels: entry "Journal Entry"; out_invoice "Customer Invoice"; out_refund "Customer Credit Note"; in_invoice "Vendor Bill"; in_refund "Vendor Credit Note"; out_receipt "Sales Receipt"; in_receipt "Purchase Receipt" (account/models/account_move.py:143-160).

Type helpers (account/models/account_move.py:6563-6602):

| Helper | Pointer | Result |
|---|---|---|
| `get_invoice_types(include_receipts=False)` | account/models/account_move.py:6564 | sale types plus purchase types |
| `is_invoice(include_receipts=False)` | account/models/account_move.py:6567 | sale document or purchase document |
| `is_entry()` | account/models/account_move.py:6570 | move_type is entry |
| `is_receipt()` | account/models/account_move.py:6573 | move_type is out_receipt or in_receipt |
| `get_sale_types(include_receipts=False)` | account/models/account_move.py:6577 | out_invoice, out_refund (+ out_receipt when the flag is true) |
| `get_purchase_types(include_receipts=False)` | account/models/account_move.py:6584 | in_invoice, in_refund (+ in_receipt when the flag is true) |
| `get_inbound_types(include_receipts=True)` | account/models/account_move.py:6591 | out_invoice, in_refund (+ out_receipt) |
| `get_outbound_types(include_receipts=True)` | account/models/account_move.py:6598 | in_invoice, out_refund (+ in_receipt) |

The defaults differ: sale/purchase/invoice helpers exclude receipts unless asked, while the inbound/outbound helpers include receipts unless told otherwise. Several `_post` checks depend on that difference (see CAP-U238-03).

### D2 Behaviour

1. `state` is a three-value selection (draft, posted, cancel). It is readonly and is changed only by code paths: `_post` writes posted (account/models/account_move.py:5757-5760), `button_draft` writes draft (6280), `button_cancel` writes cancel (6396). `create` refuses a vals dictionary that asks for state posted (3893-3910); a posted move can exist only by being created as a draft and posted afterwards.
2. `payment_state` is a stored computed field. Only invoice-like moves (including receipts) that are posted, or draft with a non-zero total, are evaluated against reconciliations; everything else is set to not_paid (account/models/account_move.py:1235-1248). Moves already in invoicing_legacy or blocked are skipped by the recompute (1242-1247).
3. The evaluation of qualifying documents is described in C004: a raw SQL over partial reconciles groups settlement counterparts per source line (1261-1279), restricted to receivable and payable lines (1292); zero residual yields paid, or reversed when the counterparts are refund-type or entry moves (1307-1319); non-zero residual with reconciliation rows yields partial (1322-1323).
4. `in_payment` is declared but, in the Community tree, no code path produces it: the single definition of `_get_invoice_in_payment_state` returns paid (account/models/account_move.py:7366-7371) and its docstring says it is overridden in the accountant module to enable in_payment. Whether that override exists is INFERENCE (Enterprise is out of scope).
5. `status_in_payment` is a non-stored display merge (C005): posted moves show the payment state (partial, in_payment, paid, reversed, blocked) or sent when `is_move_sent`; draft moves show partial, in_payment, paid or blocked; otherwise the plain state (account/models/account_move.py:1328-1341). Its SQL expression for search/group maps draft to draft, cancel to cancel and everything else to payment_state (1343-1351).
6. `action_toggle_block_payment` flips between blocked and not_paid and refuses to block a paid or in-payment document: "You can't block a paid invoice." (account/models/account_move.py:6398-6406). After unblocking it schedules a recompute of payment_state (6402).
7. No Community Python assigns `invoicing_legacy`: it appears as a selection value (account/models/account_move.py:56), as a skip group in the recompute (1243), and as a read-only filter in portal (account/controllers/portal.py:63), purchase (purchase/models/purchase_order_line.py:202) and sale (sale/models/sale_order_line.py:1020, 1039, 1143, 1157). The producer is therefore outside the studied tree (INFERENCE: an accounting-app migration step).

### D3 State diagram

State of `state`:
- (new) -> draft [create default (account/models/account_move.py:141); create with state posted is refused (3893-3910)]
- draft -> posted [`_post` write at 5757-5760; entry points: `action_post` 6180-6201, auto-post cron 6460-6493]
- posted -> draft [`button_draft` 6269-6284]
- cancel -> draft [`button_draft` 6269-6284 accepts cancel and posted]
- draft -> cancel [`button_cancel` 6384-6396]
- posted -> cancel [`button_cancel` first runs `button_draft` (6387-6389), then cancels]
- posted or cancel -> posted [not allowed: `_post` reports "must be in draft" (5652-5653)]

State of `payment_state` (qualifying invoice-like documents):
- not_paid -> paid [residual zero and no payment or statement counterpart (1304-1305), or all counterpart payments matched (1299-1300)]
- not_paid -> partial [residual non-zero with reconciliation rows (1322-1323)]
- not_paid -> in_payment [only through `_get_invoice_in_payment_state`; Community returns paid, so unreachable in Community (7371)]
- paid -> reversed [counterparts are only refund-type moves, or refund-type plus entry (1307-1319)]
- not_paid -> blocked [`action_toggle_block_payment` (6406)]
- blocked -> not_paid [`action_toggle_block_payment` (6400-6402)]
- any -> not_paid [group "unpaid": non-invoice moves, cancelled moves, zero-total drafts (1245-1248)]
- invoicing_legacy -> invoicing_legacy [never recomputed (1243)]

### Ten-dimension analysis

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | A move is created as draft; posting writes posted (5757-5760); as reconciliations appear `payment_state` moves not_paid, partial, paid; `status_in_payment` mirrors it for display. |
| 2 | Reversal, cancel, negative | `TYPE_REVERSE_MAP` (59-67) selects the reverse type; `payment_state` becomes reversed when settled only by refund-type moves (1307-1319); posting a negative total is refused (5624-5629); `button_cancel` writes cancel (6396). |
| 3 | Multi-company, data scope | `company_id` participates in the compute trigger (1233) and supplies the currency fallback (1236, 1288); global record rule `account.account_move_comp_rule` restricts to the user's companies (DB reconciliation below). |
| 4 | Side effects, cross-module | `status_in_payment` follows `payment_state`, `state`, `is_move_sent` (1328); portal filters use payment_state (account/controllers/portal.py:63); sale and purchase invoicing-state code reads `payment_state == 'invoicing_legacy'` (sale/models/sale_order_line.py:1020 and others); account_payment gates on edition (account/models/account_payment.py:255-259, 912-914). |
| 5 | Configuration, optionality | Receipts participate only where code passes `include_receipts` (see D1); `in_payment` availability depends on an accounting-app override (INFERENCE); `account_debit_note` is not installed so no debit-note type is added. |
| 6 | Validation, constraints | `state` and `move_type` are readonly; `create` refuses state posted (3893-3910); `_check_journal_move_type` ties type to journal type (2849-2855, CAP-U238-05). |
| 7 | Roles, permissions | Posting requires `account.group_account_invoice` unless superuser (5583-5584); ACL rows in the DB reconciliation below. |
| 8 | Scheduled, automated | Payment state recomputes by ORM triggers, not by cron; the auto-post cron posts due drafts (CAP-U238-06). |
| 9 | Exception, failure | "You can't block a paid invoice." (6405); `button_draft` refuses states other than posted/cancel (6270-6271); `button_cancel` refuses non-drafts (6391-6392). |
| 10 | Accounting, audit, security, compliance | `state`, `payment_state`, `move_type` carry tracking (chatter audit); a hash-locked move cannot be reset to draft (6372-6373); posted-move write guard in CAP-U238-04. |

### DB reconciliation (restored copy, structure only)

- Selection value counts for `account.move` fields: move_type 7, state 3, payment_state 7, status_in_payment 11 (OBSERVATION; matches source).
- `status_in_payment` is non-stored in the metadata; `payment_state` is stored.
- The `account_move` table has 0 rows in the restored copy, so no runtime payment-state behaviour can be observed there.
- Installed modules relevant to this capability: account, account_payment, sale, purchase, sale_stock, purchase_stock, stock_account, hr_expense, l10n_th; no accountant module; `account_debit_note` not installed.
- ACL rows on `account.move`: group_account_invoice full CRUD; group_purchase_user full CRUD; group_account_manager, group_account_readonly, group_sale_salesman, group_hr_expense_team_approver and group_portal read only.

### Unknown and runtime list

- RT: payment-state transitions with real partial, full, reversed and statement-matched reconciliations (the SQL grouping at 1261-1279 and the matched-payment branches at 1320-1325).
- UNKNOWN: whether an accounting-app override of `_get_invoice_in_payment_state` exists (outside the Community tree).
- UNKNOWN: which external process assigns invoicing_legacy.
- RT: effect on `payment_state` of resetting a reconciled posted invoice to draft (see CAP-U238-04: `button_draft` does not unlink reconciliations).

## CAP-U238-02 Header amounts, signs and the tax summary structure

Function-ID: FUNCTION MAPPING REQUIRED (the existing function index has no header amount entry)
Claims: C006, C007, C008

### D1 Structure

| Field | Pointer | Declaration summary |
|---|---|---|
| `direction_sign` | account/models/account_move.py:547-550 | Integer, non-stored, compute `_compute_direction_sign`; help text: multiplicator by document type to convert a price into a balance |
| `amount_untaxed` | account/models/account_move.py:551-555 | Monetary 'Untaxed Amount'; compute `_compute_amount`, store, readonly, tracking (the only amount field with tracking) |
| `amount_tax` | account/models/account_move.py:556-559 | Monetary 'Tax'; same compute; store, readonly |
| `amount_total` | account/models/account_move.py:560-564 | Monetary 'Total'; same compute; store, readonly; inverse `_inverse_amount_total` |
| `amount_residual` | account/models/account_move.py:565-568 | Monetary 'Amount Due'; same compute; store (no readonly flag) |
| `amount_untaxed_signed`, `amount_tax_signed`, `amount_total_signed`, `amount_residual_signed` | account/models/account_move.py:569-573, 579-583, 584-588, 594-598 | company currency (`company_currency_id`), stored, same compute; strings 'Untaxed Amount Signed', 'Tax Signed', 'Total Signed', 'Amount Due Signed' |
| `amount_untaxed_in_currency_signed`, `amount_total_in_currency_signed` | account/models/account_move.py:574-578, 589-593 | document currency (`currency_id`), stored, same compute; strings 'Untaxed Amount Signed Currency', 'Total in Currency Signed' |
| `tax_totals` | account/models/account_move.py:599-605 | Binary "Invoice Totals", compute `_compute_tax_totals`, inverse `_inverse_tax_totals`, non-stored, exportable=False |
| `amount_total_words` | account/models/account_move.py:623-626 | NEW; non-stored; compute `_compute_amount_total_words` (2218) = `currency_id.amount_to_text(amount_total)` with commas removed (2220) |
| `company_currency_id`, `currency_id` | account/models/account_move.py:522-532 | company currency related; document currency required, compute, inverse, store, precompute |
| `invoice_currency_rate` | account/models/account_move.py:537-544 | compute, store, precompute, readonly=False, copy=False, digits 0; help: "Currency rate from company currency to document currency." |

### D2 Behaviour

1. `direction_sign` (account/models/account_move.py:1157-1163) is 1 when the move is an entry or `is_outbound()` (in_invoice, out_refund, in_receipt), otherwise -1 (out_invoice, in_refund, out_receipt).
2. `_compute_amount` (decorator 1165-1179, def 1180) reads the line fields and classifies each line of an invoice-like move (`is_invoice(True)`) by `display_type`:
   - tax, non_deductible_tax, and rounding lines that carry a `tax_repartition_line_id` add to the tax and total accumulators (1199-1204);
   - product, rounding (without repartition), non_deductible_product and non_deductible_product_total lines add to the untaxed and total accumulators (1205-1210);
   - payment_term lines add to the residual accumulators (1211-1214);
   - for entries only lines with a debit add to the total (1215-1219).
3. The assignments (1221-1231), with `sign = direction_sign`:
   - `amount_untaxed = sign * total_untaxed_currency` (1222); `amount_tax = sign * total_tax_currency` (1223); `amount_total = sign * total_currency` (1224); `amount_residual = -sign * total_residual_currency` (1225);
   - `amount_untaxed_signed = -total_untaxed` (1226); `amount_untaxed_in_currency_signed = -total_untaxed_currency` (1227); `amount_tax_signed = -total_tax` (1228);
   - `amount_total_signed = abs(total)` for entries, else `-total` (1229); `amount_residual_signed = total_residual` (1230);
   - `amount_total_in_currency_signed = abs(amount_total)` for entries, else `-(sign * amount_total)` (1231).
4. Sign convention consequence (derived from the formulas): document-currency amounts of invoices, bills and credit notes are positive; the signed company-currency fields are positive for receivable-side documents (out_invoice, in_refund, out_receipt) and negative for payable-side documents; `amount_residual_signed` keeps the raw balance sign of the receivable or payable lines.
5. `tax_totals` is computed only for invoice-like moves including receipts (account/models/account_move.py:1841) and is None for every other move (1857). The structure comes from `AccountTax._get_tax_totals_summary(base_lines, currency, company, cash_rounding)` (1843-1848), fed by `_get_rounded_base_and_tax_lines` (1778-1823): product lines as base lines (`line_ids` when the move is stored or not an invoice, otherwise `invoice_line_ids`, 1791-1794); for stored moves early-payment-discount, cash-rounding and non-deductible lines are added and existing tax journal items are used to keep manual tax amounts (1798-1816); for unsaved moves only invoice lines are used (1817-1822). `display_in_company_currency` is set only when the company flag `display_invoice_tax_company_currency` is on, currencies differ, tax groups exist and the move is a sale document including receipts (1849-1854).
6. `_inverse_tax_totals` (2548-2576) adjusts the first tax line per group by the edited delta and then recomputes amounts; `_inverse_amount_total` (2578-2596) applies only to non-invoice moves with exactly two lines.

### D3 State diagram

- amounts (not computed) -> amounts (computed) [any change of line fields listed in the compute dependencies (1165-1179); stored]
- tax_totals (none) -> tax_totals (structure) [`_compute_tax_totals` for invoice-like moves (1836-1848); recomputed on lang context and the listed line, term, partner and currency dependencies (1825-1835)]
- tax_totals (edited) -> tax lines adjusted -> amounts recomputed [`_inverse_tax_totals` (2548-2576)]

### Ten-dimension analysis

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Line changes trigger `_compute_amount`; document-currency and company-currency amounts are stored; `tax_totals` is derived on demand from base and tax lines. |
| 2 | Reversal, cancel, negative | Refund types flip `direction_sign` and the line signs so document amounts stay positive; negative totals block posting (5624-5629); `amount_total_signed` for entries uses the absolute value (1229). |
| 3 | Multi-company, data scope | Company currency is the source of balances (`company_currency_id`); `tax_totals` takes the company for rounding (1846); `display_invoice_tax_company_currency` is a per-company setting (account/models/company.py:153). |
| 4 | Side effects, cross-module | `amount_residual` feeds `payment_state` (1233); `tax_totals` feeds the invoice widget and reports; `amount_total_words` feeds printed layouts (field is non-stored). |
| 5 | Configuration, optionality | Cash rounding (`invoice_cash_rounding_id`, passed at 1847), early-payment discount lines, non-deductible lines, and the company currency-display flag change the structure. |
| 6 | Validation, constraints | `_check_balanced` is a context manager wrapped around create (3898), write (3981) and other mutators; it raises "The entry is not balanced." (2782-2793); `_check_invoice_currency_rate` requires a strictly positive rate for foreign-currency invoices (2872-2883). |
| 7 | Roles, permissions | Fields carry no group restriction in the declarations read; access follows the model ACL (CAP-U238-01 DB reconciliation). |
| 8 | Scheduled, automated | None; stored amounts recompute on dependency change. |
| 9 | Exception, failure | `_inverse_amount_total` silently does nothing for invoices and for moves without exactly two lines (2578-2596). |
| 10 | Accounting, audit, security, compliance | Amounts are stored; only `amount_untaxed` carries chatter tracking (554). The integrity-hash field set is read in CAP-U238-04 (hash fields come from `_get_integrity_hash_fields`, 4592-4599). |

### DB reconciliation

- Non-stored fields in the metadata: tax_totals, amount_total_words, expected_currency_rate, is_storno, needed_terms, alerts, status_in_payment (OBSERVATION); the amount fields and `invoice_currency_rate` are stored.
- `account_move` has 0 rows; no numeric behaviour was observed.

### Unknown and runtime list

- RT: numeric behaviour with cash rounding, early-payment discount, multi-currency and non-deductible lines.
- RT: `display_in_company_currency` rendering conditions.
- Detailed tax computation is delegated to U224; line-level fields to U204.

## CAP-U238-03 Posting pipeline (`_post`), sequence trigger and post hooks

Function-ID: PCO-F01 (lock-date adjustment step, C010); FUNCTION MAPPING REQUIRED (C009, C011, C012, C013)
Claims: C009, C010, C011, C012, C013

### D1 Structure

`_post(self, soft=True)` is declared at account_move.py:5569 and ends at 5801 (returns `to_post`). Stages in source order:

| # | Stage | Lines |
|---|---|---|
| 1 | Access guard: not superuser and not in group `account.group_account_invoice` -> AccessError | 5583-5584 |
| 2 | Context flag `skip_is_manually_modified=True` | 5587 |
| 3 | Invoice-like validations (collected in `validation_msgs`) | 5591-5648 |
| 4 | Per-move checks | 5650-5679 |
| 5 | Aggregated UserError for collected messages | 5681-5683 |
| 6 | Archived analytic accounts UserError (raised separately) | 5685-5689 |
| 7 | Soft-mode handling of future-dated moves | 5691-5700 |
| 8 | Lock-date date adjustment | 5702-5706 |
| 9 | Analytic lines creation | 5709 |
| 10 | Recurring copy (`_copy_recurring_entries`) unless `skip_recurring_copy` | 5711-5713 |
| 11 | Partner aligned to commercial partner | 5715-5723 |
| 12 | Draft-reversal / partial / cash-basis preparation | 5725-5755 |
| 13 | State write `{'state': 'posted', 'posted_before': True}` | 5757-5760 |
| 14 | Auto-grant of `group_partial_purchase_deductibility` to current user | 5762-5764 |
| 15 | Non-deductible line names | 5766-5773 |
| 16 | `_reconcile_reversed_moves` and `_reconcile_marked` | 5775-5776 |
| 17 | Customer / supplier rank increment | 5778-5794 |
| 18 | Zero-total `_invoice_paid_hook` | 5796-5799 |
| 19 | Return `to_post` | 5801 |

Invoice-like validations (stage 3), pointer `account/models/account_move.py`:

| Check | Lines |
|---|---|
| Quick-edit total mismatch | 5592-5602 |
| Archived partner bank | 5603-5607 |
| Inbound document with a bank that is not `allow_out_payment` (superuser/public/portal: bank cleared silently; user able to trust: RedirectWarning; otherwise UserError) | 5608-5623 |
| Negative total | 5624-5629 |
| Partner required (`is_sale_document()` / `is_purchase_document()` WITHOUT receipts) | 5631-5638 |
| Missing `invoice_date`: sale documents incl. receipts get context today (protecting `invoice_currency_rate`); purchase documents incl. receipts raise "The Bill/Refund date is required to validate this document." | 5642-5648 |

Per-move checks (stage 4):

| Check | Lines |
|---|---|
| `_check_constrains_account_id_journal_id` | 5651 |
| Move must be draft | 5652-5653 |
| At least one line that is not section / subsection / note ("Even magicians can't post nothing!") | 5654-5655 |
| Hard post (`soft=False`) of a move with `auto_post != 'no'` and a future date | 5656-5658 |
| Archived journal | 5659-5663 |
| Inactive currency | 5664-5668 |
| Archived accounts unless context `skip_account_deprecation_check` | 5670-5671 |
| Accounts of another company (parent_ids) | 5673-5679 |

Sequence, date, hash and lock machinery:

| Element | Pointer |
|---|---|
| `_compute_name` (depends posted_before, state, journal_id, date, move_type, origin_payment_id) | account/models/account_move.py:951-968 |
| `_set_next_sequence` | account/models/sequence_mixin.py:425-447 |
| `_sequence_matches_date` / `_constrains_date_sequence` | account/models/sequence_mixin.py:138-154 / 156-181 |
| `_compute_date` | account/models/account_move.py:861-876 |
| `_get_accounting_date_source` | account/models/account_move.py:857-859 |
| `_get_accounting_date` | account/models/account_move.py:6714-6751 |
| `_get_violated_lock_dates` (move) / (company) | account/models/account_move.py:6753-6760 / account/models/company.py:723-739 |
| Write post-checks (`_check_fiscal_lock_dates`, hash) | account/models/account_move.py:3999-4006; 2823-2840 |
| `_must_check_constrains_date_sequence` | account/models/account_move.py:4197-4199 |

`_post` extension chain (pointers relative to the addons root):

| Module | Lines | Effect |
|---|---|---|
| sale | sale/models/account_move.py:120-133 | `posted = super()._post(soft)` at 124; then auto-reconciles payments of payment transactions via `js_assign_outstanding_line` (126-132) |
| stock_account | stock_account/models/account_move.py:29-44 | Skipped when `move_reverse_cancel`; creates COGS lines before super; sets stock-move value after |
| purchase_stock | purchase_stock/models/account_invoice.py:113-117 | Anglo-saxon lines unless `move_reverse_cancel` |
| account_edi | account_edi/models/account_move.py:233-265 | Creates/updates EDI documents per journal format; raises "Invalid invoice configuration"; triggers cron |
| account_fleet | account_fleet/models/account_move.py:9-29 | Fleet log services for in_invoice product lines with a vehicle |
| account_payment_interco | account_payment_interco/models/account_move.py:30-37 | Inter-company clearing check |
| product_email_template | product_email_template/models/account_move.py:25-29 | `invoice_validate_send_email` |
| account_peppol_response | account_peppol_response/models/account_move.py:41-44 | `action_peppol_send_approval_response` |
| country packs | 16 files | Out of Thailand-only scope; not read |

### D2 Behaviour

1. Entry points: `action_post` calls `_post(soft=False)` (6180-6201); the cron `_autopost_draft_entries` calls `_post()` with the default `soft=True` (6475, 6486); recurring and other callers pass their own mode. `soft` only changes stage 7 (5691-5700) and the stage-4 check at 5656-5658.
2. Guards: stage 1 is the only permission check inside `_post`; the model ACL is separate (see the ten-dimension table). Context `skip_is_manually_modified` (5587) prevents the writes made during posting from flagging the move as manually modified.
3. Errors are collected into one set `validation_msgs` and raised together at 5681-5683, so a user sees all invoice-level problems at once. The bank-trust errors (5612-5623) and archived analytic accounts (5685-5689) are raised separately and immediately.
4. Sale versus purchase `invoice_date` handling: sale documents (incl. receipts) silently default to today; purchase documents (incl. receipts) refuse. The partner-required rule (5631-5638) excludes receipts, but the invoice_date rule (5642-5648) includes receipts.
5. Soft mode (5691-5700): moves with a future date are not posted; `auto_post` 'no' is switched to 'at_date', a chatter message is posted, and the move is excluded from `to_post`. Hard mode raises for such a move only when `auto_post != 'no'` (5656-5658).
6. Lock-date adjustment (5702-5706): for moves that `_affect_tax_report()` or have violated lock dates (`_get_violated_lock_dates`, which includes the hard lock; company.py:723-739), `date` is replaced by `_get_accounting_date`. No exception is raised at this step. `_get_accounting_date` (6714-6751) sets `invoice_date` to last violated lock + 1 day; for sale documents with lock dates it uses `min(today, end of month/year)` depending on the sequence reset type; for purchase documents it uses the end of the invoice month/year when that period is past, otherwise `max(invoice_date, today)`. For non-sale documents the adjustment is already applied at compute time (`_compute_date` 869-870), sale documents take `invoice_date` directly (861-876). EDGE (INFERENCE/RT): the adjusted date can still fall inside a lock (for example a lock date at or after today for a sale document), in which case the write-time checks (3999-4002) raise.
7. Sequence assignment has NO explicit call in `_post`. It is a side effect of the state write (stage 13): `_compute_name` (951-968) depends on `state`, `posted_before`, `date`; it skips cancelled moves (956-957), resets the name when not `posted_before` and `_sequence_matches_date()` fails (960-964), and calls `_set_next_sequence()` (966, the only caller in the account addon) when a date exists, no real name is set and state is not draft. `_inverse_name` follows at 968.
8. `posted_before` is written together with `state` at 5757-5760 and is never reset by `button_draft` (see CAP-U238-04); it gates the audit-trail unlink guard and the draft name reset (3990-3995).
9. Hash: `write` calls `flush_recordset()` then `_hash_moves()` at 4004-4006 whenever state is posted. At post time `_hash_moves()` runs with `force_hash=False`, so chains are skipped unless the journal has `restrict_mode_hash_table` (see CAP-U238-04).
10. Post-hook order inside the chain: sale/stock_account/purchase_stock/account_edi/account_fleet/account_payment_interco/product_email_template/account_peppol_response each call `super()._post()`; the base implementation (above) runs innermost, so base validations and the state write happen before the post-super parts of the extensions. stock_account creates COGS lines BEFORE calling super.
11. OBSERVATION: L5749 reads `move`, a loop variable leaked from earlier loops in the same method (bound, but order-dependent). The multi-move cash-basis branch therefore depends on loop order (RT).
12. `group_partial_purchase_deductibility` is granted to the current user when a posted line is partially deductible (5762-5764).
13. Context flags that change `_post`: `skip_is_manually_modified`, `skip_account_deprecation_check`, `skip_recurring_copy`, `move_reverse_cancel`, `disable_abnormal_invoice_detection` (action layer, 6183).
14. After the state write: `_reconcile_reversed_moves` and `_reconcile_marked` (5775-5776), customer/supplier rank (5778-5794), and for a zero-total move `_invoice_paid_hook` (5796-5799).
15. Deprecated gap helpers: `_set_next_made_sequence_gap` (5803-5805, replaced by `_update_sequence_made_gap` at 5820); `_get_sequence_suffix` 5807.

### D3 State diagram

- draft -> posted [`_post`, stage 13 (5757-5760), requires state draft (5652-5653)]
- draft (auto_post 'no') -> draft (auto_post 'at_date') [soft `_post` with future date (5691-5700)]
- draft (auto_post 'at_date'/'monthly'/...) -> posted [`_autopost_draft_entries` when date <= today (6460-6493)]
- posted -> posted [post of non-draft raises (5652-5653)]
- create with state posted -> refused [3895-3896]

### Ten-dimension analysis

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Draft with partner, dates, lines and a balanced entry; `action_post` -> `_post(soft=False)` -> validations -> state write -> name assigned by compute -> hooks (5583-5801). |
| 2 | Reversal/cancel/negative | Negative total refused for invoice-like moves (5624-5629); reversal posting uses context `move_reverse_cancel`, which stock_account and purchase_stock respect. |
| 3 | Multi-company/data scope | Accounts of another company refused (5673-5679); `_check_company_auto = True` (79). |
| 4 | Side effects/cross-module | Eight extension modules (table above); COGS lines, payment-transaction reconciliation, EDI documents, fleet logs, interco check, email send, peppol response. |
| 5 | Configuration/optionality | Journal `restrict_mode_hash_table`, company lock dates, `auto_post`, `skip_*` context flags. |
| 6 | Validation/constraints | Stage 3 and 4 checks; balanced and lock constraints on write (2782-2840). |
| 7 | Roles/permissions | Group `account.group_account_invoice` at 5583-5584; superuser bypass; ACL rows (see DB reconciliation). |
| 8 | Scheduled/automated | Cron `_autopost_draft_entries` posts due entries (6460-6493); recurring copy at 5711-5713. |
| 9 | Exception/failure | One aggregated UserError (5681-5683); bank trust RedirectWarning (5612-5623); cron falls back to per-move posting and sets `auto_post='no'` on failure (6481-6493). |
| 10 | Accounting/audit/security/compliance | Sequence and date written at post; lock-date adjustment without an error step; hash only for restricted journals; `posted_before` for audit trail. |

### DB reconciliation

Structure-only DB (restored private copy, since cleaned up): account_move had 0 rows; no journal had `restrict_mode_hash_table`; company lock dates were NULL; sale, stock_account, purchase_stock, account_edi were installed; account_fleet, account_payment_interco, product_email_template and account_peppol_response install status is unverified. ACL rows on account.move: group_account_invoice and group_purchase_user full CRUD; manager, readonly, salesman, hr_expense approver and portal read only; 9 ir_rule rows.

### Unknown and runtime list

- Lock-date adjustment under real lock dates and lock exceptions, including future lock dates (RT).
- Multi-move cash-basis branch at 5749 (RT).
- Purchase date adjustment versus sequence reset type (RT).
- Whether the auto-grant of `group_partial_purchase_deductibility` triggers in practice (RT).
- v16/v17 differences of the pipeline: PENDING CLAUDE VERIFICATION (no migrations directory).

## CAP-U238-04 Reset to draft, cancel, hash lock, posted-move write limits and deletion

Function-ID: FUNCTION MAPPING REQUIRED
Claims: C014, C015, C016, C017

### D1 Structure

| Element | Pointer |
|---|---|
| `action_post` | account/models/account_move.py:6180-6201 |
| `_get_moves_requiring_confirmation` / `action_validate_moves_with_confirmation` | account/models/account_move.py:6203-6208 / 6210-6237 |
| `set_moves_checked` | account/models/account_move.py:6265-6267 |
| `button_draft` | account/models/account_move.py:6269-6284 |
| `_check_draftable` | account/models/account_move.py:6348-6373 |
| `_unlink_next_draft_auto_post_moves` | account/models/account_move.py:6319-6346 |
| `_detach_attachments` and helpers | account/models/account_move.py:6286-6317 |
| `button_hash` | account/models/account_move.py:6375-6376 |
| `button_request_cancel` | account/models/account_move.py:6378-6382 |
| `button_cancel` | account/models/account_move.py:6384-6396 |
| `action_toggle_block_payment` | account/models/account_move.py:6398-6406 |
| `write` guards | account/models/account_move.py:3912-4018 |
| `unlink` guards | account/models/account_move.py:4023-4088 |
| Hash fields: `restrict_mode_hash_table` (related journal), `secure_sequence_number`, `inalterable_hash`, `secured` | account/models/account_move.py:353-360 |
| Hash methods | account/models/account_move.py:4592-4803 |

Comparison of the three buttons:

| Aspect | action_post | button_draft | button_cancel |
|---|---|---|---|
| Allowed source state | draft (5652-5653) | cancel or posted (6270-6271) | draft, or posted after an implicit reset (6387-6392) |
| Target state | posted | draft (6280) | cancel (6396) |
| Reconciliations | reconciles reversed and marked moves (5775-5776) | NOT removed (no `remove_move_reconcile` in 6269-6284) | removed with `remove_move_reconcile` (6394) |
| Payments | n/a | untouched | `payment_ids.state = "canceled"` (6395) |
| auto_post | draft -> at_date in soft mode only | Following draft auto-post moves unlinked (6319-6346) | set to 'no' (6396) |
| Analytic lines | created (5709) | unlinked | via reset to draft |
| Attachments | n/a | detached (6296-6317) | via reset to draft |
| Hash | hash at post only for restricted journals | refused for `inalterable_hash` (6372-6373) | goes through button_draft first, so also refused when hashed |
| Lock dates | adjustment (5702-5706) | write-time un-posting lock check (3953-3956) | same via write |
| Refusals | many (CAP-03) | `need_cancel_request` (6272-6273); `_check_draftable` | non-draft/posted refused (6391-6392) |
| Extensions | CAP-03 chain | sale 99-105; stock_account 46-52 | sale 107-118; stock_account 54-62; peppol response 46-51 |

### D2 Behaviour

1. `button_draft` (6269-6284): checks state (6270-6271), `need_cancel_request` (6272-6273), `_check_draftable`; unlinks following draft auto-post moves; unlinks analytic lines; writes `state='draft'` (6280); clears `sending_data`; detaches attachments. It does NOT unlink reconciliations (migration flag; see section on flags).
2. `_check_draftable` (6348-6373): refuses exchange-difference moves (6363-6364), cash-basis related moves (6365-6371) and any move with `inalterable_hash` ("You cannot reset to draft a locked journal entry.", 6372-6373).
3. `button_cancel` (6384-6396): posted moves are first reset via `button_draft` (6387-6389); other non-draft states refused (6391-6392); then `remove_move_reconcile` (6394), payments set canceled (6395), writes `auto_post='no'` and `state='cancel'` (6396).
4. Hash mechanics: `_get_integrity_hash_fields` (4592-4599): version 1 uses date, journal_id, company_id; versions 2-4 add name. `_get_move_hash_domain` 4604-4614; `_is_move_restricted` 4616-4623; `_hash_moves` 4625-4637 (logs "This journal entry has been secured."; grants the secured group via `_activate_group_account_secured`, res_users.py:27-38, when any chain journal is not in restrict mode); `_get_chain_info` 4639-4725 (warnings gap / unreconciled / no_document); `_get_chains_to_hash` 4727-4769 (raises on unreconciled statement lines, no_document, gap); `_calculate_hashes` 4771-4803 (sha256 over previous hash plus sorted JSON of move and line hash fields; `$4$` prefix at version >= 4, 4801). `MAX_HASH_VERSION = 4` (47). `button_hash` uses `force_hash=True` (6375-6376), so it hashes regardless of the journal mode. The group is defined at account/security/account_security.xml:82; the Community wizard is account/wizard/account_secure_entries_wizard.py.
5. Hash is Community-present (not Enterprise only); `secured` is computed with search `_search_secured` (356-360).
6. Posted-move write restrictions (3958-3969): when `move_state == "posted"` (3959, 3964) and no `skip_readonly_check`, modification of nine fields is refused: invoice_line_ids, line_ids, invoice_date, date, partner_id, invoice_payment_term_id, currency_id, fiscal_position_id, invoice_cash_rounding_id. Other header fields (ref, narration, invoice_origin, payment_reference, partner_bank_id, invoice_date_due, invoice_user_id) stay editable unless hash-protected: hash-protected fields are `_get_integrity_hash_fields` plus `inalterable_hash` (3923-3929).
7. Other write rules: journal change refusals (3930-3943); fiscal-lock check on posted name/date change (3945-3951); un-posting lock check (3953-3956); draft name reset (3990-3995); lock checks (3999-4002); hash (4004-4006); `_synchronize_business_models` (4008); constraint recheck (4015-4016). Reviewer guards (3917-3921) are inert in Community: `_is_user_able_to_review` returns True always (7014-7016) and `_compute_checked` makes `checked` True for every posted move (2432-2434).
8. Unlink: `_unlink_forbid_parts_of_chain` (4048-4066) allows deletion for group_account_manager, any company in quick_edit_mode, context `force_delete`, or when the move is last in its chain; `_unlink_account_audit_trail_except_once_post` (4068-4077) forbids deleting a `posted_before` move when the journal is `restrictive_audit_trail`, unless `force_delete`; `unlink` (4079-4088) removes reconciliations then lines. `_can_be_unlinked` (5541-5546), `_is_protected_by_audit_trail` (5548-5549) and `_unlink_or_reverse` (5551-5567) support the delete-or-reverse flow. Logger message at 4023-4046.

### D3 State diagram

- posted -> draft [`button_draft` (6269-6284); refused if `inalterable_hash` (6372-6373)]
- cancel -> draft [`button_draft`]
- draft -> cancel [`button_cancel` (6396)]
- posted -> cancel [`button_cancel` via implicit reset to draft (6387-6389)]
- draft -> (deleted) [`unlink` unless audit-trail refusal (4068-4077)]

### Ten-dimension analysis

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Posted unhashed invoice -> `button_draft` -> edit -> `action_post`. |
| 2 | Reversal/cancel/negative | `button_cancel` removes reconciliations and cancels payments; `button_draft` keeps reconciliations. |
| 3 | Multi-company/data scope | Quick-edit mode of any company relaxes the chain deletion rule (4048-4066). |
| 4 | Side effects/cross-module | sale, stock_account and peppol response extend draft/cancel; attachments detached. |
| 5 | Configuration/optionality | Journal restrict hash and audit-trail flags; context `force_delete`, `skip_readonly_check`. |
| 6 | Validation/constraints | `_check_draftable`, nine unmodifiable fields, hash-protected fields. |
| 7 | Roles/permissions | Chain deletion by group_account_manager; reviewer guard inert. |
| 8 | Scheduled/automated | Following draft auto-post moves are unlinked on reset (6319-6346). |
| 9 | Exception/failure | Hash chain errors on gap, unreconciled statement lines, missing document (4727-4769). |
| 10 | Accounting/audit/security/compliance | Hash chain integrity, `posted_before` audit trail, lock dates block un-posting. |

### DB reconciliation

No journal had `restrict_mode_hash_table` in the structure-only DB; ACL on account.move: invoice group and purchase user full CRUD, others read only.

### Unknown and runtime list

- Reset to draft of a posted move that is still reconciled (RT).
- Hash chain behaviour with restrict mode enabled (RT; none enabled in the DB).
- Audit-trail deletion behaviour at runtime (RT).

## CAP-U238-05 Header dates, references, parties, bank, currency and journal consistency

Function-ID: FUNCTION MAPPING REQUIRED
Claims: C018, C019, C020, C021, C022

### D1 Structure

| Field | Declaration | Compute / inverse | Notes |
|---|---|---|---|
| `invoice_date` | account_move.py:375 | none (user-set; set by `_post` for sale documents, 5642-5648) | `copy=False`, indexed |
| `date` | account_move.py:123 | `_compute_date` 861-876 | accounting date; see CAP-U238-03 |
| `invoice_date_due` | account_move.py:380 | `_compute_invoice_date_due` 1091-1098 (depends `needed_terms`) | stored, `copy=False`; max of term maturities, else existing value, else today |
| `invoice_payment_term_id` | account_move.py:406 | `_compute_invoice_payment_term_id` 1080-1089; inverse 2642-2646 | sale incl. receipts: partner `property_payment_term_id`; purchase incl. receipts: `property_supplier_payment_term_id`; others False; precompute |
| `delivery_date` | account_move.py:386 | `_compute_delivery_date` 1100-1101 (`pass`); `_inverse_delivery_date` 2545-2546 (`pass`) | populated only by sale_stock (sale_stock/models/account_move.py:117-127; draft only; max `effective_date` of linked sale orders) |
| `show_delivery_date` | account_move.py:395 | 1103-1106 | `delivery_date` and `is_sale_document()` |
| `taxable_supply_date` | account_move.py:396 | `_compute_taxable_supply_date` 1108-1109 (`pass`) | hook stub; also in `_compute_date` depends (861) and currency-rate depends (1143, 1151) |
| `show_taxable_supply_date`, `taxable_supply_date_placeholder` | account_move.py:404-405 | 1111-1117 | constant False / empty string |
| `ref` | account_move.py:117 | none | vendor reference; part of duplicate detection |
| `payment_reference` | account_move.py:468 | `_compute_payment_reference` 843-850; inverse 2636-2640 | only computed for posted `out_invoice` without a value, via `_get_invoice_computed_reference` (4408-4413) from journal `invoice_reference_model` / `invoice_reference_type`; UserError when the combination is not implemented |
| `invoice_origin` | account_move.py:695 | none | `readonly=True`, `copy=False`, tracking |
| `partner_id` | account_move.py:420 | inverse `_inverse_partner_id` 2598-2605 | tracking, `ondelete='restrict'`, `check_company` |
| `commercial_partner_id` | account_move.py:431 | `_compute_commercial_partner_id` 1022-1025 | stored; `partner_id.commercial_partner_id` |
| `partner_shipping_id` | account_move.py:438 | `_compute_partner_shipping_id` 1027-1034 | invoice-like (incl. receipts): partner `address_get(['delivery'])`; others False |
| `bank_partner_id` | account_move.py:739 | `_compute_bank_partner_id` 1923-1928 | technical, non-stored; inbound moves use the company partner, other moves the commercial partner (1925-1928) |
| `partner_bank_id` | account_move.py:445 | `_compute_partner_bank_id` 1052-1078 | see D2 |
| `fiscal_position_id` | account_move.py:457 | `_compute_fiscal_position_id` 1036-1050 | `in_receipt` uses company `account_purchase_receipt_fiscal_position_id`; otherwise `_get_fiscal_position(partner, delivery=...)` |
| `company_currency_id` | account_move.py:522 | related `company_id.currency_id` | |
| `currency_id` | account_move.py:526 | `_compute_currency_id` 1119-1128; inverse 2618-2623 | required, tracking; order: statement-line foreign currency, journal currency, current value, company currency |
| `expected_currency_rate` | account_move.py:533 | 1143-1149 | rate at `_get_invoice_currency_rate_date` (1130-1132: `invoice_date` or today) |
| `invoice_currency_rate` | account_move.py:537 | 1151-1155 | invoice-like (incl. receipts): equals expected rate |
| `journal_id` | account_move.py:162 | `_compute_journal_id` 897-900; helper 902-938; inverse 2625-2634 | see D2 |
| `company_id` | account_move.py:176 | `_compute_company_id` 891-895; inverse 2607-2616 | see D2 |
| `invoice_user_id` | account_move.py:684 | stored, editable | not frozen after posting (see CAP-U238-04) |
| `delivery_date` extension in sale_stock | sale_stock/models/sale_order.py:301 | sets `delivery_date` into invoice values from `effective_date` | |

Constraints on the header (account/models/account_move.py):

| Constraint | Lines | Rule |
|---|---|---|
| `_require_bill_date_for_autopost` | 2842-2847 | auto_post != 'no' on a purchase document without invoice_date -> ValidationError |
| `_check_journal_move_type` | 2849-2855 | purchase document (incl. receipts) needs journal type purchase; sale document (incl. receipts) needs journal type sale |
| `_validate_taxes_country` | 2857-2870 | taxes of another country than fiscal country / fiscal position -> ValidationError |
| `_check_invoice_currency_rate` | 2872-2883 | invoice-like with a currency different from the company currency needs `invoice_currency_rate > 0` |

Duplicate detection: `_compute_duplicated_ref_ids` 2078-2083 (depends ref, move_type, partner_id, invoice_date, tax_totals, currency_id); `_fetch_duplicate_reference` 2085-2185; `_compute_is_draft_duplicated_ref_ids` 2187-2199.

### D2 Behaviour

1. `date` for invoice-like moves follows `invoice_date` (861-876): sale documents take `invoice_date` as is; purchase documents pass through `_get_accounting_date` at compute time (869-870). Entries default to today when empty (866-868).
2. `invoice_date_due`: when `needed_terms` has keys it is the latest `date_maturity`; otherwise the existing value, otherwise today (1091-1098). `_compute_needed_terms` (1388-1457; detail in CAP-U238-07) uses `invoice_date or date or today` as the term reference date (1419).
3. `partner_bank_id` (1052-1078): for inbound moves with a preferred payment method line (or the partner's inbound method line) whose journal has a bank account, that journal bank account is used (1066-1073); otherwise the first active partner bank of `bank_partner_id` filtered by company, sorted by currency match (same currency or no currency first) and `allow_out_payment` (1054-1063, 1075-1078).
4. `fiscal_position_id` (1036-1050): delivery partner is `partner_shipping_id`, falling back to the partner's delivery address.
5. `commercial_partner_id` is the stored commercial entity of `partner_id`; `_post` aligns line partners to the commercial partner (5715-5723) and `_inverse_partner_id` (2598-2605) pushes the commercial partner onto lines for invoice-like moves. `partner_id` is also one of the nine fields frozen after posting (3958-3969).
6. Duplicate detection (2085-2185) applies to sale and purchase documents without receipts (2086). Used fields: company, partner, commercial partner, ref, move_type, invoice_date, state, amount_total, currency. Matching states default to draft and posted. Out documents (out_invoice/out_refund): same amount_total and invoice_date (2120-2126). In documents (in_invoice/in_refund): same ref and (null date or same year), or different ref with same commercial partner, same non-zero total and same invoice_date (2131-2154). Same company, move_type and currency, and same commercial partner (or a null commercial partner against a draft) in all cases (2163-2172). Results are filtered by read access (2183). `is_exact_move_duplicate` is only true for purchase documents (2191-2199).
7. Currency: `_compute_currency_id` (1119-1128) and `_inverse_journal_id` (2625-2634) re-trigger company and currency compute when journal and company/currency disagree. Rate fields depend on `invoice_date` and `taxable_supply_date`; `_post` protects a manually set `invoice_currency_rate` when it differs from `_get_expected_currency_rate_at(create_date.date())` (5642-5648).
8. Journal and company: `_compute_company_id` (891-895) sets the company to the journal company's first accessible branch when the journal company is not among the move's company parents. `_compute_journal_id` (897-900) searches a default journal only when the current journal type is not valid; valid types are `sale` for sale documents (incl. receipts), `purchase` for purchase documents (incl. receipts), bank/cash/credit for payment/statement moves and `general` otherwise (902-909). `_search_default_journal` (911-938) prefers the statement journal, then a journal matching the move currency when it differs from the company currency, then any journal of the valid types of the company; raises UserError when none exists (934-936). `_inverse_company_id` (2607-2616) refuses an empty company and recomputes the journal when it does not match the company.
9. `payment_reference` is computed only for posted `out_invoice` records without a value (843-850); its inverse refreshes the names of payment-term lines (2636-2640). `sanitize_payment_reference` strips non-alphanumeric characters (852-855).
10. `invoice_origin` is read-only in the model and not copied. `purchase` reads it to link purchase orders (`_link_bill_origin_to_purchase_orders`, 5919-5923). The purchase module declares `purchase_vendor_bill_id` and `purchase_id` as non-stored helper Many2one fields and `purchase_order_count` / `purchase_order_name` / `is_purchase_matched` as computed fields (purchase/models/account_invoice.py:19-27). The sale module adds `team_id`, UTM fields and `sale_order_count` (sale/models/account_move.py:10-20).

### D3 State diagram

Header editability follows the move state: all header fields are editable in draft; in posted state nine fields are blocked (CAP-U238-04). Reference states: `delivery_date` populated only while the move is draft (sale_stock 121-122).

### Ten-dimension analysis

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Partner chosen -> fiscal position, payment term, shipping address and bank computed -> `invoice_date` -> `date`, rate and due date follow. |
| 2 | Reversal/cancel/negative | A refund keeps the partner of the original (5514-5518); duplicate detection includes refund types. |
| 3 | Multi-company/data scope | `_compute_company_id` picks an accessible branch; `check_company` on partner, bank, fiscal position, term; duplicates matched within a company (2164). |
| 4 | Side effects/cross-module | sale_stock fills `delivery_date`; purchase links `invoice_origin` to purchase orders; sale adds team and UTM fields. |
| 5 | Configuration/optionality | Company `account_purchase_receipt_fiscal_position_id`; journal reference model/type; partner term properties; `taxable_supply_date` and delivery-date hooks are stubs in the base model. |
| 6 | Validation/constraints | Four constraints above plus post-time checks in CAP-U238-03. |
| 7 | Roles/permissions | No header-specific group in these methods (RT for field-level groups). |
| 8 | Scheduled/automated | Recurring copies shift `invoice_date` and due date (4854-4870). |
| 9 | Exception/failure | UserError when no journal exists (934-936); UserError for unimplemented reference model/type (4410-4412); ValidationError for empty company (2612-2613). |
| 10 | Accounting/audit/security/compliance | `invoice_currency_rate` positive; duplicate warning is advisory (a computed field), not a constraint (OBSERVATION). |

### DB reconciliation

Structure-only DB: account_move had 0 rows. Selection counts: move_type 7, state 3, payment_state 7, status_in_payment 11, auto_post 5. No business data was queried.

### Unknown and runtime list

- Duplicate detection runtime (RT): whether it blocks anything (it only warns; blocking in the cron path is via `_autopost_bill`, 5936-5937).
- Whether any accounting-app extension fills `taxable_supply_date` (UNKNOWN; not in Community).
- Currency rate fallback when no rate row exists (RT).
- Differences versus v16/v17 are PENDING CLAUDE VERIFICATION.

## CAP-U238-06 Auto-post, recurring entries and reversal summary

Function-ID: SDV-F07 (reversal summary, C024); FUNCTION MAPPING REQUIRED (C023)
Claims: C023, C024

### D1 Structure

| Element | Pointer |
|---|---|
| `auto_post` selection (no, at_date, monthly, quarterly, yearly), default 'no', required, `copy=False` | account/models/account_move.py:294-304 |
| `auto_post_until` / `auto_post_origin_id` | account/models/account_move.py:305 / 310 |
| `hide_post_button`, `_compute_hide_post_button` | account/models/account_move.py:316; 884-889 |
| `_compute_auto_post_until` (cleared for 'no'/'at_date') | account/models/account_move.py:878-882 |
| `_apply_delta_recurring_entries` | account/models/account_move.py:4809-4814 |
| `_copy_recurring_entries` | account/models/account_move.py:4816-4852 |
| `_get_fields_to_copy_recurring_entries` | account/models/account_move.py:4854-4870 |
| `_autopost_draft_entries` (cron) | account/models/account_move.py:6460-6493 |
| `_autopost_bill` | account/models/account_move.py:5925-5939 |
| `_show_autopost_bills_wizard` | account/models/account_move.py:5941-5978 |
| `_link_bill_origin_to_purchase_orders` | account/models/account_move.py:5919-5923 |
| Company `autopost_bills` (default True) / partner `autopost_bills` | account/models/company.py:269 / account/models/partner.py:610 |
| `TYPE_REVERSE_MAP` | account/models/account_move.py:59-67 |
| `_reconcile_reversed_moves` | account/models/account_move.py:5474-5492 |
| `_reverse_moves` | account/models/account_move.py:5495-5539 |
| `_set_reversed_entry` | account/models/account_move.py:7388-7396 |
| `reversed_entry_id` / `reversal_move_ids` | account/models/account_move.py:629 / 637 |
| sale reverse extension | sale/models/account_move.py:71-81 |

### D2 Behaviour

1. Cron `_autopost_draft_entries(batch_size=100)` (6460-6493): searches draft moves with `date <= today` and `auto_post != 'no'` (6465-6469), then calls `moves._post()` in soft mode for the whole batch (6475). On UserError it rolls back and retries move by move with `try_lock_for_update` (6481-6486); a failing move gets a chatter message and `auto_post = 'no'` (6488-6493). Progress is committed through `ir.cron._commit_progress`.
2. Recurring copy: after posting a move with `auto_post` not in (no, at_date), `_post` calls `_copy_recurring_entries` (5711-5713). The first move becomes its own `auto_post_origin_id` (4823); the next date is origin date + period months (4810-4814); the copy is skipped when beyond `auto_post_until` (4826) or when a move with the same origin and date exists (4837-4851). Copied extra fields: auto_post, auto_post_until, auto_post_origin_id, invoice_user_id, shifted invoice_date, due date shift when there is no payment term (4854-4870).
3. Vendor-bill auto-post (`_autopost_bill`, 5925-5939): requires company `autopost_bills`, a partner with `autopost_bills == 'always'`, a purchase document (incl. receipts), no abnormal amount warning, and no hash restriction; with a duplicate reference it only posts a chatter message and does not post (5936-5937), otherwise `action_post` is called (5939). `_show_autopost_bills_wizard` (5941-5978) offers the wizard (partner setting 'ask') after at least three unmodified bills (5960-5966), a single posted purchase document, imported lines, not manually modified.
4. `_require_bill_date_for_autopost` (2842-2847) requires a bill date for auto-posted purchase documents.
5. Hard post of a move with `auto_post != 'no'` and a future date is refused (5656-5658); soft post sets 'at_date' for future moves (5691-5700).
6. Reversal: `TYPE_REVERSE_MAP` (59-67) maps out_invoice -> out_refund, in_invoice -> in_refund, out_receipt -> out_refund (65), in_receipt -> in_refund (66), entry -> entry. CONTRA: prior unit U79 claim U79-047 describes receipts as reversing into each other (out_receipt <-> in_receipt); the code at lines 65-66 maps both receipts to refunds.
7. `_reverse_moves(default_values_list, cancel)` (5495-5539): when `cancel` is true, `remove_move_reconcile` runs on all lines first (5506-5510). Each original is copied with context `move_reverse_cancel=cancel`, `include_business_fields=True` and `skip_invoice_sync` for entries, with `move_type` from `TYPE_REVERSE_MAP`, `reversed_entry_id` and the partner (5513-5523). For entry-type moves and COGS lines the balance and amount_currency are negated, and `is_storno` toggled when the company uses storno (5525-5533). With `cancel` the reverses are posted immediately with `_post(soft=False)` (5536-5537); without it they stay draft (reversal wizard behaviour is out of scope). `_reconcile_reversed_moves` reconciles unreconciled lines per account/currency when the account is reconcilable or cash/credit-card (5474-5492); it is called from `_post` (5775).
8. Sale extension of `_reverse_moves` (sale/models/account_move.py:71-81) copies `campaign_id`, `medium_id` and `source_id` from the original to the reverse; sale `action_post`, `button_draft` and `button_cancel` (83-118) recompute the name and price unit of down-payment sale-order lines linked to the move (field names and link semantics only).
9. Credit-note immutability and refund policy are covered by U122; lock/sequence by U114; lifecycle by U79. This capability only records the header-level summary.

### D3 State diagram

- draft (auto_post at_date/monthly/quarterly/yearly) -> posted [cron when date <= today (6465-6475)]
- draft (cron failure) -> draft (auto_post 'no') [6488-6493]
- posted (recurring) -> new draft copy [`_copy_recurring_entries` (4816-4852)]
- posted original -> original + reverse (draft or posted) [`_reverse_moves` (5495-5539)]

### Ten-dimension analysis

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Recurring entry posts at its date by cron, spawns the next copy. |
| 2 | Reversal/cancel/negative | `_reverse_moves` with and without `cancel`; negated balances only for entries and COGS lines (5532); invoice lines are re-derived from the refund type. |
| 3 | Multi-company/data scope | Cron runs over all companies visible to the cron user (RT). |
| 4 | Side effects/cross-module | sale and stock_account respect `move_reverse_cancel` (CAP-U238-03); stock_account `copy_data` (18-27) and sale `_reverse_moves`. |
| 5 | Configuration/optionality | `autopost_bills` on company (default True) and partner; `auto_post_until`. |
| 6 | Validation/constraints | Bill date constraint; hard post refusal for future auto-post moves. |
| 7 | Roles/permissions | Cron posts as the cron user; `_post` access guard still applies (5583-5584). |
| 8 | Scheduled/automated | The cron body above; the cron record itself was not read (UNKNOWN). |
| 9 | Exception/failure | Batch rollback and per-move fallback; failure disables auto-post and logs to the chatter. |
| 10 | Accounting/audit/security/compliance | Failure messages are kept in the chatter; duplicates block auto-post with a message. |

### DB reconciliation

Selection count for auto_post is 5. No move rows existed; cron scheduling not checked (UNKNOWN).

### Unknown and runtime list

- Cron schedule and user (UNKNOWN; data file not read).
- Recurrence copy runtime and day-of-month clamping (RT).
- Reversal without cancel followed by manual post (RT).
- Whether `account_debit_note` (not installed) alters `_reverse_moves` (UNKNOWN).

## CAP-U238-07 Line synchronisation hooks from the header (pointers only)

Function-ID: FUNCTION MAPPING REQUIRED
Claims: C025

### D1 Structure

| Element | Pointer |
|---|---|
| `line_ids` | account/models/account_move.py:182 |
| `journal_line_ids` (deprecated) | account/models/account_move.py:190 |
| `invoice_line_ids` (subset of `line_ids`; domain product, line_section, line_subsection, line_note) | account/models/account_move.py:366-372 |
| `needed_terms` / `needed_terms_dirty` | account/models/account_move.py:413-414 |
| `_compute_needed_terms` | account/models/account_move.py:1388-1457 |
| `_sync_invoice` | account/models/account_move.py:3698-3720 |
| `_get_sync_stack` | account/models/account_move.py:3722-3764 |
| `_sync_dynamic_lines` | account/models/account_move.py:3767-3784 |
| `_get_default_read_fields` | account/models/account_move.py:3800-3802 |

### D2 Behaviour

1. `invoice_line_ids` is explicitly "just a subset of `line_ids`" (366): it holds product and note-like lines, while tax, payment-term, rounding, discount and EPD lines exist only in `line_ids`.
2. `_get_sync_stack` (3722-3764) returns an ordered stack: 10 payment-term lines (`term_key`, `needed_terms`), 20 unbalanced lines for entries, 30 rounding lines, 40 discount allocation, 50 tax lines, 60 non-deductible base lines, 70 early-payment-discount lines, 80 `_sync_invoice`. Tax container covers invoice-like moves and entries with taxes (3727); invoice container invoice-like moves (3728); misc container plain entries excluding cash-basis moves (3729).
3. `_compute_needed_terms` (1388-1457) depends on payment term, invoice_date, currency, `amount_total_in_currency_signed` and `invoice_date_due`. For invoice-like moves with invoice lines: with a payment term, the term amounts come from `invoice_payment_term_id._compute_terms` (1418-1428) using, for a draft/new record, amounts rebuilt from `_get_rounded_base_and_tax_lines` and the tax engine (1399-1412), otherwise the stored `amount_tax`/`amount_untaxed` signed values (1413-1417); terms are keyed by `move_id`, `date_maturity`, `discount_date` (1430-1434) and equal keys are summed (1442-1446). Without a payment term, a single term at `invoice_date_due` carries the signed total (1447-1457).
4. Detail of payment-term line generation and discount rounding belongs to U204/U212; tax lines to U224. Not duplicated here.
5. Deprecated `journal_line_ids` (190-197) is kept for compatibility (migration flag).

### D3 State diagram

Not applicable (no state transition).

### Ten-dimension analysis

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Invoice lines edited -> sync stack regenerates payment-term, rounding, tax lines -> totals recomputed. |
| 2 | Reversal/cancel/negative | `skip_invoice_sync` context used by `_reverse_moves` (5522, 5525). |
| 3 | Multi-company/data scope | Not specific; lines inherit company. |
| 4 | Side effects/cross-module | sale/purchase link lines to orders (field names only). |
| 5 | Configuration/optionality | Cash rounding method and payment term drive rounding and term lines. |
| 6 | Validation/constraints | `_check_balanced` (2782-2799) after sync. |
| 7 | Roles/permissions | None in these methods. |
| 8 | Scheduled/automated | None. |
| 9 | Exception/failure | Not studied beyond pointers. |
| 10 | Accounting/audit/security/compliance | Posted moves block edits to `line_ids` and `invoice_line_ids` (3958-3969). |

### DB reconciliation

Not applicable (code-only pointers).

### Unknown and runtime list

- Interaction of the sync stack with `needed_terms_dirty` under concurrent edits (RT).
- Full behaviour belongs to U204 and U212 (pointer only).

## CAP-U238-08 Thai localisation at header level (l10n_th)

Function-ID: FUNCTION MAPPING REQUIRED
Claims: C026

### D1 Structure

`l10n_th` is PRESENT in Community with 19 files (directory listing taken in this session):

| Path (relative to addons root) | Header relevance |
|---|---|
| l10n_th/models/account_move.py | Only account.move override: `_get_name_invoice_report` (lines 7-11) |
| l10n_th/models/res_partner.py, res_bank.py, ir_actions_report.py, template_th.py | Partner / bank / report / chart-template level (not read in depth) |
| l10n_th/views/report_invoice.xml | Invoice report document |
| l10n_th/data/account_tax_report_data.xml and data/template/*.csv | Tax report and chart data (accounts, tax groups, taxes, assets) |
| l10n_th/demo/demo_company.xml, tests/*, i18n/*, __manifest__.py, __init__.py | Demo, tests, translations, packaging |

### D2 Behaviour

1. The only account.move override returns the report template `l10n_th.report_invoice_document` when the company's fiscal country code is TH, otherwise the parent value (l10n_th/models/account_move.py:7-11).
2. No tax-invoice-number field, branch field or withholding-tax hook is declared on account.move by `l10n_th`: the directory listing above contains no such model file and the only move override is the report-name method. ABSENT in Community (INFERENCE from the listing and the file read).
3. Withholding-tax data exists only as data files (tax and tax-group CSV); no WHT method on the move.
4. Thai tax invoice header concepts (tax invoice number, branch) must therefore be handled by sequence configuration (U114), report layout, or Extra modules outside Community scope.

### D3 State diagram

Not applicable.

### Ten-dimension analysis

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | A TH-company invoice prints with the Thai report template. |
| 2 | Reversal/cancel/negative | No Thai-specific refund logic on the move. |
| 3 | Multi-company/data scope | Selected by company fiscal country (line 9). |
| 4 | Side effects/cross-module | Report only. |
| 5 | Configuration/optionality | Chart template and tax data; no header toggles. |
| 6 | Validation/constraints | None on the move. |
| 7 | Roles/permissions | None. |
| 8 | Scheduled/automated | None. |
| 9 | Exception/failure | None. |
| 10 | Accounting/audit/security/compliance | Tax-invoice numbering and WHT certificates are not provided on the header in Community (ABSENT). |

### DB reconciliation

l10n_th was installed in the structure-only DB; no account.move fields beyond the base model were observed.

### Unknown and runtime list

- Whether partner-level branch field (non-stored) is used on printed invoices (not read; UNKNOWN).
- Behaviour with real Thai tax data (RT).

## Migration flags (v16 / v17 to v19)

The source tree contains no `account/migrations` directory, so every comparison with v16/v17 is INFERENCE / PENDING CLAUDE VERIFICATION. Facts below are about v19 code only.

| # | Flag | v19 evidence | Kind |
|---|---|---|---|
| M01 | `status_in_payment` is a new non-stored 11-value selection | account_move.py:613-622; `_compute_status_in_payment` 1329 | ADDED field |
| M02 | `payment_state` has `blocked` and `invoicing_legacy` values; no Python producer of `invoicing_legacy` was found in Community | account_move.py:49-57 | ADDED/CHANGED values |
| M03 | `taxable_supply_date`, `delivery_date` and the `show_*` / placeholder fields are hook stubs in the base model; `_inverse_delivery_date` is a no-op; only sale_stock fills `delivery_date` | account_move.py:386-405, 1100-1117, 2545-2546; sale_stock/models/account_move.py:117-127 | ADDED fields |
| M04 | `amount_total_words` | account_move.py:623-626, 2218 | ADDED field |
| M05 | `alerts` field | account_move.py:774 | ADDED field |
| M06 | `line_subsection` display type in `invoice_line_ids` domain and in `_post` empty-move check | account_move.py:371, 5654 | ADDED value |
| M07 | `is_storno` | account_move.py:161, 940-944 | ADDED / kept field |
| M08 | `preferred_payment_method_line_id` drives `partner_bank_id` for inbound moves | account_move.py:513-519, 1066-1073 | ADDED field |
| M09 | `secured` computed field with search on `inalterable_hash` | account_move.py:356-360 | ADDED field |
| M10 | `button_draft` does not unlink reconciliations (only `button_cancel` does) | account_move.py:6269-6284, 6394 | BEHAVIOUR |
| M11 | `journal_line_ids` deprecated | account_move.py:190-197 | DEPRECATED |
| M12 | `_compute_made_sequence_gap` and `_set_next_made_sequence_gap` deprecated; `_update_sequence_made_gap` replaces | account_move.py:985-987, 5803-5805, 5820 | DEPRECATED / ADDED method |
| M13 | `invoice_currency_rate` must be strictly positive for foreign-currency invoices | account_move.py:2872-2883 | ADDED constraint |
| M14 | `tax_totals` computed through the tax-totals summary engine | account_move.py:1836-1843 | CHANGED source |
| M15 | Non-deductible display types and auto-grant of `group_partial_purchase_deductibility` to the posting user | account_move.py:5762-5773 | ADDED behaviour |
| M16 | Deprecated `check_field_access_rights` and `_prepare_invoice_aggregated_taxes` | account_move.py:3790-3797, 4961-4984 | DEPRECATED |
| M17 | Hash `$4$` prefix (hash version 4); `MAX_HASH_VERSION = 4` | account_move.py:47, 4801 | CHANGED |
| M18 | `_check_draftable` refuses locked (hashed) entries and certain cash-basis / exchange-difference moves | account_move.py:6348-6373 | BEHAVIOUR |
| M19 | `_get_invoice_in_payment_state` returns 'paid' in Community | account_move.py:7366-7371 | BEHAVIOUR |
| M20 | Context `disable_abnormal_invoice_detection`; abnormal-amount wizard off by default | account_move.py:6183 | BEHAVIOUR |
| M21 | Duplicate detection covers sale and purchase documents with out/in-specific rules | account_move.py:2085-2185 | BEHAVIOUR |
| M22 | `debit_origin_id` lives in the uninstalled `account_debit_note` module | account_debit_note (not installed) | MOVED field |
| M23 | `_is_user_able_to_review` always True and `checked` always True for posted moves in Community | account_move.py:7014-7016, 2432-2434 | BEHAVIOUR |
| M24 | `payment_ids` declared in account_payment.py rather than account_move.py | account/models/account_payment.py:1250 | MOVED field |
| M25 | Lock dates split into soft fields, hard lock and exceptions; `_get_violated_lock_dates` includes the hard lock | company.py:607-740 | CHANGED configuration |
| M26 | Vendor-bill auto-post through company and partner `autopost_bills` | company.py:269; partner.py:610; account_move.py:5925-5939 | ADDED configuration |
| M27 | Vendor-bill accounting date derived from `invoice_date` via `_get_accounting_date` at compute time | account_move.py:861-876, 6714-6751 | CHANGED behaviour |
| M28 | `TYPE_REVERSE_MAP` sends receipts to refund types | account_move.py:65-66 | BEHAVIOUR |
| M29 | Sale `_post` extension auto-reconciles payment-transaction payments | sale/models/account_move.py:126-132 | BEHAVIOUR |

## DISCOVERED SUPPORTING MODULES

| Module | Role for the header model | Evidence |
|---|---|---|
| sale | `_post`, `_reverse_moves`, `action_post`, `button_draft`, `button_cancel`, `_invoice_paid_hook`; team and UTM fields | sale/models/account_move.py |
| purchase | helper fields `purchase_id` etc.; purchase-order matching | purchase/models/account_invoice.py |
| stock_account | COGS lines before post; `copy_data`; draft/cancel overrides | stock_account/models/account_move.py |
| purchase_stock | anglo-saxon lines after post | purchase_stock/models/account_invoice.py:113-117 |
| sale_stock | `delivery_date` population | sale_stock/models/account_move.py:117-127 |
| account_payment | declares `payment_ids` | account/models/account_payment.py:1250 |
| account_edi | EDI documents on post | account_edi/models/account_move.py:233-265 |
| account_fleet | fleet log services on post | account_fleet/models/account_move.py:9-29 |
| account_payment_interco | interco clearing check on post | account_payment_interco/models/account_move.py:30-37 |
| product_email_template | send on validate | product_email_template/models/account_move.py:25-29 |
| account_peppol_response | approval response on post; cancel override | account_peppol_response/models/account_move.py:41-51 |
| account_debit_note | NOT installed; owns `debit_origin_id` | not read |
| l10n_th | report-name override only | l10n_th/models/account_move.py:7-11 |

Installed but not studied in depth: account_check_printing, account_qr_code_emv, account_qr_code_sepa, purchase_requisition, sale_purchase, sale_management. Install status of account_fleet, account_payment_interco, product_email_template and account_peppol_response is UNVERIFIED.

## Contradictions with prior units

| Item | Prior statement | v19 code | Treatment |
|---|---|---|---|
| Receipt reversal mapping | U79-047: out_receipt reverses to in_receipt and vice versa | `TYPE_REVERSE_MAP` maps out_receipt to out_refund and in_receipt to in_refund (account_move.py:65-66) | CONTRA recorded on C024 |

## Relationship to prior units

| Unit | Scope | Treatment in U238 |
|---|---|---|
| U204 | Line-level (account.move.line) | Not duplicated; pointer only (CAP-U238-07) |
| U212 | Payment terms | Pointer only; header due-date interplay recorded (C018, C025) |
| U224 | Tax engine | Pointer only; `tax_totals` source recorded (C008) |
| U114 | Sequence and lock | Trigger and lock-date adjustment recorded from the header view only (C010, C011) |
| U79 | Lifecycle | Confirmed and extended (C014 to C017, C023); CONTRA on C024 |
| U122 | Credit-note immutability | Reversal summary only (C024) |
| U11, U12, U33 | Earlier account.move work | Extended (C005, C015, C016, C017, C019, C023, C025) |

## Runtime-test (RT) list

1. payment_state transitions with real reconciliations (C004).
2. Effect of resetting a reconciled posted move to draft (C014).
3. Hash chain behaviour with `restrict_mode_hash_table` enabled (C015).
4. Lock-date adjustment under real lock dates, exceptions and future lock dates (C010).
5. Multi-move cash-basis branch at account_move.py:5749 (C012).
6. Duplicate-detection and auto-post cron runtime (C019, C023).
7. Producer of the `invoicing_legacy` payment_state value (C004).
8. Whether an accounting-app override of `_get_invoice_in_payment_state` exists (UNKNOWN; accounting app not in Community).
9. Rounding with cash rounding or foreign currency (C006, C021).
10. Payment-transaction auto-reconciliation inside sale `_post` (C013).

## Quality-gate note

Checker outputs recorded verbatim (local checker, run on this F1 plus its neutral file F2):

- Full pair (F1 + F2 as committed): `claims=26 supported_pointer_and_anchor=26 unknown_class=0 neutral_ids=26` then `FAIL claim-checks=0 neutral-leak-tokens=96`.
- The 96 leak tokens all originate from the Pointer and Anchor columns of the F2 claims table (snake_case names, file extensions, path-like tokens, a code keyword). The Neutral-ref column and the F2 narrative contain none.
- Narrative-only variant (F2 lines 1-77 without the table, scratch copy): `claims=26 supported_pointer_and_anchor=26 unknown_class=0 neutral_ids=26` then `FAIL claim-checks=0 neutral-leak-tokens=0`.
- Clean synthetic baseline pair (scratch, 26 rows): the same `FAIL claim-checks=0` line, so a FAIL with claim-checks=0 is produced independently of this unit's content.
- No Gate PASS statement is made in this file. The packet field gate is set to GREEN as required by the work order only.
- Open decision for the reviewer: keep the F2 claims table (leak count 96 disclosed above) or strip it from F2 so a whole-file scan reports zero leak tokens.

## Claims register

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U238-C001 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:143 | move_type | FACT | always | — | The move type selection has seven values (entry, out_invoice, out_refund, in_invoice, in_refund, out_receipt, in_receipt) with default entry; type helper methods classify them | N-U238-001 |
| VDR-U238-C002 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:134 | Cancelled | FACT | always | — | The state selection has three values (draft, posted, cancel), is read-only and tracked with default draft; creation with state posted is refused | N-U238-002 |
| VDR-U238-C003 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:49 | PAYMENT_STATE_SELECTION | FACT | always | — | The payment state selection has seven values and is shared by the stored payment state and the new status in payment field | N-U238-003 |
| VDR-U238-C004 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1234 | def _compute_payment_state | INFERENCE | invoice-like moves with reconciled lines | RT | Payment state is derived from the reconciliation of receivable and payable lines with an in-payment split in Community and a legacy value without a Python producer; blocking toggles a separate flag | N-U238-004 |
| VDR-U238-C005 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1329 | def _compute_status_in_payment | FACT | always | — | The status in payment field is non-stored, has eleven values and combines state and payment state for display | N-U238-005 |
| VDR-U238-C006 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1180 | def _compute_amount | FACT | always | — | Untaxed, tax, total and residual amounts in document and company currency are derived by classifying lines by display type | N-U238-006 |
| VDR-U238-C007 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1158 | def _compute_direction_sign | FACT | always | — | The direction sign is plus one for entries and outbound types and minus one otherwise, and drives the signed amount fields | N-U238-007 |
| VDR-U238-C008 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1836 | def _compute_tax_totals | FACT | always | — | The tax totals structure is produced from rounded base and tax lines through the tax-totals summary engine and has an inverse that rewrites tax amounts | N-U238-008 |
| VDR-U238-C009 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5584 | access rights to post an invoice | FACT | posting | — | Posting requires the invoice group unless superuser and collects invoice-level validation problems into one aggregated error | N-U238-009 |
| VDR-U238-C010 | PCO-F01 | account/models/account_move.py:5704 | _get_violated_lock_dates | FACT | posting a move whose date violates a lock date | RT | Posting replaces the accounting date through the lock-date adjustment without raising an error at that step; the hard lock is included in the violated set | N-U238-010 |
| VDR-U238-C011 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:966 | _set_next_sequence | FACT | posted state with a date and no real name | — | Sequence assignment has no explicit call in posting and is triggered by the name compute when the move is no longer draft | N-U238-011 |
| VDR-U238-C012 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5759 | posted_before | FACT | posting | RT | Posting writes state posted together with the posted-before flag and then runs reconciliation of reversed moves, partner rank updates and the zero-total paid hook | N-U238-012 |
| VDR-U238-C013 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:124 | posted = super()._post(soft) | FACT | posting with the extension modules installed | — | Eight installed-module extensions wrap posting to add cost lines, reconciliation of payment transactions, electronic documents, fleet logs, inter-company checks, email sending and approval responses | N-U238-013 |
| VDR-U238-C014 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6269 | def button_draft | INFERENCE | reset to draft or cancel | RT | Reset to draft keeps reconciliations while cancel removes them and cancels payments; hashed entries cannot be reset to draft | N-U238-014 |
| VDR-U238-C015 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4625 | def _hash_moves | FACT | journal in restricted hash mode or explicit hashing | RT | Integrity hashing is present in Community, runs at post only for restricted journals, and chains entries with a version four prefix | N-U238-015 |
| VDR-U238-C016 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3960 | unmodifiable_fields | FACT | writing a posted move | — | Nine header and line fields are blocked on posted moves while other header fields stay editable unless protected by the hash | N-U238-016 |
| VDR-U238-C017 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4069 | _unlink_account_audit_trail_except_once_post | FACT | deleting a move | RT | Deletion is refused for previously posted moves in audit-trail journals and for entries that are not the end of their chain except for privileged cases | N-U238-017 |
| VDR-U238-C018 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:862 | def _compute_date | FACT | always | — | The accounting date follows the invoice date with purchase-side adjustment at compute time, the due date is the latest term maturity, and delivery and taxable supply dates are base hook stubs | N-U238-018 |
| VDR-U238-C019 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2085 | def _fetch_duplicate_reference | FACT | sale and purchase documents | RT | Duplicate detection compares company, partner, type, currency and either amount and date or reference, and only warns | N-U238-019 |
| VDR-U238-C020 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1053 | def _compute_partner_bank_id | FACT | always | — | Commercial partner, shipping address, fiscal position and recipient bank are computed from the partner with inbound moves preferring the payment method journal bank | N-U238-020 |
| VDR-U238-C021 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2873 | _check_invoice_currency_rate | FACT | invoice-like with foreign currency | — | A foreign-currency invoice must have a strictly positive currency rate that defaults to the expected rate at the invoice date | N-U238-021 |
| VDR-U238-C022 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2850 | _check_journal_move_type | FACT | always | — | Sale and purchase documents require a journal of matching type, and company and journal are kept consistent through compute and inverse methods | N-U238-022 |
| VDR-U238-C023 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6460 | def _autopost_draft_entries | FACT | scheduled run | RT | A scheduled job posts due draft entries in batches with per-move fallback, recurring entries copy themselves, and vendor-bill auto-post depends on company and partner settings | N-U238-023 |
| VDR-U238-C024 | SDV-F07 | account/models/account_move.py:5495 | def _reverse_moves | FACT | reversal | CONTRA | Reversal copies the move with the mapped refund type, optionally cancels by reconciliation and posting, and maps both receipt types to refund types | N-U238-024 |
| VDR-U238-C025 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3722 | def _get_sync_stack | FACT | line changes on invoice-like moves | — | Header changes drive an ordered synchronisation stack for term, rounding, discount, tax and invoice lines and invoice lines are a subset of all lines | N-U238-025 |
| VDR-U238-C026 | FUNCTION MAPPING REQUIRED | l10n_th/models/account_move.py:7 | def _get_name_invoice_report | INFERENCE | Thai company | — | The Thai localisation adds only a report template override on the move and provides no tax invoice number, branch or withholding field on the header in Community | N-U238-026 |
