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

