> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE - product_3d_viewer

Module: product_3d_viewer
License (confirmed in manifest): LGPL-3 (product_3d_viewer/__manifest__.py:23)
Author (manifest): SCG Legacy (Thailand) Co., Ltd. (product_3d_viewer/__manifest__.py:6)
Version (manifest): 19.0.1.0.1 (product_3d_viewer/__manifest__.py:4)
Path: addons_Extramodule/addons/product_3d_viewer
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Lets a user attach one 3D model file (GLB format) to a product template and preview it in the browser (product_3d_viewer/models/product_template.py:8-13).
- On a quotation / sales order, each order line shows a small "3D" icon column that opens the product's model in a pop-up viewer (product_3d_viewer/views/sale_order_views.xml:8-15; static/src/js/viewer_widget.js:235).

## 2. Attachment to CORE
- Depends on core `product` and `sale` (product_3d_viewer/__manifest__.py:9).
- core `product.template`: adds a file field for the model and a file-name field (models/product_template.py:8-13). Stored as attachment (line 10). No core method is overridden.
- core `sale.order.line`: adds three read-only, non-stored mirror fields pointing to the product's model file, file name and template (models/sale_order_line.py:8-25). No core method overridden.
- core views: form of product template inherited via `product.product_template_only_form_view` (views/product_template_views.xml:6; core:product/views/product_template_views.xml:55) - adds a "3D Model" notebook page. The page is declared permanently hidden (views/product_template_views.xml:9), so the upload field is not reachable from that page as written.
- core view `sale.view_order_form` (views/sale_order_views.xml:6; core:sale/views/sale_order_views.xml:252) - adds an optional column before the product column of the order lines.
- Core method overrides: none. ALTERS CORE CONTROL: none found.

## 3. New objects, security, automation, external calls
- New models: none. New fields only (see section 2).
- Security: no access file, no groups, no record rules declared in the manifest data list (product_3d_viewer/__manifest__.py:10-13). Access follows the inherited core models.
- Automation: none (no cron, no server action found).
- Front-end assets: styles, a template and a script registered in the backend bundle (product_3d_viewer/__manifest__.py:14-20); two field widgets registered (static/src/js/viewer_widget.js:104, :235).
- EXTERNAL CALL: on load the script inserts a script tag pulling a 3D viewer library from a public CDN host (unpkg.com), pinned to a fixed release (static/src/js/viewer_widget.js:14-21). This means end-user browsers need internet access to that host; no server-side call.
- The order-line widget reads the product record over the standard client ORM and fetches the file through the standard content route (static/src/js/viewer_widget.js:184, :192).

## 4. Odoo 19 compatibility
- Checked in Community 19 tree: views `product.product_template_only_form_view` exists (core:product/views/product_template_views.xml:55); `sale.view_order_form` exists (core:sale/views/sale_order_views.xml:252); order lines use `list` tag as in 19 syntax (views/sale_order_views.xml:8).
- Fields referenced (`product_id.product_tmpl_id`) exist on core models: not individually grepped beyond view check -> not checked.
- JS imports (@web/core/registry, @odoo/owl, standardFieldProps) - not checked against core web asset tree.

## 5. Custom-to-custom dependencies
- None declared (depends: product, sale only).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the hidden "3D Model" page is intended (the upload field would then be only reachable by another route); no other upload route was found in this module.
- UNKNOWN - EVIDENCE INSUFFICIENT: maximum file size / performance behaviour with large files (no limit found in module).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the CDN-hosted library is acceptable in an offline / restricted deployment.
