# U48 — account EDI UBL/CII format architecture (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

- Unit: U48
- Modules: account_add_gln, account_edi_ubl_cii
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: DELTA-FIRST — deep field-level mapping study; U13/U24 breadth was only boundary profiling. Source evidence only; RT flags for runtime unknowns.

---

## CAP-U48-01 GLN (Global Location Number) on Partner

### D1 — Module identity and auto-install

`account_add_gln` is a standalone module that depends only on `account` and is set `auto_install: True`, meaning it installs automatically when `account` is present. Its manifest describes its purpose as providing the GLN field to be used on delivery addresses and notes the field is mandatory on UBL/CII e-invoices.

### D2 — GLN field definition

A single `Char` field named `global_location_number` with the string label "GLN" and the help text "Global Location Number" is added to `res.partner` via `_inherit`. No length constraint, validation, or unique constraint is present in the model definition.

### D3 — GLN UI placement

The field is placed in two positions in the partner form view, both guarded by `invisible="type != 'delivery'"`:
1. Inside `page[@name='sales_purchases'] // group[@name='misc']`
2. Inside the inline form of the `child_ids` widget on the `contact_addresses` tab, after `company_id`

This means the GLN field is only visible/editable when the partner type is "delivery", reflecting its logistical routing purpose.

### D4 — GLN integration with UBL/CII

The manifest of `account_add_gln` explicitly states the GLN is used on delivery addresses and is mandatory on UBL/CII e-invoices. However, the `account_add_gln` module itself does not contain any XML generation logic. The field is consumed by `account_edi_ubl_cii`. The delivery address lookup in `account_edi_xml_ubl_20.py` reads `partner_shipping_id` or falls back to `partner_id` for the delivery party — the GLN on that delivery partner flows into the XML at that point. RT: Exact XML element name mapped to GLN at runtime would need tracing through `account_edi_ubl_cii` delivery node generation.

---

## CAP-U48-02 UBL/CII Module Architecture and Inheritance Chain

### D1 — Module manifest and supported formats

`account_edi_ubl_cii` supports: E-FFF (Belgium), UBL BIS 3 (Peppol), EHF3 (Norway, same as BIS 3), NLCIUS (Netherlands), Factur-X (CII, France), XRechnung UBL (Germany). Auto-install is `True`. The module has no `account_edi` dependency — it directly extends `account`.

### D2 — Class inheritance chain

The inheritance chain is:
- `account.edi.common` (abstract) — base helpers: tax category, exemption reason, UoM, partner import, line import, currency import
- `account.edi.ubl` (abstract) inherits `account.edi.common` — base UBL tax grouping helpers, recycling contribution dispatch, base line UBL value computation
- `account.edi.xml.ubl_20` (abstract) inherits `account.edi.ubl` — UBL 2.0 format; main `_export_invoice`, node-builder architecture
- `account.edi.xml.ubl_21` (abstract) inherits `account.edi.xml.ubl_20` — UBL 2.1 incremental extension
- `account.edi.xml.ubl_bis3` (abstract) inherits `account.edi.xml.ubl_21` + `account.edi.ubl_pint_eu` — Peppol BIS Billing 3.0
- `account.edi.ubl_pint` (abstract) inherits `account.edi.ubl` — PINT-specific node overrides (withholding, invoice type codes 380/381/389/261)
- `account.edi.ubl_pint_eu` (abstract) inherits `account.edi.ubl_pint` — EU PINT layer
- `account.edi.cii` (abstract) — base CII helpers
- `account.edi.xml.cii` (abstract) inherits `account.edi.cii` — Factur-X/ZUGFeRD CII 2.2.0; both old qweb template path and new `dict_to_xml` path

### D3 — Format dispatch via res.partner

`res.partner._get_edi_builder()` maps `invoice_edi_format` strings to builder models:
- `'xrechnung'` → `account.edi.xml.ubl_de`
- `'facturx'` / `'zugferd'` → `account.edi.xml.cii`
- `'ubl_a_nz'` → `account.edi.xml.ubl_a_nz`
- `'nlcius'` → `account.edi.xml.ubl_nl`
- `'ubl_bis3'` → `account.edi.xml.ubl_bis3`
- `'ubl_sg'` → `account.edi.xml.ubl_sg`

### D4 — Country-to-format mapping

`_get_ubl_cii_formats_info()` returns a dictionary mapping format keys to country lists and Peppol flags. Thailand (TH) is NOT present in any country list in the Community source. UBL BIS 3 is available for countries in `PEPPOL_DEFAULT_COUNTRIES` (defined in `account` module, not in scope here). Thailand is not a BIS 3 country in Community.

### D5 — Format selection logic

`res.partner._get_ubl_cii_edi_format()` first returns `invoice_edi_format` if set, else calls `_get_suggested_ubl_cii_edi_format()`. That method looks up the partner's country code in `_get_ubl_cii_formats_by_country()`. For DE, if `peppol_eas == '0204'` (Leitweg-ID), `xrechnung` is selected.

---

## CAP-U48-03 UBL 2.0/2.1 Export — Document Structure and Node Building

### D1 — Export entry point

`account.edi.xml.ubl_20._export_invoice()` is the public export method. It:
1. Validates tax structure
2. Instantiates the XML builder via `vals = {'invoice': invoice.with_context(lang=invoice.partner_id.lang)}`
3. Calls `_get_invoice_node(vals)` to build the node tree
4. Calls `_export_invoice_constraints()` for validation errors
5. Uses `dict_to_xml(document_node, nsmap=nsmap, template=template)` to serialize

### D2 — Node-builder orchestration

`_get_invoice_node()` calls in order:
1. `_add_invoice_config_vals(vals)` — sets document_type, supplier, customer, partner_shipping, currency, company
2. `_add_invoice_base_lines_vals(vals)` — populates base_lines from invoice
3. `_add_invoice_currency_vals(vals)`
4. `_add_invoice_tax_grouping_function_vals(vals)`
5. `_setup_base_lines(vals)`
6. `_add_invoice_monetary_totals_vals(vals)`
7. `_add_invoice_header_nodes(document_node, vals)` — ID, IssueDate, InvoiceTypeCode, DocumentCurrencyCode, etc.
8. `_add_invoice_accounting_supplier_party_nodes(document_node, vals)`
9. `_add_invoice_accounting_customer_party_nodes(document_node, vals)`
10. `_add_invoice_seller_supplier_party_nodes(document_node, vals)`
11. `_add_invoice_delivery_nodes(document_node, vals)` — invoice only
12. `_add_invoice_payment_means_nodes(document_node, vals)`
13. `_add_invoice_payment_terms_nodes(document_node, vals)`
14. `_add_invoice_line_nodes(document_node, vals)`
15. `_add_invoice_allowance_charge_nodes(document_node, vals)`
16. `_add_invoice_exchange_rate_nodes(document_node, vals)`
17. `_add_invoice_tax_total_nodes(document_node, vals)`
18. `_add_invoice_monetary_total_nodes(document_node, vals)`
19. `_add_invoice_optional_nodes(document_node, vals)`

### D3 — Document type determination

`_add_invoice_config_vals()` sets `document_type` to:
- `'debit_note'` if `debit_origin_id` field exists on account.move AND invoice has debit_origin_id
- `'credit_note'` if `move_type in ('out_refund', 'in_refund')`
- `'invoice'` otherwise

Supplier/customer are swapped for purchase documents (is_purchase_document()).

### D4 — Namespace map for UBL 2.0

The namespace map includes:
- None (default): `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2` (for invoice), CreditNote-2, DebitNote-2, or Order-2
- `cac`: `urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2`
- `cbc`: `urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2`
- `ext`: `urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2`

### D5 — Document type code tags per document_type

`_get_tags_for_document_type()` maps document_type to XML tag names:
- `document_type_code`: `cbc:InvoiceTypeCode` / `cbc:CreditNoteTypeCode` / None (debit_note) / `cbc:OrderTypeCode`
- `monetary_total`: `cac:LegalMonetaryTotal` (invoice, credit_note) / `cac:RequestedMonetaryTotal` (debit_note) / `cac:AnticipatedMonetaryTotal` (order)
- `document_line`: `cac:InvoiceLine` / `cac:CreditNoteLine` / `cac:DebitNoteLine` / `cac:OrderLine`
- `line_quantity`: `cbc:InvoicedQuantity` / `cbc:CreditedQuantity` / `cbc:DebitedQuantity` / `cbc:Quantity`

---

## CAP-U48-04 UBL Field-Level Mappings — Header Level

### D1 — invoice.name maps to cbc:ID

The invoice number (`invoice.name`) is used as the UBL `cbc:ID` (invoice identifier, BT-1 in EN 16931). RT: Confirmed indirectly from standard pattern; the header node builder sets this.

### D2 — invoice.invoice_date maps to cbc:IssueDate

The invoice date (`invoice.invoice_date`) maps to `cbc:IssueDate` (BT-2). CII equivalent: `ExchangedDocument/IssueDateTime/DateTimeString` formatted with `DEFAULT_FACTURX_DATE_FORMAT = '%Y%m%d'`.

### D3 — invoice.currency_id maps to cbc:DocumentCurrencyCode

The invoice currency (`invoice.currency_id.name`) maps to `cbc:DocumentCurrencyCode` (BT-5, ISO 4217 alpha-3). In PINT layer: `_ubl_add_document_currency_code_node()` explicitly sets `vals['document_node']['cbc:DocumentCurrencyCode']['_text'] = vals['currency'].name`.

### D4 — company.currency_id as tax currency

In PINT layer, `_ubl_add_tax_currency_code_node()` sets `cbc:TaxCurrencyCode` (BT-6) to the company currency. The PINT comment states this is used for tax accounting and reporting; it must differ from invoice currency if provided.

### D5 — narration maps to cbc:Note

In PINT layer `_ubl_add_notes_nodes_all_invoices()`, `invoice.narration` (converted from HTML to plain text via `html2plaintext`) is included in the `cbc:Note` element together with withholding tax explanation. In CII format: `ExchangedDocument/IncludedNote/Content`.

### D6 — invoice_date_due maps to payment terms

`invoice.invoice_date_due` maps to the due date element. In CII import: `SpecifiedTradePaymentTerms/DueDateDateTime/DateTimeString`.

### D7 — ref maps to BuyerReference / purchase order reference

In CII export: `invoice.buyer_reference` (if field exists and set) else `commercial_partner_id.ref` is passed as `buyer_reference`. `invoice.purchase_order_reference` (if field exists) else `invoice.ref or invoice.name` is passed as `purchase_order_reference`. In CII import: `BuyerOrderReferencedDocument/IssuerAssignedID` → `invoice_origin`.

### D8 — company_registry / partner.company_registry as seller/buyer legal entity

In CII: `seller_specified_legal_organization = invoice.company_id.company_registry`. `buyer_specified_legal_organization = invoice.commercial_partner_id.company_registry`.

### D9 — delivery_date maps to scheduled delivery

In CII: `_get_scheduled_delivery_time()` returns `invoice.delivery_date` if set, else `invoice.invoice_date`. Maps to CII delivery date element.

### D10 — invoice type code 380/381/389/261

In PINT layer: `cbc:InvoiceTypeCode` is set to 380 for invoice, 389 for self_invoice. `cbc:CreditNoteTypeCode` is 381 for credit_note, 261 for self_credit_note. In CII: TypeCode 380/381 (plus 389, 527 interpreted as invoice, 261 as refund).

---

## CAP-U48-05 UBL Field-Level Mappings — Party Level

### D1 — peppol_eas and peppol_endpoint on res.partner

`res.partner` has two stored, computed fields: `peppol_eas` (Selection, ~60 values) and `peppol_endpoint` (Char). These map to the UBL `cac:PartyIdentification/cbc:ID@schemeID` element combination used for electronic addressing (Endpoint ID, BT-34/BT-49).

### D2 — EAS auto-compute logic

`_compute_peppol_eas()` inspects `EAS_MAPPING[country_code]` and sets the first non-deprecated EAS for which a valid field value exists on the partner. `_compute_peppol_endpoint()` then derives the endpoint value from the matched field (e.g., `vat`, `company_registry`, `l10n_no_bronnoysund_number`, etc.).

### D3 — EAS_MAPPING coverage — Thailand absent

`EAS_MAPPING` in `account_edi_common.py` covers AD, AE, AL, AT, AU, BA, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, SG, GB, GR, HR, HU, IE, IS, IT, JP, LI, LT, LU, LV, MC, ME, MK, MT, MY, NG, NL, NO, NZ, PL, PT, RO, RS, SE, SI, SK, SM, TR, VA, and several French DOM-TOM. Thailand (TH) is NOT listed.

### D4 — vat maps to seller/buyer VAT ID in XML

For most countries, the `vat` field on the partner (or company) maps to the UBL `cac:PartyTaxScheme/cbc:CompanyID` (BT-31 for seller, BT-48 for buyer). In CII: `ram:SpecifiedTaxRegistration/ram:ID`.

### D5 — partner.name maps to PartyName

`partner.name` maps to `cac:PartyName/cbc:Name` (BT-27 for seller trading name, BT-44 for buyer trading name). In CII import: `ram:SellerTradeParty/ram:Name` / `ram:BuyerTradeParty/ram:Name`.

### D6 — Address fields mapping

In CII import: `ram:{role}/ram:PostalTradeAddress`:
- `ram:LineOne` → `street`
- `ram:LineTwo` → `street2` (additional_street)
- `ram:CityName` → `city`
- `ram:PostcodeCode` → `zip`
- `ram:CountryID` → `country_code`

### D7 — Phone and email in CII

In CII import: `ram:{role}/ram:DefinedTradeContact/ram:TelephoneUniversalCommunication/ram:CompleteNumber` → `phone`. `ram:{role}//ram:EmailURIUniversalCommunication/ram:URIID` → `email`.

### D8 — Bank account: partner_bank_id maps to payment means

In CII export: `invoice.partner_bank_id.sanitized_acc_number` maps to the bank account element in `SpecifiedTradeSettlementPaymentMeans/PayeePartyCreditorFinancialAccount/IBANID`. CII import reads both `IBANID` and `ProprietaryID` from `SpecifiedTradeSettlementPaymentMeans`.

### D9 — Peppol endpoint format validation constraints

`_build_error_peppol_endpoint()` enforces:
- EAS `0208` (BE company registry): must match `^\d{10}$`
- EAS `0009` (FR SIRET): must pass `siret.is_valid()`
- EAS `0007` (SE org.nr.): must match `^\d{10}$`
- EAS `EM` (email): must pass `single_email_re`
- Default: no chars matching `[^a-zA-Z\d\-._~]`, length 1–50

### D10 — Chorus Pro detection

`_is_customer_behind_chorus_pro()` returns True when `customer.peppol_eas + ':' + customer.peppol_endpoint == "0009:11000201100044"`. This is used for Chorus Pro-specific behavior in BIS 3.

---

## CAP-U48-06 UBL Field-Level Mappings — Tax Level

### D1 — account.tax new fields for UBL/CII

`account.tax` gains three fields:
- `ubl_cii_tax_category_code`: Selection — 10 values: AE, E, S, Z, G, O, K, L, M, B
- `ubl_cii_tax_exemption_reason_code`: Selection — ~60+ VATEX-EU-* and VATEX-FR-* values
- `ubl_cii_requires_exemption_reason`: Boolean computed — True when category is AE, E, G, O, or K

### D2 — Tax category code determination logic

`_get_tax_category_code(customer, supplier, tax)` in `account.edi.common`:
1. Returns `tax.ubl_cii_tax_category_code` if set on the tax
2. Applies Spain Canary Islands (zip 35/38) → `'L'`, Ceuta/Melilla (51/52) → `'M'`
3. Same country supplier/customer: zero-amount tax → `'E'`; negative factor tax → `'AE'`; else `'S'`
4. EEA cross-border with VAT: zero or negative → `'K'` (intra-EU) or `'G'` (export); else `'S'`
5. Non-EEA: nonzero → `'S'`; zero → `'E'`

### D3 — GST scheme ID

`GST_COUNTRY_CODES` = AU, NZ, IN, SG, MY, PK, BD, LK, NP, BT, PG, SA, AG, BS, BB, DM, GD, JM, KN, LC, VC, TT. For suppliers in these countries, the tax scheme ID in XML is `'GST'` instead of `'VAT'`.

### D4 — Tax grouping keys

`_ubl_default_tax_category_grouping_key()` returns a dict with keys: `tax_category_code`, `tax_exemption_reason`, `tax_exemption_reason_code`, `percent` (tax.amount or None for 'O'), `scheme_id` ('GST' or 'VAT'), `is_withholding`, `currency`. Recycling contribution taxes and excise taxes return `None` (excluded from standard tax grouping).

### D5 — TaxTotal / TaxSubtotal grouping

Three nested grouping levels: `_ubl_default_tax_total_grouping_key()` (by `is_withholding` and `currency`), `_ubl_default_tax_subtotal_grouping_key()` (full tax_category dict), `_ubl_default_tax_subtotal_tax_category_grouping_key()` (same). For reverse-charge (negative factor) taxes, the XML reports percent = 0.0 with category AE.

### D6 — Fixed taxes as AllowanceCharges

`account_edi_ubl.py` comment: `fixed_taxes_as_allowance_charges: True` by default. Fixed taxes (amount_type == 'fixed') are dispatched into AllowanceCharge nodes on lines rather than TaxTotal. In CII, fixed taxes are added as AllowanceCharge with reason_code `'AEO'` and excluded from tax totals; `base_amount_currency` is increased correspondingly.

### D7 — Recycling contribution taxes

Taxes with `amount_type == 'fixed'` and `include_base_amount == True` are treated as recycling contributions (RECUPEL, AUVIBEL pattern in BE). They are extracted from base_lines and put in `allowance_charges_recycling_contribution` on the UBL values, not in TaxTotal.

### D8 — Excise taxes

Taxes with `amount_type == 'code'` and `include_base_amount == True` are treated as excise taxes and similarly extracted into `allowance_charges_excise`.

### D9 — Tax exemption reason mapping

`TAX_EXEMPTION_MAPPING` in `account_edi_common.py` maps ~60 VATEX codes to EN descriptive strings. `_get_tax_exemption_reason()` auto-selects VATEX-EU-G for 'G', VATEX-EU-IC for 'K', and "Exempt from tax" for 'E' as defaults when no explicit code is set.

### D10 — Belgian co-contractant note

`_get_belgian_cocontractant_note()` detects the Belgian co-contractant fiscal position (chart template ref `fiscal_position_template_4`) and adds the standard reverse-charge notice text. This note overrides the default VATEX-EU-AE code behavior.

---

## CAP-U48-07 UBL Field-Level Mappings — Line Level

### D1 — Line-level calculation basis

`_retrieve_line_vals()` in `account.edi.common` implements the line-level import formula documented inline:
```
line_net_subtotal = (gross_unit_price - rebate) * (delivered_qty / basis_qty) - allow_charge_amount
```
UBL xpaths: `net_price_unit` = `Price/PriceAmount` (BT-146), `gross_price_unit` = `Price/AllowanceCharge/BaseAmount` (BT-148), `basis_qty` = `Price/BaseQuantity` (BT-149), `delivered_qty` = `InvoicedQuantity` (BT-129), `line_total_amount` = `LineExtensionAmount` (BT-131).

### D2 — Odoo quantity/price_unit mapping

From UBL import, Odoo derives:
- `price_unit` = `gross_price_unit / basis_qty` (if gross given), else `(net_price_unit + rebate) / basis_qty`
- `quantity` = `delivered_qty`
- `discount` = `100 * (1 - price_subtotal / (delivered_qty * price_unit))`

### D3 — UoM to UNECE code mapping

`UOM_TO_UNECE_CODE` in `account_edi_common.py` maps 26 Odoo UoM XML IDs to UNECE Rec 20 codes. Default fallback is `'C62'` (unit/piece). On import, `unitCode` attribute on quantity node is reverse-mapped via dict inversion to find an Odoo UoM.

### D4 — Product identification in UBL import

`xpath_dict['product']` for UBL/CII maps:
- CII: `ram:SpecifiedTradeProduct/ram:SellerAssignedID` → `default_code`, `ram:SpecifiedTradeProduct/ram:Name` → `name`, `ram:SpecifiedTradeProduct/ram:GlobalID` → `barcode`
- These values are passed to `product.product._retrieve_product()` for matching

### D5 — Line description / name

CII: `_get_line_xpaths()` returns name xpaths as a list: first `ram:SpecifiedTradeProduct/ram:Description`, fallback `ram:SpecifiedTradeProduct/ram:Name`. Both are tried in order via `_find_value()`.

### D6 — AllowanceCharge on lines (charges)

Line-level AllowanceCharge nodes (CII: `SpecifiedLineTradeSettlement/SpecifiedTradeAllowanceCharge`) are read with indicator (true=charge/false=discount), amount, reason_code, reason. Charges are turned into new invoice lines via `_retrieve_line_charges()`. Special case: `reason_code == 'AEO'` → attempt to match a fixed tax record.

### D7 — Line rebate / item price discount

In CII import: `GrossPriceProductTradePrice/AppliedTradeAllowanceCharge/ActualAmount` (BT-147) is the item price discount (rebate). `gross_price_unit - rebate = net_price_unit`.

### D8 — Deferred/billing period on lines

In CII format `_get_invoice_line_xpaths()`: `deferred_start_date` = `SpecifiedLineTradeSettlement/BillingSpecifiedPeriod/StartDateTime/DateTimeString`, `deferred_end_date` = corresponding EndDateTime. These map to `line.deferred_start_date` / `line.deferred_end_date` if those fields exist on account.move.line.

### D9 — Line extension amount (BT-131)

In `_ubl_add_base_line_ubl_values_line_extension_amount()`, the line extension amount = `total_excluded + delta_total_excluded + recycling_contribution_amounts + excise_amounts`. This excludes discounts from the charge/allowance side.

### D10 — Negative unit price handling

`_ubl_turn_base_lines_price_unit_as_always_positive()`: when `price_unit < 0.0`, the quantity is inverted and price_unit made positive. In CII export: if `gross_price_total_unit < 0`, quantity is negated and price unit negated. Implements BIS 3 business rules BR-27 and BR-28.

---

## CAP-U48-08 CII (Factur-X / ZUGFeRD) Format Architecture

### D1 — CII namespace map

`CII_NAMESPACES` in `account_edi_xml_cii_facturx.py`:
- `ram`: `urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100`
- `rsm`: `urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100`
- `udt`: `urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100`

New export also adds `qdt` and `xsi` namespaces.

### D2 — Document context ID for Factur-X

`document_context_id = "urn:cen.eu:en16931:2017#conformant#urn:factur-x.eu:1p0:extended"`. This is the Factur-X Extended profile identifier placed in `rsm:CrossIndustryInvoice/rsm:ExchangedDocumentContext/ram:GuidelineSpecifiedDocumentContextParameter/ram:ID`.

### D3 — Dual export path in CII

`_export_invoice()` in CII checks `ir.config_parameter` `account_edi_ubl_cii.use_new_dict_to_xml_helpers` (default True). If True: new `_export_invoice_new()` path using `dict_to_xml` with `CrossIndustryInvoice` template. If False: legacy `ir.qweb._render('account_edi_ubl_cii.account_invoice_facturx_export_22', vals)` path with QWeb template.

### D4 — CII invoice type code interpretation

TypeCode 381 or 261 → `'refund'`, qty_factor=1. TypeCode 380, 389, or 527 → check `GrandTotalAmount`; if negative → `'refund'`, qty_factor=-1; else `'invoice'`, qty_factor=1. Other codes → None (unrecognized).

### D5 — CII date format

`DEFAULT_FACTURX_DATE_FORMAT = '%Y%m%d'` — 8-digit date format (YYYYMMDD) used throughout CII document for all date fields.

### D6 — Payment means code in CII

`PAYMENT_MEAN_CODES = {'Payment to bank account': 42, 'SEPA direct debit': 59}`. If `sdd_mandate_id` field exists on `account.payment` and invoice has reconciled SDD payments, code 59 (SEPA DD) is used; otherwise 42 (bank transfer). Maps to `ApplicableHeaderTradeSettlement/SpecifiedTradeSettlementPaymentMeans/TypeCode`.

### D7 — CII seller contact validation (BR-DE-6, BR-DE-7)

CII export constraints require `seller_phone` (partner.phone) and `seller_email` (company.email). These are German-specific Factur-X rules for ZUGFeRD compatibility, enforced in `_export_invoice_constraints()`.

### D8 — CII seller payment instructions constraint

For `out_invoice`, CII validates `partner_bank_id` and `partner_bank_id.sanitized_acc_number` (BR-DE-1: payment instructions mandatory for seller invoices).

### D9 — CII TaxSubtotal fixed tax adjustment

Fixed taxes are excluded from `TaxTotal` in CII: `tax_amount_currency -= fixed_tax_details['tax_amount_currency']`, `base_amount_currency += fixed_tax_details['tax_amount_currency']`. The totals `tax_basis_total_amount` and `tax_total_amount` are set after this adjustment.

### D10 — CII node structure overview

`_get_invoice_node()` calls `_cii_add_exchanged_document_context_node()`, `_cii_add_exchanged_document_node()`, `_cii_add_supply_chain_trade_transaction_node()`. The supply chain transaction contains seller/buyer trade parties, header trade delivery, header trade agreement, header trade settlement, and included supply chain trade line items.

---

## CAP-U48-09 BIS 3 / Peppol Profile Architecture

### D1 — BIS 3 class and customization ID

`account.edi.xml.ubl_bis3` inherits from `account.edi.xml.ubl_21` and `account.edi.ubl_pint_eu`. Customization ID for billing: `urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0`. For self-billing: `urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:selfbilling:3.0`.

### D2 — BIS 3 self-billing

`_can_export_selfbilling()` returns True if `_get_customization_id(process_type='selfbilling')` returns a value (always True for BIS 3). This allows buyer-created invoices.

### D3 — EHF 3 equivalence with BIS 3

EHF 3 (Norway) is explicitly documented as identical to BIS 3: "EHF Billing 3.0 is therefore done by implementing PEPPOL BIS Billing 3.0 without extensions or extra rules." The EHF3 format in the manifest is handled by the BIS 3 class.

### D4 — BIS 3 party node overrides

`_add_invoice_accounting_supplier_party_nodes()` and `_add_invoice_accounting_customer_party_nodes()` in BIS 3 delegate to `_ubl_add_accounting_supplier_party_node(sub_vals)` / `_ubl_add_accounting_customer_party_node(sub_vals)` from the PINT layer, passing the `document_node` in `sub_vals`.

### D5 — BIS 3 delivery nodes

`_add_invoice_delivery_nodes()` in BIS 3 delegates to `_ubl_add_delivery_nodes(sub_vals)`. In PINT layer, this is further constrained to maximum one Delivery element (`document_node['cac:Delivery'] = document_node['cac:Delivery'][0]`).

### D6 — BIS 3 line node overrides

BIS 3 overrides all line-node add methods to delegate to PINT/UBL layer helpers: `_ubl_add_line_id_node`, `_ubl_add_line_allowance_charge_nodes`, `_ubl_add_line_invoiced_quantity_node` / `_ubl_add_line_credited_quantity_node`, `_ubl_add_line_extension_amount_node`, `_ubl_add_line_pricing_reference_node`, `_ubl_add_line_tax_totals_nodes`, `_ubl_add_line_item_node`.

### D7 — BIS 3 monetary total

`_add_invoice_monetary_total_vals()` is overridden to a no-op in BIS 3; the monetary total is computed in `_ubl_add_legal_monetary_total_node(sub_vals)` at the time `_add_invoice_monetary_total_nodes()` is called.

### D8 — PINT invoice type codes

PINT layer sets `cbc:InvoiceTypeCode` 380 (invoice), 389 (self_invoice). `cbc:CreditNoteTypeCode` 381 (credit_note), 261 (self_credit_note). These codes are UBL-standard document type codes defined by UN/CEFACT UNCL1001.

### D9 — BIS 3 line tax category nodes suppressed

`_add_invoice_line_tax_category_nodes()` is overridden to a no-op in BIS 3. Line-level tax category information is included inside the Item node via `_ubl_add_line_item_node()` instead of as a separate TaxCategory on the line.

### D10 — BIS 3 invoice period nodes suppressed

`_add_invoice_line_period_nodes()` is overridden to a no-op in BIS 3.

---

## CAP-U48-10 Import (Inbound EDI) Flow

### D1 — Import entry point

`_import_invoice_ubl_cii()` in `account.edi.common` is the main import coordinator:
1. Checks invoice has no existing lines
2. Reads XML tree from `file_data['xml_tree']`
3. Calls `_get_import_document_amount_sign(tree)` → (move_type, qty_factor)
4. Reconciles move_type with journal type
5. Calls `_import_fill_invoice(invoice, tree, qty_factor)` (format-specific)
6. Calls `_correct_invoice_tax_amount(tree, invoice)` for rounding correction
7. If purchase document: stores XML file in `ubl_cii_xml_file` field
8. Posts import log via `message_post`

### D2 — UBL vs CII import fill

CII `_import_fill_invoice()` extracts:
- Currency: `.//{*}InvoiceCurrencyCode`
- Reference: `ExchangedDocument/ID`
- Invoice origin: `BuyerOrderReferencedDocument/IssuerAssignedID`
- Narration: `ExchangedDocument/IncludedNote/Content` and `SpecifiedTradePaymentTerms/Description`
- Payment reference: `ApplicableHeaderTradeSettlement/PaymentReference`
- Issue date: `ExchangedDocument/IssueDateTime/DateTimeString`
- Due date: `SpecifiedTradePaymentTerms/DueDateDateTime/DateTimeString`

### D3 — Partner search/creation priority

`_import_retrieve_customer_search_plan()` defines partner search priority:
1. `_import_retrieve_customer_from_vat`
2. `_import_retrieve_customer_from_eas_endpoint`
3. `_import_retrieve_customer_from_email`
4. `_import_retrieve_customer_from_phone`
5. `_import_retrieve_customer_from_name`

### D4 — Tax retrieval on import

`_retrieve_taxes()` in `account.edi.common` searches for matching taxes in priority order:
1. With fiscal position filter + price_include=False (+ exigibility if given)
2. With fiscal position filter + price_include=True (+ exigibility)
3. Without fiscal position filter + price_include=False
4. Without fiscal position filter + price_include=True
If price_include=True tax is matched, `price_unit *= (1 + tax.amount / 100)` to convert to tax-excluded basis.

### D5 — Rounding correction mechanism

`_correct_invoice_tax_amount()` is a hook that can override computed tax amounts. It is triggered after the first import to handle cases where the XML tax total differs by < 0.05 from the computed total (UBL rounding support). In `account.edi.common` this method is a no-op; specific formats override it.

### D6 — Document-level AllowanceCharge import

`_import_document_allowance_charges()` reads document-level allowance/charge elements, computes price_unit (base_amount * charge_indicator if base_amount given, else actual_amount), creates line vals with tax_ids derived from embedded tax percentage nodes.

### D7 — Prepaid amount detection

`_import_prepaid_amount()` reads the prepaid amount at the specified XPath (in CII: `ApplicableHeaderTradeSettlement/SpecifiedTradeSettlementHeaderMonetarySummation/TotalPrepaidAmount`) and logs a message if non-zero.

### D8 — Embedded attachment extraction

`_import_attachments()` looks for `AdditionalDocumentReference` nodes, extracts `EmbeddedDocumentBinaryObject` where mimeCode is in `SUPPORTED_FILE_TYPES`. Supported types: PDF, ODS, XLSX, JPEG, PNG, CSV. Base64 padding is corrected. If mimetype is PDF, it becomes the main attachment.

### D9 — Country code special handling

In `_import_retrieve_country()`: country code `'GB'` is mapped to `'UK'` for the Odoo base.UK xmlid lookup (Odoo uses UK not GB for the United Kingdom record).

### D10 — account.move extensions for EDI

`account.move` gains three new fields: `ubl_cii_xml_id` (Many2one to ir.attachment, computed), `ubl_cii_xml_file` (Binary, attachment=True), `ubl_cii_xml_filename` (Char computed). The file is detached on reset via `_get_fields_to_detach()`. The `_get_invoice_legal_documents()` override serves the XML via URL `/account/download_invoice_documents/{ids}/ubl`.

---

## CAP-U48-11 Thailand-Scope Analysis

### D1 — Thailand not in EAS_MAPPING

Thailand country code `'TH'` is not present in `EAS_MAPPING` in `account_edi_common.py`. This means there is no pre-configured Peppol EAS code for Thai partners — `peppol_eas` would not auto-compute for a partner with country_code='TH'. A Thai Thai implementer would need to manually assign an EAS or extend the mapping.

### D2 — Thailand not in format country lists

`_get_ubl_cii_formats_info()` does not list 'TH' in any format's country list. Therefore, `_get_suggested_ubl_cii_edi_format()` returns False for Thai companies in Community. No EDI format is auto-suggested for Thai companies.

### D3 — UBL BIS 3 as a valid framework for Thai e-Tax

The UBL BIS 3 format (EN 16931 compliant) is an internationally recognized electronic invoice format. Thailand's Revenue Department e-Tax Invoice standard (RD e-Tax Invoice) is based on a similar XML structure. The UBL framework in this module could be extended to support Thai e-Tax by: (a) adding 'TH' to `EAS_MAPPING` with a suitable EAS, (b) creating a new format class inheriting `account.edi.xml.ubl_20` or `account.edi.xml.ubl_bis3`, (c) overriding `_get_document_nsmap()` and `_get_document_type_code_vals()` for Thai-specific elements, (d) adding tax-specific fields for Thai VAT (7% standard rate, 0% for exports).

### D4 — Thai VAT rate in GST_COUNTRY_CODES

Thailand ('TH') is NOT in `GST_COUNTRY_CODES`. Therefore, if a Thai company generates a UBL invoice, the tax scheme ID would be `'VAT'` not `'GST'`. This is factually correct — Thailand uses VAT, not GST.

### D5 — Thai tax category code alignment

Thailand's standard VAT rate is 7% (reduced from 10%). In the existing framework, a Thai 7% tax with no explicit `ubl_cii_tax_category_code` set would compute to category `'S'` (standard rate) if supplier and customer are in the same country. Export transactions at 0% would compute to `'G'` (free export). These standard codes align with Thai RD requirements for e-Tax Invoice XML.

### D6 — GLN potential for Thai supply chain

Thailand does not mandate GLN in its e-Tax Invoice standard, but GLN from `account_add_gln` could be used in Thai e-procurement contexts (e.g., GS1 Thailand implementations or large retail supply chains). The field is available via `partner.global_location_number`.

### D7 — CII format relevance for Thailand

The CII Factur-X profile is specifically designed for France/Germany. Thailand uses neither Factur-X nor ZUGFeRD. The relevant format for a Thai implementation would be a UBL 2.1 profile, either BIS 3 based or a new Thai-specific profile.

### D8 — CONTRA indicator with U13/U24

U13 noted that `account_edi_ubl_cii` supports multiple formats but did not detail the class hierarchy or Thailand absence. This unit confirms: (a) Thailand is explicitly absent from both EAS_MAPPING and format country lists; (b) the extension architecture is available; (c) no Thai-specific UBL/CII class exists in Community 19.

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U48-C001 | CAP-U48-01-D1 | `account_add_gln/__manifest__.py:8` | `'auto_install': True` | FACT | — | — | account_add_gln has auto_install True, activates with account module | N-U48-001 |
| VDR-U48-C002 | CAP-U48-01-D1 | `account_add_gln/__manifest__.py:3` | `'summary': "This module adds the Global Location Number to the partner. Used on delivery addresses, it is used to identify stock locations and is mandatory on the UBL/CII eInvoices` | FACT | — | — | Manifest explicitly states GLN is mandatory on UBL/CII e-invoices | N-U48-002 |
| VDR-U48-C003 | CAP-U48-01-D2 | `account_add_gln/models/res_partner.py:7` | `global_location_number = fields.Char(string="GLN", help="Global Location Number")` | FACT | — | — | GLN field is a Char field with no length or format validation | N-U48-002 |
| VDR-U48-C004 | CAP-U48-01-D3 | `account_add_gln/views/res_partner_views.xml:10` | `<field name="global_location_number" invisible="type != 'delivery'"/>` | FACT | — | — | GLN field is hidden unless partner type is 'delivery' | N-U48-002 |
| VDR-U48-C005 | CAP-U48-01-D3 | `account_add_gln/views/res_partner_views.xml:13` | `<field name="global_location_number" invisible="type != 'delivery'"/>` | FACT | — | — | GLN is also placed in the inline child address form, still invisible unless type=delivery | N-U48-002 |
| VDR-U48-C006 | CAP-U48-02-D1 | `account_edi_ubl_cii/__manifest__.py:9` | Allows to export | FACT | — | — | Module description enumerates six supported EDI formats | N-U48-003 |
| VDR-U48-C007 | CAP-U48-02-D2 | `account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:18-21` | class AccountEdiXmlUBL20(models.AbstractModel) | FACT | — | — | UBL 2.0 class inherits from account.edi.ubl abstract base | N-U48-003 |
| VDR-U48-C008 | CAP-U48-02-D2 | `account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:11-14` | class AccountEdiXmlUBLBIS3(models.AbstractModel) | FACT | — | — | BIS 3 class uses multiple inheritance: UBL 2.1 + PINT EU | N-U48-003 |
| VDR-U48-C009 | CAP-U48-02-D2 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:28-31` | class AccountEdiXmlCii(models.AbstractModel) | FACT | — | — | CII Factur-X class inherits from account.edi.cii | N-U48-004 |
| VDR-U48-C010 | CAP-U48-02-D3 | `account_edi_ubl_cii/models/res_partner.py:332-346` | def _get_edi_builder(self, invoice_edi_format) | FACT | — | — | EDI builder dispatch is a conditional method on res.partner | N-U48-003 |
| VDR-U48-C011 | CAP-U48-02-D4 | `account_edi_ubl_cii/models/res_partner.py:168-181` | return | FACT | — | — | Format-to-country mapping uses PEPPOL_DEFAULT_COUNTRIES list from account module | N-U48-003 |
| VDR-U48-C012 | CAP-U48-02-D4 | `account_edi_ubl_cii/models/res_partner.py:175-180` | 'xrechnung': {'countries | FACT | — | — | Country-specific formats: XRechnung for DE, A-NZ for NZ/AU, NLCIUS for NL, UBL-SG for SG, Factur-X for FR, ZUGFeRD for DE | N-U48-003 |
| VDR-U48-C013 | CAP-U48-02-D5 | `account_edi_ubl_cii/models/res_partner.py:205` | if self.peppol_eas == '0204 | FACT | — | — | Leitweg-ID EAS (0204) forces XRechnung format for German companies | N-U48-003 |
| VDR-U48-C014 | CAP-U48-03-D1 | `account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:39-58` | def _export_invoice(self, invoice) | FACT | — | — | Export sets invoice with partner language context before building document node | N-U48-003 |
| VDR-U48-C015 | CAP-U48-03-D1 | `account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:55-58` | xml_content = dict_to_xml | FACT | — | — | UBL XML is serialized with XML declaration and UTF-8 encoding | N-U48-003 |
| VDR-U48-C016 | CAP-U48-03-D3 | `account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:161-177` | 'document_type | FACT | — | — | Document type classification: debit_note > credit_note > invoice | N-U48-003 |
| VDR-U48-C017 | CAP-U48-03-D3 | `account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:156-158` | if invoice.is_purchase_document() | FACT | — | — | Supplier and customer roles are swapped for purchase documents | N-U48-003 |
| VDR-U48-C018 | CAP-U48-03-D4 | `account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:71-82` | def _get_document_nsmap(self, vals) | FACT | — | — | UBL 2.0 uses standard OASIS UBL 2 namespace URNs | N-U48-003 |
| VDR-U48-C019 | CAP-U48-03-D5 | `account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:87-113` | def _get_tags_for_document_type(self, vals) | FACT | — | — | Document-type-to-tag mapping covers invoice, credit_note, debit_note, order | N-U48-003 |
| VDR-U48-C020 | CAP-U48-04-D3 | `account_edi_ubl_cii/models/account_edi_ubl_pint.py:91-96` | def _ubl_add_document_currency_code_node | FACT | — | — | PINT layer sets DocumentCurrencyCode to currency.name (ISO 4217 code) | N-U48-005 |
| VDR-U48-C021 | CAP-U48-04-D5 | `account_edi_ubl_cii/models/account_edi_ubl_pint.py:62-71` | notes.append(_ | FACT | — | — | invoice.narration is HTML-stripped to plain text for cbc:Note | N-U48-005 |
| VDR-U48-C022 | CAP-U48-04-D8 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:184-193` | 'seller_specified_legal_organization | FACT | — | — | company_registry fields map to seller/buyer legal organization in CII | N-U48-004 |
| VDR-U48-C023 | CAP-U48-04-D9 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:111-114` | def _get_scheduled_delivery_time(self, invoice) | FACT | — | — | Delivery date falls back to invoice_date if delivery_date not set | N-U48-004 |
| VDR-U48-C024 | CAP-U48-04-D10 | `account_edi_ubl_cii/models/account_edi_ubl_pint.py:16-30` | def _ubl_add_invoice_type_code_node(self, vals) | FACT | — | — | PINT invoice type codes: 380 for standard invoice, 389 for self-invoice | N-U48-005 |
| VDR-U48-C025 | CAP-U48-04-D10 | `account_edi_ubl_cii/models/account_edi_ubl_pint.py:23-30` | def _ubl_add_credit_note_type_code_node | FACT | — | — | PINT credit note type codes: 381 for credit_note, 261 for self_credit_note | N-U48-005 |
| VDR-U48-C026 | CAP-U48-04-D4 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:121-128` | def _get_exchanged_document_vals(self, invoice) | FACT | — | — | CII ExchangedDocument: invoice.name → ID, move_type out_invoice → type_code 380 | N-U48-004 |
| VDR-U48-C027 | CAP-U48-05-D1 | `account_edi_ubl_cii/models/res_partner.py:43-50` | peppol_endpoint = fields.Char | FACT | — | — | peppol_endpoint is stored computed with write-back (readonly=False), tracked | N-U48-006 |
| VDR-U48-C028 | CAP-U48-05-D1 | `account_edi_ubl_cii/models/res_partner.py:51-151` | peppol_eas = fields.Selection | FACT | — | — | peppol_eas Selection field has ~60 EAS code options | N-U48-006 |
| VDR-U48-C029 | CAP-U48-05-D2 | `account_edi_ubl_cii/models/res_partner.py:278-303` | @api.depends(lambda | FACT | — | — | peppol_eas auto-selects first valid non-deprecated EAS for country | N-U48-006 |
| VDR-U48-C030 | CAP-U48-05-D3 | `account_edi_ubl_cii/models/account_edi_common.py:58-125` | EAS_MAPPING = | FACT | — | — | Thailand (TH) is absent from EAS_MAPPING; no Peppol EAS auto-configured for Thai partners | N-U48-011 |
| VDR-U48-C031 | CAP-U48-05-D4 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:279` | `'vat': self._find_value(f".//ram:{role}/ram:SpecifiedTaxRegistration/ram:ID[string-length(text()) > 5]", tree)` | FACT | — | — | CII import reads VAT from SpecifiedTaxRegistration/ID with minimum length 6 chars | N-U48-004 |
| VDR-U48-C032 | CAP-U48-05-D6 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:286-293` | def _get_postal_address(self, tree, role) | FACT | — | — | CII postal address maps: LineOne→street, LineTwo→street2, CityName→city, PostcodeCode→zip, CountryID→country_code | N-U48-007 |
| VDR-U48-C033 | CAP-U48-05-D8 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:307-315` | bank_detail_nodes | FACT | — | — | CII import reads IBAN from PayeePartyCreditorFinancialAccount/IBANID | N-U48-007 |
| VDR-U48-C034 | CAP-U48-05-D9 | `account_edi_ubl_cii/models/res_partner.py:315-329` | def _build_error_peppol_endpoint | FACT | — | — | EAS-specific endpoint format validation with regex and length checks | N-U48-006 |
| VDR-U48-C035 | CAP-U48-05-D10 | `account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:8` | `CHORUS_PRO_PEPPOL_ID = "0009:11000201100044"` | FACT | — | — | Chorus Pro (French procurement portal) identified by hardcoded EAS:endpoint string | N-U48-006 |
| VDR-U48-C036 | CAP-U48-06-D1 | `account_edi_ubl_cii/models/account_tax.py:7-10` | ubl_cii_tax_category_code = fields.Selection | FACT | — | — | account.tax gains 10-option tax category code Selection field for UBL/CII | N-U48-008 |
| VDR-U48-C037 | CAP-U48-06-D1 | `account_edi_ubl_cii/models/account_tax.py:120-125` | ubl_cii_requires_exemption_reason | FACT | — | — | Exemption reason is required for categories AE, E, G, O, K | N-U48-008 |
| VDR-U48-C038 | CAP-U48-06-D2 | `account_edi_ubl_cii/models/account_edi_common.py:405-463` | def _get_tax_category_code | FACT | — | — | Tax category code computation: manual override > country-specific rules > same-country/EEA/cross-border logic | N-U48-008 |
| VDR-U48-C039 | CAP-U48-06-D3 | `account_edi_ubl_cii/models/account_edi_common.py:228-231` | GST_COUNTRY_CODES = | FACT | — | — | GST country codes list; Thailand absent; Thai invoices use 'VAT' scheme ID not 'GST' | N-U48-008 |
| VDR-U48-C040 | CAP-U48-06-D4 | `account_edi_ubl_cii/models/account_edi_ubl.py:97-162` | def _ubl_default_tax_category_grouping_key | FACT | — | — | Tax category grouping key for UBL TaxTotal/TaxSubtotal includes scheme_id (VAT/GST) | N-U48-008 |
| VDR-U48-C041 | CAP-U48-06-D6 | `account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:176` | `'fixed_taxes_as_allowance_charges': True` | FACT | — | — | Fixed taxes are always converted to AllowanceCharge in UBL export by default | N-U48-008 |
| VDR-U48-C042 | CAP-U48-06-D7 | `account_edi_ubl_cii/models/account_edi_ubl.py:37-47` | def _ubl_is_recycling_contribution_tax | FACT | — | — | Recycling contribution taxes: fixed type + include_base_amount=True | N-U48-008 |
| VDR-U48-C043 | CAP-U48-06-D8 | `account_edi_ubl_cii/models/account_edi_ubl.py:49-59` | def _ubl_is_excise_tax(self, tax_data) | FACT | — | — | Excise taxes: code type + include_base_amount=True | N-U48-008 |
| VDR-U48-C044 | CAP-U48-06-D9 | `account_edi_ubl_cii/models/account_edi_common.py:465-500` | def _get_tax_exemption_reason | FACT | — | — | Auto-default exemption reasons: VATEX-EU-G for G, VATEX-EU-IC for K, "Exempt from tax" for E | N-U48-008 |
| VDR-U48-C045 | CAP-U48-06-D10 | `account_edi_ubl_cii/models/account_edi_common.py:361-374` | def _get_belgian_cocontractant_note | FACT | — | — | Belgian co-contractant fiscal position triggers reverse-charge notice text | N-U48-008 |
| VDR-U48-C046 | CAP-U48-07-D1 | `account_edi_ubl_cii/models/account_edi_common.py:908-944` | def _retrieve_line_vals | FACT | — | — | Line import formula per UBL/CII spec with BT references documented inline | N-U48-009 |
| VDR-U48-C047 | CAP-U48-07-D2 | `account_edi_ubl_cii/models/account_edi_common.py:998-1012` | if gross_price_unit is not None | FACT | — | — | price_unit derivation priority: gross÷basis > (net+rebate)÷basis > subtotal÷qty | N-U48-009 |
| VDR-U48-C048 | CAP-U48-07-D3 | `account_edi_ubl_cii/models/account_edi_common.py:23-51` | UOM_TO_UNECE_CODE = | FACT | — | — | 26-entry UoM to UNECE Rec 20 mapping; default fallback 'C62' for unrecognized UoMs | N-U48-009 |
| VDR-U48-C049 | CAP-U48-07-D4 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:397-402` | 'product': | FACT | — | — | CII product identification: SellerAssignedID→internal reference, GlobalID→barcode | N-U48-009 |
| VDR-U48-C050 | CAP-U48-07-D5 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:393-396` | 'name': | FACT | — | — | CII line name: Description preferred over Name | N-U48-009 |
| VDR-U48-C051 | CAP-U48-07-D6 | `account_edi_ubl_cii/models/account_edi_common.py:1133-1161` | def _retrieve_line_charges | FACT | — | — | ReasonCode AEO on AllowanceCharge triggers fixed tax lookup; amount divided by quantity to get per-unit amount | N-U48-009 |
| VDR-U48-C052 | CAP-U48-07-D8 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:370-375` | def _get_invoice_line_xpaths | FACT | — | — | CII billing period dates map to deferred_start_date / deferred_end_date if those fields exist on the line | N-U48-009 |
| VDR-U48-C053 | CAP-U48-07-D10 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:244-248` | # Invert the quantity | FACT | — | — | Negative price total lines have quantity and price negated (BR-27/BR-28 compliance) | N-U48-009 |
| VDR-U48-C054 | CAP-U48-08-D1 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:15-19` | CII_NAMESPACES = | FACT | — | — | CII uses UN/CEFACT namespace URIs for ram, rsm, udt | N-U48-004 |
| VDR-U48-C055 | CAP-U48-08-D2 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:194` | `'document_context_id': "urn:cen.eu:en16931:2017#conformant#urn:factur-x.eu:1p0:extended"` | FACT | — | — | Factur-X Extended profile context identifier hardcoded | N-U48-004 |
| VDR-U48-C056 | CAP-U48-08-D3 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:261-271` | def _export_invoice(self, invoice) | FACT | — | — | CII export path controlled by ir.config_parameter; new dict_to_xml path is default | N-U48-004 |
| VDR-U48-C057 | CAP-U48-08-D4 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:408-424` | def _get_import_document_amount_sign(self, tree) | FACT | — | — | TypeCode 527 (proforma) treated as invoice; negative GrandTotal triggers refund conversion | N-U48-004 |
| VDR-U48-C058 | CAP-U48-08-D5 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:14` | `DEFAULT_FACTURX_DATE_FORMAT = '%Y%m%d'` | FACT | — | — | All dates in CII are formatted YYYYMMDD without separators | N-U48-004 |
| VDR-U48-C059 | CAP-U48-08-D6 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:22-25` | PAYMENT_MEAN_CODES = | FACT | — | — | CII payment means: code 42 for bank transfer, 59 for SEPA direct debit | N-U48-004 |
| VDR-U48-C060 | CAP-U48-08-D7 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:63-79` | # [BR-08]-An Invoice | FACT | — | — | CII constraints require seller phone (BR-DE-6) and seller email (BR-DE-7) | N-U48-004 |
| VDR-U48-C061 | CAP-U48-08-D9 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:167-173` | fixed_taxes_keys | FACT | — | — | Fixed taxes removed from TaxTotal in CII; their amount shifted to base_amount | N-U48-008 |
| VDR-U48-C062 | CAP-U48-08-D10 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:461-469` | def _get_invoice_node(self, vals) | FACT | — | — | New CII export builds three top-level nodes: ExchangedDocumentContext, ExchangedDocument, SupplyChainTradeTransaction | N-U48-004 |
| VDR-U48-C063 | CAP-U48-09-D1 | `account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:50-54` | def _get_customization_id | FACT | — | — | BIS 3 customization ID matches Peppol BIS Billing 3.0 specification URN | N-U48-010 |
| VDR-U48-C064 | CAP-U48-09-D1 | `account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:52-54` | return 'urn:cen.eu:en16931:2017#complian | FACT | — | — | BIS 3 self-billing customization ID references Peppol self-billing profile | N-U48-010 |
| VDR-U48-C065 | CAP-U48-09-D3 | `account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:16-31` | * Documentation | FACT | — | — | EHF 3 (Norway) implemented as BIS 3 without additional rules per official Norwegian procurement authority | N-U48-010 |
| VDR-U48-C066 | CAP-U48-09-D4 | `account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:56-71` | def _add_invoice_accounting_supplier_party_nodes | FACT | — | — | BIS 3 overrides supplier/customer party node methods to delegate to PINT layer | N-U48-010 |
| VDR-U48-C067 | CAP-U48-09-D7 | `account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:130-132` | def _add_invoice_monetary_total_vals(self, vals) | FACT | — | — | BIS 3 no-ops the monetary total vals computation (handled differently) | N-U48-010 |
| VDR-U48-C068 | CAP-U48-09-D9 | `account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:189-191` | def _add_invoice_line_tax_category_nodes | FACT | — | — | BIS 3 suppresses separate line TaxCategory nodes | N-U48-010 |
| VDR-U48-C069 | CAP-U48-09-D10 | `account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:167-169` | def _add_invoice_line_period_nodes | FACT | — | — | BIS 3 suppresses line-level period nodes | N-U48-010 |
| VDR-U48-C070 | CAP-U48-10-D1 | `account_edi_ubl_cii/models/account_edi_common.py:564-616` | def _import_invoice_ubl_cii | FACT | — | — | Import uses context manager _get_edi_creation; qty_factor from document sign detection | N-U48-009 |
| VDR-U48-C071 | CAP-U48-10-D1 | `account_edi_ubl_cii/models/account_edi_common.py:601-611` | # This has to be | FACT | — | — | XML attachment stored in ubl_cii_xml_file only for purchase documents | N-U48-009 |
| VDR-U48-C072 | CAP-U48-10-D3 | `account_edi_ubl_cii/models/account_edi_common.py:1232-1240` | def _import_retrieve_customer_search_plan | FACT | — | — | Five-step partner search plan; VAT first, then EAS/endpoint, then email/phone/name | N-U48-007 |
| VDR-U48-C073 | CAP-U48-10-D4 | `account_edi_ubl_cii/models/account_edi_common.py:1071-1131` | def _retrieve_taxes | FACT | — | — | Tax import attempts price_include=False first, then True; adapts price_unit if include tax found | N-U48-008 |
| VDR-U48-C074 | CAP-U48-10-D5 | `account_edi_ubl_cii/models/account_edi_common.py:1171-1172` | def _correct_invoice_tax_amount | FACT | — | — | Tax amount correction hook is a no-op in base; format subclasses can override | N-U48-008 |
| VDR-U48-C075 | CAP-U48-10-D6 | `account_edi_ubl_cii/models/account_edi_common.py:732-773` | def _import_document_allowance_charges | FACT | — | — | Document-level allowance charge indicator: 'false'→discount(-1), 'true'→charge(+1) | N-U48-009 |
| VDR-U48-C076 | CAP-U48-10-D7 | `account_edi_ubl_cii/models/account_edi_common.py:799-806` | def _import_prepaid_amount | FACT | — | — | Non-zero prepaid amount is logged as a message only; not automatically reconciled | N-U48-009 |
| VDR-U48-C077 | CAP-U48-10-D8 | `account_edi_ubl_cii/models/account_edi_common.py:250-257` | SUPPORTED_FILE_TYPES = | FACT | — | — | Six MIME types supported for embedded attachment extraction from XML | N-U48-009 |
| VDR-U48-C078 | CAP-U48-10-D9 | `account_edi_ubl_cii/models/account_edi_common.py:1227-1230` | if country_code == 'GB | FACT | — | — | GB country code mapped to base.uk xmlid; all other codes lowercased for base.{code} lookup | N-U48-007 |
| VDR-U48-C079 | CAP-U48-10-D10 | `account_edi_ubl_cii/models/account_move.py:17-27` | ubl_cii_xml_id = fields.Many2one | FACT | — | — | account.move gains ubl_cii_xml_file Binary field (stored as attachment, not copied on copy) | N-U48-003 |
| VDR-U48-C080 | CAP-U48-10-D10 | `account_edi_ubl_cii/models/account_move.py:64-90` | def _get_invoice_legal_documents | FACT | — | — | _get_invoice_legal_documents serves stored XML first; if allow_fallback generates XML on-the-fly | N-U48-003 |
| VDR-U48-C081 | CAP-U48-11-D1 | `account_edi_ubl_cii/models/account_edi_common.py:58-125` | EAS_MAPPING = | FACT | — | C1 | Thailand absent from EAS_MAPPING; Thai partner peppol_eas will not auto-compute | N-U48-011 |
| VDR-U48-C082 | CAP-U48-11-D2 | `account_edi_ubl_cii/models/res_partner.py:168-181` | return | FACT | — | C1 | Thailand absent from all format country lists; no EDI format suggested for Thai companies in Community | N-U48-011 |
| VDR-U48-C083 | CAP-U48-11-D4 | `account_edi_ubl_cii/models/account_edi_common.py:228-231` | GST_COUNTRY_CODES = | FACT | — | C1 | Thai invoices would use scheme_id='VAT' (not 'GST') in XML; factually correct for Thai VAT | N-U48-011 |
| VDR-U48-C085 | CAP-U48-06-D2 | `account_edi_ubl_cii/models/account_edi_common.py:429-463` | return 'M'  # Ceuta & Mellila | FACT | — | — | EEA cross-border detection: both in EEA→K (intra-community), one in EEA→G (export/import) | N-U48-008 |
| VDR-U48-C086 | CAP-U48-06-D5 | `account_edi_ubl_cii/models/account_edi_ubl.py:164-182` | def _ubl_default_tax_subtotal_tax_catego | FACT | — | — | TaxSubtotal grouping by full tax category key (including percent); each percent/category combination becomes a separate TaxSubtotal | N-U48-008 |
| VDR-U48-C087 | CAP-U48-06-D5 | `account_edi_ubl_cii/models/account_edi_ubl.py:184-195` | def _ubl_default_tax_total_grouping_key | FACT | — | — | TaxTotal level groups only by withholding flag and currency; all non-withholding taxes go in one TaxTotal per currency | N-U48-008 |
| VDR-U48-C088 | CAP-U48-07-D3 | `account_edi_ubl_cii/models/account_edi_common.py:338-345` | def _get_uom_unece_code(self, uom) | FACT | — | — | UoM lookup uses external XML ID from the UoM record; unrecognized UoMs default to C62 | N-U48-009 |
| VDR-U48-C089 | CAP-U48-07-D7 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:383-384` | `'rebate': './{*}SpecifiedLineTradeAgreement/{*}GrossPriceProductTradePrice/{*}AppliedTradeAllowanceCharge/{*}ActualAmount'` | FACT | — | — | CII item price rebate (BT-147) XPath: GrossPriceProductTradePrice/AppliedTradeAllowanceCharge/ActualAmount | N-U48-009 |
| VDR-U48-C090 | CAP-U48-07-D1 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:386` | `'delivered_qty': './{*}SpecifiedLineTradeDelivery/{*}BilledQuantity'` | FACT | — | — | CII billed quantity (BT-129) XPath: SpecifiedLineTradeDelivery/BilledQuantity | N-U48-009 |
| VDR-U48-C091 | CAP-U48-07-D1 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:392` | `'line_total_amount': './{*}SpecifiedLineTradeSettlement/{*}SpecifiedTradeSettlementLineMonetarySummation/{*}LineTotalAmount'` | FACT | — | — | CII line total (BT-131) XPath: LineTotalAmount under SpecifiedTradeSettlementLineMonetarySummation | N-U48-009 |
| VDR-U48-C092 | CAP-U48-08-D3 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:268-271` | vals = self._export_invoice_vals | FACT | — | — | Legacy CII export uses QWeb template named account_invoice_facturx_export_22 | N-U48-004 |
| VDR-U48-C093 | CAP-U48-10-D2 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:304` | invoice_values['currency_id'] | FACT | — | — | CII import: ExchangedDocument/ID maps to invoice ref field | N-U48-004 |
| VDR-U48-C094 | CAP-U48-10-D2 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:327-337` | invoice_values['payment_reference'] | FACT | — | — | CII import: IssueDateTime/DateTimeString parsed with YYYYMMDD format to invoice_date | N-U48-004 |
| VDR-U48-C095 | CAP-U48-04-D7 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:321-325` | './/{*}BuyerOrderReferencedDocument/ | FACT | — | — | CII import: BuyerOrderReferencedDocument/IssuerAssignedID→invoice_origin; PaymentReference→payment_reference | N-U48-004 |
| VDR-U48-C096 | CAP-U48-04-D6 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:335-337` | due_date = tree.findtext | FACT | — | — | CII import: DueDateDateTime maps to invoice_date_due | N-U48-004 |
| VDR-U48-C097 | CAP-U48-10-D6 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:359-368` | def _get_document_allowance_charge_xpaths(self) | FACT | — | — | CII document-level AllowanceCharge XPaths: root under ApplicableHeaderTradeSettlement | N-U48-009 |
| VDR-U48-C098 | CAP-U48-10-D2 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:344-346` | invoice_line_vals | FACT | — | — | CII line items XPath: SupplyChainTradeTransaction/IncludedSupplyChainTradeLineItem | N-U48-009 |
| VDR-U48-C099 | CAP-U48-10-D2 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:356-357` | def _get_tax_nodes(self, tree) | FACT | — | — | CII tax rate nodes: all ApplicableTradeTax/RateApplicablePercent found anywhere in document | N-U48-008 |
| VDR-U48-C100 | CAP-U48-02-D3 | `account_edi_ubl_cii/models/res_partner.py:30-39` | invoice_edi_format = fields.Selection | FACT | — | — | invoice_edi_format Selection on res.partner adds 7 format options including Singapore (SG) and Australia (A-NZ) | N-U48-003 |
| VDR-U48-C101 | CAP-U48-05-D2 | `account_edi_ubl_cii/models/res_partner.py:247-264` | self.ensure_one() | FACT | — | — | Belgian company_registry endpoint falls back to VAT number if registry absent | N-U48-006 |
| VDR-U48-C102 | CAP-U48-05-D2 | `account_edi_ubl_cii/models/res_partner.py:12-17` | PEPPOL_ENDPOINT_INVALIDCHARS_RE | FACT | — | — | EAS-specific endpoint sanitization removes disallowed characters per EAS type | N-U48-006 |
| VDR-U48-C103 | CAP-U48-08-D6 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:254-257` | if self.env['account.payment']._fields.get | FACT | — | — | SDD detection checks for sdd_mandate_id field existence before accessing it (module-safe guard) | N-U48-004 |
| VDR-U48-C104 | CAP-U48-07-D2 | `account_edi_ubl_cii/models/account_edi_common.py:1009-1011` | currency = self.env.company.currency_id | FACT | — | — | Discount percentage inferred from subtotal vs price_unit*qty using company currency rounding | N-U48-009 |
| VDR-U48-C105 | CAP-U48-07-D2 | `account_edi_ubl_cii/models/account_edi_common.py:1020-1031` | net_price_unit is not None | FACT | — | — | Special handling for bad XML: zero net_price_unit with zero qty sets qty=1, price_unit=price_subtotal | N-U48-009 |
| VDR-U48-C106 | CAP-U48-10-D4 | `account_edi_ubl_cii/models/account_edi_common.py:1127-1131` | else | FACT | — | — | Missing tax warning logged; import continues with no tax on line if lookup fails | N-U48-008 |
| VDR-U48-C107 | CAP-U48-10-D8 | `account_edi_ubl_cii/models/account_edi_common.py:660-668` | # Upon receiving | FACT | — | — | Base64 padding correction: appends 0-3 '=' chars based on text length modulo 3 | N-U48-009 |
| VDR-U48-C108 | CAP-U48-03-D2 | `account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:123-148` | def _get_invoice_node(self, vals) | FACT | — | — | Invoice node building is strictly sequential; each method mutates document_node or vals | N-U48-003 |
| VDR-U48-C110 | CAP-U48-11-D6 | `account_add_gln/models/res_partner.py:7` | `global_location_number = fields.Char(string="GLN"` | FACT | condition: delivery partner | C1 | GLN field available on delivery partners for Thai supply chain contexts; no Thai mandate requires it | N-U48-002 |
| VDR-U48-C111 | CAP-U48-04-D2 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:332-334` | issue_date = tree.findtext | FACT | — | — | CII invoice_date parsed from YYYYMMDD string using datetime.strptime | N-U48-004 |
| VDR-U48-C112 | CAP-U48-10-D3 | `account_edi_ubl_cii/models/res_partner.py:347-358` | @api.model | FACT | — | — | EAS+endpoint partner search is an exact match on both fields | N-U48-007 |
| VDR-U48-C113 | CAP-U48-10-D1 | `account_edi_ubl_cii/models/account_edi_common.py:596-600` | with invoice._get_edi_creation() as invoice | FACT | — | — | Tax amount correction runs in a second _get_edi_creation context after the primary import | N-U48-008 |
| VDR-U48-C114 | CAP-U48-02-D5 | `account_edi_ubl_cii/models/res_partner.py:211-213` | def _get_ubl_cii_edi_format(self) | FACT | — | — | Manual invoice_edi_format on partner always overrides the auto-detected format | N-U48-003 |
| VDR-U48-C115 | CAP-U48-06-D1 | `account_edi_ubl_cii/models/account_tax.py:23-118` | ubl_cii_tax_exemption_reason_code | FACT | — | — | ~60 exemption reason codes span VATEX-EU-* (standard EU) and VATEX-FR-* (France-specific) | N-U48-008 |
| VDR-U48-C116 | CAP-U48-10-D6 | `account_edi_ubl_cii/models/account_edi_common.py:748-772` | quantity = 1 | FACT | — | — | Document AllowanceCharge tax lookup by percentage amount and type_tax_use only (no country filter at this level) | N-U48-008 |
| VDR-U48-C117 | CAP-U48-09-D2 | `account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:47-48` | def _can_export_selfbilling(self) | FACT | — | — | BIS 3 always permits self-billing export (returns non-empty string for selfbilling) | N-U48-010 |
| VDR-U48-C118 | CAP-U48-05-D3 | `account_edi_ubl_cii/models/account_edi_common.py:57` | `DEPRECATED_PEPPOL_EAS = {'0037', '0213', '9955', '0193'}` | FACT | — | — | Four EAS codes deprecated: Finnish LY-tunnus (0037), Finnish VAT (0213), Swedish VAT (9955), UBL.BE (0193) | N-U48-006 |
| VDR-U48-C120 | CAP-U48-08-D10 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:452-458` | def _get_document_nsmap(self) | FACT | — | — | New CII export adds qdt and xsi namespaces beyond the legacy three | N-U48-004 |
| VDR-U48-C121 | CAP-U48-04-D7 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:189-193` | 'buyer_reference | FACT | — | — | buyer_reference and contract_reference use field-existence guards (hasattr pattern via _fields check) | N-U48-004 |
| VDR-U48-C122 | CAP-U48-10-D4 | `account_edi_ubl_cii/models/account_edi_common.py:1082-1084` | fpos_domain | FACT | — | — | For domestic fiscal positions, tax search includes taxes with no fiscal position restriction | N-U48-008 |
| VDR-U48-C123 | CAP-U48-10-D5 | `account_edi_ubl_cii/models/account_edi_xml_cii_facturx.py:475-481` | def _import_invoice_ubl_cii | FACT | — | — | New CII import path delegates to _cii_import_invoice in account.edi.cii | N-U48-004 |
| VDR-U48-C125 | CAP-U48-02-D3 | `account_edi_ubl_cii/models/res_partner.py:176-181` | 'ubl_a_nz': {'countries | FACT | — | — | A-NZ and SG profiles not yet connected to Odoo's Peppol Access Point (on_peppol=False) | N-U48-010 |

---

## Ten-dimension Summary Table

| Dimension | Finding |
|---|---|
| Field-level mapping (UBL) | invoice.name→ID, invoice_date→IssueDate, currency_id.name→DocumentCurrencyCode, partner.vat→CompanyID, partner_bank_id→IBAN, narration→Note, company_registry→LegalOrganization |
| Field-level mapping (CII) | Same invoice fields; dates YYYYMMDD format; delivery_date→ScheduledDeliveryTime; ExchangedDocument/ID←invoice.name; BuyerOrderReferencedDocument←invoice_origin |
| Extension architecture | Python abstract model inheritance chain (common→ubl→ubl_20→ubl_21→bis3+pint_eu); each level overrides/extends node-add methods; new format = new class inheriting nearest fit |
| Country profile overrides | xrechnung(DE), nlcius(NL), ubl_a_nz(NZ/AU), ubl_sg(SG) each inherit ubl_21/ubl_bis3 and override constraints, filename, specific nodes |
| Tax framework | ubl_cii_tax_category_code field on account.tax; 10 categories; auto-computed from country logic; exemption reason codes managed per category |
| Thai e-Tax relevance | No native Thai support; TH absent from EAS_MAPPING and format country lists; extension path exists; UBL 2.1 profile with 7%/0% VAT compatible with framework's 'S'/'G' category codes |
| Inbound (import) flow | 5-step partner search; 4-step price_include tax lookup; embedded PDF/attachment extraction; prepaid amount warning; document-level AllowanceCharge to invoice lines |
| Outbound (export) flow | Builder dispatched from res.partner._get_edi_builder; invoice with lang context; node-builder chain; constraints validated; dict_to_xml serialization |
| GLN routing | global_location_number Char on res.partner (delivery type only); consumed by UBL delivery party node; no validation; auto_install with account |
| Delta vs U13/U24 | U13 confirmed format breadth; this unit adds: class hierarchy detail, field-level XPaths, Thailand absence confirmed in source, tax category auto-logic, import algorithm details |
