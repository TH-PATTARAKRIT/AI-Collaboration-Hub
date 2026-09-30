> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE - product_sequence

Module: product_sequence
License (confirmed in manifest): LGPL-3 (product_sequence/__manifest__.py:21)
Author (manifest): SMEsPlus Co.,Ltd (product_sequence/__manifest__.py:9)
Version (manifest): 19.0.1.0 (product_sequence/__manifest__.py:8)
Path: addons_Extramodule/addons_extra/product_sequence
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Lets a product category own a numbering series (prefix, built up through the parent categories) and automatically stamps new products of that category with the next number as their internal reference (product_sequence/models/product_category.py:7-14, :34-46; models/product_template.py:14-22).

## 2. Attachment to CORE
- Depends on core `base`, `product` (product_sequence/__manifest__.py:11-14).
- core `product.category`: adds a link to a sequence record, a prefix, a "show prefix" flag, and two stored computed full-prefix fields (models/product_category.py:7-14). Full prefix = parent's full prefix followed by own prefix (models/product_category.py:24-27).
- core `ir.sequence` (base): creates a no-gap sequence with fixed code, 3-digit padding, step 1, per category (models/product_category.py:36-46, :57, :77).
- core `product.template`: internal reference field is written from the category series.
- Overrides of core methods (by name):
  - `product.category.create` - ADDS behavior before core: creates the sequence record when the flag and a prefix are given (models/product_category.py:48-60).
  - `product.category.write` - ADDS behavior after core: creates or renames the sequence to follow name/prefix changes (models/product_category.py:62-78).
  - `product.category.unlink` - ADDS behavior before core: deletes the linked sequence with elevated rights (models/product_category.py:29-32).
  - `product.template.create` - ADDS behavior before core: fetches next number and sets internal reference when category has the flag (models/product_template.py:14-22).
  - `product.template.write` - ADDS behavior before core: when the category is (re)set to a flagged one, a NEW number is drawn and overwrites the internal reference, even if the user typed one (models/product_template.py:24-30). This REPLACES the user-entered value in that case.
  - onchange on category: blanks the internal reference when the category is not flagged (models/product_template.py:7-12).
- Compared with core: core defines internal reference as a stored computed field with an inverse from variants (core:product/models/product_template.py:153-155). This module writes into it directly. ALTERS CORE CONTROL: none of the listed controls (numbering of products is affected: product internal-reference numbering only, not accounting/document numbering).

## 3. New objects, security, automation, external calls
- New models: none. New fields listed above.
- Security: access file grants full rights on product.category and product.template to stock user and stock manager groups (product_sequence/security/ir.model.access.csv:2-5). NOTE: the file is NOT listed in the manifest data list (product_sequence/__manifest__.py:15-16), so these lines are not loaded as written. Also rows 2-3 and rows 4-5 reuse the same record id, so if loaded only one row per pair would survive (security/ir.model.access.csv:2-5).
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- `create` is declared with the single-record decorator while the body loops over the input as if it were a list of dicts (models/product_category.py:48-52; models/product_template.py:14-17). Core convention in 19: create accepts a dict or a list (core:odoo/orm/decorators.py:357-372). A call with a single dict would iterate over key names; a call with a list works. Runtime behavior not tested -> risk, not confirmed.
- The `complete_seq` field is recursive and stored (models/product_category.py:10-12); core category also uses recursive compute (core:product/models/product_category.py:18-19). No mismatch found.
- View inherits `product.product_category_form_view` (views/product_cate_views.xml:6) - exists (core:product/views/product_category_views.xml:4).

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: number gaps when a product save fails after a number was drawn (no-gap type set at models/product_category.py:38, actual behavior on rollback not tested).
- UNKNOWN - EVIDENCE INSUFFICIENT: multi-company handling of the sequences (no company set in the sequence definition, models/product_category.py:36-46).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether duplicates of internal reference are blocked (no constraint in module).
