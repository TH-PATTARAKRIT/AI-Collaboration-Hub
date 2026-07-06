# STATE AI EXECUTION STANDARD

Status: Active  
Project: SMEsPlus Enterprise Suite  
Control Principle: State-Based AI Execution Control  
Rule: No Evidence = No Progress

## 1. Standard Objective

This standard prevents AI agents from working outside the approved project scope, skipping gates, generating unsupported conclusions, or producing development output before the required state is approved.

It applies to every AI-assisted activity in SMEsPlus.

## 2. Universal State Control Model

Every state must define:

```text
1. Input Package
2. AI Allowed Scope
3. AI Prohibited Scope
4. Review Criteria
5. Required Output
6. Evidence Requirement
7. Owner
8. Reviewer / Verifier
9. Gate Result
10. Next-State Handoff
```

## 3. Universal AI Rules

```text
AI must follow the state criteria.
AI must not use open-ended prompts.
AI must not invent missing requirements.
AI must not claim completion without evidence.
AI must not move work to the next state without gate approval.
AI must not code before Development Gate.
AI must not merge, release, deploy, or operate production without explicit approval.
```

## 4. State Control Layers

```text
Layer 1: Functional / Business Control
Layer 2: Architecture / Technical Control
Layer 3: Evidence / PMO Control
Layer 4: Security / Compliance Control
Layer 5: Executive Approval Control
```

## 5. Mandatory Evidence Fields

Every output must include:

```text
Task / Item
State
Owner
Evidence Path / Link
Timestamp
Reviewer / Verifier
Verification Status
Gate Impact
Next Action
```

## 6. State Completion Rule

A state cannot be reported as passed unless all required evidence is available, accessible, reviewed, and linked to the gate result.

If evidence is missing:

```text
Status = HOLD or FAIL
Progress = Not counted
Gate Impact = Block next state
```

## 7. Executive Control Rule

Only authorized PMO / Architecture / QA / Security / Boss approval can change a state from HOLD to PASS.

AI-generated reports are evidence inputs only. AI does not approve itself.
