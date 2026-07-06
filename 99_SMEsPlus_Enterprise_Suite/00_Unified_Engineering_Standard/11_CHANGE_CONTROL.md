# EOS Change Control

Status: MASTER CONTROL  
Version: v1.0  
Control Level: /L99  
Owner: PMO Evidence Controller  
Reviewer: Strategic Delivery Lead  
Evidence Path: 99_SMEsPlus_Enterprise_Suite/00_Unified_Engineering_Standard/11_CHANGE_CONTROL.md  
Gate Status: ACTIVE / CONTROLLED

## Purpose

This document defines how changes to SMEsPlus standards, templates, states, modules, AI prompts, evidence gates, and review workflows are requested, assessed, approved, implemented, and closed.

## Change Rule

```text
No Change Request = No Change
No Criteria = HOLD
No Owner = HOLD
No Reviewer = HOLD
No Gate Impact Review = HOLD
Unauthorized Change = FROZEN
```

## Change Request Fields

```text
Change ID
Request Date
Requester
Affected Standard / State / Module / AI / Evidence Gate
Current Version
Proposed Version
Change Reason
Business Impact
Technical Impact
Evidence Impact
Gate Impact
Risk Level
Owner
Reviewer
Approver
Decision
Evidence Path
Closure Date
```

## Change Types

| Type | Description | Minimum Approval |
|---|---|---|
| STANDARD | Standard or policy change | Technical PMO Director |
| TEMPLATE | Working template change | PMO Evidence Controller |
| STATE | State workflow or gate change | Strategic Delivery Lead |
| MODULE | Module-specific rule change | Module Owner + Technical PMO Director |
| AI | Prompt, persona, or AI execution rule change | AI Governance Lead |
| EVIDENCE | Evidence requirement or gate field change | PMO Evidence Controller |

## Workflow

```text
Request -> Impact Review -> Evidence Review -> Owner Review -> Reviewer Decision -> Approval -> Registry Update -> GitHub Update -> Jira Update -> Closure
```

## Decision Values

| Decision | Meaning |
|---|---|
| APPROVED | May be implemented under controlled execution |
| HOLD | Missing owner, reviewer, criteria, or evidence |
| REJECTED | Not aligned with SUES / EOS / project direction |
| FROZEN | Conflict affects active gate, compliance, or governance control |

## Required Evidence

Every approved change must include a GitHub path, Jira issue or comment reference where available, owner, reviewer, timestamp, and gate impact summary.
