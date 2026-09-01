# SMEsPlus NEW PROMPT Governance Standard — 9 Veto Challenge Council + 9 Special Team Challenge

Document ID: `SMEPLUS-26-08-30-PRE-PROMPT-CHALLENGE-001`  
Version: `v2.0`  
Status: `BOSS APPROVED / EFFECTIVE`  
Effective Date: `2026-09-02`  
Project: `SMEsPlus ENTERPRISE SUITE`  
Scope: `Every controlled Session and every controlled Prompt from STATE03 onward`  
Control Level: `/L999.999`  
Final Approval Authority: `Boss — Sole Final Approver`  
Supersedes: `v1.1` of this document

---

## 1. Boss Ruling

Boss approves a mandatory two-layer independent challenge structure for every controlled Session and Prompt:

1. **9 Veto Challenge Council — PRIMARY FUNCTION**
2. **9 Special Team Challenge — SECONDARY / DEEP-INVESTIGATION FUNCTION**

Both challenge layers report directly to Boss for authority purposes.

PMO / Secretary is the **Evidence Custodian, Challenge Coordinator and Record Keeper only**. PMO does not command the Council, does not command the Special Teams, does not vote on behalf of Boss and does not convert challenge findings into approval.

Every controlled Session and Prompt must be challenged **before** the final executable Prompt is issued.

Mandatory principles:

`Challenge First -> Prompt Second -> Execution Third.`  
`Ask until materially clear — not until everyone agrees.`  
`No repeated question without a material delta.`  
`No reset-to-zero challenge.`  
`Boss Idea != Verified Requirement != Approved Scope != Proven Business Fact.`  
`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`

---

## 2. Purpose

The challenge system exists to prevent:

- hidden assumptions;
- confirmation bias;
- repeated questioning that loses prior learning;
- stale Prompt construction;
- scope creep;
- lifecycle / Gate skipping;
- clean-room contamination;
- accounting / inventory / migration contradictions;
- SaaS / tenant / security control gaps;
- AI overreach;
- unresolved material unknowns being silently treated as facts;
- loss of challenge history between Sessions.

The objective is not to make every AI agree. The objective is to expose material uncertainty early, preserve the learning, investigate the uncertainty when needed, and present Boss with a traceable basis for decision.

---

## 3. Authority Structure

```text
                         BOSS
                  Sole Final Approver
                          |
              +-----------+-----------+
              |                       |
              v                       v
   9 VETO CHALLENGE COUNCIL     PMO / SECRETARY
       PRIMARY FUNCTION          Evidence Custodian
              |                  No approval authority
              |
       Material Unknown /
       Conflict / Blind Spot
              |
              v
    9 SPECIAL TEAM CHALLENGE
       SECONDARY FUNCTION
      Deep Investigation only
              |
              v
       Evidence / Finding
              |
              v
   9 VETO CHALLENGE COUNCIL
              |
       Gate Recommendation
              |
              v
             BOSS
```

The Council and Special Teams are independent challenge functions. Neither replaces the authorized lifecycle execution Team.

`Challenge != Execution.`  
`Challenge != Approval.`  
`Challenge != Scope Creation.`

---

## 4. 9 Veto Challenge Council — Primary Standing Function

The Council must challenge **every controlled Session and every controlled Prompt** before final issuance.

Each mandate must remain materially distinct. Duplicate questioning is prohibited unless a documented delta justifies reopening.

### Council 01 — Audit VETO / Evidence & Governance

Challenge:

- evidence sufficiency and traceability;
- contradictions;
- Gate / authority conflicts;
- unsupported completion claims;
- scope creep;
- lifecycle jump;
- missing owner / verifier / timestamp / evidence location;
- Boss ruling conflicts.

### Council 02 — TBRAC / Thailand Business Reality & User Fitness

Challenge:

- real Thai business practice;
- user/persona fitness;
- industry/company variation;
- Thailand document / operational reality;
- real-user validation;
- unsupported generalization from one company or reference ERP.

### Council 03 — EXPERT IBPV / Business Process & Design Integrity

Challenge:

- process completeness;
- state / event ownership;
- cross-module flow;
- exceptions;
- approval / segregation of duties;
- user flow;
- traceability;
- design contradictions.

Formal IBPV lifecycle authority remains unchanged; this pre-prompt role is a challenge function only unless the lifecycle has formally reached IBPV.

### Council 04 — EXPERT IDTM / Data, Identity, Reconciliation & Integrity

Challenge:

- canonical identity;
- reconciliation;
- migration integrity;
- duplicate / idempotency risk;
- data lineage;
- historical continuity;
- edge-case integrity;
- testability of material invariants.

Formal IDTM lifecycle authority remains unchanged.

### Council 05 — EXPERT IESA / ERP & SaaS System Integrity

Challenge:

- ERP-wide architecture coherence;
- tenant / company boundaries;
- cross-domain integrity;
- performance / resilience implications;
- interoperability;
- platform boundary;
- production-assurance implications.

Formal IESA lifecycle authority remains unchanged.

### Council 06 — Financial, Accounting, Tax & Statutory VETO

Challenge:

- accounting ownership and financial truth;
- posting / reversal / period / cut-off implications;
- AR/AP / tax / asset / reporting impacts;
- financial reconciliation;
- Thailand tax or statutory claims that require authoritative evidence;
- conflicts with controlled Accounting Core contracts.

This Council does not invent accounting answers where evidence or Boss-approved policy is absent.

### Council 07 — Security, Privacy & Resilience VETO

Challenge:

- access control;
- tenant isolation;
- sensitive data exposure;
- PDPA/privacy implications;
- audit/security evidence;
- backup / recovery / continuity;
- destructive / irreversible actions;
- secrets / credentials / production risk.

### Council 08 — Clean-Room, IP & Provenance VETO

Challenge:

- source-code reuse / cloning / contamination risk;
- license / provenance ambiguity;
- vendor architecture leakage into target design;
- raw customer/source evidence handling;
- source / learning / target boundary;
- evidence-chain integrity.

Mandatory invariant:

`Reference ERP behavior = Evidence / Learning Input, not target architecture by default.`

### Council 09 — AI Control, Automation & Human Oversight VETO

Challenge:

- AI being used where deterministic control is required;
- unsupported AI certainty;
- explainability / provenance;
- human override / escalation;
- AI tutor / guard / reviewer boundaries;
- autonomous action authority;
- user dependency on AI;
- failure mode if AI output is wrong.

Mandatory invariant:

`AI may assist, detect, recommend, challenge and explain; deterministic controls must not rely solely on probabilistic AI.`

---

## 5. 9 Special Team Challenge — Secondary Deep-Investigation Function

The 9 Special Teams mirror the 9 Council mandates above.

They are **not** automatically activated in full for every Prompt.

They are activated only when the Council identifies a material issue that cannot be responsibly resolved by current evidence or prior controlled learning.

Typical activation triggers:

- material Unknown;
- conflicting evidence;
- repeated defect / regression;
- accounting / inventory contradiction;
- architecture collision;
- Thailand business-reality uncertainty;
- tax / statutory uncertainty;
- SaaS / tenant / security uncertainty;
- clean-room / provenance uncertainty;
- migration / historical continuity uncertainty;
- AI-control uncertainty;
- two or more Council mandates materially disagree;
- Boss explicitly requests deep challenge.

Special Team outputs must contain:

- Challenge ID;
- exact question investigated;
- reason for activation;
- evidence inspected;
- evidence location / hash / commit where available;
- finding;
- unresolved Unknown / Conflict;
- risk / Gate impact;
- recommended disposition;
- reviewer / verifier;
- timestamp.

A Special Team may investigate deeply, but it may not self-approve lifecycle progression.

---

## 6. Independent First-Pass Rule — Anti-Groupthink

For MEDIUM / HIGH risk Prompts, and any Prompt with a material issue, each Council mandate must perform an independent first pass **before** seeing the fresh findings of the other Council mandates.

Process:

```text
Prompt Delta Pack
      |
      +--> Council 01 independent finding
      +--> Council 02 independent finding
      +--> Council 03 independent finding
      +--> Council 04 independent finding
      +--> Council 05 independent finding
      +--> Council 06 independent finding
      +--> Council 07 independent finding
      +--> Council 08 independent finding
      `--> Council 09 independent finding
                |
                v
        PMO duplicate suppression
                |
                v
        Council deliberation / consolidation
```

The purpose is to prevent nine nominal voices from becoming one copied opinion.

`9 Units != 9 Independent Thoughts unless first-pass independence is preserved.`

---

## 7. Challenge Continuity — No Reset-to-Zero

Every new Session and every new Prompt must begin by loading the **current challenge state**, not by starting the challenge from the beginning.

Mandatory prior records to read, when applicable:

- previous Prompt / Session record;
- prior Challenge Readiness Record;
- Challenge Continuity Ledger;
- Unknown / Conflict Register;
- Evidence Chain Index;
- Boss decisions / overrides;
- current frozen input commit;
- current Gate status;
- latest independent review / correction / re-verification.

The challenge process must then operate **DELTA-FIRST**.

### 7.1 Mandatory Prompt Delta Pack

Before Council review, PMO prepares only the material delta:

- what changed since the previous Prompt;
- new Boss intent;
- new evidence;
- changed Scope / authority;
- new or reopened Unknown;
- new contradiction;
- new Gate / lifecycle impact;
- unresolved carry-forward items that remain material.

### 7.2 Prohibited Repetition

A Council or Special Team must not ask the same question again merely because a new Session or Prompt has started.

A prior question may be reopened only if at least one documented Delta Trigger exists:

- new evidence contradicts prior resolution;
- baseline / Boss ruling changed;
- scope materially changed;
- upstream/downstream dependency changed;
- regression reintroduced the issue;
- prior answer was only provisional / carry-forward;
- evidence location became unavailable or untrustworthy;
- new law / regulation / authoritative evidence materially changes the question;
- the question was previously closed without adequate evidence and the deficiency is now detected.

Every reopened question must state:

`Why reopened now?`  
`What changed?`  
`Which prior Challenge ID is being reopened?`

Without a valid Delta Trigger:

`DUPLICATE QUESTION = SUPPRESS.`

---

## 8. Challenge Continuity Ledger

Every controlled Group / Domain / Workstream must maintain or reference a Challenge Continuity Ledger.

Minimum fields:

```text
Challenge_ID
Council_Mandate
Question_Fingerprint
Question
First_Raised_In
Risk
Evidence_Required
Status
Resolution_Evidence
Boss_Decision
Carry_Forward
Last_Reviewed_In
Delta_Trigger
Reopen_Reason
Affected_Scope_or_Gate
Special_Team_Activated
Notes
```

Controlled challenge statuses:

- `NEW`
- `OPEN`
- `EVIDENCE_REQUIRED`
- `CONFLICTING_EVIDENCE`
- `CARRY_FORWARD`
- `RESOLVED`
- `CLOSED_WITH_EVIDENCE`
- `REOPENED_WITH_DELTA`
- `SUPERSEDED`
- `DUPLICATE_SUPPRESSED`

Historical challenge rows must not be deleted simply because they were resolved.

---

## 9. Mandatory Challenge Sequence for Every Controlled Session / Prompt

```text
1. Load Previous Controlled Context
2. Load Challenge Continuity Ledger
3. Load Unknown / Conflict / Evidence Chain
4. Build Prompt Delta Pack
5. Classify Risk
6. 9 Veto Council Independent First Pass
7. Suppress Duplicate / Previously Resolved Questions
8. Consolidate Only New / Reopened Material Challenges
9. Activate relevant Special Team(s) only if triggered
10. Special Team Deep Investigation / Evidence
11. Return findings to 9 Veto Council
12. PMO Prompt Readiness Record
13. READY / HOLD / FAIL-FROZEN
14. Boss Decision / Exception where required
15. Final Controlled New Prompt
16. Authorized Team Execution
17. Update Challenge Ledger + Evidence Chain
```

If there is no new material question after Delta review, record:

`NO NEW MATERIAL CHALLENGE — PRIOR CONTROLLED QUESTIONS CARRIED FORWARD.`

This is an acceptable outcome and is preferable to manufacturing repetitive questions.

---

## 10. Prompt Risk Classification

Every controlled Prompt must still receive all 9 Council lenses; risk changes depth, not participation.

### LOW

- 9-Council DELTA screening;
- duplicate suppression mandatory;
- Special Team normally not activated;
- if material risk appears, escalate to MEDIUM / HIGH.

### MEDIUM

- full 9-Council DELTA challenge;
- independent first pass;
- Prompt Readiness Record mandatory;
- Special Team activated where material investigation is required.

### HIGH

Examples include Accounting/Tax, Inventory Backbone, migration write/execution, security/tenant control, sensitive data transformation, irreversible configuration, Development authorization, Production action, Boss Freeze, Release, regulatory claim.

Required:

- full 9-Council independent challenge;
- Prompt Readiness Record;
- blocking Unknown prevents execution unless Boss-controlled exception exists;
- relevant Special Team deep investigation where required;
- no lifecycle promotion until evidence is preserved.

---

## 11. Mandatory Consolidated Pre-Prompt Output

PMO must consolidate Council and Special Team inputs into:

1. `NEW MATERIAL QUESTIONS`
2. `REOPENED QUESTIONS WITH DELTA`
3. `DUPLICATE QUESTIONS SUPPRESSED`
4. `RISKS / BLIND SPOTS`
5. `EVIDENCE / VALIDATION CONCERNS`
6. `SCOPE / AUTHORITY CONCERNS`
7. `SPECIAL TEAM ACTIVATIONS`
8. `BLOCKING UNKNOWNS / CONFLICTS`
9. `CARRY-FORWARD ITEMS`
10. `NO NEW MATERIAL CHALLENGE`, where applicable.

Only material questions that can change Scope, architecture, business semantics, evidence sufficiency, risk, Gate result or execution authority should reach Boss.

---

## 12. Prompt Readiness Record — v2.0

Every controlled Prompt must have a traceable Challenge result. MEDIUM/HIGH must have a full record.

Minimum fields:

```text
PROMPT READINESS RECORD

Prompt / Session ID:
Parent Prompt / Session:
Current STATE / STEP / Domain:
Current Authorized Execution Team:
Risk Class:

Boss Intent Delta:
Changed Evidence:
Changed Scope / Authority:
Previous Challenge Ledger Ref:
Open Carry-Forward Challenges:

9 Veto Council Summary:
New Material Questions:
Reopened Questions + Delta Trigger:
Duplicate Questions Suppressed:
Special Teams Activated:
Special Team Evidence / Findings:

Resolved Before Execution:
Remaining Unknowns / Conflicts:
Execution Authority:
Prohibited Actions:
Evidence Required:
Acceptance Criteria:
Gate Impact:

Readiness Status:
READY / HOLD / FAIL-FROZEN

Boss Exception / Override:
NONE or exact evidence reference
```

A Challenge / Readiness PASS is governance evidence only. It creates no execution progress credit.

---

## 13. Readiness Rules

### READY

Only when:

- intent delta is clear;
- prior learning has been loaded;
- duplicate questions are suppressed;
- no unresolved blocking conflict remains;
- Scope / authority is controlled;
- evidence plan is inspectable;
- Council has no unresolved blocking Veto;
- required Special Team findings are available or intentionally deferred without blocking the current authorized scope.

### HOLD

Use when:

- material evidence is missing;
- a new/reopened question can change architecture, accounting, inventory, security, migration, Scope or compliance outcome;
- a required Special Team investigation is incomplete;
- authority / linkage is unclear;
- challenge history cannot be reconstructed.

### FAIL / FROZEN

Use when:

- mandatory Gate would be skipped;
- Prompt contradicts Boss-approved baseline without controlled change;
- clean-room / tenant / financial / security / evidence-chain control is materially violated;
- lifecycle promotion occurs without authority;
- challenge history was erased or manipulated to hide a material finding.

---

## 14. No Answer-Key / No Confirmation Bias

Council and Special Teams must challenge using:

`Question -> Risk -> Evidence Gap -> Investigation Need`

not:

`Expected Answer -> Required Conclusion`.

They must not:

- ask questions only to validate Boss's preferred answer;
- force the authorized Team to reach a predetermined conclusion;
- treat AI consensus as approval;
- convert Boss experience into verified Thailand-wide truth without evidence;
- design the execution Team's answer for it.

The authorized Team must remain free to discover evidence that contradicts Boss, AI, vendor or reviewer assumptions.

---

## 15. Scope Protection

Challenge may discover a Scope Gap; it cannot silently convert that Gap into Scope.

```text
Challenge
-> Gap
-> Evidence
-> Baseline Check
-> IN-SCOPE: Controlled Action
   OR
-> OUT-OF-SCOPE: Change Request / Boss Decision
```

`Increasing rigor of scope verification != increasing scope.`

---

## 16. Boss Authority / No Majority Vote

Neither 9 Veto Council nor 9 Special Teams decide by majority vote.

They challenge, investigate, provide evidence and recommend.

Boss remains Sole Final Approver.

A Boss Override of a material Veto must preserve:

- Challenge ID;
- original finding;
- Boss decision;
- rationale;
- known risk;
- evidence considered;
- compensating control;
- owner for later closure where applicable;
- timestamp;
- affected Prompt / Gate.

The original Veto finding must never be erased.

---

## 17. PMO / Secretary Role

PMO / Secretary is responsible for:

- retrieving prior controlled context;
- preparing the Delta Pack;
- enforcing Question Fingerprint / duplicate suppression;
- maintaining Challenge Continuity Ledger;
- coordinating Council / Special Team evidence flow;
- preserving independent first-pass findings;
- consolidating material questions without changing their meaning;
- maintaining Prompt Readiness Record;
- maintaining Evidence Chain and Session archive;
- recording Jira / GitHub linkage;
- raising Red Flags to Boss.

PMO / Secretary must not:

- decide a Veto by itself;
- suppress a unique material challenge merely because it is inconvenient;
- reopen closed questions without a Delta Trigger;
- manufacture new questions to make the process appear rigorous;
- convert a Challenge finding into Scope or approval;
- replace Boss authority.

---

## 18. Formal Lifecycle Boundaries Remain Unchanged

This standard does not itself authorize:

- Team B;
- Team C / Development;
- Team D;
- Production;
- Release;
- deployment;
- schema / code changes;
- statutory claims;
- Scope expansion.

Formal IBPV / IDTM / IESA stages remain at their approved lifecycle positions.

Pre-Prompt participation never counts as formal lifecycle execution credit.

---

## 19. Evidence Preservation

For every controlled Session / Prompt, preserve at minimum:

- Prompt / Session ID;
- Parent Prompt / Session;
- Delta Pack or concise delta summary;
- 9-Council challenge result;
- Special Team activation and result where applicable;
- Challenge Ledger update;
- Prompt Readiness status;
- final Prompt;
- immutable GitHub commit / evidence reference where applicable;
- Jira linkage where applicable;
- Boss decision / override where applicable.

Hard controls:

`No Challenge Evidence = No Controlled Prompt Execution.`  
`No Evidence Preservation = No Lifecycle Promotion.`  
`No Evidence Chain Seal = No Team C.`

---

## 20. Operating Standard / L999.999

For every controlled Session and every controlled Prompt:

```text
PRIOR LEARNING
    ↓
LOAD CHALLENGE LEDGER
    ↓
DELTA PACK
    ↓
9 VETO COUNCIL — INDEPENDENT FIRST PASS
    ↓
DUPLICATE SUPPRESSION
    ↓
NEW / REOPENED MATERIAL CHALLENGES ONLY
    ↓
9 SPECIAL TEAM CHALLENGE — IF TRIGGERED
    ↓
EVIDENCE / FINDINGS
    ↓
9 VETO COUNCIL DISPOSITION
    ↓
PMO READINESS RECORD
    ↓
READY / HOLD / FAIL-FROZEN
    ↓
BOSS DECISION WHERE REQUIRED
    ↓
FINAL NEW PROMPT
    ↓
AUTHORIZED EXECUTION
    ↓
UPDATE LEARNING / CHALLENGE LEDGER / EVIDENCE CHAIN
```

Final mandatory principles:

`Challenge First -> Prompt Second -> Execution Third.`  
`No reset-to-zero challenge.`  
`No repeated question without a material delta.`  
`Closed-with-evidence questions stay closed unless a Delta Trigger exists.`  
`New evidence may reopen old questions — but reopening must be traceable.`  
`Independent First Pass before Council convergence.`  
`Special Team investigates; Council challenges; PMO preserves; Boss decides.`  
`No Answer Key Before Research.`  
`No Cross-Team Execution.`  
`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`
