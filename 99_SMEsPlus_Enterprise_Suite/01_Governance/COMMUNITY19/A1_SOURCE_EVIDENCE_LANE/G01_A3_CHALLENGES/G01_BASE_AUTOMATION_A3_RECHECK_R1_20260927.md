# G01 PLATFORM_BASE — RED TEAM A3 Re-Check of Remediation R1 (STATIC scope) — `base_automation`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, independent adversarial re-check of remediation R1 |
| Independence statement | This reviewer did not author the original A3 report, the A2/REC/PROOF addenda R1, or any upstream stage for this module. The addenda were treated as claims to disprove. Source was re-fetched into a separate scratchpad (`a3r1_baut/src/`) and re-read on its own terms. No upstream artifact was edited |
| Group / Module | G01 PLATFORM_BASE / `base_automation` |
| Date | 2026-09-27 (intake 15:22:05 UTC; source fetch 15:23:03–15:23:05 UTC; re-execution log 15:24:56 UTC) |
| Scope | STATIC only. Every runtime/config-inspection case (30 active) is **NOT-EXECUTED**. The runtime device THPATTARAKRIT-SOLUTION-SERVICE-2.local is recorded offline by the Proof addendum; this re-check did not execute runtime. Nothing is treated as passed or failed at runtime |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, fetched via raw URL and checked with `git hash-object`. 9 of 9 blobs MATCH the addendum record: rule model `099ba2e3…7144`, controller `e2eae519…81b0`, module data `a680e343…f54f`, base `ir_cron.py` `e8762b92…561d`, base `ir_actions.py` `45d06ee4…1a52`, base cron data `0676236b…f203`, `odoo/orm/environments.py` `ec6b89fc…134fd`, `odoo/sql_db.py` `e24a5a66…412a`, `odoo/modules/loading.py` `7be8669d…5d56`. Additionally read: module ACL `77253ff3…df34` (MATCH to original A3 record) |
| **Overall disposition** | **`A3 R1 RE-CHECK: STATIC PASS WITH RESIDUAL DEFECTS (route A2, PROOF, REC, Integration Control/MASTER)`**. No static FAIL. MASTER handoff remains **pending runtime** |

### 0.1 Lineage hashes (sha256), intake and exit

Paths relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/` unless stated. "Git" = read-only `git log` / `git rev-parse` on the committed blob.

| Input | sha256 at intake (15:22:05Z) | sha256 at exit | Git |
|---|---|---|---|
| Original A3 `G01_A3_CHALLENGES/G01_BASE_AUTOMATION_A3_STATIC_20260927.md` | `9b8bb57ab6bd62bf4b2165a06c4e31dfe612d48b1fa746e304520511938b1604` (equals the value cited in all three addenda) | identical | — |
| A2 addendum R1 `G01_A2_REVIEWS/G01_BASE_AUTOMATION_A2_ADDENDUM_R1_20260927.md` | `be0cf294d1be8121954c65556a0f923b13b08186c4af045278c6927eca7b5c0a` (equals the Proof addendum header) | identical | 1 commit `6d55fdb` 15:18:45Z, subject names resource/resource_mail; committed blob = current |
| REC addendum R1 `G01_RECONCILIATION/G01_BASE_AUTOMATION_REC_ADDENDUM_R1_20260927.md` | `05cd7a32a86ec23144529462fc491ea8456c4182eddf299d818d87b8795eb172` (equals the Proof addendum header) | identical | 1 commit `d14de3c` 15:19:52Z, subject names bus/digest A3; committed blob = current |
| PROOF addendum R1 `G01_PROOF/G01_BASE_AUTOMATION_PROOF_ADDENDUM_R1_20260927.md` | `091359539b2648a2a1ffa886188dd9c9d9a40dfe7b43d56ddbac5473ebf21e39` | identical | 1 commit `123da2d` 15:20:53Z, subject names web_unsplash proof; committed blob = current |
| Parent A2 `G01_A2_REVIEWS/G01_BASE_AUTOMATION_A2_REVIEW_20260927.md` | `bf95295f2d53891c8358422a8a3b5179e50bc44fa028a8be19be6c2a72bd4208` (unchanged since original A3) | identical | — |
| Parent REC `G01_RECONCILIATION/G01_BASE_AUTOMATION_REC_20260927.md` | `6f4471f430863392e757f99fc3a818cf60a0820350a724fa3720b1f2a39ed0ab` (unchanged) | identical | — |
| Parent PROOF `G01_PROOF/G01_BASE_AUTOMATION_PROOF_20260927.md` | `d3d3ad25a58a74c96b1aa7ee81eaf1760b2066add79163807984f77534867aff` (unchanged) | identical | — |
| Predeclared cases (scratch) `remed_baut/proof_addendum_R1_cases_predeclared.txt` | `531f5951bc25bbd4496d201598418a250fb096af6a8b8e742a13cbc2a5e8456d` — **VERIFIED**, equals the stated `531f5951…456d`; birth/mtime 15:17:13.23Z; companion `predeclared.timestamp` = 15:17:13Z | identical | not committed (scratch) |
| Proof exec log (scratch) `remed_baut/exec_log.txt` | `4e691140cb348e6ab5a10c15f7082f7a70f4e6457b70de1d07e519c9f53cc813` (equals Proof header); birth 15:17:31Z | identical | not committed |
| MASTER board `../MASTER_CONTROLLED_HANDOFF_STATE_20260927_C1B.md` | `d3966ad058ca11e82ef20ec777818486a726996f8d04f6a59da4315cf6e84e42` | identical | 1 commit `57c46fe` 15:20:45Z |
| Module A1 `G01_A1_PACKAGES/G01_BASE_AUTOMATION_A1_PACKAGE_20260927.md` (context) | `f01dec29aeb323747b288b4ef3687acad4e5deefdddc10d7422fa4fac6297007` | identical | — |
| Bank `../GMVQ/G01_PLATFORM_BASE/G01_BASE_AUTOMATION_GMVQ_MVQ_40_V1.00_DRAFT.md` (context) | `3c38cec4aa1ef2aa92d0e850da0d18242da9dc7c6ef7bd137c433edb379b9a49` (equals freeze entry) | identical | — |
| This re-check's own exec log (scratch) `a3r1_baut/exec_log.txt` | `ab1e9de6d021cb0af6c0024038d0460fb5c1977f71b5a0a20f237c1a7109dc97` | — | not committed |

### 0.2 Reconstructed remediation timeline (file birth times and git)

| UTC | Event |
|---|---|
| 15:12:11 | Original A3 written |
| 15:13:40–15:14:39 | Remediation source fetch (9 blobs) |
| 15:17:13 | Proof addendum cases predeclared and hashed |
| 15:17:31 | Proof static execution log started |
| **15:18:33** | **A2 addendum R1 file created** (birth = mtime) |
| 15:19:43 | REC addendum R1 file created |
| 15:20:45 | MASTER C1-B board with the 5 systemic process rules committed |
| 15:20:49 | Proof addendum R1 file created |

Clean-room note: every statement below is a neutral WHAT/WHY/RISK paraphrase; identifiers are evidence pointers only. No vendor code is reproduced and nothing recommends reuse of vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. No QID is answered. No git write operations; inputs not edited.

## 1. Per-challenge status (original sustained challenges)

| CH (orig. severity) | Required action (original A3 §2) | Remediation evidence | A3 R1 independent check | Status |
|---|---|---|---|---|
| **CH-10** (MED, D1) | Extend O3 to job-wide deactivation; runtime case on a controllable clock; carry to REC-27 | A2-R1-01 (O3-R1, O18); PR-12R1; PC-56/57/58 static; PC-12R1 runtime; REC-27 basis updated; REC-47 new | Re-derived independently (section 2.1). Single shipped job; processor never reports a processed count; a raised run with zero done is FAILED; deactivation needs count at least 5 AND first failure strictly more than 7 days old; counters reset at deactivation and on any non-FAILED run; base admin hook only logs a warning. Restart triggers confirmed. All addendum statements reproduce | **CLOSED** (static). Runtime PC-12R1 pending. Residual wording notes RD-2, RD-3 (LOW/INFO) do not reopen it |
| **CH-09** (MED, D2) | Re-predeclare PC-13 naming the action type; qualify C20 RISK and PR-13 | A2-R1-03; PR-13R1; PC-13R1 (action type named, expected zero calls on rollback); PC-61 static; REC-20 basis | Base outbound-webhook runner registers the send as post-commit and a cancel notice as post-rollback; the cursor rollback clears post-commit callbacks before rolling back, and commit runs them after the database commit; the time processor rolls back on rule failure. Reproduced | **CLOSED** (static). Carried limitation: the restricted evaluator's lack of an HTTP facility is still not re-verified by any stage (A2-R1-03 says so); runtime PC-13R1 pending |
| **CH-08** (LOW, D3) | Per-path qualifier on C11 verdict and O14; fix PC-42 wording | A2-R1-02 (C11 note, O14-R1); PC-42R1, PC-59, PC-60; PR-28/PC-63, PR-29/PC-64; REC-38 | Time-path selection and processor contain no elevation call (count 0); condition evaluated with the job environment's uid; event paths filter an elevated copy; environment forces superuser mode when uid is the superuser id; shipped job sets no user; user default is creator; module loading runs under a superuser environment. Reproduced | **CLOSED** (core qualifier). New residual **RD-1** (LOW-MED) on the "reassigned ordinary user" branch of O14-R1 / PC-64 — a new defect, not a reopening |
| **CH-12** (LOW, D5) | Record PC-49 interval deviation or re-predeclare with bound-testing fail condition | PC-49 re-recorded PASS on time-zone element only, "(last-run, now]" NOT MET; PC-49R1 with per-branch inclusivity fail condition; REC-35 basis | Operators re-extracted in order: date branch strict-lower / inclusive-upper; datetime branch inclusive-lower / strict-upper; calendar branch inclusive-lower / strict-upper; no user time zone. Matches PC-49R1 | **CLOSED**. Weight note: PC-49R1's expected bounds were set from the bounds already observed (disclosed), so it is a re-read, not a blind test |
| **CH-16** (LOW, process, D7) | Record REC's use of Proof outputs or re-issue REC as pre-Proof snapshot; separate stage records | REC addendum §4: finding accepted; per-class Proof-independence table; PC citations re-labelled as post-Proof annotations; forward process correction | The retrospective table is correct: re-deriving the classes from A1/A2 rules alone gives the same classes and counts. **But R1 repeated the pattern**: the REC addendum was created at 15:19:43, after Proof execution (disclosed); and the A2 addendum was created at 15:18:33, **after** the Proof predeclaration (15:17:13) and Proof execution (15:17:31) — **not disclosed** in the A2 addendum. The Proof header lists both addenda as "inputs" although neither existed when its cases were predeclared and executed | **PARTIALLY CLOSED** (retrospective closed; stage-record separation not achieved in R1). See RD-5 |
| **CH-19** (LOW, D6) | Add lineage-only mappings for Q019 and Q020 | REC addendum §3: Q019 → REC-04/05/35/37; Q020 → REC-30/35/32; "no evidence yet" 9 → 7 | Mappings checked against bank hypotheses and cited source: topical, lineage-only, answer nothing. Correct | **CLOSED**. New residual RD-6 (Rule 3: other "no evidence" QIDs not re-scanned) |
| **CH-21** (LOW, D4) | Restate REC-11 and PC-40 uid per trigger type | REC-11-R1 table; PC-40R1 | Rules come back in the caller's environment from an elevated lookup (event paths = triggering user); message and onchange use the posting/form environment; time path = job user; webhook route public-auth with elevated rule lookup; action lists are elevated in every path. Reproduced. Public-user resolution rests on base A1 C25 (base `http` not re-read by any stage) | **CLOSED**. Cross-lineage notes carried: base A1 CRQ-01 "runs without a user" vs public auth; base A1 C29 "not in superuser mode at entry" is true only when the configured user is not the superuser id (base lineage) |

Summary: 6 CLOSED (CH-08, CH-09, CH-10, CH-12, CH-19, CH-21), 1 PARTIALLY CLOSED (CH-16), 0 OPEN.

## 2. Independent re-derivations

### 2.1 CH-10 — cron-wide stall and deactivation

1. **One job for all time rules.** The module data file ships exactly one scheduled-job record (inactive at ship, 4-hour interval, no-update flag, calls the time processor). The processor searches all active rules of the three time triggers and iterates them in one run. **Confirmed.**
2. **Every run with a failing rule is FAILED.** After each successful rule the processor calls the scheduler's commit-progress with no arguments, so the processed increment is zero and "done" stays zero. On a rule failure it rolls back, keeps the error, continues, and re-raises the last error after the loop. The scheduler's run loop classifies "action raised" as FAILED unless both done and remaining are non-zero; done is always zero for this module, so the run is FAILED even when other rules committed. **Confirmed.**
3. **Deactivation thresholds.** Constants: at least 5 failures; 7 days. The test joins both with AND and the time delta is strict (first failure plus 7 days earlier than now). On deactivation: active off, counter and first-failure reset, admin hook called; the base hook only writes a warning to the server log. Any non-FAILED status resets both counters. Under continuous failure at the 4-hour default, the count threshold is met long before the time threshold, so the effective trigger is the first FAILED run more than 7 days after the first failure. **Confirmed.**
4. **Blast radius.** Deactivation turns off the single job, so every time rule stops. **Confirmed** (A2 O3-R1 and REC-27 correct).
5. **Restart triggers.** The job's active flag is written only by the module's cron-update routine, called from rule create, rule delete, and rule write when a critical field (model, active, trigger, on-change fields) or a delay-range field changes; plus manual edit of the job. There is no timer-based or self-healing path. **Confirmed.** Additional nuances not stated by the addenda (INFO, see RD-3): (a) the routine returns silently if it cannot lock the job row (the O10 behaviour), so a restart attempt concurrent with a locked job is a no-op; (b) it sets active only when at least one active time rule exists; (c) a create/delete/critical write of **any** rule, including non-time rules, re-activates the job; (d) counters were reset at deactivation, so after re-activation a still-failing rule needs a fresh full cycle (at least 5 FAILED runs over more than 7 days) before the next deactivation — the job oscillates rather than stays off.
6. **Additional FAILED route (INFO, RD-3).** The scheduler also classifies a run as FAILED without executing it when the job has timed out at least 3 consecutive times and the last progress shows no work done. Because this module never reports a done count, repeated worker timeouts (for example a large backlog) also feed the same failure counter and can lead to deactivation with no rule error at all. Runtime-only; not covered by any case.

### 2.2 O18 / REC-BAUT-47 — selection outside per-rule isolation

In the processor loop the order is: narrow guard around the rule-existence check; then record selection (apply-on condition evaluation and search) **outside** any guard; then a guard around per-record processing and flush only; then the last-run write and commit-progress, also outside the guard. **O18 confirmed**: a selection error propagates immediately, is not stored as the "last error", ends the run, leaves later rules unprocessed in that run, and the run is FAILED (rules earlier in the order have already committed). REC-47 class UNKNOWN_PENDING_PROOF, Lane B UNCORROBORATED, links PC-62/PC-65: consistent with the parent REC rule.

Refinements (RD-2): (a) if the selection error is persistent, rules after the failing rule in iteration order never run in any run, not only "that run" — and O3-R1's "healthy rules still advance within each run" holds only for processing-phase failures; (b) a persistent selection error also drives the CH-10 deactivation path; (c) an error in the last-run write is likewise not isolated; (d) PC-65's "lower-id rule first" relies on the rule model declaring no ordering attribute (confirmed: none declared) and on the ORM default ordering, which no stage has read.

### 2.3 New defect found during re-derivation (RD-1)

The rule model's ACL file has a single row granting access only to the settings (system) group. The time processor searches the rule model and writes last-run **without elevation**, in the job user's environment. Statically, then, if the job is reassigned to an ordinary internal user who is not in the settings group, the run is predicted to fail at the rule lookup with an access error before any selection happens (ORM access enforcement not re-read here; this rests on the ACL file and standard model-access semantics). Consequences:
- A2 O14-R1 and the C11 note ("a reassigned ordinary user would apply that user's rights to record selection") are incomplete. For a non-settings user the predicted effect is not restricted selection but a FAILED run with nothing processed, which then feeds the CH-10 deactivation path.
- PR-29 / PC-64 step (ii) reassigns the job to "internal user U". As designed, the fail condition (X2 stamped, or uid not the job user) would not fire, but the expected result "only X1 stamped" would also not be observed. The case cannot discriminate the claim unless U is a settings-group user and X2 is hidden from U by a record rule that applies to that group.

## 3. Re-executed static cases (independent)

Executed from this re-check's own blobs; log `a3r1_baut/exec_log.txt` (sha256 `ab1e9de6…dc97`). Each was evaluated against the **predeclared** fail condition in `531f5951…456d`.

| Case | Predeclared fail condition | A3 R1 observation | A3 R1 result |
|---|---|---|---|
| PC-BAUT-56 | Positive count passed; run classified partially/fully done; final error swallowed | Commit-progress called with no arguments; classifier makes "raised, done zero" FAILED; last error re-raised | **REPRODUCED PASS** |
| PC-BAUT-57 | Threshold absent/different; OR-logic; no reset on success | 5 and 7 days; AND; strict delta; reset on deactivation and on non-FAILED; hook = log warning | **REPRODUCED PASS** |
| PC-BAUT-58 | Per-rule jobs; self-healing path | One job record; only two references to it (cron-update routine and a navigation action); no self-healing path | **REPRODUCED PASS** |
| PC-BAUT-59 | Elevation on time-path search/eval context; an event path non-elevated | Zero elevation calls in the selection routine and the processor; eval context carries current env uid/user; pre/post filter helpers filter an elevated copy | **REPRODUCED PASS** |
| PC-BAUT-60 | Job env from another identity; user set in data; non-superuser loading env | Both scheduler entry points build the environment from the job's user id; environment forces superuser mode for the superuser id; data file has no user; field default is the current user; loader builds a superuser environment and passes it down to data loading (conversion layer unread) | **REPRODUCED PASS** (static; prediction for PC-63) |
| PC-BAUT-61 | Immediate send; rollback does not clear; no rollback | Send registered post-commit; cancel notice post-rollback; rollback clears post-commit first; processor rolls back on failure | **REPRODUCED PASS** |
| PC-BAUT-62 | Selection inside the isolation block | Selection call precedes the guard that wraps processing | **REPRODUCED PASS** |
| PC-BAUT-49R1 | Any bound inclusivity differs; user time zone applied | Operator sequence matches all three branches; no user time zone | **REPRODUCED PASS** |
| PC-BAUT-40R1 | Different uid source; run on non-elevated list | As in CH-21 row; action lists elevated on every path | **REPRODUCED PASS** (static only) |
| PC-BAUT-42R1 | Company field / record rule present; qualifier fails | ACL single settings-group row; per-path qualifier holds. Note RD-1 affects O14-R1's ordinary-user branch, which PC-42R1 does not test | **REPRODUCED PASS** |

10 of 10 addendum static cases reproduced; 0 disagreements on the predeclared fail conditions. Evidential weight: the predeclared expectations were written by the same controller after its own source re-read (disclosed), so the Proof addendum PASSes are single-reader re-reads. This independent re-execution supplies the second reading.

## 4. Supersede map and totals

| Check | Result |
|---|---|
| Supersede map (Proof §1) against predeclared file | Identical: 12→12R1, 13→13R1, 40→40R1, 42→42R1, 49→49R1; new 56..62 static, 63..65 runtime |
| Static active | Parent 28 (PC-28..55) − 3 + 3 + 7 = **35**; all PASS → PASS 35 |
| Runtime active | Parent 27 (PC-01..27) − 2 + 2 + 3 = **30**; all NOT-EXECUTED |
| Total | **65 active: 35 PASS / 0 FAIL / 30 NOT-EXECUTED** — **CONSISTENT** |
| Superseded retained for lineage | 5 (not counted) — consistent |
| A2 proof requirements | 27 − 2 + 2 + 3 = 30 — consistent |
| REC | 46 + REC-47 = 47; MATCH 16, CONTRADICTION 5, UNKNOWN_PENDING_PROOF 21 (C06, C09, C11, C14, C18, C20, O2–O9, O11, O13–O18), GAP 5; Lane B UNCORROBORATED 38 + NOT_APPLICABLE 9 = 47 — consistent |
| QID lineage | 31 + 2 = 33 mapped; "no evidence yet" 9 − 2 = 7 — arithmetic consistent (see RD-6 for content) |

Minor inconsistencies (no count effect): the runtime PC-12R1 row in the Proof addendum adds a step ("then write a delay-range field on a rule") and a positive expectation ("the job re-activates after the rule write") absent from the predeclared runtime steps; PC-64 drops the predeclared fail condition "flag not set in the action" and the expected "flag set" in step (i). Neither is tagged POST-DECLARATION (RD-4).

## 5. Disclosures adjudicated

| Disclosure | Adjudication |
|---|---|
| One controller wrote all three addenda (separation of duties) | A2, REC and PROOF are sequential stages; the protocol's independence requirement falls on A3, not on each pair of upstream stages. For these items the **content** is not materially compromised: every static statement was re-derived by this independent reviewer from source and reproduced (sections 2–3), and the one new defect found (RD-1) is an incompleteness, not a reversal. The **process** is compromised: the same reader predeclared, executed and then wrote the A2 and REC records afterwards, so the stage records do not evidence stage order. Sustained as RD-5 (LOW, process) |
| Expected results not blind to source | Accepted and weighed: the 10 static PASSes are treated as single-reader re-reads, corroborated only by this re-check. For static source cases, blindness is inherently limited; the residual risk is a shared misreading, which the independent re-execution did not find |
| REC addendum written after Proof static run, claiming no Proof dependency | Claim **verified**: no REC class, basis correction or lineage entry in the addendum depends on a Proof addendum PASS/FAIL; PC IDs appear only as link targets. Ordering defect stands (Rule 4), disclosed |
| A2 addendum ordering (not disclosed) | The A2 addendum file was created **after** the Proof predeclaration and execution. The A2 addendum text does not disclose this, and the Proof header lists it as an input. No Proof-result citation was found in the A2 addendum text, so no content dependency is evidenced; the defect is disclosure and ordering (RD-5) |
| New files read (`environments.py`, `sql_db.py`, `loading.py`) | Blobs recorded (A2 addendum §0.1) and **independently re-verified** (9 of 9 match). The cited sections (superuser-id rule; commit/rollback callback handling; superuser loading environment) say what the addenda state. These are new evidence pointers without Lane A lineage records; Lane A should register them if they are to be relied on beyond this remediation |

## 6. Systemic process rules (MASTER C1-B) — compliance of R1

The rules were committed at 15:20:45Z, after the A2 (15:18:45) and REC (15:19:52) addenda were committed and 8 seconds before the Proof addendum commit. Compliance is recorded for routing; non-compliance by artifacts that pre-date the rule is not a violation of a rule in force, but the gap must be closed before MASTER consumption.

| Rule | R1 compliance | Evidence |
|---|---|---|
| 1. Preserve A2 `MISSING_REQUIRED_RUNTIME_PROOF`; do not collapse into UNCORROBORATED | **NOT MET** | The REC addendum keeps the collapsed Lane B column (REC-47 = UNCORROBORATED; totals UNCORROBORATED 38). The parent A2 uses the label 12 times; the A2 addendum assigns none to O18. REC's own §4 cites the A2 labels as class basis, so the information exists but is not preserved as a label |
| 2. Untagged post-declaration Expected text prohibited | **PARTIALLY MET** | Static cases match the predeclaration in substance. Runtime PC-12R1 adds an untagged step and expectation; PC-64 silently drops a fail condition and an expectation element (RD-4) |
| 3. REC must scan all A1 item classes for "no evidence" QIDs | **PARTIALLY MET** | Q019/Q020 re-assessed. The remaining 7 were not re-scanned against A1 BR/F/G/CRQ items or the new O3-R1/O18. Topical candidates exist: Q028 (one customer's trigger storm must not exhaust shared capacity) ↔ O3-R1/O18 (one rule's failure stops or starves the single shared job for all rules); Q024 (restore must not replay completed effects without deduplication) ↔ A1 G9 / CRQ-04 (no deduplication or idempotency marker) (RD-6) |
| 4. REC frozen (sha256) before PROOF executes; PROOF header records the REC sha256 consumed | **NOT MET** | REC addendum created 15:19:43, after Proof execution 15:17:31 (disclosed). The Proof header records the REC addendum sha256 as an input it could not have consumed at predeclaration or execution |
| 5. Cases file sha256 + UTC timestamp written before the first source fetch | **NOT MET** | Source fetch 15:13:40–15:14:39; predeclaration hashed 15:17:13. The sha256 and timestamp exist only as scratch files (not committed, not externally anchored). Disclosed as "not blind" |

Integration Control corrective rule (accurate commit subjects): **NOT MET**. The three addenda sit in commits whose subjects name other modules (resource/resource_mail, bus/digest, web_unsplash). Commit `6ef8bef` "remediation R1 G01: base_automation addenda" (15:21:58Z, after the rule) contains only the html_editor A3 file. Content lineage is intact: each committed blob equals the current file and the recorded hash.

## 7. Clean-room scan

| Target | Result |
|---|---|
| A2, REC and PROOF addenda R1; predeclared cases file | No fenced code, no code statements, no reuse or adoption recommendation, no schema reproduction, no percentages, no Formal Coverage claim. Identifiers appear only as pointers. Field-level paraphrase (for example, the list of critical fields as "model, active, trigger, on-change fields") stays at pointer level — **PASS** |
| Scratch execution logs (`remed_baut/exec_log.txt`; this re-check's `a3r1_baut/exec_log.txt`) | Contain verbatim vendor source lines as grep output. Acceptable only as un-governed scratch evidence; they must not be promoted into governed artifacts or design stages — **OBSERVATION** |
| This re-check | Paraphrase only; no vendor code — **PASS** |

## 8. Residual defects routed

| # | Severity | Owner | Required action |
|---|---|---|---|
| RD-1 | LOW-MED | **A2**, then **PROOF** | Qualify O14-R1 / C11 note: the time processor reads and writes the rule model unelevated, and that model is accessible only to the settings group, so reassignment to a non-settings user is predicted to FAIL every run at rule lookup (feeding CH-10), not to restrict selection. Re-predeclare PR-29 / PC-64 (ii) with U in the settings group and X2 hidden by a record rule that applies to U, and add a variant with a non-settings U whose expected result is a FAILED run with nothing processed |
| RD-2 | LOW | **A2** (wording), **PROOF** (optional case) | O18 / O3-R1: state that a persistent selection error starves all later rules in every run (not only "that run") and also drives deactivation; "healthy rules advance within each run" holds only for processing-phase failures. Note that the last-run write is also outside isolation. PC-65 ordering depends on the unread ORM default ordering |
| RD-3 | INFO / LOW | **A2** note; **PROOF** runtime candidate | Add to O3-R1: repeated worker timeouts are also FAILED for this module (no done count) and feed deactivation; restart via cron-update is a silent no-op on lock failure and requires at least one active time rule; any rule's create/delete/critical write re-activates; counters restart after re-activation, so a persistent failure makes the job oscillate |
| RD-4 | LOW | **PROOF** | Tag the PC-12R1 added step and expectation as `POST-DECLARATION`; restore the predeclared PC-64 fail condition "flag not set in the action" and expected "flag set" in (i), or record the removal as a tagged post-declaration change (MASTER Rule 2) |
| RD-5 | LOW (process) | **A2**, **REC**, **Integration Control / MASTER** | A2 addendum: disclose that it was recorded after the Proof predeclaration and execution. Proof header: record the addenda as "recorded after execution", not "inputs". Future remediation rounds: freeze A2 then REC (hashed and committed with accurate subjects) before Proof predeclaration, and write the predeclaration before the first source fetch (Rules 4 and 5; Integration Control subject rule) |
| RD-6 | LOW | **REC** | Rule 1: restore the A2 `MISSING_REQUIRED_RUNTIME_PROOF` label alongside the Lane B column for UNKNOWN items, including REC-47 (A2 to assign O18's label). Rule 3: re-scan the 7 "no evidence yet" QIDs against all A1 item classes and R1 findings; at minimum evaluate Q028 ↔ O3-R1/O18 and Q024 ↔ G9/CRQ-04 (lineage only) |

No residual reverses a MATCH, CONTRADICTION or UNKNOWN_PENDING_PROOF class or any static PASS. No item returns to A1.

## 9. Runtime-blocked items (NOT-EXECUTED; neither passed nor failed)

- All 30 active runtime/config cases, including PC-12R1 (deactivation), PC-13R1 (post-commit suppression), PC-63 (default job user), PC-64 (time-path identity; see RD-1 before execution) and PC-65 (O18).
- 21 UNKNOWN_PENDING_PROOF items and the runtime effect of the 5 CONTRADICTION items remain open. A full A3 → MASTER sufficiency judgement is not possible until runtime executes.

## 10. Limitations

- Static only; every "predicted" statement is a source reading, not an observation.
- Not read by this re-check: ORM model-access enforcement and default ordering (RD-1 and RD-2(d) rest on the ACL file and standard semantics); the data-conversion layer (default job user remains a prediction for PC-63); base `http`/`ir_http` public-user resolution; the restricted evaluator; other modules' overrides of the scheduler's admin-notification hook.
- Stage timing rests on local file birth/mtime and single git commits; predeclaration files are scratch-only and not externally anchored.
- QID review for Rule 3 was topical and covered only the 7 remaining "no evidence" QIDs; it is not a coverage measure.
- No percentages. No Formal Coverage claim. No QID answered. No git write operations. Inputs were not edited. Source copies are held only in scratchpad `a3r1_baut/src/`.
