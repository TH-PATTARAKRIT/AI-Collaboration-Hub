# U105 — pos_restaurant: Floor/Table Management + Course Ordering
**Unit**: U105 | **Module**: pos_restaurant | **GAP**: GAP-038
**Date**: 2026-10-02 | **Status**: GATE-PASS

## Floor Plan Architecture

The `restaurant.floor` model is the server-side persistence record for a POS restaurant floor plan canvas. It supports ordering by `sequence, name` and can be shared across multiple `pos.config` instances via a Many2many relation. Visual fields include a binary background image, CSS background colour, and an integer sequence (default 1) for display ordering. The model implements the `pos.load.mixin` protocol for lazy-loading into POS sessions.

Structural changes to floor assignments (modifying `pos_config_ids` or deactivating a floor) are blocked while any linked POS configuration has an active session. Deletion is similarly blocked. Floor creation from the OWL frontend is handled by `sync_from_ui`, which returns a JSON-serialisable dict with id, name, background_color, table_ids, and sequence. Floor deactivation via `deactivate_floor(session_id)` requires no draft orders to exist for the floor in that session before it iterates child tables to `active=False`.

## Table Architecture

The `restaurant.table` model also implements `pos.load.mixin`. Each table requires a floor reference (indexed foreign key), a table number (integer, required), and a shape (square or round, required). Canvas geometry is stored as four Float fields: horizontal and vertical position from the origin, plus width and height in pixels. Additional metadata includes seat count, CSS colour, and a self-referential `parent_id` for table grouping.

Table display names are computed from floor name + table number. Session load domain filters to active tables belonging to floors configured for the session. A draft-order guard prevents deletion or deactivation when orders remain open. The `set_parent_id` method performs cycle detection via `_has_cycle('parent_id')` before assigning a group parent, reverting to the previous parent if a cycle would result.

## Order and Config Extensions

`pos.order` gains three fields in restaurant mode: a Many2one to `restaurant.table` (read-only, indexed), an integer guest count, and a One2many to `restaurant.order.course` records. Order recovery on client reconnect uses a compound domain: UUID match, OR the combination of matching table, draft state, and config identity.

`pos.config` gains `iface_splitbill`, `iface_printbill`, `floor_ids`, `set_tip_after_payment`, and `default_screen` (tables or register). The `floor_ids` field is in the forbidden-change-fields list, preventing direct write outside of module toggle or the default-floor setup helper. On first activation of restaurant mode, `_setup_default_floor` creates one floor (named from the company) and one table (number 1, 130×130 px at position 100/100).

## Course Ordering Persistence

Course ordering is fully persisted server-side, not transient or JS-only. The `restaurant.order.course` model stores a fired boolean, auto-assigned fired timestamp (idempotent — not overwritten on subsequent writes), a UUID4 key (copy=False), a display index, the parent order reference (cascade delete), and a One2many to the order lines assigned to the course. The POS session loads course records scoped to orders already loaded in the session payload.

## Bill Splitting Architecture

Bill splitting (`iface_splitbill`) exists as a Python config Boolean only. The actual split-order operation — creating a new order from a subset of lines — is implemented exclusively in the JavaScript/OWL frontend. No Python model, wizard, or server method for splitting orders exists.

## Odoo 19 Restaurant Onboarding

Odoo 19 introduces `pos.preset` (takeIn/takeOut/delivery presets). On restaurant config creation, `use_presets`, `default_preset_id`, and `available_preset_ids` are set, and `group_pos_preset` is implied for standard users when presets are enabled.

## Session Loading

At POS session open, `_load_pos_data_models` appends `restaurant.floor`, `restaurant.table`, and `restaurant.order.course` to the model loading list when `module_pos_restaurant=True`. Preparation change tracking serialises current order lines to a JSON dict keyed by UUID for kitchen display synchronisation.
