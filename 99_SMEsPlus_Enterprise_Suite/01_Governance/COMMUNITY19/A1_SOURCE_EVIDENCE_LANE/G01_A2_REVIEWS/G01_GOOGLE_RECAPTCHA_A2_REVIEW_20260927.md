# G01 PLATFORM_BASE — RED TEAM A2 Review — `google_recaptcha`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional / semantic verifier of A1 conclusions) |
| Group / Module | G01 PLATFORM_BASE / `google_recaptcha` |
| A1 package under review | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_GOOGLE_RECAPTCHA_A1_PACKAGE_20260927.md` |
| A1 package sha256 | `122308a976f8c966682372697463653f9218ccc6977399257f1430bc39d0b270` |
| Upstream Lane A packet sha256 | `a7710f32db0332615bf8debc478b8c30e3c98ec2755e4bb473cc9e9a2d770479` (matches the A1 header) |
| Question bank (lens only) | `GMVQ/G01_PLATFORM_BASE/G01_GOOGLE_RECAPTCHA_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `471e0323450c71223ac795ee859f004d1f5f8e0c8baac04a398b51f7c3bd7724` (matches the A1 header; batch W1-B04, ELIGIBLE) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Lane B | None available. See section 5 |
| Date | 2026-09-27 |
| Disposition | **A2 PASS WITH FINDINGS** |

Independence and clean-room note: A2 re-read the source independently at the anchor commit. It did not repair or edit the A1 package or the Lane A packet. This review contains no vendor code. Identifiers appear only as evidence pointers. It answers no QIDs, gives no percentages and makes no Formal Coverage claim.

### Source re-check (A2 independent fetch, `git hash-object`)

| Ref | Path | Blob SHA-1 (A2 computed) | vs Lane A / A1 |
|---|---|---|---|
| E1 | addons/google_recaptcha/__manifest__.py | 0dcee1649c8558f30fbbf7c3c680b0c292bd37ba | MATCH |
| E4 | addons/google_recaptcha/models/ir_http.py | 78d5a71cfdcf6acea4c08c9e5ccdc1a42ed7b9c8 | MATCH |
| E5 | addons/google_recaptcha/models/res_config_settings.py | c2f237bba64c4147098c610cc41348806a58af7d | MATCH |
| E6 | addons/google_recaptcha/views/res_config_settings_view.xml | cb5edc792d822a113f710eb8d9a13142a0abfdcf | MATCH |
| E7 | addons/google_recaptcha/static/src/js/recaptcha.js | 2cbbf952a2fa31da0f2e024acd17cfa1d31dabdb | MATCH |
| X1 | odoo/addons/base/models/ir_http.py | d9d2a00b9bc7d3e7f439b7ff4ecc46488876953a | MATCH |
| X2 | addons/base_setup/models/res_config_settings.py | 7de297811c8722411552e9bdc4ba12b1d2201029 | MATCH |
| X3 | addons/base_setup/views/res_config_settings_views.xml | f97b9b257d32480312e4ca826fed780ee99ca19e | MATCH |
| A2-X4 (new) | odoo/http.py | ebfc2ac8d268a45aaf4b8cde8c9ce8b480d58dbb | New to A2. Defines the safe-method set: GET, HEAD, OPTIONS, TRACE |
| A2-X5 (new) | odoo/addons/base/models/res_config.py | 504644162d067988dd7d3dcb90cd7e1a065c9fc3 | New to A2. Settings save/load for config-parameter fields |
| A2-X6 (new) | odoo/addons/base/models/ir_config_parameter.py | 21c82bf62ed0fec4b4307c935f8a2b4ebaff4321 | New to A2. Setting a false value deletes the parameter. The model has no company field |
| A2-X7 (new) | odoo/tools/misc.py | 6d27505917a80a2cf9d3b3c6faa6bf8bca86acfd | New to A2. The string-to-boolean helper raises on unrecognised text when no default is given |
| A2-X8 (new) | odoo/addons/base/security/ir.model.access.csv | 29785e02c9795cd27a0b6b5652853d03995b9c35 | New to A2. The parameter model's ACL is granted to the system group only |
| A2-X9 (new) | addons/website/controllers/form.py | 2caa89e06266808af059e4ecc1edaf2812178271 | New to A2. One consumer example: a public POST form route that declares a captcha action and disables CSRF |
| — | addons/google_recaptcha/controllers/__init__.py, tests/__init__.py | HTTP 404 | Confirms that there are no routes and no tests package (C01) |

## 1. Test plan (predeclared before claim review)

| TP | Check | Applies to | Pass rule |
|---|---|---|---|
| TP1 | Lineage: recompute the sha256 of the A1 package, Lane A packet and bank | Header | All hashes match |
| TP2 | Blob integrity: re-fetch every cited file and compare its `git hash-object` | E1–E7, X1–X3 | All blobs match |
| TP3 | Independent semantic re-read of every HIGH claim | C01–C09, C11–C13, C15–C17, C19 | The statement is supported, and the scope qualifiers are accurate |
| TP4 | Deep read of contradiction and CRQ items: C02/C03 (dispatch gate and ordering), C06 (fail-open), C07 (fail-closed), C08 (min-score conversion and seeding, including how the core settings save handles it), C10 (empty-action binding), C13 (logging), C15 (secret storage and masking) | Listed claims, CON-RCAP-01/02/03 | A2 traces the path independently, and reaches the same result or records a divergence |
| TP5 | Protection-posture matrix: flag × site key × secret × min-score state, combined with client and server behaviour | Section 3 | Every posture maps to a defined outcome, or is flagged |
| TP6 | Business-meaning review: bot protection on public SaaS forms, including tenant scope, privacy and operator visibility | All | Overclaims and omissions are recorded |
| TP7 | Bank topic lens (topics only) to find areas A1 did not address | Section 4 | Each omission is recorded with evidence or marked as unexamined |
| TP8 | Lane B classification and Proof for runtime claims only | Sections 5–6 | Each item has an expected result and a fail condition |

## 2. Claim verdict table

| Claim | A1 conf. | A2 verdict | A2 independent basis / note |
|---|---|---|---|
| C01 | HIGH | VERIFIED | The manifest is Hidden with a single `base_setup` dependency and one view data file. No routes or tests package (404). The only models are extensions of existing core/transient models. |
| C02 | HIGH | PARTIAL | Verified: the core generic dispatch calls the hook only when the route declares a captcha name and the method is outside the safe set (GET/HEAD/OPTIONS/TRACE per A2-X4). The core default hook is a no-op. Overclaim: the word "only" cannot be established from module scope. The verification method is an ordinary model method that any other module's code could call directly, and other dispatchers were not examined. The consumer example A2-X9 does use the declarative path. |
| C03 | HIGH | VERIFIED | In the core dispatch the hook call comes before the endpoint call. Pre-dispatch work (session, auth, routing) happens earlier, but the endpoint's own side effects do not. |
| C04 | HIGH | VERIFIED | Both the settings load and the verification read the flag with an enabled default when it is absent. If the flag is off, the hook returns immediately. |
| C05 | HIGH | PARTIAL | The token is removed from the request parameters, but only **after** the enabled check. When the flag is off, the token stays in the parameters and is passed to the endpoint. "Never reaches the endpoint" is therefore true only in the enabled postures. |
| C06 | HIGH | VERIFIED | An absent secret returns the no-secret result before any outbound call and before any log statement. The hook treats it as a pass. The docstring and settings help ("no keys → no checks") state this policy. |
| C07 | HIGH | VERIFIED | A 2-second timeout and a single call with no retry. The timeout exception class gives the retryable refusal. Every other exception gives the malformed refusal, including connection failure, a non-JSON body, and a missing success key or, when applicable, a missing action key. Both refusals block the request. The HTTP status code is not checked separately. |
| C08 | HIGH (source path) | VERIFIED (source path). Reachability refined, see SF-1 | The minimum score is read before the guarded block and converted to a number after it, on the success branch only. The only default is on the settings field, and no data file seeds the parameter. An absent parameter produces an unhandled type error. Non-numeric text produces an unhandled value error. CON-RCAP-01 is upheld. |
| C09 | HIGH | VERIFIED | A missing score defaults to false, which compares below any positive threshold and gives the bot outcome. With a zero threshold it would not (but see SF-1: a zero threshold cannot persist). |
| C10 | MED | VERIFIED | The binding check runs only when the success flag, the expected action and a non-empty returned action are all truthy. An empty returned action therefore skips the check. A reply with no action key goes to malformed (C07), not to a skip. The expected action comes from the route declaration, not from the client. |
| C11 | HIGH | VERIFIED | The error-code mapping is as stated. The first recognised code wins. An empty or unrecognised code list, a low score and a wrong action all give the generic "suspicious" refusal. Secret and token categories raise validation errors. The others raise user errors. |
| C12 | HIGH | VERIFIED (nuance) | There is no local short-circuit. A missing token is posted as a false value, and how the HTTP client serialises it was not re-read. Rejection depends on the verifier. There is no local replay cache, and duplicate detection relies on the verifier's timeout-or-duplicate code. |
| C13 | HIGH | VERIFIED | Verifier failure: the IP, the error codes and the full raw token are logged at warning. Timeout: IP at error. Other exception: a generic error line with no IP and no exception detail. Low score: IP and score at warning. Wrong action: warning whose action slot prints the score, so the returned action is never logged (CON-RCAP-03 upheld). Success: IP and score at info, on every protected submission. |
| C14 | MED | VERIFIED | The raw remote address of the request is used. Proxy handling is in the core and was not examined. |
| C15 | HIGH | VERIFIED | Four settings fields are bound to plain config parameters and restricted to the system group. The secret is read with elevated privilege at verification. The view gives the secret no password or masking attribute. No encryption. |
| C16 | HIGH | VERIFIED | No constraint or onchange validates the score range or key format. The only guidance is the help text. |
| C17 | HIGH | VERIFIED | Only the site key is added to the backend and frontend session info, and only when the flag is enabled and a site key exists. The secret never appears there. |
| C18 | MED | VERIFIED (nuance) | The library loads only when a site key exists, and the site key is URL-encoded into the script URL. With no key, a "disabled or no site key" message object is returned instead of a token. **Any** client-side execution failure is reported as "site key is invalid". |
| C19 | HIGH | VERIFIED | The host settings model declares the install toggle. The host view defines the block and a "save and come back" notice. This module replaces the toggle's position with the enable flag and replaces the notice with the key inputs. |

Verdict counts: VERIFIED 17, PARTIAL 2, NOT_VERIFIED 0, OUT_OF_SCOPE 0.

A1 business rules: BR1 is PARTIAL (see C02). BR2, BR3 and BR6 are supported. BR4 is supported, with the SF-1 caveat that a zero threshold cannot be persisted. BR5 is supported, including the skip on an empty action. A1 contradictions: CON-RCAP-01 is upheld and refined (SF-1). CON-RCAP-02 is upheld, and its mirror case is added (SF-3). CON-RCAP-03 is upheld.

## 3. Semantic findings (A2)

- **SF-1 (C08 reachability refinement, via core settings save A2-X5/X6).** When the settings screen opens, it shows the field default (0.7) for an absent parameter. The core save writes a numeric setting only when the value is non-zero. A zero value is converted to false, and saving false **deletes** the parameter. Consequences:
  - (a) An admin who saves the secret through the settings screen normally persists 0.7 in the same save. This narrows A1's "never saved" path to secrets set outside the screen: the technical parameter menu, data import, restore/migration, or manual deletion of the parameter.
  - (b) A newly identified path: choosing 0.0, the documented bottom of the scale, deletes the parameter. After that, every *successful* verification raises the unhandled technical error, and the protected forms become unusable for real humans while bots failing verification still receive a defined refusal. In business terms, a plausible admin choice ("accept everyone") turns into an outage.
- **SF-2 (asymmetric failure policy).** A missing secret fails open silently (C06). An *invalid* secret fails closed, and every public visitor gets a message saying the site's private key is invalid (C11). For operators, a key typo blocks every protected form, while deleting the key silently removes protection. The public message also discloses a configuration fault to anonymous users. A1 records both paths but does not state this asymmetry or the disclosure.
- **SF-3 (mirror of CON-RCAP-02).** With a secret configured and **no site key**, the client obtains no token (C18) and the server posts a missing token. The expected verifier reply is missing-input-response, which gives the token-invalid validation error. So every protected form would refuse every visitor. A1's posture list (P0–P3) does not cover this. It is routed to PR-RCAP-08.
- **SF-4 (malformed enable flag, via A2-X7).** The flag is read as text and parsed by a strict boolean helper with no fallback default. Unrecognised text raises a value error. The same parse runs when session info is built (C17), which feeds backend and frontend page loads, not only protected submissions. The settings screen always writes a canonical value, so this path needs a non-screen write. This is a candidate, and is routed to PR-RCAP-09.
- **SF-5 (C05 disabled posture).** When the flag is off, the client token is not removed and is passed to the endpoint as an ordinary parameter. How each endpoint handles an unexpected extra parameter depends on the consumer (for example, a generic form handler might persist or reject unknown fields). This was not examined.
- **SF-6 (business meaning: bot protection).** The protected surface is opt-in per route (C02). One consumer (A2-X9) is a public POST form route that also disables CSRF, so for that route the captcha is the main automated-abuse control, and the fail-open posture (C06) leaves it unprotected with no operator signal. A1's overall posture analysis is sound. It does not overclaim the effect of protection, and it correctly separates configuration fail-open from verifier-outage fail-closed.

Protection-posture matrix (TP5):

| Flag | Site key | Secret | Min score | Client | Server outcome | Defined? |
|---|---|---|---|---|---|---|
| off | any | any | any | No token (the site key is not in session info) | Skip. The token, if present, passes to the endpoint | Yes (C04, SF-5) |
| on | yes | no | any | Tokens minted | Pass, unlogged | Yes, but misleading (C06, CON-RCAP-02) |
| on | no | no | any | No token | Pass | Yes (C06) |
| on | no | yes | any | No token | Token-invalid refusal (expected) | Undocumented (SF-3) |
| on | yes | yes | absent, zero-saved or non-numeric | Tokens minted | Technical error on verifier success. Defined refusal on failure | **No** (C08, SF-1) |
| on | yes | yes (invalid) | any | Tokens minted | Private-key-invalid refusal to the public | Yes, but discloses a fault (SF-2) |
| on | yes | yes | valid | Tokens minted | Full verification (C07, C09–C11) | Yes |

## 4. Omissions (A1 did not address; bank used as topic lens only)

- **OM-1 — hostname and freshness are not checked locally.** Only success, score and action are read from the verifier reply. The returned hostname and challenge timestamp are ignored, so a token minted on another site that shares the same key pair would not be distinguished locally. Freshness relies on the verifier alone.
- **OM-2 — tenant/site scope.** All four settings are database-wide parameters, and the parameter model has no company field (A2-X6). A multi-company or multi-website database therefore has one key pair and one threshold for all its sites and companies. For a SaaS offering this is a tenant-isolation design point.
- **OM-3 — who can read the secret (partial static answer to GAP-5 / CRQ-RCAP-06).** The parameter model's ACL is granted to the system group only (A2-X8). Code paths that read parameters with elevated privilege elsewhere were not enumerated, so GAP-5 stays open but is narrowed.
- **OM-4 — third-party data transfer and privacy.** Each protected submission sends the client IP and token to the vendor and loads a vendor script. A legal-notice template exists (Lane A E8), but A1 has no claim on consent or disclosure. This matters for PDPA/GDPR-style obligations in SME SaaS.
- **OM-5 — outage observability.** The generic exception path logs no IP and no exception detail, so operators cannot tell DNS, TLS, HTTP-status and JSON failures apart. A1 C13 covers what *is* logged but not this diagnostic gap.
- **OM-6 — positive controls that A1 did not state.** The expected action and the threshold are server-side (they come from the route declaration and the server parameter), so a client cannot lower them. The site key is URL-encoded before it goes into the script URL.

## 5. Lane B classification

There is no Lane B Evidence Pool for this module. None of the claims is FAIL on Lane B grounds.

| Claims | Classification | Reason |
|---|---|---|
| C01, C02, C03, C05, C08, C11, C12, C13, C14, C16, C17, C19 | NOT_APPLICABLE | These are structural, dispatch-internal, log or configuration-internal claims with no normal-user surface. |
| C04, C06, C07, C09, C10, C15, C18 | UNCORROBORATED | Their outcome could be observed on the user or admin surface (form accepted or refused, messages, settings screen), but there is no Lane B evidence. |

## 6. Proof requirements (inherently runtime claims only)

| PR | Claim | Falsifiable test (isolated test database, test keys) | Expected (claim holds) | Fail condition (claim falsified) |
|---|---|---|---|---|
| PR-RCAP-01 | C06 | Flag on, site key set, secret absent. Submit a captcha-declared POST with no token | Accepted. No captcha log line at any level | Refused, or any captcha log or operator signal emitted |
| PR-RCAP-02 | C08, SF-1 | Secret set. (a) Delete the min-score parameter. (b) Save 0.0 through the settings screen, then confirm the parameter is absent. Submit with a token that verifies successfully | Unhandled technical error (server error, not a user/validation refusal) in both cases | The request passes, or maps to a defined refusal, or the 0.0 save persists the parameter |
| PR-RCAP-03 | C07 | Secret set. Route the verifier host to a sink that (a) delays by more than 2 s and (b) refuses the connection | (a) Retryable timeout refusal. (b) Malformed refusal. The endpoint is not executed and there is a single outbound attempt | The request is accepted, the endpoint executes, or a retry is observed |
| PR-RCAP-04 | C13 | Force a verifier failure (invalid token). Inspect the server log at warning level | The full token string and the client IP are present | The token is masked or truncated, or absent |
| PR-RCAP-05 | C02 | Send GET/HEAD to a captcha-declared route that accepts them, then list any such routes that have side effects | No verification call on safe methods | A verification call occurs on a safe method |
| PR-RCAP-06 | C10 | Submit a token minted for a different action. Separately, obtain a reply with an empty action | Different action: wrong-action refusal. Empty action: binding skipped and the outcome depends on score | A different-action token passes, or an empty action is refused on binding |
| PR-RCAP-07 | C05, SF-5 | Flag off. Submit with the token parameter to a generic form endpoint | The token parameter reaches the endpoint | The token is stripped when disabled |
| PR-RCAP-08 | SF-3 | Flag on, secret set, site key absent. Submit a protected form from the browser | Token-invalid refusal for every submission | The submission is accepted |
| PR-RCAP-09 | SF-4 | Set the flag parameter to unrecognised text outside the settings screen. Load a backend page and submit a protected form | A technical value error on session-info build and on submission | A graceful default, or a controlled message |
| PR-RCAP-10 | C14 | Behind a reverse proxy, with and without core proxy mode, compare the IP logged and posted with the client's real IP | Documented as the raw peer address unless the core proxy handling rewrites it | A client-supplied header value is used without proxy trust configuration |
| PR-RCAP-11 | C15, OM-3 | As non-system roles (internal user, portal user, public), try to read the secret parameter through any UI or RPC surface | Denied on all of them | The secret is readable by any non-system role |
| PR-RCAP-12 | C12 | Secret set. Submit a protected form with the token parameter omitted, then replay one valid token twice | Missing token: token-invalid refusal. Replay: the second submission is refused (timeout-or-duplicate) | A missing token or a replayed token is accepted |

Proof requirement count: 12.

## 7. Limitations

- This is static review at one anchor commit. Source presence does not establish runtime reachability, and no runtime execution was performed. The verifier's own behaviour (reply content for an empty action, a missing token or a replay) is outside source scope.
- The HTTP client's form-encoding of a missing token, the core proxy handling and the repository-wide set of captcha-declared routes (GAP-1) were not examined. A2-X9 is one example only, not an inventory.
- The JavaScript was read at the helper level only. The interactions glob remains unknown (GAP-2).
- The bank was used only as a topic lens. No QIDs were answered, and nothing was edited. The re-fetched source is held only in the session scratchpad. This review makes no Formal Coverage claim and gives no percentages.
