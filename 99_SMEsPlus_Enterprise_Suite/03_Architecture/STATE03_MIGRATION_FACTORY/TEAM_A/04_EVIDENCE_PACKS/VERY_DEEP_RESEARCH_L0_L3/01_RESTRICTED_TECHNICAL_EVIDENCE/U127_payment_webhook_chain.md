# U127 — Payment Provider Webhook Chain: Restricted Technical Evidence
**Unit:** U127 | **G-Group:** G03/G15 | **Priority:** P2
**Gaps:** GAP-015 (payment provider integration), GAP-041 (eCommerce payment confirmation)
**Produced:** 2026-10-02 | **Branch:** claude/local-odoo-source-research
**Source tree (READ-ONLY):** `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/`

---

## 1. Scope

SOURCE-ONLY study of the Community payment webhook chain covering:
- Base `payment` module: provider model, transaction state machine, post-processing
- `account_payment` bridge: journal entry creation and reconciliation
- `sale` bridge: sale order confirmation and auto-invoicing
- `payment_stripe`, `payment_xendit`, `payment_paypal`: representative provider webhook implementations
- `website_payment`: donation flow extension

No runtime environment. Webhook receipt, live state transitions, and account entry creation are flagged AWT.

---

## 2. Community Payment Providers Enumerated

```
payment           payment_adyen     payment_aps       payment_asiapay
payment_authorize payment_buckaroo  payment_custom    payment_demo
payment_dpo       payment_ecpay     payment_flutterwave payment_iyzico
payment_mercado_pago payment_mollie payment_nuvei     payment_paymob
payment_paypal    payment_payu      payment_razorpay  payment_redsys
payment_stripe    payment_toss_payments payment_worldline payment_xendit
account_payment   account_payment_interco pos_online_payment
pos_online_payment_self_order website_payment
```

26 payment-related modules present in Community. Each provider contributing a webhook adds its own HTTP controller under `payment_<provider>/controllers/main.py`.

---

## 3. VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|----------|-------------|---------|--------|-------|-----------|-------|--------------------|-----------| 
| U127-C001 | PaymentProvider-model-def | `payment/models/payment_provider.py:22-26` | `class PaymentProvider(models.Model)` | C1 | Always | C1 | `payment.provider` model with `_name='payment.provider'`, `_order='module_state, state desc, sequence, name'`, `_check_company_auto=True` | Base provider registry model definition in the payment module |
| U127-C002 | PaymentProvider-code-field | `payment/models/payment_provider.py:34-40` | `code = fields.Selection(selection=[('none', ...)])` | C1 | Always | C1 | `code` is an extensible Selection with default `'none'`; each provider module extends the selection with its own code value | Provider technical code field with extensible enumeration |
| U127-C003 | PaymentProvider-state-field | `payment/models/payment_provider.py:41-46` | `state = fields.Selection(selection=[('disabled', ...), ('enabled', ...), ('test', ...)])` | C1 | Always | C1 | `state` has three values: `disabled`, `enabled`, `test`; write handler triggers `_toggle_post_processing_cron` when any provider becomes not-disabled | Provider operational state controlling background cron lifecycle |
| U127-C004 | PaymentProvider-get-default-pm-codes | `payment/models/payment_provider.py:451-460` | `def _get_default_payment_method_codes(self):` | C1 | Always | C1 | Base returns `set()`; overridden by each provider module to return the provider's default payment method code strings; used in `_activate_default_pms` on state change | Default payment method code resolver returning empty set at base level |
| U127-C005 | PaymentProvider-get-compatible | `payment/models/payment_provider.py:554-665` | `def _get_compatible_providers(self, company_id, partner_id, amount, ...)` | C1 | Always | C1 | Filters providers sequentially: not disabled, is_published for non-internal users, partner country, maximum amount (via currency conversion), available currency, tokenization flag, express checkout flag; logs exclusion reasons to report dict | Provider compatibility filter applying sequential exclusion rules for payment form |
| U127-C006 | PaymentProvider-send-api-request | `payment/models/payment_provider.py:756-814` | `def _send_api_request(self, method, endpoint, ...)` | C1 | Always | C1 | Calls `_build_request_url`, `_build_request_headers`, `_build_request_auth`; calls `requests.request` with 10-second timeout; raises `ValidationError` on `ConnectionError`, `Timeout`, or HTTP error; parses response via `_parse_response_content` | Base provider API request dispatcher with structured error propagation |
| U127-C007 | PaymentTransaction-state-field | `payment/models/payment_transaction.py:65-69` | `state = fields.Selection(selection=[('draft', ...), ('pending', ...), ('authorized', ...), ('done', ...), ('cancel', ...), ('error', ...)])` | C1 | Always | C1 | Six-state machine: `draft` → `pending` → `authorized` → `done`; `draft/pending/authorized` → `cancel`; `draft/pending/authorized` → `error`; transitions enforced in `_update_state` | Transaction six-state machine field with enforced transition rules |
| U127-C008 | PaymentTransaction-process | `payment/models/payment_transaction.py:738-756` | `def _process(self, provider_code, payment_data):` | C1 | Always | C1,AWT | Main processing entry point called by provider controllers after webhook receipt or return redirect; calls `_search_by_reference` if no tx, then `_validate_amount`, `_apply_updates`, and `_tokenize` when `tokenize` flag and state in `{'authorized', 'done'}` | Payment data processing entry point receiving provider webhook or redirect data |
| U127-C009 | PaymentTransaction-search-by-reference | `payment/models/payment_transaction.py:758-779` | `def _search_by_reference(self, provider_code, payment_data):` | C1 | Always | C1 | Calls `_extract_reference` to get reference string; searches by `reference` and `provider_code`; logs warning if not found and returns empty recordset | Transaction lookup by provider code and extracted reference |
| U127-C010 | PaymentTransaction-validate-amount | `payment/models/payment_transaction.py:794-844` | `def _validate_amount(self, payment_data):` | C1 | Always | C1 | Skips validation operations and providers returning `None` from `_extract_amount_data`; negates amount for refunds; compares using `float_round` with `CURRENCY_MINOR_UNITS` precision; calls `_set_error` on mismatch | Amount and currency integrity check protecting against provider data substitution |
| U127-C011 | PaymentTransaction-apply-updates-base | `payment/models/payment_transaction.py:858-874` | `def _apply_updates(self, payment_data):` | C1 | Always | C1 | Base implementation is a no-op; each provider must override to update `provider_reference` and call the appropriate state setter based on mapped provider status | Provider state-update hook that must be overridden by each payment integration |
| U127-C012 | PaymentTransaction-set-done | `payment/models/payment_transaction.py:949-965` | `def _set_done(self, *, state_message=None, extra_allowed_states=()):` | C1 | Always | C1 | Allowed source states: `draft`, `pending`, `authorized`, `error`; calls `_update_state`, `_log_received_message`, and `_update_source_transaction_state` | Transaction confirmed-state transition including source transaction propagation |
| U127-C013 | PaymentTransaction-state-setters | `payment/models/payment_transaction.py:915-1000` | `_set_pending`, `_set_authorized`, `_set_canceled`, `_set_error` methods | C1 | Always | C1 | `_set_pending` allows source `draft`; `_set_authorized` allows `draft`, `pending`; `_set_canceled` allows `draft`, `pending`, `authorized`; `_set_error` allows `draft`, `pending`, `authorized`; all call `_log_received_message` | State setter methods enforcing allowed-source-state rules for each target state |
| U127-C014 | PaymentTransaction-update-state | `payment/models/payment_transaction.py:1002-1058` | `def _update_state(self, allowed_states, target_state, state_message):` | C1 | Always | C1 | Classifies transactions into to_process / already_processed / wrong_state; writes `state`, `state_message`, `last_state_change`; resets `is_post_processed` to `False` to allow re-entry of post-processing | Core state transition writer with classification and idempotency logic |
| U127-C015 | PaymentTransaction-post-process-base | `payment/models/payment_transaction.py:1112-1122` | `def _post_process(self):` | C1 | Always | C1 | Base sets `is_post_processed = True`; overridden by `account_payment` (creates `account.payment`) and `sale` (confirms orders, invoices); `website_payment` adds donation email | Base post-processing hook setting the processed flag; extended by document-aware modules |
| U127-C016 | PaymentTransaction-cron-post-process | `payment/models/payment_transaction.py:1082-1110` | `def _cron_post_process(self):` | C1 | Always | C1 | Finds all transactions with `is_post_processed=False` and `last_state_change >= now-4days`; calls `_post_process` per transaction with `env.cr.commit`; handles `psycopg2.OperationalError` by rollback and retry | Background post-processing cron with 4-day retry window for missed callbacks |
| U127-C017 | PaymentPostProcessing-poll-status | `payment/controllers/post_processing.py:41-73` | `def poll_status(self, **_kwargs):` | C1 | Always | C1,AWT | Jsonrpc `/payment/status/poll`; retrieves monitored transaction from session; calls `_post_process()` if not yet post-processed; returns `provider_code`, `state`, `landing_route`; handles `psycopg2.OperationalError` by raising `'retry'` | Status polling endpoint triggering transaction post-processing and returning state for redirect |
| U127-C018 | PaymentPortal-create-transaction | `payment/controllers/portal.py:258-283` | `def payment_transaction(self, amount, currency_id, partner_id, access_token, **kwargs):` | C1 | Always | C1 | Jsonrpc `/payment/transaction`; validates access token via HMAC; calls `_create_transaction`; calls `_update_landing_route` appending `tx_id` and `access_token` to landing route; returns `_get_processing_values()` | Transaction creation endpoint returning provider-specific processing values for the client |
| U127-C019 | PaymentPostProcessing-monitor | `payment/controllers/post_processing.py:75-82` | `def monitor_transaction(cls, transaction):` | C1 | Always | C1 | Class method storing `transaction.id` in `request.session[MONITORED_TX_ID_KEY]`; called from `_create_transaction` after every new transaction | Session-based transaction monitor enabling status page and post-processing polling |
| U127-C020 | AccountPayment-post-process | `account_payment/models/payment_transaction.py:98-131` | `def _post_process(self):` (override in `account_payment`) | C1 | Always | C1,AWT | For `done` transactions: posts draft invoices via `action_post`; calls `_create_payment` if no `payment_id` and no settled child transactions; logs payment link on linked documents; for `cancel`: calls `payment_id.action_cancel` | Account-aware post-processing creating journal entries from confirmed payment transactions |
| U127-C021 | AccountPayment-create-payment | `account_payment/models/payment_transaction.py:133-211` | `def _create_payment(self, **extra_create_values):` | C1 | Always | C1 | Creates `account.payment` with provider journal, inbound/outbound type based on amount sign, posts it, reconciles with invoice payment term lines via `line_ids.reconcile()`; handles early payment discount write-off | Journal entry creation and automatic reconciliation from a confirmed payment transaction |
| U127-C022 | Sale-post-process | `sale/models/payment_transaction.py:40-106` | `def _post_process(self):` (override in `sale`) | C1 | Always | C1,AWT | For `pending`: sends quotation email; for `authorized`: calls `_check_amount_and_confirm_order`; for `done`: confirms order, then calls `_invoice_sale_orders` if `sale.automatic_invoice` parameter is `True`; sends invoice if not async | Sale order lifecycle management triggered by payment transaction state changes |
| U127-C023 | Sale-check-amount-confirm | `sale/models/payment_transaction.py:108-133` | `def _check_amount_and_confirm_order(self):` | C1 | Always | C1 | Confirms SO only when exactly one SO linked, SO in draft/sent state, no signature required, and `_is_confirmation_amount_reached()` returns True; calls `action_confirm` with `send_email=True` | Sale order confirmation based on payment amount threshold reaching the confirmation requirement |
| U127-C024 | StripeController-webhook | `payment_stripe/controllers/main.py:69-155` | `def stripe_webhook(self):` | C1 | Always | C1,AWT | POST `/payment/stripe/webhook` csrf=False; handles `payment_intent.*`, `setup_intent.*`, `charge.refunded`, `charge.refund.updated` events from `const.HANDLED_WEBHOOK_EVENTS`; calls `_verify_signature` then `tx._process('stripe', data)` | Stripe provider webhook receiver handling payment, validation, and refund event types |
| U127-C025 | StripeController-verify-signature | `payment_stripe/controllers/main.py:193-235` | `def _verify_signature(self, tx_sudo):` | C1 | Always | C1 | Validates `Stripe-Signature` header: parses `t=` timestamp and `v1=` signatures; checks timestamp freshness within 10-minute tolerance; computes HMAC-SHA256 of `{timestamp}.{payload}` against webhook secret; uses `hmac.compare_digest` for constant-time comparison | Stripe webhook HMAC-SHA256 signature verification with timestamp replay protection |
| U127-C026 | Stripe-apply-updates | `payment_stripe/models/payment_transaction.py:326-389` | `def _apply_updates(self, payment_data):` (Stripe override) | C1 | Always | C1 | Maps Stripe `payment_intent` / `setup_intent` / `refund` status through `const.STATUS_MAPPING` to Odoo states; triggers post-processing cron immediately after refund `_set_done`; handles `last_payment_error` for error messages | Stripe-specific status mapping updating transaction state from provider-normalized data |
| U127-C027 | XenditController-webhook | `payment_xendit/controllers/main.py:39-54` | `def xendit_webhook(self):` | C1 | Always | C1,TH,AWT | POST `/payment/xendit/webhook` csrf=False; reads `x-callback-token` header; calls `_verify_notification_token` via `consteq` comparison against `xendit_webhook_token` on provider; calls `tx._process('xendit', data)` | Xendit webhook receiver with callback-token verification, relevant for Southeast Asia deployments |
| U127-C028 | Xendit-apply-updates | `payment_xendit/models/payment_transaction.py:180-212` | `def _apply_updates(self, payment_data):` (Xendit override) | C1 | Always | C1,TH | Sets `provider_reference` from `payment_data['id']`; maps FPX method codes; maps status through `PAYMENT_STATUS_MAPPING` to pending/done/cancel/error states | Xendit status-to-Odoo-state mapping including FPX payment method handling for Southeast Asia |
| U127-C029 | WebsitePayment-donation-post-process | `website_payment/models/payment_transaction.py:13-26` | `def _post_process(self):` (website_payment override) | C1 | Always | C1 | Calls `super()._post_process()`; for `done` donations (`is_donation=True`): calls `_send_donation_email` and logs payment details in `payment_id` chatter | Website donation payment confirmation email sent after transaction reaches confirmed state |

---

## 4. Key Architectural Findings

### 4.1 Webhook Chain Architecture

The payment webhook chain follows a layered architecture:

```
Provider Server → [HTTP POST csrf=False] → Provider Controller (e.g. StripeController.stripe_webhook)
  → signature/token verification
  → tx = payment.transaction._search_by_reference(provider_code, data)
  → tx._process(provider_code, data)
    → tx._validate_amount(data)
    → tx._apply_updates(data)   [provider override: maps status, calls _set_done/_set_pending/etc.]
    → tx._tokenize(data)        [if tokenize=True and state in done/authorized]
  → return 200 acknowledgement

Client Browser → [GET /payment/status] → PaymentPostProcessing.display_status
  → [JS poll /payment/status/poll] → PaymentPostProcessing.poll_status
    → tx._post_process()
      [account_payment override]:
        → draft invoices .action_post()
        → tx._create_payment()  [creates account.payment, posts, reconciles]
      [sale override]:
        → _check_amount_and_confirm_order()  [confirms SO if threshold reached]
        → _invoice_sale_orders()  [if sale.automatic_invoice=True]
```

### 4.2 GAP-015 Finding (Payment Provider Integration)

Community includes 26 payment-related modules including 18 distinct provider implementations. The base `payment` module provides the full webhook framework (`_process`, `_apply_updates`, `_set_done`, `_post_process`) and all providers follow the same pattern. The source is complete for static analysis; runtime testing is required to verify webhook delivery, signature validation, and state transition correctness.

**Status: PARTIAL** — Source framework fully documented. AWT items: live webhook receipt, HMAC verification under load, provider-specific edge cases.

### 4.3 GAP-041 Finding (eCommerce Payment Confirmation)

The `sale/models/payment_transaction.py` `_post_process` override implements the full eCommerce confirmation chain: pending → quotation email, authorized/done → SO confirmation via `_check_amount_and_confirm_order`, done → auto-invoicing via `_invoice_sale_orders`. The `sale.automatic_invoice` IR config parameter gates invoice creation. The `account_payment` module creates the `account.payment` record and reconciles it against invoices.

**Status: PARTIAL** — Full source chain documented from payment.transaction through SO confirmation to invoice creation. AWT items: live trigger timing, partial payment handling edge cases.

### 4.4 TH-Relevance

- Xendit (`payment_xendit`) is explicitly a Southeast Asia provider with FPX payment support, making it relevant to Thailand-adjacent deployments.
- `payment_xendit/controllers/main.py` implements `/payment/xendit/webhook` with `x-callback-token` header verification.
- Thai Baht (THB) is present in `payment/const.py:CURRENCY_MINOR_UNITS` with 2 decimal places.

---

## 5. File Index

| File | Lines read | Purpose |
|------|-----------|---------|
| `payment/models/payment_provider.py` | 1-860 | Base provider model, _get_compatible_providers, _send_api_request |
| `payment/models/payment_transaction.py` | 1-1281 | Transaction state machine, _process, _post_process, state setters |
| `payment/controllers/portal.py` | 1-512 | /payment/transaction, /payment/confirmation routes |
| `payment/controllers/post_processing.py` | 1-93 | /payment/status/poll, monitor_transaction |
| `payment/const.py` | 1-553 | CURRENCY_MINOR_UNITS, REPORT_REASONS_MAPPING |
| `account_payment/models/payment_transaction.py` | 1-243 | _post_process override, _create_payment |
| `sale/models/payment_transaction.py` | 1-268 | _post_process override, _check_amount_and_confirm_order |
| `payment_stripe/controllers/main.py` | 1-254 | Stripe webhook, return URL, signature verification |
| `payment_stripe/models/payment_transaction.py` | 1-435 | Stripe _apply_updates, _search_by_reference, _extract_amount_data |
| `payment_xendit/controllers/main.py` | 1-85 | Xendit webhook, return URL, token verification |
| `payment_xendit/models/payment_transaction.py` | 1-220 | Xendit _apply_updates, _extract_reference |
| `payment_paypal/controllers/main.py` | 1-100 | PayPal webhook, complete_order endpoint |
| `website_payment/models/payment_transaction.py` | 1-60 | Donation _post_process |
| `website_payment/models/account_payment.py` | 1-11 | is_donation field bridge |
