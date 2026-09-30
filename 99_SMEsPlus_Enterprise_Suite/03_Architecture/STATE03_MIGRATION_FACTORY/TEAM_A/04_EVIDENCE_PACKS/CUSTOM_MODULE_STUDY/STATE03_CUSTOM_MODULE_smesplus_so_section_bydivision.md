> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: smesplus_so_section_bydivision

Module: smesplus_so_section_bydivision (name field in manifest equals the technical name)
License (confirmed in manifest): LGPL-3
Author (manifest): SMEsPlus
Version (manifest): 18.0.1.0.1 (manifest still carries the 18.0 series number; other 19 modules carry 19.0.x)
Path: addons_Extramodule/addons_extra/smesplus_so_section_bydivision
Source revision studied: workspace on-disk copy (not verified against upstream)
Classification (batch_07): Company Extra/Custom
Note: manifest dependencies are wider than the batch file said: sale, website_sale, website_sale_loyalty and product_brand_sale (__manifest__.py:1-23).

## 1. Business capability
- Automatically groups the lines of a sales order under one section header per division/brand of the product, and keeps sections and lines in that order (smesplus_so_section_bydivision/models/sale_order.py:8-34, 51).
- Removes section headers whose division no longer appears on any line (models/sale_order.py:13-15).
- Web shop: on the cart page, drops cart lines whose product has been archived, and hides section/note lines from the cart list (controller/main.py:12-58 in particular the archived-product cleanup; models/sale_order.py:68-70).

## 2. Attachment to CORE
- Core modules: sale, website_sale, website_sale_loyalty (present in Community 19). Non-core: product_brand_sale (not in the Community tree; two copies exist elsewhere in the workspace under addons_Extramodule/addons and addons_Extramodule/addons_extra; not opened for this study). The brand object comes from that module.
- sale.order (core:sale/models/sale_order.py:1042 for write): three overrides.
  - create (models/sale_order.py:36-40): ADDS behavior after core - rebuilds sections on the new orders.
  - write (models/sale_order.py:42-45): ADDS behavior after core, on EVERY write to an order, whatever the state - re-runs the section rebuild, which may create, delete and resequence lines. No state guard in module. This touches lines of confirmed orders; core protections for locked orders and line deletion still apply because the calls are ordinary ORM calls (core:sale/models/sale_order_line.py:1413-1426, 1464-1477), so the effect on confirmed/locked orders is "may raise a core error", not a bypass. Marked as touching a core control: ALTERS CORE CONTROL (order-line stability after confirmation) - by side effect only.
  - New method check_brand_section (models/sale_order.py:8).
- sale.order.line (core:sale/models/sale_order_line.py): new stored field brand_id "Division", computed from the product template brand (models/sale_order.py:51, 63-66); field sequence is REDECLARED as a plain integer without the core default of 10 (models/sale_order.py:52; core:sale/models/sale_order_line.py:38) - this REPLACES the core default (new lines get no default sequence value).
- website_sale line method _show_in_cart (models/sale_order.py:68-70; core:website_sale/models/sale_order_line.py:80-84): ADDS a section/note exclusion that core already contains.
- Controller: re-declares route /shop/cart in a class derived from the shop controller (controller/main.py:10-12) and REPLACES the whole cart page logic: abandoned-cart revive (merge/squash), archived product cleanup, suggested products, express payment values, popover variant (controller/main.py:12-58). The merge path cancels the abandoned order (controller/main.py, merge branch around 37-38).
- Multi-company, numbering, approvals, valuation: untouched.

## 3. New objects, security, automation, external calls
- New models: none. Security: none shipped. No cron / server action. No external call.
- Public web route touched (auth public, website) - it reads and changes the visitor's cart and, with an access token, an abandoned order via elevated access (controller/main.py:28 uses the elevated environment to find the order by token).

## 4. Odoo 19 compatibility - mismatches
- Core 19 defines /shop/cart in class Cart (core:website_sale/controllers/cart.py:18-21) with parameter revive_method; module uses parameter revive (controller/main.py:12) and derives from WebsiteSale (core:website_sale/controllers/main.py:133; controller/main.py:7, 10). Route collision / behavior with two handlers on the same path: not determined.
- The helper for express payment values is a method of the Cart class in core 19 (core:website_sale/controllers/cart.py:282); module calls it on its WebsiteSale-derived class (controller/main.py, express-values call near line 53). Presence on that class not confirmed.
- Section line creation passes field product_qty (models/sale_order.py:26-27); sale.order.line in Community 19 has no product_qty (core:sale/models/sale_order_line.py: no definition; only local variables in core:sale_stock/models/sale_order_line.py:141). Would fail on unknown-field creation unless another module adds it.
- Manifest version series 18.0 (not 19.0).
- Comment in controller mentions "new version" of the extra-values helper (controller/main.py, commented line near 48) - dead code.

## 5. Custom-to-custom dependencies
- product_brand_sale (third-party/custom brand module; not studied here). Field brand_id on product template and model product.brand are assumed from it (models/sale_order.py:51, 63).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: which module in the workspace supplies product_brand_sale for the active build (two copies exist).
- UNKNOWN - EVIDENCE INSUFFICIENT: runtime result of the section rebuild when lines have no division, when notes exist, or when the order is locked.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the module loads without error in Odoo 19 given the controller and field mismatches above.
