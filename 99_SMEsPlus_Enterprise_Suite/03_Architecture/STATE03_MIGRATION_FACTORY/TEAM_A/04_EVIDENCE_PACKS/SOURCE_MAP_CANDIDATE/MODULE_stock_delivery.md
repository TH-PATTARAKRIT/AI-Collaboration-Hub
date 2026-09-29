# Source Map (candidate) — `stock_delivery`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `stock_delivery` |
| Display name | Delivery - Stock |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `ce43bcacdcd000d9` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/stock_delivery/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_stock`, `delivery`
- Direct dependents in 300-module list (1): `delivery_stock_picking_batch`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `delivery_mondialrelay`, `l10n_it_stock_ddt`, `l10n_ro_edi_stock`, `website_sale_stock`
- Custom / third-party modules that declare a dependency (name — license only) (1): `d_tiktok_shop_connector` — OPL-1

## 3. Capabilities / functions
- Manifest category / summary: Shipping Connectors / —
- Inventory of user-facing artifacts (counts): menu items 2, views 16, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 3, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (13): `stock.return.picking`, `choose.delivery.carrier`, `stock.put.in.pack`, `stock.package`, `sale.order`, `sale.order.line`, `product.template`, `stock.route`, `stock.move`, `stock.move.line`, `stock.picking`, `stock.package.type`, `delivery.carrier`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.return.picking`, `choose.delivery.carrier`, `stock.put.in.pack`, `stock.package`, `sale.order`, `sale.order.line`, `product.template`, `stock.route`, `stock.move`, `stock.move.line`, `stock.picking`, `stock.package.type`, `delivery.carrier`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 7

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 57 of 57 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: stock_delivery
Source revision: 19.0.post20260921 (Odoo 19 Community). Read-only trace; neutral business language; no code copied.

## A. Capabilities / activation
- Connects shipping methods (owned by delivery) to warehouse transfers: carrier and shipping cost on the transfer, tracking reference/link, weight, package weight, shipping labels via carrier integrations, real-cost shipping written back to the sales order, carrier propagation across multi-step deliveries. stock_delivery/__manifest__.py:5-13; stock_delivery/models/stock_picking.py:21-32
- Conditional bridge: auto-installs when sale_stock and delivery are both present. stock_delivery/__manifest__.py:14,33
- On installation, if e-commerce is not installed, it installs the Sales app (sale_management) if that is still uninstalled. stock_delivery/__init__.py:6-16; stock_delivery/__manifest__.py:36
- Optional sub-features: label generation is a per-operation-type switch ("Generate Shipping Labels", default on for outgoing types only); carrier propagation is a per-stock-rule switch; "Real cost" invoicing is a per-carrier policy option. stock/models/stock_picking.py:61-63,338-345; stock/models/stock_rule.py:100-102; stock_delivery/models/delivery_carrier.py:19-25
- Adds product fields for customs: HS code and country of origin. stock_delivery/models/product_template.py:9-18
- Adds a "shipping selectable" flag on routes and a routes list on carriers so a carrier can force routes on sale lines. stock_delivery/models/stock_move.py:8-11; stock_delivery/models/delivery_carrier.py:27-29; stock_delivery/models/sale_order.py:52-56

## B. Business objects, relationships, lifecycle
- Transfer (stock.picking) gains: carrier (company-checked, limited to allowed carriers), shipping cost, tracking ref (not copied), tracking URL (computed), weight (stored, excludes cancelled moves), return-flag and return labels, destination country, integration level. stock_delivery/models/stock_picking.py:21-32,67-70
- Allowed carriers = carriers of the transfer's company that match the customer address and product/weight/volume/tag criteria; without customer, all company carriers. stock_delivery/models/stock_picking.py:34-38; delivery/models/delivery_carrier.py:179-185
- Package types gain a carrier code and carrier type; packages compute weight and expose weight unit; the "put in pack" wizard computes shipping weight (package base weight + contents + inner packages), warns when above the package type maximum. stock_delivery/models/stock_package_type.py:9-10; stock_delivery/models/stock_package.py:9-33; stock_delivery/wizard/stock_put_in_pack.py:16-47
- Packing lines with different carriers, or without carrier, cannot go in the same package (error). stock_delivery/models/stock_move.py:119-122
- Sales order side: choosing/setting a carrier on a confirmed order applies it to all not-yet-done, non-return transfers of that order. stock_delivery/models/sale_order.py:9-19
- With "Real cost" policy, the delivery line on the order is created at price 0 with an "estimated" label, then updated after shipment with the carrier's real price (created if missing; writing that price is allowed through a context flag on the protected fields). stock_delivery/models/sale_order.py:21-37,58-62; stock_delivery/models/stock_picking.py:169-191
- Test coverage: real-cost update including back orders (each back order adds its own delivery line). stock_delivery/tests/test_delivery_cost.py:30-83 (TEST)
- Validation flow (outgoing with carrier at "rate and ship" level and label option on): confirmation email step sends the shipment to the carrier and stores tracking/price; then compliance hook (empty by default) is checked. stock_delivery/models/stock_picking.py:94-123,160-163
- If the carrier call fails after another transfer in the same batch was already processed, the error becomes a chatter note plus a warning activity for the responsible user instead of an exception; otherwise it raises. stock_delivery/models/stock_picking.py:96-121
- "Free over" logic: if the order amount (excluding delivery) reaches the threshold, the real price recorded is 0. stock_delivery/models/stock_picking.py:125-132
- Tracking reference is spread over the whole chain of related transfers (upstream and downstream); comma-appended if already set. stock_delivery/models/stock_picking.py:133-148
- Carrier propagation: at creation of next-step transfers the carrier (taken from previous transfer, else from the single sale order carrier) and tracking ref are copied if the rule has propagation on; after validating a transfer, next transfers lacking a carrier receive it. stock_delivery/models/stock_move.py:41-55; stock_delivery/models/stock_picking.py:72-85; (TEST) stock_delivery/tests/test_carrier_propagation.py:58-147,300-330 (TEST)
- Transfers are also split by carrier when moves are assigned to pickings (carrier of the order is part of the grouping key). stock_delivery/models/stock_move.py:57-59
- Return transfers created through the return wizard have carrier and carrier price cleared ("no integration of returns"). stock_delivery/wizard/stock_return_picking.py:9-23
- Return-label capability: only when carrier supports it and the transfer's moves return to an internal location. stock_delivery/models/stock_picking.py:45-58,165-167
- Cancel shipment: calls carrier cancel, posts note, clears tracking ref. stock_delivery/models/stock_picking.py:218-223
- Weight-based rules: move weight = product weight x quantity (0 if product weight not positive); a data-migration step populates the column for large databases without recomputation. stock_delivery/models/stock_move.py:17-39
- Sale price per move line for customs documents (tax-included, based on delivered quantity). stock_delivery/models/stock_move.py:65-87
- Aggregated shipping-document lines carry HS code. stock_delivery/models/stock_move.py:89-101
- Commercial invoice needed when warehouse country differs from customer country. stock_delivery/models/stock_picking.py:232-234
- Wizard "choose delivery carrier" shows message that shipping price is set after delivery for real cost. stock_delivery/wizard/choose_delivery_carrier.py:9-13
- No state machine of its own; transfer states owned by stock. (see stock)

## C. Validations / constraints / security / multi-company
- Error if total package weight is zero when building packages from an order; weight/volume/tag filters via available-carrier match. stock_delivery/models/delivery_carrier.py:118-120
- Error when trying to open tracking page with no tracking link. stock_delivery/models/stock_picking.py:193-196
- Access (csv): carrier read for inventory users, full rights for inventory managers; zip-prefix and price-rule tables the same; choose-carrier wizard read/write/create for inventory users. stock_delivery/security/ir.model.access.csv:2-8
- Company scoping: carriers visible for the user's companies plus company-less carriers (rule in delivery). delivery/security/ir_rules.xml:4-7
- Carrier call is made with elevated rights. stock_delivery/models/stock_picking.py:105
- The transfer's carrier field is company-checked. stock_delivery/models/stock_picking.py:24

## D. Handoffs (owner in brackets)
- Sales delivery line, pricing, invoicing policy on carrier [delivery, sale]. stock_delivery/models/sale_order.py:21-37
- Carrier provider APIs (rate, ship, label, cancel, tracking) are dispatched by delivery type to methods defined by provider modules; Community core provides only "fixed" and "based on rules" types. stock_delivery/models/delivery_carrier.py:35-52,248-283
- Batch/wave grouping by carrier and weight [delivery_stock_picking_batch]. delivery_stock_picking_batch/models/stock_picking.py:31-59
- Return processing [stock return wizard]. stock_delivery/wizard/stock_return_picking.py:9-14
- Sales invoice creation and revenue posting [sale/account]; stock_delivery only writes the delivery-line price. stock_delivery/models/stock_picking.py:183-191
- No stock valuation handoff.

## E. Configuration that changes outcomes
- Carrier: delivery type, integration level ("get rate" vs "get rate and create shipment"), invoicing policy (estimated / real cost), free-over amount, max weight/volume, tag criteria, routes. delivery/models/delivery_carrier.py:42-63,90; stock_delivery/models/delivery_carrier.py:19-29
- Operation type: label generation. stock/models/stock_picking.py:61-63
- Stock rule: propagate carrier. stock/models/stock_rule.py:100-102
- System weight unit parameter drives weight labels. stock_delivery/models/stock_picking.py:14-19
- Product weight, HS code, country of origin. stock_delivery/models/product_template.py:9-18

## F. Effective extension path (Community modules extending the same objects; names only)
- delivery.carrier: delivery_mondialrelay, l10n_ro_edi_stock, sale_gelato, stock_delivery, website_sale, website_sale_collect.
- stock.picking: delivery_stock_picking_batch, sale_stock, stock_account, stock_dropshipping, stock_picking_batch, plus others.
- stock.move / stock.move.line: mrp, mrp_repair, repair, sale_stock, stock_account, stock_picking_batch, stock_delivery and others.
- stock.package / stock.package.type / stock.put.in.pack: only stock_delivery among Community modules searched.
- choose.delivery.carrier: delivery_mondialrelay, stock_delivery. stock.return.picking: mrp_subcontracting, purchase_stock, sale_stock, stock_delivery.

## G. Not verified
- Behaviour of real external carrier connectors (not in Community): UNKNOWN — EVIDENCE INSUFFICIENT
- Rate/ship behaviour for "fixed" and "based on rules" beyond stubs (cancel not implemented for these two types): UNKNOWN — EVIDENCE INSUFFICIENT (stock_delivery/models/delivery_carrier.py:260-261,282-283 show cancel is not implemented)
- Tax and currency treatment of the real-cost line beyond the margin/currency helper calls: UNKNOWN — EVIDENCE INSUFFICIENT
- Portal access to return labels/tracking: UNKNOWN — EVIDENCE INSUFFICIENT
- Behaviour when the carrier differs between sale order and later picking edits beyond the tests listed: UNKNOWN — EVIDENCE INSUFFICIENT

