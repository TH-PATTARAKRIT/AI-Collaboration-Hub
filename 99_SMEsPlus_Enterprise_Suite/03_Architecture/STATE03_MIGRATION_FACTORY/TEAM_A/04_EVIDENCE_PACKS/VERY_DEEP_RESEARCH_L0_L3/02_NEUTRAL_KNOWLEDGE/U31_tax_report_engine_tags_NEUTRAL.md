# U31 — Tax report and tax grid tag infrastructure (neutral knowledge)

> `DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION` — neutral layer for Thai Tax Core unit U31; clean-room wording; Odoo 19 Community (named once here). Not legal or tax advice; statutory identifiers refer to the statutory register of the programme and are cross-references only.

Scope of the unit: how a report is defined as data, what exists in the studied edition to compute, show or file a report, how tax grid tags are created, named, scoped and applied to journal items (including credit notes, reversals and payment-time entries), what the closing flag and carry-over fields do, who can see and change this data, and what Thai VAT and withholding reporting would need from this layer.

Reading rule: every statement carries an id in square brackets that links to technical evidence in the restricted file. Where the studied edition has no function, the text says "not present"; absence does not prove that a business requirement is absent.

## CAP-U31-01 Report definition structure

### WHAT

- [N-U31-001] A report is not code. It is stored data made of five kinds of records: the report itself, its lines, the computation rules (expressions) attached to lines, its display columns, and externally entered values.
- [N-U31-002] A report can be a variant of a root report (for example a national variant of a generic tax report), and a composite report can list other reports as sections; only one level of each is allowed.
- [N-U31-003] Report lines form a tree of parent and child lines; a line may carry a short code, unique inside its report, that other formulas use to refer to it; a line can also be set to break down by dimensions of the journal items.
- [N-U31-004] A report has display columns; each column names the computation label it shows, a figure type (monetary by default, or percentage, integer, float, date, datetime, boolean, string), and may blank zero values.
- [N-U31-005] A line can be foldable, start a new printed page, be hidden when zero, or link to an action; a line's hierarchy level is derived from its parent.

### WHY

- [N-U31-006] Keeping the layout of a return as data lets a country package ship its structure, tag names, line labels and formulas together and keep them consistent without writing code.

### BUSINESS RULE

- [N-U31-007] A report that is already a variant cannot be the root of another variant, and the sections of a composite report cannot have sections of their own.
- [N-U31-008] A parent line must be listed before its children, a line cannot be its own parent, and a line that has children cannot also break down by dimensions.
- [N-U31-009] A line code is unique within its report and a computation label is unique within its line.
- [N-U31-010] A report that has variants cannot be deleted.
- [N-U31-011] Copying a report copies its lines, rules and columns, gives copied line codes a copy suffix, and rewrites those codes inside aggregation formulas and sub-formulas.
- [N-U31-012] A report whose availability is by country match must name that country; a variant that has a country defaults to country-match availability.

### OPTIONALITY

- [N-U31-013] Availability of a report can be by country match, by chart-of-accounts match, or always.
- [N-U31-014] A report declares which viewer controls would be offered: multi-company mode (company selector or tax units), date range, draft entries, unreconciled entries, unfold all, hide zero lines, period and growth comparison, journals, analytic filter, account groups, account types, partners, saved filters and budgets; variants and sections take their defaults from their root or main report.
- [N-U31-015] A report also declares a default opening period, a currency translation method (latest rate or cumulative translation), integer rounding, a load-more limit, a search bar, a prefix-grouping threshold, an only-exigible-lines switch and a foreign-VAT permission.

### DEPENDENCY

- [N-U31-016] Which national report applies to a company follows the company's fiscal country, which defaults to the company's country and is described as the country whose tax reports are used.

### RISK

- [N-U31-017] Report, line, rule, column, tag and external-value records keep no change history of their own; edits are visible only through creation and modification stamps.
- [N-U31-018] Deleting a report sets the link of its columns to empty instead of deleting them, so orphan columns can remain (inference from the link behaviour).

### UNKNOWN

- [N-U31-019] How lines, columns and switches would be presented to a user is not defined in the studied scope because no viewer exists in it.

## CAP-U31-02 Computation methods a report line can declare

### WHAT

- [N-U31-020] A computation rule uses one of six methods: a stored condition over journal items, tax grid tags, aggregation of other rules, account-code prefixes, externally entered values, or a custom routine.
- [N-U31-021] Formulas are checked when saved: a condition formula must be a valid search condition over journal items, an account-code formula must split into prefix terms (with optional exclusions, balance side, or a tag reference), and an aggregation formula must be arithmetic over line-code references or the keyword for the sum of children.
- [N-U31-022] A line accepts one-field shortcuts per method so a data file can declare the common balance rule compactly; a shortcut creates or replaces the rule named balance, and an external shortcut maps to a most-recent or sum rule.
- [N-U31-023] Aggregation rules may refer to another report through a cross-report reference and may carry conditional sub-formulas (above or below a threshold, or depending on another rule); dependency-expansion helpers exist for them.
- [N-U31-024] An external-value rule reads values a user enters (numeric or text, dated, per company) and can be marked editable.
- [N-U31-025] A custom-routine rule only names a routine; the routine must be supplied by another package.
- [N-U31-026] Every method except custom is flagged auditable, meaning a value could be drilled into the underlying entries.
- [N-U31-027] A rule can carry a figure type, a growth-is-good flag (true by default) and a blank-when-zero flag.

### BUSINESS RULE

- [N-U31-028] A condition rule must have a sub-formula; aggregation and external rules cannot sit on a line that breaks down by dimensions; a cross-report reference cannot point at its own report and must be well formed.
- [N-U31-029] For a tag rule the formula is the tag name, optionally preceded by a minus that means the balance is negated when displayed.

### RISK

- [N-U31-030] Tag, external and custom rules have no formula validation at save time, so a mistyped tag name simply creates a new tag.
- [N-U31-031] No routine in this edition evaluates any method, so the grammar, thresholds and date scopes are carriers of syntax only and their numeric meaning is undefined here.

### UNKNOWN

- [N-U31-032] Numeric results of any rule, the treatment of the negation prefix at evaluation, rounding, and the meaning of the conditional sub-formulas cannot be established from the studied source.

## CAP-U31-03 Running, displaying, exporting and filing a report (entry points and what is absent)

### WHAT

- [N-U31-033] No screen, menu entry, window action, client action, print template, controller, scheduled job or export routine exists in this edition to evaluate, display, print, export or file a report built from these definitions.
- [N-U31-034] Menu containers named for partner reports, tax and fiscal reports, statement reports and management reports exist; the tax and fiscal, partner and statement containers hold no entries, and the dump shows the same empty containers.
- [N-U31-035] The accounting settings show a dynamic-reports switch that is an upgrade prompt for a package that is not in the source tree and not in the dump.
- [N-U31-036] The only code trace of a viewer is a lookup for a client action of a particular kind, used to decide filter defaults; no such action exists in the source or the dump.
- [N-U31-037] Printable accounting documents that do exist are invoices (with or without payments), the original vendor bill, the payment receipt, the bank statement, the ledger-integrity check and the Thai commercial invoice; none is a tax return, tax book or withholding certificate.
- [N-U31-038] Analysis entries that exist are invoice analysis, an analytic report and product margins; none reads tax grid tags.
- [N-U31-039] An installed spreadsheet-formula package can fetch debit, credit, balance, residual and partner balance by account-code prefix or by account tag and period; it cannot select entries by tax grid tag; one invoicing dashboard uses it.
- [N-U31-040] A tax-details query helper and an exigible-lines filter exist, but nothing in the edition calls the filter and only tests call the helper.

### WHY

- [N-U31-041] Monthly VAT returns, withholding returns and tax books are statutory outputs (see the statutory register); report definitions alone cannot produce them.

### DEPENDENCY

- [N-U31-042] Any Thai return or tax book depends on an evaluation, display, export and filing layer that this edition does not contain; it must come from an extension or another package.

### RISK

- [N-U31-043] A reader who sees three Thai report definitions in the data may wrongly assume that Thai returns can be produced; no figure can be computed or displayed with the shipped edition.
- [N-U31-044] Some foreign-country packages extend the report model with viewer behaviour that has no base here, which shows that the viewer is expected from a package outside this edition.

### UNKNOWN

- [N-U31-045] The behaviour of the outside package (period selection, return creation, export formats) is not studied and nothing is assumed about it.

## CAP-U31-04 Thai VAT and withholding report definitions as supplied

### WHAT

- [N-U31-046] The Thai package supplies three report definitions, all variants of the generic tax report, available when the company's fiscal country is Thailand, each with a single balance column; the main one allows foreign VAT.
- [N-U31-047] Together they hold 24 lines and 29 rules: 13 tag rules, 15 aggregations and 1 external-value rule; 24 rules are declared in the data and 5 more are generated from line shortcuts.
- [N-U31-048] The main report has four headed sections (output tax, input tax, value added tax, net tax) holding twelve numbered lines that follow the layout of the monthly VAT return: sales amount, zero-rated sales, exempt sales, taxable sales, output tax, purchases entitled to deduction, input tax, tax payable, excess tax, excess carried from the previous period, net tax payable and net excess.
- [N-U31-049] Lines 1, 2, 3, 5, 6, 7 and 10 read tax grid tags; the output-side tag rules carry the negation prefix and the input-side ones do not.
- [N-U31-050] Taxable sales are sales minus zero-rated and exempt sales; tax payable is output tax minus input tax when positive; excess tax is input tax minus output tax when positive; net tax payable is payable minus the carried excess when positive.
- [N-U31-051] Line 10 adds an externally stored value taken from the previous return period to its own tag; line 12 combines two partial results and names line 10 as its carry-over target.
- [N-U31-052] The two withholding reports (payee is a juristic person, payee is an individual) each have four lines: total income (tag), total remittance (tag), surcharge (tag) and a total that adds remittance and surcharge.
- [N-U31-053] The positive-part sub-formulas hard-code the Thai baht as currency.
- [N-U31-054] The tag for excess carried forward and both surcharge tags exist, but no tax distribution line uses them; surcharges and carried excess can only come from manual tagging or from the external value.
- [N-U31-056] Line labels double as tag names, and Thai translations of them are shipped in the data but the Thai language is not active in the dump.

### RISK

- [N-U31-055] The input-side and withholding tag rules have no negation; with ordinary vendor-bill signs the raw tax balance is credit-negative and the income balance debit-positive, so the sign shown to a user would depend on the missing evaluator (inference).

### UNKNOWN

- [N-U31-057] Whether the shipped definitions match current statutory return layouts is a legal question not answered by the source.

## CAP-U31-05 Provisioning, naming and country scope of tax grid tags

### WHAT

- [N-U31-058] A tag has a name, a purpose (accounts, taxes or products), an optional country, a colour and an active flag; tax tags are bound to a country.
- [N-U31-059] A tax tag never carries a sign; the sign is expressed by the leading minus of the report rule that reads it, and a tag can report whether its rule negates.
- [N-U31-060] Saving a tag rule creates the matching tax tag in the report's own country if it does not exist; the tag name is the formula without its minus.
- [N-U31-061] Chart templates only look up tags by name for the template's country (archived tags included) and never create them; an unknown name stops loading with an instruction to update the localization unless the loader is told to ignore missing tags.
- [N-U31-062] Tax tags whose name equals a report line label are translated from the line's translations when created and when a language is installed.

### BUSINESS RULE

- [N-U31-063] A tag name is unique per purpose and country; the same name may exist for several countries, and tags without a country are not protected from duplicates by the database.
- [N-U31-067] The three cash-flow master tags cannot be deleted.

### STATE

- [N-U31-064] When the formula of every rule using a tag is changed together the tag is renamed; when other rules still use the old text a new tag is created instead.
- [N-U31-065] Deleting the last rule that uses a tag archives the tag if journal items carry it and deletes it otherwise; in both cases it is removed from tax distribution lines.
- [N-U31-066] Changing a report's country moves its tags to the new country when no other report uses them, otherwise creates matching tags in the new country.

### OPTIONALITY

- [N-U31-070] Products can carry tags of product purpose that the engine copies onto their journal items, and accounts can carry account tags for custom reporting such as cash-flow classification.

### DEPENDENCY

- [N-U31-071] Tax tags exist because a report rule names them; a report without a country creates tags without a country.
- [N-U31-072] The Thai package gets its thirteen tags from its report rules, not from the chart template; they have no data identifiers, so the upgrade-preservation hook has nothing to protect in this database.

### CONSTRAINT

- [N-U31-068] A tag used on a tax distribution line or on a journal item cannot be deleted directly.
- [N-U31-069] The tags offered for a distribution line are those with no country, the company's fiscal country or its foreign-VAT countries; this is a form-level filter and is not enforced on save, where only the tax purpose is checked.

### RISK

- [N-U31-073] A tag is linked to its rule by name only, ignoring country and method, so identical formula text in different countries' reports would resolve ambiguously.
- [N-U31-074] Editing a report formula silently renames a tag already carried by posted entries, changing how historical entries are read.
- [N-U31-075] Deleting a country empties the country of its tags, which turns them into global tags.
- [N-U31-076] If a rule is later created with the name of an archived tag, that archived tag is found and reused without being reactivated and is no longer on any distribution line (inference).

### UNKNOWN

- [N-U31-077] The effect of activating the Thai language on tag names and translations was not executed.

## CAP-U31-06 Applying tax grid tags to journal items (documents, credit notes, entries, reversals)

### WHAT

- [N-U31-078] Tags are written onto journal items when the tax lines of a draft document are computed; posting does not recompute them and posted documents are not recomputed.
- [N-U31-079] A base line receives the base-side tags of every tax on it plus product tags; a tax line receives its distribution line's tags, the product tags, and the base tags of earlier taxes that affect the base.
- [N-U31-080] Customer invoices and vendor bills use invoice distribution lines, credit notes use refund distribution lines, and manual entries choose by the sign of the amount and the purpose of the tax.
- [N-U31-081] Because tags are unsigned and a credit note carries the same tags with opposite amounts, a report that sums tagged balances nets credit notes automatically; the displayed sign comes from the negation prefix of the rule.
- [N-U31-082] Reversing an invoice creates a credit note whose lines are recomputed with refund distribution; reversing a manual entry copies its lines, tags included, with negated amounts.
- [N-U31-083] A cash-rounding line using the biggest-tax strategy copies the tags of the biggest tax line, and early-payment-discount lines carry their base and tax tags.
- [N-U31-084] Tax lines with a zero amount are dropped, so zero-rated and exempt sales carry base tags only.
- [N-U31-085] Tax lines merge only when partner, currency, analytic distribution, account, taxes, distribution line, group and tags are identical.
- [N-U31-086] Company-paid expense entries are built with the same engine and include cash-basis tags.

### BUSINESS RULE

- [N-U31-088] On a posted entry a change to amount, tax, tax line or tags is checked against the tax lock date, and changing the taxes of a posted line is refused outright; only lines that affect the tax report (have taxes, are tax lines, or carry tax tags) are guarded.
- [N-U31-090] Reverse-charge treatment uses the negative-factor distribution lines and adds no base tags.
- [N-U31-091] Changing the tags of a tax distribution line does not change existing journal items; only lines computed afterwards use the new tags.

### STATE

- [N-U31-087] When every tax is removed from a non-posted entry, the tags on its lines are cleared.

### OPTIONALITY

- [N-U31-092] Whether a tag appears on tax lines at all is a matter of tax configuration: taxes with no distribution tags produce untagged lines.

### CONSTRAINT

- [N-U31-089] Invoice and refund distribution of a tax must have the same number of lines in the same order with the same basis and percentage; positive tax factors total 100 percent and negative ones, if any, total minus 100 percent; exactly one base line is required for each document type.

### RISK

- [N-U31-093] For manual entries that mix sale and purchase taxes the invoice or refund choice defaults by amount sign, which can mis-tag unusual entries.
- [N-U31-094] Withholding tax lines on vendor bills are credit-negative and are read without negation in the Thai rules, so their presentation sign is undecided.

### UNKNOWN

- [N-U31-095] The dump holds no transactions, so real tag outcomes for invoices, credit notes and reversals were not executed.

## CAP-U31-07 Cash-basis exigibility and its tags

### WHAT

- [N-U31-096] A company switch enables cash-basis taxes and each tax is due either on invoice or on payment; the Thai company has the switch on and every Thai tax is due on invoice.
- [N-U31-097] For a tax due on payment the original invoice carries no tag; the tags appear on a separate entry created at each payment and posted on the settlement date, moved after the fiscal lock date if needed.
- [N-U31-098] Entries that are not invoices and have no cash-basis lines count as always exigible and receive all tags at entry time.
- [N-U31-099] An optional payment-time withholding add-on (not installed) builds its entries from the same tax engine: withholding tax lines carry the distribution tags with negated amounts, the withholding base line carries no tag, and its counterpart line keeps the base tags (inference).

### STATE

- [N-U31-100] Undoing a reconciliation reverses the cash-basis entry in the period of the original entry, or after the lock date if the period is locked.

### OPTIONALITY

- [N-U31-103] A report can be marked to count only exigible lines; all six reports have it on, but no evaluator in this edition uses it and the filter that expresses it has no caller.

### CONSTRAINT

- [N-U31-101] Taxes due on payment and taxes due on invoice cannot share a tag on the same journal item.
- [N-U31-102] Cash-basis entries are not generated when several currencies are involved on the entry.

### RISK

- [N-U31-104] The cash-basis path is dormant for Thailand because no tax is due on payment; adopting payment-time withholding would activate it and its tag behaviour has never been exercised here.

### UNKNOWN

- [N-U31-105] Cash-basis entry outcomes (tags, dates, partial payments) were not executed.

## CAP-U31-08 Re-applying tags to existing journal items

### WHAT

- [N-U31-106] The only way to bring existing journal items in line with a changed tag configuration is an optional administrator tool, not installed in the dump; no automatic propagation exists.
- [N-U31-107] From a chosen date and for one company, the tool recomputes the tags the current tax configuration assigns (base items through the tax or its children, tax items through their distribution line, invoice versus refund by document type, amount sign for plain entries) and replaces all tag links on those items with direct database statements.

### BUSINESS RULE

- [N-U31-108] The tool refuses a child tax that belongs to several parent group taxes; apart from that it has no state, lock or role check beyond administrator access, and its lock-date warning is informational.

### STATE

- [N-U31-109] A run is irreversible except from a backup, leaves no change log and covers draft, posted and cancelled entries alike.

### RISK

- [N-U31-110] The tool deletes all tag links on affected items but re-inserts only distribution tags, so product-purpose tags carried by those items would be lost (inference).
- [N-U31-111] The tool does not skip taxes due on payment, so on entries with such taxes it would add base and tax tags that the normal engine deliberately omits, risking double counting with cash-basis entries (inference).

### UNKNOWN

- [N-U31-112] The tool was not executed; effects on closed returns, hashed entries and reconciled items are unknown.

## CAP-U31-09 Tax closing flag, return periods, date scope and carry-over

### WHAT

- [N-U31-113] Each tax distribution line has a used-in-tax-closing flag, true by default for tax-type lines on accounts that are neither income nor expense.
- [N-U31-114] In this edition the flag only decides whether the line's analytic distribution is copied to the tax line, appears in the tax change log, and is returned by the legacy computing interface and a details query; no closing routine reads it.
- [N-U31-115] Tax groups hold payable, receivable and advance accounts described as counterparts of a tax closing entry; no routine reads them here; the Thai groups have payable and receivable set.
- [N-U31-116] The tax lock date is a manual company field whose help text says it is set when a closing entry is posted; nothing in the studied source sets it.
- [N-U31-117] Report options and one date-scope value speak of this or the previous return period, but the company has no return periodicity and no period model exists here.
- [N-U31-118] A rule's date scope is one of six values: from the very start, from fiscal-year start, at fiscal-year start, at period start, strictly the given dates, or from the previous return period; only the definitions exist.
- [N-U31-119] Carry-over is defined by label convention: a rule whose label starts with the carry prefix targets a rule whose label starts with the applied-carry prefix, by default on the same line or through an explicit target; the stored values live on the external-value record, whose origin line and label can be kept; no routine here creates or reads them.

### OPTIONALITY

- [N-U31-121] The generic tax report opens by default on the previous return period and every variant, including the three Thai ones, inherits that.

### DEPENDENCY

- [N-U31-123] The generic report asks for a tax-unit multi-company mode, but no tax-unit concept exists in this edition.

### CONSTRAINT

- [N-U31-120] A carry-over target may be set only on a rule whose label starts with the carry prefix, and it must point at a rule whose label starts with the applied-carry prefix; without an explicit target the applied rule on the same line is chosen, and its absence is an error.

### RISK

- [N-U31-122] Without a closing routine, month-end transfer of tax balances, carry-forward of excess input tax and advancement of the tax lock date are manual.

### UNKNOWN

- [N-U31-124] How a return period would be derived for a Thai monthly filer cannot be determined from the source.

## CAP-U31-10 Access control, company scope and audit of report and tag data

### WHAT

- [N-U31-125] Report definitions can be read by the basic accounting, read-only accounting and administrator groups and changed only by administrators; invoicing users and plain internal users have no access to report, line, rule or column definitions.
- [N-U31-126] Tags can be read by every internal user and by sales, purchase and invoicing groups and changed by the full accounting group; distribution lines can be read by internal users and changed by administrators.
- [N-U31-127] Externally entered values can be read by the read-only accounting group and changed by administrators; the basic accounting group has no access; a company rule limits them to the user's companies.
- [N-U31-128] Report definitions, columns, rules and tags carry no company and are shared by all companies, scoped only by country; external values and journal items are company-scoped.
- [N-U31-129] Changes to report, line, rule, column, tag and external-value records are not logged; tag edits on journal items after first posting and distribution edits on a used tax are logged.
- [N-U31-130] Spreadsheet formulas read journal items under the caller's access rights and the requested company.

### BUSINESS RULE

- [N-U31-131] Condition formulas are parsed as literal search conditions and are not executed.
- [N-U31-132] Each company's fiscal country selects which country's reports and tags apply, so companies in different countries can use different variants of the same shared data.

### RISK

- [N-U31-133] Because definitions and tags are shared, an administrator of one company who changes a shared report or tag affects every company.
- [N-U31-134] There is no audit trail for definition changes, although such changes can alter how past entries are read.

### UNKNOWN

- [N-U31-135] Effective access for real users was not exercised; the dump holds the same access rows as the source.

## REGISTER: Function Catalog

| Cat-ID | Function (neutral name) | Topic # | Statutory link | Native status | Statements |
|---|---|---|---|---|---|
| U31-F01 | Maintain report definitions as data (reports, variants, sections, lines, columns) | 9 | not applicable | PARTIAL | N-U31-001 N-U31-002 N-U31-003 N-U31-004 |
| U31-F02 | Declare computation rules and validate their formulas when saved | 9 | not applicable | PARTIAL | N-U31-020 N-U31-021 N-U31-030 |
| U31-F03 | Evaluate report rules into figures | 9 | S09-01, S09-02, S15-01 | NATIVE GAP / EXTENSION REQUIRED | N-U31-031 N-U31-032 N-U31-042 |
| U31-F04 | Display, print or export a tax report | 9 | S09-01, S09-08, S15-01 | NATIVE GAP / EXTENSION REQUIRED | N-U31-033 N-U31-034 N-U31-035 |
| U31-F05 | Produce VAT return filing data and file it | 9 | S09-02, S09-09, S11-04 | NATIVE GAP / EXTENSION REQUIRED | N-U31-041 N-U31-042 |
| U31-F06 | Produce withholding returns by payee type and payee certificates | 9 | S13-02, S13-03, S13-04, S13-08 | NATIVE GAP / EXTENSION REQUIRED | N-U31-052 N-U31-041 |
| U31-F07 | Output tax and input tax books per document | 9 | S09-08, S15-01 | NATIVE GAP / EXTENSION REQUIRED | N-U31-040 N-U31-041 |
| U31-F08 | Foreign-payee withholding and reverse-charge VAT return data | 9 | S10-02, S13-04 | NATIVE GAP / EXTENSION REQUIRED | N-U31-041 |
| U31-F09 | Create tax grid tags from report rules | 1 | not applicable | NATIVE | N-U31-060 N-U31-064 N-U31-065 N-U31-066 |
| U31-F10 | Map tags by name when loading a chart template | 8 | not applicable | NATIVE | N-U31-061 |
| U31-F11 | Apply tags to journal items of invoices, bills, credit notes and tax entries | 1, 7 | not applicable | NATIVE | N-U31-078 N-U31-079 N-U31-080 |
| U31-F12 | Tags on reversals and credit notes (netting by amount sign) | 4, 7 | not applicable | NATIVE | N-U31-081 N-U31-082 |
| U31-F13 | Tags on payment-time (cash-basis) entries | 5, 7 | S05-02 | PARTIAL | N-U31-097 N-U31-096 N-U31-104 |
| U31-F14 | Re-apply tags to existing entries after a configuration change | 7, 9 | not applicable | PARTIAL | N-U31-106 N-U31-107 N-U31-091 |
| U31-F15 | Tax closing, return period and carry-forward of excess input tax | 5, 9 | S09-01, S09-06, S09-07 | NATIVE GAP / EXTENSION REQUIRED | N-U31-114 N-U31-115 N-U31-119 N-U31-122 |
| U31-F16 | Tax lock date guarding tax-affecting entries and tag edits | 5 | not applicable | NATIVE | N-U31-088 N-U31-116 |
| U31-F17 | Access and company scope of report and tag data | 10 | not applicable | PARTIAL | N-U31-125 N-U31-126 N-U31-128 |
| U31-F18 | Audit trail of tag and definition changes | 10 | not applicable | PARTIAL | N-U31-129 N-U31-134 |
| U31-F19 | Ledger balance spreadsheet formulas and invoicing dashboard | 12 | not applicable | NATIVE | N-U31-039 |
| U31-F20 | Thai VAT and withholding report definitions as supplied | 9 | S09-01, S13-04 | PARTIAL | N-U31-046 N-U31-048 N-U31-052 N-U31-057 |

## REGISTER: Business Rules

| BR-ID | Rule (neutral) | Condition / configuration | Statements | Class |
|---|---|---|---|---|
| BR-U31-01 | A variant cannot have a variant and a section cannot have sections | always | N-U31-007 | CONSTRAINT |
| BR-U31-02 | A parent line precedes its children, a line is not its own parent, and a line with children does not break down by dimensions | always | N-U31-008 | CONSTRAINT |
| BR-U31-03 | A line code is unique per report and a rule label is unique per line | always | N-U31-009 | CONSTRAINT |
| BR-U31-04 | A report with variants cannot be deleted | always except package removal | N-U31-010 | CONSTRAINT |
| BR-U31-05 | Country-match availability needs a country | always | N-U31-012 | CONSTRAINT |
| BR-U31-06 | Copying a report renames line codes inside its formulas | on copy | N-U31-011 | DERIVATION |
| BR-U31-07 | Condition, account-code and aggregation formulas are validated when saved; tag, external and custom ones are not | always | N-U31-021 N-U31-030 | CONSTRAINT |
| BR-U31-08 | A condition rule needs a sub-formula; aggregation and external rules cannot sit on a line that breaks down by dimensions | always | N-U31-028 | CONSTRAINT |
| BR-U31-09 | A tag rule names a tag; a leading minus negates the displayed balance | tag rules | N-U31-029 N-U31-059 | DERIVATION |
| BR-U31-10 | Saving a tag rule creates the tag in the report's country when absent | rule saved | N-U31-060 N-U31-071 | DERIVATION |
| BR-U31-11 | A tag name is unique per purpose and country; tags without a country can be duplicated | always | N-U31-063 | CONSTRAINT |
| BR-U31-12 | A formula change renames the tag only when every rule using it changes together | rule edited | N-U31-064 N-U31-074 | DERIVATION |
| BR-U31-13 | Deleting the last rule using a tag archives it if entries carry it, otherwise deletes it | rule deleted | N-U31-065 | DERIVATION |
| BR-U31-14 | Changing a report's country moves or duplicates its tags | report edited | N-U31-066 | DERIVATION |
| BR-U31-15 | Master cash-flow tags and tags in use cannot be deleted | always | N-U31-067 N-U31-068 | CONSTRAINT |
| BR-U31-16 | The tag choice on a distribution line is filtered by country only in the form | form | N-U31-069 | CONFIG |
| BR-U31-17 | Chart templates map tags by name and never create them; an unknown name stops the load | template load | N-U31-061 | CONSTRAINT |
| BR-U31-18 | Tags are applied while the document is a draft; posting does not recompute them | always | N-U31-078 | DERIVATION |
| BR-U31-19 | Credit notes use refund distribution; entries choose by amount sign and tax purpose | always | N-U31-080 | DERIVATION |
| BR-U31-20 | Tags carry no sign; credit notes net by amount; the displayed sign is the rule's minus | always | N-U31-081 N-U31-059 | DERIVATION |
| BR-U31-21 | Invoice and refund distribution match in count, order, basis and percentage and total 100 percent | always | N-U31-089 | CONSTRAINT |
| BR-U31-22 | Reverse charge uses negative-factor lines and adds no base tags | reverse-charge tax | N-U31-090 | DERIVATION |
| BR-U31-23 | Tax lines of zero amount are dropped, so zero-rated sales carry base tags only | always | N-U31-084 | DERIVATION |
| BR-U31-24 | Edits of amount, tax or tags on posted lines are checked against the tax lock date and tax edits are refused | posted lines | N-U31-088 | CONSTRAINT |
| BR-U31-25 | Changing distribution tags does not change existing entries | always | N-U31-091 N-U31-106 | DERIVATION |
| BR-U31-26 | Taxes due on payment carry no tag on the invoice; tags arrive on the payment-time entry | tax due on payment | N-U31-097 | DERIVATION |
| BR-U31-27 | Payment-time and invoice-time taxes cannot share a tag on one line; mixed currencies are unsupported | always | N-U31-101 N-U31-102 | CONSTRAINT |
| BR-U31-28 | The re-tag tool refuses multi-parent child taxes and has no other gate | tool installed | N-U31-108 | CONSTRAINT |
| BR-U31-29 | The closing flag defaults true for tax-type lines on non-income, non-expense accounts and has no closing reader | always | N-U31-113 N-U31-114 | CONFIG |
| BR-U31-30 | A carry-over target needs the carry label and points to an applied-carry label | always | N-U31-120 | CONSTRAINT |
| BR-U31-31 | Report definitions are read by basic, read-only and administrator groups and changed by administrators | always | N-U31-125 | CONFIG |
| BR-U31-32 | Tags are read by internal users and changed by the full accounting group | always | N-U31-126 | CONFIG |
| BR-U31-33 | External values follow a company rule and the basic group has no access | always | N-U31-127 | CONFIG |

## REGISTER: State and Reversal

| Document or entity | State or event | Trigger | Reversal, cancel or correction path | Blocked when | Statements |
|---|---|---|---|---|---|
| Tax tag | created | tag rule saved | rename when all rules change together, or archive or delete when the last rule is deleted | deletion while used | N-U31-060 N-U31-064 N-U31-068 |
| Tax tag | archived | last rule deleted while entries carry it | a recreated rule reuses the archived tag without reactivating it (inference) | not applicable | N-U31-065 N-U31-076 |
| Tax tag | country moved or duplicated | report country changed | change the country back | not applicable | N-U31-066 |
| Journal item tags (draft document) | set or recomputed | tax synchronisation | edit taxes; tags cleared when all taxes are removed | posted document | N-U31-078 N-U31-087 |
| Journal item tags (posted) | frozen | posting | edit refused or lock-checked; re-tag only by the optional tool | tax lock date; tax edits refused | N-U31-088 N-U31-106 |
| Invoice | reversed | reverse action | credit note computed with refund distribution | lock rules | N-U31-082 N-U31-080 |
| Manual tax entry | reversed | reverse action | lines copied with tags and negated amounts | lock rules | N-U31-082 |
| Payment-time entry | created then reversed | partial reconciliation then undo | reversal in the original period or after the lock | mixed currencies | N-U31-097 N-U31-100 N-U31-102 |
| Tag re-application run | executed | administrator action | none except backup | child tax with several parents | N-U31-109 N-U31-108 |
| Report definition | deleted | deletion | none | variants exist | N-U31-010 |
| Return, period and closing | not present | not applicable | not applicable | not applicable | N-U31-122 N-U31-117 |

## REGISTER: Accounting Impact

| Event | Entries created or changed (neutral) | Tax lines, tags and accounts affected | Period, lock or date effect | Reversal effect | Statements |
|---|---|---|---|---|---|
| Post a customer invoice or vendor bill with taxes | No new entry; tag links on its lines | Base lines get base tags, tax lines get distribution tags, zero-amount tax lines are dropped | Tax lock date applies to tax-affecting entries | Credit note uses refund distribution with the same tags | N-U31-079 N-U31-084 N-U31-088 |
| Issue a credit note | Lines with opposite amounts | Same tags, refund distribution | as above | not applicable | N-U31-080 N-U31-081 |
| Manual entry with taxes | Lines tagged by amount sign and tax purpose | Invoice or refund distribution | as above | Reversal copies tags with negated amounts | N-U31-080 N-U31-082 |
| Thai withholding on a vendor bill | Tax line on a liability account with a negative percent | Income and remittance tags by payee type, no closing flag | as above | Credit note nets | N-U31-055 N-U31-052 |
| Payment of an invoice with a payment-time tax (dormant for Thailand) | Separate entry per partial payment | Tags at settlement date | Dated after the fiscal lock if needed | Undoing the reconciliation reverses it | N-U31-097 N-U31-100 N-U31-104 |
| Edit of a report formula or country | No entry | Tags renamed, created, moved or archived; reading of posted entries changes | None | None | N-U31-064 N-U31-074 N-U31-066 |
| Run of the re-tag tool | Tag links rewritten on selected entries | All tag links replaced from current distribution | Warning only for locked periods | Irreversible | N-U31-107 N-U31-109 |
| Month-end tax closing (not present) | None created | Closing flag and group accounts unused | Tax lock date manual | not applicable | N-U31-114 N-U31-115 N-U31-116 |

## Thailand VAT and withholding reporting needs versus this layer

Candidates are listed only where the statutory register verifies a need; the identifiers are cross-references. Odoo behaviour and statutory need are kept separate, and absence in the studied edition is not proof that a need does not exist.

| Need | Statutory ids | What the edition provides | Class | Candidate | Statements |
|---|---|---|---|---|---|
| Monthly VAT return figures by return box | S09-01, S09-02 | Tag definitions and a sixteen-line definition; tags on entries; nothing computes or shows figures | NATIVE GAP / EXTENSION REQUIRED | U31-F03, U31-F04 | N-U31-048 N-U31-079 N-U31-031 N-U31-033 |
| Return form output and filing data | S09-02, S09-09 | None | NATIVE GAP / EXTENSION REQUIRED | U31-F05 | N-U31-041 |
| Carry-forward of excess input tax and refund claim | S09-06 | Definition lines and carry-over fields; no routine; no closing | NATIVE GAP / EXTENSION REQUIRED | U31-F15 | N-U31-051 N-U31-119 N-U31-122 |
| Corrective return | S09-07 | Manual tax lock date only | NATIVE GAP / EXTENSION REQUIRED | U31-F15 | N-U31-116 N-U31-122 |
| Output tax and input tax books per document | S09-08, S15-01 | Tags carry no document reference; a helper query exists but only tests use it | NATIVE GAP / EXTENSION REQUIRED | U31-F07 | N-U31-040 N-U31-041 |
| Branch-level return filing | S11-04 | Foreign-VAT permission only | UNKNOWN | U31-F05 | N-U31-046 |
| Withholding returns by payee type and remittance by month | S13-04, S13-08 | Four-line definitions with tags; no evaluation or filing | NATIVE GAP / EXTENSION REQUIRED | U31-F06 | N-U31-052 N-U31-041 |
| Withholding certificate to the payee | S13-02, S13-03 | None | NATIVE GAP / EXTENSION REQUIRED | U31-F06 | N-U31-041 |
| Foreign-payee withholding return and reverse-charge VAT return | S13-04, S10-02 | No tax, tag, report or form | NATIVE GAP / EXTENSION REQUIRED | U31-F08 | N-U31-041 |
| Retention of tax documents and reports | S15-02 | Posted entries persist; no retention policy in this layer | UNKNOWN | none | N-U31-129 |

Direction of an extension (not a design): a layer that reads tax grid tags on posted entries per period and company; a display and export layer; return and carry-over records tied to the tax lock date; Thai filing data, certificates and tax books. It must respect that tags are unsigned, that credit notes net by amount sign, that history is re-tagged only by an explicit tool, and that report definitions are shared by all companies.
