# Source Map (candidate) — `google_recaptcha`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `google_recaptcha` |
| Display name | Google reCAPTCHA integration |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `320497122541ef1d` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/google_recaptcha/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`
- Direct dependents in 300-module list (1): `website`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `website_mass_mailing`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 33 of 33 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: google_recaptcha
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Bot/spam protection for public forms using Google reCAPTCHA v3 (score-based, invisible): the browser obtains a token for a named action and the server verifies it with Google before processing the request (google_recaptcha/__manifest__.py:9; google_recaptcha/models/ir_http.py:36-61,63-121; google_recaptcha/static/src/js/recaptcha.js:20-43).
- Optional: enabled from the General Settings integration toggle; depends on base_setup; no auto-install flag (google_recaptcha/__manifest__.py:11; base_setup/models/res_config_settings.py:30).
- Conditional twice over: verification only runs when the "Enable reCAPTCHA" switch is on (default on) AND a secret key exists; with no secret the check is treated as passed (google_recaptcha/models/ir_http.py:44-46,80-82; google_recaptcha/views/res_config_settings_view.xml:9). Public site key is only announced to the browser when both switch and site key exist (google_recaptcha/models/ir_http.py:30-33).
- Legal notice snippet ("Protected by reCAPTCHA ... Privacy Policy & Terms") provided for forms (google_recaptcha/static/src/xml/recaptcha.xml:4-12).

## B. Business objects, relationships, lifecycle
- No stored business objects. Four system parameters: enable switch, site (public) key, secret (private) key, minimum score (google_recaptcha/models/res_config_settings.py:10-19).
- Lifecycle of a protected request: page loads -> site key delivered in session info (backend and public site) -> script loaded from Google's recaptcha host -> token requested for the form's action -> token sent with the request -> server verifies token, client address, score and action -> request proceeds or fails (google_recaptcha/models/ir_http.py:17-24,47-61,85-89; google_recaptcha/static/src/js/recaptcha.js:10-22,34-43).
- The verification hook is invoked by the base HTTP layer for routes that declare a captcha action, and by the backend login form for action "login" (base/models/ir_http.py:352,455; web/controllers/home.py:131). Which other routes declare captcha: UNKNOWN — EVIDENCE INSUFFICIENT.

## C. Validations, automation, security, credentials
- Outcomes and messages: human or no-secret -> pass; bad secret -> "private key is invalid"; bad token -> "token is invalid"; timeout -> "request has timed out, please retry"; malformed -> "request is invalid or malformed"; anything else (bot, wrong action) -> "Suspicious activity detected" (google_recaptcha/models/ir_http.py:50-61).
- Score check: token score below the configured minimum (default 0.7) is treated as a bot; action mismatch between token and expected action fails (google_recaptcha/models/res_config_settings.py:17; google_recaptcha/models/ir_http.py:100-107).
- External-service implication: each protected submission sends the secret key, the token and the visitor's IP address to Google's verification endpoint (recaptcha.net), timeout 2 seconds; timeouts and other exceptions fail the request rather than skip the check (google_recaptcha/models/ir_http.py:80-98). Visitor's browser also loads Google's script and shows Google's badge (google_recaptcha/static/src/js/recaptcha.js:20-22). Privacy note: visitor IP and interaction data go to Google.
- Credential implications: secret key stored as a plain system parameter; settings fields restricted to the system administration group; site key is public by design (google_recaptcha/models/res_config_settings.py:11-16). Failure logs include the submitted token (google_recaptcha/models/ir_http.py:111).
- Potential defect to note: when the minimum-score parameter is unset and a valid response arrives, the score comparison would need a number (google_recaptcha/models/ir_http.py:83,102); default in settings is 0.7, so behavior depends on the settings screen having been saved: UNKNOWN — EVIDENCE INSUFFICIENT whether a data default exists elsewhere.
- No record rules, groups (other than settings), or company scoping: parameters are database-wide.

## D. Handoffs to other modules
- Base HTTP dispatch declares the hook and captcha route option (base/models/ir_http.py:352,455); backend login form calls it (web/controllers/home.py:131).
- Settings page and toggle: base_setup (google_recaptcha/views/res_config_settings_view.xml:6-13; base_setup/models/res_config_settings.py:30).
- Alternative captcha provider toggle (Cloudflare Turnstile) exists in the same settings block: website_cf_turnstile (base_setup/models/res_config_settings.py:31); module not in scope.
- Form-building/website modules that add their own captcha widget: UNKNOWN — EVIDENCE INSUFFICIENT (a front-end interaction file exists: google_recaptcha/__manifest__.py:19).

## E. Configuration/defaults that change outcomes
- Enable switch default true when the parameter is absent (google_recaptcha/models/ir_http.py:30,44; google_recaptcha/models/res_config_settings.py:25).
- Minimum score default 0.7, suggested values 0.1/0.3/0.7/0.9 (google_recaptcha/models/res_config_settings.py:13-19).
- Help text states: no keys provided means no checks (google_recaptcha/views/res_config_settings_view.xml:9).

## F. Effective extension path
- Other providers or modules override the verification hook in the HTTP layer (google_recaptcha/models/ir_http.py:36-42 calls the parent). Consumers add a captcha action to routes/forms; module names beyond web/base: UNKNOWN — EVIDENCE INSUFFICIENT.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end form interaction details (recaptcha_form.js not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: no automated tests in module.
- UNKNOWN — EVIDENCE INSUFFICIENT: what other routes are protected.

