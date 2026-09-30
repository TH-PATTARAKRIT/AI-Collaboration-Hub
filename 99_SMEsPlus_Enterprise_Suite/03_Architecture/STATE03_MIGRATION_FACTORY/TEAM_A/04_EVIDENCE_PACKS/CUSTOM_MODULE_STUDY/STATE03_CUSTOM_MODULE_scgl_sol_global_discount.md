> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_sol_global_discount

Module: scgl_sol_global_discount
License (confirmed in manifest): LGPL-3 (scgl_sol_global_discount/__manifest__.py:12)
Author (manifest): SCGL (scgl_sol_global_discount/__manifest__.py:7)
Version (manifest): 19.0.1.0.0 (scgl_sol_global_discount/__manifest__.py:6)
Path: addons_Extramodule/addons/scgl_sol_global_discount
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Tags each sales-order line created by the core "Discount" wizard with how it came about: fixed amount, or global percentage, and stores the percentage used (scgl_sol_global_discount/wizard/sale_order_discount.py:70-81; scgl_sol_global_discount/models/sale_order.py:22-26).
- When a new global-percentage discount is applied, previously tagged global-percentage discount lines are removed first, so only one global discount line set remains (scgl_sol_global_discount/wizard/sale_order_discount.py:82-85).
- Shows the two new columns (hidden by default) on the sales-order line list (scgl_sol_global_discount/views/sale_order_view.xml:8-11).

## 2. Attachment to CORE
- sale.order.line (core:sale): ADDS fields `discount_type` (percent on all lines / global / fixed amount) and `global_percent` (scgl_sol_global_discount/models/sale_order.py:22-26). Note: `discount_type` here is a different field from the wizard's own selector.
- sale.order.discount wizard (core:sale/wizard/sale_order_discount.py:11-12): overrides `_prepare_global_discount_so_lines` (scgl_sol_global_discount/wizard/sale_order_discount.py:70). Calls core first, then ADDS tags to each returned line, and additionally DELETES existing global-discount lines of the order (line 85). The deletion is a side effect inside a method that core expects only to return values (core:sale/wizard/sale_order_discount.py:56, 157). Classified: ADDS behavior after core plus a side effect. Whether deletion is blocked on a confirmed order depends on core line-unlink rules (not traced): UNKNOWN.
- sale.order: class declared with no active code, only commented text (scgl_sol_global_discount/models/sale_order.py:4-16). Wizard `_create_discount_lines` override is fully commented out (scgl_sol_global_discount/wizard/sale_order_discount.py:11-68).
- Does not touch posting, lock dates, valuation, numbering, approvals. No ALTERS CORE CONTROL identified.

## 3. New objects, security, automation, external calls
- No new models, ACLs, record rules, groups, crons, server actions or external calls.
- Company scoping inherited from core wizard/line rules; nothing added.

## 4. Odoo 19 compatibility
- Overridden method exists in Community 19: `_prepare_global_discount_so_lines` (core:sale/wizard/sale_order_discount.py:56). Wizard selector values `so_discount` / `amount` exist (core:sale/wizard/sale_order_discount.py:21-28).
- Percentage saved as a whole number (multiplied by 100) (scgl_sol_global_discount/wizard/sale_order_discount.py:80) whereas core stores the wizard percentage as a fraction (core:sale/wizard/sale_order_discount.py:132 multiplies by 100 for display). Different scale by design; not a mismatch.
- View inherits `sale.view_order_form` and targets list column `discount` (core:sale/views/sale_order_views.xml:728). Tag "list" is used (Odoo 18+ naming) - consistent with 19.
- Typo in commented code ("global_dicount") differs from the live value "global_discount" (scgl_sol_global_discount/wizard/sale_order_discount.py:25 vs 79); harmless as the old code is inactive.
- Imports unused (defaultdict, ValidationError) - cosmetic.

## 5. Custom-to-custom dependencies
- None.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the removal of the earlier global discount line is intended when the second application is of a different type (removal is keyed on the current choice being "global", scgl_sol_global_discount/wizard/sale_order_discount.py:82-83).
- UNKNOWN - EVIDENCE INSUFFICIENT: reports, exports, or e-invoice mapping that read the new fields (none found in this module).
- UNKNOWN - EVIDENCE INSUFFICIENT: effect on confirmed or invoiced orders.
