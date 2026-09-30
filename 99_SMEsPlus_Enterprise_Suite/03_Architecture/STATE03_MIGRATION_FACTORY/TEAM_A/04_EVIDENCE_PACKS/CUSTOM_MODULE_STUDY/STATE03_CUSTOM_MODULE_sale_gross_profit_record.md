> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE - sale_gross_profit_record

Module: sale_gross_profit_record
License (confirmed in manifest): LGPL-3 (sale_gross_profit_record/__manifest__.py:5)
Author (manifest): Moe Pa Pa (sale_gross_profit_record/__manifest__.py:11)
Version (manifest): 19.0.1.1 (sale_gross_profit_record/__manifest__.py:4)
Path: addons_Extramodule/addons_extra/sale_gross_profit_record
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds a "Gross Profit" tab on the quotation / sales order form listing each line with product, quantity, list price, entered unit price and product cost (sale_gross_profit_record/views/sale_extend_view.xml:14-29).
- Provides a second, wider version of the tab (margin, %GP, average price columns) shown only if a separate module named sale_fixed_discount is installed (views/sale_extend_view.xml:31-54; models/sale_order.py:10-13).

## 2. Attachment to CORE
- Depends on core `sale` only (sale_gross_profit_record/__manifest__.py:14-16).
- core `sale.order`: adds a hidden yes/no flag computed by looking up the installed-modules list for sale_fixed_discount (models/sale_order.py:7-13), and two computed line lists that simply mirror the order lines (models/sale_order.py:15-37).
- core `sale.order.line`: adds two related read-only fields (list price and cost taken from the product template, models/sale_order_line.py:7-8) and ten plain numeric fields (margin, %margin, %GP, average quantity, discount, average prices; models/sale_order_line.py:9-18). No code in this module fills those ten fields (grep of models dir shows no compute/write) - they are expected to be populated by another module.
- Core method overrides: none. New compute methods only. ALTERS CORE CONTROL: none.
- Views: inherits `sale.view_order_form`, anchors payment_term_id and notebook (views/sale_extend_view.xml:6,10,14; core:sale/views/sale_order_views.xml:41, :252, :496).

## 3. New objects, security, automation, external calls
- New models: none. No access file, no groups, no record rules (manifest data list has only the view, sale_gross_profit_record/__manifest__.py:17-19).
- Cost exposure: the product cost field in core is restricted to internal users group (core:product/models/product_template.py:100-103); this module shows it in the tab for whoever can see the tab; the tab itself has no group restriction (views/sale_extend_view.xml:17-19) -> any user with core-level access to the field sees cost. Portal users are outside base.group_user (inference).
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- Checked: `sale.order.line.product_template_id` exists (core:sale/models/sale_order_line.py:89); `standard_price` on template exists (core:product/models/product_template.py:100); view anchors exist (see section 2).
- The installed-module lookup reads the module table; core grants access to that table only to the system administrator group (core:base/security/ir.model.access.csv:25). The lookup is not elevated (models/sale_order.py:12), so opening an order as a non-administrator may raise an access error -> inferred from ACL, not run.
- Manifest name says "Not depend sale_fixed_discount"; that module was not located in this batch (not checked).

## 5. Custom-to-custom dependencies
- Soft, by name only: sale_fixed_discount (models/sale_order.py:12) - not declared in manifest, not present in the assigned folder.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: which process fills margin / %GP fields (no writer in this module).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether cost shown is in order currency or company currency (no conversion in code).
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior of the list-mirroring computed lists on large orders (performance).
