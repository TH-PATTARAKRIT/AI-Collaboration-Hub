# Source Map (candidate) — `spreadsheet_dashboard`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `spreadsheet_dashboard` |
| Display name | Spreadsheet dashboard |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `9f2eefba5c2fb49e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/spreadsheet_dashboard/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `spreadsheet`
- Direct dependents in 300-module list (9): `board`, `spreadsheet_dashboard_account`, `spreadsheet_dashboard_event_sale`, `spreadsheet_dashboard_hr_expense`, `spreadsheet_dashboard_hr_timesheet`, `spreadsheet_dashboard_im_livechat`, `spreadsheet_dashboard_sale`, `spreadsheet_dashboard_sale_timesheet`, `spreadsheet_dashboard_stock_account`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `spreadsheet_dashboard_pos_hr`, `spreadsheet_dashboard_pos_restaurant`, `spreadsheet_dashboard_website_sale`, `spreadsheet_dashboard_website_sale_slides`
- Custom / third-party modules that declare a dependency (name — license only) (2): `scgl_dashboard_finance` — LGPL-3, `scgl_dashboard_logistics` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Dashboard / Spreadsheet
- Inventory of user-facing artifacts (counts): menu items 4, views 5, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 4
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `spreadsheet.dashboard` (Spreadsheet Dashboard); `spreadsheet.dashboard.share` (Copy of a shared dashboard); `spreadsheet.dashboard.group` (Group of dashboards)
- Objects extended from other modules (1): `spreadsheet.mixin`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `spreadsheet.mixin`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`spreadsheet_dashboard.group_dashboard_manager`); record rules 4 (of which company-scoped by text 1); access rows 5

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

