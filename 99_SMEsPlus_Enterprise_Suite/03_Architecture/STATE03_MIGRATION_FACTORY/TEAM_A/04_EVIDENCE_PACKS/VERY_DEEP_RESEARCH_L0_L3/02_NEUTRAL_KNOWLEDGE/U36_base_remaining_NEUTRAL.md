# U36 Base Remaining Capabilities — Neutral Knowledge (clean-room layer)

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
> Baseline: Odoo 19 Community (named once, here only)
> Scope: platform foundation, remaining areas (application registry, screens, templates, assets, request handling, reports, outgoing mail, saved filters and exports, actions and menus, geography and language, registry and support)
> Each statement carries an id that links to technical claims in the restricted layer; statements describe what the system must do and why; no implementation names appear here.

## CAP-U36-01 Application registry and lifecycle

### WHAT
- [N-U36-102] Installing an application first schedules it together with every application it depends on; nothing is loaded until the scheduled operation is applied, and an application whose dependency is missing from the system cannot be scheduled.
- [N-U36-107] Removing an application also schedules every application that depends on it; a confirmation screen lists the affected applications and the data structures that will be lost, and applying the removal deletes the data, tables, columns and customised screens that the removed applications own; the data layer repeats the administrator check.
- [N-U36-108] Upgrading an application also upgrades every installed application that depends on it; upgrading the foundation application upgrades everything and installs any newly required dependency.
- [N-U36-109] Refreshing the application list scans the applications available on disk, updates the stored description, author, licence, dependencies, countries, exclusions and category of known applications, adds new ones, and reports how many were updated and added.
- [N-U36-113] When applications are installed or upgraded, their translation files are loaded for every active language in dependency order; importing a translation file creates and activates the language when needed and by default replaces existing translations, including customised ones.

### WHY
- [N-U36-103] Glue applications that only make sense when several others are present are installed automatically once all their required dependencies are installed or scheduled; a country-specific one is added only when at least one company belongs to one of its countries.

### BUSINESS RULE
- [N-U36-101] Installing, upgrading or removing an application, refreshing the list of available applications, cancelling an interrupted operation and loading demonstration data are limited to the system administrator role; every attempt, allowed or refused, is written to the server log with the user, the target and the origin address, and the buttons that start these operations are shown only to that role.
- [N-U36-104] Two applications can declare themselves incompatible, and some categories are exclusive: scheduling is refused when incompatible applications would coexist, or when applications of an exclusive category do not all belong to the dependency chain of one of them.
- [N-U36-105] An application whose required external software or libraries are missing cannot be installed or upgraded; the message names the missing item and, on Debian-style hosts, suggests the package to install.
- [N-U36-106] The immediate install, upgrade and uninstall paths refuse to start while another operation is pending, while a scheduled job is running, or during tests; they lock the registry, apply the change, reload the system and then show the next pending configuration step or the first menu; the activated companies of the user are passed on so that a chart of accounts installed meanwhile is configured for the right company.
- [N-U36-110] An interrupted or cancelled operation can be reset: applications waiting to be installed return to not installed, and those waiting to be upgraded or removed return to installed; the upgrade screen shows a completion message when nothing is pending.
- [N-U36-111] An application record that is installed or scheduled cannot be deleted.

### STATE
- [N-U36-112] An application is uninstallable, not installed, to be installed, installed, to be upgraded or to be removed; its technical name is unique, and a dependency not present on disk is reported as unknown.

### OPTIONALITY
- [N-U36-114] Descriptive data such as the licence, the enterprise-only flag, the icon and the category are informational and do not block installation; the store view hides theme categories, and hides the hidden category unless technical features are enabled; the full dependency map can be requested for display, and installed-application lookups are cached.

### DEPENDENCY
- [N-U36-120] In the restored database 356 of 713 applications are installed, 334 are not installed and 23 are uninstallable; 402 are flagged for automatic installation and 21 as enterprise-only; all installed ones carry the same open licence, 35 installed ones are test fixtures, no category is exclusive, exactly two accounts hold the system administrator role, and the access-rights and technical-features roles have no direct members.
- [N-U36-121] The restored database holds exactly the foundation application's own configuration as declared in source: 146 access rows, 32 record rules, 66 menus, 182 screens (177 definitions and 5 templates), 2 scheduled jobs and 3 paper formats.

### CONSTRAINT
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### RISK
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### UNKNOWN
- [N-U36-122] The behaviour of the operation lock, the registry reload and the cancellation path under concurrent workers or a running scheduled job is not confirmed, and the language-installation wizard and the application-request module were not read in depth.

## CAP-U36-02 View definition, inheritance and validation

### WHAT
- [N-U36-201] A screen definition (view) is a stored structured document with a type, a target model, a priority, an optional parent and a mode; it keeps the current text, the text before the last change and the originating file so that it can be reset.
- [N-U36-203] A user may hold a personal customised copy of a screen (for dashboards); the newest copy wins, copies are removed when the user or the original screen is deleted, and any change to the original screen discards all personal copies.
- [N-U36-210] The final screen is built by taking the base screen and applying active extensions in priority order, each extension's own children immediately after it, then child base screens; during an upgrade only screens of already loaded applications take part.
- [N-U36-219] A multi-screen request returns the screens, the field descriptions of every model involved, the print and action entries bound to the model and the saved filters of the model.

### WHY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### BUSINESS RULE
- [N-U36-204] A screen can be reset to its previous text or to the text of its source file, or replaced by another screen's text; the reset itself does not overwrite the saved previous text, and in developer mode the file text is used for screens not modified in the database.
- [N-U36-205] Creating a screen derives its type from the root element or its parent, requires a text, gives template screens a generated key, and validates the result; deleting a screen is refused while other screens inherit from it, except during application removal; copying makes a new unique key.
- [N-U36-206] A screen that extends another cannot carry role restrictions on the record itself; role restrictions must be written inside the definition.
- [N-U36-207] Every creation or relevant change is validated as a whole: the combined document must parse, locators must resolve, every referenced field must exist on the model and be accessible, expressions and filters must be valid, buttons must call public methods, removed legacy attributes and forbidden client-template directives are refused, and any failure cancels the whole operation.
- [N-U36-208] Custom screens (those without an application origin) are re-validated for a model whenever the registry is rebuilt, and screens of an application are re-checked after it loads, so that a model change that breaks a user-made screen fails at update time; diagnostics list locators that no longer anchor on their parent.
- [N-U36-209] The default screen for a model and type is the active base screen with the lowest priority; when none exists a generated default is used, and a missing type for which no default can be generated gives an error.
- [N-U36-211] Extension instructions are applied by shared template-inheritance logic; an error names the screen, its identifier, file and line.
- [N-U36-212] A screen with no role assignment is private; one with roles is accessible only to members; extensions follow their parent; public templates can be rendered for anonymous visitors only if they pass this check.
- [N-U36-214] When a screen is served, elements restricted to roles the user lacks are removed, create, edit and delete options are switched off where the user lacks the matching permission on the model, and fields required by expressions are added invisibly; a field is hidden when the user lacks either the model access or the element's role.
- [N-U36-216] A button on a screen may call only public methods that take no parameters; private methods and unknown actions are refused when the screen is validated.
- [N-U36-217] When an application updates a shared template, its site-specific copies are updated only for values that were not individually changed, and parent changes are replayed after the website application loads.

### STATE
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### OPTIONALITY
- [N-U36-213] Compiled screens and templates are looked up by identifier or key in a cache that is cleared on any screen change; the cache holds per-language results for all roles, and role filtering happens afterwards per user; developer mode bypasses the cache.
- [N-U36-215] Elements restricted to the technical-features role become invisible to others; that role is treated as a display switch, not as a security role.
- [N-U36-221] Editing branding attributes are added to rendered output only in editing mode and are removed for elements that cannot be edited in place.

### DEPENDENCY
- [N-U36-220] The restored database has 4271 template screens and about 2840 screens of other types (list, form, search, kanban, graph, pivot, calendar, activity, hierarchy), none flagged as modified, 31 with role assignments, no personal copies, and 2306 template screens that belong to websites without an application origin; 182 screens are owned by the foundation application, as in source.

### CONSTRAINT
- [N-U36-202] Only the system administrator role can read or change the stored screen definitions directly; ordinary users have no access to them, and the reset wizard is available to administrators and to the access-rights role.

### RISK
- [N-U36-218] Screens are fetched with elevated rights for any user who may read the model; protection comes from model access and from element-level role filtering afterwards, not from the screen records themselves.

### UNKNOWN
- [N-U36-222] Structural validation performed by shared tooling outside the foundation application, the web client's use of served screens and screen behaviour during a real upgrade were not read.

## CAP-U36-03 Template engine and asset bundles

### WHAT
- [N-U36-301] The template engine compiles each template into a function, caches it per language, branding and profiling settings, and renders output as escaped markup so that untrusted values cannot inject markup; deprecated raw output wraps content as trusted.

### WHY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### BUSINESS RULE
- [N-U36-302] Template expressions run in a restricted sandbox: each expression is compiled, checked against an allow-list of operations and run with a limited set of names; templates receive the user, the company, the request and the full environment unless a minimal context is requested.
- [N-U36-303] A template element can be shown only to members of named roles, or hidden from them, evaluated at render time for the viewing user.
- [N-U36-305] HTML content is rendered as trusted after link clean-up, and dynamic links using a script scheme are blanked.
- [N-U36-306] One template can call another by a fixed or computed name, passing values and a content block; the language and options can be changed for the call.
- [N-U36-307] Pages include script and style bundles through a dedicated directive that emits escaped link tags; bundle links are cached until restart outside developer mode.
- [N-U36-308] Bundle contents are assembled from application declarations plus administrator-defined asset rows (append, prepend, before, after, replace, remove, include), with early rows applied before application files and later rows after; circular includes are refused; editing asset rows is limited to the system administrator and website editors.
- [N-U36-310] Generated bundles are saved as public files created with elevated rights under a versioned address, outdated versions are deleted, and connected clients are told to refresh when a tracked bundle changes.

### STATE
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### OPTIONALITY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### DEPENDENCY
- [N-U36-311] Conversion of right-to-left styles and of style preprocessor sources depends on external converters; when missing, the original style is used and the issue is logged.

### CONSTRAINT
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### RISK
- [N-U36-304] Related-record fields and contact blocks print their names, addresses, phone, email and tax numbers with elevated rights, so a report or page can show details of related records that the viewer could not open directly, including across companies.
- [N-U36-309] An asset row may point to an external web address or an uploaded file, so an administrator can load third-party scripts into every page using a bundle; local paths are limited to the static folders of installed applications.

### UNKNOWN
- [N-U36-312] The output of asset compilation, the availability of converters on the host and the client-side loading of bundles were not exercised or read.

## CAP-U36-04 Request handling, authentication modes and binary content

### WHAT
- [N-U36-401] The routing layer builds the list of web addresses from installed applications only, and every route declares an authentication mode; many applications extend this layer.
- [N-U36-407] Internal data cleanup runs daily: the foundation owns an auto-vacuum job and a user-deletion job, the vacuum job runs every cleanup routine of every installed application (expired web sessions, orphaned stored files, device logs, saved script revisions, profiles); the restored database has both jobs active.
- [N-U36-409] The web client receives translated terms of installed applications and the language's formatting parameters, and a hash of this data versions the translation file.

### WHY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### BUSINESS RULE
- [N-U36-402] A route requiring a signed-in user refuses anonymous or public sessions; a public route silently uses the public user; a route with no user runs without identity; a session whose security token no longer matches is ended before the route runs.
- [N-U36-403] A key-based route accepts an API key in the authorisation header and works without a session; a key that does not match an existing session user is refused; without a key an interactive browser request is accepted only for a same-origin top-level page visit.
- [N-U36-404] Before a route runs, the request upload limit is set from a database parameter, and every record identified in the address is bound to the request user and must pass a read check; the public user or a missing record sees page-not-found.
- [N-U36-405] Routes can require a captcha token on state-changing requests; the foundation provides only the hook.
- [N-U36-406] When no route matches, the address is looked up among stored public file attachments and served if it has content; creating such attachments is limited to the system administrator role.
- [N-U36-410] Downloaded files are served if a valid file-specific or attachment token is supplied, if the file is public, or if the user can read it; portal users are checked through the document the file belongs to; attachment tokens are readable only by internal users.
- [N-U36-411] Files are streamed from the file store, the database, a module's static folder or by redirect; names are cleaned of line breaks and shortened, images can be resized on request, and a placeholder is shown when an image is missing or not allowed.
- [N-U36-413] Files in the store that no attachment references any more are removed by the daily cleanup after a short lock on the attachment table; this does not apply to database storage.
- [N-U36-415] Uploaded images above a size limit are reduced and compressed according to parameters, uploaded files record size, checksum and indexed text, and a helper can reuse an existing identical file, returning identifiers of files the caller might not otherwise see.
- [N-U36-416] A file held only as a remote address is fetched and stored locally before it is merged into a printed document; failure is logged and the file skipped.

### STATE
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### OPTIONALITY
- [N-U36-408] Cookie consent is a hook: required cookies are always allowed and others only for identified users; website applications refine it.
- [N-U36-412] Attachment storage is the file system by default or the database by parameter; files are named by content hash and spread over subfolders; an administrator can migrate all attachments to the configured storage; the restored database uses the file system.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### CONSTRAINT
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### RISK
- [N-U36-414] Uploaded web pages and similar active content are stored as plain text unless the user may edit screens, and serving a stored file at a chosen address is limited to the system administrator role.

### UNKNOWN
- [N-U36-417] The real handling of each authentication mode, cross-site protection and upload limits was not exercised, and most applications that extend request handling were only listed.

## CAP-U36-05 Report actions and document rendering

### WHAT
- [N-U36-501] A report definition names the model, the output kind (page, PDF or text), the template, an optional paper format, an optional stored-copy name, a filter, and roles allowed to see it in print menus.
- [N-U36-504] PDF output renders the document, splits headers, footers and bodies, runs an external conversion tool, then splits the PDF per document so each can be stored; corrupted pieces raise an error listing the problem records.
- [N-U36-511] Barcode and QR images are generated by the server for several symbologies, with size limits and a fallback to a general symbology when a check digit fails.

### WHY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### BUSINESS RULE
- [N-U36-505] If a report has a stored-copy name expression, an existing stored copy for the document is found by name and returned when reuse is enabled; otherwise the generated PDF is saved as an attachment under the user's rights, and a refusal is silently ignored; the name expression runs in a restricted sandbox; the document template must expose the record markers for splitting.
- [N-U36-510] A report with a filter appears only when at least one selected record matches the filter; administrators can add or remove a report from the print menu of its model.

### STATE
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### OPTIONALITY
- [N-U36-508] A report uses its own paper format or the company's default; values embedded in the document override the format record; a format is either a standard size or a custom size; default margins are 40, 20, 7 and 7 millimetres and the default resolution is 90 dots per inch, and the restored database seeds three base formats among twelve, with the model's own orientation default differing from the seeded ones.
- [N-U36-509] When an administrator prints and the company has no document layout chosen, the layout configurator opens first; the restored database has no company with a layout chosen.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### CONSTRAINT
- [N-U36-502] Report definitions can be created or changed only by the system administrator role; paper formats are visible to internal users and editable by administrators; the choice of document layout is open to every internal user.
- [N-U36-506] PDF printing requires the external conversion tool, and with a single server worker it is flagged as unavailable; otherwise the user gets a clear error.

### RISK
- [N-U36-503] Rendering reads the report definition with elevated rights for any signed-in user, then reads the documents under the user's own rights; a report-specific data model can replace this and carries its own access discipline; the user's name, timezone and company appear in the document.
- [N-U36-507] For PDF printing the user's session is copied to a temporary session handed to the external tool so internal links work as that user; local file access is disabled and the base address and rendering delay come from parameters.
- [N-U36-512] The report page route is open to every signed-in user, including portal users, and does not test the report's role list; protection is therefore the user's access to the documents, to be confirmed at runtime.
- [N-U36-513] The barcode image route is open to anonymous visitors and returns only an image of the value given in the address.

### UNKNOWN
- [N-U36-514] Presence and version of the external conversion tool on the target host, rendering with real documents and custom report models of other applications were not examined.

## CAP-U36-06 Outgoing mail servers

### WHAT
- [N-U36-601] An outgoing mail server describes how to send email: host, port, login or certificate or command-line authentication, encryption level, priority, sender filter, maximum size and active flag; only the system administrator role can manage servers.
- [N-U36-608] A connection test checks the sender, a test recipient and the start of data transfer without sending, and can detect the maximum message size from the server.

### WHY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### BUSINESS RULE
- [N-U36-604] A mail server that is still used (for example by an email template) cannot be archived; the message lists where it is used.
- [N-U36-605] The server for a message is chosen by sender address, then sender domain, then the notifications address, then the first server without filter, then the first server, then the command-line configuration; when a server cannot send for the sender's domain the notifications address is used instead; the restored database has no server rows.
- [N-U36-606] Before sending, the envelope sender is set (the bounce address only if the server allows it), recipients from To, Cc and Bcc are cleaned to plain ASCII addresses and deduplicated, optional allow and block lists apply, and blind copies are removed from the message headers; special headers can alter the visible recipient list.
- [N-U36-607] Sending is direct with no queue or retry; failure raises a delivery error naming the server and cause; no real sending happens during tests or while the registry is starting; mails need a configured sender address.

### STATE
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### OPTIONALITY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### CONSTRAINT
- [N-U36-602] Credentials and certificates of a mail server are visible only to the system administrator role and are read with elevated rights when a message is sent.
- [N-U36-603] Certificate authentication requires an encrypted connection and both certificate and key; connections default to no encryption, and the non-strict encrypted modes encrypt without verifying the server identity; the strict modes verify certificate and host name.

### RISK
- [N-U36-609] Server debug logging records the whole conversation, possibly including credentials, to the server log.

### UNKNOWN
- [N-U36-610] Delivery through a real server, the deployment's command-line mail settings and personal mail servers of the mail application were not examined.

## CAP-U36-07 Saved filters, export templates, embedded actions and language exchange

### WHAT
- [N-U36-701] A saved filter stores a search domain, context, sort order and model, can be private, shared with named users or global, can be tied to an action or an embedded action, and can be the default.
- [N-U36-704] Filters offered for a model are those private to the user or global that match the current action, or have no action; the restored database holds 13 filters, none default, on four models.
- [N-U36-705] An export template stores a model and a list of fields for repeated data exports; it has no owner and no record rule; the restored database holds 4 templates with 34 lines.
- [N-U36-708] An embedded action is a shortcut on an action that opens another action or runs a method, with domain, context, roles and default view; it shows only for matching parent records and permitted users; those loaded with an application cannot be deleted by users.

### WHY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### BUSINESS RULE
- [N-U36-703] Shared filters lose default values in their context so they cannot inject defaults into other users' sessions; domains are read as plain data, never executed; sort must be a list.
- [N-U36-709] Exporting a language template can be done by every internal user, for chosen applications or for a model with a user-given domain, under the user's own access; importing a language file is limited to the system administrator role.

### STATE
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### OPTIONALITY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### CONSTRAINT
- [N-U36-702] Internal users may see and change filters that are global or assigned to them, including changing or deleting global filters; portal and public users see only filters assigned to them; administrators see all; embedded actions can be modified by their owner or when shared.
- [N-U36-706] Managing export templates is granted to an optional export-permission group which administrators hold by implication and other users only by explicit assignment; template lines are open to all internal users.

### RISK
- [N-U36-707] Data export routes of the web application run in the caller's rights and log who exported what; in the lines read they do not test the export-permission group (the group is tested in the user interface and in the JSON data route), so the group looks like a screen-level control, to be confirmed at runtime.

### UNKNOWN
- [N-U36-710] Client behaviour of the export dialog, filter sharing and embedded actions, and the remaining server-side export code, were not fully read.

## CAP-U36-08 Actions, scheduled wizards and menus

### WHAT
- [N-U36-801] Actions are the stored operations that menus, buttons and scheduled jobs run: window, report, address, server and client actions share a base, a type, a bound model, bound view types and an optional short address.
- [N-U36-808] Every change of server action code is kept as a revision; at most 100 are kept per action, a wizard shows the difference and restores a revision; the restored database holds 169 revisions.
- [N-U36-813] Menus form a tree with a sequence, role restrictions, an optional action and icon; recursion is refused.

### WHY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### BUSINESS RULE
- [N-U36-802] An action's short address must be lowercase letters, digits, dashes and underscores starting with a letter, may not use reserved prefixes or the word new, and must be unique across all kinds of action.
- [N-U36-803] Deleting an action also deletes its wizard entries and saved filters, and users whose home action is removed lose it.
- [N-U36-804] The print and action entries bound to a model are cached, then filtered per user: entries restricted to roles the user lacks, and entries whose target model the user cannot read, are dropped.
- [N-U36-806] A window action must target an existing model, may not repeat view modes, has default view modes, size limit and caching, and asks the target model for its empty-list help text.
- [N-U36-807] An address action holds a web address and a target; the address is not validated.
- [N-U36-811] A client action carries a tag, target, optional model, context and parameters stored as text and read in a sandbox.
- [N-U36-814] A menu is shown to a user only if it passes its role restriction and, when it has an action, that action exists and the user can read its model; folders appear only above a visible menu; menus for roles without a readable action are hidden; this check uses model-level read access only and is a convenience, not a protection; the Apps root is for the system administrator role and the Settings root for the access-rights role; the restored database has 729 menus of which the foundation owns 66.
- [N-U36-815] Deleting a menu promotes its children to the top level, copying a menu renames it with a counter, and menu changes clear caches.

### STATE
- [N-U36-810] A configuration wizard entry is open or done; only one can be open at a time; launching marks it done and opens its action; the restored database has 3 entries, all done.

### OPTIONALITY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### CONSTRAINT
- [N-U36-809] The code of a server action can be read or written only by the system administrator role; an action with roles runs for those roles regardless of record rights, one without roles needs write access to its model and records; failed attempts are logged; update actions evaluate values in a sandbox.
- [N-U36-812] Every action table and the revision table can be written only by the system administrator role; embedded actions by every internal user within their rules; the restored database holds 1117 actions (839 window, 78 report, 9 address, 168 server, 23 client), all server actions are code actions, 42 are restricted to roles, none is a webhook, 207 are bound to models and 192 have short addresses.

### RISK
- [N-U36-805] Actions are delivered to the client by reading with elevated rights and returning only a whitelist of safe fields, so users need no access to action tables to open an action but never receive server-side content.

### UNKNOWN
- [N-U36-816] Client rendering of menus and actions and the use of server actions by scheduled jobs and automation rules of other applications were not exercised.

## CAP-U36-09 Countries, languages, banks and contact classification

### WHAT
- [N-U36-901] Countries carry a unique name and code, address layout, calling code, currency, groups, states, a flag for zip and state requirements, and a tax label; the restored database holds 251 countries, 2131 states, 10 country groups and the Thai record has a layout, required zip, calling code 66 and 77 states.
- [N-U36-903] Country groups have an upper-case unique code and a list of countries and serve as reference lists that other applications can use.
- [N-U36-906] Contact tags form a tree with colours and a search that includes sub-tags; industries are a translatable list editable only by the system administrator role; the restored database has 21 industries, no tags, 1 bank and no bank accounts.
- [N-U36-910] A language record holds locale code, ISO code, address code, direction, date and time formats, first weekday, digit grouping and separators; at least one language must stay active, active-language data is cached; the restored database has 93 languages with only English active.
- [N-U36-915] Decimal precisions are named values (default 2 digits, unknown names give 2), changing them clears caches and warns that existing data is not updated; the restored database has eight, with Payment Terms at 6 and ORM Precision at 3; only the system administrator role may change them.

### WHY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### BUSINESS RULE
- [N-U36-902] A country's address layout drives how addresses are printed and how the address part of the contact form is arranged for the current company's country; an invalid layout key is refused; changing a country's layout or tax label clears screen caches; the contact form's tax label follows the company's country when set.
- [N-U36-904] States belong to one country with a code unique per country and are found by code first or by a name-and-country pattern.
- [N-U36-907] On import, a state that does not belong to the imported country is replaced by the same-code state of that country or removed.
- [N-U36-911] Date and time formats may only use allowed directives and a 24-hour clock combined with AM or PM is converted to 12-hour with a warning.
- [N-U36-912] A language code cannot change; a language cannot be deactivated while any user, contact or automated process uses it; English cannot be deleted, nor the language in use, nor an active language.
- [N-U36-913] Activating a language loads translations of all installed applications; a new language takes its formats from the host's locale data or defaults with a warning; at initialisation the first configured language becomes the default for contacts and for the main company.
- [N-U36-914] Numbers are formatted with the language's decimal point, thousands separator and international or Indian grouping.
- [N-U36-919] At most three contacts can be merged at once, a contact cannot be merged with its own parent or child, contacts linked to more than one user cannot be merged, and contacts with different emails can be merged only by an administrator.

### STATE
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### OPTIONALITY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### CONSTRAINT
- [N-U36-905] Countries, states and country groups are readable by everyone including public visitors; the contact-creation group edits states and country groups, and only the system administrator role edits countries.
- [N-U36-916] Banks and bank accounts: internal users read, the contact-creation group and the system administrator role edit banks, and the contact-creation group edits bank accounts; bank accounts follow a company rule, with extra rules added by HR and billing applications.
- [N-U36-917] The contact merge wizard is open to the contact-creation group (which administrators hold by implication), not only to administrators.

### RISK
- [N-U36-918] Merging contacts repoints records of other applications that refer to a merged contact, including company-specific values across all companies, with elevated rights and raw database statements, and deletes rows that would violate a uniqueness rule, so a user with only contact-creation rights can change or remove data of other applications.

### UNKNOWN
- [N-U36-920] Completeness and accuracy of the seeded country, state and language data and the availability of host locale data were not examined; no Thai statutory fact is asserted here.

## CAP-U36-10 Metadata registry and platform support

### WHAT
- [N-U36-1001] The registry stores every model and field of the system and also user-created custom models and fields, whose names must begin with a fixed prefix; creating a custom model creates its table and a default name field; the restored database has 1182 models and 23168 fields, all application-owned, no custom ones and no fields with computed code.
- [N-U36-1008] Dynamic user-defined properties on models without a parent keep one definition per property field, created on demand and cached; contacts use it so properties are global; only the system administrator role edits definitions.
- [N-U36-1010] Device logs record each session's platform, browser, address, country, city and activity times; users read only their own devices and administrators all; revoking a device ends its session after an identity check; duplicate logs are compacted and logs whose session no longer exists are marked revoked; the restored database holds 4 logs.
- [N-U36-1011] A log table holds server and client log lines and is managed by the Access Rights group.
- [N-U36-1013] Each user has one settings row, created on demand and readable and writable only by that user and administrators.
- [N-U36-1014] Avatars are generated as coloured initials when no image exists; images are stored once and as four stored smaller sizes; a scoped token can authorise anonymous download of the small avatar.
- [N-U36-1015] Group privileges are the rows of the user permission matrix, each with a category and groups; editable by the Access Rights group.

### WHY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### BUSINESS RULE
- [N-U36-1003] Only custom models and fields can be deleted; application-owned ones cannot; deleting a custom model drops its table and its dependent fields, jobs and identifiers; a custom field cannot be removed or renamed while another depends on it or a screen uses it.
- [N-U36-1004] A model name allows only lowercase letters, digits, underscores and dots; the ordering expression must use stored fields; a model's name, kind and type flags are fixed after creation.
- [N-U36-1005] Custom fields cannot change model or type, many-to-many ones get generated relation tables, domains are validated, and selection values of application-owned fields can be changed only by an administrator.
- [N-U36-1007] Data import converts text into typed values with per-cell errors and warnings and resolves related records by name, external identifier or database identifier; missing matches are errors unless configured, auto-creation from a name is limited to enabled fields, external identifier lookup is unfiltered by record rules, and nested creation of many-to-one records is refused.
- [N-U36-1009] Performance profiling can be switched on only until a database expiry set by the administrator wizard; profiles contain SQL and stack traces, are deleted after 30 days, and profiler settings come from the client session, which the code flags as potentially dangerous.
- [N-U36-1012] Loading demonstration data into a running database is administrator-gated and logged; the restored database has none.

### STATE
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### OPTIONALITY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### DEPENDENCY
- NOT APPLICABLE — no statement of this kind was supported by the source read for this capability.

### CONSTRAINT
- [N-U36-1002] The Access Rights group, not only the system administrator role, can create and change models, fields, access rows, record rules and external identifiers; internal users hold rows that grant no permissions.

### RISK
- [N-U36-1006] A custom field can carry code that is run in a sandbox on every read of the field; the code is expected to run with the rights of the reader (to be confirmed), and the code entry page is shown only when technical features are enabled, which is a display switch.

### UNKNOWN
- [N-U36-1016] The strength of the code sandbox for custom fields, profiler behaviour on a live system, geolocation of device logs and the remaining parts of the model registry file were not exercised or read.

