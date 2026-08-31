# [SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-011]
# GROUP A — CORR-010 Formal Independent Business Process & Design Re-Verification / EXPERT IBPV / L999.999

## SINGLE END-TO-END SELF-STARTING FORMAL IBPV PROMPT

Project: SMEsPlus ENTERPRISE SUITE  
STATE: STATE03 — Architecture  
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification  
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone  
Boss: Sole Final Approver  
Control Level: `/L999.999`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Canonical Governance Baseline at Prompt Creation: `b95f6ce7391a1ee6215df205f9b0baed58e93636`  
Original TEAM B Design Commit: `b98a3b9fb435845dbd15fae79db63b0b73a82420`  
TEAM B CORR-008 Frozen Input: `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`  
Prior Formal IBPV RV-009 Final Commit: `b2f7cbd3131963fca176a0ac0939c4bdf8af3e25`  
TEAM B CORR-010 Baseline-Correction Commit: `a08300bc817a52595d29759f11f71f6f69d1dbfb`  
TEAM B CORR-010 Final Executor Commit: `e44186448eaae38926a78447639d6fa693cc1a6f`  
CORR-010 Five-Unit Governance Commit: `36820bf574272fc1d818da178584fd4cec04826b`  
RV-011 Five-Unit Readiness Commit: `b95f6ce7391a1ee6215df205f9b0baed58e93636`  
Dedicated Independent Branch: `ibpv/group-a-sip-nonacct-reverification-011`  
Risk: HIGH  
Readiness: READY  
STEP Binding: `TBD / BASELINE LINKAGE REQUIRED — DO NOT INVENT`  
Jira Key: `TBD / DO NOT INVENT`

This is the **only execution instruction for this session**.

**ONE SESSION = ONE END-TO-END PROMPT.**

Do **not** ask Boss for a separate `START`, `CONTINUE`, `NEXT`, `COMMIT`, `PUSH`, or routine phase-by-phase confirmation.

Execution mode:

`AUTO-CONTINUE`  
`AUTO-COMMIT/PUSH EVIDENCE`  
`NO ROUTINE CONFIRMATION`  
`ASK BOSS ONLY ON TRUE STOP CONDITIONS`

---

## 1. Mission

Independently re-verify TEAM B CORR-010 and determine whether every authorized **non-Accounting** correction is genuinely closed at the business-process/design level.

Do not accept TEAM B's self-declared closure as evidence.

The target successful meaning is narrow:

`NON-ACCOUNTING GROUP A CORRECTIVE ITEMS VERIFIED CLOSED`

while preserving:

`PRE-DEVELOPMENT GATE HOLD — WAITING FOR ACCOUNTING/AR-AP AND OTHER CONTROLLED DEPENDENCIES`.

This session must **not** authorize Team C, Development, merge, Release, Production, Formal IDTM, Formal IESA, or final design approval.

---

## 2. Independence and Source-Control Rules

You are an Independent Formal IBPV reviewer.

You must not:

- edit TEAM B design files;
- edit CORR-010 executor evidence;
- repair findings while reviewing them;
- merge branches;
- resolve Accounting/AR-AP facts for GROUP A;
- infer unavailable legacy approval internals;
- set Boss/business policy defaults;
- redesign Multi-Approve;
- convert carry-forward unknowns into facts;
- authorize Team C or Development.

You may create only independent RV-011 verification artifacts under the RV-011 folder on the dedicated IBPV branch.

---

## 3. Mandatory Inputs — Verify Every Coordinate Before Use

### 3.1 TEAM B corrected package

Freeze and inspect:

`claude/team-b-group-a-sip-nonacct-corr-010`

at:

`e44186448eaae38926a78447639d6fa693cc1a6f`

Confirm its parent chain includes:

- `a08300bc817a52595d29759f11f71f6f69d1dbfb` — CORR-010 baseline corrections;
- `b2f7cbd3131963fca176a0ac0939c4bdf8af3e25` — prior Formal IBPV RV-009;
- `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45` — CORR-008 corrected package.

### 3.2 CORR-010 evidence files

Inspect all files `29–38` under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/CORRECTIVE_CORR_010/`

Mandatory focus:

- `29_CORR010_PREFLIGHT_AND_FINDING_REPRODUCTION.md`
- `30_CORR010_EVENT_RACE_AND_RESERVATION_ATOMICITY_CLOSURE.md`
- `31_CORR010_EVT001_004_005_ZERO_SILENT_DROP_REGISTER.md`
- `32_CORR010_B1_B8_PRECISION_CLEANUP_REGISTER.md`
- `33_CORR010_APPROVAL_AND_MULTI_APPROVE_INTERFACE_BOUNDARY.md`
- `34_CORR010_ACCOUNTING_HOLD_AND_RESIDUAL_DEPENDENCY_MATRIX.md`
- `35_CORR010_CROSS_FILE_REGRESSION_AND_CONSISTENCY_REPORT.md`
- `36_CORR010_FORMAL_IBPV_REVERIFICATION_READINESS.md`
- `37_SESSION_SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-010_CLOSURE.md`
- `38_CORR010_FINAL_SHA256_MANIFEST.txt`

Treat all of these as TEAM B claims/evidence to verify — not independent proof.

### 3.3 Prior Formal IBPV baseline

Read RV-009, especially:

- `03_RV009_NINE_FINDING_REVERIFICATION_MATRIX.md`
- `04_RV009_STATE_EVENT_AND_E2E_REVERIFICATION.md`
- `05_RV009_APPROVAL_PERMISSION_SOD_REVERIFICATION.md`
- `06_RV009_RETRY_IDEMPOTENCY_FAILURE_RECOVERY_REVERIFICATION.md`
- `10_RV009_REGRESSION_AND_CROSS_FILE_CONSISTENCY_REPORT.md`
- `11_RV009_RESIDUAL_OPEN_ITEM_AND_BLOCKING_RULE_REGISTER.md`
- `12_RV009_REQUIREMENT_EVIDENCE_DESIGN_TRACEABILITY_RECHECK.md`
- `13_RV009_FORMAL_IBPV_INDEPENDENT_REVERIFICATION_REPORT.md`
- `14_RV009_PRE_DEVELOPMENT_GATE_RECOMMENDATION_TO_BOSS.md`
- `15_RV009_BOSS_DECISION_INPUT_REGISTER.md`

Reproduce the original concern before judging CORR-010.

### 3.4 Governance evidence that CORR-010 executor reported missing

Mandatory independent check:

Commit:

`36820bf574272fc1d818da178584fd4cec04826b`

Expected file:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/GROUP_A_SALES_INVENTORY_PURCHASE/GROUP_A_CORR010_NON_ACCOUNTING_PRE_PROMPT_FIVE_UNIT_CHALLENGE.md`

Also inspect the RV-011 readiness record at canonical commit:

`b95f6ce7391a1ee6215df205f9b0baed58e93636`

Do not limit repository verification to ancestry of the TEAM B branch. Inspect the remote canonical `SMEsPlus` lineage and exact commit directly.

If `36820bf...` and the file exist remotely but are absent from the CORR-010 branch ancestry/local view, classify accurately as:

`GOVERNANCE EVIDENCE EXISTS — CROSS-BRANCH TRACEABILITY / LINEAGE VISIBILITY ISSUE`

or another evidence-supported equivalent.

Do **not** retain `EVIDENCE DOES NOT EXIST` if remote evidence proves existence.

If exact root cause of the executor visibility mismatch cannot be proven, do not guess it.

---

## 4. Five-Unit Controls Embedded in Execution

### Audit VETO

- No self-review by TEAM B.
- No evidence invention.
- Re-perform hashes independently.
- Verify exact branch/commit ancestry.
- Distinguish remote evidence existence from audited-lineage reachability.
- No silent waiver.
- No Gate PASS by prose assertion.

### TBRAC

- No new Thailand-wide claims.
- Preserve evidence classifications and real-user-validation requirements.
- Do not convert generic concurrency/control design into Thai statutory or common-practice claims.

### IBPV

- Verify process/state/event/owner/handoff/invariant completeness.
- Verify cross-module effects and exceptions.
- Verify Approval interface boundaries without designing the engine.
- Verify Accounting dependency remains isolated.

### IDTM Advisory

- Challenge future testability of race/idempotency/atomicity semantics.
- No Formal IDTM execution.
- No implementation-technology prescription.

### IESA Advisory

- Challenge ERP/SaaS system integrity and Tenant/Company boundaries.
- No Formal IESA assurance.
- No release/production authorization.

---

## 5. Mandatory Independent Re-Performance

### RV11-01 — `FV006-EVT-004` Ordering Race

Reproduce the RV-009 finding first.

Then verify CORR-010's design independently:

1. Does the corrected rule remove the self-contradictory FIFO/no-ordering wording?
2. Is correctness genuinely ordering-independent for same-line different-event-type arrival?
3. Does the consumer re-read current authoritative state rather than apply stale event-carried values?
4. What happens if quantity-change arrives before fulfillment-request?
5. What happens on replay/redelivery?
6. Does idempotency still apply?
7. Does unresolved handoff remain separately observable rather than being masked by this rule?
8. Is the design technology-neutral?
9. Are all cross-references correct?

Construct at least one explicit counterexample attempt. If the rule fails under any realistic ordering, mark `GAP FOUND`.

### RV11-02 — `FV006-EVT-005` Reservation-Claim Atomicity

Reproduce the original simultaneous-claim gap.

Independently verify:

1. Inventory is canonical owner of reservation truth.
2. Evaluation uses authoritative Available truth at commit point, not stale pre-read truth.
3. Two simultaneous claims cannot jointly commit beyond available quantity.
4. Full/partial/zero outcomes are observable.
5. No claim silently disappears.
6. Same-business-identity retries cannot double-commit.
7. Release/cancel restores availability only for later evaluation.
8. Tenant/Company/bin scope is explicit.
9. No database-lock/CAS/queue mechanism is prescribed as architecture fact.

Use the concrete oracle:

Given On-Hand=10 and two simultaneous claims of 6 each, total committed allocation must never exceed 10.

Verify that the design is precise enough for future testing without prescribing implementation.

### RV11-03 — `FV006-EVT-001` Dead-Event-Catalog Question

Verify CORR-010 did not falsely claim resolution.

Confirm:

- it is now registered in the controlled unknown/carry-forward mechanism;
- status reflects `CONTROLLED CARRY-FORWARD` or equivalent, not fabricated closure;
- owner/next decision point is identifiable;
- no live event is deleted merely to make the register clean.

### RV11-04 — RV-009 B1–B8 Precision Cleanup

Re-check all eight individually.

At minimum verify:

- B1 `Rejected` state enumeration + correct approval-control cross-reference;
- B2 fulfillment/reservation trigger naming in idempotency language;
- B3 Handoff-Unresolved non-disappearance guarantee + corrected references;
- B4 residual `sequential/ordered` wording is properly qualified;
- B5 self-approval remains substantively correct without unnecessary modification;
- B6 event-transport wording no longer contains the RV-009 contradiction;
- B7 handling-unit/archival citation correction;
- B8 evidenced-vs-Team-B-extension labeling accurately counts and classifies the master concepts.

Search package-wide for residual contradictory phrases rather than trusting TEAM B's own cleanup register.

### RV11-05 — Zero-Silent-Drop / New Carry-Forwards

Verify file 18 and CORR-010 file 31 contain correct current disposition for:

- `FV006-EVT-001`;
- `FV006-EVT-004`;
- `FV006-EVT-005`;
- N12 reservation tie-break policy;
- N13 dead-event inclusion-rule question.

Closed findings may remain in the register as resolved audit trail; open questions must not be mislabeled as closed.

### RV11-06 — Approval / Multi-Approve Interface Boundary

Verify CORR-010 stayed within GROUP A authority.

Confirm it may define only the business contract such as:

- facts supplied for approval;
- generic decision outputs;
- actor/timestamp/reason/audit requirements;
- source-module state/event consequences;
- SoD/self-approval target requirements.

Confirm it did **not** design:

- approval engine internals;
- rule DSL;
- physical schema;
- approver-resolution algorithm;
- company-specific approval policy;
- legacy internal workflow from missing evidence.

Legacy fidelity gap A2 must remain controlled unless new authoritative evidence exists.

### RV11-07 — Accounting HOLD Isolation

Verify CORR-010 did not answer Accounting's questions.

A1 must remain:

`HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY`

Check that GROUP A only asks for an authoritative interface contract concerning relevant Customer Invoice/AR and Vendor Bill/AP states and does not invent `posted / locked / reconciled / reversed` semantics.

This review must not decide cancellation symmetry itself.

### RV11-08 — Governance Evidence / Branch-Lineage Classification

Independently verify:

1. commit `36820bf574272fc1d818da178584fd4cec04826b` exists;
2. it contains the CORR-010 Five-Unit challenge artifact;
3. the artifact is reachable on the canonical `SMEsPlus` lineage or exact commit;
4. whether it is or is not in the TEAM B CORR-010 branch ancestry;
5. whether the CORR-010 executor's `NOT FOUND` statement therefore describes local/lineage visibility rather than repository-wide nonexistence.

Correct the current classification in RV-011 evidence. Do not edit TEAM B historical files merely to make them say something different; preserve them as historical executor observations and supersede them in the independent review.

### RV11-09 — Manifest / Repository Integrity

Independently recompute CORR-010 file `38` hashes for every listed file.

Verify:

- exact match count;
- no missing path;
- no duplicate path;
- file 38 self-hash limitation is accurately described;
- file 21 and file 28 remain historical manifests rather than overwritten current manifests;
- TEAM A / prior IBPV evidence was not modified by CORR-010;
- no unrelated file was included in the corrective delta.

Integrity PASS is not design PASS. Report separately.

### RV11-10 — Cross-File Regression / System Consistency

Perform a fresh sweep across every CORR-010-modified baseline file and material dependents.

Check at minimum:

- state/event ownership;
- demand/supply handoff consistency;
- cancel/reject wind-down;
- idempotency vs concurrency separation;
- reservation quantity conservation;
- retry/replay behavior;
- Approval/SoD boundary;
- Tenant/Company boundaries;
- archival/history preservation;
- no Accounting Core authority crossing;
- no new unregistered assumption.

---

## 6. Controlled Residuals — Mandatory Zero-Silent-Drop Reassessment

Reassess and report current status without self-closing:

### A1 — Sales cancellation gate / Accounting-AR/AP dependency

Expected current status:

`HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY`

### A2 — Legacy approval internal workflow/permission evidence

Expected current status:

`EVIDENCE MISSING / BOSS DECISION REQUIRED`

Do not confuse vendor-neutral target approval design with proof of legacy behavior.

### A3 — Three deferred policy defaults

- canonical Invoiced Quantity definition;
- Over-Fulfillment / Over-Billing default;
- Sales Confirmation Gate default.

Reconfirm whether they remain safe to defer. If CORR-010 changed their decision deadline, cite exact evidence.

### C4 — TEAM A evidence branch-lineage integration

Treat as PMO/repository-governance action unless evidence shows otherwise.

### N12 / N13

Verify they are genuinely open business/evidence questions and correctly classified.

---

## 7. Required Execution Phases

Execute automatically unless a True Stop Condition occurs.

### PHASE 0 — Preflight / Independence

- verify repo, branches, commits, governance;
- verify independent branch is based on `e4418644...`;
- verify reviewer is not modifying TEAM B artifacts.

### PHASE 1 — Integrity / SHA Reproduction

- reproduce CORR-010 manifest;
- verify changed files and branch ancestry.

### PHASE 2 — Governance Evidence Discrepancy Reconciliation

- independently inspect `36820bf...` and the Five-Unit file;
- record accurate repository-existence vs lineage-reachability classification.

### PHASE 3 — Original Finding Reproduction

- reproduce RV-009 EVT-004, EVT-005, EVT-001 and B1–B8 before judging corrections.

### PHASE 4 — Event Race / Ordering Re-Verification

- execute RV11-01.

### PHASE 5 — Reservation Atomicity Re-Verification

- execute RV11-02.

### PHASE 6 — Carry-Forward / Zero-Silent-Drop Re-Verification

- execute RV11-03 and RV11-05.

### PHASE 7 — Precision Cleanup / Cross-File Regression

- execute RV11-04 and RV11-10.

### PHASE 8 — Approval / Multi-Approve Boundary

- execute RV11-06.

### PHASE 9 — Accounting and Controlled Residual Boundary

- execute RV11-07 and §6 reassessment.

### PHASE 10 — Blocking Rule Assessment

For every material item state:

- `VERIFIED`;
- `VERIFIED WITH CONDITIONS`;
- `GAP FOUND`;
- `CONFLICT FOUND`;
- `EVIDENCE MISSING`;
- owner;
- exact next action;
- whether it blocks non-Accounting closure;
- whether it blocks the final Pre-Development Gate.

### PHASE 11 — Report / Manifest / Commit / Push

- create all required RV-011 deliverables;
- create final SHA manifest over RV-011 evidence, excluding manifest self-hash;
- commit and push to dedicated IBPV branch;
- issue exactly one terminal recommendation.

---

## 8. Required Deliverables

Create under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/EXPERT_IBPV/GROUP_A_SALES_INVENTORY_PURCHASE/FORMAL_REVERIFICATION_RV_011/`

on:

`ibpv/group-a-sip-nonacct-reverification-011`

### 01 — `01_RV011_PREFLIGHT_AND_INDEPENDENCE_VERIFICATION.md`

### 02 — `02_RV011_CORR010_PACKAGE_INTEGRITY_AND_SHA_REPRODUCTION.md`

### 03 — `03_RV011_GOVERNANCE_EVIDENCE_LINEAGE_RECONCILIATION.md`

Must explicitly resolve the `36820bf...` / Five-Unit artifact existence classification.

### 04 — `04_RV011_EVENT_ORDERING_RACE_REVERIFICATION.md`

### 05 — `05_RV011_RESERVATION_CLAIM_ATOMICITY_REVERIFICATION.md`

### 06 — `06_RV011_EVT001_AND_ZERO_SILENT_DROP_REVERIFICATION.md`

### 07 — `07_RV011_B1_B8_PRECISION_CLEANUP_REVERIFICATION.md`

### 08 — `08_RV011_APPROVAL_MULTI_APPROVE_BOUNDARY_REVERIFICATION.md`

### 09 — `09_RV011_ACCOUNTING_HOLD_AND_CONTROLLED_RESIDUAL_REVIEW.md`

### 10 — `10_RV011_CROSS_FILE_REGRESSION_AND_SYSTEM_CONSISTENCY.md`

### 11 — `11_RV011_RESIDUAL_OPEN_ITEM_AND_BLOCKING_RULE_REGISTER.md`

Zero-silent-drop register for A1/A2/A3/C4/N12/N13 and any new material finding.

### 12 — `12_RV011_REQUIREMENT_EVIDENCE_DESIGN_TRACEABILITY_RECHECK.md`

### 13 — `13_RV011_FORMAL_IBPV_INDEPENDENT_REVERIFICATION_REPORT.md`

### 14 — `14_RV011_NEXT_STEP_RECOMMENDATION_TO_BOSS.md`

Clearly distinguish:

- non-Accounting items independently verified closed;
- non-Accounting items still requiring rework, if any;
- Accounting-dependent HOLD;
- Boss-decision items;
- PMO/repository-governance actions;
- items safe to defer.

Do not recommend Team C authorization while the controlled Pre-Development blockers remain open.

### 15 — `15_RV011_BOSS_DECISION_AND_DEPENDENCY_INPUT_REGISTER.md`

### 16 — `16_SESSION_SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-011_CLOSURE.md`

### 17 — `17_RV011_FINAL_SHA256_MANIFEST.txt`

Hash RV-011 files 01–16; do not self-hash file 17.

---

## 9. Acceptance Criteria

A successful independent non-Accounting closure requires all of the following:

1. EVT-004 closure independently survives counterexample testing.
2. EVT-005 closure independently demonstrates quantity-conservation/atomicity semantics.
3. EVT-001 remains honestly registered, not fabricated as resolved.
4. B1–B8 are correctly corrected or accurately reclassified.
5. No material new contradiction is introduced.
6. Approval/Multi-Approve boundary remains clean.
7. No Accounting-owned fact is invented.
8. `36820bf...` and Five-Unit governance evidence classification is corrected from repository-wide nonexistence if remote evidence proves existence.
9. All residuals are zero-silent-drop registered.
10. Manifest independently reproduces.
11. Pre-Development Gate remains HOLD for Accounting/controlled dependencies.

---

## 10. True Stop Conditions

Stop and ask Boss only if:

- frozen commit/branch identity cannot be resolved;
- material evidence required for re-performance is genuinely unavailable everywhere accessible;
- a destructive/irreversible/live-system write would be required;
- scope would need expansion into Accounting Core design, Multi-Approve engine design, Team C, or another formal lifecycle stage;
- evidence proves a material contradiction that cannot safely remain a registered `CONFLICT FOUND`/`HOLD` without immediate Boss ruling.

Do not stop for routine uncertainty that can safely be registered and carried forward.

---

## 11. Permitted Terminal Status

If all authorized non-Accounting corrections independently verify:

`FORMAL IBPV CORR-010 RE-VERIFICATION COMPLETE — NON-ACCOUNTING CLOSURE VERIFIED — PRE-DEVELOPMENT GATE STILL HOLD FOR ACCOUNTING/CONTROLLED DEPENDENCIES — READY FOR BOSS NEXT-STEP DECISION`

If material non-Accounting rework remains:

`FORMAL IBPV CORR-010 RE-VERIFICATION COMPLETE — REWORK REQUIRED / NOT READY FOR NEXT GATE`

If material verification evidence is unavailable:

`EVIDENCE MISSING / NOT READY FOR NEXT GATE`

No other terminal wording may imply Team C authorization, final design approval, Pre-Development Gate PASS, Development readiness, Release, or Production readiness.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
