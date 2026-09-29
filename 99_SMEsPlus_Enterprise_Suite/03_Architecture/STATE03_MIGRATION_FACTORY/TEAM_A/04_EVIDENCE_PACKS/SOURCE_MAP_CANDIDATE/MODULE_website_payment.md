# Source Map (candidate) — `website_payment`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_payment` |
| Display name | Website Payment |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `75697a98878a1df9` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_payment/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `website`, `account_payment`, `portal`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `website_sale`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Payment integration with website
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 3
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (4): `payment.provider`, `payment.transaction`, `account.payment`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `payment.provider`, `payment.transaction`, `account.payment`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 54 of 55 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_payment (Website Payment)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_payment.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: bridge that adds multi-website awareness to payment providers, plus a donation feature and a payment-methods snippet (website_payment/__manifest__.py:8-10; snippets/views listed at 16-24).

## A. Capabilities / functions
- Conditional bridge: depends on website, account_payment and portal, with `auto_install` (website_payment/__manifest__.py:11-15, 25). Present automatically wherever those three are installed; website_sale depends on it, so shop checkout relies on it (website_sale/__manifest__.py:11).
- Core: a provider can be restricted to one website; a provider without a website is usable on every website of its company (website_payment/models/payment_provider.py:15-20, 37-41). The field is shown on the provider form only in multi-website mode (website_payment/views/payment_provider.xml:11).
- Core: when providers are filtered out for a website mismatch, the availability report records "incompatible website" as the reason (website_payment/models/payment_provider.py:42-47; payment/const.py:547).
- Core: pay pages, saved-payment-method page and invoice page always pass the current website into provider selection (website_payment/controllers/payment.py:10-18; website_payment/controllers/portal.py:240-243). Checkout in the shop passes it too (website_sale/controllers/main.py:1573; website_sale/controllers/sale.py:9-24).
- Core: provider callback/base URL is taken from the actual request root so each website domain gets its own return links; falls back to the standard base URL outside a request (website_payment/models/payment_provider.py:50-58).
- Core: "Donation" feature: public page `/donation/pay`, donation button/snippet with preset amounts, descriptions, min/max, slider and free amount, with a transaction endpoint `/donation/transaction/<minimum>` (website_payment/controllers/portal.py:19-52, 54-102; website_payment/views/snippets/s_donation.xml:4-20).
- Core: "Supported payment methods" snippet fed by a public JSON route listing method names and images of providers published on the current website (website_payment/controllers/portal.py:174-237; website_payment/views/snippets/s_supported_payment_methods.xml:4).
- Core: donation confirmation email to the donor and an internal notification email to a configured recipient; chatter note on the payment recording donor details (website_payment/models/payment_transaction.py:13-59; website_payment/data/mail_templates.xml:4).
- Core: settings banner prompting to enable a provider for the website being configured, with onboarding shortcut (website_payment/views/res_config_settings_views.xml:9-73; website_payment/models/res_config_settings.py:12-33).

## B. Business objects, relationships, lifecycle
- Payment provider (owned by payment) -> optional website (restrict on delete) and company check (website_payment/models/payment_provider.py:15-20). Transaction (payment) gains a "donation" flag; accounting payment mirrors it (website_payment/models/payment_transaction.py:11; website_payment/models/account_payment.py:10).
- Donation lifecycle: donor opens form (amount stored in session, redirect) -> submits name/email/country (or uses own contact) -> transaction created with donation flag and recomputed access token -> internal notification email sent immediately -> provider flow -> on state "done" post-processing sends the donor confirmation and logs a note on the payment (website_payment/controllers/portal.py:32-52, 55-102; website_payment/models/payment_transaction.py:13-25).
- Transaction states and confirmation are owned by payment/account_payment (see account_payment note: payment created and reconciled on "done").
- Duplicating a provider inside a child company keeps the parent's website only when the source website's company is an ancestor of the copy's company (website_payment/models/payment_provider.py:60-66).

## C. Validations, automation, security, multi-company
- Donation amount must reach the configured minimum (from the snippet) or a validation error is raised (website_payment/controllers/portal.py:55-57). Anonymous or contact-less donors must give name, email and country (website_payment/controllers/portal.py:58-66). Server-side maximum amount: UNKNOWN — EVIDENCE INSUFFICIENT (a maximum exists in the snippet options, website_payment/views/snippets/s_donation.xml:14; not enforced in the transaction route).
- Public donors are recorded against the website's public user contact, with donor name/email/country/language stored on the transaction, and payment method is not saved (tokenisation off) (website_payment/controllers/portal.py:67, 75-87; website_payment/controllers/portal.py:155-172).
- Logged-in donors use their own contact, whatever contact id the request carries (website_payment/controllers/portal.py:69-70, 114-128). Payment page access for public users is protected by an amount-bound token generated server-side (website_payment/controllers/portal.py:48-50, 91-95).
- Unexpected request keys are rejected except a whitelist for donation extras (website_payment/controllers/portal.py:72-74; payment/controllers/portal.py:481-490).
- Minimum-amount route parameter is trusted from the URL (website_payment/controllers/portal.py:54-57, 140). The donation recipient email and comment come from the form (website_payment/controllers/portal.py:97-100): mail is sent to whatever recipient the form supplies. Abuse implications: UNKNOWN — EVIDENCE INSUFFICIENT.
- Donation emails are created and sent immediately with elevated rights, using the company email as sender (website_payment/models/payment_transaction.py:53-59); (TEST) internal notification email content/sender (website_payment/tests/test_mailing.py:10-29).
- Supported-method endpoint is public and cacheable for public/portal users (7 days plus stale reuse), no-cache for internal users; uses the website's company and a public-user context so editors see what customers see (website_payment/controllers/portal.py:196-237).
- Technical pages `/donation/pay` and `/payment/status` load correctly (TEST) (website_payment/tests/test_website_payment_technical_page.py:8-12). Donation UI tour needs payment_demo, else skipped (TEST) (website_payment/tests/test_snippets.py:8-14).
- No access-control rows or record rules in this module. Provider visibility per company/user follows payment's rules (payment/security/payment_security.xml).

## D. Handoffs to other modules
- payment (owner): providers, methods, tokens, transaction state machine, post-processing, portal payment pages, compatibility filtering (payment/models/payment_provider.py:555; payment/controllers/portal.py:40,194).
- account_payment (owner): invoice payment, payment creation/reconciliation on confirmation, portal invoice page (account_payment/controllers/payment.py:77; account_payment/controllers/portal.py:121).
- sale / website_sale: shop checkout and order payment call the provider filter with the website (website_sale/controllers/main.py:1562-1573; sale/controllers/portal.py:263). Payment reconciliation with sale orders is owned by sale.
- website: multi-website, snippets, layout, public user; portal: frontend layout; mail: donation emails.
- Provider modules (payment_*): actual gateways, out of scope here.

## E. Configuration / defaults that change outcomes
- Provider `website` blank = all websites of the company; set = only that website (website_payment/models/payment_provider.py:37-41).
- Donation defaults: currency = company currency, amount 25, free-amount mode (website_payment/controllers/portal.py:44-46); snippet defaults: presets 10/25/50/100, min 5, max 100, step 5, default 25, internal email placeholder (website_payment/views/snippets/s_donation.xml:7-16).
- Settings banner filters providers by company and website (website_payment/models/res_config_settings.py:20-26).
- Provider "published" flag decides website visibility of a provider (payment/models/payment_provider.py:47-52).

## F. Effective extension path (module names only)
- payment.provider: account_payment, delivery, sale, sale_loyalty_delivery, website_payment, website_sale_collect and the payment_* provider modules (adyen, aps, asiapay, authorize, buckaroo, custom, demo, dpo, ecpay, flutterwave, iyzico, mercado_pago, mollie, nuvei, paymob, paypal, payu, razorpay, redsys, stripe, toss_payments, worldline, xendit).
- payment.transaction: account_payment, delivery, pos_online_payment, pos_online_payment_self_order, sale, website_payment, website_sale_collect (plus provider modules).
- account.payment: account_payment, website_payment and localisation/other modules (account_check_printing, hr_expense, point_of_sale, pos_online_payment, l10n_*).
- Controllers extended: payment portal (website_payment), account_payment portal; website_sale controllers reuse the website parameter.

## G. Not verified
- Refund, capture and reconciliation of donations after confirmation (only the flag and notes are added here): UNKNOWN — EVIDENCE INSUFFICIENT.
- Fiscal/receipt treatment of donations (no invoice is created by this module): UNKNOWN — EVIDENCE INSUFFICIENT.
- Multi-company behaviour when a website's company differs from a provider's company beyond the compatibility filter: UNKNOWN — EVIDENCE INSUFFICIENT.

