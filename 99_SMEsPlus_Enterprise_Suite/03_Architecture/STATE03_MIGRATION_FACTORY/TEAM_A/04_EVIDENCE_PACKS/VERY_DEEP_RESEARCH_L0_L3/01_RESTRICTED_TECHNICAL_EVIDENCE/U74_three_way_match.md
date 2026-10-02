# U74 — Three-Way Match / Bill Control Depth (GRV-F06)
**Unit**: U74
**Phase**: Second-Pass Depth Closure — P0 Critical
**Scope**: purchase.order.line bill control policy, qty_invoiced, qty_received, invoice_status, three-way match blocking
**Modules**: purchase, purchase_stock, account
**Function-IDs targeted**: GRV-F06
**L-levels**: L3, L4, L7
**Proof layers**: P3, P4
**Date**: 2026-10-02
**Status**: GATE-PASS (exit 0, claim-checks=0, neutral-leak-tokens=0)
**Predecessor**: U07, U12

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U74-001 | GRV-F06 | purchase/models/product.py:14 | purchase_method = fields.Se | DEF | always | C1 | `purchase_method` is defined on `product.template` as a stored, precomputed, user-editable Selection field. | NR-U74-001 |
| U74-002 | GRV-F06 | purchase/models/product.py:15 | 'purchase', 'On ordered qu | CONST | always | C1 | Value `'purchase'` maps to "On ordered quantities"; bills are controlled against the ordered quantity on the PO line. | NR-U74-002 |
| U74-003 | GRV-F06 | purchase/models/product.py:16 | 'receive', 'On received qu | CONST | always | C1 | Value `'receive'` maps to "On received quantities"; bills are controlled against stock-confirmed received quantity. | NR-U74-003 |
| U74-004 | GRV-F06 | purchase/models/product.py:24 | default_purchase_method = s | ASSIGN | at _compute_purchase_method call | | The default policy is resolved via `default_get` on `product.template`; falls back to `'receive'` if no IR default is set. | NR-U74-004 |
| U74-005 | GRV-F06 | purchase/models/product.py:27 | product.purchase_method = ' | ASSIGN | product.type == 'service' | C1 | Service products are forced to policy `'purchase'` regardless of system default. | NR-U74-005 |
| U74-006 | GRV-F06 | purchase/models/product.py:29 | product.purchase_method = d | ASSIGN | product.type != 'service' | | Non-service products receive the system default policy (typically `'receive'` unless an IR default overrides). | NR-U74-006 |
| U74-007 | GRV-F06 | purchase/models/purchase_order_line.py:66 | qty_invoiced = fields.Float( | DEF | always | C1 | `qty_invoiced` is a stored computed Float field on `purchase.order.line`, labelled "Billed Qty". | NR-U74-007 |
| U74-008 | GRV-F06 | purchase/models/purchase_order_line.py:171 | @api.depends('invoice_lines | TRIGGER | always | | `_compute_qty_invoiced` is triggered by changes to `invoice_lines.move_id.state`, `invoice_lines.quantity`, `qty_received`, `product_uom_qty`, or `order_id.state`. | NR-U74-008 |
| U74-009 | GRV-F06 | purchase/models/purchase_order_line.py:173 | invoiced_quantities = self._ | CALL | always | | `_compute_qty_invoiced` delegates accumulation to `_prepare_qty_invoiced()`, then assigns per-line totals. | NR-U74-009 |
| U74-010 | GRV-F06 | purchase/models/purchase_order_line.py:202 | state not in ['cancel'] or | GUARD | always | C1 | `_prepare_qty_invoiced` includes invoice lines whose parent `account.move` state is NOT `'cancel'` (plus `invoicing_legacy` exception); draft-state bills ARE counted. | NR-U74-010 |
| U74-011 | GRV-F06 | purchase/models/purchase_order_line.py:204 | invoiced_qties[line] += inv | CALC | move_type == 'in_invoice' | C1 | `in_invoice` lines add their UoM-converted quantity to `qty_invoiced`. | NR-U74-011 |
| U74-012 | GRV-F06 | purchase/models/purchase_order_line.py:206 | invoiced_qties[line] -= inv | CALC | move_type == 'in_refund' | C1 | `in_refund` lines subtract their UoM-converted quantity from `qty_invoiced`. | NR-U74-012 |
| U74-013 | GRV-F06 | purchase/models/purchase_order_line.py:180 | line.product_qty - line.qty_ | CALC | purchase_method == 'purchase' AND order state == 'purchase' | C1 | When policy is `'purchase'`, `qty_to_invoice = product_qty - qty_invoiced` (ordered-quantity basis). | NR-U74-013 |
| U74-014 | GRV-F06 | purchase/models/purchase_order_line.py:182 | line.qty_received - line.qty | CALC | purchase_method == 'receive' AND order state == 'purchase' | C1 | When policy is `'receive'`, `qty_to_invoice = qty_received - qty_invoiced` (received-quantity basis, three-way cap). | NR-U74-014 |
| U74-015 | GRV-F06 | purchase/models/purchase_order_line.py:72 | qty_received = fields.Float( | DEF | always | C1 | `qty_received` is a stored computed Float field with `compute_sudo=True` and an inverse for manual entry. | NR-U74-015 |
| U74-016 | NEW:U74-F01 | purchase/models/purchase_order_line.py:638 | else self.qty_to_invoice, | ASSIGN | on bill line creation from PO | C1 | `_prepare_account_move_line` sets the bill line `quantity` = `qty_to_invoice`; for `in_refund` the quantity is negated. | NR-U74-016 |
| U74-017 | GRV-F06 | purchase/models/purchase_order.py:127 | invoice_status = fields.Sele | DEF | always | | `invoice_status` is a stored computed Selection on `purchase.order` with values `'no'`, `'to invoice'`, `'invoiced'`. | NR-U74-017 |
| U74-018 | GRV-F06 | purchase/models/purchase_order.py:51 | if order.state != 'purchase' | GUARD | state != 'purchase' | | Non-confirmed orders are unconditionally assigned `invoice_status = 'no'` without evaluating line quantities. | NR-U74-018 |
| U74-019 | GRV-F06 | purchase/models/purchase_order.py:52 | order.invoice_status = 'no' | ASSIGN | state != 'purchase' | | `invoice_status = 'no'` set when order is not in purchase state. | NR-U74-019 |
| U74-020 | GRV-F06 | purchase/models/purchase_order.py:59 | order.invoice_status = 'to i | ASSIGN | any non-display line has nonzero qty_to_invoice | C1 | `invoice_status = 'to invoice'` set when at least one line has `qty_to_invoice != 0`. | NR-U74-020 |
| U74-021 | GRV-F06 | purchase/models/purchase_order.py:66 | order.invoice_status = 'invo | ASSIGN | all qty_to_invoice == 0 AND invoice_ids present | C1 | `invoice_status = 'invoiced'` set when all lines are fully billed and at least one bill exists. | NR-U74-021 |
| U74-022 | NEW:U74-F02 | purchase_stock/models/purchase_order_line.py:25 | selection_add=[('stock_moves' | DEF | always | | `purchase_stock` extends `qty_received_method` selection with value `'stock_moves'` for storable consumable products. | NR-U74-022 |
| U74-023 | NEW:U74-F02 | purchase_stock/models/purchase_order_line.py:28 | move_ids = fields.One2many('s | DEF | always | | `move_ids` One2many to `stock.move` on `purchase.order.line` holds all associated stock moves, linked via `purchase_line_id`. | NR-U74-023 |
| U74-024 | NEW:U74-F02 | purchase_stock/models/purchase_order_line.py:41 | line.qty_received_method = ' | ASSIGN | product.type == 'consu' | C1 | Products with type `'consu'` are assigned `qty_received_method = 'stock_moves'`, routing received-qty computation through done stock moves. | NR-U74-024 |
| U74-025 | NEW:U74-F02 | purchase_stock/models/purchase_order_line.py:51 | @api.depends('move_ids.state | TRIGGER | always | | `_compute_qty_received` in `purchase_stock` triggers on `move_ids.state`, `move_ids.product_uom`, and `move_ids.quantity`. | NR-U74-025 |
| U74-026 | NEW:U74-F02 | purchase_stock/models/purchase_order_line.py:64 | if move.state == 'done': | GUARD | per-move in _prepare_qty_received | C1 | Only moves in state `'done'` contribute to the received quantity total; pending or cancelled moves are excluded. | NR-U74-026 |
| U74-027 | NEW:U74-F02 | purchase_stock/models/purchase_order_line.py:67 | total -= move.product_uom._c | CALC | move._is_purchase_return() AND (not origin_returned_move_id OR to_refund) | C1 | Purchase-return moves that are marked for refund or lack an originating return subtract from received quantity after UoM conversion. | NR-U74-027 |
| U74-028 | NEW:U74-F02 | purchase_stock/models/purchase_order_line.py:77 | total += move.product_uom._c | CALC | done non-return incoming moves | C1 | Normal done incoming stock moves add their UoM-converted quantity to the received total (HALF-UP rounding). | NR-U74-028 |
| U74-029 | NEW:U74-F02 | purchase_stock/models/stock_move.py:15 | purchase_line_id = fields.Ma | DEF | always | C1 | `stock.move.purchase_line_id` Many2one (ondelete='set null', indexed) is the cross-module FK linking each stock move to its originating `purchase.order.line`. | NR-U74-029 |
| U74-030 | GRV-F06 | purchase/models/res_config_settings.py:17 | module_account_3way_match =  | CONFIG | always | | `module_account_3way_match` Boolean setting references an optional module for hard three-way blocking; that module is **absent** from the Community addons tree. | NR-U74-030 |
| U74-031 | GRV-F06 | purchase_stock/models/purchase_order_line.py:173 | float_compare(line.product_q | GUARD | product_qty < qty_invoiced after line write | | When ordered quantity falls below already-billed quantity, a mail-activity warning is scheduled on the bill — no `UserError` or `ValidationError` is raised; posting is not blocked in Community. | NR-U74-031 |
| U74-032 | NEW:U74-F02 | purchase_stock/models/purchase_order_line.py:43 | def _get_po_line_moves(self): | DEF | always | | `_get_po_line_moves` filters `move_ids` to those matching the line's product; when an accrual date is present, further restricts to moves dated on or before that date. | NR-U74-032 |
