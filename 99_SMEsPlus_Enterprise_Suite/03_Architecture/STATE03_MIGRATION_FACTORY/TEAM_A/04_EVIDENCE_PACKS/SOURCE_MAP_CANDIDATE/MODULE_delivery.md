# Source Map (candidate) — `delivery`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `delivery` |
| Display name | Delivery Costs |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `60f39ec19a8a8ac3` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/delivery/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale`, `payment_custom`
- Direct dependents in 300-module list (3): `sale_gelato`, `sale_loyalty_delivery`, `stock_delivery`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `website_sale`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Delivery / —
- Inventory of user-facing artifacts (counts): menu items 1, views 12, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (4): `choose.delivery.carrier` (Delivery Carrier Selection Wizard); `delivery.price.rule` (Delivery Price Rules); `delivery.zip.prefix` (Delivery Zip Prefix); `delivery.carrier` (Shipping Methods)
- Objects extended from other modules (8): `payment.provider`, `ir.module.module`, `payment.transaction`, `ir.http`, `product.category`, `sale.order`, `sale.order.line`, `res.partner`
- Company-dependent settings introduced: 1 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `choose.delivery.carrier` ← Community: `delivery_mondialrelay`, `stock_delivery`; open-license custom/third-party scanned: —
- `delivery.carrier` ← Community: `delivery_mondialrelay`, `l10n_ro_edi_stock`, `sale_gelato`, `stock_delivery`, `website_sale`, `website_sale_collect`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `payment.provider`, `ir.module.module`, `payment.transaction`, `ir.http`, `product.category`, `sale.order`, `sale.order.line`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 3 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 1); access rows 10

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 65 of 69 source pointers resolve to an existing file and in-range line (4 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — delivery
Source revision: 19.0.post20260921 | Module: "Delivery Costs" (delivery/__manifest__.py:4) | depends: sale, payment_custom (:13) | License LGPL-3 (:46)
Basis: static reading of all 10 model files, wizard, controller, security, seed data, key views; 5 test files read (availability, cost, COD provider/transaction, pickup address). Not auto_install (no such key) — optional module, installed explicitly (e.g. from Sales settings shipping option). delivery/wizard/res_config_settings_views.xml:9-19 (the shipping-methods link appears in Sales settings when the option module_delivery is on)

## A. Capabilities and optionality
- A1. Core: define shipping methods (carriers) with a price mechanism, let a salesperson attach one to a quotation through a chooser, and add a "shipping" line to the order at the quoted cost. delivery/models/delivery_carrier.py:13-16,42-47; delivery/wizard/choose_delivery_carrier.py:7-96; delivery/models/sale_order.py:54-72,203-242
- A2. Two built-in price mechanisms: "Fixed Price" (default) and "Based on Rules". Other providers (real-time carriers) plug in by adding their own type and rate/ship/track/cancel methods; those are separate modules. delivery/models/delivery_carrier.py:20-32,42-47,321-322
- A3. Optional per carrier: availability restrictions (countries, states, zip prefixes, maximum weight, maximum volume, must-have tags, excluded tags), margins, "free if order above amount", description shown to customer, tracking link template, insurance percentage, return-label flags (used only by provider modules), cash-on-delivery permission. delivery/models/delivery_carrier.py:48-110
- A4. Conditional feature: Cash on Delivery payment (provider seeded enabled, method code cash_on_delivery) usable only when the chosen carrier allows it; installing sets the provider up and uninstalling resets it. delivery/data/payment_provider_data.xml:4-21; delivery/__init__.py:8-13; delivery/models/payment_provider.py:26-51 (TEST: tests/test_payment_provider.py:11-32)
- A5. Conditional: pickup-point delivery for provider types that support locations: order stores chosen pickup point; two authenticated endpoints set/list pickup locations. delivery/models/sale_order.py:74-125; delivery/controllers/location_selector.py:8-37
- A6. Seed data: product category "Deliveries" (protected from deletion), service product "Standard delivery" (not sellable/purchasable as normal item, invoice on order), and a free fixed carrier "Standard delivery". delivery/data/delivery_data.xml:4-23; delivery/models/product_category.py:10-14
- A7. Neutralisation script (copies of databases): all carrier "production environment" flags off and carriers of external provider types archived. delivery/data/neutralize.sql:1-6

## B. Business objects, relationships, lifecycle
- B1. Carrier (delivery.carrier, owner delivery) points to one delivery product (required, cannot be deleted while used); company is taken from that product (stored, editable). delivery/models/delivery_carrier.py:55-56
- B2. Price rule (delivery.price.rule) belongs to a carrier: condition on weight, volume, weight x volume, order price or quantity with an operator and threshold, priced as base price + unit price x chosen variable; ordered by sequence then price. delivery/models/delivery_price_rule.py:16-53
- B3. Zip prefix (delivery.zip.prefix): unique, always stored upper-case, used by carriers as regular-expression prefixes. delivery/models/delivery_zip_prefix.py:8-30
- B4. Order (sale.order, owner sale) gains: delivery method, "delivery set" flag (any delivery line), "recompute delivery price" flag, all-service flag, shipping weight, pickup data, delivery message. delivery/models/sale_order.py:12-18,37-40
- B5. Order line gains "is delivery" mark; delivery lines cannot be invoiced alone, get no pricelist item, are excluded from pricelist price updates, and may be deleted even on a confirmed order. delivery/models/sale_order_line.py:9,15-16,45-62; delivery/models/sale_order.py:49-52
- B6. Partner gets a per-company default delivery method and a "pickup location" flag; pickup addresses are excluded from delivery-address defaults. delivery/models/res_partner.py:10-14 (TEST: tests/test_sale_order.py:9-13)
- B7. Lifecycle on the order: (1) "Add a shipping method" appears when the order has lines, is not all services and has no delivery line; (2) wizard proposes carriers, quotes a price; (3) confirmation writes/replaces the delivery line and stores the delivery message; (4) any change to lines, customer or shipping address flags the delivery cost for recomputation (line highlighted, "Update shipping cost" button); (5) recompute re-opens the wizard on the current carrier. delivery/views/sale_order_views.xml:13-34; delivery/models/sale_order.py:42-47,127-153; delivery/wizard/choose_delivery_carrier.py:91-96
- B8. Replacing shipping: existing delivery lines are removed first, but if any has already been invoiced the change is refused with a message listing them. delivery/models/sale_order.py:54-72
- B9. Removing the delivery line clears the order's carrier. delivery/models/sale_order_line.py:28-30
- B10. Default carrier proposal: the customer's shipping partner (else its commercial partner) default method is proposed only if active and available for the order (TEST: tests/test_delivery_availability.py:198-245 - restricted, unset and archived carriers are not proposed).
- B11. Delivery line content: product, quantity 1, customer-language description (carrier name plus product sale description), price as quoted, taxes of the delivery product mapped by fiscal position and filtered to the order company; "Free Shipping" appended when the free-over rule gives zero. delivery/models/sale_order.py:203-238
- B12. Pickup point on confirmation: a delivery-type child address (flagged pickup) is reused or created under the shipping partner and becomes the order's shipping address. delivery/models/sale_order.py:155-201
- B13. Cash on delivery: a pending COD transaction confirms a draft order and sends the confirmation email. delivery/models/payment_transaction.py:9-18 (TEST: tests/test_payment_transaction.py:12-28 order state becomes sale)

## C. Validations, security, multi-company
- C1. Constraints: margin cannot be below -100% (stored as fraction >= -1); insurance between 0 and 100; a tag cannot be both must-have and excluded; zip prefix unique. delivery/models/delivery_carrier.py:112-125; delivery/models/delivery_zip_prefix.py:27-30
- C2. Availability test = address (country, state, zip prefix pattern) AND tags AND max weight AND max volume (0 means no limit); for rule-based carriers also requires that a price can be computed. delivery/models/delivery_carrier.py:168-257 (TEST: tests/test_delivery_availability.py:31-196 heavy/big products in different units, tag combinations)
- C3. Rule-based pricing: first matching rule wins; none matching gives "Not available for current order"; services and combo header products, cancelled lines and delivery lines are ignored in totals. delivery/models/delivery_carrier.py:451-476,489-502 (TEST: tests/test_delivery_cost.py:593-640 combo quantities counted through components, result 25 for 5 combos + 5 units)
- C4. Access on carriers: salespersons and system read only; sales managers full; partner managers read. Price rules: salespersons read, sales managers full. Zip prefixes: salespersons read, partner managers full (row id says sale manager but group is partner manager). Chooser wizard: salespersons read/write/create. delivery/security/ir.model.access.csv:2-11
- C5. Record rule: carriers visible when company is among the user's companies or empty. delivery/security/ir_rules.xml:4-8
- C6. Multi-company: carrier on order has company check; wizard offers only carriers valid for the order company; rule-based carriers without a company convert amounts from the main company's currency (TEST: tests/test_delivery_cost.py:522-591); partner default carrier is company-dependent. delivery/models/sale_order.py:13; delivery/wizard/choose_delivery_carrier.py:65; delivery/models/delivery_carrier.py:437-449; delivery/models/res_partner.py:10
- C7. Rate computation and delivery-line creation run with elevated rights (sudo). delivery/models/delivery_carrier.py:453-454; delivery/models/sale_order.py:242
- C8. Pickup endpoints: authenticated internal/portal users; they operate on the order as the caller (no explicit ownership check in module). delivery/controllers/location_selector.py:8,19. Ownership enforcement: UNKNOWN — EVIDENCE INSUFFICIENT (record rules of sale).

## D. Handoffs
- D1. Quotation, confirmation, invoicing of the shipping line, taxes, fiscal position: sale / account (line is a normal order line, product invoice policy "order" in seed). delivery/data/delivery_data.xml:15; delivery/models/sale_order.py:203-238
- D2. Picking creation, shipment booking, tracking numbers, real-cost invoicing: stock_delivery (extends carrier and chooser) and provider modules. This module's only invoicing policy is "Estimated cost". delivery/models/delivery_carrier.py:60-66
- D3. Payment collection: payment / payment_custom (provider); confirmation of COD order is delivered here. delivery/models/payment_transaction.py:9-18
- D4. Analytic/accounting posting: none in module; follows the shipping product's income account and analytic rules of sale/account. (none found in module)
- D5. Weight and volume data: product (units read from system parameters). delivery/models/delivery_carrier.py:127-131

## E. Configuration/defaults that change outcomes
- E1. Carrier price mechanism default "Fixed Price"; fixed price is the delivery product's list price (two-way link). delivery/models/delivery_carrier.py:42-47,385-394
- E2. Fixed price is taken from the order pricelist for the delivery product when one exists (TEST: tests/test_delivery_cost.py:140-177 pricelist price 5 used), and margins are ignored for fixed carriers (TEST: tests/test_delivery_cost.py:331-353). delivery/models/delivery_carrier.py:295-300,403
- E3. Rate pipeline: raw rate -> converted to tax-included per fiscal position -> margin (percent + fixed) -> rounded -> free-over override to zero (not for rule-based). delivery/models/delivery_carrier.py:321-348 (TEST: tests/test_delivery_cost.py:219-272 line total 10.45 / subtotal 9.09 same as adding product manually)
- E4. "Free if order above" threshold default 1000 in company currency, compares the order total without delivery. delivery/models/delivery_carrier.py:90-95,339-347
- E5. Shipping weight order: weight typed in chooser, else stored order weight, else sum of lines; the stored weight counts only storable/consumable ("consu") lines with positive quantity and updates when quantities change (TEST: tests/test_delivery_cost.py:274-293,473-520). delivery/models/sale_order.py:244-254; delivery/models/delivery_carrier.py:471-475
- E6. Order-level flag decides whether "Add/Update shipping" buttons show; all-service orders hide them. delivery/views/sale_order_views.xml:18,25,31
- E7. Zero-weight physical lines can be flagged (helper) for warnings. delivery/models/sale_order_line.py:36-43 (TEST: tests/test_delivery_cost.py:295-329)

## F. Effective extension path (grep of _inherit)
- F1. This module extends: sale.order, sale.order.line, res.partner, payment.provider, payment.transaction, product.category, ir.http, ir.module.module; defines delivery.carrier, delivery.price.rule, delivery.zip.prefix, choose.delivery.carrier. delivery/models/*.py; delivery/wizard/choose_delivery_carrier.py:8
- F2. Modules extending delivery.carrier: delivery_mondialrelay, l10n_ro_edi_stock, sale_gelato, stock_delivery, website_sale, website_sale_collect. Modules extending the chooser: delivery_mondialrelay, stock_delivery.
- F3. Modules depending on delivery: sale_gelato, sale_loyalty_delivery, stock_delivery, website_sale (reverse dependency index).

## G. Not verified
- G1. UNKNOWN — EVIDENCE INSUFFICIENT: shipment creation, tracking and real-cost invoicing (owned by stock_delivery/provider modules, not read).
- G2. UNKNOWN — EVIDENCE INSUFFICIENT: website checkout behaviour of carrier choice (website_sale, not read).
- G3. UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of return-label and insurance fields (only computed as false in this module). delivery/models/delivery_carrier.py:133-141
- G4. UNKNOWN — EVIDENCE INSUFFICIENT: how a draft order is prevented or allowed to confirm without a delivery method (no such gate found in this module).

