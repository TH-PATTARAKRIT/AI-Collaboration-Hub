# U170 — Stock Put-Away Rules: Warehouse Location Assignment
**Unit:** U170 | **Group:** G06 | **Priority:** P2 | **Status:** NOT_STUDIED → STUDIED
**Source tree:** Odoo 19.0 Community (odoo-19.0.post20260921) — READ-ONLY

---

## SOURCE FILES EXAMINED

| File | Purpose |
|------|---------|
| `odoo/addons/stock/models/product_strategy.py` | `stock.putaway.rule` model definition + `_get_putaway_location()` |
| `odoo/addons/stock/models/stock_location.py` | `stock.location` — `putaway_rule_ids`, `storage_category_id`, `_get_putaway_strategy()`, `_check_can_be_used()` |
| `odoo/addons/stock/models/stock_move_line.py` | `_apply_putaway_strategy()`, `_onchange_putaway_location()` |
| `odoo/addons/stock/models/stock_storage_category.py` | `stock.storage.category` + `stock.storage.category.capacity` |
| `odoo/addons/stock/models/stock_package.py` | `stock.package` — `package_type_id` field |

---

## CLAIM TABLE (18 claims)

| # | Claim | Source File | Key Symbol | Evidence Strength | Notes |
|---|-------|-------------|-----------|-------------------|-------|
| C01 | `stock.putaway.rule` is defined in `product_strategy.py`, _order = `'sequence,product_id'` | product_strategy.py:17–18 | `_name = 'stock.putaway.rule'`, `_order = 'sequence,product_id'` | CONFIRMED | Model name and default DB ordering |
| C02 | Core fields: `location_in_id` (M2O stock.location, required), `location_out_id` (M2O stock.location, required, domain child_of location_in_id), `product_id` (M2O product.product), `category_id` (M2O product.category), `sequence` (Integer) | product_strategy.py:43–59 | Fields declaration block | CONFIRMED | All five scope fields present |
| C03 | `sequence` field labeled "Priority"; help text: "Give to the more specialized category, a higher priority to have them in top of the list." Lower integer = earlier in ordered list | product_strategy.py:59 | `_order = 'sequence,product_id'` | CONFIRMED | DB order ascending by sequence; smaller number wins |
| C04 | `putaway_rule_ids` is a `One2many('stock.putaway.rule', 'location_in_id', 'Putaway Rules')` on `stock.location` — not named `putaway_strategy_ids` | stock_location.py:78 | `putaway_rule_ids` field | CONFIRMED | Field name is `putaway_rule_ids`, inverse key `location_in_id` |
| C05 | `_get_putaway_strategy()` on `stock.location`: filters `putaway_rule_ids` by product match OR no-product, category/parent-category match OR no-category, package_type match OR no-package-type | stock_location.py:319–322 | lambda filter block | CONFIRMED | Three-way optional filter |
| C06 | After filtering, rules are **re-sorted** in descending priority order: package_type_ids present > product_id present > exact category match > any category match; this overrides DB `sequence` ordering during selection | stock_location.py:324–328 | `.sorted(lambda rule: (bool(rule.package_type_ids), bool(rule.product_id), bool(rule.category_id == categs[:1]), bool(rule.category_id)), reverse=True)` | CONFIRMED | Python-side sort takes precedence over `sequence` order |
| C07 | Best-match selection: product-specific rule beats category rule; exact-category rule beats parent-category fallback; package-type rule beats product/category rule | stock_location.py:324–328 | Sorted tuple logic | CONFIRMED | Specificity hierarchy explicit |
| C08 | `_get_putaway_location()` on the putaway rules recordset: if `storage_category_id` is absent on rule, immediately validates the `location_out_id` via `_check_can_be_used()` and returns if usable | product_strategy.py:150–155 | `if not putaway_rule.storage_category_id:` block | CONFIRMED | Short-circuit path for simple rules |
| C09 | `_get_putaway_location()` — `sublocation` field supports 3 modes: `'no'` (use `location_out_id` directly), `'last_used'` (find last done move-line destination), `'closest_location'` (use storage-category child scan) | product_strategy.py:69–73, 144–146 | `sublocation` Selection + usage in `_get_putaway_location` | CONFIRMED | Sublocation behavior encoded on rule |
| C10 | `package_type_ids` is a M2M to `stock.package.type` on `stock.putaway.rule`; when a move line or package is incoming, the package's `package_type_id` is extracted and matched against `package_type_ids` | product_strategy.py:63, 135–139 | `package_type_ids` field; `_get_putaway_location()` package_type extraction | CONFIRMED | Package type directly influences rule selection |
| C11 | `storage_category_id` on `stock.location` (M2O to `stock.storage.category`, check_company, indexed) gates capacity checks in `_check_can_be_used()` | stock_location.py:86, 418–462 | `storage_category_id` + `_check_can_be_used()` | CONFIRMED | Storage category on location enforces constraints |
| C12 | `stock.storage.category` has `max_weight` (Float), `allow_new_product` (Selection: empty/same/mixed), `product_capacity_ids` and `package_capacity_ids` (computed from `capacity_ids`) | stock_storage_category.py:13–20 | Model fields | CONFIRMED | Three-axis constraint: weight, product-mix, qty capacity |
| C13 | `_check_can_be_used()` enforces: (a) `allow_new_product='empty'` → reject if any positive quant exists; (b) `allow_new_product='same'` → reject if any quant of different product; (c) weight check using `forecast_weight + incoming weight <= max_weight`; (d) package/product capacity count check | stock_location.py:426–461 | `_check_can_be_used()` body | CONFIRMED | Full enforcement logic |
| C14 | `company_id` on `stock.putaway.rule` is required, defaults to `env.company`, and `_check_company_auto = True` — company isolation is automatic; changing company after creation raises `UserError` | product_strategy.py:20, 60–62, 107–112 | `_check_company_auto`, `company_id` field, `write()` guard | CONFIRMED | Multi-company isolation enforced |
| C15 | `stock.storage.category` has `company_id` (M2O, optional) — can be shared across companies when left empty | stock_storage_category.py:22 | `company_id` field on storage category | CONFIRMED | Category can be company-agnostic |
| C16 | `_apply_putaway_strategy()` on `stock.move.line` handles three cases: (a) packaged move with typed package → single best_loc for all smls; (b) untyped package → per-sml strategy, collapses if >1 location used; (c) no package → per-sml strategy | stock_move_line.py:262–293 | `_apply_putaway_strategy()` | CONFIRMED | Move line is entry point for applying rules during reception |
| C17 | Putaway is skipped entirely when context key `avoid_putaway_rules` is set | stock_move_line.py:263 | `if self.env.context.get('avoid_putaway_rules'): return` | CONFIRMED | Escape hatch for programmatic bypass |
| C18 | `_get_putaway_strategy()` fallback: if no rule matches, returns `locations[0]` when parent `usage='view'`, else returns `self` (the destination location unchanged) | stock_location.py:373–375 | `if not putaway_location:` block | CONFIRMED | Graceful no-op fallback |

---

## KEY ARCHITECTURAL NOTES

### Rule Resolution Priority (descending):
1. Rule with matching `package_type_ids`
2. Rule with matching `product_id`
3. Rule with matching exact `category_id`
4. Rule with matching parent `category_id`
5. Fallback: original destination location

### Within same priority tier, `sequence` (Integer, ascending) breaks ties via DB order.

### Capacity Gate (`_check_can_be_used`):
- Only fires when target location has `storage_category_id` set
- Checks: product-mix policy, weight, qty capacity (product-based or package-count-based)

### Package Type Integration:
- `package_type_ids` M2M on rule allows filtering by package type
- During `_get_putaway_location()`, already-stored packages of same type in child locations are prioritized (consolidation logic at lines 163–173)

---

## FILES — ABSOLUTE PATHS

- `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/stock/models/product_strategy.py`
- `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/stock/models/stock_location.py`
- `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/stock/models/stock_move_line.py`
- `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/stock/models/stock_storage_category.py`
