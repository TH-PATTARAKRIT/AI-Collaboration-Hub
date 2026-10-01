# U20 — payment_providers — RESTRICTED TECHNICAL EVIDENCE

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

- Unit: U20 — short name `payment_providers`
- Modules owned: `payment_adyen`, `payment_aps`, `payment_asiapay`, `payment_authorize`, `payment_buckaroo`, `payment_custom`, `payment_demo`, `payment_dpo`, `payment_ecpay`, `payment_flutterwave`, `payment_iyzico`, `payment_mercado_pago`, `payment_mollie`, `payment_nuvei`, `payment_paymob`, `payment_paypal`, `payment_payu`, `payment_razorpay`, `payment_redsys`, `payment_stripe`, `payment_toss_payments`, `payment_worldline`, `payment_xendit` (generic `payment` framework read only as far as the provider contract needs; its own study is CAP-U12-08 in U12)
- Source revision: `19.0.post20260921` (Odoo 19 Community only; root `odoo-19.0.post20260921/odoo/addons`)
- Date of study: 2026-10-02
- Method: static read of source (read-only); configuration-only queries of the restored database (counts, flags, row names; no business data, no credential values). No Odoo execution. Anything needing execution is flagged `RT`.
- Edition note: only Community code was read. The DB shows a provider placeholder for an Enterprise add-on (`payment_sepa_direct_debit`, uninstallable); it was not studied.
- Prior evidence read first: U12 (CAP-U12-08 and its claims), `B01` DB-count baseline, `wave3_common.txt`, worker spec.
- Reading depth: every `controllers/*.py` and `models/*.py` of the 23 add-ons (docstrings skipped), `const.py` of all add-ons (full for tables cited; skimmed for long mapping tables), `utils.py` where present, data files for neutralization and provider rows, selected views/JS only where a claim cites them.
- Reviewer note: severity labels in the weakness register are reviewer-suggested review priorities, not gate decisions, V-levels or approvals.

## Capability list

- CAP-U20-01 Gateway add-on contract and provider lifecycle
- CAP-U20-02 Initiating an online payment through a gateway
- CAP-U20-03 Gateway notifications, return handling and forgery and replay protection
- CAP-U20-04 Amount and currency validation and state translation
- CAP-U20-05 Credential storage, access and logging
- CAP-U20-06 Capture, void, refund and saved payment methods
- CAP-U20-07 Availability, currencies, countries and Thailand relevance
- CAP-U20-08 Offline payment modes (wire transfer and cash on delivery)
- CAP-U20-09 Demo gateway
- CAP-U20-10 External connectivity and merchant onboarding

## CAP-U20-01 Gateway add-on contract and provider lifecycle

**Function-ID(s):** FUNCTION MAPPING REQUIRED (no entry in the 53-function index concerns online payment gateways).

**D1 — Business purpose and process semantics.** Odoo ships one generic payment engine (`payment`, studied in CAP-U12-08) and twenty-three gateway add-ons plus an offline add-on (`payment_custom`) and a fake one (`payment_demo`). Each add-on turns the engine into a working integration for one acquirer. A provider record is the merchant's configured account (credentials, state, supported currencies and countries, payment methods, messages). The engine owns the life cycle; the add-on supplies gateway-specific behaviour through a fixed set of override points. VDR-U20-C001 VDR-U20-C003 VDR-U20-C007

**D2 — Architecture, data and object relationships.** `payment.provider` (company-scoped, `code` selection extended by each add-on via `selection_add`, `state`, `is_published`, m2m `payment_method_ids`, `available_country_ids`, `available_currency_ids` computed/stored, `maximum_amount`, four QWeb form views, message fields, `module_id`). Add-on fields are added by `_inherit = 'payment.provider'` with `required_if_provider='<code>'` so the engine can enforce them. `payment.transaction`/`payment.token` are extended per add-on with a few gateway fields (e.g. Toss `toss_payments_payment_secret`, Stripe/Adyen/Razorpay token fields). Provider rows for all gateways are declared in the `payment` module's data file (24 records, each linked to its add-on through `module_id`) and the add-on's own data file adds code, form views and default flags to the same xmlid; `delivery` adds one more custom provider. VDR-U20-C016 VDR-U20-C085

**D3 — Source, technical and workflow logic.**
Provider state machine (field `state`):
- `disabled -> test|enabled` [write; `_activate_default_pms`, `_check_required_if_provider`, cron toggle] VDR-U20-C010 VDR-U20-C004 VDR-U20-C012
- `test|enabled -> disabled` [write; tokens archived, unsupported payment methods deactivated, cron toggled] VDR-U20-C008 VDR-U20-C009
- `test <-> enabled` [write; tokens archived (state_changed filter excludes only disabled-origin)] VDR-U20-C008

Override contract of a gateway add-on (what the engine calls): provider side `_get_default_payment_method_codes`, `_compute_feature_support_fields`, `_get_supported_currencies`, `_build_request_url/_headers/_auth`, `_parse_response_*`, `_setup_provider`/`_get_removal_values`; transaction side `_get_specific_processing_values`, `_get_specific_rendering_values`, `_send_payment_request`, `_send_capture/void/refund_request`, `_search_by_reference`, `_extract_reference`, `_extract_amount_data`, `_apply_updates`, `_extract_token_values`, `_compute_reference`. VDR-U20-C020 VDR-U20-C021 VDR-U20-C022 VDR-U20-C023 VDR-U20-C024 VDR-U20-C025

Install/uninstall: `post_init_hook` -> `setup_provider` copies provider per top-level company; `uninstall_hook` -> `reset_payment_provider` resets code/state/forms. VDR-U20-C014 VDR-U20-C017 VDR-U20-C018

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Install add-on -> provider row exists disabled -> administrator fills credentials -> state test/enabled -> default payment methods activated, cron on. VDR-U20-C010 VDR-U20-C012 |
| 2 | Reversal / cancel / negative | Disabling archives tokens, deactivates methods, may switch the cron off; uninstall resets the row to code none; provider with an external id cannot be deleted. VDR-U20-C008 VDR-U20-C009 VDR-U20-C017 VDR-U20-C018 |
| 3 | Multi-company / data scope | One provider copy per top-level company; engine searches use the parent_of company check domain; transactions are company-scoped through the provider. VDR-U20-C016 |
| 4 | Side effects / cross-module | Creating/enabling a provider toggles a cron; account_payment creates a payment method line/journal on the first compute of an enabled provider (CAP-U12-08); neutralization disables providers. VDR-U20-C012 VDR-U20-C034 |
| 5 | Configuration / optionality | Per-gateway credentials mandatory only when state is test or enabled; feature support declared per gateway (default none). VDR-U20-C004 VDR-U20-C019 |
| 6 | Validation / constraints | required_if_provider; absent amount extraction fails closed, opt-out only by returning None; HTTP calls time out after 10 s and failures become ValidationError. VDR-U20-C026 VDR-U20-C027 VDR-U20-C028 VDR-U20-C030 |
| 7 | Roles / permissions | Only base.group_system has ACL on payment.provider (CAP-U20-05). VDR-U20-C206 |
| 8 | Scheduled / automated | Single cron "Payment: Post-process transactions" (10 min) shipped inactive and toggled by provider states. VDR-U20-C013 VDR-U20-C012 |
| 9 | Exception / failure | Send-step ValidationError becomes error state on the transaction; unknown gateway status becomes error. VDR-U20-C029 VDR-U20-C030 |
| 10 | Accounting / audit / security | The engine hands confirmed transactions to account_payment for posting (CAP-U12-08); creation from the storefront does not re-check provider availability server side. VDR-U20-C039 VDR-U20-C040 |

**DB reconciliation (configuration only).** 25 `payment_provider` rows: 24 with xmlids in module `payment` (adyen, aps, asiapay, authorize, buckaroo, demo, dpo, ecpay, flutterwave, iyzico, mercado_pago, mollie, nuvei, paymob, paypal, payu, razorpay, redsys, sepa_direct_debit placeholder, stripe, toss_payments, transfer (wire transfer), worldline, xendit) and 1 (`payment_provider_cod`) in module `delivery`. States: demo `test`, cash on delivery `enabled`, 23 `disabled`. All 25 rows belong to company 1. `ir_module_module`: payment, all 23 provider add-ons, payment_custom, payment_demo, account_payment, account_payment_interco, website_payment, delivery, sale, l10n_th installed; `payment_sepa_direct_debit` uninstallable; `pos_online_payment` and `website_sale` uninstalled. ACL rows seeded by `payment`: 12 (+ account_payment wizard/transaction rows); rule rows: 5; cron rows: 1 (active, 10 min); res.groups seeded by payment_* modules: 0; base_automation rows: 0 (the table exists and is empty). B01 source-vs-DB id counts (`src_declared_ids` = `db_ids`, no missing ids): adyen 5, aps 2, asiapay 2, authorize 3, buckaroo 2, custom 6, demo 9, dpo 2, ecpay 2, flutterwave 2, iyzico 2, mercado_pago 5, mollie 2, nuvei 2, paymob 2, paypal 4, payu 3, razorpay 3, redsys 2, stripe 8, toss_payments 2, worldline 2, xendit 3; payment 317 source vs 318 in DB (one extra row). ir.ui.view rows seeded by the 25 provider add-ons: 72 in total (adyen 5, aps 2, asiapay 2, authorize 3, buckaroo 2, custom 5, demo 8, dpo 2, ecpay 2, flutterwave 2, iyzico 2, mercado_pago 5, mollie 2, nuvei 2, paymob 2, paypal 4, payu 3, razorpay 3, redsys 2, stripe 7, toss_payments 2, worldline 2, xendit 3), of which 44 are QWeb templates. VDR-U20-C085 VDR-U20-C086

**Unknown / Runtime (RT) list.**
- RT: execution of `post_init_hook` on a multi-company database (copies per company) not observed.
- UNKNOWN: front-end JavaScript of each add-on (static/src) was read only where cited.
- UNKNOWN: whether third-party/custom add-ons in the deployment override any of these hooks (none seen in the community tree).

## CAP-U20-02 Initiating an online payment through a gateway

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 — Business purpose and process semantics.** When a customer chooses to pay online the storefront/portal posts to `/payment/transaction` (engine, CAP-U12-08), which creates a draft `payment.transaction` and asks the add-on for processing/rendering values. The add-on prepares the first outbound leg: a signed redirect form, a hosted session obtained by an API call, an embedded form session (Stripe, Adyen, Razorpay, Authorize.Net, Toss, Mercado Pago bricks), a token charge, or a server-created order/charge. The reference, amount, currency and customer snapshot let the later gateway message be matched to exactly one transaction. VDR-U20-C042 VDR-U20-C081 VDR-U20-C070

**D2 — Architecture, data and object relationships.** Flow types per provider (operation values `online_redirect`, `online_direct`, `online_token`, `validation`, `offline`): redirect form + signature (APS VDR-U20-C046, AsiaPay VDR-U20-C047, Buckaroo, ECPay VDR-U20-C053, Nuvei VDR-U20-C061, PayU VDR-U20-C064, Redsys VDR-U20-C066); hosted session via API (Flutterwave VDR-U20-C054, Iyzico VDR-U20-C055, Mercado Pago VDR-U20-C056, Mollie VDR-U20-C060, Paymob VDR-U20-C062, Worldline VDR-U20-C068, Xendit invoices VDR-U20-C069, DPO VDR-U20-C051); embedded/direct (Stripe VDR-U20-C042, Adyen VDR-U20-C044, Authorize.Net VDR-U20-C048, Razorpay VDR-U20-C065, PayPal VDR-U20-C063, Toss VDR-U20-C067, Mercado Pago bricks VDR-U20-C057); offline (custom) and simulated (demo) in CAP-U20-08/09. Reference formatting overrides: APS VDR-U20-C072, Redsys VDR-U20-C075; idempotency keys VDR-U20-C077.

**D3 — Source, technical and workflow logic.** Transaction state at this stage: `draft -> pending|error` [processing values; API failures `_set_error`] ; token flow `draft -> done|pending|authorized|error` immediately via `_send_payment_request` -> `_process`. Access-token tamper checks on browser-initiated direct steps: Adyen binds reference+amount+currency+partner VDR-U20-C045, Authorize.Net reference+partner only VDR-U20-C049, Xendit reference only VDR-U20-C084, Mercado Pago none VDR-U20-C057, Adyen `/payments/details` and `/return` none VDR-U20-C082 VDR-U20-C083. DPO builds XML by string concatenation VDR-U20-C051. Weakness refs W-02 (Mercado Pago amount), W-03 (DPO), W-07 (Adyen): see the weakness register.

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Draft transaction -> add-on creates gateway-side object (intent/order/session) -> customer pays at gateway or in embedded form -> notification (CAP-U20-03). VDR-U20-C042 VDR-U20-C063 |
| 2 | Reversal / cancel / negative | API error during preparation puts the transaction in `error` with the gateway message (Flutterwave, Iyzico, Mercado Pago, Mollie, Paymob, Razorpay, Stripe, Xendit). VDR-U20-C055 VDR-U20-C060 |
| 3 | Multi-company / data scope | Provider is chosen by id from the client; the provider's company decides credentials; no cross-company check in the creation route. VDR-U20-C039 |
| 4 | Side effects / cross-module | Customer name, email, phone, address are sent to the gateway; Stripe creates a gateway Customer per payment; shipping address from sale order/invoice for Stripe and PayPal. VDR-U20-C081 |
| 5 | Configuration / optionality | Test vs live endpoint chosen by provider state; Adyen/Paymob URL prefix configurable; capture method manual vs automatic by `capture_manually`. VDR-U20-C042 |
| 6 | Validation / constraints | Reference format rules for APS/AsiaPay/ECPay/Redsys/Worldline; Nuvei rounds amounts down and requires first+last name for some methods; Xendit and ECPay truncate to integers. VDR-U20-C072 VDR-U20-C075 VDR-U20-C053 VDR-U20-C179 |
| 7 | Roles / permissions | Routes are `auth='public'`; protection is the access token (where present) and server-side lookup by reference. VDR-U20-C045 VDR-U20-C049 |
| 8 | Scheduled / automated | None at initiation (post-processing is CAP-U12-08). |
| 9 | Exception / failure | Gateway timeout/HTTP error -> ValidationError -> error state; Razorpay blocks token charges for 36 h after an earlier pending one. VDR-U20-C028 VDR-U20-C256 |
| 10 | Accounting / audit / security | Idempotency keys prevent duplicate charges; Mercado Pago trusts a client-supplied amount (W-02); DPO XML not escaped (W-03). VDR-U20-C077 VDR-U20-C057 VDR-U20-C051 |

**DB reconciliation (configuration only).** No transactions, no tokens in the restored DB. Flow-related provider columns: `redirect_form_view_id` is set on aps, asiapay, buckaroo, dpo, ecpay, flutterwave, iyzico, mercado_pago, mollie, nuvei, paymob, payu, redsys, worldline, xendit, wire transfer and cash on delivery (the last two use the same custom redirect form, view 3588); `inline_form_view_id` on adyen, authorize, demo, mercado_pago, stripe, xendit; `token_inline_form_view_id` on demo and razorpay; `express_checkout_form_view_id` on demo and stripe; none of the four on paypal, toss_payments and the sepa placeholder. `allow_tokenization` is true on adyen, authorize, demo, flutterwave, stripe, worldline; `capture_manually` is empty on all rows; `maximum_amount` and country restrictions are empty. VDR-U20-C081

**Unknown / Runtime (RT) list.**
- RT: all outbound API calls (shapes, auth failures, 3-D Secure behaviour).
- RT: Mercado Pago under-payment (W-02), Adyen details/return binding (W-07), DPO XML parsing (W-03).
- UNKNOWN: front-end flows (static/src) beyond the cited Razorpay and Mercado Pago lines.

## CAP-U20-03 Gateway notifications, return handling and forgery and replay protection

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 — Business purpose and process semantics.** The gateway tells the shop the outcome by (a) redirecting the customer's browser back (return route) and (b) a server-to-server webhook. Both are public routes (`auth='public'`, webhooks `csrf=False`). Because anybody can call them, each add-on must authenticate the message, bind it to one transaction, and be idempotent. Three authentication families exist: signed payload, static header token, and unauthenticated message followed by a pull from the gateway API. VDR-U20-C092 VDR-U20-C122 VDR-U20-C127

**D2 — Architecture, data and object relationships.** Each add-on owns a controller (routes) and the transaction overrides `_search_by_reference`/`_extract_reference` to locate the transaction (`reference` + `provider_code` unique pair), the controller then calls its `_verify_signature` (or pull) and `tx._process`. State machine and replay behaviour are in the engine: same-state messages are skipped, disallowed transitions refused. VDR-U20-C087 VDR-U20-C088 VDR-U20-C089

**D3 — Source, technical and workflow logic.** Message pipeline (all signed gateways): `route -> _search_by_reference -> (if tx) _verify_signature -> _process -> _validate_amount -> _apply_updates -> _tokenize? -> HTTP ack`. Missing tx: ack only. Missing signature: `Forbidden`; a missing secret is refused explicitly only by Stripe and by the Razorpay webhook path, in other add-ons it ends in an unhandled exception (HTTP 500) with the transaction unchanged. Matrix:

| Provider | Return route | Callback route | Authentication | Binding / notes |
|---|---|---|---|---|
| Stripe | GET /payment/stripe/return (pull PaymentIntent, compare description) | POST /payment/stripe/webhook | HMAC-SHA256 of `t.payload` with `stripe_webhook_secret`, 10 min age window; refuse if no secret | VDR-U20-C091 VDR-U20-C092 VDR-U20-C093 VDR-U20-C094 VDR-U20-C095 VDR-U20-C096 |
| Adyen | GET/POST /payment/adyen/return, jsonrpc /payments/details (no token) | POST /payment/adyen/notification | HMAC-SHA256 (base64, hex key) over 8 fields | VDR-U20-C098 VDR-U20-C099 VDR-U20-C100 VDR-U20-C082 VDR-U20-C083 |
| APS | POST /payment/aps/return | POST /payment/aps/webhook | SHA-256 phrase digest (aps_sha_response) | VDR-U20-C102 VDR-U20-C103 VDR-U20-C104 |
| AsiaPay | GET /payment/asiapay/return (not processed) | POST /payment/asiapay/webhook | secureHash SHA1 default (SHA256/512 selectable) | VDR-U20-C105 VDR-U20-C106 VDR-U20-C107 |
| Authorize.Net | none; jsonrpc /payment/authorize/payment | none | access token over reference+partner; response of direct API call | VDR-U20-C049 VDR-U20-C110 VDR-U20-C109 |
| Buckaroo | POST /payment/buckaroo/return | POST /payment/buckaroo/webhook | SHA-1 digest + secret | VDR-U20-C111 VDR-U20-C112 |
| Custom (wire/COD) | POST /payment/custom/process | none | none | VDR-U20-C113 VDR-U20-C114 |
| Demo | jsonrpc /payment/demo/simulate_payment | none | none | VDR-U20-C115 |
| DPO | GET /payment/dpo/return | none | pull verifyToken, no signature | VDR-U20-C116 VDR-U20-C117 VDR-U20-C118 VDR-U20-C119 |
| ECPay | GET/POST /payment/ecpay/return | POST /payment/ecpay/webhook | CheckMacValue SHA-256 (hash key/IV), consteq | VDR-U20-C120 VDR-U20-C121 |
| Flutterwave | GET return / auth_return (pull verify_by_reference) | POST webhook | static `verif-hash` equals stored secret | VDR-U20-C122 VDR-U20-C123 |
| Iyzico | POST return | POST webhook | none; pull detail API; basketId must equal reference | VDR-U20-C124 |
| Mercado Pago | GET /payment/mercado_pago/return | POST /payment/mercado_pago/webhook/<reference> | none; pull + external_reference compare | VDR-U20-C125 VDR-U20-C126 |
| Mollie | GET/POST return | POST webhook | none; pull by stored provider_reference | VDR-U20-C127 |
| Nuvei | GET return (+error token) | POST webhook | SHA-256 prefix checksum, consteq | VDR-U20-C128 VDR-U20-C129 VDR-U20-C130 VDR-U20-C131 |
| Paymob | GET return | POST webhook (hmac query) | HMAC-SHA512 + order id equals stored reference | VDR-U20-C132 VDR-U20-C133 VDR-U20-C134 |
| PayPal | jsonrpc complete_order (capture) | POST webhook | PayPal verify-webhook-signature API | VDR-U20-C135 VDR-U20-C136 VDR-U20-C137 |
| PayU | POST return | POST webhook | SHA-512 hash, consteq | VDR-U20-C138 VDR-U20-C139 |
| Razorpay | POST return | POST webhook | HMAC-SHA256 (key secret / webhook secret) | VDR-U20-C140 VDR-U20-C141 VDR-U20-C142 VDR-U20-C143 VDR-U20-C144 |
| Redsys | GET return | POST webhook | HMAC-SHA256 with per-order 3DES-derived key | VDR-U20-C145 |
| Toss Payments | GET success / failure | POST webhook | per-payment secret equals stored; EXPIRED/ABORTED exempt | VDR-U20-C146 VDR-U20-C148 VDR-U20-C149 VDR-U20-C150 VDR-U20-C151 VDR-U20-C152 |
| Worldline | GET return (pull hostedcheckout) | POST webhook | HMAC-SHA256 base64 of raw body | VDR-U20-C153 VDR-U20-C154 |
| Xendit | GET return (sets draft->pending only) | POST webhook | static `x-callback-token`, consteq | VDR-U20-C155 VDR-U20-C156 VDR-U20-C157 |

Weakness refs: W-01 Toss, W-03 DPO, W-04 Razorpay redirect, W-05 static-token gateways, W-06 PayPal, W-07 Adyen, W-10 protocol-dictated hashes, W-13 offline/demo public routes.

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Gateway posts notification -> tx located by reference -> authenticity verified -> amount validated -> state set -> acknowledged; return route redirects to `/payment/status` which post-processes. VDR-U20-C092 VDR-U20-C098 |
| 2 | Reversal / cancel / negative | Cancel/failed notifications map to cancel/error; refund notifications create refund children (CAP-U20-06). VDR-U20-C088 |
| 3 | Multi-company / data scope | The tx lookup is global by reference + provider code; the verification uses the transaction's own provider credentials (so the right company's secret). VDR-U20-C098 VDR-U20-C102 |
| 4 | Side effects / cross-module | `_process` may create tokens (`_tokenize`), refund/capture children, and updates is_post_processed False so the cron/portal poll posts payments. VDR-U20-C097 |
| 5 | Configuration / optionality | Webhook secret optional on the provider form for Stripe (webhook refused if missing); required to enable Flutterwave, Worldline and Xendit; generated automatically for Razorpay; PayPal webhook id created by an action. VDR-U20-C093 VDR-U20-C122 |
| 6 | Validation / constraints | Constant-time comparison for all secret comparisons; only Stripe has an age limit; others rely on state machine. VDR-U20-C091 VDR-U20-C094 |
| 7 | Roles / permissions | Public routes; processing happens in sudo. Authentication is the sole control. VDR-U20-C113 VDR-U20-C115 |
| 8 | Scheduled / automated | Post-processing cron/poll follows (CAP-U12-08); no retry scheduling in add-ons. |
| 9 | Exception / failure | Handled ValidationError acknowledged (Stripe); Forbidden returned to gateway; malformed payload raises 500 (Paymob, Stripe header, Flutterwave). VDR-U20-C097 VDR-U20-C134 VDR-U20-C096 |
| 10 | Accounting / audit / security | A forged confirmed state would post a real payment and release goods; hence the weakness register. VDR-U20-C150 VDR-U20-C117 |

**DB reconciliation (configuration only).** No transactions or tokens exist, all providers except demo (test) and cash on delivery (enabled) are disabled with empty credentials; therefore the webhook controllers are routable but any message for a real transaction cannot match. Routes are not stored in the DB (controllers). VDR-U20-C234

**Unknown / Runtime (RT) list.**
- RT: Toss forged-webhook chain (W-01), DPO TransID reuse (W-03), Razorpay redirect binding (W-04), PayPal forced error (W-06), Adyen pre-verification child creation and rollback (W-07), Stripe header parsing under secret rotation, Mercado Pago payment-id path manipulation.
- RT: behaviour of gateways when the shop returns 403/500 to a notification (retry policy).
- UNKNOWN: whether a WAF or proxy limits public callbacks.

## CAP-U20-04 Amount and currency validation and state translation

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 — Business purpose and process semantics.** Even for authenticated messages the engine compares amount and currency, then each add-on translates gateway codes into shop states. This prevents paying a cheaper amount or a different currency and keeps the transaction state machine consistent. VDR-U20-C158 VDR-U20-C159 VDR-U20-C160

**D2 — Architecture, data and object relationships.** `_validate_amount` (engine) -> `_extract_amount_data` (add-on) returns `{amount, currency_code, precision_digits?}` or `None`; `_apply_updates` (add-on) calls `_set_pending/_set_authorized/_set_done/_set_canceled/_set_error`; engine `_update_state` records `state_message`, `last_state_change`, resets `is_post_processed`. Minor-unit table `CURRENCY_MINOR_UNITS` (THB 2). VDR-U20-C162 VDR-U20-C181

**D3 — Source, technical and workflow logic.**
`_process`: `validate_amount -> (error? stop) -> apply_updates -> tokenize`. Amount rule: floor(shop amount, precision) == message amount; refunds negated; currency name equality. Opt-outs and config-sourced currency are in the matrix:

| Provider | Amount source | Currency source | Precision | Opt-out / note |
|---|---|---|---|---|
| Stripe | PaymentIntent/Refund amount | message currency | table (ISK, UGX, MGA) | VDR-U20-C174 |
| Adyen | notification amount | message | table (CLP, CVE, IDR, ISK) | skip for redirect/3DS/refused VDR-U20-C166 |
| APS | amount (minor units) | message currency | default | |
| AsiaPay | Amt | provider's single currency | default | VDR-U20-C169 |
| Authorize.Net | transaction details authAmount | provider's currency | default | skip on API error VDR-U20-C167 VDR-U20-C170 |
| Buckaroo / DPO / Flutterwave / Mollie / PayPal / Paymob / Worldline / Xendit(card) | message | message | default (Xendit table) | |
| ECPay | TradeAmt | tx currency | default | VDR-U20-C171 |
| Iyzico | price | currency | default | |
| Mercado Pago | additional_info item unit_price (redirect/direct) or transaction_amount (token) | message | table | VDR-U20-C059 |
| Nuvei | totalAmount | message | 0 for integer-only methods | skip for empty message VDR-U20-C168 |
| PayU | amount | tx currency | default | VDR-U20-C172 |
| Razorpay | entity amount | message | default | skip on redirect return VDR-U20-C142 |
| Redsys | Ds_Amount | numeric ISO currency | default | |
| Toss | totalAmount | constant KRW | default | VDR-U20-C173 |
| Custom / Demo | none | none | n/a | VDR-U20-C164 VDR-U20-C165 |

State mapping per gateway: Stripe VDR-U20-C182 VDR-U20-C183; Adyen VDR-U20-C184; APS VDR-U20-C185; AsiaPay VDR-U20-C186; Authorize.Net VDR-U20-C187; Buckaroo VDR-U20-C188; DPO VDR-U20-C189; ECPay VDR-U20-C190; Flutterwave VDR-U20-C191; Iyzico VDR-U20-C192; Mercado Pago VDR-U20-C193; Mollie VDR-U20-C194 VDR-U20-C195; Nuvei VDR-U20-C196; Paymob VDR-U20-C197; PayPal VDR-U20-C198; PayU VDR-U20-C199; Razorpay VDR-U20-C200; Redsys VDR-U20-C201; Toss VDR-U20-C202; Worldline VDR-U20-C203; Xendit VDR-U20-C204. Thai-baht rounding at Xendit: VDR-U20-C178 VDR-U20-C179 VDR-U20-C180.

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Message amount equals floored shop amount and currency equals -> `_apply_updates` sets the mapped state. VDR-U20-C158 VDR-U20-C159 |
| 2 | Reversal / cancel / negative | Refund amounts compared negated; amount mismatch -> `error` with message and no further updates. VDR-U20-C161 VDR-U20-C162 |
| 3 | Multi-company / data scope | Currency is the transaction's; provider-level single currency for AsiaPay/Authorize.Net/Paymob/MP. VDR-U20-C169 |
| 4 | Side effects / cross-module | State changes reset `is_post_processed`, trigger posting and sale-order confirmation downstream. VDR-U20-C205 |
| 5 | Configuration / optionality | Provider message fields supply customer-facing text; empty message suppresses notice. VDR-U20-C205 |
| 6 | Validation / constraints | Floor rounding, currency equality, `authorized` requires manual-capture support. VDR-U20-C158 VDR-U20-C195 |
| 7 | Roles / permissions | n/a (system processing in sudo). |
| 8 | Scheduled / automated | n/a here. |
| 9 | Exception / failure | Unknown codes -> error; Authorize.Net skips amount check on API error (fail-open); Razorpay redirect skips. VDR-U20-C167 VDR-U20-C142 |
| 10 | Accounting / audit / security | THB truncation at Xendit; opt-outs; DPO treats pre-authorization as paid. VDR-U20-C180 VDR-U20-C189 |

**DB reconciliation (configuration only).** Active currencies THB and USD only; company currency THB (so THB precision is the one that matters); `payment_provider.available_currency_ids` explicit for buckaroo 8, ecpay 1, flutterwave 22, iyzico 8, mollie 30, nuvei 9, paypal 24, payu 1, razorpay 92, toss 1, xendit 7 currencies; `asiapay_secure_hash_function` = sha1 on all 25 rows. VDR-U20-C292

**Unknown / Runtime (RT) list.**
- RT: Mercado Pago echo of unit price vs charged amount (W-02); Xendit satang truncation at runtime (W-08); Mollie `authorized` constraint effect.
- UNKNOWN: complete gateway response-code tables beyond the constants read.

## CAP-U20-05 Credential storage, access and logging

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 — Business purpose and process semantics.** Gateway credentials are the keys to the merchant's money. The system stores them on the provider record, masks them in the form (`password="True"`), restricts reading to administrators, and blanks them when a database is neutralized. Saved payment methods hold only gateway references and last digits. VDR-U20-C206 VDR-U20-C211 VDR-U20-C231

**D2 — Architecture, data and object relationships.** Fields on `payment.provider` per add-on (see matrix). Access: model ACL `payment_provider_system` (system only), company rule `parent_of`; `payment.token` readable by employee/portal/public ACL but restricted by own-partner rule; `payment.transaction` system plus invoicing (account_payment). Logging uses `get_payment_logger(name, sensitive_keys)` with a global `SENSITIVE_KEYS` set extended by Stripe and Toss. VDR-U20-C207 VDR-U20-C208 VDR-U20-C209 VDR-U20-C210 VDR-U20-C220

**D3 — Source, technical and workflow logic.** Credential matrix (field-level group restriction as read from field definitions; `sys` = `groups='base.group_system'`, `open` = no groups argument):

| Provider | Secret / identifier fields |
|---|---|
| Stripe | publishable key open; secret key sys; webhook secret sys |
| Adyen | merchant account sys; API key sys; HMAC key sys; client key open; URL prefix open |
| APS | merchant identifier open; access code sys; SHA request phrase sys; SHA response phrase sys |
| AsiaPay | merchant id open; secure hash secret sys; brand and hash function open |
| Authorize.Net | login open; transaction key sys; signature key sys (never used); client key open |
| Buckaroo | website key open; secret key sys |
| DPO | service ref open; company token sys |
| ECPay | merchant id open; hash key sys; hash IV sys |
| Flutterwave | public key open; secret key sys; webhook secret sys |
| Iyzico | key id open; key secret sys |
| Mercado Pago | access token, expiry, refresh token, public key sys |
| Mollie | API key sys |
| Nuvei | merchant identifier open; site identifier sys; secret key sys |
| Paymob | public key open; secret key sys; **HMAC key open; API key open** |
| PayPal | email, client id open; client secret sys; access token and expiry sys; webhook id open |
| PayU | key id open; merchant salt sys |
| Razorpay | key id open; key secret, webhook secret, account id, refresh/public/access tokens, expiry sys |
| Redsys | merchant code, terminal open; secret key sys |
| Toss Payments | client key open; secret key sys; per-payment secret on transaction sys |
| Worldline | **pspid, API key, API secret, webhook key, webhook secret all open** |
| Xendit | public key, secret key, webhook token sys |
| Custom / Demo | none |

VDR-U20-C215 VDR-U20-C216 VDR-U20-C217 VDR-U20-C218 VDR-U20-C229 VDR-U20-C230

Logging: base mask set empty, Stripe adds `client_secret`, Toss adds `secret`; request payloads and full responses are logged at info; controllers log full notifications; Authorize.Net and onboarding controllers use the plain logger. VDR-U20-C220 VDR-U20-C221 VDR-U20-C223 VDR-U20-C224 VDR-U20-C225 VDR-U20-C226 VDR-U20-C227 VDR-U20-C228 Neutralization: VDR-U20-C034 VDR-U20-C036.

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Admin enters credentials (password fields) -> provider enabled -> credentials used server side in sudo for API calls. VDR-U20-C211 |
| 2 | Reversal / cancel / negative | `action_reset_credentials` disables and unpublishes and clears provider-specific values (Mercado Pago, PayU, Razorpay implement `_get_reset_values`). |
| 3 | Multi-company / data scope | Provider rule `parent_of company_ids`; each company's provider holds its own credentials. VDR-U20-C209 |
| 4 | Side effects / cross-module | OAuth token refresh writes tokens back to the provider row during payment requests. VDR-U20-C230 |
| 5 | Configuration / optionality | Required credentials by add-on (`required_if_provider`); PayU and Razorpay validate credentials only when state changes (Mercado Pago also when its access token changes). VDR-U20-C139 |
| 6 | Validation / constraints | Authorize.Net signature key mandatory but unused. VDR-U20-C109 |
| 7 | Roles / permissions | ACL: system only for providers; tokens: all users read, own-partner rule; transactions: system and invoicing. VDR-U20-C206 VDR-U20-C207 VDR-U20-C208 |
| 8 | Scheduled / automated | OAuth refresh occurs lazily when building request headers (PayPal, Mercado Pago, Razorpay). VDR-U20-C230 |
| 9 | Exception / failure | Missing/blank credential: ValidationError at provider write; at runtime API 401 errors surface as transaction error. VDR-U20-C030 |
| 10 | Accounting / audit / security | Worldline/Paymob secret fields lack field-level restriction; masks incomplete; plain-text storage. VDR-U20-C215 VDR-U20-C217 VDR-U20-C225 |

**DB reconciliation (configuration only).** `ir_model_access` rows for payment models: payment.provider.system (full, Administrator), payment.method.* (public/portal/user read; system full), payment.token.* (public/portal/user read; system full), payment.transaction.system (full), payment.transaction.user (Invoicing read/write/create), payment.capture.wizard (user), payment.link.wizard (Invoicing), payment.refund.wizard (Invoicing), plus sale's link-wizard row; `ir_rule` rows: provider company, transaction company, token user, token company, capture wizard (+ account_payment 'Access every payment transaction/token' rows seen in the DB listing). All 68 credential/identifier columns (counted by script, values never read) are NULL on all 25 rows; `paypal_access_token_expiry` carries the 1970-01-01 default on all rows. VDR-U20-C234 VDR-U20-C235

**Unknown / Runtime (RT) list.**
- UNKNOWN: production secret handling (environment injection, encryption at rest).
- RT: that `sudo` code paths never expose open credential fields to non-admin users (e.g. website forms, exports) — worldline/paymob open fields.
- UNKNOWN: contents of server logs in production.

## CAP-U20-06 Capture, void, refund and saved payment methods

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 — Business purpose and process semantics.** Beyond the first payment: save the payment method (tokenization) for later off-session charges; authorize now and capture or void later; refund from the transaction form. Only gateways that implement the corresponding hooks expose these features. VDR-U20-C236 VDR-U20-C245

**D2 — Architecture, data and object relationships.** Provider feature fields `support_tokenization`, `support_manual_capture`, `support_refund`, `support_express_checkout` (computed, add-on overrides) and per-method fields on `payment.method`. Child transactions link via `source_transaction_id`; tokens (`payment.token`) hold `provider_ref` and `payment_details` plus per-gateway fields (Stripe `stripe_payment_method`, `stripe_mandate`; Adyen `adyen_shopper_reference`; Authorize.Net profile id; Flutterwave customer email; Mercado Pago customer id; Razorpay combined ref; Demo simulated state). VDR-U20-C246 VDR-U20-C247 VDR-U20-C260 VDR-U20-C261

**D3 — Source, technical and workflow logic.** Capture/void/refund: `action_capture/void/refund` (CAP-U12-08) -> `_capture/_void/_refund` -> child tx -> `_send_*_request` -> `_process`; the source transaction is finalized when children sum to its amount. VDR-U20-C248 VDR-U20-C249 VDR-U20-C250
Tokenization: `tokenize` decided by portal controller VDR-U20-C257; `_process` -> `_tokenize` -> provider `_extract_token_values` VDR-U20-C259; token-owner check VDR-U20-C258.
Gateway specifics: Authorize.Net void-vs-refund VDR-U20-C254; Razorpay no void VDR-U20-C255, 36-hour pending guard VDR-U20-C256; refunds started at the gateway: Stripe VDR-U20-C251, Adyen VDR-U20-C252, Razorpay VDR-U20-C253.
Feature matrix: Stripe VDR-U20-C236; Adyen VDR-U20-C237; Authorize.Net VDR-U20-C238; Razorpay VDR-U20-C239; Flutterwave VDR-U20-C240.

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Customer ticks "save" -> `tokenize` true -> gateway returns token -> token created -> later `_charge_with_token`. VDR-U20-C257 VDR-U20-C259 |
| 2 | Reversal / cancel / negative | Void of authorized; refund child with negative amount; Authorize.Net void-instead-of-refund; Razorpay cannot void. VDR-U20-C246 VDR-U20-C254 VDR-U20-C255 |
| 3 | Multi-company / data scope | Tokens belong to provider (company) and partner; other commercial partner -> AccessError. VDR-U20-C258 |
| 4 | Side effects / cross-module | Refund done -> post-processing creates a refund payment (CAP-U12-08); tokens archived when provider leaves enabled/test. VDR-U20-C008 |
| 5 | Configuration / optionality | `capture_manually` per provider only with methods supporting it; allow_tokenization per provider; mandate max amounts (Razorpay/Stripe INR mandates). VDR-U20-C257 |
| 6 | Validation / constraints | Only done tx refundable; provider not disabled; archived token cannot be used; refund bounds in wizard (U12). VDR-U20-C249 VDR-U20-C250 |
| 7 | Roles / permissions | Invoicing role has transaction ACL; refund wizard Invoicing (U12). VDR-U20-C208 |
| 8 | Scheduled / automated | Refund-done triggers the post-process cron immediately for several gateways (Stripe, Adyen, Razorpay, Authorize.Net, Demo). VDR-U20-C251 |
| 9 | Exception / failure | Send-step ValidationError -> child tx error; Stripe refund failure after success message set error from done. VDR-U20-C248 |
| 10 | Accounting / audit / security | Tokens store no PAN; gateways without refund support require manual dashboard refund + manual accounting. VDR-U20-C231 VDR-U20-C245 |

**DB reconciliation (configuration only).** `payment_method` rows: 232 (181 primary, 51 brands); active: cash_on_delivery and demo only; `support_tokenization` true for demo (and card methods are inactive); provider `allow_tokenization` true on adyen, authorize, demo, flutterwave, stripe, worldline; `capture_manually` is empty on all rows; no tokens, no transactions. VDR-U20-C236

**Unknown / Runtime (RT) list.**
- RT: rounding behaviour of partial-capture sums; gateway-side authorization expiry.
- RT: Stripe SCA migration path (`_stripe_sca_migrate_customer`) not exercised.
- UNKNOWN: capture/void wizard views were not read.

## CAP-U20-07 Availability, currencies, countries and Thailand relevance

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 — Business purpose and process semantics.** The checkout offers only providers and methods that can serve the customer's country, the document currency and the amount. Thailand relevance: the company's currency is THB, so THB acceptance and Thai wallet/bank methods decide which gateways could ever be useful. VDR-U20-C262 VDR-U20-C266 VDR-U20-C292

**D2 — Architecture, data and object relationships.** `payment.provider.available_country_ids`, `available_currency_ids` (computed stored from `_get_supported_currencies`, writable), `maximum_amount`; `payment.method.supported_country_ids/supported_currency_ids`; per-provider constants (supported currency lists, single-currency constraints, supported countries for onboarding). The Thai method records (country TH, currency THB) live in `payment/data/payment_method_data.xml`. VDR-U20-C267 VDR-U20-C283 VDR-U20-C284

**D3 — Source, technical and workflow logic.** Provider filter chain: company/state -> published -> country -> max amount (converted at today's rate) -> currency -> tokenization -> express checkout; payment-method filter chain follows. VDR-U20-C262 VDR-U20-C263 VDR-U20-C264 VDR-U20-C265 VDR-U20-C266 VDR-U20-C268

Currency matrix: restricted by list - Buckaroo (EUR GBP PLN DKK NOK SEK CHF USD), ECPay (TWD), Flutterwave, Iyzico (CHF EUR GBP IRR NOK RUB TRY USD), Mollie (30 currencies incl. THB), Nuvei (LatAm), PayPal (24 incl. THB), PayU (INR), Razorpay (large list incl. THB), Toss (KRW), Xendit (IDR MYR PHP SGD THB USD VND); single-currency by constraint - AsiaPay (code table includes THB), Authorize.Net, Paymob (AED EGP OMR SAR), Mercado Pago; no list - Adyen, APS, DPO, Redsys, Stripe, Worldline, Demo, Custom. VDR-U20-C270 VDR-U20-C277 VDR-U20-C278 VDR-U20-C279 VDR-U20-C280 VDR-U20-C281

Thailand: Thai methods and their carriers VDR-U20-C285 VDR-U20-C286 VDR-U20-C287 VDR-U20-C288 VDR-U20-C289 VDR-U20-C290 VDR-U20-C291.

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | THB invoice, Thai customer: Stripe/Adyen/AsiaPay/Xendit offer PromptPay; Xendit/AsiaPay offer TrueMoney and LINE Pay; PayPal/Mollie/Razorpay accept THB cards. VDR-U20-C291 VDR-U20-C278 |
| 2 | Reversal / cancel / negative | Disabling a provider deactivates methods unique to it. VDR-U20-C009 |
| 3 | Multi-company / data scope | Provider selection uses company parent_of domain. VDR-U20-C262 |
| 4 | Side effects / cross-module | Unsupported currency at gateways without a list fails at the gateway after redirect; Xendit/ECPay/Nuvei truncate decimals. VDR-U20-C267 VDR-U20-C180 |
| 5 | Configuration / optionality | Country/currency/max-amount fields are editable by admin; empty means all. VDR-U20-C264 VDR-U20-C266 |
| 6 | Validation / constraints | Single-currency constraints (AsiaPay, Authorize.Net, Paymob, MP); ECPay TWD and Toss KRW and PayU INR only. VDR-U20-C270 |
| 7 | Roles / permissions | Administrator edits provider; public sees published providers only. VDR-U20-C263 |
| 8 | Scheduled / automated | n/a. |
| 9 | Exception / failure | Gateway rejects unsupported currency after the redirect -> error state with message. VDR-U20-C268 |
| 10 | Accounting / audit / compliance | Thai VAT/withholding handling is outside this unit (U13); no Thai domestic acquirer add-on exists in the community tree read. VDR-U20-C291 |

**DB reconciliation (configuration only).** Company currency THB, active currencies THB and USD (EUR, KRW, TWD, INR inactive); one country row TH exists; 16 payment methods carry country TH and 17 carry THB, all inactive; provider-method links for Thai methods: promptpay -> adyen, asiapay, stripe, xendit; truemoney, linepay, scb, krungthai_bank, bangkok_bank -> asiapay and xendit; shopeepay -> xendit; online_banking_thailand -> adyen; alipay_plus -> worldline; rabbit_line_pay, ttb, tmb, kasikorn_bank, bank_of_ayudhya, hoolah, pace -> asiapay. VDR-U20-C291 VDR-U20-C292

**Unknown / Runtime (RT) list.**
- RT: whether each gateway really accepts THB and PromptPay for a Thai merchant account (commercial/contractual, not in source).
- UNKNOWN: minimum/maximum PromptPay amounts and QR expiry.
- UNKNOWN: whether Thai e-tax or tax invoice rules interplay with online payment confirmation (U13 scope).

## CAP-U20-08 Offline payment modes (wire transfer and cash on delivery)

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 — Business purpose and process semantics.** Wire transfer and cash on delivery let the customer place an order without an online gateway. The system records a transaction in pending state, shows bank/collection instructions, sends the quotation or confirms the order (COD) and leaves money matching to accounting. VDR-U20-C297 VDR-U20-C300

**D2 — Architecture, data and object relationships.** `payment.provider` with `code='custom'` and `custom_mode` (`wire_transfer` from payment_custom, `cash_on_delivery` from delivery); `qr_code` Boolean; payment method `wire_transfer` (inactive by default) and `cash_on_delivery`; redirect form view `payment_custom.redirect_form` posting to `/payment/custom/process`; delivery carrier flag `allow_cash_on_delivery`. VDR-U20-C293 VDR-U20-C294 VDR-U20-C302 VDR-U20-C301

**D3 — Source, technical and workflow logic.** `draft -> pending` [POST /payment/custom/process -> `_process('custom')` -> `_apply_updates` -> `_set_pending`] VDR-U20-C113 VDR-U20-C114 VDR-U20-C297; sale post-process of pending: send quotation, set order reference for custom VDR-U20-C299; delivery post-process: confirm draft orders for COD VDR-U20-C300; wire pending message regeneration from bank journals VDR-U20-C295; communication selection VDR-U20-C296; custom transactions excluded from the "received" log VDR-U20-C304.

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Customer selects Wire Transfer -> draft tx -> redirect form posts -> pending -> quotation sent; payment registered later in accounting. VDR-U20-C297 VDR-U20-C299 |
| 2 | Reversal / cancel / negative | No automatic reversal; pending can be cancelled by backend actions (engine). VDR-U20-C304 |
| 3 | Multi-company / data scope | Bank accounts listed per provider company; provider per company. VDR-U20-C295 |
| 4 | Side effects / cross-module | COD confirms draft sale orders; wire sends quotation; order reference changed for custom. VDR-U20-C300 VDR-U20-C299 |
| 5 | Configuration / optionality | Wire disabled/inactive by default; COD enabled and published on install but only offered when carrier allows. VDR-U20-C302 VDR-U20-C303 VDR-U20-C301 |
| 6 | Validation / constraints | custom_mode constraint; no amount check. VDR-U20-C293 VDR-U20-C164 |
| 7 | Roles / permissions | Public route; provider edit admin only. VDR-U20-C113 VDR-U20-C206 |
| 8 | Scheduled / automated | Post-process cron handles pending transactions (quotation email, COD order confirmation). VDR-U20-C300 |
| 9 | Exception / failure | Unknown reference: engine ignores; disabled provider can still be driven (creation not gated). VDR-U20-C305 VDR-U20-C039 |
| 10 | Accounting / audit / security | No payment is posted by offline transactions; unauthenticated processing route (W-13). VDR-U20-C304 VDR-U20-C305 |

**DB reconciliation (configuration only) — payment_custom (installed) and delivery COD.** Source seeds (payment_custom data): provider `payment.payment_provider_transfer` gets `code=custom`, `custom_mode=wire_transfer`, `redirect_form_view_id=payment_custom.redirect_form`, `pending_msg` cleared then recomputed, payment method link wire_transfer (inactive). DB row 22 `Wire Transfer`: code custom, mode wire_transfer, disabled, unpublished, sequence 30, redirect view 3588 (= `payment_custom.redirect_form`), pending message begins with the "transfer details/Bank Accounts" heading (no bank accounts listed: the single bank journal has no bank account and res_partner_bank is empty), `qr_code` empty, `allow_tokenization` false. Delivery seeds `delivery.payment_provider_cod`: code custom, mode cash_on_delivery, company main, enabled, published, pending_msg "The delivery staff will collect payment upon delivery." and redirect view the same `payment_custom.redirect_form`; DB row 25 matches exactly (enabled, published, redirect view 3588, sequence empty). Payment methods: `wire_transfer` inactive; `cash_on_delivery` active. 6 delivery carriers, 0 with `allow_cash_on_delivery`. No `account_payment_method_line` row for either provider (3 rows total: manual in, manual out, checks). Id-level reconciliation for payment_custom: source declares 6 own ids (views custom_state_header, payment_method_form, payment_provider_form, redirect_form, token_form; payment method payment_method_wire_transfer) plus 1 foreign-namespace record (`payment.payment_provider_transfer`, B01 foreign_ns 1); DB `ir_model_data` for the module has exactly those 6 (missing 0, extra 0) plus technical rows (2 models, 1 constraint, 7 fields, 2 selection values); no ACL, rule, cron, group or automation rows are declared by the module or present for it. VDR-U20-C306 VDR-U20-C307

**Unknown / Runtime (RT) list.**
- RT: sale-order confirmation under COD in a real flow; rendering of the bank-details message with real bank accounts.
- UNKNOWN: `qr_code` effect without the accounting app.
- UNKNOWN: reconcile of wire payments (accounting, U12).

## CAP-U20-09 Demo gateway

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 — Business purpose and process semantics.** A fake gateway for demonstrations and tests: the user picks the result on screen. It supports tokenization, manual capture, void and refund simulation, express checkout. VDR-U20-C310 VDR-U20-C311

**D2 — Architecture, data and object relationships.** `payment.provider` code `demo` (constraint state in test/disabled), payment method `demo` (tokenization, partial capture, partial refund), `payment.token.demo_simulated_state`, `payment.transaction` buttons `action_demo_set_done/canceled/error`, controller `/payment/demo/simulate_payment`, portal controller override that re-checks compatibility. VDR-U20-C308 VDR-U20-C313 VDR-U20-C040

**D3 — Source, technical and workflow logic.** `draft -> pending|done|authorized|cancel|error` [simulated_state in `_apply_updates`]; `done` becomes `authorized` when `capture_manually` and not a manual capture/refund VDR-U20-C310; token charges use the token's stored simulated state; amounts never checked VDR-U20-C165; public route accepts arbitrary data VDR-U20-C312 VDR-U20-C115.

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Customer chooses Demo -> selects "confirmed" -> transaction done -> post-processing creates payment. VDR-U20-C310 |
| 2 | Reversal / cancel / negative | Simulated cancel/error states; void/refund simulated. VDR-U20-C310 |
| 3 | Multi-company / data scope | Provider per company; demo token bound to partner. VDR-U20-C313 |
| 4 | Side effects / cross-module | Done demo transactions post payments, confirm orders, send invoices exactly like real ones (account_payment/sale). VDR-U20-C310 |
| 5 | Configuration / optionality | Shipped as test + published; admin may disable; cannot be set to enabled. VDR-U20-C308 VDR-U20-C309 |
| 6 | Validation / constraints | State constraint; portal compatibility check. VDR-U20-C308 VDR-U20-C040 |
| 7 | Roles / permissions | Public simulation route; backend buttons for users with transaction write rights. VDR-U20-C312 VDR-U20-C311 |
| 8 | Scheduled / automated | Post-process cron (CAP-U12-08). |
| 9 | Exception / failure | Unknown state -> error with message. VDR-U20-C310 |
| 10 | Accounting / audit / security | Risk: demo provider active in a production-like DB lets payments be marked done with no money (W-12). VDR-U20-C314 VDR-U20-C315 |

**DB reconciliation (configuration only) — payment_demo (installed).** Source seeds: `payment.payment_provider_demo`: code demo, state test, is_published True, inline/token-inline/express-checkout views, allow_tokenization, allow_express_checkout, method link demo; method `demo` active with support_tokenization True, manual capture partial, refund partial, express False. DB row 6 `Demo`: code demo, state test, published, allow_tokenization true, sequence 40, inline form view present; matches the source. DB method `demo` active, tokenization true, express false, refund partial. Id-level reconciliation for payment_demo: source declares 9 own ids (views express_checkout_form, express_inline_form, inline_form, payment_details, payment_provider_form, payment_token_form, payment_transaction_form, token_inline_form; payment method payment_method_demo) plus 1 foreign-namespace record (`payment.payment_provider_demo`); DB has exactly those 9 (missing 0, extra 0) plus 3 models, 9 fields, 5 selection values; no ACL, rule, cron, group or automation rows. No transactions, no tokens in DB. Provider flag allow_express_checkout is true on the demo and stripe rows (source data sets it for demo). No account.payment.method.line row for the demo provider yet (journal is computed lazily). VDR-U20-C314 VDR-U20-C309

**Unknown / Runtime (RT) list.**
- RT: whether the demo provider shows on the customer portal and storefront of this installation.
- UNKNOWN: payment-method-line/journal creation timing for the demo provider.

## CAP-U20-10 External connectivity and merchant onboarding

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 — Business purpose and process semantics.** Gateway add-ons call external services (APIs, hosted checkouts) and four use vendor-run proxies for OAuth/Connect onboarding and token refresh. Administrators can register callbacks at the gateway from within the ERP (Stripe, PayPal, Razorpay). VDR-U20-C344 VDR-U20-C345

**D2 — Architecture, data and object relationships.** Request helpers on `payment.provider` (`_send_api_request`, `_build_request_*`, `_parse_response_*`, proxy JSON-RPC wrapper `_prepare_json_rpc_payload`); onboarding controllers (`auth='user'`) with CSRF validation; provider actions (`action_start_onboarding`, `action_*_create_webhook`, `action_reset_credentials`). VDR-U20-C343 VDR-U20-C340 VDR-U20-C341 VDR-U20-C342

**D3 — Source, technical and workflow logic.** Endpoint inventory (host per provider; all RT): see the claims immediately below in the claims table with condition `provider installed` and flag RT (Stripe, Adyen, APS, AsiaPay, Authorize.Net, Buckaroo, DPO, ECPay, Flutterwave, Iyzico, Mercado Pago, Mollie, Nuvei, Paymob, PayPal, PayU, Razorpay, Redsys, Toss, Worldline, Xendit). Onboarding: `action_start_onboarding` -> redirect to vendor proxy `/authorize` -> return to `/payment/<code>/oauth/return` (CSRF checked) -> exchange authorization code via proxy -> write credentials + enable + publish. VDR-U20-C340 VDR-U20-C341 VDR-U20-C342 Callback auto-registration VDR-U20-C345 VDR-U20-C346 VDR-U20-C347. Offline reachability risk VDR-U20-C348.

**Ten-dimension table**

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Admin clicks Connect -> vendor proxy -> OAuth -> credentials saved -> provider enabled and published; webhook created automatically (Razorpay) or by button (Stripe, PayPal). VDR-U20-C341 VDR-U20-C347 |
| 2 | Reversal / cancel / negative | Authorization cancelled -> redirect back to provider form without change; reset credentials action disables and unpublishes. VDR-U20-C341 |
| 3 | Multi-company / data scope | Onboarding uses the provider id of the current company; Stripe account country from the provider's company. VDR-U20-C344 |
| 4 | Side effects / cross-module | Credentials + `state=enabled` + `is_published=True` written in one step; cron toggled. VDR-U20-C341 VDR-U20-C012 |
| 5 | Configuration / optionality | Test vs live host from provider state; Adyen/Paymob prefixes. |
| 6 | Validation / constraints | CSRF token required; Stripe country must be in SUPPORTED_COUNTRIES; PayPal webhook creation refuses localhost. VDR-U20-C340 VDR-U20-C344 VDR-U20-C346 |
| 7 | Roles / permissions | Onboarding routes `auth='user'`; credential write needs administrator by ACL. VDR-U20-C343 VDR-U20-C206 |
| 8 | Scheduled / automated | Access token refresh is lazy at request time (no cron). VDR-U20-C230 |
| 9 | Exception / failure | Proxy errors render an authorization-error page; API timeouts after 10 s. VDR-U20-C028 |
| 10 | Accounting / audit / security | Vendor-run proxies hold OAuth exchange; callbacks must be publicly reachable; no source-level pinning of hosts beyond TLS. VDR-U20-C341 VDR-U20-C348 |

**DB reconciliation (configuration only).** No provider carries OAuth tokens or credentials; `payment_provider` has no row with `razorpay_account_id`/`mercado_pago_access_token`/`paypal_webhook_id` set; the action `payment_stripe.action_payment_provider_onboarding` exists as the only ir.actions.act_window row seeded by payment_stripe (DB seeds: payment_stripe act_window 1). VDR-U20-C234

**Unknown / Runtime (RT) list.**
- RT: all outbound traffic and proxies; certificate validation behaviour of `requests`.
- UNKNOWN: vendor proxy availability, data retention and contract terms.
- UNKNOWN: egress policy of the target deployment.

## Weakness register (security-relevant findings with pointers)

| ID | Finding | Suggested review priority | Evidence class | Summary | Claims |
|---|---|---|---|---|---|
| W-01 | Toss Payments webhook can be forged to confirm a payment | HIGH (suggested review priority) | INFERENCE / RT | Signature check skipped for EXPIRED/ABORTED; message secret overwrites the stored secret; non-DONE statuses map to error; error -> done is an allowed transition; chain: ABORTED(secret=X, amount=tx amount) then DONE(secret=X, amount=tx amount). Needs a known reference. Korean gateway, KRW only. | VDR-U20-C146 VDR-U20-C147 VDR-U20-C148 VDR-U20-C149 VDR-U20-C150 VDR-U20-C089 VDR-U20-C151 |
| W-02 | Mercado Pago direct payment trusts browser-supplied amount | HIGH (suggested review priority) | INFERENCE / RT | Public route, no access token, amount overwritten from the browser; later check reads echoed item price instead of charged amount. Latin-American gateway; not Thailand. | VDR-U20-C057 VDR-U20-C058 VDR-U20-C059 |
| W-03 | DPO return does not tie gateway answer to the transaction; XML built unescaped | MEDIUM | FACT lines / RT effect | verifyToken answer merged into URL data and processed on the transaction found from the URL reference; no CompanyRef comparison; no uniqueness check on the gateway id; customer and TransID values placed in XML unescaped. | VDR-U20-C116 VDR-U20-C117 VDR-U20-C118 VDR-U20-C119 VDR-U20-C051 |
| W-04 | Razorpay redirect return: amount unchecked, reference tie client-controlled | MEDIUM-LOW | FACT lines / RT effect | Signature covers order and payment ids only; amount validation skipped when redirecting; description compared with the shop reference is set by the browser script. | VDR-U20-C141 VDR-U20-C142 VDR-U20-C143 VDR-U20-C144 |
| W-05 | Static shared token authentication (Flutterwave, Xendit) | MEDIUM-LOW | FACT | Header token independent of the message; leaked token allows forging any notification; no per-message MAC. | VDR-U20-C122 VDR-U20-C155 |
| W-06 | PayPal: failed origin verification sets the transaction to error | LOW | FACT / RT | ValidationError from the verification call (not Forbidden) is caught and sets error on an unauthenticated message naming a known reference; recoverable because error -> done is allowed. | VDR-U20-C136 VDR-U20-C135 VDR-U20-C089 |
| W-07 | Adyen: details and return routes without tamper token; child transactions created before signature check | LOW-MEDIUM | FACT / RT | Public routes accept reference and payment details; return route rewrites the operation; search before verification may create child transactions (rolled back on Forbidden). | VDR-U20-C082 VDR-U20-C083 VDR-U20-C100 VDR-U20-C101 |
| W-08 | Xendit truncates Thai baht (and other currencies) to whole units | MEDIUM (Thailand-relevant) | FACT / INFERENCE | Zero-decimal table includes THB; amount floored when sent and when validated, so up to 0.99 THB per transaction is under-collected but recorded in full. | VDR-U20-C178 VDR-U20-C179 VDR-U20-C180 VDR-U20-C181 |
| W-09 | Secret fields without administrator-only restriction; unused signature key | LOW-MEDIUM (defence in depth) | INFERENCE | Worldline (five fields) and Paymob (HMAC key, API key) lack the field-level group; Authorize.Net requires a signature key it never uses. | VDR-U20-C215 VDR-U20-C216 VDR-U20-C217 VDR-U20-C218 VDR-U20-C109 |
| W-10 | Incomplete log masking | LOW | FACT | Mask set holds two keys; request payloads, full responses and complete notifications (with customer data) are logged; several flows use the unmasked logger. | VDR-U20-C220 VDR-U20-C221 VDR-U20-C224 VDR-U20-C225 VDR-U20-C226 VDR-U20-C227 VDR-U20-C228 |
| W-11 | Vendor-dictated weak constructions and no replay window except Stripe | INFO | FACT | SHA-1 (Buckaroo, AsiaPay default), prefix-hash without delimiters (Nuvei), phrase-wrapped SHA-256 (APS); only Stripe bounds message age; others depend on the state machine. | VDR-U20-C112 VDR-U20-C107 VDR-U20-C129 VDR-U20-C104 VDR-U20-C091 VDR-U20-C087 VDR-U20-C088 |
| W-12 | Demo gateway active and published in the reference database | HIGH for production use | OBSERVATION / RT | Demo provider in test state, published, method active; public simulation route; done demo transactions post payments and confirm orders. | VDR-U20-C314 VDR-U20-C315 VDR-U20-C312 VDR-U20-C309 VDR-U20-C310 |
| W-13 | Offline and demo routes unauthenticated; creation route does not re-check provider availability | LOW-MEDIUM | FACT / INFERENCE | Public routes move transactions to pending (custom) or any state (demo); transaction creation takes a provider id from the client without compatibility or state check. | VDR-U20-C113 VDR-U20-C114 VDR-U20-C305 VDR-U20-C039 VDR-U20-C115 |
| W-14 | Authorize.Net amount check fails open | LOW | FACT | Validation skipped if the transaction-detail lookup errors. | VDR-U20-C167 |
| W-15 | Credential presence validated only on state change (PayU, Razorpay) | LOW | INFERENCE / RT | Clearing the salt after enabling is not caught; PayU would hash with a placeholder salt text. | VDR-U20-C139 |
| W-16 | Robustness: malformed notifications raise 500 (Stripe header, Paymob, Flutterwave); Mollie authorized state conflicts with engine constraint; Mercado Pago payment id in URL path | LOW | INFERENCE / RT |  | VDR-U20-C096 VDR-U20-C134 VDR-U20-C195 VDR-U20-C126 |

## Per-provider delta summary

| Provider (module) | Flow | Notification auth | Features | Currencies / countries | Thailand relevance | DB row (id, state) |
|---|---|---|---|---|---|---|
| Stripe (`payment_stripe`) | embedded (intent + client secret) | HMAC-SHA256 + 10-min window; return pull-verified | express, manual capture (full), refund (partial), tokens | no currency list; onboarding countries incl. TH (beta) | PromptPay, GrabPay, cards; THB unrestricted | 20, disabled |
| Adyen (`payment_adyen`) | embedded (drop-in) | HMAC-SHA256 base64 | manual capture (partial), refund (partial), tokens | no list; special decimals CLP/CVE/IDR/ISK | PromptPay, Online Banking Thailand, Alipay, WeChat | 1, disabled |
| Amazon Payment Services (`payment_aps`) | redirect form | SHA-256 phrase digest | none | no list | no Thai-specific method | 2, disabled |
| AsiaPay (`payment_asiapay`) | redirect form | secureHash SHA1/256/512 (webhook only) | none | single currency from code table (THB 764) | SiamPay brand; TrueMoney, LINE Pay, Rabbit LINE Pay, SCB, KTB, BBL, KBank, BAY, TMB/TTB, PromptPay | 3, disabled |
| Authorize.Net (`payment_authorize`) | embedded (Accept.js opaque data) | none (synchronous) | manual capture (full), refund (full), tokens | single currency by account | none | 4, disabled |
| Buckaroo (`payment_buckaroo`) | redirect form | SHA-1 digital signature | none | EUR GBP PLN DKK NOK SEK CHF USD | none (no THB) | 5, disabled |
| Custom (`payment_custom`) | offline form | none | none | none | n/a | 22 wire transfer disabled; 25 COD enabled (delivery) |
| Demo (`payment_demo`) | simulated | none | all | none | n/a | 6, test, published |
| DPO (`payment_dpo`) | hosted token XML | pull verifyToken only | none | no list | none | 7, disabled |
| ECPay (`payment_ecpay`) | redirect form | CheckMacValue SHA-256 | none | TWD only | none (Taiwan) | 8, disabled |
| Flutterwave (`payment_flutterwave`) | hosted link | static header token; return pull-verified | tokens | 22 currencies, no THB | none | 9, disabled |
| Iyzico (`payment_iyzico`) | hosted checkout form | none; pull + basketId | none | 8 currencies, no THB | none | 10, disabled |
| Mercado Pago (`payment_mercado_pago`) | hosted preference / bricks | none; pull + external_reference | tokens | single currency by account country (AR BR CL CO MX PE UY) | none | 11, disabled |
| Mollie (`payment_mollie`) | hosted payment | none; pull by stored id | none | 30 currencies incl. THB | THB cards only | 12, disabled |
| Nuvei (`payment_nuvei`) | redirect form | SHA-256 prefix checksum | none | 9 LatAm currencies, no THB | none | 13, disabled |
| Paymob (`payment_paymob`) | hosted intention | HMAC-SHA512 + order binding | none | single currency (AED EGP OMR SAR) | none | 14, disabled |
| PayPal (`payment_paypal`) | embedded (JS SDK order) | PayPal verify-webhook-signature API | none (no refund from Odoo) | 24 currencies incl. THB | THB wallet/cards | 15, disabled |
| PayU (`payment_payu`) | redirect form | SHA-512 hash | none | INR only | none | 16, disabled |
| Razorpay (`payment_razorpay`) | embedded checkout script | HMAC-SHA256 | manual capture (full), refund (partial), tokens | 92 currencies incl. THB | THB international cards | 17, disabled |
| Redsys (`payment_redsys`) | redirect form | HMAC-SHA256 (3DES-derived key) | none | no list (EUR in practice) | none | 18, disabled |
| Toss Payments (`payment_toss_payments`) | widget + confirm API | per-payment secret (exemptions) | none | KRW only | none | 21, disabled |
| Worldline (`payment_worldline`) | hosted checkout session | HMAC-SHA256 raw body | tokens | no list | Alipay Plus; cards | 23, disabled |
| Xendit (`payment_xendit`) | hosted invoice / card token | static header token | tokens | IDR MYR PHP SGD THB USD VND (zero decimals) | PromptPay, TrueMoney, LINE Pay, ShopeePay, SCB/KTB/BBL direct debit | 24, disabled |

## DISCOVERED SUPPORTING MODULES

- `payment` (engine; read only for the provider contract: `models/payment_provider.py`, `models/payment_transaction.py`, `models/payment_method.py`, `models/payment_token.py`, `controllers/portal.py`, `utils.py`, `logging.py`, `const.py`, security files, data files). Full study is U12.
- `account_payment` (read `models/payment_provider.py` for journal/payment-method-line creation; ACL file). Studied in U12.
- `sale` (read `models/payment_transaction.py` post-process for pending/authorized/done orders and custom reference).
- `delivery` (read `models/payment_provider.py`, `models/payment_transaction.py`, data files, neutralize.sql; seeds the cash-on-delivery provider and method; carrier flag).
- `website_payment`, `website_sale` (installed/not installed per DB; not read), `pos_online_payment`, `pos_online_payment_self_order`, `website_sale_collect` (found by grep as further `payment.transaction` extenders; not installed or not read), `l10n_th` (installed; not read for this unit), `onboarding` and `portal` (dependencies of `payment`; not read).
- `payment_sepa_direct_debit` (placeholder row in DB; module absent from Community source; not studied).

## Contradictions with prior evidence / task premise

- CONTRA (task premise): the worklist states that only `payment_custom` and `payment_demo` are installed and the others are source-only. The restored DB shows all 23 provider add-ons installed; they are installed but unconfigured. VDR-U20-C085
- Clarification of U12 CAP-U12-08 DB text: the provider row described there as `custom` (enabled) is the Cash on Delivery row owned by module `delivery` (id 25); `payment_custom`'s own Wire Transfer row (id 22) is disabled.

## Consolidated Runtime (RT) list

- All outbound gateway/proxy traffic and gateway retry behaviour (CAP-U20-02/03/10).
- Toss Payments forged-webhook chain (W-01); Mercado Pago under-payment (W-02); DPO payment-id reuse and XML injection (W-03); Razorpay redirect binding (W-04); PayPal forced error (W-06); Adyen pre-verification child creation and details/return routes (W-07); Xendit satang truncation (W-08).
- Whether the demo provider appears on the storefront and portal of this installation (W-12).
- Stripe webhook secret rotation with several v1 signatures; malformed notification handling (W-16).
- Mollie `authorized` message against the engine's manual-capture constraint (W-16).
- Multi-company post-install hooks (provider copies).

## Not read / not determined

- i18n files and unit tests of the add-ons; most QWeb templates and form views (only cited ones); JavaScript front-end beyond the Razorpay and Mercado Pago lines cited.
- Wizards `payment_capture_wizard`, `payment_link_wizard`, `res_config_settings` (outside the provider contract; ACL rows only).
- Engine controller `post_processing.py`, `portal.py` lines 1-250 (U12).
- Production secret handling, network policy, certificates, rate limits.
- Third-party or custom add-ons that may override these hooks in a deployment.

## Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U20-C001 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:37 | No Provider Set | FACT | always | — | payment.provider.code is a selection holding only the placeholder 'none' in the base engine; each provider add-on extends it | N-U20-001 |
| VDR-U20-C002 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_provider.py:26 | selection_add=[('stripe', "Stripe")] | FACT | payment_stripe installed | — | Provider add-ons extend the code selection with selection_add and ondelete set default (example Stripe) | N-U20-001 |
| VDR-U20-C003 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:29 | return name == 'required_if_provider' | FACT | always | — | The field parameter required_if_provider is whitelisted so provider add-ons can declare provider-specific mandatory fields | N-U20-003 |
| VDR-U20-C004 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:381 | p.state in ['enabled', 'test'] | FACT | always | — | _check_required_if_provider only applies to providers in enabled or test state | N-U20-003 |
| VDR-U20-C005 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:339 | providers._check_required_if_provider() | FACT | always | — | Required-if-provider is enforced after create | N-U20-003 |
| VDR-U20-C006 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:359 | self._check_required_if_provider() | FACT | always | — | Required-if-provider is enforced after write | N-U20-003 |
| VDR-U20-C007 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:45 | selection=[('disabled', "Disabled") | FACT | always | — | State selection disabled/enabled/test with default disabled and copy False | N-U20-004 |
| VDR-U20-C008 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:352 | state_changed_providers._archive_linked_tokens() | FACT | always | — | On a state change away from disabled the linked tokens are archived (providers not changing state are untouched) | N-U20-004 |
| VDR-U20-C009 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:361 | deactivated_providers._deactivate_unsupported_payment_methods() | FACT | always | — | After a write, payment methods supported only by disabled providers are deactivated | N-U20-004 |
| VDR-U20-C010 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:362 | activated_providers._activate_default_pms() | FACT | always | — | Providers leaving disabled get their default payment-method codes (provider-specific constant) activated | N-U20-004 |
| VDR-U20-C011 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:460 | return set() | FACT | always | — | _get_default_payment_method_codes returns an empty set in the base so each add-on must supply its default methods | N-U20-004 |
| VDR-U20-C012 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:407 | any_active_provider = bool( | FACT | always | — | _toggle_post_processing_cron activates the cron only if a provider with state != disabled exists | N-U20-005 |
| VDR-U20-C013 | FUNCTION MAPPING REQUIRED | payment/data/payment_cron.xml:15 | _toggle_post_processing_cron | FACT | always | — | The cron ships inactive and is toggled at module load by a function call | N-U20-005 |
| VDR-U20-C014 | FUNCTION MAPPING REQUIRED | payment/__init__.py:9 | def setup_provider(env, code, **kwargs) | FACT | always | — | setup_provider/reset_payment_provider helpers are called from every add-on's post_init and uninstall hooks | N-U20-006 |
| VDR-U20-C015 | FUNCTION MAPPING REQUIRED | payment_custom/__init__.py:10 | setup_provider(env, 'custom' | FACT | payment_custom installed | — | Example hook call in payment_custom with custom_mode wire_transfer | N-U20-006 |
| VDR-U20-C016 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:987 | main_provider.copy({'company_id': company.id}) | FACT | always | — | _setup_provider copies the first provider for each top-level company lacking one | N-U20-006 |
| VDR-U20-C017 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:1020 | 'code': 'none', | FACT | always | — | _get_removal_values resets code to none, state disabled, unpublished and clears the four form view links | N-U20-006 |
| VDR-U20-C018 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:470 | You cannot delete the payment provider | FACT | always | — | Providers having a non-export external id cannot be deleted; message tells to disable or uninstall | N-U20-007 |
| VDR-U20-C019 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:268 | 'support_refund': 'none', | FACT | always | — | Base _compute_feature_support_fields sets express checkout, manual capture, tokenization to None and refund to none | N-U20-008 |
| VDR-U20-C020 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:759 | def _search_by_reference | FACT | always | — | Engine hook: locate transaction from provider data | N-U20-009 |
| VDR-U20-C021 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:845 | def _extract_amount_data | FACT | always | — | Engine hook: provider returns amount, currency code and optional precision; returning None skips validation | N-U20-009 |
| VDR-U20-C022 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:858 | def _apply_updates | FACT | always | — | Engine hook: provider maps data to state, provider reference and payment method; must be overridden | N-U20-009 |
| VDR-U20-C023 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:902 | def _extract_token_values | FACT | always | — | Engine hook: provider supplies data for token creation | N-U20-009 |
| VDR-U20-C024 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:576 | def _send_payment_request | FACT | always | — | Engine hooks for token charge, capture, void and refund are empty in the base (they only run if overridden) | N-U20-009 |
| VDR-U20-C025 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:746 | tx = self or self._search_by_reference(provider_code, payment_data) | FACT | always | — | _process finds the transaction (self or by provider data), validates amount, stops on new error state, applies updates and tokenizes if requested | N-U20-009 |
| VDR-U20-C026 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:816 | if not amount or not currency_code: | INFERENCE | always | — | Base _extract_amount_data returns {} (line 856), so _validate_amount at this line sets the transaction to error unless the provider overrides it; opt-out is only by returning None (line 809) | N-U20-010 |
| VDR-U20-C027 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:809 | if amount_data is None: | FACT | always | — | A provider that returns None from _extract_amount_data skips amount and currency validation | N-U20-010 |
| VDR-U20-C028 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:793 | timeout=10, | FACT | always | — | provider._send_api_request uses requests with a 10 second timeout | N-U20-011 |
| VDR-U20-C029 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:796 | Could not establish the connection | FACT | always | — | Connection and timeout errors raise ValidationError | N-U20-011 |
| VDR-U20-C030 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:813 | The payment provider rejected the request | FACT | always | — | HTTP error responses raise ValidationError carrying the parsed provider message | N-U20-011 |
| VDR-U20-C031 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:608 | capture_tx._set_error(str(e)) | FACT | always | — | Capture, void and refund wrap the send step and convert ValidationError into an error state on the child transaction | N-U20-011 |
| VDR-U20-C032 | FUNCTION MAPPING REQUIRED | payment_stripe/__manifest__.py:10 | 'depends': ['payment'] | FACT | always | — | payment_stripe depends only on payment (same pattern read for all 23 manifests by grep) | N-U20-012 |
| VDR-U20-C033 | FUNCTION MAPPING REQUIRED | payment_ecpay/__manifest__.py:9 | "depends": ["payment"] | FACT | always | — | payment_ecpay (double-quoted manifest style) depends only on payment | N-U20-012 |
| VDR-U20-C034 | FUNCTION MAPPING REQUIRED | payment/data/neutralize.sql:4 | WHERE state NOT IN ('test', 'disabled') | FACT | always | — | Neutralization disables every enabled provider and keeps test providers | N-U20-013 |
| VDR-U20-C035 | FUNCTION MAPPING REQUIRED | payment_adyen/data/neutralize.sql:4 | adyen_api_key = NULL | FACT | payment_adyen installed | — | Adyen neutralization nulls merchant account, API key and HMAC key | N-U20-013 |
| VDR-U20-C036 | FUNCTION MAPPING REQUIRED | payment_xendit/data/neutralize.sql:2 | xendit_secret_key = 'dummysecret' | FACT | payment_xendit installed | — | Xendit neutralization sets dummy secret and webhook token rather than NULL | N-U20-013 |
| VDR-U20-C037 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/data/neutralize.sql:3 | mercado_pago_access_token = NULL | OBSERVATION | source | — | Mercado Pago neutralization nulls only the access token and leaves refresh token and public key (observation from source) | N-U20-013 |
| VDR-U20-C038 | FUNCTION MAPPING REQUIRED | payment_paypal/data/neutralize.sql:5 | paypal_client_secret = NULL | OBSERVATION | source | — | PayPal neutralization does not clear the cached access token or webhook id (only email, client id, client secret) | N-U20-013 |
| VDR-U20-C039 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:312 | provider_sudo = request.env['payment.provider'].sudo().browse(provider_id) | FACT | always | — | _create_transaction browses the provider from the client-supplied id without a compatibility or state check | N-U20-014 |
| VDR-U20-C040 | FUNCTION MAPPING REQUIRED | payment_demo/controllers/portal.py:26 | is not properly configured | FACT | payment_demo installed | — | payment_demo overrides _create_transaction to reject a demo provider that is not among the compatible providers | N-U20-014 |
| VDR-U20-C041 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:687 | def _ensure_provider_is_not_disabled | FACT | always | — | Only token charge, capture, void and refund call _ensure_provider_is_not_disabled; transaction create has no such check | N-U20-014 |
| VDR-U20-C042 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_transaction.py:34 | intent = self._stripe_create_intent() | FACT | payment_stripe installed | — | Stripe: processing values create a PaymentIntent/SetupIntent server-side and return client_secret plus return_url | N-U20-016 |
| VDR-U20-C043 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_transaction.py:151 | setup_future_usage | FACT | payment_stripe installed | — | Stripe: tokenize sets setup_future_usage off_session; capture_method manual when provider.capture_manually | N-U20-016 |
| VDR-U20-C044 | FUNCTION MAPPING REQUIRED | payment_adyen/models/payment_transaction.py:37 | 'access_token': payment_utils.generate_access_token( | FACT | payment_adyen installed | — | Adyen: processing values include converted_amount and an access token over reference, amount, currency id and partner | N-U20-016 |
| VDR-U20-C045 | FUNCTION MAPPING REQUIRED | payment_adyen/controllers/main.py:83 | access_token, reference, converted_amount, currency_id, partner_id | FACT | payment_adyen installed | — | Adyen /payments verifies the token over reference, amount, currency and partner and raises ValidationError if tampered | N-U20-024 |
| VDR-U20-C046 | FUNCTION MAPPING REQUIRED | payment_aps/models/payment_transaction.py:56 | 'command': 'PURCHASE', | FACT | payment_aps installed | — | APS: redirect form with PURCHASE command, merchant reference, minor-unit amount and signature | N-U20-016 |
| VDR-U20-C047 | FUNCTION MAPPING REQUIRED | payment_asiapay/models/payment_transaction.py:71 | 'mps_mode': 'SCP', | FACT | payment_asiapay installed | — | AsiaPay: redirect form with merchant id, amount, reference, currency code taken from the single provider currency and secure hash | N-U20-016 |
| VDR-U20-C048 | FUNCTION MAPPING REQUIRED | payment_authorize/models/payment_transaction.py:33 | processing_values['reference'], processing_values['partner_id'] | FACT | payment_authorize installed | — | Authorize.Net: access token over reference and partner only; amount is not part of the token | N-U20-016 |
| VDR-U20-C049 | FUNCTION MAPPING REQUIRED | payment_authorize/controllers/main.py:29 | check_access_token(access_token, reference, partner_id) | FACT | payment_authorize installed | — | Authorize.Net payment route verifies the token over reference and partner and then loads the transaction by reference | N-U20-024 |
| VDR-U20-C050 | FUNCTION MAPPING REQUIRED | payment_buckaroo/models/payment_transaction.py:33 | 'Brq_amount': self.amount, | FACT | payment_buckaroo installed | — | Buckaroo: redirect form fields Brq_* signed with SHA-1 digest | N-U20-016 |
| VDR-U20-C051 | FUNCTION MAPPING REQUIRED | payment_dpo/models/payment_transaction.py:52 | <CompanyToken> | FACT | payment_dpo installed | — | DPO: createToken XML request built by f-string concatenation including customer fields | N-U20-016 |
| VDR-U20-C052 | FUNCTION MAPPING REQUIRED | payment_dpo/models/payment_transaction.py:61 | <customerFirstName> | INFERENCE | payment_dpo installed | RT | Customer first/last name, email, city and zip are interpolated into the XML without escaping (lines 60-65); effect on the gateway parser requires runtime test | N-U20-025 |
| VDR-U20-C053 | FUNCTION MAPPING REQUIRED | payment_ecpay/models/payment_transaction.py:73 | "TotalAmount": int(self.amount), | FACT | payment_ecpay installed | — | ECPay: amount sent as truncated integer; CheckMacValue signature; payment methods not chosen are listed in IgnorePayment | N-U20-016 |
| VDR-U20-C054 | FUNCTION MAPPING REQUIRED | payment_flutterwave/models/payment_transaction.py:100 | 'payments', json=payload | FACT | payment_flutterwave installed | — | Flutterwave: payment link created through POST payments; link returned as api_url | N-U20-016 |
| VDR-U20-C055 | FUNCTION MAPPING REQUIRED | payment_iyzico/models/payment_transaction.py:38 | checkoutform/initialize/auth/ecom | FACT | payment_iyzico installed | — | Iyzico: hosted checkout form initialised via API; paymentPageUrl returned | N-U20-016 |
| VDR-U20-C056 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/models/payment_transaction.py:39 | '/checkout/preferences' | FACT | payment_mercado_pago installed | — | Mercado Pago: checkout preference created via API; init_point (live) or sandbox_init_point used | N-U20-016 |
| VDR-U20-C057 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/controllers/payment.py:41 | 'transaction_amount': float(transaction_amount), | FACT | payment_mercado_pago installed | RT | Direct payment route (auth public) overwrites the server payload amount with the browser-supplied transaction_amount and has no access-token check | N-U20-026 |
| VDR-U20-C058 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/static/src/interactions/payment_form.js:148 | 'transaction_amount': processingValues.amount, | FACT | payment_mercado_pago installed | RT | Front-end sends the amount from processing values; nothing server-side forces equality | N-U20-026 |
| VDR-U20-C059 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/models/payment_transaction.py:208 | get('additional_info', {}).get('items', [{}])[0].get('unit_price') | INFERENCE | payment_mercado_pago installed | RT | For online_redirect/online_direct _extract_amount_data reads the echoed item unit_price (server-set in line 107) not transaction_amount; whether the gateway echoes the server item price while charging a lower transaction_amount needs runtime test | N-U20-026 |
| VDR-U20-C060 | FUNCTION MAPPING REQUIRED | payment_mollie/models/payment_transaction.py:35 | payment_data = self._send_api_request('POST', '/payments', json=payload) | FACT | payment_mollie installed | — | Mollie: payment created via API; provider_reference stored immediately; checkout href returned | N-U20-016 |
| VDR-U20-C061 | FUNCTION MAPPING REQUIRED | payment_nuvei/models/payment_transaction.py:81 | 'payment_method_mode': 'filter', | FACT | payment_nuvei installed | — | Nuvei: purchase URL parameters with checksum; amount rounded down (0 decimals for integer-only methods) | N-U20-016 |
| VDR-U20-C062 | FUNCTION MAPPING REQUIRED | payment_paymob/models/payment_transaction.py:58 | 'POST', '/v1/intention/', json=payload | FACT | payment_paymob installed | — | Paymob: payment intention created with secret key; provider_reference stored as intention_order_id | N-U20-016 |
| VDR-U20-C063 | FUNCTION MAPPING REQUIRED | payment_paypal/models/payment_transaction.py:42 | 'POST', '/v2/checkout/orders' | FACT | payment_paypal installed | — | PayPal: order created server-side (intent CAPTURE); order_id returned to the browser | N-U20-016 |
| VDR-U20-C064 | FUNCTION MAPPING REQUIRED | payment_payu/models/payment_transaction.py:48 | payload["hash"] = self.provider_id._payu_generate_signature(payload) | FACT | payment_payu installed | — | PayU: form parameters signed with SHA-512 including merchant salt | N-U20-016 |
| VDR-U20-C065 | FUNCTION MAPPING REQUIRED | payment_razorpay/models/payment_transaction.py:44 | order_id = self._razorpay_create_order(customer_id).get('id') | FACT | payment_razorpay installed | — | Razorpay: customer and order created server-side; order id and public key returned to checkout script | N-U20-016 |
| VDR-U20-C066 | FUNCTION MAPPING REQUIRED | payment_redsys/models/payment_transaction.py:107 | 'DS_MERCHANT_TRANSACTIONTYPE': '0', | FACT | payment_redsys installed | — | Redsys: merchant parameters base64-encoded and signed (HMAC_SHA256_V1); transaction type 0 | N-U20-016 |
| VDR-U20-C067 | FUNCTION MAPPING REQUIRED | payment_toss_payments/models/payment_transaction.py:57 | 'success_url': urljoin(base_url, const.PAYMENT_SUCCESS_RETURN_ROUTE) | FACT | payment_toss_payments installed | — | Toss Payments: processing values give the widget success and failure URLs; failure URL carries an access token over the reference | N-U20-016 |
| VDR-U20-C068 | FUNCTION MAPPING REQUIRED | payment_worldline/models/payment_transaction.py:160 | 'hostedcheckouts', json=payload | FACT | payment_worldline installed | — | Worldline: hosted checkout session created through API; redirectUrl returned | N-U20-016 |
| VDR-U20-C069 | FUNCTION MAPPING REQUIRED | payment_xendit/models/payment_transaction.py:56 | 'v2/invoices' | FACT | payment_xendit installed | — | Xendit: non-card payments create an invoice via API and redirect; card payments use a browser token plus the controller charge | N-U20-016 |
| VDR-U20-C070 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:367 | tx_sudo._charge_with_token() | FACT | always | — | Token flow: _create_transaction calls _charge_with_token immediately unless delay_token_charge is set | N-U20-020 |
| VDR-U20-C071 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:574 | self._set_error(str(e)) | FACT | always | — | _charge_with_token converts a ValidationError from the send step into the error state | N-U20-020 |
| VDR-U20-C072 | FUNCTION MAPPING REQUIRED | payment_aps/models/payment_transaction.py:36 | prefix = payment_utils.singularize_reference_prefix() | FACT | payment_aps installed | — | APS reference regenerated from a timestamped 'tx' prefix to keep only alphanumerics, - and _ | N-U20-021 |
| VDR-U20-C073 | FUNCTION MAPPING REQUIRED | payment_asiapay/models/payment_transaction.py:46 | max_length=35 | FACT | payment_asiapay installed | — | AsiaPay singularized prefix limited to 35 characters | N-U20-021 |
| VDR-U20-C074 | FUNCTION MAPPING REQUIRED | payment_ecpay/models/payment_transaction.py:39 | max_length=20 | FACT | payment_ecpay installed | — | ECPay prefix limited to 20 characters with empty separator | N-U20-021 |
| VDR-U20-C075 | FUNCTION MAPPING REQUIRED | payment_redsys/models/payment_transaction.py:52 | separator='S' | FACT | payment_redsys installed | — | Redsys prefix is 10-digit timestamp and separator S; provider_reference set to reference on create | N-U20-021 |
| VDR-U20-C076 | FUNCTION MAPPING REQUIRED | payment_worldline/models/payment_transaction.py:38 | if len(reference) <= 30: | FACT | payment_worldline installed | — | Worldline references longer than 30 characters are regenerated with a WL prefix | N-U20-021 |
| VDR-U20-C077 | FUNCTION MAPPING REQUIRED | payment/utils.py:265 | database_uuid = tx.env['ir.config_parameter'] | FACT | always | — | Idempotency key = sha1 of database.uuid, reference and scope | N-U20-022 |
| VDR-U20-C078 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_transaction.py:79 | idempotency_key=payment_utils.generate_idempotency_key( | FACT | payment_stripe installed | — | Stripe payment_intents creation sends an idempotency key | N-U20-022 |
| VDR-U20-C079 | FUNCTION MAPPING REQUIRED | payment_adyen/controllers/main.py:153 | idempotency_key = payment_utils.generate_idempotency_key( | FACT | payment_adyen installed | — | Adyen /payments and /payments/details send idempotency keys | N-U20-022 |
| VDR-U20-C080 | FUNCTION MAPPING REQUIRED | payment_paypal/controllers/main.py:36 | idempotency_key = payment_utils.generate_idempotency_key( | FACT | payment_paypal installed | — | PayPal capture sends PayPal-Request-Id derived from the idempotency key | N-U20-022 |
| VDR-U20-C081 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:195 | 'partner_email': partner_emails[0] if partner_emails else None, | FACT | always | — | create copies partner name, lang, first normalised email, address, zip, city, state, country, phone | N-U20-023 |
| VDR-U20-C082 | FUNCTION MAPPING REQUIRED | payment_adyen/controllers/main.py:166 | def adyen_payment_details(self, provider_id, reference, payment_details) | FACT | payment_adyen installed | RT | /payment/adyen/payments/details (auth public) has no access token; the caller picks reference and payment_details and the response is processed against the reference | N-U20-027 |
| VDR-U20-C083 | FUNCTION MAPPING REQUIRED | payment_adyen/controllers/main.py:223 | tx_sudo.operation = 'online_redirect' | FACT | payment_adyen installed | RT | /payment/adyen/return rewrites the operation of the referenced transaction before processing; no signature on this route | N-U20-027 |
| VDR-U20-C084 | FUNCTION MAPPING REQUIRED | payment_xendit/controllers/main.py:35 | if not payment_utils.check_access_token(access_token, reference): | FACT | payment_xendit installed | — | Xendit card charge route verifies a token over the reference only; amount comes from the stored transaction | N-U20-024 |
| VDR-U20-C085 | FUNCTION MAPPING REQUIRED | payment/data/payment_provider_data.xml:4 | payment_provider_adyen | OBSERVATION | restored DB | CONTRA | Restored DB ir_module_module: payment_adyen, aps, asiapay, authorize, buckaroo, custom, demo, dpo, ecpay, flutterwave, iyzico, mercado_pago, mollie, nuvei, paymob, paypal, payu, razorpay, redsys, stripe, toss_payments, worldline, xendit are all state installed (CONTRA the worklist premise that only payment_custom and payment_demo are installed; U12 CAP-U12-08 named only those two as examples); 25 payment_provider rows: 24 defined by the payment module data plus 1 from delivery | N-U20-029 |
| VDR-U20-C086 | FUNCTION MAPPING REQUIRED | payment/data/payment_provider_data.xml:434 | module_payment_sepa_direct_debit | OBSERVATION | restored DB | — | Restored DB: provider 19 'SEPA Direct Debit' code none, disabled, linked to module payment_sepa_direct_debit with module state uninstallable (module absent from the community source tree) | N-U20-029 |
| VDR-U20-C087 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1038 | Skipped the update of transaction | FACT | always | — | _update_state logs and skips a transaction already in the target state | N-U20-035 |
| VDR-U20-C088 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1043 | Refused to update transaction | FACT | always | — | _update_state refuses and logs transitions from states not in the allowed list | N-U20-035 |
| VDR-U20-C089 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:958 | allowed_states = ('draft', 'pending', 'authorized', 'error') | FACT | always | — | _set_done is allowed from draft, pending, authorized and error | N-U20-035 |
| VDR-U20-C090 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:976 | allowed_states = ('draft', 'pending', 'authorized') | FACT | always | — | _set_canceled and _set_error are allowed from draft, pending, authorized only | N-U20-035 |
| VDR-U20-C091 | FUNCTION MAPPING REQUIRED | payment_stripe/controllers/main.py:27 | WEBHOOK_AGE_TOLERANCE = 10*60 | FACT | payment_stripe installed | — | Stripe webhook timestamp tolerance is 10 minutes (the only age check among providers read) | N-U20-035 |
| VDR-U20-C092 | FUNCTION MAPPING REQUIRED | payment_stripe/controllers/main.py:95 | self._verify_signature(tx_sudo) | FACT | payment_stripe installed | — | Stripe webhook verifies the signature after locating the transaction and before processing | N-U20-034 |
| VDR-U20-C093 | FUNCTION MAPPING REQUIRED | payment_stripe/controllers/main.py:204 | undefined webhook secret | FACT | payment_stripe installed | — | Stripe webhook without a configured signing secret is refused (Forbidden) | N-U20-034 |
| VDR-U20-C094 | FUNCTION MAPPING REQUIRED | payment_stripe/controllers/main.py:233 | hmac.compare_digest(received_signature, expected_signature) | FACT | payment_stripe installed | — | Stripe signature = HMAC-SHA256(secret, timestamp.payload) compared in constant time | N-U20-034 |
| VDR-U20-C095 | FUNCTION MAPPING REQUIRED | payment_stripe/controllers/main.py:55 | if tx_sudo.reference != response_content["description"]: | FACT | payment_stripe installed | RT | Stripe return route fetches the intent from the API and requires description to equal the transaction reference (Forbidden otherwise) | N-U20-036 |
| VDR-U20-C096 | FUNCTION MAPPING REQUIRED | payment_stripe/controllers/main.py:209 | signature_data = {k: v | INFERENCE | payment_stripe installed | RT | Signature header parsed into a dict: if Stripe sends several v1 entries only the last is kept, and a value containing '=' would break the split; header absence raises KeyError (line 208) | N-U20-046 |
| VDR-U20-C097 | FUNCTION MAPPING REQUIRED | payment_stripe/controllers/main.py:154 | skipping to acknowledge | FACT | payment_stripe installed | — | ValidationError during webhook processing is logged and acknowledged | N-U20-037 |
| VDR-U20-C098 | FUNCTION MAPPING REQUIRED | payment_adyen/controllers/main.py:265 | self._verify_signature(payment_data, tx_sudo) | FACT | payment_adyen installed | — | Adyen webhook verifies HMAC after the transaction lookup, inside if tx_sudo | N-U20-034 |
| VDR-U20-C099 | FUNCTION MAPPING REQUIRED | payment_adyen/controllers/main.py:303 | hmac.compare_digest(received_signature, expected_signature) | FACT | payment_adyen installed | — | Adyen HMAC (SHA-256, base64, key hex-decoded) over pspReference, originalReference, merchantAccountCode, merchantReference, amount, currency, eventCode, success | N-U20-034 |
| VDR-U20-C100 | FUNCTION MAPPING REQUIRED | payment_adyen/models/payment_transaction.py:262 | tx = self._adyen_create_child_tx(source_tx, payment_data) | INFERENCE | payment_adyen installed | RT | _search_by_reference (called before verification) may create a child transaction for capture/cancellation events; Forbidden after verification failure rolls the request back | N-U20-043 |
| VDR-U20-C101 | FUNCTION MAPPING REQUIRED | payment_adyen/models/payment_transaction.py:246 | arbitrary_decimal_number=const.CURRENCY_DECIMALS.get(self.currency_id.name), | INFERENCE | payment_adyen installed | RT | In _search_by_reference self is an empty recordset (model method) so currency_id.name is False and Adyen's special decimals (CLP, CVE, IDR, ISK) are not applied to child amounts; effect needs runtime test | N-U20-046 |
| VDR-U20-C102 | FUNCTION MAPPING REQUIRED | payment_aps/controllers/main.py:41 | self._verify_signature(data, tx_sudo) | FACT | payment_aps installed | — | APS return and webhook both verify the signature before processing | N-U20-034 |
| VDR-U20-C103 | FUNCTION MAPPING REQUIRED | payment_aps/controllers/main.py:80 | hmac.compare_digest(received_signature, expected_signature) | FACT | payment_aps installed | — | APS compares SHA-256 digests in constant time | N-U20-034 |
| VDR-U20-C104 | FUNCTION MAPPING REQUIRED | payment_aps/models/payment_provider.py:75 | hashlib.sha256(signing_string.encode()).hexdigest() | FACT | payment_aps installed | — | APS signature is plain SHA-256 over phrase + sorted key=value pairs + phrase (not an HMAC) | N-U20-044 |
| VDR-U20-C105 | FUNCTION MAPPING REQUIRED | payment_asiapay/controllers/main.py:27 | Don't process the payment data | FACT | payment_asiapay installed | — | AsiaPay return route does not process data (only redirects to status); processing is webhook-only | N-U20-034 |
| VDR-U20-C106 | FUNCTION MAPPING REQUIRED | payment_asiapay/controllers/main.py:64 | hmac.compare_digest(received_signature, expected_signature) | FACT | payment_asiapay installed | — | AsiaPay webhook verifies secureHash in constant time | N-U20-034 |
| VDR-U20-C107 | FUNCTION MAPPING REQUIRED | payment_asiapay/models/payment_provider.py:43 | default='sha1', | FACT | payment_asiapay installed | — | AsiaPay secure-hash function defaults to SHA1 (SHA256 and SHA512 selectable) | N-U20-044 |
| VDR-U20-C108 | FUNCTION MAPPING REQUIRED | payment_asiapay/models/payment_provider.py:43 | default='sha1', | OBSERVATION | restored DB | — | All 25 provider rows in the restored DB carry asiapay_secure_hash_function = sha1 (column default); asiapay_brand = paydollar on all 25 rows | N-U20-044 |
| VDR-U20-C109 | FUNCTION MAPPING REQUIRED | payment_authorize/models/payment_provider.py:35 | authorize_signature_key = fields.Char( | INFERENCE | payment_authorize installed | — | authorize_signature_key is required to enable the provider but a grep of the module finds no use of it besides view, neutralize and tests; no webhook route exists in the module | N-U20-046 |
| VDR-U20-C110 | FUNCTION MAPPING REQUIRED | payment_authorize/controllers/main.py:41 | FOR NO KEY UPDATE | FACT | payment_authorize installed | — | Authorize payment route locks the transaction row before using the single-use opaque token | N-U20-036 |
| VDR-U20-C111 | FUNCTION MAPPING REQUIRED | payment_buckaroo/controllers/main.py:103 | hmac.compare_digest(received_signature, expected_signature) | FACT | payment_buckaroo installed | — | Buckaroo return and webhook verify brq_signature in constant time | N-U20-034 |
| VDR-U20-C112 | FUNCTION MAPPING REQUIRED | payment_buckaroo/models/payment_provider.py:96 | return sha1(sign_string.encode('utf-8')).hexdigest() | FACT | payment_buckaroo installed | — | Buckaroo digital signature is SHA-1 over sorted brq_/add_/cust_ pairs plus the secret key | N-U20-044 |
| VDR-U20-C113 | FUNCTION MAPPING REQUIRED | payment_custom/controllers/main.py:16 | auth='public', methods=['POST'], csrf=False | FACT | payment_custom installed | — | Custom payment processing route is public, CSRF-exempt and takes the reference from the POST body | N-U20-045 |
| VDR-U20-C114 | FUNCTION MAPPING REQUIRED | payment_custom/controllers/main.py:19 | _process('custom', post) | FACT | payment_custom installed | — | The route passes the posted data to _process; the provider's _apply_updates sets pending without checks | N-U20-045 |
| VDR-U20-C115 | FUNCTION MAPPING REQUIRED | payment_demo/controllers/main.py:17 | _process('demo', data) | FACT | payment_demo installed | — | Demo simulation route (auth public, jsonrpc) passes caller data, including simulated_state, to _process | N-U20-045 |
| VDR-U20-C116 | FUNCTION MAPPING REQUIRED | payment_dpo/controllers/main.py:47 | <Request>verifyToken</Request> | FACT | payment_dpo installed | — | DPO return route verifies the payment by calling verifyToken with the TransID taken from the URL | N-U20-036 |
| VDR-U20-C117 | FUNCTION MAPPING REQUIRED | payment_dpo/controllers/main.py:55 | data.update(verified_data) | FACT | payment_dpo installed | RT | Gateway answer is merged into the URL data; no comparison of the answer's CompanyRef with the transaction reference follows | N-U20-040 |
| VDR-U20-C118 | FUNCTION MAPPING REQUIRED | payment_dpo/controllers/main.py:56 | tx_sudo._process('dpo', data) | FACT | payment_dpo installed | RT | _process is called on the transaction located from the URL reference (self non-empty), so it does not re-search by the verified reference | N-U20-040 |
| VDR-U20-C119 | FUNCTION MAPPING REQUIRED | payment_dpo/controllers/main.py:48 | data.get("TransID") | FACT | payment_dpo installed | RT | TransID from the URL is placed unescaped into the XML request body | N-U20-040 |
| VDR-U20-C120 | FUNCTION MAPPING REQUIRED | payment_ecpay/controllers/main.py:98 | if not consteq(received_signature, expected_signature): | FACT | payment_ecpay installed | — | ECPay CheckMacValue compared with consteq | N-U20-034 |
| VDR-U20-C121 | FUNCTION MAPPING REQUIRED | payment_ecpay/controllers/main.py:69 | data.get("SimulatePaid") == "0" | FACT | payment_ecpay installed | — | ECPay webhook processes only notifications with SimulatePaid equal to 0; simulated payments are ignored | N-U20-034 |
| VDR-U20-C122 | FUNCTION MAPPING REQUIRED | payment_flutterwave/controllers/main.py:85 | expected_signature = tx_sudo.provider_id.flutterwave_webhook_secret | FACT | payment_flutterwave installed | — | Flutterwave verif-hash header must equal the configured secret itself (static token) | N-U20-038 |
| VDR-U20-C123 | FUNCTION MAPPING REQUIRED | payment_flutterwave/controllers/main.py:105 | 'GET', 'transactions/verify_by_reference' | FACT | payment_flutterwave installed | — | Flutterwave return route verifies by reference through the API before processing | N-U20-036 |
| VDR-U20-C124 | FUNCTION MAPPING REQUIRED | payment_iyzico/controllers/main.py:87 | if verified_payment_data.get('basketId') != tx_sudo.reference: | FACT | payment_iyzico installed | — | Iyzico return and webhook (no signature) verify the token through the API and require basketId to equal the transaction reference | N-U20-036 |
| VDR-U20-C125 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/controllers/payment.py:118 | if tx_sudo.reference != verified_data["external_reference"]: | FACT | payment_mercado_pago installed | — | Mercado Pago return and webhook (no signature) verify the payment via API and compare external_reference with the transaction reference | N-U20-036 |
| VDR-U20-C126 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/controllers/payment.py:113 | f'/v1/payments/{data.get("payment_id")}' | INFERENCE | payment_mercado_pago installed | RT | payment_id from the query/body is concatenated into the API path without validation; path manipulation could target other endpoints of the same API with the shop's token | N-U20-046 |
| VDR-U20-C127 | FUNCTION MAPPING REQUIRED | payment_mollie/controllers/main.py:67 | f'/payments/{tx_sudo.provider_reference}' | FACT | payment_mollie installed | — | Mollie return and webhook (no signature) fetch the payment by the provider_reference stored at creation | N-U20-036 |
| VDR-U20-C128 | FUNCTION MAPPING REQUIRED | payment_nuvei/controllers/main.py:91 | if not consteq(received_signature, expected_signature): | FACT | payment_nuvei installed | — | Nuvei advanceResponseChecksum compared with consteq | N-U20-034 |
| VDR-U20-C129 | FUNCTION MAPPING REQUIRED | payment_nuvei/models/payment_provider.py:81 | signing_string = f'{key}{sign_data}' | FACT | payment_nuvei installed | — | Nuvei checksum = SHA-256(secret + concatenation of six fields with no delimiter) | N-U20-044 |
| VDR-U20-C130 | FUNCTION MAPPING REQUIRED | payment_nuvei/controllers/main.py:78 | if not payment_utils.check_access_token(error_access_token, ref): | FACT | payment_nuvei installed | — | Nuvei cancel/error returns carry no checksum and are authenticated by an access token over the reference alone | N-U20-044 |
| VDR-U20-C131 | FUNCTION MAPPING REQUIRED | payment_nuvei/models/payment_transaction.py:143 | self._set_canceled(state_message=_("The customer left the payment page.")) | FACT | payment_nuvei installed | — | An authenticated error return processes empty data and cancels the transaction | N-U20-046 |
| VDR-U20-C132 | FUNCTION MAPPING REQUIRED | payment_paymob/controllers/main.py:33 | if data["order"] != tx_sudo.provider_reference: | FACT | payment_paymob installed | — | Paymob return requires the gateway order id to equal the stored provider_reference before verifying the HMAC | N-U20-036 |
| VDR-U20-C133 | FUNCTION MAPPING REQUIRED | payment_paymob/controllers/main.py:112 | if not hmac.compare_digest(received_signature, expected_signature): | FACT | payment_paymob installed | — | Paymob HMAC (SHA-512 hex over 20 sorted fields) compared in constant time | N-U20-034 |
| VDR-U20-C134 | FUNCTION MAPPING REQUIRED | payment_paymob/controllers/main.py:84 | 'data.message': payment_data.get('data').get('message'), | INFERENCE | payment_paymob installed | RT | Malformed webhook without data object raises AttributeError (500) before verification | N-U20-046 |
| VDR-U20-C135 | FUNCTION MAPPING REQUIRED | payment_paypal/controllers/main.py:128 | 'POST', '/v1/notifications/verify-webhook-signature' | FACT | payment_paypal installed | — | PayPal notifications are verified by calling PayPal's verify-webhook-signature with the stored webhook id | N-U20-034 |
| VDR-U20-C136 | FUNCTION MAPPING REQUIRED | payment_paypal/controllers/main.py:69 | tx_sudo._set_error(_("Unable to verify the payment data")) | FACT | payment_paypal installed | RT | When the verification call raises ValidationError the referenced transaction is set to error | N-U20-042 |
| VDR-U20-C137 | FUNCTION MAPPING REQUIRED | payment_paypal/controllers/main.py:42 | normalized_response | FACT | payment_paypal installed | — | complete_order captures the order and then re-locates the transaction from the reference in the PayPal response (not from the caller's reference) | N-U20-036 |
| VDR-U20-C138 | FUNCTION MAPPING REQUIRED | payment_payu/controllers/main.py:80 | if not consteq(received_signature, expected_signature): | FACT | payment_payu installed | — | PayU hash compared with consteq on return and webhook | N-U20-034 |
| VDR-U20-C139 | FUNCTION MAPPING REQUIRED | payment_payu/models/payment_provider.py:25 | @api.constrains("state") | INFERENCE | payment_payu installed | RT | PayU credential presence is validated only when state changes; clearing the salt afterwards is not caught and the salt would enter the hash as the text None or False | N-U20-046 |
| VDR-U20-C140 | FUNCTION MAPPING REQUIRED | payment_razorpay/controllers/main.py:110 | not hmac.compare_digest(received_signature, expected_signature) | FACT | payment_razorpay installed | — | Razorpay: return verified with HMAC(key_secret, order_id and payment_id joined by a vertical bar); webhook with HMAC(webhook_secret, raw body); None expected signature (no webhook secret) is refused | N-U20-034 |
| VDR-U20-C141 | FUNCTION MAPPING REQUIRED | payment_razorpay/models/payment_provider.py:229 | data["razorpay_order_id"] | FACT | payment_razorpay installed | RT | Redirect signature covers only order and payment ids (no amount, no reference) | N-U20-041 |
| VDR-U20-C142 | FUNCTION MAPPING REQUIRED | payment_razorpay/models/payment_transaction.py:352 | 'amount' not in payment_data | FACT | payment_razorpay installed | RT | Redirect return data carry no amount so _extract_amount_data returns None and amount validation is skipped | N-U20-041 |
| VDR-U20-C143 | FUNCTION MAPPING REQUIRED | payment_razorpay/models/payment_transaction.py:381 | if self.reference != reference: | FACT | payment_razorpay installed | RT | After fetching the payment by id, _apply_updates compares its description/notes reference with the transaction reference | N-U20-041 |
| VDR-U20-C144 | FUNCTION MAPPING REQUIRED | payment_razorpay/static/src/interactions/payment_form.js:66 | 'description': processingValues['reference'], | FACT | payment_razorpay installed | RT | The description compared above is set by the browser script | N-U20-041 |
| VDR-U20-C145 | FUNCTION MAPPING REQUIRED | payment_redsys/controllers/main.py:75 | if not hmac.compare_digest(received_signature, expected_signature): | FACT | payment_redsys installed | — | Redsys signature verified with a per-order key derived by 3DES from the secret and the transaction reference | N-U20-034 |
| VDR-U20-C146 | FUNCTION MAPPING REQUIRED | payment_toss_payments/controllers/main.py:108 | if payment_data.get('status') in const.VERIFICATION_EXEMPT_STATUSES: | FACT | payment_toss_payments installed | RT | Webhook signature verification is skipped for statuses EXPIRED and ABORTED | N-U20-039 |
| VDR-U20-C147 | FUNCTION MAPPING REQUIRED | payment_toss_payments/const.py:30 | VERIFICATION_EXEMPT_STATUSES = {'EXPIRED', 'ABORTED'} | FACT | payment_toss_payments installed | RT | Exempt statuses constant | N-U20-039 |
| VDR-U20-C148 | FUNCTION MAPPING REQUIRED | payment_toss_payments/models/payment_transaction.py:88 | self.toss_payments_payment_secret = payment_data.get('secret') | FACT | payment_toss_payments installed | RT | _apply_updates overwrites the stored per-payment secret from the message for any status | N-U20-039 |
| VDR-U20-C149 | FUNCTION MAPPING REQUIRED | payment_toss_payments/models/payment_transaction.py:101 | self._set_error(self.env._("Received data with invalid payment status | FACT | payment_toss_payments installed | RT | Statuses other than DONE, EXPIRED or partial cancellation fall through to error | N-U20-039 |
| VDR-U20-C150 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:958 | allowed_states = ('draft', 'pending', 'authorized', 'error') | INFERENCE | payment_toss_payments installed | RT | _set_done is allowed from error (line 958), so ABORTED(secret=X) then DONE(secret=X, amount=tx amount) would pass verification (controller line 117) and amount check; exploit chain unverified at runtime | N-U20-039 |
| VDR-U20-C151 | FUNCTION MAPPING REQUIRED | payment_toss_payments/controllers/main.py:117 | if not hmac.compare_digest(received_signature, expected_signature): | FACT | payment_toss_payments installed | — | Toss compares the message secret with the stored secret in constant time; empty stored secret never matches a non-empty one | N-U20-034 |
| VDR-U20-C152 | FUNCTION MAPPING REQUIRED | payment_toss_payments/controllers/main.py:34 | tx_sudo._validate_amount({'totalAmount': data.get('amount')}) | FACT | payment_toss_payments installed | — | Success return validates the browser-supplied amount against the transaction before calling /v1/payments/confirm | N-U20-036 |
| VDR-U20-C153 | FUNCTION MAPPING REQUIRED | payment_worldline/controllers/main.py:42 | f'hostedcheckouts/{data["hostedCheckoutId"]}' | FACT | payment_worldline installed | — | Worldline return route fetches the hosted checkout from the API (provider id and checkout id from URL) and processes the answer, locating the transaction by merchantReference in the answer | N-U20-036 |
| VDR-U20-C154 | FUNCTION MAPPING REQUIRED | payment_worldline/controllers/main.py:96 | if not hmac.compare_digest(received_signature.encode(), expected_signature): | FACT | payment_worldline installed | — | Worldline webhook: base64 HMAC-SHA256 of the raw body with the webhook secret | N-U20-034 |
| VDR-U20-C155 | FUNCTION MAPPING REQUIRED | payment_xendit/controllers/main.py:82 | consteq(tx_sudo.provider_id.xendit_webhook_token, received_token) | FACT | payment_xendit installed | — | Xendit webhook authenticated by static x-callback-token compared in constant time | N-U20-038 |
| VDR-U20-C156 | FUNCTION MAPPING REQUIRED | payment_xendit/controllers/main.py:65 | payment_utils.check_access_token(access_token, tx_ref, tx_sudo.amount) | FACT | payment_xendit installed | — | Xendit return route sets a draft transaction to pending only if the token over reference and amount is valid | N-U20-036 |
| VDR-U20-C157 | FUNCTION MAPPING REQUIRED | payment_xendit/controllers/main.py:83 | invalid callback token | FACT | payment_xendit installed | — | Invalid callback token is logged verbatim (attacker-supplied value, not the secret) | N-U20-046 |
| VDR-U20-C158 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:830 | rounding_method='DOWN' | FACT | always | — | Shop amount is float_round DOWN to the precision (provider precision or currency minor units) | N-U20-049 |
| VDR-U20-C159 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:832 | if self.currency_id.compare_amounts(amount, tx_amount) != 0: | FACT | always | — | Amount mismatch sets error: 'The amount from the payment data doesn't match' | N-U20-049 |
| VDR-U20-C160 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:839 | if currency_code != self.currency_id.name: | FACT | always | — | Currency code mismatch sets error | N-U20-049 |
| VDR-U20-C161 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:717 | amount = -amount | FACT | always | — | For refund operations the provider's positive amount is negated before comparison | N-U20-049 |
| VDR-U20-C162 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:751 | tx.state != previous_state | FACT | always | — | _process returns without applying updates if validation put the transaction in error | N-U20-049 |
| VDR-U20-C163 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:806 | Skip validation for $0-auth transactions. | FACT | always | — | Validation operations skip the amount check | N-U20-050 |
| VDR-U20-C164 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_transaction.py:51 | validation for custom flows | FACT | payment_custom installed | — | Custom (wire transfer, COD) returns None from _extract_amount_data | N-U20-050 |
| VDR-U20-C165 | FUNCTION MAPPING REQUIRED | payment_demo/models/payment_transaction.py:100 | def _extract_amount_data | FACT | payment_demo installed | — | Demo returns None from _extract_amount_data | N-U20-050 |
| VDR-U20-C166 | FUNCTION MAPPING REQUIRED | payment_adyen/models/payment_transaction.py:324 | return None  # Skip the validation | FACT | payment_adyen installed | — | Adyen skips validation for redirect or threeDS2 actions and refused result codes | N-U20-050 |
| VDR-U20-C167 | FUNCTION MAPPING REQUIRED | payment_authorize/models/payment_transaction.py:164 | return None  # Skip the validation | FACT | payment_authorize installed | — | Authorize.Net skips validation when get_transaction_details returns an error code | N-U20-052 |
| VDR-U20-C168 | FUNCTION MAPPING REQUIRED | payment_nuvei/models/payment_transaction.py:123 | if not payment_data: | FACT | payment_nuvei installed | — | Nuvei returns None (no validation) for the empty cancel message | N-U20-050 |
| VDR-U20-C169 | FUNCTION MAPPING REQUIRED | payment_asiapay/models/payment_transaction.py:102 | 'currency_code': currency.name, | FACT | payment_asiapay installed | — | AsiaPay currency to validate is the provider's single configured currency, not the message Cur | N-U20-051 |
| VDR-U20-C170 | FUNCTION MAPPING REQUIRED | payment_authorize/models/payment_transaction.py:171 | 'currency_code': currency.name, | FACT | payment_authorize installed | — | Authorize.Net currency to validate is the provider's configured currency | N-U20-051 |
| VDR-U20-C171 | FUNCTION MAPPING REQUIRED | payment_ecpay/models/payment_transaction.py:109 | return {"amount": amount, "currency_code": self.currency_id.name} | FACT | payment_ecpay installed | — | ECPay uses the transaction's own currency as the message currency | N-U20-051 |
| VDR-U20-C172 | FUNCTION MAPPING REQUIRED | payment_payu/models/payment_transaction.py:65 | effectively disables the currency validation | FACT | payment_payu installed | — | PayU comment states that the currency validation is effectively disabled (callback has no currency) | N-U20-051 |
| VDR-U20-C173 | FUNCTION MAPPING REQUIRED | payment_toss_payments/models/payment_transaction.py:76 | 'currency_code': const.SUPPORTED_CURRENCY, | FACT | payment_toss_payments installed | — | Toss uses constant KRW as the message currency | N-U20-051 |
| VDR-U20-C174 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_transaction.py:323 | 'precision_digits': const.CURRENCY_DECIMALS.get(self.currency_id.name), | FACT | payment_stripe installed | — | Stripe supplies precision_digits from its special-decimals table (ISK, UGX, MGA) | N-U20-053 |
| VDR-U20-C175 | FUNCTION MAPPING REQUIRED | payment_adyen/models/payment_transaction.py:336 | 'precision_digits': const.CURRENCY_DECIMALS.get(self.currency_id.name), | FACT | payment_adyen installed | — | Adyen supplies precision_digits (CLP, CVE, IDR, ISK) | N-U20-053 |
| VDR-U20-C176 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/models/payment_transaction.py:215 | 'precision_digits': const.CURRENCY_DECIMALS.get(currency_code), | FACT | payment_mercado_pago installed | — | Mercado Pago supplies precision_digits from the message currency | N-U20-053 |
| VDR-U20-C177 | FUNCTION MAPPING REQUIRED | payment_nuvei/models/payment_transaction.py:134 | 'precision_digits': rounding, | FACT | payment_nuvei installed | — | Nuvei precision is 0 for integer-only methods (webpay) else currency decimals | N-U20-053 |
| VDR-U20-C178 | FUNCTION MAPPING REQUIRED | payment_xendit/const.py:21 | 'THB': 0, | FACT | payment_xendit installed | — | Xendit CURRENCY_DECIMALS declares THB (and IDR, MYR, PHP, SGD, USD, VND) with 0 decimals | N-U20-054 |
| VDR-U20-C179 | FUNCTION MAPPING REQUIRED | payment_xendit/models/payment_transaction.py:158 | return float_round(self.amount, decimal_places, rounding_method='DOWN') | FACT | payment_xendit installed | — | _get_rounded_amount floors the amount to the table decimals; used for invoice and charge payloads | N-U20-054 |
| VDR-U20-C180 | FUNCTION MAPPING REQUIRED | payment_xendit/models/payment_transaction.py:177 | 'precision_digits': const.CURRENCY_DECIMALS.get(currency_code), | INFERENCE | payment_xendit installed | RT | Message check uses the same zero-decimal precision (lines 177 and engine lines 829-832): a transaction of 100.75 THB is sent as 100 and the check compares 100 with 100, so the shortfall is not flagged; THB in the engine table has 2 decimals (payment/const.py line 483) | N-U20-054 |
| VDR-U20-C181 | FUNCTION MAPPING REQUIRED | payment/const.py:483 | 'THB': 2, | FACT | always | — | Engine minor-unit table gives THB 2 decimals | N-U20-054 |
| VDR-U20-C182 | FUNCTION MAPPING REQUIRED | payment_stripe/const.py:64 | 'authorized': ('requires_capture',), | FACT | payment_stripe installed | — | Stripe status mapping: requires_confirmation/requires_action ignored; processing/pending -> pending; requires_capture -> authorized; succeeded -> done; canceled -> cancel; requires_payment_method/failed -> error | N-U20-055 |
| VDR-U20-C183 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_transaction.py:389 | Received data with invalid intent status | FACT | payment_stripe installed | — | Unknown Stripe status becomes error | N-U20-055 |
| VDR-U20-C184 | FUNCTION MAPPING REQUIRED | payment_adyen/models/payment_transaction.py:97 | if not self.provider_id.capture_manually: | FACT | payment_adyen installed | — | Adyen successful result is done unless manual capture is configured, in which case AUTHORISATION gives authorized and CAPTURE gives done | N-U20-055 |
| VDR-U20-C185 | FUNCTION MAPPING REQUIRED | payment_aps/const.py:7 | 'done': ('14',), | FACT | payment_aps installed | — | APS: status 14 done, 19 pending, everything else error | N-U20-055 |
| VDR-U20-C186 | FUNCTION MAPPING REQUIRED | payment_asiapay/const.py:152 | 'done': ('0',), | FACT | payment_asiapay installed | — | AsiaPay: successcode 0 done, 1 error, other codes error with 'Unknown success code' | N-U20-055 |
| VDR-U20-C187 | FUNCTION MAPPING REQUIRED | payment_authorize/models/payment_transaction.py:192 | status_code = response_content.get('x_response_code', '3') | FACT | payment_authorize installed | — | Authorize.Net: 1 approved (auth_capture/prior_auth_capture -> done; auth_only -> authorized; void -> canceled or done for validation/refund; refund -> done), 2 declined -> canceled, 4 held -> pending, else error | N-U20-055 |
| VDR-U20-C188 | FUNCTION MAPPING REQUIRED | payment_buckaroo/const.py:50 | 'done': (190,), | FACT | payment_buckaroo installed | — | Buckaroo: 190 done; 790-793 pending; cancel/refused/error code lists; unknown codes error | N-U20-055 |
| VDR-U20-C189 | FUNCTION MAPPING REQUIRED | payment_dpo/models/payment_transaction.py:116 | const.PAYMENT_STATUS_MAPPING['authorized'] + const.PAYMENT_STATUS_MAPPING['done'] | FACT | payment_dpo installed | — | DPO authorized (001, 005) and done (000, 002) codes both call _set_done | N-U20-056 |
| VDR-U20-C190 | FUNCTION MAPPING REQUIRED | payment_ecpay/models/payment_transaction.py:130 | elif return_code in const.SUCCESS_CODE_MAPPING["done"]: | FACT | payment_ecpay installed | — | ECPay: RtnCode in done list -> done; any other code -> error with RtnMsg | N-U20-055 |
| VDR-U20-C191 | FUNCTION MAPPING REQUIRED | payment_flutterwave/const.py:35 | 'done': ['successful'], | FACT | payment_flutterwave installed | — | Flutterwave: successful done; pending/pending auth pending (records authorization URL as provider_reference); cancelled cancel; failed error | N-U20-055 |
| VDR-U20-C192 | FUNCTION MAPPING REQUIRED | payment_iyzico/const.py:41 | 'done': ('SUCCESS',), | FACT | payment_iyzico installed | — | Iyzico: SUCCESS done; INIT_*/PENDING_CREDIT pending; FAILURE error | N-U20-055 |
| VDR-U20-C193 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/models/payment_transaction.py:257 | const.TRANSACTION_STATUS_MAPPING['done'] | FACT | payment_mercado_pago installed | — | Mercado Pago maps status to pending/done/canceled/error and falls back to the unknown payment method | N-U20-055 |
| VDR-U20-C194 | FUNCTION MAPPING REQUIRED | payment_mollie/models/payment_transaction.py:121 | self._set_authorized() | FACT | payment_mollie installed | — | Mollie status authorized calls _set_authorized although the provider declares no manual-capture support | N-U20-056 |
| VDR-U20-C195 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:159 | _check_state_authorized_supported | INFERENCE | payment_mollie installed | RT | Engine constraint rejects authorized state when provider.support_manual_capture is empty (lines 158-167), so a Mollie authorized message would raise ValidationError at runtime | N-U20-056 |
| VDR-U20-C196 | FUNCTION MAPPING REQUIRED | payment_nuvei/const.py:65 | 'done': ('approved', 'ok',), | FACT | payment_nuvei installed | — | Nuvei: approved/ok done; pending; declined/error/fail error | N-U20-055 |
| VDR-U20-C197 | FUNCTION MAPPING REQUIRED | payment_paymob/models/payment_transaction.py:146 | elif payment_data.get('success') == 'true': | FACT | payment_paymob installed | — | Paymob: pending == true -> pending; success == true -> done; otherwise error with data.message | N-U20-055 |
| VDR-U20-C198 | FUNCTION MAPPING REQUIRED | payment_paypal/const.py:48 | 'APPROVED', | FACT | payment_paypal installed | — | PayPal: PENDING/CREATED/APPROVED pending; COMPLETED/CAPTURED done; DECLINED/DENIED/VOIDED cancel; FAILED error | N-U20-055 |
| VDR-U20-C199 | FUNCTION MAPPING REQUIRED | payment_payu/const.py:97 | "done": ("success",), | FACT | payment_payu installed | — | PayU: success done, pending pending, failure error | N-U20-055 |
| VDR-U20-C200 | FUNCTION MAPPING REQUIRED | payment_razorpay/models/payment_transaction.py:146 | if self.provider_id.capture_manually: | FACT | payment_razorpay installed | — | Razorpay authorized maps to authorized only when manual capture is configured; otherwise no state change | N-U20-055 |
| VDR-U20-C201 | FUNCTION MAPPING REQUIRED | payment_redsys/models/payment_transaction.py:154 | if status_code in const.PAYMENT_STATUS_MAPPING['done']: | FACT | payment_redsys installed | — | Redsys: Ds_Response done/cancel/error lists; error codes mapped to generic messages | N-U20-055 |
| VDR-U20-C202 | FUNCTION MAPPING REQUIRED | payment_toss_payments/const.py:27 | 'canceled': 'EXPIRED', | FACT | payment_toss_payments installed | — | Toss: DONE done; EXPIRED canceled; ABORTED error | N-U20-055 |
| VDR-U20-C203 | FUNCTION MAPPING REQUIRED | payment_worldline/models/payment_transaction.py:273 | elif status in const.PAYMENT_STATUS_MAPPING['done']: | FACT | payment_worldline installed | — | Worldline: pending/done/cancel/declined maps; AUTHORIZATION_REQUESTED on token payment becomes error to force the redirect flow | N-U20-055 |
| VDR-U20-C204 | FUNCTION MAPPING REQUIRED | payment_xendit/models/payment_transaction.py:203 | elif payment_status in const.PAYMENT_STATUS_MAPPING['done']: | FACT | payment_xendit installed | — | Xendit maps statuses to pending/done/cancel/error; an unmapped status leaves the state unchanged (no else branch) | N-U20-055 |
| VDR-U20-C205 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:1052 | if not is_html_empty(status_message): | FACT | always | — | _get_status_message returns the configured message only if not empty | N-U20-057 |
| VDR-U20-C206 | FUNCTION MAPPING REQUIRED | payment/security/ir.model.access.csv:4 | payment_provider_system | FACT | always | — | ACL on payment.provider: base.group_system read/write/create/unlink and no other group | N-U20-061 |
| VDR-U20-C207 | FUNCTION MAPPING REQUIRED | payment/security/ir.model.access.csv:11 | payment_token_employee | FACT | always | — | ACL on payment.token: employee, portal and public read; system full | N-U20-061 |
| VDR-U20-C208 | FUNCTION MAPPING REQUIRED | account_payment/security/ir.model.access.csv:4 | payment_transaction_user | FACT | account_payment installed | — | account_payment adds read/write/create on payment.transaction to the invoicing group | N-U20-061 |
| VDR-U20-C209 | FUNCTION MAPPING REQUIRED | payment/security/payment_security.xml:6 | payment_provider_company_rule | FACT | always | — | Record rule company_id parent_of company_ids on providers | N-U20-061 |
| VDR-U20-C210 | FUNCTION MAPPING REQUIRED | payment/security/payment_security.xml:25 | [('partner_id', '=', user.partner_id.id)] | FACT | always | — | Token rule: users, portal, public see only their own partner's tokens | N-U20-061 |
| VDR-U20-C211 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_provider.py:37 | groups='base.group_system' | FACT | payment_stripe installed | — | stripe_secret_key restricted to system group | N-U20-062 |
| VDR-U20-C212 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_provider.py:44 | groups='base.group_system' | FACT | payment_stripe installed | — | stripe_webhook_secret restricted to system group | N-U20-062 |
| VDR-U20-C213 | FUNCTION MAPPING REQUIRED | payment_adyen/models/payment_provider.py:33 | groups='base.group_system' | FACT | payment_adyen installed | — | adyen_api_key restricted to system group (merchant account and HMAC key also) | N-U20-062 |
| VDR-U20-C214 | FUNCTION MAPPING REQUIRED | payment_xendit/models/payment_provider.py:28 | groups='base.group_system' | FACT | payment_xendit installed | — | xendit_secret_key restricted to system group | N-U20-062 |
| VDR-U20-C215 | FUNCTION MAPPING REQUIRED | payment_worldline/models/payment_provider.py:34 | worldline_api_secret = fields.Char( | INFERENCE | payment_worldline installed | — | Lines 34-38: the field definition has no groups argument (ast scan of all payment_* provider fields found groups absent for worldline_api_key/api_secret/webhook_key/webhook_secret) | N-U20-063 |
| VDR-U20-C216 | FUNCTION MAPPING REQUIRED | payment_worldline/models/payment_provider.py:44 | worldline_webhook_secret = fields.Char( | INFERENCE | payment_worldline installed | — | Lines 44-48: webhook secret also has no groups argument | N-U20-063 |
| VDR-U20-C217 | FUNCTION MAPPING REQUIRED | payment_paymob/models/payment_provider.py:45 | paymob_hmac_key = fields.Char( | INFERENCE | payment_paymob installed | — | Lines 45-49: HMAC key has no groups argument while paymob_secret_key (line 43) has | N-U20-063 |
| VDR-U20-C218 | FUNCTION MAPPING REQUIRED | payment_paymob/models/payment_provider.py:50 | paymob_api_key = fields.Char( | INFERENCE | payment_paymob installed | — | Lines 50-54: API key (exchanged for access tokens, line 252 of the same file) has no groups argument | N-U20-063 |
| VDR-U20-C219 | FUNCTION MAPPING REQUIRED | payment_stripe/views/payment_provider_views.xml:25 | password="True" | FACT | payment_stripe installed | — | Provider form shows Stripe secret key and webhook secret as password fields | N-U20-062 |
| VDR-U20-C220 | FUNCTION MAPPING REQUIRED | payment/const.py:9 | SENSITIVE_KEYS = set() | FACT | always | — | Base mask set is empty; only add-ons extend it | N-U20-064 |
| VDR-U20-C221 | FUNCTION MAPPING REQUIRED | payment_stripe/const.py:5 | SENSITIVE_KEYS = {'client_secret'} | FACT | payment_stripe installed | — | Stripe adds client_secret to the global set | N-U20-064 |
| VDR-U20-C222 | FUNCTION MAPPING REQUIRED | payment_toss_payments/const.py:5 | SENSITIVE_KEYS = {'secret'} | FACT | payment_toss_payments installed | — | Toss adds secret to the global set | N-U20-064 |
| VDR-U20-C223 | FUNCTION MAPPING REQUIRED | payment/logging.py:52 | "[REDACTED]" if k in self._sensitive_keys | FACT | always | — | SensitiveDataFilter masks dict keys and quoted JSON values listed in the set in log args | N-U20-064 |
| VDR-U20-C224 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:874 | log_msg += " Payload:\n%(payload)s" | FACT | always | — | provider._log_request appends the request payload to the info log | N-U20-064 |
| VDR-U20-C225 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:906 | 'data': response.text, | FACT | always | — | provider._log_response logs the full response body | N-U20-064 |
| VDR-U20-C226 | FUNCTION MAPPING REQUIRED | payment_stripe/controllers/main.py:77 | Notification received from Stripe with data | FACT | payment_stripe installed | — | Webhook controllers log the whole notification with pprint (same pattern in the other gateway controllers) | N-U20-064 |
| VDR-U20-C227 | FUNCTION MAPPING REQUIRED | payment_authorize/models/authorize_request.py:13 | _logger = logging.getLogger(__name__) | FACT | payment_authorize installed | — | Authorize.Net request helper uses the standard logger (no payment mask); it logs requests without merchantAuthentication | N-U20-064 |
| VDR-U20-C228 | FUNCTION MAPPING REQUIRED | payment_razorpay/controllers/onboarding.py:31 | Returning from authorization with data | FACT | payment_razorpay installed | — | Razorpay onboarding logs the OAuth return data (authorization code) with the standard logger | N-U20-064 |
| VDR-U20-C229 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_provider.py:33 | stripe_secret_key = fields.Char( | INFERENCE | always | — | Credentials are ordinary Char columns (no encryption declared in the model); sensitivity is by group and view masking only | N-U20-065 |
| VDR-U20-C230 | FUNCTION MAPPING REQUIRED | payment_paypal/models/payment_provider.py:180 | 'paypal_access_token': access_token, | FACT | payment_paypal installed | — | OAuth access tokens are written back to the provider row (PayPal, Mercado Pago, Razorpay refresh flows) | N-U20-065 |
| VDR-U20-C231 | FUNCTION MAPPING REQUIRED | payment_authorize/models/authorize_request.py:145 | get('cardNumber')[-4:] | FACT | payment_authorize installed | — | Authorize.Net token keeps only the last four digits | N-U20-066 |
| VDR-U20-C232 | FUNCTION MAPPING REQUIRED | payment_xendit/models/payment_transaction.py:226 | payment_data['masked_card_number'][-4:] | FACT | payment_xendit installed | — | Xendit token keeps only the last four digits and the gateway token id | N-U20-066 |
| VDR-U20-C233 | FUNCTION MAPPING REQUIRED | payment_razorpay/data/neutralize.sql:10 | razorpay_access_token_expiry = NULL | FACT | always | — | Razorpay neutralization clears eight credential/token columns | N-U20-067 |
| VDR-U20-C234 | FUNCTION MAPPING REQUIRED | payment/security/ir.model.access.csv:4 | payment_provider_system | OBSERVATION | restored DB | — | Restored DB: ir_model_access holds one row for payment.provider (Administrator, full); 68 credential/identifier columns of payment_provider have zero non-NULL values across the 25 rows | N-U20-068 |
| VDR-U20-C235 | FUNCTION MAPPING REQUIRED | payment/security/payment_security.xml:22 | payment_token_user_rule | OBSERVATION | restored DB | — | Restored DB: payment module seeds 5 ir.rule rows (provider company, transaction company, token user, token company, capture wizard); no res.groups seeded by any payment_* module | N-U20-068 |
| VDR-U20-C236 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_provider.py:53 | 'support_express_checkout': True, | FACT | payment_stripe installed | — | Stripe: express checkout, manual capture full_only, refund partial, tokenization | N-U20-071 |
| VDR-U20-C237 | FUNCTION MAPPING REQUIRED | payment_adyen/models/payment_provider.py:92 | 'support_manual_capture': 'partial', | FACT | payment_adyen installed | — | Adyen: manual capture partial, refund partial, tokenization | N-U20-071 |
| VDR-U20-C238 | FUNCTION MAPPING REQUIRED | payment_authorize/models/payment_provider.py:66 | 'support_refund': 'full_only', | FACT | payment_authorize installed | — | Authorize.Net: manual capture full_only, refund full_only, tokenization | N-U20-071 |
| VDR-U20-C239 | FUNCTION MAPPING REQUIRED | payment_razorpay/models/payment_provider.py:77 | 'support_refund': 'partial', | FACT | payment_razorpay installed | — | Razorpay: manual capture full_only, refund partial, tokenization | N-U20-071 |
| VDR-U20-C240 | FUNCTION MAPPING REQUIRED | payment_flutterwave/models/payment_provider.py:46 | 'support_tokenization': True, | FACT | payment_flutterwave installed | — | Flutterwave: tokenization only | N-U20-071 |
| VDR-U20-C241 | FUNCTION MAPPING REQUIRED | payment_worldline/models/payment_provider.py:56 | 'support_tokenization': True, | FACT | payment_worldline installed | — | Worldline: tokenization only | N-U20-071 |
| VDR-U20-C242 | FUNCTION MAPPING REQUIRED | payment_xendit/models/payment_provider.py:42 | support_tokenization = True | FACT | payment_xendit installed | — | Xendit: tokenization only | N-U20-071 |
| VDR-U20-C243 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/models/payment_provider.py:69 | 'support_tokenization': True, | FACT | payment_mercado_pago installed | — | Mercado Pago: tokenization only | N-U20-071 |
| VDR-U20-C244 | FUNCTION MAPPING REQUIRED | payment_demo/models/payment_provider.py:20 | 'support_express_checkout': True, | FACT | payment_demo installed | — | Demo: express checkout, partial manual capture, partial refund, tokenization | N-U20-071 |
| VDR-U20-C245 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:268 | 'support_refund': 'none', | INFERENCE | always | — | A grep of the 23 add-ons finds no _compute_feature_support_fields override in aps, asiapay, buckaroo, custom, dpo, ecpay, iyzico, mollie, nuvei, paymob, paypal, payu, redsys, toss, so the base default (no refund, no capture, no tokenization) applies to them | N-U20-071 |
| VDR-U20-C246 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:716 | reference_prefix = f'R-{self.reference}' | FACT | always | — | Refund child: R- prefix, negated amount, operation refund | N-U20-072 |
| VDR-U20-C247 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:720 | reference_prefix = f'P-{self.reference}' | FACT | always | — | Partial capture/void child: P- prefix, same operation as source | N-U20-072 |
| VDR-U20-C248 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:1074 | fully_voided = all(tx.state == | FACT | always | — | Source becomes cancel if all done/cancel siblings are canceled else done, when sibling amounts sum to source amount | N-U20-072 |
| VDR-U20-C249 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:322 | Only confirmed transactions can be refunded | FACT | always | — | action_refund requires all transactions in done state | N-U20-074 |
| VDR-U20-C250 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:696 | provider is disabled | FACT | always | — | Capture, void, refund and token charge refuse a disabled provider | N-U20-074 |
| VDR-U20-C251 | FUNCTION MAPPING REQUIRED | payment_stripe/controllers/main.py:139 | refund_tx_sudo = self._create_refund_tx_from_refund(tx_sudo, refund) | FACT | payment_stripe installed | — | Stripe webhook charge.refunded creates refund child transactions for refunds not yet recorded | N-U20-073 |
| VDR-U20-C252 | FUNCTION MAPPING REQUIRED | payment_adyen/models/payment_transaction.py:281 | tx = self._adyen_create_child_tx(source_tx, payment_data, is_refund=True) | FACT | payment_adyen installed | — | Adyen creates a refund child for REFUND notifications not initiated from Odoo | N-U20-073 |
| VDR-U20-C253 | FUNCTION MAPPING REQUIRED | payment_razorpay/models/payment_transaction.py:317 | tx = self._razorpay_create_refund_tx_from_payment_data( | FACT | payment_razorpay installed | — | Razorpay creates a refund child for refund notifications initiated at Razorpay | N-U20-073 |
| VDR-U20-C254 | FUNCTION MAPPING REQUIRED | payment_authorize/models/payment_transaction.py:102 | has not been settled | FACT | payment_authorize installed | — | Authorize.Net: authorized-pending payments are voided instead of refunded; settled ones refunded; unknown status errors | N-U20-076 |
| VDR-U20-C255 | FUNCTION MAPPING REQUIRED | payment_razorpay/models/payment_transaction.py:281 | can't be manually voided from Odoo | FACT | payment_razorpay installed | — | Razorpay _send_void_request raises UserError | N-U20-077 |
| VDR-U20-C256 | FUNCTION MAPPING REQUIRED | payment_razorpay/models/payment_transaction.py:202 | earlier_pending_tx = self.search([ | FACT | payment_razorpay installed | — | Token payments are blocked for 36 hours after an earlier pending Razorpay token payment on the same reference prefix | N-U20-077 |
| VDR-U20-C257 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:185 | provider_sudo.allow_tokenization | FACT | always | — | Tokenize is set only if provider allows, method supports, and flow requires or customer requested | N-U20-075 |
| VDR-U20-C258 | FUNCTION MAPPING REQUIRED | payment/controllers/portal.py:332 | do not have access | FACT | always | — | Token flow raises AccessError when the payer's commercial partner differs from the token owner's | N-U20-075 |
| VDR-U20-C259 | FUNCTION MAPPING REQUIRED | payment/models/payment_transaction.py:884 | if not (token_values := self._extract_token_values(payment_data)): | FACT | always | — | _tokenize creates a token only if the provider returns token values (base returns empty dict) | N-U20-075 |
| VDR-U20-C260 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_transaction.py:432 | 'stripe_payment_method': payment_method['id'], | FACT | payment_stripe installed | — | Stripe token stores customer id, PaymentMethod id, mandate and last4 | N-U20-075 |
| VDR-U20-C261 | FUNCTION MAPPING REQUIRED | payment_razorpay/models/payment_transaction.py:475 | 'provider_ref': f'{payment_data["customer_id"]},{payment_data["token_id"]}', | FACT | payment_razorpay installed | — | Razorpay token provider_ref combines customer id and token id | N-U20-075 |
| VDR-U20-C262 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:436 | ('state', 'in', ['enabled', 'test']), | FACT | always | — | _get_compatible_providers base domain: company check domain and state enabled/test | N-U20-081 |
| VDR-U20-C263 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:588 | providers = providers.filtered('is_published') | FACT | always | — | Non-internal users only see published providers | N-U20-081 |
| VDR-U20-C264 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:596 | not p.available_country_ids | FACT | always | — | Country filter: empty list means all countries | N-U20-081 |
| VDR-U20-C265 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:617 | currency.compare_amounts(p.maximum_amount, converted_amount) != -1 | FACT | always | — | Maximum amount is compared in company currency after conversion at today's rate | N-U20-081 |
| VDR-U20-C266 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:632 | not p.available_currency_ids | FACT | always | — | Currency filter: empty list means all currencies | N-U20-081 |
| VDR-U20-C267 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:206 | if supported_currencies < all_currencies: | FACT | always | — | available_currency_ids is set only when the add-on returns a strict subset; otherwise left empty | N-U20-082 |
| VDR-U20-C268 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:224 | return self.env['res.currency'].with_context(active_test=False).search([]) | FACT | always | — | Default _get_supported_currencies returns all currencies including inactive | N-U20-082 |
| VDR-U20-C269 | FUNCTION MAPPING REQUIRED | payment_buckaroo/models/payment_provider.py:37 | c.name in const.SUPPORTED_CURRENCIES | FACT | payment_buckaroo installed | — | Buckaroo filters to its constant currency list | N-U20-082 |
| VDR-U20-C270 | FUNCTION MAPPING REQUIRED | payment_asiapay/models/payment_provider.py:54 | selected by AsiaPay account | FACT | payment_asiapay installed | — | AsiaPay: more than one currency not allowed unless disabled; currency must be in the code table | N-U20-083 |
| VDR-U20-C271 | FUNCTION MAPPING REQUIRED | payment_authorize/models/payment_provider.py:56 | selected by Authorize.Net account | FACT | payment_authorize installed | — | Authorize.Net: one currency per account | N-U20-083 |
| VDR-U20-C272 | FUNCTION MAPPING REQUIRED | payment_paymob/models/payment_provider.py:62 | selected per Paymob account | FACT | payment_paymob installed | — | Paymob: one currency per account; account country limited to AE, EG, OM, SA | N-U20-083 |
| VDR-U20-C273 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/models/payment_provider.py:100 | Only the currency %s | FACT | payment_mercado_pago installed | — | Mercado Pago: currency forced to the account country's currency | N-U20-083 |
| VDR-U20-C274 | FUNCTION MAPPING REQUIRED | payment_ecpay/const.py:10 | SUPPORTED_CURRENCY = "TWD" | FACT | payment_ecpay installed | — | ECPay supports TWD only | N-U20-083 |
| VDR-U20-C275 | FUNCTION MAPPING REQUIRED | payment_toss_payments/const.py:13 | SUPPORTED_CURRENCY = 'KRW' | FACT | payment_toss_payments installed | — | Toss supports KRW only | N-U20-083 |
| VDR-U20-C276 | FUNCTION MAPPING REQUIRED | payment_payu/const.py:17 | SUPPORTED_CURRENCIES = ["INR"] | FACT | payment_payu installed | — | PayU supports INR only | N-U20-083 |
| VDR-U20-C277 | FUNCTION MAPPING REQUIRED | payment_mollie/const.py:44 | 'THB', | FACT | payment_mollie installed | — | Mollie list includes THB | N-U20-084 |
| VDR-U20-C278 | FUNCTION MAPPING REQUIRED | payment_paypal/const.py:31 | 'THB', | FACT | payment_paypal installed | — | PayPal list includes THB | N-U20-084 |
| VDR-U20-C279 | FUNCTION MAPPING REQUIRED | payment_razorpay/const.py:93 | 'THB', | FACT | payment_razorpay installed | — | Razorpay list includes THB (international payments) | N-U20-084 |
| VDR-U20-C280 | FUNCTION MAPPING REQUIRED | payment_xendit/const.py:9 | 'THB', | FACT | payment_xendit installed | — | Xendit list includes THB | N-U20-084 |
| VDR-U20-C281 | FUNCTION MAPPING REQUIRED | payment_asiapay/const.py:38 | 'THB': '764', | FACT | payment_asiapay installed | — | AsiaPay currency code table includes THB | N-U20-084 |
| VDR-U20-C282 | FUNCTION MAPPING REQUIRED | payment_flutterwave/const.py:7 | SUPPORTED_CURRENCIES = [ | OBSERVATION | source | — | Flutterwave list (GBP, CAD, XAF, ... USD, ZMW) has no THB; same for Iyzico, Nuvei, Buckaroo (observation from reading the lists) | N-U20-084 |
| VDR-U20-C283 | FUNCTION MAPPING REQUIRED | payment/data/payment_method_data.xml:2869 | <field name="code">promptpay</field> | FACT | always | — | PromptPay payment method record with country TH and currency THB (lines 2879, 2884) | N-U20-085 |
| VDR-U20-C284 | FUNCTION MAPPING REQUIRED | payment/data/payment_method_data.xml:2328 | <field name="code">online_banking_thailand</field> | FACT | always | — | Online Banking Thailand payment method record (country TH, currency THB) | N-U20-085 |
| VDR-U20-C285 | FUNCTION MAPPING REQUIRED | payment_adyen/const.py:58 | 'online_banking_thailand': 'molpay_ebanking_TH', | FACT | payment_adyen installed | — | Adyen maps Online Banking Thailand to molpay_ebanking_TH | N-U20-085 |
| VDR-U20-C286 | FUNCTION MAPPING REQUIRED | payment_asiapay/const.py:117 | 'truemoney': 'TRUEMONEY', | FACT | payment_asiapay installed | — | AsiaPay maps TrueMoney, LINE Pay, ShopeePay, KTB, TMB to its channel codes | N-U20-085 |
| VDR-U20-C287 | FUNCTION MAPPING REQUIRED | payment_asiapay/models/payment_provider.py:21 | ("siampay", "SiamPay") | FACT | payment_asiapay installed | — | AsiaPay brand selection includes SiamPay | N-U20-085 |
| VDR-U20-C288 | FUNCTION MAPPING REQUIRED | payment_xendit/const.py:38 | 'promptpay', | FACT | payment_xendit installed | — | Xendit default payment methods include promptpay, linepay, shopeepay under the TH comment | N-U20-085 |
| VDR-U20-C289 | FUNCTION MAPPING REQUIRED | payment_xendit/const.py:110 | 'scb': 'DD_SCB_MB', | FACT | payment_xendit installed | — | Xendit maps SCB, Krungthai and Bangkok Bank direct debit channels | N-U20-085 |
| VDR-U20-C290 | FUNCTION MAPPING REQUIRED | payment_stripe/const.py:128 | 'TH',  # Beta | FACT | payment_stripe installed | — | TH appears in Stripe SUPPORTED_COUNTRIES (onboarding eligibility) | N-U20-086 |
| VDR-U20-C291 | FUNCTION MAPPING REQUIRED | payment/data/payment_method_data.xml:2869 | <field name="code">promptpay</field> | OBSERVATION | restored DB | — | Restored DB: PromptPay is linked to adyen, asiapay, stripe, xendit; TrueMoney/LINE Pay to asiapay, xendit; ShopeePay to xendit; Alipay Plus to worldline; 16 payment methods carry country TH and 17 carry THB; all of them inactive (only demo and cash on delivery methods are active) | N-U20-085 |
| VDR-U20-C292 | FUNCTION MAPPING REQUIRED | payment/data/payment_provider_data.xml:442 | payment_provider_stripe | OBSERVATION | restored DB | — | Restored DB: company currency THB; res_currency active only THB and USD; providers with explicit currency lists: buckaroo 8, ecpay 1, flutterwave 22, iyzico 8, mollie 30, nuvei 9, paypal 24, payu 1, razorpay 92, toss 1, xendit 7; others empty | N-U20-088 |
| VDR-U20-C293 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_provider.py:13 | CHECK(custom_mode IS NULL | FACT | payment_custom installed | — | SQL constraint: custom_mode only for code custom and mandatory for it | N-U20-094 |
| VDR-U20-C294 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_provider.py:23 | required_if_provider='custom', | FACT | payment_custom installed | — | custom_mode is required if provider custom (selection wire_transfer only) | N-U20-094 |
| VDR-U20-C295 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_provider.py:57 | Please use the following transfer details | FACT | payment_custom installed | — | action_recompute_pending_msg builds an HTML message listing the bank accounts of the company's bank journals (only if account_payment installed) | N-U20-092 |
| VDR-U20-C296 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_transaction.py:45 | communication = self.invoice_ids[0].payment_reference | FACT | payment_custom installed | — | _get_communication: invoice payment_reference, else sale order reference, else transaction reference | N-U20-092 |
| VDR-U20-C297 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_transaction.py:64 | self._set_pending() | FACT | payment_custom installed | — | _apply_updates for custom sets pending with log 'Validated custom payment' | N-U20-091 |
| VDR-U20-C298 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_transaction.py:28 | 'api_url': CustomController._process_url, | FACT | payment_custom installed | — | Rendering values post to /payment/custom/process with the reference | N-U20-091 |
| VDR-U20-C299 | FUNCTION MAPPING REQUIRED | sale/models/payment_transaction.py:56 | if pending_tx.provider_id.code == 'custom': | FACT | sale installed | — | Sale post-process for pending custom transactions sets the order reference and sends the quotation | N-U20-091 |
| VDR-U20-C300 | FUNCTION MAPPING REQUIRED | delivery/models/payment_transaction.py:15 | cod_pending_txs.sale_order_ids.filtered( | FACT | delivery installed | — | Delivery post-process confirms draft orders of pending cash-on-delivery transactions | N-U20-091 |
| VDR-U20-C301 | FUNCTION MAPPING REQUIRED | delivery/models/payment_provider.py:39 | if not sale_order.carrier_id.allow_cash_on_delivery: | FACT | delivery installed | — | Cash on delivery removed from compatible providers unless the carrier allows it | N-U20-093 |
| VDR-U20-C302 | FUNCTION MAPPING REQUIRED | payment_custom/data/payment_method_data.xml:8 | <field name="active">False</field> | FACT | payment_custom installed | — | Wire Transfer payment method ships inactive | N-U20-095 |
| VDR-U20-C303 | FUNCTION MAPPING REQUIRED | delivery/data/payment_provider_data.xml:16 | <field name="state">enabled</field> | FACT | delivery installed | — | Cash on Delivery provider ships enabled and published (is_published True) | N-U20-095 |
| VDR-U20-C304 | FUNCTION MAPPING REQUIRED | payment_custom/models/payment_transaction.py:71 | other_provider_txs = self.filtered( | FACT | payment_custom installed | — | _log_received_message skips custom transactions | N-U20-096 |
| VDR-U20-C305 | FUNCTION MAPPING REQUIRED | payment_custom/controllers/main.py:19 | request.env['payment.transaction'].sudo()._process('custom', post) | INFERENCE | payment_custom installed | — | Anonymous caller with a reference moves the draft transaction to pending (state machine allows only draft to pending); combined with PORTAL_NOCHK in CAP-U20-01 | N-U20-097 |
| VDR-U20-C306 | FUNCTION MAPPING REQUIRED | payment_custom/data/payment_provider_data.xml:9 | <field name="custom_mode">wire_transfer</field> | OBSERVATION | restored DB | — | Restored DB: provider 22 Wire Transfer (custom, wire_transfer) disabled, unpublished, sequence 30; provider 25 Cash on Delivery (custom, cash_on_delivery) enabled, published, owned by module delivery; payment methods wire_transfer inactive, cash_on_delivery active; 6 delivery carriers, none with the cash-on-delivery option; no account.payment.method.line row for any provider | N-U20-097 |
| VDR-U20-C307 | FUNCTION MAPPING REQUIRED | delivery/data/payment_provider_data.xml:17 | <field name="is_published">True</field> | OBSERVATION | restored DB | — | Restored DB: COD pending_msg is 'The delivery staff will collect payment upon delivery.' (seeded text) | N-U20-095 |
| VDR-U20-C308 | FUNCTION MAPPING REQUIRED | payment_demo/models/payment_provider.py:31 | Demo providers should never be enabled | FACT | payment_demo installed | — | Constraint: demo provider state must be test or disabled | N-U20-101 |
| VDR-U20-C309 | FUNCTION MAPPING REQUIRED | payment_demo/data/payment_provider_data.xml:6 | <field name="state">test</field> | FACT | payment_demo installed | — | Shipped data: state test, published, tokenization and express checkout allowed | N-U20-101 |
| VDR-U20-C310 | FUNCTION MAPPING REQUIRED | payment_demo/models/payment_transaction.py:123 | state = payment_data['simulated_state'] | FACT | payment_demo installed | — | _apply_updates reads the simulated_state from the data (pending, done, cancel, else error) | N-U20-102 |
| VDR-U20-C311 | FUNCTION MAPPING REQUIRED | payment_demo/models/payment_transaction.py:19 | def action_demo_set_done | FACT | payment_demo installed | — | Backend buttons call _process with simulated_state | N-U20-102 |
| VDR-U20-C312 | FUNCTION MAPPING REQUIRED | payment_demo/controllers/main.py:11 | def demo_simulate_payment(self, **data): | FACT | payment_demo installed | — | Public route: demo_simulate_payment(**data) passes arbitrary data to _process | N-U20-102 |
| VDR-U20-C313 | FUNCTION MAPPING REQUIRED | payment_demo/models/payment_token.py:9 | demo_simulated_state = fields.Selection( | FACT | payment_demo installed | — | Demo token stores the simulated state for future token payments | N-U20-102 |
| VDR-U20-C314 | FUNCTION MAPPING REQUIRED | payment_demo/data/payment_provider_data.xml:7 | <field name="is_published">True</field> | OBSERVATION | restored DB | — | Restored DB: provider 6 Demo state test, is_published true, allow_tokenization true, sequence 40; payment method demo active (support_tokenization true); no transactions or tokens | N-U20-103 |
| VDR-U20-C315 | FUNCTION MAPPING REQUIRED | payment/models/payment_provider.py:587 | if not self.env.user._is_internal(): | FACT | always | — | Published providers are shown to non-internal users (portal and public) — the demo provider qualifies in the restored DB | N-U20-103 |
| VDR-U20-C316 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_provider.py:465 | 'https://api.stripe.com/v1/' | FACT | provider installed | RT | Stripe API host (live and test share the host; test keys decide) | N-U20-107 |
| VDR-U20-C317 | FUNCTION MAPPING REQUIRED | payment_stripe/const.py:11 | PROXY_URL = 'https://stripe.api.odoo.com/api/stripe/' | FACT | provider installed | RT | Stripe Connect proxy run by the vendor (accounts, account_links) | N-U20-107 |
| VDR-U20-C318 | FUNCTION MAPPING REQUIRED | payment_adyen/models/payment_provider.py:165 | -checkout-live.adyenpayments | FACT | provider installed | RT | Adyen host built from the configured prefix: <prefix>.adyen.com in test, <prefix>-checkout-live.adyenpayments.com in live | N-U20-107 |
| VDR-U20-C319 | FUNCTION MAPPING REQUIRED | payment_aps/models/payment_provider.py:59 | https://checkout.payfort.com/FortAPI/paymentPage | FACT | provider installed | RT | APS (PayFort) live checkout page; sandbox sbcheckout.payfort.com | N-U20-107 |
| VDR-U20-C320 | FUNCTION MAPPING REQUIRED | payment_asiapay/const.py:8 | 'paydollar': 'https://www.paydollar.com/b2c2/eng/payment/payForm.jsp' | FACT | provider installed | RT | AsiaPay brand-specific checkout hosts (PayDollar, PesoPay, SiamPay, BimoPay); BimoPay has no sandbox entry and falls back to the PayDollar test host | N-U20-107 |
| VDR-U20-C321 | FUNCTION MAPPING REQUIRED | payment_authorize/models/authorize_request.py:34 | https://api.authorize.net/xml/v1/request.api | FACT | provider installed | RT | Authorize.Net live API; sandbox apitest.authorize.net | N-U20-107 |
| VDR-U20-C322 | FUNCTION MAPPING REQUIRED | payment_buckaroo/models/payment_provider.py:62 | https://checkout.buckaroo.nl/html/ | FACT | provider installed | RT | Buckaroo live checkout page; test testcheckout.buckaroo.nl | N-U20-107 |
| VDR-U20-C323 | FUNCTION MAPPING REQUIRED | payment_dpo/models/payment_provider.py:41 | https://secure.3gdirectpay.com/API/v6/ | FACT | provider installed | RT | DPO API (same host for live and test; token decides) | N-U20-107 |
| VDR-U20-C324 | FUNCTION MAPPING REQUIRED | payment_ecpay/models/payment_provider.py:77 | https://payment.ecpay.com.tw/Cashier/AioCheckOut/V5 | FACT | provider installed | RT | ECPay live checkout; stage host payment-stage.ecpay.com.tw | N-U20-107 |
| VDR-U20-C325 | FUNCTION MAPPING REQUIRED | payment_flutterwave/models/payment_provider.py:94 | https://api.flutterwave.com/v3/ | FACT | provider installed | RT | Flutterwave API | N-U20-107 |
| VDR-U20-C326 | FUNCTION MAPPING REQUIRED | payment_iyzico/models/payment_provider.py:59 | api_url = 'https://api.iyzipay.com' | FACT | provider installed | RT | Iyzico live API; sandbox sandbox-api.iyzipay.com | N-U20-107 |
| VDR-U20-C327 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/models/payment_provider.py:267 | urljoin('https://api.mercadopago.com', endpoint) | FACT | provider installed | RT | Mercado Pago API | N-U20-107 |
| VDR-U20-C328 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/const.py:8 | PROXY_URL = 'https://mercadopago.api.odoo.com/api/mercado_pago' | FACT | provider installed | RT | Mercado Pago OAuth proxy run by the vendor | N-U20-107 |
| VDR-U20-C329 | FUNCTION MAPPING REQUIRED | payment_mollie/models/payment_provider.py:54 | https://api.mollie.com/v2/ | FACT | provider installed | RT | Mollie API | N-U20-107 |
| VDR-U20-C330 | FUNCTION MAPPING REQUIRED | payment_nuvei/models/payment_provider.py:64 | https://secure.safecharge.com/ppp/purchase.do | FACT | provider installed | RT | Nuvei live purchase page; test ppp-test.safecharge.com | N-U20-107 |
| VDR-U20-C331 | FUNCTION MAPPING REQUIRED | payment_paymob/models/payment_provider.py:224 | url = f'https://{api_prefix}.paymob.com' | FACT | provider installed | RT | Paymob API host chosen by account country (uae, accept, oman, ksa) | N-U20-107 |
| VDR-U20-C332 | FUNCTION MAPPING REQUIRED | payment_paypal/models/payment_provider.py:135 | return 'https://api-m.paypal.com' | FACT | provider installed | RT | PayPal live API; sandbox api-m.sandbox.paypal.com | N-U20-107 |
| VDR-U20-C333 | FUNCTION MAPPING REQUIRED | payment_payu/const.py:8 | PAYMENT_API_LIVE_URL = "https://secure.payu.in" | FACT | provider installed | RT | PayU live payment host; OAuth proxy payu.api.odoo.com; partner API partner.payu.in | N-U20-107 |
| VDR-U20-C334 | FUNCTION MAPPING REQUIRED | payment_razorpay/const.py:3 | OAUTH_URL = 'https://razorpay.api.odoo.com/api/razorpay/1' | FACT | provider installed | RT | Razorpay OAuth proxy run by the vendor | N-U20-107 |
| VDR-U20-C335 | FUNCTION MAPPING REQUIRED | payment_razorpay/models/payment_provider.py:278 | f'https://api.razorpay.com/{api_version}/{endpoint}' | FACT | provider installed | RT | Razorpay API | N-U20-107 |
| VDR-U20-C336 | FUNCTION MAPPING REQUIRED | payment_redsys/models/payment_provider.py:58 | https://sis.redsys.es/sis/realizarPago | FACT | provider installed | RT | Redsys live payment page; test sis-t.redsys.es:25443 | N-U20-107 |
| VDR-U20-C337 | FUNCTION MAPPING REQUIRED | payment_toss_payments/models/payment_provider.py:94 | urljoin('https://api.tosspayments.com/', endpoint) | FACT | provider installed | RT | Toss Payments API | N-U20-107 |
| VDR-U20-C338 | FUNCTION MAPPING REQUIRED | payment_worldline/models/payment_provider.py:84 | https://payment.direct.worldline-solutions.com | FACT | provider installed | RT | Worldline live API; preprod host for test | N-U20-107 |
| VDR-U20-C339 | FUNCTION MAPPING REQUIRED | payment_xendit/models/payment_provider.py:90 | f'https://api.xendit.co/{endpoint}' | FACT | provider installed | RT | Xendit API | N-U20-107 |
| VDR-U20-C340 | FUNCTION MAPPING REQUIRED | payment_mercado_pago/controllers/onboarding.py:41 | if not request.validate_csrf(csrf_token): | FACT | payment_mercado_pago installed | — | OAuth return validates the CSRF token created in action_start_onboarding | N-U20-108 |
| VDR-U20-C341 | FUNCTION MAPPING REQUIRED | payment_razorpay/controllers/onboarding.py:42 | if not request.validate_csrf(csrf_token): | FACT | payment_razorpay installed | — | Razorpay OAuth return validates CSRF then writes credentials, enables and publishes the provider | N-U20-108 |
| VDR-U20-C342 | FUNCTION MAPPING REQUIRED | payment_payu/controllers/onboarding.py:48 | if not request.validate_csrf(csrf_token): | FACT | payment_payu installed | — | PayU OAuth return validates CSRF then stores key and salt and enables | N-U20-108 |
| VDR-U20-C343 | FUNCTION MAPPING REQUIRED | payment_razorpay/controllers/onboarding.py:21 | @route(OAUTH_RETURN_URL, type='http', auth='user' | FACT | payment_razorpay installed | — | The return routes require a logged-in user (auth user); the provider write is not sudo so ACL requires administrator | N-U20-108 |
| VDR-U20-C344 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_provider.py:159 | if self._stripe_get_country(self.env.company.country_id.code) not in const.SUPPORTED_COUNTRIES: | FACT | payment_stripe installed | — | Stripe onboarding refuses companies whose country is not in SUPPORTED_COUNTRIES (TH included as beta) | N-U20-108 |
| VDR-U20-C345 | FUNCTION MAPPING REQUIRED | payment_stripe/models/payment_provider.py:216 | 'POST', 'webhook_endpoints', data={ | FACT | payment_stripe installed | — | action_stripe_create_webhook registers the callback and stores the returned signing secret | N-U20-109 |
| VDR-U20-C346 | FUNCTION MAPPING REQUIRED | payment_paypal/models/payment_provider.py:95 | 'POST', '/v1/notifications/webhooks', json=data | FACT | payment_paypal installed | — | action_paypal_create_webhook registers the callback and stores webhook id; refuses a localhost base URL | N-U20-109 |
| VDR-U20-C347 | FUNCTION MAPPING REQUIRED | payment_razorpay/models/payment_provider.py:177 | webhook_secret = uuid.uuid4().hex | FACT | payment_razorpay installed | — | Razorpay generates a random webhook secret and registers it | N-U20-109 |
| VDR-U20-C348 | FUNCTION MAPPING REQUIRED | payment_asiapay/controllers/main.py:27 | Don't process the payment data | FACT | payment_asiapay installed | — | AsiaPay confirms only through the webhook, so an unreachable callback leaves transactions pending | N-U20-110 |
