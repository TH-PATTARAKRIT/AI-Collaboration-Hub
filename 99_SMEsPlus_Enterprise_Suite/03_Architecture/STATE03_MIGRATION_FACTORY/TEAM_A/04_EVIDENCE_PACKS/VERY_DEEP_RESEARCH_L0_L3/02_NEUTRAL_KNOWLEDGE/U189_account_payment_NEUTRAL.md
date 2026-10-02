# U189 Neutral Knowledge — account.payment (Odoo 19 Community)

## Overview

The `account.payment` model is the core record for customer receipts and vendor payments in Odoo 19 Community. It maintains its own lifecycle state machine, creates a matching double-entry journal entry on confirmation, and links back to invoices through the partial reconciliation mechanism.

---

## VDR Claims Table (22 claims)

| # | Claim ID | Topic | Layer | Claim (plain language) | Code Evidence | Verified |
|---|---|---|---|---|---|---|
| 1 | U189-C01 | Model identity | L0 | The payment model technical name is `account.payment`; it inherits mail thread and activity mixin for chatter and attachments | `_name = 'account.payment'`; `_inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']` (line 7–9) | YES |
| 2 | U189-C02 | payment_type field | L1 | A payment may be inbound (money received, e.g. customer payment) or outbound (money sent, e.g. vendor payment); no other values exist in the core model | `payment_type = fields.Selection([('outbound','Send'),('inbound','Receive')], default='inbound')` (line 99–102) | YES |
| 3 | U189-C03 | partner_type field | L1 | Partner type distinguishes customer-facing flows from supplier-facing flows and drives which receivable or payable account is used as the counterpart | `partner_type = fields.Selection([('customer','Customer'),('supplier','Vendor')], default='customer')` (line 103–106) | YES |
| 4 | U189-C04 | State machine — values | L1 | In Odoo 19 the payment state machine has five values: draft, in_process, paid, canceled, rejected; this differs from earlier versions where state was delegated to the journal entry | `state = fields.Selection([('draft','Draft'),('in_process','In Process'),('paid','Paid'),('canceled','Canceled'),('rejected','Rejected')])` (line 36–49) | YES |
| 5 | U189-C05 | State machine — confirmation | L2 | Calling action_post() runs a partner-bank guard, immediately marks cash-account payments as paid, and otherwise sets state to in_process; the write() override then creates the journal entry and posts it | `action_post()` line 1130–1148; `write()` override line 951–959 | YES |
| 6 | U189-C06 | State machine — auto-advance | L2 | The computed _compute_state() method automatically advances in_process to paid when the sum of liquidity-line residuals reaches zero, or when all linked invoices reach payment_state paid | `_compute_state()` line 455–471 | YES |
| 7 | U189-C07 | outstanding_account_id | L2 | The outstanding account (also called the transit or clearing account) is taken from the payment method line's payment_account_id; in Community with no payment method line set, a fallback resolves it from the chart-template debit/credit references | `_compute_outstanding_account_id()` line 624–627; `_get_outstanding_account()` line 940–949 | YES |
| 8 | U189-C08 | Journal entry — liquidity line | L3 | The liquidity journal entry line is posted to the outstanding account; for an inbound payment the amount is positive (debit), for outbound it is negative (credit) | `_prepare_move_liquidity_lines()` line 288–298; `_prepare_move_lines_per_type()` line 350–376 | YES |
| 9 | U189-C09 | Journal entry — counterpart line | L3 | The counterpart journal entry line uses the destination account (receivable for customer payments, payable for vendor payments); its amount is the mirror of the liquidity line | `_prepare_move_counterpart_lines()` line 300–310; `counterpart_balance = -liquidity_balance - ...` line 380 | YES |
| 10 | U189-C10 | destination_account_id computation | L2 | The destination account is the partner's property_account_receivable_id for customer flows and property_account_payable_id for supplier flows; falls back to a company-level account search when no partner is set | `_compute_destination_account_id()` line 629–650 | YES |
| 11 | U189-C11 | Move generation | L3 | The actual account.move (journal entry) is created by _generate_journal_entry() → _generate_move_vals(); the move has move_type='entry' and origin_payment_id pointing back to the payment | `_generate_move_vals()` line 1085–1105; `origin_payment_id` field line 207 in account_move.py | YES |
| 12 | U189-C12 | action_cancel behavior | L2 | Cancellation sets payment state to canceled, deletes any draft journal entry, and calls button_cancel() on already-posted entries (which in Odoo 19 creates a reversal) | `action_cancel()` line 1156–1160 | YES |
| 13 | U189-C13 | is_matched field | L2 | is_matched is true when the liquidity account lines carry zero residual amount, meaning the payment has been matched to a bank statement line; if the journal uses its own default account directly, is_matched is always true | `_compute_reconciliation_status()` line 473–501 | YES |
| 14 | U189-C14 | is_reconciled field | L2 | is_reconciled is true when all counterpart and write-off lines pointing to reconcilable accounts carry zero residual, meaning the payment has been applied (at least partially) to an invoice | `_compute_reconciliation_status()` line 499–501 | YES |
| 15 | U189-C15 | payment_state on invoice — values | L1 | The payment_state field on account.move (invoice) has seven possible values: not_paid, in_payment, paid, partial, reversed, blocked, invoicing_legacy | `PAYMENT_STATE_SELECTION` line 49–57 in account_move.py | YES |
| 16 | U189-C16 | payment_state on invoice — Community behavior | L2 | In Community edition _get_invoice_in_payment_state() always returns 'paid', so invoices jump directly from partial/in_process to paid without passing through in_payment; the in_payment state is only activated by the account_accountant module (Enterprise) | `_get_invoice_in_payment_state()` line 7367–7371 in account_move.py | YES |
| 17 | U189-C17 | _compute_payment_state SQL logic | L3 | The invoice payment_state is derived by a raw SQL query across account.partial.reconcile to find all reconciled counterpart moves; zero residual with payment/statement matches → paid (Community) or in_payment (Enterprise); partial matches → partial; credit note reversal → reversed | `_compute_payment_state()` line 1234–1326 in account_move.py | YES |
| 18 | U189-C18 | Reconciliation chain to invoice | L3 | The link between a payment and its invoices is maintained through account.partial.reconcile records joining the payment's receivable/payable line to the invoice's receivable/payable line; this SQL join is executed in _compute_stat_buttons_from_reconciliation() | `_compute_stat_buttons_from_reconciliation()` line 680–773 | YES |
| 19 | U189-C19 | Multi-currency — field layout | L2 | currency_id (the payment's own currency) and company_currency_id (company base currency) are separate fields; when they differ, journal lines carry amount_currency (payment currency) and balance (company currency), and the accounting engine auto-generates FX gain/loss entries | `currency_id` line 110–114; `company_currency_id` line 115; conversion at line 363–368 | YES |
| 20 | U189-C20 | Multi-currency — FX conversion | L3 | The liquidity balance in company currency is computed via currency_id._convert(amount_currency, company_currency, company, date) at the time the journal entry is built; the rate comes from the res.currency.rate table for that date | `liquidity_balance = self.currency_id._convert(...)` line 363–368 | YES |
| 21 | U189-C21 | Synchronization draft moves | L3 | Changes to key payment fields (amount, date, partner_id, currency_id, journal_id, etc.) are automatically propagated to a still-draft journal entry via _synchronize_to_moves(); posted moves are explicitly skipped | `_synchronize_to_moves()` line 999–1064; trigger fields line 1067–1071; guard line 1008 | YES |
| 22 | U189-C22 | Community outstanding account auto-set | L2 | In Community mode (without account_accountant), if outstanding_account_id is not populated via payment method line, create() automatically resolves and sets it from the chart template; this ensures a journal entry can always be generated | `create()` line 912–919; `_get_outstanding_account()` line 940–949 | YES |

---

## Key Architecture Patterns

### Dual-line journal entry per payment
Every posted payment produces exactly one `account.move` of type `entry` with:
- **Liquidity line**: outstanding (transit) account — the "in-transit" side
- **Counterpart line**: receivable or payable — the "partner debt" side

### Reconciliation chain
```
Invoice (account.move)
  └─ receivable/payable line (account.move.line)
       └─ account.partial.reconcile ──▶ payment's counterpart line (account.move.line)
                                           └─ account.move (payment entry)
                                                └─ liquidity line ──▶ bank statement line
                                                                        (is_matched = True)
```

### Community vs Enterprise
| Aspect | Community | Enterprise (account_accountant) |
|---|---|---|
| `in_payment` state on invoice | Never shown; jumps to `paid` | Shown while liquidity line unmatched |
| `_get_invoice_in_payment_state()` | Returns `'paid'` | Returns `'in_payment'` |
| Payment state validation | `['in_process', 'paid']` | `['in_process']` |

---

## Migration Risk Notes

1. **State machine changed**: v16/v17 used `draft/posted/cancel` on `account.move` as the primary state; v19 adds its own `draft/in_process/paid/canceled/rejected` on `account.payment`. Any migration code that reads `payment.move_id.state == 'posted'` may need to be updated to check `payment.state in ('in_process', 'paid')`.
2. **outstanding_account_id required**: If a custom payment flow bypasses payment method lines, the outstanding account may not be set. Community mode has a fallback but it relies on the chart template being present.
3. **No direct cancel reversal entry**: `action_cancel()` calls `button_cancel()` on the move; it does not create its own reversal — that is delegated to the move's cancel logic.
4. **FX rate at posting time**: The balance is locked at `self.date` when the entry is first created; changing the date later (while still draft) triggers `_synchronize_to_moves()` and recomputes the balance at the new date.
