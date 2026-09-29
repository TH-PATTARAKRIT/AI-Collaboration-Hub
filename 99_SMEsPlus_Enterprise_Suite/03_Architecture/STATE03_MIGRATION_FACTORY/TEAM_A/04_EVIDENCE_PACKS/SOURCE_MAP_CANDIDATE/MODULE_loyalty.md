# Source Map (candidate) — `loyalty`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `loyalty` |
| Display name | Coupons & Loyalty |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `03537054d1786db6` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/loyalty/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `product`, `portal`, `account`
- Direct dependents in 300-module list (1): `sale_loyalty`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `pos_loyalty`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales / Use discounts, gift card, eWallets and loyalty programs in different sales channels
- Inventory of user-facing artifacts (counts): menu items 0, views 16, window actions 4, server actions 0, reports 2, mail templates 2, scheduled jobs 0, wizards 3, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (8): `loyalty.card.update.balance` (Update Loyalty Card Points); `loyalty.generate.wizard` (Generate Coupons); `loyalty.mail` (Loyalty Communication); `loyalty.history` (History for Loyalty cards and Ewallets); `loyalty.program` (Loyalty Program); `loyalty.card` (Loyalty Coupon); `loyalty.rule` (Loyalty Rule); `loyalty.reward` (Loyalty Reward)
- Objects extended from other modules (6): `base.partner.merge.automatic.wizard`, `product.pricelist`, `product.template`, `product.product`, `mail.thread`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `loyalty.mail` ← Community: `pos_loyalty`; open-license custom/third-party scanned: —
- `loyalty.history` ← Community: `sale_loyalty`; open-license custom/third-party scanned: —
- `loyalty.program` ← Community: `pos_loyalty`, `sale_loyalty`, `sale_loyalty_delivery`, `website_sale_loyalty`; open-license custom/third-party scanned: —
- `loyalty.card` ← Community: `pos_loyalty`, `sale_loyalty`, `website_sale_loyalty`; open-license custom/third-party scanned: —
- `loyalty.rule` ← Community: `pos_loyalty`, `website_sale_loyalty`; open-license custom/third-party scanned: —
- `loyalty.reward` ← Community: `pos_loyalty`, `sale_loyalty`, `sale_loyalty_delivery`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `base.partner.merge.automatic.wizard`, `product.pricelist`, `product.template`, `product.product`, `mail.thread`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 7 declarative constraint method(s), 6 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 5 (of which company-scoped by text 5); access rows 8

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

