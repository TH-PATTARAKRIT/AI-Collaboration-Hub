> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: scgl_pos_prep_display

## 0. Header
- Module: scgl_pos_prep_display
- License (confirmed in manifest): LGPL-3 (scgl_pos_prep_display/__manifest__.py:17)
- Author (manifest): SCG Legacy (Thailand) Co., Ltd. (scgl_pos_prep_display/__manifest__.py:18)
- Version (manifest): 19.0.1.1.0 (scgl_pos_prep_display/__manifest__.py:15)
- Path: Extra_Module_scgl/scgl_pos_prep_display
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Kitchen / preparation display board for Point of Sale, as a Community-side replacement for a preparation display (manifest:3-13).
- Managers configure one or more displays: which Points of Sale feed it, which product categories are shown, auto-clear, and ordered stages with colour and an alert timer, defaults "To prepare" 10 min, "Ready" 5 min, "Completed" 0 (models/prep_display.py:12-35).
- Each POS order sent to preparation becomes a ticket on every matching display, listing lines, notes and elapsed time; staff advance it by stage, drag and drop, "Next" or "Done" (models/prep_order.py:122-142; views/prep_order_views.xml:6-30).
- Reaching the last stage records a completion time and stamps the POS order's "Kitchen Ready At" (models/prep_order.py:107-121); moving a ticket back clears both (:116-120).
- Board reloads every 10 seconds while visible (static/src/prep_board/prep_board.js:9-28).
- Reporting menu "Preparation Time": pivot/graph of preparation minutes by display, stage, product, POS and cashier (models/prep_report.py:5-31; views/prep_report_views.xml).
- Menus: "Preparation Display" under the POS menu for POS users; "Preparation Time" under POS Reporting for POS managers (views/menus.xml:4-8). These are additions, nothing is hidden.

## 2. Attachment to CORE
- Depends declared: point_of_sale and scgl_pos_order_times (manifest:20).
- Core objects extended: `pos.order` (create and write); reads `pos.config`, `pos.category`, `product.product`, `pos.session`, `product.category`, `res.partner`, `res.users` for display and reporting. Core anchors: menus `point_of_sale.menu_point_of_sale` and `point_of_sale.menu_point_rep` (core:point_of_sale/views/point_of_sale_view.xml:12, :24); groups `point_of_sale.group_pos_user` / `group_pos_manager` (core:point_of_sale/security/point_of_sale_security.xml:8, :13).
- Overrides by name (models/pos_order.py):
  - `create` (:13-17): ADDS after core — for new orders that already carry a preparation-change record, feeds the boards.
  - `write` (:19-26): ADDS after core — when the preparation-change record is written, feeds the boards; when the order state becomes cancelled, archives its tickets.
  - Input consumed: the preparation-change JSON that the POS client writes (core field core:point_of_sale/models/pos_order.py:305; client structure core:point_of_sale/static/src/app/models/pos_order.js:39-51, :232-250 with keys such as uuid, product_id, quantity, note). The module parses the text as JSON and ignores unreadable data with a warning (models/pos_order.py:28-39).
- No core control is replaced or blocked. No ALTERS CORE CONTROL.

## 3. New objects, security, automation, external calls
- New models: `scgl.prep.display`, `scgl.prep.stage` (models/prep_display.py:7-97), `scgl.prep.order` (ticket) and `scgl.prep.line` (models/prep_order.py:5-233), and read-only analysis model `scgl.prep.report` backed by a database view (models/prep_report.py:8-50).
- ACL (security/ir.model.access.csv:2-10): POS users read displays and stages, and read/create/modify (no delete) tickets and ticket lines; POS managers full rights on all four; POS users read the report. No report row for managers separately (manager group implies user group, core:point_of_sale/security/point_of_sale_security.xml:17).
- Record rules (security/security.xml:4-13): company scoping on displays (`company_id in company_ids`) and tickets (via the display's company). No rule on ticket lines, stages or the report view; the report view exposes rows across companies to any POS user with menu access in principle (the report menu is manager-only, views/menus.xml:8) (inference from missing rule; not tested).
- Automation: no cron; board refresh is client-side polling. Ticket creation is synchronous inside POS order create/write (models/pos_order.py:13-26), so its failure could affect order saving (inference).
- Performance: the "late" filter is computed by searching all open tickets in memory (models/prep_order.py:67-72).
- Reads the report SQL directly from database tables (models/prep_report.py:33-50); table set: ticket lines, tickets, POS orders, products, templates.
- External calls: none.

## 4. Odoo 19 compatibility
- Confirmed in Community 19: `last_order_preparation_change` (core:point_of_sale/models/pos_order.py:305), `floating_order_name` (:346), `tracking_number` (:368), `pos_categ_ids` on products (core:point_of_sale/models/product_template.py:26), `_read_group` (core:odoo/orm/models.py:1867), `drop_view_if_exists` (core:odoo/tools/sql.py:665), field `aggregator` attribute usage, kanban `t-name="card"` template style.
- Not verified: the report model's `init` builds the view with string formatting of a query text (models/prep_report.py:50); Community 19 has a newer helper style for view creation — not checked.
- Uses the ORM `_read_group` with a `['__count']` aggregate (models/prep_display.py:44-45) consistent with 19 naming; not runtime-tested.

## 5. Custom-to-custom dependencies
- Depends on scgl_pos_order_times: calls its method `action_mark_kitchen_ready` and reads its field `preparation_done_date` (models/prep_order.py:112, :118-120).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the restaurant POS extension (order button flow) is installed and writes the preparation-change record the same way as the base POS.
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour for combo lines and for orders edited after being sent (only line-level upsert logic was read).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether users in the report menu can see other companies' rows (no rule on the analysis view).
