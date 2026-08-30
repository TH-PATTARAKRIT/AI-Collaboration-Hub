# PROJECT_CONSTITUTION.md

Version: v1.3
Status: Approved
Owner: SMEsPlus PMO / Repository Owner
Approved By: Boss
Original Effective Date: 2026-07-05
Current Revision Effective Date: 2026-08-30
Scope: `99_SMEsPlus_Enterprise_Suite/`

## Purpose

This document is the project constitution for SMEsPlus Enterprise Suite. It defines the operating principles, authority model, repository control model, evidence rule and gate-control discipline for all human and AI contributors.

## Core Principles

1. Repository is the Single Source of Truth.
2. No Evidence = No Progress.
3. No Gate Approval = No Move Forward.
4. AI may draft, analyze, review and support execution, but Boss holds final approval authority.
5. Build and Production are controlled gates, not automatic outcomes of documentation completion.
6. Learning, architecture, functional design, software design, testing and deployment must remain traceable.
7. Independent reviewers must not review their own work.
8. Critical unresolved flow/design gaps block Development until Boss decides otherwise.
9. Critical unresolved system-level ERP/SaaS readiness gaps block Release/Production until Boss decides otherwise.
10. Module-level PASS does not by itself prove whole-system Production readiness.
11. Every controlled Test Case must define its Tolerance before execution; the ordinary project ceiling is `0.001%`, with stricter/zero tolerance required where defined.
12. `0 BUG FOUND` is not evidence of zero defects and automatically triggers Test Adequacy Verification before Production-readiness evidence is trusted.
13. Critical integrity, financial and tenant-isolation failures may be designated `Tolerance = 0` and must not be averaged into a low overall defect percentage.

## Authority Model

| Role | Authority |
|---|---|
| Boss | Sole Final Approver and final business decision authority |
| Repository Owner | Repository structure and standards control |
| Liza / ChatGPT | Architecture governance, PMO control, cross-AI review |
| Claude AI | Repository review, evidence matching, SaaS alignment, gap analysis |
| Functional Specification AI | Business functional specification draft |
| Team A | Source learning, business evidence extraction, neutral observation and evidence preparation |
| Team B | Independent SMEsPlus canonical domain and process design |
| Figma / UX Team | UX, screen, interaction and developer-handoff design based on controlled Team B business/process inputs; must not guess Business Logic |
| EXPERT IBPV | Independent Business Process & Design Verification; reports directly to Boss only; no Team/Board/PMO may alter its independent findings |
| Team C / Claude Code | Engineering / implementation only after Pre-Development Design Gate and Boss approval |
| Team D | Independent QA / clean-room / compliance audit after implementation evidence exists |
| EXPERT IDTM | Independent 100% AI Deep Test Matrix & System Verification; reports directly to Boss only; produces independent deep-test and Test-Adequacy evidence |
| EXPERT IESA | Independent ERP & SaaS Intelligence Assurance after implementation, Team D and IDTM evidence; reports directly to Boss only; no Team/Board/PMO may alter its independent findings |

## EXPERT IBPV — Independent Business Process & Design Verification

Effective 2026-08-30, Boss formally appoints **EXPERT IBPV — Independent Business Process & Design Verification Team** as an independent project unit.

### Independence

1. EXPERT IBPV reports directly to Boss only.
2. EXPERT IBPV is organizationally and functionally independent from Team A, Team B, Figma/UX, Team C, Team D, EXPERT IDTM, EXPERT IESA, all Boards and PMO review influence.
3. PMO may register, route and preserve IBPV evidence, but may not direct, rewrite, suppress or override an IBPV finding.
4. EXPERT IBPV must not verify work it authored itself.
5. EXPERT IBPV must not implement Production Code or redesign Team B/Figma work on their behalf.
6. Any conflict between Team B/Figma and EXPERT IBPV must be recorded in a Design Conflict Register and escalated directly to Boss.

### Mandatory Position in Delivery Flow

```text
Team A — Evidence / Source Understanding
→ Evidence Gate
→ Team B — Independent Canonical Domain Design
→ Figma / UX — UX, Screen and Interaction Design
→ EXPERT IBPV — Independent Business Process & Design Verification
→ Pre-Development Design Gate
→ Boss Decision
→ Team C — Engineering / Development
```

EXPERT IBPV verification is mandatory before Team C Development for each controlled domain/workstream unless Boss explicitly issues a written exception.

### Verification Scope

EXPERT IBPV must independently verify, as applicable:

- End-to-End Business Flow
- Cross-Module / Cross-Domain Flow
- State Transition and Event Flow
- Data Flow and Data Ownership
- Approval / Permission / Segregation-of-Duties Control Flow
- Exception, Reject, Cancel, Partial, Retry, Reversal and Correction Flow
- Accounting / Tax / WHT / Compliance Impact Flow
- Multi-company and Multi-currency Flow
- Integration and Failure-Recovery Flow
- Figma Screen/Interaction Flow against Team B business rules
- Traceability from approved business evidence to Team B/Figma design
- Open assumptions, unknowns, conflicts and evidence gaps

### Allowed IBPV Status

EXPERT IBPV may issue only evidence-based verification findings such as:

- VERIFIED
- VERIFIED WITH CONDITIONS
- GAP FOUND
- CONFLICT FOUND
- EVIDENCE MISSING
- REWORK REQUIRED
- NOT READY FOR DEVELOPMENT
- READY FOR BOSS DECISION

EXPERT IBPV may not declare `FINAL APPROVED`, `BOSS APPROVED`, `PRODUCTION READY`, or `RELEASE APPROVED`.

## EXPERT IDTM — Independent Deep Test Matrix & System Verification

Effective 2026-08-30, Boss formally appoints **EXPERT IDTM — Independent Deep Test Matrix & System Verification Team** as an independent project verification unit.

### Purpose

IDTM independently executes the approved 10-Dimension Deep Test Matrix using 100% AI execution and produces evidence that attempts to expose defects under normal, boundary, adversarial, concurrent, failure, recovery and cross-domain conditions.

IDTM is an evidence producer and deep-system verifier. It does not replace IESA system-level assurance and does not replace Boss approval.

### Independence

1. EXPERT IDTM reports directly to Boss only.
2. EXPERT IDTM is independent from Team A, Team B, Figma/UX, EXPERT IBPV, Team C, Team D, EXPERT IESA, Boards, PMO and delivery owners.
3. PMO may register, preserve and route IDTM evidence but may not direct, rewrite, suppress or override an IDTM finding.
4. IDTM must not repair the Production Code it independently tests.
5. Team C performs remediation; Team D performs regression/compliance recheck; IDTM performs independent retest.
6. The code-authoring AI must not be the sole AI that creates, executes and judges its own acceptance evidence.
7. Material disagreements between delivery teams and IDTM must be recorded and escalated directly to Boss.

### 10 Mandatory Test Dimensions

1. Mathematical & Accounting Invariants
2. Inventory Conservation & State
3. Concurrency & Race Conditions
4. Edge Cases & Lifecycle Traversal
5. Multi-Tenant & Security Isolation
6. Integration & Idempotency
7. Performance & Scalability
8. Resilience / Chaos / Recovery
9. Audit / Permission / Segregation-of-Duties Integrity
10. Cross-Domain ERP Integrity

### 100% AI Execution Rule

For each frozen Approved Matrix version:

- Approved Dimension Coverage = 100%
- Approved Test Case Execution = 100%
- Critical Test Case Execution = 100%
- Executed Test Case Evidence Capture = 100%
- Failed/Remediated Case Independent Retest = 100%

100% matrix execution does not mean 100% bug-free guarantee and does not prove every theoretically possible combination has been tested.

### Test Tolerance Rule

Every controlled Test Case must declare its Tolerance before execution:

```text
0% <= T_case <= 0.001%
```

A stricter target is allowed. A value above `0.001%` is prohibited unless Boss explicitly rules otherwise.

Critical categories defined by the approved Test Tolerance Policy have `Tolerance = 0`, including tenant leakage, Critical privilege escalation, posted Debit/Credit imbalance, silent financial corruption, unauthorized/duplicate financial posting, irrecoverable controlled-data loss, Critical inventory-integrity breach and defined exact statutory/security invariants.

The denominator/metric must be frozen before execution. A percentage without a denominator is not valid evidence.

### Zero-Defect Challenge Rule

If approved matrix execution reaches 100% and `BUG FOUND = 0`, IDTM must execute Test Adequacy Verification before readiness evidence can progress.

Applicable techniques include:

- Mutation Testing
- Blind Seeded Defect Testing
- Property-Based Testing
- Fuzzing / Adversarial Input
- State-Space Traversal
- Cross-Domain Reconciliation
- Concurrency Amplification
- Chaos / Fault Injection
- Independent AI Test Generation and Oracle Review

Critical injected faults have `Miss Tolerance = 0%`.

Non-critical injected-fault miss rate target must not exceed `0.001%` with a pre-frozen denominator. An escaped seeded/mutation defect is a `TEST ADEQUACY GAP`, not a PASS.

### Mandatory Position in Delivery Flow

```text
Team C — Engineering / Development
→ Team D — Independent QA / Clean-room / Compliance Audit
→ EXPERT IESA — Pre-Assurance Challenge (No Final Production Verdict)
→ EXPERT IDTM — 100% AI Deep Test Matrix Execution
→ Independent Deep Test Matrix Gate
→ EXPERT IESA — Final ERP & SaaS Assurance
```

### Allowed IDTM Status

- MATRIX EXECUTION COMPLETE
- VERIFIED WITHIN DECLARED TOLERANCE
- DEFECT FOUND
- CRITICAL INVARIANT VIOLATION
- TEST ADEQUACY GAP FOUND
- MUTATION / SEEDED DEFECT ESCAPED
- EVIDENCE MISSING
- RETEST REQUIRED
- DEEP TEST GATE HOLD
- READY FOR IESA FINAL ASSURANCE

EXPERT IDTM may not declare `FINAL APPROVED`, `BOSS APPROVED`, `PRODUCTION APPROVED`, or `RELEASE APPROVED`.

## EXPERT IESA — Independent ERP & SaaS Intelligence Assurance

Effective 2026-08-30, Boss formally appoints **EXPERT IESA — Independent ERP & SaaS Intelligence Assurance Team** as an independent project assurance unit.

### Purpose

IESA independently determines whether the completed solution is genuinely ready to be considered for customer/Production use at whole-system ERP and SaaS level after Figma/UX, Team C implementation, Team D independent QA/clean-room/compliance and EXPERT IDTM deep-test evidence exist.

IESA may perform a Pre-Assurance Challenge before IDTM execution to identify assurance evidence or risk scenarios that the matrix should address. This Pre-Assurance phase does not issue a Production-readiness verdict.

IESA Final Assurance occurs after IDTM Gate evidence.

### Independence

1. EXPERT IESA reports directly to Boss only.
2. EXPERT IESA is independent from Team A, Team B, Figma/UX, EXPERT IBPV, Team C, Team D, EXPERT IDTM, Boards, PMO and delivery owners.
3. PMO may register, preserve and route IESA evidence but may not direct, rewrite, suppress or override an IESA finding.
4. EXPERT IESA must not implement or repair the Production Code it independently assesses.
5. EXPERT IESA must not rewrite IDTM evidence or self-approve remediation it authored.
6. Material disagreement between delivery teams/IDTM and IESA must be recorded and escalated directly to Boss.
7. Boss alone may accept residual risk, waive a gap, authorize Release or authorize Production.

### Mandatory Position in Delivery Flow

```text
Team D — Independent QA / Clean-room / Compliance Audit
→ IESA Pre-Assurance Challenge (No Final Verdict)
→ EXPERT IDTM Deep Test Matrix Gate
→ EXPERT IESA Final ERP & SaaS Intelligence Assurance
→ Pre-Production Enterprise & SaaS Assurance Gate
→ Boss Release / Production Decision
→ Production / Customer Use
```

IESA Final Assurance is mandatory before Production/customer release unless Boss explicitly issues a written exception.

### IESA Assurance Scope

EXPERT IESA independently assesses, as applicable:

- ERP End-to-End Integrity
- Cross-Domain Transaction Integrity
- SaaS Multi-Tenant Architecture / Tenant Isolation
- Multi-Company / Multi-Organization Integrity
- Data / Transaction Consistency
- Security / Authorization Boundaries
- Performance / Scalability
- Availability / Reliability
- Failure Recovery / Retry / Idempotency / Concurrency
- Observability / Logging / Monitoring
- Auditability / Traceability
- Accounting / Financial Integrity
- Integration Resilience
- UX Operational Coherence against actual implementation
- Configuration / Extensibility
- Maintainability / Technical Debt
- Backup / Restore / Disaster Recovery
- Deployment / Upgrade / Rollback
- Production Operations Readiness
- Enterprise ERP Fitness for intended customer use
- IDTM Test Matrix adequacy and residual-risk evidence

### Allowed IESA Status

EXPERT IESA may issue evidence-based findings such as:

- SYSTEM VERIFIED
- VERIFIED WITH CONDITIONS
- SYSTEMIC GAP FOUND
- ARCHITECTURE RISK FOUND
- ERP INTEGRITY GAP FOUND
- SAAS READINESS GAP FOUND
- SECURITY / TENANT ISOLATION GAP FOUND
- PERFORMANCE / SCALABILITY GAP FOUND
- OPERATIONS READINESS GAP FOUND
- TEST ADEQUACY CONCERN
- EVIDENCE MISSING
- REMEDIATION REQUIRED
- NOT READY FOR PRODUCTION
- READY FOR BOSS DECISION

EXPERT IESA may not declare `FINAL APPROVED`, `BOSS APPROVED`, `PRODUCTION APPROVED`, or `RELEASE APPROVED`.

## Lifecycle Ruling — IDTM & IESA

A new numbered STATE is **not required at this time**.

IDTM is established as a mandatory independent Deep Test Matrix Gate within the controlled Testing/UAT lifecycle and before IESA Final Assurance.

IESA is established as a mandatory independent assurance/control layer through the Pre-Production Enterprise & SaaS Assurance Gate.

This preserves existing STATE numbering and historical traceability while adding hard controls before Final Assurance and Production/customer use.

If future evidence shows that IDTM or IESA requires a standalone lifecycle STATE, PMO may submit a controlled STATE-baseline Change Request to Boss. No STATE renumbering is authorized by the current ruling.

## Standard Execution Flow

```text
Governance
→ Learning / Knowledge Base
→ SaaS Foundation
→ Functional Specification
→ Evidence Review
→ Team B Independent Canonical Design
→ Figma / UX Design
→ EXPERT IBPV Independent Process & Design Verification
→ Pre-Development Design Gate
→ Boss Decision
→ SDS / API / DB / Engineering Preparation
→ Team C Development
→ Team D Independent QA / Clean-room / Compliance Audit
→ IESA Pre-Assurance Challenge
→ EXPERT IDTM 100% AI 10-Dimension Deep Test Matrix
→ Independent Deep Test Matrix Gate
→ Infrastructure / Deployment / Operations Evidence Reconciliation
→ EXPERT IESA Final ERP & SaaS Intelligence Assurance
→ Pre-Production Enterprise & SaaS Assurance Gate
→ Boss Release / Production Decision
→ Production / Customer Use
```

## Gate Rule

A downstream phase may not proceed unless the upstream gate is explicitly approved or marked PASS WITH CONTROL by the proper authority.

EXPERT IBPV findings do not replace Boss approval. A Critical unresolved IBPV gap keeps Development on HOLD unless Boss explicitly rules otherwise.

A Critical zero-tolerance IDTM defect, material tolerance breach, incomplete approved matrix execution, missing mandatory evidence, or unresolved Test Adequacy gap keeps IESA Final Assurance progression on HOLD unless Boss explicitly rules otherwise.

EXPERT IESA findings do not replace Boss approval. A Critical unresolved IESA gap keeps Release/Production/Customer Go-Live on HOLD unless Boss explicitly accepts the risk or rules otherwise.

## Current Control Status

```text
Project Constitution: APPROVED — v1.3
EXPERT IBPV: APPOINTED BY BOSS — ACTIVE GOVERNANCE UNIT
IBPV Reporting Line: DIRECT TO BOSS ONLY
IBPV Pre-Development Verification: MANDATORY
EXPERT IDTM: APPOINTED BY BOSS — ACTIVE INDEPENDENT DEEP TEST UNIT
IDTM Reporting Line: DIRECT TO BOSS ONLY
IDTM AI Execution: 100% OF APPROVED 10-DIMENSION MATRIX
Test Case Tolerance Ceiling: <= 0.001%
Critical Tolerance Classes: 0%
Zero-Bug Result: TEST ADEQUACY CHALLENGE MANDATORY
Independent Deep Test Matrix Gate: MANDATORY BEFORE IESA FINAL ASSURANCE
EXPERT IESA: APPOINTED BY BOSS — ACTIVE INDEPENDENT ASSURANCE UNIT
IESA Reporting Line: DIRECT TO BOSS ONLY
IESA Pre-Assurance Challenge: ALLOWED / NO FINAL VERDICT
Pre-Production Enterprise & SaaS Assurance Gate: MANDATORY
New numbered STATE for IDTM/IESA: NOT REQUIRED AT THIS TIME
AI Role Model: APPROVED
Functional Specification Standard: APPROVED FOR USE
Build Gate: HOLD unless domain-specific Boss approval exists
Production Gate: HOLD unless IDTM Gate, IESA Final Assurance and Boss Production decision are complete
```
