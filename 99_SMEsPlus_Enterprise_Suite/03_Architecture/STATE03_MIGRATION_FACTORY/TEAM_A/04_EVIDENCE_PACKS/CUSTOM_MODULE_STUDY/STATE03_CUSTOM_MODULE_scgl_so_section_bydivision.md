> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_so_section_bydivision

Module: scgl_so_section_bydivision
License (confirmed in manifest): LGPL-3 (scgl_so_section_bydivision/__manifest__.py:18)
Author (manifest): SCGL (scgl_so_section_bydivision/__manifest__.py:9)
Version (manifest): 18.0.1.0.1 (scgl_so_section_bydivision/__manifest__.py:3) - note: not a 19.0 version string
Path: addons_Extramodule/addons/scgl_so_section_bydivision
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Automatically groups sales-order lines under section headers named after the product's division/brand: for every brand present, a section line with that name is created (if missing) and the lines of that brand are renumbered beneath it (scgl_so_section_bydivision/models/sale_order.py:8-34).
- Section lines whose name is no longer a brand on the order are deleted (scgl_so_section_bydivision/models/sale_order.py:13-15).
- Runs after every order create and every order write (scgl_so_section_bydivision/models/sale_order.py:36-45).
- Adds a stored "Division" field on order lines, taken from the product template's brand (scgl_so_section_bydivision/models/sale_order.py:51, 63-66), and a hidden column for it (scgl_so_section_bydivision/views/sale_order_view.xml:9-11).
- Web shop: replaces the cart page handler so that inactive products are dropped from the cart (scgl_so_section_bydivision/controller/main.py:10-59).

## 2. Attachment to CORE
- sale.order (core:sale): overrides `create` and `write` (scgl_so_section_bydivision/models/sale_order.py:36-45). Both call core first (super), then ADD the section reorganisation. Because it runs on every write, it can rewrite sequence numbers and delete or create lines on any order state; core lock rules for confirmed orders are not consulted. Classified: ADDS behavior after core; potentially ALTERS CORE CONTROL (line edits on confirmed/locked orders and re-entrancy of write, since section creation triggers further writes) - effect on confirmed orders: UNKNOWN.
- sale.order.line: redeclares `sequence` (core:sale/models/sale_order_line.py:38 already defines it, default 10; here without default) (scgl_so_section_bydivision/models/sale_order.py:52). ADDS `brand_id` and method `compute_brand_id` (line 51, 63-66). Overrides `_show_in_cart` to hide section/note lines from the cart (scgl_so_section_bydivision/models/sale_order.py:68-70; core:website_sale/models/sale_order_line.py:80) - ADDS behavior after core.
- HTTP controller: subclass of core WebsiteSale defining route /shop/cart (scgl_so_section_bydivision/controller/main.py:10-13). It REPLACES the core cart logic with a copy of an older version: reads abandoned carts by access token alone (lines 27-40) - core now requires cart id plus token (core:website_sale/controllers/cart.py:39-40). ALTERS CORE CONTROL (access control for reviving abandoned carts; security relevant: token-only lookup with elevated read).
- Views: inherits `sale.view_order_form`, adds a hidden field after `product_template_id` (scgl_so_section_bydivision/views/sale_order_view.xml:6-11).

## 3. New objects, security, automation, external calls
- No new models, ACLs, record rules, groups, crons, server actions. No external calls.
- Public shop route (auth public, website=True) is re-declared (scgl_so_section_bydivision/controller/main.py:12).
- Company scoping: none added.

## 4. Odoo 19 compatibility
- Manifest version says 18.0 (scgl_so_section_bydivision/__manifest__.py:3).
- Mismatch: controller calls `request.website.sale_get_order()` (scgl_so_section_bydivision/controller/main.py:19, 22); no such method exists in Community 19 website/website_sale (grep of core:website, core:website_sale found none; core uses `request.cart`, core:website_sale/controllers/cart.py:35).
- Mismatch: the cart handler lives in class `Cart` in Community 19 (core:website_sale/controllers/cart.py:18-21), not in WebsiteSale (core:website_sale/controllers/main.py:133). The override extends WebsiteSale, so it does not replace the core method and may register a competing route; outcome UNKNOWN.
- Mismatch: template `website_sale.cart_popover` (scgl_so_section_bydivision/controller/main.py:57) not found in core:website_sale views (only in translation files). Helper `_get_express_shop_payment_values` is defined on `Cart` (core:website_sale/controllers/cart.py:282), not WebsiteSale.
- Mismatch: core cart parameter names are `id` / `revive_method` (core:website_sale/controllers/cart.py:21); this module uses `revive`.
- Fields `product_qty` on sale lines used when creating section rows (scgl_so_section_bydivision/models/sale_order.py:26): not verified for Community 19 - not checked.
- `brand_id` on product template and `product.brand` are not in Community core (grep of core:product, core:sale, core:website_sale found none); they come from a third-party brand module (product_brand_sale, declared dependency; scgl_so_section_bydivision/__manifest__.py:12-17).
- Uses removed name `tree` only in commented XML (scgl_so_section_bydivision/views/sale_order_view.xml:12-19).

## 5. Custom-to-custom dependencies
- No scgl_* module. Third-party/non-Community dependency: product_brand_sale (manifest lines 12-17). Core dependencies: sale, website_sale, website_sale_loyalty.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the rewriting on every write causes recursion, slowdown, or edits on confirmed/invoiced orders.
- UNKNOWN - EVIDENCE INSUFFICIENT: how orders with lines lacking a brand are handled (brand names list may contain empty entries; scgl_so_section_bydivision/models/sale_order.py:12).
- UNKNOWN - EVIDENCE INSUFFICIENT: which /shop/cart handler wins at runtime on Community 19.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the module installs on the target database (not run).
