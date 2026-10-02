# U171 — product.pricelist: Pricing List Rule Computation and Price Override Chain
**Unit:** U171 | **Group:** G05 | **Priority:** P1 | **Status:** NOT_STUDIED → STUDIED
**Source tree:** Odoo 19.0 Community (odoo-19.0.post20260921) — READ-ONLY

---

## SOURCE FILES EXAMINED

| File | Purpose |
|------|---------|
| `odoo/addons/product/models/product_pricelist.py` | `product.pricelist` model — header fields, `_compute_price_rule()`, `_get_applicable_rules()`, partner/country resolution |
| `odoo/addons/product/models/product_pricelist_item.py` | `product.pricelist.item` — rule fields (`applied_on`, `compute_price`, `min_quantity`, dates), `_is_applicable_for()`, `_compute_price()`, `_compute_base_price()` |
| `odoo/addons/product/models/res_partner.py` | `res.partner` extension — `property_product_pricelist`, `specific_property_product_pricelist` |
| `odoo/addons/product/models/product_product.py` | `product.product._price_compute()` — base price fetch with currency for `list_price` / `standard_price` |
| `odoo/addons/sale/models/sale_order.py` | `sale.order.pricelist_id` field, `_compute_pricelist_id()` from partner |
| `odoo/addons/point_of_sale/models/pos_config.py` | `pos.config.pricelist_id`, `available_pricelist_ids`, company/currency constraints |

---

## CLAIM TABLE (22 claims)

| # | Claim | Source File | Key Symbol | Evidence Strength | Notes |
|---|-------|-------------|-----------|-------------------|-------|
| C01 | `product.pricelist` inherits `mail.thread` and `mail.activity.mixin`; tracked fields include `currency_id` (tracking=1) and `company_id` (tracking=5) | product_pricelist.py:11–46 | `_inherit`, `currency_id` tracking=1, `company_id` tracking=5 | CONFIRMED | Chatter and activity support built-in |
| C02 | `product.pricelist.item_ids` is a `One2many('product.pricelist.item', 'pricelist_id')` with a dynamic `domain` lambda filtering out items linked to archived products or templates | product_pricelist.py:58–64 | `item_ids`, `_base_domain_item_ids()`, `_domain_item_ids()` | CONFIRMED | Domain excludes inactive product/template items |
| C03 | `product.pricelist.company_id` is optional (not required), defaults to `env.company`; the search domain used in `_get_partner_pricelist_multi_search_domain_hook()` filters `company_id in [current_company, False]` — so a pricelist with company_id=False is visible to all companies | product_pricelist.py:43–47, 377–381 | `company_id` field, `_get_partner_pricelist_multi_search_domain_hook` | CONFIRMED | company_id is soft-scope, not a hard access-control gate |
| C04 | When `company_id` is changed on an existing pricelist (single record), `write()` calls `self.item_ids._check_company()` to validate all rules against the new company | product_pricelist.py:72–79 | `write()` + `_check_company()` | CONFIRMED | Cross-company rule validation enforced on company change |
| C05 | `product.pricelist.item` is the rule model; `_order = 'applied_on, min_quantity desc, categ_id desc, id desc'` — variant-level rules sort before product-level, which sort before category-level, which sort before global | product_pricelist_item.py:11–12 | `_order` | CONFIRMED | DB order determines rule precedence; most-specific first |
| C06 | `applied_on` selection: `'3_global'` (All Products), `'2_product_category'` (Product Category), `'1_product'` (Product template), `'0_product_variant'` (Product Variant); the string sort `'0' < '1' < '2' < '3'` means variant rules appear first in `_order` | product_pricelist_item.py:51–61 | `applied_on` selection | CONFIRMED | `_order applied_on` ascending sorts `0_product_variant` first |
| C07 | `compute_price` selection: `'fixed'` (fixed price), `'percentage'` (discount %), `'formula'` (formula with base+discount+surcharge+rounding+margins) | product_pricelist_item.py:106–114 | `compute_price` | CONFIRMED | Three pricing strategies |
| C08 | `min_quantity` (Float, default=0, digits='Product Unit') gates rule applicability — rule applies only when `qty_in_product_uom >= min_quantity`; 0 means no minimum | product_pricelist_item.py:43–49, 541–542 | `min_quantity`, `_is_applicable_for()` | CONFIRMED | Quantity threshold in product UoM |
| C09 | `date_start` / `date_end` are Datetime fields; `_get_applicable_rules_domain()` filters with `'|', ('date_start','=',False), ('date_start','<=',date)` and `'|', ('date_end','=',False), ('date_end','>=',date)` — both ends are inclusive and optional | product_pricelist.py:262–264 | `_get_applicable_rules_domain()` | CONFIRMED | Null-tolerant date range enforced at SQL domain level |
| C10 | `_compute_price_rule()` is the core mono-pricelist dispatcher: fetches applicable rules via `_get_applicable_rules()`, then iterates products — for each product finds the first matching rule via `rule._is_applicable_for(product, qty_in_product_uom)` and calls `rule._compute_price()` | product_pricelist.py:169–236 | `_compute_price_rule()` | CONFIRMED | First-match-wins per product |
| C11 | `_get_products_price()` is the batch wrapper: calls `_compute_price_rule(products, ...)` and returns `{product_id: price}` dict by discarding the rule id from each tuple | product_pricelist.py:90–110 | `_get_products_price()` | CONFIRMED | Batch pricing strips rule reference |
| C12 | `_get_product_price()` is the single-product wrapper: calls `_compute_price_rule(product, ...)` and returns `price` from the tuple; `_get_product_price_rule()` returns the full `(price, rule_id)` tuple; `_get_product_rule()` returns only `rule_id` via `compute_price=False` | product_pricelist.py:112–167 | Three wrapper methods | CONFIRMED | API surface clearly separated |
| C13 | UoM conversion: if `target_uom != product_uom`, quantity is converted to product UoM before rule applicability check (`qty_in_product_uom`); `_compute_price()` later converts fixed/surcharge back via `product_uom._compute_price(p, uom)` | product_pricelist.py:215–220; product_pricelist_item.py:596–599 | `qty_in_product_uom`, `convert` lambda | CONFIRMED | All rule thresholds expressed in product default UoM |
| C14 | For `compute_price='formula'`: formula = `base_price * (1 - discount/100)` then optional `price_round` (float_round), then `+ price_surcharge`, then `max(price, base + price_min_margin)`, then `min(price, base + price_max_margin)` | product_pricelist_item.py:606–622 | `_compute_price()` formula branch | CONFIRMED | Five-step formula pipeline; margins applied after surcharge |
| C15 | For `compute_price='percentage'`: price = `base_price * (1 - percent_price/100)`; negative `percent_price` creates a mark-up | product_pricelist_item.py:603–605 | `_compute_price()` percentage branch | CONFIRMED | Simple percentage discount/markup |
| C16 | `_compute_base_price()` resolves the base price from `base` field: `'list_price'` → `product.list_price + attribute extras` (currency = product.currency_id); `'standard_price'` → `product.standard_price` (currency = product.cost_currency_id); `'pricelist'` → recursively calls `base_pricelist_id._get_product_price()` (currency = base_pricelist_id.currency_id) | product_pricelist_item.py:628–659 | `_compute_base_price()` | CONFIRMED | Three base types; pricelist chaining supported |
| C17 | Multi-currency: after resolving `base_price` in `src_currency`, if `src_currency != currency` (the target pricelist's currency), `src_currency._convert(price, currency, self.env.company, date, round=False)` is called — company and date are passed for correct rate lookup | product_pricelist_item.py:656–658 | `src_currency._convert()` | CONFIRMED | Currency conversion always uses company context and date |
| C18 | Recursive pricelist chaining is prevented by `_check_pricelist_recursion()` constraint using DFS; raises `ValidationError` with full cycle path if detected | product_pricelist_item.py:321–352 | `_check_pricelist_recursion()` | CONFIRMED | DFS recursion guard at DB write time |
| C19 | `res.partner.property_product_pricelist` is a computed (non-stored) Many2one to `product.pricelist`; the inverse writes to `specific_property_product_pricelist` (company_dependent=True); computation delegates to `product.pricelist._get_partner_pricelist_multi()` | res_partner.py:14–36 | `property_product_pricelist`, `specific_property_product_pricelist`, `_compute_product_pricelist()` | CONFIRMED | Partner-pricelist assignment is company-context-aware |
| C20 | `_get_partner_pricelist_multi()` resolution order: (1) partner-specific `specific_property_product_pricelist` if active; (2) country-group-matching pricelist; (3) `ir.config_parameter` `res.partner.property_product_pricelist_{company_id}` (company fallback); (4) `res.partner.property_product_pricelist` (global fallback); (5) first active pricelist | product_pricelist.py:332–375 | `_get_partner_pricelist_multi()`, `_get_country_pricelist_multi()` | CONFIRMED | Five-level resolution with config-parameter fallback |
| C21 | `sale.order.pricelist_id` is computed (stored, precompute=True, readonly=False) from `partner_id.property_product_pricelist` via `_compute_pricelist_id()`; only recomputed when order is in `'draft'` state; domain restricts to same company or no company | sale_order.py:188–195, 444–452 | `pricelist_id` field + `_compute_pricelist_id()` | CONFIRMED | Pricelist locked once order is confirmed |
| C22 | `pos.config.pricelist_id` (default pricelist for session) and `available_pricelist_ids` (Many2many); constraint enforces: (a) default pricelist must be in available list; (b) all available pricelists must share the same currency as the POS company; (c) pricelist company_id must match POS company or be False | pos_config.py:139–142, 483–520 | `pricelist_id`, `available_pricelist_ids`, `_check_pricelists()` | CONFIRMED | POS enforces currency uniformity across pricelists |

---

## KEY ARCHITECTURAL NOTES

### Rule Selection Pipeline (per product in `_compute_price_rule()`):
1. `_get_applicable_rules()` fetches all rules from DB whose pricelist, product/category/template scope, and date range match — ordered by `applied_on` (variant first), `min_quantity desc`, `categ_id desc`, `id desc`.
2. For each product, iterate rules in DB order; first rule where `_is_applicable_for(product, qty)` returns True is selected (first-match-wins).
3. `_compute_price()` is called on the selected rule, returning the final price in the requested currency.

### Formula Rule Execution Order:
```
base_price → × (1 - discount/100) → round(price_round) → + price_surcharge
           → max(price, base + price_min_margin)
           → min(price, base + price_max_margin)
```
Rounding is applied **before** surcharge and margins.

### Pricelist Chaining (`base='pricelist'`):
- `_compute_base_price()` recursively calls the referenced pricelist's `_get_product_price()`.
- `_compute_price_before_discount()` traverses the chain to find the deepest percentage rule (used for discount display to customer).
- DFS cycle detection prevents infinite recursion.

### Partner Pricelist Assignment:
- `property_product_pricelist` on `res.partner` is a computed field; actual storage is in `specific_property_product_pricelist` (company_dependent=True).
- Country-group assignment allows geo-based pricing without per-partner configuration.

### Multi-Company Isolation:
- `product.pricelist.company_id` is optional; `company_id=False` pricelists are accessible by all companies.
- Rule items carry `company_id` (computed from pricelist company), with `_check_company_auto=True`.
- `_get_partner_pricelist_multi_search_domain_hook()` always restricts searches to `[current_company, False]`.

---

## FILES — ABSOLUTE PATHS

- `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/product/models/product_pricelist.py`
- `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/product/models/product_pricelist_item.py`
- `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/product/models/res_partner.py`
- `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/product/models/product_product.py`
- `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/sale/models/sale_order.py`
- `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/point_of_sale/models/pos_config.py`
