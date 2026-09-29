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
| EV-SMD-06 | Odoo 19.0.post20260921 Community source, read-only, path `odoo/addons/base/models/ir_rule.py` (exact lines cited in `06_BUSINESS_RULE_REGISTER.md`) and `addons/uom/models/uom_uom.py` (lines 41, 44, 159, 218-230) | **Source-code-tier — direct verification, not documentation-derived.** Retrieved 2026-09-30 by Boss's own local Claude Code session, running on Boss's own Mac against the actual Odoo Community source tree at `.../SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/` (Clean-Room read-only; `addons_Extramodule`, `Extra_Module_scgl`, `addons_smeplus` explicitly excluded and not opened). This session (cloud) did not read the source directly — it received only the business-language findings and file+line citations relayed by Boss, never raw source code | `GAP-SMD-04` refinement (global-AND/group-OR composition confirmed for `base`/`sale` sample; superuser/`sudo()` bypass of record rules discovered — see `06_BUSINESS_RULE_REGISTER.md`), `GAP-SMD-05` closure (no `uom.category` model exists in actual source, confirmed by full-tree search) |

## Clean-room boundary

`EV-SMD-01`–`05` are documentation-tier, retrieved by WebSearch. `EV-SMD-06` is source-code-tier, but was retrieved and summarized by a *separate, local* Claude Code session under its own Clean-Room instructions — this cloud session never read Odoo source code directly, only the neutral summary + file+line pointers relayed by Boss. No raw source code, schema dump, or SQL was pasted into this repository at any point.
