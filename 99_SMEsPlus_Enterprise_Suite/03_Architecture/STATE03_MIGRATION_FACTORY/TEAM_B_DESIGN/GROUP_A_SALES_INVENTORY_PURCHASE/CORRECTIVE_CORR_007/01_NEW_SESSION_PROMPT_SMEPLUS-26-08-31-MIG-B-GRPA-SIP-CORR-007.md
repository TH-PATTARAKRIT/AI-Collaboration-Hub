# [SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-007]
# GROUP A — Sales + Inventory + Purchase Targeted Formal-IBPV Corrective Rework / TEAM B / L999.999

## SINGLE END-TO-END SELF-STARTING TEAM B CORRECTIVE PROMPT

Project: SMEsPlus ENTERPRISE SUITE  
STATE: STATE03 — Architecture  
Execution Team: TEAM B — Independent Canonical Domain Design  
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone  
Control Level: `/L999.999`  
Boss: Sole Final Approver  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Canonical Governance Baseline at Prompt Creation: `e13b34fb3ca7123ab64c8a243c12906d5888965d`  
Frozen TEAM B Pre-Correction Design Commit: `b98a3b9fb435845dbd15fae79db63b0b73a82420`  
Formal IBPV Finding Commit: `535724c0a2a5d0a972713f513dc567d8b27fc89b`  
Dedicated Corrective Working Branch: `claude/team-b-group-a-sip-corr-007`  
Risk: HIGH  
Readiness: READY  
STEP Binding: `TBD / BASELINE LINKAGE REQUIRED — DO NOT INVENT`  
Jira Execution Key: `TBD / DO NOT INVENT`

This is the ONLY execution instruction for this corrective session.

**ONE SESSION = ONE END-TO-END PROMPT.**

Do **not** ask Boss for a second `START`, `CONTINUE`, `NEXT`, `COMMIT`, or `PUSH` instruction.

Execution mode:

`AUTO-CONTINUE`  
`AUTO-COMMIT/PUSH EVIDENCE`  
`NO ROUTINE CONFIRMATION`  
`ASK BOSS ONLY ON TRUE STOP CONDITIONS`

---

## 1. Mission

Perform a narrow, controlled TEAM B corrective rework of the **eight TEAM-B-owned defects** identified by Formal IBPV FV-006, and continue until the material design ambiguity in those eight items is exhausted.

Do not restart GROUP A research.  
Do not redesign unrelated TEAM B work.  
Do not begin Team C / Development.  
Do not self-approve the Pre-Development Gate.

The terminal objective is:

`TEAM B CORRECTIVE REWORK COMPLETE — EIGHT FINDINGS CLOSED — READY FOR FORMAL IBPV RE-VERIFICATION`

only if every one of the eight findings is demonstrably closed and cross-file consistency is clean.

---

## 2. Governing Inputs — Verify Before Acting

Independently verify that each input exists and matches the cited commit/ref before using it.

### 2.1 TEAM B Frozen Design Package

Branch/input commit:

`b98a3b9fb435845dbd15fae79db63b0b73a82420`

Folder:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/`

Required baseline files include `01`–`21` from the TEAM B design candidate package.

### 2.2 Formal IBPV Findings

Branch:

`ibpv/group-a-sip-formal-verification-006`

Commit:

`535724c0a2a5d0a972713f513dc567d8b27fc89b`

Folder:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/EXPERT_IBPV/GROUP_A_SALES_INVENTORY_PURCHASE/FORMAL_VERIFICATION_FV_006/`

Read all 16 deliverables, with mandatory focus on:

- `04_STATE_TRANSITION_VERIFICATION_MATRIX.md`
- `05_EVENT_FLOW_VERIFICATION_MATRIX.md`
- `06_DATA_FACT_OWNERSHIP_AND_HANDOFF_VERIFICATION.md`
- `07_CONTROL_APPROVAL_SOD_VERIFICATION_MATRIX.md` or the exact D07 filename present in the verified folder
- `10_INTEGRATION_FAILURE_RETRY_RECOVERY_VERIFICATION.md` or the exact D10 filename present
- `14_IBPV_INDEPENDENT_VERIFICATION_REPORT.md`
- `15_PRE_DEVELOPMENT_GATE_RECOMMENDATION_TO_BOSS.md`

Do not guess filenames if they differ; inspect the actual directory and use the files that exist.

### 2.3 Governance / Readiness

Read and obey:

- `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/PROJECT_CONSTITUTION.md`
- `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/EXPERT_IBPV_CHARTER.md`
- `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/STATE03_PLUS_PRE_PROMPT_INDEPENDENT_CHALLENGE_RULE.md`
- `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/CORRECTIVE_CORR_007/00_PRE_PROMPT_READINESS_SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-007.md`

If a cited governance filename/path is not present exactly, search the repository for the canonical current file and record the resolved path. Do not invent a substitute.

---

## 3. Boss Authorization Boundary

Boss authorizes TEAM B to correct the eight findings below to design-complete clarity without routine confirmation.

This authorization does **not** mean:

- TEAM B is Final;
- Formal IBPV is automatically PASS after TEAM B edits;
- Pre-Development Gate is PASS;
- Team C may start;
- Boss approved any unrelated business-policy decision;
- missing legacy source/evidence may be invented.

After correction, independent Formal IBPV re-verification remains mandatory.

---

## 4. Corrective Scope — Exactly Eight Findings

Close these eight and no unrelated findings merely to increase completion count.

### CORR7-01 — Denied-Approval Wind-Down Path

Formal IBPV references:

- D14 §3.4
- `FV006-STE-004`
- `FV006-EVT-003`

Problem to resolve:

A Supply Commitment can enter Pending Approval, but the canonical design lacks a complete state/event path for a denied approval and the wind-down of downstream demand/control consequences.

TEAM B must independently define a business-semantic closure that makes the state, event, ownership, downstream effect, and audit history unambiguous.

Do not infer the missing legacy approval module's exact internal implementation.

### CORR7-02 — Retry / Idempotency Contract for Confirm & Movement Execution

Formal IBPV reference:

- D14 §3.5
- `FV006-INT-001`

Problem to resolve:

The design does not state the semantic contract for duplicate Confirm or Movement Execution requests caused by double-click, retry, redelivery, or repeated invocation.

TEAM B must define the canonical business invariant and observable outcome that prevent duplicate business effects, without prescribing a particular technical implementation such as a database lock, queue technology, or framework-specific mechanism.

### CORR7-03 — Downstream-Failure Compensation / Reconciliation

Formal IBPV reference:

- D14 §3.5
- `FV006-INT-002`

Problem to resolve:

Hard Sales↔Inventory and Inventory↔Purchase handoffs describe success paths but do not define the business truth when the initiating domain commits and the receiving domain fails.

TEAM B must define a canonical failure/compensation/reconciliation state contract at business/design level, including ownership, audit visibility, retry eligibility, and convergence criteria.

Do not prescribe production infrastructure.

### CORR7-04 — Sequential-Approval Wording Inconsistency

Formal IBPV reference:

- D14 §3.1
- `FV006-SOD-004`

Problem to resolve:

The design uses terms such as `Sequential` / `ordered levels` while correctly holding the actual enforcement/transition logic as evidence-missing. The wording can be misread as claiming more than evidence supports.

TEAM B must remove the ambiguity while preserving the verified vendor-neutral approval data shape and the explicit HOLD on unavailable legacy enforcement semantics.

### CORR7-05 — Self-Approval Mechanism Gap

Formal IBPV reference:

- D14 §3.1
- `FV006-SOD-001`

Problem to resolve:

The stated purpose says self-approval is prevented, but a role-only condition does not necessarily prevent the same identity from creating/requesting and approving the same business object.

TEAM B must define the vendor-neutral business control requirement precisely enough that creator/requester identity and approver identity can be evaluated independently, without inventing the legacy module's hidden permission algorithm.

### CORR7-06 — Event Transport Semantics

Formal IBPV reference:

- D14 §3.6
- `FV006-EVT-002`

Problem to resolve:

The canonical event catalog lacks explicit contract semantics for synchronous/asynchronous behavior, ordering expectations, duplicate delivery/replay behavior, and consumer failure.

TEAM B must add semantic transport/interaction classifications only to the depth needed for correct business flow, state ownership, retry/idempotency, and recovery reasoning.

Do **not** choose Kafka, RabbitMQ, HTTP, DB triggers, outbox, or any other implementation technology in this session.

### CORR7-07 — Traceability Unit / Handling Unit Ownership & Lifecycle

Formal IBPV reference:

- D14 §3.7
- `FV006-DFO-001`

Problem to resolve:

Lot/serial (`Traceability Unit`) and package (`Handling Unit`) are treated as first-class facts but have no complete canonical owner, create/change/retire event set, lifecycle end, or historical-reference rule.

TEAM B must close these ownership/lifecycle semantics and reconcile them across Inventory, event, handoff, and traceability artifacts.

### CORR7-08 — Shared-Master Archival / Hard-Delete Protection Rule

Formal IBPV reference:

- D14 §3.7
- `FV006-DFO-005`

Problem to resolve:

The package lacks a general canonical rule preventing destructive hard deletion of Shared Master facts after historical transactions reference them.

TEAM B must define a neutral archival/history-preservation rule, its scope, ownership, and exceptions/unknowns if any, without inventing physical schema or storage mechanics.

---

## 5. Explicit Non-Scope

Do not use CORR-007 to settle these separate items:

1. Sales/Purchase cancellation-gate policy that depends on Accounting / AR-AP semantics.
2. Acquisition/reconstruction of missing Python source for the three legacy approval modules.
3. Exact legacy approval-button / level-transition / permission algorithm.
4. Deferred business-policy defaults:
   - canonical Invoiced Quantity definition;
   - Over-Fulfillment / Over-Billing default;
   - Sales Confirmation Gate default.
5. Any unrelated Team A High/Medium/Low gap.
6. Figma/UX design.
7. Team C implementation architecture, APIs, ORM, database schema, code, deployment, infrastructure.
8. Team D, Formal IDTM, Formal IESA, Release, Production.

### SaaS / Tenant Clarification

Do not ask whether SMEsPlus should be multi-tenant. The project already treats Tenant context as a mandatory cross-module SaaS invariant.

CORR-007 is not a Tenant-baseline redesign session. If one of the eight corrections touches tenant/company boundaries, preserve the existing mandatory Tenant/Company context and do not invent new structural tenancy rules merely to close the finding.

---

## 6. Five-Unit Controls Embedded in This Prompt

### Audit VETO

- No evidence invention.
- No cross-team execution.
- Preserve pre-correction history through commit ancestry and explicit delta records.
- Every correction must map to one or more IBPV finding IDs.
- Any new material unknown must be registered, not silently solved.

### TBRAC

- Do not generalize these generic design controls into Thailand-wide business practice.
- Preserve existing evidence classifications.
- Real-user validation is not automatically required for these eight internal design defects.

### IBPV Advisory

- TEAM B discovers the corrective answers.
- IBPV findings define the defects/verification questions, not the target answer key.
- Re-verification is independent and mandatory after TEAM B correction.

### IDTM Advisory

Make corrected semantics future-testable:

- clear preconditions;
- observable events/state changes;
- explicit duplicate/retry invariants;
- explicit recovery/convergence truth;
- exact ownership/history invariants.

Do not write a Formal Test Matrix now.

### IESA Advisory

Avoid local corrections that create systemic ERP/SaaS integrity problems, especially orphaned demand, duplicated effects, unauditable failure states, tenant/company leakage, or destroyed historical references.

---

## 7. Required Execution Phases

Execute all phases automatically unless a True Stop Condition is reached.

### PHASE 0 — Preflight / Frozen Baseline Verification

1. Verify repository and branch state.
2. Verify frozen TEAM B commit `b98a3b9...`.
3. Verify Formal IBPV commit `535724c...` and all 16 deliverables.
4. Verify dedicated branch `claude/team-b-group-a-sip-corr-007` exists and is based on the frozen TEAM B design lineage.
5. Record any branch mismatch before editing.
6. Do not proceed on an incorrect lineage.

### PHASE 1 — Finding-to-Artifact Impact Map

For each CORR7-01..08:

- reproduce the IBPV finding from the actual verification artifact;
- identify all TEAM B design files materially affected;
- identify cross-file references that could become stale;
- classify correction as state/event/control/ownership/failure/archival/wording.

Create the impact map before making edits.

### PHASE 2 — Denied Approval Closure

Correct the canonical lifecycle/state/event/ownership/handoff artifacts required to close CORR7-01.

Cross-check that a denied approval cannot leave contradictory downstream demand/control state in the design narrative.

### PHASE 3 — Retry / Idempotency Closure

Correct the relevant canonical fact/event/handoff/exception artifacts required to close CORR7-02.

State semantic invariants, not implementation technology.

### PHASE 4 — Cross-Domain Failure / Compensation Closure

Correct the E2E, handoff, exception/recovery, event, and ownership artifacts required to close CORR7-03.

Explicitly cover both hard Sales↔Inventory and Inventory↔Purchase handoffs where applicable.

### PHASE 5 — Approval Semantics Closure

Close CORR7-04 and CORR7-05 together:

- eliminate any wording that implies verified sequential enforcement when that evidence is missing;
- retain the explicit legacy-enforcement HOLD;
- define the vendor-neutral self-approval business-control requirement at identity/role semantic level;
- reconcile approval events, states, ownership, and SoD language across all affected files.

### PHASE 6 — Event Contract Closure

Close CORR7-06 by classifying material event interaction semantics at canonical level and reconciling them with retry/idempotency and failure recovery.

Perform a complete sweep of the event catalog, not only the events mentioned in the original finding.

### PHASE 7 — Traceability / Handling Unit Ownership Closure

Close CORR7-07 across Inventory, business facts, events, ownership/handoff, exception/reversal, and traceability artifacts.

### PHASE 8 — Shared-Master Archival Closure

Close CORR7-08 with a consistent history-preservation rule and reconcile all Shared Master concepts that are referenced by historical transactions.

### PHASE 9 — Cross-File Consistency Sweep

Read all TEAM B files `01`–`21` after edits and verify:

- no stale statement contradicts a corrected rule;
- no affected finding remains absent from `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` where tracking is required;
- `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md` reflects the correction lineage;
- `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` no longer presents the pre-correction package as the current unchanged package; add an explicit corrective supersession/current-state note if needed;
- `21_TEAM_B_FINAL_SHA256_MANIFEST.txt` is explicitly treated as the historical pre-CORR-007 manifest and is not falsely presented as the current manifest.

Do not modify unrelated conclusions simply for stylistic consistency.

### PHASE 10 — Closure Re-performance

Re-open the actual Formal IBPV findings and, for each CORR7-01..08, prove:

- finding reproduced;
- TEAM B corrective artifact(s) identified;
- exact corrected section(s) identified;
- contradiction sweep complete;
- future verification question now answerable from the design package;
- no hidden dependency silently pushed into another domain.

If any one of the eight is not materially closed, do not claim 8/8.

### PHASE 11 — Corrective Evidence Package / Manifest / Closure

Create the required corrective evidence files listed in §8, generate a reproducible SHA-256 manifest, commit, push, and issue the terminal status.

---

## 8. Required Corrective Deliverables

Create these new files in the TEAM B GROUP A folder on the corrective branch:

### 22 — `22_TEAM_B_CORR007_FINDING_CLOSURE_REGISTER.md`

For each CORR7-01..08 include:

- IBPV finding ID/reference;
- original defect statement;
- affected TEAM B artifacts;
- corrective reasoning;
- exact corrected section references;
- state/event/owner/handoff impact as applicable;
- status: `CLOSED BY TEAM B CORRECTION` or `HOLD`;
- residual unknown, if any;
- Formal IBPV re-verification question.

### 23 — `23_TEAM_B_CORR007_CROSS_FILE_CONSISTENCY_REPORT.md`

Must show:

- all baseline files reviewed;
- stale/contradictory statements found and reconciled;
- changed files list;
- intentionally unchanged files list;
- no unrelated scope expansion;
- historical manifest/readiness supersession handling.

### 24 — `24_TEAM_B_CORR007_FORMAL_IBPV_REVERIFICATION_READINESS.md`

Must state only one evidence-based outcome:

- `READY FOR FORMAL IBPV RE-VERIFICATION — EIGHT CORR-007 FINDINGS CLOSED`, or
- `HOLD — CORR-007 MATERIAL GAP REMAINS`.

It must explicitly state that this is not Boss approval, not Pre-Development Gate PASS, and not Team C authorization.

### 25 — `25_TEAM_B_CORR007_DELTA_AND_TRACEABILITY_REGISTER.md`

Map:

`Formal IBPV Finding → TEAM B pre-correction statement → correction decision → corrected artifact/section → verification question`

### 26 — `26_SESSION_SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-007_CLOSURE.md`

Record:

- Session ID and purpose;
- frozen input commits;
- corrective branch;
- commits produced this session;
- eight-finding closure count;
- residual items outside CORR-007 scope;
- terminal status;
- no Team C / no merge / no production;
- Session Link field: if the executor cannot know the Claude web session URL, record `TBD — PMO/Boss to register; executor has no authoritative session URL` rather than inventing it.

### 27 — `27_TEAM_B_CORR007_FINAL_SHA256_MANIFEST.txt`

Generate SHA-256 for the complete current TEAM B corrective package files `01`–`26` after all edits.

File `27` must not claim to hash itself. State this limitation explicitly.

Do not overwrite or reinterpret file `21` as the current manifest; file `21` remains historical evidence for the frozen pre-CORR-007 package.

---

## 9. Expected Existing Artifacts to Reconcile

Do not assume all must change; inspect first. Modify only if the correction materially requires it.

Likely affected design artifacts include:

- `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md`
- `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md`
- `05_INVENTORY_CORE_CANONICAL_DESIGN.md`
- `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md`
- `09_CANONICAL_BUSINESS_EVENT_CATALOG.md`
- `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md`
- `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md`
- `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md`
- `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md`
- `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md`
- `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md`

This list is an impact hypothesis, not an instruction to edit every file.

Do not edit Team A artifacts or Formal IBPV artifacts.

---

## 10. Corrective Design Discipline

### 10.1 Business Semantics, Not Implementation

Allowed:

- business fact identity;
- owner;
- lifecycle;
- state;
- event;
- invariant;
- handoff;
- failure/recovery semantics;
- control/SoD requirement;
- archival/history rule;
- observable outcome.

Prohibited in this session:

- physical schema;
- ORM;
- table/column design;
- Node.js implementation;
- API endpoint contract at implementation level;
- queue/database/framework selection;
- production deployment design.

### 10.2 No Legacy Algorithm Invention

For the missing approval-source area, distinguish:

- target vendor-neutral control requirement TEAM B is authorized to design;
- legacy internal workflow behavior that remains evidence-missing.

Do not convert target design into a claim about the missing legacy algorithm.

### 10.3 No Answer-Key Contamination

Formal IBPV findings state defects and verification expectations. They do not dictate the exact target design.

TEAM B must reason independently and document why each correction is coherent with the existing canonical model.

---

## 11. Closure Criteria for Each Finding

A finding is `CLOSED BY TEAM B CORRECTION` only if all applicable criteria are met:

1. the original IBPV concern is reproducible;
2. the corrected business semantics are explicit;
3. owner is explicit;
4. lifecycle/state impact is explicit;
5. event impact is explicit;
6. handoff/downstream impact is explicit;
7. exception/failure/retry behavior is explicit where applicable;
8. audit/history impact is explicit where applicable;
9. cross-file references are consistent;
10. the correction does not rely on an invented external-domain fact;
11. the correction is future-verifiable;
12. residual unknowns are explicitly registered.

No `CLOSED` by prose assertion alone.

---

## 12. Git / Branch Controls

Work only on:

`claude/team-b-group-a-sip-corr-007`

The branch was created from the frozen TEAM B design lineage at:

`b98a3b9fb435845dbd15fae79db63b0b73a82420`

Before editing, verify this ancestry.

You are authorized to:

- edit TEAM B GROUP A design artifacts required by CORR-007;
- create files `22`–`27`;
- commit in logical batches;
- push to `claude/team-b-group-a-sip-corr-007`;
- continue automatically after each commit/push.

You are **not** authorized to:

- merge to `SMEsPlus`;
- modify Team A evidence;
- modify Formal IBPV evidence;
- open Team C implementation;
- release/deploy.

If the local checkout contains unrelated concurrent changes, isolate this work in a clean clone/worktree/branch. Never overwrite unrelated work.

---

## 13. Commit / Evidence Requirements

Use clear commits tied to the eight findings. The final commit message must include:

- Session `SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-007`;
- number of CORR7 findings closed;
- unresolved CORR7 findings if any;
- statement that Formal IBPV re-verification is still required;
- statement that Team C is not authorized.

At the end report:

- Repo;
- Branch;
- final commit SHA;
- files changed;
- files created;
- eight-finding closure table;
- final manifest status;
- terminal status.

Do not report work complete unless the push is verified.

---

## 14. True Stop Conditions

Do not ask Boss routine questions.

Stop/escalate only if one of these occurs:

1. the corrective branch is not descended from the frozen TEAM B design and cannot be safely repaired without destructive action;
2. a CORR7 item unexpectedly requires a material business-policy decision not authorized by this prompt;
3. a CORR7 item cannot be closed without inventing Accounting/Tax/Thailand/legacy behavior outside TEAM B authority;
4. a material contradiction cannot safely remain registered as Unknown/Conflict;
5. required evidence/commit is inaccessible after reasonable repository verification;
6. destructive/irreversible/live-system action would be required;
7. scope expansion or Change Request is materially required.

When one item hits a localized HOLD, continue the other seven if safe. Do not stop the entire session merely because one finding remains open.

---

## 15. Terminal Status Rules

If all eight close and all closure evidence is pushed:

`TEAM B CORRECTIVE REWORK COMPLETE — EIGHT FINDINGS CLOSED — READY FOR FORMAL IBPV RE-VERIFICATION`

If one or more material CORR7 finding remains:

`TEAM B CORRECTIVE REWORK PARTIAL — MATERIAL GAP REMAINS / HOLD`

If a true frozen condition occurs:

`FAIL / FROZEN — TRUE STOP CONDITION`

Never output:

- `FINAL APPROVED`
- `BOSS APPROVED`
- `PRE-DEVELOPMENT GATE PASS`
- `TEAM C AUTHORIZED`
- `DEVELOPMENT READY`
- `PRODUCTION READY`

---

## 16. Autonomous Execution Command

Immediately begin PHASE 0 after receiving this prompt.

Do not wait for another instruction.

Proceed PHASE 0 → PHASE 11 autonomously, commit/push evidence to the dedicated corrective branch, re-perform closure against all eight Formal IBPV findings, and stop only at the terminal status or a True Stop Condition.

**Ask until materially clear — not until everyone agrees.**  
**Independent experts challenge the questions; the authorized Team discovers the answers.**
