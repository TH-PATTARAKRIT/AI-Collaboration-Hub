# G01 PLATFORM_BASE — Module `http_routing` — Lane A Pass-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | SMEsPlus LANE A (blind source/static evidence) |
| Slot | T5 (refill) |
| Governed group | G01 PLATFORM_BASE |
| Module | `http_routing` (roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` 19.0, commit `8d05257d83f9128953f580a066db67c48fcdb96f` (raw.githubusercontent fetch) |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (all manifest-declared Python and data files read; base-layer behaviour it overrides is out of scope — see Gaps) |
| Handoff target | RED TEAM A1 only. No Lane B material consulted. No GMVQ QID answered. |

## 1. Evidence Pointer Table

| Path (addons/http_routing/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | 9321b4082f847cd079780946e3fc1335059211fb | Identity, deps, data list, post-init hook |
| `__init__.py` | ad6393eeedf4aa6485f38cdd5ea0230cd89e205c | Import graph; post-init hook resets request frontend flags |
| `controllers/__init__.py` | 5d4b25db9c00182450a7328f8348aa3ad4ba706e | Controller import |
| `controllers/main.py` | a0c0d3597f0f1a9209339f58aad2b03893ec374d | Frontend translations route; logout route override |
| `models/__init__.py` | 21691caed740bcac504e186a4240af3464cba131 | Model import list |
| `models/ir_http.py` | d508ceb82321dbda60e7fcdc1554b74eb17d3c49 | Slug/unslug, record converter, lang routing, redirects, error pages, rewrite cache |
| `models/ir_qweb.py` | 39ffe9272cdc70767cf698b9b010d36d18678a8c | Injects slug/URL helpers into template context; frontend-flag sanity warning |
| `models/res_lang.py` | e82c025e55338726be8b85b289267ce31547a907 | Frontend-language list accessor |
| `views/http_routing_template.xml` | 5c5e7d00a6f2c38b7973de87f57e564a4e336250 | Error page templates (generic, 4xx, 400, 403, 404, 415, 422, 500, debug block) |
| `views/res_lang_views.xml` | cd9eea30edaad8377b6f7f72e11e09ba0092ff6c | Adds language URL-code to language form/list views |

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
1. Technical, hidden-category module ("Web Routing"); single declared dependency `web`; LGPL-3. Purpose statement: advanced routing options kept out of base/web. [`__manifest__.py`]
2. Data files: two view files only (error templates, language view extension). No security file, no ACL CSV, no cron, no demo. [`__manifest__.py`]
3. Post-init hook sets the current request (if any) to non-frontend / non-multilang, so installation-time rendering does not assume frontend context. [`__init__.py` `_post_init_hook`]
4. `ir_qweb.py` carries an explanatory warning text stating it is a dependency "of both portal and website" and that every request is expected to pass through its match step. [`models/ir_qweb.py`]

### 2.2 Data (models, fields, constraints)
5. No new persistent model; all three Python models extend existing abstract/base models (`ir.http`, `ir.qweb`, `res.lang`). [`models/*`]
6. The language "URL code" field shown in views is not defined in this module; the view extension only exposes it (optional on form, technical-group-only on list). Field definition lives upstream (base). [`views/res_lang_views.xml`]
7. No SQL constraints, no Python constraints declared.

### 2.3 Business rules / exceptions
8. **Slug generation:** a record URL segment is "slugified display name + hyphen + numeric id"; empty slug name falls back to id only; a missing id raises a value error. [`ir_http.py` `_slug`]
9. **Unslug:** a pattern accepts optional slug prefix and a (possibly negative) numeric id terminated by end/slash/hash/query; returns (slug, id) or (None, None). A URL helper replaces only the last path segment with the bare id. [`ir_http.py` `_UNSLUG_RE`, `_unslug`, `_unslug_url`]
10. **Record converter:** route segments typed as model records use the unslug pattern; negative ids that do not exist are retried as absolute value (documented "limited support"). Original raw value is kept in context. [`ir_http.py` `ModelConverter`]
11. **Canonical slug redirect (SEO):** on frontend multilang GET/HEAD, if the rebuilt path from route args differs from the requested path, a 301 redirect to the canonical path (with lang prefix when non-default) is issued. RISK: record display-name changes alter canonical URLs. [`ir_http.py` `_pre_dispatch`]
12. **Language-prefixed routing** — nine documented cases in the match step: non-frontend passthrough; default lang w/o prefix; bot user-agents served without redirect; no redirect on POST; redirect to insert lang prefix; redirect removing default-lang prefix; 301 from lang alias to preferred URL code; 301 removing trailing slash on lang homepage; internal reroute stripping a valid lang prefix. Unmatched case logs a warning and continues as-is. [`ir_http.py` `_match`]
13. **Requested-lang precedence:** URL segment → `frontend_lang` cookie → context lang → default lang; each resolved via "nearest lang" (exact, then same language prefix). Language resolution temporarily runs under the public-user auth method, then restores the real env. [`ir_http.py` `_match`, `get_nearest_lang`]
14. **Default language** is taken from the stored default partner-language setting (read with elevated rights), else first active language. [`ir_http.py` `_get_default_lang`]
15. **Double-slash normalization:** redirect-capable requests containing `//` receive 301 to a single-slash path (local redirect). [`ir_http.py` `_match`]
16. **Localized / canonical URL builder:** re-matches a URL, re-contexts record args to the target language, rebuilds via router; on not-found/access/missing errors falls back to quoted raw path. Canonical-domain mode drops the query string. [`ir_http.py` `_url_localized`]
17. **Multilang URL test:** `/static/` and `/web/` paths are never multilang; otherwise matched endpoint must be `website`-flagged and multilang (default true for http type); unmatched paths are treated as multilang; any exception → false with warning. [`ir_http.py` `_is_multilang_url`]
18. **Language in relative links:** relative URLs get the lang code inserted/removed/replaced only when more than one frontend language exists or a lang is forced; absolute URLs untouched. [`ir_http.py` `_url_lang`, `_url_for`]
19. **Error handling (frontend only):** backend requests and non-HTTP-exception responses pass through. Frontend: ensures a (public) user, rolls back the transaction, maps user errors to their HTTP status and HTTP exceptions to their code; a template-origin 404 with a nested path is reclassified to 500. For 404/403 a fallback server hook is tried first; otherwise a per-code error template renders, 4xx falls back to generic 4xx template, render failure yields status 418 with a generic error template. [`ir_http.py` `_get_exception_code_values`, `_handle_error`, `_get_error_html`]
20. **Error-page information exposure:** templates show error message; traceback / QWeb expression / exception text are shown only when `editable` or `debug` is truthy. The 500 template is deliberately asset-free because the cursor may be broken. RISK: debug-mode leakage of tracebacks to the requester depends on how `debug` is granted upstream. [`views/http_routing_template.xml`]
21. **404 page** references an illustration via the html_editor shape route and a `/contactus` link. [`views/http_routing_template.xml` `404`]

### 2.4 Security
22. No groups, no ACLs, no record rules defined by this module.
23. Routes: `/website/translations` — `auth=public`, readonly, sitemap off; it reads installed-module list with elevated rights and forwards caller-supplied extra module names to the web translations handler. `/web/session/logout` override — flagged website, non-multilang, default redirect `/odoo`. [`controllers/main.py`]
24. Elevated reads: default-lang setting and module list read via sudo. [`ir_http.py`]
25. Redirects built in the match step are local/path-based (`local=True` on the slash-merge redirect; others use path concatenation). Open-redirect surface not evident from this file; logout `redirect` parameter handling is delegated to the parent controller (not read — gap). [`ir_http.py`, `controllers/main.py`]
26. Rewrite lookup results are ORM-cached under a dedicated `routing.rewrites` cache keyed by path and query. [`ir_http.py` `url_rewrite`]
27. Reroute limit constant = 10. [`ir_http.py` `rerouting_limit`]

### 2.5 UI surfaces
28. Routes: `/website/translations`, `/web/session/logout` (override). Templates: 9 error-related QWeb templates. Views: 2 inherited `res.lang` views. No JS/asset bundles declared.

### 2.6 Jobs / config
29. No cron, no config parameters declared. Behaviour switches: `frontend_lang` cookie (set on redirects and on frontend dispatch), bot detection, multilang route flags, debug/editable flags.

## 3. Cross-module edges
- **web** (declared): extends web Home/Session/WebClient controllers; error templates call `web.frontend_layout`.
- **base** (implicit via web): overrides base `ir.http` (match, pre-dispatch, handle-error, converters), `ir.qweb`, `res.lang`; uses `ir.default`, `ir.module.module`.
- **html_editor** (undeclared, soft): 404 template embeds an image served by html_editor's shape route; html_editor in turn consumes `_slug`/`_unslug`.
- **website / portal** (downstream): route flags `website=`/`multilang=`, `_serve_fallback`, `is_a_bot`, `_get_translation_frontend_modules_*` are extension points consumed/overridden by downstream modules.

## 4. Evidence gaps / contradictions
- G1: `_serve_fallback`, `is_a_bot`, `_auth_method_public`, `_handle_debug`, `redirect_query`, parent logout redirect sanitation, and `url_code` field definition live in base/web — not read (outside module scope).
- G2: `/contactus` link and html_editor shape image in the 404 template are unresolved when website/html_editor absent — contradiction between declared deps (`web` only) and template references. Runtime effect unknown.
- G3: Whether caller-supplied `mods` on the public translations route is filtered is determined by the web handler — not read.
- G4: Test files not reviewed.

## 5. Limitations
Source presence ≠ runtime reachability. No runtime proof, no Formal Coverage. Clean-room: descriptions are neutral WHAT/WHY/RISK abstractions; identifiers are pointers only.
