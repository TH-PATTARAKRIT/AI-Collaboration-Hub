# Source Map (candidate) — `account_payment`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_payment` |
| Display name | Payment - Account |
| Manifest version | 2.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a390533acf333e62` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_payment/` |
| auto_install / application | ['account'] / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`, `payment`
- Direct dependents in 300-module list (3): `account_payment_interco`, `sale`, `website_payment`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `pos_online_payment`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / Enable customers to pay invoices on the portal and post payments when transactions are processed.
- Inventory of user-facing artifacts (counts): menu items 4, views 9, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 4, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `payment.refund.wizard` (Payment Refund Wizard)
- Objects extended from other modules (11): `payment.provider`, `account.move`, `payment.transaction`, `account.payment.method.line`, `account.journal`, `account.payment.method`, `account.payment`, `account.bank.statement.line`, `account.payment.register`, `res.config.settings`, `payment.link.wizard`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `payment.provider`, `account.move`, `payment.transaction`, `account.payment.method.line`, `account.journal`, `account.payment.method`, `account.payment`, `account.bank.statement.line`, `account.payment.register`, `res.config.settings`, `payment.link.wizard`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 0); access rows 3

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 83 of 84 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: account_payment (Payment - Account)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/account_payment.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: enables customers to pay invoices on the portal and posts payments when transactions are processed (account_payment/__manifest__.py:5).

## A. Capabilities / functions
- Connects the online-payment engine (module payment) to accounting: depends on account and payment (account_payment/__manifest__.py:7); `auto_install` is keyed to account (account_payment/__manifest__.py:8), so it is conditional/automatic rather than a manual option. Whether payment is pulled in by that rule: UNKNOWN — EVIDENCE INSUFFICIENT.
- Core: create an accounting payment from a confirmed online transaction and reconcile it with the linked invoices (account_payment/models/payment_transaction.py:98-131, 133-211).
- Core: portal "pay now" for customer invoices, including custom/partial amounts, installment and early-payment-discount awareness, and the invoice page payment form (account_payment/controllers/portal.py:14-51; account_payment/views/account_portal_templates.xml:287-323).
- Core: "overdue invoices" portal page and one-shot payment of all overdue invoices of the logged-in customer, requiring login and a single currency/partner/company (account_payment/controllers/portal.py:53-109; account_payment/controllers/payment.py:38-57).
- Core: payment links for invoices through the payment link wizard, using portal URL, an amount-bound access token and the pay anchor (account_payment/wizards/payment_link_wizard.py:75-110); shows a warning when online payment is disabled (account_payment/wizards/payment_link_wizard.py:29-33). QR code image of the portal payment link is available for documents (account_payment/models/account_move.py:171-182).
- Core: pay with a saved token when registering/creating a payment in the back office, which triggers an offline charge (account_payment/models/account_payment.py:124-151, 183-222; account_payment/wizards/account_payment_register.py:73-77).
- Core: refunds of electronic payments via a refund wizard, partial or full according to provider and method capability (account_payment/wizards/payment_refund_wizard.py:38-84; account_payment/models/account_payment.py:49-70).
- Core: capture or void authorized transactions from the invoice; the normal Register Payment buttons are hidden while authorized transactions exist (account_payment/models/account_move.py:110-123; account_payment/views/account_move_views.xml:12-29).
- Core: providers own a payment journal and matching inbound payment-method line (account_payment/models/payment_provider.py:10-19, 23-75).
- Optional feature toggle: "Invoice Online Payment" setting stored as system parameter, default on at install (account_payment/data/ir_config_parameter.xml:4-7; account_payment/wizards/res_config_settings.py:9; account_payment/wizards/res_config_settings_views.xml:9-11).
- Back-office menus for providers, methods (all), tokens and transactions (debug-only for the last two) under the accounting Payment menu (account_payment/views/account_payment_menus.xml:4-21).

## B. Business objects, relationships, lifecycle
- Transaction (payment.transaction, owned by payment) <-> Invoices (many-to-many); transaction -> Payment (one-to-one tracking) (account_payment/models/payment_transaction.py:9-16; account_payment/models/account_move.py:16-19). Payment -> Transaction, saved token, source payment for refunds (account_payment/models/account_payment.py:11-21, 36-44).
- Payment method line (journal-level) -> Provider; provider -> Journal (bank type) (account_payment/models/account_payment_method_line.py:10-16; account_payment/models/payment_provider.py:10-19).
- Transaction states are defined by payment: draft, pending, authorized, done, cancel, error; operations include online redirect/direct/token, validation, offline, refund (payment/models/payment_transaction.py:65-89).
- Handoff on confirmation (state done): draft invoices are posted, a missing inbound/outbound payment is created and posted, invoice receivable lines are reconciled, and a chatter message links transaction and payment (account_payment/models/payment_transaction.py:106-129, 191-209).
- No payment for validation-type transactions, nor for source transactions whose child transactions (partial capture/void) are done or cancelled (account_payment/models/payment_transaction.py:116-120); (TEST) (account_payment/tests/test_account_payment.py:195,203).
- Cancelled transaction cancels its linked payment (account_payment/models/payment_transaction.py:130-131). Back-office token payment: posted immediately when tx done, left pending/authorized when the provider is asynchronous, cancelled otherwise (account_payment/models/account_payment.py:140-149); (TEST) pending stays in process (account_payment/tests/test_account_payment.py:148).
- Payment direction follows transaction amount sign (negative = outbound) (account_payment/models/payment_transaction.py:151-152).
- Early-payment-discount: when the transaction covers the discounted amount due, discount write-off lines are added to the payment (account_payment/models/payment_transaction.py:167-185).
- Invoice payable online only if: feature enabled; posted; customer invoice (`out_invoice`); payment state not paid/reversed (not_paid, in_payment, partial); non-zero residual and total; no pending or authorized provider transaction (excluding "none"/"custom" providers) (account_payment/models/account_move.py:55-74). Human-readable reasons in account_payment/models/account_move.py:76-103.
- Refund availability: original amount minus confirmed refund payments, only if provider and method support refunds and the payment was created by a non-refund transaction (account_payment/models/account_payment.py:49-70); (TEST) (account_payment/tests/test_account_payment.py:16-112).

## C. Validations, automation, security, multi-company
- Refund amount must be > 0 and <= available amount (account_payment/wizards/payment_refund_wizard.py:38-45). Refund support = weakest of provider and method (none < full-only < partial) (account_payment/wizards/payment_refund_wizard.py:58-70). Pending refunds are flagged (account_payment/wizards/payment_refund_wizard.py:72-80).
- One transaction per payment; a token is mandatory to create a transaction from a payment (account_payment/models/account_payment.py:183-191).
- Method line linked to an enabled/test provider cannot be deleted (account_payment/models/account_payment_method_line.py:63-74); a journal used by a non-disabled provider cannot be deleted (account_payment/models/account_journal.py:16-25); available inbound method lines exclude those whose provider is disabled (account_payment/models/account_journal.py:11-14); (TEST) (account_payment/tests/test_account_payment.py:230).
- Provider module uninstall is blocked if payments already use its method (account_payment/models/payment_provider.py:135-147); payment-method records are created for installed providers at install and removed at uninstall (account_payment/__init__.py:11-22).
- Bank reconciliation: payments coming from a provider transaction or ISO 20022/SEPA credit-transfer methods cannot be partially matched with statement lines (account_payment/models/account_bank_statement_line.py:9-15); (TEST) (account_payment/tests/test_account_payment.py:490).
- Portal security: invoice route requires a valid document access token (else "access token is invalid") (account_payment/controllers/payment.py:26-31); payment-link amount is protected by an access token bound to partner/amount/currency (account_payment/controllers/payment.py:97-100; account_payment/controllers/portal.py:173-175); unexpected request keys are rejected (TEST: account_payment/tests/test_payment_flows.py:96). Cancelled invoice forces amount zero (account_payment/controllers/payment.py:141-143). Company mismatch between paying partner and invoice company is flagged on the portal page (account_payment/controllers/portal.py:139-147).
- ACL: accounting invoicing group (`account.group_account_invoice`) gets read/write/create (no delete) on payment link wizard, refund wizard and payment transactions (account_payment/security/ir.model.access.csv:2-4). Same group can read every payment token (record rule resets the owner-only rule) (account_payment/security/ir_rules.xml:4-12). Capture/void/refund buttons and the transactions stat button are limited to that group (account_payment/views/account_move_views.xml:21,25,32; account_payment/views/account_payment_views.xml:14).
- Multi-company: provider journal is company-checked (account_payment/models/payment_provider.py:16); payment is created in the provider's company, with the transaction's company context (account_payment/models/payment_transaction.py:121,157); token search filtered by company domain (account_payment/models/account_payment.py:76-81); owner rules for provider/transaction/token company scoping live in payment (payment/security/payment_security.xml:6-34). Child-company provider duplicate-journal behaviour: (TEST) exists (account_payment/tests/test_payment_provider.py:11) but conclusion not extracted: UNKNOWN — EVIDENCE INSUFFICIENT.
- Elevated access: transaction creation from a payment and portal reads run with elevated rights (account_payment/models/account_payment.py:131-133; account_payment/controllers/portal.py:121-137).

## D. Handoffs to other modules
- payment (owner): providers, methods, tokens, transaction state machine, post-processing entry point, capture/refund actions; this module overrides `_post_process`, reference prefix (invoice names), logging targets (account_payment/models/payment_transaction.py:68-95, 98, 215-242).
- account (owner): invoices, payments, payment method lines, registration wizard, bank statement reconciliation, portal invoices and overdue domain (account/controllers/portal.py:59-66). Journal/posting entries are generated by account when the payment is posted.
- Audit trail: chatter messages on payment, source payment and invoices for confirmed and refund events (account_payment/models/payment_transaction.py:123-129, 231-238).
- Sales (sale): reuses the invoice payability check and payment-link defaults for orders (sale/models/sale_order.py; sale/controllers/portal.py mentions `_has_to_be_paid`). Its depth is outside this note.
- Inventory, e-invoicing and approval: none in this module. No e-invoicing handoff here; the e-invoicing module is account_edi_ubl_cii (see its note).

## E. Configuration / defaults that change outcomes
- System parameter `account_payment.enable_portal_payment`: default True on install (`forcecreate=0`, noupdate) (account_payment/data/ir_config_parameter.xml:2-7); when off, invoices are not payable online and link wizard warns.
- Provider fields: payment journal (required unless disabled or code none/custom) and refund support level (debug group) (account_payment/views/payment_provider_views.xml:14-19). Default journal on provider enable/test: first bank journal of the company (account_payment/models/payment_provider.py:98-107).
- Manual capture on a provider excludes its tokens from back-office payments (account_payment/models/account_payment.py:78; account_payment/wizards/account_payment_register.py:45).
- Electronic method info is registered for every provider except none/custom (account_payment/models/account_payment_method.py:10-20). Outstanding account defaults from chart-template refs, falling back to the company transfer account (account_payment/models/payment_provider.py:77-86).
- Method lines auto-assign an unused provider of the same company/code (account_payment/models/account_payment_method_line.py:28-61).

## F. Effective extension path (module names only; grep of `_inherit` across addons root)
- account.payment: account_check_printing, hr_expense, l10n_account_withholding_tax, l10n_ar_withholding, l10n_au, l10n_ch, l10n_in, l10n_latam_check, l10n_nz, l10n_ph, l10n_pl_bank_verification, point_of_sale, pos_online_payment, website_payment.
- payment.transaction: delivery, sale, pos_online_payment, pos_online_payment_self_order, website_payment, website_sale_collect, plus the payment_* provider modules (adyen, aps, asiapay, authorize, buckaroo, custom, demo, dpo, ecpay, flutterwave, iyzico, mercado_pago, mollie, nuvei, paymob, paypal, payu, razorpay, redsys, stripe, toss_payments, worldline, xendit).
- payment.provider: delivery, sale, sale_loyalty_delivery, website_payment, website_sale_collect and the same payment_* provider modules.
- account.payment.method.line: l10n_it_edi. account.payment.method: account_check_printing, l10n_latam_check. payment.link.wizard: sale. account.payment.register: hr_expense, l10n_account_withholding_tax, l10n_ar_withholding, l10n_latam_check, l10n_pl_bank_verification.
- Modules depending on account_payment (manifest): sale, website_payment, pos_online_payment, account_payment_interco.

## G. Not verified
- Full portal browser flow (JS interactions under account_payment/static/src/interactions) not analysed: UNKNOWN — EVIDENCE INSUFFICIENT.
- Exact treatment of vendor bills/credit notes by online payment (transaction invoice domain allows in/out invoice and refund types, account_payment/models/payment_transaction.py:15, but `_has_to_be_paid` admits only customer invoices): net effect for other types UNKNOWN — EVIDENCE INSUFFICIENT.
- Provider-specific behaviour, sale-order linkage, POS online payment: UNKNOWN — EVIDENCE INSUFFICIENT.
- No rule above is asserted as universal; each depends on installed providers, settings and journals.

