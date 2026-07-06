# STATE HANDOFF RULE

Status: Active  
Project: SMEsPlus Enterprise Suite

## 1. Purpose

This rule controls movement from one project state to the next. No state may hand off work without evidence and gate approval.

## 2. Handoff Requirements

A handoff report must include:

```text
Source State
Target State
Completed Work Items
Open Work Items
Evidence Register Link
Known Risks
Gate Decision
Approval Owner
Reviewer
Timestamp
Next-State Readiness
```

## 3. Handoff Decision

```text
PASS = handoff allowed
HOLD = handoff blocked until evidence/review is complete
FAIL = handoff rejected
FROZEN = handoff stopped due to critical breach
```

## 4. Handoff Restrictions

```text
Functional Design cannot hand off to UX/UI without approved FDS.
UX/UI cannot hand off to Development without approved screen/spec evidence.
Development cannot hand off to QA without PR/test evidence.
QA cannot hand off to Deployment without test/UAT evidence.
Deployment cannot hand off to Production without security/backup/monitoring approval.
Production cannot change without incident/change control evidence.
```

## 5. AI Role in Handoff

AI may prepare the handoff report, detect gaps, and summarize risks.

AI must not approve handoff on its own.

## 6. No Evidence Rule

If any required evidence is missing:

```text
Handoff Status = HOLD
Next State = Not Started
Progress = Not Counted
```
