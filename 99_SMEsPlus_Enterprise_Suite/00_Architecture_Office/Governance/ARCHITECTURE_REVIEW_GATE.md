# Architecture Review Gate (ARG)

Document ID: SMEPLUS-ARG-v0.1
Project: SMEsPlus Enterprise Suite
Status: Approved for Execution
Owner: Architecture Office (ChatGPT)
Execution Consumer: Engineering Office (Claude)
Tracking System: PMO Office (Jira)
Approved by: CEO / Product Owner

## 1. Purpose

Architecture Review Gate (ARG) is the mandatory review process before any Epic or Feature is released to Claude for development.

ARG prevents premature implementation by confirming that business, functional, data, integration, and quality readiness are complete enough for controlled engineering execution.

## 2. Mandatory Rule

No ARG Pass = No Claude Development.

Claude must not start code, unit test, refactor, or technical implementation unless the related Jira Epic or Feature has passed ARG or has been explicitly accepted with control.

## 3. Scope

ARG applies to:

- Epic
- Feature
- Functional Requirement group
- Architecture decision impacting implementation
- Cross-module design
- Data model change
- API or integration change
- Any Claude implementation work

## 4. ARG Gate Set

Every Epic or Feature must pass the following 5 gates.

### 4.1 Business Gate

Checks whether the requirement and business value are clear.

Minimum criteria:

- Business objective exists
- Business value is stated
- Scope is clear
- Owner is identified
- Priority is clear
- Requirement ID exists

Decision:

- PASS
- HOLD
- FAIL
- ACCEPTED WITH CONTROL

### 4.2 Functional Gate

Checks whether functional design is ready.

Minimum criteria:

- FDS section exists
- Functional Requirements are listed
- Business Rules are listed
- Workflow or process is clear
- Screen requirement is identified where applicable
- Exception path is identified where applicable

Decision:

- PASS
- HOLD
- FAIL
- ACCEPTED WITH CONTROL

### 4.3 Data Gate

Checks whether data readiness is sufficient.

Minimum criteria:

- Data model or entity list exists
- Master data impact is identified
- Tenant / company / branch scope is clear
- Traceability mapping exists
- Audit and evidence requirement is defined
- Data ownership is identified where applicable

Decision:

- PASS
- HOLD
- FAIL
- ACCEPTED WITH CONTROL

### 4.4 Integration Gate

Checks whether interface and dependency readiness is clear.

Minimum criteria:

- API requirement is identified where applicable
- Event or webhook requirement is identified where applicable
- External dependency is identified
- Internal module dependency is identified
- Error and retry rule is identified where applicable
- Security and permission impact is identified

Decision:

- PASS
- HOLD
- FAIL
- ACCEPTED WITH CONTROL

### 4.5 Quality Gate

Checks whether test and acceptance readiness is sufficient.

Minimum criteria:

- UAT case exists
- Acceptance Criteria exists
- Test data need is identified
- Evidence requirement is identified
- Review owner is identified
- Done criteria is clear

Decision:

- PASS
- HOLD
- FAIL
- ACCEPTED WITH CONTROL

## 5. Final ARG Result

Final ARG result is one of:

| Result | Meaning | Claude Action |
|---|---|---|
| ARG-PASS | All required gates pass | Claude may start implementation |
| ARG-HOLD | Missing information or evidence | Claude must wait |
| ARG-FAIL | Requirement or design is not acceptable | Claude must not start |
| ARG-ACCEPTED-WITH-CONTROL | Limited gaps accepted with named controls | Claude may start only within approved scope |

## 6. Required Jira Fields or Comment Template

Every Epic or Feature must include an ARG summary in Jira.

```text
ARG Result:
Business Gate:
Functional Gate:
Data Gate:
Integration Gate:
Quality Gate:
Final Architecture Decision:
Evidence Reference:
Reviewer:
Review Date:
Claude Execution Permission: YES / NO / CONTROLLED
```

## 7. Required Markdown Evidence

ARG evidence must reference Markdown source in GitHub wherever possible.

Minimum source references:

- FDS document path
- Requirement ID
- Business Rule ID
- API ID where applicable
- Screen ID where applicable
- UAT ID where applicable
- Traceability Matrix reference
- ADR reference where applicable

## 8. Operating Policy

1. Architecture Office reviews Epic or Feature.
2. Architecture Office records ARG result.
3. PMO Office updates Jira status and evidence.
4. Engineering Office receives only ARG-approved work.
5. Claude executes only Jira-approved scope.
6. GitHub stores implementation output and evidence.

## 9. Rejection Rules

Claude implementation must be blocked when:

- Requirement ID is missing
- Business Rule is missing where required
- FDS is missing or unclear
- Data ownership is unclear
- API or dependency is unclear
- UAT or Acceptance Criteria is missing
- Evidence cannot be traced

## 10. Status

ARG is approved for immediate use in SMEsPlus Enterprise Suite.
