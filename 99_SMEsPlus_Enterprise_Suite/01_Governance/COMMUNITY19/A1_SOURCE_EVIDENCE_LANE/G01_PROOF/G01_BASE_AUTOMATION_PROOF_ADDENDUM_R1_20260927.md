# G01 PLATFORM_BASE — RED TEAM Proof Addendum R1 (A3 remediation) — `base_automation`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **PROOF**. This is an addendum only. The parent Proof package is immutable and was not edited |
| Group / Module | G01 PLATFORM_BASE / `base_automation` |
| Parent artifact | `A1_SOURCE_EVIDENCE_LANE/G01_PROOF/G01_BASE_AUTOMATION_PROOF_20260927.md`, sha256 `d3d3ad25a58a74c96b1aa7ee81eaf1760b2066add79163807984f77534867aff` (unchanged since A3 intake) |
| A3 report | `A1_SOURCE_EVIDENCE_LANE/G01_A3_CHALLENGES/G01_BASE_AUTOMATION_A3_STATIC_20260927.md`, sha256 `9b8bb57ab6bd62bf4b2165a06c4e31dfe612d48b1fa746e304520511938b1604` |
| Upstream addenda (inputs) | A2 `G01_A2_REVIEWS/G01_BASE_AUTOMATION_A2_ADDENDUM_R1_20260927.md` sha256 `be0cf294d1be8121954c65556a0f923b13b08186c4af045278c6927eca7b5c0a`; REC `G01_RECONCILIATION/G01_BASE_AUTOMATION_REC_ADDENDUM_R1_20260927.md` sha256 `05cd7a32a86ec23144529462fc491ea8456c4182eddf299d818d87b8795eb172` |
| Challenge IDs addressed | **CH-10** (MED, D1, PROOF part), **CH-09** (MED, D2), **CH-08** (LOW, D3, PC-42 wording), **CH-21** (LOW, D4, PC-40), **CH-12** (LOW, D5) |
| Predeclaration | Scratchpad `remed_baut/proof_addendum_R1_cases_predeclared.txt`, sha256 `531f5951bc25bbd4496d201598418a250fb096af6a8b8e742a13cbc2a5e8456d`, hashed **2026-09-27 15:17:13 UTC** (file mtime 15:17:13.24). It was written before the Proof-stage execution below |
| Execution log | Scratchpad `remed_baut/exec_log.txt` (started 15:17:31 UTC), sha256 `4e691140cb348e6ab5a10c15f7082f7a70f4e6457b70de1d07e519c9f53cc813`; blob log `remed_baut/blob_log.txt` |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`, fetched 15:13:40–15:14:39 UTC. All six previously recorded blobs MATCH. Three newly read files are hashed in the A2 addendum R1, section 0.1 |
| Runtime device | THPATTARAKRIT-SOLUTION-SERVICE-2.local: **OFFLINE**. `getent hosts` returned rc=2 at 2026-09-27 15:19:50 UTC |
| Date | 2026-09-27 |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** (Proof disposition remains PARTIAL: source/config executed, runtime pending) |

**Independence and blindness disclosure.** The same controller performed the A2-addendum source re-read before it wrote the predeclaration. The predeclared expected results are therefore **not blind** to source. PC-49R1's bounds were set from the bounds already observed in the parent PC-49. These cases are falsifiable re-reads, and their evidential weight is limited accordingly. A3 should weigh them as such.

Clean-room note: results are neutral paraphrases, and identifiers are pointers only. No vendor code. No percentages. No Formal Coverage claim. No git operations. No existing artifact was edited.

## 1. Supersede map

| Old case (parent) | New case | Reason (A3 CH) | Old case status after this addendum |
|---|---|---|---|
| PC-BAUT-12 (runtime, 3-run stall) | **PC-BAUT-12R1** | CH-10: the horizon cannot observe job deactivation | SUPERSEDED (was NOT-EXECUTED; never run) |
| PC-BAUT-13 (runtime, "one capture call per run (duplicates)") | **PC-BAUT-13R1** | CH-09: the action type was not named; the expected result contradicted post-commit semantics | SUPERSEDED (was NOT-EXECUTED; never run). Its expected result is **withdrawn** |
| PC-BAUT-40 (cross-module static, "triggering uid") | **PC-BAUT-40R1** | CH-21: uid per trigger type | SUPERSEDED. The parent PASS stands for the elevated-dispatch element only; its uid wording is withdrawn |
| PC-BAUT-42 (static, "conditions evaluated on an elevated recordset") | **PC-BAUT-42R1** | CH-08: per-path qualifier | SUPERSEDED. The parent PASS stands for the company-field, ACL and record-rule elements; its actual-result wording is withdrawn |
| PC-BAUT-49 (static, window) | **PC-BAUT-49R1** | CH-12: the fail condition could not test the bounds | SUPERSEDED. Parent result re-recorded as **PASS on the time-zone element only**. The predeclared "(last-run, now]" expectation was **NOT MET** for the datetime branch, which uses an inclusive lower and exclusive upper bound. The parent did not reconsider that deviation |
| — | PC-BAUT-56..62 (new static) | CH-10, CH-08, CH-09, O18 | — |
| — | PC-BAUT-63..65 (new runtime/config) | CH-08, CH-21, O18 | — |

## 2. Static cases — executed (SOURCE / CONFIG / CROSS-MODULE)

| Case | Layer | Links | Expected (predeclared, in substance) | Fail condition (predeclared) | Actual (observed, paraphrased) | Result |
|---|---|---|---|---|---|---|
| PC-BAUT-56 | SOURCE + CROSS-MODULE | PR-12R1, O3-R1, REC-27 | The processor reports progress with no processed count and re-raises the last error. The scheduler classifies "raised with zero processed" as FAILED, so any run containing a failing rule is FAILED | Positive count passed; such a run classified partially or fully done; final error swallowed | After each successful rule the processor calls the scheduler's commit-progress with no arguments, so the processed increment is zero. After the loop it re-raises the last stored error. The scheduler's classifier puts "action failed" with no recorded done count into FAILED, and the only exception is failure with both done and remaining non-zero. Because done stays zero, a run with any failing rule is FAILED even though healthy rules committed | **PASS** |
| PC-BAUT-57 | CROSS-MODULE | PR-12R1, base C31 | Counter plus first-failure stamp on FAILED; deactivate only at 5 or more AND more than 7 days; reset both; non-FAILED resets; notification hook | Threshold differs; OR-logic; no reset on success | Constants: 5 minimum failures and 7 days minimum. Both conditions are joined by AND, and the delta is strict (more than 7 days since the first failure). On deactivation active is set false, the counters reset and the admin-notification hook is called. Any other status resets the counters. Refinement: the base notification hook only writes a warning to the server log | **PASS** |
| PC-BAUT-58 | SOURCE + CONFIG | PR-12R1, CH-10 | One shipped job for all time triggers; processor iterates all active time rules; active recomputed only on rule create/delete/critical-or-range write (plus manual); no self-healing | Per-rule jobs; self-healing path | The data file holds one job record (inactive, 4 hours, no-update) that calls the time processor. The processor iterates every active rule of the three time trigger types. The job's active flag is written only by the cron-update routine, which is called from rule create, rule unlink and rule write when critical fields (model, active, trigger, on-change fields) or delay-range fields change. The only other reference to the job is a navigation action. No timer-based or self-healing re-activation exists | **PASS** |
| PC-BAUT-59 | SOURCE | O14-R1, C11 note | Time path: the condition is evaluated inside a plain search in the job environment with no module elevation, and the eval-context uid is the job user. Event paths filter elevated | Elevation on the time-path search or eval context; an event path non-elevated | The time-record selection routine contains no elevation call at all (count 0 in the log). It evaluates the apply-on condition with the rule's eval context (uid and user of the current environment) and searches the target model in the processor's environment. The processor itself contains no elevation call. The create, write, recompute and unlink patches, and the message and onchange hooks, all filter through the pre/post filter helpers, which filter an elevated copy of the records | **PASS** |
| PC-BAUT-60 | CROSS-MODULE + CONFIG | PR-28, O14-R1, REC-11-R1 | Job environment built from the configured user; ORM forces superuser mode for the superuser id; shipped job sets no user; default = creating env's user; loading env is superuser | Other identity; user set in data; non-superuser loading env | Both scheduler entry points build the job environment from the job's user id. The ORM environment constructor turns on superuser mode when the uid equals the superuser id. The module data file sets no user (zero occurrences). The scheduler's user field defaults to the current environment's user. The module-loading routine builds a superuser environment and passes it to the module graph loader, which loads data files with that environment. **Limitation:** the data-conversion layer between loader and record creation was not read. Default job user = superuser account is a **prediction** (PC-63) | **PASS** (static; conversion layer unread) |
| PC-BAUT-61 | CROSS-MODULE | PR-13R1, CH-09, base C28 | Webhook action: no send in the body, send registered post-commit plus a post-rollback notice; cursor clears post-commit on rollback and runs it on commit; processor rolls back a failing rule | Immediate send; rollback does not clear; no rollback | The base outbound-webhook runner reads and serializes the record, then registers the HTTP post (1-second timeout, errors logged) as a post-commit callback and a "cancelled due to a rollback" warning as a post-rollback callback. No send occurs in the runner body. The cursor's commit runs the post-commit callbacks after the database commit. Its rollback clears them before rolling back and then runs the post-rollback callbacks. The time processor rolls back the cursor when a rule fails | **PASS** |
| PC-BAUT-62 | SOURCE | PR-30, O18 | Record selection for a rule happens before and outside the per-rule isolation | Selection inside the isolation block | In the processor loop, the rule-existence check has its own narrow guard. Record selection is then called **before** the per-rule error-isolation block opens, and only the per-record processing and flush sit inside it. A selection error therefore propagates out of the loop | **PASS** |
| PC-BAUT-40R1 | CROSS-MODULE | REC-11-R1, CH-21 | Per trigger: event, message and onchange use the triggering user; time uses the job's configured user; webhook uses the public-auth user. Actions are dispatched from an elevated list and keep the uid | Any different uid source; run called on a non-elevated list | Event patches get rules through the lookup helper, which searches elevated and returns the rules in the **caller's** environment. Records are processed in that environment, so the uid is the triggering user. The message hook uses the posting environment. The onchange hook loads the rule in the form's environment. The time path runs in the environment of the scheduler's job user (PC-60). The webhook route is declared public-auth and loads the rule elevated from the request environment, which keeps the request uid; base A1 C25 records that public-auth falls back to the public user (base `http`/`ir_http` not re-read here). The per-record processor and the onchange hook both call run only on the elevated action list. Base run keeps the uid under elevation (base A1 C27) | **PASS** (static only) |
| PC-BAUT-42R1 | SOURCE + CONFIG | O14-R1, C16 | No company field; single admin ACL row; no record-rule file; elevated condition evaluation on event and onchange paths; job environment on the time path | Company field or record rule; qualifier fails | The company-field, ACL and record-rule elements are unchanged from the parent PC-42 (blob-verified files unchanged). Per-path evaluation is as observed in PC-59: elevated filtering on the event, message and onchange paths; job environment without module elevation on the time path | **PASS** |
| PC-BAUT-49R1 | SOURCE | PR-14, PR-15, O11, CH-12 | Datetime: lower bound inclusive, upper bound exclusive. Date: lower exclusive, upper inclusive. Calendar: lower inclusive, upper exclusive. No user time zone | Any bound inclusivity differs; user time zone applied | Comparison operators logged in order. Date branch: strictly greater than the shifted last-run date, and at most the shifted now date; the empty-field fallback branch uses the same inclusivity on creation date, with the O17a upper-bound refinement. Datetime branch: at least the shifted last-run and strictly less than the shifted now; the fallback uses the same. Calendar branch: planned last-run at most the record date, which is strictly less than planned now. No user time zone is consulted | **PASS** |

**Static totals (addendum): 10 executed. PASS 10, FAIL 0.** There is no failed static result to preserve.

Refinement recorded for A3 (not a failure): **R5.** The base admin-notification hook at job deactivation only writes a server-log warning unless another module overrides it. Base A1 C31 and A3 CH-10 describe it as "notifies an admin". Overrides were not searched.

## 3. Runtime and config cases — NOT-EXECUTED

Common preconditions: a disposable database built from anchor `8d05257d…` with `base_automation` installed, a controllable clock, and an outbound capture endpoint. Status for all: **NOT-EXECUTED — runtime device THPATTARAKRIT-SOLUTION-SERVICE-2.local offline** (rc=2, 15:19:50 UTC). No result is inferred from the static cases.

| Case | Layer | Links | Steps (ready to run) | Expected | Fail condition | Status |
|---|---|---|---|---|---|---|
| PC-BAUT-12R1 | RUNTIME + CROSS-MODULE | PR-12R1, REC-27 (supersedes PC-12) | Time rule A always fails on record R; healthy time rule B. Run the job at least 5 times, with more than 7 days between the first failure and the last run. Add eligible A and B records between runs. After deactivation, add B records and advance several intervals. Then write a delay-range field on a rule | Every run FAILED and the counter increments. A never advances. B advances until deactivation. After at least 5 failures AND more than 7 days the job goes inactive, and the hook fires (a log warning in base). B's new records are then not processed. The job re-activates after the rule write | Job still active after both thresholds; deactivated early; a non-FAILED run while A fails; B processed while inactive; A advances | NOT-EXECUTED |
| PC-BAUT-13R1 | RUNTIME + CROSS-MODULE | PR-13R1, REC-20 (supersedes PC-13) | (a) Time rule: a standard outbound-webhook action to the capture endpoint, then a code action that raises. Run twice. (b) Without the raising action, run once | (a) **Zero** calls in both runs; a rollback-cancel log line per queued send; DB changes rolled back; last-run not advanced. (b) One call per processed record, after commit | (a) Any call received. (b) No call | NOT-EXECUTED |
| PC-BAUT-63 | CONFIG (runtime inspection) | PR-28, REC-11-R1 | On a fresh install, read the automation job's configured user | The superuser account | Any other user | NOT-EXECUTED |
| PC-BAUT-64 | RUNTIME + CROSS-MODULE | PR-29, REC-38, REC-11-R1 | The condition matches X1 (visible to internal user U) and X2 (hidden from U by a record rule). A code action records uid and superuser flag and stamps the record. (i) Default job user. (ii) Job reassigned to U, last-run reset | (i) X1 and X2 stamped; uid is the superuser account. (ii) Only X1 stamped; uid is U; flag set in the action | (ii) X2 stamped, or uid is not the job user | NOT-EXECUTED |
| PC-BAUT-65 | RUNTIME | PR-30, REC-47 | Two time rules. The lower-id rule's condition raises when evaluated; the other is healthy with eligible records. Run once | Run FAILED; the healthy rule is not processed and its last-run is unchanged | The healthy rule is processed | NOT-EXECUTED |

**Runtime totals (addendum): 5 cases. NOT-EXECUTED 5, PASS 0, FAIL 0.**

## 4. Consolidated case status (parent plus addendum)

| Layer | Active cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| Static (SOURCE / CONFIG / CROSS-MODULE) | 35: parent 28 minus 3 superseded (40, 42, 49), plus 3 replacements and 7 new | 35 | 0 | 0 |
| Runtime / config inspection | 30: parent 27 minus 2 superseded (12, 13), plus 2 replacements and 3 new | 0 | 0 | 30 |
| **Total active** | **65** | **35** | **0** | **30** |

Superseded cases (5) are kept in the parent for lineage and are not counted as active.

REC effect: no class changes. All UNKNOWN_PENDING_PROOF items (now 21, including REC-47) and the runtime effect of the 5 CONTRADICTION items remain open. **Disposition: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.** Eligible for A3 static re-check. The A3 → MASTER full handoff is still not eligible.

## 5. Limitations

- No runtime was executed and no runtime result is claimed.
- The predeclared expected results were not blind to source (see the disclosure in section 0).
- The data-conversion layer, base `http`/`ir_http` public-user resolution and the restricted evaluator were not read in this addendum. Conclusions that depend on them rest on base A1 C25 and C28, or are routed to runtime.
- The static-case timing rests on scratch-file timestamps and hashes, which are not externally anchored (the same limitation A3 recorded as CH-14).
- No percentages, no Formal Coverage claim, no git operations. No existing artifact was edited. Source copies are in scratchpad `remed_baut/src/` only.
