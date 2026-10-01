# U11 — account_entry_lifecycle — Restricted Technical Evidence

**RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION**

- Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U11 `account_entry_lifecycle` (Odoo 19 Community, VDR L2/L3 worker)
- Modules owned: `account` (entry/invoice/bill/credit-note lifecycle: `account.move`, `account.move.line`, `account.journal`, `sequence.mixin`, `account.lock_exception`, company lock fields, reversal/validate/secure/resequence wizards, audit-trail mail overrides)
- Source revision: `19.0.post20260921` (`odoo/addons`, Community only)
- Date: 2026-10-02
- Worker spec: `00_CONTROL/WORKER_SPEC_L2_L3.md` (two layers, claims table, anchors, honest partials). No V-levels, coverage %, gate or approval are asserted.
- Not owned (hand-off only): payments / reconciliation / bank statements / payment terms (U12); taxes / fiscal positions / chart / rounding / analytic distribution / localization (U13).

## 0. Scope, method and limits

- Read-only study of source; DB queried for configuration/structure only (counts, flags, constraint definitions, ACL/rule/cron rows). No business data printed; DB has zero journal entries and one company.
- Prior register `DOMAIN_01_ACCOUNTING_CORE/04_FUNCTION_REGISTER.md` (FN-01..FN-17) was found in the archived pilot tree (`_ARCHIVED/2026-09_VDR_PREP/.../TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/04_FUNCTION_REGISTER.md`), not at the path in the assignment; it was re-verified here and mapped below. Existing IDs (`PCO-F01`, `PCO-F02`, `PCO-F04`, `RCN-F02`, `SDV-F07`) come from `EXISTING_FUNCTION_ID_INDEX_53.json`; FN-xx ids are register ids, not part of that JSON.
- `account` is very large: `account_move.py` (7,489 lines) was read for the lifecycle paths listed in the claims; areas not read in detail are listed per capability under Unknown/Runtime (e.g. tax-line sync internals, abnormal-invoice warnings, e-invoice sending, QR/portal code).
- Pointer convention in prose: aliases are module-relative paths (`am:` = `account/models/account_move.py`, `aml:` = `account/models/account_move_line.py`, `co:` = `account/models/company.py`, `aj:` = `account/models/account_journal.py`, `ajd:` = `account/models/account_journal_dashboard.py`, `sm:` = `account/models/sequence_mixin.py`, `le:` = `account/models/account_lock_exception.py`, `wrev:` = `account/wizard/account_move_reversal.py`, `wval:` = `account/wizard/account_validate_account_move.py`, `wsec:` = `account/wizard/account_secure_entries_wizard.py`, `wreseq:` = `account/wizard/account_resequence.py`, `sec:` = `account/security/account_security.xml`, `csv:` = `account/security/ir.model.access.csv`, `cron:` = `account/data/service_cron.xml`, `mm:` = `account/models/mail_message.py`, `mtv:` = `account/models/mail_tracking_value.py`, `ru:` = `account/models/res_users.py`, `bsl:` = `account/models/account_bank_statement_line.py`, `pay:` = `account/models/account_payment.py`; other aliases name their module). The claims table below uses full module-relative paths.

## 1. Prior evidence re-verification (map and CONTRA)

| Prior ID | Prior statement (abridged) | Result against Odoo 19 Community source | Claim rows |
|---|---|---|---|
| FN-01 | `action_post` -> `_post(soft=True)` | CONTRA: `action_post` calls `_post(soft=False)` (hard); `soft=True` is only the default parameter (used by cron/programmatic callers) | VDR-U11-C005 |
| FN-02 | reset to draft guarded: must be posted or cancelled | MATCH, with extra guards (cancel request, exchange diff, caba, hash, lock) | VDR-U11-C022, VDR-U11-C023, VDR-U11-C024, VDR-U11-C025, VDR-U11-C026, VDR-U11-C027 ... |
| FN-03 | `button_cancel` | MATCH, nuance: posted entries are first reset to draft | VDR-U11-C030, VDR-U11-C031, VDR-U11-C032, VDR-U11-C033, VDR-U11-C034, VDR-U11-C035 ... |
| FN-04 | `_check_balanced` context manager wrapping create/write | MATCH; also wraps line create/write/unlink; single unbalanced entry message does not name the entry | VDR-U11-C059, VDR-U11-C060, VDR-U11-C061, VDR-U11-C062, VDR-U11-C063, VDR-U11-C064 ... |
| FN-05 | suppression via `_disable_recursion(...'check_move_validity'...)` | MATCH (only point_of_sale uses it, not installed) | VDR-U11-C069, VDR-U11-C070, VDR-U11-C071 |
| FN-06 | `_get_unbalanced_moves` with warning comment | MATCH | VDR-U11-C067, VDR-U11-C068 |
| FN-07 | `_reverse_moves` with `reversed_entry_id` | MATCH | VDR-U11-C224, VDR-U11-C225, VDR-U11-C226, VDR-U11-C227, VDR-U11-C228 |
| FN-08 | auto-reconcile draft reversals on posting | MATCH; only reconcilable or cash/credit-card accounts | VDR-U11-C229, VDR-U11-C230, VDR-U11-C251 |
| FN-09 | `_compute_name`, `highest_name`, prefix/number split | MATCH (regex-based mixin; no `ir.sequence` for entries) | VDR-U11-C109, VDR-U11-C110, VDR-U11-C111, VDR-U11-C112, VDR-U11-C113, VDR-U11-C114 ... |
| FN-10 | `secure_sequence_number` gapless counter for hashed journals | CONTRA: field exists but the current post/hash path never writes it; chain is journal + `sequence_prefix` + `sequence_number`; only legacy integrity report reads it | VDR-U11-C134, VDR-U11-C135 |
| FN-11 | constraint journal vs type | MATCH | VDR-U11-C079 |
| FN-12 | tax-country constraint | MATCH (detail U13) | VDR-U11-C080, VDR-U11-C106, VDR-U11-C107 |
| FN-13 | currency-rate constraint | MATCH | VDR-U11-C081 |
| FN-14 | require date for auto-post | CONTRA/NARROWED: only vendor documents (in_invoice, in_refund) need `invoice_date` | VDR-U11-C082 |
| FN-15 | journal write blocks clearing hash mode when hashed entries exist | MATCH | VDR-U11-C152, VDR-U11-C153 |
| FN-16 | account deprecation guard vs tax repartition | NOT VERIFIED here (U13 scope: account/tax configuration) | — |
| FN-17 | lock exception with audit interrogation | MATCH with detail (scope: one soft lock per exception, user or everybody, expiry, revoke by manager) | VDR-U11-C203, VDR-U11-C204, VDR-U11-C205, VDR-U11-C206, VDR-U11-C207, VDR-U11-C208 ... |
| PCO-F01 | Lock dates (global/purchase/sales/tax/hard) | MATCH; mechanics are postpone-on-post plus reject-on-edit; no Community UI found | VDR-U11-C168, VDR-U11-C169, VDR-U11-C170, VDR-U11-C171, VDR-U11-C172, VDR-U11-C173 ... |
| PCO-F02 | Fiscal year / period configuration | PARTIAL: only `fiscalyear_last_day/month` use in numbering (am:4277-4287) and company constraint (co:330-345); no period model in account | VDR-U11-C116, VDR-U11-C118, VDR-U11-C165 |
| PCO-F04 | Physical-date vs recorded-date cut-off | PARTIAL: accounting date vs invoice date logic and lock shift only; delivery/taxable supply date hooks are empty stubs in Community | VDR-U11-C187, VDR-U11-C188, VDR-U11-C189, VDR-U11-C190, VDR-U11-C191 |
| RCN-F02 | Backdating audit trail (dual chatter) | PARTIAL: `date` is tracked on the entry (am:128) and the lock-exception audit domain reads date tracking (le:257-296); the stock-side leg of 'dual' is not in this unit | CAP-U11-04, CAP-U11-09 |
| SDV-F07 | Return after invoicing, via credit note | PARTIAL: accounting leg (reversal wizard, linkage, reconciliation); the delivery/return leg is out of unit | VDR-U11-C223, VDR-U11-C231, VDR-U11-C232, VDR-U11-C233, VDR-U11-C234, VDR-U11-C235 ... |

## CAP-U11-01 Entry state machine (draft / posted / cancel; payment-state hand-off)

**Function-ID(s):** FN-01 (post; CONTRA on soft/hard), FN-02 (reset to draft), FN-03 (cancel). Payment-state derivation, scheduled/soft posting and `_unlink_or_reverse`: FUNCTION MAPPING REQUIRED.

**Claims:** VDR-U11-C001 .. VDR-U11-C058 (58 rows, see claims table)

### D1 Business purpose and process semantics

- Business purpose: a journal entry (manual entry, customer invoice/credit note, vendor bill/credit note, receipts) is prepared in `draft`, becomes ledger-affecting only when `posted`, and may be `cancel`led. Posting is the controlled act that assigns the number, fixes the accounting date against locks, creates analytic lines and (where configured) hashes the entry. Payment progress is a separate derived indicator (`payment_state`) that depends on reconciliation, not on user input.
- Process semantics: UI `Post` calls `action_post` -> `_post(soft=False)` (hard posting: immediate even for future dates, but refused if the entry is flagged for auto-post with a future date). `_post()` with the default `soft=True` (cron, many programmatic callers) defers future-dated entries by flagging `auto_post='at_date'`. Reset-to-draft and cancel are the only ways back; reversal (CAP-U11-05) is the audit-friendly correction path.

### D2 Architecture / data / object relationships

- `account.move` (state, move_type, payment_state, auto_post, auto_post_until, posted_before, checked, inalterable_hash, sending_data) 1—N `account.move.line` (stored related `parent_state`). Posting touches: `account.analytic.line` (created), partner ranks (`customer_rank`/`supplier_rank`), `account.partial.reconcile` (draft caba / reversal reconciliation), `mail.message` (tracking), plus extension tables from installed modules (EDI documents, stock valuation/COGS lines, fleet service logs).
- Inheritance: base `account.move` + overrides of `_post` in sale, stock_account, purchase_stock, account_edi, account_fleet, product_email_template, account_payment_interco; overrides of `button_draft`/`button_cancel` in sale, stock_account, account_edi, hr_expense, sale_expense; `action_post` in sale, sale_timesheet (and account_payment/hr_expense for other models).

### D3 Source / technical / workflow logic

State diagram (A -> B [trigger]):
- (new) -> draft [`create`; `state='posted'` in vals raises UserError, am:3895]
- draft -> posted [`action_post` -> `_post(soft=False)` am:6198; validation wizard `_post(not force_post)` wval:75; cron `_post()` am:6475; statement-line create -> `action_post` bsl:420]
- draft -> draft + `auto_post='at_date'` [`_post(soft=True)` and `date > today`, am:5691-5698; no state change, chatter note]
- posted -> draft [`button_draft` am:6269; blocked by: not posted/cancel, `need_cancel_request`, exchange-diff move, caba move, `inalterable_hash` (am:6348-6373), locked period via write() am:3953-3956]
- cancel -> draft [`button_draft`; same guards]
- draft -> cancel [`button_cancel` am:6384; removes reconciliations, sets payments canceled, `auto_post='no'`]
- posted -> cancel [`button_cancel` runs `button_draft` first, am:6387-6389]
- payment_state (derived): not_paid <-> partial <-> in_payment <-> paid; reversed (settled only by refunds/entries); blocked <-> not_paid via `action_toggle_block_payment` (am:6398-6406); invoicing_legacy preserved (am:1243).
- Control flow of `_post` (am:5569-5801): access check -> per-invoice validation (quick-edit total, bank account, negative total, partner, dates) -> per-move validation (account/journal/currency/company/analytic) -> raise all messages together -> soft split -> lock-date date shift -> analytic lines -> recurring copy -> OCR partner fix -> draft-caba partial handling -> `write(state=posted, posted_before=True)` (write() then flushes and `_hash_moves`) -> non-deductible line naming -> reconcile reversal / marked lines -> partner ranks -> zero-total paid hook.

### Ten-dimension table

| # / Dimension | Finding | Key pointers |
|---|---|---|
| 1 Happy path | Create draft -> `action_post` -> state posted, number assigned by `_compute_name`, analytic lines created, ranks incremented, hash applied if journal flag set. | am:6180-6201; am:5569-5801; am:4004-4006 |
| 2 Reversal / cancel / negative path | Reset to draft (guards incl. hash, caba, exchange, cancel-request, locks) and cancel (draft first, reconciliations removed, auto_post off); correction by reversal (CAP-U11-05). | am:6269-6396; am:6348-6373 |
| 3 Multi-company / data-scope | Entry company must be accessible; post refuses accounts of other company trees; record rules on company (see CAP-U11-09/10). | am:5673-5679; sec:128-138 |
| 4 Side effects & cross-module triggers | Analytic lines; partner ranks; sale reconciles payment-transaction payments; stock_account/purchase_stock add COGS/anglo-saxon lines before posting; account_edi creates EDI documents; fleet service logs; product e-mail; intercompany clearing; sale/hr_expense/sale_expense/timesheet adjust links on draft/cancel/post. | sale:120-133; stockacc:29-44; pstock:113-118; edi:233-265; fleet:9-29; pet:25-29; interco:30-37 |
| 5 Configuration & optionality | Context keys: `disable_abnormal_invoice_detection`, `skip_account_deprecation_check`, `skip_recurring_copy`, `move_reverse_cancel`; confirmation wizard for future/hash-journal entries; `abnormal` warnings off by default. | am:6182-6196; am:6203-6237; am:5670; am:5712 |
| 6 Validation & constraints | See CAP-U11-02 (message set raised together); state-specific: must be draft, must have non-note lines, no auto-post-future in hard mode, no archived journal/account/currency. | am:5650-5683 |
| 7 Roles & permissions | `_post` requires superuser or `account.group_account_invoice`; button_draft on checked entries requires review right (always true with account only); validation wizard ACL: invoicing group. | am:5583-5584; am:3918-3921; am:7014-7016; csv:120 |
| 8 Scheduled/automated behavior | Soft posting defers future entries to the daily cron (CAP-U11-06); statement-line moves are auto-posted at creation. | am:5691-5698; am:6460-6493; bsl:420 |
| 9 Exception & failure behavior | All validation messages collected and raised as one UserError; AccessError for non-invoicing users; RedirectWarning for untrusted company bank account; cron catches UserError per entry (CAP-U11-06). | am:5681-5683; am:5583; am:5613 |
| 10 Accounting, stock, audit, security & compliance | Posted entries are immutable for key fields (readonly check, lock checks); `posted_before` drives audit-trail deletion rules; hash on post; COGS/valuation lines when stock_account installed; chatter tracking on `state`. | am:3958-3969; am:322; am:128-142 |

### DB reconciliation (configuration only)

Restored DB: 0 rows in `account_move` and `account_move_line`; module `account` and extensions (`sale`, `purchase`, `stock_account`, `purchase_stock`, `account_edi`, `account_fleet`, `product_email_template`, `account_payment_interco`, `hr_expense`, `sale_expense`, `sale_timesheet`) are installed (356 installed modules). Cron 'Account: Post draft entries...' is active (see CAP-U11-06).

### Unknown / Runtime list

- RT: effective behaviour of the validation wizard under multi-select with mixed hash/future entries.
- RT: whether cancelling keeps the assigned number reserved in every numbering configuration (name is not cleared by `button_cancel`, `_compute_name` skips `cancel`).
- RT: interplay of sale/stock_account/purchase_stock `_post` overrides on one invoice (order of COGS vs anglo-saxon line creation).

## CAP-U11-02 Posting validation (balance assertion, required fields, journal/type, currency, tax-country, date, auto-post)

**Function-ID(s):** FN-04 (assert balance), FN-05 (suppress), FN-06 (detect unbalanced), FN-11, FN-12 (U13 hand-off), FN-13, FN-14 (narrowed, CONTRA), FN-01 (posting validation message set).

**Claims:** VDR-U11-C059 .. VDR-U11-C108 (50 rows, see claims table)

### D1 Business purpose and process semantics

- Business purpose: protect the double-entry invariant, the integrity of document metadata (partner, dates, bank account), and the consistency of journal, currency and tax configuration before an entry becomes ledger-affecting.
- Process semantics: the balance test runs on every create/write/unlink of entries and lines (not only at posting); posting adds a second layer of document-completeness validation that is aggregated into one error; database CHECK constraints and a partial unique index are a third layer.

### D2 Architecture / data / object relationships

- Objects: `account.move` (constraints `_check_journal_move_type`, `_validate_taxes_country`, `_check_invoice_currency_rate`, `_require_bill_date_for_autopost`, unique index on posted names), `account.move.line` (CHECK constraints, `_check_off_balance`, `_check_payable_receivable`, `_check_constrains_account_id_journal_id`), `res.company` (`account_storno`, fiscal country), `account.journal`.
- Balance check uses SQL against stored `balance` of lines joined to the company currency decimals (am:2810-2821), independent of computed fields; automatic balancing line for tax-bearing drafts (am:3204-3245).

### D3 Source / technical / workflow logic

- Control flow: `create`/`write`/`unlink` -> `with self._check_balanced(container)` -> body -> if the recursion stack/context `check_move_validity` is False the post-check is skipped (am:2786-2789) -> else `_get_unbalanced_moves` -> UserError (1 entry: generic message; many: names listed).
- Suppression mechanism: `_disable_recursion(container,'check_move_validity',default=True,target=False)` (am:7052-7078) keeps a StackMap in `cr.cache['account_disable_recursion_stack']`; a block executed with context `check_move_validity=False` (or an enclosing stack entry False) yields `disabled=True`. Only Community callers: point_of_sale pos_session (not installed).
- Posting validations (am:5583-5689): see claims; they are grouped in `validation_msgs` and raised together, except the archived analytic account check (raised separately) and RedirectWarning/UserError for company bank account trust.
- Auto-sync side: for non-posted moves involving taxes `_sync_unbalanced_lines` (stack priority 20) creates/updates an 'Automatic Balancing Line' on the journal default or suspense account (am:3204-3245) so such entries do not fail the balance check.

### Ten-dimension table

| # / Dimension | Finding | Key pointers |
|---|---|---|
| 1 Happy path | Balanced entry with required fields passes `_check_balanced`, constraints and `_post` message set; DB CHECKs satisfied. | am:2781-2821; am:5583-5683 |
| 2 Reversal / cancel / negative path | Negative invoice total refused with advice to use credit note; reset/cancel do not re-run balance check except through line writes; reversal of unbalanced impossible by construction. | am:5624-5629 |
| 3 Multi-company / data-scope | Accounts must belong to move company or its parents; journal/partner/bank checked by `check_company`; balance SQL joins company currency. | am:5673-5679; am:2816-2819 |
| 4 Side effects & cross-module triggers | Automatic balancing line; EDI and localization may add constraints (not installed); pos_session sets suspension flag (not installed). | am:3204-3245; pos:442 |
| 5 Configuration & optionality | Quick-edit total check only in quick-edit mode; `skip_account_deprecation_check` context; `check_move_validity` suspension; `sequence.mixin.constraint_start_date` parameter for the date-number constraint. | am:5592-5602; am:5670; am:2786; sm:160 |
| 6 Validation & constraints | Full list in claims: balance, line CHECKs (4), journal/type, tax country, currency rate>0, bill date for auto-post (vendor docs only), unique posted name, off-balance, payable/receivable, archived account/journal/currency/analytic, partner/date required, negative total. | am:2842-2883; aml:483-498; aml:1478-1520 |
| 7 Roles & permissions | Posting needs invoicing group; constraints are not role dependent; the bank-account trust bypass depends on superuser/public/portal. | am:5583; am:5608-5623 |
| 8 Scheduled/automated behavior | Cron-driven `_post()` runs the same validation; failures are caught per entry (CAP-U11-06). | am:6474-6493 |
| 9 Exception & failure behavior | UserError vs ValidationError vs RedirectWarning; DB CHECK failures surface as ORM integrity errors (not read). | am:2793; am:2799; am:5681-5683 |
| 10 Accounting, stock, audit, security & compliance | Balance rounding at company-currency precision; automatic balancing may post to suspense; messages and constraints protect tax-country integrity of reports. | am:2810-2821; am:2857-2870 |

### DB reconciliation (configuration only)

Restored DB: the four CHECK constraints on `account_move_line` and the partial unique index `account_move_unique_name` on `(name, journal_id) WHERE state='posted' AND name != '/'` exist and match the source. No entries exist, so constraint behaviour cannot be observed (RT).

### Unknown / Runtime list

- RT: wording/ordering of combined validation messages when several conditions fail at once.
- RT: DB-level IntegrityError presentation for CHECK violations.
- UNKNOWN — EVIDENCE INSUFFICIENT: invoice abnormal-amount/date warning algorithm (am:2251-2360) was not read in detail; it only warns unless the wizard flow is enabled.

## CAP-U11-03 Naming, sequences and inalterability (hash chain)

**Function-ID(s):** FN-09 (compute name), FN-10 (inalterability sequence/hash; CONTRA on `secure_sequence_number`), FN-15 (hash-mode disable guard).

**Claims:** VDR-U11-C109 .. VDR-U11-C167 (59 rows, see claims table)

### D1 Business purpose and process semantics

- Business purpose: give every posted entry a unique, ordered, period-consistent number and, optionally, make posted entries tamper-evident through a per-journal hash chain, as required by audit and some national regulations.
- Process semantics: numbers are assigned at posting (not for drafts); the pattern is inferred from the previous number of the same journal (and refund/payment/partner sub-chain); hash chaining is journal opt-in or on-demand and, once applied, irreversibly locks fields and lines.

### D2 Architecture / data / object relationships

- `sequence.mixin` fields `sequence_prefix`, `sequence_number` (stored, computed from `name`), `account.move.name`, `made_sequence_gap`, `inalterable_hash`, `secured`, legacy `secure_sequence_number`; journal fields `code`, `refund_sequence`, `payment_sequence`, `is_self_billing`, `sequence_override_regex`, `restrict_mode_hash_table`; company `fiscalyear_last_day/month`; group `account.group_account_secured`; wizards `account.secure.entries.wizard`, `account.resequence.wizard`.
- No `ir.sequence` is used for entries in Community (only a payment sequence record exists in data); numbering is computed by regex from the last number in SQL (sm:243-310).

### D3 Source / technical / workflow logic

- Number allocation: `_compute_name` (am:952) -> `_set_next_sequence` (sm:425) -> `_get_next_sequence_format` (sm:449) -> `_get_last_sequence` with `_get_last_sequence_domain` (am:4201) -> if none, relaxed search or `_get_starting_sequence` (am:4273) -> `_locked_increment` (sm:355): UPDATE of the row under the unique partial index inside a savepoint, retry on UniqueViolation, per-transaction cache.
- Reset kinds detected from the reference number: year_range_month, month, year_range, year, never (sm:193-225). Date/number consistency constraint (sm:156-181, applied to posted moves only, am:4197).
- Hash chain: `write(state='posted')` -> `_hash_moves` (am:4004-4006, am:4625) -> `_get_chains_to_hash` per journal and sequence_prefix (am:4727) -> `_get_chain_info` (am:4639) selects posted, unhashed moves after the last hashed one, warns/raises on gaps, unreconciled statement lines, no document -> `_calculate_hashes` (am:4771) SHA-256(previous_hash + JSON of fields), version 4 prefix `$4$`.
- After hashing: write guard on integrity fields (am:3923-3929, aml:1827-1836), line unlink guard (aml:1982-1989), reset-to-draft guard (am:6372), `_can_be_unlinked` False (am:5546), line name recompute skipped (aml:575), resequence by date forbidden (wreseq:157-159).
- Disable guard: journal write refuses clearing `restrict_mode_hash_table` if any posted hashed move exists (aj:786-793).

### Ten-dimension table

| # / Dimension | Finding | Key pointers |
|---|---|---|
| 1 Happy path | Posting a draft in journal INV assigns e.g. prefix/year/counter by pattern; with hash flag the move and all earlier unhashed ones of the chain are hashed. | am:952-968; am:4625-4637 |
| 2 Reversal / cancel / negative path | Deleting numbered moves limited to chain tail for non-managers; changing journal after numbering refused; hashed entries cannot be reset/deleted; reversal creates a new number. | am:4048-4066; am:3930-3943; am:6372-6373 |
| 3 Multi-company / data-scope | Sequences are per journal (journal belongs to one company); hash chain search uses sudo; self-billing chains per commercial partner. | am:80; am:4647-4649; am:4218-4223 |
| 4 Side effects & cross-module triggers | Hashing logs 'secured' and may enable the inalterability feature group; localizations may add secure sequence fields (l10n_fr_pos_cert, not installed). | am:4635-4637; ru:27-38 |
| 5 Configuration & optionality | Journal `restrict_mode_hash_table` (NULL in DB), `refund_sequence`, `payment_sequence`, `sequence_override_regex`, company fiscal year end, config parameter `sequence.mixin.constraint_start_date`; on-demand hashing wizard or `button_hash`. | aj:145-146; aj:177-203; sm:160; wsec:260-269; am:6375 |
| 6 Validation & constraints | Unique posted name per journal; date vs number constraint; gap/no-document/unreconciled errors at hash time; integrity field write guards; override-regex conformity for non-managers. | am:791-794; sm:156-181; am:4753-4764; am:3971-3974 |
| 7 Roles & permissions | Resequence wizard and secure wizard ACL = account manager only; hash integrity report needs `group_account_user`; deletion of chain-middle moves needs account manager / fiduciary mode / force_delete. | csv:119; co:1008; am:4057-4062 |
| 8 Scheduled/automated behavior | Hashing is triggered synchronously on post; dashboard computes `has_unhashed_entries` and `has_sequence_holes` indicators (query at ajd:150-200). | am:4004-4006; ajd:150-206 |
| 9 Exception & failure behavior | Errors for gaps, unreconciled lines, nothing to hash; concurrency handled by lock-and-retry in `_locked_increment`; `ValidationError` when regex lacks seq. | am:4753-4764; sm:409-424; sm:222-225 |
| 10 Accounting, stock, audit, security & compliance | Tamper evidence (v4 hash incl. name, date, journal, company and line name/debit/credit/account/partner); legacy `secure_sequence_number` retained read-only; integrity report supports hash versions 1-4. | am:4592-4603; aml:3394-3401; co:1005-1096 |

### DB reconciliation (configuration only)

Restored DB: `restrict_mode_hash_table` is NULL (not set) on all 7 journals; 0 entries; `ir_sequence` has 1 `account.*` record (payment); partial unique index on posted names present; no `secure_sequence_number` usage possible without data.

### Unknown / Runtime list

- RT: exact starting pattern produced for journals INV/BILL/BNK1 given the company fiscal year end 31/12 and chart th (not re-derived).
- RT: behaviour under concurrent posting (savepoint/retry path).
- RT: whether a hash-protected journal on first post hashes only the posted entry or an earlier unhashed backlog (code says up to last hashed or first of chain).

## CAP-U11-04 Lock dates and lock exceptions

**Function-ID(s):** PCO-F01 (Lock dates incl. hard lock), PCO-F04 (physical vs recorded date cut-off; partial), PCO-F02 (fiscal year configuration; partial via fiscal-year-end fields), FN-17 (lock exception).

**Claims:** VDR-U11-C168 .. VDR-U11-C222 (55 rows, see claims table)

### D1 Business purpose and process semantics

- Business purpose: freeze closed accounting periods. Five kinds exist (global/fiscal-year, tax return, sale, purchase, hard). Soft locks can be relaxed per user or for everyone through time-boxed, audited exceptions; the hard lock is irreversible.
- Process semantics (Odoo 19): locks mostly postpone rather than reject at posting (date is shifted to the first open date), while edits of already posted entries inside a lock are rejected. This differs from older 'raise on lock' behaviour and is central to the accounting-date logic (CAP-U11-04/PCO-F04).

### D2 Architecture / data / object relationships

- `res.company` lock fields + computed per-user fields `user_*_lock_date` (depends on `uid`, `ignore_exceptions`); `account.lock_exception` (company, user, lock_date_field, lock_date, company_lock_date, end_datetime, active/state, reason); `account.move._get_violated_lock_dates`/`_check_fiscal_lock_dates`; `account.move.line._check_tax_lock_date` and `_get_lock_date_protected_fields`; journal dashboard and `account.secure.entries.wizard` consume lock dates.
- Company hierarchy: lock evaluation walks `parent_ids` (branches inherit parents' locks).

### D3 Source / technical / workflow logic

- Effective user lock for a field: for each company in parent chain with a lock date -> find active exception (user match or global, exception date earlier, earliest first) else company date; max over chain (co:607-640). Hard lock: max over chain, no exceptions (co:442-448).
- Violation for a date: soft lock violated only if date <= lock ignoring exceptions AND still <= lock including the user's exceptions (co:656-673); selection of checked kinds per operation (co:675-739).
- Operations: (a) posting -> date shift (am:5702-5706, am:6714-6751); (b) write of date/name/state on posted entry -> `_check_fiscal_lock_dates` (fiscal+sale/purchase by journal type + hard, no tax) and `_check_tax_lock_date` on lines (am:3945-3956, am:3997-4002); (c) line write of protected fields on posted lines (aml:1849-1858, aml:3485-3496); (d) line unlink (aml:1997-2004); (e) entry unlink eligibility (am:5541-5546); (f) copy/reverse date proposal (am:3827-3829).
- Setting locks: `res.company.write` -> `_validate_locks` (hard lock monotonic, no drafts in hard-locked period, no unreconciled bank statement lines in fiscal/hard period) -> invalidation -> revoke-and-recreate active exceptions (co:741-772).
- Exception lifecycle: create (single field) -> chatter log on company -> active until `end_datetime` or revoked by account manager/superuser; `copy` forbidden; audit button lists entries changed during exception (le:164-306).

### Ten-dimension table

| # / Dimension | Finding | Key pointers |
|---|---|---|
| 1 Happy path | Company sets e.g. global lock date; posting an entry dated before it moves its date to the day after (adjusted to period); users with an exception can edit within the excepted window. | co:741-772; am:5702-5706; co:607-640 |
| 2 Reversal / cancel / negative path | Reset to draft/cancel of a posted entry inside a lock is refused (write checks); reversal dated inside a lock is shifted; deletion of posted entries in lock refused. | am:3953-3956; am:3827-3829; am:5541-5546 |
| 3 Multi-company / data-scope | Locks inherited from parent companies; exceptions are per company; hard lock max over parents; dashboard comment: branch locked when parent locked. | co:617; co:442-448; ajd:150-153 |
| 4 Side effects & cross-module triggers | Bank statement reconciliation gates fiscal/hard lock; tax report/tax tags protected by tax lock; point_of_sale validates session dates vs locks (not installed); localizations call `_check_fiscal_lock_dates` (not installed). | co:597-605; aml:1526-1543 |
| 5 Configuration & optionality | All five fields unset in DB; no Community UI to maintain them was found; exception reason/user/expiry are optional. | co:76-102; le:15-70 |
| 6 Validation & constraints | Hard lock can only advance and needs no drafts; fiscal/hard lock needs no unreconciled statement lines; exception must change exactly one soft lock; exceptions cannot be copied. | co:552-605; le:172-180; le:218-219 |
| 7 Roles & permissions | Exception create: account manager (ACL read+create), read: all internal users; revoke: manager or superuser; company write: base `group_erp_manager`; no role check in `_validate_locks`. | csv:18-19; le:234-243; basecsv:42; co:552 |
| 8 Scheduled/automated behavior | None; exception expiry is evaluated lazily by `state` (end_datetime vs now). | le:104-112; le:123-134 |
| 9 Exception & failure behavior | UserError 'cannot add/modify entries prior to and inclusive of ...'; tax lock error 'impact an already issued tax statement'; RedirectWarning for drafts/unreconciled lines when locking. | am:2837-2839; aml:1540-1542; co:584; co:605 |
| 10 Accounting, stock, audit, security & compliance | Exception creation is logged on company chatter with tracking value; per-exception audit domain; lock fields are tracked on the company; date shift can move entries into later periods (reporting effect). | le:187-213; le:257-296; co:76-102 |

### DB reconciliation (configuration only)

Restored DB: 1 company, all five lock dates NULL; `account_lock_exception` has 0 rows; all five lock fields are tracked (ir_model_fields); ACL rows for lock exception: Role/User read, Administrator read+create.

### Unknown / Runtime list

- RT: Community UI exposure of lock dates (no view found in account; may exist in the base company form or be absent).
- UNKNOWN — EVIDENCE INSUFFICIENT: automatic setting of the tax lock date at tax closing (help text claims it; no Community code found).
- RT: interaction of the date shift with hash chains, sequence reset periods and branch companies.

## CAP-U11-05 Reversal and credit notes

**Function-ID(s):** FN-07 (reverse), FN-08 (auto-reconcile reversal), SDV-F07 (return after invoicing via credit note; partial: only the accounting leg is in scope here).

**Claims:** VDR-U11-C223 .. VDR-U11-C252 (30 rows, see claims table)

### D1 Business purpose and process semantics

- Business purpose: correct or cancel posted documents without editing them: reversal creates an opposite entry, and for invoices a credit note, linked through `reversed_entry_id`.
- Process semantics: the reversal wizard offers two outcomes: (1) 'Credit Note/Reverse' creates a draft opposite document that the user may edit and post (partial credit by editing lines); (2) 'Cancel / modify' posts the reversal immediately, reconciles it with the original, and optionally rebuilds a new draft copy. Entries (type entry) are reversed and posted at once.

### D2 Architecture / data / object relationships

- `account.move.reversed_entry_id` / `reversal_move_ids`; `TYPE_REVERSE_MAP`; wizard `account.move.reversal` (move_ids, date, reason, journal_id, company_id); reconciliation objects (`account.partial.reconcile`) via `lines.reconcile()`; storno flag on lines; extension modules sale, hr_expense, sale_expense, sale_timesheet, purchase.

### D3 Source / technical / workflow logic

- Wizard `reverse_moves` (wrev:110-174): defaults per move (`_prepare_default_reversal` wrev:92-108) -> batches: cancel batch if not auto-post and (modify option or wizard move_type entry) else plain batch -> `_reverse_moves` (am:5495-5539) -> log on original -> modify option creates a new draft from product/section/note lines (wrev:142-149).
- `_reverse_moves`: (cancel) remove reconciliations -> `copy(default)` with `move_reverse_cancel`, `include_business_fields` contexts (copy_data shifts date after lock, am:3827-3829; drops partner for entries, am:3824-3826) -> negate balance/amount_currency for entries and cogs lines (am:5525-5533) -> if cancel `_post(soft=False)`.
- Posting a draft reversal later: `_post` collects `draft_reverse_moves` (am:5726) and after writing state calls `_reconcile_reversed_moves` (am:5775), which reconciles unreconciled lines grouped by (account, currency) only for reconcilable accounts or cash/credit-card types (am:5474-5492).
- State diagram: posted original -> [reverse] -> reversal draft -> [post] -> reversal posted + reconciled (payment_state of original becomes `reversed` when only refunds/entries settle it, am:1307-1319).

### Ten-dimension table

| # / Dimension | Finding | Key pointers |
|---|---|---|
| 1 Happy path | Credit note button on posted invoice -> draft out_refund linked to the invoice -> user posts it -> reconciled and invoice shows reversed/partial/paid as applicable. | wrev:176-177; am:5726; am:5775 |
| 2 Reversal / cancel / negative path | Reversal date in the future -> auto_post at_date; reversal in lock -> date shifted; cancel option posts and reconciles immediately; hashed original is untouched. | wrev:106; am:3827-3829; am:5536-5537 |
| 3 Multi-company / data-scope | Selection must be one company; wizard journal limited to company and same journal type. | wrev:71-72; wrev:47-58 |
| 4 Side effects & cross-module triggers | sale copies campaign/medium/source; hr_expense clears expense link; sale_expense resets SO quantities; sale_timesheet releases timesheets on credit-note post; purchase skips PO message for reversals. | sale:71-81; hrexp:101-104; saleexp:9-12; saleaccm:99-108; purchase:176-177 |
| 5 Configuration & optionality | Origin link only enforced when `_refunds_origin_required` (False in Community); storno accounting toggles line sign flag (company flag false in DB). | am:7385-7397; am:5529 |
| 6 Validation & constraints | Only posted moves; same company; journal type match; standard `_post` validation on the credit note. | wrev:60-82 |
| 7 Roles & permissions | Wizard ACL: invoicing group read/write/create; posting requires invoicing group. | csv:121; am:5583 |
| 8 Scheduled/automated behavior | Future-dated reversals are flagged `at_date` and posted by the daily cron. | wrev:106; am:6460-6493 |
| 9 Exception & failure behavior | UserError for non-posted selection / mixed companies / wrong journal type. | wrev:71-77; wrev:64 |
| 10 Accounting, stock, audit, security & compliance | Reversal is the audit-friendly correction; original keeps hash; reversal logged on both entries ('has been reversed from'/'This entry has been reversed'). | am:3852; wrev:138-140 |

### DB reconciliation (configuration only)

Restored DB: no entries; `account_storno` false; ACL `access_account_move_reversal` (Invoicing: read/write/create) present.

### Unknown / Runtime list

- RT: reconciliation outcome for multi-currency originals and for caba entries on reversal (code path: `reconcile()` with `move_reverse_cancel` context).
- RT: wizard `move_type` for multi-selection ('some_invoice' or False) means the immediate-cancel branch only triggers for a single entry or the modify option — confirm by execution.
- INFERENCE: partial credit is done by editing the draft credit note; no amount field exists in the wizard (wrev:15-31).

## CAP-U11-06 Auto-post and scheduled entries

**Function-ID(s):** FUNCTION MAPPING REQUIRED (no existing ID covers scheduled/recurring posting).

**Claims:** VDR-U11-C253 .. VDR-U11-C275 (23 rows, see claims table)

### D1 Business purpose and process semantics

- Business purpose: let users prepare entries ahead of time (accruals, recurring charges, future-dated documents) and have the system post them on the accounting date; recurring entries propagate themselves.
- Process semantics: entries with `auto_post != 'no'` and `date <= today` are posted by a daily cron; recurring options (monthly/quarterly/yearly) copy the next occurrence on posting; failures disable auto-post on the failing entry and leave a note.

### D2 Architecture / data / object relationships

- `account.move.auto_post`, `auto_post_until`, `auto_post_origin_id`; cron `ir_cron_auto_post_draft_entry` (model `account.move`, code `model._autopost_draft_entries()`); `ir.cron._commit_progress`; journal archive constraint; company `autopost_bills`, partner `autopost_bills` (bill auto-validation, separate mechanism).

### D3 Source / technical / workflow logic

- Cron: `_autopost_draft_entries(batch_size=100)` (am:6460-6493): domain draft & date<=today & auto_post!='no' -> try `moves._post()` as batch; on UserError rollback and per move: `try_lock_for_update().filtered_domain(domain)` -> `_post()`; on UserError rollback, chatter comment, `auto_post='no'`.
- Recurrence: `_post` -> `_copy_recurring_entries` (am:5711-5713, am:4816-4852): next date = origin date + n periods, copy unless an entry with that date and origin exists or `auto_post_until` passed; `button_draft` deletes next draft recurrence (am:6319-6346).
- Soft/hard: `_post(soft=True)` flags future entries (am:5691-5698); hard posting refuses flagged future entries (am:5656-5658); validation wizard can force (wval:69-70).

### Ten-dimension table

| # / Dimension | Finding | Key pointers |
|---|---|---|
| 1 Happy path | Entry dated next month with auto_post 'at_date' stays draft; on that date the cron posts it; monthly entries create next month's draft. | am:6460-6476; am:4816-4852 |
| 2 Reversal / cancel / negative path | Failure -> note + auto_post 'no'; reset to draft of a recurring entry deletes next draft; cancel writes auto_post 'no'. | am:6488-6493; am:6319-6346; am:6396 |
| 3 Multi-company / data-scope | Cron searches across companies with the cron user (root); company of each move applies in `_post`. | cron:3-11; am:6465-6470 |
| 4 Side effects & cross-module triggers | Recurring copies call `copy()` with extension hook; stock_account closing cron creates auto-posted valuation entries; reversal entries future-dated use the same mechanism. | am:4854-4862; stockco:148; wrev:106 |
| 5 Configuration & optionality | Cron interval/active set by admin (daily, active in DB); `auto_post_until` optional; `skip_recurring_copy` context. | cron:3-11; am:5712 |
| 6 Validation & constraints | Vendor docs need a bill date when auto_post set; journals with drafts cannot be archived; hard lock requires no drafts in period. | am:2842-2847; aj:677-691; co:578-594 |
| 7 Roles & permissions | Cron runs as the root user (DB: user_id resolves to base root); `_post` permits superuser; setting auto_post needs write rights on entries (invoicing group). | am:5583; csv:38 |
| 8 Scheduled/automated behavior | Daily at first call 02:00 next day; batches of 100; progress committed per batch/move. | cron:7; am:6460-6493 |
| 9 Exception & failure behavior | Only UserError caught; others propagate; rollback of batch then per-entry retry. | am:6478-6493 |
| 10 Accounting, stock, audit, security & compliance | Posting date equals entry date (<= today); numbers allocated at cron time; chatter message documents failures. | am:6490-6492; am:5691-5698 |

### DB reconciliation (configuration only)

Restored DB: cron id 17 'Account: Post draft entries with auto_post enabled and accounting date up to today' active, daily, user root, failure_count 0; 0 entries.

### Unknown / Runtime list

- RT: scheduler progress/commit semantics of `_commit_progress` (base) and exception propagation.
- RT: time-zone effect of `context_today` on the selection date in a cron context.

## CAP-U11-07 Entry-line computation and dynamic lines

**Function-ID(s):** FUNCTION MAPPING REQUIRED (tax-line and payment-term detail hand off to U13/U12).

**Claims:** VDR-U11-C276 .. VDR-U11-C311 (36 rows, see claims table)

### D1 Business purpose and process semantics

- Business purpose: keep balance, debit/credit and document-currency amounts consistent and synthesize system lines (payment terms, taxes, rounding, discounts, early-payment, non-deductible) from the invoice lines.
- Process semantics: `balance` (company currency, signed) is the master; `debit`/`credit` derive from it; `amount_currency` and `currency_rate` convert both ways; dynamic lines are re-synchronised around every create/write of the move or its lines.

### D2 Architecture / data / object relationships

- `account.move.line` fields: `display_type` (13 values), `balance`, `debit`, `credit`, `amount_currency`, `currency_id`, `currency_rate`, `is_storno`, keys `term_key`, `discount_allocation_key`, `epd_key`; `account.move` helper fields `needed_terms`/`needed_terms_dirty`, `invoice_currency_rate`; tax objects owned by U13, payment terms by U12.

### D3 Source / technical / workflow logic

- Sync stack (am:3722-3764): 10 payment_term, 20 unbalanced, 30 rounding, 40 discount, 50 tax, 60 non-deductible, 70 epd, 80 invoice partner; wrapped by `_sync_dynamic_lines` (am:3767-3784) in `create` (am:3899) and `write` (am:3982).
- Generic algorithm `_sync_dynamic_line` (am:3591-3695): snapshot needed/existing before, run body, then delete obsolete / rewrite replaced / create missing / update changed; early-return when needs unchanged or user created lines manually.
- Amount sync: `_sanitize_vals` converts debit/credit to balance (aml:1693-1712); `_sync_invoice` at line level (aml:1733-1778); computes `_compute_balance`, `_compute_debit_credit`, `_compute_amount_currency`, `_compute_currency_rate` (aml:727-783); inverses (aml:1413-1439).

### Ten-dimension table

| # / Dimension | Finding | Key pointers |
|---|---|---|
| 1 Happy path | Invoice with product lines gets tax lines, one or more payment-term lines and rounding; debit/credit derived from balance. | am:3722-3784; aml:727-783 |
| 2 Reversal / cancel / negative path | Reversal copies lines (payment term name dropped, product balance recomputed); entry reversals negate balance directly. | aml:2078-2094; am:5525-5533 |
| 3 Multi-company / data-scope | Line company related to move; line `check_company`; accounts computed with company-specific properties. | aml:56-59; aml:607-660 |
| 4 Side effects & cross-module triggers | Taxes (U13), payment terms (U12), stock COGS lines (stock_account), cash rounding, down-payment/discount lines. | am:3287; am:1389; stockacc:29-44 |
| 5 Configuration & optionality | Rounding method and cash rounding on company/invoice (U13); `skip_invoice_sync` context disables sync; payment reference/term influence labels. | am:3768; aml:574-593 |
| 6 Validation & constraints | DB CHECKs on lines; `_check_payable_receivable`; dynamic lines undeletable by hand unless `dynamic_unlink`. | aml:483-498; aml:1507-1520; aml:1968-1980 |
| 7 Roles & permissions | Invoicing group full CRUD on lines; others read. | csv:35-42 |
| 8 Scheduled/automated behavior | None; recomputation is event-driven. | am:3767-3784 |
| 9 Exception & failure behavior | Constraint violations surface from DB; sync tries to avoid overwriting manual input. | am:3644-3647 |
| 10 Accounting, stock, audit, security & compliance | Hashed moves skip label recompute; amounts rounded at currency precision; posted lines cannot change protected fields. | aml:575; aml:1827-1836 |

### DB reconciliation (configuration only)

Restored DB: CHECK constraints on lines present (see CAP-U11-02); no lines exist.

### Unknown / Runtime list

- RT: rounding outcomes for tax-included prices with cash rounding and foreign currencies.
- UNKNOWN — EVIDENCE INSUFFICIENT: `_sync_tax_lines` (am:3287-3495) and `_sync_non_deductible_base_lines` (am:3496-3589) internals not analysed here (U13).

## CAP-U11-08 Journals

**Function-ID(s):** FN-15 (hash-mode disable guard); other journal functions: FUNCTION MAPPING REQUIRED.

**Claims:** VDR-U11-C312 .. VDR-U11-C343 (32 rows, see claims table)

### D1 Business purpose and process semantics

- Business purpose: classify entries into books (sales, purchase, cash, bank, credit card, miscellaneous), supply default/suspense accounts, numbering prefix and chain options, and e-mail/e-invoice intake.

### D2 Architecture / data / object relationships

- `account.journal` (type, code, default_account_id, suspense_account_id, currency_id, restrict_mode_hash_table, refund_sequence, payment_sequence, is_self_billing, sequence_override_regex, alias, payment method lines, bank account), `account.journal.group`; relation to `account.move.journal_id` (required, FK RESTRICT in DB).

### D3 Source / technical / workflow logic

- Creation: `_fill_missing_values` (aj:955-1019) creates liquidity accounts for bank/cash, default accounts for sale/purchase, alias for sale/purchase; `create` (aj:1021-1038) sets bank account. Default code `_get_next_journal_default_code` (aj:876-895).
- Move<->journal consistency: `_get_valid_journal_types` (am:902-909), `_search_default_journal` (am:911-938), constraint `_check_journal_move_type` (am:2849-2855), `_inverse_journal_id` recomputes company/currency (am:2625-2634).
- Guards: unique code per company (aj:293-296), company change vs entries (aj:597-604), default-account type (aj:606-610), archive vs drafts (aj:677-691), hash disable (aj:786-793), bank account holder (aj:586-595).

### Ten-dimension table

| # / Dimension | Finding | Key pointers |
|---|---|---|
| 1 Happy path | New sale journal with code, default income account, alias; entries numbered with its code. | aj:955-1038 |
| 2 Reversal / cancel / negative path | Archive blocked with drafts; delete blocked by FK RESTRICT when entries exist; unarchive not checked. | aj:677-691; am:162-169 (DB FK) |
| 3 Multi-company / data-scope | `_check_company_domain_parent_of`; record rule `journal_comp_rule` parent_of company_ids; company change guarded. | aj:52; sec:146-150; aj:597-604 |
| 4 Side effects & cross-module triggers | Payment method lines, bank account creation, alias model account.move; hr_expense, sale, purchase, stock_account add journal ACL rows. | aj:723; aj:821-823; csv:54-59 |
| 5 Configuration & optionality | Per-journal currency, custom sequence regex, dedicated refund/payment sequences, self-billing, hash restriction. | aj:145-203 |
| 6 Validation & constraints | See D3 guards; default account domain by type. | aj:81-93 |
| 7 Roles & permissions | Manager CRUD; invoicing/readonly read; plus rows from other modules. | csv:54-59 |
| 8 Scheduled/automated behavior | Dashboard indicators (has_sequence_holes, has_unhashed_entries) computed on demand. | ajd:150-206 |
| 9 Exception & failure behavior | `_build_no_journal_error_msg` UserError when no journal of valid type; ValidationError on constraints. | am:934-936; aj:610; aj:687 |
| 10 Accounting, stock, audit, security & compliance | Journal type drives valid accounts and numbering; hash flag change guarded; journals tracked via mail.thread. | aj:42-53; aj:786-793 |

### DB reconciliation (configuration only)

Restored DB: 7 journals (sale INV, purchase BILL, bank BNK1, general MISC/EXCH/CABA/STJ), all active, `refund_sequence` true for INV and BILL, `restrict_mode_hash_table` NULL, `account_move_journal_id_fkey` ON DELETE RESTRICT, unique (company_id, code).

### Unknown / Runtime list

- RT: delete behaviour of journals with only bank statements; scheduled entries due after archive.

## CAP-U11-09 Audit trail, compliance, roles/ACL/record rules

**Function-ID(s):** RCN-F02 (backdating audit trail; partial: date tracking on the entry and exception audit domain only). Others: FUNCTION MAPPING REQUIRED.

**Claims:** VDR-U11-C344 .. VDR-U11-C384 (41 rows, see claims table)

### D1 Business purpose and process semantics

- Business purpose: provide traceability of accounting changes, protect history from deletion in strict mode, and segregate duties through roles, access rights and record rules.

### D2 Architecture / data / object relationships

- Tracking via `mail.thread` on `account.move`, `account.move.line` (logged onto the move), `account.journal`, `res.company` lock/audit fields; `mail.message` and `mail.tracking.value` guards (account overrides); company `restrictive_audit_trail`; groups (10 in account), ACL rows (125), record rules (31).

### D3 Source / technical / workflow logic

- Deletion/modification rules: entry unlink guards (am:4048-4088), line guards (aml:1959-1989), audit messages protected for restricted records (mm:13-30, 180-199; mtv:9-15).
- Logging of line changes onto the entry (aml:1797-1810, 1927-1937, 2006-2019) only for entries posted at least once; unlink logger message (am:4023-4046).
- Reviewed flag (`checked`): compute (am:2431-2434), write guards (am:3918-3921), `set_moves_checked` (am:6265-6267).

### Ten-dimension table

| # / Dimension | Finding | Key pointers |
|---|---|---|
| 1 Happy path | Posting an entry logs state/number/date changes; changes to posted lines are logged on the entry; audit view lists notification messages. | am:109-142; aml:1797-1937; am:335-343 |
| 2 Reversal / cancel / negative path | With restrictive audit trail, posted-once entries cannot be deleted (cancel instead); deletion logging for force-delete override. | am:4068-4077; am:4023-4046 |
| 3 Multi-company / data-scope | Global company record rules on entries/lines (`company_id in company_ids`) and journals (`parent_of`); portal rule; sale/purchase/hr_expense add narrower rules. | sec:128-150; sec:247-259 |
| 4 Side effects & cross-module triggers | Audit messages for partners, taxes, accounts and company are protected through `DOMAINS`. | mm:13-30 |
| 5 Configuration & optionality | `restrictive_audit_trail` company flag (NULL in DB), `force_restrictive_audit_trail` (False in Community), integrity hash, reviewed flag. | co:258-266; co:347-349 |
| 6 Validation & constraints | Cannot disable audit trail if forced; cannot delete restricted logs; force_delete context bypass. | co:319-323; mm:180-188 |
| 7 Roles & permissions | Declared: 10 groups; ACL rows for move/line/journal/lock exception/wizards; rules: company, invoicing see-all, readonly read-only, portal; DB counts equal declared counts (125 ACL, 31 rules, 10 groups). | sec:40-105; csv:18-19,35-42,54-59,119-125; sec:128-297 |
| 8 Scheduled/automated behavior | None specific; dashboard indicators only. | ajd:150-206 |
| 9 Exception & failure behavior | UserError on restricted deletion; AccessError on review right; `force_delete`/`bypass_audit` tokens exist. | mm:188; am:3919; am:4070 |
| 10 Accounting, stock, audit, security & compliance | Hash integrity report restricted to full accounting group; no read-access log in account (absence by grep). | co:1005-1096; n/a |

### DB reconciliation (configuration only)

Restored DB: account module declares 10 groups (all 10 present), ACL rows 125 (CSV 125 data rows), record rules 31 (declared 31). Other-module rows on `account.move`/`account.move.line`/`account.journal`: sale (Personal/All Invoices rules; salesman ACL), purchase (Purchase User Account Move rule; ACLs), hr_expense (Team Approver). `res_company` ACL: `group_erp_manager` full, others read. `restrictive_audit_trail` NULL; 17 tracked fields on `account.move`.

### Unknown / Runtime list

- RT: effective visibility when several record rules apply to one user (sale/purchase + invoicing see-all).
- UNKNOWN — EVIDENCE INSUFFICIENT: read-access logging (none found in account).

## CAP-U11-10 Multi-company / data-scope and cross-module triggers into entry creation

**Function-ID(s):** FUNCTION MAPPING REQUIRED (existing MCT-F02 'Inter-company transaction automation' relates to the intercompany clearing leg but its source scope is another unit).

**Claims:** VDR-U11-C385 .. VDR-U11-C420 (36 rows, see claims table)

### D1 Business purpose and process semantics

- Business purpose: keep ledgers isolated per company (with branch inheritance) and keep operational documents (sales, purchasing, stock, expenses, manufacturing, payments, bank statements) in step with accounting by creating entries automatically.

### D2 Architecture / data / object relationships

- `account.move.company_id` (stored, computed from journal/branch), `_check_company_auto`, record rules, journal parent_of domain, account company_ids; creation callers: see claims (sale, purchase, hr_expense, stock_account, mrp_account, account_payment, bank statement line, reconciliation exchange diff, accrued orders wizard, automatic entries wizard, company opening entry, mail alias, upload).

### D3 Source / technical / workflow logic

- Company resolution: `_compute_company_id` (am:891-895) and `_inverse_company_id` (am:2607-2616). Account/company check at post (am:5673-5679). Intercompany: `account_payment_interco._post` (interco:30-37) -> `_check_interco_clearing` (interco:39-80, 94-100).
- Caller list (grep of `account.move` creation in installed Community modules; may be incomplete): sale (saleorder:1550, saleadv:180), purchase (po:811, pbl:155), hr_expense (hrexpm:1572, hrpw:56), stock_account (stockmove:209, stockco:76), mrp_account (mrpprod:125, mrpwip:126), account (pay:1081, bsl:367-420, aml:3128, aem:408, acc:384, co:950, ajd:952), account_payment_interco (interco:57, 96).

### Ten-dimension table

| # / Dimension | Finding | Key pointers |
|---|---|---|
| 1 Happy path | Sales order invoicing creates a draft customer invoice with sudo; posting numbers it; payments and bank lines create their own entries. | saleorder:1545-1550; pay:1081; bsl:367-420 |
| 2 Reversal / cancel / negative path | Operational documents' cancel paths call button_draft/cancel overrides (sale, stock_account, expenses). | sale:99-118; stockacc:46-60; hrexp:106-112 |
| 3 Multi-company / data-scope | Company defaults from journal/branch, record rules, parent_of for journals and accounts; lock inheritance; intercompany clearing add-on. | am:891-895; sec:128-156; co:617 |
| 4 Side effects & cross-module triggers | Callers list; sudo creation for salespeople/approvers; statement lines auto-posted; stock closing and WIP entries. | see claims |
| 5 Configuration & optionality | Intercompany clearing journal/accounts per company; journals alias; chart of accounts. | interco:8-28 |
| 6 Validation & constraints | All callers pass through the common create/_check_balanced/validation chain. | am:3894-3910 |
| 7 Roles & permissions | Callers use sudo to avoid billing rights; invoicing group otherwise required for post. | saleorder:1547-1550; am:5583 |
| 8 Scheduled/automated behavior | Stock closing cron and cron auto-post create/post entries. | stockco:148; am:6460 |
| 9 Exception & failure behavior | Errors from callers propagate to the originating document (not analysed here). | n/a |
| 10 Accounting, stock, audit, security & compliance | Elevated-mode creation bypasses user ACL; valuation entries tie stock to GL. | stockmove:209-213 |

### DB reconciliation (configuration only)

Restored DB: 1 company (branch/inter-company behaviour cannot be observed); modules sale, purchase, stock_account, mrp_account, hr_expense, account_payment, account_payment_interco installed; no entries.

### Unknown / Runtime list

- RT: multi-company and branch behaviour (needs a multi-company database).
- RT: completeness of the caller list (grep patterns limited to `account.move` creation with direct `create`).

## 2. Cross-cutting findings

### 2.1 DISCOVERED SUPPORTING MODULES (read only as far as needed)

- `base` (res.company ACL: `base/security/ir.model.access.csv:42`).
- Installed Community modules that extend entry lifecycle: `sale`, `sale_expense`, `sale_timesheet`, `purchase`, `purchase_stock`, `stock_account`, `account_edi`, `account_fleet`, `product_email_template`, `account_payment_interco`, `hr_expense`, `mrp_account` (callers/overrides read only for the lines cited in the claims).
- Not installed in the restored DB but read for evidence: `point_of_sale` (`check_move_validity=False` callers; `validate_lock_dates` constraint at `point_of_sale/models/res_company.py:44-62` not read in detail), grep-only mentions in `l10n_my_edi`, `l10n_vn_edi_viettel`, `account_peppol`, `account_update_tax_tags`, `l10n_fr_pos_cert` (not analysed).

### 2.2 Contradictions with prior evidence

- FN-01: hard vs soft posting (`action_post` -> `_post(soft=False)`).
- FN-10: `secure_sequence_number` is legacy; chain keyed by journal + `sequence_prefix` + `sequence_number`.
- FN-14: auto-post bill-date requirement is limited to vendor documents.

### 2.3 Runtime (RT) list

1. Posting-wizard behaviour for mixed future/hash selections; cancellation vs number reservation.
2. Numbering under concurrency; exact starting pattern for the configured fiscal year and country.
3. Lock-date user interface in Community; lock shift of the accounting date for sale vs purchase documents and its effect on sequences/hash.
4. Reversal reconciliation for multi-currency and cash-basis entries; wizard behaviour with multi-selection.
5. Cron failure handling for non-UserError exceptions; scheduler commit semantics; time-zone selection of 'today'.
6. Multi-company/branch behaviour of record rules, locks and intercompany clearing.
7. Sales/purchase/hr_expense record-rule combinations with the invoicing see-all rule.


### 2.4 Not covered / honest partials

- Not read in detail (UNKNOWN — EVIDENCE INSUFFICIENT): tax-line synchronisation (am:3287-3589, U13), amount/residual computation (am:1165-1231, U12), abnormal-invoice warnings (am:2251-2360), duplicate-reference detection (am:2085-2200), quick-edit mode helpers (am:2063-2080, 4462-4586), adjusting entries, invoice sending/e-invoicing (am:6851-6990 and `account_move_send`), portal/QR/PDF helpers, automatic entry wizard and accrued-orders internals (only their entry-creation calls were read), journal dashboard beyond lock/hash indicators.
- Function-ID mapping: no Function-ID exists in the 53-ID index for scheduled/recurring posting, journals, line synthesis, or audit/ACL; those capabilities are marked FUNCTION MAPPING REQUIRED.
- The caller list for entry creation (CAP-U11-10) comes from grep of direct `create` calls on `account.move` in installed Community modules and may be incomplete (e.g. creation through `_create_records_from_attachments` or helper methods).
- Lock-date maintenance UI, Enterprise-only features (account_accountant, asset, consolidation) and OEEL/OPL code were not consulted and are not asserted.

## 3. Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U11-C001 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:133 | ('posted', 'Posted') | FACT | always | — | Entry lifecycle state selection has exactly three values draft, posted, cancel; the field is required, read-only in forms, not copied and defaults to draft. | N-U11-001 |
| VDR-U11-C002 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:150 | out_receipt | FACT | always | — | move_type selection has seven values: entry, out_invoice, out_refund, in_invoice, in_refund, out_receipt, in_receipt; default entry, required, read-only. | N-U11-001 |
| VDR-U11-C003 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:57 | invoicing_legacy | FACT | always | — | Payment-state selection holds not_paid, in_payment, paid, partial, reversed, blocked and invoicing_legacy; it is a separate stored computed field from the lifecycle state. | N-U11-002 |
| VDR-U11-C004 | FN-01 | account/models/account_move.py:3895 | already in the posted state | FACT | always | — | create() refuses any vals_list item carrying state 'posted' with a UserError telling users to create a draft and post it afterwards. | N-U11-005 |
| VDR-U11-C005 | FN-01 | account/models/account_move.py:6198 | self._post(soft=False) | FACT | always | CONTRA | action_post calls _post(soft=False), i.e. HARD posting; the prior register FN-01 states action_post calls _post(soft=True). CONTRA with FN-01 (soft is the default parameter of _post and is used by the cron and by callers that do not pass the flag). | N-U11-009 |
| VDR-U11-C006 | FN-01 | account/models/account_move.py:5569 | def _post(self, soft=True) | FACT | always | — | _post signature defaults soft=True; the docstring states that with soft=True future documents are not immediately posted but set to be auto-posted at the accounting date. | N-U11-010 |
| VDR-U11-C007 | FN-01 | account/models/account_move.py:5583 | group_account_invoice | FACT | always | — | _post raises AccessError unless the environment is superuser or the user holds the invoicing group. | N-U11-006 |
| VDR-U11-C008 | FN-01 | account/models/account_move.py:5652 | must be in draft | FACT | always | — | _post validation message set refuses any entry whose state is already posted or cancel. | N-U11-007 |
| VDR-U11-C009 | FN-01 | account/models/account_move.py:5654 | Even magicians | FACT | always | — | _post refuses entries having no line other than line_section, line_subsection or line_note display types. | N-U11-008 |
| VDR-U11-C010 | FN-01 | account/models/account_move.py:5656 | configured to be auto-posted | FACT | always | — | When soft is False, auto_post differs from 'no' and the date is in the future, _post adds a validation message that the move is configured to be auto-posted on that date; this blocks manual posting of scheduled entries. | N-U11-009 |
| VDR-U11-C011 | FN-01 | account/models/account_move.py:5691 | future_moves | FACT | soft posting | — | With soft=True, moves whose date is after today are not posted: auto_post is set to 'at_date' when it was 'no' and a chatter message 'will be posted at the accounting date' is logged. | N-U11-010 |
| VDR-U11-C012 | FN-01 | account/models/account_move.py:5757 | 'posted_before': True | FACT | always | — | Final step of _post writes state posted and posted_before True in one write on the entries to post. | N-U11-003 |
| VDR-U11-C013 | FN-01 | account/models/account_move.py:4004 | self._hash_moves() | FACT | always | — | When write receives state posted the entries are flushed (so the name is computed) and _hash_moves is called; hashing only acts on journals flagged for it (see CAP-U11-03). | N-U11-003 |
| VDR-U11-C014 | FN-01 | account/models/account_move.py:5709 | _create_analytic_lines | FACT | always | — | _post creates analytic lines in batch for all moves to post. | N-U11-003 |
| VDR-U11-C015 | FN-01 | account/models/account_move.py:5779 | customer_count | FACT | always | — | After posting, customer_rank and supplier_rank of the partner and its commercial partner are incremented for sale, purchase and entry receivable or payable lines. | N-U11-014 |
| VDR-U11-C016 | FN-01 | account/models/account_move.py:5797 | _invoice_paid_hook | FACT | always | — | Posted invoices or receipts with a zero total trigger _invoice_paid_hook. | N-U11-014 |
| VDR-U11-C017 | FN-01 | account/models/account_move.py:5726 | draft_reverse_moves | FACT | always | — | Posting a draft reversal whose reversed_entry_id is posted triggers reconciliation back to the original at the end of _post (see CAP-U11-05). | N-U11-015 |
| VDR-U11-C018 | FN-01 | account/models/account_move.py:6180 | def action_post | FACT | always | — | action_post opens the abnormal-invoice confirmation wizard only if context disable_abnormal_invoice_detection is explicitly falsy and some move has an abnormal amount or date warning; the key defaults to True so the wizard is skipped by default. | N-U11-020 |
| VDR-U11-C019 | FN-01 | account/models/account_move.py:6203 | _get_moves_requiring_confirmation | FACT | UI flow | — | action_validate_moves_with_confirmation posts directly the draft moves with lines that are neither future dated nor in a hash journal and opens the 'Confirm Entries' wizard for the rest; raises UserError when no draft entry with lines is selected. | N-U11-019 |
| VDR-U11-C020 | FN-01 | account/wizard/account_validate_account_move.py:75 | moves_to_post._post(not self.force_post) | FACT | wizard validate_move | — | The validate wizard calls _post with soft = not force_post, so unchecked 'Force' keeps future entries scheduled and 'Force' posts them now after setting auto_post to 'no'. | N-U11-019 |
| VDR-U11-C021 | FN-01 | account/wizard/account_validate_account_move.py:72 | moves_to_post = self.move_ids | FACT | wizard validate_move | — | The wizard excludes entries of hash-restricted journals from posting unless force_hash is ticked. | N-U11-019 |
| VDR-U11-C022 | FN-02 | account/models/account_move.py:6270 | Only posted/cancelled journal entries | FACT | always | — | button_draft raises UserError if any selected move is not in state cancel or posted. | N-U11-011 |
| VDR-U11-C023 | FN-02 | account/models/account_move.py:6272 | need_cancel_request | FACT | always | — | button_draft refuses when need_cancel_request is true; the Community hook _need_cancel_request returns False so only a localization can set it. | N-U11-011 |
| VDR-U11-C024 | FN-02 | account/models/account_move.py:6348 | def _check_draftable | FACT | always | — | _check_draftable refuses exchange-difference entries, tax cash basis entries (by rec id or origin move) and any entry with inalterable_hash set. | N-U11-011 |
| VDR-U11-C025 | FN-02 | account/models/account_move.py:6280 | self.state = 'draft' | FACT | always | — | button_draft deletes next draft recurrence, removes analytic lines of the entry, sets state draft, clears sending_data and detaches printable PDF attachments for sale documents. | N-U11-012 |
| VDR-U11-C026 | FN-02 | account/models/account_move.py:6296 | def _detach_attachments | FACT | always | — | Detaching renames the stored invoice PDF attachment adding user and date and clears its res_field so it can be regenerated. | N-U11-012 |
| VDR-U11-C027 | FN-02 | account/models/account_move.py:3953 | post subtract a move | FACT | always | — | write() on a posted move whose new state is not posted runs _check_fiscal_lock_dates and the tax lock check on its lines, so resetting a posted entry to draft inside a lock raises UserError. | N-U11-078 |
| VDR-U11-C028 | FN-02 | account/models/account_move.py:3920 | Validated entries can only be changed | FACT | always | — | write() with state draft on a checked (reviewed) move raises ValidationError unless _is_user_able_to_review; the account-only implementation returns True so no restriction applies in Community. | N-U11-022 |
| VDR-U11-C029 | FN-02 | account/models/account_move.py:7014 | def _is_user_able_to_review | FACT | only account installed | — | _is_user_able_to_review returns True with the comment that access rights are not checked if only account is installed. | N-U11-022 |
| VDR-U11-C030 | FN-03 | account/models/account_move.py:6384 | def button_cancel | FACT | always | — | button_cancel first calls button_draft on posted moves, then raises if any move is not draft. | N-U11-013 |
| VDR-U11-C031 | FN-03 | account/models/account_move.py:6394 | self.line_ids.remove_move_reconcile() | FACT | always | — | button_cancel removes reconciliations, sets payment_ids state to canceled, and writes auto_post 'no' and state 'cancel'. | N-U11-013 |
| VDR-U11-C032 | FN-03 | account/models/account_move.py:955 | if move.state == 'cancel' | FACT | always | — | _compute_name skips cancelled moves, so a cancelled entry never has its number recomputed. | N-U11-025 |
| VDR-U11-C033 | FN-03 | account/models/account_move.py:6392 | Only draft journal entries | FACT | always | — | Error text for cancel from a non-draft state after the draft reset step. | N-U11-013 |
| VDR-U11-C034 | FN-03 | account/models/account_move.py:1962 | show_reset_to_draft_button | FACT | UI | — | Reset-to-draft button shows for cancelled entries and for posted entries without cancel request, only if the journal is not hash restricted and the entry has no inalterable hash. | N-U11-011 |
| VDR-U11-C035 | FN-03 | account/models/account_move.py:884 | hide_post_button | FACT | UI | — | The Post button is hidden unless the entry is draft and not (auto_post set and dated in the future). | N-U11-009 |
| VDR-U11-C036 | FN-01 | account/models/account_move.py:5551 | def _unlink_or_reverse | FACT | always | — | _unlink_or_reverse chooses per move: reverse (cancel=True) if _can_be_unlinked is false, cancel if audit-trail protected, else button_draft then unlink; grep found no caller in Community modules. | N-U11-112 |
| VDR-U11-C037 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:606 | PAYMENT_STATE | FACT | always | — | payment_state is stored computed, read-only, tracked and depends on amount_residual, move_type, state, company and reconciled payment state. | N-U11-016 |
| VDR-U11-C038 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1233 | _invoice_qualifies | FACT | always | — | Only invoices or receipts that are posted, or draft with a non-zero total, are evaluated; legacy and blocked states are preserved; all other entries get not_paid. | N-U11-018 |
| VDR-U11-C039 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1295 | currency.is_zero(invoice.amount_residual) | FACT | always | — | Zero residual leads to paid or in_payment (when linked payments are not all matched), or reversed when the only counterpart moves are refunds or entries. | N-U11-016 |
| VDR-U11-C040 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1322 | new_pmt_state = 'partial' | FACT | always | — | A non-zero residual with reconciliation parts gives partial; draft or posted with matched in-process payment lines gives in_payment or paid via _get_invoice_in_payment_state. | N-U11-016 |
| VDR-U11-C041 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6398 | def action_toggle_block_payment | FACT | always | — | Blocking toggles payment_state between not_paid and blocked and raises if the invoice is paid or in_payment. | N-U11-017 |
| VDR-U11-C042 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1328 | status_in_payment | FACT | always | — | status_in_payment is a non-stored display state merging state, payment_state and is_move_sent (sent). | N-U11-016 |
| VDR-U11-C043 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:120 | Auto-reconcile the invoice | FACT | sale installed | — | sale overrides _post to reconcile posted invoices with payments from linked transactions in state in_process or paid. | N-U11-021 |
| VDR-U11-C044 | FUNCTION MAPPING REQUIRED | stock_account/models/account_move.py:33 | move_reverse_cancel | FACT | stock_account installed | — | stock_account _post creates COGS (display_type cogs) lines before posting, except for reversal moves posted with move_reverse_cancel, and sets stock move values afterwards. | N-U11-021 |
| VDR-U11-C045 | FUNCTION MAPPING REQUIRED | stock_account/models/account_move.py:46 | def button_draft | FACT | stock_account installed | — | stock_account button_draft and button_cancel unlink the COGS lines created at post. | N-U11-021 |
| VDR-U11-C046 | FUNCTION MAPPING REQUIRED | purchase_stock/models/account_invoice.py:113 | def _post | FACT | purchase_stock installed | — | purchase_stock _post creates anglo-saxon lines for vendor documents unless the move is a cancelling reversal. | N-U11-021 |
| VDR-U11-C047 | FUNCTION MAPPING REQUIRED | account_edi/models/account_move.py:233 | def _post | FACT | account_edi installed | — | account_edi _post creates account.edi.document records in state to_send for each journal edi format that applies, raises UserError on configuration errors, and triggers the EDI cron. | N-U11-021 |
| VDR-U11-C048 | FUNCTION MAPPING REQUIRED | account_edi/models/account_move.py:291 | def button_draft | FACT | account_edi installed | — | account_edi button_draft refuses when an EDI document was already sent and deletes pending to_send documents; button_cancel marks documents cancelled or to_cancel. | N-U11-021 |
| VDR-U11-C049 | FUNCTION MAPPING REQUIRED | account_fleet/models/account_move.py:9 | def _post | FACT | account_fleet installed | — | account_fleet _post creates fleet service logs for posted vendor-bill product lines having a vehicle. | N-U11-021 |
| VDR-U11-C050 | FUNCTION MAPPING REQUIRED | product_email_template/models/account_move.py:25 | def _post | FACT | product_email_template installed | — | product_email_template _post sends product-specific validation e-mails after posting. | N-U11-021 |
| VDR-U11-C051 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/account_move.py:30 | def _post | FACT | account_payment_interco installed | — | account_payment_interco _post checks pending payments of other companies for the posted invoice and creates intercompany clearing entries. | N-U11-186 |
| VDR-U11-C052 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:99 | def button_draft | FACT | sale installed | — | sale button_draft and button_cancel recompute down-payment line descriptions and prices on the linked sale order lines. | N-U11-021 |
| VDR-U11-C053 | FUNCTION MAPPING REQUIRED | sale_expense/models/account_move.py:14 | def button_draft | FACT | sale_expense installed | — | sale_expense button_draft, _reverse_moves and unlink reset sale order line quantities of linked expenses. | N-U11-106 |
| VDR-U11-C054 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:106 | def button_cancel | FACT | hr_expense installed | — | hr_expense button_cancel clears the expense link from the cancelled move so expenses can be reimbursed again. | N-U11-021 |
| VDR-U11-C055 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/account_move.py:99 | def action_post | FACT | sale_timesheet installed | — | sale_timesheet action_post releases timesheet invoice links for credit notes that reverse an invoice. | N-U11-106 |
| VDR-U11-C056 | FN-01 | account/models/account_move.py:5571 | give it a number | INFERENCE | always | — | The _post docstring (am:5570-5576) describes posting as giving the document a number, checking completeness and, for hashed journals, making some fields unchangeable afterwards; INFERENCE of purpose: separation of draft preparation from validated ledger impact. | N-U11-004 |
| VDR-U11-C057 | FN-01 | account/models/account_move.py:5699 | to_post = self | INFERENCE | always | — | With soft False (manual post) all selected moves are posted regardless of date unless the auto_post validation at am:5656 applies; an unflagged future-dated entry is therefore posted immediately (am:5699-5700). | N-U11-023 |
| VDR-U11-C058 | FN-03 | account/models/account_move.py:6394 | self.line_ids.remove_move_reconcile() | INFERENCE | always | — | button_cancel removes reconciliations of the cancelled entry's lines and button_draft (called first for posted entries) deletes analytic lines; downstream matching of payments or statement lines is undone without a separate confirmation in this code path. | N-U11-024 |
| VDR-U11-C059 | FN-04 | account/models/account_move.py:2781 | def _check_balanced | FACT | always | — | _check_balanced is a context manager wrapped around create, write and unlink; after the body it raises unless balanced. | N-U11-028 |
| VDR-U11-C060 | FN-04 | account/models/account_move.py:2793 | The entry is not balanced | FACT | always | — | A single unbalanced entry raises UserError 'The entry is not balanced.' without naming the entry. | N-U11-028 |
| VDR-U11-C061 | FN-04 | account/models/account_move.py:2795 | following entries are unbalanced | FACT | several entries | — | With several unbalanced entries the UserError lists each by name. | N-U11-028 |
| VDR-U11-C062 | FN-04 | account/models/account_move.py:3898 | with self._check_balanced(container) | FACT | always | — | account.move create wraps the whole creation in _check_balanced. | N-U11-029 |
| VDR-U11-C063 | FN-04 | account/models/account_move.py:3981 | self._check_balanced(container) | FACT | always | — | account.move write wraps the write in _check_balanced for the moves and the moves whose lines are stolen via link commands. | N-U11-029 |
| VDR-U11-C064 | FN-04 | account/models/account_move_line.py:1785 | moves._check_balanced(move_container) | FACT | always | — | account.move.line create is wrapped in the move's _check_balanced. | N-U11-029 |
| VDR-U11-C065 | FN-04 | account/models/account_move_line.py:1891 | self.move_id._check_balanced(move_container) | FACT | always | — | account.move.line write is wrapped in the move's _check_balanced. | N-U11-029 |
| VDR-U11-C066 | FN-04 | account/models/account_move_line.py:2022 | self.move_id._check_balanced(move_container) | FACT | always | — | account.move.line unlink is wrapped in the move's _check_balanced. | N-U11-029 |
| VDR-U11-C067 | FN-06 | account/models/account_move.py:2801 | def _get_unbalanced_moves | FACT | always | — | _get_unbalanced_moves returns moves with lines whose rounded SUM(balance) is non-zero in company currency decimal places, using direct SQL after flushing debit, credit, balance, currency_id and move_id. | N-U11-028 |
| VDR-U11-C068 | FN-06 | account/models/account_move.py:2806 | MUST NOT depend on computed | FACT | always | — | Source comment: query must not depend on computed stored fields because the ORM calls create with no_recompute. | N-U11-047 |
| VDR-U11-C069 | FN-05 | account/models/account_move.py:2786 | 'check_move_validity', default=True, target=False | FACT | always | — | Balance assertion is suppressed when the recursion stack or context key check_move_validity is False (default True); the context manager returns without running the check. | N-U11-042 |
| VDR-U11-C070 | FN-05 | account/models/account_move.py:7052 | def _disable_recursion | FACT | always | — | _disable_recursion stores a StackMap in cr.cache and compares the current value to target; the container argument is deprecated. | N-U11-042 |
| VDR-U11-C071 | FN-05 | point_of_sale/models/pos_session.py:442 | check_move_validity=False | FACT | point_of_sale installed (NOT installed in DB) | — | The only non-test Community callers that set check_move_validity=False are in point_of_sale pos_session (lines 442 and 1051); point_of_sale is not installed in the restored DB. | N-U11-046 |
| VDR-U11-C072 | FN-04 | account/models/account_move.py:3204 | def _sync_unbalanced_lines | FACT | always | — | For non-posted moves that had or have tax lines in play, _sync_unbalanced_lines creates or updates a line named 'Automatic Balancing Line' to make entries saveable. | N-U11-030 |
| VDR-U11-C073 | FN-04 | account/models/account_move.py:3197 | _get_automatic_balancing_account | FACT | always | — | Automatic balancing uses the journal default account or the company suspense account. | N-U11-030 |
| VDR-U11-C074 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:483 | _check_credit_debit | FACT | always | — | DB constraint check_credit_debit: for non-section lines credit * debit must be 0. | N-U11-031 |
| VDR-U11-C075 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:487 | _check_amount_currency_balance_sign | FACT | always | — | DB constraint check_amount_currency_balance_sign: amount_currency and balance must have the same sign for accountable lines. | N-U11-031 |
| VDR-U11-C076 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:491 | _check_accountable_required_fields | FACT | always | — | DB constraint: accountable lines must have account_id. | N-U11-031 |
| VDR-U11-C077 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:495 | _check_non_accountable_fields_null | FACT | always | — | DB constraint: section, subsection and note lines must have zero amounts and no account. | N-U11-031 |
| VDR-U11-C078 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:483 | CHECK(display_type IN | OBSERVATION | restored DB | — | Restored DB has the four check constraints on account_move_line (check_credit_debit, check_amount_currency_balance_sign, check_accountable_required_fields, check_non_accountable_fields_null) with the same definitions as the source. | N-U11-045 |
| VDR-U11-C079 | FN-11 | account/models/account_move.py:2849 | def _check_journal_move_type | FACT | always | — | Constraint on journal_id and move_type: purchase documents including receipts must be in a purchase journal, sale documents including receipts in a sale journal; ValidationError otherwise. | N-U11-032 |
| VDR-U11-C080 | FN-12 | account/models/account_move.py:2857 | def _validate_taxes_country | FACT | always | — | Constraint on line_ids, fiscal_position_id, company_id: tax countries on lines must equal tax_country_id; two distinct ValidationErrors for fiscal position and fiscal country mismatches (detail: taxation capability). | N-U11-033 |
| VDR-U11-C081 | FN-13 | account/models/account_move.py:2872 | def _check_invoice_currency_rate | FACT | always | — | Constraint: invoice-type moves in a currency different from the company currency must have invoice_currency_rate > 0. | N-U11-034 |
| VDR-U11-C082 | FN-14 | account/models/account_move.py:2842 | def _require_bill_date_for_autopost | FACT | always | CONTRA | Constraint requires invoice_date only when auto_post != 'no' AND is_purchase_document() (in_invoice, in_refund; receipts excluded because include_receipts defaults False). The prior FN-14 states a generic date requirement for auto-post; narrowed here. | N-U11-035 |
| VDR-U11-C083 | FN-01 | account/models/account_move.py:5624 | negative total amount | FACT | always | — | _post refuses invoices with negative amount_total and tells users to create a credit note. | N-U11-036 |
| VDR-U11-C084 | FN-01 | account/models/account_move.py:5631 | if not invoice.partner_id | FACT | always | — | _post requires partner on sale and purchase documents with distinct messages. | N-U11-036 |
| VDR-U11-C085 | FN-01 | account/models/account_move.py:5642 | if not invoice.invoice_date | FACT | always | — | Sale documents without invoice_date get today's date at post (keeping a manual rate); purchase documents without date raise 'Bill/Refund date is required'. | N-U11-036 |
| VDR-U11-C086 | FN-01 | account/models/account_move.py:5603 | bank account linked to this invoice | FACT | always | — | _post refuses invoices whose partner_bank_id is archived. | N-U11-037 |
| VDR-U11-C087 | FN-01 | account/models/account_move.py:5608 | allow_out_payment | FACT | always | — | Inbound invoices whose bank account is not trusted: superuser, public or portal flows silently clear the bank account; other users get RedirectWarning (if they can trust) or UserError. | N-U11-037 |
| VDR-U11-C088 | FN-01 | account/models/account_move.py:5592 | quick_edit_total_amount | FACT | quick edit mode | — | In quick-edit mode a posted invoice's total must equal the typed expected total. | N-U11-043 |
| VDR-U11-C089 | FN-01 | account/models/account_move.py:5659 | archived journal | FACT | always | — | _post refuses entries in an archived journal. | N-U11-037 |
| VDR-U11-C090 | FN-01 | account/models/account_move.py:5664 | inactive currency | FACT | always | — | _post refuses documents with an inactive currency. | N-U11-037 |
| VDR-U11-C091 | FN-01 | account/models/account_move.py:5670 | archived account | FACT | skip_account_deprecation_check unset | — | _post refuses lines with archived accounts unless context skip_account_deprecation_check is set. | N-U11-037 |
| VDR-U11-C092 | FN-01 | account/models/account_move.py:5673 | mismatched_accounts | FACT | always | — | _post refuses lines using accounts that do not belong to the entry company or its parents. | N-U11-184 |
| VDR-U11-C093 | FN-01 | account/models/account_move.py:5685 | archived analytic account | FACT | always | — | _post raises UserError for archived analytic accounts in line distributions (outside the message set). | N-U11-037 |
| VDR-U11-C094 | FN-01 | account/models/account_move.py:5681 | if validation_msgs | FACT | always | — | Validation messages are accumulated in a set and raised together as one UserError. | N-U11-038 |
| VDR-U11-C095 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1478 | def _check_constrains_account_id_journal_id | FACT | always | — | Called at post and after account, currency or journal writes: refuses archived accounts (unless imported or skip flag) and accounts whose forced currency differs from both company and line currency. | N-U11-037 |
| VDR-U11-C096 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1496 | def _check_off_balance | FACT | always | — | Constraint: off-balance accounts cannot mix with other account types, cannot carry taxes and cannot be reconciled. | N-U11-039 |
| VDR-U11-C097 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1507 | def _check_payable_receivable | FACT | always | — | Constraint: sale documents cannot use payable accounts, purchase documents cannot use receivable accounts, and payment_term display type must coincide with receivable (sale) or payable (purchase) account. | N-U11-039 |
| VDR-U11-C098 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:791 | _unique_name | FACT | always | — | Unique index on (name, journal_id) where state posted and name != '/' with message 'Another entry with the same name already exists.' | N-U11-040 |
| VDR-U11-C099 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:791 | _unique_name | OBSERVATION | restored DB | — | Restored DB has unique partial index account_move_unique_name on (name, journal_id) WHERE state posted AND name != '/'. | N-U11-040 |
| VDR-U11-C100 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3945 | can't change the date or name | FACT | always | — | write() on a posted move changing name or date runs the fiscal lock check and the tax lock check on its lines. | N-U11-041 |
| VDR-U11-C101 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3960 | unmodifiable_fields | FACT | skip_readonly_check unset | — | write() on a posted move refuses invoice_line_ids, line_ids, invoice_date, date, partner_id, invoice_payment_term_id, currency_id, fiscal_position_id, invoice_cash_rounding_id unless context skip_readonly_check. | N-U11-041 |
| VDR-U11-C102 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:298 | At Date | FACT | always | — | auto_post selection: no, at_date, monthly, quarterly, yearly; required, default no, not copied. | N-U11-120 |
| VDR-U11-C103 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:878 | def _compute_auto_post_until | FACT | always | — | auto_post_until is cleared when auto_post is 'no' or 'at_date'. | N-U11-120 |
| VDR-U11-C104 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3930 | posted_before | FACT | always | — | write() forbids changing journal of a posted-once move unless name is cleared or '/'; a second guard blocks journal change when name is real and sequence_number is not 0 or 1 (not in quick-edit mode). | N-U11-058 |
| VDR-U11-C105 | FN-01 | account/models/account_move.py:5650 | for move in self: | INFERENCE | always | — | The posting checks are layered: per-invoice checks (am:5591-5648), per-move checks (am:5650-5679), one raised message set (am:5681-5683), the analytic check (am:5685-5689), plus constraints on create/write and DB checks; INFERENCE of the three layers described in D1. | N-U11-026 |
| VDR-U11-C106 | FN-12 | account/models/account_move.py:2861 | inconsistencies in the reports | INFERENCE | always | — | The docstring of _validate_taxes_country states the constraint exists because incoherent taxes could generate inconsistencies in the reports; INFERENCE of the purpose of coherence checks. | N-U11-027 |
| VDR-U11-C107 | FN-12 | account/models/account_move.py:2863 | _compute_tax_country_id | FACT | always | — | The tax-country constraint depends on tax_country_id which is derived from the fiscal position's country when foreign VAT is set, otherwise the company's fiscal country (am:1943-1950); owned by U13. | N-U11-044 |
| VDR-U11-C108 | FN-04 | n/a | n/a | UNKNOWN | n/a | RT | Concurrent-edit and multi-currency edge cases of the balance check and the automatic balancing line were not executed; resolve with a runtime test using two sessions and a foreign-currency tax invoice. | N-U11-048 |
| VDR-U11-C109 | FN-09 | account/models/account_move.py:109 | compute='_compute_name' | FACT | always | — | Number field name is stored, computed, writable, not copied, tracked, trigram indexed. | N-U11-049 |
| VDR-U11-C110 | FN-09 | account/models/account_move.py:80 | _sequence_index = "journal_id" | FACT | always | — | The sequence mixin is indexed per journal_id, meaning numbering chains are per journal. | N-U11-052 |
| VDR-U11-C111 | FN-09 | account/models/account_move.py:84 | _sequence_monthly_regex | FACT | always | — | All five sequence regex properties return journal.sequence_override_regex when set, else the mixin default. | N-U11-068 |
| VDR-U11-C112 | FN-09 | account/models/account_move.py:952 | def _compute_name | FACT | always | — | _compute_name sorts by date, reference and origin id; unposted moves whose name does not match their date have the name reset; a name is assigned with _set_next_sequence only when the move has a date, no real name and state is not draft. | N-U11-051 |
| VDR-U11-C113 | FN-09 | account/models/account_move.py:971 | def _compute_name_placeholder | FACT | always | — | name_placeholder shows the next candidate number for a draft without name (last sequence plus one). | N-U11-051 |
| VDR-U11-C114 | FN-09 | account/models/account_move.py:4201 | def _get_last_sequence_domain | FACT | always | — | Last-sequence domain limits to journal, name != '/', date range of the detected reset period, and splits refund (when refund_sequence), payment (when payment_sequence) and per-partner (self-billing) chains. | N-U11-054 |
| VDR-U11-C115 | FN-09 | account/models/account_move.py:4224 | reference_move_name | FACT | always | — | The reset kind is deduced from the latest move with date <= current date in the same journal, else the oldest move. | N-U11-052 |
| VDR-U11-C116 | FN-09 | account/models/account_move.py:4273 | def _get_starting_sequence | FACT | always | — | Starting pattern: journal code / year part / '00000' for sale, bank, cash, credit journals; code / year / month / '0000' otherwise; staggered fiscal years use a 'YY-YY' year part and four digits. | N-U11-053 |
| VDR-U11-C117 | FN-09 | account/models/account_move.py:4307 | starting_sequence = "R" | FACT | always | — | Prefix R is added for refund types when the journal has refund_sequence; prefix P for payments when payment_sequence. | N-U11-054 |
| VDR-U11-C118 | FN-09 | account/models/account_move.py:4313 | def _get_sequence_date_range | FACT | always | — | Year-range resets use the fiscal year bounds of the company; year_range_month truncates the month at the fiscal year end day. | N-U11-052 |
| VDR-U11-C119 | FN-09 | account/models/sequence_mixin.py:41 | _sequence_year_range_monthly_regex | FACT | always | — | The mixin defines five regex families: year-range-monthly, monthly, year-range, yearly and fixed. | N-U11-052 |
| VDR-U11-C120 | FN-09 | account/models/sequence_mixin.py:193 | def _deduce_sequence_number_reset | FACT | always | — | _deduce_sequence_number_reset returns year_range_month, month, year_range, year or never by matching the regexes in that order and raises ValidationError if no seq group exists. | N-U11-052 |
| VDR-U11-C121 | FN-09 | account/models/sequence_mixin.py:355 | def _locked_increment | FACT | always | — | _locked_increment locks the candidate number by updating the row covered by a unique index inside a savepoint and retries with the next number on UniqueViolation; subsequent numbers come from a transaction cache. | N-U11-055 |
| VDR-U11-C122 | FN-09 | account/models/sequence_mixin.py:422 | pgerrors.UniqueViolation | FACT | always | — | Retry loop catches ExclusionViolation and UniqueViolation, rolls back to the savepoint and increments. | N-U11-055 |
| VDR-U11-C123 | FN-09 | account/models/sequence_mixin.py:449 | def _get_next_sequence_format | FACT | always | — | When no last sequence is found in the period, the format is taken from a relaxed search or the starting sequence with seq 0, year and month set from the entry date. | N-U11-052 |
| VDR-U11-C124 | FN-09 | account/models/sequence_mixin.py:156 | def _constrains_date_sequence | FACT | always | — | Constraint on name and date: a posted entry's date must match the year and month embedded in its number (using the reset kind); error tells the user to clear the number or use resequence. | N-U11-056 |
| VDR-U11-C125 | FN-09 | account/models/sequence_mixin.py:160 | sequence.mixin.constraint_start_date | FACT | always | — | Constraint is skipped for dates up to config parameter sequence.mixin.constraint_start_date (default 1970-01-01). | N-U11-070 |
| VDR-U11-C126 | FN-09 | account/models/account_move.py:4197 | def _must_check_constrains_date_sequence | FACT | always | — | For account.move the date-sequence constraint applies only to posted moves not in quick-edit mode. | N-U11-056 |
| VDR-U11-C127 | FN-09 | account/models/account_move.py:5820 | def _update_sequence_made_gap | FACT | always | — | made_sequence_gap flags the entry that breaks consecutive numbering within journal and prefix, recomputed for previous, current and next entries. | N-U11-060 |
| VDR-U11-C128 | FN-09 | account/models/account_move.py:3976 | _update_sequence_made_gap(invalidate_current=True) | FACT | always | — | write() of sequence_prefix, sequence_number, journal_id or name triggers the gap update; unlink also does at line 4080. | N-U11-060 |
| VDR-U11-C129 | FN-09 | account/models/account_move.py:4048 | def _unlink_forbid_parts_of_chain | FACT | always | — | Deleting a numbered move is allowed only for account managers, fiduciary-mode companies, force_delete context, or when the move is the last of its chain; otherwise UserError advising to reverse. | N-U11-059 |
| VDR-U11-C130 | FN-09 | account/models/account_move.py:4020 | def check_move_sequence_chain | FACT | always | — | check_move_sequence_chain uses _is_end_of_seq_chain over named moves. | N-U11-059 |
| VDR-U11-C131 | FN-09 | account/models/sequence_mixin.py:487 | def _is_end_of_seq_chain | FACT | always | — | A group of moves is at the end of the chain if their numbers are contiguous and the highest equals last sequence plus one. | N-U11-059 |
| VDR-U11-C132 | FN-09 | account/models/account_move.py:3971 | sequence_override_regex | FACT | always | — | write() with a name not matching the journal's override regex raises UserError for non-managers; for managers the override regex is cleared. | N-U11-068 |
| VDR-U11-C133 | FN-09 | account/models/account_move.py:2694 | def _onchange_name_warning | FACT | UI | — | Editing a number to a lower value than the highest name shows a warning flag; changing the detected format shows a message explaining the reset behaviour. | N-U11-052 |
| VDR-U11-C134 | FN-10 | account/models/account_move.py:354 | secure_sequence_number | FACT | always | CONTRA | secure_sequence_number remains declared (read-only, copy False, indexed) but within account the only reader is the legacy integrity report (company.py:1025 and 1051); the current post/hash path never writes it. CONTRA with prior FN-10 which presents it as the live gapless counter. | N-U11-071 |
| VDR-U11-C135 | FN-10 | account/models/company.py:1025 | secure_sequence_number ASC NULLS LAST | FACT | always | CONTRA | _check_hash_integrity orders hashed moves by secure_sequence_number NULLS LAST, then sequence_prefix and sequence_number, and uses it only to choose the previous-hash reference for legacy entries. | N-U11-071 |
| VDR-U11-C136 | FN-10 | account/models/account_move.py:1001 | def _compute_secured | FACT | always | — | secured is computed as bool(inalterable_hash) and is searchable. | N-U11-067 |
| VDR-U11-C137 | FN-10 | account/models/account_journal.py:145 | restrict_mode_hash_table | FACT | always | — | Journal field restrict_mode_hash_table 'Secure Posted Entries with Hash': posting retroactively hashes all moves from the posted one back to the last hashed entry; hashing can also be done on demand with the Secure Entries wizard. | N-U11-061 |
| VDR-U11-C138 | FN-10 | account/models/account_move.py:4592 | def _get_integrity_hash_fields | FACT | always | — | Hash fields per version: v1 date, journal_id, company_id; v2 to v4 add name; line fields v1 debit, credit, account_id, partner_id and v2 to v4 add name (aml:3394). | N-U11-061 |
| VDR-U11-C139 | FN-10 | account/models/account_move.py:47 | MAX_HASH_VERSION = 4 | FACT | always | — | Current hash version is 4. | N-U11-061 |
| VDR-U11-C140 | FN-10 | account/models/account_move.py:4771 | def _calculate_hashes | FACT | always | — | Hash = SHA-256 over previous hash concatenated with sorted JSON of the integrity fields of move and lines; v4 stores '$4$' prefix; monetary values are formatted with currency decimals from v3. | N-U11-061 |
| VDR-U11-C141 | FN-10 | account/models/account_move.py:4741 | grouped('sequence_prefix') | FACT | always | — | Chains are built per journal and per sequence_prefix. | N-U11-061 |
| VDR-U11-C142 | FN-10 | account/models/account_move.py:4681 | include_pre_last_hash | FACT | always | — | Only moves with sequence number above the last hashed move are hashed unless include_pre_last_hash. | N-U11-061 |
| VDR-U11-C143 | FN-10 | account/models/account_move.py:4761 | gap has been detected | FACT | raise_if_gap | — | Hashing raises UserError when the moves to hash contain a gap; unreconciled bank statement lines raise 'All entries have to be reconciled'; nothing to hash raises 'could not be locked'. | N-U11-062 |
| VDR-U11-C144 | FN-10 | account/models/account_move.py:4625 | def _hash_moves | FACT | always | — | _hash_moves writes inalterable_hash with sudo, logs 'This journal entry has been secured.' per move, and activates the account_secured group when any chain belongs to a journal without hash-on-post. | N-U11-064 |
| VDR-U11-C145 | FN-10 | account/models/account_move.py:6375 | def button_hash | FACT | manual | — | button_hash hashes with force_hash=True (independent of journal setting). | N-U11-064 |
| VDR-U11-C146 | FN-10 | account/wizard/account_secure_entries_wizard.py:269 | force_hash=True, raise_if_gap=False | FACT | secure wizard | — | Secure Entries wizard hashes the computed move_to_hash_ids with force_hash=True and raise_if_gap=False; gaps are only warned. | N-U11-064 |
| VDR-U11-C147 | FN-10 | account/models/account_move.py:3923 | violated_fields | FACT | always | — | write() on a hashed move refuses writes to integrity fields (name, date, journal_id, company_id) and to inalterable_hash with UserError listing the field labels. | N-U11-063 |
| VDR-U11-C148 | FN-10 | account/models/account_move_line.py:1827 | inalterable_fields | FACT | always | — | Line write on a hashed move refuses name, debit, credit, account_id, partner_id and inalterable_hash. | N-U11-063 |
| VDR-U11-C149 | FN-10 | account/models/account_move_line.py:1982 | _except_hashed_entry_lines | FACT | always | — | Deleting lines of a hashed move raises UserError. | N-U11-063 |
| VDR-U11-C150 | FN-10 | account/models/account_move.py:6372 | reset to draft a locked | FACT | always | — | _check_draftable refuses entries with inalterable_hash. | N-U11-063 |
| VDR-U11-C151 | FN-10 | account/models/account_move.py:5546 | not self.inalterable_hash | FACT | always | — | _can_be_unlinked requires no hash, date after lock date and not a posted caba or exchange-diff entry. | N-U11-063 |
| VDR-U11-C152 | FN-15 | account/models/account_journal.py:786 | restrict_mode_hash_table' in vals | FACT | always | — | Journal write refuses clearing restrict_mode_hash_table when a posted hashed move exists in the journal ('cannot modify the field ... already has accounting entries'). | N-U11-065 |
| VDR-U11-C153 | FN-15 | account/wizard/account_resequence.py:157 | restrict_mode_hash_table | FACT | always | — | Resequence refuses ordering by date when the journal is hash restricted. | N-U11-057 |
| VDR-U11-C154 | FN-10 | account/models/company.py:1008 | group_account_user | FACT | always | — | _check_hash_integrity requires full accounting group; computes hashes per journal and prefix over hash versions 1 to 4 and returns verified, corrupted or no_data. | N-U11-066 |
| VDR-U11-C155 | FN-10 | account/models/res_users.py:27 | _activate_group_account_secured | FACT | always | — | _activate_group_account_secured applies the inalterability group to the read-only and invoicing groups. | N-U11-064 |
| VDR-U11-C156 | FN-10 | account/models/account_move.py:322 | posted_before | FACT | always | — | posted_before boolean is set at first posting and never cleared by the code read. | N-U11-058 |
| VDR-U11-C157 | FN-10 | account/models/account_move.py:6372 | inalterable_hash | OBSERVATION | restored DB | — | Restored DB: restrict_mode_hash_table is NULL (not set) on all 7 journals and there are zero entries, so no hash chain exists. | N-U11-068 |
| VDR-U11-C158 | FN-09 | account/wizard/account_resequence.py:160 | moves_to_rename.name = False | FACT | resequence wizard | — | Resequence clears and rewrites names period by period, keeping current order or reordering by date; wizard ACL is limited to the administrator group. | N-U11-057 |
| VDR-U11-C159 | FN-09 | account/models/account_journal.py:199 | sequence_override_regex | FACT | always | — | Journal sequence_override_regex is a technical text regex with capture groups prefix1, year, prefix2, month, prefix3, seq, suffix. | N-U11-068 |
| VDR-U11-C160 | FN-09 | account/models/account_journal.py:177 | refund_sequence | FACT | always | — | refund_sequence and payment_sequence are stored computed booleans defaulting true for sale and purchase (refund) and bank, cash, credit (payment). | N-U11-054 |
| VDR-U11-C161 | FN-09 | account/models/account_journal.py:706 | journal.type in ('sale', 'purchase') | FACT | always | — | _compute_refund_sequence sets true for sale and purchase journal types. | N-U11-054 |
| VDR-U11-C162 | FN-09 | account/models/account_journal.py:120 | is_self_billing | FACT | always | — | Self-billing journals number invoices with a different sequence per partner. | N-U11-054 |
| VDR-U11-C163 | FN-09 | account/models/account_move.py:4218-4223 | is_self_billing | INFERENCE | self-billing journal | — | With is_self_billing and no partner, the last-sequence domain forces a reset (4222-4223) and the starting sequence uses the partner id zero-filled (4296-4303). | N-U11-054 |
| VDR-U11-C164 | FN-10 | account/models/account_move_line.py:1982 | legally required | INFERENCE | always | — | Source comment states hashed entries are legally required not to be deleted; INFERENCE of the compliance purpose of the hash chain. | N-U11-050 |
| VDR-U11-C165 | FN-09 | account/models/account_move.py:4278 | fiscalyear_last_day | FACT | always | — | Starting-sequence generation reads company fiscalyear_last_day and fiscalyear_last_month to decide staggered fiscal year patterns. | N-U11-069 |
| VDR-U11-C166 | FN-09 | account/models/account_move.py:4057 | group_account_manager | INFERENCE | always | — | Managers (and fiduciary-mode companies and force_delete) may delete numbered moves from the middle of a chain, creating gaps; only the hash setting prevents this. | N-U11-072 |
| VDR-U11-C167 | FN-09 | n/a | n/a | UNKNOWN | n/a | RT | Numbering under concurrent posting and the exact starting pattern for the seeded journals were not executed; resolve by posting in a scratch database. | N-U11-073 |
| VDR-U11-C168 | PCO-F01 | account/models/company.py:57 | SOFT_LOCK_DATE_FIELDS | FACT | always | — | Soft lock fields are fiscalyear_lock_date, tax_lock_date, sale_lock_date, purchase_lock_date; LOCK_DATE_FIELDS adds hard_lock_date (five kinds in total). | N-U11-074 |
| VDR-U11-C169 | PCO-F01 | account/models/company.py:76 | fiscalyear_lock_date = fields.Date | FACT | always | — | Company field fiscalyear_lock_date ('Global Lock Date') is tracked; help says entries up to and including the date are postponed to a later time according to the journal's sequence. | N-U11-074 |
| VDR-U11-C170 | PCO-F01 | account/models/company.py:81 | tax_lock_date = fields.Date | FACT | always | — | tax_lock_date ('Tax Return Lock Date') applies to entries with taxes; its help says it is set automatically when the tax closing entry is posted (setting mechanism not found in Community). | N-U11-094 |
| VDR-U11-C171 | PCO-F01 | account/models/company.py:87 | sale_lock_date = fields.Date | FACT | always | — | sale_lock_date applies to sales entries; purchase_lock_date (line 92) to purchase entries. | N-U11-076 |
| VDR-U11-C172 | PCO-F01 | account/models/company.py:97 | hard_lock_date = fields.Date | FACT | always | — | hard_lock_date help: irreversible and does not allow any exception. | N-U11-076 |
| VDR-U11-C173 | PCO-F01 | account/models/company.py:552 | def _validate_locks | FACT | always | — | Company write calls _validate_locks first: checks hard lock monotonicity, draft entries inside hard lock, and unreconciled statement lines inside the fiscal or hard lock. | N-U11-086 |
| VDR-U11-C174 | PCO-F01 | account/models/company.py:573 | Hard Lock Date cannot be removed | FACT | always | — | Once hard_lock_date is set it cannot be cleared (UserError) and a new value must be posterior or equal to the previous one. | N-U11-086 |
| VDR-U11-C175 | PCO-F01 | account/models/company.py:584 | There are still draft entries | FACT | always | — | Setting hard_lock_date is refused (RedirectWarning to the draft list) when draft entries exist on or before the date within the company tree. | N-U11-086 |
| VDR-U11-C176 | PCO-F01 | account/models/company.py:597 | unreconciled bank statement lines | FACT | always | — | Setting fiscalyear_lock_date or hard_lock_date is refused when unreconciled statement lines (is_reconciled False, move draft or posted) exist on or before the maximum of the two. | N-U11-086 |
| VDR-U11-C177 | PCO-F01 | account/models/company.py:607 | def _get_user_lock_date | FACT | always | — | User lock date loops over the company and its parents; for each company with a lock it looks for an active exception of that field for the current user or for everybody with a lock date earlier than the company lock, ordered by lock_date ascending nulls first; the exception date replaces the company date, and the maximum over companies is returned. | N-U11-087 |
| VDR-U11-C178 | PCO-F01 | account/models/company.py:414 | @api.depends('fiscalyear_lock_date') | FACT | always | — | user_*_lock_date fields depend on context uid and ignore_exceptions; they are non-stored computed per user. | N-U11-091 |
| VDR-U11-C179 | PCO-F01 | account/models/company.py:442 | def _compute_user_hard_lock_date | FACT | always | — | user_hard_lock_date is the maximum hard_lock_date over the company and its parent companies (inactive included, sudo); exceptions are never consulted. | N-U11-087 |
| VDR-U11-C180 | PCO-F01 | account/models/company.py:642 | def _get_user_fiscal_lock_date | FACT | always | — | Fiscal lock for a journal is max(global lock, hard lock) and, for a sale journal, also the sale lock, for a purchase journal the purchase lock. | N-U11-076 |
| VDR-U11-C181 | PCO-F01 | account/models/company.py:656 | def _get_violated_soft_lock_date | FACT | always | — | A date violates a soft lock if it is <= the lock ignoring exceptions and also <= the lock including the user's exceptions; the returned date is the exception-adjusted lock. | N-U11-082 |
| VDR-U11-C182 | PCO-F01 | account/models/company.py:675 | def _get_lock_date_violations | FACT | always | — | Returns tuples (lock date, field) for global, sale, purchase and tax locks selected by flags plus the hard lock. | N-U11-076 |
| VDR-U11-C183 | PCO-F01 | account/models/company.py:723 | def _get_violated_lock_dates | FACT | always | — | Posting-time violations use fiscalyear True, sale only for sale journals, purchase only for purchase journals, tax only when the entry has tax impact, hard True; result sorted chronologically. | N-U11-076 |
| VDR-U11-C184 | PCO-F01 | account/models/account_move.py:2823 | def _check_fiscal_lock_dates | FACT | always | — | _check_fiscal_lock_dates evaluates global, sale and purchase locks (by journal type) and the hard lock with tax=False; raises UserError 'You cannot add/modify entries prior to and inclusive of' plus the formatted locks. | N-U11-078 |
| VDR-U11-C185 | PCO-F01 | account/models/account_move.py:2824 | BYPASS_LOCK_CHECK | FACT | always | — | Context key bypass_lock_check equal to the BYPASS_LOCK_CHECK sentinel skips the fiscal lock check; its only Community use is partner.py:774 and 777 (commercial partner propagation). | N-U11-078 |
| VDR-U11-C186 | PCO-F01 | account/models/account_move.py:5702 | lock_dates = move._get_violated_lock_dates | FACT | always | — | At posting, each move to post whose date violates a lock gets move.date replaced by _get_accounting_date; the entry is not rejected. | N-U11-077 |
| VDR-U11-C187 | PCO-F04 | account/models/account_move.py:6728 | lock_dates = lock_dates or self._get_violated_lock_dates | FACT | always | RT | _get_accounting_date first moves the candidate date to the day after the latest violated lock; sale documents are then adjusted only when a lock is violated (min of today and end of month or year, depending on the sequence reset kind); the result depends on the last number of the journal, so exact outputs need a running system. | N-U11-077 |
| VDR-U11-C188 | PCO-F04 | account/models/account_move.py:6741 | number_reset in ('month', 'year_range_month') | FACT | non-sale documents | RT | For non-sale documents (evaluated even without locks), with a month-resetting sequence a candidate date in a past month becomes the last day of that month, otherwise max(candidate, today); with a year-resetting sequence a past year becomes 31 December of that year; docstring: when registering in the past the sequence must still increase. | N-U11-077 |
| VDR-U11-C189 | PCO-F04 | account/models/account_move.py:861 | def _compute_date | FACT | always | — | Accounting date of an invoice or receipt is computed from invoice_date (or date); for non-sale documents it passes through _get_accounting_date with the tax-impact flag (so purchase-side dates are adjusted at entry time), sale documents keep invoice_date until posting; non-invoices only default to today. | N-U11-077 |
| VDR-U11-C190 | PCO-F04 | account/models/account_move.py:857 | def _get_accounting_date_source | FACT | always | — | Accounting date source is invoice_date, falling back to date. | N-U11-077 |
| VDR-U11-C191 | PCO-F04 | account/models/account_move.py:1108 | def _compute_taxable_supply_date | FACT | always | — | taxable_supply_date and delivery_date computes are empty stubs (pass) in Community; localizations override them; so no physical-versus-recorded date logic exists in account beyond date vs invoice_date. | N-U11-095 |
| VDR-U11-C192 | PCO-F01 | account/models/account_move.py:1932 | def _compute_tax_lock_date_message | FACT | UI | — | A non-stored warning message explains that a date prior to the locks will be moved on posting. | N-U11-077 |
| VDR-U11-C193 | PCO-F01 | account/models/account_move.py:6762 | def _get_lock_date_message | FACT | UI | — | Message states 'The date is being set prior to' the formatted locks and the date the entry will be accounted on. | N-U11-077 |
| VDR-U11-C194 | PCO-F01 | account/models/account_move.py:3997 | date of a not-locked move | FACT | always | — | After write, posted moves are re-checked against fiscal and tax locks when date or state changed, preventing moving a posted move into a locked period. | N-U11-078 |
| VDR-U11-C195 | PCO-F01 | account/models/account_move_line.py:3485 | def _get_lock_date_protected_fields | FACT | always | — | Tax-lock protected line fields: balance, tax_line_id, tax_ids, tax_tag_ids; fiscal-lock protected adds account_id, journal_id, amount_currency, currency_id, partner_id; reconciliation-protected: account_id, date, balance, amount_currency, currency_id. | N-U11-078 |
| VDR-U11-C196 | PCO-F01 | account/models/account_move_line.py:1853 | protected_fields['fiscal'] | FACT | always | — | Line write on a posted line changing a fiscal-protected field runs _check_fiscal_lock_dates; changing tax-protected fields queues _check_tax_lock_date. | N-U11-078 |
| VDR-U11-C197 | PCO-F01 | account/models/account_move_line.py:1849 | modify the taxes related to | FACT | always | — | Line write refuses changing tax_ids or tax_line_id on posted lines regardless of locks. | N-U11-079 |
| VDR-U11-C198 | PCO-F01 | account/models/account_move_line.py:1526 | def _check_tax_lock_date | FACT | always | — | _check_tax_lock_date refuses (UserError 'impact an already issued tax statement') when a posted line affecting the tax report has a date within tax lock or hard lock; the check ignores global, sale and purchase locks. | N-U11-079 |
| VDR-U11-C199 | PCO-F01 | account/models/account_move_line.py:1794 | ignore_tax_lock_date | FACT | always | — | Line create and unlink skip the tax lock check only when context ignore_tax_lock_date is the module sentinel _ignore_tax_lock_date; no Community caller sets it. | N-U11-079 |
| VDR-U11-C200 | PCO-F01 | account/models/account_move_line.py:1997 | Check the lock date | FACT | always | — | Line unlink on non-zero lines of posted moves runs _check_fiscal_lock_dates and _check_tax_lock_date. | N-U11-080 |
| VDR-U11-C201 | PCO-F01 | account/models/account_move.py:5541 | def _can_be_unlinked | FACT | always | — | An entry can be deleted only if it has no hash, its date is later than the user's fiscal lock date for its journal, and it is not a posted caba or exchange entry. | N-U11-080 |
| VDR-U11-C202 | PCO-F01 | account/models/account_move.py:3827 | user_fiscal_lock_date | FACT | always | — | copy_data replaces the date with the user fiscal lock date plus one day when the (default or original) date is on or before the lock. | N-U11-081 |
| VDR-U11-C203 | PCO-F01 | account/models/account_lock_exception.py:11 | class AccountLock_Exception | FACT | always | — | Lock exception model account.lock_exception: active flag, state active/revoked/expired computed, company, user (empty means everybody), reason, optional end_datetime, lock_date_field, lock_date and company_lock_date snapshot. | N-U11-082 |
| VDR-U11-C204 | PCO-F01 | account/models/account_lock_exception.py:177 | exactly one lock date field | FACT | always | — | An exception must change exactly one soft lock field; hard lock is not selectable; the company lock date at creation is stored. | N-U11-082 |
| VDR-U11-C205 | PCO-F01 | account/models/account_lock_exception.py:104 | def _compute_state | FACT | always | — | State: revoked if inactive, expired if end_datetime in the past, else active. | N-U11-088 |
| VDR-U11-C206 | PCO-F01 | account/models/account_lock_exception.py:203 | company_chatter_message | FACT | always | — | Exception creation posts a message with tracking values on the company chatter naming user, expiry and reason. | N-U11-083 |
| VDR-U11-C207 | PCO-F01 | account/models/account_lock_exception.py:218 | cannot duplicate a Lock Date Exception | FACT | always | — | copy() raises UserError. | N-U11-083 |
| VDR-U11-C208 | PCO-F01 | account/models/account_lock_exception.py:234 | def action_revoke | FACT | always | — | Revoke requires the account manager group or superuser; sets active False and end_datetime now for active exceptions. | N-U11-083 |
| VDR-U11-C209 | PCO-F01 | account/models/account_lock_exception.py:221 | def _recreate | FACT | always | — | _recreate copies all exceptions with the new company lock date and revokes the originals. | N-U11-085 |
| VDR-U11-C210 | PCO-F01 | account/models/company.py:764 | revoke all active exceptions | FACT | always | — | Company write recreates active exceptions affecting changed soft lock fields after saving new lock dates. | N-U11-085 |
| VDR-U11-C211 | PCO-F01 | account/models/account_lock_exception.py:257 | def _get_audit_trail_during_exception_domain | FACT | always | — | Audit domain: moves of the company whose chatter has messages created since the exception start (by the exception user, up to end) and whose date lies in the excepted period or whose date was changed from or to it; opened by action_show_audit_trail_during_exception. | N-U11-084 |
| VDR-U11-C212 | PCO-F01 | account/security/ir.model.access.csv:19 | account.group_account_manager | OBSERVATION | restored DB | — | ACL: lock exception rows are read for base.group_user, and read plus create for account.group_account_manager; no write or unlink for anyone; DB shows the same two rows (Role User read, Administrator read+create). | N-U11-093 |
| VDR-U11-C213 | PCO-F01 | base/security/ir.model.access.csv:42 | group_erp_manager | OBSERVATION | restored DB | — | res.company write requires group_erp_manager (base ACL, DISCOVERED SUPPORTING MODULE base); account _validate_locks adds no role check, so lock dates are set by whoever can edit the company record. | N-U11-093 |
| VDR-U11-C214 | PCO-F01 | account/models/company.py:742 | self._validate_locks(vals) | FACT | always | — | write() on res.company calls _validate_locks, invalidates user lock caches for changed lock fields, then recreates exceptions. | N-U11-086 |
| VDR-U11-C215 | PCO-F01 | account/models/account_lock_exception.py:98 | _company_id_end_datetime_idx | FACT | always | — | Index on (company_id, user_id, end_datetime) for active exceptions supports lookup speed. | N-U11-088 |
| VDR-U11-C216 | PCO-F01 | account/models/account_journal_dashboard.py:156 | _get_user_fiscal_lock_date | FACT | dashboard | — | Journal dashboard sequence-hole indicator considers only moves after the journal's lock date ignoring exceptions. | N-U11-060 |
| VDR-U11-C217 | PCO-F01 | account/models/company.py:76 | fiscalyear_lock_date | OBSERVATION | restored DB | — | Restored DB: 1 company; fiscalyear, tax, sale, purchase and hard lock dates are all NULL; account_lock_exception has 0 rows; res_company lock fields carry tracking (5 of 5). | N-U11-089 |
| VDR-U11-C218 | PCO-F01 | account/models/company.py:56 | SOFT_LOCK_DATE_FIELDS | UNKNOWN | n/a | RT | No Community view or menu was found that edits the lock dates (grep of views, wizard and data for the fields only found the exception form view); UNKNOWN whether the company form exposes them via other modules. Resolution: run Odoo and inspect Settings > Companies and Accounting settings. | N-U11-089 |
| VDR-U11-C219 | PCO-F01 | account/models/account_move_line.py:1540 | already issued tax statement | INFERENCE | always | — | The tax lock error message states that the operation would impact an already issued tax statement; INFERENCE of the purpose of locks. | N-U11-075 |
| VDR-U11-C220 | PCO-F01 | account/wizard/account_secure_entries_wizard.py:38 | hard lock date | FACT | secure wizard | — | The max_hash_date of the secure wizard considers only entries after the hard lock date, tying integrity protection to period locks. | N-U11-090 |
| VDR-U11-C221 | PCO-F01 | account/models/account_move.py:5706 | move.date = move._get_accounting_date | INFERENCE | always | — | The date shift at posting means the stored accounting date may differ from the document's own date (invoice_date) for postings made inside locked periods. | N-U11-092 |
| VDR-U11-C222 | PCO-F01 | n/a | n/a | UNKNOWN | n/a | RT | Interaction of the date shift with hash chains and branch companies is unknown; resolve with a multi-company runtime test. | N-U11-095 |
| VDR-U11-C223 | SDV-F07 | account/models/account_move.py:59 | TYPE_REVERSE_MAP | FACT | always | — | Reversal type map: out_invoice to out_refund, out_refund to out_invoice, in_invoice to in_refund, in_refund to in_invoice, out_receipt to out_refund, in_receipt to in_refund, entry to entry. | N-U11-096 |
| VDR-U11-C224 | FN-07 | account/models/account_move.py:629 | reversed_entry_id = fields.Many2one | FACT | always | — | reversed_entry_id 'Reversal of' is read-only, not copied, indexed, company-checked; reversal_move_ids is its inverse One2many. | N-U11-096 |
| VDR-U11-C225 | FN-07 | account/models/account_move.py:5495 | def _reverse_moves | FACT | always | — | _reverse_moves copies each move with move_type mapped, reversed_entry_id, partner_id and given defaults, with include_business_fields and move_reverse_cancel contexts. | N-U11-096 |
| VDR-U11-C226 | FN-07 | account/models/account_move.py:5506 | if cancel | FACT | cancel=True | — | With cancel True the reconciliations of all original lines are removed first. | N-U11-105 |
| VDR-U11-C227 | FN-07 | account/models/account_move.py:5525 | reverse_moves.with_context | FACT | always | — | For entries (and cogs lines) of the reversal, balance and amount_currency are negated, and is_storno toggled when the company uses storno. | N-U11-103 |
| VDR-U11-C228 | FN-07 | account/models/account_move.py:5536 | Reconcile moves together to cancel | FACT | cancel=True | — | With cancel True the reversal is posted at once with _post(soft=False) and reconciled with the original. | N-U11-101 |
| VDR-U11-C229 | FN-08 | account/models/account_move.py:5474 | def _reconcile_reversed_moves | FACT | always | — | Lines of original and reversal that are not reconciled are grouped by account and currency and reconciled when the account is reconcilable (receivable first) or of type cash or credit card. | N-U11-102 |
| VDR-U11-C230 | FN-08 | account/models/account_move.py:5775 | _reconcile_reversed_moves(draft_reverse_moves | FACT | always | — | At the end of _post, draft reversals of posted originals are reconciled with the original (move_reverse_cancel context passed through). | N-U11-102 |
| VDR-U11-C231 | SDV-F07 | account/wizard/account_move_reversal.py:15 | domain=[('state', '=', 'posted')] | FACT | always | — | Reversal wizard move_ids domain is posted moves; default_get raises UserError if any selected move is not posted and if the selection spans several companies. | N-U11-098 |
| VDR-U11-C232 | SDV-F07 | account/wizard/account_move_reversal.py:60 | def _check_journal_type | FACT | always | — | Wizard constraint: chosen journal type must be among the types of the reversed moves' journals. | N-U11-098 |
| VDR-U11-C233 | SDV-F07 | account/wizard/account_move_reversal.py:92 | def _prepare_default_reversal | FACT | always | — | Default reversal values: ref 'Reversal of: name, reason', date and invoice_date_due = wizard date, invoice_date = wizard date for invoices, journal, payment term only if mixed early pay discount, salesperson, auto_post at_date when the date is in the future, invoice_origin. | N-U11-099 |
| VDR-U11-C234 | SDV-F07 | account/wizard/account_move_reversal.py:129 | is_cancel_needed = not is_auto_post | FACT | always | — | Batch rule: cancel (immediate posting and reconciliation) only if not auto-post and (modify option or wizard move_type is entry); otherwise reversal is created draft. | N-U11-100 |
| VDR-U11-C235 | SDV-F07 | account/wizard/account_move_reversal.py:176 | def refund_moves | FACT | always | — | refund_moves (credit note button) calls reverse_moves with is_modify False; for invoices the credit note stays draft and editable. | N-U11-100 |
| VDR-U11-C236 | SDV-F07 | account/wizard/account_move_reversal.py:179 | def modify_moves | FACT | always | — | modify_moves calls reverse_moves with is_modify True: reversal posted and reconciled, then a new draft copy of product, section and note lines is created for correction. | N-U11-101 |
| VDR-U11-C237 | SDV-F07 | account/wizard/account_move_reversal.py:145 | include_business_fields | FACT | modify option | — | The rebuilt draft copies business data via copy_data with date and origin, keeps the vendor main attachment copy for vendor documents. | N-U11-101 |
| VDR-U11-C238 | SDV-F07 | account/wizard/account_move_reversal.py:84 | def _compute_from_moves | INFERENCE | always | — | The wizard exposes only date, reason and journal fields (lines 15 to 31) and read-only residual; no amount field exists, so a partial credit requires editing the draft credit note (lines 15-31 and 129-131). | N-U11-111 |
| VDR-U11-C239 | SDV-F07 | account/models/account_move.py:3824 | elif move.move_type == 'entry' | FACT | always | — | copy_data drops the partner for entries unless the reversal-cancel path keeps it, and for out_invoice and in_invoice keeps only create commands of line_ids. | N-U11-103 |
| VDR-U11-C240 | SDV-F07 | account/models/account_move.py:6172 | def action_reverse | FACT | always | — | action_reverse opens the reversal wizard action, titled Credit Note for invoices. | N-U11-096 |
| VDR-U11-C241 | SDV-F07 | account/models/account_move.py:7388 | def _set_reversed_entry | FACT | always | — | _set_reversed_entry links a single out_refund to its original invoice only when the original requires an origin; _refunds_origin_required returns False in Community. | N-U11-108 |
| VDR-U11-C242 | SDV-F07 | account/models/account_move.py:1312 | in_reverse | FACT | always | — | payment_state reversed when an invoice is settled only by refunds or entries of the opposite family. | N-U11-107 |
| VDR-U11-C243 | SDV-F07 | sale/models/account_move.py:71 | def _reverse_moves | FACT | sale installed | — | sale _reverse_moves copies campaign, medium and source to the reversal. | N-U11-106 |
| VDR-U11-C244 | SDV-F07 | hr_expense/models/account_move.py:101 | def _reverse_moves | FACT | hr_expense installed | — | hr_expense _reverse_moves clears the expense link of moves before reversing. | N-U11-106 |
| VDR-U11-C245 | SDV-F07 | sale_timesheet/models/account_move.py:101 | credit_notes = self.filtered | FACT | sale_timesheet installed | — | After posting, timesheet_invoice_id is cleared on timesheets of the reversed invoice linked to the credit note lines. | N-U11-106 |
| VDR-U11-C246 | SDV-F07 | purchase/models/account_invoice.py:176 | if move.reversed_entry_id | FACT | purchase installed | — | purchase create skips the 'created from purchase order' chatter message for reversals. | N-U11-096 |
| VDR-U11-C247 | SDV-F07 | account/security/ir.model.access.csv:121 | access_account_move_reversal | OBSERVATION | restored DB | — | ACL access_account_move_reversal grants the invoicing group read, write and create on the reversal wizard (csv line 121); DB has the same row. | N-U11-110 |
| VDR-U11-C248 | SDV-F07 | account/models/account_move.py:3852 | has been reversed from | FACT | always | — | Copy logs 'This entry has been reversed from' on the new entry when default has reversed_entry_id; wizard logs 'This entry has been reversed' on the original. | N-U11-096 |
| VDR-U11-C249 | SDV-F07 | account/models/account_move.py:3958 | readonly fields on a posted move | INFERENCE | always | — | Posted entries cannot be edited in key fields (am:3958-3969), so reversal is the supported correction path; INFERENCE of purpose. | N-U11-097 |
| VDR-U11-C250 | SDV-F07 | account/models/account_move.py:3827-3829 | timedelta(days=1) | FACT | always | — | A copy or reversal dated inside the user's locked period is proposed one day after the user fiscal lock date. | N-U11-104 |
| VDR-U11-C251 | FN-08 | account/models/account_move.py:5491 | .reconcile() | FACT | always | — | Reversal reconciliation delegates to reconcile() owned by the payments capability (U12). | N-U11-109 |
| VDR-U11-C252 | SDV-F07 | n/a | n/a | UNKNOWN | n/a | RT | Reconciliation of multi-currency and cash-basis reversals not executed; resolve with a runtime reversal of such entries. | N-U11-113 |
| VDR-U11-C253 | FUNCTION MAPPING REQUIRED | account/data/service_cron.xml:4 | Post draft entries with auto_post enabled | FACT | always | — | Cron 'Account: Post draft entries with auto_post enabled and accounting date up to today' runs daily, first call next day 02:00, executing model._autopost_draft_entries(). | N-U11-124 |
| VDR-U11-C254 | FUNCTION MAPPING REQUIRED | account/data/service_cron.xml:4 | ir_cron_auto_post_draft_entry | OBSERVATION | restored DB | — | Restored DB: cron id 17 exists, active, interval 1 day, owned by the root user, failure_count 0, code model._autopost_draft_entries(); no entries exist so each run selects nothing. | N-U11-124 |
| VDR-U11-C255 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6460 | def _autopost_draft_entries | FACT | always | — | _autopost_draft_entries(batch_size=100) searches draft moves with date <= today and auto_post != 'no', limited to the batch size, reports remaining work to the scheduler. | N-U11-116 |
| VDR-U11-C256 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6474 | try posting in batch | FACT | always | — | The whole batch is posted with _post() (soft default); on UserError the transaction is rolled back and moves are retried individually. | N-U11-117 |
| VDR-U11-C257 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6488 | except UserError as e | FACT | always | — | A move failing individually gets a chatter comment 'could not be posted for the following reason', auto_post set to 'no' and progress is committed; each retry locks the row for update and re-checks the domain. | N-U11-117 |
| VDR-U11-C258 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4816 | def _copy_recurring_entries | FACT | always | — | After posting an entry with auto_post monthly, quarterly or yearly, _copy_recurring_entries copies the next occurrence (first entry referenced by auto_post_origin_id) unless one with that date exists or auto_post_until is exceeded. | N-U11-118 |
| VDR-U11-C259 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4810 | def _apply_delta_recurring_entries | FACT | always | — | Next date = origin date plus (1, 3 or 12 months) times the number of elapsed periods, preserving the day where possible. | N-U11-118 |
| VDR-U11-C260 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5712 | skip_recurring_copy | FACT | always | — | _post triggers recurring copy for moves whose auto_post is neither 'no' nor 'at_date' unless context skip_recurring_copy is set. | N-U11-118 |
| VDR-U11-C261 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4854 | def _get_fields_to_copy_recurring_entries | FACT | always | — | Recurring copies keep auto_post, auto_post_until and auto_post_origin_id; modules add fields through this hook. | N-U11-118 |
| VDR-U11-C262 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6319 | def _unlink_next_draft_auto_post_moves | FACT | always | — | On reset to draft the next draft recurrence of the same origin with a later date is deleted via SQL lateral join. | N-U11-119 |
| VDR-U11-C263 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:687 | archive a journal containing draft | FACT | always | — | Constraint on journal active: archiving refused if the journal has draft entries. | N-U11-121 |
| VDR-U11-C264 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2847 | automatically posted | FACT | always | — | Auto-posted vendor documents require a bill date (constraint). | N-U11-120 |
| VDR-U11-C265 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5925 | def _autopost_bill | FACT | always | — | _autopost_bill posts a bill only if company autopost_bills, partner autopost 'always', purchase document, no abnormal amount warning and journal not hash restricted; a duplicate reference prevents it with a note. | N-U11-122 |
| VDR-U11-C266 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:1134 | invoice._autopost_bill() | FACT | always | — | Bills created from attachments in a journal call _autopost_bill (also called by account_peppol, not installed). | N-U11-122 |
| VDR-U11-C267 | FUNCTION MAPPING REQUIRED | account/models/company.py:269 | autopost_bills = fields.Boolean | FACT | always | — | Company autopost_bills defaults True (DB: true). | N-U11-122 |
| VDR-U11-C268 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6478 | except UserError | INFERENCE | always | RT | Only UserError is caught (lines 6478 and 6488); any other exception class propagates out of the cron run. Marked RT: scheduler behaviour on unexpected exceptions needs execution. | N-U11-126 |
| VDR-U11-C269 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6472 | _commit_progress | FACT | always | RT | Cron progress is committed through ir.cron._commit_progress after batches and single moves; commit semantics are not read here (base). | N-U11-128 |
| VDR-U11-C270 | FUNCTION MAPPING REQUIRED | stock_account/models/res_company.py:148 | action_close_stock_valuation | FACT | stock_account installed | — | stock_account calls action_close_stock_valuation(auto_post=True) from a closing cron, creating an entry in the stock journal (DISCOVERED SUPPORTING MODULE). | N-U11-187 |
| VDR-U11-C271 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6462-6463 | recurring entries created in | FACT | always | — | Docstring: the cron method posts entries such as those created by account_asset (Enterprise, not present) and recurring entries created in _post(). | N-U11-114 |
| VDR-U11-C272 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:304 | posted automatically on its | INFERENCE | always | — | auto_post help text: entry is posted automatically on its accounting date and for similar recurring invoices; INFERENCE of purpose: preparation ahead of time. | N-U11-115 |
| VDR-U11-C273 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6492 | move.auto_post = 'no' | FACT | always | — | A move that failed to post in the cron is returned to a normal draft state with auto_post 'no'. | N-U11-123 |
| VDR-U11-C274 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6475 | moves._post() | FACT | always | — | The cron calls the standard _post (soft default), so locks, numbering, validation and hashing apply as for manual posting. | N-U11-125 |
| VDR-U11-C275 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6492 | move.auto_post = 'no' | INFERENCE | always | — | Because failure turns auto_post off, a recurring entry that failed is not posted again and its next occurrence is never created (copy happens at posting, am:5711-5713). | N-U11-127 |
| VDR-U11-C276 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:340 | ('payment_term', 'Payment Term') | FACT | always | — | display_type selection: product, cogs, tax, discount, rounding, payment_term, line_section, line_subsection, line_note, epd, non_deductible_product_total, non_deductible_product, non_deductible_tax (13 values); stored, computed, required. | N-U11-131 |
| VDR-U11-C277 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:524 | def _compute_display_type | FACT | always | — | For lines without display type: invoices get tax when tax_line_id is set, payment_term when the account is receivable or payable, else product; non-invoice entries default to product. | N-U11-131 |
| VDR-U11-C278 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:366 | invoice_line_ids = fields.One2many | FACT | always | — | invoice_line_ids is a subset of line_ids restricted to product, section, subsection and note display types. | N-U11-131 |
| VDR-U11-C279 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:727 | def _compute_balance | FACT | always | — | balance is blank for section lines; for non-invoice entries a new line defaults to the negative sum of the other lines (default balancing); invoices default 0. | N-U11-132 |
| VDR-U11-C280 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:747 | def _compute_debit_credit | FACT | always | — | debit and credit are computed from balance; for storno lines the sides are swapped. | N-U11-132 |
| VDR-U11-C281 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1425 | def _inverse_debit | FACT | always | — | Writing debit sets is_storno when negative, clears credit when debit non-zero and sets balance = debit - credit; _inverse_credit is symmetrical. | N-U11-132 |
| VDR-U11-C282 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1693 | def _sanitize_vals | FACT | always | — | Before create or write, debit and credit values are popped and converted to balance (debit - credit) unless balance is given; storno companies mark is_storno for negative inputs. | N-U11-132 |
| VDR-U11-C283 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1714 | def _prepare_create_values | FACT | always | — | If amount_currency is given without balance, debit or credit, balance is not defaulted so it can be derived; section lines drop account_id. | N-U11-133 |
| VDR-U11-C284 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:777 | def _compute_amount_currency | FACT | always | — | amount_currency defaults to balance times currency_rate rounded; when line currency equals company currency on a non-invoice, amount_currency = balance. | N-U11-133 |
| VDR-U11-C285 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1413 | def _inverse_amount_currency | FACT | always | — | Writing amount_currency: same-currency lines copy it to balance; foreign lines on non-invoices set balance = amount_currency / currency_rate rounded in company currency. | N-U11-133 |
| VDR-U11-C286 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1733 | def _sync_invoice | FACT | always | — | Line-level sync: when balance or move type changed and the line currency equals the company currency, amount_currency is set to balance; when amount_currency, rate or type changed, balance is recomputed as amount_currency / rate; debit and credit are recomputed. | N-U11-133 |
| VDR-U11-C287 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:541 | def _compute_currency_id | FACT | always | — | Line currency: cogs lines use company currency; invoice lines follow the move currency; other lines keep their currency or fall back to company currency. | N-U11-134 |
| VDR-U11-C288 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:757 | def _compute_currency_rate | FACT | always | — | Line rate: invoices use the move's invoice_currency_rate; other entries use the conversion rate at invoice date, entry date or today. | N-U11-134 |
| VDR-U11-C289 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1120 | def _compute_currency_id | FACT | always | — | Move currency defaults to the statement line foreign currency, then journal currency, current currency or company currency. | N-U11-134 |
| VDR-U11-C290 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1151 | def _compute_invoice_currency_rate | FACT | always | — | invoice_currency_rate for invoices and receipts equals the expected rate at the invoice date (or today) and is re-derived when currency, company or dates change. | N-U11-134 |
| VDR-U11-C291 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3722 | def _get_sync_stack | FACT | always | — | Dynamic-line sync stack in order: 10 payment_term lines, 20 unbalanced (entries), 30 rounding lines, 40 discount lines, 50 tax lines, 60 non-deductible lines, 70 early-payment-discount lines, 80 commercial partner propagation. | N-U11-135 |
| VDR-U11-C292 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3727 | Only invoice-like and journal entries | FACT | always | — | Tax sync applies to invoices or entries in 'auto tax mode' (lines with taxes or repartition lines); unbalanced sync applies to entries not generated as cash-basis. | N-U11-135 |
| VDR-U11-C293 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3767 | def _sync_dynamic_lines | FACT | always | — | _sync_dynamic_lines wraps create and write; recursion is blocked through the skip_invoice_sync key and the context managers are entered in stack order. | N-U11-135 |
| VDR-U11-C294 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3591 | def _sync_dynamic_line | FACT | always | — | Generic sync compares needed values before and after the write by key, deletes obsolete lines, rewrites lines being replaced, creates missing lines and updates changed amounts. | N-U11-136 |
| VDR-U11-C295 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3644 | do not modify user input | FACT | always | — | Sync returns early if needs did not change, and when the lines were created manually with no previous need. | N-U11-136 |
| VDR-U11-C296 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1968 | def _prevent_automatic_line_deletion | FACT | dynamic_unlink unset | — | Deleting a tax line while line taxes exist, or a payment_term line, raises ValidationError unless context dynamic_unlink (set by the sync) is true. | N-U11-137 |
| VDR-U11-C297 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3698 | def _sync_invoice | FACT | always | — | Move-level sync propagates the commercial partner to all lines when it changes; _inverse_partner_id also writes line partners for invoices. | N-U11-138 |
| VDR-U11-C298 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3248 | def _sync_rounding_lines | FACT | always | — | Cash-rounding lines are recomputed only for non-posted invoices. | N-U11-135 |
| VDR-U11-C299 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3287 | def _sync_tax_lines | FACT | always | — | _sync_tax_lines builds tax lines from base lines of display types product, epd, rounding and non_deductible_product (detail belongs to the taxation unit). | N-U11-141 |
| VDR-U11-C300 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1389 | def _compute_needed_terms | FACT | always | — | needed_terms maps keys (move, maturity date, discount date) to balance and amount_currency from the payment terms (or a single line at due date) for invoices with invoice lines (detail belongs to the payments unit). | N-U11-141 |
| VDR-U11-C301 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:574 | term_by_move | FACT | always | — | payment_term line names derive from move ref and payment_reference, with 'installment #n' when the payment term has several lines; lines of hashed moves are skipped. | N-U11-139 |
| VDR-U11-C302 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:607 | def _compute_account_id | FACT | always | — | payment_term line account comes from an existing term line, else partner receivable or payable property, else company partner, else any active receivable or payable account, mapped by fiscal position; product lines use product accounts or the partner's most frequent account; remaining lines use journal default. | N-U11-139 |
| VDR-U11-C303 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3854 | def _sanitize_vals | FACT | always | — | Move create and write merge invoice_line_ids commands into line_ids and drop invoice_line_ids. | N-U11-129 |
| VDR-U11-C304 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3986 | skip_account_move_synchronization | FACT | always | — | Move write runs the ORM write with skip_account_move_synchronization and then _synchronize_business_models(changed fields). | N-U11-129 |
| VDR-U11-C305 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:353 | collapse_composition | FACT | always | — | Section lines carry collapse_composition and collapse_prices options for reports and portal. | N-U11-140 |
| VDR-U11-C306 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:182 | line_ids = fields.One2many | FACT | always | — | line_ids is copied with the entry (copy=True); journal_line_ids is a deprecated duplicate. | N-U11-129 |
| VDR-U11-C307 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2078 | def copy_data | FACT | always | — | Line copy drops the name of payment-term lines on invoices, drops balance and account of section or note lines, drops balance of invoice product lines (recomputed from price) and adds business fields only under context include_business_fields. | N-U11-136 |
| VDR-U11-C308 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1765 | line.amount_currency = line.balance | INFERENCE | always | — | Line-level sync keeps amount_currency and balance coherent in both directions when only one changed (aml:1759-1772); INFERENCE of the purpose of synchronisation. | N-U11-130 |
| VDR-U11-C309 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:487 | _check_amount_currency_balance_sign | OBSERVATION | restored DB | — | DB has check_amount_currency_balance_sign, check_credit_debit, check_accountable_required_fields and check_non_accountable_fields_null enforcing line consistency regardless of application path. | N-U11-142 |
| VDR-U11-C310 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1766-1769 | not self.env.is_protected | INFERENCE | always | — | Sync only writes balance or amount_currency when the counterpart field is not protected and not changed; a caller protecting or setting one side relies on this logic (aml:1759-1772). | N-U11-143 |
| VDR-U11-C311 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | Rounding outcomes for tax-included prices with cash rounding in foreign currencies not executed; resolve with runtime invoices. | N-U11-144 |
| VDR-U11-C312 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:112 | ('general', 'Miscellaneous') | FACT | always | — | Journal type selection: sale, purchase, cash, bank, credit, general; required. | N-U11-145 |
| VDR-U11-C313 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:97 | size=5 | FACT | always | — | Journal code (Sequence Prefix) is required, stored, max 5 characters and computed by default from the type (INV, BILL, CSH, BNK, CCD, MISC plus a number). | N-U11-147 |
| VDR-U11-C314 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:293 | _code_company_uniq | FACT | always | — | SQL constraint unique(company_id, code) 'Journal codes must be unique per company'. | N-U11-147 |
| VDR-U11-C315 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:876 | def _get_next_journal_default_code | FACT | always | — | Default codes are prefix plus 1 to 99 chosen among unused codes of the company. | N-U11-147 |
| VDR-U11-C316 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:902 | def _get_valid_journal_types | FACT | always | — | Valid journal types: sale for sale documents, purchase for purchase documents, bank/cash/credit for payments and statement lines, general otherwise. | N-U11-148 |
| VDR-U11-C317 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:934 | _build_no_journal_error_msg | FACT | always | — | If no journal of the valid types exists for the company, _search_default_journal raises UserError. | N-U11-148 |
| VDR-U11-C318 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:897 | def _compute_journal_id | FACT | always | — | journal_id is recomputed by default when the current journal type is invalid for the move; currency-matching journals are preferred when the move currency differs from the company's. | N-U11-148 |
| VDR-U11-C319 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:606 | def _check_type_default_account_id_type | FACT | always | — | Sale and purchase journals cannot have a receivable or payable default account. | N-U11-149 |
| VDR-U11-C320 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:81 | def _get_default_account_domain | FACT | always | — | Default-account domain depends on type: bank gets cash or credit-card accounts, sale gets income, purchase gets expense, general gets all account types. | N-U11-149 |
| VDR-U11-C321 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:130 | suspense_account_id = fields.Many2one | FACT | always | — | suspense_account_id is stored computed and used for statement lines until reconciliation. | N-U11-145 |
| VDR-U11-C322 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:677 | _check_auto_post_draft_entries | FACT | always | — | Archiving a journal that holds draft entries raises ValidationError; unarchiving is not checked. | N-U11-150 |
| VDR-U11-C323 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5659 | if not move.journal_id.active | FACT | always | — | Posting in an archived journal is refused. | N-U11-150 |
| VDR-U11-C324 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:597 | def _check_company_consistency | FACT | always | — | Changing a journal's company is refused when entries of another company tree exist. | N-U11-151 |
| VDR-U11-C325 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:586 | def _check_bank_account | FACT | always | — | Bank journal account must belong to the journal company and its holder must be the company partner. | N-U11-151 |
| VDR-U11-C326 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:177 | Dedicated Credit Note Sequence | FACT | always | — | Journal option refund_sequence (dedicated credit note numbering) and payment_sequence default from journal type. | N-U11-152 |
| VDR-U11-C327 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:786-793 | cannot modify the field | FACT | always | — | Journal write refuses switching off hash protection when hashed posted entries exist. | N-U11-153 |
| VDR-U11-C328 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:717 | def unlink | FACT | always | — | Journal unlink deletes payment method lines and orphan bank accounts and has no explicit guard on entries. | N-U11-154 |
| VDR-U11-C329 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:162 | journal_id = fields.Many2one | OBSERVATION | restored DB | — | Restored DB: account_move_journal_id_fkey has delete action RESTRICT, so journals with entries cannot be deleted at database level; the field is required and company-checked. | N-U11-154 |
| VDR-U11-C330 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:728 | def copy_data | FACT | always | — | Journal copy generates a unique code and appends '(copy)' to the name. | N-U11-155 |
| VDR-U11-C331 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:955 | def _fill_missing_values | FACT | always | — | Journal create fills missing values: bank and cash journals get a liquidity account, profit and loss accounts; sale and purchase journals get default accounts and an alias; credit journals get a credit-card account. | N-U11-156 |
| VDR-U11-C332 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:1021 | def create | FACT | always | — | Journal create runs _fill_missing_values, creates the record and sets the bank account for bank journals. | N-U11-156 |
| VDR-U11-C333 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:199 | sequence_override_regex | FACT | always | — | Optional technical regex overrides sequence parsing for the journal. | N-U11-157 |
| VDR-U11-C334 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:52 | check_company_domain_parent_of | FACT | always | — | Journal company checks use the parent-of domain: records of parent companies are valid for child companies. | N-U11-159 |
| VDR-U11-C335 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:120 | different sequence per partner | FACT | always | — | is_self_billing journals number per partner. | N-U11-157 |
| VDR-U11-C336 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:171 | currency_id = fields.Many2one | FACT | always | — | A journal may carry its own currency which becomes the default currency of its entries. | N-U11-157 |
| VDR-U11-C337 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:258 | alias_name = fields.Char | FACT | always | — | Journal e-mail alias creates documents from incoming mail; alias model is account.move. | N-U11-157 |
| VDR-U11-C338 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:823 | alias_model_id | FACT | always | — | _alias_get_creation_values sets the alias model to account.move. | N-U11-189 |
| VDR-U11-C339 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:110 | ('bank', 'Bank') | OBSERVATION | restored DB | — | Restored DB: 7 journals: sale INV, purchase BILL, bank BNK1, general MISC, EXCH, CABA, STJ; all active; refund_sequence true for INV and BILL; restrict_mode_hash_table NULL for all; sequence_override_regex NULL. | N-U11-158 |
| VDR-U11-C340 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:55 | access_account_journal_manager | OBSERVATION | restored DB | — | Journal ACL: manager read/write/create/unlink, invoicing and read-only read only; DB also shows rows from purchase, sale, stock_account and hr_expense (read) and sale_stock (administrator read and write). | N-U11-169 |
| VDR-U11-C341 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:102-103 | named using this prefix | INFERENCE | always | — | Journal code help: shorter display name and default prefix for entry numbers; INFERENCE of the purpose of journals as separate numbered books. | N-U11-146 |
| VDR-U11-C342 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3943 | journal of an account move | INFERENCE | always | — | Changing the journal of a numbered entry is refused (am:3936-3943) and the dashboard flags sequence irregularities; INFERENCE: changes to journal setup after entries exist can strand numbering. | N-U11-160 |
| VDR-U11-C343 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | Interaction of archiving with scheduled entries due later, and deletion of journals holding only statements, was not analysed; resolve by runtime test. | N-U11-161 |
| VDR-U11-C344 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:113 | tracking=True | FACT | always | — | account.move tracks name, ref, date, state, move_type, checked, partner_id, partner_bank_id, payment_reference, currency_id, amount_untaxed, payment_state, invoice_source_email, invoice_user_id, invoice_origin. | N-U11-164 |
| VDR-U11-C345 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:113 | tracking | OBSERVATION | restored DB | — | Restored DB: 17 account.move fields have tracking set; the 15 declared in account plus team_id (sale, tracking at sale/models/account_move.py:13) and one more user field whose source was not located. | N-U11-164 |
| VDR-U11-C346 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:104 | tracking=True | FACT | always | — | account.move.line tracks account_id, name, balance and tax_ids (plus other tracked fields at 239 and 393). | N-U11-164 |
| VDR-U11-C347 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1797 | Log changes to move lines | FACT | always | — | Line create logs 'Journal Item created' with tracking values on the move for moves already posted once, unless tracking_disable. | N-U11-164 |
| VDR-U11-C348 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1933 | Journal Item %s updated | FACT | always | — | Line write logs 'Journal Item updated' with the old and new tracked values on posted-once moves. | N-U11-164 |
| VDR-U11-C349 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2016 | Journal Item %s deleted | FACT | always | — | Line unlink logs 'Journal Item deleted' with tracking values. | N-U11-164 |
| VDR-U11-C350 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:335 | audit_trail_message_ids | FACT | always | — | audit_trail_message_ids exposes the notification messages of the entry as 'Audit Trail Messages'. | N-U11-164 |
| VDR-U11-C351 | FUNCTION MAPPING REQUIRED | account/models/company.py:258 | restrictive_audit_trail = fields.Boolean | FACT | always | — | Company flag restrictive_audit_trail (tracked) prevents deletion of journal item related logs. | N-U11-165 |
| VDR-U11-C352 | FUNCTION MAPPING REQUIRED | account/models/company.py:319 | def _check_audit_trail_restriction | FACT | always | — | Turning the flag off is refused when force_restrictive_audit_trail is true; the Community compute returns False. | N-U11-172 |
| VDR-U11-C353 | FUNCTION MAPPING REQUIRED | account/models/company.py:258 | restrictive_audit_trail | OBSERVATION | restored DB | — | Restored DB: restrictive_audit_trail is NULL (off) on the single company; account_storno is false. | N-U11-173 |
| VDR-U11-C354 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4068 | def _unlink_account_audit_trail_except_once_post | FACT | always | — | With restrictive audit trail on, deleting a move that was posted once raises UserError (use cancel) unless context force_delete. | N-U11-165 |
| VDR-U11-C355 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4023 | def _get_unlink_logger_message | FACT | always | — | Deleting posted-once moves of audit-trail companies builds a server log message with user, name, amount, partner and account balances; it is logged at info level after unlink. | N-U11-167 |
| VDR-U11-C356 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1959 | def _unlink_except_posted | FACT | force_delete unset | — | Deleting lines with non-zero balance of posted moves is refused unless context force_delete. | N-U11-166 |
| VDR-U11-C357 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1982 | Hashed entres are legally required | FACT | always | — | Lines of hashed moves are never deletable. | N-U11-166 |
| VDR-U11-C358 | FUNCTION MAPPING REQUIRED | account/models/mail_message.py:180 | def _except_audit_log | FACT | always | — | Deleting an audit message is refused for restricted records (moves of audit-trail companies posted once, used accounts, taxes on lines, partners with lines) unless bypass_audit token. | N-U11-165 |
| VDR-U11-C359 | FUNCTION MAPPING REQUIRED | account/models/mail_message.py:190 | def write | FACT | always | — | mail.message write on res_id, res_model, message_type, subtype, subject (other than whitespace) or non-empty body triggers the same audit protection. | N-U11-165 |
| VDR-U11-C360 | FUNCTION MAPPING REQUIRED | account/models/mail_message.py:13 | DOMAINS | FACT | always | — | Restricted audit logs cover account.move, res.company, account.account, account.tax and res.partner records. | N-U11-165 |
| VDR-U11-C361 | FUNCTION MAPPING REQUIRED | account/models/mail_tracking_value.py:9 | def _except_audit_log | FACT | always | — | Tracking values cannot be deleted or written when their message is protected. | N-U11-165 |
| VDR-U11-C362 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:317 | checked = fields.Boolean | FACT | always | — | checked 'Reviewed' is stored computed, tracked, true by default for posted general-journal entries or when the user may review. | N-U11-168 |
| VDR-U11-C363 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6265 | def set_moves_checked | FACT | always | — | set_moves_checked only touches posted moves; write raises AccessError when marking checked without review right. | N-U11-168 |
| VDR-U11-C364 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:38 | access_account_move_uinvoice | FACT | always | — | ACL account.move: invoicing group read/write/create/unlink; manager read; readonly read; portal read (csv lines 35-41). | N-U11-169 |
| VDR-U11-C365 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:35 | access_account_move_line_manager | FACT | always | — | ACL account.move.line: invoicing full, manager and readonly read, portal read. | N-U11-169 |
| VDR-U11-C366 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:18 | access_account_lock_exception | FACT | always | — | ACL lock exception: base.group_user read; account manager read and create. | N-U11-169 |
| VDR-U11-C367 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:78 | group_account_invoice | FACT | always | — | Group group_account_manager 'Administrator' implies group_account_invoice; manager is also assigned to root and admin users by data. | N-U11-169 |
| VDR-U11-C368 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:5 | There are 5 groups | FACT | always | — | Comment: with only account installed, group_account_invoice and group_account_manager are the groups to use; basic, readonly and user exist but are hidden. | N-U11-175 |
| VDR-U11-C369 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:82 | group_account_secured | FACT | always | — | group_account_secured 'Show Inalterability Features' is a separate group activated when hashing is used. | N-U11-064 |
| VDR-U11-C370 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:128 | account_move_comp_rule | FACT | always | — | Global record rule on account.move: company_id in company_ids; same for account.move.line (134). | N-U11-170 |
| VDR-U11-C371 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:146 | journal_comp_rule | FACT | always | — | Journal rule: company_id parent_of company_ids. | N-U11-170 |
| VDR-U11-C372 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:232 | account_move_see_all | FACT | always | — | Group rules: invoicing group sees all moves and lines (1=1); readonly group read-only 1=1 (lines 263-281). | N-U11-169 |
| VDR-U11-C373 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:247 | account_invoice_rule_portal | FACT | always | — | Portal rule: posted invoices and credit notes (out and in) whose partner is a child of the user's commercial partner. | N-U11-169 |
| VDR-U11-C374 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:40 | res_groups_privilege_accounting | OBSERVATION | restored DB | — | Restored DB: 10 groups with xml id module account (matches declared 10), 125 access rows (CSV 125 data rows), 31 record rules (31 declared); counts match. | N-U11-173 |
| VDR-U11-C375 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:261 | restrict the access for some | FACT | always | — | Comment: sale and other modules restrict user access; readonly and invoicing groups keep access via explicit 1=1 rules. | N-U11-171 |
| VDR-U11-C376 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:121 | access_account_move_reversal | OBSERVATION | restored DB | — | Reversal wizard ACL: invoicing read/write/create; validate wizard likewise (line 120); resequence and secure wizards are manager only (119 and secure row). | N-U11-169 |
| VDR-U11-C377 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | No read-access log or access-log model was found in account (grep for access log or read log in models, wizard and controllers returned no hit); UNKNOWN whether platform-level access logging exists. Resolve by inspecting base modules and server logs. | N-U11-178 |
| VDR-U11-C378 | FUNCTION MAPPING REQUIRED | sale/security/ir_rules.xml:119 | Personal Invoices | OBSERVATION | restored DB | — | Restored DB shows additional rules from sale (Personal Invoices, All Invoices), purchase (Purchase User Account Move) and hr_expense (Team Approver) on account.move and account.move.line (DISCOVERED SUPPORTING MODULES); these are outside this unit's declared source. | N-U11-171 |
| VDR-U11-C379 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:335 | audit_trail_message_ids | INFERENCE | always | — | The entry exposes its notification messages as an audit trail (am:335-343); INFERENCE of the scope of the audit record. | N-U11-162 |
| VDR-U11-C380 | FUNCTION MAPPING REQUIRED | account/models/company.py:261 | prevent deletion of journal item | INFERENCE | always | — | Help of restrictive_audit_trail says it prevents deletion of journal item related logs; INFERENCE of the compliance purpose. | N-U11-163 |
| VDR-U11-C381 | FUNCTION MAPPING REQUIRED | account/models/res_users.py:28 | group_account_secured | FACT | always | — | Inalterability features are hidden behind a dedicated group, applied to read-only and invoicing groups only when hashing is first used (ru:27-38; am:4636-4637). | N-U11-174 |
| VDR-U11-C382 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:42 | group_erp_manager | FACT | always | — | res.company full rights belong to the base administration group (group_erp_manager); account declares no company ACL, so lock-field edits are not governed by accounting groups. | N-U11-176 |
| VDR-U11-C383 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4070 | force_delete | INFERENCE | always | — | Context key force_delete bypasses audit-trail deletion refusal, and the audit-log bypass token bypasses message protection (mm:182); privileged callers can delete protected records. | N-U11-177 |
| VDR-U11-C384 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | Visibility of tracked history to read-only roles and combination of several record rules per user not executed; resolve with test users. | N-U11-179 |
| VDR-U11-C385 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:79 | _check_company_auto = True | FACT | always | — | account.move uses automatic company consistency checks on fields flagged check_company (journal, partner, bank, fiscal position, etc.). | N-U11-183 |
| VDR-U11-C386 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:168 | check_company=True | FACT | always | — | journal_id has check_company True and domain restricted to suitable journals. | N-U11-183 |
| VDR-U11-C387 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:892 | def _compute_company_id | FACT | always | — | company_id defaults from the journal company or the first accessible branch of the current company when the journal company is not in the move company's parents. | N-U11-182 |
| VDR-U11-C388 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2613 | without any company | FACT | always | — | Clearing company raises ValidationError; changing company recomputes the journal when it does not fit. | N-U11-182 |
| VDR-U11-C389 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5673 | move_company_and_parents | FACT | always | — | Account company check allows accounts of the entry company or its parents. | N-U11-184 |
| VDR-U11-C390 | FUNCTION MAPPING REQUIRED | account/models/company.py:617 | for company in self.sudo().parent_ids | FACT | always | — | Lock evaluation walks the company's parents with sudo because parent access may be missing. | N-U11-185 |
| VDR-U11-C391 | FUNCTION MAPPING REQUIRED | account/models/account_journal_dashboard.py:150 | branch company is locked | FACT | always | — | Comment: a branch company is locked when the parent is locked; parent companies cannot add moves to the journal. | N-U11-185 |
| VDR-U11-C392 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5852 | Use sudo() because the SQL | FACT | always | — | Gap-flag maintenance uses sudo browse because the SQL has no company filter and records of sibling companies may be returned. | N-U11-183 |
| VDR-U11-C393 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4647 | sudo() | FACT | always | — | Hash chain search runs with sudo to see all moves regardless of access rights. | N-U11-183 |
| VDR-U11-C394 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/account_move.py:57 | payment_clearing = self.env | FACT | account_payment_interco installed | — | Intercompany clearing creates an entry in the payment company's clearing journal and posts it; a second entry at line 96 settles in the invoice company. | N-U11-186 |
| VDR-U11-C395 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1550 | invoice_vals_list | FACT | sale installed | — | sale _create_account_invoices creates customer invoices as superuser with default_move_type out_invoice so salespeople need no billing right. | N-U11-187 |
| VDR-U11-C396 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:180 | invoice_sudo | FACT | sale installed | — | sale down-payment wizard creates the down-payment invoice with sudo. | N-U11-187 |
| VDR-U11-C397 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:811 | AccountMove.with_company | FACT | purchase installed | — | purchase action_create_invoice creates vendor bills per company with default_move_type in_invoice. | N-U11-187 |
| VDR-U11-C398 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_bill_line_match.py:155 | bill = self.env | FACT | purchase installed | — | purchase bill-line matching creates a vendor bill. | N-U11-187 |
| VDR-U11-C399 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1572 | expense_receipt_vals_list | FACT | hr_expense installed | — | hr_expense creates expense receipts and payment entries with sudo and posts the receipts. | N-U11-187 |
| VDR-U11-C400 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_post_wizard.py:56 | moves_sudo | FACT | hr_expense installed | — | hr_expense post wizard creates receipts with sudo. | N-U11-187 |
| VDR-U11-C401 | FUNCTION MAPPING REQUIRED | stock_account/models/stock_move.py:209 | account_move = self.env | FACT | stock_account installed | — | stock_account creates a valuation entry per stock move in the company's stock journal. | N-U11-187 |
| VDR-U11-C402 | FUNCTION MAPPING REQUIRED | stock_account/models/res_company.py:76 | account_move = self.env | FACT | stock_account installed | — | stock_account stock closing creates an entry in the stock journal and optionally posts it. | N-U11-187 |
| VDR-U11-C403 | FUNCTION MAPPING REQUIRED | mrp_account/models/mrp_production.py:125 | account_move = self.env | FACT | mrp_account installed | — | mrp_account creates work-in-progress valuation entries for manufacturing with sudo. | N-U11-187 |
| VDR-U11-C404 | FUNCTION MAPPING REQUIRED | mrp_account/wizard/mrp_wip_accounting.py:126 | move = self.env | FACT | mrp_account installed | — | mrp_account WIP wizard creates a manual WIP entry with sudo after checking debit equals credit and reversal date. | N-U11-187 |
| VDR-U11-C405 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1081 | moves = self.env | FACT | always | — | account.payment creates the payment journal entry and links it to the payment. | N-U11-187 |
| VDR-U11-C406 | FUNCTION MAPPING REQUIRED | account/models/account_bank_statement_line.py:420 | st_lines.move_id.action_post() | FACT | always | — | Creating bank statement lines creates their move (type entry) and posts it automatically. | N-U11-187 |
| VDR-U11-C407 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3128 | exchange_moves = self.env | FACT | always | — | Reconciliation creates exchange-difference entries. | N-U11-187 |
| VDR-U11-C408 | FUNCTION MAPPING REQUIRED | account/wizard/account_automatic_entry_wizard.py:408 | created_moves = self.env | FACT | always | — | Automatic entries wizard creates and posts transfer or period-change entries. | N-U11-187 |
| VDR-U11-C409 | FUNCTION MAPPING REQUIRED | account/wizard/accrued_orders.py:384 | move = self.env | FACT | always | — | Accrued orders wizard creates and posts an accrual entry and its reversal. | N-U11-187 |
| VDR-U11-C410 | FUNCTION MAPPING REQUIRED | account/models/company.py:950 | self.account_opening_move_id = self.env | FACT | always | — | Company opening-balance setup creates the opening entry. | N-U11-189 |
| VDR-U11-C411 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7109 | def message_new | FACT | always | — | Incoming mail on a journal alias creates an entry (invoice, bill or entry) through message_new. | N-U11-189 |
| VDR-U11-C412 | FUNCTION MAPPING REQUIRED | account/models/account_journal.py:1101 | def _create_document_from_attachment | FACT | always | — | Uploading documents creates entries via _create_records_from_attachments in the selected or first journal of the right type. | N-U11-189 |
| VDR-U11-C413 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3894 | def create | FACT | always | — | Every creation path ends in account.move create (balance check, dynamic-line sync). | N-U11-192 |
| VDR-U11-C414 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | Multi-company behaviour with more than one company cannot be confirmed from the single-company restored DB; needs a multi-company runtime test. | N-U11-194 |
| VDR-U11-C415 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:176 | comodel_name='res.company' | INFERENCE | always | — | company_id of the entry is a stored computed field, indexed, precomputed and writable; the document family derives from it (am:176-181). | N-U11-180 |
| VDR-U11-C416 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1547 | salesperson must be able | INFERENCE | sale installed | — | Comment: salesperson must be able to invoice without billing rights, hence creation in sudo; INFERENCE of why automatic creation keeps operations and accounting in step. | N-U11-181 |
| VDR-U11-C417 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1550 | sudo().with_context | INFERENCE | sale installed | — | Automatically created invoices are created in superuser mode but then follow the common creation, validation and posting rules. | N-U11-188 |
| VDR-U11-C418 | FUNCTION MAPPING REQUIRED | account_payment_interco/models/account_move.py:11 | account_interco_clearing_journal_id | FACT | account_payment_interco installed | — | Intercompany clearing runs only when the invoice company has a clearing journal and interco receivable or payable accounts are configured on both companies. | N-U11-190 |
| VDR-U11-C419 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_post_wizard.py:56 | moves_sudo | INFERENCE | hr_expense installed | — | Several non-account modules create entries; they are outside this unit and listed as supporting modules only. | N-U11-191 |
| VDR-U11-C420 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1572 | .sudo().create | INFERENCE | hr_expense installed | — | Callers using sudo creation bypass user-level access checks; errors in those callers could create entries the user could not create directly. | N-U11-193 |
