# Source Map (candidate) — `event_booth_sale`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `event_booth_sale` |
| Display name | Events Booths Sales |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `6e999c2196b915db` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/event_booth_sale/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `event_booth`, `event_sale`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `website_event_booth_sale`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Events / Manage event booths sale
- Inventory of user-facing artifacts (counts): menu items 0, views 13, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `event.booth.configurator` (Event Booth Configurator); `event.booth.registration` (Event Booth Registration)
- Objects extended from other modules (8): `account.move`, `sale.order`, `sale.order.line`, `product.template`, `product.product`, `event.booth.category`, `event.type.booth`, `event.booth`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `event.booth.registration` ← Community: `website_event_booth_sale_exhibitor`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `account.move`, `sale.order`, `sale.order.line`, `product.template`, `product.product`, `event.booth.category`, `event.type.booth`, `event.booth`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 5 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 41 of 41 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: event_booth_sale
Revision 19.0.post20260921 | Bridge: Event Booths (event_booth) <-> Event Sales (event_sale) | booth reservation via sales orders

## A. Capabilities (core / optional / conditional)
- Sells event booths on sales orders and tracks payment on the order ("Sell your event booths and track payments on sale orders") (event_booth_sale/__manifest__.py:8-10). Depends on event_booth and event_sale (:12).
- Auto-install: yes (event_booth_sale/__manifest__.py:24). No settings toggle.
- Adds a product tracking choice "Event Booth" (event_booth_sale/models/product_template.py:8-10); it cannot be used by generic tracking lists (:22-23); selecting it forces invoicing on order (models/product_template.py:17-20; models/product_product.py:8-11); tooltip: marks the selected booth as unavailable (models/product_template.py:12-15).
- Every booth category now has a required sale product (default: a shared "Event Booth" service product), plus price, tax-included price, reduced price and image inherited from the product (event_booth_sale/models/event_booth_category.py:16-37,50-86; data/product_data.xml:4-13). Standard/Premium/VIP categories are priced 100 / 500 / 1000 by this module's data (event_booth_sale/data/event_booth_category_data.xml:4-17).
- Event templates' booth lines expose product and price from the category (event_booth_sale/models/event_type_booth.py:10-17).
- Event-booth products are hidden from the order product catalog (event_booth_sale/models/sale_order.py:41-42). Order shows a booth count and a booth-list action (models/sale_order.py:11-22,36-39).

## B. Business objects and lifecycle
- Booth registration (new object): a reservation request linking one booth to one sale order line, with contact name/email/phone defaulting from the order customer; unique per booth per line (event_booth_sale/models/event_booth_registration.py:12-26,28-44). Several customers can request the same booth at once (docstring :9-10).
- Sale order line gains booth category, "pending booths" (selection that creates/removes registrations), confirmed registrations, confirmed booths (event_booth_sale/models/sale_order_line.py:12-43).
- Booth gains registrations, reservation lines, final sale order line/order, and a paid flag (event_booth_sale/models/event_booth.py:12-25).
- Order confirmation: every booth line must have at least one pending booth, else confirmation is blocked; then booths on each line are confirmed if still available, otherwise the whole confirmation is blocked listing unavailable booths (event_booth_sale/models/sale_order.py:24-34; models/sale_order_line.py:75-86). Confirming a registration marks the booth unavailable and stores sale line, partner and contacts (models/event_booth_registration.py:46-56; base owner event_booth). (TEST) prices with orders: event_booth_sale/tests/test_event_booth_sale.py:49; registrations: :121.
- First confirmed order wins: all other orders holding registrations on those booths are cancelled, with a note to the order and a notification to its salesperson, and their registrations deleted (event_booth_sale/models/event_booth_registration.py:57-74).
- Payment: when an invoice linked to the order is paid, its booths are flagged paid (event_booth_sale/models/account_move.py:10-16; models/sale_order_line.py:84-85; booth "set paid" action models/event_booth.py:35-36). (TEST) event_booth_sale/tests/test_event_booth_sale.py:168.

## C. Validations, automation, security
- All registrations of one order line must be for a single event (event_booth_sale/models/sale_order_line.py:50-53).
- Changing product clears the event if product isn't among pending booths' products; changing event clears pending booths (event_booth_sale/models/sale_order_line.py:55-65).
- Booths linked to a sales order cannot be deleted (event_booth_sale/models/event_booth.py:27-33).
- Booth category product must be tracked as Event Booth; a product used by a booth category cannot change its tracking (event_booth_sale/models/event_booth_category.py:39-48; models/product_product.py:13-25; models/product_template.py:25-43).
- Configurator wizard requires at least one booth (event_booth_sale/wizard/event_booth_configurator.py:31-34); booth and category selection reset when event/category changes (:23-29).
- Access: salespeople full rights on booth registrations and create/edit on configurator; event registration desk read-only; event users full (event_booth_sale/security/ir.model.access.csv:2-5). Sale-side fields on booths restricted to salespeople group (event_booth_sale/models/event_booth.py:17,21,24). Product/price on booth category visible to registration-desk group (models/event_booth_category.py:22,25,28).
- Company scoping: price uses event company currency (event_booth_sale/models/sale_order_line.py:101,108); explicit record rules: UNKNOWN — EVIDENCE INSUFFICIENT (none in this module's security data).

## D. Handoffs
- event_booth owns booths, categories, availability and confirmation state; event_sale owns event/order-line link and tracking mechanics; sale owns orders, invoices; account owns invoice paid hook; product owns tracking option.

## E. Configuration that changes outcomes
- Line price: sum of booths' category prices — reduced prices (contextual discount) when the pricelist does not display discounts, otherwise plain category prices; converted into the order currency (event_booth_sale/models/sale_order_line.py:99-109; category reduce logic models/event_booth_category.py:73-78).
- Category price defaults from product list price plus extra but is editable by event staff (event_booth_sale/models/event_booth_category.py:55-61).
- Booth is reserved at order confirmation, "paid" at invoice payment (two-stage) (event_booth_sale/models/sale_order.py:33; models/account_move.py:15).
- On install, existing categories get the shared booth product (event_booth_sale/models/event_booth_category.py:88-125).

## F. Effective extension path
- event_booth, event_sale, sale, account (module names only).

## G. Not verified
- Behaviour on order refusal/cancel for confirmed booths (release of booths): UNKNOWN — EVIDENCE INSUFFICIENT in this module.
- Website booth-selling flow: UNKNOWN — EVIDENCE INSUFFICIENT.

