# Source Map (candidate) — `bus`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `bus` |
| Display name | IM Bus |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `0da3173c1091b701` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/bus/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `web`
- Direct dependents in 300-module list (4): `auth_timeout`, `html_editor`, `mail`, `spreadsheet`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `bus.bus` (Communication Bus); `ir.websocket` (websocket message handling); `bus.listener.mixin` (Can send messages via bus.bus)
- Objects extended from other modules (8): `ir.model`, `ir.http`, `ir.attachment`, `res.users.settings`, `res.groups`, `ir.qweb`, `res.users`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `ir.websocket` ← Community: `auth_timeout`, `hr_presence`, `html_editor`, `im_livechat`, `mail`; open-license custom/third-party scanned: —
- `bus.listener.mixin` ← Community: `mail`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `ir.model`, `ir.http`, `ir.attachment`, `res.users.settings`, `res.groups`, `ir.qweb`, `res.users`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 41 of 41 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — bus
Source revision: 19.0.post20260921 | Module: "IM Bus" (bus/__manifest__.py:2), category Hidden (:4), LGPL-3 (:38). Infrastructure module (brief note). Basis: static reading of models, controllers, security, key constants and test names.

## A. Capabilities and optionality
- A1. Live notification transport: server code can push a message to specific recipients (a person, a group, all users, a named channel) and connected browsers receive it without polling, through a persistent connection (websocket) with a shared background worker on the client. bus/__manifest__.py:5; bus/models/bus.py:110-133; bus/controllers/websocket.py:11-14
- A2. Messages are stored briefly in a table and announced through the database notification service ("imbus"); a listener thread relays announcements to the connected sessions that subscribed to the channel. bus/models/bus.py:88-95,135-168,207-262
- A3. Notification is sent only after the business transaction commits (nothing is announced for rolled-back work); very large announcements are split. bus/models/bus.py:135-168,68-85 (TEST) bus/tests/test_notify.py:15,56
- A4. Any model can be a recipient by mixing in the "can send via bus" helper; the person (partner), user, group, attachment (goes to the current user), and user-settings records are already recipients. bus/models/bus_listener_mixin.py:12-30; bus/models/res_partner.py:6-8; bus/models/res_users.py:6-11; bus/models/res_groups.py:6-8; bus/models/ir_attachment.py:6-11; bus/models/res_users_settings.py:6-11
- A5. Default subscriptions of every connected session: the "broadcast" channel, each group the user belongs to, and the user's partner. bus/models/ir_websocket.py:15-28
- A6. Client services: multi-tab coordination, presence, assets watchdog (notify when a newer version of the web assets exists), simple notification popups, debug log menu. bus/static/src/services/ (file names: bus_service.js, presence_service.js, assets_watchdog_service.js); bus/static/src/simple_notification_service.js; bus/static/src/debug/bus_logs_menu_item.js
- A7. Health endpoint, missed-notification detector, and delivery of the worker script bundle. bus/controllers/websocket.py:22-24,50-51; bus/controllers/main.py:15-19
- A8. Optionality: auto_install = True (depends base, web), so present in essentially all databases; no settings switch, no group. bus/__manifest__.py:6,11

## B. Objects and relationships
- B1. bus.bus "Communication Bus": channel text, message text, creation time (indexed). No user-facing UI. bus/models/bus.py:88-95
- B2. bus.listener.mixin (abstract) and ir.websocket (abstract handler for subscribe/authenticate/close events). bus/models/bus_listener_mixin.py:6-30; bus/models/ir_websocket.py:11-83
- B3. Lifecycle of a message: queued at commit -> row created -> announced -> delivered to subscribers -> deleted by scheduled autovacuum. bus/models/bus.py:97-108,139-141
- B4. Model metadata service for the web client (field definitions, only for models the caller lists, inverse fields only where the reader has read access). bus/models/ir_model.py:9-36; bus/controllers/main.py:9-13

## C. Validations, security, audit
- C1. Table has an access row with no group and no rights: normal users cannot read or write messages; the system reads and writes through elevated rights. bus/security/ir.model.access.csv:2; bus/models/bus.py:141,182
- C2. Only text channel names from the client are accepted for subscription; the server adds the trusted ones (broadcast, groups, partner). Text channels used server-side must not be guessable. bus/models/ir_websocket.py:38-60; bus/models/bus.py:111-119
- C3. Websocket authentication: logged-in sessions are re-validated and expired ones are logged out; anonymous sessions act as the public user. bus/models/ir_websocket.py:75-83
- C4. Protection limits: message size cap (1 MiB), per-connection frame rate limit with burst and delay from server configuration, supported protocol version 13, client/server worker version check. bus/websocket.py:271,299-301,697-708,977,988,1100,1120 (TEST) bus/tests/test_websocket_rate_limiting.py:18-64
- C5. Missed-notification check answers whether a given last-seen id still exists. bus/controllers/main.py:15-19
- C6. Default-password warning: after a login with the password "admin" from a non-private address on a database without demo data, the Administrator receives a sticky warning through the bus. bus/controllers/home.py:10-31
- C7. No company scoping and no audit trail of notifications (rows deleted after retention). bus/models/bus.py:97-108
- C8. Notification retention window: 24 h by default, parameter bus.gc_retention_seconds. bus/models/bus.py:26,99-103 (TEST) bus/tests/test_bus_gc.py:12-30

## D. Handoffs
- D1. Chat, presence, and user-facing notifications built on the bus: mail (extends ir.websocket and uses the bus), im_livechat, hr_presence. Group of modules that extend ir.websocket: auth_timeout, hr_presence, html_editor, im_livechat, mail (inheritance scan).
- D2. Session inactivity lock: auth_timeout uses the bus. bus dependency via manifest scan: auth_timeout, html_editor, mail, spreadsheet.
- D3. HTTP/websocket server and session framework: odoo core (http.py, service) and web.
- D4. Modules that call the bus sender directly (grep of _bus_send/_sendone, module names): account, account_peppol, analytic, auth_signup, base_geolocalize, calendar, crm_livechat, hr_timesheet, iap_mail, im_livechat, l10n_fr_pdp, l10n_in, l10n_tr_nilvera, mail, point_of_sale, survey, website_crm_partner_assign, website_livechat (plus bus itself).

## E. Configuration/defaults that change outcomes
- E1. bus.gc_retention_seconds (default 86400). bus/models/bus.py:26,99-103
- E2. Server configuration for websocket rate limit burst/delay. bus/websocket.py:299-301
- E3. Environment variables ODOO_NOTIFY_FUNCTION (default pg_notify) and ODOO_NOTIFY_PAYLOAD_MAX_LENGTH (default 8000 bytes). bus/models/bus.py:29,32-43
- E4. Long-poll/listener timeout constant of 50 s; first-poll buffer of the same duration. bus/models/bus.py:25,173-175

## F. Effective extension path (module names only)
- Depend on bus (direct manifests): auth_timeout, html_editor, mail, spreadsheet. Mixed-in bus.listener.mixin outside bus: mail (grep). ir.websocket extended by: auth_timeout, hr_presence, html_editor, im_livechat, mail.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour under multi-worker / reverse-proxy deployments (needs deployment configuration outside the module).
- UNKNOWN — EVIDENCE INSUFFICIENT: default values of the websocket rate-limit configuration (read from server config, not from module files).
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side JS internals beyond file inventory.

