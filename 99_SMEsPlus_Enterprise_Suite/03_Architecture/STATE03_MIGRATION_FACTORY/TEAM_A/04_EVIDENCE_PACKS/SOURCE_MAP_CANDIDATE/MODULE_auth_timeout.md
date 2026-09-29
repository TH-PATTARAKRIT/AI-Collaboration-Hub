# Source Map (candidate) — `auth_timeout`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `auth_timeout` |
| Display name | Auth Timeout |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `3083d239169c5a7f` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/auth_timeout/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `auth_totp`, `auth_totp_mail`, `auth_passkey`, `bus`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / Ask for authentication after user inactivity
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 3
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `ir.http`, `auth_totp.device`, `res.groups`, `res.users`, `ir.websocket`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.http`, `auth_totp.device`, `res.groups`, `res.users`, `ir.websocket`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 38 of 38 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: auth_timeout (Odoo 19.0.post20260921)
Scope: only pointers cited; anything else is UNKNOWN — EVIDENCE INSUFFICIENT.

## A. Capabilities
- Forces users to re-confirm identity after (1) a maximum session age ("session timeout" -> full logout / re-login) and/or (2) inactivity ("screen lock" -> confirm dialog without leaving the page). auth_timeout/models/ir_http.py:20-72,162-186; manifest summary auth_timeout/__manifest__.py:3.
- Configured per user group (no global switch). auth_timeout/models/res_groups.py:37-55; UI on group form "Timeouts" tab auth_timeout/views/res_groups_views.xml:9-35.
- Core: timeout evaluation, identity re-check screen/dialog, inactivity tracking. Optional: MFA requirement per timeout type (per-group flag). auth_timeout/models/res_groups.py:42-55.
- Conditional: hard dependency on auth_totp, auth_totp_mail, auth_passkey, bus. auth_timeout/__manifest__.py:5. Not auto_install (installed deliberately).

## B. Business objects, relationships, lifecycle
- No new tables; adds settings fields to permission groups (session timeout minutes, inactivity timeout minutes, MFA flags) plus session markers. auth_timeout/models/res_groups.py:37-55.
- Effective timeout for a user = shortest across all groups implied by membership, kept separately for MFA and non-MFA values. auth_timeout/models/res_groups.py:192-236.
- Session lifecycle: session age measured from session creation; inactivity from a "next check" marker set when presence says the user is idle or the last websocket tab closes; marker cleared once the user is active again before threshold. auth_timeout/models/ir_http.py:124-160; auth_timeout/models/ir_websocket.py:9-42.
- After successful re-check the marker is cleared and last-check time recorded. auth_timeout/models/ir_http.py:121-122.

## C. Validations, automation, security, session/audit
- Every authenticated-user request is checked; session-age expiry raises full logout; inactivity expiry raises identity-check (dialog for RPC calls, redirect to page for web pages). auth_timeout/models/ir_http.py:180-186,204-208.
- Routes can opt out of the inactivity check (needed for the confirm screen itself, menu loading, passkey start). auth_timeout/controllers/main.py:7,15,20; auth_timeout/controllers/web_home.py:12; auth_timeout/controllers/auth_passkey_webauthn.py:9.
- Allowed credential types = user's own methods: passkey if any registered, mail/app second factor if configured, always password. Other type -> access denied. auth_timeout/models/res_users.py:7-24; auth_timeout/models/ir_http.py:100-107.
- MFA path: first factor accepted then a second, different method is required; the first factor is remembered briefly and cannot be reused as the second; a passkey login skips the second factor. auth_timeout/models/ir_http.py:66-72,109-119; auth_passkey/models/res_users.py:66-70 (parent).
- MFA only asked when more than one method is available. auth_timeout/models/ir_http.py:116.
- Trusted-device lifetime for 2FA is capped at the user's shortest MFA timeout. auth_timeout/models/auth_totp_device.py:7-14.
- Timeout config changes clear the cached timeouts on create/write/delete of groups. auth_timeout/models/res_groups.py:173-190.
- Rate-limited mail-code sending is a write path, so check route cannot be read-only. auth_timeout/controllers/main.py:13-14.
- Audit: expiry uses debug-level logging only for the identity-check event. auth_timeout/models/ir_http.py:13-14. No dedicated audit record: none found.
- Security groups: settings are visible on the group form (backend, administrators via base group form); no new access CSV or record rules in module. auth_timeout/__manifest__.py:6-9. Company scoping: none.
- Login screen page shows company logo/name on the confirm page. auth_timeout/views/login_templates.xml:7-8.

## D. Handoffs
- auth_totp / auth_totp_mail: second-factor verification and email code. auth_timeout/controllers/main.py:20-23; auth_totp_mail/models/res_users.py:116,181.
- auth_passkey: passkey re-authentication. auth_timeout/static/src/services/check_identity/check_identity.js:87-88.
- bus/websocket presence: source of inactivity signal. auth_timeout/models/ir_websocket.py:9-23.
- web client: session info exposes inactivity threshold to backend and public site. auth_timeout/models/ir_http.py:211-252.

## E. Configuration/defaults
- Ticking "session timeout" defaults to 1 day with 2FA required; ticking "inactivity" defaults to 15 minutes without 2FA. auth_timeout/models/res_groups.py:144-145,162-163.
- Unticking clears value and MFA flag. auth_timeout/models/res_groups.py:140-142,158-160.
- Units minutes/hours/days converted to minutes. auth_timeout/models/res_groups.py:7-31.
- Multiple groups: shortest wins; MFA and non-MFA values evaluated in order. auth_timeout/models/res_groups.py:222-234.
- Trusted device age parameter interplay: see auth_totp/models/auth_totp.py:25-36.

## F. Effective extension path
- auth_totp, auth_totp_mail, auth_passkey, bus; base group form (view_groups_form). auth_timeout/views/res_groups_views.xml:6.

## G. Not verified
- Behaviour on public/portal website pages beyond session-info exposure: UNKNOWN — EVIDENCE INSUFFICIENT.
- Direct database-session/API-key access (non-browser clients) treatment: UNKNOWN — EVIDENCE INSUFFICIENT.
- Test coverage (TEST): timeout calculation, auth methods, identity-check exception, multi-timeout MFA, remember-device, tour. auth_timeout/tests/test_auth_timeout.py:23,49,290,314,357,414,477,530.
- Universal rules: none stated.

