# G01 PLATFORM_BASE — RED TEAM Reconciliation Addendum R1 (A3 remediation) — `base_automation`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **RECONCILIATION (REC)**. This is an addendum only. The parent REC is immutable and was not edited |
| Group / Module | G01 PLATFORM_BASE / `base_automation` |
| Parent artifact | `A1_SOURCE_EVIDENCE_LANE/G01_RECONCILIATION/G01_BASE_AUTOMATION_REC_20260927.md`, sha256 `6f4471f430863392e757f99fc3a818cf60a0820350a724fa3720b1f2a39ed0ab` (unchanged since A3 intake) |
| A3 report | `A1_SOURCE_EVIDENCE_LANE/G01_A3_CHALLENGES/G01_BASE_AUTOMATION_A3_STATIC_20260927.md`, sha256 `9b8bb57ab6bd62bf4b2165a06c4e31dfe612d48b1fa746e304520511938b1604` |
| Additional inputs (immutable) | A2 addendum R1 `G01_A2_REVIEWS/G01_BASE_AUTOMATION_A2_ADDENDUM_R1_20260927.md` (written before this addendum in the same remediation); base A1 `G01_A1_PACKAGES/G01_BASE_A1_PACKAGE_20260927.md` sha256 `a45a2beff88b8be61cd81b6075f7072f156c1b9d1d93029f0afb6ad35a0189e7` (C25, C27, C29), which was absent at the parent's intake; question bank sha256 `3c38cec4aa1ef2aa92d0e850da0d18242da9dc7c6ef7bd137c433edb379b9a49`, which equals FREEZE_W1-B02 (re-verified 2026-09-27 15:15 UTC); freeze hash `cd966040f720456420057fe98fdb1176fbb9b0e85b456891f4dab82ea3ba0202` |
| Challenge IDs addressed | **CH-21** (LOW, D4, REC part), **CH-19** (LOW, D6), **CH-16** (LOW process, D7). Carry-forward of CH-10 and CH-08 into the bases of REC-20, REC-27 and REC-38 |
| Date | 2026-09-27 |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

Clean-room note: this addendum contains neutral paraphrase only, with identifiers used as pointers. No vendor code. No percentages. No Formal Coverage claim. No QID is answered. No git operations. No existing artifact was edited.

## 1. CH-21: REC-BAUT-11 execution identity restated per trigger type

**Parent basis text (defective wording):** "…the base run path evaluates in that elevated environment with the triggering uid."

**Corrected basis (REC-11-R1).** In every path, actions are dispatched from an elevated action list, and elevation keeps the uid of the environment it came from. The uid that expressions see and that is carried into run depends on the trigger type:

| Trigger type | Effective uid (static) | Evidence pointers |
|---|---|---|
| Record events: create, create-or-edit, field-value-set, archive/unarchive, delete, and the recompute path | **The triggering user** (the environment of the operation that fired the rule) | Module model patch makers and the lookup helper (rules returned in the caller's environment); base A1 C27 |
| Message received/sent | **The triggering user** (the posting environment) | Module model message patch |
| UI change (onchange) | **The triggering user** (the editing user's form environment) | Module model onchange maker |
| Time-based (three variants) | **The scheduled job's configured user**. The shipped job sets no user, and the predicted default is the superuser account, created under the superuser loading environment (A2-R1-02). Under that default the environment is superuser-mode by configuration. A reassigned ordinary user would apply that user's rights to record selection | Base `ir_cron.py` (job environment built from the configured user); ORM environments (superuser id forces superuser mode); module data (no user set); base A1 C29 |
| Webhook | **The public user**, resolved by the public-auth route. The rule is then loaded elevated | Module controller route (public auth); base A1 C25 ("public falls back to the public user") |

Cross-lineage note, carried and not resolved here: base A1 CRQ-01 says the webhook route "runs without a user". That conflicts with the public auth level and belongs to the base lineage (A3 CH-21).

REC-11 class: **unchanged, UNKNOWN_PENDING_PROOF.** Final identity and privilege effect remain runtime items. Proof links, updated: PC-BAUT-40R1 (replaces PC-40); runtime PC-01 (event), PC-02 (webhook), PC-63 (default job user), PC-64 (time path).

## 2. Carry-forward of basis corrections (no class change)

| REC ID | Item | Basis addendum | Class | Proof link update |
|---|---|---|---|---|
| REC-BAUT-27 | O3 | Per A2 O3-R1, the consequence goes beyond a single-rule stall. Every run that contains the failing rule is FAILED, because the module reports no processed counts. After at least 5 FAILED runs spanning more than 7 days, the single shared job is deactivated and all time rules stop until a rule create/delete, a critical or delay-range write, or a manual edit. New O18: an error during record selection aborts the rest of the run | UNKNOWN_PENDING_PROOF (unchanged) | PC-12 → **PC-12R1**; static PC-56, PC-57, PC-58; new PC-65 (O18) |
| REC-BAUT-20 | C20 | Per A2-R1-03, the standard outbound-webhook action sends only after commit and is cancelled on rollback. The "external side effects already sent" RISK does not apply to that action type. It remains open only for action types with immediate external effects, and none is evident in the module | UNKNOWN_PENDING_PROOF (unchanged) | PC-13 → **PC-13R1**; static PC-61 |
| REC-BAUT-38 | O14 | Per A2 O14-R1, elevated condition evaluation applies to the event, message, onchange and webhook paths. On the time path, condition evaluation runs in the job user's environment | UNKNOWN_PENDING_PROOF (unchanged) | PC-42 → **PC-42R1**; static PC-59, PC-60; runtime PC-64 |
| REC-BAUT-35 | O11 | Window-bound precision per PC-49R1: datetime fields use an inclusive lower and exclusive upper bound; date fields an exclusive lower and inclusive upper bound; calendar mode an inclusive lower and exclusive upper bound | UNKNOWN_PENDING_PROOF (unchanged) | PC-49 → **PC-49R1** |

New REC item for the A2-R1 omission O18:

| REC ID | Item | A1 | A2 | REC class | Basis | Lane B | Proof link | QID lineage |
|---|---|---|---|---|---|---|---|---|
| REC-BAUT-47 | O18 | (not stated) | O18 MED (A2 addendum R1): time-rule record selection sits outside the per-rule isolation, so a selection error aborts the rest of the run | UNKNOWN_PENDING_PROOF | An A2 omission that is predicted only statically (parent rule). The run-level effect is runtime | UNCORROBORATED | PC-62; PC-65 | Q009, Q014, Q034 |

Counts after addendum: MATCH 16, CONTRADICTION 5, UNKNOWN_PENDING_PROOF **21**, GAP 5. Total **47**. Lane B: UNCORROBORATED 38, NOT_APPLICABLE 9, and no FAIL for absence.

## 3. CH-19: QID lineage re-assessment for Q019 and Q020 (lineage only, not answers)

Bank text (paraphrased). Q019: archived or inactive records are processed only if a rule explicitly includes them. Q020: deletion of a target before deferred execution fails safely and does not retarget.

| QID | Added mapped REC items | Evidence pointers (topical relevance only) |
|---|---|---|
| G01-BASE_AUTOMATION-Q019 | REC-04 (C04), REC-05 (C05), REC-35 (O11), REC-37 (O13) | C04: the trigger taxonomy includes archive and unarchive triggers. C05: those triggers resolve by convention to the model's active-flag field (module model convention resolver, boolean active or customization-prefixed active). O11: time-path records are re-selected at job time through a model search in the job environment, and the module sets no active-test override on that search. The effect of default active filtering is an ORM behaviour not read here (the PC-30 limitation). O13 and the rule-level active filtering relate to rule lifecycle only; they are included because the bank's precondition covers deactivation before execution. Event paths act on the records supplied by the triggering operation, and no active-state check on target records is evident in the module. That is a runtime question and **not** an answer |
| G01-BASE_AUTOMATION-Q020 | REC-30 (O6/F2), REC-35 (O11), REC-32 (O8) | O6 and F2: the webhook path checks that the resolved record exists and raises a validation error, which becomes a generic 500 response, when it does not. There is no fallback target. O11: the time path keeps no stored queue of targets; it re-selects records at job time, so a deleted target is not in the selection. O8: delete-trigger actions run before the deletion. Deferred post-commit outbound sends (A2-R1-03) serialize the record values at action time, before commit. Topical only; the runtime outcome is open |

Updated section 3 totals: **33 QIDs mapped** (31 + Q019, Q020). **"No evidence yet": 7 QIDs**: Q017, Q024, Q025, Q026, Q027, Q028 and Q033. Q019 and Q020 are removed from that list. The mapping answers no QID and satisfies no disconfirming observation. It is not a coverage measure.

## 4. CH-16: process finding and corrective statement

**Finding (accepted).** The parent REC was finalised after the static Proof cases (PC-28..55) had been executed by the same controller. Its "Basis for class" column cites static Proof results (for example "PC-44 PASS" and "PC-50 PASS"), and its limitations say it used them. The REC→PROOF stage separation was therefore not kept in the record: REC was not handed off to Proof before Proof ran. Integration Control has already been informed by A3.

**Corrective statement: which REC classes are independent of Proof results.** Each class was re-derived here from the parent's predeclared rules using **only** A1 and A2 inputs, ignoring every PC citation:

| Class | Items | Derivation without Proof | Independent of Proof? |
|---|---|---|---|
| MATCH (16) | C01–C05, C07, C08, C10, C13, C15–C17, C21–C23, O12 | A1 claim together with an A2 VERIFIED verdict from A2's own source re-read (A2 T3). O12 comes from A2's source finding in the direction of A1's C03 RISK | **Yes** |
| CONTRADICTION, A1 vs A2 (2) | C12, C19 | A2 PARTIAL verdicts. The parent rule maps a PARTIAL to CONTRADICTION | **Yes** |
| CONTRADICTION, source vs intent (3) | C24, O1, O10 | A2's source findings (C24 confirmed at source; O1; O10 docstring conflict) | **Yes** |
| UNKNOWN_PENDING_PROOF (20 + REC-47) | C06, C09, C11, C14, C18, C20, O2–O9, O11, O13–O18 | A2 MISSING_REQUIRED_RUNTIME_PROOF labels, or an A2 omission predicted only statically | **Yes** |
| GAP (5) | G1, G2, G3, G5, G6 | A1 gaps carried, which nothing in scope can close | **Yes** |

Conclusion: **no REC class depends on a Proof result.** The Proof-derived content in the parent is limited to (a) the "Proof link" column and (b) PC-xx citations and phrases such as "confirmed statically (PC-nn)" in the "Basis for class" column. From this addendum on, both are to be read as **post-Proof corroborative annotations**, not as classification inputs. Without them the parent's classes, counts and Lane B labels stand unchanged.

**Process correction for future runs:** hand REC off as a separate, hashed record before any Proof execution. Proof results may be referenced only in a later, labelled REC addendum.

## 5. Handoff and limitations

- Handoff: to PROOF (addendum R1: PC-12R1, PC-13R1, PC-40R1, PC-42R1, PC-49R1, PC-56..65), then back to A3 for re-check.
- Timing disclosure: this addendum was written after the A2 addendum R1 and after the Proof addendum R1 cases were predeclared (predeclaration hashed at 15:17:13 UTC). The Proof static execution log (`remed_baut/exec_log.txt`, 15:17:31 UTC) had also already been captured when this file was written. This addendum **cites no Proof addendum result**: every class, basis correction and lineage entry above rests on A1, A2, the A2 addendum R1, base A1 and the bank, and none depends on a Proof PASS or FAIL. The PC IDs appear only as link targets. This ordering repeats the CH-16 pattern in a milder form, and it is recorded here so that A3 can judge it.
- The same controller authored the A2, REC and PROOF addenda R1. That independence limitation is disclosed.
- No runtime evidence exists and no Lane B evidence exists. Absence is not treated as failure. No percentages, no Formal Coverage claim, no git operations, and no existing file was edited.
