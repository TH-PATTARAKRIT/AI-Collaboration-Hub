# PROJECT_CONSTITUTION.md

Version: v1.1
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
| EXPERT IBPV | Independent Business Process & Design Verification; reports directly to Boss only; no Team/Board/PMO may alter its independent findings |
| Team C / Claude Code | Engineering / implementation only after Pre-Development Design Gate and Boss approval |
| Team D | Independent QA / clean-room / compliance audit after implementation evidence exists |

## EXPERT IBPV — Independent Business Process & Design Verification

Effective 2026-08-30, Boss formally appoints **EXPERT IBPV — Independent Business Process & Design Verification Team** as an independent project unit.

### Independence

1. EXPERT IBPV reports directly to Boss only.
2. EXPERT IBPV is organizationally and functionally independent from Team A, Team B, Team C, Team D, all Boards and PMO review influence.
3. PMO may register, route and preserve IBPV evidence, but may not direct, rewrite, suppress or override an IBPV finding.
4. EXPERT IBPV must not verify work it authored itself.
5. EXPERT IBPV must not implement Production Code or redesign Team B work on Team B's behalf.
6. Any conflict between Team B and EXPERT IBPV must be recorded in a Design Conflict Register and escalated directly to Boss.

### Mandatory Position in Delivery Flow

```text
Team A — Evidence / Source Understanding
→ Evidence Gate
→ Team B — Independent Canonical Domain Design
→ EXPERT IBPV — Independent Business Process & Design Verification
→ Pre-Development Design Gate
→ Boss Decision
→ Team C — Engineering / Development
→ Team D — Independent QA / Clean-room / Compliance Audit
→ Release Gate
→ Boss Final Approval
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
- Traceability from approved business evidence to Team B design
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

## Standard Execution Flow

```text
Governance
→ Learning / Knowledge Base
→ SaaS Foundation
→ Functional Specification
→ Evidence Review
→ Team B Independent Canonical Design
→ EXPERT IBPV Independent Process & Design Verification
→ Pre-Development Design Gate
→ Boss Decision
→ SDS / API / DB / UX / Engineering Preparation
→ Development
→ Team D Independent QA / Clean-room / Compliance Audit
→ Traceability / QA / UAT
→ Release Review
→ Production Gate
→ Boss Final Approval
```

## Gate Rule

A downstream phase may not proceed unless the upstream gate is explicitly approved or marked PASS WITH CONTROL by the proper authority. EXPERT IBPV findings do not replace Boss approval. A Critical unresolved IBPV gap keeps Development on HOLD unless Boss explicitly rules otherwise.

## Current Control Status

```text
Project Constitution: APPROVED — v1.1
EXPERT IBPV: APPOINTED BY BOSS — ACTIVE GOVERNANCE UNIT
IBPV Reporting Line: DIRECT TO BOSS ONLY
IBPV Pre-Development Verification: MANDATORY
AI Role Model: APPROVED
Functional Specification Standard: APPROVED FOR USE
Build Gate: HOLD unless domain-specific Boss approval exists
Production Gate: HOLD
```
