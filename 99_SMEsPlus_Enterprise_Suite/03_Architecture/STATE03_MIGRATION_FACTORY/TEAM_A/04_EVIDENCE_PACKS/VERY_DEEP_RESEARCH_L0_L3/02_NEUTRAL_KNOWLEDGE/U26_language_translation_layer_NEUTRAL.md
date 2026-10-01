# U26 Language and translation layer - NEUTRAL KNOWLEDGE

> Clean-room layer. Source scope: Odoo 19 Community only. Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> Unit U26. Statements carry identifiers that link to the restricted evidence layer. No completeness or maturity is asserted.
> Business and process language only; the restored database was used for configuration facts, never for transactions or translation text.
> The programme's own design constraint (English canonical, Thai as a translation layer, no hard-coded Thai interface text) is used only as the comparison frame; nothing here is a requirement.

## CAP-U26-01 Language master and activation

### WHAT
- The system keeps a catalogue of languages. Each entry carries a locale code, a display name, a short code used in web addresses, a text direction, a date pattern, a time pattern, a first day of the week, a digit-grouping style, a decimal separator and a thousands separator. Only languages flagged active can be used for users, contacts, documents and websites. [N-U26-001]
- The date pattern is chosen from a fixed list of nine day, month and year orderings using slash, dash or dot separators; the time pattern is either a 24-hour or a 12-hour clock with AM or PM; the week may start on any of the seven days; digit grouping is either international (groups of three) or Indian (three then two). All of these are Gregorian-calendar numeric patterns; the language entry has no field for an alternative calendar era. [N-U26-002]
- The product ships a catalogue of 93 languages. In the studied configuration exactly one language, the base language English, is active. Thai is present in the catalogue but inactive; its entry uses day-month-year with slashes, a 24-hour clock, Sunday as first day, international grouping, a dot as decimal separator and a comma as thousands separator. [N-U26-003]

### WHY
- Language data is cached and kept independent of other records and of the caller's context so that every formatted number, date and screen can read it cheaply and consistently; this is why only a small fixed set of locale fields exists on the language entry, and why date and time patterns are limited to directives that behave the same on every operating system. [N-U26-104]

### BUSINESS RULE
- Activating a language from the language list or from the install wizard loads the translation files of every installed module for that language. The install wizard offers an overwrite option that is on by default and replaces customised translations with the shipped ones. [N-U26-004]
- A language name, locale code and web-address short code must each be unique; the locale code cannot be changed after creation; at least one language must remain active; date and time patterns containing unsupported directives are rejected; mixing a 24-hour directive with AM or PM is silently converted to a 12-hour pattern with a notification. [N-U26-005]
- A language cannot be deactivated while any active or archived user, any active contact or any website uses it. Deactivating a language also removes it as the stored default language for new contacts. [N-U26-006]
- The base language English can never be deleted, an active language cannot be deleted, and the language of the current user context cannot be deleted. [N-U26-007]

### STATE
- A language moves from inactive to active when activated (translations are then loaded) and back to inactive only if no user, contact or website depends on it; deletion is allowed only from the inactive state and never for the base language. [N-U26-008]

### OPTIONALITY
- At database creation the first requested language, or English when none is requested, is activated and becomes the stored default language for new contacts and the language of the main company contact. If the requested language is not in the catalogue it is created from the host operating system locale information, falling back to the host default locale with a warning. In the studied configuration the default is English and every contact and user is set to English. [N-U26-009]

### DEPENDENCY
- The language used for a user session is resolved in order: the language stored on the user if active, else the language of the browser request, else the language of the main company contact, else English, else the first active language. A request with an unknown language is corrected to the same fallback chain before access is checked. [N-U26-010]
- A contact has a language chosen from the active languages. A new contact takes its parent's language when it has one, otherwise the stored default, otherwise the environment language. The language is described as the language of all emails and documents sent to that contact. [N-U26-011]

### CONSTRAINT
- Only administrators may create, change or delete languages and run the language install wizard; internal, portal and public users may read the catalogue. The language menus are visible only in developer mode, and the general settings screen offers add-language and manage-language entries. [N-U26-012]
- Active-language data used for formatting is held in a cache that is cleared whenever a language is created, changed or deleted; asking for the data of an inactive language returns an empty placeholder instead of an error, while formatting with an uninstalled language raises an error. [N-U26-013]

### RISK
- Locale behaviour is limited to the knobs on the language entry; there is no calendar-era setting, no per-language sorting rule and no per-language numeral system on the server. A language activated by hand with an empty translation set silently shows English text. [N-U26-014]

### UNKNOWN
- How the language list behaves when 93 catalogue entries are activated together at scale, and the exact host-locale data used when a language is created outside the catalogue, require running the system. [N-U26-015]

## CAP-U26-02 Translatable source strings (code-level terms)

### WHAT
- Terms written in program code are translated by looking up the English source sentence itself. There is no symbolic key: the English text is the identifier, and a translation is stored as a pair of English sentence and target sentence, grouped by the module that owns the code and by the target language. This is the central finding for the language architecture. [N-U26-016]
- Server code marks a user-facing term by passing the English sentence to a translation function (immediate or lazy), or by calling the same function on the request environment. Client-side code does the same with its own function. A lazy form defers the lookup so that module-level constants can be translated later in the language of the moment. [N-U26-017]

### WHY
- The module is used as a context so that the same English word with different meanings in different applications can have different translations; the lazy form exists so that terms declared early in code, such as module-level constants, can be found by the extraction tool and translated later in the language of the moment. [N-U26-105]

### BUSINESS RULE
- English is the identity language: when the active language is English the sentence is returned unchanged and no translation file is consulted. For any other language the lookup is a plain match of the English sentence against the module's translation pairs; when no pair matches the English sentence is returned. [N-U26-018]
- The owning module is detected automatically from where the call is made. The same English sentence can therefore have different translations in different modules, but one module can hold only one translation per English sentence; two meanings of the same sentence inside one module cannot be told apart. On the client, a lookup first tries the module and then falls back to any module. [N-U26-019]
- The language for a lookup is taken from the context of the call, then from the environment, then from the web request, then from the language of the current user, then from an optional default given to the lazy form; if none is found the term is returned untranslated and a warning is logged. [N-U26-020]
- Placeholders are positional or named substitutions applied after the lookup. Markup values force the sentence to be escaped, lazy terms passed as values are translated in the target language, and list values are rendered as a language-aware enumeration. A translation whose placeholders do not fit the arguments is rejected: an error is logged and the English sentence is used instead. [N-U26-021]
- There is no plural function and no context argument: only the single-sentence form is extracted and looked up. Plural-dependent sentences are written as separate English sentences, and the translation files carry an empty plural rule in exported files. [N-U26-022]

### STATE
- Code translations live in the translation files shipped with each module and are read directly from those files into process memory per module and language; they are not stored in the database. Language files are read in order of base language then regional language, and from the standard translation folder and an extra folder. Python and client-side terms are kept in separate pools identified by a comment in the file. [N-U26-023]

### OPTIONALITY
- The export tool discovers terms by scanning source files: server code for the translation function and the lazy form, client code for its function, client templates, and spreadsheet data files, limited to installed modules. Only sentences that contain at least one letter are exported. [N-U26-024]

### DEPENDENCY
- Accounting master data created from a chart template is loaded in English and then translated with the same sentence-matching mechanism, using the translation pairs of the module that defined the template, trying the regional language and then the generic language. [N-U26-025]

### CONSTRAINT
- A translated sentence may not contain a literal escaped line break; lazy terms cannot be compared, hashed or sorted; one module cannot hold two translations of the same sentence; only the first source reference of a code entry is kept when a translation file is read. [N-U26-106]

### RISK
- Because the English sentence is the key, editing an English wording silently orphans every existing translation of it; a typo fix in English breaks all other languages until they are re-translated. Colliding meanings inside one module cannot be separated. Any design that needs stable keys must add them as a separate layer. [N-U26-026]

### UNKNOWN
- Performance of the in-memory translation pools for many languages and modules, and the exact behaviour of fallback when a regional language file is partially translated, need execution to confirm. [N-U26-027]

## CAP-U26-03 Translatable data on records

### WHAT
- A field can be declared translatable. Its stored value is then a single structured value holding one text per language, always including the English text, instead of a plain text. Reading returns the text of the reader's language and, when that language has no stored text, the English text. [N-U26-028]
- Two translation granularities exist: whole-value translation for short names and labels, and term-level translation for rich text and screen definitions, where the value is split into sentences or fragments and each fragment is translated separately inside the structure of the text. [N-U26-029]
- Translatable master data covers product names and sales, purchase and picking descriptions; unit of measure names; tax names, labels, descriptions and legal notes; tax group names; payment term names and notes; fiscal position names and notes; journal and journal group names; ledger account names and descriptions; account tag names; report and report line names; cash rounding, reconciliation model and payment method names; incoterm names; operation type, route and rule names; removal strategy names; scrap reason tags; pricing list, tag and attribute names; company header, footer and invoice terms; country names and tax-identifier labels; currency unit labels; screen, menu, action and report titles. Contact names, warehouse names, location names, product category names, country subdivision names and the free text of sales and purchase documents are not translatable. [N-U26-034]

### WHY
- The English text is always kept as a meaningful base value, even when English is not an active language, because it is the fallback for every other language and the source text exported to translators. [N-U26-107]

### BUSINESS RULE
- Writing a whole-value translatable field in a language stores only that language's text; the English text is changed only when the writer works in English. If English is not an active language the English slot is always written too. Writing a term-level field in a language re-aligns the fragments of all other languages with the new structure. [N-U26-030]
- Translations of a record are edited per language through a translation dialog that shows one line per language or per fragment. Editing needs write permission on the record and on the field. Setting a translation to empty removes it and the field falls back to English. [N-U26-031]
- Searching and sorting on a translatable field use the reader's language with fallback to English at query time. For large tables a trigram index prefilter looks across all stored languages and then the language-specific condition is applied. [N-U26-032]
- Record translations can be exported for a chosen model and filter, in PO, CSV or archive form. A record without a stable external identifier gets one created on export, and the identifier plus the field name is what later identifies the target of an import. [N-U26-033]
- Document lines copy product text into a plain, non-translatable description at the time the line is created, in the language of the document partner. Later translations of the product do not change existing lines. [N-U26-035]

### STATE
- In the studied configuration 357 stored fields across 179 models are translatable; every stored value in them carries only the English text, because no other language is active. No stored translation of any other language exists in any translatable column. [N-U26-037]

### OPTIONALITY
- Translatability is chosen field by field and at two granularities (whole value or term level); a model can opt out of translation export entirely; in the studied configuration translation is declared on 357 stored fields but used for only one language. [N-U26-108]

### DEPENDENCY
- Accounting master data created from a chart template (ledger accounts, taxes, tax groups, journals, fiscal positions, reconciliation models) is created in English and then receives its translations from the template's own per-language columns or from the module translation files, matched through the record identifier and the field name. A short journal code, although not translatable, is translated into the company language at load time. [N-U26-036]

### CONSTRAINT
- A stored translatable field cannot depend on the language of the context, and a stored related translatable field is not computed correctly for all languages; term-level translated values must keep the same number of fragments when edited. [N-U26-038]

### RISK
- The identifier of a translated value is the record identifier plus field name; the English text is the fallback and the only guaranteed value. A record whose English text is edited keeps its other-language text for whole-value fields but may lose fragment translations for term-level fields when fragments change. [N-U26-039]

### UNKNOWN
- How term-level translations behave after bulk edits of English rich text and how long the trigram-assisted search takes on large product catalogues require execution. [N-U26-040]

## CAP-U26-04 Translation files, import and export

### WHAT
- Each module may ship translation files in a standard folder: one template file (all English terms, no translations) and one file per language. Across the 692 Community modules, 607 have such a folder, 606 have a template, 406 ship a Thai file and none ships a file named for the Thai regional variant. The Thai file is named for the generic language and therefore applies to the regional Thai language through the base-language rule. [N-U26-041]
- Of the 356 installed modules in the studied configuration, 310 ship a Thai file; the 46 without one are test, theme, bridge and technical modules. Across all 406 Thai files there are 64,199 entries of which 52,873 have a non-empty translation. The Thai file of the Thai accounting localization has only 23 entries; the localization's chart of accounts is translated through per-language columns in its data files instead. [N-U26-042]

### WHY
- Translations from many files are collected and written in one pass because per-file writing would be too slow; the template file is merged into each language file when reading so that source comments stay correct even when the language file is stale. [N-U26-109]

### BUSINESS RULE
- Translations are loaded when a language is activated, when a module is installed or updated, and when a database is created with a language. Loading takes every installed module in dependency order, reads its translation files for each active language (generic language first, then regional) and its data files for embedded per-language columns, and writes them at the end in one pass. [N-U26-043]
- Overwrite rules: a record flagged as not-updatable keeps its existing translations unless a forced overwrite is requested; a normal record is overwritten only when overwrite is requested. Module update overwrites only when the operator asks for it on the command line, and that option is refused without the update option. The language install wizard and the file import wizard both default to overwrite on, the command-line import defaults per its own flag. [N-U26-044]
- On loading, empty translations are ignored, code-level entries are ignored by the database import (they are read from the files at run time), obsolete entries and two deprecated reference kinds are skipped with a log line, and entries for models or fields that no longer exist or are not translatable are dropped. Terms with no translation fall back to the English text. [N-U26-045]
- The export wizard produces a template or a language file for chosen modules or for chosen records of one model, as PO, CSV or an archive of per-module files. A command-line tool imports and exports the same files and can load languages. Exported entries carry the source reference, the owning module and the English text; entries without alphabetic characters are left out. [N-U26-046]

### STATE
- The studied database has no stored non-English translation, no active non-English language, and the list of code translations kept by the external-service module is empty. [N-U26-050]

### OPTIONALITY
- Overwrite of existing translations is optional and off by default for module update; an extra translation folder is optional; the external-service module and its weekly job are optional; export may be limited to chosen modules or to chosen records of one model. [N-U26-110]

### DEPENDENCY
- Several modules extend loading: the accounting module reloads chart-of-accounts and tax tag translations after the language files; the website module copies generic page translations to website-specific page copies; the e-commerce module copies checkout-step translations; the data-module import module reads translation files attached to imported modules. [N-U26-049]

### CONSTRAINT
- Permissions: importing a language file and installing a language are limited to administrators; the export wizard is available to every internal user; the translation menus appear only in developer mode. A weekly scheduled job refreshes a read-only list of code translations used to propose edits on an external translation service; that list is readable only by administrators. [N-U26-047]
- An import with a wrong or malformed file raises a user error naming the file and the technical cause and is rolled back; an unknown language code on import creates the language first; an unreadable file during module loading is logged and skipped. [N-U26-048]

### RISK
- A translation file keyed by English sentences must be regenerated after any English wording change; overwrite-on-update can erase customised translations on non-protected records; the export wizard being open to all internal users exposes the full term catalogue and any record translations the user can read. [N-U26-051]

### UNKNOWN
- Load time with all 406 Thai files, memory footprint of in-process code translations, and the actual effect of overwrite on customised records require running the system. [N-U26-052]

## CAP-U26-05 Per-user, per-partner and per-template language

### WHAT
- Every user has a preferred language, stored on the user's contact record, that the user can change in their own preferences. It drives the interface language and the language of everything the user reads that is not tied to a document partner. If the stored language is not active the session falls back to the request language, the company language, English or any active language. [N-U26-053]
- Every contact has a language that is described as the language for all emails and documents sent to it. New contacts take it from their parent or from the stored default; it is editable only among active languages. Documents and emails for a customer or vendor are therefore produced in the contact's language, not in the language of the staff member who triggers them. [N-U26-054]

### WHY
- Before any session exists the login page can only use the language of the browser, so a lightweight path loads just the generic language file for it; after login the stored preference takes over. [N-U26-111]

### BUSINESS RULE
- When a sales, purchase, invoice or stock line is created from a product, the product description is rendered in the language of the document partner (public customers fall back to the staff language) and then frozen as plain text on the line. Printed lines show the frozen text, while product names shown through a translated-name helper are recomputed in the document language. [N-U26-055]
- An email template has an optional language expression. When set it is evaluated per record (for example the recipient's language); when empty the first customer partner's language is used. The template is then rendered once per distinct language, with its subject, body and name taken from the translated values; a preview language can force a language. [N-U26-056]
- Sending an invoice by email proposes a language computed from the template; the staff member can change it in the send wizard, and the body, subject, recipients and the model description in the message are regenerated in the chosen language. Purchase orders and quotations by email use the template language or the context language the same way. [N-U26-057]
- Portal and website visitors get a language from the address prefix, then a remembered cookie, then the context language, then the website default; non-default languages add a prefix to the address, a browser-language redirect can be switched on, and only the languages ticked on the website are offered. Logged-in portal users read in their stored preference, and the invitation email is rendered in the invited user's language. [N-U26-058]

### STATE
- A contact's language is always set (computed from parent or default) and always one of the active languages; a language becomes locked against deactivation as soon as any contact, user or website uses it. [N-U26-112]

### OPTIONALITY
- Website language selection exists only when the website module is installed; browser-language redirect is a per-website switch that is on by default. In the studied configuration there are 29 websites, each offering only English, and no contact or user uses another language. [N-U26-060]

### DEPENDENCY
- A language must be active before any user, contact, website or template can use it, and a language in use by any of them cannot be deactivated. The languages offered on a website are a subset of the active languages chosen per website. [N-U26-059]

### CONSTRAINT
- Staff cannot choose a language that is not active. Printed documents use the contact's language even when the staff member works in another language; there is no setting that forces a language independent of the contact. [N-U26-061]

### RISK
- A contact left in the wrong language silently produces documents and emails in that language; frozen line descriptions keep the language at creation time; the public-customer rule means anonymous orders are described in the staff language. [N-U26-062]

### UNKNOWN
- How the browser-language redirect and cookie behave across multiple websites and domains, and real-time language switching in the portal, require running the system. [N-U26-063]

## CAP-U26-06 Formats and locale-dependent behaviours for Thailand

### WHAT
- Numbers and amounts are formatted from the language entry: decimal separator, thousands separator and grouping style, with the number of decimals taken from the currency or a named precision. The currency adds its symbol before or after the amount according to its own setting, separated by a non-breaking space. Rounding is by currency, not by language. [N-U26-064]
- Dates and times are rendered on the server from the language's date and time patterns, translated into the locale library's pattern syntax, with the locale's month and weekday names; the web client builds the same patterns from the language data it receives and sets the week start and text direction from it. All patterns are numeric Gregorian ones; no Buddhist-era handling exists in the Community source. [N-U26-065]
- An amount can be written in words on an invoice or a printed cheque. The words are produced by an external number-to-words library using the language's ISO code, with the currency unit and subunit labels from the currency record. The library is a separate, optional dependency pinned in the requirements, is not part of the source tree and was not found on the analysis machine either, so its Thai coverage could not be checked. [N-U26-066]

### WHY
- Locale conventions are data on the language and country entries so that a new locale needs no code; formatting functions only apply those data to values. [N-U26-113]

### BUSINESS RULE
- If the library is missing the words are empty and a warning is logged; if it does not support the language it silently uses English words. Whether Thai is among the supported languages cannot be established from the source tree; the Thai accounting localization adds no amount-in-words logic of its own. An invoice shows the words only when a company option is on; the option is on in the studied configuration. [N-U26-067]
- Name and address layout is per country: each country has an address layout pattern, an optional required-state and required-postal-code flag, a position for the customer name before or after the address, and an optional tax-identifier label that is translatable. The layout patterns of the Thai entry place street lines, city, province name with postal code and country name on separate lines and the name before the address. [N-U26-068]
- Country subdivisions (provinces) have a single non-translatable name. The 77 Thai province records are loaded with their names written in Thai script as the only value, so the name cannot be shown in English or any other language by translation. [N-U26-069]
- Sorting is performed by the database in the reader's language with English fallback for translatable fields; there is no per-language collation rule in the application. The collation of the studied database is the operating system English locale, and the framework creates new databases with the simple byte collation when created from the empty template. [N-U26-070]

### STATE
- The Thai accounting localization adds a branch-or-headquarter label for company contacts in Thailand, computed as a translatable code-level sentence; it is placed on the tax invoice next to the tax identifier. Printed document titles such as the tax invoice title are English source sentences held in the report screen definition. [N-U26-071]
- The Thai baht currency is shipped inactive with English unit and subunit labels (Baht, Satang), a Thai-script currency symbol character, rounding 0.01 and symbol after the amount; in the studied configuration it is active and used by the company. [N-U26-072]

### OPTIONALITY
- Several locale behaviours are optional: the company chooses whether the amount in words is printed, each currency chooses whether its symbol goes before or after the amount, each country chooses its address layout and whether province and postal code are mandatory, and the number-to-words library is an optional dependency. [N-U26-114]

### DEPENDENCY
- The formatting language for a document is the language in force in the rendering context; for a printed document that is the contact's language (see document-language capability), for the web client it is the user's language. A language that is inactive cannot be used for formatting. [N-U26-073]

### CONSTRAINT
- An address layout containing an unknown field key is rejected when saved; date and time patterns accept only supported directives; amounts are rounded by currency rules, not by language rules. [N-U26-115]

### RISK
- A Buddhist-era year is not produced by the server patterns; whether a client-side locale library would show a Buddhist year in some localized widgets cannot be determined from source. Amount-in-words in Thai depends on an external library that is outside this source tree. [N-U26-074]

### UNKNOWN
- Whether the number-to-words library supports Thai, how the browser locale renders Thai dates and numerals in the web client, and the collation behaviour of the production database need running the system and installing the dependency to confirm. [N-U26-075]

## CAP-U26-07 Hard-coded text audit

### WHAT
- User-visible text lives in three places: program code (English sentences passed to the translation function, field labels and help texts, exception messages), data (names and descriptions in data files and screen definitions, stored as translatable values), and translation files (one per language). In every studied business module the English wording is the base in code or data, and other languages exist only in translation files or in per-language columns of data files. [N-U26-076]
- Mechanical counts in the Thai accounting localization and the core accounting, sales, purchase, stock, product, unit-of-measure and analytic modules: server code calls the translation function 8, 688, 104, 64, 278, 110, 4 and 14 times respectively; exception messages are all passed through the translation function except three that join already-built message lists; no bare English literal is raised directly. [N-U26-077]
- The same modules define their screens with text attributes (labels, placeholders, help) counted at 0, 633, 162, 160, 495, 166, 5 and 25 for the string attribute respectively, and give names to seeded records through data files; these are translatable data, not code. [N-U26-078]
- The Thai translation files of those modules hold 23 (Thai accounting), 3171 (accounting), 862 (sales), 587 (purchase), 1809 (stock), 749 (product), 63 (unit of measure) and 162 (analytic) entries, split into model, model-term and code references; the code-reference entries translate exactly the code strings counted above. [N-U26-079]

### WHY
- Chart-of-accounts data lets a localization carry translations beside the English values in the same file, so a language can be added to a chart without changing any code. [N-U26-116]

### BUSINESS RULE
- Test of the rule that Thai text must not be hard-coded in source code: across the whole Community server tree no non-test Python file contains a Thai-script literal, and none of the studied business modules does; the single Python file with Thai characters is a mail-gateway test. This is an observation about the product source, not a requirement. [N-U26-080]
- In the Thai accounting localization the English text is always the base value and the Thai text is stored beside it as a per-language value tied to the same record identifier and field; this is a translation layer expressed in data, not in code. The exception inside the same product is the province list, where Thai script is the only stored value. [N-U26-082]

### STATE
- Thai-script text outside translation files is nevertheless present as data: 16 files in the Community tree contain it. They are the Thai accounting localization (four chart-template data files carrying Thai in per-language columns for 144 ledger account names and descriptions, 5 tax group names, 12 asset model names and 18 tax descriptions; one tax report file with 30 Thai report line names; one demonstration company record), the base module (the language catalogue name, the 77 Thai province names stored as the only value, and the baht currency symbol), one Cambodian chart file with a single stray Thai-block character, and web client library and test files (calendar locales, a PDF viewer and its Thai localization file, a list of language names in their own script, a search test) plus one mail test. [N-U26-081]

### OPTIONALITY
- The Thai demonstration company record is loaded only with demonstration data, which is not loaded in the studied configuration; Thai values in data files take effect only when Thai is activated. [N-U26-117]

### DEPENDENCY
- Thai values in chart data are applied only by the chart loader or the language loader after the English record exists, and only for active languages; they therefore depend on the English base record and its identifier. [N-U26-118]

### CONSTRAINT
- A data file carrying per-language columns must be named after its model (the part before the first dash selects the model) and every per-language column must pair with a base column of the same name. [N-U26-119]

### RISK
- Because Thai values in the localization are keyed by record identifier and field, renaming the identifier orphans them; because province names have no English value, any English-language report or form shows Thai script for them. [N-U26-084]

### UNKNOWN
- One additional file inside the studied folder, outside the product's own module structure, contains Thai text; it is a verification note of the programme and is excluded from the Community counts. [N-U26-083]

## CAP-U26-08 Roles, security, failure behaviour and performance of translation administration

### WHAT
- Translation administration is split by role. Administrators manage the language catalogue, activate languages, import language files and (through developer mode) edit application terms and run the scheduled code-translation refresh. Every internal user can run the language export wizard. Portal and public users and internal users can only read the catalogue. Editing a record's translations needs only write permission on that record and field, with no separate translation role. [N-U26-085]

### WHY
- The weekly refresh exists only to speed up community translation work by listing code translations with links to the external translation service; it carries no business function. [N-U26-120]

### BUSINESS RULE
- Failure behaviour: an invalid language code on a context raises an error; a malformed translation placeholder is logged and the English sentence is used; a missing language file is silently skipped with an information log; a language that is not active cannot be loaded and logs an error; an import file error aborts with a message; formatting with a missing language raises an error; a missing external translation library makes amount-in-words empty with a warning. [N-U26-087]

### STATE
- In the studied database the language catalogue has four access rules (public, portal and internal read; administrator full), the install and import wizards are administrator-only, the export wizard is internal-user, there are no record rules on any of these models, no automation rules and exactly one scheduled job related to translation: a weekly refresh of the code-translation list that is active. [N-U26-086]

### OPTIONALITY
- The translation menus appear only in developer mode, and the external-service module and its job are installed optionally; in the studied configuration both are present. [N-U26-121]

### DEPENDENCY
- The scheduled refresh depends on the external-service module being installed and on at least one installed non-English language to have anything to list; amount-in-words depends on an external library. [N-U26-122]

### CONSTRAINT
- Performance mechanisms visible in the source: active language data is cached; code translations are read once per module and language into memory; database imports are batched and executed as one statement per batch; a language activation updates all installed modules in one importer pass; translated text search uses a trigram prefilter; the web client fetches terms with a hash so unchanged terms are not resent; the login page loads only the generic language file. [N-U26-088]
- Limits noted in source: a lazily translated term cannot be compared or hashed; translated stored fields cannot depend on the language of the context; the database function argument limit is respected by splitting language lists into groups of fifty; an overwrite during module update must be requested explicitly. [N-U26-089]

### RISK
- Administrative rights are coarse: any internal user can export the whole term catalogue; any user with write access to a translated field can change that field's text in every active language without a separate review step; there is no audit trail dedicated to translation changes other than the usual field tracking. [N-U26-090]

### UNKNOWN
- Whether changing a translation is captured by record tracking for tracked fields, and the load impact of activating many languages on a large installation, require running the system. [N-U26-091]

## CAP-U26-09 Document and report presentation language

### WHAT
- A printed or emailed document is rendered in a language that is chosen separately from the viewer's interface language. For invoices, payment receipts, sales orders, quotations, purchase orders and delivery slips the language is the language stored on the document's partner (for delivery slips the first move's partner, then the picking partner, then the viewer), and the report template switches into that language before rendering the document body, header and footer. [N-U26-092]
- The switch is a template directive that renders a called template in a given language; the language value is always an expression over a record (partner, event, vendor, picking helper) and never a fixed constant in any of the 52 uses found in the Community source. The print pipeline keeps the document language on each article so that headers, footers and body are laid out consistently when the document is split into parts. [N-U26-093]

### WHY
- The directive that renders a called template in another language exists so that a document can be produced in a language different from the one of the person printing it. [N-U26-123]

### BUSINESS RULE
- The report definition has no language field and the print action takes no language option; there is no per-report, per-journal, per-company or per-user setting that forces a document language independent of the partner. The only controls are the partner's language and, for emails, the template language expression. [N-U26-094]
- A sent or posted invoice's PDF is generated once and stored on the invoice; it is not regenerated when it already exists, so the stored document keeps the language in force at its first generation even if the partner language changes later. Printing from the invoice menu does not save a copy by default. [N-U26-095]
- For emails, the template language expression may be any expression and can therefore yield a fixed language chosen by the template author, and the send wizard lets staff override it. The email body, subject, recipients and attachment descriptions follow the chosen language; the attached document itself still follows the partner language. [N-U26-096]

### STATE
- Where fixed document wording lives: report titles and labels are English source sentences inside report screen definitions held as translatable data, with other-language wording stored as per-language values of that data and exported in translation files; code-built phrases such as the branch-or-headquarter label are English sentences in code with translations in the translation files; master data names printed on documents (taxes, accounts, units, payment terms, journal names, company header and footer, invoice terms) are translatable record values. [N-U26-097]
- For Thailand, the Thai accounting localization supplies its own invoice document (English title sentence, branch label) and a second invoice report limited to sales invoices of Thai-country companies; both render in the partner's language like all other documents. The Thai translation of the title and of the branch sentences are entries in the localization's translation file. [N-U26-098]

### OPTIONALITY
- A precedent for fixing a second language exists in a Community localization that is not installed here: when a company option is on, its invoice report prints a second block in a language whose code is written into the report definition (Arabic, or English when the main language is Arabic), alongside the partner-language block. No installed module provides a comparable switch for Thailand. [N-U26-099]

### DEPENDENCY
- To render a document in a given language, that language must be active, the master data printed on it must hold values for it (otherwise English is shown), and the report definition text must have been translated for it; missing values silently fall back to English text inside an otherwise translated document. [N-U26-100]

### CONSTRAINT
- The viewer's interface language affects the surrounding screens, buttons and wizards but not the body of a document whose template switches to the partner language; two staff members with different interface languages print identical document text for the same customer, except for any text outside the switched template. [N-U26-101]

### RISK
- A statutory document whose required presentation language differs from the customer's stored language cannot be forced without changing the customer language, changing the report definition or adding a new switch; stored invoice PDFs can drift from later changes; mixed-language output arises when a language lacks translations for part of the printed master data. [N-U26-102]

### UNKNOWN
- Print behaviour in the portal download path, the language of the cached document preview, and the exact output of a Thai-language invoice (fonts, numerals, calendar year) require running the system with Thai active. [N-U26-103]

