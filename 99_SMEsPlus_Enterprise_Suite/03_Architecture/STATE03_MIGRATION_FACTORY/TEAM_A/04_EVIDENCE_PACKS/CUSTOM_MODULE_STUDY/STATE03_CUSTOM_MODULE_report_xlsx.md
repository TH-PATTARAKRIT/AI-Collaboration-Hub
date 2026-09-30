> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: report_xlsx

## 0. Header
- Module: report_xlsx
- License (confirmed in manifest): AGPL-3 (report_xlsx/__manifest__.py:11)
- Author (manifest): ACSONE SA/NV, Creu Blanca, Odoo Community Association (OCA) (report_xlsx/__manifest__.py:6)
- Version (manifest): 19.0.1.0.1 (report_xlsx/__manifest__.py:9)
- Path: addons_Extramodule/addons_extra/report_xlsx
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Foundation for spreadsheet (xlsx) reports: adds a new report output type "XLSX" to report actions, a download route, and an abstract base class that other modules extend to produce workbooks (report_xlsx/models/ir_report.py:7-12; controllers/main.py:24-104; report/report_abstract_xlsx.py:66-118).
- Extra behaviour: when two worksheets in a workbook would get the same name, the second one is renamed with a numbered suffix instead of failing (report/report_abstract_xlsx.py:18-60).
- A demo report action "Print to XLSX" on partners is loaded only with demo data (demo/report.xml:6-12; report/report_partner_xlsx.py:7-16).

## 2. Attachment to CORE
- Depends declared: base, web (manifest:13); external Python libraries xlsxwriter and xlrd (manifest:12).
- Core objects extended: `ir.actions.report` (core:base/models/ir_actions_report.py; selection field `report_type` at :170), the web report controller (core:web/controllers/report.py:18).
- Overrides by name:
  - `report_type` selection: ADDS value "xlsx" (models/ir_report.py:10-12).
  - `_get_report_from_name` (models/ir_report.py:25-37): ADDS after core — if the core lookup (core:base/models/ir_actions_report.py:650) finds nothing, searches xlsx-type reports by name using the caller's own rights (no elevation), whereas the core lookup uses elevated access. Because the core lookup already matches by name across all types, this branch is rarely reached (inference from core :650-657).
  - `_render_xlsx` (new, models/ir_report.py:15-23): renders using the report model named "report.<report_name>", switching back to the caller's normal rights when calling the generator (line :21). Core dispatches renders by report type (core:base/models/ir_actions_report.py:1145-1147).
  - Controller `report_routes` (controllers/main.py:25-49): ADDS a branch for converter "xlsx" before the core route; otherwise passes to core (core:web/controllers/report.py:27).
  - Controller `report_download` (controllers/main.py:51-104): ADDS an xlsx branch; otherwise passes to core (core:web/controllers/report.py:94). Core signature has an extra `readonly` parameter (core:web/controllers/report.py:94) that this override does not list; the non-xlsx branch forwards without it (controllers/main.py:104).
- No core control is weakened. No ALTERS CORE CONTROL. Report permission: the generated workbook is built with the caller's rights (models/ir_report.py:21); whether report-level group restrictions from the report action record apply to xlsx type is not implemented here beyond the core lookup (UNKNOWN below).

## 3. New objects, security, automation, external calls
- New abstract models: `report.report_xlsx.abstract` (report/report_abstract_xlsx.py:66-69) and demo `report.report_xlsx.partner_xlsx` (report/report_partner_xlsx.py:7-10). No stored models, ACLs, groups, rules or company scoping added.
- The download route builds file names from the report name and, if set, the report's print-name expression evaluated by the safe evaluator on the selected records (controllers/main.py:85-92).
- Errors are returned to the browser as escaped JSON containing the serialized exception (controllers/main.py:98-102).
- Automation: none. External calls: none.
- Client side: an ES-module download handler registers for report type xlsx (static/src/js/report/action_manager_report.esm.js:6-54) and a legacy script file exists (static/src/js/report/action_manager_report.js:1-30). Neither is currently wired: the manifest line loading the ES-module file is commented out (manifest:16-20) and the manifest has no data list, so the template that would include the legacy script is not loaded (views/webclient_templates.xml:6-13 not referenced in manifest). See section 4.

## 4. Odoo 19 compatibility
- Present in Community 19: `ir.actions.report._get_report_from_name`, `_get_report`, `_render` (core:base/models/ir_actions_report.py:650, :660, :1145), `ReportController.report_routes` / `report_download` (core:web/controllers/report.py:27, :94), `serialize_exception` and `content_disposition` (core:odoo/http.py:469, :353), report handler registry used by the web client (core:web/static/src/webclient/actions/action_service.js:1357).
- Possible issue: the controller imports a URL-decoding helper from the Werkzeug URL module (controllers/main.py:8). The core requirements pin Werkzeug 3.0.1 for newer Python versions (core requirements.txt:98), and that helper is understood to have been removed in Werkzeug 3 — not verified against the installed library; if absent, the module fails at import. Marked as risk only.
- Client-side handler not loaded: unless another module supplies the handler, the browser may not trigger the xlsx download route (inference from manifest lines :16-20 and lack of a data list). Legacy `odoo.define` script (static/src/js/report/action_manager_report.js:3) uses removed web client classes; not usable in 19.
- Signature drift: `report_download` in core has an additional `readonly` argument (core:web/controllers/report.py:94); the override omits it.
- Names checked: `xlrd` and `xlsxwriter` requirement declared; presence in the deployed Python environment not checked.

## 5. Custom-to-custom dependencies
- None declared. Extended by report_xlsx_helper (depends on report_xlsx).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the xlsx download works in the deployed backend given the commented-out asset registration.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether report-level group restrictions (report action groups) are honoured for xlsx reports by the core lookup path.
- UNKNOWN — EVIDENCE INSUFFICIENT: the installed Werkzeug version.
