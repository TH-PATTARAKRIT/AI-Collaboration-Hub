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
