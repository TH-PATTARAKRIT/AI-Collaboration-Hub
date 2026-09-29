# Source Map (candidate) — `website_cf_turnstile`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_cf_turnstile` |
| Display name | Cloudflare Turnstile |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `55bb4090108b7bb8` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_cf_turnstile/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `website`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / —
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `ir.http`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.http`, `res.config.settings`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 38 of 39 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_cf_turnstile (Cloudflare Turnstile)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_cf_turnstile.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: bot-spam protection for website forms using Cloudflare Turnstile (website_cf_turnstile/__manifest__.py:9).

## A. Capabilities / functions
- Optional add-on (no `auto_install`, depends only on website): installed on demand, not automatically (website_cf_turnstile/__manifest__.py:11). It is switched on from the general settings toggle "Cloudflare Turnstile" (base_setup/models/res_config_settings.py:31; base_setup/views/res_config_settings_views.xml:178-181).
- Core: adds a second human-verification check on top of the base captcha hook: after the parent checks run, it reads a challenge token from the submitted request and asks Cloudflare to validate it (website_cf_turnstile/models/ir_http.py:28-48, 51-104).
- Core: exposes the public site key to the browser session so front-end forms can show the challenge widget (website_cf_turnstile/models/ir_http.py:17-25).
- Front end: website forms (form builder) and any form flagged for captcha get a challenge widget, and the submit button is disabled until it is solved; forms opting out of captcha are skipped (website_cf_turnstile/static/src/interactions/form.js:12-28; website_cf_turnstile/static/src/interactions/turnstile_captcha.js:6-28).
- Two setting fields for the site key and secret key on the general settings screen (website_cf_turnstile/models/res_config_settings.py:9-10; website_cf_turnstile/views/res_config_settings_view.xml:8-25).

## B. Business objects, relationships, lifecycle
- No new stored business object. Keys live as system parameters `cf.turnstile_site_key` and `cf.turnstile_secret_key` (website_cf_turnstile/models/res_config_settings.py:9-10; website_cf_turnstile/models/ir_http.py:21,68).
- Verification outcome vocabulary (human, bot, no secret, wrong action, wrong token, wrong secret, timeout, bad request) is the only state; it is per request and not persisted (website_cf_turnstile/models/ir_http.py:56-66).

## C. Validations, automation, security, multi-company
- Missing secret key means the check is treated as passed (feature silently inactive) (website_cf_turnstile/models/ir_http.py:37-38, 69-70).
- Failure handling: invalid secret or invalid token raises a validation error; timeout or malformed request raises a user error; any other outcome (including wrong action or a detected bot) raises a "suspicious activity" error (website_cf_turnstile/models/ir_http.py:39-48, 87-104).
- The external call has a short time limit (about 3 seconds) and any unexpected failure of the call is reported as a bad request, so an unreachable service blocks the form submission once a secret is configured (website_cf_turnstile/models/ir_http.py:71-85). Whether this is the desired availability trade-off: UNKNOWN — EVIDENCE INSUFFICIENT.
- The action label sent with the front-end challenge must match the action the server expects, else "wrong action" (website_cf_turnstile/models/ir_http.py:87-90; website_cf_turnstile/static/src/interactions/turnstile_captcha.js:21).
- Keys are readable/editable only by the system administrators group (`base.group_system`) on the settings fields (website_cf_turnstile/models/res_config_settings.py:9-10). The site key is nevertheless public by nature (sent to all visitors) (website_cf_turnstile/models/ir_http.py:22-23).
- Keys are global system parameters: no per-website or per-company key (website_cf_turnstile/models/ir_http.py:21,68). No record rules or access-control rows in this module.
- The page-side widget is created only when a site key is present (website_cf_turnstile/static/src/interactions/form.js:15-19; website_cf_turnstile/static/src/interactions/turnstile_captcha.js:12-15).

## D. Handoffs to other modules
- base (owner of the captcha extension point, which does nothing by default) (base/models/ir_http.py:455-456); google_recaptcha (sibling implementation that also chains to the parent, so both checks can run when both are configured) (google_recaptcha/models/ir_http.py:36-42; google_recaptcha/__manifest__.py:11).
- Callers that trigger the check: web login (web/controllers/home.py:131), website form submissions (website/controllers/form.py:31), website_mail follow (website_mail/controllers/main.py:27), website_event registration (website_event/controllers/main.py:455), website_mass_mailing subscribe (website_mass_mailing/controllers/main.py:39), auth_signup sign-up and reset forms (auth_signup/views/auth_signup_login_templates.xml:38,81), forum follow modal (website_forum/views/forum_templates_mail.xml:36).
- Website form builder client code is patched, owned by website (website_cf_turnstile/static/src/interactions/form.js:1,8).

## E. Configuration / defaults that change outcomes
- Site key and secret key: empty means no protection (website_cf_turnstile/models/ir_http.py:69-70). Setting only the site key shows the widget but the server still skips verification (website_cf_turnstile/models/ir_http.py:22-23, 69-70).
- Forms carrying the "no recaptcha" marker class skip the widget (website_cf_turnstile/static/src/interactions/form.js:16).
- Tests: only front-end (JS) tests exist for the widget; no server tests (TEST) (website_cf_turnstile/static/tests/interactions/turnstile_captcha.test.js). Behaviour against the live Cloudflare service: UNKNOWN — EVIDENCE INSUFFICIENT.

## F. Effective extension path (module names only)
- ir.http captcha hook overridden by: base (default), google_recaptcha, website_cf_turnstile. res.config.settings extended here alongside base_setup, which hosts the on/off toggle.
- Consumers: web, auth_signup, website, website_mail, website_event, website_mass_mailing, website_forum.

## G. Not verified
- Cloudflare-side verification behaviour, key rotation and rate limiting: UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether the base routing layer calls the hook automatically for routes declared with a captcha option: UNKNOWN — EVIDENCE INSUFFICIENT (the routing code is outside the addons tree).

