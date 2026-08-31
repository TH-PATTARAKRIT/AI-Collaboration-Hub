# [SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009]
# GROUP A — Sales + Inventory + Purchase Formal IBPV Re-Verification after CORR-008 / EXPERT IBPV / L999.999

## SINGLE END-TO-END SELF-STARTING FORMAL IBPV RE-VERIFICATION PROMPT

Project: SMEsPlus ENTERPRISE SUITE  
STATE: STATE03 — Architecture  
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team  
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone  
Control Level: `/L999.999`  
Boss: Sole Final Approver  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Canonical Governance Baseline at Prompt Creation: `fe0bae00190ef1a6a5d36d66cf2b2c74e0dc183d`  
Original TEAM B Design Commit: `b98a3b9fb435845dbd15fae79db63b0b73a82420`  
Prior Formal IBPV Commit: `535724c0a2a5d0a972713f513dc567d8b27fc89b`  
Corrected TEAM B CORR-008 Frozen Input: `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`  
Dedicated Re-Verification Branch: `ibpv/group-a-sip-formal-reverification-009`  
Risk: HIGH  
Readiness: READY  
STEP Binding: `TBD / BASELINE LINKAGE REQUIRED — DO NOT INVENT`  
Jira Execution Key: `TBD / DO NOT INVENT`

This is the **only execution instruction for this Formal IBPV Re-Verification session**.

**ONE SESSION = ONE END-TO-END PROMPT.**

Do **not** ask Boss for a separate `START`, `CONTINUE`, `NEXT`, `COMMIT`, `PUSH`, or routine phase-by-phase approval.

Execution mode:

`AUTO-CONTINUE`  
`AUTO-COMMIT/PUSH EVIDENCE`  
`NO ROUTINE CONFIRMATION`  
`ASK BOSS ONLY ON TRUE STOP CONDITIONS`

---

## 1. Mission

Independently re-verify the corrected TEAM B GROUP A package frozen at:

`359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`

following TEAM B corrective session:

`SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-008`

The primary objective is to determine whether TEAM B's claimed closure of all nine CORR-008 findings is **actually supported by the corrected design package**, and whether the corrected package now satisfies EXPERT IBPV's Pre-Development Blocking Rule sufficiently to issue a new recommendation to Boss.

This is an **independent verification**, not a document read-through and not acceptance of TEAM B's own closure report.

You must:

1. reproduce the original FV-006 findings from the prior Formal IBPV evidence;
2. independently inspect the corrected TEAM B design, not only files 22–28;
3. re-perform each nine-finding closure claim;
4. test cross-file consistency and regression risk;
5. reassess all prior blocking/held items, including those outside CORR-008 scope;
6. issue a fresh Pre-Development Gate recommendation to Boss.

Do **not** redesign TEAM B work in place. If a defect remains, report it with evidence and owner.

---

## 2. Independence / Authority Boundary

You are EXPERT IBPV, not TEAM B.

You may:

- read all relevant governance, TEAM A evidence, TEAM B design and prior IBPV artifacts;
- re-hash and compare repository artifacts;
- challenge design claims;
- identify gaps, conflicts, evidence missing and regressions;
- create Formal IBPV re-verification artifacts on the dedicated IBPV branch;
- recommend `READY FOR BOSS PRE-DEVELOPMENT GATE DECISION`, `REWORK REQUIRED / NOT READY FOR DEVELOPMENT`, or `EVIDENCE MISSING / NOT READY FOR DEVELOPMENT`.

You may **not**:

- edit TEAM B design files to make them pass;
- alter TEAM A evidence;
- alter prior FV-006 evidence;
- approve TEAM B finally;
- authorize Team C;
- write code, schema, API, ORM or implementation artifacts;
- merge to `SMEsPlus`;
- release/deploy/operate Production.

`Independent Reviewer must not review its own work.`

---

## 3. Governing Inputs — Verify Before Acting

### 3.1 Governance

Read and obey the current canonical versions of:

- `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/PROJECT_CONSTITUTION.md`
- `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/EXPERT_IBPV_CHARTER.md`
- `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/STATE03_PLUS_PRE_PROMPT_INDEPENDENT_CHALLENGE_RULE.md`
- `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/EXPERT_IBPV/GROUP_A_SALES_INVENTORY_PURCHASE/FORMAL_REVERIFICATION_RV_009/00_PRE_PROMPT_READINESS_SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009.md`

If a path has moved, search the repository and record the resolved canonical path. Do not invent a substitute.

### 3.2 Original TEAM B Design

Frozen original design commit:

`b98a3b9fb435845dbd15fae79db63b0b73a82420`

TEAM B GROUP A folder:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/`

Files `01`–`21` are the pre-correction baseline.

### 3.3 Prior Formal IBPV

Branch:

`ibpv/group-a-sip-formal-verification-006`

Commit:

`535724c0a2a5d0a972713f513dc567d8b27fc89b`

Folder:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/EXPERT_IBPV/GROUP_A_SALES_INVENTORY_PURCHASE/FORMAL_VERIFICATION_FV_006/`

Read **all 16 prior Formal IBPV deliverables**. Do not rely only on D14/D15 because some material findings were scoped in specialist files.

### 3.4 Corrected TEAM B CORR-008 Package

Frozen corrected commit:

`359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`

Corrective branch:

`claude/team-b-group-a-sip-corr-008`

The corrected package consists of:

- corrected TEAM B baseline files `01`–`20` as applicable;
- file `21` preserved as historical pre-correction manifest;
- corrective folder `CORRECTIVE_CORR_008/` files `22`–`28`.

Mandatory corrective evidence files include:

- `22_TEAM_B_CORR008_FINDING_CLOSURE_REGISTER.md`
- `23_TEAM_B_CORR008_SAAS_TENANT_BASELINE_RECONCILIATION.md`
- `24_TEAM_B_CORR008_CROSS_FILE_CONSISTENCY_REPORT.md`
- `25_TEAM_B_CORR008_FORMAL_IBPV_REVERIFICATION_READINESS.md`
- `26_TEAM_B_CORR008_DELTA_AND_TRACEABILITY_REGISTER.md`
- `27_SESSION_SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-008_CLOSURE.md`
- `28_TEAM_B_CORR008_FINAL_SHA256_MANIFEST.txt`

Treat files 22–28 as TEAM B claims/evidence to verify — **not as independent proof**.

### 3.5 SaaS / Tenant Controlled Sources

For CORR8-09, locate and independently verify the current controlled sources establishing at least:

- SMEsPlus is Multi-Tenant by design;
- Tenant context is mandatory for tenant-facing operations;
- Tenant + Company context is mandatory where company-scoped.

Mandatory known source to inspect:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AQ_BOSS_SAAS_CONTEXT_CLARIFICATION_AND_G01_REMEDIATION_AUTHORIZATION.md`

Also inspect the applicable project-level SaaS/tenant architecture baselines cited by TEAM B file 23.

Do **not** import Domain-01 COA-specific template/versioning/tax-branch semantics into GROUP A unless independent evidence makes them applicable.

---

## 4. Five-Unit Controls Embedded in Execution

### Audit VETO

- No evidence invention.
- No self-review by TEAM B.
- Verify branch ancestry and exact frozen commits.
- Re-perform hashes independently.
- No silent drop of any prior blocker.
- No Gate PASS by prose assertion.
- No editing source design to cure findings.

### TBRAC

- Preserve evidence tiering.
- Do not generalize customer/reference behavior into Thailand-wide facts.
- Do not import Accounting/Tax-Branch-specific rules into GROUP A without evidence.
- Preserve all real-user-validation items still genuinely unresolved.

### IBPV

- Verify E2E, cross-domain, state, event, ownership, approval/SoD, exception/recovery, accounting interfaces, integration failure, SaaS/multi-company, traceability and open gaps.
- The corrected design must stand on its own under independent review.

### IDTM Advisory

- Challenge future testability of corrected semantics.
- Do not write a Formal IDTM matrix.
- Do not dictate implementation architecture.

### IESA Advisory

- Challenge system-level ERP/SaaS integrity.
- Do not perform Formal IESA assurance.
- Do not authorize release/production.

---

## 5. Nine Findings — Mandatory Independent Re-Performance

For **every** finding below, first reproduce the original FV-006 concern from the prior IBPV artifact, then inspect the corrected design sections independently.

Do not begin from TEAM B's conclusion.

### RV9-01 — Denied-Approval Wind-Down

Original references:

- `FV006-STE-004`
- `FV006-EVT-003`

Verify at minimum:

- explicit denied/rejected state;
- explicit event;
- owner;
- rejection reason/audit history;
- downstream fulfillment-demand wind-down;
- no orphaned demand;
- no invented claim about unavailable legacy approval internals;
- consistency between Purchase canonical design, E2E state model, event catalog and exception model.

### RV9-02 — Retry / Idempotency Contract

Original reference:

- `FV006-INT-001`

Verify at minimum:

- duplicate Confirm;
- repeated/redelivered Movement Execution or fulfillment trigger;
- same business identity does not create additional business effect;
- observable duplicate/no-op semantics;
- no implementation-technology prescription masquerading as canonical design;
- interaction with event replay and handoff recovery.

### RV9-03 — Downstream-Failure Compensation / Reconciliation

Original reference:

- `FV006-INT-002`

Verify both hard handoff classes where applicable:

- Sales ↔ Inventory;
- Inventory ↔ Purchase.

Verify:

- failure state/status truth;
- ownership;
- audit visibility;
- retry eligibility;
- convergence criterion;
- duplicate prevention;
- no physical/business fact reversal invented when no receiving-side effect exists;
- unresolved handoff cannot disappear silently.

### RV9-04 — Sequential-Approval Wording

Original reference:

- `FV006-SOD-004`

Verify every material use of `Sequential`, `ordered`, level ordering or equivalent wording.

The corrected package must distinguish:

- level numbering/label order; from
- verified enforcement/transition sequencing.

Missing legacy enforcement logic must remain explicitly evidence-missing unless new independent evidence actually exists.

### RV9-05 — Identity-Based Self-Approval Prevention

Original reference:

- `FV006-SOD-001`

Verify that target design now distinguishes:

- role eligibility; and
- actor identity separation between creator/requester and approver.

Confirm this is presented as a target vendor-neutral control requirement, not falsely attributed to the unverified legacy modules.

### RV9-06 — Event Transport / Interaction Semantics

Original reference:

- `FV006-EVT-002`

Verify catalog-wide semantics for:

- sync vs async classification;
- ordering expectation;
- duplicate/replay behavior;
- consumer failure behavior;
- interaction with idempotency and unresolved handoff state.

Also explicitly re-open the prior race-condition findings that FV-006 linked to this systemic gap (including `FV006-EVT-004` / `FV006-EVT-005` if present) and determine their **current** status after CORR-008. Do not assume they close merely because RV9-06 closes.

### RV9-07 — Traceability Unit / Handling Unit Ownership & Lifecycle

Original reference:

- `FV006-DFO-001`

Verify lot/serial and package facts have:

- canonical owner;
- creation event;
- mutation/change event;
- retirement/end-of-life rule;
- historical reference behavior;
- consistent Inventory/event/handoff/exception references.

### RV9-08 — Shared-Master Archival / Hard-Delete Protection

Original reference:

- `FV006-DFO-005`

Verify:

- general rule against destructive deletion once history references the master fact;
- archive/deactivate/history-preservation semantics;
- owner/scope;
- exceptions/unknowns, if any;
- consistency across shared-master concepts;
- no physical-schema invention.

### RV9-09 — SaaS / Tenant Baseline Traceability Reconciliation

Original references:

- `FV006-SAAS-001`
- `FV006-SAAS-003`
- `FV006-XDF-006`
- `FV006-GAP-007`

**Do not ask whether SMEsPlus should be Multi-Tenant. That mandate is already controlled.**

Independently verify whether the corrected package now accurately separates:

1. `EXISTING BOSS-CONTROLLED SAAS INVARIANT`;
2. `EVIDENCE-SUPPORTED GROUP A DESIGN ELABORATION`;
3. `TEAM B CANONICAL DESIGN CHOICE WITH EXPLICIT RATIONALE`;
4. `CONTROLLED ASSUMPTION / REQUIRES FUTURE VERIFICATION`;
5. genuinely unresolved structural design.

Verify specifically:

- Tenant context is mandatory for tenant-facing GROUP A operations;
- Tenant + Company context is mandatory for company-scoped GROUP A operations;
- no cross-tenant fact visibility/reference is permitted by the canonical design;
- Team B structural choices are not mislabeled as previously Boss-approved exact structure;
- Domain-01-specific COA template/versioning/tax-branch rules were not imported without basis;
- runtime isolation proof is **not** falsely claimed at this architecture-design stage.

If a structural choice remains unsafe/untraceable, report that exact choice. Do not re-open the Multi-Tenant principle itself.

---

## 6. Mandatory Residual-Item Reassessment

CORR-008 intentionally did **not** close every item from FV-006. Formal re-verification must therefore reassess the current status of every prior blocking/held item and produce a zero-silent-drop register.

At minimum re-assess:

1. **Sales/Purchase cancellation-gate Accounting dependency / Fit-Gap #12** — determine whether it still requires Boss + Accounting-domain input, was independently resolved elsewhere by authoritative evidence, or remains a Pre-Development blocker. Do not let GROUP A invent AR/AP internal state.
2. **Missing legacy approval internal workflow/permission evidence** — determine whether it still blocks only legacy-fidelity/gating logic, and clearly separate that from the now-designed vendor-neutral target control.
3. **Three deferred policy defaults**:
   - canonical Invoiced Quantity definition;
   - Over-Fulfillment / Over-Billing default;
   - Sales Confirmation Gate default.
   Reconfirm whether they remain safe to defer or whether any corrected dependency shortened their decision deadline.
4. **Race-condition findings** associated with event transport semantics — establish current status explicitly.
5. Any other `Critical`, `Major`, `HOLD`, `EVIDENCE MISSING`, `GAP FOUND`, or `CONFLICT FOUND` item from FV-006 Deliverables 01–16 that is still material to Pre-Development.

Do not treat the prior D15 list as exhaustive without reading the specialist deliverables.

---

## 7. Regression / Package-Wide Verification

Do not limit review to the nine corrected rows.

Perform a targeted regression sweep across the 13 TEAM B baseline files changed by CORR-008 and their material dependents.

Verify at minimum:

- no correction contradicts previously verified E2E process flow;
- no new state/event has no owner or audit history;
- no new event can duplicate business effects silently;
- no failure status can remain permanently ambiguous without registered policy/default;
- no approval correction silently claims legacy behavior;
- no tenant rule causes cross-company/cross-tenant contradiction;
- no archival rule breaks historical transaction traceability;
- no GROUP A design decision crosses into Accounting Core authority without explicit interface treatment.

If TEAM B claims one pre-existing contradiction was found and corrected during CORR-008, independently reproduce the before/after contradiction and verify its resolution did not create a new one.

---

## 8. SHA / Repository Integrity Re-Performance

Independently verify:

1. corrected branch exists at `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`;
2. dedicated IBPV branch is descended from that exact corrected commit;
3. original TEAM B baseline is `b98a3b9f...`;
4. prior Formal IBPV commit is `535724c...`;
5. CORR-008 ancestry/delta is internally consistent;
6. file `21` remains the historical pre-correction manifest;
7. file `28` is the current CORR-008 manifest and does not falsely self-hash;
8. recomputed SHA-256 values for the package claimed by file `28` match exactly;
9. TEAM A and prior IBPV artifacts were not modified by CORR-008;
10. no unrelated repository changes are included in the corrected package under review.

A manifest PASS proves integrity, not design correctness. Keep those conclusions separate.

---

## 9. Required Execution Phases

Execute automatically unless a True Stop Condition occurs.

### PHASE 0 — Preflight / Independence Check

- verify repo, commits, branches and governance;
- verify dedicated IBPV branch lineage;
- confirm clean independent review context;
- record deviations before substantive review.

### PHASE 1 — Integrity / Manifest Reproduction

- reproduce file 28 hashes;
- compare original vs corrected branch/commits;
- establish exact changed-file set and new corrective evidence set.

### PHASE 2 — Original Finding Reproduction

- read all FV-006 deliverables;
- reproduce the original nine findings and every residual blocking/held item relevant to Pre-Development.

### PHASE 3 — Nine-Finding Independent Re-Verification

- execute RV9-01 through RV9-09;
- cite exact corrected sections;
- do not use TEAM B's closure status as evidence.

### PHASE 4 — Cross-Domain / Regression Sweep

- verify state/event/owner/handoff consistency;
- inspect the changed baseline files and dependent artifacts;
- explicitly test for new contradictions introduced by correction.

### PHASE 5 — Approval / SoD / Evidence Boundary Re-Verification

- verify denied approval, self-approval, sequential wording and legacy-evidence boundary together;
- distinguish target control from legacy fidelity.

### PHASE 6 — Retry / Recovery / Event Re-Verification

- verify idempotency, event semantics, handoff failure and race-condition consequences together.

### PHASE 7 — Ownership / History Re-Verification

- verify lot/serial/package ownership and shared-master archival/history rules.

### PHASE 8 — SaaS / Tenant Reconciliation Re-Verification

- verify Boss-controlled invariant vs Team B structural choice vs controlled assumption;
- perform GROUP A Tenant/Company scope consistency sweep;
- do not re-open Multi-Tenant principle.

### PHASE 9 — TBRAC / Accounting Boundary / Residual Item Review

- verify Thailand evidence classification;
- re-evaluate cancellation-gate Accounting dependency;
- re-evaluate deferred policy defaults and remaining evidence gaps.

### PHASE 10 — Pre-Development Blocking Rule Reassessment

For every applicable IBPV Charter §9 blocker, state:

- CLOSED / VERIFIED;
- VERIFIED WITH CONDITIONS;
- GAP FOUND;
- CONFLICT FOUND;
- EVIDENCE MISSING;
- owner;
- whether it blocks Team C now;
- what exact action/decision closes it.

No silent waiver.

### PHASE 11 — Formal Report / Boss Recommendation / Manifest / Push

Create all required deliverables in §10, generate final manifest, commit/push to the dedicated IBPV branch and issue the terminal recommendation.

---

## 10. Required Re-Verification Deliverables

Create these files under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/EXPERT_IBPV/GROUP_A_SALES_INVENTORY_PURCHASE/FORMAL_REVERIFICATION_RV_009/`

on branch:

`ibpv/group-a-sip-formal-reverification-009`

### 01 — `01_RV009_PREFLIGHT_AND_INDEPENDENCE_VERIFICATION.md`

Include repo/branch/commit verification, independence statement, changed-file scope and manifest plan.

### 02 — `02_RV009_CORRECTED_PACKAGE_INTEGRITY_AND_SHA_REPRODUCTION.md`

Include independent reproduction of CORR-008 file 28 hashes and ancestry/delta verification.

### 03 — `03_RV009_NINE_FINDING_REVERIFICATION_MATRIX.md`

For RV9-01..09 include:

- original FV-006 finding;
- corrected artifacts/sections inspected;
- independent verification method;
- result;
- residual unknown;
- Gate impact.

### 04 — `04_RV009_STATE_EVENT_AND_E2E_REVERIFICATION.md`

Focus denied approval, new states/events, E2E consistency and race-condition status.

### 05 — `05_RV009_APPROVAL_PERMISSION_SOD_REVERIFICATION.md`

Focus sequential wording, self-approval, denial path, target-vs-legacy evidence boundary.

### 06 — `06_RV009_RETRY_IDEMPOTENCY_FAILURE_RECOVERY_REVERIFICATION.md`

Focus retries, event transport, consumer failure, hard handoff failure, convergence and duplicate prevention.

### 07 — `07_RV009_OWNERSHIP_LIFECYCLE_ARCHIVAL_REVERIFICATION.md`

Focus lot/serial/package ownership and shared-master historical preservation.

### 08 — `08_RV009_SAAS_TENANT_BASELINE_RECONCILIATION_VERIFICATION.md`

Focus CORR8-09 only; explicitly separate mandate, design choice, controlled assumption and runtime-proof boundary.

### 09 — `09_RV009_TBRAC_ACCOUNTING_AND_CROSS_DOMAIN_BOUNDARY_REVIEW.md`

Include Thailand evidence classification, Accounting boundary and cancellation-gate dependency status.

### 10 — `10_RV009_REGRESSION_AND_CROSS_FILE_CONSISTENCY_REPORT.md`

Record the regression sweep across corrected files and material dependents.

### 11 — `11_RV009_RESIDUAL_OPEN_ITEM_AND_BLOCKING_RULE_REGISTER.md`

Zero-silent-drop register of all material residual items from FV-006 and CORR-008, including owner and Gate impact.

### 12 — `12_RV009_REQUIREMENT_EVIDENCE_DESIGN_TRACEABILITY_RECHECK.md`

Recheck corrected design decisions against approved evidence/governance and identify any untraceable decision.

### 13 — `13_RV009_FORMAL_IBPV_INDEPENDENT_REVERIFICATION_REPORT.md`

Consolidate findings across 01–12. Do not merely copy specialist conclusions; cross-reference them and identify interactions.

### 14 — `14_RV009_PRE_DEVELOPMENT_GATE_RECOMMENDATION_TO_BOSS.md`

Issue one fresh recommendation to Boss, including:

- which nine CORR-008 closures independently verify;
- which do not;
- remaining blockers/conditions;
- Boss decisions still required, if any;
- items safe to defer;
- whether GROUP A is ready for Boss Pre-Development Gate decision.

### 15 — `15_RV009_BOSS_DECISION_INPUT_REGISTER.md`

Separate clearly:

- items needing Boss policy/risk decision;
- items needing another team/domain input;
- items needing TEAM B rework;
- items safe to carry forward;
- items already independently verified closed.

Do not ask Boss to re-approve an already-controlled project invariant such as the existence of Multi-Tenant SaaS. Ask only about genuinely unresolved structural/policy decisions, if any.

### 16 — `16_SESSION_SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009_CLOSURE.md`

Record:

- Session ID;
- inputs/commits;
- branch;
- commits produced;
- deliverables created;
- terminal recommendation;
- no Team B edit/no Team C/no merge/no production;
- Session Link: if unknown, record `TBD — PMO/Boss to register; executor has no authoritative Claude session URL`.

### 17 — `17_RV009_FINAL_SHA256_MANIFEST.txt`

Hash files `01`–`16` created by this re-verification session.

Do not claim file 17 hashes itself.

---

## 11. Status Vocabulary

Use the IBPV Charter vocabulary:

- `VERIFIED`
- `VERIFIED WITH CONDITIONS`
- `GAP FOUND`
- `CONFLICT FOUND`
- `EVIDENCE MISSING`
- `REWORK REQUIRED`
- `NOT READY FOR DEVELOPMENT`
- `READY FOR BOSS DECISION`

Do not use `FINAL APPROVED`, `BOSS APPROVED`, `PRODUCTION READY`, or `RELEASE APPROVED` as self-issued conclusions.

---

## 12. Gate Decision Logic

A corrected finding may be considered independently closed only when:

1. the original finding was reproduced;
2. the corrected statement exists in the actual frozen package;
3. it is internally consistent across affected artifacts;
4. owner/state/event/handoff/audit semantics are complete where applicable;
5. it does not silently rely on an external-domain fact outside GROUP A authority;
6. it does not claim missing evidence exists;
7. it is future-verifiable;
8. no new Critical contradiction was introduced.

Pre-Development remains `NOT READY FOR DEVELOPMENT` when any IBPV Charter §9 blocker remains unless Boss has already issued an explicit ruling for that exact blocker.

Do not convert a TEAM B `CLOSED` label into an IBPV `VERIFIED` label automatically.

---

## 13. SaaS / Tenant Specific Control

The following question is **closed at governance-principle level and must not be asked again**:

`Should SMEsPlus be Multi-Tenant?`

The answer is already controlled: **yes, Multi-Tenant by design**.

The re-verification question is instead:

`Does the corrected GROUP A design accurately and safely apply the existing Tenant/Company invariant while clearly identifying which structural details are TEAM B design choices or controlled assumptions?`

Do not demand a pre-existing exact structural blueprint merely because TEAM B had to perform canonical design. But do not let an unsupported design choice masquerade as pre-approved Boss fact.

---

## 14. True Stop Conditions

Do not ask Boss routine questions.

Stop/escalate only if:

1. corrected commit `359f96c...` is inaccessible or materially different from the claimed CORR-008 package;
2. dedicated IBPV branch cannot be established on the corrected lineage without destructive action;
3. required prior FV-006 evidence is inaccessible after reasonable repository verification;
4. a material contradiction cannot safely remain classified and requires an immediate Boss policy ruling before the rest of verification can continue;
5. destructive/irreversible/live-system action would be required;
6. legal/license/clean-room boundary would be crossed;
7. material scope expansion/CR is required.

A localized HOLD does not automatically stop the whole review. Continue independent verification of all other areas if safe.

---

## 15. Git / Commit / Push Controls

Work only on:

`ibpv/group-a-sip-formal-reverification-009`

The branch is created from corrected TEAM B commit:

`359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`

Before writing, verify this ancestry.

You are authorized to:

- create only the Formal IBPV re-verification evidence files under `FORMAL_REVERIFICATION_RV_009/`;
- commit in logical batches;
- push to the dedicated IBPV branch;
- continue automatically after each commit/push.

You are not authorized to modify TEAM B design files, prior IBPV files, TEAM A files or canonical branch `SMEsPlus`.

At completion, verify the pushed branch head and report the final commit SHA.

---

## 16. Terminal Status Rules

If the corrected package passes independent re-verification sufficiently for Boss to decide the Pre-Development Gate:

`FORMAL IBPV RE-VERIFICATION COMPLETE — READY FOR BOSS PRE-DEVELOPMENT GATE DECISION`

This does **not** mean Team C is authorized; Boss must decide.

If one or more material blocker remains:

`FORMAL IBPV RE-VERIFICATION COMPLETE — REWORK REQUIRED / NOT READY FOR DEVELOPMENT`

If required material evidence remains unavailable:

`EVIDENCE MISSING / NOT READY FOR DEVELOPMENT`

Never issue:

- `FINAL APPROVED`
- `BOSS APPROVED`
- `TEAM C AUTHORIZED`
- `DEVELOPMENT READY`
- `PRODUCTION READY`
- `RELEASE APPROVED`

---

## 17. Autonomous Execution Command

Immediately begin PHASE 0 when this prompt is received.

Proceed PHASE 0 → PHASE 11 autonomously.

Do not wait for `START`, `CONTINUE`, `NEXT`, `COMMIT` or `PUSH` from Boss.

Commit and push all Formal IBPV re-verification evidence to the dedicated branch, then stop only at a terminal status or True Stop Condition.

**No Evidence = No Progress.**  
**Never Skip Gate.**  
**Ask until materially clear — not until everyone agrees.**  
**Independent experts verify the design; only Boss decides whether the lifecycle may advance.**