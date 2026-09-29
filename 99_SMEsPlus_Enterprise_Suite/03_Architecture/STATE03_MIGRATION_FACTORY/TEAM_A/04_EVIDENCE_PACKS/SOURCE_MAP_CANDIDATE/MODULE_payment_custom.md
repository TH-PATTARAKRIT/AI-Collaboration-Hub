# Source Map (candidate) — `payment_custom`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `payment_custom` |
| Display name | Payment Provider: Custom Payment Modes |
| Manifest version | 2.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `5a7f0b3d2ce6f1aa` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/payment_custom/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `payment`
- Direct dependents in 300-module list (1): `delivery`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `website_sale_collect`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Payment Providers / A payment provider for custom flows like wire transfers.
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `payment.provider`, `payment.transaction`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `payment.provider`, `payment.transaction`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 22 of 22 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: payment_custom
Source revision: 19.0.post20260921 | Path base: odoo/addons | Method: static source read (no execution)

## A. Capabilities
- Offline "custom" payment provider; only mode shipped is Wire Transfer (payment_custom/models/payment_provider.py:17-23). Depends only on payment (payment_custom/__manifest__.py:10). Not an application; no auto_install. Optional payment provider module, but hard dependency of delivery and website_sale_collect (delivery/__manifest__.py:13; website_sale_collect/__manifest__.py:10).
- Wire-transfer payment method (code wire_transfer), shipped inactive, no tokenization, no express checkout, no manual capture, no refund (payment_custom/data/payment_method_data.xml:4-14, noupdate).
- The pre-existing core provider record "Wire Transfer" (owned by payment) is completed by this module: code custom, mode wire_transfer, method attached (payment/data/payment_provider_data.xml:500-506; payment_custom/data/payment_provider_data.xml:4-15).
- On install the provider is set up, on uninstall it is reset (payment_custom/__init__.py:9-14).
- Customer flow: checkout posts to an internal public route which registers the payment data and redirects to the payment status page (payment_custom/controllers/main.py:13-20; payment_custom/models/payment_transaction.py:15-30). The transaction is set to pending; amount validation is skipped for this provider (payment_transaction.py:50-64). Pending state is never finalised automatically (payment_custom/static/src/interactions/post_processing.js:8 comment: custom transactions remain pending) - completion is a back-office reconciliation action outside this module (UNKNOWN — EVIDENCE INSUFFICIENT for exact confirm path).
- Payment instruction text: pending message is rebuilt to list bank accounts of company bank journals, only when account_payment is installed (payment_provider.py:45-62); manual "Reload Pending Message" button (views/payment_provider_views.xml:32-42). Conditional on account_payment.
- Payment reference shown to the payer: invoice payment reference, else sale order reference, else transaction reference (payment_transaction.py:32-48). (TEST) payment_custom/tests/test_payment_transaction.py:25, :32, :51.
- Optional QR code on the status page when "Enable QR Codes" is on and the company partner has a bank account (payment_provider.py:25-26; views/payment_custom_templates.xml:32-35). Conditional per provider.
- Chatter message on the transaction says the customer selected the provider (payment_transaction.py:74-86).

## B. Objects and lifecycle
- Extends payment.provider (adds code "custom", custom mode, QR flag) and payment.transaction (behaviour only; no new fields) (payment_provider.py:10-26; payment_transaction.py:12-13).
- Transaction lifecycle in this module: created -> pending (payment_transaction.py:56-64). Later states (done/cancel/error) belong to core payment, not set by this module.
- Provider states (enabled / test / disabled) are defined in core payment; not restated here (UNKNOWN — EVIDENCE INSUFFICIENT for state names from this module alone).

## C. Validations, security, multi-company
- Database check: custom mode may only be set on providers with code custom, and must be set for them (payment_provider.py:12-15, 23-24).
- Route is public without CSRF token, uses elevated access to process; only reference is read from the form (controllers/main.py:16-19; templates redirect_form: views/payment_custom_templates.xml:16-20). Business consequence: security relies on core payment reference handling (UNKNOWN — EVIDENCE INSUFFICIENT for how core validates the reference).
- No ACL, group or record-rule file in this module (manifest lines 11-17); access follows core payment provider rules.
- Multi-company: provider is per company (company_id read at payment_provider.py:50); bank accounts listed are those of that company's bank journals (lines 51-54).
- Provider form hides credentials, method list, messages for done/cancel/pre-payment and follow-up group for custom providers (views/payment_provider_views.xml:14-48).

## D. Handoffs (owner in brackets)
- Accounting [account_payment]: bank accounts for instructions, invoice link for reference (payment_provider.py:46-48; payment_transaction.py:44-45). Payment record creation from a confirmed transaction is owned by account_payment, not here (not evidenced in this module).
- Sales [sale]: on pending custom transaction the sale order reference is recomputed and quotation marked sent (sale/models/payment_transaction.py:40-58).
- Website/pickup [website_sale_collect]: adds mode "Pay on site" to custom_mode (website_sale_collect/models/payment_provider.py:12).
- Delivery [delivery]: depends on this module for cash-on-delivery style option (delivery/__manifest__.py:13; delivery/models/delivery_carrier.py:50 help text). Detailed link UNKNOWN — EVIDENCE INSUFFICIENT.
- Test-suite references to the core transfer provider in website_sale, website_event_sale, website_sale_loyalty, website_event_booth_exhibitor (TEST).

## E. Configuration that changes outcomes
- Provider enable state and company; QR code flag; pending message text (auto-rebuilt only if empty on data load: payment_provider.py:80-85; data/payment_provider_data.xml:17-19); payment method active flag (payment_method_data.xml:8).
- Presence of account_payment and sale modules changes the reference and instruction text.

## F. Effective extension path (module names only)
- payment.provider extended by: sale, website_sale_collect, sale_loyalty_delivery, account_payment. payment.transaction extended by: sale, website_sale_collect, account_payment. Direct dependents: delivery, website_sale_collect.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: how a pending wire transfer is marked paid (core payment and account_payment logic not traced).
- UNKNOWN — EVIDENCE INSUFFICIENT: interaction of the delivery module with this provider beyond the manifest dependency.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether additional custom modes exist beyond wire transfer and pay-on-site in Community.

