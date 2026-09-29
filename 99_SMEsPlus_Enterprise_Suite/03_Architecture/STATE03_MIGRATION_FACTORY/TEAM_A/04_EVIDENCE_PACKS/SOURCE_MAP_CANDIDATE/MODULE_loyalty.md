# Source Map (candidate) — `loyalty`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

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
- Core/optional/conditional behavior and business meaning of each capability: see section 10

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
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 60 of 60 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — loyalty (Coupons & Loyalty) (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities; core / optional / conditional
- Defines the shared data model for discounts, coupons, gift cards, eWallets, loyalty-point cards, promo codes, buy-X-get-Y and next-order coupons (loyalty/__manifest__.py:5; loyalty/models/loyalty_program.py:95-108).
- Depends on product, portal, account; not auto_install; no menus are defined here (loyalty/__manifest__.py:8; menus found only in sale_loyalty/views/sale_loyalty_menus.xml:4-14).
- This module does NOT apply anything to orders or prices itself; order-side application is owned by sale_loyalty (depends sale, loyalty — sale_loyalty/__manifest__.py:9) and point-of-sale side by pos_loyalty (pos_loyalty/__manifest__.py:10).
- Program templates offered in the UI: gift card, eWallet (gift/eWallet menu) versus promotion, promo code, buy X get Y, next order coupon, loyalty card, coupon, fidelity card (loyalty/models/loyalty_program.py:522-577).
- Portal page for customers to see loyalty/eWallet cards and point history (loyalty/controllers/portal.py:12-84).
- Optional visibility flags: portal_visible per program (loyalty/models/loyalty_program.py:145-151); pricelist restriction field shown only with pricelist group (loyalty/views/loyalty_program_views.xml:112).

## B. Business objects, relationships, lifecycle
- Program (loyalty.program) owns Rules (conditions that earn points), Rewards (what points buy) and Communication plans (mails) (loyalty/models/loyalty_program.py:54-79).
- Card/Coupon (loyalty.card) belongs to one program, optional customer, holds points, unique code, optional expiry; History lines record issued/used points against an order reference (loyalty/models/loyalty_card.py:28-52; loyalty/models/loyalty_history.py:11-20).
- Rule: earns points per order, per money spent, or per unit; can restrict by products, category, tag or domain; minimum quantity and minimum amount (tax incl/excl); automatic or by code (loyalty/models/loyalty_rule.py:48-87, :139-151).
- Reward: either free product or discount; discount as percent, fixed per order, or per point; applies to whole order, cheapest product or specific products; optional maximum amount; points required (loyalty/models/loyalty_reward.py:63-131).
- Program types set default behaviour (when points usable: current order / future orders / both; trigger: automatic or with code). Defaults per type e.g. promotion auto+current, gift card future+auto, loyalty both, promo code with_code (loyalty/models/loyalty_program.py:119-134, :283-439).
- Changing program type resets rules/rewards/communications to the type's defaults (loyalty/models/loyalty_program.py:441-449).
- Lifecycle: active/archived flag; archiving propagates to rules, rewards, communications and reward discount products (loyalty/models/loyalty_program.py:513-518). Active programs cannot be deleted (loyalty/models/loyalty_program.py:487-490). Program type becomes read-only once cards exist (loyalty/views/loyalty_program_views.xml:47).
- Unarchive is blocked when an active code duplicates another active rule code (loyalty/models/loyalty_rule.py:101-112) (TEST: loyalty/tests/test_loyalty.py:320-341).
- Card creation sends the "At Creation" mail; crossing a points threshold sends the highest reached "When Reaching" mail (loyalty/models/loyalty_card.py:133-190, :192-205).
- Manual balance change requires description, new balance must differ and be non-negative, writes a history line (loyalty/wizard/loyalty_card_update_balance.py:20-39).
- Bulk coupon generation for anonymous or selected customers (by partner or tag), writes history with issued points (loyalty/wizard/loyalty_generate_wizard.py:15-95).
- Order-side lifecycle (owned by sale_loyalty): points and history added on order confirmation, reversed on cancellation, "current" program coupons without claimed reward removed at confirmation (sale_loyalty/models/sale_order.py:140-207).

## C. Validations, automation, security, multi-company
- Program: max usage must be positive when limit on (loyalty/models/loyalty_program.py:177-180); currency must equal pricelists' currency (:182-191); start date not after end date (:193-198); at least one reward (skippable by context flag) (:200-205).
- Reward: required points >0, discount >0 for discount type, product qty >0 for product type (loyalty/models/loyalty_reward.py:135-146); reward product cannot be combo type (:288-291). Each reward auto-creates its own service-type, non-sellable discount product (:293-340).
- Rule: points per rule >0 (loyalty/models/loyalty_rule.py:89-92); split per unit not allowed for eWallet or "both" programs (:94-99); active code must be unique among rules and must not equal a card code (:101-117); card code must not equal a rule code (loyalty/models/loyalty_card.py:60-64); card code unique (:55-58).
- Card expiry cannot be set on a loyalty card type in the form (onchange) (loyalty/models/loyalty_card.py:71-75).
- Pricelist used by an active program cannot be archived (loyalty/models/product_pricelist.py:8-19) (TEST: loyalty/tests/test_loyalty.py:182). Product used by an active reward cannot be archived (loyalty/models/product_product.py:10-21). Seeded gift card / eWallet products cannot be deleted (loyalty/models/product_product.py:23-34; loyalty/models/product_template.py:23-34).
- Partner merge: nominative cards of merged partners are combined, points summed, extra cards zeroed and archived (loyalty/wizard/base_partner_merge.py:12-45) (TEST: loyalty/tests/test_loyalty.py:246).
- Access: base loyalty grants NO rights to internal users (all four permissions 0) (loyalty/security/ir.model.access.csv:2-9); actual rights come from sale_loyalty (salesperson read; sales manager full on program/rule/reward/mail; salesperson read/write on cards) (sale_loyalty/security/ir.model.access.csv:2-11).
- Multi-company: record rules on program, card, history, rule, reward use company in allowed companies, unset, or parent of allowed companies (loyalty/security/loyalty_security.xml:4-32). Program default company = current company; currency follows company (loyalty/models/loyalty_program.py:30-41, :239-242). Order-side domain includes the order company and its parent (sale_loyalty/models/sale_order.py:665-675).
- Portal: customer sees only cards linked to own partner, active loyalty/eWallet programs, not expired (loyalty/controllers/portal.py:12-28, :49-56).

## D. Handoffs (module ownership)
- Order lines, reward lines, discount computation, points on confirm/cancel: sale_loyalty (sale_loyalty/models/sale_order.py:140-207, :536, :945). Program validity domain on order: active, company, pricelist, date window (sale_loyalty/models/sale_order.py:665-688).
- Point of sale: pos_loyalty (pos_loyalty/models/loyalty_program.py:9). Invoice line linkage: sale_loyalty/models/account_move_line.py:7 and pos_loyalty/models/account_move_line.py:7 (accounting detail UNKNOWN — EVIDENCE INSUFFICIENT).
- Discount lines use per-reward service products (product module) (loyalty/models/loyalty_reward.py:333-340); tax/account behaviour of those products: UNKNOWN — EVIDENCE INSUFFICIENT.
- Emails through mail templates for model loyalty.card (loyalty/models/loyalty_mail.py:25-31; loyalty/data/mail_template_data.xml).

## E. Configuration/defaults that change outcomes
- System parameter loyalty.compute_all_discount_product_ids is seeded as False on install; code treats value 'enabled' as "precompute all discounted products" and any other value as domain-only (loyalty/data/loyalty_data.xml:22-25; loyalty/models/loyalty_reward.py:194-207).
- Program-type defaults (points, minimum amount 50, discount 10, 15% next-order, 5 for 200 points, min qty 2 for buy-X-get-Y) (loyalty/models/loyalty_program.py:289-438).
- Trigger (auto vs code), applies_on, portal visibility, point name (eWallet/gift card show currency symbol) (loyalty/models/loyalty_program.py:135-158, :451-456); several fields visible only in debug group (loyalty/views/loyalty_program_views.xml:113-120).
- Minimum amount tax mode default "tax included" (loyalty/models/loyalty_rule.py:68-75). Gift card/eWallet programs seeded (gift card program, product priced 50) (loyalty/data/loyalty_data.xml:5-52).
- Discount amounts can be capped (discount_max_amount) (loyalty/models/loyalty_reward.py:100-103).

## F. Extension path (grep of _inherit)
- Extended by sale_loyalty (loyalty.card, .reward, .program, .history; sale.order, sale.order.line, account.move.line) and pos_loyalty (loyalty.mail, .card, .program, .rule, .reward; pos.order, pos.order.line, pos.config, pos.session, res.partner, product.*, barcode.rule). loyalty itself extends product.pricelist, product.product, product.template, res.partner, base.partner.merge.automatic.wizard.

## G. Not verified
- Exact discount computation on orders (discountable amount, best global discount, tax handling): UNKNOWN — EVIDENCE INSUFFICIENT (only sale_loyalty entry points sampled, not traced).
- eCommerce (website_sale_loyalty) and other consumers: UNKNOWN — EVIDENCE INSUFFICIENT.
- Report/PDF template content (loyalty/report): UNKNOWN — EVIDENCE INSUFFICIENT.

