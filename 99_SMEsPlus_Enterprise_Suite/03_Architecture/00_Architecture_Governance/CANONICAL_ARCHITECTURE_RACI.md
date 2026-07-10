# Canonical Architecture RACI

Session: [SMEPLUS-26-07-10-001]
Version: 2.0-draft
Status: CONTROLLED DRAFT
Gate Status: HOLD

## Role Definitions

| Role ID | Role | Primary Responsibility |
|---|---|---|
| ARC-R01 | SMEsPlus Domain Owner | Provides business context, validates scope and confirms domain correctness |
| ARC-R02 | Domain AI Owner | Owns domain content quality, deliverables and corrective action |
| ARC-R03 | Claude AI Execution Agent | Drafts, analyzes, prepares files and performs authorized GitHub execution |
| ARC-R04 | Domain Specialist Reviewer | Performs specialist review for the assigned domain |
| ARC-R05 | ChatGPT L99 Reviewer | Performs cross-domain, traceability, evidence and governance review |
| ARC-R06 | PMO Evidence Controller | Maintains WBS, registers, findings, evidence and gate records |
| ARC-R07 | Human Accountable Reviewer | Accepts business or technical accountability for critical domains |
| ARC-R08 | Repository Owner | Controls repository structure, branch and merge standards |
| ARC-R09 | Boss | Approves baseline, exception and final gate decisions |

## RACI Matrix

| Activity | Domain Owner | Domain AI Owner | Claude AI | Specialist Reviewer | ChatGPT L99 | PMO Evidence | Human Reviewer | Repo Owner | Boss |
|---|---|---|---|---|---|---|---|---|---|
| Define business context | A/R | C | I | C | C | I | C | I | I |
| Prepare domain charter | A | R | R | C | C | I | C | I | I |
| Draft architecture document | C | A/R | R | C | I | I | I | I | I |
| Commit working evidence | I | A | R | I | I | C | I | C | I |
| Validate domain content | A/R | C | I | C | I | I | C | I | I |
| Specialist review | C | C | I | A/R | C | I | C | I | I |
| Cross-domain review | C | C | I | C | A/R | C | C | I | I |
| Evidence validation | I | C | C | C | C | A/R | I | C | I |
| Correct finding | C | A/R | R | C | C | C | I | I | I |
| Close finding recommendation | C | C | I | R | A/R | R | C | I | I |
| Prepare gate recommendation | C | C | I | C | A/R | R | C | I | I |
| Approve Architecture Baseline | C | I | I | C | C | C | C | I | A/R |
| Approve exception or waiver | C | I | I | C | C | R | C | I | A/R |
| Merge governance PR | I | I | I | I | C | C | I | A/R | I |

Legend: R = Responsible, A = Accountable, C = Consulted, I = Informed.

## Separation-of-Duties Rules

1. The author or execution agent cannot independently approve the same deliverable.
2. Claude AI may draft and commit but cannot approve, close critical findings or issue a final gate decision.
3. ChatGPT L99 issues review recommendations only and cannot grant final approval.
4. Critical domains require both a specialist reviewer and a human accountable reviewer.
5. Boss is the only final approval authority for State 03 baseline and gate decisions.
6. Repository merge authority does not equal architecture approval authority.

## Critical Domains Requiring Specialist and Human Review

- Tenant Architecture
- Identity and Access Architecture
- Security Architecture
- Data Governance, Privacy and Compliance
- Data and Database Architecture
- Accounting and Thai Tax controls
- Infrastructure Architecture
- Deployment, DevSecOps and Release
- Business Continuity, Backup and Disaster Recovery

## Conflict Rule

For State 03 architecture work, this RACI supersedes conflicting role descriptions in older role directories after merge and approval. General project roles outside State 03 remain unchanged unless separately approved.
