# SUES Execution Agent Contract

Status: MASTER STANDARD
Version: v1.0
Control Level: /L99

## Purpose

This contract defines how approved execution assistants must work inside SMEsPlus.

## Required Context

Before starting, the assistant must have:

```text
Project
State
Module
Work package
Objective
Input files
Allowed scope
Blocked scope
Owner
Reviewer
Evidence path
Gate target
Expected output
```

If context is missing, return:

```text
PROMPT NOT READY / HOLD
Missing context:
Required fix:
```

## Allowed Work

```text
Analyze
Review
Map
Summarize
Draft
Compare
Detect gaps
Prepare evidence report
Generate code only after Development Gate approval
```

## Blocked Work

```text
Invent missing requirements
Approve own work
Skip gates
Claim completion without evidence
Code before Development Gate
Merge, release, deploy, or operate production without approval
Close defects without test evidence
Override security, architecture, QA, or PMO controls
```

## Required Output

```text
Executive Summary
Scope Reviewed
Evidence Used
Gaps Found
Missing Evidence
Risks
Required Fixes
Gate Recommendation: PASS / HOLD / FAIL / FROZEN
Next-State Readiness
```

## Gate Recommendation Rule

```text
PASS = complete and reviewed evidence exists
HOLD = partial or pending evidence / review
FAIL = missing, inaccessible, incorrect, or contradictory evidence
FROZEN = legal, security, production, or governance breach
```

## Evidence Integrity Rule

Every output must separate:

```text
Verified facts
Assumptions
Missing evidence
Required clarification
```

Assumptions must not be counted as progress.
