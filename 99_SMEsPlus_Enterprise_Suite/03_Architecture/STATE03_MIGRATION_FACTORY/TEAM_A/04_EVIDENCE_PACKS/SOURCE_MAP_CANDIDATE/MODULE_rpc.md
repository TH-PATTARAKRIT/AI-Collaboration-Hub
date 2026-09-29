# Source Map (candidate) — `rpc`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `rpc` |
| Display name | RPC endpoints |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `0a2ffba442c6417b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/rpc/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `test_http`, `test_rpc`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Extra Tools / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 2
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 34 of 35 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: rpc
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Technical module that exposes external programmatic access to business models: legacy XML-RPC and JSON-RPC endpoints plus the newer "JSON-2" endpoint (rpc/__manifest__.py:3-9; rpc/controllers/__init__.py:19-23).
- Conditional-by-default: it depends only on the base module and is flagged to install automatically (rpc/__manifest__.py:10,12). No settings toggle or group gates the module itself.
- Version-information endpoint (`/web/version`, `/json/version`) returns product version data with no authentication (rpc/controllers/__init__.py:24-29).
- The legacy XML-RPC (`/xmlrpc`, `/xmlrpc/2`) and JSON-RPC (`/jsonrpc`) endpoints are declared deprecated in Odoo 19, with removal scheduled for Odoo 22; each call logs a warning (rpc/controllers/__init__.py:6-11; rpc/controllers/xmlrpc.py:144,159; rpc/controllers/jsonrpc.py:14).
- The JSON-2 endpoint accepts a single call form: POST to model + method; other paths/verbs under `/json/2` return a not-found hint (rpc/controllers/json2.py:38-56).

## B. Business objects, relationships, lifecycle
- No business objects or stored data are defined; manifest lists no models, data files, groups, rules, or scheduled jobs (rpc/__manifest__.py:1-15; skeleton sourcemap/rpc.json).
- Calls act on whatever models are installed: the caller names a model, a public method, optional record identifiers, a context, and arguments (rpc/controllers/json2.py:57-64).
- Results returning record sets are converted to lists of record identifiers (rpc/controllers/json2.py:87-88).
- Legacy services are dispatched by service name and method to the platform's generic dispatcher (rpc/controllers/xmlrpc.py:130-135; rpc/controllers/jsonrpc.py:11-16).

## C. Validations, automation, security, credentials
- JSON-2 requires bearer-token authentication for the model/method route (rpc/controllers/json2.py:49-56). Session is not saved for these calls (rpc/controllers/json2.py:55).
- Unknown model -> not found; unknown or non-public method -> not found (rpc/controllers/json2.py:65-74).
- A model-level (class) method cannot be called with record identifiers -> unprocessable (rpc/controllers/json2.py:75-77).
- Argument shape is checked against the method signature before execution -> unprocessable on mismatch (rpc/controllers/json2.py:80-84).
- Read-only vs read/write database transaction is chosen from the target method's read-only marker; if the model is unknown the request is treated as read-only (rpc/controllers/json2.py:23-35).
- Legacy XML-RPC and JSON-RPC use no platform authentication at route level (auth "none") and skip CSRF for XML-RPC; authentication is done inside the dispatched service call (rpc/controllers/xmlrpc.py:137,156; rpc/controllers/jsonrpc.py:11). Whether access rights apply to the invoked model is decided by the model service, not visible here: UNKNOWN — EVIDENCE INSUFFICIENT.
- Fault mapping: access-denied, access-error, user-error/warning and internal errors are turned into distinct fault codes; unexpected errors return full trace text to the caller (rpc/controllers/xmlrpc.py:20-48,51-68). Business note: internal error detail leaks to the RPC client on unhandled errors.
- Marshalling: control characters are stripped from text, dates become strings, binary data is sent as text (rpc/controllers/xmlrpc.py:30-31,81-100).
- (TEST) Wrong password: authentication returns false and later model call is denied (rpc/tests/test_xmlrpc.py:218-226). API keys can be used in place of a password (rpc/tests/test_xmlrpc.py:228-253). A user can delete own API keys, an administrator can delete others', other users cannot (rpc/tests/test_xmlrpc.py:255-277). Deactivated user is denied with both password and key (rpc/tests/test_xmlrpc.py:279-295). Programmatic API-key renewal depends on a system parameter for enabling programmatic API keys (rpc/tests/test_xmlrpc.py:297-299).
- Credential implication: external clients hold either a user password or a per-user API key; JSON-2 needs a bearer token (rpc/controllers/json2.py:52).

## D. Handoffs to other modules
- Authentication, API keys, user and access-rule enforcement: owned by the base/core platform, not by rpc (evidence only via tests: rpc/tests/test_xmlrpc.py:228,255).
- Documentation for the JSON-2 endpoint and bearer-authenticated doc routes: api_doc module (api_doc/controllers/api_doc.py:48,165).
- Everything else the caller invokes belongs to the model's owning module.

## E. Configuration/defaults that change outcomes
- Auto-install: present whenever base is installed unless explicitly excluded (rpc/__manifest__.py:12).
- (TEST) System parameter for programmatic API keys influences key renewal (rpc/tests/test_xmlrpc.py:298).
- Deprecation logger can be muted through log-handler level (rpc/controllers/__init__.py:10).

## F. Effective extension path
- Not a business extension point; other modules extend behavior only by adding public model methods that become callable. Modules consuming this: api_doc.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: enforcement of record-level access rules on legacy dispatch (lives outside the module).
- UNKNOWN — EVIDENCE INSUFFICIENT: rate limiting, bearer token issuance, and API-key lifecycle rules (outside this module).

