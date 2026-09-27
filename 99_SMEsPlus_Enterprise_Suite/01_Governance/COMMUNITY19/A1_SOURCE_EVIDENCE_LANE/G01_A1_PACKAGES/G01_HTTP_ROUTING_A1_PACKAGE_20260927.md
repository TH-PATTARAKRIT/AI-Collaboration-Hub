# G01 PLATFORM_BASE — Module `http_routing` — RED TEAM A1 Package

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Governed group / module | G01 PLATFORM_BASE / `http_routing` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_HTTP_ROUTING_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `9dfcb95f2521ec078ee425e4755054844d54eb3e4233b8d83c04b03f9bfa612c` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Freeze (topic lens only) | W1-B08, freeze_hash `b5402bab2164ac8314ed4e470e747fb846c1cc63500db688209131be1dda46a7`; bank `G01_HTTP_ROUTING_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `b5cecfd6…11844c0` (matches FREEZE_W1-B08.json) |
| Gate status | **DELTA-RECHECK — non-canonical freeze basis, reproducible** (QUESTION_GATE_G01_FREEZE_REPLAY_20260927). A1 proceeds as source research; canonical re-freeze pending (GMVQ/OVQDT). |
| Date | 2026-09-27 |
| Lane B dependency | None. A1 did not wait for, view, or use Lane B evidence. |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Bank used as a topic lens only (routing, language resolution, redirects, error exposure, public routes, dependency integrity). No QID answered; bank not edited. Paths relative to `addons/http_routing/` at the anchor.

## 1. Claims

| Claim ID | Claim (neutral WHAT / WHY / RISK) | Evidence (path @ blob) | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-HROU-C01 | WHAT: hidden technical routing module declaring a single dependency (`web`) and a post-init hook; ships two view files, no ACL/security/cron/demo data. | `__manifest__.py` @ 9321b408 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HROU-C02 | WHAT: post-init hook clears frontend/multilang flags on the current request. WHY: prevents install-time rendering from assuming a frontend context. | `__init__.py` @ ad6393ee (Lane A only) | MED | SOURCE-STATIC |
| A1-G01-HROU-C03 | WHAT: no persistent model is created; the module extends the platform request dispatcher, template engine and language model. RISK: behaviour is global to every HTTP request, not opt-in per route. | `models/*` (Lane A); `models/ir_qweb.py` @ 39ffe927 warning text | MED | SOURCE-STATIC |
| A1-G01-HROU-C04 | WHAT: record URL segment = slugified display name + id; empty name falls back to id; missing id raises error. Slug/unslug helpers are defined here and consumed by other modules. | `models/ir_http.py` @ d508ceb8 (spot-checked: `_slug`, `_unslug`, `_unslug_url` defined) | HIGH | SOURCE-STATIC |
| A1-G01-HROU-C05 | WHAT: record converter accepts negative ids and retries absolute value when the negative record does not exist. RISK: two URL forms resolve to one record; "limited support" is self-declared. | `models/ir_http.py` @ d508ceb8 (Lane A) | MED | SOURCE-STATIC |
| A1-G01-HROU-C06 | WHAT: on frontend multilang GET/HEAD, a non-canonical record path is 301-redirected to the canonical slug path. RISK: display-name edits change canonical URLs (link churn/SEO). | `models/ir_http.py` @ d508ceb8 (301 redirects spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HROU-C07 | WHAT: language resolution precedence is URL segment, then language cookie, then context language, then default; each via nearest-language match. Resolution runs temporarily under the public-user auth method. | `models/ir_http.py` @ d508ceb8 (Lane A) | MED | SOURCE-STATIC |
| A1-G01-HROU-C08 | WHAT: default language read from stored partner-language default with elevated rights, else first active language. | `models/ir_http.py` @ d508ceb8 (spot-checked: elevated read of default setting) | HIGH | SOURCE-STATIC |
| A1-G01-HROU-C09 | WHAT: nine language-prefix routing cases; bots served without redirect; POST never redirected; unmatched case logs and continues. | `models/ir_http.py` @ d508ceb8 (Lane A) | MED | SOURCE-STATIC |
| A1-G01-HROU-C10 | WHAT: double-slash paths receive a 301 local-only redirect; other language redirects are path-concatenated via a query-preserving redirect helper. WHY: normalisation; RISK: open-redirect safety of the helper lives in base (unread). | `models/ir_http.py` @ d508ceb8 (spot-checked: `local=True` on one redirect; others use `redirect_query`) | HIGH | SOURCE-STATIC |
| A1-G01-HROU-C11 | WHAT: `/static/` and `/web/` paths are never multilang; unmatched paths default to multilang; exceptions yield non-multilang with warning. | `models/ir_http.py` @ d508ceb8 (Lane A) | MED | SOURCE-STATIC |
| A1-G01-HROU-C12 | WHAT: frontend error handling rolls back the transaction, maps user/HTTP errors to status, tries a server fallback for 404/403, renders per-code templates, and on render failure returns status 418 with a generic template. | `models/ir_http.py` @ d508ceb8 (spot-checked: `_handle_error`, `_serve_fallback`, 418) | HIGH | SOURCE-STATIC |
| A1-G01-HROU-C13 | WHAT: error templates include a debug block (traceback / expression / exception text) whenever `editable` or `debug` is truthy. RISK: exposure to anonymous requesters depends on how those flags are granted upstream. | `views/http_routing_template.xml` @ 5c5e7d00 (spot-checked: 7 `editable or debug` gates) | HIGH | SOURCE-STATIC |
| A1-G01-HROU-C14 | WHAT: 404 template embeds an image served by the `html_editor` shape route and links to `/contactus`; neither module providing them is declared. | `views/http_routing_template.xml` @ 5c5e7d00 + `__manifest__.py` @ 9321b408 (both spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HROU-C15 | WHAT: public, readonly `/website/translations` route reads the frontend module list with elevated rights and appends caller-supplied comma-separated module names before delegating to the web translation handler. RISK: any filtering of caller names is in web (unread). | `controllers/main.py` @ a0c0d359 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HROU-C16 | WHAT: logout route is overridden (website-flagged, non-multilang) with default redirect `/odoo`; redirect parameter passed unchanged to parent. RISK: redirect sanitation is parent-owned (unread). | `controllers/main.py` @ a0c0d359 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-HROU-C17 | WHAT: URL rewrite lookups are ORM-cached per path+query; reroute limit is 10. | `models/ir_http.py` @ d508ceb8 (spot-checked: `rerouting_limit = 10`) | HIGH | SOURCE-STATIC |
| A1-G01-HROU-C18 | WHAT: no groups, ACLs or record rules; no company dimension observed in routing or language resolution in the Lane A packet. RISK: per-company language/URL policy is not modelled at this layer. | Lane A §2.4 items 22–24 | MED | SOURCE-STATIC |

## 2. Business rules
- BR1 Record URLs carry a human-readable name plus a stable numeric id; the id alone is authoritative (C04, C06).
- BR2 Frontend URLs are language-prefixed except for the default language; canonical form is enforced via 301 on safe methods only (C06, C09).
- BR3 Language resolution order is fixed: URL > cookie > context > default (C07, C08).
- BR4 Technical paths (`/static/`, `/web/`) are excluded from language handling (C11).
- BR5 Error details are shown only in editable/debug rendering (C13).

## 3. States / transitions
- Request: backend passthrough | frontend → lang resolved → (redirect 301 | reroute internally | serve) (C09, C10).
- Error: exception → rollback → fallback (404/403) → code template → generic 4xx → 418 render-failure (C12).
- Canonical URL: requested path → rebuilt path; mismatch → 301 (C06).

## 4. Exceptions / failure modes
- Missing id in slug build → value error (C04).
- Unmatched routing case → warning, request served as-is (C09).
- Localized URL rebuild failure (not-found/access/missing) → falls back to quoted raw path (Lane A item 16).
- Template-origin 404 with nested path → reclassified as 500 (Lane A item 19).
- Error-template render failure → 418 (C12).

## 5. Cross-module handoffs
- `web` (declared): controller bases (Home, Session, WebClient); frontend layout.
- `base` (implicit): request dispatcher, template engine, language model, defaults, module registry.
- `html_editor` (undeclared): 404 image route; reverse edge — html_editor consumes slug/unslug from here (see HEDT package).
- `website` / `portal` (downstream): route flags, fallback serving, bot detection, translation module list are extension points.

## 6. Evidence gaps
- EG1 Base/web internals: fallback serving, bot detection, public auth method, debug-flag grant, `redirect_query`, parent logout sanitation, language URL-code field (Lane A G1).
- EG2 Web translation handler filtering of caller-supplied module names (Lane A G3).
- EG3 Runtime effect of 404 page when html_editor / website are absent (Lane A G2).
- EG4 Test files not reviewed (Lane A G4).

## 7. CRQ candidates
| CRQ | Question | Why |
|---|---|---|
| CRQ-HROU-01 | Can an anonymous requester obtain `debug`/`editable` truthy and receive traceback content on error pages? | C13, EG1 |
| CRQ-HROU-02 | Does the logout `redirect` parameter permit off-site redirects? | C16, EG1 |
| CRQ-HROU-03 | Does the public translations route filter caller module names (enumeration / payload amplification)? | C15, EG2 |
| CRQ-HROU-04 | What renders for the 404 page when html_editor and/or `/contactus` provider are not installed? | C14, EG3 |
| CRQ-HROU-05 | Is the path-concatenated language redirect safe against scheme-relative/host injection? | C10, EG1 |
| CRQ-HROU-06 | Should language/URL policy be company-scoped in a multi-tenant target? | C18 |

## 8. Contradictions
| ID | Contradiction | Status |
|---|---|---|
| X-HROU-01 | Declared deps = `web` only, but 404 template references html_editor shape route (`/html_editor/shape/http_routing/404.svg`) and `/contactus` (website-provided). | **CONFIRMED-FROM-SOURCE** (spot-checks 1, 2) |
| X-HROU-02 | Template engine warning claims every request passes through the match step, yet backend requests pass through untouched in error handling. | CANDIDATE (not a conflict unless runtime shows otherwise; Lane A only) |

## 9. Spot-check log
Re-fetched from `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/http_routing/<path>`; `git hash-object` computed in session scratchpad (no repo git operations).

| # | Path | Recorded blob | Computed blob | Match | Claim(s) verified in content |
|---|---|---|---|---|---|
| 1 | `__manifest__.py` | 9321b4082f847cd079780946e3fc1335059211fb | 9321b4082f847cd079780946e3fc1335059211fb | YES | C01, X-HROU-01: `depends: ['web']`, post-init hook |
| 2 | `views/http_routing_template.xml` | 5c5e7d00a6f2c38b7973de87f57e564a4e336250 | 5c5e7d00a6f2c38b7973de87f57e564a4e336250 | YES | C13 (debug gates), C14 (html_editor shape src, `/contactus` href) |
| 3 | `controllers/main.py` | a0c0d3597f0f1a9209339f58aad2b03893ec374d | a0c0d3597f0f1a9209339f58aad2b03893ec374d | YES | C15 (public, sudo, `mods` appended), C16 (default `/odoo`, passthrough) |
| 4 | `models/ir_http.py` | d508ceb82321dbda60e7fcdc1554b74eb17d3c49 | d508ceb82321dbda60e7fcdc1554b74eb17d3c49 | YES | C04, C06, C08, C10, C12, C17 |

## 10. Provenance
- Input: Lane A packet above (sha256 recorded); no other lane packets, no Lane B, no runtime.
- Spot-check fetches: anchor commit via raw.githubusercontent; files held in scratchpad only.
- Topic lens: frozen bank W1-B08 (bank hash verified against freeze manifest); gate DELTA-RECHECK noted; no QID answered.

## 11. Limitations
- Source presence != runtime reachability; nothing here is runtime proof. No Formal Coverage; no percentages.
- MED-confidence claims rest on the Lane A packet without A1 re-read of the specific function.
- Clean room: neutral WHAT/WHY/RISK only; identifiers are evidence pointers, not design recommendations.
