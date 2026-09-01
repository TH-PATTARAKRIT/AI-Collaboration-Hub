# CORR-006 — Boss High Escalation Re-Proof Report

Project: SMEsPlus ENTERPRISE SUITE  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Branch: `audit/inventory-core-corr006-boss-high-reproof-008`  
Base audit branch: `audit/inventory-core-corr005-delta-rereview-007`  
Timestamp: 2026-09-01  
Authority: Boss directed escalation of selected Medium findings to High for re-proof  
Mode: Evidence-first / clean-room / no development authorization

## 1. Boss Direction

Boss disagrees with the prior independent delta re-review severity position that none of the Medium items warranted High/Critical elevation. Boss directed the following eight items to be treated as High and re-proven:

1. `GRPA-M18`
2. `GRPA-M12`
3. `GRPA-M11`
4. `GRPA-M15`
5. `GRPA-M16`
6. `N-A7-01`
7. `N-A7-02`
8. `N-A12-01`

This CORR-006 report accepts Boss's severity direction for gate-control purposes. It does not rewrite evidence facts. It re-tests each item against available source/dump evidence and distinguishes actual closure from remaining High blockers.

## 2. Governance Boundary

This is not a Gate PASS.  
This is not Team B Inventory Design authorization.  
This is not Team C Development authorization.  
This is not permission to reuse Odoo source architecture.  
Odoo source remains reference / learning / benchmark only.

No Evidence = No Progress.  
Never Skip Gate.  
Boss is the sole Final Approver.

## 3. Evidence Sources Rechecked

Primary source inspected under the controlled local source tree:

- `SOURCE CODE/02 OTHER/stock/models/stock_move.py`
- `SOURCE CODE/02 OTHER/stock/models/stock_move_line.py`
- `SOURCE CODE/02 OTHER/stock/models/stock_quant.py`
- `SOURCE CODE/02 OTHER/stock/wizard/stock_picking_return.py`
- `SOURCE CODE/02 OTHER/stock/wizard/stock_inventory_conflict.py`
- `SOURCE CODE/02 OTHER/stock/wizard/stock_inventory_warning.py`
- `SOURCE CODE/02 OTHER/stock/wizard/stock_inventory_adjustment_name.py`
- `SOURCE CODE/02 OTHER/stock_dropshipping/models/stock.py`
- `SOURCE CODE/02 OTHER/mrp/models/mrp_unbuild.py`
- `SOURCE CODE/02 OTHER/purchase_stock/models/purchase_order_line.py`
- `SOURCE CODE/02 OTHER/sale_purchase_stock/models/purchase_order.py`
- `SOURCE CODE/02 OTHER/purchase_requisition/models/purchase.py`
- `SOURCE CODE/addons_extra/order_line_sequence/models/purchase_order_line.py`
- `SOURCE CODE/addons_extra/purchase_order_lines_discount/models/purchase_order_line.py`
- `SOURCE CODE/02 OTHER/l10n_th_reports/models/tax_report_pnd.py`
- `SOURCE CODE/02 OTHER/l10n_th_reports/tests/test_tax_report.py`
- `SOURCE CODE/02 OTHER/stock_account/models/stock_quant.py`
- `SOURCE CODE/02 OTHER/stock_account/wizard/stock_inventory_adjustment_name.py`
- `SOURCE CODE/02 OTHER/stock_account/models/stock_move.py`
- `SOURCE CODE/02 OTHER/stock_account/models/stock_picking.py`
- `SOURCE CODE/02 OTHER/stock_account/models/res_company.py`
- `SOURCE CODE/02 OTHER/stock_account/tests/test_stockvaluation.py`
- `SOURCE CODE/02 OTHER/stock_account/tests/test_account_move.py`

Database dump evidence attempted through `pg_restore -l` because the installed local `pg_restore` cannot fully restore dump format version `1.16`. Schema/list inspection was still possible and was used only where applicable.

## 4. Re-Proof Result Matrix

| ID | Boss severity | Re-proof result | Current gate disposition | Summary |
|---|---|---|---|---|
| `GRPA-M11` | High | Source evidence located | `RESOLVED — pending Boss acceptance` | `returned_move_ids` exists on `stock.move` and is used by the return wizard. |
| `GRPA-M12` | High | Source evidence located | `RESOLVED — pending Boss acceptance` | `produce_line_ids` exists on `stock.move.line` and `mrp.unbuild`; traceability linkage is written during unbuild. |
| `GRPA-M15` | High | Partially resolved | `HIGH REMAINS` | Most purchase-order-line unexplained columns were mapped to owning modules; one material source/dump drift remains for `purchase_request_id` on `purchase_order_line`. |
| `GRPA-M16` | High | Source file read in full | `RESOLVED AS READ-GAP; DESIGN CARRY-FORWARD` | Dropshipping file is now read; no missing-file evidence gap remains. Dropship remains a design concern, not a source-evidence blocker. |
| `GRPA-M18` | High | Source implementation located but statutory correctness not fully proven | `HIGH REMAINS — Accounting/Tax statutory proof required` | PND3/PND53 report handlers and tests exist, but source alone does not prove current Thai Revenue Department compliance completeness. |
| `N-A7-01` | High | Source behavior clarified | `HIGH REMAINS — Inventory design decision required` | Inventory count has `is_outdated` conflict detection; no hard count-in-progress freeze/lock field was found. |
| `N-A7-02` | High | Source flow traced | `RESOLVED — pending Boss acceptance` | `inventory_diff_quantity` is converted into stock moves through `_apply_inventory()` and `_get_inventory_move_values()`, then validated via `_action_done()`. |
| `N-A12-01` | High | Partially resolved | `HIGH REMAINS — Accounting x Inventory cross-proof required` | Accounting date and lock-date mechanisms exist, but full cross-year migration continuity still requires joint cross-proof. |

## 5. Item-by-Item Proof

### 5.1 `GRPA-M11` — `returned_move_ids`

Prior issue: field definition not located.

Rechecked source evidence:

- `stock/models/stock_move.py:155-158`
  - `origin_returned_move_id = fields.Many2one('stock.move', ...)`
  - `returned_move_ids = fields.One2many('stock.move', 'origin_returned_move_id', ...)`
- `stock/wizard/stock_picking_return.py:55-78`
  - return wizard links original moves, sibling moves, and downstream return chains through `returned_move_ids`.

Conclusion:

`GRPA-M11` is no longer evidence-missing. The field exists and the return workflow uses it. For Boss gate purposes this item may be closed as `RESOLVED`, subject to Boss acceptance.

Recommended disposition: `RESOLVED`.

### 5.2 `GRPA-M12` — `produce_line_ids`

Prior issue: field definition not located; suspected MRP/unbuild/traceability relation.

Rechecked source evidence:

- `stock/models/stock_move_line.py:87-88`
  - `consume_line_ids` and `produce_line_ids` are Many2many fields using relation table `stock_move_line_consume_rel`.
- `mrp/models/mrp_unbuild.py:73-78`
  - `consume_line_ids` and `produce_line_ids` exist on unbuild order as `One2many` relationships to `stock.move`.
- `mrp/models/mrp_unbuild.py:234-239`
  - unbuild flow marks finished/consume/produce moves as picked, validates them, then writes `produce_line_ids` onto consumed move lines.

Conclusion:

`GRPA-M12` is no longer evidence-missing. The field exists and is used in MRP/unbuild traceability.

Recommended disposition: `RESOLVED`.

### 5.3 `GRPA-M15` — purchase-order-line unexplained columns

Prior issue: owning modules for remaining `purchase_order_line` columns not fully identified.

Dump/schema evidence from `pg_restore -l` identified `purchase_order_line` columns including:

- `orderpoint_id`
- `location_final_id`
- `product_description_variants`
- `propagate_cancel`
- `sale_line_id`
- `price_total_cc`
- `sequence_no`
- `fixed_discount`
- `purchase_request_id`

Source ownership evidence located:

| Column | Source evidence | Owner / interpretation |
|---|---|---|
| `orderpoint_id` | `purchase_stock/models/purchase_order_line.py:28-35`, `333-360` | `purchase_stock`; procurement/replenishment linkage. |
| `location_final_id` | `purchase_stock/models/purchase_order_line.py:35`, `333-360`; `sale_purchase_stock/models/purchase_order.py:21-50` | Purchase-to-stock / sale-purchase-stock location propagation. |
| `product_description_variants` | `purchase_stock/models/purchase_order_line.py:31`, `333-360` | Variant/custom description propagation to purchase line and stock moves. |
| `propagate_cancel` | `purchase_stock/models/purchase_order_line.py:32`, `300-310`; `purchase_stock/models/purchase_order.py:215` | Cancellation propagation to stock moves. |
| `sale_line_id` | `sale_purchase_stock/models/purchase_order.py:21-50` | Dropship / SO-to-PO traceability. |
| `price_total_cc` | `purchase_requisition/models/purchase.py:249-255` | Purchase requisition/company-currency subtotal. |
| `sequence_no` | `addons_extra/order_line_sequence/models/purchase_order_line.py:6-20` | Extra module order-line sequence. |
| `fixed_discount` | `addons_extra/purchase_order_lines_discount/models/purchase_order_line.py:9-35` | Extra module fixed-discount behavior. |

Remaining unresolved drift:

- Dump contains `purchase_order_line.purchase_request_id`.
- Source search found `purchase_request_ids` on `stock_move`, but did not locate a `purchase_order_line.purchase_request_id` field definition in the available source tree.

Conclusion:

`GRPA-M15` is materially narrowed but not fully closed. Because `purchase_request_id` appears in dump schema without located source ownership, this remains a real source-to-dump drift and should stay High until resolved by either:

1. locating the owning source module, or
2. confirming it is legacy/custom residue and designing a migration disposition.

Recommended disposition: `HIGH REMAINS — source/dump drift`.

### 5.4 `GRPA-M16` — `stock_dropshipping/models/stock.py`

Prior issue: file was not read in full.

Rechecked source evidence:

- `stock_dropshipping/models/stock.py:7-34`
  - extends `stock.rule`.
  - groups procurements by `sale_line_id` to avoid incorrectly merging purchase lines tied to different sale lines.
  - returns no partner for dropship route in `_get_partner_id()`.
  - filters rule domain by `company_id` when `sale_line_id` and `company_id` exist.
- `stock_dropshipping/models/stock.py:37-52`
  - computes `stock.picking.is_dropship` when source is supplier/transit and destination is customer/transit.
  - treats dropship picking as external-location flow.
- `stock_dropshipping/models/stock.py:54-84`
  - extends picking type with `code='dropship'`, default supplier/customer locations, and visible picking type behavior.
- `stock_dropshipping/models/stock.py:87-104`
  - adjusts lot partner computation and outgoing-domain behavior for dropship deliveries.

Conclusion:

The specific read-gap is closed. Dropshipping remains architecturally important for SMEsPlus because it changes normal Stock Truth assumptions, but it is no longer an evidence-missing file-read blocker.

Recommended disposition: `RESOLVED AS READ-GAP; CARRY TO DESIGN AS DROPSHIP FLOW REQUIREMENT`.

### 5.5 `GRPA-M18` — Thai WHT PND form-code correctness

Prior issue: current Thai WHT PND correctness not proven.

Rechecked source evidence:

- `l10n_th_reports/models/tax_report_pnd.py:12-23`
  - defines abstract PND report handler and CSV headers.
- `l10n_th_reports/models/tax_report_pnd.py:30-60`
  - SQL extracts Tax ID, address, branch number, date, tax rate, base amount, WHT amount, WHT condition, and tax type.
- `l10n_th_reports/models/tax_report_pnd.py:48-54`
  - tax type is hard-coded by tax rate:
    - `-1` = Transportation
    - `-2` = Advertising
    - `-3` = Service
    - `-5` = Rental
    - otherwise blank
- `l10n_th_reports/models/tax_report_pnd.py:74-108`
  - PND53 handler exports CSV.
- `l10n_th_reports/models/tax_report_pnd.py:111-145`
  - PND3 handler exports CSV.
- `l10n_th_reports/tests/test_tax_report.py:46-86`
  - PND53 test covers 3% service and 2% advertising.
- `l10n_th_reports/tests/test_tax_report.py:88-128`
  - PND3 test covers 1% transportation and 2% advertising.

Material limitation:

The source proves that PND3/PND53 report handlers and tests exist. It does not prove current statutory completeness, all WHT categories, e-filing layout compatibility, title/person/company classification completeness, branch-code correctness, or current Revenue Department mapping correctness.

Conclusion:

Boss's High escalation is justified. This item is not closable from source evidence alone. It must be owned by Accounting/Tax with statutory rule verification.

Recommended disposition: `HIGH REMAINS — Accounting/Tax statutory validation required`.

### 5.6 `N-A7-01` — count-in-progress vs settled on-hand freeze state

Prior issue: model/field/state representing count-in-progress freeze was unknown.

Rechecked source evidence:

- `stock/models/stock_quant.py:97-114`
  - inventory fields include `inventory_quantity`, `inventory_quantity_auto_apply`, `inventory_diff_quantity`, `inventory_date`, `last_count_date`, `inventory_quantity_set`, `is_outdated`, `user_id`.
- `stock/models/stock_quant.py:185-202`
  - `inventory_diff_quantity` computes counted minus theoretical quantity.
  - `is_outdated` becomes true when quantity changed after inventory count was set.
- `stock/models/stock_quant.py:433-450`
  - `action_apply_inventory()` detects outdated quants and opens `stock.inventory.conflict` wizard before applying inventory.
- `stock/wizard/stock_inventory_conflict.py:16-24`
  - users must choose whether to keep counted quantity or keep difference.
- `stock/wizard/stock_inventory_warning.py:13-18`
  - warning wizard can reset or set inventory quantities.

What was not found:

No explicit hard freeze/lock field or state was located that blocks normal stock movement while a count is in progress. The evidence points to conflict detection at apply-time rather than prevention at movement-time.

Conclusion:

Boss's High escalation is justified. This item affects Quantity Integrity and inventory cutover safety. SMEsPlus must make an explicit design decision: hard freeze, soft conflict resolution, location freeze, count session lock, or controlled exception workflow.

Recommended disposition: `HIGH REMAINS — Inventory count freeze policy required before design freeze`.

### 5.7 `N-A7-02` — conversion of `inventory_diff_quantity` into posted stock move

Prior issue: exact method converting inventory difference into stock move was not traced.

Rechecked source evidence:

- `stock/models/stock_quant.py:996-1035`
  - `_apply_inventory()` sets inventory quantity, calculates `inventory_diff_quantity`, creates `move_vals`, creates `stock.move`, validates with `_action_done()`, triggers assignment, updates next inventory date, and clears counted quantity.
- `stock/models/stock_quant.py:1015-1025`
  - positive difference creates movement from inventory loss location to stock location.
  - negative difference creates movement from stock location to inventory loss location.
- `stock/models/stock_quant.py:1253-1292`
  - `_get_inventory_move_values()` builds the stock move and move line values, including product, UOM, quantity, company, source/destination locations, lot/package/owner, `is_inventory=True`, and `picked=True`.
- `stock_account/models/stock_quant.py:80-101`
  - accounting override passes `force_period_date` and adjusts inventory move naming for accounting date.
- `stock_account/models/stock_move.py:199-206`
  - account move is created and posted with `date = force_period_date or today`.

Conclusion:

`N-A7-02` is closed as a source-flow proof. The exact source path is now traced.

Recommended disposition: `RESOLVED`.

### 5.8 `N-A12-01` — cross-year inventory continuity / fiscal-year boundary

Prior issue: year-end / fiscal-year-boundary handling unknown.

Rechecked source evidence:

- `stock_account/models/stock_quant.py:12-16`
  - `accounting_date` exists for inventory adjustment accounting entries.
- `stock_account/wizard/stock_inventory_adjustment_name.py:7-20`
  - inventory adjustment wizard carries `accounting_date` into context as `force_period_date`.
- `stock_account/models/stock_move.py:199-206`
  - accounting entry date uses `force_period_date` when present.
- `stock_account/models/stock_picking.py:13-33`
  - validates scheduled/date_done against company lock-date violations for fiscalyear and hard lock dates.
- `stock_account/tests/test_account_move.py:258-322`
  - test confirms fiscal-year/hard lock dates prevent backdating completed picking into locked periods.
- `stock_account/tests/test_stockvaluation.py:3057-3082`
  - test confirms inventory adjustment journal entry can be created with specified accounting date.
- `stock_account/models/res_company.py:264-310`
  - period variation logic uses fiscal year start and stock accounting values over period.

Material limitation:

The source proves mechanisms exist for lock-date protection and inventory adjustment accounting date. It does not fully prove SMEsPlus migration continuity across a real legacy cutover, cross-year stock valuation reconciliation, opening quantity valuation, or Accounting x Inventory cross-proof.

Conclusion:

Partially resolved. Boss's High escalation remains justified until a joint Accounting x Inventory cross-proof validates the target SMEsPlus design and migration continuity.

Recommended disposition: `HIGH REMAINS — cross-proof required`.

## 6. Updated High Disposition After Re-Proof

If Boss accepts the proof results, the eight Boss-escalated items should be dispositioned as follows:

| Result bucket | Items | Count |
|---|---|---:|
| `RESOLVED — close as evidence-missing item` | `GRPA-M11`, `GRPA-M12`, `N-A7-02` | 3 |
| `RESOLVED AS READ-GAP; design carry-forward` | `GRPA-M16` | 1 |
| `HIGH REMAINS` | `GRPA-M18`, `GRPA-M15`, `N-A7-01`, `N-A12-01` | 4 |

Therefore, the corrected post-reproof High blocker count is not 8 if Boss accepts closure evidence. It is 4 remaining High items plus 1 design carry-forward (`GRPA-M16`) that should not block evidence-read closure but should influence Inventory design.

## 7. Boss Decision Recommendation

Recommended decision:

`BOSS REVIEW REQUIRED — ACCEPT CORR-006 PARTIAL HIGH CLOSURE AND KEEP 4 HIGH BLOCKERS CONTROLLED`

Recommended Boss acceptance actions:

1. Accept closure of `GRPA-M11`, `GRPA-M12`, and `N-A7-02`.
2. Accept `GRPA-M16` as source-read resolved, with dropshipping carried forward into Inventory design requirements.
3. Keep `GRPA-M18` High under Accounting/Tax statutory validation.
4. Keep `GRPA-M15` High until `purchase_request_id` source/dump drift is resolved.
5. Keep `N-A7-01` High until Inventory count freeze/conflict policy is decided.
6. Keep `N-A12-01` High until Accounting x Inventory cross-proof validates fiscal-year / migration continuity.
7. Do not authorize Team C Development from this report.
8. Do not declare Inventory Evidence Gate PASS until Boss explicitly decides.

## 8. Final Status

`CORR-006 BOSS HIGH RE-PROOF COMPLETE — READY FOR BOSS RE-CONSIDERATION`

This report is evidence publication only. Final approval remains with Boss.
