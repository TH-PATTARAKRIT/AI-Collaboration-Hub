> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 7 of 10 — Source↔Database↔Semantic Traceability Matrix
> Per governance §15: the database is evidence of business facts and usage, NOT a target schema. Where source and
> DB disagree, both are recorded — no silent winner is picked. Consolidates DB reconciliation work already done
> per-concept across Phases 1-5 into one canonical index. Every row cites an existing evidence ID.

# 08 — SOURCE ↔ DATABASE ↔ SEMANTIC TRACEABILITY MATRIX

## 00 — Method and legend

For each model: **Clean** = source and DB agree with no unexplained columns. **Wide** = DB carries columns not
declared in the module(s) this research opened — additive, not contradictory; declaring module usually identified
or reasonably inferred. **Orphaned** = DB carries columns/tables with **zero** declaring source found anywhere in
the extraction after exhaustive grep — a genuine gap, not merely out-of-scope. **Conflict** = source and DB
actively disagree (rare; recorded in full when found).

## 01 — Clean reconciliations (no unexplained columns)

| Model | Table | Evidence | Notes |
|---|---|---|---|
| `product.pricelist.item` | `product_pricelist_item` | Phase 1 PRC synthesis | Matches model 1:1, no unexplained extra columns |
| `account.payment.term.line` | `account_payment_term_line` | Phase 1 PAY synthesis | Matches PAY-08 exactly |
| `res.currency` / `res.currency.rate` | `res_currency` / `res_currency_rate` | Phase 1 CUR synthesis | All compute-only fields correctly absent as physical columns; matches exactly |
| `ir.sequence` | `ir_sequence` | Phase 1 SEQ synthesis | Matches SEQ-02 model fields exactly |
| `stock.location` | `stock_location` | Phase 1 WH-1.3 | Matches source 1:1 |
| `stock.putaway.rule` | `stock_putaway_rule` | Phase 2 PA synthesis | **The one sub-concept in the entire domain with no unexplained extension columns** |
| `account.analytic.plan` | `account_analytic_plan` | Phase 1 AN-3.3 | Matches source; no `company_id` column on the Plan itself, as source predicts |

## 02 — Wide shared tables (DB is a superset of the opened module — declaring module identified or inferred)

| Model | Table | Extra columns (sample) | Declaring module | Evidence | Confidence |
|---|---|---|---|---|---|
| `stock.move` | `stock_move` | `account_move_id`, `sale_line_id`, `purchase_line_id`, `production_id`, `workorder_id`, `repair_id`, `is_in`/`is_out` | `stock_account`, `sale_stock`, `purchase_stock`, `mrp`, `repair` (FKs confirm targets exactly: `→account_move`, `→sale_order_line`, `→purchase_order_line`) | Phase 2 DB-MOV-02/03/04/05 | VERIFIED FACT for the FK targets; `is_in`/`is_out` compute source EVIDENCE_MISSING |
| `stock.move.line` | `stock_move_line` | `workorder_id`, `production_id`, `expiration_date`, `removal_date` | `mrp`, expiry-tracking module (not opened) | Phase 2 DB-MOVL-01 | SUPPORTED INFERENCE on exact module names |
| `stock.picking` | `stock_picking` | `sale_id`, `carrier_id`, `project_id`, `ticket_id`, `batch_id`, `website_id`, `job_type_id` | `sale_stock`, shipping connector, `project`, `helpdesk`, `stock_picking_batch`, `website_sale` | Phase 2 PICK synthesis | SUPPORTED INFERENCE |
| `stock.lot` | `stock_lot` | `standard_price`, `avg_cost`, `expiration_date`, `use_date`, `removal_date`, `alert_date` | `product_expiry`, a landed-cost/valuation module | Phase 2 LOT synthesis | SUPPORTED INFERENCE |
| `stock.package_type` | `stock_package_type` | `shipper_package_code`, `package_carrier_type` | shipping/delivery-carrier module | Phase 2 PKG synthesis | SUPPORTED INFERENCE |
| `stock.warehouse.orderpoint` | `stock_warehouse_orderpoint` | `supplier_id`, `bom_id` | `purchase`/`purchase_stock` (supplier), `mrp` (BOM) | Phase 2 REPL synthesis | VERIFIED FACT — DB-level proof exactly matching the source-predicted extension pattern (REPL-07/09) |
| `stock.warehouse` | `stock_warehouse` | `manufacture_*`, `repair_*`, `subcontracting_*` | `mrp`, `repair`, `mrp_subcontracting` | Phase 1 WH-1.3 | SUPPORTED INFERENCE, out of GROUP A scope |
| `product.template` | `product_template` | `part_thickness`, `part_length`, `holding_conditions`, `min_qty`/`max_qty`, `*_filename` | Unidentified — reads like a manufacturing/engineering or cold-chain vertical | Phase 1 PRD-17 | SUPPORTED INFERENCE on purpose only, module not identified |
| `sale.order.line` | `sale_order_line` | `is_service`, `project_id`, `task_id`, `fsm_lot_id`, `planning_hours_*` | `sale_project`/`industry_fsm`, `sale_timesheet`/`planning` (not opened) | Sales §03 DB evidence | SUPPORTED INFERENCE |
| `purchase.order.line` | `purchase_order_line` | `sale_line_id`, `purchase_request_id`, `price_total_cc` | `sale_purchase` (confirmed, SLID-01 — declares `sale_line_id`), `purchase_request` (confirmed for `purchase_request_id`), `purchase_requisition` (`price_total_cc`, PREQS-15) | Purchase POL-37/38; Gap-closure SLID-01..12 | VERIFIED FACT — this row was fully closed in Phase 5, unlike most "Wide" rows which remain inferred |
| `purchase.order` | `purchase_order` | `auto_sale_order_id`, `auto_generated`, `requisition_id`, `purchase_group_id` | `sale_purchase_inter_company_rules` (confirmed), `purchase_requisition` (confirmed) | Purchase PO-21 database evidence | VERIFIED FACT |
| `res.partner` | `res_partner` | `brand_id`, `parent_company_id`, `hq_brand_id`, `is_hq_brand`, `store_type_id`, `bh_parent_company_code` | **None found** — see §03 Orphaned | — | Moved to Orphaned, not Wide — see below |

## 03 — Orphaned columns/tables (zero declaring source found anywhere, exhaustive grep)

This is the most consequential category for governance review — these are not "out of scope," they were
specifically searched for and not found.

| Model(s)/Table(s) | Orphaned columns | Search performed | Evidence | Severity |
|---|---|---|---|---|
| `res.partner` | `brand_id`, `parent_company_id`, `bh_parent_company_code`, `is_hq_brand`, `hq_brand_id`, `hq_brand_count`, `store_type_id`, plus 13 `x_studio_*` columns | Full-tree grep across `01 ACCOUNT`, `02 OTHER`, `addons_extra` | Phase 1 PTY-21, CO-24 | Medium — plausible Odoo-Studio/production customization; suggests a real multi-brand/multi-HQ retail structure never captured in this extraction |
| `sale_order`, `purchase_order`, `purchase_request` (all three) | `level1_user_id`, `level2_user_id`(missing on `purchase_request`), `level1_approved_by`, `level2_approved_by`, `level1_approved_date`, `level2_approved_date`, `reject_reason`, `x_review_result`, `x_has_request_approval` | Exhaustive full-tree grep, multiple independent passes across three separate research phases | Sales SO-43 (item 1); Purchase PO-21..34, DBX-01..06 | **Critical — the single largest open governance question in GROUP A research.** The one module whose manifest most directly promises this (`multi_level_approval_configuration`) is confirmed to have zero code wiring to two of the three models AND its own storage tables were never installed in this database — it cannot be the mechanical origin. `x_review_result`/`x_has_request_approval` circumstantially match that module's dynamic-field-creation pattern; the `level1_*`/`level2_*`/`reject_reason` fields do not match any known module's pattern at all. |
| `purchase_order_level_reject`, `purchase_request_level_reject` (whole tables) | `order_id`/`request_id`, `current_state`, `mode`, `reason` | Exhaustive grep for the table name and every plausible model-name variant | Purchase PO-23, DBX-04 | Critical — same investigation as above; two purpose-built audit-log tables with no owning model anywhere |
| `product_template` (subset) | `code`, `part_thickness`, `part_length`, `part_type_wi`, `part_code_id`, `product_revise_id`, `holding_conditions` | Full grep of `product/models/`, `stock/models/product.py`, opened `addons_extra` product modules | Phase 1 PRD-17/19 | Low-medium — reads like an unrelated vertical (manufacturing/cold-chain), not migration-blocking for GROUP A itself but worth flagging to whoever scopes Product master data fully |

## 04 — Conflicts (source and DB actively disagree — both recorded, neither silently resolved)

| Concept | Source says | DB says | Resolution recorded | Evidence |
|---|---|---|---|---|
| UOM grouping | `.po` translation files reference `uom.category` model and `uom.field_uom_uom__category_id` | No `uom_category` table exists; `uom_uom` has no `category_id` column | `.py` source and DB **agree** with each other (self-referential `relative_uom_id` tree, no category model) and **both disagree** with the stale `.po` files. Treat `.po` files as unreliable evidence of current model shape — do not resolve in the `.po` files' favor | Phase 1 UOM-20/21/22 |
| Purchase requisition's stated purpose | Manifest/description: "calls for tenders" | `requisition_type` Selection offers only `blanket_order`/`purchase_template` — no tender value exists | The manifest's marketing description does not match the field's actual domain. The real tendering mechanism lives on `purchase.order` (`alternative_po_ids`), independent of `purchase.requisition` entirely | Purchase PREQS-02, synthesis |
| `multi_level_approval_configuration`'s manifest | Names "Sale Order, Purchase Order, MRP Order" as example gated models | Zero code references to `sale.order` or `purchase.order` anywhere in the module; its own tables don't exist in the DB | Manifest description is a generic capability description / marketing text, not a record of actual configuration in this installation | Sales SO-43; Purchase APPR-05..07, PO-27..31 |

## 05 — Capability → Evidence chain index (governance §15's required format, worked examples)

```
Business Capability: "Can Sales confirm an order without checking inventory availability?"
→ Source Observation: sale_order_line._compute_qty_at_date() reads product-level forecast fields for
  display only (Sales GRPA-02/03/04); _confirmation_error_message() checks only state+product presence (SO-14)
→ Database Entity: no FK/trigger/constraint on sale_order/sale_order_line ties confirmation to stock_quant
→ State/Quantity Evidence: stock.quant.available_quantity is never queried inside action_confirm()'s call chain
→ Business Semantic: confirmation is availability-agnostic by design in this source system
→ Confidence: VERIFIED FACT (positive citation + full-file read of the confirmation gate)
```

```
Business Capability: "Does a two-level manager approval gate exist for Purchase Orders?"
→ Source Observation: _approval_allowed() implements a single amount-threshold+group check (PO-06), test-
  confirmed (PO-08); separately, level1_user_id/level2_user_id/etc. are referenced by ZERO source files
→ Database Entity: purchase_order carries both a working po_double_validation_amount column AND the orphaned
  level1_*/level2_* columns simultaneously
→ State/Quantity Evidence: only the amount-threshold mechanism has a traceable state transition (state='to
  approve' → 'purchase'); the level1/level2 columns have no observed write path anywhere
→ Business Semantic: TWO different approval concepts coexist on one model; only one is implemented in code
→ Confidence: VERIFIED FACT for the real gate; EVIDENCE_MISSING for the orphaned one — recorded as a
  CONFLICT/UNKNOWN, not resolved in either direction
```

## 06 — Summary counts (for the eventual Evidence Completeness deliverable)

- **Clean**: 7+ models fully reconciled with no unexplained columns (non-exhaustive list above; every phase's
  capability model contains additional clean reconciliations not repeated here to avoid duplication).
- **Wide**: 12 models/tables carry columns from other, unopened modules — 4 of these (`purchase.order.line`,
  `purchase.order`, plus the two closed in Phase 5) have their declaring module **confirmed**, not merely
  inferred; the remainder are SUPPORTED INFERENCE only.
- **Orphaned**: 3 model families (`res.partner`'s brand/HQ cluster; the cross-model approval schema; a narrow
  `product.template` manufacturing-vertical cluster) — the approval schema is by far the highest-severity item and
  should be the lead item in the eventual Fit-Gap pack's Unknown register.
- **Conflict**: 3 documented, all resolved in favor of the code+schema agreement over stale/aspirational
  documentation (translation files, module manifests) — none required inventing a tiebreaker, each had an
  independent second source (the DB schema itself) confirming which side was current.
