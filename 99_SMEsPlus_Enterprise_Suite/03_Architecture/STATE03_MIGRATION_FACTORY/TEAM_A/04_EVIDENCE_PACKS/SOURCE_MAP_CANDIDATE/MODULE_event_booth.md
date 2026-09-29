# Source Map (candidate) — `event_booth`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

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
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

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
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

