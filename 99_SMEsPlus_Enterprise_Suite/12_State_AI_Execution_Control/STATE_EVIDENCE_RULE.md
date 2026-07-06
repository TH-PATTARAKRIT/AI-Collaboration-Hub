# STATE EVIDENCE RULE

Status: Active  
Project: SMEsPlus Enterprise Suite  
Control Rule: No Evidence = No Progress

## 1. Purpose

This rule defines how evidence must be attached, reviewed, and used for state gate decisions.

## 2. Required Evidence Fields

Every evidence item must include:

```text
Evidence ID
State ID
Work Item
Owner
Evidence Location / Link / Path
Timestamp
Reviewer / Verifier
Verification Status
Gate Impact
Decision: PASS / HOLD / FAIL / FROZEN
```

## 3. Evidence Quality Rule

Valid evidence must be:

```text
Accessible
Inspectible
Linked to a work item
Timestamped
Owned
Reviewed
Mapped to gate impact
```

## 4. Invalid Evidence

The following cannot be counted as progress:

```text
Screenshot without context
Claim without file/link/path
AI statement without source
Percentage without evidence
Output without owner
Output without reviewer
Evidence that cannot be opened
Evidence that contradicts reported status
```

## 5. Gate Classification

```text
PASS = evidence complete and reviewed
HOLD = evidence partial or awaiting review
FAIL = evidence missing, inaccessible, or incorrect
FROZEN = legal, security, production, or governance breach
```

## 6. PMO Control

PMO must maintain a state evidence register. Each state must have its own evidence register using the standard template.

## 7. AI Evidence Rule

AI must produce evidence reports, but AI cannot verify itself. Human or assigned PMO/Lead reviewer must confirm the evidence before PASS.
