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

