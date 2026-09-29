> Domain: SHARED_MASTER_DATA_PILOT | Evidence Annex Index

# 19 — PROVENANCE REGISTER

Retrieved via `WebSearch` (search-engine-mediated; direct fetch blocked, same constraint as every prior Deep Study unit) on **2026-09-29**.

| Evidence ID | URL | Tier | Used for |
|---|---|---|---|
| EV-SMD-01 | `https://www.odoo.com/documentation/19.0/applications/essentials/contacts.html` | Official documentation | `SMD-F01` (Individual/Company contact types, child contacts, typed addresses) |
| EV-SMD-02 | `https://www.odoo.com/documentation/19.0/applications/sales/sales/products_prices/products/variants.html` | Official documentation | `SMD-F02` (Product Template/Variant, Attributes/Values, Instantly/Dynamically creation modes) |
| EV-SMD-03 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/product_management/configure/uom.html` | Official documentation | `SMD-F03` (UoM Category, Ratio-to-reference-unit conversion mechanism) |
| EV-SMD-04 | `https://www.odoo.com/documentation/19.0/applications/general/users/access_rights.html` | Official documentation | `SMD-F04` (Groups, additive access, Roles as Group bundles) |
| EV-SMD-05 | `https://www.odoo.com/documentation/19.0/developer/tutorials/restrict_data_access.html` | Official documentation | `GAP-SMD-04` closure: model-level access (Groups) and record-level rules (`ir.rule`, including multi-company rules) are two distinct, composable layers — global rules (no group) AND-combine as a hard floor; group-carrying rules OR-combine among themselves. Multi-company rules are typically global, so they apply as an unconditional filter on top of whatever a Group already permits |

## Clean-room boundary

Same as all prior Gx/pilots — evidence annex only, not to be copied verbatim into a future Clean-Room Neutral Pack. No Odoo source code, schema, or ORM identifier was read or recorded this round — documentation-tier only.
