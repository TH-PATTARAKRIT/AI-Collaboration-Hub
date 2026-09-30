> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE - purchase_order_lines_discount

Module: purchase_order_lines_discount
License (confirmed in manifest): AGPL-3 (purchase_order_lines_discount/__manifest__.py:17)
Author (manifest): Sayed Hassan (purchase_order_lines_discount/__manifest__.py:15)
Version (manifest): 19.0.0.0 (purchase_order_lines_discount/__manifest__.py:16)
Path: addons_Extramodule/addons_extra/purchase_order_lines_discount
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds a fixed-amount discount column to purchase order lines and keeps it in sync with a percentage discount: typing one recomputes the other on screen (purchase_order_lines_discount/models/purchase_order_line.py:9-35; views/purchase_order_view.xml:8-10).
- Passes the percentage discount to the vendor bill line when a bill is created from the order (models/purchase_order_line.py:56-73).

## 2. Attachment to CORE
- Depends on core `base`, `purchase` (purchase_order_lines_discount/__manifest__.py:21).
- core `purchase.order.line`:
  - Redefines the percentage discount field (models/purchase_order_line.py:11). Core 19 already has this field, stored and computed from vendor price lists (core:purchase/models/purchase_order_line.py:29-33; :461, :483). Here it becomes a plain stored field with default zero and label "% Disc." -> REPLACES core field definition; the automatic vendor-pricelist discount fill is expected to be lost (inference from field redefinition; not run).
  - Adds a new fixed-amount discount field (models/purchase_order_line.py:9). It is not used in any amount calculation found; only the percentage feeds core totals (core:purchase/models/purchase_order_line.py:123).
- Overrides / new methods (by name):
  - onchange of percentage discount, onchange of fixed discount: ADD behavior (screen-only conversion, call amount recompute) (models/purchase_order_line.py:13-35). The fixed-to-percent formula divides by quantity x unit price with no zero guard (models/purchase_order_line.py:30) -> risk for zero-price lines (inference).
  - `_convert_to_tax_base_line_dict`: defined here; this method name is not present in the Community 19 account tax code searched (core:account/models/account_tax.py, grep no hit) -> dead code in 19 (models/purchase_order_line.py:37-54).
  - `_prepare_account_move_line`: REPLACES core behavior (models/purchase_order_line.py:56-73; core:purchase/models/purchase_order_line.py:628-648). It reads `taxes_id` and `product_uom` on the line; in 19 the fields are `tax_ids` and `product_uom_id` (core:purchase/models/purchase_order_line.py:34, :43). Also omits down-payment flag and the refund sign handling present in core (core:purchase/models/purchase_order_line.py:637-644). ALTERS CORE CONTROL (vendor-bill preparation from purchase order; may raise an error at bill creation -> inferred, not run).
- View: inherits `purchase.purchase_order_form`, anchor on tax_ids column (views/purchase_order_view.xml:6,8; core:purchase/views/purchase_views.xml:126, :292).

## 3. New objects, security, automation, external calls
- New models: none. Security file has one line naming a model that this module does not define, and the file is not listed in the manifest data (purchase_order_lines_discount/security/ir.model.access.csv:2; __manifest__.py:24-26) -> not loaded.
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility (checked by grep in Community 19)
- Mismatch: `taxes_id` on purchase.order.line does not exist; 19 uses `tax_ids` (models/purchase_order_line.py:49, :68 vs core:purchase/models/purchase_order_line.py:34).
- Mismatch: `product_uom` on purchase.order.line does not exist; 19 uses `product_uom_id` (models/purchase_order_line.py:64 vs core:purchase/models/purchase_order_line.py:43).
- Mismatch: `_convert_to_tax_base_line_dict` not found in core account tax model (models/purchase_order_line.py:44).
- Conflict: percentage discount field already defined by core with different type of definition (see section 2).
- View anchors `purchase_order_form` and `tax_ids` exist (core:purchase/views/purchase_views.xml:126, :292).

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the fixed amount is meant to be reflected in totals (no compute uses it).
- UNKNOWN - EVIDENCE INSUFFICIENT: real runtime effect of the field redefinition on existing data after upgrade.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether a second module (e.g., any purchase discount module in the same workspace) collides on the same fields.
