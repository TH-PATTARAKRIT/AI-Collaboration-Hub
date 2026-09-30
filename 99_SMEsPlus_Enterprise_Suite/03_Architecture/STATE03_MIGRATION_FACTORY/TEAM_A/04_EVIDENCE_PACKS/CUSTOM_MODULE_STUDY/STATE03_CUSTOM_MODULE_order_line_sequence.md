> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: order_line_sequence

## 0. Header
- Module: order_line_sequence
- License (confirmed in manifest): AGPL-3 (order_line_sequence/__manifest__.py:25)
- Author (manifest): Yin Htay (order_line_sequence/__manifest__.py:8); company/maintainer entries name SMEsPlus (manifest:9-10)
- Version (manifest): 19.0.1.0.1 (order_line_sequence/__manifest__.py:3)
- Path: addons_Extramodule/addons_extra/order_line_sequence
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Shows a running line number ("No") next to each product line on sales orders, purchase orders, invoices/bills and delivery/receipt operation lines, and prints numbering on some printed documents (order_line_sequence/models/*.py; views/*.xml; report/*.xml).
- The number is a stored computed integer recalculated from the line order (models/sale_order_line.py:7-22; models/purchase_order_line.py:6-20; models/account_move_line.py:6-24; models/stock_move.py:7-28).
- Printed documents: sales order PDF gets a "NO" column with a blank cell for section, note and combo rows (report/report_saleorder_inherit.xml:4-33); customer invoice PDF gets a "No" column that shows the number only on product lines (report/report_invoice_sequence.xml:3-17); the delivery slip PDF gets a "NO" column on the pending, done (serial and aggregated) and backorder tables using a running index (report/report_purchaseorder_inherit.xml:6-56).

## 2. Attachment to CORE
- Manifest depends: sale_management, base (manifest:11-14). It also inherits models and views of purchase, stock and account, which are not declared (see section 4).
- Extends core models sale.order.line, purchase.order.line, account.move.line, stock.move by adding one stored computed field sequence_no with its compute method _compute_sequence_no on each (pointers above). No core method is overridden. ADDS after core. ALTERS CORE CONTROL: no.
- Uses core "sequence" fields: core:sale/models/sale_order_line.py:38, core:purchase/models/purchase_order_line.py:22, core:stock/models/stock_move.py:24, core:account/models/account_move_line.py:90.
- Views inherit sale.view_order_form, purchase.purchase_order_form (core:purchase/views/purchase_views.xml:126), stock.view_picking_form (core:stock/views/stock_picking_views.xml:110), account.view_move_form, inserting the number column before the product column (views/*.xml).
- Report templates inherit sale.report_saleorder_document, account.report_invoice_document, stock.report_delivery_document, and its sub-templates stock.stock_report_delivery_has_serial_move_line and stock.stock_report_delivery_aggregated_move_lines (report/*.xml; core sub-templates referenced at core:stock/report/report_deliveryslip.xml:140,146).

## 3. New objects, security, automation, external calls
- New fields only (sequence_no on four line models, indexed). No new models, ACLs (the access file entry is commented out, manifest:16), groups, record rules, cron, or external calls.

## 4. Odoo 19 compatibility
- Undeclared dependencies: the module inherits purchase.order.line, stock.move and the purchase / stock views but its manifest lists only sale_management and base (manifest:11-14); sale_management depends on sale and digest (core:sale_management/__manifest__.py:38) and sale does not depend on purchase or stock (core:sale/__manifest__.py:11-15). Installing on a database without purchase and stock would probably fail at load. Whether they are always installed in the target suite is not known.
- File naming mismatch: report/report_purchaseorder_inherit.xml actually contains the delivery slip changes (templates on stock.report_delivery_document), while no template modifies the purchase order PDF (grep of inherit_id in report/*.xml). The purchase order print is therefore not numbered by this module, despite the file name.
- report/stock_picking_report_view.xml duplicates the delivery slip changes but is not listed in the manifest data (manifest:21-23), so it is not loaded; if it were added together with report_purchaseorder_inherit.xml the delivery slip would receive two number columns.
- Invoice print numbering uses stored sequence_no of lines, whereas sales order and delivery slip use a running loop index; numbers can therefore differ between documents (report_invoice_sequence.xml:13 vs report_saleorder_inherit.xml:14). Index variables such as line_index, move_index, bo_line_index depend on the core templates defining them; not verified.
- Account move line compute is triggered by lines of the whole move and rewrites numbers for all invoice lines (models/account_move_line.py:14-24); purchase and sale computes sort by sequence only, without a tie-breaker on id (models/purchase_order_line.py:18; models/sale_order_line.py:20), so equal sequences give an unstable order.
- The stock move compute assumes a picking is set (models/stock_move.py:17-28); moves without a picking get 0.
- Xpaths into core templates were checked only for names of sale (th_description, tr_product, td_product_name, tr_section, tr_combo, td_note_name at core:sale/report/ir_actions_report_templates.xml) and invoice (core:account/views/report_invoice.xml:176,224); others not checked.
- Licence note: the top-level __init__.py carries a header text stating LGPL v3 attributed to Cybrosys Technologies (order_line_sequence/__init__.py:4-19) while the manifest declares AGPL-3 (manifest:25). The gate used the manifest value.

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether purchase and stock modules are always installed alongside this one in the target suite.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the stored numbers are recomputed when lines are re-ordered by drag-and-drop in the UI.
- UNKNOWN - EVIDENCE INSUFFICIENT: intended treatment of purchase order print (no template found).
