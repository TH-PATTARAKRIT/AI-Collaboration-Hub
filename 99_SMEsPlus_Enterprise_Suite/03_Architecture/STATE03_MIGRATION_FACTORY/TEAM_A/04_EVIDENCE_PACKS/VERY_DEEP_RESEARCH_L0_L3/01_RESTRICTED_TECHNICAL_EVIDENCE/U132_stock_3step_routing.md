# U132 — stock: 3-Step Routing AWT-Prep + Source Deep (GAP-030)

**Unit:** U132 | **G-Group:** G06 | **Priority:** P2 | **Gap:** GAP-030
**Date:** 2026-10-02 | **Status:** GATE-PASS

---

## L1–L12 Applicability Matrix

| Layer | Status | Notes |
|-------|--------|-------|
| L1 | APPLICABLE | `stock/__manifest__.py:9` — depends: `['product', 'barcodes_gs1_nomenclature', 'digest']`; version 1.1 |
| L2 | APPLICABLE | `stock_warehouse.py` fields `reception_steps`, `delivery_steps`, `wh_qc_stock_loc_id`, `qc_type_id`, `store_type_id` |
| L3 | APPLICABLE | Route/rule creation in `_create_or_update_route`; state chain: Supplier→Input→QC→Stock |
| L4 | APPLICABLE | `stock_rule.py` `_run_push` / `_run_pull`; `stock_move.py` `_push_apply` cross-model calls |
| L5 | APPLICABLE | `stock_warehouse_views.xml:39-40` — radio widgets for `reception_steps` / `delivery_steps` |
| L6 | APPLICABLE | `stock_security.xml:50-52` `group_adv_location`; `stock_security.xml:96-100` warehouse multi-company rule |
| L7 | APPLICABLE | `res_config_settings.py:23-25` — `group_stock_adv_location` Boolean (implied_group `stock.group_adv_location`) must be enabled |
| L8 | APPLICABLE | Rule `procure_method`: first rule `make_to_stock`, subsequent rules `make_to_order` (`stock_warehouse.py:834`); last rule's `propagate_cancel` forced False (`stock_warehouse.py:851`) |
| L9 | N/A | No direct account posting in routing logic |
| L10 | APPLICABLE | `stock_rule.py:693-716` — `_run_scheduler_tasks` assigns reserved moves; cron triggers procurement |
| L11 | APPLICABLE | `stock_rule.py` `Procurement` NamedTuple at line 31; `run()` method is the public procurement API |
| L12 | AWT-REQUIRED | GAP-030: 3-step sequence execution NOT_PROVEN at runtime; AWT test plan below |

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|----------|-------------|---------|--------|-------|-----------|-------|---------------------|-------------|
| U132-C01 | WH-FIELD-RECV | `stock/models/stock_warehouse.py:56-61` | `reception_steps` Selection field | C1 | Always | C1 | `reception_steps` Selection field defines three incoming modes: `one_step`, `two_steps`, `three_steps` (label: "Receive, Quality Control, then Store (3 steps)") | Warehouse model carries a selection field for inbound routing that offers a three-step mode labelled receive, quality control then store |
| U132-C02 | WH-FIELD-DELV | `stock/models/stock_warehouse.py:62-67` | `delivery_steps` Selection field | C1 | Always | C1 | `delivery_steps` Selection field defines three outgoing modes: `ship_only`, `pick_ship`, `pick_pack_ship` (label: "Pick, Pack, then Deliver (3 steps)") | Warehouse model carries a selection field for outbound routing that offers a three-step mode labelled pick, pack then deliver |
| U132-C03 | WH-FIELD-LOCS | `stock/models/stock_warehouse.py:68-80` | `wh_qc_stock_loc_id`, `qc_type_id`, `store_type_id` | C1 | Always | C1 | Warehouse declares `wh_qc_stock_loc_id` (Quality Control location), `qc_type_id` (QC picking type) and `store_type_id` (Storage picking type) as Many2one fields | Warehouse model declares dedicated fields for the quality control staging area, the quality control operation category, and the storage operation category |
| U132-C04 | WH-RULES-3IN | `stock/models/stock_warehouse.py:777-780` | `get_rules_dict` `three_steps` entry | C1 | `reception_steps == 'three_steps'` | C1 | `three_steps` inbound route creates 3 Routing objects: (1) Supplier→lot_stock pull via in_type; (2) wh_input→wh_qc push via qc_type; (3) wh_qc→lot_stock push via store_type | Inbound three-step mode defines a pull rule from vendor to input then two push rules chaining input to quality control and quality control to stock |
| U132-C05 | WH-RULES-3OUT | `stock/models/stock_warehouse.py:785-788` | `get_rules_dict` `pick_pack_ship` entry | C1 | `delivery_steps == 'pick_pack_ship'` | C1 | `pick_pack_ship` outbound route creates 3 Routing objects: (1) lot_stock→Customer pull via pick_type; (2) wh_pack→wh_output push via pack_type; (3) wh_output→Customer push via out_type | Outbound three-step mode defines a pull rule from stock to customer via the pick operation then two push rules chaining pack zone to output and output to customer |
| U132-C06 | WH-PROCURE-CHAIN | `stock/models/stock_warehouse.py:834` | `_get_rule_values` `procure_method` assignment | C1 | Always | C1 | First rule in a chain receives `procure_method='make_to_stock'`; all subsequent rules receive `make_to_order`, which causes each downstream step to wait for the previous move to complete | In a multi-step route only the first rule takes from available stock; every subsequent rule triggers demand on the preceding step, enforcing sequential execution |
| U132-C07 | WH-CANCEL-PROP | `stock/models/stock_warehouse.py:841-851` | `_get_rule_values` propagate_cancel override | C1 | `values.get('propagate_cancel')` is True | C1 | When `propagate_cancel` is requested, the last rule in the chain has it forced to False to prevent cancellation propagating beyond the route's boundary | Cancel propagation is deliberately terminated at the last rule in the chain to avoid inadvertently cancelling moves that follow the route |
| U132-C08 | WH-LOC-QC-ACT | `stock/models/stock_warehouse.py:946` | `_update_location_reception` | C1 | `new_reception_step` value | C1 | `_update_location_reception` activates `wh_qc_stock_loc_id` only when `new_reception_step == 'three_steps'`; Input location is activated for any multi-step incoming | Quality control location is toggled active exclusively for three-step inbound; the input staging location activates for both two-step and three-step inbound |
| U132-C09 | WH-TYPE-QC-ACT | `stock/models/stock_warehouse.py:980-981` | `_get_picking_type_update_values` `qc_type_id` block | C1 | `reception_steps == 'three_steps'` | C1 | Quality Control picking type is activated only when `reception_steps == 'three_steps'`; Storage picking type source is set to QC location in three-steps mode, Input location in two-steps mode | The quality control operation category is activated exclusively for three-step inbound; the storage operation category adjusts its source location to match the active inbound step count |
| U132-C10 | WH-TYPE-QC-CREATE | `stock/models/stock_warehouse.py:1040-1048` | `_get_picking_type_create_values` `qc_type_id` block | C1 | warehouse creation | C1 | On warehouse creation, `qc_type_id` is created with `code='internal'`, `sequence_code='QC'`, `default_location_src_id=wh_input_stock_loc_id`, `default_location_dest_id=wh_qc_stock_loc_id` | On warehouse creation the quality control operation category is always created as an internal transfer type with a QC prefix, source set to input and destination set to quality control location |
| U132-C11 | RULE-PUSH-APPLY | `stock/models/stock_move.py:1214-1264` | `_push_apply` method | C1 | called in `_action_confirm` at line 2299 | C1 | After a move is confirmed, `_push_apply` calls `StockRule._get_push_rule` to find a matching push rule from the move's destination location; if found, `_run_push` creates a successor move linked via `move_dest_ids` | After a transfer step is confirmed the engine searches for a push rule whose source matches the step's destination; if found a successor move is created and linked to the originator |
| U132-C12 | RULE-RUN-PUSH | `stock/models/stock_rule.py:222-254` | `_run_push` method | C1 | rule.auto != 'transparent' | C1 | `_run_push` calls `_push_prepare_move_copy_values` to build a new move with `procure_method='make_to_order'` and `picking_type_id=self.picking_type_id.id`, then sets `move.move_dest_ids` to link the chain | The push rule execution creates a downstream move with make-to-order procurement and links it as a successor of the triggering move |
| U132-C13 | RULE-GET-PUSH | `stock/models/stock_rule.py:668-678` | `_get_push_rule` method | C1 | Always | C1 | Push rule search walks the location tree upward from `location_dest_id` searching for a rule with `action in ('push', 'pull_push')` and matching route and warehouse | Push rule lookup ascends the location hierarchy until a matching rule is found, enabling inherited push routing |
| U132-C14 | WH-L7-PREREQ | `stock/models/res_config_settings.py:23-25` | `group_stock_adv_location` field | C1 | Multi-Step Routes setting | C1 | `group_stock_adv_location = fields.Boolean("Multi-Step Routes", implied_group='stock.group_adv_location')` — this group must be enabled for `reception_steps`/`delivery_steps` selection to appear in the warehouse form | The Multi-Step Routes configuration toggle must be enabled before multi-step routing options are exposed in the warehouse form |
| U132-C15 | WH-VIEW-RADIO | `stock/views/stock_warehouse_views.xml:38-41` | Warehouse form Shipments group | C1 | `groups="stock.group_adv_location"` | C1 | The Shipments group containing `reception_steps` and `delivery_steps` radio widgets is conditionally rendered only for users in `stock.group_adv_location` | The inbound and outbound routing step selectors in the warehouse form are only visible to users who have the advanced location permission group enabled |
| U132-C16 | WH-RECEIVE-DICT | `stock/models/stock_warehouse.py:803-806` | `_get_receive_rules_dict` `three_steps` entry | C1 | Used with `_get_receive_routes_values` | C1 | `_get_receive_rules_dict` for `three_steps` returns only the two push rules (input→QC, QC→stock), omitting the initial pull rule, for use when an external module provides the initial trigger | An alternative three-step inbound rule dictionary exists that omits the supplier pull rule, intended for modules that supply their own initial inbound trigger |
| U132-C17-AWT | AWT-3IN-EXEC | Runtime — AWT required | Three-step inbound execution | C3 | `reception_steps == 'three_steps'` in live instance | AWT, GAP | Create a receipt (IN) for a product; validate it; confirm that a Quality Control (QC) transfer is automatically created; validate QC transfer; confirm Storage (STOR) transfer is auto-created and moves product to stock location | End-to-end three-step inbound chain must be exercised on a live instance to verify each push rule fires in sequence |
| U132-C18-AWT | AWT-3OUT-EXEC | Runtime — AWT required | Three-step outbound execution | C3 | `delivery_steps == 'pick_pack_ship'` in live instance | AWT, GAP | Confirm a delivery order; verify PICK transfer is created from stock to pack zone; validate PICK; verify PACK transfer is created from pack zone to output; validate PACK; verify OUT delivery order fires and reaches customer location | End-to-end three-step outbound chain must be exercised on a live instance to verify pick, pack and ship transfers chain correctly |
| U132-C19-AWT | AWT-CANCEL-PROP | Runtime — AWT required | Cancel propagation boundary | C3 | `propagate_cancel=True` on reception route | AWT, GAP | Cancel the QC transfer after the IN transfer is done; confirm that the STOR transfer is cancelled but any downstream customer-facing move is unaffected | Runtime verification that cancel propagation stops at the last inbound step and does not cascade beyond the route boundary |

---

## AWT Test Plan (GAP-030)

### AWT-01: Three-Step Inbound (Receive + Quality Control + Storage)

**Prerequisites:**
1. Enable Multi-Step Routes: Settings → Inventory → Warehouse → Multi-Step Routes = True (activates `stock.group_adv_location`)
2. Navigate to warehouse configuration and set Incoming Shipments to "Receive, Quality Control, then Store (3 steps)"
3. Confirm `wh_qc_stock_loc_id` and `qc_type_id` are now active

**Steps:**
1. Create a purchase order (or manual receipt) for any product
2. Confirm the receipt (IN picking type); verify `state='confirmed'`
3. Validate the receipt; verify a QC transfer (type `QC`) is automatically created with source=Input location, destination=Quality Control location
4. Validate the QC transfer; verify a Storage transfer (type `STOR`) is automatically created with source=QC location, destination=stock location
5. Validate the Storage transfer; verify product quant is at `lot_stock_id`

**Expected outcomes:**
- Three distinct pickings created for the one-receipt event
- `move_dest_ids` linkage visible on each move (IN→QC, QC→STOR)
- `procure_method` on rule 2 and rule 3 = `make_to_order`

---

### AWT-02: Three-Step Outbound (Pick + Pack + Ship)

**Prerequisites:**
1. Same Multi-Step Routes toggle enabled
2. Set Outgoing Shipments to "Pick, Pack, then Deliver (3 steps)"
3. Confirm `wh_pack_stock_loc_id`, `pack_type_id`, `wh_output_stock_loc_id` are active

**Steps:**
1. Create a sale order (or manual delivery) for a product in stock
2. Confirm the order; verify PICK transfer created (source=stock, dest=pack zone)
3. Validate PICK transfer; verify PACK transfer auto-created (source=pack zone, dest=output location)
4. Validate PACK transfer; verify OUT delivery order ready (source=output location, dest=customer)
5. Validate OUT; verify delivery is done

**Expected outcomes:**
- Three distinct pickings created for the one-delivery event
- `move_dest_ids` linkage: PICK→PACK, PACK→OUT
- OUT picking type `code='outgoing'`

---

### AWT-03: Cancel Propagation Boundary

**Steps:**
1. Follow AWT-01 steps 1-3 (receipt validated, QC transfer created)
2. Cancel the QC transfer
3. Verify the Storage transfer is also cancelled (propagate_cancel=True on inbound route rule 1)
4. Verify no downstream customer-facing move is cancelled (last rule's propagate_cancel forced to False)

---

## Key Source Pointers

| File | Line | Symbol |
|------|------|--------|
| `stock/models/stock_warehouse.py` | 56-61 | `reception_steps` field definition |
| `stock/models/stock_warehouse.py` | 62-67 | `delivery_steps` field definition |
| `stock/models/stock_warehouse.py` | 777-780 | `three_steps` inbound Routing list |
| `stock/models/stock_warehouse.py` | 785-788 | `pick_pack_ship` outbound Routing list |
| `stock/models/stock_warehouse.py` | 823-852 | `_get_rule_values` — procure_method and cancel chaining |
| `stock/models/stock_warehouse.py` | 946-947 | `_update_location_reception` — QC location activation |
| `stock/models/stock_warehouse.py` | 980-988 | `_get_picking_type_update_values` — QC/Store type activation |
| `stock/models/stock_rule.py` | 222-254 | `_run_push` — push move creation with move_dest_ids |
| `stock/models/stock_rule.py` | 668-678 | `_get_push_rule` — location-tree push rule lookup |
| `stock/models/stock_move.py` | 1214-1264 | `_push_apply` — post-confirm push chain trigger |
| `stock/models/res_config_settings.py` | 23-25 | `group_stock_adv_location` prerequisite |
| `stock/views/stock_warehouse_views.xml` | 38-41 | Warehouse form radio widgets (group_adv_location gated) |
| `stock/security/stock_security.xml` | 50-52 | `group_adv_location` security group definition |
