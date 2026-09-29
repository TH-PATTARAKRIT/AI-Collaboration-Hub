# Source Map (candidate) — `website_timesheet`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_timesheet` |
| Display name | Hide Portal Timesheet Information |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `271def8752b750f4` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_timesheet/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `website`, `hr_timesheet`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Allow hiding timesheet information in the portal
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `account.analytic.line`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.analytic.line`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 12 of 13 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_timesheet (Hide Portal Timesheet Information)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_timesheet.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: lets a website administrator hide timesheet information from the customer portal, consistently across other records (website_timesheet/__manifest__.py:4-8).

## A. Capabilities / functions
- Conditional: depends on website and hr_timesheet with `auto_install` (website_timesheet/__manifest__.py:9,11); appears automatically when both are installed.
- Core (single behaviour): the decision "should timesheet details be shown in the portal?" is answered by whether the portal-home "Timesheets" website view is currently enabled; disabling that view hides timesheet information everywhere the decision is consulted (website_timesheet/models/account_analytic_line.py:7-13).
- Without this module, the same decision always says yes (hr_timesheet/models/hr_timesheet.py:532-536).

## B. Business objects, relationships, lifecycle
- No new object. Acts on timesheet lines (account.analytic.line, owned by analytic/hr_timesheet) and on the website view record of the portal home "Timesheets" block (hr_timesheet/views/hr_timesheet_portal_templates.xml:11).
- The view is a "customize show" toggle (hr_timesheet/views/hr_timesheet_portal_templates.xml:11), i.e. it is switched from the website customise menu; lifecycle is on/off, with duplicate per-website copies collapsed by the filter (website_timesheet/models/account_analytic_line.py:13). How duplicates are prioritised across websites: UNKNOWN — EVIDENCE INSUFFICIENT.

## C. Validations, automation, security, multi-company
- The lookup reads the view with elevated rights and includes inactive views, then takes its active state (website_timesheet/models/account_analytic_line.py:13). Consequence: the flag is global to the view set, not per portal user. Per-website nuance: UNKNOWN — EVIDENCE INSUFFICIENT.
- No access-control rows, record rules or constraints in this module; no company scoping.

## D. Handoffs to other modules
- hr_timesheet (owner of the hook and portal templates): task portal page hides timesheet table, allocated hours and progress when the hook says no (hr_timesheet/views/project_task_portal_templates.xml:6, 27, 49).
- sale_timesheet: sales-order and invoice portal pages consult the same hook (sale_timesheet/views/sale_timesheet_portal_templates.xml:6, 66, 76).
- website: the view / customise-menu machinery.

## E. Configuration / defaults that change outcomes
- The single control is the portal "Timesheets" customisation toggle in the website editor; default shows timesheets (hr_timesheet/models/hr_timesheet.py:536; hr_timesheet/views/hr_timesheet_portal_templates.xml:11).

## F. Effective extension path (module names only)
- account.analytic.line hook `_show_portal_timesheets` defined in hr_timesheet and overridden in website_timesheet; consumed by hr_timesheet and sale_timesheet templates.

## G. Not verified
- Tests: none. Effect on portal users with access via project sharing: UNKNOWN — EVIDENCE INSUFFICIENT.

