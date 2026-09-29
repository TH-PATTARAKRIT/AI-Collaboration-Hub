# Source Map (candidate) — `product_expiry`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `product_expiry` |
| Display name | Products Expiration Date |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c644d9e4b5012b68` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/product_expiry/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock`
- Direct dependents in 300-module list (2): `mrp_product_expiry`, `sale_stock_product_expiry`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (1): `19_bhpro_master_data` — OPL-1

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / —
- Inventory of user-facing artifacts (counts): menu items 0, views 14, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `expiry.picking.confirmation` (Confirm Expiry)
- Objects extended from other modules (11): `stock.move.line`, `stock.quant`, `product.product`, `product.template`, `stock.move`, `stock.picking`, `stock.rule`, `res.config.settings`, `stock.lot`, `stock.forecasted_product_product`, `report.stock.quantity`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `expiry.picking.confirmation` ← Community: `mrp_product_expiry`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `stock.move.line`, `stock.quant`, `product.product`, `product.template`, `stock.move`, `stock.picking`, `stock.rule`, `res.config.settings`, `stock.lot`, `stock.forecasted_product_product`, `report.stock.quantity`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`group_expiry_date_on_delivery_slip`); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 39 of 39 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: product_expiry
Source revision: 19.0.post20260921 | Path base: odoo/addons | Method: static source read (no execution)

## A. Capabilities
- Adds shelf-life dates to tracked products and lot/serial numbers, plus a First-Expiry-First-Out picking policy; depends on stock (product_expiry/__manifest__.py:5,10-17). Not an application, not auto_install; optional add-on switched on by the "Expiration Dates" setting in inventory settings (stock/models/res_config_settings.py:11; product_expiry/models/res_config_settings.py:18-22 turns it on when lot tracking is enabled). Conditional per product ("Use Expiration Date").
- Product-level lead times in days: expiration, best-before, removal, alert (product_expiry/models/product_product.py:38-54). The flag is forced off when tracking is set to none (line 56-59). Form section visible only for tracked products with the flag, for users in the lot-tracking group (views/product_template_views.xml:9-13).
- Lot-level dates: expiration date defaults to now + product expiration days; best-before, removal and alert dates derive from expiration minus product offsets; editing the expiration shifts the other dates by the same difference (product_expiry/models/production_lot.py:12-19, 50-79). (TEST) product_expiry/tests/test_stock_lot.py:30, :233, :740.
- Receipt-time capture: move lines compute expiration and removal dates from the lot, or from the picking scheduled date + product days when lots are created on the operation; new lot is created with that date (models/stock_move_line.py:34-62). (TEST) test_stock_lot.py:290, :334, :665.
- Bulk lot/serial generation and pasted text import carry a default expiration date, and text input containing a date is parsed as expiration date (models/stock_move.py:18-52).
- FEFO removal strategy record seeded (data/product_expiry_data.xml:3-6); ordering by removal date, then incoming date (models/stock_quant.py:24-28). (TEST) test_stock_lot.py:630.
- Fresh-stock accounting: quants past removal date count as zero available quantity; reservations and availability consider the move date; product free/forecast quantities computed with the current date (models/stock_quant.py:30-36; models/stock_move.py:87-95; models/product_product.py:11-12; stock consumer at stock/models/stock_quant.py:767-768 and stock/models/product.py:219).
- Expired-delivery guard: validating a transfer containing lots past expiry alert or past removal date opens a confirmation dialog: proceed anyway, or drop expired lines then validate (models/stock_picking.py:11-48; wizard/confirm_expiry.py:37-52). (TEST) test_stock_lot.py:383, :709, :774, :831.
- Reminder activity: scheduled job hook logs a to-do for the product responsible on lots whose alert date is reached and that still hold internal stock; once per lot (models/production_lot.py:81-107; models/stock_rule.py:8-17). (TEST) test_stock_lot.py:78-222.
- Reporting: "Expiration Alerts" filter on lots (views/production_lot_views.xml:38); forecast report adds "to remove now/on" lines and a to-remove figure (report/stock_forecasted.py:11-61); stock-quantity report counts only reserved quantity for items due for removal (report/report_stock_quantity.py:13-15); lot label shows best-before and expiry (report/report_lot_barcode.xml:3-15); GS1 barcode on quants prepends expiry (17) and best-before (15) identifiers (models/stock_quant.py:15-22).
- Delivery slip column "Expiration Date" only when the extra group is enabled (report/report_deliveryslip.xml:3-21; security/stock_security.xml:4-6; settings toggle models/res_config_settings.py:10-16).
- Lot display name flags "Expired" or "Expire on" in formatted display contexts (production_lot.py:24-39).

## B. Objects and lifecycle
- Extends product.template, stock.lot, stock.move, stock.move.line, stock.quant, stock.picking, stock.rule and the product-product quantity computation (models/__init__ list; see F). One new transient dialog model expiry.picking.confirmation (wizard/confirm_expiry.py:9-16).
- Derived flags, not workflow states: product_expiry_alert = expiration date reached (production_lot.py:41-48); reminder flag product_expiry_reminded (line 22). "Expired" status for dialog purposes = alert flag OR removal date passed (stock_picking.py:22).
- Lifecycle gate: expiry check runs in the picking pre-validation hook, skipped when context flag skip_expired is set after the user confirms (stock_picking.py:11-19; wizard/confirm_expiry.py:41).

## C. Validations, security, multi-company
- No hard constraint prevents shipping expired goods; the control is a confirmation dialog (stock_picking.py:16-18), so it is a soft control.
- ACL: dialog model readable/writable/creatable (no delete) for stock users (security/ir.model.access.csv:2). Extra group "Include expiration dates on delivery slip" (security/stock_security.xml:4-6). No record rules in module.
- Install hook makes lot tracking group implied for internal and portal users (product_expiry/__init__.py:10-16).
- Multi-company: reminder chooses the product responsible under the lot's company, falls back to any responsible, then the superuser (production_lot.py:101). No company rule added here.

## D. Handoffs (owner in brackets)
- Stock [stock]: owns lots, quants, moves, removal strategies, availability logic that reads the with_expiration context (stock/models/stock_quant.py:767; stock/models/product.py:219); scheduler job that this module extends: stock/data/stock_sequence_data.xml:46-56 (daily "Procurement: run scheduler").
- Barcode [barcodes_gs1_nomenclature via stock]: GS1 date identifiers 15/17 (barcodes_gs1_nomenclature/data/barcodes_gs1_rules.xml:107-119).
- Sales [sale_stock_product_expiry]: fresh-quantity forecast on order lines (sale_stock_product_expiry/models/sale_order_line.py:9-16; auto_install true at its manifest:8).
- Manufacturing [mrp_product_expiry]: same expired-lot dialog before marking a production done (mrp_product_expiry/models/mrp_production.py:9-26; auto_install at manifest:17).
- Messaging [mail]: to-do activity creation. No accounting entry is created by this module.

## E. Configuration that changes outcomes
- Setting "Expiration Dates" (module switch) and "Display Expiration Dates on Delivery Slips" (needs lot-on-delivery-slip enabled) (res_config_settings.py:10-27).
- Per product: use flag, four day offsets; per product category: removal strategy FEFO must be chosen to get FEFO picking (TEST test_stock_lot.py:635-637).
- Editing lot dates by hand overrides derived dates.

## F. Effective extension path (module names only)
- Modules depending on product_expiry: sale_stock_product_expiry, mrp_product_expiry. Objects extended here are also extended by: stock_delivery, mrp, mrp_subcontracting, sale_stock, purchase_requisition_stock (for stock.move/line/quant/picking/rule/lot).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: interaction of expiry dates with landed costs, valuation or accounting (no such code in this module).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of the reminder when the scheduler is disabled by an administrator (job is defined in stock).
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side views and tours (static JS not analysed).

