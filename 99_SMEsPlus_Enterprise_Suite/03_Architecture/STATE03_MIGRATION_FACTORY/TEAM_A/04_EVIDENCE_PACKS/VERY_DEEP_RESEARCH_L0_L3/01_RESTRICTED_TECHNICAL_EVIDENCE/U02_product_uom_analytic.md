# U02 - product_uom_analytic - Restricted Technical Evidence (L2/L3)

> RESTRICTED - TECHNICAL EVIDENCE - NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

| Field | Value |
|---|---|
| Unit | U02 - `product_uom_analytic` |
| Modules owned | `product`, `uom`, `analytic`, `utm` (light), `resource` (light) |
| Source revision | `19.0.post20260921` (Odoo 19 Community only; read-only) |
| Date | 2026-10-02 |
| Method | static source reading under `odoo/addons`; restored DB `itest19c_research` queried for configuration/structure only (counts, groups, ACL, rules, parameters); no Odoo start, no business data |
| Existing Function-IDs used | RTG-F01 (matched), RTG-F04 (matched, product side only); all other claims `FUNCTION MAPPING REQUIRED` |
| Core platform read (outside module scope) | `odoo/orm/fields.py` company-dependent mechanism (cited in prose only; not claim-checkable) |

## 0. Executive summary and cross-cutting findings

1. **Product classification in 19**: `type` has only three values (`consu` Goods, `service`, `combo`). The inventory classification is the separate boolean `is_storable` ("Track Inventory") added by `stock`; it is forced False for non-goods and drives reservation, valuation eligibility and lot/serial tracking. (CAP-U02-01)
2. **No unit categories and no purchase-unit field in 19**: units form a tree (`relative_uom_id`, `relative_factor`, stored `factor`); conversion never checks a common root (`_has_common_reference` exists but is only used by timesheet/EDI/label code). Packagings are `uom_ids` on the product plus `product.uom` barcode rows. (CAP-U02-04)
3. **Lead times are calendar days**: contrary to the assignment's premise, Sales/Purchase/Inventory lead-time logic in the installed Community modules does not use `resource` working calendars; it uses `relativedelta(days=...)`/`timedelta(days=...)`. Calendars are used by manufacturing work centers (and HR/project, out of unit). (CAP-U02-10)
4. **Company-dependent properties** (hand-off table in CAP-U02-02): 8 on `product.category`, 1 on `product.product` (`standard_price`), 10 on `product.template`, 1 on `account.analytic.plan`, 21 on `res.partner` (DB-verified list). Fallback is `ir.default` per company, seeded from company settings by `_set_category_defaults`.
5. **Security gaps by design (UNKNOWN effect)**: no `ir.rule` on `product.product`, `product.category`, `uom.uom`, attributes, tags, packagings; only template/pricelist/rule/vendor line/combo/document are company-ruled. ACL and rule counts equal DB (product 38/6, uom 2/0, analytic 5/4, utm 10/0, resource 8/5). (CAP-U02-08)
6. **Not installed / not observable**: `website_sale` (per-website pricelists) is not installed; DB has no goods or combo products (16 services only), 0 vendor lines, 0 pricelist rules, 0 attributes, analytic group not enabled.

## CAP-U02-01 Product master: definition vs variant, product type, inventory tracking, variants, archive, uniqueness

**Function-ID(s):** RTG-F01 (Product Type x Track Inventory classification: matches), RTG-F04 (Service routing: matches product-side only; order-side routing is out of this unit), all other sub-capabilities `FUNCTION MAPPING REQUIRED`.

### D1 Business purpose and process semantics
A product is maintained once as a *definition* (`product.template`) and once per sellable/stockable combination as a *variant* (`product.product`). Commercial data (name, description, list price, taxes, UoM, policies) lives on the definition; identity and cost data (reference, barcode, standard price, weight, volume) lives on the variant and is mirrored on the definition when exactly one variant exists. In 19 the product type has three values only (`consu`, `service`, `combo`); *whether stock is kept* is a separate boolean `is_storable` ("Track Inventory") that is defined in `stock`, not in `product`. Therefore the effective classification when `stock` is installed is: goods+tracked, goods+untracked ("consumable" behaviour), service, combo. The classification drives fulfilment (stock moves or not), reservation, valuation eligibility, invoicing policy defaults and purchase-control defaults in downstream modules.

### D2 Architecture / data / object relationships
- `product.template` (definition) 1..n `product.product` (variant) via `product_tmpl_id` (cascade). Delegation inheritance (`_inherits`) means variant reads template fields.
- `product.template.attribute.line` (template x attribute) 1..n `product.template.attribute.value` (line x value) ; variant n..m ptav via relation `product_variant_combination`; `combination_indices` (stored, indexed string) + partial unique index gives one active variant per combination.
- `product.attribute` (create_variant always/dynamic/no_variant, display_type) 1..n `product.attribute.value`; exclusions in `product.template.attribute.exclusion`.
- `product.combo` 1..n `product.combo.item` (-> variant); `product.template.combo_ids` m2m.
- `product.uom` (packaging barcode link, see CAP-U02-04), `product.tag`, `product.document` (see CAP-U02-07).
- Extensions studied: `stock` (`is_storable`, `tracking`, routes, company-dependent locations/responsible), `stock_account` (cost method, valuation, lot valuation), `account` (taxes, accounts), `sale`/`sale_stock`/`sale_project`/`sale_purchase`/`purchase`/`purchase_stock` (policies and fulfilment).

### D3 Source / technical / workflow logic
- Variant generation entry points: `product.template.create/write`, attribute-line create/write/unlink, attribute-value-line sync (`_update_product_template_attribute_values`), exclusion create/write/unlink, `product.template.attribute.value.write(exclude_for)`, all converge on `_create_variant_ids` (`product/models/product_template.py:770`). Algorithm: flush; ignore `no_variant` lines; single-value lines merged into existing variants; if no dynamic attribute -> cartesian product of active ptavs filtered by `_filter_combinations_impossible_by_config` (limit param `product.dynamic_variant_limit`, default 1000); else only reactivate existing valid variants; remaining variants -> `_unlink_or_archive` (batch unlink w/ savepoint, dichotomy, fallback archive).
- On-demand creation: `_create_product_variant` (dynamic attributes only; reactivates archived variant; creates via `sudo`).
- Type x tracking: `compute_is_storable` (type!=consu -> False) ; `_compute_tracking` (not storable -> 'none'); `write` (False->True) -> `_reset_inventory` which synthesises quants from done move lines and applies inventory.
- Override/inheritance chain for the classification (effective behaviour = base + overrides when module installed): `product` (type) -> `stock` (`is_storable`, `tracking`) -> `stock_account` (valuation eligibility) -> `sale`/`sale_stock` (invoice policy, delivered qty method, expense policy) -> `purchase`/`purchase_stock` (billing control, received qty method) -> `sale_project`/`sale_purchase` (service routing).

State diagram (lists):
- `Active -> Archived [action_archive on template; cascades to variants and reordering rules]`
- `Active(variant) -> Archived(variant) [last active variant archived => template archived]`
- `Archived -> Active [action_unarchive; template reactivation regenerates variants]`
- `Untracked goods -> Tracked goods [is_storable False->True; quants rebuilt via _reset_inventory]`
- `Tracked goods -> Untracked goods [is_storable True->False; quants kept; tracking forced to none]`
- `Goods -> Service/Combo [type write; is_storable forced False; warning only if moves/sales exist]`

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Create template -> variants generated per attribute mode -> variant carries barcode/reference/cost; set type; (stock) tick Track Inventory. `product/models/product_template.py:567-583`, `stock/models/product.py:839-841`. |
| 2 Reversal / cancel / negative path | Untick Track Inventory keeps quants (`stock/models/product.py:1183-1185`); re-tick only counterbalances unreflected moves; archive instead of delete when referenced (`product/models/product_product.py:750-784`); type change on used product warns only. |
| 3 Multi-company / data-scope | Template `company_id` optional (shared if empty); rule `product_comp_rule` (parent_of company_ids or no company); company change blocked by stock moves/quants (stock) and sales lines (sale); barcode uniqueness is per company (company-less products conflict with all). No rule on product.product (UNKNOWN effect). |
| 4 Side effects / cross-module triggers | Archive -> reordering rules archived (stock); tracking on -> inventory adjustment (stock); variant create -> registry cache clear; type drives purchase_method, invoice_policy, service_type, expense_policy. |
| 5 Configuration and optionality | Variants group (`product.group_product_variant`), `product.dynamic_variant_limit` system parameter, attribute `create_variant`, module `stock` for tracking, module `product_matrix` implies variants for all internal users. |
| 6 Validation and constraints | Combo constraints; attribute line/value constraints; `_combination_unique` index; barcode uniqueness (products + packagings); multi-checkbox CHECK; attribute mode locked once used; company-change locks. |
| 7 Roles and permissions | ACL: internal users read; `product.group_product_manager` (name 'Create') full on template/product/attribute/line/value/exclusion/combo/tag/supplierinfo/pricelist/category (see CAP-U02-08). |
| 8 Scheduled / automated | NOT APPLICABLE - no cron, autovacuum or automation in product (source and DB). |
| 9 Exception and failure behaviour | UserError when variant count exceeds limit, when exclusions would leave no variant, when attribute mode changed while used, when company change blocked; ValidationError on barcode duplicates, combo rules; deletion falls back to archive. |
| 10 Accounting, stock, audit, security, compliance | Tracked goods only are valued (`stock_account`); type/tracking determine whether a move generates valuation entries; tracking switch creates inventory adjustments; `is_storable`, type, company tracked in chatter (`tracking=True` on is_storable, uom_id, list_price, categ_id). |

### DB reconciliation (configuration/structure only)

Restored DB (config only): 16 `product_template` rows, 16 `product_product` rows, all `type='service'`, `is_storable=false`, `tracking='none'` (none are goods or combos); 0 attributes, 0 attribute values, 0 template attribute lines, 0 combos, 0 packaging (`product_uom`) rows, 0 tags, 0 documents. `base.group_user` implies `product.group_product_variant` (group id 20) and `uom.group_uom` (14) and `product.group_product_pricelist` (19). Unique index `product_product_combination_unique` (product_tmpl_id, combination_indices) WHERE active exists; `product_attribute_check_multi_checkbox_no_variant` CHECK exists; `product_uom_barcode_uniq` exists. Parameter `analytic.project_plan`, `product.weight_in_lbs`, `product.volume_in_cubic_feet` present; `product.dynamic_variant_limit` not set (default 1000 applies).

### Unknown / Runtime list

- UNKNOWN - EVIDENCE INSUFFICIENT: whether product.product reads are filtered per company (no explicit ir.rule on product.product; mechanism through delegation inheritance not traced in core). RT: AWT with two companies.
- RT: effect of switching `is_storable` on a product with history (quant rebuild numbers) requires execution.
- RT: dynamic variant creation from an order line and the limit error path require execution.
- UNKNOWN: order-side service routing (create project/task on confirmation) is outside this unit; only product-side configuration studied.
- UNKNOWN: no goods/combo products exist in the DB, so goods-specific defaults (e.g. invoicing policy for goods) are not observable there.

## CAP-U02-02 Product categories and company-dependent properties (accounting, valuation, routing) - hand-off to stock and accounting units

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`. (RTG-F02 Consumable expense timing / RTG-F03 Storable-COGS expense timing consume these properties but belong to other units; not claimed here.)

### D1 Business purpose and process semantics
Finance and logistics want posting accounts, valuation and costing methods, routes and some product-level logistics defaults to be set **once per product family and per company** instead of per product. The category tree holds those defaults; product definitions can override income/expense accounts. The values are *company-dependent*: the same category or product record has one value per company, with a system default (`ir.default`) when a company has none. This unit's modules only define `product.category` itself; the property fields are added by `account`, `stock`, `stock_account`, `mrp_account`, `sale_project`, `sale_purchase` and consumed by accounting and inventory valuation units (hand-off).

### D2 Architecture / data / object relationships
- `product.category` (tree, `parent_path`) 1..n `product.template` via `categ_id`.
- Company-dependent fields are stored as a JSON map {company_id: value} in the field's own column (type `jsonb` observed) with fallback through `ir.default`.
- Company configuration (`res.company`) provides last-resort defaults and, through `_set_category_defaults`, seeds the category defaults (`ir.default` rows scoped by company).
- Resolution chain objects: `product.template` -> `product.category` (and ancestors for income/expense) -> `res.company`.

### D3 Source / technical / workflow logic
Resolution algorithms (effective behaviour = base + overrides when module installed):
- Income/expense (`account/models/product.py:68`): `template.property_account_*_id` -> category chain `_get_category_account` -> `company.income_account_id|expense_account_id` -> `fiscal_position.map_account`.
- Stock valuation / journal (`stock_account/models/product.py:130-156`): `category.property_stock_*` (company context) -> `field.get_company_dependent_fallback(category)` (ir.default for current company) -> `company.account_stock_valuation_id|account_stock_journal_id`. Note: **no category-chain walk** for stock properties (only the product's own category).
- Production (`mrp_account/models/product.py:10`): category value even if empty; fallback only without category and under `real_time` valuation.
- Valuation / costing (`stock_account/models/product.py:60-79`): `category.with_company(company).property_*` else company field; effect on `standard_price` through `_update_standard_price` and `product.value` rows.

State diagram:
- `Category default unset -> Category default set [category write / _set_category_defaults]`
- `Company default (ir.default) -> Category value [explicit write for that company]`
- `Cost method A -> B [category write] => products' standard prices recomputed`

### Hand-off table: company-dependent property fields on product / category / uom / partner (exact list)
Source of list: `ir_model_fields.company_dependent = true` in the restored DB cross-checked to source lines. (U02 owns none of the property fields except `product.product.standard_price` and none of `uom`; all others are consumed by units noted.)

| Model | Field | Type | Defining module | Resolution / fallback | Consumer unit |
|---|---|---|---|---|---|
| product.product | standard_price | float | product | per company; template shows single-variant value | stock valuation / sales margin / purchase |
| product.category | property_account_income_categ_id | m2o account.account | account | ir.default (company) | accounting (invoices) |
| product.category | property_account_expense_categ_id | m2o account.account | account | ir.default (company) | accounting (bills, COGS) |
| product.category | property_valuation | selection periodic/real_time | stock_account | ir.default -> company.inventory_valuation | stock valuation |
| product.category | property_cost_method | selection standard/fifo/average | stock_account | ir.default -> company.cost_method | stock valuation |
| product.category | property_stock_journal | m2o account.journal | stock_account | ir.default -> company.account_stock_journal_id | stock valuation |
| product.category | property_stock_valuation_account_id | m2o account.account | stock_account | ir.default -> company.account_stock_valuation_id | stock valuation |
| product.category | property_price_difference_account_id | m2o account.account | stock_account | none (standard cost only) | accounting / stock valuation |
| product.category | property_stock_account_production_cost_id | m2o account.account | mrp_account | category value (even empty) -> fallback if no category and real_time | manufacturing accounting |
| product.template | property_account_income_id | m2o account.account | account | blank -> category chain | accounting |
| product.template | property_account_expense_id | m2o account.account | account | blank -> category chain | accounting |
| product.template | property_price_difference_account_id | m2o account.account | stock_account | TODO-remove field; unused by resolution | - |
| product.template | responsible_id | m2o res.users | stock | default = creating user (not OdooBot) | inventory |
| product.template | property_stock_production | m2o stock.location | stock | ir.default (1 row) | manufacturing / inventory |
| product.template | property_stock_inventory | m2o stock.location | stock | ir.default (1 row) | inventory adjustments |
| product.template | project_id / project_template_id / task_template_id | m2o | sale_project (also sale_timesheet) | none | sales-project unit |
| product.template | service_to_purchase | boolean | sale_purchase | none | sales/purchase |
| res.partner | specific_property_product_pricelist | m2o product.pricelist | product | no fallback by design | sales pricelist (CAP-U02-03) |
| account.analytic.plan | default_applicability | selection | analytic | ir.default 'optional' | analytic (CAP-U02-06) |

Also company-dependent on partners (owned by other units, listed for completeness by DB): property_account_receivable_id/payable_id, property_account_position_id, property_payment_term_id, property_supplier_payment_term_id, property_stock_customer/supplier/subcontractor, property_delivery_carrier_id, property_inbound/outbound_payment_method_line_id, property_purchase_currency_id, credit_limit, trust, barcode, invoice_sending_method, invoice_edi_format_store, receipt_reminder_email, reminder_date_before_receipt, ignore_abnormal_invoice_*.

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Create category tree; set per-company income/expense/valuation/costing; products inherit; accounts resolved at posting (`account/models/product.py:68-79`). |
| 2 Reversal / cancel / negative path | Clear category value -> falls back to ir.default then company setting; cost method change recomputes prices; no restatement of posted entries. |
| 3 Multi-company / data-scope | Category has no company_id and no record rule (shared across companies); every property is per company; per-company reads need the correct company context (`with_company`). |
| 4 Side effects / cross-module triggers | Category cost-method change -> `_update_standard_price` for all category products; product category change -> recompute; company creation -> `_set_category_defaults` (ir.default). |
| 5 Configuration and optionality | Company settings (valuation, cost method, default income/expense, stock journal/valuation account); modules account / stock_account / mrp_account provide the fields. |
| 6 Validation and constraints | No recursive categories; account domain excludes receivable/payable/cash/credit-card/off-balance; check_company on stock accounts; `ondelete='restrict'` on account links. |
| 7 Roles and permissions | Internal users read category; product manager writes (CAP-U02-08); `standard_price` visible only to base.group_user. |
| 8 Scheduled / automated | NOT APPLICABLE - no scheduled jobs; only event-driven recompute on write. |
| 9 Exception and failure behaviour | Missing account -> empty record returned (no error at resolution); lot valuation enable refused when quants lack lots (stock_account). |
| 10 Accounting, stock, audit, security, compliance | Determines which accounts post income, COGS, stock valuation, price difference and production cost; tracked fields on category (income/expense/valuation/cost method) leave chatter audit; company scoping protects entity separation. |

### DB reconciliation (configuration/structure only)

Restored DB: `product_category` has 5 rows (Goods, Expenses, Services, Events child of Services, Deliveries); category property values for cost method stored as `{"1": "standard"}` on the first three; income/expense/valuation account properties are empty on all categories (chart `th` present but no category-level accounts configured); `ir_default` rows exist for category income/expense, stock journal, valuation account (1 each), valuation and cost method (2 each), template production/inventory locations (1 each) and plan default applicability (1). Single company: valuation `periodic`, cost method `standard`, anglo-saxon off. Company-dependent columns are `jsonb`. `ir_model_fields.company_dependent` = true: product.category 8 fields, product.product 1, product.template 10, res.partner 21 (of which 1 pricelist-related), account.analytic.plan 1 (default_applicability); no company-dependent fields on uom.uom, product.pricelist or product.supplierinfo.

### Unknown / Runtime list

- UNKNOWN - EVIDENCE INSUFFICIENT: physical storage/fallback of company-dependent values is a core ORM mechanism (not in module scope). It was read in core (`odoo/orm/fields.py`, lines ~466-476, 794-801, 1210-1260) but cannot be pointer-checked by the quality script; treat as DISCOVERED SUPPORTING (core).
- RT: resolution with two companies (different category values per company) requires AWT; only one company exists in the DB.
- UNKNOWN: whether category chain should also be walked for stock properties (it is not in source) - semantic difference vs income/expense resolution is recorded as FACT, business intent not inferred.

## CAP-U02-03 Pricelists and price rules: rule types, applicability, computation order, currency, scoping, lookup by sales

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

### D1 Business purpose and process semantics
A pricelist converts the catalogue price of a product into a selling price for a customer context (currency, period, quantity, product/category). It is optional ("Basic Pricelists" feature) and, when enabled, every sales order is priced through exactly one pricelist selected from the partner (own setting, country group, fallback). Rules are fixed price, percentage discount, or formula (base + discount/markup, rounding, surcharge, margins). Purchasing does **not** use these pricelists: vendor prices live on `product.supplierinfo` (CAP-U02-05).

### D2 Architecture / data / object relationships
- `product.pricelist` 1..n `product.pricelist.item` (cascade). Item targets: all / category / template / variant (`applied_on` + `categ_id`, `product_tmpl_id`, `product_id`).
- Item base: `list_price` | `standard_price` | `pricelist` (`base_pricelist_id`), recursion guarded.
- `res.partner.specific_property_product_pricelist` (company-dependent) -> computed `property_product_pricelist`; `res.country.group` m2m pricelists; ir.config_parameter fallbacks `res.partner.property_product_pricelist[_<company_id>]`.
- Sales: `sale.order.pricelist_id` (computed, draft only), `sale.order.line.pricelist_item_id` (computed technical).

### D3 Source / technical / workflow logic
Price lookup (effective behaviour = product base + sale overrides when `sale` installed; website_sale NOT installed):
1. `sale.order.line._compute_pricelist_item_id` -> `pricelist._get_product_rule(product, quantity, uom, date, currency)` -> `_compute_price_rule(compute_price=False)`.
2. `_get_applicable_rules(_domain)` searches rules by pricelist/category ancestry/template/variant/date; default model order is `applied_on, min_quantity desc, categ_id desc, id desc`.
3. Per product: quantity converted to product UoM; first rule passing `_is_applicable_for` wins.
4. `rule._compute_price(product, quantity, uom, date, currency)`: fixed/percentage/formula; base from product (`_price_compute` with attribute extras) or from another pricelist (recursive `_get_product_price`), converted by `currency._convert(..., round=False)`.
5. Sales display price: `_get_display_price` (combo handling) -> pricelist price, and, when discount is shown, `max(price_before_discount, pricelist_price)`.
6. Tax-included conversion afterwards via fiscal position (accounting unit).

State diagram:
- `Draft order: pricelist computed from partner [partner/company change]`
- `Draft order: pricelist changed manually -> lines keep price [flag show_update_pricelist]`
- `Draft order -> Confirmed [pricelist frozen; write refused]`
- `Pricelist Active -> Archived [feature disabled / currency archived / manual]`

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Partner chosen -> pricelist computed -> line product/qty/uom -> rule found -> price_unit set (`sale/models/sale_order_line.py:589-636`). |
| 2 Reversal / cancel / negative path | Change pricelist on draft: only new lines priced until user updates; manual price kept; confirmed order refuses pricelist change; deleting a base pricelist refused. |
| 3 Multi-company / data-scope | Pricelist/rule company-scoped via rules `product_pricelist_comp_rule`/`product_pricelist_item_comp_rule`; partner lookup restricted to current company or no company; one default pricelist per company; per-website scoping only in uninstalled web shop. |
| 4 Side effects / cross-module triggers | Archiving a currency archives pricelists; enabling multi-currency enables feature; company creation creates default list; loyalty/partnership/website modules extend pricelists. |
| 5 Configuration and optionality | `group_product_pricelist` (setting 'Pricelists'); `sale.group_discount_per_so_line`; config parameters for partner fallback; per-company default list. |
| 6 Validation and constraints | Base-pricelist required and acyclic; date range; margin order; target consistency; rule normalisation; negative rounding only onchange-blocked. |
| 7 Roles and permissions | Internal users read pricelist and rules; partner managers read pricelists; product managers full (see CAP-U02-08). |
| 8 Scheduled / automated | NOT APPLICABLE - no cron; activation is event-driven. |
| 9 Exception and failure behaviour | No rule found -> list price; no pricelist -> list price/base conversion; UserError on cycle/delete/confirmed change; empty product recordset returns {}. |
| 10 Accounting, stock, audit, security, compliance | Determines invoiced unit price (before taxes); pricelist, currency and company changes tracked in chatter (`tracking` on currency/company/country groups); cost-based rules read cost as sudo (cost privacy bypass for computed price only). |

### DB reconciliation (configuration/structure only)

Restored DB: 1 pricelist `Default` (active, company 1, currency id 134), 0 `product_pricelist_item` rows, `base.group_user` implies `product.group_product_pricelist` (id 19) so the feature is enabled; 2 active currencies; no `res.partner.property_product_pricelist*` config parameters set; ACL rows for pricelist: user read, partner-manager read, manager full (3 rows) and pricelist item (2 rows); rules `product_pricelist_comp_rule`, `product_pricelist_item_comp_rule` present and global. `website_sale` is not installed (no website pricelist fields).

### Unknown / Runtime list

- RT: rule ordering with several category levels and equal minimum quantities (ordering by categ_id id) requires execution to demonstrate.
- RT: formula rounding/margin outputs and cross-currency base chains require execution.
- UNKNOWN: pricelist usage by point-of-sale, loyalty and partnership extensions not traced (outside this unit).
- UNKNOWN: report 'Pricelist Report' (client action) not studied.

## CAP-U02-04 Units of measure: tree of units, conversion and rounding, change-after-use rules, packagings

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

### D1 Business purpose and process semantics
Quantities and unit prices appear on sales, purchase, stock, manufacturing and accounting lines in a unit chosen per line from the set that the product allows. The unit tree makes those conversions systematic. In 19 there is **no unit category** and **no separate purchase unit** on the product: the product has one base unit (`uom_id`), optional packagings (`uom_ids`, "Packagings") and — only for purchasing — the units named on vendor price lines. Packagings with barcodes are stored as `product.uom` rows (the former packaging model no longer exists in these modules).

### D2 Architecture / data / object relationships
- `uom.uom` tree: `relative_uom_id` (reference), `relative_factor` (contains), `factor` (stored absolute), parent_path; no category field.
- `product.template.uom_id` (m2o required), `product.template.uom_ids` (m2m packagings).
- `product.uom` (uom_id, product_id, barcode unique, company) via `product.product.product_uom_ids`.
- Vendor line `product.supplierinfo.product_uom_id`.
- Document lines: `sale.order.line.product_uom_id`, `purchase.order.line.product_uom_id`, `account.move.line.product_uom_id`, `stock.move.product_uom`, `stock.move.line.product_uom_id` (restricted by `allowed_uom_ids`).
- Global rounding via decimal precision "Product Unit"; weight/volume/length units by ir.config_parameter.

### D3 Source / technical / workflow logic
- `uom._compute_quantity(qty, to_unit, round=True, rounding_method='UP')` — no category test; `_compute_price` is inverse ratio; `_check_qty` rounds to packaging multiples; `_has_common_reference` compares tree roots.
- UoM change on a product (`product.template.write(uom_id)`): `variants._update_uom(new)` (stock, purchase relabel documents or refuse if other units used) then template write; accounting constraint `_check_uom_not_in_invoice` runs after write (blocks if posted journal items use a different unit).
- Ratio change on a unit (`stock` override of `uom.uom.write`): refused if open moves/lines or non-zero quants exist.
- Effective behaviour = `uom` base + `product` (packaging, parameters) + `stock` (ratio lock, reservation, propagate-unit) + `purchase`/`sale`/`account` (allowed units, relabel, posted lock).

State diagram:
- `Unit Active -> Archived [manual; imperial seeds archived]`
- `Product unit A -> B [allowed only if documents (moves, move lines, purchase lines) use only A; posted entries must not use another unit]`
- `Unit ratio X -> Y [refused while open moves/lines or quants exist (stock)]`

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Choose base unit on product; pick allowed unit on a line; quantity/price converted via factor ratio; rounded in target unit. |
| 2 Reversal / cancel / negative path | Unit change refused when other units used on stock/purchase documents; ratio change refused with open moves; archive instead of delete for protected units. |
| 3 Multi-company / data-scope | uom.uom has no company field and no record rule (global master data); `product.uom` rows carry a company field (default current company) but no rule exists. |
| 4 Side effects / cross-module triggers | Unit change relabels purchase lines, moves and move lines; packaging barcode participates in barcode uniqueness; timesheet/EDI use common-root test. |
| 5 Configuration and optionality | `uom.group_uom` (setting 'Units of Measure & Packagings'), weight/volume config parameters, 'Product Unit' decimal precision, `stock.propagate_uom` parameter. |
| 6 Validation and constraints | relative_factor != 0; root units must have factor 1; protected units cannot be deleted; packaging barcode unique and distinct from product barcodes; posted-entry unit lock. |
| 7 Roles and permissions | Internal users read; system admin and product manager write (2 ACL rows in uom plus product-module manager row). |
| 8 Scheduled / automated | NOT APPLICABLE - none. |
| 9 Exception and failure behaviour | UserError on blocked unit/ratio changes; no exception on cross-root conversion (silent numeric result). |
| 10 Accounting, stock, audit, security, compliance | Unit consistency protects valuation (stock quants/moves), posted journal quantities and invoice units; ratio lock avoids revaluation of open quantities; no audit tracking on unit fields except `uom_id` on product (tracking=True). |

### DB reconciliation (configuration/structure only)

Restored DB: `uom_uom` has 30 rows (e.g. units, pack of 6, hours/days/minutes, mm..km, m2, ml/L/m3, g/kg/ton, imperial units mostly archived, KWH); columns: id, sequence, relative_uom_id, parent_path, name, relative_factor, factor, active, package_type_id, timesheet_widget (no category column); `product_uom` has 0 rows; ACL rows: 2 in module uom, matches source; `uom.group_uom` (id 14) implied by `base.group_user`; decimal precision `Product Unit` = 2. Constraint `uom_uom_factor_gt_zero` and `product_uom_barcode_uniq` present.

### Unknown / Runtime list

- RT: cross-root conversion behaviour (silent numeric result) is inferred from reading; execution needed to confirm.
- RT: unit-change refusal paths across sale/stock/purchase documents require execution with documents.
- UNKNOWN: manufacturing and point-of-sale unit logic not traced beyond allowed-unit lists.
- UNKNOWN: client-side widget behaviour (unit selector) not studied.

## CAP-U02-05 Vendor price lines on the product (supplier info): selection, validity, minimum quantity, currency, company scope

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`. (Hand-off to the purchase unit U06: vendor selection is consumed there; only the definition and the selection algorithm are studied here.)

### D1 Business purpose and process semantics
`product.supplierinfo` ("Supplier Pricelist") stores what each vendor charges for a product, per minimum quantity, unit, currency, validity window and delivery lead time. Purchase order lines, replenishment (reordering rules / procurement), vendor bills and service resale call a single selection routine to pick the best line.

### D2 Architecture / data / object relationships
- `product.supplierinfo` n..1 `res.partner` (vendor), n..1 `product.template` (required), n..1 `product.product` (optional variant), n..1 `uom.uom`, `res.currency`, `res.company`.
- `product.template.seller_ids` (company-context dependent) / `variant_seller_ids`.
- Extensions: `purchase` (currency onchange, order company in filter), `purchase_requisition` (agreement link and filter), `mrp_subcontracting` (subcontractor filter), `purchase_stock` (replenishment), `sale_purchase`.

### D3 Source / technical / workflow logic
`product.product._select_seller(partner_id, quantity, date, uom_id, ordered_by, params)`:
1. `_prepare_sellers(params)`: lines of the product (sudo) -> `_get_filtered_supplier(company, product, params)` -> sort `(sequence, -min_qty, price, id)` (+ overrides: requisition, subcontracting).
2. `_get_filtered_sellers`: skip by date window, forced unit, partner (or parent), min quantity in line unit, variant mismatch.
3. `_select_seller`: take lines until a different partner appears; sort by `price_discounted` converted into company currency (round=False), then sequence, id; return first.
Order-line use: `purchase.order.line._compute_selected_seller_id` and `_prepare_purchase_order_line` (price conversion, planned date = order date + delay).

State diagram:
- `Vendor line valid -> not applicable [date_start > date or date_end < date]`
- `Vendor line applicable -> selected [lowest discounted price of first vendor]`

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Define vendor lines on product; create purchase order -> selected_seller_id -> price, date, name. |
| 2 Reversal / cancel / negative path | No eligible line -> price 0 / no seller; quantity below minimum -> line skipped; `quantity=None` flows ask for any vendor. |
| 3 Multi-company / data-scope | Line `company_id` default current company; empty = shared; filter and record rule `product_supplierinfo_comp_rule`; purchase uses the order's company. |
| 4 Side effects / cross-module triggers | Lead time feeds planned dates (calendar days); display names and searches use vendor codes; agreements and subcontracting filter lines. |
| 5 Configuration and optionality | Currency per line; unit per line; validity dates optional; shared vs company-specific; no switch. |
| 6 Validation and constraints | Required fields; cascade deletes; no overlapping-validity constraint exists (UNKNOWN effect of overlaps handled only by ordering). |
| 7 Roles and permissions | Internal users read; product manager full; global company rule. |
| 8 Scheduled / automated | NOT APPLICABLE - none. |
| 9 Exception and failure behaviour | No exception when no vendor found (empty recordset); silent skip of inactive vendors/other-company lines. |
| 10 Accounting, stock, audit, security, compliance | Determines vendor price, currency conversion and planned dates on purchase documents; no chatter tracking on vendor lines. |

### DB reconciliation (configuration/structure only)

Restored DB: `product_supplierinfo` has 0 rows (no vendor prices configured). ACL: `access_product_supplierinfo_user` (read) and `access_product_supplierinfo_manager` (full). Record rule `product.product_supplierinfo_comp_rule` present as a global rule.

### Unknown / Runtime list

- RT: selection result when lines from several vendors overlap on dates/quantities requires execution.
- UNKNOWN: no constraint prevents overlapping validity windows for the same vendor/product; business handling is by ordering only.
- UNKNOWN: vendor lines in other currencies than the company currency use conversion at the selection date (round=False) - end results with rates not exercised.

## CAP-U02-06 Analytic accounting: plans, accounts, applicability, distribution models, analytic lines, attachment to documents

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`. (Hand-off: how distribution attaches to documents -> U13 (accounting posting) and U11 (sales/purchase documents).)

### D1 Business purpose and process semantics
Analytic accounting records cost/revenue by dimensions (plans such as project, department) independently from general-ledger accounts. A **plan** is a dimension; an **analytic account** belongs to a plan; documents carry an **analytic distribution** (percentage split across accounts); posting a journal item creates **analytic lines** that carry plan-specific account columns. **Applicability** (optional/mandatory/unavailable) per plan, company, business domain, account prefix and product category controls where analytic coding is requested or required. **Distribution models** prefill distributions from partner / partner category / product / product category / account prefix / company.

### D2 Architecture / data / object relationships
- `account.analytic.plan` (tree) 1..n `account.analytic.account`; `account.analytic.applicability` n..1 plan; `account.analytic.distribution.model` (mixin `analytic.mixin`).
- Dynamic columns: for each root plan `x_plan<id>_id` (the project plan uses `account_id`) is created on every model that inherits `analytic.plan.fields.mixin` (analytic line and others); sub-plans create non-stored related grouping fields.
- Documents with `analytic.mixin`: `sale.order.line`, `purchase.order.line`, `account.move.line`, `hr.expense`, `purchase.requisition`, `mrp.workcenter` (and others found by grep).
- `account.analytic.line` -> `account.move.line` (move_line_id) via `account` extension; `product_id`, `general_account_id`, `partner_id` computed from the journal item.
- `analytic_distribution` is stored Json: {"id1,id2": percent}; key = comma-joined account ids (one per plan).

### D3 Source / technical / workflow logic
- Attachment to documents: line `analytic_distribution` is a **computed stored** field on sales/purchase lines (`_compute_analytic_distribution` -> `account.analytic.distribution.model._get_distribution({product, product_categ, partner, partner_category, company})`) and on journal items (`account.move.line._compute_analytic_distribution` merges related-document distribution and model results, with `account_prefix` and plans already served).
- Validation: `analytic.mixin._validate_distribution` (context `validate_analytic`) checks 100% for mandatory plans; `account.move.line._validate_analytic_distribution` called in `_create_analytic_lines` at posting.
- Line creation: `account.move.line._create_analytic_lines` -> `_prepare_analytic_lines` per distribution key -> `_round_analytic_distribution_line`; `account.analytic.line.create` triggers `_update_analytic_distribution` on source items.
- Effective behaviour = `analytic` base + `account` (move-line link, applicability domains, model criteria) + `purchase`/`sale`/`hr_timesheet`/`hr_expense`/`project_stock_account` (extra business domains).

State diagram:
- `Account Active -> Archived [manual]`
- `Journal item (draft) with distribution -> posted -> analytic lines created [posting]`
- `Posted -> reset/reversed -> analytic lines removed [cascade via move_line_id ondelete cascade]`
- `Plan created -> column created [sync]` ; `Plan deleted -> column dropped`

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Define plan and accounts; set applicability; distribution model prefill on line; post invoice -> analytic lines (`account/models/account_move_line.py:3221-3281`). |
| 2 Reversal / cancel / negative path | Reset/reverse -> lines removed through cascade on journal item; moving accounts between plans blocked when overwriting; distribution edit on analytic line re-splits lines. |
| 3 Multi-company / data-scope | Account company optional (shared if empty); analytic lines require company and rule `[company_id in company_ids]`; applicability and models scoped by company; company-specific accounts cannot be in shared models. |
| 4 Side effects / cross-module triggers | Plan creation changes table structure of all mixin models; posting creates lines; sale/purchase lines prefill from models; timesheet/expense/stock add business domains. |
| 5 Configuration and optionality | Analytic setting (group); `analytic.project_plan` parameter; plan default applicability per company; applicability rules; distribution models; 'Percentage Analytic' precision. |
| 6 Validation and constraints | 100% for mandatory plans; at least one account per line; no parent for base plan; company-change lock; model company consistency; line account must match journal item account. |
| 7 Roles and permissions | All five analytic models: group `analytic.group_analytic_accounting` full; four global company rules. |
| 8 Scheduled / automated | NOT APPLICABLE - none. |
| 9 Exception and failure behaviour | ValidationError/RedirectWarning at posting for missing 100%; UserError for invalid project plan parameter; RedirectWarning on data-overwriting moves. |
| 10 Accounting, stock, audit, security, compliance | Analytic lines mirror posted journal items (amount = -balance * percent); rounding differences redistributed; chatter tracking on account name/code/partner/company/active; analytic data is isolated by company rule; deleting a plan drops data. |

### DB reconciliation (configuration/structure only)

Restored DB: `account_analytic_plan` 1 row (Project, no parent); `account_analytic_account` 1 row; `account_analytic_line` 2 rows (config/demo-like, not inspected); `account_analytic_applicability` 0; `account_analytic_distribution_model` 0; `analytic.project_plan` = 1; decimal precision `Percentage Analytic` = 2; ACL rows 5 and rules 4 for module analytic match the source; `analytic.group_analytic_accounting` (id 18) is not implied by any other group in the DB and no user membership was found (feature not switched on); `ir_default` has 1 row for plan default applicability.

### Unknown / Runtime list

- RT: plan creation/rename column synchronisation and drop-on-delete behaviour require execution (DDL side effects).
- RT: distribution model merge when several plans/models match requires execution to demonstrate numerical output.
- UNKNOWN: the 2 analytic lines present in the DB were not inspected (business-data guard); origin (module data vs manual) unknown.
- UNKNOWN: models inheriting the mixin outside the studied set (project, expense modules) were only listed, not traced.

## CAP-U02-07 Product documents, combos, tags, attribute exclusions, catalog helper and bulk attribute wizard (brief)

**Function-ID(s):** `FUNCTION MAPPING REQUIRED` (brief coverage).

### D1 Business purpose and process semantics
Supporting master data around products: shareable **documents**, marketing **tags**, **combos** (bundle of choice groups), **attribute exclusions** (incompatible values) and two maintenance helpers (catalog view mixin, bulk attribute-value wizard). Combos' core product-type rules are in CAP-U02-01.

### D2 Architecture / data / object relationships
- `product.document` -> `ir.attachment` (delegation), keyed by `res_model/res_id` (template or variant).
- `product.tag` m2m `product.template` (`product_tag_product_template_rel`) and `product.product` (`product_tag_product_product_rel`).
- `product.combo` 1..n `product.combo.item` -> `product.product`; `product.template.combo_ids` m2m.
- `product.template.attribute.exclusion` (template, ptav) m2m excluded ptavs.
- `update.product.attribute.value` (transient) -> bulk write on attribute lines / values.
- `product.catalog.mixin` (abstract) used by order documents.

### D3 Source / technical / workflow logic
- Chatter attachment -> `ir.attachment.create` override -> `product.document.create` (sudo) unless flagged.
- Exclusion create/write/unlink -> `product.template._create_variant_ids` (variant regeneration); exclusion data used by `_get_own_attribute_exclusions`, `_filter_combinations_impossible_by_config`, `_cartesian_product`.
- Wizard `action_confirm` -> `_add_value_to_existing_attribute_lines` or `_update_extra_price_on_existing_products` (company-limited writes), each triggering attribute-line/value sync and variant generation.

State diagram:
- `Document Active -> Archived [active flag]`
- `Exclusion defined -> variants regenerated [create/unlink]`

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Upload file in chatter -> document; define combo and add to combo product; define exclusion -> variants regenerated. |
| 2 Reversal / cancel / negative path | Document delete deletes attachment; exclusion removal regenerates variants; combo item removal via variant removal. |
| 3 Multi-company / data-scope | Document and combo company rules; tags/attributes have no company scope; wizard limited to user's companies. |
| 4 Side effects / cross-module triggers | Exclusions and wizard regenerate variants; chatter attachments auto-create documents; catalog mixin used by sales/purchase documents. |
| 5 Configuration and optionality | No switch; presence of web-shop modules extends tag/document use (not installed). |
| 6 Validation and constraints | Tag name unique; combo item and group constraints; URL scheme warning (onchange). |
| 7 Roles and permissions | Internal read; product manager full; wizard manager rwc. |
| 8 Scheduled / automated | NOT APPLICABLE - none. |
| 9 Exception and failure behaviour | ValidationError on combo/URL issues; UserError if exclusions leave no variants. |
| 10 Accounting, stock, audit, security, compliance | No direct accounting; documents expose customer-shared files (security via company rule only); no tracking on these models. |

### DB reconciliation (configuration/structure only)

Restored DB: 0 `product_document`, 0 `product_tag`, 0 `product_combo`, 0 `product_attribute*`, 0 exclusions; constraints `product_tag_name_uniq` present; ACL rows for these models present (document 2, tag 2, combo 2, combo item 2, exclusion 2, wizard 1).

### Unknown / Runtime list

- UNKNOWN: label printing wizard (`product.label.layout`) not studied.
- RT: bulk wizard effect on large catalogues and variant regeneration requires execution.

## CAP-U02-08 Roles, access rights, record rules and multi-company scoping on product, pricelist, unit, analytic, tracker and calendar objects

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

### D1 Business purpose and process semantics
Defines who may read/maintain the product master, pricing master data, units, analytic dimensions, marketing trackers and calendars, and how data is isolated between companies.

### D2 Architecture / data / object relationships
Groups: `base.group_user` (read), `product.group_product_manager` ("Create", implied by `base.group_system`), `base.group_partner_manager` (pricelist read), `analytic.group_analytic_accounting`, feature groups `product.group_product_pricelist`, `product.group_product_variant`, `uom.group_uom` (feature switches, no ACL). Record rules are global (no groups) company rules.

### D3 Source / technical / workflow logic
ACL rows come from `ir.model.access.csv`; rules from `*_security.xml` (`noupdate="1"` for rules). `check_company` / `_check_company_auto` enforce company consistency of relations at write time. Rule domains use `parent_of company_ids` (child companies see ancestors' shared data).

#### ACL / rule matrix (declared)
| Model | Internal user (base.group_user) | Product manager | Other | Company rule |
|---|---|---|---|---|
| product.template | R | CRUD | - | yes (company parent_of or none) |
| product.product | R | CRUD | - | none declared |
| product.category | R | CRUD | - | none |
| product.attribute / value / custom value / ptav / exclusion / line | R | CRUD | - | none |
| product.pricelist | R | CRUD | partner manager R | yes |
| product.pricelist.item | R | CRUD | - | yes |
| product.supplierinfo | R | CRUD | - | yes |
| product.tag | R | CRUD | - | none |
| product.combo / item | R | CRUD | - | combo yes; item none (company stored related) |
| product.document | R | CRUD | - | yes |
| product.uom (packaging) | R | CRUD | - | none |
| uom.uom | R | CRUD | system admin CRUD | none |
| update.product.attribute.value | - | CRU | - | n/a (transient) |
| product.label.layout | CRUD | - | - | n/a |
| account.analytic.* (5 models) | - | - | group_analytic_accounting CRUD | accounts/applicability/models: shared or parent_of; lines: company_id in company_ids |
| utm.campaign/medium/source | R,W,C | - | system admin CRUD | none |
| utm.stage / utm.tag | R | - | system admin CRUD | none |
| resource.calendar / attendance | R | - | system admin CRUD | none (calendar company field only) |
| resource.resource | R | - | system admin R | company_ids + False |
| resource.calendar.leaves | CRUD with rules | - | admin (erp manager) modify global | multi-company + own/global rules |

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Internal user reads catalogue; product manager creates/changes; company rule limits to allowed companies. |
| 2 Reversal / cancel / negative path | Non-managers get AccessError on write/delete; trackers cannot be deleted by non-admin; protected units/categories rules per capability. |
| 3 Multi-company / data-scope | Company rules on template, pricelist, item, supplierinfo, combo, document, analytic account/line/applicability/model, resource objects; no rule on category/attribute/unit/tag/variant. |
| 4 Side effects / cross-module triggers | `group_user` implied-group switches (variants, pricelist, multiple units) set by other modules and settings. |
| 5 Configuration and optionality | Feature groups toggled in Settings; analytic group not implied in DB. |
| 6 Validation and constraints | check_company on relations; ACL/rule counts reconciled to DB. |
| 7 Roles and permissions | See matrix above; declared groups 5, ACL rows 63 (38+2+5+10+8), rules 15 (6+4+5). |
| 8 Scheduled / automated | NOT APPLICABLE. |
| 9 Exception and failure behaviour | AccessError for unauthorised operations; UserError/ValidationError cited per capability. |
| 10 Accounting, stock, audit, security, compliance | Cost field privacy; analytic access limited to a separate group; company isolation relies on rules and consistency checks; gaps recorded as UNKNOWN. |

### DB reconciliation (configuration/structure only)

Restored DB: ACL rows by module: product 38, uom 2, analytic 5, utm 10, resource 8 (equal to source); record rules: product 6 (all global), analytic 4 (all global), resource 5 (2 global), uom 0, utm 0 (equal to source). No `ir.rule` rows exist for product.product, product.category, uom.uom, product.attribute, product.template.attribute.value, product.combo.item, product.uom or product.tag. Groups from these modules: group_product_manager (id 21, 2 members), group_product_pricelist (19), group_product_variant (20), group_uom (14), group_analytic_accounting (18); `base.group_user` (1) implies 14, 19 and 20 but not 18; no users in group 18. No crons and no base_automation rows for these modules.

### Unknown / Runtime list

- RT: two-company test of product.product visibility and of shared-unit/attribute data required (variants have no rule).
- UNKNOWN: ACL for models extended by other modules (e.g. stock, sale) are out of this unit.

## CAP-U02-09 Scheduled and automated behaviour; configuration and optionality switches

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

### D1 Business purpose and process semantics
Documents which behaviours are automatic (event-driven) and which switches/parameters make the capabilities optional.

### D2 Architecture / data / object relationships
- Settings model `res.config.settings` extended by `product` (`group_uom`, `group_product_variant`, `group_product_pricelist`, `module_loyalty`, weight/volume units) and `analytic` (`group_analytic_accounting`).
- Parameters in `ir.config_parameter` (see table).
- Event hooks: `res.company.create/write`, `res.currency.write/_activate_group_multi_currency`, `res.config.settings.set_values`.

| Switch / parameter | Defined in | Effect | DB state |
|---|---|---|---|
| `product.group_product_variant` | product | variant UI/features | implied by base.group_user (via product_matrix) |
| `product.group_product_pricelist` | product | pricelists enabled; default list per company | implied by base.group_user; 1 default list |
| `uom.group_uom` | uom (setting in product) | multiple units/packagings UI | implied by base.group_user (via sale_timesheet) |
| `analytic.group_analytic_accounting` | analytic | analytic permissions/UI | not implied; no members |
| `product.weight_in_lbs` | product | weight unit lb vs kg | parameter present |
| `product.volume_in_cubic_feet` | product | volume/length units | parameter present |
| `product.dynamic_variant_limit` | product (read in code) | max variants generated | not set (default 1000) |
| `analytic.project_plan` | analytic | identity of project plan | 1 |
| `res.partner.property_product_pricelist[_<company>]` | product (read in code) | partner pricelist fallback | not set |
| `stock.propagate_uom` | stock (read in code) | propagate procurement unit | not set |
| `account.product_name_similarity_threshold` | account (read in code) | invoice-import name match | present |

### D3 Source / technical / workflow logic
Settings `set_values` (`product/models/res_config_settings.py:36`) -> `res.company._activate_or_create_pricelists`; company write wraps the parent write with `disable_company_pricelist_creation`. No `ir.cron`, no `@api.autovacuum`, no `base.automation` in the five modules (grep and DB).

State diagram:
- `Pricelist feature Off -> On [settings] => default pricelists created/reactivated`
- `Pricelist feature On -> Off [settings] => all pricelists archived`

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Toggle feature in Settings -> group applied -> default records created. |
| 2 Reversal / cancel / negative path | Disabling pricelists archives all lists (re-enable reactivates default list). |
| 3 Multi-company / data-scope | Per-company default price list and default calendar; parameters can be company-keyed for partner fallback. |
| 4 Side effects / cross-module triggers | Other modules imply the feature groups; multi-currency activation enables price lists. |
| 5 Configuration and optionality | See table above. |
| 6 Validation and constraints | Project plan parameter validated on write; others unvalidated. |
| 7 Roles and permissions | Settings require system administration; groups listed in CAP-U02-08. |
| 8 Scheduled / automated | No cron, no autovacuum, no automation rule in the five modules (source + DB). |
| 9 Exception and failure behaviour | UserError on invalid project plan parameter; warnings on onchange for pricelist disable. |
| 10 Accounting, stock, audit, security, compliance | Parameters change valuation-adjacent behaviour only through other units; settings changes are system configuration (audit via normal write logs, not chatter). |

### DB reconciliation (configuration/structure only)

Restored DB: `ir_cron` rows owned by product, uom, analytic, utm, resource = 0; `base_automation` rows = 0 (grep of source also finds no cron/autovacuum). Config parameter keys present: `analytic.project_plan`, `product.volume_in_cubic_feet`, `product.weight_in_lbs`, `account.product_name_similarity_threshold`. Feature groups: base.group_user implies uom.group_uom (14), product.group_product_pricelist (19), product.group_product_variant (20); analytic.group_analytic_accounting (18) not implied.

### Unknown / Runtime list

- UNKNOWN: other installed modules might add crons touching product/pricelist/analytic objects; only these five modules were searched.
- RT: toggling of pricelist feature (archive/reactivate) requires execution to observe default list reuse.

## CAP-U02-10 Marketing trackers (utm) and working calendars (resource): what they give the core chains (light touch)

**Function-ID(s):** `FUNCTION MAPPING REQUIRED` (light-touch coverage by design).

### D1 Business purpose and process semantics
- **utm**: three marketing tags (campaign, medium, source) copied onto sales orders and invoices so revenue can be attributed. Values arrive from URL parameters -> cookies -> default values on creation, or are picked by users.
- **resource**: working calendars (weekly periods, time off) plus helpers to plan hours/days. **Finding:** in the Community modules installed here, Sales, Purchase and Inventory lead times are NOT based on working calendars; they use calendar-day arithmetic (`relativedelta(days=...)`, `timedelta(days=...)`). Working calendars are consumed by manufacturing work centers (and HR / project modules outside this unit).

### D2 Architecture / data / object relationships
- `utm.mixin` (abstract; campaign_id, source_id, medium_id) inherited by `sale.order` and `account.move` (sale), `crm.lead` (not in this unit).
- `utm.campaign` (stage, tags, responsible), `utm.medium`, `utm.source`, `utm.stage`, `utm.tag`; `sale` extends `utm.campaign` with quotation counts and invoiced revenue.
- `resource.calendar` 1..n `resource.calendar.attendance`; `resource.calendar.leaves` (company or resource); `resource.resource` (user/work center) -> calendar; `res.company.resource_calendar_id`.

### D3 Source / technical / workflow logic
- Tracking: website visit -> `ir.http._post_dispatch/_set_utm` sets cookies -> `utm.mixin.default_get` fills fields -> `sale.order._prepare_invoice` copies to invoice -> `utm.campaign` statistics.
- Names: `_get_unique_names` suffix logic on create/write for campaign, medium, source.
- Planning: `resource.calendar.plan_hours/plan_days` iterate fortnight windows up to 100 times; used by `mrp` work orders.
- Lead time chain (days): sale line `customer_lead` / company `security_lead` -> stock rule `delay` -> purchase `seller.delay`, `days_to_purchase`.

State diagram:
- `Visit with utm params -> cookie set [31 days] -> new document defaults tracker fields`
- `Quotation -> Invoice [copy trackers]`

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Visitor arrives with utm parameters -> cookie -> quotation created with trackers -> invoice copies trackers -> campaign shows revenue. |
| 2 Reversal / cancel / negative path | Deleting a tracker nulls it on documents; protected seeded mediums/source cannot be deleted; draft/cancelled invoices excluded from revenue. |
| 3 Multi-company / data-scope | Trackers have no company scope (campaign gains company in sale); calendars company-scoped by field; resource objects by company rule. |
| 4 Side effects / cross-module triggers | Sales campaign stats; manufacturing planning uses calendars; lead times independent of calendars. |
| 5 Configuration and optionality | No switches; website cookies need the web layer; sales reps skip automatic UTM defaults. |
| 6 Validation and constraints | Unique tracker names; overlapping attendance blocked; time off dates ordered. |
| 7 Roles and permissions | See CAP-U02-08 matrix. |
| 8 Scheduled / automated | NOT APPLICABLE - no cron. |
| 9 Exception and failure behaviour | UserError/ValidationError on deleting protected tracker records; planning helpers return False when no slot is found within 100 fortnights. |
| 10 Accounting, stock, audit, security, compliance | Trackers are reporting attributes on invoices (no accounting effect); calendars influence only scheduling in manufacturing; lead-time assumptions are calendar days. |

### DB reconciliation (configuration/structure only)

Restored DB: utm_campaign 1, utm_medium 11, utm_source 13, utm_stage 1, utm_tag 1; resource_calendar 1 (15 attendance rows), resource_resource 1, resource_calendar_leaves 0; `res.company.resource_calendar_id` set; ACL rows utm 10 and resource 8; resource rules 5 (2 global); no sale orders/invoices exist, so tracker propagation is not observable.

### Unknown / Runtime list

- RT: cookie-to-document defaulting and invoice propagation require execution (web request).
- UNKNOWN: use of resource calendars by hr_holidays, hr_work_entry, project and employee functions (outside this unit).

## DISCOVERED SUPPORTING MODULES (read only as far as needed)

`account` (product accounts, taxes, analytic line creation, applicability criteria), `stock`, `stock_account`, `mrp_account` (property fields and valuation), `sale`, `sale_stock`, `sale_project`, `sale_purchase`, `sale_timesheet` (data only), `purchase`, `purchase_stock`, `purchase_requisition`, `mrp_subcontracting`, `mrp` (calendar use), `hr_timesheet`, `project_stock_account`, `product_matrix` (data only), `account_edi_ubl_cii` (common-root test), `website_sale` (source only - not installed in DB), core `orm/fields.py`.

## Contradictions with prior evidence / assignment premises

- Assignment premise 'working-calendar based lead-time' for Sales/Purchase/Inventory: **not supported by source** (calendar-day arithmetic; see CAP-U02-10). (Not a contradiction with prior evidence, so no `CONTRA` flag is set; recorded here for the controller.)
- Assignment premise 'UoM categories/relations in 19': there are **no unit categories**; only a tree of reference units (CAP-U02-04). Prior candidate map `MODULE_uom.md` agrees (no contradiction with prior evidence; contradiction only with the assignment wording).
- Prior candidate map `MODULE_uom.md` statement A8 (sale_timesheet implies group_uom for internal users) is confirmed by source and DB.

## Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U02-C001 | RTG-F01 | product/models/product_template.py:54-65 | ('combo', "Combo") | FACT | always | — | Product type selection has three values consu (Goods), service, combo; the field is required with default consu. | N-U02-003 |
| VDR-U02-C002 | RTG-F01 | product/models/product_template.py:269-290 | variant_count == 1 | FACT | always | — | Template-level fields barcode/default_code/weight/volume/standard_price are computed from the variant only when exactly one variant exists; otherwise the supplied default (blank) is set. | N-U02-002 |
| VDR-U02-C003 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:292-308 | count == 1 | FACT | always | — | Writing such a field on the template propagates to the single variant (or to a single archived variant if no active variant). | N-U02-002 |
| VDR-U02-C004 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:16-20 | _inherits | FACT | always | — | product.product inherits product.template by delegation (_inherits), so each variant exposes template fields through product_tmpl_id. | N-U02-001 |
| VDR-U02-C005 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:42-47 | ondelete="cascade" | FACT | always | — | Variant requires a template (cascade on delete); barcode is a variant field, copy=False, btree index where not null. | N-U02-001 |
| VDR-U02-C006 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:119-121 | _combination_unique | FACT | always | — | Unique index on (product_tmpl_id, combination_indices) WHERE active IS TRUE: at most one active variant per attribute-value combination. | N-U02-058 |
| VDR-U02-C007 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:300-303 | _ids2str | FACT | always | — | combination_indices is the sorted comma-joined ids of the variant's template attribute values (stored, indexed). | N-U02-058 |
| VDR-U02-C008 | RTG-F01 | stock/models/product.py:839-841 | Track Inventory | FACT | module stock installed | — | is_storable (label 'Track Inventory') is a stored computed boolean, readonly=False, default False, precompute, tracked in chatter, added by stock. | N-U02-004 |
| VDR-U02-C009 | RTG-F01 | stock/models/product.py:911-913 | t.type != 'consu' | FACT | module stock installed | — | compute_is_storable depends on type and forces is_storable=False for any template whose type is not consu (service or combo). | N-U02-010 |
| VDR-U02-C010 | RTG-F01 | stock/models/product.py:1094-1096 | tracking != 'none' | FACT | module stock installed | — | Tracking (serial/lot/none) is reset to 'none' whenever is_storable is False. | N-U02-011 |
| VDR-U02-C011 | RTG-F01 | stock/models/product.py:856-862 | By Unique Serial Number | FACT | module stock installed | — | tracking selection is serial / lot / none, required, default none, stored computed (editable). | N-U02-011 |
| VDR-U02-C012 | RTG-F01 | stock/models/product.py:1129-1160 | _reset_inventory | FACT | module stock installed | — | write(): when is_storable goes from False to True, quant reservations are cleaned and _reset_inventory is called for the templates that became storable. | N-U02-012 |
| VDR-U02-C013 | RTG-F01 | stock/models/product.py:1162-1202 | _apply_inventory | FACT | module stock installed | — | _reset_inventory rebuilds quants from done move lines (internal/transit) and applies an inventory adjustment so valuation is consistent; quantities already on hand are not counted twice. | N-U02-012 |
| VDR-U02-C014 | RTG-F01 | stock/models/product.py:1183-1185 | keeps the existing quants | FACT | module stock installed | — | Unticking Track Inventory keeps existing quants; a later re-tick only counterbalances moves not already reflected on hand. | N-U02-041 |
| VDR-U02-C015 | RTG-F01 | stock/models/stock_rule.py:447-450 | != "consu" | FACT | module stock installed | — | _skip_procurement returns True when the product type is not consu or the quantity is zero: services and combos never generate stock procurement. | N-U02-013 |
| VDR-U02-C016 | RTG-F01 | stock/models/stock_move.py:1967-1970 | is_storable | FACT | module stock installed | — | _should_bypass_reservation is true when the location bypasses reservation or the product is not storable: non-tracked goods are never reserved. | N-U02-014 |
| VDR-U02-C017 | RTG-F01 | stock/models/stock_move.py:514-516 | not_product_moves | FACT | module stock installed | — | For moves of non-storable products the forecast availability is simply the move quantity (no forecast computation). | N-U02-014 |
| VDR-U02-C018 | RTG-F01 | stock_account/models/stock_move.py:660-666 | self.product_id.is_storable | FACT | module stock_account installed | — | Journal-entry eligibility of a stock move requires product is_storable and is_valued and a valuation account on a location. | N-U02-015 |
| VDR-U02-C019 | RTG-F01 | stock_account/models/account_move_line.py:30-35 | is_storable | FACT | module stock_account installed | — | _eligible_for_stock_account returns False for non-storable products and for dropshipped moves. | N-U02-015 |
| VDR-U02-C020 | RTG-F01 | sale_stock/models/sale_order_line.py:190-193 | stock_move | FACT | module sale_stock installed | — | Sales lines for goods (type consu, not expense) get qty_delivered_method 'stock_move'. | N-U02-016 |
| VDR-U02-C021 | RTG-F01 | sale_stock/models/sale_order_line.py:395-399 | != 'consu' | FACT | module sale_stock installed | — | Procurement launch on a confirmed order skips lines whose product type is not consu. | N-U02-013 |
| VDR-U02-C022 | RTG-F01 | sale_stock/models/sale_order_line.py:426-430 | cannot be decreased below | FACT | module sale_stock installed | — | The ordered quantity of a goods line cannot be decreased below the delivered quantity; a return must be created. | N-U02-016 |
| VDR-U02-C023 | RTG-F01 | sale_stock/models/sale_order_line.py:54-59 | line.is_storable | FACT | module sale_stock installed | — | The on-hand/forecast widget on a sales line is shown only for storable products with quantity still to deliver. | N-U02-014 |
| VDR-U02-C024 | RTG-F01 | purchase_stock/models/purchase_order_line.py:38-41 | stock_moves | FACT | module purchase_stock installed | — | Purchase lines for goods get qty_received_method 'stock_moves'. | N-U02-017 |
| VDR-U02-C025 | RTG-F01 | purchase_stock/models/purchase_order_line.py:169-172 | _create_or_update_picking | FACT | module purchase_stock installed | — | Picking creation for a purchase line only happens for products of type consu. | N-U02-017 |
| VDR-U02-C026 | RTG-F01 | purchase_stock/models/purchase_order.py:378-381 | type == 'consu' | FACT | module purchase_stock installed | — | Receipt creation/update for a confirmed order is triggered only when the order contains at least one consu product. | N-U02-017 |
| VDR-U02-C027 | RTG-F01 | sale_stock/models/product_template.py:10-18 | is_storable | FACT | module sale_stock installed | — | For storable products the cost re-invoicing policy is forced to 'no' and the service type to 'manual'. | N-U02-018 |
| VDR-U02-C028 | RTG-F01 | sale/models/product_template.py:158-164 | _compute_invoice_policy | FACT | module sale installed | — | service_type defaults to 'manual' and invoice_policy defaults to 'order' for type consu (or when unset). | N-U02-018 |
| VDR-U02-C029 | RTG-F01 | purchase/models/product.py:22-29 | product.type == 'service' | FACT | module purchase installed | — | purchase_method (billing control) is 'purchase' (ordered quantities) for services, otherwise the field default (receive). | N-U02-019 |
| VDR-U02-C030 | RTG-F01 | stock/models/product.py:1098-1113 | used in at least one inventory movement | FACT | module stock installed | — | Changing the product type on a product already used in non-cancelled move lines only returns a warning (onchange), not a block. | N-U02-060 |
| VDR-U02-C031 | RTG-F01 | sale/models/product_template.py:148-156 | already used in sales orders | FACT | module sale installed | — | Changing type on a product with sales_count > 0 only returns a warning. | N-U02-060 |
| VDR-U02-C032 | RTG-F01 | stock/models/product.py:1151-1156 | templates_to_reset | INFERENCE | module stock installed | — | Lines 1151-1156: clean_inventory is set only when a template that is currently not storable receives a different value, and templates_to_reset is filled only when the written value is true, so the rebuild runs only on a switch on. | N-U02-061 |
| VDR-U02-C033 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:489-493 | must contain at least 1 combo choice | FACT | always | — | Constraint: a combo-type product must have at least one combo choice (combo_ids). | N-U02-020 |
| VDR-U02-C034 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:495-507 | can only contain sellable products | FACT | always | — | Constraint: a sellable combo can only contain sellable products. | N-U02-020 |
| VDR-U02-C035 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:459-472 | can't have attributes | FACT | always | — | Onchange type=combo raises if the template has attribute lines or is already part of a combo; sets purchase_ok False. | N-U02-020 |
| VDR-U02-C036 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:603-605 | combo_ids = False | FACT | always | — | write(): when type is written to a value other than combo, combo_ids is cleared. | N-U02-021 |
| VDR-U02-C037 | FUNCTION MAPPING REQUIRED | product/models/product_combo.py:64-73 | duplicate products | FACT | always | — | A combo choice must contain at least 1 product and no duplicate products. | N-U02-020 |
| VDR-U02-C038 | FUNCTION MAPPING REQUIRED | product/models/product_combo_item.py:30-33 | products of type | FACT | always | — | A combo choice cannot contain a product of type combo (no nesting). | N-U02-020 |
| VDR-U02-C039 | FUNCTION MAPPING REQUIRED | account/models/product.py:152-157 | self.taxes_id = False | FACT | module account installed | — | Onchange to combo clears sales and purchase taxes. | N-U02-020 |
| VDR-U02-C040 | RTG-F04 | sale_project/models/product_template.py:22-32 | task_global_project | FACT | module sale_project installed | — | service_tracking gains values task_global_project, task_in_project, project_only (default 'no' from product). | N-U02-022 |
| VDR-U02-C041 | RTG-F04 | sale_project/models/product_template.py:115-127 | should not have a project | FACT | module sale_project installed | — | Constraint ties project / project template choice to the service_tracking value (no project with 'no', no template with global task, no global project when a project is generated). | N-U02-022 |
| VDR-U02-C042 | RTG-F04 | sale_project/models/product_template.py:139-145 | service_tracking | FACT | module sale_project installed | — | write(): when type is written to a non-service value, service_tracking is reset to 'no' and project_id cleared. | N-U02-022 |
| VDR-U02-C043 | RTG-F04 | product/models/product_template.py:198-200 | _compute_service_tracking | FACT | always | — | service_tracking is forced to 'no' for any non-service product (base compute); sale also forces 'no' when not sellable. | N-U02-022 |
| VDR-U02-C044 | RTG-F04 | sale/models/product_template.py:88-91 | pt.sale_ok | FACT | module sale installed | — | service_tracking is also forced to 'no' when sale_ok is False. | N-U02-022 |
| VDR-U02-C045 | RTG-F04 | sale_purchase/models/product_template.py:11-21 | service_to_purchase | FACT | module sale_purchase installed | — | service_to_purchase is company-dependent, only allowed on services, and requires at least one vendor line. | N-U02-022 |
| VDR-U02-C046 | RTG-F04 | sale_purchase/models/product_template.py:34-37 | p.type != 'service' | FACT | module sale_purchase installed | — | Onchange of type or expense policy clears service_to_purchase when type is not service or re-invoicing is set. | N-U02-022 |
| VDR-U02-C047 | FUNCTION MAPPING REQUIRED | product/models/product_attribute.py:24-36 | no_variant | FACT | always | — | create_variant selection: always (Instantly), dynamic (Dynamically), no_variant (Never); default 'always', required. | N-U02-023 |
| VDR-U02-C048 | FUNCTION MAPPING REQUIRED | product/models/product_attribute.py:14-17 | Multi-checkbox display type | FACT | always | — | DB-level check: display_type 'multi' requires create_variant 'no_variant'. | N-U02-059 |
| VDR-U02-C049 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:567-583 | _create_variant_ids | FACT | context create_product_product not False | — | Template create() generates variants through _create_variant_ids (unless context create_product_product is False) and re-applies given related values to the first variant. | N-U02-023 |
| VDR-U02-C050 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:585-593 | attribute_line_ids | FACT | always | — | write(): changes of attribute_line_ids (or reactivation of a template without variants) trigger _create_variant_ids; archiving a template archives all variants (active_test False). | N-U02-029 |
| VDR-U02-C051 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:814-835 | has_dynamic_attributes | FACT | no dynamic attribute on template | — | Variants to create are the cartesian product of active values per attribute line (excluding no_variant lines), filtered by exclusions; creation limit from ir.config_parameter product.dynamic_variant_limit (default 1000) else UserError. | N-U02-025 |
| VDR-U02-C052 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:837-842 | elif existing_variants | FACT | dynamic attribute present | — | With a dynamic attribute no variants are pre-created; existing variants that are still possible are re-activated. | N-U02-028 |
| VDR-U02-C053 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:788-802 | single_value_lines | FACT | always | — | An attribute line with a single active value is added to every existing variant instead of multiplying variants. | N-U02-026 |
| VDR-U02-C054 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:844-861 | _unlink_or_archive | FACT | always | — | Variants that are no longer in the target set are unlinked or archived; if the template itself would vanish a UserError is raised; combo items referencing removed variants are unlinked. | N-U02-027 |
| VDR-U02-C055 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:1198-1243 | has_dynamic_attributes | FACT | dynamic attribute present | — | On-demand variant creation (_create_product_variant) only works when the template has dynamic attributes and the combination is possible; an archived variant is re-activated instead of duplicated. | N-U02-023 |
| VDR-U02-C056 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:1076-1111 | exclusions | FACT | always | — | _filter_combinations_impossible_by_config drops combinations with the wrong number/kind of values, inactive values, or values excluded by exclusion rules. | N-U02-024 |
| VDR-U02-C057 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:60-68 | must have at least one value | FACT | always | — | Active attribute line must have at least one value and values must belong to the line's attribute. | N-U02-057 |
| VDR-U02-C058 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:98-108 | archived_ptal | FACT | always | — | Creating a line equal to an archived one re-activates the archived line to reuse existing variants. | N-U02-026 |
| VDR-U02-C059 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:117-145 | cannot move the attribute | FACT | always | — | Lines cannot be moved to another product or transformed to another attribute. | N-U02-057 |
| VDR-U02-C060 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_line.py:160-192 | ptal_to_archive | FACT | always | — | Unlinking a line falls back to archiving when blocked by references; archiving a line clears its values. | N-U02-027 |
| VDR-U02-C061 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_value.py:118-150 | ptav_to_archive | FACT | always | — | Unlinking a template attribute value removes it from single-value variants, unlinks/archives affected variants, and archives the value if it cannot be deleted. | N-U02-027 |
| VDR-U02-C062 | FUNCTION MAPPING REQUIRED | product/models/product_attribute.py:115-123 | cannot change the Variants Creation Mode | FACT | always | — | create_variant cannot change while the attribute has related products. | N-U02-056 |
| VDR-U02-C063 | FUNCTION MAPPING REQUIRED | product/models/product_attribute.py:133-152 | cannot delete the attribute | FACT | always | — | Attributes used on products cannot be deleted or archived. | N-U02-056 |
| VDR-U02-C064 | FUNCTION MAPPING REQUIRED | product/models/product_attribute_value.py:97-106 | cannot change the attribute of the value | FACT | always | — | An attribute value cannot be moved to another attribute while used on products; deleting a used value is blocked. | N-U02-057 |
| VDR-U02-C065 | FUNCTION MAPPING REQUIRED | product/models/product_attribute_value.py:132-145 | pavs_to_archive | FACT | always | — | Deleting a value found only on archived variants archives the value instead. | N-U02-027 |
| VDR-U02-C066 | FUNCTION MAPPING REQUIRED | product/models/product_attribute_custom_value.py:6-17 | custom_value | FACT | always | — | Free-text custom attribute values are stored in a separate model keyed by template attribute value (restrict on delete); the line link is added by order modules. | N-U02-034 |
| VDR-U02-C067 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:696-710 | action_unarchive | FACT | always | — | Archiving the last active variant archives its template; unarchiving a variant re-activates an archived template. | N-U02-029 |
| VDR-U02-C068 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:712-745 | has_other_products | FACT | always | — | Deleting variants also deletes the template when it was the last variant and the template has no dynamic attributes; variant image moves to the template first. | N-U02-030 |
| VDR-U02-C069 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:750-784 | dichotomy | FACT | always | — | _unlink_or_archive tries to delete in batch, uses dichotomy on error, and archives what cannot be deleted. | N-U02-027 |
| VDR-U02-C070 | FUNCTION MAPPING REQUIRED | stock/models/product.py:714-719 | orderpoint_ids | FACT | module stock installed | — | Archiving/unarchiving a variant propagates the active flag to its reordering rules. | N-U02-040 |
| VDR-U02-C071 | FUNCTION MAPPING REQUIRED | stock/models/product.py:761-765 | stock.lot | FACT | module stock installed | — | Variants that have lots/serials are excluded from deletion and archived instead. | N-U02-027 |
| VDR-U02-C072 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:129 | active = fields.Boolean | FACT | always | — | Template and variant have an active flag (hide without removing); no other state field exists in the product module. | N-U02-040 |
| VDR-U02-C073 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:282-290 | skip_preprocess_gs1 | FACT | always | — | barcode constraint groups products by company and checks duplicates among products and among packaging barcodes within each company group. | N-U02-031 |
| VDR-U02-C074 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:252-275 | (False, company_id) | INFERENCE | always | — | Lines 252-275: duplicate search domain is barcode in list AND company in (False, company); duplicates counted via read-group having count > 1 and reported with a ValidationError (product list limited to readable products). | N-U02-031 |
| VDR-U02-C075 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:277-280 | packaging | FACT | always | — | A product barcode equal to an existing packaging barcode is refused ('A packaging already uses the barcode'). | N-U02-031 |
| VDR-U02-C076 | FUNCTION MAPPING REQUIRED | product/models/product_uom.py:15-26 | unique(barcode) | FACT | always | — | Packaging (product.uom) barcode is required, copy=False and DB-unique; a clash with a product barcode is refused. | N-U02-032 |
| VDR-U02-C077 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:251-254 | _check_barcode_uniqueness | FACT | always | — | Changing a template's company re-runs the barcode uniqueness check on its variants. | N-U02-031 |
| VDR-U02-C078 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:422-435 | already exists | FACT | always | — | Duplicate internal reference only raises an onchange warning ('already exists'); there is no constraint. | N-U02-033 |
| VDR-U02-C079 | FUNCTION MAPPING REQUIRED | stock/models/product.py:1129-1147 | company cannot be changed | FACT | module stock installed | — | Template company cannot change while stock moves or non-zero quants exist in another company. | N-U02-055 |
| VDR-U02-C080 | FUNCTION MAPPING REQUIRED | sale/models/product_template.py:108-132 | already been used in quotations | FACT | module sale installed | — | Template cannot be restricted to a company if it was used in sales order lines of another company. | N-U02-055 |
| VDR-U02-C081 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:292-295 | combo_items._check_company | FACT | always | — | Changing a variant's company re-checks company consistency of combo items referencing it. | N-U02-055 |
| VDR-U02-C082 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:22 | _check_company_domain | OBSERVATION | always | — | product.product declares a company domain but no _check_company_auto, and the product module declares no ir.rule for product.product (rules exist for product.template only; DB confirms 0 rules on product.product). | N-U02-065 |
| VDR-U02-C083 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:520-565 | import_attribute_values | FACT | import with column present | — | Import with the import_attribute_values column creates templates then variants from the same file; attribute/value records are created on the fly (dynamic, radio) when missing. | N-U02-066 |
| VDR-U02-C084 | FUNCTION MAPPING REQUIRED | product/models/res_config_settings.py:10 | group_product_variant | FACT | always | — | The Variants setting is an implied-group switch (product.group_product_variant). | N-U02-045 |
| VDR-U02-C085 | FUNCTION MAPPING REQUIRED | product_matrix/data/res_groups.xml:4-6 | group_product_variant | FACT | module product_matrix installed | — | product_matrix makes base.group_user imply the variants group (observed enabled for all internal users in DB). | N-U02-045 |
| VDR-U02-C086 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:1503-1518 | has_configurable_attributes | FACT | always | — | get_single_product_variant returns the single variant directly only when the template has one variant and no configurable attributes. | N-U02-062 |
| VDR-U02-C087 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:216-236 | has_dynamic_attributes | FACT | always | — | has_configurable_attributes is true when dynamic attributes exist, a line has at least two values or is multi-checkbox, or a custom value exists. | N-U02-062 |
| VDR-U02-C088 | FUNCTION MAPPING REQUIRED | sale/models/product_template.py:225-231 | _get_saleable_tracking_types | FACT | module sale installed | — | Sales module returns ['no'] as the saleable service tracking types; extended by project module. | N-U02-047 |
| VDR-U02-C089 | FUNCTION MAPPING REQUIRED | stock/models/product.py:839-841 | is_storable | OBSERVATION | restored DB (config only) | — | DB: 16 product definitions, all type service (16 of 16, none storable, tracking none); no goods products and no combos exist in the studied database. | N-U02-046 |
| VDR-U02-C090 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:66-70 | Combo Choices | FACT | always | — | Template combo_ids (Combo Choices) is a many2many to product.combo with company check. | N-U02-005 |
| VDR-U02-C091 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:132-146 | attribute_line_ids | INFERENCE | always | — | Lines 133-146: attribute lines hang on the template while variants are the one2many product_variant_ids, so commercial data is shared by all variants (purpose inferred). | N-U02-006 |
| VDR-U02-C092 | RTG-F01 | stock/models/product.py:911-913 | compute_is_storable | INFERENCE | module stock installed | — | Tracking is a separate stored boolean computed from type, so untracked goods are a first-class state next to tracked goods, services and combos (purpose inferred; DB holds services only). | N-U02-007 |
| VDR-U02-C093 | RTG-F01 | sale_stock/models/sale_order_line.py:190-193 | stock_move | INFERENCE | modules sale_stock, purchase_stock, stock_account installed | — | Lines 190-193 here, purchase_stock purchase_order_line.py:38-41, stock_account account_move_line.py:30-33 and stock stock_rule.py:447-450 all branch on product type or is_storable, so the classification is read by sales, purchase, stock and accounting alike. | N-U02-050 |
| VDR-U02-C094 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | import of products with attribute values | RT | UNKNOWN - EVIDENCE INSUFFICIENT: end-to-end effect of an import that changes attribute values of existing variants; resolve by runtime import test. | N-U02-066 |
| VDR-U02-C095 | FUNCTION MAPPING REQUIRED | product/models/product_category.py:8-26 | _parent_store | FACT | always | — | product.category is a parent_store tree (parent_id, parent_path, child_id, complete_name stored). | N-U02-070 |
| VDR-U02-C096 | FUNCTION MAPPING REQUIRED | product/models/product_category.py:46-49 | recursive categories | FACT | always | — | Constraint on parent_id prevents cycles ('You cannot create recursive categories'). | N-U02-090 |
| VDR-U02-C097 | FUNCTION MAPPING REQUIRED | product/models/product_category.py:27 | PropertiesDefinition | FACT | always | — | Category holds product_properties_definition (custom property schema). | N-U02-085 |
| VDR-U02-C098 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:186 | categ_id.product_properties_definition | FACT | always | — | product_properties on the template is defined by the category's definition. | N-U02-085 |
| VDR-U02-C099 | FUNCTION MAPPING REQUIRED | account/models/product.py:11 | ACCOUNT_DOMAIN | FACT | module account installed | — | Accounts selectable for income/expense exclude receivable, payable, cash, credit card and off-balance types. | N-U02-091 |
| VDR-U02-C100 | FUNCTION MAPPING REQUIRED | account/models/product.py:17-23 | property_account_income_categ_id | FACT | module account installed | — | Category field property_account_income_categ_id: Many2one account.account, company_dependent, restrict on delete, tracked. | N-U02-075 |
| VDR-U02-C101 | FUNCTION MAPPING REQUIRED | account/models/product.py:24-30 | property_account_expense_categ_id | FACT | module account installed | — | Category field property_account_expense_categ_id: Many2one account.account, company_dependent, restrict on delete, tracked. | N-U02-075 |
| VDR-U02-C102 | FUNCTION MAPPING REQUIRED | account/models/product.py:53-60 | property_account_income_id | FACT | module account installed | — | Template fields property_account_income_id and property_account_expense_id are company_dependent Many2one account.account (restrict); help says empty = use category. | N-U02-075 |
| VDR-U02-C103 | FUNCTION MAPPING REQUIRED | account/models/product.py:68-79 | _get_category_account | FACT | module account installed | — | _get_product_accounts: income/expense = template account, else category account via _get_category_account, else company income_account_id/expense_account_id. | N-U02-075 |
| VDR-U02-C104 | FUNCTION MAPPING REQUIRED | account/models/product.py:81-92 | categ.parent_id | FACT | module account installed | — | _get_category_account walks up the category parents until a value is found. | N-U02-075 |
| VDR-U02-C105 | FUNCTION MAPPING REQUIRED | account/models/product.py:94-98 | map_account | FACT | module account installed | — | get_product_accounts maps each account through the fiscal position (map_account). | N-U02-076 |
| VDR-U02-C106 | FUNCTION MAPPING REQUIRED | account/models/company.py:282-295 | income_account_id | FACT | module account installed | — | Company-level default income_account_id and expense_account_id exist on res.company. | N-U02-075 |
| VDR-U02-C107 | FUNCTION MAPPING REQUIRED | account/models/company.py:1145-1148 | _set_category_defaults | FACT | module account installed | — | _set_category_defaults writes ir.default values for product.category property_account_expense_categ_id/property_account_income_categ_id per company from the company defaults. | N-U02-072 |
| VDR-U02-C108 | FUNCTION MAPPING REQUIRED | account/models/company.py:500 | _set_category_defaults | FACT | module account installed | — | Called after company creation. | N-U02-072 |
| VDR-U02-C109 | FUNCTION MAPPING REQUIRED | account/models/company.py:763 | _set_category_defaults | FACT | module account installed | — | Called again on company write (during accounting default changes). | N-U02-072 |
| VDR-U02-C110 | FUNCTION MAPPING REQUIRED | stock_account/models/res_company.py:371-377 | property_stock_valuation_account_id | FACT | module stock_account installed | — | Extension of _set_category_defaults sets ir.default for category property_valuation, property_cost_method, property_stock_journal and property_stock_valuation_account_id per company. | N-U02-072 |
| VDR-U02-C111 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:731-740 | property_valuation | FACT | module stock_account installed | — | Category property_valuation (periodic/real_time): company_dependent, copy=True, tracked. | N-U02-079 |
| VDR-U02-C112 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:741-755 | property_cost_method | FACT | module stock_account installed | — | Category property_cost_method (standard/fifo/average): company_dependent, copy=True, default company cost_method, tracked. | N-U02-079 |
| VDR-U02-C113 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:756-758 | property_stock_journal | FACT | module stock_account installed | — | Category property_stock_journal: Many2one account.journal, company_dependent. | N-U02-077 |
| VDR-U02-C114 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:759-762 | property_stock_valuation_account_id | FACT | module stock_account installed | — | Category property_stock_valuation_account_id: Many2one account.account, company_dependent, check_company. | N-U02-077 |
| VDR-U02-C115 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:763-766 | property_price_difference_account_id | FACT | module stock_account installed | — | Category property_price_difference_account_id: Many2one account.account, company_dependent, check_company. | N-U02-082 |
| VDR-U02-C116 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:60-79 | company.cost_method | FACT | module stock_account installed | — | Template cost_method/valuation are computed per company context: category value for the chosen company, else company cost_method / inventory_valuation. | N-U02-079 |
| VDR-U02-C117 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:130-142 | get_company_dependent_fallback | FACT | module stock_account installed | — | _get_product_accounts adds stock_valuation = category value, else the field's company-dependent fallback (ir.default), else company account_stock_valuation_id; stock_variation from that account. | N-U02-077 |
| VDR-U02-C118 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:144-156 | stock_journal | FACT | module stock_account installed | — | get_product_accounts adds stock_journal = category value, else company-dependent fallback, else company account_stock_journal_id. | N-U02-077 |
| VDR-U02-C119 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:158-162 | cost_method == 'standard' | FACT | module stock_account installed | — | _get_price_diff_account returns the category price difference account only when cost_method is standard. | N-U02-082 |
| VDR-U02-C120 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:36-40 | TODO remove in master | FACT | module stock_account installed | — | A template-level property_price_difference_account_id (company_dependent) is kept but marked TODO remove; the category field is the effective one. | N-U02-082 |
| VDR-U02-C121 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:81-125 | _update_standard_price | FACT | module stock_account installed | — | Template write: changing categ_id to a category with a different cost method or changing lot_valuated triggers _update_standard_price on the variants and lots; enabling lot valuation is refused when on-hand quants lack lots. | N-U02-080 |
| VDR-U02-C122 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:775-787 | products_to_update | FACT | module stock_account installed | — | Category write: changing property_cost_method triggers _update_standard_price for all products of the category (and lots when lot valuated). | N-U02-080 |
| VDR-U02-C123 | FUNCTION MAPPING REQUIRED | mrp_account/models/product.py:10-26 | production_account | FACT | module mrp_account installed | — | _get_product_accounts adds 'production': category property_stock_account_production_cost_id when the product has a category (even if empty); without category only the fallback under real_time valuation. | N-U02-078 |
| VDR-U02-C124 | FUNCTION MAPPING REQUIRED | mrp_account/models/product.py:118-122 | company_dependent=True | FACT | module mrp_account installed | — | Category property_stock_account_production_cost_id: Many2one account.account, company_dependent, check_company. | N-U02-078 |
| VDR-U02-C125 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:62-68 | company_dependent=True | FACT | always | — | standard_price (Cost) is a company_dependent float on the variant, restricted to base.group_user. | N-U02-081 |
| VDR-U02-C126 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:310-321 | depends_context('company') | FACT | always | — | Template standard_price is computed from the variant per company context and written back to the single variant. | N-U02-081 |
| VDR-U02-C127 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:417-420 | can't be negative | FACT | always | — | Onchange on standard_price raises 'The cost of a product can't be negative' (onchange only, not a DB constraint). | N-U02-081 |
| VDR-U02-C128 | FUNCTION MAPPING REQUIRED | stock/models/product.py:842-852 | property_stock_production | FACT | module stock installed | — | Template responsible_id, property_stock_production and property_stock_inventory are company_dependent (check_company, domain by usage production/inventory). | N-U02-083 |
| VDR-U02-C129 | FUNCTION MAPPING REQUIRED | stock/models/product.py:1306-1331 | packaging_reserve_method | FACT | module stock installed | — | Category route_ids (selectable), removal_strategy_id, putaway rules and packaging_reserve_method (full/partial) are ordinary (not company-dependent) fields. | N-U02-084 |
| VDR-U02-C130 | FUNCTION MAPPING REQUIRED | stock/models/product.py:1333-1351 | parent_route_ids | FACT | module stock installed | — | Total routes of a category = own routes plus all ancestors' routes. | N-U02-084 |
| VDR-U02-C131 | FUNCTION MAPPING REQUIRED | sale_project/models/product_template.py:33-43 | company_dependent=True | FACT | module sale_project installed | — | Template project_id, project_template_id and task_template_id are company_dependent. | N-U02-083 |
| VDR-U02-C132 | FUNCTION MAPPING REQUIRED | sale_purchase/models/product_template.py:11-13 | company_dependent=True | FACT | module sale_purchase installed | — | Template service_to_purchase is company_dependent boolean. | N-U02-083 |
| VDR-U02-C133 | FUNCTION MAPPING REQUIRED | product/models/res_partner.py:14-29 | specific_property_product_pricelist | FACT | always | — | Partner pricelist: property_product_pricelist is a computed, non company-dependent field; specific_property_product_pricelist is the company_dependent stored value. | N-U02-086 |
| VDR-U02-C134 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:77-86 | company_dependent=True | FACT | always | — | Plan default_applicability (optional/mandatory/unavailable) is company_dependent. | N-U02-087 |
| VDR-U02-C135 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:94-102 | 'optional' | FACT | always | — | _auto_init sets the ir.default of default_applicability to 'optional' in a precommit. | N-U02-087 |
| VDR-U02-C136 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:741-748 | company_dependent=True | OBSERVATION | restored DB (config only) | — | DB: company-dependent columns are jsonb keyed by company id (observed for product_product.standard_price and account_analytic_plan.default_applicability); the three seeded categories Goods/Expenses/Services store property_cost_method {"1": "standard"}; ir_default holds 1 row each for category income/expense account, stock journal and valuation account, 2 each for valuation and cost method, 1 each for template production and inventory locations, 1 for plan default applicability. | N-U02-071 |
| VDR-U02-C137 | FUNCTION MAPPING REQUIRED | stock_account/models/res_company.py:22-40 | default='periodic' | OBSERVATION | restored DB (config only) | — | Company defaults inventory_valuation default 'periodic' and cost_method default 'standard'; DB single company shows periodic / standard. | N-U02-079 |
| VDR-U02-C138 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | core platform | — | UNKNOWN - EVIDENCE INSUFFICIENT for physical fallback mechanics: read from core ORM (odoo/orm/fields.py, outside the module scope) which stores a JSON map by company id with fallback to ir.default; not claimed as module evidence. | N-U02-095 |
| VDR-U02-C139 | FUNCTION MAPPING REQUIRED | account/models/product.py:219-221 | _get_product_accounts | FACT | module account installed | — | The variant delegates _get_product_accounts to its template, so category resolution is identical for variants. | N-U02-093 |
| VDR-U02-C140 | FUNCTION MAPPING REQUIRED | stock_account/models/product.py:42-52 | domain_company | FACT | module stock_account installed | — | valuation can be searched only with '=' and the two values; search combines category property_valuation with company inventory_valuation, shared products included. | N-U02-093 |
| VDR-U02-C141 | FUNCTION MAPPING REQUIRED | account/models/product.py:131-150 | already being used in posted Journal Entries | FACT | module account installed | — | Posted-entry history locks a product's unit change; account resolution is evaluated at posting time with no restatement. | N-U02-094 |
| VDR-U02-C142 | FUNCTION MAPPING REQUIRED | account/models/product.py:17-30 | company_dependent=True | INFERENCE | module account installed | — | Category-level company-dependent account fields with help texts indicate that product families share posting accounts per company (purpose inferred). | N-U02-073 |
| VDR-U02-C143 | FUNCTION MAPPING REQUIRED | mrp_account/models/product.py:118-122 | company_dependent=True | INFERENCE | module mrp_account installed | — | Property fields are added by separate modules (account, stock_account, mrp_account), so each exists only when its module is installed. | N-U02-092 |
| VDR-U02-C144 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:28-64 | country_group_ids | FACT | always | — | Pricelist fields: name, active, sequence, currency_id (required, default company currency), company_id (default current company), country_group_ids, item_ids. | N-U02-100 |
| VDR-U02-C145 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:51-61 | 3_global | FACT | always | — | Rule applied_on selection: 3_global, 2_product_category, 1_product, 0_product_variant (default 3_global, required). | N-U02-102 |
| VDR-U02-C146 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:91-104 | Other Pricelist | FACT | always | — | Rule base selection: list_price, standard_price, pricelist (default list_price). | N-U02-101 |
| VDR-U02-C147 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:106-114 | Fixed Price | FACT | always | — | Rule compute_price selection: percentage (Discount), formula, fixed (default fixed). | N-U02-101 |
| VDR-U02-C148 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:121-152 | price_max_margin | FACT | always | — | Formula parameters: price_discount, price_round, price_surcharge, price_markup (stored inverse of discount), price_min_margin, price_max_margin. | N-U02-101 |
| VDR-U02-C149 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:43-49 | min_quantity | FACT | always | — | min_quantity is in the product's default unit of measure (help text). | N-U02-108 |
| VDR-U02-C150 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:11 | min_quantity desc | FACT | always | — | Rule order: applied_on, min_quantity desc, categ_id desc, id desc (variant first, then product, category, global). | N-U02-105 |
| VDR-U02-C151 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:239-264 | parent_of | FACT | always | — | Applicable rules search: this pricelist, category null or parent_of the products' categories, product/template null or matching, date_start null or <= date, date_end null or >= date. | N-U02-106 |
| VDR-U02-C152 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:199-201 | fields.Datetime.now() | FACT | always | — | Pricing date defaults to now when none is given. | N-U02-106 |
| VDR-U02-C153 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:213-225 | qty_in_product_uom | FACT | always | — | Quantity is converted to the product unit before rule matching; the first applicable rule in order wins (break). | N-U02-105 |
| VDR-U02-C154 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:526-568 | _is_applicable_for | FACT | always | — | _is_applicable_for: min quantity test; category rule matches product category or any descendant via parent_path; template rules compare template id; variant rule on a template applies only when the template has exactly one variant that is the rule's variant. | N-U02-135 |
| VDR-U02-C155 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:570-626 | _compute_price | FACT | always | — | _compute_price: fixed -> convert(fixed_price); percentage -> base - base*percent/100; formula -> discounted base, round, surcharge, margins; otherwise base price. | N-U02-109 |
| VDR-U02-C156 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:606-621 | price_limit | FACT | always | — | Formula: discount = price_discount (or -price_markup when base is cost); price = base - base*discount/100; round to price_round; add convert(price_surcharge); max(price, base+min_margin); min(price, base+max_margin). | N-U02-109 |
| VDR-U02-C157 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:593-599 | convert = lambda | FACT | always | — | Rule amounts are in the product unit; for another unit they are converted with product_uom._compute_price. | N-U02-108 |
| VDR-U02-C158 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:628-659 | _compute_base_price | FACT | always | — | Base price: other pricelist's price (same quantity/uom/date) or product cost / list price, converted to the target currency at the date with round=False; empty rule uses list_price. | N-U02-111 |
| VDR-U02-C159 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:656-657 | round=False | FACT | always | — | Currency conversion of the base uses _convert(..., self.env.company, date, round=False). | N-U02-112 |
| VDR-U02-C160 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:737-768 | _get_attributes_extra_price | FACT | always | — | Template _price_compute: list_price base adds attribute extras; cost base read as sudo; unit and currency converted. | N-U02-113 |
| VDR-U02-C161 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1099-1102 | no_variant_attributes_price_extra | FACT | always | — | Variant extra price = variant ptav extras + extras from no_variant attributes in context. | N-U02-113 |
| VDR-U02-C162 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1104-1113 | base.group_user | FACT | always | — | _price_compute for standard_price runs as superuser because the field is restricted to internal users. | N-U02-114 |
| VDR-U02-C163 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:661-684 | _compute_price_before_discount | FACT | always | — | Price before discount follows chained pricelists while the referenced rule is a percentage rule, then computes that rule's base price. | N-U02-115 |
| VDR-U02-C164 | FUNCTION MAPPING REQUIRED | sale/models/product_pricelist_item.py:7-16 | group_discount_per_so_line | FACT | module sale installed | — | _show_discount is true only when sale.group_discount_per_so_line is enabled and the rule is a percentage rule. | N-U02-127 |
| VDR-U02-C165 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:659-677 | max(base_price, pricelist_price) | FACT | module sale installed | — | Display price: pricelist price; if the rule shows discount, max(base price before discount, pricelist price) so negative discounts (surcharges) are included. | N-U02-115 |
| VDR-U02-C166 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:316-319 | must have a base_pricelist_id | FACT | always | — | Constraint: base 'pricelist' requires base_pricelist_id. | N-U02-130 |
| VDR-U02-C167 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:321-352 | Recursive pricelist rules detected | FACT | always | — | Constraint detects cycles among pricelists through rules based on other pricelists (depth-first search). | N-U02-130 |
| VDR-U02-C168 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:354-364 | should be after start date | FACT | always | — | Constraint: date_end must be after date_start. | N-U02-131 |
| VDR-U02-C169 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:366-369 | minimum margin should be lower | FACT | always | — | Constraint: price_min_margin must not exceed price_max_margin. | N-U02-131 |
| VDR-U02-C170 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:371-379 | Please specify the category | FACT | always | — | Constraint: category/product/variant must be specified according to applied_on. | N-U02-131 |
| VDR-U02-C171 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:468-471 | strictly positive | FACT | always | — | Negative price_round is rejected in an onchange only (no constraint). | N-U02-131 |
| VDR-U02-C172 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:479-522 | Ensure item consistency | FACT | always | — | create/write normalise target fields according to applied_on (global clears product/category, category clears product, etc.). | N-U02-133 |
| VDR-U02-C173 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:170-182 | item.pricelist_id.company_id | FACT | always | — | Rule company = pricelist company, else its template's company; rule currency = pricelist currency, else company/env currency. | N-U02-132 |
| VDR-U02-C174 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:72-80 | item_ids._check_company | FACT | always | — | Changing a pricelist's company (single record) re-checks its rules. | N-U02-132 |
| VDR-U02-C175 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:393-405 | _unlink_except_used_as_rule_base | FACT | always | — | Deleting a pricelist used as base of rules in other pricelists is refused (UserError). | N-U02-122 |
| VDR-U02-C176 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:348-350 | group_product_pricelist | FACT | always | — | When the pricelist feature is disabled, partner pricelist resolution returns no pricelist. | N-U02-116 |
| VDR-U02-C177 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:356-375 | specific_property_product_pricelist | FACT | feature enabled | — | Partner pricelist: specific (company-dependent) value if active; else country-group based; remaining partners get the country result. | N-U02-116 |
| VDR-U02-C178 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:296-330 | pl_fallback | FACT | feature enabled | — | Fallback order: active pricelist of the company with no country group; config parameter res.partner.property_product_pricelist_<company>; generic parameter; first active pricelist of the company. | N-U02-116 |
| VDR-U02-C179 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:377-384 | company_id', 'in' | FACT | always | — | Candidate pricelists must be active and belong to the current company or no company. | N-U02-116 |
| VDR-U02-C180 | FUNCTION MAPPING REQUIRED | product/models/res_partner.py:31-45 | _inverse_product_pricelist | FACT | always | — | Effective partner pricelist is computed per company/country; writing it stores a specific value only when it differs from the country default. | N-U02-116 |
| VDR-U02-C181 | FUNCTION MAPPING REQUIRED | product/models/res_partner.py:47-51 | _synced_commercial_fields | FACT | always | — | The specific pricelist is a commercial field synced from the commercial partner. | N-U02-116 |
| VDR-U02-C182 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:443-452 | property_product_pricelist | FACT | module sale installed | — | Order pricelist is computed for draft orders from the partner's pricelist in the order's company. | N-U02-117 |
| VDR-U02-C183 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:454-457 | pricelist_id.currency_id | FACT | module sale installed | — | Order currency = pricelist currency, else company currency. | N-U02-117 |
| VDR-U02-C184 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1043-1044 | confirmed order | FACT | module sale installed | — | Writing pricelist_id on a confirmed order raises UserError. | N-U02-117 |
| VDR-U02-C185 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:928-930 | show_update_pricelist | FACT | module sale installed | — | Changing the pricelist on an order with lines only sets a flag; existing lines keep their price until the user updates prices. | N-U02-117 |
| VDR-U02-C186 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:577-587 | _get_product_rule | FACT | module sale installed | — | pricelist_item_id on the line = pricelist._get_product_rule(product, quantity, uom, date, currency). | N-U02-118 |
| VDR-U02-C187 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:589-620 | has_manual_price | FACT | module sale installed | — | Unit price recompute skips lines with manual price, qty_invoiced > 0 or at-cost expenses; otherwise price_unit is reset from the pricelist display price. | N-U02-118 |
| VDR-U02-C188 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:693-699 | _get_pricelist_kwargs | FACT | module sale installed | — | Pricing call arguments: quantity (>=1 default), line uom, order date, order currency. | N-U02-118 |
| VDR-U02-C189 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:1534-1550 | _get_contextual_pricelist | FACT | always | — | Contextual price: pricelist from context key 'pricelist', quantity, uom, date -> pricelist._get_product_price. | N-U02-128 |
| VDR-U02-C190 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:90-110 | _compute_price_rule | FACT | always | — | Public API: _get_products_price, _get_product_price, _get_product_price_rule, _get_product_rule all delegate to _compute_price_rule (price and rule id). | N-U02-128 |
| VDR-U02-C191 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:273-286 | _compute_price_rule_multi | FACT | always | — | Multi-pricelist evaluation loops over pricelists (all when none given). | N-U02-128 |
| VDR-U02-C192 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1170-1195 | _get_contextual_discount | FACT | always | — | Contextual discount = (list price in pricelist currency - contextual price) / list price; zero without pricelist. | N-U02-115 |
| VDR-U02-C193 | FUNCTION MAPPING REQUIRED | product/models/res_company.py:15-34 | _activate_or_create_pricelists | FACT | pricelist feature enabled | — | Creates/reactivates a default pricelist per company (reuses an archived rule-less pricelist with company currency). | N-U02-120 |
| VDR-U02-C194 | FUNCTION MAPPING REQUIRED | product/models/res_company.py:36-51 | 'name': _("Default") | FACT | always | — | Default pricelist values: name Default, company currency, company id, sequence 10. | N-U02-120 |
| VDR-U02-C195 | FUNCTION MAPPING REQUIRED | product/models/res_company.py:9-13 | _activate_or_create_pricelists | FACT | always | — | Company creation calls the default-pricelist routine. | N-U02-120 |
| VDR-U02-C196 | FUNCTION MAPPING REQUIRED | product/models/res_config_settings.py:36-43 | action_archive() | FACT | always | — | Saving settings: enabling the feature creates/activates default pricelists; disabling archives all pricelists. | N-U02-121 |
| VDR-U02-C197 | FUNCTION MAPPING REQUIRED | product/models/res_currency.py:10-23 | action_archive | FACT | always | — | Activating multi-currency applies the pricelist group to internal users and creates default pricelists; archiving a currency archives pricelists in that currency. | N-U02-121 |
| VDR-U02-C198 | FUNCTION MAPPING REQUIRED | product/models/res_country_group.py:7-15 | pricelist_ids | FACT | always | — | Country groups link to pricelists through a many2many table shared with the pricelist field. | N-U02-116 |
| VDR-U02-C199 | FUNCTION MAPPING REQUIRED | website_sale/models/product_pricelist.py:26-38 | selectable | FACT | module website_sale installed (NOT installed in DB) | — | DISCOVERED SUPPORTING MODULE (not installed): website_sale adds website_id, code and selectable to pricelists for per-website scoping. | N-U02-123 |
| VDR-U02-C200 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:37 | default=_default_currency_id | OBSERVATION | restored DB (config only) | — | DB: 1 pricelist ('Default', active, company 1, currency id 134), 0 pricelist items, 0 country-group links; feature group id 19 implied by base.group_user; 2 active currencies (multi-currency activation path). | N-U02-126 |
| VDR-U02-C201 | FUNCTION MAPPING REQUIRED | sale/models/product_pricelist_item.py:7-9 | _is_discount_feature_enabled | FACT | module sale installed | — | Discount feature flag is read from sale.group_discount_per_so_line via res.groups feature check. | N-U02-127 |
| VDR-U02-C202 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1076-1085 | _get_product_price_context | FACT | always | — | Price context carries no_variant attribute extras into the pricelist call. | N-U02-113 |
| VDR-U02-C203 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:170-173 | _compute_company_id | FACT | always | — | company_id on rule is stored computed (pricelist company, else product template company); rule record rule uses it. | N-U02-132 |
| VDR-U02-C204 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:19-26 | _domain_item_ids | FACT | always | — | item_ids domain hides rules whose template or variant is archived. | N-U02-125 |
| VDR-U02-C205 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:157-162 | pricelist_rule_ids | FACT | always | — | Template exposes pricelist_rule_ids (rules of active pricelists); variants expose the subset not targeting other variants. | N-U02-102 |
| VDR-U02-C206 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:51-61 | applied_on | INFERENCE | always | — | Rule dimensions (target level, minimum quantity, dates, currency of the list) show that one product price can vary by customer context without touching the product price (purpose inferred). | N-U02-103 |
| VDR-U02-C207 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:623-624 | empty self | FACT | always | — | With no rule (empty rule record) the price is the base price, i.e. the product list price converted to the requested unit and currency. | N-U02-107 |
| VDR-U02-C208 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:603-605 | percent_price | FACT | always | — | Percentage rule: price = base - base * percent_price / 100 where base comes from list price or another pricelist. | N-U02-110 |
| VDR-U02-C209 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:669-688 | seller.price | INFERENCE | module purchase installed | — | Purchase order line price comes from the selected vendor line (seller.price) with no pricelist call in this path. | N-U02-119 |
| VDR-U02-C210 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:43-49 | default unit of measure of the product | INFERENCE | always | — | Minimum quantity is expressed in the product's default unit, so a later change of the product unit changes the meaning of existing thresholds. | N-U02-134 |
| VDR-U02-C211 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | document-level rounding | RT | UNKNOWN - EVIDENCE INSUFFICIENT: final rounding of price_unit to currency precision at order-line level is outside this unit; resolve in the sales unit. | N-U02-137 |
| VDR-U02-C212 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:17-22 | _parent_name | FACT | always | — | uom.uom is a parent_store tree on relative_uom_id. | N-U02-140 |
| VDR-U02-C213 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:34-44 | relative_factor | FACT | always | — | Fields: name, sequence, relative_factor (default 1, numeric unlimited precision), rounding (computed), active, relative_uom_id, related_uom_ids, factor (stored, recursive), parent_path. | N-U02-140 |
| VDR-U02-C214 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:69-75 | relative_uom_id.factor | FACT | always | — | factor = relative_factor * relative_uom_id.factor, or relative_factor for roots. | N-U02-140 |
| VDR-U02-C215 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:46-49 | cannot be 0 | FACT | always | — | DB CHECK relative_factor != 0. | N-U02-164 |
| VDR-U02-C216 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:97-101 | Reference unit of measure is missing | FACT | always | — | Constraint: a unit without reference must have relative_factor 1.0. | N-U02-164 |
| VDR-U02-C217 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:62-67 | Product Unit | FACT | always | — | rounding is computed from the decimal precision named 'Product Unit' for all units. | N-U02-148 |
| VDR-U02-C218 | FUNCTION MAPPING REQUIRED | uom/data/uom_data.xml:5-8 | Product Unit | FACT | always | — | The Product Unit precision is created with 2 digits (forcecreate). | N-U02-148 |
| VDR-U02-C219 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:116-137 | precision_get('Product Unit') | FACT | always | — | round, compare, is_zero all use the Product Unit precision. | N-U02-148 |
| VDR-U02-C220 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:147-176 | rounding_method: RoundingMethod = 'UP' | FACT | always | — | _compute_quantity: same unit -> qty; else qty*factor/to_unit.factor; rounded to to_unit.rounding with default method UP when round=True. | N-U02-146 |
| VDR-U02-C221 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:147-176 | raise_if_failure | INFERENCE | always | — | Lines 147-176: parameter raise_if_failure is accepted and documented but never referenced in the body; no common-root check is made, so cross-root conversions are computed silently. | N-U02-149 |
| VDR-U02-C222 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:196-203 | _compute_price | FACT | always | — | _compute_price converts a price as price * to_unit.factor / self.factor (inverse of quantity ratio). | N-U02-147 |
| VDR-U02-C223 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:178-194 | _check_qty | FACT | always | — | _check_qty rounds a quantity to a multiple of the packaging quantity (float_round on ratio, chosen method); same unit returns the quantity unchanged. | N-U02-150 |
| VDR-U02-C224 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:853 | _check_qty | FACT | module stock installed | — | Reservation of packaged quantities calls packaging_uom._check_qty(..., product uom, 'DOWN'). | N-U02-150 |
| VDR-U02-C225 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:218-230 | _has_common_reference | FACT | always | — | _has_common_reference compares parent_path roots of two units. | N-U02-149 |
| VDR-U02-C226 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order_line.py:49 | _has_common_reference | FACT | module sale_timesheet installed | — | Timesheet logic uses the common-root test against the hour unit. | N-U02-149 |
| VDR-U02-C227 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:976 | _has_common_reference | FACT | module account_edi_ubl_cii installed | — | Electronic invoice import tests the common root against the product unit. | N-U02-149 |
| VDR-U02-C228 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:24-32 | product_uom_pack_6 | FACT | always | — | Unprotected units are hour, dozen and pack of six. | N-U02-155 |
| VDR-U02-C229 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:105-112 | cannot be deleted | FACT | always | — | Deleting protected (module-owned, not in unprotected list) units is refused: archive instead. | N-U02-155 |
| VDR-U02-C230 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:205-216 | _filter_protected_uoms | FACT | always | — | Protected = xml-id in module uom and not in the unprotected list. | N-U02-155 |
| VDR-U02-C231 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:79-93 | existing data WON'T be updated | FACT | always | — | Onchange warning when relative_factor of a protected unit changes more than one day after creation. | N-U02-166 |
| VDR-U02-C232 | FUNCTION MAPPING REQUIRED | uom/security/uom_security.xml:4-6 | group_uom | FACT | always | — | Group uom.group_uom 'Manage Multiple Units of Measure' is declared in the uom module. | N-U02-161 |
| VDR-U02-C233 | FUNCTION MAPPING REQUIRED | product/models/res_config_settings.py:9 | group_uom | FACT | always | — | Setting 'Units of Measure & Packagings' is an implied-group switch for uom.group_uom. | N-U02-161 |
| VDR-U02-C234 | FUNCTION MAPPING REQUIRED | sale_timesheet/data/sale_service_data.xml:15-17 | uom.group_uom | FACT | module sale_timesheet installed | — | sale_timesheet makes base.group_user imply uom.group_uom (DB shows the implication). | N-U02-161 |
| VDR-U02-C235 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:118-123 | uom_ids | FACT | always | — | Template: uom_id (required, default Units) 'Default unit used for all stock operations'; uom_ids Many2many 'Packagings' excluding uom_id. | N-U02-145 |
| VDR-U02-C236 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:1571-1580 | _get_available_uoms | FACT | always | — | Available units = uom_id plus uom_ids; multiple-unit UI only when feature enabled, type not combo and more than one unit. | N-U02-162 |
| VDR-U02-C237 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:539-542 | allowed_uom_ids | FACT | module sale installed | — | Sales line allowed units = product uom_id plus uom_ids. | N-U02-145 |
| VDR-U02-C238 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:411-417 | seller_uom | FACT | module purchase installed | — | Purchase line allowed units = product uom plus packagings plus units of the product's vendor lines (variant-less or this variant). | N-U02-145 |
| VDR-U02-C239 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:882-885 | allowed_uom_ids | FACT | module account installed | — | Journal item allowed units = product uom plus packagings. | N-U02-145 |
| VDR-U02-C240 | FUNCTION MAPPING REQUIRED | stock/wizard/product_replenish.py:36-39 | seller_ids.product_uom_id | FACT | module stock installed | — | Replenishment wizard allowed units include vendor-line units. | N-U02-145 |
| VDR-U02-C241 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:474-487 | What to expect | FACT | always | — | Changing uom_id raises an onchange warning that 1 old unit = 1 new unit and existing records are relabelled, shown when documents use the product. | N-U02-153 |
| VDR-U02-C242 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:585-589 | skip_uom_conversion | FACT | always | — | write(uom_id) calls _update_uom on the variants with skip_uom_conversion before the template write. | N-U02-153 |
| VDR-U02-C243 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1197-1200 | _update_uom | FACT | always | — | Base _update_uom hook is a no-op returning True; modules override it to relabel documents. | N-U02-153 |
| VDR-U02-C244 | FUNCTION MAPPING REQUIRED | stock/models/product.py:784-808 | change of unit of measure can not be done | FACT | module stock installed | — | Stock _update_uom: if any stock move or move line uses another unit than the template's, the change is refused; otherwise moves/lines are relabelled. | N-U02-153 |
| VDR-U02-C245 | FUNCTION MAPPING REQUIRED | purchase/models/product.py:117-132 | po_lines.product_uom_id = to_uom_id | FACT | module purchase installed | — | Purchase _update_uom: refused if purchase lines use a different unit; otherwise lines relabelled and flushed. | N-U02-153 |
| VDR-U02-C246 | FUNCTION MAPPING REQUIRED | account/models/product.py:131-150 | posted Journal Entries | FACT | module account installed | — | Constraint: unit cannot change while posted journal items use a different unit than the template's. | N-U02-165 |
| VDR-U02-C247 | FUNCTION MAPPING REQUIRED | stock/models/product.py:1373-1404 | cannot change the ratio | FACT | module stock installed | — | uom write: factor/relative_factor/relative_uom_id change refused when open moves, open move lines or non-zero quants of products with that unit exist. | N-U02-154 |
| VDR-U02-C248 | FUNCTION MAPPING REQUIRED | stock/models/product.py:1406-1417 | stock.propagate_uom | FACT | module stock installed | — | Procurement quantities are converted to the quant unit unless config parameter stock.propagate_uom is '1'. | N-U02-157 |
| VDR-U02-C249 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:25-26 | product_uom_id | FACT | always | — | Vendor line unit: stored computed default product (variant or template) uom, editable, required. | N-U02-158 |
| VDR-U02-C250 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:27-29 | Product Unit | FACT | always | — | min_qty is in the vendor-line unit if set, else the product unit (help text), digits Product Unit. | N-U02-158 |
| VDR-U02-C251 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:213-220 | qty_in_product_uom | FACT | always | — | Pricelist rule quantity thresholds use the product unit (quantity converted). | N-U02-151 |
| VDR-U02-C252 | FUNCTION MAPPING REQUIRED | product/models/product_uom.py:8-26 | unique(barcode) | FACT | always | — | product.uom links product variant and unit with required unique barcode and company; barcode must not equal a product barcode. | N-U02-156 |
| VDR-U02-C253 | FUNCTION MAPPING REQUIRED | product/models/uom_uom.py:19-30 | product_uom_ids | FACT | always | — | uom.uom gains product_uom_ids (barcodes filtered by context) and an action to open packaging barcodes. | N-U02-142 |
| VDR-U02-C254 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:354-402 | product.weight_in_lbs | FACT | always | — | Weight/length/volume units come from ir.config_parameter product.weight_in_lbs and product.volume_in_cubic_feet (kg/mm/m3 default). | N-U02-152 |
| VDR-U02-C255 | FUNCTION MAPPING REQUIRED | product/models/res_config_settings.py:14-21 | product_weight_in_lbs | FACT | always | — | Settings expose weight (kg/lb) and volume (m3/ft3) units as config parameters. | N-U02-152 |
| VDR-U02-C256 | FUNCTION MAPPING REQUIRED | uom/security/ir.model.access.csv:2-3 | access_uom_uom_manager | FACT | always | — | ACL uom.uom: system admin full, internal users read only (2 rows); product manager full via product module row. | N-U02-155 |
| VDR-U02-C257 | FUNCTION MAPPING REQUIRED | uom/data/uom_data.xml:21-23 | product_uom_dozen | OBSERVATION | restored DB (config only) | — | DB: 30 uom_uom rows, columns include relative_factor, relative_uom_id, factor, parent_path, package_type_id (stock), timesheet_widget; no category or rounding column; Dozens archived, imperial units archived. | N-U02-141 |
| VDR-U02-C258 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:48 | product_uom_ids | OBSERVATION | restored DB (config only) | — | DB: 0 product_uom (packaging barcode) rows; unique constraint product_uom_barcode_uniq present; product_template has no packaging or purchase-unit column besides uom_id. | N-U02-142 |
| VDR-U02-C259 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:665-677 | uom_po_qty | FACT | module purchase installed | — | Purchase-order-line creation from procurement converts quantity to the vendor-line unit (HALF-UP) when it differs from the ordered unit; the product's vendor lines, not a product-level purchase unit field, carry the purchase unit. | N-U02-151 |
| VDR-U02-C260 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1033-1036 | quantity_uom_seller | FACT | always | — | Vendor selection converts the requested quantity into the vendor-line unit before comparing to min_qty. | N-U02-151 |
| VDR-U02-C261 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:70-74 | _compute_price | FACT | always | — | price_discounted converts the vendor unit price to the product unit and applies the discount. | N-U02-147 |
| VDR-U02-C262 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:35 | compute="_compute_sequence" | FACT | always | — | Unit sequence defaults to min(int(relative_factor*100), 1000) before first save. | N-U02-160 |
| VDR-U02-C263 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:422-428 | _trigger_uom_warning | FACT | always | — | Product-level unit-change warning is shown only when a module reports existing documents (stock/purchase override _trigger_uom_warning). | N-U02-166 |
| VDR-U02-C264 | FUNCTION MAPPING REQUIRED | stock/models/product.py:821-828 | _trigger_uom_warning | FACT | module stock installed | — | Stock reports a warning when any move exists for the variants. | N-U02-166 |
| VDR-U02-C265 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:36-38 | How much bigger or smaller | INFERENCE | always | — | The relative factor is stated against the reference unit ('how much bigger or smaller'), so one tree replaces fixed category tables (purpose inferred). | N-U02-143 |
| VDR-U02-C266 | FUNCTION MAPPING REQUIRED | stock/wizard/stock_lot_label_layout.py:33 | _has_common_reference | FACT | module stock installed | — | Lot label layout also uses the common-root test against the unit. | N-U02-163 |
| VDR-U02-C267 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:62-67 | Product Unit | INFERENCE | always | — | Lines 62-67: rounding is derived from one global precision, so a change of that precision affects every conversion (consequence inferred). | N-U02-167 |
| VDR-U02-C268 | FUNCTION MAPPING REQUIRED | uom/models/uom_uom.py:160-176 | amount = qty * self.factor | INFERENCE | always | — | The conversion body multiplies and divides factors without testing common roots, so a mis-configured cross-root conversion yields a number (consequence inferred). | N-U02-168 |
| VDR-U02-C269 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | UI selection of units | RT | UNKNOWN - EVIDENCE INSUFFICIENT: whether any screen restricts the unit choice to the product's root; resolve by UI/runtime check. | N-U02-169 |
| VDR-U02-C270 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:13-16 | ondelete='cascade' | FACT | always | — | partner_id (Vendor) required, cascade, check_company. | N-U02-195 |
| VDR-U02-C271 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:17-24 | Vendor Product Code | FACT | always | — | Vendor product name/code fields and sequence (default 1). | N-U02-180 |
| VDR-U02-C272 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:27-32 | min_qty | FACT | always | — | min_qty required (default 0, Product Unit digits), price float, price_discounted computed. | N-U02-180 |
| VDR-U02-C273 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:33-41 | date_end | FACT | always | — | company_id default current company; currency_id required default company currency; date_start/date_end are dates. | N-U02-180 |
| VDR-U02-C274 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:42-53 | Lead Time | FACT | always | — | product_id (variant, optional), product_tmpl_id (required, cascade), delay required default 1 day used for purchase planning. | N-U02-192 |
| VDR-U02-C275 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:54-57 | Discount (%) | FACT | always | — | discount percentage on the vendor line. | N-U02-180 |
| VDR-U02-C276 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:59-63 | _compute_product_uom_id | FACT | always | — | Unit defaults to variant or template unit. | N-U02-192 |
| VDR-U02-C277 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:70-74 | price_discounted | FACT | always | — | price_discounted = price converted to the product unit * (1 - discount/100). | N-U02-185 |
| VDR-U02-C278 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:65-68 | _compute_price | INFERENCE | always | — | Lines 30-31 and 65-68: price is a plain float without compute= while _compute_price (cost default) is defined but not bound to the field, so it is not executed. | N-U02-197 |
| VDR-U02-C279 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:82-86 | default_product_id | INFERENCE | always | — | _compute_product_id reads self.env.get('default_product_id') (registry lookup, not context) so the intended default is likely never applied. | N-U02-199 |
| VDR-U02-C280 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:101-116 | _sanitize_vals | FACT | always | — | create/write fill product_tmpl_id from product_id when only the variant is given. | N-U02-190 |
| VDR-U02-C281 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:118-119 | partner_id.sudo().active | FACT | always | — | _get_filtered_supplier keeps lines with no company or the given company, active partner, and no variant or the same variant. | N-U02-182 |
| VDR-U02-C282 | FUNCTION MAPPING REQUIRED | purchase/models/product.py:151-154 | params['order_id'].company_id | FACT | module purchase installed | — | Purchase override uses the order's company when an order is passed in params. | N-U02-182 |
| VDR-U02-C283 | FUNCTION MAPPING REQUIRED | purchase/models/product.py:147-149 | property_purchase_currency_id | FACT | module purchase installed | — | Onchange of partner sets line currency to the vendor's purchase currency or company currency. | N-U02-192 |
| VDR-U02-C284 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1019-1021 | s.sequence, -s.min_qty, s.price | FACT | always | — | _prepare_sellers: filtered lines sorted by (sequence, -min_qty, price, id), read as sudo. | N-U02-184 |
| VDR-U02-C285 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1023-1050 | force_uom | FACT | always | — | _get_filtered_sellers: skip by date window, forced unit, partner/parent, min quantity in line unit (float_compare), variant mismatch. | N-U02-182 |
| VDR-U02-C286 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1041-1042 | force_uom | FACT | always | — | With params.force_uom only lines whose unit equals the requested unit or the product's unit pass. | N-U02-183 |
| VDR-U02-C287 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1052-1074 | price_discounted | FACT | always | — | _select_seller: keeps lines of the first partner (in sorted order), then orders by discounted price converted to company currency (then sequence, id); ordered_by can put another key first; returns one line. | N-U02-184 |
| VDR-U02-C288 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1052-1056 | ordered_by | FACT | always | — | Sort key = (price_discounted, sequence, id), or (ordered_by, price_discounted, sequence, id) for another key. | N-U02-186 |
| VDR-U02-C289 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:272-283 | selected_seller_id | FACT | module purchase installed | — | Purchase line computes selected_seller_id with _select_seller(partner, abs(qty), order date, line unit, params). | N-U02-187 |
| VDR-U02-C290 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:768-773 | force_uom | FACT | module purchase installed | — | Purchase lines pass params order_id and force_uom=True. | N-U02-183 |
| VDR-U02-C291 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:683-697 | _convert | FACT | module purchase installed | — | Procurement-created line: price from seller converted to line unit and to order currency at order date; name includes vendor code via seller_id context. | N-U02-187 |
| VDR-U02-C292 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:362-366 | seller.delay | FACT | module purchase installed | — | Planned date = order date + seller.delay days (calendar days) or today + delay. | N-U02-187 |
| VDR-U02-C293 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock_rule.py:187-197 | _select_seller | FACT | module purchase_stock installed | — | Replenishment chooses supplier via _select_seller (rule company, quantity, date, unit); falls back to first prepared seller. | N-U02-188 |
| VDR-U02-C294 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock_rule.py:332 | supplier'].delay | FACT | module purchase_stock installed | — | Order date = planned date minus supplier delay in plain calendar days. | N-U02-188 |
| VDR-U02-C295 | FUNCTION MAPPING REQUIRED | mrp_subcontracting/models/product.py:23-26 | subcontractor_ids | FACT | module mrp_subcontracting installed | — | Subcontracting restricts sellers to the BoM's subcontractors when requested. | N-U02-189 |
| VDR-U02-C296 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/product.py:17-22 | purchase_requisition_id | FACT | module purchase_requisition installed | — | Agreement-linked vendor lines are only offered for orders of that agreement. | N-U02-189 |
| VDR-U02-C297 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2936-2943 | ordered_by='min_qty' | FACT | module account installed | — | Vendor-bill price lookup uses _select_seller with quantity None ordered by min_qty. | N-U02-186 |
| VDR-U02-C298 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:337-354 | supplier_info.product_code | FACT | always | — | code = vendor product code when partner in context matches an allowed (company-compatible) vendor line, preferring the variant-specific one. | N-U02-191 |
| VDR-U02-C299 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:838-875 | seller_variant | FACT | always | — | Display name with partner in context uses vendor product name/code, filtered by company. | N-U02-191 |
| VDR-U02-C300 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:891-899 | supplier_domain | FACT | always | — | Name search also matches vendor product code/name for the partner in context. | N-U02-191 |
| VDR-U02-C301 | FUNCTION MAPPING REQUIRED | product/security/product_security.xml:57-61 | product_supplierinfo_comp_rule | FACT | always | — | Record rule: vendor lines visible when company is empty or parent_of user's companies. | N-U02-196 |
| VDR-U02-C302 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:190-194 | _select_seller | FACT | module sale_purchase installed | — | Sale-driven RFQ creation selects a vendor line for the service product. | N-U02-194 |
| VDR-U02-C303 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1019 | _prepare_sellers | OBSERVATION | restored DB (config only) | — | DB: 0 product_supplierinfo rows; ACL rows: user read, manager full; rule product_supplierinfo_comp_rule present and global. | N-U02-193 |
| VDR-U02-C304 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:126-127 | seller_ids | FACT | always | — | Template seller_ids depends on company context; variant_seller_ids is a second view of the same lines. | N-U02-193 |
| VDR-U02-C305 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:51-53 | Used by the scheduler | INFERENCE | always | — | Lead-time help text states the line is used by the scheduler for purchase planning (purpose of automatic proposal inferred). | N-U02-181 |
| VDR-U02-C306 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1047-1048 | seller.product_id != self | INFERENCE | always | — | Variant-specific lines are only excluded for other variants; there is no explicit precedence of a variant line over a generic line besides ordering. | N-U02-198 |
| VDR-U02-C307 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1037-1040 | seller.date_start | FACT | always | — | Applicability of a vendor line is decided only by its date window (date_start/date_end) and the other filters; there is no state field. | N-U02-200 |
| VDR-U02-C308 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:13-26 | _parent_store | FACT | always | — | account.analytic.plan is a parent_store hierarchy with name (translated), parent, complete_name. | N-U02-210 |
| VDR-U02-C309 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:77-92 | default_applicability | FACT | always | — | default_applicability is company_dependent (optional/mandatory/unavailable); applicability_ids one2many by current company. | N-U02-215 |
| VDR-U02-C310 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:104-121 | analytic.project_plan | FACT | always | — | The project plan id comes from ir.config_parameter analytic.project_plan (error if missing); column name is account_id for it, x_plan<id>_id for other root plans. | N-U02-211 |
| VDR-U02-C311 | FUNCTION MAPPING REQUIRED | analytic/data/analytic_data.xml:13-17 | analytic.project_plan | FACT | always | — | Seed: parameter analytic.project_plan = 1 and plan 'Project' with optional applicability; comment states it cannot be changed safely once set. | N-U02-211 |
| VDR-U02-C312 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:314-374 | _sync_plan_column | FACT | always | — | Creating/renaming/reparenting a plan syncs dynamic many2one columns (root plans) or related grouping fields (sub-plans) on every model using analytic.plan.fields.mixin, with an index. | N-U02-211 |
| VDR-U02-C313 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:270-278 | _find_plan_column | FACT | always | — | Unlinking a plan deletes its dynamic field/column. | N-U02-231 |
| VDR-U02-C314 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:184-188 | cannot add a parent | FACT | always | — | Onchange: the base (project) plan cannot have a parent. | N-U02-228 |
| VDR-U02-C315 | FUNCTION MAPPING REQUIRED | analytic/models/ir_config_parameter.py:11-28 | valid analytic plan | FACT | always | — | Writing analytic.project_plan requires a numeric id of a non-sub plan; columns are re-synced and the new plan's field removed. | N-U02-228 |
| VDR-U02-C316 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:213-244 | get_relevant_plans | FACT | always | — | get_relevant_plans returns root plans with accounts whose applicability is not unavailable, plus forced plans of existing accounts; cached per request kwargs. | N-U02-215 |
| VDR-U02-C317 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:246-268 | score = 0.5 | FACT | always | — | _get_applicability: start from default (company) and replace it by the highest-scoring applicability rule (company 0.5, other criteria +1, mismatch -1). | N-U02-215 |
| VDR-U02-C318 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:449-458 | business_domain | FACT | always | — | Applicability score: 0.5 if company-specific, +1 on matching business domain, -1 on mismatch. | N-U02-215 |
| VDR-U02-C319 | FUNCTION MAPPING REQUIRED | account/models/account_analytic_plan.py:59-76 | account_prefix | FACT | module account installed | — | Account module extends applicability scoring with financial account prefix (+1/-1) and product category (+1/-1) and adds domains invoice and bill. | N-U02-215 |
| VDR-U02-C320 | FUNCTION MAPPING REQUIRED | purchase/models/analytic_applicability.py:10-15 | purchase_order | FACT | module purchase installed | — | Purchase adds the business domain 'purchase_order'. | N-U02-215 |
| VDR-U02-C321 | FUNCTION MAPPING REQUIRED | sale/models/analytic.py:12-21 | sale_order | FACT | module sale installed | — | Sales adds business domain 'sale_order' and the sales-order-item field on analytic lines. | N-U02-215 |
| VDR-U02-C322 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/analytic_applicability.py:10-15 | timesheet | FACT | module hr_timesheet installed | — | Timesheet adds business domain 'timesheet'. | N-U02-215 |
| VDR-U02-C323 | FUNCTION MAPPING REQUIRED | project_stock_account/models/analytic_applicability.py:10-15 | stock_picking | FACT | module project_stock_account installed | — | Stock account adds business domain 'stock_picking'. | N-U02-215 |
| VDR-U02-C324 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_account.py:38-49 | root_plan_id | FACT | always | — | Analytic account requires a plan; root_plan_id stored related. | N-U02-210 |
| VDR-U02-C325 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_account.py:95-102 | analytical disaster | FACT | always | — | Constraint: company of an account cannot change when it has lines of other companies. | N-U02-227 |
| VDR-U02-C326 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_account.py:162-203 | _compute_debit_credit_balance | FACT | always | — | Balance/debit/credit computed from lines of the plan column, converted to company currency, restricted to selected companies and date context. | N-U02-222 |
| VDR-U02-C327 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_account.py:205-243 | RedirectWarning | FACT | always | — | Changing an account's plan moves existing lines to the new column or raises RedirectWarning when data would be overwritten. | N-U02-223 |
| VDR-U02-C328 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:381-405 | _update_accounts_in_analytic_lines | FACT | always | — | Re-parenting a plan moves accounts in analytic lines before/after columns are re-synced. | N-U02-223 |
| VDR-U02-C329 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_distribution_model.py:9-37 | partner_category_id | FACT | always | — | Distribution model fields: partner, partner category, company, sequence, analytic distribution (mixin). | N-U02-213 |
| VDR-U02-C330 | FUNCTION MAPPING REQUIRED | account/models/account_analytic_distribution_model.py:9-32 | product_categ_id | FACT | module account installed | — | Account module adds account_prefix, product and product category criteria to distribution models. | N-U02-213 |
| VDR-U02-C331 | FUNCTION MAPPING REQUIRED | account/models/account_analytic_distribution_model.py:34-49 | delimiter_pattern | FACT | module account installed | — | Account-prefix match splits the model's prefixes on ; or , and tests startswith against the line's account code. | N-U02-213 |
| VDR-U02-C332 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_distribution_model.py:60-76 | _merge_distribution | FACT | always | — | _get_distribution: matching models in order; a model is ignored if its root plans were already applied; distributions merged with __update__ plan list. | N-U02-217 |
| VDR-U02-C333 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_distribution_model.py:86-99 | _create_domain | FACT | always | — | Applicable models: each criterion matches the value or is empty (partner category list also allows empty). | N-U02-213 |
| VDR-U02-C334 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_distribution_model.py:39-58 | belonging to a specific company | FACT | always | — | Constraint: a model with company-specific accounts must be specific to the same company. | N-U02-227 |
| VDR-U02-C335 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:244-275 | _merge_distribution | FACT | always | — | _merge_distribution combines unchanged-plan and changed-plan parts so percentages multiply across plans; remainder keys keep the larger side. | N-U02-217 |
| VDR-U02-C336 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:16-30 | analytic_distribution | FACT | always | — | analytic_distribution is a stored Json (copy=True) keyed by comma-joined account ids with percentage values; distribution_analytic_account_ids derived. | N-U02-212 |
| VDR-U02-C337 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:169-180 | Percentage Analytic | FACT | always | — | create/write round distribution percentages to the 'Percentage Analytic' precision. | N-U02-221 |
| VDR-U02-C338 | FUNCTION MAPPING REQUIRED | analytic/data/analytic_data.xml:4-6 | Percentage Analytic | FACT | always | — | Decimal precision 'Percentage Analytic' is seeded with 2 digits. | N-U02-221 |
| VDR-U02-C339 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:182-196 | 100% analytic distribution | FACT | context validate_analytic | — | _validate_distribution (only with context validate_analytic): for each mandatory plan the summed percentage must equal 100, else ValidationError. | N-U02-216 |
| VDR-U02-C340 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3188-3219 | _validate_analytic_distribution | FACT | module account installed | — | Journal item validation runs _validate_distribution per product line with business domain invoice/bill/general; missing distribution raises ValidationError (one move) or RedirectWarning. | N-U02-216 |
| VDR-U02-C341 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2053-2076 | has_invalid_analytics | FACT | module account installed | — | has_invalid_analytics flags lines whose mandatory-plan distribution is incomplete (skipping receivable/payable/cash/credit-card accounts). | N-U02-216 |
| VDR-U02-C342 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1239-1252 | _get_distribution | FACT | module account installed | — | Journal-item analytic_distribution is computed from the related document distribution merged with distribution-model results (cached by arguments). | N-U02-234 |
| VDR-U02-C343 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1254-1270 | account_prefix | FACT | module account installed | — | Distribution arguments: product, product category, partner, partner category, account code prefix, company and root plans already served. | N-U02-234 |
| VDR-U02-C344 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1248-1259 | _get_distribution | FACT | module sale installed | — | Sales lines compute analytic_distribution from distribution models using product, category, order partner and category, company. | N-U02-234 |
| VDR-U02-C345 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:368-379 | _get_distribution | FACT | module purchase installed | — | Purchase lines compute analytic_distribution the same way. | N-U02-234 |
| VDR-U02-C346 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3221-3232 | _create_analytic_lines | FACT | module account installed | — | _create_analytic_lines validates, builds values per line and creates analytic lines with skip_analytic_sync. | N-U02-218 |
| VDR-U02-C347 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3249-3281 | -self.balance | FACT | module account installed | — | Analytic line values: amount = -balance * percent (remainder when the plan reaches 100), plan column, date, name, partner, quantity, product, unit, general account, reference, user, company, category invoice/vendor_bill/other. | N-U02-219 |
| VDR-U02-C348 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3297-3321 | rounding_error | FACT | module account installed | — | Rounding error of analytic line amounts is redistributed over lines in company currency steps. | N-U02-218 |
| VDR-U02-C349 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3234-3247 | is_zero(line_values.get('amount')) | FACT | module account installed | — | Zero-amount analytic line values are skipped. | N-U02-218 |
| VDR-U02-C350 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_line.py:237-267 | _inverse_analytic_distribution | FACT | always | — | Writing analytic_distribution on an analytic line splits it: first account set on the line, further combinations created as copies with proportional amounts. | N-U02-220 |
| VDR-U02-C351 | FUNCTION MAPPING REQUIRED | account/models/account_analytic_line.py:125-129 | _update_analytic_distribution | FACT | module account installed | — | Creating analytic lines updates the distribution of the source journal item. | N-U02-220 |
| VDR-U02-C352 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_line.py:93-98 | At least one analytic account | FACT | always | — | Constraint across plan columns: every analytic line needs at least one account. | N-U02-227 |
| VDR-U02-C353 | FUNCTION MAPPING REQUIRED | account/models/account_analytic_line.py:66-70 | correct financial account | FACT | module account installed | — | Constraint: analytic line's general account must equal its journal item's account. | N-U02-229 |
| VDR-U02-C354 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_line.py:163-231 | company_id | FACT | always | — | Analytic line fields: name, date, amount (Monetary), unit_amount, unit, partner, user, company (required), currency stored related, category. | N-U02-219 |
| VDR-U02-C355 | FUNCTION MAPPING REQUIRED | analytic/security/analytic_security.xml:5-31 | analytic_line_comp_rule | FACT | always | — | Four global rules: accounts, applicabilities and distribution models shared when company empty or parent_of company_ids; lines restricted to company_ids. | N-U02-225 |
| VDR-U02-C356 | FUNCTION MAPPING REQUIRED | analytic/security/ir.model.access.csv:2-6 | group_analytic_accounting | FACT | always | — | Five ACL rows, all for group_analytic_accounting with full rights (account, line, plan, applicability, distribution model). | N-U02-225 |
| VDR-U02-C357 | FUNCTION MAPPING REQUIRED | analytic/models/res_config_settings.py:10 | group_analytic_accounting | FACT | always | — | Setting 'Analytic Accounting' is an implied-group switch for analytic.group_analytic_accounting. | N-U02-225 |
| VDR-U02-C358 | FUNCTION MAPPING REQUIRED | analytic/security/analytic_security.xml:35-37 | Analytic Accounting | OBSERVATION | restored DB (config only) | — | DB: 1 plan (Project, no parent), 1 account, 2 analytic lines, 0 applicability rows, 0 distribution models; analytic.project_plan = 1; group analytic.group_analytic_accounting (id 18) is not implied by any group and has no user members counted; 5 ACL rows and 4 rules match source. | N-U02-226 |
| VDR-U02-C359 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:32-39 | gin(regexp_split_to_array | FACT | always | — | A GIN index on the distribution keys is created for stored distribution columns of every model using the mixin. | N-U02-233 |
| VDR-U02-C360 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_line.py:16-33 | auto_account_id | FACT | always | — | Plan-fields mixin: fixed account_id (project plan) plus a magic auto_account_id for search/one2many on all plans. | N-U02-211 |
| VDR-U02-C361 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_distribution_model.py:23-30 | automatically take this as an analytic account | INFERENCE | always | — | Help texts state that matching documents automatically take the analytic account (purpose of prefill inferred). | N-U02-214 |
| VDR-U02-C362 | FUNCTION MAPPING REQUIRED | account/models/account_analytic_line.py:40-46 | ondelete='cascade' | FACT | module account installed | — | Analytic line move_line_id is cascade-on-delete, so lines vanish with their journal item; accounts have an active flag. | N-U02-224 |
| VDR-U02-C363 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:184-186 | mandatory_plans_ids | INFERENCE | context validate_analytic | — | Only plans whose applicability is mandatory are validated; failure raises 'One or more lines require a 100% analytic distribution' (ValidationError), so changing applicability changes blocking at posting. | N-U02-230 |
| VDR-U02-C364 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:182-196 | get_relevant_plans | INFERENCE | context validate_analytic | — | No check applies to optional plans, so their distributions may total any percentage. | N-U02-232 |
| VDR-U02-C365 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_plan.py:314-374 | _sync_plan_column | FACT | always | — | Plan creation adds a column and a database index on each mixin model (structural DDL). | N-U02-231 |
| VDR-U02-C366 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | volume behaviour | RT | UNKNOWN - EVIDENCE INSUFFICIENT: performance/reporting behaviour at scale of the Json distribution and plan columns; needs load testing. | N-U02-233 |
| VDR-U02-C367 | FUNCTION MAPPING REQUIRED | product/models/product_document.py:8-23 | _inherits | FACT | always | — | product.document delegates to an ir.attachment (required, cascade) and adds active and sequence. | N-U02-260 |
| VDR-U02-C368 | FUNCTION MAPPING REQUIRED | product/models/product_document.py:25-33 | valid URL | FACT | always | — | Onchange: link documents must start with http://, https:// or ftp://. | N-U02-267 |
| VDR-U02-C369 | FUNCTION MAPPING REQUIRED | product/models/product_document.py:57-60 | attachments.unlink | FACT | always | — | Deleting a document deletes its attachment. | N-U02-260 |
| VDR-U02-C370 | FUNCTION MAPPING REQUIRED | product/models/ir_attachment.py:9-26 | disable_product_documents_creation | FACT | always | — | Attachments created on product.product/product.template without res_field create a product.document (unless context flag). | N-U02-266 |
| VDR-U02-C371 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:164-170 | product_document_ids | FACT | always | — | Template documents relation by res_model/res_id domain with count. | N-U02-260 |
| VDR-U02-C372 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:1552-1555 | _get_product_document_domain | FACT | always | — | Document domain covers the template and its variants. | N-U02-260 |
| VDR-U02-C373 | FUNCTION MAPPING REQUIRED | product/security/product_security.xml:39-43 | product_document_comp_rule | FACT | always | — | Documents visible when company empty or parent_of user companies. | N-U02-260 |
| VDR-U02-C374 | FUNCTION MAPPING REQUIRED | product/models/product_tag.py:7-48 | Tag name already exists | FACT | always | — | product.tag: name (translated) unique, color, visible_to_customers, image; m2m to templates and variants. | N-U02-261 |
| VDR-U02-C375 | FUNCTION MAPPING REQUIRED | product/models/product_tag.py:50-62 | _compute_product_ids | FACT | always | — | product_ids = template variants union variant-level tags; search through both relations. | N-U02-261 |
| VDR-U02-C376 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:89-95 | additional_product_tag_ids | FACT | always | — | Variant tags add to the template's tags (all_product_tag_ids computed, sorted by sequence). | N-U02-261 |
| VDR-U02-C377 | FUNCTION MAPPING REQUIRED | product/models/product_combo.py:12-30 | base_price | FACT | always | — | product.combo: name, sequence, company, items, computed currency and base_price (minimum item price). | N-U02-262 |
| VDR-U02-C378 | FUNCTION MAPPING REQUIRED | product/models/product_combo.py:44-62 | to_currency=combo.currency_id | FACT | always | — | Combo currency = company currency or main company currency; base price = min item list price converted at now. | N-U02-268 |
| VDR-U02-C379 | FUNCTION MAPPING REQUIRED | product/models/product_combo.py:75-79 | _check_company | FACT | always | — | Changing a combo's company re-checks templates and items for company consistency. | N-U02-272 |
| VDR-U02-C380 | FUNCTION MAPPING REQUIRED | product/models/product_combo_item.py:12-28 | extra_price | FACT | always | — | Combo item: variant (not combo type, restrict on delete, check_company), related list price, extra_price default 0. | N-U02-262 |
| VDR-U02-C381 | FUNCTION MAPPING REQUIRED | product/security/product_security.xml:63-69 | product_combo_comp_rule | FACT | always | — | Combos visible when company empty or parent_of user companies. | N-U02-272 |
| VDR-U02-C382 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:856-861 | combo_items_to_unlink | INFERENCE | always | — | Lines 856-861 of product_template.py (variant removal loop): combo items referencing variants removed by _create_variant_ids are unlinked (pointer note: loop is at 856-861 in the same file). | N-U02-270 |
| VDR-U02-C383 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_exclusion.py:6-26 | value_ids | FACT | always | — | Exclusion model: ptav, template, excluded values; domain only active values of the same template. | N-U02-263 |
| VDR-U02-C384 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_exclusion.py:28-47 | _create_variant_ids | FACT | always | — | Create/unlink/write of exclusions call _create_variant_ids on the templates. | N-U02-269 |
| VDR-U02-C385 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_value.py:44-49 | exclude_for | FACT | always | — | ptav.exclude_for: exclusions against other values of the product or of optional/accessory products. | N-U02-263 |
| VDR-U02-C386 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:974-988 | _complete_inverse_exclusions | FACT | always | — | Exclusions are completed symmetrically (A excludes B => B excludes A). | N-U02-263 |
| VDR-U02-C387 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:1033-1056 | parent_combination | FACT | always | — | Parent-combination exclusions: a value of the parent product can exclude all or some values of this template. | N-U02-263 |
| VDR-U02-C388 | FUNCTION MAPPING REQUIRED | product/wizard/update_product_attribute_value.py:52-73 | product_tmpl_id.company_id | FACT | always | — | Wizard confirm: add value to all attribute lines of that attribute, or reset price_extra on all template values to default; both limited to products of the user's companies or without company. | N-U02-264 |
| VDR-U02-C389 | FUNCTION MAPPING REQUIRED | product/models/product_attribute_value.py:152-180 | update.product.attribute.value | FACT | always | — | Attribute value actions open the wizard in add or update_extra_price mode. | N-U02-271 |
| VDR-U02-C390 | FUNCTION MAPPING REQUIRED | product/models/product_catalog_mixin.py:39-48 | Domain('type', '!=', 'combo') | FACT | always | — | Catalog domain: products with no company or parent_of the document company, excluding combos. | N-U02-265 |
| VDR-U02-C391 | FUNCTION MAPPING REQUIRED | product/models/product_catalog_mixin.py:129-134 | display_uom | FACT | always | — | Catalog context shows unit only when the user has uom.group_uom. | N-U02-265 |
| VDR-U02-C392 | FUNCTION MAPPING REQUIRED | product/security/ir.model.access.csv:34-36 | access_product_document_manager | FACT | always | — | ACL: document user read, manager full; wizard model manager rwc (no delete). | N-U02-273 |
| VDR-U02-C393 | FUNCTION MAPPING REQUIRED | product/models/product_tag.py:8 | product.tag | OBSERVATION | restored DB (config only) | — | DB: 0 documents, 0 tags, 0 combos, 0 attributes/values, 0 exclusions; product_tag_name_uniq constraint present. | N-U02-273 |
| VDR-U02-C394 | FUNCTION MAPPING REQUIRED | product/models/product_template_attribute_exclusion.py:28-32 | _create_variant_ids | INFERENCE | always | — | Exclusion create triggers variant regeneration for the template, which may archive or delete variants without a preview (consequence inferred). | N-U02-274 |
| VDR-U02-C395 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | label printing and web shop | — | UNKNOWN - EVIDENCE INSUFFICIENT: label printing wizard and web-shop uses of tags/documents not studied. | N-U02-275 |
| VDR-U02-C396 | FUNCTION MAPPING REQUIRED | product/models/product_document.py:8-23 | sequence | INFERENCE | always | — | Document, tag, combo and exclusion models sit next to the product definition with their own order and company fields (purpose inferred). | N-U02-276 |
| VDR-U02-C397 | FUNCTION MAPPING REQUIRED | product/models/product_document.py:22-23 | active = fields.Boolean | FACT | always | — | Product document has an active flag. | N-U02-277 |
| VDR-U02-C398 | FUNCTION MAPPING REQUIRED | product/security/product_security.xml:20-25 | group_product_manager | FACT | always | — | Group product.group_product_manager (name 'Create') is implied by base.group_system and linked to user_root, in privilege 'Products'. | N-U02-281 |
| VDR-U02-C399 | FUNCTION MAPPING REQUIRED | product/security/product_security.xml:27-29 | base.user_admin | FACT | always | — | The admin user is added to the product manager group. | N-U02-281 |
| VDR-U02-C400 | FUNCTION MAPPING REQUIRED | product/security/product_security.xml:12-18 | Basic Pricelists | FACT | always | — | Feature groups group_product_pricelist and group_product_variant declared with names only (no ACL attached). | N-U02-293 |
| VDR-U02-C401 | FUNCTION MAPPING REQUIRED | product/security/product_security.xml:33-37 | product_comp_rule | FACT | always | — | Global rule on product.template: company parent_of company_ids or no company. | N-U02-283 |
| VDR-U02-C402 | FUNCTION MAPPING REQUIRED | product/security/product_security.xml:45-55 | product_pricelist_item_comp_rule | FACT | always | — | Global rules on product.pricelist and product.pricelist.item with the same domain. | N-U02-283 |
| VDR-U02-C403 | FUNCTION MAPPING REQUIRED | product/security/ir.model.access.csv:2-17 | access_product_template_user | FACT | always | — | Internal users (base.group_user) have read-only rows on category, template, supplierinfo, pricelist, pricelist item, variant, attribute, attribute value, custom value, ptav, exclusion, attribute line, tag, combo and combo item. | N-U02-280 |
| VDR-U02-C404 | FUNCTION MAPPING REQUIRED | product/security/ir.model.access.csv:18-33 | access_product_template_manager | FACT | always | — | Product manager group has full rights (r,w,c,d) on the same models plus tag, combo and item. | N-U02-280 |
| VDR-U02-C405 | FUNCTION MAPPING REQUIRED | product/security/ir.model.access.csv:7 | base.group_partner_manager | FACT | always | — | Partner managers have an additional read row on product.pricelist. | N-U02-282 |
| VDR-U02-C406 | FUNCTION MAPPING REQUIRED | product/security/ir.model.access.csv:30 | access_product_label_layout_user | FACT | always | — | Internal users have full rights on the label layout wizard. | N-U02-282 |
| VDR-U02-C407 | FUNCTION MAPPING REQUIRED | product/security/ir.model.access.csv:34-39 | access_product_uom_manager | FACT | always | — | Document, wizard, product.uom (packaging) and uom.uom rows for product manager (and read for users). | N-U02-288 |
| VDR-U02-C408 | FUNCTION MAPPING REQUIRED | uom/security/ir.model.access.csv:2-3 | access_uom_uom_user | FACT | always | — | uom.uom: system admin full, internal users read. | N-U02-288 |
| VDR-U02-C409 | FUNCTION MAPPING REQUIRED | analytic/security/ir.model.access.csv:2-6 | access_account_analytic_plan | FACT | always | — | All five analytic models are accessible only by group_analytic_accounting (full rights). | N-U02-287 |
| VDR-U02-C410 | FUNCTION MAPPING REQUIRED | analytic/security/analytic_security.xml:12-17 | analytic_line_comp_rule | FACT | always | — | Analytic line rule: company_id in company_ids (no null company allowed). | N-U02-287 |
| VDR-U02-C411 | FUNCTION MAPPING REQUIRED | utm/security/ir.model.access.csv:2-11 | access_utm_campaign_user | FACT | always | — | Trackers: users r/w/c without delete on campaign, medium, source; read on stage and tag; system admin full. | N-U02-289 |
| VDR-U02-C412 | FUNCTION MAPPING REQUIRED | resource/security/ir.model.access.csv:2-9 | access_resource_calendar_leaves_user | FACT | always | — | Calendars/attendances: users read, system admin full; resources read; time off: users and admin full rights subject to rules. | N-U02-290 |
| VDR-U02-C413 | FUNCTION MAPPING REQUIRED | resource/security/resource_security.xml:4-28 | resource_calendar_leaves_rule_group_user_create | FACT | always | — | Time-off rules: employees read own or global entries and modify own; administrators (erp manager) modify global entries. | N-U02-290 |
| VDR-U02-C414 | FUNCTION MAPPING REQUIRED | resource/security/resource_security.xml:30-40 | resource_resource_multi_company | FACT | always | — | Global multi-company rules on resource and time off: company in company_ids or none. | N-U02-290 |
| VDR-U02-C415 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:24-25 | _check_company_auto | FACT | always | — | product.template enables automatic company consistency checks with parent_of domain. | N-U02-291 |
| VDR-U02-C416 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist_item.py:80-87 | check_company=True | FACT | always | — | Pricelist rule product, variant and base pricelist are company-checked. | N-U02-291 |
| VDR-U02-C417 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:22 | _check_company_domain | FACT | always | — | Variant declares company domain but no auto check; rules for product.product are not declared in product (DB confirms no rule on product.product). | N-U02-285 |
| VDR-U02-C418 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:62-68 | groups="base.group_user" | FACT | always | — | standard_price is restricted to internal users by field groups. | N-U02-286 |
| VDR-U02-C419 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:742-746 | standard_price field can only be seen | FACT | always | — | Price computation reads the cost as superuser. | N-U02-286 |
| VDR-U02-C420 | FUNCTION MAPPING REQUIRED | product/security/ir.model.access.csv:2 | access_product_category_user | OBSERVATION | restored DB (config only) | — | DB counts by module (ir_model_access via model data): product 38, uom 2, analytic 5, utm 10, resource 8 - equal to source rows (product 38 of 39 lines excluding header). | N-U02-292 |
| VDR-U02-C421 | FUNCTION MAPPING REQUIRED | product/security/product_security.xml:31-37 | noupdate="1" | OBSERVATION | restored DB (config only) | — | DB rules by module: product 6 (all global), analytic 4 (all global), resource 5 (2 global); uom and utm 0 - equal to source (product 6 rules, analytic 4, resource 5). | N-U02-292 |
| VDR-U02-C422 | FUNCTION MAPPING REQUIRED | product/security/product_security.xml:20-25 | implied_by_ids | OBSERVATION | restored DB (config only) | — | DB groups defined by these modules: product.group_product_manager, product.group_product_pricelist, product.group_product_variant, uom.group_uom, analytic.group_analytic_accounting; base.group_user implies group_uom, group_product_pricelist and group_product_variant; product manager has 2 user members. | N-U02-293 |
| VDR-U02-C423 | FUNCTION MAPPING REQUIRED | product/security/product_security.xml:63-69 | ir.rule | OBSERVATION | restored DB (config only) | — | DB: no ir.rule exists for product.product, product.category, uom.uom, product.attribute, product.tag, combo item or packaging. | N-U02-284 |
| VDR-U02-C424 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:292-295 | _check_company | UNKNOWN | company-restricted variant read | RT | UNKNOWN - EVIDENCE INSUFFICIENT: whether the template rule filters variant reads is not stated in the module; resolve with a two-company runtime test. | N-U02-295 |
| VDR-U02-C425 | FUNCTION MAPPING REQUIRED | product/models/product_attribute.py:7-17 | product.attribute | FACT | always | — | Attributes and values have no company field (global master data). | N-U02-284 |
| VDR-U02-C426 | FUNCTION MAPPING REQUIRED | product/security/product_security.xml:33-37 | product_comp_rule | INFERENCE | always | — | Company rules exist only for template, document, pricelist, rule, vendor line and combo; the other master data are shared, so multi-company separation of them depends on consistency checks (consequence inferred). | N-U02-294 |
| VDR-U02-C427 | FUNCTION MAPPING REQUIRED | product/security/ir.model.access.csv:18-20 | access_product_category_manager | INFERENCE | always | — | Read rows for internal users versus full rows for the product manager group separate usage from maintenance of master data (purpose inferred). | N-U02-296 |
| VDR-U02-C428 | FUNCTION MAPPING REQUIRED | product/__manifest__.py:25-52 | 'data': [ | INFERENCE | always | — | Lines 25-52 list the data files of product (data, security, views, reports): no cron or automation file is declared. | N-U02-320 |
| VDR-U02-C429 | FUNCTION MAPPING REQUIRED | uom/__manifest__.py:12-17 | 'data': [ | INFERENCE | always | — | Data files of uom list no scheduled action. | N-U02-320 |
| VDR-U02-C430 | FUNCTION MAPPING REQUIRED | analytic/__manifest__.py:15-24 | 'data': [ | INFERENCE | always | — | Data files of analytic list no scheduled action. | N-U02-320 |
| VDR-U02-C431 | FUNCTION MAPPING REQUIRED | utm/__manifest__.py:11-24 | 'data': [ | INFERENCE | always | — | Data files of utm list no scheduled action. | N-U02-320 |
| VDR-U02-C432 | FUNCTION MAPPING REQUIRED | resource/__manifest__.py:16-28 | 'data': [ | INFERENCE | always | — | Data files of resource list no scheduled action. | N-U02-320 |
| VDR-U02-C433 | FUNCTION MAPPING REQUIRED | product/models/res_config_settings.py:9-21 | implied_group | FACT | always | — | Settings fields: group_uom, group_product_variant, group_product_pricelist (implied groups), module_loyalty, product_weight_in_lbs and product_volume_volume_in_cubic_feet (config parameters). | N-U02-321 |
| VDR-U02-C434 | FUNCTION MAPPING REQUIRED | analytic/models/res_config_settings.py:10 | group_analytic_accounting | FACT | always | — | Setting 'Analytic Accounting' implies the analytic group. | N-U02-321 |
| VDR-U02-C435 | FUNCTION MAPPING REQUIRED | product/models/res_config_settings.py:23-34 | will be archived | FACT | always | — | Onchange warns that disabling pricelists archives every active pricelist. | N-U02-322 |
| VDR-U02-C436 | FUNCTION MAPPING REQUIRED | product/models/res_config_settings.py:36-43 | _activate_or_create_pricelists | FACT | always | — | set_values: turning the feature on activates/creates default pricelists; turning it off archives all pricelists. | N-U02-322 |
| VDR-U02-C437 | FUNCTION MAPPING REQUIRED | product/models/res_company.py:9-13 | _activate_or_create_pricelists | FACT | always | — | Company create creates default pricelists when the feature is on. | N-U02-323 |
| VDR-U02-C438 | FUNCTION MAPPING REQUIRED | resource/models/res_company.py:35-45 | _create_resource_calendar | FACT | always | — | Company create creates the default calendar 'Standard 40 hours/week' if none and assigns company to calendars created from the form. | N-U02-323 |
| VDR-U02-C439 | FUNCTION MAPPING REQUIRED | product/models/res_company.py:53-69 | disable_company_pricelist_creation | FACT | always | — | Company write with currency change delays pricelist creation until after the write so the currency is right. | N-U02-324 |
| VDR-U02-C440 | FUNCTION MAPPING REQUIRED | product/models/res_currency.py:10-16 | _activate_group_multi_currency | FACT | always | — | Activating multi-currency applies the pricelist group to internal users and creates default pricelists. | N-U02-326 |
| VDR-U02-C441 | FUNCTION MAPPING REQUIRED | product/models/res_currency.py:18-23 | action_archive | FACT | always | — | Archiving a currency archives pricelists in that currency. | N-U02-326 |
| VDR-U02-C442 | FUNCTION MAPPING REQUIRED | product/models/product_template.py:828-833 | product.dynamic_variant_limit | FACT | always | — | Variant generation limit from ir.config_parameter product.dynamic_variant_limit (default 1000). | N-U02-325 |
| VDR-U02-C443 | FUNCTION MAPPING REQUIRED | analytic/models/ir_config_parameter.py:11-28 | analytic.project_plan | FACT | always | — | System parameter analytic.project_plan is guarded on write. | N-U02-325 |
| VDR-U02-C444 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:309-321 | res.partner.property_product_pricelist | FACT | always | — | Fallback partner pricelists are read from config parameters res.partner.property_product_pricelist[_company]. | N-U02-325 |
| VDR-U02-C445 | FUNCTION MAPPING REQUIRED | stock/models/product.py:1412-1413 | stock.propagate_uom | FACT | module stock installed | — | Config parameter stock.propagate_uom controls unit propagation in procurements. | N-U02-325 |
| VDR-U02-C446 | FUNCTION MAPPING REQUIRED | account/models/product.py:355-356 | product_name_similarity_threshold | FACT | module account installed | — | Config parameter account.product_name_similarity_threshold (default 0.9) sets product name matching on invoice import. | N-U02-325 |
| VDR-U02-C447 | FUNCTION MAPPING REQUIRED | sale_timesheet/data/sale_service_data.xml:15-17 | uom.group_uom | FACT | module sale_timesheet installed | — | sale_timesheet implies the multiple-units group for all internal users. | N-U02-328 |
| VDR-U02-C448 | FUNCTION MAPPING REQUIRED | product_matrix/data/res_groups.xml:4-6 | group_product_variant | FACT | module product_matrix installed | — | product_matrix implies the variants group for all internal users. | N-U02-328 |
| VDR-U02-C449 | FUNCTION MAPPING REQUIRED | product/models/res_config_settings.py:9-13 | group_product_pricelist | OBSERVATION | restored DB (config only) | — | DB: base.group_user implies uom.group_uom, product.group_product_variant and product.group_product_pricelist; analytic group not implied; config parameters present: product.weight_in_lbs, product.volume_in_cubic_feet, analytic.project_plan, account.product_name_similarity_threshold; none of product.dynamic_variant_limit or res.partner.property_product_pricelist* set. | N-U02-327 |
| VDR-U02-C450 | FUNCTION MAPPING REQUIRED | product/models/res_config_settings.py:9-13 | implied_group | OBSERVATION | restored DB (config only) | — | DB: 0 ir_cron rows and 0 base_automation rows owned by modules product, uom, analytic, utm, resource. | N-U02-320 |
| VDR-U02-C451 | FUNCTION MAPPING REQUIRED | product/models/product_pricelist.py:262-263 | date_end | INFERENCE | always | — | Expired rules are ignored by date filters in the rule search rather than removed, since no job exists (consequence inferred). | N-U02-329 |
| VDR-U02-C452 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | other modules | — | UNKNOWN - EVIDENCE INSUFFICIENT: crons added by other installed modules on these objects not searched. | N-U02-330 |
| VDR-U02-C453 | FUNCTION MAPPING REQUIRED | product/models/res_config_settings.py:9-13 | implied_group | INFERENCE | always | — | Features are exposed as implied-group switches in Settings, consistent with enabling advanced features only on demand (purpose inferred). | N-U02-331 |
| VDR-U02-C454 | FUNCTION MAPPING REQUIRED | product/models/res_config_settings.py:36-43 | had_group_pl | FACT | always | — | The pricelist feature has two states (group on or off) and each transition triggers creation or archiving of pricelists. | N-U02-332 |
| VDR-U02-C455 | FUNCTION MAPPING REQUIRED | utm/models/utm_mixin.py:18-23 | campaign_id | FACT | always | — | utm.mixin adds campaign_id, source_id, medium_id many2one fields. | N-U02-340 |
| VDR-U02-C456 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:36 | utm.mixin | FACT | module sale installed | — | sale.order inherits utm.mixin. | N-U02-340 |
| VDR-U02-C457 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:8 | utm.mixin | FACT | module sale installed | — | account.move inherits utm.mixin in sale. | N-U02-340 |
| VDR-U02-C458 | FUNCTION MAPPING REQUIRED | utm/models/utm_mixin.py:25-46 | sale_salesman | FACT | always | — | default_get reads cookies for tracker values except for non-superuser sale salesmen; string values are found or created. | N-U02-341 |
| VDR-U02-C459 | FUNCTION MAPPING REQUIRED | utm/models/ir_http.py:14-22 | max_age=31 * 24 * 3600 | FACT | always | — | ir.http sets optional cookies from URL params utm_campaign/source/medium for 31 days. | N-U02-341 |
| VDR-U02-C460 | FUNCTION MAPPING REQUIRED | utm/models/utm_source.py:13-23 | UNIQUE(name) | FACT | always | — | Source name unique; 'Referral' source cannot be deleted. | N-U02-342 |
| VDR-U02-C461 | FUNCTION MAPPING REQUIRED | utm/models/utm_medium.py:19-51 | SELF_REQUIRED_UTM_MEDIUMS_REF | FACT | always | — | Medium name unique; Email, Direct, Website, X, Facebook, LinkedIn mediums cannot be deleted. | N-U02-342 |
| VDR-U02-C462 | FUNCTION MAPPING REQUIRED | utm/models/utm_campaign.py:31-53 | _get_unique_names | FACT | always | — | Campaign identifier unique and auto-suffixed; title copied to name on create. | N-U02-342 |
| VDR-U02-C463 | FUNCTION MAPPING REQUIRED | utm/models/utm_mixin.py:105-164 | _get_unique_names | FACT | always | — | Duplicate names get [n] counters via _get_unique_names. | N-U02-342 |
| VDR-U02-C464 | FUNCTION MAPPING REQUIRED | utm/models/utm_source.py:51-89 | utm.source.mixin | FACT | always | — | utm.source.mixin generates a source name from the record content (mailing, post) on create/write. | N-U02-342 |
| VDR-U02-C465 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:284-286 | ondelete='set null' | FACT | module sale installed | — | On sale.order, deleting a campaign/medium/source sets the field to null. | N-U02-343 |
| VDR-U02-C466 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:17-19 | ondelete='set null' | FACT | module sale installed | — | Same set-null behaviour on invoices. | N-U02-343 |
| VDR-U02-C467 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1433-1435 | 'campaign_id': self.campaign_id.id | FACT | module sale installed | — | _prepare_invoice copies campaign, medium and source to the invoice. | N-U02-343 |
| VDR-U02-C468 | FUNCTION MAPPING REQUIRED | sale/models/utm_campaign.py:26-40 | move.state not in ('draft', 'cancel') | FACT | module sale installed | — | invoiced_amount sums -balance of product lines of non-draft, non-cancelled invoice/refund/receipt moves of the campaign. | N-U02-344 |
| VDR-U02-C469 | FUNCTION MAPPING REQUIRED | sale/models/utm_campaign.py:18-24 | quotation_count | FACT | module sale installed | — | quotation_count counts sale orders per campaign. | N-U02-344 |
| VDR-U02-C470 | FUNCTION MAPPING REQUIRED | utm/models/utm_mixin.py:88-103 | =ilike | FACT | always | — | _find_or_create_record matches names case-insensitively (inactive included) or creates the record. | N-U02-345 |
| VDR-U02-C471 | FUNCTION MAPPING REQUIRED | resource/models/resource_calendar.py:62-118 | schedule_type | FACT | always | — | resource.calendar: attendances, company, time off, schedule type (flexible or fully fixed), two-week mode, timezone, hours per day/week, full time hours. | N-U02-346 |
| VDR-U02-C472 | FUNCTION MAPPING REQUIRED | resource/models/resource_calendar.py:854-897 | def plan_hours | FACT | always | — | plan_hours returns the datetime after consuming hours of working time forward or backward over up to 100 fortnight windows (False if not found), optionally subtracting leaves. | N-U02-346 |
| VDR-U02-C473 | FUNCTION MAPPING REQUIRED | resource/models/resource_calendar.py:899-941 | def plan_days | FACT | always | — | plan_days schedules whole working days forward or backward, optionally considering global leaves. | N-U02-346 |
| VDR-U02-C474 | FUNCTION MAPPING REQUIRED | resource/models/res_company.py:10-45 | resource_calendar_id | FACT | always | — | res.company gets resource_calendar_ids and default resource_calendar_id; a 'Standard 40 hours/week' calendar is created at company creation. | N-U02-347 |
| VDR-U02-C475 | FUNCTION MAPPING REQUIRED | resource/data/resource_data.xml:4-9 | Standard 40 hours/week | FACT | always | — | Seed: calendar 'Standard 40 hours/week' (40 full-time hours) set as the main company's default and _init_data_resource_calendar fills missing ones. | N-U02-347 |
| VDR-U02-C476 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock_rule.py:332 | relativedelta(days=int(value['supplier'].delay)) | FACT | module purchase_stock installed | — | Purchase order date = planned date minus vendor lead time in calendar days (no calendar). | N-U02-348 |
| VDR-U02-C477 | FUNCTION MAPPING REQUIRED | stock/models/stock_rule.py:215-220 | relativedelta(days=self.delay) | FACT | module stock installed | — | Push rule new date = move date + rule delay in calendar days. | N-U02-348 |
| VDR-U02-C478 | FUNCTION MAPPING REQUIRED | stock/models/stock_rule.py:333-336 | relativedelta(days=self.delay or 0) | FACT | module stock installed | — | Pull rule planned/deadline dates subtract rule delay in calendar days. | N-U02-348 |
| VDR-U02-C479 | FUNCTION MAPPING REQUIRED | sale_stock/models/sale_order_line.py:278-293 | timedelta(days= | FACT | module sale_stock installed | — | Customer lead time and company security lead are subtracted/added as plain days to deadlines and planned dates. | N-U02-348 |
| VDR-U02-C480 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:362-366 | relativedelta(days=seller.delay | FACT | module purchase installed | — | Purchase line planned date = order date + vendor delay days. | N-U02-348 |
| VDR-U02-C481 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock_rule.py:234 | days_to_purchase | FACT | module purchase_stock installed | — | Days to purchase is a company float number of days. | N-U02-348 |
| VDR-U02-C482 | FUNCTION MAPPING REQUIRED | mrp/models/mrp_workorder.py:458-461 | plan_hours | FACT | module mrp installed | — | Work order scheduling uses the work center's calendar plan_hours. | N-U02-349 |
| VDR-U02-C483 | FUNCTION MAPPING REQUIRED | mrp/models/mrp_workcenter.py:81 | resource_calendar_id | FACT | module mrp installed | — | Work centers have a resource calendar (resource mixin). | N-U02-349 |
| VDR-U02-C484 | FUNCTION MAPPING REQUIRED | resource/models/resource_calendar_leaves.py:35-51 | time_type | FACT | always | — | Time off: name, company, calendar, date_from/date_to (required), optional resource (company-wide if empty), time_type leave/other. | N-U02-350 |
| VDR-U02-C485 | FUNCTION MAPPING REQUIRED | resource/models/resource_calendar_leaves.py:75-78 | must be earlier than the end date | FACT | always | — | Constraint: start date must be before end date. | N-U02-350 |
| VDR-U02-C486 | FUNCTION MAPPING REQUIRED | resource/models/resource_calendar_leaves.py:17-33 | tz.localize(datetime.combine(today, time.min)) | FACT | always | — | Default time off covers the current day in the calendar timezone. | N-U02-350 |
| VDR-U02-C487 | FUNCTION MAPPING REQUIRED | resource/models/resource_calendar.py:123-143 | _check_overlap | FACT | always | — | Constraint on attendance_ids: no overlapping periods per week type; two-week mode needs section structure. | N-U02-351 |
| VDR-U02-C488 | FUNCTION MAPPING REQUIRED | utm/security/ir.model.access.csv:2-11 | access_utm_campaign_user | FACT | always | — | Tracker ACL: user r/w/c, system full; stage/tag read for users. | N-U02-352 |
| VDR-U02-C489 | FUNCTION MAPPING REQUIRED | resource/security/ir.model.access.csv:2-9 | access_resource_calendar_user | FACT | always | — | Calendar ACL: user read; system full. | N-U02-352 |
| VDR-U02-C490 | FUNCTION MAPPING REQUIRED | utm/models/utm_campaign.py:7-34 | utm.campaign | OBSERVATION | restored DB (config only) | — | DB: utm_campaign 1, utm_medium 11, utm_source 13, utm_stage 1, utm_tag 1; resource_calendar 1 (15 attendance rows), resource_resource 1, resource_calendar_leaves 0; company default calendar set. | N-U02-352 |
| VDR-U02-C491 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:284-286 | campaign_id | OBSERVATION | restored DB (config only) | — | DB: no sale orders or invoices exist, so tracker propagation cannot be observed. | N-U02-353 |
| VDR-U02-C492 | FUNCTION MAPPING REQUIRED | resource/models/resource_calendar.py:854-860 | compute_leaves | FACT | always | — | plan_hours default compute_leaves is False (global leaves ignored unless requested). | N-U02-354 |
| VDR-U02-C493 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | other consumers of calendars | — | UNKNOWN - EVIDENCE INSUFFICIENT: consumption of working calendars by employee, time-off and project functions (outside this unit). | N-U02-355 |
| VDR-U02-C494 | FUNCTION MAPPING REQUIRED | utm/models/utm_mixin.py:18-23 | Campaign | INFERENCE | always | — | Campaign, source and medium tags exist to track marketing effort (purpose inferred from help texts); calendars exist to schedule resources. | N-U02-356 |
