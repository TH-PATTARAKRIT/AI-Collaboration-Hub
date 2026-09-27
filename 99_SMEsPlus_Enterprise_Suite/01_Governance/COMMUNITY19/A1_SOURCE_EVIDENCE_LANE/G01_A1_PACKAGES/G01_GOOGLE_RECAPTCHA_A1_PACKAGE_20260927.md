# G01 PLATFORM_BASE — RED TEAM A1 Package — `google_recaptcha`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `google_recaptcha` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_GOOGLE_RECAPTCHA_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `a7710f32db0332615bf8debc478b8c30e3c98ec2755e4bb473cc9e9a2d770479` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/google_recaptcha/` (+ core cross-refs) |
| Question bank (lens only) | `GMVQ/G01_PLATFORM_BASE/G01_GOOGLE_RECAPTCHA_GMVQ_MVQ_40_V1.00_DRAFT.md` (sha256 `471e0323…7724`, matches `FREEZE_W1-B04.json`) |
| Freeze | batch W1-B04, freeze hash `9e31f2d27dfb959e555cf8ff117d829969e8122fe5e5544bbaf737b6ddea0377`, ELIGIBLE |
| Lane B dependency | None. A1 does not wait for Lane B, and no runtime evidence was used |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Clean-room note: the claims are neutral WHAT / WHY / RISK statements. Identifiers are evidence pointers only. Nothing here recommends reusing the vendor's schema, ORM, workflow, UI or naming. No QIDs are answered. The bank was used only as a topic lens: the server-authoritative decision, missing-secret policy, fail-closed behaviour on outage, action binding, score enforcement, secret exposure, logging of sensitive values, network context, scope of protected routes, and configuration validation.

Evidence key (blob SHA-1 from Lane A): E1 `__manifest__.py` 0dcee164…; E4 `models/ir_http.py` 78d5a71c…; E5 `models/res_config_settings.py` c2f237bb…; E6 `views/res_config_settings_view.xml` cb5edc79…; E7 `static/src/js/recaptcha.js` 2cbbf952…; X1 core `odoo/addons/base/models/ir_http.py` d9d2a00b…; X2/X3 `base_setup` settings 7de29781… / f97b9b25…

## 1. Claims

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-RCAP-C01 | WHAT: A hidden integration adds score-based invisible bot checks (reCAPTCHA v3) to public forms. It depends only on the general-settings host module. It defines no routes, no persistent models and no tests. | E1 (S1); Lane A 404s | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C02 | WHAT: The server check runs only when the target route declares a captcha action name AND the HTTP method is not a "safe" method. The core default is a no-op that this module overrides. RISK: routes without that declaration, and safe-method requests, are never checked. So the protected surface is whatever other modules opt into. | X1 dispatch (S2) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C03 | WHAT: Verification runs before the endpoint is invoked, so a refusal happens before the endpoint's business side effects. | X1 (S2) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C04 | WHAT: The enable flag defaults to on when the parameter is missing. When the flag is off, verification is skipped entirely. | E4, E5 (S3, S4) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C05 | WHAT: The client token is removed from the request parameters before verification, so it never reaches the endpoint. | E4 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C06 | WHAT: With no secret key configured, the result is "no secret", and that is treated as a pass (FAIL-OPEN). WHY: the docstring and settings help say "no keys → no checks". RISK: a "enabled" posture with a missing secret silently gives no protection, and nothing is logged on that path. | E4 (S3); E6 help (S4) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C07 | WHAT: With a secret configured, a verifier timeout maps to a retryable refusal, and any other failure (connection error, non-JSON reply, missing expected key) maps to a "malformed" refusal. Both BLOCK the request (FAIL-CLOSED). The outbound call has a 2-second timeout and makes no retries. | E4 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C08 | WHAT: The minimum score is read before the guarded block but converted to a number outside it, after a successful reply. The 0.7 default exists only on the settings field, and no data file seeds the parameter. RISK: if the parameter was never saved, or is not numeric, the conversion raises an unhandled technical error instead of mapping to a defined outcome. | E4 (S3); E5 default (S4); E1 data list (S1) | HIGH (source path) | SOURCE-STATIC — **CONTRADICTION CONFIRMED-FROM-SOURCE** (runtime reachability unproven) |
| A1-G01-RCAP-C09 | WHAT: A successful reply with no score is treated as falsy, and so falls below any positive threshold and is classified as a bot. | E4 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C10 | WHAT: Action binding refuses a mismatch only when the verifier returns a non-empty action that differs from the expected one. RISK: an empty returned action skips the binding check. | E4 (S3) | MED | SOURCE-STATIC |
| A1-G01-RCAP-C11 | WHAT: Verifier error codes are mapped as follows: missing/invalid secret → "private key invalid"; missing/invalid token → "token invalid"; timeout-or-duplicate → retryable timeout; bad-request → malformed. Unrecognised or empty codes, low score and wrong action all give a generic "suspicious activity" refusal. The two configuration/token categories are validation errors, the rest are user errors. | E4 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C12 | WHAT: A missing client token is still sent to the verifier. Whether it is rejected depends on the verifier's reply, since there is no local short-circuit. Replay protection relies entirely on the verifier's duplicate code, with no local token cache. | E4 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C13 | RISK: When the verifier returns a failure, the raw client token and the client IP are logged at warning level. The IP is also logged on timeout (error), on low score and wrong action (warning), and on success (info). A log line labelled as the action prints the score value instead. | E4 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C14 | WHAT: The client IP used is the raw remote address of the request. How it behaves behind a proxy depends on core request handling, which was not examined. | E4 (S3) | MED | SOURCE-STATIC |
| A1-G01-RCAP-C15 | WHAT: Four settings (enable, site key, secret key, minimum score) are stored as plain system configuration parameters, and their settings fields are restricted to system administrators. The secret is read with elevated privilege at verification time. No encryption and no input masking of the secret appear in the settings view. | E5 (S4); E6 (S4); E4 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C16 | WHAT: There is no validation of score range or key format. The help text suggests 0.1/0.3/0.7/0.9 on a scale from 0.0 to 1.0. | E5 (S4) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C17 | WHAT: Only the site (public) key is added to backend and frontend session info, and only when the flag is enabled and a site key exists. The secret is never put into session info. | E4 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-RCAP-C18 | WHAT: The frontend helper loads the vendor library only when a site key is present and returns an error message when the site key is invalid. (Surface read only. The interactions glob is unknown.) | E7 (Lane A) | MED | SOURCE-STATIC |
| A1-G01-RCAP-C19 | WHAT: The module is installed through a core general-settings toggle, and its settings block extends the host settings block. | X2, X3 (Lane A) | HIGH | SOURCE-STATIC |

## 2. Business rules
- BR1: Only routes that declare a captcha action are checked, and only on mutating methods (C02).
- BR2: No secret means no verification. This is an explicit pass, not an error (C06).
- BR3: With a secret configured, every verifier-unavailable outcome refuses the request (C07).
- BR4: A score below the configured minimum, or a missing score, is refused (C08, C09).
- BR5: A token is bound to the route's declared action when the verifier reports an action (C10).
- BR6: Only system administrators may change the configuration (C15).

## 3. States / transitions (effective protection posture)
- P0 Disabled (flag off) → no check (C04).
- P1 Enabled with no secret → FAIL-OPEN pass (C06). The client library may still load if a site key is present (see CON-RCAP-02).
- P2 Enabled with a secret and an unset or invalid minimum score → a technical error after the verifier succeeds (C08).
- P3 Enabled with a secret and a valid minimum score → full verification. Outcomes: pass, or refused as {secret, token, timeout, malformed, suspicious} (C07, C11).
- Transitions happen only when a system administrator saves the settings. No audit of posture changes is visible (GAP-5).

## 4. Exceptions / failure modes
- F1: Missing secret → silent pass (C06).
- F2: Verifier timeout or duplicate token → retryable user error (C07, C11).
- F3: Connection failure, bad JSON or missing key → "malformed" user error (C07).
- F4: Invalid secret or invalid token → validation error (C11).
- F5: Minimum score unset or non-numeric → unhandled technical error (C08).
- F6: Unknown verifier codes → generic suspicious-activity refusal (C11).

## 5. Cross-module handoffs
- H1: The core request dispatch hook (X1) is where verification is invoked.
- H2: The host `base_setup` settings supply the install toggle and the settings block (X2, X3).
- H3: Consumer modules that declare captcha on routes, and frontend callers of the token helper, are not enumerated (GAP-1).
- H4: There is an external dependency on the vendor verify endpoint and the vendor client library, reached through recaptcha.net (E4, E7).

## 6. Evidence gaps (Lane A gaps carried forward)
- GAP-1 (Lane A G1): The routes and forms in 19.0 that declare captcha (the actual protected surface) are not enumerated.
- GAP-2 (Lane A G2): The contents of the frontend interactions glob are unknown.
- GAP-3 (Lane A G3): No in-module tests package was found.
- GAP-4 (Lane A G4 / G5): The partial-configuration posture (see CON-RCAP-02) and C08 / C13 still need Proof.
- GAP-5 (new): Whether changes to the configuration parameters are audited, and who can read those parameters outside the settings screen, was not examined.
- GAP-6 (new): Core handling of the client address behind a reverse proxy was not examined (C14).

## 7. CRQ candidates
- CRQ-RCAP-01: With the flag enabled and no secret configured, confirm that protected submissions succeed unchecked, and whether any operator-visible signal exists (C06).
- CRQ-RCAP-02: With a secret configured but the minimum score never saved, confirm whether a successful verification produces a technical error (C08).
- CRQ-RCAP-03: With a secret configured and the verifier unreachable or slow, confirm the refusal and its message (C07).
- CRQ-RCAP-04: Confirm whether the raw token and IP appear in server logs when a verification fails (C13).
- CRQ-RCAP-05: Confirm that GET or other safe-method calls to a captcha-declared route skip verification, and whether any such route has side effects (C02).
- CRQ-RCAP-06: Confirm which non-administrator roles, if any, can read the secret parameter through other surfaces (C15, GAP-5).
- CRQ-RCAP-07: Confirm the binding behaviour when a token minted for another action is submitted (C10).

## 8. Contradictions
- CON-RCAP-01 **CONFIRMED-FROM-SOURCE** (S3, S4, S1): the verification routine is designed to map every outcome to a defined category, but the minimum-score conversion sits outside the guarded block and has no seeded default, so one path leaves the defined categories (C08). Runtime reachability has not been proven.
- CON-RCAP-02 CANDIDATE: the settings help says "no keys → no checks". But when the flag is enabled, a site key is set and there is no secret, the client still obtains tokens while the server passes every request unchecked. The appearance and the enforcement diverge (C06, C17, C18).
- CON-RCAP-03 CANDIDATE (cosmetic): the wrong-action log line labels the score value as the action (C13).

## 9. Spot-check log
Files re-fetched from `raw.githubusercontent.com/odoo/odoo/8d05257d…/<path>`. Every fetch returned HTTP 200, and `git hash-object` was compared with the Lane A blob.

| # | File | Lane A blob | Computed blob | Result | Claims verified |
|---|---|---|---|---|---|
| S1 | `addons/google_recaptcha/__manifest__.py` | 0dcee164… | 0dcee1649c8558f30fbbf7c3c680b0c292bd37ba | MATCH | C01, C08: one view data file only, no parameter seed |
| S2 | `odoo/addons/base/models/ir_http.py` | d9d2a00b… | d9d2a00b9bc7d3e7f439b7ff4ecc46488876953a | MATCH | C02, C03: route captcha attribute + non-safe method gate, verification before endpoint call, no-op default |
| S3 | `addons/google_recaptcha/models/ir_http.py` | 78d5a71c… | 78d5a71cfdcf6acea4c08c9e5ccdc1a42ed7b9c8 | MATCH | C04–C14, C17: fail-open on missing secret, fail-closed on timeout and exceptions, score conversion outside the guard, raw token and IP logged, action check |
| S4 | `models/res_config_settings.py`, `views/res_config_settings_view.xml` | c2f237bb…, cb5edc79… | c2f237bba64c4147098c610cc41348806a58af7d, cb5edc792d822a113f710eb8d9a13142a0abfdcf | MATCH | C04, C15, C16: plain config params, system-admin group, default only on field, unmasked secret input, "no keys" help |

Refinements to Lane A: item 16 is corrected so that the wrong-action log prints the score in the action slot. Item 11 is sharpened, because a missing action key in a successful reply also maps to "malformed". Item 14 is extended with the fact that the secret input is not masked in the view.

## 10. Provenance
- The only input is the Lane A packet (sha256 above), plus spot-check re-fetches at the anchor commit. Re-fetched copies are held only in the session scratchpad.
- The GMVQ bank was used as a topic lens only. Its hash was verified against `FREEZE_W1-B04.json`. No QID was answered and nothing was edited.

## 11. Limitations
- This is static source at one anchor commit. Source presence does not mean runtime reachability, and no runtime execution took place. This is not Formal Coverage and gives no percentages.
- The JavaScript was read at surface level only (by Lane A). The interactions glob is unknown.
- The actual protected route surface and the verifier's own behaviour are outside this source scope.
