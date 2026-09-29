# Source Map (candidate) — `auth_totp_mail`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `auth_totp_mail` |
| Display name | 2FA Invite mail |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c955b8f553531186` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/auth_totp_mail/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `auth_totp`, `mail`
- Direct dependents in 300-module list (1): `auth_timeout`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `l10n_fr_pdp`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Extra Tools / —
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 2, reports 0, mail templates 2, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `auth_totp.device`, `res.users`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `auth_totp.device`, `res.users`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 38 of 38 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: auth_totp_mail (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities
- Adds two email-based capabilities on top of authenticator-app two-factor sign-in: (1) an administrator can invite a user to enable two-factor; (2) an organisation-wide policy can require a one-time code sent by email at login; plus security-alert emails (auth_totp_mail/__manifest__.py:3-10; auth_totp_mail/models/res_users.py:93-102,116-126).
- CONDITIONAL: auto_install True, depends auth_totp and mail (auth_totp_mail/__manifest__.py:11,13). Enforcement itself is OPTIONAL and off until set in general settings (auth_totp_mail/models/res_config_settings.py:9-18,27-31).

## B. Business objects and lifecycle
- No new stored entity. Extends User (secret/mfa logic), Trusted Device (deletion alert) and Settings (auth_totp_mail/models/res_users.py:19; auth_totp_mail/models/auth_totp_device.py:8; auth_totp_mail/models/res_config_settings.py:7).
- Email code lifecycle: user passes password step -> lands on code page -> code emailed -> code valid for one hour (3600 s window) -> success clears rate-limit counters (auth_totp_mail/controllers/home.py:13-26; auth_totp_mail/models/res_users.py:143,148-149,165,175).
- Code is derived from a per-user secret built from user id, login and last login date, so it changes after a successful login (auth_totp_mail/models/res_users.py:160).

## C. Validations, automation, security
- Code check is rate limited; wrong codes give a generic failure message and are logged with user and login (auth_totp_mail/models/res_users.py:140,144-146). Sending emails is also rate limited (auth_totp_mail/models/res_users.py:183).
- User without an email address cannot receive a code (auth_totp_mail/models/res_users.py:185-186).
- Page refuses to send unless the session is in the pre-authentication phase (auth_totp_mail/controllers/home.py:19-20).
- Code email includes device, browser, IP and approximate location for the recipient to spot suspicious attempts (auth_totp_mail/models/res_users.py:190-200).
- Where a real code cannot be generated (not superuser, not mid-login) a placeholder "000000" is returned (auth_totp_mail/models/res_users.py:169-170).
- When email-based policy applies to a user, remote API access with password is refused; API keys only (auth_totp_mail/models/res_users.py:135-136; (TEST) auth_totp_mail/tests/test_totp.py:19-50).
- Audit/notifications: user emailed when 2FA activated or deactivated (auth_totp_mail/models/res_users.py:24-36), when a trusted device is removed (auth_totp_mail/models/auth_totp_device.py:10-22), and when a login comes from an untrusted device on a 2FA-enabled account (auth_totp_mail/models/res_users.py:40-67; (TEST) auth_totp_mail/tests/test_notify_security_update_totp.py:12,33).
- Invitation action restricted to ERP-manager group and shown only for other users without 2FA (auth_totp_mail/data/ir_action_data.xml:13; auth_totp_mail/views/res_users_views.xml:9). The invite-target page action is available to internal users (auth_totp_mail/data/ir_action_data.xml:25). Invitations are only sent to users with no secret set (auth_totp_mail/models/res_users.py:95).
- No new groups, access files or record rules; no company scoping (auth_totp_mail/__manifest__.py:14-21 lists no security file).

## D. Handoffs
- Authenticator-app 2FA, trusted devices, secret storage, code-entry page and rate limiter: auth_totp (auth_totp_mail/models/res_users.py:13,140; auth_totp_mail/controllers/home.py:2). Security-alert email layout: mail (auth_totp_mail/data/security_notifications_template.xml:5). Base MFA hooks (type/url): base/web (auth_totp_mail/models/res_users.py:117,129).
- Signup with enforced 2FA must still succeed ((TEST) auth_totp_mail/tests/test_auth_signup.py:25-49); signup owner: auth_signup.

## E. Configuration that changes outcomes
- "Enforce two-factor authentication" with policy "Employees only" (internal users) or "All users" (incl. portal); switching on defaults to employees-only; stored as system parameter auth_totp.policy (auth_totp_mail/models/res_config_settings.py:12-25; auth_totp_mail/models/res_users.py:122-126).
- Precedence: if the base or authenticator-app method already applies, its result wins; the email method is used only otherwise (auth_totp_mail/models/res_users.py:117-119,129-131; auth_totp/models/res_users.py:47-53).

## F. Extension path
- auth_timeout and l10n_fr_pdp depend on it (manifest scan). l10n_fr_pdp checks the user's 2FA or the policy parameter before registration (l10n_fr_pdp/wizard/pdp_registration.py:205). Models _mfa_type/totp handled also by auth_totp, base, web (model scan).

## G. Not verified
- Full wording/validity claims inside email templates (auth_totp_mail/data/mail_template_data.xml:4,32 not reviewed line-by-line): UNKNOWN — EVIDENCE INSUFFICIENT.
- Rate-limit thresholds (implemented in auth_totp): UNKNOWN — EVIDENCE INSUFFICIENT.

