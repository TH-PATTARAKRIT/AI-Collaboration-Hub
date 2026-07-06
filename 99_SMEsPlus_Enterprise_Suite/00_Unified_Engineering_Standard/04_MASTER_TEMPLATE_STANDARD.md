# SUES Master Template Standard

Status: MASTER STANDARD
Version: v1.0
Control Level: /L99

## Purpose

This standard defines the required structure for all SMEsPlus working documents. It keeps documents strict enough for governance and flexible enough for different states and modules.

## Mandatory Header Fields

Every document must include these fields:

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
Last Updated
Gate Status
Rule
Control Level
```

## Mandatory Sections

Every major document must include:

```text
Objective
Scope / Out of Scope
Input References
Requirement / Work Item List
Business Rule / Control Rule
Process / Workflow
Data / Field / Mapping
Role / Permission / Responsibility
Validation / Acceptance Criteria
Risk / Assumption / Dependency
Evidence Register
Traceability Matrix
Review Criteria
Gate Checklist
Gate Decision Summary
Next-State Handoff
```

## Gate Decision Rule

```text
PASS = complete reviewed evidence exists
HOLD = partial evidence or pending review
FAIL = missing, incorrect, inaccessible, or contradictory evidence
FROZEN = critical control breach
```

## Flexibility Rule

Teams may add sections required by their state or module. Teams must not remove the mandatory header, evidence register, traceability matrix, gate checklist, or handoff section.

## Enforcement

A document without owner, reviewer, evidence path, traceability, and gate decision cannot be counted as progress.
