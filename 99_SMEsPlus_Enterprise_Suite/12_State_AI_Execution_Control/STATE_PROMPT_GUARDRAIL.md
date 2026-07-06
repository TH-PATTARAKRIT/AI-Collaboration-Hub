# STATE PROMPT GUARDRAIL

Status: Active  
Project: SMEsPlus Enterprise Suite

## 1. Purpose

This guardrail prevents open-ended AI execution, hallucinated progress, unapproved coding, and gate skipping.

## 2. Mandatory Prompt Structure

Every AI prompt must include:

```text
Project
State ID
State Name
Objective
Input Files
Allowed Scope
Prohibited Scope
Review Criteria
Required Output
Evidence Path
Gate Recommendation Format
No Evidence Rule
```

## 3. Universal Prompt Header

```text
You are operating under SMEsPlus State-Based AI Execution Control.
You must follow the approved state criteria only.
Do not invent missing requirements.
Do not skip gates.
Do not claim progress without evidence.
Do not code unless Development Gate is approved.
Return PASS / HOLD / FAIL / FROZEN with evidence reasons.
```

## 4. Forbidden Prompt Types

```text
Build everything
Improve everything
Review generally
Make it enterprise-grade without criteria
Proceed to coding without approved FDS
Mark complete without evidence
Deploy to production
Merge this PR without review
```

## 5. Required AI Output Format

```text
1. Executive Summary
2. Scope Reviewed
3. Evidence Used
4. Gaps Found
5. Missing Evidence
6. Risks
7. Required Fixes
8. Gate Recommendation
9. Next State Readiness
```

## 6. Prompt Failure Rule

If the prompt lacks scope, criteria, input, output, or evidence path:

```text
AI must return: PROMPT NOT READY / HOLD
```
