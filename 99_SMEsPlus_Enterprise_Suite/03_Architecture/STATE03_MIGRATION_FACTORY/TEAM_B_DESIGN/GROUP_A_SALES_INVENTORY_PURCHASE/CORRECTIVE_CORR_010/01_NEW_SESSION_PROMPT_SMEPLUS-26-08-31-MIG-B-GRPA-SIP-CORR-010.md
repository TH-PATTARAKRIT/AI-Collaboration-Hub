# [SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-010]
# GROUP A — Non-Accounting Targeted Pre-Gate Closure / TEAM B / L999.999

## SINGLE END-TO-END SELF-STARTING TEAM B CORRECTIVE PROMPT

Project: SMEsPlus ENTERPRISE SUITE  
STATE: STATE03 — Architecture  
Execution Team: TEAM B — Independent Canonical Domain Design / Corrective Rework  
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone  
Boss: Sole Final Approver  
Control Level: `/L999.999`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Canonical Governance Baseline at Prompt Creation: `36820bf574272fc1d818da178584fd4cec04826b`  
Original TEAM B Design Commit: `b98a3b9fb435845dbd15fae79db63b0b73a82420`  
TEAM B CORR-008 Corrected Frozen Input: `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`  
Formal IBPV RV-009 Final Commit: `b2f7cbd3131963fca176a0ac0939c4bdf8af3e25`  
Dedicated Corrective Branch: `claude/team-b-group-a-sip-nonacct-corr-010`  
Risk: HIGH  
Readiness: READY  
STEP Binding: `TBD / BASELINE LINKAGE REQUIRED — DO NOT INVENT`  
Jira Key: `TBD / DO NOT INVENT`

This is the **only execution instruction for this session**.

**ONE SESSION = ONE END-TO-END PROMPT.**

Do **not** ask Boss for separate `START`, `CONTINUE`, `NEXT`, `COMMIT`, `PUSH`, or routine phase-by-phase confirmation.

Execution mode:

`AUTO-CONTINUE`  
`AUTO-COMMIT/PUSH EVIDENCE`  
`NO ROUTINE CONFIRMATION`  
`ASK BOSS ONLY ON TRUE STOP CONDITIONS`

---

## 1. Boss-Controlled Mission

Boss has approved the following control rule:

> **Close all non-Accounting GROUP A work first. Do not declare Pre-Development Gate PASS until the required Accounting/AR-AP dependency is independently resolved.**

Your mission is therefore to close every TEAM-B-executable, non-Accounting finding surfaced by Formal IBPV RV-009, while explicitly preserving Accounting-dependent and Boss-decision-dependent items as controlled HOLD/carry-forward items.

The objective is **not** to make GROUP A Development-ready in this session. The objective is to reach:

`ALL AUTHORIZED NON-ACCOUNTING TEAM B ITEMS CLOSED — READY FOR INDEPENDENT IBPV RE-VERIFICATION — PRE-DEVELOPMENT GATE STILL HOLD FOR ACCOUNTING/CONTROLLED DEPENDENCIES`

if and only if the evidence supports that statement.

---

## 2. Governing Inputs — Verify Before Acting

You must independently verify every cited repository coordinate before treating it as ground truth.

Mandatory inputs:

1. TEAM B corrected package frozen at:
   `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`
2. Formal IBPV RV-009 branch/final commit:
   `b2f7cbd3131963fca176a0ac0939c4bdf8af3e25`
3. RV-009 artifacts, especially:
   - `03_RV009_NINE_FINDING_REVERIFICATION_MATRIX.md`
   - `04_RV009_STATE_EVENT_AND_E2E_REVERIFICATION.md`
   - `06_RV009_RETRY_IDEMPOTENCY_FAILURE_RECOVERY_REVERIFICATION.md`
   - `10_RV009_REGRESSION_AND_CROSS_FILE_CONSISTENCY_REPORT.md`
   - `11_RV009_RESIDUAL_OPEN_ITEM_AND_BLOCKING_RULE_REGISTER.md`
   - `12_RV009_REQUIREMENT_EVIDENCE_DESIGN_TRACEABILITY_RECHECK.md`
   - `13_RV009_FORMAL_IBPV_INDEPENDENT_REVERIFICATION_REPORT.md`
   - `14_RV009_PRE_DEVELOPMENT_GATE_RECOMMENDATION_TO_BOSS.md`
   - `15_RV009_BOSS_DECISION_INPUT_REGISTER.md`
4. Five-Unit readiness record:
   `BOSS_GATE/GROUP_A_SALES_INVENTORY_PURCHASE/GROUP_A_CORR010_NON_ACCOUNTING_PRE_PROMPT_FIVE_UNIT_CHALLENGE.md`
5. Applicable project governance, including EXPERT IBPV charter and clean-room rules.

Do not begin from TEAM B's previous self-closure statements. Reproduce the RV-009 findings first.

---

## 3. Hard Scope Boundary

### 3.1 Authorized non-Accounting closure scope

You are authorized to close:

A. `FV006-EVT-004` — ordering race condition.  
B. `FV006-EVT-005` — reservation-claim atomicity race.  
C. `FV006-EVT-001` — dead-event-catalog question: explicit registration and evidence-based disposition.  
D. RV-009 TEAM B light defects B1–B8.  
E. False/stale claims that `FV006-EVT-001/004/005` were already tracked.  
F. Cross-file consistency, evidence labels, exact section references and residual-register correctness directly affected by A–E.  
G. Corrective evidence, manifest and independent re-verification readiness.

### 3.2 Explicitly NOT authorized to self-close

#### A1 — Sales-side cancellation gate / Accounting-AR/AP dependency

Current control status:

`HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY`

Do not invent:

- Customer Invoice/AR internal lifecycle;
- Vendor Bill/AP internal lifecycle;
- posted/locked/reconciled accounting-state semantics;
- which Accounting fact must hard-block Sales cancellation.

GROUP A may state only the required interface question/contract boundary. It may not answer the Accounting-owned fact without authoritative Accounting evidence.

#### A2 — Legacy approval internal workflow/permission evidence

Current control status:

`EVIDENCE MISSING / BOSS DECISION REQUIRED`

Do not infer exact legacy level sequencing, transition logic, permissions, button behavior or internal enforcement from field names or historical row data.

The vendor-neutral target control already designed may remain, but legacy fidelity is not silently declared closed.

#### A3 — Three deferred policy defaults

- Canonical Invoiced Quantity definition;
- Over-Fulfillment / Over-Billing default;
- Sales Confirmation Gate default.

Treat as `SAFE TO DEFER` unless this correction uncovers new evidence that materially shortens the decision deadline. If so, document the exact dependency; do not choose the policy yourself.

#### C4 — TEAM A evidence branch-lineage integration

Owner: PMO / repository governance.

TEAM B may document exact missing lineage and required PMO action. TEAM B must not modify TEAM A evidence or fake branch ancestry.

---

## 4. Mandatory Findings to Close

### CORR10-01 — `FV006-EVT-004` Ordering Race

Formal IBPV found the catalog-wide ordering rule internally self-contradictory for the same business line when different event types interleave.

You must independently inspect the exact current wording and design a **single unambiguous canonical ordering invariant** at business-semantic level.

Minimum closure criteria:

1. Identify the exact business identity / ordering scope.
2. Define whether ordering is required across event types for the same originating business line.
3. Eliminate contradictory wording.
4. Define the observable truth when events arrive/replay out of order.
5. Preserve idempotency and unresolved-handoff behavior from CORR-008.
6. Do not prescribe Kafka, queues, locks, database technology or implementation mechanism.
7. Update every material cross-reference/summary affected by the correction.
8. Register `FV006-EVT-004` in file 18 with exact status and closure evidence.

If no safe vendor-neutral business invariant can be designed without additional business evidence, use `HOLD` rather than inventing one.

### CORR10-02 — `FV006-EVT-005` Reservation-Claim Atomicity Race

Formal IBPV found the reservation-claim atomicity race remains genuinely open.

Design a canonical business invariant that prevents two competing claims from both becoming valid against the same constrained inventory availability.

Minimum closure criteria:

1. Define canonical owner of the claim/reservation truth.
2. Define the business precondition for a valid claim.
3. Define the invariant preventing double allocation/over-claim.
4. Define the observable loser/outcome of competing claims.
5. Define state/event/audit consequences.
6. Keep Tenant + Company scoping explicit where applicable.
7. Remain technology-neutral; no physical locking/transaction/ORM/database prescription.
8. Ensure partial reservation, release/cancel and retry do not violate the invariant.
9. Register `FV006-EVT-005` in file 18 with exact status and closure evidence.

### CORR10-03 — `FV006-EVT-001` Dead-Event-Catalog Question

Reproduce the original concern from FV-006 and RV-009.

Then:

1. determine whether the event is genuinely required, conditionally required, superseded, or remains unknown;
2. do not delete an event solely to make the register clean;
3. state exact evidence/design rationale;
4. update file 18 with a zero-silent-drop disposition;
5. correct any stale statements elsewhere.

This item was non-blocking in RV-009, but it must be explicitly tracked/dispositioned now.

---

## 5. Mandatory RV-009 TEAM B Precision Cleanup — B1 through B8

Reproduce each RV-009 defect first, then correct it precisely.

### B1 — Denied-Approval Wind-Down Documentation

- Add `Rejected` to the canonical state enumeration where RV-009 found it missing.
- Repair the claimed approval-control cross-reference if it is absent/wrong.
- Do not invent legacy approval internals.

### B2 — Retry / Idempotency Wording

- Make the fulfillment-request/redelivery trigger coverage explicit where RV-009 found the wording indirect.
- Preserve the technology-neutral business invariant.

### B3 — Downstream-Failure Compensation Precision

- Correct wrong/nonexistent section references.
- State explicitly that an unresolved hard handoff cannot silently disappear from observable business truth.

### B4 — Sequential / Ordered Approval Wording Residue

- Find every material unqualified use of `sequential`, `ordered`, or equivalent in the TEAM B package.
- Qualify numbering/label order versus verified enforcement sequence consistently.
- Missing legacy gating evidence remains missing.

### B5 — Self-Approval Control

RV-009 found the substantive correction `VERIFIED` with no material residual defect.

Do not redesign it. Re-verify it did not regress as a consequence of other corrections and record `NO CHANGE REQUIRED` if true.

### B6 — Event Transport Semantics Precision

- Fix the ordering-clause defect together with CORR10-01.
- Remove/correct the false claim that `EVT-004/005` were already tracked in file 18.
- Ensure event transport, ordering, replay, idempotency and unresolved-handoff statements are mutually consistent.

### B7 — Lot/Serial / Package Ownership Citation

- Repair the mis-citation identified by RV-009 (`04` §09 vs actual applicable section, if independently confirmed).
- Do not alter the already-verified ownership semantics unless another evidence-based defect is found.

### B8 — Shared-Master Archival Evidence Labeling

- Preserve the general archival/hard-delete protection design if still sound.
- Explicitly distinguish which shared-master protections are individually TEAM-A-evidenced versus TEAM B's own canonical extension.
- Correct the undercount/labeling issue identified by RV-009.
- Do not claim all concepts were individually observed if they were not.

---

## 6. Approval / Multi-Approve Interface Boundary — Scope-Safe Only

This session may ensure GROUP A's approval-related business contract remains compatible with a configurable approval capability, but it must not design or implement a Multi-Approve engine.

Allowed GROUP A contract questions:

- What business facts does Sales/Purchase submit for an approval decision?
- What generic outputs are required (`APPROVED`, `REJECTED`, actor, reason, audit, effective decision)?
- What state/event consequences occur in the source module after a decision?
- What SoD/self-approval requirements must the approval capability satisfy?

Prohibited here:

- approval engine internals;
- rule DSL/schema;
- approver-resolution implementation;
- company-specific approval policies;
- database/API/ORM design;
- copying legacy approval logic.

Record any separate Multi-Approve design need as a handoff, not as GROUP A implementation.

---

## 7. Mandatory Accounting Hold Isolation

Create a dedicated residual dependency section that states at minimum:

`Sales-side cancellation-gate symmetry = HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY`

The section must identify the minimum authoritative interface facts GROUP A needs from Accounting, without answering them:

- relevant AR/customer-invoice lifecycle fact(s);
- relevant AP/vendor-bill lifecycle fact(s) where comparison is required;
- definition of posted/locked/reversed/settled significance to cancellation;
- exact Accounting fact, if any, that should hard-block cancellation.

Do **not** require all Accounting work to finish before GROUP A can proceed. The dependency is on an authoritative Accounting/AR-AP contract, not on blanket completion of the Accounting domain.

---

## 8. Required Execution Phases

Execute continuously unless a True Stop Condition occurs.

### PHASE 0 — Preflight / Frozen-Input Verification

Verify repo, branches, commits, RV-009 artifacts, Five-Unit record and dedicated branch lineage.

### PHASE 1 — Reproduce Current Findings

Reproduce C1/C2/C3 and B1–B8 directly from RV-009 and current TEAM B files. Build a before-correction matrix.

### PHASE 2 — Ordering Race Closure

Execute CORR10-01 and update all directly affected canonical artifacts.

### PHASE 3 — Reservation Atomicity Closure

Execute CORR10-02 and update all directly affected canonical artifacts.

### PHASE 4 — Dead-Event / Zero-Silent-Drop Registration

Execute CORR10-03; register `EVT-001/004/005`; correct false tracking claims.

### PHASE 5 — B1–B8 Precision Cleanup

Close each B-item or explicitly HOLD if the reproduced defect cannot be corrected safely within TEAM B authority.

### PHASE 6 — Approval Boundary Sanity Check

Confirm no correction invents legacy approval internals or redesigns Multi-Approve. Record scope-safe interface handoffs only.

### PHASE 7 — Accounting Hold Isolation / Residual Matrix

Create one canonical residual matrix covering A1, A2, A3, C4 and any newly discovered issue. No silent waiver.

### PHASE 8 — Cross-File Regression Sweep

Search all material TEAM B files for stale state/event/order/reservation/approval/citation/tracking language and contradictions introduced by the correction.

### PHASE 9 — Corrective Evidence / SHA

Create corrective artifacts listed in §9, recompute SHA-256 over the corrected package, and preserve prior manifests as historical evidence.

### PHASE 10 — Commit / Push / Closure

Commit in logical batches if useful, push only to `claude/team-b-group-a-sip-nonacct-corr-010`, verify remote head, working tree and exact changed-file set, then issue terminal status.

Do not merge to `SMEsPlus`.

---

## 9. Required Corrective Deliverables

Create under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/CORRECTIVE_CORR_010/`

### 29 — `29_CORR010_PREFLIGHT_AND_FINDING_REPRODUCTION.md`

Repo/commit verification, exact reproduced RV-009 findings and before-state.

### 30 — `30_CORR010_EVENT_RACE_AND_RESERVATION_ATOMICITY_CLOSURE.md`

Full closure evidence for `EVT-004` and `EVT-005`, including exact changed sections and future-verifiable invariants.

### 31 — `31_CORR010_EVT001_004_005_ZERO_SILENT_DROP_REGISTER.md`

Explicit disposition and registration proof for `EVT-001/004/005`.

### 32 — `32_CORR010_B1_B8_PRECISION_CLEANUP_REGISTER.md`

One row per B1–B8: reproduced defect, changed file/section, status, residual unknown.

### 33 — `33_CORR010_APPROVAL_AND_MULTI_APPROVE_INTERFACE_BOUNDARY.md`

Scope-safe approval-interface contract and explicit non-claims; no engine design.

### 34 — `34_CORR010_ACCOUNTING_HOLD_AND_RESIDUAL_DEPENDENCY_MATRIX.md`

Must include A1 Accounting HOLD, A2 legacy approval evidence/Boss decision, A3 deferred defaults, C4 PMO lineage action and any new residual.

### 35 — `35_CORR010_CROSS_FILE_REGRESSION_AND_CONSISTENCY_REPORT.md`

Package-wide regression sweep and stale-language search.

### 36 — `36_CORR010_FORMAL_IBPV_REVERIFICATION_READINESS.md`

State whether all authorized non-Accounting TEAM B items are materially closed. Do not conflate this with Gate PASS.

### 37 — `37_SESSION_SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-010_CLOSURE.md`

Session scope, commits, changed files, unresolved dependencies and terminal status.

### 38 — `38_CORR010_FINAL_SHA256_MANIFEST.txt`

Hash the current corrected TEAM B content package and corrective artifacts as reproducibly as possible. Do not self-hash file 38; document the self-reference limitation accurately.

---

## 10. Closure Criteria

You may declare a non-Accounting item CLOSED only if:

1. original RV-009 concern is reproduced;
2. corrected semantic/design text is explicit;
3. owner/state/event/handoff/invariant is explicit where applicable;
4. exact changed sections are cited;
5. cross-file references resolve;
6. no Accounting-owned fact is invented;
7. no legacy approval behavior is invented;
8. no Thailand-wide claim is invented;
9. residual unknowns are explicitly registered;
10. future independent IBPV can reproduce the closure from repository evidence.

A prose assertion such as `fixed` or `closed` without the above is not closure.

---

## 11. True Stop Conditions

Ask Boss only if one of these occurs:

- frozen commit/branch is missing or materially inconsistent;
- required correction would cross into Accounting Core internal design;
- required correction would require a new material business-policy decision not already controlled;
- destructive/irreversible/shared production write would be required;
- legal/license/clean-room boundary cannot be resolved safely;
- material evidence conflict cannot remain honestly `UNKNOWN/CONFLICTING EVIDENCE`;
- branch conflict makes safe isolated correction impossible.

Non-blocking unknowns must be registered and carried forward; they are not a reason for routine interruption.

---

## 12. Mandatory Terminal Status

If every authorized non-Accounting TEAM B item is materially closed, report exactly:

`TEAM B NON-ACCOUNTING CORRECTIVE CLOSURE COMPLETE — READY FOR FORMAL IBPV RE-VERIFICATION — PRE-DEVELOPMENT GATE STILL HOLD FOR ACCOUNTING/CONTROLLED DEPENDENCIES`

If any authorized non-Accounting blocker remains:

`TEAM B NON-ACCOUNTING CORRECTIVE CLOSURE INCOMPLETE — HOLD / REWORK REQUIRED`

Never output:

- `BOSS APPROVED`
- `FINAL APPROVED`
- `PRE-DEVELOPMENT GATE PASS`
- `TEAM C AUTHORIZED`
- `DEVELOPMENT READY`
- `PRODUCTION READY`

unless a later explicit Boss-controlled Gate artifact actually grants that authority.

---

## 13. Final Governance Rule

Close everything TEAM B can close without Accounting now. Keep only genuine external/Boss-controlled dependencies visible. Do not wait idly for Accounting, but do not cross its authority boundary.

**No Evidence = No Progress.**  
**Never Skip Gate.**  
**Independent Reviewer must not review its own work.**  
**Boss = Sole Final Approver.**
