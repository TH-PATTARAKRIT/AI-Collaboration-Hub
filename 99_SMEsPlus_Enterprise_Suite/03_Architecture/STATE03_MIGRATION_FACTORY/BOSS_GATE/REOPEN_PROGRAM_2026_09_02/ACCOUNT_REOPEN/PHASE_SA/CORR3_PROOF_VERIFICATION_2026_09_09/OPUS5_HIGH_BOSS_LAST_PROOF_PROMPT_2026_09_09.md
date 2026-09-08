# [SMEPLUS-26-09-09-PHASE-SA-CORR3-PROOF-001]
# SMEsPlus PHASE SA — CORR3 PROOF, TARGETED STUDY, CROSS-PROOF RE-RUN & FINAL-GATE QUALIFICATION
# BOSS LAST PROOF EXECUTION PROMPT
# Claude Opus 5 / Effort High
# /L99999.99999

Repository:
`TH-PATTARAKRIT/AI-Collaboration-Hub`

Control Branch:
`architecture/phase-sa-corr3-proof-verification-2026-09-09-001`

Parent CORR2 Publication Commit:
`990f915ed39e6a5a07c16cecb1d2c5d099b8c227`

Parent Canonical Session:
`[SMEPLUS-26-09-08-ACC-PHASE-SA-NEWSESSION-001]`

Execution Model:
`Claude Opus 5 — Effort High`

Execution Mode:
`AUTONOMOUS / SMEs CORE / TARGETED VERY DEEP STUDY / PROOF-FIRST / EVIDENCE-FIRST / DELTA-FIRST / CHECKPOINT-CONTROLLED`

Boss Interaction Mode:
`BOSS FINAL GATE ONLY`

Boss:
`SOLE FINAL APPROVER`

Current inherited state:
`PHASE SA = HOLD — SMEs CORE TARGETED DEEP STUDY & RE-CHALLENGE REQUIRED`

---

## 0. WHY THIS ROUND EXISTS

CORR2 reached a Boss Gate too early.

The remaining issues were still partly:

- UNKNOWN;
- UNPROVEN;
- UNVERIFIED;
- architecture ambiguity;
- cross-module proof gaps;
- governance correction items;
- structural-independence qualification items.

These must NOT be pushed to Boss as design questions merely because they are difficult.

This CORR3 round exists to enforce the following rule:

> EVERY MATERIAL FINDING THAT IS STILL UNKNOWN, UNPROVEN OR UNVERIFIED MUST FIRST PASS SMEs CORE STUDY, PROOF, CROSS-DOMAIN SYNTHESIS, RE-CHALLENGE AND EVIDENCE VERIFICATION BEFORE IT MAY APPEAR AT BOSS FINAL GATE.

Boss must not become the first-line researcher, designer, debugger or proof authority.

---

## 1. CORE PHASE SA LAW

All material flows must be proven using:

`INPUT -> PROCESS -> OUTPUT -> DOWNSTREAM ROUTING -> NEXT MODULE INPUT`

Phase S remains the Process Knowledge baseline.

Phase SA must prove cross-module completeness.

Mandatory routing/convergence rules:

- Stock-affecting flow -> Inventory.
- Manufacture-required flow -> Manufacturing.
- Procurement-required / Dropship flow -> Purchase.
- Every material business flow -> Accounting semantic reconciliation.
- One Output may have multiple downstream consumers.
- Routing follows Business Nature, not module name alone.

Do not restart Phase S.
Do not restart L1.
Do not reopen unrelated verified work.

---

## 2. NON-NEGOTIABLE CORR3 OBJECTIVE

Convert every remaining material Phase SA item from one of:

`UNKNOWN / UNPROVEN / UNVERIFIED / AMBIGUOUS / ASSUMED`

to one of:

`EVIDENCE-PROVEN`
`EVIDENCE-REJECTED`
`NOT APPLICABLE — EVIDENCE-BACKED`
`TARGETED RESEARCH COMPLETE — PROOF ESTABLISHED`
`MATERIAL HOLD — EXACT UNRESOLVED PROOF GAP`

No material item may remain merely “covered”.

No material invariant may remain merely “specified”.

No material Boss question may survive unless the technical/business uncertainty has already been reduced to an actual policy or authority choice.

---

## 3. CORR2 FINDING RE-CLASSIFICATION

Re-open the latest CORR2 Boss Final Gate Pack and all cited evidence.

For every requested decision or blocker, classify it as exactly one of:

A. `SMEs CORE CAN RESOLVE — STUDY/PROOF REQUIRED`
B. `GOVERNANCE CORRECTION — NO BOSS DECISION REQUIRED`
C. `STRUCTURAL INDEPENDENCE ACTION REQUIRED`
D. `GENUINE BOSS POLICY/AUTHORITY DECISION AFTER PROOF`

Do not preserve the previous Boss-decision classification by default.

Required artifact:
`SA_CORR3_00_DECISION_RECLASSIFICATION.md`

Checkpoint:
`CP-SA-C3-00 — DECISIONS RECLASSIFIED BEFORE ESCALATION`

---

## 4. REQUIRED TARGETED VERY DEEP STUDY — XD-01 CUSTOMER INVOICE DURABILITY

The prior pack identified a customer-invoice-state durability issue.

Do NOT ask Boss to choose a state or design.

SMEs Core must study and prove:

- what business fact must become durable;
- which module owns that fact;
- when it becomes authoritative;
- which downstream processes depend on it;
- what must survive retry/restart/reversal;
- what may be transient;
- what must be immutable or append-only;
- what control requires blocking authority;
- what accounting/tax/payment consequences exist;
- how correction/reversal works;
- Tenant/Company boundary;
- audit/evidence requirements;
- at least two independent architecture alternatives where meaningful;
- why the recommended SMEsPlus semantic is independently justified.

Do not copy a vendor workflow/state model.

Required artifact:
`SA_CORR3_01_XD01_CUSTOMER_INVOICE_DURABILITY_PROOF.md`

Acceptance condition:
`XD-01 must end as EVIDENCE-PROVEN architecture recommendation OR exact material HOLD with the remaining unknown explicitly bounded.`

---

## 5. REQUIRED TARGETED VERY DEEP STUDY — C2-D-03 KIT / PRODUCT CATEGORY COSTING

Do NOT ask Boss to resolve the ambiguity until SMEs Core has proven the business and accounting semantics.

Study at minimum:

- logical/non-stock Kit;
- stock Bundle;
- component-level inventory consumption;
- manufactured Kit/FG where applicable;
- component Product Categories;
- parent Product Category;
- valuation recognition;
- Standard/Average/FIFO behavior;
- COGS recognition;
- returns;
- partial delivery;
- substitution where applicable;
- price difference;
- inventory/accounting reconciliation;
- whether any true conflict exists with Boss-approved `BD-ACC-03A/03B`.

Preserve Boss-approved rule unless evidence proves a genuine policy gap:

- Inventory Valuation Recognition = `Periodic | Perpetual`, Product Category only, no Product override.
- Costing Method = `Standard | Average | FIFO`, Product Category only, no Product override.

Required artifact:
`SA_CORR3_02_KIT_CATEGORY_COSTING_PROOF.md`

Acceptance condition:
`Determine whether existing Boss policy already resolves the case. Escalate only if a genuine policy choice remains after proof.`

---

## 6. REQUIRED TARGETED VERY DEEP STUDY — BLK-07 PRODUCTION OVERHEAD

The prior pack reported that Production Overhead lacked a proven path.

SMEs Core must deeply study and prove the complete semantic chain:

`Cost Source -> Cost Classification -> Allocation Basis -> Manufacturing Consumption/Absorption -> WIP/FG Cost -> Accounting Fact/Event -> Posting/Reporting`

Study at minimum:

- fixed production overhead;
- variable production overhead if applicable;
- normal capacity treatment;
- under/over absorption;
- idle capacity;
- direct vs indirect production cost;
- Work Center relationship;
- period timing;
- standard vs actual cost implications;
- inventory valuation interaction;
- COGS interaction;
- month close interaction;
- reversals/corrections;
- evidence lineage;
- clean-room rationale.

Do not assume a vendor costing engine is the target.

Required artifact:
`SA_CORR3_03_PRODUCTION_OVERHEAD_PROOF.md`

Acceptance condition:
`Production overhead path must be EVIDENCE-PROVEN or explicitly HOLD with exact unresolved semantic/proof gap.`

---

## 7. REQUIRED TARGETED VERY DEEP STUDY — BLK-07 MAINTENANCE COST TO ACCOUNTING FACT

The prior pack also reported Maintenance Cost had not become a proven Accounting Fact path.

Study and prove applicable routes such as:

- Maintenance expense directly to period cost;
- Maintenance related to production equipment;
- capitalization where legally/accountingly appropriate;
- production cost allocation where appropriate;
- Asset relationship;
- Work Center relationship;
- downtime effects where material;
- monthly close;
- accounting event ownership;
- posting ownership;
- reversal/correction;
- audit trail.

Do not assume all Maintenance must enter manufacturing cost.

Classify by Business Nature and accounting substance.

Required artifact:
`SA_CORR3_04_MAINTENANCE_COST_ACCOUNTING_FACT_PROOF.md`

---

## 8. GOVERNANCE ITEMS — FIX, DO NOT ASK BOSS TO RESEARCH

The following are governance/control corrections unless current evidence proves otherwise:

### 8.1 Standards/Compliance Overclaim

Search the entire active Phase SA package for unqualified claims involving:

- ISO 27001;
- ISO 9001;
- SOC 2;
- GDPR;
- `CERTIFIED`;
- compliance/conformance/certification wording;
- any other named standard/framework.

Classify statements as:

`REQUIREMENT MAPPING`
`CONTROL DESIGN TARGET`
`EVIDENCE-BACKED CONFORMANCE`
`CERTIFICATION/ATTESTATION VERIFIED`
`UNQUALIFIED CLAIM — RETRACT/CORRECT`
`NOT APPLICABLE`

Do not claim certification without certification evidence and authority.

### 8.2 PASS / Approval Authority

Normalize the distinction:

- Technical/SMEs Core bodies may publish `PASS/HOLD RECOMMENDATION` when authorized.
- They may publish checkpoint evidence/readiness.
- Final Phase approval remains Boss authority.
- `PASS` must not be written in a way that falsely implies Boss Final Approval.

Correct all conflicting material wording before Final Gate.

Required artifact:
`SA_CORR3_05_GOVERNANCE_AND_STANDARDS_CORRECTION.md`

Checkpoint:
`CP-SA-C3-20 — GOVERNANCE CLAIMS CORRECTED`

---

## 9. 22/22 JOINT CROSS-PROOF — RE-RUN FOR VERIFICATION, NOT COVERAGE

The prior result stated:

`22 of 22 covered, 0 of 22 verified.`

Coverage is insufficient.

Re-run the Joint Cross-Proof.

For each of the 22 scenarios, prove:

- exact Inputs;
- upstream authoritative source;
- Process baseline;
- exact Outputs;
- all downstream consumers;
- conditional routing;
- Inventory effect if applicable;
- Manufacturing effect if applicable;
- Purchase/AP effect if applicable;
- Sales/AR effect if applicable;
- Accounting semantics;
- Tax/Payment effect;
- exception/reversal behavior;
- Tenant/Company boundary;
- evidence pointers;
- proof result.

Allowed per-scenario result:

`VERIFIED`
`NOT APPLICABLE — EVIDENCE-BACKED`
`HOLD — EXACT PROOF GAP`

Not allowed:

`COVERED ONLY`
`ASSUMED`
`INFERRED WITHOUT EVIDENCE`

Required artifact:
`SA_CORR3_06_JOINT_CROSS_PROOF_VERIFICATION_22X22.md`

Checkpoint:
`CP-SA-C3-30 — JOINT CROSS-PROOF VERIFIED OR EXACTLY BOUNDED`

---

## 10. 58 INVARIANTS — BUILD AND PROVE

The prior pack stated:

`58 specified, 0 proven.`

A specified invariant is not a proven invariant.

For every in-scope invariant:

- state the invariant;
- explain why it exists;
- identify owner;
- identify affected domains;
- identify enforcement point conceptually;
- identify evidence;
- construct proof/test logic;
- run available evidence verification;
- record contradiction;
- record exception if permitted;
- classify result.

Allowed results:

`PROVEN`
`NOT APPLICABLE — EVIDENCE-BACKED`
`SUPERSEDED — EVIDENCE-BACKED`
`HOLD — PROOF MISSING`

Do not leave any invariant as merely `SPECIFIED` in the final register.

Required artifact:
`SA_CORR3_07_INVARIANT_PROOF_REGISTER.md`

Checkpoint:
`CP-SA-C3-40 — INVARIANT PROOF STATUS COMPLETE`

---

## 11. CROSS-MODULE OUTPUT -> INPUT CONTRACT PROOF

For every material handoff, prove:

`UPSTREAM OUTPUT = DOWNSTREAM REQUIRED INPUT`

At minimum test:

- Sales -> Inventory;
- Sales -> Manufacturing where make is required;
- Sales -> Purchase where Dropship/Buy/MTO requires procurement;
- Manufacturing -> Inventory;
- Inventory -> Accounting;
- Sales -> AR/Accounting;
- Purchase -> AP/Accounting;
- Payment -> Bank/Accounting;
- Asset -> Accounting;
- Expense -> Accounting;
- Tax -> Accounting/reporting;
- Close -> all required subledgers/control sources.

One Output may produce multiple downstream obligations.

Required artifact:
`SA_CORR3_08_CROSS_MODULE_CONTRACT_PROOF.md`

Checkpoint:
`CP-SA-C3-50 — CROSS-MODULE CONTRACTS PROVEN OR BOUNDED`

---

## 12. SMEs CORE MANDATORY MULTI-SPECIALIST PROOF PANEL

Every material finding must be reviewed by the relevant SMEs Core perspectives before Boss sees it.

Use as applicable:

- Functional Domain Owner;
- Sales / AR;
- Purchase / AP;
- Inventory;
- Manufacturing;
- Accounting / Posting;
- Tax;
- Bank / Payment;
- Asset;
- Expense / Cost;
- Data / Identity / Integration;
- SaaS / Tenant / Company;
- Security;
- Audit / Standards;
- Clean-room;
- UX / Operations;
- External ERP Advisor / Challenger.

Each material issue must record:

- initial hypothesis;
- evidence;
- dissent;
- contradiction;
- research performed;
- proof performed;
- final SMEs Core recommendation;
- residual uncertainty.

Required artifact:
`SA_CORR3_09_SMES_CORE_PROOF_PANEL.md`

---

## 13. FIRST-DETECTOR RULE — ENFORCE STRICTLY

Boss must never be the first detector of an obvious:

- functional defect;
- missing routing;
- missing Input;
- unusable Output;
- missing inventory effect;
- missing accounting effect;
- unproven invariant;
- missing reversal;
- unsupported compliance claim;
- tenant/company leakage;
- vendor-copying risk;
- evidence mismatch.

If SMEs Core can study or prove it, SMEs Core MUST do so before escalation.

Boss receives only:

- fully studied issue;
- verified evidence;
- alternatives;
- impacts;
- SMEs Core recommendation;
- dissent result;
- exact authority/policy decision genuinely outside SMEs Core authority.

If this pack cannot be produced, the issue is NOT READY FOR BOSS.

---

## 14. STRUCTURAL INDEPENDENCE

Same-model subagents, role-play adversaries or repeated Opus self-review are useful but must be labelled:

`INTERNAL ADVERSARIAL SELF-CHALLENGE`

They are NOT structurally independent assurance.

If a structurally independent reviewer is available, submit the completed proof package for falsification only after SMEs Core proof is complete.

The independent challenger must:

- attempt to falsify claims;
- verify evidence pointers;
- search for false positives;
- search for false negatives;
- not rewrite the package;
- not inherit executor conclusions as facts.

If no structurally independent reviewer is available, record truthfully:

`EXTERNAL INDEPENDENT CHALLENGE — PENDING STRUCTURALLY INDEPENDENT REVIEW`

Do not fabricate independence.

Required artifact:
`SA_CORR3_10_INDEPENDENCE_STATUS.md`

---

## 15. AUTOMATION — BOSS MUST NOT BE INTERRUPTED

Execute autonomously.

Mandatory automation:

`AUTO-C3-01` Delta-first evidence consumption.

`AUTO-C3-02` Auto-split targeted study by issue/domain.

`AUTO-C3-03` Automatically trigger Targeted Very Deep Research when evidence is insufficient.

`AUTO-C3-04` Automatically re-synthesize findings into SMEsPlus semantics.

`AUTO-C3-05` Automatically re-challenge corrected items.

`AUTO-C3-06` Automatically rerun affected cross-proof scenarios.

`AUTO-C3-07` Automatically update proof registers.

`AUTO-C3-08` Automatically verify evidence pointers before use.

`AUTO-C3-09` Maintain `PHASE_SA_CORR3_AUTO_RESUME_STATE.md` after every checkpoint.

`AUTO-C3-10` Failure containment — one failed route does not reset unrelated verified routes.

`AUTO-C3-11` Boss silence — no routine questions.

`AUTO-C3-12` Final-Gate stop — do not begin Pre-Test Matrix.

---

## 16. CHECKPOINT LADDER

- `CP-SA-C3-00` — Boss Questions Reclassified
- `CP-SA-C3-10` — Targeted Deep Studies Complete or Precisely Bounded
- `CP-SA-C3-20` — Governance / Standards Corrections Complete
- `CP-SA-C3-30` — 22/22 Joint Cross-Proof Verification Complete
- `CP-SA-C3-40` — 58-Invariant Proof Register Complete
- `CP-SA-C3-50` — Cross-Module Output/Input Contracts Proven
- `CP-SA-C3-60` — Inventory / Manufacturing / Purchase Routing Reconciled
- `CP-SA-C3-70` — Accounting / Tax / Payment Convergence Reconciled
- `CP-SA-C3-80` — SMEs Core Proof Panel Complete
- `CP-SA-C3-90` — Structural Independence Status Verified
- `CP-SA-C3-95` — Final Evidence Integrity Verified
- `CP-SA-C3-FINAL` — Boss Final Gate Pack Published

Checkpoint completion is NOT Boss approval.

Continue automatically between checkpoints.

---

## 17. FINAL EVIDENCE INTEGRITY

Before Boss Final Gate verify:

- every material claim has evidence;
- every pointer resolves;
- no cited evidence file is empty/corrupt;
- every count is reproducible;
- 22-scenario status is reproducible;
- invariant status is reproducible;
- false positives are removed/superseded;
- no unsupported compliance claim remains;
- no misleading PASS/CERTIFIED wording remains;
- all material unresolved gaps have exact proof gap, owner and next action;
- no Boss question remains that SMEs Core could still research/prove itself.

Required artifact:
`SA_CORR3_11_FINAL_EVIDENCE_INTEGRITY.md`

Checkpoint:
`CP-SA-C3-95 — FINAL EVIDENCE INTEGRITY VERIFIED`

---

## 18. BOSS FINAL GATE QUALIFICATION TEST

Before any issue enters the Boss Final Gate Pack, answer YES to ALL:

1. Has the issue been deeply studied?
2. Has available evidence been consumed?
3. Has the relevant cross-module flow been proven/challenged?
4. Have at least the relevant SMEs Core specialists reviewed it?
5. Has material dissent been resolved or bounded?
6. Has the issue been checked for an existing Boss ruling?
7. Is the remaining question genuinely policy/authority rather than missing research/design/proof?

If ANY answer is NO:

`NOT READY FOR BOSS — RETURN TO SMEs CORE`

---

## 19. BOSS FINAL GATE PACK

Create:
`SA_CORR3_12_BOSS_FINAL_GATE_PACK.md`

It must include:

1. Executive disposition.
2. CORR2 issues reclassified.
3. Targeted Deep Study results.
4. XD-01 proof result.
5. C2-D-03 Kit/Category proof result.
6. BLK-07 Production Overhead proof result.
7. BLK-07 Maintenance Cost proof result.
8. Governance/Standards correction result.
9. 22/22 Joint Cross-Proof result by status.
10. 58-invariant proof result by status.
11. Cross-module contract proof result.
12. Inventory/Manufacturing/Purchase routing result.
13. Accounting/Tax/Payment convergence result.
14. SMEs Core Proof Panel result.
15. Independence status and exact basis.
16. Remaining material HOLDs.
17. Complete evidence index.
18. Exact Boss decisions that survived the qualification test.
19. SMEs Core recommendation for Phase Pre-Test Matrix.

Valid recommendations:

`RECOMMEND APPROVE TO PHASE PRE-TEST MATRIX`

`RECOMMEND CONDITIONAL APPROVAL TO PHASE PRE-TEST MATRIX`

`RECOMMEND HOLD PHASE SA — EXACT PROOF GAPS LISTED`

Only Boss may approve.

---

## 20. TERMINAL CONDITIONS

Continue autonomously until one of these occurs:

A. `BOSS FINAL GATE PACK READY — ALL BOSS QUESTIONS QUALIFIED`

or

B. `CONSTITUTIONAL / AUTHORITY BLOCKER — CANNOT PROCEED WITHOUT BOSS`

Condition B is valid only when SMEs Core has exhausted authorized research, proof, re-challenge, governance correction and evidence reconciliation.

Do not use Condition B for ordinary uncertainty.

---

## 21. PROHIBITIONS

Do NOT:

- restart Phase S;
- restart L1;
- ask Boss to design the answer;
- ask Boss to resolve unresearched ambiguity;
- leave material findings merely covered/unverified;
- leave in-scope material invariants merely specified/unproven;
- copy vendor architecture;
- fabricate evidence;
- fabricate structural independence;
- claim certification without evidence;
- begin Phase Pre-Test Matrix;
- begin Functional Design;
- begin Database/API/UI Design;
- write application code;
- merge;
- release;
- deploy;
- self-approve Phase SA.

---

## 22. STOP POINT

When `SA_CORR3_12_BOSS_FINAL_GATE_PACK.md` is published and evidence integrity is verified:

STOP AT:

# `BOSS FINAL GATE`

Do not proceed to Phase Pre-Test Matrix.

Boss remains the sole Final Approver.

No Evidence = No Progress.
Never Skip Gate.
Understand deeply.
Transfer accurately.
Preserve verifiably.
