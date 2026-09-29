# Source Map (candidate) — `http_routing`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `http_routing` |
| Display name | Web Routing |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `3ab78e1de53f3711` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/http_routing/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`
- Direct dependents in 300-module list (3): `portal`, `survey`, `website`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `pos_self_order`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / Web Routing
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 2
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `res.lang`, `ir.http`, `ir.qweb`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.lang`, `ir.http`, `ir.qweb`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 36 of 36 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: http_routing
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Adds advanced web-address handling for public-facing pages: language prefix in the address, redirects to the preferred form, pretty "name-id" record links, link building for the current or another language, and branded error pages (http_routing/__manifest__.py:8-10; http_routing/models/ir_http.py:322-518,524-607; http_routing/views/http_routing_template.xml:3-239).
- Optional: not auto-installing; depends on web only; described in code as a dependency of portal and website (http_routing/__manifest__.py:17; http_routing/models/ir_qweb.py:22). Which modules depend on it: UNKNOWN — EVIDENCE INSUFFICIENT beyond that comment.
- Applies only to requests whose target page is flagged as public-facing ("website"); backend and non-flagged endpoints are left unchanged (http_routing/models/ir_http.py:371-378).
- Language-in-address handling applies only to pages flagged multi-language (default: normal page requests, not JSON calls) and never to static or web-client paths (http_routing/models/ir_http.py:222-253,373-376).
- Post-install hook resets the front-end flags on any current request (http_routing/__init__.py:9-12).

## B. Business objects, relationships, lifecycle
- No stored business objects. Adds "URL code" to the Language record, editable in the language form and shown in the list only to debug-feature users (http_routing/views/res_lang_views.xml:9,20). (TEST) creating a language with a URL code works (http_routing/tests/test_res_lang.py:9-14).
- "Front-end languages" = active languages by code (http_routing/models/res_lang.py:10-14).
- Language decision for a public request, in order: language in address, then front-end language cookie, then user context language, then default language (the configured default partner language, else the first active) (http_routing/models/ir_http.py:361-364,404-410,259-263).
- Nearest-language matching: exact code, else another installed variant of the same base language (fr_BE vs fr_FR) (http_routing/models/ir_http.py:301-316).
- Address rules (nine cases): default language shown without prefix; other languages get a prefix through redirect (not for POST or bots); alias prefixes are redirected permanently; homepage trailing slash removed; valid prefix stripped internally before routing (http_routing/models/ir_http.py:330-359,418-464).
- Pretty links: record links become "slug-id"; visits to a non-canonical form are redirected permanently, for SEO (http_routing/models/ir_http.py:54-87,494-512).
- Front-end language cookie is set on page loads (http_routing/models/ir_http.py:514-518).

## C. Validations, automation, security, credentials
- Double slashes in an address are merged via permanent redirect (http_routing/models/ir_http.py:391-396).
- Negative ids in pretty links are handled by assuming absolute value if not found (http_routing/models/ir_http.py:38-42).
- Errors on public pages: the system renders status-specific pages (400, 403, 404, 415, 422, 500, generic 4xx); on failure to render, an HTTP 418 fallback page is used (http_routing/views/http_routing_template.xml:62-193; http_routing/models/ir_http.py:559-607). Technical details (debug panel) appear only in edit or debug mode (http_routing/views/http_routing_template.xml:9,69,88,107). Transaction is rolled back before error rendering (http_routing/models/ir_http.py:587).
- Backend requests and plain responses do not get these pages (http_routing/models/ir_http.py:573-576).
- Public user is temporarily substituted while resolving the language before authentication (http_routing/models/ir_http.py:398-413). Business note: language resolution runs before user identification.
- `/website/translations` serves front-end translations to public visitors for web module plus module-declared extras; `/web/session/logout` is made multi-language-aware and redirects to the backend by default (http_routing/controllers/main.py:12-25). Redirect target parameter is passed through: open-redirect handling is done by the base logout: UNKNOWN — EVIDENCE INSUFFICIENT.
- Template-rendering side effect: when a front-end request is rendered, link helpers for localization are injected; a missing front-end flag on a request logs a warning (http_routing/models/ir_qweb.py:37-53).
- No groups, access rules, credentials or external services.

## D. Handoffs to other modules
- Website/portal (page flags, canonical domain, homepage, 404 handling with "serve fallback"): website module owns the fallback page logic (http_routing/models/ir_http.py:588-596; module presence UNKNOWN — EVIDENCE INSUFFICIENT).
- Base HTTP dispatch, authentication and language data: base/web (http_routing/models/ir_http.py:15-18; http_routing/controllers/main.py:5-7).
- Modules adding translatable front-end resources extend the extra-module list/domain hooks (http_routing/models/ir_http.py:277-299).

## E. Configuration/defaults that change outcomes
- Default language = default value of partner language, fallback first active language (http_routing/models/ir_http.py:259-263).
- Installed language count: with a single language the prefix is not added unless forced (http_routing/models/ir_http.py:167-168).
- Redirect limit constant 10 for rerouting (http_routing/models/ir_http.py:48).
- Route flags "website" and "multilang" on controllers decide behavior (http_routing/models/ir_http.py:250-253,375-376).

## F. Effective extension path
- Override hooks for extra front-end translation modules and domain, error-values and error-page selection, and default language (http_routing/models/ir_http.py:287-299,556-567,258-263). Website module extends these (module presence UNKNOWN — EVIDENCE INSUFFICIENT).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: bot detection details (case 3 condition line not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: template text of each error page beyond structure.
- UNKNOWN — EVIDENCE INSUFFICIENT: automated tests for routing rules (only language-creation test and a request mock helper found: http_routing/tests/common.py:14).

