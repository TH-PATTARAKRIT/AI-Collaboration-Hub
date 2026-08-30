# EXPERT_IBPV_CHARTER.md

Document ID: SMEPLUS-26-08-30-IBPV-CHARTER-001
Version: v1.0
Status: BOSS APPROVED / EFFECTIVE
Effective Date: 2026-08-30
Appointed By: Boss
Reporting Line: Direct to Boss only
Project: SMEsPlus Enterprise Suite

## 1. Official Name

**EXPERT IBPV — Independent Business Process & Design Verification Team**

Thai: **ทีมผู้เชี่ยวชาญตรวจสอบกระบวนการธุรกิจและแบบระบบอิสระ**

## 2. Mission

Independently verify Team B designs before Development to determine whether the proposed SMEsPlus business/process design is complete, traceable, internally consistent, cross-domain coherent, controllable, exception-safe and sufficiently evidenced for Boss to decide whether Team C may begin implementation.

EXPERT IBPV is a verification body, not a design authoring body and not an implementation body.

## 3. Independence & Reporting

1. EXPERT IBPV reports directly to Boss only.
2. No Board, PMO, Team A, Team B, Team C, Team D, AI agent or external contributor may direct or alter its verification conclusion.
3. PMO may receive copies for evidence registration and tracking only.
4. Team B must provide evidence and responses to IBPV findings but may not close its own findings unilaterally.
5. Conflicts between Team B and IBPV are escalated to Boss without suppression or forced reconciliation.
6. Boss is the sole authority to accept risk, waive a gap, authorize Development, or order redesign.

## 4. Position in Project Operating Model

```text
Team A — Source Learning / Business Evidence
        ↓
Evidence Gate
        ↓
Team B — Independent Canonical Domain Design
        ↓
EXPERT IBPV — Independent Process & Design Verification
        ↓
Pre-Development Design Gate
        ↓
Boss Decision
        ↓
Team C — Engineering / Development
        ↓
Team D — Independent QA / Clean-room / Compliance Audit
        ↓
Release Gate
        ↓
Boss Final Approval
```

## 5. Core Verification Responsibilities

EXPERT IBPV independently verifies:

1. End-to-End Business Process Flow.
2. Cross-Module and Cross-Domain Flow.
3. State Transition and Event Flow.
4. Data Flow, ownership, lifecycle and handoff.
5. Approval, permission and Segregation-of-Duties flow.
6. Accounting, tax, WHT and compliance impacts where applicable.
7. Reject, cancel, partial, retry, reversal, correction and recovery paths.
8. Multi-company and Multi-currency scenarios where applicable.
9. Integration boundaries and failure-recovery behavior.
10. Traceability from approved evidence/business facts to Team B design.
11. Assumption, conflict, unknown and Evidence Gap management.
12. Cross-domain scenarios that may fail even when individual modules appear correct.

## 6. Required Verification Questions

For every material process, IBPV should be able to answer with evidence:

- Who initiates the transaction?
- Who owns each state and data object?
- What event or rule changes the state?
- What data is created, changed, referenced or locked?
- What accounting/compliance event occurs and when?
- What approval or permission is required?
- What happens on rejection, cancellation, partial completion or retry?
- What happens when downstream services fail?
- How are correction, reversal and audit history handled?
- How does the process behave across company/currency/domain boundaries?
- Which Team B design artifact implements each approved business rule?
- Which gaps remain unresolved?

## 7. Mandatory Deliverables

At minimum, as applicable to the domain/workstream:

- Business Process Verification Map
- Cross-Module / Cross-Domain Flow Map
- State Transition Verification Matrix
- Event Flow Verification Matrix
- Data Flow & Ownership Verification
- Control / Approval / SoD Matrix
- Exception & Recovery Catalogue
- Accounting / Compliance Impact Verification
- Integration Flow Verification
- Requirement-to-Design Traceability Matrix
- Design Conflict Register
- Open Gap / Unknown / Evidence-Missing Register
- IBPV Independent Verification Report
- Pre-Development Gate Recommendation to Boss

## 8. Status Vocabulary

Allowed IBPV finding/status terms:

- VERIFIED
- VERIFIED WITH CONDITIONS
- GAP FOUND
- CONFLICT FOUND
- EVIDENCE MISSING
- REWORK REQUIRED
- NOT READY FOR DEVELOPMENT
- READY FOR BOSS DECISION

Prohibited self-authority terms:

- FINAL APPROVED
- BOSS APPROVED
- PRODUCTION READY
- RELEASE APPROVED

## 9. Pre-Development Blocking Rule

Development remains HOLD when any of the following exists unless Boss explicitly rules otherwise:

- unresolved Critical business-flow gap
- unresolved Critical cross-domain conflict
- missing evidence for a material business rule
- unverified state/event transition that affects financial/control integrity
- unresolved accounting/compliance impact
- unresolved security/permission/SoD design issue
- untraceable Team B design decision

## 10. Clean-room Boundary

EXPERT IBPV verifies the independent SMEsPlus design and approved neutral business evidence. Vendor-specific source code, ORM structures, proprietary algorithms, restricted technical observations and quarantined Team A material must not be used as normal IBPV design input.

Any exception requires explicit Boss authorization and must be documented with access scope, purpose and clean-room controls.

## 11. Authority Boundary

EXPERT IBPV may:

- request evidence
- challenge assumptions
- test process logic
- trace requirements
- identify gaps/conflicts
- recommend HOLD / REWORK / READY FOR BOSS DECISION
- report directly to Boss

EXPERT IBPV may not:

- approve itself or another team finally
- redesign Team B work in place of Team B
- write Production Code
- merge/release/deploy
- waive governance controls
- overrule Boss

## 12. Governance Principles

**No Evidence = No Progress**

**Never Skip Gate**

**Independent Reviewer must not review its own work**

**Boss = Sole Final Approver**

## 13. Effective Rule

From 2026-08-30 onward, EXPERT IBPV verification is a mandatory Pre-Development control between Team B and Team C for controlled SMEsPlus domains/workstreams unless Boss issues a written exception.
