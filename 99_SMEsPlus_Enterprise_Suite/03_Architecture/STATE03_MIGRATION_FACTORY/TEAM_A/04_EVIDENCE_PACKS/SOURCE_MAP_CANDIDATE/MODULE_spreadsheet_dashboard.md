# Source Map (candidate) — `spreadsheet_dashboard`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

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
- Core/optional/conditional behavior and business meaning of each capability: see section 10

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
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 37 of 39 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: spreadsheet_dashboard (Spreadsheet dashboard)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton: sourcemap/spreadsheet_dashboard.json. Pointers `module/path:LINE`; (TEST) = test-derived.

## A. Capabilities / functions
- Framework for read-only "Dashboards" built on the spreadsheet engine: a Dashboards app (menu, sequence 37) shows published dashboards organised in groups, with per-user favourites, sample content for empty databases, and public sharing by link with optional Excel download (spreadsheet_dashboard/views/menu_views.xml:2-20; spreadsheet_dashboard/models/spreadsheet_dashboard.py:7-45).
- Depends only on the spreadsheet module (spreadsheet_dashboard/__manifest__.py:9). Not auto-install; installs on demand or as a dependency of the per-domain dashboard modules (14 dependants found: board, event_sale, hr_expense, hr_timesheet, account, sale, sale_timesheet, stock_account, pos_hr, pos_restaurant, website_sale, website_sale_slides, im_livechat, plus itself; found by grep of `spreadsheet_dashboard` in manifests under the addons root, e.g. spreadsheet_dashboard_hr_expense/__manifest__.py, spreadsheet_dashboard_hr_timesheet/__manifest__.py).
- Ships only empty dashboard groups: Sales (100), Finance (300), Logistics (400), Services (500), Marketing (600), Website (700), Human Resources (800); actual dashboards come from other modules (spreadsheet_dashboard/data/dashboard.xml:4-38).
- Configuration menu to manage dashboard groups (spreadsheet_dashboard/views/menu_views.xml:20-40).

## B. Business objects, relationships, lifecycle
- Dashboard group -> dashboards; group exposes only published ones (spreadsheet_dashboard/models/spreadsheet_dashboard_group.py:11-12). (TEST) publish/unpublish moves a dashboard in/out of the visible list (spreadsheet_dashboard/tests/test_spreadsheet_dashboard.py:54-71).
- Dashboard: name, group (required), order, published flag (default published), allowed companies, allowed user groups (default: all internal users), favourite users, list of "main" data models used for emptiness detection (spreadsheet_dashboard/models/spreadsheet_dashboard.py:13-31).
- Sample mode: if a dashboard has a sample file and any of its main data models has no records at all, the sample content is returned flagged as sample instead of real data; a model the user cannot read is checked with elevated rights, so the emptiness test itself does not leak content (spreadsheet_dashboard/models/spreadsheet_dashboard.py:59-73; spreadsheet_dashboard/controllers/dashboards_controllers.py:21-27). (TEST) unreadable main model does not force sample mode (spreadsheet_dashboard/tests/test_dashboard_controllers.py:64-79).
- Data load is served in the user's language/number locale and company currency; company scope taken from the user's currently selected companies (spreadsheet_dashboard/controllers/dashboards_controllers.py:18-20; spreadsheet_dashboard/models/spreadsheet_dashboard.py:47-57). (TEST) locale/currency/namespace (spreadsheet_dashboard/tests/test_dashboard_controllers.py:9-49).
- Favourite toggling is personal and uses elevated rights only to update the favourites list (spreadsheet_dashboard/models/spreadsheet_dashboard.py:39-45); (TEST) (spreadsheet_dashboard/tests/test_spreadsheet_dashboard.py:73).
- Shared dashboard copy ("share"): a frozen copy with a random secret token and an optional pre-built Excel export; URL = base URL + share id + token (spreadsheet_dashboard/models/spreadsheet_dashboard_share.py:9-33). Lifecycle: created by any internal user; removed when the source dashboard is deleted (spreadsheet_dashboard/models/spreadsheet_dashboard_share.py:14).
- Copy of a dashboard is named "<name> (copy)" unless a name is given (spreadsheet_dashboard/models/spreadsheet_dashboard.py:82-88); (TEST) (spreadsheet_dashboard/tests/test_spreadsheet_dashboard.py:25).

## C. Validations, automation, security, multi-company
- Groups: one new privilege group "Dashboard: Admin" (implies internal user) given to root and admin users (spreadsheet_dashboard/security/security.xml:17-29).
- Access lists: internal users read-only on dashboards and groups; dashboard admins full rights on both; internal users full rights on their shares (spreadsheet_dashboard/security/ir.model.access.csv:2-6). Note: the third row's first id token has an unbalanced quote in the file, a data-formatting oddity (spreadsheet_dashboard/security/ir.model.access.csv:3); effect on load: UNKNOWN — EVIDENCE INSUFFICIENT.
- Record rules: internal users see a dashboard only if one of its allowed groups is among their (implied) groups; separate company rule: dashboards with allowed companies are visible only within the user's selected companies, dashboards with no company are visible everywhere; admins see all (spreadsheet_dashboard/security/security.xml:4-15,31-36). Business implication: HR/finance dashboards can be limited to specific groups and companies by configuring the two lists on each dashboard.
- Shares: each user sees only shares they created (spreadsheet_dashboard/security/security.xml:38-43); (TEST) another user cannot read a share's token (spreadsheet_dashboard/tests/test_dashboard_share.py:37-41).
- Public link access requires (a) matching secret token (constant-time compare) AND (b) the sharer still having read access to the dashboard; if the sharer loses the group, the link returns forbidden (spreadsheet_dashboard/models/spreadsheet_dashboard_share.py:35-46); (TEST) wrong token and revoked access give 403 (spreadsheet_dashboard/tests/test_share_controllers.py:23-56,81-95). Privacy implication: a shared link exposes a frozen data snapshot to anyone holding the link, without login (spreadsheet_dashboard/controllers/share.py:6-28,42-63).
- Excel download of a share requires the logged-in user to hold the export right group; otherwise an error (spreadsheet_dashboard/controllers/share.py:13-14,30-40); (TEST) (spreadsheet_dashboard/tests/test_share_controllers.py:58-80).
- Deleting a dashboard group that was loaded from another module is blocked (spreadsheet_dashboard/models/spreadsheet_dashboard_group.py:15-21); (TEST) (spreadsheet_dashboard/tests/test_spreadsheet_dashboard.py:41).

## D. Accounting / payroll / analytic handoffs
- None here; it only displays data owned by other modules (which module supplies which numbers: per dependant module, not read).

## E. Configuration / defaults that change outcomes
- New dashboards default to published and to internal-user visibility (spreadsheet_dashboard/models/spreadsheet_dashboard.py:17,19).
- Sample data only when a sample file path is set and a main model is empty (spreadsheet_dashboard/controllers/dashboards_controllers.py:21).

## F. Effective extension path
- Extended by data-only modules named spreadsheet_dashboard_* (account, sale, hr_expense, hr_timesheet, etc.); front-end editing of dashboards is not in Community (UNKNOWN — EVIDENCE INSUFFICIENT; the security file mentions an "edition" module rule at spreadsheet_dashboard/security/security.xml:2).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: spreadsheet engine internals, spreadsheet.mixin behaviour (spreadsheet module), dashboard JSON contents.

