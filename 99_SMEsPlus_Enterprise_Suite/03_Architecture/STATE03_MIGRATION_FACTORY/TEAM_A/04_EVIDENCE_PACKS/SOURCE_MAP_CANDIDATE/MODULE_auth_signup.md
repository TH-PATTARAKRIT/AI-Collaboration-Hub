# Source Map (candidate) — `auth_signup`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `auth_signup` |
| Display name | Signup |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `4e2be94656bf1268` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/auth_signup/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`, `mail`, `web`
- Direct dependents in 300-module list (6): `auth_oauth`, `auth_password_policy_signup`, `portal`, `survey`, `website`, `website_forum`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / —
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 1, reports 0, mail templates 4, scheduled jobs 1, wizards 1, web routes 3
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (4): `ir.http`, `res.users`, `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.http`, `res.users`, `res.config.settings`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: `['res.users']` → ['new', 'active']
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Users: Notify About Unregistered Users every 1 days
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 48 of 48 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: auth_signup (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities
- Lets people sign up themselves, be invited by an administrator, and reset a forgotten password via emailed link (auth_signup/__manifest__.py:6-8; auth_signup/controllers/main.py:39,87).
- CONDITIONAL/core-like: category Hidden/Tools and auto_install True, depends base_setup, mail, web (auth_signup/__manifest__.py:11-17).
- Sign-up page is available only if scope is "free sign up" or a valid token is present (auth_signup/controllers/main.py:43-44,132). Password reset page requires the reset setting on, or a token (auth_signup/controllers/main.py:91-92,133).
- Standard well-known "change password" address redirects to the reset page (auth_signup/controllers/main.py:177-184).

## B. Business objects and lifecycle
- No new stored entity; extends Partner (adds an admin-only "signup token type", not copied) (auth_signup/models/res_partner.py:27) and User (adds status Invited/Confirmed) (auth_signup/models/res_users.py:22-23).
- Status is derived: a user with a last-login date is Confirmed, otherwise Invited (auth_signup/models/res_users.py:33-35).
- Lifecycle: admin creates user with email -> invitation email with signup link sent automatically (auth_signup/models/res_users.py:269-280) -> recipient opens link, sets password, first login confirms -> token stops working because it embeds the last-login date (auth_signup/models/res_partner.py:180-181,189,199).
- Free sign-up creates a new external user by copying a "template user" (auth_signup/models/res_users.py:92-102,111-126).
- Archiving a user or deleting a user cancels pending signup (auth_signup/models/res_users.py:282-292).
- Duplicating a user does not send an invitation unless a new email is given (auth_signup/models/res_users.py:294-298).

## C. Validations, automation, security
- Uninvited signup rejected unless scope is free sign-up (auth_signup/models/res_users.py:96-98). Email already used by any user (including archived) is rejected (auth_signup/models/res_users.py:99-101; (TEST) auth_signup/tests/test_auth_signup.py:70).
- Password and confirmation must match (auth_signup/controllers/main.py:157-158). Password reset for unknown or ambiguous logins fails (auth_signup/models/res_users.py:135-141).
- Token is a signed, time-limited payload: reset default 4 hours, signup 144 hours; also bound to user set and login date, so it self-invalidates (auth_signup/models/res_partner.py:184-190,196-199).
- Archived users cannot be sent reset/invitation (auth_signup/models/res_users.py:160-161); users without email cannot (auth_signup/models/res_users.py:193-194). Mail-server failures surface as user-facing errors (auth_signup/models/res_users.py:150-154; (TEST) auth_signup/tests/test_reset_password.py:37).
- Audit: reset attempts logged with login, acting user and IP (auth_signup/controllers/main.py:103-105); sent-mail log lines (auth_signup/models/res_users.py:216-221).
- Captcha applies on signup and reset routes (auth_signup/controllers/main.py:39,87). Pages forbid embedding in foreign frames (auth_signup/controllers/main.py:83-84).
- Token field restricted to ERP-manager group (auth_signup/models/res_partner.py:27). Signup link generation demands write rights on users (internal) or partners (portal) for other users' partners (auth_signup/models/res_partner.py:32-35). Token retrieval for partners is only available to internal users or administrators (auth_signup/models/res_partner.py:95-96).
- "Send Password Reset Instructions" bulk action restricted to ERP-manager group (auth_signup/views/res_users_views.xml:36-42). No record rules/company scoping added here; signup copies partner company onto new user (auth_signup/models/res_users.py:76-78).
- Automation: daily job emails the inviting user about invitees still not registered after 5 days (auth_signup/data/ir_cron_data.xml:3-12; auth_signup/models/res_users.py:232-258; (TEST) auth_signup/tests/test_auth_signup.py:123).

## D. Handoffs
- Login page and controller base, captcha: web. Email delivery/templates: mail. Settings page shell: base_setup. Portal invitation wizard uses the portal invite template: portal (portal/wizard/portal_wizard.py:223). Password strength rules on signup form: auth_password_policy_signup (auth_password_policy_signup/controllers.py:4-8).

## E. Configuration that changes outcomes
- Customer Account: "On invitation" or "Free sign up"; module default is free sign-up (auth_signup/data/ir_config_parameter_data.xml:5; auth_signup/models/res_config_settings.py:13-20).
- Password reset from login page: enabled by default (auth_signup/data/ir_config_parameter_data.xml:7; auth_signup/models/res_config_settings.py:10-12).
- Template user for new signups sets default access rights of the new account (auth_signup/models/res_config_settings.py:21-24; auth_signup/views/res_config_settings_views.xml:14).
- Validity hours parameters for reset (4) and signup (144) (auth_signup/models/res_partner.py:186,188).
- Website module can override the scope per website (website/models/res_users.py:68).

## F. Extension path
- Depend directly: auth_oauth, auth_password_policy_signup, portal, survey, website, website_forum. Also use signup helpers (model scan): mail, project, website_slides.

## G. Not verified
- Exact content/wording of emails and portal-visible rendering: UNKNOWN — EVIDENCE INSUFFICIENT (templates at auth_signup/data/mail_template_data.xml:5,103,155,250 not fully reviewed).
- Behaviour of multi-factor sign-in during signup: UNKNOWN — EVIDENCE INSUFFICIENT (only comment at auth_signup/controllers/main.py:50-51).

