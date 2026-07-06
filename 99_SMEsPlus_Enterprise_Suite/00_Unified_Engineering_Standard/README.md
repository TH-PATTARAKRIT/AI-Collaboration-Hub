# SMEsPlus Unified Engineering Standard (SUES)

Status: MASTER STANDARD  
Version: v1.0  
Control Level: /L99  
Applies To: All States, Modules, AI Agents, PMO Reviews, Engineering Work, Evidence Gates  
Rule: No Evidence = No Progress

## 1. Purpose

SUES is the master operating standard for SMEsPlus. It defines how project standards, state controls, module rules, AI execution, evidence gates, and working templates inherit from one governance model.

This is not only a document template. It is an engineering contract for the project.

## 2. Operating Principle

```text
Template -> Standard -> Contract -> Enforcement
```

All working templates must inherit from SUES. Teams may add module-specific or state-specific details, but they must not remove mandatory control fields.

## 3. Standard Layers

```text
Level 1: Enterprise Constitution
Level 2: Global Standards
Level 3: State Standards
Level 4: Module Standards
Level 5: Working Templates
Level 6: Evidence and Gate Enforcement
```

## 4. Required AI Context Before Execution

Every AI agent must know the current execution context before starting work:

```text
AI Identity
Current State
Current Module
Current Gate
Current Owner
Current Reviewer
Current Constraints
Current Evidence
Current Objective
Allowed Scope
Prohibited Scope
Required Output
Evidence Path
```

If any required context is missing, AI must return:

```text
PROMPT NOT READY / HOLD
```

## 5. Relationship to Existing Frameworks

SUES is the master standard. The existing State-Based AI Execution Control Framework is a child framework under SUES.

```text
SUES
  -> State-Based AI Execution Control
  -> State Gate Matrix
  -> State Input / Output Rule
  -> State Evidence Rule
  -> State Prompt Guardrail
  -> Working Templates
```

## 6. Gate Rule

```text
No Evidence = No Progress
No Criteria = No AI Execution
No Owner = HOLD
No Reviewer = HOLD
No Gate Approval = No Next State
Critical breach = FROZEN
```

## 7. Flexibility Rule

SUES supports controlled flexibility through inheritance and override.

```text
Inherited rule = mandatory baseline
Override = allowed only when documented, justified, reviewed, and approved
Exception = must include risk, owner, reviewer, evidence, and expiry/review date
```

## 8. Immediate Use

All new SMEsPlus documents should use SUES-compatible headers, evidence fields, traceability matrix, AI review criteria, gate checklist, and handoff sections.
