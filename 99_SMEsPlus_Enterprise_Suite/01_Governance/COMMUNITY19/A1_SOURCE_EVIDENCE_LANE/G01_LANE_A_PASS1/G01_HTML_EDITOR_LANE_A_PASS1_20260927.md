# G01 PLATFORM_BASE — Module `html_editor` — Lane A Pass-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | SMEsPlus LANE A (blind source/static evidence) |
| Slot | T5 (refill) |
| Governed group | G01 PLATFORM_BASE |
| Module | `html_editor` (roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` 19.0, commit `8d05257d83f9128953f580a066db67c48fcdb96f` (raw.githubusercontent fetch) |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (server-side Python + security data fully read; JS layer counted only, per brief) |
| Handoff target | RED TEAM A1 only. No Lane B material consulted. No GMVQ QID answered. |

## 1. Evidence Pointer Table

| Path (addons/html_editor/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | 6f0356c53e7ea2902dbda178d1b33c57fe06c41c | Identity, deps, data, asset bundles, auto-install |
| `__init__.py` | f7209b17100218a42c80c8e984c08597d630b188 | Import graph |
| `controllers/__init__.py` | 80ee4da1c5ecc388c9dd3e3e0b56f60a77471e66 | Controller import |
| `controllers/main.py` | df0db6c76ab9e4599219761e27027f6ca5695fc7 | Media/attachment, image, shape, AI text, collaboration, link preview, media library routes |
| `models/__init__.py` | 385d7a5a523322f8efc14a13610e0b327c3ea89b | Model import list |
| `models/ir_attachment.py` | 49820e8d353bad5688f023e1e03513a3da9ed50f | Supported image types; computed URL/size fields; original-link; media-dialog bypass hook |
| `models/ir_http.py` | 77f00f5f3b2f160c81ab513435707901cada86bf | Query-string editor context flags; frontend translation module |
| `models/ir_qweb_fields.py` | b080a1cca907a6fde688b61b1979e54bf55eac8e | Editor-branding attributes, sanitize markers, HTML→value converters, image fetch |
| `models/ir_ui_view.py` | b16975fbfaddcd8e6448039ab97d20d7fe8e064c | View section save, embedded field save, custom snippet save/rename/delete |
| `models/ir_websocket.py` | 98d4d53e9730cb5334993752fb93b89bcff9e493 | Collaboration bus channel authorization |
| `models/models.py` | fbdbb0565a9a01b3c867dc9c8934ce379a9883af | Exposes `sanitize` / `sanitize_tags` as view field attributes |
| `models/test_models.py` | d72b4ef173c28bcf2f1d6db16ae5df59ebb61600 | Two converter test models |
| `models/html_field_history_mixin.py` | 6ad306f86b11767957b90dbd789aa7bb46d45a24 | HTML field revision history mixin |
| `models/diff_utils.py` | fe6bb818bbe612c77aeaac9d3688527d044493ba | Patch/diff/compare utilities used by history mixin |
| `tools.py` | 8683de75fbf5e6e7c1ea82feb82e7f9ae73187cc | Video URL parsing/embedding/thumbnail; collaborative history divergence check |
| `security/ir.model.access.csv` | 48079732ad690f12adf58061fbb4f614b1833e97 | ACLs for test models |

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
1. "HTML Editor": extensible editor component and plugin system; hidden category; `auto_install=True`; LGPL-3. Declared deps: `base`, `bus`, `web`. [`__manifest__.py`]
2. Data: only `security/ir.model.access.csv`. [`__manifest__.py`]
3. Assets: 18 bundle keys with 65 entries (globs/includes/removes) spanning backend, frontend, readonly viewer, media dialog, history diff, image cropper, report, dark-mode, tests, code highlighting. Third-party libs referenced: DOMPurify, diff2html, cropperjs, webgl-image-filter, vkbeautify, prismjs. File counts behind globs not enumerated (gap G6). [`__manifest__.py`]

### 2.2 Data (models, fields, constraints)
4. `ir.attachment` extended: computed local URL, computed image source (only for supported image MIME types; remote URL attachments routed via a redirect path), computed width/height, stored self-link to "original (unoptimized) attachment" (indexed). [`models/ir_attachment.py`]
5. Supported image MIME set: gif, jpe, jpeg, jpg, png, svg+xml, webp. [`models/ir_attachment.py`]
6. New abstract mixin `html.field.history.mixin`: JSON revision store (readonly, not prefetched) + computed metadata; history size cap 300 revisions per field; each revision records patch, incrementing revision id, timestamp, user id and user name. [`html_field_history_mixin.py`]
7. Constraint: writing a versioned field that is not declared sanitized raises a validation error; history cannot be set directly on create/write (stripped). Diff computed after write so patches reflect sanitized content. Restore/compare/unified-diff accessors per revision. [`html_field_history_mixin.py`]
8. Two concrete test models (converter test + sub) exist in production code path. [`models/test_models.py`]

### 2.3 Business rules / exceptions
9. **Field-level sanitize signalling:** in editable rendering, sanitized HTML fields are tagged with the sanitize mode (attributes-only / form-sanitized / allow-form). If the field's sanitize is overridable and the user holds the sanitize-override group, no marker is added; if the user lacks it and current content would fail sanitization (saved earlier by a privileged user), the field is marked edit-prevented. [`ir_qweb_fields.py` `IrQwebFieldHtml.attributes`]
10. `sanitize` and `sanitize_tags` are exposed as field attributes to client views. [`models/models.py`]
11. **Server-side sanitization itself** is not implemented here; it is inherited from the core HTML field (gap G1).
12. **Image upload (base64):** when flagged as image, MIME is sniffed from bytes; unsupported → error payload; name auto-generated when missing; image re-processed with requested size/quality and resolution verification. Non-image data accepted without type check at this layer. [`controllers/main.py` `add_data`]
13. **Attachment creation rules:** `.bmp` suffix stripped; attachments bound to views are public with no res_id; others bound to given model/id; URL attachments get a HEAD probe (10s timeout) to set MIME if supported image. Dedup by checksum/URL before creating. [`controllers/main.py` `_attachment_create`, `get_existing_attachment`]
14. **Image modification:** creates a modified copy linked to its original; checks read on source record and write on target record; copy done with elevated rights; MIME forced back by superuser if downgraded to text/plain; optional resized/format variants (webp/jpeg) created as child attachments; static-path URLs cleared, other URLs uniquified with id; non-public result returns tokenized URL. [`controllers/main.py` `modify_image`]
15. **Attachment removal:** refused (returned as blockers) when any view arch references the attachment URL; otherwise unlinked. [`controllers/main.py` `remove`]
16. **Shape/illustration SVG:** colour parameters accepted only as hex/rgb(a) or theme colour tokens resolved from the frontend CSS bundle; otherwise bad request. Flip and animation-speed options rewrite the SVG. Illustration shapes served only from public binary attachments whose URL matches the request path; module shapes read from module static dir with `.svg`-only file filter. [`controllers/main.py` `shape`, `_update_svg_colors`, `_get_shape_svg`]
17. **Image-in-shape:** embeds a record's image (base64) inside a module SVG; URL-type streams redirect. [`controllers/main.py` `image_shape`]
18. **Video embeds:** platform whitelisting by regex (YouTube, Vimeo, Dailymotion, Instagram, Facebook); unmatched → error; builds embed URL with player options; thumbnail fetch from platform hosts (10s timeouts). [`tools.py`]
19. **Collaborative edit conflict:** incoming HTML carrying a history-step marker is compared with stored marker; if stored last step is not in incoming steps → validation error ("already saved with different history"); bus notification emitted on each write; only the latest step id is kept. Skipped during module install. [`tools.py` `handle_history_divergence`]
20. **View editing:** saving a view section writes embedded field values back via typed converters (invalid → validation error), splits `oe_structure` blocks into extension views, marks the view no-update when changed, copies translations; hard-coded patch for specific footer views. Custom snippets: saved as new QWeb views with unique key, cleaned root attributes, and an addition view injecting the snippet into a snippets template; rename/delete helpers. [`models/ir_ui_view.py`]
21. **Converters from HTML:** many2one, date/datetime (format + timezone), selection (label lookup, error if unknown), duration, monetary, text, image. Image converter resolves `/web/image` URLs to stored binaries, `/<module>/static/` to local files, otherwise fetches remotely (2.5s timeout) and re-encodes via image library. [`ir_qweb_fields.py`]
22. **Link preview:** external preview returns OpenGraph metadata with description stripped to text; internal preview parses backend URL (model or action path + numeric id), resolves action with elevated rights, then reads description / link-preview name / display name under the user's rights; errors returned as messages. [`controllers/main.py`]

### 2.4 Security
23. ACL: only the two test models, full CRUD for system group. No record rules, no groups defined. [`security/ir.model.access.csv`]
24. Route auth levels — `public`: shape, image_shape, **link_preview_external**; `user`: all other routes. Several routes flagged `website=True`. [`controllers/main.py`]
25. **SSRF-like outbound fetch risks (source-visible):** (a) public link-preview route fetches an arbitrary caller URL (delegated to mail tool — gap G2); (b) URL attachment creation issues HEAD to arbitrary user URL; (c) image converter GETs arbitrary `src` URLs on save; (d) media-library download iterates remote-returned URLs without timeout; (e) Vimeo oEmbed call over plain HTTP. No host allow/deny list visible in this module.
26. **Elevated operations:** media-dialog bypass hook (default false; overridable) enables sudo create + token generation; `modify_image` copies via sudo and writes MIME as superuser; media-library attachments created as superuser (comment: SVGs from whitelisted origin); illustration lookup and action resolution via sudo; config params read via sudo; `_set_noupdate` via sudo.
27. **Upload controls:** type allow-list enforced only for image-flagged uploads and modify MIME; size/resolution guarded by image processing verification; no explicit byte-size cap in this module (gap G3).
28. **Collaboration channels:** subscription to an editor channel requires non-public user, existing record, read+write access on record and field; broadcast route performs the same checks. [`ir_websocket.py`, `bus_broadcast`]
29. `t-install` directive renders module-install snippet only for system group. Query-string flags `editable`/`edit_translations`/`translatable` are injected into context on any request (effect gated elsewhere — gap G4). [`ir_qweb_fields.py`, `models/ir_http.py`]
30. Internal link preview catches all exceptions and returns raw exception text to client. [`controllers/main.py`]

### 2.5 UI surfaces (route names only)
31. `/html_editor/attachment/remove`; `…/get_image_info`; `…/video_url/data`; `…/attachment/add_data`; `…/attachment/add_url`; `…/modify_image/<attachment>`; `…/save_library_media`; `…/shape/<module>/<path>`; `…/image_shape/<key>/<module>/<path>`; `…/generate_text`; `…/get_ice_servers`; `…/bus_broadcast`; `/html_editor/link_preview_external`; `/html_editor/link_preview_internal`; `/html_editor/media_library_search`. Most have legacy `/web_editor/…` aliases (11 aliased). 15 distinct handlers.
32. JS: 18 asset bundle keys / 65 manifest entries (counts only).

### 2.6 Jobs / config
33. No cron. Config parameters read: `html_editor.media_library_endpoint` (default external media API), `html_editor.olg_api_endpoint` (default external AI text endpoint), `database.uuid` (sent to both external services). AI text call via IAP JSON-RPC, 30s timeout, maps quota/prompt-length statuses to user errors.

## 3. Cross-module edges
- **base / web / bus** (declared): `ir.attachment`, `ir.ui.view`, `ir.qweb`, `ir.http`, `ir.binary`, `ir.websocket`, `bus.bus`.
- **http_routing** (undeclared): uses `_slug`/`_unslug` via `ir.http`; http_routing 404 page consumes the shape route.
- **mail** (undeclared): imports link-preview tool; calls `mail.ice.server`.
- **iap** (undeclared): imports IAP JSON-RPC tool.
- **website** (undeclared): `save_snippet` references the `website` model and website domain; view-save patches `website.*` footer keys.
- **html_builder**: legacy `web_editor` shape module name remapped to it.
- Downstream: history mixin and divergence helper are consumable by any model with versioned HTML fields.

## 4. Evidence gaps / contradictions
- G1: Actual HTML sanitizer (tags/attributes policy) is in core field/tools — not read.
- G2: Link-preview fetch safeguards (scheme/host/IP filtering, size limits) are in mail tools — not read; SSRF exposure of the public route therefore UNRESOLVED.
- G3: Upload size limits and `image_process` resolution cap live in core tools — not read.
- G4: Consumers of `editable`/`translatable` context flags not traced.
- G5: **Contradiction:** module-level imports of `mail` and `iap` tools plus `website` model reference versus declared deps `base, bus, web`. Runtime load behaviour unproven.
- G6: JS glob contents not enumerated (raw fetch cannot list directories).
- G7: Test models ship in production import path with system-only ACL. Tests not reviewed.

## 5. Limitations
Source presence ≠ runtime reachability. No runtime proof, no Formal Coverage. JS behaviour (client-side sanitization, DOMPurify usage) not studied per brief. Clean-room: neutral WHAT/WHY/RISK abstractions; identifiers are pointers only.
