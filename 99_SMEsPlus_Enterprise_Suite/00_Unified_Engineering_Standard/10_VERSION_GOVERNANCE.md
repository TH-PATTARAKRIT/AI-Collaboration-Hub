# EOS Version Governance

Status: MASTER CONTROL  
Version: v1.0  
Control Level: /L99  
Owner: Technical PMO Director  
Reviewer: PMO Evidence Controller  
Evidence Path: 99_SMEsPlus_Enterprise_Suite/00_Unified_Engineering_Standard/10_VERSION_GOVERNANCE.md  
Gate Status: ACTIVE / CONTROLLED

## Purpose

This document defines how SMEsPlus standards, templates, registries, and operating procedures are versioned, reviewed, approved, baselined, superseded, or retired.

## Version Rule

```text
No Version = Invalid Document
No Change Reason = HOLD
No Reviewer = HOLD
No Evidence Path = HOLD
Unauthorized Version Change = FROZEN
```

## Version Format

```text
vMAJOR.MINOR.PATCH
```

| Level | Meaning | Approval Required |
|---|---|---|
| MAJOR | Structural change affecting state, module, AI, evidence, or gate behavior | Technical PMO Director + Strategic Delivery Lead |
| MINOR | New section, registry entry, template, workflow, or control table | PMO Evidence Controller + Owner |
| PATCH | Typo, clarification, non-structural correction | Owner + Reviewer |

## Document Status Model

| Status | Meaning | Allowed Use |
|---|---|---|
| DRAFT | Work in progress | Internal preparation only |
| REVIEW | Under reviewer inspection | No execution dependency |
| APPROVED | Approved for controlled use | May be used by teams and AI agents |
| BASELINE | Frozen foundation | Only approved correction allowed |
| SUPERSEDED | Replaced by newer version | Historical reference only |
| RETIRED | No longer valid | Do not use |
| FROZEN | Governance conflict or control issue | Stop related execution until decision |

## SUES Baseline Rule

SUES Foundation files 01 to 07 are set as BASELINE. EOS files 08 to 22 provide the operating control layer and may evolve under this version governance model.

## Required Version Record

Each version change must record Document ID, current version, new version, change type, change reason, owner, reviewer, approver, evidence path, gate impact, and approval date.

## Gate Impact

A version change that affects AI execution, state handoff, owner accountability, evidence requirements, or approval gates must be treated as a controlled change request under 11_CHANGE_CONTROL.md.
