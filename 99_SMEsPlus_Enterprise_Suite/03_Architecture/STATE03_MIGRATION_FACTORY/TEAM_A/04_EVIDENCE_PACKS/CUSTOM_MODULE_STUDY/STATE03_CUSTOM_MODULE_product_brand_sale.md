> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE - product_brand_sale

Module: product_brand_sale
License (confirmed in manifest): AGPL-3 (product_brand_sale/__manifest__.py:49). Note: the file header in product_brand_sale/__init__.py:9-19 quotes LGPL v3; manifest value is used here.
Author (manifest): Cybrosys Techno Solutions (product_brand_sale/__manifest__.py:20)
Version (manifest): 19.0.1.0.1 (product_brand_sale/__manifest__.py:3)
Path: addons_Extramodule/addons_extra/product_brand_sale
Source revision studied: workspace on-disk copy (not verified against upstream). Contains local edits ("Refactored by SMEsPlus", product_brand_sale/models/res_users.py:1).

## 1. Business capability
- Introduces a "Division" (brand) master linked to products, customers, users/employees and sales teams; limits which products a salesperson / customer can pick on a sales order and which product categories/products show on the web shop (models/brand.py:66-70, :72-82; models/sale.py:322-354; controllers/main.py:31-56).
- Optional per-company switches: split delivery per division (warehouse chosen from division) and split invoice per division (models/res_config_settings.py:7-8, :19-20; models/sale.py:121-156, :362-368).
- Also adds distribution channel and sales office masters (models/employee.py:22-35), a division column in sales reporting and journal-item lists (models/brand.py:101-115; models/account.py:7).

## 2. Attachment to CORE (depends: sale_management, base, account, sales_team, hr, website, website_sale - product_brand_sale/__manifest__.py:25-33)
- core `product.template`: adds division link (models/brand.py:69). core `sale.report`: adds division dimension (models/brand.py:104-115). core `account.move.line`: stored division copied from product (models/account.py:7). core `res.partner`, `res.users`, `hr.employee`, `crm.team`: division lists; employee, user and partner lists are linked by write-back methods (models/employee.py:7-12; models/res_users.py:15-27; models/res_partner.py:21-37). `res.company`: two switches (models/res_config_settings.py:4-8). `website`, `product.public.category`: web-shop filtering.
- Overrides of core methods, by name:
  - `sale.order._create_invoices` - REPLACES core (full copy of an older core body, splitting per division; models/sale.py:97-315; core:sale/models/sale_order.py:1552). ALTERS CORE CONTROL (invoicing). Differences from core 19: bypasses `_create_account_invoices` and the reversed-entry marking (core:sale/models/sale_order.py:1678-1686); creates invoices under elevated rights (models/sale.py:249). When "split invoice" is on (default on, models/res_config_settings.py:8) only order lines whose product has a division are invoiced; lines without division are skipped (models/sale.py:121-133, :72). When the switch is off the branch uses names not defined in that scope (models/sale.py:158-183) -> failure risk (inference from reading, not run).
  - `sale.order._get_invoiceable_lines` - REPLACES core, adds division filter from context (models/sale.py:63-95; core:sale/models/sale_order.py:1501).
  - `sale.order.line._prepare_procurement_values` - ADDS/ALTERS after core: overrides warehouse, deadline, route, partner keys; BLOCKS order confirmation with an error when split delivery is on and the product's division has no warehouse (models/sale.py:356-389). ALTERS CORE CONTROL (delivery routing). Signature takes an extra argument that core 19 does not (models/sale.py:356 vs core:sale_stock/models/sale_order_line.py:284) -> super call would fail in 19 (inference; not run).
  - `sale.order` fields customer and salesperson redefined: salesperson becomes a plain stored field defaulting to current user, core automatic salesperson-from-customer compute is dropped (models/sale.py:26-35, :46-61; core:sale/models/sale_order.py:208, :478). Customer field redefined with legacy readonly-state keyword (models/sale.py:18-24). `_onchange_partner_id_domain`: limits selectable customers to those listing the salesperson, except sales managers (models/sale.py:37-44).
  - `account.move.create` - ADDS after core: re-copies division into lines (models/account.py:13-19).
  - `website._search_exact`, `product.public.category.check_has_ptemplate` (new) - ADDS: filters search results and categories by the visitor's divisions (models/brand.py:12-38, :44-64). WebsiteSale `_get_additional_shop_values` - REPLACES core's category list logic (controllers/main.py:31-56; core:website_sale/controllers/main.py:262 - core takes extra keyword arguments).
  - Settings `get_values` / `set_values` - ADD storage of two system parameters (models/res_config_settings.py:22-40).
- Not a posting / lock-date / valuation control; ALTERS CORE CONTROL applies to invoicing (above), delivery creation (above) and security (below).

## 3. New objects, security, automation, external calls
- New models: product.brand, distribution.channel, sales.office (models/brand.py:72; models/employee.py:22,30). None declares a description.
- ACL: all three granted with an EMPTY group, i.e. to every user including portal/public; brand has full delete right (security/ir.model.access.csv:2-4).
- Record rules (persistent, noupdate): salesperson group sees only own user record; "all leads" group sees internal or same-company users (security/record_rules.xml:4-16). ALTERS CORE CONTROL (record rules on users): core has a global users rule and a portal rule (core:base/security/base_security.xml:141-153); the added group rule narrows the salesperson group, so choosing another salesperson from an order may show restricted names (inference).
- Company scoping: switches stored per company; brand/channel/office have no company field.
- Automation: none (no cron, no server action). External calls: none; two system parameters are read at runtime (models/sale.py:324).
- Web: controller subclass of the shop controller (controllers/main.py:29).

## 4. Odoo 19 compatibility (grep in Community 19)
- Mismatch: `_prepare_procurement_values` signature (see above). Mismatch: `_create_invoices` fork lacks 19 hooks (`_create_account_invoices`, core:sale/models/sale_order.py:1546).
- Mismatch: `_get_additional_shop_values(self, values)` lacks the extra keyword arguments that core passes (controllers/main.py:31 vs core:website_sale/controllers/main.py:262, :545).
- `user_has_groups` used at models/sale.py:60 is not found in Community 19 orm (`has_groups` exists, core:base/models/res_users.py:1034); only in an unused compute (compute keyword commented, models/sale.py:29).
- Field keyword `states=` (models/sale.py:23) not found in Community 19 fields code - likely ignored.
- Warehouse link uses stock model but manifest does not depend on stock / sale_stock (models/brand.py:82; models/sale.py:364, :380) -> undeclared dependency.
- `create` overrides use single-record decorator with list-style callers (models/account.py:13). Views/templates: anchors found for website_sale.categories_recursive, option_collapse_categories_recursive (core:website_sale/views/templates.xml:1650,1745), sale settings block `catalog_setting_container` (core:sale/wizard/res_config_settings_views.xml:12), hr `hr_settings` page (core:hr/views/hr_employee_views.xml:358), report filter Customer (core:sale/report/sale_report_views.xml:106). Same block id used twice in settings view (views/res_config_settings_views.xml:27,33).

## 5. Custom-to-custom dependencies
- None declared. Runtime interplay with any module also overriding sale order invoicing/procurement: UNKNOWN.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether write-back between employee, user and partner division lists loops (models/employee.py:7-12, models/res_users.py:15-27, models/res_partner.py:21-37).
- UNKNOWN - EVIDENCE INSUFFICIENT: meaning of "SAP Code" fields (external SAP link not evidenced; no integration code found).
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior for multi-company invoicing splits; runtime results of invoice/delivery override on 19.
