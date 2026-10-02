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

| EV-MFG-07 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/inventory_valuation/operations_valuation.html` | **Official documentation** | MFG-F05 — general (not MO-specific) negative-stock valuation rule: last-known-cost + Stock Variation account |
| EV-MFG-SRC-01 | Odoo 19.0.post20260921 Community source, read-only, `stock_account`/`purchase_stock`/`account`/`mrp_account` modules (exact file+line in `SRC_GAP-MFG-01_VALUATION_TIMING_SOURCE_CHECK_EVIDENCE.md`) | **Source-code-tier**, retrieved 2026-09-30 by Boss's own local Claude Code session, incorporated here by this session (never read directly by it — see `SRC_GAP-MFG-01_VALUATION_TIMING_SOURCE_CHECK_BUSINESS_SUMMARY.md`) | `GAP-MFG-01` corroborating (not closing) evidence, and the corrected Step 1/3/4 characterization of the cross-Gx valuation-timing chain — see `STATE03_VALUATION_TIMING_CROSS_GX_CONTRADICTION_MATRIX.md` |
| EV-MFG-SRC-02 | Same source tree, `mrp`/`mrp_account`/`l10n_th` modules + Odoo's own bundled unit tests (exact file+line in `SRC_GAPS_MFG-02-03-04-05_EVIDENCE.md`) | **Source-code-tier**, same provenance as `EV-MFG-SRC-01` | `GAP-MFG-02`/`03`/`04`/`05` corroborating (not closing) evidence |
| EV-MFG-SRC-03 | `TEAM_A/04_EVIDENCE_PACKS/SOURCE_MAP_CANDIDATE/MODULE_mrp_account.md` (`mrp_account/models/mrp_production.py`, `mrp_account/wizard/mrp_wip_accounting.py`, `mrp_account/models/mrp_workcenter.py`, Odoo's own bundled tests) | **Source-code-tier, S2-CANDIDATE** — a per-module structural/trace record from the worker's broader 300-module source-map pass, retrieved 2026-09-30, incorporated here by this session (never read directly by it) | `GAP-MFG-02`/`04`/`05` independent re-verification and refinement — surfaces the Standard-cost unoffset-labour-balance risk, the WIP wizard's current-vs-consumption-cost mismatch, and the order-company-vs-user-company multi-company nuance; also corroborates `GAP-BRP-09`'s Cost Share mechanism with exact test citations |

## Evidence-tier disclosure

EV-MFG-05 and EV-MFG-06 are both sub-official-documentation tier (V1) and **disagree by Odoo version** — recorded as an open tension per `06_BUSINESS_RULE_REGISTER.md` MFG-F05, not silently reconciled. Neither is treated as a documentation-tier (V2) finding; an official Odoo 19 documentation page or AWT runtime confirmation is still required to close `GAP-MFG-01` fully. `EV-MFG-SRC-01`/`02` are source-code-tier — strictly higher confidence than V1/V2 for what they directly evidence, but this session did not read the source itself (relayed via a separate local session's own Clean-Room-scoped work, per `STATE03_ODOO_CLEAN_ROOM_SOURCE_ACCESS_PROBE.md`) and the DB-schema cross-check found the actual test/pilot database extends beyond vanilla Community (~696 non-Community tables) — so these findings describe Community-core behavior, not necessarily the full behavior of any live/customized deployment.
