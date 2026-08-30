> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 1 of 10 — Shared Master Dependency Learning
> All source paths relative to `ACCOUNT/01 ACCOUNT/SOURCE CODE/` unless stated otherwise. DB evidence pulled from a
> schema-only extraction (`pg_restore --schema-only`) of `ACCOUNT/01 ACCOUNT/iTEST02_2026-06-14_14-41-19.dump`, an
> Odoo-19-based source tree. Evidence IDs are unique per concept (PTY-, PRD-, CAT-, UOM-, PRC-, TAX-, PAY-, CUR-,
> SEQ-, WH-, CO-, AN-) and are cited to exact file+line or exact DB table/column.

# 01 — SHARED MASTER DEPENDENCY MAP

## 00 — Scope & Method

Researched only to the depth needed for GROUP A (Sales/Inventory/Purchase) dependency, per the New Prompt Governance
v1.1 scope. Not a redesign of Wave 1 (Shared Business Master); not a redesign of Wave 3 (Accounting Core, already
researched separately in `DOMAIN_01_ACCOUNTING_CORE/`).

- Source tree mixes three layers: `02 OTHER/<module>/models/*.py` (stock Odoo apps: base, product, uom, sale,
  purchase, stock, analytic), `01 ACCOUNT/<module>/models/*.py` (Odoo Accounting-line modules), and
  `addons_extra/<module>/` (SMEsPlus/ACSONE/OCA/third-party custom modules — most business-specific coupling and
  all Thailand-localization logic lives here).
- DELTA-FIRST: checked `DOMAIN_01_ACCOUNTING_CORE/` research before reading fresh source for Tax Master / Payment
  Terms. Conclusion: Accounting Core explicitly deferred tax/payment-term source reads (only column-count/FK facts
  existed) — nothing to reuse; everything below on Tax/Payment Terms is freshly derived.
- Every claim below is either cited to an exact file+line this pass actually read, an exact DB table/column found
  in the schema extraction, or marked `EVIDENCE_MISSING` / `UNKNOWN`. Nothing is invented to fill a gap.

## 01 — Rollup Index

| # | Concept | Model(s) | Company-scoped? | GROUP A coupling | Confidence |
|---|---|---|---|---|---|
| 1 | Party | `res.partner`, `res.partner.category` | Optional (nullable `company_id`) | Sale (customer), Purchase (vendor), Stock (owner/dest) — all direct | VERIFIED FACT, some DB columns EVIDENCE_MISSING |
| 2 | Product/Service | `product.template`, `product.product` | Optional (template only) | Sale, Purchase, Stock — all direct | VERIFIED FACT, some DB columns EVIDENCE_MISSING |
| 3 | Product Category | `product.category`, `product.brand` | None (no `company_id`) | Stock direct; Sale/Purchase only transitively via product | VERIFIED FACT |
| 4 | UOM | `uom.uom` (self-referential; no `uom.category`) | None (global) | Sale, Purchase, Stock — all direct | VERIFIED FACT |
| 5 | Pricing/Pricelist | `product.pricelist`, `product.pricelist.item` | Optional | **Sale only — Purchase has no pricelist field at all** | VERIFIED FACT |
| 6 | Tax Master | `account.tax`, `account.tax.group` | Required (`company_id` NOT NULL) | Sale & Purchase, via two different product fields (`taxes_id` vs `supplier_taxes_id`) | VERIFIED FACT; fiscal-position base model EVIDENCE_MISSING |
| 7 | Payment Terms | `account.payment.term(.line)` | Optional | Sale & Purchase, via two different partner properties | VERIFIED FACT |
| 8 | Currency/Rate | `res.currency`, `res.currency.rate` | Currency: none; Rate: optional, root-company only | Sale (from pricelist), Purchase (from vendor property) — different default chains | VERIFIED FACT |
| 9 | Sequence | `ir.sequence` | Optional | Sale (`sale.order` code), Purchase (`purchase.order` code) — inconsistent fallback sentinel | VERIFIED FACT; CONFLICT noted |
| 10 | Warehouse/Location (master only) | `stock.warehouse`, `stock.location` | Warehouse: required+immutable; Location: optional | Only via `sale_stock`/`purchase_stock` bridge modules, not base sale/purchase | VERIFIED FACT |
| 11 | Company/Branch | `res.company` (+ Thai `branch` addons) | n/a | Sale & Purchase both call `_accessible_branches()` | VERIFIED FACT; Thai branch duplication CONFLICT |
| 12 | Analytic/Dimension | `account.analytic.account/.plan` | Plan: none; Account: optional; Line: required | Sale & Purchase — both use identical `analytic.mixin` | VERIFIED FACT |

---

# 02 — PARTY (Customer / Supplier / Contact) — `res.partner`

## Source-evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PTY-01 | `02 OTHER/base/models/res_partner.py` | L184–192 | `class ResPartner`, `_name='res.partner'`, `_description='Contact'` — one model for every party role (customer, vendor, contact, employee, company). `_inherit=['format.address.mixin','format.vat.label.mixin','avatar.mixin','properties.base.definition.mixin']`, `_check_company_auto=True` |
| PTY-02 | `02 OTHER/base/models/res_partner.py` | L213–217 | `name`, `complete_name` (computed+stored), `parent_id` (Many2one **self**, "Related Company"), `child_ids` (One2many self) — hierarchical company→contact structure |
| PTY-03 | `02 OTHER/base/models/res_partner.py` | L249–250 | `category_id` — Many2many to `res.partner.category`, label "Tags" |
| PTY-04 | `02 OTHER/base/models/res_partner.py` | L254–260 | `type` selection: `contact`/`invoice`/`delivery`/`other` ("Address Type") — one company record carries multiple addressed sub-contacts via `parent_id` + `type` |
| PTY-05 | `02 OTHER/base/models/res_partner.py` | L277–284 | `is_company` boolean; `company_type` selection person/company is explicitly commented `# company_type is only an interface field, do not use it in business logic` |
| PTY-06 | `02 OTHER/base/models/res_partner.py` | L285 | `company_id` — Many2one `res.company`, `index=True` — the multi-company scoping field (nullable = shared/global partner) |
| PTY-07 | `02 OTHER/base/models/res_partner.py` | L302–305 | `commercial_partner_id` — computed, `store=True`, `recursive=True` — groups delivery/invoice sub-contacts under one commercial/billing entity |
| PTY-08 | `02 OTHER/base/models/res_partner.py` | L326–329 | `_check_name` — real DB CHECK, matches `res_partner_check_name` in schema |
| PTY-09 | `02 OTHER/base/models/res_partner.py` | L139–154 | `class ResPartnerCategory` (`res.partner.category`, "Partner Tags") lives **inside** `res_partner.py` |
| PTY-10 | `02 OTHER/base/models/res_partner.py` | L156–159 | `_check_parent_id` — recursion guard via `_has_cycle()` on partner tags |
| PTY-11 | `02 OTHER/base/models/res_partner.py` | L1245–1251 | `class ResPartnerIndustry` (`res.partner.industry`) — separate flat classification |
| PTY-12 | `02 OTHER/base/models/res_bank.py` | L73–76 | `res.partner.bank` ("Bank Accounts") — file named `res_bank.py` |
| PTY-13 | `02 OTHER/sale/models/res_partner.py` | L10–16 | GROUP A/Sales: `sale_order_count`, `sale_order_ids` One2many `sale.order` |
| PTY-14 | `02 OTHER/sale/models/res_partner.py` | L83–110 | `_compute_credit_to_invoice` — cross-module (sale+account) credit-limit coupling on the party |
| PTY-15 | `02 OTHER/purchase/models/res_partner.py` | L31–45 | GROUP A/Purchase: `property_purchase_currency_id`, `purchase_order_count`, `buyer_id` |
| PTY-16 | `02 OTHER/stock/models/res_partner.py` | L11–18 | GROUP A/Stock: `property_stock_customer`/`property_stock_supplier` — Many2one `stock.location`, per-company routing lives on the partner |
| PTY-17 | `addons_extra/l10n_th_partner/models/res_partner.py` | L15 | `branch = fields.Char(string="Tax Branch", ...)` — Thai Revenue-Department tax-branch identifier, a **legal/VAT concept**, not operational site |
| PTY-18 | `addons_extra/l10n_th_partner/models/res_partner.py` | L16–57 | `name_company` + Thai legal-entity naming composition (prefix/suffix) |
| PTY-19 | `addons_extra/partner_company_type/models/res_partner.py` | L7–21 | `partner_company_type_id` ("Legal Form") + `title` — further extended by `l10n_th_partner` |
| PTY-20 | `addons_extra/product_brand_sale/models/res_partner.py` | L9–19 | `product_brand_ids` M2M `product.brand` ("Divisions") on `res.partner` — ties Party to Product-classification layer |
| PTY-21 | `schema_only.sql` L40396–40538 | DDL | `res_partner`: ~135 columns. Confirms `company_id` (PTY-06); many bespoke columns have **no matching `.py` field definition anywhere in the scanned tree**: `brand_id`, `parent_company_id`, `bh_parent_company_code`, `is_hq_brand`, `hq_brand_id`, `hq_brand_count`, `store_type_id`, plus 13 `x_studio_*` columns |
| PTY-22 | `schema_only.sql` L114560–114572 | DDL | `res_partner_category`: 10 columns, **no `company_id`** — tags are global |

## Synthesis — PARTY

- **Business purpose**: single unified "party" record for every external/internal actor an SME deals with —
  customer, vendor, contact, delivery/invoice sub-address, company. Customer/Supplier are not distinct entities;
  both are `res.partner` rows distinguished by usage and by `customer_rank`/`supplier_rank` DB counters whose
  owning `.py` definition was **not found** (expected `01 ACCOUNT/account/models/res_partner.py` does not exist in
  this tree).
- **Actor / maintainer / consumer**: Sales, Purchasing, Accounting back-office users; consumed by `sale.order`,
  `purchase.order`, `stock.picking`/`stock.move`/`stock.quant`, and Thai VAT-branch localisation modules.
- **Source owner observation**: `res.partner` is the most heavily extended model in the tree (~190 `_inherit`
  files). GROUP A modules each add a thin, well-scoped slice — clean extension pattern. The SMEsPlus/Thai
  `addons_extra` layer additionally reshapes identity/naming and adds a Division classification directly on the
  partner (PTY-20), which is unusual (Division/brand access-control is normally product-side).
- **GROUP A consumers (citations)**: Sales `sale/models/sale_order.py` L64–69 (`partner_id`, Customer, required);
  Purchase `purchase/models/purchase_order.py` L92/L95 (Vendor, dest_address_id) and
  `purchase_order_line.py` L84 (related); Stock `stock_move.py` L94/L164, `stock_picking.py` L624/L632/L652,
  `stock_quant.py` L75.
- **Company/warehouse/branch context**: `company_id` (PTY-06) is the real multi-company scoping field. **No
  dedicated warehouse/branch FK** on `res.partner`. `branch` (PTY-17) is a Thai tax-branch string, not an
  operational site. DB carries `parent_company_id`/`brand_id`/`hq_brand_id`/`is_hq_brand`/`store_type_id` columns
  suggesting a real multi-brand/multi-HQ retail structure was layered on — **no source file found**, EVIDENCE_MISSING.
- **Database evidence**: `res_partner` key columns confirmed: `id, company_id, name, parent_id,
  commercial_partner_id, type, is_company, vat, credit_limit(jsonb), property_account_payable_id(jsonb),
  property_account_receivable_id(jsonb), property_payment_term_id(jsonb), supplier_rank, customer_rank,
  property_stock_customer(jsonb), property_stock_supplier(jsonb), buyer_id, branch, name_company,
  partner_company_type_id, parent_company_id, brand_id, is_hq_brand, hq_brand_id, store_type_id,
  bh_parent_company_code` + 13 `x_studio_*` columns (PTY-21). `res_partner_category`: `id, color, parent_id,
  name(jsonb), active` — no `company_id` (PTY-22).
- **Source-specific coupling (flag, do not copy)**: (1) `jsonb`-typed `property_*` columns are Odoo's
  `company_dependent` storage trick, not a relational pattern. (2) `company_type` explicitly **not for business
  logic** (PTY-05). (3) Two independent custom modules (`partner_company_type`, `l10n_th_partner`) both extend the
  same `_compute_name()` in a layered/`super()`-chained way — fragile MRO-order-dependent naming.
- **Confidence**: VERIFIED FACT for PTY-01…PTY-20, PTY-22. SUPPORTED INFERENCE for the "multi-brand/multi-HQ"
  reading of unexplained DB columns.
- **Unknown / Conflict**: `customer_rank`/`supplier_rank`/`property_account_receivable_id`/`property_account_payable_id`
  are real DB columns with no located owning `.py` definition — **EVIDENCE_MISSING**. `brand_id`,
  `parent_company_id`, `bh_parent_company_code`, `is_hq_brand`, `hq_brand_id`, `hq_brand_count`, `store_type_id` —
  full-tree grep found no `fields.*` definitions; likely Odoo-Studio-authored — **EVIDENCE_MISSING**.

---

# 03 — PRODUCT / SERVICE — `product.template` / `product.product`

## Source-evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PRD-01 | `02 OTHER/product/models/product_template.py` | L18–21 | `class ProductTemplate`, `_name='product.template'` |
| PRD-02 | product_template.py | L54–65 | `type` selection: `consu` (Goods) / `service` / `combo` — required, default `consu`. This is the Product/Service split |
| PRD-03 | product_template.py | L81–86 | `categ_id` — Many2one `product.category`, `group_expand='_read_group_categ_id'` |
| PRD-04 | product_template.py | L94–106 | `list_price` (Sales Price) vs `standard_price` (Cost, `groups="base.group_user"`) — separate, cost access-restricted |
| PRD-05 | product_template.py | L116–121 | `sale_ok`/`purchase_ok` booleans; `uom_id` required — **one single uom_id**, no separate purchase-UoM field |
| PRD-06 | product_template.py | L122 | `uom_ids` M2M `uom.uom`, "Packagings" for sale |
| PRD-07 | product_template.py | L124–127 | `company_id` nullable (shared across companies); `seller_ids` One2many `product.supplierinfo` |
| PRD-08 | product_template.py | L144–152 | `product_variant_ids` One2many `product.product` (required) — template/variant split |
| PRD-09 | `02 OTHER/stock/models/product.py` | L813–822 | GROUP A/Stock: `is_storable` boolean, "Track Inventory" |
| PRD-10 | stock/models/product.py | L894–895 | `compute_is_storable`: forces `False` whenever `type != 'consu'` — services/combos never stock-tracked |
| PRD-11 | `02 OTHER/product/models/product_product.py` | L16–20 | `class ProductProduct`, `_description="Product Variant"` |
| PRD-12 | product_product.py | L39–48 | `product_tmpl_id` (required, cascade), `barcode`, `default_code` — variant-level identity |
| PRD-13 | `02 OTHER/product/models/product_uom.py` | L8–18 | `product.uom` — join of `uom_id`+`product_id`+`barcode`(unique)+`company_id` — separate barcode-per-packaging table |
| PRD-14 | `02 OTHER/product/models/product_supplierinfo.py` | L7–49 | `product.supplierinfo` — `partner_id`+`product_id`/`product_tmpl_id`+`product_uom_id`+`price`/`currency_id`/`company_id`/`min_qty`/`delay` — joins **Party + Product + UOM** for vendor-specific pricing/lead-time |
| PRD-15 | `addons_extra/product_variant_reference/models/product_product.py` | L13–58 | SMEsPlus override: `default_code` computed/stored from `product_tmpl_id.name` + attribute values |
| PRD-16 | `addons_extra/product_sequence/models/product_template.py` | L7–22 | **Second, independent** SMEsPlus module also writing `default_code`, from `categ_id.seq_id.next_by_id()` |
| PRD-17 | `schema_only.sql` L97042–97154 | DDL | `product_template`: 112 columns. Confirms `company_id`, `categ_id`, `uom_id NOT NULL`, `type`, `is_storable`, plus unexplained: `code`, `part_thickness`, `part_length`, `part_type_wi`, `part_code_id`, `product_revise_id`, `holding_conditions`, `min_qty`, `max_qty`, `*_filename` cols |
| PRD-18 | `schema_only.sql` L95780–95805 | DDL | `product_product`: 21 columns — **no `company_id`, no `uom_id`, no `categ_id`** — confirms template/variant split at DB level |

## Synthesis — PRODUCT / SERVICE

- **Business purpose**: sellable/purchasable/stockable "thing" — goods, services, or bundles ("combo"). One
  template can have many variants via `product.product`; most business fields live on the template.
- **Actor / maintainer / consumer**: Purchasing/Product-Data-Management; consumed by `sale.order.line`,
  `purchase.order.line`, `stock.move`, `stock.quant`, `product.supplierinfo`.
- **Source owner observation**: Product/Service is a plain `type` selection, not two models — a service simply
  cannot be `is_storable`. **Two independent, uncoordinated SMEsPlus customizations both write `default_code`**
  (PRD-15 attribute-based, PRD-16 category-sequence-based) — a genuine collision risk.
- **GROUP A consumers (citations)**: Sales `sale_order_line.py` L83–102; Purchase `purchase_order.py` L156,
  `purchase_order_line.py` L37; Stock `stock_move.py` L40/L73, `stock_quant.py` L46/L50, `stock_picking.py` L675.
- **Company/warehouse/branch context**: `company_id` on template nullable (global-or-company-specific); variant
  carries no `company_id` of its own. No warehouse/branch field on either model.
- **Database evidence**: see PRD-17/PRD-18.
- **Source-specific coupling (flag, do not copy)**: (1) `standard_price` ACL-gated (Odoo groups mechanism, not
  data model). (2) Dual `default_code`-writer conflict (PRD-15/16) is a defect pattern, not worth preserving. (3)
  `product.uom` (PRD-13) and `uom.uom`'s own packaging hierarchy (UOM-10 below) are two overlapping mechanisms for
  "alternate unit with a barcode."
- **Confidence**: VERIFIED FACT for PRD-01…PRD-16, PRD-18. SUPPORTED INFERENCE that unexplained columns
  (`part_thickness`, `holding_conditions`, etc.) reflect a manufacturing/cold-chain vertical — inferred from names only.
- **Unknown / Conflict**: owning source for `product_template` columns `code`, `part_thickness`, `part_length`,
  `part_type_wi`, `part_code_id`, `product_revise_id`, `holding_conditions`, `min_qty`, `max_qty`, `*_filename` —
  **EVIDENCE_MISSING**.

---

# 04 — PRODUCT CATEGORY / CLASSIFICATION — `product.category` (+ `product.brand`)

## Source-evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| CAT-01 | `02 OTHER/product/models/product_category.py` | L8–16 | `product.category`, `_parent_store=True`, `_rec_name='complete_name'` |
| CAT-02 | product_category.py | L17–27 | `complete_name` (recursive, stored), `parent_id` (self, cascade), `product_properties_definition` (dynamic per-category attributes) |
| CAT-03 | product_category.py | L29–35 | `_compute_complete_name` builds "Parent / Child" path — real hierarchical category |
| CAT-04 | product_category.py | L46–49 | `_check_category_recursion` via `_has_cycle()` |
| CAT-05 | product_category.py | L37–44 | `_compute_product_count` rolls up the whole subtree |
| CAT-06 | `02 OTHER/stock/models/product.py` | L1274–1302 | GROUP A/Stock: `route_ids`, `removal_strategy_id` (FIFO/LIFO/Closest/FEFO/Least-Packages), `putaway_rule_ids`, `packaging_reserve_method` — category is a first-class inventory-policy carrier |
| CAT-07 | `addons_extra/product_category_filter/models/category.py` | L8–17 | SMEsPlus custom: `show_on_product` boolean — categories can be hidden from selection while still existing |
| CAT-08 | `addons_extra/product_sequence/models/product_category.py` | L4–14, L49–77 | SMEsPlus custom: `seq_id` ties a category to an `ir.sequence`; `create`/`write` provisions/renames it |
| CAT-09 | `addons_extra/product_brand_sale/models/brand.py` | L66–98 | `product.brand` ("Division") — separate flat model: `name`, `code` ("SAP Code"), `warehouse_id` Many2one `stock.warehouse` |
| CAT-10 | brand.py | L12–64 | `product.brand` drives website/portal filtering — a data-visibility/tenancy boundary, not just reporting |
| CAT-11 | `schema_only.sql` L94102–94128 | DDL | `product_category`: 20 columns — `property_*`(jsonb), `removal_strategy_id`, `seq_id`, etc. **No `company_id` column.** |

## Synthesis — PRODUCT CATEGORY / CLASSIFICATION

- **Business purpose**: hierarchical grouping for (a) accounting defaults, (b) inventory policy defaults (removal
  strategy, routes, putaway), (c) reporting/UI grouping. A second, unrelated, flat classification (`product.brand`,
  "Division") exists in parallel for commercial/portal segmentation.
- **Actor / maintainer / consumer**: Product-Data-Management/Finance (accounting property defaults), Inventory Ops
  (removal strategy/routes).
- **Source owner observation**: `product.category` does three structurally different jobs simultaneously —
  classification taxonomy, inventory-policy template, and (via `product_sequence`) an **SKU-numbering authority**
  that directly conflicts with PRD-15's attribute-based SKU generator. `product.brand` is orthogonal — should not
  be conflated with `product.category`.
- **GROUP A consumers (citations)**: only Stock extends `product.category` directly (CAT-06). Sales/Purchase reach
  category only transitively through the product record.
- **Company/warehouse/branch context**: **NONE FOUND** — no `company_id` on `product_category` (global across
  companies). `product.brand` carries a single `warehouse_id` (1:1-ish, unusual) — not company-scoped.
- **Database evidence**: CAT-11.
- **Source-specific coupling (flag, do not copy)**: (1) accounting property fields = Odoo `company_dependent`
  jsonb mechanism. (2) category-owned SKU sequence (CAT-08) conflicts with PRD-15 — two sources of truth for one
  identifier. (3) `product.brand` mixing classification with portal access control.
- **Confidence**: VERIFIED FACT for CAT-01…CAT-11.
- **Unknown / Conflict**: `product.brand`'s own DB table was not independently confirmed against the schema in
  this pass — model verified from source, DB shape **EVIDENCE_MISSING**.

---

# 05 — UOM (Unit of Measure) — `uom.uom`

## Source-evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| UOM-01 | `02 OTHER/uom/models/uom_uom.py` | L17–22 | `uom.uom`, `_parent_name='relative_uom_id'` — hierarchy is **self-referential**, not grouped by a separate category model |
| UOM-02 | uom_uom.py | L34–44 | `relative_factor`, `relative_uom_id` (self, "Reference Unit"), `factor` (computed, recursive, stored, "Absolute Quantity") |
| UOM-03 | uom_uom.py | L46–49 | `_factor_gt_zero` CHECK, confirmed in schema |
| UOM-04 | uom_uom.py | L69–75 | `_compute_factor`: `factor = relative_factor * relative_uom_id.factor` — recursive up the tree |
| UOM-05 | uom_uom.py | L97–101 | root unit's `relative_factor` must be exactly `1.0` |
| UOM-06 | uom_uom.py | L24–32, L105–112 | Protected "master data" UoMs cannot be deleted, only archived |
| UOM-07 | uom_uom.py | L116–137 | `round()`/`compare()`/`is_zero()` all use ONE shared `'Product Unit'` decimal-precision record — same rounding for every UoM regardless of what it measures |
| UOM-08 | uom_uom.py | L147–176 | `_compute_quantity`: `amount = qty * self.factor / to_unit.factor` — purely arithmetic; no visible hard incompatible-category guard in this excerpt |
| UOM-09 | uom_uom.py | L218–230 | `_has_common_reference`: compares `parent_path` — the actual runtime replacement for the old `uom.category` grouping |
| UOM-10 | `02 OTHER/stock/models/product.py` | L1338–1342 | GROUP A/Stock: `package_type_id` on `uom.uom` — physical packaging is a `uom.uom` row, not a separate model |
| UOM-11 | stock/models/product.py | L1344–1372 | `write()` override: conversion ratio **immutable once transacted** (blocked if any non-cancel/done stock.move/quant references it) |
| UOM-12 | `02 OTHER/product/models/uom_uom.py` | L8–19 | GROUP A/Product: `product_uom_ids` One2many `product.uom` ("Barcodes") |
| UOM-13 | `02 OTHER/product/models/product_uom.py` | L8–18 | Separate `product.uom` model — a **second**, distinct packaging mechanism coexisting with UOM-10 |
| UOM-14 | `addons_extra/smesplus_uom_ext/models/uom_uom.py` | L3–31 | SMEsPlus custom `get_lower_uom()`/`get_upper_uom()`/`get_same_group_uoms()` — re-derives "same conversion family" because there is no `uom.category` table |
| UOM-15 | `addons_extra/smesplus_uom_ext/models/product_supplierinfo.py` | L3–13 | `filter_uom` on `product.supplierinfo` directly consumes UOM-14's grouping logic |
| UOM-16 | `02 OTHER/sale/models/sale_order_line.py` | L132–138 | GROUP A/Sales: `product_uom_id`, `allowed_uom_ids` |
| UOM-17 | `02 OTHER/purchase/models/purchase_order_line.py` | L35–37 | GROUP A/Purchase: `allowed_uom_ids` + `product_uom_id` |
| UOM-18 | `02 OTHER/stock/models/stock_move.py` | L66–68, L194 | GROUP A/Stock: `product_uom` + `packaging_uom_id` |
| UOM-19 | `02 OTHER/stock/models/stock_quant.py` | L46–53 | GROUP A/Stock: `product_id`, `product_tmpl_id`, `uom_id` |
| UOM-20 | `schema_only.sql` L102188–102203 | DDL | `uom_uom`: `id, sequence, relative_uom_id, parent_path, name(jsonb), relative_factor NOT NULL, factor, active, package_type_id, timesheet_widget`. **No `category_id` column.** |
| UOM-21 | `schema_only.sql` — searched, absent | DDL | `grep "CREATE TABLE public.uom_category"` → **zero matches** — no `uom_category` table exists in the DB at all |
| UOM-22 | `02 OTHER/uom/i18n/*.po` (sample) | multiple | Shipped translation files still reference `uom.model_uom_category`/`uom.field_uom_uom__category_id` — **stale artifacts** contradicted by both source and DB |

## Synthesis — UOM

- **Business purpose**: defines the unit a product is counted/measured/sold in and how to convert between related
  units for stock, sales, and purchase quantities.
- **Actor / maintainer / consumer**: centrally maintained (Product/Inventory admin); consumed by every
  quantity-bearing line.
- **Source owner observation**: the most structurally distinctive concept in this cluster. Instead of the classic
  two-model design (category + members), `uom.uom` is self-referential — "same category" is now an emergent tree
  property (UOM-09), not an explicit FK. Physical packaging is just another `uom.uom` node (UOM-10), while a
  **second, independent** packaging/barcode mechanism (`product.uom`, UOM-13) also exists. The SMEsPlus
  `smesplus_uom_ext` add-on (UOM-14/15) exists specifically to paper over the loss of `uom.category` — real
  evidence that downstream logic still needs that old grouping concept even though the model was removed upstream.
- **GROUP A consumers (citations)**: Sales UOM-16, Purchase UOM-17, Stock UOM-18/UOM-19. All three constrain
  `uom_id` to a computed `allowed_uom_ids` domain rather than trusting `uom.uom` centrally.
- **Company/warehouse/branch context**: **NONE FOUND** — no `company_id` on `uom_uom` (global).
- **Database evidence**: UOM-20, UOM-21.
- **Source-specific coupling (flag, do not copy)**: (1) immutability guard (UOM-11) enforced in application code
  via ad-hoc searches, not a DB constraint. (2) single shared decimal-precision setting (UOM-07) — an Odoo
  global-settings simplification. (3) two coexisting packaging representations (UOM-10 vs UOM-13) is duplication
  specific to this codebase's evolution.
- **Confidence**: VERIFIED FACT for UOM-01…UOM-21. SUPPORTED INFERENCE for "no hard incompatible-category guard"
  (UOM-08) — only the shown method body was read.
- **Unknown / Conflict**: **CONFLICT** — `.po` translation files (UOM-22) describing a `uom.category` model are
  directly contradicted by both `.py` source and the live DB schema, which agree with each other. Treat `.po`
  files as unreliable evidence of current model shape.

## Cross-concept note (Party+Product+UOM)

`product.supplierinfo` (PRD-14) is the one model that structurally joins all three shared masters at once:
`partner_id` (Party/Vendor) + `product_id`/`product_tmpl_id` (Product) + `product_uom_id` (UOM), scoped by
`company_id`/`currency_id`.

---

# 06 — PRICING / PRICELIST

## Source evidence

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PRC-01 | `02 OTHER/product/models/product_pricelist.py` | L9–14 | `product.pricelist` model, ordered `sequence, id, name` |
| PRC-02 | product_pricelist.py | L36–41 | `currency_id` required, defaults to `env.company.currency_id` |
| PRC-03 | product_pricelist.py | L43–47 | `company_id` nullable (global pricelist allowed) |
| PRC-04 | product_pricelist.py | L58–64 | `item_ids` One2many `product.pricelist.item` |
| PRC-05 | product_pricelist.py | L169–236 | `_compute_price_rule`: multi-product pricing engine; currency falls back to company; converts qty into product UoM before rule matching |
| PRC-06 | product_pricelist.py | L239–264 | `_get_applicable_rules_domain`: filters by product/template/category AND `date_start`/`date_end` window |
| PRC-07 | `product_pricelist_item.py` | L8–12 | `product.pricelist.item` ("Pricelist Rule"), ordered `applied_on, min_quantity desc, categ_id desc, id desc` — most specific rule wins |
| PRC-08 | product_pricelist_item.py | L51–61 | `applied_on`: `3_global`/`2_product_category`/`1_product`/`0_product_variant` — rule scope hierarchy |
| PRC-09 | product_pricelist_item.py | L91–135 | `base` + `compute_price` (percentage/formula/fixed) + `fixed_price`/`percent_price`/`price_discount`/`price_round`/`price_surcharge`/margin clamps |
| PRC-10 | product_pricelist_item.py | L513–555 | `_is_applicable_for`: gates by `min_quantity` then scope match |
| PRC-11 | product_pricelist_item.py | L557–613 | `_compute_price`: fixed → percentage → formula+rounding+surcharge+margin clamps, in that literal order |
| PRC-12 | product_pricelist_item.py | L615–646 | `_compute_base_price`: base = another pricelist (recursive) OR `standard_price` OR `list_price`; cross-currency conversion when needed |
| PRC-13 | product_pricelist_item.py | L321–339 | `_check_pricelist_recursion`: DFS guard against self-chaining |
| PRC-14 | product_pricelist_item.py | L316–319 | `_check_base_pricelist_id` |
| PRC-15 | product_pricelist.py | L334–375 | `_get_partner_pricelist_multi`: resolution order = partner-specific → country-group → generic fallback → first available |

## GROUP A consumption (Sale / Purchase)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PRC-16 | `sale/models/sale_order.py` | L187–194 | `pricelist_id`, stored+precompute; changing it only affects newly added lines |
| PRC-17 | sale_order.py | L443–451 | `_compute_pricelist_id`: defaults from `partner_id.property_product_pricelist` |
| PRC-18 | sale_order.py | L453–456 | `_compute_currency_id`: **order currency derives from pricelist currency** — pricelist is the primary currency driver on Sale |
| PRC-19 | sale_order.py | L1039–1040 | `write()` guard: `UserError` if `pricelist_id` changed on a confirmed order |
| PRC-20 | `sale/models/sale_order_line.py` | L173–175, L574–584 | `pricelist_item_id` caches the matched rule per line |
| PRC-21 | sale_order_line.py | L667, L685, L727 | Line price resolved via the matched rule object, not the pricelist header |
| PRC-22 | `purchase/models/purchase_order.py` | whole-file grep | **No `pricelist_id` field exists on `purchase.order`.** `product.pricelist` is not used by Purchase. |
| PRC-23 | `purchase/models/purchase_order_line.py` | L96 | `selected_seller_id` → `product.supplierinfo` — informal "pricelist" here means vendor-specific pricing, a different model |
| PRC-24 | `02 OTHER/product/models/product_supplierinfo.py` | L10, L27–38 | `product.supplierinfo`: `min_qty`/`price`/`currency_id` — vendor price-break list, structurally parallel but separate from `product.pricelist` |
| PRC-25 | purchase_order_line.py | L434–462 | Purchase unit price: no seller → cost-based conversion; seller found → seller price converted to PO currency — **no pricelist rule engine involved** |

## Synthesis — PRICING

- **Business purpose**: rule-based sale-price derivation (discount/formula/fixed) scoped by product/category/
  variant, qty break, validity window, and currency.
- **Actor / maintainer / consumer**: pricing/sales admin maintains rules; consumed at quotation-line creation.
  **Purchase does not consume it at all.**
- **Source owner observation**: header (`product.pricelist`) is near-metadata; pricing math lives entirely in
  `product.pricelist.item`. "Pricelist" is a rule-tree, not a literal price list.
- **GROUP A consumers (cited)**: Sale only (PRC-16..21). Purchase uses a structurally analogous but architecturally
  absent-of-pricelist concept (`product.supplierinfo`, PRC-22..25) — **do not assume Purchase inherits Pricelist.**
- **Company/warehouse/branch context**: `product_pricelist.company_id` nullable; `product_pricelist_item.company_id`
  is a stored compute derived from pricelist/product, not independently settable. **NONE FOUND** for warehouse/branch.
- **Database evidence**: `product_pricelist`: `id, sequence, currency_id NOT NULL, company_id, name(jsonb) NOT NULL,
  active, website_id, code, selectable` (last three not in base `.py` — added by an unopened module, likely
  `website_sale`). `product_pricelist_item`: matches model 1:1, no unexplained columns.
- **Source-specific coupling (do not copy)**: (a) qty always resolved into product default UoM before rule
  matching — a UoM-conversion dependency, not inherent to pricing. (b) pricelist chaining with DFS guard is
  Odoo-specific indirection. (c) pricelist currency silently becomes the order's transaction currency (PRC-18) — an
  easy-to-miss coupling a migration must explicitly decide to preserve or decouple.
- **Confidence**: VERIFIED FACT throughout. `website_id`/`code`/`selectable` origin: SUPPORTED INFERENCE only.
- **Unknown/Conflict**: EVIDENCE_MISSING — which module contributes `website_id`/`code`/`selectable`.

---

# 07 — TAX MASTER

## Source evidence

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| TAX-01 | `01 ACCOUNT/account/models/account_tax.py` | L71–78 | `account.tax`, `_check_company_auto=True`, ordered `sequence, id` |
| TAX-02 | account_tax.py | L18–22 | `TYPE_TAX_USE`: `sale`/`purchase`/`none` — a tax is scoped to one usage side at the master level |
| TAX-03 | account_tax.py | L84–95 | `amount_type`: `group`/`fixed`/`percent`/`division` (tax-included formula documented inline) |
| TAX-04 | account_tax.py | L137–147 | `price_include` computed from company default unless overridden per-tax |
| TAX-05 | account_tax.py | L156–161 | `tax_group_id` required, country-restricted domain |
| TAX-06 | account_tax.py | L174–195 | Tax amount is **distributed** across accounts/tags via repartition lines, not posted as one line |
| TAX-07 | account_tax.py | L96–101 | `fiscal_position_ids` M2M `account.fiscal.position` — substitution target |
| TAX-08 | account_tax.py | L164–169 | `tax_exigibility`: `on_invoice` vs `on_payment` — cash-basis timing lives on the tax master |
| TAX-09 | account_tax.py | L4852–4968 | `compute_all(...)` — master computation entry point, shared by Sale/Purchase/Accounting |
| TAX-10 | account_tax.py | L4970–4980 | `_filter_taxes_by_company`: walks company hierarchy — multi-company/branch tax resolution rule |
| TAX-11 | account_tax.py | L25–34 | `account.tax.group`: carries the GL settlement accounts, not the individual tax |
| TAX-12 | account_tax.py | L211–239 | `_constrains_name`: uniqueness scoped by `company_id, name, type_tax_use, tax_scope, country_id` |

## GROUP A consumption (Sale / Purchase)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| TAX-13 | `sale/models/sale_order_line.py` | L162–169 | `tax_ids` domain-restricted to `type_tax_use='sale'` **at the field level** |
| TAX-14 | sale_order_line.py | L541–568 | `_compute_tax_ids`: source = `product.taxes_id` filtered by company, then `fiscal_position.map_tax()` |
| TAX-15 | sale_order.py | L168–175, L411–428 | `fiscal_position_id` via `_get_fiscal_position(partner, shipping)`, cached by (partner, shipping, company) |
| TAX-16 | `purchase/models/purchase_order_line.py` | L34 | `tax_ids` M2M — **no field-level `type_tax_use` domain** (contrast with Sale) |
| TAX-17 | purchase_order_line.py | L146–152 | `_compute_tax_id`: source = `product.supplier_taxes_id` (**different product field from Sale's `taxes_id`**), then `fpos.map_tax()` |
| TAX-18 | purchase_order.py | L143, L451–453 | `fiscal_position_id` resolved via `_get_fiscal_position(partner)` on partner change (onchange, not stored-compute chain) |
| TAX-19 | account_tax.py | L4983–4999 | `_fix_tax_included_price(_company)` used by Purchase line pricing to reconcile tax-included vendor price |

## Synthesis — TAX MASTER

- **Business purpose**: central tax-rate/rule master plus settlement-account grouping and per-document
  distribution; computes and routes tax amounts, decoupled from where it's applied.
- **Actor / maintainer / consumer**: finance/tax admin per company/country (`company_id`/`country_id` both NOT
  NULL). Consumed identically by Sale, Purchase, Accounting through the shared computation engine.
- **Source owner observation**: tax is scoped in two dimensions at once — `type_tax_use` on the tax record AND a
  per-consumer product field (`taxes_id` for Sale vs `supplier_taxes_id` for Purchase) deciding candidacy before
  fiscal-position substitution. Migrating "tax master" alone is insufficient — the sale/purchase default-tax
  linkage on the product master is a separate structure that must be preserved or explicitly redesigned.
- **GROUP A consumers (cited)**: Sale TAX-13..15 (field-level domain). Purchase TAX-16..19 (no field-level domain;
  relies on `supplier_taxes_id`). Both route through `fiscal_position.map_tax()`.
- **Company/warehouse/branch context**: `account_tax.company_id`/`country_id` both NOT NULL — strictly scoped, no
  fallback-to-global row (unlike Pricelist). `_filter_taxes_by_company` implies branch/subsidiary resolution
  exists. **NONE FOUND** for warehouse-level scoping.
- **Database evidence**: `account_tax` columns include `ubl_cii_tax_category_code`, `ubl_cii_tax_exemption_reason_code`
  (e-invoicing/UBL), `wt_tax` (withholding tax) — **not** declared in the base fields read; added by an unopened
  e-invoicing/WHT-localization module. `account_tax_group` matches model 1:1.
- **Source-specific coupling (do not copy)**: (a) `account.fiscal.position`'s **own base model file was not found**
  anywhere in the read scope (only country-localization overrides exist) — the actual tax-substitution logic
  (`map_tax()`, `_get_fiscal_position()`) is a verified black box in this evidence set. (b) `compute_all` is a
  large, generic multi-mode entrypoint — Odoo's own accretion of edge cases, not a business requirement to
  replicate wholesale.
- **Confidence**: VERIFIED FACT for all Sale/Purchase consumption and tax/tax-group structure.
- **Unknown/Conflict**: **EVIDENCE_MISSING** — base `account.fiscal.position` model (fields, `map_tax()` body,
  `_get_fiscal_position()` body) not located; any claim about *how* tax substitution actually matches/replaces
  taxes is UNKNOWN pending that file. Also EVIDENCE_MISSING for module contributing `ubl_cii_*`/`wt_tax` columns.

---

# 08 — PAYMENT TERMS

## Source evidence

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PAY-01 | `01 ACCOUNT/account/models/account_payment_term.py` | L11–15 | `account.payment.term`, ordered `sequence, id` |
| PAY-02 | account_payment_term.py | L17–18, L26 | New term defaults to one 100%/0-day line |
| PAY-03 | account_payment_term.py | L39–46 | Early-payment-discount fields; country-conditional default (BE→mixed, NL→excluded, else→included) |
| PAY-04 | account_payment_term.py | L156–169 | `_check_lines`: percent lines must sum to exactly 100% |
| PAY-05 | account_payment_term.py | L171–256 | `_compute_terms`: builds the installment schedule; last line absorbs rounding residual |
| PAY-06 | account_payment_term.py | L61–79 | `_get_amount_due_after_discount`: early-discount computed on total or (total−untaxed) per config |
| PAY-07 | account_payment_term.py | L258–261 | Delete blocked if any `account.move` still references the term |
| PAY-08 | account_payment_term.py | L286–299 | Line: `value` (percent/fixed), `delay_type` (4 variants), `nb_days` |
| PAY-09 | account_payment_term.py | L310–327 | `_get_due_date`: implements each `delay_type` via `dateutil.relativedelta` |
| PAY-10 | account_payment_term.py | L343–347 | `_check_percent`: line `value_amount` in [0,100] |

## GROUP A consumption (Sale / Purchase)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PAY-11 | `sale/models/sale_order.py` | L176–181 | `payment_term_id`, stored+precompute |
| PAY-12 | sale_order.py | L431–434 | Defaults from `partner_id.property_payment_term_id` (customer term) |
| PAY-13 | sale_order.py | L538–544 | Sale reuses `payment_term_id.early_discount` fields for tax-totals display |
| PAY-14 | sale_order.py | L1437 | Order's `payment_term_id` copied verbatim onto generated `account.move` |
| PAY-15 | `purchase/models/purchase_order.py` | L153 | `payment_term_id` — **plain field, not a stored compute** (contrast with Sale) |
| PAY-16 | purchase_order.py | L454 | Defaults from `partner_id.property_supplier_payment_term_id` — **distinct partner property from Sale's** |
| PAY-17 | purchase_order.py | L939 | Same target field `account.move.invoice_payment_term_id` on bill creation as Sale |

## Synthesis — PAYMENT TERMS

- **Business purpose**: splits a total into dated installments (percent/fixed, multiple due-date rules) plus an
  optional early-payment discount; shared master referenced by both sales and purchase documents, copied onto the
  resulting journal entry.
- **Actor / maintainer / consumer**: finance/credit-control admin. Consumed identically in shape by Sale and
  Purchase, sourced from two different partner properties (customer vs vendor term).
- **Source owner observation**: the installment engine (`_compute_terms`/`_get_due_date`) is exercised at the
  Accounting (`account.move`) layer — Purchase does not appear to call it directly, only stamps `payment_term_id`
  onto the bill.
- **GROUP A consumers (cited)**: Sale PAY-11..14 (`property_payment_term_id`). Purchase PAY-15..17
  (`property_supplier_payment_term_id`). Both funnel into `account.move.invoice_payment_term_id`.
- **Company/warehouse/branch context**: `account_payment_term.company_id` nullable (global term allowed). **NONE
  FOUND** for warehouse/branch.
- **Database evidence**: `account_payment_term` matches model; several model fields (`currency_id`,
  `example_amount`, etc.) are correctly non-stored computes, absent from DB. `account_payment_term_line` matches
  PAY-08 exactly.
- **Source-specific coupling (do not copy)**: (a) BE/NL country-conditional default is a statutory quirk baked
  into generic code. (b) "last line absorbs residual" is a rounding-safety pattern worth preserving conceptually;
  the specific cash-rounding interplay is tightly coupled to a model outside this cluster.
- **Confidence**: VERIFIED FACT for all cited lines. SUPPORTED INFERENCE that Purchase doesn't itself compute an
  installment schedule (based on a targeted, not exhaustive, grep).
- **Unknown/Conflict**: UNKNOWN whether `account_move.py` (out of this cluster's read list) is what actually
  invokes `_compute_terms` for vendor bills.

---

# 09 — CURRENCY / EXCHANGE RATE

## Source evidence

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| CUR-01 | `02 OTHER/base/models/res_currency.py` | L20–24 | `res.currency`, ordered `active desc, name` |
| CUR-02 | res_currency.py | L27–47 | `name`(ISO code), `symbol`, `rounding`(default 0.01), `decimal_places`(computed), `rate_ids` |
| CUR-03 | res_currency.py | L49–56 | `UNIQUE(name)`; `CHECK(rounding>0)` |
| CUR-04 | res_currency.py | L120–139 | `_get_rates`: company-specific rate overrides NULL/global rate, `COALESCE(...,1.0)` triple fallback |
| CUR-05 | res_currency.py | L146–160 | "current rate" is not a stored fact — always relative-to-something-and-when |
| CUR-06 | res_currency.py | L280–299 | `_convert()`: the canonical conversion function |
| CUR-07 | res_currency.py | L216–223, L248–261 | `round()`/`is_zero()` route through the currency's own `rounding` |
| CUR-08 | res_currency.py | L108–118 | A currency used by any company cannot be deactivated |
| CUR-09 | res_currency.py | L342–348 | `res.currency.rate` model, ordered `name desc, id` |
| CUR-10 | res_currency.py | L349–373 | `name`(Date=effective date, required), `rate`, `company_rate`/`inverse_company_rate` |
| CUR-11 | res_currency.py | L375–382 | `UNIQUE(name,currency_id,company_id)` — one rate per currency per company per day; `CHECK(rate>0)` |
| CUR-12 | res_currency.py | L469–473 | Rate rows only creatable for **root companies** — branch/child companies inherit the parent's rates |

## GROUP A consumption (Sale / Purchase)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| CUR-13 | `sale/models/sale_order.py` | L195–201 | `currency_id`, stored+precompute, `ondelete='restrict'` |
| CUR-14 | sale_order.py | L453–456 | `pricelist_id.currency_id or company_id.currency_id` — currency derives from Pricing on Sale |
| CUR-15 | sale_order.py | L202–206, L458–463 | `currency_rate` frozen at `date_order`, not a live lookup |
| CUR-16 | `purchase/models/purchase_order.py` | L98–104 | `currency_id`, required, **`readonly=False`** (user can override the computed default) |
| CUR-17 | purchase_order.py | L460–466 | `partner_id.property_purchase_currency_id or company_id.currency_id` — **Purchase derives currency from a vendor property, not any pricelist** |
| CUR-18 | purchase_order.py | L211–219 | `_compute_currency_rate` — same snapshot pattern as Sale |
| CUR-19 | `purchase/models/purchase_order_line.py` | L461–462 | Line-level conversion when the chosen vendor's own currency differs — a second, independent conversion point |
| CUR-20 | purchase_order.py | L141, L161 | `amount_total_cc` pinned to `company_currency_id` — a parallel company-currency total alongside the transaction total |

## Synthesis — CURRENCY

- **Business purpose**: ISO-4217 currency master plus dated, company-scoped exchange-rate history; provides
  rounding precision and the one true `_convert()` used throughout.
- **Actor / maintainer / consumer**: master = rarely-edited system/finance config; rates = feed-imported or
  finance-maintained daily. Consumed pervasively.
- **Source owner observation**: currency itself carries **no company scoping** (genuinely global master); scoping
  enters only at the rate level (root-company-only, CUR-12) and at the consuming document level (Sale/Purchase
  compute `currency_id` via two unrelated default chains).
- **GROUP A consumers (cited)**: Sale CUR-13..15 (from pricelist). Purchase CUR-16..20 (from vendor property, plus
  a second line-level conversion). **The two document types arrive at "order currency" via two unrelated default
  chains** — a real semantic divergence to carry into any target design, not an oversight to normalize away.
- **Company/warehouse/branch context**: currency global; rate constrained to root companies only. **NONE FOUND**
  for warehouse-level currency scoping.
- **Database evidence**: `res_currency`/`res_currency_rate` match source exactly; all compute-only fields
  correctly absent as physical columns.
- **Source-specific coupling (do not copy)**: (a) `_get_rates`'s silent COALESCE-to-1.0 fallback treats "no rate
  found" as parity rather than raising — a data-quality risk a target design should make explicit/auditable. (b)
  Sale's currency-from-pricelist and Purchase's currency-from-vendor-property are both Odoo-specific convenience
  chains; the currency concept proper is clean/portable, the document-level default-selection logic is not.
- **Confidence**: VERIFIED FACT throughout.
- **Unknown/Conflict**: None identified within the read scope.

---

# 10 — SEQUENCE / DOCUMENT NUMBERING

## Source evidence

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| SEQ-01 | `02 OTHER/base/models/ir_sequence.py` | L93–96 | `ir.sequence`, ordered `name, id` |
| SEQ-02 | ir_sequence.py | L130–153 | `code`, `implementation`(standard/no_gap), `prefix`/`suffix`, `number_next`, `padding`, `company_id`(nullable) |
| SEQ-03 | ir_sequence.py | L13–19, L155–163 | `standard` implementation creates a **real PostgreSQL SEQUENCE object** — numbering delegated to the DB engine |
| SEQ-04 | ir_sequence.py | L58–64, L200–205 | `no_gap` implementation uses `SELECT ... FOR UPDATE NOWAIT` — pessimistic row lock, gap-free even across rollbacks |
| SEQ-05 | ir_sequence.py | L132–136 | Trade-off documented inline: no-gap is slower, standard can have gaps |
| SEQ-06 | ir_sequence.py | L207–242 | Prefix/suffix support date-token interpolation + zero-padding |
| SEQ-07 | ir_sequence.py | L114–128, L244–271 | `use_date_range` routes numbering through per-calendar-year child rows (hardcoded Jan1–Dec31 default) |
| SEQ-08 | ir_sequence.py | L301–304 | `UNIQUE(sequence_id, date_from, date_to)` |
| SEQ-09 | ir_sequence.py | L278–292 | `next_by_code`: company-specific row wins over global row when both exist; returns `False` (not exception) if none found |
| SEQ-10 | ir_sequence.py | L165–198 | Switching `standard`↔`no_gap` is a real DDL DROP/CREATE, not metadata-only |

## GROUP A consumption (Sale / Purchase)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| SEQ-11 | `sale/models/sale_order.py` | L54–57 | `name`: default placeholder literal `"New"` means "not yet numbered" |
| SEQ-12 | sale_order.py | L1001–1011 | `create()`: calls `next_by_code('sale.order', ...)`, falls back to `_("New")` again if no sequence matches |
| SEQ-13 | sale_order.py | L1004–1007 | `seq_date` derived from `date_order` — ties date-range sequencing to order date, not creation timestamp |
| SEQ-14 | `purchase/models/purchase_order.py` | L77 | Same `"New"` sentinel pattern |
| SEQ-15 | purchase_order.py | L393–406 | `create()`: same gate, calls `next_by_code('purchase.order', ...)`, but falls back to literal `'/'` — **a different, inconsistent fallback sentinel from Sale** |
| SEQ-16 | purchase_order.py | L398 | Comment confirms the per-order company-switch exists for more than sequencing (bleeds into picking-type/currency) |

## Synthesis — SEQUENCE

- **Business purpose**: reusable numbering service keyed by a `code` string, giving any document a gapless-or-gappy,
  optionally prefixed/padded/date-scoped running number.
- **Actor / maintainer / consumer**: system/technical admin configures rows; Sale/Purchase both call `next_by_code()`
  directly inline in their own `create()`.
- **Source owner observation**: Sale and Purchase gate on the identical `name == 'New'` sentinel but diverge on (a)
  how they scope company context and (b) the no-match fallback (`_('New')` vs literal `'/'`) — a genuine
  inconsistency, not a stylistic choice. Notably, Accounting Core's journal-entry numbering
  (`account.move._compute_name`, per its own evidence file SE-13) is an **entirely different, unrelated mechanism**
  in the same codebase — numbering is not uniform even within this one source tree.
- **GROUP A consumers (cited)**: Sale SEQ-11..13 (code `'sale.order'`). Purchase SEQ-14..16 (code `'purchase.order'`).
- **Company/warehouse/branch context**: `ir_sequence.company_id` nullable; company-specific row preferred over
  global when both exist. **NONE FOUND** for warehouse-level scoping.
- **Database evidence**: `ir_sequence` matches model exactly. Companion `ir_sequence_date_range` table referenced
  in source but not independently re-verified against the schema in this pass — EVIDENCE_MISSING.
- **Source-specific coupling (do not copy)**: (a) dependency on a real per-sequence PostgreSQL SEQUENCE object is
  deep RDBMS-specific — the *contract* (gapless/date-scoped next-number) is the portable part. (b) hardcoded
  Jan1–Dec31 calendar-year reset may not match every target fiscal-year convention.
- **Confidence**: VERIFIED FACT for all cited mechanics.
- **Unknown/Conflict**: **CONFLICT** (source inconsistency) — Sale vs Purchase use different no-sequence-found
  fallback sentinels; not resolvable to "correct" without a functional spec. EVIDENCE_MISSING —
  `ir_sequence_date_range` columns not cross-checked against the schema dump.

## Cross-cutting note (Pricing/Tax/Payment-Term/Currency/Sequence)

Sale and Purchase repeatedly diverge by reading **different partner "property" fields** for the same underlying
decision: `property_product_pricelist` (Sale only, no Purchase equivalent), `taxes_id` vs `supplier_taxes_id`,
`property_payment_term_id` vs `property_supplier_payment_term_id`. This directional-property pattern recurs three
times and is a strong signal for how the target partner-master should be shaped — not incidental.

---

# 11 — WAREHOUSE / LOCATION (SHARED MASTER DATA ONLY)

Movement/lifecycle behavior (stock.move, stock.quant, stock.picking transactions) is explicitly **out of scope**
here — covered in Phase 2 (Inventory Core).

## Source-evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| WH-01 | `stock/models/stock_warehouse.py` | L24–27 | `stock.warehouse`, `_check_company_auto=True` |
| WH-02 | stock_warehouse.py | L31–35 | `name` default-derives from `env.company.name` |
| WH-03 | stock_warehouse.py | L37–40 | `company_id` required, readonly, defaults from user's company |
| WH-04 | stock_warehouse.py | L41 | `partner_id` defaults from the owning company's partner |
| WH-05 | stock_warehouse.py | L42–45 | `view_location_id` domain requires matching company |
| WH-06 | stock_warehouse.py | L46–49 | `lot_stock_id` domain requires `usage='internal'` + same company |
| WH-07 | stock_warehouse.py | L50 | `code` Char(5), required |
| WH-08 | stock_warehouse.py | L91–98 | `UNIQUE(name,company_id)` and `UNIQUE(code,company_id)` — identity scoped **per company** |
| WH-09 | stock_warehouse.py | L113–135 | `create()`: auto-fills name/code/partner from company; creates `stock.location` tree stamped with same company |
| WH-10 | stock_warehouse.py | L184–188 | `write()`: changing `company_id` raises `UserError` — **immutable post-creation** |
| WH-11 | `stock/models/stock_location.py` | L14–20 | `stock.location`, `_parent_store=True` (nested-set hierarchy) |
| WH-12 | stock_location.py | L29 | `name` required |
| WH-13 | stock_location.py | L32–47 | `usage`: `supplier`/`view`/`internal`/`customer`/`inventory`/`production`/`transit` |
| WH-14 | stock_location.py | L48–50 | `location_id` self (parent) |
| WH-15 | stock_location.py | L51 | `child_ids` |
| WH-16 | stock_location.py | L60–63 | `company_id` optional — help text: "Let this field empty if this location is shared between companies" |
| WH-17 | stock_location.py | L84–85 | `warehouse_id` computed+store |
| WH-18 | stock_location.py | L93–96 | `UNIQUE(barcode,company_id)` |
| WH-19 | stock_location.py | L159–172 | `_compute_warehouse_id`: derived by walking `parent_path` against warehouse `view_location_id` ancestry — a computed hierarchical fact, not an authored FK |

## Cross-module dependency evidence (Sale / Purchase)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| WH-20 | `sale/models/sale_order.py` | whole-file grep | Literal string "warehouse" occurs **0 times** — base Sales has NO warehouse coupling |
| WH-21 | `purchase/models/purchase_order.py` | whole-file grep | Same — **0** occurrences in base Purchase |
| WH-22 | `sale_stock/models/sale_order.py` | L27–29 | `warehouse_id` added **only by the bridge module `sale_stock`**, not base `sale` |
| WH-23 | sale_stock/models/sale_order.py | L74–78 | Raw-SQL company-keyed warehouse backfill at module-install time |
| WH-24 | sale_stock/models/sale_order.py | L130–152 | `_check_warehouse()`: storable-product orders must have `warehouse_id`; multi-company lines must resolve a matching-company warehouse |
| WH-25 | `purchase_stock/models/purchase_order.py` | L24 | Picking-type domain cross-checks warehouse company against order company |
| WH-26 | purchase_stock/models/purchase_order.py | L331–337 | Receiving location resolved transitively through `picking_type_id.warehouse_id.lot_stock_id` |

## Database cross-reference

`stock_warehouse` key columns: `id, company_id NOT NULL, partner_id, view_location_id NOT NULL, lot_stock_id NOT
NULL, wh_input/qc/output/pack_stock_loc_id, ..., name NOT NULL, code varchar(5) NOT NULL, reception_steps NOT NULL,
delivery_steps NOT NULL` — extra `manufacture_*`/`repair_*`/`subcontracting_*` columns come from unopened
extension modules (`mrp`, `repair`, `mrp_subcontracting`) — out of scope, not analyzed.
`stock_location` full columns: `id, location_id, company_id, removal_strategy_id, warehouse_id, storage_category_id,
name NOT NULL, complete_name, usage NOT NULL, parent_path, barcode, active, valuation_account_id` — matches source
1:1. No `branch` column on either table (confirmed by the full-file grep in §12 below).

## Synthesis — WAREHOUSE / LOCATION

- **Business purpose**: Warehouse = master record for a physical stocking facility; Location = master record for a
  place/zone within (or a virtual accounting point outside) it.
- **Actor / maintainer / consumer**: Inventory/Stock managers maintain; consumed by Sales via `sale_stock` and
  Purchase via `purchase_stock` bridge modules — **never by base sale/purchase directly**.
- **Source owner observation**: Warehouse is strictly company-owned and immutable after creation; Location is
  company-scoped by default but explicitly nullable/shareable — an intentional design asymmetry.
- **GROUP A consumers (with citations)**: WH-22..26. Base sale/purchase carry zero direct references (WH-20/21) —
  the dependency is strictly through the bridge layer, itself gated on the `stock` module being installed.
- **Company/warehouse/branch context**: 1-required-company-per-warehouse with per-company unique name/code. No
  "Branch" model or field touches Warehouse or Location anywhere (see §12) — Thai tax-branch identity and physical
  warehouse structure are entirely disjoint concepts here.
- **Source-specific coupling (do not copy)**: Sale/Purchase gain `warehouse_id` only when the `*_stock` bridge
  module is installed — an Odoo modularity pattern, not a universal ERP requirement.
- **Confidence**: VERIFIED FACT for WH-01…WH-26.
- **Unknown/Conflict**: None for this concept. Extra `stock_warehouse` columns from `mrp`/`repair`/
  `mrp_subcontracting` — EVIDENCE_MISSING (out of scope, not analyzed).

---

# 12 — COMPANY / BRANCH

## Source-evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| CO-01 | `base/models/res_company.py` | L16–21 | `res.company` is itself hierarchical (`_parent_store=True`) — not a separate Branch model |
| CO-02 | res_company.py | L33 | `name` related from `partner_id.name` — every company IS a partner |
| CO-03 | res_company.py | L36 | `parent_id` Many2one self |
| CO-04 | res_company.py | L37 | `child_ids` — **literal field label is "Branches."** No separate `res.branch` model exists; "Branch" = a child `res.company` |
| CO-05 | res_company.py | L38 | `all_child_ids` (includes archived) |
| CO-06 | res_company.py | L52 | `currency_id` required |
| CO-07 | res_company.py | L96–104 | `currency_id` is a declared "root-delegated field" — must be identical across an entire branch hierarchy |
| CO-08 | res_company.py | L184–189 | `_onchange_parent_id`: delegated fields copied down from parent to child on set |
| CO-09 | res_company.py | L341–343 | `write()`: changing `parent_id` raises `UserError` — hierarchy position permanently fixed |
| CO-10 | res_company.py | L366–368 | Archiving a parent cascades archival onto all branches |
| CO-11 | res_company.py | L370–382 | Root-company currency change is force-propagated to ALL descendant branches |
| CO-12 | res_company.py | L411–418 | `_check_root_delegated_fields`: a branch's `currency_id` MUST equal its root's, else `ValidationError` — **DB/ORM-enforced: a branch cannot run a different operating currency** |
| CO-13 | res_company.py | L429–450 | `_accessible_branches()`: per-session, which branches the logged-in user can use |
| CO-14 | res_company.py | L452–459 | `_all_branches_selected()`: whether the user has all branches of a root selected at once |

## The Branch finding (prominent)

Two independent findings, from two different `addons_extra/` modules:

**(a) `l10n_th_partner` — genuine Thai "Tax Branch" identifier**

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| CO-15 | `addons_extra/l10n_th_partner/__manifest__.py` | full | "Thai Localization - Partner", author Ecosoft/OCA (`l10n-thailand`) — third-party community addon |
| CO-16 | `addons_extra/l10n_th_partner/models/res_partner.py` | L15 | `branch = fields.Char(string="Tax Branch", help="Branch ID, e.g., 0000, 0001, ...")` — a plain text code, not a linked model or hierarchy |
| CO-17 | `addons_extra/l10n_th_partner/models/res_company.py` | L9–11 | `res.company.branch` is a **non-stored related pass-through** to the partner's field |

**(b) `bm_thai_rd_vat_company_search` — a second, unrelated "branch" concept (VAT lookup integration)**

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| CO-18 | `addons_extra/bm_thai_rd_vat_company_search/models/res_partner.py` | L18–24 | `office_type`: `head_office`/`branch` — a **different field** from `l10n_th_partner`'s `branch`; reuses `company_registry` to store the branch number |
| CO-19 | same file | L118–247 | `search_thai_vat_company()` calls the live Thai Revenue Department SOAP/VAT web service, keyed by `BranchNumber` — independent of `l10n_th_partner`'s field |

**(c) Database confirmation**

| ID | Evidence | Anchor | What it evidences |
|---|---|---|---|
| CO-20 | `schema_only.sql` | L40396, col at L40515 | `res_partner.branch character varying` exists in the live DB |
| CO-21 | `schema_only.sql` | L41341–41344 | `COMMENT ON COLUMN ... 'Tax Branch'` — matches CO-16's label exactly |
| CO-22 | `schema_only.sql` | full-file grep "branch" | **Zero matches** on `res_company`, `stock_warehouse`, `stock_location`, `account_analytic_*` — confirms `res_company.branch` is non-stored and confirms Warehouse/Location have no branch dimension |
| CO-23 | `schema_only.sql` | L40525, L40529 | `x_studio_branch`, `x_studio_branch_name` also exist — Odoo Studio naming convention |
| CO-24 | full-tree grep | — | `x_studio_branch`, `x_studio_branch_name`, `parent_company_id`, `brand_id`, `bh_parent_company_code`, `is_hq_brand`, `hq_brand_id` (all real `res_partner` columns) have **no corresponding field definition anywhere in the tree** — EVIDENCE_MISSING |

## Cross-module dependency evidence (Sale / Purchase)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| CO-25 | `sale/models/sale_order.py` | L60 | `company_id` field on `sale.order` |
| CO-26 | sale_order.py | L453–456 | Company currency is the fallback for order currency |
| CO-27 | sale_order.py | L846–861 | `_check_order_line_company_id()`: rejects lines whose product's company is not in `order.company_id._accessible_branches()` — **direct, live use of the Branch access-scoping API** |
| CO-28 | `purchase/models/purchase_order.py` | L160–163 | `company_id` + `company_currency_id` (related) |
| CO-29 | purchase_order.py | L184–199 | **Identical `_accessible_branches()` pattern**, mirrored verbatim from Sale |

## Database cross-reference

`res_company`: matches `parent_id`/`currency_id`/`partner_id` exactly; **no `branch` column** (confirms CO-17's
non-stored nature). `res_partner`: confirmed `branch`, `x_studio_branch`, `x_studio_branch_name`,
`parent_company_id`, `brand_id`, `bh_parent_company_code`, `is_hq_brand`, `hq_brand_id`.

## Synthesis — COMPANY / BRANCH

- **Business purpose**: multi-company/multi-branch structuring for a group of entities sharing master data, which
  per CO-07/CO-12 MUST share one operating currency across a branch hierarchy.
- **Actor / maintainer / consumer**: hierarchy set up once at implementation (immutable after, CO-09); access
  scoping automatic per user session.
- **Source owner observation**: Odoo core has **no dedicated Branch model** — "Branch" is a UI label on child
  `res.company` records. Two *separate, independently developed* addons layer a genuine Thai tax-branch concept on
  top, with **no evidence either is aware of the other**. Neither links Tax Branch to Warehouse, Location, or the
  Company/Branch hierarchy — it is a flat attribute on Partner/Company, not a structural entity.
- **GROUP A consumers (with citations)**: CO-27 and CO-29 — both Sale and Purchase directly call
  `_accessible_branches()` to police cross-branch product usage on order lines. This is the one place the real
  Company/Branch hierarchy (not the Thai tax field) is load-bearing business logic.
- **Company/warehouse/branch context**: no overlap found between Warehouse (§11) and either Branch concept anywhere.
- **Source-specific coupling**: Thai tax-branch behavior is entirely additive (two independent bolt-ons), not part
  of the base data model — must be treated as a localization requirement layered onto Partner/Company, separate
  from Odoo's own Company/Branch hierarchy.
- **Confidence**: VERIFIED FACT for CO-01…CO-22, CO-25…CO-29. CO-23/24: column existence VERIFIED, origin/purpose
  EVIDENCE_MISSING.
- **Unknown/Conflict — PROMINENT**:
  - **EVIDENCE_MISSING**: `x_studio_branch`, `x_studio_branch_name`, `parent_company_id`, `brand_id`,
    `bh_parent_company_code`, `is_hq_brand`, `hq_brand_id` — real columns, no source-of-truth module found anywhere.
  - **CONFLICT/AMBIGUITY**: `l10n_th_partner`'s `branch` Char vs `bm_thai_rd_vat_company_search`'s `office_type` +
    reused `company_registry` — two unrelated modules implementing "Thai branch" with no evidence of coordination.
    UNKNOWN whether both are active together in production or produce inconsistent branch-number data. Not
    resolvable from static source alone — recommend data-profiling both columns before Phase 2/7 conclusions rely
    on either.
  - `office_type`'s presence in the DB schema was not independently re-verified in this pass — ASSUMPTION, not
    directly confirmed against `schema_only.sql`.

---

# 13 — DIMENSION / ANALYTIC REFERENCE

## Source-evidence table

Module: `analytic/`. A second module, `analytic_enterprise/`, exists but was not read — EVIDENCE_MISSING on its
contents.

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| AN-01 | `analytic/models/analytic_account.py` | L11–17 | `account.analytic.account`, `_check_company_domain=models.check_company_domain_parent_of` — a branch may use its root/head-office's analytic accounts |
| AN-02 | analytic_account.py | L38–43 | `plan_id` required — every analytic account belongs to exactly one Plan (dimension) |
| AN-03 | analytic_account.py | L44–49 | `root_plan_id` related, stored |
| AN-04 | analytic_account.py | L61–65 | `company_id` **NOT required** — an analytic account can be company-agnostic |
| AN-05 | analytic_account.py | L67–75 | `partner_id` on the analytic account itself |
| AN-06 | analytic_account.py | L90–93 | `currency_id` inherited from own `company_id` |
| AN-07 | analytic_account.py | L95–102 | `_check_company_consistency`: once lines exist, `company_id` can't change unless still `child_of` the existing lines' companies |
| AN-08 | `analytic/models/analytic_plan.py` | L14–19 | `account.analytic.plan` — Plans (dimensions) are THEMSELVES hierarchical |
| AN-09 | analytic_plan.py | L30–48 | self-referential `parent_id`/`children_ids`, recursive `complete_name` |
| AN-10 | analytic_plan.py | L78–93 | `default_applicability`(optional/mandatory/unavailable), `company_dependent=True` |
| AN-11 | `analytic/models/analytic_mixin.py` | L12–21 | `AnalyticMixin`: `analytic_distribution` — JSON map of account-id(s)→percentage, allowing split allocation |
| AN-12 | analytic_mixin.py | L26–30 | `distribution_analytic_account_ids` computed from JSON keys |

## Cross-module dependency evidence (Sale / Purchase)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| AN-13 | `sale/models/sale_order_line.py` | L14 | `_inherit=['analytic.mixin']` |
| AN-14 | sale_order_line.py | L1228 | `_compute_analytic_distribution()` override |
| AN-15 | `sale/models/sale_order.py` | L1990–2004 | Sale Orders can auto-generate a new `account.analytic.account` record, company-stamped |
| AN-16 | sale_order.py | L2097 | `analytic_distribution` passed through to downstream invoice line values |
| AN-17 | `purchase/models/purchase_order_line.py` | L15 | `_inherit=['analytic.mixin']` |
| AN-18 | purchase_order_line.py | L353–363 | `_compute_analytic_distribution()`: suggested distribution from `account.analytic.distribution.model` (a rules engine) |
| AN-19 | `purchase/models/purchase_order.py` | L632 | `_validate_analytic_distribution()` invoked at PO confirmation |

## Database cross-reference

`account_analytic_account`: `plan_id NOT NULL, root_plan_id, company_id(nullable), partner_id, code, name(jsonb)
NOT NULL` — confirms AN-04 nullable. `account_analytic_plan`: no `company_id` column at all. `account_analytic_line`:
`company_id NOT NULL` (contrast with nullable on the Account) — posted lines are always company-attributed even if
the parent Account is shared; `so_line` column confirms Sale-Order-Line linkage at the DB level.

## Synthesis — DIMENSION / ANALYTIC

- **Business purpose**: secondary, cross-cutting coding dimension (cost center/project/department) attachable with
  percentage-split allocation to transaction lines, independent of the primary Chart of Accounts.
- **Actor / maintainer / consumer**: Plans/Accounts are admin-maintained master data; `analytic_distribution`
  values set manually or auto-suggested (AN-18) at line entry.
- **Source owner observation**: two-tiered — Plan (dimension category, hierarchical) contains Accounts (selectable
  values). Company scoping is asymmetric: Plan has none, Account is optional, but posted Lines are mandatorily
  company-stamped — dimension *definitions* can be shared while dimension *usage* is always attributed.
- **GROUP A consumers (with citations)**: AN-13..19. Both Sale and Purchase Order Lines use the **identical
  `analytic.mixin` inheritance** — a symmetric, first-class dependency, unlike Warehouse (bridge-module-only).
- **Company/warehouse/branch context**: company-check explicitly honors the Company/Branch parent-of relationship
  (AN-01) — reuses the §12 hierarchy. No connection to Warehouse/Location.
- **Source-specific coupling**: `analytic_distribution`'s JSON-map storage is an Odoo-specific mechanism; the
  underlying business concept (split a line's value across N cost dimensions by percentage) is generic/portable.
- **Confidence**: VERIFIED FACT for AN-01…AN-19 and the DB column lists.
- **Unknown/Conflict**: `analytic_enterprise/` contents and `account.analytic.distribution.model`'s exact
  suggestion logic — both EVIDENCE_MISSING (not opened).

---

# 14 — CRITICAL FINDINGS CARRIED FORWARD TO LATER PHASES

These are not resolved here; they are registered so Phases 2–10 (and the eventual Unknown/Conflict register,
deliverable #14) do not silently re-derive or contradict them.

1. **Stale `.po` files claim a `uom.category` model that does not exist** in source or DB (UOM-22) — treat shipped
   translation files as unreliable evidence of current model shape anywhere else in this codebase too.
2. **Two independent, uncoordinated modules both auto-generate `product.default_code`** by different rules
   (PRD-15, PRD-16/CAT-08) — a real collision risk, not a design pattern to preserve.
3. **Purchase does not use `product.pricelist` at all** — vendor pricing is structurally separate
   (`product.supplierinfo`). Any cross-module pricing synthesis in Phase 5 must not assume symmetry with Sale.
4. **`account.fiscal.position`'s base model file was not found** anywhere in the read source tree — the actual
   tax-substitution mechanism is a verified black box, relevant to Phase 7 (source↔DB reconciliation).
5. **Sale and Purchase diverge on every partner-property default**: pricelist vs. none; `taxes_id` vs.
   `supplier_taxes_id`; `property_payment_term_id` vs. `property_supplier_payment_term_id`; pricelist-derived vs.
   vendor-property-derived currency. This is a recurring structural asymmetry, not incidental.
6. **Sequence fallback sentinel differs between Sale (`"New"`) and Purchase (`"/"`)** when no `ir.sequence` row
   matches — a genuine source inconsistency.
7. **Two independent Thai "branch" modules exist with no evidence of coordination**
   (`l10n_th_partner.branch` vs `bm_thai_rd_vat_company_search.office_type`+`company_registry`) — mutual data
   consistency is UNKNOWN; flagged for Phase 8 (Thailand Business Reality) data-profiling before any Thailand
   requirement is declared.
8. **A cluster of `res_partner` DB columns has no source-of-truth module anywhere in the extraction**
   (`x_studio_branch`, `x_studio_branch_name`, `parent_company_id`, `brand_id`, `bh_parent_company_code`,
   `is_hq_brand`, `hq_brand_id`, `hq_brand_count`, `store_type_id`) — likely Odoo Studio / direct DB
   customization from live production use. Relevant to Phase 7 and to the Fit-Gap pack (candidate: real
   multi-brand/multi-HQ retail requirement, currently UNVERIFIED).
9. **`product.brand` ("Division") carries a single `warehouse_id`** (CAT-09) and is used for **portal
   search/access control**, not accounting or inventory defaults — do not conflate with `product.category` in any
   later synthesis.
10. Numbering is **not uniform across this codebase**: `ir.sequence` (Sale/Purchase) vs. Accounting Core's
    self-computed, hash-chained `account.move._compute_name` are two unrelated mechanisms for the same job.
