# U37 base family, bus, calendar and cloud storage — NEUTRAL KNOWLEDGE

> Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**
> Clean-room neutral layer for Odoo 19 Community (revision 19.0.post20260921). Plain business statements only; each statement carries an id linked to claims in the restricted layer.


## CAP-U37-01 Contact directory application

**WHAT**
- [N-U37-001] A stand-alone address-book application lists customers, vendors and other contacts in one place, with list, card, form and activity-planning layouts, and offers it as a tile on the home screen.

**WHY**
- [N-U37-002] A directory of contacts is needed before any sales, purchasing or marketing application is installed, so employees can keep partner records without adopting a larger application.

**BUSINESS RULE**
- [N-U37-003] New records started from the directory default to being a company rather than a person.
- [N-U37-004] The directory entry is shown to internal users and to users holding the contact-management role; what each user may read or change is still governed by the access rights of the contact records themselves, not by the menu.
- [N-U37-005] Maintenance lists for contact tags, industries, countries, states, country groups, banks and bank accounts sit in a configuration area reserved for system administrators.
- [N-U37-006] When a contact record is opened from elsewhere, the directory is offered as the preferred home menu for that record, provided the user can see it.
- [N-U37-007] Contact-related activities in the activity indicator show the directory application icon instead of a generic icon.

**OPTIONALITY**
- [N-U37-008] The only demonstration content is one sample message with a scheduled notification on a demonstration contact, and the examined database was built without demonstration content.

**DEPENDENCY**
- [N-U37-009] The directory needs only the core platform and the messaging module; customer-relationship, mass-mailing and the mail-client plug-in modules require it, so installing them brings it in.

**RISK**
- [N-U37-010] The application adds no data model, rules or validations of its own; every data-protection, uniqueness and access behaviour of contacts comes from the shared contact record, which is outside this study.

**UNKNOWN**
- [N-U37-011] Whether the menus and layouts behave as declared for each role was not exercised at run time.


## CAP-U37-02 Address geolocation

**WHAT**
- [N-U37-012] A contact's postal address can be converted to latitude and longitude by an external geocoding service, on demand per contact, and the date of the lookup is stored; a reverse lookup turns coordinates into a place label.

**WHY**
- [N-U37-013] Coordinates support maps, partner assignment by area, pickup-point selection and labelling attendance check-in positions.

**BUSINESS RULE**
- [N-U37-014] Changing any part of an address clears the stored coordinates to zero unless new coordinates are supplied in the same change, so stale positions are not kept.
- [N-U37-015] If the full address finds nothing, a second attempt uses only city, state and country.
- [N-U37-016] Lookups are skipped during file imports, tests, demonstration installs and system start-up unless explicitly forced, and are blocked for reverse lookups in test mode.
- [N-U37-017] Contacts that could not be located are listed in a warning shown to the user who triggered the lookup.

**STATE**
- [N-U37-018] One of two seeded providers (OpenStreetMap or Google) is selected in settings; if the choice is missing or stale the first provider is used, and an unknown provider name stops with an error.

**OPTIONALITY**
- [N-U37-019] The Google provider needs an API key and stops with an instruction when none is set; the OpenStreetMap provider needs no key.

**DEPENDENCY**
- [N-U37-020] The module needs only the base settings module; time attendance, website maps, partner assignment and pickup-point delivery build on it.

**RISK**
- [N-U37-021] Addresses, or coordinates for reverse lookups, are sent to a third-party service; one forward call has no time limit; unexpected failures are hidden as no result, so users see only a no-match warning.

**UNKNOWN**
- [N-U37-022] Service availability, rate limits, terms of use and data-residency effects of the external services were not exercised and need a runtime test.


## CAP-U37-03 Bank account number validation

**WHAT**
- [N-U37-023] A bank account number can be typed as an international bank account number, which is recognised, formatted in blocks of four characters and offered with a validity indicator while typing.

**WHY**
- [N-U37-024] Cross-border payments and payment-document generation need account numbers in a standard checkable form.

**BUSINESS RULE**
- [N-U37-025] A valid number starts with a supported country code, has the exact length of that country's pattern, uses letters and digits only, and passes the standard modulo checksum.
- [N-U37-026] A number that passes validation is stored with spaces after every fourth character.
- [N-U37-027] The basic account number is the part after the first four characters, and individual parts such as bank code, branch and account can be extracted using the country pattern; asking for it on a non-standard account is an error.

**OPTIONALITY**
- [N-U37-030] The check indicator is a client widget used on the bank account form and the bank setup wizard and is advisory only.

**DEPENDENCY**
- [N-U37-031] The module needs accounting and the web client; the European payment QR-code module depends on it.

**CONSTRAINT**
- [N-U37-028] Supported countries come from a fixed table of seventy patterns in the source; Thailand has no entry, and one entry has an inconsistent prefix that does not affect validation.

**RISK**
- [N-U37-029] Because the account type is derived from the same check, a number that fails validation is stored as an ordinary account instead of being rejected, so the built-in rejection rule is effectively inactive; this needs a runtime test.

**UNKNOWN**
- [N-U37-032] Whether the country pattern table matches the current official registry was not checked.


## CAP-U37-04 Record import from spreadsheet and text files

**WHAT**
- [N-U37-033] Users can load records into almost any business object from CSV, Excel and OpenDocument files through a guided flow: upload, preview with suggested column mapping, test run, then real import in batches with resume.

**WHY**
- [N-U37-034] Bulk loading and migration of master and transaction data needs a user-operated path that applies the same validations as normal entry.

**BUSINESS RULE**
- [N-U37-036] Empty rows are dropped, spreadsheet error cells stop the import, comment cells in OpenDocument files are skipped, and text encoding and separator are guessed when not chosen.
- [N-U37-038] Importable columns follow the object's writable fields, add an external identifier column, offer identifier sub-columns for relations, expose custom properties the user may read, and show database identifiers of lines only in developer mode.
- [N-U37-039] Column suggestions use, in order, remembered mappings, exact name or label matches, and fuzzy matches restricted to compatible field types, accepting only close matches and keeping the closest column when several compete.
- [N-U37-041] Date formats are guessed from many day, month and year orders and separators, or taken from the user's choice, and bad dates name the column and line.
- [N-U37-042] Numbers may carry currency symbols, parentheses for negatives and either decimal convention, which are inferred or taken from options; unreadable numbers stop the import with the column and value.
- [N-U37-044] Several columns mapped to the same text field are concatenated with a space, a line break, an HTML break or a comma depending on field type.

**STATE**
- [N-U37-040] The preview shows ten rows, example values per column, the detected types and whether the file needs several batches; errors return a short raw excerpt.
- [N-U37-047] Each import uses a short-lived work record; a test run never saves, a real import commits per batch of two thousand rows by default and can resume at the next line, and names of imported rows are reported back.

**OPTIONALITY**
- [N-U37-035] Four file formats are supported and each depends on an optional software library; a missing library or unknown format produces a specific message.
- [N-U37-037] Each business object may offer downloadable sample files; sales, products, manufacturing, customer relationship and pricing offer them.
- [N-U37-046] Per-field choices for creating missing related names, setting empty values, skipping records and fallback values for choices and flags, plus a switch for change tracking, are passed through to the loading step.
- [N-U37-049] The import module is installed automatically with the web client and can be removed; the examined database has it installed.

**DEPENDENCY**
- [N-U37-048] A shared import flag changes behaviour elsewhere: no invitation mails for imported users, no registry refresh for imported automation rules, account and journal defaults, inventory lines not merged, sales combo handling, no approval activities for time-off, no automatic installation of localisation modules for new companies, and no geolocation lookups.

**CONSTRAINT**
- [N-U37-043] Image or file columns accept web addresses (restricted by role, size and time), file names to be supplied later, or encoded data; other values are rejected.
- [N-U37-045] At least one column must be mapped, the first data row must match the header width, empty mapped rows are discarded, and pre-load validation failures use the same message shape as load errors.

**RISK**
- [N-U37-050] Remembered column mappings are shared by all internal users, web-address fetching (limited to administrators by default) applies no host filtering in this module, and side effects of a test run on external services were not verified.

**UNKNOWN**
- [N-U37-051] Behaviour with very large files, memory limits, character sets and each model's own load rules was not exercised.


## CAP-U37-05 Module package import and installation requests

**WHAT**
- [N-U37-052] Administrators can import a data package (data files, static files, translations and asset declarations) or fetch an industry package from the vendor store; ordinary employees can ask administrators by mail to install an application, and an administrator reviews the request and installs it in one step.
- [N-U37-056] The installation request mail goes to every system administrator immediately with the requester's text and a link to a review step that lists the applications that would be installed.

**WHY**
- [N-U37-053] Customisations delivered as data and controlled user-initiated requests for new applications reduce direct administrator involvement while keeping installation an administrator decision.

**BUSINESS RULE**
- [N-U37-054] Only administrators may import or download packages; only data, initial-load and optional demonstration files, static assets, translations and asset declarations are used; wildcards in asset paths, unknown dependencies and oversize entries are refused; known uninstalled dependencies are installed first.

**STATE**
- [N-U37-055] An imported package becomes an installed module record flagged as imported; it is not loaded as code at start-up, cannot be upgraded, gets its translations and static files from stored attachments, and is deleted entirely when removed.

**OPTIONALITY**
- [N-U37-057] Both modules install automatically; the force option and the Import Module menu are visible only in developer mode; a server option may auto-install a default set of productivity applications after installation.

**RISK**
- [N-U37-058] Package import runs with elevated rights, may execute database scripts from the package, and relies on a vendor store reached over the internet; the installation request module also widens the Apps menu to all employees, and sent request mails are deleted after sending.

**UNKNOWN**
- [N-U37-059] Behaviour of the vendor store, network failures during download, and the effect of update-list files that are extracted but not loaded were not exercised.


## CAP-U37-06 Real-time notification channel

**WHAT**
- [N-U37-060] A server-to-browser push channel delivers short messages (toasts, chat, alarms, collaborative-editing signals) to users in real time over a persistent connection, with a polling alternative.

**WHY**
- [N-U37-061] Interactive features need immediate delivery without the user refreshing the page.

**BUSINESS RULE**
- [N-U37-062] Messages are written and announced only when the sending transaction commits; each message targets a channel made of a record or a text name; every connection is automatically subscribed to the broadcast channel, the channels of the user's groups and the user's own contact, and other modules add discussion and document channels with their own access checks.

**STATE**
- [N-U37-063] Each connection is open, closing or closed with named close reasons; clients reconnect with growing delay and random jitter, a shared worker serves all tabs of a browser, notifications received are tracked by id with a ten-second history to avoid loss and duplication, and the page warns when it is outdated or notifications were missed.

**OPTIONALITY**
- [N-U37-064] Retention of stored messages (one day by default), payload size, keep-alive lifetime and rate limits are configurable; same-site restriction and the notification function are set through environment variables; sockets are disabled in tests.

**DEPENDENCY**
- [N-U37-065] Messaging, the HTML editor and spreadsheets depend on the channel; discussion and collaborative-editing channels are authorised by those modules.

**RISK**
- [N-U37-066] The connection endpoint is public with open cross-origin access, text channel names are not secret, any signed-in user can read model field metadata through a helper route, and stored messages are cleaned only by the periodic vacuum.

**UNKNOWN**
- [N-U37-067] Behaviour behind reverse proxies, under load, and with the evented server port was not exercised.


## CAP-U37-07 Calendar events, attendees, recurrence and visibility

**WHAT**
- [N-U37-068] Employees schedule events with an organiser, attendees taken from contacts, reminders, tags, a video-call link, an optional link to a business document, and optional repetition.

**WHY**
- [N-U37-069] Shared scheduling needs one authoritative record of time, people and visibility, tied to the work records that triggered the meeting.

**BUSINESS RULE**
- [N-U37-070] A new event starts at the next half hour with a default duration of one hour unless a stored default exists; changing the start keeps the duration; all-day events are stored as dates and are not shifted by time zone.
- [N-U37-072] Each event is public, private or internal-only; an empty setting follows the organiser's default, which new users take from a system parameter; others see only the word Busy for private events, grouped reads and chat history are restricted, nobody may change another user's default, and administrators may edit non-private events they were not invited to.
- [N-U37-073] Attendees are generated from the contact list with the organiser accepted by default and others awaiting an answer; answers can apply to one occurrence, following ones or all; copying an event gives fresh attendee records; unavailable attendees are those with another busy overlapping event.
- [N-U37-074] An event created for a business document also creates a meeting activity on that document, and later changes to the activity deadline, title, description or responsible stay synchronised both ways with guards against loops; completing the activity with feedback appends it to the event notes.
- [N-U37-075] Repetition is daily, weekly, monthly or yearly with interval and an end by count, date or horizon; at most 720 occurrences and fifteen years by default are generated; weekly rules need a weekday; edits can target this event, following events or all events and replace, trim or detach the rule accordingly; wall-clock time is kept across daylight-saving changes.
- [N-U37-076] Invitation mails go to newly added attendees and cancellation mails can be sent when an event with other attendees is deleted; occurrences generated by a rule are created without mails.
- [N-U37-078] Signed-in users presenting an event token are added as attendees; a public route creates the call channel on first use; internal users following an invitation link reach the event form while others get a simple page.

**STATE**
- [N-U37-077] Events can be active or archived, linked to a video-call channel created on first use, and removed individually or by recurrence scope; deleting an event with alarms refreshes the next-alarm notices of its attendees.

**DEPENDENCY**
- [N-U37-079] The calendar needs only the platform and messaging modules; customer-relationship, time-off, recruitment, attendance-related, SMS and the external calendar synchronisation modules build on it.

**CONSTRAINT**
- [N-U37-071] An event may not end before it starts; filters per user and contact, and tags by name, are unique.

**UNKNOWN**
- [N-U37-080] Run-time behaviour of recurrence edits near daylight-saving boundaries, mass edits and synchronisation with external calendars was not exercised.


## CAP-U37-08 Event reminders, invitations and text-message reminders

**WHAT**
- [N-U37-081] Attendees are told about events by invitation and change mails with a calendar file attached, by reminders at a chosen time before the start (browser notification, mail, or text message when the SMS extension is installed), and by answer links that work without signing in.

**WHY**
- [N-U37-082] Timely notice and quick replies reduce no-shows and keep the attendee list truthful.

**BUSINESS RULE**
- [N-U37-083] Mails are rendered per attendee in the attendee language, only for attendees with an address, with copies of template attachments, and a fallback sender; five templates cover invitation, date change, reminder, event update and deletion.
- [N-U37-084] Reminders are defined by type, length in minutes, hours or days and a template; seven are seeded; browser notices cover the next 24 hours after the last acknowledgement and are shown with OK, Details and Snooze.
- [N-U37-086] Accept and decline links use per-attendee tokens, can apply to a whole recurrence, run as the public user and show a page in the attendee language and time zone.
- [N-U37-087] A text-message alarm type uses a template; the message goes to attendees with a usable phone number who did not decline, normally excluding the organiser, is sent immediately, and a manual bulk text action refuses events without attendees.

**STATE**
- [N-U37-085] A daily job and one-off triggers send due reminders to attendees who did not decline for events not yet ended, looking back at most one week by default, with an immediate-send limit across attendees and re-arming for recurring events.

**OPTIONALITY**
- [N-U37-088] Attendee mail can be blocked by a system parameter or per call; the SMS extension is installed automatically with the calendar and the text gateway.

**UNKNOWN**
- [N-U37-089] Mail delivery, text gateway credit, failures and bounce handling, and the exact timing of triggers were not exercised.


## CAP-U37-09 Certificates and cryptographic keys

**WHAT**
- [N-U37-090] Administrators store per-company certificates and keys, parse common formats, derive validity and issuer chains, and let other modules sign, verify, decrypt, fingerprint and present client certificates.

**WHY**
- [N-U37-091] Electronic documents and secure service connections need a controlled store of key material.

**BUSINESS RULE**
- [N-U37-092] A key file is read as private or public material in several encodings; an encrypted key without its password shows no error until a password is given.
- [N-U37-093] Signing needs a private key and supports three algorithm families with SHA-1 or SHA-256 digests; verification needs a public key; decryption supports RSA only.
- [N-U37-094] Keys can be generated for a company: elliptic curve with one curve, RSA with limited exponent and a minimum size, and Ed25519; a password can protect them.
- [N-U37-095] Certificate files are parsed as DER, PKCS12 or PEM; subject name, serial, validity dates and a stored PEM copy are derived; a linked key must match the certificate; validity is time-based; a key bundled with the file is extracted into a key record.
- [N-U37-096] Issuer certificates are detected by name and then by cryptographic proof or key identifiers; missing authorities in an uploaded bundle are created automatically as archived records without duplicates.
- [N-U37-098] Certificates and keys are reachable from settings by system administrators only, and both records follow a company visibility rule.

**OPTIONALITY**
- [N-U37-097] A client-certificate adapter lets callers present a stored certificate and add trusted authorities to a web session; invalid authorities stop with an error.

**DEPENDENCY**
- [N-U37-100] The e-invoice proxy client uses the key store and is the only installed dependent; no certificate or key exists in the examined database.

**RISK**
- [N-U37-099] Passwords of certificates and keys are stored as plain text and removed only when a copy of the database is neutralised; the stored key copy is unencrypted unless a password was set, and the client adapter loads keys without a password, which would fail for password-protected keys.

**UNKNOWN**
- [N-U37-101] Behaviour with real certificates, key rotation and expiry reminders was not exercised, and no expiry notification was found in the module.


## CAP-U37-10 Add-ons not installed in the examined database

**WHAT**
- [N-U37-102] Three add-ons are present in source but not installed: personal dashboards, sparse-field storage and Google cloud attachment storage; their configuration context in the examined database is unknown.

**WHY**
- [N-U37-103] A personal dashboard lets each user collect their favourite views; sparse storage avoids very wide tables; cloud storage keeps large chat attachments outside the database.

**BUSINESS RULE**
- [N-U37-104] From any non-form view a user can add the current view, filters and grouping to a personal dashboard of one to three columns in five layouts; items can be moved, folded and removed and are saved per user as a personal view.
- [N-U37-107] A field can be declared sparse so its value lives inside a shared text container as a key-value mapping; empty values remove the key, relation values are filtered to existing records, and the link cannot be renamed or changed after creation.
- [N-U37-109] When enabled, chat attachments above a size threshold are uploaded by the browser straight to a Google bucket using short-lived signed addresses; settings need a bucket name and a service-account key and are tested with live upload, download and bucket-policy calls.

**STATE**
- [N-U37-105] Each addition creates a new personal view record, the newest being the one used; rewriting a base view discards personal customisations; the browser must be refreshed to see an added item.

**OPTIONALITY**
- [N-U37-108] Only a test model uses the option and no community module depends on this add-on; custom fields created in the interface can also be sparse.
- [N-U37-111] The add-on needs the vendor authentication library and is removed only when no attachment points to the bucket; neutralising a database copy deletes its parameters.

**RISK**
- [N-U37-106] Items remember the filters at the time of adding, additions are written with elevated rights, and an item whose target action no longer exists is shown as invalid.
- [N-U37-110] The service-account credential is stored in clear text and appears to be shown again on the settings page, the bucket is opened to any origin, a manual clean-up script with embedded credentials is the only way to remove unreferenced objects, and region or consent controls are left to the operator.

**UNKNOWN**
- [N-U37-112] None of the three add-ons has configuration rows in the examined database; their run-time behaviour, migration of existing attachments and interplay with installed modules are unknown.
