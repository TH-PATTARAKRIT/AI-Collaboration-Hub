> Domain: PARTIAL_FULFILLMENT_TIMING_PILOT (Gx5) | Evidence Annex Index

# 19 — PROVENANCE REGISTER (Gx5)

Retrieved via `WebSearch` on **2026-09-28**; same egress constraint as all prior Gx.

| Evidence ID | URL | Tier | Used for |
|---|---|---|---|
| EV-PDT-01 | `https://www.odoo.com/documentation/19.0/applications/sales/sales/invoicing/invoicing_policy.html` | Official documentation | PDT-F01 (per-shipment invoicing, two-invoices-per-backorder finding) |
| EV-PDT-02 | `https://www.odoo.com/documentation/19.0/applications/finance/accounting/vendor_bills.html` | Official documentation | PDT-F02, PDT-F04 (multiple bills, Bill Reference) |
| EV-PDT-03 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/purchase/manage_deals/control_bills.html` | Official documentation | PDT-F02 (Bill Control Policy, cross-referenced with Gx1 GRV-F06) |
| EV-PDT-04 | `https://www.odoo.com/forum/help-1/why-does-odoo-version-19-allow-me-to-create-a-bill-for-a-purchase-order-without-having-received-the-product-knowing-that-i-have-the-purchase-invoice-policy-set-to-the-received-quantity-291885` | **Community forum — lower evidence tier, explicitly flagged** | PDT-F03 (bill-before-receipt anomaly) |

## Evidence-tier disclosure

EV-PDT-04 is **not** official Odoo documentation. It is included because it is a specific, on-topic, dated community report that directly corroborates an independently-derived finding from official documentation (Gx1 `CQS-GRV-04`) — not because forum posts are treated as equivalent evidence to vendor documentation. Its status remains `Community-Reported / Unverified` throughout this pilot's registers.
