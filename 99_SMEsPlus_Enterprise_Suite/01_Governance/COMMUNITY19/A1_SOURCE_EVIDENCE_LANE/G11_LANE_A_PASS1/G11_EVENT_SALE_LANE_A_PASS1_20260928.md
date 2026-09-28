> **CANDIDATE-ROSTER PILOT — G11 membership is DERIVED, not Boss-confirmed; not Formal Coverage; not a precedent for opening any other G02–G16 group.** See MASTER_DECISION_LOG_G01_20260927.md MD-17/MD-18.

# G11 EVENTS (pilot) — Module `event_sale` — LANE A PASS-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Group | G11 EVENTS (CANDIDATE-ROSTER PILOT; DERIVED membership, not CONFIRMED) |
| Module | `event_sale` |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/event_sale/`) |
| Retrieval | raw.githubusercontent.com at pinned commit; blob SHA-1 verified with `git hash-object` against `git ls-tree` of the same pinned commit |
| Date | 2026-09-28 |
| Scope | PASS-1 breadth: manifest, models, report model (SQL view definition read), wizards, security CSV/XML. Views, mail-template body, JS assets, demo data, i18n, tests NOT studied. |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |

Clean-room note: neutral WHAT/WHY/RISK abstraction only; no verbatim vendor code reproduced beyond short field/method-name pointers and the report model's own field list (a schema description, not business logic). No runtime proof, no Formal Coverage, no percentages, no GMVQ QID answered. `depends` in section 3 is a dependency relationship only, not a group-membership claim (MD-07/08).

## 1. Evidence Pointer Table (18 blobs)

| Path (addons/event_sale/…) | git blob SHA-1 (fetched, hash-verified) | Purpose |
|---|---|---|
| `__manifest__.py` | 4f116f541e8a8690ac3f7daf25099d1ff6fa1d52 | Name "Events Sales", depends `event_product`+`sale_management`, `auto_install: True` |
| `__init__.py` | de3c67453a778d3d4bd7a2aff54380057fd5dd14 | Package init |
| `data/event_sale_data.xml` | 69edfed87526b3a01883a27f1630b1bace72809a | Seed data (not deeply read) |
| `data/mail_templates.xml` | 3cef762bc3728b57c3ef55f2836dc04c23b07377 | Mail template(s) (not deeply read) |
| `models/__init__.py` | 47178d89be0d7feab05df682cadbdd8c16454320 | Model import roster |
| `models/event_event.py` | 9f2f1274a5ae6938c80e48b1380357a545416d6d | `event.event` extension: linked sale-order lines, currency-converted revenue total |
| `models/event_registration.py` | 82d36dde4f6c8d8679e61884f297eeafff7f3e5e | `event.registration` extension: SO link, state/sale_status computation, UTM sync |
| `models/event_ticket.py` | dbf8ee2109723cfa0e524e2d3ed7c2dd4eb810de | `event.event.ticket` extension: SO-line description override |
| `models/product_template.py` | bf75ae80adf6c8b2d908c80b794aaf340f33e29f | `product.template` extension: tooltip + invoice-policy onchange for `event` tracking |
| `models/sale_order.py` | 560eea73ab76dd6742b30757e479a7838db15b1a | `sale.order` extension: partner sync, confirm-time registration init, attendee count |
| `models/sale_order_line.py` | 3bc5f2fc35031e197d9e3bc5df8fc5215d95a828 | `sale.order.line` extension: event/slot/ticket fields, registration creation, pricing |
| `report/__init__.py` | 9608c798dfcc018fc1d6e53023e498861282d8e0 | Report package init |
| `report/event_sale_report.py` | 2ccac8a60be711c661c95cfcb3a6a260f9a04b24 | `event.sale.report`: SQL-view-backed analysis model (registrations × sale data) |
| `security/event_security.xml` | dfb2911a32adf109f5cd49220b03e2c95e924444 | Grants `sales_team.group_sale_salesman` the event registration-desk group (implied_ids) |
| `security/ir.model.access.csv` | 1c5cf1cd81ed338fa81f589f4ad93a14026572ea | Model ACL (4 rows) |
| `security/ir_rule.xml` | 26d54d7f1bacb814399c75595f07c07c22f67d03 | Multi-company `ir.rule` on the sale report view |
| `wizard/__init__.py` | b2eda10be39632bfdc252bc77a89c6600d12339d | Wizard package init |
| `wizard/event_configurator.py` | 4c96e9231d04d16c85cba435085311e8b631811b | Transient wizard: pick event/slot/ticket when adding an event line to a quote |
| `wizard/event_edit_registration.py` | 534743858f9d69d815b47f0e8901f88476fb8025 | Transient wizard: edit/create attendee details at order-confirmation time |

Blobs cited: **18**. All returned HTTP 200 and hash-verified against the pinned-commit tree.

## 2. Findings by A1 completion-card section

### 2.1 Manifest / dependencies / purpose
1. WHAT: `event_sale` connects `event`'s registration model to `sale.order`/`sale.order.line`, so that selling an "event" service product (`service_tracking='event'`, defined in `event_product`) automatically creates and manages attendee registrations, tracks per-event revenue, and reports on ticket sales. `depends`: `event_product`, `sale_management`; `auto_install: True` (installs automatically once both are present, consistent with the other bridge modules in this pilot). (`__manifest__.py`)
2. Backend + test-tour asset bundles only; a `report/` package provides an analysis (BI-style) model backed by a raw SQL view rather than a printed document. (`__manifest__.py`, `report/event_sale_report.py`)

### 2.2 Data — models, inheritance, key fields, identity/uniqueness
3. `sale.order.line` extension adds `event_id` (computed/store/precompute, reset to `False` if the line's product isn't one of the event's ticket products), `event_slot_id`/`event_ticket_id` (computed/store, reset together whenever `event_id` changes so they always stay consistent with it), `is_multi_slots` (related), `registration_ids` (one2many back-reference). (`models/sale_order_line.py`)
4. `sale.order` extension adds `attendee_count` (computed, excludes cancelled registrations). (`models/sale_order.py`)
5. `event.registration` extension adds `sale_order_id`/`sale_order_line_id` (both `ondelete='cascade'`, not copied), overrides the base `state` field's default to `None` (computed instead, precompute), and adds `utm_campaign_id`/`utm_source_id`/`utm_medium_id` as computed-from-the-order fields (falling back to whatever value was already set if the order has none). (`models/event_registration.py`)
6. `event.event` extension adds `sale_order_lines_ids` (field-group-restricted to `sales_team.group_sale_salesman`) and a computed, currency-converted `sale_price_total` (same restriction). (`models/event_event.py`)
7. `event.sale.report` (new, `_auto=False`, backed by a hand-written SQL view joining `event_registration`/`event_event`/`event_slot`/`event_event_ticket`/`sale_order`/`sale_order_line`): exposes per-registration sale price and untaxed price (converted from the order's currency using the order's own `currency_rate`, i.e. the rate frozen at order time, not "today"), event/ticket/slot identifiers, registration and sale-order state, and a copy of `sale_status`. Built with extensible `_with_clause`/`_select_clause`/`_from_clause`/`_group_by_clause` hooks presumably meant for downstream modules to extend the query (structural observation, not verified against another module here). (`report/event_sale_report.py`)
8. Two transient wizards: `event.event.configurator` (event/slot/ticket picker used when adding an event product to a quote, with a constraint that the chosen ticket/slot must actually belong to the chosen event) and `registration.editor`/`registration.editor.line` (lets a user review/complete per-attendee name/email/phone for every unit sold on a confirmed order, for both already-existing and not-yet-created registrations, before finalizing). (`wizard/event_configurator.py`, `wizard/event_edit_registration.py`)

### 2.3 Business rules / states / lifecycle / exceptions
9. Registration state/sale_status computation (`event.registration._compute_registration_status`, overriding the `_has_order`/base compute contract established in `event_product`): grouped per linked sale order — if the order is cancelled, its registrations become `state='cancel'`; if the order's total is zero, registrations are `sale_status='free'` and any draft/unset state becomes `open`; otherwise, registrations belonging to a confirmed (`state='sale'`) order become `sale_status='sold'` and (if previously draft/cancel) `state='open'`, while the rest become `sale_status='to_pay'` and (if not already sold/cancelled) `state='draft'`. Registrations with no linked sale order fall through to `event_product`'s simpler default (`free`/`open`). WHY: unpaid-order registrations are deliberately held in `draft` (not counted against seat limits in the normal open/done sense) until payment or an explicit backend override — RISK: A1/A2 should confirm whether `draft` registrations are excluded from `event.event`'s seat-availability computation (evidenced separately in `event`'s file) as intended, since an unpaid pending order could otherwise appear to consume seats. (`models/event_registration.py`)
10. Order confirmation guard: `sale.order.action_confirm()` is overridden to block confirmation (`ValidationError` naming the offending lines) if any event-service line lacks a configured `event_id`, then calls `_init_registrations()` to create the correct number of registration stubs per line (`product_uom_qty` minus any already-existing non-cancelled registrations) — paid single-order confirmations start attendees in `draft` specifically so the attendee-detail wizard can be used before the registrations are "real," while free lines go straight to a state resolved by the compute above. A single-order confirmation additionally returns a redirect action to the attendee-registration screen instead of the normal post-confirm result. (`models/sale_order.py`, `models/sale_order_line.py`)
11. Line-level consistency guard: a quote line selling an event-tracked product must have both an event and a ticket (and, if the event is multi-slot, a slot too) or it cannot be validated (`@api.constrains`, `ValidationError`). (`models/sale_order_line.py`)
12. Registration/order data sync: creating or writing a registration with a `sale_order_line_id` pulls partner/event/slot/ticket/order identifiers from that line (`_synchronize_so_line_values`), explicitly avoiding assigning a public-portal user as the registration's own partner (kept blank instead) while still respecting portal workflows; writing the order's `partner_id` propagates it (sudo) to every linked registration. Changing a confirmed registration's slot or ticket after the fact triggers a chatter warning-activity on the sale order for the responsible salesperson/event owner, naming the old vs. new value. (`models/event_registration.py`, `models/sale_order.py`)
13. Pricing on the quote line mirrors the pattern seen in `event_booth_sale`: `_get_display_price()` returns the ticket's `price_reduce` or plain `price` (depending on whether the pricelist item shows a discount), converted to the order's currency; the auto-generated line description is overridden to use the ticket's (or its product's) description plus the slot name instead of the generic product description, and template-based name rewriting is suppressed while a ticket is selected. (`models/sale_order_line.py`, `models/event_ticket.py`)
14. `product.template` extension forces `invoice_policy='order'` when `service_tracking` is set to `event` (mirroring `event_booth_sale`'s and `event_product`'s own onchange for their respective tracking values) and supplies a tooltip ("Create an Attendee for the selected Event"). (`models/product_template.py`)

### 2.4 Security
15. ACL (4 rows): `registration.editor`/`registration.editor.line` and `event.event.configurator` — CRUD-minus-unlink for `sales_team.group_sale_salesman` (transient wizards, no unlink needed); `event.sale.report` — read-only for `event.group_event_manager` only (an analysis view restricted to event managers, not exposed to plain event users or salesmen). (`security/ir.model.access.csv`)
16. `security/event_security.xml` grants every `sales_team.group_sale_salesman` member the `event.group_event_registration_desk` group via `implied_ids` — i.e. installing this bridge module widens the permission set of an existing group (every salesperson automatically gains base event-desk read access) rather than only adding new, separately-scoped groups. RISK: this is a source-confirmed, install-time privilege widening of a pre-existing group, worth flagging distinctly from the additive-only patterns seen in the other `event_*` bridge modules. (`security/event_security.xml`)
17. One `ir.rule`: `event.sale.report` is scoped to `company_id in company_ids + [False]` (multi-company). No record rule is declared for `event.registration`'s new SO-linked fields, `sale.order.line`'s new event fields, or the wizards — those rely on the underlying `sale.order`/`event.registration` rules already established in `sale`/`event`. (`security/ir_rule.xml`)

### 2.5 UI surfaces (names only, not fetched/read)
18. `views/`: `event_registration_views.xml`, `event_views.xml`, `product_template_views.xml`, `sale_order_views.xml`. `report/event_sale_report_views.xml`. `wizard/event_edit_registration.xml`, `wizard/event_configurator_views.xml`. File presence only.

### 2.6 Jobs / config / integrations
19. No crons and no `ir.config_parameter` reads found in this module's fetched files. `event.sale.report`'s SQL view converts sale amounts using each order's own frozen `currency_rate` (not a live conversion), while `event.event.sale_price_total` (in `models/event_event.py`) explicitly uses today's conversion rate instead — two different, both source-confirmed, currency-conversion strategies coexist in this module for different purposes (per-line historical accuracy in the report vs. a live aggregate total on the event record); A1 should not conflate the two. (`report/event_sale_report.py`, `models/event_event.py`)

## 3. Cross-module edges
20. Depends on `event_product` and `sale_management` (dependency relationship only, not group membership per MD-07/08); `event_product` is confirmed (in that module's own evidence file) to be the origin of the `service_tracking='event'` product type and the `sale_status` field this module completes. `auto_install: True` — presence in a database is a consequence of both dependencies, not an independent choice. (`__manifest__.py`)
21. `event_crm_sale`'s evidence file (this pilot) already documents a direct, source-confirmed read of the `sale_order_id` field this module adds to `event.registration` — confirming the cross-file dependency graph is internally consistent across this pilot's evidence set.
22. Reuses `sales_team.group_sale_salesman` (from `sale`) and `event.group_event_manager`/`group_event_registration_desk` (from `event`) for ACL/field-group scoping and for the `implied_ids` grant in finding 16.

## 4. Evidence gaps / contradictions
- G1: Seven view/wizard-view XML files not read.
- G2: `data/event_sale_data.xml` and `data/mail_templates.xml` fetched and hash-verified but not read in depth; not cited as numbered findings beyond their presence.
- G3: JS assets (`static/src/js/event_configurator_controller.js`, `sale_product_field.js`) and the JS test tour not fetched.
- G4: `data/event_sale_demo.xml`, `data/event_registration_demo.xml` (demo-only) not fetched.
- G5: i18n and the remaining tests (5 files) not fetched.
- No contradictions observed between manifest, `__init__.py` roster, and fetched files. All 18 fetches returned HTTP 200 and hash-verified.

## 5. Limitations
Static source only, single pinned commit, no runtime/DB observation. CANDIDATE-ROSTER PILOT under MD-18 — G11 membership of this module is DERIVED, not Boss-confirmed. No GMVQ QID answered; no Formal Coverage claimed.
