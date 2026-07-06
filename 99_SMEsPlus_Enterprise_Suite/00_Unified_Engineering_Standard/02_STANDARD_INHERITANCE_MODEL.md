# SUES Standard Inheritance Model

Status: MASTER STANDARD  
Version: v1.0  
Control Level: /L99

## 1. Purpose

This document defines how SMEsPlus standards inherit rules from the enterprise level down to state, module, and working templates.

## 2. Inheritance Chain

```text
Enterprise Constitution
  -> Global Standard
    -> State Standard
      -> Module Standard
        -> Work Package
          -> Working Template
            -> Evidence Output
              -> Gate Decision
```

## 3. Mandatory Rule

A lower-level document may add detail, but must not remove mandatory controls inherited from the higher level.

Mandatory inherited fields:

```text
Document ID
Version
Status
Project
State
Module
Owner
Reviewer
Approver
Jira ID
GitHub Path
Evidence Path
Gate Status
Control Level
No Evidence Rule
Traceability Matrix
Evidence Register
Gate Checklist
Next-State Handoff
```

## 4. Override Model

Overrides are allowed only when controlled.

```text
Override Type:
- Business override
- Architecture override
- Security override
- Performance override
- Integration override
- PMO/Gate override
```

Every override must include:

```text
Inherited Rule
Proposed Override
Reason
Risk
Mitigation
Owner
Reviewer
Approver
Evidence Path
Expiry / Review Date
Gate Impact
```

## 5. Override Decision

```text
APPROVED = override accepted with evidence
HOLD = waiting for evidence/reviewer/approver
REJECTED = not accepted
FROZEN = critical breach or unsafe exception
```

## 6. Example

```text
Enterprise rule: Use ORM by default for maintainability and security.
Module exception: Raw SQL candidate for high-volume posting report.
Required control: Architecture approval, tenant isolation proof, audit review, performance evidence, test evidence.
```

## 7. Conflict Resolution

If module rule conflicts with state rule, state rule wins unless approved override exists.

If state rule conflicts with enterprise constitution, enterprise constitution wins.

If AI output conflicts with evidence, evidence wins.
