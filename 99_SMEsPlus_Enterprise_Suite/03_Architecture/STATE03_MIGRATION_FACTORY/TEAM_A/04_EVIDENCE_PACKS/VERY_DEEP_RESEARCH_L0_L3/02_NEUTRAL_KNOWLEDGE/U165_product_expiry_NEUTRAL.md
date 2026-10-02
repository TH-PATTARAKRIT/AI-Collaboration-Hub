# U165 — product_expiry: Neutral Knowledge
**Unit:** U165 | **Module:** product_expiry | **Group:** G06 | **Priority:** P2
**Date:** 2026-10-02

---

## Overview

The product_expiry module extends Odoo's warehouse management with lifecycle date tracking on lot and serial numbers. It supports four date dimensions per lot — an expiration cutoff, a best-before threshold, a removal date, and an alert date — all derived automatically from configurable integer offsets set at the product-template level. The module also registers the First Expiry First Out (FEFO) removal strategy, which orders stock quants by removal date during reservation so the stock closest to expiry is consumed first.

---

## VDR Claims Table

| # | Claim | Source File | Lines | Evidence Quality | Confidence | L-Level | Contradictions | Notes |
|---|---|---|---|---|---|---|---|---|
| C01 | Module depends solely on `stock` with no additional module dependencies beyond core | `__manifest__.py` | 5 | Direct source read | HIGH | L3 | None | Post-init hook enables tracking numbers |
| C02 | The `use_expiration_date` Boolean on product.template gates whether any expiry date logic applies to a product; it is forced to False when lot tracking is removed | `models/product_product.py` | 38, 57-58 | Direct source read | HIGH | L3 | None | `write()` override enforces this |
| C03 | Four integer offset fields on product.template (`expiration_time`, `use_time`, `removal_time`, `alert_time`) express each date dimension as days relative to expiration date | `models/product_product.py` | 41-53 | Direct source read | HIGH | L3 | None | All in days |
| C04 | `stock.lot` gains four stored datetime fields: `expiration_date`, `use_date` (best before), `removal_date`, and `alert_date`; all are writable after computation | `models/production_lot.py` | 12-20 | Direct source read | HIGH | L3 | None | `readonly=False` allows manual override |
| C05 | The lot's `expiration_date` is automatically set to the current datetime plus the product's `expiration_time` offset when the lot is first created and the product uses expiration dates | `models/production_lot.py` | 51-56 | Direct source read | HIGH | L3 | None | Only sets if not already set |
| C06 | The three derived dates (`use_date`, `removal_date`, `alert_date`) on a lot are recalculated when `expiration_date` changes, either by applying template offsets fresh on creation or by shifting existing dates by the same delta | `models/production_lot.py` | 58-79 | Direct source read | HIGH | L3 | None | Handles both create and edit cases |
| C07 | A lot's `product_expiry_alert` flag becomes True when `expiration_date` is in the past (less than or equal to the current datetime) | `models/production_lot.py` | 41-48 | Direct source read | HIGH | L3 | None | Drives picking soft-block |
| C08 | Stock move lines carry their own stored `expiration_date` and `removal_date`, propagated from the linked lot or auto-computed from scheduled date plus product offset at receipt for new-lot picking types | `models/stock_move_line.py` | 13-17, 34-55 | Direct source read | HIGH | L3 | None | Column pre-created in `_auto_init` to avoid memory errors |
| C09 | At receipt, the system automatically proposes an expiration date on move lines for products that use expiry tracking, calculated as the picking's scheduled date plus the product's expiration-time offset | `models/stock_move.py` | 19-39 | Direct source read | HIGH | L3 | None | Both `action_generate_lot_line_vals` and `_generate_serial_move_line_commands` handle this |
| C10 | Picking validation is intercepted before completion: if any move line references an expired lot or a lot past its removal date, a confirmation wizard is displayed asking whether to proceed | `models/stock_picking.py` | 11-48 | Direct source read | HIGH | L3 | None | Soft block — not a hard error |
| C11 | The expired-lot check is a soft block: users may either confirm delivery of expired goods (proceeds with a context flag) or strip the expired move lines and validate the remainder | `wizard/confirm_expiry.py` | 37-52 | Direct source read | HIGH | L3 | None | `skip_expired` context key bypasses re-check |
| C12 | The scheduler task hook in `stock.rule` calls `stock.lot._alert_date_exceeded()` as part of the standard replenishment scheduler run, scheduling a to-do activity on lots whose alert date has passed | `models/stock_rule.py` | 8-17 | Direct source read | HIGH | L3 | None | One-shot: `product_expiry_reminded` prevents repeat activities |
| C13 | Alert activities are assigned to the product's responsible user or fall back to the superuser; once scheduled, the lot's `product_expiry_reminded` flag prevents further duplicate activities | `models/production_lot.py` | 81-107 | Direct source read | HIGH | L3 | None | Only processes lots with positive on-hand internal stock |
| C14 | The FEFO removal strategy orders stock quants by `removal_date` ascending, then by receipt date (`in_date`), then by id, ensuring the lot closest to its removal deadline is consumed first | `models/stock_quant.py` | 25-28 | Direct source read | HIGH | L3 | None | Strategy method registered as `fefo` |
| C15 | A `product.removal` record with method `fefo` is seeded by the module's data XML, registering the FEFO strategy in the system without manual setup | `data/product_expiry_data.xml` | 3-6 | Direct source read | HIGH | L3 | None | Record ID: `removal_fefo` |
| C16 | Quants belonging to lots past their removal date report zero available quantity, effectively hiding expired stock from demand availability calculations | `models/stock_quant.py` | 30-36 | Direct source read | HIGH | L3 | None | Only applies when `use_expiration_date` is True |
| C17 | Reservation and availability queries for expiry-tracked products pass a `with_expiration` date context, excluding quants whose removal date precedes the move's own scheduled date | `models/stock_move.py` | 87-95 | Direct source read | HIGH | L3 | None | Applied in `_update_reserved_quantity` and `_get_available_quantity` |
| C18 | GS1 barcode generation for stock quants incorporates the lot's expiration date (AI `17`) and best-before date (AI `15`) as barcode segments when expiry tracking is enabled | `models/stock_quant.py` | 15-22 | Direct source read | HIGH | L3 | None | Standard GS1 application identifiers |
| C19 | Enabling lot-number tracking in inventory settings automatically activates the product_expiry module, coupling expiry tracking to lot management as the default behaviour | `models/res_config_settings.py` | 18-22 | Direct source read | HIGH | L3 | None | Via `_onchange_group_stock_production_lot` |
| C20 | The lot's display name in selection dropdowns can optionally show "--Expired--" or "--Expire on <date>--" suffixes when a `formatted_display_name` context flag is active | `models/production_lot.py` | 26-39 | Direct source read | HIGH | L3 | None | Helps users identify expired lots during operations |

---

## Summary Assessment

- **Module status:** PRESENT and fully active
- **Total claims verified:** 20
- **All claims:** L3 (direct source read, no inference required)
- **No contradictions found**
- **Key capability:** Comprehensive 4-date-dimension tracking per lot, FEFO strategy, soft-block on expired-lot shipments, scheduler-driven alert activities, GS1 barcode integration
