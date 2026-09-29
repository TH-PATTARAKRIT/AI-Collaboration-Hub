> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Evidence Annex Index

# 19 — PROVENANCE REGISTER

Retrieved via `WebSearch` (search-engine-mediated; direct fetch blocked, same as every prior Deep Study unit) on **2026-09-29**.

| Evidence ID | URL | Tier | Used for |
|---|---|---|---|
| EV-BRP-01 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/basic_setup/bill_configuration.html` | Official documentation | BRP-F01 (BoM Type field, three values) |
| EV-BRP-02 | `https://octurasolutions.com/resources/odoo-19-bill-of-materials-multi-level-bom-kits-and-phantom-assemblies` | Odoo-partner blog | BRP-F01/F02 (corroborating context, not primary) |
| EV-BRP-03 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/advanced_configuration/kit_shipping.html` | Official documentation | BRP-F02 (Kit BoM, "Kit Value Does Not Change" rule) |
| EV-BRP-04 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/subcontracting.html` | Official documentation | BRP-F03 (Subcontracting BoM type, feature toggle) |
| EV-BRP-05 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/subcontracting/subcontracting_basic.html` | Official documentation | BRP-F03 (Subcontracting Location = Internal Location, valuation non-impact rule — the pilot's key finding) |
| EV-BRP-06 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/advanced_configuration/using_work_centers.html` | Official documentation | BRP-F04 (Work Center: Cost per hour, Allowed Employees) |
| EV-BRP-07 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/basic_setup/mo_costs.html` (revisited, cross-referenced with Gx7's `EV-MFG-02`) | Official documentation | BRP-F05 (Routing Operations required on a work order; expected duration) |
| EV-BRP-08 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/subcontracting.html` (revisited) + `https://www.erpgap.com/blog/odoo-19-stock-valuation-use-cases/` | **Mixed: official documentation + Odoo-partner blog** (search-result attribution blended the two this round; not separately re-confirmed against the bare official page alone) | BRP-F03 (`GAP-BRP-03` closure — subcontractor fee capture via vendor-bill posting, Finished Goods Valuation Account debit) |
| EV-BRP-09 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/reordering_rules.html` | Official documentation | BRP-F06 (min/max, automatic vs. manual replenishment) |
| EV-BRP-10 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/workflows/use_mps.html` | Official documentation | BRP-F07 (MPS scope, explicit incompatibility with Reordering Rules) |
| EV-BRP-11 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/workflows/byproducts.html` | Official documentation | BRP-F08 (By-Products feature toggle, BOM tab, Produced in Operation field) |
| EV-BRP-12 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/advanced_configuration/sub_assemblies.html` | Official documentation | BRP-F09 (multilevel BOM, recursive resolution, BOM Overview hierarchy) |
| EV-BRP-13 | `https://apps.odoo.com/apps/modules/12.0/mfg_byproduct_cost` (third-party app listing, describing the native-core default behavior it patches) | **Third-party marketplace listing — not official documentation** | `GAP-BRP-09` (`BRP-F08` cost-allocation default): "by default, no material cost is allocated to the by-products manufactured therefore full production cost is charged to main finished goods" — cross-checked, the official `mo_costs.html` (`EV-BRP-11`'s own source page, re-queried this round) does **not** itself state this; the claim is corroborated only at third-party-listing tier |
| EV-BRP-14 | `https://www.odoo.com/forum/help-1/calculate-production-cost-enterprise-v12-deduct-cost-for-by-product-153907` (community forum, pre-19 version, V12) | Community forum — **pre-19, not version-confirmed for 19.0** | `GAP-BRP-09`: independent corroboration of the same "no automatic by-product cost deduction" behavior, from a different source and an earlier version — consistent with `EV-BRP-13`, not a second confirmation of the same source |

## Clean-room boundary

Same as all prior Gx/pilots — evidence annex only, not to be copied verbatim into a future Clean-Room Neutral Pack. No Odoo source code, schema, or ORM identifier was read or recorded this round — documentation-tier only.
