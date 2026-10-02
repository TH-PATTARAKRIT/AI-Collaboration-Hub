# U154 — stock: Scrapping Flow and Valuation Impact (L3 Deep)

**Unit:** U154 | **G Group:** G06/G01 | **Priority:** P1
**Status:** GATE-PASS | **Claims:** 22

---

## ARCHITECTURAL NOTE — Odoo 19 Has No SVL Model

Odoo 16/17 documentation refers to `stock.valuation.layer` (SVL) as a dedicated model.
In Odoo 19 (`post20260921`) this model **does not exist**. Valuation is stored directly
on `stock.move` as the `value` field (Monetary, `stock_account/models/stock_move.py:24`).
The replacement audit-history model is `product.value` (`stock_account/models/product_value.py:4`).
All claims below use Odoo-19 terminology: `stock.move.value` instead of SVL.

---

## VDR CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| C001 | SCRAP-MODEL | `stock/models/stock_scrap.py:10` | `class StockScrap` | STRUCTURAL | Always | VERIFIED | `stock.scrap` model inherits `mail.thread`; ordered `id desc`. | The scrap order is a first-class document model with message-thread inheritance. |
| C002 | SCRAP-FIELDS | `stock/models/stock_scrap.py:21-23` | `product_id` field | FIELD | Always | VERIFIED | `product_id` is Many2one to `product.product`, domain `[('type','=','consu')]`, required, check_company. | The product on a scrap order is restricted to consumable and storable goods with company enforcement. |
| C003 | SCRAP-FIELDS | `stock/models/stock_scrap.py:43-46` | `scrap_location_id` field | FIELD | Always | VERIFIED | `scrap_location_id` is Many2one to `stock.location`, domain `[('usage','=','inventory')]`; computed from company_id. | The scrap destination is always a location of Inventory Loss type, computed per company. |
| C004 | SCRAP-FIELDS | `stock/models/stock_scrap.py:30-32` | `lot_id` field | FIELD | Tracked products | VERIFIED | `lot_id` is Many2one to `stock.lot`, domain `[('product_id','=',product_id)]`, check_company. | Lot or serial is optionally linked to the scrap order and is restricted to the same product. |
| C005 | SCRAP-FIELDS | `stock/models/stock_scrap.py:47-49` | `scrap_qty` field | FIELD | Always | VERIFIED | `scrap_qty` Float field, required, digits `Product Unit`, default 1.0, computed from linked moves. | The scrapped quantity is stored as a float with product-precision and defaults to one unit. |
| C006 | SCRAP-FIELDS | `stock/models/stock_scrap.py:50-53` | `state` field | FIELD | Always | VERIFIED | `state` Selection `[('draft','Draft'),('done','Done')]`, default `draft`, tracking enabled. | A scrap order has two states only: draft and done; state changes are tracked in the chatter. |
| C007 | SCRAP-VALIDATE | `stock/models/stock_scrap.py:211-234` | `action_validate()` | METHOD | Always | VERIFIED | Guards zero-qty, calls `check_available_qty()`; if sufficient stock calls `do_scrap()`; else opens `stock.warn.insufficient.qty.scrap` wizard. | The validation entry point enforces positive quantity and optionally warns when on-hand stock is insufficient before executing the scrap. |
| C008 | SCRAP-EXECUTE | `stock/models/stock_scrap.py:152-163` | `do_scrap()` | METHOD | Always | VERIFIED | Assigns sequence name, calls `_create_scrap_move()`, invokes `move.with_context(is_scrap=True)._action_done()`, writes state to `done`. | The core execution method creates a stock move and immediately validates it with the is_scrap context flag set. |
| C009 | SCRAP-MOVE | `stock/models/stock_scrap.py:125-150` | `_prepare_move_values()` | METHOD | Always | VERIFIED | Returns dict with `location_id=self.location_id.id`, `location_dest_id=self.scrap_location_id.id`, `scrap_id=self.id`, `picked=True`; inline move_line_ids with lot, package, owner. | The scrap move is built from source to scrap-type destination and carries lot, package, and owner from the scrap order. |
| C010 | SCRAP-MOVE | `stock/models/stock_move.py:139` | `scrap_id` field | FIELD | Always | VERIFIED | `scrap_id` is Many2one to `stock.scrap` with `index='btree_not_null'`, readonly. | Every stock move carries an optional back-reference to its originating scrap order, indexed for fast lookup. |
| C011 | SCRAP-NO-BACKORDER | `stock/models/stock_move.py:2305-2308` | `_action_done()` backorder guard | GUARD | is_scrap context | VERIFIED | After completing moves, `if self.env.context.get('is_scrap'): return moves` — backorder creation is skipped entirely. | Scrap moves never generate backorders; the is_scrap context flag short-circuits the backorder branch. |
| C012 | VALUATION-OUT | `stock_account/models/stock_move.py:575-583` | `_is_out()` | METHOD | stock_account installed | VERIFIED | `_is_out()` returns truthy when `_get_out_move_lines()` is non-empty: lines where `location_id._should_be_valued()=True` and `location_dest_id._should_be_valued()=False`. | A scrap move qualifies as outgoing for valuation because the source location is internal (valued) and the destination is inventory-loss type (not valued). |
| C013 | VALUATION-SHOULDBE | `stock_account/models/stock_location.py:36-41` | `_should_be_valued()` | METHOD | stock_account installed | VERIFIED | Returns `bool(self.company_id) and self.usage in ['internal','transit']`; usage `inventory` returns False. | Only internal and transit locations are considered part of the company stock value; a scrap location with usage inventory is explicitly outside the valued perimeter. |
| C014 | VALUATION-SETVALUE | `stock_account/models/stock_move.py:292-351` | `_set_value()` | METHOD | stock_account installed | VERIFIED | For outgoing moves: if `cost_method=='fifo'` calls `product._run_fifo(valued_qty)` (line 348); else `move.value = product.standard_price * move._get_valued_qty()` (line 351). | For AVCO and standard-price products the scrapped-goods value equals the product standard price multiplied by the scrapped quantity; for FIFO it consumes from the oldest in-move cost stack. |
| C015 | VALUATION-FIFO | `stock_account/models/product.py:540-581` | `_run_fifo()` | METHOD | FIFO product | VERIFIED | Builds `fifo_stack` from `_run_fifo_get_stack()` of oldest in-moves ordered `date desc, id desc`, reversed; pops front (oldest) first, consumes `in_value * qty / in_qty` proportionally. | FIFO scrap cost is drawn from the oldest inbound cost layers in chronological order, consuming proportional value from each receipt move in the stack. |
| C016 | VALUATION-ACCTMOVE | `stock_account/models/stock_move.py:177-191` | `_action_done()` override | METHOD | stock_account installed | VERIFIED | Calls `moves_out._set_value()` before super, then `moves._create_account_move()` after super returns; scrap is handled in `moves_out`. | The accounting module's override of action_done ensures outgoing value is computed before move completion, then posts the journal entry immediately after. |
| C017 | VALUATION-JOURNAL | `stock_account/models/stock_move.py:229-249` | `_get_account_move_line_vals()` | METHOD | stock_account + real_time | VERIFIED | When `location_id.valuation_account_id` is absent: debit_acc = `scrap_location.valuation_account_id`, credit_acc = `product._get_product_accounts()['stock_valuation']`; returns two AML dicts. | The journal entry for scrap credits the product's stock valuation account (removes inventory value) and debits the scrap location's expense account (records the loss). |
| C018 | VALUATION-GUARD | `stock_account/models/stock_move.py:659-667` | `_should_create_account_move()` | METHOD | stock_account + real_time | VERIFIED | Returns True only when `product.is_storable`, `is_valued`, `location_dest_id.valuation_account_id or location_id.valuation_account_id`, non-zero qty, `product.valuation=='real_time'`. | No journal entry is created for a scrap unless the scrap location has a valuation account configured and the product uses real-time (automated) inventory valuation. |
| C019 | VALUATION-ACCOUNT | `stock_account/models/stock_location.py:11-14` | `valuation_account_id` field | FIELD | stock_account installed | VERIFIED | `valuation_account_id` Many2one to `account.account` on `stock.location`; help text: "Expense account used to re-qualify products removed from stock and sent to this location". | The scrap-loss expense account is configured directly on the scrap location record via the valuation account field added by the stock_account module. |
| C020 | SCRAP-NO-CANCEL | `stock/models/stock_scrap.py:120-123` | `_unlink_except_done()` | GUARD | Always | VERIFIED | `@api.ondelete`: raises `UserError` if any record in the set has `state=='done'`. No cancel/undo method exists on `stock.scrap`. | A validated scrap order cannot be deleted or reversed through the standard interface; there is no cancel state or reverse-scrap button on the model. |
| C021 | MULTICOMPANY | `stock/models/stock_scrap.py:88-98` | `_compute_scrap_location_id()` | METHOD | Multi-company | VERIFIED | Reads `stock.location` filtered by `[('company_id','in',self.company_id.ids),('usage','=','inventory')]`; `location_id` also carries `check_company=True`. | Scrap respects company isolation: both the source location and the scrap destination are filtered to the scrap order's company, preventing cross-company inventory moves. |
| C022 | NO-SVL-IN-V19 | `stock_account/models/stock_move.py:24` | `value` field | ARCHITECTURAL | Odoo 19 | VERIFIED | No `stock.valuation.layer` model exists in Odoo 19. Inventory value is the `value` Monetary field on `stock.move`; audit history of manual changes is `product.value` (`product_value.py:4`). | Odoo 19 eliminated the separate valuation-layer record; the scrapped inventory value lives directly on the stock move and is reconciled through the linked journal entry on the same record. |

---

## SCRAP FLOW SEQUENCE (L3 Detail)

```
stock.scrap.action_validate()          [stock_scrap.py:211]
  └─► check_available_qty()             [stock_scrap.py:196]
  └─► do_scrap()                        [stock_scrap.py:152]
        ├─ ir.sequence → scrap.name
        ├─ _create_scrap_move()          [stock_scrap.py:165]
        │    └─ stock.move.create(       [stock_scrap.py:125-150]
        │         location_id     = internal source
        │         location_dest_id= scrap/inventory-loss
        │         scrap_id        = self.id
        │         picked          = True
        │       )
        └─ move.with_context(is_scrap=True)._action_done()
              ├─ [stock_account override]  [stock_account/stock_move.py:177]
              │    moves_out._set_value()  → value = std_price × qty  (AVCO/std)
              │                           → _run_fifo()               (FIFO)
              ├─ super()._action_done()    [stock/stock_move.py:2307]
              │    └─ is_scrap ctx → skip backorder
              └─ moves._create_account_move()
                   └─ _should_create_account_move()  → needs real_time + valuation_account
                   └─ _get_account_move_line_vals()
                        Credit: product stock_valuation account
                        Debit:  scrap_location.valuation_account_id
                   └─ account.move.sudo().create() + _post()  [stock_account/stock_move.py:209-217]
```

---

## KEY FILE REFERENCES

| File | Line(s) | Purpose |
|------|---------|---------|
| `stock/models/stock_scrap.py` | 10–59 | Model definition, all fields |
| `stock/models/stock_scrap.py` | 125–163 | Move preparation and execution |
| `stock/models/stock_scrap.py` | 211–234 | action_validate entry point |
| `stock/models/stock_move.py` | 139 | scrap_id backlink field |
| `stock/models/stock_move.py` | 2305–2308 | is_scrap backorder guard |
| `stock/models/stock_location.py` | 196–199 | _check_scrap_location constraint |
| `stock_account/models/stock_move.py` | 24 | value field (replaces SVL) |
| `stock_account/models/stock_move.py` | 177–191 | _action_done override (value + journal) |
| `stock_account/models/stock_move.py` | 229–249 | _get_account_move_line_vals (debit/credit) |
| `stock_account/models/stock_move.py` | 292–351 | _set_value (AVCO vs FIFO formula) |
| `stock_account/models/stock_move.py` | 575–583 | _is_out (scrap = out) |
| `stock_account/models/stock_move.py` | 659–667 | _should_create_account_move guard |
| `stock_account/models/stock_location.py` | 11–41 | valuation_account_id, _should_be_valued |
| `stock_account/models/product.py` | 540–581 | _run_fifo (FIFO cost stack) |
| `stock_account/models/product_value.py` | 1–88 | ProductValue audit model |
| `stock_account/tests/test_stockvaluation.py` | 2843–2846 | Test confirms debit/credit accounts for scrap |
