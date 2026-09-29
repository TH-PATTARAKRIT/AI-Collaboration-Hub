# Source Map (candidate) — `stock_maintenance`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `stock_maintenance` |
| Display name | Stock - Maintenance |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `94a69dcdacd9cfe6` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/stock_maintenance/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock`, `maintenance`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / See lots used in maintenance
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `stock.location`, `maintenance.equipment`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.location`, `maintenance.equipment`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 12 of 12 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: stock_maintenance
Source revision: 19.0.post20260921 | Path base: odoo/addons | Method: static source read (no execution)

## A. Capabilities (all conditional on both parent apps)
- Bridge module linking equipment records to inventory: summary "See lots used in maintenance" (stock_maintenance/__manifest__.py:17). Depends on stock and maintenance (manifest line 12) and is auto_install (manifest line 18), so it appears automatically whenever both are installed; otherwise absent.
- Equipment gets an optional "Used in location" reference to an internal stock location (stock_maintenance/models/maintenance.py:9; form placement views/maintenance_views.xml:17-19). Location choice is limited to locations of usage type internal (maintenance.py:9).
- Equipment serial number is compared with lot/serial names; if any lot matches, a "Serial Number" smart button appears on the equipment form, opening the matching lot (single match: form; several: list) (maintenance.py:10-24, 26-44; views/maintenance_views.xml:9-16). Matching is by name only (maintenance.py:18).
- The button is hidden (match false) for users lacking read access to lots or not in the lot-tracking group (maintenance.py:14-16).
- Stock location form shows an "Equipments" smart button with count, visible when count is not zero, opening equipment list filtered to that location (stock_maintenance/models/stock_location.py:7-18; views/stock_location.xml:8-21).

## B. Objects and relationships
- No new models. Adds fields to maintenance.equipment (location, match flag) and stock.location (equipment count) (stock_maintenance/models/maintenance.py:6-10; models/stock_location.py:4-7).
- Relationship: equipment n..1 stock location (optional, informational); equipment serial number loosely matches stock.lot names (no foreign key) (maintenance.py:17-24).
- No states, transitions, gates, or automation. Placing equipment in a location creates no stock quant, move, or valuation entry (nothing in module writes to stock objects).

## C. Validations, security, multi-company
- No constraints, ACL file, groups or record rules in this module (manifest data list, lines 13-16; skeleton shows none). Visibility follows the parent models: maintenance equipment rules (maintenance/security/maintenance.xml:28-47, 55-59) and stock location rules from stock.
- Serial lookup is not company-filtered in the code shown (maintenance.py:17-19, 32); cross-company lot visibility therefore depends on stock lot record rules (UNKNOWN — EVIDENCE INSUFFICIENT for the resulting behaviour).
- Non-unique lot names across products/companies can produce a list rather than a single lot (maintenance.py:33-43).

## D. Handoffs (owner in brackets)
- Equipment [maintenance]: base object and the "hr_equipment_action" list opened from the location button (maintenance/views/maintenance_views.xml action id referenced at stock_maintenance/models/stock_location.py:16).
- Lots and locations [stock]: action for lots "stock.action_production_lot_form" (stock_maintenance/models/maintenance.py:28) and internal location definition.
- No accounting, approval, audit-trail, or integration handoff exists in this module.

## E. Configuration that changes outcomes
- Lot/serial tracking enabled for the user group (stock.group_production_lot) governs whether the serial button is available (maintenance.py:14).
- Equipment serial number entry and location selection are the only inputs.
- Auto-install behaviour: presence of both stock and maintenance.

## F. Effective extension path (module names only)
- Key objects extended here: maintenance.equipment (also extended by hr_maintenance) and stock.location (also extended by many stock-related modules). Modules depending on stock_maintenance: none found in addons manifests (grep of depends).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: any tests (no tests directory in this module; skeleton files.tests_py = 0).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether maintenance requests reference location or lot beyond the equipment form.
- UNKNOWN — EVIDENCE INSUFFICIENT: consumption of spare parts/lots in repair requests (not present in this module).

