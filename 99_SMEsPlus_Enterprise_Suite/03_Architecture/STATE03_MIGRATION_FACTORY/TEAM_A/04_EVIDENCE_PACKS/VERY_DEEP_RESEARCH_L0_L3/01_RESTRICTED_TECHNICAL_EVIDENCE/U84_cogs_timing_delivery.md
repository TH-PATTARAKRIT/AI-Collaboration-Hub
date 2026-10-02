# U84 — COGS Timing at Delivery (L3/L7/L8)
**Unit**: U84
**Phase**: Second-Pass Depth Closure — P1 Core Business
**Scope**: Delivery validate→_action_done→_create_account_move; COGS account determination; AVCO vs FIFO timing; lock date interaction; analytic distribution
**Modules**: stock_account, stock, sale_stock
**Function-IDs targeted**: SDV-F05, C1
**L-levels**: L3, L7, L8
**Proof layers**: P2, P3, P4
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: U05, U10, U76, U80

## Research Summary

### Call chain: button_validate → COGS account.move

1. `stock.picking.button_validate()` (stock/models/stock_picking.py:1420) performs sanity checks, runs `_pre_action_done_hook()` which may pause for backorder wizard user input, then calls `picking._action_done()` synchronously.
2. `stock_picking._action_done()` (stock/models/stock_picking.py:1263) collects todo_moves and calls `todo_moves._action_done()` at line 1280.
3. `stock_account.StockMove._action_done()` (stock_account/models/stock_move.py:177) overrides the base: first calls `moves_out._set_value()` at line 182 (BEFORE super), then calls `super()._action_done()` at line 183 which writes `state='done'` in the base class at stock/models/stock_move.py:2290, then calls `moves._create_account_move()` at line 187 (AFTER state='done').
4. `_create_account_move()` (stock_account/models/stock_move.py:193) creates a single account.move for the batch, dated today (not the delivery date), and calls `account_move._post()` at line 217 immediately — no draft state.

### COGS account determination (outgoing delivery)

`_get_account_move_line_vals()` (line 229) checks `location_id.valuation_account_id` first (line 230):
- If truthy (return/reversal path): debit = stock_valuation account, credit = location_id.valuation_account_id
- Standard delivery (else branch): debit = `location_dest_id.valuation_account_id` (line 234) = the customer location's configured COGS account; credit = `product._get_product_accounts()['stock_valuation']` (line 235) = the product category's stock valuation (inventory) account

### AVCO vs FIFO timing

Both computed inside `_set_value()` at line 182, BEFORE `super()._action_done()` sets state='done'.
- AVCO/standard: `move.value = product.standard_price * _get_valued_qty()` (line 351)
- FIFO: `move.value = product._run_fifo(valued_qty)` with context `fifo_qty_already_processed` (line 348)
No timing difference in when the COGS account.move is posted; the difference is only in value computation.

### Date and lock date

COGS account.move date = `context.get('force_period_date') or fields.Date.context_today(self)` (line 214). This is today's date — NOT the delivery's `scheduled_date` or `date_done`. Even backdated deliveries produce a COGS entry dated today. `account_move._post()` (account/models/account_move.py:5706) auto-bumps the date forward to the next open day if it falls in a locked period; no hard error for stock valuation entries.

### sale.order.line → stock.move → account.move linkage

`stock.move.sale_line_id` (Many2one → sale.order.line) is defined at sale_stock/models/stock.py:17. The created account.move is linked back via `stock.move.account_move_id` (defined at stock_account/models/stock_move.py:51). The account.move itself has no direct field pointing to sale.order.

### Analytic distribution

`_get_analytic_distribution()` (stock_account/models/stock_move.py:255) returns `{}` in the base module — no analytic_distribution is written to COGS account.move.line in a standard stock_account setup. Analytic tracking uses separate `account.analytic.line` records linked via `analytic_account_line_ids` (line 50), created by `_create_analytic_move()` (line 190). When sale_stock is installed, `_prepare_procurement_values()` (sale_stock/models/stock.py:143) copies `sale_line_id.analytic_distribution` to the procurement context for chained (MTO) moves, but this does not override `_get_analytic_distribution()` for COGS line computation.

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U84-001 | SDV-F05 | stock/models/stock_picking.py:1420 | def button_validate(self): | DEF | | | button_validate() is the public synchronous entry point for delivery validation on stock.picking; no async queue involved | NR-U84-001 |
| U84-002 | SDV-F05 | stock/models/stock_picking.py:1436 | _pre_action_done_hook() | CALL | backorder/lot wizard needed | | _pre_action_done_hook() runs pre-validation wizards; if result is not True the wizard is returned to the user and _action_done() is not called until user responds | NR-U84-002 |
| U84-003 | SDV-F05 | stock/models/stock_picking.py:1448 | pickings_not_to_backorder | CALL | after pre-hook returns True | | picking._action_done() called synchronously; no job queue | NR-U84-003 |
| U84-004 | SDV-F05 | stock/models/stock_picking.py:1280 | todo_moves._action_done( | CALL | | | stock_picking._action_done() delegates to stock.move._action_done() on all todo_moves | NR-U84-004 |
| U84-005 | SDV-F05 | stock_account/models/stock_move.py:182 | moves_out._set_value() | CALL | move._is_out() is True | C1 | moves_out._set_value() is called BEFORE super()._action_done(); COGS value computed before state='done' is written | NR-U84-005 |
| U84-006 | SDV-F05 | stock/models/stock_move.py:2290 | 'state': 'done', 'date' | ASSIGN | in base _action_done | C1 | state='done' written by moves_todo.write() in base stock.move._action_done() at line 2290, which is called via super() at stock_account/models/stock_move.py:183; this happens BEFORE _create_account_move() at line 187 | NR-U84-006 |
| U84-007 | SDV-F05 | stock_account/models/stock_move.py:187 | moves._create_account_move() | CALL | after super()._action_done() | C1 | _create_account_move() is called at line 187, after state='done' has been written; exact call site for COGS entry creation | NR-U84-007 |
| U84-008 | SDV-F05 | stock_account/models/stock_move.py:193 | def _create_account_move(self | DEF | | | _create_account_move() iterates self; calls _should_create_account_move() per move; accumulates aml_vals_list; creates one account.move for the whole batch | NR-U84-008 |
| U84-009 | SDV-F05 | stock_account/models/stock_move.py:214 | force_period_date | ASSIGN | | C1 | account.move date = context.get('force_period_date') or fields.Date.context_today(); NOT the delivery's scheduled_date or date_done; backdated deliveries use today's accounting date | NR-U84-009 |
| U84-010 | SDV-F05 | stock_account/models/stock_move.py:217 | account_move._post() | CALL | | C1 | account_move._post() called immediately after create; COGS entry posted in the same transaction, never left in draft | NR-U84-010 |
| U84-011 | SDV-F05 | stock_account/models/stock_move.py:664 | is_storable and self.is_valued | GUARD | | | _should_create_account_move() requires: product.is_storable=True AND is_valued=True AND (location_dest_id.valuation_account_id OR location_id.valuation_account_id) AND non-zero quantity AND product.valuation='real_time' | NR-U84-011 |
| U84-012 | SDV-F05 | stock_account/models/stock_move.py:234 | debit_acc = self.location_dest | ASSIGN | location_id has no valuation_account_id | C1 | outgoing delivery: COGS debit account = location_dest_id.valuation_account_id (customer location's configured COGS account) | NR-U84-012 |
| U84-013 | SDV-F05 | stock_account/models/stock_move.py:235 | credit_acc = self.product_id | ASSIGN | location_id has no valuation_account_id | C1 | outgoing delivery: inventory credit account = product._get_product_accounts()['stock_valuation'] = product category's property_stock_valuation_account_id | NR-U84-013 |
| U84-014 | SDV-F05 | stock_account/models/stock_move.py:351 | product_id.standard_price | CALC | cost_method != 'fifo' | C1 | AVCO/standard: move.value = product.standard_price (at moment _set_value() executes, before state='done') × _get_valued_qty() | NR-U84-014 |
| U84-015 | SDV-F05 | stock_account/models/stock_move.py:348 | ._run_fifo(valued_qty) | CALC | cost_method == 'fifo' | C1 | FIFO: move.value = product._run_fifo(valued_qty) consuming oldest FIFO cost layers; fifo_qty_already_processed context tracks batch qty to avoid double-consumption when multiple out-moves validated together | NR-U84-015 |
| U84-016 | SDV-F05 | account/models/account_move.py:5706 | _get_accounting_date( | ASSIGN | date in locked period | | _post() auto-bumps COGS account.move date to next open period if it falls in a locked period; no hard UserError for stock valuation entries dated today | NR-U84-016 |
| U84-017 | SDV-F05 | sale_stock/models/stock.py:17 | sale_line_id = fields.Many2one | SCHEMA | sale_stock installed | | stock.move.sale_line_id Many2one → sale.order.line provides the link from each delivery move back to the originating sale order line | NR-U84-017 |
| U84-018 | SDV-F05 | stock_account/models/stock_move.py:51 | account_move_id = fields.Many | SCHEMA | | | stock.move.account_move_id Many2one → account.move links each valued delivery move to its COGS entry; the account.move has no direct link back to sale.order | NR-U84-018 |
| U84-019 | SDV-F05 | stock_account/models/stock_move.py:255 | _get_analytic_distribution | RETURN | | | _get_analytic_distribution() returns {} in stock_account base; COGS account.move.line has no analytic_distribution in base configuration | NR-U84-019 |
| U84-020 | SDV-F05 | sale_stock/models/stock.py:143 | analytic_distribution'] = self | ASSIGN | sale_line_id.analytic_distribution truthy | | _prepare_procurement_values() copies sale.order.line.analytic_distribution to procurement context for chained MTO moves; does not override _get_analytic_distribution() for COGS line computation | NR-U84-020 |
| U84-021 | SDV-F05 | stock_account/models/stock_move.py:190 | ._create_analytic_move() | CALL | | | analytic tracking for delivery moves uses separate account.analytic.line records (via analytic_account_line_ids field) created by _create_analytic_move(); not analytic_distribution on COGS account.move.line | NR-U84-021 |
