# EOS Exception Register

Status: MASTER CONTROL  
Version: v1.0  
Control Level: /L99  
Owner: PMO Evidence Controller  
Reviewer: Technical PMO Director  
Evidence Path: 99_SMEsPlus_Enterprise_Suite/00_Unified_Engineering_Standard/12_EXCEPTION_REGISTER.md  
Gate Status: ACTIVE / CONTROLLED

## Purpose

This register controls approved, rejected, held, and frozen exceptions from SUES, EOS, state standards, module standards, AI execution rules, and evidence gates.

## Rule

```text
No Exception ID = Invalid Exception
No Owner = HOLD
No Reviewer = HOLD
No Expiry Date = HOLD
No Approval = HOLD
```

## Required Fields

```text
Exception ID
Request Date
Requester
Affected Standard / State / Module
Exception Reason
Business Justification
Risk Level
Owner
Reviewer
Approver
Expiry Date
Evidence Path
Gate Impact
Decision
```

## Decision Values

| Decision | Meaning |
|---|---|
| APPROVED TEMPORARY | Allowed until expiry date |
| HOLD | Missing evidence, owner, reviewer, or criteria |
| REJECTED | Not aligned with SUES / EOS |
| FROZEN | Related work must stop until governance review is complete |

## Register Table

| Exception ID | Scope | Reason | Owner | Reviewer | Expiry | Decision | Evidence Path | Gate Impact |
|---|---|---|---|---|---|---|---|---|
| EXC-TEMPLATE-001 | Example only | Template placeholder | PMO Evidence Controller | Technical PMO Director | TBD | HOLD | TBD | No execution impact until completed |

## Closure Rule

Every exception must be closed by removal, renewal, conversion into a change request, or governance closure decision.
