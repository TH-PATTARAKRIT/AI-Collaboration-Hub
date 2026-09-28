> Domain: GOODS_RECEIPT_VALIDATION_PILOT | Restricted Reference Evidence Annex Index (Master Prompt §10.1) | Documentation-Tier

# 19 — PROVENANCE REGISTER (Evidence Annex Index)

All entries below are **public vendor documentation URLs**, retrieved via WebSearch (search-engine-mediated fetch; direct WebFetch to `odoo.com` was blocked by this container's network egress policy — see GAP-GRV-08 in `22_UNKNOWN_AND_GAPS.md`) on **2026-09-28**, during this session.

| Evidence ID | URL | Used for |
|---|---|---|
| EV-GRV-01 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step.html` | GRV-F01, GRV-F02 (one-step receipt) |
| EV-GRV-02 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps.html` | GRV-F01, GRV-F02 (two-step receipt) |
| EV-GRV-03 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_three_steps.html` | GRV-F01, GRV-F02 (three-step receipt) |
| EV-GRV-04 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/inventory_valuation/cheat_sheet.html` | GRV-F04 (valuation cheat sheet — search-summary only, direct fetch blocked) |
| EV-GRV-05 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/product_management/inventory_valuation/inventory_valuation_config.html` | GRV-F04 (automatic vs manual valuation) |
| EV-GRV-06 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/product_management/inventory_valuation/landed_costs.html` | GRV-F05 (landed costs) |
| EV-GRV-07 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/purchase/manage_deals/control_bills.html` | GRV-F06 (bill control policies, 3-way matching) |
| EV-GRV-08 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/purchase/manage_deals/manage.html` | GRV-F06 (manage vendor bills) |
| EV-GRV-09 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing/workflows/manufacturing_backorders.html` | GRV-F03 (backorder concept, adjacent manufacturing domain — analogy only, not directly cited as inventory-receipt evidence) |

## Retrieval method disclosure

Retrieval was via the `WebSearch` tool (Anthropic-mediated search + summarization), not a direct page fetch performed by this session — direct `WebFetch` calls to `www.odoo.com` returned `EGRESS_BLOCKED` from this container's network proxy. This means the content above is a **search-engine-mediated synthesis of the cited pages**, not a verbatim page read. Where higher-confidence verification is required (e.g. exact GL account names for GRV-F04), a direct fetch or manual documentation read is required — recorded as `SOURCE VERIFICATION REQUIRED` in the relevant rows of `06_BUSINESS_RULE_REGISTER.md`.

## Clean-room boundary

This annex may reference vendor documentation URLs and vendor terminology (as Team A evidence). It must not be copied verbatim into a future Clean-Room Neutral Function Knowledge Pack (Master Prompt §10.2) — that sanitization pass is deferred to Phase B.
