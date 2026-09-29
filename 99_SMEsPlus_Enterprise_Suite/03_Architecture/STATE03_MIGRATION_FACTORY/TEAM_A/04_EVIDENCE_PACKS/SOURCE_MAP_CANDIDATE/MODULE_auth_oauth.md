# Source Map (candidate) — `auth_oauth`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `auth_oauth` |
| Display name | OAuth2 Authentication |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `70b72cdbfa35051e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/auth_oauth/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `web`, `base_setup`, `auth_signup`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / —
- Inventory of user-facing artifacts (counts): menu items 1, views 3, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 2
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `auth.oauth.provider` (OAuth2 provider)
- Objects extended from other modules (3): `ir.config_parameter`, `res.users`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.config_parameter`, `res.users`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 42 of 42 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: auth_oauth (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities
- Lets people sign in with an external identity provider (OAuth2: Odoo.com accounts, Facebook, Google, or any custom provider) from the login page, and optionally auto-creates their account on first sign-in (auth_oauth/__manifest__.py:5-9; auth_oauth/data/auth_oauth_data.xml:4-29; auth_oauth/models/res_users.py:104-133).
- OPTIONAL: installed via the setting "Use external authentication providers (OAuth)" (base_setup/models/res_config_settings.py:22; base_setup/views/res_config_settings_views.xml:145-146). Not auto-installed (auth_oauth/__manifest__.py:11-25). Depends on base, web, base_setup, auth_signup.
- Google can be enabled through a simplified settings block (client ID only) (auth_oauth/models/res_config_settings.py:14-36; auth_oauth/views/res_config_settings_views.xml:15-25).

## B. Business objects and lifecycle
- OAuth Provider: name, client ID, authorization URL, user-info URL, optional extra data URL, scope, allowed flag, button label/style, sequence (auth_oauth/models/auth_oauth.py:9-22).
- User gains: provider, provider-side user ID (unique per provider), stored access token (hidden from all normal access), "has token" indicator (auth_oauth/models/res_users.py:22-30).
- Lifecycle: login page lists allowed providers -> user goes to provider -> returns with token -> token validated at provider -> matching user found (provider + external ID) -> session opened; if no match, and signup is allowed/invited, an account is created via signup (auth_oauth/controllers/main.py:29-46,96-135; auth_oauth/models/res_users.py:135-150,104-133).

## C. Validations, automation, security
- Token is validated by calling provider user-info endpoint (and data endpoint if set); error responses abort login; response must identify a subject (sub, id or user_id), else denied (auth_oauth/models/res_users.py:63-87).
- External ID unique per provider (auth_oauth/models/res_users.py:27-30). Users matched only by provider ID, not by email (auth_oauth/models/res_users.py:117).
- Unknown users: account creation goes through the signup flow using the invitation token carried in login state, so sign-in-created accounts follow the auth_signup rules (invitation vs free sign-up) (auth_oauth/models/res_users.py:126-131; auth_signup/models/res_users.py:96-98). On failure: generic denied (auth_oauth/models/res_users.py:132-133). Redirect codes: sign-up not allowed / access denied / invitation expired (auth_oauth/controllers/main.py:73-78,139-147).
- Stored access token: no read access for anyone through normal fields; only an indicator readable by ERP managers and the user themself; token can be cleared by that user or an ERP manager (auth_oauth/models/res_users.py:24-25,32-34,41-45). Token is part of the session-validation fields, so changing it invalidates existing sessions (auth_oauth/models/res_users.py:169-170).
- Token re-login path: a token may replace the password only when the account is active and either the login is interactive or API access via password is allowed (i.e. not restricted to API keys, as when enforced 2FA by email applies) (auth_oauth/models/res_users.py:152-167; cf. auth_totp_mail/models/res_users.py:135-136). Returned authentication is marked default-MFA level (auth_oauth/models/res_users.py:162-166).
- Redirect handling: internal-only landing on /web; other users sent to home (auth_oauth/controllers/main.py:132-134). Database filter enforced on callback (auth_oauth/controllers/main.py:104-105). Provider calls timeout after 10 seconds (auth_oauth/models/res_users.py:49-51).
- Weak points noted in comments/code: the check that the token was issued for this application (audience) is only a comment, not implemented (auth_oauth/models/res_users.py:137-141); implicit-flow token returned in URL fragment (auth_oauth/controllers/main.py:38,97).
- Access: providers manageable only by system administrators (auth_oauth/security/ir.model.access.csv:2); menu visible only in technical/debug mode (auth_oauth/views/auth_oauth_views.xml:43-45). Odoo.com provider dedicated entry point that never creates users (auth_oauth/controllers/main.py:153-182). No record rules / company scoping. No automated tests shipped in module directory (directory listing).

## D. Handoffs
- Account creation, invitation/free sign-up policy, template user: auth_signup. Login page shell: web. Settings page switch: base_setup. Multi-factor policy that may restrict token/password API use: auth_totp_mail (see C). Session cookie/authentication: web/base.

## E. Configuration that changes outcomes
- Provider "Allowed" flag decides who appears on the login page (auth_oauth/controllers/main.py:31; auth_oauth/models/auth_oauth.py:19). Shipped state: Odoo.com provider enabled, Facebook and Google disabled (auth_oauth/data/auth_oauth_data.xml:11,13-29).
- Odoo.com client ID is the database UUID, refreshed at parameter initialisation (auth_oauth/data/auth_oauth_data.xml:32-37; auth_oauth/models/ir_config_parameter.py:10-17).
- System parameter auth_oauth.authorization_header switches token transmission from URL parameter to bearer header (auth_oauth/models/res_users.py:48-51).
- Scope default "openid profile email"; login button text and style per provider (auth_oauth/models/auth_oauth.py:16,20-21).
- Sign-up scope from auth_signup (on invitation vs free) governs new-account creation (auth_signup/models/res_users.py:89,96-98).

## F. Extension path
- No Community module lists auth_oauth as a dependency (manifest scan). It extends auth_signup's login controller and res.users (auth_oauth/controllers/main.py:18,28; auth_oauth/models/res_users.py:20). Only base_setup references its switch.

## G. Not verified
- Behaviour of any specific external provider (Google/Facebook/Odoo.com account service): UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether email-based account linking is possible via extensions: UNKNOWN — EVIDENCE INSUFFICIENT.

