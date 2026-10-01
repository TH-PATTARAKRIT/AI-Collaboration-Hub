# Business Rule Register

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Source/dump evidence only — not runtime proof, not statutory proof. No V-level, no Complete, no coverage percentage. Assembled mechanically from the unit files named in each row; Restricted Technical Evidence (this file) is separate from the Neutral Clean-Room Knowledge Pack.


| Unit | BR-ID | Rule (neutral) | Condition / configuration | Claim-IDs | Class |
|---|---|---|---|---|---|
| TXA1 | TXA1-BR01 | A tax has one computation type: percentage, fixed, percentage-included division, or group; no formula type in the installed set | always | VDR-TXA1-C001 VDR-TXA1-C317 | Calculation |
| TXA1 | TXA1-BR02 | A tax is selectable for sales, purchases or none; none is usable only inside a group | always | VDR-TXA1-C002 VDR-TXA1-C015 | Constraint |
| TXA1 | TXA1-BR03 | Taxes are applied in ascending sequence, ties by creation order; fixed first, then included, then excluded | always | VDR-TXA1-C004 VDR-TXA1-C033 VDR-TXA1-C020 | Calculation |
| TXA1 | TXA1-BR04 | Group members replace the group and are sorted by their own sequence at the group's position | tax group on a line | VDR-TXA1-C020 VDR-TXA1-C015 | Calculation |
| TXA1 | TXA1-BR05 | Same-type, same-inclusion, same-base-flag taxes are computed as one batch | always | VDR-TXA1-C021 | Calculation |
| TXA1 | TXA1-BR06 | A base-affecting tax adds its amount to the base of later taxes unless they opt out | include-in-base flag set | VDR-TXA1-C005 VDR-TXA1-C006 VDR-TXA1-C022 | Configuration |
| TXA1 | TXA1-BR07 | Fixed tax = quantity x amount with the sign of the unit price, not reduced by discount | fixed tax | VDR-TXA1-C023 VDR-TXA1-C084 VDR-TXA1-C248 | Calculation |
| TXA1 | TXA1-BR08 | Exclusive percentage tax = base x percent / 100 (base includes propagated extra base) | percentage tax, price-excluded | VDR-TXA1-C026 | Calculation |
| TXA1 | TXA1-BR09 | Inclusive percentage tax = base x percent / (100 + batch percent total); base = price minus batch tax | percentage tax, price-included | VDR-TXA1-C024 VDR-TXA1-C034 | Calculation |
| TXA1 | TXA1-BR10 | Division tax uses the divided base; inclusive division tax = base x percent / 100 | division tax | VDR-TXA1-C027 VDR-TXA1-C025 | Calculation |
| TXA1 | TXA1-BR11 | Line discount reduces the unit price before taxes | discount on line | VDR-TXA1-C047 | Calculation |
| TXA1 | TXA1-BR12 | Negative-factor taxes create a mirrored reverse-charge entry and are never price-included | distribution with negative factor | VDR-TXA1-C030 VDR-TXA1-C031 VDR-TXA1-C067 | Calculation |
| TXA1 | TXA1-BR13 | A line may force total-included or total-excluded reading of every tax | special mode set | VDR-TXA1-C041 VDR-TXA1-C086 VDR-TXA1-C087 | Configuration |
| TXA1 | TXA1-BR14 | Whether a price includes tax: tax override, else company default (tax excluded) | always | VDR-TXA1-C007 VDR-TXA1-C008 VDR-TXA1-C170 | Default |
| TXA1 | TXA1-BR15 | The company price-inclusion default cannot change after invoicing started | company has accounting | VDR-TXA1-C171 | Constraint |
| TXA1 | TXA1-BR16 | Expense claims are read as tax-included whatever the company default | hr_expense installed | VDR-TXA1-C244 VDR-TXA1-C246 | Calculation |
| TXA1 | TXA1-BR17 | Rounding method follows the company setting (default global); each step rounds in the precision of its currency | always | VDR-TXA1-C048 VDR-TXA1-C169 VDR-TXA1-C208 | Default |
| TXA1 | TXA1-BR18 | Global rounding rounds each tax total once and spreads the delta; included taxes round base plus tax and derive the base | round globally | VDR-TXA1-C053 VDR-TXA1-C054 VDR-TXA1-C055 VDR-TXA1-C052 | Calculation |
| TXA1 | TXA1-BR19 | Per-line rounding rounds tax amounts and raw base at calculation | round per line | VDR-TXA1-C029 VDR-TXA1-C051 | Calculation |
| TXA1 | TXA1-BR20 | Manual tax amounts are kept unless currency or document type changes or taxes-affecting lines change | draft document edited | VDR-TXA1-C114 VDR-TXA1-C116 VDR-TXA1-C044 VDR-TXA1-C127 | Calculation |
| TXA1 | TXA1-BR21 | Totals are grouped by tax group in group order with optional subtotal labels | always | VDR-TXA1-C072 VDR-TXA1-C071 VDR-TXA1-C073 | Calculation |
| TXA1 | TXA1-BR22 | Cash rounding adds a line or changes the largest tax; nothing happens for biggest-tax strategy without a tax | cash rounding set | VDR-TXA1-C075 VDR-TXA1-C211 VDR-TXA1-C212 | Calculation |
| TXA1 | TXA1-BR23 | Global discounts and down payments are split across taxes; fixed taxes are not discounted | discount or advance applied | VDR-TXA1-C099 VDR-TXA1-C100 VDR-TXA1-C226 VDR-TXA1-C227 VDR-TXA1-C084 | Calculation |
| TXA1 | TXA1-BR24 | Early-payment discount tax treatment follows the payment term mode | payment term with early discount | VDR-TXA1-C144 VDR-TXA1-C107 VDR-TXA1-C217 | Configuration |
| TXA1 | TXA1-BR25 | Each tax has mirrored invoice and credit-note distribution lines with one base line and totals of 100 percent | always | VDR-TXA1-C014 VDR-TXA1-C094 VDR-TXA1-C064 | Constraint |
| TXA1 | TXA1-BR26 | A distribution-line account cannot be receivable, payable or off-balance; missing account falls back to the base account | always | VDR-TXA1-C098 VDR-TXA1-C062 | Constraint |
| TXA1 | TXA1-BR27 | Tax tags attach from distribution lines, product tags and preceding base-affecting taxes; cash-basis tags attach at payment | always | VDR-TXA1-C063 VDR-TXA1-C065 VDR-TXA1-C066 VDR-TXA1-C069 VDR-TXA1-C070 | Calculation |
| TXA1 | TXA1-BR28 | Selectable tags are limited to no-country, fiscal-country and foreign-VAT-country tags | tax maintenance | VDR-TXA1-C097 | Constraint |
| TXA1 | TXA1-BR29 | Zero-amount tax items are not created; zero-rated and exempt sales keep only base items with tags | zero-amount tax | VDR-TXA1-C079 | Calculation |
| TXA1 | TXA1-BR30 | Tax items are merged by partner, currency, analytic, account, taxes, distribution line and group | always | VDR-TXA1-C060 VDR-TXA1-C081 | Calculation |
| TXA1 | TXA1-BR31 | Tax items inherit analytic split only for analytic-cost taxes or non-closing lines | analytic distribution present | VDR-TXA1-C061 | Calculation |
| TXA1 | TXA1-BR32 | Draft documents re-synchronise tax items; posted documents do not | draft document | VDR-TXA1-C114 VDR-TXA1-C082 | Calculation |
| TXA1 | TXA1-BR33 | A tax belongs to one tax group; default group is first of its country, else without country | tax created without group | VDR-TXA1-C013 VDR-TXA1-C200 | Default |
| TXA1 | TXA1-BR34 | Tax names are unique per usage, scope and country across the company tree | tax create or rename | VDR-TXA1-C010 | Constraint |
| TXA1 | TXA1-BR35 | A cash-basis tax needs a reconcilable transition account; the company switch cannot be disabled while one exists | on_payment tax | VDR-TXA1-C012 VDR-TXA1-C182 VDR-TXA1-C175 | Constraint |
| TXA1 | TXA1-BR36 | Customer lines default to product sales taxes else account sale taxes; vendor lines symmetric; then company filter and fiscal position mapping | line tax recompute | VDR-TXA1-C135 VDR-TXA1-C136 VDR-TXA1-C138 VDR-TXA1-C134 | Default |
| TXA1 | TXA1-BR37 | Order lines take product taxes only (no account taxes), mapped by the order's fiscal position | sale or purchase order line | VDR-TXA1-C218 VDR-TXA1-C220 VDR-TXA1-C230 | Default |
| TXA1 | TXA1-BR38 | The company default sale and purchase taxes seed new products; line-level defaults do not read them | product creation | VDR-TXA1-C172 VDR-TXA1-C145 VDR-TXA1-C146 VDR-TXA1-C139 | Default |
| TXA1 | TXA1-BR39 | Quick encoding falls back to journal-account taxes, then company default tax | quick encoding mode | VDR-TXA1-C291 VDR-TXA1-C130 | Default |
| TXA1 | TXA1-BR40 | Combo products carry no taxes | product type combo | VDR-TXA1-C149 VDR-TXA1-C218 | Default |
| TXA1 | TXA1-BR41 | Order taxes travel unchanged to invoice lines with engine data | invoice from order | VDR-TXA1-C225 VDR-TXA1-C224 | Calculation |
| TXA1 | TXA1-BR42 | Order-line taxes are limited to sale-type taxes of the order's tax country | sale order line | VDR-TXA1-C219 VDR-TXA1-C214 | Constraint |
| TXA1 | TXA1-BR43 | A document may not keep taxes of another country than its tax country | post or edit document | VDR-TXA1-C126 VDR-TXA1-C113 | Constraint |
| TXA1 | TXA1-BR44 | Fiscal position resolution order: partner, delivery address, manual position, country, automatic candidates with tests | document partner or address change | VDR-TXA1-C161 VDR-TXA1-C159 VDR-TXA1-C160 | Calculation |
| TXA1 | TXA1-BR45 | A fiscal position replaces taxes by listed replacements and swaps accounts by mapping; no position leaves taxes unchanged | position present | VDR-TXA1-C157 VDR-TXA1-C158 VDR-TXA1-C156 | Calculation |
| TXA1 | TXA1-BR46 | When mapped taxes are price-included the unit price is adapted symmetrically | fiscal position maps included taxes | VDR-TXA1-C037 VDR-TXA1-C154 VDR-TXA1-C092 | Calculation |
| TXA1 | TXA1-BR47 | Foreign tax IDs on positions need country, state within fiscal country, and are unique per country | foreign VAT position | VDR-TXA1-C164 VDR-TXA1-C166 | Constraint |
| TXA1 | TXA1-BR48 | Partner VAT check in the installed set is a stub; VAT presence means set and not a slash | always | VDR-TXA1-C167 VDR-TXA1-C168 | Risk |
| TXA1 | TXA1-BR49 | Vendor-bill lines may be partly deductible (0 to 100); the private share and its taxes go to the journal's private-share account | vendor bill line deductibility below 100 | VDR-TXA1-C123 VDR-TXA1-C124 VDR-TXA1-C119 VDR-TXA1-C118 VDR-TXA1-C125 | Configuration |
| TXA1 | TXA1-BR50 | Totals show non-deductible tax separately | private-share lines present | VDR-TXA1-C076 | Calculation |
| TXA1 | TXA1-BR51 | Receipt cost excludes taxes whose distribution lines have an account and includes taxes without account | purchase receipt valuation | VDR-TXA1-C237 VDR-TXA1-C236 VDR-TXA1-C088 | Calculation |
| TXA1 | TXA1-BR52 | Cost-of-goods entries are untaxed and exist only for real-time valuation products | customer invoice posting, real-time valuation | VDR-TXA1-C322 VDR-TXA1-C240 VDR-TXA1-C242 | Calculation |
| TXA1 | TXA1-BR53 | Foreign-amount base and tax are divided by the line rate to get company amounts; each currency is rounded separately | foreign-currency line | VDR-TXA1-C050 VDR-TXA1-C059 VDR-TXA1-C046 | Calculation |
| TXA1 | TXA1-BR54 | Invoice rate = rate at invoice date (today if empty), refreshable, positive, manual edits protected | invoice or receipt | VDR-TXA1-C201 VDR-TXA1-C202 VDR-TXA1-C203 VDR-TXA1-C204 VDR-TXA1-C128 | Calculation |
| TXA1 | TXA1-BR55 | Orders use their own order-date rate; the invoice created from an order recomputes its rate at invoice date | order to invoice | VDR-TXA1-C215 VDR-TXA1-C234 VDR-TXA1-C224 | Calculation |
| TXA1 | TXA1-BR56 | Rate lookup falls back to earliest rate then 1.0; no installed feed; no rate rows in this database | any conversion | VDR-TXA1-C205 VDR-TXA1-C278 VDR-TXA1-C209 | Risk |
| TXA1 | TXA1-BR57 | Rates and cash-basis switch live on the root company; branches share them | company tree | VDR-TXA1-C206 VDR-TXA1-C176 | Constraint |
| TXA1 | TXA1-BR58 | Foreign sale documents may show tax in company currency (company flag on by default) | foreign-currency sale document | VDR-TXA1-C112 VDR-TXA1-C173 | Configuration |
| TXA1 | TXA1-BR59 | A currency precision cannot be reduced once used in entries | currency maintenance | VDR-TXA1-C210 | Constraint |
| TXA1 | TXA1-BR60 | Taxable supply date has no logic; rate date is the invoice date | always | VDR-TXA1-C267 VDR-TXA1-C122 VDR-TXA1-C201 | Risk |
| TXA1 | TXA1-BR61 | A used tax cannot be deleted and its company cannot change; archiving is not guarded; sales-order-only use does not count | tax maintenance | VDR-TXA1-C093 VDR-TXA1-C016 VDR-TXA1-C326 VDR-TXA1-C302 VDR-TXA1-C300 VDR-TXA1-C301 | Constraint |
| TXA1 | TXA1-BR62 | Chart reload skips changed taxes unless forced; forced reload renames the old tax and creates a new one | chart template reload | VDR-TXA1-C256 VDR-TXA1-C257 | Calculation |
| TXA1 | TXA1-BR63 | Only the accounting administrator role creates, edits or deletes taxes, groups, distribution lines and fiscal positions | always | VDR-TXA1-C271 | Constraint |
| TXA1 | TXA1-BR64 | Tax visibility is limited to the user's allowed companies and their parents | always | VDR-TXA1-C272 VDR-TXA1-C091 | Constraint |
| TXA1 | TXA1-BR65 | Non-sale taxed documents are moved to the first open day under a tax lock; posted taxed lines are protected | tax lock date set | VDR-TXA1-C293 VDR-TXA1-C294 VDR-TXA1-C266 VDR-TXA1-C129 | Constraint |
| TXA1 | TXA1-BR66 | The Thai template recognises all 18 taxes at invoicing, uses only generic engine features and ships no fiscal position | Thai chart loaded | VDR-TXA1-C189 VDR-TXA1-C187 VDR-TXA1-C275 VDR-TXA1-C186 | Configuration |
| TXA1 | TXA1-BR67 | Zero and exempt Thai taxes have no template group and fall to the first withholding group | Thai chart loaded | VDR-TXA1-C200 VDR-TXA1-C192 VDR-TXA1-C195 | Risk |
| TXA1 | TXA1-BR68 | Sale withholding taxes are forced price-excluded; purchase withholding follows the company default | Thai chart loaded | VDR-TXA1-C198 VDR-TXA1-C324 | Risk |
| TXA1 | TXA1-BR69 | Withholding tax is selected manually per line; no payee-driven selection exists | Thai chart loaded | VDR-TXA1-C196 VDR-TXA1-C197 VDR-TXA1-C187 | Risk |
| TXA1 | TXA1-BR70 | Without a category code the e-invoice exporter infers exempt for a domestic zero-amount tax | e-invoice export | VDR-TXA1-C297 VDR-TXA1-C299 | Risk |
| TXA1 | TXA1-BR71 | Legal notes of taxes and fiscal positions print on invoices; Thai taxes have none | invoice print | VDR-TXA1-C284 VDR-TXA1-C285 VDR-TXA1-C290 | Configuration |
| TXA2 | TXA2-BR-01 | A document is always created in draft and becomes posted only through the posting action by a user with the invoicing role. | always | VDR-TXA2-C008, VDR-TXA2-C009, VDR-TXA2-C010 | FACT |
| TXA2 | TXA2-BR-02 | Posting refuses a negative total, a missing customer on invoices, a missing bill date on vendor documents, documents without lines, archived journals or accounts and accounts of another company tree. | always (receipts are not asked for a customer, inferred) | VDR-TXA2-C027, VDR-TXA2-C028, VDR-TXA2-C029, VDR-TXA2-C055, VDR-TXA2-C241 | FACT |
| TXA2 | TXA2-BR-03 | A credit note is a reversal of a posted invoice or bill, linked to the original, of the matching type; receipts reverse to credit notes of their side. | always | VDR-TXA2-C011, VDR-TXA2-C012, VDR-TXA2-C013 | FACT |
| TXA2 | TXA2-BR-04 | The reversal can be taken as a draft credit note to edit and post, or as an immediately posted and reconciled credit note with a new draft copy of the original. | reversal date not in the future for the immediate option | VDR-TXA2-C127, VDR-TXA2-C128, VDR-TXA2-C130, VDR-TXA2-C134 | FACT |
| TXA2 | TXA2-BR-05 | A reversal of a posted invoice sets the credit note date and invoice date to the date chosen in the wizard. | always | VDR-TXA2-C129 | FACT |
| TXA2 | TXA2-BR-06 | No document or field links a re-issued tax document to the document it replaces. | always (negative search) | VDR-TXA2-C119, VDR-TXA2-C131 | INFERENCE |
| TXA2 | TXA2-BR-07 | A debit note exists only in an optional module that is not installed; when installed it copies a posted document into a linked draft with its own numbering prefix. | optional module installed | VDR-TXA2-C002, VDR-TXA2-C143, VDR-TXA2-C144, VDR-TXA2-C146, VDR-TXA2-C147 | FACT |
| TXA2 | TXA2-BR-08 | Sales receipts need a setting (on in the studied database); purchase receipts are always available; receipts share the number series of invoices and use the same taxes and posting flow. | setting for sales receipts | VDR-TXA2-C017, VDR-TXA2-C018, VDR-TXA2-C019, VDR-TXA2-C023, VDR-TXA2-C024, VDR-TXA2-C022 | FACT |
| TXA2 | TXA2-BR-09 | Receipts print without a document title in the core layout. | core invoice layout | VDR-TXA2-C040, VDR-TXA2-C041 | INFERENCE |
| TXA2 | TXA2-BR-10 | Resetting a posted document to draft keeps its number and is refused for hashed documents, cash-basis and exchange entries, localizations demanding a cancellation request, and locked periods. | always | VDR-TXA2-C030, VDR-TXA2-C031, VDR-TXA2-C033, VDR-TXA2-C094, VDR-TXA2-C121 | FACT |
| TXA2 | TXA2-BR-11 | Cancelling a document keeps its number and removes its reconciliations but leaves the settling payments posted and unreconciled. | always | VDR-TXA2-C032, VDR-TXA2-C125, VDR-TXA2-C036, VDR-TXA2-C037 | FACT |
| TXA2 | TXA2-BR-12 | Reset to draft and cancel carry no role check in code; only the view limits the buttons to the invoicing role. | always | VDR-TXA2-C256, VDR-TXA2-C034, VDR-TXA2-C122 | FACT |
| TXA2 | TXA2-BR-13 | The accounting date of a customer document equals its invoice date until posting; for vendor documents it is derived from the bill date to keep the number series increasing. | always | VDR-TXA2-C050, VDR-TXA2-C051, VDR-TXA2-C052, VDR-TXA2-C053 | FACT |
| TXA2 | TXA2-BR-14 | An empty invoice date on a customer document becomes today at posting; a vendor document needs a bill date. | always | VDR-TXA2-C055, VDR-TXA2-C056 | FACT |
| TXA2 | TXA2-BR-15 | Invoice date, accounting date, partner, lines, payment terms, currency and fiscal position cannot be edited after posting. | always | VDR-TXA2-C057, VDR-TXA2-C058 | FACT |
| TXA2 | TXA2-BR-16 | Delivery date is copied from the first completed customer delivery of the order onto customer invoices when the delivery module is installed and is informational only. | delivery module installed | VDR-TXA2-C061, VDR-TXA2-C062, VDR-TXA2-C063, VDR-TXA2-C064, VDR-TXA2-C066 | FACT |
| TXA2 | TXA2-BR-17 | The supply (tax-point) date field exists but is empty and hidden in the base and in the Thai localization. | always | VDR-TXA2-C047, VDR-TXA2-C060, VDR-TXA2-C067 | FACT |
| TXA2 | TXA2-BR-18 | Posting inside a locked period moves the date to the first date not blocked by the applicable locks instead of refusing. | always | VDR-TXA2-C082, VDR-TXA2-C083, VDR-TXA2-C086, VDR-TXA2-C085 | FACT |
| TXA2 | TXA2-BR-19 | Which locks apply depends on journal type and tax impact: global and hard always, sales on customer journals, purchase on vendor journals, tax only for tax-affecting documents. | always | VDR-TXA2-C087, VDR-TXA2-C088, VDR-TXA2-C090 | FACT |
| TXA2 | TXA2-BR-20 | Editing, resetting, cancelling or deleting a posted document inside a locked period is refused; the tax lock protects tax-affecting items even when the global lock is open. | always | VDR-TXA2-C091, VDR-TXA2-C092, VDR-TXA2-C093, VDR-TXA2-C094, VDR-TXA2-C096, VDR-TXA2-C099 | FACT |
| TXA2 | TXA2-BR-21 | Soft locks can be relaxed per user or for all by time-boxed exceptions created by accounting administrators; the hard lock cannot be relaxed, lowered or removed. | always | VDR-TXA2-C101, VDR-TXA2-C102, VDR-TXA2-C103, VDR-TXA2-C109, VDR-TXA2-C110 | FACT |
| TXA2 | TXA2-BR-22 | The tax lock date is not maintained automatically: no tax closing entry exists to set it. | always | VDR-TXA2-C115, VDR-TXA2-C116 | INFERENCE |
| TXA2 | TXA2-BR-23 | There is no tax period or tax return object; a period is a date range chosen when a report is run. | always | VDR-TXA2-C078, VDR-TXA2-C079 | INFERENCE |
| TXA2 | TXA2-BR-24 | Lock dates and exceptions are not maintained through any menu or setting in the base application. | always (negative search) | VDR-TXA2-C107 | INFERENCE |
| TXA2 | TXA2-BR-25 | Transfers are checked only against the fiscal-year and hard locks. | stock valuation module installed | VDR-TXA2-C114 | FACT |
| TXA2 | TXA2-BR-26 | Numbers are assigned at posting from the previous number of the same journal and series; customer invoices default to a yearly pattern, vendor bills to a monthly pattern. | always | VDR-TXA2-C167, VDR-TXA2-C169, VDR-TXA2-C173 | FACT |
| TXA2 | TXA2-BR-27 | Credit notes and payments get separate series by journal flag, with a distinguishing prefix, defaulting on for customer and vendor journals and bank journals. | journal flags | VDR-TXA2-C172, VDR-TXA2-C170, VDR-TXA2-C174 | FACT |
| TXA2 | TXA2-BR-28 | The Thai localization adds no numbering rule, sequence, journal option or date rule. | always | VDR-TXA2-C175, VDR-TXA2-C067, VDR-TXA2-C038 | FACT |
| TXA2 | TXA2-BR-29 | A posted number must agree with the date period of its pattern; moving a document across periods needs the number cleared. | always | VDR-TXA2-C177, VDR-TXA2-C123, VDR-TXA2-C184 | FACT |
| TXA2 | TXA2-BR-30 | Gaps and irregularities caused by draft, cancelled or deleted numbered documents are flagged on the journal dashboard; deletion of numbered documents that are not last in their series is restricted. | always | VDR-TXA2-C180, VDR-TXA2-C181, VDR-TXA2-C182, VDR-TXA2-C183, VDR-TXA2-C179 | FACT |
| TXA2 | TXA2-BR-31 | An optional per-journal hash chain makes posted documents unalterable in number, date, journal, company and line label, amounts, account and partner; taxes, tags and invoice date are not covered. | journal option on | VDR-TXA2-C186, VDR-TXA2-C187, VDR-TXA2-C188, VDR-TXA2-C189, VDR-TXA2-C191, VDR-TXA2-C192, VDR-TXA2-C193 | FACT |
| TXA2 | TXA2-BR-32 | Tax lines and tags are computed in draft and frozen at posting; taxes of posted items cannot change and tax lines cannot be deleted by hand. | always | VDR-TXA2-C198, VDR-TXA2-C200, VDR-TXA2-C202, VDR-TXA2-C097, VDR-TXA2-C212 | FACT |
| TXA2 | TXA2-BR-33 | Tags follow the tax distribution for invoice or credit note when the tax is due on invoice or cash-basis tags are requested. | always | VDR-TXA2-C204, VDR-TXA2-C205 | FACT |
| TXA2 | TXA2-BR-34 | Withholding in the Thai tax set is an ordinary negative tax booked at posting, not at payment. | Thai chart loaded | VDR-TXA2-C208, VDR-TXA2-C209, VDR-TXA2-C211 | FACT |
| TXA2 | TXA2-BR-35 | Cash-basis taxes sit on a transition account until reconciliation and are then moved by a cash-basis entry; no Thai tax uses this. | tax set to payment basis | VDR-TXA2-C213, VDR-TXA2-C216, VDR-TXA2-C218, VDR-TXA2-C219, VDR-TXA2-C215 | FACT |
| TXA2 | TXA2-BR-36 | Payment-time withholding exists only in an optional module that is not installed; it requires a withholding number and ignores the tax in document computation. | optional module installed | VDR-TXA2-C221, VDR-TXA2-C223, VDR-TXA2-C226, VDR-TXA2-C227 | FACT |
| TXA2 | TXA2-BR-37 | An optional tool rewrites tax tags on existing items from a date, irreversibly, without lock checks or log. | optional module installed | VDR-TXA2-C231, VDR-TXA2-C232, VDR-TXA2-C234, VDR-TXA2-C235, VDR-TXA2-C236 | FACT |
| TXA2 | TXA2-BR-38 | Documents are isolated by company; tax and fiscal configuration is shared up the company tree. | always | VDR-TXA2-C238, VDR-TXA2-C239, VDR-TXA2-C240 | FACT |
| TXA2 | TXA2-BR-39 | Only invoicing and administrator roles are intended with the accounting application alone; operational roles are narrowed by record rules. | always | VDR-TXA2-C244, VDR-TXA2-C245, VDR-TXA2-C250, VDR-TXA2-C252, VDR-TXA2-C253, VDR-TXA2-C251 | FACT |
| TXA2 | TXA2-BR-40 | Documents created from sales orders are created with elevated rights; vendor bills from purchase orders with the user's own rights. | sales or purchasing installed | VDR-TXA2-C255, VDR-TXA2-C295 | FACT |
| TXA2 | TXA2-BR-41 | Field tracking and chatter record document and tax changes; line changes are logged only after the document was posted once. | always | VDR-TXA2-C260, VDR-TXA2-C264, VDR-TXA2-C261 | FACT |
| TXA2 | TXA2-BR-42 | With the restrictive audit trail option, posted-once entries are cancelled rather than deleted and audit messages and attachments are protected; the option is off in the studied database. | option on | VDR-TXA2-C269, VDR-TXA2-C271, VDR-TXA2-C272, VDR-TXA2-C268 | FACT |
| TXA2 | TXA2-BR-43 | Sales and purchase hand-offs copy taxes, fiscal position, currency and analytic distribution from the order but pass no invoice date. | always | VDR-TXA2-C279, VDR-TXA2-C280, VDR-TXA2-C292, VDR-TXA2-C282, VDR-TXA2-C294, VDR-TXA2-C284, VDR-TXA2-C296 | FACT |
| TXA2 | TXA2-BR-44 | Invoices from sales are merged only for the same company, partner, shipping partner, currency and fiscal position; bills from purchases by company, partner and currency. | always | VDR-TXA2-C281, VDR-TXA2-C293 | FACT |
| TXA2 | TXA2-BR-45 | Draft and posted invoices count as invoiced quantity on the order; cancelled ones do not; returns create no credit note. | sales installed | VDR-TXA2-C286, VDR-TXA2-C291 | FACT |
| TXA2 | TXA2-BR-46 | Cost lines and closing entries created from inventory carry no document taxes; with periodic valuation no cost lines are created at invoicing. | stock valuation installed | VDR-TXA2-C298, VDR-TXA2-C299, VDR-TXA2-C302, VDR-TXA2-C301 | FACT |
| TXA2 | TXA2-BR-47 | Online payment confirmation posts the linked draft invoices automatically and reconciles payments; automatic invoicing after payment is off unless a parameter is set. | payment modules installed | VDR-TXA2-C290, VDR-TXA2-C288, VDR-TXA2-C289, VDR-TXA2-C287 | FACT |
| TXA2 | TXA2-BR-48 | Employee-paid expenses are posted as purchase receipts partnered with the employee and dated today. | expense module installed | VDR-TXA2-C305, VDR-TXA2-C306, VDR-TXA2-C307 | FACT |
| TXA2 | TXA2-BR-49 | The Thai print layout is selected by company fiscal country; the title of a posted customer invoice is a fixed text; credit notes and drafts keep core titles; a Commercial Invoice print exists. | company fiscal country is Thailand | VDR-TXA2-C310, VDR-TXA2-C316, VDR-TXA2-C317, VDR-TXA2-C320, VDR-TXA2-C321 | FACT |
| TXA2 | TXA2-BR-50 | The in-payment status is not reachable in the base application. | always | VDR-TXA2-C005, VDR-TXA2-C006 | INFERENCE |

**Rows:** 121 · **Units without this register:** none · generated 2026-10-02
