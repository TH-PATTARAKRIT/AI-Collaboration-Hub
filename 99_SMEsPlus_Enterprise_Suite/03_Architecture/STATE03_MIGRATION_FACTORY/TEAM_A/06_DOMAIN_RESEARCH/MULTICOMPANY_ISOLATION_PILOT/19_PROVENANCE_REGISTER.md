> Domain: MULTICOMPANY_ISOLATION_PILOT (Gx9) | Evidence Annex Index

# 19 — PROVENANCE REGISTER (Gx9)

Retrieved via `WebSearch` on **2026-09-28**; same egress constraint as all prior Gx.

| Evidence ID | URL | Tier | Used for |
|---|---|---|---|
| EV-MCT-01 | `https://www.odoo.com/documentation/19.0/applications/general/companies/multi_company.html` | Official documentation | MCT-F02, F03, F04 (inter-company transactions, shared accounts, consolidation) |
| EV-MCT-02 | `https://www.odoo.com/documentation/19.0/applications/finance/accounting/get_started/consolidation.html` | Official documentation | MCT-F04 (consolidation detail) |
| EV-MCT-03 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses.html` | Official documentation | MCT-F01 (warehouse Company field) |
| EV-MCT-04 | `https://www.odoo.com/forum/help-1/how-to-assign-a-user-to-a-specific-warehouse-208699` | **Community forum, corroborating evidence for an absence** | MCT-F05 (used to evidence that a native solution is NOT documented/available, not to describe a positive mechanism) |
| EV-MCT-05 | Marketplace app listings (`warehouse_access_control`, `cr_warehouse_stock_restrictions`, `bi_stock_access_rules`) | **Third-party product listings — corroborating, not authoritative** | MCT-F05 (existence of paid solutions corroborates the native gap) |

| EV-MCT-SRC-01 | Odoo 19.0.post20260921 Community source, read-only, `stock`/`stock_account`/`product` modules (exact file+line in `STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md` round 2 `R4`) | **Source-code-tier lead**, retrieved 2026-09-30 by Boss's own local Claude Code session, incorporated here by this session (never read directly by it) | `GAP-MCT-01` corroborating (not closing) evidence — no cross-company value-copy mechanism found, per-company cost field confirmed |
| EV-MCT-SRC-02 | Same source tree, `stock` security XML + `stock_account` security XML (exact file+line in Handoff round 2 `R8`) | **Source-code-tier lead**, same provenance as `EV-MCT-SRC-01` | `GAP-MCT-02` corroborating evidence — confirms, at Community-source tier, the company-only scope of stock security rules |

## Evidence-tier disclosure

MCT-F05's finding is unusual in this Deep Study: it is a documented **absence** (no native single-field solution), evidenced by the *existence of a market* for third-party fixes plus a direct community question, rather than by an official documentation page describing a mechanism. This is disclosed explicitly rather than presented with the same confidence as a positive documented feature. `EV-MCT-SRC-01`/`02` are source-code-tier but explicitly self-labeled by the worker as "research leads," a step below the round-1 `D-01`–`D-14` items (no Odoo unit-test corroboration; several sub-findings are `INFER`/`ABSENCE`) — this session did not read the source itself and preserves that same conservative reading. `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET` applies; the actual test database carries ~696 non-Community tables.
