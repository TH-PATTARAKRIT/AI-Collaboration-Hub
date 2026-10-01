# U12 — account_payment_reconcile — RESTRICTED TECHNICAL EVIDENCE

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION


- Unit: U12 — short name `account_payment_reconcile`
- Modules / files owned: within `account` — payments, payment register wizard, payment methods and method lines, reconciliation models (partial/full), exchange-difference entries, reconcile models, bank statements and statement lines, payment terms and early-payment discount, invoice payment-status computation; whole modules `account_payment`, `account_check_printing`, `account_payment_interco`, `payment` (generic framework only); `snailmail_account` skipped (out of scope per assignment).
- Source revision: `19.0.post20260921` (Odoo 19 Community only; root `odoo-19.0.post20260921/odoo/addons`)
- Date of study: 2026-10-01 to 2026-10-02
- Method: static read of source (read-only), configuration-only queries of the restored database. No Odoo execution; anything needing execution is flagged `RT`.
- Edition note (load-bearing for the whole unit): the invoice "in payment" hook returns `paid` in this source tree (no override found in `odoo/addons`), so every statement about invoice status or payment status is for the Community edition without the accounting app. The `in_payment` value exists in the selection but is unreachable here (see CAP-U12-04).
- DISCOVERED SUPPORTING MODULES (read only as far as needed): `sale` (invoice post hook that reconciles transaction payments; paid hook note), `purchase`/`sale_stock` (extra ACL rows on partial reconcile), `payment_custom` and `payment_demo` (installed provider modules, provider rows only), `hr_expense` and `point_of_sale` (call the invoice in-payment hook; not studied), `l10n_latam_check`/`l10n_ar_withholding` (override payment methods; not installed, not studied), `event_booth_sale` (paid hook; not studied).
- Function-IDs: no existing Function-ID from EXISTING_FUNCTION_ID_INDEX_53 matches these capabilities (lock-date interplay is a hand-off to PCO-F01 / unit U11 and is not claimed here). All claims therefore carry `FUNCTION MAPPING REQUIRED`.
- Not in scope / hand-off: entry posting, lock dates, reversal engine (U11); taxes, chart, currency, analytic (U13). Tax cash-basis is noted only where the reconciliation engine hands off to it.


## CAP-U12-01 Payment lifecycle


**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 — Business purpose and process semantics.** A payment is the user-facing record of money coming in from a customer or going out to a vendor. Confirming it creates one posted journal entry with a money-side line on an intermediate "outstanding receipts / outstanding payments" account and a counterpart line on the partner's receivable or payable account. The payment record then tracks whether the money has actually reached or left the bank (`in_process` to `paid`) while invoices are settled through reconciliation (CAP-U12-02, CAP-U12-03). VDR-U12-C001 VDR-U12-C034 VDR-U12-C006 VDR-U12-C007

**D2 — Architecture, data and object relationships.** `account.payment` (own table) points to one `account.move` (`move_id`), and the move points back (`origin_payment_id`, `payment_ids`). Journal items on the move are classified at runtime by account into liquidity, counterpart and write-off lines (`_seek_for_lines`). Payment method line (`account.payment.method.line`, per journal) gives the intermediate (outstanding) account; the partner gives the destination account. Invoices are linked to payments in two ways: through reconciliation (`account.partial.reconcile`) and through the explicit many2many `invoice_ids` / `matched_payment_ids`. VDR-U12-C004 VDR-U12-C042 VDR-U12-C016 VDR-U12-C017 VDR-U12-C043

**D3 — Source, technical and workflow logic.**

State machine (as present in 19, `account.payment.state`):
- `draft -> in_process` [action_post; also any write of `state` in (in_process, paid) generates and posts the entry] VDR-U12-C034 VDR-U12-C026
- `draft -> paid` [action_post when the outstanding account type is `asset_cash`] VDR-U12-C034
- `in_process -> paid` [`_compute_state`: liquidity residual is zero, or liquidity accounts are not reconcilable, or all reconciled invoices are `paid`; also `action_validate`] VDR-U12-C018 VDR-U12-C035
- `paid -> in_process` [`_compute_state` re-evaluation when matching is removed; partial unlink also resets payments without outstanding account] VDR-U12-C018
- `in_process -> rejected` [action_reject; state write only, entry untouched] VDR-U12-C036
- `draft | in_process -> canceled` [action_cancel; button visible only for draft, or in_process and sent] VDR-U12-C037 VDR-U12-C041
- `any -> draft` [action_draft: state draft, entry button_draft] VDR-U12-C038
- `payment move cancelled -> canceled` [account.move.button_cancel marks its payments canceled] VDR-U12-C040

Control flow of confirmation: `action_post` (account) -> state write -> `write()` override: if state in (in_process, paid) and move_id not in vals, `_generate_journal_entry()` for payments without move, then post draft moves -> `_generate_move_vals` -> `_prepare_move_line_default_vals` (liquidity / counterpart / write-off / withholding) -> `account.move.create` -> payment `move_id` set and state `in_process`. Overrides: `account_payment.action_post` (token payments, transaction), `account_check_printing.action_post` (check number for manually sequenced journals) both call `super()`. VDR-U12-C034 VDR-U12-C026 VDR-U12-C031 VDR-U12-C032

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Create draft payment, confirm: entry generated and posted, status in process (or paid for cash-type outstanding account). Entry lines: money side on outstanding account, counterpart on receivable/payable. VDR-U12-C031 VDR-U12-C006 VDR-U12-C007 VDR-U12-C009 |
| 2 | Reversal / cancel / negative | `action_cancel` (draft entry unlinked, posted entry `button_cancel`), `action_draft`, `action_reject` (state only), payment `unlink` (entry reset and deleted, invoice status recomputed). Negative amounts refused by SQL check. VDR-U12-C037 VDR-U12-C038 VDR-U12-C036 VDR-U12-C027 VDR-U12-C002 |
| 3 | Multi-company / data scope | Company computed from journal (branch aware); record rule `company_id in company_ids`; journal and method lines checked with company domain. VDR-U12-C014 VDR-U12-C050 |
| 4 | Side effects / cross-module | Entry creation, invoice payment status recompute on unlink, move tracking forwards state messages to the payment; `account_payment` creates provider transactions for token payments; `account_check_printing` assigns check numbers on post. VDR-U12-C027 VDR-U12-C044 |
| 5 | Configuration / optionality | Payment method line account, journal, partner default methods, company outstanding accounts; `payment_account_id` empty in this DB so Community fallback is used. VDR-U12-C008 VDR-U12-C024 VDR-U12-C013 |
| 6 | Validation / constraints | Non-negative amount, method line required and journal-consistent, move required for non-draft with outstanding account, no amount change with several liquidity lines, duplicate warning. VDR-U12-C002 VDR-U12-C020 VDR-U12-C021 VDR-U12-C029 VDR-U12-C022 |
| 7 | Roles / permissions | ACL: Invoicing group full CRUD on payments, readonly group read; record rule company only; reset-to-draft button restricted to Invoicing group in view. See CAP-U12-09. VDR-U12-C048 VDR-U12-C049 VDR-U12-C041 |
| 8 | Scheduled / automated | No cron in the payment model itself; status recomputes on reconciliation events (CAP-U12-03/04). UNKNOWN beyond that. VDR-U12-C018 |
| 9 | Exception / failure | UserError when no outstanding account can be found; UserError when amount edited with several liquidity lines; UserError when recipient bank account required but untrusted. VDR-U12-C008 VDR-U12-C029 VDR-U12-C033 |
| 10 | Accounting / audit / compliance | Posted entry with intermediate account until bank matching; rejected payments keep entry; restrictive audit trail (company flag) blocks deletion of posted-before entries; payments tracked via mail tracking on state, partner, amount, date. VDR-U12-C036 VDR-U12-C027 VDR-U12-C045 |

**DB reconciliation (configuration only).** Seeded: journal BNK1 (bank) has three method lines (manual inbound, manual outbound, check printing outbound) and all three have an empty payment account. Company outstanding accounts "Outstanding Receipts" (inbound) and "Outstanding Payments" (outbound) exist as chart records (reconcilable, current-asset type) and are what the Community fallback in `create()` uses. Company transfer account is set. No payments exist (count 0). VDR-U12-C008 VDR-U12-C024

**Unknown / Runtime (RT) list.**
- RT: whether `paid` is reached immediately or only after bank matching for a normal bank-journal payment (static reading says it also flips to paid when all settled invoices are paid, see CAP-U12-04). VDR-U12-C018
- RT: effect of resetting a payment to draft while its entry is reconciled (no code in scope removes the matching). VDR-U12-C039
- UNKNOWN: any producer of paired internal-transfer payments in Community. VDR-U12-C051
- UNKNOWN: handling of rejected payments beyond the state flag (Enterprise bank features not in scope). VDR-U12-C036


## CAP-U12-02 Payment registration against invoices and bills


**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 — Business purpose and process semantics.** Registering a payment is the guided way to pay vendor bills or collect customer invoices (and refunds / other receivable-payable items): the user picks documents or journal items, the wizard proposes journal, method, amount, memo and recipient bank, and on confirmation creates the payment(s), posts them and reconciles them with the open items. Differences (partial payment, early-payment discount, write-off) are decided in the wizard. VDR-U12-C053 VDR-U12-C091 VDR-U12-C092 VDR-U12-C064

**D2 — Architecture, data and object relationships.** `account.payment.register` is a transient model fed by `active_model` = `account.move` or `account.move.line`; its `line_ids` are receivable/payable journal items. `batches` (binary computed) groups lines by `_get_line_batch_key`. For each payment to create the wizard builds `create_vals`, creates `account.payment` (with `write_off_line_vals`/`force_balance` hacks), posts it, and reconciles `payment.move_id` lines with the batch lines per account; the invoice's `matched_payment_ids` is linked. Extended by `account_payment` (token fields). VDR-U12-C056 VDR-U12-C057 VDR-U12-C063 VDR-U12-C090 VDR-U12-C092 VDR-U12-C108

**D3 — Source, technical and workflow logic.** Control flow: `account.move.action_register_payment` (posted-only) -> `action_force_register_payment` (not misc entries, not blocked) -> `account.move.line.action_register_payment` (opens wizard, context active_model `account.move.line`) -> wizard `default_get` (filters lines, company/type checks) -> computes (`_compute_batches`, `_compute_from_lines`, journal / method / partner bank / amount / installments / difference) -> `action_create_payments` -> `_create_payments` (skips untrusted-bank batches, decides edit-mode vs batch mode, builds `to_process`) -> `_init_payments` (create) -> `_post_payments` (action_post) -> `_reconcile_payments` (reconcile per account, link `matched_payment_ids`). VDR-U12-C053 VDR-U12-C058 VDR-U12-C070 VDR-U12-C090 VDR-U12-C091 VDR-U12-C092

State diagram (wizard process; the wizard itself is transient and has no status field):
- `opened -> lines accepted` [default_get checks pass] VDR-U12-C058 VDR-U12-C059
- `lines accepted -> batches computed` [_compute_batches] VDR-U12-C064
- `batches computed -> payments created (draft)` [action_create_payments -> _init_payments] VDR-U12-C090
- `payments created -> in_process or paid` [_post_payments -> action_post, see CAP-U12-01] VDR-U12-C091
- `payments posted -> items matched` [_reconcile_payments -> reconcile(), see CAP-U12-03] VDR-U12-C092
- `batch skipped` [untrusted or missing recipient bank when required; error if none left] VDR-U12-C103
Payments created follow CAP-U12-01 and invoices follow CAP-U12-04.

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Select posted invoices/bills, wizard proposes journal, method, memo, amount; confirm creates posted payment(s) and reconciles; documents become paid or partial. VDR-U12-C091 VDR-U12-C092 VDR-U12-C082 |
| 2 | Reversal / cancel / negative | Wizard cannot be undone; reversal is by payment cancel/reset (CAP-U12-01) and unreconcile (CAP-U12-03). Credit notes (negative direction) are batched with sign-based payment type. VDR-U12-C065 |
| 3 | Multi-company / data scope | Lines of different root companies refused; sibling-company lines need parent company access and are paid as the parent company under sudo; journals filtered by company domain. VDR-U12-C060 VDR-U12-C066 VDR-U12-C094 VDR-U12-C095 |
| 4 | Side effects / cross-module | Posts payments, reconciles (exchange difference / cash basis entries may be created, CAP-U12-03), links matched payments; with `account_payment` a saved token can be selected. VDR-U12-C092 VDR-U12-C108 |
| 5 | Configuration / optionality | Grouping, journal, method, bank account, amount, difference handling are user choices; early-payment discount from the term; partner default methods; company discount and exchange accounts. VDR-U12-C068 VDR-U12-C096 VDR-U12-C077 |
| 6 | Validation / constraints | Posted only, no misc entries, not blocked, one root company, same account type, something left to pay, bank trusted when required. VDR-U12-C053 VDR-U12-C054 VDR-U12-C055 VDR-U12-C059 VDR-U12-C061 VDR-U12-C103 |
| 7 | Roles / permissions | Wizard ACL read/write/create for Invoicing group (no unlink). VDR-U12-C109 |
| 8 | Scheduled / automated | None in the wizard. NOT APPLICABLE. |
| 9 | Exception / failure | UserError set: wrong active model, nothing to pay, companies/branches, mixed types, blocked invoices, all batches untrusted. VDR-U12-C057 VDR-U12-C059 VDR-U12-C060 VDR-U12-C061 VDR-U12-C062 VDR-U12-C103 |
| 10 | Accounting / audit / compliance | Payment entry via outstanding account; write-off lines to chosen account; exchange-difference special account handling; early-payment discount entries to company cash-discount accounts; duplicate warning and in-process warning reduce double payment. VDR-U12-C079 VDR-U12-C080 VDR-U12-C075 VDR-U12-C105 VDR-U12-C106 |

**DB reconciliation (configuration only).** Journal BNK1 (bank) exposes manual inbound, manual outbound and check outbound method lines; no payment accounts on those lines; company cash-discount gain/loss accounts and exchange gain/loss accounts are set; early-payment discount term "2/7 Net 30" exists; no documents, no payments (nothing to register). Wizard ACL row for the Invoicing group exists (read/write/create). VDR-U12-C109

**Unknown / Runtime (RT) list.**
- RT: over-payment path (negative `payment_difference` with `reconcile`) and rounding on foreign-currency payments need execution. VDR-U12-C079 VDR-U12-C089
- RT: exact set of lines selected in `lines_to_pay` for installment modes with several moves. VDR-U12-C072
- UNKNOWN: behaviour when `group_payment` is true but batch partner banks differ (batch keys keep banks separate unless merged). VDR-U12-C064


## CAP-U12-03 Reconciliation engine


**Function-ID(s):** FUNCTION MAPPING REQUIRED. (Lock-date interplay is a hand-off to U11 / PCO-F01; tax cash-basis is noted only.)

**D1 — Business purpose and process semantics.** Reconciliation (matching) pairs debit and credit journal items on the same reconcilable account so receivables/payables are settled and open amounts are known. Each pairing is an `account.partial.reconcile`; when a connected set of items reaches zero in both company and foreign currency, an `account.full.reconcile` is created and every item receives the same matching number. Foreign-currency mismatches generate automatic exchange-difference entries. VDR-U12-C113 VDR-U12-C129 VDR-U12-C144 VDR-U12-C146 VDR-U12-C135

**D2 — Architecture, data and object relationships.** `account.move.line` carries `amount_residual`, `amount_residual_currency`, `reconciled`, `matching_number`, `full_reconcile_id`, `matched_debit_ids` / `matched_credit_ids` (partials as credit/debit side) and `reconciled_lines_ids`. `account.partial.reconcile` has `debit_move_id`, `credit_move_id`, `amount` (company currency), `debit_amount_currency`, `credit_amount_currency`, `exchange_move_id`, `full_reconcile_id`, `draft_caba_move_vals`, `max_date`. `account.full.reconcile` groups partials and lines. Exchange entries are normal `account.move` entries linked through `exchange_move_id`. VDR-U12-C113 VDR-U12-C114 VDR-U12-C128 VDR-U12-C118 VDR-U12-C142

**D3 — Source, technical and workflow logic.**

Control flow of `account.move.line.reconcile()`: `_reconcile_plan([lines])` -> `_optimize_reconciliation_plan` (sort by maturity/date, currency, amounts; split by currency; `_check_amls_exigibility_for_reconciliation`) -> within `_check_balanced` / `_sync_dynamic_lines` -> `_reconcile_plan_with_sync`: pre-hook (invoice payment states) -> build residual map -> `_prepare_reconciliation_plan` -> `_prepare_reconciliation_amls` pairs debit/credit values iteratively with `_prepare_reconciliation_single_partial` (choose reconciliation currency, compute partial amounts, compute exchange difference values) -> create partials -> create exchange difference moves (`_create_exchange_difference_moves`, post if both sides posted) and link them to partials -> cash-basis moves (hand-off) -> detect fully reconciled groups -> create full reconcile records -> post-hook (`_invoice_paid_hook`). VDR-U12-C121 VDR-U12-C122 VDR-U12-C123 VDR-U12-C125 VDR-U12-C126 VDR-U12-C129 VDR-U12-C131 VDR-U12-C141 VDR-U12-C149 VDR-U12-C144

State diagram of a journal item (field `matching_number`, `reconciled`):
- `unreconciled -> partially reconciled` [partial created, residual remains; matching_number `P<n>`] VDR-U12-C129 VDR-U12-C146
- `partially reconciled -> fully reconciled` [residuals zero in company and line currency; full reconcile created; matching_number = full id] VDR-U12-C144 VDR-U12-C145
- `fully | partially reconciled -> unreconciled` [partials unlinked by remove_move_reconcile, by writes on account/date/balance/amount/currency, or by entry/line deletion] VDR-U12-C156 VDR-U12-C159 VDR-U12-C162 VDR-U12-C163
- `import marker I<text> -> fully reconciled` [_reconcile_marked once all marked moves are posted] VDR-U12-C148
- `any -> blocked` [cancelled parent entry cannot be reconciled] VDR-U12-C124
Constraints on the number format: VDR-U12-C147; residual rule: VDR-U12-C128.

Unreconcile: `remove_move_reconcile` unlinks partials -> `account.partial.reconcile.unlink` (find CABA and exchange entries, unlink full reconcile, reverse or delete those entries, update matching numbers, reset payments without outstanding account to in_process). VDR-U12-C156 VDR-U12-C154

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Debit/credit lines of the same account matched oldest-first until one side is exhausted; partials created, exchange differences created if needed, full reconcile created when everything is zero. VDR-U12-C129 VDR-U12-C133 VDR-U12-C144 |
| 2 | Reversal / cancel / negative | Partial unlink reverses exchange/CABA entries (or deletes drafts); writes on matched lines auto-unreconcile; cancelled entries cannot be matched; moves delete -> remove reconcile first. VDR-U12-C154 VDR-U12-C159 VDR-U12-C124 VDR-U12-C163 |
| 3 | Multi-company / data scope | All lines must share the root company; partial company taken from the invoice side; exchange entry company from the invoice (or first) line; reconcilable accounts checked per company. VDR-U12-C123 VDR-U12-C116 VDR-U12-C138 |
| 4 | Side effects / cross-module | Exchange differences, cash-basis entries (note), payment status recompute, paid hook (sale posts "Invoice paid" on order), statement-line undo, payments reset. VDR-U12-C141 VDR-U12-C149 VDR-U12-C127 VDR-U12-C160 |
| 5 | Configuration / optionality | Company exchange journal and gain/loss accounts; cash-basis journal when cash-basis taxes; context switches `no_exchange_difference`, `no_cash_basis`, `move_reverse_cancel`, `reduced_line_sorting`, `forced_rate_from_register_payment`. VDR-U12-C140 VDR-U12-C150 VDR-U12-C170 |
| 6 | Validation / constraints | Already reconciled, cancelled, mixed accounts, mixed roots, non-reconcilable account, required partial currencies, matching-number formats, off-balance lines cannot reconcile. VDR-U12-C123 VDR-U12-C115 VDR-U12-C147 VDR-U12-C166 |
| 7 | Roles / permissions | ACL on partial reconcile: Invoicing full CRUD, full-accounting full CRUD, readonly read (+ sale/purchase/sale_stock extra rows); unreconcile server action for full-accounting group. See CAP-U12-09. VDR-U12-C171 VDR-U12-C158 |
| 8 | Scheduled / automated | None in the engine (batch driven by user actions and posting hooks). NOT APPLICABLE. |
| 9 | Exception / failure | UserError for config (exchange journal/accounts, cash-basis journal), already reconciled, cancelled, account mismatch, company mismatch, non-reconcilable account. VDR-U12-C140 VDR-U12-C150 VDR-U12-C123 |
| 10 | Accounting / audit / compliance | Exchange gain/loss booked to company accounts; matched amounts immutable except via auto-unreconcile; lock-date checks on write/unlink (hand-off U11); reversal date after lock when unreconciling; tax lock check on write. VDR-U12-C138 VDR-U12-C159 VDR-U12-C161 VDR-U12-C155 |

**DB reconciliation (configuration only).** Company: exchange journal (EXCH) and income/expense currency-exchange accounts set; cash-basis journal (CABA) set and company tax exigibility flag true; no partial or full reconciles (count 0); partial reconcile ACL has extra rows from `purchase` (User), `sale` (User: Own Documents Only) and `sale_stock` (Administrator). VDR-U12-C140 VDR-U12-C150 VDR-U12-C171

**Unknown / Runtime (RT) list.**
- RT: multi-currency rounding tolerance and exchange-difference amounts in real combinations (code paths read, not executed). VDR-U12-C134 VDR-U12-C135
- RT: effect of reset-to-draft on matched entries (no unreconcile in `button_draft`). VDR-U12-C164
- RT / CONTRA: helper `_check_reconciliation` has no caller in `odoo/addons` (prior candidate says it refuses edits of matched posted lines). VDR-U12-C165
- UNKNOWN: any Community UI consumer of `_get_default_amls_matching_domain` (statement-line candidate domain). VDR-U12-C172


## CAP-U12-04 Payment status on invoices


**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 — Business purpose and process semantics.** The invoice (or bill / credit note / receipt) payment status tells users whether a document is unpaid, partly paid, paid, reversed (cancelled by a credit note or reversing entry, not by money) or blocked from payment. It drives dashboards, the portal "pay now" button, follow-ups, expense states and reporting. VDR-U12-C176 VDR-U12-C196 VDR-U12-C198

**D2 — Architecture, data and object relationships.** Stored computed selection `account.move.payment_state` (values `not_paid`, `in_payment`, `paid`, `partial`, `reversed`, `blocked`, `invoicing_legacy`); derived label `status_in_payment`. Inputs are the document's `amount_residual` (from `payment_term` lines' residuals), the partial reconciles on its receivable/payable lines, the counterpart moves' types (payment entry, bank statement line entry, refund), `origin_payment_id.is_matched` of counterpart payments, and `matched_payment_ids` for payments without entries. `reconciled_payment_ids` merges SQL-found payments and `matched_payment_ids`. VDR-U12-C175 VDR-U12-C178 VDR-U12-C182 VDR-U12-C191

**D3 — Source, technical and workflow logic.** `_compute_payment_state` groups moves: legacy and blocked keep their value; posted invoice-type moves (and draft ones with non-zero total) are computed; others are `not_paid`. For computed invoices a SQL gathers, per partial on receivable/payable lines, counterpart move types, whether counterparts are payments / statement lines and whether all counterpart payments are matched. Decision order: residual zero and any payment/statement counterpart -> `paid` if all payments matched else `_get_invoice_in_payment_state()` (which returns `paid` in this tree); residual zero without payment/statement counterpart -> `paid` unless counterpart types are only refunds (and entries) of the opposite family -> `reversed`; residual non-zero and a posted invoice with entry-less in-process matched payment -> in-payment hook value; residual non-zero and any partial exists -> `partial`; residual non-zero and an entry-less paid matched payment -> in-payment hook value; else `not_paid`. VDR-U12-C180 VDR-U12-C181 VDR-U12-C183 VDR-U12-C184 VDR-U12-C186 VDR-U12-C185 VDR-U12-C187

State diagram:
- `not_paid -> partial` [partial reconcile created on a receivable/payable line] VDR-U12-C186
- `not_paid | partial -> paid` [residual becomes zero, via payment, statement line, or other entries] VDR-U12-C183
- `not_paid | partial -> reversed` [residual zero with only refund/misc-entry counterparts and no payment or statement line] VDR-U12-C184
- `paid | partial -> not_paid / partial` [unreconcile or payment delete/cancel recompute] VDR-U12-C178 VDR-U12-C190
- `not_paid | partial -> blocked` [action_toggle_block_payment]; `blocked -> not_paid` [toggle again, then recompute]; refused when paid or in_payment VDR-U12-C193
- `in_payment` is declared in the selection but, with the hook returning `paid`, not reachable in this edition. VDR-U12-C187

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Register payment -> reconcile -> residual zero -> `paid` (immediately in Community since in-payment hook returns paid). VDR-U12-C183 VDR-U12-C187 |
| 2 | Reversal / cancel / negative | Credit note or reversing entry that zeroes the residual yields `reversed` when no payment/statement line is involved; unreconcile / payment unlink recompute status. VDR-U12-C184 VDR-U12-C190 |
| 3 | Multi-company / data scope | Compute keyed on invoice company; payments read through `_filtered_access('read')` in `reconciled_payment_ids`. VDR-U12-C191 |
| 4 | Side effects / cross-module | Dashboard counts (not_paid, partial), invoice analysis report, portal payability, expense state, sales-team KPI use the value; paid-notification subtype; reconcile post-hook. VDR-U12-C196 VDR-U12-C197 VDR-U12-C198 VDR-U12-C199 VDR-U12-C200 |
| 5 | Configuration / optionality | Edition hook `_get_invoice_in_payment_state` decides whether `in_payment` exists. VDR-U12-C187 |
| 6 | Validation / constraints | `payment_state` is readonly stored; block only if not paid/in_payment; registering payments refused for blocked. VDR-U12-C176 VDR-U12-C193 |
| 7 | Roles / permissions | No dedicated ACL; follows account.move ACL (field is readonly). See CAP-U12-09. |
| 8 | Scheduled / automated | None: recomputed on dependency change (partial create/unlink, payment matched flag, residual). VDR-U12-C178 |
| 9 | Exception / failure | Blocking a paid invoice raises UserError. VDR-U12-C193 |
| 10 | Accounting / audit / compliance | Status transitions are tracked; paid transition posts a message subtype; `reversed` distinguishes credit-note settlement from cash settlement. VDR-U12-C200 VDR-U12-C184 |

**Sensitivity to reversals and to the bank statement process.** Reversal entries/credit notes that are reconciled against the invoice leave `reversed` only if neither a payment nor a statement-line entry is among counterparts; a payment plus a credit note gives `paid`. In Community a payment's `is_matched` (bank match of the outstanding line) changes only the in-payment hook branch, which yields `paid` anyway; hence bank statement matching does not change the invoice status in this edition (but changes payment status, CAP-U12-01). VDR-U12-C183 VDR-U12-C184 VDR-U12-C187 VDR-U12-C178

**DB reconciliation (configuration only).** Bank journal BNK1 method lines carry no payment account (`payment_account_id` empty), company outstanding accounts exist and are used by the Community create-time fallback; no invoices, no payments, no reconciles exist, so no status values are present; accounting app module is not installed. VDR-U12-C187

**Unknown / Runtime (RT) list.**
- RT: ordering of recomputation after reconcile (flush / hook) for payment status flip `in_process -> paid` caused by invoice `paid` (circular dependency payment <-> invoice status). VDR-U12-C189
- RT: behaviour of `blocked` when a blocked invoice later receives a reconcile through other paths (e.g. credit note). VDR-U12-C180


## CAP-U12-05 Bank statements, statement lines and reconcile models


**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 — Business purpose and process semantics.** Bank statement lines record bank/cash transactions as journal entries (bank-account line + suspense counterpart) so book and bank can be compared; statements are integrity checkpoints (starting balance chain and completeness), not a validation workflow. Reconcile models are presets describing entries to create or partner mappings to propose when a transaction is matched. In this Community tree the matching engine, import and automated application of reconcile models are not present (see D3). VDR-U12-C206 VDR-U12-C220 VDR-U12-C223 VDR-U12-C258

**D2 — Architecture, data and object relationships.** `account.bank.statement` (journal derived from lines, balances, `is_complete`, `is_valid`, `first_line_index`) has many `account.bank.statement.line`. A statement line `_inherits` `account.move` (`move_id`, required, cascade); its lines are `_seek_for_lines` -> liquidity (journal default account), suspense (journal suspense account) and other lines. `account.reconcile.model` with `account.reconcile.model.line`; `account.move.line.reconcile_model_id` records which model created a line. Payments created while reconciling are held in `payment_ids`. VDR-U12-C205 VDR-U12-C220 VDR-U12-C228 VDR-U12-C255 VDR-U12-C234

**D3 — Source, technical and workflow logic.**

State diagram of a statement line (`is_reconciled`):
- `(none) -> unreconciled` [create: entry forced, liquidity + suspense lines, entry posted] VDR-U12-C221 VDR-U12-C222
- `unreconciled -> reconciled` [suspense residual becomes zero; the matching action itself is outside the studied scope] VDR-U12-C227 VDR-U12-C237
- `reconciled -> unreconciled` [action_undo_reconciliation: matches removed, auto-generated payments unlinked, default lines restored] VDR-U12-C233
- `unreconciled | reconciled -> entry canceled` [unlink on company with restrictive audit trail] VDR-U12-C231
- `unreconciled | reconciled -> deleted` [unlink otherwise; refused for lines of a valid and complete statement] VDR-U12-C231 VDR-U12-C232
Statement checks (computed, no workflow): `incomplete -> complete` [balance_end equals balance_end_real] and `invalid -> valid` [balance_start equals previous balance_end_real]. VDR-U12-C212 VDR-U12-C213

Statement integrity: `first_line_index` (earliest line index) orders statements; `balance_start` computed from the previous statement's real ending balance plus intervening posted lines; `balance_end` = start + posted lines; `balance_end_real` defaults to `balance_end` and is editable; `is_complete` when lines exist and `balance_end == balance_end_real`; `is_valid` when `balance_start == previous.balance_end_real`. Journal flag `has_invalid_statements` aggregates. VDR-U12-C207 VDR-U12-C209 VDR-U12-C210 VDR-U12-C211 VDR-U12-C212 VDR-U12-C213 VDR-U12-C243

Reconcile models: pure configuration records (trigger manual/auto_reconcile, condition fields, line amount types fixed / percentage of balance / percentage of statement line / regex from label) with validation constraints and helper actions; `can_be_proposed` and `mapped_partner_id` stored computes. No code in `account`, `account_payment`, `payment`, `account_check_printing` or `account_payment_interco` applies them to statement lines. VDR-U12-C246 VDR-U12-C247 VDR-U12-C248 VDR-U12-C249 VDR-U12-C251 VDR-U12-C252 VDR-U12-C258

Scheduled / automated behaviour: `account` ships two crons only (auto-post draft entries; send invoices) and none for statements or reconcile models. VDR-U12-C261

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Create statement line -> entry posted with bank + suspense lines; statement created from lines shows completeness and validity; match via external/enterprise UI (not in scope). VDR-U12-C221 VDR-U12-C212 VDR-U12-C213 |
| 2 | Reversal / cancel / negative | `action_undo_reconciliation`, line unlink (cancel entry under restrictive audit trail), statement line cannot be deleted from valid+complete statement. VDR-U12-C233 VDR-U12-C231 VDR-U12-C232 |
| 3 | Multi-company / data scope | Record rules on statement (company_id in company_ids + False) and line (company_id in company_ids); journal company drives statement company; candidate domain includes child companies. VDR-U12-C264 VDR-U12-C265 VDR-U12-C236 |
| 4 | Side effects / cross-module | Statement line creation posts a move; undo unlinks payments; matched lines write unreconcile statement lines (CAP-U12-03); `account_payment` overrides a partial-amount helper that does not exist in Community. VDR-U12-C221 VDR-U12-C233 VDR-U12-C260 |
| 5 | Configuration / optionality | Journal suspense account, bank-feed source (only undefined), reconcile models and trigger types, parameter to skip bank-account creation. VDR-U12-C223 VDR-U12-C242 VDR-U12-C235 |
| 6 | Validation / constraints | Foreign currency consistency, exactly one liquidity line and at most one suspense line, contiguous multi-line statement creation, regex and amount validations in models. VDR-U12-C225 VDR-U12-C229 VDR-U12-C216 VDR-U12-C249 |
| 7 | Roles / permissions | Statement and line: Invoicing and readonly read only, Basic full CRUD; reconcile model: readonly read, Invoicing read+create, Basic full. See CAP-U12-09. VDR-U12-C262 VDR-U12-C263 |
| 8 | Scheduled / automated | No cron for statements or reconcile models in scope. VDR-U12-C261 |
| 9 | Exception / failure | UserErrors: no suspense account, statement lines from several journals, non-contiguous lines, invalid entry shape (liquidity/suspense lines), validated entries changed by non-accountant. VDR-U12-C223 VDR-U12-C216 VDR-U12-C229 VDR-U12-C233 |
| 10 | Accounting / audit / compliance | Suspense account keeps unmatched money visible; running balance by statement anchors; restrictive audit trail prevents deletion; reviewed flag rules reserved to accountant role (always allowed in Community). VDR-U12-C223 VDR-U12-C238 VDR-U12-C231 VDR-U12-C245 |

**Statement validation / lock concept in 19.** There is no draft/validated/locked state on `account.bank.statement`; "validity" is the starting-balance chain and "completeness" is the internal sum check; deletion protection applies to lines of valid and complete statements. Entry-level locking is U11. VDR-U12-C206 VDR-U12-C232

**DB reconciliation (configuration only).** Journal BNK1 bank feed source is undefined; suspense account set on BNK1; no statements or lines exist; two manual reconcile models are seeded (Internal Transfers to the transfer account; Bank Fees on label "Bank Fees", whose line account is the first expense account of the chart, here "Employees compensation", to be reviewed); crons present in DB: auto-post draft entries (active), send invoices (active) — no statement cron. VDR-U12-C242 VDR-U12-C256 VDR-U12-C257 VDR-U12-C261

**Unknown / Runtime (RT) list.**
- UNKNOWN: how an accountant matches a statement line to an invoice or payment in Community (no consumer of the candidate domain; no import / matching module). VDR-U12-C237
- UNKNOWN: effect of `auto_reconcile` trigger (no engine in scope). VDR-U12-C258
- RT: statement `balance_start` recompute when lines are reordered or edited. VDR-U12-C209


## CAP-U12-06 Payment terms and early-payment discount


**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 — Business purpose and process semantics.** A payment term splits an invoice/bill total into installments with due dates, or offers a single-line early-payment discount (EPD). It fixes the document's due date and drives dunning, installment payment, portal payment and the wizard's discount handling. Three accounting treatments of the discount exist (`included`, `excluded`, `mixed`) which change how the tax base and tax are adjusted. VDR-U12-C267 VDR-U12-C276 VDR-U12-C281 VDR-U12-C282

**D2 — Architecture, data and object relationships.** `account.payment.term` (company optional, parent-of scoped) has `account.payment.term.line` (value percent/fixed, `delay_type`, `nb_days`, `days_next_month`). A document (`account.move.invoice_payment_term_id`) computes `needed_terms` -> payment_term journal items carrying `date_maturity`, `discount_date`, `discount_balance`, `discount_amount_currency`. Company fields point to cash-discount gain/loss accounts. Partner properties give default customer/vendor terms. VDR-U12-C289 VDR-U12-C291 VDR-U12-C294 VDR-U12-C313

**D3 — Source, technical and workflow logic.**

Due-date computation: `_compute_terms(date_ref, ...)` returns installments (`date`, `company_amount`, `foreign_amount`) and discount values; each line's date comes from `_get_due_date(date_ref)` by `delay_type`; the last line always carries the remaining balance (percent or fixed); cash rounding is applied per non-last line. Invoice side: `_compute_needed_terms` calls it with tax/untaxed amounts (from base lines when the record is new/draft, from stored totals otherwise), merges installments with identical date key, and `_compute_invoice_date_due` takes the maximum maturity. VDR-U12-C275 VDR-U12-C276 VDR-U12-C277 VDR-U12-C291 VDR-U12-C292

EPD discount computation: with `early_discount` the term stores `discount_percentage` and `discount_days`; `discount_balance`/`discount_amount_currency` = `total - untaxed * pct` for `excluded`/`mixed`, or `total * (1 - pct)` for `included`; `discount_date = date_ref + discount_days`. VDR-U12-C279 VDR-U12-C280

Accounting variants: `included` ("On early payment") keeps the invoice untouched and, when the discount is taken in the register wizard, books base discount lines plus adjusted tax lines on the cash-discount accounts; `excluded` ("Never") reduces only the untaxed part, with no tax lines (tax lines are generated only for `included`); `mixed` ("Always (upon invoice)") adds `epd` and counterpart lines on the invoice itself that reduce the tax base at invoicing time. VDR-U12-C299 VDR-U12-C301 VDR-U12-C305 VDR-U12-C307

Eligibility and application: `_is_eligible_for_early_payment_discount` (move types, same currency, term has EPD, payment date not after discount date, no existing reconcile). Installment data marks the line `early_payment_discount` and exposes discounted residual; the wizard then applies the difference automatically; `account_payment` transactions apply it when the paid amount equals the discounted amount. VDR-U12-C296 VDR-U12-C297 VDR-U12-C298 VDR-U12-C311

State diagram: NOT APPLICABLE — terms are configuration data without workflow VDR-U12-C316; document-level `invoice_date_due`, installments and `payment_state` interplay is in CAP-U12-04.

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Select a term on the invoice, installments and due date computed; with EPD the discounted amount is proposed in the payment wizard and the difference booked automatically. VDR-U12-C291 VDR-U12-C298 |
| 2 | Reversal / cancel / negative | Credit notes carry their own terms; EPD not eligible once any matching exists; unreconcile re-enables eligibility; term deletion refused when referenced. VDR-U12-C296 VDR-U12-C283 |
| 3 | Multi-company / data scope | Term company optional; record rule: no company or parent of allowed companies; check-company domain parent-of. VDR-U12-C286 VDR-U12-C287 |
| 4 | Side effects / cross-module | Journal items for terms, EPD lines (mixed), write-off lines in payments, portal payment links, invoice PDF installments. VDR-U12-C305 VDR-U12-C299 VDR-U12-C310 VDR-U12-C312 |
| 5 | Configuration / optionality | Term lines, EPD on/off, discount percentage/days, tax reduction mode by country, company discount accounts, partner defaults, display installment dates. VDR-U12-C281 VDR-U12-C313 VDR-U12-C289 |
| 6 | Validation / constraints | Percent sum 100, ≥1 percent line, single 100% line with EPD, positive percentage and days, percent range, days-of-month range. VDR-U12-C270 VDR-U12-C271 VDR-U12-C272 |
| 7 | Roles / permissions | Terms: all internal users read, portal read, Administrator (account manager) full CRUD. See CAP-U12-09. VDR-U12-C288 |
| 8 | Scheduled / automated | None. NOT APPLICABLE (installment overdue state is date-driven at read time via installments data). VDR-U12-C297 |
| 9 | Exception / failure | ValidationError on invalid lines/EPD parameters; UserError on deleting referenced term; EPD edge cases fall back to normal amount when ineligible. VDR-U12-C270 VDR-U12-C283 |
| 10 | Accounting / audit / compliance | Discount booked to contra accounts (customer: loss/sales discounts; vendor: gain/purchase discounts); taxes adjusted per computation mode; rounding pushed to largest line; tax base changes only in mixed mode at invoicing. VDR-U12-C300 VDR-U12-C301 VDR-U12-C303 VDR-U12-C307 |

**Effect on payment registration and tax base.** Registration: see CAP-U12-02 (default amount, difference auto handling). Tax base: only `mixed` changes the invoice tax base at invoicing (EPD lines with taxes are part of base-line calculation); `included` adjusts tax lines only at payment time; `excluded` never adjusts taxes. Fixed taxes are excluded from discount calculations. VDR-U12-C307 VDR-U12-C301 VDR-U12-C302

**DB reconciliation (configuration only).** Ten seeded terms (Immediate Payment, 15, 21, 30, 45 Days, End of Following Month, 10 Days after End of Next Month, 30% Now Balance 60 Days, 2/7 Net 30 (the only one with EPD: 2%, 7 days, computation `included`), 90 days on the 10th); all company-agnostic and active. Company cash-discount accounts: loss account is a "Sales Discounts" (income type) account and gain account is a "Purchase Discounts" (other income type) account (local chart mapping). VDR-U12-C313 VDR-U12-C315

**Unknown / Runtime (RT) list.**
- RT: rounding and tax-line distribution of EPD in included mode with several taxes / foreign currency. VDR-U12-C303
- RT: behaviour of `mixed` mode EPD lines when taxes are edited after posting. VDR-U12-C305


## CAP-U12-07 Check printing


**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 — Business purpose and process semantics.** `account_check_printing` lets a company pay vendors by printed cheque: payments using the `check_printing` outbound method are numbered, printed on a layout (supplied by country modules), marked sent, and can be voided. The cheque carries payee, amount in words and a stub listing paid bills/refunds. VDR-U12-C318 VDR-U12-C337 VDR-U12-C340 VDR-U12-C339 VDR-U12-C342

**D2 — Architecture, data and object relationships.** Extends `account.payment` (`check_number`, `check_amount_in_words`, `show_check_number`, `check_manual_sequencing` related to the journal), `account.journal` (`check_manual_sequencing`, `check_sequence_id`, `check_next_number`, `bank_check_printing_layout`), `res.company` (layout selection plus margins, date label, multi-stub) and `account.payment.method` (code `check_printing`). Transient `print.prenumbered.checks` collects the first pre-printed number. Numbers are stored on the payment; the journal sequence (`ir.sequence`, no_gap) drives manual numbering. VDR-U12-C329 VDR-U12-C321 VDR-U12-C326 VDR-U12-C318 VDR-U12-C344

**D3 — Source, technical and workflow logic.**

Control flow: `print_checks()` (button / server action) -> filter valid payments (`check_printing` method, not sent) -> same journal check -> if journal not manually sequenced: wizard asks first number (suggested = max existing + 1) -> wizard posts drafts, sets `is_sent`, assigns consecutive numbers, calls `do_print_checks`; else drafts are posted (numbering happens in `action_post` using the journal sequence) and `do_print_checks` runs -> layout resolved (journal layout else company layout; `disabled` or missing -> `RedirectWarning`) -> `is_sent` written -> report action rendered with `_check_get_pages()` (pages built by `_check_build_page_info`, stub by `_check_make_stub_pages`). Void: `action_void_check` = `action_draft` then `action_cancel`. VDR-U12-C337 VDR-U12-C344 VDR-U12-C336 VDR-U12-C340 VDR-U12-C339 VDR-U12-C341

State diagram (payment states of CAP-U12-01 plus the `is_sent` flag):
- `draft -> in_process (not sent)` [action_post, check number assigned for manually sequenced journals] VDR-U12-C336
- `in_process (not sent) -> in_process (sent)` [print_checks / do_print_checks writes is_sent] VDR-U12-C340 VDR-U12-C344
- `in_process (sent) -> draft -> canceled` [Void Check = action_draft then action_cancel] VDR-U12-C339
- `in_process (sent) -> in_process (not sent)` [Unmark Sent button] VDR-U12-C347

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Create vendor payment with method Checks, confirm, Print Check: number assigned (journal sequence or wizard), layout rendered, payment marked sent. VDR-U12-C336 VDR-U12-C337 VDR-U12-C340 |
| 2 | Reversal / cancel / negative | Void Check (draft then cancel) for in-process sent checks; Unmark Sent. VDR-U12-C339 VDR-U12-C347 |
| 3 | Multi-company / data scope | Layout/margins on company; journal sequence per company; no extra record rule beyond payment's. VDR-U12-C326 VDR-U12-C323 |
| 4 | Side effects / cross-module | Check number sets journal item labels; sequence padding follows entered number; dashboard counts; stub reads reconciled invoices. VDR-U12-C335 VDR-U12-C333 VDR-U12-C325 VDR-U12-C342 |
| 5 | Configuration / optionality | Layout (journal override of company), margins, date label, multi-page stub, manual vs pre-numbered, next number. VDR-U12-C326 VDR-U12-C321 VDR-U12-C322 |
| 6 | Validation / constraints | Digits only, unique per journal among posted, same journal for batch printing, valid method and unsent, next number monotonic and ≤ INT max. VDR-U12-C330 VDR-U12-C331 VDR-U12-C337 VDR-U12-C322 |
| 7 | Roles / permissions | Print Checks server action and numbering wizard for account.group_account_user; payment ACL otherwise. VDR-U12-C345 VDR-U12-C346 |
| 8 | Scheduled / automated | None. NOT APPLICABLE. |
| 9 | Exception / failure | UserError for no valid payments / mixed journals; RedirectWarning for missing layout; ValidationError for non-digit, duplicates, too-low or too-high numbers. VDR-U12-C337 VDR-U12-C340 VDR-U12-C330 VDR-U12-C331 VDR-U12-C322 |
| 10 | Accounting / audit / compliance | Sequence is no_gap; used numbers not reused; voiding keeps trail via cancel; stub cropped unless multi-page. VDR-U12-C323 VDR-U12-C331 VDR-U12-C342 |

**DB reconciliation (configuration only).** Journal BNK1 has the outbound Checks method line (empty payment account); its check sequence exists (no_gap, padding 5, next number 1); manual numbering off; no journal layout; company layout is `disabled` (None) with multi-stub off, so printing would be refused until a layout from a country module is chosen (no module in the studied source adds one). VDR-U12-C326 VDR-U12-C327 VDR-U12-C323

**Unknown / Runtime (RT) list.**
- RT: report rendering of stub pages and VOID pages (templates not read). VDR-U12-C341
- INFERENCE: no module in `odoo/addons` adds a layout to `account_check_printing_layout`; with the base selection only (`disabled`) printing is refused. VDR-U12-C350


## CAP-U12-08 Inter-company payments and payment-provider transaction framework


**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 — Business purpose and process semantics.** (a) Inter-company payment: when a sister company's invoice is paid through a provider transaction recorded in another company, clearing entries in both companies keep each company's receivable/payable and cash consistent through inter-company clearing accounts. (b) Payment-provider framework (`payment`): every online/token payment attempt (and capture, void, refund) is a `payment.transaction` with a state machine; confirmed transactions are post-processed (by cron or the customer status page) and `account_payment` turns them into posted payments reconciled with invoices. Framework only; individual provider modules are not studied. VDR-U12-C353 VDR-U12-C364 VDR-U12-C383 VDR-U12-C395

**D2 — Architecture, data and object relationships.** `payment.provider` (company-scoped, `state`, journal via `account_payment`), `payment.method`, `payment.token` (partner, provider, method, `active`), `payment.transaction` (provider, method, token, amount/currency, `state`, `operation`, `source_transaction_id`/`child_transaction_ids`, `is_post_processed`, `landing_route`). `account_payment` links `payment_id` and `invoice_ids` (relation `account_invoice_transaction_rel`) and account.payment gets `payment_transaction_id`, `payment_token_id`, `source_payment_id`. Interco extends `res.company` with a clearing journal and two clearing accounts. VDR-U12-C363 VDR-U12-C393 VDR-U12-C394 VDR-U12-C352

**D3 — Source, technical and workflow logic.**

Transaction state machine (`payment.transaction.state`):
- `draft -> pending` [_set_pending] VDR-U12-C370
- `draft | pending -> authorized` [_set_authorized; only if provider supports manual capture] VDR-U12-C370 VDR-U12-C367
- `draft | pending | authorized | error -> done` [_set_done; also updates source transaction state] VDR-U12-C370 VDR-U12-C372
- `draft | pending | authorized -> cancel` [_set_canceled] VDR-U12-C370
- `draft | pending | authorized -> error` [_set_error, also on provider request ValidationError] VDR-U12-C370 VDR-U12-C378
- Same-state requests are skipped (INFO log); other source states are refused (WARNING log); each accepted change sets `last_state_change`, `state_message` and `is_post_processed=False`. VDR-U12-C371

Processing: provider data -> `_process` -> find by reference/provider -> `_validate_amount` (amount rounded DOWN to precision and currency code; mismatch -> `error`) -> `_apply_updates` (provider-specific) -> `_tokenize` if requested and state in authorized/done. Child transactions: `_create_child_transaction` (capture/void prefix `P-`, refund prefix `R-` with negative amount); source state resolved by `_update_source_transaction_state` once children total equals source amount. VDR-U12-C379 VDR-U12-C380 VDR-U12-C381 VDR-U12-C373 VDR-U12-C372

Post-processing: base `_post_process` flags `is_post_processed`; cron `_cron_post_process` (every 10 min, retry window 4 days, per-transaction commit, error -> rollback and log) and the status poll controller call it; the cron is switched on only while some provider is not disabled. `account_payment._post_process`: for done transactions post draft invoices, create+post a payment if none (not validation, no done/cancel child) with reconciliation to the invoices (incl. EPD write-off), log messages; for cancel transactions cancel the payment. VDR-U12-C383 VDR-U12-C382 VDR-U12-C385 VDR-U12-C386 VDR-U12-C395 VDR-U12-C396

Interco flow: `account.move._post` override -> `_interco_filter_moves` -> `_check_interco_clearing(payments)`: per payment create clearing entry in the payment company (counterpart account vs inter-company payable/receivable) and reconcile with the payment counterpart; then create a settlement entry in the invoice company and reconcile with the invoice's receivable/payable lines. VDR-U12-C354 VDR-U12-C355 VDR-U12-C356 VDR-U12-C357

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Customer pays online -> transaction draft/pending -> done -> post-processing creates payment, posts invoices, reconciles; interco: invoice posted in other company triggers clearing. VDR-U12-C395 VDR-U12-C354 |
| 2 | Reversal / cancel / negative | cancel -> payment canceled; refund child transactions and refund payments; void of authorized; interco has no explicit reversal (entries are normal moves). VDR-U12-C395 VDR-U12-C376 VDR-U12-C375 |
| 3 | Multi-company / data scope | Provider, token, transaction rules by company; interco requires payment company different from invoice company; tokens must belong to the commercial partner. VDR-U12-C410 VDR-U12-C411 VDR-U12-C353 VDR-U12-C391 |
| 4 | Side effects / cross-module | Posts invoices, creates payments, logs chatter, creates saved tokens, portal link, journal/method line management, provider uninstall guards. VDR-U12-C395 VDR-U12-C381 VDR-U12-C402 VDR-U12-C403 |
| 5 | Configuration / optionality | Provider state, journal, tokenization, manual capture, portal-payment parameter, interco clearing journal/accounts per company. VDR-U12-C387 VDR-U12-C401 VDR-U12-C398 VDR-U12-C352 |
| 6 | Validation / constraints | Unique reference, authorized requires manual capture support, token must be active, amount/currency match, refund amount bounds, token ownership. VDR-U12-C365 VDR-U12-C367 VDR-U12-C368 VDR-U12-C380 VDR-U12-C399 VDR-U12-C391 |
| 7 | Roles / permissions | Transaction: Invoicing read/write/create, system full; tokens: employees read own, billing see all, system full; interco: none declared. See CAP-U12-09. VDR-U12-C407 VDR-U12-C410 VDR-U12-C412 VDR-U12-C409 |
| 8 | Scheduled / automated | Cron Payment: Post-process transactions every 10 minutes (active only with an enabled/test provider). VDR-U12-C382 VDR-U12-C385 |
| 9 | Exception / failure | Provider disabled -> UserError; provider request errors -> transaction error; post-process exceptions rolled back and logged; token from other partner -> AccessError. VDR-U12-C377 VDR-U12-C378 VDR-U12-C382 VDR-U12-C391 |
| 10 | Accounting / audit / compliance | Payments created in the provider's journal with provider method line; transaction keeps partner snapshot; messages on documents; interco clearing entries posted in clearing journals. VDR-U12-C396 VDR-U12-C369 VDR-U12-C356 |

**DB reconciliation (configuration only).** Providers: 25 rows, of which `custom` (enabled) and `demo` (test) are active, 23 disabled; payment modules `payment_custom` and `payment_demo` installed; cron "Payment: Post-process transactions" is active (10 min) consistent with an active provider; no transactions and no tokens; interco company fields (clearing journal, interco payable/receivable) are not set; portal-payment parameter is True. VDR-U12-C385 VDR-U12-C398 VDR-U12-C352

**Unknown / Runtime (RT) list.**
- RT: ordering/atomicity of status poll vs cron post-processing (both guard with `is_post_processed`). VDR-U12-C382 VDR-U12-C386
- RT: interco clearing in multi-currency and with partially paid invoices. VDR-U12-C355
- UNKNOWN: provider-specific `_apply_updates` / webhooks (out of scope). VDR-U12-C379


## CAP-U12-09 Roles, record rules, data scope, exceptions and scheduled jobs


**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 — Business purpose and process semantics.** This section collects who may do what with payments, registration, matching, statements, reconcile models, payment terms, payment methods and provider transactions, how data is scoped between companies, which failures stop a process, and which scheduled or automated jobs exist. It aggregates facts proven in CAP-U12-01 to 08 and confirms them against the restored database (configuration only). VDR-U12-C416 VDR-U12-C435

**D2 — Architecture, data and object relationships.** Roles are `res.groups` of the Accounting privilege (`group_account_readonly`, `group_account_invoice`, `group_account_basic`, `group_account_user`, `group_account_manager`) with an extra permission `group_validate_bank_account`. Access is via `ir.model.access` rows (account CSV and rows from other modules), global company `ir.rule` records, view-level group restrictions on buttons and server actions. VDR-U12-C416 VDR-U12-C417 VDR-U12-C428 VDR-U12-C437

**D3 — Source, technical and workflow logic.** State diagram: NOT APPLICABLE — cross-cutting capability without its own state machine. Role hierarchy: `basic -> invoice`, `user -> basic + readonly`, `manager -> invoice`. Rights to payments/registration/matching/methods sit on the Invoicing role; statements, reconcile models and the check wizard on Basic / Full accounting; payment terms on Administrator. Company rules are global (not bypassed by roles). A separate bank-trust permission gates `allow_out_payment`. VDR-U12-C417 VDR-U12-C419 VDR-U12-C425 VDR-U12-C436

**Ten-dimension table (cross-capability)**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Invoicing user registers payment; accountant (Basic+) manages statement lines and models; administrator manages terms. VDR-U12-C419 VDR-U12-C435 |
| 2 | Reversal / cancel / negative | Reset-to-draft on payments restricted to Invoicing group in the form; Unreconcile server action restricted to full-accounting; reviewed statement undo reserved to accountants (no-op in Community). VDR-U12-C437 VDR-U12-C438 |
| 3 | Multi-company / data scope | Global company rules on payments, statements and lines, reconcile models, terms, providers, transactions, tokens; invoicing users see all moves within company rules; branch handling via company hierarchy. VDR-U12-C428 VDR-U12-C429 VDR-U12-C430 |
| 4 | Side effects / cross-module | Other modules add ACL rows on matching and payment terms for sales, purchase and stock roles. VDR-U12-C431 VDR-U12-C432 VDR-U12-C433 |
| 5 | Configuration / optionality | Groups, ACL rows, rules in DB; crons in DB; no automation rules; payment restrictive audit trail flag off. VDR-U12-C441 VDR-U12-C442 VDR-U12-C443 |
| 6 | Validation / constraints | Trust permission needed to set allow_out_payment; ACL gaps (no unlink for wizards, no create on methods). VDR-U12-C426 VDR-U12-C419 |
| 7 | Roles / permissions | Matrix below. VDR-U12-C419 VDR-U12-C435 |
| 8 | Scheduled / automated | Crons: auto-post draft entries (daily), send invoices (daily), payment post-processing (10 min, active). No payment/statement/matching cron. VDR-U12-C441 VDR-U12-C440 |
| 9 | Exception / failure | Catalogue below. VDR-U12-C445 |
| 10 | Accounting / audit / compliance | Restrictive audit trail; global company isolation; bank-account trust control; mail tracking on payments. VDR-U12-C443 VDR-U12-C425 |

**Permission matrix (source CSV, confirmed against DB rows).**

| Model | Read-only accounting | Invoicing | Basic | Full accounting | Administrator |
|---|---|---|---|---|---|
| account.payment | R | CRUD | (via invoicing) | (via invoicing) | (via invoicing) |
| account.payment.register | - | R W C | via invoicing | via invoicing | via invoicing |
| account.payment.method / .line | R (all internal users R) | method R W D, line CRUD | - | - | - |
| account.partial.reconcile / full | R | CRUD | - | CRUD | via invoicing |
| account.bank.statement / line | R | R | CRUD | CRUD (implied) | via invoicing |
| account.reconcile.model / line | R | R C | CRUD | CRUD | via invoicing |
| account.payment.term / line | all internal users R | R | - | - | CRUD |
| print.prenumbered.checks | - | - | - | R W C | - |
| payment.transaction | - | R W C | - | - | system: CRUD |
| payment.provider / method / token | provider: system only; method and token: internal R | token: all via rule | - | - | system: CRUD |

(Derived from the claims linked in this section and in CAP-U12-01..08.) VDR-U12-C435 VDR-U12-C419

**Exception and failure catalogue (with claim links).** Posting/payment: no outstanding account (UserError), untrusted recipient bank (UserError), amount change with several liquidity lines (UserError), negative amount (DB constraint), duplicate check number (ValidationError). Registration: not posted, misc entry, blocked, nothing left, mixed company / account type, all batches untrusted. Matching: already reconciled, cancelled entries, mixed accounts / companies, non-reconcilable account, exchange journal/account not configured, cash-basis journal missing. Statements: no suspense account, non-contiguous selection, invalid entry shape, valid+complete statement line deletion. Terms: invalid line set, EPD parameters, deleting referenced term. Check printing: no valid payments, mixed journals, missing layout (RedirectWarning). Transactions: disabled provider, wrong state for capture/void/refund, amount/currency mismatch (state error), token ownership (AccessError). VDR-U12-C445 VDR-U12-C008 VDR-U12-C059 VDR-U12-C123 VDR-U12-C223 VDR-U12-C270 VDR-U12-C340 VDR-U12-C377

**DB reconciliation (configuration only).** ACL rows in DB for the studied models equal the account/payment CSV rows (see claim) plus extra rows from sale (salesman read on matches and terms), purchase (purchase user read on matches), sale_stock (stock manager, labelled "Administrator" in the group list, full on matches). All studied record rules are global. Crons: three payment/accounting related crons active (post draft entries daily, send invoices daily, payment post-processing 10 min); `base_automation` is installed but has zero rules; five server actions bound to payment, statement-line and move-line models exist (Post Payments, Print Checks, Unreconcile, Move to Account, Change Period). Company restrictive audit trail is off. VDR-U12-C435 VDR-U12-C436 VDR-U12-C441 VDR-U12-C442 VDR-U12-C443 VDR-U12-C434

**Unknown / Runtime (RT) list.**
- UNKNOWN: membership of real users in these groups (not queried: user data out of scope). VDR-U12-C446
- RT: effect of sibling-company and branch payments for users without parent-company access (code path read only). VDR-U12-C430


## NEUTRAL-REF TO CLAIM INDEX

| Neutral-ref | Claim-IDs |
|---|---|
| N-U12-001 | VDR-U12-C042, VDR-U12-C043 |
| N-U12-002 | VDR-U12-C003, VDR-U12-C014, VDR-U12-C015 |
| N-U12-003 | VDR-U12-C048, VDR-U12-C049, VDR-U12-C050 |
| N-U12-004 | VDR-U12-C001 |
| N-U12-005 | VDR-U12-C034 |
| N-U12-006 | VDR-U12-C018 |
| N-U12-007 | VDR-U12-C035, VDR-U12-C037, VDR-U12-C038, VDR-U12-C041 |
| N-U12-008 | VDR-U12-C004, VDR-U12-C005, VDR-U12-C006, VDR-U12-C007, VDR-U12-C023, VDR-U12-C026, VDR-U12-C031, VDR-U12-C032 |
| N-U12-009 | VDR-U12-C009, VDR-U12-C011 |
| N-U12-010 | VDR-U12-C010 |
| N-U12-011 | VDR-U12-C008, VDR-U12-C016, VDR-U12-C024, VDR-U12-C025 |
| N-U12-012 | VDR-U12-C017 |
| N-U12-013 | VDR-U12-C002 |
| N-U12-014 | VDR-U12-C012 |
| N-U12-015 | VDR-U12-C028, VDR-U12-C030 |
| N-U12-016 | VDR-U12-C022 |
| N-U12-017 | VDR-U12-C033 |
| N-U12-018 | VDR-U12-C021 |
| N-U12-019 | VDR-U12-C020 |
| N-U12-020 | VDR-U12-C029 |
| N-U12-021 | VDR-U12-C019 |
| N-U12-022 | VDR-U12-C027 |
| N-U12-023 | VDR-U12-C040 |
| N-U12-024 | VDR-U12-C046 |
| N-U12-025 | VDR-U12-C013, VDR-U12-C047 |
| N-U12-026 | VDR-U12-C036 |
| N-U12-027 | VDR-U12-C039 |
| N-U12-028 | VDR-U12-C052 |
| N-U12-029 | VDR-U12-C051 |
| N-U12-030 | VDR-U12-C044, VDR-U12-C045 |
| N-U12-031 | VDR-U12-C056 |
| N-U12-032 | VDR-U12-C111 |
| N-U12-033 | VDR-U12-C053, VDR-U12-C054, VDR-U12-C055, VDR-U12-C057, VDR-U12-C062 |
| N-U12-034 | VDR-U12-C058, VDR-U12-C059 |
| N-U12-035 | VDR-U12-C060, VDR-U12-C061, VDR-U12-C066, VDR-U12-C094 |
| N-U12-036 | VDR-U12-C063, VDR-U12-C064, VDR-U12-C065 |
| N-U12-037 | VDR-U12-C067, VDR-U12-C070, VDR-U12-C073, VDR-U12-C074 |
| N-U12-038 | VDR-U12-C068, VDR-U12-C069, VDR-U12-C071 |
| N-U12-039 | VDR-U12-C072, VDR-U12-C082, VDR-U12-C083, VDR-U12-C084, VDR-U12-C085, VDR-U12-C086 |
| N-U12-040 | VDR-U12-C076, VDR-U12-C077, VDR-U12-C079 |
| N-U12-041 | VDR-U12-C078 |
| N-U12-042 | VDR-U12-C075 |
| N-U12-043 | VDR-U12-C080, VDR-U12-C081 |
| N-U12-044 | VDR-U12-C087, VDR-U12-C088, VDR-U12-C089 |
| N-U12-045 | VDR-U12-C095, VDR-U12-C096, VDR-U12-C097, VDR-U12-C098, VDR-U12-C099 |
| N-U12-046 | VDR-U12-C100, VDR-U12-C101 |
| N-U12-047 | VDR-U12-C102, VDR-U12-C103 |
| N-U12-048 | VDR-U12-C104 |
| N-U12-049 | VDR-U12-C090, VDR-U12-C091, VDR-U12-C092, VDR-U12-C093 |
| N-U12-050 | VDR-U12-C105, VDR-U12-C106 |
| N-U12-051 | VDR-U12-C107 |
| N-U12-052 | VDR-U12-C108 |
| N-U12-053 | VDR-U12-C109 |
| N-U12-054 | VDR-U12-C110 |
| N-U12-055 | VDR-U12-C112 |
| N-U12-056 | VDR-U12-C113, VDR-U12-C116, VDR-U12-C117, VDR-U12-C121, VDR-U12-C125, VDR-U12-C152, VDR-U12-C153 |
| N-U12-057 | VDR-U12-C173 |
| N-U12-058 | VDR-U12-C123, VDR-U12-C124 |
| N-U12-059 | VDR-U12-C122, VDR-U12-C129 |
| N-U12-060 | VDR-U12-C114, VDR-U12-C115, VDR-U12-C133 |
| N-U12-061 | VDR-U12-C128 |
| N-U12-062 | VDR-U12-C130, VDR-U12-C131, VDR-U12-C132, VDR-U12-C240 |
| N-U12-063 | VDR-U12-C134 |
| N-U12-064 | VDR-U12-C135, VDR-U12-C137, VDR-U12-C138, VDR-U12-C142, VDR-U12-C143 |
| N-U12-065 | VDR-U12-C136, VDR-U12-C139, VDR-U12-C141 |
| N-U12-066 | VDR-U12-C140 |
| N-U12-067 | VDR-U12-C118, VDR-U12-C119, VDR-U12-C144, VDR-U12-C145, VDR-U12-C146 |
| N-U12-068 | VDR-U12-C147, VDR-U12-C148 |
| N-U12-069 | VDR-U12-C149, VDR-U12-C150, VDR-U12-C151 |
| N-U12-070 | VDR-U12-C126, VDR-U12-C127 |
| N-U12-071 | VDR-U12-C120, VDR-U12-C154, VDR-U12-C156 |
| N-U12-072 | VDR-U12-C159, VDR-U12-C160 |
| N-U12-073 | VDR-U12-C162, VDR-U12-C163 |
| N-U12-074 | VDR-U12-C157, VDR-U12-C158 |
| N-U12-075 | VDR-U12-C167, VDR-U12-C168, VDR-U12-C169 |
| N-U12-076 | VDR-U12-C170 |
| N-U12-077 | VDR-U12-C155, VDR-U12-C161 |
| N-U12-078 | VDR-U12-C166 |
| N-U12-079 | VDR-U12-C165 |
| N-U12-080 | VDR-U12-C164 |
| N-U12-081 | VDR-U12-C174 |
| N-U12-082 | VDR-U12-C172 |
| N-U12-083 | VDR-U12-C171 |
| N-U12-084 | VDR-U12-C175, VDR-U12-C177 |
| N-U12-085 | VDR-U12-C202, VDR-U12-C203 |
| N-U12-086 | VDR-U12-C180, VDR-U12-C181, VDR-U12-C186 |
| N-U12-087 | VDR-U12-C184 |
| N-U12-088 | VDR-U12-C182, VDR-U12-C183 |
| N-U12-089 | VDR-U12-C187, VDR-U12-C188 |
| N-U12-090 | VDR-U12-C185 |
| N-U12-091 | VDR-U12-C178, VDR-U12-C179, VDR-U12-C190 |
| N-U12-092 | VDR-U12-C193, VDR-U12-C194, VDR-U12-C195 |
| N-U12-093 | VDR-U12-C196, VDR-U12-C197, VDR-U12-C198, VDR-U12-C199, VDR-U12-C201 |
| N-U12-094 | VDR-U12-C200 |
| N-U12-095 | VDR-U12-C191, VDR-U12-C192 |
| N-U12-096 | VDR-U12-C189 |
| N-U12-097 | VDR-U12-C176 |
| N-U12-098 | VDR-U12-C204 |
| N-U12-099 | VDR-U12-C205, VDR-U12-C218, VDR-U12-C219 |
| N-U12-100 | VDR-U12-C220 |
| N-U12-101 | VDR-U12-C241 |
| N-U12-102 | VDR-U12-C206, VDR-U12-C212, VDR-U12-C213, VDR-U12-C214, VDR-U12-C215 |
| N-U12-103 | VDR-U12-C209, VDR-U12-C210, VDR-U12-C211 |
| N-U12-104 | VDR-U12-C207, VDR-U12-C208, VDR-U12-C226 |
| N-U12-105 | VDR-U12-C216, VDR-U12-C217, VDR-U12-C239 |
| N-U12-106 | VDR-U12-C221, VDR-U12-C222 |
| N-U12-107 | VDR-U12-C223, VDR-U12-C224 |
| N-U12-108 | VDR-U12-C225 |
| N-U12-109 | VDR-U12-C227 |
| N-U12-110 | VDR-U12-C228, VDR-U12-C229 |
| N-U12-111 | VDR-U12-C230 |
| N-U12-112 | VDR-U12-C231, VDR-U12-C232 |
| N-U12-113 | VDR-U12-C233, VDR-U12-C234 |
| N-U12-114 | VDR-U12-C235 |
| N-U12-115 | VDR-U12-C236 |
| N-U12-116 | VDR-U12-C238 |
| N-U12-117 | VDR-U12-C242 |
| N-U12-118 | VDR-U12-C243, VDR-U12-C244 |
| N-U12-119 | VDR-U12-C245 |
| N-U12-120 | VDR-U12-C246, VDR-U12-C247, VDR-U12-C248 |
| N-U12-121 | VDR-U12-C249, VDR-U12-C250 |
| N-U12-122 | VDR-U12-C251, VDR-U12-C252 |
| N-U12-123 | VDR-U12-C253, VDR-U12-C254, VDR-U12-C255 |
| N-U12-124 | VDR-U12-C256 |
| N-U12-125 | VDR-U12-C258 |
| N-U12-126 | VDR-U12-C260 |
| N-U12-127 | VDR-U12-C237 |
| N-U12-128 | VDR-U12-C262, VDR-U12-C263, VDR-U12-C264, VDR-U12-C265, VDR-U12-C266 |
| N-U12-129 | VDR-U12-C261 |
| N-U12-227 | VDR-U12-C257 |
| N-U12-130 | VDR-U12-C259 |
| N-U12-131 | VDR-U12-C267 |
| N-U12-132 | VDR-U12-C268 |
| N-U12-133 | VDR-U12-C274, VDR-U12-C277 |
| N-U12-134 | VDR-U12-C271, VDR-U12-C272 |
| N-U12-135 | VDR-U12-C269, VDR-U12-C273 |
| N-U12-136 | VDR-U12-C275 |
| N-U12-137 | VDR-U12-C276, VDR-U12-C291, VDR-U12-C292, VDR-U12-C293 |
| N-U12-138 | VDR-U12-C278 |
| N-U12-139 | VDR-U12-C289, VDR-U12-C290 |
| N-U12-140 | VDR-U12-C270, VDR-U12-C280 |
| N-U12-141 | VDR-U12-C279, VDR-U12-C281, VDR-U12-C282 |
| N-U12-142 | VDR-U12-C302 |
| N-U12-143 | VDR-U12-C296, VDR-U12-C297 |
| N-U12-144 | VDR-U12-C298, VDR-U12-C299, VDR-U12-C300, VDR-U12-C301, VDR-U12-C303, VDR-U12-C304, VDR-U12-C313, VDR-U12-C314, VDR-U12-C315 |
| N-U12-145 | VDR-U12-C309, VDR-U12-C312 |
| N-U12-146 | VDR-U12-C294, VDR-U12-C295 |
| N-U12-147 | VDR-U12-C310 |
| N-U12-148 | VDR-U12-C311 |
| N-U12-149 | VDR-U12-C283 |
| N-U12-150 | VDR-U12-C286, VDR-U12-C287, VDR-U12-C288 |
| N-U12-151 | VDR-U12-C284, VDR-U12-C285 |
| N-U12-152 | VDR-U12-C317 |
| N-U12-153 | VDR-U12-C316 |
| N-U12-154 | VDR-U12-C305 |
| N-U12-155 | VDR-U12-C306, VDR-U12-C307, VDR-U12-C308 |
| N-U12-156 | VDR-U12-C329 |
| N-U12-157 | VDR-U12-C351 |
| N-U12-158 | VDR-U12-C318, VDR-U12-C319, VDR-U12-C320 |
| N-U12-159 | VDR-U12-C323, VDR-U12-C324 |
| N-U12-160 | VDR-U12-C344 |
| N-U12-161 | VDR-U12-C321, VDR-U12-C322, VDR-U12-C332, VDR-U12-C333, VDR-U12-C336 |
| N-U12-162 | VDR-U12-C330, VDR-U12-C331, VDR-U12-C343 |
| N-U12-163 | VDR-U12-C337 |
| N-U12-164 | VDR-U12-C340 |
| N-U12-165 | VDR-U12-C339, VDR-U12-C347 |
| N-U12-166 | VDR-U12-C341, VDR-U12-C342 |
| N-U12-167 | VDR-U12-C334, VDR-U12-C335 |
| N-U12-168 | VDR-U12-C326, VDR-U12-C328, VDR-U12-C349 |
| N-U12-169 | VDR-U12-C327, VDR-U12-C348 |
| N-U12-170 | VDR-U12-C325 |
| N-U12-171 | VDR-U12-C345, VDR-U12-C346 |
| N-U12-172 | VDR-U12-C338 |
| N-U12-173 | VDR-U12-C350 |
| N-U12-174 | VDR-U12-C358 |
| N-U12-175 | VDR-U12-C359 |
| N-U12-176 | VDR-U12-C354 |
| N-U12-177 | VDR-U12-C353 |
| N-U12-178 | VDR-U12-C355, VDR-U12-C356, VDR-U12-C357 |
| N-U12-179 | VDR-U12-C352, VDR-U12-C361 |
| N-U12-180 | VDR-U12-C362 |
| N-U12-181 | VDR-U12-C363, VDR-U12-C393 |
| N-U12-182 | VDR-U12-C360 |
| N-U12-183 | VDR-U12-C364 |
| N-U12-184 | VDR-U12-C370 |
| N-U12-185 | VDR-U12-C371 |
| N-U12-186 | VDR-U12-C367 |
| N-U12-187 | VDR-U12-C365, VDR-U12-C366 |
| N-U12-188 | VDR-U12-C369 |
| N-U12-189 | VDR-U12-C379, VDR-U12-C380, VDR-U12-C381, VDR-U12-C392 |
| N-U12-190 | VDR-U12-C372, VDR-U12-C373 |
| N-U12-191 | VDR-U12-C374, VDR-U12-C375, VDR-U12-C376, VDR-U12-C377, VDR-U12-C378 |
| N-U12-192 | VDR-U12-C368, VDR-U12-C389, VDR-U12-C390 |
| N-U12-193 | VDR-U12-C391 |
| N-U12-194 | VDR-U12-C382, VDR-U12-C383, VDR-U12-C384, VDR-U12-C386 |
| N-U12-195 | VDR-U12-C385 |
| N-U12-196 | VDR-U12-C395 |
| N-U12-197 | VDR-U12-C394, VDR-U12-C396 |
| N-U12-198 | VDR-U12-C397 |
| N-U12-199 | VDR-U12-C398 |
| N-U12-200 | VDR-U12-C399, VDR-U12-C400 |
| N-U12-201 | VDR-U12-C401, VDR-U12-C402, VDR-U12-C403, VDR-U12-C404, VDR-U12-C405 |
| N-U12-202 | VDR-U12-C387, VDR-U12-C388 |
| N-U12-203 | VDR-U12-C407, VDR-U12-C408, VDR-U12-C409 |
| N-U12-204 | VDR-U12-C410, VDR-U12-C411, VDR-U12-C412, VDR-U12-C413 |
| N-U12-205 | VDR-U12-C414 |
| N-U12-206 | VDR-U12-C415 |
| N-U12-207 | VDR-U12-C406 |
| N-U12-208 | VDR-U12-C416 |
| N-U12-209 | VDR-U12-C418 |
| N-U12-210 | VDR-U12-C417 |
| N-U12-211 | VDR-U12-C420, VDR-U12-C421, VDR-U12-C435 |
| N-U12-212 | VDR-U12-C422, VDR-U12-C423 |
| N-U12-213 | VDR-U12-C424 |
| N-U12-214 | VDR-U12-C419 |
| N-U12-215 | VDR-U12-C425, VDR-U12-C426, VDR-U12-C427 |
| N-U12-216 | VDR-U12-C428, VDR-U12-C430, VDR-U12-C436 |
| N-U12-217 | VDR-U12-C429 |
| N-U12-218 | VDR-U12-C431, VDR-U12-C432, VDR-U12-C433 |
| N-U12-219 | VDR-U12-C440, VDR-U12-C441 |
| N-U12-220 | VDR-U12-C442 |
| N-U12-221 | VDR-U12-C437, VDR-U12-C439 |
| N-U12-222 | VDR-U12-C443, VDR-U12-C444 |
| N-U12-223 | VDR-U12-C434 |
| N-U12-224 | VDR-U12-C445 |
| N-U12-225 | VDR-U12-C446 |
| N-U12-226 | VDR-U12-C438 |

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U12-C001 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:39 | In Process | FACT | always | — | account.payment.state selection is draft, in_process, paid, canceled, rejected; required, default draft, stored, computed (_compute_state) but readonly=False so it is directly writable, tracked, copy=False | N-U12-004 |
| VDR-U12-C002 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:201 | CHECK(amount >= 0.0) | FACT | always | — | SQL constraint _check_amount_not_negative: amount >= 0; direction is carried by payment_type (outbound/inbound) | N-U12-013 |
| VDR-U12-C003 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:100 | 'outbound', 'Send' | FACT | always | — | payment_type selection outbound (Send) / inbound (Receive), default inbound; partner_type customer/supplier, default customer; both required and tracked | N-U12-002 |
| VDR-U12-C004 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:215 | _seek_for_lines | FACT | always | — | _seek_for_lines splits move lines into liquidity (account in _get_valid_liquidity_accounts), counterpart (receivable/payable type or company transfer account) and write-off lines; when only one write-off line exists it is promoted to a missing liquidity/counterpart line | N-U12-008 |
| VDR-U12-C005 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:245 | _get_valid_liquidity_accounts | FACT | always | — | Valid liquidity accounts = journal default account, plus the payment method line account, plus all inbound and outbound method line accounts of the journal, plus the payment outstanding_account_id | N-U12-008 |
| VDR-U12-C006 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:288 | _prepare_move_liquidity_lines | FACT | always | — | Liquidity line values use account_id = outstanding_account_id, date_maturity = payment date, partner, currency, balance and amount_currency from the default values | N-U12-008 |
| VDR-U12-C007 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:300 | _prepare_move_counterpart_lines | FACT | always | — | Counterpart line values use account_id = destination_account_id with the same date_maturity, partner and currency | N-U12-008 |
| VDR-U12-C008 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:326 | without an outstanding | FACT | always | — | _prepare_move_lines_per_type raises UserError when outstanding_account_id is empty (message names the payment method and journal) | N-U12-011 |
| VDR-U12-C009 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:349 | Prepare liquidity lines | FACT | always | — | Liquidity amount_currency = +amount for inbound, -amount for outbound; counterpart amounts = -liquidity - write_off - withholding so the entry balances | N-U12-009 |
| VDR-U12-C010 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:359 | force_balance is not None | FACT | always | — | When no write-off values are given and force_balance is supplied, the liquidity balance takes sign and abs of force_balance; otherwise amount is converted to company currency at payment date with currency_id._convert | N-U12-010 |
| VDR-U12-C011 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:338 | _prepare_move_withholding_lines | FACT | always | — | Withholding lines come from the hook _prepare_move_withholding_lines (empty in base); write-off and withholding lines cannot be combined: write-off lines are dropped when withholding lines exist | N-U12-009 |
| VDR-U12-C012 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:418 | payment.move_id.name | FACT | always | — | _compute_name sets name from move_id.name once the payment is in_process or paid (else from the account.payment sequence); drafts have no name (display name falls back to Draft Payment) | N-U12-014 |
| VDR-U12-C013 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:428 | _compute_journal_id | FACT | always | — | Journal defaults from the partner's default payment method line (property_inbound/outbound_payment_method_line_id) for new records, otherwise the first bank/cash/credit journal of the company | N-U12-025 |
| VDR-U12-C014 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:449 | _compute_company_id | FACT | always | — | company_id is computed from journal_id; if the journal company is not in the payment company's parents the accessible branch of the journal company is taken | N-U12-002 |
| VDR-U12-C015 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:620 | _compute_currency_id | FACT | always | — | currency_id defaults to the journal currency or the journal company currency | N-U12-002 |
| VDR-U12-C016 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:625 | _compute_outstanding_account_id | FACT | always | — | outstanding_account_id is computed from payment_method_line_id.payment_account_id | N-U12-011 |
| VDR-U12-C017 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:630 | _compute_destination_account_id | FACT | always | — | destination_account_id = partner receivable (customer) or payable (supplier); with no partner the first asset_receivable / liability_payable account of the company | N-U12-012 |
| VDR-U12-C018 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:455 | _compute_state | FACT | always | — | _compute_state: for paid/in_process payments with a move: paid if the liquidity residual is zero in company currency or no liquidity account is reconcilable, else in_process; additionally an in_process payment whose reconciled invoices/bills are all payment_state paid becomes paid and its is_matched is re-added to compute | N-U12-006 |
| VDR-U12-C019 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:474 | _compute_reconciliation_status | FACT | always | — | is_matched: True when the journal default account is among liquidity accounts, else liquidity residual zero; is_reconciled: counterpart+write-off lines on reconcilable accounts have zero residual; no outstanding account -> is_matched = state == paid | N-U12-021 |
| VDR-U12-C020 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:868 | _check_payment_method_line_id | FACT | always | — | Constraint: payment_method_line_id must be set and, if the method line has a journal, it must equal the payment journal | N-U12-019 |
| VDR-U12-C021 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:879 | _check_move_id | FACT | always | — | Constraint: state not in (draft, canceled) with an outstanding account and no move_id raises ValidationError | N-U12-018 |
| VDR-U12-C022 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:793 | _fetch_duplicate_reference | FACT | always | — | Duplicate detection matches other payments with same partner, company, date, payment_type and amount in draft or in_process state; skipped for in_process payments and for records without partner or amount | N-U12-016 |
| VDR-U12-C023 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:922 | write_off_line_vals_list[i] is not None | FACT | always | — | create() pops write_off_line_vals, force_balance and line_ids from vals; if any is supplied the journal entry is generated at once via _generate_journal_entry and move-related fields are propagated to the move | N-U12-008 |
| VDR-U12-C024 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:914 | accounting_installed | FACT | Community (invoice in-payment hook returns paid) | — | create() sets outstanding_account_id from _get_outstanding_account when the in-payment hook is not 'in_payment' (accounting_installed False) and none is set, or when context force_payment_move is set | N-U12-011 |
| VDR-U12-C025 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:940 | _get_outstanding_account | FACT | always | — | _get_outstanding_account takes the chart-template record account_journal_payment_debit_account_id (inbound) or ..._credit_account_id (outbound), else company.transfer_account_id; raises UserError No outstanding account could be found if neither | N-U12-011 |
| VDR-U12-C026 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:951 | def write | FACT | always | — | write(): when vals state is in_process or paid and move_id not in vals, entries are generated for payments without a move and draft moves are posted before super().write; afterwards the entry is synchronised | N-U12-008 |
| VDR-U12-C027 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:961 | def unlink | FACT | always | — | unlink(): non-draft moves are reset to draft and all moves unlinked, then reconciled invoices' payment_state is added to compute | N-U12-022 |
| VDR-U12-C028 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1008 | pay.move_id.state == 'posted' | FACT | always | — | _synchronize_to_moves skips payments whose move is posted: only draft entries are rewritten | N-U12-015 |
| VDR-U12-C029 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1013 | multiple liquidity lines | FACT | always | — | Changing amount on a draft payment with more than one liquidity line raises UserError | N-U12-020 |
| VDR-U12-C030 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1067 | _get_trigger_fields_to_synchronize | FACT | always | — | Synchronisation triggers: date, amount, payment_type, partner_type, payment_reference, currency_id, partner_id, destination_account_id, partner_bank_id, journal_id (account_check_printing adds check_number) | N-U12-015 |
| VDR-U12-C031 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1073 | _generate_journal_entry | FACT | always | — | _generate_journal_entry creates moves only for payments with an outstanding account and no move, then writes move_id and state in_process on each payment | N-U12-008 |
| VDR-U12-C032 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1085 | _generate_move_vals | FACT | always | — | Move values: move_type entry, ref = memo, date, journal, company, partner, currency, partner_bank_id, lines from _prepare_move_line_default_vals, origin_payment_id = payment id | N-U12-008 |
| VDR-U12-C033 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1135 | require_partner_bank_account | FACT | always | — | action_post raises UserError for outbound payments whose method requires a bank account (require_partner_bank_account) when partner_bank_id.allow_out_payment is not set; require_* depends on _get_method_codes_needing_bank_account which returns [] in base | N-U12-017 |
| VDR-U12-C034 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1145 | asset_cash | FACT | always | — | action_post: payments whose outstanding account type is asset_cash are set to paid; payments in state False/draft/in_process are set to in_process (avoids going back one state from list-view confirm) | N-U12-005 |
| VDR-U12-C035 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1150 | def action_validate | FACT | always | — | action_validate sets state paid | N-U12-007 |
| VDR-U12-C036 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1153 | def action_reject | FACT | always | — | action_reject only sets state rejected; the move and any reconciliation are untouched in this code | N-U12-026 |
| VDR-U12-C037 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1156 | def action_cancel | FACT | always | — | action_cancel sets state canceled, unlinks draft moves and calls button_cancel on non-draft moves | N-U12-007 |
| VDR-U12-C038 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1165 | def action_draft | FACT | always | — | action_draft sets state draft then calls button_draft on the entry | N-U12-007 |
| VDR-U12-C039 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6280 | self.state = 'draft' | INFERENCE | always | RT | Inference from grep of remove_move_reconcile call sites (account_move.py unlink/_reverse_moves/button_cancel, account_move_line.py write/unlink, statement line undo): button_draft sets state draft without removing partial reconciles; the effect of a reset-to-draft of a reconciled payment entry needs runtime confirmation | N-U12-027 |
| VDR-U12-C040 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6395 | self.payment_ids.state | FACT | always | — | account.move.button_cancel removes reconciliations, sets payment_ids.state to canceled and writes state cancel | N-U12-023 |
| VDR-U12-C041 | FUNCTION MAPPING REQUIRED | account/views/account_payment_view.xml:161 | action_cancel | FACT | always | — | Payment form: Cancel visible when record exists and state is draft, or in_process and is_sent; Validate visible when in_process without move; Reject when in_process and is_sent; Reset to Draft hidden in draft and restricted to account.group_account_invoice | N-U12-007 |
| VDR-U12-C042 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1250 | payment_ids | FACT | always | — | account.move gets the reverse One2many payment_ids (account.payment.move_id); account.move.origin_payment_id is the many2one back to the payment | N-U12-001 |
| VDR-U12-C043 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:140 | invoice_ids | FACT | always | — | invoice_ids many2many (relation account_move__account_payment) holds invoices linked to the payment even without entry or reconciliation | N-U12-001 |
| VDR-U12-C044 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7258 | origin_payment_id | FACT | always | — | account.move._track_subtype forwards state tracking of non-invoice moves to origin_payment_id._message_track | N-U12-030 |
| VDR-U12-C045 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:16 | tracking=True | FACT | always | — | date, state, partner_bank_id, payment_type, partner_type, memo, payment_reference, partner_id, amount_signed and payment_method_id are tracked fields | N-U12-030 |
| VDR-U12-C046 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:709 | payment_sequence | FACT | always | — | Journal.payment_sequence defaults to True for bank, cash and credit journal types (dedicated payment sequence) | N-U12-024 |
| VDR-U12-C047 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:593 | _get_payment_method_codes_to_exclude | FACT | always | — | available_payment_method_line_ids come from journal._get_available_payment_method_lines(payment_type) minus codes returned by the hook _get_payment_method_codes_to_exclude (empty in base) | N-U12-025 |
| VDR-U12-C048 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:114 | access_account_payment, | FACT | always | — | ACL: account.payment full CRUD for account.group_account_invoice | N-U12-003 |
| VDR-U12-C049 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:113 | access_account_payment_readonly | FACT | always | — | ACL: account.payment read-only for account.group_account_readonly | N-U12-003 |
| VDR-U12-C050 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:218 | account_payment_comp_rule | FACT | always | — | Record rule account_payment_comp_rule: company_id in company_ids (global rule) | N-U12-003 |
| VDR-U12-C051 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:68 | paired_internal_transfer_payment_id | INFERENCE | always | — | paired_internal_transfer_payment_id is declared (help text describes pairing) but grep over odoo/addons finds no other reference outside the field definition, so no producer exists in Community | N-U12-029 |
| VDR-U12-C052 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:468 | all(invoice.payment_state == 'paid' | UNKNOWN | Community | RT | Interaction between the line-468 rule (in_process -> paid when all reconciled invoices are paid) and the invoice hook that returns paid in Community means a normal payment may show paid before any bank match; requires execution | N-U12-028 |
| VDR-U12-C053 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6101 | You can only register payment | FACT | always | — | account.move.action_register_payment raises UserError unless all moves are posted, then calls action_force_register_payment | N-U12-033 |
| VDR-U12-C054 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6106 | miscellaneous entries | FACT | always | — | action_force_register_payment raises UserError for move_type entry | N-U12-033 |
| VDR-U12-C055 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6108 | blocked invoices | FACT | always | — | action_force_register_payment raises UserError when any move payment_state is blocked | N-U12-033 |
| VDR-U12-C056 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1369 | account.payment.register | FACT | always | — | account.move.line.action_register_payment opens the account.payment.register wizard as a dialog with context active_model account.move.line and active_ids; action_payment_items_register_payment adds default_group_payment True | N-U12-031 |
| VDR-U12-C057 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:942 | active_model | FACT | always | — | default_get accepts only active_model account.move (all lines) or account.move.line, else UserError | N-U12-033 |
| VDR-U12-C058 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:960 | valid_account_types | FACT | always | — | Lines kept for payment: account type in _get_valid_payment_account_types (asset_receivable, liability_payable) and a non-zero residual in line currency (or company currency if none) | N-U12-034 |
| VDR-U12-C059 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:975 | nothing left to pay | FACT | always | — | default_get raises UserError when no line has anything left to pay | N-U12-034 |
| VDR-U12-C060 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:977 | different companies | FACT | always | — | default_get refuses lines from more than one root company, and lines from different branches (sibling companies) unless the user can access the root company | N-U12-035 |
| VDR-U12-C061 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:981 | both inbound and outbound | FACT | always | — | default_get refuses mixing receivable and payable account types | N-U12-035 |
| VDR-U12-C062 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:983 | blocked invoices | FACT | always | — | default_get refuses lines whose move payment_state is blocked | N-U12-033 |
| VDR-U12-C063 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:266 | _get_line_batch_key | FACT | always | — | Batch key = partner_id, account_id, currency_id, partner_bank_id (invoice partner_bank_id for invoices/receipts) and partner_type (customer if receivable else supplier) | N-U12-036 |
| VDR-U12-C064 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:332 | _compute_batches | FACT | always | — | _compute_batches groups lines by key; a partner whose inbound lines and outbound lines each have a single bank has its compatible batches merged and the partner_bank_id taken from the resulting direction | N-U12-036 |
| VDR-U12-C065 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:388 | balance = sum(lines.mapped('balance')) | FACT | always | — | Batch payment_type is inbound when the sum of line balances is positive, else outbound | N-U12-036 |
| VDR-U12-C066 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:345 | different companies | FACT | always | — | _compute_batches raises UserError for lines belonging to different root companies and for no lines | N-U12-035 |
| VDR-U12-C067 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:429 | _compute_from_lines | FACT | always | — | With a single batch the wizard is editable (can_edit_wizard True) and takes partner, type, amounts from the batch; with several batches partner and amounts are cleared and can_edit_wizard is False | N-U12-037 |
| VDR-U12-C068 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:483 | _compute_group_payment | FACT | always | — | group_payment defaults to True only when the wizard is editable and the batch has exactly one move, else False | N-U12-038 |
| VDR-U12-C069 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:457 | _compute_can_group_payments | FACT | always | — | can_group_payments (checkbox visible) is true for a single batch with several lines that are not all one invoice; for several batches it is true if any batch has other than one payable line | N-U12-038 |
| VDR-U12-C070 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1235 | edit_mode = self.can_edit_wizard | FACT | always | — | edit_mode = can_edit_wizard and (single line in first batch or group_payment); in edit mode one payment is created from wizard values | N-U12-037 |
| VDR-U12-C071 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1256 | Don't group payments | FACT | always | — | Without edit mode and group_payment False, one sub-batch per move is created (payment type from the line balance sign) restricted to lines_to_pay; installments modes next/overdue/before_date restrict lines_to_pay via _get_total_amounts_to_pay | N-U12-038 |
| VDR-U12-C072 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1254 | lines_to_pay | FACT | always | RT | lines_to_pay = installment-selected lines when installments_mode is next/overdue/before_date, else all wizard lines | N-U12-039 |
| VDR-U12-C073 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:993 | _create_payment_vals_from_wizard | FACT | always | — | Edit-mode payment values: date, amount, payment_type, partner_type, memo=communication, journal, company, currency, partner, partner_bank, method line, destination_account_id of first line, empty write_off_line_vals filled by difference handling | N-U12-037 |
| VDR-U12-C074 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1054 | _create_payment_vals_from_batch | FACT | always | — | Batch-mode payment values use the batch source_amount_currency in the source currency, memo from _get_communication of the batch lines, journal bank account for inbound partner bank, and fall back to the journal's first method of the batch direction if the selected method has another direction | N-U12-037 |
| VDR-U12-C075 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1090 | epd_applied | FACT | always | — | In batch mode with an early payment discount applied the payment amount becomes the discounted amount and write-off lines come from _get_invoice_counterpart_amls_for_early_payment_discount | N-U12-042 |
| VDR-U12-C076 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:834 | _compute_payment_difference | FACT | always | — | payment_difference = amount_for_difference (or full_amount_for_difference in full mode) minus the entered amount; 0 when no payment date | N-U12-040 |
| VDR-U12-C077 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:862 | _compute_payment_difference_handling | FACT | always | — | payment_difference_handling defaults to reconcile (Mark as fully paid) when early_payment_discount_mode is true, otherwise open (Keep open); False if the wizard is not editable | N-U12-040 |
| VDR-U12-C078 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:321 | _compute_show_payment_difference | FACT | always | — | show_payment_difference requires a non-zero difference, not epd mode, can_edit_wizard, (cannot group or group_payment) and a method line with payment_account_id | N-U12-041 |
| VDR-U12-C079 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1038 | write_off_amount_currency | FACT | always | — | Write-off line: amount_currency = payment_difference for inbound, -payment_difference for outbound; name = writeoff_label; account = writeoff_account_id; converted to company currency at payment date; added only if the difference is non-zero and handling is reconcile | N-U12-040 |
| VDR-U12-C080 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1029 | writeoff_is_exchange_account | FACT | always | — | If the write-off account is the company income or expense currency-exchange account (and handling reconcile, currencies differ), force_balance = sum of residuals is passed; with same currencies rate is forced in the reconciliation (to_process rate = abs(total residual currency / amount)) | N-U12-043 |
| VDR-U12-C081 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:848 | _compute_writeoff_is_exchange_account | FACT | always | — | writeoff_is_exchange_account true when editable, handling reconcile, wizard currency differs from source currency and the write-off account is the company expense or income exchange account | N-U12-043 |
| VDR-U12-C082 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:741 | _compute_amount | FACT | always | — | amount defaults to amount_by_default from _get_total_amounts_to_pay unless a custom user amount exists | N-U12-039 |
| VDR-U12-C083 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:628 | _get_total_amounts_to_pay | FACT | always | — | _get_total_amounts_to_pay classifies each line's installments (early_payment_discount, overdue, next, before_date) and returns amount_by_default, full_amount, amount_for_difference, full_amount_for_difference, epd_applied, installment_mode and the lines concerned | N-U12-039 |
| VDR-U12-C084 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3327 | _get_installments_data | FACT | always | — | Installments data per payment term line: early payment discount if eligible; else overdue (due before payment date), next (first not overdue) or before_date (due before the context next payment date); reconciled lines skipped | N-U12-039 |
| VDR-U12-C085 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:750 | _compute_installments_mode | FACT | always | — | installments_mode becomes full when the amount equals full_amount, the installment mode when it equals amount_by_default, and full otherwise | N-U12-039 |
| VDR-U12-C086 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:704 | _onchange_amount | FACT | always | — | An amount different from every computed reference amount is stored as custom_user_amount (with its currency) and is kept across date/currency changes | N-U12-039 |
| VDR-U12-C087 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:491 | _compute_currency_id | FACT | always | — | Wizard currency = journal currency, else source currency, else company currency | N-U12-044 |
| VDR-U12-C088 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:597 | _convert_to_wizard_currency | FACT | always | — | Residual amounts are converted into the wizard currency at the payment date unless same currency, in which case the foreign amount residual is used directly | N-U12-044 |
| VDR-U12-C089 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1129 | currency different than | FACT | always | RT | In edit mode with a payment currency different from the lines, if the amount in currency matches the converted source residual, the balance of the first debit and credit lines is adjusted so the source lines are fully paid | N-U12-044 |
| VDR-U12-C090 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1123 | skip_invoice_sync=True | FACT | always | — | _init_payments creates account.payment records with skip_invoice_sync | N-U12-049 |
| VDR-U12-C091 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1185 | skip_sale_auto_invoice_send | FACT | always | — | _post_payments calls action_post on all created payments with skip_sale_auto_invoice_send | N-U12-049 |
| VDR-U12-C092 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1187 | _reconcile_payments | FACT | always | — | _reconcile_payments reconciles, per account, unreconciled receivable/payable lines of the posted payment move with the batch lines, using a forced rate when provided, then links the payment to the documents via matched_payment_ids | N-U12-049 |
| VDR-U12-C093 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1296 | clean_context | FACT | always | — | Payments are created with a cleaned context so default_* keys of the wizard do not leak into the payment | N-U12-049 |
| VDR-U12-C094 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1286 | from_sibling_companies | FACT | always | — | For lines of sibling companies the wizard runs as sudo (company taken as root company) and may suppress the redirect to payments | N-U12-035 |
| VDR-U12-C095 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:194 | _get_batch_available_journals | FACT | always | — | Available journals: company-domain journals of type bank, cash or credit having inbound (or outbound) payment method lines for the batch direction | N-U12-045 |
| VDR-U12-C096 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:212 | _get_batch_journal | FACT | always | — | Default journal search order: currency and partner bank, partner bank only, currency only, any available journal of the (root) company | N-U12-045 |
| VDR-U12-C097 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:504 | _compute_journal_id | FACT | always | — | Journal default: the single preferred payment method line's journal of the documents, else batch journal when editable, else first available | N-U12-045 |
| VDR-U12-C098 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:553 | _compute_payment_method_line_id | FACT | always | — | Method default: keep current if available, else the documents' preferred method line when unique and available, else first available method line of the journal | N-U12-045 |
| VDR-U12-C099 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1534 | _compute_preferred_payment_method_line_id | FACT | always | — | Document preferred method line comes from the partner's property_inbound (sale documents) or property_outbound payment method line for the company | N-U12-045 |
| VDR-U12-C100 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:253 | _get_batch_available_partner_banks | FACT | always | — | Available recipient banks: inbound = journal.bank_account_id; outbound = partner banks of the lines with company False or the root company | N-U12-046 |
| VDR-U12-C101 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:531 | _compute_partner_bank_id | FACT | always | — | Recipient bank defaults to the batch bank if still available, else the first available bank; none when not editable | N-U12-046 |
| VDR-U12-C102 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:399 | _compute_trust_values | FACT | always | — | Trust values: with require_partner_bank_account, batches with no bank count as missing, banks with allow_out_payment False count as untrusted; counts feed the warning banner | N-U12-047 |
| VDR-U12-C103 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1221 | Skip batches that are not valid | FACT | always | — | _create_payments skips batches without a trusted bank when required and raises UserError (bank must be manually validated) if none remain | N-U12-047 |
| VDR-U12-C104 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:177 | _get_communication | FACT | always | — | Memo: single move -> payment_reference or ref or name; several moves with an outbound one -> sorted list of those references; otherwise company.get_next_batch_payment_communication() | N-U12-048 |
| VDR-U12-C105 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:912 | _fetch_duplicate_reference | FACT | always | — | Wizard duplicate check builds a dummy account.payment and reuses _fetch_duplicate_reference with states draft and posted | N-U12-050 |
| VDR-U12-C106 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:585 | _compute_actionable_errors | FACT | always | — | actionable_errors warns when the documents already have reconciled payments in state in_process (don't pay twice) and links to them | N-U12-050 |
| VDR-U12-C107 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1309 | is_register_payment_on_draft | FACT | always | — | action_create_payments forces payment_difference_handling to open when any selected line belongs to a draft move | N-U12-051 |
| VDR-U12-C108 | FUNCTION MAPPING REQUIRED | account_payment/wizards/account_payment_register.py:76 | payment_token_id | FACT | account_payment installed | — | account_payment extends the wizard with payment_token_id (suitable tokens of the partner for the method's provider, not manual-capture) and passes it into the payment values | N-U12-052 |
| VDR-U12-C109 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:116 | access_account_payment_register | FACT | always | — | ACL for account.payment.register: read, write, create (no unlink) for account.group_account_invoice | N-U12-053 |
| VDR-U12-C110 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:1038 | write_off_amount_currency | INFERENCE | always | RT | A negative payment_difference with handling reconcile yields a write-off of opposite sign through the same code (lines 1036-1041); no explicit overpayment branch exists | N-U12-054 |
| VDR-U12-C111 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:27 | Only one payment will be created | FACT | always | — | group_payment help text: only one payment is created per partner (bank) instead of one per bill; the wizard is the single entry that creates, posts and reconciles the payment | N-U12-032 |
| VDR-U12-C112 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:136 | payment_difference_handling | FACT | always | — | payment_difference_handling choices are open (Keep open) and reconcile (Mark as fully paid); writeoff_label defaults to Write-Off | N-U12-055 |
| VDR-U12-C113 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:15 | debit_move_id = fields.Many2one | FACT | always | — | account.partial.reconcile: debit_move_id and credit_move_id (required, indexed), full_reconcile_id, exchange_move_id, draft_caba_move_vals (Json) | N-U12-056 |
| VDR-U12-C114 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:50 | Always positive amount | FACT | always | — | amount is always positive in company currency; debit_amount_currency / credit_amount_currency are always positive in the debit / credit line currency | N-U12-060 |
| VDR-U12-C115 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:75 | _check_required_computed_currencies | FACT | always | — | Constraint: both debit_currency_id and credit_currency_id must be set on a partial | N-U12-060 |
| VDR-U12-C116 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:93 | _compute_company_id | FACT | always | — | Partial company is the debit line company if the debit move is an invoice (incl. receipts), else the credit line company, so exchange/CABA entries are created on the invoice side | N-U12-056 |
| VDR-U12-C117 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:85 | _compute_max_date | FACT | always | — | max_date = max(debit line date, credit line date), used for aged reports | N-U12-056 |
| VDR-U12-C118 | FUNCTION MAPPING REQUIRED | account/models/account_full_reconcile.py:6 | account.full.reconcile | FACT | always | — | account.full.reconcile holds partial_reconcile_ids and reconciled_line_ids | N-U12-067 |
| VDR-U12-C119 | FUNCTION MAPPING REQUIRED | account/models/account_full_reconcile.py:28 | full_reconcile_id = source.full_id | FACT | always | — | account.full.reconcile.create stamps full_reconcile_id on lines and partials by SQL and then calls _update_matching_number | N-U12-067 |
| VDR-U12-C120 | FUNCTION MAPPING REQUIRED | account/models/account_full_reconcile.py:47 | def unlink | FACT | always | — | Unlinking a full reconcile recomputes matching numbers of its lines (False or P<n> for surviving partials) | N-U12-071 |
| VDR-U12-C121 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3142 | def reconcile | FACT | always | — | account.move.line.reconcile() is _reconcile_plan([self]) | N-U12-056 |
| VDR-U12-C122 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2720 | sorted_amls = amls.sorted | FACT | always | — | _optimize_reconciliation_plan sorts lines by (date_maturity or date, currency, amount_currency, balance), or only date/currency with context reduced_line_sorting, and splits into one node per currency when several currencies are present | N-U12-059 |
| VDR-U12-C123 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2651 | _check_amls_exigibility_for_reconciliation | FACT | always | — | Eligibility checks raise UserError for: already reconciled lines, cancelled parent entries, more than one account, more than one root company, account that is not reconcile-enabled and not asset_cash / liability_credit_card | N-U12-058 |
| VDR-U12-C124 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2669 | You can not reconcile cancelled entries | FACT | always | — | Cancelled entries cannot be reconciled | N-U12-058 |
| VDR-U12-C125 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2797 | def _reconcile_plan | FACT | always | — | _reconcile_plan runs _reconcile_plan_with_sync inside _check_balanced and _sync_dynamic_lines of the touched moves | N-U12-056 |
| VDR-U12-C126 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2783 | _reconcile_pre_hook | FACT | always | — | Pre-hook records invoices not yet paid/in_payment; post-hook calls _invoice_paid_hook on those that reached paid or in_payment (or in_payment -> paid) | N-U12-070 |
| VDR-U12-C127 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:135 | _invoice_paid_hook | FACT | sale installed | — | sale overrides _invoice_paid_hook to post Invoice <name> paid on the source sale orders | N-U12-070 |
| VDR-U12-C128 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:815 | _compute_amount_residual | FACT | always | — | amount_residual = round(balance - sum(debit partial amounts) + sum(credit partial amounts)) in company currency and the same in line currency; reconciled = both residuals zero; lines on non-reconcilable accounts (and not cash/credit card) get residual 0 and reconciled False | N-U12-061 |
| VDR-U12-C129 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2557 | debit_values_list = iter | FACT | always | — | _prepare_reconciliation_amls builds debit values (balance or amount_currency > 0) and credit values (< 0) and pairs them iteratively, advancing each side when its line is fully reconciled | N-U12-059 |
| VDR-U12-C130 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2174 | def get_odoo_rate | FACT | always | — | Rate for a counterpart in another currency: forced_rate_from_register_payment if given; if the opposite line is a payment or statement line its accounting rate; else invoice_date for invoices or the line date | N-U12-062 |
| VDR-U12-C131 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2284 | recon_currency = debit_currency | FACT | always | — | Reconciliation currency is the debit line foreign currency if available on both lines, else the credit line foreign currency, else company currency | N-U12-062 |
| VDR-U12-C132 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2315 | exchange_line_mode | FACT | always | — | exchange_line_mode (company-currency matching of lines with same foreign currency when one has no foreign amount) suppresses rates so the exchange difference only reduces the company-currency amount | N-U12-062 |
| VDR-U12-C133 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2344 | if recon_currency == company_currency | FACT | always | — | In company-currency matching the partial amount is the smaller recon amount; foreign amounts = rounded(rate x amount) capped by remaining foreign residual | N-U12-060 |
| VDR-U12-C134 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2395 | Prevent exchange differences | FACT | always | RT | In foreign-currency matching, if both sides' company-currency amounts fall within the rounding range of each other the partial amount is the smaller remaining residual, preventing needless exchange differences | N-U12-063 |
| VDR-U12-C135 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2442 | no_exchange_difference | FACT | always | RT | Exchange difference values are computed unless context no_exchange_difference or no_exchange_difference_no_recursive is set; they apply to fully matched lines (and to partially matched lines to keep rate consistency) | N-U12-064 |
| VDR-U12-C136 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2510 | exchange_values']['to_post'] | FACT | always | — | exchange_values to_post is true only when both matched lines belong to posted moves | N-U12-065 |
| VDR-U12-C137 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2994 | _get_exchange_account | FACT | always | — | Exchange account: company expense_currency_exchange_account_id when amount > 0, else income_currency_exchange_account_id | N-U12-064 |
| VDR-U12-C138 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2999 | _prepare_exchange_difference_move_vals | FACT | always | — | Exchange move values: entry in company.currency_exchange_journal_id, always_tax_exigible True; per line a line on the original account (carrying the original full_reconcile_id and reconciled_lines_ids) and an opposite line on the gain/loss account | N-U12-064 |
| VDR-U12-C139 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3019 | accounting_exchange_date | FACT | always | — | Exchange entry date = max(journal accounting date for the exchange date, dates of the lines concerned) | N-U12-065 |
| VDR-U12-C140 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3107 | Exchange Gain or Loss Journal | FACT | always | — | _create_exchange_difference_moves raises UserError if the exchange journal, the loss account or the gain account of the company is not configured | N-U12-066 |
| VDR-U12-C141 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3128 | no_exchange_difference=True | FACT | always | — | Exchange entries are created with context no_exchange_difference and posted (soft False) when their to_post flag is set | N-U12-065 |
| VDR-U12-C142 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2889 | partial.exchange_move_id = exchange_move | FACT | always | — | After creation each exchange move is attached to the first partial whose debit or credit line is among the move's reconciled_lines_ids (partial.exchange_move_id) | N-U12-064 |
| VDR-U12-C143 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1468 | _inverse_reconciled_lines_ids | FACT | always | — | Setting reconciled_lines_ids reconciles each line with those lines via _reconcile_plan; used to reconcile exchange entry lines with the original lines | N-U12-064 |
| VDR-U12-C144 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2931 | is_fully_reconciled = all | FACT | always | — | A group of lines (all lines matched by number with the plan) is fully reconciled when each line is reconciled or, for lines with partials, has zero residual in company currency (multi-currency) or line currency | N-U12-067 |
| VDR-U12-C145 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2966 | self.env['account.full.reconcile'].create | FACT | always | — | Full reconcile records are created in batch for the fully reconciled groups, linking all partials and lines | N-U12-067 |
| VDR-U12-C146 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:228 | UPDATE account_move_line l | FACT | always | — | _update_matching_number numbers connected graphs of partials by minimum partial id and sets matching_number = full_reconcile_id text if full else 'P' + number; lines no longer in a graph get False | N-U12-067 |
| VDR-U12-C147 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1594 | _constrains_matching_number | FACT | always | — | Constraint on matching_number format: digits, P+digits or I+text; I numbers cannot have partials; P requires partials and no full; digits require full and must equal the full reconcile id; partials require a number | N-U12-068 |
| VDR-U12-C148 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3157 | _reconcile_marked | FACT | always | — | _reconcile_marked reconciles lines sharing an I-prefixed matching number once all their moves are posted, enabling reconcile on the account if needed, with no exchange difference and no cash basis | N-U12-068 |
| VDR-U12-C149 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2894 | is_cash_basis_needed | FACT | company has cash-basis taxes | — | Cash-basis entries are created from the plan partials when any company has tax_exigibility and the account is receivable/payable, unless context move_reverse_cancel or no_cash_basis (hand-off to tax unit) | N-U12-069 |
| VDR-U12-C150 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:274 | tax_cash_basis_journal_id | FACT | cash-basis entries needed | — | _collect_tax_cash_basis_values raises UserError when the company has no tax cash basis journal | N-U12-069 |
| VDR-U12-C151 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:680 | both_move_posted | FACT | cash-basis entries needed | — | Cash-basis entries are created and posted when both reconciled moves are posted, otherwise created in draft (draft_caba_move_vals tracks their origin) | N-U12-069 |
| VDR-U12-C152 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:157 | def create | FACT | always | — | Partial create: payments without outstanding account in state in_process whose amount is covered become paid; matching numbers are updated | N-U12-056 |
| VDR-U12-C153 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:169 | not payment.outstanding_account_id | FACT | Community | CONTRA | Partial create/unlink only flip payments that have no outstanding account (to_check_payments filter); Community create() always assigns an outstanding account, so for ordinary payments this branch does nothing; CONTRA prior source-map candidate section 2.3 which presents in_process<->paid flips on partial create/unlink as general behaviour | N-U12-056 |
| VDR-U12-C154 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:105 | def unlink | FACT | always | — | Partial unlink: gathers CABA entries (by tax_cash_basis_rec_id) and exchange entries, unlinks the full reconcile, reverses non-draft entries with cancel=True and deletes drafts, updates matching numbers, resets affected payments to in_process | N-U12-071 |
| VDR-U12-C155 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:142 | _get_violated_lock_dates | FACT | always | — | Reversal date of CABA/exchange entries keeps the origin date, or the day after the last violated lock date (hand-off to the lock-date unit) | N-U12-077 |
| VDR-U12-C156 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3146 | def remove_move_reconcile | FACT | always | — | remove_move_reconcile unlinks matched_debit_ids and matched_credit_ids of the lines | N-U12-071 |
| VDR-U12-C157 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3150 | action_unreconcile_match_entries | FACT | always | — | action_unreconcile_match_entries removes all matches of all lines of the matching groups of the active journal items | N-U12-074 |
| VDR-U12-C158 | FUNCTION MAPPING REQUIRED | account/wizard/account_unreconcile_view.xml:5 | action_account_unreconcile | FACT | always | — | Server action Unreconcile on account.move.line restricted to account.group_account_user | N-U12-074 |
| VDR-U12-C159 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1860 | Break the reconciliation | FACT | always | — | Writing account_id, date, balance, amount_currency or currency_id on a line with a matching number unreconciles it, except an account change on all lines of the reconciliation together | N-U12-072 |
| VDR-U12-C160 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1879 | st_lines_to_unreconcile | FACT | always | — | For lines whose statement line move passes fiscal and tax lock checks, the statement line is also returned to unreconciled state (action_undo_reconciliation); lock failures drop it from the set | N-U12-072 |
| VDR-U12-C161 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1854 | _check_fiscal_lock_dates | FACT | always | — | Write on posted lines changing protected fiscal fields calls the fiscal lock check; unlink and tax-field writes call tax lock checks (owned by U11, noted only) | N-U12-077 |
| VDR-U12-C162 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1995 | self.remove_move_reconcile() | FACT | always | — | account.move.line.unlink removes reconciles first | N-U12-073 |
| VDR-U12-C163 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4083 | self.line_ids.remove_move_reconcile() | FACT | always | — | account.move.unlink removes reconciles of its lines before deleting them | N-U12-073 |
| VDR-U12-C164 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6275 | self._check_draftable() | INFERENCE | always | RT | button_draft performs _check_draftable (exchange, cash-basis and hashed entries refused) and sets state draft without calling remove_move_reconcile; effect on matches needs runtime confirmation | N-U12-080 |
| VDR-U12-C165 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1545 | def _check_reconciliation | INFERENCE | always | CONTRA | _check_reconciliation (UserError on modifying a reconciled posted line) has no caller anywhere in odoo/addons (py, xml, js grep); CONTRA prior source-map candidate section 2.4 which states that a posted-line change is refused if matched via this helper, whereas write() unreconciles instead | N-U12-079 |
| VDR-U12-C166 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1497 | _check_off_balance | FACT | always | — | Constraint: lines on off-balance accounts cannot be reconciled (and cannot mix with other account types or carry taxes) | N-U12-078 |
| VDR-U12-C167 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6239 | js_assign_outstanding_line | FACT | always | — | js_assign_outstanding_line reconciles the chosen outstanding line together with the unreconciled invoice lines of the same account | N-U12-075 |
| VDR-U12-C168 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6250 | js_remove_outstanding_partial | FACT | always | — | js_remove_outstanding_partial unlinks the given partial reconcile | N-U12-075 |
| VDR-U12-C169 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1485 | ('reconciled', '=', False) | FACT | always | — | Outstanding credits/debits widget searches posted, unreconciled lines of the invoice's receivable/payable accounts for the commercial partner with the opposite sign and a non-zero residual; only for draft/posted invoices in payment_state not_paid or partial | N-U12-075 |
| VDR-U12-C170 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2854 | no_exchange_difference=self.env.context | FACT | always | — | Reconcile propagates no_exchange_difference and no_exchange_difference_no_recursive from the context into plan preparation | N-U12-076 |
| VDR-U12-C171 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:98 | access_account_partial_reconcile_group_invoice | FACT | always | — | ACL: account.partial.reconcile full CRUD for Invoicing and full-accounting groups, read for readonly group; account.full.reconcile same pattern | N-U12-083 |
| VDR-U12-C172 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:504 | _get_default_amls_matching_domain | INFERENCE | always | RT | _get_default_amls_matching_domain is defined on the statement line model; grep over odoo/addons shows no caller, so its consumer (a bank reconciliation UI) is outside the studied Community code | N-U12-082 |
| VDR-U12-C173 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:816 | residual amount of a move line | FACT | always | — | _compute_amount_residual docstring: residual is 0 for fully reconciled lines or non-reconcilable accounts, the original amount for unreconciled lines and in between for partially reconciled lines, in company and line currency | N-U12-057 |
| VDR-U12-C174 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2395 | exchange differences if amounts are close | UNKNOWN | multi-currency | RT | Resulting residuals of foreign-currency matching with tiny differences cannot be asserted without execution | N-U12-081 |
| VDR-U12-C175 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:51 | ('in_payment', 'In Payment') | FACT | always | — | PAYMENT_STATE_SELECTION: not_paid, in_payment, paid, partial, reversed, blocked, invoicing_legacy | N-U12-084 |
| VDR-U12-C176 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:606 | payment_state = fields.Selection | FACT | always | — | payment_state: stored, computed (_compute_payment_state), readonly, copy=False, tracking=True | N-U12-097 |
| VDR-U12-C177 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1329 | _compute_status_in_payment | FACT | always | — | status_in_payment (display/search helper) mirrors payment_state for posted (partial, in_payment, paid, reversed, blocked) and draft (partial, in_payment, paid, blocked) moves, else state; sent when is_move_sent | N-U12-084 |
| VDR-U12-C178 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1233 | reconciled_payment_ids.state | FACT | always | — | _compute_payment_state depends on amount_residual, move_type, state, company_id and reconciled_payment_ids.state; _compute_amount additionally depends on counterpart payments is_matched and counterpart residuals | N-U12-091 |
| VDR-U12-C179 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1166 | origin_payment_id.is_matched | FACT | always | — | account.move._compute_amount depends on line_ids.matched_debit_ids/matched_credit_ids counterpart move origin_payment_id.is_matched, so a payment's matched flag change triggers the invoice amount/status chain | N-U12-091 |
| VDR-U12-C180 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1242 | groups = self.grouped | FACT | always | RT | Moves are grouped: legacy (invoicing_legacy kept), blocked (kept), invoices (qualifying), unpaid (set to not_paid) | N-U12-086 |
| VDR-U12-C181 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1235 | def _invoice_qualifies | FACT | always | — | A move qualifies if it is an invoice-type (incl. receipts) and either posted or draft with non-zero total | N-U12-086 |
| VDR-U12-C182 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1268 | all_payments_matched | FACT | always | — | SQL per partial collects counterpart move types, all_payments_matched (BOOL_AND of origin payment is_matched, TRUE when no payments), has_payment (counterpart is a payment) and has_st_line (counterpart has a statement line) | N-U12-088 |
| VDR-U12-C183 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1295 | currency.is_zero(invoice.amount_residual) | FACT | always | — | Residual zero with a payment or statement-line counterpart: paid when all payments are matched, else _get_invoice_in_payment_state(); residual zero with neither: paid unless reversed | N-U12-088 |
| VDR-U12-C184 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1307 | reverse_move_types | FACT | always | — | reversed when: vendor invoice/receipt settled only by in_refund (and entries); customer invoice/receipt settled only by out_refund (and entries); entry/credit-note moves settled only by entries | N-U12-087 |
| VDR-U12-C185 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1320 | matched_payment_ids.filtered | FACT | always | — | With non-zero residual: a posted invoice with a matched payment without move in state in_process (or without move in state paid after the partial check) takes _get_invoice_in_payment_state() | N-U12-090 |
| VDR-U12-C186 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1323 | new_pmt_state = 'partial' | FACT | always | — | Non-zero residual with any reconciliation values on receivable/payable lines gives partial; else not_paid | N-U12-086 |
| VDR-U12-C187 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7367 | _get_invoice_in_payment_state | FACT | Community (no override in odoo/addons) | — | _get_invoice_in_payment_state returns paid; docstring says the accounting app overrides it to enable in_payment; grep finds no other override in odoo/addons | N-U12-089 |
| VDR-U12-C188 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:255 | _valid_payment_states | FACT | Community | — | account.payment._valid_payment_states returns [in_process, paid] when the in-payment hook returns paid, else [in_process] | N-U12-089 |
| VDR-U12-C189 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:468 | payment.state == 'in_process' and (moves | FACT | always | RT | In _compute_state an in_process payment becomes paid when all reconciled invoices/bills have payment_state paid; payment state depends on reconciled_invoice_ids.payment_state while invoice payment_state depends on reconciled_payment_ids.state | N-U12-096 |
| VDR-U12-C190 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:965 | linked_invoices | FACT | always | — | Payment unlink adds payment_state of the reconciled invoices to compute after deletion | N-U12-091 |
| VDR-U12-C191 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2390 | _compute_reconciled_payment_ids | FACT | always | — | reconciled_payment_ids = payments found by SQL via partials on receivable/payable lines (filtered by read access) union matched_payment_ids | N-U12-095 |
| VDR-U12-C192 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:214 | matched_payment_ids | FACT | always | — | matched_payment_ids many2many shares relation account_move__account_payment with account.payment.invoice_ids | N-U12-095 |
| VDR-U12-C193 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6398 | def action_toggle_block_payment | FACT | always | — | action_toggle_block_payment: blocked -> not_paid and recompute; otherwise refuses paid/in_payment (UserError You can't block a paid invoice) and sets blocked | N-U12-092 |
| VDR-U12-C194 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6107 | payment_state == 'blocked' | FACT | always | — | Registering payments is refused for blocked invoices (document and wizard level) | N-U12-092 |
| VDR-U12-C195 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1473 | move.payment_state not in ('not_paid', 'partial') | FACT | always | — | Outstanding credits/debits widget is computed only for draft/posted invoices whose payment_state is not_paid or partial | N-U12-092 |
| VDR-U12-C196 | FUNCTION MAPPING REQUIRED | account/models/account_journal_dashboard.py:349 | move.payment_state in ('not_paid', 'partial') | FACT | always | — | Journal dashboard sale/purchase figures count moves with payment_state not_paid or partial | N-U12-093 |
| VDR-U12-C197 | FUNCTION MAPPING REQUIRED | account/report/account_invoice_report.py:40 | payment_state = fields.Selection | FACT | always | — | account.invoice.report carries payment_state using PAYMENT_STATE_SELECTION | N-U12-093 |
| VDR-U12-C198 | FUNCTION MAPPING REQUIRED | account_payment/models/account_move.py:69 | self.payment_state in | FACT | account_payment installed | — | _has_to_be_paid requires posted out_invoice with open residual, payment_state in not_paid, in_payment, partial, no pending transaction and the portal-payment config parameter | N-U12-093 |
| VDR-U12-C199 | FUNCTION MAPPING REQUIRED | sale/models/crm_team.py:31 | move.payment_state IN | FACT | sale installed | — | sale.crm_team invoiced KPI query counts invoices with payment_state in_payment, paid or reversed | N-U12-093 |
| VDR-U12-C200 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7262 | 'payment_state' in init_values | FACT | always | — | _track_subtype returns the mt_invoice_paid subtype when payment_state changes to paid | N-U12-094 |
| VDR-U12-C201 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:790 | _payment_idx | FACT | always | — | Index on (journal_id, state, payment_state, move_type, date) supports status filters | N-U12-093 |
| VDR-U12-C202 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:477 | move.payment_state == 'not_paid' | FACT | hr_expense installed (supporting module) | — | hr_expense derives the expense state from the move: posted when payment_state not_paid, paid (via _get_invoice_in_payment_state) when in_payment or partial with zero residual | N-U12-085 |
| VDR-U12-C203 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1884 | invoice.payment_state in ('not_paid', 'partial') | FACT | always | — | show_discount_details / show_payment_term_details are true only for invoice-type moves still not_paid or partial (payment-term and discount information on the document) | N-U12-085 |
| VDR-U12-C204 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1244 | 'blocked' if move.payment_state == 'blocked' | UNKNOWN | always | RT | A blocked document keeps blocked regardless of later reconciliation; how credit notes applied afterwards are surfaced cannot be determined without execution | N-U12-098 |
| VDR-U12-C205 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:16 | name = fields.Char | FACT | always | — | account.bank.statement fields: name (computed, editable), reference (external), date (computed), first_line_index, balance_start, balance_end, balance_end_real, company (related to journal), currency, journal (computed from lines), line_ids, is_complete, is_valid, problem_description, attachment_ids | N-U12-099 |
| VDR-U12-C206 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:10 | class AccountBankStatement | INFERENCE | always | — | The model defines no state selection and no validate/confirm/lock method (fields lines 16-109, only compute/search/default_get/create/write methods); statement 'validity' is computed, not a workflow | N-U12-102 |
| VDR-U12-C207 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:127 | _compute_first_line_index | FACT | always | — | first_line_index = internal_index of the earliest line with an index; statements are ordered by it | N-U12-104 |
| VDR-U12-C208 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:134 | _compute_date | FACT | always | — | statement date = date of the last posted line (by internal_index) | N-U12-104 |
| VDR-U12-C209 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:141 | _compute_balance_start | FACT | always | RT | balance_start = previous statement's balance_end_real (statement of the latest earlier posted line) minus lines in common, plus posted lines in between by internal_index | N-U12-103 |
| VDR-U12-C210 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:170 | _compute_balance_end | FACT | always | — | balance_end = balance_start + sum of posted line amounts | N-U12-103 |
| VDR-U12-C211 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:176 | _compute_balance_end_real | FACT | always | — | balance_end_real defaults to balance_end and is editable (readonly=False) | N-U12-103 |
| VDR-U12-C212 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:191 | _compute_is_complete | FACT | always | — | is_complete = has posted lines and balance_end equals balance_end_real in the statement currency | N-U12-102 |
| VDR-U12-C213 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:228 | _get_statement_validity | FACT | always | — | is_valid compares balance_start with the previous statement's (same journal, lower first_line_index) balance_end_real; no previous statement means valid | N-U12-102 |
| VDR-U12-C214 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:242 | _get_invalid_statement_ids | FACT | always | — | Bulk validity uses LAG(balance_end_real) per journal ordered by first_line_index; statements without lines or first in journal are considered valid | N-U12-102 |
| VDR-U12-C215 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:210 | _compute_problem_description | FACT | always | — | problem_description: invalid chain message, else running balance mismatch message | N-U12-102 |
| VDR-U12-C216 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:322 | contiguous | FACT | always | — | default_get for multi-edit raises UserError for lines of several journals and for non-contiguous selections (cancelled lines between are allowed and added) | N-U12-105 |
| VDR-U12-C217 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:293 | creating statements with split button | FACT | always | — | default_get supports split (lines of the current statement up to the split line), single line edit and multi edit contexts | N-U12-105 |
| VDR-U12-C218 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:186 | _compute_journal_id | FACT | always | — | statement journal is derived from its lines' journal; currency from journal else company | N-U12-099 |
| VDR-U12-C219 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement.py:340 | _check_attachments | FACT | always | — | Attachments set on statement create/write are re-linked to the statement record (res_model/res_id) | N-U12-099 |
| VDR-U12-C220 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:13 | _inherits = {'account.move': 'move_id'} | FACT | always | — | account.bank.statement.line _inherits account.move (move_id required, readonly, ondelete cascade, bypass_search_access) | N-U12-100 |
| VDR-U12-C221 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:367 | def create | FACT | always | — | create(): forces move_type entry, defaults amount 0, derives journal from statement, drops foreign currency equal to journal currency, creates liquidity+suspense lines when none given, and posts the move (action_post) | N-U12-106 |
| VDR-U12-C222 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:419 | No need for the user | FACT | always | — | Statement line moves are posted automatically at creation (comment: no need to manage Draft to Posted) | N-U12-106 |
| VDR-U12-C223 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:636 | counterpart_account_id | FACT | always | — | _prepare_move_line_default_vals uses the journal suspense account when no counterpart account is given and raises UserError if the journal has no suspense account | N-U12-107 |
| VDR-U12-C224 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:392 | Hack to force different account | FACT | always | — | create pops counterpart_account_id from vals to force another account than the suspense account | N-U12-107 |
| VDR-U12-C225 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:321 | _check_amounts_currencies | FACT | always | — | Constraint: foreign currency must differ from the journal currency; amount_currency requires foreign currency and vice versa | N-U12-108 |
| VDR-U12-C226 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:259 | _compute_internal_index | FACT | always | — | internal_index = YYYYMMDD + (MAXINT - sequence, 10 digits) + id (10 digits); used for ordering and balance lookups | N-U12-104 |
| VDR-U12-C227 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:287 | _compute_is_reconciled | FACT | always | — | is_reconciled: no id -> False; suspense lines present -> residual is zero; no suspense lines -> True; amount_residual = -amount (or -amount_currency) while the move is not checked, else the suspense residual | N-U12-109 |
| VDR-U12-C228 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:686 | _seek_for_lines | FACT | always | — | Statement move lines split into liquidity (journal default account, or any asset_cash/credit-card line if none), suspense (journal suspense account) and other lines | N-U12-110 |
| VDR-U12-C229 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:731 | len(liquidity_lines) != 1 | FACT | always | — | _synchronize_from_moves raises UserError unless the entry has exactly one liquidity line and at most one suspense line; payment_ref, partner and amount are copied from the liquidity line | N-U12-110 |
| VDR-U12-C230 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:797 | def _synchronize_to_moves | FACT | always | — | Changes of payment_ref, amount, amount_currency, foreign_currency_id, currency_id or partner_id are rewritten into the liquidity and suspense lines (other lines removed) | N-U12-111 |
| VDR-U12-C231 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:432 | restrictive_audit_trail | FACT | always | — | unlink: lines of companies with restrictive_audit_trail have their move button_cancel'ed instead of deleted; others delete the move with force_delete | N-U12-112 |
| VDR-U12-C232 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:483 | _check_allow_unlink | FACT | always | — | ondelete guard: lines of a valid and complete statement cannot be deleted; the statement must be removed first | N-U12-112 |
| VDR-U12-C233 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:460 | def action_undo_reconciliation | FACT | always | — | action_undo_reconciliation raises ValidationError for checked reconciled lines when the user cannot review (always allowed in Community), removes matches, unlinks payment_ids, and rewrites the move lines to the default liquidity + suspense lines | N-U12-113 |
| VDR-U12-C234 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:55 | Auto-generated Payments | FACT | always | — | payment_ids holds payments generated during reconciliation of the statement line | N-U12-113 |
| VDR-U12-C235 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:492 | skip_create_bank_account_on_reconcile | FACT | always | — | _find_or_create_bank_account creates the partner bank account unless config parameter account.skip_create_bank_account_on_reconcile is true, then only searches | N-U12-114 |
| VDR-U12-C236 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:504 | _get_default_amls_matching_domain | FACT | always | — | Candidate domain: posted lines (plus partnered draft lines if allow_draft), non-section lines, company in the line company and its children, not reconciled, account reconcile-enabled in the root company, receivable/payable lines only when not already payment lines, excluding lines of this statement line | N-U12-115 |
| VDR-U12-C237 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:504 | _get_default_amls_matching_domain | INFERENCE | always | RT | No caller of _get_default_amls_matching_domain was found in odoo/addons; the matching UI that would use it is not in Community scope | N-U12-127 |
| VDR-U12-C238 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:178 | _compute_running_balance | FACT | always | — | running_balance = anchor statement balance_start plus posted line amounts in internal_index order; draft/cancelled lines keep the previous value | N-U12-116 |
| VDR-U12-C239 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:541 | _get_default_statement | FACT | always | — | Default statement for a new line is the latest statement on or before the date, only if it is not complete | N-U12-105 |
| VDR-U12-C240 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:581 | _prepare_counterpart_amounts_using_st_line_rate | FACT | always | — | Counterpart amounts are converted with the bank-provided rate between transaction currency, journal currency and company currency | N-U12-062 |
| VDR-U12-C241 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:133 | until the final reconciliation | FACT | always | — | Journal suspense_account_id help: bank statement transactions are posted on the suspense account until the final reconciliation finds the right account; domain asset_current; computed from the company suspense account | N-U12-101 |
| VDR-U12-C242 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:253 | bank_statements_source | FACT | always | — | Journal bank_statements_source selection (Bank Feeds) offers only 'undefined' in base via _get_bank_statements_available_sources | N-U12-117 |
| VDR-U12-C243 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:298 | _compute_has_invalid_statements | FACT | always | — | has_invalid_statements true when the journal has a statement that is not valid or not complete | N-U12-118 |
| VDR-U12-C244 | FUNCTION MAPPING REQUIRED | account/models/account_journal_dashboard.py:454 | Number to reconcile | FACT | always | — | Dashboard number_to_reconcile counts posted, checked statement-line moves with is_reconciled not true per bank/cash journal | N-U12-118 |
| VDR-U12-C245 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7014 | _is_user_able_to_review | FACT | Community (accounting app absent) | — | _is_user_able_to_review returns True ('If only account is installed, we don't check user access rights'); checked is computed true for posted entries of general journals or reviewable entries | N-U12-119 |
| VDR-U12-C246 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:110 | trigger = fields.Selection | FACT | always | — | account.reconcile.model.trigger: manual (default) or auto_reconcile, tracked, required | N-U12-120 |
| VDR-U12-C247 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:126 | match_journal_ids | FACT | always | — | Conditions: match_journal_ids (bank/cash/credit), match_amount lower/greater/between with min/max, match_label contains/not_contains/match_regex with parameter, match_partner_ids | N-U12-120 |
| VDR-U12-C248 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:25 | amount_type = fields.Selection | FACT | always | — | Model line amount types: fixed, percentage (of balance), percentage_st_line (of statement line), regex (from label); lines carry account, partner, label, taxes, analytic distribution | N-U12-120 |
| VDR-U12-C249 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:79 | _validate_amount | FACT | always | — | Constraint: fixed amount cannot be 0 (not a number), percentage amounts cannot be 0, regex amount_string must compile; model match_label_param regex must compile | N-U12-121 |
| VDR-U12-C250 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:153 | _check_match_label_param | FACT | always | — | Constraint on the model: match_regex label parameter must be a valid regular expression | N-U12-121 |
| VDR-U12-C251 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:162 | _compute_can_be_proposed | FACT | always | — | can_be_proposed (stored) = no mapped partner and (label, amount, partner conditions or auto_reconcile trigger) | N-U12-122 |
| VDR-U12-C252 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:167 | _compute_partner_mapping | FACT | always | — | mapped_partner_id set when match_label is used and the single line has a partner but no account | N-U12-122 |
| VDR-U12-C253 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:172 | action_set_manual | FACT | always | — | action_set_manual / action_set_auto_reconcile set trigger; action_reconcile_stat lists moves containing lines created by the model (reconcile_model_id) | N-U12-123 |
| VDR-U12-C254 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:193 | def copy_data | FACT | always | — | copy_data gives a unique name '<name> (copy)' | N-U12-123 |
| VDR-U12-C255 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:162 | reconcile_model_id | FACT | always | — | account.move.line.reconcile_model_id records the model that created a line | N-U12-123 |
| VDR-U12-C256 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1196 | _get_account_reconcile_model | FACT | always | — | Chart template seeds reconcile models internal_transfer_reco (100% percentage line) and bank_fees_reco (label contains Bank Fees); post-load sets their line accounts to the transfer account and bank-fees account | N-U12-124 |
| VDR-U12-C257 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:800 | Bank Fees | OBSERVATION | restored DB (company 1) | RT | DB: the seeded Bank Fees reconcile model line points to an expense account named Employees compensation, because _get_bank_fees_reco_account falls back to the first expense account when no account name contains Bank Fees; the Internal Transfers line points to the Liquidity Transfer (company transfer) account; mapping should be reviewed | N-U12-227 |
| VDR-U12-C258 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:110 | auto_reconcile | INFERENCE | always | RT | Grep of odoo/addons for auto_reconcile, trigger values and amount types finds no code outside the model definition, views and chart-template data that applies the models to statement lines; the engine is outside the studied Community code | N-U12-125 |
| VDR-U12-C259 | FUNCTION MAPPING REQUIRED | account/models/account_reconcile_model.py:111 | Validate the statement line automatically | UNKNOWN | always | RT | Help text says the automated trigger validates the statement line automatically; the implementing code is not in Community scope | N-U12-130 |
| VDR-U12-C260 | FUNCTION MAPPING REQUIRED | account_payment/models/account_bank_statement_line.py:9 | _get_partial_amounts | INFERENCE | account_payment installed | — | account_payment overrides _get_partial_amounts on the statement line to refuse partial matching of provider/ISO20022/SEPA payments; grep shows the base method is not defined anywhere in odoo/addons, so the override has no super and cannot run without an external module | N-U12-126 |
| VDR-U12-C261 | FUNCTION MAPPING REQUIRED | account/data/service_cron.xml:3 | ir_cron_auto_post_draft_entry | FACT | always | — | account/data/service_cron.xml defines two crons only: auto-post draft entries (daily) and send invoices automatically (daily); none concerns statements or reconcile models | N-U12-129 |
| VDR-U12-C262 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:32 | access_account_bank_statement, | FACT | always | — | ACL statement and statement line: Basic group full CRUD; Invoicing and readonly groups read only (rows 28-33) | N-U12-128 |
| VDR-U12-C263 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:91 | access_account_reconcile_model_readonly | FACT | always | — | ACL reconcile model and line: readonly read; Invoicing read+create; Basic full CRUD | N-U12-128 |
| VDR-U12-C264 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:194 | account_bank_statement_comp_rule | FACT | always | — | Record rule statement: company_id in company_ids or False | N-U12-128 |
| VDR-U12-C265 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:200 | account_bank_statement_line_comp_rule | FACT | always | — | Record rule statement line: company_id in company_ids | N-U12-128 |
| VDR-U12-C266 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:206 | account_reconcile_model_template_comp_rule | FACT | always | — | Record rule reconcile model and line: company_id parent_of company_ids | N-U12-128 |
| VDR-U12-C267 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:23 | name = fields.Char | FACT | always | — | account.payment.term fields: name, active, note, line_ids (copy=True), company_id (optional), sequence, display_on_invoice, example preview fields, discount_percentage (default 2.0), discount_days (default 10), early_pay_discount_computation, early_discount | N-U12-131 |
| VDR-U12-C268 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:25 | Description on the Invoice | FACT | always | — | Term carries note (Description on the Invoice, translatable) and display_on_invoice (Show installment dates, default True) so the term text and installments are presented to the partner on the document | N-U12-132 |
| VDR-U12-C269 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:17 | _default_line_ids | FACT | always | — | Default line: percent 100, nb_days 0 | N-U12-135 |
| VDR-U12-C270 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:157 | _check_lines | FACT | always | — | Constraint: percent lines sum to 100 (decimal precision Payment Terms); EPD only on single-line terms; EPD percentage > 0; EPD days > 0 | N-U12-140 |
| VDR-U12-C271 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:344 | _check_percent | FACT | always | — | Constraint: percent line value between 0 and 100 | N-U12-134 |
| VDR-U12-C272 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:330 | _check_valid_char_value | FACT | always | — | Constraint: days_next_month must be numeric between 0 and 31 | N-U12-134 |
| VDR-U12-C273 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:350 | _compute_days | FACT | always | — | New line nb_days defaults to previous line nb_days + 30; value_amount of a new percent line defaults to 100 minus the sum of other percent lines | N-U12-135 |
| VDR-U12-C274 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:294 | delay_type = fields.Selection | FACT | always | — | delay_type: days_after, days_after_end_of_month, days_after_end_of_next_month, days_end_of_month_on_the | N-U12-133 |
| VDR-U12-C275 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:310 | def _get_due_date | FACT | always | — | _get_due_date: end of month + nb_days; end of next month + nb_days; for the day-of-month variant due_date + nb_days then next month on day days_next_month (0 or less -> end of that month); default date + nb_days | N-U12-136 |
| VDR-U12-C276 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:171 | def _compute_terms | FACT | always | — | _compute_terms returns total, discount values and per-line date, company_amount, foreign_amount for a document date, currency, company, tax/untaxed amounts and sign | N-U12-137 |
| VDR-U12-C277 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:226 | always the balance | FACT | always | — | The last line takes the residual amount (company and foreign) regardless of type; non-last lines use rounded percent of total or fixed amount converted by the rate | N-U12-133 |
| VDR-U12-C278 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:242 | cash_rounding and not on_balance_line | FACT | always | — | With cash rounding each non-last installment is cash-rounded and the last absorbs the remainder | N-U12-138 |
| VDR-U12-C279 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:201 | only available on single line | FACT | always | — | Discount amounts: excluded or mixed -> total - untaxed * pct; included -> total * (1 - pct); optional cash rounding of the discounted amount | N-U12-141 |
| VDR-U12-C280 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:195 | discount_date | FACT | always | — | discount_date = date_ref + discount_days when early_discount, else False | N-U12-140 |
| VDR-U12-C281 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:82 | _compute_discount_computation | FACT | always | — | early_pay_discount_computation default by company country: BE mixed, NL excluded, otherwise included (stored, editable) | N-U12-141 |
| VDR-U12-C282 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:61 | _get_amount_due_after_discount | FACT | always | — | _get_amount_due_after_discount reduces total by pct of total (included) or pct of tax-excluded part (excluded/mixed) and applies the move's cash rounding when called from a move | N-U12-141 |
| VDR-U12-C283 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:259 | _unlink_except_referenced_terms | FACT | always | — | ondelete guard: a term referenced by any account.move cannot be deleted (UserError, suggests archiving) | N-U12-149 |
| VDR-U12-C284 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:275 | def copy_data | FACT | always | — | copy_data appends (copy) to the name | N-U12-151 |
| VDR-U12-C285 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:98 | _compute_example_preview | FACT | always | — | example_preview computes installments and an EPD text for an example amount and date without storing | N-U12-151 |
| VDR-U12-C286 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:15 | check_company_domain_parent_of | FACT | always | — | Payment term _check_company_domain is parent-of based; company_id is optional | N-U12-150 |
| VDR-U12-C287 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:224 | account_payment_term_comp_rule | FACT | always | — | Record rule: company_id False or parent_of company_ids | N-U12-150 |
| VDR-U12-C288 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:104 | access_account_payment_term_partner_manager | FACT | always | — | ACL: payment term and line readable by internal users, term readable by portal, full CRUD for account.group_account_manager | N-U12-150 |
| VDR-U12-C289 | FUNCTION MAPPING REQUIRED | account/models/partner.py:559 | property_payment_term_id | FACT | always | — | Partner company-dependent properties property_payment_term_id (customer) and property_supplier_payment_term_id (vendor) | N-U12-139 |
| VDR-U12-C290 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1081 | _compute_invoice_payment_term_id | FACT | always | — | invoice_payment_term_id defaults from partner customer term (sales), vendor term (purchases), else False | N-U12-139 |
| VDR-U12-C291 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1389 | def _compute_needed_terms | FACT | always | — | needed_terms built for invoice-type moves with invoice lines: with a term, _compute_terms is called with tax/untaxed amounts (from base-line computation when the record is draft/new, stored totals otherwise) and merged by key (date_maturity, discount_date); without a term a single entry with invoice_date_due and the total | N-U12-137 |
| VDR-U12-C292 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1092 | _compute_invoice_date_due | FACT | always | — | invoice_date_due = max maturity of needed_terms, else existing due date, else today | N-U12-137 |
| VDR-U12-C293 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3740 | line_type='payment_term' | FACT | always | — | Dynamic line synchronisation order: payment_term (10), unbalanced (20), rounding (30), discount (40), taxes (50), non-deductible (60), epd (70), invoice (80) | N-U12-137 |
| VDR-U12-C294 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:444 | discount_date = fields.Date | FACT | always | — | Payment-term journal items store discount_date, discount_amount_currency and discount_balance; payment_date = discount date while today is not after it, else date_maturity | N-U12-146 |
| VDR-U12-C295 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1273 | _compute_payment_date | FACT | always | — | payment_date = discount_date if set and today <= discount_date else date_maturity | N-U12-146 |
| VDR-U12-C296 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3031 | _is_eligible_for_early_payment_discount | FACT | always | — | Eligible if currency equals the move currency, move type in (out_invoice, out_receipt, in_invoice, in_receipt), term has early_discount, reference date not after the first term line discount_date (or no reference/invoice date) and the term lines have no matches | N-U12-143 |
| VDR-U12-C297 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3356 | Early payment discount | FACT | always | — | _get_installments_data marks an eligible line as early_payment_discount and exposes discounted residual amounts | N-U12-143 |
| VDR-U12-C298 | FUNCTION MAPPING REQUIRED | account/wizard/account_payment_register.py:819 | _compute_early_payment_discount_mode | FACT | always | — | Wizard early_payment_discount_mode is true when epd_applied and the amount equals the by-default amount or the full amount; (the write-off section is hidden and difference handling set to reconcile by the dependent computes at lines 861-872) | N-U12-144 |
| VDR-U12-C299 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5068 | _get_invoice_counterpart_amls_for_early_payment_discount_per_payment_term_line | FACT | always | — | Builds discount counterpart values per payment term line in three groups (term_lines, tax_lines, base_lines); returns empty groups when the term has no discount percentage | N-U12-144 |
| VDR-U12-C300 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5131 | cash_discount_account | FACT | always | — | Discount lines use company account_journal_early_pay_discount_loss_account_id for inbound (customer) documents and ..._gain_account_id for outbound (vendor) documents | N-U12-144 |
| VDR-U12-C301 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5096 | tax_lines_needed | FACT | always | — | Tax adjustment lines are needed only when early_pay_discount_computation is included and the invoice lines have taxes | N-U12-144 |
| VDR-U12-C302 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5122 | t.amount_type != 'fixed' | FACT | always | — | Discount tax recomputation filters out fixed-amount taxes on the base lines; epd_needed dispatch also excludes taxes that cannot be discounted | N-U12-142 |
| VDR-U12-C303 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5231 | biggest_base_line | FACT | always | RT | Rounding differences of the discount base lines are added to the base line with the largest amount currency | N-U12-144 |
| VDR-U12-C304 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5283 | exchange_diff_sign | FACT | always | — | Residual open balance after discount lines becomes an exchange line on the company expense (positive) or income (negative) currency exchange account named Early Payment Discount (Exchange Difference) | N-U12-144 |
| VDR-U12-C305 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1077 | _compute_epd_needed | FACT | always | RT | In mixed mode, invoice product lines with taxes get epd and counterpart lines at invoicing (percentage of tax-excluded amounts grouped by account, analytic and taxes), distributed smoothly per line | N-U12-154 |
| VDR-U12-C306 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1062 | _compute_epd_key | FACT | always | — | epd lines are keyed only when the term has early_discount and computation mixed | N-U12-155 |
| VDR-U12-C307 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1801 | epd_amls | FACT | always | — | Tax computation base lines include existing epd lines (stored moves) or epd base lines derived from product lines (new moves), so mixed mode reduces the tax base at invoicing | N-U12-155 |
| VDR-U12-C308 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4506 | early_pay_discount_computation == 'mixed' | FACT | always | — | Quick-edit total back-computation adjusts untaxed price by (1 - discount) * tax rate in mixed mode when a single percent tax is used | N-U12-155 |
| VDR-U12-C309 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6647 | elif epd_installment | FACT | always | — | _get_invoice_next_payment_values returns installment_state epd with discounted amount, discount date and a message of days left or paid today | N-U12-145 |
| VDR-U12-C310 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1886 | show_discount_details | FACT | always | — | show_discount_details/show_payment_term_details only for invoice-type moves in payment_state not_paid or partial; details show when more than one installment or EPD | N-U12-147 |
| VDR-U12-C311 | FUNCTION MAPPING REQUIRED | account_payment/models/payment_transaction.py:171 | installment_state'] == 'epd' | FACT | account_payment installed | — | Transaction _create_payment adds EPD write-off lines when the invoice installment_state is epd and the transaction amount equals the discounted amount_due | N-U12-148 |
| VDR-U12-C312 | FUNCTION MAPPING REQUIRED | account_payment/models/account_move.py:155 | installment_state == 'epd' | FACT | account_payment installed | — | Default payment link values for an EPD invoice use next_amount_to_pay as maximum and add discount date info | N-U12-145 |
| VDR-U12-C313 | FUNCTION MAPPING REQUIRED | account/models/company.py:123 | account_journal_early_pay_discount_gain_account_id | FACT | always | — | Company fields account_journal_early_pay_discount_gain_account_id and ..._loss_account_id (Cash Discount Write-Off Gain / Loss) | N-U12-144 |
| VDR-U12-C314 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:860 | account_journal_early_pay_discount_loss_account_id | FACT | chart template | — | Chart template data creates default accounts Cash Discount Loss (999998, expense) and Cash Discount Gain (999997, other income) for these company fields | N-U12-144 |
| VDR-U12-C315 | FUNCTION MAPPING REQUIRED | account/models/company.py:124 | account_journal_early_pay_discount_loss_account_id | OBSERVATION | restored DB (company 1) | RT | DB: the company early-discount loss account is a Sales Discounts account of type income and the gain account is a Purchase Discounts account of type other income; the template accounts 999998 and 999997 do not exist in this DB (local chart mapping); semantic fit to be reviewed | N-U12-144 |
| VDR-U12-C316 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:11 | class AccountPaymentTerm | INFERENCE | always | — | account.payment.term and account.payment.term.line define no state field or workflow method | N-U12-153 |
| VDR-U12-C317 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5180 | percentage_paid | UNKNOWN | foreign currency or several taxes | RT | Distribution of tax and base discount lines scaled by percentage_paid with several taxes or currencies cannot be asserted without execution | N-U12-152 |
| VDR-U12-C318 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment_method.py:13 | check_printing | FACT | account_check_printing installed | — | Method information: check_printing mode multi, type bank only; data record account_payment_method_check name Checks, code check_printing, outbound | N-U12-158 |
| VDR-U12-C319 | FUNCTION MAPPING REQUIRED | account_check_printing/data/account_check_printing_data.xml:5 | account_payment_method_check | FACT | account_check_printing installed | — | Payment method record Checks / check_printing / outbound is created (noupdate) | N-U12-158 |
| VDR-U12-C320 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_journal.py:13 | _default_outbound_payment_methods | FACT | account_check_printing installed | — | Journals add the check method to default outbound methods when _is_payment_method_available('check_printing') | N-U12-158 |
| VDR-U12-C321 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_journal.py:19 | check_manual_sequencing | FACT | always | — | Journal fields: check_manual_sequencing (default False, 'Manual Numbering': pre-printed checks not numbered), check_sequence_id (readonly), check_next_number, bank_check_printing_layout (layouts excluding disabled) | N-U12-161 |
| VDR-U12-C322 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_journal.py:57 | _inverse_check_next_number | FACT | always | — | check_next_number must be digits, not lower than the sequence's number_next_actual, not above 2147483647; setting it updates sequence number_next_actual and padding | N-U12-161 |
| VDR-U12-C323 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_journal.py:85 | _create_check_sequence | FACT | always | — | Journal creation creates an ir.sequence named '<journal>: Check Number Sequence' implementation no_gap, padding 5, increment 1, company of the journal | N-U12-159 |
| VDR-U12-C324 | FUNCTION MAPPING REQUIRED | account_check_printing/__init__.py:7 | create_check_sequence_on_bank_journals | FACT | at installation | — | post_init_hook creates check sequences on all existing bank journals | N-U12-159 |
| VDR-U12-C325 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_journal.py:98 | num_checks_to_print | FACT | always | — | Journal dashboard counts payments with method check_printing, state in_process and is_sent False (num_checks_to_print); action_checks_to_print opens them with outbound defaults | N-U12-170 |
| VDR-U12-C326 | FUNCTION MAPPING REQUIRED | account_check_printing/models/res_company.py:11 | account_check_printing_layout | FACT | always | — | Company settings: account_check_printing_layout (selection with only disabled in base, default disabled), date label (default True), multi-stub (default False), margins top/left/right default 0.25 | N-U12-168 |
| VDR-U12-C327 | FUNCTION MAPPING REQUIRED | account_check_printing/models/res_company.py:9 | needs to be overridden with `selection_add` | FACT | always | — | Comment: modules adding layouts must extend the selection with selection_add and use the report action xmlid as key | N-U12-169 |
| VDR-U12-C328 | FUNCTION MAPPING REQUIRED | account_check_printing/models/res_config_settings.py:10 | account_check_printing_layout | FACT | always | — | res.config.settings exposes the company layout, date label, multi-stub and margins (related, editable) | N-U12-168 |
| VDR-U12-C329 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:15 | check_amount_in_words | FACT | always | — | account.payment adds check_amount_in_words (stored compute from currency.amount_to_text), check_number (stored compute with inverse, copy=False), show_check_number, check_manual_sequencing (related) and check_layout_available | N-U12-156 |
| VDR-U12-C330 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:48 | _constrains_check_number | FACT | always | — | Constraint: check_number must be decimal digits | N-U12-162 |
| VDR-U12-C331 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:64 | _constrains_check_number_unique | FACT | always | — | Constraint: same check number (compared as BIGINT) cannot exist twice in one journal among payments whose moves are posted | N-U12-162 |
| VDR-U12-C332 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:107 | _compute_check_number | FACT | always | — | check_number is proposed (next sequence char) for journals with manual sequencing and method check_printing, else False | N-U12-161 |
| VDR-U12-C333 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:115 | _inverse_check_number | FACT | always | — | Writing a check number sets the journal check sequence padding to the number's length | N-U12-161 |
| VDR-U12-C334 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:131 | _get_trigger_fields_to_synchronize | FACT | always | — | check_number is added to the fields that trigger payment-to-entry synchronisation | N-U12-167 |
| VDR-U12-C335 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:134 | _get_aml_default_display_name_list | FACT | always | — | With a check number the journal item label is 'Checks - <number>' plus ': memo' when present | N-U12-167 |
| VDR-U12-C336 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:155 | def action_post | FACT | always | — | action_post assigns check_number = journal.check_sequence_id.next_by_id() for check-method payments on manually sequenced journals, then calls super | N-U12-161 |
| VDR-U12-C337 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:162 | def print_checks | FACT | always | — | print_checks keeps payments with method check_printing and not is_sent (else UserError), requires one journal for all (else UserError); on journals without manual sequencing it opens the numbering wizard with the next number = max existing + 1 (same width); otherwise confirms drafts and calls do_print_checks | N-U12-163 |
| VDR-U12-C338 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:181 | ORDER BY payment.check_number::BIGINT DESC | FACT | always | — | Suggested next check number query: highest check_number of the journal's payments (any state) cast to BIGINT, plus one | N-U12-172 |
| VDR-U12-C339 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:205 | def action_void_check | FACT | always | — | action_void_check = action_draft() then action_cancel() | N-U12-165 |
| VDR-U12-C340 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:209 | def do_print_checks | FACT | always | — | do_print_checks uses journal bank_check_printing_layout or company layout; disabled/missing raises RedirectWarning to settings; then writes is_sent and returns the report action | N-U12-164 |
| VDR-U12-C341 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:228 | _check_build_page_info | FACT | always | RT | Page data: check number, date, partner, company, currency, state, amount (VOID on extra pages), amount in words, memo, stub_cropped flag and stub lines | N-U12-166 |
| VDR-U12-C342 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:256 | _check_make_stub_pages | FACT | always | — | Stub lists reconciled outbound invoices (bills/receipts and refunds grouped), cropped to INV_LINES_PER_STUB = 9 lines (8 plus ellipsis) unless multi-stub is enabled, then split in pages | N-U12-166 |
| VDR-U12-C343 | FUNCTION MAPPING REQUIRED | account_check_printing/wizard/print_prenumbered_checks.py:16 | _check_next_check_number | FACT | always | — | Wizard constraint: next check number digits only | N-U12-162 |
| VDR-U12-C344 | FUNCTION MAPPING REQUIRED | account_check_printing/wizard/print_prenumbered_checks.py:21 | def print_checks | FACT | always | — | Wizard posts draft payments, marks in-process unsent ones is_sent, assigns zero-padded consecutive numbers starting at the entered number, then do_print_checks with close_on_report_download | N-U12-160 |
| VDR-U12-C345 | FUNCTION MAPPING REQUIRED | account_check_printing/data/account_check_printing_data.xml:11 | action_account_print_checks | FACT | always | — | Server action Print Checks on account.payment (list/kanban) restricted to account.group_account_user | N-U12-171 |
| VDR-U12-C346 | FUNCTION MAPPING REQUIRED | account_check_printing/security/ir.model.access.csv:2 | access_print_prenumbered_checks | FACT | always | — | ACL print.prenumbered.checks: read, write, create (no unlink) for account.group_account_user | N-U12-171 |
| VDR-U12-C347 | FUNCTION MAPPING REQUIRED | account_check_printing/views/account_payment_views.xml:9 | print_checks | FACT | always | — | Payment form buttons: Print Check (method check, not sent, layout available), Unmark Sent (check and sent), Void Check (check, in_process and sent) | N-U12-165 |
| VDR-U12-C348 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:33 | check_layout_available | FACT | always | — | check_layout_available is true only if the company layout selection has more than one value (a country layout exists) | N-U12-169 |
| VDR-U12-C349 | FUNCTION MAPPING REQUIRED | account_check_printing/views/account_journal_views.xml:30 | check_printing | FACT | always | — | Journal form shows check numbering and layout settings only for bank journals that have the check method selected | N-U12-168 |
| VDR-U12-C350 | FUNCTION MAPPING REQUIRED | account_check_printing/models/res_company.py:11 | account_check_printing_layout | INFERENCE | installed modules | RT | Grep over odoo/addons for account_check_printing_layout finds only account_check_printing files (no selection_add by another module), and the DB shows no other check-printing module installed; check rendering therefore cannot be traced | N-U12-173 |
| VDR-U12-C351 | FUNCTION MAPPING REQUIRED | account_check_printing/models/account_payment.py:99 | _compute_check_amount_in_words | FACT | always | — | check_amount_in_words = currency.amount_to_text(amount), recomputed with amount, method line and currency; filled to 200 chars with asterisks by _check_fill_line when printed | N-U12-157 |
| VDR-U12-C352 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/res_company.py:8 | account_interco_clearing_journal_id | FACT | account_payment_interco installed | — | res.company adds account_interco_clearing_journal_id (general journal), account_interco_payable_id (payable, reconcile) and account_interco_receivable_id (receivable, reconcile) | N-U12-179 |
| VDR-U12-C353 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/account_move.py:7 | _interco_filter_moves | FACT | account_payment_interco installed | — | Moves qualify when invoice, payment_state in not_paid, partial, in_payment, company has a clearing journal, a transaction payment exists in a different company, matching interco account pair exists (receivable for inbound, payable for outbound) and the payment is in_process or paid with its company having a clearing journal | N-U12-177 |
| VDR-U12-C354 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/account_move.py:30 | def _post | FACT | account_payment_interco installed | — | _post override: after super, for qualifying moves (sudo) runs _check_interco_clearing with payments of transactions in authorized/done | N-U12-176 |
| VDR-U12-C355 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/account_move.py:39 | _check_interco_clearing | FACT | account_payment_interco installed | RT | _check_interco_clearing builds clearing amounts from the payment counterpart lines (balance and amount_currency), labels by partner and invoice name | N-U12-178 |
| VDR-U12-C356 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/account_move.py:57 | payment_clearing | FACT | account_payment_interco installed | — | In the payment company a misc entry in its clearing journal debits/credits the counterpart account and the other interco account, is posted and its counterpart line is reconciled with the payment counterpart lines | N-U12-178 |
| VDR-U12-C357 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/account_move.py:99 | Interco Settlement | FACT | account_payment_interco installed | — | In the invoice company an entry 'Interco Settlement - <memos>' in its clearing journal moves the invoice receivable/payable balance against the company interco account, is posted and reconciled with the invoice term lines | N-U12-178 |
| VDR-U12-C358 | FUNCTION MAPPING REQUIRED | account_payment_interco/__manifest__.py:4 | Enable Intercompany payments | FACT | account_payment_interco installed | — | Module summary: enable inter-company payments to reconcile with their invoices on post; depends on account_payment | N-U12-174 |
| VDR-U12-C359 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/res_company.py:19 | Intercompany invoice payments will be cleared | FACT | account_payment_interco installed | — | Company help texts: the clearing journal is where inter-company payments are cleared; the payable account clears invoice payments and the receivable account clears credit note payments | N-U12-175 |
| VDR-U12-C360 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1180 | def _log_message_on_linked_documents | FACT | always | — | Transactions log state messages on linked records (invoices, payments) through _log_message_on_linked_documents, giving a document-side audit trail of payment attempts | N-U12-182 |
| VDR-U12-C361 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/account_move.py:33 | interco_moves := | FACT | always | — | Without configured clearing journal and accounts _interco_filter_moves returns nothing so no clearing entries are created | N-U12-179 |
| VDR-U12-C362 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/account_move.py:82 | (counterpart_lines + payment_clearing_line).reconcile() | UNKNOWN | multi-currency / partial payments | RT | Outcome for foreign-currency payments and partly paid invoices (clearing uses the invoice company balance only) cannot be asserted without execution; interco is not configured in the DB | N-U12-180 |
| VDR-U12-C363 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:24 | class PaymentTransaction | FACT | always | — | payment.transaction fields: provider, company (related, stored), method, token, reference (unique), provider_reference, amount, currency, state, state_message, last_state_change, operation, is_live, source/child transactions, is_post_processed, tokenize, landing_route, partner snapshot fields | N-U12-181 |
| VDR-U12-C364 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:67 | selection=[('draft', "Draft") | FACT | always | — | state selection draft, pending, authorized, done (Confirmed), cancel (Canceled), error; default draft, readonly, required, copy=False | N-U12-183 |
| VDR-U12-C365 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:135 | _reference_uniq | FACT | always | — | SQL constraint unique(reference) | N-U12-187 |
| VDR-U12-C366 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:370 | def _compute_reference | FACT | always | — | _compute_reference uses the (ASCII-normalised) prefix, else a prefix computed from documents, else a time-based prefix; adds -<n> suffix with the max existing sequence + 1 when the prefix exists | N-U12-187 |
| VDR-U12-C367 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:159 | _check_state_authorized_supported | FACT | always | — | Constraint: state authorized requires provider.support_manual_capture | N-U12-186 |
| VDR-U12-C368 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:171 | _check_token_is_active | FACT | always | — | Constraint: creating a transaction from an archived token is forbidden | N-U12-192 |
| VDR-U12-C369 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:188 | Duplicate partner values | FACT | always | — | create() copies partner name, language, first normalised email, address, zip, city, state, country, phone and sets is_live from provider state enabled | N-U12-188 |
| VDR-U12-C370 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:915 | def _set_pending | FACT | always | — | _set_pending allows draft; _set_authorized draft/pending; _set_done draft/pending/authorized/error; _set_canceled draft/pending/authorized; _set_error draft/pending/authorized (each plus provider extra_allowed_states) | N-U12-184 |
| VDR-U12-C371 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1002 | def _update_state | FACT | always | — | _update_state classifies transactions: allowed source state -> updated (state, state_message, last_state_change, is_post_processed False); already in target -> INFO log skip; other -> WARNING log refusal | N-U12-185 |
| VDR-U12-C372 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1060 | _update_source_transaction_state | FACT | always | — | When child transactions of the same operation in done/cancel sum to the source amount, the authorized source becomes cancel if all children are canceled, else done | N-U12-190 |
| VDR-U12-C373 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:699 | _create_child_transaction | FACT | always | — | Child transactions: refund -> reference prefix R-<ref>, negative amount, operation refund; partial capture/void -> prefix P-<ref>, same operation; linked by source_transaction_id | N-U12-190 |
| VDR-U12-C374 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:266 | def action_capture | FACT | always | — | action_capture opens the partial capture wizard if the provider supports partial capture, else captures authorized transactions in sudo after checking write rights on the recordset | N-U12-191 |
| VDR-U12-C375 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:301 | Only authorized transactions can be voided | FACT | always | — | action_void raises ValidationError unless all transactions are authorized; voids the amount not yet captured | N-U12-191 |
| VDR-U12-C376 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:322 | Only confirmed transactions can be refunded | FACT | always | — | action_refund raises ValidationError unless all transactions are done | N-U12-191 |
| VDR-U12-C377 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:687 | _ensure_provider_is_not_disabled | FACT | always | — | Capture, void, refund and token charge raise UserError when the provider state is disabled | N-U12-191 |
| VDR-U12-C378 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:561 | def _charge_with_token | FACT | always | — | _charge_with_token ensures provider enabled, logs the sent message and sends the provider request; a ValidationError from the provider sets the transaction to error with the message | N-U12-191 |
| VDR-U12-C379 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:738 | def _process | FACT | always | — | _process finds the transaction (self or by reference and provider code), validates the amount, stops if it became error, applies provider updates and tokenizes when tokenize is set and state is authorized or done | N-U12-189 |
| VDR-U12-C380 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:794 | def _validate_amount | FACT | always | — | Amount validation (skipped for validation operations or when the provider opts out): missing amount/currency -> error; amount compared to the transaction amount rounded DOWN to provider/currency precision (refunds negated); currency code must match; mismatch -> error | N-U12-189 |
| VDR-U12-C381 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:876 | def _tokenize | FACT | always | — | _tokenize creates a payment.token (provider, method, partner plus provider values), links it and clears tokenize | N-U12-189 |
| VDR-U12-C382 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1082 | def _cron_post_process | FACT | always | RT | Cron post-processing: transactions with is_post_processed False and last_state_change within 4 days; each processed and committed separately; OperationalError rolls back and retries later, other exceptions are logged and rolled back | N-U12-194 |
| VDR-U12-C383 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1112 | def _post_process | FACT | always | — | Base _post_process only sets is_post_processed True; modules override it | N-U12-194 |
| VDR-U12-C384 | FUNCTION MAPPING REQUIRED | payment/data/payment_cron.xml:4 | cron_post_process_payment_tx | FACT | always | — | Cron record 'Payment: Post-process transactions' runs model._cron_post_process() every 10 minutes as the root user, shipped inactive | N-U12-194 |
| VDR-U12-C385 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:396 | _toggle_post_processing_cron | FACT | always | — | _toggle_post_processing_cron activates the cron when any provider is not disabled and deactivates it otherwise; called on provider create/write of state and from the cron data file | N-U12-195 |
| VDR-U12-C386 | FUNCTION MAPPING REQUIRED | payment/controllers/post_processing.py:42 | def poll_status | FACT | always | RT | The /payment/status/poll route post-processes the monitored transaction if not yet post-processed; database errors roll back and ask the client to retry | N-U12-194 |
| VDR-U12-C387 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:41 | state = fields.Selection | FACT | always | — | payment.provider.state: disabled (default), enabled, test; company required; copy=False | N-U12-202 |
| VDR-U12-C388 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:348 | if 'state' in vals | FACT | always | — | Provider write: on state change away from disabled the linked tokens are archived; disabled -> unsupported payment methods deactivated; disabled->enabled/test -> default methods activated; cron toggled | N-U12-202 |
| VDR-U12-C389 | FUNCTION MAPPING REQUIRED | payment/models/payment_token.py:77 | Prevent unarchiving tokens | FACT | always | — | Token write: unarchiving refused when the method is inactive or the provider disabled; archiving runs handlers in sudo | N-U12-192 |
| VDR-U12-C390 | FUNCTION MAPPING REQUIRED | payment/models/payment_token.py:101 | _check_partner_is_never_public | FACT | always | — | Constraint: no token can be assigned to the public partner | N-U12-192 |
| VDR-U12-C391 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:332 | access to this payment token | FACT | always | — | _create_transaction for the token flow raises AccessError when the payer's commercial partner differs from the token owner's commercial partner | N-U12-193 |
| VDR-U12-C392 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:318 | Don't tokenize if the user tried | FACT | always | — | For redirect/direct flows tokenize is true only if the provider allows tokenization, the method supports it and it is required by the flow or requested by the user | N-U12-189 |
| VDR-U12-C393 | FUNCTION MAPPING REQUIRED | account_payment/models/payment_transaction.py:9 | payment_id = fields.Many2one | FACT | account_payment installed | — | account_payment adds payment_id and invoice_ids (relation account_invoice_transaction_rel) to payment.transaction | N-U12-181 |
| VDR-U12-C394 | FUNCTION MAPPING REQUIRED | account_payment/models/account_payment.py:11 | payment_transaction_id | FACT | account_payment installed | — | account.payment gains payment_transaction_id (readonly), payment_token_id, amount_available_for_refund, source_payment_id (related, stored), refunds_count | N-U12-197 |
| VDR-U12-C395 | FUNCTION MAPPING REQUIRED | account_payment/models/payment_transaction.py:98 | def _post_process | FACT | account_payment installed | — | For done transactions: draft invoices are posted, a payment is created unless validation / already linked / a child is done or canceled, a message with payment link is logged; for cancel transactions the payment is canceled | N-U12-196 |
| VDR-U12-C396 | FUNCTION MAPPING REQUIRED | account_payment/models/payment_transaction.py:133 | def _create_payment | FACT | account_payment installed | — | _create_payment builds the payment from the provider journal and inbound method line, abs(amount), direction by sign, commercial partner, token and transaction links, EPD write-off lines when installment_state is epd and the amount is the discounted amount, posts it and reconciles its destination-account lines with the invoices' lines | N-U12-197 |
| VDR-U12-C397 | FUNCTION MAPPING REQUIRED | account_payment/models/account_payment.py:124 | def action_post | FACT | account_payment installed | — | Payments with a token and no transaction create a transaction (offline), charge it, post-process it, then post if the transaction is done, and cancel the payment if the transaction is not done/pending/authorized | N-U12-198 |
| VDR-U12-C398 | FUNCTION MAPPING REQUIRED | account_payment/models/account_move.py:55 | _has_to_be_paid | FACT | account_payment installed | — | _has_to_be_paid requires parameter account_payment.enable_portal_payment, posted out_invoice not paid with open residual, and no pending/authorized transaction of non-custom providers | N-U12-199 |
| VDR-U12-C399 | FUNCTION MAPPING REQUIRED | account_payment/wizards/payment_refund_wizard.py:39 | _check_amount_to_refund_within_boundaries | FACT | account_payment installed | — | Refund wizard constraint: 0 < amount_to_refund <= amount_available_for_refund | N-U12-200 |
| VDR-U12-C400 | FUNCTION MAPPING REQUIRED | account_payment/models/account_payment.py:49 | _compute_amount_available_for_refund | FACT | account_payment installed | — | amount_available_for_refund = payment amount minus the abs sum of refund payments, only when the provider and method support refunds and the payment is not itself a refund | N-U12-200 |
| VDR-U12-C401 | FUNCTION MAPPING REQUIRED | account_payment/models/payment_provider.py:10 | journal_id = fields.Many2one | FACT | account_payment installed | — | payment.provider gains journal_id (bank journal where successful transactions are posted), computed from its method line or the first bank journal when enabled/test | N-U12-201 |
| VDR-U12-C402 | FUNCTION MAPPING REQUIRED | account_payment/models/payment_provider.py:23 | _ensure_payment_method_line | FACT | account_payment installed | — | _ensure_payment_method_line links or creates the account.payment.method.line for the provider on its journal (outstanding account from chart or company transfer account) | N-U12-201 |
| VDR-U12-C403 | FUNCTION MAPPING REQUIRED | account_payment/models/payment_provider.py:145 | cannot uninstall this module | FACT | account_payment installed | — | _remove_provider refuses uninstall when payments exist for the provider method and deletes the method otherwise | N-U12-201 |
| VDR-U12-C404 | FUNCTION MAPPING REQUIRED | account_payment/models/account_journal.py:17 | _unlink_except_linked_to_payment_provider | FACT | account_payment installed | — | A journal linked to a non-disabled provider cannot be deleted | N-U12-201 |
| VDR-U12-C405 | FUNCTION MAPPING REQUIRED | account_payment/models/account_payment_method_line.py:64 | _unlink_except_active_provider | FACT | account_payment installed | — | A payment method line linked to an enabled or test provider cannot be deleted | N-U12-201 |
| VDR-U12-C406 | FUNCTION MAPPING REQUIRED | payment/utils.py:15 | def generate_access_token | FACT | always | — | Access tokens are HMAC signatures (superuser env) over partner, amount, currency values and are verified with check_access_token | N-U12-207 |
| VDR-U12-C407 | FUNCTION MAPPING REQUIRED | account_payment/security/ir.model.access.csv:4 | payment_transaction_user | FACT | account_payment installed | — | ACL payment.transaction: account.group_account_invoice read, write, create (no unlink); system group full rights in payment module | N-U12-203 |
| VDR-U12-C408 | FUNCTION MAPPING REQUIRED | payment/security/ir.model.access.csv:13 | payment_transaction_system | FACT | always | — | ACL payment.transaction, payment.provider: base.group_system full; payment.method and payment.token readable by employees, portal and public, writable by system | N-U12-203 |
| VDR-U12-C409 | FUNCTION MAPPING REQUIRED | payment/security/ir.model.access.csv:11 | payment_token_employee | FACT | always | — | ACL payment.token: employees, portal and public read; system full | N-U12-203 |
| VDR-U12-C410 | FUNCTION MAPPING REQUIRED | payment/security/payment_security.xml:14 | transaction_company_rule | FACT | always | — | Record rule transactions: company_id in company_ids | N-U12-204 |
| VDR-U12-C411 | FUNCTION MAPPING REQUIRED | payment/security/payment_security.xml:6 | payment_provider_company_rule | FACT | always | — | Record rule providers: company_id parent_of company_ids | N-U12-204 |
| VDR-U12-C412 | FUNCTION MAPPING REQUIRED | payment/security/payment_security.xml:22 | payment_token_user_rule | FACT | always | — | Record rule tokens: users, portal and public see only tokens of their own partner; company rule parent_of; billing (invoicing) group sees all via account_payment rule | N-U12-204 |
| VDR-U12-C413 | FUNCTION MAPPING REQUIRED | account_payment/security/ir_rules.xml:6 | payment_token_billing_rule | FACT | account_payment installed | — | Rule 'Access every token' domain [(1,'=',1)] for account.group_account_invoice | N-U12-204 |
| VDR-U12-C414 | FUNCTION MAPPING REQUIRED | payment/controllers/post_processing.py:53 | if not monitored_tx.is_post_processed | INFERENCE | always | RT | Post-processing is triggered either by the status poll or by the cron (both guarded by is_post_processed); with neither running a done transaction is never post-processed | N-U12-205 |
| VDR-U12-C415 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:465 | _get_processing_values | UNKNOWN | provider modules | RT | Provider-specific hooks (_apply_updates, _extract_amount_data, _get_specific_rendering_values) are empty in the framework; behaviour belongs to provider modules not studied | N-U12-206 |
| VDR-U12-C416 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:50 | group_account_readonly | FACT | always | — | Groups: group_account_readonly (Show Accounting Features - Readonly), group_account_invoice (Invoicing), group_account_basic (Basic), group_account_user (Show Full Accounting Features), group_account_manager (Administrator), group_account_secured, group_validate_bank_account | N-U12-208 |
| VDR-U12-C417 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:63 | group_account_basic | FACT | always | — | Implications: basic implies invoice; user implies basic and readonly; manager implies invoice; invoice and readonly imply base.group_user | N-U12-210 |
| VDR-U12-C418 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:58 | Invoices, payments and basic invoice reporting | FACT | always | — | Group Invoicing comment: Invoices, payments and basic invoice reporting; Administrator: full access including configuration rights | N-U12-209 |
| VDR-U12-C419 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:109 | access_account_payment_method_line_readonly | FACT | always | — | ACL: payment method and method line readable by base.group_user; method line CRUD and method read/write/delete (no create) for account.group_account_invoice | N-U12-214 |
| VDR-U12-C420 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:114 | access_account_payment, | FACT | always | — | Invoicing group has full CRUD on account.payment; readonly group read only (rows 113-114) | N-U12-211 |
| VDR-U12-C421 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:98 | access_account_partial_reconcile_group_invoice | FACT | always | — | Invoicing group has full CRUD on partial and full reconcile; readonly group read only | N-U12-211 |
| VDR-U12-C422 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:28 | access_account_bank_statement_group_readonly | FACT | always | — | Statement and line ACL: readonly and invoicing read only; basic full CRUD | N-U12-212 |
| VDR-U12-C423 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:92 | access_account_reconcile_model_billing | FACT | always | — | Reconcile model ACL: invoicing read and create; basic full; readonly read | N-U12-212 |
| VDR-U12-C424 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:106 | access_account_payment_term_manager | FACT | always | — | Payment term ACL: administrator full CRUD; internal users and portal read | N-U12-213 |
| VDR-U12-C425 | FUNCTION MAPPING REQUIRED | account/models/res_partner_bank.py:273 | _user_can_trust | FACT | always | — | _user_can_trust requires su, or group_validate_bank_account, or base.group_system, and a user other than the superuser unless install mode or tests | N-U12-215 |
| VDR-U12-C426 | FUNCTION MAPPING REQUIRED | account/models/res_partner_bank.py:61 | _check_allow_out_payment | FACT | always | — | Enabling allow_out_payment without the right raises ValidationError (disabling is allowed without the group) | N-U12-215 |
| VDR-U12-C427 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:101 | group_validate_bank_account | FACT | always | — | group_validate_bank_account (Bank privilege) is implied by base.group_system | N-U12-215 |
| VDR-U12-C428 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:194 | account_bank_statement_comp_rule | FACT | always | — | Global company rules: statements (company_ids + False), statement lines, payments (company_id in company_ids), reconcile models and lines and payment terms (parent_of / False) | N-U12-216 |
| VDR-U12-C429 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:232 | account_move_see_all | FACT | always | — | Rule All Journal Entries / All Journal Items domain (1,=,1) for account.group_account_invoice | N-U12-217 |
| VDR-U12-C430 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:452 | _accessible_branches | FACT | always | RT | Payment company is the accessible branch of the journal company when the journal company is not among the company's parents; wizard handles sibling companies with sudo and root-company rights check | N-U12-216 |
| VDR-U12-C431 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:10 | access_account_partial_reconcile_salesman | FACT | sale installed | — | sale ACL: sales_team.group_sale_salesman read on account.partial.reconcile and account.payment.term | N-U12-218 |
| VDR-U12-C432 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:29 | account_partial_reconcile | FACT | purchase installed | — | purchase ACL: group_purchase_user read on account.partial.reconcile | N-U12-218 |
| VDR-U12-C433 | FUNCTION MAPPING REQUIRED | sale_stock/security/ir.model.access.csv:12 | access_account_partial_reconcile | FACT | sale_stock installed | — | sale_stock ACL: stock.group_stock_manager full CRUD on account.partial.reconcile | N-U12-218 |
| VDR-U12-C434 | FUNCTION MAPPING REQUIRED | sale_stock/security/ir.model.access.csv:12 | stock.group_stock_manager | OBSERVATION | restored DB | — | DB lists this row under the group label 'Administrator' (the stock manager group), distinct from the accounting Administrator group | N-U12-223 |
| VDR-U12-C435 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:112 | access_account_payment_method, | OBSERVATION | restored DB | — | DB ir_model_access rows for account.payment, register, method, method line, term, term line, partial/full reconcile, statement, statement line, reconcile model/line, print.prenumbered.checks, payment link/refund/capture wizards and payment.* models equal the CSV permission strings (e.g. method: Invoicing 1101, internal users 1000; register: Invoicing 1110) | N-U12-211 |
| VDR-U12-C436 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:218 | account_payment_comp_rule | OBSERVATION | restored DB | — | DB: the studied record rules (statement, statement line, payment, term, reconcile model/line, payment provider, transaction, token company rule) are stored as global rules; the token own-partner rule applies to employee, portal and public groups | N-U12-216 |
| VDR-U12-C437 | FUNCTION MAPPING REQUIRED | account/views/account_payment_view.xml:402 | action_account_confirm_payments | FACT | always | — | Server action Post Payments (records.action_post()) bound to payment list/kanban, group account.group_account_invoice; DB has five server actions bound to payment, statement-line and move-line models | N-U12-221 |
| VDR-U12-C438 | FUNCTION MAPPING REQUIRED | account/wizard/account_unreconcile_view.xml:7 | group_account_user | FACT | always | — | Unreconcile server action group_ids = account.group_account_user | N-U12-226 |
| VDR-U12-C439 | FUNCTION MAPPING REQUIRED | account_check_printing/data/account_check_printing_data.xml:16 | group_account_user | FACT | account_check_printing installed | — | Print Checks server action restricted to account.group_account_user | N-U12-221 |
| VDR-U12-C440 | FUNCTION MAPPING REQUIRED | account/data/service_cron.xml:13 | ir_cron_account_move_send | FACT | always | — | account crons: auto-post draft entries (daily at 02:00 first call) and send invoices automatically (daily, root user); neither processes payments or statements | N-U12-219 |
| VDR-U12-C441 | FUNCTION MAPPING REQUIRED | payment/data/payment_cron.xml:4 | cron_post_process_payment_tx | OBSERVATION | restored DB | — | DB crons: Payment: Post-process transactions (10 minutes, active), Account: Post draft entries (daily, active), Send invoices automatically (daily, active); no cron for statements, matching or check printing | N-U12-219 |
| VDR-U12-C442 | FUNCTION MAPPING REQUIRED | account/data/service_cron.xml:3 | ir_cron_auto_post_draft_entry | OBSERVATION | restored DB | — | DB: base_automation is installed with zero rules, so the only scheduled or automated behaviours on these models are the cron records defined in code (compare account service_cron.xml and payment_cron.xml) | N-U12-220 |
| VDR-U12-C443 | FUNCTION MAPPING REQUIRED | account/models/company.py:258 | restrictive_audit_trail | FACT | always | — | Company restrictive_audit_trail option; when on, posted-before moves cannot be deleted (UserError) and statement lines are cancelled instead of deleted; DB value is off for the company | N-U12-222 |
| VDR-U12-C444 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4071 | restrictive_audit_trail | FACT | always | — | account.move ondelete guard raises UserError for posted-before moves of companies with restrictive audit trail (unless force_delete) | N-U12-222 |
| VDR-U12-C445 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:326 | without an outstanding | INFERENCE | always | — | Catalogue of refusal paths assembled from the claims of CAP-U12-01 to 08 (no single source line) | N-U12-224 |
| VDR-U12-C446 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:50 | group_account_readonly | UNKNOWN | always | RT | User-to-group membership was not queried (user data out of scope); effective rights per user cannot be stated | N-U12-225 |
