# Source Map (candidate) — `product`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `product` |
| Display name | Products & Pricelists |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e36045b7a3af91b6` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/product/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `mail`, `uom`
- Direct dependents in 300-module list (5): `account`, `event_product`, `loyalty`, `mrp`, `stock`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (16): `product_sequence` — LGPL-3, `d_product_brand` — OPL-1, `19_bhpro_product_part` — OPL-1, `multi_level_approval` — OPL-1, `odoo19_uom_ext` — no-license, `product_3d_viewer` — LGPL-3, `19_bhpro_master_data` — OPL-1, `19_product_variant_reference` — OPL-1, `scgl_import_product_images` — no-license, `product_category_filter` — AGPL-3, `19_bhpro_inventory` — OPL-1, `bh_product_label_qrcode` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / —
- Inventory of user-facing artifacts (counts): menu items 0, views 60, window actions 13, server actions 4, reports 7, mail templates 0, scheduled jobs 0, wizards 3, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (26): `product.label.layout` (Choose the sheet layout to print the labels); `update.product.attribute.value` (Update product attribute value); `product.attribute.custom.value` (Product Attribute Custom Value); `product.template.attribute.line` (Product Template Attribute Line); `product.combo` (Product Combo); `product.attribute.value` (Attribute Value); `product.pricelist` (Pricelist); `product.category` (Product Category); `product.combo.item` (Product Combo Item); `product.supplierinfo` (Supplier Pricelist); `product.template.attribute.exclusion` (Product Template Attribute Exclusion); `product.uom` (Link between products and their UoMs); `product.document` (Product Document); `product.template` (Product); `product.product` (Product Variant); `product.template.attribute.value` (Product Template Attribute Value); `product.attribute` (Product Attribute); `product.catalog.mixin` (Product Catalog Mixin); `product.pricelist.item` (Pricelist Rule); `product.tag` (Product Tag); `report.product.report_pricelist` (Pricelist Report); `report.product.report_producttemplatelabel2x7` (Product Label Report 2x7); `report.product.report_producttemplatelabel4x7` (Product Label Report 4x7); `report.product.report_producttemplatelabel4x12` (Product Label Report 4x12); `report.product.report_producttemplatelabel4x12noprice` (Product Label Report 4x12 No Price) … (+1)
- Objects extended from other modules (10): `res.country.group`, `mail.thread`, `mail.activity.mixin`, `ir.attachment`, `image.mixin`, `res.company`, `res.currency`, `uom.uom`, `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 2 field(s); company-consistency auto-check declared on 3 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `product.label.layout` ← Community: `stock`; open-license custom/third-party scanned: `bh_product_label_qrcode`
- `product.attribute.custom.value` ← Community: `point_of_sale`, `sale`; open-license custom/third-party scanned: —
- `product.template.attribute.line` ← Community: `point_of_sale`, `website_sale`, `website_sale_comparison`; open-license custom/third-party scanned: —
- `product.combo` ← Community: `point_of_sale`, `website_sale_stock`; open-license custom/third-party scanned: —
- `product.pricelist` ← Community: `loyalty`, `partnership`, `point_of_sale`, `website_sale`; open-license custom/third-party scanned: —
- `product.category` ← Community: `account`, `delivery`, `mrp_account`, `point_of_sale`, `stock`, `stock_account`; open-license custom/third-party scanned: `product_category_filter`, `product_sequence`
- `product.combo.item` ← Community: `point_of_sale`; open-license custom/third-party scanned: —
- `product.supplierinfo` ← Community: `mrp_subcontracting`, `purchase`, `purchase_requisition`, `purchase_stock`; open-license custom/third-party scanned: `smesplus_uom_ext`
- `product.template.attribute.exclusion` ← Community: `point_of_sale`; open-license custom/third-party scanned: —
- `product.uom` ← Community: `point_of_sale`; open-license custom/third-party scanned: —
- `product.document` ← Community: `mrp`, `sale`, `sale_gelato`, `sale_pdf_quote_builder`, `website_sale`, `website_sale_gelato`; open-license custom/third-party scanned: —
- `product.template` ← Community: `account`, `event_booth_sale`, `event_product`, `event_sale`, `hr_expense`, `l10n_account_withholding_tax`, `l10n_ar_website_sale`, `l10n_de`, `l10n_eg_edi_eta`, `l10n_gr_edi` … (+47); open-license custom/third-party scanned: `base_accounting_kit`, `l10n_th_withholding_tax`, `om_account_asset`, `product_3d_viewer`, `product_brand_sale`, `product_category_filter`, `product_sequence`, `purchase_request` … (+2)
- `product.product` ← Community: `account`, `event_booth_sale`, `event_product`, `hr_expense`, `l10n_eg_edi_eta`, `l10n_gcc_invoice`, `l10n_in_pos`, `l10n_tr_nilvera_einvoice_extended`, `loyalty`, `mrp` … (+29); open-license custom/third-party scanned: —
- `product.template.attribute.value` ← Community: `point_of_sale`, `product_matrix`, `website_sale`; open-license custom/third-party scanned: —
- `product.attribute` ← Community: `point_of_sale`, `website_sale`, `website_sale_comparison`; open-license custom/third-party scanned: —
- `product.catalog.mixin` ← Community: `account`, `mrp`, `purchase`, `repair`, `sale`, `stock`; open-license custom/third-party scanned: —
- `product.pricelist.item` ← Community: `point_of_sale`, `sale`, `website_event_sale`, `website_sale`; open-license custom/third-party scanned: —
- `product.tag` ← Community: `point_of_sale`, `pos_self_order`, `website_sale`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `res.country.group`, `mail.thread`, `mail.activity.mixin`, `ir.attachment`, `image.mixin`, `res.company`, `res.currency`, `uom.uom`, `res.config.settings`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 18 declarative constraint method(s), 4 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 5 (`group_product_pricelist`, `group_product_variant`, `group_product_manager`, `base.group_user`, `base.default_user_group`); record rules 6 (of which company-scoped by text 6); access rows 38

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 117 of 117 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: `product` (Products & Pricelists)

- Source revision: `19.0.post20260921` (Odoo 19.0 Community, read-only). Pointers are relative to the addons root.
- Manifest: `product/__manifest__.py:1-77` — version 1.2, LGPL-3, depends `base`, `mail`, `uom` (`:5`). No `auto_install`, not flagged as an application. Cron jobs: none (skeleton `crons: []`; UNKNOWN for schedulers in other modules — not traced).
- Evidence key: claims are from static source unless marked `(TEST)`.

## 1. Capabilities (core vs optional vs conditional)

Core (always present once installed):
- Product master data with two levels: a product *template* (the commercial item) and *variants* (concrete sellable/stockable combinations). `product/models/product_template.py:18-20`, `product/models/product_product.py:16-20`.
- Product type limited to three business types: Goods, Service, Combo (default Goods). `product/models/product_template.py:54-66`. Storable / stock tracking is NOT defined here (see section 4).
- Categories (hierarchical, no cycles), tags, documents/attachments, images, barcodes, internal reference, vendor price lists (supplier info), attributes/variants, combo bundles, label printing, product catalog helper used by order screens. `product/models/product_category.py:6-47`, `product/models/product_tag.py`, `product/models/product_document.py:8`, `product/models/product_catalog_mixin.py:13`, `product/wizard/product_label_layout.py`.
- HTTP endpoints (login required): pricelist export, document upload, catalog order-line info/update. `product/controllers/pricelist_report.py:13`, `product/controllers/product_document.py:14`, `product/controllers/catalog.py:8,34`.

Optional (feature groups toggled in Settings; UI and behavior gated):
- Pricelists (`product.group_product_pricelist`, label "Basic Pricelists"): `product/security/product_security.xml:12-14`; setting `product/models/res_config_settings.py:12-13`. Turning ON creates one "Default" pricelist per company in the company currency (`product/models/res_company.py:15-46`); turning OFF archives every pricelist (`product/models/res_config_settings.py:36-43`) after a warning (`:23-34`). Also switched on automatically when multi-currency is activated (`product/models/res_currency.py:10-16`). With the group off, partner pricelist lookup returns nothing (`product/models/product_pricelist.py:334-360`).
- Variants (`product.group_product_variant`): only gates visibility of variant-level fields/filters in forms (e.g. `product/views/product_pricelist_item_views.xml:10,27,73`, `product/views/product_supplierinfo_views.xml:23`). Variant *data model* exists regardless.
- Units of Measure & Packagings (`uom.group_uom`, owned by `uom`): gates UoM fields in forms (`product/models/res_config_settings.py:9`, `product/views/product_views.xml:81,118`).
- Weight and volume display units (kg/lb, m3/ft3) stored as system parameters `product.weight_in_lbs`, `product.volume_in_cubic_feet`. `product/models/res_config_settings.py:14-21`. Only affects labels (`product/models/product_template.py:405-412`), not stored quantities.
- Loyalty/promotions install checkbox (`module_loyalty`) is a pointer to another module. `product/models/res_config_settings.py:11`.

Conditional: dynamic-variant safety cap (system parameter `product.dynamic_variant_limit`, default 1000) — `product/models/product_template.py:828-831`.

## 2. Business objects and lifecycle

- Product Template -> many Variants (cascade delete of variants with template). `product/models/product_product.py:42-44`. Variant inherits template fields by delegation (`:19`). Template compute/inverse sync: for single-variant products, barcode, internal reference, cost, weight, volume are mirrored to the sole variant. `product/models/product_template.py:269-310`; related-field list at `:509-511`.
- Creation: creating a template auto-generates its variants; changing attribute lines regenerates them; reactivating a template with no variants regenerates. `product/models/product_template.py:568-584`, `:585-595`, `:770`.
- Archiving: archiving a template archives all variants; archiving the last active variant archives the template; unarchiving a variant reactivates the template. `product/models/product_template.py:592-593`, `product/models/product_product.py:696-711`.
- Deleting: last variant deletion removes the template unless it uses dynamic attributes; "unlink or archive" fallback archives when deletion is blocked by references. `product/models/product_product.py:712-748`, `:750-786`.
- Copy: a copied product gets " (copy)" name suffix; copying a variant copies the template instead. `product/models/product_template.py:608-628`, `product/models/product_product.py:786`.
- Attributes: attribute -> values -> per-template attribute lines -> per-template attribute values (with extra price). Variant creation mode per attribute: Instantly / Dynamically (on order) / Never. `product/models/product_attribute.py:24-33`. Multi-checkbox display is only allowed with "Never". `product/models/product_attribute.py:14-17`. Mode cannot change once used by products. `product/models/product_attribute.py:107-125`. Used attribute/values cannot be deleted. `product/models/product_attribute.py:133-150`, `product/models/product_attribute_value.py:127-130`. Excluded combinations model: `product/models/product_template_attribute_exclusion.py`. Extra prices on attribute values are guarded and follow variants. `product/models/product_template_attribute_value.py:84-110`.
- "Configurable" flag (stored): dynamic attributes, or any line with 2+ values, multi-checkbox, or custom value. `product/models/product_template.py:173,217-235`.
- Category tree: name path stored; recursion forbidden. `product/models/product_category.py:22-47`. Categories carry a property-definition schema that products inherit as custom properties. `product/models/product_category.py:29`, `product/models/product_template.py:184-185`. Three seeded categories: Goods, Expenses, Services. `product/data/product_data.xml:5-13`.
- UoM: each product has one default unit (default "Unit", cached) plus optional additional packagings (`uom_ids`). `product/models/product_template.py:24-31,118-122`. Changing the default unit applies a 1:1 relabel (no numeric conversion), with a warning. `product/models/product_template.py:475-484`, write hook `:585-588`. Packaging barcodes are a separate link record (unit + product + barcode), unique globally and disjoint from product barcodes. `product/models/product_uom.py:9-27`, `product/models/uom_uom.py:9-21`.
- Combo: combo product holds "combo choices"; each choice holds 1+ non-combo products, no duplicates. `product/models/product_combo.py:7-79`, `product/models/product_combo_item.py:30-33`.
- Vendor prices (supplier info): vendor, product/variant, min qty, unit price, discount %, currency, validity dates, lead time (days), unit. `product/models/product_supplierinfo.py:15-58`. Seller selection picks lowest discounted price in company currency among the first matching vendor, ties by sequence. `product/models/product_product.py:1052-1075`.
- Pricelist: name, currency, optional company, country groups, ordered by sequence. `product/models/product_pricelist.py:12-57`. Rules (items): applied on All / Category / Product / Variant; based on Sales Price / Cost / Other Pricelist; computed as Fixed, Discount %, or Formula (discount/markup, rounding, surcharge, min/max margin); date range and minimum quantity. `product/models/product_pricelist_item.py:51-115,116-152`. First matching rule wins after ordering by scope specificity then larger min quantity. `product/models/product_pricelist_item.py:11`, `product/models/product_pricelist.py:169-236`. No matching rule -> product's list price used. `product/models/product_pricelist_item.py:570-626`.
- Partner pricelist resolution order: partner-specific setting; else pricelist of the partner's country group; else system-parameter fallback per company / global; else first available pricelist. `product/models/product_pricelist.py:334-360`, `:288-332`. Partner-specific pricelist is company-dependent and synced from commercial parent. `product/models/res_partner.py:26-50`.

## 3. Actions, validation, constraints, automation

Validations (all raise business errors):
- Combo product must have at least 1 choice; sellable combo may only contain sellable products. `product/models/product_template.py:489-505`. Choosing type=Combo is blocked if the product has attributes or is already inside a combo; it also switches "can be purchased" off. `product/models/product_template.py:460-472`. Switching away from Combo clears choices. `product/models/product_template.py:604-605`.
- Negative product cost rejected (form-level check). `product/models/product_template.py:417-420`.
- Duplicate internal reference: warning only, not blocked. `product/models/product_template.py:422-432`.
- Barcode: unique per company scope (company or shared/no-company); must also not clash with any packaging barcode. `product/models/product_product.py:252-290`; company change re-checks. `product/models/product_template.py:251-253`. `(TEST)` `product/tests/test_barcode.py`.
- Pricelist rule checks: "Other Pricelist" base requires a base pricelist; recursion between pricelists forbidden; end date after start; min margin below max margin; required scope target (category/product/variant) present; positive rounding. `product/models/product_pricelist_item.py:316-381,469-471`. A pricelist used as base by another cannot be deleted. `product/models/product_pricelist.py:393-404`.
- Company change on a pricelist re-validates its rules. `product/models/product_pricelist.py:72-80`.
- Combo choice and combo company consistency. `product/models/product_combo.py:75-79`, `product/models/product_product.py:292-295`.
- Attribute line: values must belong to the attribute; conflicting archive/value edits blocked. `product/models/product_template_attribute_line.py:60-75,117-145`.
- Document link URLs must be http/https/ftp. `product/models/product_document.py:25-35`.

Wizards/actions: label layout printing (`product/wizard/product_label_layout.py`), bulk "add value to existing lines / update extra price" (`product/wizard/update_product_attribute_value.py`), pricelist PDF/XLSX report (`product/report/product_pricelist_report.py`, `product/controllers/pricelist_report.py:13`), server-action "Pricelist Report" restricted to the pricelist group (`product/views/product_template_views.xml:208-211`).

Automation: no scheduled jobs. Event-style behavior: company creation auto-creates default pricelist if feature on (`product/models/res_company.py:10-14`); currency archival archives pricelists in that currency (`product/models/res_currency.py:18-24`); company currency change delays default pricelist creation until after write (`product/models/res_company.py:53-69`) `(TEST)` `product/tests/test_pricelist_auto_creation.py:24`.

## 4. Security and multi-company

Groups: `Products` privilege with manager group "Create" (`group_product_manager`), implied by System admin, granted to root and admin users. `product/security/product_security.xml:4-29`. Everyone in `base.group_user` gets read-only on all product models; manager group gets full CRUD (`product/security/ir.model.access.csv`, 38 rows: read rows lines 2-17, manager rows 18-31). Exceptions: label-layout wizard full access for internal users; attribute-value update wizard has no delete (manager). Partner managers can read pricelists. `product/security/ir.model.access.csv`.
- Record rules (all non-global, applied to everyone): visible if record has no company or company is an ancestor-or-self of the user's active companies. Applied to templates, documents, pricelists, pricelist rules, supplier info, combos. `product/security/product_security.xml:33-69`. Variants are not directly ruled; they follow template via delegation/search bypass (`product/models/product_product.py:44`). UNKNOWN — EVIDENCE INSUFFICIENT for effective variant-level enforcement beyond that.
- Cost visibility: cost (standard price) fields restricted to internal users (`base.group_user`). `product/models/product_template.py:100-107`, `product/models/product_product.py:62-66`. Price computation from cost runs elevated so that non-cost users still get cost-based prices. `product/models/product_product.py:1104-1112`.
- Company scoping: template company optional (shared if empty); auto company-consistency checks with parent-of semantics. `product/models/product_template.py:22-24`, `product/models/product_product.py:22`. Pricelist default company = current company; may be blank (shared). `product/models/product_pricelist.py:39-43`.

## 5. Handoffs to other modules (owner in bold)

- Accounting: taxes (customer/vendor), income and expense accounts on product and category (company-dependent) — owner `account`. `account/models/product.py:15-30,38-60`.
- Inventory: storable flag, lot/serial tracking, routes, delivery lead time — owner `stock`. `stock/models/product.py:839,856,892`. Product cost method and valuation (Standard/FIFO/AVCO; periodic vs perpetual) per category, company-dependent — owner `stock_account`. `stock_account/models/product.py:731-745`.
- Sales: invoicing policy, service type, expense policy — owner `sale`. `sale/models/product_template.py:14,22,35`. Pricelist rule extension for sale — `sale`.
- Purchasing: purchase control method, vendor price use in RFQs — owner `purchase`. `purchase/models/product.py:14`. "Can be purchased" default is left as a stub here (subclass-computed). `product/models/product_template.py:202-203`.
- Service tracking selection (only "Nothing" here) is extended by sale-side modules (e.g. `sale_project`). `product/models/product_template.py:71-80`, `sale_project/models/product_template.py:45`.
- Catalog mixin consumed by order-like documents — owners `sale`, `purchase`, `stock`, `account`, `mrp`, `repair` (see section 7).

## 6. Config/defaults/computed behavior that changes outcomes

- Cost is per-company (company-dependent) on the variant; the template shows the value for the current company only when it has exactly one variant, else empty. `product/models/product_product.py:62-66`, `product/models/product_template.py:100,312-317`. Cost currency follows the product's company, else the active company. `product/models/product_template.py:264-268`. Actual costing method comes from `stock_account`.
- List price default 1.0; sale and purchase flags default true; type default Goods. `product/models/product_template.py:94-96,116-117,54-66`.
- Sales price for a variant = template price + extra price of selected attribute values (+ non-variant extras from context); converted to requested unit and currency. `product/models/product_product.py:1099-1130`.
- Pricelist item currency/company inherit from the pricelist, else product company, else active company. `product/models/product_pricelist_item.py:171-182`.
- Rule quantities and margins are expressed in the product's default unit and converted for other units. `product/models/product_pricelist_item.py:585-592`, `product/models/product_pricelist.py:169-236`.
- Dynamic attribute limit (default 1000) governs mass variant creation. `product/models/product_template.py:828`.
- Decimal precisions seeded: Product Price, Discount, Stock Weight, Volume — 2 digits each. `product/data/product_data.xml:15-30`.
- Vendor price default currency = active company currency; default lead time 1 day. `product/models/product_supplierinfo.py:35-37,50`. `(TEST)` seller selection rules `product/tests/test_seller.py:27-154`.

## 7. Effective extension path (modules that `_inherit` key models; module names only)

- `product.template`: account, event_booth_sale, event_product, event_sale, hr_expense, l10n_account_withholding_tax, l10n_ar_website_sale, l10n_de, l10n_eg_edi_eta, l10n_gr_edi, l10n_hr_edi, l10n_hu_edi, l10n_id_efaktur_coretax, l10n_in, l10n_in_pos, l10n_my, l10n_my_edi, l10n_pl, l10n_ro_cpv_code, l10n_tr, l10n_tr_nilvera_einvoice_extended, loyalty, mrp, mrp_account, partnership, point_of_sale, pos_discount, pos_loyalty, pos_sale, pos_self_order, product_email_template, product_expiry, product_matrix, purchase, purchase_stock, repair, sale, sale_expense, sale_gelato, sale_product_matrix, sale_project, sale_purchase, sale_stock, sale_timesheet, stock, stock_account, stock_delivery, stock_landed_costs, website_event_booth_sale, website_event_sale, website_sale, website_sale_collect, website_sale_gelato, website_sale_slides, website_sale_stock, website_sale_stock_wishlist, website_sale_wishlist. `l10n_th` is NOT among them.
- `product.product`: account, event_booth_sale, event_product, hr_expense, l10n_eg_edi_eta, l10n_gcc_invoice, l10n_in_pos, l10n_tr_nilvera_einvoice_extended, loyalty, mrp, mrp_account, mrp_subcontracting, mrp_subcontracting_account, mrp_subcontracting_purchase, point_of_sale, pos_hr, pos_loyalty, pos_self_order, product_expiry, product_margin, purchase, purchase_requisition, purchase_stock, repair, sale, sale_edi_ubl, sale_gelato, sale_project, sale_timesheet, stock, stock_account, stock_dropshipping, website_event_sale, website_sale, website_sale_comparison, website_sale_loyalty, website_sale_slides, website_sale_stock, website_sale_wishlist.
- `product.pricelist`: loyalty, partnership, point_of_sale, website_sale. `product.pricelist.item`: point_of_sale, sale, website_event_sale, website_sale.
- `product.category`: account, delivery, mrp_account, point_of_sale, stock, stock_account. `product.supplierinfo`: mrp_subcontracting, purchase, purchase_requisition, purchase_stock.
- `product.attribute` / lines / template values: point_of_sale, website_sale, website_sale_comparison, product_matrix. `product.combo`: point_of_sale, website_sale_stock. `product.tag`: point_of_sale, pos_self_order, website_sale. `product.document`: mrp, sale, sale_gelato, sale_pdf_quote_builder, website_sale, website_sale_gelato. `product.uom`: point_of_sale. `product.catalog.mixin`: account, mrp, purchase, repair, sale, stock.
- Manifest-level dependents (direct `depends` on `product`): account, event_product, loyalty, mrp, stock (plus others transitively). Note: the `_inherit` grep is by module-name only; many additional modules depend transitively.

## 8. UNKNOWN items

- Scheduler/automation that runs periodically for product data: UNKNOWN — EVIDENCE INSUFFICIENT (none inside `product`; other modules not traced).
- Effective access to product variants for non-manager, multi-company users beyond template rule: UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether any storable/tracking/valuation behavior is universal: UNKNOWN — EVIDENCE INSUFFICIENT for `product` alone; defined only in `stock` / `stock_account`.
- Default value of "can be purchased" outcome when `purchase` is not installed: field defaults true (`product/models/product_template.py:117`), compute is a stub (`:202-203`); downstream effect UNKNOWN — EVIDENCE INSUFFICIENT.
- Thai-specific pricing or product rules: none found in `product`; see `l10n_th` note.

