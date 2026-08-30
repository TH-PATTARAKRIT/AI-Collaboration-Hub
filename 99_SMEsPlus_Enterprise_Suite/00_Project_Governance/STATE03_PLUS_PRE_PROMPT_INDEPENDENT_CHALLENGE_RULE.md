# SMEsPlus NEW PROMPT Governance Standard — STATE03+ Pre-Prompt Independent Challenge Rule

Document ID: SMEPLUS-26-08-30-PRE-PROMPT-CHALLENGE-001
Version: v1.1
Status: BOSS APPROVED / EFFECTIVE
Effective Date: 2026-08-30
Project: SMEsPlus ENTERPRISE SUITE
Scope: Every controlled New Prompt / New Session Prompt / Carry-Forward Prompt / Corrective Prompt / Deep Research Prompt / Execution Prompt from STATE03 onward
Final Approval Authority: Boss
Supersedes: v1.0 of this document

## 1. Boss Ruling

Boss approves this rule as the mandatory **NEW PROMPT Governance Standard** for SMEsPlus from STATE03 onward.

Every controlled New Prompt shall be challenged before execution so that the execution Team receives a prompt whose intent, scope, authority, material unknowns, evidence expectations and acceptance conditions are sufficiently clear.

The five mandatory independent challenge functions are:

1. Audit VETO — Evidence / Governance Challenge
2. TBRAC — Thailand Business Reality Challenge
3. EXPERT IBPV — Business Process & Design Challenge
4. EXPERT IDTM — Deep Test / Integrity Challenge
5. EXPERT IESA — ERP & SaaS System-Level Challenge

The purpose is to reduce avoidable rework, hidden assumptions, confirmation bias, scope creep and downstream control failures.

The purpose is NOT to obtain a predetermined answer, provide an answer key, force agreement with Boss, prescribe the expected research result, or allow downstream reviewers to control the current execution Team.

Mandatory interpretation:

`Ask until materially clear — not until everyone agrees.`

`Boss Idea != Verified Requirement != Approved Scope != Proven Business Fact.`

`Independent experts challenge the questions; the authorized Team discovers the answers.`

## 2. Control Objective

The Pre-Prompt Challenge Gate must answer, to the extent applicable:

- What exactly is Boss asking to accomplish?
- Why is the work being requested?
- What is explicitly in scope and out of scope?
- Which facts are verified, unverified, assumed, conflicting or unknown?
- What authority does the execution Team have?
- What actions are prohibited?
- What evidence is required?
- What conditions constitute acceptance, HOLD or FAIL/FROZEN?
- Which material risks or blind spots should the execution Team investigate without prescribing the answer?
- Does the Prompt accidentally expand Scope, skip a Gate, contaminate clean-room boundaries, or authorize Development/Production without authority?

The challenge process shall eliminate material ambiguity where reasonably possible, but must preserve legitimate Unknowns when evidence does not yet exist.

## 3. Team Boundary Rule — No Cross-Team Execution

Each Team owns and executes only its approved lifecycle scope.

Examples:

- Team A performs source learning / evidence extraction within Team A scope.
- Team B performs independent canonical design within Team B scope.
- Team C performs engineering / implementation within Team C scope after authorization.
- Team D performs independent QA / clean-room / compliance work within Team D scope after the lifecycle reaches Team D.

A Team that is not the current authorized execution Team must not enter the current Team's execution work, co-author its findings, prescribe its conclusion, or impose its downstream test/design method on the current Team.

`No Cross-Team Execution.`

`No Downstream Team may control Upstream Research.`

## 4. Current Team Autonomy

The currently authorized Team has full execution authority inside its approved scope, subject only to project governance, evidence rules, clean-room rules, approved Gates and Boss rulings.

Independent challenge functions may question and recommend; they do not take over execution.

The execution Team must remain free to discover evidence that contradicts expectations, Boss assumptions, AI assumptions, vendor assumptions or reviewer assumptions.

No reviewer may convert a hypothesis into a required conclusion merely because it appears plausible.

## 5. Mandatory Five-Unit Pre-Prompt Challenge

Before finalizing every controlled New Prompt, all five challenge functions shall perform a pre-prompt review. Review depth may scale with Prompt risk, but participation of the five challenge lenses remains mandatory for controlled New Prompts.

### 5.1 Audit VETO — Evidence / Governance Challenge

Purpose:

- challenge evidence sufficiency;
- challenge unsupported assumptions;
- identify governance/Gate conflicts;
- identify material unknowns, contradictions and missing evidence;
- identify accidental Scope expansion;
- identify unauthorized Build / Production / write actions;
- ask questions that should be resolved or explicitly carried as Unknown.

Audit VETO must NOT prescribe the business answer or force the execution Team to produce a predetermined finding.

### 5.2 TBRAC — Thailand Business Reality Challenge

Purpose:

- challenge whether Thailand business reality has been overlooked;
- challenge textbook/vendor assumptions against real Thai operating practice;
- raise user/persona, document, compliance, industry-variation and real-user-validation questions where materially relevant;
- identify areas where authoritative Thai evidence or real-user validation may be required;
- identify whether a Founder/Boss observation should remain a hypothesis pending evidence.

TBRAC must NOT provide an answer key for the execution Team or force the Team to conclude that a particular Thai practice is correct without evidence.

### 5.3 EXPERT IBPV — Business Process & Design Challenge

IBPV may raise questions and recommendations about potential business-process, cross-module, state/event, ownership, exception, approval/SoD, user-flow and traceability blind spots.

At pre-prompt stage IBPV is advisory only unless the lifecycle has formally reached IBPV Verification.

IBPV must NOT design the answer for Team A/Team B, rewrite the current Team's work, or prescribe a future verification checklist as the current Team's required conclusion.

### 5.4 EXPERT IDTM — Deep Test / Integrity Challenge

IDTM may raise questions and recommendations about possible blind spots that could later create deep-test difficulty, including integrity, concurrency, edge-case, tenant/security, integration/idempotency, performance, recovery, audit/SoD or cross-domain concerns.

At pre-prompt stage IDTM is advisory only unless the lifecycle has formally reached IDTM Deep Test execution.

IDTM must NOT turn its future 10-Dimension Deep Test Matrix into an answer key for upstream research. It must not require the current Team to study only what IDTM later intends to test.

### 5.5 EXPERT IESA — ERP & SaaS System-Level Challenge

IESA may raise questions and recommendations about potential ERP/SaaS system-level implications, cross-domain integrity, tenancy, multi-company, security, performance, resilience, operational coherence, migration and future production-assurance concerns.

At pre-prompt stage IESA is advisory only unless the lifecycle has formally reached IESA Pre-Assurance or Final Assurance.

IESA must NOT prescribe target architecture, predetermined findings or production-readiness conclusions to an upstream Team.

## 6. Prompt Risk Classification

Every controlled New Prompt shall be classified before execution.

### LOW RISK

Examples: read-only lookup, factual extraction, formatting, controlled summary or analysis that cannot materially alter Scope, architecture, data, configuration or Gate status.

Required treatment:

- five-unit lightweight screening;
- no unnecessary interrogation if no material issue is found;
- any discovered material risk automatically escalates the Prompt to MEDIUM or HIGH.

### MEDIUM RISK

Examples: design proposal, mapping, architecture option, business rule interpretation, migration design, controlled configuration proposal, evidence-based recommendation.

Required treatment:

- full five-unit Pre-Prompt Challenge;
- consolidated material questions;
- Prompt Readiness Record;
- unresolved material items explicitly carried as Unknown / HOLD where applicable.

### HIGH RISK

Examples: Scope change, Accounting/Tax rule, migration write/execution, security/tenant control, sensitive data transformation, irreversible configuration, Development authorization, Production action, Boss Freeze, regulatory claim or Release decision.

Required treatment:

- full five-unit Pre-Prompt Challenge;
- mandatory Prompt Readiness Record;
- unresolved blocking issue prevents Prompt execution;
- Boss-controlled exception required for any explicit override of a blocking governance/risk finding.

Risk classification changes review depth; it does not authorize work outside the approved lifecycle or Scope.

## 7. No Answer-Key / Confirmation-Bias Rule

Independent challenge functions must operate using a `Question / Risk / Blind Spot / Evidence Gap` model, not an `Expected Answer / Mandatory Conclusion` model.

Preferred form:

```text
Question:
What happens if the transaction is partially completed and then cancelled?

Risk:
Cross-module state may become inconsistent.

Evidence concern:
Source observation and target business semantics must be reconciled.

Recommendation:
Consider whether this scenario is material to the current approved scope.
```

Prohibited form:

```text
Expected Answer:
The current Team must conclude that state X must transition to Y and must use rule Z.
```

Also prohibited:

- asking questions only to validate Boss's preferred conclusion;
- converting Boss experience into verified Thailand-wide business fact without evidence;
- converting AI consensus into approval;
- treating majority agreement among the five challenge functions as a Boss decision.

## 8. Scope Protection Rule

Pre-Prompt Challenge may discover a Scope Gap, but it may not silently expand Scope.

Required handling:

```text
Potential Missing Capability
→ Evidence / Business Need
→ Baseline Check
→ IN-SCOPE: route to controlled execution
   OR
→ OUT-OF-SCOPE: Gap / Change Request / Boss Decision
```

Anything outside the current Team's approved scope is carry-forward only unless separately authorized.

`Stronger Scope Verification != Automatic Scope Expansion.`

## 9. Mandatory Consolidated Pre-Prompt Output

Before a controlled New Prompt is finalized, PMO/ChatGPT shall consolidate the five independent inputs into these categories:

1. `QUESTIONS TO CONSIDER`
2. `RISKS / BLIND SPOTS`
3. `EVIDENCE / VALIDATION CONCERNS`
4. `SCOPE / AUTHORITY CONCERNS`
5. `OPTIONAL SCOPE-SAFE RECOMMENDATIONS`
6. `BLOCKING UNKNOWNS / CONFLICTS`

Each material item must identify its originating challenge function.

PMO must remove duplicate questions and present Boss only with questions that can materially change Scope, architecture, business semantics, evidence sufficiency, risk or execution authority.

The purpose is not to create an AI committee meeting for every trivial detail.

## 10. Prompt Readiness Record

Every MEDIUM/HIGH controlled New Prompt, and every LOW Prompt escalated due to material findings, shall have a concise Prompt Readiness Record before execution.

Minimum fields:

```text
PROMPT READINESS RECORD

Prompt / Session ID:
Current STATE / STEP / Domain:
Current Authorized Execution Team:
Risk Class: LOW / MEDIUM / HIGH

Boss Intent:
Expected Outcome:
In Scope:
Out of Scope:
Known / Verified Facts:
Unverified Assumptions:
Critical Unknowns / Conflicts:
Five-Unit Challenge Summary:
Resolved Before Execution:
Carry-Forward Unknowns:
Execution Authority:
Prohibited Actions:
Evidence Required:
Acceptance Criteria:
Gate Impact:

Readiness Status:
READY / HOLD / FAIL-FROZEN

Boss Exception / Override:
NONE or explicit evidence reference
```

A Prompt Readiness Record is governance evidence. It is not execution evidence and creates no progress credit by itself.

## 11. Readiness Decision Rules

### READY

Use only when:

- Boss intent is sufficiently clear;
- Scope and authority are controlled;
- no unresolved blocking Unknown remains;
- required pre-execution evidence is available or explicitly planned within authorized scope;
- the five challenge functions have no unresolved blocking governance conflict.

### HOLD

Use when:

- material information/evidence is incomplete;
- a question can change Scope, architecture, accounting semantics, security, compliance or migration outcome;
- linkage/authority is unclear;
- a required reviewer/evidence source is unavailable.

### FAIL / FROZEN

Use when:

- the Prompt contradicts an approved Boss ruling or frozen baseline;
- execution would skip a mandatory Gate;
- execution would create unacceptable clean-room, tenant, financial, security or compliance risk;
- required authority is absent;
- a material contradiction cannot be safely carried as an Unknown.

## 12. Boss Authority / No Majority Vote

The five challenge functions do not govern by majority vote.

They challenge, provide evidence, identify uncertainty and recommend status.

Boss remains Sole Final Approver for business decisions, controlled exceptions, Scope decisions, Gate approvals, Release and Production authority.

If Boss explicitly overrides a material recommendation, preserve at minimum:

- Boss Override Decision;
- reason/rationale;
- known risk;
- evidence considered;
- compensating control if applicable;
- timestamp;
- affected Gate / Prompt.

An override does not permit an AI to erase the original challenge finding.

## 13. Team D Clarification

Team D is NOT part of the five mandatory pre-prompt advisory functions for another Team's work.

Team D enters only when the approved lifecycle reaches Team D, or when Team D itself is the current authorized execution Team.

Therefore, for a Team A or Team B Prompt, Team D shall not:

- participate in the upstream Team's execution;
- define upstream research/design scope;
- prescribe what the upstream Team must discover;
- impose Team D's future QA checklist as an upstream answer key;
- co-author upstream evidence or findings.

This protects both upstream autonomy and Team D independence.

## 14. Prompt Construction Rule

After independent challenge, PMO/ChatGPT may strengthen the New Prompt by adding:

- questions that reduce foreseeable evidence gaps;
- explicit Unknown / Conflict handling;
- clean-room and evidence controls;
- scope-safe exception areas worth examining;
- applicable Thailand reality checks;
- SaaS/tenant/security implications;
- measurable acceptance criteria where evidence permits;
- carry-forward warnings for future Teams.

PMO/ChatGPT must NOT convert reviewer questions into predetermined answers or allow downstream units to control the current Team's methodology.

The current Team's Prompt remains an execution instruction for that Team only.

## 15. Evidence / Repository Rule

For controlled MEDIUM/HIGH New Prompts, preserve the Prompt Readiness Record with the Prompt/session evidence in the approved GitHub project structure.

Where a Jira execution item exists, record the relevant Prompt ID, GitHub evidence path/commit and current readiness status in Jira.

Required governance principle:

`No Evidence = No Progress.`

Pre-Prompt review approval alone does not count as Team execution progress, STATE progress, STEP progress, Development authorization or Production authorization.

## 16. Formal Lifecycle Authority Remains Unchanged

This Pre-Prompt Governance Standard does not move any Team or Expert Unit from its approved lifecycle position.

- Team A remains Team A.
- Team B remains Team B.
- Team C remains Team C.
- Team D remains Team D.
- IBPV Formal Verification remains at the approved Pre-Development position.
- IDTM Formal Deep Test remains at the approved Deep Test position.
- IESA Formal Pre-Assurance / Final Assurance remains at the approved assurance positions.

Early recommendations do not count as formal Gate execution or Gate completion.

No Development, Release or Production authority is granted by this document.

## 17. Operating Standard

For every controlled New Prompt from STATE03 onward:

```text
Boss Intent
→ Prompt Risk Classification
→ Five-Unit Independent Challenge
→ Consolidated Material Questions / Risks / Unknowns
→ Clarification / Evidence Check
→ Prompt Readiness Record where required
→ READY / HOLD / FAIL-FROZEN
→ Boss-controlled decision where required
→ Final Controlled Prompt
→ Authorized Execution Team executes only within approved scope
```

Mandatory principles:

`Ask until materially clear — not until everyone agrees.`

`No Answer Key Before Research.`

`No Cross-Team Execution.`

`No Downstream Control of Upstream Research.`

`Stronger Scope Verification != Automatic Scope Expansion.`

`No Evidence = No Progress.`

`Never Skip Gate.`

`Boss = Sole Final Approver.`
