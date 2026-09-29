# Source Map (candidate) — `payment`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

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
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

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
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

