# G01 PLATFORM_BASE — Module `base_sparse_field` — PROOF (Stage 2)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2; Reconciliation recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `base_sparse_field` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_BASE_SPARSE_FIELD_REC_20260927.md` (24 REC items) |
| Upstream A2 | `G01_A2_REVIEWS/G01_BASE_SPARSE_FIELD_A2_REVIEW_20260927.md` sha256 `b50478d63b806e827dfb561cc784bf6d4208dca568e7f37e3060531c640ee42a` (9 proof requirements, PR-SPRS-01..09) |
| Upstream A1 / Lane A | sha256 `50c2c610…ebca91d` / `d18d6476…b08b9f` (full values are in the REC intake) |
| Frozen bank | W1-B04, freeze_hash `9e31f2d27dfb959e555cf8ff117d829969e8122fe5e5544bbaf737b6ddea0377` (recomputed: MATCH) |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/base_sparse_field/<path>` |
| Runtime device | OFFLINE (last recorded 2026-09-24T12:53Z, `MASTER_CONTROLLED_HANDOFF_STATE_20260927.md`) |
| Lane B | None exists (search recorded in REC section 3) |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

## 2. Predeclaration

- There are 21 proof cases: 12 SOURCE/CONFIG and 9 RUNTIME. There is one RUNTIME case for each A2 proof requirement, and SOURCE/CONFIG cases for the source-visible premises and the REC items that have no PR.
- The expected and fail conditions were fixed in a scratchpad file **before any Stage-2 source fetch**. The file is `PROOF_CASES_PREDECLARED.md` (it also covers `google_recaptcha`), sha256 `59a6e0d0ec0ec259bb7dec88c64d80d74c90c38d89042a3d2c350004096adcbc`, written 2026-09-27T15:03:45Z. The first Stage-2 fetch followed at about 15:04Z. The case content came from the A1/A2 text only.
- RUNTIME cases stay NOT-EXECUTED while the runtime device is OFFLINE. They are ready to run and contain no invented results.
- Verdict rule: PASS means the predeclared expected condition was observed, so the claim premise holds as stated. FAIL means the fail condition was observed.

## 3. Source retrieval and blob verification

All 9 Lane A pointer files were fetched again from the anchor URL on 2026-09-27 (HTTP 200 each) and hashed with `git hash-object`. Copies are held only in the scratchpad. No repository git operations were run. The log is `blob_results.txt` (shared with `google_recaptcha`, 23 files), sha256 `c046d0b2c601beb22a8f5fb8ea43d181bba73bc5e03f91608b19d6973db3222b`.

| Ref | Path | Blob (recorded = computed) | Result |
|---|---|---|---|
| E1 | `__manifest__.py` | c487ecfef4f50434826b1df23933f76a3dcd686c | MATCH |
| E2 | `__init__.py` | cde864bae21a11c0e4f50067aa46b4c497549b4c | MATCH |
| E3 | `models/__init__.py` | 37c0f9345ccd8da658314ee901c59970f16c8039 | MATCH |
| E4 | `models/fields.py` | cb26946e9e356dee65fe65fca09dbe24fd4373cb | MATCH |
| E5 | `models/models.py` | f219622654de80989f1202226dee84c3ff8caef9 | MATCH |
| E6 | `security/ir.model.access.csv` | c163e1f2c64d9e3f76a0d2cc426e70d622ec60b3 | MATCH |
| E7 | `views/views.xml` | 1c199e72b7736ef1170bf0de9e929b205950d579 | MATCH |
| E8 | `tests/__init__.py` | 1dc570533d5d6f4099d65adcb935a1d925179b5c | MATCH |
| E9 | `tests/test_sparse_fields.py` | 944ff206dc137b8ca61f23e33860b40ce1dba122 | MATCH |

Negative scans of E4 and E5 are logged in `static_checks.txt`, sha256 `d28764781afce80c0da4bb654957a03dadcf9801a5adf8eec4f16b705b421c1b`. They found 0 constraint, unlink or create overrides and 0 `search=` or `depends` declarations.

## 4. Proof cases and results

Evidence cites `path`@short-blob with line ranges in the fetched copy. Summaries are neutral and reproduce no code.

| PC | PR / REC | Layer | Preconditions | Steps | Expected | Fail condition | Result | Evidence |
|---|---|---|---|---|---|---|---|---|
| PC-SPRS-01 | lineage / REC-SPRS-01, 02 | SOURCE | Anchor reachable | Fetch E1–E9 and run git hash-object | All 9 blobs equal the Lane A SHA-1 | Any mismatch or non-200 | **PASS** (9/9 MATCH) | `blob_results.txt` |
| PC-SPRS-02 | PR-SPRS-02 premise / REC-SPRS-04 | SOURCE | E4 verified | Read the sparse inverse | A falsy value removes the key, a truthy value is stored, and the map is written back only when it changed | A falsy value is stored under the key | **PASS** | `models/fields.py`@cb26946e L59–71 |
| PC-SPRS-03 | PR-SPRS-03 premise / REC-SPRS-06 | SOURCE | Same | Read the container write/cache conversion, the read conversion and the sparse compute | A dict is JSON-encoded. Any other value passes through unchanged (null when falsy), with no JSON validity check. The decode has no error handling and no type check. The compute does a key lookup on the decoded value | Guarded decode, or a non-dict rejected on write | **PASS**. A2 SF-2 is confirmed on source: a decoded list or scalar reaches a map lookup | `models/fields.py`@cb26946e L85–93, L50–54 |
| PC-SPRS-04 | PR-SPRS-01 premise / REC-SPRS-10 | SOURCE | E5 verified | Read the field-metadata write override | The outer condition is "pointer key OR name key present". For a field that has a pointer, the rename test indexes the incoming name without checking that it is present | The name's presence is checked before indexing | **PASS**. CON-SPRS-01 is confirmed on source, and runtime reachability stays open | `models/models.py`@f2196226 L29–39 (condition L32, unguarded index L36) |
| PC-SPRS-05 | PR-SPRS-06 premise / REC-SPRS-09, 11 | SOURCE | Same | Read the write override and look for a create override | The current pointer id is compared with the requested value, so any difference (attach or detach) raises a user error. A rename of a field that has a pointer raises a user error. There is no create override | Attach or detach allowed, or create restricted | **PASS** (0 create overrides) | `models/models.py`@f2196226 L32–37; `static_checks.txt` |
| PC-SPRS-06 | REC-SPRS-08 (CONTRADICTION) | SOURCE | Same | Read the pointer field definition and search for constraints | The same-model limit is expressed only as a string domain. The pointer is cascade-deleted. There is no server-side constraint on the target model | A constraint enforcing the same model exists | **PASS**. Confirms A2 SF-1 against A1 C08's "limited to" wording | `models/models.py`@f2196226 L22–27; `views/views.xml`@1c199e72 L12, L24–26; `static_checks.txt` (0 constraints) |
| PC-SPRS-07 | REC-SPRS-21 (OM-1) | SOURCE | Same | Search for an unlink override or key cleanup | The module has neither | Cleanup present | **PASS** (only `write`, `_reflect_fields` and `_instanciate_attrs` are overridden) | `models/models.py`@f2196226 L29–89 |
| PC-SPRS-08 | REC-SPRS-22 (OM-2) | SOURCE | E4, E5 | Search for per-key validation of container writes | The container accepts any map, and no key allow-list exists. A sparse read looks up only its own name | Key allow-list or validation present | **PASS** | `models/fields.py`@cb26946e L50–54, L88–90 |
| PC-SPRS-09 | PR-SPRS-07 premise / REC-SPRS-12 | SOURCE | E5 | Read the post-reflection sync | Existing pointers are read with raw SQL, updates are computed only for rows whose value differs, and those rows are updated with raw SQL grouped by value. A missing container raises a user error. Modified-notification is deferred to post-init | Unconditional rewrite, or an ORM write path | **PASS**. The static premise for idempotency holds; runtime is pending | `models/models.py`@f2196226 L41–82 (diff L70–71, SQL L77–79, error L62–69) |
| PC-SPRS-10 | REC-SPRS-03, 18, 20 (C03, C18, SF-6 premise) | SOURCE | E4 | Read the field attribute patch | The field is forced non-stored. Copy defaults to false unless given. The compute is attached, and the inverse only when the field is not read-only. There is no search method and no explicit dependency on the container | Stored allowed, a search method defined, or a container dependency declared | **PASS** (0 `search=` / `depends`). Whether the core infers a dependency (SF-6) is not examined here | `models/fields.py`@cb26946e L38–48; `static_checks.txt` |
| PC-SPRS-11 | REC-SPRS-14, 15 (C14, C15, SF-4) | CONFIG | E6, E7 | Read the ACL CSV and the views | One ACL row: the demo model, the system group, read/write/create = 1, unlink = 0. On both forms the selector is read-only only when the state is base, and quick-create is off | A different ACL, or read-only for manual fields as well | **PASS**. SF-4 is confirmed: the selector is editable on manual fields | `security/ir.model.access.csv`@c163e1f2 L2; `views/views.xml`@1c199e72 L11–13, L24–26 |
| PC-SPRS-12 | REC-SPRS-19 (C19, OM-5) | SOURCE | E9 | Read the test file | One test. Only truthy values are set, and unset is done by writing false. There is no test for zero or 0.0, rename, storage change, concurrency or malformed payloads. A reflection check is present | Any such test present | **PASS** | `tests/test_sparse_fields.py`@944ff206 L8–40 |
| PC-SPRS-13 | PR-SPRS-01 / REC-SPRS-10 | RUNTIME | Isolated test DB, module installed, admin RPC | Write only the unchanged pointer to a sparse field's metadata record | A technical missing-key server error, rolled back | A user error, or the write succeeds | **NOT-EXECUTED** (runtime device OFFLINE; ready to run) | — |
| PC-SPRS-14 | PR-SPRS-02 / REC-SPRS-04 | RUNTIME | A demo record holding truthy values | Write 0, 0.0 and false. Read back and inspect the container | Keys removed. The read-back equals never-set | A key is kept, or the read-back differs | **NOT-EXECUTED** | — |
| PC-SPRS-15 | PR-SPRS-03 / REC-SPRS-06 | RUNTIME | A test record | Set the container to (a) non-JSON text and (b) a JSON list, then read one attribute | (a) A decode error. (b) An error at the sparse read. Neither case is silently empty | Silent empty or default, or partial values | **NOT-EXECUTED** | — |
| PC-SPRS-16 | PR-SPRS-04 / REC-SPRS-17 | RUNTIME | Two concurrent transactions | Write different attributes on the same record | One transaction is refused or retried, and both values are present after the retry | Both commit and one value is lost | **NOT-EXECUTED** | — |
| PC-SPRS-17 | PR-SPRS-05 / REC-SPRS-16 | RUNTIME | One attribute restricted to a group | As a non-member, read the container field and export it | The restricted value is visible through the container | The value is not reachable | **NOT-EXECUTED** | — |
| PC-SPRS-18 | PR-SPRS-06 / REC-SPRS-11 | RUNTIME | Existing manual fields | Attach and then detach a container through the form | Both are refused with the storage-change user error | Either change is saved | **NOT-EXECUTED** | — |
| PC-SPRS-19 | PR-SPRS-07 / REC-SPRS-12 | RUNTIME | Module installed | Upgrade twice and capture the pointers and the count of updated rows | The second run updates 0 rows and the pointers are unchanged | Any change | **NOT-EXECUTED** | — |
| PC-SPRS-20 | PR-SPRS-08 / REC-SPRS-20 | RUNTIME | A test record | Write the container directly, then read the attribute in the same transaction | The new value | A stale value | **NOT-EXECUTED** | — |
| PC-SPRS-21 | PR-SPRS-09 / REC-SPRS-18 | RUNTIME | Demo records | Search, filter and order by a sparse attribute (UI and API) | Refused, or explicitly unsupported | Silently empty or wrong results | **NOT-EXECUTED** | — |

### Result totals

| Result | Count | Cases |
|---|---|---|
| PASS | 12 | PC-SPRS-01 to PC-SPRS-12 (SOURCE/CONFIG) |
| FAIL | 0 | — |
| NOT-EXECUTED | 9 | PC-SPRS-13 to PC-SPRS-21 (all RUNTIME) |

No failures occurred, so none needed to be preserved. A static PASS confirms only the source-visible premise. It is **not** runtime proof of the A2 prediction.

Observation for A3 (outside the predeclared cases; not a verdict): the attach/detach comparison in PC-SPRS-05 compares the current pointer id, which is false when there is none, with the raw requested value. A payload that sends a null of a different type from false for a non-sparse field would therefore also compare as "different" and be refused. This was read statically and not executed.

## 5. Effect on REC items

| REC item | Status after Proof |
|---|---|
| REC-SPRS-08 (CONTRADICTION) | Source side confirmed by PC-SPRS-06 PASS. A1 C08's "limited to containers on the same model" is advisory only (domain/UI). A2 SF-1 stands. The runtime cross-model setup behaviour is not examined |
| REC-SPRS-04, 10, 11, 12, 16, 17, 18 (UNKNOWN_PENDING_PROOF) | The source premises PASS (PC-SPRS-02, 04, 05, 09, 10). These items stay UNKNOWN_PENDING_PROOF until PC-SPRS-13, 14, 16, 17, 18, 19 and 21 are run |
| REC-SPRS-06, 20, 21, 22 (GAP) | A2's extension or omission is confirmed on source (PC-SPRS-03, 10, 07, 08). The runtime effect is pending for 06 (PC-SPRS-15) and 20 (PC-SPRS-20) |
| REC-SPRS-23 (GAP, no case) | No proof case. The uninstall data effect was not examined. A3 may challenge it |
| MATCH items | Static checks PASS where a case exists (REC-SPRS-01, 02, 03, 09, 14, 15, 19). REC-SPRS-05, 07, 13 and 24 rest on A2's source basis |

## 6. Runtime pack (ready to run when the device is online)

Use an authorized, isolated test instance at anchor `8d05257d` with `base_sparse_field` installed and the demo model `sparse_fields.test` available. There must be no production data. PC-SPRS-16 needs two independent DB cursors or sessions. PC-SPRS-15 needs direct SQL write access to the test DB. PC-SPRS-19 needs module upgrade rights and SQL row-count capture on the field-metadata table. For each case, record the request payload, the raw error class and message, the container contents before and after, and the user and group context. Record every FAIL as it occurs. Do not re-run a case to get a pass.

## 7. A3 eligibility and challenge surface

**A3 may challenge now:**
1. The REC classifications, especially the REC-SPRS-08 CONTRADICTION (rather than GAP), and the choice of GAP for REC-SPRS-06 (the C06 extension).
2. The QID lineage mapping: 29 mapped, 12 with no evidence, and 3 REC items with no fit.
3. The 12 executed SOURCE/CONFIG cases: whether each predicate is sufficient, the line citations and the blob verification.
4. Predeclaration independence: the cases were written at 15:03:45Z, before the Stage-2 fetch, but the controller had read A1 and A2 (which paraphrase the source) beforehand.
5. The GAP items with no proof case (REC-SPRS-23) and the open core gaps (GAP-3, GAP-4, GAP-6).
6. Clean-room compliance and the lineage hashes.

**A3 may not treat as proven:** the outcome of any RUNTIME case (PC-SPRS-13 to PC-SPRS-21). These remain NOT-EXECUTED, and Lane B stays UNCORROBORATED.

## 8. Limitations

- Everything rests on one anchor commit. The core field attribute resolution, core reflection, transaction isolation and the core search fallback were not read.
- No runtime execution took place, and no results were fabricated.
- No Formal Coverage claim, no percentages and no QID answered.
- Clean room: neutral summaries only. Identifiers and line numbers are evidence pointers, and no code is reproduced.
- The inputs were not edited and no git operations were run. Scratch: `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/rec_sprs_rcap`.
