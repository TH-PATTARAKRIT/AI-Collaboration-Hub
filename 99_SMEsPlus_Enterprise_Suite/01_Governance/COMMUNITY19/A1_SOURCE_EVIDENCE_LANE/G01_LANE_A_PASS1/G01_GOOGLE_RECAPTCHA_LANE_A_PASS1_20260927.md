# G01 PLATFORM_BASE — LANE A PASS-1 — `google_recaptcha`

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T4 (refill) |
| Group | G01 PLATFORM_BASE |
| Module | `google_recaptcha` (governed roster member, FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |
| Handoff target | RED TEAM A1 only. No Lane B material viewed. No runtime proof claimed. |

Clean-room note: findings are neutral WHAT / WHY / RISK abstractions. Identifiers are pointers only; nothing here is a recommendation to copy schema, ORM, workflow or UI. No GMVQ QID is answered here. JS reviewed at surface level only.

## 1. Evidence Pointer Table

Paths relative to repo root at the anchor commit (module files under `addons/`). SHA-1 = `git hash-object` of the fetched file.

| # | Path | Git blob SHA-1 | Purpose |
|---|---|---|---|
| E1 | addons/google_recaptcha/__manifest__.py | 0dcee1649c8558f30fbbf7c3c680b0c292bd37ba | Manifest: purpose, deps, data, asset bundles |
| E2 | addons/google_recaptcha/__init__.py | dc5e6b693d19dcacd224b7ab27b26f75e66cb7b2 | Package imports (models only) |
| E3 | addons/google_recaptcha/models/__init__.py | 2d6a3834916c5d5582290625ed0bc5e61c8a76c1 | Model file list |
| E4 | addons/google_recaptcha/models/ir_http.py | 78d5a71cfdcf6acea4c08c9e5ccdc1a42ed7b9c8 | Session key exposure; token verification + outcome mapping |
| E5 | addons/google_recaptcha/models/res_config_settings.py | c2f237bba64c4147098c610cc41348806a58af7d | Settings fields bound to config params |
| E6 | addons/google_recaptcha/views/res_config_settings_view.xml | cb5edc792d822a113f710eb8d9a13142a0abfdcf | Settings UI extension |
| E7 | addons/google_recaptcha/static/src/js/recaptcha.js | 2cbbf952a2fa31da0f2e024acd17cfa1d31dabdb | Frontend helper: lib load, token fetch (surface read) |
| E8 | addons/google_recaptcha/static/src/xml/recaptcha.xml | 4b7c23b4c2fbaf252aff7d566213961e85b8e9bc | Legal-terms notice template |
| E9 | addons/google_recaptcha/static/src/scss/recaptcha.scss | 1603d4749b727fb13420c58c9720cf2d16928c1e | Styling (not analysed) |
| X1 | odoo/addons/base/models/ir_http.py | d9d2a00b9bc7d3e7f439b7ff4ecc46488876953a | Core dispatch hook calling captcha verification (cross-ref) |
| X2 | addons/base_setup/models/res_config_settings.py | 7de297811c8722411552e9bdc4ba12b1d2201029 | Core install toggle `module_google_recaptcha` (cross-ref) |
| X3 | addons/base_setup/views/res_config_settings_views.xml | f97b9b257d32480312e4ca826fed780ee99ca19e | Host settings block `recaptcha` (cross-ref) |

HTTP 404 at anchor: `controllers/__init__.py` (no controllers), `tests/__init__.py` (no tests package found), `static/src/interactions/recaptcha.js` (guessed name; glob content unknown).

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
1. WHAT: Hidden-category integration implementing Google reCAPTCHA v3 (invisible, score-based) to deter bot spam on public-facing forms. Depends on `base_setup`; LGPL-3; one data file (settings view); frontend assets (JS helper, SCSS, an `interactions` glob) and one backend QWeb template. [E1]
2. Installation is driven by the core settings toggle `module_google_recaptcha` in the general settings "recaptcha" block. [X2, X3]

### 2.2 Data (models, fields, constraints)
3. No new persistent models. Extends transient `res.config.settings` with four fields, each backed by a system configuration parameter: enable flag, site (public) key, secret (private) key, minimum score (default 0.7; help text suggests 0.1/0.3/0.7/0.9 on a 0.0–1.0 scale). [E5]
4. Enable flag is read/written explicitly as a string boolean, defaulting to enabled when the parameter is absent. [E5 `get_values`/`set_values`]
5. No validation constraints on keys or on score range are visible. [E5]

### 2.3 Business rules / states / exceptions — verification flow
6. Trigger point: core request dispatch invokes the verification hook when the target route declares a `captcha` action name in its routing and the HTTP method is not a "safe" method. Core default hook is a no-op; this module overrides it. [X1 `_dispatch`, `_verify_request_recaptcha_token`; E4]
7. Flow: (a) if enable flag is false, verification is skipped; (b) the client token is removed from request parameters (so it does not reach the endpoint); (c) token, client IP and secret are posted to the external verify service with a 2-second timeout; (d) result string is mapped to pass or to an exception. [E4]
8. Pass outcomes: `is_human`, and `no_secret` (secret key absent) — i.e. the check is FAIL-OPEN when no secret is configured. WHY per docstring: absent key = verification inactive. RISK: enabled flag + missing secret silently disables protection. [E4]
9. Score rule: service success with score below configured minimum → `is_bot`; action returned by service different from the route's expected action → `wrong_action`; otherwise `is_human`. [E4 `_verify_recaptcha_token`]
10. Failure mapping: invalid/missing secret → validation error ("private key is invalid"); invalid/missing token → validation error ("token is invalid"); network timeout or service `timeout-or-duplicate` → user error "timed out, please retry"; malformed/other exception → user error "invalid or malformed"; `is_bot`, `wrong_action`, and any unrecognized service error → generic user error "Suspicious activity detected". [E4]
11. Unreachable service: timeout → `timeout`; any other exception (connection error, non-JSON response) → `bad_request`; both BLOCK the request (fail-closed when a secret is configured). [E4]
12. Source observation (not runtime-proven): the minimum-score parameter is converted to a number outside the guarded block; the default 0.7 lives on the settings field, so if the parameter was never saved the conversion appears liable to fail with an unhandled error. Also a missing `score` in a successful response is treated as falsy (effectively below threshold). Flag for A1/Proof. [E4, E5]
13. Replay: single-use enforcement relies on the external service (`timeout-or-duplicate`); no local token cache. [E4]

### 2.4 Security
14. All four settings fields are restricted to the system-administrator group. Secret key is stored in plain configuration parameters (no encryption visible); read via `sudo` at verification time. [E5, E4]
15. Public (site) key is injected into both backend and frontend session info (via `sudo` read) only when enabled and a public key exists. [E4 `_add_public_key_to_session_info`]
16. Privacy/logging RISK: client IP is sent to Google and logged; on failure the raw token is logged at warning level; score logged at info. A log line for `wrong_action` formats the action with a numeric specifier (cosmetic defect candidate). [E4]
17. No ACL CSV, no groups, no record rules shipped. [E1]

### 2.5 UI surfaces (names only)
18. General settings "recaptcha" block: enable toggle replaces host field; key/secret/min-score inputs; external link to key-generation console; help text "If no keys are provided, no checks will be done." [E6, X3]
19. Frontend: helper loads the vendor library from recaptcha.net only when a public key is present, obtains an action-scoped token, and returns an error message on invalid site key. Legal-terms notice template (privacy/terms links). [E7, E8] No routes defined by this module.

### 2.6 Jobs / config / external integration
20. Config params: `enable_recaptcha`, `recaptcha_public_key`, `recaptcha_private_key`, `recaptcha_min_score`. External service: recaptcha.net siteverify endpoint (server) and api.js (client). No cron. [E4, E5, E7]

## 3. Cross-module edges
- Core `ir.http` dispatch → captcha hook (X1). Core `base_setup` settings host + install toggle (X2, X3).
- Protected routes are those in OTHER modules declaring a `captcha` routing attribute (e.g. candidates in website/auth/portal forms) — not enumerated here.
- Consumers of the frontend helper/`getToken` not enumerated.

## 4. Evidence gaps / contradictions
- G1: Which 19.0 routes/forms declare `captcha` (the actual protected surface) — requires repository-wide search; api.github.com blocked.
- G2: `static/src/interactions/**` contents unknown (glob; filenames not discoverable via raw fetch).
- G3: No tests package found at anchor; behaviour unverified by in-module tests.
- G4: Contradiction candidate: settings help says "no keys → no checks", but enabled + public key present + secret absent still loads client lib while server fails open (E4/E6/E7). Consistent with help text, but partial-config state is ambiguous.
- G5: Items 12 and 16 are static observations requiring Proof.

## 5. Limitations
- Static source at anchor only; source presence != runtime reachability. No runtime execution, no Formal Coverage, no percentages. JS depth skipped by instruction.
