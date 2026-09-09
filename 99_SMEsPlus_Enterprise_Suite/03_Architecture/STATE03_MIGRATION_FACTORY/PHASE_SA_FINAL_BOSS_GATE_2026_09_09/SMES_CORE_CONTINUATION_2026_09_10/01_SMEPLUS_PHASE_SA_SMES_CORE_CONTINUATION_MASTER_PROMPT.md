# [SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]
# ACCOUNT PHASE SA — SMEs CORE FINAL SCRUB CONTINUATION MASTER PROMPT

Project: SMEsPlus ENTERPRISE SUITE  
Phase: **PHASE SA ONLY**  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`  
Parent Final Boss Gate package: `9d5bc2db4a6b62c4cd01a04388b5bad23e6f5306`  
Boss: **Sole Final Approver**  
Execution owner: **SMEs Core**  
Challenge owner: relevant **SMT / Specialist Teams**  
Mode: controlled continuation / no reset / no architecture restart

---

## 1. BOSS AUTHORIZATION

Boss authorizes SMEs Core to continue Phase SA closure work autonomously within its authority.

This authorization means:

> **Exhaust Team Authority Before Boss Escalation.**

It does **NOT** authorize SMEs Core to make Boss-only business/risk-policy decisions, discharge another body's veto, declare independent assurance, close Phase SA by itself, start Functional Design, implement application code, merge/release/deploy, or move to Production.

Boss must not be the first detector of an unresolved functional, clean-room, evidence, control, or cross-module defect.

> **SMT detects first -> SMEs Core / SMT researches and resolves first -> SMT challenges first -> Boss receives only genuinely Boss-owned decisions.**

If a material defect reaches Boss without prior SMT detection/triage when it was reasonably detectable, record it as an `SMT Escape`, perform root-cause analysis, and publish a prevention control.

---

## 2. FROZEN CONTEXT — DO NOT RESET

Preserve all completed Phase S and Phase SA evidence and Boss-approved decisions. Do not restart Phase S, do not restart Account research from L1, and do not repeat completed questions without material delta.

Carry forward at minimum:

- Phase S: `CONDITIONALLY CLOSED` with controlled targeted Very Deep Research re-entry.
- Phase SA: architecture/synthesis work substantially complete and at Final Boss Gate preparation state.
- Boss-approved Clean Room 100% direction.
- `SOURCE IS EVIDENCE, NOT DESIGN.`
- `LEARN BEHAVIOR, NOT STRUCTURE.`
- `TRANSFER BUSINESS MEANING, NOT APPLICATION ARCHITECTURE.`
- Every SMEsPlus design requires an independent clean-room rationale.
- SMEsPlus-owned persistent business tables use the `smeplus_*` namespace.
- Boss-approved `BD-ACC-01`, `BD-ACC-02`, `BD-ACC-03A`, `BD-ACC-03B` are not re-askable absent material delta.
- Boss is the sole Final Approver.

Do not mutate historical evidence to make current conclusions look cleaner. Preserve supersession and contradiction lineage.

---

## 3. CURRENT DELTA THAT MUST BE RE-MEASURED FIRST

The parent Final Boss Gate package `9d5bc2db...` was published while PR #63 was still open and the unqualified standards-compliance claim remained live on mainline.

Since that publication, PR #63 was merged and the mainline correction was recorded at merge commit:

`3f5d915a2dc14f8121c4292e863f08b743992101`

SMEs Core MUST independently re-measure the current default branch before inheriting this as closed.

Required output:

`SC-00_PMO_MAINLINE_DELTA_REMEASUREMENT.md`

It must state exactly:

1. current default-branch SHA,
2. PR #63 state and merge SHA,
3. whether the prior unqualified compliance claim is still live,
4. whether the former Category-3 PMO mainline blocker is now CLOSED, OPEN, or CHANGED,
5. evidence commands/paths used,
6. whether any new material delta was introduced by the merge.

No Evidence = No Progress.

---

## 4. SMEs CORE PRIMARY WORK — FINAL DECISION SCRUB

Take the eight Final Gate decision families `F1`–`F8` as an input population, not as automatically Boss-bound questions.

For every family, SMEs Core MUST perform the following authority scrub before escalation:

### A. Existing-authority test
Determine whether an existing Boss ruling, approved architecture principle, constitutional rule, source-independent business fact, or already-closed cross-module contract already resolves all or part of the family.

### B. SMEs Core authority test
Determine what SMEs Core can decide as architecture/specification without Boss policy choice.

### C. SMT specialist test
Send the domain-specific issues to the relevant SMT first-line specialists for challenge before Boss escalation.

### D. Evidence sufficiency test
If evidence is materially insufficient or contradictory, do not ask Boss to guess. Open **targeted Very Deep Research** for only the affected function/question.

### E. Clean-room test
For every surviving recommendation answer:

- What did we learn?
- What did we deliberately NOT inherit?
- What alternatives were considered?
- Why is this SMEsPlus's own design?
- What is SMEsPlus doing better or differently?

### F. Boss-only test
Escalate only when the remaining choice is genuinely one of:

- business policy,
- risk appetite,
- scope/meaning of an existing Boss ruling,
- change to a Boss-approved constitution,
- final acceptance of a materially bounded trade-off,
- Final Gate authority.

Required output:

`SC-01_FINAL_DECISION_SCRUB_REGISTER.md`

For each F1–F8 show:

`Family | Original IDs | SMEs Core closable | SMT required | Targeted research required | Existing Boss ruling applicable | Remaining Boss-only decision | Recommendation | Evidence | Status`

The goal is to **minimize Boss cognitive load without hiding any material choice**.

---

## 5. MANDATORY FAMILY-SPECIFIC HANDLING

### F1 — COGS recognition and reversal basis
Do not merely restate prior alternatives. Reconcile the existing approved direction that COGS is associated with delivery/physical movement with the current Phase SA event model, and distinguish:

- business recognition event,
- accounting posting event,
- invoice event,
- return/reversal cost basis.

If any apparent conflict with prior Boss-approved direction exists, state the conflict explicitly and classify whether it is a true policy conflict or only terminology/model-layer confusion.

Do not re-ask a question already ruled unless a material contradiction is proven.

### F2 — Commercial control-default policy
SMEs Core may recommend the default control posture, but if the choice is truly risk appetite, retain it as Boss-only. Verify that `block`, `warn-and-allow`, and any override path preserve audit evidence and Company scope.

### F3 — Dropship valuation and cost landing
This family has a live standing dissent. It MUST NOT be escalated to Boss until SMEs Core performs a bounded evidence re-read of the relevant buy-side / Inventory / Accounting evidence.

If the evidence resolves the question, close or narrow it within team authority. If not, trigger targeted Very Deep Research only for the unresolved dropship semantics.

Required dedicated output:

`SC-02_F3_DROPSHIP_BOUNDED_VERIFICATION.md`

### F4 — Cross-module contract scope and supply binding
This includes a Pre-Test-entry scope issue. SMEs Core MUST provide a direct architecture recommendation on whether the 16-element handoff contract should apply to all required cross-module boundaries, and must challenge the recommendation against Clean Room / Nature DNA principles.

Do not leave eleven boundaries uncontracted merely because the original approval named one boundary unless a deliberate architecture rationale supports that limitation.

### F5 — Manufacturing overhead governance
Separate statutory/accounting constraints from configurable business policy. Do not present a false binary where one branch is already invalidated by evidence. Restate the decision family into only live choices.

### F6 — Cross-company visibility and commercial scope
Reconcile this family against `BD-ACC-02`: no cross-company statutory posting/offset/filing; management information may aggregate. Distinguish management visibility from statutory accounting ownership. Do not re-ask already-closed statutory scope.

### F7 — Authorization axis and configurable-record scope
Use the approved Tenant/Company isolation and existing authorization-axis rulings first. Escalate only the genuinely unresolved axis/scope choice. The Pre-Test denominator must be explicit before entry.

### F8 — Idempotency severity
Respect `BD-ACC-01`: same-event retry must not duplicate Accounting Events and Accounting Core owns canonical identity. The open question, if any, is gate severity/proof timing — not whether idempotency is required.

---

## 6. TARGETED VERY DEEP RESEARCH RE-ENTRY RULE

Phase S remains conditionally closed. Phase SA may return a function to Very Deep Research when SMEs Core/SMT detects a material gap.

Re-entry MUST be:

- targeted to the affected function/question,
- evidence-preserving,
- Boss-ruling-preserving,
- non-resetting,
- bounded by an explicit unknown register,
- followed by fresh synthesis and SMT challenge before return to Phase SA.

Do not use Very Deep Research as a substitute for making an architecture decision when evidence is already sufficient.

Required output for each re-entry, if any:

`SC-TVR-xx_<FUNCTION>_TARGETED_RESEARCH_REENTRY.md`

If none is needed, publish the explicit result: `NO TARGETED RESEARCH RE-ENTRY REQUIRED` with basis.

---

## 7. SMT FIRST-LINE CHALLENGE

Before any updated Boss pack is published, every surviving family must be challenged by the SMT(s) relevant to that family.

At minimum consider:

- Accounting / Thai Accounting-Tax SMT,
- Inventory SMT,
- Manufacturing/Costing SMT,
- SaaS/Multi-Company SMT,
- Internal Control / Audit SMT,
- Cross-Module Integration SMT.

Each SMT disposition must be one of:

`PASS / PASS WITH CONDITION / RETURN TO SME CORE / TARGETED VERY DEEP RESEARCH / BOSS-ONLY DECISION`

Required output:

`SC-03_SMT_FIRST_LINE_CHALLENGE_REGISTER.md`

No family may reach Boss without an SMT disposition.

---

## 8. VETO / INDEPENDENCE BOUNDARY

SMEs Core may satisfy the factual basis of a veto but may NOT discharge another authority's veto.

For each veto still in force:

- identify issuer,
- identify current factual basis,
- identify whether SMEs Core work is complete,
- identify the exact next authority/action.

Required output:

`SC-04_VETO_AUTHORITY_HANDOFF_REGISTER.md`

Also preserve the distinction:

- internal adversarial self-challenge != structural independent assurance.

Do not self-declare independent PASS.

The scope question concerning `SMEPLUS-DR-EXIT-8C-001` must be presented only after SMEs Core has completed all work within its own authority. If the constitution's applicability can only be determined by Boss because it changes the scope of a Boss-approved project-wide rule, prepare a one-page scope-clarification card with both readings, consequences, and SMEs Core recommendation — do not decide it unilaterally.

---

## 9. UPDATED PRE-TEST ENTRY QUALIFICATION

After sections 3–8, recompute Pre-Test entry qualification from current evidence.

Do not inherit the old blocker count.

Required output:

`SC-05_PRETEST_ENTRY_REQUALIFICATION.md`

It must enumerate exactly:

- CLOSED entry conditions,
- OPEN entry conditions,
- Boss-only entry decisions,
- external-authority actions,
- structurally independent review obligations, if applicable,
- targeted research re-entry, if any.

Do not start the Pre-Test Matrix in this continuation.

---

## 10. UPDATED BOSS FINAL GATE PACK

Only after all preceding work is complete may SMEs Core publish an updated Boss decision pack.

Required output:

`SC-06_BOSS_FINAL_GATE_DELTA_PACK.md`

The pack must contain only:

1. decisions genuinely requiring Boss authority,
2. a clear SMEs Core recommendation for each,
3. SMT challenge/disposition,
4. evidence references,
5. consequences of each alternative,
6. what is already closed and must not be re-asked,
7. any remaining Veto/Independent Review actions outside Boss decision scope.

Never present Boss with raw research ambiguity that SMEs Core/SMT can still resolve.

Target principle:

> **Boss decides policy; teams exhaust evidence, architecture, and challenge first.**

---

## 11. CHECKPOINTS

Use this controlled ladder:

- `CP-SA-SC-00` — Mainline delta re-measured
- `CP-SA-SC-10` — F1–F8 authority scrub complete
- `CP-SA-SC-20` — F3 bounded verification complete
- `CP-SA-SC-30` — Any targeted Very Deep Research completed or explicitly not required
- `CP-SA-SC-40` — SMT first-line challenge complete
- `CP-SA-SC-50` — Veto/authority handoff reconciled
- `CP-SA-SC-60` — Pre-Test entry re-qualified
- `CP-SA-SC-70` — Updated Boss Final Gate Delta Pack published
- `CP-SA-SC-FINAL` — `READY FOR BOSS PHASE SA FINAL DECISION` only if evidence actually supports it

Checkpoint completion is not Boss approval.

---

## 12. STOP CONDITIONS / PROHIBITIONS

Do NOT:

- restart Phase S,
- restart Account research from L1,
- repeat approved Boss questions without material delta,
- redesign by copying source ERP architecture/schema/ORM/workflow/UI,
- assume source behavior is SMEsPlus design authority,
- self-discharge vetoes,
- self-claim structural independence,
- self-close Phase SA,
- start Pre-Test Matrix execution,
- start Functional Design,
- start physical database/API/UI design beyond what is necessary to clarify architecture semantics,
- write application code,
- merge/release/deploy,
- authorize Production.

If an unresolved function is not clean or not complete, SMEs Core/SMT must catch it before Boss and use the targeted re-entry rule.

---

## 13. TERMINAL STATES

This continuation may terminate only in one of these states:

### TERMINAL A
`READY FOR BOSS PHASE SA FINAL DECISION`

Use only when SMEs Core authority is exhausted, SMT challenge is complete, all team-owned material gaps are closed/bounded, and the updated Boss pack contains only genuinely Boss-owned decisions/actions.

### TERMINAL B
`HOLD — TARGETED VERY DEEP RESEARCH REQUIRED`

Name the exact function/question and bounded research scope.

### TERMINAL C
`HOLD — EXTERNAL AUTHORITY / INDEPENDENT REVIEW REQUIRED`

Name the exact authority, veto issuer, or independent-review requirement.

### TERMINAL D
`HOLD — MATERIAL SME CORE / SMT GAP REMAINS`

This is an execution failure state for the continuation. Boss must not be asked to compensate for unfinished team work.

---

No Evidence = No Progress.  
Never Skip Gate.  
Boss is the sole Final Approver.  
Source is evidence, not design.  
SMT must detect first.  
Exhaust Team Authority Before Boss Escalation.
