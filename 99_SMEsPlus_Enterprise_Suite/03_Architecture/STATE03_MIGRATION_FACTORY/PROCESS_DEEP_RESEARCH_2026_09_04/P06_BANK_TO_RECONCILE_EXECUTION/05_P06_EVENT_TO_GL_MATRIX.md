# P06_EVENT_TO_GL_MATRIX.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Invariant under test:** ONE FACT → ONE OWNER → ONE ACCOUNTING EFFECT

---

## 1. The account-determination chain, and what happens when it is unset

This is the spine of the matrix. Every row below resolves an account through one of these five chains.

| Leg | Chain | If unset |
|---|---|---|
| **Outstanding receipts / payments** | `account.payment.method.line.payment_account_id` **only** — `$V18E/account/models/account_payment.py:585-589` is a pure passthrough with no company fallback | **UserError** at `:305-308` |
| Outstanding, *community-edition path only* | chart-template XML ref → `company.transfer_account_id` → error — `$V18E/account/models/account_payment.py:899-908`, reached only when `_get_invoice_in_payment_state() != 'in_payment'` (`:873-878`) | **UserError** |
| **Bank liquidity** | `journal.default_account_id` | **silent `False`** on a statement line (`$V18E/account/models/account_bank_statement_line.py:670-674` — unguarded); auto-created at journal creation (`$V18E/account/models/account_journal.py:833-834`) |
| **Suspense** | `journal.suspense_account_id` → `company.account_journal_suspense_account_id` → `False` — `$V18E/account/models/account_journal.py:419-429` | silent `False` at journal level, then **UserError** at statement-line create (`$V18E/account/models/account_bank_statement_line.py:645-652`) |
| **Destination (AR/AP)** | partner property → first matching non-deprecated account of the type — `$V18E/account/models/account_payment.py:598-604` | **silent `False`** — no error branch |

**EGL-F-01 — Two of the five chains fail silently to `False`.** Bank liquidity on a statement line, and the AR/AP destination. A journal item with `account_id = False` is not a business error the system reports; it is a value it accepts.

**EGL-F-02 — There is no company-level default outstanding receipts/payments account.**
NOT FOUND in `$V18E/account/models/company.py`, PATTERN `outstanding|suspense|exchange|currency_exchange` — the only company-level payment landing account is `transfer_account_id`, and it is reachable only on the community path. **Class A within that file's scope.**
**Consequence:** outstanding-account determination is entirely per-payment-method-line. In a 12-bank-journal estate (runtime finding CPO-F-04) that is at least 12 configuration points with no fallback and no consistency check.

**EGL-F-03 — Assigning a payment account silently mutates the target account's `reconcile` flag.**
`$V18E/account/models/account_payment_method.py:170-186`:
```
if not account.reconcile and account.account_type not in ('asset_cash', 'liability_credit_card', 'off_balance'):
    account.reconcile = True
```
A configuration write changes the reconcilability of a general-ledger account, on create **and** on write. This is the second place in the system where chart-of-accounts configuration is mutated as a side effect (the first is RM-F-26).

---

## 2. The matrix

Notation: `Dr` / `Cr`. "Silent" means the reference produces the entry with no error and no flag.

### 2.1 Customer receipt

| # | Event | Entry | Account source | Notes |
|---|---|---|---|---|
| G-01 | Payment registered against a customer invoice | Dr Outstanding Receipts · Cr Receivable | method line · partner property | `$V18E/account/models/account_payment.py:352,354-364` |
| G-02 | Bank statement line ingested | Dr Bank · Cr Suspense | journal default · journal suspense | `$V18E/account/models/account_bank_statement_line.py:645-674` |
| G-03 | Statement line matched to the payment | suspense line **destroyed**, replaced by Cr Outstanding Receipts | — | RM-F-01; the outstanding account nets to zero |
| G-04 | Receipt matched directly to the invoice (no payment record) | suspense replaced by Cr Receivable | partner property | bank-rec widget `new_aml` flow |
| G-05 | **Payment posted with cash-type outstanding account** | as G-01, but `state` jumps straight to `paid` | — | `$V18E/account/models/account_payment.py:1067-1068` — no bank event required |

### 2.2 Vendor payment

| # | Event | Entry | Notes |
|---|---|---|---|
| G-06 | Payment registered against a vendor bill | Dr Payable · Cr Outstanding Payments | mirror of G-01 |
| G-07 | Cheque printed | **no entry** | printing writes `is_sent` and `check_number` only — `$V18E/account_check_printing/models/account_payment.py:145-150,207` |
| G-08 | Cheque voided | reset to draft, then cancel | `$V18E/account_check_printing/models/account_payment.py:195-197` — see EGL-F-08 |
| G-09 | Batch validated and sent | **no entry** | `is_sent` flag only — SSM-F-05 |

### 2.3 Employee payment

| # | Event | Entry | Notes |
|---|---|---|---|
| G-10 | Expense paid by employee (`own_account`) | vendor bill → normal AP path | `$V18E/hr_expense/models/hr_expense_sheet.py:746-773` |
| G-11 | Expense paid by company (`company_account`) | move created **first**, payment injected with `move_id` | same file; **the outstanding account is overridden to the expense destination account** — `$V18E/hr_expense/models/account_payment.py:13-18` |
| G-12 | Payroll settlement | payslip move, then the standard register wizard | `$V18E/hr_payroll_account/models/hr_payslip.py:249-252`; valid counterpart types widened to include `liability_current` **by view context** — `$V18E/hr_payroll_account/models/account_payment.py:10-15` |
| G-13 | Petty cash (custom) | `payment.write({'move_id': move.id, 'state': 'in_process'})` — **direct state write** | `$CUST18/hr_expense_petty_cash/models/hr_expense_sheet.py:117`; account and partner rewritten on the journal item at `models/hr_expense.py:76-77` |

### 2.4 Internal and intercompany transfer

| # | Event | Entry | Notes |
|---|---|---|---|
| G-14 | Transfer out of Bank A | Dr Inter-Banks Transfer · Cr Bank A | via the seeded `internal_transfer_reco` write-off model — `$V18E/account/models/chart_template.py:1149-1158,724-727` |
| G-15 | Transfer into Bank B | Dr Bank B · Cr Inter-Banks Transfer | same mechanism, applied to the second statement line |
| G-16 | Intercompany settlement | two independent, **unlinked** payments | `account_inter_company_rules` covers invoices/credit notes only — see EGL-F-09 |

### 2.5 Differences, fees and adjustments

| # | Event | Entry | Account source | Notes |
|---|---|---|---|---|
| G-17 | Realised FX gain | Dr aml account · Cr `company.income_currency_exchange_account_id` | company | `$V18E/account/models/account_move_line.py:2721-2724,2779-2795` |
| G-18 | Realised FX loss | mirror, `expense_currency_exchange_account_id` | company | same |
| G-19 | Bank charge | **no first-class mechanism** — a generic write-off line | free choice | see the FX/Fee/Interest Matrix |
| G-20 | Bank interest received | **no first-class mechanism** | free choice | same |
| G-21 | Provider settlement fee | **not modelled at all in v18** | — | same |
| G-22 | Tolerated shortfall | write-off line per the reconcile model | model line account, **may be omitted entirely** | `$V18E/account_accountant/models/account_reconcile_model_line.py:53-55` |
| G-23 | Manual write-off at payment registration | Dr/Cr `writeoff_account_id` | free choice, **no account-type domain** | `$V18E/account/wizard/account_payment_register.py:140-148` — domain is only `[('deprecated','=',False)]` |
| G-24 | Early payment discount | `account_journal_early_pay_discount_loss_account_id` (inbound) / `..._gain_account_id` (outbound) | company | `$V18E/account/models/account_move.py:4401-4404` |
| G-25 | Cash-basis tax recognition | CABA journal; base account chain `company.account_cash_basis_base_account_id` → the line's own account | company → line | `$V18E/account/models/account_partial_reconcile.py:335,400` |
| G-26 | Cash till over/short | `journal.profit_account_id` / `loss_account_id`, defaulted from `company.default_cash_difference_*` | company | `$V18E/account/models/account_journal.py:835-838` |
| G-27 | Customer advance / down payment | product `downpayment` account, falling back to plain **income** | product | `$V18E/sale/wizard/sale_make_invoice_advance.py:252-253` |
| G-28 | Vendor advance (custom) | **the product's EXPENSE account** | product | `$CUST18/scgl_purchase_advance_payment/wizard/purchase_advance.py:21-22,93` — see EGL-F-10 |
| G-29 | Employee advance (custom) | request line account, defaulted from the product expense account | request line | `$CUST18/scgl_advance_expense_request/models/advance_expense_request_line.py:131` and `models/account_move.py:89-90` |
| G-30 | Unidentified receipt | Dr Bank · Cr Suspense, and it stays there | journal suspense | see EGL-F-06 |
| G-31 | Opening plug on first bank sync | a posted statement line for `balance - total` | journal default / suspense | `$V18E/account_online_synchronization/models/account_bank_statement.py:77-83` |

**Row count: 31.** **DENOMINATOR:** POPULATION: the event list enumerated in the P06 directive plus events discovered during evidence gathering. PATTERN: for each event, the account-assignment site in the S-01/S-02 path set. UNIT: event→entry pair. **This is not a claim to have enumerated every possible journal entry in the system** — it is the P06 event set as declared. Class B for anything outside it.

---

## 3. Findings on ownership and single-effect

**EGL-F-04 — Three of the thirty-one rows have no account owner at all.**
G-19, G-20 and G-21 (bank charge, bank interest, provider fee) resolve to "whatever the user typed into a write-off line." There is no configuration point, no default, and no report that groups them. **For a treasury process these are the three most frequent non-settlement bank events.** Raised as `P06-B-17`.

**EGL-F-05 — Write-off accounts are unconstrained by type.**
`$V18E/account/wizard/account_payment_register.py:143` — `domain="[('deprecated', '=', False)]"`. A settlement difference can be posted to any account in the chart, including another bank account, a control account, or an equity account. The reconcile-model route is weaker still: if the model line's account is unset the key is simply **omitted** from the values dict (`$V18E/account_accountant/models/account_reconcile_model_line.py:53-55`), producing an aml with no `account_id` key.
**NOT FOUND: any approval or limit control on write-off amount.** Three independent search scopes returned zero (see the Edge Case Matrix, E5). **Class A within those declared scopes.** The only gate is generic accounting-group membership plus lock dates.

**EGL-F-06 — Unidentified money has a home but no clock.**
The suspense account is correctly forced and its absence is a hard stop (`$V18E/account/models/account_bank_statement_line.py:645-652`), and it is domain-restricted to `asset_current` (`$V18E/account/models/account_journal.py:121`).
**But there is no ageing over it.** PATTERN `-i suspense` over `$V18E/account_reports`: **7 hits, all in `account_reports/tests/test_reconciliation_report.py`. Non-test hits = 0.** And the ageing report is structurally incapable of covering it: `$V18E/account_reports/models/account_aged_partner_balance.py:156` scopes by `account_id.account_type`, and `internal_type` is only ever `asset_receivable` or `liability_payable` (`:85,88`).
**Class A within `$V18E/account_reports`.** Whether a custom report in the SMEsPlus trees does this was **not searched** — Class C.
**Consequence:** money the business cannot identify accumulates in an `asset_current` account that no standard ageing report can see. Raised as `P06-B-18`.

**EGL-F-07 — The transit account for internal transfers is subject to the same blindness.**
`company.transfer_account_id` is domain-forced to `asset_current` and `reconcile = True` (`$V18E/account/models/company.py:110-112`). A non-zero balance there is the **only** control that both legs of a transfer were captured — and it is in the same reporting blind spot as the suspense account. Combined with the finding that nothing links the two legs (PSM-F-24), single-sided transfers are detectable only by someone looking directly at the account.

**EGL-F-08 — A voided cheque number returns to the pool.**
`$V18E/account_check_printing/models/account_payment.py:195-197` — `action_void_check` is `action_draft()` then `action_cancel()`. There is no `voided` state and no stop-list. The uniqueness constraint spans **posted moves only** (`:74-77`: `AND move.state = 'posted' AND other_move.state = 'posted'`), so a cancelled cheque number can be silently re-issued. Raised as `P06-B-19`.

**EGL-F-09 — Intercompany money in transit has no carrier.**
`$V18E/account_inter_company_rules/__manifest__.py:9` — *"Supported documents are invoices/credit notes."* PATTERN `-i payment` over that module's py+xml excluding tests: **2 hits, both incidental invoice fields** (`models/account_move.py:95,99`). PATTERN `account\.payment` over the whole module: hits only in stale `/i18n/*.po` catalogue entries with no corresponding Python.
**Class A within that module's declared scope.** An intercompany settlement produces two unlinked payments; matching them is manual. Raised as `P06-B-20`.

**EGL-F-10 — The custom vendor-advance module posts an advance to a profit-and-loss expense account.**
`$CUST18/scgl_purchase_advance_payment/wizard/purchase_advance.py:21-22`:
```
def _default_deposit_account_id(self):
    return self._default_product_id()._get_product_accounts()['expense']
```
and it writes that account onto the product template at `:93` (`'property_account_expense_id': self.deposit_account_id.id`). Unlike the sale-side path (G-27), there is **no `downpayment` or prepayment-asset fallback**.
**Stated precisely: the module's default resolves to the product's expense account. Whether the live configuration points that product at a balance-sheet prepayment account or at a profit-and-loss expense account is a data question this session cannot answer** (source NC-01, no database access). The default configured product is a system parameter (`models/res_config_settings.py`, `config_parameter='purchase.advance_default_product_id'`).
**Classification: PLAUSIBLE DEFECT, DATA-DEPENDENT.** If the product carries a P&L expense account, a vendor advance — an asset — is expensed on payment. Routed to the Accounting-Tax track as **HOLD / EVIDENCE REQUIRED**, and raised as `P06-B-21`. This is reported as a question, not a verdict, precisely because the deciding evidence is not in the searched scope.

**EGL-F-11 — Cash-basis account determination has a three-deep silent fallback.**
`$V18E/account/models/account_partial_reconcile.py:400`:
```
'account_id': tax_line.tax_repartition_line_id.account_id.id or tax_line.company_id.account_cash_basis_base_account_id.id or tax_line.account_id.id,
```
Three candidates, no error branch. The account a cash-basis tax lands in depends on which of three configurations happens to be set.

**EGL-F-12 — Two context keys silently suppress cash-basis generation.**
`$V18E/account/models/account_move_line.py:2540-2552` — `if not self._context.get('move_reverse_cancel') and not self._context.get('no_cash_basis')`. A caller passing `no_cash_basis=True` reconciles without generating the tax entry, leaving no trace. Which callers do so on the P06 path was **not enumerated** — Class C, `P06-OQ-30`.

---

## 4. Single-accounting-effect assessment

| Fact | One owner? | One effect? | Verdict |
|---|---|---|---|
| Money arrived at the bank | no — 7 ingestion doors | yes, per line | **fails owner** |
| Obligation settled | no — payment state, invoice state and reconciliation each assert it | no — the invoice can be settled while the ledger is not | **fails both** |
| Difference on settlement | no — 6 write-off entry points | yes | **fails owner** |
| FX difference | yes — company configuration | yes | holds |
| Bank charge | **none** | — | **unowned** |
| Cash over/short | yes — journal profit/loss accounts | yes | holds |
| Advance | no — invoice-side in three modules, a first-class model in a fourth | varies by module | **fails both** |
| Transfer between own banks | **none** — no pairing record | two independent effects | **fails both** |

---

## 5. Blockers raised

| ID | Blocker |
|---|---|
| P06-B-17 | Bank charges, bank interest and provider fees have no account owner and no mechanism beyond a free-form write-off. |
| P06-B-18 | Suspense and transit balances are outside every standard ageing report; unidentified money has no clock. |
| P06-B-19 | A voided cheque number returns to the pool; the uniqueness constraint covers posted moves only. |
| P06-B-20 | Intercompany money in transit has no carrier object and no automatic matching. |
| P06-B-21 | The custom vendor-advance path defaults to the product's expense account with no prepayment-asset fallback. **HOLD / EVIDENCE REQUIRED** — data-dependent, routed to Accounting-Tax. |
| P06-B-22 | Write-off accounts are unconstrained by type and unconstrained by amount, with no approval control. |
| P06-B-23 | Two account-determination chains fail silently to `False`. |
| P06-B-24 | Two separate code paths mutate chart-of-accounts configuration as a side effect of a data or configuration operation. |

---

# End
