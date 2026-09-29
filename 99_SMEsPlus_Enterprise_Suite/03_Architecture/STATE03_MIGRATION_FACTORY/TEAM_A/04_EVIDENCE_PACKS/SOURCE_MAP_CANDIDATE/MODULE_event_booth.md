# Source Map (candidate) — `event_booth`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `event_booth` |
| Display name | Events Booths |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `6d3b3158cb1b30d1` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/event_booth/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `event`
- Direct dependents in 300-module list (1): `event_booth_sale`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `test_event_full`, `website_event_booth`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Events / Manage event booths
- Inventory of user-facing artifacts (counts): menu items 2, views 21, window actions 4, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `event.booth.category` (Event Booth Category); `event.type.booth` (Event Booth Template); `event.booth` (Event Booth)
- Objects extended from other modules (5): `event.type`, `image.mixin`, `event.event`, `mail.thread`, `mail.activity.mixin`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `event.booth.category` ← Community: `event_booth_sale`, `website_event_booth_exhibitor`; open-license custom/third-party scanned: —
- `event.type.booth` ← Community: `event_booth_sale`; open-license custom/third-party scanned: —
- `event.booth` ← Community: `event_booth_sale`, `website_event_booth_exhibitor`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `event.type`, `image.mixin`, `event.event`, `mail.thread`, `mail.activity.mixin`

## 6. Actions / states / validation / automation / security
- State fields found: `event.booth` → ['available', 'unavailable']
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 9

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 42 of 43 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: event_booth (Events Booths)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton: sourcemap/event_booth.json. Pointers `module/path:LINE`; (TEST) = test-derived.

## A. Capabilities / functions
- Lets an event organiser define rentable booths, group them into booth categories (with picture and description), pre-define default booths on an event type, and track whether each booth on an event is still available or already taken (event_booth/__manifest__.py:5-12; event_booth/models/event_booth.py:6-28).
- Optional add-on to the events application: depends only on event, no auto_install, not an application (event_booth/__manifest__.py:12).
- Ships three sample booth categories (Standard, Premium, VIP) with feature bullet lists and pictures, loaded once (noupdate) (event_booth/data/event_booth_category_data.xml:2-89). Demo data for booths and event types is demo-only (event_booth/__manifest__.py:25-28).
- Menu: "Booth Categories" under event configuration; the raw "Booths" list is a technical menu shown only in developer mode (event_booth/views/event_menus.xml:4-14). Per-event "Booths" statistic button shows available/total (event_booth/views/event_event_views.xml:11-18).
- Booking a booth posts a "Booth Booked" message on the parent event (subtype off by default for followers) using a template that shows booth, renter and contact details (event_booth/models/event_booth.py:72-80; event_booth/data/mail_message_subtype_data.xml:4-8; event_booth/data/mail_templates.xml:4-20).

## B. Business objects, relationships, lifecycle
- Booth category (name, order, picture, description; archivable) -> many booths (event_booth/models/event_booth_category.py:7-18).
- Event type -> booth templates (name + category); Event -> booths (name + category + renter + status). Booth extends the template definition (event_booth/models/event_type_booth.py:7-23; event_booth/models/event_booth.py:6-17; event_booth/models/event_type.py:10-12; event_booth/models/event_event.py:12-14).
- Booth belongs to one event (required; deleting the event deletes its booths); the link back to the event type is optional and cleared if the type is removed (event_booth/models/event_booth.py:16-17).
- Renter is a contact; renter name/email/phone default from the contact but can be edited on the booth without writing back to the contact; the defaults only fill empty fields (event_booth/models/event_booth.py:19-46); (TEST) no sync back to contact and mixed details on contact change (event_booth/tests/test_event_booth_internals.py:34-56).
- State: two values only, Available (default) and Unavailable, tracked; the status bar can be clicked to switch (event_booth/models/event_booth.py:24-27; event_booth/views/event_booth_views.xml:11). No approval step in this module; confirmation is `action_confirm` which simply sets Unavailable and may set extra values (event_booth/models/event_booth.py:82-84). Reservation by a customer online or via sales orders is owned by other modules (website_event_booth, event_booth_sale: depend lists at website_event_booth/__manifest__.py:12, event_booth_sale/__manifest__.py:12).
- Transition to Unavailable (by create or write) triggers the booked notice on the event, only when it comes from Available (event_booth/models/event_booth.py:58-70).
- Event statistics: total and available booth counts, and the set of categories that still have an available booth (used by front end) (event_booth/models/event_event.py:56-89).
- Re-synchronising with the event type: when the event's type changes, unused (available) booths are removed and the new type's template booths are added; taken booths are kept (event_booth/models/event_event.py:27-54); (TEST) (event_booth/tests/test_event_internals.py:15-73, 92-103, 130-140 approx.). Changing the type's own content afterwards does not re-sync existing events (documented intent at event_booth/models/event_event.py:29-33).
- Only name and category are copied from a type template to an event booth (event_booth/models/event_type_booth.py:25-27).

## C. Validations, automation, security, multi-company
- Required fields: booth name, category, event (event_booth/models/event_type_booth.py:17-23; event_booth/models/event_booth.py:17). A category cannot be deleted while booths use it (restrict) (event_booth/models/event_type_booth.py:23).
- If exactly one category exists, it becomes the default for new booths (event_booth/models/event_type_booth.py:11-15).
- No constraint prevents a booth from being Unavailable without a renter, or Available with a renter (TEST: the booth stays Available after a partner is set, event_booth/tests/test_event_internals.py:63-68).
- Access (via groups of the event module): no rights for public/anonymous on booths or categories (rows with no group grant nothing) (event_booth/security/ir.model.access.csv:2,5); Registration Desk: read only; Event User: full rights on booths (read/write/create/delete), read-only on categories; Event Manager: full rights on booths, categories and templates (event_booth/security/ir.model.access.csv:3-4,6-10).
- Business-level implication: renter contact details (email, phone) are visible to the registration desk, editable by Event Users; the category's booth list is limited to the registration desk group (event_booth/models/event_booth_category.py:18). Website visitors reach booths only through the website modules (UNKNOWN — EVIDENCE INSUFFICIENT for their access path).
- No record rules; no company field on booths — company scope follows the parent event (event_booth/security/ir.model.access.csv; skeleton rules empty). Multi-company behaviour of events: UNKNOWN — EVIDENCE INSUFFICIENT here.
- Booth counters are computed with elevated rights so counts are correct for restricted users (event_booth/models/event_event.py:57).

## D. Accounting / payroll / analytic handoffs
- None in this module. Pricing and invoicing of booths are owned by event_booth_sale (with event_sale) (event_booth_sale/__manifest__.py:12).

## E. Configuration / defaults that change outcomes
- Booth template list on the event type decides what booths a new event starts with (event_booth/models/event_event.py:47-54).
- Booth default state Available (event_booth/models/event_booth.py:26).

## F. Effective extension path
- event_booth_sale (sales order per booth), website_event_booth (online booking), website_event_booth_sale, website_event_booth_exhibitor, website_event_booth_sale_exhibitor (dependency declarations found in the manifests listed above/ in the addons tree).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: online booking concurrency, price rules, and cancellation/return of a booth to Available (no code path in this module sets it back other than manual status change).

