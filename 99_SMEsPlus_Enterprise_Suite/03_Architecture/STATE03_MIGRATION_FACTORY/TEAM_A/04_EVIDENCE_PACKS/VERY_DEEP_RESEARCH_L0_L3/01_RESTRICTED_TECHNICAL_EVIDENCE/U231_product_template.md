# U231 — product.template: type, is_storable, tracking, UoM, tax fields, variant propagation
**VDR Research Unit U231 | Module: product (+ stock, stock_account, sale, sale_stock, purchase, account, uom) | File: product/models/product_template.py**
**Source SHA256 (first 12 chars): a6a814f94a7f**
**Odoo Community 19.0.post20260921 — READ-ONLY evidence, no fabrication**
**Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**

Full SHA-256 of `product/models/product_template.py` (1598 lines): `a6a814f94a7f7d19b32fc8b4b6e2f52769c3b1d40602346126e55398f75768d4`

---

## 0. Method, scope and caveats

- **Method.** Evidence comes from direct reading of Python source files under the read-only Community addons tree and from text searches (grep) over that tree. No Odoo process was started. Nothing was written under the source tree.
- **Pointers.** Every pointer has the form `<addon>/<path>.py:<line>[-<line>]`, relative to the addons directory. Excerpts below are copied by a script from the cited line ranges; the left gutter shows the true source line number. No excerpt was retyped.
- **Absence statements.** "Absent" means zero hits in code, view, data and script files (py, xml, js, csv, json, html, scss) of every addon in the tree. Translation catalogs are not code. Searches over ALL file types for `detailed_type` and `uom_po_id` return hits only in locale `.po` catalogs (stale translation strings; examples: product/i18n/km.po, product/i18n/es_CL.po, product/i18n/fr_BE.po, product/i18n/lb.po, product/i18n/af.po, product/i18n/am.po; also stock/i18n, event_sale/i18n and website_sale_slides/i18n/lb.po). Those hits are not evidence that either field exists.
- **Packaging search.** A regular-expression search for the text `product.packaging` returned only false positives (the report file product_packaging.xml listed at product/__manifest__.py:56, and a test method name at point_of_sale/tests/test_frontend.py:1273). A fixed-string search for that model name over py, xml, js and csv files is empty. No claim in this file depends on a model of that name; packagings appear in v19 as `uom_ids` and the `product.uom` model (section 4).
- **Baseline.** Statements about v16/v17 behaviour (that `type='product'`, `detailed_type`, `uom_po_id`, `uom.category` and `uom_type` existed earlier) come from the unit scope text. They are NOT verified in this tree. What is verified here is the v19 side: the names are absent or changed as cited.
- **No in-tree migration code.** The product and stock addon directories contain no migrations or upgrades directory in this tree, so there is no shipped migration script for these models to read.
- **Not read, not claimed.** (a) The storage format the ORM uses for company-dependent fields; only the declaration of `standard_price` is cited. (b) How the ORM merges `@api.depends` lists across overriding modules. (c) `active_test` behaviour of barcode searches beyond the cited code. (d) Legacy value names of the valuation selections. (e) What the ORM does when an explicit `tracking` value and the recompute triggered by `is_storable` meet in one write. (f) The content of the eleven XML files that mention `is_storable` (section 2.3).
- **Search limits.** The search for `@api.constrains` on `tracking` or `is_storable` matches only single-line decorators; a decorator split over several lines would not appear.

---

## 1. Product kind: `type`, `detailed_type`, and what `type='product'` became

### 1.1 Model header

**product/models/product_template.py:18-24**

```python
   18  class ProductTemplate(models.Model):
   19      _name = 'product.template'
   20      _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
   21      _description = "Product"
   22      _order = "is_favorite desc, name"
   23      _check_company_auto = True
   24      _check_company_domain = models.check_company_domain_parent_of
```

**product/models/product_product.py:19-21**

```python
   19      _inherits = {'product.template': 'product_tmpl_id'}
   20      _inherit = ['mail.thread', 'mail.activity.mixin']
   21      _order = 'default_code, name, id'
```

`product.product` delegates to `product.template` through `_inherits` (product/models/product_product.py:19) and orders by `default_code, name, id` (line 21). The template is ordered by `is_favorite desc, name` and sets `_check_company_auto = True` (product/models/product_template.py:22-23).

### 1.2 The `type` selection

**product/models/product_template.py:54-65**

```python
   54      type = fields.Selection(
   55          string="Product Type",
   56          help="Goods are tangible materials and merchandise you provide.\n"
   57               "A service is a non-material product you provide.",
   58          selection=[
   59              ('consu', "Goods"),
   60              ('service', "Service"),
   61              ('combo', "Combo"),
   62          ],
   63          required=True,
   64          default='consu',
   65      )
```

Verified facts:

1. Values are exactly `consu` (label "Goods"), `service` ("Service") and `combo` ("Combo"; line 61). The field is `required=True` with `default='consu'` and the string "Product Type" (lines 55, 63-64).
2. This is the only declaration of the product-template `type` selection. A search for `type = fields.Selection(` over all Python files lists no second declaration and no `selection_add` extension of the product-template field; the other hits belong to unrelated models (barcode rules, BoM, views, partners, journals, attachments, leads, payment methods).
3. No selectable value `'product'` exists. A search of Python files for an equality or domain term comparing `type` to the literal `'product'` returns nothing.
4. `detailed_type` is absent from code. Zero hits in py, xml, js, csv, json, html and scss; hits exist only in stale `.po` catalogs (section 0).
5. The stock-tracking meaning that `type='product'` carried in earlier releases is expressed in v19 by `is_storable` on a template whose type is `consu` (section 2). The "earlier releases" half is baseline (section 0) and is not verified in this tree.

### 1.3 Code that reacts to `type`

**product/models/product_template.py:198-203**

```python
  198      @api.depends('type')
  199      def _compute_service_tracking(self):
  200          self.filtered(lambda product: product.type != 'service').service_tracking = 'no'
  201  
  202      def _compute_purchase_ok(self):
  203          pass
```

- product/models/product_template.py:198-200: `_compute_service_tracking` depends on `type` and resets non-service templates to `'no'`. Lines 202-203: `_compute_purchase_ok` is a no-op body.

**product/models/product_template.py:459-472**

```python
  459      @api.onchange('type')
  460      def _onchange_type(self):
  461          if self.type == 'combo':
  462              if self.attribute_line_ids:
  463                  raise UserError(_("Combo products can't have attributes."))
  464              combo_items = self.env['product.combo.item'].sudo().search([
  465                  ('product_id', 'in', self.product_variant_ids.ids)
  466              ])
  467              if combo_items:
  468                  raise UserError(_(
  469                      "This product is part of a combo, so its type can't be changed to \"combo\"."
  470                  ))
  471              self.purchase_ok = False
  472          return {}
```

- product/models/product_template.py:459-472 (onchange handler, form view only): for `combo`, raises when the template has attribute lines, raises when the product is already a combo item, and sets `purchase_ok = False`. Basis for "form view only": the framework docstring of the onchange decorator (odoo/orm/decorators.py, lines 189-195; a file outside the addons root, read only for this note and not listed in the section 13 inventory) says the method is called in the form views where the field appears, on a pseudo-record that holds the form values.

**product/models/product_template.py:489-507**

```python
  489      @api.constrains('type', 'combo_ids')
  490      def _check_combo_ids_not_empty(self):
  491          for template in self:
  492              if template.type == 'combo' and not template.combo_ids:
  493                  raise ValidationError(_("A combo product must contain at least 1 combo choice."))
  494  
  495      @api.constrains('type', 'combo_ids', 'sale_ok')
  496      def _check_sale_combo_ids(self):
  497          for template in self:
  498              if (
  499                  template.type == 'combo'
  500                  and template.sale_ok
  501                  and any(
  502                      not product.sale_ok for product in template.combo_ids.combo_item_ids.product_id
  503                  )
  504              ):
  505                  raise ValidationError(
  506                      _("A sellable combo product can only contain sellable products.")
  507                  )
```

- product/models/product_template.py:489-493 and 495-507 (Python constraints, checked when the listed fields are written on create or write): a combo needs at least one combo choice; a sellable combo may only contain sellable products. Line 603-605 (inside `write`, section 9) clears `combo_ids` whenever `type` is written with a value other than `combo`.

**stock/models/product.py:1098-1113**

```python
 1098      @api.onchange('type')
 1099      def _onchange_type(self):
 1100          # Return a warning when trying to change the product type
 1101          res = super()._onchange_type()
 1102          if self.ids and self.product_variant_ids.ids and self.env['stock.move.line'].sudo().search_count([
 1103              ('product_id', 'in', self.product_variant_ids.ids), ('state', '!=', 'cancel')
 1104          ]):
 1105              res['warning'] = {
 1106                  'title': _('Warning!'),
 1107                  'message': _(
 1108                      'This product has been used in at least one inventory movement. '
 1109                      'It is not advised to change the Product Type since it can lead to inconsistencies. '
 1110                      'A better solution could be to archive the product and create a new one instead.'
 1111                  )
 1112              }
 1113          return res
```

- stock/models/product.py:1098-1113: stock `_onchange_type` returns a warning when the product is used in a non-cancelled stock move line.

**sale/models/product_template.py:148-156**

```python
  148      @api.onchange('type')
  149      def _onchange_type(self):
  150          res = super()._onchange_type()
  151          if self._origin and self.sales_count > 0:
  152              res['warning'] = {
  153                  'title': _("Warning"),
  154                  'message': _("You cannot change the product's type because it is already used in sales orders.")
  155              }
  156          return res
```

- sale/models/product_template.py:148-156: sale `_onchange_type` returns a warning when the product has sales (`sales_count > 0`).

**account/models/product.py:152-157**

```python
  152      @api.onchange('type')
  153      def _onchange_type(self):
  154          if self.type == 'combo':
  155              self.taxes_id = False
  156              self.supplier_taxes_id = False
  157          return super()._onchange_type()
```

- account/models/product.py:152-157: account `_onchange_type` clears both tax fields for `combo`.

- Further `type`-dependent computes are cited in section 2.2 (`is_storable`), section 3 (`tracking`) and section 8 (`purchase_method`, `invoice_policy`, `service_type`).

---

## 2. `is_storable` ("Track Inventory")

### 2.1 Declaration

**stock/models/product.py:839-841**

```python
  839      is_storable = fields.Boolean(
  840          'Track Inventory', store=True, compute='compute_is_storable', readonly=False,
  841          default=False, precompute=True, tracking=True, help='A storable product is a product for which you manage stock.')
```

Facts:

1. Declared once, in the stock addon (stock/models/product.py:839). A search for `is_storable = fields.` over all Python files finds that declaration plus three `related=` mirrors: stock/models/stock_move.py:177, sale_stock/models/sale_order_line.py:27 and purchase_stock/models/purchase_order_line.py:34. The product addon does not declare it.
2. Properties (from the excerpt): stored, computed through the public-named method `compute_is_storable`, `readonly=False` (user-editable), `default=False`, `precompute=True`, `tracking=True`.
3. Inference from the declaration location (not tested): an instance without the stock addon has no such field.

### 2.2 The compute

**stock/models/product.py:911-913**

```python
  911      @api.depends('type')
  912      def compute_is_storable(self):
  913          self.filtered(lambda t: t.type != 'consu' and t.is_storable).is_storable = False
```

The compute depends on `type` only. For templates whose `type` is not `consu` and whose flag is set, it assigns `False` (line 913). It never assigns `True`.

### 2.3 What writes the flag

A search of non-test Python files for assignments and mapping keys involving `is_storable` shows:

- The only assignment that writes the database is the compute at stock/models/product.py:913.
- website_sale_stock/models/product_template.py:63 holds `'is_storable': True,` as a key in a dictionary update applied to the result of `_get_additionnal_combination_info` (spelling as in the source; def at line 41). The guard at lines 59-60 returns early for non-storable products. This is not a database write:

**website_sale_stock/models/product_template.py:59-66**

```python
   59          if not product_or_template.is_storable:
   60              return res
   61  
   62          res.update({
   63              'is_storable': True,
   64              'allow_out_of_stock_order': product_or_template.allow_out_of_stock_order,
   65              'available_threshold': product_or_template.available_threshold,
   66          })
```

- mrp/report/mrp_report_bom_structure.py:218, 368 and 535 read the flag into report dictionaries; stock/report/report_stock_quantity.py:74 reads it in SQL.
- XML: eleven XML files carry `name="is_storable"` entries (not opened for content): sale_stock/data/sale_order_demo.xml, mrp/data/mrp_demo.xml, project_mrp_account/data/project_mrp_account_demo.xml, point_of_sale/data/scenarios/furniture_data.xml, stock/data/stock_demo_pre.xml, stock/data/stock_demo2.xml (data and demo files) and mrp/views/mrp_production_views.xml, point_of_sale/views/product_view.xml, stock/views/stock_picking_views.xml, stock/views/product_views.xml, repair/views/repair_views.xml (views). No CSV file mentions the field.
- Otherwise the flag is set by the user or an ORM caller, because the field is `readonly=False` and stored.

### 2.4 Create and write on the template

**stock/models/product.py:1115-1127**

```python
 1115      @api.model_create_multi
 1116      def create(self, vals_list):
 1117          product_tmpl_quantities = [
 1118              vals.pop('qty_available', 0) for vals in vals_list
 1119          ]
 1120  
 1121          product_templates = super().create(vals_list)
 1122  
 1123          if any(product_tmpl_quantities):
 1124              for product_tmpl, qty in zip(product_templates, product_tmpl_quantities):
 1125                  if qty > 0 and product_tmpl.tracking == 'none':
 1126                      product_tmpl.product_variant_id.qty_available = qty
 1127          return product_templates
```

**stock/models/product.py:1129-1160**

```python
 1129      def write(self, vals):
 1130          if 'company_id' in vals and vals['company_id']:
 1131              products_changing_company = self.filtered(lambda product: product.company_id.id != vals['company_id'])
 1132              if products_changing_company:
 1133                  move = self.env['stock.move'].sudo().search([
 1134                      ('product_id', 'in', products_changing_company.product_variant_ids.ids),
 1135                      ('company_id', 'not in', [vals['company_id'], False]),
 1136                  ], order=None, limit=1)
 1137                  if move:
 1138                      raise UserError(_("This product's company cannot be changed as long as there are stock moves of it belonging to another company."))
 1139  
 1140                  # Forbid changing a product's company when quant(s) exist in another company.
 1141                  quant = self.env['stock.quant'].sudo().search([
 1142                      ('product_id', 'in', products_changing_company.product_variant_ids.ids),
 1143                      ('company_id', 'not in', [vals['company_id'], False]),
 1144                      ('quantity', '!=', 0),
 1145                  ], order=None, limit=1)
 1146                  if quant:
 1147                      raise UserError(_("This product's company cannot be changed as long as there are quantities of it belonging to another company."))
 1148  
 1149          clean_inventory = False
 1150          templates_to_reset = self.env['product.template']
 1151          if 'is_storable' in vals and any(vals['is_storable'] != prod_tmpl.is_storable and not prod_tmpl.is_storable for prod_tmpl in self):
 1152              clean_inventory = True
 1153              if vals['is_storable']:
 1154                  templates_to_reset = self.filtered(lambda tmpl: not tmpl.is_storable)
 1155  
 1156          res = super().write(vals)
 1157          if clean_inventory:
 1158              self.env['stock.quant'].sudo()._clean_reservations()
 1159              templates_to_reset._reset_inventory()
 1160          return res
```

- Create (1115-1127) contains no inventory reset.
- Write (1129-1160): lines 1130-1147 are a company-change guard (section 11). At lines 1149-1152 the local flag `clean_inventory` is set when `is_storable` is among the written values and at least one template currently has the flag false while a different value is written (the condition is at line 1151). When the written value is truthy, `templates_to_reset` is filled with the templates that are currently NOT storable (lines 1153-1154). After `super().write(vals)`, if `clean_inventory` is set, the code calls `_clean_reservations()` on `stock.quant` through `sudo()` and then `templates_to_reset._reset_inventory()` (lines 1156-1159).

### 2.5 `_reset_inventory`

**stock/models/product.py:1162-1202**

```python
 1162      def _reset_inventory(self):
 1163          """
 1164          This methods create quants to match the move history of products that become storable
 1165          and make inventory adjustments to resets their inventory quantities.
 1166  
 1167          These adjustments are necessary to ensure the integrity of the product valuation.
 1168          """
 1169          move_line_domain = Domain([
 1170              ('product_id', 'in', self.product_variant_ids.ids),
 1171              ('state', '=', 'done'),
 1172              '|',
 1173                  ('location_usage', 'in', ('internal', 'transit')),
 1174                  ('location_dest_usage', 'in', ('internal', 'transit')),
 1175          ])
 1176          move_lines_to_match = self.env['stock.move.line'].search_fetch(domain=move_line_domain, field_names=('product_id', 'location_id', 'quantity_product_uom'))
 1177          inventory_ledger = defaultdict(float)
 1178          for move_line in move_lines_to_match:
 1179              if move_line.location_usage in ('internal', 'transit'):
 1180                  inventory_ledger[move_line.product_id, move_line.location_id] -= move_line.quantity_product_uom
 1181              if move_line.location_dest_usage in ('internal', 'transit'):
 1182                  inventory_ledger[move_line.product_id, move_line.location_dest_id] += move_line.quantity_product_uom
 1183          # Unticking "Track Inventory" keeps the existing quants, so on a
 1184          # storable -> not storable -> storable toggle only counter balance the
 1185          # moves that aren't already reflected on hand.
 1186          on_hand = self.env['stock.quant']._read_group(
 1187              [('product_id', 'in', self.product_variant_ids.ids),
 1188               ('location_id.usage', 'in', ('internal', 'transit'))],
 1189              ['product_id', 'location_id'], ['quantity:sum'],
 1190          )
 1191          for product, location, quantity in on_hand:
 1192              if (product, location) in inventory_ledger:
 1193                  inventory_ledger[product, location] -= quantity
 1194          quants_to_reset = self.env['stock.quant'].create([
 1195              {
 1196                  'product_id': product.id,
 1197                  'location_id': location.id,
 1198                  'quantity': quantity,
 1199                  'inventory_quantity': 0.0,
 1200              } for (product, location), quantity in inventory_ledger.items() if not product.uom_id.is_zero(quantity)
 1201          ])
 1202          quants_to_reset._apply_inventory()
```

- Docstring (lines 1163-1168): quants are created to match the move history of products that become storable, with inventory adjustments, to preserve the integrity of valuation.
- Mechanics: it selects done move lines whose source or destination location has internal or transit usage (1169-1176) and builds a ledger per product and location, subtracting the quantity at the source and adding it at the destination (1177-1182). It then subtracts the on-hand quantity of quants that already exist for those product and location pairs (1186-1193; the comment at lines 1183-1185 states that unticking Track Inventory keeps the existing quants). It creates quants with `quantity=<ledger>` and `inventory_quantity=0.0`, skipping zero ledgers through `product.uom_id.is_zero` (1194-1201), and finally calls `quants_to_reset._apply_inventory()` (line 1202).
- Migration relevance: switching the flag to true through the ORM write path on populated data triggers this procedure; creating the template with the flag already set does not (2.4).

### 2.6 `_clean_reservations`

**stock/models/stock_quant.py:1141-1175**

```python
 1141      @api.model
 1142      def _clean_reservations(self):
 1143          reserved_quants = self.env['stock.quant']._read_group(
 1144              [('reserved_quantity', '!=', 0)],
 1145              ['product_id', 'location_id', 'lot_id', 'package_id', 'owner_id'],
 1146              ['reserved_quantity:sum', 'id:recordset'],
 1147          )
 1148          reserved_move_lines = self.env['stock.move.line']._read_group(
 1149              [
 1150                  ('state', 'in', ['assigned', 'partially_available', 'waiting', 'confirmed']),
 1151                  ('quantity_product_uom', '!=', 0),
 1152                  ('product_id.is_storable', '=', True),
 1153              ],
 1154              ['product_id', 'location_id', 'lot_id', 'package_id', 'owner_id'],
 1155              ['quantity_product_uom:sum'],
 1156          )
 1157          reserved_move_lines = {
 1158              (product, location, lot, package, owner): reserved_quantity
 1159              for product, location, lot, package, owner, reserved_quantity in reserved_move_lines
 1160          }
 1161          for product, location, lot, package, owner, reserved_quantity, quants in reserved_quants:
 1162              ml_reserved_qty = reserved_move_lines.get((product, location, lot, package, owner), 0)
 1163              if location.should_bypass_reservation():
 1164                  quants._update_reserved_quantity(product, location, -reserved_quantity, lot_id=lot, package_id=package, owner_id=owner)
 1165              elif product.uom_id.compare(reserved_quantity, ml_reserved_qty) != 0:
 1166                  quants._update_reserved_quantity(product, location, ml_reserved_qty - reserved_quantity, lot_id=lot, package_id=package, owner_id=owner)
 1167              if ml_reserved_qty:
 1168                  del reserved_move_lines[(product, location, lot, package, owner)]
 1169  
 1170          for (product, location, lot, package, owner), reserved_quantity in reserved_move_lines.items():
 1171              if location.should_bypass_reservation() or\
 1172                  self.env['stock.quant']._should_bypass_product(product, location, reserved_quantity, lot, package, owner):
 1173                  continue
 1174              else:
 1175                  self.env['stock.quant']._update_reserved_quantity(product, location, reserved_quantity, lot_id=lot, package_id=package, owner_id=owner)
```

The method (def at line 1142) compares two groupings keyed by product, location, lot, package and owner: the reserved quantity held on quants (any product), and the sum of `quantity_product_uom` over move lines in states assigned, partially_available, waiting or confirmed whose product is storable (line 1152). For each quant group: if the location bypasses reservation, the reserved quantity is reduced to zero (line 1164); otherwise, if it differs from the move-line sum, it is adjusted to that sum (1165-1166). Move-line sums that have no reserved quant are then reserved, unless the location or `_should_bypass_product` says to bypass (1170-1175).

### 2.7 Stock-side gates that read the flag

**stock/models/stock_move.py:1967-1972**

```python
 1967      def _should_bypass_reservation(self, forced_location=False):
 1968          self.ensure_one()
 1969          location = forced_location or self.location_id
 1970          return location.should_bypass_reservation() or not self.product_id.is_storable
 1971  
 1972      def _should_assign_at_confirm(self):
```

- stock/models/stock_move.py:1967-1970: `_should_bypass_reservation` returns true when the location bypasses reservation or the product is not storable; line 1972 starts `_should_assign_at_confirm`.

**stock/models/stock_move.py:514-516**

```python
  514          not_product_moves = self.filtered(lambda move: not move.product_id.is_storable)
  515          for move in not_product_moves:
  516              move.forecast_availability = move.product_qty
```

- stock/models/stock_move.py:514-516: non-storable moves get `forecast_availability = move.product_qty`.

**stock/models/stock_move_line.py:394-397**

```python
  394              if move:
  395                  reservation = not move._should_bypass_reservation()
  396              else:
  397                  reservation = product.is_storable and not location.should_bypass_reservation()
```

**stock/models/stock_move_line.py:407-412**

```python
  407          for ml in mls:
  408              if ml.state == 'done':
  409                  if ml.product_id.is_storable:
  410                      Quant = self.env['stock.quant']
  411                      quantity = ml.product_uom_id._compute_quantity(ml.quantity, ml.move_id.product_id.uom_id, rounding_method='HALF-UP')
  412                      available_qty, in_date = Quant._update_available_quantity(ml.product_id, ml.location_id, -quantity, lot_id=ml.lot_id, package_id=ml.package_id, owner_id=ml.owner_id)
```

- stock/models/stock_move_line.py:394-397 (inside create): with a linked move, the reservation decision is delegated to the move's `_should_bypass_reservation`; without a move it is `product.is_storable and not location.should_bypass_reservation()` (line 397). Lines 407-412: for lines created in state done, the quant update runs only when the product is storable (line 409).

**stock/models/stock_quant.py:38-43**

```python
   38      def _domain_product_id(self):
   39          if self.env.user.has_group('stock.group_stock_user'):
   40              return ("[] if not context.get('inventory_mode') else"
   41                  " [('is_storable', '=', True), ('product_tmpl_id', 'in', context.get('product_tmpl_ids', []) + [context.get('product_tmpl_id', 0)])] if context.get('product_tmpl_ids') or context.get('product_tmpl_id') else"
   42                  " [('is_storable', '=', True)]")
   43          return "[]"
```

**stock/models/stock_quant.py:582-585**

```python
  582      @api.constrains('product_id')
  583      def check_product_id(self):
  584          if any(not elem.product_id.is_storable for elem in self):
  585              raise ValidationError(_('Quants cannot be created for consumables or services.'))
```

- stock/models/stock_quant.py:38-43 (`_domain_product_id`) and 582-585 (`check_product_id`): quants cannot be created for consumables or services.

**stock/models/product.py:270-292**

```python
  270      def _inverse_qty_available(self):
  271          """
  272          Inverse method for the 'qty_available' field, enabling manual adjustment of stock on hand quantity
  273          in the product form. To prevent the automatic creation of stock quants when the
  274          'compute_quantities' method is triggered, this method skips quant creation by custom context key.
  275          """
  276          if self.env.context.get('skip_qty_available_update', False):
  277              return
  278          warehouse = None
  279          for product in self:
  280              if (
  281                  product.type == "consu" and product.is_storable and float_compare(product.qty_available,
  282                       0.0, precision_rounding=product.uom_id.rounding) >= 0
  283              ):
  284                  if warehouse is None:
  285                      warehouse = self.env['stock.warehouse'].search(
  286                          [('company_id', '=', self.env.company.id)], limit=1
  287                      )
  288                  self.env['stock.quant'].with_context(inventory_mode=True, from_inverse_qty=True).create({
  289                      'product_id': product.id,
  290                      'location_id': warehouse.lot_stock_id.id,
  291                      'inventory_quantity': product.qty_available,
  292                  })._apply_inventory()
```

- stock/models/product.py:270-292: the on-hand inverse on the variant. It returns at once when the context key `skip_qty_available_update` is truthy (276-277). For each variant whose `type` is `consu`, whose `is_storable` is true and whose `qty_available` is not negative (280-283), it looks up the first warehouse of the current company once (284-287), creates a quant at that warehouse's stock location with `inventory_quantity` set to the entered on-hand quantity in inventory mode, and applies it (288-292). This method creates no quant for a non-storable variant.

**stock/models/product.py:543-550**

```python
  543          if include_zero:
  544              products_without_quants_in_domain = self.env['product.product'].search([
  545                  ('is_storable', '=', True),
  546                  ('id', 'not in', list(processed_product_ids))],
  547                  order='id'
  548              )
  549              product_ids |= set(products_without_quants_in_domain.ids)
  550          return list(product_ids)
```

- stock/models/product.py:543-549 (inside `_search_field_by_quants`, def at line 511): when the searched comparison accepts zero, storable products that have no quant in the searched locations are added to the result; line 545 restricts that addition to `is_storable`.

**stock/models/product.py:952-960**

```python
  952      @api.depends('is_storable')
  953      def _compute_show_qty_status_button(self):
  954          for template in self:
  955              template.show_on_hand_qty_status_button = template.is_storable
  956              template.show_forecasted_qty_status_button = template.is_storable and template.product_variant_id
  957  
  958      @api.depends('is_storable')
  959      def _compute_has_available_route_ids(self):
  960          self.has_available_route_ids = self.env['stock.route'].search_count([('product_selectable', '=', True)])
```

- stock/models/product.py:952-956: template `_compute_show_qty_status_button` sets the on-hand status button to the flag value and the forecast button to the flag combined with the existence of a first variant (line 956). Lines 958-960: `_compute_has_available_route_ids` is recomputed when `is_storable` changes; its body does not read the flag.

### 2.8 Valuation gate in stock_account

**stock_account/models/stock_move.py:95-98**

```python
   95      @api.depends('state', 'move_line_ids')
   96      def _compute_is_valued(self):
   97          for move in self:
   98              move.is_valued = move.is_in or move.is_out
```

**stock_account/models/stock_move.py:659-667**

```python
  659      def _should_create_account_move(self):
  660          """Determines if an account move should be created for this move.
  661          :return: True if an account move should be created, False otherwise.
  662          """
  663          self.ensure_one()
  664          return self.product_id.is_storable and self.is_valued\
  665          and (self.location_dest_id.valuation_account_id or self.location_id.valuation_account_id)\
  666          and not float_is_zero(self.quantity, precision_rounding=self.product_uom.rounding)\
  667          and self.product_id.valuation == 'real_time'
```

- stock_account/models/stock_move.py:659-667: an accounting entry is created for a stock move only when the product is storable and the move is valued, the destination or source location carries a valuation account, the quantity is non-zero, and the product's `valuation` is `real_time` (line 667). `is_valued` is computed at lines 95-98.

**stock_account/models/account_move_line.py:30-35**

```python
   30      def _eligible_for_stock_account(self):
   31          self.ensure_one()
   32          if not self.product_id.is_storable:
   33              return False
   34          moves = self._get_stock_moves()
   35          return all(not m._is_dropshipped() for m in moves)
```

- stock_account/models/account_move_line.py:30-35: `_eligible_for_stock_account` is false for non-storable products and otherwise true only when none of the moves is dropshipped.

---

## 3. `tracking` (none / lot / serial)

### 3.1 Declaration

**stock/models/product.py:856-862**

```python
  856      tracking = fields.Selection([
  857          ('serial', 'By Unique Serial Number'),
  858          ('lot', 'By Lots'),
  859          ('none', 'By Quantity')],
  860          string="Tracking", required=True, default='none', # Not having a default value here causes issues when migrating.
  861          compute='_compute_tracking', store=True, readonly=False, precompute=True,
  862          help="Ensure the traceability of a storable product in your warehouse.")
```

Facts:

1. Declared once, in the stock addon (stock/models/product.py:856). A search for `tracking = fields.Selection` over Python files finds that declaration plus `related=` mirrors at stock/models/stock_move_line.py:90, stock/models/stock_quant.py:92, stock/models/stock_scrap.py:29, mrp/models/mrp_bom.py:717 and repair/models/repair.py:100.
2. Values: `serial` "By Unique Serial Number", `lot` "By Lots", `none` "By Quantity". The field is required with `default='none'`; the inline comment at line 860 states that having no default there causes issues when migrating. It is a stored, `readonly=False`, `precompute=True` compute (`_compute_tracking`).

### 3.2 Compute and onchange

**stock/models/product.py:1090-1096**

```python
 1090      @api.onchange('tracking')
 1091      def _onchange_tracking(self):
 1092          return self.mapped('product_variant_ids')._onchange_tracking()
 1093  
 1094      @api.depends('is_storable')
 1095      def _compute_tracking(self):
 1096          self.filtered(lambda t: not t.is_storable and t.tracking != 'none').tracking = 'none'
```

- stock/models/product.py:1090-1092: template `_onchange_tracking` delegates to the variants. Lines 1094-1096: `_compute_tracking` depends on `is_storable` and resets non-storable templates to `none`.

**stock/models/product.py:564-570**

```python
  564      @api.onchange('tracking')
  565      def _onchange_tracking(self):
  566          if any(product.tracking != 'none' and product.qty_available > 0 for product in self):
  567              return {
  568                  'warning': {
  569                      'title': _('Warning!'),
  570                      'message': _("You have product(s) in stock that have no lot/serial number. You can assign lot/serial numbers by doing an inventory adjustment.")}}
```

- stock/models/product.py:564-570: variant `_onchange_tracking` returns a warning when any selected variant has a tracking value other than `none` and an on-hand quantity above zero (line 566); the message advises assigning lot or serial numbers by inventory adjustment.

### 3.3 Constraints and interplay with `is_storable`

- No `@api.constrains` on `tracking` or `is_storable` exists in the tree (single-line decorator search over all Python files for decorators naming either field). The search returned only constraints on the separate field `service_tracking`: event_product/models/product_product.py:10, event_booth_sale/models/product_template.py:25 and event_booth_sale/models/product_product.py:13. `tracking` is therefore tied to `is_storable` only through the compute above.
- The quant model carries three decorated Python constraints (stock/models/stock_quant.py:582, 605, 611): `check_product_id` on `product_id` (582-585, rejects non-storable products), `check_location_id` on `location_id` (605-609) and `check_lot_id` on `lot_id` (611-615, rejects a lot linked to another product). None is decorated for `tracking`.
- Serial uniqueness is checked by `check_quantity`. It is NOT decorated (line 586 is blank and line 587 is the `def`); it is called explicitly. `stock.move._check_quantity` (stock/models/stock_move.py:2242-2247) searches the quants of the move's product, destination location tree and lots, then calls it. `_check_quantity` runs at the end of `_action_done` (stock/models/stock_move.py:2315), at the end of move-line `create` (stock/models/stock_move_line.py:426, create spans 346-427) and in move-line `write` for done moves (stock/models/stock_move_line.py:513, write spans 429-570).

**stock/models/stock_quant.py:587-603**

```python
  587      def check_quantity(self):
  588          sn_quants = self.filtered(lambda q: q.product_id.tracking == 'serial' and q.location_id.usage != 'inventory' and q.lot_id)
  589          if not sn_quants:
  590              return
  591          domain = [
  592              ('product_id', 'in', sn_quants.product_id.ids),
  593              ('location_id', 'child_of', sn_quants.location_id.ids),
  594              ('lot_id', 'in', sn_quants.lot_id.ids)
  595          ]
  596          groups = self._read_group(
  597              domain,
  598              ['product_id', 'location_id', 'lot_id'],
  599              ['quantity:sum'],
  600          )
  601          for product, _location, lot, qty in groups:
  602              if product.uom_id.compare(abs(qty), 1) > 0:
  603                  raise ValidationError(_('The serial number has already been assigned: \n Product: %(product)s, Serial Number: %(serial_number)s', product=product.display_name, serial_number=lot.name))
```

**stock/models/stock_move.py:2242-2247**

```python
 2242      def _check_quantity(self):
 2243          return self.env['stock.quant'].sudo().search([
 2244              ('product_id', 'in', self.product_id.ids),
 2245              ('location_id', 'child_of', self.location_dest_id.ids),
 2246              ('lot_id', 'in', self.sudo().lot_ids.ids)
 2247          ]).check_quantity()
```

- `check_quantity` (587-603) keeps only quants of serial-tracked products that carry a lot and sit outside locations of usage `inventory` (line 588), sums the quantity per product, location and lot under the location tree (591-600), and raises a ValidationError when the absolute sum is greater than one in the product's unit (602-603).

### 3.4 Lot-valuated products (stock_account)

**stock_account/models/product.py:31-35**

```python
   31      lot_valuated = fields.Boolean(
   32          string="Valuation by Lot/Serial",
   33          compute='_compute_lot_valuated', store=True, readonly=False,
   34          help="If checked, the valuation will be specific by Lot/Serial number.",
   35      )
```

**stock_account/models/product.py:54-58**

```python
   54      @api.depends('tracking')
   55      def _compute_lot_valuated(self):
   56          for product in self:
   57              if product.tracking == 'none':
   58                  product.lot_valuated = False
```

**stock_account/models/product.py:81-125**

```python
   81      def write(self, vals):
   82          product_ids_to_update = set()
   83          lot_ids_to_update = set()
   84          if 'categ_id' in vals:
   85              category = self.env['product.category'].browse(vals['categ_id'])
   86              cost_method = category.property_cost_method if category else self.env.company.cost_method
   87              for product in self:
   88                  if product.cost_method != cost_method:
   89                      product_ids_to_update.update(product.product_variant_ids.ids)
   90  
   91          if 'lot_valuated' in vals:
   92              if vals.get('lot_valuated'):
   93                  products_to_enable = self.filtered(lambda p: not p.lot_valuated)
   94                  if products_to_enable:
   95                      problematic_quants = self.env['stock.quant'].search([
   96                          ('product_id', 'in', products_to_enable.product_variant_ids.ids),
   97                          ('lot_id', '=', False),
   98                          ('quantity', '!=', 0),
   99                          ('location_id.is_valued_internal', '=', True),
  100                      ])
  101                      if problematic_quants:
  102                          raise UserError(self.env._(
  103                              "You cannot enable lot valuation because the following products have"
  104                              " on-hand quantities without a lot/serial number:\n%s",
  105                              problematic_quants.product_id.mapped('display_name'),
  106                          ))
  107              for product in self:
  108                  if product.lot_valuated != vals.get('lot_valuated', product.lot_valuated):
  109                      product_ids_to_update.update(product.product_variant_ids.ids)
  110  
  111          products_to_update = self.env['product.product'].browse(product_ids_to_update)
  112          lot_ids_to_update.update(self.env['stock.lot'].sudo().search([
  113              ('product_id', 'in', products_to_update.filtered(lambda p: p.lot_valuated).ids),
  114          ]).ids)
  115  
  116          res = super().write(vals)
  117          if 'lot_valuated' in vals:
  118              lot_ids_to_update.update(self.env['stock.lot'].sudo().search([
  119                  ('product_id', 'in', self.product_variant_ids.ids),
  120              ]).ids)
  121          if product_ids_to_update:
  122              self.env['product.product'].browse(product_ids_to_update)._update_standard_price()
  123          if lot_ids_to_update:
  124              self.env['stock.lot'].browse(lot_ids_to_update).sudo()._update_standard_price()
  125          return res
```

- stock_account/models/product.py:31-35 declares `lot_valuated` ("Valuation by Lot/Serial"): a stored compute with `readonly=False`. Lines 54-58 (`@api.depends('tracking')`) set it to false when `tracking` is `none`; the compute never sets it to true.
- The template `write` override (stock_account/models/product.py:81-125) has three parts. (a) When `categ_id` is written, variants of templates whose current cost method differs from the new category's (or from the company's when no category is given) are queued for a standard price update (lines 84-89). (b) When a truthy `lot_valuated` is written, a UserError ("You cannot enable lot valuation because the following products have on-hand quantities without a lot/serial number") is raised if quants with no lot and a non-zero quantity exist in valued internal locations for the templates being switched on (lines 91-106). (c) After `super().write`, the queued variants run `_update_standard_price()` and the related lots run it through `sudo()` (lines 121-124).

---

## 4. Units of measure: `uom_id`, `uom_po_id`, the `uom.uom` redesign

### 4.1 Template fields

**product/models/product_template.py:116-123**

```python
  116      sale_ok = fields.Boolean('Sales', default=True)
  117      purchase_ok = fields.Boolean('Purchase', default=True, compute='_compute_purchase_ok', store=True, readonly=False)
  118      uom_id = fields.Many2one(
  119          'uom.uom', 'Unit', tracking=True,
  120          default=_get_default_uom_id, required=True,
  121          help="Default unit of measure used for all stock operations.")
  122      uom_ids = fields.Many2many('uom.uom', string='Packagings', help="Additional packagings for this product which can be used for sales", domain="[('id', '!=', uom_id)]")
  123      uom_name = fields.Char(string='Unit Name', related='uom_id.name', readonly=True)
```

**product/models/product_template.py:26-36**

```python
   26      @api.model
   27      def default_get(self, fields):
   28          res = super().default_get(fields)
   29          if ('uom_id' in fields and not res.get('uom_id')) or self.env.context.get('default_uom_id') is False:
   30              res['uom_id'] = self._get_default_uom_id().id
   31          return res
   32  
   33      @tools.ormcache()
   34      def _get_default_uom_id(self):
   35          # Deletion forbidden (at least through unlink)
   36          return self.env.ref('uom.product_uom_unit')
```

- `uom_id` (product/models/product_template.py:118-121): `uom.uom`, string "Unit", tracked, required, default `_get_default_uom_id`; help "Default unit of measure used for all stock operations." The default is `uom.product_uom_unit` (lines 33-36, cached with `@tools.ormcache()`), applied also in `default_get` (26-31).
- `uom_ids` (line 122): many-to-many to `uom.uom`, string "Packagings", domain `[('id', '!=', uom_id)]`. `uom_name` (line 123) is a related name.

**product/models/product_template.py:1571-1580**

```python
 1571      def _has_multiple_uoms(self) -> bool:
 1572          if self.type == 'combo':
 1573              return False
 1574          return self.env['res.groups']._is_feature_enabled('uom.group_uom') and len(
 1575              self._get_available_uoms()
 1576          ) > 1
 1577  
 1578      def _get_available_uoms(self):
 1579          self.ensure_one()
 1580          return self.uom_id | self.uom_ids
```

### 4.2 `uom_po_id` is absent

A search over py, xml, js, csv, json, html and scss files returns zero hits for `uom_po_id` (hits only in stale `.po` catalogs, section 0). The template declares one unit field, `uom_id`, plus the packaging list `uom_ids`.

### 4.3 `uom.uom` has no category

**uom/models/uom_uom.py:18-22**

```python
   18      _name = 'uom.uom'
   19      _description = 'Product Unit of Measure'
   20      _parent_name = 'relative_uom_id'
   21      _parent_store = True
   22      _order = 'sequence, relative_uom_id, id'
```

**uom/models/uom_uom.py:36-49**

```python
   36      relative_factor = fields.Float(
   37          'Contains', default=1.0, digits=0, required=True,  # force NUMERIC with unlimited precision
   38          help='How much bigger or smaller this unit is compared to the reference UoM for this unit')
   39      rounding = fields.Float('Rounding Precision', compute="_compute_rounding")
   40      active = fields.Boolean('Active', default=True, help="Uncheck the active field to disable a unit of measure without deleting it.")
   41      relative_uom_id = fields.Many2one('uom.uom', 'Reference Unit', ondelete='cascade', index='btree_not_null')
   42      related_uom_ids = fields.One2many('uom.uom', 'relative_uom_id', 'Related UoMs')
   43      factor = fields.Float('Absolute Quantity', digits=0, compute='_compute_factor', recursive=True, store=True)
   44      parent_path = fields.Char(index=True)
   45  
   46      _factor_gt_zero = models.Constraint(
   47          'CHECK (relative_factor!=0)',
   48          'The conversion ratio for a unit of measure cannot be 0!',
   49      )
```

- A literal-string search for the model name `uom.category` returns nothing in py, xml, js and csv files; a search for `uom_type` over py files returns nothing. `uom.uom` (uom/models/uom_uom.py, 230 lines) has no `category_id` field.
- Units relate through a reference-unit chain: `relative_uom_id` ("Reference Unit", cascade on delete, line 41), `relative_factor` (default 1.0, required), and a stored, recursive `factor` ("Absolute Quantity", compute `_compute_factor`). `_parent_name = 'relative_uom_id'` and `_parent_store = True` (lines 18-22). `_factor_gt_zero` is a database CHECK (46-49).

**uom/models/uom_uom.py:62-75**

```python
   62      def _compute_rounding(self):
   63          """ All Units of Measure share the same rounding precision defined in 'Product Unit'.
   64              Set in a compute to ensure compatibility with previous calls to `uom.rounding`.
   65          """
   66          decimal_precision = self.env['decimal.precision'].precision_get('Product Unit')
   67          self.rounding = 10 ** -decimal_precision
   68  
   69      @api.depends('relative_factor', 'relative_uom_id', 'relative_uom_id.factor')
   70      def _compute_factor(self):
   71          for uom in self:
   72              if uom.relative_uom_id:
   73                  uom.factor = uom.relative_factor * uom.relative_uom_id.factor
   74              else:
   75                  uom.factor = uom.relative_factor
```

**uom/models/uom_uom.py:97-101**

```python
   97      @api.constrains('relative_factor', 'relative_uom_id')
   98      def _check_factor(self):
   99          for uom in self:
  100              if not uom.relative_uom_id and uom.relative_factor != 1.0:
  101                  raise UserError(_("Reference unit of measure is missing."))
```

- `_check_factor` (97-101) raises "Reference unit of measure is missing." when a unit has no reference but `relative_factor` is not 1.0.

**uom/models/uom_uom.py:24-32**

```python
   24      def _unprotected_uom_xml_ids(self):
   25          """ Return a list of UoM XML IDs that are not protected by default.
   26          Note: Some of these may be protected via overrides in other modules.
   27          """
   28          return [
   29              "product_uom_hour",
   30              "product_uom_dozen",
   31              "product_uom_pack_6",
   32          ]
```

**uom/models/uom_uom.py:79-112**

```python
   79      @api.onchange('relative_factor')
   80      def _onchange_critical_fields(self):
   81          if self._filter_protected_uoms() and self.create_date < (fields.Datetime.now() - timedelta(days=1)):
   82              return {
   83                  'warning': {
   84                      'title': _("Warning for %s", self.name),
   85                      'message': _(
   86                          "Some critical fields have been modified on %s.\n"
   87                          "Note that existing data WON'T be updated by this change.\n\n"
   88                          "As units of measure impact the whole system, this may cause critical issues.\n"
   89                          "Therefore, changing core units of measure in a running database is not recommended.",
   90                          self.name,
   91                      )
   92                  }
   93              }
   94  
   95      # === CONSTRAINT METHODS === #
   96  
   97      @api.constrains('relative_factor', 'relative_uom_id')
   98      def _check_factor(self):
   99          for uom in self:
  100              if not uom.relative_uom_id and uom.relative_factor != 1.0:
  101                  raise UserError(_("Reference unit of measure is missing."))
  102  
  103      # === CRUD METHODS === #
  104  
  105      @api.ondelete(at_uninstall=False)
  106      def _unlink_except_master_data(self):
  107          locked_uoms = self._filter_protected_uoms()
  108          if locked_uoms:
  109              raise UserError(_(
  110                  "The following units of measure are used by the system and cannot be deleted: %s\nYou can archive them instead.",
  111                  ", ".join(locked_uoms.mapped('name')),
  112              ))
```

**hr_timesheet/models/uom_uom.py:10-17**

```python
   10      def _unprotected_uom_xml_ids(self):
   11          # Override
   12          # When timesheet App is installed, we also need to protect the hour UoM
   13          # from deletion (and warn in case of modification)
   14          return [
   15              "product_uom_dozen",
   16              "product_uom_pack_6",
   17          ]
```

- Protected units: the base list of unprotected unit xml ids is hour, dozen and pack of six (uom/models/uom_uom.py:24-32). `_filter_protected_uoms` (205-216, section 4.4) treats every other unit that has an `ir.model.data` row in module `uom` as protected. Editing `relative_factor` on a protected unit older than one day returns a UI warning (79-93), and deleting a protected unit raises a UserError that says to archive it instead (105-112; the delete hook is declared with `at_uninstall=False`). With the timesheet addon installed, the override returns only dozen and pack of six (hr_timesheet/models/uom_uom.py:10-17), which makes the hour unit protected as well.

### 4.4 Rounding and conversion

- `rounding` is a non-stored compute (line 39). `_compute_rounding` (62-67) sets `10 ** -decimal_precision`; its docstring says all units share the rounding precision defined in "Product Unit".

**uom/models/uom_uom.py:116-137**

```python
  116      def round(self, value: float, rounding_method: RoundingMethod = 'HALF-UP') -> float:
  117          """Round the value using the 'Product Unit' precision"""
  118          self.ensure_one()
  119          digits = self.env['decimal.precision'].precision_get('Product Unit')
  120          return tools.float_round(value, precision_digits=digits, rounding_method=rounding_method)
  121  
  122      def compare(self, value1: float, value2: float) -> Literal[-1, 0, 1]:
  123          """Compare two measures after rounding them with the 'Product Unit' precision
  124  
  125          :param value1: origin value to compare
  126          :param value2: value to compare to
  127          :return: -1, 0 or 1, if ``value1`` is lower than, equal to, or greater than ``value2``.
  128          """
  129          self.ensure_one()
  130          digits = self.env['decimal.precision'].precision_get('Product Unit')
  131          return tools.float_compare(value1, value2, precision_digits=digits)
  132  
  133      def is_zero(self, value: float) -> bool:
  134          """Check if the value is zero after rounding with the 'Product Unit' precision"""
  135          self.ensure_one()
  136          digits = self.env['decimal.precision'].precision_get('Product Unit')
  137          return tools.float_is_zero(value, precision_digits=digits)
```

- `round`, `compare` and `is_zero` (116-137) read the 'Product Unit' decimal precision (lines 119, 130 and 136); none of them reads a per-unit rounding value.

**uom/models/uom_uom.py:147-176**

```python
  147      def _compute_quantity(
  148          self,
  149          qty: float,
  150          to_unit: Self,
  151          round: bool = True,
  152          rounding_method: RoundingMethod = 'UP',
  153          raise_if_failure: bool = True,
  154      ) -> float:
  155          """ Convert the given quantity from the current UoM `self` into a given one
  156              :param qty: the quantity to convert
  157              :param to_unit: the destination UomUom record (uom.uom)
  158              :param raise_if_failure: only if the conversion is not possible
  159                  - if true, raise an exception if the conversion is not possible (different UomUom category),
  160                  - otherwise, return the initial quantity
  161          """
  162          if not self or not qty:
  163              return qty
  164          self.ensure_one()
  165  
  166          if self == to_unit:
  167              amount = qty
  168          else:
  169              amount = qty * self.factor
  170              if to_unit:
  171                  amount = amount / to_unit.factor
  172  
  173          if to_unit and round:
  174              amount = tools.float_round(amount, precision_rounding=to_unit.rounding, rounding_method=rounding_method)
  175  
  176          return amount
```

- `_compute_quantity` (147-176): the signature defaults are `round=True`, `rounding_method='UP'` and `raise_if_failure=True` (lines 151-153). When `self == to_unit` the quantity is returned as is (166-167). Otherwise `amount = qty * self.factor` (line 169), divided by `to_unit.factor` when a target unit is given (170-171), then rounded with `to_unit.rounding` when `round` is true (173-174). The `raise_if_failure` parameter is not used in the body even though the docstring mentions a "different UomUom category". There is no category comparison.

**uom/models/uom_uom.py:178-203**

```python
  178      def _check_qty(self, product_qty, uom_id, rounding_method="HALF-UP"):
  179          """Check if product_qty in given uom is a multiple of the packaging qty.
  180          If not, rounding the product_qty to closest multiple of the packaging qty
  181          according to the rounding_method "UP", "HALF-UP or "DOWN".
  182          """
  183          self.ensure_one()
  184          packaging_qty = self._compute_quantity(1, uom_id)
  185          if self == uom_id:
  186              return product_qty
  187          # We do not use the modulo operator to check if qty is a mltiple of q. Indeed the quantity
  188          # per package might be a float, leading to incorrect results. For example:
  189          # 8 % 1.6 = 1.5999999999999996
  190          # 5.4 % 1.8 = 2.220446049250313e-16
  191          if product_qty and packaging_qty:
  192              product_qty = float_round(product_qty / packaging_qty, precision_rounding=1.0,
  193                                    rounding_method=rounding_method) * packaging_qty
  194          return product_qty
  195  
  196      def _compute_price(self, price: float, to_unit: Self) -> float:
  197          self.ensure_one()
  198          if not self or not price or not to_unit or self == to_unit:
  199              return price
  200          amount = price * to_unit.factor
  201          if to_unit:
  202              amount = amount / self.factor
  203          return amount
```

- `_check_qty` (178-194) rounds a quantity to a whole multiple of the packaging unit's quantity, taking `_compute_quantity(1, uom_id)` as that quantity (line 184) and returning the input unchanged when both units are the same (185-186); the default rounding method is HALF-UP (line 178). `_compute_price` (196-203) converts a price as `price * to_unit.factor / self.factor` and returns the price unchanged when `price` is falsy, `to_unit` is empty or the units are equal (198-199).

**uom/models/uom_uom.py:205-230**

```python
  205      def _filter_protected_uoms(self):
  206          """Verifies self does not contain protected uoms."""
  207          linked_model_data = self.env['ir.model.data'].sudo().search([
  208              ('model', '=', self._name),
  209              ('res_id', 'in', self.ids),
  210              ('module', '=', 'uom'),
  211              ('name', 'not in', self._unprotected_uom_xml_ids()),
  212          ])
  213          if not linked_model_data:
  214              return self.browse()
  215          else:
  216              return self.browse(set(linked_model_data.mapped('res_id')))
  217  
  218      def _has_common_reference(self, other_uom: Self) -> bool:
  219          """ Check if `self` and `other_uom` have a common reference unit """
  220          self.ensure_one()
  221          other_uom.ensure_one()
  222          self_path = self.parent_path.split('/')
  223          other_path = other_uom.parent_path.split('/')
  224          common_path = []
  225          for self_parent, other_parent in zip(self_path, other_path):
  226              if self_parent == other_parent:
  227                  common_path.append(self_parent)
  228              else:
  229                  break
  230          return bool(common_path)
```

- `_filter_protected_uoms` (205-216) returns the units of `self` that carry an `ir.model.data` row in module `uom` whose name is not in `_unprotected_uom_xml_ids()` (lines 207-212). It is used at uom/models/uom_uom.py:81 and 107. `_has_common_reference` (218-230) splits the `parent_path` of both units and is true when the first path segment is shared, so it tests for a common root unit. A search of Python files finds callers outside the uom addon, among them sale_timesheet/models/product_product.py:25, sale_timesheet/models/sale_order_line.py:49 and 100, stock/wizard/product_label_layout.py:60, stock/wizard/stock_lot_label_layout.py:33 and account_edi_ubl_cii/models/account_edi_common.py:976 and 1410.

### 4.5 Packagings and `product.uom`

**product/models/product_uom.py:8-26**

```python
    8  class ProductUom(models.Model):
    9      _name = 'product.uom'
   10      _description = 'Link between products and their UoMs'
   11      _rec_name = 'barcode'
   12  
   13      uom_id = fields.Many2one('uom.uom', 'Unit', required=True, index=True, ondelete='cascade')
   14      product_id = fields.Many2one('product.product', 'Product', required=True, index=True, ondelete='cascade')
   15      barcode = fields.Char(index='btree_not_null', required=True, copy=False)
   16      company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)
   17  
   18      _barcode_uniq = models.Constraint('unique(barcode)', 'A barcode can only be assigned to one packaging.')
   19  
   20      @api.constrains('barcode')
   21      def _check_barcode_uniqueness(self):
   22          """ With GS1 nomenclature, products and packagings use the same pattern. Therefore, we need
   23          to ensure the uniqueness between products' barcodes and packagings' ones"""
   24          domain = [('barcode', 'in', [b for b in self.mapped('barcode') if b])]
   25          if self.env['product.product'].search_count(domain, limit=1):
   26              raise ValidationError(_("A product already uses the barcode"))
```

**product/models/uom_uom.py:19**

```python
   19      product_uom_ids = fields.One2many('product.uom', 'uom_id', string='Barcodes', domain=_domain_product_uoms)
```

- `product.uom` (product/models/product_uom.py, 32 lines) has `uom_id`, `product_id`, `barcode` (required, index `btree_not_null`, `copy=False`) and `company_id`. `_barcode_uniq` is `unique(barcode)` (line 18); the Python cross-check at lines 20-26 raises "A product already uses the barcode". The variant exposes `product_uom_ids` (product/models/product_product.py:48) and `uom.uom` exposes `product_uom_ids` (product/models/uom_uom.py:19).

### 4.6 Guards on changing a product's unit

**product/models/product_template.py:585-589**

```python
  585      def write(self, vals):
  586          if 'uom_id' in vals:
  587              products = self.filtered(lambda template: template.uom_id.id != vals['uom_id']).product_variant_ids
  588              products.with_context(skip_uom_conversion=True)._update_uom(vals['uom_id'])
  589          res = super(ProductTemplate, self).write(vals)
```

**product/models/product_product.py:1197-1200**

```python
 1197      def _update_uom(self, to_uom_id):
 1198          """ Hook to handle an UoM modification. Avoid recomputation and just replace the
 1199          many2one field on the impacted models."""
 1200          return True
```

**stock/models/product.py:784-808**

```python
  784      def _update_uom(self, to_uom_id):
  785          for uom, product, moves in self.env['stock.move']._read_group(
  786              [('product_id', 'in', self.ids)],
  787              ['product_uom', 'product_id'],
  788              ['id:recordset'],
  789          ):
  790              if uom != product.product_tmpl_id.uom_id:
  791                  raise UserError(_('As other units of measure (ex : %(problem_uom)s) '
  792                  'than %(uom)s have already been used for this product, the change of unit of measure can not be done.'
  793                  'If you want to change it, please archive the product and create a new one.',
  794                  problem_uom=uom.name, uom=product.product_tmpl_id.uom_id.name))
  795              moves.product_uom = to_uom_id
  796  
  797          for uom, product, move_lines in self.env['stock.move.line']._read_group(
  798              [('product_id', 'in', self.ids)],
  799              ['product_uom_id', 'product_id'],
  800              ['id:recordset'],
  801          ):
  802              if uom != product.product_tmpl_id.uom_id:
  803                  raise UserError(_('As other units of measure (ex : %(problem_uom)s) '
  804                  'than %(uom)s have already been used for this product, the change of unit of measure can not be done.'
  805                  'If you want to change it, please archive the product and create a new one.',
  806                  problem_uom=uom.name, uom=product.product_tmpl_id.uom_id.name))
  807              move_lines.product_uom_id = to_uom_id
  808          return super()._update_uom(to_uom_id)
```

**purchase/models/product.py:117-132**

```python
  117      def _update_uom(self, to_uom_id):
  118          for uom, product, po_lines in self.env['purchase.order.line']._read_group(
  119              [('product_id', 'in', self.ids)],
  120              ['product_uom_id', 'product_id'],
  121              ['id:recordset'],
  122          ):
  123              if uom != product.product_tmpl_id.uom_id:
  124                  raise UserError(_(
  125                      'As other units of measure (ex : %(problem_uom)s) '
  126                      'than %(uom)s have already been used for this product, the change of unit of measure can not be done.'
  127                      'If you want to change it, please archive the product and create a new one.',
  128                      problem_uom=uom.display_name, uom=product.product_tmpl_id.uom_id.display_name))
  129              po_lines.product_uom_id = to_uom_id
  130              po_lines.flush_recordset()
  131  
  132          return super()._update_uom(to_uom_id)
```

**sale/models/product_product.py:101-114**

```python
  101      def _update_uom(self, to_uom_id):
  102          for uom, product, so_lines in self.env['sale.order.line']._read_group(
  103              [('product_id', 'in', self.ids)],
  104              ['product_uom_id', 'product_id'],
  105              ['id:recordset'],
  106          ):
  107              if so_lines.product_uom_id != product.product_tmpl_id.uom_id:
  108                  raise UserError(_(
  109                      'As other units of measure (ex : %(problem_uom)s) '
  110                      'than %(uom)s have already been used for this product, the change of unit of measure can not be done.'
  111                      'If you want to change it, please archive the product and create a new one.',
  112                      problem_uom=uom.display_name, uom=product.product_tmpl_id.uom_id.display_name))
  113              so_lines.product_uom_id = to_uom_id
  114          return super()._update_uom(to_uom_id)
```

**mrp/models/product.py:452-489**

```python
  452      def _update_uom(self, to_uom_id):
  453          for uom, product_template, boms in self.env['mrp.bom']._read_group(
  454              [('product_tmpl_id', 'in', self.product_tmpl_id.ids)],
  455              ['product_uom_id', 'product_tmpl_id'],
  456              ['id:recordset'],
  457          ):
  458              if product_template.uom_id != uom:
  459                  raise UserError(_('As other units of measure (ex : %(problem_uom)s) '
  460                  'than %(uom)s have already been used for this product, the change of unit of measure can not be done.'
  461                  'If you want to change it, please archive the product and create a new one.',
  462                  problem_uom=uom.name, uom=product_template.uom_id.name))
  463              boms.product_uom_id = to_uom_id
  464  
  465          for uom, product, bom_lines in self.env['mrp.bom.line']._read_group(
  466              [('product_id', 'in', self.ids)],
  467              ['product_uom_id', 'product_id'],
  468              ['id:recordset'],
  469          ):
  470              if product.product_tmpl_id.uom_id != uom:
  471                  raise UserError(_('As other units of measure (ex : %(problem_uom)s) '
  472                  'than %(uom)s have already been used for this product, the change of unit of measure can not be done.'
  473                  'If you want to change it, please archive the product and create a new one.',
  474                  problem_uom=uom.name, uom=product.product_tmpl_id.uom_id.name))
  475              bom_lines.product_uom_id = to_uom_id
  476  
  477          for uom, product, productions in self.env['mrp.production']._read_group(
  478              [('product_id', 'in', self.ids)],
  479              ['product_uom_id', 'product_id'],
  480              ['id:recordset'],
  481          ):
  482              if product.product_tmpl_id.uom_id != uom:
  483                  raise UserError(_('As other units of measure (ex : %(problem_uom)s) '
  484                  'than %(uom)s have already been used for this product, the change of unit of measure can not be done.'
  485                  'If you want to change it, please archive the product and create a new one.',
  486                  problem_uom=uom.name, uom=product.product_tmpl_id.uom_id.name))
  487              productions.product_uom_id = to_uom_id
  488  
  489          return super()._update_uom(to_uom_id)
```

**repair/models/product.py:34-47**

```python
   34      def _update_uom(self, to_uom_id):
   35          for uom, product, repairs in self.env['repair.order']._read_group(
   36              [('product_id', 'in', self.ids)],
   37              ['product_uom', 'product_id'],
   38              ['id:recordset'],
   39          ):
   40              if uom != product.product_tmpl_id.uom_id:
   41                  raise UserError(_(
   42                  'As other units of measure (ex : %(problem_uom)s) '
   43                  'than %(uom)s have already been used for this product, the change of unit of measure can not be done.'
   44                  'If you want to change it, please archive the product and create a new one.',
   45                  problem_uom=uom.display_name, uom=product.product_tmpl_id.uom_id.display_name))
   46              repairs.product_uom = to_uom_id
   47          return super()._update_uom(to_uom_id)
```

- A search for `def _update_uom` over all Python files returns exactly six definitions: product/models/product_product.py:1197 (base hook, returns true, lines 1197-1200), stock/models/product.py:784, purchase/models/product.py:117, sale/models/product_product.py:101, mrp/models/product.py:452 and repair/models/product.py:34. The template write (product/models/product_template.py:585-589) collects the variants of the templates whose current `uom_id` differs from the written value (line 587) and calls the hook on them with the context flag `skip_uom_conversion=True` (line 588) before `super().write` (line 589), so each override sees the template's current (old) unit. Each override reads the usage records of its own addon, raises the same UserError ("As other units of measure (ex : %(problem_uom)s) than %(uom)s have already been used for this product, the change of unit of measure can not be done. ...") when a record uses a unit other than the template's current one, rewrites the usage records to the new unit otherwise, and then calls `super()`.
- `skip_uom_conversion` context consumers found by search: purchase/models/purchase_order_line.py:422 (the price, planned date and name recompute skips the line), stock/models/stock_move.py:853 (a `product_uom` write on a done move raises a UserError unless the flag is set) and stock/models/stock_move_line.py:454 (the loop that gathers trigger fields into `updates` skips every key when the flag is set).

**account/models/product.py:131-150**

```python
  131      @api.constrains('uom_id')
  132      def _check_uom_not_in_invoice(self):
  133          self.env['product.template'].flush_model(['uom_id'])
  134          self.env.cr.execute("""
  135              SELECT prod_template.id
  136                FROM account_move_line line
  137                JOIN product_product prod_variant ON line.product_id = prod_variant.id
  138                JOIN product_template prod_template ON prod_variant.product_tmpl_id = prod_template.id
  139                JOIN uom_uom template_uom ON prod_template.uom_id = template_uom.id
  140                JOIN uom_uom line_uom ON line.product_uom_id = line_uom.id
  141               WHERE prod_template.id IN %s
  142                 AND line.parent_state = 'posted'
  143                 AND template_uom.id != line_uom.id
  144               LIMIT 1
  145          """, [tuple(self.ids)])
  146          if self.env.cr.fetchall():
  147              raise ValidationError(_(
  148                  "This product is already being used in posted Journal Entries.\n"
  149                  "If you want to change its Unit of Measure, please archive this product and create a new one."
  150              ))
```

- account/models/product.py:131-150: `_check_uom_not_in_invoice` uses raw SQL against posted journal item lines.

**stock/models/product.py:1373-1404**

```python
 1373      def write(self, vals):
 1374          # Users can not update the factor if open stock moves are based on it
 1375          keys_to_protect = {'factor', 'relative_factor', 'relative_uom_id'}
 1376          if any(key in vals for key in keys_to_protect):
 1377              changed = self.filtered(
 1378                  lambda u: any(
 1379                      f in vals and u[f] != vals[f]
 1380                      for f in ('factor', 'relative_factor')
 1381                  ) or ('relative_uom_id' in vals and u.relative_uom_id.id != int(vals['relative_uom_id']))
 1382              )
 1383              if changed:
 1384                  error_msg = _(
 1385                      "You cannot change the ratio of this unit of measure"
 1386                      " as some products with this UoM have already been moved"
 1387                      " or are currently reserved."
 1388                  )
 1389                  if self.env['stock.move'].sudo().search_count([
 1390                      ('product_uom', 'in', changed.ids),
 1391                      ('state', 'not in', ('cancel', 'done'))
 1392                  ]):
 1393                      raise UserError(error_msg)
 1394                  if self.env['stock.move.line'].sudo().search_count([
 1395                      ('product_uom_id', 'in', changed.ids),
 1396                      ('state', 'not in', ('cancel', 'done')),
 1397                  ]):
 1398                      raise UserError(error_msg)
 1399                  if self.env['stock.quant'].sudo().search_count([
 1400                      ('product_id.product_tmpl_id.uom_id', 'in', changed.ids),
 1401                      ('quantity', '!=', 0),
 1402                  ]):
 1403                      raise UserError(error_msg)
 1404          return super().write(vals)
```

**stock/models/product.py:1406-1418**

```python
 1406      def _adjust_uom_quantities(self, qty, quant_uom):
 1407          """ This method adjust the quantities of a procurement if its UoM isn't the same
 1408          as the one of the quant and the parameter 'propagate_uom' is not set.
 1409          """
 1410          procurement_uom = self
 1411          computed_qty = qty
 1412          get_param = self.env['ir.config_parameter'].sudo().get_param
 1413          if get_param('stock.propagate_uom') != '1':
 1414              computed_qty = self._compute_quantity(qty, quant_uom, rounding_method='HALF-UP')
 1415              procurement_uom = quant_uom
 1416          else:
 1417              computed_qty = self._compute_quantity(qty, procurement_uom, rounding_method='HALF-UP')
 1418          return (computed_qty, procurement_uom)
```

- stock/models/product.py:1373-1404: the stock `uom.uom` write guard reacts only when a written `factor`, `relative_factor` or `relative_uom_id` value differs from the stored one (keys at 1375-1376, comparison at 1377-1382). For the changed units it raises one UserError ("You cannot change the ratio of this unit of measure as some products with this UoM have already been moved or are currently reserved.") when any of three searches finds a record: (1) a `stock.move` whose `product_uom` is one of the changed units and whose `state` is not `cancel` or `done` (1389-1393); (2) a `stock.move.line` whose `product_uom_id` is one of the changed units and whose `state` is not `cancel` or `done` (1394-1398); (3) a `stock.quant` with `quantity` different from zero whose `product_id.product_tmpl_id.uom_id` is one of the changed units (1399-1403). Lines 1406-1418: `stock.propagate_uom` is read in `_adjust_uom_quantities`.

### 4.7 Unit-change warnings (UI)

**product/models/product_template.py:474-487**

```python
  474      @api.onchange('uom_id')
  475      def _onchange_uom_id(self):
  476          if self._origin.uom_id == self.uom_id or not self.with_context(active_test=False).product_variant_ids._trigger_uom_warning():
  477              return
  478          message = _(
  479              'Changing the unit of measure for your product will apply a conversion 1 %(old_uom_name)s = 1 %(new_uom_name)s.\n'
  480              'All existing records (Sales orders, Purchase orders, etc.) using this product will be updated by replacing the unit name.',
  481              old_uom_name=self._origin.uom_id.display_name, new_uom_name=self.uom_id.display_name)
  482          return {
  483              'warning': {
  484                  'title': _('What to expect ?'),
  485                  'message': message,
  486              }
  487          }
```

**product/models/product_product.py:422-423**

```python
  422      def _trigger_uom_warning(self):
  423          return False
```

- Template onchange (474-487): when the unit changes and `_trigger_uom_warning` is true for any variant (including archived ones, line 476), it warns that a conversion 1 old unit = 1 new unit will be applied and that existing records using the product will be updated by replacing the unit name.
- `_trigger_uom_warning` has four definitions found by search: the base returns false (product/models/product_product.py:422-423); stock returns true when any stock move exists for the product (stock/models/product.py:821-828); purchase returns true when any purchase order line exists (purchase/models/product.py:134-141); sale returns true when any sale order line exists (sale/models/product_product.py:116-123). Each override returns the `super()` result first when it is truthy.

---

## 5. Prices, category and valuation fields

### 5.1 Prices

**product/models/product_template.py:93-106**

```python
   93      # list_price: catalog price, user defined
   94      list_price = fields.Float(
   95          'Sales Price', default=1.0,
   96          min_display_digits='Product Price',
   97          tracking=True,
   98          help="Price at which the product is sold to customers.",
   99      )
  100      standard_price = fields.Float(
  101          'Cost', compute='_compute_standard_price',
  102          inverse='_set_standard_price', search='_search_standard_price',
  103          min_display_digits='Product Price', groups="base.group_user",
  104          help="""Value of the product (automatically computed in AVCO).
  105          Used to value the product when the purchase cost is not known (e.g. inventory adjustment).
  106          Used to compute margins on sale orders.""")
```

**product/models/product_product.py:62-68**

```python
   62      standard_price = fields.Float(
   63          'Cost', company_dependent=True,
   64          min_display_digits='Product Price',
   65          groups="base.group_user",
   66          help="""Value of the product (automatically computed in AVCO).
   67          Used to value the product when the purchase cost is not known (e.g. inventory adjustment).
   68          Used to compute margins on sale orders.""")
```

- Template `standard_price` (product/models/product_template.py:100-106) is a non-stored float with compute, inverse and search (`_compute_standard_price`, `_set_standard_price`, `_search_standard_price`; lines 310-321). The variant field (product/models/product_product.py:62-68) is the company-dependent one (line 63, `company_dependent=True`). The proxy methods are `_compute_template_field_from_variant_field` (269-290) and `_set_product_variant_field` (292-308), cited again in section 9.
- `list_price` (template lines 94-99): default 1.0, tracked.

**product/models/product_product.py:308-335**

```python
  308      @api.onchange('lst_price')
  309      def _set_product_lst_price(self):
  310          for product in self:
  311              if self.env.context.get('uom'):
  312                  value = self.env['uom.uom'].browse(self.env.context['uom'])._compute_price(product.lst_price, product.uom_id)
  313              else:
  314                  value = product.lst_price
  315              value -= product.price_extra
  316              product.write({'list_price': value})
  317  
  318      @api.depends("product_template_attribute_value_ids.price_extra")
  319      def _compute_product_price_extra(self):
  320          for product in self:
  321              product.price_extra = sum(product.product_template_attribute_value_ids.mapped('price_extra'))
  322  
  323      @api.depends('list_price', 'price_extra')
  324      @api.depends_context('uom')
  325      def _compute_product_lst_price(self):
  326          to_uom = None
  327          if 'uom' in self.env.context:
  328              to_uom = self.env['uom.uom'].browse(self.env.context['uom'])
  329  
  330          for product in self:
  331              if to_uom:
  332                  list_price = product.uom_id._compute_price(product.list_price, to_uom)
  333              else:
  334                  list_price = product.list_price
  335              product.lst_price = list_price + product.price_extra
```

- Variant `lst_price` (product/models/product_product.py:30-33, string "Sales Price") declares `compute='_compute_product_lst_price'` and `inverse='_set_product_lst_price'` (line 32). The compute (323-335) depends on `list_price` and `price_extra`; when a `uom` key is present in the context it converts `list_price` from the product's unit to that unit (line 332), and it returns that price plus `price_extra` (line 335). `_set_product_lst_price` (308-316) is both the inverse and an `@api.onchange('lst_price')` handler (decorator at line 308): it converts from the context unit when one is set (line 312), subtracts `price_extra` (line 315) and writes the result to `list_price` (line 316).

**product/models/product_product.py:402-405**

```python
  402      @api.onchange('standard_price')
  403      def _onchange_standard_price(self):
  404          if self.standard_price < 0:
  405              raise ValidationError(_("The cost of a product can't be negative."))
```

**product/models/product_template.py:417-420**

```python
  417      @api.onchange('standard_price')
  418      def _onchange_standard_price(self):
  419          if self.standard_price < 0:
  420              raise ValidationError(_("The cost of a product can't be negative."))
```

- Negative cost is rejected with "The cost of a product can't be negative." (variant 402-405; template 417-420), as an onchange check.

### 5.2 Category

**product/models/product_template.py:81-86**

```python
   81      categ_id = fields.Many2one(
   82          string="Product Category",
   83          comodel_name='product.category',
   84          group_expand='_read_group_categ_id',
   85          tracking=True,
   86      )
```

**product/models/product_category.py:8-23**

```python
    8  class ProductCategory(models.Model):
    9      _name = 'product.category'
   10      _inherit = ['mail.thread']
   11      _description = "Product Category"
   12      _parent_name = "parent_id"
   13      _parent_store = True
   14      _rec_name = 'complete_name'
   15      _order = 'complete_name'
   16  
   17      name = fields.Char('Name', index='trigram', required=True)
   18      complete_name = fields.Char(
   19          'Complete Name', compute='_compute_complete_name', recursive=True,
   20          store=True)
   21      parent_id = fields.Many2one('product.category', 'Parent Category', index=True, ondelete='cascade')
   22      parent_path = fields.Char(index=True)
   23      child_id = fields.One2many('product.category', 'parent_id', 'Child Categories')
```

**product/models/product_category.py:46-49**

```python
   46      @api.constrains('parent_id')
   47      def _check_category_recursion(self):
   48          if self._has_cycle():
   49              raise ValidationError(_('You cannot create recursive categories.'))
```

- `categ_id` (product/models/product_template.py:81-86) is a many-to-one to `product.category` (line 83), with `group_expand` and tracking. It is not marked required. `product.category` is a parent-stored hierarchy (`_parent_name = 'parent_id'`, `_parent_store = True`, `_rec_name = 'complete_name'`, `_order = 'complete_name'`) with a recursion constraint (lines 8-23, 46-49).

### 5.3 Valuation fields (stock_account)

**stock_account/models/product.py:14-30**

```python
   14      cost_method = fields.Selection(
   15          string="Cost Method",
   16          selection=[
   17              ('standard', "Standard Price"),
   18              ('fifo', "First In First Out (FIFO)"),
   19              ('average', "Average Cost (AVCO)"),
   20          ],
   21          compute='_compute_cost_method',
   22      )
   23      valuation = fields.Selection(
   24          string="Valuation",
   25          selection=[
   26              ('periodic', 'Periodic (at closing)'),
   27              ('real_time', 'Perpetual (at invoicing)'),
   28          ],
   29          compute='_compute_valuation', search='_search_valuation',
   30      )
```

**stock_account/models/product.py:36-40**

```python
   36      # TODO remove in master
   37      property_price_difference_account_id = fields.Many2one(
   38          'account.account', 'Price Difference Account', company_dependent=True, ondelete='restrict',
   39          check_company=True,
   40          help="""With perpetual valuation, this account will hold the price difference between the standard price and the bill price.""")
```

**stock_account/models/product.py:42-79**

```python
   42      def _search_valuation(self, operator, value):
   43          if operator != '=':
   44              raise UserError(self.env._("You can only use the '=' operator to search on valuation field."))
   45          if value not in ['periodic', 'real_time']:
   46              raise UserError(self.env._("Only the value 'periodic' and 'real_time' are accepted to search on valuation field."))
   47          domain_categ = Domain([('categ_id.property_valuation', operator, value)])
   48          domain_company = Domain(['|', ('categ_id.property_valuation', '=', False), ('categ_id', '=', False), ('company_id.inventory_valuation', operator, value)])
   49  
   50          if self.env.company.inventory_valuation and self.env.company.inventory_valuation == value:
   51              domain_company = Domain(['|', ('categ_id.property_valuation', '=', False), ('categ_id', '=', False), '|', ('company_id.inventory_valuation', operator, value), ('company_id', '=', False)])
   52          return domain_company | domain_categ
   53  
   54      @api.depends('tracking')
   55      def _compute_lot_valuated(self):
   56          for product in self:
   57              if product.tracking == 'none':
   58                  product.lot_valuated = False
   59  
   60      @api.depends_context('company')
   61      @api.depends('categ_id.property_cost_method')
   62      def _compute_cost_method(self):
   63          for product_template in self:
   64              company = product_template.company_id
   65              if not company or self.env.company.filtered_domain([('id', 'child_of', company.id)]):
   66                  company = self.env.company
   67              product_template.cost_method = (
   68                  product_template.categ_id.with_company(company).property_cost_method
   69                  or company.cost_method
   70              )
   71  
   72      @api.depends_context('company')
   73      @api.depends('categ_id.property_valuation')
   74      def _compute_valuation(self):
   75          for product_template in self:
   76              company = product_template.company_id
   77              if not company or self.env.company.filtered_domain([('id', 'child_of', company.id)]):
   78                  company = self.env.company
   79              product_template.valuation = product_template.categ_id.with_company(company).property_valuation or company.inventory_valuation
```

**stock_account/models/product.py:725-755**

```python
  725  class ProductCategory(models.Model):
  726      _inherit = 'product.category'
  727  
  728      anglo_saxon_accounting = fields.Boolean(
  729          string="Use Anglo-Saxon Accounting", compute="_compute_anglo_saxon_accounting",
  730          help="If checked, the product will be valued using the Anglo-Saxon accounting method.")
  731      property_valuation = fields.Selection(
  732          string="Inventory Valuation",
  733          selection=[
  734              ('periodic', 'Periodic (at closing)'),
  735              ('real_time', 'Perpetual (at invoicing)'),
  736          ],
  737          company_dependent=True, copy=True, tracking=True,
  738          help="""Periodic: The accounting entries are suggested manually in the inventory valuation report.
  739          Perpetual: An accounting entry is automatically created to value the inventory when a product is billed or invoiced.
  740          """)
  741      property_cost_method = fields.Selection(
  742          string="Costing Method",
  743          selection=[
  744              ('standard', "Standard Price"),
  745              ('fifo', "First In First Out (FIFO)"),
  746              ('average', "Average Cost (AVCO)"),
  747          ],
  748          company_dependent=True, copy=True,
  749          default=lambda self: self.env.company.cost_method,
  750          help="""Standard Price: The products are valued at their standard cost defined on the product.
  751          Average Cost (AVCO): The products are valued at weighted average cost.
  752          First In First Out (FIFO): The products are valued supposing those that enter the company first will also leave it first.
  753          """,
  754          tracking=True,
  755      )
```

- stock_account/models/product.py:14-30: template `cost_method` (values standard, fifo, average) and `valuation` (values periodic, real_time; labels "Periodic (at closing)" and "Perpetual (at invoicing)") are computed without `store`, so they are not stored. `valuation` also has a search method.
- `_compute_cost_method` (lines 60-70; depends on `categ_id.property_cost_method` and on the company context) and `_compute_valuation` (lines 72-79; same pattern with `property_valuation`) read the category property under a company chosen at lines 64-66 / 76-78 (the current company when the template has none or the current company lies within the template company; otherwise the template company). They fall back to the company's `cost_method` and `inventory_valuation` when the category value is empty.
- `_search_valuation` (lines 42-52) accepts only the `=` operator and only the values `periodic` and `real_time`, and raises a UserError otherwise (lines 43-46); it combines a category-property domain with a company-fallback domain (lines 47-52).
- Category side (stock_account/models/product.py:725-755): `property_valuation` (731-740) and `property_cost_method` (741-755) are company-dependent, copied, tracked selections; `property_cost_method` defaults to the company's `cost_method` (line 749).
- `property_price_difference_account_id` on the template carries the comment `# TODO remove in master` (lines 36-40). Legacy value names of these selections were not verified in this tree.

---

## 6. Tax fields

**account/models/product.py:40-52**

```python
   40      taxes_id = fields.Many2many('account.tax', 'product_taxes_rel', 'prod_id', 'tax_id',
   41          string="Sales Taxes",
   42          help="Default taxes used when selling the product",
   43          domain=[('type_tax_use', '=', 'sale')],
   44          default=lambda self: self.env.companies.account_sale_tax_id or self.env.companies.root_id.sudo().account_sale_tax_id,
   45      )
   46      tax_string = fields.Char(compute='_compute_tax_string')
   47      supplier_taxes_id = fields.Many2many('account.tax', 'product_supplier_taxes_rel', 'prod_id', 'tax_id',
   48          string="Purchase Taxes",
   49          help="Default taxes used when buying the product",
   50          domain=[('type_tax_use', '=', 'purchase')],
   51          default=lambda self: self.env.companies.account_purchase_tax_id or self.env.companies.root_id.sudo().account_purchase_tax_id,
   52      )
```

**account/models/product.py:107-111**

```python
  107      @api.depends('taxes_id', 'list_price')
  108      @api.depends_context('company')
  109      def _compute_tax_string(self):
  110          for record in self:
  111              record.tax_string = record._construct_tax_string(record.list_price)
```

**account/models/product.py:159-193**

```python
  159      def _force_default_sale_tax(self, companies):
  160          default_customer_taxes = companies.filtered('account_sale_tax_id').account_sale_tax_id
  161          if not default_customer_taxes:
  162              return
  163          links = [Command.link(t.id) for t in default_customer_taxes]
  164          for sub_ids in split_every(self.env.cr.IN_MAX, self.ids):
  165              chunk = self.browse(sub_ids)
  166              chunk.write({'taxes_id': links})
  167              chunk.invalidate_recordset(['taxes_id'])
  168  
  169      def _force_default_purchase_tax(self, companies):
  170          default_supplier_taxes = companies.filtered('account_purchase_tax_id').account_purchase_tax_id
  171          if not default_supplier_taxes:
  172              return
  173          links = [Command.link(t.id) for t in default_supplier_taxes]
  174          for sub_ids in split_every(self.env.cr.IN_MAX, self.ids):
  175              chunk = self.browse(sub_ids)
  176              chunk.write({'supplier_taxes_id': links})
  177              chunk.invalidate_recordset(['supplier_taxes_id'])
  178  
  179      def _force_default_tax(self, companies):
  180          self._force_default_sale_tax(companies)
  181          self._force_default_purchase_tax(companies)
  182  
  183      @api.model_create_multi
  184      def create(self, vals_list):
  185          products = super().create(vals_list)
  186          # If no company was set for the product, the product will be available for all companies and therefore should
  187          # have the default taxes of the other companies as well. sudo() is used since we're going to need to fetch all
  188          # the other companies default taxes which the user may not have access to.
  189          other_companies = self.env['res.company'].sudo().search(['!', ('id', 'child_of', self.env.companies.ids)])
  190          if other_companies and products:
  191              products_without_company = products.filtered(lambda p: not p.company_id).sudo()
  192              products_without_company._force_default_tax(other_companies)
  193          return products
```

- Exact names in v19: `taxes_id` ("Sales Taxes", relation table `product_taxes_rel`) and `supplier_taxes_id` ("Purchase Taxes", relation table `product_supplier_taxes_rel`; line 47), both plain many-to-many fields, not company-dependent, with defaults taken from the company's `account_sale_tax_id` and `account_purchase_tax_id` (account/models/product.py:40-52). The names are unchanged relative to the unit-scope baseline (baseline not verified here).
- `_compute_tax_string` (107-111), the `_force_default_*` helpers (159-181) and `create` (183-193) apply the default taxes. The combo onchange that clears both fields is at account/models/product.py:152-157 (section 1.3).

---

## 7. `sale_ok`, `purchase_ok`, `active`, `barcode`, `default_code`

### 7.1 Flags

- `sale_ok` default true (product/models/product_template.py:116); `purchase_ok` default true, stored, `readonly=False`, with a no-op compute (line 117; method at 202-203); `active` default true (line 129). Variant `active` is at product/models/product_product.py:39-41.

**product/models/product_template.py:129**

```python
  129      active = fields.Boolean('Active', default=True, help="If unchecked, it will allow you to hide the product without removing it.")
```

**sale/models/product_template.py:108-132**

```python
  108      @api.constrains('company_id')
  109      def _check_sale_product_company(self):
  110          """Ensure the product is not being restricted to a single company while
  111          having been sold in another one in the past, as this could cause issues."""
  112          products_by_compagny = defaultdict(lambda: self.env['product.template'])
  113          for product in self:
  114              if not product.product_variant_ids or not product.company_id:
  115                  # No need to check if the product has just being created (`product_variant_ids` is
  116                  # still empty) or if we're writing `False` on its company (should always work.)
  117                  continue
  118              products_by_compagny[product.company_id] |= product
  119  
  120          for target_company, products in products_by_compagny.items():
  121              subquery_products = self.env['product.product'].sudo().with_context(active_test=False)._search([('product_tmpl_id', 'in', products.ids)])
  122              so_lines = self.env['sale.order.line'].sudo().search_read(
  123                  [('product_id', 'in', subquery_products), '!', ('company_id', 'child_of', target_company.id)],
  124                  fields=['id', 'product_id'])
  125              if so_lines:
  126                  used_products = [sol['product_id'][1] for sol in so_lines]
  127                  raise ValidationError(_('The following products cannot be restricted to the company'
  128                                          ' %(company)s because they have already been used in quotations or '
  129                                          'sales orders in another company:\n%(used_products)s\n'
  130                                          'You can archive these products and recreate them '
  131                                          'with your company restriction instead, or leave them as '
  132                                          'shared product.', company=target_company.name, used_products=', '.join(used_products)))
```

- sale/models/product_template.py:108-132 holds the sale-side product company check (`_check_sale_product_company`).

### 7.2 Barcode

**product/models/product_product.py:30-48**

```python
   30      lst_price = fields.Float(
   31          'Sales Price', compute='_compute_product_lst_price',
   32          min_display_digits='Product Price', inverse='_set_product_lst_price',
   33          help="The sale price is managed from the product template. Click on the 'Configure Variants' button to set the extra attribute prices.")
   34  
   35      default_code = fields.Char('Internal Reference', index=True)
   36      code = fields.Char('Reference', compute='_compute_product_code')
   37      partner_ref = fields.Char('Customer Ref', compute='_compute_partner_ref')
   38  
   39      active = fields.Boolean(
   40          'Active', default=True,
   41          help="If unchecked, it will allow you to hide the product without removing it.")
   42      product_tmpl_id = fields.Many2one(
   43          'product.template', 'Product Template',
   44          bypass_search_access=True, index=True, ondelete="cascade", required=True)
   45      barcode = fields.Char(
   46          'Barcode', copy=False, index='btree_not_null',
   47          help="International Article Number used for product identification.")
   48      product_uom_ids = fields.One2many('product.uom', 'product_id', 'Unit Barcode', store=True)
```

**product/models/product_product.py:246-290**

```python
  246      def _get_barcodes_by_company(self):
  247          return [
  248              (company_id, [p.barcode for p in products if p.barcode])
  249              for company_id, products in groupby(self, lambda p: p.company_id.id)
  250          ]
  251  
  252      def _get_barcode_search_domain(self, barcodes_within_company, company_id):
  253          domain = [('barcode', 'in', barcodes_within_company)]
  254          if company_id:
  255              domain.append(('company_id', 'in', (False, company_id)))
  256          return domain
  257  
  258      def _check_duplicated_product_barcodes(self, barcodes_within_company, company_id):
  259          domain = self._get_barcode_search_domain(barcodes_within_company, company_id)
  260          products_by_barcode = self.sudo()._read_group(
  261              domain, ['barcode'], ['id:recordset'], having=[('__count', '>', 1)],
  262          )
  263  
  264          duplicates_as_str = "\n".join(
  265              self.env._(
  266                  "- Barcode \"%(barcode)s\" already assigned to product(s): %(product_list)s",
  267                  barcode=barcode, product_list=duplicate_products._filtered_access('read').mapped('display_name'),
  268              )
  269              for barcode, duplicate_products in products_by_barcode
  270          )
  271          if duplicates_as_str:
  272              duplicates_as_str += _(
  273                  "\n\nNote: products that you don't have access to will not be shown above."
  274              )
  275              raise ValidationError(_("Barcode(s) already assigned:\n\n%s", duplicates_as_str))
  276  
  277      def _check_duplicated_packaging_barcodes(self, barcodes_within_company, company_id):
  278          packaging_domain = self._get_barcode_search_domain(barcodes_within_company, company_id)
  279          if self.env['product.uom'].sudo().search_count(packaging_domain, limit=1):
  280              raise ValidationError(_("A packaging already uses the barcode"))
  281  
  282      @api.constrains('barcode')
  283      def _check_barcode_uniqueness(self):
  284          """ With GS1 nomenclature, products and packagings use the same pattern. Therefore, we need
  285          to ensure the uniqueness between products' barcodes and packagings' ones"""
  286          # Barcodes should only be unique within a company
  287          self_ctx = self.with_context(skip_preprocess_gs1=True)
  288          for company_id, barcodes_within_company in self_ctx._get_barcodes_by_company():
  289              self_ctx._check_duplicated_product_barcodes(barcodes_within_company, company_id)
  290              self_ctx._check_duplicated_packaging_barcodes(barcodes_within_company, company_id)
```

- Variant barcode field (product/models/product_product.py:45-47): `copy=False`, `index='btree_not_null'`; there is no database-level unique constraint on it.
- Uniqueness is a Python constraint: `_check_barcode_uniqueness` on the variant (lines 282-290, `def` at 283; helper methods at 246-280). It groups by company; the search domain adds `company_id in (False, company_id)` only when the company is set. It raises "Barcode(s) already assigned" and cross-checks `product.uom` barcodes.

**product/models/product_template.py:251-254**

```python
  251      @api.constrains('company_id')
  252      def _check_barcode_uniqueness(self):
  253          for template in self:
  254              template.product_variant_ids._check_barcode_uniqueness()
```

**product/models/product_template.py:340-351**

```python
  340      @api.depends('product_variant_ids.barcode')
  341      def _compute_barcode(self):
  342          self._compute_template_field_from_variant_field('barcode')
  343  
  344      def _search_barcode(self, operator, value):
  345          subquery = self.with_context(active_test=False)._search([
  346              ('product_variant_ids.barcode', operator, value),
  347          ])
  348          return [('id', 'in', subquery)]
  349  
  350      def _set_barcode(self):
  351          self._set_product_variant_field('barcode')
```

- The template re-runs the variant check when `company_id` changes (product/models/product_template.py:251-254). Template barcode is a proxy field (field line 152; compute/search/inverse 340-351).

### 7.3 Internal reference (`default_code`)

**product/models/product_product.py:407-420**

```python
  407      @api.onchange('default_code')
  408      def _onchange_default_code(self):
  409          if not self.default_code:
  410              return
  411  
  412          domain = [('default_code', '=', self.default_code)]
  413          if self.id.origin:
  414              domain.append(('id', '!=', self.id.origin))
  415  
  416          if self.env['product.product'].search_count(domain, limit=1):
  417              return {'warning': {
  418                  'title': _("Note:"),
  419                  'message': _("The Reference '%s' already exists.", self.default_code),
  420              }}
```

**product/models/product_template.py:422-442**

```python
  422      @api.onchange('default_code')
  423      def _onchange_default_code(self):
  424          if not self.default_code:
  425              return
  426  
  427          domain = [('default_code', '=', self.default_code)]
  428          if self.id.origin:
  429              domain.append(('id', '!=', self.id.origin))
  430  
  431          if self.env['product.template'].search_count(domain, limit=1):
  432              return {'warning': {
  433                  'title': _("Note:"),
  434                  'message': _("The Internal Reference '%s' already exists.", self.default_code),
  435              }}
  436  
  437      @api.depends('product_variant_ids.default_code')
  438      def _compute_default_code(self):
  439          self._compute_template_field_from_variant_field('default_code')
  440  
  441      def _set_default_code(self):
  442          self._set_product_variant_field('default_code')
```

- No uniqueness constraint on `default_code` exists anywhere in the tree. A search found only a test string (website_sale/tests/test_fuzzy.py:42). The only guards are onchange warnings: template "The Internal Reference '%s' already exists." (product/models/product_template.py:422-435) and variant "The Reference '%s' already exists." (product/models/product_product.py:407-420). Template field: lines 153-155 (stored compute with inverse); variant field line 35, `index=True`.

### 7.4 Variant uniqueness

**product/models/product_product.py:121**

```python
  121      _combination_unique = models.UniqueIndex("(product_tmpl_id, combination_indices) WHERE active IS TRUE")
```

- Only one ACTIVE variant may exist per attribute combination on a template (partial unique index, product/models/product_product.py:121). Variant explosion itself is covered by the earlier unit U112.

---

## 8. Policy fields: `invoice_policy`, `expense_policy`, `service_type`, `purchase_method`, `service_tracking`

### 8.1 Sale layer

**sale/models/product_template.py:14-47**

```python
   14      service_type = fields.Selection(
   15          selection=[('manual', "Manually set quantities on order")],
   16          string="Track Service",
   17          compute='_compute_service_type', store=True, readonly=False, precompute=True,
   18          help="Manually set quantities on order: Invoice based on the manually entered quantity, without creating an analytic account.\n"
   19               "Timesheets on contract: Invoice based on the tracked hours on the related timesheet.\n"
   20               "Create a task and track hours: Create a task on the sales order validation and track the work hours.")
   21      sale_line_warn_msg = fields.Text(string="Sales Order Line Warning")
   22      expense_policy = fields.Selection(
   23          selection=[
   24              ('no', "No"),
   25              ('cost', "At cost"),
   26              ('sales_price', "Sales price"),
   27          ],
   28          string="Re-Invoice Costs", default='no',
   29          compute='_compute_expense_policy', store=True, readonly=False,
   30          help="Validated expenses, vendor bills, or stock pickings (set up to track costs) can be invoiced to the customer at either cost or sales price.")
   31      visible_expense_policy = fields.Boolean(
   32          string="Re-Invoice Policy visible", compute='_compute_visible_expense_policy')
   33      sales_count = fields.Float(
   34          string="Sold", compute='_compute_sales_count', digits='Product Unit')
   35      invoice_policy = fields.Selection(
   36          selection=[
   37              ('order', "Ordered quantities"),
   38              ('delivery', "Delivered quantities"),
   39          ],
   40          string="Invoicing Policy",
   41          compute='_compute_invoice_policy',
   42          precompute=True,
   43          store=True,
   44          readonly=False,
   45          tracking=True,
   46          help="Ordered Quantity: Invoice quantities ordered by the customer.\n"
   47               "Delivered Quantity: Invoice quantities delivered to the customer.")
```

**sale/models/product_template.py:88-91**

```python
   88      @api.depends('sale_ok')
   89      def _compute_service_tracking(self):
   90          super()._compute_service_tracking()
   91          self.filtered(lambda pt: not pt.sale_ok).service_tracking = 'no'
```

**sale/models/product_template.py:99-101**

```python
   99      @api.depends('sale_ok')
  100      def _compute_expense_policy(self):
  101          self.filtered(lambda t: not t.sale_ok).expense_policy = 'no'
```

**sale/models/product_template.py:158-164**

```python
  158      @api.depends('type')
  159      def _compute_service_type(self):
  160          self.filtered(lambda t: t.type == 'consu' or not t.service_type).service_type = 'manual'
  161  
  162      @api.depends('type')
  163      def _compute_invoice_policy(self):
  164          self.filtered(lambda t: t.type == 'consu' or not t.invoice_policy).invoice_policy = 'order'
```

- `service_type` (sale/models/product_template.py:14; default 'manual'), `expense_policy` (line 22; values 'no', 'cost', 'sales_price'; default 'no') and `invoice_policy` (line 35; values 'order', 'delivery') are declared in the SALE addon, not in product. Computes: `_compute_service_type` (158-160), `_compute_invoice_policy` (162-164), `_compute_expense_policy` (99-101, depends on `sale_ok`), `_compute_service_tracking` override (88-91).
- Sale settings carry the instance default:

**sale/wizard/res_config_settings.py:10-17**

```python
   10      default_invoice_policy = fields.Selection(
   11          selection=[
   12              ('order', "Invoice what is ordered"),
   13              ('delivery', "Invoice what is delivered")
   14          ],
   15          string="Invoicing Policy",
   16          default='order',
   17          default_model='product.template')
```

**sale_stock/models/product_template.py:10-18**

```python
   10      @api.depends('type')
   11      def _compute_expense_policy(self):
   12          super()._compute_expense_policy()
   13          self.filtered(lambda t: t.is_storable).expense_policy = 'no'
   14  
   15      @api.depends('type')
   16      def _compute_service_type(self):
   17          super()._compute_service_type()
   18          self.filtered(lambda t: t.is_storable).service_type = 'manual'
```

- sale/wizard/res_config_settings.py:10-17: `default_invoice_policy` defaults to 'order'. sale_stock/models/product_template.py:10-18 depends on `type` and filters on `is_storable` to force the policy fields to 'no' / 'manual'.

### 8.2 `service_type` and `service_tracking` extensions

**product/models/product_template.py:71-80**

```python
   71      service_tracking = fields.Selection(selection=[
   72              ('no', 'Nothing'),
   73          ],
   74          string="Create on Order",
   75          default="no",
   76          compute="_compute_service_tracking",
   77          required=True,
   78          store=True,
   79          readonly=False,
   80      )
```

**sale_project/models/product_template.py:22-32**

```python
   22      service_tracking = fields.Selection(
   23          selection_add=[
   24              ('task_global_project', 'Task'),
   25              ('task_in_project', 'Project & Task'),
   26              ('project_only', 'Project'),
   27          ], ondelete={
   28              'task_global_project': 'set default',
   29              'task_in_project': 'set default',
   30              'project_only': 'set default',
   31          },
   32      )
```

**partnership/models/product_template.py:9-11**

```python
    9      service_tracking = fields.Selection(
   10          selection_add=[('partnership', 'Membership / Partnership')], ondelete={'partnership': 'set default'}
   11      )
```

**event_product/models/product_template.py:7-9**

```python
    7      service_tracking = fields.Selection(selection_add=[
    8          ('event', 'Event Registration'),
    9      ], ondelete={'event': 'set default'})
```

**event_booth_sale/models/product_template.py:8-10**

```python
    8      service_tracking = fields.Selection(selection_add=[
    9          ('event_booth', 'Event Booth'),
   10      ], ondelete={'event_booth': 'set default'})
```

**website_sale_slides/models/product_template.py:10-12**

```python
   10      service_tracking = fields.Selection(selection_add=[
   11          ('course', 'Course Access'),
   12      ], ondelete={'course': 'set default'})
```

**repair/models/product.py:52-53**

```python
   52      service_tracking = fields.Selection(selection_add=[('repair', 'Repair Order')],
   53                                          ondelete={'repair': 'set default'})
```

**sale_project/models/product_template.py:45-47**

```python
   45      service_type = fields.Selection(selection_add=[
   46          ('milestones', 'Project Milestones'),
   47      ])
```

**sale_timesheet/models/product_template.py:17-19**

```python
   17      service_type = fields.Selection(selection_add=[
   18          ('timesheet', 'Timesheets on project (one fare per SO/Project)'),
   19      ], ondelete={'timesheet': 'set manual'})
```

- `service_tracking` is declared once with `selection=` in the product addon, offering only the value 'no' (product/models/product_template.py:71-80; compute 198-200). A search for single-line declarations of the field over all Python files lists six `selection_add` extensions: sale_project/models/product_template.py:22 (adds 'task_global_project', 'task_in_project', 'project_only'), partnership/models/product_template.py:9 ('partnership'), event_product/models/product_template.py:7 ('event'), event_booth_sale/models/product_template.py:8 ('event_booth'), website_sale_slides/models/product_template.py:10 ('course') and repair/models/product.py:52 ('repair'). Each extension carries an `ondelete` mapping of its value to 'set default'. A related mirror sits at sale/models/sale_order_line.py:308.
- `service_type` is extended by sale_project (value 'milestones', lines 45-47) and sale_timesheet (value 'timesheet', lines 17-19).

### 8.3 Purchase layer

**purchase/models/product.py:14-29**

```python
   14      purchase_method = fields.Selection([
   15          ('purchase', 'On ordered quantities'),
   16          ('receive', 'On received quantities'),
   17      ], string="Control Policy", compute='_compute_purchase_method', precompute=True, store=True, readonly=False,
   18          help="On ordered quantities: Control bills based on ordered quantities.\n"
   19              "On received quantities: Control bills based on received quantities.")
   20      purchase_line_warn_msg = fields.Text('Message for Purchase Order Line')
   21  
   22      @api.depends('type')
   23      def _compute_purchase_method(self):
   24          default_purchase_method = self.env['product.template'].default_get(['purchase_method']).get('purchase_method', 'receive')
   25          for product in self:
   26              if product.type == 'service':
   27                  product.purchase_method = 'purchase'
   28              else:
   29                  product.purchase_method = default_purchase_method
```

- purchase/models/product.py:14-19 declares `purchase_method` ('purchase' / 'receive'); the compute at 22-29 depends on `type`: services get 'purchase', everything else gets the default or 'receive'.
- A search for single-line field declarations (`name = fields.`) of `invoice_policy`, `expense_policy`, `service_type`, `purchase_method` and `service_tracking` over all Python files shows: in the product addon only `service_tracking`; `service_type`, `expense_policy` and `invoice_policy` on the template in the sale addon (lines 14, 22, 35); `purchase_method` in the purchase addon only (line 14). Other `invoice_policy` hits belong to other models: stock_delivery/models/delivery_carrier.py:19, delivery/models/delivery_carrier.py:60 and sale_timesheet/models/res_config_settings.py:10 (a settings Boolean).

---

## 9. Template and variant propagation, archive behaviour

(Variant explosion is covered by U112; only the write and archive paths are cited here.)

**product/models/product_template.py:144-155**

```python
  144      product_variant_ids = fields.One2many('product.product', 'product_tmpl_id', 'Products', required=True)
  145      # performance: product_variant_id provides prefetching on the first product variant only
  146      product_variant_id = fields.Many2one('product.product', 'Product', compute='_compute_product_variant_id')
  147  
  148      product_variant_count = fields.Integer(
  149          '# Product Variants', compute='_compute_product_variant_count')
  150  
  151      # related to display product product information if is_product_variant
  152      barcode = fields.Char('Barcode', compute='_compute_barcode', inverse='_set_barcode', search='_search_barcode')
  153      default_code = fields.Char(
  154          'Internal Reference', compute='_compute_default_code',
  155          inverse='_set_default_code', store=True)
```

**product/models/product_template.py:269-321**

```python
  269      def _compute_template_field_from_variant_field(self, fname, default=False):
  270          """Sets the value of the given field based on the template variant values
  271  
  272          Equals to product_variant_ids[fname] if it's a single variant product.
  273          Otherwise, sets the value specified in ``default``.
  274          It's used to compute fields like barcode, weight, volume..
  275  
  276          :param str fname: name of the field to compute
  277              (field name must be identical between product.product & product.template models)
  278          :param default: default value to set when there are multiple or no variants on the template
  279          :return: None
  280          """
  281          for template in self:
  282              variant_count = len(template.product_variant_ids)
  283              if variant_count == 1:
  284                  template[fname] = template.product_variant_ids[fname]
  285              elif variant_count == 0 and self.env.context.get("active_test", True):
  286                  # If the product has no active variants, retry without the active_test
  287                  template_ctx = template.with_context(active_test=False)
  288                  template_ctx._compute_template_field_from_variant_field(fname, default=default)
  289              else:
  290                  template[fname] = default
  291  
  292      def _set_product_variant_field(self, fname):
  293          """Propagate the value of the given field from the templates to their unique variant.
  294  
  295          Only if it's a single variant product.
  296          It's used to set fields like barcode, weight, volume..
  297  
  298          :param str fname: name of the field whose value should be propagated to the variant.
  299              (field name must be identical between product.product & product.template models)
  300          """
  301          for template in self:
  302              count = len(template.product_variant_ids)
  303              if count == 1:
  304                  template.product_variant_ids[fname] = template[fname]
  305              elif count == 0:
  306                  archived_variants = self.with_context(active_test=False).product_variant_ids
  307                  if len(archived_variants) == 1:
  308                      archived_variants[fname] = template[fname]
  309  
  310      @api.depends_context('company')
  311      @api.depends('product_variant_ids.standard_price')
  312      def _compute_standard_price(self):
  313          # Depends on force_company context because standard_price is company_dependent
  314          # on the product_product
  315          self._compute_template_field_from_variant_field('standard_price')
  316  
  317      def _set_standard_price(self):
  318          self._set_product_variant_field('standard_price')
  319  
  320      def _search_standard_price(self, operator, value):
  321          return [('product_variant_ids.standard_price', operator, value)]
```

**product/models/product_template.py:509-511**

```python
  509      def _get_related_fields_variant_template(self):
  510          """ Return a list of fields present on template and variants models and that are related"""
  511          return ['barcode', 'default_code', 'standard_price', 'volume', 'weight', 'product_properties']
```

**product/models/product_template.py:567-606**

```python
  567      @api.model_create_multi
  568      def create(self, vals_list):
  569          ''' Store the initial standard price in order to be able to retrieve the cost of a product template for a given date'''
  570          templates = super(ProductTemplate, self).create(vals_list)
  571          if self.env.context.get("create_product_product", True):
  572              templates._create_variant_ids()
  573  
  574          # This is needed to set given values to first variant after creation
  575          for template, vals in zip(templates, vals_list):
  576              related_vals = {}
  577              for field_name in self._get_related_fields_variant_template():
  578                  if vals.get(field_name) and not template[field_name]:
  579                      related_vals[field_name] = vals[field_name]
  580              if related_vals:
  581                  template.write(related_vals)
  582  
  583          return templates
  584  
  585      def write(self, vals):
  586          if 'uom_id' in vals:
  587              products = self.filtered(lambda template: template.uom_id.id != vals['uom_id']).product_variant_ids
  588              products.with_context(skip_uom_conversion=True)._update_uom(vals['uom_id'])
  589          res = super(ProductTemplate, self).write(vals)
  590          if self.env.context.get("create_product_product", True) and 'attribute_line_ids' in vals or (vals.get('active') and len(self.product_variant_ids) == 0):
  591              self._create_variant_ids()
  592          if 'active' in vals and not vals.get('active'):
  593              self.with_context(active_test=False).mapped('product_variant_ids').write({'active': vals.get('active')})
  594          if 'image_1920' in vals:
  595              self.env['product.product'].invalidate_model([
  596                  'image_1920',
  597                  'image_1024',
  598                  'image_512',
  599                  'image_256',
  600                  'image_128',
  601                  'can_image_1024_be_zoomed',
  602              ])
  603          for product_template in self:
  604              if "type" in vals and vals.get("type") != "combo":
  605                  product_template.combo_ids = False
  606          return res
```

- Fields shared between template and variant: `_get_related_fields_variant_template` (product/models/product_template.py:509-511) returns `barcode`, `default_code`, `standard_price`, `volume`, `weight`, `product_properties`.
- Template-side values are proxies of the single variant: the compute (269-290) copies the variant value when exactly one variant exists, retries with `active_test=False` when none are active, and otherwise uses the default; the inverse (292-308) writes to the one variant (or the one archived variant).
- Create (567-583): variants are created unless the context flag `create_product_product` is false; supplied values for the related fields are written back to the template after the first variant exists (lines 575-581).
- Write (585-606): `uom_id` change runs `_update_uom` first (586-588); variants are (re)created when `attribute_line_ids` is written or when a template is reactivated with no variants (590-591); archiving a template archives all its variants including inactive ones (592-593); writing a non-combo `type` clears `combo_ids` (603-605).

**product/models/product_product.py:680-710**

```python
  680      def create(self, vals_list):
  681          products = super(ProductProduct, self.with_context(create_product_product=False)).create(vals_list)
  682          # `_get_variant_id_for_combination` depends on existing variants
  683          self.env.registry.clear_cache()
  684          return products
  685  
  686      def write(self, vals):
  687          res = super().write(vals)
  688          if 'product_template_attribute_value_ids' in vals:
  689              # `_get_variant_id_for_combination` depends on `product_template_attribute_value_ids`
  690              self.env.registry.clear_cache()
  691          elif 'active' in vals:
  692              # `_get_first_possible_variant_id` depends on variants active state
  693              self.env.registry.clear_cache()
  694          return res
  695  
  696      def action_archive(self):
  697          records = self.filtered('active')
  698          super().action_archive()
  699          # We deactivate product templates which are active with no active variants.
  700          records.product_tmpl_id.filtered(
  701              lambda product_tmpl: product_tmpl.active and not product_tmpl.product_variant_ids
  702          ).action_archive()
  703  
  704      def action_unarchive(self):
  705          records = self.filtered(lambda rec: not rec.active)
  706          super().action_unarchive()
  707          # We activate product templates which are inactive with active variants.
  708          records.product_tmpl_id.filtered(
  709              lambda product_tmpl: not product_tmpl.active and product_tmpl.product_variant_ids
  710          ).action_unarchive()
```

- Variant archive (product/models/product_product.py:696-702): archiving a variant archives its template only if the template is active and no active variant remains. Unarchive (704-710) activates inactive templates that have active variants.

---

## 10. Migration flags (what a migration script must handle)

Baseline column = comparison against v16/v17 taken from the unit scope text (NOT verified in this tree). "v19 fact" column = verified here.

| Flag | v19 fact (verified here) | Baseline (not verified here) | Pointers |
|---|---|---|---|
| TYPE_PRODUCT_REMOVED | `type` has only `consu`, `service`, `combo`; no `'product'` value | storable goods used a dedicated type value | product/models/product_template.py:54-65 |
| COMBO_TYPE_ADDED | `combo` value plus `combo_ids` many-to-many; two Python constraints require at least one combo choice and, for a sellable combo, only sellable choices; the no-attributes and already-a-combo-item rules and the `purchase_ok` reset exist only in a form-view onchange; writing a non-combo `type` clears `combo_ids` | earlier releases lacked the combo type | product/models/product_template.py:61-70, product/models/product_template.py:459-472, product/models/product_template.py:489-507, product/models/product_template.py:603-605 |
| DETAILED_TYPE_ABSENT | no `detailed_type` in code, only stale `.po` strings | the field existed | section 0; section 1.2 |
| IS_STORABLE_IN_STOCK_MODULE | declared only in stock; stored, editable, default false, reset to false when type is not `consu` | the stock meaning lived in `type` | stock/models/product.py:839-841, 911-913 |
| IS_STORABLE_ENABLE_TRIGGERS_RESET_INVENTORY | write path with truthy flag on a non-storable template calls `_clean_reservations` and `_reset_inventory`; create path does not | not applicable | stock/models/product.py:1115-1160, 1162-1202; stock/models/stock_quant.py:1141-1175 |
| TRACKING_IN_STOCK_MODULE | declared only in stock; default `none` with a migration comment; recomputed to `none` for non-storable templates | tracking existed on goods | stock/models/product.py:856-862, 1094-1096 |
| UOM_PO_ID_ABSENT | no `uom_po_id` in code, only stale `.po` strings; one `uom_id` plus `uom_ids` packagings | a separate purchase unit existed | product/models/product_template.py:118-123 |
| UOM_CATEGORY_REMOVED | no `uom.category` model, no `category_id`, no `uom_type`; units chain through `relative_uom_id` and `relative_factor`; `factor` is a stored recursive compute | units were grouped by category with a type per unit | uom/models/uom_uom.py:18-22, 36-49, 62-75, 97-101 |
| UOM_ROUNDING_COMPUTED_SHARED | `rounding` is a non-stored compute from one shared precision | rounding was a per-unit stored value | uom/models/uom_uom.py:39, 62-67 |
| UOM_CONVERSION_NO_CATEGORY_GUARD | `_compute_quantity` multiplies and divides absolute factors; `raise_if_failure` unused | conversions refused across categories | uom/models/uom_uom.py:147-176 |
| UOM_RATIO_CHANGE_GUARDED | on a write that actually changes `factor`, `relative_factor` or `relative_uom_id` of a unit, stock raises a UserError when an open `stock.move` (state not cancel or done) or an open `stock.move.line` uses that unit, or when a non-zero `stock.quant` belongs to a product whose template base unit is that unit | not applicable | stock/models/product.py:1373-1404 |
| UOM_SYSTEM_UNITS_PROTECTED | units that carry an `ir.model.data` row in module `uom`, other than hour, dozen and pack of six, cannot be deleted through ORM unlink (archive instead; the delete guard is skipped at uninstall) and a UI warning appears on `relative_factor` edits once the unit is older than one day; the timesheet addon adds the hour unit to the protected set | not verified | uom/models/uom_uom.py:24-32, 79-112, 205-216; hr_timesheet/models/uom_uom.py:10-17 |
| UOM_IDS_PACKAGINGS_AND_PRODUCT_UOM_NEW | `uom_ids` "Packagings" plus model `product.uom` with a unique barcode | packagings were a separate model | product/models/product_template.py:122; product/models/product_uom.py:8-26 |
| UOM_CHANGE_ON_PRODUCT_GUARDED | changing `uom_id` runs `_update_uom` hooks that block when other units were already used | not applicable | product/models/product_template.py:585-589; stock/models/product.py:784-808; purchase/models/product.py:117-132; sale/models/product_product.py:101-114 |
| TAX_FIELDS_NAMES_UNCHANGED | `taxes_id` and `supplier_taxes_id`, plain many-to-many, not company-dependent | same names | account/models/product.py:40-52 |
| VALUATION_COST_METHOD_COMPUTED_FROM_CATEGORY | template `cost_method` and `valuation` are non-stored computes from company-dependent category properties, falling back to the company-level `cost_method` / `inventory_valuation` setting when the category property is empty | not verified | stock_account/models/product.py:14-30, 42-79, 725-755 |
| POLICY_FIELDS_IN_SALE_PURCHASE | `invoice_policy`, `expense_policy`, `service_type` live in sale; `purchase_method` lives in purchase; none in product | not verified | sale/models/product_template.py:14-47; purchase/models/product.py:14-29 |
| STANDARD_PRICE_COMPANY_DEPENDENT_ON_VARIANT | company-dependent on the variant; template field is a non-stored proxy | not verified | product/models/product_product.py:62-68; product/models/product_template.py:100-106, 310-321 |
| BARCODE_PYTHON_CONSTRAINT_COMPANY_SCOPED | no database unique on variant barcode; Python constraint scoped by company; `product.uom` barcode has a database unique | not verified | product/models/product_product.py:282-290; product/models/product_uom.py:18 |
| DEFAULT_CODE_NO_UNIQUENESS | no constraint, only onchange warnings | not verified | product/models/product_template.py:422-435; product/models/product_product.py:407-420 |
| SERVICE_TRACKING_VALUES_FROM_ADDONS | base field offers only `no`; further values come from other addons | not verified | product/models/product_template.py:71-80 |

---

## 11. Additional observations

- Template write guard for company changes (stock/models/product.py:1130-1147, inside the write excerpt of section 2.4): a UserError is raised when stock moves (search at 1133-1138) or non-zero quants (search at 1141-1147) of the template's variants belong to a company other than the new one.
- `purchase_ok` is a stored, editable field with a no-op compute method in the product addon (product/models/product_template.py:117, 202-203).
- `product.category` company-dependent valuation properties are declared in stock_account (section 5.3).
- The constraint search in section 3.3 and the data-file search in section 2.3 are limited as described in section 0.

---

## 12. Claim-to-evidence index (neutral claims file)

| Claim-ID | Pointer | Anchor | Flags |
|---|---|---|---|
| U231-C01 | product/models/product_template.py:54-65 | `('combo', "Combo"),` | MIGRATION-FLAG |
| U231-C02 | product/models/product_template.py:54-65 | No match for detailed_type in py, xml, js, csv, json, html, scss files of any addon | MIGRATION-FLAG |
| U231-C03 | stock/models/product.py:839-841, stock/models/product.py:911-913 | `is_storable = fields.Boolean(` | MIGRATION-FLAG |
| U231-C04 | stock/models/product.py:1149-1160, stock/models/product.py:1162-1202 | `templates_to_reset._reset_inventory()` | MIGRATION-FLAG |
| U231-C05 | stock/models/stock_move.py:1967-1970, stock/models/stock_move.py:514-516, stock/models/stock_move_line.py:395-397 | `return location.should_bypass_reservation() or not self.product_id.is_storable` | CONFIRMED |
| U231-C06 | stock_account/models/stock_move.py:659-667 | `and self.product_id.valuation == 'real_time'` | CONFIRMED |
| U231-C07 | stock/models/product.py:856-862, stock/models/product.py:1094-1096 | `tracking = fields.Selection([` | MIGRATION-FLAG |
| U231-C08 | product/models/product_template.py:118-121, product/models/product_template.py:33-36 | `default=_get_default_uom_id, required=True,` | CONFIRMED |
| U231-C09 | product/models/product_template.py:118-122 | No match for uom_po_id in py, xml, js, csv, json, html, scss files of any addon | MIGRATION-FLAG |
| U231-C10 | uom/models/uom_uom.py:36-49, uom/models/uom_uom.py:97-101 | `relative_uom_id = fields.Many2one('uom.uom', 'Reference Unit', ondelete='cascade', index='btree_not_null')` | MIGRATION-FLAG |
| U231-C11 | uom/models/uom_uom.py:62-67 | `self.rounding = 10 ** -decimal_precision` | MIGRATION-FLAG |
| U231-C12 | uom/models/uom_uom.py:147-176, uom/models/uom_uom.py:218-230 | `amount = qty * self.factor` | MIGRATION-FLAG |
| U231-C13 | product/models/product_template.py:585-589, stock/models/product.py:784-808, purchase/models/product.py:117-132, sale/models/product_product.py:101-114, product/models/product_product.py:1197-1200 | `products.with_context(skip_uom_conversion=True)._update_uom(vals['uom_id'])` | CONFIRMED |
| U231-C14 | account/models/product.py:131-150 | `def _check_uom_not_in_invoice(self):` | CONFIRMED |
| U231-C15 | product/models/product_template.py:122, product/models/product_template.py:1578-1580, product/models/product_uom.py:8-18 | `uom_ids = fields.Many2many('uom.uom', string='Packagings'` | MIGRATION-FLAG |
| U231-C16 | product/models/product_product.py:62-68, product/models/product_template.py:100-106, product/models/product_template.py:310-321 | `'Cost', company_dependent=True,` | MIGRATION-FLAG |
| U231-C17 | product/models/product_template.py:94-99, product/models/product_product.py:323-335 | `product.lst_price = list_price + product.price_extra` | CONFIRMED |
| U231-C18 | product/models/product_template.py:81-86, product/models/product_category.py:8-23 | `comodel_name='product.category',` | CONFIRMED |
| U231-C19 | account/models/product.py:40-52 | `supplier_taxes_id = fields.Many2many('account.tax', 'product_supplier_taxes_rel', 'prod_id', 'tax_id',` | CONFIRMED |
| U231-C20 | product/models/product_template.py:116-117, product/models/product_template.py:129, product/models/product_template.py:202-203, product/models/product_template.py:459-472 | `purchase_ok = fields.Boolean('Purchase', default=True, compute='_compute_purchase_ok', store=True, readonly=False)` | CONFIRMED |
| U231-C21 | product/models/product_product.py:246-290, product/models/product_template.py:251-254 | `def _check_barcode_uniqueness(self):` | MIGRATION-FLAG |
| U231-C22 | product/models/product_template.py:153-155, product/models/product_template.py:422-435, product/models/product_product.py:35, product/models/product_product.py:407-420 | `def _onchange_default_code(self):` | CONFIRMED |
| U231-C23 | sale/models/product_template.py:14-47, sale_project/models/product_template.py:45-47, sale_timesheet/models/product_template.py:17-19 | `invoice_policy = fields.Selection(` | MIGRATION-FLAG |
| U231-C24 | sale/models/product_template.py:99-101, sale/models/product_template.py:158-164, sale_stock/models/product_template.py:10-18, sale/wizard/res_config_settings.py:10-17 | `self.filtered(lambda t: t.type == 'consu' or not t.invoice_policy).invoice_policy = 'order'` | CONFIRMED |
| U231-C25 | purchase/models/product.py:14-29 | `purchase_method = fields.Selection([` | CONFIRMED |
| U231-C26 | product/models/product_template.py:509-511, product/models/product_template.py:585-593, product/models/product_product.py:696-710 | `return ['barcode', 'default_code', 'standard_price', 'volume', 'weight', 'product_properties']` | CONFIRMED |

---

## 13. Source file inventory

Files excerpted above, with line count and SHA-256 prefix computed by the generating script from each file as it stood at generation time. Files that appear only in search-based pointers (mirror fields, report files, test files, stale-catalog examples) are not listed in this table.

| Path (relative to addons) | Lines | SHA-256 (first 12 hex) |
|---|---|---|
| account/models/product.py | 558 | c86b3e9b9af6 |
| event_booth_sale/models/product_template.py | 43 | 56fb457c5f2b |
| event_product/models/product_template.py | 12 | e1d98e3af85c |
| hr_timesheet/models/uom_uom.py | 20 | 30d1d50240a5 |
| mrp/models/product.py | 489 | 39f1e0e2eea4 |
| partnership/models/product_template.py | 16 | d0be61a73b5a |
| product/models/product_category.py | 69 | eb003c337d40 |
| product/models/product_product.py | 1200 | d1502c13c231 |
| product/models/product_template.py | 1598 | a6a814f94a7f |
| product/models/product_uom.py | 32 | 551d39d709a8 |
| product/models/uom_uom.py | 30 | 9e624ba69e6e |
| purchase/models/product.py | 154 | 7d79d7f8e9fa |
| repair/models/product.py | 57 | 29ccfae330ab |
| sale/models/product_product.py | 134 | 52f5a72ff6b8 |
| sale/models/product_template.py | 311 | 39823da27e2e |
| sale/wizard/res_config_settings.py | 133 | 061be68a904e |
| sale_project/models/product_template.py | 153 | ce9dbe206ec6 |
| sale_stock/models/product_template.py | 18 | ae011640e21f |
| sale_timesheet/models/product_template.py | 110 | 290673088d93 |
| stock/models/product.py | 1418 | aa1a0c5c1be9 |
| stock/models/stock_move.py | 2833 | af624e7a0155 |
| stock/models/stock_move_line.py | 1244 | bdab636fdc5e |
| stock/models/stock_quant.py | 1567 | 6d894fea4095 |
| stock_account/models/account_move_line.py | 95 | 99f81b90ced0 |
| stock_account/models/product.py | 787 | b1baa31df981 |
| stock_account/models/stock_move.py | 718 | c7950b0328a3 |
| uom/models/uom_uom.py | 230 | 360db3a98217 |
| website_sale_slides/models/product_template.py | 24 | 9864af53be33 |
| website_sale_stock/models/product_template.py | 135 | 7b937b5da5ab |
