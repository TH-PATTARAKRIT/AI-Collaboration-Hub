# Source Map (candidate) — `fleet`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `fleet` |
| Display name | Fleet |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `ceb163617ae3a0c4` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/fleet/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `mail`
- Direct dependents in 300-module list (3): `account_fleet`, `hr_fleet`, `stock_fleet`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Fleet / Manage your fleet and track car costs
- Inventory of user-facing artifacts (counts): menu items 21, views 28, window actions 5, server actions 1, reports 0, mail templates 0, scheduled jobs 1, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (14): `fleet.vehicle.send.mail` (Send mails to Drivers); `fleet.service.type` (Fleet Service Type); `fleet.vehicle.log.services` (Services for vehicles); `fleet.vehicle.state` (Vehicle Status); `fleet.vehicle.model` (Model of a vehicle); `fleet.vehicle.model.brand` (Brand of the vehicle); `fleet.vehicle.assignation.log` (Drivers history on a vehicle); `fleet.vehicle` (Vehicle); `fleet.vehicle.tag` (Vehicle Tag); `fleet.vehicle.log.contract` (Vehicle Contract); `fleet.vehicle.odometer` (Odometer log for a vehicle); `fleet.vehicle.model.category` (Category of the model); `fleet.vehicle.cost.report` (Fleet Analysis Report); `fleet.vehicle.odometer.report` (Fleet Odometer Analysis Report)
- Objects extended from other modules (6): `mail.composer.mixin`, `mail.thread`, `mail.activity.mixin`, `mail.activity.type`, `avatar.mixin`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `fleet.vehicle.log.services` ← Community: `account_fleet`, `hr_fleet`; open-license custom/third-party scanned: —
- `fleet.vehicle.assignation.log` ← Community: `hr_fleet`; open-license custom/third-party scanned: —
- `fleet.vehicle` ← Community: `account_fleet`, `hr_fleet`; open-license custom/third-party scanned: —
- `fleet.vehicle.log.contract` ← Community: `hr_fleet`; open-license custom/third-party scanned: —
- `fleet.vehicle.odometer` ← Community: `hr_fleet`; open-license custom/third-party scanned: —
- `fleet.vehicle.model.category` ← Community: `stock_fleet`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.composer.mixin`, `mail.thread`, `mail.activity.mixin`, `mail.activity.type`, `avatar.mixin`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: `fleet.vehicle.log.services` → ['new', 'running', 'done', 'cancelled']; `fleet.vehicle.log.contract` → ['futur', 'open', 'expired', 'closed']
- Validation: 0 declarative constraint method(s), 3 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Fleet: Generate contracts costs based on costs frequency every 1 days
- Security: groups declared 3 (`fleet_group_user`, `fleet_group_manager`, `base.default_user_group`); record rules 9 (of which company-scoped by text 5); access rows 24

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

