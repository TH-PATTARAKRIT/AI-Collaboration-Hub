# Correction packet U07-R2 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched. No V-level, completeness or verification claim is made.

| Field | Value |
|---|---|
| Correction packet | `U07-R2` |
| Correction request | CR-014 |
| Classification | NEEDS_MORE_EVIDENCE · priority Normal |
| Boundary | U07 — receipts — double-negative condition in the bill-based receipt valuation; lot-to-purchase-order link |
| Subject | `purchase_stock/models/stock_move.py` around line 196 (expression `x -= -y` in `_get_value_from_account_move`) and `purchase_stock/models/stock.py` lines 332-354 (lot-to-order link): what each does, effect on received quantity and on lot traceability |
| Original evidence | U07 content 03a764e2 / packet HP_U07 (VDR-U07-C130, C172 to C177 cover lines 157-223 of stock_move.py but not the outgoing-move branch at line 196; CAP-U07-05 returns); U10 content 4a4f39cf (VDR-U10-C114, C115); C02 audit 72cf594a findings F06, F07; neither U07 nor U09 covers the lot-to-order link |
| Supersession | none — supplements. VDR-U07-C174 (states that earlier in / dropship moves absorb billed quantity) and neutral N-U07-085 stay valid but are incomplete: outgoing moves also change the absorbed quantity (C008 to C011). Not contradicted. |
| Function-ID | `GRV-F04` (valuation at receipt) for the bill-based allocation claims; `FUNCTION MAPPING REQUIRED` for the lot-to-order link (no existing ID matches lot traceability to purchase orders) |

## 1. Scope and method

- Original U07 / U10 / U09 claims were checked first (listed in the header); this packet adds only the two sites named in CR-014 and the code those sites depend on (`stock_account` valued quantity and value priority, purchase order line received quantity, lot view, ACL).
- Runtime behaviour is not inferred. The direction of intent of the double negation and numeric outcomes are `UNKNOWN` with `RT`.

## 2. Findings (prose, with claim ids)

**A. Line 196 of purchase_stock stock_move.py.** `_get_value_from_account_move` decides how much of the value of a receipt move can be taken from posted vendor bills of its order line (C001 to C006). Before using the bill quantity it counts, as "other candidates", the valued quantity of earlier moves of the same order line and product (C007). Incoming and drop-shipped earlier moves add their valued quantity; for earlier outgoing moves the code writes `other_candidates_qty -= -move._get_valued_qty()` (C008). The valued quantity of an outgoing move is a non-negative product-unit quantity (C009, C010), so the double negation evaluates as an addition: an earlier outgoing move (for example a return to the vendor that belongs to the order line, C016 to C018) increases the quantity treated as already covered by the bills (C011). The remaining billed quantity for the later move is then smaller or nil and its value falls back to the quotation, return or cost sources (C012 to C014). Whether adding is intended is not documented in the source (C015, UNKNOWN, RT).

**B. Effect on received quantity.** None found: the received quantity of an order line is computed from done moves by `_prepare_qty_received` (C019) and does not call the bill-based valuation (C023); the valuation result is stored in the move value (C024). The condition that decides which moves are ignored when counting received quantity (line 74 of purchase_order_line.py) has operator precedence `(A and B and not C) or (not D)` (C020 to C022); it is recorded here because it is the other double-negative-style condition on the same path, effect RT.

**C. Lot traceability.** The allocation loop calls the valued quantity without a lot argument, so it is not lot-aware (C025). The lot-to-order link is a separate, on-demand computation on the lot: for each lot it searches done move lines of that lot and keeps those whose transfer comes from a supplier or transit location and whose move has an order line, collecting the orders (C026 to C031). It is shown as a Purchases stat button on the lot form and opens the order list (C031 to C033); stock users have read-only access to orders (C034). Limits: receipt-side only, no stored link, returns do not remove the link, same lot name in several receipts links all their orders (C035, C036). The DB has no lots, so nothing could be reconciled (C037). Reverse traceability (order to lots) and lot-valuated flows are not covered here (C038, UNKNOWN).

## 3. Ten-dimension coverage (both sites)

| # | Dimension | Finding (claim ids) |
|---|---|---|
| 1 | Happy path | Receipt validated, bill posted, receipt move valued from bill (C001 to C006, C012, C013); lot received from vendor shows the order on the lot form (C028 to C033). |
| 2 | Reversal / negative | Vendor refund subtracts billed quantity (C005); earlier outgoing move adds to absorbed quantity (C008 to C011); returns subtract received quantity unless ignored (C019 to C022); returned lot keeps the order link (C035). |
| 3 | Multi-company | Lot link runs under the caller's rights and record rules; company rules on orders apply (U06 C310 family); not further read (C034). |
| 4 | Side effects | Move value updated for incoming moves (C024); no effect on received quantity (C023); no stored lot link (C027). |
| 5 | Configuration / optionality | Bill-based value only for moves with an order line (C004); lot button shown only when count is positive and the lot is saved (C032, C033). |
| 6 | Validation / constraints | None on either site; the allocation is silent arithmetic (C008, C012). |
| 7 | Roles / permissions | Stock users read orders and lines (C034); lot form button needs no extra group (C032). |
| 8 | Scheduled / automated | None. |
| 9 | Exception / failure | No raise paths in either site; wrong direction of the sum would be silent (C015). |
| 10 | Accounting, stock, audit | Bill-priced share of receipt value may be understated when earlier outgoing moves exist (C011, C014, RT); lot-to-order traceability is partial (C035, C036, C038). |

## 4. DB reconciliation (configuration only)

- Restored DB has no stock lots and no stock move lines, no purchase orders and no bills; both sites are therefore source-derived only.
- ACL rows from purchase_stock: stock user group has read-only access on purchase orders and purchase order lines (2 rows).

## 5. Unknown / Runtime list (RT)

1. Whether the double negation is intended and the numeric effect on value when an outgoing move linked to the same order line precedes the receipt being valued (C011, C014, C015).
2. Whether return-to-vendor moves reach the loop in practice (C018).
3. Effect of the precedence in the received-quantity condition for specific move kinds (C020).

## 6. DISCOVERED SUPPORTING MODULES

`stock_account` (valued quantity, value priority, move value), `stock` (move line quantity, lot display flag, base received-quantity test), `mrp_subcontracting` (extends the received-quantity test), `purchase` (order line and ACL). No Enterprise module read.

## 7. Contradictions with prior evidence

None found. VDR-U07-C174 / VDR-U10-C115 are consistent but incomplete (outgoing branch omitted).

## 8. Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U07R2-C001 | GRV-F04 | purchase_stock/models/stock_move.py:157 | def _get_value_from_account_move | FACT | purchase_stock installed | — | purchase_stock overrides _get_value_from_account_move(quantity, at_date) to value a move from posted vendor bills of its order line. | N-U07R2-001 |
| VDR-U07R2-C002 | GRV-F04 | stock_account/models/stock_move.py:481 | return dict(VALUATION_DICT) | FACT | stock_account installed | — | The base _get_value_from_account_move returns an empty valuation (no value, no quantity). | N-U07R2-001 |
| VDR-U07R2-C003 | GRV-F04 | stock_account/models/stock_move.py:403 | self._get_value_from_account_move(remaining_qty, at_date) | FACT | stock_account installed | — | In the move value computation, bills are the first source (after manual value); production, quotation, returns and product cost follow for the quantity not yet valued (lines 409-436). | N-U07R2-002 |
| VDR-U07R2-C004 | GRV-F04 | purchase_stock/models/stock_move.py:159 | if not self.purchase_line_id | FACT | purchase_stock installed | — | A move without an order line takes the base (empty) bill valuation. | N-U07R2-001 |
| VDR-U07R2-C005 | GRV-F04 | purchase_stock/models/stock_move.py:172 | aml.move_id.state != 'posted' | FACT | purchase_stock installed | — | Only posted bill lines of the order line dated on or before the as-at date count; bills add and vendor refunds subtract quantity and value (lines 175-180; same as VDR-U07-C172, C173). | N-U07R2-003 |
| VDR-U07R2-C006 | GRV-F04 | purchase_stock/models/stock_move.py:182 | if aml_quantity <= 0 | FACT | purchase_stock installed | — | If the net billed quantity is not positive the base (empty) valuation is returned. | N-U07R2-003 |
| VDR-U07R2-C007 | GRV-F04 | purchase_stock/models/stock_move.py:191 | move.date > self.date | FACT | purchase_stock installed | — | Other moves of the same order line and product that are not later than this move (earlier date, or same date with lower id) are scanned; incoming moves and drop-shipped moves add their valued quantity to other_candidates_qty (lines 193-194). | N-U07R2-004 |
| VDR-U07R2-C008 | GRV-F04 | purchase_stock/models/stock_move.py:196 | other_candidates_qty -= -move._get_valued_qty() | FACT | earlier move is outgoing | — | For earlier outgoing moves the statement is a double negation: subtracting the negated valued quantity equals adding it. | N-U07R2-005 |
| VDR-U07R2-C009 | GRV-F04 | stock_account/models/stock_move.py:455 | _get_out_move_lines(lot) | FACT | stock_account installed | — | The valued quantity of an outgoing move is the sum of the product-unit quantities of its outgoing move lines (lines 454-455). | N-U07R2-005 |
| VDR-U07R2-C010 | GRV-F04 | stock/models/stock_move_line.py:170 | quantity_product_uom | FACT | stock installed | — | The product-unit quantity of a move line is its quantity converted to the product unit with HALF-UP rounding; it carries the sign of the quantity field (not negated for outgoing lines). | N-U07R2-005 |
| VDR-U07R2-C011 | GRV-F04 | purchase_stock/models/stock_move.py:196 | other_candidates_qty -= -move._get_valued_qty() | INFERENCE | earlier outgoing move linked to the same order line | RT | INFERENCE from C008 to C010: an earlier outgoing move increases the quantity treated as already covered by the bills, exactly like an earlier receipt, instead of decreasing it. Numeric outcome needs execution. | N-U07R2-005 |
| VDR-U07R2-C012 | GRV-F04 | purchase_stock/models/stock_move.py:198 | self.product_uom.compare(aml_quantity, other_candidates_qty) | FACT | purchase_stock installed | — | If the net billed quantity is not larger than the absorbed quantity the base valuation is returned (the bill is not used for this move); otherwise value and quantity are scaled by (billed minus absorbed) over billed (lines 201-203). | N-U07R2-006 |
| VDR-U07R2-C013 | GRV-F04 | purchase_stock/models/stock_move.py:205 | if quantity >= aml_quantity | FACT | purchase_stock installed | — | The bill-valued quantity is capped to the move's remaining quantity (full remaining billed quantity if smaller, otherwise proportional) and a description naming the bills is set (lines 206-214). | N-U07R2-006 |
| VDR-U07R2-C014 | GRV-F04 | purchase_stock/models/stock_move.py:198 | other_candidates_qty | INFERENCE | earlier outgoing move linked to the same order line | RT | INFERENCE from C003, C011, C012: because of the added quantity the bill-priced share of a later receipt is smaller or zero and the rest of its value is taken from quotation, returns or product cost (stock_account lines 416-436). | N-U07R2-005 |
| VDR-U07R2-C015 | GRV-F04 | purchase_stock/models/stock_move.py:196 | other_candidates_qty -= -move._get_valued_qty() | UNKNOWN | earlier outgoing move linked to the same order line | RT | UNKNOWN — EVIDENCE INSUFFICIENT: the source has no comment on the intended sign for outgoing moves and no test was run; whether adding is intended and the resulting values need execution (AWT). | N-U07R2-014 |
| VDR-U07R2-C016 | GRV-F04 | purchase_stock/models/stock_move.py:74 | move.purchase_line_id = line[:1] | FACT | purchase_stock installed | — | When a transfer linked to an order has a moved line with no order line, from supplier or transit, or returned to the supplier with refund, the order line is set on the move (or a new order line is created, lines 76-92). | N-U07R2-007 |
| VDR-U07R2-C017 | GRV-F04 | purchase_stock/models/stock_move.py:17 | ondelete='set null' | FACT | purchase_stock installed | — | The move field purchase_line_id is declared without copy=False (the default copy behaviour of a many-to-one applies). | N-U07R2-007 |
| VDR-U07R2-C018 | GRV-F04 | purchase_stock/models/stock_move.py:68 | move.location_dest_id.usage == 'supplier' and move.to_refund | INFERENCE | purchase_stock installed | RT | INFERENCE from C016 and C017 (and VDR-U07R1-C005): return-to-vendor moves can carry the order line, so they can be among the moves scanned at line 186; whether they do in practice needs execution. | N-U07R2-007 |
| VDR-U07R2-C019 | GRV-F03 | purchase_stock/models/purchase_order_line.py:64 | move.state == 'done' | FACT | purchase_stock installed | — | Received quantity of a stock-based order line is the sum of done moves; a done purchase-return move subtracts when it has no origin returned move or has the refund flag (lines 65-67; same as VDR-U07-C074, C077). | N-U07R2-008 |
| VDR-U07R2-C020 | GRV-F03 | purchase_stock/models/purchase_order_line.py:74 | not move._should_count_for_quantity_received() | FACT | purchase_stock installed | RT | The line-74 condition parses as (origin returned move exists and is a purchase return and no refund flag) or (not should-count); when true the move is skipped for received quantity. Effect per move kind needs execution. | N-U07R2-008 |
| VDR-U07R2-C021 | GRV-F03 | stock/models/stock_move.py:373 | location_usage in ('supplier', 'transit') | FACT | stock installed | — | The base test for counting a move as received is that its source location usage is supplier or transit. | N-U07R2-008 |
| VDR-U07R2-C022 | GRV-F03 | mrp_subcontracting/models/stock_move.py:211 | self.is_subcontract | FACT | mrp_subcontracting installed (discovered) | — | mrp_subcontracting extends the test with subcontract moves and moves from subcontracting locations. | N-U07R2-008 |
| VDR-U07R2-C023 | GRV-F03 | purchase_stock/models/purchase_order_line.py:55 | def _prepare_qty_received | INFERENCE | purchase_stock installed | — | INFERENCE from reading lines 55-80 and a grep of callers of _get_value_from_account_move (stock_account line 403 and two subcontracting modules): received quantity does not depend on the bill-based valuation; the double negation therefore has no effect on received quantity. | N-U07R2-008 |
| VDR-U07R2-C024 | GRV-F04 | stock_account/models/stock_move.py:321 | move.value = move.sudo()._get_value() | FACT | stock_account installed | — | The valuation result is stored in the value of incoming moves (value only; no quantity is written). | N-U07R2-002 |
| VDR-U07R2-C025 | GRV-F04 | purchase_stock/models/stock_move.py:194 | other_candidates_qty += move._get_valued_qty() | INFERENCE | lot-valuated or lot-tracked product | — | INFERENCE: the valued quantity is requested without a lot argument, so the allocation of billed quantity is per move, not per lot. | N-U07R2-009 |
| VDR-U07R2-C026 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock.py:335 | purchase_order_ids = fields.Many2many | FACT | purchase_stock installed | — | The lot model gets non-stored, read-only computed fields purchase_order_ids and purchase_order_count. | N-U07R2-010 |
| VDR-U07R2-C027 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock.py:338 | @api.depends('name') | INFERENCE | purchase_stock installed | — | INFERENCE: the fields are not stored, so the orders are recomputed whenever read; no link record is persisted. | N-U07R2-010 |
| VDR-U07R2-C028 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock.py:341 | ('state', '=', 'done') | FACT | purchase_stock installed | — | For the lots in the recordset the compute searches move lines of those lots whose state is done (with the caller's rights). | N-U07R2-011 |
| VDR-U07R2-C029 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock.py:343 | location_id.usage in ('supplier', 'transit') | FACT | purchase_stock installed | — | A move line is kept only when the transfer's source location usage is supplier or transit and the move has an order line with an order. | N-U07R2-011 |
| VDR-U07R2-C030 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock.py:344 | purchase_orders[move_line.lot_id.id] | FACT | purchase_stock installed | — | The orders found are collected per lot; each lot gets the union of its orders and their count. | N-U07R2-011 |
| VDR-U07R2-C031 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock.py:349 | def action_view_po | FACT | purchase_stock installed | — | action_view_po opens the Purchase Orders window action with the domain replaced by the lot's order ids and creation disabled in the context. | N-U07R2-013 |
| VDR-U07R2-C032 | FUNCTION MAPPING REQUIRED | purchase_stock/views/stock_lot_views.xml:11 | purchase_order_count == 0 or not display_complete | FACT | purchase_stock installed | — | The lot form gets a Purchases stat button before the first button, hidden when the count is zero or the form is not complete; no groups attribute. | N-U07R2-013 |
| VDR-U07R2-C033 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:151 | prod_lot.display_complete = prod_lot.id | FACT | stock installed | — | The display-complete flag is true for saved lots (or when set in the context). | N-U07R2-013 |
| VDR-U07R2-C034 | FUNCTION MAPPING REQUIRED | purchase_stock/security/ir.model.access.csv:2 | access_purchase_order_stock_worker | FACT | purchase_stock installed | — | The stock user group has read-only access on purchase orders (line 2) and purchase order lines (line 3). DB: the two rows exist with read only. | N-U07R2-013 |
| VDR-U07R2-C035 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock.py:343 | move.purchase_line_id.order_id | INFERENCE | purchase_stock installed | RT | INFERENCE from C028 to C030: the link is receipt-side only (a return to the vendor starts in an internal location and is not counted; a move without a transfer is not counted), it is not removed when the lot is later returned, and a lot name used in several receipts links all their orders. | N-U07R2-012 |
| VDR-U07R2-C036 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock.py:343 | location_id.usage in ('supplier', 'transit') | INFERENCE | stock_dropshipping installed | RT | INFERENCE: a drop-shipping transfer starts in a supplier location (see stock_account _is_dropshipped, lines 593-594), so lots on drop-shipped lines are also linked to the order. | N-U07R2-012 |
| VDR-U07R2-C037 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock.py:335 | purchase_order_ids = fields.Many2many | OBSERVATION | restored DB | — | DB: no stock lots, no stock move lines, no orders; the link could not be reconciled with data. | N-U07R2-014 |
| VDR-U07R2-C038 | FUNCTION MAPPING REQUIRED | purchase_stock/models/stock.py:332 | class StockLot(models.Model) | UNKNOWN | purchase_stock installed | — | UNKNOWN — EVIDENCE INSUFFICIENT: reverse traceability (from an order to its lots) and lot-valuated bill allocation are not part of these two sites and were not studied here; hand-off to U09 / U10. | N-U07R2-014 |
