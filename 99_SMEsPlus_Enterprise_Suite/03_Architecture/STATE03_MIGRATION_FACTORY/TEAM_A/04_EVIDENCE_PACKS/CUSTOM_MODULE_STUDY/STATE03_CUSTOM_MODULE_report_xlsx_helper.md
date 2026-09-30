> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: report_xlsx_helper

## 0. Header
- Module: report_xlsx_helper
- License (confirmed in manifest): AGPL-3 (report_xlsx_helper/__manifest__.py:10)
- Author (manifest): Noviat, Odoo Community Association (OCA) (report_xlsx_helper/__manifest__.py:6)
- Version (manifest): 19.0.1.0.0 (report_xlsx_helper/__manifest__.py:9)
- Path: addons_Extramodule/addons_extra/report_xlsx_helper
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Toolkit for spreadsheet reports built on report_xlsx: predefined cell formats and page headers/footers, a table-driven way to describe columns and write rows, worksheet-name cleaning, and formula/format helpers (report/report_xlsx_abstract.py:16-100, :609-770; report/report_xlsx_format.py).
- Adds the ability to call an xlsx report by name without a report action record (models/ir_actions_report.py:11-19; controllers/main.py:12-52), used by wizards that export directly.
- Contains a sample partner report (report/test_partner_report_xlsx.py:13-30) that is part of the shipped module code, not only of tests.

## 2. Attachment to CORE
- Depends declared: report_xlsx only (manifest:11); indirect core dependencies base and web through report_xlsx.
- Core objects extended: `ir.actions.report` (via `_render_xlsx` from report_xlsx), web report route (core:web/controllers/report.py:23-27).
- Overrides by name:
  - `_render_xlsx` on `ir.actions.report` (models/ir_actions_report.py:11-19): ADDS a branch before the report_xlsx version — when called on an empty set with a report name in context, it goes straight to the report model named "report.<name>" and skips the report-action lookup; otherwise delegates.
  - Controller `report_routes` (controllers/main.py:21-52): REPLACES the parent route registration, re-declaring routes "/report/<converter>/<reportname>" and with docids for any logged-in user (website=True flag included, :14-20). Behaviour: looks up the report action; if converter is xlsx and NO report action is found, it renders through the name-based path (:22-37, note the condition at :23), otherwise delegates to the parent route (:52).
- ALTERS CORE CONTROL (partly): with this route, an authenticated user can request an xlsx export from any model named "report.<name>" even without a report action record; the report-action level group restriction (if any) is therefore not consulted on this path (inference from controllers/main.py:22-37 and models/ir_actions_report.py:13-18). Access then depends only on what the report model itself checks and on the caller's normal ORM rights (the generator runs without elevation; no sudo in these lines).
- Odd code path: in the name-based branch the variable `report` is an empty record set when the condition is true, yet it is used to call the renderer (controllers/main.py:35); this appears intended, as `_render_xlsx` handles an empty set (models/ir_actions_report.py:13).

## 3. New objects, security, automation, external calls
- New abstract extension of `report.report_xlsx.abstract` (report/report_xlsx_abstract.py:16-18) and test model `report.report_xlsx_helper.test_partner_xlsx` (report/test_partner_report_xlsx.py:14-17). No stored models, ACLs, groups, rules.
- Evaluates column expressions with Python `eval` on templates written in code (report/report_xlsx_abstract.py:757-766); the source comment states this is safe only while templates are defined in Python modules. Not user-editable in this module (inference).
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- Depends on report_xlsx's route and asset issues (see report_xlsx file section 4): client-side handler wiring and Werkzeug helper.
- Routes use `type="http"` with `auth="user"` (controllers/main.py:17-19); parent core route in 19 at core:web/controllers/report.py:23-27. Signature of `report_routes` unchanged from core.
- `website=True` route flag (controllers/main.py:19) is meaningful only with the website module; effect when absent not verified.
- Names not in Community 19: none found in Python beyond report_xlsx's own.

## 5. Custom-to-custom dependencies
- Depends on report_xlsx (see its file).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: which other installed modules call the name-based export path, and whether any rely on it for permission checks.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the sample test report is reachable by ordinary users in the deployed instance (model access on partners applies).
