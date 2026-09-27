# G01 PLATFORM_BASE — RED TEAM Proof Package — `privacy_lookup`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2 of a two-stage REC + PROOF run) |
| Group / Module | G01 PLATFORM_BASE / `privacy_lookup` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_PRIVACY_LOOKUP_REC_20260927.md` (32 REC items: MATCH 14, CONTRADICTION 3, UNKNOWN_PENDING_PROOF 12, GAP 3) |
| Inputs (sha256 at intake 15:04:27 UTC) | A1 `61524ebc…056a`; A2 `e10a3a06…aee9`; Lane A `35ccba82…e99`; bank `a6327b89…e0bb694` equals FREEZE_W1-B11 `bank_sha256`; freeze hash `94852761617bd3fc7c38182d374f6e82f62b3f5701f59fe17355c3c295202ea5`; manifest `19e3a154…78ed` |
| Freeze-basis status | **W1-B11 DELTA-RECHECK** (non-canonical). QID lineage is **NOT A3-eligible** until canonical re-freeze. Proof results below are claim-level and are not affected by the freeze basis |
| Predeclaration | Scratchpad `rec_phon_priv/proof_cases_predeclared.txt` (covers both modules), written 2026-09-27 15:05:54 UTC, sha256 `cf3bdecebb7417c002a0eaa9790c1023c891e581ededc99e43c4245a2a20ea83` hashed 15:06:04 UTC. No source was fetched in this run before that point; first fetch 15:06:05 UTC |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`, fetched 2026-09-27 15:06:05 UTC; every blob verified with `git hash-object` (section 2) |
| Runtime device | THPATTARAKRIT-SOLUTION-SERVICE-2.local: **OFFLINE** at 2026-09-27 15:08:20 UTC (`getent hosts` rc=2; `curl` rc=6 "Could not resolve host") |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

Clean-room note: neutral paraphrases only; identifiers are evidence pointers. No vendor code reproduced. No percentages. No Formal Coverage claim. No git operations. Inputs not edited. Source copies and harness stay in the scratchpad (`rec_phon_priv/src/`, `rec_phon_priv/harness_email.py` sha256 `30988af7…b783`, output `harness_email_out.txt` sha256 `7785dd29…87da`).

## 1. Case design

- The 9 A2 proof requirements PR-PRIV-01..09 become **runtime cases PC-PRIV-01..09**, one to one; setup/expected/fail are A2 §7 unchanged and restated in section 4.
- The static prediction basis becomes **SOURCE / CONFIG / CROSS-MODULE static cases PC-PRIV-10..22**, predeclared and **executed now**. Priority: the wildcard path (PC-10..13).
- One CROSS-MODULE case (PC-12) was executed with a **static harness**: the email split/normalize functions were extracted unchanged from core `odoo/tools/mail.py` at the anchor and run under the local Python standard library (3.11.15). This exercises a pure function only. It is **not** a system runtime, and results may differ under the runtime's Python version.
- A static PASS confirms only a source reading. **It is never counted as a runtime result.**

## 2. Blob verification (executed)

| File (under `addons/privacy_lookup/` unless noted) | Expected blob (Lane A / A2) | Computed `git hash-object` | Result |
|---|---|---|---|
| `__manifest__.py` | 9eaa9987… | 9eaa9987cdaa97b006c5fea0f961016490f811cd | MATCH |
| `models/privacy_log.py` | 045a2d25… | 045a2d25f7115f860d558c28d0d2f80301b64781 | MATCH |
| `models/res_partner.py` | 19962c36… | 19962c362f2b31fd12ad0aa383071db82fbd97d5 | MATCH |
| `wizard/privacy_lookup_wizard.py` | 3b6d52e0… | 3b6d52e055a912c67e85970d0299de14d97cc619 | MATCH |
| `wizard/privacy_lookup_wizard_views.xml` | 9d49f1db… | 9d49f1dbe6953295daf616f1d0f29f7b54b848fd | MATCH |
| `views/privacy_log_views.xml` | 2116cc13… | 2116cc13cac9496ea25a04b48cfba032264e6fc0 | MATCH |
| `security/ir.model.access.csv` | d70edab3… | d70edab351c9369c4e8100145b9006d1043029fe | MATCH |
| `data/ir_actions_server_data.xml` | 7aac52ec… | 7aac52ec8a0b8773de14cfc1670da285eeacf952 | MATCH |
| `odoo/tools/mail.py` (cross-module) | 2b05c91f… (A2 context file) | 2b05c91fede8af53a9d93dff511ffa3a78007b8b | MATCH |

9 of 9 blobs match.

## 3. Static cases — executed (SOURCE / CONFIG / CROSS-MODULE)

| Case | Layer | Links | Expected (predeclared) | Fail condition (predeclared) | Actual (observed, paraphrased) | Result |
|---|---|---|---|---|---|---|
| PC-PRIV-10 | SOURCE | PR-02, O-01, C05 | Trimmed name bound as case-insensitive pattern, unescaped; display-email bound wildcard-wrapped, unescaped | Any escaping of %/_ or escape clause; name by equality | The trimmed name is passed as the right operand of a case-insensitive pattern match in the partner reference set, in the user-partner subquery and in every dynamic record-name condition. The trimmed raw email is wrapped in multi-character wildcards and used for user logins, partner emails and all non-normalized email-like fields. No escaping step or escape clause exists anywhere in the module. (Core tools does provide an escaping helper for these metacharacters; the module does not call it) | PASS |
| PC-PRIV-11 | SOURCE | O-01 propagation, C04 | Name-matched partner set reused for users, authored messages and non-cascade refs; name/email OR-combined | AND, or no propagation | The partner reference set is "normalized email equals input OR name matches pattern". It feeds partner results, authored-message results and every scanned model's non-cascade partner-reference condition. User results use an equivalent OR subquery. Each model's conditions are OR-joined. A valid email therefore does not constrain the name branch | PASS |
| PC-PRIV-12 | CROSS-MODULE (static harness) | O-01 email branch, O-04 | Normalization does not reject "%" or "_" in the local part | Rejects/strips them | Harness (functions unchanged from core at anchor; Python 3.11.15): `%@x.com` → accepted unchanged; `_@x.com` → accepted; `a%b@x.com` → accepted; `%@%` → accepted; `x@y` → accepted; `Name <n@x.com>` → `n@x.com`; `"a@b" <n@x.com>` → `n@x.com`; `a@b@c.com` → rejected; `%` → rejected | PASS (harness; Python-version caveat) |
| PC-PRIV-13 | SOURCE | PR-01, C03, C07 | Flush then direct cursor execution; no company predicate; archive/delete via sudo | ORM search or company filter | Pending writes flushed, then one composed statement executed on the cursor and fetched as dictionaries. No company predicate or rule filter. Archive writes the active flag through a sudo recordset; delete unlinks through a sudo recordset | PASS |
| PC-PRIV-14 | SOURCE | PR-03(a), O-02, C10, C17 | Line action text assigned (replaced); wizard details = join of current lines; log details assigned (overwrite) | Append/accumulate | Each archive/unarchive/delete **assigns** a single action text to the line. The wizard's stored details are recomputed as the join of current lines' texts. After recompute, an existing log's details and found-records text are **assigned** from the wizard (overwrite). Archive then unarchive of one line therefore leaves only the second text | PASS |
| PC-PRIV-15 | SOURCE | PR-03(b), O-02, C17 | Lookup clears all lines then adds; existing-log update not gated on non-empty details | Update gated, or lines retained | Lookup replaces the line set with a clear-all command followed by the new results. The log helper creates a log only when none exists and details are non-empty; **otherwise** it overwrites the existing log's details and found-records with no emptiness check. After re-lookup the new lines carry no action text, so the log's details become empty. The Lookup button is hidden once lines exist, but the method remains callable | PASS |
| PC-PRIV-16 | CONFIG | C08, O-08 | Per-line delete confirmed; bulk delete server action none | Bulk has confirmation | Per-line Delete button carries a confirmation text ("irreversible"). The "Delete Selection" and "Archive Selection" server actions are plain code actions bound to the line list/kanban with no confirmation attribute | PASS |
| PC-PRIV-17 | SOURCE | PR-05, O-03, C07 | Archive toggle performs a sudo write inside a field-change handler | Write deferred to save | The active-flag change handler sets the line's action text and immediately writes the target's active flag through sudo. Bulk archive calls the same handler directly | PASS |
| PC-PRIV-18 | SOURCE | PR-06, C12, O-05 | Email masking returns (not raises) an error object for empty/"@-less" input; name routes to email masking only with "@" | Raises | The email masker returns an error object for empty or "@-less" input. Log creation assigns the masker's result to the masked-email field without inspecting it. Name masking calls the email masker only when the name contains "@" | PASS |
| PC-PRIV-19 | SOURCE | PR-07, C13, O-04 | Log created from raw wizard name/email; masking splits on "@" expecting two parts | Normalized values used, or tolerant split | The log is created from the wizard's raw name and email fields (not the trimmed/normalized values). The email masker unpacks the split on "@" into exactly two parts, so input with more than one "@" raises during log creation. PC-12 shows such input (quoted display name containing "@") passes the lookup's validation | PASS |
| PC-PRIV-20 | CONFIG | C14, O-05 | System-only; line no unlink; log full CRUD | Other | Three rows, all system group: wizard full rights; line read/write/create without unlink; log full rights (incl. create and unlink) | PASS |
| PC-PRIV-21 | SOURCE | C06, X1 | Reference cleared on failed read check; display name via sudo | Name also access-checked | The openable reference is set only if a read-access check passes (comment cites multi-company rules), else cleared. The stored display name is computed from a sudo recordset | PASS |
| PC-PRIV-22 | SOURCE + CONFIG | C15 | Wizard and line transient 24 h; log no retention; no cron | Retention on log | Wizard and line declare a 24-hour lifetime with no count cap. The log model declares no retention. The manifest data list has views, ACL and the two server actions only; no scheduled job | PASS |

**Static totals: 13 executed — PASS 13, FAIL 0.**

### 3.1 Wildcard path result (priority)

Static chain **confirmed** (PC-10, PC-11, PC-12, PC-13 all PASS): user input reaches pattern matching unescaped; a name consisting of the multi-character wildcard matches every named partner; that set becomes the reference set for users, authored messages and every partner-referencing record on every scanned model; the query runs directly on the cursor with no company predicate; archive and delete of any resulting line run through sudo. Runtime confirmation (PC-PRIV-02) is **NOT-EXECUTED**. Static PASS is not a runtime result.

### 3.2 Refinements observed (for A3; they do not change any verdict)

- R1 (PC-12, PC-10): the wildcard exposure also exists **through the email**. An email such as `%@%` passes normalization (harness). Its wildcard-wrapped raw form then matches every non-normalized email-like field value containing "@" and every user login containing "@", independent of the name. A2 mentioned single-character wildcards in emails; the multi-character case via email is additional.
- R2 (PC-10): the user branch matches logins by substring of the raw input, so over-matching occurs even without metacharacters (a login containing the input as a substring).
- R3 (PC-10): core tools at the anchor ships a helper that escapes pattern metacharacters in email strings; the module does not use it. Recorded as a neutral fact.
- R4 (PC-15): when no log exists yet and details are empty, the helper's else-branch assigns to an empty log reference. The effect is ORM-dependent (expected no-op) and routed to runtime (PC-03).
- R5 (PC-14, PC-17): bulk archive produces one action text per line and each line keeps only its latest text, so a later toggle on the same line replaces the bulk-archive text in the log.

## 4. Runtime cases — NOT-EXECUTED (runtime unavailable)

Common preconditions: a disposable database built from the anchored source with `privacy_lookup` installed (plus a module providing a company-scoped record for PC-01), two companies, a system administrator restricted to company A for PC-01, seeded subjects. Record verbatim outcomes. Status for all: **NOT-EXECUTED — runtime device THPATTARAKRIT-SOLUTION-SERVICE-2.local offline**. No result is inferred from the static cases.

| Case | Layer | Links (REC) | Steps (ready to run) | Expected | Fail condition | Status |
|---|---|---|---|---|---|---|
| PC-PRIV-01 | RUNTIME | PR-01, REC-03, REC-07 | Admin allowed only company A. Subject has a contact and a company-scoped record in B. Lookup; archive the B record; delete it | B records listed with name, no openable link; archive and delete succeed | B records absent, or archive/delete refused | NOT-EXECUTED |
| PC-PRIV-02 | RUNTIME | PR-02, REC-19 | Lookup with a valid email of a non-existent subject and a name that is only the multi-character wildcard. Do not remediate | Lines include unrelated partners, users and partner-referencing records across the database | Only email matches returned, or input rejected | NOT-EXECUTED |
| PC-PRIV-03 | RUNTIME | PR-03, REC-17, REC-20 | (a) Archive then unarchive one line; inspect log. (b) Delete one line, confirm log shows it, invoke lookup again via RPC/action; inspect log | (a) Log shows only unarchive. (b) Log details empty after re-lookup; found-records replaced | (a) Both events kept, or (b) deletion detail kept | NOT-EXECUTED |
| PC-PRIV-04 | RUNTIME + CROSS-MODULE | PR-04, REC-15, REC-20 | Perform a deletion; let/trigger transient cleanup; inspect log | Log details retained unchanged | Details blanked or altered | NOT-EXECUTED |
| PC-PRIV-05 | RUNTIME | PR-05, REC-21 | In the line list, toggle active for one record, then discard without saving (if the widget allows); inspect target and log | Target archived; no log detail | Target unchanged, or log detail exists | NOT-EXECUTED |
| PC-PRIV-06 | RUNTIME | PR-06, REC-12, REC-23 | As admin, create a log directly (RPC/import) with an email lacking "@" | Stored with non-masked/error-text value, or non-user-facing error | Clean validation error, nothing stored | NOT-EXECUTED |
| PC-PRIV-07 | RUNTIME | PR-07, REC-13, REC-22 | Lookup with display-form email whose display name contains "@" (single valid address); delete one line; record whether the deletion persisted | Lookup succeeds; delete raises during log creation | Log created normally with masked value | NOT-EXECUTED |
| PC-PRIV-08 | RUNTIME + CROSS-MODULE | PR-08, REC-28 | Delete via a line a partner referenced by restrict and by cascade dependents | Restrict blocks with no partial state; cascade dependents removed and not listed in log | Partial deletion persists, or log lists cascaded dependents | NOT-EXECUTED |
| PC-PRIV-09 | RUNTIME | PR-09, REC-29 | After lookup, delete a target via another session; then delete and archive its line | Error or explicit no-op; log does not claim an unperformed deletion | Log records "Deleted" for the missing record and no error | NOT-EXECUTED |

**Runtime totals: 9 cases — NOT-EXECUTED 9, PASS 0, FAIL 0.**

## 5. Summary of results

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| SOURCE (incl. SOURCE+CONFIG) | 10 | 10 | 0 | 0 |
| CONFIG | 2 (PC-16, PC-20) | 2 | 0 | 0 |
| CROSS-MODULE (static harness) | 1 (PC-12) | 1 | 0 | 0 |
| RUNTIME (incl. runtime + cross-module) | 9 | 0 | 0 | 9 |
| **Total** | **22** | **13** | **0** | **9** |

REC item status after Proof:
- The 3 CONTRADICTION items (C03 wording, C08, C17) are **source-confirmed on the A2 side** (PC-13, PC-16, PC-14/15). They remain CONTRADICTION for A3. C17's runtime effect is pending (PC-03, PC-04).
- The 12 UNKNOWN_PENDING_PROOF items have their static basis confirmed. **All remain UNKNOWN_PENDING_PROOF** until runtime.
- The 14 MATCH items are unchanged. The 3 GAP items are carried forward; GAP-PRIV-09 (freeze basis) routes to GMVQ/OVQDT.

## 6. Proposed additional runtime case (post-execution; NOT predeclared; not part of this run's result set)

- PC-PRIV-23 (proposed; R1): lookup with email `%@%` and a name matching nobody. Expected: lines include records whose display-email fields or user logins contain "@", unrelated to the subject. Fail: only exact-subject records returned, or input rejected.

## 7. A3 eligibility

**Disposition: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.**

A3 can challenge **now** (static, claim-level scope):
1. REC classifications and counts (32 items), folds and the MATCH treatment of O-06/O-07/O-08/O-09.
2. The 13 executed static cases, especially the wildcard chain PC-10..13, the harness method and its Python-version caveat (PC-12), and refinements R1–R5.
3. The 3 CONTRADICTION items, in particular C17 (A1's "actions remain only in the log" vs the overwritten-snapshot reading).
4. Input integrity, blob verification and predeclaration timing.

**Not A3-eligible:** the QID lineage (section 3 of the REC). W1-B11 is DELTA-RECHECK; the map is provisional until canonical re-freeze and re-validation.

**Blocked** until the runtime device is available: all 9 runtime cases (notably PC-02 wildcard scope, PC-01 cross-company, PC-03/04 log overwrite); closing any UPP item. Full A3 → MASTER handoff is **not** eligible; this package is eligible for **A3 static, claim-level challenge only**.

## 8. Limitations

- No runtime was executed and no runtime result is claimed. The PC-12 harness ran a pure standard-library function outside the system.
- ORM behaviours (transient cleanup ordering, field coercion of non-string values, change-handler transactions, stored-compute timing) are outside files read and routed to runtime.
- Effective scope depends on installed modules (not assessed). Tests and JS not read.
- No percentages, no Formal Coverage claim, no git operations. Inputs not edited.
