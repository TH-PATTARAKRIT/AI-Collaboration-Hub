# U34 E-invoice Bridges and Utilities - Neutral Knowledge (Odoo 19 Community, clean-room layer)

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Source revision 19.0.post20260921. Scope: structured electronic invoice export and import (format registry, mapping, rules, attachments), the accounting-to-fleet bridge, the partner location number, the developer documentation service and attachment text indexation. Country-specific formats are only noted as an extension boundary.

## CAP-U34-01 E-invoice format registry, partner electronic address and delivery-location number

### WHAT
- [N-U34-001] Each business partner can be assigned one of seven electronic invoice formats: a French format, an EU-wide Peppol format, two German formats, a Dutch format, an Australia and New Zealand format and a Singapore format. The choice is made per partner and is optional.
- [N-U34-002] Each format is described by a small record stating the countries it serves, whether it travels over the Peppol network, a precedence number and whether extra attachments may be embedded in the file; packs for other countries add formats by adding records to the same description.
- [N-U34-003] A partner can carry an electronic address made of a scheme code and an endpoint identifier; the scheme list contains about ninety national and international identifier schemes.
- [N-U34-004] A partner of delivery type can carry a Global Location Number, a free-text identifier of the physical delivery location.

### WHY
- [N-U34-005] Buyers that receive electronic invoices need a machine-readable identifier of the sender and receiver and a known format; the format choice drives which file is produced for each customer.
- [N-U34-006] The delivery-location number lets the receiving system identify the physical place of delivery on the invoice.

### BUSINESS RULE
- [N-U34-007] When no format is stored on the partner, a suggestion is derived from the country of the commercial partner: where several formats serve one country the one with the lowest precedence number wins, a missing number counting as 100; a German partner whose electronic address scheme is the German routing identifier gets the German public-sector format instead.
- [N-U34-008] Consequence of the precedence rule: for French, German and Dutch partners the national format (precedence 100) is suggested ahead of the EU-wide format (precedence 200); for Belgian and other EU partners the EU-wide format is the only candidate; for Australia, New Zealand and Singapore the regional format is the only candidate; countries not in any list (including Thailand) receive no suggestion.
- [N-U34-009] A second helper used for buyer-issued invoicing eligibility falls back to the EU-wide Peppol format whenever the suggestion is empty or not a Peppol format, so every partner is treated as Peppol-capable for that purpose.
- [N-U34-010] The scheme of a partner is recomputed when its country, tax identifier or company registry changes, but only if the current scheme is not one of the schemes known for the partner country; deprecated schemes are skipped unless they are the only choice, and the first scheme whose mapped partner field holds a valid value is chosen, else the first listed.
- [N-U34-011] When the scheme changes, the endpoint is cleaned of illegal characters and replaced by the value of the mapped partner field (tax identifier or company registry) if that value is valid for the scheme; otherwise the existing endpoint is kept.
- [N-U34-012] Belgian partners without a company registry number use their tax identifier without the country prefix as endpoint.
- [N-U34-013] Four schemes are deprecated and hidden from the selectable list unless a partner already uses one of them.
- [N-U34-014] The delivery-location number is written on the exported delivery only when the location-number module is installed and the delivery partner has a value, using the global location scheme code; the Factur-X builder writes it only for the ship-to party.

### STATE
- [N-U34-015] Partner format: not set (suggestion applies) or explicitly set to one of seven values or explicitly disabled by the shared accounting layer. No lifecycle states exist; the format is read at the moment an invoice is exported.

### OPTIONALITY
- [N-U34-016] The module installs automatically with accounting; a format is only used when set on the partner or suggested for the partner country, so a company outside the listed countries produces no electronic invoice file by default.
- [N-U34-017] The Global Location Number module installs automatically with accounting, adds the field only, and is shown only for partners of delivery type; it is optional on every document.
- [N-U34-018] Only the EU-wide Peppol format supports embedding extra attachments in the file.

### DEPENDENCY
- [N-U34-019] The format list, builder selection and partner fields live in the electronic-invoice module; the accounting module supplies the base empty format list, the stored per-company format choice and the country deduction helper.
- [N-U34-020] Electronic address matching is also used by the import path as the second step of partner lookup after tax identifier.

### CONSTRAINT
- [N-U34-021] The endpoint is validated only when the endpoint field changes: scheme 0208 requires ten digits, scheme 0009 requires a valid French company number checksum, scheme 0007 requires ten digits, the email scheme requires a valid email address, and every other scheme requires 1 to 50 letters, digits or the characters hyphen, dot, underscore, tilde.
- [N-U34-022] Illegal characters are silently removed from the endpoint by scheme-specific cleaning rules before validation in the computed path.
- [N-U34-023] The delivery-location number has no format or length validation.

### RISK
- [N-U34-024] No Thai identifier scheme exists in the scheme list or in the country-to-scheme table, so a Thai company cannot obtain an automatically derived electronic address and no format is suggested for Thai partners; any Thai e-invoicing format would have to come from a separate pack.
- [N-U34-025] A leftover vestigial yes-or-no field for Peppol format is kept only for compatibility and hidden; it carries no behaviour.
- [N-U34-026] On uninstall the module clears six of the seven partner formats; the German ZUGFeRD value is not in the cleared list, so stored values of that format could remain on partners.

### UNKNOWN
- [N-U34-027] Runtime result of the scheme and endpoint recomputation for partners in the restored database cannot be shown: the seven partners hold no scheme, endpoint or location number.

## CAP-U34-02 E-invoice export pipeline, delivery and attachment handling

### WHAT
- [N-U34-028] An issued customer invoice or credit note can be turned into a structured XML file in one of the supported formats, either at send time (Send and Print) or on demand through an Export XML action.
- [N-U34-029] The generated file is stored as a hidden binary attachment of the invoice, offered as an attachment on sending, and downloadable later; the invoice PDF can be embedded into UBL-family files, and a Factur-X XML can be embedded into the PDF.
- [N-U34-030] Three builder families exist: a UBL generic skeleton (versions 2.0 and 2.1) whose steps are overridden by the Peppol BIS 3.0 builder, a CII builder for Factur-X and ZUGFeRD, and country builders layered on the BIS 3.0 builder.

### WHY
- [N-U34-031] Customers and tax authorities in e-invoicing countries require the invoice as structured data rather than only as a PDF; storing the generated file keeps what was sent identical to what is later downloaded.

### BUSINESS RULE
- [N-U34-032] An XML file is needed for a move when none is stored yet, the move is a customer document (or a posted vendor document in a buyer-issued invoicing journal whose partner format supports buyer-issued invoicing), and the chosen format is one of the electronic-invoice formats.
- [N-U34-033] Send and Print builds the XML before the PDF is rendered; if the builder reports rule violations the error list is shown with a title naming the format, but sending continues (fallback to the PDF alone); if it succeeds the file is attached to the invoice at the end of the send.
- [N-U34-034] On Export XML, the stored file is returned if present; otherwise, if the partner format needs it, the file is built on the fly (not stored) and any violations are returned alongside it.
- [N-U34-035] The Export XML entry is offered only for posted moves that either already have a stored file or could produce one.
- [N-U34-036] For UBL-family formats the invoice PDF, and extra attachments of supported types (PDF, spreadsheet, image, CSV) chosen on the send wizard, are embedded as base64 additional document references inserted at a fixed anchor position of the file; if no anchor element exists the embedding is skipped to avoid breaking the structure.
- [N-U34-037] Whatever the chosen format, whenever an invoice PDF is generated in the send flow a Factur-X XML is generated and embedded in the PDF as an alternative representation, unless the chosen format already is Factur-X or ZUGFeRD; any violations of that silent export are discarded.
- [N-U34-038] The PDF is converted to an archival PDF with extra metadata only when the format is Factur-X or ZUGFeRD, or when the customer is French or German without the German routing scheme, and the invoice company country is France or Germany; a conversion failure is logged and does not stop sending.
- [N-U34-039] Custom PDF templates listed in a system parameter also receive an embedded Factur-X when a single posted customer invoice is rendered.
- [N-U34-040] Document type is chosen from the move: debit note when the invoice originates from a debit note, credit note for refunds, else invoice; in the Peppol BIS 3.0 builder debit notes are exported as invoices and only invoice and credit note line structures are produced.
- [N-U34-041] For a vendor document exported as buyer-issued invoicing, supplier and customer are swapped so the company appears as buyer and the vendor as seller; buyer-issued invoicing is only supported by the Peppol BIS 3.0 builder family and not by the German XRechnung builder.
- [N-U34-042] Sections flagged to collapse their composition are exported as one summary line per tax group instead of their detailed lines.
- [N-U34-043] File names are format specific: a language-neutral invoice name with slashes replaced by underscores plus a format suffix, the German Factur-X variant being named as ZUGFeRD and the Belgian legacy format following its own naming convention.

### STATE
- [N-U34-044] Stored XML: absent -> present when a send succeeds; present -> detached when a customer invoice is reset to draft so it is regenerated; the file is never regenerated automatically while attached.
- [N-U34-045] Export outcome per attempt: error-free (file attached), violations (file not attached, send continues), exception (tax structure invalid, send aborted with a named error).

### OPTIONALITY
- [N-U34-046] A system parameter selects between the new node-building helpers (default on) and the legacy template rendering for the Factur-X builder; the parameter is not seeded in the restored database, so the default applies.
- [N-U34-047] A system parameter lists custom PDF templates that should carry a Factur-X; it is unset by default.
- [N-U34-048] Embedding of extra attachments applies only to formats flagged as supporting it, which is only the EU-wide Peppol format.
- [N-U34-049] The builder and format chosen during rendering are remembered for the PDF embedding step of the same send.

### DEPENDENCY
- [N-U34-050] The XML tree is rendered by a shared dictionary-to-XML helper of the accounting module using element-order templates held in the electronic-invoice module; amounts and tax groups come from the accounting tax engine.
- [N-U34-051] The Send and Print flow, its wizard, attachment lists and alerts belong to the accounting module and are extended here.
- [N-U34-052] A transport over the Peppol network is not part of this module; a separate module reads a context flag set by this module during export, and that module is not installed in the restored database.

### CONSTRAINT
- [N-U34-053] Before building, every tax used on the invoice lines must have a valid distribution structure; failure raises an error naming the tax and aborts the send.
- [N-U34-054] Generated XML attachments are created with elevated rights and linked to the move only after the whole send succeeds.

### RISK
- [N-U34-055] The always-on Factur-X embedding ignores export violations, so for a company with incomplete seller data (for example no phone, email or tax identifier) the embedded XML may be incomplete; and an invalid tax structure would raise even when no electronic format is configured.
- [N-U34-056] A replacement intended to mark the archival PDF metadata as level A is computed but its result is not used, so it has no effect.
- [N-U34-057] Because the generic UBL skeleton and the BIS 3.0 builder share an inheritance chain, the effective export procedure for BIS 3.0 and its country variants is the skeleton procedure that delegates each step to the newer node helpers; the newer standalone export procedure is shadowed in the installed set.

### UNKNOWN
- [N-U34-058] Real PDF rendering, archival PDF conversion and the wire format validity of the produced XML were not executed and require runtime testing.
- [N-U34-059] What happens to a stored XML when a posted vendor bill in a buyer-issued invoicing journal is reset or re-sent was not determined.

## CAP-U34-03 Export field mapping: parties, taxes, currency and amounts

### WHAT
- [N-U34-060] Export converts invoice data into standard elements: parties (seller, buyer, delivery), identifiers, payment instructions, line items with quantity unit codes, discounts and charges, tax category and exemption information per tax group, currency declarations, and monetary totals.

### WHY
- [N-U34-061] The receiving party must be able to recompute totals and verify tax categories from the file alone, so each amount, tax group and identifier has to follow a fixed mapping from accounting data.

### BUSINESS RULE
- [N-U34-062] Tax category code: the code stored on the tax is used if present. Otherwise: a missing tax is Exempt; Spanish customers with Canary Islands or Ceuta and Melilla postcodes get the matching regional codes; same-country zero taxes are Exempt, same-country taxes with negative factor are Reverse charge, other same-country taxes are Standard; across countries with an EEA party and a seller tax identifier a taxed line is Standard, zero tax is Intra-community when both parties are in the EEA and Export otherwise; with no EEA party, non-zero is Standard and zero is Exempt.
- [N-U34-063] Exemption reason: a Belgian co-contractant fiscal position yields a reverse-charge reason with its note; a reason code stored on the tax yields its standard text; otherwise Exempt gets a generic exempt text, Export gets the export reason code and Intra-community gets the intra-community supply reason code.
- [N-U34-064] A tax stores an optional category code from ten values (reverse charge, exempt, standard, zero rated, free export, outside scope, intra-community, Canary Islands, Ceuta and Melilla, transferred in Italy) and an optional exemption reason code from 91 values; a reason is requested only for reverse charge, exempt, free export, outside scope and intra-community.
- [N-U34-065] Taxes are reported per tax category, grouped by category code, rate and scheme; the scheme is VAT except when the seller country belongs to a list of GST countries; taxes with negative rate are reported as withholding.
- [N-U34-066] Fixed taxes that are part of the price base (recycling contributions) and code-computed taxes that are part of the base (excise) are not reported as taxes but as line-level charges or allowances; fixed taxes not included in the base are turned into additional invoice lines named after the tax.
- [N-U34-067] Reverse-charge taxes of vendor documents are reported as zero percent from the seller perspective when exporting buyer-issued invoicing documents.
- [N-U34-068] Category Outside scope is reported without a rate and requires that no other categories are mixed on the same document.
- [N-U34-069] Line discount becomes an allowance (or charge when negative) carrying the percentage, amount and base; early payment discount lines become document-level allowances or charges with fixed reason codes; global discount lines become document-level allowances; cash rounding lines are removed from the lines and reported as payable rounding amount.
- [N-U34-070] A negative unit price is flipped into a positive price with negative quantity because the standard forbids negative item prices.
- [N-U34-071] Currency: the document currency is the invoice currency; when it differs from the company currency the company currency is declared as the tax accounting currency and a second tax total is emitted in the company currency (without subtotals in the newer variants). Some regional formats declare no tax currency.
- [N-U34-072] Amounts: unit price is written with 1 to 10 decimals; line net amount is the rounded gross line amount adjusted by line charges and allowances; document totals are line sum, tax-exclusive (adding charges and subtracting allowances), tax-inclusive (adding tax totals, subtracting withholding), prepaid (total minus residual), payable (residual) and a rounding amount equal to the difference between expected and written tax-inclusive total.
- [N-U34-073] Withholding taxes are not allowed as separate totals in the Peppol international profile: their amount is moved into the prepaid amount and explained in the document note, and removed from the rounding amount.
- [N-U34-074] Unit of measure is mapped to a United Nations trade-facilitation code through a table of 28 standard units; any other unit is exported as the generic unit code.
- [N-U34-075] Items carry the seller product code, a barcode with the standard global trade item scheme, product attributes as additional properties, and customs, UN standard product or procurement classification codes only when the corresponding optional modules are installed.
- [N-U34-076] Parties: name falls back to the commercial partner name; address carries street, second street, city, postcode, state name and code, and country (the Peppol profile drops state code and country name); identifiers are the electronic address, Belgian registry number, or partner reference as fallback; tax registration is the tax identifier with country-specific prefix repairs; legal entity identifier follows country-specific rules with tax identifier then endpoint as fallback; contact carries name, phone and email.
- [N-U34-077] Delivery: delivery partner address, location number with the global location scheme when the location-number module is installed, and actual delivery date from the invoice delivery date; the Peppol profile keeps at most one delivery.
- [N-U34-078] Payment means: customer invoices with a bank account use code credit transfer, without bank account the code mutually-defined; other documents use standing agreement; Danish customers use the unknown code; payee account is the sanitized account number with a bank identifier only in the non-Peppol-international variants.
- [N-U34-079] Document references: invoice type code 380, buyer-issued invoice 389, credit note 381, buyer-issued credit note 261; order reference is the customer reference or the invoice name with the customer order names appended when sales is installed; buyer reference is the customer reference; credit notes reference the invoices they were matched against.
- [N-U34-080] CII mapping follows the same logic with its own elements: seller and buyer trade parties with French company registry detection, tax registration with scheme VA using the foreign fiscal position tax identifier when present, electronic address, payment means code bank transfer or direct debit when a mandate exists, tax breakdown, period from invoice date to due date or deferral dates, payment terms with early discount, and a monetary summation with two-decimal amounts.
- [N-U34-081] Document currency of a CII file is the invoice currency, and prepaid amount is grand total minus residual; type code is 380 for customer invoices and 381 for any other document type.

### STATE
- [N-U34-082] Mapping is stateless: it is computed from the move at the time of export; a posted move is not required for the on-demand export of the in-memory file, but the menu entry is only offered for posted moves.

### OPTIONALITY
- [N-U34-083] Tax category and exemption codes are optional per tax; defaults are inferred from country relations, so a company with only unclassified taxes still obtains a category for every line.
- [N-U34-084] Optional fields prefixed for external form builders can inject extra elements (tax point date, contract reference, accounting cost, project reference, order reference, period, line order reference, buyer item id) when such fields exist on the move or line; they are read only by name.

### DEPENDENCY
- [N-U34-085] Tax grouping, rounding, discount extraction and totals come from the accounting tax engine; details of those hooks are in the tax-hooks study and are not repeated here.
- [N-U34-086] Unit-of-measure external identifiers, customer reference, company registry, fiscal position and payment term early-discount data are read from base and accounting data.

### CONSTRAINT
- [N-U34-087] Each exported tax group must have a category; a line without any tax receives the Exempt default group; exempt groups receive a default exemption text when none exists.

### RISK
- [N-U34-088] The default category inference embeds European rules (EEA membership, Intra-community and Export meanings, Canary Islands postcodes); a zero-rate Thai sale tax with no stored code would be reported as Exempt, and the GST country list does not contain Thailand so the scheme would be VAT.
- [N-U34-089] Reason codes for recycling contributions are chosen by whether the tax name contains a Belgian waste-scheme word, a name-based heuristic.
- [N-U34-090] The CII line import rounds a recomputed unit price to two decimals, whereas the UBL line import does not, so an identical document may round differently by format.
- [N-U34-091] Country-specific rules (Belgian, Dutch, Danish, Norwegian, Swedish, Spanish, Hungarian, Swiss, French) sit inside the shared builders; they are optional-country-pack material and were recorded only as an extension boundary.

### UNKNOWN
- [N-U34-092] Whether a Thai company can produce a standards-valid file with this module (tax categories, seller electronic address, buyer references) requires runtime testing and a statutory register entry; no Thai rule was derived from this source.

## CAP-U34-04 Export validation constraints and failure reporting

### WHAT
- [N-U34-093] Before a file is produced the exporter checks the invoice data against format rules (European core invoice model, Peppol profile, Peppol international profile, Factur-X and German public-sector rules) and returns a list of readable messages; the file is still produced.

### WHY
- [N-U34-094] Rule violations are detected before sending so that the user can fix partner, product or company data instead of a receiving system rejecting the file.

### BUSINESS RULE
- [N-U34-095] Every product line that requires a tax must carry at least one tax; combo products are exempt from this check.
- [N-U34-096] UBL generic rules: supplier name, customer commercial partner name, invoice number and invoice date are required.
- [N-U34-097] European core model rules: each line has an item name; each line has exactly one tax category; category Outside scope is not mixed with other categories; seller and buyer need a country; a tax identifier of VAT scheme needs an alphabetic country prefix; a delivery address needs a country; payment by credit transfer needs a bank account on the invoice.
- [N-U34-098] For intra-community supply (customer and supplier in different EU member states) the delivery address must be included and the actual delivery date or an invoicing period must be present.
- [N-U34-099] Peppol international profile rules: issue date, currency, seller name and country, seller and buyer electronic address with scheme, at least one line, per line quantity, unit code, net amount, item name, price (never negative) and tax category, and for every allowance or charge an amount and a reason or reason code.
- [N-U34-100] A buyer reference or purchase order reference must be provided in the Peppol EU profile.
- [N-U34-101] Factur-X rules: customer invoices need a recipient bank account with account number, a seller country, a seller tax identifier, seller phone and email, a tax on each line, a buyer country, buyer and seller tax identifiers for intra-community supply, and a positive rate when the Canary Islands tax applies.
- [N-U34-102] German public-sector profile additionally requires seller phone and email; the Peppol builder adds national rules for Norwegian suppliers (tax identifier format) and Belgian parties (valid registry number); the Peppol EU layer adds Dutch rules (address parts, legal entity identifier, payment means, credit note reference).

### STATE
- [N-U34-103] Each message is keyed; the result is a set of distinct texts, empty when everything passes. Messages do not change document state.

### OPTIONALITY
- [N-U34-104] Which rule set applies depends on the format selected for the partner; the Factur-X rules also apply to the silent Factur-X built for every PDF, but there the result is ignored.

### DEPENDENCY
- [N-U34-105] Rule checks read the node tree already built, so they depend on the mapping rules; some read invoice, partner, bank and company fields directly.

### CONSTRAINT
- [N-U34-106] A missing field is reported with the field label and record name; for node trees the message states the missing element.
- [N-U34-107] The partner electronic-address validation raises an error at save time, unlike export rules which only return messages.

### RISK
- [N-U34-108] For Factur-X, a company without phone, email or tax identifier always produces violations, regardless of country, because those rules come from the German profile; a company outside the format countries that selects Factur-X would be blocked from a clean file.
- [N-U34-109] The rule requiring a buyer or order reference tests whether a dictionary of the element exists, and the dictionary always exists, so the rule can never fire; this was concluded from source only.
- [N-U34-110] Constraint messages mix technical rule codes and English text; they are returned untranslated into the wizard and are not stored.

### UNKNOWN
- [N-U34-111] Whether the rule texts, ordering and quantity of messages shown to a Thai user are acceptable cannot be determined without runtime execution.

## CAP-U34-05 E-invoice import: detection, decoding, retrieval and corrections

### WHAT
- [N-U34-112] An uploaded or mailed file is recognised as an electronic invoice (UBL, Peppol BIS 3.0 and regional variants, UBL attached-document wrapper, CII or Factur-X) and decoded into a draft vendor bill or customer invoice with partner, dates, currency, bank, references, lines, taxes, discounts, notes and attachments.
- [N-U34-113] Two decoding generations coexist: a newer staged procedure for Peppol BIS 3.0 family and CII, and an older direct procedure for plain UBL 2.0 and 2.1 and the Belgian legacy format.
- [N-U34-114] The user can switch an imported draft invoice between detailed lines and one line per tax group.

### WHY
- [N-U34-115] Vendors send invoices as structured data; importing avoids manual typing and keeps the original XML with the bill.

### BUSINESS RULE
- [N-U34-116] File type detection: a wrapper root element is unwrapped; the CII root element is CII; the customization identifier selects XRechnung, Dutch, A-NZ, Singapore or Peppol BIS 3.0; otherwise the UBL version identifier selects UBL 2.0 or 2.1; any identifier containing the European core model marker is BIS 3.0; unrecognised files are left to other decoders.
- [N-U34-117] A recognised file receives decoder priority 20; among all files of an upload the highest priority decoder is used; with no decoder (or priority zero) the file is ignored with a log line; a decoder that returns a reason posts that reason in the chatter and stops.
- [N-U34-118] The wrapper format embeds the real document as base64 or as text; the embedded document is typed and decoded in its place.
- [N-U34-119] An invoice that already contains lines cannot be decoded into; the document sign follows the root element or the type code; an invoice with a negative total is turned into a credit note and quantities are reversed; the bill type direction (customer or vendor) comes from the journal type.
- [N-U34-120] Partner lookup order for the newer path: tax identifier, electronic address, bank account number (UBL only), email, phone, name; a missing partner is created only if both name and tax identifier are present, with company flag, contact data, address, country, electronic address and a tax identifier that is validated and blanked if invalid; an existing partner without a tax identifier receives the file value; an existing partner with a different tax identifier causes a new partner to be created.
- [N-U34-121] Currency: the code is searched including inactive currencies; an unknown or inactive currency is logged and, when unknown, the company currency is used; the conversion rate at the invoice date is captured.
- [N-U34-122] Bank accounts in the payment means are found or created for the counterpart partner (the vendor for vendor bills, the company for customer invoices); failures are logged; the first bank becomes the invoice bank.
- [N-U34-123] Products are searched with the partner search plan (barcode, internal reference, vendor catalogue, name) and then by prediction from history; a unit code is matched to a unit of measure but ignored with a log message if the unit is not compatible with the product unit.
- [N-U34-124] Taxes are found, never created: tax values are built from the document tax subtotals (rate, category code) and charges classified as fixed taxes; the search plan is default tax of the account, prediction, tax price-included flag with fiscal position, and a fuzzy fixed-tax match within one cent; the stored category code on the tax is preferred in the order of matches; unmatched taxes are logged.
- [N-U34-125] Line price, quantity and discount are derived from the line net amount, the net price, price base quantity, price-level allowance and line-level allowances and charges, following the documented combinations for the three cases of present or missing invoiced quantity; charges are added to the unit price and allowances become a percentage discount.
- [N-U34-126] Document-level allowances and charges become extra lines with their tax; lines with zero total and no discount are dropped; price-included taxes adjust the unit price.
- [N-U34-127] After writing the lines, tax amounts are compared with the document tax subtotals; if all taxes were found and the difference of total tax is within 0.03 the tax amounts are redistributed across the lines; then any remaining untaxed difference with the document tax-exclusive total is added as a rounding line without tax.
- [N-U34-128] A prepaid amount in the file is only reported in the log, not turned into a payment.
- [N-U34-129] References imported: document number (as the invoice name for customer invoices in quick-edit mode, else as the vendor reference), order reference or a purchase order name pattern found in item descriptions, notes and payment terms as narration, payment reference, delivery date, a single delivery-terms code matched to an incoterm, due date; optional external-form fields only for vendor bills.
- [N-U34-130] Embedded PDF or other supported documents in the XML are attached to the bill; if none exists and the bill is a vendor bill a substitute PDF labelled as generated is rendered unless disabled by a system parameter; the source XML is bound to the bill field for vendor bills.
- [N-U34-131] Grouping by tax: allowed only on draft invoices; lines are summed per tax and account and named after partner, account code and tax names; ungrouping replays the stored source file; after an automatic import, if the latest posted bill of the same vendor was grouped, the new bill is grouped too.

### STATE
- [N-U34-132] Document: draft (created or extended by import) -> draft with lines and a log message; import never posts. File data: typed -> unwrapped -> decoder chosen -> decoded or rejected with a message.
- [N-U34-133] Move type may change between invoice and credit note (same direction) during decoding.

### OPTIONALITY
- [N-U34-134] Account prediction and deferral dates are used only when the enterprise accounting extension is installed; in this Community set they are skipped.
- [N-U34-135] Product classification codes, order imports and the optional external-form fields are read only when matching fields or modules exist.
- [N-U34-136] The substitute PDF can be disabled with one system parameter, seeded as false.

### DEPENDENCY
- [N-U34-137] Dispatch, grouping of attachments, priority sorting, transaction protection and error posting belong to the shared document import layer of accounting; partner, product and tax search plans belong to accounting and product modules and are only called here.
- [N-U34-138] The import of sales and purchase orders reuses the Peppol BIS 3.0 builder in separate modules; they were only noted.

### CONSTRAINT
- [N-U34-139] The import runs inside a protected transaction: the cursor is committed before and after; any error rolls back and posts the error text on the document; a validation error never leaves a half-filled bill.
- [N-U34-140] Vendor bills receive the source XML as a bound attachment; customer invoices do not.

### RISK
- [N-U34-141] The wrapper parser returns a variable that is only assigned inside a branch; an unusual wrapper without the expected binary element would raise an error before the protected transaction starts.
- [N-U34-142] The older direct import corrects tax totals without any tolerance although its comment mentions a five-cent limit, whereas the newer path uses 0.03.
- [N-U34-143] Partner creation can create many duplicate partners if the file tax identifier differs in format from the stored one in ways the comparison does not normalise (only Swiss identifiers are normalised).
- [N-U34-144] The XML tree is parsed with entity resolution disabled in the shared layer but external embedded documents are accepted up to their declared type only; no size limit exists in this module.

### UNKNOWN
- [N-U34-145] Whether a vendor XML from a Thai vendor can be imported without error (tax identifier, currency THB and tax mapping) requires a runtime test; no Thai sample was available.
- [N-U34-146] The enterprise-only account prediction and deferral date functions were not read.

## CAP-U34-06 Regional format boundary and dependent modules

### WHAT
- [N-U34-147] Beyond the generic Peppol and CII builders the module contains named regional builders for Germany (XRechnung), the Netherlands (NLCIUS), Singapore, Australia and New Zealand, and a Belgian legacy format; country-specific rules also sit inside shared builders.
- [N-U34-148] Other installed modules extend this module: a deprecated module of optional Peppol fields, and two order modules that import sales orders and export purchase orders in the Peppol order format using the same builder.

### WHY
- [N-U34-149] Each country mandates its own variant of the European standard; recording where the generic code ends and the country code begins shows what a Thai pack must replace or add.

### BUSINESS RULE
- [N-U34-150] Regional builders override only their identifiers, file names, tax currency handling, party identifiers, payment means and a few rules; the common mapping is inherited from the Peppol BIS 3.0 builder.
- [N-U34-151] Country packs add formats by extending the partner format list and the format information dictionary and by overriding the builder selection; the generic module has one builder per format key except that Factur-X and ZUGFeRD share one.

### STATE
- None recorded.

### OPTIONALITY
- [N-U34-152] All regional builders are optional in practice: none is selected unless the partner is in the country or a format is set manually; the Belgian legacy format has no selection entry at all.

### DEPENDENCY
- [N-U34-153] Forty-five modules in the source tree depend on this module; in the restored database only three installed modules do (two order modules and the deprecated optional fields module); the Peppol network transport module is not installed.
- [N-U34-154] Order modules inherit the BIS 3.0 builder; sales order import posts an activity on the order listing what could not be imported.

### CONSTRAINT
- None recorded.

### RISK
- [N-U34-155] The Belgian legacy format builder is never detected on import because no detection rule returns it, so files of that format are decoded as plain UBL.
- [N-U34-156] Country rules in the shared builders (Belgian co-contractant note and registry numbers, Dutch KvK, Danish payment code, Norwegian and Swedish tax statements, Hungarian and Danish tax prefix, Spanish regional codes, Swiss tax identifier normalisation, French company number schemes) cannot be removed without changing generic output and are country pack material.
- [N-U34-157] The deprecated module defines fields with other names than the ones the export reads, so those fields are never exported.

### UNKNOWN
- [N-U34-158] Rules inside the regional builders were not studied; only their existence and extension points are recorded.

## CAP-U34-07 Fleet vendor-bill bridge

### WHAT
- [N-U34-159] A vendor bill line can name the vehicle it relates to; when the bill is posted for the first time a fleet service log is created for each such line, and the vehicle shows the number of bills and links to them.
- [N-U34-160] The cost of a service log created from a bill is the debit of the bill line and is read-only on the log; the log shows a button to open the bill.

### WHY
- [N-U34-161] Vehicle running costs recorded as vendor bills should appear in the fleet service history without being typed twice.

### BUSINESS RULE
- [N-U34-162] After posting, only product lines of vendor invoices (not refunds or receipts) that have a vehicle and no existing log produce a log; the log copies service type, vehicle, vendor, line description and the link to the bill line and receives a message pointing to the bill.
- [N-U34-163] If the seeded service type for vendor bills has been deleted, posting creates no logs.
- [N-U34-164] Removing the vehicle from a bill line, or deleting the line, deletes the linked logs; deleting a log that came from a bill is blocked unless done through the bill line.
- [N-U34-165] The cost of a log linked to a bill line cannot be edited; it follows the debit of the line.
- [N-U34-166] The vehicle on a log follows the vehicle of its bill line and cannot be emptied by that link; period-change entries made by the automatic entry wizard keep the vehicle on the line that stays on the original account.
- [N-U34-167] The vehicle bill count and list include purchase-type moves that are not cancelled and are visible only to users with read access to accounting.

### STATE
- [N-U34-168] Log: created at first posting of the bill; shows posted or not posted state of its bill; deleted with the bill line or when the vehicle is cleared. Bill reset to draft or reversed: behaviour not determined.

### OPTIONALITY
- [N-U34-169] The module installs automatically when fleet and accounting are installed; the vehicle column on bill lines is hidden by default and visible only on vendor documents; a vehicle is never mandatory because the hook that would require it is always false.

### DEPENDENCY
- [N-U34-170] Needs fleet and accounting; extends the move posting method, move line, vehicle, service log and the automatic entry wizard.
- [N-U34-171] Log creation runs with the permissions of the user who posts; the fleet log table grants read to fleet officers and full access to fleet administrators only.

### CONSTRAINT
- [N-U34-172] Cost of a bill-linked log cannot be written directly; the log cannot be deleted while linked to a bill line except through the line.

### RISK
- [N-U34-173] An accountant who has no fleet permissions and posts a bill with vehicle lines may be refused because the log creation is not elevated; this was inferred from source and the permission file.
- [N-U34-174] Multi-company behaviour of logs was not studied; the log has no company field in this module.

### UNKNOWN
- [N-U34-175] No vehicle exists in the restored database; the effect of reset-to-draft, reversal and re-posting on logs, and the multi-company effect, are unknown.

## CAP-U34-08 Runtime API documentation service

### WHAT
- [N-U34-176] A built-in technical documentation service lists installed modules, readable data models, their readable fields and public methods, and gives per-model details with method signatures and parameter text, for developers writing integrations.
- [N-U34-177] It is served as a single-page application at the documentation address plus JSON data endpoints, with session login or with a bearer key.

### WHY
- [N-U34-178] Integrators need an up-to-date description of what the installed system exposes; generating it from the live registry keeps the description exact for the installed set of modules.

### BUSINESS RULE
- [N-U34-179] Every documentation route checks that the caller belongs to the Technical Documentation group; the group is implied by the system administrator group and its only direct member in the restored database is the superuser account.
- [N-U34-180] The index lists only models the caller can read and only fields with read access; per-model details require read access to the model and return not found for unknown models.
- [N-U34-181] Methods listed are public methods that are not deprecated; each method is attributed to the model and module that introduced it, with signature, parameters, return annotation and text parsed from its docstring in a restricted markup mode (raw content and file insertion disabled).
- [N-U34-182] Responses are cached: the index per caller is stored as a private attachment whose name embeds the registry change sequence and a keyed hash of language and group set; older cached indexes are deleted by the periodic cleanup; per-model responses use an entity tag and may return not modified; a client asking for no cache gets a fresh document with no-store.
- [N-U34-183] The page forbids framing and the bearer routes accept the same checks as session routes.

### STATE
- [N-U34-184] Cached index: absent -> stored on first request per sequence, language and group set -> deleted when the registry sequence moves on.

### OPTIONALITY
- [N-U34-185] The module installs automatically with the web layer and belongs to the hidden category; nothing is configured; no scheduled job of its own exists, only an autovacuum hook.

### DEPENDENCY
- [N-U34-186] Depends only on the web layer; uses the module dependency graph for ordering, the registry sequence for cache validity and an external documentation parser library.

### CONSTRAINT
- [N-U34-187] Caller must be in the group; the message names the group on refusal.

### RISK
- [N-U34-188] The service exposes the full technical surface (all readable models, fields and public methods with module names) to every member of the group, including bearer-key callers; only administrators and the superuser hold the group by default.
- [N-U34-189] Cached index files can be large and accumulate per language and per group set until the next registry change.

### UNKNOWN
- [N-U34-190] Client-side scripts and styles of the documentation page were not read; behaviour of the playground that executes methods over the network is runtime only.

## CAP-U34-09 Attachment text indexation

### WHAT
- [N-U34-191] When a file is stored as an attachment, its text can be extracted for search from word-processing, presentation, spreadsheet, open-document and PDF files.

### WHY
- [N-U34-192] Searching attachment contents lets users find documents by what they contain.

### BUSINESS RULE
- [N-U34-193] Extraction tries Word, PowerPoint, Excel, OpenDocument and PDF in that order and uses the first non-empty text, else falls back to the base behaviour for plain text types; empty results store no index.
- [N-U34-194] Spreadsheet content is turned into comma-separated rows prefixed by the sheet name; empty rows are skipped; OpenDocument repeat counts are capped at 100 columns and 50 rows.
- [N-U34-195] PDF text is extracted only if the content starts with the PDF signature and the optional PDF library is installed; whitespace and control characters are normalised; failures return empty text.
- [N-U34-196] Extracted text is cached by checksum in a one-entry cache; copying an attachment primes the cache with the existing index.

### STATE
- [N-U34-197] Index text is stored with the attachment when content is written; no state machine.

### OPTIONALITY
- [N-U34-198] The module is not auto-installed; PDF indexing needs an optional library (a warning is logged at load if missing) and spreadsheet indexing needs another optional library (silently skipped).

### DEPENDENCY
- [N-U34-199] Extends the base attachment index hook; depends on the web layer; one other installed module (recruitment) depends on it.

### CONSTRAINT
- [N-U34-200] Parsing errors are swallowed in every extractor; no size, time or memory limit is applied by this module.

### RISK
- [N-U34-201] Uploaded documents are parsed on the server without size or time limits and the OpenDocument parser uses the default XML parser settings; hostile files could consume memory or time (inferred, not tested).
- [N-U34-202] The extractors guess the format by trying all of them in order on every file, not by content type.

### UNKNOWN
- [N-U34-203] Real indexing results, performance and the effect of the one-entry cache under concurrent uploads need runtime tests; only one PDF test exists.
