# Source Map (candidate) — `google_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `google_account` |
| Display name | Google Users |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `75b73968f07b0417` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/google_account/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`
- Direct dependents in 300-module list (1): `google_calendar`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `google.service` (Google Service)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 26 of 26 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: google_account
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Shared plumbing for connecting a user's Google account to the system through Google's sign-in/consent flow (OAuth 2): builds the consent address, exchanges the returned code for access and refresh tokens, renews tokens, and wraps calls to Google APIs (google_account/models/google_service.py:47-69,71-92,94-105,107-162).
- Optional building block; depends on base_setup; category Hidden/Tools; no auto-install flag (google_account/__manifest__.py:6,11). The manifest text says it "adds google user in res user" but this module defines no user fields itself (google_account/__manifest__.py:8; models listing google_account/__init__.py:4).
- Callback endpoint for Google's consent result is public (google_account/controllers/main.py:13-14).

## B. Business objects, relationships, lifecycle
- No stored business objects; abstract "Google Service" helper only (google_account/models/google_service.py:37-39).
- Flow: a consuming module asks for the consent address for a named service and scope -> user consents at Google -> Google redirects to `/google_account/authentication` with a code (or error) and a state naming the service and the return page -> tokens are exchanged and handed to the current user's settings record -> browser is redirected to the return page (google_account/controllers/main.py:15-34).
- Errors from Google (consent refused) redirect to the return page with an error parameter (google_account/controllers/main.py:35-38).
- Token storage is on the user's settings record, whose token-setting method is provided by another module (google_account/controllers/main.py:29-31). That owner: UNKNOWN — EVIDENCE INSUFFICIENT.

## C. Validations, automation, security, credentials
- Request validation: a missing service, or a code without a return address, is rejected as a bad request (google_account/controllers/main.py:19-20). The return address supplied in the state parameter is used as-is for the redirect (google_account/controllers/main.py:34,36,38); no validation is present here, so redirect targets are caller-controlled: security observation, mitigation elsewhere UNKNOWN — EVIDENCE INSUFFICIENT.
- If the user record has no settings link, a generic warning is raised (google_account/controllers/main.py:29-33).
- Credentials: per-service client identifier and client secret held as system parameters named `google_<service>_client_id` / `_client_secret`; the identifier is treated as non-secret and the secret is read with elevated rights only inside outgoing token requests (google_account/models/google_service.py:22-34,41-44,76-85). Other modules can override the secret hook to share their own keys (google_account/models/google_service.py:25).
- Outbound safety: requests are allowed only to Google token and API hosts (assertion) (google_account/models/google_service.py:121-123); client secret is masked in logs (google_account/models/google_service.py:125-133); 20-second timeout (google_account/models/google_service.py:15,108); HTTP 204/404 are treated as empty results, other HTTP errors are logged and raised (google_account/models/google_service.py:146-161).
- Token exchange failure yields a user-facing "authorization code invalid or expired" configuration warning (google_account/models/google_service.py:89-92).
- Only POST-style calls carry secrets in the body, not the URL, for token exchange (google_account/models/google_service.py:71-75,87).
- No groups, record rules or company scoping in this module; each user's tokens belong to that user's settings.

## D. Handoffs to other modules
- Calendar/contact/mail sync features using Google (e.g., Google Calendar) supply the service name, scope, redirect and token storage: consumer modules not in this assigned list; toggle exists in base_setup settings for Google Calendar (base_setup/models/res_config_settings.py:15-16). Module ownership of storage: UNKNOWN — EVIDENCE INSUFFICIENT.
- System parameters for Google credentials: configured via settings of the consuming module (name pattern: google_account/models/google_service.py:34,44).

## E. Configuration/defaults that change outcomes
- Service-specific client id/secret parameters must exist for the flow to work (google_account/models/google_service.py:34,44).
- Consent address parameters: access type, approval prompt, state (google_account/models/google_service.py:47-69).
- Redirect address is derived from the request root or the user's base URL (google_account/controllers/main.py:23-27).

## F. Effective extension path
- Consuming modules call the helper for consent address, token exchange, refresh, and API calls; they may override the secret hook (google_account/models/google_service.py:22-26,47,71,94,107).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: what happens when the callback is reached without a signed-in user (public user's settings link).
- UNKNOWN — EVIDENCE INSUFFICIENT: which modules consume this helper in this tree.
- UNKNOWN — EVIDENCE INSUFFICIENT: automated tests (none present in module).

