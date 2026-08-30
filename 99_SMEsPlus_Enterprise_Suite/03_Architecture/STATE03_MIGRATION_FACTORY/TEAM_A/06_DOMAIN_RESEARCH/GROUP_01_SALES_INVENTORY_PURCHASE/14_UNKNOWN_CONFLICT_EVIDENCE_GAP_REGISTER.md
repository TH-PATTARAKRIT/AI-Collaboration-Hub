> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 9 of 10 — Unknown / Conflict / Evidence Gap Register
> Master consolidation of every UNKNOWN, EVIDENCE_MISSING, and CONFLICT flagged across Phases 1-8. Nothing here is
> resolved to a guess — this register exists specifically so nothing gets silently dropped between deliverables.

# 14 — UNKNOWN / CONFLICT / EVIDENCE GAP REGISTER

## 00 — Severity legend

**Critical** = blocks a Fit-Gap or governance decision until resolved. **High** = materially affects confidence in
a specific capability area. **Medium** = a real gap, narrow blast radius. **Low** = out-of-scope-but-noted.

## 01 — Critical

| # | Gap | Description | Evidence | Severity rationale |
|---|---|---|---|---|
| 1 | Orphaned two-level approval schema | `sale_order`, `purchase_order`, and `purchase_request` all carry `level1_user_id`/`level2_user_id`/`level1_approved_by`/`level2_approved_by`/approval-dates/`reject_reason` columns (plus two parallel reject-log tables) with **zero corresponding Python source anywhere**. The one module whose manifest most directly promises this feature has no code wiring to two of the three models and its own storage tables were never installed in the database. | Sales SO-43, §08 item 1; Purchase PO-21..34, DBX-01..06 | Directly affects whether ANY approval workflow can be assumed to exist for Sales/Purchase order confirmation — the single largest unresolved question in this entire research effort. Requires row-level data (`ir_model_fields`/`ir_model_data`) to resolve; not resolvable from source. |
| 2 | Purchase's post-confirmation cancellation cascade into `stock.picking` | Sale's equivalent (`sale_stock._action_cancel()`) is test-confirmed to cancel not-done pickings while sparing done ones. Whether `purchase_stock` does the same was never opened in any phase. | Purchase §04 synthesis | Blocks a symmetric conclusion about cancellation behavior across the two commercial modules — flagged repeatedly (E2E Scenario 7/8, Invariant Register #8) |
| 3 | `_run_buy()`'s exact implementation | The dispatch mechanism connecting a reordering rule to Purchase order creation is fully proven (`stock.rule.run()`'s generic `getattr` dispatch); the actual body of `purchase_stock`'s `_run_buy()` — what fields it sets on the new PO — was never opened in any phase of this research. | Phase 5 gap-closure synthesis; E2E Scenario 2 | Blocks a complete "Sales demand → automatic Purchase order" narrative; the trigger and dispatch are proven, the payload is not |

## 02 — High

| # | Gap | Description | Evidence |
|---|---|---|---|
| 4 | `account.fiscal.position`'s base model file | Referenced constantly by both Sale and Purchase tax computation (`map_tax()`, `_get_fiscal_position()`) but never located in the source tree — only country-localization overrides exist by that filename. The actual tax-substitution logic is a black box in this evidence set. | Phase 1 TAX synthesis |
| 5 | Orphaned `res.partner` multi-brand/multi-HQ columns | `brand_id`, `parent_company_id`, `hq_brand_id`, `is_hq_brand`, `store_type_id`, `bh_parent_company_code`, plus 13 `x_studio_*` fields — real DB columns, zero source anywhere. Suggestive of a real multi-brand retail structure never captured in this extraction. | Phase 1 PTY-21, CO-24 |
| 6 | The exact `stock_move.py` call site that re-invokes `stock.rule.run()` for a `make_to_order` move | The chaining data model (`move_dest_ids`/`move_orig_ids`) is fully proven to exist and be populated for this purpose; the specific trigger line inside `stock_move.py`'s confirm/assign methods was never opened. | Phase 5 gap-closure RULE-13 synthesis |
| 7 | Whether `purchase_stock` extends `stock.rule.action`'s Selection with `'buy'` | Architecturally necessary (SUPPORTED INFERENCE) for `'buy'` to be a legal value at all, but `purchase_stock/models/stock_rule.py` was never opened to confirm the `selection_add` directly. | Phase 5 gap-closure Gap 1 item 4 |
| 8 | Two independent, uncoordinated Thai "branch" modules | `l10n_th_partner.branch` vs `bm_thai_rd_vat_company_search.office_type` — no evidence either is aware of the other; mutual data consistency is unresolved. | Phase 1 CO-15..24 |
| 9 | `stock.picking.action_cancel()`'s own body | Called from Sale's cancellation cascade; whether it always cascades to moves the same way `stock_move._action_cancel()`'s "cannot cancel a done move" rule does was not independently opened. | Sales CANC-05 synthesis |

## 03 — Medium

| # | Gap | Description | Evidence |
|---|---|---|---|
| 10 | `stock_move.is_in`/`is_out` column semantics | Real DB columns, compute source never opened in any phase. | Phase 2 DB-05 |
| 11 | `returned_move_ids` field definition | Referenced from the return wizard, never located as a field definition in the portions of `stock_move.py` read. | Phase 2 RET synthesis |
| 12 | `produce_line_ids` (likely MRP) | Referenced from `stock_lot.py`'s delivery-traceability walk, never independently opened. | Phase 2 LOT synthesis |
| 13 | Owning module for `sale_order_line.is_service` | Real DB column, zero grep hits in `sale`/`sale_stock`. | Sales §06 synthesis |
| 14 | `product.type` literal value `'product'` seen alongside `'consu'` in one override | Unexplained — whether this is a valid current enum value, a legacy synonym, or dead code was not resolved (Phase-1 product-master scope, not re-opened). | Sales SVS-11 |
| 15 | Owning module for `purchase_order_line`'s remaining unexplained columns | `price_total_cc` (resolved to `purchase_requisition`, PREQS-15) is closed; a few others noted in Purchase POL-38 were not individually chased. | Purchase POL-38 |
| 16 | Full contents of `stock_dropshipping/models/stock.py` | Opened only for a two-line excerpt establishing an `is_dropship` compute field; not read in full. | Purchase §07 synthesis |
| 17 | `stock.rule.Procurement`'s exact field-level typing beyond the 8 confirmed positional fields | The NamedTuple itself was fully read (Phase 5 gap-closure RULE-01) — this item is now CLOSED, listed here only for completeness/audit trail. | Phase 5 gap-closure RULE-01 |
| 18 | WHT PND form-code correctness against current Thai Revenue Department rules | Codes are present in source (PND1/3/3a/53); no authoritative government source was consulted to verify currency. | Phase 8 WHT-10 |
| 19 | Whether Thai district/sub-district address data reaches any delivery/shipping workflow | No code path was found reading these two columns outside the address-import wizard itself. | Phase 8 ADDR item 2 |

## 04 — Low (out-of-scope-but-noted)

| # | Gap | Description | Evidence |
|---|---|---|---|
| 20 | MRP/Repair/Purchase-Requisition extension columns on `stock_move`/`stock_move_line` (`production_id`, `workorder_id`, `bom_line_id`, `repair_id`, `cost_share`, etc.) | Existence confirmed via DB, semantics out of GROUP A scope. | Phase 2 DB-MOV-02/DB-MOVL-01 |
| 21 | `stock_warehouse` MRP/repair/subcontracting extension columns | Same pattern, out of scope. | Phase 1 WH-1.3 |
| 22 | `product_template` unexplained manufacturing/cold-chain-vertical columns (`part_thickness`, `holding_conditions`, etc.) | No owning module identified; likely an unrelated vertical. | Phase 1 PRD-17/19 |
| 23 | `num2words` Thai-locale linguistic/legal correctness | Not independently verified; delegated to a third-party library. | Phase 8 TXT-06/07 |

## 05 — Resolved during this research effort (for audit trail — do not re-open without new evidence)

| # | Item | How it was resolved |
|---|---|---|
| R1 | Whether the stale `.po` translation files' reference to a `uom.category` model reflects a live model | **No** — both `.py` source and DB schema independently confirm no such model/column exists; the `.po` files are stale artifacts | Phase 1 UOM-20/21/22 |
| R2 | Whether `purchase.requisition` is the multi-vendor tendering table | **No** — it's a standing agreement (blanket order/template); tendering lives on `purchase.order` itself, independent of any requisition | Purchase PREQS-02, synthesis |
| R3 | Whether `purchase_order_group`/`purchase_order_discount` DB tables are approval-related | **No** — both fully resolved to legitimate, unrelated, sourced code (RFQ-grouping and a discount wizard respectively) | Purchase PO-24/25 |
| R4 | The declaring module for `purchase_order_line.sale_line_id` | **Resolved**: `sale_purchase` (Subcontract Service scenario), subsequently reused by `sale_purchase_stock`/`stock_dropshipping` for true dropshipping | Phase 5 gap-closure SLID-01..12 |
| R5 | Whether ANY approval module wires into `purchase.order`/`purchase.requisition` in source | **No** — exactly one wiring point exists anywhere in the `multi_level_approval*` suite, and it targets `purchase.request` only | Purchase APPR-05..09 |

## 06 — Carry-forward instruction

Items in §01 (Critical) should be the lead items in `16_FIT_GAP_CANDIDATE_PACK.md`'s Unknown classification and in
`18_TEAM_A_EVIDENCE_GATE_CANDIDATE_REPORT.md`'s blocking-items section. Items in §02-04 should be preserved as-is
for whoever continues this research line — none require Boss escalation on their own, but none should be silently
dropped either.
