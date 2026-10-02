# U78 — MRP Full MO Lifecycle (L3/L4/L5/L7)
**Unit**: U78
**Phase**: Second-Pass Depth Closure — P1 Core Business
**Scope**: MO lifecycle BOM→confirm→consume→produce→close; WIP/FG account entries; subcontracting
**Modules**: mrp, mrp_account, mrp_subcontracting, mrp_subcontracting_account, stock_account
**Function-IDs targeted**: BRP-F01, BRP-F08, MFG-F01, MFG-F02
**L-levels**: L3, L4, L5, L7
**Proof layers**: P2, P3, P4
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: U14, U15, U72

---

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U78-001 | MFG-F01 | mrp/models/mrp_bom.py:27 | `('normal', 'Manufacture this product')` | SCHEMA | base | C1 | mrp.bom.type Selection has values 'normal' (Manufacture this product) and 'phantom' (Kit) in base mrp module | NR-U78-001 |
| U78-002 | MFG-F01 | mrp/models/mrp_bom.py:40 | `bom_line_ids = fields.One2many('mrp.bom.line'` | SCHEMA | base | C1 | BOM component lines stored as mrp.bom.line records linked via bom_id; finished product quantity in product_qty field | NR-U78-002 |
| U78-003 | MFG-F02 | mrp_subcontracting/models/mrp_bom.py:11 | `type = fields.Selection(selection_add=[` | OVERRIDE | mrp_subcontracting installed | C1 | mrp_subcontracting extends mrp.bom.type Selection to add 'subcontract' (Subcontracting) value via selection_add | NR-U78-003 |
| U78-004 | MFG-F02 | mrp_subcontracting/models/mrp_bom.py:14 | `subcontractor_ids = fields.Many2many('res.partner'` | SCHEMA | mrp_subcontracting installed | C1 | Subcontracting BOM carries subcontractor_ids (Many2many res.partner) to restrict which partners can supply the subcontracted item | NR-U78-004 |
| U78-005 | MFG-F01 | mrp/models/mrp_production.py:177 | `('draft', 'Draft'),` | SCHEMA | base | C1 | mrp.production.state Selection: draft→confirmed→progress→to_close→done (also cancel); state is computed and stored | NR-U78-005 |
| U78-006 | MFG-F01 | mrp/models/mrp_production.py:1625 | `def action_confirm(self):` | FLOW | state='draft' | C1 | action_confirm collects move_raw_ids and move_finished_ids, calls _adjust_procure_method, then _action_confirm(merge=False) on all moves; sets state='confirmed' for draft MOs | NR-U78-006 |
| U78-007 | MFG-F01 | mrp/models/mrp_production.py:1661 | `self.move_raw_ids.with_context(ignore_mo_ids=ignored_mo_ids` | CALL | confirmed | C1 | After move confirmation, action_confirm triggers the scheduler for move_raw_ids to replenish stock if insufficient components | NR-U78-007 |
| U78-008 | MFG-F01 | mrp/models/mrp_production.py:1666 | `self.filtered(lambda mo: mo.state == 'draft').state = 'confirmed'` | ASSIGN | state='draft' | C1 | Only draft MOs are forced to confirmed; more advanced states (progress, backorders) are preserved | NR-U78-008 |
| U78-009 | MFG-F01 | mrp/models/mrp_production.py:203 | `move_raw_ids = fields.One2many(` | SCHEMA | base | C1 | Component demand represented as stock.move records linked by raw_material_production_id (One2many); computed and stored | NR-U78-009 |
| U78-010 | MFG-F01 | mrp/models/mrp_production.py:1377 | `'location_dest_id': self.product_id.with_company(self.company_id).property_stock_production.id,` | ASSIGN | raw move creation | C1 | Raw material stock moves route FROM source_location TO product.property_stock_production (the production/WIP location) | NR-U78-010 |
| U78-011 | MFG-F01 | mrp/models/mrp_production.py:1288 | `'location_id': self.product_id.with_company(self.company_id).property_stock_production.id,` | ASSIGN | finished move creation | C1 | Finished goods stock moves route FROM property_stock_production TO location_dest_id (finished goods location) | NR-U78-011 |
| U78-012 | MFG-F01 | mrp/models/mrp_production.py:1703 | `def action_assign(self):` | FLOW | confirmed | C1 | action_assign triggers stock reservation for component moves; no separate picking created for components—moves are directly on the MO | NR-U78-012 |
| U78-013 | MFG-F01 | mrp/models/mrp_production.py:1402 | `def _set_qty_producing(self, pick_manual_consumption_moves=True):` | FLOW | qty_producing set | C1 | _set_qty_producing iterates move_raw_ids and move_finished_ids, setting each move's quantity proportional to (qty_producing - qty_produced) * unit_factor | NR-U78-013 |
| U78-014 | MFG-F01 | mrp/models/mrp_production.py:1423 | `new_qty = move.product_uom.round((self.qty_producing - self.qty_produced) * move.unit_factor)` | CALC | qty_producing set | C1 | Per-move quantity is (qty_producing - qty_produced) * unit_factor, rounded to product UoM precision | NR-U78-014 |
| U78-015 | MFG-F01 | mrp/models/mrp_production.py:2219 | `def button_mark_done(self):` | FLOW | state in progress/to_close | C1 | button_mark_done calls pre_button_mark_done, optionally _split_productions, then _post_inventory on both backorder and non-backorder sets, then sets state='done' | NR-U78-015 |
| U78-016 | MFG-F01 | mrp/models/mrp_production.py:2251 | `'state': 'done',` | ASSIGN | MO close | C1 | MO state written to 'done' with is_locked=True and date_finished=Datetime.now() in button_mark_done | NR-U78-016 |
| U78-017 | MFG-F01 | mrp/models/mrp_production.py:1907 | `def _post_inventory(self, cancel_backorder=False):` | FLOW | close | C1 | _post_inventory calls _action_done on raw moves (components), calls _cal_price on each order, then calls _action_done on finished moves; component and finished moves share same MO—no separate pickings | NR-U78-017 |
| U78-018 | MFG-F01 | mrp/models/mrp_production.py:1917 | `self.with_context(skip_mo_check=True).env['stock.move'].browse(moves_to_do)._action_done(cancel_backorder=cancel_backorder)` | CALL | close | C1 | Component raw moves (moves_to_do) are posted via _action_done before finished goods moves; cancel_backorder propagated | NR-U78-018 |
| U78-019 | MFG-F01 | mrp/models/mrp_production.py:1948 | `order.with_company(order.company_id)._cal_price(moves_to_do_by_order[order.id])` | CALL | close | C1 | _cal_price called with consumed_moves (done component moves) to set price_unit on finished move before posting finished move | NR-U78-019 |
| U78-020 | MFG-F01 | mrp/models/mrp_production.py:1903 | `def _cal_price(self, consumed_moves):` | FLOW | base mrp | C1 | Base mrp._cal_price is a no-op (returns True); overridden in mrp_account to set finished move price_unit | NR-U78-020 |
| U78-021 | BRP-F01 | mrp_account/models/mrp_production.py:57 | `def _cal_price(self, consumed_moves):` | OVERRIDE | mrp_account installed | C1 | mrp_account overrides _cal_price: sums component move values + workcenter costs + extra_cost to determine total_cost for finished goods valuation | NR-U78-021 |
| U78-022 | BRP-F01 | mrp_account/models/mrp_production.py:90 | `if finished_moves.product_id.cost_method not in ('fifo', 'average'):` | GUARD | standard cost | C1 | For standard-cost (non-AVCO/FIFO) products, finished move price_unit is set to product.standard_price regardless of actual consumed cost | NR-U78-022 |
| U78-023 | BRP-F01 | mrp_account/models/mrp_production.py:93 | `finished_moves.price_unit = total_cost * float_round(1 - byproduct_cost_share / 100, precision_rounding=0.0001) / quantity` | CALC | AVCO/FIFO | C1 | For AVCO or FIFO products, finished move price_unit = actual_total_cost * (1 - byproduct_share%) / produced_quantity | NR-U78-023 |
| U78-024 | BRP-F08 | stock_account/models/stock_move.py:177 | `def _action_done(self, cancel_backorder=False):` | FLOW | real_time valuation | C1 | stock_account overrides _action_done: sets value on out-moves (via _set_value), calls super, sets value on in-moves, then calls _create_account_move on all done moves | NR-U78-024 |
| U78-025 | BRP-F08 | stock_account/models/stock_move.py:193 | `def _create_account_move(self):` | FLOW | real_time + valued move | C1 | _create_account_move creates one account.move per batch of valued stock moves, using _get_account_move_line_vals; posts immediately; links to account_move_id | NR-U78-025 |
| U78-026 | BRP-F08 | stock_account/models/stock_move.py:659 | `def _should_create_account_move(self):` | GUARD | real_time | C1 | _should_create_account_move requires: product.is_storable, is_valued, (location_dest_id.valuation_account_id OR location_id.valuation_account_id), non-zero quantity, product.valuation=='real_time' | NR-U78-026 |
| U78-027 | BRP-F08 | stock_account/models/stock_move.py:229 | `if self.location_id.valuation_account_id:` | GUARD | component consumption | C1 | When location_id has valuation_account_id (e.g. production_loc as source for FG move): debit=product_stock_valuation, credit=location_id.valuation_account_id | NR-U78-027 |
| U78-028 | BRP-F08 | stock_account/models/stock_move.py:234 | `debit_acc = self.location_dest_id.valuation_account_id` | ASSIGN | FG incoming | C1 | When location_dest_id has valuation_account_id (production_loc as destination for component move): debit=location_dest_id.valuation_account_id (WIP), credit=product_stock_valuation | NR-U78-028 |
| U78-029 | BRP-F01 | stock_account/models/stock_location.py:11 | `valuation_account_id = fields.Many2one(` | SCHEMA | stock_account installed | C1 | stock.location has valuation_account_id field (Many2one account.account); when set on production location, it acts as the WIP account for MRP accounting entries | NR-U78-029 |
| U78-030 | BRP-F01 | stock_account/models/res_company.py:16 | `account_production_wip_account_id = fields.Many2one('account.account', string='Production WIP Account'` | SCHEMA | stock_account | C1 | res.company carries account_production_wip_account_id (Production WIP Account) and account_production_wip_overhead_account_id (Production WIP Overhead Account) fields | NR-U78-030 |
| U78-031 | BRP-F01 | mrp_account/models/mrp_production.py:101 | `def _post_labour(self):` | FLOW | real_time, production_loc.valuation_account_id set | C1 | _post_labour creates account.move for workcenter labour cost: DR production_location.valuation_account_id (WIP) / CR workcenter.expense_account_id or product expense account | NR-U78-031 |
| U78-032 | BRP-F01 | mrp_account/models/mrp_production.py:141 | `def _post_inventory(self, cancel_backorder=False):` | OVERRIDE | mrp_account | C1 | mrp_account overrides _post_inventory: calls super() then calls _post_labour() on done MOs to post workcenter labour journal entries | NR-U78-032 |
| U78-033 | BRP-F01 | mrp_account/wizard/mrp_wip_accounting.py:101 | `'account_id': self.env.company.account_production_wip_account_id.id,` | ASSIGN | WIP wizard | C1 | WIP accounting wizard creates DR WIP account (account_production_wip_account_id) / CR Stock Valuation + CR Overhead; auto-reversal posted on reversal_date | NR-U78-033 |
| U78-034 | BRP-F01 | mrp_account/wizard/mrp_wip_accounting.py:47 | `productions = productions.filtered(lambda mo: mo.state in ['progress', 'to_close', 'confirmed'])` | GUARD | WIP wizard | | WIP wizard only applies to MOs in confirmed/progress/to_close states; done/cancelled MOs produce a manual zero-value entry | NR-U78-034 |
| U78-035 | MFG-F02 | mrp_subcontracting/models/stock_move.py:143 | `def _action_confirm(self, merge=True, merge_into=False, create_proc=True):` | FLOW | subcontract BOM | C1 | On receipt move confirmation matching a subcontract BOM, _action_confirm sets is_subcontract=True, sets location_id to partner's subcontracting location, then calls _subcontracted_produce to create the linked MO | NR-U78-035 |
| U78-036 | MFG-F02 | mrp_subcontracting/models/stock_picking.py:143 | `def _subcontracted_produce(self, subcontract_details):` | FLOW | subcontract receipt | C1 | _subcontracted_produce creates mrp.production records for each subcontract move/BOM pair and calls action_confirm on them; finished move linked to receipt move via move_dest_ids | NR-U78-036 |
| U78-037 | MFG-F02 | mrp_subcontracting/models/stock_move.py:14 | `is_subcontract = fields.Boolean('The move is a subcontract receipt')` | SCHEMA | mrp_subcontracting | C1 | stock.move carries is_subcontract Boolean flag marking receipt moves that trigger subcontracting MO creation | NR-U78-037 |
| U78-038 | MFG-F01 | mrp_account/models/mrp_production.py:15 | `wip_move_ids = fields.Many2many('account.move', 'wip_move_production_rel'` | SCHEMA | mrp_account | C1 | mrp.production carries wip_move_ids (Many2many to account.move) tracking WIP journal entries associated with the MO | NR-U78-038 |
| U78-039 | BRP-F01 | mrp_account/models/mrp_production.py:74 | `total_cost = sum(move.value for move in consumed_moves) + work_center_cost + extra_cost` | CALC | AVCO/FIFO close | C1 | Total MO cost = sum of consumed component move values + workcenter costs (_cal_cost) + MO extra_cost field | NR-U78-039 |
| U78-040 | MFG-F02 | mrp_subcontracting_account/models/mrp_production.py:10 | `def _cal_price(self, consumed_moves):` | OVERRIDE | subcontract+account | C1 | mrp_subcontracting_account overrides _cal_price: for subcontract receipts sets extra_cost from bill/quotation value; calls super() to apply standard mrp_account price calculation | NR-U78-040 |
| U78-041 | BRP-F01 | mrp_account/tests/common.py:43 | `cls.account_production = cls.env['account.account'].create({` | CONFIG | test setup | | Test harness sets production_locations.valuation_account_id to an asset_current account to enable WIP accounting; without this the account entries for component/FG moves are not created | NR-U78-041 |
| U78-042 | MFG-F01 | mrp/models/mrp_production.py:208 | `move_finished_ids = fields.One2many(` | SCHEMA | base | C1 | Finished goods demand represented as stock.move records linked by production_id; includes both main product and byproducts | NR-U78-042 |
| U78-043 | MFG-F01 | mrp/models/mrp_bom.py:70 | `consumption = fields.Selection([` | SCHEMA | base | | BOM.consumption controls flexible consumption ('flexible'/'warning'/'strict'); affects whether button_mark_done is blocked when actual vs planned component qty differs | NR-U78-043 |
| U78-044 | BRP-F01 | stock_account/models/stock_move.py:346 | `if move.product_id.cost_method == 'fifo':` | GUARD | outgoing move | C1 | Outgoing stock move value: FIFO uses _run_fifo to pop FIFO layers; non-FIFO uses standard_price * valued_qty | NR-U78-044 |
| U78-045 | BRP-F08 | mrp_account/models/mrp_production.py:13 | `extra_cost = fields.Float(copy=False, string='Extra Unit Cost')` | SCHEMA | mrp_account | | mrp.production.extra_cost Float field holds additional per-unit cost (e.g. subcontractor fee) added to total_cost in _cal_price | NR-U78-045 |

---

## Notes

### MO State Machine (confirmed from mrp/models/mrp_production.py:177-191)
draft → confirmed (action_confirm) → progress (first workorder/qty_producing set) → to_close → done (button_mark_done)

### Account Entry Flow at MO Close (real_time valuation, production_location.valuation_account_id = WIP)

**Component consumption** (stock_location → production_location):
- `_is_out()=True` → `is_valued=True`
- `_should_create_account_move`: location_dest_id.valuation_account_id (WIP) is set → True
- Entry: DR WIP account / CR product.stock_valuation_account

**Finished goods receipt** (production_location → FG stock location):
- `_is_in()=True` → `is_valued=True`
- `_should_create_account_move`: location_id.valuation_account_id (WIP) is set → True
- Entry: DR product.stock_valuation_account / CR WIP account

**Labour** (via _post_labour on MO done):
- Entry: DR WIP (production_location.valuation_account_id) / CR workcenter.expense_account_id

**Key condition**: WIP accounting entries only created when `production_location.valuation_account_id` is configured.

### Variance Handling
- Standard cost: FG move price_unit = standard_price regardless of actual cost. No explicit variance account entry. Difference between actual component cost and FG standard_price is NOT isolated to a variance account in Community.
- AVCO/FIFO: FG move price_unit = total_actual_cost * (1-byproduct_share%) / qty_produced.

### Subcontracting in Community
Both `mrp_subcontracting` and `mrp_subcontracting_account` exist in the Community addons directory. Subcontracting creates a full MO linked to a supplier receipt; the MO's finished move flows into the receipt move via move_dest_ids.

### No Separate Pickings for MO
Component and finished goods stock moves are directly attached to the MO (not via pickings). pickings_ids on MO refers to replenishment transfers for components, not the production moves themselves.
