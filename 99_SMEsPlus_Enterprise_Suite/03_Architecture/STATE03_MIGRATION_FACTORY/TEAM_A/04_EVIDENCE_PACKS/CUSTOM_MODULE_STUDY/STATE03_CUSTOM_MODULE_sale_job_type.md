> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE - sale_job_type

Module: sale_job_type
License (confirmed in manifest): LGPL-3 (sale_job_type/__manifest__.py:32)
Author (manifest): BHPRO (sale_job_type/__manifest__.py:15)
Version (manifest): 19.0.1.0.0 (sale_job_type/__manifest__.py:4)
Path: addons_Extramodule/addons/sale_job_type
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- A configurable list of "job types" (installation, service, etc.) with code, order, colour, archive switch, unique name intent (sale_job_type/models/sale_job_type.py:5-37), maintained under Sales > Configuration (views/sale_job_type_views.xml:94-98).
- Each quotation / sales order carries a job type; the delivery order copies it and shows it in form, list, search/group-by and on the printed delivery slip (models/sale_order.py:9; models/stock_picking.py:8-17; views/stock_picking_views.xml:13-49; reports/stock_delivery_slip_report.xml:12-23).

## 2. Attachment to CORE
- Depends on core `sale_management`, `sale_stock`, `stock` (sale_job_type/__manifest__.py:17-21).
- core `sale.order`: adds job type link with change tracking, active-only choice, not database-required (models/sale_order.py:9-18). Adds a validation method: an order without a job type is rejected whenever that field is part of a create/write (models/sale_order.py:20-27). Method `_check_job_type_required` ADDS a validation (BLOCKS saving of orders lacking the field). Not a lock-date/posting/approval control. Inference: constraint triggers only when the field is included in the saved values (Odoo constraint semantics; not run), so records created by code paths that omit the field, and orders existing before install, may not be blocked.
- core `stock.picking`: adds stored related field to the sales order's job type (models/stock_picking.py:8-17; sale_id defined in core:sale_stock/models/stock.py:187).
- Views inherited: sale order form after tags (views/sale_order_views.xml:8,12; core:sale/views/sale_order_views.xml:157), picking form, search, list (views/stock_picking_views.xml:8,26,44; core:stock/views/stock_picking_views.xml:110,345,66), delivery slip template (reports/stock_delivery_slip_report.xml:9-12; core:stock/report/report_deliveryslip.xml:3).
- Core method overrides: none (only new validation).  ALTERS CORE CONTROL: none of the listed controls.

## 3. New objects, security, automation, external calls
- New model `sale.job.type` (models/sale_job_type.py:6). Access: salesman read only; sales manager full; administrator full (security/ir.model.access.csv:2-4). No record rules; no company field on the model, so job types are shared across companies (models/sale_job_type.py:10-33).
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility (grep in Community 19)
- `_sql_constraints` is no longer supported in 19 (warning only, constraint ignored): unique-name rule at models/sale_job_type.py:35-37 vs core:odoo/orm/model_classes.py:162-164 -> uniqueness NOT enforced by database in 19 (inference; not run).
- `name_get` override (models/sale_job_type.py:39-46): display names in 19 come from the computed display_name (core:odoo/orm/models.py:473-476) -> "[code] name" label likely never used.
- `toggle_active` override only calls super (models/sale_job_type.py:48-50); in 19 the method is deprecated in favor of action_archive/unarchive (core:odoo/orm/models.py:5802-5806).
- Manifest text says "required Job Type dropdown" but field is not required at DB or view level (models/sale_order.py:12; views/sale_order_views.xml:13-15).
- View anchors, groups and menu parent exist (core:sales_team security group_sale_salesman/manager; core:sale/views/sale_menus.xml:97). No further mismatch found.

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether orders created by web shop, API import or other modules omit the job type and pass unblocked.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether existing sales orders are back-filled at install (no data file / migration found).
- UNKNOWN - EVIDENCE INSUFFICIENT: reporting use of job type beyond the delivery slip (no sale report changes found).
