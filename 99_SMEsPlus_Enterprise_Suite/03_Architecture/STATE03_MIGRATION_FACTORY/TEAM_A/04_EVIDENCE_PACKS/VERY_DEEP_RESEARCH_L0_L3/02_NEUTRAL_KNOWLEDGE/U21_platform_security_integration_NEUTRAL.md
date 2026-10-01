# U21 Platform Security and Integration Surface — NEUTRAL KNOWLEDGE

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Clean-room layer: plain business and process language only (platform: Odoo 19 Community, named once here).
> Each statement carries an identifier in square brackets that links it to restricted technical claims. No file, module, field or code names appear below.
> Scope of this layer: how people and programs prove who they are, how sessions and data channels are protected, how data can be brought in, where secrets are kept, and what leaves the system toward outside services. No completeness, coverage or approval is asserted.

## CAP-U21-01 Second-factor sign-in (authenticator codes and e-mailed codes)

### WHAT
- [N-U21-001] An optional second sign-in step asks for a six-digit one-time code from an authenticator application after the password has been accepted.
- [N-U21-002] Until the code is accepted the visitor holds only a partial pre-session that gives no access to business pages.
- [N-U21-003] A second variant sends the six-digit code to the user by e-mail; it applies to users without an authenticator application when an administrator turns on an enforcement policy.
- [N-U21-004] Users enrol themselves: the system shows a freshly generated secret and a scannable image, and the feature becomes active only when the user types a currently valid code. Nobody can enrol on behalf of another user.
- [N-U21-005] At the code step a user may choose to trust the browser; a long-lived token kept in that browser then skips the code step on later sign-ins from it.
- [N-U21-006] Administrators can send an invitation e-mail that asks users to enable the second step; the link leads to the user's own security settings, or to the portal security page for external users.

### WHY
- [N-U21-007] The second step limits the damage of a stolen or guessed password, because a password alone no longer opens a session.

### BUSINESS RULE
- [N-U21-008] Each authenticator code is single-use: a code that does not come after the last accepted time step is refused. Codes are accepted within one 30-second step either side of the current time.
- [N-U21-009] Code checks are limited to five per hour per user and e-mail sends to five per hour per user; the counters are cleared when a code check succeeds.
- [N-U21-010] Enabling the second step, disabling it, and revoking trusted browsers require the user to have re-entered their credential within the last ten minutes.
- [N-U21-011] Only the account owner may enable the second step. The owner, or an administrator holding the access-rights role, may disable it; disabling also removes every trusted browser of that user.
- [N-U21-012] Enabling or disabling the second step changes the session fingerprint of the user: every other session of that user ends, while the session that made the change continues.
- [N-U21-013] When a user has a second step, the account password no longer works for programmatic access; an API key must be used instead, and API keys do not require the second step.
- [N-U21-014] With the e-mail policy set to employees only, internal users without an authenticator are asked for e-mailed codes; with the all-users setting, portal users are included too.
- [N-U21-015] The e-mailed code is derived from the user identity and last sign-in time (no stored secret), is accepted within a window of one-hour steps (roughly one to three hours), and is not marked as used once accepted.
- [N-U21-016] Trusted-browser tokens last 90 days by default; the length is configurable, and a non-positive or invalid setting falls back to the default with a warning.
- [N-U21-017] Changing one's own password removes all trusted browsers of that user.
- [N-U21-018] With the mail features installed, the user is e-mailed when the second step is activated or deactivated, when a trusted browser is removed, and when a sign-in comes from a browser that is not trusted (for users who have a second factor and an e-mail address).

### STATE
- [N-U21-019] Sign-in: no session, then partial session (password accepted), then full session (code accepted, trusted browser recognised, or the step skipped by a passkey).
- [N-U21-020] Account: not enrolled, then enrolled, then disabled (by the owner or an administrator).

### OPTIONALITY
- [N-U21-021] The feature is installed by default but each user opts in, unless the administrator enforces the e-mail policy; the restored database shows no enforcement policy configured and no enrolled user.

### DEPENDENCY
- [N-U21-022] The e-mail variant, invitations and alerts depend on outgoing e-mail; the portal security page depends on the portal; the web sign-in form drives the step; passkey sign-in bypasses it.

### CONSTRAINT
- [N-U21-023] With the e-mail policy on, a user without an e-mail address cannot receive a code and therefore cannot complete sign-in.
- [N-U21-024] Enrolment and the code step need an active web request; they cannot be carried out from background processes.

### RISK
- [N-U21-025] The authenticator secret is kept unencrypted in a column of the user table, and briefly in a temporary enrolment record; anyone with database or backup access can generate valid codes.
- [N-U21-026] A trusted-browser token lets its holder skip the code step for its whole lifetime; the cookie is set HTTP-only and same-site lax but without the secure attribute at source level.
- [N-U21-027] An administrator can disable another user's second step without a second approver; this is the only recovery path when a user loses the device, because no recovery codes were found.
- [N-U21-028] The rate limit is per user, not per source: someone who knows the password could use up the five hourly code attempts and keep the genuine user from the code step for up to an hour.
- [N-U21-029] API keys and passkeys bypass the second step by design; account strength therefore depends on how those are issued and kept.

### UNKNOWN
- [N-U21-030] Whether the deployment serves sign-in only over a secure channel, and whether a front proxy adds the secure attribute, cannot be determined from source.
- [N-U21-031] The procedure for a lost authenticator device is only the administrator disable action; whether the business wants recovery codes is open.

## CAP-U21-02 Passkey sign-in and credential management

### WHAT
- [N-U21-032] Users can register passkeys, which are device-bound public-key credentials, and later sign in with one instead of typing a password.
- [N-U21-033] Registering requires the user to re-confirm identity first and to name the passkey; the system issues a one-time challenge tied to the session and verifies the device's response.
- [N-U21-034] The credential identifier and public key are stored; the public key is kept outside the ordinary data layer, and the identifier, key and use counter are visible only to administrators.
- [N-U21-035] At sign-in a public endpoint issues a challenge; the browser returns a signed response; the server finds the owner by credential identifier and verifies challenge, origin, relying-party hash, user presence, user verification, counter progress and signature.
- [N-U21-036] A passkey sign-in skips any second step.
- [N-U21-037] A passkey can also be used for identity re-confirmation and becomes the default re-confirmation method when the user has one.

### WHY
- [N-U21-038] Passkeys remove the password from the sign-in and resist phishing because the credential is bound to the site address.

### BUSINESS RULE
- [N-U21-039] Registration requires user verification (biometric or device PIN) and creates a discoverable credential; attestation is not requested, so the make and model of the authenticator is not checked.
- [N-U21-040] The relying-party identity and accepted origin come from the configured system base address; a fixed mobile-application origin is also accepted.
- [N-U21-041] The use counter must strictly increase when either side holds a non-zero counter; a response that does not advance it is rejected as a possible replay, while authenticators that always report zero are tolerated.
- [N-U21-042] The challenge is consumed on first use and is held in the session; no separate short expiry was found in source.
- [N-U21-043] A user may delete only their own passkeys through the delete action; an attempt on someone else's is refused and logged. At the data level administrators holding the access-rights role can read and delete all passkeys.
- [N-U21-044] Adding or removing a passkey changes the user's session fingerprint, ending their other sessions.
- [N-U21-045] Credential identifiers are unique across all users; users may read and rename their own passkeys.

### STATE
- [N-U21-046] Passkey: not registered, then registered by its owner, then renamed any number of times, then deleted.

### OPTIONALITY
- [N-U21-047] The feature is installed by default; each user chooses whether to register a passkey; portal users get an additional management section when the portal is installed. No source setting disables the feature.

### DEPENDENCY
- [N-U21-048] Passkeys depend on the web sign-in form, on a valid system base address, and on a publicly served mobile-application link file.

### RISK
- [N-U21-049] Because a passkey skips the second step, a passkey on a lost or unlocked device gives full access without any code.
- [N-U21-050] The challenge endpoint is public and unauthenticated; the only brake on abuse is the session itself.
- [N-U21-051] A change of the system base address may invalidate existing passkeys because the expected origin changes.

### UNKNOWN
- [N-U21-052] Behaviour of the bundled third-party library with unusual authenticators was not studied beyond the authentication verification path and the registration defaults.

## CAP-U21-03 Browser sign-in, sessions, request-forgery protection and real-time channels

### WHAT
- [N-U21-053] The sign-in page builds credentials from a fixed list of form parameters, defaults the type to password, and reports failures with a generic message.
- [N-U21-054] When a bot-detection service is configured with a secret key, password sign-ins must also pass it; without a secret key the check is skipped.
- [N-U21-055] After the credential check the system creates a partial session when the user has a second step, otherwise a full session at once; a full session receives a new identifier and a validity fingerprint.
- [N-U21-056] Browsers receive notifications through a persistent socket (or polling as fallback); each subscriber is placed on a broadcast channel, the channels of the user's groups and the user's own contact channel.
- [N-U21-057] The default administrator-password warning is pushed to an administrator who signs in with the factory password from a non-private address.

### WHY
- [N-U21-058] Sessions and forgery tokens keep a signed-in browser from being driven by another web page, and the fingerprint lets the system end sessions after security-relevant changes.

### BUSINESS RULE
- [N-U21-059] The session fingerprint is built from user identity, login, password hash and active flag, plus second-factor and passkey data when those features are installed; a change in any of them ends the user's other sessions.
- [N-U21-060] Sessions expire after seven days without activity by default (configurable); the session identifier rotates every three hours; the session cookie is HTTP-only and, at source level, carries no secure or same-site attribute.
- [N-U21-061] State-changing page requests need a forgery token bound to the session and signed with a database secret; its default lifetime is about one year. JSON calls are protected instead by requiring a JSON content type, which forces a cross-origin preflight.
- [N-U21-062] Several endpoints are explicitly exempt from forgery tokens: database management, remote-call endpoints, module upload by password, and one mail add-in endpoint.
- [N-U21-063] Redirect targets are reduced to local paths unless the caller explicitly allows external ones; the mail add-in consent step allows external targets.
- [N-U21-064] A system administrator can switch the current session to the superuser through a dedicated page.
- [N-U21-065] The login failure cooldown, the identity re-check window and the password hashing rules belong to the base platform and are not restated here.
- [N-U21-066] The socket handshake requires an origin header but does not compare it with the host in the default configuration; client-chosen string channels are accepted, so their secrecy rests on being unguessable.
- [N-U21-067] Stored notifications are kept 24 hours by default and then deleted; socket connections are rate limited.
- [N-U21-068] Any request path that matches no page is answered with a stored file whose recorded address equals that path, whatever its sharing flag.
- [N-U21-069] Debug mode can be switched on through a request parameter and then stores in the session; error pages then include the technical trace.

### STATE
- [N-U21-070] Session: none, then partial (waiting for second step), then full, then rotated, then ended (logout, expiry or fingerprint change).

### OPTIONALITY
- [N-U21-071] Bot detection, session lifetime, forgery token lifetime and the cross-site socket downgrade are controlled by settings or environment options; the restored database shows bot detection switched on in principle but without keys.

### DEPENDENCY
- [N-U21-072] Sign-in depends on the base platform user rules; the real-time channel depends on a long-running socket service and on the database notification mechanism.

### CONSTRAINT
- [N-U21-073] Forgery tokens need a configured database secret; without one the system raises an error.

### RISK
- [N-U21-074] Without a secure attribute and an explicit same-site setting at source level, session cookie protection depends on the front proxy and browser defaults.
- [N-U21-075] Logout is reachable by a plain link request without a forgery token, so another page can sign a user out.
- [N-U21-076] The unmatched-path file fallback publishes any stored file whose recorded address equals the requested path; files imported with packages are flagged public and are therefore reachable this way.
- [N-U21-077] The company logo endpoint reads the logo straight from the database for any company number requested by an unauthenticated visitor, with open cross-origin access.
- [N-U21-078] A version endpoint is public and discloses the server version; a health endpoint is public as well.
- [N-U21-079] Any session, including a public one, may enable debug mode by parameter; the technical trace on error pages may then expose internals.
- [N-U21-080] Subscribing to a guessable string channel would expose its notifications; the channels created by the base features use records or random values.

### UNKNOWN
- [N-U21-081] Whether the cross-site socket downgrade option and the secure cookie attribute are configured in the target deployment cannot be determined from source or from the restored database.

## CAP-U21-04 Programmatic access (remote calls, API keys, documentation, database service)

### WHAT
- [N-U21-082] Remote-call endpoints accept a database name, user number and password or API key with every call and run the requested operation with that user's rights; the older XML and JSON variants are marked deprecated and scheduled for removal.
- [N-U21-083] A newer JSON endpoint takes a bearer API key, a model name and an operation name; only public operations are callable, parameters are checked against the operation signature, and no session is kept.
- [N-U21-084] A JSON view endpoint returns what a screen would show, and requires the data-export right.
- [N-U21-085] The web client calls any public operation of any model through a session-authenticated endpoint.
- [N-U21-086] A technical documentation site lists models, fields and operations visible to the caller, and a playground to try operations.
- [N-U21-087] A database-management service creates, duplicates, drops, backs up, restores databases and changes the master password; each request carries the master password.
- [N-U21-088] Data exports to CSV or spreadsheet files are produced for users holding the export right (or administrators).

### WHY
- [N-U21-089] External systems and administrators need a supported way to read and write business data and to manage databases without the browser.

### BUSINESS RULE
- [N-U21-090] A user holding a second step cannot use the password for remote calls; only an API key works, and an API key is also required when the account is configured as key-only.
- [N-U21-091] API keys are random 20-byte values stored as hashes with an index prefix; non-administrators must give an expiry no longer than the longest duration allowed to their groups (employees 90 days by default); administrators may create keys without expiry; keys have an optional scope, and a key without scope works for any remote call.
- [N-U21-092] Managing API keys programmatically is off by default and capped at ten live keys per user when on; administrators are exempt from the on-off setting.
- [N-U21-093] The documentation requires the technical-documentation role, which administrators imply; it lists only models and fields the caller may read, caches the index per role combination in a private stored file and deletes outdated ones automatically.
- [N-U21-094] Database creation, duplication, drop, backup, restore and master-password change require the master password; if the master password is still the factory default, the first request that supplies any password sets it.
- [N-U21-095] Export files prefix cells that begin with formula characters so spreadsheet programs do not execute them; grouped export to CSV is refused.
- [N-U21-096] Public operations are callable by any authenticated caller; the platform does not add a model-level permission check at this layer, so each operation must protect itself.

### STATE
- [N-U21-097] API key: created, used, expired or revoked or deleted by the automatic cleanup. Master password: factory default, then set by first caller, then changed on demand.

### OPTIONALITY
- [N-U21-098] The remote-call module and the documentation module are installed automatically; the database-list display and the master password come from server configuration, which was not available.

### DEPENDENCY
- [N-U21-099] Remote calls depend on the user rules of the base platform and on the second-step rules; the documentation depends on the web client.

### CONSTRAINT
- [N-U21-100] Bearer calls must name an existing model and a public operation, supply valid parameters, and may not pass record numbers to model-level operations.

### RISK
- [N-U21-101] The legacy XML endpoints return the full technical trace in the fault for non-user errors.
- [N-U21-102] The database-management forms are exempt from forgery tokens and protected only by the master password; the factory default password is the string used by the manager's own insecurity check, and the default configuration lists databases.
- [N-U21-103] A backup request returns a full dump including files to anyone who knows the master password.
- [N-U21-104] An operation that purges and reloads translation caches runs raw database statements and is callable remotely by any authenticated user; the effect is limited to cache data but shows the exposure pattern.
- [N-U21-105] Version information endpoints are public.

### UNKNOWN
- [N-U21-106] The configured master password value, the database-list setting, the reverse-proxy rules limiting these routes and any rate limiting upstream cannot be determined from source or from the restored database.

## CAP-U21-05 Data import (spreadsheet-style files and data-module packages)

### WHAT
- [N-U21-107] An import wizard lets internal users load comma-separated, spreadsheet or open-document files into any model they may create records in; it previews the file, proposes column-to-field mapping, supports a dry run, and then loads.
- [N-U21-108] An administrator-only package import loads a zip file that contains data files, static files, translations and a manifest for a data package, and an upload form can post such a zip with login and password.
- [N-U21-109] Industry data packages can be downloaded from the vendor's public store and then loaded.

### WHY
- [N-U21-110] Bulk loading speeds up migration and set-up; data packages let partners ship configuration without code.

### BUSINESS RULE
- [N-U21-111] A load runs with the rights of the importing user: model access and record rules decide whether creating or changing is allowed; only writable fields are offered for mapping.
- [N-U21-112] A dry run performs every check and then rolls the changes back.
- [N-U21-113] The wizard record is private to its creator and expires after 12 hours; mapping memory (column name to field name) is saved for later suggestions and is shared by all internal users with full rights over it.
- [N-U21-114] A binary field may be filled from a web address only when the importer is an administrator, within a size limit (10 megabytes by default) and a short timeout (3 seconds by default).
- [N-U21-115] The file format is chosen from the detected content type, the browser-supplied type and the extension, in that order.
- [N-U21-116] Package import accepts only data files with xml, csv or sql extensions plus static files and translation files; package static files become public stored files.
- [N-U21-117] The package upload form accepts a login and password, signs in, and proceeds only if a full session results and the user is an administrator; with a second step configured the sign-in stays partial and the upload is refused.

### STATE
- [N-U21-118] Import: file uploaded, preview, mapping adjusted, dry run, real load, result with messages. Package: uploaded, dependencies installed, data loaded, flagged as imported.

### OPTIONALITY
- [N-U21-119] The import wizard is a switchable feature of the general settings; the package import is installed by default and visible to administrators.

### DEPENDENCY
- [N-U21-120] The wizard uses the standard load mechanism of the platform and, for web addresses, outside network access; package loading uses the platform's data loader and the vendor store for industry packages.

### CONSTRAINT
- [N-U21-121] Uploads in package import are limited to 100 megabytes per file; packages must have a manifest and resolvable dependencies; unknown dependencies abort the import.

### RISK
- [N-U21-122] The package upload form is open to the network, exempt from forgery tokens and uses password sign-in; its gate is the access-rights role while the wizard version requires the full administrator role, so the two doors differ.
- [N-U21-123] Package data files with the sql extension are executed as raw database statements, and xml files are loaded with elevated rights, so a package is equivalent to code.
- [N-U21-124] Fetching a web address from an administrator import can reach internal network hosts because only the scheme is restricted by default.
- [N-U21-125] Mapping memory is writable by every internal user and can be altered to mislead later suggestions.
- [N-U21-126] The import can create or modify records of any model the user can write, including the external identifiers that other imports key on.

### UNKNOWN
- [N-U21-127] Whether any data package was imported in production is not determinable; the restored database shows none.

## CAP-U21-06 Certificate and key storage

### WHAT
- [N-U21-128] Administrators can store certificates and cryptographic keys per company: certificate files in several formats and private or public keys, each with an optional password.
- [N-U21-129] The system extracts the readable certificate, validity dates and subject name, links a matching private key, builds the issuer chain, and can sign data with the key.
- [N-U21-130] A certificate-based client can present a stored certificate and key when calling an outside service.

### WHY
- [N-U21-131] Electronic documents and secure service calls need keys and certificates held in one controlled place.

### BUSINESS RULE
- [N-U21-132] Only the full administrator role may read, create, change or delete certificates and keys; visibility is limited to the user's companies plus records shared by all companies.
- [N-U21-133] Certificate and key must match, a certificate must be loadable, and a certificate must be within its validity period to sign.
- [N-U21-134] When a certificate file holds a private key, the key is extracted into a separate key record in unencrypted form.
- [N-U21-135] Missing issuer certificates found in an uploaded chain are created automatically as further certificates.

### STATE
- [N-U21-136] Certificate: loaded, valid, expired, archived. Key: loaded or in error, archived.

### OPTIONALITY
- [N-U21-137] The capability is a supporting library with no automatic installation; in the restored database it is present because several electronic-document features depend on it, and it holds no certificate and no key.

### DEPENDENCY
- [N-U21-138] Consumers are electronic-document features of country packages; the outbound-client adapter patches network client libraries process-wide.

### CONSTRAINT
- [N-U21-139] Password fields are plain text fields; the database neutralisation script resets them to a dummy value.

### RISK
- [N-U21-140] Private keys and their passwords are stored without encryption in the database and in the file store; a certificate password protects only the uploaded file, not the extracted copy.
- [N-U21-141] Anyone with database, file store or backup access can use the keys; a neutralised copy is the only built-in protection for test copies.

### UNKNOWN
- [N-U21-142] Which installed features consume these records, and how they protect the signing action, belongs to other units.

## CAP-U21-07 Third-party account links (calendar synchronisation and mail-server sign-in)

### WHAT
- [N-U21-143] Users can link their personal Google or Microsoft calendar; the system exchanges the authorization for tokens and then synchronises events both ways.
- [N-U21-144] Administrators can link outgoing and incoming mail servers to Google or Microsoft mailboxes by the same kind of authorization; the system then sends or fetches mail using the access token.
- [N-U21-145] A scheduled job synchronises every linked calendar every 12 hours; users can also trigger a sync from the calendar screen.

### WHY
- [N-U21-146] Employees keep one calendar and the company can send mail from accounts that require modern sign-in.

### BUSINESS RULE
- [N-U21-147] The client identifier and secret of each provider are system parameters set by administrators; the identifier is not secret, the secret is used only for server-to-server requests.
- [N-U21-148] Access tokens are refreshed when less than one minute of validity remains; a rejected refresh clears the stored tokens and asks the user to link again.
- [N-U21-149] Events sent outward carry title, description, location, start and end, attendee e-mail addresses and answers, organiser e-mail, reminder settings and, for Google, a marker with the database name and record number; events from the outside are matched, and for Google the most recently changed side wins.
- [N-U21-150] Mail-server links verify a state value protected by a signature bound to the record, and for outgoing servers that are personal, or linked by someone who is not a full administrator, the mailbox address must match the address the provider reports.
- [N-U21-151] Mail sign-in asks the provider for full mailbox access for Google and for send or read access for Microsoft; tokens are used with the standard token-based sign-in of mail protocols.
- [N-U21-152] Where the vendor relay is not available (the open-source edition), servers cannot be linked without the administrator's own provider credentials.

### STATE
- [N-U21-153] Link: not linked, linked (tokens stored), paused or stopped, relinked after rejection or after account reset.

### OPTIONALITY
- [N-U21-154] Calendar synchronisation can be paused system-wide or stopped per user; the restored database has the schedule jobs active but no provider credentials and no stored tokens.

### DEPENDENCY
- [N-U21-155] Depends on the calendar and mail features, on outside provider services reachable from the server, and on the system base address for the return address.

### CONSTRAINT
- [N-U21-156] Outgoing requests to the calendar providers are restricted to a short list of provider hosts by an assertion; mail-server links require secure connection settings.

### RISK
- [N-U21-157] Google calendar tokens live as plain text in the per-user settings table and Microsoft calendar tokens as plain text columns of the user table; mail-server tokens live as plain text on the server record; field-level rights limit them to administrators, but database and backup readers can use them.
- [N-U21-158] The calendar return endpoint is public and carries no signed state; an attacker able to induce a signed-in victim to open a crafted link could bind an attacker's calendar to the victim's account.
- [N-U21-159] The mail-server return state is signed per record but not per user or session, and the tokens for the vendor-relay variant arrive in the browser address.
- [N-U21-160] Microsoft requests are logged at debug level with their parameters, which include the secret and refresh token; Google requests mask the secret.
- [N-U21-161] The Google calendar access token is sent as a query parameter on read and delete requests, so it can appear in proxy or provider logs.
- [N-U21-162] Outbound calendar content includes attendee personal data and meeting descriptions that leave the system to the provider.
- [N-U21-163] The neutralisation script clears tokens in copies of the database.
- [N-U21-234] When no own provider credentials are configured, refreshing a mail-server token sends the refresh token and the database identifier to the vendor relay service.

### UNKNOWN
- [N-U21-164] Whether secrets are provided by system parameters in the target environment, and the behaviour of the provider services (rate limits, token lifetime), cannot be determined from source.

## CAP-U21-08 Other outbound service calls and add-in access

### WHAT
- [N-U21-165] Bot detection (reCAPTCHA) sends the visitor's token and address to Google for scoring when a secret key is configured.
- [N-U21-166] Address geolocation sends a postal address to OpenStreetMap or Google, and reverse lookup sends coordinates to OpenStreetMap.
- [N-U21-167] Address autocomplete sends the partial address text typed by an internal user to Google Places and uses the company's key.
- [N-U21-168] A mail add-in lets an internal user link a mailbox add-in through a consent page that issues a short-lived code, which the add-in exchanges for a 30-day API key; the add-in can search and create contacts, enrich companies through the vendor service and log mail content on contacts.
- [N-U21-169] The translation helper only builds links to the translation platform and never calls it.
- [N-U21-170] The module store listing sends the version series, filter and search terms to the vendor store; industry downloads fetch a package from it.

### WHY
- [N-U21-171] These features add convenience (spam control, map coordinates, faster address entry, mailbox integration) at the cost of sending some data to outside providers.

### BUSINESS RULE
- [N-U21-172] Bot detection fails closed on invalid token, low score or timeout when a secret key exists; with no secret key it is silently off.
- [N-U21-173] Address autocomplete never uses the key for public visitors; the detailed lookup requires an internal user.
- [N-U21-174] Geolocation starts only from an explicit user action and is skipped during imports and installation; the default provider is OpenStreetMap, which needs no key.
- [N-U21-175] The add-in consent code is valid three minutes and is signed; the resulting key expires after 30 days by default and belongs to the consenting user, who must be internal.
- [N-U21-176] By default the add-in logs mail only on contacts and only through the user's own rights.

### STATE
- [N-U21-177] Add-in key: consent shown, code issued, key exchanged, expired or revoked.

### OPTIONALITY
- [N-U21-178] All of these features are inert without keys or user action; geolocation provider and keys are administrator settings; bot detection and the add-in can be disabled by not configuring them.

### DEPENDENCY
- [N-U21-179] They depend on outside networks; enrichment depends on the vendor credit service.

### CONSTRAINT
- [N-U21-180] Address autocomplete needs a minimum input length (five characters by default) and has a 2.5-second timeout.

### RISK
- [N-U21-181] The geolocation call to OpenStreetMap has no timeout and sends full postal addresses of customers; the autocomplete sends text typed by employees; both can leak personal data to third parties.
- [N-U21-182] The consent redirect can send the signed code to any external address chosen by the caller, so the consent page is the only protection against a hostile add-in.
- [N-U21-183] The add-in endpoints are open to any origin and authenticated only by the issued key; the key is scoped so it cannot be used for general remote calls, but through the add-in endpoints it acts with the user's rights.
- [N-U21-184] The add-in lets a user create contacts and log arbitrary message bodies on contacts using the key.
- [N-U21-233] The web client offers a link to the vendor's account service built from the database identifier, the system address and the database name.

### UNKNOWN
- [N-U21-185] Which of these features the business enables, and whether the contractual terms for the outside providers permit the data sent, is open.

## CAP-U21-09 Spreadsheet formulas, dashboards and sharing

### WHAT
- [N-U21-186] Dashboards are stored spreadsheets shown to users; each dashboard names the roles allowed to see it and optionally the companies; ready-made dashboards exist for invoicing, sales, warehouse, expenses, events, live chat and timesheets.
- [N-U21-187] Accounting formulas let a spreadsheet read debit, credit, balance, residual and partner balance totals for chosen accounts, periods and partners.
- [N-U21-188] A user can share a frozen copy of a dashboard through a link that contains a secret token and is readable without signing in.

### WHY
- [N-U21-189] Management wants live figures in familiar spreadsheet form, and occasionally to give a snapshot to people outside.

### BUSINESS RULE
- [N-U21-190] Employees see only dashboards whose allowed roles overlap their own; dashboard administrators see all; dashboards limited to companies follow the user's active companies, and dashboards with no company are visible everywhere.
- [N-U21-191] Dashboard figures come from live reads performed with the viewer's own rights; a viewer without rights on the underlying data gets no figures or an error rather than someone else's view.
- [N-U21-192] Accounting formulas read journal lines through the standard aggregation with the caller's rights, filter by company, posted state (unposted only when asked), period and partners.
- [N-U21-193] A shared copy holds data computed in the sharer's browser at sharing time; access needs the token, and the sharer must still have read rights on the dashboard at access time; downloading the spreadsheet file needs the export right.
- [N-U21-194] Exports, copies, freezes and prints of spreadsheet data, as reported by the browser, are written to the server log with user, source model, fields, grouping, filters and source address.
- [N-U21-195] A dashboard shows sample data when the main source has no records.

### STATE
- [N-U21-196] Dashboard: published or unpublished; favourite per user. Share: created, accessed by token, deleted with its dashboard.

### OPTIONALITY
- [N-U21-197] The base library is a dependency of dashboards; each ready-made dashboard installs with its business area; four further dashboard packages (point of sale, restaurant, shop and online courses) are present in source but not installed here.

### DEPENDENCY
- [N-U21-198] Dashboards depend on business modules whose models they query; sharing depends on the portal layout.

### CONSTRAINT
- [N-U21-199] Dashboard content must be valid spreadsheet data; invalid content is refused; deletion of a dashboard group supplied by a package is blocked.

### RISK
- [N-U21-200] Any employee can create a share for any dashboard number because creation rights are broad; the token and the sharer's own read right at access time then govern access.
- [N-U21-201] The shared copy's content is whatever the sharer's browser submitted, so it is not verified by the server and can contain data the sharer was able to see at that time, persisting after the sharer loses access to the live data until the share is removed.
- [N-U21-202] A helper that returns display names for any list of records works with the caller's rights but accepts arbitrary models.
- [N-U21-203] The restored database holds ten dashboards, none company-restricted, and no shares; several are limited to the administrator role of their business area.

### UNKNOWN
- [N-U21-204] Client-side formula evaluation and the exact set of data sources used by each ready-made dashboard were not read.

## CAP-U21-10 Privacy lookup and erasure, and small platform utilities

### WHAT
- [N-U21-205] Administrators can search the whole database for personal data linked to a name or e-mail address, list the matching records, archive them or delete them, and keep a log of what was done.
- [N-U21-206] Internal users can ask the administrators, by e-mail, to install an app; administrators can review and install it.
- [N-U21-207] Onboarding panels track set-up steps per company; guided tours can be defined by administrators and consumed once per user.
- [N-U21-208] A built-in chat bot welcomes internal users and teaches basic chat features; it makes no outside calls.
- [N-U21-209] Barcode rules and nomenclatures interpret scanned codes, including GS1 element strings.
- [N-U21-210] Bank account numbers are validated as international account numbers for many countries.
- [N-U21-211] Attachment indexing extracts text from office and PDF files for search.
- [N-U21-212] A hierarchy view reads parent and child records.
- [N-U21-235] The contacts app adds only a menu entry and an activity icon on top of the contact records; it declares no permissions of its own.

### WHY
- [N-U21-213] Privacy law requires finding and removing personal data; the utilities support everyday set-up and scanning.

### BUSINESS RULE
- [N-U21-214] The privacy search runs as raw database queries across all models, ignoring record rules and company restrictions, and only the full administrator role may use it; deleting a line permanently removes the record with elevated rights.
- [N-U21-215] The privacy log stores a masked form of the name and address, who handled the request, the actions taken and a description of the found records.
- [N-U21-216] App installation requests go to all full administrators; only the full administrator role can approve and install.
- [N-U21-217] Guided tours and onboarding progress are written by administrators; users mark tours consumed for themselves.
- [N-U21-218] International account numbers are checked for country, length and checksum only for accounts classified as such; other strings are saved as ordinary bank accounts.
- [N-U21-219] Barcode rules and nomenclatures are maintained by the access-rights role; all internal users can read them; with GS1 active, exact barcode searches are widened to partial matches on the unpadded code.
- [N-U21-220] Attachment indexing parses uploaded file content on the server and stores the extracted text with the attachment.

### STATE
- [N-U21-221] Privacy case: lookup, selection, archive or delete, logged. App request: sent, reviewed, installed.

### OPTIONALITY
- [N-U21-222] Each utility is an installed module; the privacy search and the request feature are always visible to their roles; the restored database holds no log entries.

### DEPENDENCY
- [N-U21-223] Privacy search needs every other module's tables; app requests need outgoing e-mail; chat bot needs the chat feature.

### CONSTRAINT
- [N-U21-224] Privacy deletion cannot be undone; protections that run on deletion at model level still apply, so posted accounting records are expected to be protected, which was not verified here.
- [N-U21-225] Barcode matching patterns are administrator-supplied regular expressions run on scanned input.

### RISK
- [N-U21-226] Privacy deletion with elevated rights ignores record rules and company limits and could damage referenced data where a model has no deletion guard; no extra confirmation or second approver was found.
- [N-U21-227] When an e-mail address is invalid the privacy log helper returns an error object instead of raising it, so the log field receives an unexpected value.
- [N-U21-228] Administrator-supplied barcode patterns could be slow on crafted input.
- [N-U21-229] Office-file indexing parses untrusted files, so a hostile file could cost server time.
- [N-U21-230] Guided-tour steps contain instructions executed in the user's browser; only administrators can write them.
- [N-U21-231] Employees can read the list of installable apps.

### UNKNOWN
- [N-U21-232] Whether privacy requests are handled in production, the retention of the log, and whether the business needs a four-eyes rule for deletion, is open.
