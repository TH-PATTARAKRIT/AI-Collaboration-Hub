# Neutral Clean-Room Knowledge Pack — Thai Tax Core

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Neutral layer only: no vendor structure, no code, no schema. Concatenated from the neutral files below; each statement keeps its id and links to claims in the restricted layer.

## Sources
- `TXA1_thaitax_engine_vat_classes_NEUTRAL.md`
- `TXA2_thaitax_documents_period_reversal_NEUTRAL.md`
- `TXC_thaitax_schema_dump_reconciliation_NEUTRAL.md`
- `U13_account_tax_chart_localization_NEUTRAL.md`
- `U23_not_installed_current_NEUTRAL.md`
- `U24_thailand_localization_NEUTRAL.md`
- `U25_multicurrency_international_NEUTRAL.md`
- `TXS_thai_statutory_neutral.md`


---

<!-- source: TXA1_thaitax_engine_vat_classes_NEUTRAL.md -->
# TXA1 - Thai tax core: calculation engine, VAT treatments, price inclusion, currency - Neutral Knowledge

> **NEUTRAL KNOWLEDGE - clean-room layer.** Source product studied: Odoo 19 Community (named once, here only). Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**. Date 2026-10-02.
> Scope: how the system computes and books tax, which tax treatments the Thai set-up represents, and which configuration drives them. It describes what the system does and why; it does not state what Thai law requires. Every Thai treatment is marked STATUTORY CHECK PENDING (TXS).
> Statements are tagged with identifiers and linked to restricted evidence by the same identifier. No coverage, completeness or approval is claimed.

## CAP-TXA1-01 Generic tax calculation engine

### WHAT

- [N-TXA1-001] A single shared calculation routine turns the taxes attached to a document line, together with unit price, quantity and discount, into a base amount, one tax amount per tax, a total without tax and a total with tax. Every document type that carries taxes calls the same routine.
- [N-TXA1-002] Any business record that carries a price, a quantity and taxes (an order line, a journal item, an expense, a plain data structure) is first converted into a neutral line description, so order lines, purchase lines, invoice lines and expense lines produce identical results for identical inputs.
- [N-TXA1-003] An older single-line entry point remains available. It wraps the same routine and returns the total without tax, the total with tax, the amount per distribution line with account, tags and exigibility, and the portion of taxes that have no account.
- [N-TXA1-004] The routine is duplicated in client-side code so that previews on screen match the stored result. Both implementations are required to stay equivalent; the only documented difference is non-deductible handling, which exists on the server side only.

### WHY

- [N-TXA1-099] Every document that carries taxes must show the same tax figures for the same inputs, so one calculation is shared by orders, invoices, expenses and exports instead of being repeated per document type.

### BUSINESS RULE

- [N-TXA1-005] A tax has one of four computation types: percentage, fixed amount, percentage-included division, or a group of other taxes. The installed set offers no formula-based type.
- [N-TXA1-006] Every tax declares where it may be selected: sales, purchases, or none. A tax of type none can be used only as a member of a group. The default is sales.
- [N-TXA1-007] A tax may optionally be limited to services or to goods.
- [N-TXA1-008] Taxes on a line are applied in ascending order of a sequence number, ties broken by creation order. Inside the routine, fixed taxes are evaluated first, then taxes whose amount is contained in the price, then taxes added on top of the price.
- [N-TXA1-009] A group of taxes is replaced by its member taxes. The group's own sequence decides where its members sit, and the members are ordered among themselves by their own sequence.
- [N-TXA1-010] Taxes of the same computation type, the same price-inclusion setting and the same base-affecting setting are calculated together as one batch, so that several inclusive percentages are extracted jointly rather than one after another.
- [N-TXA1-011] A tax may be flagged to add its amount to the base of later taxes, and a later tax may opt out of being affected. The routine propagates each tax amount as extra base to taxes before or after it according to these flags, price-inclusion and the active special mode. This is how compounding taxes are modelled.
- [N-TXA1-012] A fixed tax equals quantity times its amount, carrying the sign of the unit price. It does not depend on the price, and discounts do not reduce it.
- [N-TXA1-013] A percentage tax added on top of the price equals the base times its percentage, where the base already includes any amounts propagated from earlier base-affecting taxes.
- [N-TXA1-014] A division-type tax added on top of the price equals the base times its percentage, divided by one minus the sum of the percentages in its batch.
- [N-TXA1-015] A line may force a special mode in which every tax is read as contained in the price or as added on top of it. A line may also carry a special type (early payment, cash rounding, non-deductible, global discount, down payment) that selects custom handling inside the routine.
- [N-TXA1-016] A tax whose distribution has a negative factor produces a second, mirrored entry with the opposite amount, the reverse-charge pattern. Such a tax is never read as contained in the price.
- [N-TXA1-017] When a percentage tax has no printed label, the label defaults to its percentage.

### STATE

- [N-TXA1-108] A taxed line moves from its source record to a neutral description, then to unrounded tax details, then to rounded details, then to journal items.

### OPTIONALITY

- [N-TXA1-019] Several related capabilities exist in the community source but are not installed in this database: formula-defined taxes, payment-time withholding, VAT-number validation, re-application of tax tags to existing entries and debit notes. None of them is part of the effective behaviour studied here.

### DEPENDENCY

- [N-TXA1-018] Each calculation receives a context holding product values, unit-of-measure values, price, quantity, base and special mode. The base set of product and unit fields is empty; it is a hook that extensions fill when a tax depends on product attributes.

### CONSTRAINT

No statement in this section for this capability.

### RISK

No statement in this section for this capability.

### UNKNOWN

- [N-TXA1-116] The numeric result of combining a VAT with a withholding tax on one line, and of rounding differences over several lines in the Thai currency, has never been executed.

## CAP-TXA1-02 Rounding, totals, discounts and cash rounding

### WHAT

No statement in this section for this capability.

### WHY

- [N-TXA1-100] The tax and total of a document must equal what a computation over the whole document would give, whatever the number of lines, so rounding is controlled at document level and differences are assigned deliberately.

### BUSINESS RULE

- [N-TXA1-020] Rounding follows a company setting with two methods: round each line, or round globally across the whole document. The default is global rounding. Every rounding step uses the precision of the currency concerned.
- [N-TXA1-021] Under global rounding the routine rounds the document total of each tax once and spreads the difference against the sum of rounded line amounts over the lines. For taxes contained in the price it rounds base plus tax and derives the base by subtraction, so that the document total equals a total computed on the whole.
- [N-TXA1-022] Rounding differences are distributed in smallest-currency units in proportion to the line amounts, largest first, with any leftover units given one each to the biggest amounts.
- [N-TXA1-023] When a user edits a tax amount by hand, the edited amount is kept as long as the lines do not change in a way that affects taxes. Changing the currency or switching between invoice and credit note discards manual amounts and recomputes everything; editing the tax totals rewrites the first tax item of the group by the difference.
- [N-TXA1-024] Lines may carry forced untaxed totals or forced per-tax amounts, used by down payments, combo products and global discounts. They are stored with the line and re-used only if price, quantity, discount, currency and the set of taxes are unchanged; they are rescaled when the rate changes.
- [N-TXA1-025] A totals summary gives, in document currency and in company currency, the untaxed amount, the tax amount and the total, grouped by tax group in group order and under optional subtotal labels. Orders, invoices and printed documents all use it; the displayed base of a group is blank for fixed-only groups.
- [N-TXA1-026] Cash rounding can add a separate rounding line or change the largest tax amount so that the total lands on a coin-size step. A rule has a precision, a strategy, a direction and gain and loss accounts. The strategy that changes a tax does nothing when the document has no tax.
- [N-TXA1-027] A per-line discount reduces the unit price before tax. A global discount is split into discount lines per tax set so that tax falls proportionally; fixed taxes are not discounted; a negative-quantity line that exactly matches a positive line is netted against it for tax purposes.
- [N-TXA1-028] A down payment is split across the taxes of the original lines through the same routine, so the advance invoice carries its own tax and later invoices deduct it. After posting, the order's down payment lines take over the taxes actually invoiced.
- [N-TXA1-029] An early-payment discount reduces tax according to a payment-term choice: reduce the tax only on early payment, never, or always at invoicing. In the always mode the tax is computed on the discounted untaxed amount through paired special lines.

### STATE

- [N-TXA1-109] Manual tax amounts are kept while edits do not affect taxes. They are discarded when the currency or the document type changes. A change of rate alone keeps the foreign-currency amounts and re-derives the company-currency amounts.

### OPTIONALITY

No statement in this section for this capability.

### DEPENDENCY

No statement in this section for this capability.

### CONSTRAINT

No statement in this section for this capability.

### RISK

No statement in this section for this capability.

### UNKNOWN

- [N-TXA1-117] The Thai statutory convention for rounding tax amounts is not established by community evidence and is pending statutory validation.

## CAP-TXA1-03 Distribution lines, tax grid tags, accounts and tax journal items

### WHAT

No statement in this section for this capability.

### WHY

- [N-TXA1-101] Each tax figure must land on the right account with the right return-grid tags, for invoices and credit notes alike, so that reports can be built from posted entries alone.

### BUSINESS RULE

- [N-TXA1-030] Each tax has an invoice side and a credit-note side of distribution lines. Each side has exactly one base line and at least one tax line; the two sides are equal in number and mirrored in order, type and percentage. Positive tax factors total one hundred percent and any negative factors total minus one hundred percent. A tax line may name an account other than receivable, payable or off-balance. Credit notes use the credit-note side, and rounding differences between distribution lines are spread automatically.
- [N-TXA1-031] Tax grid tags attach to base items and tax items from the distribution lines, together with tags stored on the product and tags of preceding base-affecting taxes. On the document, only taxes recognised at invoicing attach their tags; cash-basis taxes attach theirs when payment is registered. Selectable tags are limited to tags without country, tags of the company's fiscal country and tags of its foreign-VAT countries.
- [N-TXA1-032] Tax journal items are grouped by partner, currency, analytic split, account, line taxes, distribution line and group. Each carries its base amount and is named after the tax. On a draft document the existing tax items are updated, removed or created to match the new result; posted documents are not re-synchronised.
- [N-TXA1-033] A tax journal item whose amount is zero in both currencies is not created, so zero-rated and exempt sales leave only base items carrying their tags.
- [N-TXA1-034] A tax item inherits the analytic split of its base line only when the tax is flagged for inclusion in analytic cost or when its distribution line is not used in tax closing.
- [N-TXA1-035] Every tax belongs to a required tax group that carries a country, payable, receivable and advance accounts and an optional subtotal label. When a tax has no group, the first group of its country is assigned, else a group without country. Group membership forbids nesting and cycles, and the scope of members must match the group.
- [N-TXA1-038] Each distribution line carries a closing flag that defaults true only for tax lines on accounts that are neither income nor expense. No installed module was found that posts a tax closing entry from this flag; only the reporting query and the analytic decision read it.

### STATE

- [N-TXA1-036] A tax is recognised either at invoicing (default) or at payment (cash basis). A cash-basis tax posts to a transition account until settlement, and entries in a cash-basis journal are created at reconciliation. Items mixing cash-basis and invoice-basis taxes may not share tags. The installed Thai taxes are all recognised at invoicing.
- [N-TXA1-110] A draft document keeps its tax items in step with its lines: items are created, updated or removed whenever lines change. Posted documents are not re-synchronised.

### OPTIONALITY

- [N-TXA1-037] A company switch unlocks the cash-basis option on taxes; it cannot be switched off while any tax is cash-basis. Loading a chart sets the switch only when a cash-basis tax exists, but the Thai template sets it on although no Thai tax uses it.

### DEPENDENCY

- [N-TXA1-039] A shared query maps base items to their tax items, expanding group taxes into their members, to support tax reporting.

### CONSTRAINT

No statement in this section for this capability.

### RISK

No statement in this section for this capability.

### UNKNOWN

- [N-TXA1-118] Whether a zero-rated sale leaves exactly the base items with both tags at runtime, and whether the unused tags matter to any report formula, has not been exercised.

## CAP-TXA1-04 Sales and purchase VAT on documents

### WHAT

No statement in this section for this capability.

### WHY

- [N-TXA1-102] Taxes should be proposed automatically from product, account and company set-up, so that users rarely pick a tax by hand and the chain from order to invoice stays consistent.

### BUSINESS RULE

- [N-TXA1-040] On a customer document line the default taxes are the product's sales taxes of the company tree, else the sale-type taxes set on the line's account; on a vendor document line they are the product's purchase taxes, else the purchase-type taxes of the account. The result is narrowed to the company tree and mapped through the document's fiscal position. Miscellaneous entries get no default taxes. The company's own default tax is not read at this level.
- [N-TXA1-041] On sales and purchase orders the default comes only from the product, narrowed by company and mapped by the order's fiscal position. Combo products and lines without a product carry no tax, and the account's taxes are not consulted.
- [N-TXA1-042] A company has a default sale tax and a default purchase tax. They become the default taxes of new products, a product created without company also receives the defaults of other companies, and loading a chart assigns them when missing.
- [N-TXA1-043] Quick encoding suggests the partner's most frequent account and tax combination of the last two years. Without history it falls back to the taxes of the journal's account, then to the company default tax, then maps through the fiscal position.
- [N-TXA1-044] A ledger account may carry default taxes. An off-balance account may not.
- [N-TXA1-045] A product carries a sales tax set and a purchase tax set that default from the company defaults. Choosing the combo product type clears both sets.
- [N-TXA1-046] Product income and expense accounts resolve from the product, then the category chain, then the company, and the document's fiscal position then maps the account. Stock accounting and manufacturing accounting add the stock valuation and production cost accounts.
- [N-TXA1-047] Taxes set on an order line travel unchanged to the invoice line together with the engine's stored data. Delivery operations re-use the sale line's calculation to value the delivered quantity including tax for display.
- [N-TXA1-048] Expense claims are taxed with the entered amount read as tax-included regardless of the company price-inclusion setting. Their taxes default from the product's purchase taxes, and the expense module extends the engine hooks so tax items stay linked to the expense.

### STATE

- [N-TXA1-111] An order line receives its taxes when entered, and creating the invoice copies them. Changing the fiscal position of an order that has lines raises a prompt to update taxes. Posting a down payment hands its taxes back to the order lines.

### OPTIONALITY

No statement in this section for this capability.

### DEPENDENCY

No statement in this section for this capability.

### CONSTRAINT

No statement in this section for this capability.

### RISK

No statement in this section for this capability.

### UNKNOWN

- [N-TXA1-119] Whether the tax amounts of a foreign-currency order and of the invoice created from it differ because their rates are taken at different dates has not been exercised.

## CAP-TXA1-05 Thai tax treatments represented in the Thai template

### WHAT

- [N-TXA1-049] The Thai localization loads for companies located in Thailand. It sets six-digit account codes, default receivable, payable, stock valuation and down-payment accounts, and company defaults: fiscal country, default sale tax and default purchase tax set to the standard VAT, and the cash-basis switch. It ships no fiscal position, journal or reconciliation-model data and overrides no tax or calculation behaviour; its only accounting override chooses the Thai invoice layout. STATUTORY CHECK PENDING (TXS) for every content choice.
- [N-TXA1-050] Standard-rated treatment is represented by one purchase tax and one sale tax at seven percent, placed in a VAT group, booked to input VAT and output VAT accounts, with return-grid tags on the base and on the tax and with the closing flag on. Credit notes mirror the invoice side. STATUTORY CHECK PENDING (TXS).
- [N-TXA1-051] Zero-rated treatment is represented by a zero-percent purchase tax and a zero-percent sale tax. The sale tax base carries both the sales grid tag and a dedicated zero-rated sales tag; the zero tax item is not persisted. Neither tax names a group in the template. STATUTORY CHECK PENDING (TXS).
- [N-TXA1-052] Exempt treatment is represented by zero-percent purchase and sale taxes named exempt. The sale tax base carries the sales tag and an exempted-sales tag; the purchase tax shares the ordinary purchase grid tag. The Thai-language description of the purchase record also mentions input tax that the law does not allow to be refunded; this is translation text only and no separate non-deductible tax record exists. STATUTORY CHECK PENDING (TXS).
- [N-TXA1-053] Withholding is represented by ordinary negative-percentage taxes recognised at posting: eight purchase-side taxes (four rates for company payees, four for individual payees) credited to withholding liability accounts, and four sale-side taxes for amounts withheld by customers, debited to a creditable asset account and forced price-excluded. None is flagged for closing. The tax is chosen by the user line by line; no payee-driven selection exists. STATUTORY CHECK PENDING (TXS).
- [N-TXA1-054] Five tax groups exist: four withholding groups by rate and one VAT group at seven percent. Because the zero-rate and exempt taxes name no group, the default group search places them in the first withholding group, which is a configuration risk for any report or total that groups by tax group.
- [N-TXA1-055] Tax-related ledger accounts defined by the Thai chart include input VAT, output VAT, undue input VAT and undue output VAT (referenced by no tax), withholding liability accounts by return form (one for foreign payees, referenced by no tax), creditable withholding, VAT receivable and payable, withholding receivable and payable, and customer advances.
- [N-TXA1-056] Thirteen Thai tax-grid tags are defined: return lines for sales, zero-rated sales, exempt sales, output tax, purchase amount, input tax, excess carried forward, plus withholding return tags and two surcharge tags. The excess and surcharge tags are used by no tax.
- [N-TXA1-057] The Thai module selects a Thai invoice layout for companies whose fiscal country is Thailand; its title is a fixed word that is translatable, and partner branch labels are computed.

### WHY

- [N-TXA1-103] Thai tax treatments are expressed with generic mechanisms only, so what is Thai about the set-up is data that can be validated against official sources without touching calculation behaviour.

### BUSINESS RULE

- [N-TXA1-059] Legal notes entered on taxes and on fiscal positions print on invoices, lines show tax labels, totals print per tax group with an optional company-currency block, and total in words is optional. The Thai taxes declare no legal notes.

### STATE

- [N-TXA1-112] A company without a chart receives the Thai chart when the Thai module is installed on a company located in Thailand; afterwards documents book taxes at posting, and reloading the chart follows the reload rules.

### OPTIONALITY

No statement in this section for this capability.

### DEPENDENCY

- [N-TXA1-058] The e-invoicing module adds a tax category code and an exemption reason code to taxes and validates tax distribution at export. None of the Thai taxes has a category code and no Thai e-invoice format exists in the installed set; without a code, a domestic zero-amount tax would be inferred as exempt.

### CONSTRAINT

No statement in this section for this capability.

### RISK

No statement in this section for this capability.

### UNKNOWN

- [N-TXA1-120] The statutory classification, rate, grid and account of every seeded Thai tax record are unverified and pending statutory validation.

## CAP-TXA1-06 Non-deductible tax and tax on stock and cost flows

### WHAT

No statement in this section for this capability.

### WHY

- [N-TXA1-104] A business must be able to claim only the deductible part of a mixed-use purchase and to treat irrecoverable tax as part of cost; the system offers percentage-based routing and cost capitalisation for these needs.

### BUSINESS RULE

- [N-TXA1-060] On vendor bills each line has a deductibility percentage (default one hundred, range zero to one hundred, vendor documents only). The non-deductible share of the subtotal, together with its non-fixed taxes, is moved to a separate private-share account of the purchase journal through additional lines, so the bill still balances.
- [N-TXA1-061] Document totals report the tax on private-share lines as a separate non-deductible tax amount, deducted from the regular tax of each group and from the document tax total.
- [N-TXA1-062] Posting a partly deductible bill adds the user to a group that reveals the deductibility column.
- [N-TXA1-064] The inventory cost of a received purchase line excludes taxes whose distribution lines have an account. Taxes whose distribution lines have no account are included in cost. All Thai tax lines have an account, so no tax enters inventory cost under the Thai set.
- [N-TXA1-065] A vendor bill line prepared from a stored purchase line carries an explicit company-currency balance equal to the unrounded untaxed total converted without rounding.
- [N-TXA1-066] The valuation unit price taken from an invoice line applies the discount to the unit price unless a tax contained in the price is present, in which case the subtotal divided by quantity is used.
- [N-TXA1-067] Cost-of-goods entries for customer invoices are produced only for storable products with real-time valuation, and valuation difference entries at bill posting are created without taxes; so VAT never enters cost of goods sold. In this database the anglo-saxon flag is off.

### STATE

- [N-TXA1-113] A vendor bill line with full deductibility is normal. With less than full deductibility, private-part lines are created when the draft is saved and renamed with the document number at posting.

### OPTIONALITY

- [N-TXA1-063] The private-share account is configured per purchase journal and is not set in this database; the revealing group exists. Mechanism is percentage-based and does not mark a particular tax or rate as prohibited.

### DEPENDENCY

No statement in this section for this capability.

### CONSTRAINT

No statement in this section for this capability.

### RISK

No statement in this section for this capability.

### UNKNOWN

- [N-TXA1-121] Whether a prohibited input-tax treatment can be represented by the percentage deductibility mechanism, given that the return grid would still count the base as claimable, is unknown and pending statutory validation.

## CAP-TXA1-07 Price-included and price-excluded handling, currency conversion and multi-currency tax amounts

### WHAT

No statement in this section for this capability.

### WHY

- [N-TXA1-105] A foreign-currency transaction needs its tax shown both in the transaction currency and in the company currency, using a rate stored on the document for audit.

### BUSINESS RULE

- [N-TXA1-068] Whether an entered price contains the tax is decided per tax: a tax-level override wins, otherwise the company default applies, which is tax excluded unless changed.
- [N-TXA1-070] A tax contained in the price is extracted in reverse: the base equals the price divided by one plus the sum of the batch percentages. Quick encoding uses forced inclusive mode to derive an untaxed price from a typed total.
- [N-TXA1-071] The default unit price of a line is the product's list price (sales) or standard cost (purchase), converted for the unit of measure, adapted to the tax mapping of the fiscal position and finally converted to the document currency at the document date without rounding.
- [N-TXA1-072] The product form shows computed amounts including and excluding tax, and invoices show the untaxed subtotal or the taxed total on each line according to the company default.
- [N-TXA1-073] Amounts are kept in the document currency and in the company currency. The company-currency amount equals the document amount divided by the line rate and is rounded separately in each currency; the document-currency amount is never derived from a rounded company amount.
- [N-TXA1-074] Tax amounts in company currency are displayed on sale documents in a foreign currency when a company flag (on by default) is set; purchase orders also show their total converted to company currency.
- [N-TXA1-075] An invoice stores its currency rate at the invoice date (today when empty), can refresh it on demand, keeps a rate the user edited manually, requires it to be positive, and recomputes the dependent amounts when it changes. Orders store their own rate at the order date, and the invoice created from an order computes its own rate at its own date.
- [N-TXA1-076] The rate used is the latest rate on or before the date, else the earliest rate, else one. Conversion multiplies by that rate and rounds to the target currency unless rounding is disabled. No installed module or scheduled job fetches rates, and this database holds no rate rows, so a foreign amount converts at one until a rate is entered.
- [N-TXA1-077] The company defines an exchange-difference journal and gain and loss accounts for settlements in foreign currency.
- [N-TXA1-079] A taxable supply date field exists on documents, but its logic is an empty stub in the accounting module and the date used for the currency rate is the invoice date; no tax-point date logic exists in the installed set.

### STATE

- [N-TXA1-114] An invoice rate is recomputed when currency, company or invoice date changes, stays as typed when the user edited it, and must be positive.

### OPTIONALITY

No statement in this section for this capability.

### DEPENDENCY

No statement in this section for this capability.

### CONSTRAINT

- [N-TXA1-069] The company price-inclusion default cannot be changed once the company has started invoicing.
- [N-TXA1-078] A currency's decimal precision cannot be reduced once it has been used in accounting entries.

### RISK

- [N-TXA1-080] If the company price-inclusion default were switched to tax included, a purchase VAT and a purchase withholding on one line would be extracted together and the negative percentage would shrink the base; sale withholding taxes are protected by a price-excluded override but purchase withholding taxes are not. The numeric effect has not been run.

### UNKNOWN

- [N-TXA1-122] The statutory source and date of exchange rates for tax on foreign-currency transactions are not established and are pending statutory validation.

## CAP-TXA1-08 Company, partner, product and fiscal configuration that drives tax

### WHAT

- [N-TXA1-082] Customer orders, vendor orders, invoices, agreements, replenishment orders and service-resale orders all call the same fiscal position finder and then map product taxes through the result.
- [N-TXA1-084] A fiscal position holds replacement taxes, an account mapping, an automatic-detection flag, a VAT-required flag, country, country group, states, a zip range, notes and an optional foreign tax identifier; a zip range needs both bounds, and a foreign identifier needs a country, a state within the fiscal country, a country inside its group and is unique per country. Creating foreign taxes may install another country's localization and is limited to accounting managers.
- [N-TXA1-091] Company settings that shape tax behaviour include fiscal country, rounding method, price-inclusion default, default sale and purchase taxes, cash-basis switch and its journal, taxes-in-company-currency flag, anglo-saxon flag and exchange-difference accounts; all are stored on the company and surfaced in the accounting settings.
- [N-TXA1-092] In this database the company uses the Thai chart, global rounding, tax-excluded prices, the cash-basis switch on, taxes-in-company-currency on, anglo-saxon off, default sale and purchase taxes set to the standard VAT, fiscal country Thailand and no tax lock date.
- [N-TXA1-093] Sixteen seeded service products exist; fourteen carry the standard sales VAT and all sixteen carry the standard purchase VAT; none carries account tags. Ten payment terms exist, all using the early-payment mode that reduces tax on early payment, and one has an early discount.

### WHY

- [N-TXA1-106] Which tax and account apply depends on who the partner is and where the goods go, so a partner-driven rule, the fiscal position, can replace taxes and accounts on a document.

### BUSINESS RULE

- [N-TXA1-081] A document's fiscal position is found in this order: no partner gives none; the delivery address stands in for the partner (and for EU partners sharing the company's VAT prefix the invoicing partner is used); a position set manually on the delivery or invoicing partner wins without further checks; without a partner country there is no automatic position; otherwise the first automatic position of the company, company-specific before parent, then by sequence, that passes tests on VAT presence, zip range, state, country and country group.
- [N-TXA1-083] A fiscal position replaces taxes: each original tax is replaced by the replacement taxes that list it, unmapped taxes pass through, a position without taxes keeps only taxes that belong to no position, and no position leaves taxes unchanged. It also swaps ledger accounts through an account mapping.
- [N-TXA1-085] The company's domestic fiscal position is computed as the lowest-sequence position matching the company country or its country group.
- [N-TXA1-086] When a position maps taxes contained in the price to other taxes, the unit price is adapted so the customer-facing price stays coherent: the original included taxes are stripped and the new included taxes added. If any original tax is not price-included, the price is left unchanged.
- [N-TXA1-088] A document's tax country is the foreign-VAT position's country or else the company's fiscal country. Taxes whose country differs are refused on the document, and selectable taxes on order lines are limited to the order's tax country.
- [N-TXA1-089] In the accounting module the VAT-number syntax check is an empty stub that returns the number unchanged; a partner counts as having a VAT number when the field is set and is not a slash. Real validation belongs to an extension that is not installed.
- [N-TXA1-090] Taxes, tax groups, distribution lines and fiscal positions are visible within the user's allowed companies and their parents. Selecting taxes walks up the company tree. Exchange rates and the cash-basis switch live on the root company of a tree, so branches share them.

### STATE

- [N-TXA1-115] A document gets its fiscal position when the partner, delivery address or company is set or changed; a position set manually on the partner wins over automatic detection.

### OPTIONALITY

No statement in this section for this capability.

### DEPENDENCY

No statement in this section for this capability.

### CONSTRAINT

No statement in this section for this capability.

### RISK

No statement in this section for this capability.

### UNKNOWN

- [N-TXA1-087] This database has no fiscal position, no account mapping, no default tax on any account and no cash-rounding rule, so detection, mapping and price adaptation have never been exercised for the Thai company.

## CAP-TXA1-09 Tax record lifecycle, template loading, security and locks

### WHAT

- [N-TXA1-097] All internal users can read taxes, tax groups, distribution lines and fiscal positions; creating, editing and deleting is limited to the accounting administrator role; cash-rounding rules are editable by the invoicing role.

### WHY

- [N-TXA1-107] Tax set-up is sensitive: used taxes must never disappear, only authorised roles may change them, and reloading a template must not silently alter live taxes.

### BUSINESS RULE

- [N-TXA1-098] A taxed document other than a sales document that is dated on or before the tax lock date is moved to the first open day, and at posting the same date check applies; any change to a posted taxed line on or before the lock date is refused. A document counts as affecting the tax report when a line has taxes, is a tax line or carries tax tags.

### STATE

- [N-TXA1-094] A tax is created with default distribution lines, may be archived at any time, cannot be deleted once used on a journal item, a reconciliation model, a purchase line or an expense, and its company cannot change once journal items refer to it. Order lines on sales alone do not count as use. Changes to tracked fields are logged only after first use.
- [N-TXA1-096] When a chart template is loaded again, a tax is treated as changed if its type, amount or number of distribution lines differ; changed taxes are skipped unless creation is forced, in which case the old tax is renamed with a marker prefix and a new one is created. Existing user-set group accounts are kept. Other modules extend the loader for their own accounts.

### OPTIONALITY

No statement in this section for this capability.

### DEPENDENCY

No statement in this section for this capability.

### CONSTRAINT

- [N-TXA1-095] Tax names are unique per usage, scope and country across the company tree; a tax group with a country must match the tax country; a cash-basis tax needs a reconcilable transition account; the tax company cannot change once used.

### RISK

No statement in this section for this capability.

### UNKNOWN

- [N-TXA1-123] Whether a tax used only on sales order lines can be deleted in practice, and how reloading the Thai template behaves against modified taxes, have not been exercised.

## REGISTER: Function Catalog

Candidate catalogue identifiers, not function identifiers. Status vocabulary: NATIVE, PARTIAL, NATIVE GAP / EXTENSION REQUIRED, UNKNOWN. A gap status means the statutory need is pending validation by the statutory unit; absence in community source is not proof that no requirement exists.

| Cat-ID | Function (neutral name) | Topic # | Existing Function-ID or FUNCTION MAPPING REQUIRED | Trigger | Neutral-refs | Statutory link | Native status |
|---|---|---|---|---|---|---|---|
| TXA1-F01 | Define a tax record: computation type, usage scope, goods or services scope, sequence, rate, label | 1 | FUNCTION MAPPING REQUIRED | Tax master maintenance; chart load | N-TXA1-005 N-TXA1-006 N-TXA1-007 N-TXA1-008 N-TXA1-017 | none | NATIVE |
| TXA1-F02 | Expand a group of taxes into ordered member taxes | 1 | FUNCTION MAPPING REQUIRED | Every calculation involving a group | N-TXA1-009 N-TXA1-035 | none | NATIVE |
| TXA1-F03 | Batch compatible taxes for joint calculation | 1 | FUNCTION MAPPING REQUIRED | Every calculation | N-TXA1-010 | none | NATIVE |
| TXA1-F04 | Compute a percentage tax added on top of the price for one line | 1 | FUNCTION MAPPING REQUIRED | Any taxed line | N-TXA1-013 N-TXA1-001 N-TXA1-008 N-TXA1-116 | none | NATIVE |
| TXA1-F05 | Compute a fixed-amount tax | 1 | FUNCTION MAPPING REQUIRED | Any line with a fixed tax | N-TXA1-012 | none | NATIVE |
| TXA1-F06 | Compute a division-type tax | 1 | FUNCTION MAPPING REQUIRED | Any line with a division tax | N-TXA1-014 N-TXA1-070 | none | NATIVE |
| TXA1-F07 | Formula-defined tax | 1 | FUNCTION MAPPING REQUIRED | Not available | N-TXA1-019 N-TXA1-005 | none | UNKNOWN |
| TXA1-F08 | Make a tax affect the base of later taxes (include-in-base chain) | 1 | FUNCTION MAPPING REQUIRED | Compounding taxes | N-TXA1-011 | none | NATIVE |
| TXA1-F09 | Extract tax from a tax-included price | 1 | FUNCTION MAPPING REQUIRED | Prices that contain tax | N-TXA1-070 | none | NATIVE |
| TXA1-F10 | Choose price-included or price-excluded per tax and per company | 6 | FUNCTION MAPPING REQUIRED | Company settings; tax form | N-TXA1-068 | none | NATIVE |
| TXA1-F11 | Force all taxes to included or excluded mode for one calculation | 6 | FUNCTION MAPPING REQUIRED | Quick encoding, expenses, early-payment lines, product helpers | N-TXA1-001 N-TXA1-003 N-TXA1-070 | none | NATIVE |
| TXA1-F12 | Compute line totals with and without tax | 1 | FUNCTION MAPPING REQUIRED | Any taxed line | N-TXA1-001 N-TXA1-099 N-TXA1-108 | none | NATIVE |
| TXA1-F13 | Apply line discount before tax | 1 | FUNCTION MAPPING REQUIRED | Lines with discount | N-TXA1-027 | none | NATIVE |
| TXA1-F14 | Split global discounts, down payments and returns across taxes | 1 | FUNCTION MAPPING REQUIRED | Order discount wizard; advance invoice | N-TXA1-027 N-TXA1-028 N-TXA1-111 | none | NATIVE |
| TXA1-F15 | Reduce tax for an early-payment discount (three modes) | 1 | FUNCTION MAPPING REQUIRED | Payment term with early discount | N-TXA1-029 N-TXA1-093 | none | NATIVE |
| TXA1-F16 | Reverse-charge pair (negative-factor distribution) | 1 | FUNCTION MAPPING REQUIRED | Taxes with negative factor | N-TXA1-016 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F17 | Round each line | 6 | FUNCTION MAPPING REQUIRED | Company rounding method | N-TXA1-020 | none | NATIVE |
| TXA1-F18 | Round globally and distribute the delta | 6 | FUNCTION MAPPING REQUIRED | Default company method | N-TXA1-021 N-TXA1-022 N-TXA1-100 N-TXA1-117 | none | NATIVE |
| TXA1-F19 | Keep or discard manually edited tax amounts | 1 | FUNCTION MAPPING REQUIRED | Totals widget edit; sync | N-TXA1-024 N-TXA1-023 N-TXA1-032 N-TXA1-109 | none | NATIVE |
| TXA1-F20 | Cash rounding of document totals | 6 | FUNCTION MAPPING REQUIRED | Invoice cash rounding field | N-TXA1-026 | none | NATIVE |
| TXA1-F21 | Document tax totals by tax group and subtotal | 1 | FUNCTION MAPPING REQUIRED | Order, invoice, printed documents | N-TXA1-025 | none | NATIVE |
| TXA1-F22 | Distribute tax amount over base and tax distribution lines with account | 1 | FUNCTION MAPPING REQUIRED | Posting of any taxed document | N-TXA1-030 N-TXA1-101 | none | NATIVE |
| TXA1-F23 | Attach tax grid tags to base and tax items (including product tags) | 1 | FUNCTION MAPPING REQUIRED | Posting of any taxed document | N-TXA1-031 | none | NATIVE |
| TXA1-F24 | Generate and synchronise tax journal items on draft documents | 1 | FUNCTION MAPPING REQUIRED | Editing a draft document | N-TXA1-032 N-TXA1-110 | none | NATIVE |
| TXA1-F25 | Suppress zero-amount tax items | 3 | FUNCTION MAPPING REQUIRED | Zero-rated and exempt taxes | N-TXA1-033 | none | NATIVE |
| TXA1-F26 | Allocate analytic split to tax items | 1 | FUNCTION MAPPING REQUIRED | Lines with analytic distribution | N-TXA1-034 | none | NATIVE |
| TXA1-F27 | Recognise tax on payment (cash basis) | 1 | FUNCTION MAPPING REQUIRED | Taxes flagged on payment; reconciliation | N-TXA1-036 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F28 | Tax closing flag per distribution line and month-end settlement of tax accounts | 1 | FUNCTION MAPPING REQUIRED | Not available as a routine | N-TXA1-038 | STATUTORY CHECK PENDING (TXS) | NATIVE GAP / EXTENSION REQUIRED |
| TXA1-F29 | Query base-to-tax item mapping for tax reporting | 9 | FUNCTION MAPPING REQUIRED | Tax reports | N-TXA1-039 | none | NATIVE |
| TXA1-F30 | Legacy single-line tax computation API | 1 | FUNCTION MAPPING REQUIRED | Product forms, event pricing, stock price, loyalty | N-TXA1-003 N-TXA1-090 | none | NATIVE |
| TXA1-F31 | Client-side preview of tax results | 1 | FUNCTION MAPPING REQUIRED | Form editing | N-TXA1-004 | none | NATIVE |
| TXA1-F32 | Guard tax lifecycle: archive, delete, company change, used flag, change log | 1 | FUNCTION MAPPING REQUIRED | Tax maintenance | N-TXA1-107 N-TXA1-095 N-TXA1-094 N-TXA1-123 | none | NATIVE |
| TXA1-F33 | Enforce tax and tax group constraints | 1 | FUNCTION MAPPING REQUIRED | Tax maintenance | N-TXA1-095 N-TXA1-036 N-TXA1-035 | none | NATIVE |
| TXA1-F34 | Load or reload taxes from a chart template | 1 | FUNCTION MAPPING REQUIRED | Module install; settings; reload | N-TXA1-096 N-TXA1-042 N-TXA1-037 | none | NATIVE |
| TXA1-F35 | Apply sales VAT on sales order lines | 2 | FUNCTION MAPPING REQUIRED | Order line entry | N-TXA1-041 N-TXA1-002 N-TXA1-025 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F36 | Apply sales VAT on customer invoice lines | 2 | FUNCTION MAPPING REQUIRED | Invoice line entry; invoice from order | N-TXA1-102 N-TXA1-040 N-TXA1-047 N-TXA1-075 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F37 | Apply purchase VAT on purchase order lines | 2 | FUNCTION MAPPING REQUIRED | Order line entry | N-TXA1-041 N-TXA1-002 N-TXA1-025 N-TXA1-082 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F38 | Apply purchase VAT on vendor bill lines | 2 | FUNCTION MAPPING REQUIRED | Bill line entry | N-TXA1-040 N-TXA1-102 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F39 | Default tax from the product, and from the company into new products | 2 | FUNCTION MAPPING REQUIRED | Product creation; chart load | N-TXA1-045 N-TXA1-042 N-TXA1-093 N-TXA1-041 | none | NATIVE |
| TXA1-F40 | Default tax from the ledger account | 2 | FUNCTION MAPPING REQUIRED | Bill and invoice lines without product | N-TXA1-044 N-TXA1-040 | none | NATIVE |
| TXA1-F41 | Default tax from the partner (through fiscal position) | 8 | FUNCTION MAPPING REQUIRED | Any document | N-TXA1-081 N-TXA1-106 N-TXA1-115 | none | PARTIAL |
| TXA1-F42 | Default tax from the company at document level (quick encoding) | 8 | FUNCTION MAPPING REQUIRED | Quick encoding mode | N-TXA1-043 N-TXA1-040 N-TXA1-042 | none | NATIVE |
| TXA1-F43 | Quick encoding by typed total with frequent tax suggestion | 2 | FUNCTION MAPPING REQUIRED | Quick encoding mode | N-TXA1-043 N-TXA1-070 | none | NATIVE |
| TXA1-F44 | Apply tax on delivery charge lines | 2 | FUNCTION MAPPING REQUIRED | Add shipping | N-TXA1-041 N-TXA1-086 N-TXA1-047 | none | NATIVE |
| TXA1-F45 | Apply tax on loyalty reward and discount lines | 2 | FUNCTION MAPPING REQUIRED | Apply reward | N-TXA1-027 N-TXA1-012 | none | NATIVE |
| TXA1-F46 | Apply tax on expense claims | 2 | FUNCTION MAPPING REQUIRED | Expense entry and posting | N-TXA1-048 | none | NATIVE |
| TXA1-F47 | Represent standard-rated VAT (7 percent purchase and sale) | 3 | FUNCTION MAPPING REQUIRED | Thai chart load | N-TXA1-050 N-TXA1-054 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F48 | Represent zero-rated treatment (0 percent purchase and sale) | 3 | FUNCTION MAPPING REQUIRED | Thai chart load | N-TXA1-051 N-TXA1-033 N-TXA1-054 N-TXA1-118 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F49 | Represent exempt treatment (0 percent exempt purchase and sale) | 3 | FUNCTION MAPPING REQUIRED | Thai chart load | N-TXA1-052 N-TXA1-033 N-TXA1-054 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F50 | Partly deductible vendor-bill lines routed to a private-share account | 3 | FUNCTION MAPPING REQUIRED | Vendor bill line column | N-TXA1-060 N-TXA1-104 N-TXA1-061 N-TXA1-113 N-TXA1-062 N-TXA1-063 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F51 | Capitalise taxes without account into inventory cost | 3 | GRV-F04 | Purchase receipt valuation | N-TXA1-064 N-TXA1-003 N-TXA1-065 | none | NATIVE |
| TXA1-F52 | Prohibited or non-claimable input VAT as a distinct tax treatment with return-grid exclusion | 3 | FUNCTION MAPPING REQUIRED | Not available | N-TXA1-052 N-TXA1-104 N-TXA1-056 N-TXA1-121 | STATUTORY CHECK PENDING (TXS) | NATIVE GAP / EXTENSION REQUIRED |
| TXA1-F53 | Withholding tax computed on purchase documents at posting | 3 | FUNCTION MAPPING REQUIRED | Select the tax on a bill line | N-TXA1-053 N-TXA1-080 N-TXA1-013 N-TXA1-036 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F54 | Withholding tax suffered on sales documents | 3 | FUNCTION MAPPING REQUIRED | Select the tax on an invoice line | N-TXA1-053 N-TXA1-013 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F55 | Choose withholding tax from payee type (company, individual, foreign) | 3 | FUNCTION MAPPING REQUIRED | Not available (manual selection) | N-TXA1-049 N-TXA1-053 N-TXA1-083 | STATUTORY CHECK PENDING (TXS) | NATIVE GAP / EXTENSION REQUIRED |
| TXA1-F56 | Withholding tax registered at payment time | 3 | FUNCTION MAPPING REQUIRED | Not installed | N-TXA1-019 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F57 | Lock the company price-inclusion default after invoicing | 6 | FUNCTION MAPPING REQUIRED | Company settings | N-TXA1-069 | none | NATIVE |
| TXA1-F58 | Adapt unit price when a fiscal position maps included taxes | 6 | FUNCTION MAPPING REQUIRED | Product price and order line | N-TXA1-086 N-TXA1-071 | none | NATIVE |
| TXA1-F59 | Show amounts with and without tax on products and documents | 6 | FUNCTION MAPPING REQUIRED | Product form; invoice print | N-TXA1-072 | none | NATIVE |
| TXA1-F60 | Compute tax amounts in document currency and company currency | 6 | FUNCTION MAPPING REQUIRED | Foreign-currency documents | N-TXA1-108 N-TXA1-105 N-TXA1-073 | none | NATIVE |
| TXA1-F61 | Select, store, refresh and protect the invoice currency rate | 6 | FUNCTION MAPPING REQUIRED | Invoice date change; post | N-TXA1-075 N-TXA1-114 N-TXA1-109 | none | NATIVE |
| TXA1-F62 | Order-level currency rate (sales and purchase) | 6 | FUNCTION MAPPING REQUIRED | Order creation | N-TXA1-075 N-TXA1-074 N-TXA1-119 | none | NATIVE |
| TXA1-F63 | Look up and apply exchange rates with fallback | 6 | FUNCTION MAPPING REQUIRED | Any foreign-currency conversion | N-TXA1-076 N-TXA1-090 | none | NATIVE |
| TXA1-F64 | Automatic exchange-rate feed | 6 | FUNCTION MAPPING REQUIRED | Not available | N-TXA1-076 N-TXA1-122 | STATUTORY CHECK PENDING (TXS) | NATIVE GAP / EXTENSION REQUIRED |
| TXA1-F65 | Tax-point date for tax and rate (taxable supply date) | 5 | FUNCTION MAPPING REQUIRED | Document form | N-TXA1-079 N-TXA1-075 | STATUTORY CHECK PENDING (TXS) | NATIVE GAP / EXTENSION REQUIRED |
| TXA1-F66 | Display tax in company currency on foreign sale documents | 6 | FUNCTION MAPPING REQUIRED | Invoice print | N-TXA1-074 N-TXA1-059 | none | NATIVE |
| TXA1-F67 | Exchange-difference accounts and currency precision guard | 6 | FUNCTION MAPPING REQUIRED | Settlement; currency maintenance | N-TXA1-077 N-TXA1-078 | none | NATIVE |
| TXA1-F68 | Company tax settings and defaults | 8 | FUNCTION MAPPING REQUIRED | Accounting settings | N-TXA1-020 N-TXA1-068 N-TXA1-042 N-TXA1-091 N-TXA1-037 N-TXA1-074 N-TXA1-067 N-TXA1-092 | none | NATIVE |
| TXA1-F69 | Resolve the fiscal position for a document | 8 | FUNCTION MAPPING REQUIRED | Order, invoice, agreement, replenishment | N-TXA1-106 N-TXA1-081 N-TXA1-085 N-TXA1-115 N-TXA1-082 N-TXA1-111 N-TXA1-087 | none | PARTIAL |
| TXA1-F70 | Map taxes through a fiscal position | 8 | FUNCTION MAPPING REQUIRED | After default tax selection | N-TXA1-083 N-TXA1-040 | none | NATIVE |
| TXA1-F71 | Map ledger accounts through a fiscal position | 8 | FUNCTION MAPPING REQUIRED | Account selection on lines | N-TXA1-083 N-TXA1-046 | none | NATIVE |
| TXA1-F72 | Foreign-VAT fiscal positions and foreign tax creation | 8 | FUNCTION MAPPING REQUIRED | Cross-border, foreign-owned structures | N-TXA1-084 | none | NATIVE |
| TXA1-F73 | Guard tax country consistency on documents | 8 | FUNCTION MAPPING REQUIRED | Posting and editing | N-TXA1-088 N-TXA1-041 | none | NATIVE |
| TXA1-F74 | Validate partner VAT number | 8 | FUNCTION MAPPING REQUIRED | Partner save | N-TXA1-089 N-TXA1-081 N-TXA1-019 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F75 | Scope taxes and rates to the company tree | 8 | FUNCTION MAPPING REQUIRED | Any tax read | N-TXA1-090 | none | NATIVE |
| TXA1-F76 | Restrict tax maintenance by role | 8 | FUNCTION MAPPING REQUIRED | Tax maintenance | N-TXA1-097 | none | NATIVE |
| TXA1-F77 | Exclude tax from stock valuation and cost-of-goods entries | 2 | FUNCTION MAPPING REQUIRED | Customer invoice posting; bill posting | N-TXA1-067 N-TXA1-066 | none | NATIVE |
| TXA1-F78 | Print tax labels, legal notes and group totals on invoices | 4 | FUNCTION MAPPING REQUIRED | Invoice print | N-TXA1-059 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F79 | Move taxed entries clear of the tax lock date | 5 | PCO-F01 | Posting; edit posted line | N-TXA1-098 | none | NATIVE |
| TXA1-F80 | Classify taxes for electronic invoices (category and exemption codes) | 9 | FUNCTION MAPPING REQUIRED | E-invoice export | N-TXA1-058 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F81 | Select Thai invoice layout and branch label | 4 | FUNCTION MAPPING REQUIRED | Invoice print for Thai companies | N-TXA1-057 | STATUTORY CHECK PENDING (TXS) | PARTIAL |
| TXA1-F82 | Convert any business record into a neutral base line and tax line description | 1 | FUNCTION MAPPING REQUIRED | Every taxed document | N-TXA1-002 N-TXA1-015 N-TXA1-018 N-TXA1-023 N-TXA1-020 | none | NATIVE |
| TXA1-F83 | Compute document untaxed, tax and total amounts and identify tax items | 1 | FUNCTION MAPPING REQUIRED | Journal item changes | N-TXA1-025 N-TXA1-032 N-TXA1-024 | none | NATIVE |
| TXA1-F84 | Load the Thai template with tax defaults | 8 | FUNCTION MAPPING REQUIRED | Module install on a Thai company | N-TXA1-112 N-TXA1-049 N-TXA1-103 N-TXA1-054 N-TXA1-037 N-TXA1-050 N-TXA1-055 N-TXA1-120 | STATUTORY CHECK PENDING (TXS) | NATIVE |
| TXA1-F85 | Issue debit notes and re-apply tax tags to existing items | 4 | FUNCTION MAPPING REQUIRED | Not installed | N-TXA1-019 | STATUTORY CHECK PENDING (TXS) | UNKNOWN |

## REGISTER: Business Rules

| BR-ID | Rule (neutral) | Condition | Neutral-refs | Class |
|---|---|---|---|---|
| TXA1-BR01 | A tax has one computation type: percentage, fixed, percentage-included division, or group; no formula type in the installed set | always | N-TXA1-005 N-TXA1-019 | Calculation |
| TXA1-BR02 | A tax is selectable for sales, purchases or none; none is usable only inside a group | always | N-TXA1-006 N-TXA1-035 | Constraint |
| TXA1-BR03 | Taxes are applied in ascending sequence, ties by creation order; fixed first, then included, then excluded | always | N-TXA1-008 N-TXA1-009 | Calculation |
| TXA1-BR04 | Group members replace the group and are sorted by their own sequence at the group's position | tax group on a line | N-TXA1-009 N-TXA1-035 | Calculation |
| TXA1-BR05 | Same-type, same-inclusion, same-base-flag taxes are computed as one batch | always | N-TXA1-010 | Calculation |
| TXA1-BR06 | A base-affecting tax adds its amount to the base of later taxes unless they opt out | include-in-base flag set | N-TXA1-011 | Configuration |
| TXA1-BR07 | Fixed tax = quantity x amount with the sign of the unit price, not reduced by discount | fixed tax | N-TXA1-012 | Calculation |
| TXA1-BR08 | Exclusive percentage tax = base x percent / 100 (base includes propagated extra base) | percentage tax, price-excluded | N-TXA1-013 | Calculation |
| TXA1-BR09 | Inclusive percentage tax = base x percent / (100 + batch percent total); base = price minus batch tax | percentage tax, price-included | N-TXA1-070 | Calculation |
| TXA1-BR10 | Division tax uses the divided base; inclusive division tax = base x percent / 100 | division tax | N-TXA1-014 N-TXA1-070 | Calculation |
| TXA1-BR11 | Line discount reduces the unit price before taxes | discount on line | N-TXA1-027 | Calculation |
| TXA1-BR12 | Negative-factor taxes create a mirrored reverse-charge entry and are never price-included | distribution with negative factor | N-TXA1-016 | Calculation |
| TXA1-BR13 | A line may force total-included or total-excluded reading of every tax | special mode set | N-TXA1-001 N-TXA1-003 | Configuration |
| TXA1-BR14 | Whether a price includes tax: tax override, else company default (tax excluded) | always | N-TXA1-068 | Default |
| TXA1-BR15 | The company price-inclusion default cannot change after invoicing started | company has accounting | N-TXA1-069 | Constraint |
| TXA1-BR16 | Expense claims are read as tax-included whatever the company default | expense module installed | N-TXA1-048 | Calculation |
| TXA1-BR17 | Rounding method follows the company setting (default global); each step rounds in the precision of its currency | always | N-TXA1-020 N-TXA1-078 | Default |
| TXA1-BR18 | Global rounding rounds each tax total once and spreads the delta; included taxes round base plus tax and derive the base | round globally | N-TXA1-021 N-TXA1-022 | Calculation |
| TXA1-BR19 | Per-line rounding rounds tax amounts and raw base at calculation | round per line | N-TXA1-020 | Calculation |
| TXA1-BR20 | Manual tax amounts are kept unless currency or document type changes or taxes-affecting lines change | draft document edited | N-TXA1-032 N-TXA1-109 N-TXA1-024 N-TXA1-023 | Calculation |
| TXA1-BR21 | Totals are grouped by tax group in group order with optional subtotal labels | always | N-TXA1-025 | Calculation |
| TXA1-BR22 | Cash rounding adds a line or changes the largest tax; nothing happens for biggest-tax strategy without a tax | cash rounding set | N-TXA1-026 | Calculation |
| TXA1-BR23 | Global discounts and down payments are split across taxes; fixed taxes are not discounted | discount or advance applied | N-TXA1-027 N-TXA1-028 N-TXA1-012 | Calculation |
| TXA1-BR24 | Early-payment discount tax treatment follows the payment term mode | payment term with early discount | N-TXA1-029 | Configuration |
| TXA1-BR25 | Each tax has mirrored invoice and credit-note distribution lines with one base line and totals of 100 percent | always | N-TXA1-030 N-TXA1-101 | Constraint |
| TXA1-BR26 | A distribution-line account cannot be receivable, payable or off-balance; missing account falls back to the base account | always | N-TXA1-030 | Constraint |
| TXA1-BR27 | Tax tags attach from distribution lines, product tags and preceding base-affecting taxes; cash-basis tags attach at payment | always | N-TXA1-031 N-TXA1-036 | Calculation |
| TXA1-BR28 | Selectable tags are limited to no-country, fiscal-country and foreign-VAT-country tags | tax maintenance | N-TXA1-031 | Constraint |
| TXA1-BR29 | Zero-amount tax items are not created; zero-rated and exempt sales keep only base items with tags | zero-amount tax | N-TXA1-033 | Calculation |
| TXA1-BR30 | Tax items are merged by partner, currency, analytic, account, taxes, distribution line and group | always | N-TXA1-032 | Calculation |
| TXA1-BR31 | Tax items inherit analytic split only for analytic-cost taxes or non-closing lines | analytic distribution present | N-TXA1-034 | Calculation |
| TXA1-BR32 | Draft documents re-synchronise tax items; posted documents do not | draft document | N-TXA1-032 N-TXA1-110 | Calculation |
| TXA1-BR33 | A tax belongs to one tax group; default group is first of its country, else without country | tax created without group | N-TXA1-035 N-TXA1-054 | Default |
| TXA1-BR34 | Tax names are unique per usage, scope and country across the company tree | tax create or rename | N-TXA1-095 | Constraint |
| TXA1-BR35 | A cash-basis tax needs a reconcilable transition account; the company switch cannot be disabled while one exists | cash-basis tax | N-TXA1-036 N-TXA1-037 | Constraint |
| TXA1-BR36 | Customer lines default to product sales taxes else account sale taxes; vendor lines symmetric; then company filter and fiscal position mapping | line tax recompute | N-TXA1-040 N-TXA1-102 | Default |
| TXA1-BR37 | Order lines take product taxes only (no account taxes), mapped by the order's fiscal position | sale or purchase order line | N-TXA1-041 | Default |
| TXA1-BR38 | The company default sale and purchase taxes seed new products; line-level defaults do not read them | product creation | N-TXA1-042 N-TXA1-045 N-TXA1-040 | Default |
| TXA1-BR39 | Quick encoding falls back to journal-account taxes, then company default tax | quick encoding mode | N-TXA1-043 | Default |
| TXA1-BR40 | Combo products carry no taxes | product type combo | N-TXA1-045 N-TXA1-041 | Default |
| TXA1-BR41 | Order taxes travel unchanged to invoice lines with engine data | invoice from order | N-TXA1-047 N-TXA1-075 | Calculation |
| TXA1-BR42 | Order-line taxes are limited to sale-type taxes of the order's tax country | sale order line | N-TXA1-041 N-TXA1-088 | Constraint |
| TXA1-BR43 | A document may not keep taxes of another country than its tax country | post or edit document | N-TXA1-088 | Constraint |
| TXA1-BR44 | Fiscal position resolution order: partner, delivery address, manual position, country, automatic candidates with tests | document partner or address change | N-TXA1-106 N-TXA1-081 | Calculation |
| TXA1-BR45 | A fiscal position replaces taxes by listed replacements and swaps accounts by mapping; no position leaves taxes unchanged | position present | N-TXA1-083 | Calculation |
| TXA1-BR46 | When mapped taxes are price-included the unit price is adapted symmetrically | fiscal position maps included taxes | N-TXA1-086 | Calculation |
| TXA1-BR47 | Foreign tax IDs on positions need country, state within fiscal country, and are unique per country | foreign VAT position | N-TXA1-084 | Constraint |
| TXA1-BR48 | Partner VAT check in the installed set is a stub; VAT presence means set and not a slash | always | N-TXA1-089 N-TXA1-081 | Risk |
| TXA1-BR49 | Vendor-bill lines may be partly deductible (0 to 100); the private share and its taxes go to the journal's private-share account | vendor bill line deductibility below 100 | N-TXA1-060 N-TXA1-104 N-TXA1-063 | Configuration |
| TXA1-BR50 | Totals show non-deductible tax separately | private-share lines present | N-TXA1-061 | Calculation |
| TXA1-BR51 | Receipt cost excludes taxes whose distribution lines have an account and includes taxes without account | purchase receipt valuation | N-TXA1-064 N-TXA1-003 | Calculation |
| TXA1-BR52 | Cost-of-goods entries are untaxed and exist only for real-time valuation products | customer invoice posting, real-time valuation | N-TXA1-067 | Calculation |
| TXA1-BR53 | Foreign-amount base and tax are divided by the line rate to get company amounts; each currency is rounded separately | foreign-currency line | N-TXA1-105 N-TXA1-073 N-TXA1-108 | Calculation |
| TXA1-BR54 | Invoice rate = rate at invoice date (today if empty), refreshable, positive, manual edits protected | invoice or receipt | N-TXA1-075 N-TXA1-114 | Calculation |
| TXA1-BR55 | Orders use their own order-date rate; the invoice created from an order recomputes its rate at invoice date | order to invoice | N-TXA1-075 | Calculation |
| TXA1-BR56 | Rate lookup falls back to earliest rate then 1.0; no installed feed; no rate rows in this database | any conversion | N-TXA1-076 | Risk |
| TXA1-BR57 | Rates and cash-basis switch live on the root company; branches share them | company tree | N-TXA1-090 | Constraint |
| TXA1-BR58 | Foreign sale documents may show tax in company currency (company flag on by default) | foreign-currency sale document | N-TXA1-074 | Configuration |
| TXA1-BR59 | A currency precision cannot be reduced once used in entries | currency maintenance | N-TXA1-078 | Constraint |
| TXA1-BR60 | Taxable supply date has no logic; rate date is the invoice date | always | N-TXA1-079 N-TXA1-075 | Risk |
| TXA1-BR61 | A used tax cannot be deleted and its company cannot change; archiving is not guarded; sales-order-only use does not count | tax maintenance | N-TXA1-107 N-TXA1-095 N-TXA1-094 | Constraint |
| TXA1-BR62 | Chart reload skips changed taxes unless forced; forced reload renames the old tax and creates a new one | chart template reload | N-TXA1-096 | Calculation |
| TXA1-BR63 | Only the accounting administrator role creates, edits or deletes taxes, groups, distribution lines and fiscal positions | always | N-TXA1-097 | Constraint |
| TXA1-BR64 | Tax visibility is limited to the user's allowed companies and their parents | always | N-TXA1-090 | Constraint |
| TXA1-BR65 | Non-sale taxed documents are moved to the first open day under a tax lock; posted taxed lines are protected | tax lock date set | N-TXA1-098 | Constraint |
| TXA1-BR66 | The Thai template recognises all 18 taxes at invoicing, uses only generic engine features and ships no fiscal position | Thai chart loaded | N-TXA1-103 N-TXA1-049 N-TXA1-050 N-TXA1-037 | Configuration |
| TXA1-BR67 | Zero and exempt Thai taxes have no template group and fall to the first withholding group | Thai chart loaded | N-TXA1-054 N-TXA1-051 N-TXA1-052 | Risk |
| TXA1-BR68 | Sale withholding taxes are forced price-excluded; purchase withholding follows the company default | Thai chart loaded | N-TXA1-053 N-TXA1-080 | Risk |
| TXA1-BR69 | Withholding tax is selected manually per line; no payee-driven selection exists | Thai chart loaded | N-TXA1-053 N-TXA1-049 | Risk |
| TXA1-BR70 | Without a category code the e-invoice exporter infers exempt for a domestic zero-amount tax | e-invoice export | N-TXA1-058 | Risk |
| TXA1-BR71 | Legal notes of taxes and fiscal positions print on invoices; Thai taxes have none | invoice print | N-TXA1-059 | Configuration |

## REGISTER: Source and Override Map

Described generically: where the base behaviour lives and which other installed capabilities extend it. Exact locations are kept in the restricted layer.

| Concept | Base behaviour (generic) | Extensions in installed capabilities (generic) | Effective-behaviour condition | Neutral-refs |
|---|---|---|---|---|
| Tax record, constraints and lifecycle | Accounting core, tax model | Expense, purchase and e-invoicing capabilities extend the tax model; the sales capability does not; formula-defined taxes and payment-time withholding exist only as optional add-ons that are not installed | Accounting core plus three extensions | N-TXA1-095 N-TXA1-107 N-TXA1-058 N-TXA1-094 N-TXA1-019 |
| Tax calculation core | Accounting core, calculation routine | None among installed capabilities; the formula add-on would extend it but is not installed | Base only | N-TXA1-099 N-TXA1-009 N-TXA1-010 N-TXA1-011 N-TXA1-019 |
| Base-line and tax-line preparation hooks | Accounting core | Expense capability carries the expense reference through lines and grouping keys | Base plus expense extension | N-TXA1-002 N-TXA1-048 |
| Per-document line producers | Accounting core for journal items | Sales order, purchase order and expense each have their own producer; expense also overrides the journal item producer | Each document type has its own producer, calculation shared | N-TXA1-002 N-TXA1-048 |
| Rounding and totals | Accounting core | None; callers are invoices, sales orders and purchase orders | Base only | N-TXA1-100 N-TXA1-025 |
| Tax journal item generation and synchronisation | Accounting core | None; expense extends grouping keys | Base plus expense keys | N-TXA1-033 N-TXA1-032 N-TXA1-048 |
| Non-deductible handling | Accounting core | None; the client-side mirror lacks it | Accounting core only | N-TXA1-060 N-TXA1-104 N-TXA1-061 N-TXA1-004 |
| Default tax on journal items | Accounting core | None | Accounting core only | N-TXA1-102 N-TXA1-040 |
| Default tax on sales order lines | Sales capability | Loyalty rewards, delivery charges and project stock moves | Sales plus loyalty, delivery and project stock | N-TXA1-041 N-TXA1-027 |
| Default tax on purchase order lines | Purchase capability | Purchase agreements, service resale and replenishment | Purchase plus agreements, resale and replenishment | N-TXA1-041 N-TXA1-082 |
| Default tax on products | Accounting core | None; company defaults come from company settings | Accounting core only | N-TXA1-045 N-TXA1-042 |
| Fiscal position finder and mapping | Accounting core | None | Accounting core only | N-TXA1-106 N-TXA1-083 N-TXA1-081 |
| Fiscal position on documents | Accounting core | Sales and purchase orders each resolve their own | Each document type resolves its own | N-TXA1-115 N-TXA1-082 |
| Product accounts | Accounting core | Stock accounting and manufacturing accounting | Accounting plus stock and manufacturing accounting | N-TXA1-046 |
| Company tax fields and settings | Accounting core | None | Accounting core only | N-TXA1-042 N-TXA1-020 N-TXA1-068 N-TXA1-037 N-TXA1-091 |
| VAT-number validation | Accounting core stub | A VAT-validation add-on exists but is not installed | Stub effective | N-TXA1-089 N-TXA1-019 |
| Currency conversion and rate lookup | Base platform | Accounting precision guard; pricelist side effect; no rate feed | Base plus accounting guard | N-TXA1-076 N-TXA1-078 |
| Invoice currency rate | Accounting core | None | Accounting core only | N-TXA1-075 N-TXA1-114 |
| Taxable supply date | Accounting core stub | None; the Thai module does not implement it | Stub effective | N-TXA1-079 |
| Cash rounding | Accounting core | None | Accounting core only | N-TXA1-026 |
| Chart template loading of taxes | Accounting core loader | Thai data; sales down-payment account property; stock accounting accounts | Loader plus Thai data plus two extensions | N-TXA1-096 N-TXA1-042 N-TXA1-049 |
| Invoice document selection | Accounting core | Thai module for companies whose fiscal country is Thailand | Thai fiscal-country companies | N-TXA1-057 |
| Tax cost in stock valuation | Purchase and stock accounting | Valuation entries and price-difference entries | Purchase stock plus stock accounting | N-TXA1-064 N-TXA1-067 N-TXA1-066 |
| Client-side calculation mirror | Web client helper | None | Web client | N-TXA1-004 |
| E-invoice tax classification | E-invoicing capability | Tax model fields | E-invoicing installed | N-TXA1-058 |

## REGISTER: Thai Tax Record Treatment Map

Each seeded Thai tax record and the treatment it represents. No statutory correctness is asserted: every row is STATUTORY CHECK PENDING (TXS).

| Record | Usage | Percent | Treatment represented | Tax group | Base tags | Tax tag and account | Closing flag | Price-inclusion override | Neutral-refs | Statutory link |
|---|---|---|---|---|---|---|---|---|---|---|
| Standard VAT (purchase, 7 percent) | purchase | 7 | STANDARD-RATED (input) | VAT group | purchase-amount return line | input-tax line; input VAT account | true | none | N-TXA1-050 N-TXA1-054 | STATUTORY CHECK PENDING (TXS) |
| Standard VAT (sale, 7 percent) | sale | 7 | STANDARD-RATED (output) | VAT group | sales-amount return line | output-tax line; output VAT account | true | none | N-TXA1-050 N-TXA1-054 | STATUTORY CHECK PENDING (TXS) |
| Zero-rate VAT (purchase, 0 percent) | purchase | 0 | ZERO-RATED (input) | first withholding group by fallback | purchase-amount return line | input-tax line; input VAT account (zero amount item not created) | true | none | N-TXA1-051 N-TXA1-033 N-TXA1-054 | STATUTORY CHECK PENDING (TXS) |
| Zero-rate VAT (sale, 0 percent) | sale | 0 | ZERO-RATED (output) | first withholding group by fallback | sales-amount line and zero-rated sales line | output-tax line; output VAT account (zero amount item not created) | true | none | N-TXA1-051 N-TXA1-033 N-TXA1-054 | STATUTORY CHECK PENDING (TXS) |
| Exempt VAT (purchase, 0 percent) | purchase | 0 | EXEMPT (input); the Thai-language description also mentions non-claimable input tax (translation text only) | first withholding group by fallback | purchase-amount return line | input-tax line; input VAT account (zero amount item not created) | true | none | N-TXA1-052 N-TXA1-033 N-TXA1-054 | STATUTORY CHECK PENDING (TXS) |
| Exempt VAT (sale, 0 percent) | sale | 0 | EXEMPT (output) | first withholding group by fallback | sales-amount line and exempted sales line | output-tax line; output VAT account (zero amount item not created) | true | none | N-TXA1-052 N-TXA1-033 N-TXA1-054 | STATUTORY CHECK PENDING (TXS) |
| Withholding tax (purchase, -1 percent) | purchase | -1 | WITHHOLDING (company payee, rate 1) | withholding group for 1 percent | withholding income line for company payees | withholding line for company payees; withholding liability account for company payees | false | company default | N-TXA1-053 N-TXA1-080 | STATUTORY CHECK PENDING (TXS) |
| Withholding tax (purchase, -2 percent) | purchase | -2 | WITHHOLDING (company payee, rate 2) | withholding group for 2 percent | withholding income line for company payees | withholding line for company payees; withholding liability account for company payees | false | company default | N-TXA1-053 N-TXA1-080 | STATUTORY CHECK PENDING (TXS) |
| Withholding tax (purchase, -3 percent) | purchase | -3 | WITHHOLDING (company payee, rate 3) | withholding group for 3 percent | withholding income line for company payees | withholding line for company payees; withholding liability account for company payees | false | company default | N-TXA1-053 N-TXA1-080 | STATUTORY CHECK PENDING (TXS) |
| Withholding tax (purchase, -5 percent) | purchase | -5 | WITHHOLDING (company payee, rate 5) | withholding group for 5 percent | withholding income line for company payees | withholding line for company payees; withholding liability account for company payees | false | company default | N-TXA1-053 N-TXA1-080 | STATUTORY CHECK PENDING (TXS) |
| Withholding tax (purchase, -1 percent) | purchase | -1 | WITHHOLDING (individual payee, rate 1) | withholding group for 1 percent | withholding income line for individual payees | withholding line for individual payees; withholding liability account for individual payees | false | company default | N-TXA1-053 N-TXA1-080 | STATUTORY CHECK PENDING (TXS) |
| Withholding tax (purchase, -2 percent) | purchase | -2 | WITHHOLDING (individual payee, rate 2) | withholding group for 2 percent | withholding income line for individual payees | withholding line for individual payees; withholding liability account for individual payees | false | company default | N-TXA1-053 N-TXA1-080 | STATUTORY CHECK PENDING (TXS) |
| Withholding tax (purchase, -3 percent) | purchase | -3 | WITHHOLDING (individual payee, rate 3) | withholding group for 3 percent | withholding income line for individual payees | withholding line for individual payees; withholding liability account for individual payees | false | company default | N-TXA1-053 N-TXA1-080 | STATUTORY CHECK PENDING (TXS) |
| Withholding tax (purchase, -5 percent) | purchase | -5 | WITHHOLDING (individual payee, rate 5) | withholding group for 5 percent | withholding income line for individual payees | withholding line for individual payees; withholding liability account for individual payees | false | company default | N-TXA1-053 N-TXA1-080 | STATUTORY CHECK PENDING (TXS) |
| Withholding tax (sale, -1 percent) | sale | -1 | WITHHOLDING SUFFERED (sale, rate 1) | withholding group for 1 percent | no tag | no tag; creditable withholding asset account | false | tax-excluded | N-TXA1-053 | STATUTORY CHECK PENDING (TXS) |
| Withholding tax (sale, -2 percent) | sale | -2 | WITHHOLDING SUFFERED (sale, rate 2) | withholding group for 2 percent | no tag | no tag; creditable withholding asset account | false | tax-excluded | N-TXA1-053 | STATUTORY CHECK PENDING (TXS) |
| Withholding tax (sale, -3 percent) | sale | -3 | WITHHOLDING SUFFERED (sale, rate 3) | withholding group for 3 percent | no tag | no tag; creditable withholding asset account | false | tax-excluded | N-TXA1-053 | STATUTORY CHECK PENDING (TXS) |
| Withholding tax (sale, -5 percent) | sale | -5 | WITHHOLDING SUFFERED (sale, rate 5) | withholding group for 5 percent | no tag | no tag; creditable withholding asset account | false | tax-excluded | N-TXA1-053 | STATUTORY CHECK PENDING (TXS) |



---

<!-- source: TXA2_thaitax_documents_period_reversal_NEUTRAL.md -->
# TXA2 — Tax documents, dates, periods, reversal and cross-module triggers — Neutral Knowledge

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Clean-room knowledge layer for Thai Tax Core unit TXA2 (study of Odoo 19 Community behaviour).
> Describes what a ledger system does with tax documents, dates, locks, corrections, numbering, access, audit and hand-offs from business events. It states system behaviour only; statutory requirements are validated elsewhere and nothing here is a legal conclusion.
> No V-level, no Complete, no coverage percentage, no Gate PASS.

## CAP-TXA2-01 Tax document types, states and issuing identity

### WHAT
- [N-TXA2-001] The ledger distinguishes seven kinds of journal document: ordinary journal entry, customer invoice, customer credit note, vendor bill, vendor credit note, sales receipt and purchase receipt. A debit note is not one of them in the studied configuration.
- [N-TXA2-002] Every document is in exactly one of three states: draft, posted or cancelled. Payment progress is a separate derived indicator that never changes the document state.

### WHY
- [N-TXA2-003] A single ledger document model covers entries, invoices, bills, credit notes and receipts so that every tax document is subject to the same posting, numbering, locking and audit rules.

### BUSINESS RULE
- [N-TXA2-004] A document is always created in draft; it can become posted only through the posting action, never by direct creation.
- [N-TXA2-005] A credit note is produced by reversing a posted customer invoice or vendor bill: the reversal creates an opposite document of the matching credit-note type linked back to the original. Receipts reverse to credit notes of the same side.
- [N-TXA2-006] Sales receipts are available only when a setting is on (it is on in the studied database); purchase receipts are always available. Receipts take the same taxes, journal type and posting flow as invoices and bills and, as inferred from the numbering logic, share the number series of the invoices of their journal.
- [N-TXA2-007] Posting enforces completeness: a customer on invoices, a date on vendor documents, a non-negative total, at least one non-note line, an active journal and accounts, and accounts that belong to the document company tree. Receipts are validated by the same routine but, as inferred from the validation logic, are not asked for a customer.

### STATE
- [N-TXA2-008] A posted or cancelled document can be reset to draft and a draft can be cancelled; cancelling a posted document first resets it. Reset is refused for secured (hashed) documents, exchange-difference and cash-basis entries and where a localization demands a cancellation request.
- [N-TXA2-009] Cancelling an invoice removes its reconciliations but does not cancel the payments that settled it; those payments stay posted and become unreconciled.

### OPTIONALITY
- [N-TXA2-010] Sales receipts, the dedicated credit-note number series, the abnormal-document confirmation and the debit-note module are all optional; none of them is switched on by the tax localization for Thailand.

### DEPENDENCY
- [N-TXA2-011] The kind of document decides the journal type that can hold it, the numbering series, the default taxes and the print layout.

### CONSTRAINT
- [N-TXA2-012] The kind of a document can be switched between invoice and credit note only while it has never been numbered; the same action is refused for ordinary entries.

### RISK
- [N-TXA2-013] Receipts and reset-to-draft carry weaker controls than invoices: no customer is required on receipts (inferred) and resetting a posted document to draft needs only the invoicing role.

### UNKNOWN
- [N-TXA2-014] Whether a sales receipt printed from the form shows any document title, and how receipts are counted in order invoicing quantities, cannot be settled without running the system.

## CAP-TXA2-02 Tax-relevant dates: invoice date, accounting date, due date, supply and delivery dates

### WHAT
- [N-TXA2-015] Four dates matter on a tax document: the document (invoice or bill) date, the accounting date that places the entry in a period, the payment due date, and optional supply and delivery dates. Only the first two drive posting, locks and tax reporting; the other two are informational.

### WHY
- [N-TXA2-016] Dates are derived by rule so that numbers keep increasing with time and each document lands in an identifiable period.

### BUSINESS RULE
- [N-TXA2-017] The accounting date of an invoice or receipt is derived from the invoice date, not typed independently; customer documents keep the invoice date until posting, while vendor documents are moved at entry time to a date that keeps the number series increasing.
- [N-TXA2-018] At posting, an empty invoice date on a customer document is set to today; a vendor document without a bill date is refused. After posting, the invoice date and the accounting date cannot be edited.
- [N-TXA2-019] A delivery date is copied onto customer invoices created from sales orders when the delivery module is installed (it is): it is the completion date of the first customer delivery of the order. It is shown and printed only when set and is not used for locks, numbering or the accounting date.
- [N-TXA2-020] The Thai localization neither overrides nor adds any date field, date default or date validation; Thai documents use the generic date logic.
- [N-TXA2-021] The due date follows the payment term; without a term it defaults to the later of the existing value and today.
- [N-TXA2-022] A draft whose date falls inside a locked period shows a warning stating that it will be accounted on a later date when posted.

### STATE
- [N-TXA2-023] The date fields are free while the document is in draft, are frozen at posting, and the accounting date can still move during posting if a lock is violated.

### OPTIONALITY
- [N-TXA2-024] Delivery and supply dates are optional, informational and only filled by a module or a person; no switch makes them drive the accounting date for Thailand.

### DEPENDENCY
- [N-TXA2-025] The date logic depends on the sequence pattern of the journal (monthly for vendor journals, yearly for customer journals by default), on company lock dates and, for foreign-currency documents, on the rate of the invoice date.

### CONSTRAINT
- [N-TXA2-026] A vendor bill needs a bill date to be posted, a posted document cannot change its dates, and a number that no longer matches the date blocks re-posting until the number is cleared.

### RISK
- [N-TXA2-027] Two different dates can exist on a posted customer invoice (printed invoice date and ledger date) after a lock shift, and a vendor bill dated earlier in the current period is accounted on the posting day rather than on the bill date; any statutory tax-point rule must be checked against these defaults.

### UNKNOWN
- [N-TXA2-028] Which date is the statutory tax point for Thailand, and whether the generic defaults satisfy it, is a statutory question for the statutory lane; the exact accounting date chosen for each lock and numbering combination needs execution.

## CAP-TXA2-03 Lock dates, tax lock, cut-off and the absence of a tax-period object

### WHAT
- [N-TXA2-029] Five company-level lock dates freeze closed periods: a global (fiscal year) lock, a tax-return lock, a sales lock, a purchase lock and an irreversible hard lock. There is no period or tax-return object; a period is only a date range chosen when a report is run.

### WHY
- [N-TXA2-030] Locks exist so that closed periods, and tax statements already issued, are not silently changed; postponement keeps documents recordable.

### BUSINESS RULE
- [N-TXA2-031] Posting inside a locked period does not fail: the entry date is moved to the first date that no applicable lock blocks, and posting continues. This applies equally to documents created from other modules and to valuation and closing entries.
- [N-TXA2-032] Which locks apply depends on the document: the global and hard locks always; the sales lock only on customer journals; the purchase lock only on vendor journals; the tax lock only when the document touches the tax report.
- [N-TXA2-033] Editing an already posted document inside a locked period is refused: changing its date or number, resetting it to draft, changing amounts, accounts, partner or taxes, deleting its lines. The tax lock additionally protects every item that affects the tax report, even when the global lock is open.
- [N-TXA2-034] A soft lock can be relaxed for one user or for everyone by a time-limited, audited exception created by an accounting administrator and revocable by an administrator. The hard lock cannot be relaxed and cannot be lowered or removed.
- [N-TXA2-035] Copies and reversals of documents dated inside a fiscal lock are dated on the day after the user's fiscal lock; reversal of cash-basis and exchange entries when payments are undone keeps the original period unless it is locked.
- [N-TXA2-036] The tax lock date is not set by any Community routine: its help text says it is set automatically when a tax closing entry is posted, but no tax closing entry or tax return object exists in Community, so no automatic maintenance exists and no menu or setting for maintaining it was found.

### STATE
- [N-TXA2-037] A period is open until a lock date covers it; a locked period reopens for chosen users through an exception unless the hard lock covers it.

### OPTIONALITY
- [N-TXA2-038] All locks and exceptions are optional; the Thai localization sets none and the studied database has none set. The stock-valuation closing period and the audit-trail mode are separate company options.

### DEPENDENCY
- [N-TXA2-039] Locks interact with numbering (the shifted date can open a new number period), bank statement reconciliation, the hash chain and every module that creates entries; branch companies inherit the locks of their parents.

### CONSTRAINT
- [N-TXA2-040] Setting a hard lock requires that no draft document and no unreconciled bank line remains in the period; a lock never shifts a document at editing time, only at posting.

### RISK
- [N-TXA2-041] Postponing instead of refusing means a late document silently lands in a later period, which changes the tax period of its tax lines; the tax lock help text overpromises automation that does not exist; without an in-product way to maintain locks or exceptions they depend on technical access.

### UNKNOWN
- [N-TXA2-042] Whether the tax lock date can or should be maintained by users for Thailand, the exact date chosen when several locks overlap, and the effect of a shifted date on numbering, hash chains and period reports need execution and the statutory lane.

## CAP-TXA2-04 Correction of posted tax documents: reset, cancel, reverse, re-issue, copy and debit note

### WHAT
- [N-TXA2-043] To correct a posted tax document the base offers: reset to draft and edit, cancel, reverse into a credit note (optionally cancelling the original immediately and opening a new draft copy), duplicate, and, only with an optional module, a debit note. There is no native 'replacement' or 're-issued document' concept linking a new document to the one it replaces.

### WHY
- [N-TXA2-044] Corrections are made by new documents or controlled resets so that history stays traceable.

### BUSINESS RULE
- [N-TXA2-045] Resetting a posted document to draft keeps its number; the document can be edited and posted again with the same number. Reset is refused for secured documents, in a locked period and where a localization requires a cancellation request. No guard was found that refuses reset because the document is paid (inferred; to be confirmed by execution).
- [N-TXA2-046] Cancelling takes a document out of the ledger but keeps its number; cancelled documents can be reset to draft again.
- [N-TXA2-047] The reversal wizard has two buttons: 'Reverse', which creates a draft credit note to be edited and posted (partial credit by editing its lines), and 'Reverse and Create Invoice', which posts the credit note at once, reconciles it with the original and opens a new draft copy of the original lines.
- [N-TXA2-048] An invoice or bill that comes out negative when created from an order can be turned into a credit note, but only before it has ever been numbered.
- [N-TXA2-049] Duplicating a posted document creates a new draft with no link to the original and a new number at posting.
- [N-TXA2-050] A debit note, an upward correction linked to the corrected document, exists only in an optional module that is not installed: it copies a posted invoice or credit note into a new draft invoice of the matching direction, links it to the origin, and gives it its own number series with a distinguishing prefix.

### STATE
- [N-TXA2-051] Correction paths map to states as follows: a posted document goes back to draft by reset, becomes cancelled by cancel, or stays posted while an opposite credit note is created; a hashed document can only use the credit-note path.

### OPTIONALITY
- [N-TXA2-052] The abnormal-document warning, the cancel-request hook, the debit-note module and the dedicated credit-note series are optional; the immediate-cancel reversal needs a reversal date that is not in the future.

### DEPENDENCY
- [N-TXA2-053] Corrections depend on lock dates, the hash option, reconciliation state of the document, and on the order, purchase and stock links that must be unwound separately.
- [N-TXA2-054] Installed modules extend posting, resetting, cancelling and reversing with side effects on orders, timesheets, expenses, electronic documents, cost lines, emails and vehicle logs; none of these side effects is specific to Thailand.

### CONSTRAINT
- [N-TXA2-055] Only posted documents can be reversed, all documents of one reversal must share a company, the reversal journal must be of the same type as the original, and a posted document cannot be deleted before it is reset to draft.

### RISK
- [N-TXA2-056] Without a replacement link, an auditor cannot navigate from a cancelled tax document to the one that replaced it except through the number reuse, chatter and references; reset-to-draft and re-posting keeps the same number, which hides the correction unless the audit trail is read.

### UNKNOWN
- [N-TXA2-057] The effect of resetting a paid document, of cancelling a cash-basis-tax document and of reversing multi-currency originals needs execution; whether Thai practice needs a replacement concept is a statutory question.

## CAP-TXA2-05 Numbering, sequences, gaps and inalterability of tax documents

### WHAT
- [N-TXA2-058] Numbers are assigned when a document is posted, per journal, by a pattern deduced from the previous number of the same journal. Optional per-journal hashing makes posted documents tamper-evident. There is no configurable sequence object for documents in Community.

### WHY
- [N-TXA2-059] Continuous numbering and optional tamper evidence let a reviewer detect missing or altered documents.

### BUSINESS RULE
- [N-TXA2-060] Customer and vendor journals keep invoices and credit notes in separate series by default; bank journals keep payments in a separate series. Self-billing journals number per partner. Receipts and invoices share one series.
- [N-TXA2-061] The numbering period (monthly, yearly, year-range or never) is deduced from the previous number; the sequence resets accordingly and a posted number must agree with its date.
- [N-TXA2-062] A number is never given to another document after posting, so cancelling or deleting a numbered document, or leaving it in draft, leaves an irregularity that the system flags; ordinary users cannot delete a numbered document that is not the last of its series.
- [N-TXA2-063] A journal can be set to secure posted entries with a hash chain: when an entry is posted, all earlier unhashed entries of its chain are hashed. A hashed entry can no longer be reset, cancelled, deleted or altered in its integrity fields. The hash covers number, date, journal, company and, per line, label, amounts, account and partner; it does not cover taxes, tax tags, invoice date or document type.
- [N-TXA2-064] A journal can carry a custom number format expression; non-administrators must then respect it when typing a number.

### STATE
- [N-TXA2-065] A document has no number in draft, receives it at its first posting, keeps it through reset, cancellation and reposting, and may additionally become secured.

### OPTIONALITY
- [N-TXA2-066] Dedicated credit-note and payment series, billing on behalf of the vendor, the regex override and the hash option are per-journal options; none of them is enabled by the Thai localization, and the studied database has only the default credit-note and payment series.

### DEPENDENCY
- [N-TXA2-067] Numbering depends on the accounting date, which depends on locks and the invoice date; and on the company fiscal-year end for staggered years.

### CONSTRAINT
- [N-TXA2-068] Numbers are unique among posted documents of a journal; a posted number must agree with its date; documents cannot move to another journal after numbering without clearing the number.

### RISK
- [N-TXA2-069] Because the hash omits taxes, tags and invoice date, a secured document can still have its tax classification touched by tools that bypass the normal record checks; the statutory Thai tax-invoice numbering rules (continuity, per-branch or per-point-of-sale series, separate series by document type) are not modelled and must be validated separately.

### UNKNOWN
- [N-TXA2-070] The first number generated for a Thai company's journals and the exact reuse behaviour after cancellation need execution; statutory numbering requirements belong to the statutory lane.

## CAP-TXA2-06 Tax journal entries: tax lines, tags, cash basis, withholding, reversal and re-tagging

### WHAT
- [N-TXA2-071] Tax lines and their tax-report tags are created while a document is in draft, are frozen when it is posted, and are changed afterwards only by reversal or by an optional administrator tool. Posting itself does not create tax lines. Payments create tax lines only for cash-basis taxes and for the optional payment-time withholding module.

### WHY
- [N-TXA2-072] Tags on tax lines are what places each amount in the tax report; freezing them at posting makes reports reproducible.

### BUSINESS RULE
- [N-TXA2-073] Each tax line and each taxed base line receives the tax-report tags of the tax distribution that matches the document (invoice or credit note); tags are taken only when the tax is due on the invoice or cash-basis tags are requested.
- [N-TXA2-074] Once posted, a tax line cannot be changed or deleted by hand; changing taxes needs a reset to draft (refused in a locked period) or a reversal.
- [N-TXA2-075] Cash-basis taxes are an optional per-tax mode: the tax sits on a transition account until the document is reconciled with a payment, when a cash-basis entry moves it to the real tax account and keeps the tax base. They are not used by any Thai tax in the studied configuration.
- [N-TXA2-076] An optional module, not installed here, lets withholding be registered at payment: the withholding tax then ignores document computation and is booked on the payment entry as a withholding line with a mandatory withholding number, a base pair and a reduced cash amount.
- [N-TXA2-077] Reversal of a taxed document recomputes tax lines with the credit-note distribution of the same taxes; reversal of an ordinary entry with taxes negates amounts directly. Reversal does not copy stock or cost-of-sales lines unless it is the cancelling reversal.
- [N-TXA2-078] An optional administrator tool, not installed here, rewrites the tax-report tags on existing journal items from a chosen date so that they match the current tax configuration. It is irreversible, bypasses the normal write checks and the lock dates, leaves no log, and refuses configurations where a child tax has several parents.

### STATE
- [N-TXA2-079] Tax lines go through: created in draft, fixed at posting, mirrored by the credit note, moved at reconciliation (cash-basis only), re-tagged by the optional tool.

### OPTIONALITY
- [N-TXA2-080] Cash basis, payment-time withholding and the re-tagging tool are all optional; the Thai localization uses ordinary negative-percentage taxes booked at posting for withholding.

### DEPENDENCY
- [N-TXA2-081] Tax lines depend on the taxes of the lines (product, account or fiscal position), the repartition configuration, the price-included setting, rounding and currency rate, and the lock dates.

### CONSTRAINT
- [N-TXA2-082] A posted item cannot change taxes; a tax line cannot be deleted by hand; cash-basis taxes need a reconcilable transition account; payment-time withholding needs a positive base and a number.

### RISK
- [N-TXA2-083] The re-tagging tool and any direct database change alter tax history without trace; withholding booked at posting is recognised before payment; no tax closing entry exists to settle the tax accounts.

### UNKNOWN
- [N-TXA2-084] Numeric tax results with rounding and currency, tag polarity on credit notes, and behaviour of cash-basis entries on reversal need execution; whether bank-statement reconciliation models can add taxed lines is not read.

## CAP-TXA2-07 Multi-company isolation, access groups and record rules for tax and fiscal records

### WHAT
- [N-TXA2-085] Tax and fiscal configuration and documents are isolated by company: documents by the company of their journal, configuration records by the company tree, so a branch may use the configuration of its parent. Access is split between an invoicing role, an administrator role, read-only roles and operational roles in sales and purchasing.

### WHY
- [N-TXA2-086] Roles and company boundaries limit who can create, post, correct and configure tax records.

### BUSINESS RULE
- [N-TXA2-087] With the accounting application alone only two roles are meant to be used: Invoicing (create, edit, post, pay) and Administrator (configuration and exceptions); the other accounting groups give shallow read access.
- [N-TXA2-088] Record rules narrow what operational roles see: salespeople see only customer invoices and credit notes (their own unless they have the all-leads right), purchasing users only vendor documents (including purchase receipts), invoicing users everything, portal users their own non-draft invoices and bills but not receipts.
- [N-TXA2-089] Posting needs the invoicing role, but reset to draft and cancel carry no role check in code, only in the view; documents created from sales orders are created with elevated rights so that a salesperson need not hold the invoicing role.
- [N-TXA2-090] Community contains no automatic inter-company invoice or order mirroring; the only inter-company mechanism found is the payment-clearing add-on, which posts clearing entries when a payment taken by one company settles an invoice of another.

### STATE
- [N-TXA2-091] Not applicable as a state machine; visibility changes with company selection, role and record-rule combination.

### OPTIONALITY
- [N-TXA2-092] Multi-company behaviour exists only when more than one company or branch is configured; the studied database has one company.

### DEPENDENCY
- [N-TXA2-093] Lock dates and exceptions are inherited down the branch tree; tax and journal configuration is shared up the tree; sequences are per journal and hence per company.

### CONSTRAINT
- [N-TXA2-094] A document, its journal, accounts, fiscal position and taxes must belong to the same company tree; accounts of another tree block posting.

### RISK
- [N-TXA2-095] Several additive record rules apply to one user (invoicing see-all plus sales or purchase rules); a role with no read rule for receipts (sales) may not see them; segregation between creating, posting, resetting and cancelling documents is weak because only posting is enforced in code.

### UNKNOWN
- [N-TXA2-096] Effective visibility for users holding several roles, branch and parent behaviour, and cross-company reporting cannot be observed in a single-company database.

## CAP-TXA2-08 Audit trail for tax-relevant records: tracking, chatter, deletion and attachment rules

### WHAT
- [N-TXA2-097] Tax-relevant changes are traced through field tracking on documents, journal items, taxes, partners, journals and the company, through chatter messages for state changes and reversals, and through guards on deleting records and attachments when the restrictive audit trail option is on.

### WHY
- [N-TXA2-098] An audit trail lets authorities and reviewers reconstruct changes; the restrictive option prevents loss of that record.

### BUSINESS RULE
- [N-TXA2-099] With the restrictive audit trail option a document that has been posted once can no longer be deleted (it can only be cancelled), the audit messages of documents, taxes, partners, accounts and the company cannot be deleted, and invoice PDFs and e-invoice files are detached rather than deleted. The option is off in the studied database and not forced by the Thai localization.
- [N-TXA2-100] State changes and corrections write notes on both documents involved: the reversal on the original and on the copy, the securing of an entry, the creation of a lock exception on the company, and the creation of a debit note or duplicate.
- [N-TXA2-101] No record of who read or printed a tax document is kept by the accounting application, and invoice date, due date, delivery date and fiscal position changes in draft are not tracked.

### STATE
- [N-TXA2-102] Not applicable as a state machine.

### OPTIONALITY
- [N-TXA2-103] Restrictive audit trail, the hash option, tracking-disable contexts and force-delete are the switches that change how much is recorded and protected.

### DEPENDENCY
- [N-TXA2-104] The audit of locks depends on date tracking; the audit of re-tagging does not exist; chatter retention depends on the audit-trail option.

### CONSTRAINT
- [N-TXA2-105] Restricted logs cannot be deleted; hashed entries cannot be altered or deleted; posted items cannot be deleted before the entry is reset.

### RISK
- [N-TXA2-106] Bypass contexts (force delete, tracking disable, bypass of audit, ignore tax lock) exist for code paths and imports; raw SQL tools leave no trace; draft-stage edits of the dates and fiscal position that decide the tax period are not tracked.

### UNKNOWN
- [N-TXA2-107] Retention of chatter in the studied configuration, and the completeness of the log for documents edited through import or external code, need execution.

## CAP-TXA2-09 Cross-module triggers into taxed documents: sales, purchase, inventory, expenses, payments

### WHAT
- [N-TXA2-108] Taxed documents are produced from sales orders, purchase orders, expense claims and (in the periodic valuation used here) from period-end closing. Each source passes currency, fiscal position, partner, payment term, line taxes and analytic distribution, but none passes an invoice date or a tax-point date; the delivery module adds a delivery date.
- [N-TXA2-109] Vendor bills created from purchase orders carry currency, fiscal position, partner, bank account, payment term and the order lines' taxes, with no bill date; the bill date must be entered before posting.

### WHY
- [N-TXA2-110] Taxed documents should be produced from business events with the same taxes, fiscal position and currency the business decided on, not retyped.

### BUSINESS RULE
- [N-TXA2-111] Inventory events create tax-neutral ledger lines. With perpetual valuation, posting a customer invoice adds cost-of-sales lines for eligible products; with periodic valuation (the studied configuration) no cost lines are added at invoicing and cost enters through a period-end closing entry. Neither carries document taxes.
- [N-TXA2-112] Employee expense claims paid by the employee are posted as purchase receipts partnered with the employee, dated today, created and posted with elevated rights; the supplier of the expense is not the partner of the document. Company-paid expenses create payment entries with taxes computed by the engine.
- [N-TXA2-113] The Thai localization sets the default sales and purchase taxes of the company to Output VAT 7% and Input VAT 7%, so documents created without an explicit tax pick them up through the product or account.

### STATE
- [N-TXA2-114] Orders drive documents forward but documents do not drive orders back except through invoiced quantity: a draft invoice already counts as invoiced and a cancelled one does not.

### OPTIONALITY
- [N-TXA2-115] Automatic invoicing after payment, the valuation mode, the anglo-saxon flag and the closing period are company or parameter options; the studied configuration has them off, periodic and manual.

### DEPENDENCY
- [N-TXA2-116] The tax outcome of a sales or purchase document depends on the fiscal position resolved at order level, the taxes stored on order lines at order time, and the date on which the document is posted.

### CONSTRAINT
- [N-TXA2-117] Documents of different fiscal positions or currencies from sales are never merged; vendor bills need a user with create rights; transfers cannot be dated inside a fiscal or hard lock.

### RISK
- [N-TXA2-118] Taxes and fiscal position are copied from the order and are not recomputed when the invoice is posted later or in another period; a delivery in one period and posting in another yields the invoice-date period, not the delivery period; returned goods do not produce a credit note by themselves; online payment can post invoices automatically.

### UNKNOWN
- [N-TXA2-119] Behaviour of manufacturing entries, landed costs, subcontracting and timesheet or expense re-invoicing for taxes was not read; perpetual-valuation cost lines are RT; bank statement reconciliation models that add taxed lines were not read.

## CAP-TXA2-10 Document presentation of tax documents: titles, report selection, stored PDFs

### WHAT
- [N-TXA2-120] A customer invoice prints with a document title that depends on type and state, in the language of the partner. For a company whose fiscal country is Thailand a different print layout is used whose invoice title for posted customer invoices is a fixed text, together with the buyer's branch label; a separate Commercial Invoice print exists for Thai customer-journal documents.

### WHY
- [N-TXA2-121] A tax document must be presentable in the form the local market expects; localization modules may substitute the print layout.

### BUSINESS RULE
- [N-TXA2-122] Core titles: Invoice (posted), Draft Invoice, Cancelled Invoice, Credit Note (posted or draft or cancelled), Vendor Credit Note, Vendor Bill, Self Billing variants; proforma variants when printing a proforma. Receipts have no title branch.
- [N-TXA2-123] In the Thai layout the title of a posted customer invoice is replaced by the fixed text Tax Invoice; draft, cancelled and credit note documents keep their core titles, so a Thai credit note prints Credit Note and a draft invoice prints Draft Invoice. The title text does not depend on any setting and its language follows the partner language only through translation of the fixed source text.
- [N-TXA2-124] A separate Commercial Invoice print is offered for Thai customer-journal documents; it renders the standard invoice document (not the Thai tax-invoice layout) in the partner language and refuses to print documents that are not invoices or receipts.
- [N-TXA2-125] Which print template is used for sending is chosen by partner, then journal, then the default invoice report; a generated PDF is stored on the document and detached when the document is reset to draft.
- [N-TXA2-126] The printed date block shows the invoice date with a type-specific label, the due date for posted customer invoices only, the supply date and delivery date only when set.
- [N-TXA2-127] A payment receipt is a separate printable document with a fixed generic title; it lists the invoices settled, with date, number and amounts, and shows no tax breakdown.

### STATE
- [N-TXA2-128] The title changes with the state: draft, posted and cancelled customer invoices print different titles; the stored PDF follows the posted document.

### OPTIONALITY
- [N-TXA2-129] The Thai layout depends only on the company fiscal country; the amount-in-words block, the payment QR block, the commercial invoice and the debit-note titles are separate options.

### DEPENDENCY
- [N-TXA2-130] Presentation depends on the company fiscal country, the partner language, the partner company registry and the optional debit-note module.

### CONSTRAINT
- [N-TXA2-131] The Commercial Invoice cannot be printed for entries or non-invoice documents.

### RISK
- [N-TXA2-132] The layout cannot be driven by the language or by document type; Thai statutory presentation (title wording per document kind, original or copy marking, seller branch, abbreviated or combined formats) is not modelled; the Thai text is a translation of a fixed English source string.

### UNKNOWN
- [N-TXA2-133] Rendered output (fonts, Thai text, number-in-words) needs execution; statutory content requirements are for the statutory lane.

## REGISTER: Function Catalog

| Cat-ID | Function (neutral name) | Topic # | Existing Function-ID or FUNCTION MAPPING REQUIRED | Neutral statements | Statutory link | Native status |
|---|---|---|---|---|---|---|
| TXA2-F01 | Issue and post a customer tax document (invoice) | 4, 5 | FUNCTION MAPPING REQUIRED | N-TXA2-004, N-TXA2-007, N-TXA2-018, N-TXA2-108 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F02 | Capture and post a vendor bill | 4, 5 | FUNCTION MAPPING REQUIRED | N-TXA2-004, N-TXA2-007, N-TXA2-018, N-TXA2-017, N-TXA2-109 | TXS pending (statutory need not derived from system behaviour) | NATIVE |
| TXA2-F03 | Credit note by reversal (customer and vendor) | 4, 7 | SDV-F07 | N-TXA2-005, N-TXA2-047 | TXS pending (statutory need not derived from system behaviour) | NATIVE |
| TXA2-F04 | Reverse and re-issue in one step (cancel with new draft copy) | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-047, N-TXA2-054 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F05 | Debit note issuance and numbering | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-001, N-TXA2-050 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F06 | Sales and purchase receipt document types | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-001, N-TXA2-006, N-TXA2-007, N-TXA2-014, N-TXA2-112 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F07 | Replacement / re-issued tax document concept (cross-referenced replacement) | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-043, N-TXA2-047 | TXS pending (statutory need not derived from system behaviour) | NATIVE GAP / EXTENSION REQUIRED |
| TXA2-F08 | Reset to draft and cancel of a posted document | 4, 7 | FUNCTION MAPPING REQUIRED | N-TXA2-008, N-TXA2-045, N-TXA2-046, N-TXA2-089 | none | NATIVE |
| TXA2-F09 | Derivation of invoice date, accounting date and due date | 5 | PCO-F04 | N-TXA2-015, N-TXA2-017, N-TXA2-018, N-TXA2-021 | TXS pending (statutory need not derived from system behaviour) | NATIVE |
| TXA2-F10 | Tax-point (supply or delivery) date handling | 5, 12 | PCO-F04 | N-TXA2-015, N-TXA2-019, N-TXA2-020 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F11 | Company lock dates, lock exceptions and hard lock | 5 | PCO-F01 | N-TXA2-029, N-TXA2-032, N-TXA2-034, N-TXA2-039 | none | NATIVE |
| TXA2-F12 | Postponement of entries that fall inside a locked period | 5, 7 | PCO-F01 | N-TXA2-031, N-TXA2-035, N-TXA2-022, N-TXA2-023 | none | NATIVE |
| TXA2-F13 | Refusal of edits to posted documents inside a locked period | 5, 7 | PCO-F01 | N-TXA2-033, N-TXA2-032 | none | NATIVE |
| TXA2-F14 | Tax period or tax-return period object and period closing | 5 | PCO-F02 | N-TXA2-029, N-TXA2-036 | TXS pending (statutory need not derived from system behaviour) | NATIVE GAP / EXTENSION REQUIRED |
| TXA2-F15 | Tax lock date maintenance (automatic at tax closing) | 5 | PCO-F01 | N-TXA2-036 | TXS pending (statutory need not derived from system behaviour) | NATIVE GAP / EXTENSION REQUIRED |
| TXA2-F16 | Fiscal year configuration for numbering | 5 | PCO-F02 | N-TXA2-029 | none | PARTIAL |
| TXA2-F17 | Cut-off of transfers against fiscal and hard locks | 5, 12 | PCO-F04 | N-TXA2-035 | none | PARTIAL |
| TXA2-F18 | Document numbering per journal, series and period | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-058, N-TXA2-060, N-TXA2-061, N-TXA2-062, N-TXA2-064 | TXS pending (statutory need not derived from system behaviour) | NATIVE |
| TXA2-F19 | Sequence gap detection and resequencing | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-062, N-TXA2-063 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F20 | Hash inalterability of posted documents (optional per journal) | 4, 10 | FUNCTION MAPPING REQUIRED | N-TXA2-063, N-TXA2-047 | TXS pending (statutory need not derived from system behaviour) | NATIVE |
| TXA2-F21 | Tax line and tag generation on documents | 7 | FUNCTION MAPPING REQUIRED | N-TXA2-071, N-TXA2-073, N-TXA2-074 | none | NATIVE |
| TXA2-F22 | Cash-basis tax entries at reconciliation | 7 | FUNCTION MAPPING REQUIRED | N-TXA2-075, N-TXA2-073 | none | NATIVE |
| TXA2-F23 | Withholding tax registered at payment time (optional module) | 7 | FUNCTION MAPPING REQUIRED | N-TXA2-076 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F24 | Re-tagging of tax-report tags on existing entries (optional tool) | 7 | FUNCTION MAPPING REQUIRED | N-TXA2-078 | none | PARTIAL |
| TXA2-F25 | Settlement and closing of tax accounts | 7 | FUNCTION MAPPING REQUIRED | N-TXA2-073, N-TXA2-036 | TXS pending (statutory need not derived from system behaviour) | NATIVE GAP / EXTENSION REQUIRED |
| TXA2-F26 | Reversal of tax effects (credit note, unreconcile) | 7 | SDV-F07 | N-TXA2-073, N-TXA2-047, N-TXA2-077, N-TXA2-075 | none | NATIVE |
| TXA2-F27 | Multi-company isolation of tax documents and configuration | 10 | MCT-F03 | N-TXA2-085 | none | NATIVE |
| TXA2-F28 | Access roles and record rules for tax documents | 10 | FUNCTION MAPPING REQUIRED | N-TXA2-087, N-TXA2-088, N-TXA2-089 | none | PARTIAL |
| TXA2-F29 | Audit trail by field tracking and chatter | 10 | RCN-F02 | N-TXA2-097, N-TXA2-100, N-TXA2-103, N-TXA2-028 | none | NATIVE |
| TXA2-F30 | Backdating audit (lock exception audit view) | 5, 10 | RCN-F02 | N-TXA2-100, N-TXA2-034 | none | PARTIAL |
| TXA2-F31 | Restrictive audit trail and attachment protection (optional) | 10 | FUNCTION MAPPING REQUIRED | N-TXA2-099, N-TXA2-101 | none | NATIVE |
| TXA2-F32 | Order-to-invoice hand-off of tax data (sales) | 12 | PDT-F01 | N-TXA2-108, N-TXA2-048 | none | NATIVE |
| TXA2-F33 | Order-to-bill hand-off of tax data (purchase) | 12 | PDT-F02 | N-TXA2-109, N-TXA2-048 | none | NATIVE |
| TXA2-F34 | Inventory-to-ledger triggers (cost lines, closing, date check) | 12 | SDV-F05 | N-TXA2-111, N-TXA2-054 | none | NATIVE |
| TXA2-F35 | Expense-claim receipts and their tax lines | 12 | FUNCTION MAPPING REQUIRED | N-TXA2-112, N-TXA2-054 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F36 | Online-payment driven invoice posting and reconciliation | 12 | FUNCTION MAPPING REQUIRED | N-TXA2-108 | none | NATIVE |
| TXA2-F37 | Return after invoicing: credit note raised separately | 4, 12 | SDV-F07 | N-TXA2-108, N-TXA2-048 | none | PARTIAL |
| TXA2-F38 | Thai tax-invoice print layout, fixed title and buyer branch | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-120, N-TXA2-122, N-TXA2-123, N-TXA2-124, N-TXA2-125, N-TXA2-126, N-TXA2-132 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F39 | Inter-company payment clearing | 10, 12 | FUNCTION MAPPING REQUIRED | N-TXA2-090 | none | PARTIAL |
| TXA2-F40 | Side effects of posting, reset, cancel and reversal in installed modules | 12 | FUNCTION MAPPING REQUIRED | N-TXA2-054 | none | NATIVE |

## REGISTER: Business Rules

| BR-ID | Rule (neutral) | Condition / configuration | Neutral statements | Class |
|---|---|---|---|---|
| TXA2-BR-01 | A document is always created in draft and becomes posted only through the posting action by a user with the invoicing role. | always | N-TXA2-004 | FACT |
| TXA2-BR-02 | Posting refuses a negative total, a missing customer on invoices, a missing bill date on vendor documents, documents without lines, archived journals or accounts and accounts of another company tree. | always (receipts are not asked for a customer, inferred) | N-TXA2-007, N-TXA2-018, N-TXA2-085 | FACT |
| TXA2-BR-03 | A credit note is a reversal of a posted invoice or bill, linked to the original, of the matching type; receipts reverse to credit notes of their side. | always | N-TXA2-005 | FACT |
| TXA2-BR-04 | The reversal can be taken as a draft credit note to edit and post, or as an immediately posted and reconciled credit note with a new draft copy of the original. | reversal date not in the future for the immediate option | N-TXA2-047 | FACT |
| TXA2-BR-05 | A reversal of a posted invoice sets the credit note date and invoice date to the date chosen in the wizard. | always | N-TXA2-047 | FACT |
| TXA2-BR-06 | No document or field links a re-issued tax document to the document it replaces. | always (negative search) | N-TXA2-043, N-TXA2-047 | INFERENCE |
| TXA2-BR-07 | A debit note exists only in an optional module that is not installed; when installed it copies a posted document into a linked draft with its own numbering prefix. | optional module installed | N-TXA2-001, N-TXA2-050 | FACT |
| TXA2-BR-08 | Sales receipts need a setting (on in the studied database); purchase receipts are always available; receipts share the number series of invoices and use the same taxes and posting flow. | setting for sales receipts | N-TXA2-006 | FACT |
| TXA2-BR-09 | Receipts print without a document title in the core layout. | core invoice layout | N-TXA2-014 | INFERENCE |
| TXA2-BR-10 | Resetting a posted document to draft keeps its number and is refused for hashed documents, cash-basis and exchange entries, localizations demanding a cancellation request, and locked periods. | always | N-TXA2-008, N-TXA2-033, N-TXA2-045 | FACT |
| TXA2-BR-11 | Cancelling a document keeps its number and removes its reconciliations but leaves the settling payments posted and unreconciled. | always | N-TXA2-008, N-TXA2-046, N-TXA2-009 | FACT |
| TXA2-BR-12 | Reset to draft and cancel carry no role check in code; only the view limits the buttons to the invoicing role. | always | N-TXA2-089, N-TXA2-008, N-TXA2-045 | FACT |
| TXA2-BR-13 | The accounting date of a customer document equals its invoice date until posting; for vendor documents it is derived from the bill date to keep the number series increasing. | always | N-TXA2-017 | FACT |
| TXA2-BR-14 | An empty invoice date on a customer document becomes today at posting; a vendor document needs a bill date. | always | N-TXA2-018 | FACT |
| TXA2-BR-15 | Invoice date, accounting date, partner, lines, payment terms, currency and fiscal position cannot be edited after posting. | always | N-TXA2-018 | FACT |
| TXA2-BR-16 | Delivery date is copied from the first completed customer delivery of the order onto customer invoices when the delivery module is installed and is informational only. | delivery module installed | N-TXA2-019 | FACT |
| TXA2-BR-17 | The supply (tax-point) date field exists but is empty and hidden in the base and in the Thai localization. | always | N-TXA2-015, N-TXA2-019, N-TXA2-020 | FACT |
| TXA2-BR-18 | Posting inside a locked period moves the date to the first date not blocked by the applicable locks instead of refusing. | always | N-TXA2-031 | FACT |
| TXA2-BR-19 | Which locks apply depends on journal type and tax impact: global and hard always, sales on customer journals, purchase on vendor journals, tax only for tax-affecting documents. | always | N-TXA2-032 | FACT |
| TXA2-BR-20 | Editing, resetting, cancelling or deleting a posted document inside a locked period is refused; the tax lock protects tax-affecting items even when the global lock is open. | always | N-TXA2-033 | FACT |
| TXA2-BR-21 | Soft locks can be relaxed per user or for all by time-boxed exceptions created by accounting administrators; the hard lock cannot be relaxed, lowered or removed. | always | N-TXA2-034 | FACT |
| TXA2-BR-22 | The tax lock date is not maintained automatically: no tax closing entry exists to set it. | always | N-TXA2-036 | INFERENCE |
| TXA2-BR-23 | There is no tax period or tax return object; a period is a date range chosen when a report is run. | always | N-TXA2-029 | INFERENCE |
| TXA2-BR-24 | Lock dates and exceptions are not maintained through any menu or setting in the base application. | always (negative search) | N-TXA2-034 | INFERENCE |
| TXA2-BR-25 | Transfers are checked only against the fiscal-year and hard locks. | stock valuation module installed | N-TXA2-035 | FACT |
| TXA2-BR-26 | Numbers are assigned at posting from the previous number of the same journal and series; customer invoices default to a yearly pattern, vendor bills to a monthly pattern. | always | N-TXA2-058, N-TXA2-060 | FACT |
| TXA2-BR-27 | Credit notes and payments get separate series by journal flag, with a distinguishing prefix, defaulting on for customer and vendor journals and bank journals. | journal flags | N-TXA2-060, N-TXA2-058 | FACT |
| TXA2-BR-28 | The Thai localization adds no numbering rule, sequence, journal option or date rule. | always | N-TXA2-060, N-TXA2-020, N-TXA2-010 | FACT |
| TXA2-BR-29 | A posted number must agree with the date period of its pattern; moving a document across periods needs the number cleared. | always | N-TXA2-061, N-TXA2-045, N-TXA2-062 | FACT |
| TXA2-BR-30 | Gaps and irregularities caused by draft, cancelled or deleted numbered documents are flagged on the journal dashboard; deletion of numbered documents that are not last in their series is restricted. | always | N-TXA2-062 | FACT |
| TXA2-BR-31 | An optional per-journal hash chain makes posted documents unalterable in number, date, journal, company and line label, amounts, account and partner; taxes, tags and invoice date are not covered. | journal option on | N-TXA2-063 | FACT |
| TXA2-BR-32 | Tax lines and tags are computed in draft and frozen at posting; taxes of posted items cannot change and tax lines cannot be deleted by hand. | always | N-TXA2-071, N-TXA2-033, N-TXA2-074 | FACT |
| TXA2-BR-33 | Tags follow the tax distribution for invoice or credit note when the tax is due on invoice or cash-basis tags are requested. | always | N-TXA2-073 | FACT |
| TXA2-BR-34 | Withholding in the Thai tax set is an ordinary negative tax booked at posting, not at payment. | Thai chart loaded | N-TXA2-073 | FACT |
| TXA2-BR-35 | Cash-basis taxes sit on a transition account until reconciliation and are then moved by a cash-basis entry; no Thai tax uses this. | tax set to payment basis | N-TXA2-075 | FACT |
| TXA2-BR-36 | Payment-time withholding exists only in an optional module that is not installed; it requires a withholding number and ignores the tax in document computation. | optional module installed | N-TXA2-076 | FACT |
| TXA2-BR-37 | An optional tool rewrites tax tags on existing items from a date, irreversibly, without lock checks or log. | optional module installed | N-TXA2-078 | FACT |
| TXA2-BR-38 | Documents are isolated by company; tax and fiscal configuration is shared up the company tree. | always | N-TXA2-085 | FACT |
| TXA2-BR-39 | Only invoicing and administrator roles are intended with the accounting application alone; operational roles are narrowed by record rules. | always | N-TXA2-087, N-TXA2-088 | FACT |
| TXA2-BR-40 | Documents created from sales orders are created with elevated rights; vendor bills from purchase orders with the user's own rights. | sales or purchasing installed | N-TXA2-089, N-TXA2-109 | FACT |
| TXA2-BR-41 | Field tracking and chatter record document and tax changes; line changes are logged only after the document was posted once. | always | N-TXA2-097 | FACT |
| TXA2-BR-42 | With the restrictive audit trail option, posted-once entries are cancelled rather than deleted and audit messages and attachments are protected; the option is off in the studied database. | option on | N-TXA2-099 | FACT |
| TXA2-BR-43 | Sales and purchase hand-offs copy taxes, fiscal position, currency and analytic distribution from the order but pass no invoice date. | always | N-TXA2-108, N-TXA2-109 | FACT |
| TXA2-BR-44 | Invoices from sales are merged only for the same company, partner, shipping partner, currency and fiscal position; bills from purchases by company, partner and currency. | always | N-TXA2-108, N-TXA2-109 | FACT |
| TXA2-BR-45 | Draft and posted invoices count as invoiced quantity on the order; cancelled ones do not; returns create no credit note. | sales installed | N-TXA2-108 | FACT |
| TXA2-BR-46 | Cost lines and closing entries created from inventory carry no document taxes; with periodic valuation no cost lines are created at invoicing. | stock valuation installed | N-TXA2-111 | FACT |
| TXA2-BR-47 | Online payment confirmation posts the linked draft invoices automatically and reconciles payments; automatic invoicing after payment is off unless a parameter is set. | payment modules installed | N-TXA2-108 | FACT |
| TXA2-BR-48 | Employee-paid expenses are posted as purchase receipts partnered with the employee and dated today. | expense module installed | N-TXA2-112 | FACT |
| TXA2-BR-49 | The Thai print layout is selected by company fiscal country; the title of a posted customer invoice is a fixed text; credit notes and drafts keep core titles; a Commercial Invoice print exists. | company fiscal country is Thailand | N-TXA2-120, N-TXA2-123, N-TXA2-124 | FACT |
| TXA2-BR-50 | The in-payment status is not reachable in the base application. | always | N-TXA2-002 | INFERENCE |

## REGISTER: State and Reversal

| Document or entity | State or event | Trigger | Reversal, cancel or correction path | Blocked when | Neutral statements |
|---|---|---|---|---|---|
| Customer invoice | draft -> posted | Post / Confirm by invoicing user; online payment confirmation; auto-post cron | Reset to draft (if allowed) or credit note | negative total; no customer; vendor needs bill date; inactive journal or account; hashed or locked states block later reversal only | N-TXA2-004, N-TXA2-007, N-TXA2-108 |
| Customer invoice | posted -> draft | Reset to Draft | Repost keeps the same number | hash; cash-basis or exchange entry; cancel-request localization; date inside fiscal or sale or hard lock or tax lock for tax items | N-TXA2-008, N-TXA2-033, N-TXA2-045 |
| Customer invoice | posted -> cancelled | Cancel (via reset to draft) | Reset to draft again | same as reset; payments stay posted | N-TXA2-008, N-TXA2-009, N-TXA2-046 |
| Customer invoice | posted + credit note | Reverse / Credit Note button | Credit note is itself reversible; replacement via new draft copy | original not posted; selection spans companies; journal type mismatch | N-TXA2-005, N-TXA2-055 |
| Vendor bill | draft -> posted | Post; auto-complete from purchase order | Reset to draft or vendor credit note | bill date missing; negative total; locked period shifts date | N-TXA2-018, N-TXA2-048, N-TXA2-031 |
| Customer / vendor credit note | draft -> posted (+ reconcile with original) | Post of reversal draft or immediate-cancel reversal | Reset to draft (not hashed); new invoice | negative total; lock shift; original not posted | N-TXA2-047 |
| Sales / purchase receipt | draft -> posted | Post | Reversal through the wizard from a list (no Credit Note button); reset or cancel as invoices | receipt customer not enforced (inference); no title on print | N-TXA2-006, N-TXA2-014, N-TXA2-007, N-TXA2-005 |
| Debit note (optional module) | draft linked to origin -> posted | Debit Note wizard then Post | Reverse via credit note; debit of debit refused | module not installed in studied database; origin not posted or already debited | N-TXA2-001, N-TXA2-050 |
| Journal entry with taxes | posted -> reversed | Reverse Entry (wizard); cancel or immediate reversal | Reversal entry posted and reconciled | hash; locked period | N-TXA2-077, N-TXA2-047, N-TXA2-008 |
| Hashed document | secured | Hash on post or on demand | Only credit note or reversal | reset, cancel, delete, hash-field edit, line deletion | N-TXA2-063, N-TXA2-008, N-TXA2-047 |
| Cash-basis tax entry | created / reversed | Reconcile / unreconcile payment | Reversal created automatically on unreconcile | cannot be reset to draft | N-TXA2-075, N-TXA2-008 |
| Company lock date | set / lowered / removed | Company record update (programmatic) | Soft lock: exception or lowering; hard lock: none | hard lock lowering or removal; hard lock with drafts; fiscal or hard lock with unreconciled statement lines | N-TXA2-034, N-TXA2-029 |
| Lock exception | create / revoke / expire | Created programmatically by an accounting administrator; revoked by an administrator | Revoke; expires automatically | more than one lock field; copy; non-manager revoke | N-TXA2-034 |
| Numbered document | delete | Delete by user | Reverse instead; administrators may delete with warning | not last in chain for non-administrators; posted lines; audit trail on; hashed | N-TXA2-062, N-TXA2-055, N-TXA2-099, N-TXA2-033 |
| Draft dated inside a lock | post | Post | Date shifted instead of refused | none (shift) ; edits afterwards refused | N-TXA2-031, N-TXA2-022 |
| Stock closing entry | create / post | Manual action or valuation cron | Reverse by dated entry or cancel | fiscal or hard lock shifts the date; cron skips manual-period companies | N-TXA2-111, N-TXA2-031 |
| Order invoiced quantity | draft invoice counted; cancelled invoice not counted | Invoice create / cancel | Credit note lowers invoiced quantity | receipts not counted (inference) | N-TXA2-108, N-TXA2-014 |
| Expense receipt | create and post | Expense approval | Cancel or reversal clears the expense link | none specific | N-TXA2-112, N-TXA2-054 |
| Tax tags on existing items | rewritten | Optional re-tag tool | None (irreversible) | only multi-parent child taxes block; no lock check | N-TXA2-078 |
| Payment-time withholding (optional) | registered on payment | Payment register | Payment cancel or unreconcile (behaviour unknown) | negative-or-zero base; missing number | N-TXA2-076 |

## REGISTER: Accounting Impact

| Event | Entries created or changed | Tax lines, tags and accounts affected | Period, lock and date effect | Reversal effect | Neutral statements |
|---|---|---|---|---|---|
| Draft created or edited (invoice, bill, receipt) | No posted entry; draft items and tax lines synchronised on each edit | Tax lines and tags computed in draft from line taxes; Thai VAT lines to the output or input VAT accounts, withholding lines to the withholding accounts | Date derived from invoice date; lock-shift alert shown for dates that will be moved | Delete or cancel the draft; nothing in ledger | N-TXA2-071, N-TXA2-073, N-TXA2-022 |
| Post customer invoice | Invoice entry (receivable, revenue, tax); cost-of-sales pair only for perpetual valuation (RT; periodic in the studied database) | Output VAT line (account 213200, grid labels 1 and 5); withholding sale lines to 114300; tags frozen | Date = invoice date, shifted if inside a lock; number assigned; hash if journal option | Credit note or reset to draft | N-TXA2-071, N-TXA2-073, N-TXA2-111, N-TXA2-031, N-TXA2-058 |
| Post vendor bill | Bill entry (expense, tax, payable); price-difference lines only with anglo-saxon flag (RT) | Input VAT line (114200, labels 6 and 7); withholding purchase lines to 213302 or 213301 reduce the payable | Accounting date derived from bill date (max with today in period), shifted by locks | Vendor credit note or reset to draft | N-TXA2-073, N-TXA2-017, N-TXA2-111, N-TXA2-031 |
| Post credit note (reversal) | Reversal entry with refund distribution; reconciled with the original | Same VAT or withholding accounts and grid labels as invoices (refund distribution) | Reversal date from wizard; shifted by fiscal lock at copy and by tax or fiscal locks at post | New invoice or reset to draft | N-TXA2-073, N-TXA2-047, N-TXA2-035 |
| Reverse and re-issue | Credit note posted and reconciled; new draft copy of the original lines | Credit note tax lines as above; new draft recomputes taxes | Wizard date for credit note and draft; future date blocks immediate cancel | Cancel the new draft; reverse the credit note by a new invoice | N-TXA2-047 |
| Reset to draft | Posted entry becomes draft; cost-of-sales lines and analytic lines removed; PDF detached | Tax lines remain on the draft and can be edited; tags recomputed on edit | Refused when date or tax items are inside a lock; number kept | Repost | N-TXA2-008, N-TXA2-054, N-TXA2-045, N-TXA2-033 |
| Cancel | Entry leaves the ledger; reconciliations removed; settling payments stay posted | Tax lines no longer in posted ledger; number kept | Same lock refusals as reset | Reset to draft | N-TXA2-008, N-TXA2-009, N-TXA2-046 |
| Register payment on invoice | Payment entry on outstanding account; reconciliation partials; possible exchange difference | No tax lines on the payment (base); cash-basis entry only for payment-basis taxes (none in Thai set); optional withholding module adds tax lines | Payment date; lock checks as any entry; cash-basis entry dated max(settlement, day after lock) | Unreconcile reverses cash-basis and exchange entries; cancel keeps payments posted | N-TXA2-076, N-TXA2-075, N-TXA2-009 |
| Online payment confirmed | Draft invoices linked to the transaction posted; payment created and reconciled | Taxes as on the invoice | Posting date = today unless locked | Credit note | N-TXA2-108 |
| Withholding registered at payment (optional module) | Payment entry with cash net of withholding, tax item, base and counterpart | Tax lines and base lines from the withholding tax tags; number required | Payment date | Payment cancel or unreconcile (unknown) | N-TXA2-076 |
| Tax tag update tool (optional) | No entry; tag links rewritten for items dated on or after the chosen date | Tags replaced with those of current tax configuration | Operates regardless of lock dates (warning only) | Irreversible except from backup | N-TXA2-078 |
| Stock closing entry (periodic valuation) | Entry in the stock journal for valuation and cost variation | No document taxes | Dated at the chosen closing date or today; shifted if inside fiscal or hard lock; cron posts | Reverse by dated entry | N-TXA2-111, N-TXA2-031 |
| Expense claim approved (own account) | Purchase receipt posted, partner = employee | Input tax lines from expense taxes, expense account; supplier not on receipt (inference) | invoice date set to today; accounting date derived | Cancel or reversal clears expense link | N-TXA2-112 |
| Down-payment invoice and final invoice | Down-payment invoice with order taxes; final invoice negates the down-payment lines | Tax lines for down payment and their negation on the final invoice | Dates as invoices | Credit note of either | N-TXA2-108 |
| Secure entries (hash) | No accounting change; hash stored; note logged | None; tags and taxes not hashed | Unreconciled lines or gaps block hashing | None; credit note only | N-TXA2-063 |
| Lock date set or relaxed | No entry; exceptions logged on company | Tax lock protects tax items | Later postings shift; edits refused | Soft: exception or lower; hard: none | N-TXA2-029, N-TXA2-034, N-TXA2-033 |
| Resequence numbers | Names of posted entries rewritten | None | Refused inside lock or for hashed documents sorted by date | Resequence again | N-TXA2-063, N-TXA2-033 |



---

<!-- source: TXC_thaitax_schema_dump_reconciliation_NEUTRAL.md -->
# TXC — Thai tax capability: stored information and constraints — Neutral Knowledge

> Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**
> Layer: neutral knowledge (clean-room). Source basis: Odoo 19 Community, revision 19.0.post20260921, static review of data declarations and one restored configuration-only database. No runtime proof. No statutory conclusion is drawn here.
> Scope: what information the Thai-tax execution path must store, how those pieces relate, how they change over time and which rules protect them. Unit TXC; neutral ids N-TXC-###.
> This file contains no technical names; the restricted technical evidence file holds the mappings.


## CAP-TXC-01 Tax definition and classification data

### WHAT

- [N-TXC-001] The tax capability keeps a catalogue of tax definitions. Each definition records a name, a calculation method (percentage, fixed amount, or a group of other taxes), a rate, whether it applies to sales, purchases or neither, a scope label, the country and company it belongs to, an active flag and a position in the calculation order.
- [N-TXC-002] Every tax definition belongs to exactly one tax group. A group is a presentation and settlement bucket: it carries the accounts used for tax payable, tax receivable and advance tax payment, an optional country and company, a position, and a label that precedes it on documents.
- [N-TXC-003] Each tax definition owns an ordered list of distribution lines, kept separately for invoices and for credit notes. A distribution line states whether it targets the base amount or the tax amount, the percentage of the tax it carries, an optional destination account, an optional flag that includes it in the periodic tax closing, and zero or more reporting tags.
- [N-TXC-004] Reporting tags are labels with an applicability (for taxes or for accounts), an optional country and a name. They attach to distribution lines, to journal item lines, to accounts and to products so that returns can collect base and tax amounts by label. Name, applicability and country together are unique at database level.

### WHY

- [N-TXC-074] Separating the definition, the group and the distribution lets one tax feed the document total, the correct ledger accounts and the correct return boxes, and lets value-added and withholding taxes share one mechanism.

### BUSINESS RULE

- [N-TXC-005] Whether a tax is price-inclusive is decided per definition by an optional override with a company-wide default behind it; the effective flag is derived and is not stored as an independent input.
- [N-TXC-006] A tax group is mandatory. When a definition is saved without a group, the system picks the first group that matches the definition country and company, or else the first generic group.

### STATE

- [N-TXC-011] A tax definition has no workflow state; its only lifecycle control is the active flag. Distribution lines and groups have no state either.

### OPTIONALITY

- [N-TXC-007] Cash-basis recognition, where the tax becomes due on payment rather than on invoice, is selectable per definition, is only offered when the company enables it, and uses a transition account to hold amounts until payment.
- [N-TXC-008] A definition can list the original taxes it substitutes for, list replacement taxes, and be linked to fiscal positions. These are many-to-many links held in separate link tables, and are empty in the seeded configuration.

### DEPENDENCY

- [N-TXC-009] Names, descriptions, invoice labels and legal notes of tax definitions, and names of groups, tags, report lines and report columns, are stored once with all languages inside a single value rather than as one row per language.
- [N-TXC-010] Tax definitions, tax groups and distribution lines are company-scoped and protected by a company-based access rule; reporting tags and report definitions are shared across companies and carry no company-based rule.

### CONSTRAINT

- [N-TXC-012] The database declares no uniqueness or check constraint on tax definitions, groups or distribution lines. Rules such as a unique name per company, scope and country, agreement between group country and tax country, a valid cash-basis transition account, a valid distribution-line set and scope compatibility of grouped taxes are enforced by application-level checks and need runtime verification.

### RISK

- [N-TXC-013] In the seeded Thai configuration the zero-rate and exempt VAT definitions carry no group in the seed data; the group default rule gave them the first group found, which is a withholding group. Any group-based subtotal, presentation or closing setting therefore treats those VAT definitions as members of that withholding group.

### UNKNOWN

- [N-TXC-014] Whether the first-match group assignment is what users see on documents and returns cannot be determined from static evidence; it requires a runtime check.


## CAP-TXC-02 Tax return and report definition structure

### WHAT

- [N-TXC-015] Tax returns are described by report definitions made of columns, lines and expressions. A line may be a heading with child lines; an expression has an engine (collect by reporting tag, sum other lines, or take manually entered external values), a formula and a label. A report can be limited to a country and can be a variant of a root report.

### WHY

- [N-TXC-075] Describing returns as data lets the same stored tags produce different return layouts without changing stored journal data.

### BUSINESS RULE

- [N-TXC-016] The tag-collection engine identifies tags through the formula text of the expression, and the sign applied to the collected amount is derived from that expression; the tag record itself carries only a derived, non-stored negate indicator.

### STATE

- [N-TXC-017] Manually entered external report values are stored per company with a date, a value or text, and a target expression; none exist in this database.

### DEPENDENCY

- [N-TXC-019] Report, line, expression and column definitions are shared reference data without a company column; only external manual values are company-scoped.

### CONSTRAINT

- [N-TXC-018] Report lines are unique by code within a report, expressions are unique by label within a line, and an expression using the domain engine must have a sub-formula; these three rules are database constraints.

### UNKNOWN

- [N-TXC-020] How a return is rendered, filtered by fiscal position and period, and exported is outside this schema reconciliation and needs runtime verification.


## CAP-TXC-03 Fiscal position and mapping data

### WHAT

- [N-TXC-021] A fiscal position is a named rule set selected by country, country group, region, postal range, a requirement for a tax number, and an optional foreign tax number. It maps taxes (original to replacement) and accounts (source to destination), is company-scoped and can be applied automatically.
- [N-TXC-023] The Thai chart seeds no fiscal positions and no account mappings; the tables are empty in this database.

### WHY

- [N-TXC-076] Fiscal positions let the same product and price produce different tax outcomes for different customer or supplier situations.

### DEPENDENCY

- [N-TXC-022] Tax mapping is expressed by linking replacement taxes to the position and by listing original taxes on the tax definition; account mapping is a separate child list with a unique source-destination pair per position.
- [N-TXC-024] The company designates a domestic fiscal position and a fiscal position for purchase receipts. Partners hold their fiscal position as a per-company property, and sales orders, purchase orders and journal entries each store the position used.

### UNKNOWN

- [N-TXC-025] How a position is selected automatically from partner data, and its effect on tax and account substitution, is runtime behaviour outside this reconciliation.


## CAP-TXC-04 Journal entry, entry line, reconciliation and journal tax and currency data

### WHAT

- [N-TXC-026] A journal entry header stores the accounting date, the invoice date, the due date, a separate taxable-supply date and a delivery date, the document currency, a stored rate between document currency and company currency, the fiscal position, the tax country, stored untaxed, tax and total amounts with signed variants, and links to a cash-basis origin. The rounding method is read from the company and not stored, and a tax summary structure is computed on demand and is not stored.
- [N-TXC-027] Each entry line stores debit, credit, balance, a foreign-currency amount with its currency and rate, the tax that generated it, the distribution line that generated it, its tax group, the base amount for tax lines, the taxes applied to base lines, the tax tags, a parent group tax, extra tax data and a deductible amount. Line-level taxes and tags are many-to-many links.
- [N-TXC-030] A partial reconciliation stores the matched debit and credit lines, the amount in company currency and in each line currency, an optional exchange-difference entry and optional draft cash-basis values; a full reconciliation groups partial reconciliations and the lines they cover.

### WHY

- [N-TXC-077] Entry lines are the single stored basis for tax returns, so each line carries the tax, tag and currency facts needed to rebuild a return.

### BUSINESS RULE

- [N-TXC-028] Amounts are kept in both the company currency and the line currency, with the rate stored on the line and the entry, so that tax and base amounts exist in both currencies after posting.
- [N-TXC-031] Period lock dates live on the company, and time-limited exceptions are a separate store keyed by user, company, lock type, validity end and reason. No exception exists in this database.

### OPTIONALITY

- [N-TXC-029] Cash-basis entries keep references to the originating entry and to the reconciliation that triggered them; the supporting journal and base account are company settings.

### CONSTRAINT

- [N-TXC-032] Entry lines carry four database checks: debit and credit cannot both be non-zero, balance and foreign amount must have the same sign, accountable lines require an account, and heading or note lines must carry no amount or account. Posted entries are unique by name within a journal; journals are unique by code within a company.

### RISK

- [N-TXC-033] Several supporting indexes on entries and entry lines are created by routine start-up code rather than declared with the data model, so a schema comparison based only on declarations misses them.

### UNKNOWN

- [N-TXC-034] No journal entry, entry line or reconciliation exists in this database, so stored behaviour of tax, rounding, rate and cutoff columns cannot be observed and needs runtime verification.


## CAP-TXC-05 Accounts and payments including withholding-related columns

### WHAT

- [N-TXC-035] An account has a type, a reconcile flag, a non-trade flag, an optional currency lock, default taxes and tags as many-to-many links, a list of companies it is shared with, and a code stored per company inside one value, with a derived displayed code.
- [N-TXC-036] A payment stores direction, partner type, amount, currency, date, journal, payment method line, outstanding account, destination account and a link to its journal entry. Several amount and state columns are derived or related and are not stored.
- [N-TXC-038] A journal can name an account for non-deductible tax, and an entry line stores a deductible amount, so a deductible share of tax can be kept per line.

### WHY

- [N-TXC-078] Account flags and payment data decide how tax-related balances are reconciled and settled.

### CONSTRAINT

- [N-TXC-039] Payment amount cannot be negative at database level; accounts have no database uniqueness rule in the declarations reviewed here.

### UNKNOWN

- [N-TXC-037] The installed schema holds no structure for withholding amounts on a payment, withholding certificates or withholding form categories; withholding in this configuration is only carried by ordinary taxes with negative rates and reporting tags. Whether this is sufficient for Thai statutory needs is a gap to be judged against official sources, not from system behaviour.


## CAP-TXC-06 Partner, company, product, country and currency tax configuration, with lock dates

### WHAT

- [N-TXC-040] A partner stores a tax number and a company registration number as plain text. The Thai branch label is derived when read from the registration number (or shows a headquarters label when empty) and is not stored; there is no separate branch record or stored branch code in the installed schema.
- [N-TXC-042] The company stores its fiscal country, tax rounding method (per line or globally), the default price-inclusion choice, the cash-basis switch with its journal and base account, default sales and purchase taxes, a domestic fiscal position, fiscal year end day and month, the exchange-difference accounts and journal, and the chart identifier.
- [N-TXC-044] A product template stores its customer taxes and vendor taxes as many-to-many links, income and expense accounts as per-company properties, and tax tags; product categories hold account defaults, also per company. The product variant reads these through delegation and adds no tax column of its own.
- [N-TXC-045] A currency stores rounding, decimal places and an active flag; exchange rates are dated rows per currency and company with a positive-rate check and a uniqueness rule per day. No rate rows exist in this database.

### WHY

- [N-TXC-079] Company settings and master data supply defaults and cut-off controls so that documents are taxed and locked consistently.

### BUSINESS RULE

- [N-TXC-043] Five lock dates (sales, purchases, tax, fiscal year and hard lock) are stored on the company; per-user effective lock values are derived and not stored. All five are unset in this database.

### OPTIONALITY

- [N-TXC-041] A partner's fiscal position, receivable and payable accounts and payment terms are per-company properties, each stored as a per-company map inside a single column.

### DEPENDENCY

- [N-TXC-046] Countries, country groups and regions are shared reference data used by fiscal positions, taxes, tags and reports; countries are unique by name and by code.

### UNKNOWN

- [N-TXC-047] Which partner and product values override company defaults at document time is runtime behaviour outside this reconciliation.


## CAP-TXC-07 Order, purchase, expense and stock line tax and currency columns

### WHAT

- [N-TXC-048] Sales order lines store tax links as a many-to-many, unit price, discount, stored subtotal, tax amount and total, the line currency, invoiced quantity and extra tax data; the order header stores fiscal position, currency, rate, stored untaxed, tax and total amounts, and a rounding-method indicator that is read from the company and not stored.
- [N-TXC-049] Purchase order lines and headers store the same kinds of tax and currency data as sales lines, plus a company-currency total; vendor taxes are a many-to-many on the line.
- [N-TXC-050] Expense records store tax links, the amount in the expense currency and in company currency, untaxed amount and tax amount, and a link to the generated entry.
- [N-TXC-051] A stock movement stores a unit price and a value in the company currency and carries no tax column; tax data reaches the stock side only through the order lines and entries it relates to.

### WHY

- [N-TXC-080] Business documents store tax and currency data so that invoices, bills and expense entries can be created consistently from them.

### CONSTRAINT

- [N-TXC-052] Order lines use database checks that heading or note lines carry no product, price or quantity and that real lines require a product and unit; a confirmed sales order requires an order date.

### UNKNOWN

- [N-TXC-053] How these stored subtotals and totals are recomputed and rounded is runtime behaviour; no order, line or movement exists in this database.


## CAP-TXC-08 Thai localisation additions and seeded Thai tax configuration

### WHAT

- [N-TXC-054] The Thai localisation adds exactly one derived, non-stored field (a branch label on partners) and extends the list of bank proxy types with three Thai values; it adds no stored column, no table and no database constraint, only one application-level validation of Thai bank proxy values.
- [N-TXC-055] The seeded Thai tax set has eighteen definitions: six VAT definitions (standard 7 percent, zero and exempt for sales and for purchases), eight purchase withholding definitions (company and individual at 1, 2, 3 and 5 percent) and four sales withholding definitions at the same rates, price-exclusive. They sit in five groups with seventy-two distribution lines. The database matches the seed files for every attribute compared.
- [N-TXC-056] Three Thai reports are seeded (a VAT return and two withholding returns) with twenty-four lines, twenty-four expressions and three columns, producing thirteen tax tags; three further tags for account classification come from the base accounting module.
- [N-TXC-057] The seeded company defaults are Thailand as fiscal country, output VAT as default sales tax, input VAT as default purchase tax, global rounding, tax-exclusive prices, cash basis enabled at company level and all lock dates unset.

### WHY

- [N-TXC-081] A country package lets a Thai company start with a ready chart, tax set and return layouts, but statutory adequacy has to be judged separately against official sources.

### RISK

- [N-TXC-058] Thai withholding is represented only as negative-rate taxes grouped by rate and tagged by return form; withholding certificates, payer or payee categories and payment-time withholding are not modelled in the installed schema. This is a native gap to be validated against official Thai sources.

### UNKNOWN

- [N-TXC-059] The Thai chart data also carries a fixed-asset model file with twelve rows; the database has no fixed-asset table, so that file is source-only here and its effect after a future installation is unknown.


## CAP-TXC-09 Constraint, index, key and relation-table reconciliation

### WHAT

- [N-TXC-072] The earlier reconciliation conclusion holds for the tax path models: no field declared in source is missing from the database, and every database field outside the declarations is either an implicit standard field, an inherited field or a delegated field.

### WHY

- [N-TXC-082] Database-level rules protect entry integrity independently of application code, so they are inventoried separately from application checks.

### DEPENDENCY

- [N-TXC-084] Several reviewed models receive the same field declared again by other installed packages, for example bank account fields redeclared by accounting, contact fields redeclared by messaging, and the unit price of a stock movement redeclared by stock valuation; the database keeps a single column for each.

### CONSTRAINT

- [N-TXC-060] Every database constraint and unique index declared with the data model for the reviewed models is present in the database. Across the whole installation every declared constraint and index of a table-backed model is present; the only apparent exception, a query-defined session-device view unrelated to tax, inherits two index declarations that the database applies on its backing log table.
- [N-TXC-061] The database holds extra indexes beyond declarations: field-level indexes, primary keys, and indexes created by routine start-up code. None is unexplained.
- [N-TXC-062] Foreign keys are created from many-to-one fields with delete behaviour taken from the field definition; references stored per company and references to a polymorphic action base have no foreign key.
- [N-TXC-063] Each stored many-to-many link table has both columns mandatory, a composite primary key, foreign keys on both sides and a reverse-order index. Deletion cascades on both sides except where a field declares restrictive deletion, and one link is backed by a full record table instead of a plain link table.
- [N-TXC-064] Every field the application marks as required that has a stored column is also mandatory in the database for the reviewed models.

### RISK

- [N-TXC-065] Some reviewed models have no table at all (query-defined reports, virtual mappings, abstract bases), so they cannot be observed through stored data and their declarations cannot be reconciled to columns.

### UNKNOWN

- [N-TXC-073] The earlier reconciliation did not enumerate indexes, constraints, foreign keys, link tables or column types; this reconciliation adds them and found no unexplained difference.


## CAP-TXC-10 Optional tax-path source not present in this database

### WHY

- [N-TXC-083] Knowing which optional capabilities are absent explains why certain Thai needs, such as payment-time withholding, have no stored structure.

### OPTIONALITY

- [N-TXC-066] An optional capability records withholding at payment time through withholding lines on the payment, a flag on taxes, a sequence for withholding numbers and a company base account; it is not installed, so none of its columns or tables exist here.
- [N-TXC-067] An optional capability adds debit notes, linking an entry to its origin and counting follow-up notes, and a journal option for a separate debit-note sequence; it is not installed.
- [N-TXC-068] An optional capability adds a custom-formula calculation method and decoded formula information to taxes; it is not installed, so the calculation-method list holds only the standard methods.
- [N-TXC-069] An optional capability adds online tax-number validation flags to companies and partners and a foreign-position indicator to countries; it is not installed, so tax numbers are free text without those flags.
- [N-TXC-070] An optional maintenance wizard can update tags on existing tax lines after a tag definition change; it is not installed.

### UNKNOWN

- [N-TXC-071] Other country-specific optional packages also declare fields on the reviewed models; they are outside the Thai scope and only counted, not described.



---

<!-- source: U13_account_tax_chart_localization_NEUTRAL.md -->
# U13 Taxes, chart of accounts, currencies, localization and e-invoicing - NEUTRAL KNOWLEDGE

> Clean-room layer. Source scope: Odoo 19 Community only. Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> Unit U13. Statements are tagged with identifiers that link to the restricted evidence layer. No completeness or maturity is asserted.
> Business and process language only; the restored database was used for configuration facts, never for transactions.


## CAP-U13-01 Tax computation engine

### WHAT
- The system calculates taxes for each document line from the taxes attached to it, producing the untaxed base, the amount of each tax, and totals without and with tax. A single-line legacy interface and a document-level interface both exist and rely on the same algorithm. [N-U13-001]
- A tax is one of four computation kinds: a percentage of the base, a fixed amount per unit, a percentage included inside the price and extracted by division, or a group that bundles several other taxes. [N-U13-002]
- Each tax is usable for sales, for purchases, or for neither on its own; a tax marked for neither can only be used as a member of a group. [N-U13-003]

### WHY
- The same tax algorithm is deliberately implemented on both the client and the server and must stay consistent, so that what the user sees while typing equals what is posted and exported. [N-U13-036]

### BUSINESS RULE
- Taxes are applied in a defined order: a group is replaced by its member taxes, members are ordered by their own order number and then by creation order, and the order number of the group decides where its members fall among the other taxes. [N-U13-004]
- Whether a tax is already included in the price is decided by an override on the tax when present, otherwise by the company default; the company default in this configuration is prices excluding tax. [N-U13-005]
- Evaluation proceeds in passes: fixed-amount taxes first, then price-included taxes from the last to the first, then price-excluded taxes from the first to the last. Neighbouring taxes of the same kind are evaluated together as one batch, and a caller may force all taxes to be treated as included or excluded. [N-U13-006]
- A price-included percentage tax extracts its share from the price using the combined percentage of its batch; a price-excluded percentage tax applies its percentage to the base; a fixed tax is quantity times its amount with the sign of the price; the division kind divides by one minus the combined percentage when excluded and takes its percentage of the price when included. [N-U13-007]
- A tax may be flagged to affect the base of later taxes, and a later tax may be flagged not to be affected by earlier ones; where these flags interact with the inclusive setting, the amount of one tax is added to or removed from the base of others so that totals stay consistent. [N-U13-008]
- Rounding follows a company-wide method: round each line, or round globally. Under the global method amounts are accumulated per tax across the document and rounded once, and the resulting cent differences are spread over lines and taxes proportionally to their size, largest first. Under the per-line method each tax amount and base is rounded as computed. Manual amounts entered by the user replace computed ones after rounding. The default is the global method. [N-U13-009]
- A line discount reduces the unit price before taxes are computed. Amounts are computed in the document currency and converted to the company currency with the document rate, with company-currency rounding applied per line only under the per-line method. [N-U13-010]
- Every tax has separate distribution lines for invoices and for credit notes. Each is based on either the base or the tax and has a percentage (default 100), an optional ledger account, optional tax-report tags and a flag saying whether it feeds the tax closing entry, which defaults to on for tax lines whose account is not an income or expense account. A tax created without distribution lines receives one base line and one tax line per document type. In the loaded Thai set, withholding taxes use negative percentages and post to liability accounts when purchased and to an asset account when sold. [N-U13-011]
- A tax amount is posted to the account of its distribution line, or to the account of the base line when none is given. Tags of base distribution lines go to the base line and tags of tax distribution lines to the tax line, together with tags configured on the product; rounding differences between a tax amount and its distribution parts are spread across the parts. [N-U13-012]
- A credit note uses the credit-note distribution of each tax. A tax with a negative distribution part (reverse-charge pattern) produces a second, opposite entry so that its effect on the document nets to zero while both parts are reported. [N-U13-013]
- Tax journal lines are merged by partner, currency, analytic distribution, account, attached taxes, distribution line and tags; lines with zero amounts are dropped; on recalculation existing tax lines are updated, removed or added rather than recreated. The analytic distribution is copied to a tax line only when the tax is flagged for analytic cost or the distribution part is not used for tax closing. [N-U13-014]
- Document totals present taxes grouped by tax group, ordered by the order number of the group, with an optional subtotal label that places a group after a named subtotal; without a label the group follows the untaxed amount. For sales documents in a foreign currency the taxes can also be shown in the company currency. [N-U13-015]
- A tax group carries the payable, receivable and advance accounts used as counterparts when the tax closing entry is produced. [N-U13-016]
- Every tax has a fiscal country, defaulting to the fiscal country of the company, which governs which groups, tags and positions it can be combined with. [N-U13-035]

### STATE
- A tax is active or archived. Once it is used, changes to its main settings and to its distribution lines are written to its history; before that they are not logged. Nothing in the accounting code prevents archiving a used tax. [N-U13-024]

### OPTIONALITY
- The company chooses the rounding method and whether prices include tax; the price setting can no longer be changed once the company has entries. In this configuration the company uses global rounding and tax-excluded prices, and the 18 loaded taxes are percentage taxes sharing one order number, none due on payment and none affecting the base of others. [N-U13-025]
- Each tax may be due on invoice (default) or on payment. A payment-based tax needs a reconcilable transition account and holds its tax there until payment; a company switch controls whether the option is shown and cannot be turned off while such taxes exist. This capability only records the setting; settlement mechanics belong to payment processing. [N-U13-026]

### DEPENDENCY
- A tax without a tax group receives the first group of its country, else the first group without a country, in group order; a tax group and a country are required on every tax. [N-U13-027]
- Default taxes on a line come from the product (filtered by company, walking up the company hierarchy), else from the default taxes of the account of the line, and the fiscal position then maps them. [N-U13-028]
- When a fiscal position maps price-included taxes to other taxes, the unit price is adapted so that the customer-visible price keeps its meaning; adaptation applies only when all original taxes are price-included. [N-U13-030]

### CONSTRAINT
- The invoice distribution and the credit-note distribution of a tax must mirror each other: exactly one base line each, the same number of lines, at least one tax line, and the same kind and percentage line by line. Electronic export re-checks this structure and refuses to export a tax whose structure is invalid. [N-U13-017]
- The positive tax percentages of a distribution must add up to 100 percent; if negative parts exist they must add up to minus 100 percent. [N-U13-018]
- Tax names must be unique within a company tree for the same use, scope and country. [N-U13-019]
- Members of a group tax must be usable for the same purpose as the group or for neither, must have a compatible scope, may not be groups themselves and may not form cycles. [N-U13-020]
- A tax group that has a country must have the same country as every tax that uses it; the country of a group defaults to the fiscal country of the company. [N-U13-021]
- A tax that appears on any journal item or reconciliation rule cannot be deleted, and cannot be moved to another company; archiving is the intended alternative. [N-U13-022]
- The account of a distribution line may not be a receivable, payable or off-balance account, and its tags must be tax-report tags valid for the fiscal country of the company or its foreign-tax countries. [N-U13-023]

### RISK
- In the loaded Thai set the zero-rate and exempt VAT taxes are given no tax group by the template, so they inherited the first Thai group, the 1 percent withholding group; document totals then show these taxes under a withholding heading. [N-U13-031]
- Under global rounding the tax of a line can differ by one currency unit from the same line computed alone, because document-level differences are redistributed. [N-U13-032]
- All loaded taxes share the same order number, so combined taxes are ordered by creation sequence; results are order-independent for the plain percentage taxes loaded, but other combinations were not examined. [N-U13-033]

### UNKNOWN
- Numeric outcomes for combined Thai taxes, for example VAT with withholding on the same line, were not executed and need a runtime test. [N-U13-034]

## CAP-U13-02 Fiscal positions and tax and account mapping

### WHAT
- A fiscal position is a company-specific rule set that adapts the taxes and ledger accounts used on a document to the circumstances of the customer or vendor. [N-U13-050]
- It contains a tax mapping, where a replacement tax lists the domestic taxes it replaces, and an account mapping that substitutes one ledger account for another. [N-U13-051]

### WHY
- Positions exist so that taxes and accounts adapt automatically to the customer, defaulting from the settings of the customer. [N-U13-070]

### BUSINESS RULE
- A position set manually on the delivery address, or else on the partner, always wins over automatic detection. [N-U13-052]
- Automatic detection considers only positions flagged for it. A position matches when all its conditions hold: a VAT number is present when required, the postal code is in range, the state is in the list, the country is equal, the country is inside a group and not in the excluded states of that group. Candidates are tried company-specific first and then by order number, and the first match is used. [N-U13-053]
- Without a partner country no automatic position is selected. [N-U13-054]
- When company and partner share the same VAT country prefix inside the European Union and the partner country equals the company country, the invoicing address is used instead of the delivery address. [N-U13-055]
- Applying a position to taxes: with no position the taxes are unchanged; with a position that has no taxes only taxes not restricted to any position remain; otherwise each tax is replaced by its mapped replacements and unmapped taxes pass through. [N-U13-056]
- The account mapping applies to the income or expense account taken from the product and to receivable and payable lines of the document. [N-U13-057]
- Default unit prices are adapted when a position maps price-included taxes. [N-U13-058]
- A document computes its position from the partner, the delivery address and the company, except purchase receipts which take a company default; the user may override it and a prompt offers to update existing lines. A position used on a document cannot be deleted. [N-U13-059]

### STATE
- A fiscal position can be archived without being deleted. [N-U13-069]

### OPTIONALITY
- Positions are optional and none is shipped with the Thai chart; automatic detection, mapping and foreign taxes are therefore inactive until a position is created. The database holds no position and the company has no domestic position. [N-U13-064]

### DEPENDENCY
- The domestic position of a company is derived from its country; a tax is domestic when it has no positions or includes the domestic one. [N-U13-065]
- Foreign taxes for a foreign-VAT position can be created by an accounting administrator from the chart of that country, which may install its localization. [N-U13-066]

### CONSTRAINT
- A postal code range needs both ends with the upper bound not smaller than the lower bound; numeric bounds are padded with zeros to the same length. [N-U13-060]
- A foreign VAT number requires a country, must be unique per country, requires states when it lies in the fiscal country of the company, and its country must be inside the selected country group. [N-U13-061]
- An account mapping pair may appear only once per position. [N-U13-062]
- A document may not carry taxes whose country is incompatible with the position or with the fiscal country of the company; a position with a foreign VAT sets the tax country of the document. [N-U13-063]

### RISK
- With no positions, mixed local and foreign scenarios such as export or zero-rating by customer type rely on users choosing taxes by hand. [N-U13-067]

### UNKNOWN
- Detection, mapping and price adaptation were never exercised for the Thai company because no position exists. [N-U13-068]

## CAP-U13-03 Chart of accounts and company chart loading

### WHAT
- The chart of accounts is the list of ledger accounts, each with a code, name, type, reconcilable flag, optional currency, default taxes and tags, and the list of companies that use it. Accounts cannot be created by name alone outside file import. [N-U13-080]
- Nineteen account types exist: receivable, bank and cash, current assets, non-current assets, prepayments, fixed assets, payable, credit card, current liabilities, non-current liabilities, equity, current-year earnings, income, other income, expenses, other expenses, depreciation, cost of revenue and off-balance. [N-U13-081]
- A company chart is created by loading a country template. The template supplies, from data files and company-level values, the accounts, account groups, tax groups, taxes, fiscal positions, journals (sales, purchases, miscellaneous, exchange difference, cash-basis taxes, bank) and reconciliation rules. Account codes are padded to the digit count of the template, unknown fields are ignored, loaded records are protected from later updates, and loading can be started from settings, by installing a localization, or when a company is created. [N-U13-082]
- Taxes of another country can be created for a company from the template of that country, cloning local accounts, and are skipped when taxes of that country already exist. [N-U13-107]

### WHY
- Account types exist to drive statutory reports and the rules for year-end closing and opening entries. [N-U13-109]

### BUSINESS RULE
- The internal group of an account follows from its type. Income and expense accounts are not carried forward at year end, all others are. Receivable and payable accounts must allow reconciliation; income, expense and equity accounts do not; cash, credit-card and off-balance accounts default to not reconcilable; off-balance accounts can neither be reconcilable nor carry taxes. [N-U13-083]
- An account code contains only letters, digits and dots and is unique across a company and its parent and child companies. Codes are kept per company root: companies in one tree share a code, and each company using an account must have one. New codes can be generated by incrementing a prefix. [N-U13-084]
- An account may be shared by several companies, but bank and cash accounts belong to one company only, an account must keep at least one company, and a company cannot be removed from an account once that company has entries on it. Users see only accounts of their allowed companies and their parents. [N-U13-085]
- An account can force a single currency for its entries; this cannot be set when entries in another foreign currency exist and must match the currency of any journal using the account. [N-U13-086]
- Turning reconciliation on or off rewrites open amounts on the lines of the account; turning it off is refused while partial matches are pending. [N-U13-087]
- Account groups form a prefix hierarchy per root company; the group of an account is the one with the longest matching prefix, groups of equal length may not overlap, and the parent of a group is the enclosing group. [N-U13-088]
- Account tags can mark accounts, taxes or products; names are unique per use and country; accounts without a type or tags take them from the nearest lower code. [N-U13-089]
- A current-year earnings account is reused or created at load, using code 999999 or the next free lower code. [N-U13-090]
- Only a system administrator may load a template; regional umbrella templates cannot be loaded directly; a missing localization module is installed first; loading runs for a single company, in English, without change tracking and with account group synchronisation delayed until the end. [N-U13-095]
- When a root company with no entries is switched to a different template, or when demo data is requested, all entries and all records of the template types of that company are removed first so the new chart replaces the old. [N-U13-096]
- Loading the template already set is a reload: company values and property defaults are not reapplied; existing accounts only receive tag updates and keep their reconcilable flag; journals found by code or name are kept; a tax whose kind, rate or number of distribution lines differs from the template is renamed with an old marker and a new tax is created, while unchanged taxes only refresh tags and position links. [N-U13-097]
- Subsidiaries receive the same template with only company-level values applied; a company created below a company that has a chart receives that chart automatically. [N-U13-099]

### STATE
- An account is active or archived and is flagged as used once it appears on any journal item. Archiving itself is not guarded by code; error texts that mention deactivation belong to deletion checks. [N-U13-091]
- In the restored database the Thai chart has 147 accounts (144 from the template, two Outstanding accounts and one bank account), six-digit numeric codes, one company, no shared accounts, no account groups, no foreign-currency accounts, 4 receivable, 3 payable and 4 bank and cash accounts, and one current-year earnings account. [N-U13-106]

### OPTIONALITY
- Loading can be asked not to create new records, and may include demo data; demo failures are logged without undoing the chart. [N-U13-098]

### DEPENDENCY
- After loading, the system sets journal suspense and difference accounts, default journals, default accounts on sales and purchase journals, default company taxes, default taxes on products lacking company taxes, cash-basis availability, product category defaults for income and expense, and partner defaults for receivable and payable; it always creates the Outstanding Receipts and Outstanding Payments accounts for root companies and creates helper accounts named by the company only when missing. [N-U13-100]
- Available templates are discovered from installed localization modules; installing one on a company without a chart loads the template for the country of the company; removing the module clears the template reference of the company. [N-U13-101]
- On first load the company currency is set from the fiscal country of the template when no entries exist. [N-U13-102]

### CONSTRAINT
- An account cannot be deleted when it has journal items, is used in a fiscal position mapping, or is used on a tax distribution line; the three cash-flow master tags cannot be deleted; a check meant to block archival of accounts used in tax distribution is keyed to a field that does not exist and appears ineffective. [N-U13-092]
- An account that is the default account of a journal cannot be changed to a receivable or payable type. [N-U13-093]
- Accounts cannot be merged by the generic merge; a wizard merges only accounts with the same type, trade flag, currency, reconcilable flag and active state, and never bank or cash accounts. A shared account can be split into one account per company. [N-U13-094]
- Loading stops with an invitation to update the localization when a template names a tax tag that does not exist. [N-U13-103]

### RISK
- The Thai template passes a template-style identifier text as the transfer account prefix and the company stores that literal text; this is harmless only because the transfer account is set directly. [N-U13-104]

### UNKNOWN
- A depreciation-model data file ships with the Thai template but no Community routine reads it; whether it is used depends on an optional asset application that was not studied. [N-U13-105]
- What happens when a different chart is loaded on a company that already has entries was not exercised: the removal step is skipped and template data is merged by identifier. [N-U13-108]
- The effect of reloading the Thai template on this database was not executed. [N-U13-110]

## CAP-U13-04 Currencies in accounting and cash rounding

### WHAT
- Every company has one base currency; documents and journal lines may use another currency, and each line stores both the foreign amount and the base amount. Partners show the base currency of their company. A company option displays taxes in the base currency on foreign sales documents that carry taxes. [N-U13-130]

### WHY
- Cash rounding exists for countries where the smallest coins are withdrawn so that cash invoices must be rounded. [N-U13-148]

### BUSINESS RULE
- The base currency of a company cannot change once journal items exist; it is set from the country of the template when the chart is first loaded. [N-U13-131]
- The currency of a document defaults to the foreign currency of the bank line, then the journal currency, then the existing value, then the base currency; invoice lines follow the document currency. [N-U13-132]
- A rate is looked up for the document date (invoice date, else today) among rates of the main company or without company: the latest rate on or before the date, else the earliest rate, else a neutral rate of one. Branch companies use the rates of their main company, and rates may only be recorded for main companies. [N-U13-133]
- An invoice stores its rate, recomputed when currency, company or date change until the user edits it; it must be positive; a refresh action resets it to the expected rate; if the invoice date is empty at posting it is set to today and the rate recomputed unless the user chose it manually. [N-U13-134]
- Foreign and base amounts are linked by the rate: the base amount is the foreign amount divided by the rate rounded to base-currency precision, and a missing foreign amount defaults to the balance times the rate rounded to the line currency. [N-U13-135]
- Multi-currency features are switched on for users automatically when more than one currency is active; a currency set on a company cannot be archived. [N-U13-138]
- Cash rounding rounds the document total to a chosen step (up, down or to nearest) and records the difference either as a separate rounding line, posted to a loss account when the difference is positive and one is set, otherwise to a profit account, or by adjusting the tax line with the largest amount. [N-U13-139]
- The rounding line is created, updated or removed whenever the document changes, replaced when the strategy changes, and absent when the total is already round. [N-U13-141]

### STATE
- A document keeps its own stored rate; later changes of the rate table do not alter it. [N-U13-147]

### OPTIONALITY
- Cash rounding is hidden unless its feature group is enabled, and only invoicing users manage the rules; no cash rounding rule exists in this configuration. [N-U13-142]

### DEPENDENCY
- The company holds the exchange gain account, the exchange loss account and the exchange journal used by exchange-difference entries produced during reconciliation. [N-U13-143]
- Tax amounts are rounded globally in the document currency and in the base currency independently. [N-U13-144]

### CONSTRAINT
- A line may not have both a debit and a credit, and its foreign amount must have the same sign as its balance. [N-U13-136]
- The rounding factor of a currency must be positive, currency codes are unique, and the precision cannot be reduced once the currency appears on journal items. [N-U13-137]
- The rounding step must be positive; profit and loss accounts are company-specific and cannot be receivable or payable; choosing the separate-line strategy without a profit account raises a warning. [N-U13-140]

### RISK
- The database has two active currencies and no rate records; any conversion to the second currency would use a neutral rate of one until rates are recorded. [N-U13-145]

### UNKNOWN
- Automatic retrieval of rates depends on an optional module; Community accounting has no rate-fetching job. [N-U13-146]

## CAP-U13-05 Accounting company settings and period configuration

### WHAT
- Each company holds its accounting configuration: fiscal year end, opening date and opening entry, tax rounding and price-inclusion defaults, default sale and purchase taxes, default income and expense accounts, exchange accounts, cash-basis option, storno option, restricted audit trail, bill auto-posting, credit limit feature and fiscal country (defaulting to the company country). [N-U13-160]

### WHY
- The opening date states the date from which accounting is managed in the system. [N-U13-176]

### BUSINESS RULE
- A fiscal year is defined only by its last day and month (default 31 December); no fiscal-year or period records are stored, and year boundaries are computed on demand. [N-U13-161]
- The fiscal year end determines the date ranges used for yearly and year-range numbering of entries and for the resequencing preview. [N-U13-162]
- Five lock dates are stored per company: global, tax, sales and purchase soft locks plus an irreversible hard lock. Writing them recreates affected exceptions; the hard lock cannot be removed or moved back; locking is refused while drafts (hard lock) or unreconciled bank lines (fiscal and hard locks) exist in the period; the tax lock date is meant to be set when the tax closing entry is posted. Enforcement belongs to entry posting. [N-U13-163]
- The cost-accounting style flag (anglo-saxon) is a company option that is off by default and is reset to off by every chart except the generic one; in this configuration it is off. [N-U13-165]
- Company income and expense accounts feed product category defaults and the default accounts of sales and purchase journals; changing the bank or cash code prefix renumbers existing cash and credit-card accounts that use the old prefix. [N-U13-166]
- Storno accounting defaults on in countries where it is mandatory and is offered in some others; Thailand is in neither list. [N-U13-167]

### STATE
- The opening date and opening entry define when accounting starts; a draft opening entry follows the date and is dated the day before it. [N-U13-170]
- In the configured company the fiscal year ends on 31 December, no lock date is set, there is no opening date or entry, the cost-accounting flag is off, cash-basis is enabled, global rounding and tax-excluded prices are used, the credit limit feature is enabled with a zero default, and bills auto-post by default. [N-U13-173]

### OPTIONALITY
- The onboarding text mentions tax return periodicity, but only the fiscal year end and the opening date can be configured here. [N-U13-168]
- Restricted audit trail is optional unless a localization forces it; no Thai rule forces it. [N-U13-169]

### DEPENDENCY
- Fiscal year end, storno and cash-basis settings of a branch company come from its main company. [N-U13-171]

### CONSTRAINT
- The last day must exist in the chosen month, with 29 February accepted. [N-U13-172]

### RISK
- Changing the fiscal year end after entries exist could place new entries in different numbering ranges. [N-U13-174]

### UNKNOWN
- Tax return periodicity, tax closing entry creation and period locking workflows are not implemented in the sources read. [N-U13-175]

## CAP-U13-06 Partner accounting properties and defaults

### WHAT
- Each partner carries accounting defaults per company: receivable account, payable account, fiscal position, customer and vendor payment terms, credit limit, degree of trust, invoice sending method and format, bill auto-posting choice, and counters of customer and supplier activity; the values can differ by company for the same partner. [N-U13-190]

### WHY
- Auto-posting exists to post bills of trusted vendors automatically. [N-U13-200]

### BUSINESS RULE
- Accounting defaults of the commercial partner are synchronised to its contacts, and company-dependent values are stored separately for each company. [N-U13-192]
- The receivable or payable account of a document is the account of its existing term line, else the setting of the commercial partner, else the setting of the company partner, else the first active receivable or payable account of the company, then mapped by the fiscal position. Chart loading stores receivable and payable accounts as defaults for new partners. [N-U13-193]
- A credit limit is optional per partner, visible only to invoicing and read-only accounting users, falls back to the company default and is shown only when the company enables the feature; the receivable and payable totals sum the open amounts of posted entries. [N-U13-194]

### STATE
- Customer and supplier counters grow as documents are generated and are used to order partner lists. [N-U13-199]
- In the configured database new partners default to the Thai trade receivable and trade payable accounts, a zero credit limit and normal trust; ten payment terms and seven partners exist. [N-U13-197]

### OPTIONALITY
- The credit limit feature is optional and per company: it appears only when enabled in company settings, with a default limit that partners may override. [N-U13-201]

### DEPENDENCY
- Payment terms, fiscal position and ledger accounts used by partner defaults come from other capabilities and must belong to the same company; customer and vendor payment terms are applied by the payment terms capability. [N-U13-202]

### CONSTRAINT
- A partner cannot be deleted once used on draft or posted documents, and cannot be attached to a parent with a different tax identifier if it already has entries. [N-U13-196]

### RISK
- Defaults stored at chart load apply to partners created later; existing partners keep their value. [N-U13-198]

### UNKNOWN
- Where the credit limit is enforced belongs to the sales application and was not studied. [N-U13-195]

## CAP-U13-07 Analytic distribution on journal items

### WHAT
- Each journal item can carry an analytic distribution: percentages across analytic accounts, where accounts of different plans can be combined in one share. [N-U13-210]

### WHY
- A running proportion is kept per plan so that a fully distributed plan yields exactly the real amount. [N-U13-225]

### BUSINESS RULE
- A distribution is stored as a map from an analytic account, or a combination of accounts, to a percentage rounded to the configured precision (two decimals here); an editing key allows updating only some plans. [N-U13-211]
- The default distribution of a line comes from matching distribution models by product, product category, partner, partner category, account code prefix and company, combined with the distribution of the originating record. [N-U13-212]
- Each plan is optional, mandatory or unavailable according to the best-scoring rule for the company, the business domain (invoice, bill, miscellaneous), the account prefix and the product category, else the default of the plan. [N-U13-213]
- A mandatory plan requires one hundred percent on that plan; this is enforced when the user posts through the form buttons or the validation wizard, and lines in breach are flagged, except for receivable, payable, cash and card accounts. [N-U13-214]
- Posting creates analytic lines in one batch for every line with a distribution: the amount is the balance of the line times the percentage with the opposite sign, the last share of a plan takes the remainder, rounding errors are spread, zero amounts are skipped, and each analytic line records date, partner, product, quantity, financial account, reference, responsible user and company. [N-U13-215]
- Changing the distribution of a posted line deletes and recreates its analytic lines; draft lines keep none. [N-U13-216]
- Editing or deleting an analytic line recomputes the percentages of its journal item; deleting the journal item deletes its analytic lines. [N-U13-217]
- A tax line inherits the distribution only when its tax is flagged for analytic cost or its distribution part is not used for tax closing. [N-U13-218]

### STATE
- The category of an analytic line follows the document: customer invoice, vendor bill or other. [N-U13-224]

### OPTIONALITY
- Analytic accounting is an optional feature; in this configuration there is one plan, no applicability rule and no distribution model, so no plan is mandatory; access to the structure is for full accounting users. [N-U13-220]

### DEPENDENCY
- Analytic plans and accounts belong to the analytic capability; the accounting side adds invoice and bill domains and account prefix and product category criteria. [N-U13-221]

### CONSTRAINT
- The financial account of an analytic line must equal the account of its journal item. [N-U13-219]

### RISK
- The mandatory-plan check runs only when the caller marks it; posting by import, automatic jobs or external calls may skip it, and exchange-difference entries are posted without it. [N-U13-222]

### UNKNOWN
- Posting with mandatory plans and multi-plan combinations was not executed. [N-U13-223]

## CAP-U13-08 Thai localization

### WHAT
- The Thai localization supplies a chart of 144 accounts with six-digit codes, 18 taxes, five tax groups, three tax report definitions, an invoice layout, a commercial invoice report, a branch label for partners and payment QR support for Thai bank accounts. [N-U13-240]
- It is a Community module and independent of any extra Thai add-on; nothing from the extra Thailand collection was used in this study. [N-U13-241]

### WHY
- The localization exists to give Thai companies a ready chart and taxes. [N-U13-255]

### BUSINESS RULE
- VAT at 7 percent, 0 percent and exempt exist for both sales and purchases. Output VAT posts tax to the output VAT account with the sales grids; input VAT posts to the input VAT account with the purchase grids; zero-rate sales are tagged also as zero-rated and exempt sales as exempt; refunds mirror; tax groups hold payable and receivable accounts. [N-U13-242]
- Withholding taxes exist at 1, 2, 3 and 5 percent for transport, advertising, services and rental. Purchase withholding distinguishes individuals from companies with separate income and remittance tags and liability accounts; sales withholding records the amount withheld by customers as a recoverable asset and is price-excluded. [N-U13-243]
- The tax report shows sales, zero-rated and exempt sales, output tax, purchases, input tax, tax payable or excess, excess carried forward and net tax; two further reports for individual and company withholding show income, remittance, surcharge and total. [N-U13-244]
- For companies whose fiscal country is Thailand the invoice is printed with the title Tax Invoice and the branch label of the customer; a commercial invoice report is available for customer invoices in Thailand and refuses records that are not invoices. [N-U13-245]
- Thai bank accounts can generate payment QR codes using the mobile number, the merchant tax identifier or the e-wallet identifier; the mobile number is converted to the international form; only the Thai baht is accepted; the user messages name another country scheme by mistake. [N-U13-246]
- A company partner in Thailand shows Branch followed by its company registry number, or Headquarter when none is set. [N-U13-248]

### STATE
- In the database the localization is installed, the company uses the Thai chart, fiscal country Thailand and the baht, with 5 tax groups, 13 Thai tax tags, 3 Thai tax reports and one commercial invoice report. [N-U13-251]

### OPTIONALITY
- The module installs automatically with accounting; its template sets Thailand as fiscal country, default VAT taxes, default accounts and the cash-basis switch (although no shipped tax is cash-basis); post-install keeps existing tags on upgrade; demo data creates a Thai demo company. [N-U13-249]

### DEPENDENCY
- It depends on accounting and on the shared QR code module; the only core behaviours it adjusts are the choice of invoice document, a print guard for its own report, extra bank identifier types and QR rules; tax computation, posting and locking are untouched. [N-U13-250]

### CONSTRAINT
- A merchant tax identifier must have 13 digits and a mobile number 10 digits; other identifier types are rejected for Thai bank accounts. [N-U13-247]

### RISK
- The surcharge tags of the withholding reports are used by no shipped tax, so surcharge amounts depend on manual tagging; no fiscal positions, account groups, journals or reconciliation rules come from the localization itself (journals and rules come from the generic template). [N-U13-252]
- No Thai e-invoice or e-tax format exists in the Community e-invoicing modules: Thailand is absent from the format-by-country and electronic address mappings. [N-U13-253]

### UNKNOWN
- Conformity of the tax grids, reports and invoice layout with current Thai statutory requirements is outside the evidence. [N-U13-254]

## CAP-U13-09 E-invoicing, payment QR and location number

### WHAT
- Two e-invoicing mechanisms coexist: a framework that tracks an electronic document per invoice and format with a state and an error log, and a send-time exporter that builds standard XML when invoices are sent. The framework base provides no format of its own and lets formats embed content in the invoice PDF. [N-U13-270]
- Available standard formats are Factur-X and ZUGFeRD (CII), Peppol BIS 3 (UBL, EU countries), XRechnung (Germany), NLCIUS (Netherlands), Australia and New Zealand BIS 3 and Singapore BIS 3, with PINT layers; any partner can be set to any of them manually. No format is registered in the framework in this configuration and none exists for Thailand. [N-U13-271]
- Partners can hold a Global Location Number, shown only on delivery addresses and not validated, which e-invoice formats may use. [N-U13-272]
- Payment QR codes follow the EMV merchant-presented standard: fields joined in length-value form with a checksum; the method is available on bank accounts with priority 30, is refused when merchant information, city or identifier is missing, and only country modules (here Thailand) can supply merchant information; an invoice uses its chosen method or the first eligible one. [N-U13-273]

### WHY
- The PDF is embedded in the XML so that recipients handling only the XML still receive the printable invoice. [N-U13-293]

### BUSINESS RULE
- When an invoice is posted, each format enabled on its journal that applies first checks the configuration and blocks posting with the list of problems; then a document in state to send is created or reset, formats without an external service are processed at once, and web-service formats are queued; mail sending waits while a document is still to send. [N-U13-274]
- A sent web-service document blocks reset to draft; the user requests cancellation, which can be withdrawn; cancelling an invoice marks sent documents to cancel and others cancelled; an approved cancellation resets the invoice to draft and cancels it; requesting cancellation first checks the fiscal lock. [N-U13-276]
- Documents are grouped into jobs by format, state, company and optional format key; web-service jobs lock records and are skipped if another process holds them, or refused when run manually; a commit is made between jobs. [N-U13-277]
- Formats compatible with a journal (sales journals by default) are enabled by default; formats with pending web-service documents cannot be removed from a journal; internal users read, and invoicing users manage, documents and formats. [N-U13-278]
- When invoices are sent, a UBL or CII file is built if the partner format requires one, the invoice is a sales document (or an exportable buyer-issued invoice) and no file exists yet; errors are listed and allow a fallback document; the file is linked to the invoice and can be exported on demand. [N-U13-280]
- For UBL formats the invoice PDF and supported extra attachments are embedded in the XML. [N-U13-281]
- A Factur-X XML is always generated and embedded in the PDF for portability regardless of the country of the invoice; conversion to the PDF-A archive standard with metadata is attempted only for French or German parties. [N-U13-282]
- Export validates the tax structure and the common rule that product lines need a tax, then format rules: payment instructions and bank account number, seller postal address, identifier and contact, buyer address, intra-community delivery, the Canary Islands rate, and Peppol national rules for Norway and Belgium. [N-U13-283]
- Each tax may carry a tax category code and an exemption reason code; without a code the category is predicted from the countries of seller and buyer, zero rate and the reverse-charge pattern. [N-U13-284]
- The electronic address scheme and identifier of a partner are computed from country, VAT number and company registry and validated by scheme; the send wizard alerts when the company or partner address is missing for Peppol formats. [N-U13-285]
- Imported XML files are recognised by their declared profile and decoded into a draft invoice that has no lines yet, with partner, products, units, accounts and taxes found by matching, tax totals corrected within five cents, and a log entry listing the sources. [N-U13-286]

### STATE
- A document moves from to send to sent, and from sent to to cancel to cancelled; failures keep the document with an error text and a severity of info, warning or error, and error-level documents are skipped until retried; the invoice shows the combined state of its web-service documents. [N-U13-275]

### OPTIONALITY
- The web-service queue runs daily, handles up to 20 jobs, ships inactive and is activated when a web-service format is created; an option controls extraction of PDFs embedded in imported XML; in this configuration there are no formats or documents and the queue is inactive. [N-U13-287]

### DEPENDENCY
- All of these modules depend only on accounting; the exporter and the GLN module are set to install automatically with it. [N-U13-288]

### CONSTRAINT
- Only one electronic document per invoice per format exists; attachments of web-service documents cannot be deleted; invoices with sent web-service documents cannot be resequenced. [N-U13-279]

### RISK
- A Thai partner with no explicit format gets no UBL or CII file in the send flow, because no suggestion exists for Thailand and the exporter relies on the stored partner format. [N-U13-290]
- A Factur-X attachment is embedded in the PDF of any company without a country test and its errors are discarded, so Thai invoices may carry a CII part not needed locally. [N-U13-291]

### UNKNOWN
- Send behaviour when the embedded export fails, and the actual file naming for Thai invoices, were not executed. [N-U13-292]

## CAP-U13-10 Roles, access rules, data scope, failure paths and scheduled jobs

### WHAT
- Accounting access is organised in roles: Invoicing, read-only accounting, Basic, full accounting user and accounting Administrator (which includes Invoicing), plus the system administrator for chart loading; technical groups control cash rounding, partial purchase deductibility, delivery addresses, inalterability and bank validation. [N-U13-320]

### WHY
- Only the Invoicing and Administrator roles are meant to be used when only invoicing is installed; the other roles give shallow access. [N-U13-331]

### BUSINESS RULE
- Internal users may read taxes, tax groups, fiscal positions, accounts, tags and distribution rules; only accounting administrators create, change or delete taxes, distribution lines, tax groups, accounts, account groups, fiscal positions and currency rates; full accounting users manage tags and the analytic structure; invoicing users manage cash rounding, analytic distribution models and electronic documents. [N-U13-321]
- Taxes, tax groups, fiscal positions, account groups and accounts are visible only when their company is, or is a parent of, an allowed company of the user; distribution lines are also visible when they have no company; branches can use records of their parent. [N-U13-322]
- Only a system administrator can load or reload a chart; only accounting managers or the administrator can create foreign taxes. [N-U13-323]
- Currency rates are managed by accounting administrators and are visible for the companies of the user or when not tied to a company. [N-U13-324]

### STATE
- Scheduled work: a daily job that sends invoices automatically (active), a daily job that posts automatic draft entries (active, owned by entry posting) and the electronic document queue (inactive); none belongs to the Thai, QR, GLN or exporter modules. [N-U13-325]

### OPTIONALITY
- Several groups are optional switches that a company turns on when needed: cash rounding, partial purchase deductibility, delivery addresses, inalterability and bank account validation; scheduled sending and the electronic document queue can be deactivated. [N-U13-332]

### DEPENDENCY
- The access rules and record rules declared by the modules were confirmed against the configured database for taxes, tax groups, distribution lines, accounts, fiscal positions, currencies, cash rounding, account groups, tags and electronic documents. [N-U13-329]

### CONSTRAINT
- Failure paths include deleting a used tax or account, duplicate tax names or account codes, invalid distribution structures, group nesting, missing localization tags, loading a chart without administrator rights, and e-invoice export errors, each raising a clear message. [N-U13-326]

### RISK
- Uniqueness checks on tax names run with elevated rights across the company tree, so an error message may name taxes of other companies. [N-U13-327]

### UNKNOWN
- Which users hold which roles was not studied. [N-U13-330]


---

<!-- source: U23_not_installed_current_NEUTRAL.md -->
# U23 Authentication integrations, optional accounting add-ons, cloud attachment storage and peripheral features - NEUTRAL KNOWLEDGE

> Clean-room layer. Source scope: Odoo 19 Community only. Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> Unit U23. Statements are tagged with identifiers that link to the restricted evidence layer. No completeness or maturity is asserted.
> Business and process language only; every feature in this unit is an optional add-on that is not installed in the studied configuration, so behaviour is described from the add-on definitions alone and runtime behaviour is flagged unknown.

## CAP-U23-01 Withholding tax registered at payment time

### WHAT
- The system can record a withholding tax at the moment a payment is registered: part of a settlement is retained by the payer and owed to the tax authority, so the cash that moves is smaller than the document being settled. [N-U23-001]
- A tax can be flagged as withheld on payment. Such a tax is ignored when the sales or purchase document itself is calculated, so document totals, document journal items and tax reports built from the document are unaffected until a payment is registered. [N-U23-002]
- At payment time the payer sees a table of withholding lines (number, account, base, tax, analytic distribution, withheld amount) proposed from the settled documents and may edit them before confirming. [N-U23-003]
- The standard distribution provides only this generic mechanism. It contains no country rate table, no authority-specific withholding certificate or return, and no Thai content; the Thai localization shipped in the same distribution models withholding taxes as ordinary negative taxes booked on the document, not on payment. [N-U23-004]

### WHY
- The add-on exists so that withholding taxes can be registered while a payment is made rather than on the invoice or bill: invoices stay at their gross value and the tax effect arises with the payment entry. [N-U23-005]

### BUSINESS RULE
- Only taxes with a negative rate, usable for sales or purchases, can be flagged as withheld on payment; a tax that is a group of other taxes or a percentage-included-in-price tax cannot be flagged. Flagging forces the tax to be recognised on the document date and to be price-excluded, and entering a positive rate clears the flag. [N-U23-006]
- On a payment, the cash line equals the payment amount minus the withheld amounts and the counterparty line still equals the full settled amount. The withheld tax is posted to the tax account, and the withheld base is posted as an equal and opposite pair of lines so the base can be reported without changing the balance. [N-U23-007]
- The withholding lines proposed to the payer are derived from the withholding taxes found on the settled document lines, grouped by number, analytic distribution, account, tax and currency. The withheld amount of a line follows its base in proportion to the amount originally computed, and both can be edited manually. [N-U23-008]
- Each withholding line needs a withholding number: either typed by the user or drawn from a numbering series defined on the tax. If neither exists the payment cannot be completed. Series numbers are consumed only when the payment entry is built. [N-U23-009]
- Receipts of a sale-side payment use sale taxes and outgoing payments use purchase taxes; for refunds the roles are inverted so that the correct distribution of the tax applies. Withholding is offered only when the company has at least one matching withholding tax and only when the payment produces a single entry. [N-U23-010]
- The base account of the withholding lines can be set once per company; when set, the account column is hidden and used as default. A cash account chosen as the withholding account is rejected. [N-U23-011]
- When the payment method has no dedicated holding account, the payer must name an outstanding account for a payment with withholding; the chosen account is made reconcilable if it is not already. [N-U23-012]

### STATE
- Withholding lines are editable only while the payment is in draft; once confirmed they are fixed and printed on the payment receipt together with number, tax, base and amount. [N-U23-013]

### OPTIONALITY
- The feature is dormant unless at least one tax is flagged and the add-on is installed; the company-level base account, per-tax numbering series and per-line analytic distribution are all optional. [N-U23-014]
- Several other localizations in the distribution opt in to this mechanism by flagging their own taxes; the Thai localization does not, so enabling the add-on alone changes nothing for the Thai tax set. [N-U23-015]

### DEPENDENCY
- The add-on depends only on core accounting and hooks into the payment entry builder, the payment registration step, the tax calculation engine, the product price label and the payment receipt; downstream localizations depend on it. [N-U23-016]

### CONSTRAINT
- The base of a withholding line must be greater than zero; the net payment (amount minus withheld) must not be negative; the line account may not be a cash, bank, outstanding or transfer account; a withholding number is mandatory. [N-U23-017]
- Withholding cannot be combined with a payment write-off in the same entry; when both are present the write-off is dropped. [N-U23-018]

### RISK
- Using Thai withholding at payment time is not available out of the box: the shipped Thai taxes would have to be re-created or flagged, and the effect on existing history, tax-return grids and withholding certificates is not documented in this distribution. [N-U23-019]
- Because the tax effect leaves the invoice, an invoice-based tax report will not show withheld amounts until the payment entry exists; reporting that needs withheld amounts must read payment entries. [N-U23-020]

### UNKNOWN
- Numeric results for combined cases (value-added tax together with withholding, foreign currency, instalments, partial payments, refunds) were not executed; they require a runtime test. [N-U23-021]
- The behaviour when a payment that carries withholding lines is cancelled, reset to draft or reversed was not traced and is unknown. [N-U23-022]
- Whether the withholding numbering and receipt table satisfy Thai statutory certificate requirements is unknown; no Thai withholding certificate or return form was found in the studied distribution. [N-U23-023]

## CAP-U23-02 Debit note issuance and numbering

### WHAT
- A posted customer invoice, customer credit note, vendor bill or vendor credit note can be corrected upward by creating a debit note: a new draft document that carries a link back to the document it corrects and is otherwise an ordinary invoice or bill. [N-U23-024]
- A debit note is created through a dialog that asks for a reason, a date, an optional journal and whether to copy the original lines. Several documents of the same family can be processed at once, producing one debit note each. [N-U23-025]
- A document that has debit notes shows a counter button listing them; debit notes can be filtered in the document, invoice and journal item search views, and printed documents are titled debit note instead of invoice. [N-U23-026]

### WHY
- In many countries a debit note is used to increase the amounts of an existing invoice or, in specific cases, to cancel a credit note; it is like a regular invoice but the link to the original document must be kept. [N-U23-027]

### BUSINESS RULE
- Only posted documents can be debited; a document that is itself a debit note, or already linked to one, cannot be debited again; journal entries that are not invoices, bills or credit notes are refused. [N-U23-028]
- The debit note takes the type of an invoice or bill: debiting a credit note produces an invoice or bill of the matching direction. Its reference combines the original number and the reason, its date and invoice date default to the dialog date, its payment terms are cleared and its journal is the one chosen or that of the original. [N-U23-029]
- Lines are copied only when the user asks for it; otherwise the debit note starts empty. The dialog hides the copy option for credit notes, but the creation logic itself would still copy lines for credit notes when the option is ticked. [N-U23-030]
- Once posted, a debit note behaves exactly as an invoice or bill of the same direction: it increases the receivable or payable and the related income or expense and tax, in contrast with a credit note, which is a reversal document linked to the original and may be reconciled against it on creation. [N-U23-031]
- A journal may keep a dedicated number series for debit notes, on by default for sales and purchase journals; when active, debit note numbers are drawn from a separate series prefixed with a letter D, so they do not share numbering with invoices. [N-U23-032]

### STATE
- The dialog creates the debit note in draft state; it is not posted automatically. The link to the original document is read-only and cannot be copied. [N-U23-033]

### OPTIONALITY
- The add-on is optional and not installed in the studied database. Several country localizations require it; none of those is installed. The dedicated series can be turned off per journal. [N-U23-034]

### DEPENDENCY
- Depends on core accounting only. The dialog and button are shown to users of the invoicing group. Printing relies on replacing the title blocks of the standard invoice layout, which the Thai localization also replaces with a fixed title. [N-U23-035]

### CONSTRAINT
- The original document and its debit notes are linked one-to-many; a debit note cannot be created from a document that already has an original link. A document cannot be unlinked from its original by the user because the link is read-only. [N-U23-036]

### RISK
- The Thai invoice layout replaces the document title with a fixed Tax Invoice text; with both layouts active, whether a Thai debit note prints with the debit note title depends on view application order and was not verified. [N-U23-037]
- The condition meant to suppress line copying for credit notes compares a text value against a list holding a single pair and is therefore never true; credit-note lines can be copied when the option is ticked via an external call, although the dialog hides the option. [N-U23-038]

### UNKNOWN
- Whether copying business links (for example links to sales or purchase orders) onto the debit note changes delivered or invoiced quantities downstream was not traced and requires a runtime test. [N-U23-039]
- The statutory treatment of debit notes for Thailand (document title, tax invoice requirements, relation to value-added tax filing) is not provided by this add-on and is unknown from source. [N-U23-040]

## CAP-U23-03 Partner tax-number validation (VAT or TIN) and cross-border check

### WHAT
- When installed, the tax identification number typed on a business partner is validated against country rules for each supported country, normalised to a canonical format, and saved only if valid; an explicit slash can be entered to say that no valid number exists. [N-U23-041]
- Optionally, per company, numbers can also be checked against the European cross-border register through an external service run by the software vendor; the result is stored on the partner as a validity flag and logged in the partner history. [N-U23-042]
- Without this add-on the core accounting layer still calls the number check on every save, but the check is an empty placeholder that returns the number unchanged and never raises an error, so any text is accepted as a tax number. [N-U23-043]

### WHY
- Two levels of validation are offered: a quick offline check against the known rules of each country, always available, and an optional online check against the cross-border register, which is slower, needs a connection and may be unavailable. [N-U23-044]

### BUSINESS RULE
- The check runs when the number or the country of the partner is saved. A missing country or number is accepted. A single character is accepted only if it is the slash; any other single character is refused (or blanked when the saving mode asks for blanking). Importers can bypass validation with a dedicated context switch. [N-U23-045]
- Each country has its own check. The Thai check applies the Thai taxpayer identification number rule of the underlying number library to the value as typed; a country-code prefix typed before a Thai number appears not to be stripped for Thai partners, so a Thai number is expected as plain digits (to be confirmed by a runtime test). Countries with no specific rule and no library rule are accepted without any check. [N-U23-046]
- An invalid number is refused with a message naming the partner, the number and the expected format for the country; for imported or automated saves the same check can instead blank the number. [N-U23-047]
- Cross-border checking is off by default. When any company turns it on, every partner with a number is submitted whenever the number changes, except a contact whose parent has the same number, which inherits the parent result. The external reply is valid, pending, unassigned or fault; only valid sets the flag. [N-U23-048]
- A pending result is completed later: a daily scheduled job asks the external service for updates, and the service can also call a public endpoint protected by a signed token valid for one week; updates apply to every partner with that number. [N-U23-049]
- When cross-border checking applies to a partner, the requirement for a valid number used by fiscal positions additionally demands that the cross-border flag is set. [N-U23-050]

### STATE
- The cross-border flag moves from unknown to valid, or stays false after a pending, unassigned or fault result; a pending result is later updated by the daily job or by the vendor callback. [N-U23-051]

### OPTIONALITY
- The add-on is not installed in the studied database; nothing checks tax numbers there today. Cross-border checking is a per-company opt-in and only meaningful for European numbers; the external call is attempted for any number once enabled. [N-U23-052]

### DEPENDENCY
- Depends on core accounting. The cross-border check relies on an internet connection to the vendor service, an identifier and token generated per database and stored in system parameters, and a public web address of the system for the callback. [N-U23-053]

### CONSTRAINT
- Contacts and companies share the check through the commercial partner country; changing the country of a partner re-runs the check and can fail if the stored number no longer fits the new country. [N-U23-054]

### RISK
- Turning the add-on on makes saves fail for partners whose existing Thai tax number is not a valid taxpayer number or that carry a letter prefix; data imported without the bypass switch can be rejected. [N-U23-055]
- The cross-border check sends the tax number, a database identifier, a client token and a callback address to the vendor service; the number is personal or commercial data leaving the system. Failure of the service is silent apart from a history note and the flag staying false. [N-U23-056]
- The public callback endpoint accepts a signed token; anyone holding a token valid for one week can set the flag on all partners with that number, because the update runs with elevated rights. [N-U23-057]

### UNKNOWN
- The exact acceptance rules for Thai numbers depend on the version of the external number library, which was not available for inspection; whether a country-code prefix is accepted for a Thai number requires a runtime test. [N-U23-058]
- The behaviour of the vendor service for non-European numbers when cross-border checking is enabled (the code does not filter by country) is unknown and needs a network test. [N-U23-059]

## CAP-U23-04 Formula-defined taxes

### WHAT
- A tax can be defined by a custom formula instead of a percentage or fixed amount: the formula computes the tax amount from the unit price, quantity, the base amount, selected fields of the product and selected fields of its unit of measure. [N-U23-060]
- The formula is limited to a small safe language: numbers, the five allowed inputs, the four arithmetic operators, comparisons, logical and-or, a leading plus or minus sign, and the functions minimum and maximum. Product and unit fields are read with a dotted or bracketed name and only simple, non-linked fields are allowed. [N-U23-061]

### WHY
- Some levies depend on product attributes or non-linear rules that the standard percentage and fixed types cannot express; a restricted formula covers them without arbitrary program code, and the same formula text is evaluated identically on the server and in the browser. [N-U23-062]

### BUSINESS RULE
- The formula result is the tax amount. It is evaluated in the same pass as fixed-amount taxes, before price-included and price-excluded percentage taxes. A division by zero yields zero tax. The default formula is ten percent of the unit price. [N-U23-063]
- When the add-on is removed, formula taxes are converted to percentage taxes and archived, so they no longer apply to new documents. [N-U23-064]
- Fields of the product and unit of measure named in a formula are preloaded for the calculation; any other field, any unknown name, any function other than minimum or maximum, any keyword argument and any text constant is rejected when the tax is saved. [N-U23-065]

### OPTIONALITY
- The add-on is optional and not installed in the studied database; none of the 18 seeded Thai taxes is a formula tax. No formula tax is required for standard Thai value-added or withholding taxes. [N-U23-066]

### DEPENDENCY
- Depends on core accounting only and extends the shared tax calculation engine on both the server and the client. [N-U23-067]

### CONSTRAINT
- Context values must be plain numbers, text or lists convertible to a data-interchange text; the formula must pass the syntax and allowed-element check each time the tax is saved and each time it is evaluated. [N-U23-068]

### RISK
- The module description promises a second code snippet deciding whether the tax applies, but only one formula field exists; users expecting an applicability condition must encode it inside the single formula. [N-U23-069]
- Formula taxes follow the fixed-amount pass, so combining them with price-included taxes, groups, cash-basis recognition or repartition percentages was not traced and may not behave like percentage taxes. [N-U23-070]

### UNKNOWN
- Numeric behaviour of formula taxes in combination with discounts, price-included prices, rounding methods and tax reports was not executed and requires a runtime test. [N-U23-071]

## CAP-U23-05 Re-applying tax-report tags to existing journal items

### WHAT
- An administrator can re-apply the current tax-report tags of taxes to existing journal items from a chosen date forward, so that history matches a changed tax configuration; the tool is reachable only from accounting settings in developer mode. [N-U23-072]

### WHY
- After a legal change to the tax report, tags attached to taxes change, but journal items already posted keep the old tags; this tool realigns them without re-posting documents. [N-U23-073]

### BUSINESS RULE
- The start date defaults to the day after the company tax lock date, or to today when no lock exists. Choosing a date inside the locked period only shows a warning; it does not block the update. [N-U23-074]
- For every journal item of the company dated on or after the start date that relates to a tax, all existing tag links are removed and the tags of the matching tax distribution lines are written; base items take the base distribution tags and tax items take the tax distribution tags. Child taxes of a group and cash-basis entries are traced to their origin. [N-U23-075]
- For plain journal entries the invoice or refund distribution is chosen from the sign of the amount and the tax use: sale taxes use invoice for credit amounts and refund for debit amounts, purchase taxes the opposite; a zero amount is treated as invoice. [N-U23-076]
- The tool refuses to run if a child tax belongs to more than one parent group. [N-U23-077]

### STATE
- The update is a single immediate, irreversible bulk operation with no draft, preview, confirmation count or history entry. [N-U23-078]

### OPTIONALITY
- The add-on is optional and not installed in the studied database; the Thai chart is not affected unless it is installed and used. [N-U23-079]

### CONSTRAINT
- Only users with the accounting manager role can open the wizard; the update is limited to the active company and to entries on or after the chosen date; draft, posted and cancelled entries are all in scope. [N-U23-080]

### RISK
- The update writes directly to the database, bypassing the usual change checks, lock dates and audit chatter; it deletes every tag on every affected item, including tags that were not derived from the tax setup. [N-U23-081]
- No result summary or log of changed items is returned to the user, and the operation cannot be undone other than from a backup. [N-U23-082]

### UNKNOWN
- Interaction with the Thai localization post-installation tag preservation, with posted and hashed entries beyond the tag field, and with period-closed tax returns was not traced. [N-U23-083]

## CAP-U23-06 Accounting consistency tests

### WHAT
- A set of stored consistency tests can be printed as a PDF report, each test being a short program that queries the accounting tables directly and lists inconsistencies, or states the test was passed. [N-U23-084]
- The shipped tests check: overall debit-credit balance, balanced movements with a single date, reconciled invoices against their receivable or payable lines, invoice payment status, and bank statement closing balances. [N-U23-085]

### WHY
- Accountants can run quick data-integrity audits without custom reports, and can add further tests of their own. [N-U23-086]

### BUSINESS RULE
- A test returns nothing when it passes; any returned rows are printed as inconsistencies, and the report header carries the print time. A test program may read the database cursor, the user, a helper listing reconciled invoices and a result variable. [N-U23-087]
- Test programs run in the restricted evaluation sandbox but receive the live database cursor, so a program can read or write any table; only read statements are shipped. [N-U23-088]

### STATE
- Tests have no lifecycle beyond active or archived and a sequence; each print executes all selected tests afresh at render time. [N-U23-089]

### OPTIONALITY
- The add-on is optional, not installed in the studied database, and its menu is visible only in developer mode. [N-U23-090]

### CONSTRAINT
- No role is granted create or modify rights on tests: administrators may read and delete them and accounting managers may read them. Tests therefore arrive only through installed data or superuser actions. [N-U23-091]

### RISK
- Several shipped tests query a legacy invoice table that no longer exists in this version and would fail with a database error; their results cannot be trusted and they are not a valid control in this version. [N-U23-092]
- Tests read raw tables without company filter or record rules, include draft and cancelled entries, and any user-added program has direct cursor access, so test content must be treated as privileged code. [N-U23-093]

### UNKNOWN
- How a test authored after installation would be created given the access rights (data import by a superuser, another module or direct database work) was not traced. [N-U23-094]

## CAP-U23-07 External authentication - directory server and identity providers

### WHAT
- Users can sign in with their directory-server password: the system searches the corporate directory for the login, then verifies the password by attempting to bind to the directory as the found entry. Directory servers are configured per company by a system administrator, in sequence order. [N-U23-095]
- Users can also sign in with an external identity provider (for example Google, Facebook or the vendor's own account service): the browser obtains an access token from the provider, the system asks the provider's user-information address who the token belongs to and, if the subject is already linked to a local user, signs that user in; otherwise it may create a new user. [N-U23-096]
- A signed-in session created through the identity provider is later validated against the stored provider token; the token is stored on the user, hidden from all field access, and can be removed by the user or an administrator. [N-U23-097]

### WHY
- Directory sign-in lets users log in with their directory name and password and creates local users on the fly, so passwords are managed in one place and are not duplicated in the system database. [N-U23-098]

### BUSINESS RULE
- Directory sign-in is attempted only when no local user exists for the login (or, for an existing user, when the local password check fails). The directory filter must match exactly one entry; an empty password is refused before any bind to prevent unauthenticated binds. [N-U23-099]
- When the directory authenticates a login with no local user and automatic creation is on, a user is created for the configuration's company, copying a template user when one is set; the name comes from the common name of the entry and the login is used as email if it looks like one. An inactive local user is never reactivated by the directory. [N-U23-100]
- When a user changes their password and a directory server accepts the change, the local stored password is emptied so the directory becomes the only password; otherwise the normal local change applies. [N-U23-101]
- Provider sign-in links a provider identity to a local user only by a stored provider and subject pair, which must be unique. A provider identity that is not yet linked is never matched to an existing user by email; it can only create a new user, subject to the system's open or invitation-only sign-up policy, and fails if the email is already registered. [N-U23-102]
- The provider's user-information reply must contain a subject identifier (standard subject, id or user id); otherwise access is denied. Provider errors and unreachable providers lead to a generic redirect to the login page with a coded message. [N-U23-103]
- Both methods return control to the standard second-factor step when it is installed, rather than skipping it. [N-U23-104]

### OPTIONALITY
- Neither add-on is installed in the studied database. Directory sign-in needs a directory library on the server; provider sign-in needs outbound web access to the provider. The vendor's own account provider is seeded enabled when the add-on is installed, Google and Facebook are seeded disabled. In the studied database the system-wide sign-up policy allows any visitor to register, so enabling a provider could let that provider's users create portal accounts. [N-U23-105]

### DEPENDENCY
- Provider sign-in depends on the web client and the sign-up add-on; directory sign-in depends only on the base and base settings. Both depend on external services whose availability is outside the system. [N-U23-106]

### CONSTRAINT
- Only system administrators can read or change directory configurations and provider records. The provider token is unreadable through normal field access. Directory connections use plain directory protocol, optionally upgraded to TLS by a configuration flag; there is no direct secure-protocol option. [N-U23-107]

### RISK
- If the template user used for automatic creation has a local password, every automatically created directory user inherits that password as a local password, which acts as a shared master password until changed. [N-U23-108]
- The add-on documentation states that password changes are not managed in the directory, but the code does attempt a directory password change, so documentation and behaviour differ. [N-U23-109]
- The directory bind password is stored unencrypted in the database and exposed to anyone with direct database or administrator access; the form masks it only on screen. [N-U23-110]
- Provider sign-in uses the implicit token flow without a state secret tied to the browser or a nonce, and the system does not check that the token was issued for its own client (the advice to check the audience is left as a comment), so a token issued to another application by the same provider may be accepted as proof of identity. [N-U23-111]
- With a directory sign-in, the password travels to the directory server in clear text unless TLS is turned on; a directory configuration for one company can authenticate logins for any company because all configurations are consulted. [N-U23-112]
- Password strength rules of the system apply only to local passwords, so directory and provider users are governed by the external system's policy. [N-U23-113]

### UNKNOWN
- Certificate validation for the directory TLS option, directory referral handling in production, case handling of logins, and the reply format of non-default providers could not be established from source and require runtime tests. [N-U23-114]

## CAP-U23-08 Password policy and session timeout

### WHAT
- When the password policy add-on is installed, every time a password is set the system checks it against a minimum length held in a system parameter, seeded at eight characters; shorter passwords are refused with a message naming the required and actual length. Setting the minimum to zero disables the rule. [N-U23-115]
- The password entry screens (own password change, administrator multi-user change, portal security page and public sign-up) show a strength meter and, on the public pages, carry the minimum length as a browser hint. The meter scores length, number of words and number of character classes against a stricter recommendation, but only length is enforced on the server. [N-U23-116]
- When the session-timeout add-on is installed, a group of users can be given two time limits: a maximum session age after which they must sign in again, and an inactivity limit after which a lock screen asks them to confirm their identity. Each limit can optionally demand a second factor. [N-U23-117]
- Confirmation of identity can use a passkey, a one-time code (application or email) or the password, depending on what the user has set up; when a second factor is required, two different methods must be used in sequence. [N-U23-118]

### BUSINESS RULE
- Without the password policy add-on the core system accepts any non-empty password; with it, only the length rule is checked, empty values are skipped, and the minimum cannot be set below zero. Class, word and dictionary rules exist only as client-side advice. [N-U23-119]
- A user's effective timeouts are the shortest values found across all groups the user belongs to, directly or by implication, separately for limits that need a second factor and those that do not; the shortest value wins for each type. [N-U23-120]
- Enabling a session limit in the group form proposes one day with second factor; enabling an inactivity limit proposes fifteen minutes without second factor. No group in the shipped data has a limit, so nothing times out until an administrator sets it. [N-U23-121]
- Inactivity is reported by the browser through the live-update channel and also when the last browser connection closes; reopening before the limit cancels the pending lock. The age limit counts from session creation regardless of activity. [N-U23-122]
- On web routes requiring a signed-in user, an expired session limit ends the session and an expired inactivity limit raises a re-authentication request, except for a few routes needed to perform the re-authentication itself. [N-U23-123]
- The lifetime of a remembered trusted device for one-time codes is shortened to the shortest session limit that requires a second factor. [N-U23-124]

### OPTIONALITY
- Neither add-on is installed in the studied database. The password policy add-on brings two auto-installed companions for the portal and sign-up pages; they are also not installed. The session-timeout add-on's prerequisites (one-time-code, passkey, live-update modules) are installed. [N-U23-125]

### DEPENDENCY
- The password policy depends on base settings and the web client; its companions depend on portal or sign-up. The session-timeout add-on depends on the one-time-code, one-time-code by email, passkey and live-update add-ons. [N-U23-126]

### CONSTRAINT
- Only the minimum length is enforced server-side; the same rule applies to every path that sets a stored password, but not to paths that bypass the setter (directory password change that empties the local password, external identity providers). [N-U23-127]

### RISK
- Eight characters of any content is the only server-side rule even though the interface suggests stronger ones; there is no history, expiry, lockout tuning or complexity enforcement in these add-ons. [N-U23-128]
- Timeouts are enforced on interactive web routes only; whether programmatic access with a password or key is limited by the same timeouts was not established. [N-U23-129]
- A session without a recorded creation time may be treated as already expired when an age limit exists, forcing sign-in. [N-U23-130]

### UNKNOWN
- How session creation times are recorded by the web layer, how programmatic interfaces are treated, and how the lock screen behaves for external identity users were not traced and require a runtime test. [N-U23-131]

## CAP-U23-09 External (cloud) attachment storage

### WHAT
- Large files attached in the collaboration thread of a record (the chatter) can be stored in an external cloud object store instead of the system's own file storage. The browser uploads the file bytes directly to the store using a short-lived signed address; the system keeps only the attachment record with its name, type and the blob address. [N-U23-132]
- Downloads are served by redirecting the browser to a short-lived signed address generated per request; the redirect is cached for slightly less than the validity of the address. [N-U23-133]
- One provider is active at a time: Azure Blob Storage (using an application registration to obtain a delegation key and per-blob access tokens) or Google Cloud Storage (using a service account key to sign addresses). A provider and a minimum file size are chosen in settings; the default threshold is twenty megabytes. [N-U23-134]
- A migration add-on can move existing local binary attachments to the cloud store in the background, for chosen record types (message attachments only or all attachments), within size, age and batch limits; it also provides an attachment size report by record type. A reverse path can bring a cloud attachment back to local storage. [N-U23-135]

### WHY
- Offloading avoids sending large file bytes through the application server: the browser uploads directly to the store and the server receives only a placeholder file. [N-U23-136]

### BUSINESS RULE
- A file is offloaded only if it is larger than the threshold and is attached to a record type that does not use the attachment in business logic. Invoices, journal entries and payments are among the excluded record types because they keep a main attachment; when installed, expense, leave request and employee records are excluded for the same reason. [N-U23-137]
- The upload address allows only creation of one blob for five minutes; the download address allows only reading for five minutes (configurable per call) and can force a download file name. Blob names combine the attachment number, a random identifier and the file name. [N-U23-138]
- Changing the provider while attachments still live in the old provider is refused by the provider's own check; disabling or uninstalling a provider is likewise refused while attachments use it, so they must be migrated first. [N-U23-139]
- Saving a provider configuration performs a live test: it creates and reads back a test blob; for Google it also rewrites the bucket's cross-origin rules to allow any origin to read and write with the needed headers. [N-U23-140]
- The migration job selects local binary attachments that are linked to a record, are not field-stored, have a file on disk, belong to a chosen record type that is not excluded, were created more than seven days ago, and lie between the minimum and maximum file sizes (maximum one gigabyte by default). It never runs on a timer; it is started by an administrator and re-arms itself until the list is exhausted. [N-U23-141]
- Migration progress is recorded before each upload so a timeout does not re-upload the same file; an attachment that fails is skipped permanently and left local. A batch stops at a size limit or at half the worker time limit. [N-U23-142]

### STATE
- An attachment is either local binary or cloud-stored; migration changes the type to cloud-stored and clears the local content; the reverse path restores binary content from the cloud. [N-U23-143]

### OPTIONALITY
- None of the four add-ons is installed in the studied database and no attachment is cloud-stored (only binary and address attachments exist). Direct cloud upload also requires browser access to the store and cross-origin configuration. [N-U23-144]

### DEPENDENCY
- The base add-on depends on the settings and messaging modules; each provider and the migration add-on depend on the base add-on. The Google add-on needs an external Python library for signing; Azure signing is implemented in-module with a standard library. [N-U23-145]

### CONSTRAINT
- Provider credentials are stored as plain system parameters and are visible to anyone who can open the settings page or read system parameters; they are removed by database neutralisation and by provider uninstallation. [N-U23-146]

### RISK
- Because the browser uploads directly, the system never sees the bytes: no server-side size, type, malware or content check applies, and the system does not confirm the blob exists after upload (the browser deletes the attachment record on a failed upload). [N-U23-147]
- Deleting an attachment in the system does not delete the blob; orphan blobs accumulate unless a manual clean-up script is used (a script is shipped for Azure; a similarly named script for Google exists but was not inspected). Retention, backup and encryption of the external store are outside the system. [N-U23-148]
- The Google configuration step opens the bucket to cross-origin requests from any origin and requests full control of the bucket; the Azure application needs create and read rights on the container; broad service credentials stored in plain parameters increase exposure. [N-U23-149]
- When the Azure add-on is installed but another provider is selected, the Azure configuration lookup returns a method object instead of delegating, which is non-empty and truthy; the effect on a mixed installation was not traced and is a defect candidate. [N-U23-150]
- Changing provider or credentials without migrating blobs makes existing attachments unreadable; the signing key and the Azure delegation key are cached per process and refreshed on a schedule, so credential changes may take effect late unless the invalidate option is used. [N-U23-151]
- For Thailand, personal data in attachments stored in an external cloud region raises data-residency and consent questions that this software does not address. [N-U23-152]

### UNKNOWN
- Cloud region, encryption, retention, antivirus and logging of the external store, deletion of local files after migration, and behaviour of the signed addresses over real networks require runtime tests and the operator's cloud configuration. [N-U23-153]

## CAP-U23-10 Peripheral features - personal dashboards, extended address, sparse storage, bot challenge, course forum

### WHAT
- Personal dashboards: each user can build a private dashboard page by pinning views of other screens (with their filters) into a column layout; the dashboard is stored per user as a customised copy of the page layout. [N-U23-154]
- Extended addresses: a partner street is split into street name, house number and door number, kept in step in both directions; for countries flagged as enforcing a city list, the user picks a city from a reference list, which fills the city name, postal code and state. [N-U23-155]
- Sparse storage: a technical facility that lets many rarely filled fields of a record type be packed into one text column holding a data-interchange map, avoiding the database column-count limit; it is infrastructure with no business screen. [N-U23-156]
- Bot challenge: public website forms (and optionally other protected routes) can require a challenge response from an external bot-detection service; the browser gets a site key, the server verifies the response with a secret key against the service together with the client address. [N-U23-157]
- Course forum: an e-learning course can be linked to a discussion forum; the forum takes its visibility from the course, is shown to course members or the public according to the course setting, and course managers can see all course forums. [N-U23-158]

### BUSINESS RULE
- The dashboard is read-only for all internal users except for the personal customised copy; adding a view to the dashboard drops the multi-company selection from the saved context so that records are not filtered by the company chosen at pinning time. [N-U23-159]
- A city picked from the list overwrites the free-text city, postal code and state, and clearing the city or changing the country clears them again. The house number and door number fields are rebuilt into the street line as street name, space, number and, if present, a dash and the door number. [N-U23-160]
- The rule that a country must use its city list is applied only through screen visibility; no server rule prevents saving an address without a listed city. [N-U23-161]
- A sparse field can never be renamed or moved to another storage after creation; empty values are removed from the stored map; stored values are returned by reading the map. [N-U23-162]
- When no secret key is configured the bot challenge is considered inactive and every request passes. When a secret is set, a failed or missing response, a wrong secret, a suspicious action label, a timeout of three seconds or a malformed reply each block the request with a distinct message; a service outage blocks users rather than letting them pass. [N-U23-163]
- A forum linked to a course is made non-private and takes the course visibility; when a forum is unlinked from a course it becomes private to the course officer group. A forum can belong to at most one course. [N-U23-164]
- Visitors see only forums of published public courses; signed-in portal and internal users see forums of published courses that are public or for signed-in users, or where they are members; course officers see all forums, posts and tags. [N-U23-165]

### OPTIONALITY
- None of these five add-ons is installed in the studied database. The course forum add-on is flagged to install automatically when both the course and forum add-ons are present, yet it is not installed although both are; the cause is not shown by source. [N-U23-166]

### DEPENDENCY
- Dashboards depend on the spreadsheet dashboard add-on (installed). Extended addresses depend on base and contacts (installed). The bot challenge depends on the website add-on (installed) and calls an external service; another challenge add-on is installed and both run in sequence. The course forum depends on e-learning and forum add-ons (both installed). [N-U23-167]

### CONSTRAINT
- Only internal users can read the dashboard model; only the partner manager group can edit the city list while all internal users can read it; course officers can create and edit forums but not delete them; the bot-challenge keys are readable only by system administrators. [N-U23-168]

### RISK
- The challenge service receives the visitor's address and the challenge response for every protected submission and failed verifications are logged with the response token; an outage of the service blocks all protected forms. [N-U23-169]
- A logging statement on a mismatched action label uses a numeric placeholder for a text value, which makes that log line fail to render; the block itself still applies. [N-U23-170]
- The Thai address layout (sub-district, district, province) is not modelled by the extended address add-on, which offers only street parts and a flat list of cities with postal code and state. [N-U23-171]

### UNKNOWN
- Behaviour of the street splitting for Thai street text, the exact precedence when two challenge add-ons run, and the reason the course forum add-on is not installed require runtime or deployment-history checks. [N-U23-172]



---

<!-- source: U24_thailand_localization_NEUTRAL.md -->
# U24 Thailand localization - NEUTRAL KNOWLEDGE

> Clean-room layer. Source scope: Odoo 19 Community only. Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> Unit U24. Statements are tagged with identifiers that link to the restricted evidence layer. No completeness or maturity is asserted.
> Business and process language only; the restored database was used for configuration facts, never for transactions. Thai-language labels are translatable text over English keys and are never stated as requirements; legal requirements are not asserted.


## CAP-U24-01 Thai chart of accounts structure and loading

### WHAT
- A Thai chart of accounts is shipped as a loadable template: 144 numbered ledger accounts, a set of Thai tax records, tax groups, tax-report grid labels and tax-report definitions. It is applied to a company by a loading step, not merely by installing the package. [N-U24-001]
- The account list is six digits wide and organised by the first digit: assets, liabilities, equity, income, direct costs and operating expenses, plus one technical account for current-year earnings. [N-U24-002]

### WHY
- A company registered in Thailand needs a ready ledger structure, default receivable and payable accounts, default sales and purchase taxes and Thai tax-return grids from day one, so that the first invoice can be posted without manual accounting setup. [N-U24-003]

### BUSINESS RULE
- Installing the Thai package on a company that has no chart yet and whose country is Thailand loads the Thai chart automatically on that company; installing it on a company with another country does not. [N-U24-004]
- The Thai package is marked to install itself together with the accounting application, but only when at least one company in the database is located in Thailand. [N-U24-005]
- The loading step sets, for the company: Thailand as fiscal country, six-digit account codes, trade receivable 112100, trade payable 212100, down-payment account 212400, stock valuation account 113100, point-of-sale receivable 112101, exchange gain 421300, exchange loss 621200, bank suspense 111201, liquidity transfer 111202, cash difference income 421600, cash difference loss 622200, sales revenue 411100 and cost of goods sold 511100 as default income and expense accounts, early-payment discount accounts 411400 and 421500, and the 7 percent output and input VAT taxes as default sale and purchase taxes. [N-U24-006]
- After the template data is loaded the system also creates a bank account, an outstanding-receipts account and an outstanding-payments account from the bank prefix 11120, and gives each bank, cash and credit journal the company suspense and cash-difference accounts. [N-U24-007]
- The standard journals come from the generic accounting template, not from the Thai package: sales, purchases, miscellaneous, exchange difference, cash-basis taxes and one bank journal, plus an inventory valuation journal when stock accounting is present. The sales and purchase journals take the company default income and expense accounts. [N-U24-008]
- Account type counts in the shipped list are: 42 expense, 22 fixed asset, 15 current asset, 13 current liability, 12 depreciation expense, 7 direct cost, 6 non-current asset, 6 other income, 4 receivable, 4 income, 3 cash, 3 payable, 3 non-current liability, 3 equity and 1 current-year earnings. Thirty accounts are flagged reconcilable. [N-U24-009]
- The chart reserves dedicated tax accounts: undue input VAT 114100, input VAT 114200, creditable withholding 114300, VAT receivable 114400, withholding receivable 114401, undue output VAT 213100, output VAT 213200, withholding payable accounts for forms PND 1, PND 3, PND 53 and PND 54 (213300 to 213303), VAT payable 213400 and withholding payable 213500. The VAT and withholding receivable and payable accounts are flagged as non-trade. [N-U24-010]

### STATE
- A company moves from no chart to Thai chart loaded; loading the same chart again is a reload that refreshes records, while switching to a different chart on a company without accounting entries removes the previous chart records first. [N-U24-011]

### OPTIONALITY
- Only 24 distinct accounts are wired into company defaults, tax records or tax groups by the template; the other accounts exist for manual selection. Several reserved accounts (undue VAT, PND 1, PND 54, corporate income tax, prepaid income tax) are not used by any shipped tax. [N-U24-012]
- A set of twelve fixed-asset category definitions (land improvements, buildings, machinery, vehicles, computers, software, goodwill and others, with straight-line periods) ships as data, but the Community accounting core has no asset model and does not load it. [N-U24-013]

### DEPENDENCY
- The Thai package depends on the core accounting application and on the EMV payment-QR bridge only. Nothing else in the Community source depends on the Thai package. [N-U24-014]
- Chart records are owned per company: account codes are stored per company, and a loaded chart is propagated to subsidiary companies by the same loader. Company-structure behaviour is studied elsewhere. [N-U24-015]

### CONSTRAINT
- Loading a chart requires an administrator; all template records are loaded in the English source language and translated afterwards, so the Thai names and descriptions are a translation layer over stable English keys. [N-U24-016]

### RISK
- The template supplies no account groups, no fiscal positions, no cash journal and no reconciliation rules of its own; the transfer-account prefix is passed as a template key string instead of a digit prefix; the cash-basis feature switch is turned on for the company although no shipped tax is cash-basis. [N-U24-017]

### UNKNOWN
- Whether the account list, names and numbering conform to current Thai statutory chart or financial-statement requirements is not determinable from the source. Whether an external fixed-asset module would load the asset definitions is not determinable here. [N-U24-018]


## CAP-U24-02 Thai VAT: taxes, tags, accounts and standard sale and purchase entries

### WHAT
- The Thai package ships six VAT records: output and input VAT at 7 percent, output and input VAT at 0 percent, and output and input VAT labelled 0 percent exempt. Each VAT record has separate invoice and credit-note distribution lines for the base and for the tax. [N-U24-019]
- On a customer invoice the 7 percent output VAT credits account 213200 (output VAT) and its base carries the grid label sales amount; on a vendor bill the 7 percent input VAT debits account 114200 (input VAT) and its base carries the label purchase amount entitled to input-tax deduction. Credit notes use the same accounts and labels with the opposite effect. [N-U24-020]
- The zero-rate output tax base is labelled both as sales amount and as sales subject to the 0 percent rate; the exempt output tax base is labelled both as sales amount and as exempted sales. Output tax lines of all three output taxes are labelled output tax. [N-U24-021]

### WHY
- The grid labels attached to base and tax lines let tax-report definitions total each box of the Thai VAT summary directly from posted entries, without separate manual classification. [N-U24-022]

### BUSINESS RULE
- New products default to the 7 percent output VAT for sales and the 7 percent input VAT for purchases, taken from the company default taxes that the Thai template sets. A different tax must be chosen by the user or by a fiscal position for zero-rated or exempt supplies. [N-U24-023]
- The company default is that sales prices exclude tax and tax is added on top; this can be changed per tax by an override, and the company-wide choice cannot be changed once the company has started invoicing. Tax rounding follows the company method, which defaults to rounding per tax over the whole document. [N-U24-024]
- All 18 Thai taxes have the same sequence number, none affects the base of another and none is price-included by override except the four sale-side withholding taxes which are forced to price-excluded. Therefore withholding is computed on the untaxed amount, not on the amount including VAT. [N-U24-025]
- Three tax-report definitions are shipped for Thailand: a VAT report with numbered lines 1 to 12 (sales, zero-rated and exempt sales, taxable sales, output tax, purchases, input tax, tax payable, excess tax, excess carried forward, net tax payable, net excess), a PND 53 report and a PND 3 report. Output lines are read with reversed sign; payable is output minus input when positive, excess is input minus output when positive. [N-U24-026]
- VAT tax lines are flagged as feeding a tax closing entry while withholding tax lines are not; the five tax groups carry payable and receivable accounts for that purpose. The Community accounting source contains no routine that creates the closing entry or sets the tax lock date from it. [N-U24-027]
- Descriptions attached to the tax accounts (English source text with Thai translations, informational only) describe month-end steps that the source does not automate: undue VAT moved to VAT on payment, input and output VAT balances moved to VAT payable or receivable at month end, and withholding balances consolidated into one withholding account. Such transfers are manual journal entries. [N-U24-135]

### STATE
- A tax is active or archived; a customer or vendor document keeps the tax lines it was posted with. No Thai tax is cash-basis, so VAT is recognised when the document is posted, not when it is paid. [N-U24-028]

### OPTIONALITY
- No fiscal position ships with the Thai chart, so export, foreign-customer and special-regime tax mapping is not automated; a user selects the zero-rate or exempt tax per line or creates fiscal positions. A customer or a vendor may carry a manually assigned fiscal position that always wins. [N-U24-029]
- For sales documents in a foreign currency the document totals can also show the taxes in the company currency; this company setting is on and applies only when the document currency differs from Thai baht. [N-U24-030]

### DEPENDENCY
- The tax-report definitions are data only: the Community accounting source stores them but contains no screen, menu or engine that renders them, so producing a VAT return from them depends on functionality outside Community. [N-U24-031]

### CONSTRAINT
- The invoice and credit-note distribution of every tax must mirror each other, positive percentages must add to 100 and every tax must belong to a tax group of its country; a tax cannot be deleted once used. [N-U24-032]
- Taxes, tax groups and fiscal positions can be read by all internal users and changed only by the accounting administrator role; tax, group, account, journal and partner bank records are company-scoped by multi-company rules, so a company sees only its own Thai taxes and accounts. [N-U24-134]

### RISK
- The zero-rate and exempt VAT taxes have no tax group in the template and inherit the first Thai group, which is the 1 percent withholding group, so document totals can show them under a withholding heading. [N-U24-033]
- Zero-rate input VAT and exempt input VAT have identical grid labels and accounts, and zero-rate and exempt output VAT differ only in one grid label, so only the label distinguishes them in reports. [N-U24-034]
- If the company default were switched to price-inclusive, the purchase-side VAT and withholding taxes would be combined into one batch and the base extracted by the sum of their percentages, which does not match extracting 7 percent VAT alone; the sale-side withholding taxes are protected by their price-excluded override. The switch is blocked once invoicing started. [N-U24-035]
- The report definitions use a literal baht currency in their payable and excess formulas, and two tag families (surcharge and excess carried forward) are never attached to any shipped tax. [N-U24-036]

### UNKNOWN
- Numeric results of combined 7 percent VAT and withholding on one line, rounding differences by method, and the exact printed form of the VAT summary are not determinable without execution. Statutory conformity of grids and rates is not determinable from source. [N-U24-037]


## CAP-U24-03 Withholding tax in the Thai tax set

### WHAT
- The Thai tax set contains twelve withholding taxes, all expressed as negative percentages of the line amount: eight on the purchase side and four on the sale side, at 1, 2, 3 and 5 percent. [N-U24-038]
- Purchase-side withholding exists twice per rate: one set for payees that are companies, whose base and tax lines are labelled for the PND 53 form and posted to account 213302, and one set for payees that are individuals, labelled for the PND 3 form and posted to account 213301. The rate names in the description are transportation 1, advertising 2, service 3 and rental 5 percent. [N-U24-039]
- Sale-side withholding (tax withheld by customers) is posted to account 114300, a current-asset account, as a creditable amount; its base and tax lines carry no report label, and the four taxes are forced to price-excluded. [N-U24-040]
- An optional accounting add-on lets a tax be flagged as withheld on payment: the tax is ignored when the invoice or bill is computed and the amounts are registered on the payment, which then books cash net of withholding, a withheld-tax item and a pair of base items, and requires a withholding number per line. The Thai tax set does not use it and the Thai package does not depend on it; no Thai tax carries the flag. [N-U24-047]

### WHY
- Withholding is modelled as an ordinary negative tax so that, with no extra module, a vendor bill or customer invoice can show the withheld amount, reduce the amount payable or receivable and accumulate the withheld total in a liability or asset account. [N-U24-041]

### BUSINESS RULE
- All twelve taxes are recognised on the document, at posting, not at payment: the cash-based option is not used for any Thai tax. A vendor bill carrying VAT and withholding therefore shows the payable already reduced by the withheld amount and the withheld amount already sitting in the withholding liability account. [N-U24-042]
- Because VAT does not alter the base of other taxes and every Thai tax has the same sequence number, withholding is computed on the amount before VAT. [N-U24-043]
- Withholding taxes belong to four groups by rate (1, 2, 3, 5 percent), shared by the company-payee, individual-payee and sale-side variants; the groups point to payable account 213500 and receivable account 114401, which no shipped tax line uses directly. [N-U24-044]
- Withholding tax lines are not flagged as feeding the tax closing entry, unlike VAT lines. [N-U24-045]
- Two return-style report definitions exist, one for PND 53 and one for PND 3, each showing total income (base label), total remittance (tax label), surcharge and a total; no report definition exists for PND 1, PND 2, PND 54 or for the sale-side withholding. [N-U24-046]
- The add-on accepts only sale or purchase taxes with a negative percentage that are not group or division types, forces on-invoice recognition and price-excluded, and takes the number from the user or from a sequence on the tax. Under the add-on the withheld amount would be recognised at payment time instead of document time. [N-U24-048]
- The account descriptions also say that sale-side withheld tax is a prepaid amount claimable against year-end corporate income tax and that the form-specific withholding liabilities are consolidated at month end; no routine or tax record performs these steps. [N-U24-136]

### STATE
- Withholding on a document is a posted tax line like any other: it follows the document through posting, reversal by credit note (mirrored distribution) and cancellation; there is no separate withholding record, status or certificate object in the Thai set. [N-U24-050]

### OPTIONALITY
- The add-on is not installed in this database. Converting Thai withholding taxes to payment-time recognition is technically allowed by the add-on rules but would move their effect from the document to the payment and change when report labels are populated; the consequences for existing history are not determined. [N-U24-049]

### DEPENDENCY
- The add-on and the Thai package are independent. Other country packs that depend on the add-on are listed in the boundary section; they are a future optional pack family and are not studied here. [N-U24-051]

### CONSTRAINT
- The payee type (company or individual) is chosen by picking the matching tax; nothing in the Thai set selects it from the partner, because the tax file has no fiscal-position or original-tax mapping values. [N-U24-052]

### RISK
- Purchase withholding taxes have no price-excluded override: only the company-wide price setting keeps them excluded, unlike the sale-side taxes. [N-U24-053]
- Booking withholding at document time may differ from the point at which a payer is obliged to withhold; which is correct is a legal question that source evidence cannot settle. [N-U24-054]
- Reserved accounts for PND 1 and PND 54 withholding exist, but there is no tax record for payees in those categories (for example foreign payees); such withholding is not modelled. [N-U24-055]

### UNKNOWN
- No withholding certificate, no certificate numbering, no payee-level withholding statement, no return filing format and no clearing of creditable withholding against income tax exist in the Community source. Whether the shipped rates and categories match current statutory rates is not determinable from source. [N-U24-056]


## CAP-U24-04 Tax invoice, receipt, credit note and debit note documents

### WHAT
- For a company whose fiscal country is Thailand the printed customer invoice uses a Thai variant of the standard invoice layout: the document title of a posted customer invoice is replaced by the fixed English source text Tax Invoice, and the customer tax identifier line is followed by a branch label. [N-U24-057]
- The branch label is the word Branch followed by the customer's company registration value when one is present, or the word Headquarter when it is empty; it is shown only for customers that are companies located in Thailand. Both words are translatable source strings with Thai translations. [N-U24-058]
- A second printable document, the Commercial Invoice, is offered for sales-journal documents of Thai companies; it prints the standard invoice layout (title Invoice, not Tax Invoice) in the customer's language, and refuses to print records that are not invoices or receipts. [N-U24-059]
- Credit notes, draft and cancelled documents keep the standard titles (Credit Note, Draft Invoice, Cancelled Invoice); vendor bills and vendor credit notes use their standard titles. Receipt document types exist (sales and purchase receipt) but the standard layout has no title branch for them, and the payment receipt document has the standard title Payment Receipt. [N-U24-060]

### WHY
- The localisation makes the standard invoice carry a Thai title and a buyer-branch label while leaving numbering, taxes and posting to the standard accounting flows. [N-U24-061]

### BUSINESS RULE
- Which layout is used is decided by the company's fiscal country, not by the user interface language: a company whose fiscal country is Thailand always prints the Thai variant. The title text itself is a fixed English source string in the layout; its Thai rendering comes from the translation catalogue and appears when the document is rendered in the customer's language, so a customer with an English language record sees the English words even though the Thai layout is selected. [N-U24-062]
- Document numbers come from journal sequences. Sales documents use a yearly pattern of journal code, four-digit Gregorian year and five-digit counter; purchase documents use journal code, year, month and a four-digit counter; credit notes get a prefix letter when the journal has a dedicated credit-note sequence (default on for sales and purchase journals); payments get a payment prefix on a journal with a dedicated payment sequence. [N-U24-063]
- The printed invoice shows the buyer tax identifier (label Tax ID) and address, the seller tax identifier from the company layout, dates, origin, payment reference, lines, tax totals grouped by tax group and an optional payment QR. No Thai-specific rule forces a buyer tax identifier, a branch value, a seller branch or any other field before posting. [N-U24-064]
- The generic accounting layout can print the total amount in words when a company switch is on; the Thai package does not set this switch. The words are produced by an external number-to-words library in the language of the current user, falling back to English when that library lacks the language; Baht and Satang are the unit labels of the Thai currency. [N-U24-065]
- An optional add-on lets a posted customer or vendor invoice or credit note be debited through a wizard, producing a new invoice linked to the original, with a dedicated sequence prefix letter D when the journal has a dedicated debit-note sequence, and replaces the invoice title by Debit Note when the document is linked to an original. It is not installed in this database and not part of the Thai package. [N-U24-066]

### STATE
- Titles follow document type and state: posted, draft and cancelled customer invoices, credit notes and vendor documents have separate titles; the Thai variant overrides only the posted customer-invoice title. [N-U24-067]

### OPTIONALITY
- The total-in-words switch, the payment QR, the credit-note and debit-note dedicated sequences and the commercial invoice document are all optional or configurable; the commercial invoice is only offered for Thailand sales journals. [N-U24-068]

### DEPENDENCY
- The Thai layout inherits the standard invoice layout; when the debit-note add-on is also installed its title changes apply to the standard layout first, and the Thai title replacement then overrides the posted-invoice title, so a posted debit note of a Thai company is expected to print the Thai invoice title instead of Debit Note (not executed). [N-U24-069]

### CONSTRAINT
- Printing the Commercial Invoice on anything other than a customer or vendor invoice or receipt raises an error. A debit note can only be created from posted invoices, vendor bills and credit notes, and not from a document that is already linked to a debit note. [N-U24-070]

### RISK
- Numbering uses the Gregorian year; no Buddhist-era year printing exists in sequences, date formats or the layout, and the Thai language uses a day-month-year numeric date pattern. [N-U24-071]
- The Thai package shows the buyer branch but no seller branch, and has no abbreviated tax invoice, no combined receipt and tax invoice, and no electronic tax invoice or receipt output; a Thai invoice presented as a legal tax invoice depends on content that is not enforced. [N-U24-072]

### UNKNOWN
- Statutory content, numbering, language and format requirements for tax invoices, credit notes, debit notes and receipts are not determinable from source; any requirement needs an authoritative statutory source. Whether the external words library renders Thai text, and the exact printed result, are not determinable without execution. [N-U24-073]


## CAP-U24-05 Thai partner identity (tax ID, branch) and address

### WHAT
- A Thai party is identified by the generic tax-identifier field (labelled Tax ID for Thailand), a free-text company registration field, and one Thai addition: a computed branch label for company partners located in Thailand. [N-U24-074]
- The branch label is the word Branch followed by the registration value, or Headquarter when the registration value is empty. It is computed on demand, not stored, appears on the invoice layout, and is empty for partners that are not companies or are not in Thailand. [N-U24-075]

### WHY
- The invoice shows the buyer's tax identifier and a branch label; the localisation reuses the generic registration field for the branch value instead of adding a dedicated field. [N-U24-076]

### BUSINESS RULE
- In this database no tax-identifier validation runs: the core validation entry point is a placeholder that returns the value unchanged for every country, because the optional validation add-on is not installed. [N-U24-077]
- When the optional validation add-on is installed, a partner in Thailand has its identifier checked by the Thai taxpayer-identification routine of an external standards library; hyphenated and compact 13-digit forms with a correct check digit are accepted in the add-on tests, a wrong final digit or a letter is rejected, and a failure raises a validation error quoting the expected format (13 digits). [N-U24-078]
- Validation can be skipped for imports through a context switch, can be set to blank the value instead of raising, and applies on creation and on every change of the identifier or country; a single slash means explicitly no valid identifier. [N-U24-079]
- The partner form warns, without blocking, when another partner has the same tax identifier or the same registration value in the same company scope; branches of one juristic person share an identifier and each branch uses the same registration field for its own code, so these warnings can appear for legitimate branches and head office. [N-U24-080]
- Thai addresses use the generic address layout (street, second street line, city, province and postcode, country) and 77 Thai provinces exist as reference data; there are no district or sub-district fields. The optional extended-address add-on only splits a street value into name, number and door number with a generic pattern and ships no Thai city list. [N-U24-081]

### STATE
- None recorded for this capability.

### OPTIONALITY
- Tax-identifier validation and extended address splitting are optional add-ons and are not installed. The identifier label for Thailand is the generic Tax ID because the country has no custom label. [N-U24-082]

### DEPENDENCY
- The branch label depends on the partner being a company with country Thailand; an invoice addressed to a contact person of a company (a child partner that is not itself a company) shows no branch label. [N-U24-083]

### CONSTRAINT
- Branch values are not validated: any text, including a non-numeric value or an empty value, is accepted and an empty value is shown as Headquarter. [N-U24-084]

### RISK
- The external library that performs Thai identifier checks is not part of the source tree, so its exact rules (length, check digit, handling of separators) cannot be confirmed here; the stored form after validation (compact or as typed) is not determinable without execution. [N-U24-085]
- Reusing the generic registration field for the Thai branch code means any other use of that field for the same partner (a different registry number) would be printed as a branch. [N-U24-086]

### UNKNOWN
- Statutory format of Thai taxpayer and branch identifiers, and whether a branch code must be a five-digit number, are not determinable from source. [N-U24-087]


## CAP-U24-06 Payments, PromptPay and EMV QR and bank and journal setup

### WHAT
- A payment QR can be printed on customer invoices. The generic bridge builds an EMV merchant-presented QR payload (format indicator, dynamic type, merchant account information, merchant category, currency code, amount, country, merchant name, merchant city, optional additional data and a CRC-16 trailer). [N-U24-088]
- For bank accounts held by a partner located in Thailand the Thai package supplies the PromptPay merchant account information (tag 29 with the PromptPay application identifier A000000677010111 and one of three proxy identifiers: mobile number, merchant tax identifier or e-wallet identifier), so PromptPay is supported as a static-account credit-transfer QR carried on the invoice. [N-U24-089]
- A separate online route exists: the payment application has a PromptPay payment method record, inactive here, that four gateways (Adyen, AsiaPay, Stripe, Xendit) list; every real gateway in this database is disabled. [N-U24-090]

### WHY
- A customer paying a Thai invoice with a banking app can scan the QR and transfer the exact residual amount to the seller's PromptPay identifier without typing account details. [N-U24-091]

### BUSINESS RULE
- A QR appears only when the company switch for invoice QR codes is on (it is off here), the document is a customer or vendor invoice or receipt with a residual amount, a bank account is chosen for the document, that account's holder is in Thailand, the account has a PromptPay proxy type and value, the holder has a city, and the document currency is Thai baht. The first eligible method is chosen unless a method is stored on the document. [N-U24-092]
- For Thai bank accounts the proxy type must be mobile number, merchant tax identifier or e-wallet identifier (or none); a merchant tax identifier must be exactly 13 digits and a mobile number exactly 10 digits. A mobile number's leading zero is replaced by 66 and padded to 13 digits in the payload. [N-U24-093]
- The payload carries amount and merchant name but, for Thailand, no additional reference data and the default merchant category code 0000; the include-reference option on the bank account therefore has no effect in Thailand. [N-U24-094]
- The Thai template creates one bank journal with a bank account 111203, outstanding receipts and payments accounts, suspense 111201 and manual in and out payment methods plus a cheque-printing method; it does not create a cash journal although cash account 111100 and a cash prefix exist. [N-U24-095]

### STATE
- A QR method on a document starts empty and is stored on first successful generation; changing the document currency away from baht after a Thai QR method is stored makes printing raise an error instead of silently skipping. [N-U24-096]

### OPTIONALITY
- The QR is optional and company-controlled; the online PromptPay method and its gateways are optional integrations whose contracts, credentials and failure behaviour are studied in the payment-provider unit and are runtime items. [N-U24-097]

### DEPENDENCY
- The Thai QR depends on the generic EMV bridge and on a bank account whose holder is the company partner for customer documents; the QR does not reconcile or register a payment, which remains a manual payment or bank-statement step. [N-U24-098]

### CONSTRAINT
- The Thai bank-account checks run on creation and change of the proxy fields; errors name the account number. Merchant name is cut to 25 characters and city to 15 characters. [N-U24-099]

### RISK
- The payload length fields count characters while the checksum is computed over encoded bytes, so merchant names or cities containing Thai script may produce a payload whose lengths or checksum are not what scanners expect; this was not executed. [N-U24-100]
- Error messages for Thai bank accounts name a different country's QR scheme (copied wording), and the generic missing-information check is ineffective because it tests a value that is always present; the Thai checks are the effective ones. [N-U24-101]
- Invoices in a foreign currency cannot carry a Thai QR; the amount shown is the residual in the document currency, never a converted baht amount. [N-U24-102]

### UNKNOWN
- Whether scanners and Thai banking apps accept the produced payload (merchant category, dynamic indicator, absent reference tag) and the behaviour of the online gateways are runtime items not determinable from source. [N-U24-103]


## CAP-U24-07 Period, lock and fiscal-year behaviour

### WHAT
- Accounting periods in the Community accounting application are defined by a company fiscal year end (day and month, default 31 December) and by lock dates; there is no tax-return periodicity setting, no period objects and no tax closing routine. [N-U24-104]

### WHY
- A fiscal year end lets sequences, opening balances and year-based reports align with the company's accounting year, while lock dates stop new or changed entries in closed periods. [N-U24-105]

### BUSINESS RULE
- The fiscal year end defaults to day 31 and month 12 and the Thai template does not change it; any valid day and month can be chosen, and the day is checked against the month length. A year end other than 31 December changes sales and other sequence prefixes to a two-digit year span. [N-U24-106]
- Five company lock dates exist: fiscal year, tax return, sales, purchases and hard lock. An entry dated on or before a lock date is moved to a later date according to its journal sequence; the hard lock cannot be excepted, the others can be bypassed by lock exceptions. In this database all lock dates are empty. [N-U24-107]
- The tax return lock date is documented as being set automatically when a tax closing entry is posted, but the Community source contains no routine that creates the closing entry, no return periodicity field and a deprecated placeholder for per-country return configuration that does nothing. [N-U24-108]
- The Thai VAT report definition refers to a previous return period for the excess carried forward, an idea that the Community source defines nowhere else. [N-U24-109]

### STATE
- A period is open until a lock date is set at or after its end; moving a lock date forward closes earlier entries, and an exception can reopen them for a user and a bounded time except under a hard lock. [N-U24-111]

### OPTIONALITY
- Fiscal year end, lock dates and exceptions are configuration; the Thai package sets none of them. [N-U24-110]

### DEPENDENCY
- None recorded for this capability.

### CONSTRAINT
- The fiscal year last day must be valid for the month (29 February is explicitly allowed). [N-U24-112]

### RISK
- No calendar other than Gregorian exists in sequence naming, date formats or lock dates, and the Thai language record uses a day-month-year numeric pattern; Buddhist-era years are not supported in Community source (the browser may format dates by its own locale rules, which was not examined). [N-U24-113]

### UNKNOWN
- Statutory Thai tax periods, filing deadlines and whether a calendar-year fiscal year suits a given Thai company are not determinable from source; browser date rendering for the Thai locale is a runtime item. [N-U24-114]


## CAP-U24-08 Thai statutory-output gaps (not present in Community)

### WHAT
- This capability lists statutory outputs commonly expected in a Thai accounting setup and states, for each, what the Community source provides and what it does not. Absence is recorded with the search that was run; none of it is stated as a legal requirement. [N-U24-115]
- Present in Community source for Thailand: a chart of accounts, 7 percent, 0 percent and exempt VAT taxes with report grid labels, twelve withholding taxes, report definitions for a VAT summary, PND 53 and PND 3, a Thai tax-invoice title and buyer-branch label, a commercial invoice document, PromptPay merchant QR support, and the generic amount-in-words and debit-note facilities. [N-U24-116]

### WHY
- None recorded for this capability.

### BUSINESS RULE
- None recorded for this capability.

### STATE
- None recorded for this capability.

### OPTIONALITY
- None recorded for this capability.

### DEPENDENCY
- None recorded for this capability.

### CONSTRAINT
- None recorded for this capability.

### RISK
- No VAT return form, filing file or period-based VAT submission exists; the VAT summary is a stored definition with no screen or engine in Community, so a VAT return cannot be produced from Community source alone. [N-U24-117]
- No withholding certificate document, certificate numbering, withholding return forms, payee withholding statement or filing format (for PND 1, 2, 3, 53 or 54) exists; only grid labels on entries and two report definitions exist. [N-U24-118]
- No electronic tax invoice or electronic receipt format, submission or signing exists: the electronic-invoice framework in Community lists country-specific formats and Thailand is not among them. [N-U24-119]
- No Buddhist-era year printing exists, no abbreviated or combined tax invoice or receipt, no seller-branch printing, and no enforcement of mandatory Thai tax-invoice fields. [N-U24-120]
- Amount in words is present only generically: it is a company switch, English fallback depends on an external library, and whether Thai words are produced is not determinable from source. [N-U24-121]
- No VAT purchase or sales ledger book, no input-VAT proration or non-deductible split, no payee categories for foreign payees, no withholding clearing against income tax and no Thai statutory financial-statement formats exist in Community source. [N-U24-122]
- No tax-return periodicity, tax closing entry or Thai tax calendar exists (see the period capability). [N-U24-123]

### UNKNOWN
- Whether any of these outputs is legally required for a given Thai company type, including a foreign-owned subsidiary, branch, representative office or regional office, is not determinable from source; any requirement needs an authoritative statutory source and is UNKNOWN here. [N-U24-124]


## CAP-U24-09 Country-pack boundary and cross-border touchpoints

### WHAT
- The source tree holds 231 country-localisation packages; one (Thailand) is installed in this database and 230 are not. Of the 230, 227 are country packs for other jurisdictions, now classed as a future optional country pack family, and three are generic mechanisms whose name starts with the localisation prefix (withholding on payment, its point-of-sale companion, and an electronic-invoice test helper). [N-U24-125]
- The 227 packs are described only by structure: base country pack (116), electronic-invoice (34), other extension (39), point-of-sale (17), stock, sale, purchase or website bridge (16) and payroll or HR (5). A mechanical table in the technical layer lists each pack's installation state, country gate, auto-install setting, generic accounting models it extends and core hooks it overrides. [N-U24-126]

### WHY
- None recorded for this capability.

### BUSINESS RULE
- A country pack that is set to install automatically with accounting installs only when a company in the database is in its country; with the single company in Thailand none of the other 118 country-gated packs whose dependencies are met would install. A company located in another country would trigger its pack. [N-U24-127]
- Creating foreign taxes for a foreign-country fiscal position installs that country's pack on demand and copies its taxes onto the company; this is the one generic path by which a Thai database could acquire another country's pack, and it requires an accounting manager. [N-U24-128]
- Cross-border and multi-currency behaviour touched by the Thai package: Thai baht as company currency, foreign-currency invoices with taxes optionally shown in baht, zero-rate and exempt taxes selected manually for exports, no foreign payee withholding, a Thai QR limited to baht, and a report definition that allows foreign tax registrations; none of this is a country-pack matter and deeper mechanics are in the multi-currency and translation studies. [N-U24-129]
- The Thai package extends only a few generic structures: the invoice document selector, the report print guard, the partner (one computed label), the bank account (QR proxies) and company data written by the template. It adds no company-level field, so company-structure questions (subsidiaries, branches, representative and regional offices) are governed by the generic company hierarchy and chart loader. [N-U24-130]

### STATE
- None recorded for this capability.

### OPTIONALITY
- None recorded for this capability.

### DEPENDENCY
- Packs that depend on the withholding-on-payment add-on or on the debit-note add-on are listed by name in the technical layer; they are not studied for rules. [N-U24-131]

### CONSTRAINT
- None recorded for this capability.

### RISK
- 119 packs extend core accounting structures; if one were installed beside the Thai package it could change posting, numbering, tax computation or document selection for the same company. The Thai package's own document selector is an override point shared with such packs. [N-U24-132]

### UNKNOWN
- How a Thai subsidiary of a foreign group, a foreign-company branch, a representative office or a regional office should be structured for statutory purposes is not determinable from source; company-structure behaviour is studied separately. [N-U24-133]


---

<!-- source: U25_multicurrency_international_NEUTRAL.md -->
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


---

<!-- source: TXS_thai_statutory_neutral.md -->
# TXS — Thai Statutory Requirements (Neutral Statements)

DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION — neutral summary of what official Thai sources state for a legal entity operating in Thailand, as read on **2026-10-02**. Each statement points to the register entry (Stat-ID) in TXS_thai_statutory_source_register.md, where the official URL, provision, language and status are recorded. This file names no software product and no vendor structure. It is not legal or tax advice; no coverage or compliance conclusion is drawn.

Status key (from the register): V = VERIFIED-OFFICIAL, S = OFFICIAL-SUMMARY-ONLY, U = UNVERIFIED, C = CONFLICT. "Check currency" marks items with frequent change.

## VAT registration and rate

- **N-TXS-001** A person selling goods or providing services in the course of business in Thailand, and an importer, is within the scope of VAT. (S01-01, V)
- **N-TXS-002** A business whose annual tax base exceeds the small-business limit must apply for VAT registration within 30 days; the limit set by the Royal Decree in force that I read is 1,800,000 baht per year (calendar year for individuals; accounting period for juristic persons). (S01-02, S01-03, V)
- **N-TXS-003** A registration certificate is displayed at each place of business; a multi-location business registers at the area office of its head office. (S01-06, S11-01, V)
- **N-TXS-004** The Revenue Code states a 10% statutory rate, which a Royal Decree may lower. (S02-01, V)
- **N-TXS-005** A Royal Decree published on 23 Aug 2026 keeps the rate at 6.3% (7% including a 0.7% local-tax share, per RD's own explanation of an earlier decree) for liabilities arising up to 30 Sep 2027; it is time-limited and has been renewed by successive decrees. Check currency. (S02-02, S02-04, S02-05, V; the 7% total for the current period is S)
- **N-TXS-006** The rate that applies after 30 Sep 2027 is not established by the sources read. (S02-05, U)

## Zero-rated, exempt, input tax

- **N-TXS-007** Zero-rated supplies include exports, services performed in Thailand and used abroad, international air or sea transport, and supplies to specified government-aid, UN and diplomatic recipients. (S03-01, V)
- **N-TXS-008** A registrant exporting in its own name keeps evidence of the foreign order, domestic purchase invoices, export documents, payment arrangements and the customs export declaration. (S03-02, V)
- **N-TXS-009** Exempt supplies are listed by category in the Revenue Code (for example unprocessed agricultural goods, educational, medical and professional services, domestic transport, property rental). (S03-03, V)
- **N-TXS-010** A registrant offsets monthly input tax against output tax; an excess is carried forward or refunded under Royal-Decree procedure. (S04-01, S09-06, V)
- **N-TXS-011** Input tax is non-creditable in listed cases: no tax invoice or proof, invoices with material errors or missing required items, purchases unrelated to the business, entertainment-type expenses, invoices from unauthorised issuers, and categories prescribed by the Director-General (for example passenger cars of up to 10 seats with exceptions). (S04-02, S04-03, V)
- **N-TXS-012** Where inputs serve both taxable and non-taxable activity, input tax is allocated under Director-General procedure. (S04-04, V)

## Time of supply

- **N-TXS-013** For goods, VAT liability arises at the earliest of delivery, transfer of ownership, payment received or tax invoice issued; for services, at payment received, or earlier on invoice or use; for imports, at payment of duty or customs entry. (S05-01, S05-02, S05-03, V)
- **N-TXS-014** Own use of goods outside the production process, use of passenger cars of up to 10 seats, missing stock items, and stock on cessation are deemed sales with VAT due but no tax invoice. (S05-04, V)

## Tax documents

- **N-TXS-015** A registrant issues a tax invoice immediately when VAT liability arises, with a copy kept; each place of business issues its own unless permitted otherwise. (S06-01, V)
- **N-TXS-016** A full-form tax invoice shows: the words "tax invoice", issuer name or address or taxpayer ID, buyer name or address, serial number, goods or services description and value, VAT separately, and the date. (S06-02, V)
- **N-TXS-017** A full-form invoice issued from 1 Jan 2015 also shows the buyer's taxpayer ID (if registered) and a head-office or branch designation for seller and registered buyer (head office as a word, abbreviation or code 00000; branch as branch number or five-digit code). (S06-06, S11-03, V)
- **N-TXS-018** An abbreviated tax invoice may be issued by retailers selling small amounts to many customers, shows price as VAT-inclusive, may be in Thai or English, and needs Director-General approval for non-retailers. (S06-04, V)
- **N-TXS-019** Tax invoices are in Thai (or Thai plus English per RD's guide) and in Thai currency, unless the Director-General approves another language or currency. (S06-03, V)
- **N-TXS-020** Erased or overwritten items on a full-form tax invoice make the related input tax non-creditable per RD's guide. (S04-05, S)
- **N-TXS-021** A debit note is issued when value rises after sale and a credit note when value falls; each states original and corrected values and the reason, and each adjusts output tax in the month of issue and input tax for the recipient. Both are tax invoices for VAT purposes. (S07-01, S07-02, V)
- **N-TXS-022** A lost or damaged paper tax invoice is replaced by a substitute marked as such; a defective electronic invoice is replaced by a new document with a new number that states it cancels the earlier one; a lost electronic invoice is simply resent. (S07-03, S07-04, S07-05, V)
- **N-TXS-023** A commercial receipt is a distinct obligation from a tax invoice: a payee issues a receipt each time payment is received, with prescribed particulars, and keeps the stub or copy for at least five years. (S08-01, S08-02, S15-03, V for the duty and retention; thresholds U)

## VAT return, reverse charge, imports

- **N-TXS-024** The monthly VAT return (PP 30) with payment is due by the 15th of the following month, filed per place of business unless consolidated filing is approved. (S09-01, S09-02, V)
- **N-TXS-025** An e-filing extension to the 23rd exists in RD practice (RD calendar for October 2026 shows 26 Oct because the 23rd is a holiday); the instrument currently granting it was not located. Check currency. (S09-03, S09-04, S, instrument U)
- **N-TXS-026** Corrective filing is by an additional return with any extra payment. (S09-07, V)
- **N-TXS-027** A payer remits VAT (form PP 36) when paying a non-resident operator selling temporarily without VAT registration or for services performed abroad and used in Thailand; the form is due within 7 days after month-end, and RD's calendar shows an e-filing date 15 days after month-end. Check currency. (S10-01, S10-02, V; e-filing date S)
- **N-TXS-028** Import VAT is paid to Customs with import duty; the CIF value in foreign currency is converted at the rate Customs uses for duty. (S10-04, S10-05, V)

## Foreign currency and rounding

- **N-TXS-029** Foreign-currency amounts for tax purposes are converted using either commercial-bank rates or the BOT daily reference rate, applied consistently unless the Director-General approves a change. (S12-01, V)
- **N-TXS-030** VAT tax base for foreign-currency sales: the baht actually obtained if the currency is sold in the liability month; otherwise the average commercial-bank buying rate computed by BOT for the last business day of that month. An RD English translation page appears to say "selling"; this is recorded as a conflict and the Thai text or guide wording (buying) is used. (S12-03, S12-04, V with C note)
- **N-TXS-031** Invoices for foreign-currency sales show baht values; export and international-service invoices may stay in foreign currency. The status of an older RD order on this point is unclear. (S12-02, S12-05, V; C note)
- **N-TXS-032** BOT publishes daily exchange rates (weighted-average interbank rate, average counter rates) at 18:00 Bangkok time on working days; Customs publishes its own import and export rate table. (S12-07, S10-05, V)
- **N-TXS-033** No official rounding rule for tax amounts was found in the sources read. (S12-08, U)

## Withholding tax

- **N-TXS-034** A payer of listed income must withhold tax at payment, issue a withholding certificate to the payee, and remit within 7 days after the end of the payment month; PND 3 covers individual payees and PND 53 juristic payees. (S13-01, S13-02, S13-03, S13-04, V)
- **N-TXS-035** RD's guide gives rates by income type for juristic payees: rent 5%, professional fees 3%, contract work 3%, prizes 5%, advertising 2%, other services 3%, transport 1%, non-life insurance premiums 1%, interest to companies 1%, dividends 10%, specified agricultural purchases 0.75%; payers withhold only where the payment to one payee under one contract reaches the minimum amount (RD guide says 1,000 baht; another RD page was summarised as 500 baht). The guide's edition date is not stated. Check currency. (S13-05, S13-06, S13-07, S, conflict on minimum)
- **N-TXS-036** Withholding forms are filed by the 7th (paper) or the 15th (e-filing) after the payment month per RD's calendar; employers must file employment-withholding returns electronically from 2024; a general mandate for PND 3 or 53 e-filing was not found. Check currency. (S13-08, S13-09, S, mandate U)
- **N-TXS-037** Payments to foreign companies not carrying on business in Thailand are subject to withholding on listed Thai-source income, remitted with PND 54 within 7 days after month-end; RD's English guide shows 15% for most income and 10% for dividends and profit remittance; the exact wording of the rate in the English Revenue Code page is in conflict. Check currency. (S13-10, S13-11, S, C note)
- **N-TXS-038** Contract-work payments to a foreign-law company are withheld at 3% when it has a permanent branch in Thailand and 5% when it does not. (S16-05, S)
- **N-TXS-039** A payer who fails to withhold or remit is jointly liable with the payee and owes a monthly surcharge. (S17-03, V pointer)

## Electronic tax documents (RD requirement, then ETDA technical layer)

- **N-TXS-040** RD's rules for electronic tax invoices and receipts rest on Sec. 3 sodasa of the Revenue Code, a 2022 Ministerial Regulation, and an RD announcement signed 7 Jun 2023. An electronic tax document is data signed with an electronic signature based on an electronic certificate. (S14-01, S14-02, V)
- **N-TXS-041** An issuer applies to RD to be listed as authorised; use is optional and may differ per document (paper or electronic). No mandatory-adoption date was found. (S14-03, V; mandate U)
- **N-TXS-042** Issuers' systems need access control, traceable corrections, logs and encryption controls; documents carry the essential invoice items in RD's published format. (S14-04, S14-05, V)
- **N-TXS-043** Sending the electronic document to the buyer counts as delivery; a buyer who declines receives a print-out stating it was created and sent to RD electronically. (S14-06, V)
- **N-TXS-044** Issuers (or their registered providers) send the electronic-document data to RD by the 15th of the following month in RD's standard format, signed with an unexpired certificate, by upload or host-to-host connection. Check currency. (S14-07, S14-08, V)
- **N-TXS-045** Electronic tax documents are stored in a reliable, unchanged and displayable form with origin or destination and time information. (S14-09, V)
- **N-TXS-046** ETDA is a separate technical body: it runs a certification process for e-tax service-provider systems and names a security recommendation (21-2562) and an XML data-exchange recommendation (14-2560); RD approves providers and sets the tax-law requirement. Data sent to RD is XML; documents sent to customers may be in other signed formats. (S14-10, S14-11, S)
- **N-TXS-047** An RD DG Announcement (No. 48) is cited by ETDA but its text and date were not read. (S14-12, U)

## Record keeping and accounting

- **N-TXS-048** VAT records (output or input tax reports, goods report where relevant) are updated within 3 working days of the event and kept, with tax invoices and supporting documents, at least 5 years from the filing date (shorter or longer in specified cases). (S15-01, S15-02, V)
- **N-TXS-049** Under the Accounting Act, duty-holders include Thai companies and partnerships and foreign-law juristic persons doing business in Thailand; books and supporting documents are kept at least 5 years from closing (up to 7 where prescribed). (S15-04, V)
- **N-TXS-050** Book entries are in Thai; a foreign-language entry needs Thai alongside, or account codes need a Thai code manual. No Thai-language rule for supporting documents beyond tax invoices was found in the text read. (S15-05, S15-06, V; supporting-document rule U)
- **N-TXS-051** Financial statements are due to DBD within 1 month after shareholder approval for Thai companies and within 5 months of closing for foreign-law juristic persons and some partnerships; DBD prescribes line items by entity type. (S15-08, V)

## Foreign-owned entities and branches

- **N-TXS-052** A foreign company with a branch or office in Thailand obtains a taxpayer ID within 60 days of registration or start; the 13-digit format applies (an RD English page still says 10 digits). (S16-01, S11-05, S11-06, S, C note)
- **N-TXS-053** A Thai agent bears registration and, where authorised, invoicing responsibility for a non-resident's VAT business. (S16-02, V)
- **N-TXS-054** Non-resident providers of electronic services to non-registered Thai customers register once income exceeds 1.8 million baht per year, charge VAT without issuing a tax invoice, file monthly (1st-23rd of the next month) via RD's electronic service, and cannot deduct input tax; customers who are VAT registrants use the payer-side remittance. (S16-04, V)
- **N-TXS-055** Accounting duties apply to foreign-law juristic persons and each regular place of business, which closes books with the head office. (S11-07, S16-06, V)
- **N-TXS-056** Nothing specific to representative offices or to shareholders' nationality was found in the official pages read. (S16-07, S16-08, U)

## Penalties (pointers only)

- **N-TXS-057** VAT penalty provisions are in Secs. 89 to 90 or 5, with a surcharge of 1.5% per month (0.75% with an approved extension), capped at the tax; WHT penalty pointers are Secs. 54 and 37 bis; Accounting Act penalties sit in its penalty chapter. (S17-01, S17-02, S17-03, S17-04, V pointers)

## Limits

Statements derived from pages read through a summarising fetch step carry an S read-mode in the register and need a raw second read before reliance. Items marked U or C are unresolved. Rates, deadlines and decrees change often; re-check on the day of use.

