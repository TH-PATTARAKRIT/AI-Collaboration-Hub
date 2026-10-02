# U162 — purchase_mrp: Buy Route MRP→PO Replenishment Chain (L3)

**Unit:** U162 | **Group:** G07/G08 | **Priority:** P1  
**Module status:** PRESENT  
**Source root:** `odoo/addons/`  
**Research depth:** L3 (full call-chain traced)

---

## Module Summary

`purchase_mrp` bridges the `mrp` and `purchase_stock` modules. It extends `mrp.production` with a `purchase_order_count` smart-button, extends `purchase.order` with `mrp_production_count`, links raw-component moves to purchase order lines via `created_purchase_line_ids`/`move_dest_ids`, and handles vendor notification when MRP procurement fails to find a supplier. The full buy-route replenishment chain runs through `purchase_stock` (the `_run_buy` method on `stock.rule`) and `stock` (the `run_scheduler` → `_procure_orderpoint_confirm` pathway). `purchase_mrp` itself provides the cross-module navigation and traceability layer.

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U162-C01 | manifest.depends | purchase_mrp/__manifest__.py:26 | `'depends': ['mrp', 'purchase_stock']` | DEPENDENCY | always | VERIFIED | Module declares hard dependencies on mrp and purchase_stock; auto_install=True means it activates whenever both are installed | REF-U162-N01 |
| U162-C02 | MrpProduction.purchase_order_count | purchase_mrp/models/mrp_production.py:10-13 | `purchase_order_count = fields.Integer(...)` | FIELD | always | VERIFIED | `mrp.production` gains a computed integer field `purchase_order_count` (group-restricted to purchase users) that counts POs linked to the MO | REF-U162-N02 |
| U162-C03 | MrpProduction._compute_purchase_order_count | purchase_mrp/models/mrp_production.py:15-18 | `@api.depends('reference_ids', 'reference_ids.purchase_ids')` | COMPUTE | always | VERIFIED | The count is recomputed when the MO's reference set or their linked purchase records change; delegates to `_get_purchase_orders()` | REF-U162-N03 |
| U162-C04 | MrpProduction._get_purchase_orders | purchase_mrp/models/mrp_production.py:46-50 | `moves = self.move_raw_ids \| self.move_raw_ids.move_orig_ids` | TRACEABILITY | always | VERIFIED | Collects POs by unioning `created_purchase_line_ids` and `purchase_line_id` from all raw component moves and their upstream origin moves, then maps to `order_id` | REF-U162-N04 |
| U162-C05 | MrpProduction._get_document_iterate_key | purchase_mrp/models/mrp_production.py:40-44 | `if not iterate_key and move_raw_id.created_purchase_line_ids:` | TRACEABILITY | when raw move has created PO lines | VERIFIED | When iterating upstream documents for a raw move, if no iterate key is found by the parent, the method falls back to `created_purchase_line_ids` to navigate to the PO | REF-U162-N05 |
| U162-C06 | MrpProduction._prepare_merge_orig_links | purchase_mrp/models/mrp_production.py:52-63 | `origs[move.bom_line_id.id].setdefault('created_purchase_line_ids', ...)` | MERGE | when merging backorder MOs | VERIFIED | During MO merge, `created_purchase_line_ids` sets are collected per BoM line and written with `Command.set` to preserve PO linkage across merged MOs | REF-U162-N06 |
| U162-C07 | PurchaseOrder.mrp_production_count | purchase_mrp/models/purchase.py:13-16 | `mrp_production_count = fields.Integer(...)` | FIELD | always | VERIFIED | `purchase.order` gains a computed integer counting manufacturing orders that sourced this PO (group-restricted to MRP users) | REF-U162-N07 |
| U162-C08 | PurchaseOrder._get_mrp_productions | purchase_mrp/models/purchase.py:23-24 | `return (self.order_line.move_dest_ids \| self.order_line.move_ids.move_dest_ids).raw_material_production_id` | TRACEABILITY | always | VERIFIED | Navigates from PO lines → their destination stock moves → the raw-material production IDs to surface the originating MOs | REF-U162-N08 |
| U162-C09 | StockRule._notify_responsible | purchase_mrp/models/stock_rule.py:9-14 | `origin_orders = procurement.values.get('group_id').mrp_production_ids` | NOTIFICATION | when procurement group has MO | VERIFIED | When a buy procurement fails to find a supplier, the MO's responsible users plus the product's responsible partner are all notified via `_post_vendor_notification` | REF-U162-N09 |
| U162-C10 | StockWarehouse.buy_pull_id | purchase_stock/models/stock.py:52 | `buy_pull_id = fields.Many2one('stock.rule', 'Buy rule', copy=False)` | FIELD | always | VERIFIED | Each warehouse stores a direct Many2one pointer to its active `stock.rule` with `action='buy'`; this is the pull rule that triggers PO creation | REF-U162-N10 |
| U162-C11 | StockWarehouse._generate_global_route_rules_values | purchase_stock/models/stock.py:77-98 | `'action': 'buy', 'picking_type_id': self.in_type_id.id` | CONFIG | on warehouse create/update | VERIFIED | The buy pull rule is created with action='buy' and the warehouse's incoming picking type; `location_dest_id` is the main stock location; `propagate_cancel` depends on whether reception is multi-step | REF-U162-N11 |
| U162-C12 | StockRule._run_buy | purchase_stock/models/stock_rule.py:59-165 | `po = self.env['purchase.order'].sudo().search([dom for dom in domain], limit=1)` | PO CREATION | when procurement with buy route | VERIFIED | Groups procurements by their PO domain; if no matching draft PO exists, creates one via SUPERUSER to avoid access-rights issues; if a PO exists, links new reference IDs and updates origin | REF-U162-N12 |
| U162-C13 | StockRule._run_buy (supplier resolution) | purchase_stock/models/stock_rule.py:65-80 | `supplier = rule._get_matching_supplier(...)` | SUPPLIER SELECT | for each procurement | VERIFIED | For each procurement, the matching supplier is resolved from the product's seller list (or from orderpoint's pinned supplier); if none found and context is `from_orderpoint`, a ProcurementException is raised; otherwise downstream moves switch to `make_to_stock` | REF-U162-N13 |
| U162-C14 | StockRule._make_po_get_domain | purchase_stock/models/stock_rule.py:358-392 | `('partner_id', '=', partner.id), ('state', '=', 'draft')` | GROUPING | on each procurement batch | VERIFIED | POs are consolidated by: vendor, draft state, picking type, company, buyer, and currency; partner's `group_rfq` setting optionally narrows further by reference, day, or week | REF-U162-N14 |
| U162-C15 | StockRule._prepare_purchase_order | purchase_stock/models/stock_rule.py:326-356 | `po = self.env['purchase.order'].with_company(company_id).with_user(SUPERUSER_ID).create(vals)` | PO BUILD | when new PO needed | VERIFIED | PO header values (partner, fiscal position, payment terms, date, currency) are built from the first procurement's supplier info; the PO is created as SUPERUSER | REF-U162-N15 |
| U162-C16 | PurchaseOrderLine.move_dest_ids | purchase_stock/models/purchase_order_line.py:30 | `move_dest_ids = fields.Many2many('stock.move', 'stock_move_created_purchase_line_rel', 'created_purchase_line_id', 'move_id', ...)` | FIELD | always | VERIFIED | POL carries a Many2many to downstream stock moves (the MO raw component moves) via the `stock_move_created_purchase_line_rel` table — the same table used by `stock.move.created_purchase_line_ids` | REF-U162-N16 |
| U162-C17 | PurchaseOrderLine._prepare_purchase_order_line_from_procurement | purchase_stock/models/purchase_order_line.py:356 | `res['move_dest_ids'] = [(4, x.id) for x in values.get('move_dest_ids', [])]` | LINK | when creating new POL from procurement | VERIFIED | During POL creation, the MO component move IDs are written into `move_dest_ids`, creating the bidirectional PO↔MO linkage | REF-U162-N17 |
| U162-C18 | StockMove.created_purchase_line_ids | purchase_stock/models/stock_move.py:18-20 | `created_purchase_line_ids = fields.Many2many('purchase.order.line', 'stock_move_created_purchase_line_rel', ...)` | FIELD | always | VERIFIED | Each stock move (including MO raw component moves) carries a Many2many back-reference to the PO lines that were created to fulfill it | REF-U162-N18 |
| U162-C19 | MrpProduction.action_confirm | mrp/models/mrp_production.py:1625-1667 | `move_raws_to_adjust._adjust_procure_method()` then `moves_to_confirm._action_confirm(merge=False)` | MO CONFIRM | on MO confirmation | VERIFIED | On MO confirmation, raw move procure methods are adjusted (MTS vs MTO depending on route rules), then all raw/finish moves are confirmed; finally `_trigger_scheduler` is called on raw moves | REF-U162-N19 |
| U162-C20 | MrpProduction.action_confirm (scheduler trigger) | mrp/models/mrp_production.py:1661 | `self.move_raw_ids.with_context(ignore_mo_ids=...) ._trigger_scheduler()` | SCHEDULER TRIGGER | after move confirmation | VERIFIED | After confirming MO moves, `_trigger_scheduler()` is explicitly called on all raw component moves to trigger any matching auto-reorder rules | REF-U162-N20 |
| U162-C21 | MrpProduction._get_moves_raw_values | mrp/models/mrp_production.py:1382 | `'procure_method': 'make_to_stock'` | DEFAULT | when building component moves | VERIFIED | Component moves are initially created with `procure_method='make_to_stock'`; `_adjust_procure_method` later switches to `make_to_order` if the product's route resolves to a buy (or manufacture) pull rule | REF-U162-N21 |
| U162-C22 | StockRule.run_scheduler | stock/models/stock_rule.py:734-743 | `self._run_scheduler_tasks(use_new_cursor=use_new_cursor, company_id=company_id)` | SCHEDULER | on cron / manual call | VERIFIED | Top-level entry point; delegates to `_run_scheduler_tasks`, which computes all orderpoints, calls `_procure_orderpoint_confirm`, then batch-assigns waiting moves | REF-U162-N22 |
| U162-C23 | StockRule._run_scheduler_tasks | stock/models/stock_rule.py:693-726 | `orderpoints.sudo()._procure_orderpoint_confirm(...)` then `moves._action_assign()` | SCHEDULER CHAIN | on each scheduler run | VERIFIED | Scheduler: (1) recomputes orderpoint quantities, (2) calls `_procure_orderpoint_confirm` to create buy procurements (→ RFQs), (3) assigns all confirmed MTS moves; runs as SUDO | REF-U162-N23 |
| U162-C24 | StockWarehouseOrderpoint._procure_orderpoint_confirm | stock/models/stock_orderpoint.py:712-791 | `self.env['stock.rule'].with_context(from_orderpoint=True).run(procurements, ...)` | PROCUREMENT | when orderpoint qty_to_order > 0 | VERIFIED | For each orderpoint needing replenishment, builds a Procurement namedtuple and calls `stock.rule.run()`; errors accumulate as activities on the product template | REF-U162-N24 |
| U162-C25 | StockMove._action_done (receipt → MO reservation) | stock/models/stock_move.py:2300-2303 | `for move_dest in moves_todo.move_dest_ids: ... move_dests.sudo()._action_assign()` | AVAILABILITY | when PO receipt validated | VERIFIED | After the PO receipt's incoming moves are set to 'done', `_action_assign()` is immediately called on all `move_dest_ids` — the MO raw component moves — automatically reserving stock for the MO | REF-U162-N25 |

---

## Call-Chain Summary

```
run_scheduler()                         [stock/models/stock_rule.py:734]
  → _run_scheduler_tasks()              [stock/models/stock_rule.py:693]
    → _procure_orderpoint_confirm()     [stock/models/stock_orderpoint.py:712]
      → stock.rule.run(procurements)    [purchase_stock/models/stock_rule.py:46]
        → _run_buy(procurements)        [purchase_stock/models/stock_rule.py:59]
          → purchase.order.create()     [purchase_stock/models/stock_rule.py:115]
          → purchase.order.line.create() [purchase_stock/models/stock_rule.py:165]
            (move_dest_ids links POL → MO raw move)

Also triggered from MO confirm:
mrp.production.action_confirm()        [mrp/models/mrp_production.py:1625]
  → _adjust_procure_method()           [stock/models/stock_move.py:2572]
  → stock.move._action_confirm()       [stock/models/stock_move.py:...]
  → stock.move._trigger_scheduler()   [stock/models/stock_move.py:2609]
    → _procure_orderpoint_confirm()    [stock/models/stock_orderpoint.py:712]

PO receipt → MO availability:
stock.picking._action_done()           [purchase_stock/models/stock.py:40]
  → stock.move._action_done()          [stock/models/stock_move.py:2249]
    → move_dest_ids._action_assign()   [stock/models/stock_move.py:2303]
      (MO component moves become reserved/available)
```

---

## Key Files Read

| File | Lines read |
|---|---|
| `purchase_mrp/__manifest__.py` | 1–36 |
| `purchase_mrp/models/mrp_production.py` | 1–64 |
| `purchase_mrp/models/stock_rule.py` | 1–15 |
| `purchase_mrp/models/purchase.py` | 1–125 |
| `purchase_mrp/models/stock_move.py` | 1–95 |
| `purchase_mrp/models/mrp_bom.py` | 1–77 |
| `purchase_stock/models/stock.py` | 1–355 |
| `purchase_stock/models/stock_rule.py` | 1–412 |
| `purchase_stock/models/stock_move.py` | 1–130 |
| `purchase_stock/models/purchase_order_line.py` | 333–435 |
| `mrp/models/mrp_production.py` | 1339–1391, 1625–1667 |
| `stock/models/stock_rule.py` | 693–750 |
| `stock/models/stock_orderpoint.py` | 712–791 |
| `stock/models/stock_move.py` | 2249–2310, 2572–2632 |
