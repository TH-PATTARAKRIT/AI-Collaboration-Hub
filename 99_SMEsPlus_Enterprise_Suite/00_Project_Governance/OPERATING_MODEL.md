# SMEsPlus Operating Model

Document ID: SMEPLUS-OPERATING-MODEL-v0.1
Project: SMEsPlus Enterprise Suite
Branch: SMEsPlus
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Status: Approved for Execution
Approved by: CEO / Product Owner
Control Rule: Markdown is the Single Source of Truth. PDF is publication output only.

## 1. Purpose

This document defines the official working structure for SMEsPlus Enterprise Suite.

The objective is to prevent update drift between ChatGPT, Jira, Claude, and GitHub by enforcing one controlled operating flow:

CEO / Product Owner -> Architecture Office (ChatGPT) -> PMO Office (Jira) -> Engineering Office (Claude) -> GitHub Repository

## 2. Approved Operating Structure

```text
CEO / Product Owner
          |
          v
Architecture Office (ChatGPT)
          |
          +-- Enterprise Architecture
          +-- Functional Design
          +-- Business Rules
          +-- Review Gates
          +-- ADR
          |
          v
PMO Office (Jira)
          |
          +-- Epic
          +-- Story
          +-- Task
          +-- Sprint
          +-- Progress
          |
          v
Engineering Office (Claude)
          |
          +-- Code
          +-- Unit Test
          +-- Refactor
          +-- Technical Notes
          |
          v
GitHub Repository
```

## 3. Office Responsibilities

### 3.1 CEO / Product Owner

Owns business decision, approval, priority, product direction, and final acceptance.

Authority:

- Approves project direction
- Approves product scope
- Approves gate movement
- Approves production readiness
- Resolves conflicts and escalation

### 3.2 Architecture Office (ChatGPT)

Owns architecture, functional design, business rules, traceability, review gates, and ADR control.

Responsibilities:

- Maintain Enterprise Architecture
- Maintain Functional Design
- Maintain Business Rules
- Maintain Review Gate criteria
- Maintain ADR records
- Review documents before Jira execution
- Confirm Requirement ID, Business Rule, API, Screen, UAT, and Evidence mapping

Control Rules:

- No Requirement ID = No Jira Task
- No Business Rule = No Implementation
- No Traceability = No Gate Pass
- No Review Evidence = No Done

### 3.3 PMO Office (Jira)

Owns execution tracking and work control in Jira.

Responsibilities:

- Create and maintain Epic / Story / Task / Sprint
- Track status and progress
- Record blockers
- Record owner and assignee
- Record evidence links
- Track gate status
- Keep Jira aligned with Markdown source

Control Rules:

- Jira status must reflect evidence-based progress
- Jira Done requires UAT or review evidence
- Jira Blocked requires blocker type and next action
- Claimed progress and evidence-based progress must remain separated

### 3.4 Engineering Office (Claude)

Owns technical implementation under controlled Jira and GitHub scope.

Responsibilities:

- Code implementation
- Unit test
- Refactor
- Technical notes
- Implementation handoff
- Prepare pull request evidence

Control Rules:

- Claude execution must reference Jira issue key
- Claude task must reference Functional Requirement or Technical Requirement
- No Jira Task = No Claude Execution
- No Review Gate = No Production

### 3.5 GitHub Repository

GitHub is the controlled source repository for Markdown source, code, technical notes, and implementation evidence.

Responsibilities:

- Store Markdown source documents
- Store architecture and functional design baselines
- Store implementation work
- Store technical notes
- Maintain branch and PR control

Control Rules:

- Branch: SMEsPlus
- Markdown is Single Source of Truth
- PDF is publication output only
- All important changes must be traceable to Jira and/or approved document ID

## 4. Update Control Policy

To prevent update drift, the following update sequence must be followed:

1. Architecture Office updates or reviews Markdown source.
2. PMO Office creates or updates Jira from approved Markdown.
3. Engineering Office executes only Jira-approved work.
4. Engineering Office commits work to GitHub.
5. Architecture Office reviews output and gate evidence.
6. PMO Office updates Jira status based on evidence.

## 5. Source of Truth Rule

| Artifact | Role |
|---|---|
| Markdown in GitHub | Single Source of Truth |
| Jira | Execution tracking and status control |
| Claude output | Engineering execution output |
| PDF | Publication / review output |
| ChatGPT review | Architecture and gate control |

## 6. Gate Policy

A work item may move forward only when the required evidence exists.

Minimum gate criteria:

- Requirement ID exists
- Business Rule exists where applicable
- Screen / API / UAT mapping exists where applicable
- Jira issue exists
- Owner is assigned or clearly stated
- Evidence link or attachment exists
- Review result is PASS, HOLD, FAIL, or ACCEPTED WITH CONTROL

## 7. Jira Status Policy

| Status | Meaning |
|---|---|
| To Do | Work is created but not started |
| In Progress | Work is actively being executed |
| Done | Evidence is complete and review/UAT has passed |
| Blocked | Work is stopped by a named blocker |

Important rule: Description text such as READY, COMPLETE, or APPROVED does not override Jira workflow status.

## 8. Evidence Policy

No Evidence = No Progress.

Evidence must include at least one of:

- GitHub file path
- Jira attachment
- Google Drive link
- Screenshot
- Log file
- Test result
- Review note
- Pull request link

Evidence must also include:

- Owner
- Timestamp
- Verifier or reviewer
- Gate impact

## 9. Immediate Application to SaaS Foundation

This operating model applies immediately to SaaS Foundation Functional Design Specification v0.1.

Required next actions:

1. Convert SaaS Foundation FDS into Markdown source files.
2. Create Jira Epic and child issues based on FD-001 to FD-012.
3. Create review tasks for Architecture Review and Security Review.
4. Keep Claude implementation on HOLD until Foundation Review passes.
5. Track all updates through Jira and GitHub.

## 10. Current Approval

CEO / Product Owner has approved this working model and requested strict update control.

Execution Status: Approved for controlled execution.
