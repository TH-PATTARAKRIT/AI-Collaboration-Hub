# G01 PLATFORM_BASE — Module `google_recaptcha` — PROOF (Stage 2)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2; Reconciliation recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `google_recaptcha` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_GOOGLE_RECAPTCHA_REC_20260927.md` (30 REC items) |
| Upstream A2 | `G01_A2_REVIEWS/G01_GOOGLE_RECAPTCHA_A2_REVIEW_20260927.md` sha256 `961a5d749a296601186b3eb933a5d987f0bbd00265c9670a0969ba39d574ec4b` (12 proof requirements, PR-RCAP-01..12) |
| Upstream A1 / Lane A | sha256 `122308a9…9d0b270` / `a7710f32…2d770479` (full values in the REC intake) |
| Frozen bank | W1-B04, freeze_hash `9e31f2d27dfb959e555cf8ff117d829969e8122fe5e5544bbaf737b6ddea0377` (recomputed, MATCH) |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>` (module, plus the core `odoo/addons/base/`, `odoo/http.py`, `odoo/tools/misc.py`, and the `base_setup` and `website` cross-references) |
| Runtime device | OFFLINE (last recorded 2026-09-24T12:53Z, `MASTER_CONTROLLED_HANDOFF_STATE_20260927.md`) |
| Lane B | None exists (the search is recorded in REC section 3) |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

## 2. Predeclaration

- There are 29 proof cases: 17 SOURCE/CONFIG and 12 RUNTIME. Each A2 proof requirement has one RUNTIME case. The SOURCE/CONFIG cases cover the source-visible premises and the REC items that have no PR.
- The expected and fail conditions were fixed in a scratchpad file **before any Stage-2 source fetch**. That file is `PROOF_CASES_PREDECLARED.md`, shared with `base_sparse_field`, sha256 `59a6e0d0ec0ec259bb7dec88c64d80d74c90c38d89042a3d2c350004096adcbc`, written 2026-09-27T15:03:45Z. The first fetch followed at about 15:04Z.
- RUNTIME cases stay NOT-EXECUTED while the runtime device is OFFLINE. They are ready to run and contain no invented results.
- Verdict rule: PASS means the predeclared expected condition was observed. FAIL means the fail condition was observed.

## 3. Source retrieval and blob verification

All 14 cited files were fetched again (HTTP 200 each) and hashed locally with `git hash-object`. The set is E1, E4–E7, X1–X3 and A2-X4..X9. Copies are in the scratchpad only, and no repository git operations were run. Log: `blob_results.txt`, sha256 `c046d0b2c601beb22a8f5fb8ea43d181bba73bc5e03f91608b19d6973db3222b`.

| Ref | Path | Blob (recorded = computed) | Result |
|---|---|---|---|
| E1 | `addons/google_recaptcha/__manifest__.py` | 0dcee1649c8558f30fbbf7c3c680b0c292bd37ba | MATCH |
| E4 | `addons/google_recaptcha/models/ir_http.py` | 78d5a71cfdcf6acea4c08c9e5ccdc1a42ed7b9c8 | MATCH |
| E5 | `addons/google_recaptcha/models/res_config_settings.py` | c2f237bba64c4147098c610cc41348806a58af7d | MATCH |
| E6 | `addons/google_recaptcha/views/res_config_settings_view.xml` | cb5edc792d822a113f710eb8d9a13142a0abfdcf | MATCH |
| E7 | `addons/google_recaptcha/static/src/js/recaptcha.js` | 2cbbf952a2fa31da0f2e024acd17cfa1d31dabdb | MATCH |
| X1 | `odoo/addons/base/models/ir_http.py` | d9d2a00b9bc7d3e7f439b7ff4ecc46488876953a | MATCH |
| X2 | `addons/base_setup/models/res_config_settings.py` | 7de297811c8722411552e9bdc4ba12b1d2201029 | MATCH |
| X3 | `addons/base_setup/views/res_config_settings_views.xml` | f97b9b257d32480312e4ca826fed780ee99ca19e | MATCH |
| A2-X4 | `odoo/http.py` | ebfc2ac8d268a45aaf4b8cde8c9ce8b480d58dbb | MATCH |
| A2-X5 | `odoo/addons/base/models/res_config.py` | 504644162d067988dd7d3dcb90cd7e1a065c9fc3 | MATCH |
| A2-X6 | `odoo/addons/base/models/ir_config_parameter.py` | 21c82bf62ed0fec4b4307c935f8a2b4ebaff4321 | MATCH |
| A2-X7 | `odoo/tools/misc.py` | 6d27505917a80a2cf9d3b3c6faa6bf8bca86acfd | MATCH |
| A2-X8 | `odoo/addons/base/security/ir.model.access.csv` | 29785e02c9795cd27a0b6b5652853d03995b9c35 | MATCH |
| A2-X9 | `addons/website/controllers/form.py` | 2caa89e06266808af059e4ecc1edaf2812178271 | MATCH |

The negative scans are logged in `static_checks.txt`, sha256 `d28764781afce80c0da4bb654957a03dadcf9801a5adf8eec4f16b705b421c1b`. They found no company reference in the module models or the parameter model, no hostname or timestamp reference in E4, and no constraint, onchange or password attribute in E5 or E6. The only "retry" match in E4 is inside a message string, and E4 contains no loop.

## 4. Proof cases and results

Evidence cites `path`@short-blob with line ranges in the fetched copy. Summaries are neutral and reproduce no code.

| PC | PR / REC | Layer | Preconditions | Steps | Expected | Fail condition | Result | Evidence |
|---|---|---|---|---|---|---|---|---|
| PC-RCAP-01 | lineage / REC-RCAP-01, 21 | SOURCE | Anchor reachable | Fetch the 14 files and run git hash-object on each | Every blob equals the Lane A or A2 SHA-1 | Any mismatch or non-200 response | **PASS** (14/14 MATCH) | `blob_results.txt` |
| PC-RCAP-02 | PR-RCAP-05 premise / REC-RCAP-02, 03 | SOURCE | X1, A2-X4 verified | Read the core dispatch and the safe-method set | The hook is called only when the route has a captcha name AND the method is outside {GET, HEAD, OPTIONS, TRACE}. The hook runs before the endpoint is called. The core default hook is a no-op | The hook runs on safe methods, or after the endpoint | **PASS** for the declarative path. A2's point that "only" is not established still stands: this case read only the generic dispatcher | `odoo/addons/base/models/ir_http.py`@d9d2a00b L347–356, L454–456; `odoo/http.py`@ebfc2ac8 L225 |
| PC-RCAP-03 | PR-RCAP-07 premise / REC-RCAP-04, 05 | SOURCE | E4, E5 | Read the order of steps in the verify hook | The flag is read with an enabled default. When the flag is off the hook returns **before** the token is removed. The token is removed only in the enabled posture | The token is removed before the flag check | **PASS**. The REC-RCAP-05 CONTRADICTION is confirmed on source in A2's favour | `models/ir_http.py`@78d5a71c L44–48 |
| PC-RCAP-04 | PR-RCAP-01 premise / REC-RCAP-06, 07, 22 | SOURCE | E4 | Read the token verification | An absent secret returns "no secret" before any outbound call and before any log statement. The hook treats it as a pass | A refusal or a log line on the no-secret path | **PASS** | `models/ir_http.py`@78d5a71c L80–82, L50–51 |
| PC-RCAP-05 | PR-RCAP-03 premise / REC-RCAP-08, 28 | SOURCE | E4 | Read the outbound call and the exception handling | One POST with a 2-second timeout and no retry loop. A timeout maps to "timeout" and any other exception maps to "bad request", and the hook refuses both. The generic path logs no IP and no detail | A retry loop, or an exception treated as a pass | **PASS** | `models/ir_http.py`@78d5a71c L84–98, L56–59; `static_checks.txt` |
| PC-RCAP-06 | PR-RCAP-02 premise / REC-RCAP-09, 10, 29 | SOURCE+CONFIG | E4, E5, E1, A2-X5, A2-X6 | Read how the min score is read and converted, the manifest data list, the core settings save for float parameters, and set_param with a false value | The min score is read before the guarded block and converted to a number after it, on the success path, with no default. The manifest seeds no parameter. The core save writes false for a zero float. set_param with false deletes the parameter | The conversion is guarded or defaulted, the parameter is seeded, or 0.0 is persisted | **PASS**. CON-RCAP-01 and A2 SF-1 are both confirmed on source. The threshold is server-side (OM-6) | `models/ir_http.py`@78d5a71c L83, L100–102; `__manifest__.py`@0dcee164 `data`; `models/res_config_settings.py`@c2f237bb L13–19; `res_config.py`@50464416 L341–349; `ir_config_parameter.py`@21c82bf6 L82–103 |
| PC-RCAP-07 | PR-RCAP-06 premise / REC-RCAP-11, 12, 29 | SOURCE | E4 | Read the score and action checks | A missing score defaults to false, which is below any positive threshold, giving "is bot". The wrong-action result applies only when the returned action is non-empty and differs. The expected action comes from the route argument | The action check also refuses an empty action | **PASS** | `models/ir_http.py`@78d5a71c L92, L101–107 |
| PC-RCAP-08 | REC-RCAP-07, 13 (C11, SF-2) | SOURCE | E4 | Read how results map to exceptions | Secret codes raise a validation error saying the private key is invalid, and the message is returned to the requester. Token codes raise a validation error. Timeout or duplicate raises a retryable user error. Bad request raises a malformed user error. Anything else raises a "suspicious" user error. The first recognised code wins | A different mapping | **PASS** | `models/ir_http.py`@78d5a71c L50–61, L110–121 |
| PC-RCAP-09 | PR-RCAP-04 premise / REC-RCAP-15, 28 | SOURCE | E4 | Read the log statements | On failure, a warning includes the raw token and the IP. The wrong-action warning puts the score in the action slot. On success, an info line logs the IP and score. The timeout line logs the IP at error level | The token is masked, or the action is labelled correctly | **PASS**. CON-RCAP-03 is confirmed | `models/ir_http.py`@78d5a71c L94, L97, L103, L106, L108, L111 |
| PC-RCAP-10 | PR-RCAP-10 premise / REC-RCAP-16 | SOURCE | E4 | Read where the IP comes from | The raw request remote address | A header-derived IP in the module | **PASS** (module scope; core proxy handling not read) | `models/ir_http.py`@78d5a71c L47 |
| PC-RCAP-11 | PR-RCAP-11 premise / REC-RCAP-17, 18 | CONFIG | E5, E6, A2-X8 | Read the settings fields, the view and the base ACL | Four fields bound to config parameters, each limited to the system group. No constraints or onchange. The secret input has no password or masking attribute. The parameter-model ACL is system-only | A constraint or mask is present, or the ACL is wider | **PASS** | `models/res_config_settings.py`@c2f237bb L10–19; `views/res_config_settings_view.xml`@cb5edc79 L20–23; `security/ir.model.access.csv`@29785e02 L118 |
| PC-RCAP-12 | REC-RCAP-19, 22, 23 (C17) | SOURCE | E4 | Read the session-info hook | Only the public key is added, and only when the flag is enabled and a key is present. The secret is never added | The secret is added | **PASS** | `models/ir_http.py`@78d5a71c L17–34 |
| PC-RCAP-13 | PR-RCAP-09 premise / REC-RCAP-24 | SOURCE | E4, A2-X7 | Read the flag parse and the boolean helper | The helper is called with no fallback on both the verify path and the session path. The helper raises on unrecognised text when no fallback is given. An absent parameter returns a boolean default, which the helper accepts | A fallback is supplied, or the parse is tolerant | **PASS** | `models/ir_http.py`@78d5a71c L30, L44; `odoo/tools/misc.py`@6d275059 L493–516 |
| PC-RCAP-14 | REC-RCAP-25 (OM-1) | SOURCE | E4 | List the reply keys that are read | Only success, score, action and error codes are read. Hostname and challenge timestamp are not read | Hostname or timestamp is checked | **PASS** (0 references) | `models/ir_http.py`@78d5a71c L90–111; `static_checks.txt` |
| PC-RCAP-15 | REC-RCAP-26 (OM-2) | SOURCE | A2-X6, E5 | Read the parameter model fields and the settings fields | The parameter model has only key and value, no company field, and is documented as per-database. The settings fields are not company-dependent | Company scoping present | **PASS** (0 company references) | `ir_config_parameter.py`@21c82bf6 L28–42; `models/res_config_settings.py`@c2f237bb L10–19 |
| PC-RCAP-16 | REC-RCAP-20, 23, 29 (C18) | SOURCE | E7 | Read the JS helper | The library loads only when a site key is present. The key is URL-encoded. With no key a message object is returned and no token is produced. Any failure during execution is reported as an invalid site key | The library loads without a key | **PASS** | `static/src/js/recaptcha.js`@2cbbf952 L18–25, L34–50 |
| PC-RCAP-17 | REC-RCAP-30 (SF-6) | SOURCE | A2-X9 | Read the website form route declaration | A public POST route that declares a captcha action and disables CSRF | No captcha, or CSRF left on | **PASS** (one consumer example; not an inventory) | `addons/website/controllers/form.py`@2caa89e0 L31 |
| PC-RCAP-18 | PR-RCAP-01 / REC-RCAP-06, 22 | RUNTIME | Flag on, site key set, no secret | POST to a captcha route without a token | Accepted, with no captcha log line | Refused, or a log line appears | **NOT-EXECUTED** (runtime device OFFLINE; ready to run) | — |
| PC-RCAP-19 | PR-RCAP-02 / REC-RCAP-09, 10 | RUNTIME | Secret set. (a) Min score deleted. (b) Min score saved as 0.0 | Submit with a token that verifies successfully | An unhandled server error in both cases, and the 0.0 save removes the parameter | The request passes, a defined refusal is returned, or the parameter persists | **NOT-EXECUTED** | — |
| PC-RCAP-20 | PR-RCAP-03 / REC-RCAP-08 | RUNTIME | Verifier routed to a sink that (a) delays more than 2 s or (b) refuses the connection | Submit | (a) A retry refusal. (b) A malformed refusal. The endpoint does not run, and one outbound attempt is made | The request is accepted, or a retry happens | **NOT-EXECUTED** | — |
| PC-RCAP-21 | PR-RCAP-04 / REC-RCAP-15 | RUNTIME | Invalid token | Inspect the warning log | The full token and the IP are present | Masked or absent | **NOT-EXECUTED** | — |
| PC-RCAP-22 | PR-RCAP-05 / REC-RCAP-02 | RUNTIME | A captcha route that accepts GET | Send GET and HEAD | No verification call | A verification call is made | **NOT-EXECUTED** | — |
| PC-RCAP-23 | PR-RCAP-06 / REC-RCAP-12 | RUNTIME | A token minted for another action; a reply with an empty action | Submit | Wrong-action refusal for the first; binding skipped for the empty action | The request passes, or it is refused on binding | **NOT-EXECUTED** | — |
| PC-RCAP-24 | PR-RCAP-07 / REC-RCAP-05 | RUNTIME | Flag off | Submit with the token parameter | The token reaches the endpoint | The token is stripped | **NOT-EXECUTED** | — |
| PC-RCAP-25 | PR-RCAP-08 / REC-RCAP-23 | RUNTIME | Flag on, secret set, no site key | Submit from the browser | A token-invalid refusal every time | Accepted | **NOT-EXECUTED** | — |
| PC-RCAP-26 | PR-RCAP-09 / REC-RCAP-24 | RUNTIME | Flag parameter set to unrecognised text | Load a backend page, then submit | A value error on session-info build and on submit | A graceful default | **NOT-EXECUTED** | — |
| PC-RCAP-27 | PR-RCAP-10 / REC-RCAP-16 | RUNTIME | Reverse proxy, with and without proxy mode | Compare the IP logged and posted with the real client IP | The raw peer address unless the core rewrites it | A spoofable header value is used | **NOT-EXECUTED** | — |
| PC-RCAP-28 | PR-RCAP-11 / REC-RCAP-17 | RUNTIME | Internal, portal and public users | Read the secret through the UI or RPC | Denied | Readable | **NOT-EXECUTED** | — |
| PC-RCAP-29 | PR-RCAP-12 / REC-RCAP-14 | RUNTIME | Secret set | Omit the token; replay a token | A token-invalid refusal; the replay is refused | Accepted | **NOT-EXECUTED** | — |

### Result totals

| Result | Count | Cases |
|---|---|---|
| PASS | 17 | PC-RCAP-01 to PC-RCAP-17 (SOURCE/CONFIG) |
| FAIL | 0 | — |
| NOT-EXECUTED | 12 | PC-RCAP-18 to PC-RCAP-29 (all RUNTIME) |

There were no failures, so none had to be preserved. A static PASS confirms only the source-visible premise. It is **not** runtime proof of the A2 prediction.

Observations for A3 (outside the predeclared cases; not verdicts):
- This module's own settings-load override also parses the flag strictly, with no fallback (`models/res_config_settings.py`@c2f237bb L25). An unrecognised flag value would therefore also affect opening the settings screen, in addition to the two paths in PC-RCAP-13. This was read statically and not executed.
- For a float setting, the core settings load shows the field default when the parameter is absent, and shows 0.0 (with a warning log) when the stored value is not numeric (`res_config.py`@50464416 L268, L284–289). Re-saving a non-numeric value therefore goes through the 0.0 → delete path in PC-RCAP-06. This is a static reading only.
- How the HTTP client encodes a false (missing) token was not read, so the A2 nuance on C12 stays open.

## 5. Effect on REC items

| REC item | Status after Proof |
|---|---|
| REC-RCAP-05 (CONTRADICTION) | PC-RCAP-03 PASS confirms the source side: the token is not stripped when the flag is off, which contradicts A1's "never reaches the endpoint". Runtime confirmation is pending (PC-RCAP-24) |
| REC-RCAP-06, 08, 09, 12, 14, 15, 16, 17 (UNKNOWN_PENDING_PROOF) | The source premises PASS (PC-RCAP-04, 05, 06, 07, 09, 10, 11). REC-RCAP-14 has no static case. All of these stay UNKNOWN_PENDING_PROOF until PC-RCAP-18, 19, 20, 21, 23, 27, 28 and 29 run |
| REC-RCAP-02, 07, 10, 23, 24, 25, 26, 28, 29, 30 (GAP) | Source confirms each A2 finding (PC-RCAP-02, 04/08, 06, 12/16, 13, 14, 15, 05/09, 06/07/16, 17). The runtime effect is pending for 02, 10, 23 and 24 |
| REC-RCAP-27 (GAP, no case) | Third-party transfer and privacy were outside source scope. No proof case. A3 may challenge |
| MATCH items | The static checks PASS for REC-RCAP-01, 03, 04, 11, 13, 18, 19, 20, 21 and 22 |

## 6. Runtime pack (ready to run when the device is online)

Environment: an authorized, isolated test instance at anchor `8d05257d` with `google_recaptcha` and one captcha-declaring consumer installed (for example the website form route). Use vendor **test** keys only, with no production secrets and no production data. PC-RCAP-20 needs outbound DNS/HTTP control, meaning a sink for the verifier host. PC-RCAP-23 and PC-RCAP-29 need either the real verifier with test keys or a controlled stub. Record which one was used, because stub replies are not verifier behaviour. PC-RCAP-27 needs a reverse proxy and control of proxy mode. For each case, capture the HTTP request and response, the server log at warning level and above, the parameter-table state before and after, and the user context. Record every FAIL as it occurs and do not re-run a case to get a pass.

## 7. A3 eligibility and challenge surface

**A3 may challenge now:**
1. The REC classifications, especially the REC-RCAP-05 CONTRADICTION, and the use of GAP rather than CONTRADICTION for REC-RCAP-02 (the "only" overclaim) and REC-RCAP-10 (the SF-1 refinement of C08 reachability).
2. The QID lineage mapping: 34 QIDs mapped, 8 with no evidence, and 3 REC items with no fit.
3. The 17 SOURCE/CONFIG cases that were executed: whether each predicate is sufficient, the line citations, and the blob verification. Most of the SOURCE/CONFIG layer is covered, including the settings save → parameter deletion chain.
4. Predeclaration independence. The cases were written before the Stage-2 fetch, but after reading A1 and A2, which paraphrase the source.
5. The GAP items with no proof case (REC-RCAP-27), and the open items GAP-1 (protected-route inventory), GAP-2 (interactions glob) and GAP-6 (proxy handling).
6. Clean-room compliance and the lineage hashes.

**A3 may not treat as proven:** the outcome of any RUNTIME case (PC-RCAP-18 to PC-RCAP-29), or any behaviour of the external verifier. These remain NOT-EXECUTED, and Lane B stays UNCORROBORATED.

## 8. Limitations

- The source is one anchor commit. The core proxy handling, the HTTP client's form encoding, the interactions glob and the repository-wide inventory of captcha routes were not read.
- No runtime execution took place and no results were fabricated. The external verifier's behaviour is outside the source scope.
- No Formal Coverage claim, no percentages and no QID answered.
- Clean room: neutral summaries only. Identifiers and line numbers are evidence pointers, and no code is reproduced.
- Inputs were not edited, and no git operations were run. Scratch: `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/rec_sprs_rcap`.
