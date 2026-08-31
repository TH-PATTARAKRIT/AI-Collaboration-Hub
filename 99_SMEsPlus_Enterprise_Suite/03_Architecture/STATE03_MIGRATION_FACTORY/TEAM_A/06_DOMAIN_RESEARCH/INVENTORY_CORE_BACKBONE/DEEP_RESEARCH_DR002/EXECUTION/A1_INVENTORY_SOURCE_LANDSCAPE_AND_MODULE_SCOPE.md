# A1 — Inventory Source Landscape / Module Universe

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Build a focused Inventory source map from the larger 93,866-file source universe and classify modules by relevance | Claude (Team A, DR-002) | This artifact | 2026-08-31 | Independent Evidence Review (pending) | VERIFIED (direct listing) | Scopes A2–A13 research; does not set SMEsPlus target module count |

## Method

Direct `find`/`ls` enumeration of `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/` (1,378 top-level module folders) and `01 ACCOUNT/` (62 folders, confirmed Accounting-only, no Inventory relevance — see A0 §2). Classification below is evidence-based (folder existence + `models/` file counts), not exhaustive per-file reading — deep reading of the flagged Core/Direct-Dependency modules is reported in A3–A9.

## Classification

### Inventory Core (primary Stock Truth modules)

| Module | Models files | Role |
|---|---:|---|
| `stock` | 26 | Core Move/Move Line/Quant/Picking/Location/Warehouse/Rule/Route/Scrap engine |
| `stock_account` | 17 | Inventory ⇄ Accounting valuation interface (no `stock.valuation.layer`; value lives on `stock.move` — see A9) |
| `stock_landed_costs` | 8 | Post-receipt cost allocation into `stock.move.value` |
| `stock_picking_batch` | not read in depth | Batch/wave picking grouping — flagged for future deepening, not yet material-blocking |
| `stock_barcode` + 8 barcode-extension modules | not read in depth | Mobile/scanner UX layer over core `stock` models — UI/UX, not new business-fact ownership; **out of A1–A13 material scope**, registered for completeness |
| `stock_dropshipping` | not read in depth | GROUP A Medium#16 already flags this module's contents as an open unknown — **carried forward unresolved by this pass**, see A14 |
| `stock_intrastat`, `stock_sms`, `stock_maintenance`, `stock_fleet`, `stock_enterprise` | not read | Peripheral/reporting/notification extensions — out of scope, no Stock Truth ownership evidenced or expected |

### Product / UOM / Location dependency (Shared Business Domain, per Learning Matrix Wave 1)

| Module | Role |
|---|---|
| `product` | Base `product.template`/`product.product`/`product.category`/`product.uom` — Inventory-relevant fields (`is_storable`, `tracking`, costing) are added by `stock`/`stock_account`, **not** present in base `product` (see A5) |
| `uom` | `uom.uom` self-referential conversion tree — no `uom.category` model exists (deviation from textbook Odoo, see A5) |

### Sales integration

| Module | Role |
|---|---|
| `sale_stock` | Sale ↔ delivery handoff (`stock.rule.run()` dispatch, `delivery_status`, return eligibility) |
| `sale_mrp`, `sale_purchase_stock`, `sale_project_stock*` | Not read in depth this pass — secondary/compound integrations, registered, not material-blocking |

### Purchase integration

| Module | Role |
|---|---|
| `purchase_stock` | Purchase ↔ receipt handoff (`_create_picking`, over/under-receipt, `_run_buy`) |
| `purchase_mrp`, `purchase_requisition` | Not read in depth — `purchase.requisition` already reconciled by GROUP A (R2: not the tendering table; real tendering is `purchase.order.alternative_po_ids`) |

### Manufacturing integration

| Module | Role |
|---|---|
| `mrp` | Raw-material consumption / finished-goods receipt / `mrp.production` state machine, BOM explosion |
| 18 `mrp_*` extensions (`mrp_subcontracting*`, `mrp_workorder*`, `mrp_landed_costs`, `mrp_maintenance`, `mrp_mps`, `mrp_plm`, `mrp_repair`, `mrp_product_expiry`) | Not read in depth — registered, out of this pass's material scope per DR-002 §8 ("Where does Manufacturing touch Inventory" answered at the `mrp` core level; subcontracting/workorder depth deferred) |

### Accounting/valuation integration

Covered by `stock_account`, `stock_landed_costs` above (Inventory Core). No separate module category — the interface is embedded in those two.

### Logistics / replenishment / route

| Module | Role |
|---|---|
| `stock` (routes/rules engine, embedded) | `stock.rule`, no separate route module |
| `delivery` + 13 carrier-connector modules (`delivery_ups`, `delivery_fedex`, `delivery_dhl`, etc.) | Carrier integration — out of scope, no Stock Truth ownership; registered for completeness (external-dependency risk, see A11-equivalent external register carried from GROUP A) |

### Traceability

Covered within `stock` core (`stock.lot`, `stock.package`, `stock.package.history`) — no separate traceability module exists; see A5.

### Custom / extra modules

`ks_dashboard_ninja`, `ks_dn_advance`, `addons_extra` (73 folders) — dashboard/reporting and miscellaneous third-party additions, not inspected; no evidence they own Inventory business facts (dashboards are read-only consumers by construction). Registered as out-of-scope, non-blocking.

### Source-specific technical / quarantine candidates

- The three approval modules GROUP A identified (`sale_order_level_approve`, `purchase_request_level_approve_po`, `purchase_request_level_approve`) — confirmed present as folder names in this source tree at `02 OTHER/`, consistent with GROUP A's DB-forensics finding. Their internal Python logic remains **EVIDENCE_MISSING** (GROUP A's own carried-forward item, confirmed still open — see A14).
- `ks_dashboard_ninja` / `ks_dn_advance` — third-party (Ksolves), no relation to Inventory business facts; clean-room quarantine not required (no vendor architecture adoption risk identified, since these are read-only reporting layers, not touched by this research).

### Unknown relevance (flagged, not classified)

- `barcodes_gs1_nomenclature` — GS1 barcode standard support; unclear whether this is core-relevant to Thailand retail/FMCG practice or purely a UX nicety. Registered as `UNKNOWN — LOW MATERIALITY` pending Thailand triangulation (see A11).

## Evidence counts (mechanical, not estimated)

- Total files under authorized source root: **93,866**.
- Top-level module folders in `02 OTHER/`: **1,378**.
- Module folders classified as Inventory Core or Direct Dependency (deep-read this pass, cumulative with GROUP A's prior reads): **8** (`stock`, `stock_account`, `stock_landed_costs`, `product`, `uom`, `sale_stock`, `purchase_stock`, `mrp`).
- Model files read across those 8 modules (this pass + GROUP A frozen evidence combined): **127+** (26 stock + 17 stock_account + 26 product + 2 uom + 10 sale_stock + 14 purchase_stock + 8 stock_landed_costs + 24 mrp).
- Module folders explicitly registered as out-of-scope/not-deep-read this pass: **~1,370** (barcode UX layer, carrier connectors, MRP sub-extensions, l10n_* localization packs for non-Thailand countries, dashboards, and all `02 OTHER/` folders not named above).

This is a **focused**, not exhaustive, source map, consistent with DR-002 §7/A1's own instruction to build "a focused Inventory source map from the larger source universe," not to individually classify all 93,866 files. Source count is not converted into a SMEsPlus target-module count anywhere in this document.

No Evidence = No Progress. DELTA-FIRST. Never Skip Gate.
