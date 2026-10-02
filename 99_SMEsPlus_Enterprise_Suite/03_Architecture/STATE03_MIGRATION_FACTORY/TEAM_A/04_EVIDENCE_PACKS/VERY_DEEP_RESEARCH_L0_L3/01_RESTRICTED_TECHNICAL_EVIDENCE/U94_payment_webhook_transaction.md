# U94 — Payment Provider Webhook → Transaction State → Account Move (L3/L8)
**Unit**: U94
**Phase**: Second-Pass Depth Closure — P2 Supporting Domains
**Scope**: payment.transaction state machine, webhook processing, account.move creation from confirmed payment
**Modules**: payment, payment_stripe (present), payment_paypal (present)
**Function-IDs targeted**: NEW:U94-F01 through U94-F30
**L-levels**: L3, L8
**Proof layers**: P2, P3
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: U20, U63

---

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U94-001 | U94-F01 | payment/models/payment_transaction.py:65 | `state = fields.Selection(` | SCHEMA | always | | `payment.transaction.state` is a Selection field with six values: draft, pending, authorized, done, cancel, error; default is 'draft' | NR-U94-001 |
| U94-002 | U94-F02 | payment/models/payment_transaction.py:69 | `default='draft', readonly=True` | CONST | always | | State field is readonly with copy=False and index=True; state changes must go through the state-setter methods | NR-U94-002 |
| U94-003 | U94-F03 | payment/models/payment_transaction.py:738 | `def _process(self, provider_code,` | DEF | always | | `_process()` is the single entry point for all payment data received from providers; it orchestrates reference lookup, amount validation, state update, and tokenisation | NR-U94-003 |
| U94-004 | U94-F04 | payment/models/payment_transaction.py:746 | `tx = self or self._search_by_reference` | CALL | when self is empty recordset | | `_process` calls `_search_by_reference` to locate the transaction by provider code and payment data when no transaction record is already bound | NR-U94-004 |
| U94-005 | U94-F05 | payment/models/payment_transaction.py:750 | `tx._validate_amount(payment_data)` | CALL | after tx found | | `_process` calls `_validate_amount` to verify the provider-reported amount and currency match the stored transaction values before any state change | NR-U94-005 |
| U94-006 | U94-F06 | payment/models/payment_transaction.py:753 | `tx._apply_updates(payment_data)` | CALL | when state is not 'error' after validation | | `_process` calls `_apply_updates`; provider-specific overrides of `_apply_updates` implement the actual state transitions by calling `_set_pending`, `_set_authorized`, `_set_done`, etc. | NR-U94-006 |
| U94-007 | U94-F07 | payment/models/payment_transaction.py:915 | `def _set_pending(self, *, state_message=` | DEF | allowed source: draft | | `_set_pending()` transitions state from 'draft' to 'pending'; calls `_update_state` then `_log_received_message` | NR-U94-007 |
| U94-008 | U94-F08 | payment/models/payment_transaction.py:932 | `def _set_authorized(self, *, state_message=` | DEF | allowed source: draft, pending | | `_set_authorized()` transitions state to 'authorized'; allowed source states are draft and pending | NR-U94-008 |
| U94-009 | U94-F09 | payment/models/payment_transaction.py:949 | `def _set_done(self, *, state_message=` | DEF | allowed source: draft, pending, authorized, error | | `_set_done()` transitions state to 'done'; additionally calls `_update_source_transaction_state` to propagate completion to parent transactions | NR-U94-009 |
| U94-010 | U94-F10 | payment/models/payment_transaction.py:964 | `txs_to_process._update_source_transaction_state` | CALL | inside _set_done | | `_set_done` calls `_update_source_transaction_state` after logging, which updates the parent transaction state when all child partial-capture/void transactions have finalised | NR-U94-010 |
| U94-011 | U94-F11 | payment/models/payment_transaction.py:967 | `def _set_canceled(self, state_message=None` | DEF | allowed source: draft, pending, authorized | | `_set_canceled()` transitions state to 'cancel'; also calls `_update_source_transaction_state` | NR-U94-011 |
| U94-012 | U94-F12 | payment/models/payment_transaction.py:985 | `def _set_error(self, state_message, extra` | DEF | allowed source: draft, pending, authorized | | `_set_error()` transitions state to 'error'; allowed source states are draft, pending, authorized | NR-U94-012 |
| U94-013 | U94-F13 | payment/models/payment_transaction.py:1052 | `txs_to_process.write({` | ASSIGN | when state is in allowed_states | | `_update_state` writes state, state_message, last_state_change (Datetime.now()), and resets is_post_processed to False in a single ORM write call | NR-U94-013 |
| U94-014 | U94-F14 | payment/models/payment_transaction.py:1112 | `def _post_process(self):` | DEF | always | | Core `_post_process()` only sets `self.is_post_processed = True`; it is a hook for extension by other modules | NR-U94-014 |
| U94-015 | U94-F15 | payment/models/payment_transaction.py:1082 | `def _cron_post_process(self):` | DEF | cron | | `_cron_post_process` scheduled method picks all transactions where is_post_processed=False and last_state_change >= 4-day retry limit, then calls `_post_process()` per transaction | NR-U94-015 |
| U94-016 | U94-F16 | account_payment/models/payment_transaction.py:7 | `_inherit = 'payment.transaction'` | INHERIT | always | | `account_payment` extends `payment.transaction` adding accounting fields: `payment_id` (Many2one to account.payment) and `invoice_ids` (Many2many to account.move) | NR-U94-016 |
| U94-017 | U94-F17 | account_payment/models/payment_transaction.py:9 | `payment_id = fields.Many2one(` | SCHEMA | always | | `payment_id` is a Many2one field linking `payment.transaction` to `account.payment`; it is readonly and set only after payment creation in post-processing | NR-U94-017 |
| U94-018 | U94-F18 | account_payment/models/payment_transaction.py:12 | `invoice_ids = fields.Many2many(` | SCHEMA | always | | `invoice_ids` is a Many2many field linking `payment.transaction` to `account.move` via the `account_invoice_transaction_rel` table (columns: transaction_id, invoice_id) | NR-U94-018 |
| U94-019 | U94-F19 | account_payment/models/payment_transaction.py:98 | `def _post_process(self):` | OVERRIDE | always | | `account_payment` overrides `_post_process()`: for 'done' transactions it validates draft invoices, then calls `_create_payment()` if no payment exists and no child transactions have finalised | NR-U94-019 |
| U94-020 | U94-F20 | account_payment/models/payment_transaction.py:121 | `tx.with_company(tx.company_id)._create_payment()` | CALL | state=='done', operation!='validation', no existing payment_id, no finalised children | | `_post_process` calls `_create_payment()` in the company context; this is the single path from a confirmed payment transaction to `account.payment` / `account.move` creation | NR-U94-020 |
| U94-021 | U94-F21 | account_payment/models/payment_transaction.py:133 | `def _create_payment(self, **extra_create_values):` | DEF | always | | `_create_payment()` builds a full `account.payment` create-values dict from transaction data (amount, currency, partner, journal, payment method line, memo, invoice_ids) then creates and posts the payment | NR-U94-021 |
| U94-022 | U94-F22 | account_payment/models/payment_transaction.py:191 | `payment = self.env['account.payment'].create(payment_values)` | CALL | always in _create_payment | | `account.payment` is created via `self.env['account.payment'].create(payment_values)`; this triggers the ORM create which generates the underlying `account.move` journal entry | NR-U94-022 |
| U94-023 | U94-F23 | account_payment/models/payment_transaction.py:192 | `payment.action_post()` | CALL | after create | | `payment.action_post()` is called immediately after creating the payment, posting the account.move journal entry to confirm the payment accounting | NR-U94-023 |
| U94-024 | U94-F24 | account_payment/models/payment_transaction.py:195 | `self.payment_id = payment` | ASSIGN | after action_post | | The `payment_id` field on the transaction is set to the new `account.payment` record after posting, creating the one-to-one link | NR-U94-024 |
| U94-025 | U94-F25 | account_payment/models/payment_transaction.py:206 | `(payment.move_id.line_ids + invoices.line_ids).filtered(` | CALL | when invoice_ids present | | Reconciliation is performed by filtering payment and invoice move lines by destination account and calling `.reconcile()` on the combined line recordset | NR-U94-025 |
| U94-026 | U94-F26 | payment_stripe/controllers/main.py:25 | `_webhook_url = '/payment/stripe/webhook'` | CONST | always | | Stripe webhook is registered at the URL `/payment/stripe/webhook`; return URL is `/payment/stripe/return` | NR-U94-026 |
| U94-027 | U94-F27 | payment_stripe/controllers/main.py:69 | `@http.route(_webhook_url, type='http', methods=['POST']` | DEF | POST request | | `stripe_webhook()` route handles incoming Stripe webhook events; it parses the JSON event, verifies the HMAC signature, then calls `tx_sudo._process('stripe', data)` | NR-U94-027 |
| U94-028 | U94-F28 | payment_stripe/controllers/main.py:152 | `tx_sudo._process('stripe', data)` | CALL | after signature verification | | Stripe webhook delegates transaction state update to the core `_process()` method; Stripe-specific `_apply_updates` override then maps intent status to state setter calls | NR-U94-028 |
| U94-029 | U94-F29 | payment_stripe/models/payment_transaction.py:326 | `def _apply_updates(self, payment_data):` | OVERRIDE | provider_code=='stripe' | | Stripe `_apply_updates` maps Stripe intent status strings to Odoo state setters using `const.STATUS_MAPPING`; 'succeeded' → `_set_done()`, 'requires_capture' → `_set_authorized()`, 'processing'/'pending' → `_set_pending()`, 'canceled' → `_set_canceled()` | NR-U94-029 |
| U94-030 | U94-F30 | payment_stripe/const.py:61 | `STATUS_MAPPING = {` | CONST | always | | Stripe `STATUS_MAPPING` dict: draft→('requires_confirmation','requires_action'), pending→('processing','pending'), authorized→('requires_capture',), done→('succeeded',), cancel→('canceled',), error→('requires_payment_method','failed') | NR-U94-030 |
| U94-031 | U94-F31 | payment_stripe/const.py:71 | `HANDLED_WEBHOOK_EVENTS = [` | CONST | always | | Stripe HANDLED_WEBHOOK_EVENTS includes: payment_intent.processing, payment_intent.amount_capturable_updated, payment_intent.succeeded, payment_intent.payment_failed, payment_intent.canceled, setup_intent.succeeded, charge.refunded, charge.refund.updated | NR-U94-031 |
| U94-032 | U94-F32 | payment_paypal/controllers/main.py:21 | `_webhook_url = '/payment/paypal/webhook/'` | CONST | always | | PayPal webhook is registered at `/payment/paypal/webhook/`; the PayPal controller also exposes `/payment/paypal/complete_order` for the capture flow | NR-U94-032 |
| U94-033 | U94-F33 | payment_paypal/controllers/main.py:48 | `@http.route(_webhook_url, type='http', methods=['POST']` | DEF | POST request | | `paypal_webhook()` route handles PayPal webhook events; it normalises the PayPal payload, verifies notification origin via PayPal API, then calls `tx_sudo._process('paypal', normalized_data)` | NR-U94-033 |
| U94-034 | U94-F34 | payment_paypal/models/payment_transaction.py:125 | `def _apply_updates(self, payment_data):` | OVERRIDE | provider_code=='paypal' | | PayPal `_apply_updates` maps PayPal order status from `PAYMENT_STATUS_MAPPING` to state setters: pending→`_set_pending()`, done→`_set_done()`, cancel→`_set_canceled()`; unrecognised status → `_set_error()` | NR-U94-034 |
| U94-035 | U94-F35 | payment/controllers/post_processing.py:41 | `@http.route('/payment/status/poll'` | DEF | jsonrpc | | The `/payment/status/poll` JSONRPC endpoint calls `monitored_tx._post_process()` client-side; this is the browser-triggered path that runs post-processing in parallel to the cron | NR-U94-035 |

---

## Module Presence Confirmation

Both `payment_stripe` and `payment_paypal` are present in Odoo 19.0 Community addons.
Confirmed by direct `ls` of addons root.

---

## Key Data Flow Summary

```
Provider webhook POST
  └─> StripeController.stripe_webhook()  /payment/stripe/webhook
      └─> _search_by_reference('stripe', data)
      └─> _verify_signature()
      └─> tx._process('stripe', data)            ← core entry point
              └─> _validate_amount(payment_data)
              └─> _apply_updates(payment_data)    ← Stripe override
                      └─> STATUS_MAPPING lookup
                      └─> _set_done() / _set_authorized() / _set_pending() / _set_canceled() / _set_error()
                              └─> _update_state() → write({'state': target_state, ...})

Post-processing (browser poll or cron):
  tx._post_process()                             ← account_payment override
      └─> invoice_ids.action_post()              ← validate draft invoices
      └─> tx._create_payment()
              └─> account.payment.create(payment_values)  ← creates account.move
              └─> payment.action_post()          ← posts journal entry
              └─> self.payment_id = payment      ← links tx to payment
              └─> reconcile()                    ← matches payment lines to invoice lines
```
