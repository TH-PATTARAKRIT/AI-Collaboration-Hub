# U50 neutral knowledge — base framework: module management, view engine, HTTP layer, mail server, filters

> Neutral knowledge layer. DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> Unit: U50 | Source revision: 19.0.post20260921 | Date: 2026-10-02

---

[N-U50-001] A module management system tracks which add-on packages are installed, their dependency relationships, and the sequence in which they must be upgraded or uninstalled. Each module record carries a status value that moves through a defined lifecycle from not installed through to installed or removed.

[N-U50-002] All actions that change the installation state of modules are restricted to users holding administrator-level access. An attempt by a non-administrator triggers an access denial, and every such attempt is written to the system log with the user identity and network origin.

[N-U50-003] The system can automatically install a module when all its declared required dependencies have been installed or scheduled for installation. A country restriction may additionally limit this automatic behaviour to databases where at least one company is registered in the target countries.

[N-U50-004] Two modules may declare that they cannot coexist. During installation the system checks for such mutual exclusions and raises an error if both would become active. Categories can also be marked exclusive, preventing two sibling modules from the same category being installed together unless one depends on the other.

[N-U50-005] The dependency tree is traversed recursively in both directions: downstream traversal finds all modules that depend on a given set, and upstream traversal finds all prerequisites. A recursion depth guard prevents infinite loops when circular dependencies exist.

[N-U50-006] When an immediate install, upgrade, or uninstall is triggered, the system acquires an exclusive database lock on the module registry table and a separate lock on the scheduled actions table. A short timeout causes the operation to fail fast if another operation is already in progress rather than waiting indefinitely.

[N-U50-007] Uninstalling a module removes all database structures the module created, including tables, columns, and stored records, by delegating to a central data-cleanup mechanism that tracks all records created by each module.

[N-U50-008] The module list can be refreshed from disk to discover newly added or updated packages. Version comparison determines whether an existing module record needs updating. A stable in-memory cache maps module names to their database identifiers for fast lookup.

[N-U50-009] Translation files are loaded for installed modules in topological dependency order to ensure parent module strings are available before child module strings are imported.

[N-U50-010] User interface views are stored in the database as XML text. A secondary field records the file path from which the view originated so the system can reload it from disk in developer mode. When a view is modified through the user interface, a flag marks it as having been changed relative to the on-disk version.

[N-U50-011] View inheritance allows one view to augment or override the layout of another view without modifying the original. The combined result is assembled by applying each inheriting view's change specifications in order of declared priority and then database insertion order. A recursive database query collects the full inheritance chain. A circular inheritance check runs before any view can be saved. A required technical identifier must be present on all template-type views.

[N-U50-012] A view can be restricted to specific user groups. Users who do not belong to any of the listed groups cannot load that view. Extension views are not permitted to declare group restrictions directly; restrictions must be expressed as attributes within the view definition itself.

[N-U50-013] A previous version of a view's layout is retained so it can be restored without redeploying the module. Restoring from the saved previous version is called a soft reset; restoring from the original file is a hard reset. When a base view is modified, any per-user customisations of that view are discarded so all users see the updated version. A computed warning field surfaces validation errors to the editing interface without blocking the save.

[N-U50-014] The template rendering engine compiles an XML template into a Python generator function the first time it is needed. The compiled function is stored in cache and reused for subsequent renderings. All output from the engine is automatically escaped to prevent cross-site scripting attacks.

[N-U50-015] Template directives are XML attributes beginning with a reserved prefix. Conditional rendering outputs content only when a Python expression is true. Loop rendering iterates over a collection and makes the item value, index, size, first-flag, and last-flag available by name. Calling another template substitutes the called template's output in place of the call directive. Setting a variable stores a value in the rendering context for later use. Outputting a value renders it safely escaped. Group-based access checks are evaluated at render time against the user's group membership.

[N-U50-016] Template expression security is enforced by validating compiled bytecode against a fixed allowlist of permitted operations. A further check blocks hyperlinks using executable script schemes, with a narrow exception for browser history navigation.

[N-U50-017] Web asset bundles (scripts and stylesheets) are inserted into templates by a dedicated directive that retrieves the computed list of asset nodes from the asset management subsystem.

[N-U50-018] The HTTP routing layer is implemented as a non-table model that builds and caches a URL-to-handler map from all routes declared by installed modules. Before invoking a route handler the framework validates the upload size limit, applies the correct language to the request context, and confirms that any database record referenced in the URL path is readable by the current user. A fallback mechanism serves binary files stored as database attachments when no route matches the requested path. Routes are extended to support the HTTP OPTIONS method automatically for cross-origin preflight support.

[N-U50-019] Four authentication modes are available: authenticated user, public user, no authentication, and API key bearer token. Bearer token authentication validates the key against a stored credential and marks the session as non-persistent. Browser-based bearer usage is protected by checking browser-generated security headers to prevent cross-site request forgery. Session validity is checked on every request and the session is logged out if it has been invalidated. Preflight cross-origin requests bypass authentication entirely.

[N-U50-020] Outgoing mail server records are ordered by a sequence number so the system selects the highest-priority matching server when no specific server is requested. Three authentication methods are supported: username and password, an SSL client certificate, and command-line configuration. Five connection encryption levels are available, including two strict variants that validate the remote server certificate. Both the certificate and its private key are stored directly in the database rather than as file attachments. A configurable per-server maximum message size limits outgoing email volume. Archiving a server that is still in use is prevented.

[N-U50-021] Email sending is suppressed automatically when the system is running automated tests or is in the process of initialising its module registry, preventing test runs from sending real messages.

[N-U50-022] When sending an email the system selects the appropriate outgoing server by matching the sender address against server filter rules in priority order: exact address match, then domain match, then the default notification address, then the first available server, then command-line configuration. A custom header policy prevents thread-tracking headers from being split across lines so reply tracking remains intact. Blind carbon copy recipients are removed from message headers before delivery to prevent disclosure. The bounce return path and sender address are computed from the message headers, context overrides, and server configuration. Pre-validated recipient lists and blocklist overrides can be supplied through the request context.

[N-U50-023] Saved search filters associate a domain expression, sort specification, and context with a model and optionally with a specific menu action or embedded view. Filters can be private to specific users or visible to all users. Context keys that set user-specific defaults are stripped when a filter is shared to prevent inadvertent leakage of personal settings. A database-level constraint validates the sort specification as a properly structured array. A composite index supports efficient retrieval of filters relevant to a given model and action.

[N-U50-024] Export templates store a named list of fields selected for data export against a target model. The field list is preserved when a template is duplicated. The model name is indexed for fast retrieval.

[N-U50-025] Profiling records capture execution timing, SQL query counts, call stack traces, and memory usage for individual request handling sessions. A scheduled cleanup removes records older than thirty days in batches. Profiling data can be exported in a third-party performance visualisation format.

[N-U50-026] The country reference table provides ISO two-character codes as the primary identifier, with a configurable address layout template using named field substitution. A country can specify a custom input form for addresses, replacing the standard layout. Countries without their own flag image are mapped to the flag of their administrative country. Name lookups prioritise exact two-character code matching before falling back to name pattern matching.

[N-U50-027] Each currency record holds a three-character ISO code, a rounding factor that determines how many decimal places amounts are stored to, and a time series of exchange rates. The multi-currency feature group is automatically enabled when more than one active currency exists and disabled when only one remains. Deactivating a currency that is assigned to a company is blocked. Exchange rate lookup falls back through available historical rates to a default of one if no rate is recorded.

[N-U50-028] Decimal precision records associate a named usage category with a number of decimal digits. The value is retrieved through a stable in-memory cache backed by a direct database query. All modifications clear the cache immediately. Reducing the number of digits triggers a warning in the editing interface noting that existing stored values are not automatically rounded to the new precision.
