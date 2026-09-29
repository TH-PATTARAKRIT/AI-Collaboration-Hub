# Source Map (candidate) — `sale_pdf_quote_builder`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_pdf_quote_builder` |
| Display name | Sales PDF Quotation Builder |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `06fb71e21d9b1789` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_pdf_quote_builder/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_management`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / —
- Inventory of user-facing artifacts (counts): menu items 1, views 10, window actions 1, server actions 0, reports 2, mail templates 0, scheduled jobs 1, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `sale.pdf.form.field` (Form fields of inside quotation documents.); `quotation.document` (Quotation's Headers & Footers)
- Objects extended from other modules (5): `ir.actions.report`, `sale.order.template`, `sale.order`, `sale.order.line`, `product.document`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 2 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.actions.report`, `sale.order.template`, `sale.order`, `sale.order.line`, `product.document`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 5 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Sale Pdf Quote Builder: assign form fields to documents post upgrade every 9999 months
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 1); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 45 of 45 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_pdf_quote_builder
Source revision: 19.0.post20260921 | Module: "Sales PDF Quotation Builder" (sale_pdf_quote_builder/__manifest__.py:4) | depends: sale_management (:7) | auto_install true (:29) | LGPL-3 (:39)
Basis: static reading of all models, controller, security, data, report and key views; test names listed (one 405-line test file), assertions not read in full.

## A. Capabilities and optionality
- A1. Build a customer-facing quotation PDF by merging: chosen header PDFs, per-line product PDFs ("inside quote" documents), the standard quote printout, then footer PDFs; PDF form fields inside the documents are auto-filled from the order or typed in by the salesperson. sale_pdf_quote_builder/models/ir_actions_report.py:22-80
- A2. Installs automatically with Sales (quotation templates); no on/off setting. A "Headers/Footers" shortcut appears in sales settings and a menu under Sales configuration. sale_pdf_quote_builder/__manifest__.py:7,29; sale_pdf_quote_builder/wizards/res_config_settings_views.xml:9-16; sale_pdf_quote_builder/views/sale_pdf_quote_builder_menus.xml:4-8
- A3. The standard "quotation/order" printout is renamed "PDF Quote"; a second, un-merged printout "Quotation / Order" is added. sale_pdf_quote_builder/report/ir_actions_report.xml:4-17
- A4. A "Quote Builder" tab on the order (salespeople only) shows when a customer is set and something is available to include. sale_pdf_quote_builder/views/sale_order_views.xml:18-32

## B. Objects, relationships, lifecycle
- B1. Header/footer document (quotation.document): wraps an uploaded PDF attachment; type header or footer, active flag, sequence, optional link to quotation templates, "add by default" flag, company. sale_pdf_quote_builder/models/quotation_document.py:12-56
- B2. Product document option "Inside quote pdf" added to the existing product document "attached on sale" choices. sale_pdf_quote_builder/models/product_document.py:15-27
- B3. Form field registry (sale.pdf.form.field): field name as found in a PDF, document type (header/footer or product), optional "path" (a dotted route from the order, or from the order line for product docs) that fills the field automatically; without a path the value is typed on the order. sale_pdf_quote_builder/models/sale_pdf_form_field.py:12-42
- B4. Form fields are re-detected from the PDF whenever a document's file changes (header/footer always; product documents only when "inside quote"); previous links are cleared first. sale_pdf_quote_builder/models/quotation_document.py:69-78; sale_pdf_quote_builder/models/product_document.py:52-63; sale_pdf_quote_builder/models/sale_pdf_form_field.py:193-219
- B5. Defaults: a set of standard mappings (totals, order date, validity, customer name, salesperson, quantity, price, taxes, etc.) is created at install/update and topped up when missing. sale_pdf_quote_builder/models/sale_pdf_form_field.py:124-181; sale_pdf_quote_builder/data/sale_pdf_form_field.xml:4
- B6. Order: new quotes get default headers/footers (add-by-default, not restricted to a template, current company). Choosing a quotation template removes documents no longer available and adds the template's add-by-default ones for the order's company. sale_pdf_quote_builder/models/sale_order.py:11-16,66-77. (TEST) sale_pdf_quote_builder/tests/test_pdf_quote_builder.py:177-197,372-405
- B7. Availability: documents with no template restriction, or restricted to the order's template. Product documents available on a line are those "inside quote" on its variant or template, ordered. sale_pdf_quote_builder/models/sale_order.py:40-50; sale_pdf_quote_builder/models/sale_order_line.py:38-62. Selected product documents are cleared if no longer available after product change. sale_pdf_quote_builder/models/sale_order_line.py:28-34
- B8. Typed values are stored per order in a JSON field keyed by header / footer / line and document. sale_pdf_quote_builder/models/sale_order.py:33-36,89-149; sale_pdf_quote_builder/models/ir_actions_report.py:173-194
- B9. Print rule: merging only applies to the standard sale report and only for quotes (not confirmed orders) unless the system parameter "sale.always_include_selected_documents" is true; if no header, product document or footer is selected the plain PDF is returned. sale_pdf_quote_builder/models/ir_actions_report.py:25-43. No settings screen for that parameter found in sale, sale_management or this module (grep).
- B10. Form field names in merged PDFs are prefixed per document/line so equal names on different documents don't clash; text fields are forced read-only and multi-line. sale_pdf_quote_builder/models/ir_actions_report.py:54,63,196-249
- B11. Dynamic values: booleans as Yes/No, amounts formatted in the currency, dates in the partner or user timezone, selections by label, relations as comma-joined names. sale_pdf_quote_builder/models/ir_actions_report.py:122-171

## C. Validations, security, multi-company
- C1. Header/footer must be PDF and not encrypted/unsupported; product "inside quote" documents must be a file (not URL), PDF and not encrypted. sale_pdf_quote_builder/models/quotation_document.py:60-65; sale_pdf_quote_builder/models/product_document.py:38-48; sale_pdf_quote_builder/utils.py:11-21
- C2. Form field name: letters/digits/hyphen/underscore only, may not begin with "sol_id_"; unique per document type; a field linked to one document kind cannot link to the other; path: allowed characters and each step must exist, only relational steps until the last. sale_pdf_quote_builder/models/sale_pdf_form_field.py:44-120
- C3. ACLs: sales managers full on header/footer documents; other internal users read; form fields: system administrators full, internal users read. sale_pdf_quote_builder/security/ir.model.access.csv:2-5
- C4. Record rule: header/footer visible if no company or in the user's active company hierarchy. sale_pdf_quote_builder/security/ir_rules.xml:5-10. Company consistency is auto-checked on documents/templates. sale_pdf_quote_builder/models/quotation_document.py:19,43; sale_pdf_quote_builder/models/sale_order_template.py:8
- C5. Template links on documents are visible to salespeople only; product documents chosen on lines are read with elevated rights so users without product-document access still see them in the dialog. sale_pdf_quote_builder/models/quotation_document.py:42; sale_pdf_quote_builder/models/sale_order.py:113
- C6. Upload endpoint: logged-in users; writing to a template requires write access to it; the document takes the template's company or else the active company; failures roll back. sale_pdf_quote_builder/controllers/quotation_document.py:17-64. (TEST) sale_pdf_quote_builder/tests/test_pdf_quote_builder.py:288-370
- C7. Dynamic paths are followed with elevated rights "to follow the path set by the admin" — only system admins can edit paths (ACL C3), so exposure depends on admin-defined paths. sale_pdf_quote_builder/models/ir_actions_report.py:139-140

## D. Handoffs
- D1. Standard quote rendering and mail attachment: sale (report_saleorder), mail/portal. No accounting, inventory, purchase or analytic effect.
- D2. Product documents and attachments: product module document model; PDF merging library in base tools. sale_pdf_quote_builder/models/ir_actions_report.py:8-16
- D3. Cron entry (nearly never-repeating) assigns missing form fields after upgrades because files aren't readable during upgrade. sale_pdf_quote_builder/data/ir_cron.xml:4-12; sale_pdf_quote_builder/models/sale_pdf_form_field.py:183-191

## E. Configuration that changes outcomes
- E1. Per header/footer: add-by-default, template link, active, sequence. sale_pdf_quote_builder/models/quotation_document.py:33-56
- E2. Per product document: "Inside quote pdf". sale_pdf_quote_builder/models/product_document.py:16
- E3. System parameter for including documents on confirmed orders (see B9).
- E4. Form field "path" (dynamic vs manual). sale_pdf_quote_builder/models/sale_pdf_form_field.py:32-36
- E5. Language for babel formatting from the order/partner language. sale_pdf_quote_builder/models/ir_actions_report.py:48-50

## F. Effective extension path (modules)
- Depended on by: none (grep of manifests). Overrides report streams also handled by sale, account, purchase and e-invoicing modules (grep _render_qweb_pdf_prepare_streams). Extends product.document, sale.order/line/template.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end dialog behaviour (JS), portal/customer download of the merged file, and exact assertions of the 14 tests.

