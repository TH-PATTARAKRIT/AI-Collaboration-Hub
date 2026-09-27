# G01 PLATFORM_BASE — RED TEAM A2 Addendum R1 (A3 remediation, batch 2) — `bus`, `digest`, `resource`, `resource_mail`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **RED TEAM A2** (primary). Section 1 is a separately labelled **RED TEAM A1 note**, written by the owner-stage role for A1 wording. This is an addendum only: every parent is immutable and none was edited |
| Group / Modules | G01 PLATFORM_BASE / `bus`, `digest`, `resource`, `resource_mail` |
| Date | 2026-09-27 (written after 15:25:53Z) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`. Re-fetched for this remediation into scratch `remed_batch2/src/`. `git hash-object` MATCH for all 19 module files. Two further files were recorded, not matched, because no earlier stage had pinned them: the framework `odoo/http.py` (blob `ebfc2ac8d268a45aaf4b8cde8c9ce8b480d58dbb`) and `resource/views/resource_calendar_views.xml` (blob `402890182cb087e7b649f29a42f0aef14e7ae923`, fetched and not relied on). Log: `remed_batch2/blob_log.txt`, sha256 `6f021dc87742eb0daffabf02725c1ace253d0bf3659b88876c728ea0eeabbdfb` |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

Paths below are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

### 0.1 Parent artifacts (sha256; unchanged since A3 intake, re-verified 2026-09-27T15:25Z)

| Parent | sha256 |
|---|---|
| `G01_A1_PACKAGES/G01_BUS_A1_PACKAGE_20260927.md` | `6c3e5a44267b28835f26c1859c5637432ebe791f4030f3e0f13f0f0054f1d875` |
| `G01_A1_PACKAGES/G01_DIGEST_A1_PACKAGE_20260927.md` | `030442be4f9ccd83f2f988e4299749fafcf76a6954a794f2948337c7fa04ba87` |
| `G01_A1_PACKAGES/G01_RESOURCE_A1_PACKAGE_20260927.md` | `c7f17c210f6f4abca84a26d2f024d774577b56cdfaf0b9febe4d7d1b453a0d7d` |
| `G01_A1_PACKAGES/G01_RESOURCE_MAIL_A1_PACKAGE_20260927.md` | `f3f552c5098154ed344d338ff91148b6a0f39a6c605fdb6df5284ff16cc88ee8` |
| `G01_A2_REVIEWS/G01_BUS_A2_REVIEW_20260927.md` | `41d50e929d3476039cef3f586f10250a05d8700d7f764449c5be24bf15bb9343` |
| `G01_A2_REVIEWS/G01_DIGEST_A2_REVIEW_20260927.md` | `324bde08f503ea0261aad8fb87f52794b65a0d3a100a3dee2a9ba1d77d3ef44f` |
| `G01_A2_REVIEWS/G01_RESOURCE_A2_REVIEW_20260927.md` | `23b99cd698b4aa630616e99dba28d4080c5fc8e4e95fc1242f122c6a04b3f4a0` |
| `G01_A2_REVIEWS/G01_RESOURCE_MAIL_A2_REVIEW_20260927.md` | `e4e630b904a55c3b98a75ce26f82618c11fad62cce522e11370c60d8073c42a9` |

### 0.2 A3 reports addressed (sha256)

| A3 report | sha256 |
|---|---|
| `G01_A3_CHALLENGES/G01_BUS_A3_STATIC_20260927.md` | `4f9c2676bfe15588479686392e4ec9520e26ab6b56ea90b9920ef613ef3209b6` |
| `G01_A3_CHALLENGES/G01_DIGEST_A3_STATIC_20260927.md` | `2eae23cddf02d14bb5ad47fd19890be5150733088ed332271e7daab8f31360a4` |
| `G01_A3_CHALLENGES/G01_RESOURCE_A3_STATIC_20260927.md` | `50894e31e50ad78ad88bbec72a0d0bb218bcdd38b30832f7e5dedd79675dab52` |
| `G01_A3_CHALLENGES/G01_RESOURCE_MAIL_A3_STATIC_20260927.md` | `1c570f56bb35bab9375be2c1cc287c4c3eb90bd5137e05181a0b9a49231d7a4a` |
| `G01_A3_CHALLENGES/G01_RESOURCE_RMAIL_A3_SUPPLEMENT_S2_20260927.md` (MASTER-registered; the stricter result governs) | `25c154b36361ba549f8ac4f8edd34dc6f0f70d7f7723b290499c2ccad908edb1` |

### 0.3 Challenge IDs addressed in this addendum (A1/A2 parts)

- **bus:** D-BUS-01 (A2 part, PR-BUS-06); D-BUS-02 (A2 part, OM-B01); A3 1.2 finding on REC-BUS-24 (A2 origin, OM-B04); D-BUS-05 (A2 part: PR for OM-B05, and OM-B08 wording); D-BUS-06 (A1 C14 RISK and A2 SF-B04); A3 section 3 runtime note on PC-BUS-10 (PR-BUS-05 variant).
- **digest:** D-DGST-01 (A2 part: PR for OM-D08); D-DGST-04 (A2 part: PR-DGST-05 fault injection, PR-DGST-08 disjunctive expectation, unreachable-catch finding); A3 section 3 runtime note on PC-DGST-08.
- **resource:** S-A (runtime proof requirements for REC-06, 11, 19, 20, 27, 28); S-C (A2 origin: materiality of naive-as-UTC); D01 and D02 (A2 origin of PR-06 wording); N1–N7 (A2 semantic verification and proof requirements).
- **resource_mail:** M-A (A2 origin: O-01/F-01 exposure list).

Clean-room note: neutral paraphrase only. Identifiers appear only as evidence pointers, with no code, domains or expressions reproduced. No percentages. No Formal Coverage claim. No QID answered. No git operations. No existing artifact was edited.

Method: for each sustained challenge, the owner stage first **re-derived the point from source on its own** (column "Independent re-derivation"), then recorded **AGREE** or **DISPUTE** with evidence, and only then wrote the correction.

---

## 1. RED TEAM A1 note (clearly labelled; A1 owner-stage wording correction)

| A1 item | Challenge | Independent re-derivation | Position | Corrected A1 wording (R1) |
|---|---|---|---|---|
| A1-G01-BUS-C14 (RISK) | D-BUS-06 | The module's Origin handling is confirmed: presence only, with comparison and downgrade only when the env flag is set (`websocket.py`@ca7ff5d7 L1059–1078). **New framework evidence:** at the anchor, the framework's session-save path sets the session cookie with the HttpOnly attribute and a max-age, and passes **no explicit SameSite attribute and no Secure flag** (`odoo/http.py`@ebfc2ac8 L2187–2194; the session-expiry path at L2523 behaves the same; the cookie helper's default for SameSite is "none given" at L1597/L1609). Browser cross-site cookie delivery therefore falls to browser defaults and to any reverse-proxy rewriting, and neither can be seen in source | **AGREE** (wording qualified) | **C14 RISK-R1:** "At module level, cross-site websocket Origin handling is opt-in by environment and downgrades rather than rejects. Exploitability by a browser-originated cross-site page also depends on whether the browser sends the session cookie. The framework sets no explicit SameSite attribute at the anchor, so this depends on browser defaults and deployment proxies: runtime and deployment dependent, not proven by source." The WHAT and the MED/HIGH confidence are unchanged. CRQ-BUS-03 is widened to "secure-by-default Origin **and** explicit cookie SameSite policy" |
| A1-G01-BUS-C18 (WHY) | D-BUS-01 (context) | No A1 change beyond the existing REC-BUS-18 CONTRADICTION. A1's "at-least-once" stays refuted on source (section 2.1) | — | None. The CONTRADICTION class stays |

No other A1 wording is changed by this batch. The resource and resource_mail A3 challenges carry no A1-owned defect.

---

## 2. `bus` — A2 corrections

### 2.1 D-BUS-01: loss-window mechanism and PR-BUS-06 (A2 part)

**Independent re-derivation.** The low-level send call only appends the serialized channel and message to a pre-commit data list and adds the channel to a post-commit set (`models/bus.py`@60bf05a6 L111–133). The row insert, and therefore the id, happens inside a pre-commit callback registered on the first send of the transaction (L135–141). NOTIFY happens in a post-commit callback (L143–168). On the socket side, each dispatch polls rows above the held-back last id, excluding ids in the in-memory history (`websocket.py`@ca7ff5d7 L767–773). History entries are stamped with the **dispatch** time, and entries older than the 10 s threshold are trimmed. The last id advances to the highest trimmed id, and **trimming only runs during a dispatch that returned at least one row** (L774–797). The source comment's own wording (L272–296) talks about ids being "assigned immediately when requested". In this module the request happens at pre-commit.

**Position: AGREE with A3.** The loss condition is: row X gets its id in the pre-commit hook of transaction T1, and T1's commit becomes visible later than all of the following for the same socket: (a) a higher-id row Y has been dispatched; (b) more than 10 s have passed since Y's dispatch; and (c) a further dispatch that returned at least one row has trimmed Y, moving the last id past X. The relevant gap is **pre-commit row creation → commit visibility**. It is not "business-code send call → commit", and not the whole transaction length. A2's parent C18 wording ("gap between notification creation and commit") is imprecise but not wrong. A2's inference in PR-BUS-06 is wrong: the fail condition "A's notification delivered → at-least-once holds" does not follow, because one delivery cannot show a delivery guarantee.

**PR-BUS-06R1 (replaces PR-BUS-06):**

| Field | Content |
|---|---|
| Claim(s) | C18, OM-B04; REC-BUS-18, 24 |
| Procedure | Isolated instance with the evented worker. One authenticated socket subscribed to target P. **Declared fault injection in the test harness:** in transaction T1, send a notification to P, then register a later pre-commit step (or a DB-level commit hold) that blocks **after** the bus pre-commit insert and **before** the commit, for longer than 10 s plus the time needed for the next step. While T1 is held: T2 sends and commits a notification to P (dispatched), then waits more than 10 s, then T3 sends and commits another notification to P (dispatched, which trims history). Release T1 and let it commit. Then send T4 to P. Record the ids, commit times, dispatch times and frames |
| Expected (source prediction) | T1's notification is **never** delivered on that socket, including after T4 |
| Fail condition | T1's notification is delivered on that socket. Meaning if it fails: the source reading of the trimming or exclusion is incomplete. It does **not** mean "at-least-once holds". A single delivery proves no guarantee |
| Control | The same sequence **without** the injected hold. T1's notification is delivered. This shows the harness itself does not drop rows |

### 2.2 D-BUS-02: OM-B01 wording (A2 part)

**Independent re-derivation.** NOTIFY runs on a connection to the cluster maintenance DB with one fixed channel name (`models/bus.py`@60bf05a6 L160–168). The dispatcher LISTENs there (L238–246). Wake-ups are routed through a map keyed by DB-prefixed channel keys (L212–220, L256–259). A woken socket then opens a cursor on **its own session DB** (`websocket.py`@ca7ff5d7 L759–773). The poll builds channel keys with **its own** DB name and searches its own table (`models/bus.py` L170–190). NOTIFY payloads are JSON lists of full channel keys: DB name, model name and record id for record channels, and DB name plus the **client-chosen string** for string channels (L58–85, L133, L152–153).

**Position: AGREE with A3.**

**OM-B01-R1 (replaces the OM-B01 wording):** "One fixed notify channel on the cluster maintenance database carries wake-ups for every database served by the cluster. **Wake-up routing** is keyed by the DB name in each channel key. **Payload separation** also rests on per-database storage: a woken socket reads only its own session database's table, with keys rebuilt from that database's name. The medium therefore does not by itself carry payload content across tenants. The residual exposure is metadata: NOTIFY payloads carry channel identifiers in clear text (DB names, model names, record ids, and client string channels). C05/C06 treat those string channels as unguessable capability tokens, so any principal able to LISTEN on the cluster maintenance DB (DB-level access) can learn them and could then subscribe to them within that database (links REC-BUS-05/06)."

**PR-BUS-09R1 (replaces PR-BUS-09):** two DBs on one cluster with identical channel strings and record ids. Publish in DB1. Record separately (i) **wake-up**: whether DB2 sockets on the same process are triggered to dispatch, and (ii) **content**: whether any DB2 socket receives a DB1 payload. A separate LISTEN session on the maintenance DB records the raw NOTIFY payload. Expected: (i) DB2 sockets are not woken by DB1-only keys; (ii) no DB2 socket receives DB1 content; (iii) the raw payload shows the DB1 channel keys, including string channels, in clear. Fail: any DB1 content on a DB2 socket (content leak), or a DB2 wake-up on DB1-only keys (routing defect, recorded separately). If (iii) is absent, the metadata-exposure reading is refuted.

### 2.3 A3 1.2 (REC-BUS-24 / OM-B04): publisher obligation (A2 origin)

**Independent re-derivation.** As in 2.1, the module itself defers row creation to pre-commit, whenever the business code calls send. **Position: AGREE.** **OM-B04-R1:** "The loss window runs from the bus pre-commit insert to commit visibility. The source comment's advice to publish close to commit is mostly satisfied by the module's own deferral. The residual obligation concerns work that runs **after** the bus pre-commit step inside the same commit (for example later pre-commit callbacks or a slow commit). Its ordering and duration are framework and deployment behaviour that was not read." The severity stays as in the parent, and the obligation is narrowed.

### 2.4 D-BUS-05 (A2 part): OM-B05 proof requirement and OM-B08 wording

**OM-B05: independent re-derivation.** The base channel hook always appends the broadcast channel and the env user's full group set, and it appends the partner only when a session uid exists (`models/ir_websocket.py`@538b3a63 L15–28). For a socket with no uid, authentication switches the env to the public user (L75–83). **AGREE** that this is material.

**PR-BUS-10 (new; REC-BUS-25):** an anonymous (no-session) socket and an anonymous polling-fallback call. As an internal user, publish (i) to the broadcast channel and (ii) to a group channel of a group the public user belongs to. Expected: the anonymous socket and poll receive both. Fail: either is not received, which means filtering exists outside the module or in the framework. Also record which shipped modules publish to broadcast (inventory, not a pass/fail item).

**OM-B08: independent re-derivation.** On any dispatcher loop exception, the thread logs it, sleeps for the 50 s constant, then re-enters the loop and re-LISTENs (`models/bus.py`@60bf05a6 L25, L261–269). While it sleeps, no LISTEN is active on that process. Notification rows persist in each database until GC (default 24 h; L26, L97–108). On the socket side, a dispatch runs **only** when triggered, either by a NOTIFY for one of its channels or by a subscribe call (`websocket.py`@ca7ff5d7 L390–411). The socket's event loop wakes every 15 s only to handle keep-alive, ping and timeouts. It does not re-poll the table (L343–372, L824). Whether PostgreSQL keeps NOTIFYs for a session that is not listening is database behaviour and was not read. The common understanding is that it does not.

**Position:**
- **AGREE with A3** that "silences all tenants" overstates the effect. Rows are not lost at that moment, and the effect is limited to sockets served by the affected process.
- **DISPUTE (partial)** the A3 replacement "delay of up to 50 s". Nothing in the module bounds the delay by the sleep. After re-LISTEN, a notification whose NOTIFY went out during the sleep is fetched only at that socket's **next trigger**: a later notification on any of its channels, a client resubscribe, or a reconnect. If no trigger arrives before the GC retention horizon, the row is deleted without being dispatched. Evidence: the trigger-only dispatch and the absence of any periodic re-poll, as cited above.

**OM-B08-R1:** "A dispatcher error on one process pauses wake-ups for all databases' sockets on that process for at least the 50 s retry sleep. Notification rows stay stored. Rows whose NOTIFY fell in the pause are delivered at each socket's next wake-up trigger (next notification on any subscribed channel, resubscribe or reconnect). The delay is not bounded by the module and can exceed 50 s. It becomes loss only if no trigger arrives before GC retention expires."

**PR-BUS-11 (new; REC-BUS-28):** isolated instance. **Declared fault injection:** force one dispatcher loop exception, for example by interrupting its LISTEN connection. During the sleep, publish N1 to socket S. Case A: publish nothing else for 120 s. Case B: after 70 s, publish N2 to S. Expected: Case A, N1 is **not** delivered within 120 s. Case B, N1 is delivered together with or just before N2. Fail: in Case A, N1 is delivered within about 50–65 s with no further trigger. That would show a recovery path that source does not show.

### 2.5 D-BUS-06 (A2 part): SF-B04 wording

**Independent re-derivation:** as in section 1. **AGREE.** **SF-B04-R1:** "Browsers do not apply CORS to WebSocket handshakes. The module-level control is Origin handling (presence required; comparison and downgrade only under the env flag). Whether a cross-site page can open an **authenticated** socket also depends on whether the browser sends the session cookie. The framework sets the cookie with HttpOnly and no explicit SameSite or Secure attribute at the anchor, so this is decided by browser defaults and proxies. It is **not** evidenced in source, and it is **not** tested by injecting the cookie directly."

**PR-BUS-04R1 (extends PR-BUS-04):** keeps the direct-injection steps as sub-case (a), and adds sub-case (b) **browser-originated**: an authenticated user in a current mainstream browser visits a page on a foreign origin that opens a websocket to the instance, with the env flag unset. Record the cookie attributes as received (headers), whether the cookie was sent on the handshake, and the resulting socket identity (authenticated or anonymous). Expected: recorded per browser. The RISK in C14 RISK-R1 stands only if an authenticated socket results. Fail (of the RISK): no browser tested sends the cookie cross-site.

### 2.6 A3 section 3 note: PR-BUS-05 variant

**PR-BUS-05R1 (extends PR-BUS-05):** adds sub-case (c): an **anonymous** socket and an anonymous polling call name an arbitrary string channel that an internal user published to more than 50 s earlier, with last id = 1. Expected: the retained rows on that string channel are returned (C05 combined with the replay rule). Fail: they are not returned.

### 2.7 PR-BUS-08 classification note

PR-BUS-08 records an outcome either way. It is re-labelled **MEASUREMENT**: it gathers information and cannot count as proof for or against REC-BUS-17. There is no change to its procedure.

---

## 3. `digest` — A2 corrections

### 3.1 D-DGST-04 (A2 part): C09 unreachable catch and PR-DGST-05

**Independent re-derivation.** The cron wraps each digest's send in a catch for one exception type only, the mail-delivery exception (`models/digest.py`@3eea1c39 L225–232). In the module that type appears only in the import (L12) and in that catch. The send path renders the body and then creates an outgoing, auto-delete mail record under elevated rights. There is no direct send call (L140–157, L159–223, and a module-wide search). **AGREE.** On the module's own path the catch is **effectively unreachable**. It can fire only if an override or extension in another module raises that type inside the send path, which is out of scope.

**C09 finding R1 (added to the C09 PARTIAL basis):** "The cron's catch covers an exception type that the module's queue-only send path does not raise. Delivery failures happen later in the mail queue, and any other exception propagates (framework transaction effect)."

**PR-DGST-05R1 (replaces PR-DGST-05):** as in the parent, with **declared fault injection**: the harness patches the per-recipient send step so that it raises the mail-delivery exception type after the first recipient's mail record has been created. Expected: on rerun, the first recipient gets a second queued mail and the digest stayed due. Fail: no duplicate, or the next date advanced. A control run without injection must show a normal single queue per recipient and the next date advanced.

### 3.2 D-DGST-04 (A2 part): PR-DGST-08 expectation

**Independent re-derivation.** Rendering takes the header, subject and currency from the recipient's default company (L171, L190, L220, L294–296). KPI evaluation runs as the recipient, **narrowed** to that same company (L277–279). The company-based KPI filters on the digest's company, falling back to the env company only when the digest has none (L58–69, L413–435). How narrowing interacts with record rules is framework behaviour and was not read. **AGREE** with A3. A2's own SF-D02/OM-D02 predicts that the value may be zero by rule.

**PR-DGST-08R1 (replaces PR-DGST-08):** same setup. **Expected (disjunctive):** subject, header and currency show company B; **and** the monetary KPI value is **either** (a) computed for company A **or** (b) zero or restricted by record rule under B's narrowing. Record which one occurs. Fail: labels and currency come from A, or the value is computed for B's own data. Both of those contradict the source reading.

### 3.3 A3 section 3 note: PR-DGST-04

**PR-DGST-04R1 (extends PR-DGST-04):** also record the serialized start and end strings passed to the KPI queries for each window (from logs or a debugger). This settles whether attaching the calendar timezone has any effect on the queried values (A3 1.1 row 1.7).

### 3.4 D-DGST-01 (A2 part): proof requirement for OM-D08

**Independent re-derivation.** The send loop walks every recipient in the many-to-many with no share or active filter in module code (L149–154). The recipient restriction is a field-level UI domain only (L27). The module's only users extension is the create-time auto-subscribe, which filters share users only at creation (`models/res_users.py`@44884554). Whether the framework drops archived users when reading the relation was not read. **AGREE:** this is material.

**PR-DGST-11 (new; REC-DGST-27):** isolated instance with no real delivery. Internal user U is a recipient of digest D. Convert U to a portal (share) user. Set D due and run the scheduler. Inspect the queued mail records. Expected: a digest mail is queued to U with internal KPI labels and values. Fail: no mail is queued to U, meaning a share filter exists elsewhere. Also record whether converting U was allowed while U was a recipient.

---

## 4. `resource` — A2 corrections

### 4.1 S-C: materiality of naive-as-UTC (A2 section 4 origin)

**Independent re-derivation.** The public hour-count and unusual-days entry points replace a missing timezone with UTC (`resource_calendar.py`@335a8576 L727–730, L815–818). The planning helpers use the framework helper that attaches UTC when it is missing, and hand results back naive-UTC when the input was naive (`date_utils.py`@bde8a943 L90–99; calendar L843–844, L864–865, L909–910). The framework convention is that stored datetimes are naive UTC. **AGREE.** The 7-hour effect happens only when a caller passes naive **local** wall-clock values. No such caller was identified in the module.

**Thailand bullet R1 (replaces "naive-as-UTC is material (7-hour shift)"):** "Conditionally material. If a consumer passes naive Asia/Bangkok local datetimes to the hour-count, unusual-days or planning entry points, results shift by 7 h and can cross a day boundary. Callers that follow the framework's naive-UTC convention are not affected. No affected caller is identified in `resource`. Consumers in other modules remain to be checked (runtime and cross-module)."

### 4.2 D01 / D02: PR-06 wording (A2 F-04 / O-05 origin)

**Independent re-derivation.** On creation, the default hook seeds the full-time reference from the default company's calendar, which is the session company unless a company is supplied (L56–59). The reference is a **stored**, user-editable compute (L93–96). The compute only processes calendars that have a company, and leaves company-less ones as they are (L158–161). The rate is a **non-stored** compute with no clamp, and it falls back to 100 only when the reference is empty or zero (L116–117, L250–256). **AGREE with A3 D01 and D02.** A2 F-04 already carried the caveat. A2's own PR-06 wording "shown/stored" was inaccurate.

**PR-06R1 (replaces PR-06):** (a) a 60 h/week calendar with a 40 h reference: the rate reads 150 wherever it is displayed or read. It is computed on read, not stored. (b) A company-less calendar created while the session company's calendar has a non-zero reference: record the seeded reference and the rate. Expected: the reference equals the session company calendar's value, and the rate follows hours ÷ reference (not a fixed 100). (c) The same calendar with its reference set to zero or empty: the rate reads 100. Fail: (a) clamped or rejected; (b) rate 100 while the reference is non-zero; (c) any value other than 100.

### 4.3 S-A: runtime proof requirements for GAP/CONTRADICTION items that lacked one

**Independent re-derivation.**
- REC-06/19: the section error needs two-week mode, at least one section row, and a first row by sequence that is not a section (L123–129). Overlap in two-week mode is checked only on rows typed first or second week (L134–136). The form onchange raises unless there is exactly one section per week (L183–191), so the no-section state can be reached only through non-form writes. Rows with no week type are counted as week 0 by interval generation (L355–365).
- REC-11/20: calendar-less leaves are included for every calendar (L513–515).
- REC-27: company holidays are copied as values, not linked, whenever a calendar is new or its company changes (L202–208). The mode toggles unlink rows and reload defaults (L299–321).
- REC-28: the admin exemption depends on a framework group implication that was not read.

**AGREE** with S-A on all six items.

| PR | REC | Setup / action | Expected | Fail condition |
|---|---|---|---|---|
| PR-11 | REC-06, 19 | Via RPC (not the form): create a two-week calendar with **no** section rows and overlapping rows with no week type; separately, a two-week calendar whose first row is a section but which has later rows outside any section | Both saved without error | Either rejected. Also record that the form path rejects the no-section edit (reachability) |
| PR-12 | REC-19 (R3) | Two-week calendar with one untyped row overlapping a first-week row; compute work hours for one first-week and one second-week date | The untyped row counts as first-week work; the overlap is not rejected; first-week hours include both rows | Row ignored, counted in both weeks, or overlap rejected |
| PR-13 | REC-11, 20 | Same company: calendars C1 and C2, a calendar-less company leave on day D, resources on each; compute work intervals | Day D is removed on both C1 and C2 for same-company resources and at calendar level | Day D is kept on either |
| PR-14 | REC-27 | (a) Create calendar X, then add a holiday to the company default calendar. (b) Customize X's slots, then toggle two-week mode off; separately toggle duration-based off. (c) Change X's company | (a) X lacks the new holiday; (b) custom slots replaced by company defaults with no confirmation; (c) X's global leaves replaced by the new company's | Propagation in (a), slots kept in (b), or leaves kept in (c) |
| PR-15 | REC-28 | `resource`-only install. System admin edits a personal leave of a resource linked to another user; also record whether the admin group implies the ERP-manager group. Call plan-days with a resource-specific leave on the path | Personal-leave edit denied; the implication is recorded; plan-days ignores the resource-specific leave | Edit allowed, or plan-days honours the resource leave |

### 4.4 N1–N7: A2 semantic verification (A3 supplement candidates)

| N | Independent re-derivation (paraphrase, pointers @335a8576 unless stated) | Position | PR |
|---|---|---|---|
| N1 | The global-leave compute runs for new calendars and for **any** company change, including to empty (L202–208), and rebuilds the leaves from the new company's default calendar, which is none when the company is emptied. The attendance compute instead requires a non-empty new company for existing records (L174). Whether clearing deletes the leaves or leaves them calendar-less depends on the framework: the leaf's calendar link declares no delete rule (`resource_calendar_leaves.py`@841053e6 L39–44). | AGREE (effect INCONCLUSIVE, runtime) | PR-16 |
| N2 | When the call is calendar-level, an empty resource is added to the list and the calendar term admits calendar-less leaves (L513–515). The company guard only applies when a resource is set (L535). Calendar-level results therefore subtract calendar-less leaves of **any** company the caller can see. | AGREE | PR-17 |
| N3 | The cached weekday lookup marks every attendance row of the calendar as working for its (week type, weekday), with no filter for section rows or break rows, and it is cached on the calendar id only (L1011–1018). Section rows default to Monday (`resource_calendar_attendance.py`@d8fb69b1 L15–23). **However, it has a caller in the module files:** the works-on-date helper (L943–951) calls it. That helper has no caller in the fetched module files. | **DISPUTE (partial)**: the "no caller in the module files" part is refuted. The rest is AGREED | PR-18 |
| N4 | The leave end-date compute reads the company **on the whole recordset** in its fallback branch, taken only when neither a user tz nor a context tz is set (`resource_calendar_leaves.py` L63–67). The framework's singleton rule for reading a field on several records was not read. | AGREE (effect runtime) | PR-19 |
| N5 | Leaving two-week mode also switches duration-based mode off with no notice (L306–310). A2 F-09 did not mention this. | AGREE (A2 F-09 omission acknowledged) | PR-20 |
| N6 | The tz variable is overwritten at the first **matching** (leave, resource) pair, after the skip test (L534–537). Clipping compares timezone-aware instants (L548–552), so instants stay correct. The likely effect is on output tzinfo and on whole-day widening for flexible resources (L550–551). | AGREE (supersedes the parent R1 "first resource") | PR-21 |
| N7 | The overlap check places every row on a single weekly timeline (day index × 24 + hour; L615–625). Out-of-range hours can therefore collide with the next day's rows. "Per weekday" is an approximation. | AGREE | PR-22 |

| PR | N | Setup / action | Expected | Fail condition |
|---|---|---|---|---|
| PR-16 | N1 | Calendar in company A with global leaves; set its company to empty; search leaves by their former ids | Record whether the leaves are deleted or kept with an empty calendar. If kept, check whether they then reduce hours on an unrelated calendar (REC-20 chain) | — (the outcome defines the effect). Claim refuted if the leaves survive attached to the calendar |
| PR-17 | N2 | Caller who can see companies A and B. Calendar in A. A calendar-less leave in B on day D. Compute calendar-level hours (no resource) | Day D is subtracted | Day D is not subtracted |
| PR-18 | N3 | Two-week calendar with no Monday slots but with section rows. Call the works-on-date helper for a Monday of each week type (harness call) | Monday is reported as worked | Monday is reported as not worked |
| PR-19 | N4 | User with no tz, no context tz. Create two leaves in one call with no end date | Singleton-type error | Both created |
| PR-20 | N5 | Two-week, duration-based calendar. Leave two-week mode | Duration-based is off afterwards | Duration-based stays on |
| PR-21 | N6 | Calendar-level call with two resources in different tz and a leave on the second only; repeat with a flexible second resource | Instants correct. The output tzinfo is the first matching pair's tz. The flexible leave is widened on day boundaries of that tz | Output tz is per resource, or widening follows the resource's own tz |
| PR-22 | N7 | RPC: a Monday row ending past 24 h (for example 30 h) and a Tuesday row early in the morning | Overlap error raised | Both saved |

---

## 5. `resource_mail` — A2 correction (M-A)

**Independent re-derivation.** Besides the related email, phone and share-flag fields (`resource/models/resource_resource.py`@aad3af2f L40–42), the resource declares a linked-user reference field (L38). It also declares an avatar image as a **plain non-stored compute** that copies the linked user's avatar (L39, L61–64), not as a related field. The avatar-card method returns a plain read of whatever field list the caller supplies (`resource_mail/models/resource_resource.py`@797be7bd L17–18). Whether that compute runs with the caller's rights, and so whether a restricted user's avatar is readable, is framework behaviour. **AGREE.**

**O-01-R1 / F-01-R1 (replaces the exposure list):** "The avatar-card read can return the linked user's **email, phone, share flag, presence, avatar image, and the linked-user reference** (id and display name) to any internal user who can read the resource: the session's active companies or no company (A3 N-1 precision adopted). Related fields and the avatar compute may be evaluated with elevated rights or with the caller's rights. That is framework behaviour and is not proven."

**PR-03R1 (extends PR-03):** the same setup, with the requested list extended to include the avatar image and the linked-user reference, and a variant where the linked user's own record is **not** readable by the caller under the user record rules. Expected: the values are returned for a same-company resource. Record whether the avatar and reference are returned in the restricted variant. Fail: fields filtered or denied on the same-company resource, or company-B data returned.

---

## 6. Summary of A2-owned changes

| Module | Changed item | Kind |
|---|---|---|
| bus | C14 RISK-R1 (A1), SF-B04-R1, OM-B01-R1, OM-B04-R1, OM-B08-R1 | Wording (no class change) |
| bus | PR-BUS-06R1, PR-BUS-09R1 (replace); PR-BUS-04R1, PR-BUS-05R1 (extend); PR-BUS-10, PR-BUS-11 (new); PR-BUS-08 relabelled MEASUREMENT | Proof requirements |
| digest | C09 finding R1 | Wording |
| digest | PR-DGST-05R1, PR-DGST-08R1 (replace); PR-DGST-04R1 (extend); PR-DGST-11 (new) | Proof requirements |
| resource | Thailand bullet R1 (S-C) | Wording |
| resource | PR-06R1 (replace); PR-11..PR-15 (S-A); PR-16..PR-22 (N1–N7) | Proof requirements |
| resource_mail | O-01-R1 / F-01-R1 | Wording |
| resource_mail | PR-03R1 (extend) | Proof requirement |

**DISPUTED items (partial):** (1) REC-BUS-28 / OM-B08: A3's "delay of up to about 50 s" is not supported. The delay has no module bound and lasts until the next trigger (2.4). (2) N3: "no caller in module files" is refuted, because the works-on-date helper calls the cached lookup (4.4). Every other sustained challenge in scope is **AGREED**.

## 7. Limitations

- Static only, at one anchor commit. Framework internals that bear on the corrected wording were not read beyond the session-cookie lines in `odoo/http.py`: commit-hook ordering, database NOTIFY retention, `with_company` narrowing, clear-command semantics on one-to-many, the singleton rule, and archived-user filtering on relations. Each point that depends on them is marked runtime or INCONCLUSIVE.
- A2 re-derived each point before writing. Because it read the same anchor source as the upstream stages, its independence is at role level only.
- No percentages, no Formal Coverage claim, and no QID answered. No git operations. The parents are untouched.
