# U234 — stock.move: State Machine, Reservation, procure_method, Move Chains, Backorder Split, reference_ids, location_final_id

## RESTRICTED TECHNICAL EVIDENCE

**Status**: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

**Unit**: U234
**Model**: `stock.move`
**Modules**: stock (primary); mrp, sale_stock, purchase_stock, stock_account (extension pointers only)
**Source revision**: Odoo Community 19.0.post20260921
**Research date**: 2026-10-03
**Source file**: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/stock/models/stock_move.py`
**SHA-256**: `af624e7a0155fd31f38098d163d345a1ee068544ed3505879305ad1e62762a78`
**Lines**: 2833
**Pointer notation**: `path:line` or `path:start-end`, relative to `odoo/addons/` in the release root. In running text `L<n>` means a line of `stock/models/stock_move.py` unless another file is named. A fenced block whose first line is a `# path:start-end` comment is a verbatim excerpt of exactly those source lines. A pointer that starts with `odoo/orm/` is relative to the release root and names an ORM core file; no excerpt is taken from those files.

**Secondary sources** (paths relative to `odoo/addons/`):

| File | Lines | SHA-256 | Used for |
|---|---|---|---|
| stock/models/stock_rule.py | 750 | `6ba0d0f12b2b8062ed771a0a6140e79bfa53a0c3970f2d531e8cd41691617114` | `_run_pull`, `_get_custom_move_fields`, `_get_stock_move_values` |
| stock/models/stock_picking.py | 2170 | `96fe35c33865609889cbf8747fdd4d2be18a67a0bfa554507ff207f18bb2ee25` | `reservation_method` (L68-71), validation hand-off (L1275-1285) |
| stock/models/stock_quant.py | 1567 | `6d894fea409598074a04d8ca805d7d4f974b5b34357e0ce915ec58d492a19362` | inventory-apply hand-off (L1026-1030) |
| stock/models/stock_reference.py | 15 | `b256e6dc9bfd794a39a63dc249ec26c5f9536f0f2a7776d9587f498984e276f5` | `stock.reference` model |
| mrp/models/stock_move.py | 685 | `1f75af0f794790668e02c726899f56493109615830bfd66df8efa4b48fdcfc6c` | extension fields and hooks |
| sale_stock/models/stock.py | 356 | `682a3b20bce0bc954c0bc1b24c4d6bb07f75e7af6f653ed82910e5eaa920ade5` | `sale_line_id` and hooks (no `sale_stock/models/stock_move.py` exists) |
| purchase_stock/models/stock_move.py | 251 | `51b8f99084e42fc08503d5f23338e72657f1d53953ccc3e9c32e61785b311d64` | extension fields and hooks |
| stock_account/models/stock_move.py | 718 | `c7950b0328a3366c28b3dfb15b87941557397207f1a297426726e95f675c3a29` | `to_refund`, valuation fields (pointer only; valuation is U232) |

Pointer-only reads: `mrp/models/stock_rule.py:133-134`, `stock_account/wizard/stock_picking_return.py:10,15`, `product/models/product_template.py:122`, `mrp/models/mrp_production.py:2241`, `mrp/models/mrp_production.py:2246-2249`, `odoo/orm/fields.py:281`, `odoo/orm/fields.py:440-451`, `odoo/orm/fields_relational.py:268-282`, `odoo/orm/fields_relational.py:869`, and the caller lists given in sections 4 and 5.

## Evidence summary

1. `state` is a stored, plain, read-only Selection with seven values (`stock/models/stock_move.py:107-120`). It is not computed. Writers inside `stock/models/stock_move.py` are `default_get` (L784-785), `create` (L829-830), `_action_confirm`, `_action_assign`, `_recompute_state`, `_action_done`, `_action_cancel` and `write` (L864); other modules also write it (`mrp/models/mrp_production.py:2246-2249`, `mrp/models/stock_move.py:18-24`).
2. `quantity` is the single quantity field of the move. It is the sum of the move-line quantities and serves as both reserved and done quantity (`:171-172`, `:411-441`). There is no `quantity_done` and no `reserved_availability` field (grep, section 3).
3. `procure_method` has two stored values on the move (`make_to_stock`, `make_to_order`). The third value, `mts_else_mto`, exists only on the rule and is resolved when the move is created or confirmed (`stock/models/stock_rule.py:305-310`, `stock/models/stock_move.py:1707-1710`).
4. `_action_assign` has a bypass branch, an unchained branch and a chained branch. A move with origin moves can reserve only what its origin move lines delivered (`:2145-2178`).
5. `stock.move` has no `group_id` (grep returned no lines). `reference_ids`, a Many2many to `stock.reference`, takes its place (`:141-142`, `stock/models/stock_reference.py:4-15`).
6. `location_final_id` is a stored, writable field. `location_dest_id` is the computed intermediate destination and is replaced by the final location when the final location lies inside it (`:85-90`, `:224-244`).
7. `_action_done` writes state and date in one `write` after the move lines are validated (`:2290`). Quantities below demand lead to a backorder move created by `_create_backorder` and `_split` (`:2322-2338`, `:2367-2411`).
8. Merge compatibility is a fixed list of distinct fields that includes `location_final_id` and `restrict_partner_id` (`:1280-1293`).
9. `to_refund` is declared by stock_account (`stock_account/models/stock_move.py:20-22`) while `stock/models/stock_rule.py:355-356` writes it for negative quantities without a module guard.
10. purchase_stock overrides `_prepare_extra_move_vals` (`purchase_stock/models/stock_move.py:99-102`); no base definition and no `_create_extra_move` exist anywhere in the tree (grep, section 10).

---

## 1. Model declaration and field inventory

`stock.move` is a persistent model declared at `stock/models/stock_move.py:18-22`. The only index declared in the class body is `_product_location_index` (L200). Three greps over this file (`constrains`, `Constraint`, and a case-insensitive `constraint`) returned no lines, so the model declares no Python-level constraint and no SQL or model constraint of its own. Company consistency rests on `check_company=True` on selected relational fields and on explicit `_check_company()` calls in `_action_confirm` (L1741) and `_action_done` (L2271).

```python
# stock/models/stock_move.py:15-22
PROCUREMENT_PRIORITIES = [('0', 'Normal'), ('1', 'Urgent')]


class StockMove(models.Model):
    _name = 'stock.move'
    _description = "Stock Move"
    _order = 'sequence, id'
    _rec_name = 'reference'
```

### 1.1 Field excerpts

```python
# stock/models/stock_move.py:24-105
    sequence = fields.Integer('Sequence', default=10)
    priority = fields.Selection(
        PROCUREMENT_PRIORITIES, 'Priority', default='0',
        compute="_compute_priority", store=True)
    date = fields.Datetime(
        'Date Scheduled', default=fields.Datetime.now, index=True, required=True,
        help="Scheduled date until move is done, then date of actual move processing")
    date_deadline = fields.Datetime(
        "Deadline", readonly=True, copy=False,
        help="In case of outgoing flow, validate the transfer before this date to allow to deliver at promised date to the customer.\n\
        In case of incoming flow, validate the transfer before this date in order to have these products in stock at the date promised by the supplier")
    company_id = fields.Many2one(
        'res.company', 'Company',
        default=lambda self: self.env.company,
        index=True, required=True)
    product_id = fields.Many2one(
        'product.product', 'Product',
        check_company=True,
        domain="[('type', '=', 'consu')]", index=True, required=True)
    product_category_id = fields.Many2one(
        'product.category', 'Product Category',
        related='product_id.categ_id')
    never_product_template_attribute_value_ids = fields.Many2many(
        'product.template.attribute.value',
        'template_attribute_value_stock_move_rel',
        'move_id', 'template_attribute_value_id',
        string="Never attribute Values"
    )
    description_picking = fields.Text(string="Description Of Picking", compute='_compute_description_picking', inverse='_inverse_description_picking', compute_sudo=True)
    description_picking_manual = fields.Text(readonly=True)
    product_qty = fields.Float(
        'Real Quantity', compute='_compute_product_qty', inverse='_set_product_qty',
        digits=0, store=True, compute_sudo=True,
        help='Quantity in the default UoM of the product')
    product_uom_qty = fields.Float(
        'Demand',
        digits='Product Unit',
        default=0, required=True,
        help="This is the quantity of product that is planned to be moved."
             "Lowering this quantity does not generate a backorder."
             "Changing this quantity on assigned moves affects "
             "the product reservation, and should be done with care.")
    allowed_uom_ids = fields.Many2many('uom.uom', compute='_compute_allowed_uom_ids')
    product_uom = fields.Many2one(
        'uom.uom', "Unit", required=True, domain="[('id', 'in', allowed_uom_ids)]",
        compute="_compute_product_uom", store=True, readonly=False, precompute=True,
    )
    # TDE FIXME: make it stored, otherwise group will not work
    product_tmpl_id = fields.Many2one(
        'product.template', 'Product Template',
        related='product_id.product_tmpl_id')
    location_id = fields.Many2one(
        'stock.location', 'Source Location',
        help='The operation takes and suggests products from this location.',
        bypass_search_access=True, index=True, required=True,
        compute='_compute_location_id', store=True, precompute=True, readonly=False,
        check_company=True)
    location_dest_id = fields.Many2one(
        'stock.location', 'Intermediate Location', required=True,
        help='The operations brings product to this location', readonly=False,
        index=True, store=True, compute='_compute_location_dest_id', precompute=True, inverse='_set_location_dest_id')
    location_final_id = fields.Many2one(
        'stock.location', 'Final Location',
        readonly=False, store=True,
        help="The operation brings the products to the intermediate location."
        "But this operation is part of a chain of operations targeting the final location.",
        bypass_search_access=True, index=True, check_company=True)
    location_usage = fields.Selection(string="Source Location Type", related='location_id.usage')
    location_dest_usage = fields.Selection(string="Destination Location Type", related='location_dest_id.usage')
    partner_id = fields.Many2one(
        'res.partner', 'Destination Address ',
        help="Optional address where goods are to be delivered, specifically used for allotment",
        compute='_compute_partner_id', store=True, readonly=False,
        index='btree_not_null')
    move_dest_ids = fields.Many2many(
        'stock.move', 'stock_move_move_rel', 'move_orig_id', 'move_dest_id', 'Destination Moves',
        copy=False,
        help="Optional: next stock move when chaining them")
    move_orig_ids = fields.Many2many(
        'stock.move', 'stock_move_move_rel', 'move_dest_id', 'move_orig_id', 'Original Move',
        copy=False,
        help="Optional: previous stock move when chaining them")
```

```python
# stock/models/stock_move.py:106-151
    picking_id = fields.Many2one('stock.picking', 'Transfer', index=True, check_company=True)
    state = fields.Selection([
        ('draft', 'New'),
        ('waiting', 'Waiting Another Move'),
        ('confirmed', 'Waiting'),
        ('partially_available', 'Partially Available'),
        ('assigned', 'Available'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], string='Status',
        copy=False, default='draft', index=True, readonly=True,
        help="* New: The stock move is created but not confirmed.\n"
             "* Waiting Another Move: A linked stock move should be done before this one.\n"
             "* Waiting: The stock move is confirmed but the product can't be reserved.\n"
             "* Available: The product of the stock move is reserved.\n"
             "* Done: The product has been transferred and the transfer has been confirmed.")
    picked = fields.Boolean(
        'Picked', compute='_compute_picked', inverse='_inverse_picked',
        store=True, readonly=False, copy=False, default=False,
        help="This checkbox is just indicative, it doesn't validate or generate any product moves.")

    # used to record the product cost set by the user during a picking confirmation (when costing
    # method used is 'average price' or 'real'). Value given in company currency and in product uom.
    # as it's a technical field, we intentionally don't provide the digits attribute
    price_unit = fields.Float('Unit Price', copy=False)
    origin = fields.Char("Source Document")
    procure_method = fields.Selection([
        ('make_to_stock', 'Default: Take From Stock'),
        ('make_to_order', 'Advanced: Apply Procurement Rules')], string='Supply Method',
        default='make_to_stock', required=True, copy=False,
        help="By default, the system will take from the stock in the source location and passively wait for availability. "
             "The other possibility allows you to directly create a procurement on the source location (and thus ignore "
             "its current stock) to gather products. If we want to chain moves and have this one to wait for the previous, "
             "this second option should be chosen.")
    scrap_id = fields.Many2one('stock.scrap', 'Scrap operation', readonly=True, check_company=True, index='btree_not_null')
    procurement_values = fields.Json(store=False, help="Dummy field to store procurement values to propagate them to later steps")
    reference_ids = fields.Many2many(
        'stock.reference', 'stock_reference_move_rel', 'move_id', 'reference_id', string='References')
    rule_id = fields.Many2one(
        'stock.rule', 'Stock Rule', ondelete='restrict', help='The stock rule that created this stock move',
        check_company=True)
    propagate_cancel = fields.Boolean(
        'Propagate cancel and split', default=True,
        help='If checked, when this move is cancelled, cancel the linked move too')
    delay_alert_date = fields.Datetime('Delay Alert Date', help='Process at this date to be on time', compute="_compute_delay_alert_date", store=True)
    picking_type_id = fields.Many2one('stock.picking.type', 'Operation Type', compute='_compute_picking_type_id', store=True, readonly=False, check_company=True)
    is_inventory = fields.Boolean('Inventory')
```

```python
# stock/models/stock_move.py:152-200
    inventory_name = fields.Char(readonly=True)
    move_line_ids = fields.One2many('stock.move.line', 'move_id')
    package_ids = fields.One2many('stock.package', string='Packages', compute="_compute_package_ids")
    origin_returned_move_id = fields.Many2one(
        'stock.move', 'Origin return move', copy=False, index=True,
        help='Move that created the return move', check_company=True)
    returned_move_ids = fields.One2many('stock.move', 'origin_returned_move_id', 'All returned moves', help='Optional: all returned moves created from this move')
    availability = fields.Float(
        'Forecasted Quantity', compute='_compute_product_availability',
        readonly=True, help='Quantity in stock that can still be reserved for this move')
    # used to depict a restriction on the ownership of quants to consider when marking this move as 'done'
    restrict_partner_id = fields.Many2one(
        'res.partner', 'Owner ', check_company=True,
        index='btree_not_null')
    route_ids = fields.Many2many(
        'stock.route', 'stock_route_move', 'move_id', 'route_id', 'Destination route', help="Preferred route")
    warehouse_id = fields.Many2one('stock.warehouse', 'Warehouse', help="the warehouse to consider for the route selection on the next procurement (if any).")
    has_tracking = fields.Selection(related='product_id.tracking', string='Product with Tracking')
    has_lines_without_result_package = fields.Boolean(compute="_compute_has_lines_without_result_package")
    quantity = fields.Float(
        'Quantity', compute='_compute_quantity', digits='Product Unit', inverse='_set_quantity', store=True)
    # TODO: delete this field `show_operations`
    show_operations = fields.Boolean(related='picking_id.picking_type_id.show_operations')
    picking_code = fields.Selection(related='picking_id.picking_type_id.code', readonly=True)
    show_details_visible = fields.Boolean('Details Visible', compute='_compute_show_details_visible')
    is_storable = fields.Boolean(related='product_id.is_storable')
    additional = fields.Boolean("Whether the move was added after the picking's confirmation", default=False)
    is_locked = fields.Boolean(compute='_compute_is_locked', readonly=True)
    is_initial_demand_editable = fields.Boolean('Is initial demand editable', compute='_compute_is_initial_demand_editable')
    is_date_editable = fields.Boolean("Is Date Editable", compute="_compute_is_date_editable")
    is_quantity_done_editable = fields.Boolean('Is quantity done editable', compute='_compute_is_quantity_done_editable')
    reference = fields.Char(compute='_compute_reference', string="Reference", store=True)
    move_lines_count = fields.Integer(compute='_compute_move_lines_count')
    display_assign_serial = fields.Boolean(compute='_compute_display_assign_serial')
    display_import_lot = fields.Boolean(compute='_compute_display_assign_serial')
    next_serial = fields.Char('First SN/Lot')
    next_serial_count = fields.Integer('Number of SN/Lots')
    orderpoint_id = fields.Many2one('stock.warehouse.orderpoint', 'Original Reordering Rule', index=True)
    forecast_availability = fields.Float('Forecast Availability', compute='_compute_forecast_information', digits='Product Unit', compute_sudo=True)
    forecast_expected_date = fields.Datetime('Forecasted Expected date', compute='_compute_forecast_information', compute_sudo=True)
    lot_ids = fields.Many2many('stock.lot', compute='_compute_lot_ids', inverse='_set_lot_ids', string='Serial Numbers', readonly=False)
    reservation_date = fields.Date('Date to Reserve', compute='_compute_reservation_date', store=True, help="Computes when a move should be reserved")
    packaging_uom_id = fields.Many2one('uom.uom', 'Packaging', help="Packaging unit from sale or purchase orders", compute='_compute_packaging_uom_id', precompute=True, store=True)
    packaging_uom_qty = fields.Float('Packaging Quantity', help="Quantity in the packaging unit", compute='_compute_packaging_uom_qty', store=True)
    show_quant = fields.Boolean("Show Quant", compute="_compute_show_info")
    show_lots_m2o = fields.Boolean("Show lot_id", compute="_compute_show_info")
    show_lots_text = fields.Boolean("Show lot_name", compute="_compute_show_info")

    _product_location_index = models.Index("(product_id, location_id, location_dest_id, company_id, state)")
```

### 1.2 Field table (selected fields)

| Field | Type and target | Line | Storage and attributes |
|---|---|---|---|
| sequence | Integer | 24 | stored, default 10; first key of `_order` |
| priority | Selection (Normal, Urgent) | 25-27 | stored compute `_compute_priority` (L293-296), default `'0'` |
| date | Datetime, label Date Scheduled | 28-30 | stored, required, indexed, default now |
| date_deadline | Datetime, label Deadline | 31-34 | readonly, `copy=False`; written through `_set_date_deadline` (L583-602) |
| company_id | Many2one res.company | 35-38 | required, indexed, default current company |
| product_id | Many2one product.product | 39-42 | required, indexed, `check_company`, domain type equals consu |
| never_product_template_attribute_value_ids | Many2many product.template.attribute.value | 46-51 | relation table `template_attribute_value_stock_move_rel` |
| description_picking | Text | 52 | compute `_compute_description_picking`, inverse `_inverse_description_picking`, `compute_sudo`, not stored |
| description_picking_manual | Text | 53 | readonly |
| product_qty | Float, label Real Quantity | 54-57 | stored compute `_compute_product_qty`, inverse `_set_product_qty`, `digits=0`, `compute_sudo` |
| product_uom_qty | Float, label Demand | 58-65 | stored plain field, digits Product Unit, default 0, required |
| allowed_uom_ids | Many2many uom.uom | 66 | compute `_compute_allowed_uom_ids` (L202-205), not stored |
| product_uom | Many2one uom.uom, label Unit | 67-70 | stored compute `_compute_product_uom` (L207-210), `readonly=False`, `precompute`, required, domain on `allowed_uom_ids` |
| location_id | Many2one stock.location, Source Location | 75-80 | stored compute `_compute_location_id` (L212-222), `precompute`, `readonly=False`, indexed, required, `check_company` |
| location_dest_id | Many2one stock.location, Intermediate Location | 81-84 | stored compute `_compute_location_dest_id` (L224-244), inverse `_set_location_dest_id` (L246-252), `precompute`, required, indexed |
| location_final_id | Many2one stock.location, Final Location | 85-90 | stored, `readonly=False`, indexed, `check_company`, `bypass_search_access`; no compute; no `copy` attribute is declared, so the field default `copy=True` applies (`odoo/orm/fields.py:281`) |
| partner_id | Many2one res.partner, Destination Address | 93-97 | stored compute `_compute_partner_id` (from the picking partner), `readonly=False` |
| move_dest_ids, move_orig_ids | Many2many stock.move | 98-105 | one relation table `stock_move_move_rel`, columns swapped, `copy=False` |
| picking_id | Many2one stock.picking, Transfer | 106 | indexed, `check_company` |
| state | Selection, label Status | 107-120 | stored, default draft, readonly, `copy=False`, indexed |
| picked | Boolean | 121-124 | stored compute `_compute_picked` (L281-287), inverse `_inverse_picked` (L289-291), `readonly=False`, `copy=False` |
| price_unit | Float | 129 | `copy=False` |
| procure_method | Selection, Supply Method | 131-138 | stored plain, default `make_to_stock`, required, `copy=False` |
| scrap_id | Many2one stock.scrap | 139 | readonly, `check_company` |
| procurement_values | Json | 140 | `store=False` |
| reference_ids | Many2many stock.reference | 141-142 | relation table `stock_reference_move_rel` (move_id, reference_id) |
| rule_id | Many2one stock.rule | 143-145 | `ondelete='restrict'`, `check_company` |
| propagate_cancel | Boolean | 146-148 | default true |
| delay_alert_date | Datetime | 149 | stored compute `_compute_delay_alert_date` (L391-402) |
| picking_type_id | Many2one stock.picking.type | 150 | stored compute `_compute_picking_type_id`, `readonly=False` |
| is_inventory | Boolean | 151 | plain |
| origin_returned_move_id | Many2one stock.move | 155-157 | `copy=False`, indexed, `check_company` |
| returned_move_ids | One2many stock.move | 158 | inverse of `origin_returned_move_id` |
| availability | Float, Forecasted Quantity | 159-161 | non-stored compute `_compute_product_availability` (L492-503) |
| restrict_partner_id | Many2one res.partner, label Owner | 163-165 | `check_company`, index `btree_not_null` |
| route_ids | Many2many stock.route | 166-167 | relation table `stock_route_move` |
| quantity | Float | 171-172 | stored compute `_compute_quantity` (L411-441), inverse `_set_quantity` (L443-483), digits Product Unit |
| additional | Boolean | 178 | default false |
| reference | Char | 183 | stored compute `_compute_reference`; used as `_rec_name` |
| forecast_availability, forecast_expected_date | Float, Datetime | 190-191 | non-stored compute `_compute_forecast_information` (L505-581), `compute_sudo` |
| reservation_date | Date, Date to Reserve | 193 | stored compute `_compute_reservation_date` (L730-739) |
| packaging_uom_id, packaging_uom_qty | Many2one uom.uom, Float | 194-195 | stored computes, `precompute` on the unit |
| other declared fields (names and lines only) | various | product_category_id 43-45, product_tmpl_id 72-74, location_usage 91, location_dest_usage 92, origin 130, inventory_name 152, move_line_ids 153, package_ids 154, warehouse_id 168, is_quantity_done_editable 182, orderpoint_id 189, lot_ids 192 | not analysed further; see the excerpts in section 1.1 |

---

## 2. State machine

### 2.1 State values

`state` is declared at L107-120 as a plain Selection (no compute), default `'draft'`, `readonly=True`, `copy=False`, `index=True`. The help text (L116-120) documents five values (New, Waiting Another Move, Waiting, Available, Done) and omits `partially_available` and `cancel`. The excerpt of L106-151 in section 1.1 contains the declaration.

| Value | Label | Written by |
|---|---|---|
| draft | New | field default (L115); mrp `default_get` (`mrp/models/stock_move.py:18-20`) |
| waiting | Waiting Another Move | `_action_confirm` L1701-1706; `_recompute_state` L2431-2435 |
| confirmed | Waiting | `_action_confirm` L1707-1712; `_recompute_state` L2436-2437 |
| partially_available | Partially Available | `_action_assign` L2182-2184; `_recompute_state` L2429-2430; `write` L864 |
| assigned | Available | `_action_assign` L2182-2184; `_recompute_state` L2427-2428 |
| done | Done | `_action_done` L2290; `default_get` L784-785; `create` L829-830; mrp `default_get` (`mrp/models/stock_move.py:18-22`); mrp direct write (`mrp/models/mrp_production.py:2246-2249`) |
| cancel | Cancelled | `_action_cancel` L2199 |

### 2.2 Transition list

Notation: `FROM -> TO [trigger] pointer`.

- (new record) -> draft [field default] L115
- draft -> waiting [`_action_confirm`; the move already has `move_orig_ids`] L1701-1702
- draft -> waiting [`_action_confirm`; `procure_method == 'make_to_order'`; a procurement request is issued when `create_proc` is set] L1703-1706
- draft -> confirmed [`_action_confirm`; the matching rule has `procure_method == 'mts_else_mto'`; a procurement request is issued when `create_proc` is set] L1707-1710
- draft -> confirmed [`_action_confirm`; every other case] L1711-1712
- confirmed, waiting or partially_available -> assigned [`_action_assign`; reservation covers the missing quantity] L2079-2084, L2126-2127, L2182-2184
- confirmed, waiting or partially_available -> partially_available [`_action_assign`; reservation covers part of the missing quantity] L2182-2184
- any state except cancel, done, or draft-without-quantity -> assigned, partially_available, waiting or confirmed [`_recompute_state`] L2419-2439
- assigned -> partially_available [`write` of `product_uom_qty`] L855-872
- draft, waiting, confirmed, partially_available or assigned -> cancel [`_action_cancel`] L2192, L2199
- done with a destination location usage other than inventory -> no transition [`_action_cancel` raises a UserError for the whole recordset] L2190-2191
- done with destination location usage inventory -> unchanged [`_action_cancel` filters the move out of the cancel set and does not write it] L2192
- not done -> cancel [`_action_done`; the move is not picked or has no positive quantity, is not an inventory adjustment, and its demand is zero or `cancel_backorder` is set] L2262-2264
- picked moves with positive quantity (or inventory moves) -> done [`_action_done`] L2290

### 2.3 `_action_confirm` (L1688-1783)

```python
# stock/models/stock_move.py:1688-1783
    def _action_confirm(self, merge=True, merge_into=False, create_proc=True):
        """ Confirms stock move or put it in waiting if it's linked to another move.
        :param: merge: According to this boolean, a newly confirmed move will be merged
        in another move of the same picking sharing its characteristics.
        """
        # Use OrderedSet of id (instead of recordset + |= ) for performance
        consumed_from_stock_dict = self.env.context.get('consumed_from_stock_dict', defaultdict(float))
        move_create_proc, move_to_confirm, move_waiting = OrderedSet(), OrderedSet(), OrderedSet()
        to_assign = defaultdict(OrderedSet)
        for move in self:
            if move.state != 'draft':
                continue
            # if the move is preceded, then it's waiting (if preceding move is done, then action_assign has been called already and its state is already available)
            if move.move_orig_ids:
                move_waiting.add(move.id)
            elif move.procure_method == 'make_to_order':
                move_waiting.add(move.id)
                if create_proc:
                    move_create_proc.add(move.id)
            elif move.rule_id and move.rule_id.procure_method == 'mts_else_mto':
                move_to_confirm.add(move.id)
                if create_proc:
                    move_create_proc.add(move.id)
            else:
                move_to_confirm.add(move.id)
            if move._should_be_assigned():
                key = (frozenset(move.reference_ids.ids), move.location_id.id, move.location_dest_id.id)
                to_assign[key].add(move.id)

        # create procurements for make to order moves
        procurement_requests = []
        move_create_proc = self.browse(move_create_proc)
        quantities = move_create_proc.with_context(consumed_from_stock_dict=consumed_from_stock_dict)._prepare_procurement_qty()
        for move, quantity in zip(move_create_proc, quantities):
            values = move._prepare_procurement_values()
            origin = move._prepare_procurement_origin()
            procurement_requests.append(self.env['stock.rule'].Procurement(
                move.product_id, quantity, move.product_uom,
                move.location_id, move.rule_id and move.rule_id.name or "/",
                origin, move.company_id, values))
        self.env['stock.rule'].with_context(consumed_from_stock_dict=consumed_from_stock_dict).run(procurement_requests, raise_user_error=not self.env.context.get('from_orderpoint'))

        move_to_confirm, move_waiting = self.browse(move_to_confirm).filtered(lambda m: m.state != 'cancel'), self.browse(move_waiting).filtered(lambda m: m.state != 'cancel')
        move_to_confirm.write({'state': 'confirmed'})
        move_waiting.write({'state': 'waiting'})
        # procure_method sometimes changes with certain workflows so just in case, apply to all moves
        (move_to_confirm | move_waiting).filtered(lambda m: m.picking_type_id.reservation_method == 'at_confirm')\
            .write({'reservation_date': fields.Date.today()})

        # assign picking in batch for all confirmed move that share the same details
        for moves_ids in to_assign.values():
            self.browse(moves_ids).with_context(clean_context(self.env.context))._assign_picking()

        self._check_company()
        moves = self
        if merge:
            moves = self._merge_moves(merge_into=merge_into)

        neg_r_moves = moves.filtered(lambda move: move.product_uom.compare(move.product_uom_qty, 0) < 0)

        # Push remaining quantities to next step
        neg_to_push = neg_r_moves.filtered(lambda move: move.location_final_id and move.location_dest_id != move.location_final_id)
        new_push_moves = self.env['stock.move']
        if neg_to_push:
            new_push_moves = neg_to_push._push_apply()

        # Transform remaining move in returns in case of negative initial demand
        for move in neg_r_moves:
            move.location_id, move.location_dest_id, move.location_final_id = move.location_dest_id, move.location_id, move.location_id
            orig_move_ids, dest_move_ids = [], []
            for m in move.move_orig_ids | move.move_dest_ids:
                from_loc, to_loc = m.location_id, m.location_dest_id
                if m.product_uom.compare(m.product_uom_qty, 0) < 0:
                    from_loc, to_loc = to_loc, from_loc
                if to_loc == move.location_id:
                    orig_move_ids += m.ids
                elif move.location_dest_id == from_loc:
                    dest_move_ids += m.ids
            move.move_orig_ids, move.move_dest_ids = [Command.set(orig_move_ids)], [Command.set(dest_move_ids)]
            move.product_uom_qty *= -1
            if move.picking_type_id.return_picking_type_id:
                move.picking_type_id = move.picking_type_id.return_picking_type_id
            # We are returning some products, we must take them in the source location
            move.procure_method = 'make_to_stock'
        neg_r_moves._assign_picking()

        # call `_action_assign` on every confirmed move which location_id bypasses the reservation + those expected to be auto-assigned
        moves.filtered(lambda move: move.state in ('confirmed', 'partially_available')
                       and (move._should_bypass_reservation() or move._should_assign_at_confirm()))\
             ._action_assign()
        if new_push_moves:
            neg_push_moves = new_push_moves.filtered(lambda sm: sm.product_uom.compare(sm.product_uom_qty, 0) < 0)
            (new_push_moves - neg_push_moves).sudo()._action_confirm()
            # Negative moves do not have any picking, so we should try to merge it with their siblings
            neg_push_moves._action_confirm(merge_into=neg_push_moves.move_orig_ids.move_dest_ids)
        return moves
```

Reading notes (all pointers are lines of the excerpt above):

- Moves that are not in draft are skipped (L1697-1699); moves cancelled while the procurement requests ran are filtered out before the state writes (L1730-1732).
- L1701-1712 decide the new state per move (section 2.2). The procurement request is built by `_prepare_procurement_qty`, `_prepare_procurement_values` and `_prepare_procurement_origin` and sent through `stock.rule.run` (L1717-1728).
- L1713-1715 build the picking-assignment key `(frozenset(reference_ids.ids), location_id.id, location_dest_id.id)` for moves that satisfy `_should_be_assigned()`; `_assign_picking` runs at L1738-1739.
- L1734-1735 stamp `reservation_date` with today for moves whose picking type reserves at confirmation.
- L1741 runs `_check_company`; L1743-1744 merges moves with `_merge_moves` unless merging is switched off by the caller (`_action_done` passes `merge=False`).
- Negative demand (L1746): moves whose demand is below zero at the unit rounding are collected. Those with a final location that differs from the destination first go through `_push_apply` (L1749-1752). Each negative move is then transformed (L1755-1772): the source becomes the former destination, and both the destination and the final location become the former source (L1756); `move_orig_ids` and `move_dest_ids` are rebuilt from the neighbouring moves by comparing locations (L1757-1766); `product_uom_qty` is multiplied by -1 (L1767); the return picking type of the operation type is set when it has one (L1768-1769); `procure_method` is forced to `make_to_stock` (L1770-1771); `_assign_picking` runs for these moves (L1772).
- L1775-1777 call `_action_assign` for confirmed or partially available moves that bypass reservation or must be assigned at confirmation (`_should_bypass_reservation`, `_should_assign_at_confirm`); L1778-1782 confirm the new push moves; push moves with negative demand are confirmed separately with `merge_into` set to `neg_push_moves.move_orig_ids.move_dest_ids` (L1782).

### 2.4 `_recompute_state` (L2419-2439)

```python
# stock/models/stock_move.py:2419-2439
    def _recompute_state(self):
        if self.env.context.get('preserve_state'):
            return
        moves_state_to_write = defaultdict(set)
        for move in self:
            rounding = move.product_uom.rounding
            if move.state in ('cancel', 'done') or (move.state == 'draft' and not move.quantity):
                continue
            elif float_compare(move.quantity, move.product_uom_qty, precision_rounding=rounding) >= 0:
                moves_state_to_write['assigned'].add(move.id)
            elif move.quantity and float_compare(move.quantity, move.product_uom_qty, precision_rounding=rounding) <= 0:
                moves_state_to_write['partially_available'].add(move.id)
            elif (move.procure_method == 'make_to_order' and not move.move_orig_ids) or\
                 (move.move_orig_ids and any(orig.product_uom.compare(orig.product_uom_qty, 0) > 0
                                             and orig.state not in ('done', 'cancel') for orig in move.move_orig_ids)):
                # In the process of merging a negative move, we may still have a negative move in the move_orig_ids at that point.
                moves_state_to_write['waiting'].add(move.id)
            else:
                moves_state_to_write['confirmed'].add(move.id)
        for state, moves_ids in moves_state_to_write.items():
            self.browse(moves_ids).filtered(lambda m: m.state != state).state = state
```

Reading notes:

- The context key `preserve_state` turns the method into a no-op (L2420-2421).
- Cancelled moves, done moves and draft moves without quantity are skipped (L2425).
- `quantity >= product_uom_qty` gives assigned (L2427-2428); a positive `quantity` at or below the demand gives partially_available (L2429-2430).
- Otherwise a make-to-order move without origin moves, or a move with an open origin move of positive demand, gives waiting (L2431-2435); every other move gives confirmed (L2436-2437).
- A write happens only when the computed state differs (L2438-2439). `_action_assign` does not call this method for its own state writes (section 5).

### 2.5 `_action_cancel` (L2189-2232)

```python
# stock/models/stock_move.py:2189-2232
    def _action_cancel(self):
        if any(move.state == 'done' and move.location_dest_usage != 'inventory' for move in self):
            raise UserError(_('You cannot cancel a stock move that has been set to \'Done\'. Create a return in order to reverse the moves which took place.'))
        moves_to_cancel = self.filtered(lambda m: m.state != 'cancel' and not (m.state == 'done' and m.location_dest_usage == 'inventory'))
        moves_to_cancel.picked = False
        # self cannot contain moves that are either cancelled or done, therefore we can safely
        # unlink all associated move_line_ids
        moves_to_cancel._do_unreserve()
        cancel_moves_origin = self.env['ir.config_parameter'].sudo().get_param('stock.cancel_moves_origin')

        moves_to_cancel.state = 'cancel'

        for move in moves_to_cancel:
            siblings_states = (move.move_dest_ids.mapped('move_orig_ids') - move).mapped('state')
            if move.propagate_cancel:
                # only cancel the next move if all my siblings are also cancelled
                if all(state == 'cancel' for state in siblings_states):
                    move_dest_to_cancel = move.move_dest_ids.filtered(lambda m: m.state != 'done' and move.location_dest_id == m.location_id)
                    move_dest_to_cancel._action_cancel()
                    # Unlink from dest if dest is not in the chain
                    (move.move_dest_ids - move_dest_to_cancel).write({
                        'procure_method': 'make_to_stock',
                        'move_orig_ids': [Command.unlink(move.id)]
                    })
                    if cancel_moves_origin:
                        move.move_orig_ids.sudo().filtered(lambda m: m.state != 'done')._action_cancel()
            else:
                if all(state in ('done', 'cancel') for state in siblings_states):
                    move_dest_ids = move.move_dest_ids
                    move_dest_ids.write({
                        'procure_method': 'make_to_stock',
                        'move_orig_ids': [Command.unlink(move.id)]
                    })
        if not self.env.context.get('skip_cancel_activity'):
            # log an activity on the non-cancelled origin to warn the user that some actions might be required
            moves_to_cancel._log_cancel_activity()
        moves_to_cancel.write({
            'move_orig_ids': [(5, 0, 0)],
            'procure_method': 'make_to_stock',
        })
        return True

    def _log_cancel_activity(self):
        return
```

Reading notes:

- A UserError is raised when any move of the recordset is done and its destination location usage is not inventory (L2190-2191). Done moves with an inventory destination, and moves that are already cancelled, are filtered out of the cancel set (L2192); the rest of the method does not touch them.
- Each move in the cancel set is unpicked (L2193) and its reservation released through `_do_unreserve` (L2196) before the state write at L2199.
- The system parameter `stock.cancel_moves_origin` is read at L2197; when set, open origin moves are cancelled too (L2213-2214).
- With `propagate_cancel` (L2203), destination moves are cancelled recursively only when all sibling origin moves are cancelled (L2205); destination moves that are not done and start at the cancelled move's destination are cancelled (L2206-2207); the other destination moves become make_to_stock and the link is removed (L2209-2212).
- Without `propagate_cancel`, once all siblings are done or cancelled the destination moves become make_to_stock and are unlinked from the cancelled move (L2215-2221).
- `_log_cancel_activity` (L2222-2224 call; stub at L2231-2232) is skipped when the context contains `skip_cancel_activity`; finally the cancelled move loses its `move_orig_ids` (command 5) and its `procure_method` becomes make_to_stock (L2225-2228).

---

## 3. Quantity fields

### 3.1 Roles

| Field | Role | Storage | Pointer |
|---|---|---|---|
| product_uom_qty | Demand in the move unit | stored plain, digits Product Unit, default 0, required | L58-65 |
| product_uom | Unit of the demand | stored compute, `readonly=False`, domain on `allowed_uom_ids` | L67-70, L207-210 |
| product_qty | Demand converted into the product default unit | stored compute with HALF-UP conversion; inverse raises | L54-57, L380-384, L485-490 |
| quantity | Sum of move-line quantities in the move unit | stored compute and inverse | L171-172, L411-483 |
| picked | Indicative flag derived from the lines | stored compute and inverse | L121-124, L281-291 |
| packaging_uom_id, packaging_uom_qty | Packaging unit and quantity from the commercial line | stored computes | L194-195 |

### 3.2 `picked` and `priority` computes

```python
# stock/models/stock_move.py:281-296
    @api.depends('move_line_ids.picked', 'state')
    def _compute_picked(self):
        for move in self:
            if move.state == 'done' or any(ml.picked for ml in move.move_line_ids):
                move.picked = True
            elif move.move_line_ids:
                move.picked = False

    def _inverse_picked(self):
        for move in self:
            move.move_line_ids.picked = move.picked

    @api.depends('picking_id.priority')
    def _compute_priority(self):
        for move in self:
            move.priority = move.picking_id.priority or '0'
```

`_compute_picked` marks a move picked when it is done or when any of its move lines is picked (L284-285); it clears the flag only when the move has lines and none is picked (L287). The inverse writes the same flag onto every move line (L289-291). `priority` is a stored compute copied from the picking priority (L293-296).

### 3.3 `product_qty`, `quantity`, `_set_quantity`

```python
# stock/models/stock_move.py:380-384
    @api.depends('product_id', 'product_uom', 'product_uom_qty', 'state')
    def _compute_product_qty(self):
        for move in self:
            move.product_qty = move.product_uom._compute_quantity(
                move.product_uom_qty, move.product_id.uom_id, rounding_method='HALF-UP')
```

```python
# stock/models/stock_move.py:404-441
    def _quantity_sml(self):
        self.ensure_one()
        quantity = 0
        for move_line in self.move_line_ids:
            quantity += move_line.product_uom_id._compute_quantity(move_line.quantity, self.product_uom, round=False)
        return quantity

    @api.depends('move_line_ids.quantity', 'move_line_ids.product_uom_id')
    def _compute_quantity(self):
        """ This field represents the sum of the move lines `quantity`. It allows the user to know
        if there is still work to do.

        We take care of rounding this value at the general decimal precision and not the rounding
        of the move's UOM to make sure this value is really close to the real sum, because this
        field will be used in `_action_done` in order to know if the move will need a backorder or
        an extra move.
        """
        if not any(self._ids):
            # onchange
            for move in self:
                move.quantity = move._quantity_sml()
        else:
            # compute
            move_lines_ids = set()
            for move in self:
                move_lines_ids |= set(move.move_line_ids.ids)

            data = self.env['stock.move.line']._read_group(
                [('id', 'in', list(move_lines_ids))],
                ['move_id', 'product_uom_id'], ['quantity:sum']
            )
            sum_qty = defaultdict(float)
            for move, product_uom, qty_sum in data:
                uom = move.product_uom
                sum_qty[move.id] += product_uom._compute_quantity(qty_sum, uom, round=False)

            for move in self:
                move.quantity = sum_qty[move.id]
```

```python
# stock/models/stock_move.py:443-490
    def _set_quantity(self):
        def _process_decrease(move, quantity):
            mls_to_unlink = set()
            # Since the move lines might have been created in a certain order to respect
            # a removal strategy, they need to be unreserved in the opposite order
            for ml in reversed(move.move_line_ids.sorted('id')):
                if self.env.context.get('unreserve_unpicked_only') and ml.picked:
                    continue
                if move.product_uom.is_zero(quantity):
                    break
                qty_ml_dec = min(ml.quantity, move.product_uom._compute_quantity(quantity, ml.product_uom_id, round=False))
                if ml.product_uom_id.is_zero(qty_ml_dec):
                    continue
                if ml.product_uom_id.compare(ml.quantity, qty_ml_dec) == 0 and ml.state not in ['done', 'cancel']:
                    mls_to_unlink.add(ml.id)
                else:
                    ml.quantity -= qty_ml_dec
                quantity -= ml.product_uom_id._compute_quantity(qty_ml_dec, move.product_uom, round=False)
            self.env['stock.move.line'].browse(mls_to_unlink).unlink()

        def _process_increase(move, quantity):
            # move._action_assign(quantity)
            move._set_quantity_done(move.quantity)

        err = []
        precision_digits = self.env['decimal.precision'].precision_get('Product Unit')
        for move in self:
            rounded_qty = float_round(move.quantity, precision_digits=precision_digits, rounding_method='HALF-UP')
            if float_compare(rounded_qty, move.quantity, precision_digits=precision_digits) != 0:
                err.append(_("""
The quantity done for the product %(product)s doesn't respect the rounding precision defined on the system.
Please change the quantity done or the rounding precision in your settings.""",
                             product=move.product_id.display_name))
                continue
            delta_qty = move.quantity - move._quantity_sml()
            if move.product_uom.compare(delta_qty, 0) > 0:
                _process_increase(move, delta_qty)
            elif move.product_uom.compare(delta_qty, 0) < 0:
                _process_decrease(move, abs(delta_qty))
        if err:
            raise UserError('\n'.join(err))

    def _set_product_qty(self):
        """ The meaning of product_qty field changed lately and is now a functional field computing the quantity
        in the default product UoM. This code has been added to raise an error if a write is made given a value
        for `product_qty`, where the same write should set the `product_uom_qty` field instead, in order to
        detect errors. """
        raise UserError(_('The requested operation cannot be processed because of a programming error setting the `product_qty` field instead of the `product_uom_qty`.'))
```

Reading notes:

- `_compute_product_qty` converts the demand into the product default unit with rounding method HALF-UP (L383-384).
- `_compute_quantity` sums the move-line quantities, converting each line unit into the move unit with `round=False` (L408, L438). The docstring (L413-420) says the value is rounded at the general decimal precision and that it is used in `_action_done` to decide on a backorder or an extra move; the code does not round (`round=False`), and no `_create_extra_move` exists in the tree (see M-08 and M-17). Treat the docstring as stale text.
- On saved records the sums come from one grouped read of `stock.move.line` (L431-434); in an onchange context (`not any(self._ids)`) the sums are added line by line through `_quantity_sml` (L421-424, L404-409).
- `_set_quantity` first checks that `quantity` respects the `Product Unit` precision (HALF-UP round and compare, L468-476) and collects a UserError text otherwise (L472-475, raised at L482-483). A positive delta against the line sum goes to `_set_quantity_done(move.quantity)` (L465, L478-479); a negative delta unreserves lines in reverse id order, skipping picked lines when the context contains `unreserve_unpicked_only` (L444-461, L480-481).
- `_set_product_qty` always raises a UserError (L485-490); writes must target `product_uom_qty`.
- Legacy names: grep over this file shows `quantity_done` and `reserved_availability` only in a stale comment (L2059), a local dictionary named `reserved_availability` (L2061, L2079), a stale comment (L2405) and the method names `_set_quantity_done_prepare_vals` (L2476) and `_set_quantity_done` (L2559); the Boolean `is_quantity_done_editable` is declared at L182. None of them is a stored quantity field of the move. Detail on move-line quantities is in U219.

### 3.4 Availability and forecast fields (informational)

```python
# stock/models/stock_move.py:492-581
    @api.depends('state', 'product_id', 'product_qty', 'location_id')
    def _compute_product_availability(self):
        """ Fill the `availability` field on a stock move, which is the quantity to potentially
        reserve. When the move is done, `availability` is set to the quantity the move did actually
        move.
        """
        for move in self:
            if move.state == 'done':
                move.availability = move.product_qty
            else:
                total_availability = self.env['stock.quant']._get_available_quantity(move.product_id, move.location_id) if move.product_id else 0.0
                move.availability = min(move.product_qty, total_availability)

    @api.depends('product_id', 'product_qty', 'picking_type_id', 'quantity', 'priority', 'state', 'product_uom_qty', 'location_id')
    def _compute_forecast_information(self):
        """ Compute forecasted information of the related product by warehouse."""
        self.forecast_availability = False
        self.forecast_expected_date = False

        # Prefetch product info to avoid fetching all product fields
        self.product_id.fetch(['type', 'uom_id'])

        not_product_moves = self.filtered(lambda move: not move.product_id.is_storable)
        for move in not_product_moves:
            move.forecast_availability = move.product_qty

        product_moves = (self - not_product_moves)

        outgoing_unreserved_moves_per_warehouse = defaultdict(set)
        now = fields.Datetime.now()

        def key_virtual_available(move, incoming=False):
            warehouse_id = move.location_dest_id.warehouse_id.id if incoming else move.location_id.warehouse_id.id
            return warehouse_id, max(move.date or now, now)

        # Prefetch efficiently virtual_available for _is_consuming draft move.
        prefetch_virtual_available = defaultdict(set)
        virtual_available_dict = {}
        for move in product_moves:
            if move._is_consuming() and move.state == 'draft' or move.picking_type_id.code == 'internal':
                prefetch_virtual_available[key_virtual_available(move)].add(move.product_id.id)
            elif move.picking_type_id.code == 'incoming':
                prefetch_virtual_available[key_virtual_available(move, incoming=True)].add(move.product_id.id)
        for key_context, product_ids in prefetch_virtual_available.items():
            read_res = self.env['product.product'].browse(product_ids).with_context(warehouse_id=key_context[0], to_date=key_context[1]).read([
                'virtual_available',
                'free_qty',
            ])
            virtual_available_dict[key_context] = {res['id']: (res['virtual_available'], res['free_qty']) for res in read_res}

        for move in product_moves:
            if key_virtual_available(move) in virtual_available_dict and move.product_id.id in virtual_available_dict[key_virtual_available(move)]:
                free_qty = virtual_available_dict[key_virtual_available(move)][move.product_id.id][1]
            else:
                free_qty = 0.0
            if move.state == 'assigned':
                move.forecast_availability = move.product_uom._compute_quantity(
                    move.quantity, move.product_id.uom_id, rounding_method='HALF-UP')
                continue
            elif move.state == 'draft' and float_compare(free_qty, move.product_qty, precision_rounding=move.product_id.uom_id.rounding) >= 0:
                move.forecast_availability = free_qty
                continue
            if move._is_consuming():
                if move.state == 'draft':
                    free_qty = virtual_available_dict[key_virtual_available(move)][move.product_id.id][0]
                    if float_compare(free_qty, move.product_qty, precision_rounding=move.product_id.uom_id.rounding) >= 0:
                        move.forecast_availability = free_qty
                        continue
                    # for move _is_consuming and in draft -> the forecast_availability > 0 if in stock
                    move.forecast_availability = free_qty - move.product_qty
                elif move.state in ('waiting', 'confirmed', 'partially_available'):
                    outgoing_unreserved_moves_per_warehouse[move.location_id.warehouse_id].add(move.id)
            elif move.picking_type_id.code == 'internal':
                if float_compare(free_qty, move.product_qty, precision_rounding=move.product_id.uom_id.rounding) >= 0:
                    move.forecast_availability = free_qty
                    continue
            elif move.picking_type_id.code == 'incoming':
                forecast_availability = virtual_available_dict[key_virtual_available(move, incoming=True)][move.product_id.id][0]
                if move.state == 'draft':
                    forecast_availability += move.product_qty
                move.forecast_availability = forecast_availability

        for warehouse, moves_ids in outgoing_unreserved_moves_per_warehouse.items():
            if not warehouse:  # No prediction possible if no warehouse.
                continue
            moves_per_location = self.browse(moves_ids).grouped('location_id')
            for location, mvs in moves_per_location.items():
                forecast_info = mvs._get_forecast_availability_outgoing(warehouse, location)
                for move in mvs:
                    move.forecast_availability, move.forecast_expected_date = forecast_info[move]
```

`availability` and `forecast_availability` are not stored and are not read by `_action_assign`; reservation uses quants and chained move lines (section 5).

---

## 4. procure_method, move chains and rules

### 4.1 Field and value set

`procure_method` (L131-138) is a stored Selection labelled Supply Method with `make_to_stock` ("Default: Take From Stock") and `make_to_order` ("Advanced: Apply Procurement Rules"); default `make_to_stock`, required, `copy=False`. The rule-level value `mts_else_mto` is never stored on a move: `_run_pull` maps it to `make_to_stock` for the created move (`stock/models/stock_rule.py:305-310`).

Chain links: `move_dest_ids` and `move_orig_ids` (L98-105) are two Many2many fields over the same table `stock_move_move_rel` with swapped column names, both `copy=False`. `rule_id` (L143-145) records the creating rule (`ondelete='restrict'`); `propagate_cancel` (L146-148) defaults to true.

### 4.2 Where the value is written

| Place | Effect | Pointer |
|---|---|---|
| field default | make_to_stock | L134 |
| `stock.rule._get_stock_move_values` and `_run_pull` | the created move receives the rule value, with `mts_else_mto` mapped to make_to_stock | `stock/models/stock_rule.py:305-310`, `stock/models/stock_rule.py:369` |
| `_adjust_procure_method` | looks up a non-push rule and copies make_to_stock or make_to_order, otherwise make_to_stock | L2572-2607 |
| `_action_confirm` negative demand | forces make_to_stock | L1755-1772 |
| `_action_cancel` | destination moves of a cancelled move, and the cancelled move itself, become make_to_stock | L2209-2221, L2225-2228 |
| `write` with a changed `location_id` | make_to_stock and cleared links | L877-894 |
| `_break_mto_link` | removes one parent link, sets make_to_stock, recomputes state | L2794-2797 |
| `_prepare_move_split_vals` | the split-off move copies the value | L2353-2365 |

### 4.3 Procurement preparation at confirmation (L1785-1867)

```python
# stock/models/stock_move.py:1785-1867
    def _prepare_procurement_origin(self):
        self.ensure_one()
        return (self.reference_ids and self.reference_ids[0].name) or self.origin or self.picking_id.display_name

    def _prepare_procurement_qty(self):
        consumed_from_stock_dict = self.env.context.get('consumed_from_stock_dict', defaultdict(float))
        quantities = []
        mtso_products_by_locations = defaultdict(list)
        mtso_moves = set()
        for move in self:
            if move.rule_id and move.rule_id.procure_method == 'mts_else_mto':
                mtso_moves.add(move.id)
                mtso_products_by_locations[move.location_id].append(move.product_id.id)

        # Get the forecasted quantity for the `mts_else_mto` procurement.
        forecasted_qties_by_loc = {}
        for location, product_ids in mtso_products_by_locations.items():
            if location.should_bypass_reservation():
                continue
            products = self.env['product.product'].browse(product_ids).with_context(location=location.id)
            forecasted_qties_by_loc[location] = {product.id: product.free_qty for product in products}
        for move in self:
            if move.id not in mtso_moves or move.product_id.uom_id.compare(move.product_qty, 0) <= 0:
                quantities.append(move.product_uom_qty)
                continue

            if move._should_bypass_reservation():
                quantities.append(move.product_uom_qty)
                continue

            free_qty = max(forecasted_qties_by_loc[move.location_id][move.product_id.id] - consumed_from_stock_dict[move.location_id, move.product_id.id], 0)
            quantity = max(move.product_qty - free_qty, 0)
            product_uom_qty = move.product_id.uom_id._compute_quantity(quantity, move.product_uom, rounding_method='HALF-UP')
            quantities.append(product_uom_qty)
            consumed_from_stock_dict[move.location_id, move.product_id.id] += min(move.product_qty, free_qty)

        return quantities

    def _get_partner_id(self):
        self.ensure_one()
        if self.location_id == self.env.company.internal_transit_location_id:
            return self.location_dest_id.warehouse_id.partner_id.id
        return self.partner_id.id

    def _prepare_procurement_values(self):
        """ Prepare specific key for moves or other componenets that will be created from a stock rule
        comming from a stock move. This method could be override in order to add other custom key that could
        be used in move/po creation.
        """
        self.ensure_one()

        product_id = self.product_id.with_context(lang=self._get_lang())
        dates_info = {'date_planned': self._get_mto_procurement_date()}
        route = self.route_ids
        if not route:
            related_packages = self.env['stock.package'].search_fetch([('id', 'parent_of', self.move_line_ids.result_package_id.ids)], ['package_type_id'])
            route = related_packages.package_type_id.route_ids
        if self.location_id.warehouse_id and self.location_id.warehouse_id.lot_stock_id.parent_path in self.location_id.parent_path:
            dates_info = self.product_id._get_dates_info(self.date, self.location_id, route_ids=route)
        warehouse = self.warehouse_id or self.picking_type_id.warehouse_id
        if not self.location_id.warehouse_id:
            warehouse = self.rule_id.route_id.supplier_wh_id

        move_dest_ids = False
        if self.procure_method == "make_to_order":
            move_dest_ids = self
        return {
            # TODO CLPI: maybe make this a little cleaner
            'product_description_variants': self.description_picking and self.description_picking.replace(product_id._get_description(self.picking_type_id), '').replace(product_id._get_picking_description(self.picking_type_id) or '', ''),
            'never_product_template_attribute_value_ids': self.never_product_template_attribute_value_ids,
            'date_planned': dates_info.get('date_planned'),
            'date_order': dates_info.get('date_order'),
            'date_deadline': self.date_deadline,
            'move_dest_ids': move_dest_ids,
            'partner_id': self._get_partner_id() if self.rule_id.procure_method in ('make_to_order', 'mts_else_mto') else False,
            'route_ids': route,
            'warehouse_id': warehouse,
            'priority': self.priority,
            'reference_ids': self.reference_ids,
            'orderpoint_id': self.orderpoint_id,
            'packaging_uom_id': self.packaging_uom_id,
            'procurement_values': self.procurement_values,
        }
```

Reading notes:

- `_prepare_procurement_qty` (L1789-1821) handles the `mts_else_mto` rule value (L1795): the available stock is the free quantity of the product at the source location (`product.free_qty`, L1801-1805) minus what earlier moves of the same run already consumed, floored at zero (L1815); the quantity to procure is the product quantity minus that available stock, floored at zero and converted back into the move unit with HALF-UP (L1816-1817); the consumed dictionary grows by the smaller of the product quantity and the available stock (L1819). Moves that are not stock-else-order moves, have no positive product quantity, or bypass reservation procure their full demand (L1807-1813).
- `_prepare_procurement_values`: a make-to-order move passes itself as `move_dest_ids` of the procurement (L1849-1850), so the move created by the rule is chained in front of it; the partner is propagated only for make_to_order moves or rules of type `mts_else_mto` (L1859); `reference_ids` is copied (L1863).

### 4.4 Rule side: `_run_pull`, `_get_custom_move_fields`, `_get_stock_move_values`

```python
# stock/models/stock_rule.py:289-387
    @api.model
    def _run_pull(self, procurements):
        moves_values_by_company = defaultdict(list)

        # To handle the `mts_else_mto` procure method, we do a preliminary loop to
        # isolate the products we would need to read the forecasted quantity,
        # in order to to batch the read. We also make a sanitary check on the
        # `location_src_id` field.
        for procurement, rule in procurements:
            if not rule.location_src_id:
                msg = _('No source location defined on stock rule: %s!', rule.name)
                raise ProcurementException([(procurement, msg)])

        # Prepare the move values, adapt the `procure_method` if needed.
        procurements = sorted(procurements, key=lambda proc: proc[0].product_uom.compare(proc[0].product_qty, 0.0) > 0)
        for procurement, rule in procurements:
            procure_method = rule.procure_method
            if rule.procure_method == 'mts_else_mto':
                procure_method = 'make_to_stock'

            move_values = rule._get_stock_move_values(*procurement)
            move_values['procure_method'] = procure_method
            moves_values_by_company[procurement.company_id.id].append(move_values)

        for company_id, moves_values in moves_values_by_company.items():
            # create the move as SUPERUSER because the current user may not have the rights to do it (mto product launched by a sale for example)
            moves = self.env['stock.move'].sudo().with_company(company_id).create(moves_values)
            # Since action_confirm launch following procurement_group we should activate it.
            moves._action_confirm()
        return True

    def _get_custom_move_fields(self):
        """ The purpose of this method is to be override in order to easily add
        fields from procurement 'values' argument to move data.
        """
        return []

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_dest_id, name, origin, company_id, values):
        ''' Returns a dictionary of values that will be used to create a stock move from a procurement.
        This function assumes that the given procurement has a rule (action == 'pull' or 'pull_push') set on it.

        :rtype: dictionary
        '''

        date_scheduled = fields.Datetime.to_string(
            fields.Datetime.from_string(values['date_planned']) - relativedelta(days=self.delay or 0)
        )
        date_deadline = values.get('date_deadline') and (fields.Datetime.to_datetime(values['date_deadline']) - relativedelta(days=self.delay or 0)) or False
        partner = self.partner_address_id.id or values.get('partner_id', False)
        # it is possible that we've already got some move done, so check for the done qty and create
        # a new move with the correct qty
        qty_left = product_qty

        move_dest_ids = values.get('move_dest_ids') and [(4, x.id) for x in values['move_dest_ids']] or []

        # when create chained moves for inter-warehouse transfers, set the warehouses as partners
        if move_dest_ids:
            move_dest = values['move_dest_ids']
            if location_dest_id == company_id.internal_transit_location_id:
                if not partner:
                    partners = move_dest.location_dest_id.warehouse_id.partner_id
                    if len(partners) == 1:
                        partner = partners.id
                move_dest.partner_id = self.location_src_id.warehouse_id.partner_id or self.company_id.partner_id

        # If the quantity is negative the move should be considered as a refund
        if product_uom.compare(product_qty, 0.0) < 0:
            values['to_refund'] = True

        move_values = {
            'company_id': self.company_id.id or self.location_src_id.company_id.id or self.location_dest_id.company_id.id or company_id.id,
            'product_id': product_id.id,
            'product_uom': product_uom.id,
            'product_uom_qty': qty_left,
            'partner_id': partner,
            'location_id': self.location_src_id.id,
            'location_final_id': location_dest_id.id,
            'move_dest_ids': move_dest_ids,
            'rule_id': self.id,
            'reference_ids': [Command.set(values.get('reference_ids', self.env['stock.reference']).ids)],
            'procure_method': self.procure_method,
            'origin': origin,
            'picking_type_id': self.picking_type_id.id,
            'procurement_values': self._serialize_procurement_values(values),
            'route_ids': [Command.clear()] + [Command.link(route.id) for route in values.get('route_ids', [])],
            'never_product_template_attribute_value_ids': values.get('never_product_template_attribute_value_ids'),
            'warehouse_id': self.warehouse_id.id,
            'date': date_scheduled,
            'date_deadline': date_deadline,
            'propagate_cancel': self.propagate_cancel,
            'priority': values.get('priority', "0"),
            'orderpoint_id': values.get('orderpoint_id') and values['orderpoint_id'].id,
        }
        if self.location_dest_from_rule:
            move_values['location_dest_id'] = self.location_dest_id.id
        for field in self._get_custom_move_fields():
            if field in values:
                move_values[field] = values.get(field)
        return move_values
```

Reading notes:

- L297-300 reject a rule without source location; L303 sorts the procurements so that non-positive quantities come first; L305-310 compute and overwrite `procure_method` in the move values; L315-317 create the moves as superuser in the procurement company and confirm them.
- `_get_stock_move_values` (L326-387): chain link `move_dest_ids` from the procurement values (L342, L366); `location_final_id` receives the procurement destination (L365); `rule_id` (L367); `reference_ids` copied from the procurement values (L368); `propagate_cancel` from the rule (L378); `location_dest_id` is written only when the rule declares its own destination (L382-383); custom fields declared by `_get_custom_move_fields` are copied (L384-386).
- Negative procurement quantity sets `values['to_refund'] = True` (L355-356) although `to_refund` is declared in stock_account (section 9).

### 4.5 `_adjust_procure_method` (L2572-2607)

```python
# stock/models/stock_move.py:2572-2607
    def _adjust_procure_method(self, picking_type_code=False):
        """ This method will try to apply the procure method MTO on some moves if
        a compatible MTO route is found. Else the procure method will be set to MTS
        picking_type_code (str, optional): Adjusts the procurement method based on
            the specified picking type code. The code to specify the picking type for
            the procurement group. Defaults to False.
        """
        # Prepare the MTSO variables. They are needed since MTSO moves are handled separately.
        # We need 2 dicts:
        # - needed quantity per location per product
        # - forecasted quantity per location per product

        for move in self:
            product_id = move.product_id
            location = move.location_id
            while location:
                domain = [
                    ('location_src_id', '=', location.id),
                    ('location_dest_id', '=', move.location_dest_id.id),
                    ('action', '!=', 'push')
                ]
                if picking_type_code:
                    domain.append(('picking_type_id.code', '=', picking_type_code))
                rule = self.env['stock.rule']._search_rule(False, move.packaging_uom_id, product_id, move.warehouse_id or move.picking_type_id.warehouse_id, domain)
                if rule:
                    break
                location = location.location_id
            if not rule:
                move.procure_method = 'make_to_stock'
                continue

            move.rule_id = rule.id
            if rule.procure_method in ['make_to_stock', 'make_to_order']:
                move.procure_method = rule.procure_method
            else:
                move.procure_method = 'make_to_stock'
```

The method walks from the source location up through its parents looking for a non-push rule with `_search_rule`; without a rule the move becomes make_to_stock (L2599-2601); with a rule it stores `rule_id` (L2603) and copies the rule value only for make_to_stock or make_to_order, any other rule value giving make_to_stock (L2604-2607). Grep over the addon tree finds callers only in manufacturing and repair code and one test: `mrp/models/mrp_production.py:1505`, `mrp/models/mrp_production.py:1656`, `mrp/models/mrp_production.py:2580`, `mrp/models/stock_move.py:324`, `mrp/models/stock_move.py:401`, `repair/models/repair.py:629`, `repair/models/stock_move.py:109`, `stock/tests/test_move2.py:3264-3311`. No base stock code calls it.

### 4.6 Push rules

```python
# stock/models/stock_move.py:1214-1264
    def _push_apply(self):
        new_moves = []
        for move in self:
            new_move = self.env['stock.move']

            # if the move is a returned move, we don't want to check push rules, as returning a returned move is the only decent way
            # to receive goods without triggering the push rules again (which would duplicate chained operations)
            # first priority goes to the preferred routes defined on the move itself (e.g. coming from a SO line)
            warehouse_id = move.warehouse_id or move.picking_id.picking_type_id.warehouse_id

            StockRule = self.env['stock.rule']
            if move.location_dest_id.company_id not in self.env.companies:
                StockRule = self.env['stock.rule'].sudo()
                move = move.with_context(allowed_companies=self.env.user.company_ids.ids)
                warehouse_id = False

            related_packages = self.env['stock.package'].search_fetch([('id', 'parent_of', move.move_line_ids.result_package_id.ids)], ['package_type_id'])

            rule = StockRule._get_push_rule(move.product_id, move.location_dest_id, {
                'route_ids': move.route_ids | related_packages.package_type_id.route_ids, 'warehouse_id': warehouse_id, 'packaging_uom_id': move.packaging_uom_id,
            })

            excluded_rule_ids = []
            while (rule and rule.push_domain and not move.filtered_domain(literal_eval(rule.push_domain))):
                excluded_rule_ids.append(rule.id)
                rule = StockRule._get_push_rule(move.product_id, move.location_dest_id, {
                    'route_ids': move.route_ids | related_packages.package_type_id.route_ids, 'warehouse_id': warehouse_id, 'packaging_uom_id': move.packaging_uom_id,
                    'domain': [('id', 'not in', excluded_rule_ids)],
                })

            # Make sure it is not returning the return
            if rule and (not move.origin_returned_move_id or move.origin_returned_move_id.location_dest_id.id != rule.location_dest_id.id):
                new_move = rule._run_push(move) or new_move
                if new_move:
                    new_moves.append(new_move)

            move_to_propagate_ids = set()
            move_to_mts_ids = set()
            for m in move.move_dest_ids - new_move:
                if new_move and move.location_final_id and m.location_id == move.location_final_id:
                    move_to_propagate_ids.add(m.id)
                elif not m.location_id._child_of(move.location_dest_id):
                    move_to_mts_ids.add(m.id)
            self.env['stock.move'].browse(move_to_mts_ids)._break_mto_link(move)
            move.move_dest_ids = [Command.unlink(m_id) for m_id in move_to_propagate_ids]
            new_move.move_dest_ids = [Command.link(m_id) for m_id in move_to_propagate_ids]

        new_moves = self.env['stock.move'].concat(*new_moves)
        new_moves = new_moves.sudo()._action_confirm()

        return new_moves
```

```python
# stock/models/stock_move.py:2234-2240
    def _skip_push(self):
        return self.is_inventory or (
            self.move_dest_ids and any(
                m.location_id._child_of(self.location_dest_id) or self.location_dest_id._child_of(m.location_id)
                for m in self.move_dest_ids
            )
        )
```

`_push_apply` looks for a push rule per move; it creates no push move when the rule would return the goods to the origin location of a returned move (L1245) and confirms the created moves with `sudo()._action_confirm()` (L1262). `_skip_push` (L2234-2240) skips inventory moves and moves whose destination move is already linked to a connected location. `_action_done` calls `_push_apply` only for moves for which `_skip_push()` is false (L2297-2299).

### 4.7 MTO chain overview

1. A move with `make_to_order` is confirmed: state waiting, procurement request with the move itself as `move_dest_ids` (L1703-1706, L1849-1850).
2. `stock.rule.run` selects a pull rule and `_run_pull` creates the supplying move with `move_dest_ids` pointing at the waiting move and `procure_method` taken from the rule (`stock/models/stock_rule.py:305-310`, `:366`).
3. The supplying move is confirmed and reserved normally; when it is done, `_action_done` calls `_action_assign` on its destination moves (L2300-2303).
4. The waiting move reserves only the quantity that the finished origin moves delivered (L2145-2178).
5. Cancelling either side follows the propagation rules in section 2.5.

---

## 5. Reservation

### 5.1 Entry points

| Entry point | Pointer |
|---|---|
| `_action_confirm`: moves that bypass reservation or must be assigned at confirmation | L1775-1777 |
| `_action_done`: destination moves of finished moves, grouped by company | L2300-2303 |
| `_trigger_assign`: moves waiting for stock after stock arrived | L2633-2654 |
| inventory apply: `_action_done` followed by `_trigger_assign` | `stock/models/stock_quant.py:1026-1030` |
| picking validation: `done_incoming_moves._trigger_assign()` | `stock/models/stock_picking.py:1284-1285` |
| manufacturing: finished production moves | `mrp/models/mrp_production.py:2241` |

`_trigger_assign` callers found by grep: `stock/models/stock_quant.py:1030`, `stock/models/stock_picking.py:1285`, `mrp/models/mrp_production.py:2241`. The picking-level "check availability" button is U226 scope and was not read.

### 5.2 Helper methods

```python
# stock/models/stock_move.py:1872-1915
    def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
        self.ensure_one()
        vals = {
            'move_id': self.id,
            'product_id': self.product_id.id,
            'product_uom_id': self.product_uom.id,
            'location_id': self.location_id.id,
            'location_dest_id': self.location_dest_id.id,
            'picking_id': self.picking_id.id,
            'company_id': self.company_id.id,
        }
        if quantity:
            # TODO could be also move in create/write
            rounding = self.env['decimal.precision'].precision_get('Product Unit')
            uom_quantity = self.product_id.uom_id._compute_quantity(quantity, self.product_uom, rounding_method='HALF-UP')
            uom_quantity = float_round(uom_quantity, precision_digits=rounding)
            uom_quantity_back_to_product_uom = self.product_uom._compute_quantity(uom_quantity, self.product_id.uom_id, rounding_method='HALF-UP')
            if float_compare(quantity, uom_quantity_back_to_product_uom, precision_digits=rounding) == 0:
                vals = dict(vals, quantity=uom_quantity)
            else:
                vals = dict(vals, quantity=quantity, product_uom_id=self.product_id.uom_id.id)
        package = None
        if reserved_quant:
            package = reserved_quant.package_id
            vals = dict(
                vals,
                location_id=reserved_quant.location_id.id,
                lot_id=reserved_quant.lot_id.id or False,
                package_id=package.id or False,
                owner_id =reserved_quant.owner_id.id or False,
            )
        return vals

    def _update_reserved_quantity(self, need, location_id, lot_id=None, package_id=None, owner_id=None, strict=True):
        """ Create or update move lines and reserves quantity from quants
            Expects the need (qty to reserve) and location_id to reserve from.
            `quant_ids` can be passed as an optimization since no search on the database
            is performed and reservation is done on the passed quants set
        """
        self.ensure_one()
        move_line_vals, taken_quantity = self._update_reserved_quantity_vals(need, location_id, lot_id, package_id, owner_id, strict)
        if move_line_vals:
            self.env['stock.move.line'].create(move_line_vals)
        return taken_quantity
```

```python
# stock/models/stock_move.py:1917-1965
    def _update_reserved_quantity_vals(self, need, location_id, lot_id=None, package_id=None, owner_id=None, strict=True):
        self.ensure_one()
        if not lot_id:
            lot_id = self.env['stock.lot']
        if not package_id:
            package_id = self.env['stock.package']
        if not owner_id:
            owner_id = self.env['res.partner']

        quants = self.env['stock.quant'].with_context(packaging_uom_id=self.packaging_uom_id)._get_reserve_quantity(
            self.product_id, location_id, need, uom_id=self.product_uom,
            lot_id=lot_id, package_id=package_id, owner_id=owner_id, strict=strict)

        taken_quantity = 0
        rounding = self.env['decimal.precision'].precision_get('Product Unit')
        # Find a candidate move line to update or create a new one.
        candidate_lines = {}
        for line in self.move_line_ids:
            if line.result_package_id or line.product_id.tracking == 'serial':
                continue
            candidate_lines[line.location_id, line.lot_id, line.package_id, line.owner_id] = line
        move_line_vals = []
        grouped_quants = {}
        # Handle quants duplication
        for quant, quantity in quants:
            if (quant.location_id, quant.lot_id, quant.package_id, quant.owner_id) not in grouped_quants:
                grouped_quants[quant.location_id, quant.lot_id, quant.package_id, quant.owner_id] = [quant, quantity]
            else:
                grouped_quants[quant.location_id, quant.lot_id, quant.package_id, quant.owner_id][1] += quantity
        for reserved_quant, quantity in grouped_quants.values():
            taken_quantity += quantity
            to_update = candidate_lines.get((reserved_quant.location_id, reserved_quant.lot_id, reserved_quant.package_id, reserved_quant.owner_id))
            if to_update:
                uom_quantity = self.product_id.uom_id._compute_quantity(quantity, to_update.product_uom_id, rounding_method='HALF-UP')
                uom_quantity = float_round(uom_quantity, precision_digits=rounding)
                uom_quantity_back_to_product_uom = to_update.product_uom_id._compute_quantity(uom_quantity, self.product_id.uom_id, rounding_method='HALF-UP')
            if to_update and float_compare(quantity, uom_quantity_back_to_product_uom, precision_digits=rounding) == 0:
                to_update.with_context(reserved_quant=reserved_quant).quantity += uom_quantity
            else:
                if self.product_id.tracking == 'serial' and (self.picking_type_id.use_create_lots or self.picking_type_id.use_existing_lots):
                    vals_list = self._add_serial_move_line_to_vals_list(reserved_quant, quantity)
                    if vals_list:
                        move_line_vals += vals_list
                else:
                    move_line_vals.append(self._prepare_move_line_vals(quantity=quantity, reserved_quant=reserved_quant))
        return move_line_vals, taken_quantity

    def _add_serial_move_line_to_vals_list(self, reserved_quant, quantity):
        return [self._prepare_move_line_vals(quantity=1, reserved_quant=reserved_quant) for i in range(int(quantity))]
```

```python
# stock/models/stock_move.py:1967-2048
    def _should_bypass_reservation(self, forced_location=False):
        self.ensure_one()
        location = forced_location or self.location_id
        return location.should_bypass_reservation() or not self.product_id.is_storable

    def _should_assign_at_confirm(self):
        return self._should_bypass_reservation() or self.picking_type_id.reservation_method == 'at_confirm' or (self.reservation_date and self.reservation_date <= fields.Date.today())

    def _get_picked_quantity(self):
        self.ensure_one()
        if self.picked and any(not ml.picked for ml in self.move_line_ids):
            picked_qty = 0
            for ml in self.move_line_ids:
                if not ml.picked:
                    continue
                picked_qty += ml.product_uom_id._compute_quantity(ml.quantity, self.product_uom, round=False)
            return picked_qty
        else:
            return self.quantity

    # necessary hook to be able to override move reservation to a restrict lot, owner, pack, location...
    def _get_available_quantity(self, location_id, lot_id=None, package_id=None, owner_id=None, strict=False, allow_negative=False):
        self.ensure_one()
        if location_id.should_bypass_reservation():
            return self.product_qty
        return self.env['stock.quant']._get_available_quantity(self.product_id, location_id, lot_id=lot_id, package_id=package_id, owner_id=owner_id, strict=strict, allow_negative=allow_negative)

    def _get_available_move_lines_in(self):
        move_lines_in = self.move_orig_ids.move_dest_ids.move_orig_ids.filtered(lambda m: m.state == 'done').mapped('move_line_ids')

        def _keys_in_groupby(ml):
            return (ml.location_dest_id, ml.lot_id, ml.result_package_id, ml.owner_id)

        grouped_move_lines_in = {}
        for k, g in groupby(move_lines_in, key=_keys_in_groupby):
            quantity = 0
            for ml in g:
                quantity += ml.product_uom_id._compute_quantity(ml.quantity, ml.product_id.uom_id)
            grouped_move_lines_in[k] = quantity

        return grouped_move_lines_in

    def _get_available_move_lines_out(self, assigned_moves_ids, partially_available_moves_ids):
        move_lines_out_done = (self.move_orig_ids.mapped('move_dest_ids') - self)\
            .filtered(lambda m: m.state in ['done'])\
            .mapped('move_line_ids')
        # As we defer the write on the stock.move's state at the end of the loop, there
        # could be moves to consider in what our siblings already took.
        StockMove = self.env['stock.move']
        moves_out_siblings = self.move_orig_ids.mapped('move_dest_ids') - self
        moves_out_siblings_to_consider = moves_out_siblings & (StockMove.browse(assigned_moves_ids) + StockMove.browse(partially_available_moves_ids))
        reserved_moves_out_siblings = moves_out_siblings.filtered(lambda m: m.state in ['partially_available', 'assigned'])
        move_lines_out_reserved = (reserved_moves_out_siblings | moves_out_siblings_to_consider).mapped('move_line_ids')

        def _keys_out_groupby(ml):
            return (ml.location_id, ml.lot_id, ml.package_id, ml.owner_id)

        grouped_move_lines_out = {}
        for k, g in groupby(move_lines_out_done, key=_keys_out_groupby):
            quantity = 0
            for ml in g:
                quantity += ml.product_uom_id._compute_quantity(ml.quantity, ml.product_id.uom_id)
            grouped_move_lines_out[k] = quantity
        for k, g in groupby(move_lines_out_reserved, key=_keys_out_groupby):
            grouped_move_lines_out[k] = sum(self.env['stock.move.line'].concat(*list(g)).mapped('quantity_product_uom'))

        return grouped_move_lines_out

    def _get_available_move_lines(self, assigned_moves_ids, partially_available_moves_ids):
        grouped_move_lines_in = self._get_available_move_lines_in()
        grouped_move_lines_out = self._get_available_move_lines_out(assigned_moves_ids, partially_available_moves_ids)
        available_move_lines = {key: grouped_move_lines_in[key] - grouped_move_lines_out.get(key, 0) for key in grouped_move_lines_in}
        rounding = self.product_id.uom_id.rounding
        # remove what this move already reserved
        for move_line in self.move_line_ids:
            if float_is_zero(move_line.quantity_product_uom, precision_rounding=rounding):
                continue
            key = (move_line.location_id, move_line.lot_id, move_line.package_id, move_line.owner_id)
            if key in available_move_lines:
                available_move_lines[key] -= move_line.quantity_product_uom
        # pop key if the quantity available amount to 0
        return dict((k, v) for k, v in available_move_lines.items() if float_compare(v, 0, precision_rounding=rounding) > 0)
```

Reading notes:

- `_prepare_move_line_vals` (L1872-1903) builds the move-line values, including the owner, lot and package of the reserved quant (L1901 reads `owner_id` from the reserved quant).
- `_update_reserved_quantity` (L1905-1915, default `strict=True`) delegates to `_update_reserved_quantity_vals` (L1917-1962), which asks `stock.quant._get_reserve_quantity` (U228, L1926-1928) and groups the result by `(location, lot, package, owner)` (L1941-1945). Existing lines without a result package and not serial-tracked are candidates keyed the same way (L1934-1937); a candidate is updated in place only when the quantity round-trips through its unit without loss (L1948-1954), otherwise new line values are returned (L1955-1961). Serial products create one line per unit (`_add_serial_move_line_to_vals_list`, L1956-1959, L1964-1965) only when the picking type creates or uses lots (L1956).
- `_should_bypass_reservation` (L1967-1970) is true when the source location bypasses reservation or the product is not storable; `_should_assign_at_confirm` (L1972-1973) is true when the move bypasses reservation, when the picking type reservation method is at_confirm, or when `reservation_date` is today or earlier.
- `_get_picked_quantity` (L1975-1985) and `_get_available_quantity` (L1988-1992; returns `product_qty` for a source location that bypasses reservation, otherwise asks the quant model) are helpers; a grep over `stock/models/stock_move.py` finds only their definitions (L1975, L1988) and no caller in that file (L502 calls the quant model's own method), so `_action_assign` does not use them.
- `_get_available_move_lines_in` (L1994-2007) collects the lines of done moves among the origin moves of the origin moves' destination moves, keyed `(location_dest_id, lot_id, result_package_id, owner_id)` (L1995-1998) with quantities in the product unit (L2004). `_get_available_move_lines_out` (L2009-2033) collects the lines of sibling destination moves that are done (L2010-2012) or that are partially available, assigned or already decided in the current run (L2015-2019), keyed `(location_id, lot_id, package_id, owner_id)` (L2021-2022); by code reading, L2030-2031 assign the reserved-lines total to the key rather than adding to an existing total. `_get_available_move_lines` (L2035-2048) returns in minus out per key (L2038), minus what the move itself already holds per key (L2041-2046), keeping only positive values (L2048).

### 5.3 `_action_assign` (L2050-2187)

```python
# stock/models/stock_move.py:2050-2187
    def _action_assign(self, force_qty=False):
        """ Reserve stock moves by creating their stock move lines. A stock move is
        considered reserved once the sum of `reserved_qty` for all its move lines is
        equal to its `product_qty`. If it is less, the stock move is considered
        partially available.
        """
        StockMove = self.env['stock.move']
        assigned_moves_ids = OrderedSet()
        partially_available_moves_ids = OrderedSet()
        # Read the `reserved_availability` field of the moves out of the loop to prevent unwanted
        # cache invalidation when actually reserving the move.
        reserved_availability = {move: move.quantity for move in self}

        roundings = {move: move.product_id.uom_id.rounding for move in self}
        move_line_vals_list = []
        # Once the quantities are assigned, we want to find a better destination location thanks
        # to the putaway rules. This redirection will be applied on moves of `moves_to_redirect`.
        moves_to_redirect = OrderedSet()
        moves_to_assign = self
        if not force_qty:
            moves_to_assign = moves_to_assign.filtered(
                lambda m: not m.picked and m.state in ['confirmed', 'waiting', 'partially_available']
            )
        moves_mto = moves_to_assign.filtered(lambda m: m.move_orig_ids and not m._should_bypass_reservation())
        quants_cache = self.env['stock.quant']._get_quants_by_products_locations(moves_mto.product_id, moves_mto.location_id)
        for move in moves_to_assign:
            move = move.with_company(move.company_id)
            rounding = roundings[move]
            if not force_qty:
                missing_reserved_uom_quantity = move.product_uom_qty - reserved_availability[move]
            else:
                missing_reserved_uom_quantity = force_qty
            if float_compare(missing_reserved_uom_quantity, 0, precision_rounding=rounding) <= 0:
                assigned_moves_ids.add(move.id)
                continue
            missing_reserved_quantity = move.product_uom._compute_quantity(missing_reserved_uom_quantity, move.product_id.uom_id, rounding_method='HALF-UP')
            if move._should_bypass_reservation():
                # create the move line(s) but do not impact quants
                if move.move_orig_ids:
                    available_move_lines = move._get_available_move_lines(assigned_moves_ids, partially_available_moves_ids)
                    for (location_id, lot_id, package_id, owner_id), quantity in available_move_lines.items():
                        qty_added = min(missing_reserved_quantity, quantity)
                        move_line_vals = move._prepare_move_line_vals(qty_added)
                        move_line_vals.update({
                            'location_id': location_id.id,
                            'lot_id': lot_id.id,
                            'lot_name': lot_id.name,
                            'owner_id': owner_id.id,
                            'package_id': package_id.id,
                        })
                        move_line_vals_list.append(move_line_vals)
                        missing_reserved_quantity -= qty_added
                        if move.product_id.uom_id.is_zero(missing_reserved_quantity):
                            break

                if missing_reserved_quantity and move.product_id.tracking == 'serial' and (move.picking_type_id.use_create_lots or move.picking_type_id.use_existing_lots):
                    for _i in range(int(missing_reserved_quantity)):
                        move_line_vals_list.append(move._prepare_move_line_vals(quantity=1))
                elif missing_reserved_quantity:
                    to_update = move.move_line_ids.filtered(lambda ml: ml.product_uom_id == move.product_uom and
                                                            ml.location_id == move.location_id and
                                                            ml.location_dest_id == move.location_dest_id and
                                                            ml.picking_id == move.picking_id and
                                                            not ml.picked and
                                                            not ml.lot_id and
                                                            not ml.result_package_id and
                                                            not ml.package_id and
                                                            not ml.owner_id)
                    if to_update:
                        to_update[0].quantity += move.product_id.uom_id._compute_quantity(
                            missing_reserved_quantity, move.product_uom, rounding_method='HALF-UP')
                    else:
                        move_line_vals_list.append(move._prepare_move_line_vals(quantity=missing_reserved_quantity))
                assigned_moves_ids.add(move.id)
                moves_to_redirect.add(move.id)
            else:
                if move.product_uom.is_zero(move.product_uom_qty) and not force_qty:
                    assigned_moves_ids.add(move.id)
                elif not move.move_orig_ids:
                    if move.procure_method == 'make_to_order':
                        continue
                    # If we don't need any quantity, consider the move assigned.
                    need = missing_reserved_quantity
                    if float_is_zero(need, precision_rounding=rounding):
                        assigned_moves_ids.add(move.id)
                        continue
                    # Reserve new quants and create move lines accordingly.
                    taken_quantity = move._update_reserved_quantity(need, move.location_id, strict=False)
                    if float_is_zero(taken_quantity, precision_rounding=rounding):
                        continue
                    moves_to_redirect.add(move.id)
                    if float_compare(need, taken_quantity, precision_rounding=rounding) == 0:
                        assigned_moves_ids.add(move.id)
                    else:
                        partially_available_moves_ids.add(move.id)
                else:
                    # Check what our parents brought and what our siblings took in order to
                    # determine what we can distribute.
                    # `quantity` is in `ml.product_uom_id` and, as we will later increase
                    # the reserved quantity on the quants, convert it here in
                    # `product_id.uom_id` (the UOM of the quants is the UOM of the product).
                    available_move_lines = move._get_available_move_lines(assigned_moves_ids, partially_available_moves_ids)
                    if not available_move_lines:
                        continue
                    taken_quantities = {}
                    all_move_line_vals = []
                    for (location_id, lot_id, package_id, owner_id), quantity in available_move_lines.items():
                        need = move.product_qty - sum(move.move_line_ids.mapped('quantity_product_uom')) - sum(taken_quantities.values())
                        move_line_vals, taken_quantity = move._update_reserved_quantity_vals(min(quantity, need), location_id, lot_id, package_id, owner_id, strict=True)
                        all_move_line_vals += move_line_vals
                        if move_line_vals:  # Only subtract for new lines (updates are already reflected in sum(move_line_ids))
                            taken_quantities[need, location_id, lot_id, package_id, owner_id] = taken_quantity
                    if all_move_line_vals:
                        self.env['stock.move.line'].create(all_move_line_vals)

                    for (need, location_id, lot_id, package_id, owner_id), taken_quantity in taken_quantities.items():
                        # `quantity` is what is brought by chained done move lines. We double check
                        # here this quantity is available on the quants themselves. If not, this
                        # could be the result of an inventory adjustment that removed totally of
                        # partially `quantity`. When this happens, we chose to reserve the maximum
                        # still available. This situation could not happen on MTS move, because in
                        # this case `quantity` is directly the quantity on the quants themselves.
                        if float_is_zero(taken_quantity, precision_rounding=rounding):
                            continue
                        moves_to_redirect.add(move.id)
                        if float_is_zero(need - taken_quantity, precision_rounding=rounding):
                            assigned_moves_ids.add(move.id)
                            break
                        partially_available_moves_ids.add(move.id)
            if move.product_id.tracking == 'serial':
                move.next_serial_count = move.product_uom_qty

        self.env['stock.move.line'].create(move_line_vals_list)
        StockMove.browse(partially_available_moves_ids).write({'state': 'partially_available'})
        StockMove.browse(assigned_moves_ids).write({'state': 'assigned'})
        if not self.env.context.get('bypass_entire_pack'):
            self.picking_id._check_entire_pack()
        StockMove.browse(moves_to_redirect).move_line_ids._apply_putaway_strategy()
```

Reading notes (pointers are lines of the excerpt):

- Candidates (L2068-2072): all moves of the recordset when `force_qty` is given, otherwise only moves that are not picked and are in confirmed, waiting or partially_available. For moves that have origin moves and do not bypass reservation, L2073-2074 read the quants of their products and source locations into `quants_cache` (helper at `stock/models/stock_quant.py:916-932`); a grep over `stock/models/stock_move.py` finds no later read of that variable.
- Missing quantity (L2078-2085): the loop takes the move quantity from the dictionary built before the loop (L2061, L2079), or takes `force_qty` (L2080-2081). A missing quantity at or below zero at the product-unit rounding makes the move assigned and skips it (L2082-2084). Otherwise the missing quantity is converted into the product unit with HALF-UP (L2085).
- Bypass branch (L2086-2124): with origin moves, `_get_available_move_lines` supplies the keys; serial-tracked products with create or existing lots get one line of one unit per missing unit; otherwise an unpicked, unlocked line without lot, package or owner is updated or a new line is created; the move becomes assigned and is queued for putaway.
- Non-bypass branch (L2125-2178): zero demand gives assigned (L2126-2127).
  - No origin moves (L2128-2144): make_to_order moves are skipped (L2129-2130); nothing needed gives assigned; otherwise `_update_reserved_quantity(need, location_id, strict=False)` (L2137); nothing taken leaves the move unchanged; need equal to taken gives assigned, otherwise partially_available.
  - With origin moves (L2145-2178): the comment at L2146-2147 states the intent (check what the parents brought); per `(location, lot, package, owner)` key the need is `product_qty` minus the line quantities in the product unit minus what was taken in this run (L2157); `_update_reserved_quantity_vals(min(quantity, need), ..., strict=True)` (L2158); lines are created in a batch (L2163); only keys that produced new line values are recorded in `taken_quantities`, whose dictionary key also carries the need value of that iteration (L2160-2161), because an in-place update of an existing line is already reflected in the line sum (comment L2160); the state loop (L2165-2178) reads only that dictionary: a zero result skips the key; need equal to taken gives assigned and ends the loop; otherwise partially_available.
- L2179-2180 apply `next_serial_count`; L2182-2184 create the lines and then write partially_available and assigned directly, without `_recompute_state`; L2185-2186 run `_check_entire_pack` unless the context contains `bypass_entire_pack`; L2187 applies the putaway strategy.
- L2059 holds a stale comment that mentions `reserved_availability`.

### 5.4 Strict and non-strict reservation, lots and packages

- Unchained moves reserve with `strict=False` at the move source location, so child locations and quants without lot or package qualify (L2137; semantics in U228).
- Chained moves reserve with `strict=True` against the exact key of the origin line (L2158), so a chained move never takes stock outside what its origin moves delivered.
- Lot, package and owner are part of the candidate key everywhere in the reservation code (L1937-1948, L2090, L2156-2165); the quant-side algorithm (removal strategy, locking) belongs to U228.

### 5.5 `reservation_date` and picking-type reservation method

```python
# stock/models/stock_move.py:730-739
    @api.depends('picking_type_id', 'date', 'priority', 'state')
    def _compute_reservation_date(self):
        for move in self:
            if move.picking_type_id.reservation_method == 'by_date' and move.state in ['draft', 'confirmed', 'waiting', 'partially_available']:
                days = move.picking_type_id.reservation_days_before
                if move.priority == '1':
                    days = move.picking_type_id.reservation_days_before_priority
                move.reservation_date = fields.Date.to_date(move.date) - timedelta(days=days)
            elif move.picking_type_id.reservation_method == 'manual':
                move.reservation_date = False
```

```python
# stock/models/stock_picking.py:68-73
    reservation_method = fields.Selection(
        [('at_confirm', 'At Confirmation'), ('manual', 'Manually'), ('by_date', 'Before scheduled date')],
        'Reservation Method', required=True, default='at_confirm',
        help="How products in transfers of this operation type should be reserved.")
    reservation_days_before = fields.Integer('Days', help="Maximum number of days before scheduled date that products should be reserved.")
    reservation_days_before_priority = fields.Integer('Days when starred', help="Maximum number of days before scheduled date that priority picking products should be reserved.")
```

`_compute_reservation_date` sets the date only for `by_date` picking types in the open states (date minus `reservation_days_before`, or `reservation_days_before_priority` for priority `'1'`) and clears it for `manual` (L733-739); `at_confirm` leaves the value untouched, and `_action_confirm` stamps it with today at L1734-1735. `_should_assign_at_confirm` (L1972-1973) and `_trigger_assign` (L2644-2649) read it.

### 5.6 `_trigger_scheduler` and `_trigger_assign`

```python
# stock/models/stock_move.py:2609-2654
    def _trigger_scheduler(self):
        """ Check for auto-triggered orderpoints and trigger them. """
        if not self or self.env['ir.config_parameter'].sudo().get_param('stock.no_auto_scheduler'):
            return

        orderpoints_by_company = defaultdict(lambda: self.env['stock.warehouse.orderpoint'])
        orderpoints_context_by_company = defaultdict(dict)
        for move in self:
            orderpoint = self.env['stock.warehouse.orderpoint'].search([
                ('product_id', '=', move.product_id.id),
                ('trigger', '=', 'auto'),
                ('location_id', 'parent_of', move.location_id.id),
                ('company_id', '=', move.company_id.id),
                '!', ('location_id', 'parent_of', move.location_dest_id.id),
            ], limit=1)
            if orderpoint:
                orderpoints_by_company[orderpoint.company_id] |= orderpoint
            if orderpoint and move.product_qty > orderpoint.product_min_qty and move.reference_ids:
                orderpoints_context_by_company[orderpoint.company_id].setdefault(orderpoint.id, set())
                orderpoints_context_by_company[orderpoint.company_id][orderpoint.id] |= set(move.reference_ids.ids)
        for company, orderpoints in orderpoints_by_company.items():
            orderpoints.with_context(origins=orderpoints_context_by_company[company])._procure_orderpoint_confirm(
                company_id=company, raise_user_error=False)

    def _trigger_assign(self):
        """ Check for and trigger action_assign for confirmed/partially_available moves related to done moves.
            Disable auto reservation if user configured to do so.
        """
        if not self or self.env['ir.config_parameter'].sudo().get_param('stock.picking_no_auto_reserve'):
            return

        product_domains = Domain.OR(
            [('product_id', 'in', moves.product_id.ids), ('location_id', 'parent_of', location_dest.id)]
            for location_dest, moves in self.grouped('location_dest_id').items()
        )
        static_domain = [('state', 'in', ['confirmed', 'partially_available']),
                         ('procure_method', '=', 'make_to_stock'),
                         '|',
                            ('reservation_date', '<=', fields.Date.today()),
                            ('picking_type_id.reservation_method', '=', 'at_confirm')
                        ]
        moves_to_reserve = self.env['stock.move'].search(
            Domain(static_domain) & product_domains,
            order='priority desc, date asc, id asc')
        moves_to_reserve = moves_to_reserve.sorted(key=lambda m: any(r in self.reference_ids.ids for r in m.reference_ids.ids), reverse=True)
        moves_to_reserve._action_assign()
```

Reading notes:

- `_trigger_assign` returns at once for an empty set or when the system parameter `stock.picking_no_auto_reserve` is set (L2637).
- Product domains use the arriving moves' destination locations with `parent_of` (L2640-2643); the static domain selects confirmed or partially_available moves with `procure_method` make_to_stock whose `reservation_date` is today or earlier or whose picking type reserves at confirmation (L2644-2649).
- Order is `'priority desc, date asc, id asc'` (L2650-2652); moves that share a reference with the arriving moves are sorted first (L2653); then `_action_assign` runs (L2654).

### 5.7 Unreserve

```python
# stock/models/stock_move.py:1023-1049
    def _do_unreserve(self):
        moves_to_unreserve = OrderedSet()
        for move in self:
            if move.state == 'cancel' or (move.state == 'done' and move.location_dest_usage == 'inventory') or move.picked:
                # We may have cancelled move in an open picking in a "propagate_cancel" scenario.
                # We may have done move in an open picking in a scrap scenario.
                continue
            elif move.state == 'done':
                raise UserError(_("You cannot unreserve a stock move that has been set to 'Done'."))
            moves_to_unreserve.add(move.id)
        moves_to_unreserve = self.env['stock.move'].browse(moves_to_unreserve)

        ml_to_unlink = OrderedSet()
        moves_not_to_recompute = OrderedSet()
        for ml in moves_to_unreserve.move_line_ids:
            if ml.picked:
                moves_not_to_recompute.add(ml.move_id.id)
                continue
            ml_to_unlink.add(ml.id)
        ml_to_unlink = self.env['stock.move.line'].browse(ml_to_unlink)
        moves_not_to_recompute = self.env['stock.move'].browse(moves_not_to_recompute)

        ml_to_unlink.unlink()
        # `write` on `stock.move.line` doesn't call `_recompute_state` (unlike to `unlink`),
        # so it must be called for each move where no move line has been deleted.
        (moves_to_unreserve - moves_not_to_recompute)._recompute_state()
        return True
```

`_do_unreserve` skips cancelled moves, done moves going to inventory, and picked moves; it raises a UserError for a done move ("You cannot unreserve a stock move that has been set to 'Done'.", L1030-1031).

### 5.8 Validation and inventory hand-off (other files)

```python
# stock/models/stock_picking.py:1275-1285
        todo_moves = self.move_ids.filtered(lambda self: self.state in ['draft', 'waiting', 'partially_available', 'assigned', 'confirmed'])
        for picking in self:
            if picking.owner_id:
                picking.move_ids.write({'restrict_partner_id': picking.owner_id.id})
                picking.move_line_ids.write({'owner_id': picking.owner_id.id})
        todo_moves._action_done(cancel_backorder=self.env.context.get('cancel_backorder'))
        self.write({'date_done': fields.Datetime.now(), 'priority': '0'})

        # if incoming/internal moves make other confirmed/partially_available moves available, assign them
        done_incoming_moves = self.filtered(lambda p: p.picking_type_id.code in ('incoming', 'internal')).move_ids.filtered(lambda m: m.state == 'done')
        done_incoming_moves._trigger_assign()
```

```python
# stock/models/stock_quant.py:1026-1030
        moves = self.env['stock.move'].with_context(inventory_mode=False).create(move_vals)
        moves.with_context(ignore_dest_packages=True)._action_done()
        if date:
            moves.date = date
        moves._trigger_assign()
```

### 5.9 Forecast-based reservation

No part of `_action_assign` or `_trigger_assign` reads `forecast_availability`, `forecast_expected_date` or `availability`. Reservation timing is controlled by `reservation_date` and the picking-type `reservation_method`; forecast fields are informational (section 3.4).

---

## 6. Done, backorder, split, merge

### 6.1 `_action_done` (L2249-2317; hook L2319-2320)

```python
# stock/models/stock_move.py:2249-2320
    def _action_done(self, cancel_backorder=False):
        moves = self.filtered(
            lambda move: move.state == 'draft')._action_confirm(merge=False)
        moves = (self | moves).exists().filtered(lambda x: x.state not in ('done', 'cancel'))

        # Cancel moves where necessary ; we should do it before creating the extra moves because
        # this operation could trigger a merge of moves.
        ml_ids_to_unlink = OrderedSet()
        for move in moves:
            if move.picked:
                # in theory, we should only have a mix of picked and non-picked mls in the barcode use case
                # where non-scanned mls = not picked => we definitely don't want to validate them
                ml_ids_to_unlink |= move.move_line_ids.filtered(lambda ml: not ml.picked).ids
            if (move.quantity <= 0 or not move.picked) and not move.is_inventory:
                if move.product_uom.compare(move.product_uom_qty, 0.0) == 0 or cancel_backorder:
                    move._action_cancel()
        self.env['stock.move.line'].browse(ml_ids_to_unlink).unlink()

        moves_todo = moves.filtered(lambda m:
            not (m.state == 'cancel' or (m.quantity <= 0 and not m.is_inventory) or not m.picked)
        )

        moves_todo._check_company()
        if not cancel_backorder:
            moves_todo._create_backorder()
        moves_todo.mapped('move_line_ids').sorted()._action_done()
        # Check the consistency of the result packages; there should be an unique location across
        # the contained quants.
        for result_package in moves_todo\
                .move_line_ids.filtered(lambda ml: ml.picked).mapped('result_package_id')\
                .filtered(lambda p: p.quant_ids and len(p.quant_ids) > 1):
            if len(result_package.quant_ids.filtered(lambda q: q.product_uom_id.compare(q.quantity, 0.0) > 0).mapped('location_id')) > 1:
                error_msg = _(
                    'You cannot move the same package content more than once in the same transfer'
                    ' or split the same package into two location.'
                )
                package_msg = _("\nPackage: %s", result_package.name)
                raise UserError(error_msg + package_msg)
        if any(ml.package_id and ml.package_id == ml.result_package_id for ml in moves_todo.move_line_ids):
            self.env['stock.quant']._unlink_zero_quants()
        picking = moves_todo.mapped('picking_id')
        moves_todo.write({'state': 'done', 'date': fields.Datetime.now()})

        move_dests_per_company = defaultdict(lambda: self.env['stock.move'])

        # Break move dest link if move dest and move_dest source are not the same,
        # so that when move_dests._action_assign is called, the move lines are not created with
        # the new location, they should not be created at all.
        moves_to_push = moves_todo.filtered(lambda m: not m._skip_push())
        if moves_to_push:
            moves_to_push._push_apply()
        for move_dest in moves_todo.move_dest_ids:
            move_dests_per_company[move_dest.company_id.id] |= move_dest
        for company_id, move_dests in move_dests_per_company.items():
            move_dests.sudo().with_company(company_id)._action_assign()

        # We don't want to create back order for scrap moves
        # Replace by a kwarg in master
        if self.env.context.get('is_scrap'):
            return moves

        if picking and not cancel_backorder:
            backorder = picking._create_backorder()
            if any([m.state == 'assigned' for m in backorder.move_ids]):
                backorder._check_entire_pack()
        if moves_todo:
            moves_todo._check_quantity()
            moves_todo._action_synch_order()
        return moves_todo

    def _action_synch_order(self):
        return True
```

Reading notes:

- Draft moves are confirmed first with `merge=False`; only moves that are not done or cancelled continue (L2250-2252).
- If a move is picked, its unpicked lines are queued for unlink (L2258-2261). A move that is not picked or has no positive quantity, and is not an inventory adjustment, is cancelled when its demand is zero or when `cancel_backorder` is set (L2262-2264).
- `moves_todo` excludes cancelled moves, moves with non-positive quantity that are not inventory adjustments, and moves that are not picked (L2267-2269).
- `_check_company` (L2271); `_create_backorder` unless `cancel_backorder` (L2272-2273); the move-line `_action_done` (L2274); package consistency check with an error (L2277-2286); zero quants unlinked (L2287-2288).
- `moves_todo.write({'state': 'done', 'date': fields.Datetime.now()})` (L2290) stamps state and date together.
- Push moves for moves that are not skipped (L2297-2299); destination moves are assigned per company (L2300-2303).
- With the context key `is_scrap` the method returns early (L2305-2308); otherwise the picking backorder is created, `_check_entire_pack` runs (L2310-2313), then `_check_quantity` and `_action_synch_order` (L2314-2316). `_action_synch_order` returns true in the base module (L2319-2320).
- `is_inventory` is read at L2262 and L2267-2269 and in `_skip_push` (L2234-2240); `scrap_id` (L139) links a scrap record, and the scrap flow itself belongs to another unit.

### 6.2 `_create_backorder`

```python
# stock/models/stock_move.py:2322-2351
    def _create_backorder(self):
        # Split moves where necessary and move quants
        backorder_moves_vals = []
        for move in self:
            # To know whether we need to create a backorder or not, round to the general product's
            # decimal precision and not the product's UOM.
            rounding = self.env['decimal.precision'].precision_get('Product Unit')
            if float_compare(move.quantity, move.product_uom_qty, precision_digits=rounding) < 0:
                # Need to do some kind of conversion here
                qty_split = move.product_uom._compute_quantity(move.product_uom_qty - move.quantity, move.product_id.uom_id, rounding_method='HALF-UP')
                new_move_vals = move._split(qty_split)
                backorder_moves_vals += new_move_vals
        backorder_moves = self.env['stock.move'].create(backorder_moves_vals)
        # The backorder moves are not yet in their own picking. We do not want to check entire packs for those
        # ones as it could messed up the result_package_id of the moves being currently validated
        backorder_moves.with_context(bypass_entire_pack=True)._action_confirm(merge=False, create_proc=False)
        return backorder_moves

    @api.ondelete(at_uninstall=False)
    def _unlink_if_draft_or_cancel(self):
        if any(move.state not in ('draft', 'cancel') and (move.move_orig_ids or move.move_dest_ids) for move in self):
            raise UserError(_('You can not delete moves linked to another operation'))

    def unlink(self):
        # With the non plannified picking, draft moves could have some move lines.
        self.with_context(prefetch_fields=False).mapped('move_line_ids').unlink()
        orderpoints = self._get_orderpoints_to_update()
        res = super().unlink()
        self.env.add_to_compute(self.env['stock.warehouse.orderpoint']._fields['qty_to_order_computed'], orderpoints)
        return res
```

`_create_backorder` (L2322-2338) compares `move.quantity` with `move.product_uom_qty` at the `Product Unit` decimal digits, not at the unit rounding (L2328-2329); for each short move it converts the missing quantity into the product unit with HALF-UP (L2331), calls `_split` (L2332), creates the new moves (L2334) and confirms them with `merge=False` and `create_proc=False` under `bypass_entire_pack` (L2337). `_unlink_if_draft_or_cancel` and `unlink` (L2340-2351) restrict deletion.

### 6.3 `_split`

```python
# stock/models/stock_move.py:2353-2417
    def _prepare_move_split_vals(self, qty):
        vals = {
            'product_uom_qty': qty,
            'procure_method': self.procure_method,
            'move_dest_ids': [(4, x.id) for x in self.move_dest_ids if x.state not in ('done', 'cancel')],
            'move_orig_ids': [(4, x.id) for x in self.move_orig_ids],
            'origin_returned_move_id': self.origin_returned_move_id.id,
            'price_unit': self.price_unit,
            'date_deadline': self.date_deadline,
        }
        if self.env.context.get('force_split_uom_id'):
            vals['product_uom'] = self.env.context['force_split_uom_id']
        return vals

    def _split(self, qty, restrict_partner_id=False):
        """ Splits `self` quantity and return values for a new moves to be created afterwards

        :param qty: float. quantity to split (given in product UoM)
        :param restrict_partner_id: optional partner that can be given in order to force the new move to restrict its choice of quants to the ones belonging to this partner.
        :returns: list of dict. stock move values """
        self.ensure_one()
        if self.state in ('done', 'cancel'):
            raise UserError(_('You cannot split a stock move that has been set to \'Done\' or \'Cancel\'.'))
        elif self.state == 'draft':
            # we restrict the split of a draft move because if not confirmed yet, it may be replaced by several other moves in
            # case of phantom bom (with mrp module). And we don't want to deal with this complexity by copying the product that will explode.
            raise UserError(_('You cannot split a draft move. It needs to be confirmed first.'))

        if self.product_id.uom_id.is_zero(qty):
            return []

        decimal_precision = self.env['decimal.precision'].precision_get('Product Unit')

        # `qty` passed as argument is the quantity to backorder and is always expressed in the
        # quants UOM. If we're able to convert back and forth this quantity in the move's and the
        # quants UOM, the backordered move can keep the UOM of the move. Else, we'll create is in
        # the UOM of the quants.
        uom_qty = self.product_id.uom_id._compute_quantity(qty, self.product_uom, rounding_method='HALF-UP')
        if float_compare(qty, self.product_uom._compute_quantity(uom_qty, self.product_id.uom_id, rounding_method='HALF-UP'), precision_digits=decimal_precision) == 0:
            defaults = self._prepare_move_split_vals(uom_qty)
        else:
            defaults = self.with_context(force_split_uom_id=self.product_id.uom_id.id)._prepare_move_split_vals(qty)

        if restrict_partner_id:
            defaults['restrict_partner_id'] = restrict_partner_id

        # TDE CLEANME: remove context key + add as parameter
        if self.env.context.get('source_location_id'):
            defaults['location_id'] = self.env.context['source_location_id']
        new_move_vals = self.copy_data(defaults)

        # Update the original `product_qty` of the move. Use the general product's decimal
        # precision and not the move's UOM to handle case where the `quantity_done` is not
        # compatible with the move's UOM.
        new_product_qty = self.product_id.uom_id._compute_quantity(max(0, self.product_qty - qty), self.product_uom, round=False)
        new_product_qty = float_round(new_product_qty, precision_digits=self.env['decimal.precision'].precision_get('Product Unit'))
        self.with_context(do_not_unreserve=True).write({'product_uom_qty': new_product_qty})
        self._recompute_state()
        return new_move_vals

    def _post_process_created_moves(self):
        # This method is meant to be overriden in order to execute post
        # creation actions that would be bypassed since the move was
        # and will probably never be confirmed
        pass
```

Reading notes:

- `_split` raises a UserError for done or cancelled moves and for draft moves; it returns an empty list for a zero quantity.
- A unit round trip (L2390-2394) decides which unit the new move uses; `force_split_uom_id` is set at L2394 and consumed in `_prepare_move_split_vals` (L2363-2364). `copy_data` (L2402) supplies all other copyable fields.
- `_prepare_move_split_vals` (L2353-2365) copies demand, `procure_method`, open destination moves, origin moves, `origin_returned_move_id`, `price_unit` and `date_deadline` to the new move.
- The original demand becomes `max(0, product_qty - qty)` converted back into the move unit and rounded to the `Product Unit` digits, written with `do_not_unreserve=True`, followed by `_recompute_state` on the original move.
- L2405 is a stale comment that mentions `quantity_done`.

### 6.4 Merge

```python
# stock/models/stock_move.py:1266-1301
    def _merge_moves_fields(self):
        """ This method will return a dict of stock move’s values that represent the values of all moves in `self` merged. """
        merge_extra = self.env.context.get('merge_extra')
        state = self._get_relevant_state_among_moves()
        origin = '/'.join(set(self.filtered(lambda m: m.origin).mapped('origin')))
        return {
            'product_uom_qty': sum(self.mapped('product_uom_qty')) if not merge_extra else self[0].product_uom_qty,
            'date': min(self.mapped('date')) if all(p.move_type == 'direct' for p in self.picking_id) else max(self.mapped('date')),
            'move_dest_ids': [(4, m.id) for m in self.mapped('move_dest_ids')],
            'move_orig_ids': [(4, m.id) for m in self.mapped('move_orig_ids')],
            'state': state,
            'origin': origin,
        }

    @api.model
    def _prepare_merge_moves_distinct_fields(self):
        fields = [
            'product_id', 'price_unit', 'procure_method', 'location_id', 'location_dest_id', 'location_final_id',
            'product_uom', 'restrict_partner_id', 'origin_returned_move_id',
            'propagate_cancel', 'description_picking', 'never_product_template_attribute_value_ids',
        ]
        if self.env['ir.config_parameter'].sudo().get_param('stock.merge_only_same_date'):
            fields.append('date')
        if self.env.context.get('merge_extra'):
            fields.pop(fields.index('procure_method'))
        if not self.env['ir.config_parameter'].sudo().get_param('stock.merge_ignore_date_deadline'):
            fields.append('date_deadline')
        return fields

    @api.model
    def _prepare_merge_negative_moves_excluded_distinct_fields(self):
        return ['description_picking']

    def _clean_merged(self):
        """Cleanup hook used when merging moves"""
        self.write({'propagate_cancel': False})
```

```python
# stock/models/stock_move.py:1307-1326
    def _merge_move_itemgetter(self, distinct_fields, excluded_fields=None):
        fields = set(distinct_fields or []) - set(excluded_fields or [])
        float_fields = {f_name for f_name in fields if self.env['stock.move']._fields[f_name].type == 'float'}
        base_getter = itemgetter(*fields - float_fields)

        if not float_fields:
            return base_getter

        float_precision = {f_name: (self.env['stock.move']._fields[f_name].get_digits(self.env) or (False, 2))[1] for f_name in float_fields}
        if 'price_unit' in float_fields:
            price_unit_prec = self.env['decimal.precision'].precision_get('Product Price')
            currency_precision = min(self.company_id.mapped('currency_id.decimal_places')) if self.company_id else False
            float_precision['price_unit'] = min(currency_precision, price_unit_prec) if currency_precision else price_unit_prec

        def _get_formatted_float_fields(move, f_name, precision):
            # Round and cast the value of move.f_name into a string so that rounding errors do not prevent the merge
            rounded_value = float_round(move[f_name], precision_digits=precision[f_name])
            return "{:.{precision}f}".format(rounded_value, precision=precision[f_name])

        return lambda move: base_getter(move) + tuple(_get_formatted_float_fields(move, f_name, float_precision) for f_name in float_fields)
```

```python
# stock/models/stock_move.py:1328-1409
    def _merge_moves(self, merge_into=False):
        """ This method will, for each move in `self`, go up in their linked picking and try to
        find in their existing moves a candidate into which we can merge the move.
        :return: Recordset of moves passed to this method. If some of the passed moves were merged
        into another existing one, return this one and not the (now unlinked) original.
        """

        candidate_moves_set = set()
        if not merge_into:
            self._update_candidate_moves_list(candidate_moves_set)
        else:
            candidate_moves_set.add(merge_into | self)

        distinct_fields = (self | self.env['stock.move'].concat(*candidate_moves_set))._prepare_merge_moves_distinct_fields()

        # Move removed after merge
        moves_to_unlink = self.env['stock.move']
        # Moves successfully merged
        merged_moves = self.env['stock.move']
        # Emptied moves
        moves_to_cancel = self.env['stock.move']

        moves_by_neg_key = defaultdict(lambda: self.env['stock.move'])
        # Need to check less fields for negative moves as some might not be set.
        neg_qty_moves = self.filtered(lambda m: m.product_uom.compare(m.product_qty, 0.0) < 0)
        # Detach their picking as they will either get absorbed or create a backorder, so no extra logs will be put in the chatter
        neg_qty_moves.picking_id = False
        excluded_fields = self._prepare_merge_negative_moves_excluded_distinct_fields()
        neg_key = self._merge_move_itemgetter(distinct_fields, excluded_fields)
        price_unit_prec = self.env['decimal.precision'].precision_get('Product Price')

        for candidate_moves in candidate_moves_set:
            # First step find move to merge.
            candidate_moves = candidate_moves.filtered(lambda m: m.state not in ('done', 'cancel', 'draft')) - neg_qty_moves
            for __, g in groupby(candidate_moves, key=self._merge_move_itemgetter(distinct_fields)):
                moves = self.env['stock.move'].concat(*g)
                # Merge all positive moves together
                if len(moves) > 1:
                    # link all move lines to record 0 (the one we will keep).
                    moves.mapped('move_line_ids').write({'move_id': moves[0].id})
                    # merge move data
                    merge_extra = self.env.context.get('merge_extra') and bool(merge_into)
                    moves[0].write(moves.with_context(merge_extra=merge_extra)._merge_moves_fields())
                    # update merged moves dicts
                    moves_to_unlink |= moves[1:]
                    merged_moves |= moves[0]
                # Add the now single positive move to its limited key record
                moves_by_neg_key[neg_key(moves[0])] |= moves[0]

        for neg_move in neg_qty_moves:
            # Check all the candidates that matches the same limited key, and adjust their quantities to absorb negative moves
            for pos_move in moves_by_neg_key.get(neg_key(neg_move), []):
                new_total_value = pos_move.product_qty * pos_move.price_unit + neg_move.product_qty * neg_move.price_unit
                # If quantity can be fully absorbed by a single move, update its quantity and remove the negative move
                if pos_move.product_uom.compare(pos_move.product_uom_qty, abs(neg_move.product_uom_qty)) >= 0:
                    pos_move.product_uom_qty += neg_move.product_uom_qty
                    pos_move.write({
                        'price_unit': float_round(new_total_value / pos_move.product_qty, precision_digits=price_unit_prec) if pos_move.product_qty else 0,
                        'move_dest_ids': [Command.link(m.id) for m in neg_move.mapped('move_dest_ids') if m.location_id == pos_move.location_dest_id],
                        'move_orig_ids': [Command.link(m.id) for m in neg_move.mapped('move_orig_ids') if m.location_dest_id == pos_move.location_id],
                    })
                    merged_moves |= pos_move
                    moves_to_unlink |= neg_move
                    if pos_move.product_uom.is_zero(pos_move.product_uom_qty):
                        moves_to_cancel |= pos_move
                    break
                neg_move.product_uom_qty += pos_move.product_uom_qty
                neg_move.price_unit = float_round(new_total_value / neg_move.product_qty, precision_digits=price_unit_prec)
                pos_move.product_uom_qty = 0
                moves_to_cancel |= pos_move

        # We are using propagate to False in order to not cancel destination moves merged in moves[0]
        (moves_to_unlink | moves_to_cancel)._clean_merged()

        if moves_to_unlink:
            moves_to_unlink._action_cancel()
            moves_to_unlink.sudo().unlink()

        if moves_to_cancel:
            moves_to_cancel.filtered(lambda m: not m.picked)._action_cancel()

        return (self | merged_moves) - moves_to_unlink
```

```python
# stock/models/stock_move.py:1411-1451
    def _get_relevant_state_among_moves(self):
        # We sort our moves by importance of state:
        #     ------------- 0
        #     | Assigned  |
        #     -------------
        #     |  Waiting  |
        #     -------------
        #     |  Partial  |
        #     -------------
        #     |  Confirm  |
        #     ------------- len-1
        sort_map = {
            'assigned': 4,
            'waiting': 3,
            'partially_available': 2,
            'confirmed': 1,
        }
        moves_todo = self\
            .filtered(lambda move: move.state not in ['cancel', 'done'] and not (move.state == 'assigned' and not move.product_uom_qty))\
            .sorted(key=lambda move: (sort_map.get(move.state, 0), move.product_uom_qty))
        if not moves_todo:
            return 'assigned'
        # The picking should be the same for all moves.
        if moves_todo[:1].picking_id and moves_todo[:1].picking_id.move_type == 'one':
            if all(not m.product_uom_qty for m in moves_todo):
                return 'assigned'
            most_important_move = moves_todo[0]
            if most_important_move.state == 'confirmed':
                return 'confirmed'
            elif most_important_move.state == 'partially_available':
                return 'confirmed'
            else:
                return moves_todo[:1].state or 'draft'
        elif moves_todo[:1].state != 'assigned' and any(move.state in ['assigned', 'partially_available'] for move in moves_todo):
            return 'partially_available'
        else:
            least_important_move = moves_todo[-1:]
            if least_important_move.state == 'confirmed' and least_important_move.product_uom_qty == 0:
                return 'assigned'
            else:
                return moves_todo[-1:].state or 'draft'
```

Reading notes:

- Distinct fields (L1281-1293): `product_id`, `price_unit`, `procure_method`, `location_id`, `location_dest_id`, `location_final_id` (L1283), `product_uom`, `restrict_partner_id` and `origin_returned_move_id` (L1284), `propagate_cancel`, `description_picking`, `never_product_template_attribute_value_ids` (L1285). The system parameter `stock.merge_only_same_date` adds `date` (L1287-1288); the context key `merge_extra` removes `procure_method` (L1289-1290); `date_deadline` is added unless `stock.merge_ignore_date_deadline` is set (L1291-1292).
- `_merge_move_itemgetter` (L1307-1326) builds the grouping key; float fields are formatted as rounded strings so that rounding noise does not prevent a merge, and `price_unit` is rounded to the smaller of the currency precision and the `Product Price` precision (L1315-1326).
- `_merge_moves` (L1328-1409): the candidates are the moves of every picking of the recordset, or `merge_into | self` when `merge_into` is given (L1336-1339); moves in state done, cancel or draft and negative-demand moves are not candidates (L1361); candidates with the same key are merged into the first one: lines are re-pointed to it (L1367), the merged values are written (L1370) and the others are queued for unlink (L1372).
- `_merge_moves_fields` (L1266-1278) sums `product_uom_qty` (or keeps the first move's value with `merge_extra`), takes the earliest `date` when every picking is `direct` and the latest otherwise (L1273), joins the chain links, takes the state from `_get_relevant_state_among_moves` and joins the distinct origins with a slash (L1270).
- `_get_relevant_state_among_moves` (L1411-1451) ranks open moves assigned 4, waiting 3, partially_available 2, confirmed 1 (L1422-1427) and sorts them ascending by rank and demand (L1430); cancelled, done and zero-demand assigned moves are ignored (L1429) and an empty remainder gives assigned (L1431-1432). For a picking with `move_type == 'one'` the first sorted move decides: confirmed and partially_available both give confirmed, any other state is returned as is (L1434-1443). Otherwise partially_available is returned when the first sorted move is not assigned but some move is assigned or partially_available (L1444-1445), else the state of the last sorted move, with assigned for a confirmed move of zero demand (L1446-1451). The diagram comment at L1412-1421 shows assigned first, the opposite of the ascending sort.
- Negative demand: moves of the recordset whose `product_qty` compares below zero (L1352) are detached from their picking (L1354). Their key omits the fields returned by `_prepare_merge_negative_moves_excluded_distinct_fields`, which is `description_picking` in the base (L1295-1297, L1355-1356). A negative move is absorbed by a positive move with the same reduced key (L1377-1397): when the positive demand is large enough, the positive demand is reduced, its `price_unit` recomputed, links carried over where locations match and the negative move queued for unlink (L1382-1393); otherwise the negative move absorbs the positive demand and the positive move is queued for cancel (L1394-1397).
- `_clean_merged` (L1299-1301) writes `propagate_cancel = False` on the moves that are unlinked or cancelled by the merge (L1399-1400); unlinked moves are cancelled and deleted (L1402-1404) and moves queued for cancel are cancelled unless picked (L1406-1407). The method returns the recordset plus the merged moves minus the unlinked ones (L1409).
- Extensions add keys: `purchase_stock/models/stock_move.py:22-26` (`purchase_line_id`, `created_purchase_line_ids`), `sale_stock/models/stock.py:89-93` (`sale_line_id`), `mrp/models/stock_move.py:564-570` (`created_production_id`, `cost_share`, `production_group_id`, and `bom_line_id` when the bill is of type phantom, L568-569). They also remove `created_purchase_line_ids` (`purchase_stock/models/stock_move.py:28-30`) and `created_production_id` (`mrp/models/stock_move.py:572-574`) from the negative-move key, and purchase_stock clears `created_purchase_line_ids` in `_clean_merged` (`purchase_stock/models/stock_move.py:112-114`).

---

## 7. v19 relation changes

### 7.1 `reference_ids` and the missing `group_id`

`reference_ids` (L141-142) is a Many2many to `stock.reference` over `stock_reference_move_rel`. The model `stock.reference` is defined in `stock/models/stock_reference.py`:

```python
# stock/models/stock_reference.py:1-15
from odoo import fields, models


class StockReference(models.Model):
    _name = 'stock.reference'
    _description = 'Reference between stock documents'

    name = fields.Char('Reference', required=True, readonly=True)
    move_ids = fields.Many2many(
        'stock.move', 'stock_reference_move_rel', 'reference_id', 'move_id', string="Stock Moves")
    picking_ids = fields.Many2many('stock.picking', compute='_compute_picking_ids', string="Transfers", readonly=True)

    def _compute_picking_ids(self):
        for reference in self:
            reference.picking_ids = reference.move_ids.picking_id
```

Grep for `group_id` over `stock/models/stock_move.py` returned no lines. A grep for `reference_ids` over the same file lists the declaration (L141), `_set_references` (L801-802, called from `create` at L835 and from `write` at L909-910), the picking-assignment key (L1529-1530) and search domain (L1536, L1546), the grouping key of `_action_confirm` (L1714), the procurement origin text (L1787), the procurement values (L1863), the orderpoint trigger in `_trigger_scheduler` (L2626-2628) and the ordering in `_trigger_assign` (L2653). `default_get` (L775-789) does not read the field.

```python
# stock/models/stock_move.py:799-802
    def _set_references(self):
        for move in self:
            if not move.reference_ids and move.picking_id:
                move.reference_ids = move.picking_id.reference_ids
```

```python
# stock/models/stock_move.py:1527-1583
    def _key_assign_picking(self):
        self.ensure_one()
        keys = (self.reference_ids, self.location_id, self.location_dest_id, self.picking_type_id)
        if self.move_orig_ids.picking_id and not self.reference_ids:
            keys += (self.move_orig_ids.picking_id, )
        return keys

    def _search_picking_for_assignation_domain(self):
        domain = [
            ('reference_ids', '=', self.reference_ids.ids),
            ('location_id', '=', self.location_id.id),
            ('location_dest_id', '=', (self.location_dest_id.id or self.picking_type_id.default_location_dest_id.id)),
            ('picking_type_id', '=', self.picking_type_id.id),
            ('printed', '=', False),
            ('state', 'in', ['draft', 'confirmed', 'waiting', 'partially_available', 'assigned'])]
        return domain

    def _search_picking_for_assignation(self):
        self.ensure_one()
        if not self.reference_ids:
            return self.env['stock.picking']
        domain = self._search_picking_for_assignation_domain()
        picking = self.env['stock.picking'].search(domain, limit=1)
        return picking

    def _assign_picking(self):
        """ Try to assign the moves to an existing picking that has not been
        reserved yet and has the same procurement group, locations and picking
        type (moves should already have them identical). Otherwise, create a new
        picking to assign them to. """
        Picking = self.env['stock.picking']
        grouped_moves = groupby(self, key=lambda m: m._key_assign_picking())
        for _group, moves in grouped_moves:
            moves = self.env['stock.move'].concat(*moves)
            new_picking = False
            # Could pass the arguments contained in group but they are the same
            # for each move that why moves[0] is acceptable
            picking = moves[0]._search_picking_for_assignation()
            if picking:
                # If a picking is found, we'll append `move` to its move list and thus its
                # `partner_id` and `ref` field will refer to multiple records. In this
                # case, we chose to wipe them.
                vals = moves._assign_picking_values(picking)
                if vals:
                    picking.write(vals)
            else:
                # Don't create picking for negative moves since they will be
                # reverse and assign to another picking
                moves = moves.filtered(lambda m: m.product_uom.compare(m.product_uom_qty, 0.0) >= 0)
                if not moves:
                    continue
                new_picking = True
                picking = Picking.create(moves._get_new_picking_values())

            moves.write({'picking_id': picking.id})
            moves._assign_picking_post_process(new=new_picking)
        return True
```

`_assign_picking` still describes the grouping in its docstring as based on the "procurement group" (L1553-1556); the code searches by `reference_ids`. mrp adds its own `production_group_id` (`mrp/models/stock_move.py:35-36`) and copies the production references in its `default_get` (`mrp/models/stock_move.py:26`).

### 7.2 `location_final_id` and `location_dest_id`

```python
# stock/models/stock_move.py:212-252
    @api.depends('picking_id.location_id')
    def _compute_location_id(self):
        for move in self:
            if move.picked:
                continue
            if not (location := move.location_id) or move.picking_id != move._origin.picking_id or move.picking_type_id != move._origin.picking_type_id:
                if move.picking_id:
                    location = move.picking_id.location_id
                elif move.picking_type_id:
                    location = move.picking_type_id.default_location_src_id
            move.location_id = location

    @api.depends('picking_id.location_dest_id')
    def _compute_location_dest_id(self):
        customer_loc, __ = self.env['stock.warehouse']._get_partner_locations()
        inter_comp_location = self.env.ref('stock.stock_location_inter_company', raise_if_not_found=False)
        for move in self:
            location_dest = False
            if move.picking_id:
                location_dest = move.picking_id.location_dest_id
            elif move.rule_id.location_dest_from_rule:
                location_dest = move.rule_id.location_dest_id
            elif move.picking_type_id:
                location_dest = move.picking_type_id.default_location_dest_id
            is_move_to_interco_transit = False
            if location_dest:
                is_move_to_interco_transit = location_dest._child_of(customer_loc) and move.location_final_id == inter_comp_location
            if location_dest and move.location_final_id and (move.location_final_id._child_of(location_dest) or is_move_to_interco_transit):
                # Force the location_final as dest in the following cases:
                # - The location_final is a sublocation of destination -> Means we reached the end
                # - The location dest is an out location (i.e. Customers) but the final dest is different (e.g. Inter-Company transfers)
                location_dest = move.location_final_id
            move.location_dest_id = location_dest

    def _set_location_dest_id(self):
        for ml in self.move_line_ids:
            parent_path = [int(loc_id) for loc_id in ml.location_dest_id.parent_path.split('/')[:-1]]
            if ml.move_id.location_dest_id.id in parent_path:
                continue
            loc_dest = ml.move_id.location_dest_id._get_putaway_strategy(ml.product_id, ml.quantity_product_uom)
            ml.location_dest_id = loc_dest
```

- `location_dest_id` is computed (L224-244): from the picking when present, otherwise from a rule that declares its own destination (`location_dest_from_rule`), otherwise from the picking type default; L238 computes `is_move_to_interco_transit`; L239 tests `location_final_id._child_of(location_dest)`; L243 sets the final location as destination when the test holds.
- The inverse `_set_location_dest_id` (L246-252) re-applies putaway on the move lines.
- `location_final_id` (L85-90) is stored and writable without a compute; procurement sets it from the final procurement destination (`stock/models/stock_rule.py:365`); it is a merge key (L1283), and it reaches split-off moves because `_split` calls `copy_data` (L2402) and the field declares no copy attribute (L85-90; the ORM default is copy enabled, `odoo/orm/fields.py:281`).

### 7.3 Owner restriction

`restrict_partner_id` (L163-165, label Owner) is the only owner field on the move: `owner_id` appears in this file only on move-line data and quant keys (grep lines L1626, L1628, L1901, L1905, L1912, L1917, L1923-1924, L1928, L1937, L1942-1945, L1948, L1988, L1992, L1998, L2022, L2044, L2090, L2097, L2117, L2156, L2158, L2161, L2165, L2519), never as a field of `stock.move`. The move is a merge key on it (L1284); `_split` takes it as an argument (L2367, L2396-2397); picking validation writes the owner from the picking onto moves and lines (`stock/models/stock_picking.py:1277-1279`).

### 7.4 Returns

`origin_returned_move_id` (L155-157) and `returned_move_ids` (L158) describe returns; there is no `return_line_ids` (grep). The origin link is a merge key (L1284), is copied by `_prepare_move_split_vals` (L2353-2365), and is consulted by `_push_apply` (L1245). The return wizard lives in other files (`stock_account/wizard/stock_picking_return.py:10,15` copies the `to_refund` choice onto the return move).

---

## 8. Constraints, guards and computed behaviour

### 8.1 Unit handling

```python
# stock/models/stock_move.py:202-210
    @api.depends('product_id', 'product_id.uom_id', 'product_id.uom_ids', 'product_id.seller_ids', 'product_id.seller_ids.product_uom_id')
    def _compute_allowed_uom_ids(self):
        for move in self:
            move.allowed_uom_ids = move.product_id.uom_id | move.product_id.uom_ids | move.sudo().product_id.seller_ids.product_uom_id

    @api.depends('product_id')
    def _compute_product_uom(self):
        for move in self:
            move.product_uom = move.product_id.uom_id.id
```

- `allowed_uom_ids` is the union of the product unit, the product packaging units (`uom_ids`, declared at `product/models/product_template.py:122`) and the units on the supplier price lists read with `sudo()` (L205). `mrp/models/stock_move.py:66-70` extends it with the bill-of-material units.
- `product_uom` is a stored compute with `readonly=False`; its domain is the allowed set (L67-70). No unit-category field and no unit-category constraint exists on the move (field inventory L24-200; no constraint declarations in the file).
- Rounding is checked in `_set_quantity` against the `Product Unit` precision (L468-476); `_create_backorder` and `_split` use the same decimal precision (L2328-2331).

### 8.2 Dates

```python
# stock/models/stock_move.py:391-402
    @api.depends('move_orig_ids.date', 'move_orig_ids.state', 'state', 'date')
    def _compute_delay_alert_date(self):
        for move in self:
            if move.state in ('done', 'cancel'):
                move.delay_alert_date = False
                continue
            prev_moves = move.move_orig_ids.filtered(lambda m: m.state not in ('done', 'cancel') and m.date)
            prev_max_date = max(prev_moves.mapped("date"), default=False)
            if prev_max_date and prev_max_date > move.date:
                move.delay_alert_date = prev_max_date
            else:
                move.delay_alert_date = False
```

```python
# stock/models/stock_move.py:583-602
    def _set_date_deadline(self, new_deadline):
        # Handle the propagation of `date_deadline` fields (up and down stream - only update by up/downstream documents)
        already_propagate_ids = self.env.context.get('date_deadline_propagate_ids', set())
        already_propagate_ids.update(self.ids)
        self = self.with_context(date_deadline_propagate_ids=already_propagate_ids)
        for move in self:
            moves_to_update = (move.move_dest_ids | move.move_orig_ids)
            if move.date_deadline:
                delta = move.date_deadline - fields.Datetime.to_datetime(new_deadline)
            else:
                delta = 0
            for move_update in moves_to_update:
                if move_update.state in ('done', 'cancel'):
                    continue
                if move_update.id in already_propagate_ids:
                    continue
                if move_update.date_deadline and delta:
                    move_update.date_deadline -= delta
                elif not move_update.date_deadline or move_update.date_deadline != new_deadline:
                    move_update.date_deadline = new_deadline
```

- `date` is the scheduled date until done and the actual processing date afterwards (help text L30); `_action_done` rewrites it with the current time (L2290).
- `delay_alert_date` is stored; it is false for done or cancelled moves and otherwise the latest date among the open origin moves when that date is later than the move date (L391-402).
- `date_deadline` has no compute; `write` calls `_set_date_deadline` when it changes (L873-874; method L583-602). After the standard write, a `date` value is propagated to the move lines of the done moves in the set (L883-884). Merging adds it to the keys unless `stock.merge_ignore_date_deadline` is set (L1280-1293).

### 8.3 `description_picking`

```python
# stock/models/stock_move.py:804-813
    @api.depends('product_id', 'picking_type_id', 'description_picking_manual')
    def _compute_description_picking(self):
        for move in self:
            if move.description_picking_manual:
                move.description_picking = move.description_picking_manual
            elif move.product_id:
                product = move.product_id.with_context(lang=move._get_lang())
                move.description_picking = product._get_picking_description(move.picking_type_id) or move._get_description()
            else:
                move.description_picking = ""
```

### 8.4 `create` and `write` guards

```python
# stock/models/stock_move.py:823-911
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if (vals.get('quantity') or vals.get('move_line_ids')) and 'lot_ids' in vals:
                vals.pop('lot_ids')
            picking_id = self.env['stock.picking'].browse(vals.get('picking_id'))
            if picking_id.state == 'done' and vals.get('state') != 'done':
                vals['state'] = 'done'
            if vals.get('state') == 'done':
                vals['picked'] = True
        res = super().create(vals_list)
        res._update_orderpoints()
        res._set_references()
        return res

    def write(self, vals):
        # Handle the write on the initial demand by updating the reserved quantity and logging
        # messages according to the state of the stock.move records.
        receipt_moves_to_reassign = self.env['stock.move']
        move_to_recompute_state = self.env['stock.move']
        move_to_check_location = self.env['stock.move']
        if 'quantity' in vals:
            if any(move.state == 'cancel' for move in self):
                raise UserError(_('You cannot change a cancelled stock move, create a new line instead.'))
            # TODO The order of the calls is based on the orders of the keys in vals, which is the order of changes made
            # in the UI. This should be refactored to avoid relying on the order of the keys in vals.
            if 'lot_ids' in vals:
                # If lot_ids is changed after changing the quantity, we need to ensure that the lot_ids changed is process before
                # processing the quantity change, to avoid unexpected lot_ids that will be re-added later in the process.
                vals = dict(sorted(vals.items()))
        if 'product_uom' in vals and any(move.state == 'done' for move in self) and not self.env.context.get('skip_uom_conversion'):
            raise UserError(_('You cannot change the UoM for a stock move that has been set to \'Done\'.'))
        if 'product_uom_qty' in vals:
            for move in self.filtered(lambda m: m.state not in ('done', 'draft') and m.picking_id):
                if move.product_uom.compare(vals['product_uom_qty'], move.product_uom_qty):
                    self.env['stock.move.line']._log_message(move.picking_id, move, 'stock.track_move_template', vals)
            if self.env.context.get('do_not_unreserve') is None:
                move_to_unreserve = self.filtered(
                    lambda m: m.state not in ['draft', 'done', 'cancel'] and m.product_uom.compare(m.quantity, vals.get('product_uom_qty')) == 1
                )
                move_to_unreserve._do_unreserve()
                (self - move_to_unreserve).filtered(lambda m: m.state == 'assigned').write({'state': 'partially_available'})
                # When editing the initial demand, directly run again action assign on receipt moves.
                receipt_moves_to_reassign |= move_to_unreserve.filtered(lambda m: m.location_id.usage == 'supplier')
                receipt_moves_to_reassign |= (self - move_to_unreserve).filtered(
                    lambda m:
                        m.location_id.usage == 'supplier' and
                        m.state in ('partially_available', 'assigned')
                )
                move_to_recompute_state |= self - move_to_unreserve - receipt_moves_to_reassign
        if 'date_deadline' in vals:
            self._set_date_deadline(vals.get('date_deadline'))
        if 'move_orig_ids' in vals:
            move_to_recompute_state |= self.filtered(lambda m: m.state not in ['draft', 'cancel', 'done'])
        if 'location_id' in vals:
            move_to_check_location = self.filtered(lambda m: m.location_id.id != vals.get('location_id'))
        if 'product_id' in vals or 'location_id' in vals or 'location_dest_id' in vals:
            self._update_orderpoints()
        res = super().write(vals)
        moves_done = self.filtered(lambda m: m.state == 'done')
        if 'date' in vals and moves_done:
            moves_done.move_line_ids.date = vals['date']
        if move_to_recompute_state:
            move_to_recompute_state._recompute_state()
        if move_to_check_location:
            for ml in move_to_check_location.move_line_ids:
                parent_path = [int(loc_id) for loc_id in ml.location_id.parent_path.split('/')[:-1]]
                if move_to_check_location.location_id.id not in parent_path:
                    receipt_moves_to_reassign |= move_to_check_location
                    move_to_check_location.procure_method = 'make_to_stock'
                    move_to_check_location.move_orig_ids = [Command.clear()]
                    ml.unlink()
        if 'location_id' in vals or 'location_dest_id' in vals:
            wh_by_moves = defaultdict(self.env['stock.move'].browse)
            for move in self:
                move_warehouse = move.location_id.warehouse_id or move.location_dest_id.warehouse_id
                if move_warehouse == move.warehouse_id:
                    continue
                wh_by_moves[move_warehouse] |= move
            for warehouse, moves in wh_by_moves.items():
                moves.warehouse_id = warehouse.id
        if receipt_moves_to_reassign:
            receipt_moves_to_reassign._action_assign()
        if ('product_id' in vals or 'state' in vals or 'date' in vals or 'product_uom_qty' in vals or
                'location_id' in vals or 'location_dest_id' in vals):
            self._update_orderpoints()
        if 'picking_id' in vals:
            self._set_references()
        return res
```

Reading notes:

- `create` (L823-836) drops `lot_ids` from the values when `quantity` or `move_line_ids` is given (L826-827), forces state done when the target picking is done (L829-830), sets `picked` for done values (L831-832), then updates orderpoints and calls `_set_references` (L834-835).
- Writing `quantity` on a cancelled move raises an error (L844-846); changing `product_uom` on a done move raises unless the context contains `skip_uom_conversion` (L853-854).
- A change of `product_uom_qty` logs the change, unreserves when the move quantity exceeds the new demand unless `do_not_unreserve` is set, turns an assigned move into partially_available, and re-assigns supplier receipts (L855-872).
- A change of `date_deadline` calls `_set_date_deadline`; a change of `move_orig_ids` recomputes the state; a change of `location_id` unlinks move lines outside the new location, sets make_to_stock and clears the links (L877-894); the warehouse is synchronised (L895-903); orderpoints are updated; a change of `picking_id` calls `_set_references` (L909-910).

---

## 9. Extension fields (brief)

| Module | Field | Target | Cascade behaviour | Pointer |
|---|---|---|---|---|
| sale_stock | sale_line_id | sale.order.line | Many2one with `index='btree_not_null'`; no `ondelete` or `copy` attribute declared (ORM defaults apply: set null for an optional Many2one, `odoo/orm/fields_relational.py:274-282`; copy enabled, `odoo/orm/fields.py:281`) | `sale_stock/models/stock.py:17` |
| purchase_stock | purchase_line_id | purchase.order.line | `ondelete='set null'`, `index='btree_not_null'`, `readonly=True`; no `copy` attribute | `purchase_stock/models/stock_move.py:15-17` |
| purchase_stock | created_purchase_line_ids | purchase.order.line | Many2many over `stock_move_created_purchase_line_rel`, `copy=False` | `purchase_stock/models/stock_move.py:18-20` |
| mrp | created_production_id | mrp.production | `check_company`, `index=True`; no `ondelete` attribute | `mrp/models/stock_move.py:30` |
| mrp | production_id | mrp.production | `ondelete="cascade"` | `mrp/models/stock_move.py:31-32` |
| mrp | raw_material_production_id | mrp.production | `ondelete="cascade"` | `mrp/models/stock_move.py:33-34` |
| mrp | production_group_id | mrp.production.group | no `ondelete` attribute | `mrp/models/stock_move.py:35-36` |
| mrp | unbuild_id, consume_unbuild_id | mrp.unbuild | `check_company`, `index='btree_not_null'`; no `ondelete` attribute | `mrp/models/stock_move.py:37-40` |
| mrp | allowed_operation_ids, operation_id, workorder_id | mrp.routing.workcenter, mrp.workorder | `workorder_id` is `copy=False`; no `ondelete` attribute on the three | `mrp/models/stock_move.py:41-47` |
| mrp | bom_line_id, byproduct_id | mrp.bom.line, mrp.bom.byproduct | `check_company`; no `ondelete` attribute | `mrp/models/stock_move.py:49-52` |
| mrp | unit_factor, order_finished_lot_ids, should_consume_qty, cost_share, product_qty_available, product_virtual_available, manual_consumption | float, related and computed fields | not relations to cascade | `mrp/models/stock_move.py:53-64` |
| stock_account | to_refund | boolean | `copy=True`, `default=True` | `stock_account/models/stock_move.py:20-22` |
| stock_account | company_currency_id, value, value_justification, value_computed_justification, value_manual, standard_price | related, monetary, text and float fields | valuation content belongs to U232 | `stock_account/models/stock_move.py:23-35` |
| stock_account | price_unit (redeclared), is_in, is_out, is_dropship, is_valued, remaining_qty, remaining_value, analytic_account_line_ids, account_move_id | float, boolean and relation fields | the comment above the redeclaration (L37) reads "To remove and only use value"; valuation content belongs to U232 | `stock_account/models/stock_move.py:38-51` |

```python
# mrp/models/stock_move.py:12-64
    @api.model
    def default_get(self, fields):
        defaults = super().default_get(fields)
        if self.env.context.get('default_raw_material_production_id') or self.env.context.get('default_production_id'):
            production_id = self.env['mrp.production'].browse(self.env.context.get('default_raw_material_production_id') or self.env.context.get('default_production_id'))

            if production_id.state not in ('draft', 'cancel'):
                if production_id.state != 'done':
                    defaults['state'] = 'draft'
                else:
                    defaults['state'] = 'done'
                    defaults['additional'] = True
                defaults['product_uom_qty'] = 0.0
            elif production_id.state == 'draft':
                defaults['reference_ids'] = production_id.reference_ids.ids
                defaults['reference'] = production_id.name
        return defaults

    created_production_id = fields.Many2one('mrp.production', 'Created Production Order', check_company=True, index=True)
    production_id = fields.Many2one(
        'mrp.production', 'Production Order for finished products', check_company=True, index='btree_not_null', ondelete="cascade")
    raw_material_production_id = fields.Many2one(
        'mrp.production', 'Production Order for components', check_company=True, index='btree_not_null', ondelete="cascade")
    production_group_id = fields.Many2one(
        'mrp.production.group', 'Used for Productions')
    unbuild_id = fields.Many2one(
        'mrp.unbuild', 'Disassembly Order', check_company=True, index='btree_not_null')
    consume_unbuild_id = fields.Many2one(
        'mrp.unbuild', 'Consumed Disassembly Order', check_company=True, index='btree_not_null')
    allowed_operation_ids = fields.One2many(
        'mrp.routing.workcenter', related='raw_material_production_id.bom_id.operation_ids')
    operation_id = fields.Many2one(
        'mrp.routing.workcenter', 'Operation To Consume', check_company=True,
        domain="[('id', 'in', allowed_operation_ids)]")
    workorder_id = fields.Many2one(
        'mrp.workorder', 'Work Order To Consume', copy=False, check_company=True, index='btree_not_null')
    # Quantities to process, in normalized UoMs
    bom_line_id = fields.Many2one('mrp.bom.line', 'BoM Line', check_company=True)
    byproduct_id = fields.Many2one(
        'mrp.bom.byproduct', 'By-products', check_company=True,
        help="By-product line that generated the move in a manufacturing order")
    unit_factor = fields.Float('Unit Factor', compute='_compute_unit_factor', store=True)
    order_finished_lot_ids = fields.Many2many('stock.lot', string="Finished Lot/Serial Number", related="raw_material_production_id.lot_producing_ids")
    should_consume_qty = fields.Float('Quantity To Consume', compute='_compute_should_consume_qty', digits='Product Unit')
    cost_share = fields.Float(
        "Cost Share (%)", digits=0,
        help="The percentage of the final production cost for this by-product. The total of all by-products' cost share must be smaller or equal to 100.")
    product_qty_available = fields.Float('Product On Hand Quantity', related='product_id.qty_available', depends=['product_id'])
    product_virtual_available = fields.Float('Product Forecasted Quantity', related='product_id.virtual_available', depends=['product_id'])
    manual_consumption = fields.Boolean(
        'Manual Consumption', compute='_compute_manual_consumption', store=True, readonly=False,
        help="When activated, then the registration of consumption for that component is recorded manually exclusively.\n"
             "If not activated, and any of the components consumption is edited manually on the manufacturing order, Odoo assumes manual consumption also.")
```

```python
# mrp/models/stock_move.py:542-574
    def _should_be_assigned(self):
        res = super(StockMove, self)._should_be_assigned()
        return bool(res and not (self.production_id or self.raw_material_production_id))

    def _should_bypass_set_qty_producing(self):
        if self.state in ('done', 'cancel'):
            return True
        # Do not update extra product quantities
        return self.product_uom.is_zero(self.product_uom_qty)

    def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
        vals = super()._prepare_move_line_vals(quantity, reserved_quant)
        if self.raw_material_production_id:
            vals['production_id'] = self.raw_material_production_id.id
        if self.production_id.product_tracking == 'lot' and self.product_id == self.production_id.product_id and self.production_id.lot_producing_ids:
            vals['lot_id'] = self.production_id.lot_producing_ids.ids[0]
        return vals

    def _key_assign_picking(self):
        keys = super(StockMove, self)._key_assign_picking()
        return keys + (self.created_production_id, self.production_group_id)

    @api.model
    def _prepare_merge_moves_distinct_fields(self):
        res = super()._prepare_merge_moves_distinct_fields()
        res += ['created_production_id', 'cost_share', 'production_group_id']
        if self.bom_line_id and ("phantom" in self.bom_line_id.bom_id.mapped('type')):
            res.append('bom_line_id')
        return res

    @api.model
    def _prepare_merge_negative_moves_excluded_distinct_fields(self):
        return super()._prepare_merge_negative_moves_excluded_distinct_fields() + ['created_production_id']
```

```python
# sale_stock/models/stock.py:15-17
class StockMove(models.Model):
    _inherit = "stock.move"
    sale_line_id = fields.Many2one('sale.order.line', 'Sale Line', index='btree_not_null')
```

```python
# sale_stock/models/stock.py:89-93
    @api.model
    def _prepare_merge_moves_distinct_fields(self):
        distinct_fields = super()._prepare_merge_moves_distinct_fields()
        distinct_fields.append('sale_line_id')
        return distinct_fields
```

```python
# sale_stock/models/stock.py:178-181
    def _get_custom_move_fields(self):
        fields = super(StockRule, self)._get_custom_move_fields()
        fields += ['sale_line_id', 'partner_id', 'sequence', 'to_refund']
        return fields
```

```python
# purchase_stock/models/stock_move.py:15-30
    purchase_line_id = fields.Many2one(
        'purchase.order.line', 'Purchase Order Line',
        ondelete='set null', index='btree_not_null', readonly=True)
    created_purchase_line_ids = fields.Many2many(
        'purchase.order.line', 'stock_move_created_purchase_line_rel',
        'move_id', 'created_purchase_line_id', 'Created Purchase Order Lines', copy=False)

    @api.model
    def _prepare_merge_moves_distinct_fields(self):
        distinct_fields = super(StockMove, self)._prepare_merge_moves_distinct_fields()
        distinct_fields += ['purchase_line_id', 'created_purchase_line_ids']
        return distinct_fields

    @api.model
    def _prepare_merge_negative_moves_excluded_distinct_fields(self):
        return super()._prepare_merge_negative_moves_excluded_distinct_fields() + ['created_purchase_line_ids']
```

```python
# purchase_stock/models/stock_move.py:99-114
    def _prepare_extra_move_vals(self, qty):
        vals = super()._prepare_extra_move_vals(qty)
        vals['purchase_line_id'] = self.purchase_line_id.id
        return vals

    def _prepare_move_split_vals(self, uom_qty):
        vals = super(StockMove, self)._prepare_move_split_vals(uom_qty)
        # when backordering an mto move link the bakcorder to the purchase order
        if self.procure_method == 'make_to_order' and self.created_purchase_line_ids:
            vals['created_purchase_line_ids'] = [Command.set(self.created_purchase_line_ids.ids)]
        vals['purchase_line_id'] = self.purchase_line_id.id
        return vals

    def _clean_merged(self):
        super(StockMove, self)._clean_merged()
        self.write({'created_purchase_line_ids': [Command.clear()]})
```

```python
# stock_account/models/stock_move.py:17-42
class StockMove(models.Model):
    _inherit = "stock.move"

    to_refund = fields.Boolean(
        "Update quantities on SO/PO", copy=True, default=True,
        help='Trigger a decrease of the delivered/received quantity in the associated Sale Order/Purchase Order')
    company_currency_id = fields.Many2one('res.currency', related='company_id.currency_id', string='Company Currency', readonly=True)
    value = fields.Monetary(
        "Value", currency_field='company_currency_id', copy=False,
        help="The current value of the move. It's zero if the move is not valued.")
    value_justification = fields.Text(
        "Value Description", compute="_compute_value_justification")
    value_computed_justification = fields.Text(
        "Computed Value Description", compute="_compute_value_justification")
    # Useful for testing and custom valuation
    value_manual = fields.Monetary(
        "Manual Value", currency_field='company_currency_id',
        compute="_compute_value_manual", inverse="_inverse_value_manual")
    standard_price = fields.Float(compute='_compute_standard_price', string='Standard Price')

    # To remove and only use value
    price_unit = fields.Float("Price Unit")
    is_in = fields.Boolean(string='Is Incoming (valued)', compute='_compute_is_in', store=True)
    is_out = fields.Boolean(string='Is Outgoing (valued)', compute='_compute_is_out', store=True)
    is_dropship = fields.Boolean(string='Is Dropship', compute='_compute_is_dropship', store=True)
    is_valued = fields.Boolean(string='Is Valued', compute='_compute_is_valued')
```

Files under the addons directory that extend `stock.move`, found with four literal grep patterns (`_inherit = 'stock.move'` and `_inherit = "stock.move"` matched; the two list-form patterns matched nothing), 32 files: `stock_delivery/models/stock_move.py`, `sale_project_stock_account/models/stock_move.py`, `purchase_requisition_stock/models/stock.py`, `mrp_subcontracting/models/stock_move.py`, `project_mrp/models/stock.py`, `mrp/models/stock_move.py`, `sale_project_stock/models/stock_move.py`, `project_mrp_account/models/stock_move.py`, `pos_mrp/models/stock_move.py`, `pos_mrp/models/stock_picking.py`, `mrp_subcontracting_purchase/models/stock_move.py`, `project_stock_account/models/stock_move.py`, `purchase_stock/models/stock_move.py`, `mrp_repair/models/stock_move.py`, `mrp_repair/models/repair.py`, `point_of_sale/models/stock_picking.py`, `sale_mrp/models/stock_move.py`, `mrp_subcontracting_account/models/stock_move.py`, `purchase_mrp/models/stock_move.py`, `repair/models/stock_move.py`, `sale_purchase_stock/models/stock_move.py`, `stock_picking_batch/models/stock_move.py`, `l10n_in_purchase_stock/models/stock_move.py`, `l10n_in_sale_stock/models/stock_move.py`, `sale_stock/models/stock.py`, `l10n_in_ewaybill_stock/models/stock_move.py`, `mrp_account/models/stock_move.py`, `l10n_in_stock/models/stock_move.py`, `mrp_subcontracting_dropshipping/models/stock_move.py`, `product_expiry/models/stock_move.py`, `stock_account/models/stock_move.py`, `stock_landed_costs/models/stock_move.py`. Fields of the 28 files other than the mrp, sale_stock, purchase_stock and stock_account ones were not inventoried.

---

## 10. MIGRATION FLAGS

Baseline column: statements about earlier versions are baseline knowledge and are not verifiable in this source tree.

| ID | Severity | v19 state (source-verified) | Baseline (not verifiable here) |
|---|---|---|---|
| M-01 | HIGH | `group_id` does not exist on `stock.move` (grep, no lines); `reference_ids` Many2many `stock.reference` (L141-142; `stock/models/stock_reference.py:4-15`) | earlier versions linked a move to one procurement group |
| M-02 | HIGH | one `quantity` field (L171-172, L411-441); no `quantity_done`, no `reserved_availability` field; stale comments L2059, L2405 | earlier versions exposed separate done and reserved quantity fields on the move |
| M-03 | MEDIUM | `picked` is a stored compute with inverse (L121-124); `_action_done` processes only picked moves (L2267-2269) | the done decision rested on the done quantity |
| M-04 | MEDIUM | `location_final_id` stored and writable (L85-90); `location_dest_id` computed and replaced by the final location when it contains it (L224-244); procurement writes the final location (`stock/models/stock_rule.py:365`); both are merge keys (L1280-1293) | one destination location on the move |
| M-05 | MEDIUM | `to_refund` declared in stock_account (`stock_account/models/stock_move.py:20-22`); written unguarded in `stock/models/stock_rule.py:355-356`; carried by sale_stock `_get_custom_move_fields` (`sale_stock/models/stock.py:178-181`) | declaration module of the flag in earlier versions should be confirmed against the baseline source |
| M-06 | MEDIUM | `mts_else_mto` exists only on the rule; the move stores make_to_stock or make_to_order (`stock/models/stock_rule.py:305-310`; L1707-1710; L2604-2607) | not asserted |
| M-07 | MEDIUM | `allowed_uom_ids` drives the unit domain (L66-70, L202-205); no unit-category field or constraint on the move | not asserted |
| M-08 | LOW | `_prepare_extra_move_vals` is overridden by purchase_stock (`purchase_stock/models/stock_move.py:99-102`) but no base definition and no `_create_extra_move` exist in the tree (grep); the `additional` flag remains (L178) | earlier versions created extra moves for surplus quantity |
| M-09 | LOW | `product_qty` inverse raises a UserError (L485-490) | not asserted |
| M-10 | LOW | `reservation_date` and the picking-type `reservation_method` (at_confirm, manual, by_date) drive reservation timing (L730-739, L1734-1735, L1972-1973; `stock/models/stock_picking.py:68-71`) | not asserted |
| M-11 | LOW | `_trigger_assign` honours the system parameter `stock.picking_no_auto_reserve` (L2637) | not asserted |
| M-12 | INFO | `restrict_partner_id` is the owner restriction; no `owner_id` field on the move (L163-165) | not asserted |
| M-13 | INFO | returns use `origin_returned_move_id` and `returned_move_ids`; no `return_line_ids` (L155-158) | not asserted |
| M-14 | INFO | seven state values; help text lists five (L107-120) | not asserted |
| M-15 | INFO | `_adjust_procure_method` has callers only in mrp, repair and a test (section 4.5) | not asserted |
| M-16 | INFO | `_create_backorder` compares at `Product Unit` digits (L2328-2329) | not asserted |
| M-17 | INFO | the `_compute_quantity` docstring (L413-420) describes rounded results and mentions backorder and extra-move use, while the code converts with `round=False` (L408, L438) | not asserted |
| M-18 | INFO | `quants_cache` in `_action_assign` (L2073-2074) is filled and never read again in `stock/models/stock_move.py` (grep); stale comments at L2059 and L2405 | not asserted |

---

## 11. UNKNOWN / not verified

- Access rights and record rules for `stock.move` (`ir.model.access`, rule records) were not read.
- Views, reports, wizards and data files were not read, except the pointer reads listed in the header.
- `stock.picking` actions (the availability button, `button_validate` beyond L1275-1285), `stock.quant` internals (U228), `stock.rule` beyond `_run_pull` and `_get_stock_move_values` (U203) and the `stock.rule.run` dispatch were not read; they appear only as call sites.
- No Odoo instance was started and no database was queried; runtime behaviour was not exercised and the tests listed in section 4.5 were located but not run.
- The extension modules in section 9 other than mrp, sale_stock, purchase_stock and stock_account were not inventoried; the file list comes from four literal grep patterns and may miss other spellings of `_inherit`.
- Statements about earlier versions are baseline knowledge and are not verifiable in this tree.
- The `_action_synch_order` overrides in sale_stock (`sale_stock/models/stock.py:37-87`) and purchase_stock (`purchase_stock/models/stock_move.py:61-93`) are located, but their behaviour was not analysed (U233, sale and purchase units).

---

## 12. Claim cross-reference index

| Claim | Topic | Section | Pointer |
|---|---|---|---|
| U234-C01 | state values | 2.1 | `stock/models/stock_move.py:107-120` |
| U234-C02 | confirmation routing | 2.2, 2.3 | `stock/models/stock_move.py:1701-1712` |
| U234-C03 | state recompute | 2.4 | `stock/models/stock_move.py:2419-2439` |
| U234-C04 | done stamp | 6.1 | `stock/models/stock_move.py:2289-2303` |
| U234-C05 | cancel propagation | 2.5 | `stock/models/stock_move.py:2201-2221` |
| U234-C06 | demand field | 3.1 | `stock/models/stock_move.py:58-65` |
| U234-C07 | quantity compute | 3.3 | `stock/models/stock_move.py:411-441` |
| U234-C08 | picked flag | 3.2 | `stock/models/stock_move.py:282-291` |
| U234-C09 | supply method field | 4.1 | `stock/models/stock_move.py:131-138` |
| U234-C10 | supply method adjustment | 4.5 | `stock/models/stock_move.py:2599-2607` |
| U234-C11 | chain links | 4.1 | `stock/models/stock_move.py:98-105` |
| U234-C12 | procurement destination | 4.3 | `stock/models/stock_move.py:1849-1850` |
| U234-C13 | bypass branch | 5.3 | `stock/models/stock_move.py:2086-2124` |
| U234-C14 | unchained reservation | 5.3 | `stock/models/stock_move.py:2126-2144` |
| U234-C15 | chained reservation | 5.3 | `stock/models/stock_move.py:2145-2178` |
| U234-C16 | assign at confirm | 5.2 | `stock/models/stock_move.py:1970-1973` |
| U234-C17 | trigger assign | 5.6 | `stock/models/stock_move.py:2633-2654` |
| U234-C18 | backorder split | 6.2 | `stock/models/stock_move.py:2322-2338` |
| U234-C19 | merge keys | 6.4 | `stock/models/stock_move.py:1281-1293` |
| U234-C20 | final location | 7.2 | `stock/models/stock_move.py:236-244` |
| U234-C21 | allowed units | 8.1 | `stock/models/stock_move.py:202-205` |
| U234-C22 | production links | 9 | `mrp/models/stock_move.py:31-34` |
| U234-C23 | validation filter | 6.1 | `stock/models/stock_move.py:2258-2269` |
| U234-C24 | reference records | 7.1, 10 | `stock/models/stock_move.py:141-142` |
| U234-C25 | refund flag | 9, 10 | `stock_account/models/stock_move.py:20-22` |
| U234-C26 | extra-move override | 9, 10 | `purchase_stock/models/stock_move.py:99-102` |
