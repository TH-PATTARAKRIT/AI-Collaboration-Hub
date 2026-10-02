# U49 — auth remaining: passkey, password policy, TOTP portal (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U49
- Modules: auth_passkey, auth_passkey_portal, auth_password_policy_portal, auth_password_policy_signup, auth_totp (residual), auth_totp_portal
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: DELTA-FIRST. auth_totp core in U21; only unread parts here. Source evidence only; RT flags for runtime unknowns.

---

## CAP-U49-01 auth_passkey — Module Identity and Dependencies

The `auth_passkey` module is named "Passkeys", version 1.1, with summary "Log in with a Passkey". It depends on `base_setup` and `web`. `auto_install` is `True`. License is LGPL-3. The manifest description states: "When a user logs in with a Passkey, MFA will not be required."

Sources: `auth_passkey/__manifest__.py:1-39`

---

## CAP-U49-02 auth_passkey — Data Model: auth.passkey.key

The `auth.passkey.key` model (`_name = 'auth.passkey.key'`) stores individual registered passkeys. Fields: `name` (Char, required), `credential_identifier` (Char, required, groups=`base.group_system`), `public_key` (Char, required, computed with inverse, groups=`base.group_system`), `sign_count` (Integer, default=0, groups=`base.group_system`), `create_uid` (Many2one `res.users`, indexed). A database-level UNIQUE constraint is applied to `credential_identifier`.

Sources: `auth_passkey/models/auth_passkey_key.py:21-35`

---

## CAP-U49-03 auth_passkey — Public Key Storage via Raw SQL

The `public_key` field is computed (`_compute_public_key`) using a raw SQL `SELECT public_key FROM auth_passkey_key WHERE id = %s` query (line 53-57), bypassing ORM field group restrictions for reads. The `init()` method adds the column with `ALTER TABLE auth_passkey_key ADD COLUMN public_key varchar` (line 39-41) if missing. The inverse `_inverse_public_key` is a no-op pass (line 59-60). On passkey creation in `AuthPasskeyKeyCreate.make_key()`, the public key is written via raw SQL: `UPDATE auth_passkey_key SET public_key = %s WHERE id = %s` (line 181-184).

Sources: `auth_passkey/models/auth_passkey_key.py:37-60`, `auth_passkey/models/auth_passkey_key.py:180-184`

---

## CAP-U49-04 auth_passkey — Authentication Flow: _start_auth

`_start_auth()` is an `@api.model` method. It calls `generate_authentication_options` from the vendored webauthn library with `rp_id` set to the host portion of `self.get_base_url()` and `user_verification=UserVerificationRequirement.REQUIRED`. The resulting challenge is stored in `request.session['webauthn_challenge']`. The serialised authentication options JSON is returned.

Sources: `auth_passkey/models/auth_passkey_key.py:69-77`

---

## CAP-U49-05 auth_passkey — Authentication Verification: _verify_auth

`_verify_auth(auth, public_key, sign_count)` constructs `expected_origins` as a list containing the base URL plus `_VALID_APK_KEY_HASHES` (Android APK origins). It calls `verify_authentication_response` with `require_user_verification=True`. The session challenge is retrieved and consumed by `_get_session_challenge()` which calls `request.session.pop('webauthn_challenge', None)` — any attempt to reuse the challenge will fail. Returns `auth_verification.new_sign_count`.

Sources: `auth_passkey/models/auth_passkey_key.py:79-92`, `auth_passkey/models/auth_passkey_key.py:62-67`

---

## CAP-U49-06 auth_passkey — Registration Flow: _start_registration

`_start_registration()` calls `generate_registration_options` with `rp_name='Odoo'`, `user_id=str(self.env.user.id).encode()`, `user_name=self.env.user.login`, and `AuthenticatorSelectionCriteria(resident_key=ResidentKeyRequirement.REQUIRED, user_verification=UserVerificationRequirement.REQUIRED)`. The challenge is stored in `request.session['webauthn_challenge']`.

Sources: `auth_passkey/models/auth_passkey_key.py:94-108`

---

## CAP-U49-07 auth_passkey — Registration Verification: _verify_registration_options

`_verify_registration_options(registration)` calls the vendored `verify_registration_response` with `require_user_verification=True` and expected origins including APK hashes. Returns a dict with `credential_id` and `credential_public_key` from the verification object.

Sources: `auth_passkey/models/auth_passkey_key.py:110-124`

---

## CAP-U49-08 auth_passkey — Passkey Deletion: action_delete_passkey

`action_delete_passkey` is decorated with `@check_identity`. It only allows deletion of passkeys where `key.create_uid.id == self.env.user.id`. Deletion is routed through `self.env.user.write({'auth_passkey_key_ids': [Command.delete(key.id)]})` to trigger session token cache invalidation. After deletion, the session token is recomputed with `_compute_session_token`. Unauthorized deletion attempts are logged at INFO level with the requesting user, key ID, owner, and remote IP.

Sources: `auth_passkey/models/auth_passkey_key.py:126-143`

---

## CAP-U49-09 auth_passkey — Passkey Creation Wizard: AuthPasskeyKeyCreate

`AuthPasskeyKeyCreate` is a `TransientModel` (`_name = 'auth.passkey.key.create'`) with a `name` field (Char, required). Its `make_key(registration=None)` method is decorated with `@check_identity`. On success, it calls `_verify_registration_options`, writes the new key via `self.env.user.write({'auth_passkey_key_ids': [Command.create({...})]})`, then writes the public key via raw SQL, and recomputes the session token.

Sources: `auth_passkey/models/auth_passkey_key.py:160-194`

---

## CAP-U49-10 auth_passkey — res.users Integration: auth_passkey_key_ids

`ResUsers` adds `auth_passkey_key_ids = fields.One2many('auth.passkey.key', 'create_uid')` (line 14). The field is added to `SELF_READABLE_FIELDS` (line 17-18). `_get_session_token_fields` includes `auth_passkey_key_ids` (line 76). `_get_session_token_query_params` adds a LEFT JOIN on `auth_passkey_key` and aggregates key IDs into the session token query (lines 78-85).

Sources: `auth_passkey/models/res_users.py:14-85`

---

## CAP-U49-11 auth_passkey — Login Hook: _login Override

`ResUsers._login()` overrides the login method. When `credential['type'] == 'webauthn'`, it parses the JSON response, executes a SQL query joining `auth_passkey_key` to `res_users` to look up the `login` by `credential_identifier`, and sets `credential['login']` before delegating to `super()._login()`. Raises `AccessDenied('Unknown passkey')` if not found.

Sources: `auth_passkey/models/res_users.py:34-47`

---

## CAP-U49-12 auth_passkey — Credential Check: MFA Skip for Passkey

`ResUsers._check_credentials()` handles `type='webauthn'` by searching for the passkey by `create_uid` and `credential_identifier` (sudo). Calls `_verify_auth`. On success returns `{'uid': ..., 'auth_method': 'passkey', 'mfa': 'skip'}`. The `mfa: 'skip'` value means passkey authentication bypasses any additional MFA step.

Sources: `auth_passkey/models/res_users.py:49-73`

---

## CAP-U49-13 auth_passkey — Controller: start-auth Route

`WebauthnController` exposes `/auth/passkey/start-auth` as a JSON-RPC route with `auth='public'`. It calls `request.env['auth.passkey.key']._start_auth()` and returns the authentication options.

Sources: `auth_passkey/controllers/main.py:11-14`

---

## CAP-U49-14 auth_passkey — Controller: Android Asset Links

`WebauthnController` exposes `/.well-known/assetlinks.json` as a public HTTP route serving `_WEB_WELL_KNOW_ANDROID` as JSON, enabling Android passkey credential management for the `com.odoo.mobile` application.

Sources: `auth_passkey/controllers/main.py:16-20`

---

## CAP-U49-15 auth_passkey — CREDENTIAL_PARAMS Extension

`CREDENTIAL_PARAMS.append('webauthn_response')` is executed at import time (line 7), extending the web module's credential parameter list to include the WebAuthn response field.

Sources: `auth_passkey/controllers/main.py:7`

---

## CAP-U49-16 auth_passkey — Android Mobile Utils

`mobile_utils.py` defines `_get_app_sha256_cert_fingerprints()` returning `[("com.odoo.mobile", ["D6:73:20:02:CA:2D:..."])]` (one package, one SHA256 fingerprint). `_get_apk_key_hash()` converts a hex fingerprint to base64url format. `_VALID_APK_KEY_HASHES` is a list of strings in format `android:apk-key-hash:<b64>`. `_WEB_WELL_KNOW_ANDROID` includes relations `delegate_permission/common.handle_all_urls` and `delegate_permission/common.get_login_creds`.

Sources: `auth_passkey/mobile_utils.py:1-36`

---

## CAP-U49-17 auth_passkey — Deletion Logging

`AuthPasskeyKey.unlink()` overrides the base unlink to log INFO with format `"Passkey (#%d) deleted by %s (#%d) from %s"` including passkey ID, deleting user login, user ID, and remote IP (or 'n/a'). Creation is also logged in `make_key()` at INFO: `"Passkey (#%d) created by %s (#%d) from %s"` (line 186-190).

Sources: `auth_passkey/models/auth_passkey_key.py:42-50`, `auth_passkey/models/auth_passkey_key.py:185-191`

---

## CAP-U49-18 auth_passkey — Identity Check Integration

`ResUsersIdentitycheck` extends the `res.users.identitycheck` transient model by adding `('webauthn', 'Passkey')` to the `auth_method` selection (line 8). `_get_default_auth_method()` returns `'webauthn'` if `self.env.user.auth_passkey_key_ids` is truthy (line 11-15). `_check_identity()` for webauthn method calls `self.create_uid._check_credentials({'webauthn_response': context.get('password'), 'type': 'webauthn'}, {'interactive': True})`.

Sources: `auth_passkey/models/res_users_identitycheck.py:1-41`

---

## CAP-U49-19 auth_passkey — action_use_password Fallback

`action_use_password()` (line 30-41 in res_users_identitycheck.py) allows users to switch from passkey auth to password auth during identity check. Sets `auth_method = 'password'` and `password = ''`, then returns an `act_window` action to re-open the identity check form.

Sources: `auth_passkey/models/res_users_identitycheck.py:30-41`

---

## CAP-U49-20 auth_passkey — Security Rules

`security.xml` defines three `ir.rule` records. (1) `rule_auth_passkey_key_user`: users and portal users can only access passkeys where `create_uid = user.id`. (2) `rule_auth_passkey_key_create_portal`: users and portal can only modify their own creation wizard records. (3) `rule_auth_passkey_key_admin`: ERP managers can view and delete any passkey (domain `1=1`), but perm_write is 0 (cannot modify name etc.).

Sources: `auth_passkey/security/security.xml:1-33`

---

## CAP-U49-21 auth_passkey — Access Control Rules

`ir.model.access.csv` grants: internal users (group_user) read+write on `auth.passkey.key`; portal users read+write; ERP managers read+write+unlink. For `auth.passkey.key.create` transient: both user and portal groups get full CRUD. Note internal users and portal users have no create or unlink on `auth.passkey.key` itself (only on the wizard transient).

Sources: `auth_passkey/security/ir.model.access.csv:1-6`

---

## CAP-U49-22 auth_passkey — User Verification Enforcement

The unit test `test_check_user_verification` (lines 397-485 in test_passkey_demo.py) documents the enforcement: an authenticatorData without the UV flag (bit 2 of byte 33) is rejected with error `'User verification is required but user was not verified during authentication'`. The test comment explains the UV flag is bit 2 of the 33rd byte of authenticatorData per WebAuthn spec.

Sources: `auth_passkey/tests/test_passkey_demo.py:397-485`

---

## CAP-U49-23 auth_passkey — Replay Attack Prevention

The unit test `test_authentication` documents replay attack prevention: after a successful authentication, a second attempt with the same `webauthn_response` raises `'Cannot find a challenge for this session'` because `_get_session_challenge()` pops the challenge from the session (line 64-67 in auth_passkey_key.py). For passkeys supporting sign_count (YubiKey), same-challenge replay also fails due to sign count not incrementing.

Sources: `auth_passkey/tests/test_passkey_demo.py:296-310`, `auth_passkey/models/auth_passkey_key.py:62-67`

---

## CAP-U49-24 auth_passkey — action_rename_passkey

`action_rename_passkey()` returns an `ir.actions.act_window` dict opening the `auth_passkey.auth_passkey_key_rename` view as a medium dialog. No `@check_identity` decorator — renaming does not require identity confirmation.

Sources: `auth_passkey/models/auth_passkey_key.py:145-157`

---

## CAP-U49-25 auth_passkey — action_create_passkey on res.users

`ResUsers.action_create_passkey()` is `@check_identity` decorated and calls `self.env['auth.passkey.key']._start_registration()` inline in the returned wizard context. The wizard opens with `dialog_size: 'medium'`.

Sources: `auth_passkey/models/res_users.py:20-32`

---

## CAP-U49-26 auth_passkey_portal — Module Identity

The `auth_passkey_portal` module is named "Passkeys Portal", version 1.0, summary "Passkeys for portal users". Depends on `auth_passkey` and `portal`. `auto_install = True`. License LGPL-3. It does not define any Python model files beyond `__init__.py` and test files.

Sources: `auth_passkey_portal/__manifest__.py:1-28`

---

## CAP-U49-27 auth_passkey_portal — Portal Tests: Create, Rename, Delete

`PasskeyTestPortal` (tests/test_passkey_portal.py) creates a portal user with `group_portal`. `test_passkey_portal_create` runs tour `passkeys_portal_create` on `/my/security`. `test_passkey_portal_rename` reassigns a passkey to the portal user via raw SQL update, then runs tour `passkeys_portal_rename`. `test_passkey_portal_delete` runs tour `passkeys_portal_delete`.

Sources: `auth_passkey_portal/tests/test_passkey_portal.py:8-35`

---

## CAP-U49-28 auth_passkey_portal — Portal Permission Test

`test_portal_permissions` asserts that a portal user attempting to `write` on another user's passkey (`admin_passkey.with_user(self.portal_user).write({'name': 'test'})`) raises `AccessError`. This is enforced by the `rule_auth_passkey_key_user` record rule (`create_uid = user.id`).

Sources: `auth_passkey_portal/tests/test_passkey_portal.py:37-40`

---

## CAP-U49-29 auth_password_policy_portal — Module Identity

The `auth_password_policy_portal` module depends on `auth_password_policy` and `portal`. `auto_install = True`. License LGPL-3. It provides a controller, one model extension, and one view template.

Sources: `auth_password_policy_portal/__manifest__.py:1-9` (manifest read)

---

## CAP-U49-30 auth_password_policy_portal — Controller: Portal Layout Values

`CustomerPortalPasswordPolicy` extends `CustomerPortal._prepare_portal_layout_values()`. It calls `super()._prepare_portal_layout_values()` then adds `d['password_minimum_length'] = request.env['ir.config_parameter'].sudo().get_param('auth_password_policy.minlength')` to the returned dict, making the minimum password length available to portal templates.

Sources: `auth_password_policy_portal/controllers.py:1-10`

---

## CAP-U49-31 auth_password_policy_portal — Frontend Translation Module

`IrHttp` extends `ir.http` with `_get_translation_frontend_modules_name()` returning `mods + ['auth_password_policy']`. This makes password policy JavaScript translations available on portal pages.

Sources: `auth_password_policy_portal/models/ir_http.py:1-11`

---

## CAP-U49-32 auth_password_policy_signup — Module Identity

The `auth_password_policy_signup` module is named "Password Policy support for Signup". Depends on `auth_password_policy` and `auth_signup`. `auto_install = True`. License LGPL-3. Assets include `auth_password_policy/static/src/password_meter.js` and `auth_password_policy/static/src/password_policy.js` in the frontend bundle.

Sources: `auth_password_policy_signup/__manifest__.py:1-18`

---

## CAP-U49-33 auth_password_policy_signup — Controller: Signup Config

`AddPolicyData` extends `AuthSignupHome.get_auth_signup_config()`. It calls `super().get_auth_signup_config()` then adds `d['password_minimum_length'] = request.env['ir.config_parameter'].sudo().get_param('auth_password_policy.minlength')`, injecting the minimum password length into the signup page configuration data.

Sources: `auth_password_policy_signup/controllers.py:1-10`

---

## CAP-U49-34 auth_totp (residual) — TOTP Algorithm Constants

`totp.py` defines: `TOTP_SECRET_SIZE = 160` (bits, RFC 4226 R6 recommendation), `ALGORITHM = 'sha1'`, `DIGITS = 6`, `TIMESTEP = 30` (seconds). The comment notes Google Authenticator supports 160 bits but uses 80 by default.

Sources: `auth_totp/models/totp.py:10-17`

---

## CAP-U49-35 auth_totp (residual) — TOTP.match Window

`TOTP.match(code, t=None, window=TIMESTEP, timestep=TIMESTEP)` computes `low = int((t - window) / timestep)` and `high = int((t + window) / timestep) + 1`, then iterates over counters in that range. Default window equals one full 30-second period, so codes from `t-30` to `t+30` are accepted.

Sources: `auth_totp/models/totp.py:23-41`

---

## CAP-U49-36 auth_totp (residual) — HOTP Implementation

`hotp(secret, counter)` packs counter as 64-bit big-endian (`struct.pack(">Q", counter)`), computes `hmac.new(secret, msg=C, digestmod=ALGORITHM).digest()` with SHA1, extracts offset from last nibble of MAC, reads 4 bytes at offset as 31-bit big-endian unsigned int, returns `code % (10 ** DIGITS)` (6 digits).

Sources: `auth_totp/models/totp.py:43-56`

---

## CAP-U49-37 auth_totp (residual) — auth_totp.device Model

`Auth_TotpDevice` has `_name = 'auth_totp.device'`, `_inherit = ["res.users.apikeys"]`, `_description = "Authentication Device"`, `_auto = False`. The `_auto = False` means the ORM does not auto-create a table; the table is shared with `res.users.apikeys`. Method `_check_credentials_for_uid(scope, key, uid)` returns `True` if `_check_credentials(scope, key) == uid`.

Sources: `auth_totp/models/auth_totp.py:9-23`

---

## CAP-U49-38 auth_totp (residual) — Trusted Device Age Config

`_get_trusted_device_age()` reads `ir.config_parameter` key `auth_totp.trusted_device_age`, defaulting to `TRUSTED_DEVICE_AGE_DAYS = 90`. If the value is `<= 0` or not a valid integer, it falls back to 90 days with a WARNING log. Returns the value in seconds (`nbr_days * 86400`).

Sources: `auth_totp/models/auth_totp.py:25-38`

---

## CAP-U49-39 auth_totp (residual) — Rate Limiting: TOTP_RATE_LIMITS

`TOTP_RATE_LIMITS = {'send_email': (5, 3600), 'code_check': (5, 3600)}` (line 24-27). Each limit type allows 5 attempts per 3600 seconds (1 hour).

Sources: `auth_totp/models/res_users.py:24-27`

---

## CAP-U49-40 auth_totp (residual) — _totp_rate_limit Implementation

`_totp_rate_limit(limit_type)` counts `auth.totp.rate.limit.log` records for the user within the interval. If count >= limit, raises `AccessDenied` with the appropriate error message. Creates a new log record on each call. Requires a request context.

Sources: `auth_totp/models/res_users.py:120-143`

---

## CAP-U49-41 auth_totp (residual) — Rate Limit Purge on Success

`_totp_rate_limit_purge(limit_type)` calls `unlink()` on all rate limit log records for the user and limit_type. This is called on successful TOTP code check (line 90 in res_users.py).

Sources: `auth_totp/models/res_users.py:145-152`

---

## CAP-U49-42 auth_totp (residual) — auth.totp.rate.limit.log Model

`AuthTotpRateLimitLog` is a `TransientModel` with `_name = 'auth.totp.rate.limit.log'`. Fields: `user_id` (Many2one `res.users`, required, readonly), `ip` (Char, readonly), `limit_type` (Selection: `send_email`/`code_check`, readonly). Database index on `(user_id, limit_type, create_date)`.

Sources: `auth_totp/models/auth_totp_rate_limit_log.py:1-16`

---

## CAP-U49-43 auth_totp (residual) — _check_credentials for TOTP

`_check_credentials` for type `'totp'` calls `_totp_rate_limit('code_check')`, decodes `sudo.totp_secret` from base32, calls `TOTP(key).match(credentials['token'])`. If `match is None`, raises `AccessDenied("Verification failed, please double-check the 6-digit code")`. If `match <= sudo.totp_last_counter`, raises `AccessDenied("...please use the latest 6-digit code")` to prevent counter reuse. On success updates `totp_last_counter` and purges rate limit logs. Returns `{'uid': ..., 'auth_method': 'totp', 'mfa': 'default'}`.

Sources: `auth_totp/models/res_users.py:74-96`

---

## CAP-U49-44 auth_totp (residual) — TOTP Enable: _totp_try_setting

`_totp_try_setting(secret, code)` rejects if TOTP already enabled or if `self != self.env.user`. Strips whitespace and uppercases the secret. Verifies the code, then writes `totp_secret` and `totp_last_counter` via sudo. Recomputes and updates session token to prevent logout.

Sources: `auth_totp/models/res_users.py:98-118`

---

## CAP-U49-45 auth_totp (residual) — TOTP Disable: action_totp_disable

`action_totp_disable` is `@check_identity` decorated. Allows the user themselves, admins, or sudo. Calls `revoke_all_devices()` before setting `totp_secret = False`. Recomputes session token. Returns a client action notification of type 'warning'.

Sources: `auth_totp/models/res_users.py:154-179`

---

## CAP-U49-46 auth_totp (residual) — Password Change Revokes Devices

`change_password(old_passwd, new_passwd)` calls `self.env.user._revoke_all_devices()` before `super().change_password()`. This means changing a password automatically revokes all TOTP trusted devices.

Sources: `auth_totp/models/res_users.py:214-217`

---

## CAP-U49-47 auth_totp (residual) — RPC API Keys Only When TOTP Enabled

`_rpc_api_keys_only()` returns `True` if `self.totp_enabled or super()._rpc_api_keys_only()`. This means a user with TOTP enabled cannot use password-based XML-RPC; they must use API keys.

Sources: `auth_totp/models/res_users.py:66-69`

---

## CAP-U49-48 auth_totp (residual) — TOTP Enable Wizard: auth_totp.wizard

`Auth_TotpWizard` (`_name = 'auth_totp.wizard'`) has fields: `user_id` (Many2one res.users, required, readonly), `secret` (Char, required, readonly), `url` and `qrcode` (Binary, computed, stored). `_compute_qrcode` builds an `otpauth://totp/...` URI including `issuer:login` as the path, with `secret`, `issuer`, `algorithm`, `digits`, `period` as query parameters. A QR code PNG is generated in memory using the `qrcode` library and stored as base64.

Sources: `auth_totp/wizard/auth_totp_wizard.py:21-56`

---

## CAP-U49-49 auth_totp (residual) — Wizard enable Method

`Auth_TotpWizard.enable()` is `@check_identity` decorated. Retrieves the code from `self.env.context.get('code', '')`, converts to integer (raises UserError if non-numeric). Calls `user_id._totp_try_setting(secret, code)`. On success, clears `self.secret` and returns a client notification.

Sources: `auth_totp/wizard/auth_totp_wizard.py:58-75`

---

## CAP-U49-50 auth_totp (residual) — Trusted Device Cookie

`TRUSTED_DEVICE_COOKIE = 'td_id'` (line 11). `TRUSTED_DEVICE_AGE_DAYS = 90` (line 12). On POST with `remember=True`, the device cookie is set with `httponly=True`, `samesite='Lax'`, max_age derived from `_get_trusted_device_age()`. Device name includes browser name, platform, and GeoIP city/country if available.

Sources: `auth_totp/controllers/home.py:11-12`, `auth_totp/controllers/home.py:60-81`

---

## CAP-U49-51 auth_totp (residual) — /web/login/totp Route

`Home.web_totp` handles `GET` and `POST` to `/web/login/totp`. On GET, if a `td_id` cookie exists, checks it via `auth_totp.device._check_credentials_for_uid(scope='browser', key=key, uid=user.id)` and finalises the session on match. On POST, the token is parsed from `kwargs['totp_token']` (whitespace stripped via `re.sub(r'\s', '')`).

Sources: `auth_totp/controllers/home.py:15-92`

---

## CAP-U49-52 auth_totp (residual) — Session Token Includes totp_secret

`_get_session_token_fields()` adds `'totp_secret'` to the set of fields included in the session token computation. This means enabling or disabling TOTP invalidates all existing sessions for that user.

Sources: `auth_totp/models/res_users.py:71-72`

---

## CAP-U49-53 auth_totp (residual) — TOTP Enable Wizard Launch: action_totp_enable_wizard

`action_totp_enable_wizard()` is `@check_identity` decorated. Enforces that TOTP can only be enabled for `self == self.env.user`. Generates `TOTP_SECRET_SIZE // 8 = 20` random bytes, encodes as base32, formats in groups of 4 chars for readability. Creates `auth_totp.wizard` record and returns an act_window.

Sources: `auth_totp/models/res_users.py:181-205`

---

## CAP-U49-54 auth_totp (residual) — _mfa_type and _mfa_url

`_mfa_type()` returns `'totp'` if `self.totp_enabled` and super returns None (line 47-52). `_mfa_url()` returns `'/web/login/totp'` if `_mfa_type() == 'totp'` (line 54-59).

Sources: `auth_totp/models/res_users.py:47-59`

---

## CAP-U49-55 auth_totp_portal — Module Identity

`auth_totp_portal` is named "TOTPortal". Depends on `portal` and `auth_totp`. `auto_install = True`. License LGPL-3. Includes `security/security.xml` and `views/templates.xml` in data.

Sources: `auth_totp_portal/__manifest__.py:1-20`

---

## CAP-U49-56 auth_totp_portal — get_totp_invite_url Override

`ResUsers.get_totp_invite_url()` overrides the base method. For non-internal users (`not self._is_internal()`), it returns `'/my/security'`. For internal users it delegates to `super()`.

Sources: `auth_totp_portal/models/res_users.py:10-14`

---

## CAP-U49-57 auth_totp_portal — Test: Portal TOTP Tours

`TestTOTPortal` extends `HttpCaseWithUserPortal` and `TestTOTPMixin`. The `test_totp` method runs three tours sequentially: `totportal_tour_setup` at `/my/security` (login='portal'), `totportal_login_enabled` at `/` (no login), and `totportal_login_disabled` at `/` (no login). The test also disables TOTP as part of the second tour.

Sources: `auth_totp_portal/tests/test_tour.py:10-22`

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U49-C001 | auth_passkey-manifest | auth_passkey/__manifest__.py:5 | `'version': '1.1'` | FACT | — | — | auth_passkey module version is 1.1 | N-U49-001 |
| VDR-U49-C002 | auth_passkey-manifest | auth_passkey/__manifest__.py:13 | `'depends': ['base_setup', 'web']` | FACT | — | — | Depends on base_setup and web only | N-U49-001 |
| VDR-U49-C003 | auth_passkey-manifest | auth_passkey/__manifest__.py:14 | `'auto_install': True` | FACT | — | — | Module auto-installs when dependencies are present | N-U49-001 |
| VDR-U49-C004 | auth_passkey-manifest | auth_passkey/__manifest__.py:10 | when a user logs in with a passkey | FACT | — | C1 | Passkey authentication bypasses MFA by design | N-U49-002 |
| VDR-U49-C005 | auth_passkey.key-model | auth_passkey/models/auth_passkey_key.py:22 | `_name = 'auth.passkey.key'` | FACT | — | — | Model technical name is auth.passkey.key | N-U49-003 |
| VDR-U49-C006 | auth_passkey.key-fields | auth_passkey/models/auth_passkey_key.py:27 | `credential_identifier = fields.Char(required=True, groups='base.group_system')` | FACT | — | C1 | credential_identifier is restricted to system group | N-U49-003 |
| VDR-U49-C007 | auth_passkey.key-fields | auth_passkey/models/auth_passkey_key.py:28 | `public_key = fields.Char(required=True, groups='base.group_system'` | FACT | — | C1 | public_key field restricted to system group | N-U49-003 |
| VDR-U49-C008 | auth_passkey.key-fields | auth_passkey/models/auth_passkey_key.py:29 | `sign_count = fields.Integer(default=0, groups='base.group_system')` | FACT | — | C1 | sign_count field restricted to system group, default 0 | N-U49-003 |
| VDR-U49-C009 | auth_passkey.key-constraint | auth_passkey/models/auth_passkey_key.py:32 | `'UNIQUE(credential_identifier)'` | FACT | — | C1 | DB-level unique constraint on credential_identifier | N-U49-003 |
| VDR-U49-C010 | auth_passkey.key-init | auth_passkey/models/auth_passkey_key.py:39 | `if not sql.column_exists(self.env.cr, 'auth_passkey_key', 'public_key'):` | FACT | — | — | Column existence check before ALTER TABLE | N-U49-003 |
| VDR-U49-C011 | auth_passkey.key-pubkey-raw | auth_passkey/models/auth_passkey_key.py:53 | `query = 'SELECT public_key FROM auth_passkey_key WHERE id = %s'` | FACT | — | C1 | Public key read via raw SQL bypassing field groups | N-U49-003 |
| VDR-U49-C012 | auth_passkey.key-pubkey-inverse | auth_passkey/models/auth_passkey_key.py:59 | `def _inverse_public_key(self):` | FACT | — | — | Inverse is a no-op pass; write is via raw SQL only | N-U49-003 |
| VDR-U49-C013 | auth_passkey.key-challenge | auth_passkey/models/auth_passkey_key.py:64 | `challenge = request.session.pop('webauthn_challenge', None)` | FACT | — | C1 | Challenge is consumed (pop) from session; prevents reuse | N-U49-004 |
| VDR-U49-C014 | auth_passkey.key-start-auth | auth_passkey/models/auth_passkey_key.py:72 | `rp_id=url_parse(self.get_base_url()).host` | FACT | RT | C1 | RP ID derived from system base URL at runtime | N-U49-004 |
| VDR-U49-C015 | auth_passkey.key-start-auth | auth_passkey/models/auth_passkey_key.py:73 | `user_verification=UserVerificationRequirement.REQUIRED` | FACT | — | C1 | User verification required for authentication options | N-U49-004 |
| VDR-U49-C016 | auth_passkey.key-verify-auth | auth_passkey/models/auth_passkey_key.py:82 | `expected_origins = [parsed_url.replace(path='').to_url()] + _VALID_APK_KEY_HASHES` | FACT | — | C1 | Android APK origins included in expected origins | N-U49-004 |
| VDR-U49-C017 | auth_passkey.key-verify-auth | auth_passkey/models/auth_passkey_key.py:90 | `require_user_verification=True` | FACT | — | C1 | User verification enforced on authentication response | N-U49-004 |
| VDR-U49-C018 | auth_passkey.key-verify-auth | auth_passkey/models/auth_passkey_key.py:92 | `return auth_verification.new_sign_count` | FACT | — | — | New sign count returned from verification | N-U49-004 |
| VDR-U49-C019 | auth_passkey.key-registration | auth_passkey/models/auth_passkey_key.py:99 | `rp_name='Odoo'` | FACT | — | — | Relying party name is hardcoded as 'Odoo' | N-U49-005 |
| VDR-U49-C020 | auth_passkey.key-registration | auth_passkey/models/auth_passkey_key.py:100 | `user_id=str(self.env.user.id).encode()` | FACT | — | — | User handle is string-encoded numeric user ID | N-U49-005 |
| VDR-U49-C021 | auth_passkey.key-registration | auth_passkey/models/auth_passkey_key.py:103 | `resident_key=ResidentKeyRequirement.REQUIRED` | FACT | — | C1 | Resident key required — credential must be discoverable | N-U49-005 |
| VDR-U49-C022 | auth_passkey.key-registration | auth_passkey/models/auth_passkey_key.py:104 | `user_verification=UserVerificationRequirement.REQUIRED` | FACT | — | C1 | User verification required during registration | N-U49-005 |
| VDR-U49-C023 | auth_passkey.key-delete | auth_passkey/models/auth_passkey_key.py:126 | `@check_identity` | FACT | — | C1 | Passkey deletion requires identity check | N-U49-006 |
| VDR-U49-C024 | auth_passkey.key-delete | auth_passkey/models/auth_passkey_key.py:129 | `if key.create_uid.id == self.env.user.id:` | FACT | — | C1 | User can only delete their own passkeys | N-U49-006 |
| VDR-U49-C025 | auth_passkey.key-delete | auth_passkey/models/auth_passkey_key.py:133 | `self.env.user.write({'auth_passkey_key_ids': [Command.delete(key.id)]})` | FACT | — | — | Deletion via res.users.write to trigger session token invalidation | N-U49-006 |
| VDR-U49-C026 | auth_passkey.key-delete | auth_passkey/models/auth_passkey_key.py:134 | `new_token = self.env.user._compute_session_token(request.session.sid)` | FACT | RT | C1 | Session token recomputed after passkey deletion | N-U49-006 |
| VDR-U49-C027 | auth_passkey.key.create-wizard | auth_passkey/models/auth_passkey_key.py:166 | `@check_identity` | FACT | — | C1 | Passkey creation wizard requires identity check | N-U49-005 |
| VDR-U49-C028 | auth_passkey.key.create-wizard | auth_passkey/models/auth_passkey_key.py:175 | `self.env.user.write({'auth_passkey_key_ids': [Command.create({` | FACT | — | — | Passkey created via res.users.write for session token invalidation | N-U49-005 |
| VDR-U49-C029 | auth_passkey.key.create-wizard | auth_passkey/models/auth_passkey_key.py:180 | `self.env.cr.execute(SQL(` | FACT | — | C1 | Public key written via raw SQL to bypass field group restriction | N-U49-005 |
| VDR-U49-C030 | auth_passkey-res_users | auth_passkey/models/res_users.py:14 | `auth_passkey_key_ids = fields.One2many('auth.passkey.key', 'create_uid')` | FACT | — | — | res.users has One2many to auth.passkey.key | N-U49-003 |
| VDR-U49-C031 | auth_passkey-res_users | auth_passkey/models/res_users.py:35 | `if credential['type'] == 'webauthn':` | FACT | — | — | Login method branches on credential type 'webauthn' | N-U49-004 |
| VDR-U49-C032 | auth_passkey-res_users | auth_passkey/models/res_users.py:38 | SELECT login | FACT | — | C1 | Login lookup by credential_identifier via raw SQL | N-U49-004 |
| VDR-U49-C033 | auth_passkey-res_users | auth_passkey/models/res_users.py:69 | `'mfa': 'skip'` | FACT | — | C1 | Passkey auth returns mfa='skip', bypassing MFA | N-U49-002 |
| VDR-U49-C034 | auth_passkey-res_users | auth_passkey/models/res_users.py:66 | `passkey.sign_count = new_sign_count` | FACT | — | C1 | Sign count updated after successful authentication | N-U49-004 |
| VDR-U49-C035 | auth_passkey-res_users | auth_passkey/models/res_users.py:76 | auth_passkey_key_ids | FACT | — | C1 | Passkey key IDs included in session token fields | N-U49-007 |
| VDR-U49-C036 | auth_passkey-controller | auth_passkey/controllers/main.py:11 | `@http.route(['/auth/passkey/start-auth'], type='jsonrpc', auth='public')` | FACT | — | C1 | start-auth route is public (no authentication required) | N-U49-004 |
| VDR-U49-C037 | auth_passkey-controller | auth_passkey/controllers/main.py:16 | `@http.route(['/.well-known/assetlinks.json'], type='http', auth='public')` | FACT | — | — | assetlinks.json served publicly for Android integration | N-U49-008 |
| VDR-U49-C038 | auth_passkey-android | auth_passkey/mobile_utils.py:7 | `("com.odoo.mobile", [` | FACT | — | — | Only one Android package registered: com.odoo.mobile | N-U49-008 |
| VDR-U49-C039 | auth_passkey-android | auth_passkey/mobile_utils.py:17 | `_VALID_APK_KEY_HASHES = [` | FACT | — | — | APK key hashes computed from certificate fingerprints | N-U49-008 |
| VDR-U49-C040 | auth_passkey-android | auth_passkey/mobile_utils.py:25 | `"delegate_permission/common.get_login_creds"` | FACT | — | — | get_login_creds permission required for passkey credential sharing | N-U49-008 |
| VDR-U49-C041 | auth_passkey-identitycheck | auth_passkey/models/res_users_identitycheck.py:8 | `auth_method = fields.Selection(selection_add=[('webauthn', 'Passkey')])` | FACT | — | — | webauthn added to identity check auth method selection | N-U49-009 |
| VDR-U49-C042 | auth_passkey-identitycheck | auth_passkey/models/res_users_identitycheck.py:12 | `if self.env.user.auth_passkey_key_ids:` | FACT | — | — | Default auth method is webauthn if user has any passkeys | N-U49-009 |
| VDR-U49-C043 | auth_passkey-identitycheck | auth_passkey/models/res_users_identitycheck.py:20 | `'webauthn_response': self.env.context.get('password'),` | FACT | RT | C1 | webauthn_response passed via context key 'password' during identity check | N-U49-009 |
| VDR-U49-C044 | auth_passkey-security | auth_passkey/security/security.xml:10 | `<field name="domain_force">[('create_uid', '=', user.id)]</field>` | FACT | — | C1 | Record rule restricts passkey access to owner only | N-U49-010 |
| VDR-U49-C045 | auth_passkey-security | auth_passkey/security/security.xml:23 | `<field name="name">Passkeys: Admins can view and delete other peoples Passkeys</field>` | FACT | — | C1 | ERP managers can view and delete any user's passkeys | N-U49-010 |
| VDR-U49-C046 | auth_passkey-security | auth_passkey/security/security.xml:29 | `<field name="perm_write" eval="0"/>` | FACT | — | C1 | Admins cannot write (rename) other users' passkeys | N-U49-010 |
| VDR-U49-C047 | auth_passkey-acl | auth_passkey/security/ir.model.access.csv:2 | `model_auth_passkey_key,base.group_user,1,1,0,0` | FACT | — | C1 | Internal users: read+write, no create or unlink on auth.passkey.key | N-U49-010 |
| VDR-U49-C048 | auth_passkey-acl | auth_passkey/security/ir.model.access.csv:3 | `model_auth_passkey_key,base.group_portal,1,1,0,0` | FACT | — | C1 | Portal users: read+write, no create or unlink on auth.passkey.key | N-U49-010 |
| VDR-U49-C049 | auth_passkey-acl | auth_passkey/security/ir.model.access.csv:4 | `model_auth_passkey_key,base.group_erp_manager,1,1,0,1` | FACT | — | C1 | ERP managers have unlink on auth.passkey.key | N-U49-010 |
| VDR-U49-C050 | auth_passkey-portal | auth_passkey_portal/__manifest__.py:13 | 'depends': ['auth_passkey', 'portal'] | FACT | — | — | auth_passkey_portal depends on auth_passkey and portal | N-U49-011 |
| VDR-U49-C051 | auth_passkey-portal | auth_passkey_portal/__manifest__.py:27 | 'auto_install': True | FACT | — | — | auth_passkey_portal auto-installs when auth_passkey and portal are present | N-U49-011 |
| VDR-U49-C052 | auth_passkey-portal-test | auth_passkey_portal/tests/test_passkey_portal.py:18 | group_ids | FACT | — | — | Test creates portal user in group_portal | N-U49-011 |
| VDR-U49-C053 | auth_passkey-portal-test | auth_passkey_portal/tests/test_passkey_portal.py:25 | `self.start_tour("/my/security?debug=tests", 'passkeys_portal_create'` | FACT | RT | — | Portal passkey creation tour runs at /my/security | N-U49-011 |
| VDR-U49-C054 | auth_passkey-portal-test | auth_passkey_portal/tests/test_passkey_portal.py:39 | `with self.assertRaises(AccessError):` | FACT | — | C1 | Portal user writing another's passkey raises AccessError | N-U49-010 |
| VDR-U49-C055 | auth_pwd_policy_portal-ctrl | auth_password_policy_portal/controllers.py:9 | `d['password_minimum_length'] = request.env['ir.config_parameter'].sudo().get_param('auth_password_policy.minlength')` | FACT | RT | — | Portal layout provides password_minimum_length from system parameter | N-U49-012 |
| VDR-U49-C056 | auth_pwd_policy_portal-irhttp | auth_password_policy_portal/models/ir_http.py:11 | `return mods + ['auth_password_policy']` | FACT | — | — | auth_password_policy translations available on portal frontend | N-U49-012 |
| VDR-U49-C057 | auth_pwd_policy_portal-manifest | auth_password_policy_portal/__manifest__.py:3 | `'depends': ['auth_password_policy', 'portal']` | FACT | — | — | auth_password_policy_portal depends on auth_password_policy and portal | N-U49-012 |
| VDR-U49-C058 | auth_pwd_policy_signup-ctrl | auth_password_policy_signup/controllers.py:9 | `d['password_minimum_length'] = request.env['ir.config_parameter'].sudo().get_param('auth_password_policy.minlength')` | FACT | RT | — | Signup config provides password_minimum_length from system parameter | N-U49-013 |
| VDR-U49-C059 | auth_pwd_policy_signup-manifest | auth_password_policy_signup/__manifest__.py:3 | `'depends': ['auth_password_policy', 'auth_signup']` | FACT | — | — | auth_password_policy_signup depends on auth_password_policy and auth_signup | N-U49-013 |
| VDR-U49-C060 | auth_pwd_policy_signup-assets | auth_password_policy_signup/__manifest__.py:14 | `'auth_password_policy/static/src/password_meter.js'` | FACT | — | — | Password meter JS from auth_password_policy loaded on signup frontend | N-U49-013 |
| VDR-U49-C061 | auth_totp-totp-constants | auth_totp/models/totp.py:10 | `TOTP_SECRET_SIZE = 160` | FACT | — | — | TOTP secret size is 160 bits (per RFC 4226 R6) | N-U49-014 |
| VDR-U49-C062 | auth_totp-totp-constants | auth_totp/models/totp.py:15 | `ALGORITHM = 'sha1'` | FACT | — | — | TOTP algorithm is SHA-1 | N-U49-014 |
| VDR-U49-C063 | auth_totp-totp-constants | auth_totp/models/totp.py:16 | `DIGITS = 6` | FACT | — | — | TOTP produces 6 digits | N-U49-014 |
| VDR-U49-C064 | auth_totp-totp-constants | auth_totp/models/totp.py:17 | `TIMESTEP = 30` | FACT | — | — | TOTP time step is 30 seconds | N-U49-014 |
| VDR-U49-C065 | auth_totp-match-window | auth_totp/models/totp.py:35 | `low = int((t - window) / timestep)` | FACT | — | — | Matching window is ±1 time step (±30 seconds) | N-U49-014 |
| VDR-U49-C066 | auth_totp-hotp | auth_totp/models/totp.py:43 | `def hotp(secret, counter):` | FACT | — | — | HOTP computation follows RFC 4226: HMAC-SHA1, offset from last nibble | N-U49-014 |
| VDR-U49-C067 | auth_totp-device | auth_totp/models/auth_totp.py:16 | `_name = 'auth_totp.device'` | FACT | — | — | auth_totp.device model name | N-U49-015 |
| VDR-U49-C068 | auth_totp-device | auth_totp/models/auth_totp.py:17 | `_inherit = ["res.users.apikeys"]` | FACT | — | — | auth_totp.device inherits from res.users.apikeys | N-U49-015 |
| VDR-U49-C069 | auth_totp-device | auth_totp/models/auth_totp.py:19 | `_auto = False` | FACT | — | — | No separate table; shares table with res.users.apikeys | N-U49-015 |
| VDR-U49-C070 | auth_totp-device-age | auth_totp/models/auth_totp.py:28 | `ICP.get_param('auth_totp.trusted_device_age', TRUSTED_DEVICE_AGE_DAYS)` | FACT | RT | — | Trusted device age configurable via system parameter auth_totp.trusted_device_age | N-U49-015 |
| VDR-U49-C071 | auth_totp-device-age | auth_totp/models/auth_totp.py:38 | `return nbr_days * 86400  # seconds` | FACT | — | — | Trusted device age returned in seconds | N-U49-015 |
| VDR-U49-C072 | auth_totp-rate-limits | auth_totp/models/res_users.py:24 | `TOTP_RATE_LIMITS = {` | FACT | — | C1 | Rate limits defined as module-level constant | N-U49-016 |
| VDR-U49-C073 | auth_totp-rate-limits | auth_totp/models/res_users.py:25 | `'send_email': (5, 3600),` | FACT | — | C1 | Email TOTP rate limit: 5 per hour | N-U49-016 |
| VDR-U49-C074 | auth_totp-rate-limits | auth_totp/models/res_users.py:26 | `'code_check': (5, 3600),` | FACT | — | C1 | Code check rate limit: 5 per hour | N-U49-016 |
| VDR-U49-C075 | auth_totp-check-cred | auth_totp/models/res_users.py:76 | `self._totp_rate_limit('code_check')` | FACT | — | C1 | Rate limit checked before each TOTP credential verification | N-U49-016 |
| VDR-U49-C076 | auth_totp-check-cred | auth_totp/models/res_users.py:84 | `if sudo.totp_last_counter and match <= sudo.totp_last_counter:` | FACT | — | C1 | TOTP code reuse prevented via last_counter check | N-U49-014 |
| VDR-U49-C077 | auth_totp-check-cred | auth_totp/models/res_users.py:91 | `'mfa': 'default'` | FACT | — | — | TOTP check returns mfa='default' (not skip) | N-U49-014 |
| VDR-U49-C078 | auth_totp-rpc | auth_totp/models/res_users.py:69 | `return self.totp_enabled or super()._rpc_api_keys_only()` | FACT | — | C1 | TOTP-enabled users cannot use password-based RPC | N-U49-014 |
| VDR-U49-C079 | auth_totp-disable | auth_totp/models/res_users.py:154 | `@check_identity` | FACT | — | C1 | TOTP disable requires identity check | N-U49-017 |
| VDR-U49-C080 | auth_totp-disable | auth_totp/models/res_users.py:161 | `self.revoke_all_devices()` | FACT | — | C1 | All trusted devices revoked when TOTP disabled | N-U49-017 |
| VDR-U49-C081 | auth_totp-pwd-change | auth_totp/models/res_users.py:216 | `self.env.user._revoke_all_devices()` | FACT | — | C1 | Password change revokes all TOTP trusted devices | N-U49-017 |
| VDR-U49-C082 | auth_totp-rate-log | auth_totp/models/auth_totp_rate_limit_log.py:5 | `_name = 'auth.totp.rate.limit.log'` | FACT | — | — | Rate limit log model is a TransientModel | N-U49-016 |
| VDR-U49-C083 | auth_totp-rate-log | auth_totp/models/auth_totp_rate_limit_log.py:8 | `_user_id_limit_type_create_date_idx = models.Index("(user_id, limit_type, create_date)")` | FACT | — | — | Compound index on user_id, limit_type, create_date for rate limit queries | N-U49-016 |
| VDR-U49-C084 | auth_totp-wizard-qr | auth_totp/wizard/auth_totp_wizard.py:40 | `issuer = global_issuer or w.user_id.company_id.display_name` | FACT | RT | — | QR code issuer is HTTP host or company display name | N-U49-017 |
| VDR-U49-C085 | auth_totp-wizard-qr | auth_totp/wizard/auth_totp_wizard.py:49 | `'algorithm': ALGORITHM.upper(),` | FACT | — | — | Algorithm in QR URI is uppercase ('SHA1') per Google Authenticator requirement | N-U49-017 |
| VDR-U49-C086 | auth_totp-controller-cookie | auth_totp/controllers/home.py:11 | `TRUSTED_DEVICE_COOKIE = 'td_id'` | FACT | — | C1 | Trusted device cookie name is 'td_id' | N-U49-015 |
| VDR-U49-C087 | auth_totp-controller-cookie | auth_totp/controllers/home.py:79 | httponly=True | FACT | — | C1 | Trusted device cookie is HttpOnly | N-U49-015 |
| VDR-U49-C088 | auth_totp-controller-cookie | auth_totp/controllers/home.py:80 | samesite='Lax' | FACT | — | C1 | Trusted device cookie SameSite=Lax | N-U49-015 |
| VDR-U49-C089 | auth_totp-controller-geoip | auth_totp/controllers/home.py:66 | `if request.geoip.city.name:` | FACT | RT | — | Device name includes GeoIP city/country if available | N-U49-015 |
| VDR-U49-C090 | auth_totp-controller-route | auth_totp/controllers/home.py:16 | `'/web/login/totp'` | FACT | — | — | TOTP verification page route is /web/login/totp | N-U49-018 |
| VDR-U49-C091 | auth_totp-controller-route | auth_totp/controllers/home.py:19 | `website=True, multilang=False` | FACT | — | — | TOTP route is website=True but multilang=False | N-U49-018 |
| VDR-U49-C092 | auth_totp-session-token | auth_totp/models/res_users.py:72 | totp_secret | FACT | — | C1 | totp_secret changes invalidate all user sessions | N-U49-014 |
| VDR-U49-C093 | auth_totp-enable-wizard | auth_totp/models/res_users.py:189 | `secret_bytes_count = TOTP_SECRET_SIZE // 8` | FACT | — | — | Secret is 20 random bytes (160 bits) from os.urandom | N-U49-017 |
| VDR-U49-C094 | auth_totp-enable-wizard | auth_totp/models/res_users.py:192 | `secret = ' '.join(map(''.join, zip(*[iter(secret)]*4)))` | FACT | — | — | Secret formatted in groups of 4 characters for readability | N-U49-017 |
| VDR-U49-C095 | auth_totp_portal-manifest | auth_totp_portal/__manifest__.py:2 | `'name': "TOTPortal"` | FACT | — | — | Module named TOTPortal | N-U49-019 |
| VDR-U49-C096 | auth_totp_portal-manifest | auth_totp_portal/__manifest__.py:4 | `'depends': ['portal', 'auth_totp']` | FACT | — | — | auth_totp_portal depends on portal and auth_totp | N-U49-019 |
| VDR-U49-C097 | auth_totp_portal-url | auth_totp_portal/models/res_users.py:12 | `return '/my/security'` | FACT | — | — | TOTP invite URL for portal users is /my/security | N-U49-019 |
| VDR-U49-C098 | auth_totp_portal-url | auth_totp_portal/models/res_users.py:11 | `if not self._is_internal():` | FACT | — | — | Non-internal users directed to portal security page | N-U49-019 |
| VDR-U49-C099 | auth_totp_portal-test | auth_totp_portal/tests/test_tour.py:18 | `self.start_tour('/my/security', 'totportal_tour_setup', login='portal')` | FACT | RT | — | Portal TOTP setup tour runs at /my/security with portal login | N-U49-019 |
| VDR-U49-C100 | auth_totp-mfa-url | auth_totp/models/res_users.py:58 | `return '/web/login/totp'` | FACT | — | — | _mfa_url for TOTP type returns /web/login/totp | N-U49-018 |
