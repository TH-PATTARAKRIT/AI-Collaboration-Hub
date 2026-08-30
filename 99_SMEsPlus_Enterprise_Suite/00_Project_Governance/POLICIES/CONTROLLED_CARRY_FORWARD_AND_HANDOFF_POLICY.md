# CONTROLLED CARRY-FORWARD & HANDOFF POLICY

Policy ID: SMEPLUS-POL-CF-001
Version: v1.0
Status: BOSS APPROVED / MANDATORY
Effective Date: 2026-08-30
Authority: Boss Decision `SMEPLUS-BDR-CF-2026-08-30-001`
Project: SMEsPlus Enterprise Suite
Applies To: All STATEs, STEPs, Boards, Teams, Domains, PMO, reviewers and AI execution agents

## 1. Purpose

Prevent unresolved work from being pushed forward without clear accountability, timing, deliverables, acceptance criteria, evidence requirements and Gate impact.

Carry Forward is allowed only as a controlled handoff into a later approved execution point.

## 2. Core Control Rules

```text
No Owner = No Carry Forward
No Receiver Acceptance = No Handoff
No Due/Trigger = No Schedule
No Acceptance Criteria = No Closure
```

A Carry Forward is not valid merely because it appears in a report, closure note or backlog list.

## 3. Mandatory Record Fields

Every Carry Forward record must include:

1. Carry-Forward ID
2. Source STATE
3. Source STEP / Domain / Workstream
4. Source Evidence Reference
5. Gap / Risk / Open Item description
6. Reason for deferral
7. Classification
8. Target STATE
9. Target STEP / Domain / Workstream
10. Accountable Owner
11. Responsible Team
12. Required Deliverable
13. Acceptance Criteria
14. Due Date or execution Trigger
15. Dependencies
16. Required Evidence / Evidence Path
17. Gate Impact
18. Receiver Acceptance status
19. Receiver Acceptance evidence/date
20. Aging / Days Open
21. Overdue status
22. Current Status
23. Deferral Count
24. Boss Ruling reference where required

Unknown required values must be marked `TBD / UNASSIGNED` and treated as a Red Flag. They do not qualify as an accepted handoff.

## 4. Carry-Forward Lifecycle

```text
Gap / Open Item Identified
→ classify impact
→ define Target STATE / STEP
→ assign Accountable Owner + Responsible Team
→ define Deliverable + Acceptance Criteria
→ define Due Date / Trigger
→ define Evidence + Gate Impact
→ Receiver Review
→ Receiver ACCEPTS
→ register in Target Baseline / Controlled Register
→ source item may become CARRY FORWARD ACCEPTED
→ execute at target point
→ evidence verification
→ CLOSED
```

## 5. Valid Statuses

- PROPOSED
- OWNER ASSIGNMENT REQUIRED
- RECEIVER REVIEW REQUIRED
- REJECTED / RETURN TO SOURCE
- CARRY FORWARD ACCEPTED
- SCHEDULED / TRIGGERED
- IN PROGRESS
- EVIDENCE REVIEW
- VERIFIED
- CLOSED
- OVERDUE
- ESCALATED TO BOSS

`CARRY FORWARD ACCEPTED` is permitted only after receiver acceptance and target-baseline registration.

## 6. Source-State / Source-Step Closure Rule

The source item remains OPEN when any of these conditions exists:

- Accountable Owner = TBD / UNASSIGNED
- Responsible Team = TBD
- Target STATE/STEP = TBD
- Deliverable is undefined
- Acceptance Criteria are undefined
- Due Date / Trigger is undefined
- Receiver has not accepted
- Target baseline/register does not contain the item
- material Gate Impact is unknown

Source closure may not count an invalid or unaccepted Carry Forward as completed progress.

## 7. Classification Boundary

### BLOCKER
Must be resolved before the current Gate may proceed. It must not be converted into Carry Forward merely to close the current STATE/STEP.

### CARRY FORWARD
Within approved scope. Execution is intentionally owned by a later STATE/STEP. All mandatory handoff fields and receiver acceptance are required.

### BACKLOG
Useful/desirable item not required by the current approved baseline. It does not receive current-state progress credit.

### CHANGE REQUEST
Outside the approved baseline/scope. Requires controlled CR review and Boss decision as applicable. It must not be hidden as Carry Forward.

## 8. Receiver Acceptance

Receiver acceptance means the receiving owner/team explicitly acknowledges:

- the item belongs to its controlled scope or has been authorized into that scope
- required deliverable is understood
- Acceptance Criteria are understood
- Due Date / Trigger is recognized
- dependencies are known
- Gate impact is recognized
- evidence obligation is accepted

Silence, assumed ownership or a copied name in a report is not receiver acceptance.

## 9. Target-Baseline Registration

Accepted Carry Forward must be written into the controlled target STATE/STEP register, plan or baseline. The source and target records must cross-reference the same Carry-Forward ID.

A source-only Carry Forward record is incomplete.

## 10. Aging / Overdue Control

PMO must preserve visibility of:

- created date
- accepted date
- due/trigger
- current age
- overdue days
- latest action/evidence
- next owner action

Overdue items with material Gate, risk, customer or architecture impact must be escalated as Red Flags.

## 11. No Infinite Deferral

Initial controlled Carry Forward may be approved through normal governance when all requirements are met.

If the same item is proposed to move again beyond its accepted target STATE/STEP:

```text
Deferral Count >= 2
→ Boss Review Required
```

The review package must state:

- original source
- original target
- current accountable owner
- reason for re-deferral
- aging
- unresolved dependency
- impact to timeline / Gate / risk
- revised target and due/trigger
- recommendation

No automatic cascading deferral is allowed.

## 12. Ownership Mapping Guidance

Typical routing, subject to actual approved scope:

- Business Process / Functional Design → Team B / STATE04
- UX / Interaction / User Journey → Figma / STATE05
- Implementation / Engineering → Team C / STATE06
- QA / Regression / Deep Testing → Team D / EXPERT IDTM / STATE07
- Infrastructure / Capacity / DR / Operations → Infrastructure / STATE09
- Enterprise / SaaS Production Assurance → EXPERT IESA / Pre-Production Assurance
- unclear ownership → PMO RED FLAG → Boss Decision

This guidance does not authorize scope expansion or override a specific approved owner assignment.

## 13. Evidence Rule

Every closure must identify evidence sufficient to prove the deliverable and Acceptance Criteria were met.

```text
No Evidence = No Progress
No Evidence = No Closure
```

## 14. Governance Principle

**Carry Forward is a controlled transfer of accountability, not a transfer of uncertainty.**

**Never Skip Gate.**

**Boss = Sole Final Approver.**
