# G01 PLATFORM_BASE — RED TEAM Proof Package — `html_editor`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2 of a two-stage REC + PROOF run) |
| Group / Module | G01 PLATFORM_BASE / `html_editor` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_HTML_EDITOR_REC_20260927.md` (39 items: MATCH 16, CONTRADICTION 6, UNKNOWN_PENDING_PROOF 11, GAP 6) |
| Inputs (sha256 at intake) | A1 `e96156fa…81c4`; A2 `6e078463…ca75`; Lane A `e0e59e77…f10e`; bank `a421e317…ba619` = FREEZE_W1-B07; freeze hash `ea24b270…d332e` (DELTA-RECHECK) |
| Predeclaration | Cases file `scratchpad/rec_hrou_hedt/PROOF_CASES_PREDECLARED.md`, sha256 `a660285fc3698a57c9d13363ef551950768383a63f599450ebee106479e2d5dd`, written 2026-09-27T15:04:59Z; stub with the same cases written to `G01_PROOF/` at 15:05:07Z. **First source fetch began after 15:05:07Z.** |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`; blobs via `git hash-object` in scratchpad (blob log sha256 `9e124cd5701b1075b384266c388257aca0b70baef91b7dd4efd93a07d6bb556e`) |
| Runtime device | **OFFLINE** (per controller brief). Not probed. **No live SSRF, no outbound request to any listener, media/AI endpoint or video platform was attempted** |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

Clean-room note: neutral paraphrase only; no vendor code reproduced; identifiers are evidence pointers. No percentages. No Formal Coverage. No git operations on the repository. Inputs not edited.

## 1. Case design

- A2 PR-HEDT-01..10 → **runtime cases PC-HEDT-R01..R10**, one to one, unchanged (restated in §4).
- Static bases → **SOURCE/CONFIG cases PC-HEDT-01..12**, predeclared and executed now. Static PASS never counts toward a runtime case.

### 1.1 Predeclared static cases

| Case | Layer | Preconditions | Steps | Expected | Fail condition |
|---|---|---|---|---|---|
| PC-HEDT-01 | SRC | — | Hash 11 module files + mail fetcher | Blobs as A2 | Mismatch |
| PC-HEDT-02 | SRC | mail fetcher | Search for host/IP/private checks, scheme list, redirect policy, timeout, byte cap, returned fields | No host/IP block; redirects followed; timeout 3 per-op; no byte cap; metadata returned | Any host/IP/private deny, redirects off, or byte cap |
| PC-HEDT-03 | SRC | — | Public route + internal fallback | `auth=public` passes caller URL; internal falls back for non-record URLs | Not public, or no fallback |
| PC-HEDT-04 | SRC | attachment model | modify_image signature, allow-list, elevated copy, superuser MIME write | Caller bytes; SVG in allow-list; superuser reset | SVG absent, no caller bytes, or no reset |
| PC-HEDT-05 | CFG+SRC | manifests | Import lines; mail/website model uses; reverse-dependent manifests | Module-level imports from mail/iap tool packages; ICE model call; website browse; mail and website depend on html_editor; declared deps base/bus/web | Imports absent or declared |
| PC-HEDT-06 | SRC | base ir_http | Slug call path | Via platform model; resolvable in base | Import from http_routing module path |
| PC-HEDT-07 | SRC | core loader | Addons import mechanism | Namespace package over addons path; no install-state gate | Install-state gate (INCONCLUSIVE if undecidable) |
| PC-HEDT-08 | SRC | — | Media-library save | No timeouts; superuser create; remote MIME; no origin check | Timeout or origin check |
| PC-HEDT-09 | SRC | — | Vimeo thumbnail | Plain-HTTP oEmbed; no in-module caller | HTTPS, or in-module caller |
| PC-HEDT-10 | SRC | — | Query-string editor flags | Injected without requester check | Gated by user/group |
| PC-HEDT-11 | SRC | — | Internal preview catch-all | Raw exception text returned | Generic message |
| PC-HEDT-12 | SRC | — | UUID egress | UUID in media search/download/AI payloads | Absent |

## 2. Blob verification (executed 2026-09-27 ~15:06 UTC)

| File | Expected (A2) | Computed | Result |
|---|---|---|---|
| `addons/html_editor/__manifest__.py` | 6f0356c5… | 6f0356c53e7ea2902dbda178d1b33c57fe06c41c | MATCH |
| `addons/html_editor/controllers/main.py` | df0db6c7… | df0db6c76ab9e4599219761e27027f6ca5695fc7 | MATCH |
| `addons/html_editor/tools.py` | 8683de75… | 8683de75fbf5e6e7c1ea82feb82e7f9ae73187cc | MATCH |
| `addons/html_editor/models/ir_qweb_fields.py` | b080a1cc… | b080a1cca907a6fde688b61b1979e54bf55eac8e | MATCH |
| `addons/html_editor/models/ir_ui_view.py` | b16975fb… | b16975fbfaddcd8e6448039ab97d20d7fe8e064c | MATCH |
| `addons/html_editor/models/ir_http.py` | 77f00f5f… | 77f00f5f3b2f160c81ab513435707901cada86bf | MATCH |
| `addons/html_editor/models/ir_websocket.py` | 98d4d53e… | 98d4d53e9730cb5334993752fb93b89bcff9e493 | MATCH |
| `addons/html_editor/models/html_field_history_mixin.py` | 6ad306f8… | 6ad306f86b11767957b90dbd789aa7bb46d45a24 | MATCH |
| `addons/html_editor/models/ir_attachment.py` | 49820e8d… | 49820e8d353bad5688f023e1e03513a3da9ed50f | MATCH |
| `addons/html_editor/models/test_models.py` | d72b4ef1… | d72b4ef173c28bcf2f1d6db16ae5df59ebb61600 | MATCH |
| `addons/html_editor/security/ir.model.access.csv` | 48079732… | 48079732ad690f12adf58061fbb4f614b1833e97 | MATCH |
| `addons/mail/tools/link_preview.py` | **18515419…** | 18515419263f8fc005029601a5c7bc821cc9f727 | MATCH |
| `addons/mail/tools/__init__.py` | 7c972410… | 7c972410876c75417525580e090cd817294b7d75 | MATCH |
| Manifests mail / iap / website / web / bus | 2f88958b… / 0ee693e7… / aaff2bc9… / 72f3f257… / 2fdfb246… | 2f88958b66791f6bfa3eb1b6f3861538edd10ff4 / 0ee693e7ace840e7e4066e6e4b098d5a7a42088a / aaff2bc93eb79dddb42b4c699b84bf4fb0813bb5 / 72f3f25791583968056ca4a42ab3e9cd13db9e93 / 2fdfb24697ca638a1f1cc0ebfa1884ebdbc81d03 | MATCH |
| `odoo/addons/base/models/ir_http.py` | d9d2a00b… | d9d2a00b9bc7d3e7f439b7ff4ecc46488876953a | MATCH |
| `addons/iap/tools/iap_tools.py` (new) | — | 50b05b6dc2c5022fe4d38f120638da99f52277d8 | recorded (HTTP 200: import target exists) |
| `odoo/modules/module.py` (new) | — | 488a2a063d4c2ccde0b7bb80727880050c3ff2d0 | recorded |
| `odoo/init.py` (new) | — | c6d58274f8f81b8c5633c3aa5eacf2de4af73ebc | recorded |
| `odoo/__init__.py`, `odoo/addons/__init__.py` | — | HTTP 404 at anchor (files absent) | recorded (evidence for PC-07) |
| `odoo/addons/base/__init__.py` (context) | — | ba1318b0d31a58bf730cec7afa6081cc1cef832e | recorded |

## 3. Static cases — executed

| Case | Linked REC / PR | Actual observation (neutral) | Verdict |
|---|---|---|---|
| PC-HEDT-01 | all | 11 module blobs + fetcher blob equal A2 values | **PASS** |
| PC-HEDT-02 | REC-05, REC-33, REC-35 / PR-01..03, PR-10 | Fetcher issues a GET to the caller URL with `allow_redirects` enabled, `timeout=3` (client per-operation timeout), streaming, a browser-like user agent plus an identifying preview header. No IP-address parsing, host, private/loopback/link-local/metadata deny list, or scheme allow-list anywhere in the file; client or URL-parse errors return false. HTML bodies are read in 8 KB chunks and accumulated until a head-close marker is found, with **no byte ceiling**. Image content types return the URL and MIME; HTML returns title, description, image, image type, type, site name and source URL. No throttle construct | **PASS** |
| PC-HEDT-03 | REC-05, REC-26 / PR-01 | External preview route is `jsonrpc`, `auth=public`, POST, passes the caller URL directly to the fetcher and returns its result (description text-stripped). Internal preview (`auth=user`) calls the external preview handler for any URL whose last path segment is not numeric under backend-style prefixes | **PASS** |
| PC-HEDT-04 | REC-10 / PR-05 | modify_image accepts caller `data` (used only if supplied; else source bytes) and caller `mimetype`, rejected only if outside the image allow-list; the allow-list includes `image/svg+xml`. Read check on source record only when source is record-bound; write check on target (model-level when target id is 0). Copy made with elevated rights; if the stored MIME became plain text and differs from requested, it is overwritten as superuser with the requested MIME | **PASS** |
| PC-HEDT-05 | REC-02, REC-03, REC-22, REC-23, REC-27, REC-28 / PR-06 | Controller has module-level imports `odoo.addons.iap.tools` (iap RPC helper) and `odoo.addons.mail.tools` (link preview); ICE-server route calls the mail ICE-server model; view model browses the website model by context id during custom-snippet naming and names four website footer keys. Declared deps `base, bus, web`. mail declares `html_editor`; website declares `html_editor` and `http_routing`; iap declares `web, base_setup` and is auto-install; html_editor/web/bus auto-install | **PASS** |
| PC-HEDT-06 | REC-04, REC-24 | Slug/unslug obtained via the platform request-dispatch model (`env['ir.http']`), not imported from http_routing; base defines both (PC-HROU-08) | **PASS** |
| PC-HEDT-07 | REC-02 / PR-06 | At the anchor neither `odoo/__init__.py` nor `odoo/addons/__init__.py` exists (implicit namespace packages); the core module loader appends configured, readable addons directories to the addons package search path. No install-state check at import is present in the path set-up. Whether importing a non-installed addon's package has side effects is not decided here (runtime R06) | **PASS** |
| PC-HEDT-08 | REC-08, REC-25, REC-33 / PR-04 | Save route (`auth=user`): POST to configurable endpoint with no timeout; per returned URL a GET with no timeout; attachment data public, MIME from remote content-type header; if no duplicate exists, create as superuser. The in-source comment claims a whitelisted origin; no origin/host check precedes the create | **PASS** |
| PC-HEDT-09 | REC-09, REC-32 / PR-08 | Vimeo thumbnail path: GET `http://` oEmbed with the caller video URL interpolated unencoded, then GET of the response's thumbnail URL, 10 s timeouts; other platforms HTTPS. The thumbnail function is referenced only in its own module file; the controller imports only the URL-data helper | **PASS** |
| PC-HEDT-10 | REC-34 / HROU REC-23 / PR-09 | Pre-dispatch adds `editable`, `edit_translations`, `translatable` = true to the request context whenever the key is present in the query string, with no user/group check | **PASS** |
| PC-HEDT-11 | REC-13 | Internal preview catch-all returns the raw exception string; missing-record branch embeds the exception text in a translated message | **PASS** |
| PC-HEDT-12 | REC-20, REC-31 / PR-07 | Database UUID read elevated and added to media download payload, media search payload (together with all caller keyword params, 5 s timeout) and AI text payload (30 s timeout via iap RPC) | **PASS** |

### 3.1 Refinements observed (for A3; no verdict change)

- **R1** The fetcher catches client/URL-parse exceptions and returns false; errors after the response (e.g. HTML parse) are not in that guard — relevant to Q019-type behaviour, runtime only.
- **R2** The superuser MIME write in modify_image depends on the core attachment layer first downgrading the type to plain text; that downgrade logic is base code not read here (R05 decides).
- **R3** iap is auto-install with deps `web, base_setup`; A1's "DB lacking iap" scenario therefore also depends on base_setup's install state (not read).
- **R4** The website-model browse in view naming is not wrapped in any guard for website absence (runtime effect in R06).

## 4. Runtime cases — NOT-EXECUTED (device OFFLINE; ready-to-run in an authorised sandbox only)

All network-facing cases must use sandbox-local listeners/stubs; no third-party hosts.

| Case | = PR | Setup / action | Expected (per source) | Fail condition | Status |
|---|---|---|---|---|---|
| PC-HEDT-R01 | PR-HEDT-01 | Loopback/private listener serving HTML with known title; anonymous POST to external preview | Listener receives request with preview header; title returned | No connection or no title | NOT-EXECUTED |
| PC-HEDT-R02 | PR-HEDT-02 | Sandbox URL 302 → private listener | Redirect followed; title returned | Not followed / blocked | NOT-EXECUTED |
| PC-HEDT-R03 | PR-HEDT-03 | Sandbox server trickles bytes without head-close marker beyond 3 s total | Worker held beyond 3 s; memory grows | Terminated at ~3 s total or size cap | NOT-EXECUTED |
| PC-HEDT-R04 | PR-HEDT-04 | Media endpoint system param → sandbox stub; (a) stall; (b) return SVG URL | (a) hang; (b) public SVG attachment, superuser owner | Timeout, or SVG refused/downgraded | NOT-EXECUTED |
| PC-HEDT-R05 | PR-HEDT-05 | Non-admin editor: modify_image on accessible attachment with own bytes, SVG MIME | Copy keeps SVG MIME with caller bytes | Plain text kept, or rejected | NOT-EXECUTED |
| PC-HEDT-R06 | PR-HEDT-06 | DB with web/bus/html_editor only (mail/iap/website/http_routing code present, not installed): load; ICE route; snippet save; illustration route | Loads; ICE and snippet save error; illustration id-only works | Load failure (supports A1), or ICE/snippet succeed | NOT-EXECUTED |
| PC-HEDT-R07 | PR-HEDT-07 | Capture outbound to media and AI stubs | UUID present in each payload | UUID absent | NOT-EXECUTED |
| PC-HEDT-R08 | PR-HEDT-08 | Downstream module requesting Vimeo thumbnail; sandbox interception returns crafted thumbnail URL | Server fetches crafted URL | Not fetched | NOT-EXECUTED |
| PC-HEDT-R09 | PR-HEDT-09 | Anonymous GET of frontend page with editable/translation query flags | Record rendering effect | Any editor-only data/controls exposed to anonymous | NOT-EXECUTED |
| PC-HEDT-R10 | PR-HEDT-10 | Burst of anonymous preview calls to a sandbox-local target | No throttling | 429/throttling observed | NOT-EXECUTED |

## 5. Summary of results

| Layer | Cases | PASS | FAIL | INCONCLUSIVE | NOT-EXECUTED |
|---|---|---|---|---|---|
| SOURCE / CONFIG | PC-HEDT-01..12 | 12 | 0 | 0 | 0 |
| RUNTIME | PC-HEDT-R01..R10 | 0 | 0 | 0 | 10 |

REC effects: C04 and X-HEDT-03 recorded **CONTRADICTION RESOLVED against A1** (PC-06 + PC-HROU-08). C02 stays CONTRADICTION (static support for A2; R06 decides). X-HEDT-01/02/04 confirmed at source. All 11 UNKNOWN_PENDING_PROOF items stay open. GAP items unchanged.

## 6. A3 eligibility

**Disposition: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.**

A3 may challenge **now — claim level (yes)**:
1. REC classifications/counts (39), both RESOLVED-against-A1 records, and the open C02 contradiction.
2. The 12 static cases and refinements R1–R4, in particular the SSRF guard-absence reading (PC-02/03), SVG storage via modify_image (PC-04), undeclared-dependency import paths (PC-05/07).
3. Whether the SSRF and SVG escalations are stated at the right strength (source-confirmed exposure, exploitability unproven).
4. Input integrity, blob verification (incl. fetcher 18515419…), predeclaration timing, clean-room compliance, Lane B absence record.

A3 may **not** challenge at **QID level (no)**: QID lineage (13 mapped / 27 no evidence) is **NOT A3-ELIGIBLE until canonical re-freeze of W1-B07**.

**Blocked** until runtime is available: R01..R10; closing any UNKNOWN_PENDING_PROOF item; runtime effect of C02. Full A3 → MASTER handoff not eligible.

## 7. Limitations

- No runtime executed; no runtime result claimed; no live SSRF or third-party probing performed.
- Core sanitiser, attachment MIME downgrade, image-processing limits, binary-service access and the JS layer unread (REC GAP items).
- No percentages; no Formal Coverage; no git operations on the repository; inputs not edited.
