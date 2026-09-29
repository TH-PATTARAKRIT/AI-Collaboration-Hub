# Source Map (candidate) — `api_doc`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `api_doc` |
| Display name | API Documentation |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `9a2be2c9bc19ca57` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/api_doc/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 5
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `ir.attachment`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.attachment`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 27 of 28 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: api_doc
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Developer-facing documentation page (`/doc`) generated live from the installed system: lists installed modules, models, fields and public methods, with a playground to try methods over HTTP and code examples in several languages (api_doc/__manifest__.py:6-12; api_doc/controllers/api_doc.py:31-46).
- Conditional: depends on web only and installs automatically (api_doc/__manifest__.py:14-15). Category is "Hidden" (api_doc/__manifest__.py:3).
- Two access styles: signed-in user routes and bearer-token routes for the index and per-model documents (api_doc/controllers/api_doc.py:48-53,165-170).
- Page carries a "deny framing" response header (api_doc/controllers/api_doc.py:45).

## B. Business objects, relationships, lifecycle
- One access group "Technical Documentation", created on install; the system superuser is a member and it is implied by the system administration group (api_doc/security/res_groups.xml:4-8).
- No business data models. Generated index documents are cached as private stored attachments named by registry sequence plus a hash of language and user groups (api_doc/controllers/api_doc.py:111-133).
- Cache lifecycle: an automatic vacuum removes cached index attachments whose registry sequence no longer matches the current one (api_doc/models/ir_attachment.py:11-23).
- Per-model document = model name, enriched field list, and method descriptions (signature, parameters, return, raises, docs, originating model and module) (api_doc/controllers/api_doc.py:170-240,242-301).

## C. Validations, automation, security, credentials
- Every entry point checks membership in the Technical Documentation group; otherwise an access error naming the group is returned (api_doc/controllers/api_doc.py:40-43,78-81,190-193). (TEST) A user without the group gets HTTP 403 with that message on `/doc`, `/doc/index.json`, and a model document (api_doc/tests/test_doc.py:36-46).
- The index only lists models the caller may read, and only fields the caller may read (api_doc/controllers/api_doc.py:139-162). Per-model view requires read access to the model (api_doc/controllers/api_doc.py:197-198).
- Only public methods are listed; deprecated methods, class/static methods and underscore-prefixed methods are excluded (api_doc/controllers/api_doc.py:313-318). (TEST) private, static, class and underscore methods are not public (api_doc/tests/test_doc.py:278-295).
- Unknown model name -> not found (api_doc/controllers/api_doc.py:194-195).
- Caching: client cache validation by ETag; server caches index as an attachment created with elevated rights (api_doc/controllers/api_doc.py:95-137). A client sending no-cache bypasses the stored copy (api_doc/controllers/api_doc.py:84-93).
- Bearer access uses a per-user API key (auth "bearer"); (TEST) a key with the remote-procedure scope and an expiry works for both routes (api_doc/tests/test_doc.py:60-63,98-101).
- (TEST) Model in database but missing from the registry does not break the index (api_doc/tests/test_doc.py:261-276).
- Information-disclosure note: documentation reveals technical model, field and method names; restricted by group plus per-user read rights as above.

## D. Handoffs to other modules
- Endpoints that this documentation describes for calling methods: rpc module (JSON-2) (rpc/controllers/json2.py:49-56).
- API key issuance and bearer authentication: base/core platform (evidence: api_doc/tests/test_doc.py:61-62).
- Module ordering uses the installed-module dependency graph from the platform (api_doc/controllers/api_doc.py:304-310).

## E. Configuration/defaults that change outcomes
- Group membership decides access; only superuser and system administrators get it by default (api_doc/security/res_groups.xml:6-7).
- Output depends on caller language and group set (cache key) (api_doc/controllers/api_doc.py:96-105).
- Backend action entry loaded in the backend asset bundle (api_doc/__manifest__.py:57-59).

## F. Effective extension path
- Documentation is derived from the installed models; extension modules appear automatically. Dependents/extensions in this tree: UNKNOWN — EVIDENCE INSUFFICIENT.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side playground behavior (request execution, key handling in the browser) beyond template names listed in the file tree.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether docstring parsing (second half of controller, lines 330-674) affects business outcomes; treated as presentation only.

