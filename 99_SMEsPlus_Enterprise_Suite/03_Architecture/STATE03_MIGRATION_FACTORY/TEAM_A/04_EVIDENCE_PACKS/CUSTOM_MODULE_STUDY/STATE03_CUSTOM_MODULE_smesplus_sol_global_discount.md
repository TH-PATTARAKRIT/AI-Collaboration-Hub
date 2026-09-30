> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: smesplus_sol_global_discount

Module: smesplus_sol_global_discount ("Sale Order Line Global Discount")
License (confirmed in manifest): LGPL-3
Author (manifest): SMEsPlus
Version (manifest): 19.0.1.0.0
Path: addons_Extramodule/addons_extra/smesplus_sol_global_discount
Source revision studied: workspace on-disk copy (not verified against upstream)
Classification (batch_07): Company Extra/Custom

## 1. Business capability
- Tags discount lines created by the standard sales-order "Discount" wizard so that the order shows what kind of discount each line is: a global percentage or a fixed amount, and records the percentage used (smesplus_sol_global_discount/wizard/sale_order_discount.py:70-80; models/sale_order.py:19-26).
- When a global-percentage discount is applied again, previously created global discount lines are removed first, so the order is not discounted twice (wizard/sale_order_discount.py:82-85).
- Two hidden-by-default columns on the order lines (views/sale_order_view.xml:8-11).

## 2. Attachment to CORE
- Core module depended on: sale (__manifest__.py:1-15).
- sale.order.line (core:sale/models/sale_order_line.py): new fields discount_type (selection: percent on all lines, global discount, fixed amount) and global_percent (models/sale_order.py:22-26). Column placement after core discount column (views/sale_order_view.xml:8; core:sale/models/sale_order_line.py:184).
- sale.order.discount wizard (core:sale/wizard/sale_order_discount.py:11): override of _prepare_global_discount_so_lines (wizard/sale_order_discount.py:70-86; core:sale/wizard/sale_order_discount.py:56). ADDS behavior after core: calls core first, then stamps each prepared line with the type and percent. It also DELETES existing global-discount lines of the order when the new discount is a whole-order percentage (wizard/sale_order_discount.py:82-85). The deletion happens while the new lines are still only being prepared (before they are created), inside one transaction.
- A large commented-out replacement of _create_discount_lines (wizard/sale_order_discount.py:11-68) and a commented compute on sale.order (models/sale_order.py:7-16) are inactive; they contain a mistyped literal ("global_dicount") which would never match the selection key global_discount (models/sale_order.py:24).
- Stored global_percent value is written multiplied by 100 (wizard/sale_order_discount.py:80) while core wizard percentage is a fraction (core:sale/wizard/sale_order_discount.py:20, 36-37) - a units convention to note when reading the field.
- ALTERS CORE CONTROL: no (pricing helper). It does touch order-line deletion inside a draft-order discount flow; the core wizard's own state rules were not re-checked here.

## 3. New objects, security, automation, external calls
- New models: none. Security: none shipped, so core sales access applies. No cron / server action / external call.

## 4. Odoo 19 compatibility
- Checked in Community 19: sale.order.discount wizard and method _prepare_global_discount_so_lines exist (core:sale/wizard/sale_order_discount.py:11, 56); core discount_type on the wizard uses keys sol_discount, so_discount, amount (core:sale/wizard/sale_order_discount.py:21, 36, 130) - the module tests these keys (so_discount, amount) at wizard/sale_order_discount.py:73, 83.
- Core sale.order.line has no field discount_type or global_percent (grep of core:sale/models shows none), so no name collision.
- Unused imports in wizard file (wizard/sale_order_discount.py:1-3): harmless.
- No mismatches found for active code.

## 5. Custom-to-custom dependencies
- None.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether discount_type stays consistent when a user edits or deletes a discount line manually (no write/unlink override).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the "percent on all line" option key (models/sale_order.py:23) is ever set by any code (no writer found in module).
- UNKNOWN - EVIDENCE INSUFFICIENT: effect on invoicing, reports and taxes of the tagged lines (no other file in module).
