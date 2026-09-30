> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: sale_order_line_price_history

Module: sale_order_line_price_history
License (confirmed in manifest): AGPL-3 (sale_order_line_price_history/__manifest__.py:8)
Author (manifest): SMEsPlus Co.,Ltd (__manifest__.py:6); website field points to the OCA sale-workflow repository (__manifest__.py:7)
Version (manifest): 19.0.1.1.4 (__manifest__.py:4)
Path: addons_Extramodule/addons_extra/sale_order_line_price_history
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- From a quotation/sales-order line, a salesperson opens a pop-up showing earlier sales lines of the same product for the same customer (price_unit, discount, quantity, order date, state). Pointers: models/sale_order_line.py:9-17, wizards/sale_order_line_price_history.py:61-93, wizards/sale_order_line_price_history.xml:8-38.
- Options in the pop-up: include quotations (default off), include the customer's commercial entity and its contacts (default on), row limit 5/10/15/20 (default 5). wizards/sale_order_line_price_history.py:46-59.
- Intended to let the user copy an old price/discount back onto the current line (action_set_price, wizards/sale_order_line_price_history.py:150-154; readme/DESCRIPTION.rst:1-3).

## 2. Attachment to CORE
- core:sale, object sale.order.line: adds a button-action `view_price_history` (ADDS behavior, new method; models/sale_order_line.py:9). No core method is overridden.
- Re-declares `order_partner_id` as a bare customer link (models/sale_order_line.py:7). Core already defines it as a stored related field to the order's customer (core:sale/models/sale_order_line.py:48-51). Whether the core related/stored attributes survive the re-declaration is not verifiable by reading alone (see section 6). Not a control override.
- core:sale, view sale.view_order_form: adds a history icon button and a hidden customer column next to unit price in the order-line list (views/sale_views.xml:9-12; priority 999 at line 7).
- Price write-back: action_set_price writes price_unit and discount onto a sale.order.line with no state check (wizards/sale_order_line_price_history.py:150-152). It is a plain write and does not call any approval or pricelist logic; no core control is replaced or blocked. Not `ALTERS CORE CONTROL`.
- Overrides of core methods by name: none.

## 3. New objects, security, automation, external calls
- New transient models: sale.order.line.price.history (wizards/sale_order_line_price_history.py:5) and sale.order.line.price.history.line (same file:96).
- ACL: both transient models get full CRUD for group sales_team.group_sale_salesman (security/ir.model.access.csv:2-3). No record rules, no company scoping on the wizard itself; the lookup uses the normal sale.order.line search, so core record rules on sale.order.line apply.
- Crons / server actions / external calls: none found in module files.
- Duplicate definition: a second file declares the same line model (wizards/sale_order_line_price_history_line.py:5-23) but is not imported (wizards/__init__.py:2 imports only the first file). Dead file.

## 4. Odoo 19 compatibility (checked against Community 19 tree)
- Mismatch: search uses order state value "done" (wizards/sale_order_line_price_history.py:67). Core 19 sale.order state list has no "done" (core:sale/models/sale_order.py:26-31); locking is a separate `locked` flag (core:sale/models/sale_order.py:78). Effect: locked orders remain state "sale" so they are still found; the "done" value is simply never matched.
- Core references that do exist: sale.order.line.discount (core:sale/models/sale_order_line.py:184), product_uom_qty (:127), state (:56), group sale.group_discount_per_so_line (core:sale/security/res_groups.xml:8), group sales_team.group_sale_salesman (core:sales_team/security/sales_team_security.xml:9).
- Manifest description text still mentions version 18 (__manifest__.py:11), cosmetic.

## 5. Custom-to-custom dependencies
- None (depends only on core sale, __manifest__.py:13).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether re-declaring order_partner_id keeps the core stored/related behavior at runtime.
- UNKNOWN - EVIDENCE INSUFFICIENT: reachability of action_set_price from the UI; the shipped wizard view has no button calling it (wizards/sale_order_line_price_history.xml:21-32), only tests call it (tests/test_sale_order_line_price_history.py:147,156).
- UNKNOWN - EVIDENCE INSUFFICIENT: how much of the code is derived from the OCA upstream module named in the manifest website field; no provenance note in the module folder.
