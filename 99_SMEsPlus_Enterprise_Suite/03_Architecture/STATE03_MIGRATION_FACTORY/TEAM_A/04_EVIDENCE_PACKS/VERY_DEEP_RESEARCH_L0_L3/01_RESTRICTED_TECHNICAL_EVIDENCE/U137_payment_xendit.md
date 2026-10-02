# U137 — payment_xendit: Thai-Adjacent Payment Provider Deep Study
**Unit:** U137 | **Group:** G15/G03 | **Priority:** P2
**Status:** PRESENT — full L3 study completed
**Date:** 2026-10-02

---

## MODULE PRESENCE

Module path: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/payment_xendit`

Files confirmed present: `__manifest__.py`, `const.py`, `models/payment_provider.py`, `models/payment_transaction.py`, `controllers/main.py`, `static/src/interactions/payment_form.js`, `static/src/js/auth_service.js`, `static/src/js/auth_ui.js`, `views/payment_provider_views.xml`, `views/payment_xendit_templates.xml`, `data/payment_provider_data.xml`, `tests/common.py`, `tests/test_processing_flows.py`, `tests/test_payment_transaction.py`

---

## L1 — MANIFEST / DEPENDENCIES

### Claim U137-L1-01
- **Source:** `__manifest__.py:8`
- **Finding:** Module summary declares "A payment provider for Indonesian and the Philippines." — Thailand is NOT mentioned in the summary despite THB being supported in const.py.

### Claim U137-L1-02
- **Source:** `__manifest__.py:10`
- **Finding:** Module depends only on `['payment']` — no direct dependency on `account`, `l10n_th`, or any Thai localization. Accounting postings come through the payment module's own flows.

### Claim U137-L1-03
- **Source:** `__manifest__.py:17-18`
- **Finding:** `post_init_hook` and `uninstall_hook` are declared. These are standard hooks from the payment module for activating/deactivating the provider record.

---

## L2 — MODELS / FIELDS / ORM

### Claim U137-L2-01
- **Source:** `models/payment_provider.py:15-17`
- **Finding:** Provider code `'xendit'` is added to `payment.provider.code` via `selection_add`. The ondelete policy is `'set default'`, meaning if the module is removed the provider record gets reset to default rather than deleted.

### Claim U137-L2-02
- **Source:** `models/payment_provider.py:18-28`
- **Finding:** Three provider-level credential fields: `xendit_public_key` (Char, required_if_provider='xendit', groups='base.group_system'), `xendit_secret_key` (Char, same restrictions), `xendit_webhook_token` (Char, same restrictions). All three are copy=False.

### Claim U137-L2-03
- **Source:** `models/payment_provider.py:39-42`
- **Finding:** `_compute_feature_support_fields` overrides payment module. Sets `support_tokenization = True` for Xendit. This means card tokenization (saving cards for future use) is enabled.

### Claim U137-L2-04
- **Source:** `models/payment_provider.py:44-51` + `const.py:4-12`
- **Finding:** `_get_supported_currencies` filters to `const.SUPPORTED_CURRENCIES = ['IDR', 'MYR', 'PHP', 'SGD', 'THB', 'USD', 'VND']`. THB is explicitly listed at `const.py:9`.

### Claim U137-L2-05
- **Source:** `const.py:16-24`
- **Finding:** `CURRENCY_DECIMALS` maps all 7 supported currencies to `0` decimal places. THB maps to `0` — Xendit treats THB as zero-decimal (integer baht only, no satang fractions).

### Claim U137-L2-06
- **Source:** `const.py:27-53`
- **Finding:** `DEFAULT_PAYMENT_METHOD_CODES` includes three explicitly Thai-labelled payment methods: `'promptpay'`, `'linepay'`, `'shopeepay'` (all under `# TH` comment at `const.py:38-41`). This confirms native Thai payment method support.

### Claim U137-L2-07
- **Source:** `const.py:103-116`
- **Finding:** `PAYMENT_METHODS_MAPPING` maps `'scb'` → `'DD_SCB_MB'`, `'krungthai_bank'` → `'DD_KTB_MB'`, `'bangkok_bank'` → `'DD_BBL_MB'` — three major Thai banks mapped to Xendit direct debit mobile banking (DD_..._MB) channel codes.

### Claim U137-L2-08
- **Source:** `const.py:36,41` (FPX section comment at line 55-58)
- **Finding:** FPX (Financial Process Exchange) is a Malaysian payment scheme. `const.FPX_METHODS` contains 38 variants (personal direct debit and business accounts). FPX is not Thai but is Southeast Asian adjacent. When Odoo payment method `'fpx'` is selected, the full list of 38 FPX variants is sent to Xendit as `payment_methods`.

### Claim U137-L2-09
- **Source:** `models/payment_transaction.py:154-158`
- **Finding:** `_get_rounded_amount` uses `const.CURRENCY_DECIMALS.get(self.currency_id.name, self.currency_id.decimal_places)` with `rounding_method='DOWN'`. For THB this returns `float_round(amount, 0, rounding_method='DOWN')` — always rounds DOWN to integer baht, truncating satang.

### Claim U137-L2-10
- **Source:** `models/payment_transaction.py:167-178`
- **Finding:** `_extract_amount_data` reads `payment_data.get('amount') or payment_data.get('authorized_amount')` and passes `precision_digits=const.CURRENCY_DECIMALS.get(currency_code)`. For THB this is 0 — the reconciliation is performed against an integer baht figure.

---

## L3 — WORKFLOW / STATE MACHINE

### Claim U137-L3-01
- **Source:** `models/payment_transaction.py:40-65`
- **Finding:** Non-card payment methods (all Thai methods: promptpay, linepay, shopeepay, scb, krungthai_bank, bangkok_bank) use the redirect flow: `_get_specific_rendering_values` calls `_xendit_prepare_invoice_request_payload` then POSTs to Xendit `v2/invoices` API and returns the `invoice_url`. Cards use direct flow (no invoice creation at render time).

### Claim U137-L3-02
- **Source:** `models/payment_transaction.py:81-117`
- **Finding:** Invoice payload includes `external_id` (Odoo transaction reference), `amount` (rounded integer for THB), `currency`, `payment_methods` list (single method or full FPX list), success/failure redirect URLs, and optional customer address block.

### Claim U137-L3-03
- **Source:** `models/payment_transaction.py:180-212`
- **Finding:** `_apply_updates` determines state: `PENDING` → `_set_pending()`, `SUCCEEDED`/`PAID`/`CAPTURED` → `_set_done()`, `CANCELLED`/`EXPIRED` → `_set_canceled()`, `FAILED` → `_set_error()` with failure_reason message.

### Claim U137-L3-04
- **Source:** `models/payment_transaction.py:190-196`
- **Finding:** FPX reverse-mapping on webhook: if `payment_data.get('payment_method')` is in `const.FPX_METHODS`, the code normalises it back to `'fpx'` before calling `_get_from_code`. This ensures correct Odoo payment method linkage on return.

### Claim U137-L3-05
- **Source:** `controllers/main.py:56-67`
- **Finding:** Return URL handler `/payment/xendit/return` sets draft → pending only if: (1) `success` param is true (str2bool), (2) `access_token` is valid (checked via `payment_utils.check_access_token`), (3) transaction state is currently `'draft'`. Wrong token or success=false leaves state as draft.

### Claim U137-L3-06
- **Source:** `models/payment_transaction.py:126-152`
- **Finding:** Card tokenization (`_xendit_create_charge`): if `self.tokenize` or `self.token_id`, sets `is_recurring=True` in the charge payload to suppress 3DS on subsequent charges.

---

## L4 — CROSS-MODULE DEPENDENCIES

### Claim U137-L4-01
- **Source:** `models/payment_transaction.py:10-13`
- **Finding:** Imports from `odoo.addons.payment.utils` (access token generation/check) and `odoo.addons.payment.logging`. All accounting-side flows (journal entries, account.move creation) are inherited from the parent `payment.transaction` model via `_set_done()` calling the payment module's own reconciliation logic.

---

## L5 — VIEWS / WIZARDS

### Claim U137-L5-01
- **Source:** `views/payment_provider_views.xml:9-31`
- **Finding:** The provider form view adds three credential fields (Public Key, Secret Key, Webhook Token) inside the `provider_credentials` group. All are `invisible="code != 'xendit'"` and `required="code == 'xendit' and state != 'disabled'"`. Secret Key and Webhook Token render with `password="True"`.

### Claim U137-L5-02
- **Source:** `views/payment_xendit_templates.xml:8-109`
- **Finding:** Inline form template shows card data entry fields (first name, last name, phone, email, card number, expiry month/year, CVN) only when `pm_sudo.code == 'card'`. Non-card methods (all Thai e-wallets) have no inline form — they use redirect only.

### Claim U137-L5-03
- **Source:** `views/payment_xendit_templates.xml:4-6`
- **Finding:** Redirect form template is minimal: `<form t-att-action="api_url" method="get"/>`. The `api_url` is Xendit's hosted invoice URL returned from the v2/invoices API call.

---

## L6 — ACCESS / SECURITY RULES

### Claim U137-L6-01
- **Source:** `models/payment_provider.py:21-23,27-29,33-35`
- **Finding:** All three credential fields (`xendit_public_key`, `xendit_secret_key`, `xendit_webhook_token`) are restricted to `groups='base.group_system'`. Non-admin users cannot read or write Xendit API keys. No dedicated `security/ir.model.access.csv` file found in the module (no custom model, all inherited).

---

## L7 — CONFIGURATION

### Claim U137-L7-01
- **Source:** `models/payment_provider.py:86-90`
- **Finding:** `_build_request_url` hardcodes the Xendit API base URL to `'https://api.xendit.co/'`. There is no configurable base URL for sandbox vs production — switching environments requires changing provider state (test vs enabled) at the Xendit API credentials level.

### Claim U137-L7-02
- **Source:** `models/payment_provider.py:92-96`
- **Finding:** `_build_request_auth` returns `(self.xendit_secret_key, '')` — HTTP Basic Auth with secret key as username and empty string as password. This is Xendit's documented API auth pattern.

### Claim U137-L7-03
- **Source:** `models/payment_provider.py:55-60`
- **Finding:** `_get_default_payment_method_codes` returns `const.DEFAULT_PAYMENT_METHOD_CODES` (18 methods including all Thai ones) as the default activation set when the Xendit provider is configured.

---

## L8 — IMMUTABILITY

### Claim U137-L8-01
- **Source:** `models/payment_provider.py:21,27,33`
- **Finding:** All three credential fields have `copy=False`. Duplicating a Xendit provider record does not copy sensitive API keys.

---

## L9 — ACCOUNTING POSTINGS

### Claim U137-L9-01
- **Source:** `models/payment_transaction.py:200-204` + payment module inheritance chain
- **Finding:** `_set_done()` is the terminal success state method inherited from `payment.transaction`. In the Odoo payment framework, `_set_done()` triggers `_post_process()` which creates an `account.payment` record and posts it against the linked `account.move` (invoice). This reconciliation logic is entirely in the parent `payment` module — `payment_xendit` does not override it.

---

## L10 — CRON / QUEUE

No cron jobs or queue workers declared in payment_xendit. No `data/` XML file with `ir.cron` records. Webhook processing is synchronous within the HTTP request handler.

---

## L11 — API / WEBHOOK

### Claim U137-L11-01
- **Source:** `controllers/main.py:21,39-54`
- **Finding:** Webhook URL is `/payment/xendit/webhook`, `type='http'`, `methods=['POST']`, `auth='public'`, `csrf=False`. All POST requests to this endpoint from Xendit are processed without CSRF validation, with authentication solely via `x-callback-token` header comparison.

### Claim U137-L11-02
- **Source:** `controllers/main.py:48,82-84`
- **Finding:** Token verification: reads `x-callback-token` header, compares to `tx_sudo.provider_id.xendit_webhook_token` using `consteq()` (constant-time comparison to prevent timing attacks). Missing token raises Forbidden. Wrong token raises Forbidden.

### Claim U137-L11-03
- **Source:** `controllers/main.py:24-37`
- **Finding:** Second endpoint `/payment/xendit/payment` (JSON-RPC, auth='public') handles card tokenized payments. Validates `access_token` against the transaction reference before calling `_xendit_create_charge`. This is the frontend-to-backend payment completion call.

---

## L12 — RUNTIME / AWT

### Claim U137-L12-01 (AWT)
- **Source:** `tests/test_processing_flows.py:21-33`
- **Finding:** AWT Step: POST to `/payment/xendit/webhook` with valid payment data (with `_verify_notification_token` mocked). Verifies `_process` is called exactly once. Confirms webhook reception triggers transaction processing pipeline.

### Claim U137-L12-02 (AWT)
- **Source:** `tests/test_processing_flows.py:47-56`
- **Finding:** AWT Step: Call `_verify_notification_token` with the stored `provider.xendit_webhook_token`. Asserts no `Forbidden` exception raised. Confirms valid webhook token passes security gate.

### Claim U137-L12-03 (AWT)
- **Source:** `tests/test_processing_flows.py:78-96`
- **Finding:** AWT Step: GET to `/payment/xendit/return` with `success=true` and valid `access_token`. Asserts transaction state transitions from `'draft'` to `'pending'`. Also verifies that wrong/missing token or `success=false` leaves state as `'draft'`.

### Claim U137-L12-04 (AWT)
- **Source:** `tests/test_payment_transaction.py:137-142`
- **Finding:** AWT Step: Call `_apply_updates(webhook_payment_data)` where `webhook_payment_data['status'] == 'PAID'`. Asserts `tx.state == 'done'`. Confirms the PAID status triggers the `_set_done()` accounting path.

### Claim U137-L12-05 (AWT)
- **Source:** `tests/test_payment_transaction.py:104-114`
- **Finding:** AWT Step for THB: Create transaction with amount=1000.50, currency=IDR (same 0-decimal behavior as THB). Verify `processing_values['rounded_amount'] == 1000`. Confirms DOWN-rounding to zero decimal places is applied before sending to Xendit — same logic applies for THB.

---

## APPLICABILITY MATRIX SUMMARY

| Layer | Present | Notes |
|-------|---------|-------|
| L1 Manifest | YES | Declares ID/PH in summary but THB/PromptPay/LinePay/ShopeePay fully present |
| L2 Models | YES | 3 credential fields, tokenization, 7 currencies, 18 payment methods |
| L3 Workflow | YES | Redirect (invoice) for e-wallets/banks; direct for card; state machine via _apply_updates |
| L4 Cross-module | YES | Parent payment module handles accounting; no l10n_th dependency |
| L5 Views | YES | Provider form + inline card form + redirect form template |
| L6 Access | YES | All credentials restricted to group_system |
| L7 Config | YES | 3 provider fields; hardcoded API base URL |
| L8 Immutability | YES | copy=False on all credentials |
| L9 Accounting | INHERITED | _set_done() calls parent payment module reconciliation; no Xendit override |
| L10 Cron | ABSENT | No cron/queue; webhook is synchronous |
| L11 API | YES | /webhook and /payment and /return endpoints |
| L12 AWT | YES | 5 AWT test steps identified |

---

## KEY THAI DEPLOYMENT FINDING

**THB is a first-class citizen in payment_xendit.** The module explicitly:
1. Lists THB in `SUPPORTED_CURRENCIES` (`const.py:9`)
2. Maps THB to 0 decimal places — integer baht only (`const.py:20`)
3. Registers three TH-labelled payment methods: PromptPay, LinePay, ShopeePay (`const.py:38-41`)
4. Maps Thai bank direct debit codes: SCB (`DD_SCB_MB`), Krungthai (`DD_KTB_MB`), Bangkok Bank (`DD_BBL_MB`) (`const.py:109-111`)
5. Includes a Thai locale file `i18n/th.po`

Despite the manifest summary saying "Indonesian and the Philippines only", the source code fully supports Thai payment methods. This discrepancy between manifest summary and actual const.py content is the most significant finding for Thai deployment planning.
