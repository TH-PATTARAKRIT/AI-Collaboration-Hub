# U28 Thai entity structures — Neutral Knowledge

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Clean-room layer. Source studied: Odoo 19 Community only.
> Scope: how the accounting core and the Thai localization serve foreign-owned Thai companies, Thai subsidiaries of foreign groups, and branches, representative offices and regional offices of foreign companies operating in Thailand.
> Thai legal facts are never asserted; they are marked UNKNOWN — STATUTORY SOURCE REQUIRED. Missing concepts are stated as NOT PRESENT IN COMMUNITY SOURCE.

## CAP-U28-01 Company and legal-entity model (hierarchy, branch semantics, entity-type mapping)

### WHAT
- [N-U28-001] The system organises the business as companies. A company may have one parent; a company that has a parent is called a branch, and a top-level company together with its descendants forms one company tree. No other relationship between companies exists.
- [N-U28-002] Every company is backed by exactly one contact record that holds its name, tax identifier, company registry number, address and country; the company screen only displays these values. A contact can also tell which companies refer to it.
- [N-U28-003] Each company has exactly one functional currency, which is mandatory when the company is created.
- [N-U28-004] The system holds no information about who owns a company: there is no shareholder, ownership share, foreign-ownership indicator, ultimate parent or group code on a company or on a contact.
- [N-U28-005] Mapping of business entity types to what the system can express: a legally separate subsidiary of a foreign group is a separate top-level company with its own contact, currency, books and numbering; a branch of a foreign company operating locally is either a separate top-level company or a child company that shares the top-level company's currency, fiscal-year end, tax-on-payment switch and reversal-style switch; a representative office and a regional office have no dedicated type, field or label and can only be set up as one of those two; ownership and group membership are not recorded.

### WHY
- [N-U28-006] The top-level company is treated as the unit of one set of books: currency, exchange rates, the lock on currency change and the limit on reconciliation are all decided at that level.

### BUSINESS RULE
- [N-U28-007] Company names must be unique.
- [N-U28-008] A branch must carry the same currency, fiscal-year end, tax-on-payment switch and reversal-style switch as its top-level company. The values are copied when the branch is created and pushed down whenever the top-level company changes them; the branch screen shows them read-only.
- [N-U28-009] A company cannot be moved to a different parent after it has been created, and a company cannot be duplicated.
- [N-U28-010] A company cannot be archived while it is the default company of an active user.
- [N-U28-011] Creating a company links it to the creating user and to the system administrator account, activates its currency, and gives it its own numbering series for grouped payments.
- [N-U28-012] A new branch under a top-level company that already has a chart of accounts automatically receives that chart configuration at the end of its creation.
- [N-U28-013] Each user has a set of allowed companies and one default company, and the default must belong to the allowed set. A user with more than one allowed company automatically receives the multi-company display permission; it is removed again when only one remains.
- [N-U28-014] The bank account printed on a customer invoice must belong to the issuing company or to one of its parent companies, so a branch can use its parent's bank accounts.

### STATE
- [N-U28-015] A company is either active or archived. Archiving a company also archives its branches. A branch keeps its parent for its whole life.

### OPTIONALITY
- [N-U28-016] The parent link is visible only in technical mode, the default company list shows top-level companies only, and branches are managed from a page on the parent company. Companies carry an order number that sorts the company switcher.
- [N-U28-017] Users activate companies in a switcher, either by toggling several companies on and off or by logging into a single company. The switcher also shows ancestors the user is not allowed into but only lets the user select permitted companies. The behaviour in a browser has not been executed.
- [N-U28-018] In the reference configuration there is a single company without branches and four users, each allowed into that one company, so multi-company behaviour cannot be observed there.

### DEPENDENCY
- [N-U28-019] Giving a company a country can trigger automatic installation of that country's accounting localization package. For Thailand this installs the Thai package; for any other country it would install a foreign package, which is outside the programme scope and must never be studied.
- [N-U28-020] Accounting, stock, manufacturing, point of sale and expense features recognise the branch hierarchy. Sales and purchase documents have no branch logic of their own and depend only on generic company scoping.

### CONSTRAINT
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### RISK
- [N-U28-021] The product uses the words branch and subsidiary for the same parent-child link, which can mislead anyone who reads subsidiary as a separate legal entity.
- [N-U28-022] A helper that lists all company contacts exists but no standard module uses it, so recognising a business partner as a sister company is not automated.

### UNKNOWN
- [N-U28-023] UNKNOWN — STATUTORY SOURCE REQUIRED: whether a representative office, regional office or branch is legally a separate taxpayer or part of one legal entity, and therefore which company structure suits each.

## CAP-U28-02 Tax identity and branch identification (company and partner)

### WHAT
- [N-U28-024] Every contact, and therefore every company, carries a free-text tax identifier; a single slash means the party has none.
- [N-U28-025] Every contact also carries a company registry number, to be used when it differs from the tax identifier. It is searchable together with the tax identifier. Placeholders for this number exist for only three countries and none for Thailand.
- [N-U28-026] Documents print the company's tax identifier under a label taken from the company's country, or the plain label Tax ID when the country defines none; the Thai country defines none, and the invoice prints the customer's identifier the same way.
- [N-U28-027] The Thai branch concept is not stored anywhere. A computed label marks a Thai company contact as Headquarter when its company registry number is empty and as Branch followed by that number when it is filled; the label is empty for non-companies and for other countries, and it is printed after the customer's tax identifier on the Thai invoice.
- [N-U28-028] Contact address types are contact, invoice, delivery and other; there is no head-office or branch type.
- [N-U28-029] A company can hold several tax registrations in other countries by creating one mapping rule per country with its own foreign tax identifier; when a document uses such a rule the foreign identifier is printed instead of the company's own. A rule can be restricted to parties that have a tax identifier.

### WHY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### BUSINESS RULE
- [N-U28-030] A duplicate tax identifier or duplicate registry number is only signalled, never refused: the signal ignores contacts that have a parent, ignores one-character identifiers and is limited to contacts that are shared or belong to the same company.
- [N-U28-031] The tax identifier and registry number are meant to be managed by the commercial parent contact; a branch entered as a child address contact is therefore not expected to hold its own registry number (inference, not executed).
- [N-U28-032] A contact that already has accounting entries cannot be attached under another contact whose tax identifier differs.
- [N-U28-033] Once non-draft invoices exist for a commercial contact, its tax identifier and country can no longer be edited.
- [N-U28-034] When the optional validation package is installed, a tax identifier is checked and formatted by country on every save of the identifier or the country; imports can bypass the check by a context switch.
- [N-U28-035] The only 13-digit identifier check in the Thai package applies to the merchant tax identifier used for bank QR payment, not to company or partner identifiers.

### STATE
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### OPTIONALITY
- [N-U28-036] Tax identifier validation is optional and is not active in the reference configuration. When active, Thailand is validated by an external library and only a 13-digit example is provided; without it any text is accepted.
- [N-U28-037] Online verification of European identifiers is a per-company switch of the optional validation package; it uses an external verification service and is irrelevant when the identifier prefix equals the company's fiscal country.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### CONSTRAINT
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### RISK
- [N-U28-038] The help text promises that the registry number is unique across partners of a country, but no constraint enforces it and the duplicate signal is not stored.
- [N-U28-039] Countries without a check function are accepted as valid, and an accounting module imports a symbol from the optional validation package although it does not declare it as a dependency; the effect of that import when the package is not installed is unknown.
- [N-U28-040] The Thai branch label cannot be searched, grouped or stored because it is only computed at print time.
- [N-U28-041] The Thai invoice prints a branch label only for the customer; the issuing company's own header uses free-form company details and prints no registry number or branch value.

### UNKNOWN
- [N-U28-042] UNKNOWN — STATUTORY SOURCE REQUIRED: the legal format, check rules, uniqueness and carrier of Thai taxpayer and branch identifiers, and whether using the company registry number as the branch number is appropriate.
- [N-U28-043] UNKNOWN — EVIDENCE INSUFFICIENT: the exact acceptance rules of the external Thai identifier check in the deployed library version; resolved only by executing it.

## CAP-U28-03 Foreign ownership and group relationships

### WHAT
- [N-U28-044] The relationship between contacts is a contact and address hierarchy used to inherit commercial data; it is not an ownership relationship and carries no percentage, role or date.
- [N-U28-045] A contact may be shared by all companies or owned by one company; a sister company's own contact is an ordinary contact in every other company.
- [N-U28-046] NOT PRESENT IN COMMUNITY SOURCE: shareholder, ownership percentage, foreign-ownership flag, ultimate parent or group code. A search of the base, accounting, Thai, sales, purchase, stock and supporting modules found nothing beyond unrelated ownership notions for attachments and stock.
- [N-U28-047] A company has a single currency; there is no group, presentation or parent-group currency. The only translation notion is a report-definition option choosing the most recent rate or translation adjustments.
- [N-U28-048] Three company-level settings exist for group dealings: a clearing journal, a clearing payable account and a clearing receivable account.
- [N-U28-049] When a company is created by a user in multi-company mode, the contacts of all other companies are pointed at a shared inter-company transit location as customer and supplier location, so a delivery to a sister company's contact goes to that transit location instead of to Customers. The only code that recognises a transfer partner as a group company looks for a company whose contact is an ancestor of the partner.
- [N-U28-050] A setting called Manage Inter Company promises automatic creation of matching orders and bills between group companies, but in the Community edition ticking it only opens an upgrade dialog and resets the value.
- [N-U28-051] NOT PRESENT IN COMMUNITY SOURCE: any module that mirrors a sales order into a purchase order or an invoice into a bill between group companies. A search of all 693 module directories and of the installed module list found only the payment clearing module and an unrelated family that handles service procurement.

### WHY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### BUSINESS RULE
- [N-U28-052] The clearing journal must be a general journal of the company; the clearing payable account must be a reconcilable payable account; the clearing receivable account must be a reconcilable receivable account; in the settings form both accounts become mandatory once a journal is chosen.

### STATE
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### OPTIONALITY
- [N-U28-053] The three values are edited per company in accounting settings and are visible only to users in the multi-company group.
- [N-U28-054] In the reference configuration the inter-company payment module is installed but its three settings are empty, it owns no permissions, rules, groups, scheduled jobs or automations, and no inter-company rules module exists.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### CONSTRAINT
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### RISK
- [N-U28-055] The help texts say the payable account is for invoice payments and the receivable account for credit-note payments, but the posting logic uses both accounts for each document direction, so the help is not a faithful description.
- [N-U28-056] The two clearing account settings are not checked against the company at model level; consistency is enforced only through the settings form.

### UNKNOWN
- [N-U28-057] UNKNOWN — EVIDENCE INSUFFICIENT: how a foreign parent group, ownership chain or group reporting currency must be recorded for a Thai subsidiary; the product offers no field, so it would need a custom attribute or an external record.
- [N-U28-058] UNKNOWN — STATUTORY SOURCE REQUIRED: Thai rules on the reporting currency of a foreign-owned Thai entity and on related-party disclosure of foreign owners.

## CAP-U28-04 Inter-company flows (payment clearing, stock transit, valuation)

### WHAT
- [N-U28-059] The only inter-company accounting automation is a clearing of customer invoices or vendor bills of one company that were settled through an online payment recorded in another company; a payment registered manually in the other company is not handled.
- [N-U28-060] The clearing is triggered when the invoice is posted, after the normal posting; nothing is triggered by confirming a payment and no scheduled job exists.
- [N-U28-061] Two entries are produced: in the paying company, a clearing entry that moves the payment's counterpart to that company's clearing account, labelled with the partner and invoice number, posted and reconciled; and in the invoicing company, a settlement entry that moves the invoice balance to that company's clearing account, labelled as an inter-company settlement with the payment memos, posted and reconciled against the invoice. Clearing lines on the paying side keep the payment currency, whereas the settlement lines are written in the invoicing company's currency.
- [N-U28-062] Stock keeps a shared Inter-company transit location, archived by default, unarchived when a company is created and impossible to delete. Routing rules that deliver to Customers are reused when looking for rules toward it, a delivery whose final destination is that location goes there, it counts as outgoing, resupply routes between warehouses of different companies use it while those of one company use that company's own inter-warehouse transit location, and purchase returns and lot display on invoices recognise it.
- [N-U28-063] Product cost is stored per company and valuation mode and cost method are company settings, so related companies can carry different costs and methods for the same product.
- [N-U28-064] NOT PRESENT IN COMMUNITY SOURCE: automatic sales-to-purchase or invoice-to-bill mirroring, inter-company pricing, automatic inter-company stock-valuation transfer and elimination entries; only payment clearing and stock transit plumbing exist.

### WHY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### BUSINESS RULE
- [N-U28-065] Clearing happens only if all of these hold: the entry is an invoice, bill or credit note that is not yet paid, partly paid or in payment; its company has a clearing journal; it is linked to online payment transactions that already produced payments; the payment belongs to a different company that also has a clearing journal; the required clearing account exists in each company (receivable in the invoice company and payable in the paying company for customer documents, reversed for vendor documents); the payment is in process or paid; and the transactions are authorized or done.

### STATE
- [N-U28-066] The sequence is: invoice posted in the invoicing company and payment recorded in the paying company; clearing entry posted in the paying company and reconciled with the payment; settlement entry posted in the invoicing company and reconciled with the invoice, which then counts as paid. Any failure aborts the posting of the invoice.

### OPTIONALITY
- [N-U28-067] Packages of goods going to a transit location are unpacked at validation unless the recipient is the shipping company itself, and only if the user group for packages is active and a system parameter is set; that parameter has no default and no screen in the Community edition.
- [N-U28-068] In the reference configuration the clearing module owns no permissions, rules, groups, scheduled jobs or automations; both a shared Inter-company transit location and the company's own Inter-warehouse transit location exist and are archived, and the unpack parameter is absent.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### CONSTRAINT
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### RISK
- [N-U28-069] The clearing reads and writes the other company's data with elevated rights, and the stock scheduler also runs with elevated rights across companies, so the posting user's company restrictions do not apply there.
- [N-U28-070] The settlement entry clears the whole receivable or payable balance of the invoice rather than the paid or residual amount and uses only the first payment's company and contact, so partial or multiple payments may be cleared incorrectly; this needs execution to confirm.
- [N-U28-071] The settlement lines carry no foreign-currency amount although the invoice may be in a foreign currency, so reconciliation and exchange-difference behaviour for foreign-currency invoices is unconfirmed.
- [N-U28-072] No exception handling exists: an error in either entry, such as a locked period or a missing account, propagates out of the posting of the invoice.
- [N-U28-073] No reversal or cancel logic exists for the clearing entries; they are ordinary posted entries and must be reversed manually.
- [N-U28-074] Only locations that belong to a company are valued; the shared inter-company transit location has no company, so goods moved into it leave the sending company's valuation without entering another company's valuation.

### UNKNOWN
- [N-U28-075] UNKNOWN — EVIDENCE INSUFFICIENT: the outcome of clearing with partial payments, foreign-currency invoices or exchange differences; resolved only by executing it on two companies with different currencies.
- [N-U28-076] UNKNOWN — STATUTORY SOURCE REQUIRED: Thai tax and accounting treatment of dealings between a Thai entity and its foreign group, including transfer pricing, withholding on cross-border payments and value-added tax on imported services.

## CAP-U28-05 Reporting and consolidation across entities

### WHAT
- [N-U28-077] The accounting module ships the data model that defines reports (lines, expressions, columns, variants) but only tax reports use it; it stores definitions and does not render them.
- [N-U28-078] A report definition can choose between a company selector and tax units, a grouping of companies filing jointly. NOT PRESENT IN COMMUNITY SOURCE: any model or data for tax units, even though the generic tax report is defined with that option.
- [N-U28-079] A report definition can choose between the most recent rate and translation adjustments. Builders for historical and average rates exist but no standard report enables them, so translation adjustment reporting is not delivered.
- [N-U28-080] The reporting menu has empty containers for partner reports, taxes and fiscal, and statements; the only delivered reports are Invoice Analysis and Analytic Report. No balance sheet, profit and loss, general ledger or trial balance is defined in the accounting module or the Thai package.
- [N-U28-081] Invoice, sales, purchase and point-of-sale sales analyses convert the amounts of all selected companies into the currency of the currently selected company using a rate table. If all companies share one currency the rates are one; otherwise the rate is derived from the latest rate on or before the report date, taken from the selected company's top-level company or from shared rates, and companies already in the target currency use one.
- [N-U28-082] A contact's receivable and payable totals are aggregated over the whole company tree of the current company's top-level company, not across different top-level companies. Multi-ledger journal groups are only a report filter scoped by company.
- [N-U28-083] NOT PRESENT IN COMMUNITY SOURCE: consolidation of several companies into group statements, inter-company elimination, minority interests, equity method or goodwill. A search for consolidation and elimination outside foreign country packages found only unrelated hits.

### WHY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### BUSINESS RULE
- [N-U28-084] Analysis rows are visible only for the user's activated companies, so a branch is included only when it is activated.

### STATE
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### OPTIONALITY
- [N-U28-085] In the reference configuration six report definitions exist: three generic tax variants with no lines and the Thai tax report with sixteen lines plus two withholding-related reports with four lines each; all use the tax-unit option and translation adjustments; no journal groups, no lock exceptions and no exchange rates exist.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### CONSTRAINT
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### RISK
- [N-U28-086] When no rate exists for a company's currency the conversion factor silently becomes one with no warning, which would misstate group amounts.

### UNKNOWN
- [N-U28-087] UNKNOWN — EVIDENCE INSUFFICIENT: whether a foreign group needs consolidated or translated statements from the Thai entity; if so, the gap in engine, elimination and ownership data must be closed outside Community or by custom development.
- [N-U28-088] UNKNOWN — STATUTORY SOURCE REQUIRED: the statutory financial statement formats for Thai entities and any joint-filing concept equivalent to tax units.

## CAP-U28-06 Statutory documents, entity numbering and identity on documents (Thailand)

### WHAT
- [N-U28-089] The invoice template is chosen per invoice by the fiscal country of the document's company: Thailand selects the Thai template, every other country keeps the standard one; an extra dispatch branch keeps the Thai template working when reports are customised.
- [N-U28-090] The Thai template replaces the title of a posted customer invoice with the fixed English words Tax Invoice; titles of drafts, cancelled invoices, pro-forma and supplier-issued billing documents are not replaced. In the standard template that title is shown only for posted customer invoices.
- [N-U28-091] A second report, Commercial Invoice, is offered only for sales journals and country Thailand; it renders the standard invoice template in the customer's language, without the Thai title or branch label, and refuses entries that are not invoices.
- [N-U28-092] The language of an invoice document is the customer's language. Company header text, tagline, footer and default terms are translatable company fields, so one entity can carry its legal text in several languages.
- [N-U28-093] A document prints the identity of its own company, read with elevated rights, so each entity prints its own header even if the user works in another company; the header shows the company's name and address from its contact, or the free-form company details when filled, followed by the company's tax identifier.
- [N-U28-094] The invoice can print its total in words, in the active language, if the company switch is on; unsupported languages fall back to English and Thai support depends on the installed library. The switch is on in the reference configuration and no Thai setting sets it.
- [N-U28-095] Invoice and entry numbers continue the previous number of the same journal, so numbering is per journal and a journal belongs to one company. Journal codes are unique per company; a branch can use its parent's journals and then shares their numbering, and has separate numbering only with its own journals. A journal can keep separate series for credit notes and payments. Order numbers use a sequence of the current company if one exists, otherwise a company-less sequence; in the reference configuration the sales and purchase order sequences have no company, so they are shared by all companies. Each company has its own group-payment series.
- [N-U28-096] The Thai template defaults sale tax to output value-added tax at seven percent and purchase tax to input tax at seven percent, sets the fiscal country, exchange and cash-difference accounts and early-payment accounts, and defines eighteen taxes: seven percent, zero percent and exempt for sales and purchases plus negative-rate withholding-style variants named by percentage and a letter code.
- [N-U28-097] The Thai package defines three report definitions, a general tax report and two withholding-related reports, available by company fiscal country; they are data only because Community has no engine to render or file them.
- [N-U28-098] Thai wording is supplied only through translation layers: translation attributes in report data, dedicated translation columns in the chart and tax data files, and the Thai translation file keyed by the English source strings for the branch labels and the invoice title. The English text is the source; the demonstration company also hard-codes a Thai-script city in demo data that is not loaded.
- [N-U28-099] NOT PRESENT IN COMMUNITY SOURCE for Thailand: tax-invoice numbering rules, abbreviated tax invoice, withholding certificate, value-added tax return form, electronic tax invoice, per-branch tax report. The Thai package depends only on accounting and the bank QR module; the debit-note and withholding-on-payment modules exist but are not installed; a taxable-supply-date hook exists but is empty.

### WHY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### BUSINESS RULE
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### STATE
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### OPTIONALITY
- [N-U28-100] In the reference configuration the Thai package owns one report action, three views, three report definitions with their lines, eighteen taxes and a chart of 147 accounts; debit-note and withholding modules are not installed; sale and purchase journals keep separate credit-note series; demo data is not loaded.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### CONSTRAINT
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### RISK
- [N-U28-101] The company's legal name comes from its contact name, a single non-translatable value, so a second-language legal name must be placed in the translatable details text.
- [N-U28-102] The document header reads no registry number and no branch value of the issuing company, so branch identification of the issuer depends on manually written company details.
- [N-U28-103] The Thai template switches on the company's tax-on-payment flag while all configured taxes use on-invoice timing; how the two interact needs execution.
- [N-U28-104] The error text of the Thai bank QR names it with another market's payment brand and only THB invoices can be paid by it, so user-facing text of this Thai feature is inconsistent.

### UNKNOWN
- [N-U28-105] UNKNOWN — STATUTORY SOURCE REQUIRED: which documents a Thai entity or branch must issue, their mandatory header content including legal name, address, taxpayer identifier and branch, numbering continuity per branch, and language requirements of Thai tax documents.
- [N-U28-106] UNKNOWN — EVIDENCE INSUFFICIENT: the rendered output of the Thai invoice and Commercial Invoice, including label placement, Thai script fonts and language fallback; resolved only by rendering.

## CAP-U28-07 Company-to-jurisdiction assignment for the foreign-group structures

### WHAT
- [N-U28-107] Each company has a fiscal country that decides which tax reports and taxes apply; it defaults to the address country only when empty and is separate from it afterwards. Loading the Thai chart sets it to Thailand.
- [N-U28-108] Each tax carries a country derived from its company's fiscal country; tax names are unique per type, scope and country across a whole company tree rather than per branch.
- [N-U28-109] A tax whose country differs from the accessible branch's fiscal country is displayed with its country code, which shows that the code anticipates branches and taxes with different countries.
- [N-U28-110] Fiscal positions map taxes and accounts by country, country group, state, zip range and tax-identifier presence; a position set on the contact always wins, automatic detection returns nothing for a contact without a country, the most specific company wins among automatic matches, and a company's tax-enabled countries are its fiscal country plus those of its foreign-registration positions.
- [N-U28-111] The proposed chart is the first template whose country matches the company country, otherwise the generic chart.
- [N-U28-112] Exchange rates are stored and resolved per top-level company and are unique per date, currency and company; a separate legal entity maintains its own rate table unless rates are left company-less.
- [N-U28-113] Each foreign-currency invoice stores its own rate taken at the invoice date, and exchange differences are booked in the company's exchange journal and accounts, which are company settings.
- [N-U28-114] The effective soft lock dates of a branch are the latest of its own and its ancestors' dates, with per-user exceptions per ancestor, and the hard lock is the maximum over ancestors; a branch cannot be less locked than its top-level company.
- [N-U28-115] Valuation mode, cost method, anglo-saxon switch, price-includes-tax default and storno default are per-company settings, so a Thai subsidiary can differ from its foreign parent; price-includes-tax cannot change after invoicing starts, and storno defaults from the fiscal country.
- [N-U28-116] A contact's receivable and payable accounts, fiscal position, payment terms, credit limit and trust level are stored per company, so one foreign customer or vendor can have different accounts and terms in each entity.

### WHY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### BUSINESS RULE
- [N-U28-117] Loading a chart on a top-level company with no entries sets its currency to that of the fiscal country, overriding any earlier choice; on a branch the parent's currency is used.
- [N-U28-118] Loading a chart on a branch loads only company-level values, copies the top-level company's default accounts and does not duplicate accounts, taxes, journals or fiscal positions; loading a chart on a company also loads it on all its branches.
- [N-U28-119] Switching to another chart on a top-level company with no entries deletes its existing chart records and entries before loading, and only system administrators may load a chart.
- [N-U28-120] A company's currency cannot be changed once any journal item exists anywhere in its tree, so a foreign owner cannot later re-denominate a Thai entity.

### STATE
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### OPTIONALITY
- [N-U28-121] In the reference configuration the single company has fiscal country Thailand, currency THB, the Thai chart, periodic valuation, standard cost, anglo-saxon off, tax on payment on, tax-excluded prices, fiscal year ending on 31 December, amount in words on and no lock dates, no fiscal positions, two active currencies and no exchange rates.

### DEPENDENCY
- [N-U28-122] A fiscal position with a foreign tax registration can create taxes of another country by installing that country's package; those foreign packages are outside scope.
- [N-U28-123] Creating a company with a country installs that country's automatic accounting package; creating a company in another country would install a foreign package that is out of scope.

### CONSTRAINT
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### RISK
- [N-U28-124] A foreign customer or vendor without a country receives no tax mapping, and the Thai template creates no fiscal position, so foreign parties need a country and a manually defined position to be taxed differently.
- [N-U28-125] Loading the Thai template on a branch writes Thailand as its fiscal country, so a foreign branch of a Thai company or a Thai branch of a foreign company probably cannot keep a different fiscal country once a chart is loaded; this needs execution.

### UNKNOWN
- [N-U28-126] UNKNOWN — STATUTORY SOURCE REQUIRED: Thai rules on the accounting currency of a foreign-owned entity, on keeping books in a foreign currency, and on how a Thai branch of a foreign company or a foreign branch of a Thai company is taxed and reported.
- [N-U28-127] UNKNOWN — EVIDENCE INSUFFICIENT: runtime behaviour of a branch located in a different country from its top-level company, including fiscal country, taxes and reports; resolved only by executing with two companies.

## CAP-U28-08 Roles, record rules and audit across entities

### WHAT
- [N-U28-128] The restrictive audit trail, which prevents deletion of journal-item related logs, is a per-company flag; audit log views are filtered by it for entries, accounts, taxes, contacts and companies; the company record has a change log that tracks lock dates and the flag.

### WHY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### BUSINESS RULE
- [N-U28-129] Employees, portal and public users see only the companies in their active set, while the system-administration group sees all companies.
- [N-U28-130] Contacts of internal users are visible in every company; customer and vendor contacts are visible when shared or owned by an active company or one of its ancestors.
- [N-U28-131] Users are visible to others only if they are internal or share at least one active company; belonging to several companies gives the multi-company display group, which only controls interface visibility.
- [N-U28-132] Journal entries, lines, payments, statements and invoice analysis follow a strict company rule: only entries of activated companies are visible, so a branch's entries are hidden unless the branch itself is activated. A billing group rule that shows all entries is combined with the company rule by the rule engine, which ands global rules with the group rules, so it does not remove company isolation.
- [N-U28-133] Master data such as accounts, journals, taxes, fiscal positions, exchange rates and bank accounts follow a parent-of rule: records of an ancestor are visible from a branch, and company-less records are visible to all.
- [N-U28-134] Payments cannot be registered in one operation for entries of different top-level companies; branches of one top-level company can be paid together, but sibling branches require access to the parent, and the payment is then created in the parent. Reconciliation across top-level companies is refused, and linking a record to another company's record is refused by an automatic consistency check.
- [N-U28-135] Soft lock dates can be relaxed per user or for everyone by lock exceptions defined per company; a hard lock date allows no exception and can neither be removed nor moved earlier.

### STATE
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### OPTIONALITY
- [N-U28-136] In the reference configuration 144 record rules reference a company, 139 of them global, out of 544 rules and 2010 permission rows; four users each have one allowed company; the account manager group has two members; the audit flag is unset and there are no lock exceptions.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### CONSTRAINT
- NOT APPLICABLE — no statement of this kind was derived for this capability.

### RISK
- [N-U28-137] Inter-company clearing and the stock scheduler use elevated rights, so company isolation is bypassed in those paths and depends on their correctness.

### UNKNOWN
- [N-U28-138] UNKNOWN — EVIDENCE INSUFFICIENT: behaviour for a user allowed in several entities with real data, including the switcher, the effect of the default company on new documents and cross-company reports; resolved only by executing with two companies and two users.
- [N-U28-139] UNKNOWN — STATUTORY SOURCE REQUIRED: segregation-of-duties and record-retention requirements for Thai entities and their branches.

