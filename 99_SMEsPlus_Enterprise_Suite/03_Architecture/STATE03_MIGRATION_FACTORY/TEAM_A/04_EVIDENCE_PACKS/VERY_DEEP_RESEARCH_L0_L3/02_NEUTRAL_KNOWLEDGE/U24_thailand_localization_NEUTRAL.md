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
