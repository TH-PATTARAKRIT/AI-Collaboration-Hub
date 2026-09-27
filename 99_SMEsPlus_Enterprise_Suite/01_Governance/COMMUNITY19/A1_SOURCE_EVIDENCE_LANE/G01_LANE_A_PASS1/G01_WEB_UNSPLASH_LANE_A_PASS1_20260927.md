# G01 PLATFORM_BASE — `web_unsplash` — Lane A Pass-1 Source Evidence

| Field | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T2 (refill) |
| Group | G01 PLATFORM_BASE |
| Module | `web_unsplash` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/web_unsplash/`) |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |
| Question bank | None module-specific yet; no QIDs answered (evidence only) |

## 1. Evidence Pointer Table

| Path (under `addons/web_unsplash/`) | Git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | `32cfd99d9b25c7bb9b7a7e42fc5592b8abb21f78` | Identity, deps, data, assets, auto-install |
| `__init__.py` | `7d34c7c054abd3105d5bb41fe9674111e1c27c16` | Imports controllers + models |
| `controllers/__init__.py` | `7fc0cd7cb934f5bf6ce85580e1b55623ea0e6ee6` | Imports `main` |
| `controllers/main.py` | `00cf725f2366dbaf88fa5baeb1b729f5ba4a1962` | 4 JSON-RPC routes: search proxy, download->attachment, app-id read, key save |
| `models/__init__.py` | `1c72f271b8164155ee5580332fbf720b62f49abd` | Imports 3 model files |
| `models/ir_qweb_fields.py` | `378935726fbaed412399ec4ea70fa5bce758b2bc` | Image-field HTML->binary resolution for stored images |
| `models/res_config_settings.py` | `3136eaef7fe32bf679c23cb094ae66c33069dd57` | 2 settings fields backed by system parameters |
| `models/res_users.py` | `3d4d2d8885bab0ac00acc3ed6cd4ef92bf82eb92` | "Can manage settings" predicate |
| `views/res_config_settings_view.xml` | `0eeb25183ef895c8bde40eaf1fc2ac1fcc83724b` | Settings form inheritance (only manifest data file) |
| `tests/__init__.py` | `d059700a7b1ce50340c555f0c270b0cfa26d752a` | Imports one test file |
| `tests/test_unsplash.py` | `31b8a1afd22d7789445a613dcf56112322b447b6` | Access test for attachment route |
| `static/src/frontend/unsplash_beacon.js` | `189939d2190ab306a041fcee8d69e57d7216c84a` | Frontend view beacon (surface pointer only) |
| `static/src/unsplash_service.js` | `fb8e66fe6a7ca1f7d25adbbdf8c3e6238c08e947` | Client service calling routes (surface pointer only) |

Probed absence (404): `security/ir.model.access.csv` (not in manifest — absence).

## 2. Findings by Card Section

### 2.1 Manifest / deps / purpose
1. WHAT: Hidden-category, **auto-install** integration adding third-party stock-image search into the HTML editor's media dialog. Depends on `base_setup` and `html_editor`. One data file (settings view). (`__manifest__.py`)
2. WHAT: Assets: one public-website frontend script, media-dialog bundle (media dialog, credentials, error, service), unit tests. (`__manifest__.py`)

### 2.2 Data (models, fields, constraints)
3. WHAT: No new models/tables. Settings transient gains two Char fields (access key, application id) persisted as system config parameters. No constraints/format validation on either. (`models/res_config_settings.py`)
4. WHAT: Attachment records (existing model) are created per downloaded image, named from a fixed prefix + external image key + sanitized query + guessed extension, with a synthetic local URL path under a `/unsplash/` prefix. (`controllers/main.py` `save_unsplash_url`)

### 2.3 Business rules / exceptions
5. WHAT (search proxy): Route reads key + app id; if either missing returns `no_access` (non-managers) or `key_not_found` (managers). Otherwise forwards **all caller-supplied params** plus the server-held key to the external search endpoint and returns its JSON; non-OK status returns `no_access` or the status code depending on manager predicate. (`controllers/main.py` `fetch_unsplash_images`)
6. WHAT (download -> attachment): For each submitted item, the image URL must start with one of two fixed external image-host HTTPS prefixes (check bypassed in test mode); then fetched server-side, non-OK responses skipped, connection/timeout errors logged and skipped. Content passes through image processing with resolution verification, mimetype guessed from bytes. (`controllers/main.py`)
7. WHAT (target binding): Target model defaults to the view model; a record id is honoured only when a non-default model is supplied. Attachment creation is delegated to the editor module's attachment helper (which carries access checks — test confirms AccessError when targeting another user's record). (`controllers/main.py`; `tests/test_unsplash.py`)
8. WHAT (URL bypass): After creation, the attachment's URL is set via elevated rights, explicitly bypassing the normal "binary attachment may not also carry a URL" serving protection; an access token is generated and optional description stored. (`controllers/main.py`)
9. WHAT (download notification): API-terms "download ping" to the external API only if URL starts with the fixed API photos prefix (bypassed in tests); failures logged, never raised. (`controllers/main.py` `_notify_download`)
10. WHAT (HTML save-back): When an image field is saved from edited HTML and the image src path starts with the `/unsplash/` prefix, the binary is resolved from a matching attachment (URL match AND (same model+id OR public)) instead of default handling; returns empty if no match. (`models/ir_qweb_fields.py`)
11. RISK (outbound fetch / SSRF-like): Prefix allow-list is on the submitted URL string only; outbound HTTP client default redirect following is not disabled, so the effective fetched host after redirects is not re-validated. Test-mode flag disables the allow-list entirely. (`controllers/main.py`)
12. RISK (limits): No explicit timeout on any of the three outbound GETs, no response-size cap before loading into memory, no per-user rate limit, no cap on number of items per request; only the image-processing resolution check bounds decoded image size. The timeout exception handler therefore only fires on library-level timeouts. (`controllers/main.py`)
13. RISK (param passthrough): Search proxy forwards arbitrary caller params to the external API under the server's key (key param overwritten last). Query sanitization (alnum/hyphen/space, 1024 chars) applies only to the attachment-name path, not the search proxy. (`controllers/main.py`)
14. RISK: A disallowed image URL raises a generic exception (not caught by the narrow connection/timeout handlers) — aborts the whole request rather than skipping. (`controllers/main.py`)

### 2.4 Security
15. WHAT (routes/auth): `/web_unsplash/attachment/add` (user, POST), `/web_unsplash/fetch_images` (user), `/web_unsplash/get_app_id` (**public**, reads app id via sudo), `/web_unsplash/save_unsplash` (user, gated). (`controllers/main.py`)
16. WHAT (who sets keys): Key/app-id writes via the save route require the predicate: user in Access-Rights admin group OR in the website restricted-editor group (checked via sudo; website group referenced without dependency, per in-code comment); otherwise NotFound. Writes use sudo on system parameters. Settings-form path relies on standard settings access (owned by base_setup/core). (`controllers/main.py`, `models/res_users.py`)
17. RISK: App id is exposed to anonymous callers by design (needed by frontend beacon); access key is never returned by any route but is sent to the external API and read via sudo. Save route performs no value validation. (`controllers/main.py`, `static/src/frontend/unsplash_beacon.js`)
18. WHAT: No ACL CSV, no new groups, no record rules.

### 2.5 UI surfaces
19. WHAT: 4 route names (above). One settings-form inheritance replacing a placeholder block in base settings, visible only when the module toggle is set, with a documentation link. JS: 2 files verified by path (beacon, service); media-dialog/credentials/error directories are globbed — count unknown. (`views/res_config_settings_view.xml`, `__manifest__.py`)
20. WHAT: Frontend beacon calls the public app-id route and then pings an external views endpoint from the visitor's browser (client-side third-party request). (`static/src/frontend/unsplash_beacon.js`)

### 2.6 Jobs / config
21. WHAT: No cron. Config = 2 system parameters (access key, app id). Test-mode flag alters URL validation. (`models/res_config_settings.py`, `controllers/main.py`)

## 3. Cross-module Edges
- `html_editor`: attachment-creation helper reused (access checks inherited); media-dialog asset bundle extended.
- `base_setup`: settings view inherited; module toggle field referenced there.
- `website` (soft, no dependency): restricted-editor group referenced in manage predicate; website frontend asset bundle carries beacon.
- Core: `ir.attachment` (serving-protection bypass), `ir.config_parameter`, `ir.qweb.field.image`, `res.users`.
- External: Unsplash search API, image CDN hosts, download-notify endpoint, browser-side views endpoint.

## 4. Evidence Gaps / Contradictions
- GAP-1: Globbed JS directories (media_dialog, unsplash_credentials, unsplash_error) and `static/tests/**` not enumerable; JS surface count incomplete.
- GAP-2: `html_editor` attachment helper internals and the core attachment serving-protection check not read (other modules; access behaviour inferred from this module's test only).
- GAP-3: Presence/behaviour of the `module_web_unsplash` toggle and placeholder block lives in `base_setup` — not read here.
- CONTRADICTION-lite: code comment names "download_url" API requirement but the notify URL is caller-supplied (prefix-checked only).

## 5. Limitations
- Static source only at anchor commit; no runtime proof, no Formal Coverage, no percentages. Risks are source-visible hypotheses for A1/Proof.
- Clean-room: neutral WHAT/WHY/RISK abstractions; identifiers are pointers only.
