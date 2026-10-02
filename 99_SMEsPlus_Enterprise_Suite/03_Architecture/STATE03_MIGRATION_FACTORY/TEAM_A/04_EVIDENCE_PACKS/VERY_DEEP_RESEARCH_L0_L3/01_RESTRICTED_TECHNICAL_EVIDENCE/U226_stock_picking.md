# U226 — stock.picking: State Machine, Backorder Creation, action_done, Availability
**VDR Research Unit U226 | Module: stock | File: models/stock_picking.py**
**Source SHA256 (first 12 chars): 96fe35c33865**
**Odoo Community 19.0.post20260921 — READ-ONLY evidence, no fabrication**

---

## 1. Model Declaration

`StockPicking` is declared at line 538–542:
```
_name = 'stock.picking'
_inherit = ['mail.thread', 'mail.activity.mixin']
_description = "Transfer"
_order = "priority desc, scheduled_date asc, id desc"
```

---

## 2. State Field Definition

**File**: `stock/models/stock_picking.py`, **lines 575–589**

```python
state = fields.Selection([
    ('draft', 'Draft'),
    ('waiting', 'Waiting Another Operation'),
    ('confirmed', 'Waiting'),
    ('assigned', 'Ready'),
    ('done', 'Done'),
    ('cancel', 'Cancelled'),
], string='Status', compute='_compute_state',
    copy=False, index=True, readonly=True, store=True, tracking=True, ...)
```

States:
- **draft** — picking not confirmed; no reservation
- **waiting** — waiting for a preceding operation (upstream move not done)
- **confirmed** — products not fully reserved
- **assigned** — ready to process (products reserved, or shipping policy allows partial)
- **done** — transfer validated and processed
- **cancel** — transfer cancelled

---

## 3. `_compute_state()` — Derived from Move States

**Lines 815–862**

Dependencies: `move_type`, `move_ids.state`, `move_ids.picking_id`

Logic summary:
1. Aggregates flags per picking: `any_draft`, `all_cancel`, `all_cancel_done`, `all_done_are_scrapped`, `any_cancel_and_not_scrapped`.
2. If no moves or any draft move → `draft`
3. All moves cancelled → `cancel`
4. All moves in `cancel`/`done`:
   - If all done moves go to inventory location AND at least one non-scrap move cancelled → `cancel`
   - Otherwise → `done`
5. Otherwise:
   - If source location bypasses reservation AND all moves are `make_to_stock` → `assigned`
   - Else call `_get_relevant_state_among_moves()` on stock.move (lines 857–862):
     - Returns `partially_available` → picking state = `assigned` (line 860)
     - Otherwise uses move's relevant state directly (line 862)

**Key insight**: `partially_available` move state maps to `assigned` picking state (line 859–860).

---

## 4. `_get_relevant_state_among_moves()` — in stock_move.py

**stock/models/stock_move.py, lines 1411–1451**

Sort map for moves: `assigned=4`, `waiting=3`, `partially_available=2`, `confirmed=1`.

For `move_type == 'one'` (deliver all at once):
- `confirmed` or `partially_available` most important → returns `confirmed`
- Otherwise returns most important move state

For `move_type == 'direct'` (as soon as possible):
- If any `assigned`/`partially_available` but not all assigned → `partially_available`
- Otherwise returns least important move state

---

## 5. `action_confirm()` — Lines 1194–1201

```python
def action_confirm(self):
    self._check_company()
    self.move_ids.filtered(lambda move: move.state == 'draft')._action_confirm()
    self.move_ids.filtered(lambda move: move.state not in ('draft', 'cancel', 'done'))._trigger_scheduler()
    return True
```

Transitions draft moves to confirmed; triggers scheduler for moves that might need procurement.

---

## 6. `action_assign()` — Lines 1203–1216

```python
def action_assign(self):
    self.filtered(lambda picking: picking.state == 'draft').action_confirm()
    moves = self.move_ids.filtered(
        lambda move: move.state not in ('draft', 'cancel', 'done')
    ).sorted(key=lambda move: (-int(move.priority), not bool(move.date_deadline),
                               move.date_deadline, move.date, move.id))
    if not moves:
        raise UserError(_('Nothing to check the availability for.'))
    moves._action_assign()
    return True
```

- Auto-confirms draft pickings before reserving
- Sorts moves: highest priority first, then by deadline, then by date
- Calls `_action_assign()` on `stock.move` to reserve quants

---

## 7. `button_validate()` — Lines 1420–1480

Entry point for validation UI button. Full chain:

1. Filters out already-done pickings (line 1421)
2. Auto-confirms any draft picking (line 1422–1426); sets qty = demanded if no qty set on move
3. Runs `_sanity_check()` unless `skip_sanity_check` context key set (line 1429–1430)
4. Runs `_pre_action_done_hook()` (line 1436) — triggers backorder wizard if needed
5. Separates pickings by backorder policy (lines 1441–1446):
   - `create_backorder == 'never'` → cancel_backorder=True
   - Others → cancel_backorder=False
6. Calls `_action_done()` on each group (lines 1447–1450)
7. Optionally returns reception report action (lines 1452–1480)

**No `_check_immediate()` method exists in v19.** The "immediate transfer" concept (no initial demand) has been removed from this module.

---

## 8. `_pre_action_done_hook()` — Lines 1495–1514

```python
def _pre_action_done_hook(self):
    for picking in self:
        has_quantity = False
        has_pick = False
        for move in picking.move_ids:
            if move.quantity:
                has_quantity = True
            if move.location_dest_usage == 'inventory':
                continue
            if move.picked:
                has_pick = True
            if has_quantity and has_pick:
                break
        if has_quantity and not has_pick:
            picking.move_ids.picked = True
    if not self.env.context.get('skip_backorder'):
        pickings_to_backorder = self._check_backorder()
        if pickings_to_backorder:
            return pickings_to_backorder._action_generate_backorder_wizard(
                show_transfers=self._should_show_transfers()
            )
    return True
```

- Auto-marks moves as `picked` when quantities are set but no move is explicitly picked
- Checks whether backorder wizard must appear

---

## 9. `_check_backorder()` — Lines 1555–1568

```python
def _check_backorder(self):
    prec = self.env["decimal.precision"].precision_get("Product Unit")
    backorder_pickings = self.browse()
    for picking in self:
        if picking.picking_type_id.create_backorder != 'ask':
            continue
        if any(
                (move.product_uom_qty and not move.picked) or
                float_compare(move._get_picked_quantity(), move.product_uom_qty, precision_digits=prec) < 0
                for move in picking.move_ids
                if move.state != 'cancel'
        ):
            backorder_pickings |= picking
    return backorder_pickings
```

Only pickings whose picking type has `create_backorder == 'ask'` are flagged for the wizard. The check compares picked quantity vs demanded quantity.

---

## 10. `_action_done()` — Lines 1263–1289

```python
def _action_done(self):
    self._check_company()
    todo_moves = self.move_ids.filtered(
        lambda self: self.state in ['draft', 'waiting', 'partially_available', 'assigned', 'confirmed']
    )
    for picking in self:
        if picking.owner_id:
            picking.move_ids.write({'restrict_partner_id': picking.owner_id.id})
            picking.move_line_ids.write({'owner_id': picking.owner_id.id})
    todo_moves._action_done(cancel_backorder=self.env.context.get('cancel_backorder'))
    self.write({'date_done': fields.Datetime.now(), 'priority': '0'})
    done_incoming_moves = self.filtered(
        lambda p: p.picking_type_id.code in ('incoming', 'internal')
    ).move_ids.filtered(lambda m: m.state == 'done')
    done_incoming_moves._trigger_assign()
    self._intercompany_unpack()
    self._send_confirmation_email()
    return True
```

- `date_done` is set via `fields.Datetime.now()` at line 1281 — written at the end of `_action_done()`
- After incoming/internal completion, triggers `_trigger_assign()` on done moves to reassign downstream
- Propagates `cancel_backorder` context key to `stock.move._action_done()`

---

## 11. `_create_backorder()` — Lines 1599–1624

```python
def _create_backorder(self, backorder_moves=None):
    backorders = self.env['stock.picking']
    bo_to_assign = self.env['stock.picking']
    for picking in self:
        if backorder_moves:
            moves_to_backorder = backorder_moves.filtered(lambda m: m.picking_id == picking)
        else:
            moves_to_backorder = picking._get_moves_to_backorder()
        moves_to_backorder._recompute_state()
        if moves_to_backorder:
            backorder_picking = picking._create_backorder_picking()
            moves_to_backorder.write({'picking_id': backorder_picking.id, 'picked': False})
            moves_to_backorder.mapped('move_line_ids').write({'picking_id': backorder_picking.id})
            backorders |= backorder_picking
            backorder_picking.user_id = False
            picking.message_post(body=_('The backorder %s has been created.', ...))
            if backorder_picking.picking_type_id.reservation_method == 'at_confirm':
                bo_to_assign |= backorder_picking
    if bo_to_assign:
        bo_to_assign.action_assign()
    return backorders
```

Backorder is created by `_create_backorder_picking()` which calls `self.copy({...,'backorder_id': self.id,...})` (line 1595). Unmoved moves are re-linked to the backorder picking. If reservation_method is `at_confirm`, backorder is immediately reserved.

---

## 12. `_create_backorder_picking()` — Lines 1589–1597

```python
def _create_backorder_picking(self):
    self.ensure_one()
    return self.copy({
        'name': '/',
        'move_ids': [],
        'move_line_ids': [],
        'backorder_id': self.id,
        'return_id': self.return_id.id,
    })
```

`backorder_id` FK on the new picking points to the original picking. This is the FK chain for backorder lineage.

---

## 13. `action_split_transfer()` — Lines 1482–1493

Manual split action (not from wizard). Calls `moves._create_backorder()` on stock.move level, then `self._create_backorder(backorder_moves=backorder_moves)`.

---

## 14. `_action_generate_backorder_wizard()` — Lines 1537–1548

Returns an `ir.actions.act_window` opening `stock.backorder.confirmation` wizard. Context includes `default_pick_ids`.

---

## 15. `_compute_scheduled_date()` — Lines 864–873

```python
@api.depends('move_ids.state', 'move_ids.date', 'move_type')
def _compute_scheduled_date(self):
    for picking in self:
        if not picking.id:
            continue
        moves_dates = picking.move_ids.filtered(
            lambda move: move.state not in ('done', 'cancel')
        ).mapped('date')
        if picking.move_type == 'direct':
            picking.scheduled_date = min(moves_dates, default=...)
        else:
            picking.scheduled_date = max(moves_dates, default=...)
```

- `move_type == 'direct'` → min date of undone moves
- `move_type == 'one'` → max date of undone moves

---

## 16. `picking_type_id` — Lines 620–623

```python
picking_type_id = fields.Many2one(
    'stock.picking.type', 'Operation Type',
    required=True, index=True, ...)
```

The `picking_type_id.code` distinguishes:
- `incoming` → receipt (supplier → stock)
- `outgoing` → delivery (stock → customer)
- `internal` → internal transfer

Effects:
- Incoming: `use_create_lots=True` by default; `hide_reservation_method=True`
- Outgoing: `use_existing_lots=True` by default
- `create_backorder` (ask/always/never) on the type drives the backorder policy (line 133)
- After incoming/internal `_action_done()`, `_trigger_assign()` is called (line 1284–1285)

---

## 17. `date_done` field — Line 606

```python
date_done = fields.Datetime('Date of Transfer', copy=False,
    help="Date at which the transfer has been processed or cancelled.")
```

Written at `_action_done()` line 1281:
```python
self.write({'date_done': fields.Datetime.now(), 'priority': '0'})
```

---

## 18. `reference_ids` field — Lines 590–591

```python
reference_ids = fields.Many2many(
    'stock.reference', related="move_ids.reference_ids",
    string="References", readonly=True)
```

Replaces the old `group_id` FK to `procurement.group`. The `stock.reference` model (stock/models/stock_reference.py) stores a `name` string and relates Many2many to `stock.move`. **`procurement.group` model no longer exists in v19 Community.**

---

## 19. `do_unreserve()` — Lines 1417–1418

```python
def do_unreserve(self):
    self.move_ids._do_unreserve()
```

Delegates to `stock.move._do_unreserve()`. No inline reservation logic.

---

## 20. `_should_ignore_backorders()` — Lines 1520–1523

```python
def _should_ignore_backorders(self):
    return bool(self.return_id)
```

Return pickings skip the normal backorder policy.

---

## 21. `_autoconfirm_picking()` — Lines 1570–1583

Auto-confirms picking when moves are added after initial confirmation. Also confirms draft moves that already have a quantity set (lines 1582–1583).

---

## 22. `action_cancel()` — Lines 1218–1222

```python
def action_cancel(self):
    self.move_ids._action_cancel()
    self.write({'is_locked': True})
    self.filtered(lambda x: not x.move_ids).state = 'cancel'
    return True
```

Sets picking to `cancel` if no moves remain after move cancellation.

---

## 23. MIGRATION FLAG: `show_validate` REMOVED

In Odoo 19, `_compute_show_validate()` and the `show_validate` field are **not present** in `stock_picking.py`. The field appears only in `.po` translation files (legacy strings). The validate button visibility is controlled entirely by form-view XML conditions in v19.

---

## 24. MIGRATION FLAG: `immediate_transfer` / `_check_immediate()` REMOVED

Neither `immediate_transfer` Boolean field nor `_check_immediate()` method exist in `stock_picking.py` v19. The immediate-transfer wizard flow (where no initial demand is set) was removed. In v19, `button_validate()` directly handles zero-quantity moves at lines 1425–1426 by copying demand to quantity.

---

## Source Location
`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/stock/models/stock_picking.py`
