# G01 PLATFORM_BASE — RED TEAM A1 Package — `web_unsplash`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `web_unsplash` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_WEB_UNSPLASH_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `9e1ae1b0265bfb38e931e828feaa7f69ea50301b6e9a1d64fbf5bb2a5322b5ea` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/web_unsplash/` |
| Gate status (header only) | There is no module MVQ bank; only Standard 55 applies. No QID answered. The Question Gate controls A2+ QID lineage. It does not control A1 synthesis. |
| Lane B dependency | None. A1 does not wait for Lane B. |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Clean-room note: neutral WHAT / WHY / RISK only. Identifiers (route names, parameter keys, hosts) are evidence pointers, not design recommendations.

Evidence key: E1 `__manifest__.py` 32cfd99d…; E4 `controllers/main.py` 00cf725f… V; E6 `models/ir_qweb_fields.py` 37893572… V; E7 `models/res_config_settings.py` 3136eaef…; E8 `models/res_users.py` 3d4d2d88… V; E9 `views/res_config_settings_view.xml` 0eeb2518…; E11 `tests/test_unsplash.py` 31b8a1af… V; E12 `static/src/frontend/unsplash_beacon.js` 189939d2…

## 1. Claims

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-UNSP-C01 | WHAT: A hidden integration that installs automatically and adds third-party stock-image search to the HTML editor's media dialog. It depends on `base_setup` and `html_editor`, and its only data file is a settings view. RISK: auto-install means the outbound integration surface is present wherever its dependencies are installed. | E1 | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C02 | WHAT: Configuration is two system parameters, an access key and an application id. They are exposed as two free-text settings fields and are not validated. There are no new tables, ACL files, groups or record rules. | E7; E4 V; Lane A §2.4-18 | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C03 | WHAT: There are four JSON-RPC routes: attachment add (authenticated user, POST), image search (authenticated user), app-id read (**public**) and key save (authenticated user, gated). | E4 V | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C04 | WHAT: The public app-id route reads the application id with elevated rights and returns it to anyone, including anonymous visitors. WHY: a frontend beacon on public pages needs it to send view pings from the browser to the provider. RISK: a configuration value is disclosed without authentication, and third-party requests leave visitors' browsers. | E4 V; E12 | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C05 | WHAT: The access key is read with elevated rights and never returned by any route. It is sent to the provider as a query parameter on search and on download notification. | E4 V | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C06 | WHAT: Only a user who passes the manage predicate can save keys through the save route. The predicate is checked with elevated rights and passes for members of the access-rights admin group or of the website restricted-editor group. The website group is referenced without a dependency, as an in-code comment explains. Values are written to system parameters with elevated rights and without validation. Any other user gets a not-found error. RISK: website restricted editors can change platform-wide integration credentials. | E4 V; E8 V | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C07 | WHAT: The search proxy returns `no_access` to non-managers when the key or app id is missing, and `key_not_found` to managers. Otherwise it forwards **all caller-supplied parameters** to the provider's search endpoint, with the server key inserted last (overwriting any value the caller sent under that name), and returns the provider's JSON as it is. A non-OK response gives `no_access` to non-managers and the numeric status to managers. RISK: any authenticated user can send arbitrary parameters under the server's credential and use up its quota. Query sanitisation does not apply on this path. | E4 V | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C08 | WHAT: For each item submitted to attachment add, the image URL must begin with one of two fixed HTTPS image-host prefixes. The server then fetches it, silently skips non-OK responses, and logs and skips connection and timeout errors. The content goes through image processing with a resolution check, and its mimetype is inferred from the bytes. | E4 V | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C09 | RISK (outbound fetch / SSRF-like): the allow-list checks only the submitted URL string by prefix. The outbound client's default redirect following is not disabled, and the host actually reached after any redirect is not checked again. | E4 V | HIGH (construction) / LOW (exploitability; depends on the provider hosts' redirect behaviour) | SOURCE-STATIC |
| A1-G01-UNSP-C10 | WHAT: When the platform's test-mode flag is set, both the image-URL allow-list and the notify-URL allow-list are skipped entirely. RISK: if that flag were ever set outside test runs, the integration would fetch arbitrary URLs. | E4 V | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C11 | WHAT: None of the three outbound requests (image fetch, search, notify) sets an explicit timeout. There is no response-size cap before the body is loaded into memory, no per-user rate limit and no limit on the number of items per request. The only bound is the post-download image resolution check. RISK: resource exhaustion through slow or large responses and batch submissions. The timeout handler fires only on library-level timeouts. | E4 V | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C12 | WHAT: A URL that is not on the allow-list is logged and raises a generic exception. The narrow connection and timeout handlers do not catch it, so the whole request stops at that item instead of skipping it. Whether attachments created earlier in the same request survive depends on how the framework handles the transaction (not verified). | E4 V | HIGH (abort) / UNKNOWN (rollback) | SOURCE-STATIC |
| A1-G01-UNSP-C13 | WHAT: The target model defaults to the view model. A record id is used only when the caller supplies a different model, and it is cast to an integer. Attachment creation is delegated to the editor module's attachment helper. The test confirms that targeting a record the caller cannot access raises an access error, and that targeting permitted records succeeds. | E4 V; E11 V | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C14 | WHAT: After an attachment is created, its URL is set with elevated rights to a synthetic local path under the `/unsplash/` prefix. An in-code comment says this deliberately bypasses the normal protection against a binary attachment also carrying a URL. The code then generates an access token and stores an optional description under the caller's rights. RISK: this is an explicit, deliberate exception to a platform serving-protection rule. | E4 V | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C15 | WHAT: The synthetic path and the attachment name are built from the caller-supplied item key (not sanitised) and the sanitised query (letters, digits, hyphen and space, up to 1024 characters). The file extension is appended to the shared query variable inside the loop, so later items in the same batch accumulate extensions from earlier items. RISK: the local URL path contains caller-controlled segments, and names come out wrong in multi-item batches. | E4 V | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C16 | WHAT: A "download notification" is sent to the provider's API only if the caller-supplied download URL starts with the fixed API photos prefix (skipped in test mode). Every failure, including a missing URL, is logged and not raised. | E4 V | HIGH | SOURCE-STATIC |
| A1-G01-UNSP-C17 | WHAT: When an image field is saved back from edited HTML and the image source path starts with the `/unsplash/` prefix, the binary is taken from the first attachment whose URL matches that path and which either belongs to the same model and record or is public. If there is no match, the field gets an empty value, not the default handling. RISK: matching is by URL path, so a public attachment from another record with the same path (see C15) could supply the binary (inference). | E6 V | HIGH (logic) / MED (collision) | SOURCE-STATIC |
| A1-G01-UNSP-C18 | WHAT: A settings-form inheritance replaces a placeholder block in the base settings and is visible only when the module toggle is set. There are no crons. The test-mode flag changes URL validation. | E9; E7; E4 V | HIGH | SOURCE-STATIC |

## 2. Business rules
- BR-1: Search needs both the key and the app id to be configured. Otherwise the error code depends on the caller's role (C07).
- BR-2: Downloaded images must come from the allow-listed hosts (by prefix) and pass the resolution check (C08, C09).
- BR-3: Attachment ownership follows the caller's access to the target record. The default target is the view model (C13).
- BR-4: Only access-rights admins and website restricted editors can set credentials through the route (C06).
- BR-5: Every download triggers a best-effort notification to the provider, as its API terms require (C16).
- BR-6: HTML save-back resolves integration images from local attachments, scoped to the same record or to public attachments (C17).

## 3. States / transitions
- Integration configuration: unconfigured → configured (save route or settings form). There is no validation and no revocation state (C02, C06).
- Per item: submitted → (URL rejected: request aborts) | (fetch fails: skipped) | attachment created → URL overridden with elevated rights → token generated → provider notified (best effort) (C08, C12, C14, C16).

## 4. Exceptions / failure modes
- A URL outside the allow-list aborts the request (C12).
- Non-OK responses, connection errors and library timeouts are skipped silently or with a log entry (C08).
- Access to the target record is denied with an access error (C13).
- A non-manager calling the save route gets a not-found error (C06).
- A missing or failed configuration returns role-dependent error codes. Provider status codes are exposed only to managers (C07).
- The notification is never raised (C16). HTML save-back with no match gives an empty value (C17).

## 5. Cross-module handoffs
- `html_editor`: the attachment-creation helper (access checks inherited) and the media-dialog assets (C13).
- `base_setup`: the settings view and the module toggle (C18).
- `website` (soft reference, no dependency): the restricted-editor group in the manage predicate, and the frontend beacon bundle (C04, C06).
- Core: attachments (serving-protection bypass, access token), system parameters, the image-field HTML converter and users (C14, C17).
- External: the provider's search API, image CDN hosts, the download-notify endpoint and the browser-side views endpoint (C04, C07–C09, C16).

## 6. Evidence gaps
- GAP-1: the globbed JS directories and `static/tests/**` cannot be enumerated.
- GAP-2: the internals of the `html_editor` attachment helper and of the core serving-protection check were not read. Access behaviour is inferred from this module's test (C13, C14).
- GAP-3: the module toggle and placeholder block live in `base_setup` and were not read (C18).
- GAP-4 (A1): whether items processed before an aborting item are rolled back (C12).
- GAP-5 (A1): how the provider hosts actually redirect, which decides whether C09 is exploitable. This needs runtime or proof work.
- GAP-6 (A1): whether other code paths can create public attachments whose URL collides with the synthetic path (C17).

## 7. CRQ candidates
- CRQ-UNSP-1: Should outbound fetches of external media check the destination host after each redirect, or disable redirects? (C09)
- CRQ-UNSP-2: Should outbound integration calls enforce a timeout, a maximum response size, a per-user rate limit and a per-request item cap? (C11)
- CRQ-UNSP-3: Can a runtime test-mode flag ever disable security allow-lists, or must allow-lists be enforced unconditionally and replaced with test doubles in tests? (C10)
- CRQ-UNSP-4: Should a search proxy forward only an allow-listed set of caller parameters under a server-held credential? (C07)
- CRQ-UNSP-5: May non-admin content editors manage platform-wide integration credentials, and should credential values be validated and audited? (C06)
- CRQ-UNSP-6: May integration configuration identifiers be exposed to anonymous visitors, and is sending browser-side telemetry to third parties from public pages acceptable under privacy policy? (C04)
- CRQ-UNSP-7: Should any feature be allowed to bypass a platform-wide attachment serving protection, and if so under what governed exception? (C14)
- CRQ-UNSP-8: Should local media paths be derived only from sanitised or server-generated identifiers, with collision-safe resolution when HTML is saved back? (C15, C17)
- CRQ-UNSP-9: Should a rejected item in a batch be skipped and reported per item instead of aborting the whole batch? (C12)

## 8. Contradictions
- CONTRADICTION-UNSP-1 — **CONFIRMED** (documentation vs trust assumption, low severity): the notify routine's docstring describes its parameter as "the download_url of the image" required by the provider's API. In source, that value comes straight from the caller's submitted item and is checked only by prefix, not derived from a trusted provider response. Verified in S1.
- REFINEMENT-UNSP-1 (CONFIRMED by S1): Lane A §2.3-6 says the allow-list is bypassed in test mode for images. A1 confirms that the notify-URL allow-list is bypassed by the same flag as well (C10).
- No conflicts between Lane A and the re-fetched source.

## 9. Spot-check log (A1 re-fetch at anchor commit; `git hash-object` compared)
| # | Path | Recorded blob | Recomputed blob | Result | Claim(s) checked |
|---|---|---|---|---|---|
| S1 | addons/web_unsplash/controllers/main.py | 00cf725f…1962 | 00cf725f2366dbaf88fa5baeb1b729f5ba4a1962 | MATCH | C03–C05, C07–C16: public app-id via sudo; prefix-only URL check, default redirects, no timeout/size/rate caps; test-mode bypass (both checks); param passthrough with key last; generic exception abort; sudo URL set with bypass comment; unsanitised key in path; extension accumulation |
| S2 | addons/web_unsplash/models/res_users.py | 3d4d2d88…eb92 | 3d4d2d8885bab0ac00acc3ed6cd4ef92bf82eb92 | MATCH | C06: predicate = access-rights admin OR website restricted editor, checked via sudo |
| S3 | addons/web_unsplash/models/ir_qweb_fields.py | 37893572…758b2bc | 378935726fbaed412399ec4ea70fa5bce758b2bc | MATCH | C17: `/unsplash/` prefix → attachment by URL AND (same model+id OR public), limit one |
| S4 | addons/web_unsplash/tests/test_unsplash.py | 31b8a1af…47b6 | 31b8a1afd22d7789445a613dcf56112322b447b6 | MATCH | C13: success on permitted records; AccessError when targeting another user's record |

Result: 4 of 4 re-fetched blobs match (HTTP 200). This meets the minimum of 3 for this module.

## 10. Provenance
- Input: only the Lane A packet named in the header, pinned by sha256. Re-fetched from `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/web_unsplash/<path>` into scratch storage. No Lane B or bank material was used, and no git operations were run on the repository.

## 11. Limitations
- Static source only. No outbound requests were made to the provider. No runtime proof. No percentages.
- The risks are hypotheses visible in the source, for A2 and Proof. Exploitability (C09) and rollback behaviour (C12) are explicitly unresolved.
