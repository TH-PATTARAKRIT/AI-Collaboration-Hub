# Source Map (candidate) — `account_edi_ubl_cii`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_edi_ubl_cii` |
| Display name | Import/Export electronic invoices with UBL/CII |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `48ffd430faaa6153` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_edi_ubl_cii/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (2): `purchase_edi_ubl_bis3`, `sale_edi_ubl`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (43): `account_peppol`, `account_peppol_advanced_fields`, `l10n_account_edi_ubl_cii_tests`, `l10n_anz_ubl_pint`, `l10n_at`, `l10n_be`, `l10n_ch`, `l10n_cy`, `l10n_cz`, `l10n_de`, `l10n_dk`, `l10n_dk_nemhandel` … (+31)
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / —
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 1, reports 1, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (15): `account.edi.xml.cii` (Factur-x/ZUGFeRD CII 2.2.0); `account.edi.xml.ubl_sg` (SG BIS Billing 3.0); `account.edi.xml.ubl_de` (BIS3 DE (XRechnung)); `account.edi.xml.ubl_20` (UBL 2.0); `account.edi.ubl_pint_eu` (UBL PINT-EU Layer); `account.edi.xml.ubl_21` (UBL 2.1); `account.edi.xml.ubl_bis3` (UBL BIS Billing 3.0.12); `account.edi.ubl_cen_en16931` (UBL CEN-EN16931); `account.edi.common` (Common functions for EDI documents: generate the data, the constraints, etc); `account.edi.ubl_pint` (UBL PINT); `account.edi.xml.ubl_nl` (SI-UBL 2.0 (NLCIUS)); `account.edi.xml.ubl_a_nz` (A-NZ BIS Billing 3.0); `account.edi.ubl` (Base helpers for UBL); `account.edi.xml.ubl_efff` (E-FFF (BE)); `account.edi.cii` (Base helpers for CII)
- Objects extended from other modules (6): `account.move.send.wizard`, `account.tax`, `account.move`, `ir.actions.report`, `account.move.send`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `account.edi.xml.cii` ← Community: `l10n_fr_pdp`; open-license custom/third-party scanned: —
- `account.edi.xml.ubl_20` ← Community: `l10n_dk_oioubl`; open-license custom/third-party scanned: —
- `account.edi.xml.ubl_21` ← Community: `l10n_dk_nemhandel`, `l10n_jo_edi`, `l10n_my_edi`, `l10n_rs_edi`, `l10n_sa_edi`, `l10n_tr_nilvera_einvoice`, `pos_edi_ubl`; open-license custom/third-party scanned: —
- `account.edi.xml.ubl_bis3` ← Community: `account_peppol`, `l10n_anz_ubl_pint`, `l10n_fr_facturx_chorus_pro`, `l10n_fr_pdp`, `l10n_hr_edi`, `l10n_jp_ubl_pint`, `l10n_my_ubl_pint`, `l10n_ro_edi`, `l10n_sg_ubl_pint`, `purchase_edi_ubl_bis3` … (+1); open-license custom/third-party scanned: —
- `account.edi.common` ← Community: `account_peppol`, `l10n_fr_pdp`; open-license custom/third-party scanned: —
- `account.edi.ubl` ← Community: `account_peppol`, `l10n_fr_pdp`; open-license custom/third-party scanned: —
- `account.edi.cii` ← Community: `l10n_fr_pdp`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `account.move.send.wizard`, `account.tax`, `account.move`, `ir.actions.report`, `account.move.send`, `res.partner`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 89 of 91 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: account_edi_ubl_cii (Import/Export electronic invoices with UBL/CII)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/account_edi_ubl_cii.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Module has no security folder (no ACL rows, record rules, groups or crons of its own).

## A. Capabilities / functions
- Generates and reads structured e-invoice XML for customer invoices/credit notes and for supplier-side imports; manifest lists formats E-FFF, UBL Bis 3, EHF3, NLCIUS, Factur-X (CII), XRechnung (UBL) and says PDF is embedded in UBL XML (account_edi_ubl_cii/__manifest__.py:5-22).
- Conditional/automatic: depends only on account and is `auto_install` (account_edi_ubl_cii/__manifest__.py:24,39). Not a standalone app. Other Community modules pull it in (see F).
- Formats offered on the customer record: France (Factur-X), EU Peppol Bis 3.0, Germany (ZUGFeRD), Germany (XRechnung), Netherlands (NLCIUS), Australia/New Zealand (A-NZ), Singapore (SG) (account_edi_ubl_cii/models/res_partner.py:30-40). Country eligibility and priority table: account_edi_ubl_cii/models/res_partner.py:167-182 (Bis3 for the default Peppol countries with priority 200; XRechnung DE; NLCIUS NL; A-NZ NZ/AU and SG not on the Odoo Peppol network; Factur-X FR; ZUGFeRD DE). Default Peppol country list is owned by account (account/models/company.py:34-38). Note: manifest text says formats are chosen on the journal (account_edi_ubl_cii/__manifest__.py:14) but the code stores the choice on the partner, company-dependent (account/models/partner.py:585-592, 659-666); treat manifest sentence as possibly stale.
- E-FFF builder exists (account.edi.xml.ubl_efff, filename only variant of UBL 2.0) (account_edi_ubl_cii/models/account_edi_xml_ubl_efff.py:9-17); no partner-selectable "E-FFF" option in the format list above: UNKNOWN — EVIDENCE INSUFFICIENT regarding its current use.
- Core export: builder is chosen from the customer format (account_edi_ubl_cii/models/res_partner.py:331-345); export validates tax structure, builds the document, runs format rules and returns the XML plus a set of error messages (account_edi_ubl_cii/models/account_edi_ubl.py:2719-2740; older UBL 2.0 path account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:39-56). Factur-X export can be switched to a legacy template path by a system parameter (default: new path) (account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:261-271).
- Core import: recognises file type (UBL 2.0/2.1-2.3, Bis3, XRechnung, NLCIUS, A-NZ, SG, CII, and UBL "AttachedDocument" wrappers) and registers a decoder with priority 20 (account_edi_ubl_cii/models/account_move.py:251-279, 281-361, 344-361).
- Send-time: at sending, XML is generated and attached to the invoice (field "UBL/CII File"); if a UBL format is used the invoice PDF and accepted extra attachments are embedded in the XML; a Factur-X XML is always silently embedded into the PDF (with PDF/A conversion for FR/DE) (account_edi_ubl_cii/models/account_move_send.py:124-222, 228-299).
- Manual download of "Export XML" from the print menu and download-by-URL, including on-the-fly generation when no stored file exists (fallback) (account_edi_ubl_cii/models/account_move.py:47-52, 64-112); (TEST) fallback gives German -> ZUGFeRD, Belgian -> Bis3, US -> nothing, and returns error text when a line lacks a tax (account_edi_ubl_cii/tests/test_ubl_cii.py:300).
- Optional utility: "(Un)Group lines by tax" server action for draft imported invoices, restricted to invoicing group (account_edi_ubl_cii/views/account_move_views.xml:4-14; account_edi_ubl_cii/models/account_move.py:113-247).
- Tax master data: per-tax e-invoicing category code and exemption reason code (account_edi_ubl_cii/models/account_tax.py:7-125; account_edi_ubl_cii/views/account_tax_views.xml).
- Partner Peppol address (EAS scheme + endpoint) fields with automatic proposal by country (account_edi_ubl_cii/models/res_partner.py:43-153, 266-304).
- Optional "Generated by Odoo" substitute PDF for imported vendor XML without a PDF (account_edi_ubl_cii/models/account_edi_common.py:1828-1876; report in account_edi_ubl_cii/report/account_edi_ubl_cii_report_templates.xml).
- Custom PDF templates listed in a system parameter also receive an embedded Factur-X for a single posted sales invoice (account_edi_ubl_cii/models/ir_actions_report.py:9-30).

## B. Business objects, relationships, lifecycle
- Invoice (account.move) gains an attached XML (stored as attachment) and a derived filename (account_edi_ubl_cii/models/account_move.py:17-41); the XML is detached (kept as a document) with the move via the detach list (account_edi_ubl_cii/models/account_move.py:58-62).
- Customer/vendor partner: eInvoice format (base field in account), Peppol EAS and endpoint (account_edi_ubl_cii/models/res_partner.py:30-51).
- Builders are abstract models (no tables): common helpers -> UBL base / CII base -> UBL 2.0 -> 2.1 -> Bis3 (also PINT-EU layer) -> XRechnung, NLCIUS, A-NZ, SG; CII builder = Factur-X/ZUGFeRD (account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:12-14; account_edi_ubl_cii/models/account_edi_xml_ubl_xrechnung.py:6-8; account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:28-31).
- Export eligibility gate for an invoice: no stored XML yet, is a sales document (or a self-billed purchase document on a self-billing journal whose builder supports self-billing), and the chosen format is one of the UBL/CII formats (account_edi_ubl_cii/models/account_move.py:363-377). Only posted moves are offered in the print menu (account_edi_ubl_cii/models/account_move.py:92-111). Format used = partner's setting, else a country suggestion (account_edi_ubl_cii/models/res_partner.py:195-222); (TEST) suggestion picks lowest priority number when several match (account_edi_ubl_cii/tests/test_partner_peppol_fields.py:83).
- Document type mapping in export: customer invoice = invoice, customer refund = credit note, vendor invoice/refund = self-invoice/self-credit-note (account_edi_ubl_cii/models/account_edi_ubl.py:2597-2609). Factur-X type code 380 vs 381 (account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:121-128).
- Import lifecycle: applies only to an invoice with no lines; determines invoice vs credit note from the file and converts the move type when the journal type allows (customer/supplier), logs conversion (account_edi_ubl_cii/models/account_edi_common.py:564-597, 1188-1207); draft state is where grouping/ungrouping is allowed (account_edi_ubl_cii/models/account_move.py:201-207). Result is a draft record plus chatter log listing format and warnings (account_edi_ubl_cii/models/account_edi_common.py:1801-1826). Stored XML is linked as "UBL/CII File" for purchase documents (account_edi_ubl_cii/models/account_edi_common.py:1802-1809).
- Import matching order for the counterparty: VAT, Peppol address, email, phone, name; if not found and name+VAT present, a new company partner is created (with Peppol data for CII) and logged; a VAT conflict creates a new partner rather than overwriting (account_edi_ubl_cii/models/account_edi_common.py:1232-1300; account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:483-494). Bank accounts from the file are found or created on the counterparty (account_edi_ubl_cii/models/account_edi_common.py:1332-1360); (TEST) importing must not attach the current company's own bank account (account_edi_ubl_cii/tests/test_ubl_cii.py:433).
- Imported line values are aggregated to tax totals; rounding corrections apply when the file's tax amount differs by small tolerance (account_edi_ubl_cii/models/account_edi_common.py:599-603, 1721).
- Automatic re-grouping on import: if the last posted document from the same partner had grouped lines, the new one is grouped too (account_edi_ubl_cii/models/account_move.py:221-246).

## C. Validations, automation, security, multi-company
- Export rule sets return messages instead of blocking hard; caller decides (send wizard marks "error but continue") (account_edi_ubl_cii/models/account_move_send.py:138-143). Groups of rules:
  - Common: each non-note line must carry at least one tax (account_edi_ubl_cii/models/account_edi_common.py:546-551).
  - UBL 2.0: supplier name, customer name, invoice number, invoice date required (account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:1100-1108).
  - CEN EN16931 layer: delivery address/date for intra-EU supply, bank account for payment identification, item name, exactly one tax per line, no mixing of "outside scope" tax, country and VAT prefix of parties (account_edi_ubl_cii/models/account_edi_ubl_cen_en16931.py:79-180).
  - Bis3: Norwegian supplier VAT format; Belgian company registry validity for supplier/customer (account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:291-340).
  - PINT-EU layer: buyer reference or order reference; Dutch supplier address, identifier and payment means rules (account_edi_ubl_cii/models/account_edi_ubl_pint_eu.py:86-149). PINT base rules for parties/lines (account_edi_ubl_cii/models/account_edi_ubl_pint.py:424-540).
  - XRechnung: supplier telephone and email required (account_edi_ubl_cii/models/account_edi_xml_ubl_xrechnung.py:17-26).
  - Factur-X: payment instructions (bank account + sanitized number) on customer invoices, seller country, seller VAT, seller phone and email, tax on each line, intra-community VAT numbers, Canary tax rate (account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:48-95).
- Tax structure validated before export; invalid repartition raises a blocking error (account_edi_ubl_cii/models/account_edi_common.py:396-403).
- Peppol endpoint validation on partner save (format per scheme, 1-50 chars) and sanitising/auto-fill from VAT or company registry when scheme changes (account_edi_ubl_cii/models/res_partner.py:154-160, 246-330).
- Sending alerts (informational): missing Peppol address on company or partner; suggestion to install the French Chorus Pro module when the customer is behind Chorus Pro (account_edi_ubl_cii/models/account_move_send.py:34-73). Purchase-side self-billing lifts the "sales documents only" restriction (account_edi_ubl_cii/models/account_move_send.py:23-28).
- Attachment embedding accepts only supported file types; others are flagged unsupported in the send wizard (account_edi_ubl_cii/models/account_move_send.py:106-118; account_edi_ubl_cii/wizard/account_move_send_wizard.py:7-21).
- Security: no module-specific groups/rules. Grouping action limited to `account.group_account_invoice` (account_edi_ubl_cii/views/account_move_views.xml:7). Attachments created at send time are written with elevated rights (account_edi_ubl_cii/models/account_move_send.py:311). Module-level access otherwise follows account.
- Multi-company: partner format is company-dependent (account/models/partner.py:592, 659); export reads format with the invoice's company (account_edi_ubl_cii/models/account_move.py:77-79); import searches previous documents with the company filter (account_edi_ubl_cii/models/account_move.py:237-243). Company's own Peppol identity comes from the company partner (account_edi_ubl_cii/models/account_move_send.py:38-49).
- Uninstall clears stored format choices for facturx, nlcius, ubl_a_nz, ubl_bis3, ubl_sg, xrechnung (account_edi_ubl_cii/__init__.py:5-13).

## D. Handoffs to other modules
- account (owner): invoice model, sending framework (send wizard, hooks before/after PDF render, alerts, constraints), document-import framework (file-type detection, decoders, attachment unwrapping), journal self-billing flag, partner format field and default (account/models/account_move_send.py:44-46, 398-464; account/models/account_document_import_mixin.py:370-507; account/models/account_journal.py:120).
- account_peppol (network transport): extends the same builders and send flow to transmit over Peppol; auto-installs with this module for companies in eligible countries (account_peppol/__manifest__.py:57 comment). Detail outside this note: UNKNOWN — EVIDENCE INSUFFICIENT.
- sale_edi_ubl / purchase_edi_ubl_bis3: order-level UBL bridges auto-installed with sale/purchase plus this module (sale_edi_ubl/__manifest__.py:13-15; purchase_edi_ubl_bis3/__manifest__.py:10-12).
- Accounting outcomes: import produces a draft bill/credit note that goes through normal posting; tax and account matching are done against existing master data (account_edi_ubl_cii/models/account_edi_common.py:1426-1526). No journal entries are created by this module itself.
- Audit: chatter entries on import ("format used", warnings, converted-to-credit-note, grouped/ungrouped) (account_edi_ubl_cii/models/account_edi_common.py:1820-1826; account_edi_ubl_cii/models/account_move.py:144,159).
- Product/UoM/tax data: uses UoM external ids to map units (account_edi_ubl_cii/models/account_edi_common.py:338-345); optional account prediction hook for special taxes if another module provides it (account_edi_ubl_cii/models/account_move.py:394-403).
- Inventory and approval: none in this module.

## E. Configuration / defaults that change outcomes
- Partner: eInvoice format (empty = use country suggestion; "none" disables in account base logic), Peppol EAS/endpoint (account/models/partner.py:663-666; account_edi_ubl_cii/models/res_partner.py:211-213).
- Journal: self-billing flag enables vendor-side export (account_edi_ubl_cii/models/account_move.py:370-377).
- Tax: category and exemption reason; codes AE/E/G/O/K require a reason (account_edi_ubl_cii/models/account_tax.py:120-131). When a tax has no category, a default is predicted (account_edi_ubl_cii/models/account_edi_common.py:405-420).
- System parameters: `account_edi_ubl_cii.disable_pdf_in_xml` (default False, seeded, noupdate; blocks substitute PDF creation) (account_edi_ubl_cii/data/ir_config_parameter_data.xml:4-7; account_edi_ubl_cii/models/account_edi_common.py:1831); `account_edi_ubl_cii.use_new_dict_to_xml_helpers` (default true; not seeded) (account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:262-266); `account.custom_templates_facturx_list` (account_edi_ubl_cii/models/ir_actions_report.py:14).
- Belgian co-contractant note derives from the fiscal position note (account_edi_ubl_cii/models/account_edi_common.py:361-374).
- Company details: VAT / Peppol address of the company are prerequisites flagged in alerts.

## F. Effective extension path (module names only; grep across addons root)
- Manifests depending on account_edi_ubl_cii: account_peppol, account_peppol_advanced_fields, l10n_account_edi_ubl_cii_tests, l10n_anz_ubl_pint, l10n_at, l10n_be, l10n_ch, l10n_cy, l10n_cz, l10n_de, l10n_dk, l10n_dk_nemhandel, l10n_dk_oioubl, l10n_ee, l10n_es, l10n_fi, l10n_fr_account, l10n_fr_facturx_chorus_pro, l10n_gr, l10n_hr_edi, l10n_ie, l10n_it, l10n_jo_edi, l10n_jp_ubl_pint, l10n_lt, l10n_lu, l10n_lv, l10n_mt, l10n_my_ubl_pint, l10n_nl, l10n_no, l10n_pl, l10n_pt, l10n_ro, l10n_ro_edi, l10n_rs_edi, l10n_sa_edi, l10n_se, l10n_sg_ubl_pint, l10n_si, l10n_tr_nilvera, l10n_tr_nilvera_einvoice, pos_edi_ubl, purchase_edi_ubl_bis3, sale_edi_ubl.
- Builders extended or subclassed (`account.edi.common/ubl/xml.*`): account_peppol, l10n_fr_pdp, l10n_fr_facturx_chorus_pro, l10n_dk_oioubl, l10n_dk_nemhandel, l10n_jp_ubl_pint, l10n_sg_ubl_pint, l10n_my_ubl_pint, l10n_my_edi, l10n_my_edi_pos, l10n_rs_edi, l10n_sa_edi, l10n_sa_edi_pos, l10n_ro_cpv_code, purchase_edi_ubl_bis3, pos_edi_ubl.
- Sending flow (`account.move.send`) extended by: account_edi, account_peppol, l10n_ch, l10n_dk_nemhandel, l10n_es_edi_facturae, l10n_es_edi_sii, l10n_es_edi_tbai, l10n_es_edi_verifactu, l10n_fr_pdp, l10n_gr_edi, l10n_gr_edi_e_invoo, l10n_hr_edi, l10n_hu_edi, l10n_in_edi, l10n_it_edi, l10n_jo_edi, l10n_ke_edi_tremol, l10n_my_edi, l10n_pl_edi, l10n_ro_edi, l10n_rs_edi, l10n_sa_edi, l10n_tr_nilvera_einvoice(+_extended), l10n_tw_edi_ecpay, l10n_vn_edi_viettel, snailmail_account.
- Modules referencing the stored XML field/tax category code: account_peppol, l10n_account_edi_ubl_cii_tests, l10n_dk_nemhandel, l10n_dk_oioubl, l10n_fr_pdp, l10n_hr_edi, l10n_ro_edi, l10n_sg_ubl_pint, l10n_tr_nilvera_einvoice.
- Modules using `invoice_edi_format` on partners: account_peppol, l10n_anz_ubl_pint, l10n_dk_nemhandel, l10n_dk_oioubl, l10n_es_edi_facturae, l10n_es_edi_tbai, l10n_fr_pdp, l10n_hr_edi, l10n_it_edi, l10n_jo_edi, l10n_jp_ubl_pint, l10n_my_ubl_pint, l10n_pl_edi, l10n_ro_edi, l10n_sg_ubl_pint, l10n_tr_nilvera, l10n_tr_nilvera_einvoice, l10n_tw_edi_ecpay, l10n_vn_edi_viettel.

## G. Not verified
- Correctness of each country's rule set against the official standards; only that the rule keys exist as cited.
- E-FFF selectability in current UI; PINT country modules' behaviour; Peppol transmission; sale/purchase order UBL flows: UNKNOWN — EVIDENCE INSUFFICIENT.
- Company-dependent behaviour of the format when a partner is shared across companies beyond the cited compute: UNKNOWN — EVIDENCE INSUFFICIENT.
- Failure handling when the PDF/A conversion fails (logged and skipped, account_edi_ubl_cii/models/account_move_send.py:200-203): outcome for regulatory acceptance UNKNOWN — EVIDENCE INSUFFICIENT.
- No rule above is asserted as universal; behaviour depends on installed localizations, partner data and system parameters.

