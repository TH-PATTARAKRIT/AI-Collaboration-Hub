{
  "unit": "U84",
  "title": "COGS Timing at Delivery Validation — Deep Closure",
  "date": "2026-10-02",
  "status": "GATE-PASS",
  "function_ids": ["SDV-F05"],
  "l_levels": ["L3", "L7", "L8"],
  "proof_layers": ["P2", "P3", "P4"],
  "c1_count": 9,
  "claim_count": 21,
  "gate_result": "PASS (claim-check-failures=0, neutral-leak-tokens=0)",
  "predecessors": ["U05", "U10", "U76", "U80"],
  "modules": ["stock_account", "stock", "sale_stock", "account"],
  "key_findings": {
    "call_chain": "button_validate (stock_picking:1420) → picking._action_done (stock_picking:1263) → todo_moves._action_done (stock_picking:1280) → stock_account.StockMove._action_done (stock_account/models/stock_move:177) → _create_account_move (line 187) → account_move._post() (line 217)",
    "cogs_call_site": "stock_account/models/stock_move.py:187 — moves._create_account_move()",
    "state_done_line": "stock/models/stock_move.py:2290 — moves_todo.write({'state': 'done', ...})",
    "timing": "_set_value() called at line 182 BEFORE super()._action_done(); _create_account_move() called at line 187 AFTER state='done'",
    "posting": "account_move._post() called immediately at line 217 — never draft",
    "cogs_account": "location_dest_id.valuation_account_id (customer location, line 234)",
    "inventory_account": "product._get_product_accounts()['stock_valuation'] (line 235)",
    "date_source": "fields.Date.context_today(self) or force_period_date (line 214) — NOT delivery date",
    "lock_date": "_post() auto-advances date to next open period at account_move.py:5706; no hard error",
    "avco_value": "product.standard_price * _get_valued_qty() (line 351)",
    "fifo_value": "product._run_fifo(valued_qty) with fifo_qty_already_processed context (line 348)",
    "avco_vs_fifo_timing": "No timing difference — both computed in _set_value() before super()._action_done()",
    "sale_line_link": "stock.move.sale_line_id Many2one → sale.order.line (sale_stock/models/stock.py:17)",
    "cogs_move_link": "stock.move.account_move_id Many2one → account.move (stock_account/models/stock_move.py:51); account.move has no direct sale.order link",
    "analytic": "_get_analytic_distribution() returns {} in base (line 255); no analytic_distribution on COGS account.move.line; separate account.analytic.line records via _create_analytic_move() (line 190)"
  },
  "evidence_files": [
    "01_RESTRICTED_TECHNICAL_EVIDENCE/U84_cogs_timing_delivery.md",
    "02_NEUTRAL_KNOWLEDGE/U84_cogs_timing_delivery_NEUTRAL.md"
  ],
  "gate_script": "/tmp/vdr_check_u84.py"
}
