> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: smesplus_uom_ext

Module: smesplus_uom_ext ("Units of measure")
License (confirmed in manifest): LGPL-3
Author (manifest): SMEsPlus Co., Ltd.
Version (manifest): 19.0.1.0
Path: addons_Extramodule/addons_extra/smesplus_uom_ext
Source revision studied: workspace on-disk copy (not verified against upstream)
Classification (batch_07): Company Extra/Custom

## 1. Business capability
- Restricts the unit of measure that can be chosen on a vendor price line (product supplier info) to units that belong to the same measure family as the product's own unit, i.e. units linked to it through the chain of "reference unit" relations, upward and downward (smesplus_uom_ext/models/uom_uom.py:6-36; models/product_supplierinfo.py:6-13).
- Business effect: a supplier price cannot accidentally be entered in an unrelated unit (e.g. kg for a product counted in pieces); pack sizes (box, carton) linked to the base unit remain selectable.

## 2. Attachment to CORE
- Core modules depended on (manifest): uom, product, sale (__manifest__.py:1-19). Note sale is declared but no sale object is touched in this module.
- uom.uom (core:uom/models/uom_uom.py:17-18): three helper methods added - lower units, upper units, and "same group" units (models/uom_uom.py:6, 14, 33). They walk the reference-unit relation (core:uom/models/uom_uom.py:41). No core method overridden; ADDS helpers only.
- product.supplierinfo (core:product/models/product_supplierinfo.py): new computed helper field filter_uom listing the allowed units (models/product_supplierinfo.py:6-13); the vendor price list view restricts the Unit field with it (views/product_template_view.xml:9-14; core:product/views/product_supplierinfo_views.xml:88; core field product_uom_id core:product/models/product_supplierinfo.py:25).
- ALTERS CORE CONTROL: no (a view-level input filter only; not a server-side validation, so import or API writes are not blocked by it).

## 3. New objects, security, automation, external calls
- New models: none. Security: none shipped. No cron, no server action, no external call.
- Upper-unit search loads all units of the database each time it is computed (models/uom_uom.py:15-16) - a performance observation, not a control.

## 4. Odoo 19 compatibility
- Checked in Community 19: uom.uom relative_uom_id and related_uom_ids exist (core:uom/models/uom_uom.py:41-42), so the helper logic matches the 19 measure model (which replaced the old category concept). Core has no method of the same names (core:uom/models/uom_uom.py greps show none), so no collision.
- Checked: product.supplierinfo product_uom_id exists (core:product/models/product_supplierinfo.py:25); view product.product_supplierinfo_tree_view exists (core:product/views/product_supplierinfo_views.xml:88).
- Not checked: whether the domain attribute on a column that is already computed/stored with a default in core behaves identically in the vendor-price popup form.

## 5. Custom-to-custom dependencies
- None.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the compute for the helper field gets correct results when the price line has no product yet (branch exists at models/product_supplierinfo.py:11-13; runtime not observed).
- UNKNOWN - EVIDENCE INSUFFICIENT: why sale is a declared dependency (no use found in the module).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the helper field has a dependency declaration for recompute when units change (none found at models/product_supplierinfo.py:8).
