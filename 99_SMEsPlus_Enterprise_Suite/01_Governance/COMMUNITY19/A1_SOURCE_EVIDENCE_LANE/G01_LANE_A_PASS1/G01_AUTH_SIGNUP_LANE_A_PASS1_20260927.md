# G01 PLATFORM_BASE — LANE A PASS-1 — `auth_signup`

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T3 |
| Group | G01 PLATFORM_BASE |
| Module | `auth_signup` (governed roster member, FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |
| Handoff target | RED TEAM A1 only. No Lane B material viewed. No runtime proof claimed. |

Clean-room note: findings are neutral WHAT / WHY / RISK abstractions. Identifiers are pointers only; nothing here is a recommendation to copy schema, ORM, workflow or UI.

## 1. Evidence Pointer Table

All paths relative to `addons/` at the anchor commit. SHA-1 = `git hash-object` of the fetched file.

| # | Path | Git blob SHA-1 | Purpose |
|---|---|---|---|
| E1 | auth_signup/__manifest__.py | 994203390e26eaa1c45eb34014d1487753113851 | Manifest: deps, data list, auto_install, bootstrap |
| E2 | auth_signup/__init__.py | 7d34c7c054abd3105d5bb41fe9674111e1c27c16 | Package imports (controllers, models) |
| E3 | auth_signup/models/__init__.py | 44dc1ee6b11edc7264ed40faab073f765ebc6100 | Model file list |
| E4 | auth_signup/controllers/__init__.py | 65a8c12013d23f74275a4061b0438c237a5d1bc6 | Controller file list |
| E5 | auth_signup/models/res_config_settings.py | f72a458da9b101fe2fa3f899d3c61330aa4fcfff | Settings fields bound to config params |
| E6 | auth_signup/models/ir_http.py | fa7cd42caa7e209d0230b4cbf2dae5068ed1f225 | Request pre-dispatch: token/login captured into session |
| E7 | auth_signup/models/res_partner.py | 02aab00061cebd39df9711fd188ac0c2c681c3dd | Partner extension: signup type, signed token, URL build |
| E8 | auth_signup/models/res_users.py | 1a0280b8c37a11072caabe7640342b4f3f553514 | User extension: state, signup, reset, invite, reminder |
| E9 | auth_signup/controllers/main.py | 96d8b71fe7c987f3007f9bd9f49ab5a12bbc1f6f | Public routes: signup, reset, login override |
| E10 | auth_signup/data/ir_config_parameter_data.xml | df7690a08de224e5fe0869ec64bdb5eb58454900 | Default config params (noupdate) |
| E11 | auth_signup/data/ir_cron_data.xml | 5824f4a9941ed914a203e6feea5cece437214cb3 | Daily unregistered-user reminder cron |
| E12 | auth_signup/data/mail_template_data.xml | 764e0e1a008b1984ad537bef2ceb05cd91feb258 | 4 mail templates (invite, portal invite, reminder, signup welcome) |
| E13 | auth_signup/views/res_config_settings_views.xml | 115ba089b287226f2271bd313a532f94d8f5a014 | Settings UI inheriting base_setup form |
| E14 | auth_signup/views/res_users_views.xml | c777d2650ec4e05b7830aa1fc7b482c8049c64a2 | User form/list buttons, state badge, server action |
| E15 | auth_signup/views/auth_signup_login_templates.xml | 7b15b871b1ca289e904d8a7450a1c775ed7965d9 | Login/signup/reset QWeb pages |
| E16 | auth_signup/views/auth_signup_templates_email.xml | 7d3857964a4220d51f217ea488f6febe913d5368 | Reset-password email body (QWeb view) |
| E17 | auth_signup/views/webclient_templates.xml | 7cd32f15afdc877e250898abf3ba21e468afdee0 | "Registration successful" banner on login_successful |
| E18 | base/models/res_config.py (odoo/addons) | 504644162d067988dd7d3dcb90cd7e1a065c9fc3 | Cross-ref only: defines `action_open_template_user` used by E13 |

Blob count (this module): 18 (17 in-module + 1 cross-reference).

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
1. WHAT: Purpose is self-service sign-up and password reset for users. Depends on `base_setup`, `mail`, `web`. `auto_install` true; `bootstrap` true (templates available before a DB is fully selected); category Hidden/Tools; LGPL-3. [E1]
2. WHY/RISK: auto_install means the capability is present by default whenever its deps are installed; signup policy exposure is therefore governed by config params, not by module presence. [E1, E10]
3. Manifest `data` lists no security files (no ACL CSV, no record-rule XML). [E1]

### 2.2 Data (models, inheritance, key fields, identity/uniqueness)
4. No new persistent model is created. Extensions by inheritance: `res.partner`, `res.users`, `res.config.settings` (transient), `ir.http` (abstract). [E3, E5–E8]
5. Partner gains one stored field `signup_type` (char, not copied, field-level restricted to `base.group_erp_manager`). Values observed in code: "signup", "reset", or cleared. No token is stored; the token is computed/signed on demand. [E7]
6. User gains a computed, non-stored `state` (Invited / Confirmed) derived from presence of a last-login date; its search is derived from existence of login-log records. RISK: the compute and search bases differ (login date vs log records) — potential divergence. [E8]
7. Uniqueness: sign-up path rejects creation when any user (including archived) already matches the e-mail (via an e-mail domain helper). Login uniqueness is otherwise enforced by the base user model; a failed copy is surfaced as a signup error. [E8, E9]
8. New sign-up users are created as a copy of a configured "template user" (config param `base.template_portal_user_id`); if missing/deleted, sign-up fails. [E8]

### 2.3 Business rules / states / lifecycle / exceptions
9. Token model: a signed, expiring payload (HMAC-style hash signing, scope "signup") binding partner id, the partner's user ids, the latest login timestamp, and the signup type. WHY: any later login, user-set change, or type change silently invalidates an outstanding token (single-use-by-construction). [E7]
10. Token entropy helper (20-char random) is defined but, in the fetched files, token issuance uses the signed payload instead; the helper appears unused in this module. [E7]
11. Expiry: reset tokens default 4 h (param `auth_signup.reset_password.validity.hours`); signup/invite tokens default 144 h (param `auth_signup.signup.validity.hours`). Neither param is seeded by module data — defaults are code-level. [E7, E10]
12. Sign-up flows (single entry `signup`): (a) token + existing user → update that user (login/name protected; only password etc. written), notify inviter via bus when an internal user logs in first time; (b) token + no user → create user from template bound to the partner and partner's company; (c) no token → uninvited external sign-up. The token's type is cleared on use. Geolocation-type values (city/country/lang) never overwrite existing partner data. [E8]
13. Uninvited policy: uninvited sign-up is blocked unless invitation scope = "b2c". Error raised: "Signup is not allowed for uninvited users". [E8]
14. Reset password (by login or e-mail): errors on zero or multiple matches; archived users cannot be reset/invited; users without e-mail raise an error; mail-server failures mapped to user-facing errors. Skipped entirely during install mode or file import. [E8]
15. Invitation on user create: creating a user with an e-mail automatically sends a signup/invite mail unless context suppresses it; if mail delivery fails, the pending signup type is cancelled (user still created). Duplicating a user without a new e-mail suppresses the invite. [E8]
16. Internal vs portal invite use different templates (`set_password_email` vs `portal_set_password_email`); fallback for reset is a rendered QWeb body mailed from company/user address. [E8, E12, E16]
17. Lifecycle cancellations: archiving a user or deleting a user cancels pending partner signup. [E8]
18. Bulk invite from settings (`web_create_users`) re-sends invites to still-"Invited" users matching the e-mails and delegates creation of the rest to base_setup. [E8]
19. Contradiction to flag: default invitation scope differs by layer — settings field default "b2c", seeded param "b2c" (noupdate), but the runtime getter falls back to "b2b" if the param is absent. [E5, E8, E10]
20. `_signup_retrieve_partner` accepts `check_validity` / `raise_exception` flags but always raises on invalid token regardless. [E7]

### 2.4 Security
21. No ACL or record-rule files in module. Access relies on base model rights plus field-level group on `signup_type`. [E1, E7]
22. Signup URL generation: runs privileged, then checks the caller has write access on users (if target has internal user) or partners (if portal user) other than self. [E7]
23. `signup_get_auth_param` is private and denied unless caller is internal or admin; only emits a signup token when scope is "b2c" and partner has no user. [E7]
24. Public controllers run signup/reset/lookup via elevated privileges (sudo) on users/partners/mail templates. RISK area for A1: account enumeration surfaces — the reset path returns distinct error text for "no account" vs "multiple accounts", and a `signup_email` query parameter can redirect to login with the matched login pre-filled for confirmed users. [E8, E9]
25. Tokens/login in URL query are copied into the HTTP session on every request pre-dispatch. [E6]
26. Captcha hooks declared on signup and reset routes (captcha keys "signup" / "password_reset"); anti-framing headers set on both pages. Captcha provider itself is out of module. [E9]
27. Reset-password server action is bound to users and restricted to `base.group_erp_manager`. Reset attempts are logged with requester and remote address. [E9, E14]

### 2.5 UI surfaces (names only)
28. Routes: `/web/login` (override), `/web/signup` (public, 404 when disabled and no token), `/web/reset_password` (public, 404 when disabled and no token), `/.well-known/change-password` (redirect), `/base_setup/data` (override adds a resend-invitation flag). [E9]
29. Settings fields: `auth_signup_uninvited`, `auth_signup_reset_password`, `auth_signup_template_user_id`; settings blocks `login_documents`, `enable_password_reset`; button to open template user. [E5, E13]
30. User form: "Send an Invitation Email" (Invited only), "Send Password Reset" (Confirmed, not self), status bar; list badge. Server action "Send Password Reset Instructions". [E14]
31. Web templates: `auth_signup.login`, `auth_signup.fields`, `auth_signup.signup`, `auth_signup.reset_password`, `login_successful` banner. [E15, E17]

### 2.6 Jobs / config
32. Config params: `auth_signup.invitation_scope` (b2b|b2c), `auth_signup.reset_password` (bool string), `base.template_portal_user_id`, `auth_signup.reset_password.validity.hours`, `auth_signup.signup.validity.hours`. [E5, E7, E8, E10]
33. Cron "Users: Notify About Unregistered Users": daily, runs as superuser, batch 100; notifies inviters about internal users created exactly 5 days ago with no login log; deactivates itself if template missing; progress-commit with timeout stop and explicit note that resends are not tracked. [E8, E11]
34. Mail templates: New User Invite, Unregistered User Reminder, New Portal Sign Up (welcome, sent after successful public signup), New Portal User Invite; all auto-delete. [E9, E12]

## 3. Cross-module edges
- `base_setup`: settings form inheritance anchor; `/base_setup/data` controller extended; `web_create_users` chain. [E9, E13]
- `base`: `res.users`/`res.partner` models, template-user param, `action_open_template_user` in base res.config.settings [E18], `base.group_erp_manager`, login/e-mail domain helpers.
- `web`: `Home` controller, login templates, signup request param set, captcha-skip constant. [E9]
- `mail`: templates, `mail.mail`, render mixin, delivery exception, light notification layout, bus notify. [E8]
- Captcha providers (e.g. recaptcha/turnstile modules) are external consumers of the captcha keys — not verified here.

## 4. Evidence gaps / contradictions
- G1: Invitation scope default contradiction (b2c vs b2b fallback) — see #19.
- G2: `state` compute vs search basis differ — see #6.
- G3: Signing primitives (`tools.hash_sign` / `verify_hash_signed`) live in core `odoo/tools`; not fetched — algorithm, key source and clock handling unverified.
- G4: Login/e-mail domain helpers and base login-uniqueness constraint in `base` not fetched.
- G5: Static JS assets (`static/**`) not reviewed (out of scope per instruction).
- G6: Unused parameters/helpers (#10, #20) — presence only; no inference about intent.

## 5. Limitations
- Source presence ≠ runtime reachability. No execution, no runtime observation, no Formal Coverage claim.
- No GMVQ QIDs answered; evidence only for A1.
- Single commit anchor; later/earlier revisions not compared.
