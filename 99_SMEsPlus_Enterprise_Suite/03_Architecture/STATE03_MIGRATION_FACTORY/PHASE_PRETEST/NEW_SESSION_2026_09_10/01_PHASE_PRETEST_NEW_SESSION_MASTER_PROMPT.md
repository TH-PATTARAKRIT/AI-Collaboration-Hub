# [SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]
# SMEsPlus PHASE PRE-TEST MATRIX — NEW SESSION MASTER PROMPT
# /L99999.99999

Repository:
`TH-PATTARAKRIT/AI-Collaboration-Hub`

Execution branch:
`architecture/account-phase-pretest-new-session-2026-09-10-001`

Session scope:
**PHASE PRE-TEST ONLY**

Boss:
**SOLE FINAL APPROVER**

Execution model:
**Claude Opus 5 — Effort High**

Read first, completely:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/PHASE_PRETEST/NEW_SESSION_2026_09_10/00_PHASE_PRETEST_CONTEXT_AND_LINEAGE.md`

Then execute this prompt end-to-end.

---

## 0. GOVERNING INTENT

Phase Pre-Test exists to verify, before Functional Design, that Phase SA produced a complete and testable cross-module business architecture.

The controlling pattern is:

`INPUT -> PROCESS -> OUTPUT -> DOWNSTREAM ROUTING -> NEXT MODULE INPUT`

The purpose is not to create a test document for appearance. The purpose is to discover where SMEsPlus would fail before implementation begins.

Canonical doctrine:

`Truth over Pass.`
`Evidence over Assumption.`
`Falsify before Accept.`
`Correct before Escalate.`
`No deadline can convert uncertainty into truth.`

Do not search for evidence to pass.
Search for evidence strong enough to survive falsification.

---

## 1. ABSOLUTE PHASE BOUNDARY

AUTHORIZED:

- construct the canonical Phase Pre-Test Matrix;
- trace every row to Phase S / Phase SA evidence or explicit authority;
- verify requirement completeness;
- verify cross-module input/output contracts;
- verify routing logic and downstream consumers;
- challenge contradictions, missing states and missing data;
- perform static, semantic and bounded reference/experiment checks where lawful;
- define future executable test procedures and expected results;
- collect evidence that does not require SMEsPlus implementation;
- route B-7 to a structurally independent eligible verifier;
- consume independent findings and correct/re-freeze the package;
- perform targeted re-entry only where a newly proven material knowledge gap exists.

NOT AUTHORIZED:

- Functional Design;
- physical database/schema lock;
- application implementation;
- coding;
- production migration;
- merge/release/deploy;
- inventing behavior absent from evidence;
- treating reference-system behavior as SMEsPlus authority;
- self-discharging vetoes;
- fabricating runtime proof;
- self-declaring Phase SA or State PASS;
- bypassing Boss Final Approval.

---

## 2. MANDATORY CARRY-FORWARD — DO NOT RESET

Consume and preserve the Phase SA handoff exactly:

- Phase SA state = `READY FOR PRE-TEST — INTERNAL VERIFICATION TRANSITION ONLY`;
- `SC-AUTH-02 = Reading C`;
- `8C-CLARIFICATION-01 = APPROVED`;
- Phase SA -> Pre-Test is not an 8-Criteria Exit Gate;
- `EC-04 = 0/3` runtime closures;
- `EC-07 = 0/2` clean structurally independent passes;
- `6` vetoes in force, `0` discharged;
- B-7 package ready, eligible independent executor still required;
- AAS+ concurrence / limb-2 re-wording outstanding;
- Manufacturing veto not lifted;
- `6` Boss elections ready and held;
- `POH-D-02` withheld for missing Thai statutory evidence;
- `E2E-04 = NOT TRAVERSABLE`;
- `0/22` scenarios runtime-verified;
- 22 cross-module scenarios = `10/12/0` in Phase SA classification;
- 18 E2E scenarios = `9/9/0` in Phase SA classification;
- Phase SA SMEs Core-owned specification gaps = `0` at handoff.

Entering Pre-Test changes none of these facts automatically.

---

## 3. SINGLE-SESSION EXECUTION CONTROL

This is the ONE active Phase Pre-Test canonical execution session.

Rules:

1. No competing canonical Phase Pre-Test writer.
2. Historical Phase S/SA branches = READ-ONLY LINEAGE.
3. Specialist/subagent work may be parallel only if read-only or isolated and cannot publish canonical conclusions directly.
4. The controlling executor reconciles all specialist findings before writing canonical output.
5. B-7 must remain structurally independent and must not mutate this branch while reviewing a frozen baseline.
6. If branch drift or concurrent canonical writing is detected, stop publication, record the collision, reconcile, and re-freeze.

---

## 4. PRE-TEST MATRIX ROW CONTRACT

Every material test row must contain at minimum:

1. Pre-Test ID.
2. Domain / module owner.
3. Business scenario.
4. Business nature / route trigger.
5. Input source.
6. Mandatory input fields / facts.
7. Preconditions.
8. Process semantic obligation.
9. Control / approval obligation.
10. Expected output.
11. Downstream consumer module(s).
12. Next-module required input.
13. Inventory impact.
14. Accounting impact.
15. Manufacturing impact.
16. Purchase / replenishment / dropship impact.
17. Tax impact.
18. Payment/bank impact when applicable.
19. Tenant boundary.
20. Company boundary.
21. Identity / idempotency requirement.
22. Reversal / correction / cancellation requirement.
23. Exception / failure path.
24. Negative / boundary case.
25. Expected result.
26. Evidence class.
27. Required evidence artifact.
28. Current evidence pointer.
29. Status.
30. Owner of unresolved dependency.
31. Gate effect.
32. Veto linkage if any.
33. Boss ruling linkage if any.
34. Independent challenge status.

No material row may omit downstream routing.

---

## 5. EVIDENCE CLASSIFICATION

Each row gets exactly one primary class:

- `PTE-1 STATIC/SEMANTIC PROOF`
- `PTE-2 REFERENCE/EXPERIMENT PROOF`
- `PTE-3 EXECUTION-DESIGN READY`
- `PTE-4 EXTERNAL AUTHORITY DEPENDENCY`
- `PTE-5 BOSS AUTHORITY DEPENDENCY`

Secondary tags are allowed, but the primary status must be unambiguous.

Rules:

- `PTE-3` is not runtime PASS.
- `PTE-4` cannot be self-closed by SMEs Core.
- `PTE-5` cannot be answered by AI.
- a reference-system observation can support learning but cannot become SMEsPlus design authority merely because it is observed.

---

## 6. MANDATORY DOMAIN COVERAGE

Build the matrix across the complete relevant business chain, not only Accounting screens.

At minimum cover:

### A. Sales / AR

- quotation/order commitment;
- invoice policy alternatives already approved;
- delivery-related recognition boundaries;
- AR creation;
- payment/reconciliation;
- return/refund/reversal;
- tax/WHT where applicable;
- customer credit/control paths;
- service vs stockable paths.

### B. Purchase / AP

- demand trigger;
- RFQ/PO;
- receipt/service acceptance;
- vendor bill;
- AP liability;
- payment;
- return/debit/correction;
- landed/interim implications where applicable;
- dropship route.

### C. Inventory

- stock receipt;
- reservation;
- internal transfer;
- delivery;
- return;
- scrap;
- count/adjustment;
- negative-stock controls;
- lot/serial/tracking where relevant;
- valuation/costing method interaction;
- Product Category policy authority.

### D. Manufacturing

- BOM requirement;
- material issue/consumption;
- WIP;
- FG output;
- scrap/rework;
- cost accumulation;
- direct/indirect cost boundaries;
- capacity-related routing where applicable;
- manufacturing veto linkage.

### E. Accounting Core

- canonical Accounting Event identity;
- GL posting ownership;
- AR/AP event handoff;
- inventory valuation / COGS;
- bank/cash;
- reconciliation;
- tax/VAT/WHT;
- assets/depreciation;
- analytic/dimensions;
- period close;
- reversal/correction/adjustment;
- audit lineage.

### F. Cross-cutting SaaS controls

- Tenant isolation;
- Company isolation;
- role/privilege boundaries;
- retry/idempotency;
- event ordering;
- duplicate submission;
- partial failure;
- stale state;
- asynchronous/background processing;
- metering where relevant;
- immutable audit/evidence lineage.

---

## 7. BUSINESS NATURE ROUTING TESTS

Every scenario must answer whether it routes to:

- Inventory — if stock is affected;
- Accounting — if the business event has accounting consequence;
- Manufacturing — if production is required;
- Purchase — if procurement/replenishment/dropship is required;
- Tax — if statutory consequence exists;
- Payment/Bank — if settlement is required;
- Asset — if capitalization/depreciation is required;
- other modules where the business nature demands it.

Mandatory challenge examples:

- stock sale vs service sale;
- make-to-stock vs make-to-order;
- buy vs manufacture;
- dropship;
- direct buy->sell;
- raw material -> WIP -> FG;
- FG delivery -> COGS;
- consumable/expense immediate expense;
- invoice-before-delivery;
- delivery-before-invoice;
- return after invoice;
- return before invoice;
- scrap with/without salvage;
- partial receipt/delivery/invoice/payment;
- cross-company attempt;
- cross-tenant attempt;
- duplicate event/retry;
- reversal after downstream consumption.

---

## 8. EXECUTION SEQUENCE / CHECKPOINTS

Execute sequentially. Do not skip a checkpoint.

### PT-00 — Authority + Lineage Intake

Reproduce the Phase SA handoff and SC-60 Boss authorization.

Publish:
`PT00_AUTHORITY_AND_LINEAGE_INTAKE.md`

Checkpoint:
`CP-PT-00 — PRE-TEST AUTHORITY BASELINE REPRODUCED`

### PT-01 — Canonical Scenario Population

Reconcile:

- 22 Phase SA cross-module scenarios;
- 18 E2E scenarios;
- domain-specific scenarios needed to cover AP/AR/GL/Tax/Inventory Accounting/Bank/Asset/Analytic/Close;
- negative and adversarial cases.

No forced target count. Every added scenario requires a documented coverage reason.

Publish:
`PT01_CANONICAL_SCENARIO_POPULATION.md`

Checkpoint:
`CP-PT-01 — SCENARIO POPULATION RECONCILED`

### PT-02 — Input Completeness Matrix

For every scenario, prove that inputs are sufficient and identify missing mandatory facts.

Publish:
`PT02_INPUT_COMPLETENESS_MATRIX.md`

Any material unknown that can still be researched by SMEs Core must be resolved before proceeding.

Checkpoint:
`CP-PT-02 — INPUTS COMPLETE OR BOUNDED`

### PT-03 — Process Semantic and Control Matrix

Map the Phase S/SA process obligation without redesigning it.

Cover approvals, ownership, state preconditions, prohibited transitions, reversals and audit controls.

Publish:
`PT03_PROCESS_SEMANTIC_AND_CONTROL_MATRIX.md`

Checkpoint:
`CP-PT-03 — PROCESS OBLIGATIONS TESTABLE`

### PT-04 — Output / Consumer Contract Matrix

For every output, identify exactly which downstream module consumes it and what data is required.

Publish:
`PT04_OUTPUT_CONSUMER_CONTRACT_MATRIX.md`

Checkpoint:
`CP-PT-04 — OUTPUT HANDOFF COMPLETE`

### PT-05 — Routing and Business-Nature Proof

Test stock/manufacture/purchase/dropship/accounting routing and all material route alternatives.

Publish:
`PT05_BUSINESS_NATURE_ROUTING_PROOF.md`

Checkpoint:
`CP-PT-05 — ROUTING PROOF COMPLETE`

### PT-06 — Accounting + Inventory Universal Convergence

For every scenario, explicitly test accounting consequence and inventory consequence when applicable.

Publish:
`PT06_ACCOUNTING_INVENTORY_CONVERGENCE_MATRIX.md`

Checkpoint:
`CP-PT-06 — ACCOUNTING/INVENTORY CONVERGENCE COMPLETE`

### PT-07 — Manufacturing / Purchase / Dropship Challenge

Stress routing among Manufacturing, Purchase and Dropship including partial, exception and reversal cases.

Publish:
`PT07_MFG_PURCHASE_DROPSHIP_CHALLENGE.md`

Checkpoint:
`CP-PT-07 — SUPPLY ROUTING CHALLENGED`

### PT-08 — SaaS / Tenant / Company / Security Boundary Matrix

Test isolation and privileged-path requirements at specification/test-design level.

Do not claim executed cross-tenant runtime proof without lawful runtime evidence.

Publish:
`PT08_SAAS_BOUNDARY_MATRIX.md`

Checkpoint:
`CP-PT-08 — SAAS BOUNDARIES TESTABLE`

### PT-09 — Exception / Reversal / Recovery / Idempotency Matrix

Cover:

- duplicate requests;
- same-event retry;
- partial failures;
- reversal;
- cancellation;
- correction;
- adjustment;
- stale/out-of-order events;
- downstream failure and recovery.

Publish:
`PT09_EXCEPTION_RECOVERY_IDEMPOTENCY_MATRIX.md`

Checkpoint:
`CP-PT-09 — FAILURE MODES COVERED`

### PT-10 — Test Evidence Classification + Runtime Boundary

Classify every row PTE-1..PTE-5.

Explicitly reconcile all execution-dependent carry-forward obligations including EC-04, E2E-04 and 0/22 runtime verification.

Publish:
`PT10_EVIDENCE_CLASS_AND_RUNTIME_BOUNDARY.md`

Checkpoint:
`CP-PT-10 — NO FAKE RUNTIME PROOF`

### PT-11 — Boss / External / Veto Dependency Reconciliation

Reconcile:

- 6 active vetoes;
- 6 Boss elections held;
- POH-D-02 Thai statutory dependency;
- AAS+ concurrence / limb-2 re-wording;
- Manufacturing veto;
- all external authority inputs.

Do not ask Boss any item SMEs Core can still resolve.

Publish:
`PT11_AUTHORITY_VETO_DEPENDENCY_REGISTER.md`

Checkpoint:
`CP-PT-11 — AUTHORITY DEPENDENCIES CLEANLY SEPARATED`

### PT-12 — Canonical Pre-Test Matrix

Publish one canonical matrix integrating PT-01..PT-11.

Required output:
`PT12_CANONICAL_PHASE_PRETEST_MATRIX.md`

Every row must have a source/evidence pointer and a disposition.

Checkpoint:
`CP-PT-12 — PRE-TEST MATRIX COMPLETE`

### PT-13 — SMEs Core Falsification

Attempt to break the matrix.

Challenge classes at minimum:

1. missing input;
2. ambiguous process;
3. output not consumable downstream;
4. accounting consequence omitted;
5. inventory consequence omitted;
6. wrong manufacture/purchase/dropship route;
7. cross-tenant/company leakage;
8. missing reversal/correction path;
9. non-idempotent retry;
10. approval bypass;
11. unsupported assumption;
12. vendor behavior copied as requirement;
13. untestable expected result;
14. false runtime proof;
15. hidden Boss decision;
16. hidden external dependency;
17. current-scope gap dumped forward;
18. contradiction with Boss ruling;
19. evidence pointer integrity failure;
20. scenario count or denominator defect.

Correct every verified material finding and repeat the affected checkpoint.

Publish:
`PT13_SMES_CORE_FALSIFICATION_REGISTER.md`

Checkpoint:
`CP-PT-13 — INTERNAL FALSIFICATION COMPLETE`

### PT-14 — B-7 Structurally Independent Challenge

Freeze a challenge baseline and manifest.

Route the frozen package to the eligible independent verifier under B-7.

The current Claude Opus 5 executor must not self-certify B-7.

Independent mandate: **FALSIFY the package**.

At minimum attack:

- Reading C / 8C clarification consequences;
- Phase S retrospective gate mapping;
- scenario completeness;
- accounting/inventory convergence;
- routing completeness;
- tolerance-zero carry-forward;
- hidden later-phase dumping;
- evidence integrity.

If B-7 returns a material finding:

`FINDING -> VERIFY AGAINST PRIMARY EVIDENCE -> CORRECT -> RE-RUN AFFECTED CHECKPOINTS -> RE-FREEZE -> RE-CHALLENGE`

Publish:
`PT14_B7_INDEPENDENT_CHALLENGE_REGISTER.md`

Checkpoint only when independent evidence exists:
`CP-PT-14 — INDEPENDENT CHALLENGE CONSUMED`

### PT-15 — Final Coverage / Evidence Integrity Sweep

Verify:

- unique IDs;
- denominator integrity;
- no orphan rows;
- all evidence pointers resolve;
- no hidden source-copying;
- no missing consumers;
- all unresolved items have authorized owners;
- all statuses use allowed semantics;
- no veto self-discharged;
- no PTE-3/4/5 mislabelled PASS.

Publish:
`PT15_FINAL_COVERAGE_AND_EVIDENCE_INTEGRITY.md`

Checkpoint:
`CP-PT-15 — FINAL INTEGRITY CLEAN`

### PT-16 — Boss Functional-Design Entry Gate Pack

Only after PT-00..PT-15 are complete, publish:

`PT16_BOSS_FUNCTIONAL_DESIGN_ENTRY_GATE_PACK.md`

The pack must separate:

- CLOSED by Pre-Test evidence;
- execution-dependent later proof;
- external-authority dependency;
- genuine Boss decision;
- veto still in force;
- unresolved blocker.

Terminal recommendations allowed:

- `RECOMMEND READY FOR FUNCTIONAL DESIGN ENTRY`
- `RECOMMEND HOLD — MATERIAL PRE-TEST GAP`
- `RECOMMEND HOLD — EXTERNAL AUTHORITY INPUT REQUIRED`
- `RECOMMEND HOLD — BOSS AUTHORITY DECISION REQUIRED`

AI/PMO may recommend only.
Boss alone decides entry to Functional Design.

---

## 9. AUTOMATION / AUTO-RESUME

Proceed autonomously through all authorized checkpoints.

At every checkpoint:

- write the artifact;
- update the manifest;
- record current head commit;
- record open findings;
- record next checkpoint;
- preserve single-writer state;
- continue automatically if no genuine authority stop exists.

Do not ask Boss routine questions.

Stop only if:

1. a genuine Boss-authority decision is irreducibly required;
2. an external authority input is required and no lawful parallel work remains;
3. B-7 requires an external independent execution that this session cannot perform;
4. a material contradiction makes further work unsafe;
5. PT-16 Boss Final Gate is ready.

Maintain:
`PHASE_PRETEST_AUTO_RESUME_STATE.md`

---

## 10. TARGETED VERY DEEP RESEARCH RE-ENTRY

Do not reopen Phase S broadly.

If Pre-Test proves a new material knowledge gap:

- isolate the exact function;
- preserve current evidence;
- open Targeted Very Deep Research only for that function;
- resolve the gap;
- re-synthesize;
- re-run the affected Pre-Test rows;
- re-run falsification;
- return to the same Pre-Test session.

No repeated research without material delta.

---

## 11. SUCCESS CONDITION

Success is NOT a high PASS percentage.

Success means:

- every material cross-module scenario is represented;
- every input/process/output/downstream contract is explicit;
- every accounting/inventory/manufacturing/purchase consequence is correctly routed;
- every test is evidence-grounded and testable;
- unresolved execution-dependent work is honestly classified;
- no specification gap is hidden in a later phase;
- B-7 findings are consumed correctly;
- final evidence integrity is clean;
- Boss receives only the true decision required to enter Functional Design.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
