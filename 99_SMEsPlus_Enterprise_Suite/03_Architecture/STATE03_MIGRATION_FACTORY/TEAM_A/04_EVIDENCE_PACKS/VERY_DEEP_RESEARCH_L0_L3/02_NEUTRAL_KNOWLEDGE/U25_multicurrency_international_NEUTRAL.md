# U25 Multi-currency and International Transactions — Neutral Knowledge (clean-room layer)

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
> Baseline: Odoo 19 Community (named once, here only)
> Scope: cross-cutting capability study — currencies and rates, foreign-currency documents, accounting entries and settlement, foreign partners and tax treatment, international trade documents, reporting, multi-company currency interplay, roles and failure behaviour. Foreign-country accounting localization is out of scope; Thailand localization is in scope.
> Each statement is tagged with an id that links to technical claims held in the restricted layer.
> Statements describe what the system must do and why; no implementation names appear here.

## CAP-U25-01 Currency catalogue and exchange-rate model

### WHAT
- [N-U25-001] The system keeps a catalogue of currencies, each with a three-letter code, a symbol, a symbol position (before or after the amount), an active flag and a rounding unit from which the number of decimal places is derived.
- [N-U25-002] Exchange rates are dated records attached to a currency and, optionally, to a top-level company; a rate with no company is shared by every company.
- [N-U25-003] Each stored rate is expressed against an implicit reference currency; screens present it both as units of the foreign currency per one unit of company currency and as the inverse, and editing either presentation updates the other.
- [N-U25-004] A single conversion service turns an amount in one currency into another for a given company and date and rounds the result to the target currency's unit unless it is asked not to.
- [N-U25-005] The delivered Community source provides no automatic rate download: the accounting settings page carries only an upgrade-style switch for automatic rates, and no module implementing it exists in the source set or in the module list of the restored database.

### WHY
- [N-U25-006] Dated rates let every document be valued at the rate of the relevant business day while the history of earlier rates is kept.
- [N-U25-007] One rounding unit per currency keeps comparisons and zero tests consistent across all functions that handle amounts.

### BUSINESS RULE
- [N-U25-008] Currency codes must be unique and the rounding unit must be greater than zero.
- [N-U25-009] A rate must be strictly positive, and only one rate per currency, day and company is allowed.
- [N-U25-010] For a requested date the system uses the most recent rate dated on or before that date; if there is none it uses the earliest later rate; if the currency has no rate at all the rate is silently taken as one.
- [N-U25-011] When both a company-specific rate and a shared rate exist, the company-specific rate is ranked first before dates are compared, so an older company rate can win over a newer shared rate.
- [N-U25-012] Conversion between two currencies uses the ratio of their two rates; converting a currency into itself uses exactly one; converting an amount of zero returns zero.
- [N-U25-013] Rates are held only at the top-level company; branches resolve rates through their root, and a rate cannot be created against a branch.
- [N-U25-014] Entering a rate that differs from the previous rate by more than twenty percent shows a warning on the form but does not block saving.
- [N-U25-015] Amount comparisons and zero tests round to the currency's unit first, so differences smaller than the unit are treated as equal.

### STATE
- [N-U25-016] A currency moves from active to archived by editing it; the change is refused while any company uses the currency as its own.
- [N-U25-017] When the number of active currencies rises above one, the multi-currency capability is switched on for all internal users automatically; when it falls to one or none, it is switched off again.
- [N-U25-018] A rate stays in force until a newer-dated rate for the same currency and company supersedes it for later dates; earlier dates keep using the older rate.
- [N-U25-213] Switching on multi-currency also switches on the price-list feature and creates default price lists, and archiving a currency archives the price lists that use it.

### OPTIONALITY
- [N-U25-019] Rates are optional. With no rates every conversion is one to one; the delivered configuration has two active currencies and no rate at all.
- [N-U25-020] The multi-currency capability only controls what screens show (currency fields, rate fields, foreign-currency columns); the underlying conversion logic is always available.
- [N-U25-021] Choosing a company country can pre-select that country's currency, and saving a company whose currency is inactive re-activates that currency.

### DEPENDENCY
- [N-U25-022] Currencies and rates are maintained from the accounting configuration menu, so the accounting application must be installed to reach them from the menus.
- [N-U25-023] The same rate lookup is reused by sales, purchasing, delivery, expenses, payments, reporting and spreadsheet functions rather than reimplemented in each.

### CONSTRAINT
- [N-U25-024] The number of decimal places of a currency cannot be reduced once the currency has been used on accounting entries.
- [N-U25-025] A branch company must have the same currency as its root company; the value is copied when the branch is created and pushed to all branches when the root changes.
- [N-U25-026] The currency of a company cannot be changed once accounting entries exist.

### RISK
- [N-U25-027] The silent one-to-one fallback means a missing rate produces plausible but wrong foreign amounts with no error and no warning.
- [N-U25-028] A helper meant to default a new rate to the previous rate is defined but not attached to any field, so new rates are not pre-filled from earlier ones.
- [N-U25-029] Uniqueness of shared rates is enforced by a database rule that may not treat two rows without a company as duplicates.
- [N-U25-030] Rate fields carry no fixed rounding while list screens display up to twelve decimals, so displayed and stored precision can differ.

### UNKNOWN
- [N-U25-031] The numeric results of conversion, and the precedence of company rates over shared rates, need execution to confirm.
- [N-U25-032] Whether any scheduled or external rate feed exists outside the delivered source set cannot be determined from the source.

## CAP-U25-02 Document currency and rate dates on orders, invoices and payments

### WHAT
- [N-U25-033] A sales order takes its currency from its price list, which comes from the customer's country-group or explicit choice and otherwise from the first available price list; with no price list the company currency applies.
- [N-U25-034] A purchase order takes its currency from a per-company supplier-currency setting on the vendor and otherwise from the company currency; the currency stays editable while the order is a draft.
- [N-U25-035] A customer invoice or vendor bill created from an order carries the order's currency; a manually created one takes the journal's currency, then any existing document currency, then the company currency.
- [N-U25-036] A payment takes its currency from the journal chosen; the register-payment dialog takes the journal currency, otherwise the currency of the invoice being paid, otherwise the company currency.
- [N-U25-037] Sales and purchase orders store a read-only rate from company currency to document currency computed at the order date, and a purchase order also stores its total in company currency.
- [N-U25-038] Customer invoices and vendor bills store an editable rate from company currency to document currency; each journal item stores both its amount in document currency and its balance in company currency.

### WHY
- [N-U25-039] Keeping both amounts lets the books stay in company currency while documents are issued and settled in the partner's currency.

### BUSINESS RULE
- [N-U25-040] A sales order's rate date is its order date; changing the order date recomputes the stored rate, and confirming the order resets the order date to the moment of confirmation, so the stored rate follows the confirmation time.
- [N-U25-041] A purchase order's rate date is its order deadline date, which the user can edit and which confirmation does not change.
- [N-U25-042] Sales order lines are priced at the order date in the order currency; price-list rules convert list prices and cost-based prices at that date, while fixed prices and surcharges on a rule are taken as already being in the price-list currency and are not converted.
- [N-U25-043] A vendor price in a currency different from the order's is converted at the order date when a purchase line is built, but the quick-add catalog path converts at the current day.
- [N-U25-044] An invoice created from an order carries the order's currency but computes its own rate afresh at the invoice date; the order's rate is not copied.
- [N-U25-045] The invoice rate date is the invoice date, or today while the date is empty; a customer invoice posted without a date receives today's date and its rate is recomputed unless the user entered the rate manually; a vendor bill cannot be posted without a date.
- [N-U25-046] The invoice rate can be edited by hand only while the invoice is a draft, and a refresh action resets it to the date-derived rate.
- [N-U25-047] On any invoice in a foreign currency the rate must be strictly positive.
- [N-U25-048] A vendor bill created from a purchase order converts each line's unit price from the order currency to the bill currency only if they differ, at the bill's date or the current day when no date exists.
- [N-U25-049] The unit cost of a purchase receipt is the order price converted to company currency at the order date; an unbilled receipt valued later is converted at the receipt's own date; a billed receipt is valued from the bill's company-currency amount.
- [N-U25-050] Delivery charges are computed in company currency and converted to the order currency at the order date; the free-shipping threshold is expressed in company currency.
- [N-U25-051] The cost used for margin on a sales line is converted to the order currency at the order date.
- [N-U25-052] A customer credit-limit warning converts the order total back to company currency with the order's stored rate; the credit limit is held in company currency.
- [N-U25-053] An employee expense in a foreign currency stores a rate in the opposite direction to invoices (company units per one foreign unit), defaulted at the expense date and overridable by editing the company-currency total.

### STATE
- [N-U25-054] A draft invoice follows currency and date changes with a recomputed rate until the user overrides the rate; once posted the rate and amounts are frozen.
- [N-U25-055] A sales quotation becomes a confirmed order and, at that moment, its stored rate is recomputed for the confirmation date.

### OPTIONALITY
- [N-U25-056] The price-list feature is a switch; in the delivered configuration it is on for all internal users and there is a single default price list in company currency, so every customer currently resolves to the company currency.
- [N-U25-057] The vendor's supplier-currency setting is optional; without it purchases are in company currency.
- [N-U25-058] Orders offer no manual rate; only invoices and bills allow a manual rate.

### DEPENDENCY
- [N-U25-059] Inventory valuation of purchased goods depends on three different rates: the order date rate at receipt, the receipt date rate when unbilled, and the bill rate once billed.

### CONSTRAINT
- [N-U25-060] The price list of a confirmed sales order cannot be changed.
- [N-U25-061] A document whose currency is inactive cannot be posted.
- [N-U25-062] Invoices created from orders are grouped by company, partner, delivery address, currency and fiscal position, so orders in different currencies always yield separate invoices.

### RISK
- [N-U25-063] Because the invoice rate is not inherited from the order, the company-currency value of an invoice can differ from that of its order, and a vendor bill can differ from the receipt valuation, whenever rates moved.
- [N-U25-064] Because confirming a sales order rewrites its order date, reports based on the stored order rate show the rate at confirmation rather than at quotation.
- [N-U25-065] Different paths convert at different dates (order date, current day, receipt date, bill date); the resulting rounding and valuation differences need execution to quantify.

### UNKNOWN
- [N-U25-066] Numeric outcomes of each conversion path with real rates are not determinable without execution.

## CAP-U25-03 Foreign-currency accounting entries, reconciliation and exchange differences

### WHAT
- [N-U25-067] Every journal item stores a balance in company currency, an amount in its own currency and that currency; for invoices the item currency equals the document currency and the two amounts are related by the document rate.
- [N-U25-068] When items in different currencies are matched, the system works in the foreign currency where possible, creating partial matches that record amounts in both currencies.
- [N-U25-069] When the company-currency amounts of matched items differ, the system generates an exchange-difference entry in the company's exchange journal, with a gain or loss line on the company's configured exchange accounts.

### WHY
- [N-U25-070] Receivables and payables stay correct in both currencies even when the rate moved between invoice and settlement, and the movement is surfaced as a realized gain or loss.

### BUSINESS RULE
- [N-U25-071] The company-currency amount and the document-currency amount of one item must have the same sign.
- [N-U25-072] Tax is computed in document currency first; each base and tax amount is divided by the document rate and rounded to company currency, with rounding per line or globally according to the company setting; an option shows taxes in company currency on foreign-currency documents.
- [N-U25-073] A gain is posted to the income account configured on the company and a loss to the expense account, chosen by the sign of the difference.
- [N-U25-074] The exchange entry is dated at the later of the matched items' dates, moved forward when that date falls in a locked period, created as a draft and posted only when both matched items are posted.
- [N-U25-075] Differences that come only from rounding are suppressed: the system tests amounts widened by half a rounding unit before deciding a difference exists.
- [N-U25-076] In foreign-currency matching, the leftover company-currency amount of an item that becomes fully matched turns into an exchange difference; for an item matched only in part, a difference is generated only when needed to keep the item's remaining company-currency amount consistent with its own rate.
- [N-U25-077] Removing a match reverses the exchange entry linked to it, or deletes that entry if it is still a draft; the reversal date is moved after any lock.
- [N-U25-078] An account can be forced to one foreign currency, and items of any other currency are then refused on it; a journal in a foreign currency forces its liquidity account to the same currency.
- [N-U25-079] Analytic amounts are always derived from the company-currency balance.

### STATE
- [N-U25-080] An item moves from open to partially matched to fully matched; the exchange entry moves from draft to posted when its matched items are posted.
- [N-U25-081] A full match across several currencies is detected when the company-currency residual of every item is zero.

### OPTIONALITY
- [N-U25-082] The exchange journal and both exchange accounts must be configured per company; the chart loader seeds the journal, and the Thai chart seeds both accounts; the settings are shown only when multi-currency is on.
- [N-U25-083] Showing taxes in company currency on documents is a company setting that is on by default.

### DEPENDENCY
- [N-U25-084] Cash-basis tax entries and early-payment-discount entries are generated alongside matches and use the same exchange accounts.

### CONSTRAINT
- [N-U25-085] Creating an exchange entry without the exchange journal, the gain account or the loss account configured is refused with a message naming the missing setting.
- [N-U25-086] Every posted entry must balance in company currency to the currency's decimal places.
- [N-U25-087] The company currency cannot change after entries exist, and an account cannot be given a currency while items in a different currency already exist on it.

### RISK
- [N-U25-088] With no rates, foreign-currency documents and payments are valued one to one, so no exchange difference arises although balances are wrong.
- [N-U25-089] Exchange entries dated into the open period after a lock may land in a later period than the documents they correct.
- [N-U25-090] Rounding tolerance for partial matches in foreign currency needs execution to confirm.

### UNKNOWN
- [N-U25-091] The size and sign of exchange differences in specific partial-payment sequences cannot be derived without execution.

## CAP-U25-04 Foreign-currency payments, bank statements and write-offs

### WHAT
- [N-U25-092] When paying invoices, the system prefers a bank or cash journal whose currency equals the invoice currency, then one matching the partner bank account, and otherwise any available journal.
- [N-U25-093] Payments are grouped by partner, account, currency and bank account, so invoices in different currencies are never combined in one payment.
- [N-U25-094] A payment records its liquidity item in the payment currency and the company-currency value at the payment date.
- [N-U25-095] A bank statement line carries an amount in the journal currency and may carry an amount in a different foreign currency.

### WHY
- [N-U25-096] Paying in the currency of the invoice or of the bank account avoids unnecessary conversions and leaves only the true rate movement as a gain or loss.

### BUSINESS RULE
- [N-U25-097] The foreign currency on a statement line must differ from the journal currency, an amount requires a currency and a currency requires an amount.
- [N-U25-098] A statement line whose journal is in a foreign currency is converted to company currency at the statement date; a foreign amount with none entered is derived by conversion at that date.
- [N-U25-099] When a user settles a difference with a write-off account that is one of the two exchange accounts, the difference is treated as an exchange difference with the rate forced; with any other account the write-off is converted at the payment date.
- [N-U25-100] The amount offered in the payment dialog is converted to the dialog currency at the payment date when the payment currency differs from the invoice currency.
- [N-U25-101] An early-payment discount settled in a foreign currency books any leftover rate difference to the exchange accounts under a dedicated label.
- [N-U25-102] When a payment carries withholding lines, any write-off lines on the same payment are dropped; the two are not supported together.

### STATE
- [N-U25-103] A payment is matched when its liquidity item is settled and reconciled when its receivable or payable item is settled, each tested in the payment currency when it differs from company currency.

### OPTIONALITY
- [N-U25-104] The optional withholding-on-payment module converts base and tax amounts between the source currency and the line currency at the payment date; it is not installed in the delivered configuration.
- [N-U25-105] Online payment providers may restrict the currencies they accept; an empty restriction means all currencies are accepted.
- [N-U25-106] The Thai bank-transfer QR code is generated only when the amount is in Thai baht.

### DEPENDENCY
- [N-U25-107] Bank-journal currency drives the statement, payment and reconciliation behaviour, so a foreign-currency bank account needs its own journal.

### CONSTRAINT
- [N-U25-108] The payment dialog refuses to create a payment when no outstanding-payments account is set for the method and journal.
- [N-U25-109] An online transaction is rejected when its amount or currency is missing from the provider data.

### RISK
- [N-U25-110] A foreign-currency journal with no rates converts its statement lines one to one.
- [N-U25-111] Choosing a journal in the company currency to pay a foreign-currency invoice forces a conversion at the payment date and a realized difference.

### UNKNOWN
- [N-U25-112] Provider-side currency conversion and provider rejection behaviour are runtime and network behaviour and cannot be determined from the source.

## CAP-U25-05 Foreign customer and vendor master data and tax treatment

### WHAT
- [N-U25-113] A contact holds a country, a state, a tax identification number held as free text, and a label for the tax number that follows the country of the active company.
- [N-U25-114] Fiscal positions map taxes and accounts and can be applied automatically when a contact's tax number, zip range, state, country or country group matches.
- [N-U25-115] A contact may have its own fiscal position, which always wins over automatic detection.

### WHY
- [N-U25-116] Foreign customers and vendors usually need different taxes and accounts than domestic ones, and detection by country keeps the choice consistent.

### BUSINESS RULE
- [N-U25-117] Automatic detection requires the contact to have a country; the first matching position wins, company-specific positions before shared ones and then by sequence.
- [N-U25-118] Detection on a sales order uses the shipping address; on an invoice it uses the shipping address when one exists; on a purchase order it uses the vendor itself.
- [N-U25-119] A position marked as requiring a tax number applies only when the contact has a tax number that is not the placeholder slash.
- [N-U25-120] A position can carry a foreign tax number of the company for the region it covers; the number is reformatted through the tax-number check hook when saved.
- [N-U25-121] Without the optional tax-number validation module, tax numbers are stored as typed with no format or registry check.
- [N-U25-122] The tax engine supports reverse-charge taxes through paired positive and negative repartition, and supports tax-included prices and per-line rounding.
- [N-U25-123] The Thai chart provides output and input value-added tax at seven percent, output and input taxes at zero percent, an exempt tax on each side, withholding taxes of one, two, three and five percent on purchases split into company and personal payees, and the same four rates on sales for tax withheld by customers.
- [N-U25-124] The Thai value-added tax report separates sales subject to zero percent and exempt sales, and has sections for company and personal withholding returns.
- [N-U25-125] The Thai chart contains an account for tax withheld on overseas payments, but no tax, report section or fiscal position uses it.

### STATE
- [N-U25-126] A contact moves between positions only when its country, state, zip or tax number changes or when a document is re-evaluated; a manual position on the contact overrides all changes.

### OPTIONALITY
- [N-U25-127] No fiscal position is delivered in the Thai configuration, so no foreign-customer treatment is applied automatically; positions must be created and flagged for automatic detection.
- [N-U25-128] Tax-number validation and reverse-charge treatment of imported services are optional and need their own installation or configuration.

### DEPENDENCY
- [N-U25-129] Foreign tax numbers on positions create or reuse foreign taxes through the chart-template mechanism, which installs the corresponding country chart module on demand.
- [N-U25-130] Withholding on payment to a foreign payee depends on the optional withholding module, and even there the withholding tax is picked by the user rather than derived from the payee's country.

### CONSTRAINT
- [N-U25-131] A tax number can be flagged with a placeholder to state that a contact has none, and this placeholder is not treated as a number.
- [N-U25-132] A position with a foreign tax number must name a country; when that country is the company's own fiscal country a state is required if the country has states; the country must lie inside the selected country group; and two positions with different numbers in the same country are refused.
- [N-U25-133] Thai branch labelling applies only to Thai company contacts; foreign contacts get no branch label.

### RISK
- [N-U25-134] With no seeded positions and no validation, a foreign customer would be invoiced with the domestic seven percent tax unless the user picks the zero-rate tax by hand.
- [N-U25-135] Thai withholding and import-VAT filings for foreign payees are not modelled in Community.

### UNKNOWN
- [N-U25-136] Whether a Thai deployment would need a payee-country-driven withholding rule cannot be settled from the source and is recorded for functional design.

## CAP-U25-06 International trade documents and logistics

### WHAT
- [N-U25-137] A catalogue of eleven standard delivery terms is delivered, each with a three-letter code, and can be selected on sales orders, purchase orders and invoices, with a free-text location.
- [N-U25-138] A product can carry a customs classification code and a country of origin when the shipping connector extension is installed.
- [N-U25-139] Delivery methods can be restricted to destination countries, states and zip prefixes, and are offered to an order only when the delivery address matches.
- [N-U25-140] Landed costs add freight and duty to the cost of received goods in company currency, optionally generated from a vendor bill.

### WHY
- [N-U25-141] Delivery terms state who bears transport, insurance and duty and are printed on commercial documents.
- [N-U25-142] Classification and origin codes are passed to carriers for customs declarations on international parcels.

### BUSINESS RULE
- [N-U25-143] The delivery terms of an order are copied to the invoice or bill created from it; a customer invoice otherwise defaults to the company's default terms.
- [N-U25-144] The invoice location text comes from the sales or purchase order when the stock-linked extensions are installed.
- [N-U25-145] The delivery slip prints the terms of the originating sales order; transfers themselves carry no terms field.
- [N-U25-146] A delivery method's price is computed in company currency and converted to the order currency at the order date, with margins applied in the order currency.
- [N-U25-147] When goods are described to a carrier, the origin falls back to the country of the issuing warehouse if the product has no origin.
- [N-U25-148] A landed-cost line generated from a vendor bill takes the bill line's company-currency value using the bill's rate.
- [N-U25-149] A product's standard cost is held in company currency; vendor prices keep their own currency and are converted when an order line is built.
- [N-U25-150] The imported electronic invoice format maps incoming delivery terms to the catalogue by code when exactly one code is present.

### STATE
- [N-U25-151] A landed-cost record is a draft until validated; validation is refused unless the costing method of the targets is first-in first-out or average cost.

### OPTIONALITY
- [N-U25-152] Delivery terms are optional on every document; the delivered database contains the eleven terms and the company default is set to ex works.
- [N-U25-153] Customs statistics reporting for trade in goods is an upgrade-only feature; the module is not part of the delivered source.
- [N-U25-154] Three regional delivery-point carriers limited to Belgium, Luxembourg, France, the Netherlands and Spain and two print-on-demand carriers are seeded active; they are regional integrations outside the Thai scope.

### DEPENDENCY
- [N-U25-155] Origin and classification codes depend on the shipping connector extension, which itself depends on the sales-stock and delivery applications.
- [N-U25-156] Landed costs depend on the inventory valuation setting and on the product costing method.

### CONSTRAINT
- [N-U25-157] The landed-cost currency is always the company currency; there is no currency choice on the record.
- [N-U25-158] A delivery method with a destination-country list excludes addresses whose country is not listed; an empty list means worldwide.

### RISK
- [N-U25-159] The delivered configuration uses standard cost, so landed costs cannot be applied to its products without changing the costing method.
- [N-U25-160] The delivery terms are descriptive only: they do not change taxes, accounts, prices or stock moves.
- [N-U25-161] No customs declaration, duty calculation, export document or import document is provided.

### UNKNOWN
- [N-U25-162] How duty and freight on foreign purchases should be booked for Thai needs is not determinable from the source and is left to functional design.

## CAP-U25-07 Foreign-currency reporting, revaluation, price lists and rounding

### WHAT
- [N-U25-163] Sales, purchase and invoice analysis reports express amounts in the currency of the active company by applying a rate table; the sales and purchase reports first divide by the stored order rate to return to company currency.
- [N-U25-164] When all selected companies share one currency the rate table collapses to a constant of one.
- [N-U25-165] Spreadsheet formulas can read exchange rates and company-currency account balances.
- [N-U25-166] Price lists have a currency and can be limited by country group; a rule can be based on list price, cost or another price list.

### WHY
- [N-U25-167] Management needs one comparable amount across companies and currencies without altering the books.

### BUSINESS RULE
- [N-U25-168] Where the rate table has no rate for a company's currency it uses one.
- [N-U25-169] The rate table can also build historical and average rate types for period reports, the average being weighted by days between rate changes of both currencies, but the delivered Community reports request only the current rate.
- [N-U25-170] The report rate table converts to the active company's currency using the rates held at the active company's root.
- [N-U25-171] Price-list rule results are converted between currencies without intermediate rounding and rounded at the end.
- [N-U25-172] A conversion in the invoice analysis report divides document amounts by the stored invoice rate.

### STATE
- [N-U25-173] Nothing in the system revalues open foreign-currency balances at period end; open balances are carried at their original rates until settled.

### OPTIONALITY
- [N-U25-174] Unrealized revaluation of open foreign-currency items, aged receivable and payable reports in two currencies, and consolidated statements are not provided in Community: no module, menu or report definition for them exists in the source set, and the only revaluation found concerns inventory cost.
- [N-U25-175] The report definitions model only describes report structure; the engine that renders financial reports is not part of the delivered source.

### DEPENDENCY
- [N-U25-176] Cross-company report conversion depends on rates held at the active company's root.

### CONSTRAINT
- [N-U25-177] A company-currency conversion for a report never fails on a missing rate; it silently uses one.

### RISK
- [N-U25-178] Cross-company analysis converts at the rate current at the report date for every document, so historical values shift when rates move.
- [N-U25-179] A comment in the purchase report states it is not multi-currency while its query does convert, so the comment appears stale.
- [N-U25-180] Rounding differences between document-currency totals and company-currency totals can occur on every foreign-currency document because tax and totals are rounded in both currencies.

### UNKNOWN
- [N-U25-181] Report results with real multi-currency data need execution to verify.

## CAP-U25-08 Multi-company and multi-currency interplay, including foreign-owned structures in Thailand

### WHAT
- [N-U25-182] Each company has its own currency; branches of a company share the currency of their root, so a different currency requires a separate top-level company.
- [N-U25-183] Exchange rates are held per top-level company, and the rate-table used for reports takes the active company as the reference currency.
- [N-U25-184] An optional inter-company payment module clears a payment made through one company against an invoice of a sister company using clearing accounts and a clearing journal in both companies.

### WHY
- [N-U25-185] A Thai subsidiary of a foreign group keeps its books in baht while the parent keeps its own currency; each legal entity must have a coherent ledger of its own.

### BUSINESS RULE
- [N-U25-186] The clearing entry in the paying company is posted in the payment currency with its company-currency balance; the clearing entry in the invoice company is posted in that company's own currency with that company's balance.
- [N-U25-187] The payment dialog can pay invoices of several branches of one company together and then uses the root company as the paying company.
- [N-U25-188] A branch inherits fiscal-year end, tax-exigibility basis and reversal-accounting style from its root.
- [N-U25-189] Records without a company, including shared rates and shared price lists, are visible to all companies; company-specific price lists are visible to the company and its branches.

### STATE
- [N-U25-190] An inter-company settlement moves each side's receivable or payable to the clearing account of its own company when the invoice is posted after the payment.

### OPTIONALITY
- [N-U25-191] The inter-company payment module is installed in the delivered configuration but needs a clearing journal and accounts set per company; the delivered database has a single company and so nothing to clear.
- [N-U25-192] Automatic creation of the mirror sales or purchase order or invoice in a sister company, group-currency reporting and consolidation are not provided in Community: no module for them exists in the source set.

### DEPENDENCY
- [N-U25-193] Inter-company clearing depends on the online-payment application, because it starts from a payment transaction made in another company.
- [N-U25-194] Company-to-jurisdiction assignment and the localization framework belong to other studies; this study only records that a company's fiscal country is a company setting.

### CONSTRAINT
- [N-U25-195] A foreign company's branch, representative office or regional office operating in Thailand either shares its parent's currency as a branch, or must be created as its own top-level company to keep baht books; the structure choice is therefore a design decision with currency consequences.
- [N-U25-196] The company hierarchy cannot be changed after creation.

### RISK
- [N-U25-197] The clearing entries on the two sides are independent: no exchange difference is generated between the two companies' currencies, so cross-currency inter-company balances need manual control.
- [N-U25-198] Group-level reporting in the parent's currency is not available in Community, so a Thai subsidiary of a foreign group would need external consolidation.

### UNKNOWN
- [N-U25-199] Behaviour of the clearing entries with different company currencies needs execution to confirm.

## CAP-U25-09 Roles, access, validation constraints and failure behaviour

### WHAT
- [N-U25-200] Every user, including portal and public users, can read currencies and rates; only system administrators and accounting managers can create, change or delete them.
- [N-U25-201] Delivery terms can be read by all internal users and changed only by accounting managers; the menu for them is limited to technical-feature users.
- [N-U25-202] The currencies menu sits under the accounting configuration, which only accounting managers see.

### WHY
- [N-U25-203] Rates drive every foreign amount in the books, so changing them is restricted to those accountable for the books.

### BUSINESS RULE
- [N-U25-204] Rate records are subject to a company rule: a user sees shared rates and rates of the root of any activated company.
- [N-U25-205] The multi-currency group has no permissions of its own; it only reveals fields on screens.

### STATE
- [N-U25-206] A document in draft can have its currency and rate changed; a posted document cannot.

### OPTIONALITY
- [N-U25-207] A user with currency write access can change a rate retroactively, but a posted document keeps the amounts it was posted with.

### DEPENDENCY
- [N-U25-208] Several conversions rely on the active company at the time of the call, so switching companies in a session changes which rates are used.

### CONSTRAINT
- [N-U25-209] Refusals relevant to foreign amounts include: inactive currency on posting, a missing bill date on vendor bills, a non-positive rate, a company currency change after entries, reducing decimal places after use, deactivating a company currency, missing exchange journal or accounts, a forced account currency conflict and a foreign statement currency equal to the journal currency.

### RISK
- [N-U25-210] Because a missing rate yields one silently, there is no failure message for the most likely multi-currency configuration error.
- [N-U25-211] Rates are not audit-tracked in the currency screens in the same way as business documents, so changes to rates rely on general logging.

### UNKNOWN
- [N-U25-212] Whether rate changes are traceable through the generic change log cannot be confirmed from the source read.
