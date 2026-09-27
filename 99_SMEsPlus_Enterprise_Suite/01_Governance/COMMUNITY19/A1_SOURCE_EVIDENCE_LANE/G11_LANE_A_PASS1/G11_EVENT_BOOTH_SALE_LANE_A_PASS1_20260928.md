> **CANDIDATE-ROSTER PILOT — G11 membership is DERIVED, not Boss-confirmed; not Formal Coverage; not a precedent for opening any other G02–G16 group.** See MASTER_DECISION_LOG_G01_20260927.md MD-17/MD-18.

# G11 EVENTS (pilot) — Module `event_booth_sale` — LANE A PASS-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Group | G11 EVENTS (CANDIDATE-ROSTER PILOT; DERIVED membership, not CONFIRMED) |
| Module | `event_booth_sale` |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/event_booth_sale/`) |
| Retrieval | raw.githubusercontent.com at pinned commit; blob SHA-1 verified with `git hash-object` against `git ls-tree` of the same pinned commit |
| Date | 2026-09-28 |
| Scope | PASS-1 breadth: manifest, models, wizard, security CSV, seed data. Views, JS assets, i18n, tests NOT studied. |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |

Clean-room note: neutral WHAT/WHY/RISK abstractions only; no verbatim vendor code reproduced. No runtime proof, no Formal Coverage, no percentages, no GMVQ QID answered. `depends` in section 3 is a dependency relationship only, not a group-membership claim (MD-07/08).

## 1. Evidence Pointer Table (17 blobs)

| Path (addons/event_booth_sale/…) | git blob SHA-1 (fetched, hash-verified) | Purpose |
|---|---|---|
| `__manifest__.py` | 2dc92e01fab8b7f4bdf57e4b3214593c519ccdef | Name "Events Booths Sales", `depends`: `event_booth`, `event_sale`; `auto_install: True` |
| `__init__.py` | 2ae6446f9dc25fe7563ce0c6a4f1cc4904124cc5 | Package init (models, wizard) |
| `data/event_booth_category_data.xml` | dcbd5a75570b60b5f8350684068504fa02f601bb | Attaches product + price to the 3 seeded categories from `event_booth` |
| `data/product_data.xml` | b4e7311a21617e1ed647ac1f88d22d2ec8363069 | Seed "Event Booth" service product (`service_tracking='event_booth'`) |
| `models/__init__.py` | d5a0110f95d5a4a15d24a50cca24edcae69f4c07 | Model import roster |
| `models/account_move.py` | 4c8ae8220f17d8b88e023f774c579e0f990074cf | `account.move` extension: mark booths paid when linked invoice is paid |
| `models/event_booth.py` | d3801a555325662321d27ee7208c635c2d5243be | `event.booth` extension: sale-order link, paid flag, delete guard |
| `models/event_booth_category.py` | a693412224f9a67dcfca032b32dcec4a6715c03e | `event.booth.category` extension: product/price fields |
| `models/event_booth_registration.py` | 4fb4e5a00291860bda2f2f0bffccea6959dcc493 | `event.booth.registration`: pending reservation per sale-order line |
| `models/event_type_booth.py` | 397a6ed4b057f4d29364a741a7c2ffdb5e55e8a0 | `event.type.booth` extension: related product/price |
| `models/product_product.py` | 70c21e426eb0d865f0b096cec26db2ec67bca47b | `product.product` extension: service_tracking guard |
| `models/product_template.py` | bbaa28d6770671ef30643e390cca54d67dd25a0e | `product.template` extension: adds `event_booth` service-tracking option + guard |
| `models/sale_order.py` | 390a2e9ae99942d55d6397ef0500ed08b32ee870 | `sale.order` extension: booth roll-up, confirm-time booth check |
| `models/sale_order_line.py` | 3aad207d79231b40b93e36d50e9d9042a9927a91 | `sale.order.line` extension: pending/confirmed booth selection logic |
| `security/ir.model.access.csv` | e375afb8eb347c524162c8504c330954f117a9f8 | Model ACL (4 rows) |
| `wizard/__init__.py` | c17705e493b3e2c4201d6015cdbcff1b2655292e | Wizard package init |
| `wizard/event_booth_configurator.py` | c53986305cebe34b4e4641c7522ae9845a0679a4 | Transient wizard: pick event/category/booth(s) when adding a booth line to a quote |

Blobs cited: **17**. All returned HTTP 200 and hash-verified against the pinned-commit tree.

## 2. Findings by A1 completion-card section

### 2.1 Manifest / dependencies / purpose
1. WHAT: `event_booth_sale` is the sale bridge for `event_booth`: it lets a booth be sold on a `sale.order`, ties booth availability/payment to the order/invoice lifecycle, and prevents double-booking when multiple sale order lines compete for the same booth. `depends`: `event_booth`, `event_sale`; `auto_install: True` (installs automatically once both are present). (`__manifest__.py`)
2. Backend-only asset bundle (`web.assets_backend`); no frontend/website assets declared in this module. (`__manifest__.py`)

### 2.2 Data — models, inheritance, key fields, identity/uniqueness
3. `event.booth.category` extension adds `product_id` (required, domain `service_tracking='event_booth'`, defaults to the seeded "Event Booth" product), `price`/`price_incl`/`price_reduce`/`price_reduce_taxinc` (computed from the product's list price plus tax/pricelist logic, field-group-restricted to `event.group_event_registration_desk`+), and an `image_1920` that falls back to the linked product's image. `event.type.booth` extension adds related `product_id`/`price`/`currency_id` and extends the template-copy field whitelist to include them. (`models/event_booth_category.py`, `models/event_type_booth.py`)
4. `product.template`/`product.product` gain a new `service_tracking` selection value `event_booth` ("Mark the selected Booth as Unavailable" tooltip), forced to `invoice_policy='order'` on selection, and blacklisted from the generic service-tracking configurator list (`_service_tracking_blacklist`). (`models/product_template.py`, `models/product_product.py`)
5. `event.booth` extension adds `event_booth_registration_ids` (pending reservations), `sale_order_line_registration_ids` (all SO lines that have reserved this booth, field-group-restricted to `sales_team.group_sale_salesman`), `sale_order_line_id`/`sale_order_id` (the final, confirmed sale, same field-group restriction), and `is_paid`. (`models/event_booth.py`)
6. `event.booth.registration` (new model) represents one sale-order-line's pending claim on one booth: `sale_order_line_id` (required, cascade), `event_booth_id` (required), `partner_id` (related to the order's customer), plus contact name/email/phone computed-once from the partner. Identity: unique constraint on `(sale_order_line_id, event_booth_id)` — one reservation row per line per booth, but the same booth can have many registration rows from different order lines (competing reservations), which is the mechanism used to detect and resolve double-booking. (`models/event_booth_registration.py`)
7. `sale.order.line` extension adds `event_booth_category_id`, a computed/inverse `event_booth_pending_ids` (the UI-facing "which booths did the salesperson pick" field, backed by the registration rows), `event_booth_registration_ids`, and `event_booth_ids` (booths actually confirmed to this line). `sale.order` extension adds `event_booth_ids`/`event_booth_count` roll-ups. (`models/sale_order_line.py`, `models/sale_order.py`)
8. New transient wizard `event.booth.configurator`: given a product/sale-order-line context, requires the user to pick an `event_id`, then an `event_booth_category_id` (reset whenever the event changes), then one or more `event_booth_ids` (reset whenever event or category changes); a constraint forbids confirming with zero booths selected. (`wizard/event_booth_configurator.py`)

### 2.3 Business rules / states / lifecycle / exceptions
9. Reservation-to-confirmation flow: choosing booths on a quote line only creates `event.booth.registration` rows (pending, not yet exclusive) via `_inverse_event_booth_pending_ids`; a booth becomes actually reserved only when the sale order is confirmed. `sale.order.action_confirm()` is overridden to (a) block confirmation entirely if any event-booth line has no booths configured (`ValidationError` listing the offending line descriptions) and (b) call `_update_event_booths()` on the order lines. (`models/sale_order.py`, `models/sale_order_line.py`)
10. `_update_event_booths()`: for each event-booth line with pending-but-not-yet-confirmed booths, it first re-checks availability (`ValidationError` if any pending booth has since become unavailable — i.e. a race where two orders both picked the same booth), then calls `event.booth.registration.action_confirm()` (sudo) on the registrations, which in turn calls `event.booth.action_confirm()` on each booth (marking it `unavailable`) and then `_cancel_pending_registrations()`. That method finds every *other* pending registration on the same booth(s), unlinks them, and cancels (`_action_cancel`) their parent sale orders while posting a chatter message on each cancelled order naming the lost booths. WHY: this is the double-booking-resolution mechanism — first order to confirm wins the booth, every other order that had reserved the same booth is auto-cancelled with an explanation. RISK: an entire sale order is cancelled (not just the conflicting line) if it loses a booth race; downstream automation (invoicing, other lines on that order) is affected. (`models/sale_order_line.py`, `models/event_booth_registration.py`)
11. `_update_event_booths(set_paid=True)` is also invoked from `account.move._invoice_paid_hook()`: when an invoice for booth-selling order lines is paid, every confirmed booth on those lines is marked `is_paid=True` via `event.booth.action_set_paid()`. WHY: booth payment status is invoice-driven, not order-confirmation-driven. (`models/account_move.py`, `models/event_booth.py`)
12. A booth cannot be deleted once linked to a sale order (`_unlink_except_linked_sale_order`, sudo-checked, `UserError` naming the booths). (`models/event_booth.py`)
13. Product/service-tracking integrity: a product's `service_tracking` cannot be changed away from `event_booth` (on either the template or a specific variant) once any `event.booth.category` references it, on both `product.product` and `product.template`, each raising a `ValidationError` naming the linked category. (`models/product_product.py`, `models/product_template.py`)
14. Pricing on the quote line: `_get_display_price()` is overridden so a booth line's displayed price is the sum of the selected booths' category prices (tax-reduced or plain, depending on whether the pricelist item shows a discount), converted to the order's currency — this bypasses the normal single-product pricelist computation for booth lines. The line's auto-generated description also switches to a multi-line "event + booth names" format instead of the standard product description, and template-based name rewriting is suppressed while booths are selected. (`models/sale_order_line.py`)
15. A quote line cannot mix booths from two different events (`_check_event_booth_registration_ids` constraint on `event_booth_registration_ids`, checked via the linked booths' `event_id`). Changing the line's product resets the chosen event if the new product doesn't belong to the currently pending booths' categories; changing the event resets the pending booths — both onchange guards intended to keep the line internally consistent before confirmation. (`models/sale_order_line.py`)
16. Data migration helper `_init_column` on `event.booth.category`: when this module is installed onto a database that already has `event.booth.category` rows (existing `event_booth` install), it back-fills the newly-required `product_id` column for every existing row, creating a generic fallback product if the seeded one isn't found yet. RISK: a raw SQL `UPDATE` runs directly against the table during module installation, bypassing ORM validation for that one-time backfill. (`models/event_booth_category.py`)

### 2.4 Security
17. ACL (4 rows): `event.booth.registration` — full CRUD for `sales_team.group_sale_salesman` and for `event.group_event_user`, read-only for `event.group_event_registration_desk`. `event.booth.configurator` (the wizard) — CRUD-minus-unlink for salesmen only. No explicit ACL row is declared here for `event.booth.category`'s new fields or for `product.template`'s new selection value — those are covered by the base `product`/`event_booth` ACLs, with the price/product fields restricted at field level (`groups="event.group_event_registration_desk"`) rather than via a separate ACL row. (`security/ir.model.access.csv`, `models/event_booth_category.py`)
18. `event.booth.sale_order_line_registration_ids`, `sale_order_line_id`, `sale_order_id` are field-group-restricted to `sales_team.group_sale_salesman` — an event-only user (without the sales group) cannot see which sale order booked a booth, only that it is unavailable. (`models/event_booth.py`)
19. No dedicated `ir.rule` (record rule) found in this module; multi-company scoping for the new `event.booth.registration` model is not source-evidenced here — relies (if at all) on the `sale.order`/`event.event` company rules reached transitively through relations, not verified. RISK flagged for A1/A2.

### 2.5 UI surfaces (names only, not fetched/read)
20. `views/`: `sale_order_views.xml`, `event_type_booth_views.xml`, `event_booth_category_views.xml`, `event_booth_registration_views.xml`, `event_booth_views.xml`, `wizard/event_booth_configurator_views.xml`. File presence only.

### 2.6 Jobs / config / integrations
21. No crons and no `ir.config_parameter` reads found. Integration points are purely intra-Odoo: `account.move` (invoice-paid hook), `sale.order`/`sale.order.line` (confirm hook, product-catalog domain exclusion of booth products via `_get_product_catalog_domain`), and `product.template`/`product.product` (new service-tracking type). (`models/account_move.py`, `models/sale_order.py`, `models/product_template.py`)

## 3. Cross-module edges
22. Depends on `event_booth` and `event_sale` (dependency relationship only, not group membership per MD-07/08); both are in this pilot's DERIVED G11 roster. `auto_install: True` means this bridge module installs itself automatically whenever both are present, without being separately chosen — worth flagging to A1 since its presence in a database is a *consequence* of the other two, not an independent installation decision. (`__manifest__.py`)
23. Reuses `sales_team.group_sale_salesman` (from the `sale` app, itself pulled in transitively via `event_sale`) and `event.group_event_registration_desk`/`event.group_event_user` (from `event`) for field/ACL scoping. (`security/ir.model.access.csv`, `models/event_booth.py`)
24. Touches `account.move` (from `account`, a `sale`/`event_sale` dependency) purely through a hook override — no new fields added to invoices. (`models/account_move.py`)

## 4. Evidence gaps / contradictions
- G1: Six view/wizard-view XML files not read.
- G2: JS assets (`static/src/js/event_booth_configurator_controller.js`, `sale_product_field.js`) not fetched.
- G3: i18n and tests not fetched.
- No contradictions observed between manifest, `__init__.py` roster, and fetched files. All 17 fetches returned HTTP 200 and hash-verified.

## 5. Limitations
Static source only, single pinned commit, no runtime/DB observation. CANDIDATE-ROSTER PILOT under MD-18 — G11 membership of this module is DERIVED, not Boss-confirmed. No GMVQ QID answered; no Formal Coverage claimed.
