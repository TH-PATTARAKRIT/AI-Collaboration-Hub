# Source Map (candidate) — `spreadsheet`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `spreadsheet` |
| Display name | Spreadsheet |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a662d738b5294ac2` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/spreadsheet/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `bus`, `web`, `portal`
- Direct dependents in 300-module list (2): `spreadsheet_account`, `spreadsheet_dashboard`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_spreadsheet`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Dashboard / Spreadsheet
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `spreadsheet.mixin` (Spreadsheet mixin)
- Objects extended from other modules (5): `res.lang`, `ir.model`, `ir.http`, `res.currency`, `res.currency.rate`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `spreadsheet.mixin` ← Community: `spreadsheet_dashboard`, `test_spreadsheet`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `res.lang`, `ir.model`, `ir.http`, `res.currency`, `res.currency.rate`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 54 of 54 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — spreadsheet
Source revision: 19.0.post20260921 | Module: "Spreadsheet" (spreadsheet/__manifest__.py:4) | category Productivity/Dashboard (:6) | LGPL-3 (:12)
Basis: static reading of manifest, server-side models, utils, controller, public template; front-end tree inspected by file listing and targeted searches (about 200 static files, not read in full).
## A. Capabilities and optionality
- A1. Provides the spreadsheet engine used by Odoo: a browser-based workbook editor/viewer with business-data functions, charts, pivots, lists and global filters, plus the server helpers it needs. spreadsheet/__manifest__.py:7-8,16-33; spreadsheet/static/src/index.js:44
- A2. Framework module: no menus, no actions and no standalone document model of its own; depends on bus, web, portal. It becomes visible only through other modules that store spreadsheets (see D). spreadsheet/__manifest__.py:9,13-15
- A3. Not auto_install and not an application; no security data file or access CSV is listed. spreadsheet/__manifest__.py:10-15
- A4. Business-data functions registered in the engine: ODOO.LIST, ODOO.LIST.HEADER, ODOO.FILTER.VALUE (plus a legacy V18 variant), ODOO.FILTER.LABEL, ODOO.CURRENCY.RATE; pivot values also come from this module's pivot layer. spreadsheet/static/src/list/list_functions.js:60-61; spreadsheet/static/src/pivot/pivot_functions.js:90-92; spreadsheet/static/src/currency/formulas.js:6-18
- A5. Chart types bound to Odoo data: bar, line, pie, combo, funnel, geo, pyramid, radar, scatter, sunburst, treemap, waterfall. spreadsheet/static/src/chart/odoo_chart (file list); spreadsheet/static/src/chart/index.js:12-14,25
- A6. Global filters (add/edit/remove/move; date, relation, text, selection kinds seen) that re-scope pivots, lists and charts; setting a filter value is allowed even in read-only mode. spreadsheet/static/src/global_filters/index.js:14-29; spreadsheet/static/src/global_filters/helpers.js:145,256
- A7. Read-only public page for a shared/frozen spreadsheet with optional Excel download and sign-in links; the template is here, the sharing records are elsewhere. spreadsheet/views/public_readonly_spreadsheet_templates.xml:4-37; spreadsheet/static/src/public_readonly_app/main.js:16-25
- A8. Share button component (freezes data before sharing). spreadsheet/static/src/components/share_button/ (file list); spreadsheet/static/src/helpers/model.js:61,95
- A9. The "Insert in spreadsheet" button of the web client is switched off by default here and is meant to be switched on by another module. spreadsheet/models/ir_http.py:9-16; (TEST) spreadsheet/tests/test_session_info.py:26-42. The Enterprise-side module that turns it on is not part of this tree — UNKNOWN — EVIDENCE INSUFFICIENT.
## B. Objects and lifecycle
- B1. Abstract "spreadsheet mixin" (no table of its own) that other models inherit to become spreadsheet documents: holds the workbook file (JSON, stored as binary attachment), a text view of it, a file name "<name>.osheet.json", and a thumbnail. spreadsheet/models/spreadsheet_mixin.py:17-28,96-99
- B2. New document default content: one sheet named "Sheet1" (translated for the creator), the creator's locale settings, revision marker START_REVISION. spreadsheet/models/spreadsheet_mixin.py:123-148
- B3. Data are stored in the attachment layer; the text field reads from / writes to the binary field. spreadsheet/models/spreadsheet_mixin.py:75-94
- B4. Helper services offered to the front-end: display names for record ids (archived records included, missing ids yield nothing); company currency; exchange-rate lookup by currency codes, date and company; list of language locales and the user's locale; "has parent relation" check for a model. spreadsheet/models/spreadsheet_mixin.py:105-121; spreadsheet/models/res_currency.py:7-27; spreadsheet/models/res_currency_rate.py:7-37; spreadsheet/models/res_lang.py:14-40; spreadsheet/models/ir_model.py:9-21
- B5. Export to Excel: packs generated files into a zip, replacing image references by image bytes from attachments or embedded data. spreadsheet/models/spreadsheet_mixin.py:150-175
- B6. Locale mapping: Odoo language gives thousands and decimal separators, date and time formats, formula argument separator (";" when decimal separator is ","), week start. spreadsheet/models/res_lang.py:29-40
## C. Validations, automation, security, external service
- C1. Constraint on the workbook file: must be valid JSON text, otherwise "invalid data" error. spreadsheet/models/spreadsheet_mixin.py:30-36
- C2. Deeper integrity check (models, fields chains and menu XML ids referenced by the workbook must exist and menus must have an action) runs only when the server is in test mode; excel-format files are skipped. spreadsheet/models/spreadsheet_mixin.py:37-73; spreadsheet/utils/validate_data.py:1-60
- C3. Exchange rates: use the company's conversion rule at the given date (today if none) and return false when a currency code is unknown or missing. spreadsheet/models/res_currency_rate.py:8-18; (TEST) spreadsheet/tests/test_currency_rate.py:52-143
- C4. Record-visibility caveat: display-name lookup uses the caller's rights; "has parent relation" returns false when the model is missing or not readable by the caller. spreadsheet/models/spreadsheet_mixin.py:113; spreadsheet/models/ir_model.py:15-16
- C5. Data-export audit: a logged-in user's download, copy, freeze or print actions are reported to a server endpoint that writes an information log line with user, source models, fields, groupings, domains and client IP. spreadsheet/controllers/main.py:12-26,28-45; spreadsheet/static/src/logging/logging_ui_plugin.js:27
- C6. Access control on spreadsheet content: this module defines no groups, ACLs or record rules; access to underlying business data is governed by the ordinary model rights of the viewing user, and document-level access by the module that inherits the mixin. spreadsheet/__manifest__.py:13-15. Security of shared public links is defined in the sharing module — see D2.
- C7. Company scoping: currency and rate helpers take an optional company, default the current company. spreadsheet/models/res_currency.py:18; spreadsheet/models/res_currency_rate.py:16
- C8. External service: none server-side; the browser loads bundled libraries (chart, geo maps data). spreadsheet/__manifest__.py:17-20; spreadsheet/static/topojson (folder listing)
- C9. Neutralization: links in cells are replaced by a "neutralized" marker in front-end handling (database-copy safety). spreadsheet/static/src/helpers/neutralized_link.js:6-16 (only header read).
## D. Handoffs
- D1. Dashboards (documents that use the mixin, dashboard groups, per-group visibility): spreadsheet_dashboard. spreadsheet_dashboard/models/spreadsheet_dashboard.py:7-19
- D2. Public shares of dashboards (access token, frozen copy, excel export, share URL): spreadsheet_dashboard. spreadsheet_dashboard/models/spreadsheet_dashboard_share.py:9-40
- D3. Accounting-specific spreadsheet functions (auto_install bridge on account): spreadsheet_account. spreadsheet_account/__manifest__.py:9,11
- D4. Test-only mixin consumer: test_spreadsheet. test_spreadsheet/models/spreadsheet_mixin_test.py
- D5. Real-time collaboration transport: bus (dependency). spreadsheet/__manifest__.py:9. Behaviour of collaboration — UNKNOWN — EVIDENCE INSUFFICIENT (no collaboration code in this module's server side).
- D6. Public page chrome: portal. spreadsheet/__manifest__.py:9; spreadsheet/views/public_readonly_spreadsheet_templates.xml:23-30
- D7. Odoo-native data sources (pivot, list, graph models) reuse web view models. spreadsheet/__manifest__.py:22-23
## E. Configuration that changes outcomes
- E1. User language (locale, separators, week start). spreadsheet/models/res_lang.py:26-40
- E2. Company currency and currency rate tables. spreadsheet/models/res_currency.py:18-27
- E3. Server test mode (enables the deep integrity check). spreadsheet/models/spreadsheet_mixin.py:37
- E4. Session flag for the "insert in spreadsheet" button. spreadsheet/models/ir_http.py:15
## F. Extension path
- Modules inheriting the mixin (grep of "spreadsheet.mixin" in Python): spreadsheet_dashboard (dashboard and dashboard share), test_spreadsheet. Modules listing spreadsheet in manifests: spreadsheet_dashboard, spreadsheet_account, test_spreadsheet. Front-end extension points: function, chart, plugin and command registries (spreadsheet/static/src/plugins.js, spreadsheet/static/src/index.js).
## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: exact list of all business functions, chart options and pivot behaviours (front-end code not read in full).
- UNKNOWN — EVIDENCE INSUFFICIENT: how concurrent editing/revision merging works (client engine and bus usage not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: any data-size or row limits.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether user domain filters in a shared or frozen spreadsheet can expose data beyond the viewer's normal rights (depends on the sharing module's freeze behaviour; helper `freezeOdooData` seen but not analysed).

