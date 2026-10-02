# U223 — Pricelist Model, Rule Types, Price Computation — Neutral Knowledge
**Unit**: U223 | **Module**: product pricelist | **Gate**: GREEN
**Date**: 2026-10-02

---

## VDR Claims Table

9-column format. Neutral-ref: no snake_case, no dotted names, no backticks, no file extensions, no code keywords.

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|----------|-------------|---------|--------|-------|-----------|-------|---------------------|-------------|
| C001 | ProductPricelist.fields | product_pricelist.py:9-14 | model declaration | STRUCTURAL | always | BASELINE | The pricelist model inherits from the mail thread and activity mixin mixins, and is ordered by sequence, then identifier, then name | Pricelist model definition and record ordering |
| C002 | ProductPricelist.currency_id | product_pricelist.py:36-41 | field definition | FIELD | always | BASELINE | The currency field is required and defaults to the current company currency; the display name includes the currency name in parentheses | Pricelist currency requirement and display |
| C003 | ProductPricelistItem.applied_on | product_pricelist_item.py:51-61 | field definition | FIELD | always | BASELINE | Rule scope has four values: all products (global), product category, product template, and product variant; the numeric prefix in the selection key determines evaluation priority | Rule scope selection values and priority encoding |
| C004 | ProductPricelistItem.sort_order | product_pricelist_item.py:11 | model order | STRUCTURAL | always | BASELINE | Rules are sorted by scope ascending (variant first, global last), then minimum quantity descending (largest break first), then category identifier descending, then rule identifier descending | Rule evaluation sort order |
| C005 | ProductPricelistItem.compute_price | product_pricelist_item.py:106-114 | field definition | FIELD | always | BASELINE | Pricing method has three values: fixed price, discount percentage on a base price, and formula (discount plus surcharge plus margin clamps) | Pricing method selection values |
| C006 | ProductPricelistItem.base | product_pricelist_item.py:91-103 | field definition | FIELD | compute_price in percentage or formula | BASELINE | The base price for discount and formula rules can be the product sales price, the product cost price, or the result of another pricelist | Base price source selection values |
| C007 | _compute_price_rule.algorithm | product_pricelist.py:207-234 | method body | LOGIC | always | BASELINE | The method iterates products; for each product it walks the sorted rule list and stops at the first rule that passes the applicability check; a product with no matching rule receives the sales price as fallback | Rule matching algorithm and first-match semantics |
| C008 | _get_applicable_rules_domain.date | product_pricelist.py:262-263 | domain clause | LOGIC | date_start or date_end set | BASELINE | The date domain requires start date absent or on/before the evaluation date, AND end date absent or on/after the evaluation date; both bounds are inclusive | Date validity domain inclusivity |
| C009 | _get_applicable_rules_domain.category | product_pricelist.py:259 | domain clause | LOGIC | rule has category | BASELINE | Category matching uses the parent-of operator, so a rule on a parent category also applies to products in any child category | Hierarchical category matching |
| C010 | _is_applicable_for.min_quantity | product_pricelist_item.py:541 | method body | LOGIC | min_quantity > 0 | BASELINE | A rule with minimum quantity is skipped if the requested quantity expressed in the product default unit of measure is strictly less than the minimum | Minimum quantity comparison in product UoM |
| C011 | _compute_price.fixed | product_pricelist_item.py:601-602 | method body | LOGIC | compute_price=fixed | BASELINE | For fixed-price rules the fixed price field is converted from product UoM to the requested UoM; no currency conversion is applied because the fixed price is already in the pricelist currency | Fixed price UoM conversion without currency conversion |
| C012 | _compute_price.percentage | product_pricelist_item.py:603-605 | method body | LOGIC | compute_price=percentage | BASELINE | The percentage rule subtracts the discount percentage from the base price; a negative percent price applies a markup instead of a discount | Percentage discount applied to base price |
| C013 | _compute_price.formula | product_pricelist_item.py:606-622 | method body | LOGIC | compute_price=formula | BASELINE | The formula rule applies a discount percentage, optional rounding, optional fixed surcharge, and optional minimum and maximum margin clamps in that order | Formula rule computation sequence |
| C014 | _compute_base_price.currency | product_pricelist_item.py:656-657 | method body | LOGIC | source currency differs from pricelist currency | BASELINE | When the product price currency or the chained pricelist currency differs from the target currency, the base price is converted using the exchange rate for the evaluation date, without rounding | Base price currency conversion using dated rate |
| C015 | _compute_base_price.standard_price | product_pricelist_item.py:649-651 | method body | LOGIC | base=standard_price | BASELINE | When the base is cost price, the source currency is taken from the product cost currency field, not the product sales currency | Cost base uses cost currency field |
| C016 | _compute_base_price.pricelist | product_pricelist_item.py:643-648 | method body | LOGIC | base=pricelist | BASELINE | When the base is another pricelist, the method calls that pricelist price computation recursively and uses that pricelist currency as the source for subsequent conversion | Chained pricelist base with recursive price call |
| C017 | _get_partner_pricelist_multi.priority | product_pricelist.py:334-375 | method body | LOGIC | always | BASELINE | Pricelist assignment to a partner follows this priority: explicit partner-level pricelist saved as a company-dependent property; then pricelist matching the partner country group; then configuration parameter fallback; then first active pricelist | Partner pricelist assignment priority chain |
| C018 | _get_partner_pricelist_multi.feature_gate | product_pricelist.py:348-350 | method body | LOGIC | feature flag disabled | BASELINE | When the pricelist feature group is disabled in settings, the partner pricelist lookup returns an empty recordset for all partners without performing any search | Feature flag short-circuit in partner lookup |
| C019 | ResPartner.property_product_pricelist | res_partner.py:14-45 | field and inverse | FIELD | always | BASELINE | The partner pricelist field is a computed field; the inverse stores the selection to a company-dependent backing field only when the chosen pricelist differs from the country default; when it equals the default the backing field is cleared | Partner pricelist field inverse logic |
| C020 | migration.pricelist_version | product_pricelist.py (absent) | model absence | MIGRATION | v19 | BREAKING | The pricelist version model that existed in older versions is not present in version 19; time-based scoping is handled entirely by date range fields on individual pricelist rules; databases migrating from version 14 or earlier must transform version records into date-ranged rules | Pricelist version model removed in version 19 |
| C021 | migration.discount_policy | product_pricelist.py (absent) | field absence | MIGRATION | v19 | BREAKING | The discount policy field and its two values (absorb discount into unit price vs show as line discount) are not present on the pricelist model in version 19 Community; databases migrating from version 14 or 15 that carry this field must handle its absence | Discount policy field removed in version 19 Community |
| C022 | POS.pricelist_currency_constraint | pos_config.py:494-495 | constraint | CONSTRAINT | use_pricelist=True | BASELINE | Point of sale configuration enforces that every available pricelist must share the same currency as the company; a pricelist in a different currency cannot be added to the available list | POS pricelist currency uniformity constraint |
| C023 | POS.pricelist_fields | pos_config.py:139-153 | field definitions | FIELD | use_pricelist=True | BASELINE | The point of sale configuration has a default pricelist field and a many-to-many available pricelists field; a boolean toggle enables pricelist use; when disabled the default pricelist is set to false | POS pricelist configuration fields |
| C024 | _check_pricelist_recursion | product_pricelist_item.py:321-352 | constraint | CONSTRAINT | base=pricelist | BASELINE | A depth-first search constraint prevents circular chains when pricelist rules reference other pricelists as their base; an error is raised naming the cycle path | Pricelist chaining circular reference prevention |

---

## Key Findings Summary

1. **Version model gone**: The `product.pricelist.version` concept from v13/v14 is fully removed. Time-bounded rules are handled by `date_start`/`date_end` on each `product.pricelist.item` record.

2. **Discount policy gone**: The `discount_policy` field that controlled whether pricelist discounts showed as `price_unit` reduction vs SO line `discount` column is absent from v19 Community. This is a breaking migration flag for databases from v14 or earlier.

3. **First-match wins**: Rule evaluation iterates the ORM-ordered list (most-specific first) and breaks on the first applicable rule. There is no aggregation across rules.

4. **Currency conversion at base**: Currency conversion happens inside `_compute_base_price`, not at the item level; it uses the date-parameterized exchange rate without rounding.

5. **Partner pricelist is not a stored property**: `property_product_pricelist` is a computed field backed by `specific_property_product_pricelist` (company-dependent stored); setting it only persists to the backing field when the value differs from the country-group default.

6. **POS restricts currency mix**: Unlike sales orders, POS enforces all pricelists in a session share the company currency.
