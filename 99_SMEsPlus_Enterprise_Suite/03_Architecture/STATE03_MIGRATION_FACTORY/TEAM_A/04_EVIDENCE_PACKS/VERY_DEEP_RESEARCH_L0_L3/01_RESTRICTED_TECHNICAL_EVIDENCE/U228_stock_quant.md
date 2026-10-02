# U228 — stock.quant: Inventory Quantity Tracking, Lot-Location Quantities, _update_available_quantity, Inventory Adjustment
## RESTRICTED TECHNICAL EVIDENCE

**Source file**: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/stock/models/stock_quant.py`
**SHA-256**: `6d894fea409598074a04d8ca805d7d4f974b5b34357e0ce915ec58d492a19362`
**Lines**: 1567
**Secondary source**: `.../stock_account/models/stock_quant.py` (inherit)
**Secondary source**: `.../product_expiry/models/stock_quant.py` (inherit)
**Secondary source**: `.../stock_account/models/product_value.py`
**Secondary source**: `.../odoo/orm/models.py` (line 5605: `try_lock_for_update`)

---

## 1. Model Declaration and Identity Key

```python
# stock/models/stock_quant.py:19-23
class StockQuant(models.Model):
    _name = 'stock.quant'
    _description = 'Quants'
    _rec_name = 'product_id'
    _rec_names_search = ['location_id', 'lot_id', 'package_id', 'owner_id']
```

A quant is the atomic unit of inventory. One quant record represents a specific combination of product + location + lot + package + owner, with an associated on-hand quantity and reserved quantity.

---

## 2. Key Fields

### Identity/Grouping Fields

```python
# stock/models/stock_quant.py:45-48
product_id = fields.Many2one(
    'product.product', 'Product',
    domain=lambda self: self._domain_product_id(),
    ondelete='restrict', required=True, index=True, check_company=True)

# stock/models/stock_quant.py:57-60
location_id = fields.Many2one(
    'stock.location', 'Location',
    domain=lambda self: self._domain_location_id(),
    bypass_search_access=True, ondelete='restrict', required=True, index=True)

# stock/models/stock_quant.py:64-67
lot_id = fields.Many2one(
    'stock.lot', 'Lot/Serial Number', index=True,
    ondelete='restrict', check_company=True,
    domain=lambda self: self._domain_lot_id())

# stock/models/stock_quant.py:70-73
package_id = fields.Many2one(
    'stock.package', 'Package',
    domain="['|', ('location_id', '=', location_id), ...]",
    help='The package containing this quant', ondelete='restrict', check_company=True, index=True)

# stock/models/stock_quant.py:74-77
owner_id = fields.Many2one(
    'res.partner', 'Owner',
    help='This is the owner of the quant', check_company=True,
    index='btree_not_null')
```

### Quantity Fields

```python
# stock/models/stock_quant.py:78-86
quantity = fields.Float(
    'Quantity',
    help='Quantity of products in this quant, in the default unit of measure of the product',
    readonly=True, digits='Product Unit')
reserved_quantity = fields.Float(
    'Reserved Quantity',
    default=0.0,
    help='Quantity of reserved products in this quant, ...',
    readonly=True, required=True, digits='Product Unit')
available_quantity = fields.Float(
    'Available Quantity',
    help="On hand quantity which hasn't been reserved on a transfer...",
    compute='_compute_available_quantity', digits='Product Unit')

# stock/models/stock_quant.py:91
in_date = fields.Datetime('Incoming Date', readonly=True, required=True, default=fields.Datetime.now)
```

---

## 3. _compute_available_quantity

```python
# stock/models/stock_quant.py:119-122
@api.depends('quantity', 'reserved_quantity')
def _compute_available_quantity(self):
    for quant in self:
        quant.available_quantity = quant.quantity - quant.reserved_quantity
```

Simple arithmetic: `available_quantity = quantity - reserved_quantity`. This computed field is non-stored and recalculated on demand.

**Extension in product_expiry** (`product_expiry/models/stock_quant.py:30-36`):
```python
@api.depends('removal_date')
def _compute_available_quantity(self):
    super()._compute_available_quantity()
    current_date = fields.Datetime.now()
    for quant in self:
        if quant.use_expiration_date and quant.removal_date and quant.removal_date <= current_date:
            quant.available_quantity = 0
```
When `product_expiry` is installed and the lot's removal_date has passed, available_quantity is forced to 0.

---

## 4. _get_gather_domain — Location + Lot + Package Domain

```python
# stock/models/stock_quant.py:750-769
def _get_gather_domain(self, product_id, location_id, lot_id=None, package_id=None, owner_id=None, strict=False):
    domains = [Domain('product_id', '=', product_id.id)]
    if not strict:
        if lot_id:
            domains.append(Domain('lot_id', 'in', [lot_id.id, False]))
        if package_id:
            domains.append(Domain('package_id', '=', package_id.id))
        if owner_id:
            domains.append(Domain('owner_id', '=', owner_id.id))
        domains.append(Domain('location_id', 'child_of', location_id.id))
    else:
        domains.extend((
            Domain('lot_id', 'in', [False, lot_id.id if lot_id else False]),
            Domain('package_id', '=', package_id.id if package_id else False),
            Domain('owner_id', '=', owner_id.id if owner_id else False),
            Domain('location_id', '=', location_id.id),
        ))
    if self.env.context.get('with_expiration'):
        domains.append(Domain('removal_date', '>=', ...) | Domain('removal_date', '=', False))
    return Domain.AND(domains)
```

- **strict=False**: `location_id child_of` (includes children), lot_id may match False (untracked)
- **strict=True**: exact `location_id =`, exact lot/package/owner matching

---

## 5. _gather — Quant Lookup with Removal Strategy

```python
# stock/models/stock_quant.py:771-791
def _gather(self, product_id, location_id, lot_id=None, package_id=None, owner_id=None, strict=False, qty=0):
    removal_strategy = self._get_removal_strategy(product_id, location_id)
    domain = self._get_gather_domain(product_id, location_id, lot_id, package_id, owner_id, strict)
    if removal_strategy == 'least_packages' and qty:
        domain = self._run_least_packages_removal_strategy_astar(domain, qty)
    order = self._get_removal_strategy_order(removal_strategy)
    quants_cache = self.env.context.get('quants_cache')
    if quants_cache is not None and strict and removal_strategy != 'least_packages':
        res = self.env['stock.quant']
        if lot_id:
            res |= quants_cache[product_id.id, location_id.id, lot_id.id, package_id.id, owner_id.id]
        res |= quants_cache[product_id.id, location_id.id, False, package_id.id, owner_id.id]
    else:
        res = self.search(domain, order=order)
    if removal_strategy == "closest":
        res = res.sorted(lambda q: (q.location_id.complete_name, -q.id))
    return res.sorted(lambda q: not q.lot_id)
```

---

## 6. _get_available_quantity — Quantity Check for Reservation

```python
# stock/models/stock_quant.py:793-832
def _get_available_quantity(self, product_id, location_id, lot_id=None, package_id=None, owner_id=None, strict=False, allow_negative=False):
    self = self.sudo()
    quants = self._gather(product_id, location_id, lot_id=lot_id, package_id=package_id, owner_id=owner_id, strict=strict)
    if product_id.tracking == 'none':
        available_quantity = sum(quants.mapped('quantity')) - sum(quants.mapped('reserved_quantity'))
        if allow_negative:
            return available_quantity
        else:
            return available_quantity if product_id.uom_id.compare(available_quantity, 0.0) >= 0.0 else 0.0
    else:
        availaible_quantities = {lot_id: 0.0 for lot_id in list(set(quants.mapped('lot_id'))) + ['untracked']}
        for quant in quants:
            if not quant.lot_id and strict and lot_id:
                continue
            if not quant.lot_id:
                availaible_quantities['untracked'] += quant.quantity - quant.reserved_quantity
            else:
                availaible_quantities[quant.lot_id] += quant.quantity - quant.reserved_quantity
        if allow_negative:
            return sum(availaible_quantities.values())
        else:
            return sum(available_quantity for available_quantity in availaible_quantities.values() if product_id.uom_id.compare(available_quantity, 0) > 0)
```

- **strict=False**: gathers quants at location and child locations
- **strict=True**: gathers quants at exact location/lot/package/owner
- **allow_negative=False**: negative quantities floor to 0.0
- **allow_negative=True**: returns actual signed sum (used internally in `_update_available_quantity`)

---

## 7. _update_available_quantity — Core Quantity Update with Row Lock

```python
# stock/models/stock_quant.py:1038-1105
@api.model
def _update_available_quantity(self, product_id, location_id, quantity=False, reserved_quantity=False, lot_id=None, package_id=None, owner_id=None, in_date=None):
    if not (quantity or reserved_quantity):
        raise ValidationError(_('Quantity or Reserved Quantity should be set.'))
    self = self.sudo()
    quants = self._gather(product_id, location_id, lot_id=lot_id, package_id=package_id, owner_id=owner_id, strict=True)
    if lot_id:
        if product_id.uom_id.compare(quantity, 0) > 0:
            quants = quants.filtered(lambda q: q.lot_id)
        else:
            quants = quants.filtered(lambda q: product_id.uom_id.compare(q.quantity, 0) > 0 or q.lot_id)

    if location_id.should_bypass_reservation():
        incoming_dates = []
    else:
        incoming_dates = [quant.in_date for quant in quants if quant.in_date and
                          quant.product_uom_id.compare(quant.quantity, 0) > 0]
    if in_date:
        incoming_dates += [in_date]
    if incoming_dates:
        in_date = min(incoming_dates)
    else:
        in_date = fields.Datetime.now()

    quant = None
    if quants:
        # lock the first available
        quant = quants.try_lock_for_update(allow_referencing=True, limit=1)

    if quant:
        vals = {'in_date': in_date}
        if quantity:
            vals['quantity'] = quant.quantity + quantity
        if reserved_quantity:
            vals['reserved_quantity'] = max(0, quant.reserved_quantity + reserved_quantity)
        quant.write(vals)
    else:
        vals = {
            'product_id': product_id.id,
            'location_id': location_id.id,
            'lot_id': lot_id and lot_id.id,
            'package_id': package_id and package_id.id,
            'owner_id': owner_id and owner_id.id,
            'in_date': in_date,
        }
        if quantity:
            vals['quantity'] = quantity
        if reserved_quantity:
            vals['reserved_quantity'] = reserved_quantity
        self.create(vals)
    return self._get_available_quantity(product_id, location_id, lot_id=lot_id, package_id=package_id, owner_id=owner_id, strict=True, allow_negative=True), in_date
```

### Key behaviors:
1. Always uses `strict=True` for gather — exact location/lot/package/owner match
2. **Row-level locking**: `quants.try_lock_for_update(allow_referencing=True, limit=1)` → SQL `FOR NO KEY UPDATE SKIP LOCKED` on first available quant
3. **in_date handling**: Takes the minimum (oldest) of all existing positive-qty quant in_dates plus the provided in_date. Defaults to `now()` if none available.
4. If no existing quant is found or can be locked, creates a new quant record
5. Returns `(available_quantity, in_date)` tuple

### try_lock_for_update implementation (orm/models.py:5605-5635):
```python
def try_lock_for_update(self, *, allow_referencing: bool = False, limit: int | None = None):
    if allow_referencing:
        lock_sql = SQL("FOR NO KEY UPDATE SKIP LOCKED")
    else:
        lock_sql = SQL("FOR UPDATE SKIP LOCKED")
    sql = SQL("%s %s", query.select(), lock_sql)
    real_ids = (id_ for [id_] in self.env.execute_query(sql))
    valid_ids = {*real_ids, *new_ids}
    return self.browse(i for i in self._ids if i in valid_ids)
```

`allow_referencing=True` uses `FOR NO KEY UPDATE` which allows foreign key references from other rows to still work (non-exclusive lock on the primary key constraint), preventing deadlocks while still preventing concurrent quantity writes.

---

## 8. _update_reserved_quantity

```python
# stock/models/stock_quant.py:1107-1120
@api.model
def _update_reserved_quantity(self, product_id, location_id, quantity, lot_id=None, package_id=None, owner_id=None, strict=True):
    self._update_available_quantity(product_id, location_id, reserved_quantity=quantity, lot_id=lot_id, package_id=package_id, owner_id=owner_id)
```

Thin delegation to `_update_available_quantity` with `reserved_quantity=quantity`. Note: `max(0, ...)` applied on line 1089 means reserved_quantity cannot go negative.

---

## 9. Removal Strategies

### Strategy lookup (lines 617-628):
```python
@api.model
def _get_removal_strategy(self, product_id, location_id):
    product_id = product_id.sudo()
    location_id = location_id.sudo()
    if product_id.categ_id.removal_strategy_id:
        return product_id.categ_id.removal_strategy_id.with_context(lang=None).method
    loc = location_id
    while loc:
        if loc.removal_strategy_id:
            return loc.removal_strategy_id.with_context(lang=None).method
        loc = loc.location_id
    return 'fifo'
```

Priority order: product category → location tree walk-up → default 'fifo'.

### Strategy ordering (lines 740-748):
```python
@api.model
def _get_removal_strategy_order(self, removal_strategy):
    if removal_strategy in ['fifo', 'least_packages']:
        return 'in_date ASC, id'
    elif removal_strategy == 'lifo':
        return 'in_date DESC, id DESC'
    elif removal_strategy == 'closest':
        return False
    raise UserError(...)
```

FIFO uses `in_date ASC` — oldest incoming date first. LIFO uses `in_date DESC` — newest first.

### FEFO (product_expiry/models/stock_quant.py:25-28):
```python
@api.model
def _get_removal_strategy_order(self, removal_strategy):
    if removal_strategy == 'fefo':
        return 'removal_date, in_date, id'
    return super()._get_removal_strategy_order(removal_strategy)
```

FEFO sorts by `removal_date` (from `lot_id.removal_date`), then by `in_date`. Requires `product_expiry` addon.

---

## 10. Inventory Adjustment Flow

### action_apply_inventory (lines 433-450):
```python
def action_apply_inventory(self, date=None):
    ctx = dict(self.env.context or {})
    ctx['default_quant_ids'] = self.ids
    quants_outdated = self.filtered(lambda quant: quant.is_outdated)
    if quants_outdated:
        ctx['default_quant_to_fix_ids'] = quants_outdated.ids
        return {  # opens stock.inventory.conflict wizard
            'res_model': 'stock.inventory.conflict',
            ...
        }
    self._apply_inventory(date)
    self.inventory_quantity_set = False
```

### _apply_inventory (lines 996-1035):
```python
def _apply_inventory(self, date=None):
    self.inventory_quantity_set = True
    move_vals = []
    ...
    for quant in self:
        inventory_location = quant.product_id.with_company(quant.company_id).property_stock_inventory or ...
        if quant.product_uom_id.compare(quant.inventory_diff_quantity, 0) > 0:
            move_vals.append(
                quant._get_inventory_move_values(quant.inventory_diff_quantity,
                                                 inventory_location,
                                                 quant.location_id, package_dest_id=quant.package_id))
        else:
            move_vals.append(
                quant._get_inventory_move_values(-quant.inventory_diff_quantity,
                                                 quant.location_id,
                                                 inventory_location,
                                                 package_id=quant.package_id))
    moves = self.env['stock.move'].with_context(inventory_mode=False).create(move_vals)
    moves.with_context(ignore_dest_packages=True)._action_done()
    if date:
        moves.date = date
    moves._trigger_assign()
    self.location_id.sudo().write({'last_inventory_date': fields.Date.today()})
    ...
    self.action_clear_inventory_quantity()
```

### _get_inventory_move_values (lines 1253-1292):
```python
res = {
    'product_id': self.product_id.id,
    'product_uom': self.product_uom_id.id,
    'product_uom_qty': qty,
    'company_id': self.company_id.id or self.env.company.id,
    'state': 'confirmed',
    'location_id': location_id.id,
    'location_dest_id': location_dest_id.id,
    'restrict_partner_id': self.owner_id.id,
    'is_inventory': True,
    'picked': True,
    'move_line_ids': [(0, 0, {
        ...
        'lot_id': self.lot_id.id,
        'package_id': package_id.id if package_id else False,
        'result_package_id': package_dest_id.id if package_dest_id else False,
        'owner_id': self.owner_id.id,
    })]
}
```

The inventory move uses `is_inventory=True` flag (not `inventory_adjustment` route as a separate route — it's a Boolean field on the move).

---

## 11. Negative Quant Behavior

There is NO `negative_quant_id` field in v19 stock.quant. Negative quantities are handled differently:

1. **In `_update_available_quantity`**: When quantity < 0 is passed (e.g., stock move out), the quant's quantity field is updated to a negative value. No separate "negative quant" tracking record.

2. **In `_get_reserve_quantity`** (lines 886-889): Negative reserved quantities tracked via a local defaultdict:
```python
negative_reserved_quantity = defaultdict(float)
for quant in quants:
    if product_id.uom_id.compare(quant.quantity - quant.reserved_quantity, 0) < 0:
        negative_reserved_quantity[(quant.location_id, quant.lot_id, quant.package_id, quant.owner_id)] += quant.quantity - quant.reserved_quantity
```
This in-memory dict adjusts available quantity calculations to account for over-reserved quants.

3. **In `_update_available_quantity`** (line 1089): `max(0, quant.reserved_quantity + reserved_quantity)` prevents reserved_quantity from going negative.

4. **`_merge_quants`** (lines 1177-1222): SQL-level deduplication using `GREATEST(0, SUM(reserved_quantity))` to ensure merged quant reserved_quantity is non-negative.

---

## 12. should_bypass_reservation (stock_location.py:411-413)

```python
def should_bypass_reservation(self):
    self.ensure_one()
    return self.usage in ('supplier', 'customer', 'inventory', 'production')
```

Locations with these usage types skip in_date tracking in `_update_available_quantity` (line 1064-1065). The inventory loss location (usage='inventory') bypasses reservation and in_date.

---

## 13. _merge_quants — Deduplication on Concurrent Create

```python
# stock/models/stock_quant.py:1177-1222
@api.model
def _merge_quants(self):
    """ In a situation where one transaction is updating a quant via
    `_update_available_quantity` and another concurrent one calls this function with the same
    argument, we'll create a new quant in order for these transactions to not rollback. This
    method will find and deduplicate these quants.
    """
    query = """WITH
                    dupes AS (
                        SELECT min(id) as to_update_quant_id,
                            (array_agg(id ORDER BY id))[2:...] as to_delete_quant_ids,
                            GREATEST(0, SUM(reserved_quantity)) as reserved_quantity,
                            SUM(inventory_quantity) as inventory_quantity,
                            SUM(quantity) as quantity,
                            MIN(in_date) as in_date
                        FROM stock_quant
                        GROUP BY product_id, company_id, location_id, lot_id, package_id, owner_id
                        HAVING count(id) > 1
                    ), ...
               DELETE FROM stock_quant WHERE id in (SELECT unnest(to_delete_quant_ids) from dupes)"""
```

When concurrent transactions create duplicate quants (due to SKIP LOCKED fallback to create), `_merge_quants` consolidates them using raw SQL: keeps lowest id, sums quantities, takes MIN(in_date) for FIFO correctness.

---

## 14. Migration Flag — product.value New Model (stock_account)

`stock_account/models/product_value.py` defines a NEW model `product.value` in v19:
```python
class ProductValue(models.Model):
    _name = 'product.value'
    _description = 'Product Value'
    product_id = fields.Many2one('product.product', ...)
    lot_id = fields.Many2one('stock.lot', ...)
    move_id = fields.Many2one('stock.move', ...)
    value = fields.Monetary(...)
    ...
```

This model tracks history of manual value updates (standard price changes, lot price changes, move value modifications). It is NOT a replacement for stock.quant — stock.quant still holds on-hand quantities. However, the old `stock.valuation.layer` model does NOT have a dedicated Python file in v19 stock_account models directory. The valuation is now tracked through `stock.move.value` field and `product.value` history records.

**MIGRATION FLAG**: Applications that relied on `stock.valuation.layer` (SVL) for custom reporting or integrations must be reviewed — the SVL model may have been absorbed into stock.move/product.value in v19.

---

## 15. stock_account StockQuant Inherit

```python
# stock_account/models/stock_quant.py:10-25
class StockQuant(models.Model):
    _inherit = 'stock.quant'
    value = fields.Monetary('Value', compute='_compute_value', groups='stock.group_stock_manager')
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', ...)
    accounting_date = fields.Date('Accounting Date', ...)
    cost_method = fields.Selection(...)
```

The stock_account addon adds `value` (monetary, computed) and `accounting_date` to stock.quant. The `value` computation delegates to `product.product.total_value` (or `lot.total_value` for lot-valued products).
