# U165 — product_expiry: Restricted Technical Evidence
**Unit:** U165 | **Module:** product_expiry | **Group:** G06 | **Priority:** P2
**Research Level:** L3 (Deep — module PRESENT, full source read)
**Date:** 2026-10-02

---

## 1. Module Identity

- **Technical name:** `product_expiry`
- **Display name:** Products Expiration Date
- **Category:** Supply Chain/Inventory
- **Depends:** `['stock']`
- **License:** LGPL-3
- **Author:** Odoo S.A.
- **Post-init hook:** `_enable_tracking_numbers`
- **Source manifest:** `odoo/addons/product_expiry/__manifest__.py`

---

## 2. Date Fields on stock.lot (production_lot.py)

Model inherits `stock.lot`. Fields added:

| Field | Type | Key Detail |
|---|---|---|
| `use_expiration_date` | Boolean (related) | Related to `product_id.use_expiration_date` |
| `expiration_date` | Datetime (computed, store, readonly=False) | Computed from `product_id`; auto-set as `now() + expiration_time days` |
| `use_date` | Datetime (computed, store, readonly=False) | "Best before Date" — `expiration_date - use_time days` |
| `removal_date` | Datetime (computed, store, readonly=False) | `expiration_date - removal_time days`; drives FEFO ordering |
| `alert_date` | Datetime (computed, store, readonly=False) | `expiration_date - alert_time days` |
| `product_expiry_alert` | Boolean (computed) | True when `expiration_date <= now()` |
| `product_expiry_reminded` | Boolean | Marks that activity has already been scheduled |

**Compute logic (`_compute_expiration_date`):** sets `expiration_date = now() + product.expiration_time` when `use_expiration_date` is True and `expiration_date` not already set.

**Compute logic (`_compute_dates`):** derives `use_date`, `removal_date`, `alert_date` from template integer offsets. On creation uses template offsets directly; on subsequent changes to `expiration_date`, shifts each date by the time delta.

**Display name override (`_compute_display_name`):** with context `formatted_display_name`, appends "--Expired--" or "--Expire on <date>--" suffix to lot name.

---

## 3. Product Template Fields (product_product.py / ProductTemplate)

| Field | Type | Purpose |
|---|---|---|
| `use_expiration_date` | Boolean | Gate flag; disabled automatically when tracking is set to 'none' |
| `expiration_time` | Integer (days) | Days after receipt before goods become dangerous |
| `use_time` | Integer (days) | Days before expiration_date when deterioration begins |
| `removal_time` | Integer (days) | Days before expiration_date to remove from Fresh On Hand |
| `alert_time` | Integer (days) | Days before expiration_date to raise alert |

`write()` override: when `tracking = 'none'`, forces `use_expiration_date = False`.

---

## 4. stock.move_line Expiry Fields (stock_move_line.py)

- `expiration_date` — Datetime, computed from `lot_id.expiration_date` or auto-calculated from `picking_id.scheduled_date + product.expiration_time` for new-lot picking types
- `removal_date` — Datetime, readonly=False, computed from `lot_id.removal_date` or `expiration_date - product.removal_time`
- `is_expired` — Boolean, related to `lot_id.product_expiry_alert`
- `use_expiration_date` — Boolean, related to `product_id.use_expiration_date`
- `_auto_init()`: creates `expiration_date` and `removal_date` columns directly (avoids MemoryError on large installs)
- `_prepare_new_lot_vals()`: propagates `expiration_date` when creating a new lot from a move line

---

## 5. Receipt Auto-population (stock_move.py)

- `action_generate_lot_line_vals()`: when generating lot lines at receipt, sets `expiration_date = scheduled_date + product.expiration_time` if product uses expiration dates
- `_generate_serial_move_line_commands()`: same auto-population for serial numbers; sets `expiration_date = today + expiration_time`
- `_convert_string_into_field_data()`: parses pasted text at serial entry — if a valid date string is parsed and product does NOT use expiration date, returns `"ignore"` to skip the date
- `_update_reserved_quantity()` and `_get_available_quantity()`: when `use_expiration_date`, passes `with_expiration=self.date` context to exclude lots past removal date from reservation

---

## 6. Expired Lot Blocking on Picking Validation (stock_picking.py)

- `_pre_action_done_hook()`: intercepts picking validation; calls `_check_expired_lots()` unless context key `skip_expired` is set
- `_check_expired_lots()`: filters `move_line_ids` for any lot where `product_expiry_alert=True` OR `removal_date <= now()`; returns those pickings
- `_action_generate_expired_wizard()`: opens `expiry.picking.confirmation` wizard (transient model) with expired lots listed
- **NOT a hard block**: the wizard presents two actions:
  - `process()` — confirms delivery of expired lots (adds `skip_expired=True` to context)
  - `process_no_expired()` — unlinks expired move lines and validates the rest

---

## 7. Expiry Alert Scheduler (stock_rule.py + production_lot.py)

- `StockRule._run_scheduler_tasks()` calls `stock.lot._alert_date_exceeded()` as a scheduler task
- `_get_scheduler_tasks_to_do()` increments task count by 1 (so progress tracking accounts for this step)
- `_alert_date_exceeded()` logic:
  1. Finds lots where `alert_date <= today` AND `product_expiry_reminded = False`
  2. Filters to only lots with positive on-hand quantity in internal locations
  3. Schedules a `mail.mail_activity_data_todo` activity on each lot, assigned to `product.responsible_id` or SUPERUSER
  4. Sets `product_expiry_reminded = True` — one-shot: no repeat activity generated

---

## 8. FEFO Removal Strategy Integration (stock_quant.py)

- `_get_removal_strategy_order('fefo')` returns `'removal_date, in_date, id'` — quants sorted by `removal_date` ascending, then receipt date, then id
- FEFO record registered in `data/product_expiry_data.xml`: `product.removal` record with `method='fefo'`
- `available_quantity` compute override: for quants where `use_expiration_date=True` and `removal_date <= now()`, forces `available_quantity = 0` (expired stock invisible to demand)
- GS1 barcode generation: `_get_gs1_barcode()` prepends AI `17` (expiry) and AI `15` (best-before) segments when `use_expiration_date` is enabled

---

## 9. stock.quant Expiry Denormalization

- `expiration_date` — Datetime (related, stored) from `lot_id.expiration_date`
- `removal_date` — Datetime (related, stored) from `lot_id.removal_date`
- `use_expiration_date` — Boolean (related) from `product_id.use_expiration_date`
- `_set_view_context()` adds `show_removal_date=True` context when product uses expiration dates

---

## 10. Configuration (res_config_settings.py)

- `group_expiry_date_on_delivery_slip` — Boolean: shows expiration dates on delivery slip reports
- Onchange: enabling lot tracking (`group_stock_production_lot`) auto-enables `module_product_expiry`
- Onchange: disabling lot-on-delivery-slip also disables expiry-date-on-delivery-slip

---

## 11. Wizard: Confirm Expiry (wizard/confirm_expiry.py)

- Model: `expiry.picking.confirmation`
- `lot_ids` and `picking_ids` — M2M read-only
- `description` — computed warning message (single vs multiple expired lots)
- `show_lots` — computed; shows lot list in view when >1 expired lot
- `process()` — validates picking with expired lots (skip_expired=True context)
- `process_no_expired()` — removes expired move lines (those with `removal_date < now()` and `use_expiration_date`) then validates

---

## 12. File Inventory

| File | Purpose |
|---|---|
| `models/production_lot.py` | Core lot date fields + alert scheduling method |
| `models/product_product.py` | Product template time offsets + `use_expiration_date` gate |
| `models/stock_move.py` | Auto-population at receipt, reservation context |
| `models/stock_move_line.py` | Move-line expiry fields + new-lot propagation |
| `models/stock_picking.py` | Validation hook + expired lot wizard trigger |
| `models/stock_quant.py` | FEFO sort order, available qty zeroing, GS1 barcode |
| `models/stock_rule.py` | Scheduler task integration |
| `models/res_config_settings.py` | Settings toggle for delivery slip |
| `wizard/confirm_expiry.py` | Soft-block confirmation wizard |
| `data/product_expiry_data.xml` | FEFO product.removal record |

---

## 13. Key Architectural Finding

The expired-lot check is a **soft block**, not a hard block. Validation is intercepted and the user is presented a wizard; they can choose to proceed with expired lots (context `skip_expired=True` bypasses the check) or strip the expired lines and validate the remainder. This is a deliberate design allowing overrides in urgent scenarios.
