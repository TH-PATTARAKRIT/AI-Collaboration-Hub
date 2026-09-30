> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: scgl_pos_order_times

## 0. Header
- Module: scgl_pos_order_times
- License (confirmed in manifest): LGPL-3 (scgl_pos_order_times/__manifest__.py:14)
- Author (manifest): SCG Legacy (Thailand) Co., Ltd. (scgl_pos_order_times/__manifest__.py:15)
- Version (manifest): 19.0.1.0.0 (scgl_pos_order_times/__manifest__.py:12)
- Path: Extra_Module_scgl/scgl_pos_order_times
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds two duration measures to Point of Sale orders: "Service Time" (order date to the last payment date, in hours) and "Preparation Time" (order date to a "Kitchen Ready At" moment), shown as optional hidden columns in the orders list and on the order form (models/pos_order.py:8-31; views/pos_order_views.xml:11-17, :31-35; manifest:5-10).
- A manual header button "Mark Kitchen Ready" and a public method meant to be called by a kitchen display module stamp the ready moment (models/pos_order.py:33-37; views/pos_order_views.xml:27-30).
- Meant as a Community replacement for an Enterprise column set (comment in views/pos_order_views.xml:5).

## 2. Attachment to CORE
- Depends declared: point_of_sale (manifest:17).
- Core objects extended: `pos.order` (core:point_of_sale/models/pos_order.py), list view `point_of_sale.view_pos_order_tree` (field `is_edited` anchor at core:point_of_sale/views/pos_order_view.xml:306), form view `point_of_sale.view_pos_pos_form` (header; page "extra" at core:point_of_sale/views/pos_order_view.xml:172; group "other_information" at :180; `tracking_number` at :182).
- No core method overridden. New compute `_compute_order_times` (models/pos_order.py:19-31) depends on `date_order` (core:point_of_sale/models/pos_order.py:306), `payment_ids.payment_date` (core:point_of_sale/models/pos_payment.py:24) and `state`.
- No ALTERS CORE CONTROL.

## 3. New objects, security, automation, external calls
- New fields on pos.order: `preparation_done_date` (indexed, not copied), `preparation_time`, `service_time` (stored computed, models/pos_order.py:8-17). New method `action_mark_kitchen_ready` (models/pos_order.py:33-37), idempotent, skips cancelled orders (:36).
- No ACL, group, record rule changes; no company scoping beyond core. The manual button has no group restriction in the view (views/pos_order_views.xml:28-29) — any user who can edit the order may stamp it (inference).
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- The "paid / done / invoiced" state tests (models/pos_order.py:26; views/pos_order_views.xml:16, :34) include `invoiced`, which is a value of the invoice-status field in Community 19, not of the order state (core:point_of_sale/models/pos_order.py:336 for state; :376-379 for invoice status). That value never matches order state; paid/done still work. Low impact.
- `column_invisible`, `optional`, `float_time` used consistent with 17+ syntax; not runtime-tested.
- All core anchors listed in section 2 exist in Community 19.

## 5. Custom-to-custom dependencies
- None declared. Designed to be fed by scgl_pos_prep_display (which sets the ready time from its board; see that file for how, if at all, it calls `action_mark_kitchen_ready`).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: which module in the deployed system actually calls `action_mark_kitchen_ready`.
- UNKNOWN — EVIDENCE INSUFFICIENT: timezone/rounding conventions expected by users of the H:MM display.
