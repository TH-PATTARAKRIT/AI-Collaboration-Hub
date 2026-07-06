# SUES State and Module Template Model

Status: MASTER STANDARD
Version: v1.0
Control Level: /L99

## Purpose

This model defines how state standards and module standards become working templates.

## Standard Chain

```text
SUES Enterprise Constitution
  -> Global Standard
    -> State Standard
      -> Module Standard
        -> Work Package Template
          -> Evidence Output
```

## State Standard Template

Each state must define:

```text
State ID
State Name
Objective
Input package
Allowed work
Blocked work
Review criteria
Required output
Evidence register
Gate checklist
Handoff condition
Owner
Reviewer
Approver
```

## Module Standard Template

Each module must define:

```text
Module ID
Module name
Business objective
Functional scope
Data scope
Integration scope
Thai localization scope where applicable
Security and permission scope
Performance target
Evidence register
Traceability matrix
Gate checklist
```

## Working Template Rule

A working template must inherit both state rules and module rules.

Example:

```text
ACC-001_FDS_Package inherits:
- SUES Enterprise Constitution
- Functional Standard
- State 04 Functional Specification Standard
- ACC Module Standard
- Evidence Standard
- Gate Standard
```

## Handoff Rule

A work package can move to the next state only when:

```text
Required input complete
Evidence complete
Reviewer confirmed
Gate decision recorded
Next-state handoff prepared
```
