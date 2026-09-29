# Source Map (candidate) — `stock_dropshipping`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `stock_dropshipping` |
| Display name | Drop Shipping |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d1e27f890e45301e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/stock_dropshipping/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_purchase_stock`
- Direct dependents in 300-module list (1): `mrp_subcontracting_dropshipping`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / Drop Shipping
- Inventory of user-facing artifacts (counts): menu items 1, views 4, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (11): `stock.replenish.mixin`, `purchase.order`, `purchase.order.line`, `stock.rule`, `stock.picking`, `stock.picking.type`, `stock.lot`, `res.company`, `product.product`, `sale.order`, `sale.order.line`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.replenish.mixin`, `purchase.order`, `purchase.order.line`, `stock.rule`, `stock.picking`, `stock.picking.type`, `stock.lot`, `res.company`, `product.product`, `sale.order`, `sale.order.line`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 59 of 59 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: stock_dropshipping
Source revision: 19.0.post20260921 (Odoo 19 Community). Read-only trace; neutral business language; no code copied.

## A. Capabilities / activation
- Dropshipping: goods move directly from vendor to customer without entering the company warehouse; adds a "Dropship" operation type, a "Dropship" route, per-company sequences and rules, and list/menu entries. stock_dropshipping/__manifest__.py:5-22; stock_dropshipping/data/stock_data.xml:4-18
- Optional (not auto-install): activated by the "Dropshipping" checkbox in Inventory settings or Purchase settings (module_stock_dropshipping). stock/models/res_config_settings.py:51; purchase_stock/models/res_config_settings.py:10; stock/views/res_config_settings_views.xml:210-212
- Depends on sale_purchase_stock (which itself is an auto-install bridge of sale_stock, purchase_stock, sale_purchase). stock_dropshipping/__manifest__.py:23; sale_purchase_stock/__manifest__.py:12,17
- Uninstall archives the dropship operation types. stock_dropshipping/__init__.py:7-9
- Route is selectable on sale lines, product and product category; it is excluded from the replenishment wizard route list. stock_dropshipping/data/stock_data.xml:7-14; stock_dropshipping/models/stock_replenish_mixin.py:10-12; stock_dropshipping/tests/test_dropship.py:605-620 (TEST)
- Menu "Dropships" under Inventory transfers for inventory users/managers; dropship counter buttons on sale and purchase forms. stock_dropshipping/views/stock_picking_views.xml:14-26; stock_dropshipping/views/sale_order_views.xml:9-18; stock_dropshipping/views/purchase_order_views.xml:9-14

## B. Business objects and relationships
- Operation type gets a new code "dropship" (source vendors location, destination customers location, no warehouse). If removed, types fall back to outgoing and archived. stock_dropshipping/models/stock.py:57-84
- Company creation creates the dropship sequence (prefix DS/), the operation type, and a buy-action stock rule from the vendors to the customers location, make-to-stock. stock_dropshipping/models/res_company.py:13-33,40-72,77-115
- A transfer is a "dropship" when its source is a vendor (or company-less transit) and destination a customer (or company-less transit) - defined by location types, not by operation type. stock_dropshipping/models/stock.py:40-47
- Flow: confirm sale order with dropship route -> request for quotation to vendor is generated -> confirm purchase -> dropship transfer vendor->customer -> validation updates delivered quantity on the sale line and received quantity on the purchase line. stock_dropshipping/tests/test_dropship.py:90-144 (TEST); stock_dropshipping/tests/test_dropship.py:553-583 (TEST)
- Return of a dropship reverses both delivered and received quantities. stock_dropshipping/tests/test_dropship.py:553-583 (TEST)
- Purchase and sale order counters: dropship transfers are separated from normal receipts/deliveries and counted in their own "dropship count". stock_dropshipping/models/purchase.py:13-27; stock_dropshipping/models/sale.py:10-24
- Purchase lines created from different sale lines are not merged, so delivered quantities can be mapped per sale line. stock_dropshipping/models/stock.py:10-15
- Purchase order that serves several sale orders: on confirmation, one transfer per sale order is created (not for services-only). stock_dropshipping/models/purchase.py:43-77; stock_dropshipping/tests/test_dropship.py:668-700 (TEST)
- Vendor address on rule: partner not forced for the dropship route; destination address of purchase set to the customer shipping address when picking type is dropship or when switched manually. stock_dropshipping/models/stock.py:17-21; stock_dropshipping/models/purchase.py:36-41; stock_dropshipping/tests/test_dropship.py:622-645 (TEST)
- Sale-line quantity handling: sale-line "procured quantity" is the sum of non-cancelled linked purchase lines (in UoM) if a purchase line is dropshipped; sale lines with dropship rules are flagged made-to-order in forecast display. stock_dropshipping/models/sale.py:30-53
- Service products sold with purchase (sale_purchase): the created purchase gets the dropship operation type and customer shipping address if a dropship type exists for the company. stock_dropshipping/models/sale.py:63-73
- Product description on dropship moves uses the outgoing-description (or display name) instead of the internal note/purchase description. stock_dropshipping/models/product.py:9-13; stock_dropshipping/tests/test_dropship.py:90-143 (TEST)
- Lot last-customer lookup: for dropship transfers the sale order's shipping partner is used; outgoing domain includes vendor->customer moves. stock_dropshipping/models/stock.py:90-104
- Sale-order cancel after purchase confirmation creates exactly one warning activity on the purchase order (TEST). stock_dropshipping/tests/test_dropship.py:585-603 (TEST)
- Lifecycle: no new state machine; sale (draft/sale), purchase (draft/purchase/done), transfer states are owned by sale, purchase, stock. stock_dropshipping/tests/test_dropship.py:100-118 (TEST)

## C. Validations / security / multi-company
- Rule lookup is limited to the sale line's company when the procurement comes from a sale line. stock_dropshipping/models/stock.py:29-34
- Multi-company creation: missing sequences/types/rules are created per company (run on install and on new company). stock_dropshipping/data/stock_data.xml:4,5,16-18; stock_dropshipping/models/res_company.py:33-35,70-72,113-115
- Vendor that is another company in the same database: a return still reconciles quantities (TEST). stock_dropshipping/tests/test_dropship.py:553-583 (TEST)
- Sale-side quantity computation reads purchase lines with elevated rights so that users without purchase rights can confirm. stock_dropshipping/models/sale.py:42-45
- Transfers for multi-sale purchases are created with elevated (superuser) rights. stock_dropshipping/models/purchase.py:62
- No access-rights CSV or record rules of its own. stock_dropshipping/__manifest__.py:24-29
- Menus/buttons gated: stock user/manager for menu and buttons; purchase user for the sale-form dropship button group. stock_dropshipping/views/stock_picking_views.xml:26; stock_dropshipping/views/sale_order_views.xml:10,17

## D. Handoffs (owner in brackets)
- Stock valuation: a dropship movement (vendor->customer, or transit without company) is treated separately from normal in/out; cost method logic is in [stock_account]. stock_account/models/stock_move.py:585-594
- (TEST) Valuation scenarios across standard/FIFO, continental/anglo-saxon, ordered/delivered invoicing policies for dropship. stock_dropshipping/tests/test_stockvaluation.py:114-260 (TEST)
- (TEST) A dropship does not change average cost of the product. stock_dropshipping/tests/test_stockvaluation.py:261-286 (TEST)
- (TEST) Returning a dropshipped delivery into own internal stock makes it a valued incoming move (stock valuation debited). stock_dropshipping/tests/test_stockvaluation.py:288-330 (TEST)
- Vendor bill/customer invoice: [account / purchase / sale]; on bill posting, the value of dropship movements linked to the bill lines is (re)computed. stock_account/models/account_move.py:42
- Purchase-side received-quantity edge cases for returns to stock [purchase_stock]. purchase_stock/models/purchase_order_line.py:68-70
- Procurement / RFQ grouping [purchase_stock]: dropship rfqs are grouped by reference. purchase_stock/models/stock_rule.py:370-373
- Delivery-address logic in [purchase_stock]. purchase_stock/models/purchase_order.py:327-340
- Sale line to purchase line link [sale_purchase_stock]. sale_purchase_stock/models/purchase_order.py:36-49
- Outbound external-location flag used by other logic [stock]. stock_dropshipping/models/stock.py:49-51
- Localisation modules referencing dropship: l10n_in_purchase_stock, l10n_in_stock, l10n_in_ewaybill_stock, l10n_it_stock_ddt, l10n_ro_edi_stock. (module names only)

## E. Configuration that changes outcomes
- Setting checkbox to install; per-company dropship operation type/rule; route flags (selectable on sale, product, product category). stock_dropshipping/data/stock_data.xml:7-14
- Vendor set on the product (or supplier info) determines which vendor gets the RFQ; purchase grouping by vendor setting (group_rfq) not applied for dropship type. purchase_stock/models/stock_rule.py:370
- Product outgoing description text. stock_dropshipping/models/product.py:11
- Valuation setup (cost method, real-time, anglo-saxon flag, invoicing policy) changes accounting outcome. stock_dropshipping/tests/test_stockvaluation.py:114-260 (TEST)

## F. Effective extension path (Community modules extending the same key objects; module names only)
- stock.picking: delivery_stock_picking_batch, mrp_subcontracting_dropshipping, purchase_stock, sale_stock, stock_account, stock_delivery, stock_dropshipping, and others.
- stock.picking.type: repair, stock_account, stock_picking_batch, stock_dropshipping, and others.
- stock.rule: mrp_subcontracting_dropshipping, purchase_stock, sale_purchase_stock, sale_stock, stock_dropshipping, and others.
- purchase.order: mrp_subcontracting_dropshipping, purchase_stock, sale_purchase_stock, stock_dropshipping, purchase_repair, and others.
- stock.replenish.mixin: mrp, mrp_subcontracting_dropshipping, purchase_stock, stock, stock_dropshipping. sale.order, stock.lot: multiple.
- Direct dropship-aware bridge: mrp_subcontracting_dropshipping.

## G. Not verified
- Behaviour of dropship with lot/serial numbers beyond one TEST on tracked products: UNKNOWN — EVIDENCE INSUFFICIENT (partial: stock_dropshipping/tests/test_dropship.py:528-551)
- Approval workflow: none found in this module; purchase-order approval thresholds are outside scope: UNKNOWN — EVIDENCE INSUFFICIENT
- Behaviour when the transit location is shared between companies (inter-company dropship): UNKNOWN — EVIDENCE INSUFFICIENT
- Partial delivery/backorder rules for dropship transfers: UNKNOWN — EVIDENCE INSUFFICIENT

