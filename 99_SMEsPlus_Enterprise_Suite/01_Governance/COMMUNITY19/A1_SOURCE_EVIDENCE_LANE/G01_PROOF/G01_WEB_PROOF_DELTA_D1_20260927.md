# G01 PLATFORM_BASE — RED TEAM PROOF DELTA D1 — `web`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | SMEsPlus PROOF controller — DELTA cycle D1, Stage 2 of a two-stage REC + PROOF delta run. Stage 1 is `G01_RECONCILIATION/G01_WEB_REC_DELTA_D1_20260927.md` |
| Group / Module | G01 PLATFORM_BASE / `web` |
| Date | 2026-09-27 |
| Nature | Delta addendum to `G01_WEB_PROOF_20260927.md`. The base proof is unedited, and base cases PC-WEB-01..28 keep their results, including **PC-WEB-11 FAIL** |
| Parent artifacts (sha256) | A1 DELTA D1 `bdf81cf5df68b405148c30bd030c174c3f23707beca86867c26e44338ad600c2`; A2 DELTA D1 review `3886d78cbeb90d5a3c1003ff5d65c7d0e4c6980ea278d338e338345db9554a5f`; Lane A PASS-2 `2ae1f05ee3d7e9e3cd5ca4b90c812048f1765a3dbc2ce2870f36cfc307adbc3a`; base REC `9e2a4a370ffb4e9a010e81633da1e85f0db4c2a762f8c26322ef38074e5abc2d`; base PROOF `a72724e8c7f1f5eb3b3f7707b511de3383b45b5b0b1f2d88e67db58771719d57`; REC DELTA D1 (this run, Stage 1) |
| Bank / freeze | W1-B01. Bank sha256 `259839a2c0f265b9519d23bad3b25b8d74dd5a89b9410e01d3560e0a42fcd558` equals the FREEZE_W1-B01 entry. Freeze hash `558ec88047aef5c8e7ea0e2675b1c43ef358ec29b172d6878068330f3fba7177` |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`. Every file was blob-verified with `git hash-object` before use (scratch only) |
| Runtime device | **OFFLINE**. No running instance, database, proxy or browser is available. RUNTIME cases are NOT-EXECUTED and ready to run. No master-password or DB-manager action was attempted against any host. Nothing is fabricated |
| **Disposition** | **PROOF DELTA PARTIAL — SOURCE/CONFIG EXECUTED (11 PASS / 0 FAIL), RUNTIME PENDING (9 NOT-EXECUTED)** |

Clean room: results are neutral statements of observed behaviour at one commit. Identifiers and ~L pointers are evidence pointers only. No vendor code is reproduced. No percentages. No Formal Coverage. No git operations on the repository. No input was edited.

## 1. Predeclaration record

| Item | Value |
|---|---|
| Cases file | `scratchpad/rec_web_d1/PROOF_CASES_WEB_D1_PREDECLARED.txt` |
| File mtime | **2026-09-27T15:18:51.54Z** |
| sha256 (recorded 15:19:01.02Z) | `352d0d550a18ddda9d5aa1aff86f15fd89d6902b19e81a3261fdda16049c067d` |
| Stamp file | `predeclare_stamp.txt` sha256 `8b72482147593d7d03c425a91338e74c7197a76c5721846833cef05af7718df9` |
| First source fetch | 2026-09-27T15:19:01Z, logged in `fetch_log.txt`, in the same command and after the stamp |
| Execution results log | `execution_results.txt` sha256 `432cd695b766f3c01bbf72c1312fbf3d4a85df81b95b0247f747f5dc2d4888ad` |

No case, expected result or fail condition was changed after execution. Section 3 reproduces the cases as declared, in paraphrase.

## 2. Source fetch and blob verification

| Path at anchor | HTTP | Recomputed blob | Recorded (PASS-2 / A2 D1) | Result |
|---|---|---|---|---|
| addons/web/controllers/binary.py | 200 | 7b7b84f771eeb5a0f096500f7530a48c956f41b1 | 7b7b84f7… | MATCH |
| odoo/tools/misc.py | 200 | 6d27505917a80a2cf9d3b3c6faa6bf8bca86acfd | 6d275059… | MATCH |
| addons/web/controllers/database.py | 200 | 434b915ceb3a935c1fdbee248d4a4ed7a8533b48 | 434b915c… | MATCH |
| odoo/tools/config.py | 200 | 433ff84b625a69e08cce9f42911aa608d3e615ee | 433ff84b… | MATCH |
| odoo/service/db.py | 200 | 63c314a72de738d044e542e32bc045c21f987531 | 63c314a7… | MATCH |
| odoo/http.py | 200 | ebfc2ac8d268a45aaf4b8cde8c9ce8b480d58dbb | ebfc2ac8… | MATCH |
| addons/web/controllers/pivot.py | 200 | a687d2d1dbd443c0b49c2e1b259a2dd2c9767bb1 | a687d2d1… | MATCH |
| addons/web/controllers/export.py | 200 | cb750f193c5548fe70a01422d644c66805a20e69 | cb750f19… | MATCH |
| odoo/addons/base/models/ir_attachment.py | 200 | 905ae118b8c8e5050fdc33eb1631c88e3926b888 | 905ae118… | MATCH |
| addons/web/controllers/home.py | 200 | 292aaa75a2c35b71acb3c97488a6dc2c96309c9f | 292aaa75… | MATCH |
| odoo/service/security.py | 200 | d332199c6178ea451535d0997473d7d6c8844c15 | d332199c… | MATCH |
| odoo/orm/models.py | 200 | 11f50c4e0b676fbb4b8a45e9703326946348ff98 | 11f50c4e… | MATCH |

All 12 files MATCH. Their content is kept in the scratchpad only.

## 3. Cases, execution and results

### 3.1 RUNTIME cases (PR-WD1..PR-WD8, plus the cache-public finding): NOT-EXECUTED, ready to run

Safety note for whoever runs these: PC-WEB-D-01..03 exercise the DB manager and the master secret. Run them only on a disposable, isolated instance that the operator owns, never on a shared or production host.

| Case | Source requirement / REC item | Preconditions and steps | Expected (source-predicted) | Fail | Result |
|---|---|---|---|---|---|
| PC-WEB-D-01 | PR-WD1; REC-WEB-D26 (D07), D39 (AO-W2) | Default secret, listing on, config file read-only. Unauthenticated create with secret S, then restart | Before restart S is accepted and the default refused, with a write error on stderr. After restart the default is accepted again | S survives the restart, or S is not adopted before the restart | **NOT-EXECUTED** (device offline) |
| PC-WEB-D-02 | PR-WD2; REC-WEB-D04 (CRQ-WEB-02 residual); base REC-WEB-29 | Secret hashed. 50 wrong-secret backup requests from one address straight to the app, then one correct request | All 50 refused with the same error. No lockout and no escalating delay beyond the hash cost. The correct request succeeds | A lockout, throttle or escalating delay is seen (record it; it refutes the negative) | **NOT-EXECUTED** |
| PC-WEB-D-03 | PR-WD3; REC-WEB-D29 (D10) | dbfilter hides DB X on the same PostgreSQL role. The secret holder duplicates X, backs up X, and drops a copy of X | Duplicate succeeds, backup is refused as unknown, drop succeeds | Duplicate or drop refused because of the filter, or backup succeeds | **NOT-EXECUTED** |
| PC-WEB-D-04 | PR-WD4; REC-WEB-D30 (D11) | Record the session Set-Cookie attributes at login, then repeat base PC-WEB-05(c) in at least two browser engines | No SameSite and no Secure attribute set by the app. The cross-site outcome is recorded for each engine | The app sets SameSite=Strict, or a switch happens for a non-system user | **NOT-EXECUTED** |
| PC-WEB-D-05 | PR-WD5; REC-WEB-D36 (D17, F-W2) | Unauthenticated cross-origin logo requests for (a) a company with a logo, (b) an existing company without one, (c) a non-existent id | (a) returns that logo with an any-origin header. (b) and (c) return identical placeholders | (a) refused, or (b) and (c) can be told apart | **NOT-EXECUTED** |
| PC-WEB-D-06 | PR-WD6; REC-WEB-D38 (AO-W1) | An internal user who can read record R (a non-attachment model with an image field) requests it through the image route with a unique param and a bogus access-token argument | 200 with public cache-control | Private cache-control, or refusal | **NOT-EXECUTED** |
| PC-WEB-D-07 | PR-WD7; REC-WEB-D37 (D18) | Font-route JSON-RPC with a name that climbs out of the fonts directory to another font-extension file under an addons path, then to a non-font file | The font file is returned, and the non-font file is refused | The font file is refused, or the non-font file is returned | **NOT-EXECUTED** |
| PC-WEB-D-08 | PR-WD8; REC-WEB-D22 (D03); base REC-WEB-08 | Pivot XLSX export with a client cell value starting with `=` | The cell is stored as a literal string | The cell is stored as a formula | **NOT-EXECUTED** |
| PC-WEB-D-09 | **A2 extra finding: any access-token argument marks the content response cache-public** (AO-W1, shared-cache effect); REC-WEB-D38 | Behind a caching reverse proxy that honours Cache-Control. U1 can read private non-attachment record R and requests its content/image URL with a bogus access-token argument and max-age > 0. An anonymous client then requests the identical URL. Control arm: an attachment with a mismatched stored token | U1's response carries public cache-control, and the anonymous outcome is recorded (it may be served from the shared cache). The control arm returns not-found | U1's response is private (the finding is refuted), or the control arm returns content | **NOT-EXECUTED** |

### 3.2 SOURCE / CONFIG cases: EXECUTED (2026-09-27, 15:19Z onward)

| Case | Layer | Covers | Expected (predeclared) | Observed (paraphrase; pointers approximate) | Result |
|---|---|---|---|---|---|
| PC-WEB-D-10 | SOURCE/CONFIG | PR-WD1 precondition; D07, AO-W2 | Change-password sets the in-memory secret first, then saves. The save catches write errors and reports them to stderr without raising | The service change function sets the hashed secret in memory, then calls the config save for that one key (db ~L414-417). The save wraps the file write in handlers that print an error to stderr and do not re-raise (config ~L964-978). The hash context is a strong pbkdf2 scheme at a high round count, with plaintext accepted as deprecated (config ~L21-23) | **PASS**. AO-W2 is confirmed statically. Restart reversion needs PC-WEB-D-01 |
| PC-WEB-D-11 | SOURCE | PR-WD2 precondition; CRQ-WEB-02 residual | A sweep for rate, throttl, lockout, attempt, brute, sleep, ban and backoff over five files finds no limiter on master-secret checks. Per-attempt cost is the hash only | Hits: a comment on read-only transaction retry in http.py (~L2306, unrelated) and two websocket rate-limit options in config (~L218-219, unrelated). Nothing in db.py, database.py or security.py. Master verification is a hash-context verify (config ~L1036-1047) | **PASS** (bounded to five files; a proxy or deployment limiter is out of scope) |
| PC-WEB-D-12 | SOURCE | PR-WD3 precondition; D10 | Duplicate has no filter membership check. Drop checks only the forced, unfiltered list. Backup checks the filtered list | The duplicate route and service function do no membership check (database.py ~L94-109; db ~L184-197). The drop function returns early unless the name is in the forced list (db ~L231-233). Backup checks the name against the framework list, which is unforced (so it refuses when listing is off) and filtered by dbfilter (database.py ~L133-134; http ~L372-386) | **PASS** |
| PC-WEB-D-13 | SOURCE | PR-WD4 precondition; D11 | The framework sets the session cookie without an explicit SameSite argument and without forcing Secure. The become route has no methods restriction | Both session-cookie writes pass only max-age and httponly (http ~L2189-2194, ~L2523). The response cookie wrapper defaults Secure to off and SameSite to none (http ~L1784-1790). The become route declares user auth, http type and readonly, with no methods list (home ~L162) | **PASS**. The attribute actually emitted is library/browser behaviour, left for PC-WEB-D-04 |
| PC-WEB-D-14 | SOURCE | PR-WD5 precondition; D17, F-W2 | A missing company row and a row with an empty logo fall into the same placeholder path | A single condition, "row present and logo non-empty", decides between serving the logo and serving the no-logo placeholder, so the missing-row and empty-logo cases take the same branch (binary ~L287-305). Side observation, outside the predeclared scope: a non-integer company value raises and takes a third branch (the default product logo), which is a different placeholder | **PASS**. The side observation is recorded for PC-WEB-D-05 and A3 |
| PC-WEB-D-15 | SOURCE | PR-WD6 precondition; AO-W1 | Content and image routes set the stream public flag on the presence of the access-token argument, not on the outcome of token validation | Both routes set the stream public when the request's query-string arguments contain an access token. This happens after the record is resolved, independent of which ladder step granted access (binary ~L79-80, ~L196-197). Precision: only the URL query string is consulted, not the form body | **PASS** |
| PC-WEB-D-16 | SOURCE | PR-WD7 precondition; D18 | The name is joined to the fonts directory and passed to the generic resolver, whose containment is at the addons-path or root-path level. There is no basename or normalisation back to the fonts directory. An extension allowlist is present | The route joins the caller name to the absolute fonts directory and opens it through the generic file opener with a font-extension allowlist (binary ~L325-330). The resolver normalises the path, which resolves parent segments, checks the extension, and for an absolute path accepts it if it falls under any addons path or the server root path (misc ~L195-247). An absolute caller name would also replace the fonts directory in the join | **PASS**. Supports A2 D1 PARTIAL on D18. A1's "fonts directory only" does not hold at source |
| PC-WEB-D-17 | SOURCE | PR-WD8 precondition; D03 | The pivot XLSX workbook is created without disabling string-to-formula conversion, and client cells get no prefix neutralisation | The workbook is created with only the in-memory option (pivot ~L22). Client header titles and cell values are written through the generic writer with no prefix handling (pivot ~L40-86) | **PASS**. Library default conversion is left for PC-WEB-D-08 |
| PC-WEB-D-18 | SOURCE | Cache-public finding; AO-W1 | Stream response: a public flag gives the public directive when max-age applies, otherwise private. A mismatched attachment token raises | The response builder adds the public directive only when the stream is public and max-age is positive. Otherwise it removes public and sets private (http ~L690-695). The attachment content hook compares the token in constant time and raises an access error on mismatch, which the content route turns into not-found (ir_attachment ~L965-969; binary ~L76) | **PASS** |
| PC-WEB-D-19 | SOURCE | Consistency with base PC-WEB-11 FAIL; D01, F-W3 | The flat branch makes no export-data call on an empty set. The grouped branch calls export-data on the full set before grouping | Grouped (non-import-compatible, with groupby): export-data is called once on the whole selected set before grouping, so the gate at the start of export-data runs even for an empty set (export ~L569-573; models ~L889). Flat: batching over an empty id list yields no batch, so export-data is never called and a header-only file is built. The info log line is then written with count 0 (export ~L612-623; misc ~L693-697) | **PASS**. It re-observes exactly the base PC-WEB-11 state. The PC-WEB-11 FAIL is unchanged and preserved (its predeclared expectation, "export-data is not called for an empty set" on all paths, failed on the grouped path) |
| PC-WEB-D-20 | SOURCE | AO-W4 | The attachment read check enforces field-group access on field-bound attachments for non-system users | For non-system callers the read check forbids an attachment bound to a field that the caller cannot access, or to a field that does not exist, before record-level inheritance (ir_attachment ~L554-565) | **PASS** |

### 3.3 Result counts

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| SOURCE | 10 (D-11..D-20) | 10 | 0 | 0 |
| SOURCE/CONFIG | 1 (D-10) | 1 | 0 | 0 |
| RUNTIME | 9 (D-01..D-09) | 0 | 0 | 9 |
| **Delta total** | **20** | **11** | **0** | **9** |

Base proof, unchanged and for reference: 28 cases, 19 PASS, 1 FAIL (PC-WEB-11), 8 NOT-EXECUTED.

## 4. Proof status of REC DELTA items (status, not a measure)

| REC class (delta) | Items | Proof status |
|---|---|---|
| CONTRADICTION (1) | REC-WEB-D37 (D18), OPEN | PC-WEB-D-16 PASS supports A2. Runtime PC-WEB-D-07 pending |
| UNKNOWN_PENDING_PROOF (10) | D02 X-WEB-02; D26 D07; D39 AO-W2 | PC-WEB-D-10 PASS; runtime PC-WEB-03 and PC-WEB-D-01 pending |
| | D04 CRQ-WEB-02 residual (and base REC-WEB-29) | PC-WEB-D-11 PASS (negative, five files); runtime PC-WEB-D-02 pending |
| | D22 D03 | PC-WEB-D-17 PASS; runtime PC-WEB-D-08 and PC-WEB-02 pending |
| | D25 D06 | Base PC-WEB-16 PASS; runtime PC-WEB-04 pending |
| | D29 D10 | PC-WEB-D-12 PASS; runtime PC-WEB-D-03 pending |
| | D30 D11 | PC-WEB-D-13 PASS; runtime PC-WEB-05 and PC-WEB-D-04 pending |
| | D36 D17 | PC-WEB-D-14 PASS; runtime PC-WEB-06 and PC-WEB-D-05 pending |
| | D38 AO-W1 (cache-public) | PC-WEB-D-15 and D-18 PASS; runtime PC-WEB-D-06 and D-09 pending |
| MATCH (29) | incl. D01/D20 X-WEB-01 and D01; D40 AO-W4 | Supported by base PC-WEB-09/10/12/15/16/17/21 and delta PC-WEB-D-19/D-20 |
| GAP (6) | G-D1-3, NG-1..NG-5 | Not closable in scope |
| Base REC-WEB-27 (OM-W02, empty-result), CONTRADICTION OPEN | — | PC-WEB-D-19 PASS re-observes the PC-WEB-11 state. The PC-WEB-11 FAIL stands |

## 5. Disposition

**PROOF DELTA PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.**

- 11 predeclared SOURCE/CONFIG cases were executed against blob-verified source: 11 PASS, 0 FAIL.
- 9 RUNTIME cases (PR-WD1..8 plus the cache-public finding) are NOT-EXECUTED because the device is offline. They are ready to run as written in 3.1. No runtime result is claimed or inferred.
- Base PC-WEB-11 FAIL is consistent with D1. D1 contains no statement that contradicts it, and PC-WEB-D-19 re-observes the same state.

## 6. What A3 may challenge now (source/config layer)

1. **D18 (REC-WEB-D37)**: whether the font-route containment gap matters beyond font files. The absolute-name path in PC-WEB-D-16 widens A2's parent-segment reading.
2. **Cache-public (REC-WEB-D38)**: whether a token-argument-driven public flag on a caller-authorised response is a real shared-cache risk, given that the query-string argument changes the cache key. A3 may also challenge the base REC-WEB-15 move to RESOLVED while this cache aspect remains.
3. **Empty-result export (base REC-WEB-27)**: A2 D1 is internally split (a scoped X-WEB-01 row and an unscoped D01 row). A3 can decide whether this counts as convergence.
4. **Rate limiting (REC-WEB-D04 / base REC-WEB-29)**: the negative is keyword-bounded to five files.
5. **Logo placeholders (PC-WEB-D-14 side observation)**: a malformed company value takes a third branch. This does not affect the (b)/(c) equality but is a distinguishable response.

## 7. Limitations

- Static source at one commit. No runtime, database, proxy, browser, config-file or multi-worker state was observed. Line pointers are approximate.
- Library behaviour (spreadsheet formula conversion, the cookie attributes the web library emits) is not source-verified here and is left to the runtime cases.
- No Formal Coverage, no percentages, no git operations on the repository. No input was edited.
