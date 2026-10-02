# U77 — Full Procure-to-Pay Chain (L5/L11)

**Unit**: U77
**Phase**: Second-Pass Depth Closure — P1 Core Business
**Scope**: PO confirm → receipt validate → valuation entry → vendor bill → post → payment → reconcile
**Modules**: purchase, purchase_stock, stock, stock_account, account, account_payment
**L-levels**: L4, L5, L11
**Proof layers**: P4, P5
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: C02, U06, U07, U72, U74, U76

---

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U77-001 | NEW:U77-F01 | purchase/models/purchase_order.py:625 | def button_confirm(self): | FLOW | state in ['draft','sent'] | | button_confirm() iterates orders; if approval allowed calls button_approve(), else sets state='to approve' | NR-U77-001 |
| U77-002 | NEW:U77-F02 | purchase/models/purchase_order.py:615 | def button_approve(self, force=False): | ASSIGN | _approval_allowed() | | button_approve() writes state='purchase' and date_approve=Datetime.now() on filtered records | NR-U77-002 |
| U77-003 | NEW:U77-F03 | purchase_stock/models/purchase_order.py:179 | def button_approve(self, force=False): | OVERRIDE | state='purchase' after super | | purchase_stock overrides button_approve(); after calling super, invokes self._create_picking() | NR-U77-003 |
| U77-004 | NEW:U77-F04 | purchase_stock/models/purchase_order.py:377 | def _create_picking(self): | FLOW | po.state=='purchase', product.type=='consu' | | _create_picking() creates stock.picking via _prepare_picking(), then calls order_line._create_stock_moves(picking), moves._action_confirm(), moves._action_assign() | NR-U77-004 |
| U77-005 | NEW:U77-F05 | purchase_stock/models/purchase_order.py:360 | def _prepare_picking(self): | RETURN | | | _prepare_picking() returns dict with picking_type_id, partner_id, location_id=partner.property_stock_supplier, location_dest_id from _get_destination_location(), state='draft' | NR-U77-005 |
| U77-006 | NEW:U77-F06 | purchase_stock/models/purchase_order_line.py:364 | def _create_stock_moves(self, picking): | CALL | | | _create_stock_moves() calls _prepare_stock_moves(picking) for each non-display line and batch-creates stock.move records | NR-U77-006 |
| U77-007 | NEW:U77-F07 | purchase_stock/models/purchase_order_line.py:303 | 'purchase_line_id': self.id, | ASSIGN | | | _prepare_stock_moves() sets purchase_line_id=self.id on each stock.move, linking move to PO line | NR-U77-007 |
| U77-008 | NEW:U77-F08 | purchase_stock/models/purchase_order.py:386 | StockPicking.with_user(SUPERUSER_ID).create(res) | CALL | not pickings | | When no existing open picking, _create_picking creates new stock.picking as SUPERUSER to bypass access checks | NR-U77-008 |
| U77-009 | NEW:U77-F09 | purchase_stock/models/purchase_order_line.py:25 | qty_received_method = fields.Selection(selection_add=[('stock_moves' | CONFIG | product.type=='consu' | | purchase_stock adds 'stock_moves' to qty_received_method selection; for consumable products this method drives qty_received | NR-U77-009 |
| U77-010 | NEW:U77-F10 | purchase_stock/models/purchase_order_line.py:37 | def _compute_qty_received_method(self): | FLOW | product.type=='consu' | | _compute_qty_received_method sets qty_received_method='stock_moves' for consumable (storable) products | NR-U77-010 |
| U77-011 | NEW:U77-F11 | purchase_stock/models/purchase_order_line.py:51 | move_ids.state', 'move_ids.product_uom', 'move_ids.quantity | TRIGGER | | | qty_received recomputes whenever linked stock.move state/quantity changes; triggers invoice_status recompute on PO | NR-U77-011 |
| U77-012 | NEW:U77-F12 | purchase_stock/models/purchase_order_line.py:59 | if line.qty_received_method == 'stock_moves': | FLOW | method=='stock_moves' | | _prepare_qty_received() sums done move quantities (excluding purchase returns unless to_refund) via _get_po_line_moves() | NR-U77-012 |
| U77-013 | NEW:U77-F13 | stock_account/models/stock_move.py:177 | def _action_done(self, cancel_backorder=False): | FLOW | | | _action_done: calls _set_value() for out moves before super, then _set_value() for in moves after super, then _create_account_move() for all | NR-U77-013 |
| U77-014 | NEW:U77-F14 | stock_account/models/stock_move.py:185 | moves_in = moves.filtered(lambda m: m.is_in or m.is_dropship) | FLOW | | | After super()._action_done(), incoming moves (is_in=True) are identified and _set_value() is called on them | NR-U77-014 |
| U77-015 | NEW:U77-F15 | stock_account/models/stock_move.py:193 | def _create_account_move(self): | FLOW | _should_create_account_move() | | _create_account_move iterates moves; if _should_create_account_move() returns True, collects aml_vals and creates a single account.move via sudo | NR-U77-015 |
| U77-016 | NEW:U77-F16 | stock_account/models/stock_move.py:659 | def _should_create_account_move(self): | GUARD | real_time valuation | | _should_create_account_move returns True only if product is storable, is_valued=True, valuation='real_time', AND (location_dest_id.valuation_account_id OR location_id.valuation_account_id) | NR-U77-016 |
| U77-017 | NEW:U77-F17 | stock_account/models/stock_move.py:664 | self.location_dest_id.valuation_account_id or self.location_id.valuation_account_id | GUARD | standard supplier-to-stock receipt | | For standard P2P receipt (supplier location to internal stock location), neither location has valuation_account_id set by default; _should_create_account_move returns False; NO account.move at receipt | NR-U77-017 |
| U77-018 | NEW:U77-F18 | stock_account/models/stock_move.py:292 | def _set_value(self, correction_quantity=None): | FLOW | move.is_in=True | | _set_value() for incoming moves sets move.value = _get_value() which resolves via priority: bill amount, then PO quotation price, then standard_price | NR-U77-018 |
| U77-019 | NEW:U77-F19 | stock_account/models/stock_move.py:416 | quotation_data = self._get_value_from_quotation(remaining_qty, at_date) | FLOW | no bill posted yet | | When vendor bill not yet posted, _get_value_data uses _get_value_from_quotation; purchase_stock override returns PO line price * qty as the move value | NR-U77-019 |
| U77-020 | NEW:U77-F20 | purchase_stock/models/stock_move.py:233 | purchase_line_id.with_context(conversion_date=self.date)._get_stock_move_price_unit | CALC | no bill yet | | _get_value_from_quotation in purchase_stock uses purchase_line_id's stock move price unit (converted to company currency at move date) as receipt valuation | NR-U77-020 |
| U77-021 | NEW:U77-F21 | purchase/models/purchase_order.py:760 | def action_create_invoice(self, attachment_ids=False): | FLOW | | | action_create_invoice iterates PO lines, calls _prepare_invoice() and _prepare_account_move_line(), batch-creates account.move records with move_type='in_invoice' | NR-U77-021 |
| U77-022 | NEW:U77-F22 | purchase/models/purchase_order.py:809 | self.env['account.move'].with_context(default_move_type='in_invoice') | ASSIGN | | | Vendor bills are created with move_type='in_invoice' via context default_move_type | NR-U77-022 |
| U77-023 | NEW:U77-F23 | purchase/models/purchase_order.py:925 | def _prepare_invoice(self): | RETURN | | | _prepare_invoice() returns dict with move_type from context, partner_id, currency_id, fiscal_position_id, invoice_origin=self.name, invoice_payment_term_id | NR-U77-023 |
| U77-024 | NEW:U77-F24 | stock_account/models/account_move_line.py:13 | def _compute_account_id(self): | OVERRIDE | is_purchase_document and real_time | | _compute_account_id override sets invoice line account_id to accounts['stock_valuation'] for storable products with real_time valuation on purchase documents | NR-U77-024 |
| U77-025 | NEW:U77-F25 | stock_account/models/account_move_line.py:23 | if line.product_id.valuation == 'real_time' and accounts['stock_valuation']: | GUARD | | | Vendor bill line account assignment to stock_valuation is conditional: product must have real_time valuation and the stock_valuation account must be configured | NR-U77-025 |
| U77-026 | NEW:U77-F26 | purchase/models/account_invoice.py:22 | purchase_id = fields.Many2one('purchase.order' | SCHEMA | | | account.move has a non-stored purchase_id field linking it to the originating PO; the link is maintained via invoice_line_ids.purchase_line_id.order_id | NR-U77-026 |
| U77-027 | NEW:U77-F27 | purchase/models/account_invoice.py:102 | @api.depends('line_ids.purchase_line_id') | TRIGGER | | | purchase_order_count on vendor bill is computed from line_ids.purchase_line_id.order_id, showing how many POs contributed to the bill | NR-U77-027 |
| U77-028 | NEW:U77-F28 | purchase/models/purchase_order.py:46 | @api.depends('state', 'order_line.qty_to_invoice') | TRIGGER | | | invoice_status on PO is a stored computed field depending on state and order_line.qty_to_invoice; recomputes when receipt quantities change | NR-U77-028 |
| U77-029 | NEW:U77-F29 | purchase/models/purchase_order_line.py:179 | if line.product_id.purchase_method == 'purchase': | FLOW | | | qty_to_invoice for 'purchase' method = product_qty minus qty_invoiced; for 'receive' method = qty_received minus qty_invoiced | NR-U77-029 |
| U77-030 | NEW:U77-F30 | purchase/models/purchase_order.py:54 | not float_is_zero(line.qty_to_invoice, precision_digits=precision) | GUARD | state=='purchase' | | invoice_status='to invoice' when any non-display line has qty_to_invoice not zero; 'invoiced' when all qty_to_invoice zero and invoice_ids exists | NR-U77-030 |
| U77-031 | NEW:U77-F31 | account/models/account_move.py:6180 | def action_post(self): | FLOW | | | action_post() calls _post(soft=False) to post vendor bill; creates journal entries and sets state='posted' | NR-U77-031 |
| U77-032 | NEW:U77-F32 | purchase_stock/models/account_invoice.py:113 | def _post(self, soft=True): | OVERRIDE | not move_reverse_cancel | | purchase_stock._post() calls _stock_account_prepare_anglo_saxon_in_lines_vals() before super()._post() to add Anglo-Saxon price difference lines | NR-U77-032 |
| U77-033 | NEW:U77-F33 | purchase_stock/models/account_invoice.py:12 | def _stock_account_prepare_anglo_saxon_in_lines_vals(self): | FLOW | move_type in in_invoice/in_refund and anglo_saxon_accounting | | Adds price difference lines to vendor bill only when Anglo-Saxon accounting enabled AND product cost_method is standard; creates debit to price_diff_account and credit to stock_valuation | NR-U77-033 |
| U77-034 | NEW:U77-F34 | purchase_stock/models/account_invoice.py:37 | or not move.company_id.anglo_saxon_accounting: | GUARD | | | Anglo-Saxon price difference lines are skipped entirely if not in_invoice/in_refund or if company.anglo_saxon_accounting is False | NR-U77-034 |
| U77-035 | NEW:U77-F35 | stock_account/models/account_move.py:29 | def _post(self, soft=True): | OVERRIDE | | | stock_account._post() calls _stock_account_prepare_realtime_out_lines_vals() for COGS on outgoing invoices, then super(); after super calls _set_value() on linked incoming stock moves | NR-U77-035 |
| U77-036 | NEW:U77-F36 | stock_account/models/account_move.py:42 | .filtered(lambda m: m.is_in or m.is_dropship)._set_value() | CALL | after _post | | After bill is posted, _set_value() is called on linked incoming stock moves; _get_value_from_account_move now returns bill value, updating move.value to billed amount | NR-U77-036 |
| U77-037 | NEW:U77-F37 | purchase_stock/models/stock_move.py:169 | for aml in self.purchase_line_id.invoice_lines: | FLOW | invoice posted | | _get_value_from_account_move in purchase_stock iterates invoice_lines on purchase_line_id; for in_invoice lines sums (price_subtotal / currency_rate) as company currency value | NR-U77-037 |
| U77-038 | NEW:U77-F38 | account/models/account_move.py:5757 | to_post.write({ | ASSIGN | validation passed | | _post() sets state='posted' and posted_before=True on all validated moves; triggers downstream recomputes including payment_state on vendor bills | NR-U77-038 |
| U77-039 | NEW:U77-F39 | purchase_stock/tests/test_account.py:36 | 'account_id': self.account_stock_valuation.id, 'debit': 12.0, 'credit': 0.0 | CHECK | real_time standard auto | | Test confirms vendor bill journal entry for real_time standard costing: DR stock_valuation=bill_amount, CR accounts_payable=bill_amount | NR-U77-039 |
| U77-040 | NEW:U77-F40 | purchase_stock/tests/test_account.py:52 | 'account_id': self.account_price_diff.id, 'debit': 2.0, 'credit': 0.0 | CHECK | Anglo-Saxon price diff | | Test confirms Anglo-Saxon bill entry: includes DR price_diff_account for difference (bill_price minus standard_cost), CR stock_valuation to offset | NR-U77-040 |
| U77-041 | NEW:U77-F41 | account/models/account_payment.py:99 | ('outbound', 'Send'), | CONFIG | | | payment_type='outbound' for vendor payments (send money); outbound payment has liquidity_amount_currency = negative amount | NR-U77-041 |
| U77-042 | NEW:U77-F42 | account/models/account_payment.py:353 | liquidity_amount_currency = -self.amount | CALC | payment_type=='outbound' | | Outbound payment: liquidity line balance = negative amount (credit on bank/outstanding account) | NR-U77-042 |
| U77-043 | NEW:U77-F43 | account/models/account_payment.py:642 | pay.destination_account_id = pay.partner_id.with_company(pay.company_id).property_account_payable_id | ASSIGN | partner_type=='supplier' | | For supplier payments, destination_account_id = partner.property_account_payable_id (accounts payable) | NR-U77-043 |
| U77-044 | NEW:U77-F44 | account/models/account_payment.py:294 | 'account_id': self.outstanding_account_id.id, | ASSIGN | | | Liquidity line uses outstanding_account_id (bank/outstanding account); counterpart uses destination_account_id (payable) | NR-U77-044 |
| U77-045 | NEW:U77-F45 | account/models/account_payment.py:300 | def _prepare_move_counterpart_lines(self, default_values): | FLOW | | | Counterpart line for outbound vendor payment: account_id = destination_account_id (payable), balance = positive amount (debit on payable) | NR-U77-045 |
| U77-046 | NEW:U77-F46 | account/wizard/account_payment_register.py:1297 | wizard._post_payments(to_process, edit_mode=edit_mode) | FLOW | | | _create_payments() in wizard posts payments first, then calls _reconcile_payments(); both steps are always executed sequentially | NR-U77-046 |
| U77-047 | NEW:U77-F47 | account/wizard/account_payment_register.py:1187 | def _reconcile_payments(self, to_process, edit_mode=False): | FLOW | | | _reconcile_payments() filters payment lines on payable account_type and reconciled=False, then calls .reconcile() on combined payment + invoice payable lines | NR-U77-047 |
| U77-048 | NEW:U77-F48 | account/wizard/account_payment_register.py:1209 | (payment_lines + lines)\ | CALL | | | Reconciliation matches payment payable aml against vendor bill payable aml on the same account_id, creating account.partial.reconcile | NR-U77-048 |
| U77-049 | NEW:U77-F49 | account/models/account_move_line.py:3142 | def reconcile(self): | CALL | | | reconcile() calls _reconcile_plan([self]); creates account.partial.reconcile and account.full.reconcile when fully cleared; sets amount_residual=0 | NR-U77-049 |
| U77-050 | NEW:U77-F50 | account/models/account_payment.py:454 | reconciled_bill_ids.payment_state', 'move_id.line_ids.amount_residual | TRIGGER | | | payment.state recomputes when bill payment_state or liquidity line amount_residual changes; transitions in_process to paid when fully reconciled | NR-U77-050 |
| U77-051 | NEW:U77-F51 | account/models/account_payment.py:463 | move.company_currency_id.is_zero(sum(liquidity.mapped('amount_residual'))) | CALC | | | Payment state becomes 'paid' when sum of liquidity line amount_residual is zero (bank statement reconciled) | NR-U77-051 |
| U77-052 | NEW:U77-F52 | purchase/models/purchase_order.py:59 | order.invoice_status = 'to invoice' | GUARD | state=='purchase' | | PO invoice_status becomes 'invoiced' when all non-display lines have qty_to_invoice==0 AND invoice_ids is not empty | NR-U77-052 |
| U77-053 | NEW:U77-F53 | purchase_stock/models/stock_move.py:15 | purchase_line_id = fields.Many2one( | SCHEMA | | | stock.move.purchase_line_id is a Many2one to purchase.order.line; the FK that connects incoming stock moves to PO lines and drives qty_received computation | NR-U77-053 |
| U77-054 | NEW:U77-F54 | purchase_stock/models/account_invoice.py:119 | def _stock_account_get_last_step_stock_moves(self): | OVERRIDE | move_type=='in_invoice' | | For in_invoice, _stock_account_get_last_step_stock_moves returns done stock moves where location_id.usage=='supplier' (incoming receipt moves) | NR-U77-054 |

---

## Cross-Chain Comparison: P2P vs O2C

| Step | P2P (this unit) | O2C (U76 parallel) |
|---|---|---|
| Confirm | PO button_confirm → state='purchase' | SO button_confirm → state='sale' |
| Stock doc | stock.picking (incoming, type=IN) | stock.picking (outgoing, type=OUT) |
| Validate | _action_done on incoming move | _action_done on outgoing move |
| Valuation entry at validate | NONE for standard locations | NONE for standard locations |
| Value source | PO line price (quotation) → bill price when posted | Product standard_price / FIFO |
| Accounting entry trigger | Vendor bill _post() | Customer invoice _post() |
| DR at accounting entry | stock_valuation (via _compute_account_id) | COGS / stock_variation (via _stock_account_prepare_realtime_out_lines_vals) |
| CR at accounting entry | accounts_payable | stock_valuation |
| Payment | Outbound: DR payable, CR bank | Inbound: DR bank, CR receivable |
| Reconcile | Payable line matched | Receivable line matched |

---

## Anglo-Saxon Accounting Note

When `company.anglo_saxon_accounting = True` and `product.cost_method == 'standard'`:
- `_stock_account_prepare_anglo_saxon_in_lines_vals()` in purchase_stock/models/account_invoice.py:12 adds two extra lines to the vendor bill:
  - DR `property_price_difference_account_id` (expense/variance) for the difference (bill_price − standard_cost) × qty
  - CR stock_valuation account (to offset the excess/shortfall on the bill line)
- This ensures the stock_valuation account reflects only the standard cost, not the billed price

---

## Account Entry Summary (real_time, standard costing)

| Chain Step | Account Entry |
|---|---|
| PO confirm | No accounting entry |
| Receipt validate | No accounting entry (standard locations; _should_create_account_move returns False) |
| SVL value set at receipt | move.value = PO line price × qty (from _get_value_from_quotation) |
| Vendor bill post (non-Anglo-Saxon) | DR stock_valuation = bill_amount; CR accounts_payable = bill_amount |
| Vendor bill post (Anglo-Saxon, std) | DR stock_valuation = bill_amount; CR payable = bill_amount; DR price_diff = diff; CR stock_valuation = diff |
| SVL update after bill post | move.value updated to billed amount via _get_value_from_account_move |
| Outbound payment | DR accounts_payable = payment; CR bank/outstanding = payment |
| Reconcile | Payable lines matched; amount_residual → 0; payment_state → 'paid' |
| PO invoice_status | 'invoiced' when all qty_to_invoice == 0 |
