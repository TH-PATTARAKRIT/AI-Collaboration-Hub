# Source Map (candidate) — `sale_purchase`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_purchase` |
| Display name | Sale Purchase |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `40b65bcc4f9e40b5` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_purchase/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale`, `purchase`
- Direct dependents in 300-module list (3): `purchase_requisition_sale`, `sale_purchase_project`, `sale_purchase_stock`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Sale based on service outsourcing.
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `sale.order`, `sale.order.line`, `purchase.order`, `purchase.order.line`, `product.template`
- Company-dependent settings introduced: 1 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `sale.order`, `sale.order.line`, `purchase.order`, `purchase.order.line`, `product.template`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 49 of 49 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: sale_purchase (revision 19.0.post20260921)
Scope: Odoo Community read-only study. Pointers `module/path:LINE`; (TEST) = test-derived.

## A. Capabilities and activation
- Sells a service that is fulfilled by an outside vendor: confirming the sale automatically creates a draft request for quotation (RFQ) to that vendor (sale_purchase/__manifest__.py:6-9; sale_purchase/models/sale_order.py:20-24).
- Depends on sale and purchase (sale_purchase/__manifest__.py:14-17) and is auto_install: it activates itself when both are installed (sale_purchase/__manifest__.py:24).
- Per-product opt-in: flag "Subcontract Service" on the product, company-dependent, not copied on duplicate, visible only for service-type products (sale_purchase/models/product_template.py:11-13; sale_purchase/views/product_views.xml:9-12). This is a service outsourcing feature; it is not a manufacturing subcontracting flow (no manufacturing dependency in sale_purchase/__manifest__.py:14-17).
- Adds smart links: Purchase button on the sale order (purchase users only) and Sale button on the purchase order (salesmen only) (sale_purchase/views/sale_order_views.xml:10-17; sale_purchase/views/purchase_order_views.xml:9-14).

## B. Objects, relationships, lifecycle
- Sale order line -> many generated purchase lines (read-only) (sale_purchase/models/sale_order_line.py:15). Purchase line carries an "Origin Sale Item" link and a related Sale Order (sale_purchase/models/purchase_order.py:92-93). Sale order counts distinct purchase orders reached through its lines (sale_purchase/models/sale_order.py:10-19,54-55).
- Trigger 1, order confirmation: each line whose product is flagged and that has no purchase line yet creates one (sale_purchase/models/sale_order.py:20-24; sale_purchase/models/sale_order_line.py:295-306). Re-confirming after cancel does not regenerate (sale_purchase/models/sale_order_line.py:302-303) (TEST: sale_purchase/tests/test_sale_purchase.py:134-180).
- Trigger 2, a line added to an already confirmed order (state "sale") generates immediately, except expense lines (sale_purchase/models/sale_order_line.py:42-49).
- Vendor choice: the product's vendor price list entry matched on quantity and unit; if none, confirmation is blocked with an error (sale_purchase/models/sale_order_line.py:222-227) (TEST: sale_purchase/tests/test_sale_purchase.py:126-133).
- RFQ reuse: an existing draft RFQ for the same vendor, company, and same source sale order is reused; otherwise a new RFQ is created (sale_purchase/models/sale_order_line.py:229-254). Source sale order name is appended to the RFQ origin (sale_purchase/models/sale_order_line.py:280-283). Generated RFQs stay in draft (TEST: sale_purchase/tests/test_sale_purchase.py:78-114).
- RFQ header values: vendor, vendor reference, company, vendor purchase currency (else current company currency), no delivery address, payment term and fiscal position from vendor, order date = customer commitment date (or now) minus vendor lead time (sale_purchase/models/sale_order_line.py:114-141).
- RFQ line values: quantity converted to product unit, then to vendor unit; price, discount and lead time from vendor entry; taxes = product vendor taxes of the PO company chain mapped through fiscal position; name from product/vendor description plus variant text (sale_purchase/models/sale_order_line.py:143-220) (TEST: sale_purchase/tests/test_sale_purchase.py:115-125,246-324,378-410).
- Quantity change on a confirmed line: increase -> update the latest purchase line if its PO is draft/sent/to approve, else create a new purchase line for the difference; decrease -> schedule a warning activity on the purchase order(s), no automatic reduction (sale_purchase/models/sale_order_line.py:51-69,75-112) (TEST: sale_purchase/tests/test_sale_purchase.py:181-245,411-440). A form warning also shows when qty is lowered below origin but not below delivered (sale_purchase/models/sale_order_line.py:25-36).
- Cancellation: cancelling the sale order schedules a warning activity on each non-cancelled generated PO (sale_purchase/models/sale_order.py:26-32,57-79); cancelling a PO schedules a warning on each source sale order, assigned to the salesperson (sale_purchase/models/purchase_order.py:55-82) (TEST: sale_purchase/tests/test_sale_purchase.py:78-114). Nothing is cancelled automatically in the other document.
- PO delivery address is copied from the sale shipping partner only when the PO already carries one and all source orders agree (sale_purchase/models/purchase_order.py:25-33,84-86).

## C. Validations, automation, security, multi-company
- Product constraint: flag needs type "service" and at least one vendor entry (sale_purchase/models/product_template.py:15-32); flag is auto-cleared if type is not service or expense policy is not "no" (sale_purchase/models/product_template.py:34-37).
- Generation runs with elevated rights so a salesperson without purchase rights can still confirm; that user cannot read the PO or its lines (sale_purchase/models/sale_order.py:23,31; sale_purchase/models/purchase_order.py:10-13) (TEST: sale_purchase/tests/test_access_rights.py:32-67).
- Counters are group-restricted: sale-side purchase count to purchase users, PO-side sale count to salesmen (sale_purchase/models/sale_order.py:10-13; sale_purchase/models/purchase_order.py:10-17). No access-rule or record-rule file in this module (manifest data list sale_purchase/__manifest__.py:18-23).
- Multi-company: flag is per company and evaluated in the sale line's company; RFQ created in that company (sale_purchase/models/sale_order_line.py:119-120,134,301) (TEST: sale_purchase/tests/test_sale_purchase.py:325-377, a FIXME there notes a permission workaround needing elevated rights).

## D. Handoffs (owner)
- Purchasing document lifecycle (confirm, receive, vendor bill): purchase / account (sale_purchase generates draft lines only).
- Analytics: the sale line analytic distribution is copied to the purchase line (sale_purchase/models/sale_order_line.py:218-219); analytic posting is owned by account/analytic.
- Taxes and fiscal position: account (sale_purchase/models/sale_order_line.py:129,143-145). Currency conversion of vendor price: base/account (sale_purchase/models/sale_order_line.py:146-154).
- Inventory: none for services; dropship/stock variants live in sale_purchase_stock and stock_dropshipping (see F).

## E. Configuration that changes outcomes
- Product: flag, vendor list (price, min qty, unit, lead time, discount, currency) (sale_purchase/models/sale_order_line.py:190-217).
- Customer commitment date drives RFQ order date (sale_purchase/models/sale_order_line.py:114-117). Vendor payment term, purchase currency, fiscal position (sale_purchase/models/sale_order_line.py:128-141).

## F. Extension path (modules)
- Depend on sale_purchase (manifest grep): sale_purchase_stock, sale_purchase_project, purchase_requisition_sale (all auto_install), stock_dropshipping.
- Override the generation hooks: sale_purchase_project (order and line values), stock_dropshipping (order values). Other models extended by sale_purchase_stock: stock.move, sale.order, purchase.order, purchase.order.line, stock.rule (sale_purchase_stock/models/*.py _inherit).

## G. Not verified
- Behaviour of sale_purchase_stock / purchase_requisition_sale interplay in detail: UNKNOWN — EVIDENCE INSUFFICIENT
- Message wording of the three activity templates beyond titles (sale_purchase/data/mail_templates.xml:4,28,48): UNKNOWN — EVIDENCE INSUFFICIENT
- Whether an RFQ is auto-confirmed under any setting: UNKNOWN — EVIDENCE INSUFFICIENT

