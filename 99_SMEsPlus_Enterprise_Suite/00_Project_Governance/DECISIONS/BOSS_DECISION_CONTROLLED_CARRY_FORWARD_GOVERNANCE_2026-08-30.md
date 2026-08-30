# BOSS DECISION — CONTROLLED CARRY-FORWARD GOVERNANCE

Decision ID: SMEPLUS-BDR-CF-2026-08-30-001
Project: SMEsPlus Enterprise Suite
Date: 2026-08-30
Authority: Boss
Status: APPROVED / EFFECTIVE

## Decision

Boss approves mandatory Controlled Carry-Forward Governance for all SMEsPlus STATEs, STEPs, Boards, Teams, Domains and controlled workstreams.

Carry Forward is a controlled transfer of accountability. It is not permission to move an unresolved item forward without a named receiver, timing, deliverable and closure condition.

## Mandatory Rules

```text
No Owner = No Carry Forward
No Receiver Acceptance = No Handoff
No Due/Trigger = No Schedule
No Acceptance Criteria = No Closure
```

An item proposed for Carry Forward is not valid until the receiving STATE/STEP/team has accepted responsibility and the item has been registered in the target baseline.

## Required Carry-Forward Fields

Every controlled Carry Forward must record at minimum:

- Carry-Forward ID
- Source STATE / STEP / Domain
- Gap / Risk / Open Item
- reason for deferral
- Target STATE / STEP / Domain
- Accountable Owner
- Responsible Team
- required Deliverable
- Acceptance Criteria
- Due Date or explicit execution Trigger
- dependencies
- Evidence Path / evidence requirement
- Gate Impact
- Receiver Acceptance
- aging / overdue status
- current status

Any mandatory field that is unknown must be explicitly recorded as `TBD / UNASSIGNED` and treated as a Red Flag. It does not qualify as an accepted Carry Forward.

## Source-State Closure Rule

The source STATE/STEP may treat an item as `CARRY FORWARD ACCEPTED` only when:

1. Target STATE/STEP is identified.
2. Accountable Owner is named.
3. Responsible Team is identified.
4. Deliverable and Acceptance Criteria are defined.
5. Due Date or Trigger is defined.
6. Receiving Owner/Team has accepted the handoff.
7. Item is registered into the target STATE/STEP baseline or controlled register.
8. Gate impact is recorded.

Otherwise:

```text
UNASSIGNED CARRY-FORWARD
= INVALID HANDOFF
= RED FLAG
= SOURCE ITEM REMAINS OPEN
```

## Classification Rule

The project must not use `Carry Forward` as a generic bucket.

- `BLOCKER` = must be resolved before the current Gate can pass.
- `CARRY FORWARD` = within approved scope, but execution belongs to a later controlled STATE/STEP and has an accepted owner.
- `BACKLOG` = useful or desirable, but not required by the current approved baseline.
- `CHANGE REQUEST (CR)` = outside the approved baseline/scope and requires controlled scope decision.

## No Infinite Deferral Rule

A Carry Forward may not be repeatedly pushed from one STATE to another without control.

If an accepted Carry Forward is proposed for a second downstream deferral, PMO must raise it for explicit Boss Review with:

- reason for second deferral
- accumulated aging
- risk impact
- timeline/gate impact
- current accountable owner
- revised target and due/trigger

No silent or automatic re-forwarding is allowed.

## Aging and Escalation

Carry-Forward aging and overdue status must remain visible. Overdue, unaccepted, ownerless, or repeatedly deferred items are Red Flags and must be surfaced to PMO / Boss according to impact.

## Governing Principle

**Carry Forward is a controlled transfer of accountability, not a transfer of uncertainty.**

**No Evidence = No Progress.**

**Never Skip Gate.**

**Boss = Sole Final Approver.**
