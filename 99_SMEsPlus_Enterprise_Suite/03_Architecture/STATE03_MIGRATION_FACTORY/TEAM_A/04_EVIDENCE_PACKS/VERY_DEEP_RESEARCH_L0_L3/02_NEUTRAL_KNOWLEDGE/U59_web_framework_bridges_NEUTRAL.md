# U59 neutral knowledge — web framework server layer: RPC endpoints, session management, tours, image integration

> Neutral knowledge layer. DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> No code syntax, no file paths, no snake case identifiers, no backticks, no technical notation.

---

[N-U59-001] The web framework module provides a home controller that handles the root address of the application, routing visitors without a database session to a login page, and routing internal users to the main application interface. A security check on every visit confirms the session is still valid before the page is served.

[N-U59-002] Every time the main application page is loaded, the server attaches a short-lived secret value to the page data. This secret is derived from information tied to the current user session, so it changes whenever a security event such as a password change occurs. The page instructs the browser not to store a cached copy of the response.

[N-U59-003] A dedicated endpoint delivers the navigation menu structure to the browser client. It carries the application identifier, action pointer, icon data, and child menu references for every menu item. The response is marked as non-cacheable.

[N-U59-004] The login page accepts the user name, password, and an optional authentication type. It optionally invokes a CAPTCHA verification before authenticating. On successful authentication the browser is directed to either the internal application interface or an external user landing page depending on the account type.

[N-U59-005] A health check endpoint reports the operational status of the application server. An optional flag causes the endpoint to also test the database server connection, reporting a failure status code when the connection cannot be established. The endpoint does not write to the user session.

[N-U59-006] A session information endpoint returns a comprehensive package of data about the current user: identity flags such as administrator and system status, the active database name, a hash of the server module registry for cache-busting, user preference settings, server version, partner identity, the base web address, file upload size limits, the home action, all currency definitions, and bundle loading parameters. For internal users the response additionally includes the full company hierarchy the user is allowed to access.

[N-U59-007] An authentication endpoint allows a browser client to authenticate by providing a database name, user name, and password in a single call. After authentication it returns the full session information for the newly authenticated user. A module list endpoint returns the names of all currently installed modules. A logout endpoint ends the current session and redirects the browser.

[N-U59-008] The session data includes a registry hash value derived from a keyed digest of the server module registry sequence number. This hash changes whenever the set of installed modules changes, allowing the browser to detect that cached assets are stale.

[N-U59-009] A general-purpose remote procedure call endpoint accepts a model name, method name, positional arguments, and keyword arguments. The endpoint inspects whether the requested method is read-only and sets the database transaction mode accordingly. A separate button-call endpoint performs the same invocation and additionally processes the return value as a client action when the result has an action type.

[N-U59-010] The binary content endpoint serves file attachments and images stored in the database. It resolves records by external identifier, numeric identifier, or model and field combination, and returns the binary content as a file stream. The endpoint supports cache headers for immutable content identified by a unique version token. Access tokens allow serving public content without a login session.

[N-U59-011] An attachment upload endpoint accepts multipart file uploads from the browser and creates attachment records in the database linking the file to a specified model and record. It normalises file names for Safari browser compatibility and returns the identifier and metadata of each created attachment.

[N-U59-012] A company logo endpoint returns the logo image for the current user company. When no database session exists it serves a default logo from the application files. With a session it retrieves the logo data by querying the company and user tables directly, returning the image with the correct MIME type and a last-modified date.

[N-U59-013] Three export endpoints serve data export operations. A formats endpoint lists the available export formats, currently spreadsheet and comma-separated values, noting whether the spreadsheet library is installed. A field enumeration endpoint returns the exportable fields for a model, respecting import-compatibility mode and dynamic property fields. Two download endpoints serve the actual data: one for comma-separated files and one for spreadsheet files. Grouped exports build a tree of aggregated values before writing them hierarchically into the output file. Non-grouped exports process records in batches to control memory use.

[N-U59-014] A report controller serves rendered documents in HTML, PDF, and plain text formats via separate URL patterns incorporating the document type. A download helper endpoint parses a URL encoding the report type and document identifiers, delegates to the appropriate render method, and attaches a content-disposition header for download. Report file names can be customised through an evaluated expression stored on the report definition.

[N-U59-015] Translation endpoints provide localised text to the browser client. A bootstrap translation endpoint loads translations from package files for modules marked as needing early translation, used before a session is established. A main translation endpoint returns all installed translations for the current language, gated behind a hash comparison to avoid transferring unchanged data. Translations are served with long-term caching headers.

[N-U59-016] A domain validation endpoint accepts a search domain expression and a model name. It validates the domain by preparing the equivalent database query and running it in explain mode, which forces the database engine to parse and plan the query without executing it. Returns true when the domain is valid, false otherwise.

[N-U59-017] An action loading endpoint resolves an action by numeric identifier, external identifier in dotted notation, or URL path segment, and returns the action definition filtered to the fields the client is permitted to read. A server action run endpoint executes a stored server action and returns the resulting client action. A breadcrumb loading endpoint resolves a series of action and record references to display names for restoring a navigation history.

[N-U59-018] A set of model methods provides data access optimised for the browser client. The web read method accepts a field specification that describes which fields and sub-fields to return for relational fields, respecting access rules for co-models and applying limits and ordering to related record sets. It handles reference and property field types with co-record existence checks.

[N-U59-019] The web search-read method combines a domain search with a web read in a single call, returning both the records and a total count. The count is fetched by a separate search-count call only when necessary: when the result set is exactly at the requested limit and no count limit was reached. The web save method writes values to an existing record or creates a new one, then returns the updated record via web read with binary field sizes rather than content.

[N-U59-020] A grouped data method wraps the database group-read operation to serve list and kanban views. It accepts a hierarchical groupby specification, aggregation instructions, ordering, and state information describing which groups are currently open. It automatically fetches record data for open groups, batching all records across groups into a single read operation before distributing results back to each group. A context key limits the maximum number of groups opened automatically.

[N-U59-021] The formatted group-read method translates raw database group results into the dictionary format expected by the browser client. It applies group expansion for kanban columns when the field has an expansion method defined, fills temporal gaps in date-grouped results when requested through a context flag, and converts raw field values to label-and-domain pairs used for group navigation.

[N-U59-022] Search panel methods provide the data for sidebar filter panels. A category panel method returns a hierarchical or flat list of available values for a single-select field, including optional record counts and parent identifiers needed for tree display. A multi-select filter panel method returns a flat list of values for a filter field, optionally grouped by a secondary field. Both methods return an error message object when the value count exceeds the configured limit.

[N-U59-023] The HTTP dispatch layer extension handles debug mode activation from the URL, stores the debug state in the session, and rejects unrecognised mode strings. It detects known web crawler and AI assistant user agents to suppress session-dependent rendering. A cookie cleanup step normalises the company selection cookie format on every request and clears it on logout.

[N-U59-024] The view information method returns a dictionary of all view type identifiers with their associated display icon style identifier and whether the view type supports multi-record display. Form views are marked as single-record views; all others default to multi-record.

[N-U59-025] User preference settings for embedded actions are stored as a child model linked to the user settings record. The order and visibility of embedded actions are stored as comma-separated strings. A method creates or updates the settings record for a given action and record combination.

[N-U59-026] The tour model stores guided onboarding tours with a name, starting address, completion message, and a sequence of steps. Each step carries a trigger expression, optional display text, tooltip position, and an optional run instruction. Tours track which users have completed them via a many-to-many relationship. A tour is considered current when it is not marked custom and the current user has not yet consumed it. A method generates a downloadable JavaScript file that registers the tour in the client module registry.

[N-U59-027] The tour export generates a module script that imports from the core registry and registers the tour steps in a structured format. The generated attachment is served as a downloadable file.

[N-U59-028] A computed field on user records controls whether tours are presented to that user. It is set to true only for administrator accounts when no demo data modules are installed and the application is not running in automated test mode. A method allows the user to toggle the setting. The session information delivered to the browser includes the current tour state for the user.

[N-U59-029] The hierarchy view type adds a new view mode to the action and view records. Views of this type are treated as template-based views. A validator enforces that hierarchy views contain at most one template block and only field or template children, and that only recognised attributes are present. The view type is listed in the view information dictionary with a distinct icon.

[N-U59-030] A hierarchy read method on the base model fetches a set of records matching a domain and enriches the result with child identifier lists derived from a grouped query. For single-record reads it also fetches the parent and sibling records to provide enough context for the hierarchy display. Each result dictionary receives an additional key containing the list of direct child identifiers.

[N-U59-031] The Unsplash image integration adds two configuration fields to the settings model for the API access key and application identifier, both stored in the system parameter store. A search endpoint proxies image search queries to the external Unsplash service using the stored access key, translating error codes to structured error responses. An attachment creation endpoint downloads selected images from Unsplash, validates the image origin, processes them for resolution safety, stores them as binary attachments, and notifies the Unsplash service of each download as required by the API terms. A separate endpoint stores or retrieves the application identifier for public access. Unsplash settings may be managed by users holding the ERP manager or restricted website editor group.
