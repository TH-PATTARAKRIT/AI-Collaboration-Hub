# [SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-PHASE-S-CLOSURE-001]
# PHASE S FINAL OWNER-BOUNDED CORRECTION, FRESH CHALLENGE, VERIFICATION & BOSS CLOSURE
# /L99999.99999

## 0. PROJECT IDENTITY

Project: SMEsPlus ENTERPRISE SUITE
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Canonical Branch: `SMEsPlus`
Parent Control Session: `[SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-XRECON-001]`
Execution Mode: CONTROLLED CONTINUATION / OWNER-BOUNDED / EVIDENCE-FIRST
Boss: Sole Final Approver

Absolute rules:

- No Evidence = No Progress.
- Never Skip Gate.
- Understand deeply.
- Transfer accurately.
- Preserve verifiably.
- No repeated question without a material delta.
- Reopen/continue means accumulated learning + current evidence, NEVER reset.

This prompt is NOT a new research round.
This prompt is NOT a reset.
This prompt is NOT permission to restart from L1.
This prompt is NOT Functional Design.
This prompt is NOT implementation.
This prompt is NOT merge/release authorization.

Its sole purpose is to drive the existing P06 / P08 / P09 / P11 Phase S work through exact bounded correction, fresh independent challenge, verification, Veto disposition, and preparation of the Phase S Final Boss Closure Gate.

---

## 1. EXISTING OWNER SESSIONS — DO NOT CREATE REPLACEMENT SESSIONS

Continue the existing owner sessions only:

### P06 — Bank-to-Reconcile
Branch:
`research/account-p06-bank-to-reconcile-2026-09-04-001`
Expected current HEAD at prompt issue time:
`1b018c104001eb4683166518a6161a8cd8ab5cee`
Known terminal control state at prompt issue time:
`G02-P06 INDEPENDENT VERIFICATION NOT PROVABLE — EVIDENCE INTEGRITY HOLD`
`AASP-VETO-07 NOT DISCHARGED`

### P08 — Record-to-Report
Branch:
`research/account-p08-record-to-report-2026-09-04-001`
Expected current HEAD at prompt issue time:
`00ccd663d55d72830c8e0db46e4cc1aa345d0af1`
Known terminal control state at prompt issue time:
`TERMINAL STATE C`
Evidence-integrity and domain-purity defects remain.

### P09 — Plan-to-Analyze
Branch:
`research/account-p09-plan-to-analyze-2026-09-04-001`
Expected current branch HEAD at prompt issue time:
`ec4d3d2f32c8ae72e53f043f53783beb07071ffb`
Authoritative published bounded-correction surface recorded by that HEAD:
`4778792196371c460d3e6ca87bf8d9adee760f47`
Known terminal control state:
`TERMINAL B — MATERIAL CORRECTION DEFECT REMAINS`
Known unresolved control points include M-1 / M-2 and `AAS+-VETO-04 NOT DISCHARGED`.

### P11 — Account Core Reconciliation
Branch:
`research/account-core-reconciliation-2026-09-04-001`
Expected current HEAD at prompt issue time:
`dc4cc4a6bb1ea2fac071925f5eb1c01c44072c4b`
Known terminal control state:
`TERMINAL B — MATERIAL EVIDENCE-INTEGRITY DEFECT REMAINS — EXACT BOUNDED CORRECTION REQUIRED`
Current round already received independent AAS-03 challenge on frozen surface `935655779a85defb97fbb1e2039726f0dfffc9cd`.

### P07 — READ-ONLY DEPENDENCY ONLY
P07 is NOT an execution owner in this prompt.
Do NOT mutate P07 under this prompt.
Current dependency branch at prompt issue time:
`research/account-p07-th-tax-compliance-2026-09-04-001`
Expected HEAD:
`ee2be30ebf155e241510b3c7133c69419eb060a0`
P07 may be consumed only as shared-handoff / contradiction / dependency evidence where required by P06/P08/P09/P11 or Phase S closure verification.

If Phase S cannot close because P07 itself requires mutation, do NOT silently expand scope. Publish:
`HOLD — P07 OWNER ACTION REQUIRED`
and generate a separate P07 continuation recommendation for Boss review.

---

## 2. MANDATORY PRE-FLIGHT — VERIFY BEFORE MUTATION

Before any correction:

1. Fetch all owner branches.
2. Record current remote HEAD SHA for P06 / P08 / P09 / P11.
3. Compare against the expected SHAs above.
4. If a branch moved:
   - do not assume drift is harmless;
   - inspect only the delta needed to classify it;
   - record whether it is bookkeeping-only, evidence change, correction change, challenge result, or material research delta;
   - use the verified current authoritative surface.
5. Freeze the exact pre-correction baseline for each owner.
6. Record artifact paths, evidence IDs, Veto IDs, unresolved conditions, and Boss Decision dependencies.

Create/update:

`00_PHASE_S_PRE_EXECUTION_FREEZE.md`

Mandatory fields per owner:

- Owner
- Branch
- Pre-correction HEAD
- Authoritative terminal artifact(s)
- Terminal state
- Open material defects
- Open correction requirements
- Open Vetoes
- Required fresh challenge condition
- Boss-only decisions
- Cross-package dependencies
- Mutation permission = NO until Q-BOSS-01

Do not use approximate defect counts from memory when exact current evidence exists.

---

## 3. XRECON CONTROL INPUTS

Consume the parent XRECON session:

`[SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-XRECON-001]`

Required control artifacts are logically:

1. Frozen evidence snapshot
2. Cross-Pxx defect register
3. Root-defect reconciliation
4. Propagation / contradiction mapping
5. Veto / decision dependency mapping
6. Re-challenge requirement mapping
7. `07_OWNER_BOUNDED_CORRECTION_QUEUE`
8. `08_OWNER_CORRECTION_PROMPTS`

If 07 and 08 are already published and current, verify and consume them.

If 07 and/or 08 are absent, stale, or not provably current:

- reconstruct ONLY the missing XRECON control artifacts from the frozen/current evidence;
- do NOT execute any owner correction yet;
- publish the corrected 07 and 08;
- stop at `Q-BOSS-01 — BOSS CORRECTION AUTHORIZATION REQUIRED`.

The owner correction queue is authoritative for WHAT may be changed.
This master prompt governs HOW the corrections must be executed and verified.

---

## 4. BOSS AUTHORIZATION GATE — Q-BOSS-01

No owner correction may begin until Q-BOSS-01 is explicitly recorded as APPROVED.

Required Boss decision:

`Q-BOSS-01 — AUTHORIZE OWNER-BOUNDED PHASE S CORRECTIONS FOR P06 / P08 / P09 / P11`

Allowed values:

- APPROVED
- APPROVED WITH LIMITS
- HOLD
- REJECTED

If Q-BOSS-01 is absent or not approved:

STOP after publishing the Boss Review Pack.
Do not infer approval from silence.
Do not treat creation of this prompt as execution authorization.

If APPROVED or APPROVED WITH LIMITS:
continue autonomously through all non-Boss execution steps below.

Do not ask Boss intermediate questions unless an unresolved Boss-only decision blocks all remaining execution. Otherwise record the dependency and continue all non-blocked lanes.

---

## 5. OWNER-BOUNDED EXECUTION MODEL

Execute P06 / P08 / P09 / P11 as four isolated owner lanes.

Rules:

- Keep each owner on its existing branch/session lineage.
- No cross-owner mutation.
- No shared contaminated worktree.
- No unrelated cleanup.
- No adjacent-domain redesign.
- No new research except the minimum bounded evidence acquisition explicitly required to close a registered defect/condition.
- Preserve superseded evidence as lineage; do not erase history.
- Every changed claim must point to the exact evidence that changed it.
- Every unchanged material claim challenged this round must record why it survived.

For each owner:

A. Consume its assigned queue items only.
B. State the exact correction scope before editing.
C. Correct the evidence / method / register / instrument / wording / provenance defect.
D. Re-run the required bounded evidence test.
E. Publish corrected evidence.
F. Freeze the corrected surface at an immutable SHA.
G. Hand that frozen SHA to an independent challenge lane.
H. Do not edit the frozen surface while challenge is running.
I. Accept, dispute with evidence, or route every challenge finding.
J. If challenge finds a new material defect, perform only the bounded follow-up correction required by that finding, freeze again, and fresh-challenge the changed surface.
K. Continue until the owner's required verification condition is satisfied or the owner reaches a defensible HOLD.

---

## 6. OWNER-SPECIFIC NON-NEGOTIABLE CLOSURE OBJECTIVES

### 6.1 P06

Must not close merely because evidence was republished.
The Phase S objective is to resolve or correctly disposition the evidence-integrity hold and satisfy the independent-verification requirement attached to P06's current Veto/control conditions.

At minimum:

- prove the correction surface is independently verifiable;
- preserve provenance from the pre-correction surface;
- do not let the P06 executor self-certify independence;
- keep `AASP-VETO-07` standing until independent evidence satisfies its lifting condition.

### 6.2 P08

P08 is not eligible for Phase S closure while Terminal State C conditions remain unresolved.

At minimum:

- correct registered evidence-integrity defects;
- correct registered domain-purity defects;
- resolve all queue items that were answerable from evidence already in declared scope;
- ensure no local control certifies a wider population than it actually tested;
- freeze the corrected surface;
- perform a genuinely independent pass over the corrections.

P08 may NOT self-discharge the independent-pass condition.

### 6.3 P09

At minimum:

- resolve M-1 with either a defensible replacement authority or an explicit bounded disposition that does not overclaim exclusion authority;
- satisfy M-2 by fresh-challenging the corrected surface;
- preserve all prior superseded statements and tombstones;
- re-test the exact corrected producer/control surface, not a detached second script that does not govern the produced result;
- keep `AAS+-VETO-04` standing until its evidence condition is independently satisfied.

### 6.4 P11

At minimum:

- repair the evidence-intake/currentness instrument so its control design is independently falsifiable;
- no head/tail/sampling/limit/first-N population bounding where the governing standard prohibits it;
- preserve generation/path identity where basename alone is ambiguous;
- no raw substring membership that admits unrelated artefacts;
- no tautological blind-spot control;
- control sets must not be self-selected in a way that makes failure impossible;
- re-evaluate all P11 conclusions affected by the repaired intake/currentness surface;
- explicitly disposition P07/P09 cross-package items already identified in current P11 evidence;
- freeze corrected surface and submit it to fresh independent challenge.

P11 may not self-discharge `AASP-P11-C3-VETO-04` or any equivalent independent-control requirement.

---

## 7. FRESH CHALLENGE STANDARD

Fresh challenge is mandatory whenever a material evidence surface, instrument, denominator, classification, currentness rule, or correction claim changes.

Challenge requirements:

1. Challenge reads the frozen corrected SHA, not a moving branch.
2. Challenge body must be independent of the owner executor for the challenged control.
3. Challenge must attempt falsification, not confirmation.
4. Challenge must test the actual producer/instrument used for the published result.
5. Synthetic controls are allowed only if they can genuinely fail.
6. Negative controls must be selected independently of the rule being tested.
7. Challenge must preserve disagreements; do not force consensus.
8. Every challenge finding receives one disposition:
   - ACCEPTED
   - ACCEPTED WITH RE-SCOPE
   - DISPUTED WITH EVIDENCE
   - NOT MATERIAL TO THIS OWNER QUEUE
   - ROUTED TO ANOTHER OWNER
   - BOSS DECISION REQUIRED
9. Any new material correction after challenge invalidates the old challenge for the changed surface and requires a fresh challenge of that changed surface.

---

## 8. CROSS-PACKAGE RE-VERIFICATION AFTER OWNER CORRECTIONS

After all four owner lanes reach a terminal post-correction state, return to the XRECON control layer.

Re-run cross-package verification for:

- duplicated defects
- shared root causes
- propagated false claims
- withdrawn claims still consumed by another package
- stale SHA / stale generation references
- unresolved contradictions
- handoff written vs handoff actually received
- Veto lifting dependencies
- Boss Decision dependencies
- P07 read-only shared-handoff dependencies that affect closure

No package may be declared clean if another package still consumes its superseded/withdrawn claim as current authority.

---

## 9. VETO DISPOSITION RULE

No owner may self-discharge a Veto whose lifting condition requires independent proof.

For every Veto, record:

- Veto ID
- Owner
- Original condition
- Current evidence
- Challenge evidence
- Cross-package dependency
- Lifting test
- Result
- Disposition
- Authority that may discharge it

Allowed dispositions:

- DISCHARGED BY VERIFIED EVIDENCE
- PARTIALLY SATISFIED — REMAINS OPEN
- UPHELD
- SUPERSEDED WITH LINEAGE
- ROUTED
- BOSS DECISION REQUIRED

Do not use `CLOSED` as a synonym for `DISCHARGED` unless the lifting test is actually satisfied.

---

## 10. REQUIRED OUTPUTS

Publish, at minimum:

### Pre-authorization / XRECON controls

`00_PHASE_S_PRE_EXECUTION_FREEZE.md`
`01_PHASE_S_ROOT_DEFECT_RECONCILIATION.md`
`02_PHASE_S_PROPAGATION_CONTRADICTION_MATRIX.md`
`03_PHASE_S_VETO_DECISION_DEPENDENCY_MATRIX.md`
`04_PHASE_S_RECHALLENGE_REQUIREMENT_MATRIX.md`
`05_PHASE_S_CLOSURE_CRITERIA_REGISTER.md`
`06_PHASE_S_BOSS_REVIEW_PACK.md`
`07_OWNER_BOUNDED_CORRECTION_QUEUE.md`
`08_OWNER_CORRECTION_PROMPTS.md`

### Post-Q-BOSS-01 execution evidence

`09_OWNER_CORRECTION_EXECUTION_REGISTER.md`
`10_FRESH_CHALLENGE_RESULT_REGISTER.md`
`11_POST_CORRECTION_CROSS_PACKAGE_VERIFICATION.md`
`12_VETO_DISPOSITION_REGISTER.md`
`13_OPEN_BOSS_DECISIONS_REGISTER.md`
`14_PHASE_S_FINAL_CLOSURE_EVIDENCE.md`
`15_PHASE_S_BOSS_FINAL_DECISION_PACK.md`
`PHASE_S_AUTO_RESUME_STATE.md`
`PHASE_S_CHECKPOINT_REGISTER.md`

Every output must include exact Branch + Commit SHA + Artifact Path for all evidence it relies on.

---

## 11. CHECKPOINTS / AUTO-RESUME

Mandatory checkpoints:

- CP-SC-00 Context + parent session reattached
- CP-SC-01 Current owner heads verified
- CP-SC-02 Frozen pre-correction baselines published
- CP-SC-03 XRECON 07/08 verified or rebuilt
- CP-SC-04 Q-BOSS-01 status recorded
- CP-SC-05 P06 bounded correction frozen
- CP-SC-06 P08 bounded correction frozen
- CP-SC-07 P09 bounded correction frozen
- CP-SC-08 P11 bounded correction frozen
- CP-SC-09 Fresh challenges complete
- CP-SC-10 Cross-package post-correction verification complete
- CP-SC-11 Veto dispositions complete
- CP-SC-12 Boss-only decisions consolidated
- CP-SC-13 Phase S closure evidence published
- CP-SC-14 READY FOR BOSS PHASE S FINAL DECISION

Maintain auto-resume after every material checkpoint.
If interrupted, resume from the last proven checkpoint only.
Never restart L1.

---

## 12. PHASE S CLOSURE TEST

Phase S may be recommended for closure only if ALL are true:

1. Every P06/P08/P09/P11 owner correction queue item has a terminal disposition.
2. Every changed material surface received the required fresh challenge.
3. No material evidence-integrity defect remains unbounded/unclassified.
4. No unresolved cross-package contradiction is being consumed as current authority.
5. No stale or superseded evidence is silently treated as current.
6. Every Veto has a defensible disposition and lifting evidence where required.
7. Every Boss-only decision is explicitly listed; none is silently decided by AI.
8. P07 read-only dependencies have been checked for closure impact.
9. No implementation / Functional Design / Phase A/B/C work has started.
10. All evidence is published with immutable SHA + path and remote read-back verification.

If all ten pass:

Terminal recommendation:
`READY FOR BOSS PHASE S FINAL CLOSURE DECISION`

If any fails but the remaining work is exactly bounded and available:

Terminal recommendation:
`PHASE S HOLD — EXACT BOUNDED REMEDIATION REMAINS`

If required evidence is unavailable:

Terminal recommendation:
`PHASE S HOLD — REQUIRED EVIDENCE UNAVAILABLE`

If P07 mutation becomes mandatory:

Terminal recommendation:
`PHASE S HOLD — P07 OWNER ACTION REQUIRED`

AI must NOT self-declare Phase S CLOSED.
Boss is the sole Final Approver.

---

## 13. ABSOLUTE PROHIBITIONS

During this prompt:

- NO reset.
- NO new session replacing P06/P08/P09/P11.
- NO restart from L1.
- NO broad Deep Research rerun.
- NO Functional Design.
- NO Phase A/B/C.
- NO production schema/API design.
- NO code implementation.
- NO merge/release.
- NO peer-owner mutation.
- NO self-discharge of independent Vetoes.
- NO silent assumption that an old challenge covers a newly changed surface.
- NO deletion of superseded evidence lineage.
- NO invented counts, IDs, SHAs, branches, artifact paths, or terminal states.
- NO Boss decision inferred from silence.

---

## 14. EXECUTION BEHAVIOR

Work autonomously after Q-BOSS-01 approval.
Do not require Boss to answer intermediate non-Boss questions.
Use evidence and the declared queue to resolve all executor-level questions.
Escalate only true Boss-only decisions.

If one owner lane is blocked, continue other non-blocked lanes where doing so cannot contaminate evidence or violate dependency ordering.

Do not optimize for speed by weakening evidence controls.
Do not create a PASS by narrowing denominators after seeing the result.
Do not treat publication as proof of correctness.

The goal is not to make Phase S look closed.
The goal is to make Phase S closure verifiable.

---

## 15. FINAL STOP CONDITION

When all possible work under this prompt is complete, publish the complete Boss Final Decision Pack and STOP at exactly one of:

`READY FOR BOSS PHASE S FINAL CLOSURE DECISION`

or

`PHASE S HOLD — EXACT BOUNDED REMEDIATION REMAINS`

or

`PHASE S HOLD — REQUIRED EVIDENCE UNAVAILABLE`

or

`PHASE S HOLD — P07 OWNER ACTION REQUIRED`

Do not start the next phase.
Do not perform Functional Design.
Do not merge or release.

Boss is the sole Final Approver.
