# G01 PLATFORM_BASE — RED TEAM A3 Re-check R1 (remediation batch 2) — `bus`, `digest`, `resource`, `resource_mail`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, independent adversarial re-check of remediation R1 batch 2 |
| Independence | This A3 instance wrote none of the original A3 reports, the S2 supplement, or the A2/REC/PROOF R1 addenda. It re-fetched source itself and re-read it rather than relying on addendum paraphrase. Independence is at role level; the session infrastructure (scratchpad root) is shared with the remediation controller |
| Date | 2026-09-27 (intake 15:35:26Z; source re-fetch 15:36:05Z; manifest 15:41:22Z; exit check 15:43:52Z: all 10 inputs OK, unchanged) |
| Scope | STATIC only (SOURCE/CONFIG). All runtime cases are **NOT-EXECUTED**, neither passed nor failed. No runtime prediction is treated as proven |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`. A3 re-fetched all 21 files in `remed_batch2/blob_log.txt` into scratch `a3r1_b2/src/`. `git hash-object`: **21 of 21 MATCH**, including the two files the remediation had only "RECORDED" (`odoo/http.py` `ebfc2ac8…`, `resource/views/resource_calendar_views.xml` `40289018…`). A3 additionally fetched and recorded (not previously pinned): `addons/resource/models/res_users.py` `ef4f8859…`, `resource_mixin.py` `b68b6a9f…`, `utils.py` `38137c26…`, and framework `odoo/tools/config.py` `433ff84b…` |
| **Overall** | bus: **A3 R1 RE-CHECK: STATIC PASS WITH RESIDUAL DEFECTS (route A2, REC, PROOF — LOW)**. digest: **A3 R1 RE-CHECK: STATIC PASS — MASTER HANDOFF PENDING RUNTIME**. resource: **A3 R1 RE-CHECK: STATIC PASS WITH RESIDUAL DEFECTS (route REC — LOW)**. resource_mail: **A3 R1 RE-CHECK: STATIC PASS WITH RESIDUAL DEFECTS (route REC — LOW)**. Cross-module process residuals are routed to MASTER / Integration Control (section 6). Every module's MASTER handoff remains **pending runtime** |

### 0.1 Input lineage (sha256, intake = exit)

Paths relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/` unless shown. Manifest: scratch `a3r1_b2/intake.sha256`.

| Input | sha256 | Git (read-only) |
|---|---|---|
| `G01_A3_CHALLENGES/G01_BUS_A3_STATIC_20260927.md` | `4f9c2676bfe15588479686392e4ec9520e26ab6b56ea90b9920ef613ef3209b6` | equals value cited by all three addenda |
| `G01_A3_CHALLENGES/G01_DIGEST_A3_STATIC_20260927.md` | `2eae23cddf02d14bb5ad47fd19890be5150733088ed332271e7daab8f31360a4` | same |
| `G01_A3_CHALLENGES/G01_RESOURCE_A3_STATIC_20260927.md` | `50894e31e50ad78ad88bbec72a0d0bb218bcdd38b30832f7e5dedd79675dab52` | same |
| `G01_A3_CHALLENGES/G01_RESOURCE_MAIL_A3_STATIC_20260927.md` | `1c570f56bb35bab9375be2c1cc287c4c3eb90bd5137e05181a0b9a49231d7a4a` | same |
| `G01_A3_CHALLENGES/G01_RESOURCE_RMAIL_A3_SUPPLEMENT_S2_20260927.md` (MASTER-registered; stricter governs) | `25c154b36361ba549f8ac4f8edd34dc6f0f70d7f7723b290499c2ccad908edb1` | same |
| `G01_A2_REVIEWS/G01_BATCH2_A2_ADDENDUM_R1_20260927.md` | `9664c13e01c777e4731381966a412b4a9eea675168ec5ad4f848c56d0a6a037c` | 1 commit `32b4275` 15:29:27Z; mtime 15:28:14Z; committed = disk |
| `G01_RECONCILIATION/G01_BATCH2_REC_ADDENDUM_R1_20260927.md` | `18292fd3418f26152330446fc20080f4fd453a04c3555c1932807652e56c5331` | 1 commit `efca765` 15:32:22Z; mtime 15:30:38Z; = disk |
| `G01_PROOF/G01_BATCH2_PROOF_ADDENDUM_R1_20260927.md` | `141fb8558c59303a9e6395d4bd6fd2b26bf5fb865d6d094988153108fd0854f9` | 1 commit `4ace7c3` 15:35:18Z; mtime 15:34:31Z; = disk |
| `../MASTER_CONTROLLED_HANDOFF_STATE_20260927_C1B.md` | `d3966ad058ca11e82ef20ec777818486a726996f8d04f6a59da4315cf6e84e42` | last commit `57c46fe` 15:20:45Z |
| `../MASTER_DECISION_LOG_G01_20260927.md` | `aa3230bd5d79490e6e4c390b044c1eedea72afeff082bdf814a007af69386c60` | last commit `26e5704` 15:32:39Z |

### 0.2 Sealed predeclaration and logs (scratch `remed_batch2/`)

| File | sha256 (A3 recomputed) | Birth / mtime | Finding |
|---|---|---|---|
| `proof_addendum_R1_cases_predeclared.txt` | `a93b7ed54369cda476b7676bbe6ca35add9bab7b1ab93af740d1aa6756a3d5f7` | born = mtime 15:31:42.34Z; never modified | **MATCH** to `predeclared.sha256` and to the PROOF header. Seal files `predeclared.timestamp` (15:31:46Z) and `predeclared.sha256` were born 15:31:46Z, before `exec_log.txt` was born (15:31:57.50Z). Seal **VERIFIED** |
| `exec_log.txt` | `f82238049895756d7c180e5f0a808d560451f1a5a4ede4a47d1fc3fd3a138eb0` | born 15:31:57Z; last write 15:32:38Z | MATCH to PROOF header. "EXEC END 15:32:18Z" then verdicts appended at 15:32:38Z; the recorded hash is of the final file. Consistent |
| `blob_log.txt` | `6f021dc87742eb0daffabf02725c1ace253d0bf3659b88876c728ea0eeabbdfb` | born 15:21:21Z | MATCH to both addenda headers |
| `src/exec_log.txt` (not cited anywhere) | `fb39b6a0…` | born 15:32:03Z, inside the execution window | A context-dump side file (grep context for the PC-BUS-11R1 retry check). Not a competing verdict record; hygiene note H-1 only |
| Predeclared case IDs | 44 IDs: 17 static + 24 runtime + 2 MEASUREMENT relabels (PC-BUS-16, PC-DGST-04) + 1 ILLUSTRATION relabel (PC-RSRC-10) | — | Equals the PROOF addendum supersede map and sections 2–3 |

---

## 1. Per original sustained challenge — closure status

Legend: **CLOSED** = defect remedied on content and verified by A3 from source/documents. **PARTIALLY CLOSED** = remedied in part; residual named. **OPEN** = not remedied.

### 1.1 `bus`

| Challenge | Remedy location | A3 verification | Status |
|---|---|---|---|
| D-BUS-01 (loss-window / pre-commit id; PC-BUS-11/12 design; invalid "delivered → at-least-once") | A2 add. 2.1 (PR-BUS-06R1); REC add. 1.2 (REC-BUS-18/24); PROOF PC-BUS-11R1 (static), PC-BUS-12R1 [INJ] + control | Source re-read: send only queues pre-commit values and a post-commit channel (`bus.py` L111–133); insert in pre-commit callback (L135–141); NOTIFY post-commit (L143–168); history stamped at dispatch time and trimmed only on a non-empty dispatch (`websocket.py` L771–797, early return at L774–775). Invalid inference removed; control run added | **CLOSED** |
| D-BUS-02 ("solely"; read path; clear-text string channels) | A2 OM-B01-R1, PR-BUS-09R1; REC-BUS-21 R1 (linked to 05/06); PC-BUS-17R1, PC-BUS-18R1 | Confirmed (maintenance-DB NOTIFY, own-DB cursor, own-DB poll, full channel keys in payload). PC-BUS-18R1 separates wake-up from content and adds raw-NOTIFY capture | **CLOSED** |
| A3 1.2 REC-BUS-24 / OM-B04 overstated obligation | A2 OM-B04-R1; REC-BUS-24 R1 | Narrowed to post-bus-pre-commit work; framework ordering marked unread | **CLOSED** |
| D-BUS-03 (MRRP collapsed to UNCORROBORATED, 8 items) | REC add. 1.1 | 8 rows restored; column totals NA 6 + UNC 14 + MRRP 8 = 28 = REC total | **CLOSED** |
| D-BUS-04 (Q007/Q013/Q037 wrongly "no evidence"; REC-BUS-14 unmapped) | REC add. 1.3 | Mapped 35 + no-evidence 6 = 41, disjoint. Named QIDs corrected; REC-BUS-14 → Q002/Q040. *New residual R-BUS-2 (section 5) on Q021, not previously raised* | **CLOSED** (for the challenged items) |
| D-BUS-05 (REC-BUS-25 no PR; REC-BUS-28 overstated) | A2 2.4 (PR-BUS-10, PR-BUS-11, OM-B08-R1); REC add. 1.2; PC-BUS-19/20/21/22 | REC-BUS-25: PR/PC added, source confirmed (`ir_websocket.py` L23–28, L81–83; public routes). REC-BUS-28: "silences all tenants" withdrawn. Delay wording **disputed** — ruled in section 2(a): remediation right against A3's 50 s bound, with a LOW precision residual R-BUS-1 | **CLOSED** (REC-BUS-25) / **PARTIALLY CLOSED** (REC-BUS-28: residual R-BUS-1) |
| D-BUS-06 (cookie attributes omitted; direct-injection runtime case) | A1 C14 RISK-R1; A2 SF-B04-R1, PR-BUS-04R1; REC-BUS-14; PC-BUS-23, PC-BUS-08R1(b) | Framework fact verified (section 3). Browser-originated variant added. Citation precision note R-BUS-3 (section 3) | **CLOSED** |
| D-BUS-07 (unmarked post-predeclaration Expected text) | PROOF add. §4 | 12 phrases across 12 parent cases marked; verdicts judged against TSV only; no FAIL condition changed. Tag string is "POST-PREDECLARATION TEXT" rather than the C1-B rule-2 literal `POST-DECLARATION` — content equivalent (process note) | **CLOSED** |
| A3 §3 runtime notes (PC-BUS-10 variant; PC-BUS-16 measurement) | PR-BUS-05R1 / PC-BUS-10R1; PC-BUS-16 relabelled MEASUREMENT | Verified in ledger (section 4.2) | **CLOSED** |

### 1.2 `digest`

| Challenge | Remedy | A3 verification | Status |
|---|---|---|---|
| D-DGST-01 (REC-DGST-27 no PR) | PR-DGST-11; PC-DGST-22 (static), PC-DGST-23 (runtime) | Send loop over all `user_ids` with no share/active filter (`digest.py` L149–154); UI-only domain (L27); users extension is create-time only (`res_users.py` L9–19) | **CLOSED** |
| D-DGST-02 (MRRP collapse, 7 items) | REC add. 2.1 | 7 rows restored; NA 3 + UNC 17 + MRRP 7 = 27 = REC total | **CLOSED** |
| D-DGST-03 (Q015/Q007/Q032 lineage) | REC add. 2.3 | Mapped 30 + no-evidence 10 = 40, disjoint; Q032 marked partial; lineage only | **CLOSED** |
| D-DGST-04 (PC-DGST-16 expectation; PC-DGST-10 undeclared injection; unreachable catch) | PR-DGST-05R1/08R1; PC-DGST-10R1 [INJ] + control, PC-DGST-16R1 disjunctive, PC-DGST-21 finding | Exception type appears only at import (L12) and catch (L231); send path creates `mail.mail` under sudo (L222); no direct send. Disjunctive expectation matches A2 SF-D02 | **CLOSED** |
| D-DGST-05 (unmarked post-predeclaration text) | PROOF add. §4 | PC-DGST-05/13/15 marked; others checked | **CLOSED** |
| A3 §3 runtime notes (PC-DGST-08 window strings; PC-DGST-04 measurement) | PR-DGST-04R1 / PC-DGST-08R1; PC-DGST-04 MEASUREMENT | Verified | **CLOSED** |

### 1.3 `resource` (committed D01/D02 + S2 supplement S-A..S-F; stricter governs)

| Challenge | Remedy | A3 verification | Status |
|---|---|---|---|
| A3-RSRC-D01 (REC-24 dropped the conditional) | REC-RSRC-24 basis R1; PR-06R1; PC-RSRC-08R1 | Default hook seeds reference from `res.get('company_id', env company)` calendar (`resource_calendar.py` L56–59); reference stored, editable compute (L93–96); compute only on calendars with a company (L158–161); rate non-stored, no clamp, 100 only when reference is empty/zero (L116–117, L250–256). Wording now conditional; new falsifiable case | **CLOSED** |
| A3-RSRC-D02 (R06 "stored") | PC-RSRC-R06R1 | "computed on read, not stored"; (b)/(c) sub-cases falsifiable | **CLOSED** |
| S-A (no runtime PR for REC-06/11/19/20/27/28) | PR-11..PR-15 → PC-RSRC-R11..R15 | Each item now has a runtime link with falsifiable fail; destructive R14 flagged isolated-only | **CLOSED** |
| S-B (NOT_APPLICABLE misapplied) | REC add. 3.3 | 7 items moved to UNCORROBORATED (6 named + REC-14 added by owner); NA retained only for ACL rows and declaration flags; NA 2 + UNC 33 = 35. *See residual R-RSRC-1 (MRRP not carried) — a rule-1 point outside S-B's wording* | **CLOSED** (for S-B as raised) |
| S-C (unconditional "material 7 h shift") | A2 4.1 Thailand bullet R1; REC add. 3.4 | Now "conditionally material", no affected caller identified in module, cross-module open | **CLOSED** |
| S-D (PC-RSRC-10 not independent) | PROOF §1, §5, §6 | Relabelled ILLUSTRATION; removed from PASS count (21 − 1); static basis for REC-09 is PC-RSRC-09 | **CLOSED** |
| S-E (PROOF did not record REC sha256) | PROOF header; REC add. 3.7 | Parent REC hashes + REC addendum hash recorded; new cases keyed to REC ids; parent ordering honestly left INCONCLUSIVE (cannot be repaired retroactively) | **CLOSED** (forward); parent ordering remains INCONCLUSIVE |
| S-F (literal code tokens in parent PROOF) | PROOF §5 reading table | Parent immutable; each token given an R1 paraphrase reading. Remediation's own new formula phrase adjudicated in section 7.2 | **CLOSED** (for the parent tokens) |
| S-G (predeclaration independence) | Not addressed (was INCONCLUSIVE, no action required) | Same structural condition recurs in R1 (disclosed) | **INCONCLUSIVE** (unchanged) |
| Non-blocking O-1..O-3 | — | No routing was required | n/a |

### 1.4 `resource_mail`

| Challenge | Remedy | A3 verification | Status |
|---|---|---|---|
| M-A (exposure list incomplete: avatar, linked-user reference) | A2 O-01-R1/F-01-R1; REC-RMAIL-06 R1; PR-03R1; PC-RMAIL-07, R03R1 | `user_id` reference (`resource_resource.py` L38); `avatar_128` plain non-stored compute copying the user's avatar (L39, L61–64); card method is a plain read of the caller's list (`resource_mail` L17–18). Restricted-user variant added | **CLOSED** |
| M-B (REC-RMAIL-02 label; REC-hash lineage) | REC add. 4.2; PROOF header | Relabelled UNCORROBORATED; NA 1 + UNC 6 = 7; REC hash recorded | **CLOSED** (see R-RSRC-1 for the separate MRRP point) |
| N-1 precision ("session's active companies or no company") | REC-RMAIL-06 R1 | Adopted | **CLOSED** |

**Summary:** of all sustained original challenges, none is OPEN. One is PARTIALLY CLOSED (REC-BUS-28 wording, residual R-BUS-1). S-G stays INCONCLUSIVE as before.

---

## 2. Dispute adjudication (from source)

### 2(a) REC-BUS-28 — "delay up to ~50 s" (A3) vs "delivered at the next trigger; loss only if none before GC" (remediation)

Source facts (A3 re-read):
1. On a dispatcher loop exception the thread logs, sleeps for the 50 s constant, and re-enters the loop, which re-LISTENs (`bus.py`@60bf05a6 L25, L240–245, L261–269).
2. Only two things request a socket dispatch: the dispatcher's NOTIFY handling (`bus.py` L247–259) and `subscribe` (`websocket.py`@ca7ff5d7 L390–398; reached from `ir_websocket.py` L68). A module-wide grep finds no other caller of the trigger.
3. The socket event loop's 15 s selector timeout only drives keep-alive, frame-response timeout and ping (`websocket.py` L343–372, L824). There is no table re-poll.
4. The dispatch polls `id > last` excluding history, so a later-triggered poll *would* return the missed row (L771–773) — but only once something triggers it.
5. **Not cited by either side:** every socket has a hard keep-alive lifetime. The expiry is set once at construction to K plus a random 0–K/2 (`websocket.py` L843–846) and is never extended (`acknowledge_frame_receipt`/`_sent` only move the ping time, L849–863). On expiry the server closes the socket (L350–355). K is the framework config `websocket_keep_alive_timeout`, default 3600 s (`odoo/tools/config.py`@433ff84b L217). After a close, a client that reconnects sends `subscribe`, which dispatches (fact 2). Client reconnection logic is in JS and was not read.

**Ruling:**
- **A3's "delay of up to ~50 s" is REFUTED.** It assumed a dispatch follows the re-LISTEN; source shows no such dispatch (facts 2–3). The remediation's DISPUTE is **upheld** on this point.
- **The remediation's replacement is substantively right but overstated in one respect.** "The delay is not bounded by the module … becomes loss only if no trigger arrives before GC retention expires" omits fact 5: the module itself forces every socket closed within 1–1.5 × K of opening (3600–5400 s at the framework default). For a client that reconnects (JS, not read), the missed row is delivered at reconnect, well inside the 24 h GC horizon. Loss therefore needs a client that does not reconnect, or a non-default K large enough to approach retention. → residual **R-BUS-1 (LOW; A2 OM-B08-R1 / REC-BUS-28 R1 wording; PROOF PC-BUS-22 design)**.
- PC-BUS-21 **PASS stands**: its FAIL_IF ("periodic re-poll or dispatch not driven by a trigger; or replay of missed NOTIFYs after re-LISTEN") is not met, because a keep-alive close is not a dispatch, and reconnect-plus-subscribe is a trigger. The predicate is incomplete, but the verdict is correct.
- PC-BUS-22 Case A ("N1 not delivered within 120 s") could give a false FAIL if the socket's keep-alive expiry falls inside the 120 s window. The runtime pack must record K and the socket's open time, or show that more than 120 s of lifetime remain (part of R-BUS-1).

### 2(b) N3 — does the cached weekday lookup have an in-module caller? (PC-RSRC-24b FAIL)

Source facts: the works-on-date helper calls the cached lookup (`resource_calendar.py`@335a8576 L943–951, call at L946). The lookup is cached per calendar id (L1011–1018). A3 grepped every Python model file of the module: the 5 already fetched plus `res_users.py`, `resource_mixin.py` and `utils.py`, fetched now and listed by `models/__init__.py`. The lookup has exactly one caller (L946). The works-on-date helper has **no** caller in any of the 8 model files (private method; other modules were not read).

**Ruling: the remediation is RIGHT.** The S2 supplement's N3 sub-statement "It has no caller in the module files" is false. PC-RSRC-24b was predeclared from A3's wording (sealed file line 44, FAIL_IF "a caller exists in the module files"), and its **FAIL is correctly executed and correctly preserved**. The rest of N3 is confirmed by PC-RSRC-24a (no section or break filter; section rows default to Monday, attendance L23; break rows are `day_period` "lunch", L35–37). The lookup is **reachable only through a helper that is itself uncalled within the module**, so the effect is latent inside `resource` and matters only to downstream consumers. PR-18/R18 correctly uses a harness call. Ledger note (not a defect): this FAIL refutes a *challenger* sub-statement. It is not a failure of any A1/REC claim, and it should not be read as a module-level static failure.

---

## 3. Framework fact: session cookie attributes (`odoo/http.py`@ebfc2ac8, blob MATCH)

| Location | Finding |
|---|---|
| L2187–2194 (session save on the request path) | Session cookie set through `future_response.set_cookie` with the session id, max-age from session inactivity, and HttpOnly true. No SameSite and no Secure argument is passed |
| L2521–2523 (session-expired handling) | Session cookie reset on a redirect response with max-age and HttpOnly only |
| L1597–1609 (`Response.set_cookie`, used by the L2523 path) | Defaults: `secure` off, `samesite` none; passed through to the base response cookie setter. Also defaults expiry to one year when none is given |
| L1783–1790 (`FutureResponse.set_cookie`, which **L2189 actually calls**) | Same defaults (secure off, samesite none) |

**VERIFIED:** at the anchor the session cookie is **HttpOnly, with no explicit SameSite attribute and no Secure flag**. PC-BUS-23 PASS is correct. Precision note (R-BUS-3, non-blocking): the addenda cite L1597/L1609 as "the cookie helper" for both paths. The request-path save (L2189) goes through the FutureResponse helper at L1783–1790. The defaults are identical, so the fact is unaffected. Browser cross-site delivery (browser defaults, proxy rewriting) remains runtime (PC-BUS-08R1(b)).

---

## 4. Re-execution, relabels and totals

### 4.1 New static cases re-executed by A3 (at least 2 per module)

| Case | A3 re-execution against source (paraphrase) | Predicate | Result |
|---|---|---|---|
| PC-BUS-11R1 | As in 1.1 D-BUS-01. Retry constructs are only inbound-event and lifecycle transaction retries (`websocket.py` L724, L932); no ack or redelivery | Adequate, falsifiable | **UPHELD PASS** |
| PC-BUS-19 | Broadcast and full group set always appended; partner only with a session uid; no-uid env switched to the public user; routes are public auth with CORS `*` (`ir_websocket.py` L23–28, L75–83; `controllers/websocket.py` L11, L31) | Adequate | **UPHELD PASS** |
| PC-BUS-21 | See 2(a) | Incomplete (omits keep-alive lifetime); verdict unaffected | **UPHELD PASS** (with R-BUS-1) |
| PC-BUS-23 | See section 3 | Adequate | **UPHELD PASS** |
| PC-DGST-21 | Exception type only at L12/L231; send path queues `mail.mail` under sudo (L222); no direct send in `models/` or `controllers/` | Adequate | **UPHELD PASS** |
| PC-DGST-22 | Loop at L149–154 with no filter; UI domain L27; `res_users.py` create-only extension filtering share at creation | Adequate | **UPHELD PASS** |
| PC-RSRC-08R1 | See 1.3 D01 | Strong (four independent falsifiers) | **UPHELD PASS** |
| PC-RSRC-23 | Calendar-level call appends an empty resource and admits calendar-less leaves (L513–515); the company guard fires only when the resource is non-empty (L535) | Adequate | **UPHELD PASS** |
| PC-RSRC-24a / 24b | See 2(b) | Adequate / deliberately adversarial | **UPHELD PASS / UPHELD FAIL** |
| PC-RSRC-26 | Leaving two-week mode clears the flag, unlinks rows, switches duration-based off, reloads defaults (L306–310) | Adequate | **UPHELD PASS** |
| PC-RSRC-28 | Overlap intervals built on one continuous weekly scale combining weekday and hour, with no per-day grouping and no clamp before the check (L615–625) | Adequate | **UPHELD PASS** |
| PC-RMAIL-07 | See 1.4 M-A | Adequate | **UPHELD PASS** |

Also spot-confirmed from source without full re-execution: PC-RSRC-22 (global-leave compute fires on any company change incl. to empty, L202–208, versus the attendance compute requiring a non-empty company, L174; leave calendar link declares no delete rule, leaves L39–44) and PC-RSRC-25 (fallback reads company on the whole recordset before the loop, leaves L63–67). Both **UPHELD**.

### 4.2 Relabels and ledger arithmetic

| Relabel | Handling in the PROOF §6 ledger | A3 check |
|---|---|---|
| PC-BUS-16 → MEASUREMENT | Counted inside "Runtime NOT-EXECUTED 11 (of which MEASUREMENT 1)"; not counted as proof; REC-BUS-17 kept UNKNOWN_PENDING_PROOF (REC add. 1.2) | **Correct** |
| PC-DGST-04 → MEASUREMENT | Same pattern: 11 (1); REC-DGST-04 kept UNKNOWN_PENDING_PROOF (REC add. 2.2) | **Correct** |
| PC-RSRC-10 → ILLUSTRATION | Separate ILLUSTRATION column (1); removed from static PASS (21 − 1 = 20, + 8 new PASS = 28) | **Correct** |

Arithmetic recomputed by A3:
- bus static PASS 12 = parent 9 − superseded 2 (11, 17) + 5 new. bus runtime 11 = parent 9 − 4 superseded + 4 R1 + 2 new.
- digest static 12 = 10 + 2. digest runtime 11 = 10 − 3 + 3 + 1.
- resource static PASS 28, FAIL 1, ILLUSTRATION 1. resource runtime 22 = 10 − 1 + 1 + 12.
- resource_mail static 7, runtime 3.
- Addendum executed static cases: 5 + 2 + 9 + 1 = 17 (16 PASS, 1 FAIL). New runtime cases: 6 + 4 + 13 + 1 = 24.

All equal the PROOF addendum. No UNKNOWN_PENDING_PROOF item was closed, and none could be without runtime.

### 4.3 N1–N7 → REC-RSRC-29..35

Mapping verified one-to-one: N1→29, N2→30, N3→31, N4→32, N5→33, N6→34, N7→35. Each item is UNKNOWN_PENDING_PROOF, has a static case (PC-RSRC-22..28, with 24a/24b for N3) and a runtime case (R16..R22), and each static basis was confirmed from source (sections 2(b) and 4.1). N6 correctly supersedes parent refinement R1: `tz` is set after the skip test at L534–537, so it is the first *matching* pair. Resource counts are 7 + 11 + 1 + 16 = 35. STD-QID lineage adds no new QID. REC-31 has no clear fit, which is acceptable.

---

## 5. Residual defects (all LOW; none reverses a class or an A1 WHAT)

| ID | Module | Owner | Residual | Required action |
|---|---|---|---|---|
| R-BUS-1 | bus | A2 (OM-B08-R1), REC (REC-BUS-28 R1), PROOF (PC-BUS-22) | "Not bounded by the module … loss only if no trigger before GC" omits the module's forced keep-alive close. At the framework default (3600 s) that close falls within 1–1.5 × K, so for a reconnecting client the missed row is delivered on reconnect (section 2(a) fact 5) | Reword to: "bounded in practice by the socket's remaining keep-alive lifetime when the client reconnects (client behaviour not read); loss requires no reconnect/trigger before GC". Before running PC-BUS-22, record K and the socket open time, or ensure more than 120 s of remaining lifetime in Case A |
| R-BUS-2 | bus | REC | Rule-3 scan not evidenced: the "no evidence yet" list still includes **Q021** (duplicate subscription requests do not multiply delivery). Upstream C18 and Lane A #12 (per-socket dispatched-id history that de-duplicates) are topically relevant. No all-item-class scan is recorded | Re-scan the 6 remaining QIDs against all A1 item classes (C/BR/X/H/CRQ) and Lane A items; lineage only |
| R-BUS-3 | bus | A2 / PROOF | Cookie-helper citation covers the Response helper (L1597–1609) but not the FutureResponse helper actually used at L2189 (L1783–1790) | Add L1783–1790 to the citation. No verdict change |
| R-RSRC-1 | resource, resource_mail | REC | C1-B rule 1 ("preserve A2 label"): the parent A2 reviews for both modules label their runtime proof requirement sets (resource PR-01..PR-10; resource_mail PR-01..PR-03) as `MISSING_REQUIRED_RUNTIME_PROOF` (A2 section 7 headings). REC R1 maps runtime-linked items only to UNCORROBORATED or NOT_APPLICABLE. It does not apply the R1 label rule it stated for bus ("A2's class is carried unchanged"). The original A3 and S2 did not raise this | Carry MISSING_REQUIRED_RUNTIME_PROOF for REC items whose proof link is an A2 runtime-only PR (and for the new PR-11..22 items if A2 so classes them). Lineage/label only |
| R-RSRC-2 | resource | A2 (addendum) | Clean-room: the A2 addendum's own N7 text contains the formula phrase "day index × 24 + hour" (section 4.4) while the same file states "no … expressions reproduced". See 7.2 | Non-blocking. The PROOF §5 reading note is accepted as remedy. Future addenda should use the paraphrase |

---

## 6. Process rules and MASTER decisions (per addendum)

Timing context: C1-B rules committed at 15:20:45Z. Batch-2 source fetch at 15:21:21Z. A2 addendum at 15:28Z. REC addendum at 15:30Z. Predeclaration sealed at 15:31:46Z. Execution from 15:31:57Z to 15:32:18Z. MD-04..06 committed at 15:32:39Z. PROOF addendum written at 15:34Z. As instructed, MD-05's compliance-table requirement is judged on content, because batch 2 was dispatched before it.

| Rule | A2 addendum | REC addendum | PROOF addendum |
|---|---|---|---|
| C1-B 1: preserve A2 MRRP label | n/a | **MET** for bus/digest (restored). **NOT MET** for resource/resource_mail (R-RSRC-1) | n/a |
| C1-B 2: tag post-declaration text | n/a | n/a | **MET on content** (§4 marks all parent additions; tag literal "POST-PREDECLARATION TEXT" differs from `POST-DECLARATION`). The addendum's own §2 observations stay inside predeclared predicates. The result annotations are verdict qualifiers, not new Expected text |
| C1-B 3: scan all A1 item classes for no-evidence lists | n/a | **NOT EVIDENCED**: challenged QIDs corrected, but no all-class scan recorded; bus Q021 spot-check residual (R-BUS-2). digest not spot-checked by A3 | n/a |
| C1-B 4: REC frozen (sha256) before PROOF executes; PROOF records it | n/a | **MET**: REC add. mtime 15:30:38Z, before the seal (15:31:46Z) and execution (15:31:57Z). Its sha256 `18292fd3…` is in the predeclared file header and the PROOF header. REC cites forward PC IDs only, not PROOF results | **MET** (parent REC hashes and REC addendum hash recorded) |
| C1-B 5: cases sha256 + UTC timestamp written **before first source fetch** | n/a | n/a | **NOT MET (form)**: source fetched at 15:21:21Z, seal at 15:31:46Z. **Content mitigated**: disclosed. Every sampled predicate (11R1, 17R1, 19, 21, 23, DGST-21/22, RSRC-08R1/24a/28, RMAIL-07) traces to A2/REC addendum text sealed earlier. PC-RSRC-24b was deliberately predeclared from A3's wording and FAILed, which shows the pack was not tuned to pass. No shaping found. Structural cause: one controller performed owner-stage source re-derivation and PROOF (see MD-04) |
| MD-04: runtime executed by a different author when a single controller wrote the addenda | Applies: the PROOF disclosure shows the same controller re-derived for A2/REC and wrote PROOF | same | **OPEN for runtime**: the addenda do not assign a different runtime executor. Route to MASTER / Integration Control: all 24 batch-2 runtime cases, plus the 2 MEASUREMENT cases, must run under a different author |
| MD-05: rule-compliance table in each addendum | **Absent**. Pre-dates MD-05 (A2 15:28Z); content judged above | **Absent**. Pre-dates MD-05 (15:30Z) | **Absent**. Written 15:34Z, after the MD-05 commit, but within the same pre-MD-05 dispatch. Content judged above. Not a defect for batch 2; mandatory from batch 3 |
| MD-06: commit subject from committed file names; body lists paths | **MET** (`32b4275`: subject names all 4 files, body lists paths; bundled with 3 non-batch-2 A3 files, all listed) | **MET** (`efca765`, same pattern) | **MET** (`4ace7c3`, single file) |

Hygiene notes (non-blocking): H-1 is the uncited `remed_batch2/src/exec_log.txt` side file. H-2: the git author identity is shared across roles, so role attribution rests on headers and sha256 (per C1-B).

---

## 7. Clean-room re-scan

### 7.1 Scan
The three addenda and the sealed predeclaration contain no fenced code blocks, no decorators, no domains and no `Command`/tuple-command literals. They contain no percentages and no Formal Coverage claim, and no QID is answered. Identifiers appear only as evidence pointers. The PROOF §5 reading table satisfies S-F for the parent tokens without editing the parent.

### 7.2 Adjudication: retained descriptive formula phrase ("day index × 24 + hour", A2 addendum §4.4 N7; predeclared PC-RSRC-28 "day index x 24 + hour")
- **Nature:** it is a three-term arithmetic description of an hour-of-week scale that closely mirrors the shape of the source expression. It omits the source's epsilon offset and its identifiers. The concept (hours since the start of the week) is generic and discloses no vendor design, schema or workflow, so it is **not a clean-room leak of protected implementation**.
- **Consistency:** it is the same class of token that S-F sustained against the parent (the parity formula). It appears in an addendum that was remediating S-F, and in a file that states "no … expressions reproduced". That is an internal inconsistency.
- **Ruling:** **ACCEPTED WITH NOTE (LOW, non-blocking; R-RSRC-2).** The PROOF §5 consistency note ("weekday and hour combined on one continuous weekly scale") is an adequate remedy, because the A2 addendum is immutable. No re-issue is required. Downstream consumers must use the paraphrase, and the formula must not be carried into design artifacts.

---

## 8. Runtime-blocked items (NOT-EXECUTED; neither passed nor failed)

- bus: PC-BUS-02, 04, 06, 14, 16 (MEASUREMENT), 08R1, 10R1, 12R1 [INJ], 18R1, 20, 22 [INJ, see R-BUS-1].
- digest: PC-DGST-02, 04 (MEASUREMENT), 06, 12, 14, 18, 20, 08R1, 10R1 [INJ], 16R1, 23.
- resource: PC-RSRC-R01–R05, R07–R10, R06R1, R11–R22 (R14 destructive, isolated instance only).
- resource_mail: PC-RMAIL-R01, R02, R03R1.
- Every UNKNOWN_PENDING_PROOF item stays open: bus 5, digest 5, resource 16, resource_mail 3. The CONTRADICTIONs REC-BUS-18 and REC-RSRC-06 stay open, with the A2 side confirmed on source. Lane B remains absent: UNCORROBORATED or MRRP, never FAIL.
- MD-04 applies to executing this pack.

## 9. Final dispositions

| Module | Disposition |
|---|---|
| bus | **A3 R1 RE-CHECK: STATIC PASS WITH RESIDUAL DEFECTS (route A2 + REC + PROOF: R-BUS-1, R-BUS-2, R-BUS-3 — all LOW) — MASTER HANDOFF PENDING RUNTIME** |
| digest | **A3 R1 RE-CHECK: STATIC PASS — MASTER HANDOFF PENDING RUNTIME** (cross-module process items in section 6 routed to MASTER) |
| resource | **A3 R1 RE-CHECK: STATIC PASS WITH RESIDUAL DEFECTS (route REC: R-RSRC-1; note R-RSRC-2 — LOW) — MASTER HANDOFF PENDING RUNTIME** |
| resource_mail | **A3 R1 RE-CHECK: STATIC PASS WITH RESIDUAL DEFECTS (route REC: R-RSRC-1 — LOW) — MASTER HANDOFF PENDING RUNTIME** |

Cross-module routing to MASTER / Integration Control: C1-B rule 5 not met in form (content mitigated); MD-04 different-author runtime execution to be assigned; the MD-05 compliance table is mandatory from batch 3.

## 10. Limitations

- Static only. Not read: client JS (reconnect behaviour), PostgreSQL NOTIFY retention, pre-commit hook ordering, `with_company` narrowing, one-to-many clear semantics, the singleton rule, browser cookie defaults. Conclusions that depend on them are marked.
- Callers of the works-on-date helper in other addons were not searched (out of module scope).
- The GitHub tree API was not used. Module file completeness for `resource/models` rests on `models/__init__.py`.
- No percentages, no Formal Coverage claim, no QID answered. Git was used read-only. No input was edited. Clean room: paraphrase and pointers only.
- Scratch: `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/a3r1_b2/` (`src/`, `extra/`, `blobs.txt`, `intake.sha256`).
