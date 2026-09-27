# G01 PLATFORM_BASE — RED TEAM A2 Addendum R1 (A3 remediation) — `base_automation`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **RED TEAM A2** (addendum only; the parent A2 review is immutable and was not edited) |
| Group / Module | G01 PLATFORM_BASE / `base_automation` |
| Parent artifact | `A1_SOURCE_EVIDENCE_LANE/G01_A2_REVIEWS/G01_BASE_AUTOMATION_A2_REVIEW_20260927.md`, sha256 `bf95295f2d53891c8358422a8a3b5179e50bc44fa028a8be19be6c2a72bd4208` (unchanged since A3 intake) |
| A3 report | `A1_SOURCE_EVIDENCE_LANE/G01_A3_CHALLENGES/G01_BASE_AUTOMATION_A3_STATIC_20260927.md`, sha256 `9b8bb57ab6bd62bf4b2165a06c4e31dfe612d48b1fa746e304520511938b1604` |
| Other inputs (read-only) | base A1 `G01_A1_PACKAGES/G01_BASE_A1_PACKAGE_20260927.md` sha256 `a45a2beff88b8be61cd81b6075f7072f156c1b9d1d93029f0afb6ad35a0189e7` (C27, C28, C31); base A2 `G01_A2_REVIEWS/G01_BASE_A2_REVIEW_20260927.md` sha256 `05e422246b9bb925145c67ac044a6dc789bd99212376d59d47afa28a9b3500c1` (C28 and C31 PARTIAL notes); module A1 sha256 `f01dec29…7007` |
| Challenge IDs addressed | **CH-10** (MED, D1), **CH-08** (LOW, D3), **CH-09** (MED, D2, A2 note part) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, re-fetched 2026-09-27 15:13:40–15:14:39 UTC into scratchpad `remed_baut/src/` (blob log `remed_baut/blob_log.txt`) |
| Date | 2026-09-27 |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

### 0.1 Blob verification (`git hash-object`)

| File | Blob SHA-1 | Against |
|---|---|---|
| `addons/base_automation/models/base_automation.py` | `099ba2e3b5352a03fce94aec9f7bdc7219247144` | Lane A / Proof: MATCH |
| `addons/base_automation/controllers/main.py` | `e2eae519dd6ad74866240e10a242b37d323581b0` | MATCH |
| `addons/base_automation/data/base_automation_data.xml` | `a680e343b6339e7b18a1c44582e9aaf23afad54f` | MATCH |
| `odoo/addons/base/models/ir_cron.py` | `e8762b920da6a68fd655dccf1a936671838c561d` | base Lane A E10: MATCH |
| `odoo/addons/base/models/ir_actions.py` | `45d06ee4210b6e5559c6c96ab82ddc238a891a52` | base Lane A E12: MATCH |
| `odoo/addons/base/data/ir_cron_data.xml` | `0676236bea129b4f4d5c0994eeb3c6a47701f203` | base Lane A E20: MATCH |
| `odoo/orm/environments.py` | `ec6b89fc3b752d3c52eb220e95437dbd4db134fd` | newly read here (no prior lineage record) |
| `odoo/sql_db.py` | `e24a5a665ade3f51a1b02f4296bee8e21dd3412a` | newly read here (no prior lineage record) |
| `odoo/modules/loading.py` | `7be8669d7bba55c67d3bf71c09c8b7cbf0455d56` | newly read here (no prior lineage record) |

The last three files were read in the targeted sections needed for CH-08 and CH-09: superuser-mode rule, cursor commit and rollback callback handling, and the environment used for module data loading. They close part of the "not read" limitation that A2, Proof and A3 recorded. Their blobs have no earlier Lane A record, so A3 should treat them as new evidence pointers.

Clean-room note: every statement is a neutral WHAT/WHY/RISK paraphrase. Identifiers are evidence pointers only. No vendor code is reproduced and nothing is recommended for reuse. No percentages. No Formal Coverage claim. No git operations. No existing artifact was edited.

## 1. Amendment A2-R1-01: O3 extended (CH-10, D1)

**Parent O3 (HIGH), as written:** "one record that always fails makes its rule fail on every job run, never advance, and never process later records. The rule stalls indefinitely."

**Re-derivation from source:**
1. The time processor handles every active time rule in one pass of the **single** shipped scheduled job. The data file ships exactly one job record, and the processor iterates all three time trigger types. After each successful rule it asks the scheduler to commit progress **without a processed count**. When any rule failed, it re-raises the last error after the loop.
2. Base scheduler completion handling: if the action raised and the recorded processed count is zero, the run is classified FAILED. Because this module never records a count, **any run in which at least one time rule fails is FAILED**, even when other rules succeeded and committed in that run.
3. Base failure accounting: each FAILED run increments a consecutive-failure counter and stamps the first-failure time. When the counter is at least 5 **and** the first failure is more than 7 days old, the job is set inactive, the counters are reset, and an admin-notification hook is called. Any non-FAILED run resets the counters. Refinement to base A1 C31 and A3 CH-10: the base implementation of the admin-notification hook only writes a warning to the server log. An actual notification requires an override elsewhere, which was not checked here.
4. Re-activation: the module recomputes the job's active flag only when a rule is created or deleted, or when a rule write touches the critical fields (model, active, trigger, on-change fields) or the delay-range fields. Writes of last-run do not recompute it. There is no timer-based or self-healing re-activation. An administrator can also edit the job by hand.
5. **New sub-finding O18 (MED):** for each rule, the processor selects the rule's records (it evaluates the apply-on condition and runs the search) **before**, and outside, the per-rule error isolation. An error raised during selection, such as a condition that fails to evaluate or an access error in the search, is not isolated. It ends the whole run at once, so rules later in the iteration order are not processed in that run, and the run is FAILED. Only errors raised while processing records are isolated per rule.

**Amended O3 (supersedes the parent wording for downstream use):**
> O3-R1 (HIGH). A time rule with a persistently failing record never advances its last-run (unchanged). In addition, every job run that includes that rule is classified FAILED by the scheduler, because the module never reports processed counts. Healthy rules still advance within each run. After at least 5 consecutive FAILED runs spanning more than 7 days, the scheduler deactivates the **single shared job**, and **all** time-based rules then stop. They restart only after a rule create or delete, a critical-field or delay-range write on a rule, or a manual edit of the job. The notification at deactivation is only a server-log warning in base. "Stalls indefinitely" is therefore replaced by "stalls its own rule, and after repeated failures over at least 7 days stops every time-based rule". O18: an error during record selection aborts the rest of the run.

Severity: stays HIGH. The blast radius widens from one rule to all time-based automation. A2 records the parent's omission of the scheduler consequence as an A2 omission (A3 CH-10 sustained).

Evidence pointers: module model (time processor; cron update; create, write and unlink hooks); module data (single job); base `ir_cron.py` (completion-status classification, failure-count update, admin-notification hook).

## 2. Amendment A2-R1-02: C11 verdict and O14 qualified per path (CH-08, D3)

**Parent text:** C11 "Rule lookup, filter evaluation and the action list all run elevated". O14 "The before and apply-on conditions are evaluated against superuser-visible data".

**Re-derivation from source:**
- **Event paths** (create, write, recompute, unlink, message) take rules through the elevated lookup helper. They then evaluate before- and apply-on conditions by filtering an elevated copy of the records, and hand the result back in the triggering environment. **Onchange path:** the rule is loaded in the triggering environment, but the apply-on filter still filters an elevated copy. The eval-context uid and user are the triggering user's. **Verified as elevated.**
- **Webhook path:** the rule is loaded elevated by the controller, so the record-getter evaluation and lookup run elevated. The uid is whatever the public-auth route resolves, which base A1 C25 records as the public user. **Verified as elevated** (parent O6).
- **Time-based path:** the processor searches the rules, evaluates the apply-on condition and searches the target model, all **in its own environment, with no elevation applied by this module**. The eval context carries that environment's uid and user. Base builds the job's environment from the job's **configured user**. The ORM environment switches to superuser mode only when that user id is the superuser id.
- The shipped job record sets no user. The user field defaults to the user of the environment that creates the record. Module data is loaded under a superuser environment in the loading layer. The intermediate data-conversion layer was not read. The **predicted** default job user is therefore the superuser account, which would make time-path condition evaluation superuser-mode **by configuration, not by module elevation**. If an administrator reassigns the job to an ordinary user, time-path selection is limited to that user's access rights, and conditions see that user.
- In every path, actions are dispatched from an elevated action list, and elevation keeps the uid (parent C11 and base A1 C27; unchanged).

**Amended wording:**
> C11 verdict note (A2-R1): VERIFIED **with path qualifier**. Condition evaluation is elevated on the event, message, onchange and webhook paths. On the time-based path it runs in the scheduled job's environment under the job's configured user and is **not elevated by this module**. It is superuser-mode only if that user is the superuser account, which is the predicted shipped default (config proof PR-28). Action dispatch is elevated on all paths.
>
> O14-R1 (MED): conditions are evaluated against superuser-visible data **on the event, message, onchange and webhook paths**. On the time path, visibility is that of the job's configured user (superuser under the predicted default, restricted under a reassigned ordinary user).

## 3. Note A2-R1-03: C20 RISK and PR-13 prediction (CH-09, D2)

- The base standard outbound-webhook action does not send during execution. It reads the record, serializes the values, and registers the HTTP send as a **post-commit** callback, plus a rollback warning as a post-rollback callback. The cursor layer runs post-commit callbacks on commit and **clears them on rollback**. This confirms base A1 C28 and base A2 C28 ("a rollback only logs and never sends") at the cursor level. A3 had marked that level unread.
- The time processor rolls back a failing rule's transaction before moving on. Successful rules commit progress individually, so the only callbacks still pending at a rollback belong to the failing rule. Those include the sends queued for that rule's records that were processed **before** the failing record.
- **C20 RISK note:** "external side effects already sent are not rolled back" does **not** apply to the standard outbound-webhook action on the time path, or on the synchronous paths when the triggering transaction rolls back. For that type the static prediction is **no send** on rollback. The RISK remains open only for any action type that performs an external effect immediately, outside the transaction. None is evident in this module. The restricted evaluator's lack of an HTTP facility is carried from A3 and base A1, and was not re-verified here.
- **PR-13 prediction note:** the parent Expected "the capture endpoint receives one call per run (duplicates)" is **withdrawn** for the standard outbound-webhook action and replaced by PR-13R1 below. PR-13 did not name the action type. That was the defect.

## 4. Proof requirements: new and updated (for PROOF)

"Expected" is the static prediction and "Fail" falsifies it. All are runtime or config items on a disposable database built from the anchor, unless marked otherwise.

| PR | Status | Linked | Setup / action | Expected | Fail condition |
|---|---|---|---|---|---|
| PR-12R1 | **Supersedes PR-12** | O3-R1, C20, CH-10 | Controllable clock. Time rule A always fails on record R. Healthy time rule B. Run the job at least 5 times, with the span from the first failure to the last run exceeding 7 days. Add eligible records for A and B between runs. After deactivation, add B records and advance the clock several intervals. Then write a delay-range field on a rule | Every run FAILED and the failure counter increments. A never advances. B advances each run until deactivation. After at least 5 failures AND more than 7 days, the single job goes inactive, and the admin-notification hook fires (a warning log in base). B's new records are then not processed. The job becomes active again after the rule write | Job still active after both thresholds; deactivated before both are met; a run not FAILED while A fails; B processed while the job is inactive; A advances |
| PR-13R1 | **Supersedes PR-13** | C20 note, CH-09, base C28 | Time rule: (1) standard outbound-webhook action to a capture endpoint, then (2) a code action that raises. Run the job twice. Variant (b): without action (2), run once | (a) The endpoint receives **zero** calls in both runs. The log shows a rollback-cancel notice per queued send. DB changes are rolled back and last-run does not advance. (b) Exactly one call per processed record, sent after commit | (a) Any call received. (b) No call |
| PR-28 | New | C11 note, O14-R1, CH-08, CH-21 | CONFIG: on a fresh install, read the shipped automation job's configured user | The superuser account | Any other user |
| PR-29 | New | O14-R1, CH-08 | Time rule whose condition matches X1 (visible to internal user U) and X2 (hidden from U by a record rule). A code action records uid and superuser flag and stamps the record. (i) Run under the default job user. (ii) Reassign the job to U, reset last-run, run | (i) X1 and X2 stamped; uid is the superuser account. (ii) Only X1 stamped; uid is U; the superuser flag is set inside the action | (ii) X2 stamped, or uid is not the job user |
| PR-30 | New | O18, CH-10 | Two time rules. The lower-id rule has a condition that raises when evaluated. The other is healthy and has eligible records. Run once | Run FAILED. The healthy rule is not processed and its last-run is unchanged | The healthy rule is processed in that run |

Unchanged: PR-01..PR-11 and PR-14..PR-27 stand as written in the parent.

## 5. Effect on parent verdicts and counts

- C11: still VERIFIED, with a path qualifier (section 2). C20: still VERIFIED, with a RISK-scope note (section 3). No verdict changes, so the counts stay VERIFIED 22, PARTIAL 2.
- O3 is superseded in wording by O3-R1, and O14 by O14-R1. O18 is a new omission of MED severity. The omission count becomes O1–O18, and the proof requirement count becomes 30 (27 − 2 superseded + 2 replacements + 3 new).
- No A1 claim needs to return to A1 (consistent with A3 section 2).

## 6. Limitations

- Static re-read only. Every Expected above is a prediction, not an observation.
- The data-conversion layer between module loading and record creation was not read. The default job user is therefore a prediction, to be settled by PR-28.
- Overrides of the scheduler's admin-notification hook in other modules were not searched.
- The same controller also authored the PROOF and REC addenda R1 in this remediation. That independence limitation is disclosed for A3.
- No percentages, no Formal Coverage claim, no git operations. The parent A2 and all other inputs were not edited.
