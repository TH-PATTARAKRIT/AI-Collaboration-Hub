# U52 neutral knowledge — mail: templates, rendering, composition, aliases, followers, notifications

> Neutral knowledge layer. DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> No snake_case, no dotted names, no file extensions, no backticks, no path tokens, no code keywords.

---

[N-U52-001] An email template system lets users define reusable message structures that are tied to a specific type of business record. When a message is sent, the template fields are resolved against the target record to produce a personalized email.

[N-U52-002] Template rendering is subject to a security gate. When a template contains expressions that reach beyond simple field access into arbitrary code evaluation, only users in a designated Template Editor group are allowed to save or modify that template. System administrators bypass this gate. The gate is configurable per model: some models explicitly opt out of the restriction and allow any authenticated user to edit their templates.

[N-U52-003] Every template field that can contain placeholders — subject, sender address, recipient addresses, reply-to, language selector, scheduled date, and body — is treated as a dynamic field. These are the only fields that are evaluated per-record at send time; other fields carry static values.

[N-U52-004] The body of an email template is processed through a structural template engine. After rendering, relative links in images, hyperlinks, and CSS background styles are automatically converted to absolute URLs so that email clients can fetch the resources correctly.

[N-U52-005] A template can optionally specify a notification layout to wrap the rendered body. This layout adds a standard header, footer, company branding, and action button around the core message content.

[N-U52-006] By default, email records generated from a template are deleted from the database after sending to save storage space. This behavior can be turned off. In the composition wizard, the deletion default depends on whether the message is a direct post on a record or a mass mailing.

[N-U52-007] Templates are classified into three categories: base templates are active and have both a description and a system-defined identifier; hidden templates are either inactive or lack a description while having a system identifier; custom templates are user-created without a system identifier.

[N-U52-008] When a template is saved, the system runs a trial render against a sample record of the target model to verify that all dynamic fields parse without error. Saving a template against an abstract model is blocked entirely.

[N-U52-009] A template cannot be created for an abstract data model. The system raises a validation error at save time if the chosen model has no concrete records.

[N-U52-010] Templates can attach both static files and dynamically generated reports. Dynamic reports are produced by the report engine for each target record at send time and attached as named binary files. Models can also inject additional computed attachments through an optional hook method.

[N-U52-011] When the default recipients option is enabled on a template, the system uses the record's own recipient fields rather than the explicit address fields on the template. This is the default mode.

[N-U52-012] Template rendering is orchestrated by a central method that coordinates multiple specialized sub-methods: one for ordinary fields, one for recipients, one for scheduled dates, one for static configuration values, and one for attachments. The result is a dictionary of rendered values per record.

[N-U52-013] Language resolution is a per-record process. If the template contains a language expression, it is evaluated against each record to obtain the appropriate language code. If no expression is set, the language of the record's primary contact is used. Records are then grouped by language, and the template is applied in each language group separately with the correct translations.

[N-U52-014] The public single-record sending method is a thin wrapper that delegates to the batch version. The batch version calls the rendering engine, creates the outgoing message records, optionally applies a layout wrapper, and initiates delivery either immediately or through a queue.

[N-U52-015] Mass sending uses a configurable batch size to avoid memory and transaction overload. The batch size defaults to fifty records per iteration and can be overridden through a system parameter.

[N-U52-016] A template can be bound to its target model as a sidebar action, allowing users to trigger a mass send directly from any list view of that model. The action opens the composition wizard in mass mailing mode with the template pre-selected.

[N-U52-017] The rendering infrastructure lives in a shared abstract mixin that is inherited by all rendering-capable models. By default this mixin applies the security gate; individual models can override the flag to opt out.

[N-U52-018] Before executing a template that contains arbitrary expressions, the system inspects whether each expression is allowed for the target model. For structured templates this uses the template engine's own expression allowlist. For string-based templates it checks each extracted expression individually.

[N-U52-019] The rendering context always includes the current user, the current environment, the execution context dictionary, and a set of formatting helpers for dates, times, monetary amounts, durations, and addresses.

[N-U52-020] Three rendering engines are available: a string-based inline engine that uses a simple placeholder syntax, a structural engine that processes annotated markup, and a view-reference engine that renders a named template stored in the interface view registry. For simple field-access expressions that pass the safety check, a lightweight path-traversal renderer is used that avoids any code evaluation.

[N-U52-021] The string-based inline engine resolves placeholders in the format of opening and closing brace pairs. A fallback value can be specified using a separator. After evaluation, the result is a plain string.

[N-U52-022] The view-reference engine resolves a named or numbered view from the interface registry and renders it against the record. Rendering failures produce a user-friendly error rather than a raw traceback.

[N-U52-023] Post-processing converts all relative resource references in the rendered HTML — images, links, and backgrounds — to absolute URLs. The base URL is fetched once from configuration and cached for the duration of the operation.

[N-U52-024] Layout encapsulation builds a context that includes the message body, the linked record, the company, the message subtype information, display flags for header and footer, and optional action button details. This context is passed to the layout view for rendering.

[N-U52-025] A preview text can be prepended to the rendered body as a hidden block. Most email clients display this text in the message list below the subject line.

[N-U52-026] The placeholder assistant helps users build expressions by selecting a main field and an optional related field. The resulting expression follows the object-dot-field pattern used by the inline template engine.

[N-U52-027] The message composition wizard is a temporary record that is discarded after use. It supports two modes: posting a message on one or more records, and sending mass email to many records using template-resolved content.

[N-U52-028] In the composition wizard, the body field also uses the structural rendering engine with post-processing enabled, matching the behavior of the template body field.

[N-U52-029] The composition wizard respects the email blacklist by default. This prevents sending to addresses that have been opted out. The protection can be disabled for specific use cases.

[N-U52-030] In mass mailing batch mode, the system checks a configurable threshold to decide whether to send immediately or queue. The default threshold is one hundred records.

[N-U52-031] When sending, the wizard distinguishes between comment mode and mass mail mode. Comment mode calls the record's message post method to create a chatter entry and trigger follower notifications. Mass mail mode creates standalone outgoing email records directly, bypassing the chatter.

[N-U52-032] In comment mode, replies can be configured to flow back into the document's chatter or to a separate address. A forward option in comment mode automatically skips notifying existing followers.

[N-U52-033] In mass mail mode, separate notification tracking records are created alongside the outgoing email records so that delivery status can be monitored per recipient. If the delete-after-send option is active without log retention, no tracking records are created.

[N-U52-034] Messages can be scheduled for future delivery in single-record comment mode. A scheduled message record is created to hold the content; it requires an explicit date and stores a cleaned copy of the execution context.

[N-U52-035] A user composing a message can save the current content as a new email template. The save action records the body and optionally transfers attached files from the wizard to the new template.

[N-U52-036] Orphaned attachment records created during composition but not linked to a final message are cleaned up automatically by a background routine. Records older than one day with no associated wizard are removed.

[N-U52-037] An email alias maps an incoming email address to a specific type of record. When an inbound message arrives at a known alias, the system creates a new record of the specified type (or routes to an existing one). Each alias is associated with a domain and an optional default set of field values for new records. Alias names must use only standard ASCII characters as defined by the relevant internet addressing standard.

[N-U52-038] The default field values for new records created by an alias are stored as a text representation of a dictionary and validated as a safe literal at save time.

[N-U52-039] An alias can be locked to a specific existing record. When locked, all inbound mail is attached to that record rather than creating new ones. A local-part-only detection mode is also available for specialized routing scenarios.

[N-U52-040] Three access levels control who may post to a given alias: anyone, authenticated partners only, or existing followers of the related document only. A custom bounce message can be defined for users who are not authorized to post.

[N-U52-041] Alias names are normalized at save time. Only standard ASCII letters, digits, and certain punctuation characters are permitted in the local part of an alias address.

[N-U52-042] Alias names cannot conflict with the domain's bounce or catchall addresses. In a multi-company setup, the alias domain must be compatible with the company of the owner record and any explicitly targeted record.

[N-U52-043] The alias status field tracks whether the alias configuration has been validated. It is automatically reset to untested whenever the routing configuration changes.

[N-U52-044] An email domain model stores the shared domain used for all aliases in a company. This is a structured record rather than a configuration parameter, enabling domain management per company.

[N-U52-045] Each domain record defines a bounce address for undeliverable mail and a catchall address for catching all replies. Both must be unique within the same domain.

[N-U52-046] A default sender address is configured on the domain for situations where no outgoing server filter matches. This can be either a full address or just the local part.

[N-U52-047] Two mixin variants are available for models that need an email alias. The strict variant always creates an alias and exposes its fields directly through delegation. The optional variant creates an alias only when a name is provided, keeping the alias absent for records that do not need one. Both variants expose the same writable alias fields.

[N-U52-048] When an alias is created alongside a record, it is created with elevated privileges to avoid access control issues. Company context is used to select the correct domain.

[N-U52-049] The followers table records which partners have subscribed to which documents. It does not track access events. The document model is stored as a text name rather than a foreign key for performance reasons.

[N-U52-050] Each follower subscription records which message categories the partner has opted to receive. Notifications are only sent for subscribed categories.

[N-U52-051] When a follower record is added, changed, or removed, the cache for the affected documents is invalidated because follower status affects access rights.

[N-U52-052] Recipient data for notifications is fetched in a single optimized query. The query identifies followers of the target documents that subscribe to the relevant message category, then fetches their contact details, user type, notification preference, and group memberships. Three query paths handle different combinations of records and explicit partner lists.

[N-U52-053] When a user has no explicit notification preference set, email delivery is assumed.

[N-U52-054] Recipients are classified into three types based on their user status: internal users, portal users, and customers without any user account. Group memberships are expanded to include all transitively implied groups.

[N-U52-055] Each notification record links a message to a specific recipient, recording both the delivery channel (inbox or email) and the current delivery status.

[N-U52-056] The notification lifecycle has seven states: ready to send, processing by an intermediary, sent (used by the short message channel), delivered, bounced, exception, and cancelled. The sent and delivered distinction is relevant mainly for the short message channel; email uses delivered for final success.

[N-U52-057] Eleven specific failure categories cover invalid or missing addresses, sender address problems, connection failures, blacklisted addresses, opted-out recipients, and deduplicated sends.

[N-U52-058] Database constraints and indexes are used to enforce data integrity and optimize common lookup patterns. Inbox notifications require a recipient partner. A partial index accelerates failure lookups filtered by author.

[N-U52-059] Creating notification records requires at least read access to the linked message. Updating the message or recipient of an existing notification is restricted to administrators.

[N-U52-060] A periodic cleanup routine removes old read notifications for internal partners that have been successfully delivered or cancelled, keeping only notifications newer than a configurable age threshold. The web interface filters notifications to show only those that are relevant for display.

[N-U52-061] A set of web controller routes handle incoming requests from notification email links. The main route accepts the model and record identifier and redirects the user to the appropriate record view, handling authentication, multi-company context, and access control transparently.

[N-U52-062] A one-click unsubscribe route allows email recipients to remove themselves from a document's follower list without logging in. The route is protected by a token validation to prevent unauthorized unsubscription.

[N-U52-063] Token validation uses a constant-time comparison function to prevent timing-based attacks.

[N-U52-064] When redirecting to a record, the system reads the user's active company list from a browser cookie. If the current company list does not grant access, the system suggests the required company and updates the cookie before retrying. The backend URL format uses the model name directly if it contains a dot, otherwise adds a model prefix.

[N-U52-065] During large mass mail operations run by the scheduler, the system periodically commits progress and reports completion counts so that the scheduler can track and resume the job if interrupted.

[N-U52-066] Copying a template also copies its attached files so that the original and the copy have independent attachment records, while the file content is stored only once.

[N-U52-067] Only two rendering options are recognized: one to activate link post-processing and one to preserve comment nodes in the output. Any other option is rejected with an error.

[N-U52-068] Old-format notification links that carry a message identifier rather than a record identifier are still supported for backward compatibility. The system looks up the message and extracts the linked record.

[N-U52-069] When the composition wizard is used in single-record comment mode, it computes whether any of the followers who will receive a silent copy are external contacts. This is shown as a warning in the interface.

[N-U52-070] The scheduled date field of a template is rendered per-record, then parsed and stored as a timezone-agnostic value in coordinated universal time.

[N-U52-071] Subscription data can be fetched in bulk for multiple documents in a single database query, optionally including partner sharing status and active flag.

[N-U52-072] When mass mailing deletes email records after sending, a separate option allows keeping a copy of the message body as a log entry in the chatter, providing a trace without storing the full email envelope.

[N-U52-073] When a structural template fails to render, the template source is stripped from the error before presentation to the user to avoid exposing potentially sensitive template content in error messages. An invalid address in mass mail mode produces a silent cancellation or an exception status depending on whether log retention is active.

[N-U52-074] The notification store projection includes a conditional display name for the recipient partner: the display name is only included when the partner has no name value, ensuring the most readable identifier is always available.
