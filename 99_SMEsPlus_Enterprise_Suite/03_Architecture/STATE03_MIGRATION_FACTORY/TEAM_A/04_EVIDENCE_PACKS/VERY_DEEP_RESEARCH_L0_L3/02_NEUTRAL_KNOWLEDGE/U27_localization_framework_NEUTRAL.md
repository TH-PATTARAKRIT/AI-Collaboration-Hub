# U27 Localization framework - NEUTRAL KNOWLEDGE

> Clean-room layer. Source scope: Odoo 19 Community only. Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> Unit U27. Statements are tagged with identifiers that link to the restricted evidence layer. No completeness or maturity is asserted.
> Business and process language only. Country packs other than the Thai one are future optional packs: only their packaging, dependency and extension patterns were looked at, and no country rule was studied or adopted.
> The final section is a research candidate labelled CANDIDATE — NOT APPROVED DESIGN; it is not a requirement.

## CAP-U27-01 Jurisdiction assignment of a company

### WHAT
- A company is tied to a jurisdiction through several separate settings rather than one switch: the country of its address, a separate tax-reporting country, a currency, the chart of accounts it was last loaded with, and the set of fiscal positions defined for it. [N-U27-001]
- The tax-reporting country is filled from the address country only while it is empty; once set it is an independent, editable value, so address and tax jurisdiction can differ. [N-U27-002]
- Each localization package declares the countries it serves. When a company first receives a country, or is created with one, the packages declared for that country and flagged as automatic are installed, and a default chart of accounts for the country is then loaded if the company has none. The list of selectable charts is ordered so that charts of the company's country come first. [N-U27-003]
- A partner's tax number is validated by an optional component: it infers the country from the number's prefix, normalises the number, and calls a per-country checker found by naming convention; a country without a checker is accepted. The check runs on every change of the number or the country. [N-U27-004]
- Fiscal positions are matched to a transaction automatically. A position set by hand on the partner always wins; otherwise the first automatic position of the company whose conditions all hold is used. The conditions are: tax number required, postal range, region, country and country group. Positions of a more specific company are tried before inherited ones, then by sequence. A document computes its position in the context of its own company. [N-U27-005]
- A company can hold tax registrations in other countries: a fiscal position may carry the company's own tax number for the region it maps. A document under such a position reports under that position's country instead of the company's tax-reporting country. Report tags selectable on tax distribution lines are limited to the company's own country, its registration countries and tags without country. Within a company the positions of one country must carry the same foreign tax number. [N-U27-006]
- Configuration observed in the studied database: one company with no parent; Thai chart of accounts; Thai tax-reporting country and Thai address country; Thai baht currency; due-on-payment tax option switched on; Anglo-Saxon stock accounting off; no fiscal positions; 18 taxes and 5 tax groups, all assigned to Thailand; one localization package installed (the Thai one); 188 localization packages carry the automatic-install flag and 179 package-to-country links exist, covering 157 packages. [N-U27-007]

### WHY
- Separating address, tax-reporting country and currency lets one company hold a foreign tax registration, or lets a group entity be addressed in one country and report in another, without creating a second company. [N-U27-008]

### BUSINESS RULE
- The currency, fiscal-year end, reversal-style accounting switch and due-on-payment switch of a company tree belong to its root company: branches cannot differ, and the root's currency cannot be changed once any entry exists in the tree. [N-U27-009]
- The parent of a company cannot be changed after creation; the company tree is fixed. [N-U27-010]
- A branch takes its root's chart selection (not a guess from its own country) and, when a chart is loaded, the root's currency; for a root with no entries the currency is taken from the tax-reporting country named by the chart. [N-U27-011]
- Taxes and tax groups carry a country that defaults to the company's tax-reporting country. A document may use only taxes whose country equals the document's tax country; otherwise it is rejected with a message asking the user to check the company's tax-reporting country and the taxes' countries. [N-U27-012]
- The country used to judge a tax number is the one named by the number's own prefix when present, otherwise the partner's country. [N-U27-013]

### STATE
- Jurisdiction lifecycle of a company: created without a country, then given a country (the first time only, this triggers automatic installation of the packages for that country), then given a chart, then used for entries (after which currency and price-inclusion settings are locked). Changing an existing country later triggers no installation and no chart reload. [N-U27-014]

### OPTIONALITY
- Tax number validation is an optional component. Without it the numbers are stored as typed, with only a placeholder shown; in the studied configuration the component is not installed. [N-U27-015]
- A generic chart of accounts exists in the core for companies without a matching package. It pins its own tax-reporting country (a specific non-Thai country) and switches Anglo-Saxon stock accounting on; any chart that does not state that flag has it switched off at load time. [N-U27-016]

### DEPENDENCY
- Packages and components are installed once for the whole database, and the country test for installing a country-flagged package looks at the countries of all companies together; only the configuration data they create is per company. [N-U27-017]
- A partner's tax number and country are database-wide; its fiscal position, receivable and payable accounts and payment terms are stored per company. [N-U27-018]

### CONSTRAINT
- No guard was found that prevents changing a company's tax-reporting country after entries exist, unlike currency and price-inclusion, which are guarded. This is from reading only and has not been executed. [N-U27-019]

### RISK
- Address country, tax-reporting country and currency are independent and only defaulted once, so a company can be left in an inconsistent combination; the only built-in consistency check found is on documents (taxes against tax country). [N-U27-020]
- A foreign-owned subsidiary that needs a currency different from its parent's cannot be created as a branch of that parent; it has to be a separate root company with its own chart and settings. [N-U27-021]
- The core accounting module reads a country table from the optional tax-number component at source level although it does not declare a dependency on it, so the core is not independent of that component's source. [N-U27-022]

### UNKNOWN
- Behaviour of several companies with different jurisdictions in one database while a user switches between them, and of a branch whose own tax-reporting country differs from its root's, has not been executed here and requires runtime confirmation. [N-U27-023]

## CAP-U27-02 Country-neutral accounting core boundary

### WHAT
- Without any country package the accounting core defines: the entry lifecycle and posting, the tax engine with distribution lines and report tags, fiscal positions, a configurable report engine, lock dates, numbering sequences with pattern overrides, payments and reconciliation, and hook points for electronic documents and payment QR codes. It also ships a generic chart of accounts, so it is usable on its own. [N-U27-024]
- Country-conditional behaviour found inside the core family is of four kinds: country exposed as plain data to views and rules; comparisons against specific country codes; fixed lists or tables of country codes; and country-named document formats. [N-U27-025]

### WHY
- None established in this unit.

### BUSINESS RULE
- Several extension points are explicit and documented as meant to be overridden by country packages: which invoice report to print, which partner fields are legally required to invoice, a per-company forced audit-trail flag, the suggested electronic invoice format, the list of extra electronic documents, whether a sending method is shown, and the QR eligibility, data-check and merchant-data hooks. Each default returns an empty or neutral result. [N-U27-026]
- The fiscal country code of the company is exposed as a related value on documents, orders, transfers and invoices, and a list of the fiscal country codes of the allowed companies on products, units, currencies, partners and payment terms, so that views and rules can depend on the jurisdiction without any country knowledge in the core. [N-U27-027]
- Automatic fiscal-position detection contains one hard-wired regional case: it reads the first two characters of both tax numbers and compares them with the members of a regional country group to decide an intra-regional supply. [N-U27-028]
- Literal country comparisons exist in the core: the default computation base of an early-payment discount (two countries), a default and a visibility rule for reversal-style accounting, a text block of the invoice layout, a settings block for regional distance selling, two check-printing settings, the default invoice reference standard (chosen by country prefix of the option values), and one national case in the e-invoice network module. [N-U27-029]
- Literal country lists and tables exist in the core family: lists for e-invoice network eligibility and mailing, for reversal-style accounting, for a regional chart family and for non-bank-prefix territories; a table mapping six countries to payment-reference validators; a sample-number table for 62 countries with 32 checkers in the validation component; a bank-number template table for 70 countries; and an address-scheme table for 62 countries in the shared electronic-document module. [N-U27-030]
- The shared electronic-document module is itself country-aware: it compares country codes literally about forty times across twelve files, registers seven country-named formats in the partner's format list, and contains builder components for named regional formats inside the generic package. [N-U27-031]

### STATE
- None established in this unit.

### OPTIONALITY
- None established in this unit.

### DEPENDENCY
- None established in this unit.

### CONSTRAINT
- A mechanical scan of 31 core accounting-family modules found 47 literal country comparisons (40 in the shared electronic-document module, 4 in the tax-number component, 2 in the main accounting module, 1 in the e-invoice network module), 11 literal country lists and 4 country tables. Occurrences of the fiscal-country pattern in program code are 38 in 9 core modules against 112 in 48 country packages; country conditions in views are 30 in 9 core modules against 452 in 98 country packages. These are counts of patterns, not of rules, and no country rule content was read. [N-U27-032]

### RISK
- Because of the literal comparisons, lists and a generic chart pinned to one country, the core is not strictly country-neutral; for a neutral target core these items must be moved into packages, made data-driven, or neutralised. [N-U27-033]
- Putting country-named formats and per-country branches inside the shared electronic-document module couples that module's release cycle to the countries it serves. [N-U27-034]

### UNKNOWN
- Whether every literal country branch in the core is reachable for a company with a Thai tax-reporting country has not been run; the scan is static and does not classify each branch as active or dead for Thailand. [N-U27-035]

## CAP-U27-03 Localization framework mechanisms

### WHAT
- A chart template is a named configuration bundle registered by a code. Each country package declares one or more templates through marked provider functions, and the framework discovers them by scanning the packages of the localization category, so templates of packages that are not yet installed are listed and selectable. Each entry records its name, optional parent, sequence, country, visibility and whether its package is installed. [N-U27-036]
- A template can define: default values for the company (including tax-reporting country, default accounts, bank and cash code prefixes, default taxes, and the digit width of account codes); accounts; account groups; tax groups; taxes with their distribution lines and report tags; fiscal positions; journals; and bank reconciliation models. Accounts, groups, tax groups, taxes and fiscal positions come from data tables in the package by default; a missing table is tolerated, so a template may omit any of them. Six journals (sales, purchases, miscellaneous, exchange difference, due-on-payment taxes, bank) are created by default. [N-U27-037]
- Partner identity validation is a single overridable check that receives the country and the number and returns the normalised number plus the country it was checked against; the core version does nothing and the optional component replaces it. [N-U27-038]
- The document to print for an invoice is chosen by an overridable function with a documented purpose, and the invoice title is a replaceable named block in the shared layout. Packages can also extend the document layout settings. The Thai package overrides the choice only for documents of companies whose tax-reporting country is Thailand, adds a branch label after the partner tax number, and replaces the title with an English literal that is a translatable text. [N-U27-039]
- Electronic invoice formats are registered by adding values to a partner-level selection that is empty in the core, suggested per partner by an overridable function, and resolved to a builder and to format information by further overridable functions. Extra document types register through a dictionary whose entries carry a label, an applicability test and optional help. The sending pipeline offers hooks before and after the rendered document where packages call external services. A legacy registry of formats with a unique code also exists and is extended by four packages. [N-U27-040]
- Payment QR support is registered by adding a method with a priority to a list. Each method has an eligibility message hook and a data-check hook on the bank account, and the shared EMV-style method needs a package to supply the merchant data. The Thai package plugs in through five bank-account hooks, each keyed on the bank account's country. [N-U27-041]
- A payment method declares how it may be used through an information function: whether it may be duplicated, which journal types it suits, which currencies the company needs and which country the company needs to be eligible. [N-U27-042]
- Number formats are handled by sequence patterns and a starting sequence defined per document type, a journal-level pattern override for unusual schemes, separate credit-note sequences for sale and purchase journals, and a selectable payment-reference standard whose default is chosen by country prefix; six packages override the starting sequence and seven extend the reference standards. [N-U27-043]
- A package is installed automatically when the dependencies named in its automatic-install list are installed and at least one of them is being installed now; if it is flagged with countries, at least one company in the database must belong to one of them. The country flag and the automatic flag are independent manifest attributes. [N-U27-044]
- Loading a template for a company runs: filtering for reload; writing company values and currency; loading data in a fixed model order with deferred forward references; post-load defaults (utility accounts, suspense and cash-difference accounts on bank and cash journals, default journals, default taxes on the company and on existing products that already had a tax elsewhere, per-company property defaults, bank reconciliation accounts); translations; account-group parent synchronisation; optional demo data; and finally the same template for each branch. [N-U27-045]

### WHY
- None established in this unit.

### BUSINESS RULE
- Template data is described as records keyed by external identifiers and references between records are written as identifiers resolved at load time; relations whose target is created later are postponed. Models load in a fixed order: account groups, accounts, fiscal positions, tax groups, taxes, journals, reconciliation models. [N-U27-046]
- A template may name a parent. Providers and data tables of the parent chain are merged first, and child values override parent values by identifier. The family mechanism is used by regional chart families and by territories of one country; providers of one package are reached from another through ordinary method inheritance. [N-U27-047]
- Only a system administrator can load a chart template. [N-U27-048]
- Selecting a template whose package is not installed installs the package first and then continues loading; if no company country is set, the template's country becomes the company country. [N-U27-049]
- Loading targets one company at a time: the company is the only allowed company, the language is fixed to English, and tracking is off. A branch receives only the company-level values and reuses the records of its root; branches of a loaded company are loaded in turn. [N-U27-050]
- Selecting the company's current template again is a reload that preserves user data: property defaults and reconciliation models are not reapplied, existing journals, account groups and accounts are kept (for accounts only tags are updated), a changed tax is retired by renaming it with an old label and a new one is created, and an unchanged tax only gets its position links and report tags refreshed. [N-U27-051]
- A flag lets an update touch only existing records and skip anything that would be created. [N-U27-052]
- Records created by a template are registered under the core's own namespace with the company identifier in the name, and are marked as not to be overwritten by later package updates; they are therefore not owned by the country package. [N-U27-053]
- Fields in template data that do not exist on the target model are silently dropped unless a checking mode is on. [N-U27-054]
- Report tags are named in template data and resolved by name and country against existing tags; tags are unique per name, applicability and country, and they are created from the tag-based expressions of reports, scoped to the report's country. A missing tag stops loading with a prompt to update the package first. [N-U27-055]
- A report is available under one of three conditions: always, when the company's country matches, or when the company's chart matches; a report conditioned on country must name its country. The Thai package contributes three reports, each conditioned on Thailand; the core contributes three. [N-U27-056]

### STATE
- Template states per company: no chart; chart loaded by one template; reload of the same template (user data kept); different template requested (earlier template records removed only if the tree has no entries); package uninstalled (company chart selection cleared, loaded records kept). [N-U27-057]

### OPTIONALITY
- Demo data is optional and is loaded only after the first template of a company; an error in demo loading is logged and does not undo the chart. [N-U27-058]

### DEPENDENCY
- Loading a template that uses report tags depends on the package's report data having created the tags first; a stale package therefore cannot load newer template data. [N-U27-059]

### CONSTRAINT
- Requesting a different template removes the previous template's records and entries only when the company tree has no entries; once entries exist, the company currency and the price-inclusion setting can no longer be changed, and currency assignment during loading is skipped. [N-U27-060]

### RISK
- A reload keeps old and new taxes side by side under renamed labels, which can leave duplicate-looking taxes in a company that has posted documents. [N-U27-061]
- Silently dropped unknown fields mean a package can load without error while parts of its configuration are ignored. [N-U27-062]

### UNKNOWN
- Runtime behaviour of reload, template switching with demo, and external-service hooks (before and after rendering) has not been executed and requires runtime confirmation. [N-U27-063]

## CAP-U27-04 Country pack lifecycle

### WHAT
- A country package is installed in one of three ways: by a user, automatically when its dependencies and country condition hold, or because a chart of its country was selected. On installation of a package that hosts templates, the first template matching the current company's country (or the generic one) is loaded on the current company only if that company has no chart yet; the loading is postponed until the system registry is ready. The Thai package is automatic with respect to the accounting core and is flagged for Thailand. [N-U27-064]
- Packages may declare an after-install step, a before-install step and an uninstall step. The Thai package has only an after-install step that marks its report tags as not to be overwritten, to keep tags that existed before an upgrade. Of the 227 other packages, 30 have an after-install step, 14 an uninstall step and 2 a before-install step; one before-install step creates columns and backfills them directly in the database for performance. [N-U27-065]
- Some after-install steps scope their effect to the companies of the package's jurisdiction, by company country or by the loaded chart code, and some document packages add their own fields onto already loaded taxes of root companies whose chart matches the base package. [N-U27-066]
- Uninstalling a package that hosts templates clears the chart selection of every company that used one of its templates but does not delete the records the loader created. Thirteen document packages clear stored per-company format selections on uninstall; one regional tax package deletes the external identifiers of its tax groups and accounts on uninstall, which detaches them from the package so they survive. Values that a package adds to selection lists carry a fallback rule applied on uninstall (21 packages declare such rules; the Thai package does so for its three payment-QR key types). [N-U27-067]
- Updates of template data on upgrade are delivered as version-keyed end-of-migration scripts: 41 of the 227 packages have migrations (83 scripts), 38 scripts call the loader and 31 of those with creation switched off; they iterate the companies that use the package's chart, roots before branches. A separate optional core module can re-tag existing entries after report changes. The Thai package has no migrations. [N-U27-068]
- Packages carry a version in the manifest (175 of 227 declare one); the Thai package is at version 2.0 and the database stores its version with the platform prefix. [N-U27-069]
- A package may ship a demo company of its country; the Thai package does, and demo data is not loaded in the studied database. Thai template data comprises 144 accounts, 18 taxes and 5 tax groups and no fiscal positions. [N-U27-070]
- When translation terms of the core module are loaded, the chart and tax-tag translations are reloaded for the loaded languages. [N-U27-071]
- In the studied database the Thai package seeds no access rights, no record rules, no groups, no scheduled jobs and no automation rules; it seeds three reports, one print action and three views. It ships two data files and one demo file and has no security files. [N-U27-072]
- A recount of all 227 other packages agrees with the supplied profile for dependency counts, automatic-install flags, hook flags and data file counts. Of them, 186 are automatic (129 conditional on the core, 57 unconditional), 41 are not, 155 name countries, 26 name countries but are not automatic, and all are under the same open licence. [N-U27-073]
- Samples read for manifest, dependencies and hook entry points only: a base package of a European country (automatic, after-install step, layout dependency); a base package of an Asian country (large data set, formula-tax and debit-note dependencies, loader overrides); a base package of a Latin American country (depends on two regional frameworks, loader overrides, no hooks); a regional tax package (no country, no automatic flag, uninstall step); a document package that depends on a base package and installs with it; a second document package with before-install, after-install and uninstall steps; a point-of-sale bridge that depends on its base package; and the Thai reference package. [N-U27-074]

### WHY
- None established in this unit.

### BUSINESS RULE
- None established in this unit.

### STATE
- None established in this unit.

### OPTIONALITY
- Hooks, demo data, migrations, automatic installation and country flags are all optional manifest attributes; a package may use any subset. [N-U27-077]

### DEPENDENCY
- None established in this unit.

### CONSTRAINT
- None established in this unit.

### RISK
- After-install steps of single-country packages can act database-wide: activating a feature group for all users, enabling a rounding feature for all companies, activating a language, or setting an identification type on every partner. Installing one package can therefore change behaviour for companies of other jurisdictions. [N-U27-075]
- Loaded records survive package removal and the company chart selection is cleared, so a later reinstall treats the company as having no chart even though the earlier records exist. [N-U27-076]

### UNKNOWN
- The effect of reinstalling after uninstall, behaviour when a package is upgraded while companies have posted entries, and the exact effect of the Thai after-install step on existing tags have not been executed and require runtime confirmation. [N-U27-078]

## CAP-U27-05 Extension boundary taxonomy of packs

### WHAT
- Packages fall into these archetypes by mechanical facts (dependencies, category, hosted templates): chart packages that host templates (125 in the localization chart category, 115 with a template provider of their own); document or electronic-invoice packages; point-of-sale bridges; stock, sale, purchase or website bridges; time-off packages; layout and regional-framework packages; and small extensions. A recount gives 125 chart, 34 electronic-document, 24 point-of-sale, 24 bridge, 4 time-off or expense-layout and 16 other, against the supplied heuristic of 116, 34, 17, 16, 5 and 39. [N-U27-079]
- Packages cluster into regional families: one family root hosts templates and many country packages declare children (17 depend on one regional family root which hosts two templates; one European family host hosts seven templates with six dependent stub packages that have no models); layout packages (8 dependents) and regional frameworks for Latin America (7 and 6 dependents) are shared by several countries. 135 of the 227 packages depend on another localization package and 92 do not. [N-U27-080]
- The Thai reference package consists of five model extensions (template provider, partner branch label, document choice, print pre-check and bank-account QR hooks), data tables for 144 accounts, 18 taxes and 5 tax groups, three reports and one invoice layout; it adds no fiscal positions, groups, access rights or scheduled jobs. Its content is studied in the Thai localization unit. [N-U27-085]

### WHY
- None established in this unit.

### BUSINESS RULE
- Core models most extended by country packages (counts of packages): the chart loader 128, the journal entry 87, the company 69, the partner 65, the settings 37, the tax 35, the journal 30, the sending wizard 24, the entry line 18, the product template 15, point-of-sale configuration 14 and orders 14. The most frequent method overrides are the posting step and the invoice-report choice (15 each), the extra-document dictionary (15), partner commercial fields (13), sending alerts (13) and reset-to-draft (12). [N-U27-081]

### STATE
- None established in this unit.

### OPTIONALITY
- None established in this unit.

### DEPENDENCY
- A regional framework can publish an explicit contract for packages that build on it: the Latin American document framework states in its own description that a dependent package must extend one company method to declare that it uses government document types and must supply document-type data with a country field. [N-U27-084]

### CONSTRAINT
- Of the 227 packages, 210 extend at least one model, 86 distinct models are extended, 14 models are extended by ten or more packages and 26 by five or more; 176 packages extend at least one accounting model counting the loader and 104 excluding it. [N-U27-082]
- The supplied heuristic profile is corrected on three points: its template-file column does not measure template data tables (10 against 125); its payroll category includes two Croatian chart packages that merely start with the letters hr, so only three time-off packages exist and no payroll package; and its count of 119 packages extending core accounting models could not be reproduced (176 or 104 depending on definition). [N-U27-083]

### RISK
- None established in this unit.

### UNKNOWN
- Archetype assignment is mechanical; package intent for borderline packages (for example the layout and expense-layout packages) is not established from manifests alone. [N-U27-086]

## CAP-U27-06 Multi-jurisdiction coexistence in one database

### WHAT
- Within one database each root company has its own taxes, tax groups, fiscal positions and journals (and therefore sequences), visible only to that company and its branches; sibling roots do not see each other's records. Tax names must be unique per type, scope and country within a root tree, so two jurisdictions inside one tree can reuse a name only with different countries. Choosing a chart in settings loads it only for the currently active company. [N-U27-087]
- An account can belong to several companies, which is how a chart can be shared; the account code is stored per root company, so branches share codes while different roots may code the same account differently; a cash account cannot belong to more than one company. [N-U27-088]
- The effective lock date of a company is the latest of its own and its ancestors' lock dates, with user exceptions evaluated per ancestor; the hard lock date likewise; a parent's lock therefore binds its branches. [N-U27-089]
- Cross-company documents are partly supported: an inter-company payment bridge (installed in the studied database) lets a payment in one company settle invoices of another through clearing journals configured per company. No other inter-company automation module was found in this unit's scope. [N-U27-090]
- A facility creates the taxes of another country's template inside an existing company, using substitute accounts derived from the company's own chart and no position mappings; it is limited to accounting managers and installs the other country's package if needed. [N-U27-091]
- Inside one pack, behaviour may be keyed on three different countries: the company's tax-reporting country (invoice document choice), the partner's own country (branch label) or the bank account's country (QR checks and print action domain). In a multi-jurisdiction database these three keys can disagree for a single transaction. [N-U27-092]
- Company-structure cases: a foreign-owned Thai subsidiary is a separate root company with its own Thai chart, Thai tax-reporting country and baht currency, because it cannot share a different-currency parent as a branch; a Thai branch of a Thai company may be a branch company sharing the root's chart, taxes and currency, and inherits the root's lock dates; the Thai branch concept of the Thai package is only a label derived from the partner's company registry value, not a company; a representative or regional office has no dedicated concept and would be a company (root or branch) or only a partner. Group structure details are in the company-structure unit. [N-U27-093]
- Installed packages, activated languages and feature groups are database-wide: after-install steps and installed formats act for all companies regardless of jurisdiction. [N-U27-094]

### WHY
- None established in this unit.

### BUSINESS RULE
- None established in this unit.

### STATE
- None established in this unit.

### OPTIONALITY
- None established in this unit.

### DEPENDENCY
- None established in this unit.

### CONSTRAINT
- None established in this unit.

### RISK
- Mixed keys, database-wide installation side effects and one shared posting path overridden by several packages mean a package must guard every behaviour by the jurisdiction of the transacting company; a mechanical lint finds that of 15 posting overrides, 7 test a country or chart condition, 6 test another package flag and 2 test nothing. [N-U27-095]
- Putting a different-jurisdiction subsidiary under a parent as a branch would make it inherit the parent's lock dates, chart and currency. [N-U27-096]

### UNKNOWN
- Cross-root consolidation of reports for a group of companies with different charts is not established from Community source in this unit; no multi-company transactions exist in the studied database, so every coexistence behaviour here is from reading only and needs runtime confirmation. [N-U27-097]

## CAP-U27-07 Gaps and design-relevant observations

### WHAT
- None established in this unit.

### WHY
- None established in this unit.

### BUSINESS RULE
- None established in this unit.

### STATE
- None established in this unit.

### OPTIONALITY
- Clean extension points exist and are used: the fiscal-position condition list can be extended by appending validators; the document choice, the forced audit-trail flag, the electronic-format selection and suggestion, the extra-document dictionary, the QR hooks and the regional document framework's company method are all designed to be overridden. [N-U27-103]

### DEPENDENCY
- None established in this unit.

### CONSTRAINT
- None established in this unit.

### RISK
- Country knowledge sits in the core: literal comparisons, country lists and a generic chart pinned to one country (see the core boundary capability). A neutral core should keep these in packages or in data. [N-U27-098]
- Packages override loader internals rather than a declared contract: after-load step in seven packages, load step in five, utility bank accounts in four, bank-fees account in three, tag dereferencing in two, accounts data in two and the public entry in one. Such overrides tie packages to loader structure. [N-U27-099]
- Country knowledge is duplicated between files: a comment in the core asks to keep country lists aligned with another module's manifest. [N-U27-100]
- Which chart a company receives when its country has no package depends on registry order, because the sort key for a missing country compares a display name with a code and cannot prefer the generic chart. [N-U27-101]
- Several packages override the same posting method and the same document-choice method; the guard of each depends on that package's own conditions. [N-U27-102]

### UNKNOWN
- These observations are from reading source and mechanical scans of the Community modules only; none was confirmed by execution. [N-U27-104]

## CAP-U27-07 (continued) CANDIDATE — NOT APPROVED DESIGN: neutral architecture sketch

The sketch below proposes a Country-Neutral Accounting Core, a Localization Framework and Optional Country Packs. It is written without vendor structure, derived from the observations of this unit, and is not a requirement and not approved.

### WHAT
- CANDIDATE — NOT APPROVED DESIGN. Three layers: a Country-Neutral Accounting Core that knows no country and exposes contracts; a Localization Framework that owns the registry of jurisdictions and packs, the configuration-loading contract and the lifecycle; and optional Country Packs, of which the Thai pack is the first and the reference. Packs depend only on the framework contracts, never on each other except through declared regional families. [N-U27-105]
- CANDIDATE — NOT APPROVED DESIGN. Company-to-jurisdiction assignment: every legal or accounting entity has exactly one jurisdiction profile (tax-reporting country, functional currency, calendar and language defaults, active pack set, chart selection). Address country remains data and does not drive behaviour. A branch inherits the profile of its entity and cannot override it; a separate legal entity, such as a foreign-owned Thai subsidiary, gets its own profile. Additional registrations in other countries are modelled as registrations of the same entity, not as profile changes. [N-U27-106]
- CANDIDATE — NOT APPROVED DESIGN. Contracts a pack may implement, each optional: configuration bundle (accounts, tax groups, taxes with distribution lines and tags, fiscal positions, journals, defaults); tax report and tag registration; party identity validation; document selection, title and layout; electronic document format registration; payment method and QR registration; numbering convention; regional framework contracts. Every contract states its default behaviour in the core and the context it receives, which always includes the transacting entity's jurisdiction profile. [N-U27-107]
- CANDIDATE — NOT APPROVED DESIGN. Pack lifecycle: register; install into the database (no effect on any entity); assign to an entity's jurisdiction profile (loads configuration for that entity only); upgrade (versioned configuration changes delivered as reviewed migrations); deactivate for an entity; uninstall (configuration data is retained and detached, never deleted once entries exist). Install steps may not change settings of entities outside the pack's jurisdiction. [N-U27-108]
- CANDIDATE — NOT APPROVED DESIGN. Entity-structure cases: a foreign-owned Thai subsidiary is a separate entity with its own profile; a Thai branch is a branch of the same entity and carries a branch code on its documents; a representative or regional office is left open for the company-structure unit and could be a branch or a separate entity depending on its legal status. [N-U27-113]
- CANDIDATE — NOT APPROVED DESIGN. Traceability to this unit's observations: the contract surface follows the clean extension points that exist today; moving country knowledge out of the core answers the coupling observations; scoping install effects to the pack's jurisdiction answers the database-wide side effects; the lock rule and the conformance checks answer the posting-override and reload risks. [N-U27-114]

### WHY
- CANDIDATE — NOT APPROVED DESIGN. Purpose: each legal or accounting entity must be able to use the accounting jurisdiction that applies to it, including a Thai entity beside entities of other jurisdictions, without the core carrying any country knowledge and without one pack altering another pack's results. [N-U27-109]

### BUSINESS RULE
- CANDIDATE — NOT APPROVED DESIGN. Rules proposed: behaviour is selected by the jurisdiction of the transacting entity, not by the partner's or bank's country; a jurisdiction profile is locked after the first posted entry except through a governed change; configuration reload preserves user data and retires changed items instead of editing them in place; an entity without a matching pack runs on a neutral default pack with no country pinned; the default language is English with Thai as a translation layer of stable keys. [N-U27-115]

### STATE
- CANDIDATE — NOT APPROVED DESIGN. States proposed: a jurisdiction profile is draft, then active (configuration loaded), then locked at the first posted entry, with a governed change path afterwards; a pack for an entity is not assigned, assigned, active or deactivated; a pack in the database is registered, installed or uninstalled. [N-U27-110]

### OPTIONALITY
- CANDIDATE — NOT APPROVED DESIGN. Every contract, every pack and every regional family is optional. An entity without a pack runs on a neutral default. The Thai pack would supply the Thai chart, tax set, tax reports, invoice layout and payment QR support, with English as the default text and Thai as a translation layer. [N-U27-111]

### DEPENDENCY
- CANDIDATE — NOT APPROVED DESIGN. Dependency rules proposed: the core knows nothing of packs; the framework depends only on the core; a pack depends on the framework contracts and optionally on a declared regional family; a document or point-of-sale extension depends on the base pack of the same jurisdiction. [N-U27-112]

### CONSTRAINT
- CANDIDATE — NOT APPROVED DESIGN. Conformance checks proposed for any pack: no hidden global side effects at install; every override guarded by the entity's jurisdiction; configuration bundle loads, reloads and upgrades idempotently on a database with entries; two packs of different jurisdictions coexist in one database without changing each other's results. [N-U27-116]

### RISK
- CANDIDATE — NOT APPROVED DESIGN. Risks and open questions: whether tax-reporting country can ever change for an entity and how; how group-level reports handle entities with different charts; how regional families share data without hidden inheritance; and what governs electronic-document packs that depend on external services. [N-U27-117]

### UNKNOWN
- CANDIDATE — NOT APPROVED DESIGN. This sketch is a research candidate derived from observations in this unit; it is not a requirement, is not approved, and has not been validated against the Thai statutory scope. [N-U27-118]
