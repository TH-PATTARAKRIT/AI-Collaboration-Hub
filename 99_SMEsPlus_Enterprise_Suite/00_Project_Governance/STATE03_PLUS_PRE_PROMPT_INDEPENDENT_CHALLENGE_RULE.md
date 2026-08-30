# STATE03+ Pre-Prompt Independent Challenge Rule

Document ID: SMEPLUS-26-08-30-PRE-PROMPT-CHALLENGE-001
Version: v1.0
Status: BOSS APPROVED / EFFECTIVE
Effective Date: 2026-08-30
Project: SMEsPlus ENTERPRISE SUITE
Scope: Every controlled New Prompt / Carry-Forward Prompt / Corrective Prompt / Deep Research Prompt from STATE03 onward
Final Approval Authority: Boss

## 1. Boss Ruling

From STATE03 onward, every controlled prompt shall preserve strict Team responsibility boundaries while using independent challenge functions before a New Prompt is finalized.

The purpose of the independent challenge is to reduce avoidable rework by raising questions, risks, blind spots, evidence gaps and areas that may deserve consideration before execution begins.

The purpose is NOT to provide an answer key, prescribe the expected research result, predetermine what the execution Team must discover, or force one Team to work according to another Team's later-stage test or assurance plan.

## 2. Team Boundary Rule — No Cross-Team Execution

Each Team owns and executes only its approved lifecycle scope.

Examples:

- Team A performs source learning / evidence extraction within Team A scope.
- Team B performs independent canonical design within Team B scope.
- Team C performs engineering / implementation within Team C scope after authorization.
- Team D performs independent QA / clean-room / compliance work within Team D scope after the lifecycle reaches Team D.

A Team that is not the current authorized execution Team must not enter the current Team's execution work, co-author its findings, prescribe its conclusion, or impose its downstream test/design method on the current Team.

`No Cross-Team Execution.`

`No Downstream Team may control Upstream Research.`

## 3. Current Team Autonomy

The currently authorized Team has full execution authority inside its approved scope, subject only to project governance, evidence rules, clean-room rules, approved Gates and Boss rulings.

Independent challenge functions may question and recommend; they do not take over execution.

The execution Team must remain free to discover evidence that contradicts expectations or that was not anticipated by any reviewer.

## 4. Mandatory Pre-Prompt Challenge Functions

Before creating/finalizing every controlled prompt from STATE03 onward, obtain at least the following independent challenge/recommendation inputs:

### 4.1 Audit VETO — Evidence / Governance Challenge

Purpose:

- challenge evidence sufficiency;
- challenge unsupported assumptions;
- identify governance/Gate conflicts;
- identify material unknowns, contradictions and missing evidence;
- ask questions that should be resolved or explicitly carried as Unknown.

Audit VETO must NOT prescribe the business answer or force the execution Team to produce a predetermined finding.

### 4.2 TBRAC — Thailand Reality Challenge

Purpose:

- challenge whether Thailand business reality has been overlooked;
- challenge textbook/vendor assumptions against real Thai operating practice;
- raise user/persona, document, compliance, industry-variation and real-user-validation questions where materially relevant;
- identify areas where authoritative Thai evidence or real-user validation may be required.

TBRAC must NOT provide an answer key for the execution Team or force the Team to conclude that a particular Thai practice is correct without evidence.

## 5. Mandatory Expert Recommendations Before Prompt Finalization

Obtain recommendations from at least these expert units before a controlled prompt is finalized:

### 5.1 EXPERT IBPV

IBPV may raise questions and recommendations about potential business-process, cross-module, state/event, ownership, exception, approval/SoD and traceability blind spots.

At pre-prompt stage IBPV is advisory only unless the lifecycle has formally reached IBPV Verification.

IBPV must NOT design the answer for Team A/Team B, rewrite the current Team's work, or prescribe a future verification checklist as the current Team's required conclusion.

### 5.2 EXPERT IDTM

IDTM may raise questions and recommendations about possible blind spots that could later create deep-test difficulty, including integrity, concurrency, edge-case, tenant/security, integration/idempotency, performance, recovery, audit/SoD or cross-domain concerns.

At pre-prompt stage IDTM is advisory only unless the lifecycle has formally reached IDTM Deep Test execution.

IDTM must NOT turn its future 10-Dimension Deep Test Matrix into an answer key for upstream research. It must not require the current Team to study only what IDTM later intends to test.

### 5.3 EXPERT IESA

IESA may raise questions and recommendations about potential ERP/SaaS system-level implications, cross-domain integrity, tenancy, multi-company, security, performance, resilience, operational coherence and future production-assurance concerns.

At pre-prompt stage IESA is advisory only unless the lifecycle has formally reached IESA Pre-Assurance or Final Assurance.

IESA must NOT prescribe target architecture, predetermined findings or production-readiness conclusions to an upstream Team.

## 6. Team D Clarification

Team D is NOT part of the mandatory pre-prompt advisory stack for another Team's work.

Team D enters only when the approved lifecycle reaches Team D, or when Team D itself is the current authorized execution Team.

Therefore, for a Team A Deep Research prompt, Team D shall not:

- participate in Team A research execution;
- define Team A research scope;
- prescribe what Team A must discover;
- impose Team D's future QA checklist on Team A;
- co-author Team A evidence or findings.

This protects both Team A independence and Team D independence.

## 7. No Answer-Key Contamination Rule

Independent challenge functions must operate using a `Question / Risk / Blind Spot / Evidence Gap` model, not an `Expected Answer / Mandatory Conclusion` model.

Preferred form:

```text
Question:
What happens if the transaction is partially completed and then cancelled?

Risk:
Cross-module state may become inconsistent.

Evidence concern:
Source code observation and database state must be reconciled.

Recommendation:
Consider whether this scenario is material to the current scope.
```

Prohibited form:

```text
Expected Answer:
The current Team must conclude that state X must transition to Y and must use rule Z.
```

The independent units may recommend what deserves investigation; they may not decide the evidence result in advance.

## 8. Mandatory Pre-Prompt Output

Before a New Prompt is finalized, consolidate the independent input into four categories:

1. `QUESTIONS TO CONSIDER`
2. `RISKS / BLIND SPOTS`
3. `EVIDENCE / VALIDATION CONCERNS`
4. `OPTIONAL SCOPE-SAFE RECOMMENDATIONS`

Each item must identify its originating function: Audit VETO, TBRAC, IBPV, IDTM or IESA.

Recommendations must remain within the current Team's approved scope. Anything outside current scope is carry-forward only and must not silently expand the Prompt.

## 9. Prompt Construction Rule

After independent challenge, PMO/ChatGPT may strengthen the New Prompt by adding:

- questions that reduce foreseeable evidence gaps;
- explicit Unknown / Conflict handling;
- clean-room and evidence controls;
- scope-safe exception areas worth examining;
- carry-forward warnings for future Teams.

PMO/ChatGPT must NOT convert reviewer questions into predetermined answers or allow downstream units to control the current Team's methodology.

The current Team's Prompt remains an execution instruction for that Team only.

## 10. Formal Lifecycle Authority Remains Unchanged

This pre-prompt rule does not move any Team or Expert Unit from its approved lifecycle position.

- Team A remains Team A.
- Team B remains Team B.
- Team C remains Team C.
- Team D remains Team D.
- IBPV Formal Verification remains at the approved Pre-Development position.
- IDTM Formal Deep Test remains at the approved Deep Test position.
- IESA Formal Pre-Assurance / Final Assurance remains at the approved assurance positions.

Early recommendations do not count as formal Gate execution or Gate completion.

## 11. Operating Principle

`Independent experts challenge the questions; the authorized Team discovers the answers.`

`No Answer Key Before Research.`

`No Cross-Team Execution.`

`No Downstream Control of Upstream Research.`

`No Evidence = No Progress.`

`Never Skip Gate.`

`Boss = Sole Final Approver.`
