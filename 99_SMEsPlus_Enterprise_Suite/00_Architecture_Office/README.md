# 00 Architecture Office

Document ID: SMEPLUS-ARCH-OFFICE-README-v0.1
Project: SMEsPlus Enterprise Suite
Status: Approved for Execution
Owner: Architecture Office (ChatGPT)
Approved by: CEO / Product Owner
Branch: SMEsPlus

## Purpose

This folder is the official Architecture Office control area for SMEsPlus Enterprise Suite.

Architecture Office owns the architecture baseline, functional design control, business rule review, review gates, ADR, standards, and design patterns before work is released to PMO Office (Jira) and Engineering Office (Claude).

## Approved Folder Structure

```text
00_Architecture_Office/
├── ADR/
├── Enterprise_Standards/
├── Review_Checklists/
├── Governance/
├── Decision_Log/
├── Reference_Architecture/
└── Design_Patterns/
```

## Control Flow

```text
CEO / Product Owner
        |
        v
Architecture Office (ChatGPT)
        |
        v
PMO Office (Jira)
        |
        v
Engineering Office (Claude)
        |
        v
GitHub Repository
```

## Architecture Office Scope

Architecture Office controls:

- Enterprise Architecture
- Functional Design
- Business Rules
- Review Gates
- ADR
- Reference Architecture
- Design Patterns
- Architecture Review Gate (ARG)

## Mandatory Rule

No ARG Pass = No Claude Development.

Every Epic or Feature must pass Architecture Review Gate before Claude implementation starts.

## Current Approved Process

The approved process is documented in:

- `Governance/ARCHITECTURE_REVIEW_GATE.md`
- `Review_Checklists/ARG_CHECKLIST.md`

## Status

Approved for controlled execution.
