# Source Map (candidate) — `sale_loyalty`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_loyalty` |
| Display name | Sale Loyalty |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `284a427b610067ba` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_loyalty/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale`, `loyalty`
- Direct dependents in 300-module list (1): `sale_loyalty_delivery`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `website_sale_loyalty`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Use discounts and loyalty programs in sales orders
- Inventory of user-facing artifacts (counts): menu items 2, views 6, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `sale.loyalty.reward.wizard` (Sale Loyalty - Reward Selection Wizard); `sale.loyalty.coupon.wizard` (Sale Loyalty - Apply Coupon Wizard); `sale.order.coupon.points` (Sale Order Coupon Points - Keeps track of how a sale order impacts a coupon)
- Objects extended from other modules (7): `loyalty.history`, `sale.order`, `account.move.line`, `sale.order.line`, `loyalty.program`, `loyalty.card`, `loyalty.reward`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `loyalty.history`, `sale.order`, `account.move.line`, `sale.order.line`, `loyalty.program`, `loyalty.card`, `loyalty.reward`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 17

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 62 of 62 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_loyalty
Source revision: 19.0.post20260921 | Module: "Sale Loyalty" (sale_loyalty/__manifest__.py:4) | depends: sale, loyalty (:9) | License LGPL-3 (:33)
Basis: static reading of all model and wizard files (sale_order.py read end to end), security, data, menus; test names for 12 test files listed and ~10 tests read. Program/rule/reward master definitions live in loyalty (only sampled).

## A. Capabilities and optionality
- A1. Applies loyalty and promotion programs to quotations/sales orders: automatic promotions, promo codes, coupons, gift cards, eWallets, loyalty cards, buy-X-get-Y and next-order coupons (program types owned by loyalty). loyalty/models/loyalty_program.py:95-104; sale_loyalty/models/sale_order.py:1045-1230,1411-1533
- A2. Conditional: bridge module, installed automatically when sale and loyalty are present. sale_loyalty/__manifest__.py:10
- A3. Programs have a "Sales" flag (default on) deciding whether they are usable on sales orders at all. sale_loyalty/models/loyalty_program.py:10; sale_loyalty/models/sale_order.py:665-688
- A4. Entry points: "enter a code" wizard, "claim reward" wizard (or auto-apply when exactly one single-product reward is claimable), and a gift-card smart button on the order. sale_loyalty/wizard/sale_loyalty_coupon_wizard.py:15-30; sale_loyalty/wizard/sale_loyalty_reward_wizard.py:41-69; sale_loyalty/models/sale_order.py:209-232
- A5. Menus for discount/loyalty and gift-card/eWallet program setup, shown to sales managers only. sale_loyalty/views/sale_loyalty_menus.xml:4-13
- A6. Uninstall removes loyalty history rows that point to sales orders. sale_loyalty/__init__.py:6-8

## B. Business objects, relationships, lifecycle
- B1. Order (sale.order, owner sale) gains: manually applied coupons, manually triggered code rules, per-coupon point entries (new model sale.order.coupon.points, unique per order+coupon), reward total, gift-card count, loyalty summary. sale_loyalty/models/sale_order.py:24-37; sale_loyalty/models/sale_order_coupon_points.py:7-17
- B2. Order line gains: reward, coupon, points cost, a reward identifier grouping lines of the same reward, and a computed "is reward line". sale_loyalty/models/sale_order_line.py:9-19,30-33
- B3. Card (loyalty.card, owner loyalty) gains the source order; use count includes order lines; archiving a card deletes its draft-order point entries. sale_loyalty/models/loyalty_card.py:9-17,44-54 (TEST: tests/test_loyalty.py:1229)
- B4. Recalculation engine: on every relevant change the order (1) loads nominative wallets/cards of the customer, (2) collects applied and automatic programs, (3) refreshes points, creating or deleting order-linked coupons, (4) recomputes existing reward lines, (5) applies new automatic programs and deletes stale lines. sale_loyalty/models/sale_order.py:1045-1230
- B5. Points per rule: rule may give points per order, per unit or per money spent (rounded down to 2 decimals, based on price incl. tax after discounts); gift cards can split into several codes when the split option is on; rules need minimum amount (with or without tax) and minimum quantity of eligible products. sale_loyalty/models/sale_order.py:1238-1365
- B6. Reward lines: product rewards become the product at 100% discount with quantity multiplied by claimable count; discount rewards become a negative line (split per tax group, or a single line for gift card/eWallet) limited by max discount amount, points available and order total; point cost is recorded once per reward. sale_loyalty/models/sale_order.py:254-278,536-660
- B7. Global discounts: only one global discount is kept; the better one for the customer wins; when both exceed the total, the smaller one is kept. sale_loyalty/models/sale_order.py:871-925,945-968
- B8. Confirmation: refuses if any coupon would go negative; refreshes rewards; writes loyalty history per coupon (points issued, points used); deletes order-scoped coupons that claimed no reward; adds/subtracts coupon points; then confirms and emails coupons generated for future orders; if rewards remain unclaimed and a single order, shows a notice. sale_loyalty/models/sale_order.py:140-183 (TEST: tests/test_loyalty_history.py:46-64,131-153)
- B9. Cancellation: deletes the order's history rows, reverses point changes for previously confirmed orders, removes reward lines, deletes unused order-generated coupons and point entries. sale_loyalty/models/sale_order.py:185-207 (TEST: tests/test_loyalty.py:132-192 cancel works for a salesperson; tests/test_loyalty_history.py:83-101)
- B10. Editing after confirmation: changing a reward line's cost or coupon adjusts card points and history by the difference. sale_loyalty/models/sale_order_line.py:82-113 (TEST: tests/test_loyalty_history.py:154-179)
- B11. Duplicating an order drops reward lines. sale_loyalty/models/sale_order.py:133-138
- B12. Deleting a reward line also deletes its sibling lines (same reward/coupon/code), gives points back on confirmed orders, detaches manually applied coupons, and removes order-generated current-order coupons. sale_loyalty/models/sale_order_line.py:115-140 (TEST: tests/test_unlink_reward.py:35-71)
- B13. Program date validity uses the company timezone (else a system parameter, default UTC) and, once payment is confirmed, the date of the earliest done/authorized transaction. sale_loyalty/models/sale_order.py:690-712
- B14. Price refresh (pricelist recompute) re-runs program logic when reward lines exist. sale_loyalty/models/sale_order.py:761-766

## C. Validations, security, multi-company
- C1. Codes: unknown, expired, used-up or inactive codes are rejected; loyalty/eWallet programs cannot be applied by code; a promo code already applied is refused; program row is locked while applying to prevent concurrent overuse. sale_loyalty/models/sale_order.py:1455-1520
- C2. Usage limit: programs with a maximum are skipped when total orders reached (order count includes sales orders here). sale_loyalty/models/loyalty_program.py:9-26; sale_loyalty/models/sale_order.py:1087-1089
- C3. Program applicability filter: active, "Sales" flag on, company equals order company or its parent, pricelist restriction, date window. sale_loyalty/models/sale_order.py:665-688 (TEST: tests/test_program_multi_company.py:40-137 company-specific programs do not apply to other companies; branch behaviour tested)
- C4. Pricelist-restricted programs: tests confirm both promotion and coupon programs respect pricelists. (TEST) tests/test_loyalty.py:714-840
- C5. Points from an order's coupons owned by a different customer are dropped; public-user coupons are re-assigned to the real customer once known. sale_loyalty/models/sale_order.py:1103-1112
- C6. Reward deletion: a single reward already used on order lines is archived instead of deleted. sale_loyalty/models/loyalty_reward.py:19-22
- C7. Order-line reward fields are read-only in the UI and reward lines cannot be edited on the customer portal or invoiced alone. sale_loyalty/models/sale_order_line.py:13-15,55-56,147-148
- C8. Access: salespersons read programs/rules/rewards, read+write cards and history, use wizards; sales managers full on programs/rules/rewards/communications and point entries; salespeople read point entries. sale_loyalty/security/ir.model.access.csv:2-18
- C9. Elevated rights are used for coupon creation/deletion and point writes on behalf of salespeople. sale_loyalty/models/sale_order.py:200-203,801-818,840,1200-1230
- C10. Multi-company: see C3; card mail author falls back to the order's company; program currency follows program company. sale_loyalty/models/loyalty_card.py:28-33; loyalty/models/loyalty_program.py:239-242. Cross-company coupon redemption on a card issued by another company: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs (which module owns what)
- D1. Program/rule/reward/card definitions, expiry, generation wizards, mail templates, loyalty history model: loyalty. Order lines, taxes, fiscal position, pricelists, invoicing: sale / account.
- D2. Discount product: created by loyalty, this module forces no taxes and invoice policy "order", so reward lines are invoiceable immediately even when the product line is invoiced on delivery. sale_loyalty/models/loyalty_reward.py:9-17 (TEST: tests/test_sale_invoicing.py:29-73)
- D3. Gift card / eWallet default products are stripped of taxes at install; gift card redemption takes the gift-card product taxes into account. sale_loyalty/data/sale_loyalty_data.xml:4-9; sale_loyalty/models/sale_order.py:610-635 (TEST: tests/test_pay_with_gift_card.py:151-255)
- D4. Zero-total orders with a reward: if sale automatic invoicing is on, the order is invoiced and the invoice posted automatically and, if ready, sent; done from order validation. sale_loyalty/models/sale_order.py:1534-1566 (TEST: tests/test_sale_auto_invoice.py:12-98)
- D5. Discount lines are recognised on invoices for downstream reporting (accounting side treats them as discount lines). sale_loyalty/models/account_move_line.py:9-14; sale_loyalty/models/sale_order_line.py:58-59
- D6. Delivery interplay (free shipping rewards): sale_loyalty_delivery (F2). Point-of-sale and website use: pos_loyalty, website_sale_loyalty. Analytic handoff: none in module.

## E. Configuration/defaults that change outcomes
- E1. Program design fields (program type, applies on current/future/both, trigger auto/with code, limit usage, pricelist, dates) drive behaviour; changing them changes B4-B8. loyalty/models/loyalty_program.py:95-141
- E2. Nominative programs (eWallet or loyalty applying on future orders, or applying on both) auto-load the customer's cards holding points. sale_loyalty/models/sale_order.py:1054-1065; loyalty/models/loyalty_program.py:251-255
- E3. Discount mode (percent, per order, per point), max discount, discount applicability (order, cheapest, specific) shape reward amounts. sale_loyalty/models/sale_order.py:536-604
- E4. System parameter for loyalty timezone (default UTC) and sale automatic invoicing parameter. sale_loyalty/models/sale_order.py:696; sale_loyalty/models/sale_order.py:1540
- E5. Rewards are not partially granted: points are floored to a multiple of the reward cost (except payment programs). sale_loyalty/models/sale_order.py:594-597

## F. Effective extension path (grep of _inherit)
- F1. This module extends: sale.order, sale.order.line, loyalty.card, loyalty.history, loyalty.program, loyalty.reward, account.move.line; defines sale.order.coupon.points, sale.loyalty.coupon.wizard, sale.loyalty.reward.wizard. sale_loyalty/models/*.py; sale_loyalty/wizard/*.py
- F2. Modules depending on sale_loyalty: sale_loyalty_delivery, website_sale_loyalty. Modules extending loyalty.program/card/reward (grep): pos_loyalty, sale_loyalty_delivery, website_sale_loyalty.

## G. Not verified
- G1. UNKNOWN — EVIDENCE INSUFFICIENT: loyalty-module internals (card generation, expiry rules, communication scheduling); only referenced here.
- G2. UNKNOWN — EVIDENCE INSUFFICIENT: portal/website checkout behaviour of codes (website_sale_loyalty not read).
- G3. UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of the discountable-amount calculation for orders mixing fixed taxes and multiple tax groups beyond the tests named (sale_loyalty/models/sale_order.py:282-535 only skimmed).
- G4. UNKNOWN — EVIDENCE INSUFFICIENT: behaviour when points cost is edited on a cancelled or draft order (only confirmed-state logic read).

