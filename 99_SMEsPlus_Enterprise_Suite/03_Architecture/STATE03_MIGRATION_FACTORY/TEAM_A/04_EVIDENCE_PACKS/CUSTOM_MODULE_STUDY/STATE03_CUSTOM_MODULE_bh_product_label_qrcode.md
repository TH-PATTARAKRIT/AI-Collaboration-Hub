> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: bh_product_label_qrcode

- Module: bh_product_label_qrcode
- License (confirmed in manifest): LGPL-3 (bh_product_label_qrcode/__manifest__.py:15)
- Author (manifest): SCGL (bh_product_label_qrcode/__manifest__.py:6)
- Version (manifest): 19.0.1.0.0 (bh_product_label_qrcode/__manifest__.py:4)
- Path: addons_Extramodule/addons/bh_product_label_qrcode
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Lets the user choose, in the product label print dialog, whether the product barcode is printed as a linear barcode (default) or as a QR code (models/product_label_layout.py:8-16; views/product_label_layout_views.xml:11-13).
- QR variant prints a small QR image plus the barcode text underneath, sized per label layout (report/report_simple_label.xml:9-15, 31-37, 53-59, 75-81).
- The manifest summary mentions the 2x7 layout, but the code also changes 4x7 and both 4x12 layouts (report/report_simple_label.xml:6, 28, 50, 72).

## 2. Attachment to CORE
- Core module `product`, wizard `product.label.layout` (core:product/wizard/product_label_layout.py:9): ADDS field "Label Type" (required, default barcode). Overrides `_prepare_report_data` and ADDS behavior after core: passes the selected type into the report data (models/product_label_layout.py:18-21; core:product/wizard/product_label_layout.py:37-70 returns the template id and data).
- Core wizard view `product.product_label_layout_form` (core:product/wizard/product_label_layout_views.xml:3) gets the selector after the print format field (core:...:14).
- Core report templates `product.report_simple_label2x7`, `4x7`, `4x12`, `4x12_no_price` (core:product/report/product_product_templates.xml:4, 33, 56, 81): the barcode block (core:...:15, 47, 72, 93) is REPLACED by a block with two branches (QR or the previous style with fixed image sizes). The non-QR branch is not a copy of core sizes; it uses module-defined dimensions (report/report_simple_label.xml:17-18, 39-40, 61-62, 83-84), so the default barcode look is changed as well.
- The dymo layout (core:...:102) is not touched.
- Core-control impact: none on accounting, stock valuation, security, numbering or approvals. ALTERS CORE CONTROL: not found in code read.

## 3. New objects, security, automation, external calls
- New models: none (extension of a transient wizard). ACLs, groups, record rules, crons, server actions, external calls: none.

## 4. Odoo 19 compatibility
- Checked by grep in Community tree: wizard `product.label.layout`, method `_prepare_report_data` returning (template id, data), view `product_label_layout_form`, field `print_format`, and the four templates with a `t-if="barcode"` block all exist (core pointers above). No mismatch found.
- No other Community module defines a `label_type` on `product.label.layout` (grep of product and stock found label_type only on a different stock wizard: core:stock/wizard/stock_label_type.xml:11).

## 5. Custom-to-custom dependencies
- None declared (depends: product only, manifest:8).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: how the variable `label_type` reaches the label templates when a label is printed from a path that does not call the wizard (templates read it directly, report/report_simple_label.xml:9). The core print-from-wizard path supplies report data, but other entry points were not traced.
- UNKNOWN - EVIDENCE INSUFFICIENT: scan readability of a 6 mm QR image in the 4x12 layouts (report/report_simple_label.xml:55); needs physical/print test.
