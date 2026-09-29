# Source Map (candidate) — `spreadsheet_dashboard_event_sale`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `spreadsheet_dashboard_event_sale` |
| Display name | Spreadsheet dashboard for events |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `9258b95935c838c9` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/spreadsheet_dashboard_event_sale/` |
| auto_install / application | ['event_sale'] / None |

## 2. Dependencies
- Direct dependencies (manifest): `spreadsheet_dashboard`, `event_sale`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Dashboard / Spreadsheet
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 10 of 11 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: spreadsheet_dashboard_event_sale
Revision 19.0.post20260921 | Dashboard bridge: Spreadsheet Dashboards <-> Event Sales (event_sale) | data-only module

## A. Capabilities (core / optional / conditional)
- Delivers one published dashboard "Events" showing events, attendees and untaxed ticket revenue (spreadsheet_dashboard_event_sale/data/dashboards.xml:3-11). Depends on spreadsheet_dashboard and event_sale (spreadsheet_dashboard_event_sale/__manifest__.py:9).
- Auto-install: when event_sale is installed (spreadsheet_dashboard_event_sale/__manifest__.py:14). No settings, models, rules or access CSV.
- Marketing dashboard group, sequence 60, visible to event managers (spreadsheet_dashboard_event_sale/data/dashboards.xml:8-9). Main data model: events; sample dashboard file registered (:6-7).

## B. Business objects and lifecycle
- Read-only. Sheets: Dashboard, Data (spreadsheet_dashboard_event_sale/data/files/events_dashboard.json:427); pivots for events by venue, template, tags, organizer (json:542-632), attendees current/previous (json:660,682), untaxed revenue current/previous (json:706,732), events current/previous (json:754,776).
- Widgets: scorecards Events, Revenue, Attendees each with previous-period comparison (KPI cells json:444-450); bar chart of registrations by state; bar chart of events by stage; leaderboards of venue, tag, template, organizer by number of events (Dashboard sheet cells A24-E37).
- No state changes.

## C. Validations, automation, security
- Access: event manager group only (spreadsheet_dashboard_event_sale/data/dashboards.xml:9). Underlying revenue report: read access limited to event managers and multi-company rule (event_sale/security/ir.model.access.csv:5; event_sale/security/ir_rule.xml:5-9).
- Leaderboards exclude events without the grouping value (venue, template, tag, organizer) (events_dashboard.json:542-660).
- Attendee and revenue pivots carry no state filter (events_dashboard.json:660-760); counts therefore cover every registration state that the underlying default record visibility returns. Precise inclusion of cancelled registrations: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- event owns events, tags, types (templates), registrations, stages; event_sale owns the sales report over registrations (event_sale/report/event_sale_report.py:8-14); sale owns underlying orders/prices; spreadsheet_dashboard owns the container.

## E. Measures and revenue basis (business level)
- Attendees = count of event registrations. Events = count of events. Revenue = "untaxed revenue" sum from the event sales report (events_dashboard.json:446,450).
- Report basis: per registration, the order line's untaxed subtotal, divided by the order's currency rate and by the line quantity (so it is a per-attendee share of the line, expressed in company-currency basis); registrations without an order line count as zero revenue (event_sale/report/event_sale_report.py:100-113). Basis is sale-order value at order date, not invoiced/paid amounts, and not ticket list price.
- Default period filter: last 12 months (events_dashboard.json:790); other filters: Venue, Template, Tags, Organizer (json:~790-830). Which date the period applies to is not visible in this module: UNKNOWN — EVIDENCE INSUFFICIENT.

## F. Effective extension path
- event, event_sale, spreadsheet_dashboard (module names only). Booth sales are not shown here (event_booth_sale defines no report): UNKNOWN — EVIDENCE INSUFFICIENT.

## G. Not verified
- Handling of registrations linked to cancelled or draft sales orders in the revenue figure: UNKNOWN — EVIDENCE INSUFFICIENT (report exposes order state, dashboard does not filter on it: event_sale/report/event_sale_report.py:36,96; events_dashboard.json:706-760).
- Sample-dashboard trigger conditions: UNKNOWN — EVIDENCE INSUFFICIENT.

