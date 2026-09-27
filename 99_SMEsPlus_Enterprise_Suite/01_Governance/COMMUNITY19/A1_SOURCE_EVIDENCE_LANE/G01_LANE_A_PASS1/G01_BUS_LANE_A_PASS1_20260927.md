# G01 PLATFORM_BASE — Module `bus` — Lane A Pass-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | SMEsPlus LANE A (blind source/static evidence) |
| Slot | T5 |
| Governed group | G01 PLATFORM_BASE |
| Module | `bus` (roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0, commit `8d05257d83f9128953f580a066db67c48fcdb96f` (raw.githubusercontent fetch) |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (Python/data scope; JS layer deliberately not deep-read per brief — see Limitations) |
| Handoff target | RED TEAM A1 only. No Lane B material consulted. No GMVQ QID answered. |

## 1. Evidence Pointer Table

| Path (addons/bus/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | 2fdfb24697ca638a1f1cc0ebfa1884ebdbc81d03 | Identity, deps, data list, asset bundles |
| `__init__.py` | 319991ba3864851d72d0cce4bed6d5cd28d0d6d1 | Package import graph |
| `models/__init__.py` | 2ddde8811f6c4276127c58d3d384cef09c6fff7f | Model import list |
| `controllers/__init__.py` | 33497e40e30f8b8ba33142e84dcfb9591067d0a9 | Controller import list |
| `tools/__init__.py` | 0aa8945c77d003dc57495b8f6583b3dd5eb18389 | Tool import |
| `tools/orjson.py` | 52913782eed7469b6435f8eafcec8a827c11f76d | JSON serializer shim (fast lib with stdlib fallback) |
| `models/bus.py` | 60bf05a6cd86e9be478c91fbb98d64cfc0c84dd0 | Notification store, send, poll, GC, dispatcher thread |
| `models/bus_listener_mixin.py` | ad8a73e56029e329ba48d67adb0a33ac5389a353 | Record-addressed send abstraction |
| `models/ir_websocket.py` | 538b3a639ec45fa1dd538fef6c7f31ea84fa50c5 | Channel list building, subscribe, websocket auth |
| `models/ir_attachment.py` | ed805704cfb497ee98ddcd61a486008233765047 | Attachment → current user channel |
| `models/res_users.py` | caedcedc5a882513c363c8051a9f4c1fbbb40f48 | User → partner channel |
| `models/res_users_settings.py` | 850561b6455f817f005c0a3db407589f52fe6695 | Settings → user channel |
| `models/res_partner.py` | 4a48364ece3590f613d7594e528dc48741ab00a8 | Partner is a listener |
| `models/res_groups.py` | 58a70fdc0961ff2f475ed5982ad2aba41c26c15e | Group is a listener |
| `models/ir_http.py` | 6e90c6196bb0ff6f01ce821f134e3e1df6f5da56 | Worker version in session info |
| `models/ir_model.py` | 8b306f74f2bbc32b7761c0cc8baa1d7d59280c53 | Model-definition export helper |
| `models/ir_qweb.py` | eff4b92f0a78fcc3baf7e616f4ee8190022eb332 | Worker bundle pre-generation |
| `controllers/websocket.py` | 155153e4ee94d6cee606b74bee39ca8a4546d937 | Websocket + polling-fallback routes |
| `controllers/main.py` | 92dbcb3a3d3accdc5809a91a52b4633e19efe1c0 | Model definitions + missed-notification routes |
| `controllers/home.py` | aa22eb65f67d886c4666502eccdcd8c4da49aace | Post-login default-admin-password warning |
| `websocket.py` | ca7ff5d712c479cf1859a6b41849dd3ba812a3bd | Websocket protocol, rate limit, timeouts, dispatch, handshake |
| `security/ir.model.access.csv` | 86cc83980fb0036e355edf6ac8f434d449da915e | Model ACL |

Blob count: 22.

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
1. Purpose: real-time server→client notification transport ("IM Bus"). Category Hidden; `auto_install` true — installs automatically once its deps are present (`__manifest__.py`).
2. Hard deps: `base`, `web` only. Declared data: ACL file only (no views, menus, crons, record rules, groups).
3. Ships asset bundles for backend, frontend, unit tests and a dedicated worker bundle (`bus.websocket_worker_assets`). JS content not reviewed (out of depth).

### 2.2 Data (models, key fields, constraints)
4. `bus.bus` — persisted notification log: channel (serialized target key), message (serialized type+payload), indexed create timestamp (`models/bus.py`). No SQL/Python constraints declared.
5. Channel key is namespaced by database name; a target may be a string, a record (model+id), or record+subchannel tuple (`channel_with_db`, `models/bus.py`).
6. `bus.listener.mixin` (abstract) makes a record addressable; the mixin is applied to partner, groups, users, user settings and attachment. Addressing is re-routed: user→its partner; settings→user (→partner); attachment→current user (`models/*.py`).
7. `ir.websocket` (abstract) — hook model for channel resolution and websocket events; no stored data.

### 2.3 Business rules / lifecycle / exceptions
8. Send is transactional: notifications are queued in a pre-commit hook (rows created on commit) and a post-commit hook emits a DB-level NOTIFY on a fixed channel; rolled-back transactions emit nothing (`_sendone`, `_ensure_hooks`).
9. NOTIFY payload size is bounded (env `ODOO_NOTIFY_PAYLOAD_MAX_LENGTH`, default ~8000 bytes); oversized channel lists are split recursively. NOTIFY function name overridable via env `ODOO_NOTIFY_FUNCTION` (`models/bus.py`).
10. Dispatcher: one lazily started daemon thread per process LISTENs on the notify channel, maps channel→subscribed websockets, and signals affected sockets to fetch; on loop error it logs, sleeps the timeout (50 s) and retries; stops on server stop event (`ImDispatch`).
11. Retrieval (`_poll`): first poll (last=0) returns only notifications from the last 50 s window; subsequent polls return ids greater than last known, excluding already-sent ids. If the client's claimed last id exceeds the current maximum, it is reset to 0 (`_prepare_subscribe_data`).
12. Ordering/duplicate control: per-socket in-memory history of dispatched ids kept 10 s to handle out-of-order commit visibility; last-id advances only past contiguous expired entries (`websocket.py` `_dispatch_bus_notifications`).
13. Websocket lifecycle: open/close lifecycle events; close codes include standard RFC codes plus custom session-expired (4001), keep-alive timeout (4002), kill-now (4003). Transport errors map to close codes (protocol error, message too big, try later on rate limit/pool exhaustion, session expired) (`websocket.py`).
14. Limits: max message 1 MiB (whole or fragmented); per-socket rate limiter (burst + delay from server config); cursor acquisition retries up to 10 times before failing (`websocket.py`).
15. Keep-alive/timeouts: frame-response timeout 15 s; inactivity ping ~40 s; keep-alive timeout from server config with random jitter (`TimeoutManager`).
16. Version gate: server worker version constant `19.0-2` published in session info; outdated client worker versions are closed; only websocket protocol version 13 accepted (`websocket.py`, `models/ir_http.py`).
17. Websockets disabled during test mode (service-unavailable) (`websocket_allowed`).
18. Presence: **no presence model or presence logic exists in this module at this anchor** (no presence file in models import list). See Gaps.
19. Post-login side effect: if a user logs in with the literal default admin password from a non-private IP, is the admin partner's user, and no demo data is installed, a sticky danger notification is pushed via the bus (`controllers/home.py`).

### 2.4 Jobs / config
20. GC: autovacuum job deletes notifications older than retention; retention from config parameter `bus.gc_retention_seconds` (default 24 h); deletion is direct SQL, unbatched (`_gc_messages`). No `ir.cron` data file shipped (fetch of a guessed cron file returned 404, consistent with manifest).
21. Server config keys read: `websocket_rate_limit_burst`, `websocket_rate_limit_delay`, `websocket_keep_alive_timeout`, `gevent_port` (error hint). Env vars: `ODOO_NOTIFY_FUNCTION`, `ODOO_NOTIFY_PAYLOAD_MAX_LENGTH`, `ODOO_BUS_PUBLIC_SAMESITE_WS`.
22. Websocket requires the evented (gevent) port; otherwise binding raises a runtime error with a hint.

### 2.5 Security
23. ACL: `bus.bus` granted no permissions to anyone (all zero, no group) — all access via elevated (sudo) server code (`security/ir.model.access.csv`; sudo usage in `_poll`, `_bus_last_id`, `has_missed_notifications`).
24. Channel authorization model: the server always appends broadcast, all of the user's groups, and (if logged in) the user's partner to the subscription. Client-supplied channels must be strings and are accepted as-is by the base hook; record-typed channels are server-resolved only (`_build_bus_channel_list`, `_prepare_subscribe_data`). RISK: string channels are an unguessability-based control; source docstring explicitly warns string targets must not be guessable (`_sendone`). Downstream modules extend this hook (not visible here).
25. Session validation on each dispatch and websocket authenticate: invalid session → logout + session-expired; anonymous sockets run as public user (`_authenticate`, `_dispatch_bus_notifications`).
26. Cross-site websocket hardening opt-in: with env `ODOO_BUS_PUBLIC_SAMESITE_WS`, a mismatched Origin/Host/scheme downgrades the socket to a fresh anonymous session (`_handle_public_configuration`). Default (env unset): no origin downgrade in this code path; route declares CORS `*`.
27. Company scoping: none in this module — channels are keyed by DB + record identity, not by company. No record rules.
28. `/bus/has_missed_notifications` (public) reveals only existence of a notification id (boolean) via sudo count.
29. `/bus/get_model_definitions` (user) returns field metadata for requested model names; relational inverse fields filtered by field read access; no explicit model-level access check visible in helper (RISK: metadata exposure breadth — evidence only).

### 2.6 UI surfaces (routes / names only)
30. Routes: `/websocket` (public, CORS *), `/websocket/health` (none), `/websocket/peek_notifications` (public, polling fallback; requires a websocket-session marker set on first poll), `/websocket/on_closed` (public), `/bus/websocket_worker_bundle` (public), `/bus/get_model_definitions` (user, POST), `/bus/has_missed_notifications` (public). Login-redirect override in web Home controller. No backend views/menus.

## 3. Cross-module edges
- Depends on `base` (users, partners, groups, config params, session security) and `web` (Home controller, asset/qweb bundles).
- Provides `bus.listener.mixin` and `ir.websocket` extension hooks used by other modules to publish and to widen/validate channel lists (consumers not in this module; e.g., messaging/presence expected downstream — unverified here).
- Couples to server runtime: evented worker, DB-level LISTEN/NOTIFY on the `postgres` database connection, session store.
- `digest` (same slot) has no direct import of `bus` (digest depends on mail; any bus edge would be transitive — not evidenced).

## 4. Evidence gaps / contradictions
- G1: Presence (in-scope topic per brief) not found in `bus` at this anchor; likely relocated to another module. Not verified — cross-lane pointer for A1.
- G2: Longpolling as a separate worker/route is not present; only the `peek_notifications` JSON-RPC fallback exists. "Longpolling" per brief maps to that fallback + 50 s constant; no dedicated long-poll route observed.
- G3: JS services/worker (reconnect, backoff, multi-tab sharing, outdated-worker handling) not read.
- G4: `websocket.py` read by targeted sections (dispatch, handshake, rate limit, timeouts, close codes); not every line reviewed.
- G5: Default values of the `websocket_*` server config keys live in core server config, outside anchor module — not read.
- G6: Consumers overriding `_build_bus_channel_list` (channel authorization extensions) are outside this module.
- No internal contradictions found.

## 5. Limitations
- Source presence ≠ runtime reachability; no runtime proof; no Formal Coverage claim; no percentages.
- Clean-room: neutral WHAT/WHY/RISK only; identifiers above are pointers, not design recommendations.
- Single anchor commit; findings may differ on other commits.
