# SUES Enterprise Constitution

Status: MASTER STANDARD  
Version: v1.0  
Control Level: /L99  
Rule: No Evidence = No Progress

## 1. Purpose

This constitution defines the highest-level principles for SMEsPlus engineering, AI execution, PMO control, evidence gate enforcement, and project governance.

All lower-level standards inherit from this document.

## 2. Enterprise Principles

```text
1. SMEsPlus-first, Enterprise-first control
2. Odoo-first where suitable, but not Odoo-bound where SMEsPlus requires better enterprise design
3. Thai SME and Thai accounting localization must be treated as core, not optional
4. SaaS / Multi-tenant readiness is mandatory
5. Security, audit, and evidence are mandatory controls
6. AI is an execution assistant, not an approval authority
7. No Evidence = No Progress
8. No Gate Approval = No Next State
```

## 3. Architecture Principles

```text
1. Tenant isolation must be protected in every design decision
2. Posting engine must control accounting posting
3. Approval engine approves only; source module executes business operation
4. Immutable events must be used where auditability is required
5. Performance targets must be designed, measured, and evidenced
6. Raw SQL is allowed only as an architecture-approved exception
7. Production readiness requires infrastructure, security, backup, monitoring, and approval evidence
```

## 4. Engineering Principles

```text
1. Requirement must trace to business rule
2. Business rule must trace to process
3. Process must trace to data mapping
4. Data mapping must trace to screen/API and test case
5. Test case must trace to evidence
6. Evidence must trace to gate result
```

## 5. AI Principles

```text
1. AI must work from approved context only
2. AI must not invent missing requirements
3. AI must not use open-ended prompts
4. AI must not approve itself
5. AI must not code before Development Gate
6. AI must not merge, release, deploy, or operate production without explicit approval
7. AI must return PASS / HOLD / FAIL / FROZEN with evidence reasons
```

## 6. Evidence Principles

```text
Evidence must be accessible, inspectable, timestamped, owned, reviewed, and linked to gate impact.
```

## 7. Flexibility Principle

Flexibility is allowed only through controlled override.

```text
Override must declare:
- inherited rule
- reason for override
- risk
- owner
- reviewer
- approver
- evidence path
- expiry or review date
```

## 8. Enforcement

If any team, AI agent, or workstream violates this constitution, the relevant item must be marked HOLD, FAIL, or FROZEN depending on severity.
