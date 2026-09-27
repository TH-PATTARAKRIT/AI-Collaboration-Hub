# G01 PLATFORM_BASE — Module `bus` — RED TEAM A1 Package

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Governed group / module | G01 PLATFORM_BASE / `bus` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_BUS_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `016e1d0a7204f74631c5f7968b0f1bd2ef45617800ed020ba8181583c798c2b2` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Freeze (topic lens only) | W1-B02, freeze_hash `cd966040f720456420057fe98fdb1176fbb9b0e85b456891f4dab82ea3ba0202`; bank `G01_BUS_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `cfa2be28…c8860d` (matches freeze manifest); ELIGIBLE |
| Date | 2026-09-27 |
| Lane B dependency | None. A1 did not wait for, view, or use Lane B evidence. |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Bank used as a topic lens only (subscription authorization, scope isolation, delivery semantics, retention, presence, rate limiting). No QID answered; bank not edited. All paths below are relative to `addons/bus/` at the anchor.

## 1. Claims

| Claim ID | Claim (neutral WHAT / WHY / RISK) | Evidence (path @ blob) | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-BUS-C01 | WHAT: module is a hidden, auto-installed realtime server→client notification transport depending only on base and web; ships an ACL file and no views, menus, record rules, groups or cron data. | `__manifest__.py` @ 2fdfb246 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C02 | WHAT: notifications are persisted as a log keyed by a DB-namespaced channel string, serialized payload and indexed create time. WHY: allows re-fetch after a gap. | `models/bus.py` @ 60bf05a6 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C03 | WHAT: publishing is transactional — rows created at pre-commit, DB-level notify after commit; a rolled-back transaction publishes nothing. | `models/bus.py` @ 60bf05a6 (spot-checked: pre-commit create under elevated rights) | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C04 | WHAT: the notification model's ACL row grants no read/write/create/unlink and names no group; every read/write path observed uses elevated (sudo) server code. RISK: all access control lives in channel-list construction, not in the data layer. | `security/ir.model.access.csv` @ 86cc8398; `models/bus.py`; `controllers/main.py` @ 92dbcb3a (all spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C05 | WHAT: on subscribe, the server appends broadcast, all of the user's groups and (if logged in) the user's partner; client-supplied channels are only type-checked as strings and then accepted as-is by the base hook. RISK: any authenticated or anonymous socket may subscribe to an arbitrary string channel; confidentiality of string channels rests on unguessability. | `models/ir_websocket.py` @ 538b3a63 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C06 | WHAT: source documentation on direct send states that string targets should not be guessable. WHY: acknowledges C05 as a design assumption, not an enforced check. | `models/bus.py` @ 60bf05a6 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C07 | WHAT: no company dimension exists in channel keys, subscription building, dispatch or websocket handling in this module; scoping is DB + record identity only. RISK: a partner/user shared across companies receives all its notifications regardless of active company context. | `models/bus.py`, `models/ir_websocket.py`, `websocket.py` @ ca7ff5d7 (spot-checked: no company references) | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C08 | WHAT: record addressing is re-routed — user to its partner, user settings to user, attachment to current user. RISK: fan-out follows partner identity, not user/company context. | `models/res_users.py`, `models/res_users_settings.py`, `models/ir_attachment.py` (Lane A only) | MED | SOURCE-STATIC |
| A1-G01-BUS-C09 | WHAT: first poll returns only the last ~50 s window; later polls return ids above the client's last id; a client-claimed last id above the current maximum is reset. WHY: bounded replay; no reauthorization of historical rows beyond current channel list. | `models/bus.py` @ 60bf05a6 (TIMEOUT constant spot-checked); `models/ir_websocket.py` | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C10 | WHAT: retention is an autovacuum job deleting rows older than a config parameter (default 24 h) via direct unbatched deletion; no cron data file shipped. | `models/bus.py` @ 60bf05a6 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C11 | WHAT: websocket limits — 1 MiB max message (whole or fragmented), per-socket rate limiter from server config, cursor acquisition retried up to 10 times, only protocol version 13 accepted. RISK: rate limit is per socket, not per tenant/customer. | `websocket.py` @ ca7ff5d7 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C12 | WHAT: custom close codes for session expired, keep-alive timeout and kill-now; keep-alive timeout from server config with random jitter. | `websocket.py` @ ca7ff5d7 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C13 | WHAT: session is revalidated at authenticate and on each dispatch; an invalid session forces logout with session-expired close. WHY: revocation propagates at next dispatch, not instantly. | `websocket.py` (Lane A only) | MED | SOURCE-STATIC |
| A1-G01-BUS-C14 | WHAT: cross-origin downgrade (mismatched Origin/Host/scheme → fresh anonymous session) runs only when env var `ODOO_BUS_PUBLIC_SAMESITE_WS` is set; default is no downgrade in this path; websocket route declares CORS `*`. RISK: cross-site websocket protection is opt-in by environment. | `websocket.py` @ ca7ff5d7 (spot-checked: env guard returns early when unset); CORS declaration per Lane A (`controllers/websocket.py`) | HIGH (env guard) / MED (CORS) | SOURCE-STATIC |
| A1-G01-BUS-C15 | WHAT: no presence model or presence logic exists in the module import list at this anchor. | `models/__init__.py` @ 2ddde881 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C16 | WHAT: public route reports only whether a notification id still exists (boolean) using an elevated count. RISK: low-grade existence oracle over global id space. | `controllers/main.py` @ 92dbcb3a (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-BUS-C17 | WHAT: authenticated route returns field metadata for requested model names; only relational inverse fields are filtered by field access; no model-level access check visible. RISK: metadata disclosure breadth. | `controllers/main.py`; `models/ir_model.py` (Lane A only) | MED | SOURCE-STATIC |
| A1-G01-BUS-C18 | WHAT: per-socket in-memory history of dispatched ids (10 s) de-duplicates and tolerates out-of-order commit visibility. WHY: delivery is at-least-once with client-side ordering by id. | `websocket.py` (Lane A only) | MED | SOURCE-STATIC |
| A1-G01-BUS-C19 | WHAT: post-login, a sticky danger notification is pushed when the admin logs in with the literal default password from a non-private IP without demo data. | `controllers/home.py` (Lane A only) | MED | SOURCE-STATIC |
| A1-G01-BUS-C20 | WHAT: websockets are refused in test mode and require the evented worker port. | `websocket.py`; `controllers/websocket.py` (Lane A only) | MED | SOURCE-STATIC |

## 2. Business rules (source-derived, neutral)
- BR1: A notification exists only if the publishing transaction commits (C03).
- BR2: Subscription = server-added identity channels ∪ client-supplied string channels (C05).
- BR3: Record-typed channels can only be added server-side; clients cannot name records directly (C05).
- BR4: Data-layer access to notifications is closed to all users; only elevated code reads/writes (C04).
- BR5: Notifications older than the retention parameter are purged (C10); fresh clients see only the last ~50 s (C09).
- BR6: Outdated client worker versions and non-13 protocol versions are rejected (C11; Lane A #16).

## 3. States / transitions
- Socket: handshake → open → (dispatch loop) → closed via clean / session-expired / keep-alive-timeout / kill-now / protocol error / message-too-big / try-later (C12).
- Notification row: pending (pre-commit, in memory) → persisted + notified (post-commit) → visible to poll → purged (GC). Rolled back → never exists.
- Session context: authenticated ↔ anonymous (public) on invalid session or, when env set, cross-origin downgrade (C13, C14).

## 4. Exceptions / failure modes
- Non-string client channel → value error (C05).
- Oversized notify payload → recursive split of channel list (Lane A #9).
- Dispatcher loop error → log, sleep 50 s, retry (Lane A #10): up to ~50 s delivery gap per process.
- Cursor pool exhaustion → up to 10 retries then failure / try-later close (C11).
- Oversized message → close with message-too-big (C11).
- Client last-id beyond max → reset to 0 (C09).

## 5. Cross-module handoffs
- Provides listener mixin and websocket hook for downstream modules to publish and to widen/validate channel lists; the actual authorization of string channels depends on consumers (Lane A G6).
- Depends on base (users, partners, groups, config params, session) and web (Home controller, assets).
- Presence expected downstream (C15) — owner module not identified.
- No direct edge to `digest`.

## 6. Evidence gaps (carried forward from Lane A + A1)
- GAP-BUS-01 (Lane A G1): presence location unknown at anchor.
- GAP-BUS-02 (Lane A G2): no dedicated long-poll route; only polling fallback.
- GAP-BUS-03 (Lane A G3): JS worker/reconnect/multi-tab logic not read.
- GAP-BUS-04 (Lane A G4): `websocket.py` read by targeted sections only.
- GAP-BUS-05 (Lane A G5): default values of `websocket_*` server config keys not read.
- GAP-BUS-06 (Lane A G6): downstream overrides of channel-list building not in scope — whether any consumer validates arbitrary client strings is unknown.
- GAP-BUS-07 (A1): no source evidence on multi-worker / multi-process fan-out correctness beyond per-process dispatcher.
- GAP-BUS-08 (A1): CORS declaration on `/websocket` not independently spot-checked by A1.

## 7. CRQ candidates
- CRQ-BUS-01: Must any client-requested topic subscription be authorized server-side (not by unguessability) before delivery? (C05, C06)
- CRQ-BUS-02: Must live delivery be scoped to active company/customer context, not only identity? (C07, C08)
- CRQ-BUS-03: Should cross-origin websocket protection be secure-by-default rather than environment opt-in? (C14)
- CRQ-BUS-04: Should rate limiting / resource protection be scoped per tenant in addition to per socket? (C11)
- CRQ-BUS-05: What is the required revocation latency for live subscriptions after access change? (C13)
- CRQ-BUS-06: Should the missed-notification existence check and model-metadata route be restricted or minimized? (C16, C17)
- CRQ-BUS-07: Where is presence owned, and what cross-scope visibility rule applies to it? (C15)
- CRQ-BUS-08: What retention policy applies to persisted payloads and is unbatched purge acceptable at scale? (C10)

## 8. Contradictions
- None CONFIRMED-FROM-SOURCE. Lane A statements checked in the spot-check log all matched source.
- CANDIDATE-BUS-X1: Design assumption "string targets not guessable" (C06) vs. absence of server-side validation of client string channels (C05) — a design tension, not a code contradiction; depends on downstream consumer behavior (GAP-BUS-06).

## 9. Spot-check log
Re-fetched from `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/bus/<path>`; `git hash-object` computed locally (scratchpad, no repo git operations).

| # | Path | Recorded blob | Computed blob | Match | Claim(s) verified in content |
|---|---|---|---|---|---|
| 1 | `security/ir.model.access.csv` | 86cc83980fb0036e355edf6ac8f434d449da915e | 86cc83980fb0036e355edf6ac8f434d449da915e | YES | C04: single row, no group, all perms zero |
| 2 | `models/ir_websocket.py` | 538b3a639ec45fa1dd538fef6c7f31ea84fa50c5 | 538b3a639ec45fa1dd538fef6c7f31ea84fa50c5 | YES | C05: string-type check only; appends broadcast, groups, partner |
| 3 | `websocket.py` | ca7ff5d712c479cf1859a6b41849dd3ba812a3bd | ca7ff5d712c479cf1859a6b41849dd3ba812a3bd | YES | C14 env guard; C11 1 MiB, 10 retries, version 13; C12 close codes 4001–4003; C07 no company refs |
| 4 | `models/__init__.py` | 2ddde8811f6c4276127c58d3d384cef09c6fff7f | 2ddde8811f6c4276127c58d3d384cef09c6fff7f | YES | C15: no presence module imported |
| 5 | `models/bus.py` | 60bf05a6cd86e9be478c91fbb98d64cfc0c84dd0 | 60bf05a6cd86e9be478c91fbb98d64cfc0c84dd0 | YES | C03, C06, C09 (50 s), C10 (autovacuum + retention param), sudo usage |
| 6 | `controllers/main.py` | 92dbcb3a3d3accdc5809a91a52b4633e19efe1c0 | 92dbcb3a3d3accdc5809a91a52b4633e19efe1c0 | YES | C16: elevated count, boolean result |
| 7 | `__manifest__.py` | 2fdfb24697ca638a1f1cc0ebfa1884ebdbc81d03 | 2fdfb24697ca638a1f1cc0ebfa1884ebdbc81d03 | YES | C01 (hash only; content per Lane A) |

Result: 7/7 blob matches; 0 mismatches.

## 10. Provenance
- Input: Lane A packet (sha256 above), consumed read-only.
- Spot-check fetches: anchor commit above via raw.githubusercontent; files held in session scratchpad only.
- Topic lens: frozen bank W1-B02 (hash verified against manifest); no QID answered.
- No Lane B material, no runtime system, no other lane packets consulted.

## 11. Limitations
- Source presence != runtime reachability; nothing here is runtime proof.
- No Formal Coverage claim; no percentages; no QID answers.
- Clean room: neutral WHAT/WHY/RISK only; identifiers are evidence pointers, not design recommendations; no code, schema, ORM or workflow reuse.
- Claims marked "Lane A only" were not re-read by A1 (MED confidence).
- JS layer and downstream consumers out of scope; single anchor commit.
