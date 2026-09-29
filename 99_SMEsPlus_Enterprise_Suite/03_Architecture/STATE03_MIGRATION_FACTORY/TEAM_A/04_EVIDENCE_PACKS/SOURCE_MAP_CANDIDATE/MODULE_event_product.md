# Source Map (candidate) — `event_product`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `event_product` |
| Display name | Events Product |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `3720798c6ed7831b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/event_product/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `event`, `product`, `account`
- Direct dependents in 300-module list (1): `event_sale`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `pos_event`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Events / —
- Inventory of user-facing artifacts (counts): menu items 0, views 9, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (6): `event.type.ticket`, `event.registration`, `product.template`, `product.product`, `event.event`, `event.event.ticket`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `event.type.ticket`, `event.registration`, `product.template`, `product.product`, `event.event`, `event.event.ticket`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 38 of 39 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: event_product (Events Product)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/event_product.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge that lets an event ticket type be backed by a sellable product with a price, and gives registrations a commercial "sale status". Depends on event, product, account (event_product/__manifest__.py:5).
- Conditional-on-install: auto_install true (event_product/__manifest__.py:16), so it comes in automatically when all three parents are present. Not an application; no settings.
- Ticket types (on event templates and on events) get a required Product, a price that defaults from the product's list price, a description that defaults from the product's sales description, and a "reduced price" shown for UX (event_product/models/event_type_ticket.py:20-29, 31-46, 53-58). Views place product and price on ticket forms/lists/kanban (event_product/views/event_ticket_views.xml:11, 19, 30, 38, 56, 65, 76, 84, 95-98).
- New product option: "Event Registration" as a service-tracking choice, and it is excluded from the general service-tracking blacklist set (event_product/models/product_template.py:7-12). A product marked this way is the required kind for tickets (domain on the ticket product field: event_product/models/event_type_ticket.py:22).
- Ticket price including taxes, computed from the product's customer taxes of the event's company (event_product/models/event_event_ticket.py:12-14, 30-38) and a tax-included reduced price (event_product/models/event_event_ticket.py:9-11, 23-28).
- Ticket sale availability is forced to unavailable when the product is archived (event_product/models/event_event_ticket.py:16-21), on top of the base rule: launched, not expired, not sold out (event/models/event_ticket.py:75-78).
- Registration "Sale Status" selection: Not Sold / Sold / Free, stored and computed (event_product/models/event_registration.py:7-11). Views show it as a badge, graph field and ribbons (event_product/views/event_registration_views.xml:9-13, 24, 35-38).
- Event currency is a read-only mirror of the company currency (event_product/models/event_event.py:7-9).

## B. Business objects, relationships, lifecycle
- Product <-> Event ticket: a product can be linked from many event tickets (event_product/models/product_product.py:8); a ticket has exactly one product (required, indexed) (event_product/models/event_type_ticket.py:20-22).
- Ticket type template -> event ticket: copying the template into an event also copies product and price (event_product/models/event_type_ticket.py:94-97).
- Registration -> ticket (base) with a sale status: when no order model is present (`_has_order` false), registrations with no status become "Free" and with no state become "open" (event_product/models/event_registration.py:13-14, 18-24). Sale orders (event_sale) and POS (pos_event) supply the real paid/unpaid computation by overriding the order check (event_sale/models/event_registration.py:22-23; comment event_product/models/event_registration.py:16-17; TEST event_sale/tests/test_event_sale.py:596-615: price zero without order line -> free, price above zero -> not sold, then sold once paid).
- Seed data: category "Events" under Services and a default product "Event Registration" (service, tracking "event", list price 30, cost 10) (event_product/data/event_product_data.xml:4-18). The record is installed with no-update semantics (event_product/data/event_product_data.xml:3).
- Lifecycle: no states owned here beyond the sale status above.

## C. Validations, automation, security, multi-company
- Blocking rule: a product linked to any event ticket must have service tracking "Event Registration"; changing it away, or making the product a non-service type, raises an error (event_product/models/product_product.py:10-18); (TEST) both attempts fail (event_product/tests/test_event_product.py:19-24).
- Upgrade automation: when the new required product column is added on existing ticket types, all void rows are set to the default seeded product, creating a generic zero-price "Generic Registration Product" (and its external id) if the seeded product is missing (event_product/models/event_type_ticket.py:60-92).
- Security: module ships no ACL, groups or record rules (skeleton: access [], rules []); ticket/registration/product access and multi-company are owned by event and product. The computed tax-inclusive prices are computed with elevated rights because they are read from the website (event_product/models/event_event_ticket.py:11, 14, 25).
- Tax filter uses taxes whose company equals the event's company (event_product/models/event_event_ticket.py:26, 34); a product with no tax for that company yields tax-free totals.
- The "reduced price" is tagged in code as a legacy, pricelist-context-dependent UX feature; effective price computation should not rely on it (event_product/models/event_type_ticket.py:48-52).

## D. Accounting / payroll / analytic handoffs
- Accounting: dependency on account exists so taxes on the product apply to ticket prices (event_product/__manifest__.py:5; event_product/models/event_event_ticket.py:26-27). No journal entries are created here.
- Sale order / invoicing / payment status of a registration: owned by event_sale (and by pos_event for point of sale) (event_sale/models/event_registration.py:22-23; both list event_product as dependency in their manifests: grep).
- No payroll, analytic or inventory handoff.

## E. Configuration / defaults that change outcomes
- Product selected on the ticket type drives default price and description, but price stays editable afterwards (event_product/models/event_type_ticket.py:24-26 readonly false).
- Ticket price is recalculated when the product changes; if the new product has a zero list price and the ticket already has a price, that price is kept (event_product/models/event_type_ticket.py:34-37).
- Default product for new tickets: the seeded "Event Registration" product (event_product/models/event_type_ticket.py:15-16, 22).
- Company and its currency determine the event currency; ticket type currency follows the product (event_product/models/event_event.py:7-9; event_product/models/event_type_ticket.py:23).
- Demo variants "Standard" and "VIP" products exist in demo mode only (event_product/data/event_product_demo.xml:4-20).

## F. Effective extension path (module names only)
- Extends: event (event, event ticket, ticket type, registration), product (template, product), and views of event. Manifest dependents: event_sale, pos_event. Further ticket extensions in event_sale and website_event_sale (grep of `_inherit` on the ticket model).

## G. Not verified
- Paid/unpaid determination and refund behaviour of registrations: UNKNOWN — EVIDENCE INSUFFICIENT (owned by event_sale / pos_event; only the tests cited above were seen).
- Where the service-tracking blacklist is consumed: UNKNOWN — EVIDENCE INSUFFICIENT (only overrides were found; base definition product/models/product_template.py:1564).
- Revision `19.0.post20260921`; not asserted as universal.

