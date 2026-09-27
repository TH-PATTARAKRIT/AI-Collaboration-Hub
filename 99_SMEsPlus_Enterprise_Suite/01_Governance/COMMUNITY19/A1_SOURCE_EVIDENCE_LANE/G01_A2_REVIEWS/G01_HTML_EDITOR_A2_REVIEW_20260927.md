# G01 PLATFORM_BASE — Module `html_editor` — RED TEAM A2 Review

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions). Independent of A1; A1 package not repaired. |
| Governed group / module | G01 PLATFORM_BASE / `html_editor` |
| Date | 2026-09-27 |
| A1 package (input, immutable) | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_HTML_EDITOR_A1_PACKAGE_20260927.md` sha256 `e96156fa82878ab6580ea08c74e1dc07a1b8be86c0283ade761f53fcaa81a1c4` |
| Lane A packet (upstream, immutable) | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_HTML_EDITOR_LANE_A_PASS1_20260927.md` sha256 `e0e59e77ce408839e7a0bb64197443c0f9ca8a68d394329adc92bca7236df10e` (matches hash recorded in A1 header) |
| Topic-lens bank | `GMVQ/G01_PLATFORM_BASE/G01_HTML_EDITOR_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `a421e3177abd55333a3647ead363f5e29389223581755b76273cdb84106ba619` (W1-B07). Gate: **DELTA-RECHECK — non-canonical freeze basis**. A2 verification proceeds; **QID-level lineage is NOT A3-eligible until canonical re-freeze**. No QID answered. |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` via raw.githubusercontent; blob ids via `git hash-object` in scratchpad (no repo git ops) |
| Lane B | None supplied. |
| **Disposition** | **A2 VERIFIED WITH FINDINGS (PARTIAL) — HANDOFF TO REC.** 22 VERIFIED, 1 PARTIAL, 2 NOT_VERIFIED, 0 OUT_OF_SCOPE (25 items). SSRF CRQ-HEDT-01 **resolved at source: no safeguards present** (exposure confirmed-from-source; exploitability pending runtime proof). 10 proof requirements. |

### 0.1 Source re-check (independent A2 fetch)

| Path | Lane A blob | A2 computed | Match |
|---|---|---|---|
| `addons/html_editor/__manifest__.py` | 6f0356c5… | 6f0356c53e7ea2902dbda178d1b33c57fe06c41c | YES |
| `addons/html_editor/controllers/main.py` | df0db6c7… | df0db6c76ab9e4599219761e27027f6ca5695fc7 | YES |
| `addons/html_editor/tools.py` | 8683de75… | 8683de75fbf5e6e7c1ea82feb82e7f9ae73187cc | YES |
| `addons/html_editor/models/ir_qweb_fields.py` | b080a1cc… | b080a1cca907a6fde688b61b1979e54bf55eac8e | YES |
| `addons/html_editor/models/ir_ui_view.py` | b16975fb… | b16975fbfaddcd8e6448039ab97d20d7fe8e064c | YES |
| `addons/html_editor/models/ir_http.py` | 77f00f5f… | 77f00f5f3b2f160c81ab513435707901cada86bf | YES |
| `addons/html_editor/models/ir_websocket.py` | 98d4d53e… | 98d4d53e9730cb5334993752fb93b89bcff9e493 | YES |
| `addons/html_editor/models/html_field_history_mixin.py` | 6ad306f8… | 6ad306f86b11767957b90dbd789aa7bb46d45a24 | YES |
| `addons/html_editor/models/ir_attachment.py` | 49820e8d… | 49820e8d353bad5688f023e1e03513a3da9ed50f | YES |
| `addons/html_editor/models/test_models.py` | d72b4ef1… | d72b4ef173c28bcf2f1d6db16ae5df59ebb61600 | YES |
| `addons/html_editor/security/ir.model.access.csv` | 48079732… | 48079732ad690f12adf58061fbb4f614b1833e97 | YES |
| **`addons/mail/tools/__init__.py`** (discovery; A2-only) | — | 7c972410876c75417525580e090cd817294b7d75 | n/a — exports `link_preview` submodule |
| **`addons/mail/tools/link_preview.py`** (SSRF settlement; A2-only) | — | 18515419263f8fc005029601a5c7bc821cc9f727 | n/a |
| Other A2 context reads | — | mail manifest 2f88958b66791f6bfa3eb1b6f3861538edd10ff4; iap manifest 0ee693e7ace840e7e4066e6e4b098d5a7a42088a; base `ir_http.py` d9d2a00b9bc7d3e7f439b7ff4ecc46488876953a; http_routing `ir_http.py` d508ceb82321dbda60e7fcdc1554b74eb17d3c49; bus manifest 2fdfb24697ca638a1f1cc0ebfa1884ebdbc81d03; web manifest 72f3f25791583968056ca4a42ab3e9cd13db9e93; portal manifest 0df9206a8a580649d9c2e81905e3e92a6a109587; website manifest aaff2bc93eb79dddb42b4c699b84bf4fb0813bb5 | n/a |

## 1. Test plan (predeclared before verdicts)

| TP | Target | Method | Pass criterion for VERIFIED |
|---|---|---|---|
| TP1 | Lineage | sha256 of A1 + Lane A + bank; compare to A1 header | Match |
| TP2 | Blob integrity | Re-fetch cited files at anchor; `git hash-object` | Equal to Lane A pointer table |
| TP3 | HIGH claims C01–C13, C20 and all contradictions X-01..04 | Independent semantic re-read of each cited function | WHAT matches; RISK neither overstated nor understated |
| TP4 | Undeclared-dependency claims (C02–C04, X-01..03) | Read counterpart manifests (mail, iap, website, portal, bus, web) and base definition of slug helpers | Dependency is genuinely missing, and the stated failure mode follows |
| TP5 | CRQ-HEDT-01 (SSRF) | Discover mail link-preview fetcher via mail tools package; read fetcher fully | Record scheme/host/IP filter, redirect policy, timeout, body cap, reflected fields |
| TP6 | Outbound calls (C06–C09, C20) | Verify each timeout / absence of timeout, protocol, trust of remote data, identifier egress | As stated |
| TP7 | Elevated paths (C10, C11, X-04) | Trace which caller inputs reach elevated operations | As stated |
| TP8 | MED claims C14–C19, C21 | Re-read specific functions (A1 did not) | As stated |
| TP9 | Business meaning | Evaluate as a SaaS rich-text/media layer (sanitisation, uploads, external fetch, tenant data egress, collaboration integrity) | Omissions/overclaims listed |
| TP10 | Lane B / runtime | Classify; convert runtime-inherent items to proof requirements | NOT_APPLICABLE / UNCORROBORATED; expected + fail condition |

## 2. Claim verdict table

| Item | A1 conf. | A2 verdict | A2 independent basis (neutral) |
|---|---|---|---|
| C01 | HIGH | VERIFIED | Hidden, auto-install; deps base, bus, web; data = ACL file only. |
| C02 | HIGH | **PARTIAL** | Module-level imports from mail (link-preview tool) and iap (RPC tool) and a call to mail's ICE-server model — true, undeclared. But: (a) **mail itself declares html_editor as a dependency**, so declaring mail here would create a cycle — the gap is structural, not an oversight (A1 omitted); (b) the stated failure mode "auto-install on a DB lacking mail/iap may fail at import" is not established: Python import resolution depends on the code being present on the addons path, not on database install state (inference). The source-certain runtime failure is at call time of the ICE-server route when mail is not installed. |
| C03 | HIGH | VERIFIED | Custom-snippet save browses the website model and applies its domain; view-save patch names four website footer view keys. |
| C04 | HIGH | **NOT_VERIFIED** | The platform base layer already defines id-only slug and unslug on the same abstract model; http_routing only overrides them with name-slugs. html_editor's calls resolve without http_routing (id-only form). No undeclared dependency is established. Behavioural consequence only: without http_routing, illustration URLs are id-only, and name-bearing illustration paths fall back to exact-URL lookup. |
| C05 | HIGH | VERIFIED (CRQ resolved) | Public, POST, JSON-RPC route passes caller URL straight to mail fetcher; this module adds no filter. See CRQ-HEDT-01 outcome in §6. |
| C06 | HIGH | VERIFIED | HEAD to caller URL, 10 s timeout, MIME set only if in image allow-list and status 200. A2 notes: HEAD is issued before the rights-bypass decision; network errors are not caught in this module (surface to caller). |
| C07 | HIGH | VERIFIED | Remote GET for non-local, non-`/web/image` sources; timeout constant 2.5 s (per socket operation); result validated and re-encoded by imaging library. Also: redirect-type attachment URLs trigger a remote fetch of the attachment's stored URL. In-source comment itself questions keeping remote loading. |
| C08 | HIGH | VERIFIED | POST to configurable endpoint with no timeout; per-URL GET of remote-returned URLs with no timeout; MIME from remote header; attachment created public as superuser when no duplicate exists. Route is `auth=user` (any authenticated user, incl. portal-type users unless otherwise blocked — inference). |
| C09 | HIGH | VERIFIED (reachability qualified) | Vimeo oEmbed over plain HTTP; caller video URL interpolated unencoded into the oEmbed query; thumbnail URL from response then fetched; others HTTPS; 10 s timeouts. A2 qualifier: no html_editor route calls the thumbnail function — reachability exists only through downstream consumers. |
| C10 | HIGH | VERIFIED (risk sharpened) | Read check on source only when source is bound to a record; write check on target (for view-bound targets the check runs on an empty recordset, i.e. model-level only — inference); elevated copy; superuser MIME reset when downgraded to plain text. A2 adds: **the stored bytes may be caller-supplied** (not necessarily the source's), and the caller-supplied MIME is limited to the image allow-list, **which includes SVG**. |
| C11 | HIGH | VERIFIED | Elevated create + token (bypass hook, default off), elevated illustration lookup on public shape route, elevated action lookup in internal preview, elevated config reads. |
| C12 | HIGH | VERIFIED | 15 route decorators; exactly three `auth=public` (shape, image_shape, link_preview_external). |
| C13 | HIGH | VERIFIED | Catch-all returns raw exception text; missing-record errors also embed exception text. |
| C14 | MED | VERIFIED | Image-flagged upload: sniffed MIME vs allow-list, resolution verification via image processing; non-image payload accepted without type check; no byte cap in module. |
| C15 | MED | VERIFIED | Removal blocked if any view arch contains the escaped local URL (quoted). Business note: only views are checked — references in other HTML fields (records, messages) do not block removal. |
| C16 | MED | VERIFIED | Colour params hex/rgb(a) or theme tokens resolved from frontend CSS; else bad request; module shapes `.svg`-filtered; illustrations must be public binary with URL matching request path (with URL-lookup fallback). |
| C17 | MED | VERIFIED | Sanitize required for versioned fields; direct history writes stripped; cap 300; revision stores user id and user name. |
| C18 | MED | VERIFIED | Marker applied only in branded (editable) rendering; override-group users unmarked; others get edit-prevented marker if content would fail sanitisation. Enforcement of the marker is client-side (JS, unread). |
| C19 | MED | VERIFIED | Divergence check rejects when stored last step absent from incoming steps; channel subscribe and broadcast require non-public user plus record and field read+write. Bus notification emitted on every write with a history marker (and without). |
| C20 | HIGH | VERIFIED | Database UUID sent to media search, media download-URL and AI-text endpoints; AI 30 s, search 5 s, download none. Search forwards arbitrary caller params to the external endpoint. |
| C21 | MED | VERIFIED | Two converter test models in production import path; ACL system-group full CRUD only. |
| X-HEDT-01 | — | VERIFIED (qualified) | Contradiction real; structural cause (mail → html_editor reverse dependency) — see C02. |
| X-HEDT-02 | — | VERIFIED | website model and keys referenced; website depends on html_editor (reverse edge), same structural pattern. |
| X-HEDT-03 | — | **NOT_VERIFIED** | Not a contradiction: helpers exist in base (see C04). |
| X-HEDT-04 | — | VERIFIED | "Whitelisted origin" comment not enforced: download URLs come from the configurable endpoint's response with no origin check before superuser create; trust reduces to whoever controls the configured endpoint (system parameter) and the transport. |

## 3. Semantic findings (SaaS rich-text / media layer)

| ID | Finding | Effect on A1 |
|---|---|---|
| SF-HEDT-01 | **Unauthenticated server-side fetch with partial reflection.** The public link-preview route triggers a server GET to any http(s) URL, follows redirects, and returns title/description/image/site-name/type for HTML responses, or echoes the URL with its MIME for image responses. This is an SSRF primitive with partial response disclosure (internal pages' titles/metadata), reachable anonymously. | C05 RISK upgraded from "safeguards unread" to "no safeguards at source". |
| SF-HEDT-02 | **Worker-exhaustion surfaces.** (a) Link preview: 3 s is a per-operation timeout, and the body reader accumulates until a head-close marker is found with no byte ceiling — a slow or head-less stream can hold a worker and grow memory; (b) media-library download: no timeout at all. For a SaaS multi-tenant worker pool this is a shared-availability risk. | Supports CRQ-HEDT-04; adds link-preview variant. |
| SF-HEDT-03 | **Stored-content trust via SVG.** Two paths yield SVG attachments despite core MIME downgrade: superuser media-library create and superuser MIME reset in image modification with caller-supplied bytes. Public SVG served from the application origin is an active-content concern for a rich-text platform. | CRQ-HEDT-04 and -06 sharpened. |
| SF-HEDT-04 | **Tenant identifier egress.** Database UUID leaves the tenant on media search/download and AI text calls, to endpoints overridable by system parameter. Business meaning: identifiable per-tenant telemetry to a third party; in SaaS this needs a privacy/DPA decision. | CRQ-HEDT-08 remains policy (out of verification scope). |
| SF-HEDT-05 | **Dependency graph is intentionally inverted.** html_editor is a lower layer that opportunistically calls higher layers (mail, iap, website). Architecture meaning: the editor is not independently deployable; undeclared upward calls are a layering smell rather than accidental omissions. | C02/X-01/X-02 qualified; C04/X-03 rejected. |
| SF-HEDT-06 | **Query-string editor flags for any requester.** Editable/translation flags are injected into context from the query string on every dispatch, including public requests; impact depends on consumers (unread). Links to http_routing error-template `editable` gate (HROU O3). | CRQ-HEDT-09 remains open → PR-HEDT-09. |
| SF-HEDT-07 | **Attachment-reference protection is view-only.** Business rule BR3 ("referenced attachments cannot be removed") holds only for view architectures; record-level HTML content can lose images. | BR3 overstated in business terms; C15 technically correct. |

## 4. Omissions (not in A1)

- O1: Internal link preview falls back to the external fetcher for any URL not shaped like a backend record path — a second (authenticated) SSRF entry point.
- O2: mail → html_editor and website → html_editor reverse dependencies (explains X-01/X-02).
- O3: html_editor, web and bus are all auto-install; html_editor is effectively present wherever the web client is.
- O4: Public image-in-shape route resolves an arbitrary record image by key through the binary service (access enforcement delegated, unread).
- O5: HTML→image converter also reads arbitrary model/field binaries named in `/web/image/...` source URLs under the current user's rights at save time.
- O6: Media-library search forwards arbitrary caller parameters to the external service (in addition to the UUID).
- O7: The Vimeo request embeds the caller URL unencoded in the query string (parameter injection toward the oEmbed service).

## 5. Lane B classification

No Lane B evidence supplied. No claim is FAIL on that basis.

| Claims | Classification |
|---|---|
| C01, C02, C03, C04, C11, C12, C14, C15, C16, C17, C21, X-01..X-04 (structural/static) | NOT_APPLICABLE |
| C05, C06, C07, C08, C09, C10, C13, C18, C19, C20 (request-/network-time behaviour) | UNCORROBORATED |

## 6. CRQ outcomes (A2)

| CRQ | A2 outcome |
|---|---|
| **CRQ-HEDT-01 SSRF on public link preview** | **RESOLVED AT SOURCE — NO SAFEGUARDS.** Fetcher (mail link-preview tool, blob 18515419…) applies: no host/IP/private-range/loopback/metadata deny list; no explicit scheme allow-list (only the HTTP client's native http/https support; other schemes error and return false); redirects followed; 3 s per-operation timeout; streamed read with no byte cap until head-close marker; identifying request header added; parsed metadata returned to caller. Exposure = CONFIRMED-FROM-SOURCE; deployment-level egress controls unknown → PR-HEDT-01..03 |
| CRQ-HEDT-02 rate limiting | No throttle in module or fetcher (source); infra unknown → PR-HEDT-10 |
| CRQ-HEDT-03 host lists on HEAD/converter GET | Confirmed: none at source |
| CRQ-HEDT-04 media-library stall / SVG as superuser | Source-indicated YES (no timeouts; superuser create; remote MIME) → PR-HEDT-04 |
| CRQ-HEDT-05 plain-HTTP Vimeo steering | Source-indicated YES, reachable only via downstream callers → PR-HEDT-08 |
| CRQ-HEDT-06 modify_image MIME escalation | Source-indicated YES for SVG with caller bytes → PR-HEDT-05 |
| CRQ-HEDT-07 load without mail/iap/http_routing/website | Partly answered: http_routing not needed (base helpers); mail/website are reverse-dependents; runtime failure expected at call sites → PR-HEDT-06 |
| CRQ-HEDT-08 UUID egress acceptability | OUT_OF_SCOPE for verification (policy) — fact verified (C20); route to privacy/design |
| CRQ-HEDT-09 anonymous editable flag | Open → PR-HEDT-09 |

## 7. Proof requirements (MISSING_REQUIRED_RUNTIME_PROOF — inherently runtime; authorised sandbox only)

| PR | Claim(s) | Setup / action | Expected (per source) | Fail condition |
|---|---|---|---|---|
| PR-HEDT-01 | C05, CRQ-01 | Sandbox with a listener on loopback/private address serving an HTML page with a known title; anonymous POST to external preview with that URL | Listener receives request (preview header present); response carries the known title | A2 source reading FALSIFIED if no connection reaches the listener or title is not returned |
| PR-HEDT-02 | C05, CRQ-01 | External test URL that 302-redirects to the private listener | Redirect followed; title returned | Redirect not followed / blocked |
| PR-HEDT-03 | SF-02 | Test server that sends bytes slowly without a head-close marker for longer than 3 s total | Worker remains occupied beyond 3 s; memory grows with body | Request terminated at about 3 s total or at a size cap |
| PR-HEDT-04 | C08, X-04, CRQ-04 | Point media-library endpoint (system param) at a stub; (a) stub stalls; (b) stub returns a URL to an SVG | (a) request hangs without client-side timeout; (b) public SVG attachment created with SVG MIME, owner superuser | Timeout observed, or SVG downgraded/refused |
| PR-HEDT-05 | C10, CRQ-06 | Non-admin editor calls image modification on an accessible attachment with own bytes and SVG MIME | Stored copy keeps SVG MIME (superuser reset) with caller bytes | MIME remains plain text, or call rejected |
| PR-HEDT-06 | C02, C04, CRQ-07 | DB with web/bus/html_editor only (mail/iap/website/http_routing code present but not installed): load server, call ICE-server route, snippet save, illustration route | Module loads; ICE route and snippet save error; illustration route works with id-only slug | Module fails to load (would support A1's import-failure claim), or ICE/snippet calls succeed |
| PR-HEDT-07 | C20 | Capture outbound requests to media stub and AI stub | Database UUID present in each payload | UUID absent |
| PR-HEDT-08 | C09, CRQ-05 | Via a downstream module that requests Vimeo thumbnails, with HTTP interception returning a crafted thumbnail URL | Server fetches the crafted URL | Crafted URL not fetched (e.g. HTTPS enforced by client) |
| PR-HEDT-09 | SF-06, CRQ-09 | Anonymous GET of a frontend page with editable/translation query flags | Record effect on rendering (branding attributes, debug-like blocks) | — (observation proof: fail = any editor-only data/controls exposed to anonymous) |
| PR-HEDT-10 | CRQ-02 | Burst of anonymous preview calls from one client | No throttling responses | Throttling/429 observed (narrows SF-01) |

## 8. Limitations

- Source presence ≠ runtime reachability; outcomes are source-level; proofs are not executed.
- JS layer (client-side sanitisation, DOMPurify use, marker enforcement) not studied; core sanitiser, image-processing limits and binary-service access rules unread.
- The C02 import-behaviour point is an inference about the platform's module import mechanism, not read in this review; PR-HEDT-06 decides it.
- QID-level lineage not A3-eligible until canonical re-freeze of W1-B07 (DELTA-RECHECK basis).
- Clean room: neutral WHAT/WHY/RISK only; no vendor code reproduced; identifiers are evidence pointers.
- No percentages; no Formal Coverage claimed; no git operations performed.
