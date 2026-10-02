# U49 neutral knowledge — passkey authentication, password policy, TOTP portal

> Neutral knowledge layer. DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. No vendor structure, no code.

---

[N-U49-001] The passkey module is an automatically installed extension that activates whenever its base framework dependencies are present. It provides users with the ability to log into the application using a hardware security key or device biometric instead of a password.

[N-U49-002] When a user authenticates with a passkey, the system explicitly skips any further multi-factor authentication steps. The passkey itself combines proof of physical device possession with user verification (such as a PIN or biometric), which the system treats as sufficient to replace both a password and a second factor.

[N-U49-003] Each passkey registered to a user is stored as a separate record containing a user-supplied name, a cryptographic credential identifier, the public key material used to verify future authentications, and a signature counter. The credential identifier and public key are accessible only to system-level processes, not to ordinary user queries. The credential identifier must be globally unique across all registered passkeys in the system.

[N-U49-004] The authentication ceremony proceeds in two phases. First, the server generates a one-time challenge that is bound to the user's session. The user's authenticator device signs this challenge and returns an authentication assertion. The server verifies the assertion using the stored public key, confirms that user verification actually took place, and checks that the signature counter has advanced (replay protection). The session challenge is consumed upon first use, preventing replay attacks. Expected origins include both the web application's own address and a list of approved mobile application identifiers.

[N-U49-005] Passkey registration also follows a two-phase ceremony. The server requests creation of a discoverable resident credential requiring user verification. The user's authenticator creates a new key pair, returning the public credential and attestation. The server verifies the response and stores the credential identifier and public key. Registration is protected by an identity confirmation step that the user must pass before a new passkey can be added.

[N-U49-006] Deletion of a passkey requires the user to confirm their identity first. A user may only delete their own passkeys. After deletion, the user's session token is immediately regenerated to reflect the changed credential state. Unauthorized deletion attempts by the account owner acting on someone else's passkeys are denied and logged.

[N-U49-007] The user's set of registered passkeys is included as a factor in the computation of their session token. Any change to that set — whether adding or removing a passkey — causes all existing sessions for that user to become invalid, forcing re-authentication.

[N-U49-008] To support passkey authentication in the official mobile application on Android, the server publishes a digital asset links document at a well-known web address. This document declares that the server delegates credential handling permissions to the mobile application, identified by its package name and certificate fingerprint.

[N-U49-009] Passkey authentication is integrated into the system's general identity confirmation mechanism. When a user who has registered passkeys is asked to confirm their identity before performing a sensitive operation, the system defaults to requesting passkey verification. The user may switch to password-based confirmation as an alternative.

[N-U49-010] Access to passkey records is governed by record-level rules. Each user, whether internal or a portal user, may only see and modify their own passkeys. Administrators with elevated access can view and remove any user's passkeys but cannot edit them. The underlying access control tables deny ordinary users the ability to create or remove passkey records directly; those operations are only permitted through controlled wizard flows.

[N-U49-011] The portal extension of the passkey module activates automatically when both the passkey module and the customer portal are installed. It enables portal users to manage their passkeys from their personal security page, including creating new passkeys, renaming existing ones, and deleting those they own. Attempting to modify another user's passkey results in an access denial.

[N-U49-012] The password policy portal extension automatically activates when the password policy module and the customer portal are present. It passes the configured minimum password length to portal page templates, making that requirement visible to users changing their password through the portal. It also ensures that password policy client-side validation messages are translated and available on portal pages.

[N-U49-013] The password policy signup extension automatically activates when the password policy and new-account-registration modules are installed together. It passes the configured minimum password length to the signup page configuration, making the policy requirement visible and enforceable during new account creation. A password strength meter widget is included in the signup page assets.

[N-U49-014] Time-based one-time password authentication uses a 160-bit secret key encoded in base-32, the SHA-1 hash algorithm, 6-digit codes, and a 30-second time step. The matching window accepts codes valid within one full time step before or after the current moment, accommodating clock drift and slow user input. Each successful verification stores the current counter value, preventing the same code from being accepted twice. Users with time-based one-time passwords enabled cannot use password-based API access and must use dedicated API keys instead. Enabling or disabling time-based one-time passwords on an account invalidates all existing sessions for that account.

[N-U49-015] Trusted device tokens allow a browser that has previously completed a time-based one-time password challenge to skip that challenge on subsequent logins. The token is stored in a browser cookie named with a short identifier, marked as inaccessible to client-side scripts and with a same-site restriction. The default trust duration is 90 days and is configurable through a system parameter. The server verifies the device token on each visit and completes the session automatically if it matches. All trusted device records are revoked when the user disables time-based one-time passwords or changes their password.

[N-U49-016] Rate limiting prevents brute-force attacks on the time-based one-time password verification flow. The system allows a maximum of five attempts per hour per user for both code verification and authentication email sending. Each attempt is recorded in a transient log with the user, remote address, and action type, indexed for efficient lookups. On a successful verification, the accumulated rate limit log entries for that user and action are cleared.

[N-U49-017] Enrolling a new time-based one-time password requires the user to first confirm their identity. The system generates a 20-byte random secret, encodes it in base-32, and presents it along with a scannable QR code in a setup dialog. The QR code encodes a standard authenticator URI including the issuer name, user login, algorithm, number of digits, and time step. The user must enter a valid code from their authenticator application to complete enrollment. Disabling time-based one-time passwords also requires identity confirmation.

[N-U49-018] When a user has time-based one-time passwords enabled, after entering their username and password they are redirected to a dedicated verification page. On first visit, the browser presents any stored trusted device cookie for automatic bypass. If no valid trusted device is found, the user enters their current code. If the user opts to remember the device, a new trusted device token is set in the browser, named using the browser name, operating system, and geographic location if available.

[N-U49-019] The portal time-based one-time password extension activates automatically when both the portal and the time-based one-time password modules are installed. For portal users, the link inviting them to set up two-factor authentication directs them to their personal security settings page rather than to the internal user settings area.

