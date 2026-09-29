# Source Map (candidate) — `microsoft_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `microsoft_account` |
| Display name | Microsoft Users |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `1669c6e2a148650f` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/microsoft_account/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`
- Direct dependents in 300-module list (1): `microsoft_calendar`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `microsoft.service` (Microsoft Service)
- Objects extended from other modules (1): `res.users`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.users`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 27 of 27 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: microsoft_account
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Shared plumbing for connecting a user's Microsoft account through Microsoft's sign-in/consent flow (OAuth 2): builds the consent address, exchanges the returned code for access and refresh tokens, renews tokens, and wraps calls to Microsoft's Graph API (microsoft_account/models/microsoft_service.py:59-117,119-144,146-194).
- Optional building block; depends on base_setup; category Hidden/Tools; no auto-install flag (microsoft_account/__manifest__.py:6,11).
- Calendar-oriented: the scope requested at token exchange is fixed to offline access, sign-in identity, and calendar read/write (microsoft_account/models/microsoft_service.py:48-49,125,133). The settings toggle for Outlook calendar sync lives in base_setup (base_setup/models/res_config_settings.py:17-18).
- Callback endpoint for Microsoft's consent result is public (microsoft_account/controllers/main.py:13-14).

## B. Business objects, relationships, lifecycle
- No stored business objects other than three fields added to the User: refresh token, access token, token validity time (microsoft_account/models/res_users.py:13-15).
- Flow: consuming module asks for a consent address (state carries database name, service name, return page and database UUID) -> user consents at Microsoft -> Microsoft redirects to `/microsoft_account/authentication` with code or error -> tokens are exchanged and stored on the current user -> browser is sent to the return page (microsoft_account/models/microsoft_service.py:95-117; microsoft_account/controllers/main.py:15-30).
- Token setter records validity as now plus lifetime, or empty when no lifetime is given (microsoft_account/models/res_users.py:17-22).
- Refresh: returns new access token, lifetime, and new refresh token (microsoft_account/models/microsoft_service.py:59-93).
- Consent refusal or unknown result redirects to the return page with an error parameter (microsoft_account/controllers/main.py:31-34).

## C. Validations, automation, security, credentials
- Bad request when service is missing or a code arrives without a return address (microsoft_account/controllers/main.py:19-20). The return address in the state parameter is used unchanged for redirection (microsoft_account/controllers/main.py:30,32,34); no validation here: caller-controlled redirect target, mitigation elsewhere UNKNOWN — EVIDENCE INSUFFICIENT.
- Credentials: per-service client id and client secret held as system parameters `microsoft_<service>_client_id` / `_client_secret`; id treated as non-secret; secret read with elevated rights only inside token requests; hook for modules that share keys (microsoft_account/models/microsoft_service.py:24-36,43-46,76-84,124-135).
- Token security: refresh and access tokens are readable only by system administrators at field level (the validity field is not restricted) (microsoft_account/models/res_users.py:13-15). Tokens are stored as plain text (microsoft_account/models/res_users.py:19-20).
- Outbound safety: request host must be one of Microsoft's default token or Graph hosts, so overriding the auth/token endpoint parameters to another host would fail this check (microsoft_account/models/microsoft_service.py:52-57,160-162); 20-second timeout; 204/404 treated as empty (microsoft_account/models/microsoft_service.py:15,21,177-193).
- Logging note: debug-level logging prints request parameters as passed, which include the client secret during token exchange; unlike the Google helper, no masking is applied (microsoft_account/models/microsoft_service.py:164). Compare google_account masking (google_account/models/google_service.py:125-133).
- Failed token exchange gives a user-facing configuration warning (microsoft_account/models/microsoft_service.py:142-144).
- No record rules, groups or company scoping in this module; tokens are per user.

## D. Handoffs to other modules
- Outlook/Microsoft calendar sync and any other consumer supply the service name and use the token fields and helpers: UNKNOWN — EVIDENCE INSUFFICIENT (not in the assigned module list).
- Settings toggle and System parameter configuration: base_setup / consuming module settings (base_setup/models/res_config_settings.py:17-18).
- Endpoint overrides are stored as system parameters `microsoft_account.auth_endpoint` and `.token_endpoint` (microsoft_account/models/microsoft_service.py:53,57).

## E. Configuration/defaults that change outcomes
- Seeded parameter "microsoft_redirect_uri" = out-of-band value, created once, never overwritten (microsoft_account/data/microsoft_account_data.xml:3-7). Whether the code still reads it: UNKNOWN — EVIDENCE INSUFFICIENT (the callback builds its own redirect from the request root: microsoft_account/controllers/main.py:23-27).
- Client id/secret per service must exist for the flow to work (microsoft_account/models/microsoft_service.py:36,46).

## F. Effective extension path
- Consuming modules call the helper for consent address, token exchange, refresh, and API calls; override the scope hook or secret hook (microsoft_account/models/microsoft_service.py:24-27,48-49). Module names: UNKNOWN — EVIDENCE INSUFFICIENT.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: which modules consume tokens/helper.
- UNKNOWN — EVIDENCE INSUFFICIENT: automated tests (none in module).
- UNKNOWN — EVIDENCE INSUFFICIENT: behavior when callback is hit by an unauthenticated visitor.

