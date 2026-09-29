# Source Map (candidate) — `event_sale`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `event_sale` |
| Display name | Events Sales |
| Manifest version | 1.3 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `ef65f8264314e31c` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/event_sale/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `event_product`, `sale_management`
- Direct dependents in 300-module list (3): `event_booth_sale`, `event_crm_sale`, `spreadsheet_dashboard_event_sale`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (3): `test_event_full`, `test_sale_product_configurators`, `website_event_sale`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Events / —
- Inventory of user-facing artifacts (counts): menu items 1, views 12, window actions 3, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 3, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (4): `registration.editor` (Edit Attendee Details on Sales Confirmation); `registration.editor.line` (Edit Attendee Line on Sales Confirmation); `event.event.configurator` (Event Configurator); `event.sale.report` (Event Sales Report)
- Objects extended from other modules (6): `sale.order`, `event.registration`, `sale.order.line`, `product.template`, `event.event`, `event.event.ticket`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `event.sale.report` ← Community: `website_event_sale`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `sale.order`, `event.registration`, `sale.order.line`, `product.template`, `event.event`, `event.event.ticket`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`sales_team.group_sale_salesman`); record rules 1 (of which company-scoped by text 1); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 40 of 40 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: event_sale
Revision 19.0.post20260921 | Bridge: Events (event_product, event) <-> Sales (sale_management) | ticket -> sale order line -> registration

## A. Capabilities (core / optional / conditional)
- Sells event tickets through sales orders and automatically creates attendee registrations on confirmation, enabling invoicing of registrations (event_sale/__manifest__.py:9-19). Depends on event_product and sale_management (:21).
- Auto-install: yes (event_sale/__manifest__.py:41). No settings toggle. Sales salespeople are made to imply the event registration-desk group (event_sale/security/event_security.xml:4-5).
- Service products get an "event" tracking choice; picking it forces invoicing on order (event_sale/models/product_template.py:12-15; tooltip: creates an attendee for the selected event :7-10). The service tracking field is un-hidden on the product form (event_sale/views/product_template_views.xml:7-9).
- Default event product's invoice policy set to "order" (non-updating, only if created) (event_sale/data/event_sale_data.xml:3-6).
- Event-tracked products are excluded from the product catalog on orders (event_sale/models/sale_order.py:58-59) and quantity is read-only on event lines (event_sale/models/sale_order_line.py:38-42).
- Analysis report "Event Sales" (per registration: revenue, untaxed revenue, ticket price, order status, payment status) with filters free / pending payment / sold, upcoming / past, groupings by event type, event, product, slot, ticket, registration state (event_sale/report/event_sale_report.py:8-48; report/event_sale_report_views.xml:99-121).

## B. Business objects and lifecycle
- Sale order line gains event, slot, ticket type, and its list of registrations (event_sale/models/sale_order_line.py:10-23). Event cleared if the product is not tracked as event or not sold by a ticket of that event; slot/ticket cleared when they no longer belong to the event (:70-87).
- Registration gains sale order and sale order line (cascade delete), and takes state from the order (event_sale/models/event_registration.py:12-14). Partner, event, slot, ticket, order link are copied from the line on create/update (:79-87,97-102,116-127).
- Order confirmation: blocks if any event line lacks an event; otherwise creates one registration per unit not yet registered (cancelled ones not counted); a single backend order with a priced line leaves registrations in draft so attendee details can be entered, free lines stay open; then opens the attendee editor for single orders (event_sale/models/sale_order.py:23-39; models/sale_order_line.py:44-68). (TEST) event_sale/tests/test_event_sale.py:236-270.
- State rules: order cancelled -> registrations cancelled; order total zero -> payment status "free" and registrations open; else sold orders (state "sale") give payment status "sold" and open registrations, unpaid/draft give "to pay" and draft (event_sale/models/event_registration.py:25-40). No status defaults to free / open (:42-47). (TEST) event_sale/tests/test_event_sale.py:596-615. After cancel then reset-to-draft and reconfirm, new registrations are created (TEST) :580-594.
- Confirming a registration from draft/cancel to open re-schedules event communications (event_sale/models/event_registration.py:145-154).
- Order attendee count excludes cancelled registrations and shows a button to the list (event_sale/models/sale_order.py:41-56).
- Changing the order's customer updates partner on its registrations (event_sale/models/sale_order.py:13-21).
- Campaign, source, medium of the order are copied to registrations (event_sale/models/event_registration.py:49-71).

## C. Validations, automation, security
- Each event-tracked line must have event and ticket, plus slot when event has several slots (event_sale/models/sale_order_line.py:25-36); confirmation additionally blocks unconfigured lines with a list (event_sale/models/sale_order.py:29-32).
- Configurator wizard checks ticket and slot belong to the chosen event (event_sale/wizard/event_configurator.py:21-32); it pre-selects the only ticket/slot when unique (:45-63); flags when no upcoming ticket exists for the product (:34-43).
- Changing ticket or slot of an existing registration schedules a warning activity on the order for the event responsible, else order salesperson, else current user/admin, asking for manual follow-up (event_sale/models/event_registration.py:105-112,129-143; data/mail_templates.xml:4-21).
- Access: salespeople may read/write/create (no delete) attendee editor and event configurator; delete allowed on editor lines; event managers read-only on the sales report (event_sale/security/ir.model.access.csv:2-5). Multi-company rule on report: company in allowed companies or empty (event_sale/security/ir_rule.xml:5-9).
- Event sales figures and linked-order buttons restricted to salespeople group (event_sale/models/event_event.py:10-16; views/event_views.xml:14).
- Registration creation runs with elevated rights (event_sale/models/sale_order_line.py:67).

## D. Handoffs
- event / event_product own events, tickets, registration base, sale status field; sale / sale_management own orders, lines, pricing; product owns tracking option; mail owns activities; utm owns campaign fields. Invoicing follows sale (invoice policy order).
- Booth sales layer on top: see event_booth_sale.

## E. Configuration that changes outcomes
- Ticket price rules: line price unit from the ticket (reduced price when pricelist shows no discount, otherwise base price), converted to order currency using the ticket company currency (event_sale/models/sale_order_line.py:120-129); ticket description prefers the product sales description (event_sale/models/event_ticket.py:8-14; line description combines ticket, slot, variants: event_sale/models/sale_order_line.py:101-118). (TEST) currency and pricelist/tax cases: event_sale/tests/test_event_sale.py:417,511.
- Event "Sales (Tax Included)" totals only confirmed lines with non-zero total, converted at today's rate into the event company currency (event_sale/models/event_event.py:21-46). Revenue basis: tax-included line total; order-linked view lists only confirmed orders (:48-55).
- Report unit revenue: line total (and untaxed subtotal) divided by order currency rate and by quantity, per registration, in company currency basis (event_sale/report/event_sale_report.py:100-113).
- Paid vs free ticket at confirmation decides draft vs open (event_sale/models/sale_order_line.py:60-64).

## F. Effective extension path
- event, event_product, sale, sale_management, sales_team, utm, mail (module names only). Extended by event_booth_sale, spreadsheet_dashboard_event_sale; website/POS event modules: UNKNOWN — EVIDENCE INSUFFICIENT (not opened).

## G. Not verified
- Backend attendee editor default names/contacts come from the order customer (event_sale/wizard/event_edit_registration.py:51-53,94-97); seat-limit enforcement details (tests at event_sale/tests/test_event_sale.py:314,360 (TEST)): UNKNOWN — EVIDENCE INSUFFICIENT for the underlying rule (owned by event).
- Portal/website purchase flow: UNKNOWN — EVIDENCE INSUFFICIENT.

