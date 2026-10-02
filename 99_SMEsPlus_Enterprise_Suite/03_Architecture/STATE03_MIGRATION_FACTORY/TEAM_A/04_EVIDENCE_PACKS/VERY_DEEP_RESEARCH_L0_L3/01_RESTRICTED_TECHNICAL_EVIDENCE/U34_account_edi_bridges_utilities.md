# U34 account_edi_bridges_utilities - Restricted Technical Evidence

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

- Unit: U34 `account_edi_bridges_utilities`
- Modules (5): `account_add_gln`, `account_fleet`, `account_edi_ubl_cii`, `api_doc`, `attachment_indexation`
- Source revision: `19.0.post20260921` (Odoo 19 Community, `odoo/addons`); date: 2026-10-02
- Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Scope notes: Community only; read-only static study; DB queried for configuration/structure only (module state, seeded ids, field/selection rows, parameters, counts). One company, chart `th`, no transactions, demo not loaded. Function-ID is `FUNCTION MAPPING REQUIRED` throughout: none of the 53 existing Function-IDs matches an e-invoice, fleet-bridge, API-documentation or indexation capability. Country-specific format files inside `account_edi_ubl_cii` are FUTURE OPTIONAL COUNTRY PACK material: only their existence and extension boundary are recorded (CAP-U34-06); no country rule is asserted. No Thai statutory fact is asserted; Odoo behaviour does not prove a legal requirement.
- Prior evidence read first and not redone: U13 (breadth: VDR-U13-C079, C389, C418-C445, C452-C456, C477, C482), U21 (api_doc, attachment_indexation), U22 (account_fleet, optional field names), U24-C211, U25-C232, U27-C101-C104/C162-C164/C260/C278, U02-C227, TXA1-C296-C299, TXC-C524/C544/C545, U11-C049, TXA2-C155. This unit adds format-level mapping, pipeline ordering, constraint inventory, import retrieval/correction rules and inheritance-order findings, and refines two U13 statements (see CONTRADICTIONS).
- Cross-reference: tax hooks (aggregation, rounding, repartition, `_import_retrieve_tax*` details) belong to the tax-hooks unit (U32) and TXA1; only the e-invoice side of those hooks is recorded here.
- Helper scripts (scratchpad, not deliverables): `u34_db.sh` (DB config queries), `u34_mro.py` (simulated inheritance order of builder models), `u34_build.py`.
- Pointer convention: `module/relative/path:line`; claims table at the end (class FACT/OBSERVATION/INFERENCE/UNKNOWN).

## NOT READ / READ ONLY IN PART
- `account_edi_ubl_cii`: JavaScript/SCSS under `static/`; all `tests/` (files listed and test names noticed only; no XML fixtures read); `data/cii_22_templates.xml` legacy QWeb Factur-X templates (ids and header only); `tools/ubl_21_common.py`, `ubl_21_*.py`, `cii_facturx_invoice.py` element-order templates (structure only); `account_edi_ubl.py` lines ~1553-1670 (supplier/customer wrapper methods) and the deprecated `_ubl_add_values_*` helpers (listed, not traced); `account_edi_cii.py` lines 1130-1170 and 1345-1400; `account_edi_xml_ubl_20.py` lines 830-1095 (legacy line builders); regional builder internals (nlcius, sg, a_nz, xrechnung beyond class headers and a few overrides) by scope.
- `api_doc`: `static/src` client code (not read). `attachment_indexation`: no other file. `account_fleet`: tests read by name only. `account_add_gln`: complete.
- Not installed / not studied: `account_peppol` (network transport, IAP), all country e-invoicing packs, Enterprise `account_accountant` prediction and deferral.

## DISCOVERED SUPPORTING MODULES
- `sale_edi_ubl` and `purchase_edi_ubl_bis3` (installed; order UBL BIS 3.0 builders inheriting `account.edi.xml.ubl_bis3`; decoder priority 20 for the Peppol order customization id) - read only their manifests, `sale_order.py`/`purchase_order.py` headers (U22 covers them).
- `account_peppol_advanced_fields` (installed, deprecated): fields `peppol_*` not read by export (optional fields use `x_studio_peppol_*`).
- `account` (document import mixin `account_document_import_mixin.py`, partner `invoice_edi_format*`, tax `_import_retrieve_tax*`, `PEPPOL_DEFAULT_COUNTRIES`), `fleet` (log access file), `base` (`ir.attachment._index`, `index_content`), `account_edi`, `account_edi_proxy_client` (installed, not studied here), `account_peppol` (not installed; reads `from_peppol` context).

## CAP-U34-01 E-invoice format registry, partner electronic address and delivery-location number

**Modules in scope:** `account_edi_ubl_cii` (res_partner), `account_add_gln`

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**Claims:** VDR-U34-C001 to VDR-U34-C042 (42 claims)

### D1 Business purpose and process semantics
Business purpose: decide, per business partner, which structured e-invoice format (if any) applies to that customer, keep the partner's electronic address (scheme + endpoint) consistent and valid, and carry an optional Global Location Number on delivery addresses. Process semantics: format is chosen explicitly on the partner (stored per company by the accounting module) or suggested from the partner's country when nothing is stored; the address is auto-derived from country, VAT and company registry with sanitising rules.

### D2 Architecture, data and object relationships
Objects: `res.partner` (`invoice_edi_format` Selection extended with 7 values; `peppol_eas` Selection of 90 schemes, stored computed editable tracked; `peppol_endpoint` Char stored computed; `available_peppol_eas` Json; `is_ubl_format`, `is_peppol_edi_format` non-stored; `global_location_number` Char from `account_add_gln`). Module-level tables: `EAS_MAPPING` (62 country keys -> {scheme: partner field}), `DEPRECATED_PEPPOL_EAS` (4), `PEPPOL_ENDPOINT_INVALID_CHARS_RE_BY_EAS`. Cross-module: `account/models/partner.py:585-705` (`invoice_edi_format` compute/inverse, `invoice_edi_format_store` company-dependent char, `_get_suggested_invoice_edi_format` returns False), `account/models/company.py:34-38` (`PEPPOL_DEFAULT_COUNTRIES`).

### D3 Source, technical and workflow logic
Control flow: `_get_ubl_cii_formats_info` -> `_get_ubl_cii_formats` / `_get_ubl_cii_formats_by_country` -> `_get_suggested_ubl_cii_edi_format` (commercial partner country; DE with EAS 0204 -> xrechnung; else min sequence default 100) -> `_get_ubl_cii_edi_format` (stored `invoice_edi_format` else suggestion) used by `account.move._get_invoice_legal_documents` and `get_extra_print_items`; `_get_suggested_peppol_edi_format`/`_get_peppol_edi_format` fall back to `ubl_bis3` and are used by `_is_exportable_as_self_invoice`. Address: `_compute_peppol_eas` (country/vat/company_registry triggers) and `_compute_peppol_endpoint` (scheme trigger) call `_get_peppol_endpoint_value` and `_build_error_peppol_endpoint`; `@api.constrains('peppol_endpoint')` raises ValidationError. Important inheritance fact: the shared accounting hook `_get_suggested_invoice_edi_format` is NOT overridden here, so the partner's `invoice_edi_format` stays empty unless stored explicitly; the suggestion in this module is only used on the Export-XML fallback path and for self-billing eligibility (INFERENCE; the Send & Print default reads `partner.invoice_edi_format`, account/models/account_move_send.py:44-46).

State diagram:
- partner format: unset -> explicit [user sets invoice_edi_format]
- partner format: explicit -> unset [user selects the suggestion or clears; inverse stores False/none]
- peppol_eas: any -> recomputed [country_code/vat/company_registry change AND current scheme not in country mapping]
- peppol_endpoint: any -> sanitized/replaced [peppol_eas change AND mapped field valid]

### Ten-dimension table

| Dimension | Finding |
|---|---|
| 1 Happy path | Partner picks format, sends invoice: format drives builder selection (CAP-02). A Belgian partner with VAT only gets EAS 0208 (company_registry fallback to VAT) or 9925 depending on first valid mapped value. |
| 2 Reversal / cancel / negative path | Clearing the format: stored value becomes empty; the suggestion no longer applies in Send & Print because the shared suggestion hook returns False (INFERENCE). Endpoint validation errors are raised only on endpoint writes. |
| 3 Multi-company / data scope | invoice_edi_format_store is company-dependent (account module): each company sees its own format choice; EAS and endpoint are plain stored fields shared across companies; `available_peppol_eas` depends on company context. |
| 4 Side effects and cross-module triggers | Selection of EAS filters deprecated schemes; import matches partners by EAS+endpoint (CAP-05); GLN is used by UBL and CII delivery nodes (CAP-03). |
| 5 Configuration and optionality | Module auto-installs; `account_add_gln` auto-installs; format list extensible by `selection_add` and overriding `_get_ubl_cii_formats_info`; `_peppol_eas_endpoint_depends` and `_compute_available_peppol_eas` are marked override points. |
| 6 Validation and constraints | Endpoint rules by scheme (0208 10 digits, 0009 SIRET, 0007 10 digits, EM email, default charset 1-50). GLN: no validation. EAS selection has no constraint. |
| 7 Roles and permissions | No ACL, record rule or group seeded by either module; partner fields follow base partner rules (tracked fields write to chatter). |
| 8 Scheduled / automated behaviour | None (no cron/automation). Computed fields recompute on write only. |
| 9 Exception and failure behaviour | Invalid endpoint -> ValidationError on save. Missing country in EAS table -> no automatic scheme. A deprecated-only candidate set falls back to the full set. |
| 10 Accounting, stock, audit, security and compliance implications | Compliance: electronic address and format choices decide which invoices are exported as structured data; no Thai scheme exists in the table (RT / no statutory assertion made). No audit trail beyond field tracking. |

### DB reconciliation (config only)
DB: module `account_edi_ubl_cii` seeds 198 selection rows (invoice_edi_format 7, peppol_eas 90, tax category 10, tax exemption reason 91), fields peppol_eas/peppol_endpoint stored (tracking), 7 partners, none with scheme/endpoint/GLN, `invoice_edi_format_store` null for all; `account_add_gln`: 1 view, 4 field rows (id, display_name, GLN on partner, GLN on user), 0 ACL/rule/cron/automation.

### Unknown / Runtime list
- RT: result of the scheme/endpoint recompute for real partners (DB has none).
- UNKNOWN: whether a Thai partner can be given a usable scheme and endpoint (no Thai scheme in the list); needs a Thai pack decision, not Odoo behaviour.
- UNKNOWN: effect of clearing format on Send & Print (only inferred).

## CAP-U34-02 E-invoice export pipeline, delivery and attachment handling

**Modules in scope:** `account_edi_ubl_cii` (account_move, account_move_send, ir_actions_report, wizard, builders)

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**Claims:** VDR-U34-C043 to VDR-U34-C101 (59 claims)

### D1 Business purpose and process semantics
Business purpose: when a customer invoice or credit note is sent (or on demand) produce a structured XML in the format of the partner, keep it with the invoice, give the user a chance to see rule violations, and carry the PDF inside UBL files or a Factur-X XML inside PDFs. Process semantics: XML is built before the PDF, errors do not stop sending, success is attached at the end of the send, reset to draft detaches it.

### D2 Architecture, data and object relationships
Objects: `account.move` (`ubl_cii_xml_file` Binary attachment=True copy=False, `ubl_cii_xml_id` M2O computed, `ubl_cii_xml_filename`), `account.move.send` (abstract, hooks), `account.move.send.wizard`, `ir.actions.report`, builders `account.edi.common` -> `account.edi.ubl` / `account.edi.cii` -> `account.edi.xml.ubl_20` -> `ubl_21` -> `ubl_bis3` (+ `ubl_pint_eu`, `ubl_pint`, `ubl_cen_en16931`) -> `ubl_de`/`ubl_nl`/`ubl_sg`/`ubl_a_nz`; `account.edi.xml.cii` (Factur-X/ZUGFeRD); legacy `ubl_efff`. Element-order templates in `tools/` (`Invoice`, `CreditNote`, `DebitNote`, `Order`, `CrossIndustryInvoice`). Config: `account_edi_ubl_cii.use_new_dict_to_xml_helpers` (default True, not seeded), `account.custom_templates_facturx_list`. Cross-module: `dict_to_xml` (`account/tools`), `account.tax` aggregation API, `account_peppol` (not installed) reads context `from_peppol`.

### D3 Source, technical and workflow logic
Control flow (Send & Print): `_hook_invoice_document_before_pdf_report_render` -> `_need_ubl_cii_xml` -> `res.partner._get_edi_builder(format)._export_invoice(invoice)` -> errors? set `invoice_data['error']` + `error_but_continue` : store `ubl_cii_xml_attachment_values` + options; PDF rendered; `_hook_invoice_document_after_pdf_report_render` -> `_postprocess_invoice_ubl_xml` (UBL only) and always Factur-X embedding (`account.edi.xml.cii._export_invoice(invoice)[0]` + `OdooPdfFileWriter.addAttachment`; PDF/A conversion for FR/DE) -> `_link_invoice_documents` creates attachments as superuser. Export XML action: `action_invoice_download_ubl` -> route with allow_fallback -> `_get_invoice_legal_documents('ubl')` stored else built. Builder skeleton for BIS 3.0: `ubl_20._export_invoice` (validate taxes; `_get_invoice_node`; constraints; `dict_to_xml`) whose step hooks are overridden by `ubl_bis3` to call `account.edi.ubl._ubl_add_*` helpers. MRO simulation (u34 helper script): bis3 -> ubl_21 -> ubl_20 -> pint_eu -> pint -> cen_en16931 -> ubl -> common, so `account.edi.ubl._export_invoice` (line 2719) is shadowed (INFERENCE, RT: assumes registry bases are (own class, *_inherit parents) in order). CII path: `_export_invoice` -> `_export_invoice_new` (default) with `account.edi.cii._cii_*` node builders, else legacy QWeb `account_invoice_facturx_export_22`.

State diagram:
- XML: absent -> attached [Send & Print success]
- XML: attached -> detached [reset to draft of a sale document via _get_fields_to_detach]
- export attempt: ok -> attached | violations -> not attached, continue | tax structure invalid -> ValidationError, abort

### Ten-dimension table

| Dimension | Finding |
|---|---|
| 1 Happy path | Customer with format ubl_bis3 and complete data: XML built, PDF rendered, PDF embedded as AdditionalDocumentReference, XML attached to invoice; extra manual attachments of 6 supported MIME types embedded as well. |
| 2 Reversal / cancel / negative path | Credit note exports as CreditNote (BIS3 family); debit note exports as invoice in BIS3; reset to draft detaches the stored XML so it is rebuilt on next send; vendor bills only exported for self-billing journals. |
| 3 Multi-company / data scope | Builders use `invoice.company_id`; supplier is the company partner; swap for vendor documents; per-company formats via `invoice_edi_format_store`; attachments created with SUPERUSER but linked to the move. |
| 4 Side effects and cross-module triggers | Side effects: Factur-X embedding for every sent PDF (no country test); `from_peppol` context for a not-installed transport; attachments created as superuser; chatter not written by export. |
| 5 Configuration and optionality | Format keys on partner; parameters for legacy/new Factur-X builder and custom templates; embed only for formats with `embed_attachments`. |
| 6 Validation and constraints | Tax-structure validation raises; rule violations are returned (CAP-04); anchor-less UBL skipped; test mode skips PDF rewrite. |
| 7 Roles and permissions | XML attachments created as SUPERUSER; Export XML needs the account print permissions (route/controller outside module); self-billing needs a journal flag. |
| 8 Scheduled / automated behaviour | No cron of its own; the send flow and cron `ir_cron_account_move_send` belong to `account` (U13-C477). |
| 9 Exception and failure behaviour | Violations -> titled error, send continues; ValidationError for invalid tax distribution aborts; PDF/A conversion failure logged only; Factur-X embed errors discarded (INFERENCE RT: exceptions from tax validation propagate). |
| 10 Accounting, stock, audit, security and compliance implications | Audit: the stored XML equals what was sent; the always-embedded Factur-X is not stored separately and may be incomplete; replace for metadata conformance has no effect (INFERENCE). No Thai e-tax obligations asserted. |

### DB reconciliation (config only)
DB: 1 report action (invoice report generated by Odoo), 1 server action ((Un)Group lines by tax, code, bound to account.move form), 1 config parameter (disable_pdf_in_xml False), 0 ubl_cii_xml_file attachments, 7 journals none self-billing, no `use_new_dict_to_xml_helpers` or custom-template parameter rows. Source data files: `data/cii_22_templates.xml` (5 templates), `report/…report_templates.xml` (4 templates + 1 report), `views/account_move_views.xml` (1 server action); `data/ubl_20_templates.xml` is empty and not in the manifest.

### Unknown / Runtime list
- RT: real PDF rendering and Factur-X embedding, archival PDF conversion, XML validity against schemas.
- RT: whether Factur-X embed raises for Thai-company invoices (tax validation, seller phone/email) and thereby blocks Send & Print; to be tested.
- UNKNOWN: handling of vendor-bill self-billing stored XML on reset.
- UNKNOWN: legacy QWeb template `account_invoice_facturx_export_22` body (structure only skimmed).

## CAP-U34-03 Export field mapping: parties, taxes, currency and amounts

**Modules in scope:** `account_edi_ubl_cii` (account_edi_common, account_edi_ubl, account_edi_cii, pint layers, tax); cross-reference to tax-hooks study for the tax engine

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**Claims:** VDR-U34-C102 to VDR-U34-C179 (78 claims)

### D1 Business purpose and process semantics
Business purpose: map accounting data to standard e-invoice elements so that totals, tax categories and identifiers are verifiable by the receiver. Process semantics: all values are derived at export time from the move, its base lines (tax engine), partners, bank and company data; defaults are inferred where optional codes are missing.

### D2 Architecture, data and object relationships
Objects: `account.tax` (`ubl_cii_tax_category_code` 10 values stored, `ubl_cii_tax_exemption_reason_code` 91 values stored, `ubl_cii_requires_exemption_reason` computed), `account.move` base lines via `_get_rounded_base_and_tax_lines`, partner address/identifier fields, `res.partner.bank`, `uom.uom` external ids (28 mapped), product barcode/default_code/attributes. Constants: `TAX_EXEMPTION_MAPPING` (91), `GST_COUNTRY_CODES` (22), `EUROPEAN_ECONOMIC_AREA_COUNTRY_CODES`, `SUPPORTED_FILE_TYPES` (6). Tax-hook specifics (aggregation, rounding, repartition) are in the tax-hooks unit and TXA1; only the e-invoice side is recorded here.

### D3 Source, technical and workflow logic
Control flow: `_get_tax_category_code` -> `_get_tax_exemption_reason` -> `_ubl_default_tax_category_grouping_key` -> `_ubl_tax_totals_node_grouping_key` -> `_ubl_add_tax_totals_nodes` (3 aggregation passes: tax_total, subtotal, category) -> monetary total nodes; line nodes via `_ubl_add_line_*`; PINT layer rewrites withholding, rounding, tax currency, subtotal taxable amount (`_ubl_get_tax_subtotal_node` recomputed from line nodes for PINT) and constraints. CII: `_cii_add_invoice_config_vals` (positive price, cash rounding and early-payment extraction, 6-digit rounding) -> `_cii_get_*` nodes -> monetary summation. Legacy UBL 2.0 skeleton keeps parallel generic tax/monetary helpers (`_get_tax_total_node`, `_add_document_monetary_total_vals`) used only by non-BIS3 legacy builders. Inheritance: BIS3 delegates every step to the `_ubl_*` helpers; regional builders override identifiers, tax currency and totals keys.

State diagram:
- stateless mapping (computed per export)

### Ten-dimension table

| Dimension | Finding |
|---|---|
| 1 Happy path | Domestic standard-rated sale to a domestic customer: category S, scheme VAT, percent = tax rate; PartyTaxScheme from partner VAT; payment means 30 if bank else ZZZ; totals recomputed from base lines. |
| 2 Reversal / cancel / negative path | Credit note: CreditNote document, quantities as on lines, BillingReference from reconciled invoices; negative price lines flipped; early-payment discount mixed lines become allowance/charge pairs. |
| 3 Multi-company / data scope | Per export a single company/currency context; company currency vs invoice currency drives TaxCurrencyCode and a second TaxTotal; supplier is the company partner (commercial partner for tax id). |
| 4 Side effects and cross-module triggers | Reads optional-module fields only if modules installed (intrastat, unspsc, ro cpv, hr_edi) - none installed; reads sale links (`sale_line_ids`) if sale installed. |
| 5 Configuration and optionality | Category/reason codes optional per tax; defaults inferred; optional external-form fields `x_studio_peppol_*`; regional overrides. |
| 6 Validation and constraints | No constraint forces a reason code or category (only export rules, CAP-04). |
| 7 Roles and permissions | Mapping runs under the exporting user; no ACL difference. |
| 8 Scheduled / automated behaviour | None. |
| 9 Exception and failure behaviour | Missing partner data produces empty nodes and later rule violations rather than errors, except tax-structure ValidationError. |
| 10 Accounting, stock, audit, security and compliance implications | Compliance: tax category inference is European; Thai taxes (18 in DB) have no code, so a Thai 0% sale tax would map to E (TXA1-C299 consistent); GST list excludes TH so scheme VAT. No statutory conclusion. |

### DB reconciliation (config only)
DB: 18 taxes, 0 with category code, 0 with exemption reason code; 1 company; optional modules intrastat, unspsc, ro cpv and hr_edi not installed; sale installed (order reference path active).

### Unknown / Runtime list
- RT: produced XML for a Thai invoice; schema validity; effect of PINT taxable-amount recomputation.
- UNKNOWN: Thai statutory expectations (register entry required before any NATIVE GAP claim).

## CAP-U34-04 Export validation constraints and failure reporting

**Modules in scope:** `account_edi_ubl_cii` (common, ubl_20, cen_en16931, pint, pint_eu, bis3, xrechnung, cii)

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**Claims:** VDR-U34-C180 to VDR-U34-C215 (36 claims)

### D1 Business purpose and process semantics
Business purpose: tell the user what is missing or wrong in the data before an e-invoice is sent. Semantics: rules return readable messages; the file is still produced; only tax-structure problems raise.

### D2 Architecture, data and object relationships
Objects: result dict `{key: message}` merged across layers; helper `_check_required_fields`; `_invoice_constraints_common`; node-tree rules `_export_document_node_constraints` in `ubl_cen_en16931`, `ubl_pint`, `ubl_pint_eu`; builder constraints `ubl_20._export_invoice_constraints` (4 checks) extended by `ubl_bis3`/`ubl_de`; CII `_cii_constraints` and legacy `_export_invoice_constraints`.

### D3 Source, technical and workflow logic
Control flow: `_export_invoice` builds nodes then evaluates `_export_invoice_constraints(invoice, vals)` where BIS3 merges UBL 2.0 checks, node constraints (CEN -> PINT -> PINT-EU via inheritance order), national rules and a CEN-UBL hook. Messages are returned as a set to `account.move.send` which shows them with `error_but_continue`; the Export XML fallback returns them to the controller.

State diagram:
- messages: computed per export; no persistence

### Ten-dimension table

| Dimension | Finding |
|---|---|
| 1 Happy path | All data complete: empty set; XML attached. |
| 2 Reversal / cancel / negative path | Reversal: not applicable; credit notes use same rules. |
| 3 Multi-company / data scope | Intra-community detection uses base Europe group membership of the two partner countries. |
| 4 Side effects and cross-module triggers | Messages are shown in the send wizard; nothing is written. |
| 5 Configuration and optionality | Rule set depends on partner format; the silent Factur-X ignores messages. |
| 6 Validation and constraints | Rules listed in neutral file: tax per line, item name, one tax per line, category O isolation, party country, VAT prefix, delivery country, payment account, PINT mandatory elements, Factur-X seller phone/email/VAT/bank, DE telephone and email, NO/BE/NL national rules. |
| 7 Roles and permissions | No permissions apply; partner constraint raises ValidationError for the endpoint. |
| 8 Scheduled / automated behaviour | None. |
| 9 Exception and failure behaviour | PEPPOL-EN16931-R003 cannot fire (INFERENCE RT). Exceptions: invalid tax distribution -> ValidationError. |
| 10 Accounting, stock, audit, security and compliance implications | Audit: messages are not stored; user sees them transiently. Compliance notes only. |

### DB reconciliation (config only)
DB: no constraint rows (model constraints) for these models in scope; one partner Python constraint (peppol endpoint) is code-only.

### Unknown / Runtime list
- RT: actual message sets for sample invoices.
- UNKNOWN: coverage versus official Peppol/EN16931 schematron (only rule codes in comments were read).

## CAP-U34-05 E-invoice import: detection, decoding, retrieval and corrections

**Modules in scope:** `account_edi_ubl_cii` (account_move, account_edi_common, account_edi_ubl, account_edi_cii, facturx, ubl_20, bis3); shared dispatch in `account/models/account_document_import_mixin.py`

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**Claims:** VDR-U34-C216 to VDR-U34-C283 (68 claims)

### D1 Business purpose and process semantics
Business purpose: create vendor bills (or customer invoices) from received structured files without retyping and keep the source file. Process semantics: type detection -> decoder priority -> protected transaction -> staged decoding -> chatter log; two coexisting generations of decoder.

### D2 Architecture, data and object relationships
Objects: `file_data` dicts (`xml_tree`, `import_file_type`, `decoder_info`, `attachment`), `collected_values` dict (`to_write`, `customer_values`, `currency_values`, `partner_bank_values`, `tax_total_values`, `taxes_values`, `lines_collected_values`, `logs`), `account.move` / `account.move.line`, search plans in `account.tax`, `res.partner`, `product.product`. Model hierarchy for import: `account.edi.common` (+ `account.edi.ubl`, `account.edi.cii`) -> `account.edi.xml.ubl_20/21/bis3/...`, `account.edi.xml.cii`.

### D3 Source, technical and workflow logic
Control flow: `account.move._get_import_file_type` (AttachedDocument, CII, CustomizationID substrings, UBLVersionID) -> `_unwrap_attachment` -> `_get_edi_decoder` (priority 20 for descendants of ubl_20 and cii) -> mixin `_extend_with_attachments` with `rollbackable_transaction`. Decoder: `ubl_bis3._import_invoice_ubl_cii` -> `account.edi.ubl._ubl_import_invoice`; `account.edi.xml.cii._import_invoice_ubl_cii` -> `_cii_import_invoice`; plain UBL 2.0/2.1/E-FFF fall to `account.edi.common._import_invoice_ubl_cii` which calls `_import_fill_invoice` (legacy direct, `ubl_20:1143`). Staged order is listed in claim C-level statements; helpers share `_import_invoice_*` in common. Search plans: partner (vat, EAS/endpoint, bank [UBL], email, phone, name), product (core plan + predictive), tax (account default, predictive, price include/exclude + fiscal position, fixed fuzzy). After import `_post_process_link_to_purchase_order` may auto-group lines.

State diagram:
- file: typed -> unwrapped -> decoder chosen -> decoded | rejected(reason)
- move: draft(empty) -> draft(with lines) [import]; invoice <-> refund [sign]
- grouping: detailed -> grouped -> detailed [action, draft only]

### Ten-dimension table

| Dimension | Finding |
|---|---|
| 1 Happy path | Vendor sends BIS 3.0 XML: partner found by VAT, currency/bank/lines/taxes mapped, totals corrected within 0.03, chatter message with logs, XML bound to the bill, PDF embedded in XML attached. |
| 2 Reversal / cancel / negative path | Negative-total invoice becomes credit note; a bill that already has lines is refused; ungrouping needs stored XML. |
| 3 Multi-company / data scope | Search domains are company-checked (partner/product/tax), bank accounts created for the counterpart partner; fiscal position computed from a new move with the customer. |
| 4 Side effects and cross-module triggers | Side effects: partner creation, bank account creation, substitute PDF generation, incoterm match, optional fields, notifications for new moves (account mixin), PO linking, auto grouping. |
| 5 Configuration and optionality | Parameter `disable_pdf_in_xml`; account prediction needs `account_accountant` (absent); optional classification codes. |
| 6 Validation and constraints | Decoder reasons posted in chatter; VAT validated with setnull; unit incompatibility logged. |
| 7 Roles and permissions | Import runs as the importing user (mail alias or upload); bound XML attachment is the original; elevated rights only for the substitute PDF render and the module-state check (move_send). |
| 8 Scheduled / automated behaviour | Mixin used by journal mail alias creation and upload; no cron in this module. |
| 9 Exception and failure behaviour | Any exception inside decoding -> rollback, error text in chatter, no lines; wrapper without binary object may raise before the guarded block (INFERENCE RT). |
| 10 Accounting, stock, audit, security and compliance implications | Audit: original XML kept; log lists unmatched taxes, partner creation, rounding lines. Created partners could duplicate; Thai vendor import untested (RT). |

### DB reconciliation (config only)
DB: server action for (Un)Group; parameter `disable_pdf_in_xml`=False; 0 imported attachments; account_accountant absent (Enterprise); 7 partners.

### Unknown / Runtime list
- RT: all decoding behaviour; schema variations; large files.
- UNKNOWN: Enterprise prediction and deferral functions.
- UNKNOWN: CII import lines 1130-1170 and 1345-1400 and ubl legacy `_retrieve_*` helpers 859-900 were skimmed not fully traced.

## CAP-U34-06 Regional format boundary and dependent modules

**Modules in scope:** `account_edi_ubl_cii` (xrechnung, nlcius, sg, a_nz, efff builders; country branches in shared files); DISCOVERED `sale_edi_ubl`, `purchase_edi_ubl_bis3`, `account_peppol_advanced_fields`

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**Claims:** VDR-U34-C284 to VDR-U34-C301 (18 claims)

### D1 Business purpose and process semantics
Business purpose: record where generic e-invoicing ends and country-specific code begins, so a Thai pack can be designed as an extension. This capability does NOT study country rules (FUTURE OPTIONAL COUNTRY PACK material).

### D2 Architecture, data and object relationships
Objects: abstract models `account.edi.xml.ubl_de` (XRechnung), `ubl_nl`, `ubl_sg`, `ubl_a_nz` (all `_inherit` BIS3), `ubl_efff` (inherits ubl_20), extension points `res.partner._get_ubl_cii_formats_info`, `_get_edi_builder`, `account.move._get_import_file_type`/`_get_edi_decoder`, `selection_add` on `invoice_edi_format`. 45 modules depend on the module in source (matrix); 3 installed here.

### D3 Source, technical and workflow logic
Control flow: format key -> `_get_edi_builder` -> builder; regional builders override `_get_customization_id`, `_ubl_add_customization_id_node`, party identification, tax currency, tax totals keys, payment means, filenames and, for DE, constraints. Detection is by CustomizationID/UBLVersionID in `_get_import_file_type`; E-FFF is not returned by detection or builder mapping.

State diagram:
- not applicable (static structure)

### Ten-dimension table

| Dimension | Finding |
|---|---|
| 1 Happy path | Boundary only: no happy path studied. |
| 2 Reversal / cancel / negative path | NOT APPLICABLE — boundary/static capability |
| 3 Multi-company / data scope | NOT APPLICABLE — boundary/static capability |
| 4 Side effects and cross-module triggers | Order modules reuse BIS3 builder; sale order import posts an activity on failures. |
| 5 Configuration and optionality | Packs optional; E-FFF unreachable. |
| 6 Validation and constraints | NOT APPLICABLE — boundary/static capability |
| 7 Roles and permissions | NOT APPLICABLE — boundary/static capability |
| 8 Scheduled / automated behaviour | NOT APPLICABLE — boundary/static capability |
| 9 Exception and failure behaviour | NOT APPLICABLE — boundary/static capability |
| 10 Accounting, stock, audit, security and compliance implications | Country rules inside generic files cannot be separated without changing generic output (RISK). |

### DB reconciliation (config only)
DB: installed dependents of the module: `sale_edi_ubl`, `purchase_edi_ubl_bis3`, `account_peppol_advanced_fields`; `account_peppol` and all country e-invoicing packs not installed; no TH-specific e-invoicing module exists in source (grep, U24-C211).

### Unknown / Runtime list
- UNKNOWN: contents of regional builder rules (by design).
- RT: network transport through Peppol (module not installed).

## CAP-U34-07 Fleet vendor-bill bridge

**Modules in scope:** `account_fleet`

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**Claims:** VDR-U34-C302 to VDR-U34-C326 (25 claims)

### D1 Business purpose and process semantics
Business purpose: vehicle running costs entered as vendor bills should appear as fleet service logs automatically and let fleet users reach the bills. Process semantics: creation at first posting; deletion with the line or when the vehicle is cleared.

### D2 Architecture, data and object relationships
Objects: `account.move.line` (`vehicle_id` M2O indexed, `vehicle_log_service_ids` O2M, `need_vehicle` computed False), `fleet.vehicle` (`bill_count`, `account_move_ids`), `fleet.vehicle.log.services` (`account_move_line_id`, `account_move_state` related, `amount` computed stored tracked, `vehicle_id` computed stored required), `fleet.service.type` data record (Vendor Bill), `account.automatic.entry.wizard`.

### D3 Source, technical and workflow logic
Control flow: `account.move._post` -> super -> for each posted line with vehicle and no log (in_invoice, product) `_prepare_fleet_log_service` -> batch create -> message post. `account.move.line.write`/`unlink` -> sudo unlink of logs with `ignore_linked_bill_constraint`. Log `_compute_amount` (debit), `_inverse_amount` (UserError), `_unlink_if_no_linked_bill` (ondelete guard). Vehicle `_compute_move_ids` (group `account.group_account_readonly`).

State diagram:
- log: none -> created [first post of vendor bill line with vehicle]
- log: created -> deleted [vehicle cleared, line deleted]
- log: deletion blocked [direct delete while linked]

### Ten-dimension table

| Dimension | Finding |
|---|---|
| 1 Happy path | Bill with vehicle lines posted: logs appear with vendor and description; vehicle smart button shows bills. |
| 2 Reversal / cancel / negative path | Vehicle cleared or line deleted: logs deleted; bill reset to draft or reversed: UNKNOWN. |
| 3 Multi-company / data scope | No company field on the log in this module; bills are company-scoped; multi-company effect not studied. |
| 4 Side effects and cross-module triggers | Message on log; cost follows debit. |
| 5 Configuration and optionality | Auto-install bridge; vehicle optional (need_vehicle false). |
| 6 Validation and constraints | Cost write blocked; log delete blocked; vehicle required on log. |
| 7 Roles and permissions | Fleet officers read, managers full; accountants lack rights on the log table (risk). |
| 8 Scheduled / automated behaviour | None. |
| 9 Exception and failure behaviour | AccessError possible for poster without fleet rights (INFERENCE RT). |
| 10 Accounting, stock, audit, security and compliance implications | Accounting data is the source of truth; fleet logs derive from it; no tax or stock effect. |

### DB reconciliation (config only)
DB: 1 seeded service type (Vendor Bill) of 3 existing; 0 vehicles; 5 views; 19 fields rows; no ACL/rule/cron/automation seeded by the module.

### Unknown / Runtime list
- RT: posting with fleet vehicle lines and different user roles.
- UNKNOWN: reset to draft and reversal behaviour; multi-company.

## CAP-U34-08 Runtime API documentation service

**Modules in scope:** `api_doc`

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**Claims:** VDR-U34-C327 to VDR-U34-C353 (27 claims)

### D1 Business purpose and process semantics
Business purpose: give developers a live, permission-aware description of the installed models, fields and methods for integrations. Process semantics: group-gated read-only service with caching.

### D2 Architecture, data and object relationships
Objects: `DocController` (routes `/doc`, `/doc/<model>`, `/doc/index.html`, `/doc/index.json`, `/doc/<model>.json`, `/doc-bearer/index.json`, `/doc-bearer/<model>.json`), group `api_doc.group_allow_doc`, `ir.attachment` cached index named `odoo-doc-index-<sequence>-<hash>.json`, template `api_doc.docclient`, asset bundle `api_doc.assets`.

### D3 Source, technical and workflow logic
Control flow: request -> group check -> (index) cache key hmac(sequence, lang, group ids) -> client ETag / server attachment lookup -> `_doc_index` (modules via `ModuleGraph`, models with read access, fields with read access, public methods) -> JSON; model endpoint -> `fields_get` + `_doc_method` (introducing class via MRO, signature via inspect, docstring via docutils). Autovacuum `_gc_doc_index` deletes stale cached indexes by registry sequence.

State diagram:
- cached index: absent -> stored [first request] -> deleted [registry sequence changes, autovacuum]

### Ten-dimension table

| Dimension | Finding |
|---|---|
| 1 Happy path | Authorised caller gets index and model documents; page not frameable. |
| 2 Reversal / cancel / negative path | Unauthorised caller gets AccessError naming the group; unknown model 404. |
| 3 Multi-company / data scope | Per-database; per-caller group set in cache key; no company field. |
| 4 Side effects and cross-module triggers | Creates attachments (private) on index cache miss; logs. |
| 5 Configuration and optionality | Hidden module, auto-install, no settings. |
| 6 Validation and constraints | Group required; read access per model/field. |
| 7 Roles and permissions | Group `Technical Documentation` implied by system administrators; superuser is the only direct member in DB; bearer routes use API-key authentication then same group test. |
| 8 Scheduled / automated behaviour | Autovacuum only. |
| 9 Exception and failure behaviour | Docstring parse warnings logged; stderr captured. |
| 10 Accounting, stock, audit, security and compliance implications | Security: broad technical disclosure to group members; caches contain model names of everything the caller can read. |

### DB reconciliation (config only)
DB: 1 group row, 1 model row (extension of ir.attachment), 2 field rows, 1 view (template), 0 ACL, 0 rules, 0 cron; 0 cached index attachments exist (no /doc request made).

### Unknown / Runtime list
- RT: HTTP behaviour, bearer auth, cache sizes.
- UNKNOWN: JavaScript client (static/src) not read.

## CAP-U34-09 Attachment text indexation

**Modules in scope:** `attachment_indexation`

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**Claims:** VDR-U34-C354 to VDR-U34-C373 (20 claims)

### D1 Business purpose and process semantics
Business purpose: make uploaded Office and PDF documents searchable by text content. Process semantics: extraction when file content is stored.

### D2 Architecture, data and object relationships
Objects: `ir.attachment` (`_index_docx`, `_index_pptx`, `_index_xlsx`, `_index_opendoc`, `_index_pdf`, `_index`, `copy`), module-level LRU(1) cache, helpers `textToString`, `_clean_text_content`, `_csv_escape`; base field `index_content` (Text, readonly, not prefetched) filled by `_get_datas_related_values`.

### D3 Source, technical and workflow logic
Control flow: base `_get_datas_related_values` -> `_index(bin_data, mimetype, checksum)` -> cache by checksum -> for ftype in FTYPES call `_index_<ftype>` until non-empty -> NUL removal -> else base `_index` (text types) -> store. `copy` primes the cache.

State diagram:
- index: none -> text [content written]

### Ten-dimension table

| Dimension | Finding |
|---|---|
| 1 Happy path | Upload of a docx/xlsx/pdf: text stored. |
| 2 Reversal / cancel / negative path | Unreadable/encrypted file: empty text, no error. |
| 3 Multi-company / data scope | No company scope. |
| 4 Side effects and cross-module triggers | Cache effect; copy keeps index. |
| 5 Configuration and optionality | Optional libraries (pdfminer, openpyxl); not auto-installed. |
| 6 Validation and constraints | Errors swallowed; no limits. |
| 7 Roles and permissions | No ACL change. |
| 8 Scheduled / automated behaviour | None. |
| 9 Exception and failure behaviour | Exceptions swallowed; PDF library missing -> warning at load. |
| 10 Accounting, stock, audit, security and compliance implications | Security: server-side parsing of uploaded files without limits (RISK, not tested). |

### DB reconciliation (config only)
DB: 1 model row (ir.attachment extension), 2 field rows, 0 views/ACL/rules/cron/config; hr_recruitment depends on it.

### Unknown / Runtime list
- RT: indexing outputs and performance.
- UNKNOWN: hostile-file behaviour.

## DB RECONCILIATION SUMMARY (restored dump, config rows seeded by the five modules vs source)

| Item | account_edi_ubl_cii | account_add_gln | account_fleet | api_doc | attachment_indexation |
|---|---|---|---|---|---|
| Module state / version | installed 19.0.1.0 | installed 19.0.1.0 | installed 19.0.1.0 | installed 19.0.1.0 | installed 19.0.2.1 |
| ACL rows (source / DB) | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| Record rules (source / DB) | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| Groups (source / DB) | 0 / 0 | 0 / 0 | 0 / 0 | 1 / 1 | 0 / 0 |
| Cron jobs (source / DB) | 0 / 0 (autovacuum hook none) | 0 / 0 | 0 / 0 | 0 / 0 (1 autovacuum method) | 0 / 0 |
| Automations (base.automation) | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| Server actions | 1 / 1 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| Report actions | 1 / 1 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| Views/templates | 11 / 11 | 1 / 1 | 5 / 5 | 1 / 1 | 0 / 0 |
| Menus | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| Config parameters | 1 / 1 (disable_pdf_in_xml) | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| Data records | - | - | 1 service type / 1 | - | - |
| Models rows (ir_model_data) | 21 (15 own abstract/transient, 6 extensions) | 1 | 5 | 1 | 1 |
| Field rows | 63 | 4 | 19 | 2 | 2 |
| Selection-value rows | 198 | 0 | 0 | 0 | 0 |
| Inherit rows (ir.model.inherit) | 75 | - | - | - | - |

Source counts: data files read; ACL/rule/group/cron/automation counts from manifests and file listing (no security folder in four modules, `api_doc/security/res_groups.xml` only). Template counts: `cii_22_templates.xml` 5 + report templates 4 + form-view records 2 = 11 view rows (DB identical), plus 1 report action record and 1 server action record.

## MODULE STATUS TABLE

| Module | Matrix status before | My evidence (claims by pointer module; capabilities) | My assessment |
|---|---|---|---|
| `account_add_gln` | PARTIAL (2 pointers) | 9 claims; CAP-01 | L3-READY — thin bridge (one field, one view, no logic); claim count below 15 because nothing more exists in the module; cross-module use covered in CAP-01/03 |
| `account_fleet` | PARTIAL (14 pointers) | 24 claims; CAP-07 | L3-READY — all models, wizard, views and data read; open items: reset/reversal and multi-company effects (UNKNOWN/RT) |
| `account_edi_ubl_cii` | PARTIAL (51 pointers, curated unread areas) | 281 claims; CAP-01, CAP-02, CAP-03, CAP-04, CAP-05, CAP-06 | PARTIAL — format-level pipeline, mapping, constraint, import and boundary statements are covered (claims well above 6 x 12.9 = 77); unread: legacy QWeb template bodies, legacy skeleton line builders (ubl_20:830-1095), CII import 1130-1170/1345-1400, element-order template files, tests, static assets, regional builder internals (out of scope), and everything runtime (RT) |
| `api_doc` | PARTIAL (10 pointers) | 27 claims; CAP-08 | L3-READY — controller, group, cache and cleanup fully read; JavaScript client not read (UNKNOWN) |
| `attachment_indexation` | PARTIAL (4 pointers) | 18 claims; CAP-09 | L3-READY — whole module read (one model); runtime behaviour and limits are RT |

Total claims: 373; of which pointers into the five modules: 359; into discovered/other modules: 14.

## CONTRADICTIONS WITH EARLIER UNITS
- CONTRA VDR-U34-C085: refines VDR-U13-C430 (cites account.edi.ubl._export_invoice, ubl:2719, as the export flow; in the installed inheritance order it is shadowed by the ubl_20 skeleton for every registered builder).
- CONTRA VDR-U34-C086: refines VDR-U13-C430 (cites account.edi.ubl._export_invoice, ubl:2719, as the export flow; in the installed inheritance order it is shadowed by the ubl_20 skeleton for every registered builder).
- CONTRA VDR-U34-C273: refines VDR-U13-C441 (states tax correction 'within 0.05'; the legacy direct path has no threshold, the staged path uses 0.03).
- CONTRA VDR-U34-C274: refines VDR-U13-C441 (states tax correction 'within 0.05'; the legacy direct path has no threshold, the staged path uses 0.03).
- Consistent with and re-verified: VDR-U13-C079/C431 (tax structure validation), C421 (suggested format hook not overridden), C425 (always-on Factur-X), C435/C436 (category code logic), C389/C420 (no Thai suggestion), VDR-TXA1-C299, VDR-U22-C393 (optional field names), VDR-U22-C520 (vehicle never mandatory), VDR-U25-C232 (incoterm import only).

## RUNTIME / AWT ITEMS (RT)
- VDR-U34-C023: The country-to-scheme table (lines 58-125) lists 62 country keys; no TH key was found, so no scheme/endpoint is derived automatically for Thailand (co
- VDR-U34-C059: The builder runs with a context flag from_peppol set when Peppol is among sending methods; in Community the only reader is account_peppol/models/accou
- VDR-U34-C061: The embedded Factur-X is built unconditionally; the error set (index 1) is dropped; a ValidationError from tax-structure validation inside that builde
- VDR-U34-C070: Parameter account_edi_ubl_cii.use_new_dict_to_xml_helpers defaults to True and selects the new node builder; if false the legacy QWeb template account
- VDR-U34-C097: UNKNOWN - EVIDENCE INSUFFICIENT: stored XML lifecycle of a vendor bill (reset to draft, re-send) in a self-billing journal; _get_fields_to_detach deta
- VDR-U34-C174: With DB taxes having no codes, a domestic Thai tax of amount zero would map to category E (line 432-434) and tax scheme VAT; not executed (consistent 
- VDR-U34-C177: UNKNOWN - EVIDENCE INSUFFICIENT: standards-valid output for a Thai company (statutory requirements, seller electronic address) needs runtime testing a
- VDR-U34-C196: PEPPOL-EN16931-R003 tests `not document_node['cbc:BuyerReference'] and not document_node['cac:OrderReference']`; both are dicts created unconditionall
- VDR-U34-C213: UNKNOWN - EVIDENCE INSUFFICIENT: rule coverage versus the official Peppol business rules and message quality for a Thai user; needs runtime tests.
- VDR-U34-C220: content_1 is assigned only inside the first if-branch (line 328); when that branch is not taken the final return reads an unbound variable (would rais
- VDR-U34-C282: UNKNOWN - EVIDENCE INSUFFICIENT: import of a Thai vendor XML (no Thai sample, tax identifier format, THB currency and tax mapping).
- VDR-U34-C283: UNKNOWN - EVIDENCE INSUFFICIENT: deferral dates and account prediction are only active when account_accountant is installed (not Community); not read.
- VDR-U34-C301: UNKNOWN - EVIDENCE INSUFFICIENT: rule details inside regional builders were not studied (by scope).
- VDR-U34-C321: Create of fleet logs is not wrapped in sudo; combined with the access file a user without a fleet group cannot create them (not executed).
- VDR-U34-C325: UNKNOWN - EVIDENCE INSUFFICIENT: what happens to logs when a posted bill is reset to draft or reversed (U22-C536 same gap).
- VDR-U34-C326: UNKNOWN - EVIDENCE INSUFFICIENT: company scope of logs; this module adds no company field or rule and the fleet module was not studied.
- VDR-U34-C353: UNKNOWN - EVIDENCE INSUFFICIENT: the single-page client scripts and the method playground were not read.
- VDR-U34-C364: The content part is parsed with the default lxml parser and no size limit (compare resolve_entities=False used in the shared import layer); security i

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U34-C001 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:59 | selection=[ | OBSERVATION | restored DB | — | DB: the module seeds 198 selection-value rows: res.partner.invoice_edi_format 7, res.partner.peppol_eas 90, account.tax.ubl_cii_tax_category_code 10, account.tax.ubl_cii_tax_exemption_reason_code 91; the scheme list in source has the same entries as the 90 rows. | N-U34-003 |
| VDR-U34-C002 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:167 | def _get_ubl_cii_formats_info | FACT | always | — | Each format record has keys countries, on_peppol, sequence (optional) and embed_attachments (optional); the list of formats is the key list of this dictionary, so packs extend by overriding it. | N-U34-002 |
| VDR-U34-C003 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:173 | 'embed_attachments': True | FACT | always | — | Only the ubl_bis3 record declares embed_attachments; the other six records omit it. | N-U34-018 |
| VDR-U34-C004 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:175 | 'xrechnung': {'countries': ['DE'] | FACT | always | — | xrechnung has sequence 200 and is on Peppol; zugferd and facturx have no sequence and are not on Peppol; ubl_a_nz, ubl_sg, facturx, zugferd are marked not on Peppol; nlcius and xrechnung and ubl_bis3 are on Peppol. | N-U34-002 |
| VDR-U34-C005 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:170 | 'countries': list(PEPPOL_DEFAULT_COUNTRIES) | INFERENCE | always | — | ubl_bis3 serves the 21 countries in the accounting module list PEPPOL_DEFAULT_COUNTRIES (account/models/company.py:34-38), which does not contain TH; no other format record lists TH either, so Thailand gets no suggestion. | N-U34-008 |
| VDR-U34-C006 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:208 | return min(formats_by_country | INFERENCE | several formats serve the country | — | Suggestion for multi-format countries is the format with lowest sequence, default 100 (line 208); from lines 170-180: FR gives facturx (100) over ubl_bis3 (200), DE gives zugferd (100) over xrechnung and ubl_bis3 (200) unless EAS 0204, NL gives nlcius (100) over ubl_bis3 (200). | N-U34-007 |
| VDR-U34-C007 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:205 | if self.peppol_eas == '0204': | FACT | DE partner | — | A German partner with EAS 0204 (Leitweg-ID) is suggested xrechnung before the sequence rule is applied. | N-U34-007 |
| VDR-U34-C008 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:198 | country_code = self.commercial_partner_id._deduce_country_code() | FACT | always | — | The suggestion uses the commercial partner country deduced by the account partner helper (account/models/partner.py:1124), not the invoice or delivery address. | N-U34-019 |
| VDR-U34-C009 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:218 | if suggested_format in self.env['res.partner']._get_peppol_formats() else 'ubl_bis3' | FACT | always | — | The Peppol suggestion helper returns ubl_bis3 whenever the country suggestion is empty or not a Peppol format. | N-U34-009 |
| VDR-U34-C010 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:374 | and (invoice_edi_format := self.commercial_partner_id._get_peppol_edi_format()) | INFERENCE | vendor bill in self-billing journal | — | Self-billing eligibility calls the Peppol suggestion helper, so with the fallback of line 218 any partner can qualify; the builder must additionally declare self-billing support. | N-U34-009 |
| VDR-U34-C011 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:227 | return [format_key for format_key, format_vals in | FACT | always | — | Peppol formats are the formats flagged on_peppol: ubl_bis3, xrechnung, nlcius. | N-U34-002 |
| VDR-U34-C012 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:42 | is_peppol_edi_format = fields.Boolean | FACT | always | — | The Peppol-format flag is a compute-only boolean annotated TODO remove in master; the partner view hides its label and address blocks with invisible="1" (views/res_partner_views.xml:8-9). | N-U34-025 |
| VDR-U34-C013 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:43 | peppol_endpoint = fields.Char( | FACT | always | — | peppol_endpoint and peppol_eas are stored computed fields, editable (readonly False) and tracked in the chatter; DB confirms stored char/selection with tracking sequence 100. | N-U34-003 |
| VDR-U34-C014 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:154 | @api.constrains('peppol_endpoint') | FACT | always | — | The partner validation runs on endpoint changes only and only when both endpoint and scheme are set. | N-U34-021 |
| VDR-U34-C015 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:317 | if eas == '0208' and not | FACT | always | — | Endpoint rules: 0208 ten digits; 0009 French SIRET checksum; 0007 ten digits; EM single valid email; any other scheme only [A-Za-z0-9-._~] with length 1 to 50. | N-U34-021 |
| VDR-U34-C016 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:14 | '0208': re.compile(r'[^0-9]') | FACT | always | — | Cleaning patterns by scheme: 0208 digits only, 9925 letters b/e and digits, EM email characters; default pattern removes everything except letters, digits and - . _ ~. | N-U34-022 |
| VDR-U34-C017 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:267 | def _compute_peppol_endpoint | FACT | always | — | On a scheme change the endpoint is sanitized and replaced by the mapped partner field value only if the field and value exist and pass the validator. | N-U34-011 |
| VDR-U34-C018 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:289 | if partner.peppol_eas not in eas_to_field: | FACT | country in EAS table | — | The scheme is recomputed only when the current scheme is not a scheme of the partner country; candidates exclude deprecated schemes unless that leaves none; the first candidate with a valid mapped value wins, else the first candidate. | N-U34-010 |
| VDR-U34-C019 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:232 | return ['country_code', 'vat', 'company_registry'] | FACT | always | — | Recompute triggers for the scheme are country code, tax identifier and company registry; the list is a hook for country packs. | N-U34-010 |
| VDR-U34-C020 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:255 | country_code == 'BE' | FACT | BE partner | — | Belgian company registry fallback to the tax identifier minus its alphanumeric country prefix (country-specific code inside the shared module). | N-U34-012 |
| VDR-U34-C021 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:312 | if eas not in DEPRECATED_PEPPOL_EAS or | FACT | always | — | The selectable scheme list hides deprecated schemes unless currently selected. | N-U34-013 |
| VDR-U34-C022 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:57 | DEPRECATED_PEPPOL_EAS = {'0037', '0213', '9955', '0193'} | FACT | always | — | Four schemes are deprecated: 0037, 0213, 9955, 0193. | N-U34-013 |
| VDR-U34-C023 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:58 | EAS_MAPPING = { | INFERENCE | always | RT | The country-to-scheme table (lines 58-125) lists 62 country keys; no TH key was found, so no scheme/endpoint is derived automatically for Thailand (confirms and extends U13-C389). | N-U34-024 |
| VDR-U34-C024 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:75 | 'FR': {'0225': 'peppol_endpoint' | FACT | FR partner | — | For France the endpoint field name is a placeholder resolved through the value hook (comment on the same line); the hook returns None for 'peppol_endpoint'. | N-U34-011 |
| VDR-U34-C025 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:348 | def _import_retrieve_customer_from_eas_endpoint | FACT | import | — | Partner lookup at import by exactly matching scheme and endpoint, returning no criteria if either is missing. | N-U34-020 |
| VDR-U34-C026 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/__init__.py:12 | "xrechnung", | INFERENCE | module uninstall | — | Uninstall hook clears facturx, nlcius, ubl_a_nz, ubl_bis3, ubl_sg and xrechnung (lines 5-12); zugferd is absent from the list. | N-U34-026 |
| VDR-U34-C027 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:30 | invoice_edi_format = fields.Selection( | OBSERVATION | restored DB | — | DB: 7 partners; none has a scheme, endpoint or location number; the stored per-company format column is null for all 7, so no explicit format is set. | N-U34-027 |
| VDR-U34-C028 | FUNCTION MAPPING REQUIRED | account_add_gln/models/res_partner.py:7 | global_location_number = fields.Char | OBSERVATION | restored DB | — | DB: partner column global_location_number (char) exists; no value stored; res.users mirrors it as non-stored field; module declares 1 view and 4 field rows (display name, id, and field on partner and user). | N-U34-004 |
| VDR-U34-C029 | FUNCTION MAPPING REQUIRED | account_add_gln/__manifest__.py:8 | 'auto_install': True | FACT | always | — | The location-number module auto-installs with accounting and its manifest summary says it should later be merged into accounting. | N-U34-017 |
| VDR-U34-C030 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1684 | self.module_installed('account_add_gln') | FACT | UBL export | — | UBL builder writes the location number as DeliveryLocation ID with scheme 0088 only if the location-number module is installed and the delivery partner has one. | N-U34-014 |
| VDR-U34-C031 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:590 | 'gln': 'global_location_number' in | FACT | CII export | — | CII writes the location number only for the ship-to party (ID scheme 0088); seller and buyer parties pass gln False. | N-U34-004 |
| VDR-U34-C032 | FUNCTION MAPPING REQUIRED | account_add_gln/__manifest__.py:3 | 'summary': "This module adds the Global | INFERENCE | always | — | Manifest summary states the number identifies stock locations on delivery addresses and is "mandatory on the UBL/CII eInvoices", but no export constraint in the studied builders requires it (grep found none in constraints), so it stays optional. | N-U34-006 |
| VDR-U34-C033 | FUNCTION MAPPING REQUIRED | account_add_gln/views/res_partner_views.xml:6 | <field name="priority">15</field> | FACT | always | — | The partner view extension has priority 15 and inherits base.view_partner_form; the record name still carries the old origin label account_peppol_partner_extra_fields (line 4). | N-U34-017 |
| VDR-U34-C034 | FUNCTION MAPPING REQUIRED | account_add_gln/views/res_partner_views.xml:10 | invisible="type != 'delivery'"/> | FACT | always | — | GLN appears in the Sales and Purchases page (misc group) and in the child-contact form, both invisible unless type is delivery (lines 10 and 13). | N-U34-004 |
| VDR-U34-C035 | FUNCTION MAPPING REQUIRED | account_add_gln/__manifest__.py:6 | 'depends': ['account'], | FACT | always | — | Depends on account only; data list contains only the partner view (lines 9-11): no security file, no ACL, no rule, no menu, no cron. | N-U34-019 |
| VDR-U34-C036 | FUNCTION MAPPING REQUIRED | account_add_gln/__manifest__.py:7 | 'installable': True, | FACT | always | — | Installable, auto_install True (line 8); no post-init or uninstall hook is declared. | N-U34-017 |
| VDR-U34-C037 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:31 | selection_add=[ | FACT | always | — | invoice_edi_format selection is extended with seven choices: facturx, ubl_bis3, zugferd, xrechnung, nlcius, ubl_a_nz, ubl_sg (re-verified, U13-C419). | N-U34-001 |
| VDR-U34-C038 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/__manifest__.py:39 | 'auto_install': True, | FACT | always | — | account_edi_ubl_cii depends only on account and auto-installs; manifest also registers an uninstall hook. | N-U34-016 |
| VDR-U34-C039 | FUNCTION MAPPING REQUIRED | account/models/partner.py:673 | partner.invoice_edi_format_store = 'none' | FACT | inverse of invoice_edi_format | — | Stored values: False when the chosen format equals the suggestion, "none" when cleared, else the chosen format; compute returns False for "none" else the stored value or the suggestion hook (account/models/partner.py:661-675). | N-U34-015 |
| VDR-U34-C040 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/__manifest__.py:9 | Allows to export and import formats | FACT | always | — | Manifest description: export and import of E-FFF, UBL Bis 3, EHF3, NLCIUS, Factur-X (CII) and XRechnung (UBL); formats chosen on the journal per the text (journal option not found in this module, INFERENCE: stale text). | N-U34-005 |
| VDR-U34-C041 | FUNCTION MAPPING REQUIRED | account_add_gln/models/res_partner.py:7 | global_location_number = fields.Char(string="GLN", help="Global Location Number") | FACT | always | — | The whole model extension is one Char field; no constraint, compute or default. | N-U34-023 |
| VDR-U34-C042 | FUNCTION MAPPING REQUIRED | account_add_gln/models/res_partner.py:4 | class ResPartner(models.Model): | FACT | always | — | GLN lives on res.partner (also reaches res.users through delegation). | N-U34-006 |
| VDR-U34-C043 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:23 | ubl_cii_xml_file = fields.Binary( | FACT | always | — | The stored XML is a binary field backed by an attachment (attachment=True), not copied on duplication; ubl_cii_xml_id and ubl_cii_xml_filename are computed from the linked attachment (lines 17-31). | N-U34-029 |
| VDR-U34-C044 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:61 | fields_list.append("ubl_cii_xml_file") | FACT | reset to draft | — | The XML file field is added to the fields detached when a customer invoice is reset to draft (account/models/account_move.py:6286-6293 defines the base list and applies it to sale documents). | N-U34-044 |
| VDR-U34-C045 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:50 | 'url': f'/account/download_invoice_documents/ | FACT | Export XML action | — | Export XML downloads through the invoice-documents route with the type ubl and allow_fallback=true. | N-U34-034 |
| VDR-U34-C046 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:68 | if ubl_attachment := self.ubl_cii_xml_id: | FACT | Export XML | — | Stored XML returned first (name, xml filetype, raw content). | N-U34-034 |
| VDR-U34-C047 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:82 | xml_content, errors = builder._export_invoice(self) | FACT | Export XML fallback | — | With fallback allowed and no stored file, an on-demand build is returned with filename and the error set; it is not stored. | N-U34-034 |
| VDR-U34-C048 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:108 | 'description': _('Export XML') | FACT | print menu | — | The Export XML print item appears for posted moves that have a stored XML or could be exported. | N-U34-035 |
| VDR-U34-C049 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:363 | def _need_ubl_cii_xml | FACT | always | — | XML required: none stored, sale document or exportable self-invoice, and the format key is in the UBL/CII formats list. | N-U34-032 |
| VDR-U34-C050 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:373 | and self.journal_id.is_self_billing | FACT | vendor bill | — | Self-invoice export needs a posted purchase document in a self-billing journal and a builder whose can-export-selfbilling check is true; DB: 7 journals, none flagged self-billing. | N-U34-032 |
| VDR-U34-C051 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:27 | constraints.pop('not_sale_document', None) | FACT | send wizard | — | The send wizard drops its customer-document-only constraint for exportable self-invoices. | N-U34-032 |
| VDR-U34-C052 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:44 | alerts['account_edi_ubl_cii_configure_company'] | FACT | Peppol format selected | — | Info alerts (not blocking) ask for company or partner electronic address and offer installing the French Chorus Pro module when a customer behind it is detected; the module install check reads module state with elevated rights. | N-U34-051 |
| VDR-U34-C053 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:79 | def _get_invoice_extra_attachments | FACT | send flow | — | The stored XML is added to the invoice extra attachments for mailing. | N-U34-029 |
| VDR-U34-C054 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:94 | 'placeholder': True, | FACT | send wizard preview | — | Before sending, a placeholder attachment entry (application/xml) named by the builder appears in the wizard. | N-U34-029 |
| VDR-U34-C055 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:103 | ubl_format_info.get(edi_format, {}).get('embed_attachments') | FACT | send wizard | — | The attachment widget is displayed when the chosen format supports embedding. | N-U34-048 |
| VDR-U34-C056 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:117 | accepted_attachments = attachments.filtered(lambda attachment: attachment.mimetype in | FACT | embedding format | — | Only manual or mail-template attachments of the six supported MIME types (pdf, ods, xlsx, jpeg, png, csv; common:250-257) are embedded; others are listed as not supported. | N-U34-036 |
| VDR-U34-C057 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/wizard/account_move_send_wizard.py:19 | "Unsupported file type via %s" | FACT | send wizard | — | The wizard marks unsupported attachments with the message "Unsupported file type via <format>". | N-U34-036 |
| VDR-U34-C058 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:143 | invoice_data['error_but_continue'] = True | FACT | export violations | — | Violations are reported as a titled list and sending continues; on success attachment values bind to res_field ubl_cii_xml_file and the builder is remembered. | N-U34-033 |
| VDR-U34-C059 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:132 | .with_context(from_peppol='peppol' in invoice_data['sending_methods']) | FACT | send flow | RT | The builder runs with a context flag from_peppol set when Peppol is among sending methods; in Community the only reader is account_peppol/models/account_edi_xml_ubl_bis3.py:14, a module not installed here. | N-U34-052 |
| VDR-U34-C060 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:192 | afrelationship='/Alternative' | FACT | PDF generated | — | A Factur-X XML named factur-x.xml is embedded in the PDF with relationship Alternative. | N-U34-037 |
| VDR-U34-C061 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:170 | xml_facturx = self.env['account.edi.xml.cii']._export_invoice(invoice)[0] | FACT | format not facturx/zugferd | RT | The embedded Factur-X is built unconditionally; the error set (index 1) is dropped; a ValidationError from tax-structure validation inside that builder is not caught here. | N-U34-055 |
| VDR-U34-C062 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:173 | if tools.config['test_enable']: | FACT | test mode | — | In test mode no PDF is rewritten; a factur-x.xml attachment is created instead. | N-U34-058 |
| VDR-U34-C063 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:197 | and invoice.country_code in ('FR', 'DE') | FACT | PDF generated | — | Archival PDF conversion is attempted when (format facturx/zugferd, or customer FR/DE without EAS 0204) and the invoice country code is FR or DE and the writer is not already archival; failure only logged. | N-U34-038 |
| VDR-U34-C064 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:214 | content.replace("<pdfaid:conformance>B</pdfaid:conformance>" | INFERENCE | always | — | The result of content.replace(...) is not assigned or used, so the conformance level in the metadata stays B. | N-U34-056 |
| VDR-U34-C065 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:245 | 'Invoice': "//*[local-name()='ProjectReference' | FACT | UBL formats | — | Anchor elements for inserting additional documents: Invoice before ProjectReference/Signature/AccountingSupplierParty; CreditNote before StatementDocumentReference/OriginatorDocumentReference/Signature/AccountingSupplierParty; DebitNote before Signature/AccountingSupplierParty. | N-U34-036 |
| VDR-U34-C066 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:252 | if not anchor_elements: | FACT | UBL formats | — | If none of the anchor elements exists the embedding returns without change. | N-U34-036 |
| VDR-U34-C067 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:288 | 'cbc:EmbeddedDocumentBinaryObject': { | FACT | UBL formats | — | Each attachment becomes a cac:AdditionalDocumentReference with ID = file name, DocumentTypeCode from the builder (PDF only) and a base64 EmbeddedDocumentBinaryObject with mimeCode and filename. | N-U34-036 |
| VDR-U34-C068 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:311 | self.env['ir.attachment'].with_user(SUPERUSER_ID).create(attachments_vals) | FACT | send success | — | XML attachments are created as superuser and linked after all documents were generated; caches of the file fields are invalidated. | N-U34-054 |
| VDR-U34-C069 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/ir_actions_report.py:14 | 'account.custom_templates_facturx_list' | FACT | PDF render | — | Parameter account.custom_templates_facturx_list (comma-separated report names, default empty) triggers Factur-X embedding for a single posted customer invoice rendered with a listed template. | N-U34-047 |
| VDR-U34-C070 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:263 | 'account_edi_ubl_cii.use_new_dict_to_xml_helpers', True | FACT | CII export | RT | Parameter account_edi_ubl_cii.use_new_dict_to_xml_helpers defaults to True and selects the new node builder; if false the legacy QWeb template account_invoice_facturx_export_22 renders; DB holds no such parameter (only disable_pdf_in_xml). | N-U34-046 |
| VDR-U34-C071 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:41 | # 1. Validate the structure of | FACT | UBL 2.0/2.1/BIS3 export | — | Skeleton export: validate taxes, build the node tree, run constraints into a set of messages, render with the dictionary-to-XML helper and return bytes plus the message set. | N-U34-033 |
| VDR-U34-C072 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:402 | error_msg = _("Tax '%(tax_name)s' is invalid | FACT | export | — | A tax with an invalid repartition structure raises a ValidationError naming the tax (re-verified, U13-C079/C431). | N-U34-053 |
| VDR-U34-C073 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:161 | 'document_type': 'debit_note' if 'debit_origin_id' | FACT | UBL export | — | Document type: debit_note if the move has a debit origin, credit_note for out_refund/in_refund, else invoice. | N-U34-040 |
| VDR-U34-C074 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:269 | if vals['document_type'] == 'debit_note': | FACT | BIS3 family | — | BIS 3.0 has no debit note specification and exports debit notes as invoices. | N-U34-040 |
| VDR-U34-C075 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:234 | if vals['document_type'] == 'invoice': | FACT | BIS3 family | — | BIS3 line nodes are produced only for invoice and credit note document types. | N-U34-040 |
| VDR-U34-C076 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:157 | supplier, customer = customer, supplier | FACT | vendor document | — | For purchase documents supplier and customer are swapped and the shipping partner becomes the customer. | N-U34-041 |
| VDR-U34-C077 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2707 | customer = invoice.company_id.partner_id | FACT | self-billing | — | Self-billed documents (in_invoice, in_refund) put the company as customer and the vendor partner as supplier with a delivery child partner. | N-U34-041 |
| VDR-U34-C078 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2605 | document_type = 'self_invoice' | FACT | always | — | Document types: out_invoice invoice, out_refund credit_note, in_invoice self_invoice, in_refund self_credit_note. | N-U34-041 |
| VDR-U34-C079 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:358 | def _can_export_selfbilling | FACT | always | — | Self-billing support defaults to false and is turned on by the BIS3 builder only when it has a selfbilling customization identifier. | N-U34-041 |
| VDR-U34-C080 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_xrechnung.py:32 | def _get_customization_id(self, process_type='billing'): | FACT | XRechnung | — | The German XRechnung builder returns an identifier for billing only, so self-billing is unavailable there. | N-U34-041 |
| VDR-U34-C081 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2611 | def _preprocess_base_lines | FACT | UBL export | — | Lines under a section flagged collapse_composition are replaced by one line per tax group named after the section; nested collapsed subsections are not roots. | N-U34-042 |
| VDR-U34-C082 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_efff.py:20 | return 'efff_%s%s%s.xml' | FACT | E-FFF | — | The Belgian legacy builder names files efff_<vat>_<name>.xml with non-alphanumerics removed from the name. | N-U34-043 |
| VDR-U34-C083 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:39 | return f"{invoice.name.replace('/', '_')}_zugferd.xml" | FACT | CII export | — | CII file name is _zugferd.xml for German commercial partners else _factur_x.xml. | N-U34-043 |
| VDR-U34-C084 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:42 | return f"{invoice.name.replace('/', '_')}_ubl_bis3.xml" | FACT | BIS3 export | — | Other builders use _ubl_20.xml, _ubl_21.xml, _ubl_bis3.xml, _xrechnung.xml (and regional suffixes in their classes). | N-U34-043 |
| VDR-U34-C085 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2740 | return etree.tostring(xml_content, xml_declaration=True, encoding='UTF-8'), set(errors) | INFERENCE | models with no ubl_20 in MRO | CONTRA | account.edi.ubl._export_invoice is shadowed for ubl_20, ubl_21, ubl_bis3 and all regional builders because ubl_20 appears earlier in their inheritance order; grep found no other caller of _export_document or _fill_document_values in Community, so that procedure is unreachable in the installed set (simulated inheritance order; refines U13-C430). | N-U34-057 |
| VDR-U34-C086 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:57 | # OVERRIDE | FACT | BIS3 family | CONTRA | BIS3 overrides the legacy step hooks (party, delivery, allowance, monetary total, payment, tax total, line nodes) to call the newer node helpers; the old template-method skeleton still drives the order of steps. | N-U34-057 |
| VDR-U34-C087 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:123 | def _get_invoice_node(self, vals): | FACT | UBL skeleton | — | Step order: config values, base lines, currency, tax grouping, line setup, monetary totals; then header, supplier, customer, seller; delivery, payment means and terms for invoices only (UBL 2.1 adds them to other document types); lines, document allowances, exchange rate, tax total, monetary total, optional fields. | N-U34-030 |
| VDR-U34-C088 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_21.py:24 | # In UBL 2.1, Delivery, PaymentMeans, | FACT | UBL 2.1 | — | UBL 2.1 adds delivery, payment means and payment terms to non-invoice documents. | N-U34-030 |
| VDR-U34-C089 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:170 | 'ram:ID': {'_text': "urn:cen.eu:en16931:2017#conformant#urn:factur-x.eu:1p0:extended"} | FACT | CII export | — | The CII guideline identifier is the Factur-X extended profile. | N-U34-030 |
| VDR-U34-C090 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:177 | 'ram:TypeCode': {'_text': '380' if invoice.move_type == | FACT | CII export | — | CII type code is 380 for out_invoice and 381 for every other move type. | N-U34-081 |
| VDR-U34-C091 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:184 | 'proforma_pdf_attachment_values'] | FACT | PDF generated | — | The PDF used for embedding is the stored invoice PDF unless custom-template mode, else the freshly rendered or proforma PDF values. | N-U34-037 |
| VDR-U34-C092 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:128 | if invoice.with_context(sending_method=invoice_data['sending_methods'])._need_ubl_cii_xml | FACT | Send and Print | — | At send time the need test runs with the sending methods in context before the PDF is rendered. | N-U34-028 |
| VDR-U34-C093 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/__manifest__.py:11 | retrieve the PDF with only the | FACT | always | — | Manifest: PDF embedded in the XML for all UBL formats so the receiver can retrieve the PDF from the XML alone (re-verified, U13-C456). | N-U34-031 |
| VDR-U34-C094 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/ir_actions_report.py:21 | and self._get_report(report_ref).report_name in custom_templates | FACT | PDF render | — | Embedding happens only for one record, a listed template, a sale document in state posted. | N-U34-039 |
| VDR-U34-C095 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:138 | if errors: | FACT | Send and Print | — | Branches: errors -> titled error + continue; else attach values; exceptions propagate. | N-U34-045 |
| VDR-U34-C096 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:55 | xml_content = dict_to_xml(document_node, nsmap=nsmap, template=template) | FACT | UBL skeleton | — | Rendering uses account.tools.dict_to_xml with namespace map and an element-order template from tools/. | N-U34-050 |
| VDR-U34-C097 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:369 | def _is_exportable_as_self_invoice | UNKNOWN | self-billing vendor bill | RT | UNKNOWN - EVIDENCE INSUFFICIENT: stored XML lifecycle of a vendor bill (reset to draft, re-send) in a self-billing journal; _get_fields_to_detach detaches only sale documents in the base. | N-U34-059 |
| VDR-U34-C098 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:34 | def _get_alerts | FACT | send wizard | — | Alerts and attachments extend the accounting send flow rather than replacing it (EXTENDS account). | N-U34-051 |
| VDR-U34-C099 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:301 | def _link_invoice_documents | FACT | send success | — | Documents are linked at the end of the send in a batch for all invoices of the send. | N-U34-054 |
| VDR-U34-C100 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:153 | invoice_data['ubl_cii_xml_options'] = { | FACT | send success | — | Options remember format and builder for the after-render hook. | N-U34-048 |
| VDR-U34-C101 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move_send.py:225 | def _needs_ubl_postprocessing | FACT | send flow | — | PDF embedding into XML is needed for every format except Factur-X and ZUGFeRD. | N-U34-049 |
| VDR-U34-C102 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:417 | if not tax: | FACT | always | — | A missing tax yields category E. | N-U34-062 |
| VDR-U34-C103 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:420 | if tax.ubl_cii_tax_category_code: | FACT | always | — | A stored category code on the tax always wins over inference. | N-U34-062 |
| VDR-U34-C104 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:424 | if customer.zip[:2] in ('35', '38'):  # | FACT | ES customer | — | Spanish customer postcodes 35/38 give L and 51/52 give M (before domestic rules); country-specific code inside the shared module. | N-U34-062 |
| VDR-U34-C105 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:435 | elif tax.has_negative_factor: | FACT | same country | — | Same-country supply: amount zero gives E, negative-factor tax gives AE, otherwise S. | N-U34-062 |
| VDR-U34-C106 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:456 | if supplier_in_eea and customer_in_eea: | FACT | cross-border with EEA party and supplier VAT | — | Cross-border with an EEA party and supplier VAT: non-zero tax gives S, zero tax gives K if both are EEA else G; otherwise non-zero S and zero E. | N-U34-062 |
| VDR-U34-C107 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:365 | note or COCONTRACTANT_DEFAULT_NOTE | FACT | BE co-contractant fiscal position | — | Belgian co-contractant fiscal position yields reason code VATEX-EU-AE with the fiscal position note or a default text (country-specific rule, boundary only). | N-U34-063 |
| VDR-U34-C108 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:482 | 'tax_exemption_reason': TAX_EXEMPTION_MAPPING.get(code | FACT | tax has reason code | — | A stored reason code maps to its standard text, or to "Exempt from tax" if the category requires a reason but the code has no text. | N-U34-063 |
| VDR-U34-C109 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:492 | tax_exemption_reason_code = 'VATEX-EU-G' | FACT | inferred G/K | — | Inferred G gets VATEX-EU-G and K gets VATEX-EU-IC; E gets the text "Exempt from tax" without a code. | N-U34-063 |
| VDR-U34-C110 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_tax.py:20 | ('B', 'B - Transferred (VAT), In | FACT | always | — | Ten category codes: AE, E, S, Z, G, O, K, L, M, B. | N-U34-064 |
| VDR-U34-C111 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_tax.py:125 | tax.ubl_cii_requires_exemption_reason = tax.ubl_cii_tax_category_code in ['AE', 'E', | FACT | always | — | Reason requested for AE, E, G, O, K; the onchange clears the reason code when not requested; the reason selection has 91 values; no constraint forces a reason when requested (no constrains decorator in the file). | N-U34-064 |
| VDR-U34-C112 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:228 | GST_COUNTRY_CODES = { | FACT | always | — | GST countries list (22 codes starting AU, NZ, IN, SG, MY, ...) does not contain TH; tax scheme is GST when the seller country is in it, else VAT (UBL builder lines 115-119). | N-U34-065 |
| VDR-U34-C113 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:115 | supplier_country_code = supplier.commercial_partner_id.country_id.code | FACT | UBL export | — | Scheme id GST if the seller country is in the GST list else VAT (CII always uses VAT, cii:90 etc.). | N-U34-065 |
| VDR-U34-C114 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:110 | or self._ubl_is_recycling_contribution_tax(tax_data) | FACT | UBL export | — | Non-percent taxes, recycling contribution taxes and excise taxes get no tax category grouping key (they are not reported as taxes). | N-U34-066 |
| VDR-U34-C115 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:47 | return tax.amount_type == 'fixed' and tax.include_base_amount | FACT | always | — | Recycling contribution = fixed amount tax included in the base; excise = code-type tax included in base (line 59). | N-U34-066 |
| VDR-U34-C116 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:292 | return tax.amount_type in ('fixed', 'code') and | FACT | always | — | Fixed or code taxes not included in the base are split into additional lines whose name is the tax name and product is emptied. | N-U34-066 |
| VDR-U34-C117 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:120 | if self._ubl_is_reverse_charge_tax(tax_data): | FACT | UBL export | — | Reverse-charge tax (percent amount_type with negative factor) is reported with percent 0.0 and the category from the inference. | N-U34-067 |
| VDR-U34-C118 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:136 | if tax_category_code == 'O': | FACT | UBL export | — | For category O no percent is reported (None); other taxes report their rate, or 0 for negative factor; withholding is rate < 0. | N-U34-068 |
| VDR-U34-C119 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:144 | # taxes of category 'O' should | FACT | UBL export | — | Category O lines may not be mixed with other categories on one document (constraint, see CAP-04). | N-U34-068 |
| VDR-U34-C120 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1238 | 'cbc:AllowanceChargeReasonCode': {'_text': 'ADK' if is_charge else | FACT | UBL line discount | — | Line discount: charge indicator true gives reason ADK "Charge", false gives 95 "Discount"; multiplier is the absolute percent, base amount the gross total. | N-U34-069 |
| VDR-U34-C121 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1959 | 'cbc:AllowanceChargeReasonCode': {'_text': 'ZZZ' if is_charge else | FACT | UBL export | — | Early payment discount lines map to allowance code 64 or charge ZZZ with text "Conditional cash/payment discount" and their tax category. | N-U34-069 |
| VDR-U34-C122 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1979 | '_text': _("General upsell") if is_charge else | FACT | UBL export | — | Global discount line maps to ADK/95 with reasons "General upsell"/"General discount". | N-U34-069 |
| VDR-U34-C123 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:15 | def _line_nodes_filter_base_lines | FACT | BIS3 family | — | Early payment, global discount and cash rounding base lines are excluded from line nodes. | N-U34-069 |
| VDR-U34-C124 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1197 | if 'bebat' in tax.name.lower(): | FACT | UBL line recycling charge | — | Reason code CAV if the tax name contains "bebat", else AEO; allowances use code 100; the CII builder has the same test at cii:383. | N-U34-089 |
| VDR-U34-C125 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:267 | def _ubl_turn_base_lines_price_unit_as_always_positive | FACT | always | — | Negative price_unit becomes positive with quantity multiplied by -1 (BR-27); applied in the CEN layer (cen:182-188) and by the CII config step (cii:45, common:376-387). | N-U34-070 |
| VDR-U34-C126 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:104 | if vals['document_node']['cbc:DocumentCurrencyCode']['_text'] != company_currency.name: | FACT | PINT/BIS3 family | — | DocumentCurrencyCode is the invoice currency; TaxCurrencyCode is the company currency name only when the two differ. | N-U34-071 |
| VDR-U34-C127 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:353 | tax_total_keys['tax_subtotal_key'] = None | FACT | foreign currency | — | With two currencies, two TaxTotal nodes appear and the one in the company currency has no TaxSubtotal. | N-U34-071 |
| VDR-U34-C128 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_xrechnung.py:38 | self._ubl_add_tax_currency_code_node_empty(vals) | FACT | XRechnung | — | The German builder declares no tax currency; the Dutch, Singapore and A-NZ builders override the same node (nl:52, sg:54, anz:38). | N-U34-071 |
| VDR-U34-C129 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2185 | iter_currency = [(currency, '_currency')] | FACT | UBL export | — | Tax totals are computed in the invoice currency and, if different, also in company currency. | N-U34-071 |
| VDR-U34-C130 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2221 | target_key = 'cac:WithholdingTaxTotal' | FACT | UBL export | — | Negative-rate (withholding) taxes go to WithholdingTaxTotal with sign -1 in the generic builder. | N-U34-073 |
| VDR-U34-C131 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:340 | WithholdingTaxTotal is not allowed. | FACT | BIS3 family via PINT layer | — | PINT layer removes withholding total, adds the withholding amount to PrepaidAmount (lines 380-395), removes it from rounding (357-378) and writes a note "The prepaid amount of %s corresponds to the withholding tax applied." (lines 61-65). | N-U34-073 |
| VDR-U34-C132 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1128 | '_text': FloatFmt(raw_gross_price_unit, min_dp=1, max_dp=10) | FACT | UBL export | — | Item price amount is formatted with 1 to 10 decimals. | N-U34-072 |
| VDR-U34-C133 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1316 | gross_total_excluded = currency.round(tax_details[f'raw_gross_total_excluded{suffix}']) | FACT | UBL export | — | Line extension amount = rounded gross total excluded adjusted by line allowance charges (+charge, -allowance). | N-U34-072 |
| VDR-U34-C134 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2329 | tax_exlusive_amount += sign * allowance_charge_node['cbc:Amount']['_text'] | FACT | UBL export | — | Tax-exclusive amount = sum of line extension amounts + charges - allowances at document level. | N-U34-072 |
| VDR-U34-C135 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2416 | node['cbc:PayableAmount']['_text'] = FloatFmt( | FACT | invoice/credit note | — | Payable = amount_residual and Prepaid = amount_total - amount_residual (company currency variant uses signed amounts). | N-U34-072 |
| VDR-U34-C136 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2446 | payable_rounding_amount = expected_tax_inclusive_amount - tax_inclusive_amount | FACT | UBL export | — | PayableRoundingAmount is the difference between the tax-inclusive total recomputed from base lines and the written one; written only when non-zero. | N-U34-072 |
| VDR-U34-C137 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:24 | 'uom.product_uom_unit': 'C62', | FACT | always | — | UN/ECE unit table has 28 external-id keys (unit C62, dozen, kg, g, day, hour ... kWh). | N-U34-074 |
| VDR-U34-C138 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:344 | return UOM_TO_UNECE_CODE.get(xmlid[uom.id], 'C62') | FACT | always | — | A unit without an external id or not in the table exports as C62. | N-U34-074 |
| VDR-U34-C139 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:970 | 'schemeID': '0160',  # GTIN | FACT | UBL export | — | Item seller identification = default_code; standard identification = barcode with scheme 0160. | N-U34-075 |
| VDR-U34-C140 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1031 | if self.module_installed('account_intrastat'): | FACT | optional modules | — | Commodity classification nodes are emitted only for installed modules account_intrastat (HS), product_unspsc (TST), l10n_ro_cpv_code, l10n_hr_edi; none of the four is installed in the restored DB. | N-U34-075 |
| VDR-U34-C141 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:986 | for value in product.product_template_attribute_value_ids | FACT | UBL export | — | Variant attribute values become AdditionalItemProperty name/value pairs. | N-U34-075 |
| VDR-U34-C142 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:940 | description = line_name.replace(name, '').strip() | FACT | UBL export | — | Item name is the product display name and description the line text minus the product name. | N-U34-075 |
| VDR-U34-C143 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1382 | name = partner.display_name | FACT | UBL export | — | Party name uses the partner display name when it has a name, else the commercial partner display name. | N-U34-076 |
| VDR-U34-C144 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:143 | node['cbc:CountrySubentityCode'] = None | FACT | PINT/BIS3 family | — | The Peppol profile removes state code and country name from address nodes. | N-U34-076 |
| VDR-U34-C145 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:164 | if not nodes and commercial_partner.ref and | FACT | PINT/BIS3 family | — | Party identification falls back to the partner reference except for Danish partners. | N-U34-076 |
| VDR-U34-C146 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1424 | if country_code == 'HU' and not | FACT | UBL export | — | Tax identifier prefix repair: HU gets "HU"+first 8 chars; DK gets "DK" prefix; the tax scheme id VAT/GST wraps it (country-specific code in shared module). | N-U34-076 |
| VDR-U34-C147 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1448 | if commercial_partner.peppol_eas in ('0106', '0190'): | FACT | UBL export | — | Legal entity identifier: NL KvK/OIN, LU, SE, BE (0208), DK, AU (0151), NZ (0088) rules, then tax identifier, then endpoint as fallbacks; country-specific rules in shared module. | N-U34-076 |
| VDR-U34-C148 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1684 | if self.module_installed('account_add_gln') and delivery_partner.global_location_number: | FACT | UBL export | — | Delivery node: actual delivery date from invoice.delivery_date; GLN with scheme 0088; delivery party sub-nodes (empty in PINT, pint:222-238). | N-U34-077 |
| VDR-U34-C149 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:257 | payment_means_code, payment_means_name = 57, 'standing agreement' | FACT | PINT/BIS3 family | — | Payment means: out_invoice with bank 30, without bank ZZZ, other documents 57; payee account node only if a bank is set. | N-U34-078 |
| VDR-U34-C150 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint_eu.py:64 | node['cbc:PaymentMeansCode']['_text'] = 1 | FACT | DK customer | — | Danish customers get payment means code 1 unknown (also in the legacy skeleton, ubl_20:333). | N-U34-078 |
| VDR-U34-C151 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1908 | 'cbc:ID': {'_text': partner_bank.sanitized_acc_number}, | FACT | UBL export | — | Payee financial account ID is the sanitized account number; the BIC branch node comes from bank_id (removed in PINT). | N-U34-078 |
| VDR-U34-C152 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:123 | preceding_invoice_names = [ | FACT | credit note | — | Credit note BillingReference lists names of invoices matched through the receivable lines (excluding "/"). | N-U34-079 |
| VDR-U34-C153 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:20 | vals['document_node']['cbc:InvoiceTypeCode']['_text'] = 380 | FACT | always | — | Invoice type 380, self-invoice 389, credit note 381, self credit note 261. | N-U34-079 |
| VDR-U34-C154 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1860 | order_ref_node['cbc:ID']['_text'] = invoice.ref or invoice.name | FACT | UBL export | — | OrderReference ID = customer reference or invoice name; SalesOrderID = sales order names if sale installed. | N-U34-079 |
| VDR-U34-C155 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:111 | if customer_ref := customer.ref or customer.commercial_partner_id.ref: | FACT | PINT/BIS3 family | — | BuyerReference = customer ref or commercial partner ref. | N-U34-079 |
| VDR-U34-C156 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint_eu.py:14 | 'urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0' | FACT | BIS3 | — | BIS 3.0 CustomizationID and ProfileID (lines 14, 21) with selfbilling variants (16, 23). | N-U34-079 |
| VDR-U34-C157 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:471 | if siret.is_valid(legal_organization_val): | FACT | CII export | — | Seller legal organization ID uses scheme 0002 and first 9 digits when the company registry is a valid SIRET (French rule in shared module). | N-U34-080 |
| VDR-U34-C158 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:474 | supplier_vat = invoice.fiscal_position_id.foreign_vat or commercial_partner.vat | FACT | CII export | — | Seller tax registration uses the fiscal position foreign VAT when set, scheme VA. | N-U34-080 |
| VDR-U34-C159 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:513 | 'ram:URIID': { | FACT | CII export | — | Electronic address emitted as URIUniversalCommunication with scheme from partner EAS when both EAS and endpoint exist. | N-U34-080 |
| VDR-U34-C160 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:13 | PAYMENT_MEAN_CODES = { | FACT | CII export | — | CII payment means: 42 bank transfer; 59 SEPA direct debit when a payment of the invoice has an SDD mandate (field presence tested). | N-U34-080 |
| VDR-U34-C161 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:631 | if invoice.partner_bank_id.acc_type == 'iban': | FACT | CII export | — | Creditor account is IBANID for IBAN accounts else ProprietaryID, both from the sanitized number. | N-U34-080 |
| VDR-U34-C162 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:685 | billing_start_dates = [invoice.invoice_date] if invoice.invoice_date else | FACT | CII export | — | Billing period = min start (invoice date, deferral starts) to max end (due date, deferral ends). | N-U34-080 |
| VDR-U34-C163 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:708 | 'ram:ApplicableTradePaymentDiscountTerms': { | FACT | early discount term | — | Payment terms carry description, due date and early-discount days and percentage when the term has an early discount. | N-U34-080 |
| VDR-U34-C164 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:772 | '_text': FloatFmt(sum(vals['monetary_summation_node'].get(node, {}).get('_text', 0.0) | FACT | CII export | — | Grand total = line total + tax total + rounding; prepaid = grand total - residual; due payable = grand total - prepaid; all with max two decimals. | N-U34-081 |
| VDR-U34-C165 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:671 | 'ram:CalculatedAmount': { | FACT | CII export | — | ApplicableTradeTax carries calculated amount, type VAT, exemption reason and code, basis amount, category code, due-date type 5 and rate. | N-U34-080 |
| VDR-U34-C166 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:82 | if tax_category_code == 'O': | FACT | CII export | — | CII grouping key repeats the UBL logic but with scheme VAT always and no reverse-charge branch. | N-U34-080 |
| VDR-U34-C167 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:668 | 'NOT_EU_VAT' | FACT | legacy skeleton (UBL 2.0/2.1 E-FFF) | — | The legacy party node marks the tax scheme NOT_EU_VAT when the VAT lacks an alphabetic prefix, else VAT. | N-U34-076 |
| VDR-U34-C168 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/tools/ubl_20_optional_fields.py:2 | "x_studio_peppol_tax_point_date": { | FACT | optional field names present | — | Optional element map (tax point date, contract, despatch, accounting cost, order reference, invoice period, project reference; line: order line reference and buyer item id) reads fields named x_studio_peppol_* only. | N-U34-084 |
| VDR-U34-C169 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:394 | if key.startswith("x_studio_peppol") and move[key] and key | FACT | UBL 2.0 skeleton | — | Optional fields are included only when the field exists on the record and has a value. | N-U34-084 |
| VDR-U34-C170 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:156 | 'tax_category_code': self._get_tax_category_code(customer.commercial_partner_id, supplier, self.env['account.tax']), | FACT | UBL export | — | A base line with no taxes gets a default zero-percent group with category inferred for a missing tax (E) and the exempt text. | N-U34-087 |
| VDR-U34-C171 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2211 | base_lines_aggregated_values = AccountTax._aggregate_base_lines_tax_details( | FACT | UBL export | — | Tax totals use the accounting tax engine aggregation API (details in the tax hooks unit). | N-U34-085 |
| VDR-U34-C172 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:710 | '_text': invoice.invoice_payment_term_id.discount_days, | FACT | CII export | — | Payment-term early-discount days and percentage are read from the term; company registry, fiscal position and customer reference are read elsewhere (cii:470-474, 445-447). | N-U34-086 |
| VDR-U34-C173 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:409 | Otherwise, a reasonable default is provided, | FACT | always | — | Docstring: the category default is reasonable but may be inaccurate; so explicit codes on taxes are the intended configuration. | N-U34-083 |
| VDR-U34-C174 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:431 | if supplier.country_id == customer.country_id: | INFERENCE | Thai 0% sale tax with no stored code | RT | With DB taxes having no codes, a domestic Thai tax of amount zero would map to category E (line 432-434) and tax scheme VAT; not executed (consistent with TXA1-C299). | N-U34-088 |
| VDR-U34-C175 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:361 | def _get_belgian_cocontractant_note | FACT | always | — | Belgian co-contractant helper sits in the shared common builder and refers to a Belgian chart-template fiscal position record. | N-U34-091 |
| VDR-U34-C176 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2697 | vals = {'invoice': invoice.with_context(lang=invoice.partner_id.lang)} | FACT | UBL export | — | Every export creates a fresh values dictionary in the partner language; nothing is stored between exports. | N-U34-082 |
| VDR-U34-C177 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:405 | def _get_tax_category_code | UNKNOWN | Thai company | RT | UNKNOWN - EVIDENCE INSUFFICIENT: standards-valid output for a Thai company (statutory requirements, seller electronic address) needs runtime testing and a statutory register entry. | N-U34-092 |
| VDR-U34-C178 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/tools/ubl_21_invoice.py:28 | Invoice = { | FACT | UBL export | — | The Invoice template lists UBL 2.1 elements in schema order (extensions, identifiers, dates, parties, payment, tax totals, monetary total, lines). | N-U34-060 |
| VDR-U34-C179 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:287 | # [BR-S-08]/[BR-E-08]/[BR-Z-08]/... cac:TaxSubtotal -> cbc:TaxableAmount should | FACT | PINT/BIS3 family | — | Taxable amount per subtotal is recomputed from line extension amounts and allowances/charges of the same category, percent and currency so that receiver-side schematron sums hold. | N-U34-061 |
| VDR-U34-C180 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:550 | return {'tax_on_line': _("Each invoice line should | FACT | UBL/CII export | — | Common check: lines other than section/note lines that require a tax must have a tax (message "Each invoice line should have at least one tax."); combo products are exempt through _check_edi_line_tax_required (account/models/account_move_line.py:3536). | N-U34-095 |
| VDR-U34-C181 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:506 | def _check_required_fields | FACT | always | — | Required-field helper returns a message string (not an exception); a missing record, dict key or field produces a message naming field label and record. | N-U34-106 |
| VDR-U34-C182 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:1103 | 'ubl20_supplier_name_required' | FACT | UBL 2.0 skeleton | — | Four keyed checks: supplier name, customer commercial-partner name, invoice name, invoice date. | N-U34-096 |
| VDR-U34-C183 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:124 | constraints['cen_en16931_item_name'] | FACT | BIS3 family | — | BR-25: every line node needs an item name, else "Each invoice line should have a product or a label." | N-U34-097 |
| VDR-U34-C184 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:141 | constraints['cen_en16931_tax_line'] | FACT | BIS3 family | — | UBL-SR-48: each line must have exactly one tax category (message "one and only one tax"). | N-U34-097 |
| VDR-U34-C185 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:153 | constraints['cen_en16931_tax_category_o'] | FACT | BIS3 family | — | BR-O-02: category O must not be mixed with other categories (split the invoice). | N-U34-097 |
| VDR-U34-C186 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:162 | constraints[f'cen_en16931_{role}_country'] | FACT | BIS3 family | — | BR-09/BR-11: seller and buyer postal address need a country code. | N-U34-097 |
| VDR-U34-C187 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:172 | constraints[f'cen_en16931_{role}_vat_country_code'] | FACT | BIS3 family | — | BR-CO-09: a VAT-scheme tax identifier must start with two letters. | N-U34-097 |
| VDR-U34-C188 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:179 | constraints['cen_en16931_delivery_address'] | FACT | BIS3 family | — | BR-57: delivery address needs a country (checked on the shipping partner). | N-U34-097 |
| VDR-U34-C189 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:115 | constraints['cen_en16931_payment_account_identifier'] | FACT | BIS3 family | — | BR-61: payment means code 30 or 58 require a bank account on the invoice. | N-U34-097 |
| VDR-U34-C190 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:88 | eu_countries = self.env.ref('base.europe').country_ids | FACT | BIS3 family | — | Intra-community supply is detected as customer and supplier in the base Europe country group and in different countries. | N-U34-098 |
| VDR-U34-C191 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:107 | constraints['cen_en16931_delivery_date_invoicing_period'] | FACT | intra-community | — | BR-IC-11/12: delivery address node and (delivery date or invoicing period) must be present for intra-community supply. | N-U34-098 |
| VDR-U34-C192 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:472 | constraints['ibr_081_seller_endpoint_required'] | FACT | PINT/BIS3 family | — | IBR-081/062 and IBR-080/063: seller and buyer electronic address and its scheme are required. | N-U34-099 |
| VDR-U34-C193 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:439 | constraints['ibr_003_issue_date_required'] | FACT | PINT/BIS3 family | — | IBR-003/005/006/007/009/011/016 mandatory header and party checks (issue date, currency, seller and buyer name and country, at least one line). | N-U34-099 |
| VDR-U34-C194 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:534 | constraints[f'ibr_023_line_unit_code_required_{line_idx}'] | FACT | PINT/BIS3 family | — | Per-line checks IBR-022 to IBR-027 and IBR-SR-58: quantity, unit code, net amount, item name, net price present, price not negative, tax category present. | N-U34-099 |
| VDR-U34-C195 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:588 | constraints[f'ibr_038_charge_reason_required_{charge_idx}'] | FACT | PINT/BIS3 family | — | Allowance and charge checks IBR-031/033/036/038: amount and reason or reason code are required. | N-U34-099 |
| VDR-U34-C196 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint_eu.py:97 | constraints['cen_en16931_buyer_reference_and_order_reference_must_not_be_both_present'] | INFERENCE | BIS3 family | RT | PEPPOL-EN16931-R003 tests `not document_node['cbc:BuyerReference'] and not document_node['cac:OrderReference']`; both are dicts created unconditionally by the base node builders (ubl:1834, 1840), so the condition is always false and the rule cannot fire (inferred from source; not run). | N-U34-109 |
| VDR-U34-C197 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:74 | 'seller_phone': self._check_required_fields( | FACT | legacy CII path | — | Legacy CII constraints: bank account for out_invoice, seller country, seller VAT (company vat), seller phone, seller email, tax on lines, intra-community VATs, IGIC rate. | N-U34-101 |
| VDR-U34-C198 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:852 | 'seller_phone': self._check_required_fields( | FACT | CII export | — | New CII constraints require the seller commercial partner phone and the seller email unconditionally (BR-DE-6/7), and the seller VAT (line 842) and a bank account on out_invoice (lines 817-826). | N-U34-101 |
| VDR-U34-C199 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:888 | constraints['igic_tax_rate'] | FACT | ES Canary customer | — | IGIC rate must be above zero on each line when the customer postcode starts with 35 or 38 (country-specific). | N-U34-101 |
| VDR-U34-C200 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:875 | constraints.update({ | FACT | intra-community | — | Intra-community supply needs seller VAT and buyer commercial-partner VAT. | N-U34-101 |
| VDR-U34-C201 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_xrechnung.py:22 | 'bis3_de_supplier_telephone_required' | FACT | XRechnung | — | German builder adds required supplier phone and email on top of the BIS3 rules. | N-U34-102 |
| VDR-U34-C202 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:324 | 'no_r_001': _( | FACT | NO supplier | — | Norwegian supplier tax identifier must be NO + 9 digits + MVA and valid; Belgian parties with a company registry must have a valid registry number (country-specific). | N-U34-102 |
| VDR-U34-C203 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint_eu.py:106 | constraints.update({ | FACT | NL supplier | — | Dutch supplier rules NL-R-001 to NL-R-007: street, zip and city, KvK/OIN legal entity id, payment means, credit note invoice reference (country-specific, boundary only). | N-U34-102 |
| VDR-U34-C204 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:293 | constraints.update(self._export_document_node_constraints(vals)) | FACT | BIS3 family | — | BIS3 constraints = UBL 2.0 checks + node-tree checks (CEN, PINT, PINT-EU layers) + Peppol national rules + an empty CEN-UBL hook. | N-U34-093 |
| VDR-U34-C205 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:515 | if not record: | FACT | always | — | A falsy record yields the generic text "The element %(record)s is required on %(field_list)s." | N-U34-106 |
| VDR-U34-C206 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:160 | raise ValidationError(error) | FACT | partner save | — | Partner electronic address errors are raised as ValidationError on save. | N-U34-107 |
| VDR-U34-C207 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:88 | 'errors': errors, | INFERENCE | Export XML | — | Export XML fallback returns the same message set to the download handler (move:82-89); how the controller shows it is outside this module. | N-U34-110 |
| VDR-U34-C208 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:86 | 'intracom_seller_vat': self._check_required_fields(vals['record']['company_id'], 'vat') | FACT | legacy CII path | — | Legacy Factur-X path (only with the legacy parameter off) has the same rules with record-based access. | N-U34-104 |
| VDR-U34-C209 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:84 | document_node = vals['document_node'] | FACT | BIS3 family | — | Node-tree rules read the built document node; hence rules depend on the mapping logic. | N-U34-105 |
| VDR-U34-C210 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:842 | constraints['seller_identifier'] = self._check_required_fields( | INFERENCE | CII export for any company | — | Seller VAT, phone and email requirements apply regardless of country; a company without them always receives violations. | N-U34-108 |
| VDR-U34-C211 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint_eu.py:92 | # PEPPOL-EN16931-R003: A buyer reference or | FACT | BIS3 family | — | Intended rule: a buyer reference or an order reference must be provided. | N-U34-100 |
| VDR-U34-C212 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:58 | return etree.tostring(xml_content, xml_declaration=True, encoding='UTF-8'), set(errors) | FACT | skeleton export | — | Violations are returned as a set of strings (duplicates collapsed) alongside the XML bytes. | N-U34-103 |
| VDR-U34-C213 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:426 | Validates invoice constraints for PINT payload | UNKNOWN | all | RT | UNKNOWN - EVIDENCE INSUFFICIENT: rule coverage versus the official Peppol business rules and message quality for a Thai user; needs runtime tests. | N-U34-111 |
| VDR-U34-C214 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:309 | corresponds to the errors raised by | FACT | BIS3 | — | Docstring says the checks correspond to the Peppol schematron errors detected before sending. | N-U34-094 |
| VDR-U34-C215 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:546 | def _invoice_constraints_common | FACT | always | — | Shared base checks return a dictionary which builders extend. | N-U34-093 |
| VDR-U34-C216 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:255 | if etree.QName(tree).localname == 'AttachedDocument': | FACT | import | — | Detection order: AttachedDocument root, CII root tag, customization id substrings (xrechnung, NLCIUS exact, A-NZ exact, SG exact, BIS3 exact), UBLVersionID 2.0 or 2.1/2.2/2.3, then any customization id containing urn:cen.eu:en16931:2017 as bis3. | N-U34-116 |
| VDR-U34-C217 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:358 | 'priority': 20, | FACT | import | — | A file whose type is the model of ubl_20 (any descendant, including ubl_21, efff, bis3, regional) or cii (any descendant) gets decoder priority 20 and the decoder _import_invoice_ubl_cii of that model. | N-U34-117 |
| VDR-U34-C218 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:352 | *_get_child_models('account.edi.xml.ubl_20'), | FACT | import | — | Importable models are computed from registry inheritance children of ubl_20 and cii. | N-U34-117 |
| VDR-U34-C219 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:309 | def _ubl_parse_attached_document | FACT | AttachedDocument | — | The wrapper embeds the document in Attachment/EmbeddedDocumentBinaryObject (mime xml) or in ExternalReference/Description as CDATA text. | N-U34-118 |
| VDR-U34-C220 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:342 | return content_1, None | INFERENCE | wrapper without binary object | RT | content_1 is assigned only inside the first if-branch (line 328); when that branch is not taken the final return reads an unbound variable (would raise UnboundLocalError); not executed. | N-U34-141 |
| VDR-U34-C221 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:300 | embedded_file_data['import_file_type'] = self._get_import_file_type(embedded_file_data) | FACT | AttachedDocument | — | The embedded document is re-typed and recursively unwrapped. | N-U34-118 |
| VDR-U34-C222 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:566 | if invoice.invoice_line_ids: | FACT | legacy import | — | Legacy direct import refuses an invoice that already has lines (reason text from account _reason_cannot_decode_has_invoice_lines). | N-U34-119 |
| VDR-U34-C223 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:579 | move_type = 'out_' + move_type | FACT | legacy import | — | Direction prefix out_/in_ comes from the journal type; other journal types abort silently; a mismatch is repaired only between invoice and refund of the same direction. | N-U34-119 |
| VDR-U34-C224 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:1314 | if amount_node is not None and | FACT | UBL import | — | Plain UBL Invoice root with negative TaxInclusiveAmount is treated as refund with sign -1; CreditNote root is refund with sign +1. | N-U34-119 |
| VDR-U34-C225 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:417 | if move_type_code.text in ['381', '261']: | FACT | CII import | — | CII type codes 381 and 261 are refunds; 380, 389 and 527 are invoices unless grand total is negative. | N-U34-119 |
| VDR-U34-C226 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1202 | move_type = f'{prefix}_{suffix}' | FACT | staged import | — | Staged path sets the move type from journal type and refund flag and logs a conversion message. | N-U34-119 |
| VDR-U34-C227 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:3574 | def _ubl_import_invoice | FACT | staged UBL import | — | Order of stages: init collected values, document sign, move type, bank values, customer values, retrieve and create customer, dates, currency, bank retrieval, ref/origin/narration/payment reference/delivery, optional fields, incoterm, prepaid and tax totals, document allowances/charges, line values, product/uom/account/tax retrieval, base lines, write, fix taxes, fix untaxed, post-processing. | N-U34-113 |
| VDR-U34-C228 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:1488 | def _cii_import_invoice | FACT | staged CII import | — | The CII path has the same stage order with CII element paths and no incoterm, no optional-field and no bank-based partner search step. | N-U34-113 |
| VDR-U34-C229 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2758 | party_tag = "AccountingCustomerParty" if odoo_document_type == | FACT | UBL import | — | Counterpart party: customer party for customer invoices, supplier party for vendor bills; values read: company id as VAT, telephone, registration name or name, email, country, street(s), city, zip, endpoint and scheme; VAT falls back to a scheme-specific party identification. | N-U34-120 |
| VDR-U34-C230 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2801 | ResPartner._import_retrieve_customer_from_bank_account_number, | FACT | UBL import | — | UBL partner search plan: VAT, EAS+endpoint, bank account number, email, phone, name; the CII/common plan (common:1232-1240) omits the bank account step. | N-U34-120 |
| VDR-U34-C231 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1263 | if not name or not vat: | FACT | staged import | — | A missing customer is created only if name and VAT exist; existing without VAT gets the value; VAT mismatch creates a new partner and logs. | N-U34-120 |
| VDR-U34-C232 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1298 | partner_create_values['vat'], _country_code = self.env['res.partner']._run_vat_checks(country, vat, validation='setnull') | FACT | staged import | — | VAT format validation with setnull: an invalid VAT is dropped from the created partner. | N-U34-120 |
| VDR-U34-C233 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1251 | if country and country.code == 'CH': | FACT | staged import | — | VAT comparison removes spaces and dots; only Swiss VATs are normalised further (suffixes TVA/IVA/MWST). | N-U34-143 |
| VDR-U34-C234 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:617 | partner_create_values['peppol_eas'] = peppol_eas | FACT | staged import | — | Created partners receive scheme and endpoint from the file (PINT/BIS3 and CII overrides). | N-U34-120 |
| VDR-U34-C235 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1313 | Could not retrieve currency: %s. Did | FACT | staged import | — | Currency lookup: inactive logged, unknown logged and replaced by company currency; rate from the document date or today. | N-U34-121 |
| VDR-U34-C236 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1350 | partner_banks += self.env['res.partner.bank']._find_or_create_bank_account( | FACT | staged import | — | Bank accounts are found or created for the counterpart (customer for vendor bills in_invoice and out_refund; company otherwise); UserError is logged; first becomes partner_bank_id. | N-U34-122 |
| VDR-U34-C237 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1365 | search_plan.append(ProductProduct._import_retrieve_product_from_invoice_predictive) | FACT | staged import | — | Product search plan = sorted product retrieval plan of the product module then invoice-predictive. | N-U34-123 |
| VDR-U34-C238 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:3240 | 'default_code': sellers_item_id or buyers_item_id, | FACT | UBL import | — | UBL product values: barcode from StandardItemIdentification scheme 0160, default code from seller else buyer id, name, vendor partner and predictive hint; commodity classification codes HS, TST, STI and CG are captured. | N-U34-123 |
| VDR-U34-C239 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1412 | "The Unit of Measure '%(uom)s' (from | FACT | staged import | — | Unit codes map back through the UN/ECE table; incompatibility (_has_common_reference) forces an empty unit and logs a message (refines U02-C227). | N-U34-123 |
| VDR-U34-C240 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1427 | if not self.module_installed('account_accountant'): | FACT | staged import | — | Account prediction runs only if account_accountant is installed; not available in Community. | N-U34-134 |
| VDR-U34-C241 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2962 | taxes_values.setdefault(tax_key, { | FACT | UBL import | — | Document tax subtotals are keyed by (category code, rate) and sum their tax amount with document sign; subtotals in another currency than the document currency are skipped. | N-U34-124 |
| VDR-U34-C242 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1447 | AccountTax._import_retrieve_tax_from_account_default_tax, | FACT | staged import | — | Tax search plan: account default tax, invoice-predictive, price include/exclude with fiscal position, fixed allowance/charge fuzzy match (account_tax.py:5136-5245). | N-U34-124 |
| VDR-U34-C243 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5268 | orders.insert(0, 'ubl_cii_tax_category_code') | FACT | tax retrieval with e-invoice module installed | — | Core accounting retrieval adds ubl_cii_tax_category_code in (code, False) to the domain and sorts by it first only if the field exists, a core-to-bridge coupling (cross-reference to tax hooks study). | N-U34-124 |
| VDR-U34-C244 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:3339 | if charge['reason_code'] != 'AEO': | FACT | UBL import | — | A line charge with reason code AEO becomes a fixed-tax candidate named after the reason with amount charge/quantity. | N-U34-124 |
| VDR-U34-C245 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:3140 | if price_amount: | FACT | UBL import | — | UBL line pricing cases: line amount without quantity, with quantity, or neither; price base quantity and price-level allowance feed the unit price; allowances become percent discount; charges added to unit price. | N-U34-125 |
| VDR-U34-C246 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_cii.py:1274 | price_unit = round((price_subtotal + price_discount_amount) / | INFERENCE | CII import | — | CII line pricing rounds a computed unit price to two decimals in the case with quantity; the UBL equivalent (ubl:3205) has no rounding. | N-U34-090 |
| VDR-U34-C247 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1677 | new_base_line = AccountTax._prepare_base_line_for_taxes_computation(record=base_line, discount=0.0 | FACT | staged import | — | Price-included taxes add their tax amount back to the unit price; zero-total lines without discount are removed. | N-U34-126 |
| VDR-U34-C248 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1574 | base_line_kwargs['_create_values']['name'] = reason | FACT | staged import | — | Document allowances/charges become base lines with sign from the charge indicator, price from base amount times percent or from amount. | N-U34-126 |
| VDR-U34-C249 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1721 | def _import_invoice_fix_taxes_amounts | FACT | staged import | — | Tax correction distributes the file tax amounts across line tax amounts smoothly (delta distribution) and updates tax lines in a balanced context. | N-U34-127 |
| VDR-U34-C250 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:3514 | 'name': _("Rounding"), | FACT | staged import | — | Remaining untaxed difference versus document tax-exclusive amount (plus rounding) becomes a "Rounding" line without taxes. | N-U34-127 |
| VDR-U34-C251 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2931 | collected_values['logs'].append(_("A payment of %s was detected." | FACT | staged import | — | Prepaid amount is logged only. | N-U34-128 |
| VDR-U34-C252 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2851 | if odoo_document_type == 'sale' and collected_values['invoice'].quick_edit_mode: | FACT | UBL import | — | The document ID becomes the invoice name on customer invoices in quick-edit mode, else the vendor reference. | N-U34-129 |
| VDR-U34-C253 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2866 | pattern = f'{prefix}\\d{{{sequence.padding}}}{suffix}' | FACT | UBL import with purchase installed | — | If no order reference exists and purchase is installed, purchase order names are extracted from item descriptions using the purchase sequence prefix and padding. | N-U34-129 |
| VDR-U34-C254 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2910 | if len(codes) == 1: | FACT | UBL import | — | Incoterm is set only when exactly one delivery-terms code exists and matches an incoterm code. | N-U34-129 |
| VDR-U34-C255 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:3460 | if not invoice.is_purchase_document(): | FACT | UBL import | — | External-form optional fields are read only for vendor bills and only when the target field exists with a supported type. | N-U34-129 |
| VDR-U34-C256 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:642 | attachment_data = document.find('{*}Attachment/{*}EmbeddedDocumentBinaryObject') | FACT | import | — | Embedded AdditionalDocumentReference binaries of supported types become attachments named from the ID with the right extension; none if the bill already has a PDF main attachment; the PDF becomes main attachment if the main is XML. | N-U34-130 |
| VDR-U34-C257 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:3534 | invoices_by_odoo_xmlid = 'account_edi_ubl_cii.action_report_account_invoices_generated_by_odoo' | FACT | vendor bill without PDF | — | A substitute PDF "<name> - Generated by Odoo" is rendered when no PDF is embedded, no main attachment exists, the bill is a vendor bill and the parameter is not true; errors are logged and ignored. | N-U34-130 |
| VDR-U34-C258 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/data/ir_config_parameter_data.xml:5 | <field name="key">account_edi_ubl_cii.disable_pdf_in_xml</field> | OBSERVATION | restored DB | — | Parameter account_edi_ubl_cii.disable_pdf_in_xml seeded as False (noupdate) and present in DB. | N-U34-136 |
| VDR-U34-C259 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1806 | 'res_field': 'ubl_cii_xml_file', | FACT | staged import vendor bill | — | The source attachment is rebound to ubl_cii_xml_file only for purchase documents; an originator PDF becomes the main attachment. | N-U34-140 |
| VDR-U34-C260 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1826 | invoice.with_context(no_new_invoice=True).message_post(body=body, attachment_ids=attachments.ids) | FACT | staged import | — | Chatter message "Format used to import the invoice: <model name>" with the deduplicated logs and the attachments. | N-U34-132 |
| VDR-U34-C261 | FUNCTION MAPPING REQUIRED | account/models/account_document_import_mixin.py:343 | with rollbackable_transaction(self.env.cr): | FACT | import | — | Decoder call is wrapped in a commit/rollback context: commit before, run, commit again, rollback on any exception; the error is logged and posted with the text on the document (cross-reference to accounting). | N-U34-139 |
| VDR-U34-C262 | FUNCTION MAPPING REQUIRED | account/models/account_document_import_mixin.py:335 | if file_data['decoder_info'] is None or file_data['decoder_info'].get('priority', | FACT | import | — | Highest priority decoder is selected; no decoder or priority 0 means the attachment is not imported (log only). | N-U34-117 |
| VDR-U34-C263 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:113 | def action_group_ungroup_lines_by_tax | FACT | draft invoice | — | Group/ungroup toggles by regex detection of grouped line names; only draft; invoices only. | N-U34-131 |
| VDR-U34-C264 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:192 | to_create.append(Command.create({ | FACT | grouping | — | Grouped line name = "<partner> - <account code> - <tax names or Untaxed>"; quantity and price_unit from reduced base lines; extra_tax_data preserved. | N-U34-131 |
| VDR-U34-C265 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:215 | partner_name = re.escape(self.partner_id.name or self.env._("Unknown partner")) | FACT | grouping | — | A move is considered grouped when any product line name matches "<partner> - <digits> - ...". | N-U34-131 |
| VDR-U34-C266 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:134 | files_data = self._to_files_data(self.ubl_cii_xml_id) | FACT | ungrouping | — | Ungrouping replays the stored XML with its decoder after clearing lines; fails with a message if the file is absent or has no decoder. | N-U34-131 |
| VDR-U34-C267 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:244 | if last_bill_from_vendor and last_bill_from_vendor._has_lines_grouped(): | FACT | after import | — | After import the new bill is auto-grouped if the latest posted bill of the same partner and company is grouped. | N-U34-131 |
| VDR-U34-C268 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/views/account_move_views.xml:7 | <field name="group_ids" eval="[(4, ref('account.group_account_invoice'))]"/> | OBSERVATION | restored DB | — | The (Un)Group lines by tax action is a server action bound to account.move form view for group account.group_account_invoice; DB confirms one server action record of this module, state code, form views only. | N-U34-114 |
| VDR-U34-C269 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:636 | if invoice.message_main_attachment_id.mimetype == 'application/pdf': | FACT | import | — | No embedded document import when a PDF main attachment already exists ("looks already imported"). | N-U34-130 |
| VDR-U34-C270 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:2785 | if (node := party_node.find(".//{*}EndpointID")) is not | FACT | UBL import | — | Endpoint and scheme read from EndpointID/@schemeID, stripped. | N-U34-120 |
| VDR-U34-C271 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:584 | if not new and invoice.move_type != | FACT | legacy import | — | Legacy path repairs type only for invoice/refund pairs in the same direction when called by an email alias. | N-U34-133 |
| VDR-U34-C272 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1725 | tolerance = 0.03 | FACT | staged import | — | Tax correction tolerance 0.03; it applies only if all taxes were retrieved; the correction updates tax lines. | N-U34-127 |
| VDR-U34-C273 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:1269 | def _correct_invoice_tax_amount | FACT | UBL 2.0/2.1/E-FFF import | CONTRA | Legacy correction applies any rounding-level difference found for taxes matched by exact rate without tolerance although the comment in common.py:599 states under 0.05 (CONTRA with U13-C441 wording). | N-U34-142 |
| VDR-U34-C274 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:599 | # For UBL, we should override | INFERENCE | legacy import | CONTRA | Comment states 0.05; the implementation (U20:1269-1301) has no threshold; staged path uses 0.03. | N-U34-142 |
| VDR-U34-C275 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:254 | if (tree := file_data['xml_tree']) is not | FACT | import | — | Files without a parsed XML tree are not typed here and fall to the parent type detection (PDF). | N-U34-116 |
| VDR-U34-C276 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:258 | return 'account.edi.xml.cii' | FACT | import | — | Recognised input types: UBL attached document, CII CrossIndustryInvoice root, XRechnung, NLCIUS, A-NZ, SG, BIS 3.0, UBL 2.0, UBL 2.1. | N-U34-112 |
| VDR-U34-C277 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:605 | # Set XML as ubl_cii_xml_file (XML | FACT | legacy import | — | The source XML is kept as the bill XML file for vendor bills. | N-U34-115 |
| VDR-U34-C278 | FUNCTION MAPPING REQUIRED | account/models/account_document_import_mixin.py:370 | def _get_edi_decoder | FACT | import | — | Decoder dispatch hook and priority sorting are defined in the accounting mixin; this module registers decoders only. | N-U34-137 |
| VDR-U34-C279 | FUNCTION MAPPING REQUIRED | sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:382 | def _import_order_ubl(self, order, file_data, new): | FACT | DISCOVERED module installed | — | Order import is implemented in separate modules reusing the BIS3 builder (noted only). | N-U34-138 |
| VDR-U34-C280 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:3404 | if not field or field.type not | FACT | UBL import | — | Optional line fields are written only if the target field exists on the line model with a supported type and the node has a value. | N-U34-135 |
| VDR-U34-C281 | FUNCTION MAPPING REQUIRED | account/models/account_document_import_mixin.py:492 | resolve_entities=False | FACT | import | — | XML files are parsed with comments removed and entity resolution disabled; this module sets no size limit (INFERENCE from absence). | N-U34-144 |
| VDR-U34-C282 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:3574 | def _ubl_import_invoice | UNKNOWN | Thai vendor XML | RT | UNKNOWN - EVIDENCE INSUFFICIENT: import of a Thai vendor XML (no Thai sample, tax identifier format, THB currency and tax mapping). | N-U34-145 |
| VDR-U34-C283 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:3290 | def _import_ubl_invoice_line_add_deferred_dates | UNKNOWN | enterprise extension | — | UNKNOWN - EVIDENCE INSUFFICIENT: deferral dates and account prediction are only active when account_accountant is installed (not Community); not read. | N-U34-146 |
| VDR-U34-C284 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_efff.py:9 | _name = 'account.edi.xml.ubl_efff' | FACT | always | — | E-FFF is an abstract model inheriting ubl_20 with only a file-name override. | N-U34-147 |
| VDR-U34-C285 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:339 | return self.env['account.edi.xml.ubl_a_nz'] | FACT | always | — | Builder mapping covers xrechnung, facturx+zugferd (one model), ubl_a_nz, nlcius, ubl_bis3, ubl_sg; ubl_efff is not returned. | N-U34-152 |
| VDR-U34-C286 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_move.py:251 | def _get_import_file_type | INFERENCE | import | — | The file-type function (lines 251-279) never returns account.edi.xml.ubl_efff, and grep over addons finds ubl_efff only in its own file and the models import, so the Belgian legacy builder is unreachable for detection and for builder selection. | N-U34-155 |
| VDR-U34-C287 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_xrechnung.py:6 | _name = 'account.edi.xml.ubl_de' | FACT | always | — | XRechnung builder (ubl_de) inherits BIS3, overrides file name, constraints, customization id, tax currency, buyer reference, endpoint, tax scheme and legal entity nodes. | N-U34-150 |
| VDR-U34-C288 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_nlcius.py:7 | _name = 'account.edi.xml.ubl_nl' | FACT | always | — | NLCIUS builder inherits BIS3 and overrides identifiers, tax currency, tax totals key, discount node, party identifications and payment means. | N-U34-150 |
| VDR-U34-C289 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_sg.py:6 | _name = 'account.edi.xml.ubl_sg' | FACT | always | — | SG builder inherits BIS3 with customization id, tax category key, discount, tax currency, tax totals and payment means overrides. | N-U34-150 |
| VDR-U34-C290 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_a_nz.py:7 | _name = 'account.edi.xml.ubl_a_nz' | FACT | always | — | A-NZ builder inherits BIS3 with customization id, discount, tax currency, tax totals key, endpoint, tax scheme and legal entity overrides. | N-U34-150 |
| VDR-U34-C291 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl_pint.py:203 | if country_code == 'NO': | FACT | NO/SE supplier | — | Norwegian and Swedish supplier tax-status statements are appended as tax scheme nodes in the shared PINT layer. | N-U34-156 |
| VDR-U34-C292 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_ubl.py:1464 | elif commercial_partner.country_code == 'LU' and commercial_partner.company_registry: | FACT | UBL export | — | Country branches for legal entity (NL, LU, SE, BE, DK, AU, NZ) are in the shared UBL builder (U27-C101 counts 40 literal country comparisons in the module). | N-U34-156 |
| VDR-U34-C293 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/__manifest__.py:39 | 'auto_install': True, | FACT | always | — | Manifest description: E-FFF, NLCIUS and XRechnung (UBL) are only available for Belgian, Dutch and German companies and BIS 3.0 only for companies whose country is in the EAS list (lines 11-13); the manifest also sets auto_install. | N-U34-149 |
| VDR-U34-C294 | FUNCTION MAPPING REQUIRED | purchase_edi_ubl_bis3/models/purchase_order.py:28 | 'decoder': self.env['purchase.edi.xml.ubl_bis3']._import_order_ubl, | FACT | DISCOVERED module installed | — | The purchase order module registers an order decoder (priority 20) for customization id urn:fdc:peppol.eu:poacc:trns:order:3; sale_edi_ubl does the same for sale.edi.xml.ubl_bis3 (sale_edi_ubl/models/sale_order.py:28). | N-U34-154 |
| VDR-U34-C295 | FUNCTION MAPPING REQUIRED | purchase_edi_ubl_bis3/models/purchase_edi_xml_ubl_bis3.py:12 | _inherit = ['account.edi.xml.ubl_bis3'] | FACT | DISCOVERED module installed | — | Order builders inherit the invoice BIS3 builder (sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:12). | N-U34-154 |
| VDR-U34-C296 | FUNCTION MAPPING REQUIRED | account_peppol_advanced_fields/models/account_move.py:7 | peppol_contract_document_reference = fields.Char( | FACT | DISCOVERED module installed | — | The deprecated module defines peppol_* fields with [DEPRECATED] labels, while the export reads x_studio_peppol_* names (tools/ubl_20_optional_fields.py:2-50); manifest says merged prematurely, do not use. | N-U34-157 |
| VDR-U34-C297 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:367 | def _import_order_ubl(self, order, file_data, new): | FACT | DISCOVERED order modules | — | Order import (sale/purchase) shared in BIS3 builder: date, note, payment term by name, currency; posts a chatter format message and an activity listing unimported details. | N-U34-154 |
| VDR-U34-C298 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/res_partner.py:332 | def _get_edi_builder | FACT | always | — | Packs extend by selection_add, the format info dictionary and by overriding the builder selection function (re-verified, U27-C162-C164). | N-U34-151 |
| VDR-U34-C299 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/__manifest__.py:24 | 'depends': ['account'], | OBSERVATION | restored DB and matrix | — | Matrix reverse_dep_count for the module is 45 (source), DB installed dependents: sale_edi_ubl, purchase_edi_ubl_bis3, account_peppol_advanced_fields (3). | N-U34-153 |
| VDR-U34-C300 | FUNCTION MAPPING REQUIRED | sale_edi_ubl/__manifest__.py:13 | 'depends': ['sale', 'account_edi_ubl_cii'], | FACT | DISCOVERED module | — | Order modules depend on the module and auto-install; the deprecated field module depends on account and the module. | N-U34-148 |
| VDR-U34-C301 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_nlcius.py:6 | class AccountEdiXmlUbl_Nl(models.AbstractModel): | UNKNOWN | regional builders | — | UNKNOWN - EVIDENCE INSUFFICIENT: rule details inside regional builders were not studied (by scope). | N-U34-158 |
| VDR-U34-C302 | FUNCTION MAPPING REQUIRED | account_fleet/__manifest__.py:8 | 'depends': ['fleet', 'account'], | FACT | always | — | account_fleet depends on fleet and account (manifest line 8); data loaded: service type, three view files. | N-U34-170 |
| VDR-U34-C303 | FUNCTION MAPPING REQUIRED | account_fleet/models/account_move.py:16 | posted = super()._post(soft) | FACT | post | — | Posting calls the base post first, then iterates only the moves returned as posted. | N-U34-162 |
| VDR-U34-C304 | FUNCTION MAPPING REQUIRED | account_fleet/models/account_move.py:20 | or line.display_type != 'product': | FACT | post | — | A line is skipped unless it has a vehicle, no existing log, move_type in_invoice and display_type product. | N-U34-162 |
| VDR-U34-C305 | FUNCTION MAPPING REQUIRED | account_fleet/models/account_move.py:22 | val = line._prepare_fleet_log_service() | FACT | post | — | Logs are created in one batch without elevated rights, then each gets a message "Service Vendor Bill: <link>". | N-U34-171 |
| VDR-U34-C306 | FUNCTION MAPPING REQUIRED | account_fleet/models/account_move.py:47 | 'service_type_id': vendor_bill_service.id, | FACT | post | — | Log values: service type (Vendor Bill), vehicle, vendor = bill line partner, description = line name, link to the line. | N-U34-162 |
| VDR-U34-C307 | FUNCTION MAPPING REQUIRED | account_fleet/models/account_move.py:37 | need_vehicle = fields.Boolean(compute='_compute_need_vehicle') | FACT | always | — | Hook _compute_need_vehicle sets False; view makes the vehicle required only if the hook is true and the move is a vendor invoice or refund. | N-U34-169 |
| VDR-U34-C308 | FUNCTION MAPPING REQUIRED | account_fleet/models/account_move.py:55 | if 'vehicle_id' in vals and not | FACT | write on bill line | — | Clearing the vehicle deletes the line logs with the guard bypassed, under elevated rights; deleting the line does the same (line 60). | N-U34-164 |
| VDR-U34-C309 | FUNCTION MAPPING REQUIRED | account_fleet/models/fleet_vehicle_log_services.py:50 | raise UserError(_("You cannot delete log services | FACT | unlink of log | — | A log with a bill line cannot be deleted unless the bypass context is set (ondelete guard). | N-U34-172 |
| VDR-U34-C310 | FUNCTION MAPPING REQUIRED | account_fleet/models/fleet_vehicle_log_services.py:27 | raise UserError(_("You cannot modify amount of | FACT | write amount | — | Writing the cost of a bill-linked log raises an error pointing to the accounting entry. | N-U34-165 |
| VDR-U34-C311 | FUNCTION MAPPING REQUIRED | account_fleet/models/fleet_vehicle_log_services.py:32 | log_service.amount = log_service.account_move_line_id.debit | FACT | compute | — | Cost = debit of the linked line; recomputed when price_subtotal of the line changes. | N-U34-165 |
| VDR-U34-C312 | FUNCTION MAPPING REQUIRED | account_fleet/models/fleet_vehicle_log_services.py:11 | account_move_state = fields.Selection(related= | FACT | always | — | The log exposes the bill state (parent_state of the line) for the "Service's Bill" button colouring. | N-U34-160 |
| VDR-U34-C313 | FUNCTION MAPPING REQUIRED | account_fleet/models/fleet_vehicle_log_services.py:20 | # We avoid emptying the vehicle_id | FACT | compute | — | Vehicle on the log follows the line vehicle but is not emptied when the line vehicle is cleared (field required). | N-U34-166 |
| VDR-U34-C314 | FUNCTION MAPPING REQUIRED | account_fleet/wizard/account_automatic_entry_wizard.py:14 | move_line_data[2]['vehicle_id'] = aml.vehicle_id.id | FACT | period change wizard | — | Wizard-generated line on the original account keeps the vehicle. | N-U34-166 |
| VDR-U34-C315 | FUNCTION MAPPING REQUIRED | account_fleet/models/fleet_vehicle.py:14 | if not self.env.user.has_group('account.group_account_readonly'): | FACT | vehicle form | — | Bill count and list are zero for users without accounting read group. | N-U34-167 |
| VDR-U34-C316 | FUNCTION MAPPING REQUIRED | account_fleet/models/fleet_vehicle.py:22 | ('parent_state', '!=', 'cancel'), | FACT | vehicle form | — | Counted moves are those with lines of that vehicle, not cancelled, of purchase types (in_invoice, in_refund, in_receipt). | N-U34-167 |
| VDR-U34-C317 | FUNCTION MAPPING REQUIRED | account_fleet/views/account_move_views.xml:11 | column_invisible="parent.move_type not in ('in_invoice', 'in_refund', 'in_receipt')" | FACT | bill form | — | Vehicle column is visible only on vendor documents and optional hidden. | N-U34-169 |
| VDR-U34-C318 | FUNCTION MAPPING REQUIRED | account_fleet/views/fleet_vehicle_log_services_views.xml:16 | invisible="not account_move_line_id"> | FACT | log form | — | Log form shows "Service's Bill" button only when linked to a bill line; the cost field becomes readonly when linked (lines 28-30). | N-U34-160 |
| VDR-U34-C319 | FUNCTION MAPPING REQUIRED | account_fleet/views/fleet_vehicle_views.xml:9 | <button name="action_view_bills" | FACT | vehicle form | — | Vehicle form shows a Bills smart button when the count is not zero. | N-U34-159 |
| VDR-U34-C320 | FUNCTION MAPPING REQUIRED | fleet/security/ir.model.access.csv:8 | fleet_vehicle_log_services_access_right_user | FACT | DISCOVERED fleet module | — | The fleet service log table grants read to fleet officers and full access to fleet managers; the accounting groups are not listed, so a poster with accounting rights only is not covered by this file; inferred risk with line 22 of the account_fleet move model (create without elevation). | N-U34-173 |
| VDR-U34-C321 | FUNCTION MAPPING REQUIRED | account_fleet/models/account_move.py:26 | log_service_ids = self.env['fleet.vehicle.log.services'].create(val_list) | INFERENCE | poster without fleet group | RT | Create of fleet logs is not wrapped in sudo; combined with the access file a user without a fleet group cannot create them (not executed). | N-U34-173 |
| VDR-U34-C322 | FUNCTION MAPPING REQUIRED | account_fleet/data/fleet_service_type_data.xml:3 | <record id="data_fleet_service_type_vendor_bill" | OBSERVATION | restored DB | — | DB: 3 fleet service types exist, 1 of them seeded by this module (Vendor Bill, category service); 0 vehicles; no ACL, rule, cron or automation seeded by the module; 5 views and 19 field rows. | N-U34-175 |
| VDR-U34-C323 | FUNCTION MAPPING REQUIRED | account_fleet/__manifest__.py:6 | 'summary': 'Manage accounting with fleets', | FACT | always | — | Manifest summary states the purpose: manage accounting with fleets. | N-U34-161 |
| VDR-U34-C324 | FUNCTION MAPPING REQUIRED | account_fleet/models/account_move.py:11 | if not vendor_bill_service: | FACT | post | — | If the Vendor Bill service type record cannot be found, posting proceeds without creating logs (re-verified, U22-C513). | N-U34-163 |
| VDR-U34-C325 | FUNCTION MAPPING REQUIRED | account_fleet/models/account_move.py:9 | def _post(self, soft=True): | UNKNOWN | reset to draft / reversal | RT | UNKNOWN - EVIDENCE INSUFFICIENT: what happens to logs when a posted bill is reset to draft or reversed (U22-C536 same gap). | N-U34-168 |
| VDR-U34-C326 | FUNCTION MAPPING REQUIRED | account_fleet/models/fleet_vehicle_log_services.py:7 | class FleetVehicleLogServices(models.Model): | UNKNOWN | multi-company | RT | UNKNOWN - EVIDENCE INSUFFICIENT: company scope of logs; this module adds no company field or rule and the fleet module was not studied. | N-U34-174 |
| VDR-U34-C327 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:38 | @http.route(['/doc', '/doc/<model_name>', '/doc/index.html'], type='http', auth='user') | FACT | always | — | Three HTML paths serve the page for session users; response sets X-Frame-Options deny. | N-U34-183 |
| VDR-U34-C328 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:45 | res.headers['X-Frame-Options'] = 'deny' | FACT | always | — | The page cannot be framed. | N-U34-183 |
| VDR-U34-C329 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:52 | @http.route('/doc/index.json', type='json2', auth='user') | FACT | always | — | Index data endpoint for session users; a bearer variant exists for the index (line 48) and for models (line 165). | N-U34-177 |
| VDR-U34-C330 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:169 | @http.route('/doc/<model_name>.json', type='json2', auth='user', readonly=True) | FACT | always | — | Per-model endpoint is flagged readonly (read-only transaction). | N-U34-177 |
| VDR-U34-C331 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:195 | raise NotFound() | FACT | unknown model | — | Unknown model returns not found; known model requires read access (check_access read, line 198). | N-U34-180 |
| VDR-U34-C332 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:150 | if Model._has_field_access(Model._fields[field.name], 'read') | FACT | always | — | Index fields are limited to those with read access and still present in the registry. | N-U34-180 |
| VDR-U34-C333 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:161 | if (Model := self.env[ir_model.model]).has_access('read') | FACT | always | — | Index lists only models readable by the caller. | N-U34-180 |
| VDR-U34-C334 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:84 | if parse_cache_control_header(request.httprequest.headers.get('Cache-Control')).no_cache: | FACT | no-cache request | — | A client asking no-cache receives a freshly generated index with no-store and a download file name. | N-U34-182 |
| VDR-U34-C335 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:113 | filename = f'odoo-doc-index-{db_registry_sequence}-{unique}.json' | FACT | always | — | Server cache file name embeds registry sequence and the keyed hash of sequence, language and group ids. | N-U34-182 |
| VDR-U34-C336 | FUNCTION MAPPING REQUIRED | api_doc/models/ir_attachment.py:16 | [('name', 'like', R'odoo-doc-index-%-%.json')], | FACT | autovacuum | — | Autovacuum deletes cached indexes whose sequence is not the current one. | N-U34-184 |
| VDR-U34-C337 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:238 | response.headers['Cache-Control'] = 'no-cache, private' | FACT | model endpoint | — | Model response carries an ETag and no-cache,private; matching ETag returns 304. | N-U34-182 |
| VDR-U34-C338 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:152 | 'methods': [ | FACT | always | — | Methods are those where get_public_method works and the method is not deprecated (is_public_method). | N-U34-181 |
| VDR-U34-C339 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:290 | introducing_class = next( | FACT | model endpoint | — | Each method is attributed to the earliest class in the inheritance order that defines it, giving its model and module. | N-U34-181 |
| VDR-U34-C340 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:631 | 'raw_enabled': False, | FACT | docstring parsing | — | Docstrings are parsed as reStructuredText with raw content and file insertion disabled. | N-U34-181 |
| VDR-U34-C341 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:382 | isign = isign.replace(return_annotation='list[int]') | FACT | always | — | Return annotations of record-set methods are shown as list[int]; default values are exported only if JSON serialisable (lines 574-581). | N-U34-181 |
| VDR-U34-C342 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:308 | graph = ModuleGraph(env.cr) | FACT | always | — | Installed modules are listed in dependency order. | N-U34-186 |
| VDR-U34-C343 | FUNCTION MAPPING REQUIRED | api_doc/security/res_groups.xml:4 | <record model="res.groups" id="group_allow_doc"> | OBSERVATION | restored DB | — | DB: 1 group row (Technical Documentation); module seeds 0 access rows, 0 rules, 0 cron jobs; 1 view, 2 field rows, 1 model row. | N-U34-185 |
| VDR-U34-C344 | FUNCTION MAPPING REQUIRED | api_doc/__manifest__.py:3 | 'category': 'Hidden', | FACT | always | — | Module is hidden, auto-installed, depends on web, uses a bootstrap flag and its own asset bundle api_doc.assets (action script lives in the backend bundle). | N-U34-185 |
| VDR-U34-C345 | FUNCTION MAPPING REQUIRED | api_doc/views/docclient.xml:6 | <t t-set="title">Odoo Runtime Doc</t> | FACT | always | — | Page template uses the layout with title and the dedicated assets bundle. | N-U34-177 |
| VDR-U34-C346 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:100 | message=( | FACT | always | — | Cache key message is (registry sequence, language, sorted group ids of the caller). | N-U34-182 |
| VDR-U34-C347 | FUNCTION MAPPING REQUIRED | api_doc/__manifest__.py:9 | This module provides a dynamic documentation | FACT | always | — | Manifest: dynamic documentation generated from the database listing models, fields and methods, plus a playground to run methods over HTTP with examples in several languages. | N-U34-176 |
| VDR-U34-C348 | FUNCTION MAPPING REQUIRED | api_doc/__manifest__.py:10 | The documentation is generated using the | FACT | always | — | Manifest states the documentation is generated from the live database registry. | N-U34-178 |
| VDR-U34-C349 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:40 | if not self.env.user.has_group('api_doc.group_allow_doc'): | FACT | always | — | Each route (page, index, model) tests membership of api_doc.group_allow_doc (lines 40, 78, 190). | N-U34-179 |
| VDR-U34-C350 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:42 | "This page is only accessible to | FACT | refusal | — | Refusal raises AccessError whose text names the group (read with elevated rights). | N-U34-187 |
| VDR-U34-C351 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:85 | modules, models = self._doc_index() | INFERENCE | always | — | The response lists module names, model names, field names and public method names for everything the caller can read; no per-model reduction beyond read access. | N-U34-188 |
| VDR-U34-C352 | FUNCTION MAPPING REQUIRED | api_doc/controllers/api_doc.py:111 | # Server cache, use an attachment | FACT | always | — | Comment: index can exceed 1 MiB with many modules, which is why it is cached as an attachment (per language and group set). | N-U34-189 |
| VDR-U34-C353 | FUNCTION MAPPING REQUIRED | api_doc/__manifest__.py:53 | 'api_doc/static/src/**/*.js', | UNKNOWN | client | RT | UNKNOWN - EVIDENCE INSUFFICIENT: the single-page client scripts and the method playground were not read. | N-U34-190 |
| VDR-U34-C354 | FUNCTION MAPPING REQUIRED | attachment_indexation/__manifest__.py:15 | 'depends': ['web'], | FACT | always | — | Module depends on web only and, unlike its neighbours, has no auto_install flag; version 2.1 (restored DB shows installed 19.0.2.1). | N-U34-198 |
| VDR-U34-C355 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:20 | FTYPES = ['docx', 'pptx', 'xlsx', 'opendoc', | FACT | always | — | Extractor order docx, pptx, xlsx, opendoc, pdf (re-verified, U21-C509). | N-U34-193 |
| VDR-U34-C356 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:261 | for ftype in FTYPES: | FACT | always | — | The first extractor returning non-empty text wins; NUL characters are removed; if none, the base _index is used. | N-U34-193 |
| VDR-U34-C357 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:267 | res = res or super(IrAttachment, self)._index(bin_data, | FACT | always | — | Fallback to the base index (strings extraction for text/* MIME types only, base/models/ir_attachment.py:434-441). | N-U34-193 |
| VDR-U34-C358 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:23 | index_content_cache = LRU(1) | FACT | always | — | The cache holds one entry, keyed by checksum; a cached empty value is not used (truthiness test, line 258). | N-U34-196 |
| VDR-U34-C359 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:274 | index_content_cache[attachment.checksum] = attachment.index_content | FACT | copy | — | Copy of an attachment primes the cache with its existing index to avoid recomputation. | N-U34-196 |
| VDR-U34-C360 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:77 | content = xml.dom.minidom.parseString(zf.read("word/document.xml")) | FACT | docx | — | Word text comes from paragraph, heading and list elements of the main document part; errors swallowed. | N-U34-200 |
| VDR-U34-C361 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:93 | zf_filelist = [x for x in | FACT | pptx | — | Slides are read sequentially by index from slide1; text from a:t elements. | N-U34-193 |
| VDR-U34-C362 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:118 | workbook = load_workbook(f, data_only=True, read_only=True) | FACT | xlsx | — | Spreadsheet values (not formulas) are read through the optional openpyxl library; ImportError returns empty text; rows prefixed by the sheet name, empty rows skipped. | N-U34-194 |
| VDR-U34-C363 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:144 | MAX_COLUMN_REPEAT = 100 | FACT | opendoc | — | Repeated cells and rows are capped at 100 and 50. | N-U34-194 |
| VDR-U34-C364 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:203 | content = etree.fromstring(zf.read('content.xml')) | INFERENCE | opendoc | RT | The content part is parsed with the default lxml parser and no size limit (compare resolve_entities=False used in the shared import layer); security impact not tested. | N-U34-201 |
| VDR-U34-C365 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:217 | if not bin_data.startswith(b'%PDF-'): | FACT | pdf | — | PDF extraction requires the signature and the optional pdfminer library; boxes_flow None to reduce memory; failures return empty. | N-U34-195 |
| VDR-U34-C366 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:16 | if not (importlib.util.find_spec('pdfminer') | FACT | module load | — | A warning is logged at load when the PDF library is not available. | N-U34-198 |
| VDR-U34-C367 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:40 | buf = buf.translate({ | FACT | pdf/xlsx/opendoc | — | Cleaning removes NUL and carriage returns, replaces tabs by spaces and compacts whitespace keeping at most one blank line. | N-U34-195 |
| VDR-U34-C368 | FUNCTION MAPPING REQUIRED | attachment_indexation/tests/test_indexation.py:23 | text = self.env['ir.attachment']._index(pdf, 'application/pdf') | FACT | tests | — | One test exists: the PDF test, skipped without the library; no tests for the other formats. | N-U34-203 |
| VDR-U34-C369 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:478 | index_content = fields.Text('Indexed Content', readonly=True, prefetch=False) | FACT | DISCOVERED base | — | The index is stored in a read-only text field labelled Indexed Content and not prefetched; computed when data is set (base:314-323, 779). | N-U34-192 |
| VDR-U34-C370 | FUNCTION MAPPING REQUIRED | attachment_indexation/__manifest__.py:11 | * Document Indexation: odt, pdf, xlsx, | FACT | always | — | Manifest: attachments list on top of forms and indexation of odt, pdf, xlsx, docx (pptx also supported in code). | N-U34-191 |
| VDR-U34-C371 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:317 | index_content = self._index(data, mimetype, checksum=checksum) | FACT | DISCOVERED base | — | Base computes the index whenever data-related values are computed, passing checksum when available. | N-U34-197 |
| VDR-U34-C372 | FUNCTION MAPPING REQUIRED | attachment_indexation/__manifest__.py:15 | 'depends': ['web'], | OBSERVATION | restored DB | — | DB: one installed module depends on it (hr_recruitment). | N-U34-199 |
| VDR-U34-C373 | FUNCTION MAPPING REQUIRED | attachment_indexation/models/ir_attachment.py:262 | buf = getattr(self, '_index_%s' % ftype)(bin_data) | INFERENCE | always | — | Every extractor is tried in turn on every file regardless of mimetype; each extractor checks its own container format. | N-U34-202 |
