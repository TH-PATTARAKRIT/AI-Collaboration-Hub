# STATE INPUT OUTPUT RULE

Status: Active  
Project: SMEsPlus Enterprise Suite

## 1. Purpose

This rule defines the minimum input and output requirements before AI can operate in any project state.

AI execution is blocked if the state has no defined input package, criteria, output target, or evidence path.

## 2. Minimum Input Package

Each state must provide:

```text
State ID
State Name
Objective
Scope
Out of Scope
Input Files / References
Business Context
Technical Context
Current Gate Status
Owner
Reviewer
Evidence Path
```

## 3. Minimum AI Output

Every AI output must include:

```text
Executive Summary
Reviewed Items
Gap Items
Missing Evidence
Risks
Required Fixes
Owner / Reviewer
Evidence Path
Gate Recommendation: PASS / HOLD / FAIL / FROZEN
Next-State Handoff Condition
```

## 4. Input Readiness Rule

```text
Input complete = AI review allowed
Input partial = AI gap review only
Input missing = AI execution blocked
Input contradictory = PMO investigation required
```

## 5. Output Acceptance Rule

AI output is not accepted if it lacks:

```text
Evidence linkage
Gate impact
Reviewer field
Missing-evidence section
Clear PASS / HOLD / FAIL recommendation
```

## 6. Development-Specific Restriction

Development output is allowed only after Functional Design, UX/UI Design, Architecture, and Build Readiness Gate have passed with evidence.

Before Development Gate:

```text
AI may review, analyze, map, and report.
AI must not create production-ready code.
AI must not merge or release.
```
