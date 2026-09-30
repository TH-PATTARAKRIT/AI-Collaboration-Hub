> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: bh_parent_company

- Module: bh_parent_company
- License (confirmed in manifest): LGPL-3 (bh_parent_company/__manifest__.py:31)
- Author (manifest): BHPRO (bh_parent_company/__manifest__.py:29)
- Version (manifest): 19.0.1.4.7 (bh_parent_company/__manifest__.py:4)
- Path: addons_Extramodule/addons/bh_parent_company
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Master data for a customer group hierarchy: Parent Company, Brand (owned by an "HQ Brand" customer), and Store Type under a brand (bh_parent_company/models/bh_parent_company.py:13; models/bh_brand.py:7; models/bh_store_type.py:13).
- Lets a contact be tagged with an HQ customer, a brand and a store type; sales orders inherit brand and store type from the customer and can be searched, grouped and reported by parent company (models/res_partner.py:9-72; models/sale_order.py:8-46; views/sale_order_views.xml:76-104).
- Smart buttons for brands, contacts, orders; a PDF "sales by parent company" report listing confirmed orders (models/bh_parent_company.py:194-234; reports/parent_company_sales_template.xml:67-83).
- Parent company carries VAT, registration, address, payment terms and a credit limit as descriptive data (models/bh_parent_company.py:54-92).

## 2. Attachment to CORE
- `res.partner` (core:base/models/res_partner.py:187; mail-thread from core:mail/models/res_partner.py:16): ADDS fields parent company, brand, store type, HQ flag, HQ-brand link, HQ-brand count; ADDS on-change resets and one validation: brand must belong to the chosen parent company (models/res_partner.py:97-108). No core method overridden.
- `sale.order` (core:sale/models/sale_order.py): ADDS parent company (editable), brand and store type (stored, read-only mirrors of the customer, models/sale_order.py:16-37). Overrides `create` (ADDS behavior before core: fills parent company from customer, models/sale_order.py:90-100) and `write` (ADDS: refreshes parent company when the customer changes, models/sale_order.py:102-107). On-change on parent company can blank the customer and restrict the customer list (models/sale_order.py:54-76). No effect on confirmation, pricing, invoicing, numbering.
- Because brand and store type on orders are stored mirrors of the customer, changing the customer's brand later re-labels existing (including confirmed) orders (models/sale_order.py:16-37); a migration also bulk-copies these values onto existing orders (migrations/19.0.1.4.4/post-migrate.py:15-21; migrations/19.0.1.4.7/post-migrate.py:15-21).
- Views: extends sale order form/list/search and partner form/list/search (views/sale_order_views.xml:9-104; views/res_partner_views.xml:5-81).
- Core controls: none blocked or altered (posting, lock dates, valuation, approvals, numbering). Record rules added are only on the module's own models. ALTERS CORE CONTROL: not found in code read. The credit limit on parent company is stored only; no code was found that enforces it on orders.

## 3. New objects, security, automation, external calls
- New models: bh.parent.company, bh.brand, bh.store.type (models/__init__.py:2-4). Sequence "PC" for parent-company code (data/ir_sequence_data.xml:5-13), created without company scoping (line 12).
- Groups: User and Manager under a new module category; Manager also assigned to the root and admin users by data (security/bh_parent_company_security.xml:11-30). Groups do not reference the category record.
- ACLs: read-only for User and for Sales salesman group; full rights for Manager on all three models (security/ir.model.access.csv:2-10).
- Record rules: multi-company rules on parent company and brand only (security/bh_parent_company_security.xml:33-43); no rule on store type although it stores a company (models/bh_store_type.py:45-51). Rules have no group restriction (apply to everyone).
- Cascade: archiving a brand archives its store types via elevated (sudo) write (models/bh_brand.py:99-108).
- Direct database schema/data scripts in migrations 19.0.1.2.0 to 19.0.1.4.7 (migrations/*/pre-migrate.py, post-migrate.py); they alter tables directly (column additions, dropping a not-null rule on brand, syncing order values). Not reproduced here.
- Crons: none. Server actions: none. External calls: none.

## 4. Odoo 19 compatibility
- Checked by grep in Community tree.
- `_sql_constraints` is used on all three models (models/bh_parent_company.py:134; models/bh_brand.py:83; models/bh_store_type.py:55). Community 19 logs it as no longer supported and asks for the constraint object (core:odoo/orm/model_classes.py:162-164). Mismatch: the uniqueness rules for parent-company code, brand code and store-type code are likely not created.
- `name_get` is overridden on all three models (models/bh_parent_company.py:151; models/bh_brand.py:138; models/bh_store_type.py:61). No `name_get` found in the Community 19 ORM; display name is `_compute_display_name` (core:odoo/orm/models.py:1438). Mismatch: the custom "[code] name" labels are likely not applied.
- `tracking=True` on fields of bh.store.type (models/bh_store_type.py:21,24,26,34) although the model has no chatter base (models/bh_store_type.py:13); effect not verified.
- Confirmed present in core 19: `res.users.group_ids` (core:base/models/res_users.py:257), `sales_team.group_sale_salesman`, views sale.view_quotation_tree_with_onboarding (core:sale/views/sale_order_views.xml:228), filters order_month/salesperson (lines 957-959), base.view_partner_tree and view_res_partner_filter, page `sales_purchases` (core:base/views/res_partner_views.xml:287).

## 5. Custom-to-custom dependencies
- None declared (depends: base, mail, contacts, sale_management, account; manifest:32-38).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the credit limit is enforced anywhere; only descriptive storage and a non-negative check were found (models/bh_parent_company.py:185-189).
- UNKNOWN - EVIDENCE INSUFFICIENT: total sales are summed without currency conversion across orders (models/bh_parent_company.py:170-173); behavior with mixed currencies is not established.
- UNKNOWN - EVIDENCE INSUFFICIENT: layout and permissions of the XML views for the three master models were skimmed only for menus/chatter, not fully read (views/bh_*_views.xml).
- UNKNOWN - EVIDENCE INSUFFICIENT: demo data content (demo/bh_parent_company_demo.xml) not read.
