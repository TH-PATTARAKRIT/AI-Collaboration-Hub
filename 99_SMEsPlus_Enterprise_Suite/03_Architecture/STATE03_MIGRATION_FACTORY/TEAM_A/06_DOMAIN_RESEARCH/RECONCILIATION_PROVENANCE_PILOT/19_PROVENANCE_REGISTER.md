> Domain: RECONCILIATION_PROVENANCE_PILOT (Gx10) | Evidence Annex Index

# 19 — PROVENANCE REGISTER (Gx10)

Retrieved via `WebSearch` on **2026-09-28**; same egress constraint as all prior Gx.

| Evidence ID | URL | Used for |
|---|---|---|
| EV-RCN-01 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/warehouses_storage/reporting/stock.html` | RCN-F01 (Stock report, Moves History) |
| EV-RCN-02 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/count_products.html` | RCN-F01 (adjustment → Moves History link, backdating field, dual chatter — shared with Gx4 EV-IAV-01) |
| EV-RCN-03 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/inventory_valuation.html` | RCN-F03 (Total Value click-through, incoming-quantity origin tracking) |
| EV-RCN-04 | `https://www.odoo.com/documentation/19.0/applications/finance/accounting/bank/reconciliation.html` | RCN-F04 (Bank Reconciliation, explicitly Not Applicable to this scenario) |
| EV-RCN-05 | `https://www.odoo.com/documentation/19.0/applications/finance/accounting/bank/reconciliation_models.html` | RCN-F04 (Reconciliation Models, same Not Applicable scope) |
| EV-RCN-SRC-01 | Odoo 19.0.post20260921 Community source, read-only, `stock_account`/`account` modules (exact file+line in `STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md` round 2 `R9`) | **Source-code-tier lead**, retrieved 2026-09-30 by Boss's own local Claude Code session, incorporated here by this session (never read directly by it) | `GAP-RCN-01` corroborating evidence — move-level journal-entry reference confirmed, scope limit to bill/invoice-line-originated entries disclosed |
| EV-RCN-SRC-02 | Same source tree, `stock_account` lot-valuation modules (exact file+line in Handoff round 2 `R9`) | **Source-code-tier lead**, same provenance as `EV-RCN-SRC-01` | `GAP-RCN-02` corroborating evidence — AVCO/Standard/FIFO lot-cost support confirmed |

## Evidence-tier disclosure (source/dump round, 2026-09-30)

`EV-RCN-SRC-01`/`02` are source-code-tier but explicitly self-labeled by the worker as "research leads," a step below the round-1 `D-01`–`D-14` items used elsewhere in this Deep Study (no Odoo unit-test corroboration for these two; the scope-limit finding is `INFER`, not directly observed). This session did not read the source itself and preserves that same conservative reading. `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET` applies; the actual test database carries ~696 non-Community tables.
