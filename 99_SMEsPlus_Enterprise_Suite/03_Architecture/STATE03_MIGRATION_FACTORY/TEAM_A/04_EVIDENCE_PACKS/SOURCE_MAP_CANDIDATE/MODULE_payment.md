# Source Map (candidate) — `payment`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `payment` |
| Display name | Payment Engine |
| Manifest version | 2.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `de73163d7bb451cd` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/payment/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `onboarding`, `portal`
- Direct dependents in 300-module list (2): `account_payment`, `payment_custom`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (22): `payment_adyen`, `payment_aps`, `payment_asiapay`, `payment_authorize`, `payment_buckaroo`, `payment_demo`, `payment_dpo`, `payment_ecpay`, `payment_flutterwave`, `payment_iyzico`, `payment_mercado_pago`, `payment_mollie` … (+10)
- Custom / third-party modules that declare a dependency (name — license only) (1): `payment_2c2p` — Other proprietary

## 3. Capabilities / functions
- Manifest category / summary: Hidden / The payment engine used by payment provider modules.
- Inventory of user-facing artifacts (counts): menu items 0, views 20, window actions 5, server actions 1, reports 0, mail templates 0, scheduled jobs 1, wizards 3, web routes 7
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (6): `payment.provider` (Payment Provider); `payment.transaction` (Payment Transaction); `payment.method` (Payment Method); `payment.token` (Payment Token); `payment.capture.wizard` (Payment Capture Wizard); `payment.link.wizard` (Generate Payment Link)
- Objects extended from other modules (5): `ir.http`, `res.country`, `res.company`, `res.partner`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 2 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `payment.provider` ← Community: `account_payment`, `delivery`, `payment_adyen`, `payment_aps`, `payment_asiapay`, `payment_authorize`, `payment_buckaroo`, `payment_custom`, `payment_demo`, `payment_dpo` … (+19); open-license custom/third-party scanned: —
- `payment.transaction` ← Community: `account_payment`, `delivery`, `payment_adyen`, `payment_aps`, `payment_asiapay`, `payment_authorize`, `payment_buckaroo`, `payment_custom`, `payment_demo`, `payment_dpo` … (+20); open-license custom/third-party scanned: —
- `payment.method` ← Community: `l10n_ec_sale`; open-license custom/third-party scanned: —
- `payment.token` ← Community: `payment_adyen`, `payment_authorize`, `payment_demo`, `payment_flutterwave`, `payment_mercado_pago`, `payment_razorpay`, `payment_stripe`, `website_sale`; open-license custom/third-party scanned: —
- `payment.capture.wizard` ← Community: `payment_adyen`; open-license custom/third-party scanned: —
- `payment.link.wizard` ← Community: `account_payment`, `sale`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `ir.http`, `res.country`, `res.company`, `res.partner`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: `payment.provider` → ['disabled', 'enabled', 'test']; `payment.transaction` → ['draft', 'pending', 'authorized', 'done', 'cancel', 'error']
- Validation: 6 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Payment: Post-process transactions every 10 minutes
- Security: groups declared 0 (—); record rules 5 (of which company-scoped by text 3); access rows 12

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 94 of 96 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: payment (Payment Engine)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/payment.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. The module is labelled a hidden engine used by provider modules (payment/__manifest__.py:4-8); it is not itself an application.

## A. Capabilities / functions
- Core: a provider-neutral engine to take online payments from customers: provider setup, payment methods, saved payment details ("tokens"), transactions with a fixed status set, customer-facing payment pages, and post-payment finalisation (payment/models/payment_provider.py:21; payment/models/payment_method.py:11; payment/models/payment_token.py:7; payment/models/payment_transaction.py:24). Depends on onboarding and portal only (payment/__manifest__.py:8).
- Core: it contains no real gateway. The base provider list is "no provider set"; each gateway module adds its own code and behaviour, and the engine's request/response hooks are empty by default (payment/models/payment_provider.py:34-40; payment/models/payment_transaction.py:576-589, 611-621, 643-653, 675-685).
- Core customer routes: arbitrary payment page, payment-method management page, transaction creation, confirmation page, token archiving, payment-status page with polling (payment/controllers/portal.py:37, 193, 258, 394, 419; payment/controllers/post_processing.py:28, 41).
- Core back-office actions: capture, void, refund on transactions; partial capture wizard; payment-link wizard; manual post-processing trigger (payment/models/payment_transaction.py:266-328, 355-365; payment/wizards/payment_capture_wizard.py:8; payment/wizards/payment_link_wizard.py:10).
- Optional per provider: saving payment methods, manual capture (authorise then capture), express checkout, refunds (none / full only / partial), country, currency and maximum-amount limits, help/status messages (payment/models/payment_provider.py:63-134, 136-180).
- Conditional: a 10-minute background finaliser ships switched off and is switched on only while at least one provider is enabled or in test mode (payment/data/payment_cron.xml:4-15; payment/models/payment_provider.py:395-410).
- Conditional: onboarding shortcut in settings that installs a suggested gateway module by currency/country (INR -> Razorpay; Stripe-supported country -> Stripe; Mercado Pago country -> Mercado Pago) (payment/wizards/res_config_settings.py:61-71, 85-113).
- Seed data: 24 predefined provider records pointing to gateway modules, about 230 payment-method records, one generic inactive "unknown" method that cannot be deleted (payment/data/payment_provider_data.xml; payment/data/payment_method_data.xml:3623-3631; payment/models/payment_method.py:222-226).
- Neutralisation for test copies: enabled providers are set to disabled (payment/data/neutralize.sql).

## B. Business objects, relationships, lifecycle
- Provider -> company (required, default current company), -> many supported payment methods, -> transactions, -> tokens (payment/models/payment_provider.py:53-62; payment/models/payment_transaction.py:34-43; payment/models/payment_token.py:14-18). Provider states: disabled, enabled, test mode; a separate "published" flag controls website visibility (payment/models/payment_provider.py:41-52).
- Payment method: may be a "primary" method or a "brand" of one (e.g. card and its brands); carries tokenisation, express, manual-capture and refund support levels plus country/currency limits (payment/models/payment_method.py:21-38, 61-107).
- Token: links a partner, provider and method with a provider-side reference; can be archived, cannot be reactivated if its provider is disabled or method inactive; can never belong to the public partner (payment/models/payment_token.py:14-37, 76-105); (TEST) (payment/tests/test_payment_token.py:25-44).
- Transaction: provider, method, amount, currency, partner (address details copied at creation so later partner edits do not alter history), token, operation type, source/child links, live-vs-test flag, reference unique across the database (payment/models/payment_transaction.py:34-134, 135-138, 178-204); (TEST) live flag (payment/tests/test_payment_transaction.py:15-23).
- Transaction operation types: online redirect, online direct, online by token, validation (zero-value save of a method), offline by token, refund (payment/models/payment_transaction.py:77-89).
- Transaction status set: draft, pending, authorized, done (confirmed), cancel, error (payment/models/payment_transaction.py:65-69). Allowed moves are gated by the source status: to pending from draft; to authorized from draft or pending; to done from draft, pending, authorized or error; to cancel from draft, pending or authorized; to error from draft, pending or authorized. A move from another status is refused and logged; a repeated move to the same status is skipped (payment/models/payment_transaction.py:915-1000, 1002-1058); (TEST) (payment/tests/test_payment_transaction.py:321-345).
- Any status change resets the "post-processed" flag so downstream finalisation runs again (payment/models/payment_transaction.py:1052-1057); (TEST) (payment/tests/test_payment_transaction.py:333).
- Partial capture, void and refund create child transactions (prefixes "P-" and "R-", refunds carry a negative amount). The authorised parent becomes done or cancel only when child amounts equal the parent amount; all-cancelled means cancel (payment/models/payment_transaction.py:699-734, 1060-1078); (TEST) (payment/tests/test_payment_transaction.py:200-252).
- Customer payment flow: page validates access token -> compatible providers, methods and saved tokens are listed -> draft transaction created -> provider processes -> status page polls and post-processes -> landing page (payment/controllers/portal.py:40-170, 258-283, 285-372; payment/controllers/post_processing.py:41-73).
- Payment data from a provider is matched by reference, amount and currency are checked (refunds negated, minor-unit rounding), and mismatch sets the transaction to error before any update applies; validation transactions skip the check (payment/models/payment_transaction.py:738-756, 794-843); (TEST) (payment/tests/test_payment_transaction.py:254-287, 346).
- Token creation happens only after a transaction reaches authorized or done and tokenisation was requested (payment/models/payment_transaction.py:754-756, 876-896); (TEST) (payment/tests/test_payment_transaction.py:289-320).

## C. Validations, automation, security, multi-company
- Authorised status requires a provider that supports manual capture; a transaction cannot be created from an archived token (payment/models/payment_transaction.py:158-174).
- Provider: provider-specific mandatory fields enforced only while enabled or in test (payment/models/payment_provider.py:368-393); manual capture blocked if an active method does not support it (payment/models/payment_provider.py:322-332); company cannot be changed once transactions exist (onchange guard) (payment/models/payment_provider.py:306-318); records with a data identifier cannot be deleted, only disabled or uninstalled (payment/models/payment_provider.py:462-472); cannot publish a disabled provider (payment/models/payment_provider.py:537-538).
- Side effects of changing provider state: tokens of a provider moving between enabled/test/disabled are archived; going enabled/test activates its default methods, going disabled deactivates methods used only by disabled providers; cron toggled (payment/models/payment_provider.py:344-366, 412-449); (TEST) (payment/tests/test_payment_provider.py:20-98). Payment method archive, detach from provider, or loss of tokenisation archives related tokens; enabling a method requires an enabled provider (payment/models/payment_method.py:193-218); (TEST) (payment/tests/test_payment_method.py:15-28).
- Availability rules (provider): must be enabled or test; unpublished ones hidden from non-internal users; partner country, currency, maximum amount (converted to company currency), tokenisation and express-checkout requirements; a report records why each was excluded (payment/models/payment_provider.py:554-665); (TEST) (payment/tests/test_payment_provider.py:99-290). Method availability: primary only, must belong to a compatible provider, plus country/currency/tokenisation/express filters (payment/models/payment_method.py:230-325).
- Capture wizard: amount must be positive and not exceed authorised minus captured minus voided; partial capture only when both provider and method allow it; option to void the remainder (payment/wizards/payment_capture_wizard.py:41-127, 131-161); (TEST) (payment/tests/test_payment_capture_wizard.py:11-60).
- Customer page security: signed access token binds partner, amount and currency (payment/utils.py:15-49); wrong token -> not found on page, forbidden on transaction creation (payment/controllers/portal.py:75-78, 273-277); a logged-in user always pays as their own partner; public users cannot save methods; token payments require the token's commercial partner to match (payment/controllers/portal.py:80-97, 324-333); only whitelisted request keys are accepted (payment/controllers/portal.py:480-511); (TEST) (payment/tests/test_flows.py:242-312). Currency must exist and be active (payment/controllers/portal.py:106-109).
- Back-office capture/void/refund require write access on the transaction first, then run with elevated rights (payment/utils.py:231-242; payment/models/payment_transaction.py:273, 298, 319); (TEST) blocked for unauthorised user (payment/tests/test_payment_transaction.py:52-69).
- Access control lists: system group has full rights on providers and transactions; all users see methods and tokens read-only; only system may change them; internal users have no direct rights on the payment-link wizard and may create/edit (no delete) the capture wizard (payment/security/ir.model.access.csv:2-13). Note that no ordinary user group other than system has rights on payment transactions in this module; other modules extend it (see D) (payment/security/ir.model.access.csv:13).
- Record rules: providers visible if their company is an ancestor of the user's allowed companies (branch companies inherit parent providers); transactions only in allowed companies; tokens only the owner's own for internal, portal and public users, and company-limited; capture wizard only its creator (payment/security/payment_security.xml:6-43); (TEST) branch company compatibility (payment/tests/test_payment_provider.py:129-138); other users cannot read someone's tokens (payment/tests/test_payment_token.py:18-23).
- Multi-company: a new company automatically gets copies of installed providers of the creating user's company; installing a provider module creates a copy for each top-level company lacking one (payment/models/res_company.py:9-21; payment/models/payment_provider.py:969-987); (TEST) (payment/tests/test_res_company.py:9). Transaction company follows its provider (payment/models/payment_transaction.py:38-40). A customer may pay in another company than their own; the page flags a mismatch, and tokens from all companies stay visible to their owner (payment/controllers/portal.py:132-133, 465-478); (TEST) (payment/tests/test_multicompany_flows.py:41-130).
- Logging: provider request/response logging masks a set of sensitive keys; the engine's own list is empty and gateway modules extend it (payment/const.py:9; payment/logging.py:7-90). Each outbound provider request has a 10-second timeout and connection failures become a user-facing validation error (payment/models/payment_provider.py:790-813).

## D. Handoffs
- Accounting: payment does not create accounting entries. account_payment overrides post-processing to post invoices and create/reconcile payments; see its own note (account_payment/models/payment_transaction.py:98-211).
- Sales: sale overrides post-processing: pending -> quotation marked sent and payment-status email; authorised -> order confirmation after amount check; done -> confirmation and, when the system setting for automatic invoicing is on, invoicing and invoice sending (sale/models/payment_transaction.py:40-106, 135, 201-227).
- Website: website_payment and website_sale_collect extend post-processing; delivery also (website_payment/models/payment_transaction.py:13; delivery/models/payment_transaction.py:9). Their business effect: UNKNOWN — EVIDENCE INSUFFICIENT.
- Portal: pages inherit the customer portal controller and templates (payment/controllers/portal.py:16; payment/__manifest__.py:17-19). Logging on linked documents is left empty for other modules to implement (payment/models/payment_transaction.py:1180-1191).
- Gateway modules: Community includes 23 payment_* modules that depend on this engine; per-gateway behaviour is out of scope (reverse dependency list of the source map).

## E. Configuration/defaults that change outcomes
- Provider state (disabled by default; neutralisation resets enabled ones) and published flag; company; allowed countries, currencies, maximum amount; tokenisation; manual capture; express checkout (payment/models/payment_provider.py:41-52, 63-78, 107-134).
- Payment method support levels default to "none" for manual capture and refund; refund availability is the weaker of provider and method (payment/models/payment_method.py:72-93).
- Status messages shown to customers have translatable defaults per status (payment/models/payment_provider.py:140-157, 1040-1054).
- Finaliser retry window: unprocessed transactions are retried only for 4 days after last status change (payment/models/payment_transaction.py:1090-1096).
- Reference generation: custom prefix -> document-derived prefix -> time-based fallback, with a numeric suffix on duplicates (payment/models/payment_transaction.py:369-448).
- System setting "automatic invoicing" of sale drives invoice creation after payment (sale/models/payment_transaction.py:91-93).
- Validation (save-a-method) amount and currency are chosen by the provider; default is zero and the company currency when no intersection exists (payment/models/payment_provider.py:692-737).

## F. Effective extension path
- account_payment (invoice/payment accounting); sale (order confirmation and invoicing); website_payment, website_sale, website_sale_collect, delivery (website/checkout side); payment_custom (offline/manual providers); payment_demo (test provider); payment_stripe, payment_paypal, payment_adyen and other payment_* gateway modules; onboarding and portal (dependencies).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of each gateway module, webhook handling and signature checks (outside assigned scope).
- UNKNOWN — EVIDENCE INSUFFICIENT: express-checkout controller flow and the front-end scripts (templates and JS were listed but not traced).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether a non-system, non-accounting user can view transactions in a given deployment (ACL here is system only; extending modules add groups).
- UNKNOWN — EVIDENCE INSUFFICIENT: exact effect of currency-conversion date and rounding edge cases on maximum-amount filtering (only the call was read).
- Revision `19.0.post20260921`; findings apply to this revision only and are not universal rules.

