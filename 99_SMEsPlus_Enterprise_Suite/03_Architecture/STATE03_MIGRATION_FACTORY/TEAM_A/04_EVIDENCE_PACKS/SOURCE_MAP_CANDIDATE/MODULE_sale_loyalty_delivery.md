# Source Map (candidate) — `sale_loyalty_delivery`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_loyalty_delivery` |
| Display name | Sale Loyalty - Delivery |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `75cf6cdcab930dcd` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_loyalty_delivery/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_loyalty`, `delivery`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Adds free shipping mechanism in sales orders
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (4): `payment.provider`, `sale.order`, `loyalty.program`, `loyalty.reward`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `payment.provider`, `sale.order`, `loyalty.program`, `loyalty.reward`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 25 of 25 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_loyalty_delivery
Source revision: 19.0.post20260921 | Module: "Sale Loyalty - Delivery" (sale_loyalty_delivery/__manifest__.py:4) | depends: sale_loyalty, delivery (:11) | auto_install true (:12) | LGPL-3 (:14)
Basis: static reading of all models, controller, view; test names read (two test files, ~730 lines), a few tests opened.

## A. Capabilities and optionality
- A1. Adds a "Free Shipping" reward type to promotion/loyalty programs (optionally capped at a maximum amount). sale_loyalty_delivery/models/loyalty_reward.py:9-11; sale_loyalty_delivery/views/loyalty_reward_views.xml:10-12
- A2. Default loyalty program gets a free-shipping reward at 100 points; the "promotion" template is re-described and re-built as free shipping. sale_loyalty_delivery/models/loyalty_program.py:9-35
- A3. Delivery lines and free-shipping reward lines are excluded from thresholds and from earning points; gift cards and eWallets are excluded from "amount without delivery". sale_loyalty_delivery/models/sale_order.py:11-30
- A4. Gift card / eWallet orders cannot be paid with pay-on-delivery providers. sale_loyalty_delivery/models/payment_provider.py:9-27; sale_loyalty_delivery/controllers/payment.py:9-19
- A5. Automatic bridge when sales loyalty and delivery are installed. sale_loyalty_delivery/__manifest__.py:11-12

## B. Objects, relationships, lifecycle
- B1. Reward description: "Free shipping", plus "(Max amount)" when a cap is set (currency symbol placed per currency). sale_loyalty_delivery/models/loyalty_reward.py:13-23
- B2. Reward line generated on the order: a discount line equal to minus the delivery line price (or the cap if smaller), one unit, cost in points either required points or full wallet when "clear wallet", taxes copied from the delivery product mapped by fiscal position, sequenced after normal lines. sale_loyalty_delivery/models/sale_order.py:32-57
- B3. Only one free-shipping reward can be active on an order; if one already exists, other claimable rewards remain but shipping-type ones are removed from the offer. sale_loyalty_delivery/models/sale_order.py:59-69. (TEST) other reward claimable from the same coupon: sale_loyalty_delivery/tests/test_free_shipping_reward.py:447
- B4. Lifecycle (TEST): reward appears only when the delivery method has been added and the program conditions hold; shipping does not count toward the minimum amount; the reward disappears again when the rule stops being met (e.g., quantity reduced below the threshold). sale_loyalty_delivery/tests/test_free_shipping_reward.py:58-132,355-446
- B5. (TEST) Percentage discounts ignore delivery lines; eWallet is excluded from delivery pricing; gift card paid orders keep delivery cost consistent. sale_loyalty_delivery/tests/test_loyalty_delivery.py:61-249
- B6. (TEST) Nothing delivered -> nothing to invoice with reward lines present. sale_loyalty_delivery/tests/test_free_shipping_reward.py:316

## C. Validations, security, multi-company
- C1. Payment start is refused with a message when the chosen provider is cash-on-delivery-type and the order holds gift-card/eWallet coupons; the same providers are hidden from the compatible list with an explanatory reason. sale_loyalty_delivery/controllers/payment.py:12-18; sale_loyalty_delivery/models/payment_provider.py:16-26
- C2. Reward ondelete rule: removing the module sets shipping rewards back to the default type. sale_loyalty_delivery/models/loyalty_reward.py:11
- C3. No new groups, ACLs, or record rules. Company: taxes filtered by order company. sale_loyalty_delivery/models/sale_order.py:34-35
- C4. The payment controller extends the e-commerce payment controller although the manifest does not list e-commerce as a dependency. sale_loyalty_delivery/controllers/payment.py:6; sale_loyalty_delivery/__manifest__.py:11. UNKNOWN — EVIDENCE INSUFFICIENT on behaviour when e-commerce is not installed.

## D. Handoffs
- D1. Discount accounting: the reward line is a normal negative order line invoiced as part of the order (owner sale/account); reward product configured on the reward. sale_loyalty_delivery/models/sale_order.py:42
- D2. Delivery line and carrier pricing: delivery. Points, coupons, eligibility: loyalty/sale_loyalty. Payment provider filtering: payment (custom-mode providers).
- D3. No inventory or purchase logic.

## E. Configuration that changes outcomes
- E1. Reward: maximum discount amount, required points, "clear wallet". sale_loyalty_delivery/views/loyalty_reward_views.xml:11; sale_loyalty_delivery/models/sale_order.py:36,41
- E2. Program rules (trigger auto/with code, minimum amount and tax mode). (TEST) test_free_shipping_reward.py:58-75,398-415
- E3. Fiscal position and delivery product taxes. sale_loyalty_delivery/models/sale_order.py:34-35

## F. Effective extension path (modules)
- Depended on by: none (grep of manifests). Overrides hooks of sale_loyalty (_get_reward_line_values, _get_no_effect_on_threshold_lines), delivery, loyalty, payment.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: interaction of free shipping with multiple carriers changed after reward application; behaviour of the point-of-sale channel.

