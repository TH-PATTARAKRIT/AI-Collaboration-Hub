# G01 PLATFORM_BASE — Module `html_editor` — RED TEAM A1 Package

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Governed group / module | G01 PLATFORM_BASE / `html_editor` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_HTML_EDITOR_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `e0e59e77ce408839e7a0bb64197443c0f9ca8a68d394329adc92bca7236df10e` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Freeze (topic lens only) | W1-B07, freeze_hash `ea24b270cf375fc108735ca6e15d68500dd9b5cfb69e849bd2eb673a232d332e`; bank `G01_HTML_EDITOR_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `a421e317…9223581755b76273cdb84106ba619` (matches FREEZE_W1-B07.json) |
| Gate status | **DELTA-RECHECK — non-canonical freeze basis, reproducible** (QUESTION_GATE_G01_FREEZE_REPLAY_20260927; upgraded from R14 HOLD). A1 proceeds as source research; canonical re-freeze pending. |
| Date | 2026-09-27 |
| Lane B dependency | None. A1 did not wait for, view, or use Lane B evidence. |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Bank used as a topic lens only (sanitisation, uploads, outbound fetch, elevated rights, collaboration, dependency integrity). No QID answered; bank not edited. Paths relative to `addons/html_editor/` at the anchor. JS layer out of scope (Lane A counted only).

## 1. Claims

| Claim ID | Claim (neutral WHAT / WHY / RISK) | Evidence (path @ blob) | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-HEDT-C01 | WHAT: hidden, auto-installed editor framework declaring deps `base`, `bus`, `web`; ships only an ACL file as data. | `__manifest__.py` @ 6f0356c5 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C02 | WHAT: controller imports at module load a link-preview tool from `mail` and an RPC tool from `iap`, and calls a `mail` ICE-server model; neither is declared. RISK: auto-install on a DB lacking mail/iap may fail at import. | `controllers/main.py` @ df0db6c7 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C03 | WHAT: view model browses the `website` model and patches `website.*` footer view keys; `website` not declared. | `models/ir_ui_view.py` @ b16975fb (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C04 | WHAT: controller uses slug/unslug helpers that are defined in `http_routing`, which is not declared. | `controllers/main.py` @ df0db6c7 (spot-checked) + HROU `models/ir_http.py` @ d508ceb8 | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C05 | WHAT: `/html_editor/link_preview_external` is `auth=public`, POST, and passes a caller-supplied URL to the mail link-preview fetcher; module applies no scheme/host filter itself. RISK: unauthenticated server-side fetch; safeguards unread. | `controllers/main.py` @ df0db6c7 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C06 | WHAT: URL-attachment creation issues a HEAD to a user-supplied URL (10 s timeout) to infer image MIME. RISK: authenticated-user outbound probe. | `controllers/main.py` @ df0db6c7 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C07 | WHAT: HTML→image converter GETs non-local `src` URLs on save (2.5 s timeout) and re-encodes the result. RISK: save-time outbound fetch driven by editor content. | `models/ir_qweb_fields.py` @ b080a1cc (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C08 | WHAT: media-library save POSTs to a configurable endpoint and then GETs each URL in the remote response, both without timeout; content stored as public attachment created as superuser with MIME taken from remote header. RISK: hang on slow host; trust in remote-supplied URLs/MIME (comment asserts "whitelisted origin", not enforced here). | `controllers/main.py` @ df0db6c7 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C09 | WHAT: Vimeo thumbnail lookup calls the oEmbed API over plain HTTP, then GETs a thumbnail URL taken from that response; other platforms use HTTPS; all 10 s timeout. RISK: MITM-injectable URL fetched server-side. | `tools.py` @ 8683de75 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C10 | WHAT: `modify_image` checks read on source / write on target, then copies with elevated rights and resets MIME as superuser if downgraded to plain text. RISK: MIME-downgrade guard bypassed deliberately. | `controllers/main.py` @ df0db6c7 (spot-checked: sudo copy, SUPERUSER_ID MIME write) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C11 | WHAT: other elevated paths — sudo attachment create + token (bypass hook), sudo illustration lookup on public shape route, sudo action resolution in internal link preview, sudo config-param reads. | `controllers/main.py` @ df0db6c7 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C12 | WHAT: public routes are exactly shape, image_shape and link_preview_external; all others require a user session. | `controllers/main.py` @ df0db6c7 (spot-checked: 15 route decorators) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C13 | WHAT: internal link preview catches all exceptions and returns raw exception text. RISK: internal detail disclosure to authenticated users. | `controllers/main.py` @ df0db6c7 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C14 | WHAT: base64 upload enforces image type allow-list only when flagged as image; no byte-size cap in this module. | `controllers/main.py` (Lane A item 12, 27) | MED | SOURCE-STATIC |
| A1-G01-HEDT-C15 | WHAT: attachment removal blocked while any view arch references its URL. | `controllers/main.py` (Lane A item 15) | MED | SOURCE-STATIC |
| A1-G01-HEDT-C16 | WHAT: shape colour params restricted to hex/rgb(a)/theme tokens; module shapes `.svg` only; illustrations only from public attachments whose URL matches the request. | `controllers/main.py` (Lane A item 16) | MED | SOURCE-STATIC |
| A1-G01-HEDT-C17 | WHAT: HTML history mixin requires sanitized fields, strips direct history writes, caps at 300 revisions, records user id and name per revision. | `models/html_field_history_mixin.py` @ 6ad306f8 (Lane A) | MED | SOURCE-STATIC |
| A1-G01-HEDT-C18 | WHAT: sanitize-override: content saved by a privileged user that would fail sanitisation is marked edit-prevented for non-privileged editors. WHY: prevents silent stripping. | `models/ir_qweb_fields.py` @ b080a1cc (Lane A) | MED | SOURCE-STATIC |
| A1-G01-HEDT-C19 | WHAT: collaborative save rejects incoming HTML whose step history does not contain the stored last step; channel subscription and broadcast require non-public user with read+write on record and field. | `tools.py` @ 8683de75; `models/ir_websocket.py` (Lane A) | MED | SOURCE-STATIC |
| A1-G01-HEDT-C20 | WHAT: database UUID is sent to the external media-library and AI-text endpoints (configurable); AI call 30 s timeout, media search 5 s. RISK: tenant identifier egress. | `controllers/main.py` @ df0db6c7 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HEDT-C21 | WHAT: two test models ship in the production import path with system-only ACL. | `models/test_models.py`, `security/ir.model.access.csv` (Lane A) | MED | SOURCE-STATIC |

## 2. Business rules
- BR1 Stored HTML is sanitised at field level (core); editor signals mode and blocks edits that would lose privileged content (C18).
- BR2 Versioned HTML requires sanitised fields; history is server-owned and capped (C17).
- BR3 Referenced attachments cannot be removed (C15).
- BR4 Image edits produce linked copies; access checked on source read and target write (C10).
- BR5 Video embeds restricted to a platform whitelist (Lane A item 18).

## 3. States / transitions
- Attachment: uploaded/URL → (dedup hit | created) → modified copy (linked to original) → variants → removable only when unreferenced (C06, C10, C15).
- Collaborative doc: steps accumulate → save with matching last step OK / divergent → validation error (C19).
- History: write → post-sanitise diff → revision appended → prune beyond cap (C17).

## 4. Exceptions / failure modes
- Unsupported image MIME → error payload (C14); invalid shape colour → bad request (C16).
- History divergence → validation error (C19); unsanitised versioned field → validation error (C17).
- Media-library non-OK → generic exception; per-URL GET may hang (no timeout) (C08).
- Internal link preview → raw exception string to client (C13).
- Missing mail/iap at import → load failure (CANDIDATE, C02).

## 5. Cross-module handoffs
- Declared: base (attachment, view, template, binary), bus (collaboration channels), web.
- Undeclared: mail (link preview, ICE servers), iap (RPC), http_routing (slug/unslug), website (model, footer keys).
- Reverse: http_routing 404 page consumes shape route; html_builder remapped from legacy shape module name.
- External: media-library and AI-text services (configurable endpoints), video platforms.

## 6. Evidence gaps
- EG1 Core sanitiser policy (Lane A G1). EG2 mail link-preview safeguards — scheme/host/IP/size (G2).
- EG3 Upload size / resolution caps in core (G3). EG4 Consumers of query-string `editable`/`translatable` flags (G4).
- EG5 Why import of undeclared mail/iap does not break auto-install in practice (manifest chain beyond module unread) (G5).
- EG6 JS globs, DOMPurify usage (G6). EG7 Tests (G7).

## 7. CRQ candidates
| CRQ | Question | Why |
|---|---|---|
| CRQ-HEDT-01 | Does the public external link-preview fetch block private/loopback/metadata addresses, non-HTTP schemes, redirects and large bodies? | C05, EG2 (SSRF, unresolved) |
| CRQ-HEDT-02 | Is there rate limiting on the public link-preview route? | C05 |
| CRQ-HEDT-03 | Are HEAD (URL attachment) and image-converter GET subject to any host allow/deny list? | C06, C07 |
| CRQ-HEDT-04 | Can a slow/hostile media-library host stall workers (no timeout) and inject arbitrary public SVG as superuser? | C08 |
| CRQ-HEDT-05 | Can plain-HTTP Vimeo oEmbed response steer server fetch of arbitrary thumbnail URL? | C09 |
| CRQ-HEDT-06 | Does the sudo copy / superuser MIME reset in modify_image allow MIME escalation (e.g. SVG) beyond caller rights? | C10 |
| CRQ-HEDT-07 | Does the module load/function when mail, iap, http_routing or website are absent? | C02–C04 |
| CRQ-HEDT-08 | Is database-UUID egress to external services acceptable per tenant privacy policy? | C20 |
| CRQ-HEDT-09 | Can an anonymous request set `editable`/`translatable` via query string to alter rendering? | EG4 |

## 8. Contradictions
| ID | Contradiction | Status |
|---|---|---|
| X-HEDT-01 | Declared deps `base, bus, web` vs module-level imports from `mail` and `iap` plus `mail.ice.server` call. | **CONFIRMED-FROM-SOURCE** (spot-checks 1, 2) |
| X-HEDT-02 | Declared deps vs `website` model browse and `website.*` view keys. | **CONFIRMED-FROM-SOURCE** (spot-checks 1, 5) |
| X-HEDT-03 | Declared deps vs use of `http_routing` slug/unslug helpers. | **CONFIRMED-FROM-SOURCE** (spot-check 2 + HROU spot-check 4) |
| X-HEDT-04 | Code comment asserts media SVGs come from a "whitelisted origin" but no origin check exists before superuser create. | **CONFIRMED-FROM-SOURCE** as source-visible absence in this file (spot-check 2); enforcement elsewhere unknown |

## 9. Spot-check log
Re-fetched from `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/html_editor/<path>`; `git hash-object` computed in session scratchpad (no repo git operations).

| # | Path | Recorded blob | Computed blob | Match | Claim(s) verified in content |
|---|---|---|---|---|---|
| 1 | `__manifest__.py` | 6f0356c53e7ea2902dbda178d1b33c57fe06c41c | 6f0356c53e7ea2902dbda178d1b33c57fe06c41c | YES | C01: deps `base,bus,web`, `auto_install` |
| 2 | `controllers/main.py` | df0db6c76ab9e4599219761e27027f6ca5695fc7 | df0db6c76ab9e4599219761e27027f6ca5695fc7 | YES | C02, C04, C05, C06 (HEAD 10 s), C08 (no timeout, SUPERUSER), C10, C11, C12, C13, C20 |
| 3 | `tools.py` | 8683de75fbf5e6e7c1ea82feb82e7f9ae73187cc | 8683de75fbf5e6e7c1ea82feb82e7f9ae73187cc | YES | C09: `http://vimeo.com/api/oembed.json`, thumbnail GET from response |
| 4 | `models/ir_qweb_fields.py` | b080a1cca907a6fde688b61b1979e54bf55eac8e | b080a1cca907a6fde688b61b1979e54bf55eac8e | YES | C07: remote GET, timeout constant 2.5 |
| 5 | `models/ir_ui_view.py` | b16975fbfaddcd8e6448039ab97d20d7fe8e064c | b16975fbfaddcd8e6448039ab97d20d7fe8e064c | YES | C03: `env['website']`, `website.*` footer keys |

## 10. Provenance
- Input: Lane A packet above (sha256 recorded); HROU spot-check reused for X-HEDT-03. No Lane B, no runtime.
- Spot-check fetches: anchor commit via raw.githubusercontent; files held in scratchpad only.
- Topic lens: frozen bank W1-B07 (bank hash verified against freeze manifest); gate DELTA-RECHECK noted; no QID answered.

## 11. Limitations
- Source presence != runtime reachability; no runtime proof; no Formal Coverage; no percentages.
- SSRF exposure (C05) remains UNRESOLVED until mail link-preview tool is read; kept as CRQ, not a finding of exploitability.
- MED claims rest on Lane A without A1 re-read. JS/client-side behaviour not studied.
- Clean room: neutral WHAT/WHY/RISK only; identifiers are evidence pointers, not design recommendations.
