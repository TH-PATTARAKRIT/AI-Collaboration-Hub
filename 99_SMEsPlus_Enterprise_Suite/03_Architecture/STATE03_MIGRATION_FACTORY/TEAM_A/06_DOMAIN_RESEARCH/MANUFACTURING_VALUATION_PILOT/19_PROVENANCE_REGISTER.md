> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) | Evidence Annex Index

# 19 — PROVENANCE REGISTER (Gx7)

Retrieved via `WebSearch` on **2026-09-28**; same egress constraint as all prior Gx.

| Evidence ID | URL | Tier | Used for |
|---|---|---|---|
| EV-MFG-01 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/basic_setup/work_in_progress.html` | Official documentation | MFG-F01, F02, F03 (WIP mechanism, account configuration, manual post/reverse) |
| EV-MFG-02 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/basic_setup/mo_costs.html` | Official documentation | MFG-F04 (MO cost computation) |
| EV-MFG-03 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/inventory_valuation/operations_valuation.html` | Official documentation | MFG-F01 (component consumption valuation) |
| EV-MFG-04 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/basic_setup/bill_configuration.html` | Official documentation | MFG-F04 (BOM structure, referenced not detailed) |
| EV-MFG-05 | `https://www.odoo.com/forum/help-1/why-does-odoo-system-generate-journal-entry-revaluation-of-whmoxxx-negative-inventory-mo-for-manufacture-order-232342` | **Community forum, opened 2026-09-29 (via WebSearch synthesis)** | MFG-F05 — describes pre-19 "Revaluation of WH/MO/XXX" behavior |
| EV-MFG-06 | `https://www.erpgap.com/blog/odoo-19-stock-valuation-use-cases/` | **Odoo-partner blog, not official documentation** | MFG-F05 — states Odoo 19 books raw-material cost only at vendor-bill time, no automatic revaluation entry |

## Evidence-tier disclosure

EV-MFG-05 and EV-MFG-06 are both sub-official-documentation tier (V1) and **disagree by Odoo version** — recorded as an open tension per `06_BUSINESS_RULE_REGISTER.md` MFG-F05, not silently reconciled. Neither is treated as a documentation-tier (V2) finding; an official Odoo 19 documentation page or AWT runtime confirmation is still required to close `GAP-MFG-01` fully.
