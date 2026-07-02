# GitHub Jira Synchronization Control

Document ID: SMEPLUS-GITHUB-JIRA-SYNC-CONTROL-v0.1
Project: SMEsPlus Enterprise Suite
Status: Approved for Execution
Approved by: CEO / Product Owner
Owner: Architecture Office (ChatGPT)
Tracking System: PMO Office (Jira)
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Branch: SMEsPlus
Root Path: 99_SMEsPlus_Enterprise_Suite

## 1. Purpose

This document defines the official synchronization process between GitHub Markdown source and Jira execution tracking for SMEsPlus Enterprise Suite.

The purpose is to prevent update drift, missing Jira updates, undocumented Claude execution, and evidence gaps.

## 2. Source of Truth

Markdown files in GitHub are the Single Source of Truth for architecture, functional design, business rules, standards, review gates, and AI handoff documents.

Jira is the execution tracking system.

Claude may execute only from approved Jira work items that reference GitHub source documents and pass required gates.

## 3. Operating Flow

```text
GitHub Markdown
    ↓
Architecture Office Review
    ↓
Jira Evidence / Status Update
    ↓
Architecture Review Gate
    ↓
Claude Handoff
    ↓
Engineering Output
    ↓
GitHub / Jira Evidence Update
```

## 4. Architecture Office Responsibility

Architecture Office (ChatGPT) is responsible for:

- Reviewing GitHub Markdown source updates
- Extracting document IDs, requirements, business rules, gates, and evidence references
- Mapping GitHub documents to Jira issues
- Posting Jira evidence comments
- Recommending Jira status updates based on evidence
- Blocking Claude execution when ARG is not passed
- Keeping GitHub and Jira aligned

## 5. Jira Update Rules

Jira must be updated when any of the following changes are detected in GitHub:

- New architecture document
- New functional specification
- New business rule document
- New review checklist
- New ARG result
- New Claude handoff standard or task prompt
- New traceability matrix
- New evidence file
- Updated gate policy
- Updated decision log

## 6. Required Jira Comment Format

```text
## GitHub Evidence Sync

Repository:
Branch:
Path:
Document ID:
Document Status:
Related Requirement ID:
Related Business Rule ID:
Related Gate:
Evidence Type:
Reviewer:
Review Date:

Finding:

Gate Impact:

Recommended Jira Action:

Claude Execution Permission: YES / NO / CONTROLLED
```

## 7. Status Update Policy

Jira workflow status must not be changed based on document text alone.

Required before Jira status change:

- GitHub path exists
- Document ID exists
- Evidence is openable or traceable
- Owner is identified
- Reviewer is identified
- Gate result is recorded
- Acceptance criteria or Done criteria is satisfied

## 8. Claude Release Rule

Claude may start only when Jira contains:

- Jira Issue Key
- Requirement ID
- Business Rule ID where applicable
- GitHub source path
- ARG result
- Reviewer
- Evidence reference
- Claude Execution Permission = YES or CONTROLLED

If any item is missing:

```text
Claude Development = HOLD
```

## 9. Batch Sync Mode

Architecture Office should avoid noisy small Jira updates.

Preferred update modes:

- Immediate update for gate-critical evidence
- Batch update for document indexing
- Daily sync summary for non-critical changes
- Executive sync report for Boss review

## 10. Gate Classification

| Result | Meaning | Jira Action |
|---|---|---|
| SYNC-PASS | GitHub evidence is complete and Jira can proceed | Update Jira evidence and recommend next status |
| SYNC-HOLD | Evidence exists but gate fields are incomplete | Add Jira comment and hold execution |
| SYNC-FAIL | Evidence missing or contradictory | Mark Jira as blocked or unresolved |
| SYNC-CONTROLLED | Partial evidence accepted with named control | Allow limited next step only |

## 11. Current Approval

CEO / Product Owner approved Architecture Office (ChatGPT) to own GitHub ↔ Jira synchronization for SMEsPlus.

Effective status: Approved for controlled execution.
