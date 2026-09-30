> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE - product_category_filter

Module: product_category_filter
License (confirmed in manifest): AGPL-3 (product_category_filter/__manifest__.py:7)
Author (manifest): SMEsPlus (product_category_filter/__manifest__.py:6)
Version (manifest): 19.0.1.0.0 (product_category_filter/__manifest__.py:9)
Path: addons_Extramodule/addons_extra/product_category_filter
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds an "enabled for product use" flag on each product category and restricts the category drop-down on product forms to flagged categories only (product_category_filter/models/category.py:11, :17; views/category_views.xml:38-46).
- Adds "Category Enable / Category Disable" filters and a column in the category list (views/category_views.xml:10-13, :21-23).

## 2. Attachment to CORE
- Depends on core `product` and `stock` (product_category_filter/__manifest__.py:12). No stock object is used by the code found; the stock dependency is not exercised in this module (models/category.py, views/category_views.xml).
- core `product.category`: adds a yes/no field "Show Category", default no (models/category.py:11). Consequence: after install every existing category is not flagged, so none is selectable until flagged (default at models/category.py:11).
- core `product.template`: redefines the category field with a fixed domain to flagged categories (models/category.py:17). Uses field name categ_id as in core (core:product/views/product_views.xml:127).
- core views inherited: category search, list, form and product template form (views/category_views.xml:4,17,27,38; core:product/views/product_category_views.xml:4,35,46; core:product/views/product_views.xml:5 record product_template_form_view).
  - The search view replaces the core "name" search field with the "complete name" field (views/category_views.xml:7-9; core:product/views/product_category_views.xml:46-52).
- Core method overrides: none. Validations added: none (an unused ValidationError/expression import at models/category.py:4-5). ALTERS CORE CONTROL: none (a data-entry restriction on the category choice only; it is a UI domain, not a server-side constraint, so imports and API writes are not blocked - inferred from domain-only definition at models/category.py:17).

## 3. New objects, security, automation, external calls
- New models: none. One new field on category.
- Security: no access file, no groups, no record rules (product_category_filter/__manifest__.py:13-15).
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- Checked: core views product_category_form_view, product_category_list_view, product_category_search_view exist (core:product/views/product_category_views.xml:4,35,46); list view contains display_name field used as anchor (core:product/views/product_category_views.xml:41); core product.category has complete_name (core:product/models/product_category.py:18).
- No mismatch found in the checked items. Model-level `product_template_form_view` id confirmed in core:product/views/product_views.xml:5.

## 5. Custom-to-custom dependencies
- None declared. Note: product_sequence (batch sibling) also extends the same product.category form view - interplay not tested.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether other core / custom screens (sales, purchase, website category pickers) should also be limited; only the product template form is covered.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether an install-time data step flags existing categories (no data file found in manifest).
