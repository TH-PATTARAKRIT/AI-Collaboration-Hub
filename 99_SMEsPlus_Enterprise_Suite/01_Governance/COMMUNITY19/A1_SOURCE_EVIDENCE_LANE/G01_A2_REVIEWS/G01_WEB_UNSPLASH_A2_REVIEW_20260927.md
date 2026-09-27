# G01 PLATFORM_BASE — Module `web_unsplash` — RED TEAM A2 Review

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions); independent of A1 |
| Governed group / module | G01 PLATFORM_BASE / `web_unsplash` |
| A1 package under review | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_WEB_UNSPLASH_A1_PACKAGE_20260927.md` |
| A1 package sha256 | `56fbe9f1bd4dea215de6daae9f829eb4fa2eeb63e522b4f5eecbc14cc9598829` |
| Upstream Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_WEB_UNSPLASH_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `9e1ae1b0265bfb38e931e828feaa7f69ea50301b6e9a1d64fbf5bb2a5322b5ea` (equals the value recorded in the A1 header) |
| Question Gate | No module MVQ bank exists; Standard 55 only. A2 verifies claims only. QID-level lineage is **NOT A3-eligible** until GMVQ authors a module bank. Gate condition, not an A1 defect. |
| Source anchor (independent re-check) | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/web_unsplash/`; blobs via `git hash-object` in scratchpad. No request was sent to the external provider. |
| Date | 2026-09-27 |
| Lane B | None exists (section 6) |
| **Disposition** | **A2 PASS WITH FINDINGS** |

Disposition reasons:
1. 18 claims: 17 VERIFIED, 1 PARTIAL, 0 NOT_VERIFIED, 0 OUT_OF_SCOPE. Every security-relevant construction A1 names is present in source as described.
2. PARTIAL C12: the batch-abort conditions are wider than the allow-list rejection A1 names. Image-processing failure and a missing URL also abort, because both sit outside the narrow handlers.
3. CONTRADICTION-UNSP-1 and REFINEMENT-UNSP-1 are independently confirmed.
4. Material omissions: possible access-key exposure through exception text (OM-U01), and "authenticated" includes portal users (SF-U01). Handoff: Reconciliation, carrying 13 proof requirements.

## 2. Test plan (predeclared before verification)

Plan file sha256 `a6365e49e3a9eb6479af0e0cfe5060b3b53fe1ea25ac33624a6b72472efc694c` (scratchpad).

| TP | Test | Pass condition | Result |
|---|---|---|---|
| TP-1 | Lineage hashes | Recorded equals recomputed | PASS |
| TP-2 | Re-fetch 13 Lane A pointer files; probe ACL absence | Blobs match; absence 404 | PASS (13 of 13 match; ACL 404) |
| TP-3 | Semantic re-read of every HIGH claim and CRQ/contradiction item: public app-id via elevation (C04); prefix-only URL check without redirect re-check (C09); test-mode bypasses (C10); no timeout/size/rate limits (C11); elevated local URL (C14); unsanitised caller key in path and extension accumulation (C15); same-path public attachment pickup (C17); search parameter forwarding (C07); manage predicate (C06); abort (C12); CONTRADICTION-UNSP-1 | Meaning matches source | Done, section 3 |
| TP-4 | Business framing + omission scan of controller, 3 models, settings view, test, beacon and service scripts (surface) | Omissions recorded | SF-U01..SF-U05, OM-U01..OM-U07 |
| TP-5 | Lane B classification | Never FAIL for absence | Section 6 |
| TP-6 | Proof requirements | Falsifiable | Section 7 (13 items) |
| TP-7 | Gate note | No bank recorded | Header |

## 3. Claim verdict table

| Claim | A1 conf. | A2 verdict | A2 basis (independent re-read) |
|---|---|---|---|
| A1-G01-UNSP-C01 | HIGH | VERIFIED | Hidden, auto-install, depends on `base_setup` + `html_editor`, one data file (settings view); frontend beacon, media-dialog assets. |
| A1-G01-UNSP-C02 | HIGH | VERIFIED | Two free-text settings fields bound to system parameters; no validation; no models/ACL/groups/rules. |
| A1-G01-UNSP-C03 | HIGH | VERIFIED | Four JSON-RPC routes with the stated auth modes; only attachment add restricts to POST. |
| A1-G01-UNSP-C04 | HIGH | VERIFIED | App-id route is public and reads the parameter with elevated rights. Beacon (on every public frontend page) collects image ids from local provider paths, calls the route, then pings the provider's views endpoint from the visitor's browser with image ids and app id. |
| A1-G01-UNSP-C05 | HIGH | VERIFIED | Access key read with elevation; sent as query parameter on search and notify; not part of any normal route return value. See OM-U01 for the error path. |
| A1-G01-UNSP-C06 | HIGH | VERIFIED | Predicate: access-rights admin group OR website restricted-editor group, both evaluated with elevation; code comment explains the missing website dependency. Save writes both parameters with elevation, no validation; otherwise not-found. See OM-U02. |
| A1-G01-UNSP-C07 | HIGH | VERIFIED | Missing key or app id → role-dependent error; otherwise every caller parameter is encoded to the provider search with the server key set last (overwrites a caller value of the same name); provider JSON returned unchanged; non-OK → role-dependent. See SF-U01 on who "authenticated" includes. |
| A1-G01-UNSP-C08 | HIGH | VERIFIED | Per-item prefix check against two HTTPS image-host prefixes (trailing slash included, so look-alike host names are rejected); fetch; non-OK skipped; connection and timeout errors logged and skipped; image processing with resolution check; mimetype from bytes. |
| A1-G01-UNSP-C09 | HIGH/LOW | VERIFIED | Check is on the submitted string only; the outbound call sets no redirect option, so the HTTP library default applies. There is no post-redirect host check. Exploitability rightly left LOW/open. |
| A1-G01-UNSP-C10 | HIGH | VERIFIED | Both the image allow-list and the notify allow-list are skipped when the framework's current-test marker is set. Refinement: the marker is process-wide state, so a request served by the same process while a test is running would also bypass (SF-U04). |
| A1-G01-UNSP-C11 | HIGH | VERIFIED | No timeout on the image fetch, the search or the notify call; whole body read into memory; no item cap; no rate limit. Only bound: post-download resolution check. |
| A1-G01-UNSP-C12 | HIGH/UNKNOWN | PARTIAL | Verified: a disallowed URL raises a generic exception that the narrow handlers do not catch, so the request stops. Understated: image processing (non-image content or resolution over limit) and a missing URL field also sit outside the handled cases and abort the whole batch. Rollback of earlier items remains UNKNOWN. External notifications already sent for earlier items cannot be undone (OM-U03). |
| A1-G01-UNSP-C13 | HIGH | VERIFIED | Default target model is the view model; record id used only for another model and when supplied, cast to integer; creation delegated to the editor helper; test shows success on own partner/user and access error on another user's record. |
| A1-G01-UNSP-C14 | HIGH | VERIFIED | URL set with elevation to the local provider path; in-code comment names the serving-protection bypass; description written under caller rights; access token generated. |
| A1-G01-UNSP-C15 | HIGH | VERIFIED | Path and name are built from the fixed prefix, the raw caller item key, and the sanitised query. The query keeps Unicode letters/digits, hyphen and space, up to 1024 characters, so spaces end up in URL paths. The extension is appended to the shared query variable on each loop pass, so extensions accumulate. |
| A1-G01-UNSP-C16 | HIGH | VERIFIED | Notify only for the API photos prefix (bypassed in test mode); broad handler logs every failure incl. missing URL; nothing raised. |
| A1-G01-UNSP-C17 | HIGH/MED | VERIFIED | For image paths with the provider prefix and a record id present in the HTML element, the first attachment matching the URL and (same model+record OR public) supplies the binary; no match → empty value. Refinements: with no record id in the element, default handling applies; the lookup runs under the caller's rights. |
| A1-G01-UNSP-C18 | HIGH | VERIFIED | Settings view replaces a placeholder block from `base_setup`, visible only with the module toggle; documentation link; no cron. |

Totals: VERIFIED 17 · PARTIAL 1 · NOT_VERIFIED 0 · OUT_OF_SCOPE 0.

Contradiction/CRQ items: CONTRADICTION-UNSP-1 confirmed (the notify docstring implies a trusted provider value, but the value is caller-supplied and only prefix-checked). REFINEMENT-UNSP-1 confirmed. CRQ-UNSP-1..9 are well-founded. CRQ-UNSP-9 should cover all abort causes (C12 PARTIAL). Add candidates for OM-U01 (secret in exception text) and OM-U02 (credential clearing).

## 4. Semantic / business findings

- SF-U01 (who can use the proxy, C07/C11): "Authenticated user" at this auth level includes external portal users, not only employees. External customers could consume the platform's provider quota and pass arbitrary search parameters. Whether they can create attachments depends on the editor helper's access checks (C13).
- SF-U02 (credential governance, C06): Website restricted editors are content roles. Letting them replace platform-wide integration credentials without validation or an audit trail in this module is a separation-of-duties gap for a multi-tenant SaaS.
- SF-U03 (privacy, C04): Every public page that shows a provider image makes each visitor's browser contact the provider, and anonymous callers can read the configured app id. This is a data-protection disclosure item, not only a security one.
- SF-U04 (test-mode bypass, C10): The bypass is keyed to process-wide test state rather than a configuration flag. The risk is limited to instances that run tests while serving traffic, but it is an unconditional allow-list disable under that condition.
- SF-U05 (local path identity, C15/C17): The local path doubles as an identity key for save-back. Because it is derived from caller data and is not unique, identity resolution can pick another record's public binary. This is a data-integrity risk, not only a naming defect.

## 5. Omissions (material, not in A1)

- OM-U01 Possible access-key exposure (inference): the key travels as a URL query parameter. Library connection-error messages typically embed the request URL, the notify failure is logged with the exception text, and a search connection failure is not caught at all, so it would surface as a JSON-RPC server error to the caller. Needs proof (PR-UNSP-11).
- OM-U02 Credential clearing (inference): the save route writes whatever it receives, including absent values. Under framework parameter semantics this may remove the stored credentials, and any restricted editor can do it.
- OM-U03 Non-transactional side effects: provider download notifications for earlier items are sent before a later item aborts, so they are not rolled back with the request.
- OM-U04 Serving by local path: the test shows the synthetic path is served back with the image bytes. How the framework resolves a path shared by several attachments was not read (ties to C15/C17).
- OM-U05 The search route itself calls the public app-id route's method internally; both key and app id are required even though only the key is sent to the provider.
- OM-U06 Attachment add accepts an arbitrary target model name from the caller. Only the editor helper's access check stands between the caller and attaching to any model.
- OM-U07 The manage predicate references a website group that does not exist when website is not installed; how the group check behaves for a missing group reference was not verified.

## 6. Lane B classification

No Lane B evidence exists for `web_unsplash`. Absence is not a failure.

| Claim | Classification |
|---|---|
| C01, C02, C03, C18 | NOT_APPLICABLE (static declarations) |
| C05, C08, C13, C14, C16 | UNCORROBORATED (runtime-observable; source-determined; C13 already has an in-module test) |
| C04, C06, C07, C09, C10, C11, C12, C15, C17 | MISSING_REQUIRED_RUNTIME_PROOF (security, resource and integrity conclusions whose effect depends on runtime, library defaults or provider behaviour) |

## 7. Proof requirements

All in an authorized, isolated instance; provider endpoints replaced by a controlled mock where noted; no production systems and no traffic to the real provider unless separately authorized.

| PR | Claim(s) | Procedure | Expected (source prediction) | Fail condition |
|---|---|---|---|---|
| PR-UNSP-01 | C04 | Anonymous JSON-RPC call to the app-id route with an app id configured | App id returned | Denied |
| PR-UNSP-02 | C06, SF-U02 | As a website restricted editor (not admin), call the save route with new values; as a plain internal user, repeat | Editor: values stored; plain user: not-found | Editor refused, or plain user succeeds |
| PR-UNSP-03 | C07, SF-U01 | As a portal user, call the search route with an extra parameter and a caller-supplied key parameter; capture the outbound request at a mock | Request forwarded with extra parameter; key parameter is the server value | Portal refused, extra parameter dropped, or caller key forwarded |
| PR-UNSP-04 | C09 | Allowed-prefix URL whose mock host answers with a redirect to an internal address | Internal address fetched | Redirect not followed or host re-checked |
| PR-UNSP-05 | C10, SF-U04 | While a test is running in the same process, submit a non-allow-listed URL via HTTP | Fetched without rejection | Rejected |
| PR-UNSP-06 | C11 | Mock image host delays the response indefinitely / returns a very large body | Worker blocked until an external limit; body fully buffered | Request times out or is size-capped by module code |
| PR-UNSP-07 | C12 | Batch of three: valid, disallowed URL, valid; then valid, non-image content, valid | Request fails; record whether first attachment rows and filestore blobs persist; notify for item 1 already sent | Batch skips the bad item and completes |
| PR-UNSP-08 | C15 | Item key containing path separators and dot segments | Stored local path contains those segments unsanitised | Key sanitised or rejected |
| PR-UNSP-09 | C15 | Two-item batch with the same query | Second item name/path carries two extensions | Each item has one extension |
| PR-UNSP-10 | C17, SF-U05 | Create a public attachment with a given local path on record A; save an image field on record B whose HTML references that path | Record B gets A's binary | B gets empty value or its own binary |
| PR-UNSP-11 | OM-U01 | Mock provider unreachable; trigger notify failure and search failure; inspect server log and JSON-RPC error response | Record whether the key appears in either | — (recorded either way; OM-U01 stands only if the key appears) |
| PR-UNSP-12 | OM-U02 | Restricted editor calls the save route with no values | Record whether stored credentials are removed | — (recorded either way) |
| PR-UNSP-13 | CONTRADICTION-UNSP-1, C16 | Submit a notify URL under the API photos prefix that is not the provider-supplied value; capture at a mock | Request sent with server key | Request not sent |

## 8. Limitations

- Static source at a single anchor commit. Not read: `html_editor` attachment helper, core serving protection and path-based serving, framework parameter semantics, group-check behaviour for a missing group, JSON-RPC error serialization, HTTP library redirect/timeout defaults. Items depending on these are marked inference.
- No request was made to the external provider. Nothing here is runtime proof.
- No QID answered; no module bank, so QID lineage is not A3-eligible until a bank is authored. No Formal Coverage; no percentages.
- Clean room: neutral statements; identifiers (routes, parameter keys, hosts) are pointers; no code reproduced. Inputs unmodified; no git operations.
