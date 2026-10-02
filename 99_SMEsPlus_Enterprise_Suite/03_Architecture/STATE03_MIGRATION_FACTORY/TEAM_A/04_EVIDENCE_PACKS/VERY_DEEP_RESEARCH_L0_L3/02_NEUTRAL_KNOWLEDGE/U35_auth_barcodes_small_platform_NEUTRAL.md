# U35 Authentication Extras, Barcodes and Small Platform Modules — NEUTRAL KNOWLEDGE

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Clean-room layer: plain business and process language only (platform: Odoo 19 Community, named once here).
> Each statement carries an identifier in square brackets that links it to restricted technical claims. No file, module, field or code names appear below.
> Scope: self-registration, invitations and password reset; second sign-in steps by authenticator application and by e-mailed code; passkeys; password-policy hints; barcode nomenclatures and GS1 parsing. No completeness, coverage or approval is asserted.

## CAP-U35-01 Registration of external accounts and acceptance of invitations

### WHAT
- [N-U35-001] A visitor can create an external (portal-type) account from a public sign-up page when free sign-up is the configured scope.
- [N-U35-002] An invitation e-mail gives an existing contact a link that opens the sign-up page already bound to that contact, so the person only chooses a password.
- [N-U35-003] Every new account is a copy of one designated template user that carries the external-user group and nothing else; the template itself is archived and cannot sign in.
- [N-U35-004] After a successful public sign-up the system sends a welcome e-mail and signs the visitor in; when no further page was requested the visitor sees a registration-successful notice.

### WHY
- [N-U35-005] External customers and partners reach their own documents without administrator data entry, while an invitation-only scope keeps account creation under administrator control.

### BUSINESS RULE
- [N-U35-006] The sign-up page exists only when free sign-up is configured or the visitor holds a valid invitation link; otherwise the system answers as if the page did not exist.
- [N-U35-007] The seed data switches free sign-up and password reset on; if the scope setting is ever missing, the code treats the scope as invitation-only.
- [N-U35-008] An invitation link carries a signed, time-limited token bound to the contact, the contact's current user list, the contact's latest sign-in time and the link type; it is spent on use and also stops working when the contact signs in or the users of the contact change.
- [N-U35-009] Invitation links are valid for 144 hours by default and the period is a system setting.
- [N-U35-010] A new account is refused when any user, including an archived one, already uses the same e-mail address (compared without regard to case).
- [N-U35-011] An invited contact that belongs to a company gets an account restricted to that company.
- [N-U35-012] When accepting an invitation for a contact without a user, the person can type any login; the account e-mail then becomes that login, so it may differ from the address the invitation was sent to.
- [N-U35-013] When the contact already has a user, accepting a link only sets the password and other form values; login and name cannot be changed this way, and an inviter notice is raised only for internal users who never signed in.
- [N-U35-014] City, country and language typed or detected at sign-up never overwrite values the contact already has.
- [N-U35-015] Only a fixed list of query and form parameters is carried into the sign-up and reset pages; every other parameter is dropped.
- [N-U35-016] A token or login hint arriving in any link is remembered in the visitor's session and used to prefill the next sign-up, reset or login page.
- [N-U35-017] The two password entries must be identical, and the visitor's language is stored on the new account only if that language is installed.
- [N-U35-018] When an invited internal user first completes sign-up, the person who created the account receives a real-time notice.
- [N-U35-019] A signed-in visitor opening the login page with a redirect target is forwarded to it; the redirect is forced to stay within the same site.
- [N-U35-020] The sign-up and reset pages refuse to be embedded in frames from other sites.

### STATE
- [N-U35-021] Visitor: anonymous, then holder of an invitation link (token valid), then registered and signed in; the token is spent at registration.

### OPTIONALITY
- [N-U35-022] Scope, template user and password reset are administrator settings; in the restored database free sign-up is on, reset is on, and the template user is the archived external-user template.
- [N-U35-023] Both public pages declare a bot-check action; in the restored database the bot-check service has no secret key configured, so the check passes without contacting the provider.

### DEPENDENCY
- [N-U35-024] The feature needs outgoing e-mail for invitations and welcome messages, the base user template, the settings module and the web login flow; the bot-check hook comes from a separate optional module.

### CONSTRAINT
- [N-U35-025] The new account is committed to the database before the sign-in and the welcome e-mail are attempted, so a later failure does not undo the account.
- [N-U35-026] Account creation fails when the template user is missing, when no login is given, or when neither a name nor a contact is given; any error raised while copying the template is reported as a sign-up error.

### RISK
- [N-U35-027] A failed registration tells the visitor whether an e-mail address is already registered, and unexpected internal error text is appended to the message shown.
- [N-U35-028] With free sign-up on, anyone can create an external account; protection against automated abuse depends on the bot-check being configured with a secret key.
- [N-U35-029] Because an invitee may choose any login, the registered address can differ from the invited address; nothing in the sign-up step proves control of the chosen address.

### UNKNOWN
- [N-U35-030] How the hosted bot-check, the mail delivery and the browser pages behave at run time cannot be confirmed without running the system.

## CAP-U35-02 Password reset by e-mailed link

### WHAT
- [N-U35-031] A visitor who forgot a password enters a login or e-mail address on a public page and receives an e-mail with a link that opens a page for choosing a new password.
- [N-U35-032] Reset and invitation links point to the site's base address, name the database and carry the signed token; links for an invitation use the sign-up page and links for a reset use the reset page.

### WHY
- [N-U35-033] Account recovery and first-time password setting without administrator involvement.

### BUSINESS RULE
- [N-U35-034] A reset link is valid for 4 hours by default and an invitation link for 144 hours; both periods are system settings, and the validity lives inside the signed token rather than in a stored record.
- [N-U35-035] A reset request finds the account by exact login first and then by e-mail ignoring case; if no account or more than one account matches, the request is refused.
- [N-U35-036] Archived users cannot be sent a reset or invitation link, and a user without an e-mail address cannot be sent one at all.
- [N-U35-037] The reset mail is sent immediately through the standard template (or a built-in fallback template), is deleted after sending and is labelled as a user notification; a mail-delivery failure is reported to the administrator with a distinct message.
- [N-U35-038] A reset link works once: it is spent when the new password is saved and also dies at the next sign-in of that user; a token that does not resolve is reported with the submitted token echoed back.
- [N-U35-039] Every reset request and every sent link is written to the server log with the login, the current user and the source address.
- [N-U35-040] A standard well-known address sends password-manager change-password requests to the reset page.
- [N-U35-041] Generating a link for an existing user requires write access to users when the user is internal and write access to contacts when the user is external.
- [N-U35-042] Setting a password through a reset link changes the password but, unlike changing one's own password in settings, does not remove the user's remembered trusted browsers for the second sign-in step.
- [N-U35-043] Because the user's password is part of the session fingerprint, setting a new password through a reset ends the user's other sessions.
- [N-U35-044] When the mail feature is installed, any password change, including one made through a reset link, e-mails the account owner a security notice (send errors are ignored) that suggests a reset only when reset is enabled.

### STATE
- [N-U35-045] Account recovery: no request, then link issued (token valid), then password set (token spent) or link expired.

### OPTIONALITY
- [N-U35-046] The reset page and its login-page link can be switched off by a setting; when switched off the page is reachable only with a valid token.

### DEPENDENCY
- [N-U35-047] Needs outgoing e-mail, a working base address setting and the shared sign-up helper functions.

### CONSTRAINT
- [N-U35-048] Reset needs an active HTTP request context for logging and the target user must have an e-mail address.

### RISK
- [N-U35-049] The reset page answers differently for unknown and ambiguous accounts, which reveals whether an account exists.
- [N-U35-050] Document-sharing links sent by the system to contacts without a user can embed a sign-up token when free sign-up is on, so the link recipient can register as that contact.
- [N-U35-051] A stolen trusted-browser token survives an administrator or e-mail password reset until it expires or is revoked.
- [N-U35-052] Reset requests are protected only by the bot-check: there is no per-address counter or cooldown in this feature, so the number of reset e-mails an address can receive is not otherwise limited.

### UNKNOWN
- [N-U35-053] Delivery time of the mail and behaviour when the mail server is unreachable were not exercised.

## CAP-U35-03 Invitation lifecycle, user status and the reminder for people who never registered

### WHAT
- [N-U35-054] Each user shows a status of Invited until the first sign-in and Confirmed afterwards; administrators can resend an invitation to an invited user and send a reset link to a confirmed one.
- [N-U35-055] A daily scheduled job e-mails the creator of internal accounts who never signed in five days after creation, listing the pending names and logins.
- [N-U35-056] Creating a user with an e-mail address automatically sends an invitation unless the creator suppresses it, and bulk invitations by e-mail address re-invite existing invited users instead of creating duplicates.

### WHY
- [N-U35-057] Keeps invitations from being forgotten and keeps one account per person.

### BUSINESS RULE
- [N-U35-058] Status is derived from whether the user ever signed in; searching on it supports only the 'in' form.
- [N-U35-059] Archiving a user or deleting a user cancels the contact's pending invitation or reset link; a failed invitation mail at creation also cancels it.
- [N-U35-060] The reminder looks only at internal users created on the calendar day exactly five days earlier, whose creator has an e-mail address and who never signed in; it groups them per creator and queues one e-mail each, without remembering who was reminded.
- [N-U35-061] If the reminder template is missing, the job logs a warning and deactivates itself.
- [N-U35-062] A batch size is passed to the job but is not used; every matching user is processed in one run subject only to the run's time limit.
- [N-U35-063] Bulk invitation by e-mail address re-sends invitations to existing invited users whose login or e-mail matches and creates accounts only for the remaining addresses.
- [N-U35-064] Duplicating a user does not send an invitation to the original person unless a new e-mail address is supplied.
- [N-U35-065] The reset-instructions bulk action is available only to the access-rights role.

### STATE
- [N-U35-066] User: invited (never signed in), confirmed (signed in at least once), archived; deleted users disappear and take their pending links with them.

### OPTIONALITY
- [N-U35-067] The reminder job is active in the restored database, runs daily with priority 6 and is owned by the superuser.

### DEPENDENCY
- [N-U35-068] Needs outgoing e-mail, the scheduler and the real-time notification bus.

### CONSTRAINT
- [N-U35-069] The reminder is not recorded per user, so a missed day means no reminder; mail errors at creation are swallowed after cancelling the link.

### RISK
- [N-U35-070] An invited user whose creator has no e-mail address is never reminded, and users created by the same creator on one day are listed together in one e-mail.

### UNKNOWN
- [N-U35-071] Scheduler timing, timeouts and queue delivery of the reminder mail were not exercised.

## CAP-U35-04 Password-policy hints on the sign-up and external-user pages

### WHAT
- [N-U35-072] Two optional companions add a minimum-length hint and a strength meter to the sign-up page and to the external-user security page; the actual length rule is enforced by a separate password-policy feature when it is installed.

### WHY
- [N-U35-073] Gives people immediate feedback while choosing a password and keeps the browser's own minimum-length check aligned with the server rule.

### BUSINESS RULE
- [N-U35-074] The browser hint takes its minimum from one system setting; when that setting is absent no minimum is attached to the field.
- [N-U35-075] The strength meter is advisory: it colours the entry but never blocks submission.
- [N-U35-076] The only server-side policy rule in the base feature is the minimum length, applied to every non-empty password write before hashing, so it covers sign-up, reset and settings alike; empty passwords are rejected by the generic password setter regardless.
- [N-U35-077] On the external-user security page the meter and hint apply only to the first new-password field.

### OPTIONALITY
- [N-U35-078] None of the policy feature or its two companions is installed in the restored database, so today any non-empty password is accepted by the server.

### DEPENDENCY
- [N-U35-079] The companions depend on the policy feature plus the sign-up feature or the portal respectively, and install themselves automatically when both are present.

### CONSTRAINT
- [N-U35-080] Translations for the meter text are added to the front-end translation set by both companions.

### RISK
- [N-U35-081] Without the policy feature, sign-up and reset accept very weak passwords; the companions alone would not enforce anything.

### UNKNOWN
- [N-U35-082] Client-side meter scoring and the browser's handling of the minimum-length attribute were not exercised.

## CAP-U35-05 Authenticator-application second step, trusted browsers and portal management

### WHAT
- [N-U35-083] With the authenticator-application second step, a correct password only opens a partial pre-session; the visitor must then type a six-digit code from an authenticator application before any business page becomes reachable.
- [N-U35-084] A user enrols only their own account: after an identity re-check the system shows a freshly generated secret as text and as a scannable image, and the second step becomes active when the user types a currently valid code; the secret field is cleared once the code is accepted.
- [N-U35-085] External users manage the second step on their own security page: enable, disable, view trusted browsers, revoke one or all; each action first asks for a password re-check.
- [N-U35-086] After a valid code the user may trust the browser; a random long-lived token in an HTTP-only cookie then completes later sign-ins from that browser without a code.

### WHY
- [N-U35-087] Limits the damage from stolen or guessed passwords for internal and external users and keeps password-based programmatic access closed for protected users.

### BUSINESS RULE
- [N-U35-088] Every code check is counted before the code is examined, five checks per hour per user are allowed whatever the source address, and the counter is cleared only by a successful check; repeated attempts can therefore lock the user out of the step for up to an hour.
- [N-U35-089] A code is accepted when it matches the previous, current or next 30-second step, the first matching step is used, and a step that is not newer than the last accepted one is refused as reuse.
- [N-U35-090] The secret carries 160 bits of randomness and codes follow the standard SHA-1, six-digit, 30-second scheme.
- [N-U35-091] Only the owner can enrol; the owner, an access-rights administrator or a superuser process can disable; an unauthorised disable attempt is logged and silently ignored.
- [N-U35-092] Enabling, disabling and revoking all trusted browsers require a credential re-check within the last ten minutes; the re-check asks for the password (or a passkey), never for the second-step code.
- [N-U35-093] Enabling or disabling changes the fingerprint of the user's sessions, so other sessions of that user end while the acting session is refreshed and continues.
- [N-U35-094] A trusted-browser token is a random 160-bit value stored only as a slow hash in its own table with a scope and an expiry; the stored device name combines browser, platform and, when available, city and country.
- [N-U35-095] Opening the code page with a valid trusted-browser cookie completes the sign-in without a code, without the code-check counter and without the sign-in cooldown guard.
- [N-U35-096] A user with a second step cannot use the account password for programmatic access; API keys remain usable.
- [N-U35-097] Employees and external users may read the list of their own trusted browsers but cannot create or delete rows directly; the rate-limit records are invisible to ordinary users.
- [N-U35-098] The label shown in the authenticator application is the host name of the request, falling back to the company name.
- [N-U35-099] Enrolment records are visible only to their owner; trusted-browser rows are visible to their owner and, without restriction, to system administrators, and the public role sees none.
- [N-U35-100] Administrators can disable the second step for several users at once from the user list; the action is limited to the access-rights role and also removes those users' trusted browsers.

### STATE
- [N-U35-101] Sign-in: no session, partial session (password accepted), full session (valid code, trusted-browser cookie or passkey); failures leave the visitor in the partial state.
- [N-U35-102] Account: not enrolled, enrolled, disabled again by the owner or an administrator; each trusted browser stays active until revoked, expired or its user changes the password through settings.

### OPTIONALITY
- [N-U35-103] The feature installs itself automatically but each user opts in; in the restored database nobody is enrolled, no trusted browser exists and the rate-limit table is empty.

### DEPENDENCY
- [N-U35-104] Needs the web sign-in flow, the shared identity re-check, the session fingerprint and, for the external-user page, the portal and its security page.

### CONSTRAINT
- [N-U35-105] The code must be digits (spaces ignored); a non-numeric entry is rejected before any check, and the code check and enrolment need an active web request.
- [N-U35-106] Enrolment and rate-limit records are short-lived transient data; the enrolment link and image keep the secret until cleanup even after the secret field is blanked.

### RISK
- [N-U35-107] The secret is stored unencrypted in the user table and, during enrolment, in a transient record, the setup link and the image.
- [N-U35-108] Because the counter is per user and not per source, anyone holding a password-verified partial session for that user can use up the hourly allowance and block the owner's code entry.
- [N-U35-109] The trusted-browser cookie has no secure flag and is not removed by a password reset through an e-mailed link.
- [N-U35-110] An access-rights administrator can disable another user's second step after re-entering only their own password; no second approver is involved.

### UNKNOWN
- [N-U35-111] Browser and proxy handling of the cookie, practical clock-drift tolerance and the retention of transient rows were not exercised.

## CAP-U35-06 E-mailed-code second step, enforcement policy, invitations and security alerts

### WHAT
- [N-U35-112] When an administrator enforces the e-mail policy, users who have no authenticator application receive a six-digit code by e-mail on the second sign-in page and must type it to finish signing in.
- [N-U35-113] The same feature e-mails the account owner when the second step is activated or deactivated, when a trusted browser is removed, and when a password-verified sign-in comes from a browser that is not trusted.
- [N-U35-114] Administrators can invite users, one or many from a list, to enable the authenticator second step; the e-mail link leads internal users to a reduced settings page and external users to the portal security page.

### WHY
- [N-U35-115] Gives organisations a way to require some second step for every sign-in even before users install an authenticator application, and gives users visibility of changes to their sign-in security.

### BUSINESS RULE
- [N-U35-116] The policy has two values, employees only or all users including external ones; it applies only to users who have no authenticator enrolled, and the authenticator always takes precedence.
- [N-U35-117] A user subject to the e-mail policy is restricted to API keys for programmatic access just like an enrolled user.
- [N-U35-118] The e-mailed code is a six-digit value derived from the user identity, the login name and the last sign-in time using a server secret; no code is stored, the same code is produced for every send within the hour, and it is not marked as used when accepted.
- [N-U35-119] The message says the code expires in one hour, but a code is accepted from the hour it is issued through the end of the following hour, so its effective life is between one and two hours; a later successful sign-in by the same user changes the derivation and invalidates outstanding codes.
- [N-U35-120] A message rendered outside an active pre-authentication session for that user shows a placeholder zero code rather than a real one.
- [N-U35-121] Five code sends and five code checks per hour per user are allowed; every response of the second-step page for an e-mail user (first visit, wrong code, resend) triggers a send, so the send allowance can run out and block further resends until the hour passes.
- [N-U35-122] A user without an e-mail address cannot receive a code; sending problems are shown on the page rather than raised.
- [N-U35-123] The new-browser alert is sent after the password step for any user who has an e-mail address and any second-step requirement, including users covered only by the e-mail policy, and is skipped when a valid trusted-browser cookie is present.
- [N-U35-124] Any change of the second-step secret, including an administrator disabling it, notifies the user; removal of trusted browsers notifies the user with the device names, including removals caused by disabling or by a password change.
- [N-U35-125] The invitation goes only to selected users who have not enabled a second step, is sent immediately from the acting administrator's address and lists the invited names in a confirmation notice.
- [N-U35-126] The invite actions are limited to the access-rights role; the invite button is hidden on the administrator's own record and for users who already enabled the second step.

### STATE
- [N-U35-127] Sign-in for a policy user: password accepted, code mailed, code accepted; the sign-in page re-sends a code on each visit.

### OPTIONALITY
- [N-U35-128] No enforcement policy is configured in the restored database and the two mail templates and two server actions exist; the enforce switch in settings is derived from whether the policy value is set.

### DEPENDENCY
- [N-U35-129] Needs outgoing e-mail, the second-step feature and the standard security-notification layout.

### CONSTRAINT
- [N-U35-130] Resending and checking are bounded by hourly limits and by mail delivery; the code page needs an active pre-authentication session.

### RISK
- [N-U35-131] The stated expiry understates the real acceptance window, and a code is not single-use.
- [N-U35-132] Six digits with five checks per hour per user bound guessing, but the allowance can also be used up by anyone holding the password.
- [N-U35-133] Enforcing the policy for a user with no e-mail address blocks their sign-in, because no code can be sent.
- [N-U35-134] Alerts reveal to the owner that the password was used from a new browser, but arrive after the password step and before any second step is completed.

### UNKNOWN
- [N-U35-135] Mail delivery latency and spam handling were not exercised; the exact date of the last sign-in used for the code derivation depends on when the platform records the sign-in.

## CAP-U35-07 Passkeys for sign-in and identity re-check

### WHAT
- [N-U35-136] A user can sign in with a passkey instead of a password: the browser asks the person to unlock an authenticator and the server verifies a signed response against the stored public key.
- [N-U35-137] Internal and external users register passkeys after an identity re-check, give each a name, and can rename and delete their own passkeys and see when each was created and last used.
- [N-U35-138] A passkey can also serve as the identity re-check before sensitive actions, with a visible option to fall back to the password.
- [N-U35-139] External users manage passkeys on their security page with the same checks, but the portal's identity re-check always asks for the password.

### WHY
- [N-U35-140] Replaces passwords with credentials that are bound to the site address and resistant to phishing, and removes the need for a separate second step.

### BUSINESS RULE
- [N-U35-141] A successful passkey sign-in skips the second sign-in step entirely, so a passkey stands in for both the password and any second factor.
- [N-U35-142] The server issues a random 64-byte challenge, keeps it in the visitor's session and consumes it on first use, so each challenge works once; no timestamp is stored and the browser is given a 60-second hint.
- [N-U35-143] A credential is bound to the host name of the configured base address; accepted origins are that address plus a fixed list of mobile-app signatures; user verification is mandatory and the credential must be discoverable.
- [N-U35-144] A signature counter that does not increase is refused whenever the stored or the reported counter is non-zero; authenticators that always report zero are accepted without replay protection.
- [N-U35-145] The user is found from the credential identifier alone, so the sign-in form needs no login name; an unknown identifier is refused with a distinct message and a failed verification shows the verifier's own message to the visitor.
- [N-U35-146] At registration the server checks challenge, origin, address hash, user presence, user verification, a supported key algorithm and the attestation statement; because no attestation is requested nothing about the authenticator make or model is checked, and no trust anchors are supplied for certificate chains.
- [N-U35-147] Only the credential identifier and the public key are kept; the registration-time counter and the authenticator identifier are discarded and the stored counter starts at zero.
- [N-U35-148] A user can delete only passkeys they created; an attempt on someone else's passkey is logged and silently ignored; administrators with the access-rights role can read and delete any passkey at data level but cannot edit it.
- [N-U35-149] The identifier, public key and counter are readable only by system administrators; ordinary users see only name and dates of their own passkeys.
- [N-U35-150] Adding or deleting a passkey changes the user's session fingerprint: the user's other sessions end and the acting session is refreshed.
- [N-U35-151] The same credential cannot be registered twice because the identifier is unique, but the registration request does not exclude credentials the user already registered.
- [N-U35-152] The binding host comes from the system base-address setting, which the platform refreshes at each system administrator sign-in unless it is frozen, so a changed host can break existing passkeys.
- [N-U35-153] A fixed mobile-app origin and a published asset-link file let the vendor's mobile app use passkeys for this site.
- [N-U35-154] Creation, deletion and denied deletion of passkeys are logged with the user and source address.

### STATE
- [N-U35-155] Passkey: registered, renamed, deleted. Sign-in: challenge issued, response verified, session opened with the second step skipped.

### OPTIONALITY
- [N-U35-156] The feature installs itself and has no switch to disable passkey sign-in; each user must register a passkey, and the restored database holds none.

### DEPENDENCY
- [N-U35-157] Needs the web sign-in form, the identity re-check, the session fingerprint, the base-address setting and a bundled standards library; the external-user variant needs the portal.

### CONSTRAINT
- [N-U35-158] Sign-in and registration both fail when the session holds no challenge, and the registration payload must be present.

### RISK
- [N-U35-159] Anyone holding an unlocked authenticator bypasses password and second step, and the identity re-check can be switched to password at any time, so passkeys do not strengthen that re-check.
- [N-U35-160] The endpoint that issues challenges is public and unauthenticated, and a malformed sign-in payload is not guarded against before parsing.
- [N-U35-161] Verification messages of the bundled library are shown to visitors, and most of the library's registration formats were not read.

### UNKNOWN
- [N-U35-162] Browser and authenticator behaviour, attestation formats other than none and the effect of base-address changes on existing passkeys were not exercised.

## CAP-U35-08 Barcode nomenclatures, rule matching and scan handling

### WHAT
- [N-U35-163] A barcode nomenclature is an ordered list of rules that classify a scanned code: each rule names an encoding family, a pattern and a meaning, and the first rule that matches decides what the code means.
- [N-U35-164] Each company points to one nomenclature; the default one contains a catch-all rule that treats any code as a product code, and other applications add rules for weighed products, locations, lots and packages.
- [N-U35-165] In the browser, scanner input is recognised as quick keystrokes ended by Enter or Tab (or a short pause) and then broadcast to whichever screen is listening; typing into ordinary input fields is not captured.
- [N-U35-166] Special scanned strings with fixed prefixes act as screen commands (edit, discard, save, previous record, next record, first record, last record) or click a visible button that is marked for barcode triggering.
- [N-U35-167] Forms can host a hidden receiving field and a numeric field that accepts scans; phones can scan with the camera and a manual-entry dialog is available.

### WHY
- [N-U35-168] Lets warehouses, kiosks, event desks and counters use scanners and cameras without custom code, with the meaning of codes kept as configurable data.

### BUSINESS RULE
- [N-U35-169] A rule pattern is a regular expression matched against the start of the code; it may contain one brace group of N for whole digits followed by D for decimal digits, which captures a quantity, weight or price from the code and sets those digits to zero in the base code.
- [N-U35-170] A pattern is refused when it has anything other than zero or exactly one pair of braces, braces holding anything but N followed by D, empty braces, a lone star, or is not a valid regular expression.
- [N-U35-171] Rules are tried by sequence and then creation order; the first match wins; an alias rule rewrites the code to a fixed value and matching continues with the rewritten code; a code that matches nothing returns the type error.
- [N-U35-172] A rule may require EAN-8, EAN-13 or UPC-A encoding with a correct check digit; an EAN-13 cannot start with zero; the check digit follows the standard weighted modulo-10 method and is recomputed for the base code.
- [N-U35-173] A setting lets UPC-A codes match EAN-13 rules and the reverse, but on the server path the conversion result is not used because the encoding check is made on the original code; the browser parser does apply it.
- [N-U35-174] Radio-tag style identifiers are converted into a product code plus lot number, or into a package code, with a recalculated check digit; unsupported identifiers pass through unchanged.
- [N-U35-175] The default nomenclature cannot be deleted, and companies without a nomenclature receive it when the feature is installed.
- [N-U35-176] All employees can read nomenclatures and rules and only the access-rights role can change them; the warehouse configuration menu entry is visible only in technical mode.
- [N-U35-177] The maximum pause between keystrokes of one scan is 150 milliseconds by default and can be changed by a system setting, but the value is sent only to internal users.
- [N-U35-178] Scans shorter than three characters are ignored, and the literal words for modifier keys are removed from scanned text.
- [N-U35-179] The browser parser mirrors the server logic with differences: an alias match is labelled alias, UPC-EAN conversion works, the check digit is validated on the converted code, and the 14-digit and 18-digit encodings are not recognised.
- [N-U35-180] A server-side receiving mixin lets a form model react to a scanned value like an onchange; the base method refuses to run until a model implements it, and no installed Community application was found using it.

### STATE
- [N-U35-181] A scan: keystrokes buffered, code completed by Enter, Tab or pause, event broadcast, then parsed against the active rules into a typed result or an error.

### OPTIONALITY
- [N-U35-182] In the restored database the default nomenclature serves the single company and holds five rules (weighed product, location, package, lot and the catch-all product rule).

### DEPENDENCY
- [N-U35-183] Used by attendance kiosks, event check-in and, when installed, point of sale; warehouse flows depend on the GS1 extension; camera scanning comes from the core web code.

### CONSTRAINT
- [N-U35-184] Pattern syntax is enforced when a rule is saved; check digits are verified only at parse time.

### RISK
- [N-U35-185] Any code beginning with the command prefixes triggers screen actions such as save or discard, so a printed or typed string can change what the operator is working on; nothing beyond being signed in authorises it.
- [N-U35-186] Rule patterns are regular expressions run on scanned text and are validated only for correctness, not for cost.
- [N-U35-187] Server and browser parsers give different answers for the same code in edge cases, so a code can be classified differently on the screen than on the server.

### UNKNOWN
- [N-U35-188] Scanner timing, camera scanning and consumers outside the installed set were not exercised.

## CAP-U35-09 GS1 element-string decomposition and GS1-aware barcode search

### WHAT
- [N-U35-189] A second nomenclature type decomposes one scanned GS1 string into several typed elements (product code, lot, dates, quantity, location, package) using rules that each capture an identifier prefix and a value.
- [N-U35-190] The bundled default GS1 nomenclature holds 29 rules: shipping container, trade item numbers, location numbers, lot and serial numbers, pack, best-before and expiration dates, counts, variable measures with units and a package-type rule.
- [N-U35-191] When the company uses a GS1 nomenclature, a barcode search helper can turn a scanned GS1 string or a zero-padded code into a search on the unpadded product code or the lot value.

### WHY
- [N-U35-192] One scan of a retail or logistics label identifies several facts at once, so goods receipts, counts and traceability need fewer keystrokes.

### BUSINESS RULE
- [N-U35-193] Each GS1 rule must hold exactly two parenthesised groups, the first capturing the identifier and the second the value, and its pattern must be a valid regular expression.
- [N-U35-194] Variable-length elements end at a configurable group separator (by default the standard control character, the hash sign or the text Alt029); the separator is optional after every element, and its pattern is checked only for validity.
- [N-U35-195] Scanner symbology prefixes are removed from the start of the string before parsing.
- [N-U35-196] Rules are tried in sequence order on the remaining text; parsing ends when the string is used up, and it fails as a whole with an empty result when no rule matches or no progress is made.
- [N-U35-197] A measure rule reads a number; when the rule uses decimals the last digit of the identifier gives the number of decimal places, and the unit comes from the rule.
- [N-U35-198] A numeric identifier is accepted only when its check digit is right (computed as if padded to 18 digits) and the value keeps the check digit; a wrong digit makes that rule be skipped on the server and fail the whole parse in the browser.
- [N-U35-199] A date must have six digits; the century is chosen so the year lies within about 50 years of today; a day of zero means the last day of the month; an impossible date raises an error on the server and rolls over in the browser.
- [N-U35-200] Rule types map identifiers to meanings: trade item numbers to product, lot and serial numbers to lot, three date identifiers to pack, best-before and expiration dates, counts and measures to quantity, location numbers to location or destination, shipping container to package, and one code to package type.
- [N-U35-201] The yards rule reuses the identifier pattern of the feet rule that precedes it, so a yards identifier is always taken by the earlier rule and the yards rule is never reached.
- [N-U35-202] The search helper handles equal, not-equal, in, not-in and like operators on the barcode field; several values become alternatives; lot values stay exact, numeric values are compared without leading zeros, other operators are left alone and a context flag turns the helper off.
- [N-U35-203] No Community application in the source tree calls the search helper; product and stock code only set the flag that turns it off for uniqueness and grouping checks.
- [N-U35-204] Warehouse label printing takes the identifier for non-unit measures from the unit-linked GS1 rules, reading characters from the pattern text and the unit's rounding, so editing patterns can change printed labels.
- [N-U35-205] A GS1 parse returns a list of elements instead of one result and returns nothing on failure, so callers must handle both shapes.

### STATE
- [N-U35-206] GS1 parse: prefix removed, rules applied in order to the remaining string until it is empty, then a list of typed elements or failure.

### OPTIONALITY
- [N-U35-207] The GS1 nomenclature and its 29 rules exist in the restored database because the warehouse application depends on the GS1 extension, but the single company still uses the default non-GS1 nomenclature, so GS1 parsing is inactive; no installed Community screen was found for switching the company nomenclature.

### DEPENDENCY
- [N-U35-208] Depends on the barcode feature and the unit-of-measure data; required by the warehouse application; the browser receives the separator pattern from the server only when the company nomenclature is GS1.

### CONSTRAINT
- [N-U35-209] The separator pattern is validated only when the nomenclature is flagged GS1, and nothing limits its cost.

### RISK
- [N-U35-210] Separator and rule patterns are administrator-defined regular expressions run on scanned input without cost limits.
- [N-U35-211] Editing the rule data (for instance changing identifier patterns) changes both scanning results and printed warehouse labels.

### UNKNOWN
- [N-U35-212] No test was run of the browser parser; whether enterprise warehouse screens call the search helper is not visible in the Community tree.
