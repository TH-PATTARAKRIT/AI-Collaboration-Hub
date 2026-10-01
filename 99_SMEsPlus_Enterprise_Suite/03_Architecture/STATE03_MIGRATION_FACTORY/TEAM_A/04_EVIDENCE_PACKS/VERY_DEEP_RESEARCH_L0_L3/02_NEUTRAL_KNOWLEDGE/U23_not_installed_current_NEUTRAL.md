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

