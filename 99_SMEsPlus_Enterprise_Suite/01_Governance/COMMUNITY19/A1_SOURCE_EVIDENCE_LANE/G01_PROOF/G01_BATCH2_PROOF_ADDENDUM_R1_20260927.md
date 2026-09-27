# G01 PLATFORM_BASE — RED TEAM Proof Addendum R1 (A3 remediation, batch 2) — `bus`, `digest`, `resource`, `resource_mail`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **PROOF**. This is an addendum only. All parent Proof files are immutable and were not edited |
| Group / Modules | G01 PLATFORM_BASE / `bus`, `digest`, `resource`, `resource_mail` |
| Date | 2026-09-27 |
| Parent Proof artifacts (sha256, unchanged since A3 intake; re-verified 2026-09-27T15:25Z) | `G01_PROOF/G01_BUS_PROOF_20260927.md` `d644fab63b0d237488e714f963de19768bcaa6c30d45edfe039df9c8e9dac2d7`; `G01_PROOF/G01_DIGEST_PROOF_20260927.md` `279e573c6484edf6387847394fa76377c49d48bc5503d5089a350c0008f7bec4`; `G01_PROOF/G01_RESOURCE_PROOF_20260927.md` `fd150aaf3e72454260994ef66f93a61f38a095a96ed0958da728ee4e21578e89`; `G01_PROOF/G01_RESOURCE_MAIL_PROOF_20260927.md` `c15b9e11994d2ffd6e291dda93b710f26de72920456523250360883c5d0078a6` |
| REC consumed (S-E: recorded explicitly) | Parent REC: bus `251c8a2ad06918477e4c9b9c8c52093fa95f0484ffa0db1cc5f558fe5f20e4bc`; digest `6744994d045efe9306665256b9d437f73ed0e7720d8e88302d6032c4c4192ee5`; **resource `e2adc10a1f346bb5dc1fe73100d3187c485a1208c12af6bc3a4732475a0fe259`**; **resource_mail `1ec90af273af437692663390db5e4d182cf4490204385dbf67d25fefed8cb26f`**. REC addendum `G01_RECONCILIATION/G01_BATCH2_REC_ADDENDUM_R1_20260927.md` `18292fd3418f26152330446fc20080f4fd453a04c3555c1932807652e56c5331` |
| A2 input | Parent A2 reviews (hashes in the A2 addendum section 0.1). A2 addendum `G01_A2_REVIEWS/G01_BATCH2_A2_ADDENDUM_R1_20260927.md` `9664c13e01c777e4731381966a412b4a9eea675168ec5ad4f848c56d0a6a037c` |
| A3 reports (sha256) | bus `4f9c2676bfe15588479686392e4ec9520e26ab6b56ea90b9920ef613ef3209b6`; digest `2eae23cddf02d14bb5ad47fd19890be5150733088ed332271e7daab8f31360a4`; resource `50894e31e50ad78ad88bbec72a0d0bb218bcdd38b30832f7e5dedd79675dab52`; resource_mail `1c570f56bb35bab9375be2c1cc287c4c3eb90bd5137e05181a0b9a49231d7a4a`; supplement S2 (MASTER-registered) `25c154b36361ba549f8ac4f8edd34dc6f0f70d7f7723b290499c2ccad908edb1` |
| Challenge IDs addressed (PROOF parts) | **bus:** D-BUS-01 (PC-BUS-11/12), D-BUS-02 (PC-BUS-17/18), D-BUS-05 (new cases), D-BUS-06 (PC-BUS-08), D-BUS-07, and the A3 1.2 PC-BUS-16 note. **digest:** D-DGST-01 (new cases), D-DGST-04 (PC-DGST-10/16), D-DGST-05, and the A3 1.2 PC-DGST-04 note. **resource:** A3-RSRC-D01 (PROOF part), A3-RSRC-D02, S-A (cases), S-D, S-E, S-F, N1–N7 (cases). **resource_mail:** M-A (cases), M-B (hash lineage) |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`. 19 module files were re-fetched with `git hash-object`: **19 of 19 MATCH** the earlier recorded blobs. Two files were newly recorded: `odoo/http.py` `ebfc2ac8d268a45aaf4b8cde8c9ce8b480d58dbb` and `resource/views/resource_calendar_views.xml` `402890182cb087e7b649f29a42f0aef14e7ae923` (not relied on). Blob log: scratch `remed_batch2/blob_log.txt`, sha256 `6f021dc87742eb0daffabf02725c1ace253d0bf3659b88876c728ea0eeabbdfb` |
| **Predeclaration** | Scratch `remed_batch2/proof_addendum_R1_cases_predeclared.txt`, sha256 **`a93b7ed54369cda476b7676bbe6ca35add9bab7b1ab93af740d1aa6756a3d5f7`**, sealed **2026-09-27T15:31:46Z** (file mtime 15:31:42Z). It holds every new or replacement case (Expected and Fail conditions), written **before** execution. Disclosure: the controller had read the anchor source during the owner-stage re-derivation for the A2 and REC addenda. The predicates trace to those addenda and to the A3 text. One A3 statement was predeclared exactly as written (PC-RSRC-24b) so that it could fail |
| Execution | SOURCE/CONFIG only, 2026-09-27T15:31:57Z – 15:32:18Z. Log: scratch `remed_batch2/exec_log.txt`, sha256 `f82238049895756d7c180e5f0a808d560451f1a5a4ede4a47d1fc3fd3a138eb0` |
| Runtime device | OFFLINE. Every RUNTIME case is **NOT-EXECUTED**, and no runtime result is claimed |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

Clean-room note: neutral paraphrase only, with identifiers used as evidence pointers. No code, expressions or literal tokens are reproduced. No percentages. No Formal Coverage claim. No QID answered. No git operations. No existing artifact was edited.

---

## 1. Supersede map (old → new)

| Old case (parent) | New case (R1) | Reason | Old verdict status |
|---|---|---|---|
| PC-BUS-11 (SOURCE, PASS) | **PC-BUS-11R1** | D-BUS-01: the predicate now tests the mechanism (pre-commit id allocation, dispatch-time history, trimming only on a non-empty dispatch), not just a comment | Superseded. The parent PASS is kept in lineage and no longer counted |
| PC-BUS-12 (RUNTIME) | **PC-BUS-12R1** | D-BUS-01: declared injection between the pre-commit insert and commit, plus a control run. The invalid "delivered → at-least-once" inference is removed | Superseded (was NOT-EXECUTED) |
| PC-BUS-17 (SOURCE/CONFIG, PASS) | **PC-BUS-17R1** | D-BUS-02: adds the read path (own-DB cursor) and clear-text string channels in NOTIFY | Superseded. The parent PASS is not counted |
| PC-BUS-18 (RUNTIME) | **PC-BUS-18R1** | D-BUS-02: separates wake-up from content, and adds a raw-NOTIFY capture | Superseded |
| PC-BUS-08 (RUNTIME) | **PC-BUS-08R1** | D-BUS-06: adds a browser-originated cross-site variant | Superseded |
| PC-BUS-10 (RUNTIME) | **PC-BUS-10R1** | A3 §3: adds an anonymous caller with an arbitrary string channel | Superseded |
| PC-BUS-16 (RUNTIME) | PC-BUS-16 **re-labelled MEASUREMENT** | A3 1.2: no fail condition, so it cannot count as proof | Label change only |
| — | **PC-BUS-19** (SOURCE), **PC-BUS-20** (RUNTIME) | D-BUS-05: REC-BUS-25 proof requirement | New |
| — | **PC-BUS-21** (SOURCE), **PC-BUS-22** (RUNTIME) | D-BUS-05: REC-BUS-28 (delay without a module bound) | New |
| — | **PC-BUS-23** (CONFIG/SOURCE, framework) | D-BUS-06: session-cookie attributes at the anchor | New |
| PC-DGST-10 (RUNTIME) | **PC-DGST-10R1** | D-DGST-04: declared fault injection plus a control run | Superseded |
| PC-DGST-16 (RUNTIME) | **PC-DGST-16R1** | D-DGST-04: disjunctive expectation | Superseded |
| PC-DGST-08 (RUNTIME) | **PC-DGST-08R1** | A3 §3: also records serialized window strings | Superseded |
| PC-DGST-04 (RUNTIME) | PC-DGST-04 **re-labelled MEASUREMENT** | A3 1.2 | Label change only |
| — | **PC-DGST-21** (SOURCE) | D-DGST-04: unreachable catch recorded as a finding | New |
| — | **PC-DGST-22** (SOURCE), **PC-DGST-23** (RUNTIME) | D-DGST-01: REC-DGST-27 | New |
| PC-RSRC-08 (SOURCE, PASS), **for REC-24 only** | **PC-RSRC-08R1** | D01: a falsifiable test of the conditional rate-100 statement | PC-RSRC-08 stays PASS for REC-08. For REC-24 it is superseded by 08R1 |
| PC-RSRC-R06 (RUNTIME) | **PC-RSRC-R06R1** | D02 ("stored" was wrong) and D01 (company-less seeding) | Superseded |
| PC-RSRC-10 (SOURCE+stdlib, PASS) | PC-RSRC-10 **re-labelled ILLUSTRATION** | S-D: no independent source evidence | **Removed from the PASS count** |
| — | **PC-RSRC-R11..R15** (RUNTIME) | S-A: REC-06, 11, 19, 20, 27, 28 | New |
| — | **PC-RSRC-22, 23, 24a, 24b, 25, 26, 27, 28** (SOURCE); **PC-RSRC-R16..R22** (RUNTIME) | N1–N7 (REC-RSRC-29..35) | New |
| Parent refinement R1 (calendar L537) | **PC-RSRC-27 / R21** | N6 precision: the first **matching** pair, not the first resource | The refinement text is superseded |
| PC-RMAIL-R03 (RUNTIME) | **PC-RMAIL-R03R1** | M-A: adds the avatar image, the linked-user reference and a restricted-user variant | Superseded |
| — | **PC-RMAIL-07** (SOURCE) | M-A | New |

---

## 2. New and replacement SOURCE/CONFIG cases: executed

Expected and Fail conditions are as predeclared (sha256 `a93b7ed5…d5f7`). Evidence is given as file @ blob : lines and is paraphrased.

| Case | REC / PR | Evidence | Observation | Result |
|---|---|---|---|---|
| PC-BUS-11R1 | REC-BUS-18, 24 / PR-BUS-06R1 | `bus/models/bus.py`@60bf05a6 : 111–168; `bus/websocket.py`@ca7ff5d7 : 767–798 | The send call only appends values to pre-commit data and the channel to a post-commit set. The row insert, and so the id, runs in a pre-commit callback. NOTIFY runs in a post-commit callback. History entries are stamped with the dispatch time. The dispatch returns early when no rows come back, so trimming and last-id advance happen only on a non-empty dispatch. The only retry constructs in the file are transaction retries for inbound events and lifecycle callbacks (L724, L932). There is no acknowledgement or redelivery | **PASS** |
| PC-BUS-17R1 | REC-BUS-21 / PR-BUS-09R1 | `bus/models/bus.py` : 58–85, 121, 133, 152–168, 170–190, 210–259; `bus/websocket.py` : 767–773 | NOTIFY goes to the maintenance-DB connection on one fixed channel, and the dispatcher LISTENs there. The wake-up map is keyed by DB-prefixed channel keys. A woken socket dispatches with a cursor on its own session DB, and the poll rebuilds keys with its own DB name and searches its own table. The NOTIFY payload is a serialized list of the full channel keys, including client string channels | **PASS** |
| PC-BUS-19 | REC-BUS-25 / PR-BUS-10 | `bus/models/ir_websocket.py`@538b3a63 : 23–28, 81–83; `bus/controllers/websocket.py`@155153e4 : 11, 31 | Broadcast and the env user's full group set are always appended. The partner is appended only when a session uid exists. A no-uid socket's env is switched to the public user. The socket and polling routes are public auth | **PASS** |
| PC-BUS-21 | REC-BUS-28 / PR-BUS-11 | `bus/models/bus.py` : 25–26, 97–108, 238–269; `bus/websocket.py` : 343–372, 390–411, 747–748, 824 | A loop exception logs, sleeps for the 50 s constant, then re-enters the loop and re-LISTENs. Dispatch is requested only by subscribe and by the dispatcher's NOTIFY handling. The event loop's timer covers keep-alive, ping and timeouts only, with no re-poll. The poll is reached only from dispatch and from the polling route. Rows persist until GC | **PASS** |
| PC-BUS-23 | REC-BUS-14 / PR-BUS-04R1 | `odoo/http.py`@ebfc2ac8 : 1597–1609, 2187–2194, 2523 | The session cookie is set on the session-save path and the session-expiry path with HttpOnly and max-age only. The cookie helper's SameSite default is "not given" and its Secure default is off. No explicit SameSite or Secure attribute is set for the session cookie at the anchor | **PASS** (framework, static. Browser behaviour is runtime: PC-BUS-08R1) |
| PC-DGST-21 | REC-DGST-09, 23 / PR-DGST-05R1 | `digest/models/digest.py`@3eea1c39 : 12, 130–157, 194–232 | The mail-delivery exception type appears only in the import and in the cron catch. The send path only creates mail records under elevated rights, and the module search found no direct send call. **Finding:** the catch is effectively unreachable on the module's own path | **PASS** |
| PC-DGST-22 | REC-DGST-27 / PR-DGST-11 | `digest/models/digest.py` : 27, 149–154; `digest/models/res_users.py`@44884554 : 9–19 | The send loop walks every recipient with no share or active filter. The recipient restriction is a field-level domain only. The only users extension is the create-time auto-subscribe, which filters share users at creation. The module has no constraint or write hook on user type | **PASS** |
| PC-RSRC-08R1 | REC-RSRC-08, 24 / PR-06R1 | `resource/models/resource_calendar.py`@335a8576 : 56–59, 93–96, 116–117, 158–161, 250–256 | (a) The default hook seeds the reference hours from the default (session, unless given) company's calendar. (b) The reference is a stored, editable compute. (c) That compute processes only calendars with a company and assigns nothing to company-less ones. (d) The rate field has no store flag and no clamp, and it is 100 only when the reference is empty or zero | **PASS** |
| PC-RSRC-22 | REC-RSRC-29 / PR-16 | calendar : 172–174, 202–208; `resource_calendar_leaves.py`@841053e6 : 39–44 | The global-leave compute runs for new records and for any company change, including to empty, and rebuilds from the new company's default calendar. The attendance compute requires a non-empty new company for existing records. The leave's calendar link declares no delete rule | **PASS** (deletion or orphaning is framework behaviour: R16) |
| PC-RSRC-23 | REC-RSRC-30 / PR-17 | calendar : 511–515, 535 | A calendar-level call adds an empty resource. The calendar term admits calendar-less leaves. The company guard applies only when a resource is set | **PASS** |
| PC-RSRC-24a | REC-RSRC-31 / PR-18 | calendar : 1011–1018; attendance @d8fb69b1 : 23, 46 | The cached lookup marks every attendance row as worked for its (week type, weekday), with no section or break filter, and caches on the calendar id only. Section rows default to Monday | **PASS** |
| PC-RSRC-24b | REC-RSRC-31 / PR-18 | calendar : 943–951 (caller), 1012 | **Predeclared from A3 N3 as written ("no caller in module files").** The works-on-date helper calls the cached lookup, so a caller exists in the module files. That helper itself has no caller in the fetched module files | **FAIL** (preserved. A3 N3's sub-statement is refuted. REC-RSRC-31 already carries the precision) |
| PC-RSRC-25 | REC-RSRC-32 / PR-19 | leaves : 63–68 | When neither a user tz nor a context tz is set, the fallback reads the company on the whole recordset before the per-record loop | **PASS** (the singleton effect is runtime: R19) |
| PC-RSRC-26 | REC-RSRC-33 / PR-20 | calendar : 306–310 | Leaving two-week mode clears the flag, unlinks the rows, switches duration-based off and reloads the defaults | **PASS** |
| PC-RSRC-27 | REC-RSRC-34 / PR-21 | calendar : 529–552 | The tz variable is assigned inside the nested loop after the skip test and is not reset, so it persists for later pairs. Clipping compares timezone-aware values. Flexible-leave widening receives values in that tz | **PASS** |
| PC-RSRC-28 | REC-RSRC-35 / PR-22 | calendar : 615–625 | Each row becomes an interval on one continuous weekly scale that combines weekday and hour, with no per-day grouping and no hour clamp before the check | **PASS** |
| PC-RMAIL-07 | REC-RMAIL-06 / PR-03R1 | `resource/models/resource_resource.py`@aad3af2f : 38–42, 61–64; `resource_mail/models/resource_resource.py`@797be7bd : 15–18 | The resource has a linked-user reference field. The avatar image is a non-stored plain compute that copies the linked user's avatar and is not related. The avatar-card method returns a plain read of the caller's list | **PASS** |

**Static totals for this addendum:** 17 executed. **16 PASS, 1 FAIL** (PC-RSRC-24b). No case was blocked, and no blob mismatch occurred.

---

## 3. New and replacement RUNTIME cases: NOT-EXECUTED (device OFFLINE)

Full Expected and Fail text is in the predeclaration file. Procedures follow the A2 addendum PRs. Declared harness injection is marked **[INJ]**.

| Case | REC / PR | Summary of Expected (predeclared) | Status |
|---|---|---|---|
| PC-BUS-08R1 | REC-BUS-14 / PR-BUS-04R1 | (a) as parent. (b) Browser-originated: record the cookie attributes received, whether the cookie was sent on the handshake, and the resulting identity, per browser | NOT-EXECUTED |
| PC-BUS-10R1 | REC-BUS-09, 22 / PR-BUS-05R1 | As parent, plus: an anonymous socket or poll with an arbitrary string channel and last id 1 gets retained rows older than 50 s | NOT-EXECUTED |
| PC-BUS-12R1 **[INJ]** | REC-BUS-18, 24 / PR-BUS-06R1 | T1 is held after the pre-commit insert and before commit and is never delivered. A control run without injection delivers it. A delivery ≠ at-least-once | NOT-EXECUTED |
| PC-BUS-18R1 | REC-BUS-21 / PR-BUS-09R1 | No DB2 wake-up on DB1 keys. No DB1 content on DB2. The raw NOTIFY shows the DB1 keys, including string channels | NOT-EXECUTED |
| PC-BUS-20 | REC-BUS-25 / PR-BUS-10 | An anonymous socket or poll receives broadcast and public-group notifications | NOT-EXECUTED |
| PC-BUS-22 **[INJ]** | REC-BUS-28 / PR-BUS-11 | Case A: N1 is not delivered within 120 s with no further trigger. Case B: N1 is delivered together with N2 | NOT-EXECUTED |
| PC-DGST-08R1 | REC-DGST-07, 26 / PR-DGST-04R1 | As parent, plus the serialized window strings are recorded | NOT-EXECUTED |
| PC-DGST-10R1 **[INJ]** | REC-DGST-09, 23 / PR-DGST-05R1 | Under injection, the rerun duplicates the mail to the first recipient and the digest stays due. A control run queues once | NOT-EXECUTED |
| PC-DGST-16R1 | REC-DGST-20 / PR-DGST-08R1 | Labels and currency are B, and the value is **either** A's **or** zero or restricted by rule. Record which | NOT-EXECUTED |
| PC-DGST-23 | REC-DGST-27 / PR-DGST-11 | A recipient converted to share user still gets a digest queued | NOT-EXECUTED |
| PC-RSRC-R06R1 | REC-RSRC-08, 24 / PR-06R1 | (a) 150, computed on read and not stored. (b) A company-less calendar gets a seeded reference, and the rate is hours ÷ reference. (c) With a zero or empty reference, the rate is 100 | NOT-EXECUTED |
| PC-RSRC-R11 | REC-RSRC-06, 19 / PR-11 | RPC no-section and section-first variants are saved. The form rejects the no-section edit | NOT-EXECUTED |
| PC-RSRC-R12 | REC-RSRC-19 / PR-12 | An untyped overlapping row is saved and counted as first-week only | NOT-EXECUTED |
| PC-RSRC-R13 | REC-RSRC-11, 20 / PR-13 | A calendar-less company leave removes day D on both calendars | NOT-EXECUTED |
| PC-RSRC-R14 | REC-RSRC-27 / PR-14 | No holiday propagation. Toggles replace slots. A company change replaces leaves (destructive; isolated instance) | NOT-EXECUTED |
| PC-RSRC-R15 | REC-RSRC-28 / PR-15 | Admin denied on another user's personal leave. The implication is recorded. Plan-days ignores the resource leave | NOT-EXECUTED |
| PC-RSRC-R16 | REC-RSRC-29 / PR-16 | Record whether the leaves are deleted or orphaned, and the effect on other calendars | NOT-EXECUTED |
| PC-RSRC-R17 | REC-RSRC-30 / PR-17 | A cross-company calendar-less leave is subtracted at calendar level | NOT-EXECUTED |
| PC-RSRC-R18 | REC-RSRC-31 / PR-18 | Monday is reported as worked because of the section rows (harness call) | NOT-EXECUTED |
| PC-RSRC-R19 | REC-RSRC-32 / PR-19 | A batch create with no tz raises a singleton-type error | NOT-EXECUTED |
| PC-RSRC-R20 | REC-RSRC-33 / PR-20 | Duration-based is off after leaving two-week mode | NOT-EXECUTED |
| PC-RSRC-R21 | REC-RSRC-34 / PR-21 | Instants are correct. The output tz is the first matching pair's. Flexible widening uses that tz | NOT-EXECUTED |
| PC-RSRC-R22 | REC-RSRC-35 / PR-22 | A cross-day collision raises the overlap error | NOT-EXECUTED |
| PC-RMAIL-R03R1 | REC-RMAIL-04, 06, 07 / PR-03R1 | As parent, plus the avatar and reference, and a restricted-user variant recorded | NOT-EXECUTED |

Runtime totals for this addendum: **24 new or replacement cases, all NOT-EXECUTED.** In addition, PC-BUS-16 and PC-DGST-04 are MEASUREMENT cases and remain NOT-EXECUTED.

---

## 4. D-BUS-07 / D-DGST-05: Expected text that exceeded the predeclared cases (marked)

These phrases in the **parent** Proof "Expected" column are **not** in the predeclared TSV (`rec_bus_dgst/predeclared_proof_cases.tsv`, sha256 `a6f20632b142c60377ecf4b245e52ee36ebd630e48dc7caf51e000689119fe16`). They are now marked **POST-PREDECLARATION TEXT**. The verdict is judged against the TSV text only. Fail conditions were unchanged, so no verdict changes.

| Case | Phrase added after predeclaration (paraphrased) | Nature |
|---|---|---|
| PC-BUS-01 | "the partner … when a session uid exists"; "No allow-list or ownership check exists in the module" | Qualification; restates the fail condition |
| PC-BUS-03 | "user routes to its partner" | Additional fact |
| PC-BUS-05 | "Group membership is not recomputed" | Restatement |
| PC-BUS-07 | "to a **fresh** anonymous session" | Qualification |
| PC-BUS-09 | "the socket takes the client value once" | Additional fact |
| PC-BUS-11 | "if the target receives another notification meanwhile" | Additional condition (now superseded by 11R1) |
| PC-BUS-13 | "under elevated rights"; "so a rollback leaves neither" | Additional fact and inference |
| PC-BUS-15 | "Only inverse fields are filtered by field read access" | Additional fact |
| PC-BUS-17 | "Separation depends on the DB name inside each channel key, and payloads carry the channel identifiers" | Interpretive addition that carried the "solely" overstatement (now superseded by 17R1) |
| PC-DGST-05 | "The helper returns zero when no grouped row exists" | Additional fact (supports REC-DGST-21) |
| PC-DGST-13 | "declares no … CSRF parameter"; "for daily digests sent to ERP managers" | Additional facts |
| PC-DGST-15 | "so it takes the installing context"; "adds non-share users" | Qualification |

PC-DGST-01, 03, 07, 09, 11, 17 and 19 were checked, and their Expected text matches the TSV in substance.

---

## 5. `resource` S-D, S-E, S-F and D02

- **S-D:** PC-RSRC-10 is re-labelled **ILLUSTRATION**. It is arithmetic on a source rule with a tzdata fact, not independent source evidence, and it is removed from the PASS count. The static basis for REC-RSRC-09 is PC-RSRC-09. Its materiality is conditional (REC addendum 3.4).
- **S-E:** The REC sha256 values consumed are recorded in the header. The new cases are keyed to REC ids. For the **parent** Proof, whether REC was frozen before Proof stays **INCONCLUSIVE**, because the REC file was finalized after the parent's static execution window. This cannot be repaired retroactively.
- **D02:** the parent R06 Expected "150 shown/stored" is corrected. The rate is a non-stored compute (PC-RSRC-08R1 (d)), and R06 is superseded by R06R1.
- **S-F:** literal code tokens in the parent resource Proof are to be read as the following paraphrases. The parent is not edited.

| Parent case | Literal token in parent | Paraphrase (R1 reading) |
|---|---|---|
| PC-RSRC-06 | the fixed small start offset quoted as a decimal literal | "a very small fixed offset added to each start hour so contiguous slots are not treated as overlapping" |
| PC-RSRC-07 | the bounded loop quoted as a call expression | "a bounded search of one hundred successive 14-day windows" |
| PC-RSRC-05 | "12 ± duration", "12 − d / 12 + d" | "hours placed symmetrically around midday according to the duration, with no bound" |
| PC-RSRC-15 | the parity expression quoted as a formula | "the parity of the number of whole weeks elapsed since the calendar's epoch day, not the ISO week" |
| PC-RSRC-18 | the cache decorator and cache-clear call names | "cached per calendar id; no cache-clearing call found in the module files" |
| PC-RSRC-06 | week-type literal values | "rows typed first week or second week" |

Consistency note for this remediation's own documents: the A2 addendum phrase "day index × 24 + hour" (section 4.4, N7) and the scratch predeclaration phrase for PC-RSRC-28 are descriptive paraphrases. Read them as "weekday and hour combined on one continuous weekly scale". They are not reproduced code.

---

## 6. Effective case ledger after R1 (per module)

Superseded cases are kept in lineage but not counted. MEASUREMENT and ILLUSTRATION cases are not counted as proof.

| Module | Static PASS | Static FAIL | ILLUSTRATION | Runtime NOT-EXECUTED (of which MEASUREMENT) |
|---|---|---|---|---|
| bus | 12 (PC-BUS-01, 03, 05, 07, 09, 13, 15, 11R1, 17R1, 19, 21, 23) | 0 | 0 | 11 (1): PC-BUS-02, 04, 06, 14, 16 (MEASUREMENT), 08R1, 10R1, 12R1, 18R1, 20, 22 |
| digest | 12 (PC-DGST-01, 03, 05, 07, 09, 11, 13, 15, 17, 19, 21, 22) | 0 | 0 | 11 (1): PC-DGST-02, 04 (MEASUREMENT), 06, 12, 14, 18, 20, 08R1, 10R1, 16R1, 23 |
| resource | 28 (the parent 21 minus PC-RSRC-10, plus 08R1, 22, 23, 24a, 25, 26, 27, 28) | **1 (PC-RSRC-24b)** | 1 (PC-RSRC-10) | 22 (0): R01–R05, R07–R10, R06R1, R11–R22 |
| resource_mail | 7 (PC-RMAIL-01..07) | 0 | 0 | 3 (0): R01, R02, R03R1 |

Effect on REC items: no UNKNOWN_PENDING_PROOF item is closed, since that needs runtime. The CONTRADICTIONS (REC-BUS-18, REC-RSRC-06) stay open, with the A2 side confirmed on source. The new REC-RSRC-29..35 have their static basis confirmed, and REC-RSRC-31 carries the PC-RSRC-24b FAIL as a precision. No GAP is resolved in favour of A1.

## 7. A3 re-check surface

A3 may re-check now: the supersede map; the 17 executed cases (predicates, citations, the preserved FAIL); predeclaration integrity (sealed 15:31:46Z, before execution started at 15:31:57Z); the post-predeclaration markings; the S-F readings; and the two DISPUTED points carried from the A2 and REC addenda (REC-BUS-28 delay bound; N3 caller). Runtime outcomes remain blocked: no runtime prediction is proven.

## 8. Limitations

- Static only. Framework behaviour (commit-hook ordering, database NOTIFY retention, company narrowing, clear-command semantics, the singleton rule, browser cookie defaults) is routed to runtime.
- The controller read the source before writing the predeclaration (disclosed). Independence is at role level only.
- No runtime result is claimed or fabricated. No percentages, no Formal Coverage claim, no QID answered. No git operations. The parents are untouched.
